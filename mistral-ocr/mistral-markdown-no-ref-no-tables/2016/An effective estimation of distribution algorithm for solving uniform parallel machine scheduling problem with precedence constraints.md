# An Effective Estimation of Distribution Algorithm for Solving Uniform Parallel Machine Scheduling Problem with Precedence Constraints 

Chu-ge Wu, Ling Wang, Xiao-long Zheng<br>Department of Automation, Tsinghua University<br>Beijing, China<br>E-mail: wucg15@mails.tsinghua.edu.cn; wangling@tsinghua.edu.cn; zhengx111@mails.tsinghua.edu.cn


#### Abstract

In this paper, an effective estimation of distributed algorithm (eEDA) is proposed to solve the uniform parallel machine scheduling problem with precedence constraints (prec-UFPMSP). In the eEDA, the permutation-based encoding scheme is adopted and the earliest finish time (EFT) method is used to decode the solutions to the detail schedules. A new effective probability model is designed to describe the relative positions of the jobs. Based on such a model, an incremental learning based updating method is developed and a sampling mechanism is proposed to generate feasible solutions with good diversity. In addition, the Taguchi method of design-ofexperiment (DOE) method is used to investigate the effect of key parameters on the performance of the eEDA. Finally, numerical tests are carried out to demonstrate the superiority of the probability model, and the comparative results show that the eEDA outperforms the existing algorithm for most cases.


Keywords-precedence constraint scheduling, uniform parallel machine, $E D A$, relative position probability model

## I. INTRODUCTION

The parallel machine scheduling problem (PMSP) is one of the typical scheduling problems, which has been proved to be NP-hard [1]. The precedence constraints widely exist in the real world manufacturing systems, such as allocation of workflow in cloud computing [2], wafer probing scheduling [3], and block erecting in shipbuilding [4]. Therefore, the precedence constraints between the jobs need to be considered for the PMSP in many real-world situations. Due to its practical significance, the PMSP with precedence constraints has attracted increasing attention. This paper deals with the uniform parallel machine scheduling problem with precedence constraints (prec-UFPMSP) with makespan criterion. The problem is more complex than PMSP, because it should determine the processing sequence of the jobs and the machine assignment together. In addition, it is a relaxation of the prevailing complex scheduling problems, such as the resource constrained project scheduling problem (RCPSP) [5]. The effective solution algorithms for the prec-UFPMSP can also be promoted to solve the RCPSP. Therefore, it is of practical and

[^0]academic significance to design effective algorithms for the prec-UFPMSP.

The estimation of distribution algorithm (EDA) [6] is a population-based evolutionary algorithm, which has been one of the focus among the evolutionary computing techniques in solving the complex optimization problems during recent years. The EDA generates new solutions by sampling the probability model, which is used to describe the distribution of the promising solutions in the search space. The EDA has been shown to be effective in solving many academic and engineering optimization problems in a variety of fields [7]. Inspired by the successful applications of the EDA, especially in the field of production scheduling, the EDA will be adopted in this paper to solve the prec-UFPMSP. To well solve the problem, a novel probability model of EDA is designed for the prec-UFPMSP to describe the relative positions between the jobs; and a novel sampling mechanism is proposed to generate feasible solutions so as to handle the precedence constraints effectively. Numerical tests show that the best known solutions of 33 out of 48 benchmarking instances have been updated by the proposed algorithm.

The reminder of the paper is organized as follows: Section 2 reviews the related work on this problem. The description and a mathematical model of the prec-UFPMSP are provided in Section 3. Then, the eEDA is proposed in details in Section 4. In Section 5, the effect of parameter setting is investigated and numerical comparisons are provided. Finally, the paper is ended with some conclusions and future work in Section 7.

## II. RELATED WORK

For the prec-PMSP, there exist the following studies about the mathematical models. Aho et al [8] studied the jobs with unit processing time on parallel machines with makespan criterion. Munier et al [9] presented the approximation bounds for the PMSP with the constrains, such as ordinary precedence constraints, release dates and delivery times. Chekuri et al [10] analyzed the minimization of total weighted completion times on a single machine. Liu and Yang [11] also presented a mathematical model for prec-UFPMSP.

