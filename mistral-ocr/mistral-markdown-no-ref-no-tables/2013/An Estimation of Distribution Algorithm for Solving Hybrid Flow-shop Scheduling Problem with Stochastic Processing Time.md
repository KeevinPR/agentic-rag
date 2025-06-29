# An Estimation of Distribution Algorithm for Solving Hybrid Flow-shop Scheduling Problem with Stochastic Processing Time 

WANG Shengyao ${ }^{1}$, WANG Ling ${ }^{1}$, XU Ye ${ }^{1}$<br>1. Tsinghua National Laboratory for Information Science and Technology (TNList), Department of Automation, Tsinghua University, Beijing 100084, China<br>E-mail: wangshengyao@tsinghua.org.cn


#### Abstract

In this paper, an effective estimation of distribution algorithm (EDA) is proposed to solve the hybrid flow-shop scheduling problem with stochastic processing time. Considering the effectiveness and robustness of a schedule, the schedule objective is to minimize the makespan of the initial scenario as well as the deviation of the makespan between all stochastic scenarios and the initial one. In the proposed EDA, a bi-objective evaluation function is employed to evaluate the individuals of the population. A probability model is presented to describe the probability distribution of the solution space. A mechanism is provided to update the probability model with the superior individuals. By sampling the probability model, new individuals can be generated among the search region with the promising solutions. Numerical testing results based on some well known benchmark instances are provided. The comparisons with the existing genetic algorithm demonstrate the effectiveness and robustness of the proposed EDA.


Key Words: Hybrid flow-shop scheduling problem, stochastic processing time, estimation of distribution algorithm, probability model, robust scheduling

## 1 Introduction

Flexible manufacturing system (FMS) is an automatic machinery manufacturing system which can adapt to the changes of processing objects. Production scheduling plays an important role in the FMS. Developing effective and efficient algorithms for scheduling problems is significant to improve the processing efficiency and the economic benefits. The hybrid flow-shop scheduling problem (HFSP) [1] is an extension of the classical flow-shop scheduling problem for the FMS. Many real industrial manufacturing problems can be modeled as the HFSP, like those in the fields of textile, paper, electronics and steelmaking industries [2-3]. Meanwhile, the HFSP with multiple stages and jobs is strongly NP-hard [4]. Therefore, it is of strong academic significance and engineering application value to study the HFSP in terms of theory and solution methodology.

Since the HFSP was proposed in 1954 [5], many approaches have been proposed. Roughly, they can be divided into three types: the exact methods, the heuristics and the meta-heuristics. The exact algorithms, such as branch and bound [6], can obtain the optimal solutions of a given problem, but they can only be used to solve the small-scaled problems due to the complexity of the problems. The heuristics, such as dispatching rules [7] and divide-and-conquer strategy [8], are relatively efficient. Nonetheless, the quality of the obtained solutions is often not satisfactory, especially for the large-scaled problems. With the development of computational intelligence, some meta-heuristics have been presented for solving the scheduling problem. These algorithms make it possible to achieve the satisfactory schedules for the large-scaled

[^0]problems with reasonable computational effort. Among meta-heuristics, genetic algorithm (GA) [9-10], particle swarm optimization [11], ant colony optimization [12], tabu search [13], differential evolution [14], and shuffled frog leaping algorithm [15] have already been applied to solve the HFSP.

In the literature, it is often assumed that the processing times are deterministic values. However, in practice, several sources of uncertainty have effect on the production, thus the processing times of the operations are not deterministic [16]. Consequently, it is more significant to study the HFSP with stochastic processing time, namely the stochastic HFSP (SHFSP). The SHFSP is much closer to the real applications. However, to the best of our knowledge, the only presented algorithm for solving the SHFSP is a GA developed recently [17]. In [17], it also defined a robust bi-objective evaluation function to obtain a robust and effective solution that is only slightly sensitive to data uncertainty. So, the study on the SHFSP is still in its infancy, and it is important to develop novel and effective algorithms for the problem.

