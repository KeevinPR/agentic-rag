# A two-stage assignment strategy for the robust scheduling of dual-resource constrained stochastic job shop scheduling problems 

Shichang Xiao ${ }^{1}$, Zigao $\mathbf{W u}^{2}$, Shaohua $\mathbf{Y u}^{3}$<br>${ }^{1}$ Logistics Engineering College, Shanghai Maritime University, Shanghai 201306, China. E-Mail: scxiao@shmtu.edu.cn<br>${ }^{2}$ School of Mechanical Engineering, Northwestern Polytechnical University, Xi'an 710072, China. E-Mail: zgwu@mail.nwpu.edu.cn<br>${ }^{3}$ Laboratoire Génie Industriel, CentraleSupélec, Université Paris-Saclay, Paris 91190, France. E-Mail: shaohua.yu@centralesupelec.fr


#### Abstract

This paper addresses the job shop scheduling problems with stochastic processing times (SJSSP) under machine-worker dual-resource constraints. Considering the difference in worker's proficiency level, a robust scheduling approach is adopted. And then the machine-worker dual-resource constrained robust scheduling model of SJSSP based on the expected scenario of processing times (DR-SJSSP-EPS) is formulated. In view of the requirements of DR-SJSSP-ESP for the rational assignment of the workers, we propose a two-stage assignment strategy (TSAS), which can decrease the random disturbance of the processing times as well as its impact on the scheduling performance. Furthermore, a multi-objective hybrid estimation of distribution algorithm (MO-HEDA) is employed to solve the DRSJSSP-ESP. At last, the effectiveness of the proposed method to solve the DR-SJSSP-ESP in the job shop manufacturing system is verified according to the simulation results.


(C) 2019, IFAC (International Federation of Automatic Control) Hosting by Elsevier Ltd. All rights reserved.

Keywords: Job Shop Scheduling, Dual-Resource, Two-stage Assignment Strategy, Robust Scheduling.

## 1. INTRODUCTION

The uncertainties in a job shop manufacturing environment, such as random machine breakdown, shortage of tools or materials, the difference of worker's proficiency level, will lead to the randomness of realized processing times (Aytug et al., 2005). In order to ensure the stable and efficient execution of the schedule under the stochastic variation of processing times, it is needed to optimize the scheduling performance and reduce the potential influences of stochastic processing times on the scheduling performance simultaneously. Thereby, it is of great significance to study the job shop scheduling problems with stochastic processing times (SJSSP).
The robust scheduling, which requires the decision makers taking into account the possible stochastic disturbances on the scheduling performance, is an effective method to keep up with high performance and stay profitable for a job shop (Sabuncuoglu and Goren, 2009). With the development of intelligent sensors and internet of things manufacturing technologies, the statistical information of processing data in the production process can be effectively obtained. Which makes it possible to provide enabling technology for robust scheduling (Zhang et al., 2015, Wang et al. 2015). Therefore, the statistical data of the processing process can be used to assist the scheduling decision to obtain a scheduling solution with both good performance and robustness.
The workers are essential resources in the job shop. The proficiency level of the workers is a critical factor that affects
scheduling robustness. Actually, each worker has a different proficiency level in operating the same machine. Also, assigning a worker with higher proficiency to an operation can improve the stability of the operation and better ensure on-time completion (Abad et al., 2011). Therefore, utilizing the differences in the proficiency level of workers to make more reasonable task assignments can proactively reduce the disturbance of the stochastic processing time on an initial schedule. In addition, in order to improve scheduling flexibility and avoid the scheduling disorder due to the absence of some workers, the Job Shop manufacturing environment with multiple varieties and small batches usually requires one worker be competent to operate multiple machines (Li et al., 2016).
Therefore, considering the influence of worker assignments and modeling worker factors on the randomness of processing times have important theoretical and practical value for the robust scheduling of SJSSP with machineworker dual-resource constraints. In current research, the manufacturing systems constrained by both machines and heterogeneous workers are referred to as dual-resource constrained systems. Li et. al (2016) proposed a metaheuristic algorithm named Branch Population Genetic Algorithm to minimize the makespan and cost. Mencia et al. (2013) proposed a genetic algorithm to minimize the makespan of Job Shop Scheduling Problems (JSSP) with operator constraints. However, the dual-resource constrained scheduling problems with deterministic or finite compressible processing times do not consider the constraints of processing

