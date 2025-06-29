# Minimizing makespan in a no-wait flowshop with two batch processing machines using estimation of distribution algorithm 

Shengchao Zhou ${ }^{\mathrm{a} *}$, Xueping $\mathrm{Li}^{\mathrm{b}}$, Huaping Chen ${ }^{\mathrm{c}}$ and Cong Guo ${ }^{\mathrm{b}}$<br>${ }^{a}$ School of Management, University of Science and Technology of China, Hefei, China; ${ }^{\mathrm{b}}$ Department of Industrial and Systems Engineering, University of Tennessee, Knoxville, USA; ${ }^{\mathrm{c}}$ School of Computer Science and Technology, University of Science and Technology of China, Hefei, China

(Received 24 September 2015; accepted 5 January 2016)


#### Abstract

This paper studies the problem of minimising makespan in a no-wait flowshop with two batch processing machines (comprised of a parallel batch processing machine and a serial batch processing machine), non-identical job sizes and unequal ready times. We propose a population-based evolutionary method named estimation of distribution algorithm (EDA). Firstly, the individuals in the population are coded into job sequences. Then, a probabilistic model is built to generate new population and an incremental learning method is developed to update the probabilistic model. Thirdly, the best-fit heuristic is used to group jobs into batches and a least idle/waiting time approach is proposed to sequence the batches on batch processing machines. In addition, some problem-dependent local search heuristics are incorporated into the EDA to further improve the searching quality. Computational simulation and comparisons with some existing algorithms demonstrate the effectiveness and robustness of the proposed algorithm. Furthermore, the effectiveness of embedding the local search method in the EDA is also evaluated.


Keywords: scheduling; no-wait flowshop; batch processing machines; makespan; estimation of distribution algorithm (EDA)

## 1. Introduction

Batch processing machines (BPMs) can process a number of jobs in the form of a batch. BPMs have wide applications in many industrial environments such as electronics manufacturing facilities (Lee, Uzsoy, and Martin-Vega 1992; Zhou et al. 2013; Jia, Jiang, and Li 2015), tire production plants (Oulamara, Finke, and Kamgaing Kuiteing 2009), casting industry (Mathirajan and Sivakumar 2006) and metal working industry (Tang and Liu 2009a; Gong, Tang, and Duin 2010; Tang et al. 2014). BPMs can be classified into serial and parallel batching machines. A serial batching (i.e. s-batch) machine processes the jobs in a batch serially (Cheng and Wang 1998; Glass, Potts, and Strusevich 2001). A parallel batching (i.e. p-batch) machine can simultaneously process several jobs (Ahmadi et al. 1992; Rossi, Pandolfi, and Lanzetta 2014; Li, Ishii, and Chen 2015). There are basically two types of BPM scheduling problems: problems with fixed or varying batch processing times. In fixed batch processing time problems (Sung, Kim, and Yoon 2000; Lin and Liao 2013), the processing time of a batch is independent of the jobs belonging to the batch as a constant. In varying batch processing time problems (Potts, Strusevich, and Tautenhahn 2001; Behnamian et al. 2012; Abedi et al. 2015), however, the processing time of a batch is dependent on the jobs in the batch. For example, the processing time of a batch can be equal to the sum of the processing times of all jobs belonging to the batch or the longest processing time of all jobs in the batch.

This paper considers the two-machine flowshop scheduling problem with BPMs, a no-wait constraint, non-identical job sizes and unequal ready times. The first BPM is a parallel BPM and the second BPM is a serial BPM. Batches of jobs cannot wait between the two machines. Hence, a batch that completes processing on the first machine has to remain on that machine if the second machine is busy processing another batch. A constant set-up time is considered on the second machine before each batch is processed on it. Additionally, we assume that jobs arrive dynamically at the first machine. The objective is to group the jobs into batches and schedule the batches such that the makespan (i.e. the completion time of the last batch leaving the flowshop) is minimised. A smaller makespan usually implies a higher utilisation of the production system.

This problem under study is motivated by problems arise in industrial operations. For example, for a cleaning test operation observed at a sensor manufacturing facility, the substrates (or jobs) need to be cleaned to remove any residuals. The cleaning test takes place in two baths (or processing machines). Multiple substrates with different sizes can be cleaned at one time in the first bath as long as the total size of all the substrates in a batch does not exceed the bath capacity. The time taken here depends on the composition of the batch. In general, the cleaning time is equal to the longest cleaning time among

[^0]
[^0]:    *Corresponding author. Email: zhousc@mail.ustc.edu.cn

all the substrates in the batch. This cleaning time of each substrate can be estimated a prior. The second bath can also test several substrates at a time but here the substrates are handled sequentially. Consequently, the time taken to wash in this bath is equal to the sum of the cleaning times of all substrates in the batch. One of the considerations in scheduling the batches is that each batch should be continuously processed from the start to the end (i.e. no-wait constraint). For more details of this process, please refer to Muthuswamy et al. (2012).

The rest of this paper is organised as follows. Section 2 presents the literature review of two-stage flowshop scheduling problems with BPMs and some applications of estimation of distribution algorithms (EDA) in the literature. Problem definition is given in Section 3. In Section 4, the EDA for our problem is proposed in detail. Section 5 presents the EDA with local search. Computational results and comparisons are provided in Section 6. Some concluding remarks are summarised in Section 7.

