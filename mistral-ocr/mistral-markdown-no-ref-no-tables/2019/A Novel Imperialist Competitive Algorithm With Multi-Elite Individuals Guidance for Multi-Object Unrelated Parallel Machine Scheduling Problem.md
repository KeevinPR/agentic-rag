# A Novel Imperialist Competitive Algorithm With Multi-Elite Individuals Guidance for Multi-Object Unrelated Parallel Machine Scheduling Problem 

MEI WANG AND GUOHUA PAN<br>Laboratory of Image Processing and Pattern Recognition, Yantai Vocational College, Yantai 264670, China<br>Yantai Public Security Bureau, Yantai 264670, China<br>Corresponding author: Mei Wang (wangmei336@163.com)

This work was supported by the Shandong Province Science and Technology Development Plan Project Foundation under Grant 2014GGX101030.


#### Abstract

In this study unrelated parallel machine scheduling problem (UPMSP) with preventive maintenance (PM) and sequence dependent setup times (SDST) is investigated. A novel imperialist competitive algorithm (NICA) with multi-elite individuals guidance is proposed to minimize makespan and total tardiness simultaneously. Initialization is done by two heuristics, each of which is built based on one objective. Multielite individuals guidance strategy is added in assimilation that colonies can move toward other imperialists, diversified strategies such as local search and estimation of distribution algorithm (EDA) are adopted based on solution quality in revolution and EDA is also used in imperialist competition. Empire aggression is added by local search of imperialist for plundering a randomly chosen colony. A number of experiments are conducted on the impact of new strategies and the comparisons among NICA and other algorithms. Computational results demonstrate the effectiveness and advantages of NICA in solving UPSMP with PM and SDST.


INDEX TERMS Preventive maintenance, setup times, imperialist competitive algorithm, multi-elite individual guidance, estimation of distribution algorithm.

## I. INTRODUCTION

Parallel machine scheduling problem (PMSP) is a typical problem in the manufacturing process [1]-[5], which needs to optimize the target by rational allocation and scheduling of resources. Traditional PMSP often assumes that machines are continuously available throughout the production process, but due to the need for preventive maintenance (PM), the machine cannot be processed normally during the PM. Therefore, the assumption is not realistic in many actual production and manufacturing. Considering that PM on a regular basis can effectively prevent potential failures and avoid serious accidents in production, it is necessary to consider PM in unrelated parallel machine scheduling problems in order to get a better scheduling scheme.

In the past few years, PMSP with PM has attracted much attentions. In order to minimize makespan, Li et al. [6] proposed two mathematical programming models and designed

[^0]two heuristics. Yoo and Lee [7] presented a dynamic programming approach to minimize makespan, (weighted) sum of completion times, maximum lateness and sum of lateness, respectively. For two-parallel-machine scheduling problem with machine-dependent availabilities, He et al. [8] built a mixed 0-1 programming model for small size problem and gave nine heuristics to solve large sized instances of the problem. Wang and Wei [9] designed a model and analyzed the complexity for PMSP with deteriorating maintenance to minimize the total absolute differences in completion times and the total absolute differences in waiting times.

For UPMSP with PM, Gara-Ali et al. [10] proposed several performance criteria and different maintenance systems and gave a new method to solve the problem with deteriorating and maintenance. In order to minimize total machine load, Yang et al. [11] applied the group balance principle to solve UPMSP with aging effects and PM and proved that the problem remains polynomially solvable when the maintenance frequency on every machine is given. Avalos-Rosales et al. [12] presented a mathematical


[^0]:    The associate editor coordinating the review of this article and approving it for publication was Baozhen Yao.

formulation for UPMSP with PM and SDST and designed an efficient meta-heuristic based on a multi-start strategy to solve larger instances. Tavana et al. [13] developed a three-stage maintenance scheduling model for UPMSP with aging effect and multi-maintenance activities. Wang and Liu [14] presented a multi-objective integrated optimization method with non-dominated sorting genetic algorithm-II (NSGA-II) to solve the multi-objective UPMSP with multiresources PM.

In order to simplify the model, most studies assume that the setup times between jobs can be neglected or included in the processing time. But in actual production, setup times cannot be ignored, especially when the setup times are both sequence and machine dependent, such as chemical, printing, metal processing and semiconductor industries [15]. UPMSP with SDST has attracted some attention since the pioneering work of Parker et al. [16]. Kurz and Askin [17] presented several heuristics. Vallada and Ruiz [18] designed a genetic algorithm (GA) includes a fast local search and a local search enhanced crossover operator. Arnaout et al. [19] introduced an ant colony optimization (ACO) and tackled a special structure of the problem. Wang et al. [20] developed a hybrid EDA with iterated greedy search. Diana et al. [21] proposed an immune-inspired algorithm to solve this problem. Ezugwu and Akutsah [22] built an improved firefly algorithm refined with a local search. Fanjul-Peyro et al. [23] gave new mixed integer linear programs and a mathematical programming based algorithm to solve this problem. Caniyilmaz et al. [24] collected a real-life data from a factory and gave an artificial bee colony algorithm to solve UPMSP with SDST, processing set restrictions and due date. For UPMSP with SDST, machine eligibility restrictions and a common server, Bektur and Sarac [25] proposed a mixed integer linear programming model and designed a tabu search and a simulated annealing algorithm.

