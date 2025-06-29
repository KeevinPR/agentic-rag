# An Adaptive Sampling-Estimation of Distribution Algorithm for Robust Scheduling in the Steelmaking-Continuous Casting Process* 

Sheng-long Jiang, Member, IEEE, and Qie Liu, Member, IEEE


#### Abstract

Uncertainty is an important feature of industrial systems, and it extensively exists in the steelmaking industry. This paper focuses on the uncertain scheduling problem arising from the steelmaking-continuous casting (SCC) process. Based on the Benders decomposition strategy, the SCC scheduling problem (SCCSP) is decomposed into two sub-problems: the machine allocation problem (MAP) and the timetabling problem (TTP). To solve the uncertain SCCSP with interval processing times, an estimation of distribution algorithm (EDA) combined with robust optimization (RO) is proposed. First, a novel EDA with multiple probabilistic models and adaptive sampling policy is developed to solve the MAP. Second, the RO approach with ellipsoidal sets is embedded in the EDA and used to solve the TTP. To verify the proposed algorithm, a number of instances are generated from real-world industrial data. The final simulation results show that the proposed algorithm is efficient and effective to solve the uncertain SCCSP with interval processing times.


![img-0.jpeg](img-0.jpeg)

Fig. 1. The flow diagram of SCC process
The steelmaking-continuous casting (SCC) process is one of the critical components in an integrated iron and steel company, in which the high-temperature hot metal is transformed into solidified slabs by sequentially visiting the steelmaking, refining and casting stage (as shown in Fig. 1). The main task of its production scheduling is assigning all jobs on the machines in each stage, and achieving the target of cost saving and efficiency promotion. Therefore, the scheduling decision plays an important role in production management of the SCC process. However, considering the physical and

[^0]chemical conditions during processing (e.g. temperature and element composition), the SCC scheduling problem (SCCSP) is always identified as a hybrid flow shop scheduling problem with complex constraints and a NP-hard problem [1].

In real-world production environments, affected by quality fluctuation, machine status, worker experience and other unknowable factors, there exist some uncertainties to define the parameters of SCCSP. Therefore, the solutions output by the deterministic SCCSP often suffer from performance deterioration or infeasibility. Moreover, if the executing solution is affected by uncertain factors, frequent repairing or rescheduling may reduce the stability of the SCC production, even affect product quality. Therefore, a robust scheduling approach is very crucial for SCC process to improve stability and quality.

Since the middle of 1990s, the SCCSP under uncertain environments has gained extensive attentions from industrial to academic fields. Dorn et al. [3] developed a trapezoidal fuzzy numbers-based model for the uncertain SCCSP, and used a heuristic method to construct an initial solution. During the execution of the initial solution, if its satisfaction criterion seriously deviated from the anticipated value, they proposed a tabu search algorithm to repair the infeasible solution. With the multi-criteria model with fuzzy constraints, Slany [4] proposed an hybrid algorithm combined a fuzzy constraint satisfaction and a local search. Considering uncertainties of processing times and arrival times in the SCCSP, Sun et al. [5] developed a stochastic dynamic programing to solve the sub-problems decomposed by the Lagrangian relaxation policy. Considering operation delays in the realized solution, Yu and Pan [6] constructed a multi-objective nonlinear programing model, and proposed a three-stage rescheduling algorithm including batch splitting, backward scheduling and forward scheduling method; Yu [7] proposed an event-driven mechanism to identify disturbances, and a reachability matrix for rescheduling. To make a trade-off between risks and costs for tackling uncertainties in the SCCSP, Jiang et al. [8, 9] introduced a characteristic indices-based "soft schedule", and proposed a two-stage estimation of distribution algorithm (EDA) and a prediction-based online scheduling algorithm. By analysis of starting time delay disturbance, Yu et al. [10] proposed a heuristic rescheduling algorithm to quickly react uncertain factors, which is able to make the schedule feasible and optimal.

EDA is a powerful evolutionary computation algorithm [11] based on the probabilistic model constructed by statistic or machine learning method. This paper studies the uncertain SCCSP with interval processing times, and proposes a robust scheduling approach based on a hybrid EDA. The remaining