As a kind of particular evolutionary algorithm based on statistical learning, estimation of distribution algorithm [18] has gained increasing research and applications in several fields during recent years, such as feature selection, cancer classification, multidimensional knapsack problem, quadratic assignment problem, machinery structure design, flexible job-shop scheduling, nurse rostering, resourceconstrained project scheduling, and so on [19-24]. As for the HFSP, in our previous work, an enhanced EDA with a hybrid decoding method was presented [25] and a compact EDA which employed only two individuals was introduced [26]. For the good performance of the EDA-based algorithms to the problems above, it is expected to solve the SHFSP efficiently by a well-designed EDA and to provide a new approach for solving the problem. Therefore, in this paper, we will propose an effective EDA to solve the SHFSP. To be specific, a probability model is presented to describe the probability distribution of the solution space and a


[^0]:    ${ }^{1}$ This work is supported by the National Key Basic Research and Development Program of China (2013CB329503), the National Science Foundation of China (61174189 and 61025018), the Doctoral Program Foundation of Institutions of Higher Education of China (20100002110014), and the National Science and Technology Major Project of China (No.2011ZX02504-008).

mechanism is provided to update the probability model with the superior individuals. By sampling the probability model, new individuals can be generated among the search region with promising solutions. Numerical tests based on some well known benchmark instances are carried out. The comparisons with the existing GA demonstrate the effectiveness and robustness of the proposed algorithm.

The remainder of the paper is organized as follows. The SHFSP is described in Section 2. In Section 3 the basic EDA is introduced, and the framework of the EDA for solving the SHFSP is proposed in Section 4. Simulation results and comparisons are provided in Section 5. Finally, we end the paper with some conclusions in Section 6.

## 2 Problem description

### 2.1 Nomenclature

$n$ : the number of jobs to be processed;
$s$ : the number of processing stages;
$m_{i}$ : the number of the machines at stage $k$;
$X_{j i k}$ : a binary variable which is equal to 1 if job $j$ is assigned to machine $i$ at stage $k$ and is equal to 0 otherwise;
$Y_{j i k}$ : a binary variable which is equal to 1 if job $i$ precedes job $j$ at stage $k$ and is equal to 0 otherwise;
$R_{i}$ : the releasing time of job $i$;
$S_{i k}$ : the starting time of job $i$ at stage $k$;
$P_{i k}$ : the processing time of job $i$ at stage $k$;
$C_{i k}$ : the completing time of job $i$;
$L$ : a very large constant;
$N$ : the number of stochastic scenarios;
$\zeta(I)$ : the $i^{\text {th }}$ set of the sampled parameters from the initial scenario $I$;
$P_{i}$ : the processing time of the initial scenario;
$\alpha \in[0,1]$ : the uncertainty degree of the processing times.

### 2.2 The HFSP

Generally, the HFSP consists of a set of $n$ jobs that are to be processed at $s$ stages, where each stage has at least one machine and some stages have multiple machines. Each job should be processed at all the stages, and each job can be processed by any one of machines at each stage.

Typically, the HFSP is supposed that [25-26]: all the $n$ jobs are independent and available to be processed at the initial time; the releasing time of all machines is not considered or set as 0 ; one machine can process only one operation and one job can be processed at only one machine at a time; once an operation is started, it cannot be interrupted; for all the $n$ jobs, the processing times on each machine are known in advance; buffers between stages are infinite; the time between different machines for transportation is negligible. In Fig. 1, it illustrates an example of HFSP.
![img-0.jpeg](img-0.jpeg)

Fig. 1 An example of HFSP

The HFSP can be formulated as follows [27]:

$$
\begin{aligned}
& \text { Minimize: } C_{\max } \\
& \text { Subject to: } \\
& \qquad C_{\max }=\max C_{i k}, k=1,2, \ldots, s ; i=1,2, \ldots, n \\
& \quad C_{i k}=S_{i k}+P_{i k} \\
& \quad \sum_{i=1}^{m_{k}} X_{j i k}=1 \\
& \quad S_{i k} \geq C_{i, k-1}, k=2,3, \ldots, s \\
& \quad S_{i k} \geq C_{j k}-L Y_{j i k} \text {, for all the pairs }(i, j) \\
& \quad S_{j k} \geq C_{i k}-(1-L) Y_{j i k} \text {, for all the pairs }(i, j) \\
& \quad S_{i 1} \geq R_{i}, i=1,2, \ldots, n
\end{aligned}
$$