As mentioned above, many works have been finished on UPMSP with PM and UPMSP with SDST and most of them are just about the minimization of makespan as single objective. Few studies are about multi-objective optimization of the above two kinds of UPMSP; on the other hand, UPMSP with PM and UPMSP with SDST have been handled independently; however, PM and SDST are seldom simultaneously integrated into UPMSP [12]. PM and SDST are very common processing constraints in the real-life production process and the actual scheduling problem always has some conflicting objectives, thus, it is necessary to deal with multi-objective UPMSP with PM and SDST.

It also can be found that heuristics are the main method for UPMSP with PM, only GA is applied to solve it and metaheuristics such as GA, ACO and EDA have applied to deal with UPMSP with SDST; however, the applications of metaheuristics are not investigated fully and some algorithms such as imperialist competitive algorithm(ICA) are not used to solve UPMSP with PM or SDST.

ICA is a meta-heuristic based on the sociopolitical imperialist competition [26], which is an effective global
optimization method with strong neighborhood search capability and flexible structure and can be combined easily with other algorithms [27]. In recent years, ICA has been successfully applied to solve many optimization problems including PMSP [28]-[37]. Although ICA has adopted to deal with PMSP, it is not utilized to handle UPMSP with PM or SDST. ICA has great potential to solve UPMSP with PM and SDST because of its notable features and the previous works on PMSP, so it is meaningful to consider the applications of ICA to UPMSP with PM and SDST.

In this paper, UPMSP with PM and SDST is considered and a novel imperialist competitive algorithm (NICA) with multielite individuals guidance is proposed to minimize total tardiness and makespan. In NICA, initialization is done by two heuristics, each of which is built based on one of two objectives. A new strategy of assimilation is given, where colonies can learn from other imperialists. Diversified strategies such as local search and EDA are adopted according to solution quality in revolution, and empire aggression is added by local search of imperialist for plundering a randomly chosen colony. A novel imperialist competition is designed, in which the weakest colony of the weakest empire is compared with a new solution generated by EDA and the better one will be allocated to the winning empire. A number of experiments are conducted on the impact of new strategies and the comparisons among NICA and other algorithms. Computational results demonstrate the effectiveness and advantages of NICA in solving UPSMP with PM and SDST.

The remainder of the paper is organized as follows. Problem under study are described in Sections 2. NICA for the problem is reported in Section 3. Numerical test experiments on NICA are shown in Section 4 and we summarize the conclusion and some research topics in the future in the last section.

## II. PROBLEM DESCRIPTION

UPMSP with PM and SDST can be described as follows. Suppose $n$ independent jobs $J_{1}, J_{2}, \cdots, J_{n}$ can be processed on $m$ unrelated parallel machines $M_{1}, M_{2}, \cdots, M_{m}$. Each job is available at time zero. $p_{i j}$ is the processing time of job $J_{j}$ on machine $M_{i} . d_{j}$ indicates the due date of $J_{j}$.

Jobs can be processed in an interval between two consecutive maintenance activities. The interval is called the processing one and its time length is $u_{i} . w_{i}$ is the period of each maintenance. Thus, the maintenance periodic recycle of machine $M_{i}$ is $T_{i}=w_{i}+u_{i}$. We use $J_{0}$ to denote maintenance activities [12].

The setup time is dependent on sequence and machine. $s_{i j k}$ is the setup time for processing job $J_{k}$ just after job $J_{j}$ on machine $M_{i}, s_{i j k}$ indicates the setup time of machine $M_{i}$ to process the first job $J_{k}$ after a maintenance activity, and $s_{i j 0}$ is the setup time of machine $M_{i}$ to perform a maintenance activity just after the job $J_{j}$.

There are some constraints on jobs and machines:

1) Each job can be processed on only one machine at a time.

2) Operations cannot be interrupted.
3)If the processing of a job cannot be completed in a processing interval, the job can't be processed in the current interval and should be moved to the next interval for processing etc.

The goal of UPMSP with PM and SDST is to minimize the following two objectives simultaneously:

$$
\begin{aligned}
& \min f_{1}=C_{\max }=\max \left\{C_{j} \mid j=1,2, \cdots, n\right\} \\
& \min f_{2}=\sum_{j=1}^{n} \max \left\{C_{j}-d_{j}, 0\right\}
\end{aligned}
$$

where the first objective $f_{1}$ is makespan and the second objective $f_{2}$ is total tardiness. $C_{j}$ indicates the completion time of job $J_{j}$.

We give an example with two machines and six jobs. $w_{1}=37, w_{2}=4, u_{1}=70, u_{2}=86$. Due dates of six jobs are $4,89,46,35,98,45$, respectively. $p m$ is the processing time matrix, $S_{1}$ is the setup times matrix on machine 1 , and $S_{2}$ indicates the setup times matrix on machine 2 .