time randomness and the proficiency difference of workers in the job shop manufacturing environment.
Robustness evaluation is the basis for the implementation of robust scheduling methods. Wu et al. (1999) proposed a graph theory-based decomposition method to achieve scheduling robustness and adopted the expected average weighted tardiness as a robustness measure for SJSSP. However, using the expected performance as the robustness measure only gives a performance expectation under the disturbance, it cannot provide an evaluation value of the influence degree of the random disturbance on the performance. When an initial scenario of the processing times is given, the schedule performance under the initial scenario and the robustness under the influence of processing time disturbance can both be evaluated. Thereafter, a Pareto optimization method can be employed to obtain a Pareto solution set with both performance and robustness.
In view of the randomness of processing time in actual discrete manufacturing systems and the demands for machine-worker collaborative scheduling in an actual manufacturing system, this paper studies the robust scheduling of SJSSP with machine-worker dual-resource constraints. First, the model of dual-resource constrained SJSSP based on the expected scenario of processing times (DR-SJSSP-ESP) is formulated. Second, the formulations are provided to evaluate the relationship between the worker's proficiency and the randomness of processing times, and then a two-stage machine-worker assignment strategy (TSAS) is proposed. Furthermore, a multi-objective hybrid estimation of distribution algorithm (MO-HEDA) is provided to solve the DR-SJSSP-ESP. Finally, the effectiveness of MO-HEDA, solving the actual Job Shop robust scheduling problem based on the heuristic, is verified.

## 2. MATHEMATIC MODELING

### 2.1 Problem description

The DR-SJSSP-ESP is an extended form of the classic JSSP. DR-SJSSP-ESP is described as follows: there are $n(i=1,2, \ldots n)$ jobs need to be processed on $m(j=1,2, \ldots, m)$ machines; there are $W(r=1, \ldots, W ; W \leq m)$ workers who can operate the $m$ machines; each machine can only process one job at a time; the same job can only be processed on one machine at a time; the same worker can only operate one machine at a time; the process is not allowed to be interrupted; all materials and machines are available at time 0 ; preemption is not allowed; the starting time of each job cannot earlier than its planned time.
In the scheduling process under the dual-resource constraints, the processing time of the worker in one operation is determined by the expected processing time. Besides, the realized machine operation time is not greater than its initial processing time. Moreover, in view of the tool wear, resource shortage, worker fatigue, etc., it is more likely to cause the random deterioration of processing time. Therefore, the stochastic processing time is estimated by $\xi T_{i j}=\mu_{i j}+\varepsilon_{i j}$, in which $\xi T_{i j}$ denotes the realized processing time, $\mu_{i j}$ denotes
the expected processing time, and $\varepsilon_{i j}\left(\varepsilon_{i j} \geq 0\right)$ represents the value of disturbance. Meanwhile, in the manufacturing environment, different workers have different proficiency level even they operate the same machine. Thereafter, assigning workers to their skilled operation can reduce potential disturbances on the initial processing time.
By considering the difference in worker proficiency level and the workers' proactive control on the randomness of processing time, as well as through the reasonable worker assignment, we can achieve proactively reducing the randomness of processing time. Due to the introduction of the difference in worker proficiency and the shortage of workers, the robust scheduling of DR-SJSSP-ESP needs to solve two problems: (1) How to proactively reduce the randomness of processing time by using the difference in worker proficiency? (2) How to allocate a limited number of workers to minimize the impact of the worker constraints on the scheduling performance?

### 2.2 Mathematical modeling of DR-SJSSP-ESP