# 2. Literature review 

### 2.1 Two-stage flowshops with BPMs

Problems related to scheduling in a flowshop with BPMs have received considerable attention in recent years. Ahmadi et al. (1992) considered the problem of scheduling a two-stage flowshop in which one or both of the stages may comprise a BPM. The processing time of a batch is a constant regardless of the number of jobs contained in it. They studied the complexity analysis for two problem instances with the objective of makespan and total completion time. Cheng and Wang (1998) considered a class of batching and scheduling problems in the two-machine flowshop where one machine is a discrete processor and the other one is a BPM. The batch processing time is equal to the total processing time of the jobs contained in that batch. A constant set-up time is incurred whenever a batch is formed on the BPM. All problems were shown to be NP-complete in the ordinary sense. Cheng, Lin, and Toker (2000) considered the two-machine flowshop where both machines process jobs in batches. They proved the strong NP-hardness of the problem, presented properties and polynomial algorithms for some special cases, and proposed heuristic algorithms to deal with the general problem.

Sung and Min (2001) considered the problem of scheduling one or two BPMs in a flowshop environment. The processing times of batches are independent of the composition of the batch and identical. The objective is to minimise the earliness/tardiness (E/T) measure. Sung and Kim (2002) extended the two-machine flowshop of Ahmadi et al. (1992) to the situation in which the jobs arrive dynamically at the first machine. The problem was proven as strongly NP-hard and an efficient heuristic was presented. Sung and Kim (2003) analysed a two-machine flowshop comprising BPMs with respect to three due date-related problems. The BPMs can process jobs simultaneously as long as the number of jobs in the batch is less than a predetermined number.

Su (2003) examined a two-stage flowshop scheduling problem with limited waiting time constraints. There is a BPM in the first stage and a discrete machine in the second stage. A mixed integer programming formulation and a heuristic were developed to solve the problem. Glass, Potts, and Strusevich (2001) studied a problem of batching and scheduling on two BPMs in a flowshop environment. The processing time of a batch is the sum of the processing times of the jobs in that batch. They did not consider any restrictions on the number of jobs that can be assigned to a batch. An integer programming formulation and a heuristic were developed to minimise the makespan.

Lin and Cheng (2001) investigated flowshops with two serial BPMs and a no-wait constraint. A constant set-up time is considered before a batch is processed on each machine. They showed that the problem of minimising the completion time is strongly NP-hard. Lin and Cheng (2005) examined a two-machine flowshop scheduling problem where a discrete machine is followed by a BPM. The jobs have identical sizes and no restrictions are imposed on the number of jobs that can be assigned to a batch. The processing time of a batch is equal to a constant set-up time plus the sum of the processing times of all the jobs in that batch. They showed that the problem is strongly NP-hard and designed some heuristics for deriving approximate solutions.

Oulamara, Kovalyov, and Finke (2005) studied a no-wait flowshop problem with two parallel BPMs and proposed a polynomial algorithm for the problem. Oulamara, Finke, and Kamgaing Kuiteing (2009) investigated a flowshop scheduling problem with a BPM and job compatibilities. They showed that minimising the makespan is NP-hard in the ordinary sense and presented three heuristics to minimise the makespan. Tang and Liu (2009b) studied the two-machine flowshop scheduling problem with batching and release times, in which the objective is to minimise the makespan. They formulated the problem as a mixed integer programming model and showed that it is strongly NP-hard. A dynamic programming-based heuristic was developed. Gong, Tang, and Duin (2010) considered a two-stage flowshop scheduling problem on a BPM and a discrete machine with blocking and shared set-up times. For the objective of minimising the makespan, they proved that the problem is strongly NP-hard.

All of the research works mentioned above assume that the jobs have identical sizes and the capacity of a BPM can be defined by the number of jobs in a batch or is unbounded. Moreover, these works only consider one type of BPMs, either

Table 1. The literature related to two-stage flowshop scheduling problems with $\operatorname{BPM}(\mathrm{s})$.
Note: 'I' represents identical; 'N' represents non-identical.
s-batch or p-batch machines, but not both. Considering jobs with non-identical sizes, Damodaran and Srihari (2004) presented two mixed integer formulations for scheduling two BPMs in a flowshop scenario when the intermediate buffer is infinite or zero. The processing time of a batch is the longest processing time among all the jobs in that batch on both machines. Liao and Liao (2008) and Kashan and Karimi (2009) investigated the same problem as Damodaran and Srihari (2004) and improved the models proposed by Damodaran and Srihari (2004). Mirsanei, Karimi, and Jolai (2009) and Manjeshwar, Damodaran, and Srihari (2009) developed two simulated annealing (SA) algorithms to minimise makespan in a two-machine flowshop with infinite buffer, respectively. Liao and Huang (2011) proposed a Tabu search heuristic and Manjeshwar, Damodaran, and Srihari (2011) proposed a genetic algorithm (GA) for the same case. Cheng et al. (2014) designed a polynomial time algorithm under the assumption that the processing time of a job on the first machine has a positive correlation with its processing time on the second machine.