$$
\begin{aligned}
p m & =\left[\begin{array}{llllll}
1 & 87 & 28 & 32 & 38 & 9 \\
4 & 21 & 68 & 17 & 43 & 48
\end{array}\right] \\
S_{1} & =\left[\begin{array}{llllllll}
0 & 2 & 2 & 3 & 9 & 7 & 9 \\
6 & 0 & 1 & 8 & 1 & 3 & 9 \\
1 & 4 & 0 & 7 & 3 & 7 & 8 \\
3 & 7 & 3 & 0 & 2 & 3 & 5 \\
4 & 3 & 8 & 3 & 0 & 5 & 2 \\
8 & 8 & 3 & 7 & 9 & 0 & 5 \\
1 & 8 & 8 & 1 & 2 & 2 & 0
\end{array}\right] \\
S_{2} & =\left[\begin{array}{llllllll}
0 & 3 & 7 & 3 & 7 & 6 & 3 \\
2 & 0 & 5 & 1 & 6 & 1 & 7 \\
3 & 6 & 0 & 7 & 7 & 6 & 2 \\
4 & 7 & 6 & 0 & 9 & 6 & 9 \\
3 & 3 & 7 & 3 & 0 & 1 & 7 \\
8 & 5 & 8 & 5 & 6 & 0 & 9 \\
4 & 7 & 4 & 1 & 7 & 9 & 0
\end{array}\right]
\end{aligned}
$$

## III. NICA FOR UPMSP WITH PM AND SDST

In ICA, the empire easily fall into local optimum if colonies only move toward its imperialist and it is necessary to make individuals learn from other imperialists in assimilation. Revolution is often implemented in a single way and seldom done using the diversified methods, it is important to make full use of imperialist as good solution. EDA is an emerging stochastic group evolution algorithm based on statistical learning principle [38] and has strong global exploration ability. In this study, a new NICA by introducing EDA into ICA is proposed, which is described in the following sub-sections.

## A. ENCODING AND DECODING

UPMSP with PM and SDST consists of two sub-problems: machine assignment and scheduling.Two-string representation is often used in the previous works [39]-[42]; however, two strings of a solution are often dependent with each other. In this study, a novel two-string representation is proposed, in which a solution is composed of two independent strings.

For the problem with $n$ jobs and $m$ machines, each solution consists of a scheduling string $\left[\pi_{1}, \pi_{2}, \cdots, \pi_{n}\right]$ and a machine assignment string $\left[M_{\theta_{1}}, M_{\theta_{2}}, \cdots, M_{\theta_{n}}\right]$, where $M_{\theta_{j}}$ indicates the parallel machine assigned for job $J_{j}, 1 \leq \theta_{j} \leq m$, $\pi_{i} \in\{1,2, \cdots, n\}$. The assigned machine and the processing order for each job can be determined according to the machine assignment string and scheduling string respectively.

Fig. 1 (a), shows the Gantt chart of a possible solution with a machine assignment string $\left[M_{1}, M_{2}, M_{1}, M_{1}, M_{2}, M_{2}\right]$ and a scheduling string $[3,5,1,2,6,4]$. As shown in Fig. 1 (a), when the processing of job $J_{6}$ is considered, it can be found that the processing cannot finish in the first processing interval, so job $J_{6}$ should be processed in the next interval.
![img-0.jpeg](img-0.jpeg)

FIGURE 1. Gantt charts of the solution.

## B. INITIALIZATION

In this section, initial population is first produced by two heuristics and a random way, then initial empires are constructed. To hybrid EDA with ICA, probability matrices of EDA are also initialized.

Heuristic is often used to generate initial population. In general, a heuristic can only produce a solution. In this study, heuristics 1 and 2 are adopted, each of which produces $N / 3$ initial solutions, where $N$ represents population size.

Heuristic 1 is shown in Algorithm 1. For the example, a string $[3,5,1,2,6,4]$ is first randomly obtained. Start with $J_{3}$, we calculate $\bar{C}_{3,1,1}$ and $\bar{C}_{3,1,2}$ and obtain $\bar{C}_{\min , 3}$ of 31 . $J_{3}$ is allocated to the first position on $M_{1}$. Then for $J_{5}$, $\bar{C}_{\text {min }, 5}$ is decided and equal to 49 , and $J_{5}$ is allocated on $M_{2}$. For $J_{1}$, we find that $\bar{C}_{1,1,1}=\bar{C}_{1,2,1}=\bar{C}_{\text {min }, 1}=39$, so two positions can be selected and position 1 is chosen, so $J_{1}$ is inserted on the left of $J_{3}$ and the scheduling string becomes $[1,3,5,2,6,4]$. The final scheduling string is $[1,6,3,2,5,4]$ and machine assignment string is $\left[M_{1}, M_{2}, M_{1}, M_{2}, M_{2}, M_{1}\right] . C_{\max }$ is 114. Fig.1(b) shows the Gantt chart of the obtained solution.

## Algorithm 1 Heuristic 1

