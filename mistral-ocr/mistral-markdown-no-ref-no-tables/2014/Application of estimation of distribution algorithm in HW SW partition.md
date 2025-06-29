# Application of Estimation of Distribution Algorithm in HW/SW Partition 

Juan Yu, Yuyao He<br>School of Marine Science and Technolgy, Northwestern Polytechnical University, Xi'an, Shaanxi, P.R.China<br>yujuan@snnu.edu.cn, heyyao@nwpu.edu.cn


#### Abstract

Hardware/software (HW/SW) partitioning problem is NP hard problem. An improved algorithm based on estimation of distribution algorithms is proposed to solve HW/SW partitioning problem. Estimation of distribution algorithm is good in globe search but poor in local search and may suffer from"premature convergence" beacause of diversity loss. The improved algorithm strengthens the local searching ability by cloning and searching the elite solutions and improves the diversity loss by correcting the probability model. Numerical simulation is carried out and compared with existing algorithm, the results show the effectiveness of the improved estimation of distribution algorithm in solving HW/SW partitioning problem.


Keywords-hardware/software partitioning, estimation of distribution algorithm, elite clone, probability model correction

## I. INTRODUCTION

Typical embedded system includes hardware (FPGAs or ASICs) and programmable part, namely processor (DSPs or ASIPs) [1]. Many function blocks of the system can be implemented by either hardware or software. Generally software implementation is relatively flexible and cheap, hardware implementation could improve the speed of system, but the cost is relatively high. When design a hybrid system with hardware and software, we will face hardware/software ( HW/SW) partitioning problem. The task of HW/SW partitioning problem is mapping the function blocks to target architecture to optimize the specified system overhead and meets the constraint conditions. The results of HW/SW partitioning problem have very important influence on the performance of the final product[2].

There are two types of HW/SW partitioning algorithm: exact algorithm and heuristic algorithm. Because HW/SW partitioning problem is NP hard, the exact algorithm can not solve large-scale problem,but heuristic algorithm do, such as artificial bees[2], genetic algorithm[3], particle swarm optimization algorithm[4], tabu search[5], constructed heuristic algorithm[6].These algorithms can solve the largescale problem, but cannot ensure optimal solution and each has its own disadvantages. Tabu search is dependent on the initial solution and is serial search process; genetic algorithm is poor in local search and converges slowly; particle swarm optimization algorithm is liable to premature convergence;

Xiaoqiang Li
School of Automation and Informaton Engineering, Xi'an University of Technology, Xi'an, Shaanxi, P.R.China mrglhome@xaut.edu.cn
for bee algorithm ,the search speed is slow when approximating to the global optimal solution, and suffers from the population diversity reduction.

As a new algorithm, estimation of distribution algorithm (EDA) has good global search ability, can solve the high dimensional problems and difficult optimization problems, so it is widely used in recent years[7-12], however, no literature shows that EDA was used in HW/SW partitioning problem. This paper improved the shortcoming of estimation of distribution algorithms and applied it in HW/SW partitioning problem. The results were compared with original EDA and the HA algorithm in [6], experiment results show that the proposed algorithm is effective and can solve the HW/SW partitioning problem successfully.

The rest of this paper is organized as follows. Section II describes briefly target architecture and partitioning model. Section III analyzes basic estimation of distribution algorithm. Section IV describes the proposed algorithm named IEDA for HW/SW partitioning problem. Experimental results are presented in section V. Finally, we conclude this paper in section VI.

## II. TARGET ARCHITECTURE AND PARTITIONING MODEL

The target architecture adopted is architecture of main processor with coprocessor. The main processor represents software subsystem(SW) which implements a function by software;The coprocessor represents hardware subsystem(HW) which implements a function by special hardware circuit.

Most of the existing HW/SW partitioning algorithms only consider the execution time and cost, but power consumption is also a crucial factor, high power consumption may lead to overheating and damage of circuit; On the other hand, the fact that effective working time of mobile computing devices relied on battery power has great influence on the consumer's purchase decision. So it should limit power consumption in a certain range to ensure the effective working time. This paper will minimize hardware cost under the constraints of power consumption and execution time, the same as [6].