The model is described by $.J m \mid \mathrm{SPT}, \mathrm{DR} \mid\left(C_{\max }^{c}, R M\right)$. $J m$ denotes the job shop environment, SPT denotes the stochastic processing time, DR denotes the dual-resource constraints, $C_{\max }^{c}$ denotes the scheduling performance measure, i.e., makespan, $R M$ denotes the robustness measure. The DR-SJSSP-ESP is illustrated as follows. The objective function is shown in (1)

$$
\min _{S \in \Omega} F(S)=\left[C_{\max }^{c}(S), R M(S)\right]
$$

In the objective function, $C_{\max }^{c}(S)$ is obtained by (2) using the expected scenario of the processing time, and $R M(S)$ is then evaluated by (3).

$$
\begin{gathered}
C_{\max }^{c}(S)=\max C_{i j}^{c}, \forall i, j \\
R M(S)=\frac{1}{L} \sum_{l=1}^{L}\left[C_{\max }^{l}(S)-C_{\max }^{c}(S)\right]
\end{gathered}
$$

In (3), the value of $C_{\max }^{l}(S)$ is evaluated by (4). In (4), $\xi$ is an index of the stochastic variable, and $C_{\max }^{l}(S)$ represents the stochastic makespan under a group of stochastically realized scenario.

$$
C_{\max }^{l}(S)=\max \xi C_{i j}^{l}, \forall i, j
$$

The constraints of DR-SJSSP-ESP are listed as follows.

$$
\begin{gathered}
\sum a_{i j k}=1, \forall i, j, k \wedge j \neq k \\
\sum x_{i k k}=1, \forall i, h, k \wedge i \neq h \\
\sum_{j=1}^{m} Y_{i j W r}=1, \forall i, j, r \\
\xi C_{i k}-\xi T_{i k}+M_{0}\left(1-a_{i j k}\right) \geq \xi C_{i j} \\
\forall i, j, k \wedge j \neq k \\
\xi C_{h j}-\xi T_{h j}+M_{0}\left(1-x_{i h j}\right) \geq \xi C_{i j} \\
\forall i, h, j \wedge i \neq h
\end{gathered}
$$

$$
\begin{gathered}
\xi T_{i k W r}^{\prime \prime \prime}=\max \left\{\xi T_{i j W r}^{\prime \prime}+T_{i j W r}^{\prime \prime}, \quad \xi S T_{i k}\right\} \\
\forall i, j, k, r
\end{gathered}
$$

The Equation (5) denotes that one job $J_{i}$ can only be processed on one machine $M_{j}$ or $M_{k}, a_{i j k}=1$ or $a_{i j k}=0$; (6) denotes that one machine $M_{k}$ can only process one job $J_{i}$ or $J_{h}, x_{\text {ih }}=1$ or $x_{\text {ih }}=0$; (7) denotes that one worker $W r$ can only operate one operation $O_{i j}$ at the same time, $Y_{i j W r}=1$ or $Y_{i j W r}=0$; (8) is the process constraints, which means job $J_{i}$ only can be processed on machine $M_{h}$ after machine $M_{j}$ completed the operation, $M_{i j}$ is a big enough positive integer; (9) denotes the machine constraints, which means the job $J_{h}$ can only be processed on machine $M_{j}$ after the precedence job $J_{i}$ has been completed; in (10), $T_{i j W r}^{\prime \prime}$ denotes the deterministic operating time of the worker $W r$ which is decided according to the initial processing time scenario, (10) means that the worker $W r$ can only start the operation $O_{i k}$ on machine $M_{k}$ after the operation $O_{i j}$ on machine $M_{j}$ has been completed.

## 3. A TWO-STAGE ASSIGNMENT STRATEGY