```
Randomly produce a scheduling string \(\left[\pi_{1}, \pi_{2}, \cdots, \pi_{n}\right]\)
for \(\pi_{1}\) to \(\pi_{n}\) do
    for each position \(l\) on each machine \(M_{i}, i=1,2, \cdots\),
        \(m\) do
            Calculate \(\tilde{C}_{e, l, i}\) if inserting \(\pi_{j}\) into position \(l\) of \(M_{i}\)
        end for
    Compute the minimum value \(\tilde{C}_{\text {min,e }}\) of all possible
    \(\tilde{C}_{e, l, i}\).
    Decide all machines and positions meeting \(\tilde{C}_{e, l, i}=\) $\tilde{C}_{\text {min,e }}$.
    if more than one position has \(\tilde{C}_{e, l, i}=\tilde{C}_{\text {min,e }}\) then
        Randomly choose a machine \(M_{i}^{*}\) and a position \(l^{*}\).
        else
            Directly select the machine \(M_{i}^{*}\) and the position \(l^{*}\).
        end if
    Allocate \(\pi_{j}\) into position \(l^{*}\) of \(M_{i}^{*}\).
    if \(l^{*}\) is not the last position on \(M_{i}^{*}\) then
        Adjust the position of \(\pi_{j}\) on scheduling string by
        inserting \(\pi_{j}\) into the position of \(J_{n}\), which is pro-
        cessed on position \(l^{*}+1\) of \(M_{i}^{*}\).
        end if
    end for
```

Heuristic 2 is similar with heuristic 1 and the difference between them is the computation of index. In heuristic 2, total tardiness $\tilde{T}_{e, l, i}$ of all allocated jobs is first decided and then the minimum value $\tilde{T}_{\text {min,e }}$ of all $\tilde{T}_{e, l, i}$ is obtained.

Unlike the exiting heuristics, heuristics 1 and 2 can produce many solutions. In this way, initial population $P$ is generated, in which $2 N / 3$ solutions are produced by two heuristics and the remained solutions are randomly obtained.

To construct $N_{\text {imp }}$ initial empires, cost $c_{k}$ for solution $k$ is newly defined by

$$
c_{k}=\operatorname{rank}_{k} \times D+\sum_{j=1}^{D} \frac{\left|f_{k, j}-f_{j}^{\min }\right|}{f_{j}^{\max }-f_{j}^{\min }}
$$

where $\operatorname{rank}_{k}$ represents the rank value defined by Deb et al. [43] of the solution $k . D$ is the number of objective functions. $f_{k, j}$ indicates the objective $f_{j}$ of solution $k . f_{j}^{\max }$ is the maximum $f_{j}$ of all solutions in $P . f_{j}^{\min }$ is the minimum $f_{j}$ of all solutions in $P$.

After cost of each solution is computed, all solutions are sorted in the ascending order of cost and the first $N_{\text {imp }}$ solutions are chosen as imperialists and other solutions are colonies. There are $N_{\text {col }}$ colonies, $N_{\text {col }}=N-N_{\text {imp }}$. Then the normalized cost $\tilde{c}_{k}$ and total number $N C_{k}$ of colonies are calculated [26]. Finally, $N C_{k}$ colonies are randomly allocated into empire $k$.

The optimization of EDA starts with initial probability matrices. $m(n+1) \times n$ probability matrices $\rho^{i}(g)$ are used to describe the probability of two adjacent jobs on machine $M_{i}$, $i=1,2, \cdots, m$. The probability matrix $\rho^{i}(g)$ is described as
follows

$$
\rho^{i}(g)=\left[\begin{array}{ccc}
\rho_{0,1}^{i}(g) & \cdots & \rho_{0, n}^{i}(g) \\
0 & \cdots & \rho_{1, n}^{i}(g) \\
\vdots & \vdots & \vdots \\
\rho_{n, 1}^{i}(g) & \cdots & 0
\end{array}\right], \quad i=1,2, \cdots, m
$$

where $\rho_{j, k}^{i}(g)$ represents the probability that job $J_{k}$ is on the right of job $J_{j}$ on machine $M_{i}$ at the $g$ th generation, $\rho_{0, j}^{i}(g)$ represents the probability that job $J_{j}$ is first job on machine $M_{i}$ at the $g$ th generation.

The initial probability matrices $\rho^{i}(0)$ are uniformly produced in order to ensure the uniform sampling of the solution space.

$$
\rho^{i}(0)=\left[\begin{array}{cccc}
\frac{1}{n} & \frac{1}{n} & \cdots & \frac{1}{n} \\
0 & \frac{1}{n-1} & \cdots & \frac{1}{n-1} \\
\frac{1}{n-1} & 0 & \cdots & \frac{1}{n-1} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{1}{n-1} & \frac{1}{n-1} & \cdots & 0
\end{array}\right], \quad i=1,2, \cdots, m
$$

## C. ASSIMILATION

Assimilation is often implemented by moving each colony toward its imperialist. Global search between colony and imperialist is frequently used in assimilation. If colonies only learn from its imperialist, the empire will easily fall into local optimum. In this study, a new strategy based on multi-elite individuals guidance is proposed.

Suppose that $H_{k}$ is the set of all colonies in empire $k$. The detailed steps of assimilation for empire $k$ are described in Algorithm 2.

```
Algorithm 2 Assimilation
    for each colony \(\lambda \in H_{k}\) do
        Generate a random number \(\alpha\) in \([0,1]\).
        if \(\alpha<0.5\) then
            Colony \(\lambda\) moves toward its imperialist \(k\). Two global
            search operations between \(\lambda\) and its imperialist \(k\) are
            executed sequentially.
        else
            Choose one solutions \(k^{*}\) from the other imperialists
            by tournament selection
            Colony \(\lambda\) learn from imperialist \(k^{*}\). Two global
            search operations between \(\lambda\) and imperialist \(k^{*}\) are
            executed sequentially.
        end if
    end for
```