This paper differs from the above research in that we consider the flowshop scheduling problem with a parallel BPM and a serial BPM instead of two parallel BPMs. Oulamara (2007) and Jolai et al. (2009) investigated the flowshop scheduling problem with both parallel and serial BPMs. However, they did not include unequal ready times and non-identical job sizes in their models. To the best of our knowledge, only Muthuswamy et al. (2012) examined a similar problem. In this work, the authors proposed a mathematical formulation and a particle swarm optimisation (PSO) algorithm.

The literature related to two-stage flowshop scheduling problems with BPM(s) is shown in Table 1.

# 2.2 Estimation of distribution algorithm 

The EDA is a relatively new population-based evolutionary algorithm introduced by Muhlenbein and Paass (1996). Unlike other evolutionary algorithms, the EDA generates new solutions by sampling from a probabilistic model which characterises the solution space. According to different problem types, the EDA may employ different probabilistic models, including univariate, bivariate and multivariate probabilistic models. The univariate probabilistic models assume that there is no

![img-0.jpeg](img-0.jpeg)

Figure 1. The general framework of the EDA.
interaction between/among variables such as the compact GA (Harik, Lobo, and Goldberg 1999), the self-guided GA (Chen, Chang et al. 2012), and the EDA (Wang et al. 2013). The bivariate probabilistic models consider pairwise variable interactions such as the mutual-information-maximising input clustering (De Bonet, Isbell, and Viola 1997), the combining optimisers with mutual information trees (Baluja and Davies 1997), the bivariate marginal distribution algorithm (Pelikan and Mühlenbein 1999) and the extended artificial chromosomes GA (Chen, Chen et al. 2012). Whereas the multivariate probabilistic models consider multivariate interactions such as the factorised distribution algorithms (Muhlenbein and Mahnig 1999), the extended compact GA (Harik 1999) and the Bayesian optimisation algorithm (Pelikan 2005).

The EDA is being widely used to solve various kinds of combinatorial optimisation problems such as permutation flowshop scheduling (Chang et al. 2009; Zhang and Li 2011; Pan and Ruiz 2012), nurse rostering (Aickelin, Burke, and Li 2006), software testing (Sagarna and Lozano 2005), single machine scheduling (Chang et al. 2010), jobshop scheduling (Wang et al. 2012; Liu, Fan, and Liu 2015) among many other applications. For a complete review of the EDA, please refer to Larrañaga and Lozano (2002), Pelikan, Goldberg, and Lobo (2002) and Lozano et al. (2006).

The EDA provides a new tool of stochastic optimisation methods (Wang et al. 2012). Different from the genetic algorithm which explicitly generates new offspring using crossover and mutation operators, the EDA generates new offspring implicitly. Firstly, the EDA builds a probabilistic model based on the statistical information extracted from previous searches. Then, the EDA samples from the probabilistic model and generates new solutions. Accordingly, the statistical information, as well as the probabilistic model, is updated using some of the new solutions. The general framework of the EDA is described in Figure 1.

# 3. Problem definition 

In this section, the problem under consideration is formulated as a mixed integer programming model. The parameters and variables used are given as follows.

Parameters:
$J \quad$ The set of all jobs, $J=\{1,2, \ldots, n\}$, where $n$ is the total number of jobs.
$M \quad$ The set of machines, $M=\{1,2\}$.
$s_{j} \quad$ The size of job $j$.

$p_{j m} \quad$ The processing time of job $j$ on machine $m$.
$r_{j} \quad$ The ready time of job $j$.
$S$ The capacity of the first machine.
$T$ The set-up time on the second machine.
Decision variables:

- $X_{j b} \quad 1$, if job $j$ belongs to the $b$ th batch; 0 , otherwise.
- $Y_{b} \quad 1$, if the $b$ th batch is not empty; 0 , otherwise.
- $P_{b m} \quad$ The processing time of the $b$ th batch on machine $m$.
- $R_{b} \quad$ The ready time of the $b$ th batch.
- $U_{b 1} \quad$ The starting time of the $b$ th batch processed on the first machine.
- $D_{b 1} \quad$ The departure time of the $b$ th batch processed on the first machine.
- $C_{b 2} \quad$ The completion time of the $b$ th batch processed on the second machine.
- $C_{\max } \quad$ The makespan.

The problem considered in this research can be formally stated as follows.
(1) There are $n$ jobs to be processed in a two-machine flowshop with BPMs. The jobs arrive dynamically at the first machine and the ready time of job $j$ is denoted by $r_{j}$. Each job has a size $s_{j}$ and the processing time of job $j$ on machine $m$ is denoted by $p_{j m}$.
(2) The first machine has a capacity $S$ and can process a batch of jobs as long as the total size of all the jobs in the batch does not exceed the capacity. The batch is ready for processing only after all the jobs in the batch are ready. The processing time of batch $b$ on the first machine is equal to the longest processing time of the jobs in the batch. The processing time of batch $b$ on the second machine is equal to the sum of processing times of the jobs in the batch. A constant set-up time $T$ is considered on the second machine before each batch is processed on it. The sequence in which the batches are to be processed is the same for each machine.
(3) Batch $b$ cannot wait between the two machines, though it is completely processed on the first machine. In other words, the batch must stay an extra time on the first machine if the second machine is not free.
(4) The objective is to minimise the makespan $C_{\max }$.