3.1 Processing time variance reduction model based on worker proficiency
In order to accurately describe the processing time variance reduction model based on worker proficiency, this section first provides the definitions that required to describe the method. Furthermore, a model establishing the relationship between worker proficiency and processing time variance is presented. Thus, we can evaluate the degree that the worker's proficiency influences the variance reduction of the processing time.
Proficiency level The proficiency measure of a worker operating a machine to process operation is called proficiency level, denoted by $p f_{i j}^{\prime \prime} \in[0,1]$.
The variance determination coefficient The maximum proportion of the influence of worker proficiency on processing time variance, denoted by $\eta_{i j}^{r} \in[0,1]$.
The coefficient of variance reduction The proportion of the variance reduction of processing time under the influence of worker proficiency, denoted by $\Delta c v_{i j W r}, \Delta c v_{i j W r} \in\left[0, \eta_{i j}^{r}\right]$.
A processing time variance reduction model, based on worker proficiency, can be established according to the following method.
Step 1. Given the values of the workers' proficiency level The range of proficiency level is $p f_{i j}^{\prime \prime} \in[0,1]$,i.e., if $p f_{i j}^{\prime \prime}=0$, the worker $W r$ cannot operate the corresponding machine that machining the operation $O_{i j}$; if $p f_{i j}^{\prime \prime}=1$, the worker can reduce the processing time variance according to the maximum value of the variance determination coefficient.
Step 2. The normalization of proficiency level
According to the definition of the variance determination coefficient, when the worker's proficiency level is $p f_{i j}^{\prime \prime}=1$, the corresponding coefficient of variance reduction is $\eta_{i j}^{r}$. In order to establish a functional relationship between the work's proficiency level and the coefficient of variance reduction of the processing times, the proficiency of the
workers needs to be normalized. If a worker $W r$ operates an operation $O_{i j}$ with the proficiency level $p f_{i j}^{\prime \prime}$, the normalized proficiency level $\operatorname{Normp} f_{i j}^{\prime \prime}$ can be calculated by (11)

$$
\operatorname{Normp} f_{i j}^{\prime \prime}=\frac{p f_{i j}^{\prime \prime}-p f_{\min }}{p f_{\max }-p f_{\min }}
$$

where $p f_{\text {min }}$ and $p f_{\text {max }}$ denotes the minimum and maximum of the proficiency level.
Step 3. Establish the functional relationship between the coefficient of variance reduction and proficiency level.
The functional relationship between the proficiency level and the coefficient of variance reduction is a monotonically increasing function that is positively correlated with the proficiency level, and its range is $[0,1]$. To simplify the modeling process, this study uses the function of proficiency level to estimate the coefficient of variance reduction of the processing time. The function relationship is shown in (12)

$$
\begin{aligned}
\Delta c v_{i j W r} & =f\left(p f_{i j}^{\prime \prime}\right)=\eta_{i j}^{r}\left(\operatorname{Normp} f_{i j}^{\prime \prime}\right)^{2} \\
& =\eta_{i j}^{r}\left(\frac{p f_{i j}^{\prime \prime}-p f_{\min }}{p f_{\max }-p f_{\min }}\right)^{2}
\end{aligned}
$$

Step 4. Calculate the variance of processing time that is affected by the work's proficiency.
The variance of processing time decreases as the worker's proficiency increases. It is calculated by (13)

$$
\operatorname{Var}_{i j}^{\prime \prime}=\left(1-\Delta c v_{i j W r}\right) \sigma_{i j}^{2}
$$

When considering the influence of worker proficiency level on the variance of processing time, the variance is evaluated by equations (11) to (13).
3.2 A two-stage assignment strategy based on worker proficiency and workload balancing
We provide an approach involving two stages to assigning the machine and worker resources in the job shop environment. The first stage determines the sequence of the jobs on the machines. Besides, the second stage minimizes the influence of worker insufficiency on makespan, by assigning workers according to the its availability constraints. The procedures of the assignment method are briefly described as follows.
Step 1. Sorting the jobs on the machines.
Step 2. Assigning the workers to the machines based on the proposed assignment strategy;
Step 3. Save the sequences of the jobs on the machines and the sequence of the workers.
Assigning the most proficient workers to the corresponding operation can minimize the total disturbance amount in the scheduling scheme, which is beneficial to improve the scheduling robustness of the DR-SJSSP-ESP. Thereafter, we first give a proficiency priority based worker assignment strategy, which is represented by TSAS1.
TSAS1 For a given operation, selecting the most proficient worker in the set of alternative workers $\mathbf{M}_{j}^{W}$ by the policy of $\max p f_{i j}^{\prime \prime}, \forall i, j, r=1, \ldots, K$.
Using TSAS1 can minimize the processing time variance for each operation. However, when workers are consecutively assigned to become constrained resources, the degree of deterioration of makespan also increases. Assume that when the set of available workers $\mathbf{M}_{j}^{W}$ including $W r$ for two