Two global search operators are used for two strings. For the machine assignment string, a random number string $R S=\left\{r s_{1}, r s_{2}, \cdots, r s_{n}\right\}$ with length of $n$ is first generated,

start with the first element of $r s_{1}$, and for each element $r s_{i}$, if $r s_{i}>0.5$, then $M_{0_{i}}$ of colony $\lambda$ is replaced with that of imperialist $k$.

For the scheduling string, randomly select a segment $\phi$ from the scheduling string of imperialist $k$, then we decide the position $s$ of the first job of the segment $\phi$ in colony $\lambda$, delete all jobs of $\phi$ from the scheduling string of colony $\lambda$ and insert the segment $\phi$ into position $s$ sequentially.

Unlike the existing assimilation [26]-[34], the above assimilation make colonies guided by multi-elite individuals, which can avoid the algorithm falling into local optimum. Meanwhile, inspired by the above view, a new method is also proposed by using diversified strategies such as local search and EDA in revolution.

## D. REVOLUTION

Revolution is another way to generate new solutions. In general, revolution of colony is implemented by local search like mutation of GA and all colonies are changed in a single way. In this study, the diversified methods are adopted based on solution quality.

The detailed steps of revolution in empire $k$ are as follows. For each colony $\lambda \in H_{k}$, generate a random number $\beta$, if $\beta<p_{r}$, then if $c_{\lambda}$ is less than $\gamma$ colonies, conduct four neighborhood structures on $\lambda$ sequentially; else EDA is executed on $\lambda$, a new solution $z$ is obtained, if $z$ dominates colony $\lambda$, then replace colony $\lambda$ with $z$. Where $c_{\lambda}$ is the cost of colony $\lambda$ and we set $\gamma=0.8 N_{\text {cod }}$ based on experiments.

Neighborhood structures $\mathcal{N}_{1}, \mathcal{N}_{2}, \mathcal{N}_{3}, \mathcal{N}_{4}$ are used and described below. Neighborhood structure $\mathcal{N}_{1}$ generates new solutions by randomly choosing a machine $M_{i}$ and two jobs $J_{j}$ and $J_{k}$ on $M_{i}$, and then exchange them on scheduling string. $\mathcal{N}_{1}$ is just used to change scheduling string. Neighborhood structure $\mathcal{N}_{2}$ also acts on scheduling string. Randomly choose a machine $M_{i}$ and two jobs $J_{j}$ and $J_{k}$ on $M_{i}$, and then decide all jobs between $J_{j}$ and $J_{k}$ on $M_{i}$ and reverse their sequence on scheduling string. Neighborhood structure $\mathcal{N}_{3}$ is shown below. Randomly select machines $M_{i_{1}}$ and $M_{i_{2}}$, choose a job $J_{j}$ on $M_{i_{1}}$ and a job $J_{k}$ on $M_{i_{2}}$ stochastically, swap $J_{j}$ and $J_{k}$ on scheduling string and swap machines of two jobs on machine assignment string. Neighborhood structure $\mathcal{N}_{4}$ is done in the following way. As done in $\mathcal{N}_{3}$, machines $M_{i_{1}}$ and $M_{i_{2}}$, a job $J_{j}$ on $M_{i_{1}}$ and a job $J_{k}$ on $M_{i_{2}}$ are first randomly decided, then insert $J_{j}$ on the right of $J_{k}$ on scheduling string and assign $J_{j}$ from $M_{i_{1}}$ to $M_{i_{2}}$.

For a scheduling string $[3,5,1,2,6,4]$ and a machine assignment string $\left[M_{1}, M_{1}, M_{2}, M_{1}, M_{1}, M_{2}\right]$. When $\mathcal{N}_{1}$ and $\mathcal{N}_{2}$ are applied, $J_{5}$ and $J_{4}$ are chosen on $M_{1}$. For $\mathcal{N}_{3}$ and $\mathcal{N}_{4}$, $J_{5}$ on $M_{1}$ and $J_{6}$ on $M_{2}$ are selected. Fig. 2 gives the examples of $\mathcal{N}_{1}, \mathcal{N}_{2}, \mathcal{N}_{3}, \mathcal{N}_{4}$.

EDA generates a new solution by sampling the probability model. $\Theta$ is the set of all jobs.

The detailed steps of EDA for new solution are given in Algorithm 3.

In the above procedure, the chosen good colonies are improved by local search and the selected poor solutions are
![img-1.jpeg](img-1.jpeg)

FIGURE 2. Examples for four neighborhood structures.

## Algorithm 3 EDA Generate a New Solution