As for the solution algorithms, there exist the following typical work for the parallel machine scheduling problem with


[^0]:    This work is supported by the National Key Basic Research and Development Program of China (No. 2013CB329503) and the National Science Fund for Distinguished Young Scholars of China (No. 61525304).

precedence constraints. In [9], Munier et al proposed heuristic algorithms for the prec-PMSP. In [12], a heuristic method was proposed to solve the prec-UFPMSP, and the local search methods and simulated annealing mechanism were also developed based on the heuristic method. But only the precedence constraint in chains (a job has at most one succeed and one predecessor) was considered. Liu and Yang [11] also developed some heuristic methods. Hassan et al [13] adopted the genetic algorithm (GA) to solve the prec-UFPMSP and realized a heuristic method for comparison. Under the background of the allocation of the workflow in cloud environment, Szabo et al [2] proposed an algorithm to solve the prec-PMSP. A problem specific operator was designed, and both single-objective and multi-objective situations were considered. Besides, setup times of jobs were added to generalize the problem to more complex ones. And the list scheduling methods were adopted in $[5,14]$.

Due to the complexity caused by the precedence constraints between the jobs, the generation way of the feasible solutions also caught much attention. Hassan et al [13] guaranteed the feasibility through a repairing mechanism. Omara et al [15] designed a specific crossover operator and a mutation operator to generate feasible solutions. Wang et al [16] proposed an EDA with a special probability model and a sampling mechanism to generate feasible solutions. Afzalirad and Rezaeian [17] considered the unrelated parallel machine problem with constraints, and they proposed a new corrective algorithm to obtain the feasible solutions at every stage of the algorithm.

## III. PROBLEM FORMULATION

The prec-UFPMSP can be described as follows. There are $n$ jobs to be processed on $m$ machines with different speed ratios. Each job can be executed on any machine. The processing time of job $j$ on machine $i$ is calculated as $p_{i j}=p_{j} \times s_{i}$, where $s_{i}$ denotes the speed ratio of machine $i$ and $p_{j}$ denotes the processing time of job $j$. The objective is to determine the job processing sequences on all the machines so as to minimize the makespan. In addition, the precedence relationship should be considered. If one job is precedent of the other, then the latter one cannot be processed until the former one finishes its processing. The problem can be represented as $Q \mid \operatorname{prec} \mid C_{\max }$.

## A. Notation

$n$ : the number of jobs to be processed;
$m$ : the number of machines;
$C_{i}: C_{i} \geq 0$, the completion time of job $j$;
$p_{j}$ : the processing time of job $j$ on machine $i$;
$x_{i v}:\{0,1\} . x_{i v}=1$ illustrates that job $j$ is the $r$-th job
processed on machine $i$, otherwise, $x_{i v}=0$.
$M$ : a very large constant.
$i \rightarrow j$ : job $i$ is precedent of job $j$.

## B. Mathematical model [13]

$$
\min \max _{j=1,2, \ldots, n} C_{j}
$$

Subject to:

$$
\begin{gathered}
\sum_{i=1}^{n} \sum_{r=1}^{n} x_{j i r} \approx 1 . \quad j=1,2, \ldots, n \\
\sum_{j=1}^{n} x_{j i r} \leq 1 . \quad i=1,2, \ldots, m ; \forall r \\
\sum_{j_{1}=1}^{n} x_{j_{1} i r+1}-\sum_{j_{2}=1}^{n} x_{j_{2} i r} \leq 0 . \quad i=1,2, \ldots, m ; r=1,2, \ldots, n-1 \\
C_{j_{1}}-C_{j 2}+M\left(2-x_{j_{1} i r+1}-x_{j_{2} i r}\right) \geq p_{j_{1} i} \\
i=1,2, \ldots, n ; r=1,2, \ldots, n-1 ; \forall j_{1} \neq j_{2} \\
C_{j_{1}}-C_{j_{2}} \geq \sum_{i=1}^{m} \sum_{r=1}^{n} p_{j_{1} i} x_{j_{1} i r} . \quad \forall j_{1} \rightarrow j_{2} \\
C_{j} \geq \sum_{i=1}^{n} p_{j i} x_{j i 1} . \quad j=1,2, \ldots, n
\end{gathered}
$$