[^0]:    *Resrach supported by the Fundamental Research Funds for the Central Universities, China (NO. 0903005203461).

    Sheng-long Jiang is with the School of materials science and engineering, Chongqing University, Chongqing, China (corresponding author, phone: +086-182-2323-5220; e-mail: jiang_ shli@cqu.edu.cn).

    Qie Liu is with the Department of Automation, Tsinghua University, Beijing, China (LiuQieBUCT@gmail.com)

content is organized as follows. In section II, the robust scheduling problem is formulated. In section III, a robust scheduling algorithm based on the hybrid EDA with roust optimization (RO) is proposed for solving the uncertain SCCSP. Finally, computational experiments are carried out to validate the effectiveness of the proposed algorithm.

## II. Problem Statement

The SCC process consists of $g$ stages $(g \geq 3)$, each of which has $m_{i}$ parallel machines $M_{i}=\left\{1, \cdots, k, \cdots, m_{i}\right\}$. The machines in $M_{i}(i<g)$ are identical, while these in $M_{g}$ are non-identical. The SCCSP can be described as follows: the charge (also called job) set $J=\{1, \cdots, j, \cdots, n\}$ which is grouped into a number of sorted casts (also called batches) $B=\{1, \cdots, b, \cdots, N\}$ is release to the shop floor. For the $b^{t h}$ cast, it is formed a sorted subset $B_{b}$ which has $N_{b}$ charges. $B_{b, t}$ represents the $r^{t h}$ charge in $B_{b} . B_{b}^{\prime}$ and $B_{b}^{\prime \prime}$ are denote respectively the first and the last charge in $B_{b}$. Charge $j$ should be sequentially processed on each stage, where each operation is defined as $O_{i, j}$. For charge $j$, its transfer time from stage $i$ to $i+1$ is $t r_{i, i+1}$, and arrival time is $r_{j}$. For operation $O_{i, j}$, the processing time in the upstream stages $(i<g)$ and in the last stage are defined as $p_{i, j}$ and $p_{g, k, j}$, respectively. To make a feasible solution for the SCCSP, the following decision variables must be determined:
$x_{i, k, j, j_{2}}=\left\{\begin{array}{ll}1 & \text { if charge pair }\left(j_{1}, j_{2}\right) \text { is allocated on } M_{i, k}, i<g . \\ 0 & \text { otherwise }\end{array}\right.$
$y_{h_{1} b_{2}, k}=\left\{\begin{array}{ll}1 & \text { if cast pair }\left(b_{1}, b_{2}\right) \text { is allocated on } M_{g, k}, \\ 0 & \text { otherwise. }\end{array}\right.$
$s_{i, j} \quad$ starting time of operation $O_{i, j}, i=1,2, \cdots g$.

## A. Mathematic Model

Considering the temperature drop reasons and cycle time in SCC process, the cost objective named average waiting time (AWT) is minimized.
$\min f=\left(\gamma_{i} \sum_{j=1}^{n}\left(s_{1, j}-r_{j}\right)+\sum_{i=2}^{g} \sum_{j=1}^{n} \gamma_{i}\binom{s_{i, j}-s_{i-1, j}}{-p_{i-1, j}-t r_{i-1, j}}\right) \times \frac{1}{n}$
where $\gamma_{i}$ represent the cost coefficient of each stage. Considering technical reasons in real-world production environments, the SCCSP must satisfy following constraints:
(1) Uniqueness constraints: in the upstream stages, a charge only processed on one machine (Eq.2), and the prior relationship between two different charges is unique (Eq.3); a cast also only processed on one machine in the last stage (Eq.4).

$$
\begin{gathered}
\sum_{j_{1}=1, j_{1}=j_{2}}^{n} x_{i, k, j, j_{2}}=1, i \in\{1, \cdots, g-1\}, j_{1} \in J \\
x_{i, k, j, j_{2}}+x_{i, k, j_{2}, j_{1}} \leq 1 \\
i \in\{1, \cdots, g-1\}, k \in M_{i}, j_{1}, j_{2} \in J
\end{gathered}
$$

$$
\sum_{k=1}^{m_{i, 1}} \sum_{b_{1}=1, b_{1}=b_{2}}^{N} y_{h_{1} b_{2}, k}=1, b_{1} \in B
$$

(2) Machine capacity constraints: for any two different charges allocated on the same machine, only when the preceding charge has been completed, the next one can be started.

$$
\begin{gathered}
s_{i, j_{1}}+p_{i, j_{1}}-s_{i, j_{2}}-L \times\left(1-x_{i, k, j, j_{2}}\right) \leq 0 \\
i \in\{1, \cdots, g-1\}, j_{1}, j_{2} \in J, j_{1} \neq j_{2}
\end{gathered}
$$

where $L$ is a very large constant.
(3) Precedence constraints: for two consecutive operations of the same charge, the next operation can be started only after the previous one is completed and its charge is transferred to the assigned machine.

$$
s_{i, j}+p_{i, j}+t r_{i, i+1} \leq s_{i+1, j}, i \in\{1, \cdots, g-1\}, j \in J
$$

(4) Setup constraints: for any pair two adjacent casts $\left(b_{1}, b_{2}\right)$ allocated on the same machine in the last stage, a setup time $s u_{b_{2}}$ of the second cast $b_{2}$ must be provided.

$$
\begin{gathered}
s_{g, j_{1}}+p_{g, j_{1}}+s u_{b_{2}}-L \times\left(1-y_{h_{1} b_{2}, k}\right) \leq s_{g, j_{2}} \\
j_{1}=B_{b_{1}}^{+}, j_{2}=B_{b_{2}}^{-}, b_{1}, b_{2} \in\left(b_{1}, b_{2}\right)
\end{gathered}
$$

(5) Continuity constraints: any two adjacent charges in the same cast must be continuously processed on the same machine without break.

$$
\begin{gathered}
s_{g, j_{2}}=s_{g, j_{1}}+\sum_{k=1}^{m_{i, 1}} \sum_{b_{2}=1, b_{1}=b_{2}}^{N}\left(p_{g, k, j_{1}}, \times y_{h_{1} b_{2}, k}\right) \\
r=1, \cdots, N_{b_{1}}-1, j_{1}=B_{b, r}, j_{2}=B_{b, r+1}
\end{gathered}
$$

(6) Arrival constraints: the operation in the first stage only starts after its hot metal has arrived.

$$
s_{1, j} \geq r_{j}, \quad j \in J
$$

## B. Uncertainty Set

Because there exist numberous uncertain factors under real-world environments, we assume that processing times in the upstream stages are uncertain data which can represented as a linear combination of its standard value and the predefined perturbation level multiplied by a stochastic coefficient.

$$
p_{i, j}=\bar{p}_{i, j}+\bar{\varsigma}_{i, j} \times \hat{p}_{i, j}, i \in\{1, \cdots, g-1\}, j \in J
$$

where $p_{i, j}$ standards for the uncertain processing time, $\bar{p}_{i, j}$ and $\hat{p}_{i, j}$ represents the standard values and perturbations respectively, $\bar{\varsigma}_{i, j}$ denotes an independent stochastic variable which constructs the uncertain set $U$.

$$
U=\left\{\bar{\varsigma} \in \mathbb{R}^{n \times g-1)}: \|\bar{\varsigma}\|_{\infty} \leq 1,\|\bar{\varsigma}\|_{2} \leq \Omega\right\}
$$

## III. ALGORITHM

Since the deterministic SCCSP is always NP-hard, it is more difficult to solve the uncertain SCCSP within an acceptable computing time. It can be found that the biggest challenge for solving the uncertain SCCSP is how to tackle

numerous binary variables ( $x_{i, k, j_{1}, j_{2}}$ and $y_{h_{1}, b_{2}, k}$ ) and uncertain variables ( $P_{i, j}$ ). By the way of "Benders decomposition", the SCCSP can be divided into two sub-problems: the machine allocation problem (MAP) which only contains binary decision variables $x_{i, k, j_{1}, j_{2}}$ and $y_{h_{1}, b_{2}, k}$, and the timetabling problem (TTP) which only contains continuous variable $x_{i, j}$. With traditional Benders decomposition algorithm, the MAP is iteratively solved by adding new constraints which are generated by dual of TTP, and this makes it progress towards to an optimal solution. With the increase of added constraints, the speed of solving the MAP will be slow down. Instead of this individual-based iterative search, in this section, we propose a population-based algorithm named EDA to solve the MAP, and use a RO approach to solve the TTP. The main flow chart of the AS-EDA and RO is summarized in Fig. 2.
![img-2.jpeg](img-2.jpeg)

Fig. 2. The overview flow of AS-EDA

## A. Encoding and Initialization

The MAP is formulated as follows:

$$
(M A P) \min f
$$

subject to $f \geq 0$ and Eqs. (2)-(4).
![img-2.jpeg](img-2.jpeg)

To determine a feasible solution $\left(x_{i, k, j_{1}, j_{2}}\right.$ and $\left.y_{h_{1}, b_{2}, k}\right)$ of the MAP, we use a $g$-part vector to represent the machine
allocation in each stage. Taking the 3 -stage SCCSP as an example, there are two casts, each of which has three charges, to be assigned. Its feasible solution can be represented as a 3-part vector shown in Fig. 3. The charge set $\{1,2,3,4,5,6\}$ is allocated on $\left\{M_{1,2}, M_{1,1}, M_{1,3}, M_{1,1}, M_{1,3}, M_{1,2}\right\}$ and $\left\{M_{2,4}, M_{2,1}\right.$, $\left.M_{2,3}, M_{2,3}, M_{2,4}, M_{2,2}\right\}$. Charges in the first cast $\{1,2,3\}$ and the second cast $\{4,5,6\}$ are assigned on $M_{3,1}$ and $M_{3,2}$ respectively.

For initializing the first population $P O P(0)$, we generate the first individual $P O P(0,0)$ with following steps.
Step 1: In the last stage, select the machine with the longest processing time (LPT) for each cast.
Step 2: In the upstream stages, select the earliest available machine (EAM) for each machine with backward scheduling manner.

After $P O P(0,0)$ is constructed, the other $N P-1$ solutions are generated with a random shuffling manner.

## B. Evaluation by $R O$

After the machine allocation vector is determined, the decision variables $x_{i, k, j_{1}, j_{2}}$ and $y_{h_{1}, b_{2}, k}$ in MAP are known. To simplify TTP, we use $J_{i, k}$ to represent the charge set assigned on machine $M_{i, k}(i<g)$, and $C_{k}$ to represent the sorted casts assigned on machine $M_{g, k}$. Then, the TTP is reformulated as follows.

$$
(T T P) \min f=\left(\gamma_{1} \times W_{1}+\sum_{i=2}^{n} \gamma_{i} \times W_{i}\right) \times \frac{1}{n}
$$

subject to

$$
\begin{gathered}
W_{1}-s_{1, j} \leq-r_{j}, \quad j \in J \\
W_{i}-s_{i, j}+s_{i-1, j} \leq-p_{i-1, j}, \quad j \in J, i \in\{2, \cdots, g\} \\
s_{i, j_{1}}-s_{i, j_{2}} \leq-p_{i, j_{1}}, i \in\{1, \cdots, g-1\},\left(j_{i}, j_{2}\right) \in J_{i, k} \\
s_{i, j}-s_{i+1, j}+t r_{i, i+1} \leq-p_{i, j}, i \in\{1, \cdots, g-1\}, j \in J \\
s_{g, j_{2}}-s_{g, j_{2}} \leq p_{g, j_{2}, k}+s u_{j_{1}},\left(b_{1}, b_{2}\right) \in C_{k} \\
s_{g, j_{2}}=s_{g, j_{1}}+p_{g, k, j_{2}}, r=1, \cdots, N_{b}-1 \\
j_{1}=B_{b, r}, j_{2}=B_{b, r+1}, b \in C_{k}
\end{gathered}
$$

and Eq. (9).
According to the formulation of TTP, no variable in Eqs. (9), (13), (14), (18), and (19) is uncertain, while only right-hand side variables in Eqs. (15)-(17) are uncertain. Based on the approach proposed by Ben-Tal et al. [12], the robust counterpart (RC) of the TTP with uncertainty set (11) can be rewritten by adding conic quadratic constraints. Then, Eqs. (15)-(17) are transformed as follows.

$$
\begin{gathered}
\left|\hat{p}_{i-1, j}-\omega_{i-1, j}\right|+\Omega \times\left|\omega_{i-1, j}\right| \leq s_{i, j}-\left(s_{i-1, j}+\bar{p}_{i-1, j}\right)-W_{i} \\
j \in J, i \in\{2, \cdots, g\} \\
\left|\hat{p}_{i, j}-\omega_{i, j}\right|+\Omega \times\left|\omega_{i, j}\right| \leq s_{i, j_{2}}-\left(s_{i, j_{2}}+\bar{p}_{i, j_{2}}\right) \\
i \in\{1, \cdots g-1\},\left(j_{i}, j_{2}\right) \in J_{i, k} \\
\left|\hat{p}_{i, j}-\omega_{i, j}\right|+\Omega \times\left|\omega_{i, j}\right| \leq s_{i+1, j}-\left(s_{i, j}+\bar{p}_{i, j}+t r_{i, j+1}\right) \\
i \in\{1, \cdots g-1\}, j \in J
\end{gathered}
$$

where $\omega_{i, j}$ is the auxiliary parameter, and $\Omega$ is the "safety parameter". It means that a feasible solution satisfies every constraint under randomly perturbation with the conservative level at least $\Omega^{2}=1-\exp \left(-\Omega^{2} / 2\right)$.

To solve the RC problem with above conic quadratic constraints, the powerful commercial solver Gurobi 7.0 which is able to easily tackle 'abs' constraints is applied.

## C. Model Learning

The probabilistic model (PM) is the most key component in EDA, because it directly influences the exploration and exploitation ability of the algorithm. In this paper, three different models are constructed on $N P / 2$ promising solutions. For the $r^{t h}$ solution in the current population, the following binary variables are defined:

$$
\begin{aligned}
& P M^{1}\left(\theta_{i, j}^{k}\right)=\frac{\Theta_{i, j}^{k}}{N P / 2}, i=1, \cdots g \\
& P M^{2}\left(\theta_{i, j}^{k}\right)=U(0,1) ; P M^{2}\left(\theta_{i, j}^{k}\right)=\frac{\Theta_{i, j}^{k} \times \Psi_{i, j}^{k, k^{\prime}}}{\sum_{k^{\prime} \in M_{i}}\left(\Theta_{i, j}^{k} \times \Psi_{i, j}^{k, k^{\prime}}\right)}, i=2, \cdots g \\
& P M^{2}\left(\theta_{g, j}^{k}\right)=U(0,1) ; P M^{2}\left(\theta_{i, j}^{k}\right)=\frac{\Theta_{i, j}^{k^{\prime}} \times \Phi_{i, j}^{k^{\prime}, k}}{\sum_{k \in M_{i}}\left(\Theta_{i, j}^{k^{\prime}} \times \Phi_{i, j}^{k^{\prime}, k}\right)}, i=1, \cdots g-1
\end{aligned}
$$

It is noted that, $P M^{1}$ and $P M^{2}$ generate new solutions with a forward sampling method, while $P M^{1}$ use a backward sampling method.

## D. Adaptive Sampling

When sampling new solution from above well-designed PMs, we want to select the PM with the best performance and the smallest trails. To make tradeoffs between performance and efficiency, this model selection problem can be viewed as a K-armed bandit (KAB) problem. It means that a player is to determine which arm of the K-slot machine to pull for maximizing the expected total reward with limited trials.

Let the number of models is $Q$, and the total number for sampling is $T$. Then we implement the adaptive sampling procedure by the UCB1 [13] algorithm with following steps:

Step 1: Sampling $\Delta_{q}$ new solutions from $P M^{1}$ to $P M^{Q}$, respectively. Let $\pi_{q}$ denote the best solution so far and $\pi_{q}$ denote the best solution of $P M^{q}$. Set $v_{q}=\Delta_{0}$ and $v=Q \times \Delta_{0}$. The reward of $P M^{q}$ is defined as follows:

$$
R_{q}=\frac{1}{1+e^{\left[j\left(\sigma_{q}\right)-j\left(v_{q}\right)\right]}}
$$

Step 2: Calculated a priority index for each model $P M^{q}$ :

$$
\rho_{q}=R_{q}+\sqrt{2 \ln \left(v / v_{q}\right)}
$$

Step 3: Select the best model $\hat{q}$ with the maximum $\rho$ value. Sampling $\Delta_{0}$ new solutions via the model $P M^{\hat{q}}$. Update $v_{\hat{q}} \leftarrow v_{q}+\Delta_{0}$, and $v \leftarrow v+\Delta_{0}$.
Step 4: If $v<T$, go to Step 2; Otherwise, stop sampling.

$$
\begin{aligned}
& \theta_{i, j}^{k}(r)= \begin{cases}1 & \text { if charge } j \text { alloated on } M_{i, k} \\
0 & \text { otherwise }\end{cases} \\
& \varphi_{i, j}^{k, k^{\prime}}(r)= \begin{cases}1 & \text { if charge } j \text { alloated on } M_{i, k} \text { and } M_{i+1, k^{\prime}}, i>1 \\
0 & \text { otherwise. }\end{cases} \\
& \phi_{i, j}^{k^{\prime}, k}(r)= \begin{cases}1 & \text { if charge } j \text { alloated on } M_{i+1, k^{\prime}} \text { and } M_{i, k} \\
0 & \text { otherwise }\end{cases}
\end{aligned}
$$

Then, we sum up the statistical information with above binary variables:
$\Theta_{i, j}^{k}=\sum_{k=1}^{N P / 2} \theta_{i, j}^{k}(r) ; \Psi_{i, j}^{k, k^{\prime}}=\sum_{k=1}^{N P / 2} \varphi_{i, j}^{k, k^{\prime}}(r), \Phi_{i, j}^{k^{\prime}, k}=\sum_{i=1}^{N P / 2} \phi_{i, j}^{k^{\prime}, k}(r)$.
To fully illustrate the distribution of promising solutions, three PMs are constructed with following manners:

## IV. COMPUTATIONAL EXPERIMENTS

## A. Instance Generation

In this section, the effectiveness of the proposed algorithm is tested on the instances which are generated with statistics data extracted from a steelmaking workshop within a largest integrated iron and steel company in China. In this workshop, there are 3 stages, and the machine number in each stage is set to be $3 \times 4 \times 3$. The standard processing times $\bar{p}_{1, i}$ in the steelmaking stage is a constant number, $30 . \bar{p}_{2, j}$ in the refining stage is generated with the uniform distribution $U(35,45) . P_{3, k, j}$ in the casting stage is generated with the uniform distribution $U(25,35)$. The transfer times between two adjacent stages are $t t_{1,2}=5$ and $t t_{2,3}=5$. The setup time of each cast is $s u_{k}=60$. The constant coefficient of each stage is set $\gamma_{i}=10^{i \cdot q 1}$. According to the machine capacity in the steelmaking stage, the total charges of this workshop is about 144 in one day. So, for experimental evaluation and comparison, we randomly generate 20 problem instances, each of which has 10 casts, and satisfies $N \geq 10$ and $n=140$. The perturbation levels in the steelmaking and refining stage are set $\hat{p}_{1, i}=0.05 \times \bar{p}_{1, i}$ and $\hat{p}_{2, j}=0.15 \times \bar{p}_{2, j}$.

In AS-EDA, the parameter setting is listed as follows.

- Population size, $N P=240$.
- Incremental sampling number, $\Delta_{0}=5$.
- Maximum CPU time, $T_{\max }=180$.

Moreover, to test the robustness of the final solution output by AS-EDA and RO, a simulation procedure based on forward scheduling method runs 1000 times. Then, the mean of AWT (denoted as $\bar{f}$ ) and the cast-break probability (CBP) (denoted as $e$ ) which reflects the infeasibility level under

uncertain environments, are calculated using the method proposed by Hao et al. [14].

## B. Parameter Selection

![img-3.jpeg](img-3.jpeg)

Fig. 4. Simulation results under different conservative levels
In the roust solution of SCCSP, the parameter $\Omega$ is able to improve its robustness, but deteriorate its cost objective. Therefore, the appropriate value of $\Omega$ is very vital to the performance of the final solution. In this section, we select a representative instance to test, which has 10 casts and each of them has 10 charges. With respect to four conservative levels $\Omega^{*}=\{0.00,0.50,0.75,0.95\}$, four safety parameters are set as follows: $\Omega=\{0.00,1.177,1.665,2.448\}$. With above candidate conservative levels, the values of $\bar{f}$ and $e$ are calculated. According to the results shown in Fig. 4, along with the increase of the conservative level, the CBP is decreasing, but the mean of AWT is increasing. Because the value of CBP is tiny enough at level of 0.75 , we set $\Omega=1.665$ in following experiments.

## C. Comparative Experiments

To test the effectiveness of AS-EDA and RO, the EDA without adaptive sampling mechanism is also applied to solve these testing instances. To make these comparisons more meaningful, other two evolutionary algorithms are also choosed: the differential evolution (DE) algorithm proposed by Tang et al. [15] and the hybrid ant optimization (HANO) algorithm proposed by Atighehchian et al. [16]. Both of them use their tailored linear programing (LP) methods to solve the TTP. The mean of AWT $(\bar{f})$ and the value of $\operatorname{CBP}(e)$ of the final solution are calculated by repeated simulations. The computational results are displayed in Table I, and the statistical results are listed in the bottom. The comparative results are also shown using box plots in Fig. 5 and 6.

Under the control of the RO approach, the CBP of the final solution output by AS-EDA and EDA are close to zero. Because the distribution of simulation results for each algorithm is not known in prior, we have applied a one-sided Kolmogorov-Smirnov test (KS-test) for statistical significance test. In the KS-test, the null hypothesis is defined as: if two samples X and Y are equal statistically $(\mathrm{X}=\mathrm{Y})$. Conversely, the alternative hypothesis is defined as: the samples X and Y are statistically dissimilar $(\mathrm{X} \neq \mathrm{Y})$. The comparison in statistical significance using KS-test (reported in Table II) shows that, AS-EDA and EDA have a great
advantage in optimizing CBP, because they have implemented the RO approach.

TABLE I. SIMULATION RESULTS OF COMPARATIVE ALGORITHMS

TABLE II. KS-TEST ON SIMULATION RESULTS

To compare the improving effects on the AWT objective, the relative percentage deviations (RPD) based on the average value of all comparative algorithms are calculated via Eqs. (23) and (24)

$$
\begin{aligned}
& R P D(f)=\frac{A v e\left(\bar{f}_{\text {comp }}\right)-A v e\left(\bar{f}_{A S-E D A}\right)}{A v e\left(\bar{f}_{A S-E D A}\right)} \times 100 \% \\
& R P D(e)=\frac{A v e\left(e_{\text {comp }}\right)-A v e\left(e_{A S-E D A}\right)}{A v e\left(e_{A S-E D A}\right)} \times 100 \%
\end{aligned}
$$

The computational results show that, compared with the standard EDA, DE and HANO, AS-EDA achieves the improvement rates on AWT about $8.07 \%,-9.85 \%,-12.49 \%$,

on CBP about $-17.24 \%, 494.25 \%$, and $513.22 \%$. It is concluded that, with respect to the cost objective, AS-EDA little outperforms the standard EDA due to its adaptive sampling policy, and is inferior to DE and HANO due to the introduced safety parameters. However, both the algorithms combined with RO have extremely improved the safety levels. Compared with the great improvement on safety of the final solution, the cost objective loss of the proposed algorithm is acceptable.
![img-4.jpeg](img-4.jpeg)

Fig. 5 Box plot for AWT output by different algorithms
![img-5.jpeg](img-5.jpeg)

Fig. 6 Box plot for for CBP output by different algorithms

## V. CONCLUSION

In this paper, we have studied an uncertain SCCSP with interval processing times. According Bender decomposition strategy, the SCCSP has been divided into two sub-problems: the MAP and TTP. To keep robustness under uncertain environments, the AS-EDA combined RO approach has been proposed to solve the uncertain SCCSP. The computational results have verified that the proposed algorithm is robust under uncertain environments and have a better optimization ability compared with the standard EDA.

In future studies, we will investigate the SCCSP existing more uncertain factors, such as the dynamic arrival time of hot metal and machine breakdown.