As for the above formulation: formula (1) implies that the objective function is to minimize the makespan of the HFSP, i.e., the maximum completion time of all the jobs as shown in formula (2); formula (3) describes the computation of $C_{i k}$; formula (4) ensures that one job can be processed exactly on one machine at each stage; constraints (5) and (6) ensure that one machine can process only one job at one time; constraint (7) means that one job cannot be processed until its preceding job is finished; constraint (8) bounds the starting time of a job.

### 2.3 The Stochastic HFSP

In the SHFSP, the processing times are described as random variables. To evaluate a solution of the stochastic problem, a scenario modeling approach is often adopted to represent the characteristic of the uncertainty. It constructs a set of stochastic scenarios in which the processing times are sampled according to a certain probability distribution. Same as the literature [17], the uniform distribution is used in this paper.

The initial scenario $I$ is a deterministic scenario, which represents the characteristics of the problem. The set of the stochastic scenarios is represented by sampling the initial scenario $I$. To be specific, $\zeta(I)$ is supposed to be uniformly distributed between $\left[P_{I}-\alpha P_{I}, P_{I}+\alpha P_{I}\right]$. For a given solution, the average of the makespan calculated from all the scenarios is regarded as its makespan.

## 3 Estimation of Distribution Algorithm

EDA is a new paradigm in the field of evolutionary computation, which employs explicit probability distributions in optimization [18]. Compared with GA, EDA reproduces new population implicitly instead of the crossover and mutation. In EDA, a probability model of the most promising area is built by statistical information based on the searching experience, and then the probability model is used for sampling to generate the new individuals. Meanwhile, the probability model is updated in each generation with the potential individuals of the new population. In such an iterative way, the population evolves and finally satisfactory solutions can be obtained. The procedure of the basic EDA can be described as follows.

Step 1: Initialize the population;
Step 2: Select the superior sub-population;
Step 3: Estimate the probability distribution of the superior sub-population;

Step 4: Sample the probability model to generate the new population;

Step 5: If the stopping condition is met, the algorithm ends and outputs the best solution that is obtained in the searching procedure; else, go to step 2.

The critical step of EDA is to estimate the probability distribution. EDA uses the probability model to describe the distribution of the solution space, and the updating process reflects the evolutionary trend of the population. Due to the difference of problem types, a proper probability model and an updating mechanism should be well developed to estimate the underlying probability distribution.

## 4 EDA for the SHFSP

### 4.1 Evaluation Function

Considering the effectiveness and robustness of the schedule, to evaluate a solution $x$, an evaluation function [17] aggregating the two objectives is employed, which is expressed as follows:

$$
\begin{aligned}
& f(x)=\lambda \frac{C_{\max }^{I}(x)-\mathrm{LB}}{\mathrm{LB}}+(1-\lambda) \\
& \times \frac{\sqrt{\frac{1}{N} \sum_{i=1}^{N}\left[C_{\max }^{2,1}(I)(x)-C_{\max }^{I}(x)\right]^{2}}}{(D E V \_M A X\left(x^{*}\right)}}
\end{aligned}
$$

where $\lambda \in(0,1)$ represents the weight coefficient; LB is the lower bound of the initial scenario, $D E V \_M A X\left(x^{*}\right)$ $=\max \left\{\left(C_{\max }^{I}\left(x^{*}\right)-C_{\max }^{I_{\max }}\left(x^{*}\right)\right), \mid C_{\max }^{I_{\max }}\left(x^{*}\right)-C_{\max }^{I}\left(x^{*}\right)\right\} ;$ $x^{*}$ is the best solution; $C_{\max }^{I_{\max }}\left(x^{*}\right)$ is the makespan of the minimal processing time calculated from the initial scenario, i.e., $I_{\min }=I-\alpha I ; C_{\max }^{I_{\max }}\left(x^{*}\right)$ is the makespan of the maximal processing time calculated from the initial scenario, i.e., $I_{\max }=I+\alpha I$. The two values $C_{\max }^{I_{\max }}\left(x^{*}\right)$ and $C_{\max }^{I_{\max }}\left(x^{*}\right)$ are obtained by integrating the solution $x^{*}$ obtained for the initial scenario $I$ in the minimal and maximal scenarios.