consecutive operations, the extreme situation is that the same worker will be continuously selected. In the worst case, all the operations will be are assigned to the same worker. Thus, the makespan can be equal to the sum of the processing time of all the operations. This will also cause the remaining workers to be idle. Hence, it is vital to consider workload balance of the workers.
TSAS2 First, assign a worker $W r$ to an operation by TSAS1 and then determine whether the worker included in the candidate workers set $\mathbf{M}_{j^{\prime}}^{W}$ of the succeeding operation. If not, continue to assign the worker according to TSAS1. If the worker $W r$ is still included, determine whether the $p f$ value is still the biggest. Then, the worker whose proficiency value second only to the worker is selected.
In the existing research, the workers are usually coded along with the sequence of the jobs, and the decoding process is equivalent to randomly assigning available workers to each operation (Li et al., 2016). Further, the scheduling decisions are made by evaluating the performance of the schedule solutions under different machine-worker combinations. This paper defines the strategy that the workers to be randomly assigned as TSAS3.
TSAS3 According to the available workers set $\mathbf{M}_{j}^{W}$ of an operation, a uniform distribution is used to randomly assigning an worker $W r$ to the operation $O_{i j}$.

## 4. ALGORITHM

In order to solve the DR-SJSSP-ESP, a multi-objective HEDA, based on the non-dominated sorting, is proposed. For the detail procedures of HEDA please refer to Xiao et al. (2017). Deb et al. (2002) described the NSGA-II for multiple decision making and multi-objective optimization problems. The framework of MO-HEDA is shown as Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. The framework of MO-HEDA

The first step is to set the parameters, and then the probability matrix for sampling the initial individuals is initialized. The third step is thus executed to generate new solutions. In the fourth and the fifth step, the recombination and mutation process is executed respectively to enhance the population diversity. Thereafter, the workers are assigned by using TSAS in the sixth step. Then, in the selection process, the individuals for updating the probability model are selected by using NSGA-II, in which the RM is evaluated by simulating the stochastic processing scenarios via the Monte Carlo simulation method. In the eighth step, the elite Pareto solutions are saved for the next iteration to estimate the probability distribution of the operations and then update the probabilistic model. At last, if the termination condition is satisfied, the algorithm ends the iteration and saves the optimal Pareto front.

## 5. SIMULATION EXPERIMENTS

The MO-HEDA and TSAS are coded in the Matlab 2015b. The algorithm execution platform is a Lenovo brand PC with a hardware configuration of Intel(R) Xeon(R) CPU E31230 @ 3.2 GHz, RAM 8.00 GB . In order to reduce the computational burden of the simulation experiment and ensure satisfactory optimization performance, we set the population size and evolution generation to 200 , and the simulation times of the processing time scenario to 100 . Then we use the Taguchi's method (Montgomery, 1976) to select a set of key parameters of MO-HEDA, which are $P_{e}=0.8$, $\alpha=0.3, B_{\text {size }}=40$.
First, the performance comparison of the TSAS1, TSAS2, and TSAS3 is conducted. The Set Coverage (SC) is adopted as the evaluation criteria. We modified the benchmarks of JSSP, i.e., FT06, FT10 and FT20 (Muth and Thompson, 1963) to the DR-SJSSP-ESP instances. To differentiate from the classic JSSP benchmarks, the modified benchmarks are named FT06_DR, FT10_DR, and FT20_DR, respectively. The total number of workers is set to $0.7 m, m$ is the total number of machines. Let $A$ and $B$ be two Pareto solution sets, the set coverage $S C(A, B)$ is defined as the percentage of the solutions in set $B$ are dominated by at least one solution in Pareto solution set $A$, as shown in (14).