This problem can be denoted as $F_{2} \mid p-\operatorname{batch}(1), s-\operatorname{batch}(2)$, no-wait, $s_{j}, r_{j} \mid C_{\max }$ according to the three-field notation (Graham et al. 1979). The mixed integer programming model for the problem is formulated as follows. A similar formulation can be found in Muthuswamy et al. (2012).

$$
\text { Minimize } \quad C_{\max }
$$

Subject to :

$$
\begin{gathered}
\sum_{b=1}^{n} X_{j b}=1, \quad j=1, \ldots, n \\
\sum_{j=1}^{n} s_{j} X_{j b} \leq S, \quad b=1, \ldots, n \\
P_{b 1} \geq p_{j 1} X_{j b}, \quad j=1, \ldots, n ; b=1, \ldots, n \\
P_{b 2} \geq \sum_{j=1}^{n} p_{j 2} X_{j b}, \quad b=1, \ldots, n \\
U_{b 1} \geq r_{j} X_{j b}, \quad j=1, \ldots, n ; b=1, \ldots, n \\
U_{b 1} \geq D_{b-1,1}, \quad b=2, \ldots, n \\
D_{b 1} \geq U_{b 1}+P_{b 1}, \quad b=1, \ldots, n \\
D_{b 1} \geq C_{b-1,2}, \quad b=2, \ldots, n \\
Y_{b} \geq X_{j b}, \quad j=1, \ldots, n ; b=1, \ldots, n \\
C_{b 2} \geq D_{b 1}+T \times Y_{b}+P_{b 2}, \quad b=1, \ldots, n \\
C_{\max } \geq C_{b 2}, \quad b=1, \ldots, n \\
X_{j b} \in\{0,1\}, \quad j=1, \ldots, n ; b=1, \ldots, n \\
Y_{b} \in\{0,1\}, \quad b=1, \ldots, n
\end{gathered}
$$

Table 2. Illustration of the job sequence based representation.

$$
U_{b 1}, D_{b 1}, C_{b 2} \geq 0, \quad b=1, \ldots, n
$$

The objective (1) minimises the makespan. Constraint (2) ensures that each job is assigned to exactly one batch. Constraint (3) requires that the total size of all the jobs in a batch does not exceed the machine capacity. Constraint (4) ensures that the processing time of the $b$ th batch on machine 1 is at least equal to the longest processing time of all the jobs in the batch. Constraint (5) determines the processing time on machine 2 for batch $b$. Constraint (6) indicates that the $b$ th batch is processed on machine 1 only after all the jobs in the batch have arrived. Constraint (7) ensures that the starting time of the $b$ th batch on machine 1 is at least the departure time of the $(b-1)$ th batch on machine 1 . Constraint (8) ensures that the departure time of the $b$ th batch on machine 1 is at least equal to its starting time on machine 1 plus its processing time on machine 1. Constraint (9) guarantees that a batch cannot leave from machine 1 until the previous batch completes its processing on machine 2. Constraint (10) relates the $Y_{b}$ and $X_{j b}$ variables. $Y_{b}$ is equal to 1 as long as the $b$ th batch contains at least one job. Constraint (11) decides the completion time of each batch on machine 2. Constraint (12) determines the makespan. Finally, constraints (13)-(15) define the range of the variables.

# 4. The proposed EDA algorithm 

In this section, we will present an EDA for the two-machine no-wait flowshop with BPMs, non-identical job sizes and unequal ready times. The solution representation and initial population, probabilistic model and updating mechanism, and batching and sequencing decisions are explained as follows.

### 4.1 Solution representation and initial population

The job sequence-based representation is widely used in the literature for two-stage flowshop scheduling problems (Muthuswamy et al. 2012; Chen et al. 2014). Therefore, it is also adopted in our EDA. In this representation, the $i$ th number of the sequence denotes the job placed at position $i$. A numerical example is illustrated in Table 2.

In order to guarantee the initial population with a certain quality and diversity, we construct the initial population in two ways. Firstly, some prior rules, including Johnson's rule, the longest processing time (LPT) rule, the shortest processing time (SPT) rule and the first in first out (FIFO) rule, are employed to generate initial individuals. Johnson's rule is one of the well-known heuristics in the literature and it provides an optimal solution for makespan minimisation in a two-stage flowshop with discrete machines. The LPT rule sequences the jobs in descending order of the sum of their processing times on both the machines and the SPT rule sequences the jobs in ascending order of the sum of their processing times on the machines. The FIFO rule is applied to the jobs based on their ready times. Secondly, the rest of the individuals in the initial population is generated randomly. Finally, a population with $Q$ individuals is created.

### 4.2 Probabilistic model and updating mechanism

As mentioned previously, the EDA generates new population by sampling from a probabilistic model which directly impacts the performance of the algorithm. Thus, the construction of the probabilistic model is a crucial step for excellently designing the EDA. In our algorithm, a probabilistic matrix is built to determine the estimation of distribution model as follows:

$$
P(t)=\left(\begin{array}{ccc}
p_{11}(t) & \ldots & p_{1 n}(t) \\
\vdots & \ddots & \vdots \\
p_{n 1}(t) & \ldots & p_{n n}(t)
\end{array}\right)
$$