It can be seen that, the schedule objective is to minimize the makespan of the initial scenario as well as the deviation of the makespan between all stochastic scenarios and the initial one. Note that LB and $D E V \_M A X\left(x^{*}\right)$ are used to normalize the two objectives since they do not have the same measurement scale.

### 4.2 Encoding and Decoding

Each individual of the population is a solution of the SHFSP, which is expressed by an integer number sequence with the length of $n$ and determines the processing order of the first stage. For example, a solution $x=\{5,2,3,1,4\}$ represents that job 5 is processed first at the first stage, and next are job 2 , job 3 , and job 1 in sequence. Job 4 is the last job to be processed.

To decode a sequence is to assign the jobs to the machines at each stage so as to form a feasible schedule and calculate the makespan. For the SHFSP, the decoding procedure is to decide the jobs order and the machines assignment. For the jobs order, the algorithm decides the processing order of the first stage referring to the sequence order given. From stage 2 on, the algorithm decides the processing order of the current stage according to the completion time of each job from the previous stage in a non-decreasing order. As for the machines assignment, the first available machine rule [28] is
employed. That is, the job is assigned to the machine with the earliest release time.

For a given solution $x$, the makespan values of the initial scenario and stochastic scenarios are obtained with the decoding method and the target value $f(x)$ is calculated as introduced in section 4.1.

### 4.3 Probability Model and Updating Mechanism

The EDA produces new population by sampling a probability model. In this paper, the probability model is designed as a probability matrix $P$.

The element $p_{i j}(l)$ of the probability matrix $P$ represents the probability that job $j$ appears before or in position $i$ of the solution sequence at generation $l$. The value of $p_{i j}$ refers to the importance of a job when deciding the jobs order. For all $i$ and $j, p_{i j}$ is initialized to $p_{i 0}(0)=1 / n$, which ensures that the whole solution space can be sampled uniformly.

In each generation of the EDA, the new individuals are generated via sampling according to the probability matrix $P$. For every position $i$, job $j$ is selected with the probability $p_{i j}$. If job $j$ has already appeared, the whole $j^{\text {th }}$ column of probability matrix $P$ will be set as zero and all the elements of $P$ will be normalized to maintain that each row sums up to 1. An individual is constructed until all the jobs appear in the sequence. In such a way, Psize individuals are generated.

Next, it determines the superior sub-population with the best SPsize solution. And then, the probability matrix $P$ is updated according to the following equation:

$$
p_{i j}(l+1)=(1-\beta) p_{i j}(l)+\frac{\beta}{i \times \text { SPsize }} \sum_{k=1}^{S P S i z e} P_{i j}^{k}, \forall i, j
$$

where $\beta \in(0,1)$ is the learning rate of $P$, and $I_{i j}^{k}$ is the following indicator function of the $k^{\text {th }}$ individual in the superior sub-population.