For comparison, the same partitioning model of [6] is used, as shown in Fig.1.

![img-0.jpeg](img-0.jpeg)

Fig.1. Partitioning model
For the function block set $\mathrm{B}=\left\{\mathrm{B}_{1}, \mathrm{~B}_{2} \ldots \mathrm{~B}_{\mathrm{n}}\right\}, \mathrm{HW} / \mathrm{SW}$ partitioning problem will map all the function blocks to HW and SW sets, and $H W \subset B, S W \subset B, H W \cup S W=B$, $H W \cap S W=\Phi$.

According to the requirements of the partitioning algorithm, parameterize $B_{i}$ as follow: $B_{i}=<a_{i}, t_{i}^{x}, t_{i}^{b}, p_{i}^{x}, p_{i}^{b}>$. Where $a_{i}$ is the hardware cost when $B_{i}$ implemented with hardware and it is proportional to the circuit area occupied; $t_{i}^{x}$ and $p_{i}^{x}$ are execution time and power consumption respectively when $B_{i}$ is implemented with software; $t_{i}^{b}$ and $p_{i}^{b}$ are execution time and power consumption respectively when $B_{i}$ is implemented with hardware. In general, for the same $B_{i}$, the execution time and power consumption implemented with hardware is less than that implemented with software[6],so $t_{i}^{x}>t_{i}^{b}, p_{i}^{x}>p_{i}^{b}$.

We can establish the mathematical model of HW/SW partitioning problem as Eq.(1):