where (1) is the objective function; and constraint (2) guarantees that each job must be processed only once; and (3) ensures each machine processes no more than one job at the same time; and constraint (4) means that the jobs on a certain machine are in order; and constraint (5) gives the limitation to the completion times of the adjacent jobs on the same machine; and (6) ensures the precedence constraints between jobs; and constraint (7) considers the completion time of the first job on each machine.

## IV. THE PROPOSED EDA

In this section, the proposed algorithm will be introduced in details. Firstly, the encoding and decoding methods are proposed; secondly, the probability model and its initialization mechanism are presented. Then, the sampling method is introduced. Finally, the flowchart of the eEDA is provided.

## A. Encoding and decoding method

In the eEDA, a job processing order permutation $\pi$ is used to represent a solution, where $\pi_{i}$ represents the $i$-th job to be scheduled.

In order to generate the feasible solutions in accordance with the precedence constraints, job $i$ is placed before job $j$ in the permutation if job $i$ is the precedent of job $j$. These permutations that do not violate the precedence constraints are defined legal ones. The legal permutations consist of a dominant set of schedules, which contain at least one optimal schedule [14]. It guarantees that the encoding mechanism can cover the best solution. Therefore, the eEDA is designed to generate legal permutations. In addition, by considering the legal permutations only, it can reduce the search space and save computational cost.

The eEDA maps the solutions into the detail schedules by using the earliest finish time formulation (EFT). For each solution, the jobs in the permutation are assigned to the

machine based on the EFT until all the jobs are scheduled. To explain the decoding mechanism, a problem with 2 machines and 4 jobs is used as an example. Suppose $s_{1}=2, s_{2}=3$, and $p_{i}=1$ $(j=1,2,3,4)$. The precedence constraints between jobs are $2 \rightarrow 3$, $2 \rightarrow 4$ and $3 \rightarrow 4$.

Without loss of generality, a legal processing permutation $(1,2,3,4)$ is considered. Let $C_{j i}$ denote the completion time of job $j$ on machine $i$. Job 1 is scheduled first according to the permutation. Since $p_{11}=2 \times 1=2$ and $p_{12}=3 \times 1=3$, thus $C_{11}=2$ and $C_{12}=3$. Because $C_{11}<C_{12}$, job 1 is scheduled on machine 1 according to the EFT. Then, job 2 is considered. There is no precedence constraint between job 1 and job 2 , and $C_{22}=p_{22}=3$ $<C_{21}=C_{11}+p_{21}=2+2=4$, so job 2 is scheduled on machine 2 . Since there exists precedence constraint between job 2 and job 3 , job 3 cannot start until job 2 finishes its processing. The completion time of job 3 on different machines can be calculated as $C_{31}=C_{2}+p_{31}=3+2=5$ and $C_{32}=C_{2}+p_{32}=3+3=6$. Job 3 is scheduled to machine 1 , since $C_{31}<C_{32}$. And job 4 is assigned to machine 1 because $C_{41}<C_{42}$. Therefore, the Gantt chart of the corresponding schedule is illustrated in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Corresponding Gantt chart of the solution

## B. Probability model

The probability model plays an important role in the EDA since it describes the distribution of the solutions in the search space and the solutions are generated by sampling the model. If the model can well reflect the characteristics of the problem, it may be easier to obtain better solutions.

In the prec-UFPMSP, the precedence constraints provide the relative position information between some job pairs. In many existing work, the absolute position model was adopted. Such kind of model only describes the probability that a job is placed at different positions, but it cannot represent the relative position relationship between jobs, which is related to the feasibility of solutions in the problem with precedence constraints. To overcome the shortcoming of the absolute position model, a relative position is designed in the eEDA. The model transfers the precedence constraint information into the probability value to describe the search space. Thus, a probability model $P(\mathrm{~g})$ considering the relative position is designed as follows.