1: Calculate workload of all machines and decide the minimum workload of all machines.
2: if more than one machine has the minimum workload then
3: $\quad$ Randomly choose a machine $M_{i}$.
4: else
5: Directly select the machine $M_{i}$ with minimum workload.
6: end if
7: Determine the last job on machine $M_{i}$, supposing the job is $J_{j}$. If there is no job, set a virtual job 0 .
8: Select $J_{j}$ by using roulette wheel based on probabilities on lth or 0 th row of $\rho^{i}(g)$ and assign $J_{j}$ to $M_{i} . \Theta=$ $\Theta \backslash\left\{J_{j}\right\}$.
9: Let the $j$ th column of $\rho^{i}(g), i=1,2, \cdots, m$ to be zeros and normalize each row of the matrix.
10: if $\Theta$ is not empty then
11: Go to Step1.
12: else
13: Stop the algorithm.
14: end if
made better by global search of EDA, that is, two methods are used according to solution quality and global search ability and local search ability can be balanced well.

## E. EMPIRE AGGRESSION AND IMPERIALIST COMPETITION

A new step named empire aggression is added into NICA by local search of imperialist for plundering a randomly chosen colony.

Empire aggression is as follows. For each imperialist $k$, randomly select one of four neighborhood structures $\mathcal{N}_{1}$, $\mathcal{N}_{2}, \mathcal{N}_{3}, \mathcal{N}_{4}$ and acts on the imperialist $k$, a new solution $z$ is obtained, then a colony $\lambda$ is randomly chosen, if $z$ dominates colony $\lambda$, then colony $\lambda$ is displaced by solution $z$ and this colony is moved from its empire to empire $k$.

After the process of empire aggression, the cost of all countries is calculated again and imperialist of each empire is updated if a colony dominates its imperialist.

To implement imperialist competition, total cost $T C_{k}$ is first defined by

$$
T C_{k}=c_{k}+\xi \frac{\sum_{i \in H_{k}} c_{i}}{N C_{k}}
$$

where $\xi$ is a positive number. We set $\xi=0.1$.
Then the normalized total cost $N T C_{k}$, power $T P_{k}$ and a probability vector $V$ are first computed by

$$
\begin{aligned}
N T C_{k} & =\max _{l \in Q}\left\{T C_{l}\right\}-T C_{k} \\
T P_{k} & =N T C_{k} / \sum_{l \in Q} N T C_{l} \\
V=T P-R & =\left[T P_{1}-r_{1}, T P_{2}-r_{2}, \cdots, T P_{N_{t m p}}-r_{N_{t m p}}\right]
\end{aligned}
$$

where $R=\left\{r_{1}, r_{2}, \cdots, r_{i m p}\right\}$ is a random number vector, $r_{i}$ follows uniform distribution in $[0,1]$ and Q is the set of all imperialists.

Finally, a winning empire $k$ with the biggest $T P_{k}-r_{k}$ is decided, EDA is applied and a new solution $z$ is generated, if $z$ dominates the weakest colony of the weakest empire, then the weakest colony is replaced with $z$ and moved from the weakest empire to empire $k$; otherwise, the weakest colony is directly included into empire $k$.

In the above procedure, EDA is used to try to avoid adding directly the worst colony into the winning empire because the weakest colony is a worse solution and difficult to be improved even if it is included into a strong empire.

## F. ALGORITHM DESCRIPTION

NICA is constructed by incorporating EDA into revolution and imperialist competition, respectively; moreover, there are different purposes. EDA is adopted in revolution to update colony and EDA is applied to avoid the direct inclusion of the weakest colony into the winning empire. Meanwhile, multi-elite individual guidance strategy is added in assimilation that colonies can move toward other imperialists. These are the great differences between NICA and other ICAs [33], [44], [45]. In fact, ICA is seldom hybridized with EDA. This study gives an effective hybrid method.

The detailed procedure of NICA is shown in Algorithm 4.
The stopping condition is max_it, which is maximum number of objective function evaluations. Fig. 3 shows the flow chart of NICA.

With respect to the updating probability matrices, at each generation, we choose $0.1 \times N$ individuals with smallest cost from population $P$ as elite solutions according to Wang and Zheng [18]. Probability matrices are updated by the usage of of these elite solutions.

$$
\rho_{j, k}^{i}(g+\mathrm{I})=(1-\alpha) \rho_{j, k}^{i}(g)+\frac{\alpha}{0.1 \times N} \sum_{z=1}^{0.1 \times N} I_{i, j, k}^{z}
$$

## Algorithm 4 NICA

1: Produce an initial population $P$ by heuristics and random way, let $g=1$.
2: Construct initial empires and probability matrices.
3: while The stopping criterion is not met do
4: Execute assimilation and revolution in each empire.
5: Perform empire aggression, calculate cost of all countries and exchange.
6: Execute imperialist competition and update the probability matrices, $g=g+1$.
7: end while
where $\alpha \in(0,1)$ is the learning rate, and $I_{i, j, k}^{z}$ is a $0-1$ variable. In the $z$ th solution, If job $J_{k}$ is right after job $J_{j}$ on machine $M_{i}, I_{i, j, k}^{z}$ is one; Otherwise $I_{i, j, k}^{z}$ is equal to zero.

## IV. COMPUTATIONAL EXPERIMENTS

Extensive experiments are conducted on a set of problems to test the performance of NICA for UPMSP with PM and SDST. All experiments are implemented by using matlab2015b and run on 16.0G RAM 2.80GHz CPU PC.