$$
I_{i j}^{k}=\left\{\begin{array}{l}
1, \text { if job } j \text { appears before or in position } i \\
0, \text { else }
\end{array}\right.
$$

The above updating process can be regarded as a kind of increased learning, where the second term on the right hand side of formula (10) represents learning information from the superior sub-population.

### 4.4 Procedure of the EDA for SHFSP

With the design above, the procedure of EDA for solving the SHFSP is illustrated in Fig. 2.

In the above EDA, it stops when the maximum number of generations Gen is satisfied.

### 4.5 Computation Complexity Analysis

For each generation of the EDA, its computational complexity can be roughly analyzed as follow.

For the sampling process, every position is generated with the roulette strategy by sampling the probability matrix $P$. A sequence is constructed with the complexity $O\left(n^{2}\right)$ and Psize individuals can be generated with the complexity $O\left(n^{2} P s i z e\right)$.

For the updating process, first it is with the computational complexity $O($ PsizelogPsize $)$ by using the quick sorting method to select the best SPsize individuals from population; then, it is with the complexity $O[n(S P s i z e+n)]$ to update all the $n \times n$ elements of $P$. Thus, the computational complexity for updating process is $O[n(S P s i z e+n)+P s i z e \log P s i z e]$.

It can be seen that the complexity of the proposed EDA is not large and the algorithm could be efficient for solving the considered problem.
![img-1.jpeg](img-1.jpeg)

Fig. 2 The procedure of EDA for SHFSP

## 5 Simulation and Comparison

To test the performance of the EDA, numerical tests are carried out based on some benchmarks used in [17]. Table 1 presents the configurations and the LB values of these benchmarks. The algorithm is coded in C and run on Thinkpad T420 with a 2.3 GHz processor and 2 GB RAM.

Table 1: Configurations and LB values
To compare the proposed EDA to the GA [17], the best solution obtained by the algorithm is evaluated using extra 100 times to confirm the accuracy as the literature [17]. The parameters of the EDA are set as follows: Psize $=50$, SPsize $=10, N=20, \beta=0.1$, and Gen $=100$. Furthermore, the evaluation time of the EDA is $10^{5}$ and it is no less than $2 \times 10^{6}$ of the GA [17].

Tables 2-4 provide the detailed results for the benchmarks with the uncertainty degree equals to $10 \%, 25 \%$ and $50 \%$, respectively. The column " $C_{\text {max }}$ " presents the best makespan value of the initial scenario. The column "STD" presents the deviation of the makespan between all
stochastic scenarios and the initial one, which is calculated as follows:

$$
S T D=\sqrt{\frac{1}{100} \sum_{i=1}^{100}\left(C_{\max }^{\xi, 11 i}-C_{\max }^{\prime}\right)^{2}}
$$

The column " $A V G$ " presents the average makespan value of 100 stochastic scenarios. The column " $D E V$ " (in \%) presents the deviation between $A V G$ and $C_{\text {max }}$, which is calculated as follows:

$$
D E V=\frac{A V G-C_{\max }^{I}}{C_{\max }^{I}} \times 100
$$

Furthermore, Tables 5-6 provide the summarized results of $C_{\text {max }}$ and STD for all the benchmarks with different degrees of uncertainty.

Table 2: Experimental results for $\alpha=10 \%$

From Tables 2-6, it can be seen that the EDA performs better than the GA in solving the SHFSP. The $C_{\text {max }}$ values and the $A V G$ values by the EDA are smaller than or equal to that by the GA for all the instances, which means that the EDA is more effective when solving the initial scenario and the stochastic scenarios. In addition, the STD values by the EDA are also smaller than that by the GA for all the instances, which means that the EDA is more robust to the

data uncertainty. Therefore, it can be concluded that the EDA is more effective and more robust than the GA for solving the SHFSP.

According to Tables 5-6, when the value of $\lambda$ decreases, the values of $C_{\text {max }}$ increase and the values of STD decrease. It is because the algorithm only minimizes the $C_{\text {max }}$ when $\lambda=1$ while it only minimizes the STD when $\lambda=0$. For $\lambda=0.5$, it makes a trade off between the two objectives.

Table 3: Experimental results for $\alpha=25 \%$

## 6 Conclusion

In this paper, an estimation of distribution algorithm was proposed for solving the hybrid flow-shop scheduling problem with stochastic processing time. In the proposed EDA, a bi-objective evaluation function was employed to evaluate the individuals of the population. A probability model was presented to describe the probability distribution of the solution space and mechanism was provided to update the probability model with the superior individuals. By sampling the probability model, new individuals were generated among the search region with the promising solutions. The effectiveness and robustness were demonstrated by numerical testing results and the comparison to the existing GA. The future work is to design
effective EDA-based algorithms for other kinds of shop scheduling problems with the fuzzy or interval processing times.

Table 4: Experimental results for $\alpha=50 \%$

Table 5: The average $C_{\text {max }}$ for all the benchmarks

Table 6: The average STD for all the benchmarks