$$
\left\{\begin{aligned}
\min \cos t(X) & =\sum_{i=1}^{n} a_{i} x_{i} \\
s . t \sum_{i=1}^{n}\left[t_{i}^{x}\left(1-x_{i}\right)+t_{i}^{b} x_{i}\right] & \leq T \\
\sum_{i=1}^{n}\left[p_{i}^{x}\left(1-x_{i}\right)+p_{i}^{b} x_{i}\right] & \leq P \\
& x_{i} \in\{0,1\}
\end{aligned}\right.
$$

Among them: n is the number of functional blocks; $x_{i}=1$ means $B_{i}$ implemented with hardware, $x_{i}=0$ means $B_{i}$ implemented with software; T is the time constraint, P is the power consumption constraint.

Let $T^{t}=\sum_{i=1}^{n} t_{i}^{x}-T, P^{t}=\sum_{i=1}^{n} p_{i}^{x}-P, t_{i}=t_{i}^{x}-t_{i}^{b}$,
$p_{i}=p_{i}^{x}-p_{i}^{b}$, we obtained Eq.(2) which is eqcuivalent to Eq.(1):

$$
\begin{aligned}
\min \cos t(X) & =\sum_{i=1}^{n} a_{i} x_{i} \\
s . t \sum_{i=1}^{n} t_{i} x_{i} & \geq T \\
\sum_{i=1}^{n} p_{i} x_{i} & \geq P \\
x_{i} & \in\{0,1\}
\end{aligned}
$$

The improved estimation of distribution algorithm is applied to solving the HW/SW partitioning problem represented by Eq.(2) in this paper.

## III. ESTIMATION OF DISTRIBUTION ALGORITHM

Estimation of distribution algorithm is a new branch of evolutionary computation, which is the combination of statistical learning and evolutionary algorithms. It is proposed to solve the building block damage problem of genetic algorithm. EDA builds a probability model from promising solutions set, then attempts to estimate the probability distribution of the promising solutions. Once the model is built, new solutions are generated by sampling the distribution encoded by this model. The operation is repeated and the evolution of population is realized. EDA procedure is outlined as follows:
Step $1 \mathrm{~g}=0$, generate initial population pop(g) .
Step 2 Select S(g) from pop(g).
Step 3 Build probability model $\rho(\mathrm{g})$ from $\mathrm{S}(\mathrm{g})$.
Step 4 Randomly sample from $\rho(\mathrm{g})$.
Step 5 Generate pop $(\mathrm{g}+1)$.
Step $6 \mathrm{~g}=\mathrm{g}+1$.
Step 7 Judges whether the termination criterion is met, if met then output the optimization results; otherwise, turn to Step2.
Sampling probability model avoids damaging the promising solutions, which is contrary to the operation of crossover and mutation in genetic algorithm. It is also the main characteristics different from genetic algorithm. EDA controls the evolutionary direction of population from macroscopic, solves high dimensional problem and difficult optimization problem effectively and reduces the time complexity.

But EDA also has some shortcomings: (1).the local search ability is poor relatively; (2). when studying the probability model in the process of evolution, it tends to overfit the distribution of solution space, no longer generate diversity solutions after several generations and results in premature convergence.

## IV. IMPROVED EDA SOLVING HW/SW PARTITIONING PROBLEM

There is an underlying assumption in most heuristic algorithms: good solutions have similar structure.This assumption is reasonable for most real-world problems,e.g., the percentage of common edges in any two locally optimal solutions of a traveling salesman problem obtained by the Lin-Kernighan method is about $85 \%$ on average[8]. Based on this theory, the proposed method strengthens the local search ability of original algorithm by cloning and searching good solutions, and alleviates diversity loss by correcting probability model. The improved algorithm based on EDA is named as IEDA, which is applied to solving HW/SW partitioning problem.

## A. Representation of Solution

The solution of HW/SW partitioning problem is represented as a binary string with length of n , i.e., $\boldsymbol{X}=\left(x_{l} \ldots x_{l} \ldots x_{n}\right)$.
B. Elite Clone Selection Operation

The elite clone selection operation is applied before Step 2 of EDA algorithm.

## 1.) Size of Clone

Elite population $\mathrm{s}^{\prime}(\mathrm{g})$ which consists of Ms the best fitnesses individuals in $\operatorname{pop}(\mathrm{g})$ is selected and cloned, $\mathrm{Ms}=\left[\alpha^{*} \mathrm{M}\right], \mathrm{M}$ is population size, $0<\alpha<1 . \mathrm{nc}_{\mathrm{i}}$ is the clone size of the ith elite solution $\boldsymbol{X}_{i}$, when $\mathrm{nc}_{\mathrm{i}}$ is determined, two factors should be considered:objective function value $\operatorname{cost}\left(\boldsymbol{X}_{i}\right)$ and the similarity of $\boldsymbol{X}_{i}$ with the rest solutions of the population. In the problem represented by Eq.(2), the smaller $\operatorname{cost}\left(\boldsymbol{X}_{i}\right)$ and the smaller the similarity of $\boldsymbol{X}_{i}, \boldsymbol{X}_{i}$ is more promising and should strengthen the search for it. $\mathrm{nc}_{\mathrm{i}}$ is calculated by Eq.(3) :
$n c_{i}=\operatorname{int}\left(N c^{*} \frac{1 / \operatorname{cost}\left(X_{j}\right)}{\sum_{j=1}^{M} 1 / \operatorname{cost}\left(X_{j}\right)} * \frac{q_{j}}{\sum_{j=1}^{M} q_{j}}\right)$
Where $\operatorname{int}(x)$ is the minimum integer greater than $x . N c$ is a constant for clone, it is an integer greater than M. $q_{i}=\min \left\{d_{i j}\right\}, i=1,2,3 \ldots, \mathrm{Ms}, j=i+1 \ldots, \mathrm{M}, d_{i j}$ is the hamming distance between $\boldsymbol{X}_{i}$ and $\boldsymbol{X}_{j}$. The greater the $q_{i}$, the smaller the similarity of $\boldsymbol{X}_{i}$.

## 2) $T$ transformation

Supposing $X_{i}^{j}$ is the $j$ th cloned individual of $\boldsymbol{X}_{i}$, transformation from $X_{i}^{j}$ to $X_{i}^{j}$ is defined as $\mathrm{T}\left(X_{i}^{j} \rightarrow X_{i}^{j}\right)$ : randomly select k genes which value equal to 0 and turn them to 1 ; randomly select $\mathrm{k}+\mathrm{t}$ genes which value equal to 1 and turn them to 0 . The meaning of T transformation in HW/SW partitioning problem lies in switching the mapping domain of k function blocks in software domain and $\mathrm{k}+\mathrm{t}$ function blocks in hardware domain.

## 3) Dominance Replacement

Let $\operatorname{cost}\left(X_{i}^{k}\right)=\min \left(\operatorname{cost}\left(X_{i}^{j}\right)\right), \boldsymbol{X}_{i} \in \mathrm{~s}^{\prime}(\mathrm{g}), \mathrm{j}=1,2, \ldots, \mathrm{nc}_{\mathrm{i}}, \mathrm{if}$ $\operatorname{cost}\left(X_{i}^{k}\right) \leq \operatorname{cost}\left(\boldsymbol{X}_{i}\right), \boldsymbol{X}_{i}$ is replaced by $X_{i}^{k}$. For $\boldsymbol{X}_{i} \in \mathrm{~s}^{\prime}(\mathrm{g})$, the process of elite clone selection operation offers $\mathrm{nc}_{\mathrm{i}}$ different search directions in the neighborhood of $\boldsymbol{X}_{i}$ and makes local search in the neighborhood, the dominance replacement ensures that the solutions will not be worse, and accelerates the convergence speed. After dominance replacement, a new population pop ' $(\mathrm{g})$ is formed.

## C. Probability Model

Probability vector $\rho(g)=\left(\rho_{1}, \ldots \rho_{k} \ldots, \rho_{n}\right)$ is probability model to describe the distribution of solution space. $\rho_{k}$ is the probability of $\mathrm{B}_{\mathrm{k}}$ mapped to the hardware domain i.e., the probability of $x_{k}=1$. Offspring solutions are generated by sampling from probability model, i.e., a number r can be generated randomly, $\mathrm{r}_{\in}[0,1]$ if $\mathrm{r}<\rho_{j}, x_{i}=1$; otherwise $x_{i}=0$.

This paper adopts the UMDA [7] probability model, it builds the probability model on $\mathrm{s}^{\prime}(\mathrm{g})$ subset which is composed of $[\beta * \mathrm{M}]$ individuals with best fitness in $\operatorname{pop}^{\prime}(\mathrm{g}), \quad 0<\beta<1 . \quad \rho_{j}$ is updated by (4), $x_{i}^{j}$ is the value of the ith gene of the jth individual:

$$
\rho_{i}=\frac{\sum_{j \in \mathrm{~T}^{\prime}(g)} x_{i}^{j}}{[\beta * \mathrm{M}]}
$$

The probability of generating solution $X$ is calculated by Eq.(5) :

$$
\rho(X)=\prod_{i=1}^{n}\left[\rho_{i} * x_{i}+\left(1-\rho_{i}\right) *\left(1-x_{i}\right)\right]
$$

Initial population pop (0) is generated randomly with uniform distribution of the solution space, namely $\rho(0)=(0.5 \ldots 0.5 \ldots 0.5)$.

## D. Probability Model Correction

Along with the iteration, EDA will lose diversity, population variance is growing smaller, eventually reduces to zero, probability model evolves to only produce same solutions[12].

EDA diversity loss occurred in two stages :

- Sampling from the probability model to generate population. This diversity loss is due to the fact that variance of population sampled from probability model will be less than the variance of parent population. Elite clone selection operation introduced by part B not only strengthens the local search ability but also improves the population diversity loss problem since $X_{i}^{k}$ is obtained by T transformating the sampled solution.
- Selecting M solutions to build the probability model of next generation. Usually high fitnesses solutions are selected to build probability model, thus distribution characteristics of good solutions are achieved, but will cause loss of diversity. It can be relieved by slowing down the update speed of probability model, making update speed relatively slower than the search speed of algorithm. Once $\rho_{j}$ is close enough to 0 or 1 , the value of $x_{i}$ tends to fix and lead to the combination reduction of n genes,i.e., the diversity of population is made to decrease. So the boundary of probability model is corrected by Eq.(6):

$$
\rho_{i}^{\prime}=\left\{\begin{array}{c}
\gamma, \rho_{i}<\gamma \\
p_{i}, \lambda<\rho_{i}<1-\gamma \\
1-\gamma, \rho_{i}>1-\gamma
\end{array}\right.
$$

$\rho_{i}$ is probability before correction, $\rho_{i}$ is probability after correction, $\gamma=1 / n$.

The correction prevents $\rho_{i}$ reaching 1 and 0 , lowers the update speed of probability model, also improves the diversity loss of population and avoids falling into local optimum .

## E. Repair Infeasible Solution

Sampled solutions may not satisfy the time or power consumption constraints, so it is necessary to repair the infeasible solutions. The repair process is as follows:

Step1 Compute tuse,puse: tuse $=\sum_{i=1}^{n} t_{i} x_{i}$ puse $=\sum_{i=1}^{n} p_{i} x_{i}$.
Step2 Compute $b_{i}$ :
if tuse $<T$ ' $\& \&$ puse $>=P$ ', solution not meeting the time constraint, $b_{i}=a_{i} / t_{i}$;
if puse $<P$ ' $\& \&$ tuse $>=T$ ', solution not meeting the power consumption constraint, $b_{i}=a_{i} / p_{i}$;
if puse $<P$ ' $\& \&$ tuse $<T$ ', solution meets neither time constraint nor power consumption constraint, $b_{i}=a_{i} / \sqrt{t_{i}^{2}+p_{i}^{2}} ;$
Step3 Sort $b_{i}$ in ascending order, let the sequence after sort is $b_{1}<b_{2}<\ldots<b_{n}$.
Step 4 for $\mathrm{i}=1: \mathrm{n}$
if $x_{i}=0$, let $x_{i}=1$, tuse=tuse $+t_{i}$, puse $=$ puse $+p_{i}$; if tuse $>=T^{\prime} \& \&$ puse $>=P^{\prime}$,break.

## F. IEDA Algorithm

The algorithm flow of IEDA is as follows:
Input: $a_{i}, t_{i}^{\prime}, p_{i}^{\prime}, t_{i}^{\prime \prime}, p_{i}^{h}, T, P$
Output: $\boldsymbol{X}_{\text {bestroflar }}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$
Step1 Parameter settings: set value of $\mathrm{G}, \mathrm{M}, \mathrm{Nc}, \alpha, \beta, \mathrm{k}$ and t .
Step2 Let $\mathrm{g}=0$, generate initial population $\operatorname{pop}(0)=\left\{\boldsymbol{X}_{l}, \ldots \boldsymbol{X}_{M}\right\}$ and repair infeasible solutions, then calculate the objective function value $\operatorname{cost}\left(\boldsymbol{X}_{i}\right)$ and sort in ascending order,let $\operatorname{cost}_{\text {bestroflar }}=\operatorname{cost}\left(\boldsymbol{X}_{1}\right), \boldsymbol{X}_{\text {bestroflar }}=\boldsymbol{X}_{1}$.
Step3 Perform elite clone selection operation for pop(g), and form a new population pop '(g).
Step4 Select $\mathrm{s}^{2}(\mathrm{~g})$ from pop ' $(\mathrm{g})$ and build probability model from $\mathrm{s}^{2}(\mathrm{~g})$.
Step5 Correct probability model.
Step6 Generate new population pop $(\mathrm{g}+1)$ by sampling , and repairing infeasible solutions .
Step7 Calculate $\operatorname{cost}\left(\boldsymbol{X}_{i}\right)$ and sort in ascending, $X_{i} \in \operatorname{pop}(g+1)$.
Step8 Update cost $_{\text {bestroflar }}$ and $\boldsymbol{X}_{\text {bestroflar }}$.
if $\operatorname{cost}\left(\boldsymbol{X}_{i}\right)<\operatorname{cost}_{\text {bestroflar }}$ then $\operatorname{cost}_{\text {bestroflar }}=\operatorname{cost}\left(\boldsymbol{X}_{i}\right)$, $\boldsymbol{X}_{\text {bestroflar }}=\boldsymbol{X}_{i}$.
Step9 $\mathrm{g}=\mathrm{g}+1$.

Step10 If the termination criterion is met, then $\boldsymbol{X}_{\text {bestroflar }}$ is output;otherwise, turn to Step3.

## V. SIMULATION

Reference [6] solves the HW/SW partitioning problem by a heuristic algorithm(HA) based on greedy algorithm. In this paper, basic EDA, IEDA and HA algorithms under 36 different constraint conditions are simulated by C language and the simulation results are compared.

## A. Parameters Settings

## 1) Function Block Parameters

In order to compare with HA algorithm, parameter setting is the same as [6]. $t_{i}^{\prime}$ is generated randomly in $(0,30), p_{i}^{\prime}$ is generated randomly in $(0,20) ; t_{i}^{\mathrm{h}}$ and $p_{i}^{h}$ are generated randomly in $\left(0, \lambda^{*} t_{i}^{\prime}\right)$ and $\left(0, \lambda^{*} p_{i}^{\prime}\right)$ respectively.

## 2) IEDA Parameters

According to the experience, let $\mathrm{M}=40, \mathrm{Nc}=25 * \mathrm{M}$, $\beta=1 / 4 ; \alpha$ decides the number of elite solutions needed to clone, larger $\alpha$ makes more comprehensive search, but also brings longer computing time. For comprehensive consideration, let $\alpha=1 / 8$.

Under five kinds of typical constraint conditions (i.e., $\left(\theta_{T}, \theta_{P}\right)$ takes $(1 / 6,1 / 6),(1 / 6,6 / 6),(3 / 6,3 / 6),(6 / 6,1 / 6)$, $(6 / 6,6 / 6)$ respectively), a total of six kinds of combination of $k$ and $t$ are simulated, in which $k$ takes 1,2 and 3 , $t$ takes 1,2 respectively, and eventually $\mathrm{k}=1, \mathrm{t}=1$ are determined.

Termination criterion is achieving maximum number of iterations $\mathrm{G}, \mathrm{G}=2000$.

## B. Simulation Results

For further describe the simulation results, we employ the following notations.

- Suppose $\cos t(A)$ is hardware cost obtained by algorithm A, and $\cos t \_h w$ is hardware cost when all the blocks are mapped to hardware domain. Let
$\cos t \_u s e d(A)=\frac{\cos t(A)}{\cos t \_h w} \times 100 \%$
Because the optimization objective is minimizing cost, the smaller $\cos t \_u s e d(A)$, the better the optimization results of the algorithm. Let
$\delta_{\mathrm{A}-\mathrm{B}}=\cos t \_u s e d(A)-\cos t \_u s e d(B)$
If $\delta_{A-B}>0$, the results of algorithm B is better than that of algorithm A, and the greater the value,the better the algorithm B relative to algorithm A . If $\delta_{A-B}<0$, the results of algorithm A is better than that of algorithm B .
- The HW/SW partitioning problem is solved under different constraints, so the time constraint and power consumption constraint are set by Eq.(9):

$$
\left\{\begin{array}{l}
T\left(\theta_{T}\right)=T \_h w+\theta_{T} *\left(T \_s w-T \_h w\right) \\
P\left(\theta_{P}\right)=P \_h w+\theta_{P} *\left(P \_s w-P \_h w\right)
\end{array}\right.
$$

$T \_h w$ and $P \_h w$ are time and power consumption when all the blocks are mapped to hardware domain; $T \_s w$ and $P \_s w$ are time and power consumption when all the blocks mapped to software domain; $0 \leq \theta_{T} \leq 1,0 \leq \theta_{P} \leq 1$, different $\theta_{T}, \theta_{P}$ values represent different time constraint and power consumption constraint. As can be seen, the value of time constraint is limited within the range of $\left[T \_h w, T \_s w\right]$, the value of power consumption constraint is limited within the range of $\left[P \_h w, P \_s w\right]$.

The same as [6], $\mathrm{n}=100, \lambda=1 / 2, \theta_{T}$ and $\theta_{P}$ take $1 / 6$, $2 / 6,3 / 6,4 / 6,5 / 6,6 / 6$ respectively, the algorithm is simulated under 36 kinds of constraint conditions, the simulation results are shown in TABLE I.The results are average value of 20 random instances. For comparison, $\delta$ is also listed, $\delta$ is the error between the solution of HA algorithm and the optimal solution. The smaller the value of $\delta$, results
of HA are closer to the optimal solution, the data of $\delta$ come from [6].

As can be seen from the data shown in TABLE I:

- Compare $\delta_{\text {HA-IEDA }}$ and $\delta_{\text {HA-IEDA }}$, all the remaining 35 kinds of constraint conditions are $\delta_{\text {HA-IEDA }}>\delta_{\text {HA-IEDA }}$, except under the constraint condition of $(6 / 6,6 / 6)$ that EDA and IEDA both obtained the optimal value of 0 , lead to $\delta_{\text {HA-IEDA }}$ equal to $\delta_{\text {HA-IEDA }}$. The results indicate that IEDA can obtain better optimization results compared to EDA for HW/SW partitioning problem, so the improvement of EDA is effective.
- The relation between $\delta$ and $\mathrm{P}\left(\theta_{P}\right)$ is shown in Fig. 2 (a), the relation between $\delta$ and $\mathrm{T}\left(\theta_{T}\right)$ is shown in Fig. 2 (b). For the same time constraint $\mathrm{T}\left(\theta_{T}\right), \delta$ is larger under $\mathrm{P}(2 / 6), \mathrm{P}(3 / 6), \mathrm{P}(4 / 6)$ than it is under $\mathrm{P}(5 / 6)$ and $\mathrm{P}(6 / 6)$, There is the same situation for the same power consumption $P\left(\theta_{P}\right)$. It shows that when (1).at least one constraint condition is loose or (2). difference between $\theta_{T}$ and $\theta_{P}$ (degree of relaxation of two constraint conditions ) is larger, $\delta$ is smaller, and HA could get better results, that is to say, results of HA solving the HW/SW partitioning problem are dependent on the constraints.

TABLE I SIMULATION RESULTS OF HA,EDA AND IEDA

![img-2.jpeg](img-2.jpeg)
(a) Relation between $\overline{\boldsymbol{\delta}}$ and $\mathrm{P}\left(\theta_{F}\right)$
![img-2.jpeg](img-2.jpeg)
(b) Relation between $\overline{\boldsymbol{\delta}}$ and $\mathrm{T}\left(\theta_{F}\right)$

Fig. 2. Relation between $\overline{\boldsymbol{\delta}}$ and $\mathrm{P}\left(\theta_{F}\right) . \mathrm{T}\left(\theta_{F}\right)$

- Can be seen from TABLE I that $\delta_{\text {HA-IEDA }}>0$, and the change trend of $\delta_{\text {HA-IEDA }}$ with $\mathrm{P}\left(\theta_{F}\right)$ under different $\mathrm{T}\left(\theta_{F}\right)$ is almost the same as change trend of $\overline{\boldsymbol{\delta}} . \delta_{\text {HA-IEDA }}>0$ shows that the results obtained from IEDA are better than results from HA; $\delta_{\text {HA-IEDA }}$ and $\overline{\boldsymbol{\delta}}$ having same change trend shows that the error between the results of IEDA and the optimal solutions is substantially constant. That is to say the constraint does not affect the performance of the IEDA algorithm. IEDA algorithms could obtain good results both under the loose constraints and strict constraints. Because the results are average value of 20 instances generated randomly, there is a small error between $\delta_{\text {HA-IEDA }}$ and $\overline{\boldsymbol{\delta}}$. The small error implies that the results obtained from IEDA are very close to or equal to the optimum value. So the IEDA algorithm can more effectively solve the HW/SW partitioning problem than HA .


## VI. CONCLUSION

Estimation of distribution algorithm is analyzed, the basic distribution estimation algorithm is improved and applied to solving HW/SW partitioning problem in this paper. The elite clone selection operation is introduced to strengthen the local search ability and the probability model is corrected to improve the diversity loss problem. The improved algorithm is used to solve the HW/SW partitioning problem which with time and power consumption as constraint conditions, minimizing the cost as optimal objective. Compared with the basic EDA algorithm and the HA algorithm, the results show that the improved EDA algorithm (IEDA) can obtain better results, and effectively solve the HW/SW partitioning problem.

## ACKNOWLEDGMENT

This paper is supported by the National Natural Science Foundation of China (Grant No. 61271143 and No.60871080).