## A. TEST INSTANCES, METRICS AND COMPARATIVE ALGORITHMS

Test sets of small, medium and large scale $[11,15]$ can be selected to evaluate the algorithmic performance. There exist 66 instances. For small instances, $n \in\{10,12\}$ and $m \in\{2,3\}$. For medium instances, $n \in\{20,30\}$ and $m \in$ $\{2,3,4\}$. For large instances, $n \in\{50,100,150,200\}$ and $m \in\{10,15,20\} . p_{i j} \in[1,99]$. There are three types of setup times, which are chosen from $[1,9],[1,99]$ and $[1,124]$. The processing time and setup times of small and large scales are taken from http://www.cima.uadec.mx/instancias/. The medium scale is generated randomly according to the literature [12]. $w_{i} \in[1,99]$, the length of processing interval is decided by

$$
u_{i}=(1+\delta) \times \max _{\forall j}\left\{s_{i l j}+p_{i j}+s_{j i 0}\right\}
$$

Duedate $d_{j}$ of job $J_{j}$ is computed by

$$
d_{j}=(1+2 \delta) \times \sum_{i=1}^{m} p_{i j} / m
$$

where $\delta$ is a random number between 0 and 1 .
Two metrics are used. Metric $D I_{R}$ [46] is applied to measure the convergence performance by computing the distance of the non-dominated set $\Omega_{l}$ relative to a reference set $\Omega^{*}$.

$$
D I_{R}\left(\Omega_{l}\right)=\frac{1}{\left|\Omega^{*}\right|} \sum_{y \in \Omega^{*}} \min \left\{\sigma_{x y} \mid x \in \Omega_{l}\right\}
$$

where $\sigma_{x y}$ is the distance between a solution $x$ and a reference solution $y$ in the normalized objective space. The reference set $\Omega^{*}$ is composed of the non-dominated set solutions in $\bigcup_{l} \Omega_{l}$.

The smaller $D I_{R}\left(\Omega_{l}\right)$ is, the better the algorithm is. $D I_{R}\left(\Omega_{l}\right)=0$ means that algorithm $l$ provides all members of the set $\Omega^{*}$.

![img-2.jpeg](img-2.jpeg)

FIGURE 3. The flow chart of the NICA.

Metric $\rho$ [47] indicates the ratio of number of the elements in the set $\left\{x \in \Omega_{l} \mid x \in \Omega^{*}\right\}$ to $\left|\Omega^{*}\right|$.

As stated above, multi-objective UPMSP with PM and SDST is seldom investigated and there are no existing comparative algorithms. In this study, we compare NICA with multi-objective multi-point simulated annealing (MOMSA [48]) and multi-objective harmony search (MOHS) algorithm [49].
MOMSA is proposed for solving multi-objective UPMSP by simultaneously minimising makespan, total weighted completion time and total weighted tardiness. The effectiveness of MOMSA is verified. Meanwhile, MOMSA can be directly applied to solve multi-objective UPMSP with PM and SDST by considering setup times and maintenance in decoding process.

As for MOHS, it presented to minimize the makespan, tardiness penalties and the purchasing cost of machines simultaneously. The effectiveness of MOHS is verified by the comparison with multi-objective particle swarm optimization, NSGA-II, and multi-objective ACO. MOHS can also be

TABLE 1. Parameters and their levels.


directly used to solve multi-objective UPMSP with PM and SDST by adding setup times and maintenance in decoding process.

## B. PARAMETER SETTINGS

NICA has five important parameters: maximum number of objective function evaluations max it, population scale $N$, the ratio of number of imperialists to population scale $N_{\text {imp }} / N$, revolutionary probability $p_{r}$ and learning rate $\alpha$.

A three-level design of experiment is designed on an instance with 20 machines and 200 jobs. Table 1 gives the

![img-3.jpeg](img-3.jpeg)

FIGURE 4. Main effect plot of $D I_{R}$.

TABLE 2. The orthogonal array $L_{27}\left(5^{5}\right)$.


settings of each parameter at each level. Orthogonal arrays of different parameter levels are given in Table 2. For each group of parameters, NICA runs independently 20 times. $D I_{R}$ is used to evaluate the results of each parameter combination, where the reference set $\Omega^{*}$ is composed of the non-dominated solutions from the union set of all sets $\Omega$ of NICA. The results are shown in Table 2. Table 3 describes the average $D I_{R}$ of each parameter. The main effect plot of mean is shown in Fig. 4.

TABLE 3. Computational results.

From Table 3, we can see that $N$ has the greatest influence on the result of the algorithm. Meanwhile, when max_it increases from $5 \times 10^{4}$ to $10^{5}$, the results of NICA improve a lot. However, when max_it is greater than $10^{5}$, NICA improves little. Therefore, in order to balance the performance and time consumption of the algorithm, we set $\max _{-} i t=10^{5}$. The other parameters are as follows: $N=100, N_{\text {im }} / N=0.1, p_{r}=0.4, \alpha=0.05$.

## C. STRATEGY EFFECTIVENESS ANALYSIS

NICA is built by the combination of EDA and ICA, inclusion of empire aggression and the usage of two heuristics in initialization.