$$
P(g)=\left[\begin{array}{cccc}
0 & \rho_{12}(g) & \cdots & \rho_{1 n}(g) \\
\rho_{21}(g) & 0 & \cdots & \rho_{2 n}(g) \\
\vdots & \vdots & \ddots & \vdots \\
\rho_{n 1}(g) & \rho_{n 2}(g) & \cdots & 0
\end{array}\right]
$$

In (8), element $\rho_{i j}(g)$ represents the probability that job $i$ is placed in front of job $j$ in the permutation at the $g$-th generation. Clearly, $\forall i, j, g, \rho_{i j}(g)+\rho_{j i}(g)=1$. Note that, $\forall j, g, \rho_{j j}(g)=0$ means that each job is impossible to be placed in front of itself.

The initialization mechanism is designed to make use of the information of the problem. As mentioned before, if job $i$ is the precedent of job $j$, job $i$ must be placed in front of job $j$. Therefore, $\rho_{i j}(0)$ is set to be 1 and $\rho_{i i}(0)$ is 0 . On the other hand, if the precedence relationship between the jobs is not given, $\rho_{i j}(0)$ and $\rho_{j i}(0)$ are both set to be 0.5 . The probability values of $\rho_{i j}$ are initialized as follows:

$$
\rho_{i j}(0)=\left\{\begin{array}{c}
1, i \rightarrow j \\
0, j \rightarrow i \\
0.5, \text { otherwise }
\end{array}\right.
$$

In the procedure of updating the model, all solutions are sorted in an ascending order with respect to the makespan, and the top EPSize solutions are selected to construct the elite population.

The probability values of the model are updated using the population based incremental learning method (PBIL) [18] as follows:

$$
p_{i j}(g+1)=(1-\alpha) p_{i j}(g)+\alpha \frac{1}{\text { EPSize }} \sum_{k=1}^{E P S i z e} I_{i j}^{k}(g)
$$

where $\alpha \in(0,1)$ represents the learning rate and $I_{i j}^{k}(g)$ is the following indicator function corresponding to the $k$-th solution of the elite population.

$$
I_{i j}^{k}(g)=\left\{\begin{array}{l}
1, \text { if job } i \text { is before job } j \text { in the } k-\text { th individual } \\
0, \text { otherwise }
\end{array}\right.
$$

## C. Sampling method

The population is generated by sampling the probability model in the eEDA and the elements in the permutation are sampled independently.

For each element $\pi_{i}(i=1 \ldots n)$ in the permutation, the Pseudo code of the sampling procedure is shown in Fig 2.

```
sample_array[n]=0;
sum=0;
for \(j=0 ; j \leq n ; j++\) do
    sample_array[j] = \(\prod_{k \in C_{j}} P[k][j] ;\)
    sum += sample_array[j];
for \(j=0 ; j \leq n ; j++\) do
    sample_array[j] = sample_array[j]/sum;
\(\pi_{i}=\) RouletteWheelMethod(sample_array);
return \(\pi_{i}\);
```

Fig. 2. Pseudo code of sampling an element in the permutation

In the procedure, a temporary probability array sample_array is built to sample the job number, and $C$ is the set of the jobs that are not scheduled till now, and the function RouletteWheelMethod (sample_array) illustrates that $\pi_{i}$ is generated by the roulette wheel method based on sample_array. The sampling method guarantees that the generated permutations are legal. Besides, due to the designed sampling method, all the solutions generated by sampling $P(0)$ do not violate the precedence constraints. According to (10), the fixed 0 and 1 in the probability model will not be altered, which guarantees the solutions sampled based on the probability model are legal during the whole procedure of evolution.

## D. Flowchart

With the above design, the flowchart of the proposed eEDA is illustrated in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Flowchart of the eEDA
In the initialization phase, the probability model is initialized based on the precedence constraints. Then, the eEDA uses the EDA-based mechanism to sample the relative position probability model to construct the population. After that, it sorts the population and determines the best EPSize individuals as the elite population. Then, it updates the probability values according to the elite population. In such a way, the algorithm runs until the stopping condition is met.

## V. NUMERICAL RESULTS AND COMPARISONS

To test the performances of the eEDA, numerical tests are carried out using a set of benchmarking instances [13]. The testing set consists of $48=4 \times 4 \times 3$ instances, where $n=\{20,50$, $100,200\}$ and $m=\{2,5,10,20\}$. For each combination of the number of machine and job, 3 different instances are generated, in which the densities of precedence constraints are high, medium and low, respectively. The eEDA is implemented in C language and run on a personal computer with a 2.83 GHz processor and 4GB RAM.

## A. Parameter setting

The eEDA has three key parameters: PSize (size of the population), and $\eta$ (percentage of elite solutions, EPSize $=$ PSize $=\eta \%$ ), and $\alpha$ (learning rate). To investigate the effect of these parameters, the Taguchi method of design-of-experiment method (DOE) [19] is employed, where a moderate scaled instance ( $m=5, n=100$ and the density is high) is used. The stopping criterion is set the same one as [13], i.e. 10 seconds.

Considering the scale of the benchmarking instances, four factor levels are employed and the different values of these parameters are listed in Table I. The orthogonal array $\mathrm{L}_{16}\left(4^{3}\right)$ is chosen accordingly. For each parameter combination, the eEDA is run 20 times independently and the average value of 20 runs is used as the response variable (RV) value. The orthogonal array and RV values are listed in Table II.

TABLE I. FACtOR LEVELS OF PARAMETERS


TABLE II. THE RV VALUE

According to the results, the influence trend of each parameter is illustrated in Fig. 4. The significance rank of each parameter is analyzed and the results are listed in Table III.
![img-2.jpeg](img-2.jpeg)

Fig. 4. The influence trend of each parameter

From Fig. 4 and Table III, it can be seen that all the parameter values should be set neither too small nor too large. The percentage of elite population is of the most significant impact. A small value of $\eta$ may result in that useful information obtained from the elite population is not enough to update the probability model, while a big value of $\eta$ may bring the worse solutions into the elite population and decrease the accuracy of the model. The significance of PSize ranks the second. The Psize affects the balance of search breadth and depth. Thus, a moderate value is preferred. Although $\alpha$ has the slightest influence, a small value of $\alpha$ may slow the convergence of the probability model, while a large value may lead to premature convergence.

TABLE III. RESPONSE TABLE


For further investigation, non-parametric tests are carried out. According to the results of DOE, PSize $=150, \eta=2$, and $\alpha$ $=0.1$ are recommended for parameter setting. In the nonparametric tests, we alter one parameter value and keep the other two parameters fixed as the recommended values to investigate the effect. For each parameter combination, the eEDA is run 20 times independently and the average makespan value of 20 runs is used as RV value. Then, the Kruskal-Wallis test (with $95 \%$ confidence) is carried out based on the RV values and the results are shown in Table IV.

TABLE IV. KRUSKAL-WALLIS TESTS FOR THE PARAMETERS

It can be seen from Table IV that the difference between the eEDAs with variable parameter settings is not significant. In other word, the eEDA is not sensitive to the parameter values. Due to the robustness of the eEDA, the choice of parameter combination does not affect its performance too much. To obtain better results, the recommended values based on the results of DOE are adopted.

## B. Superiority of the probability model

To testify the superiority of the relative position probability model, the eEDA is compared with the EDA adopting the absolute position model. Considering that there is no EDA applied to solve the prec-UFPMSP while the problem can be regarded as a special case of the RCPSP, we reimplement the pareto-archived EDA (PAEDA) [16] for comparisons, which is proposed for the RCPSP by using the absolute position model. For a fair comparison, the two algorithms use the same parameter values as aforementioned values but are different in terms of the probability model and the sampling method.

To be specific, the job processing permutation is adopted by the PAEDA to encode the problem in [16], and the following absolute position probability model is used.

$$
M_{-} \operatorname{act}(g)=\left[\begin{array}{ccc}
\alpha_{11}(g) & \cdots & \alpha_{1 n}(g) \\
\vdots & \ddots & \vdots \\
\alpha_{n 1}(g) & \cdots & \alpha_{n n}(g)
\end{array}\right]
$$

where element $\alpha_{j i}(g)$ represents the probability that job $j$ is set at the $i$-th place in the permutation at the $g$-th generation.

The probability model is initialized uniformly, that is $\alpha_{i j}(0)=1 / n, \forall i, j$. To obtain feasible solutions, the probability vector of the PAEDA is defined as follows.

$$
P_{\alpha_{i j}}=\alpha_{j i} / \sum_{h=1}^{S_{i j}} \alpha_{h i}
$$

where $P_{\alpha_{i j}}$ represents the sampling probability that job $j$ is chosen at the $i$-th position in the permutation, and $S_{0}$ denotes the set of the active jobs at position $i$ (the jobs whose preceding jobs have been scheduled). After job $j$ is chosen, the $j$-th row of the probability model $\left(\left(\alpha_{j 1}(g), \alpha_{j 2}(g) \cdots \alpha_{j n}(g)\right)\right.$ in the $M_{-} \operatorname{act}(g)$ is set as 0 to avoid generating the repeated job $j$ in the solution.

Both algorithms are run 20 times independently. For further statistical analysis, the student's t-test is used to show the whether the proposed model is superior over that of the PAEDA significantly. The average results and the statistical test results are listed in Table V. If the $p$-value is less than 0.05 , the difference between the algorithms are statistically significant at $95 \%$ confidence level, which is denoted ' Y '; otherwise, ' N '.

It can be seen from Table V that, for most low density cases, the eEDA outperforms the PAEDA significantly. For the medium density cases, the PAEDA outperforms the eEDA on $n=20$. The possible reason is the PAEDA is of better exploitation ability due to its probability model and sampling mechanism. Thus, the PAEDA performs better on the small scaled instances. For the high density cases, there are more precedence constraints between the jobs and the legal solutions are limited. Both the two algorithms can obtain the best solutions on $n=20$, and on $n=50$ the PAEDA still outperforms the eEDA. However, on the large scaled instances, the eEDA is much superior to the PAEDA. So, it can be concluded that the eEDA is able to locate good solutions quickly and has better exploration ability.

## C. Comparison with existing algorithm

In [13], Hassan et al proposed a powerful GA for the precUFPMSP and provided the best results with the stopping criterion of 10 seconds time limits. Here, we also set the time limit with 10 seconds. In Table VI, the best and average results are listed by running the eEDA 20 times independently.

TABLE VI. BEST AND AVERAGE RESULTS OF GA AND EDA


Note: The bold values mean the best results
From Table VI, it can be seen the eEDA outperforms the GA in most instances. On $87.5 \%$ of the instances the best results of the eEDA are not worse than that of the GA, and on $83.3 \%$ instances the average results of the eEDA are not worse than that of the GA. In most situations, especially on the large scaled instances, the eEDA performs much better than the GA. The reason mainly lies in that the eEDA has good exploration ability and on the large scale instance the eEDA can locate the good searching space quickly. Moreover, the probability model and its sampling mechanism are helpful to find the feasible solutions. However, on several large-scaled instances with medium density, GA has better performance. So, further research is still needed for the eEDA to enhance its search ability for most cases, such as the hybridization with local search.

## VI. ConCLUSIONS

In this paper, an effective EDA is proposed to solve the prec-UFPMSP with the makespan criterion. Some best solutions of the benchmarking instances [13] are updated by the proposed eEDA. The main contribution of this work is to
propose a simple but effective probability model and the sampling mechanism to deal with the precedence constraints between jobs. The probability model utilizes the characteristics of the problem in the initialization procedure. In addition, the sampling mechanism is able to produce the feasible solutions effectively. Due to the simplicity, the eEDA can be used to initialize the feasible population or contribute to a part of the solver for other complex problems such as the RCPSP.

As for the future work, it is interesting to design a selfadaptive probability model according to the characteristic of the problem or to develop an adaptive way to utilize the merits of different models. In addition, the proposed could be generalized to the with more complexity like the distributed production systems.