$$
S C(A, B)=\frac{|\lfloor x \in B| \exists y \in A: y \prec x\rfloor|}{|B|} \times 100 \%
$$

Three benchmarks are solved 10 times using TSAS1, TSAS2, and TSAS3 by the MO-HEDA. The corresponding $S C$ values of the obtained Pareto solution set are shown in the Table 1.

Table 1. The $S C$ values of the three comparison TSAS

| Benchmarks | $S C(1,2)$ | $S C(2,1)$ | $S C(3,2)$ | $S C(2,3)$ |
| :--: | :--: | :--: | :--: | :--: |
| FT06_DR | $0.00 \%$ | $100 \%$ | $0.00 \%$ | $100 \%$ |
| FT10_DR | $63.95 \%$ | $98.75 \%$ | $29.07 \%$ | $100 \%$ |
| FT20_DR | $27.94 \%$ | $94.94 \%$ | $2.94 \%$ | $100 \%$ |
| Average | $30.63 \%$ | $97.89 \%$ | $10.67 \%$ | $100 \%$ |

In Table 1, $S C(1,2)$ and $S C(3,2)$ represent the dominance rate of TSAS1 and TSAS3 to the Pareto solution set of TSAS2, respectively. $S C(2,1)$ and $S C(2,3)$ represent the dominance rate of TSAS2 to the Pareto solution set of TSAS1 and

TSAS3, respectively. It can be seen from the table, for all the benchmarks, the $S C$ values of TSAS2 are higher than that of TSAS1. The overall mean values of $S C(1,2)$ and $S C(2,1)$ for the three modified benchmarks are $30.63 \%$ and $97.89 \%$, respectively, which indicates that TSAS2 has a better Pareto dominates performance than that of TSAS1. The set coverage of TSAS3 and TSAS2 shows the same result. The overall average $S C$ values of the Pareto solution sets of $S C(2,3)$ and $S C(3,2)$ are $100 \%$ and $10.67 \%$, respectively, indicating that the Pareto solution set obtained by TSAS2 has apparently Pareto dominates performance. The analysis results show that the proposed TSAS2 has the best Pareto optimization performance among the three comparison assignment strategies.
Second, a problem instance extracted from the manufacturing enterprise is employed. There are 8 jobs to be processed, which are typical aircraft engine parts. The given operation time of each worker is 0.8 times of the initial processing time. The six machine tools in the job shop are numbered respectively, including lathe $(M 1)$, milling machine $(M 2)$, planer $(M 3)$, grinding machine $(M 4)$, drilling machine $(M 5)$, and boring machine $(M 6)$. The sample mean and variance of the processing time of each process are obtained according to 50 sets of historical data of the processing time scenarios, including the operations of the 8 jobs. It is found that the stochastic processing times approximately follow the normal distribution. The corresponding machine information and processing time information (units/hour) are shown in Table 2 in the form of (machine, the expected processing time, the variance of the processing time).

Table 2. The processing information the 8 jobs

| Jobs | The number of operations |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 2 | 3 | 4 | 5 | 6 |
| J1 | $(1,4,0.75)$ | $(2,6,4.14)$ | $(3,4,0.60)$ | $(6,7,3.99)$ | $(5,9,2.34)$ | $(4,3,0.45)$ |
| J2 | $(2,5,0.96)$ | $(4,8,6.33)$ | $(6,6,1.02)$ | $(5,6,0.84)$ | $(1,7,0.45)$ | $(3,5,4.41)$ |
| J3 | $(6,5,3.72)$ | $(5,9,1.95)$ | $(1,4,0.15)$ | $(3,5,2.13)$ | $(4,7,3.72)$ | $(2,8,4.95)$ |
| J4 | $(4,4,0.36)$ | $(3,8,1.26)$ | $(5,6,0.99)$ | $(1,6,0.75)$ | $(2,5,3.33)$ | $(6,8,6.21)$ |
| J5 | $(3,7,0.69)$ | $(1,3,0.45)$ | $(4,6,1.95)$ | $(2,8,1.32)$ | $(6,4,2.16)$ | $(5,5,0.36)$ |
| J6 | $(1,4,0.33)$ | $(6,7,0.75)$ | $(2,5,0.21)$ | $(4,8,2.07)$ | $(5,5,1.02)$ | $(3,4,0.30)$ |
| J7 | $(5,3,1.74)$ | $(6,5,3.75)$ | $(4,3,0.99)$ | $(2,7,3.36)$ | $(3,3,1.44)$ | $(1,4,0.60)$ |
| J8 | $(1,5,0.39)$ | $(3,7,6.75)$ | $(2,6,2.49)$ | $(6,5,4.05)$ | $(5,8,3.18)$ | $(4,3,1.20)$ |