where $p_{j k}(t)$ denotes the probability of job $j$ to be placed at position $k$ at generation $t$. At the beginning of the algorithm, each $p_{j k}(0)$ is initialised to be $1 / n$. This initialisation means that all solutions can be sampled uniformly.

![img-1.jpeg](img-1.jpeg)

Figure 2. Extracting statistical information and building a probabilistic matrix.

Table 3. The probability and accumulated probability of each job at position 1.


Figure 3. The probabilistic matrix after assigning job 2 at position 1.

According to the probabilistic matrix, new individuals are generated by sampling at generation $t$. For each new individual, position $k$ (from 1 to $n$ ) is assigned job $j$ by proportional selection based on probability $p_{j k}(t)$. If a job is assigned to a certain position, the data in the probabilistic matrix for that job and that position would be set to zero. In such a way, a number of $Q$ individuals are generated.

In order to illustrate how the new individual generation procedure works, a four-job instance is used. Suppose there are eight individuals which are selected to build the probabilistic matrix, as shown in the left-hand side of Figure 2. Then, we construct the probabilistic matrix $P$ as shown in the right-hand side of Figure 2. To generate an individual, jobs are assigned to each position by proportional selection based on the probability of each job at this position. Taking position 1 as an example, the probability and accumulated probability of each job at the position is given in Table 3. Suppose job 2 is chosen to be assigned at position 1, and then the probabilistic matrix is updated as shown in Figure 3. Following the same procedure, all positions will be assigned a job and a new individual is generated.

After the new population is generated, the fitness of these individuals is evaluated and the best $Q_{1}$ individuals are chosen to update the probabilistic matrix, where $Q_{1}=\alpha \times Q, 0<\alpha<1$. The probabilistic matrix is updated by the following equation:

$$
p_{j k}(t+1)=(1-\beta) p_{j k}(t)+\frac{\beta}{Q_{1}} \sum_{l=1}^{Q_{1}} Z_{j k}^{l}, \quad j, k=1, \ldots, n
$$

where $\beta \in(0,1)$ is the learning rate and $Z_{j k}^{l}$ is a binary variable in the $l$ th individual which is defined by Equation (18). As can be seen in Equation (17), we consider both of historical knowledge $p_{j k}(t)$ and current knowledge $1 / Q_{1} \sum_{i=1}^{Q_{1}} Z_{j k}^{i}$ which is learnt from the superior individuals. The relative importance of the two kinds of knowledge is determined by rate $\beta$. This updating method is an incremental learning one as suggested in Baluja and Davies (1998).

$$
Z_{j k}^{l}= \begin{cases}1 & \text { if job } j \text { is assigned to position } k \\ 0 & \text { otherwise }\end{cases}
$$

![img-2.jpeg](img-2.jpeg)

Figure 4. Illustration of the LIWT heuristic.

# 4.3 Batching decision 

The best-fit (BF) heuristic is one of the well-known methods for the bin packing problem (Bramel and Simchi-Levi 1998). It has been applied to group jobs into batches for machine scheduling problems (Ghazvini and Dupont 1998; Damodaran, Kumar Manjeshwar, and Srihari 2006; Chen, Du, and Huang 2010). In our EDA, we also employ the BF heuristic to form batches. The BF adapted to this scheduling problem is as follows:

Step 1 Sequence the jobs randomly.
Step 2 Select the job at the head of the list and assign it to the batch with the least remaining capacity. If the job does not fit in any existing batches, create a new batch. Repeat step 2 until all the jobs have been assigned to a batch.

### 4.4 Sequencing decision

In order to sequence the formed batches processed on the BPMs, a method, which we refer to as the least idle/waiting time (LIWT) heuristic, is developed based on the scheduling heuristic of Muthuswamy et al. (2012). Firstly, we define the idle/waiting time of the $b$ th batch on machine $m$ by $\theta_{b m}$ and the total idle/waiting time of the $b$ th batch on both the machines by $\theta_{b}$. Then $\theta_{b m}$ and $\theta_{b}$ can be determined by the following equations:

$$
\begin{aligned}
& \left\{\begin{array}{l}
D_{b+1,1}=\max \left\{\max \left\{R_{b+1}, D_{b 1}\right\}+P_{b+1,1}, C_{b 2}\right\} \\
\theta_{b+1,1}=D_{b+1,1}-\left(D_{b 1}+P_{b+1,1}\right)
\end{array}\right. \\
& \left\{\begin{array}{l}
C_{b+1,2}=D_{b+1,1}+T+P_{b+1,2} \\
\theta_{b+1,2}=C_{b+1,2}-\left(C_{b 2}+T+P_{b+1,2}\right) \\
\theta_{b+1}=\theta_{b+1,1}+\theta_{b+1,2}
\end{array}\right.
\end{aligned}
$$

The LIWT heuristic is described as follows:
Step 1 Arrange the batch with the least sum of the batch ready time and the batch processing time on machine 1 (i.e. $R_{b}+P_{b 1}$ ) as the first batch.
Step 2 Calculate the total idle/waiting times $\theta_{b+1}$ of all the unscheduled batches on both the machines by Equations (19)(21), and schedule the batch with the least idle/waiting time as the next batch. Repeat this step until all the batches have been scheduled on the machines.

An example of 4 batches is used to illustrate the LIWT heuristic. The ready times and processing times of the batches, the set-up time and their schedule are given in Figure 4. The shadow areas in the figure show the idle/waiting time.

## 5. The EDA with local search

### 5.1 Local search heuristics

The EDA makes effective use of global statistic information rather than local information about individual solutions during the evolution process. An efficient EDA should find an appropriate balance between global statistic information and local information. Hence in this paper, some problem-dependent local search heuristics are proposed and incorporated into the EDA in order to further improve the solution quality. The local search is designed for the batch sequencing phrase and applied to the best solution at each generation. Two types of neighbourhood structures are considered, namely insert-based local

search and swap-based local search. For a given sequence of batches, it tries to reduce the makespan through inserting a batch into another position or exchanging two batches at different positions. The pseudo code of the local search is described in Algorithm 1 (insert-based local search) and Algorithm 2 (swap-based local search).

```
Algorithm 1. The insert-based local search.
1: Let \(\lambda\) denote a given batch sequence, where \(\lambda=\left\{b^{1}, b^{2}, \ldots, b^{l}\right\}\) and \(l\) is the number of the batches, each of which contains
    at least one job;
    Set \(k=0\) and \(g=0\);
    while \(g<l\) do
        Set \(\lambda_{\text {best }}=\) null and \(C_{\max }\left(\lambda_{\text {best }}\right)=+\infty\);
        Set \(k=k \% l+1\) and \(k^{\prime}=k ; / / \%\) denotes the modulus operator.
        while true do
            Remove the \(k\) th batch \(\left(b^{k}\right)\) from \(\lambda\). Insert \(b^{k}\) into the \((k \% l+1)\) th position of \(\lambda\), resulting in a new schedule \(\lambda^{\prime}\);
            Set \(k=k \% l+1\);
            if \(k=k^{\prime}\) then
            break;
        end if
        if \(C_{\max }\left(\lambda^{\prime}\right)<C_{\max }\left(\lambda_{\text {best }}\right)\) then
            Update \(\lambda_{\text {best }}=\lambda^{\prime}\);
        end if
        end while
        if \(C_{\max }\left(\lambda_{\text {best }}\right)<C_{\max }(\lambda)\) then
            Update \(g=0\) and \(\lambda=\lambda_{\text {best }}\);
        else
        Set \(g=g+1\);
        end if
    end while
```


# 5.2 Framework of the EDA with local search 

Based on the above sections, the general framework of the EDA with local search (EDA $_{l s}$ for short) is summarised in Algorithm 3.

## 6. Computational experiments

### 6.1 Experimental design

To evaluate the proposed algorithm, problem instances were randomly generated in a way like Muthuswamy et al. (2012). Five factors that have effect on instances were identified: the number of jobs, the variation in job sizes, the variation in job processing times, the variation in job ready times and the set-up time on the second machine.

Random instances with 20, 50, 100, 200 and 300 jobs were generated. The job sizes $s_{j}$ were generated from a discrete uniform distribution $[1,10]$ and $[1,20]$. The job processing times $p_{j 1}$ and $p_{j 2}$ were generated from discrete uniform distributions $[1,50]$ and $[1,10]$, respectively. The job ready times $r_{j}$ were generated from a uniform distribution [0, $R \sum_{j=1}^{n} p_{j 1}$ ], where the factor $R$ determines the relative frequency of job arrivals. Two set-up times $T$ on the second machine were considered, 5 and 10 . The capacity of the first machine $S$ was assumed to be 20 for all instances. For each combination of factors and levels, 5 problem instances were randomly generated, thus, resulting in 200 instances. The experimental design is summarised in Table 4. Each category of problems is represented with a run code. For example, a problem category with 50 jobs, $T=10$, job sizes generated from $[1,10]$ and $R=0.1$ is denoted by n2T2s1R1.

Algorithm 2. The swap-based local search.

```
1: Let \(\lambda\) denote a given batch sequence, where \(\lambda=\left\{b^{1}, b^{2}, \ldots, b^{l}\right\}\) and \(l\) is the number of the batches, each of which contains
    at least one job;
2: Set \(a=0\) and sum \(=l\);
3: while sum \(>1\) do
4: \(\quad\) Set \(\lambda_{\text {best }}=\) null and \(C_{\max }\left(\lambda_{\text {best }}\right)=+\infty\);
5: Set \(a=a \% l+1\), sum \(=\operatorname{sum}-1\) and times \(=0\);
6: while times \(<\operatorname{sum}\) do
7: Set \(b=(a+\) times \() \% l+1\);
8: Exchange the \(a\) th batch and the \(b\) th batch in \(\lambda\), resulting in a new schedule \(\lambda^{\prime}\);
9: \(\quad\) if \(C_{\max }\left(\lambda^{\prime}\right)<C_{\max }\left(\lambda_{\text {best }}\right)\) then
10: \(\quad\) Update \(\lambda_{\text {best }}=\lambda^{\prime}\);
11: end if
12: Exchange the \(a\) th batch and the \(b\) th batch back;
13: Set times \(=\) times +1 ;
14: end while
15: if \(C_{\max }\left(\lambda_{\text {best }}\right)<C_{\max }(\lambda)\) then
16: \(\quad\) Update sum \(=l\) and \(\lambda=\lambda_{\text {best }}\);
17: end if
18: end while
```

Algorithm 3. The $\mathrm{EDA}_{l s}$ algorithm.

```
1: Initialize parameters \(Q, \alpha\) and \(\beta\);
2: Create an initial population of individuals;
3: Set \(t=0\);
4: while \(t<\) Maximum_Generations do
5: For each individual (corresponding to a job sequence), group jobs into batches using the BF heuristic, sequence the
    obtained batches by the LIWT heuristic and then calculate the \(C_{\max}\) value;
6: Apply the insert-based local search and swap-based local search to the best solution orderly;
7: Determine the best \(Q_{1}\) individuals from the current population;
8: Update the probabilistic matrix with the selected individuals by Equation (17);
9: Sample from the probabilistic matrix to generate new population;
10: Update \(t=t+1\);
11: end while
12: Output the best \(C_{\max }\) found so far;
```

Table 4. Summary of experimental design.

Table 5. Simulation results under different combinations of $\alpha$ and $\beta$.
Note: 1-25 represent the 25 combinations of $(\alpha, \beta)$. For example, ' 2 ' represents combination $(0.05,0.01)$.

# 6.2 Parameter settings 

A preliminary experiment was conducted to determine the parameters for the EDA. There are three parameters that affect solution quality and computational time obtained by the EDA. They are population size $Q$, parameter $\alpha$ associated with the best $Q_{1}$ individuals, and learning rate $\beta$. The population size was fixed to 40 . In order to set $\alpha$ and $\beta$, different values of them were tested: $\alpha \in\{0.05,0.1,0.2,0.3,0.4\}$ and $\beta \in\{0.005,0.01,0.05,0.1,0.5\}$. This results in a total of 25 combinations. All the combinations were tested on the whole 100 job instances. For each instance, the EDA was run five independent times with a termination criterion of a maximum of 200 generations and the average makespan values were reported. The simulation results are shown in Table 5. The EDA was coded in JAVA. All the experiments were run on a Windows 7 Enterprise computer with AMD Dual Core processor 2.3 GHz and 4.0 GB of RAM.

Table 5 shows the fourth combination, i.e. $(0.05,0.1)$, achieves the best result among all the combinations. Thus, $\alpha$ and $\beta$ are set to 0.05 and 0.1 in the further experiments.

### 6.3 Comparison of EDA and CPLEX

In this subsection, the mixed integer programming model given in Section 3 was solved using CPLEX and its results were compared with the EDA. CPLEX is a commercial solver for linear programming problems. In our experiments, we terminated

Table 6. Results of CPLEX and EDA.

Note: ' - ' represents CPLEX cannot find a feasible solution in 1800 s .
CPLEX after allowing it to run for 1800 s and the best-known solution was used for comparison. Several random problem instances of category T1s2R2 were generated and the numbers of jobs varied from 10 to 100.

Table 6 shows the results obtained by CPLEX and the EDA for these instances. Column 1 represents the number of jobs for the instances. Columns 2, 3 and 4 report the $C_{\text {max }}$, GAP and run time (s) obtained by CPLEX, respectively. Each instance was solved 10 times by the EDA. Columns 5, 6, 7 and 8 report the best, average, worst $C_{\text {max }}$, and the standard deviation (SD) among the 10 runs of the EDA, respectively. Column 9 reports the run time (s) taken by the EDA. The last column reports the improvement realised through the EDA over CPLEX in terms of the solution, where Impr. $(\%)=100 *\left[C_{\max }(\right.$ CP L E X $)-$ Best $\left.C_{\max }(\mathrm{EDA})\right] / C_{\max }(\mathrm{CPLEX})$.

As can be observed from Table 6, for the 10-20 job instances, the $C_{\text {max }}$ obtained by CPLEX is better than the best one obtained by the EDA. When the number of jobs is greater than or equal to 25 , the EDA reports better results as compared to CPLEX. In addition, the EDA takes much less time than CPLEX.

# 6.4 Comparison of EDA and PSO 

The EDA is compared with the PSO algorithm proposed by Muthuswamy et al. (2012). The parameters of the PSO algorithm were fixed the same as those in the literature except the number of particles and number of iterations. In our experiments, the two parameters were set to 100 particles and 1000 iterations for PSO.

Table 7 presents the results obtained by the EDA and PSO algorithms for 20 job instances. Column 1 represents the run code for the problem instances. Five instances were generated for each run code and each instance was solved five independent times by each algorithm. Columns 2, 3 and 4 report the average values of the best, average and worst $C_{\text {max }}$ of the five instances among the five runs of the EDA, respectively. Columns 5 and 6 report the standard deviation and the average run time (s) taken by the EDA for each instance. Columns $7-11$ report those results obtained by the PSO algorithm. Column 12 reports the improvement realised through the EDA over PSO in terms of solution quality, where Impr. (\%) over PSO $=100 *\left[\right.$ Avg. $\left.C_{\max }(\mathrm{PSO})-\right.$ Avg. $\left.C_{\max }(\mathrm{EDA})\right] /$ Avg. $\left.C_{\max }(\mathrm{PSO})\right.$. Tables $8-11$ show the results obtained by the two algorithms for $50,100,200$ and 300 job instances, respectively.

It can be seen from Table 7 that for all the 20 job instances, the solutions obtained by the EDA are better than those obtained by PSO. Moreover, the SD values of the solutions produced by the EDA are smaller when compared to PSO. It signifies that the EDA is more robust than PSO. On average, the EDA is better than PSO by $2.87 \%$.

As can been observed from Tables 8-11, the solutions yielded by the EDA are better than the solutions yielded by PSO for all the categories of problem instances. Especially, the improvements realised through the EDA over PSO become more

Table 7. Results for 20 job instances.

Table 8. Results for 50 job instances.

Table 9. Results for 100 job instances.

pronounced as the number of jobs in the instances increases. For example, the EDA is better than PSO by, on average, $6.96 \%$ for 50 job instances, while the EDA is better than PSO by $14.01 \%$ for 300 job instances. Besides, for each problem category, the EDA achieves better the best, average and worst $C_{\text {max }}$ when compared to PSO. In addition, the SD values of the solutions produced by the EDA are consistently less than those produced by PSO. For example, the average SDs of the EDA and PSO algorithms are, respectively, 5.04 and 43.27 for 300 job instances, which indicates that the EDA has the better quality of convergence.

Figures 5-8 graphically show the effect of different problem factors, including number of jobs, job sizes, job ready times and setup times, on the average improvement in makespan when the EDA and PSO algorithms are compared, respectively. From these figures, it is evident that the EDA is more effective than PSO.

Table 10. Results for 200 job instances.

Table 11. Results for 300 job instances.

![img-3.jpeg](img-3.jpeg)

Figure 5. Effect of job number on makespan improvements.

EDA vs. PSO
![img-4.jpeg](img-4.jpeg)

Figure 6. Effect of job size distribution on makespan improvements.

![img-5.jpeg](img-5.jpeg)

Figure 7. Effect of job ready time distribution on makespan improvements.

# EDA vs. PSO 

![img-6.jpeg](img-6.jpeg)

Figure 8. Effect of setup time on makespan improvements.

Table 12. Results of the EDA and the $\mathrm{EDA}_{l s}$ for 100 job instances.

With respect to the run times of the EDA and PSO algorithms, experimental results show the run time of the EDA is less than that of PSO for smaller scale problems ( 20 and 50 jobs). The EDA requires more run time compared to PSO as the number of jobs increases. This is due to the fact that the EDA generates new population by sampling from the probabilistic model.

### 6.5 Comparison of EDA and $E D A_{l s}$

In order to see the effectiveness of combining the EDA algorithm and problem-dependent local search, computational experiments and comparison were conducted between the EDA and the $\mathrm{EDA}_{l s}$ algorithms. The computational results are given in Tables 12-14.

It is easily observed from Tables 12-14 that the solutions obtained by the $\mathrm{EDA}_{l s}$ are better than those obtained by the EDA. On average, the improvement of the $\mathrm{EDA}_{l s}$ over the EDA in terms of solution quality is $1.89 \%$ for 100 job instances, $1.55 \%$ for 200 job instances, and $1.33 \%$ for 300 job instances, respectively. This indicates the fact that incorporating the local

Table 13. Results of the EDA and the $\mathrm{EDA}_{O_{2}}$ for 200 job instances.

Table 14. Results of the EDA and the $\mathrm{EDA}_{O_{2}}$ for 300 job instances.

search in the EDA algorithm leads to further improvement in solution quality. Compared to the EDA, the $\mathrm{EDA}_{O_{2}}$ requires longer run time. However, its solution quality is better.

# 7. Conclusions 

This paper investigated the problem of minimising makespan in a no-wait flowshop with two batch processing machines (BPMs), non-identical job sizes and arbitrary ready times. A parallel BPM (p-batch) is followed by a serial BPM (s-batch). The problem was formulated as a mixed integer linear programming model. We then proposed a population-based evolutionary method named estimation of distribution algorithm (EDA), in which individuals were represented as job sequences. A probabilistic model was built to generate new individuals and an incremental learning mechanism was developed to update the probabilistic model. The best-fit heuristic was adopted to form batches and a least idle/waiting time approach was proposed to schedule the batches. Two local search heuristics were embedded in the EDA to further enhance the exploitation ability. Computational experiments and comparisons demonstrated the superiority of the proposed algorithm for solving the problem under study in terms of solution quality and robustness. The effectiveness of the local search was evaluated.

There are a few important directions for future research. First of all, this research can be extended to optimise other objectives such as total completion time, completion time variance and so on. Adding due date constraints to the jobs is also of interest as it may arise in real-world applications. In addition, this approach could be extended to flowshop problems with more than two stages. Finally, BPM problems with incompatible job families can be considered as well.

## Funding

This work was supported by the National Natural Science Foundation of China [grant number 71171184]. This research also received funding from the University of Tennessee Health Information Technology \& Simulation (HITS) Laboratory.

# Disclosure statement 

No potential conflict of interest was reported by the authors.