Three variants of NICA are constructed. NICA1 is similar with NICA except that initial population is generated randomly. The difference between NICA and NICA2 lies in the elimination of EDA from NICA. In NICA3, colonies only can move toward its imperialist in assimilation. The parameter settings are as same as NICA. Each algorithm runs independently 20 times. Tables 4 and 5 show the computational results of NICA and its three variants and Fig. 5 and 6 describes the boxplot of four NICAs of the computational results. Table 9 shows the statistic results. We set confidence level as $95 \%$. When $p_{\text {_value }}<0.05$, the difference between algorithms is significant.

TABLE 4. Computational results of four NICAs on metric $D I_{R}$.

TABLE 5. Computational results of four NICAs on metric $\rho$.

It can be found that NICA has smaller $D I_{R}$ than NICA1 on 49, and is only worse than NICA1 on 6 instances. As for metric $\rho$, NICA1 is better than or equal to NICA1 on

63 instances. The inclusion of two heuristics really improves the performance of NICA. With respect to NICA2, it is inferior to NICA on two metrics, $D I_{R}$ of NICA2 is worse

TABLE 6. Computational results of three algorithms on metric $D I_{R}$.

![img-4.jpeg](img-4.jpeg)

FIGURE 5. Boxplot of four NICAs on metric $D I_{R}$.
than or equal to that of NICA2 on 47 instances and $\rho$ of NICA1 is bigger than or equal to that of NICA2 on 52 instances, that is, the hybridization of ICA with EDA are effective and efficient. As stated in Tables 4 and 5, NICA performs better than NICA3. NICA produces smaller $D I_{R}$ than or identical $D I_{R}$ with NICA3 on 64 instances and obtains bigger $\rho$ than NICA3 on 63 instances. The multielite individuals guidance strategy is really necessary. The same conclusions also can be drawn by the statistical results in Table 9 and Fig. 5 and 6, thus, three new strategies of NICA have positive impacts on its performances.
![img-5.jpeg](img-5.jpeg)

FIGURE 6. Boxplot of four NICAs on metric $\rho$.

## D. COMPARATIVE ANALYSIS WITH OTHER ALGORITHMS

To analyze the superiority of NICA in solving UPMSP with PM and SDST, we compare NICA with MOMSA and MOHS. The parameters of MOMSA and MOHS are directly adopted from Lin and Ying [48] and Shahidi-Zadeh et al. [49] expect the termination condition. Three algorithms have the same termination condition: max_it $=10^{5}$. Each algorithm runs independently 20 times. Tables 6, 7 and 8 list the results and computational time of NICA and two comparative algorithms. Fig. 7 and 8 shows the boxplot of the computational results.

TABLE 7. Computational results of three algorithms on metric $\rho$.

TABLE 8. Computational time (seconds) of three algorithms.

As stated in Tables 6 and 7, MOMSA obtains better $D I_{R}$ than NICA on only 2 instance and MOMSA is inferior to NICA on $\rho$ on 62 instances. With respect to MOHS, NICA
gets smaller results of $D I_{R}$ than MOHS on 51 instances and has greater $\rho$ than MOHS on 51 instances. Moreover, $D I_{R}$ of NICA is 0 on 40 instances and NICA provides all members

![img-6.jpeg](img-6.jpeg)

FIGURE 7. Boxplot of three algorithms on metric $D l_{R}$ -
![img-7.jpeg](img-7.jpeg)

FIGURE 8. Boxplot of three algorithms on metric $\rho$.
of the set $\Omega^{*}$ on 40 instances. We also can find from the Fig. 7 and 8 that NICA has better performance than other algorithms. The statistical results in Table 9 are in agreement with this conclusion. Thus, NICA can get better results than other two algorithms on most of instances in similar computation times and has promising advantages in solving UPMSP with PM and SDST.

TABLE 9. Results of paired sample t-test

Colonies moving toward other imperialists can avoid the algorithm falling into local optimum. Meanwhile, different strategies in revolution are beneficial to make good balance between global search and local search. New added step and imperialist competition can make full use of good solutions. Besides, initialization can guarantee that the search of NICA starts with good initial population. Based on the above analysis, it can be concluded that NICA can effectively solve the UPMSP with PM and SDST.

## V. CONCLUSION

UPMSP with PM and UPMSP with SDST are often studied; however, UPMSP with PM and SDST is seldom considered. In this paper, a new novel algorithm called NICA is proposed to solve UPMSP with PM, SDST and the minimization of makespan and total tardiness. Two heuristics are designed to initialize population. Multi-elite individuals guidance strategy is designed in assimilation that colonies can move toward other imperialists. EDA is adopted in revolution and imperialist competition for different purposes. A novel step named empire aggression is introduced by local search of imperialist for plundering a randomly chosen colony. Extensive experiments are conducted and the computational results show that NICA provides promising results for the considered UPMSP.

UPMSP with practical processing constraints such as SDST is an important one and extensively exists in the actual manufacturing systems. In the near future, we will continue to focus on this kind of problem and apply some meta-heuristics such as shuffled frog-leaping algorithm and teaching-learning-based optimization to solve it. Energyefficient distributed scheduling in multiple factories is also our future topics. We will investigate distributed scheduling problems in unrelated parallel machines environment.