The workers have the ability to operate multiple machine tools after be trained. Each machine needs to ensure that at least two workers can operate to improve the flexibility of worker assignment under the shortage of workers. In this instance, 4 workers operate 6 machine tools to complete the tasks. The available worker information for each machine is shown in Table 3.

Table 3. The available workers of the machines

| The available workers of the machines |  |
| :--: | :--: |
| Machine | The workers' number |
| M1 | $W 1, W 3, W 4$ |
| M2 | $W 1, W 2, W 4$ |
| M3 | $W 1, W 2, W 3$ |
| M4 | $W 2, W 3, W 4$ |
| M5 | $W 2, W 3, W 4$ |
| M6 | $W 2, W 3, W 4$ |

If the worker's proficiency on one operation reaches 0.8 , it fulfills the quality requirement, and when the proficiency is 1 ,
the operation will be finished within the given processing time with the best quality. In the problem instance, the proficiency of the workers working on different operations machine is randomly generated from the range of $[0.8,1]$ by a uniform distribution.
The TSAS2 is adopted and combined with the MO-HEDA to solve the problem instances since it has the lower probability to increase the makespan. The CPU time is 6732 seconds according to the simulation results. The obtained Pareto front contains seven Pareto solutions, and the corresponding objective values are $(66,6.86),(67,5.36),(68,4.14),(69$, $3.67),(71,2.89),(72,2.67)$ and $(73,2.43)$, respectively, as shown in Fig. 2.
![img-2.jpeg](img-2.jpeg)

Fig. 2. The Pareto solution front obtained by the simulation
A scheduling solution includes two parts: the sequence of the jobs on the machines and the order for workers assigned to the machines. For example, the makespan of the solution (67, 5.36 ) is 67 hours without considering the disturbance. When the scheduling solution is executed, the robustness value under the influence of the expected disturbance is 5.36 hours. The Gantt chart of the solution is shown in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Fig. 3. The schedule solution with the objective values of $(67,5.36)$
In Fig. 3, the (a) represents the order of the jobs on each machine, the (b) represents the order of the workers assigned

to each operation. Since there is no effective method for the manufacturing enterprise to solve the robust scheduling problem under machine-worker dual-resource constraints, it is impossible to evaluate the robustness of the realized schedule solution. as a comparison experiment, TSAS2 will be incorporated into HEDA (Xiao et al., 2017), and then the HEDA is adopted to solve the problem instance with the expected scenario of the processing times. The simulation result shows that the makespan of the schedule solution is 66 hours, and the expected deviation of makespan during actual execution is 7.12 hours. The data of the existing scheduling method and the robust scheduling results based on DR-SJSSP-ESP are shown in Table 4.

Table 4 The results comparison

|  |  | Makespan | RM | Percentage |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| The existing schedule solution |  | 66 | 7.12 | Makespan decrease(\%) | Robustness increase(\%) |
| TSAS2 <br> based <br> MO- <br> HEDA | Solution 1 | 66 | 6.86 | 0.00 | 3.65 |
|  | Solution 2 | 67 | 5.36 | 1.52 | 24.72 |
|  | Solution 3 | 68 | 4.14 | 3.03 | 41.85 |
|  | Solution 4 | 69 | 3.67 | 4.55 | 48.46 |
|  | Solution 5 | 71 | 2.89 | 7.58 | 59.41 |
|  | Solution 6 | 72 | 2.67 | 9.09 | 62.50 |
|  | Solution 7 | 73 | 2.43 | 10.61 | 65.87 |

From the data in Table 4, using the DR-SJSSP-ESP and the TSAS2 based MO-HEDA, the robustness can be significantly improved by sacrificing a small amount of makespan. Taking the solution 6 as an example, sacrificing $9.09 \%$ of makespan yields $62.5 \%$ robustness improvement. Moreover, according to the analysis, the Pareto solutions can be provided to the decision makers under an insufficient number of workers. Meanwhile, the expected value of the actual makespan deviation under the influence of the potential processing times disturbance is given along with the makespan.

## 6. CONCLUSIONS

This section summarized the contributions of this paper. First, a machine-worker dual-resource constrained robust scheduling model for the job shop scheduling problems was formulated. Second, a two-stage assignment strategy based on the worker proficiency and workload balancing was provided, which can minimize the random disturbances of the processing times and reduces its impact on the makespan. Third, the Pareto solutions can be provided to the decision makers by using the TSAS2 based MO-HEDA. According to the simulation results, it is concluded that the proposed TSAS2 has the best Pareto optimization performance. Also, the DR-SJSSP-ESP can effectively increase the robustness with a small amount sacrifice of makespan according to the analyzing of the simulation results.

## ACKNOWLEDGMENTS

The authors are grateful to the referee for providing us with valuable revision suggestions. The authors would also like to acknowledge the financial support from the Natural Science Foundation of China under Contract Number 51775435.

## REFERENCES

Aytug, H., Lawley, M.A., McKay, K., Mohan, S., and Uzsoy, R. (2005). Executing production schedules in the face of uncertainties: A review and some future directions. European Journal of Operational Research, 161(1), 86110 .
Abad, A., Paynabar, K., \& Jin, J., 2011. Modeling and analysis of operator effects on process quality and throughput in mixed model assembly systems. Journal of manufacturing science and engineering. 133(2): 021016.

Deb, K., Pratap, A., Agarwal, S., and Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE Transactions on Evolutionary Computation, 6(2), 182-197.
Li, J., Huang, Y., Wang, J.. (2016) Scheduling strategy of dual resource constrained job shop based on compressed time window [J]. Computers Integrated Manufacturing Systems, 12, 2827-2835.
Li, J., Huang, Y., and Niu, X. (2016). A branch population genetic algorithm for dual-resource constrained job shop scheduling problem. Computers \& Industrial Engineering, 102, 113-131.
Mencía, R., Sierra, M.R., Mencía, C., and Varela, R. (2013). A genetic algorithm for job-shop scheduling with operators enhanced by weak Lamarckian evolution and search space narrowing. Natural Computing, 13(2), 179192.

Montgomery, D. C. (1976). Design and Analysis of Experiments: J. Wiley.
Muth, J.F.; Thompson, G.L. Industrial Scheduling; PrenticeHall: Upper Saddle River, NJ, USA, 1963.
Sabuncuoglu, I., and Goren, S. (2009). Hedging production schedules against uncertainty in manufacturing environment with a review of robustness and stability research. International Journal of Computer Integrated Manufacturing, 22(2), 138-157.
Wang, L., Törngren, M., and Onori, M. (2015). Current status and advancement of cyber-physical systems in manufacturing. Journal of Manufacturing Systems, 37, 517-527.
Wu, S.D., Byeon, E.S., and Storer, R.H. (1999). A GraphTheoretic Decomposition of the Job Shop Scheduling Problem to Achieve Scheduling Robustness. Operations Research, 47(1), 113-124.
Xiao, S., Sun, S., and Jin, J. (2017). Surrogate Measures for the Robust Scheduling of Stochastic Job Shop Scheduling Problems. Energies, 10(4), 543.
Zhang, Y., Zhang, G., Wang, J., Sun, S., Si, S., and Yang, T. (2015). Real-time information capturing and integration framework of the internet of manufacturing things. International Journal of Computer Integrated Manufacturing, 28(8), 4059-4063.