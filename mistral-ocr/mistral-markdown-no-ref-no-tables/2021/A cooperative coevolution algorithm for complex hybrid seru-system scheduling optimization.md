# A cooperative coevolution algorithm for complex hybrid seru-system scheduling optimization 

Yuting Wu ${ }^{1}$ (1) $\cdot$ Ling Wang ${ }^{1}$ (1) $\cdot$ Jing-fang Chen ${ }^{1}$ (1)<br>Received: 13 April 2021 / Accepted: 9 June 2021<br>(c) The Author(s) 2021


#### Abstract

Under the current volatile business environment, the requirement of flexible production is becoming increasingly urgent. As an innovative production mode, seru-system with reconfigurability can overcome the lack of flexibility in traditional flow lines. Compared with pure seru-system, the hybrid seru-system composed of both serus and production lines is more practical for adapting to many production processes. This paper addresses a specific hybrid seru-system scheduling optimization problem (HSSOP), which includes three strongly coupled sub-problems, i.e., hybrid seru formation, seru scheduling and flow line scheduling. To minimize the makespan of the whole hybrid seru-system, we propose an efficient cooperative coevolution algorithm (CCA). To tackle three sub-problems, specific sub-algorithms are designed based on the characteristic of each sub-problem, i.e., a sub-space exploitation algorithm for hybrid seru formation, an estimation of distribution algorithm for seru scheduling, and a first-arrive-first-process heuristic for flow line scheduling. Since three sub-problems are coupled, a cooperation coevolution mechanism is proposed for the integrated algorithm by information sharing. Moreover, a batch reassign rule is designed to overcome the mismatch of partial solutions during cooperative coevolution. To enhance the exploitation ability, problem-specific local search methods are designed and embedded in the CCA. In addition to the investigation about the effect of parameter setting, extensive computational tests and comparisons are carried out which demonstrate the effectiveness and efficiency of the CCA in solving the HSSOP.


Keywords Hybrid seru-system $\cdot$ Cooperative coevolution $\cdot$ Estimation of distribution algorithm $\cdot$ Sub-space exploitation $\cdot$ Problem-specific local search

## Introduction

Under the background of Industry 4.0, demand volatility is a growing reality in current market due to the increasing demands of consumers as well as the rapid development of manufacturing technologies. However, traditional flow lines developed for mass production cannot well adapt to the changes in global market. To achieve production flexibility, many companies have transformed the flow lines into other production systems, e.g., seru-system [1], which can

[^0]be constructed by dismantling a flow line. A seru-system contains one or more serus, where a seru is an assembly unit that consists of simple equipment and one or several multiskilled workers to operate different types of production [2]. Such a system is more agile than the traditional production system. The agility comes from the quick reconfiguration considering the changes of demands, ensuring high levels of productivity and quality [3]. The seru-system can yield satisfactory performances in reducing makespan, labor time, carbon emission, required workforce, WIP inventories, and finished-product inventories [1, 4]. As an innovative production mode, the seru-production system has been successfully applied in many companies, e.g., Sony and Canon [5-7]. After reviewing operations management research in last 25 years of studies, Roth et al. [8] listed several promising research directions and pointed out "seru production systems are more flexible than Toyota's production system, and they represent the next generation of lean production that has recently been introduced to operations". Nowadays,


[^0]:    1) Ling Wang
    wangling@tsinghua.edu.cn
    Yuting Wu
    wyt20@mails.tsinghua.edu.cn
    Jing-fang Chen
    cjf17@mails.tsinghua.edu.cns
    1 Department of Automation, Tsinghua University, Beijing 100084, China

seru-system has gained increasing attention in both academic and engineering fields.

Generally, the seru-system can be classified into two types: pure seru-system (usually termed seru-system for short) composed of one or several serus, and hybrid serusystem composed of seru(s) and a flow line. For pure serusystem, Yin et al. [7] elaborated the origin and conversion process of seru-system and analyzed the reasons of its successful applications. Kaku et al. [9] analyzed the human-task-related performances in line-cell conversion (LCC) including the operational tasks, skill level and the crosstraining of workers. Three theoretical models including a conveyor assembly line (CAL), a cellular manufacturing (CM) and a joint type (CAL + CM) were built and a human-factor-based training method was presented. Kaku et al. [10] addressed the LCC problem by considering the total throughput time (TTPT) and total labor hour (TLH) as objectives. Yu et al. [11] focused on an LCC problem including two sub-problems: assembly cell formation and assembly cell loading. A mathematical model was developed to minimize the TTPT and the TLH, and the Pareto-optimal front of the model was investigated. Besides, several managerial insights on improving the performance of LCC were summarized to facilitate the implementation of seru-system. Yu et al. [12] formulated the LCC problem into a mathematical model with the objectives of reducing worker number and increasing productivity. They designed an exact algorithm to find Pareto-optimal solutions. The results showed that the performance of LCC could be improved by reducing worker number without deteriorating productivity. Yu et al. [13] developed a model to minimize the TTPT and the TLH. They analyzed the mathematical model and revealed some mathematical characteristics of the problem. A nondominated sorting genetic algorithm (NSGA-II) was employed to obtain Pareto-optimal solutions on large-sized cases. Liu et al. [14] designed an algorithm based on NSGA-II to minimize the carbon dioxide emission and makespan. Sun et al. [15] developed a cooperative coevolution algorithm by combining GA, local search and ant colony algorithm for the seru production with the minimization of makespan. Yılmaz [16] built a mathematical model for the workforce scheduling problem in seru-system and designed an NSGA-II to minimize the makespan and workload imbalance. Yılmaz [17] presented an optimization model to achieve Shojinka (refer to transferring workers in seru-system) and designed variants of GAs for distinct scenarios, respectively. The structural characteristics, lower bound, and upper bound were analyzed as well. Zhang et al. [18] proposed a PSO algorithm for a scheduling problem in unbalanced seru production system with lot splitting.

Compared to the pure seru-system, the hybrid seru-system with serus and a flow line is more practical, since it can adapt to many production processes. For instance, some
equipment is too expensive or bulky to copy or move to the serus so that it needs to be retained in the flow line. Besides, some temporary workers must be assigned to the flow line, since they are not capable of completing all processes in a seru. This situation often occurs when order demand suddenly increases [21]. However, the literature about the hybrid seru-system is very scant. To the best of our knowledge, Kaku et al. [19] first presented the concept of hybrid seru-system which was formed by a CM and a CAL, and they formulated the system into a model to minimize the TTPT and TLH. Subsequently, Kaku et al. [9] constructed a theoretical model of CAL + CM with the constraints of additional operational tasks, the skill level and the cross-training of workers. Kaku et al. [10] proposed a model to describe the problem of LCC mathematically with the TTPT and the TLH as optimization objectives. Liu et al. [20] proposed a comprehensive mathematical model of hybrid seru-system incorporating the number of serus and workers as decision variables. The model was studied on an industrial case, and the experiment results indicated that the proposed model could achieve better performances on the reconfiguration problem of flow line compared to Kaku's model [10]. Yu et al. [21] formulated several hybrid seru-system models under an integrated framework and analyzed the properties of hybrid seru-system by means of dividing sub-space. An exact algorithm and a heuristic were developed to solve hybrid seru-system optimization problem on different scales of instances.

From the above literature review on seru-system, most of the research works focus on pure seru-system rather than hybrid seru-system. Regarding the existing research on hybrid seru-system, the proposed algorithms cannot obtain satisfactory solutions in solving large-scale instances with limited computational time. Therefore, it is significant to develop effective algorithms for solving the large-scale hybrid seru-system optimization problem.

The cooperative coevolution (CC) [22] provides an effective divide-and-conquer architecture to solve largescale optimization problems by decomposing the complex problem into several sub-problems. The effectiveness of the CC mechanism exhibits its potential to divide and conquer complex coupled optimization problems [23]. Some typical works about CC are as follows. Omidvar et al. [24] proposed a contribution based cooperative coevolution to alleviate the unbalance due to the different contribution of sub-problems to the global fitness calculation. The sub-problems were treated according to their respective contributions, which effectively saved the computational resources compared with the strategy that treats all the sub-problems equally. Omidvar et al. [25] proposed a differential grouping method that could reveal the interaction structure of the decision variables and form the least connected sub-problems. In addition, they analyzed the validity of this decomposition

strategy mathematically. Shang et al. [26] presented a multi-population cooperative coevolutionary algorithm for multi-objective capacitated arc routing problem. The whole population was divided into several sub-populations which evolved, respectively, in each generation, and an internal elitism archive was constructed to speed up the convergence of algorithm. Trunfio et al. [27] presented a new CC algorithm based on the dimension of the sub-components and the size of population during the process of evolution, which outperformed the algorithm based on a homogeneous decomposition. Besides, they investigated the effect of the population size and dimension of sub-problems on the CC mechanism. Hu et al. [28] designed a fast interdependency identification algorithm for CC in solving large-scale global optimization problems. Specifically, the algorithm could recognize whether the variables were separable and then avoid factoring non-separable variables to achieve nearoptimal decomposition for CC. Yang et al. [29] proposed a data-driven decomposition method for CC, which mined the information among variables based on historical evolutionary data and grouping the variables dynamically. Li et al. [30] presented a fuzzy decomposition algorithm based on an interaction structure matrix and designed a spectral clustering algorithm to decompose the decision variables according to the number of sub-populations. Yang et al. [31] designed an efficient recursive differential grouping method to reduce the consumption of computation on the decomposition of CC.

In this paper, a cooperative coevolution algorithm (CCA) is proposed to solve the HSSOP with the minimization of makespan criterion. We decompose a hybrid seru-system into three decision-making processes, i.e., hybrid seru formation, seru scheduling, and flow line scheduling. To tackle three strongly coupled sub-problems, effective subalgorithms are designed for different sub-problems. To be specific, a sub-space exploitation algorithm (SSEA) is developed to solve the hybrid seru formation sub-problem by exploiting the solution space with different number of serus; an estimation of distribution algorithm (EDA) is presented to solve the seru scheduling sub-problem by learning the distribution of high-quality batching processing sequences; and a first-arrive-first-process (FAFP) heuristic is designed to efficiently and effectively generate a flow line scheduling. To improve the performance of the integrated algorithm, a cooperation coevolution (CC) mechanism is proposed via information sharing. Moreover, a batch reassignment rule (BRR) is designed to avoid mismatch of the partial solutions. To enhance the exploitation ability of CCA, multiple local search methods are developed based on the characteristics of sub-problems. Extensive testing results and comparisons demonstrate the effectiveness of the proposed algorithm.

The remaining contents of the paper are organized as follows. Section "Formulation of HSSOP" describes the

HSSOP with a computational model. In Section "CCA for HSSOP", the design of the CCA is presented in detail. Section "Computational results and comparisons" presents the investigation on parameter setting and the comparison on performances. Finally, the paper is ended with some conclusions and the future work.

## Formulation of HSSOP

## Problem description

The hybrid seru-system studied in this paper is shown in Fig. 1, which is a generalization of the model in [4]. The complicated operation of such a hybrid seru-system is considered as a four-stage decision process, including worker allocation, seru formation, seru scheduling and flow line scheduling. The operation process of the hybrid seru-system is stated as follows.

The problem to be solved in this paper concentrates on structuring the hybrid seru-system and scheduling batches in the system properly. There are $W$ workers with different skill levels and $N$ batches with various types. Different workers have different levels of proficiency for different product types. The processing time of various batches in different serus is different due to the diversity of worker skill levels in each seru. All the batches should pass through the serusystem first and then through the flow line to complete all the processing tasks. A hybrid seru-system is constructed, where three aspects are required to be determined: the number of workers allocated to the serus, the number of serus to be formed and the number of workers assigned to the flow line. Step 1: determine the numbers of workers in the flow line and serus. Step 2: determine the number of serus to be formed and the workers allocated to each seru and the flow line. Then, batches should be assigned to the hybrid seru-system. There are $N$ batches to be processed and each batch can be assigned to any of the serus. Step 3: determine the seru which each batch assigns to and then determine the processing sequence of batches in each seru. Once the batch assignment is determined, the whole assembling process of a batch must be fulfilled within a single seru. Step 4: after all the batches are assembled by the seru-system, they are sent to the flow line for final manufacturing procedure. The sequence of batches in the flow line is determined in this step. Briefly, the above four steps are called worker allocation, seru formation, seru scheduling and flow line scheduling, respectively. The objective is to minimize the makespan of hybrid seru-system by reasonably arranging the four-stage decision process.

In Fig. 1, two serus are constructed: seru 1 contains worker 1 and worker 5, while seru 2 contains worker 2 and worker 4 . Worker 3 and worker 6 are assigned to the flow

![img-0.jpeg](img-0.jpeg)

Fig. 1 An example of hybrid seru-system
line. There are 6 batches to be processed. Batch 1, batch 3 and batch 4 are processed in seru 1 in order, while batch 2 , batch 5 and batch 6 are processed in seru 2 in sequence. Finally, six batches are sent to the flow line to finish the final process.

## Computational model

The following assumptions are considered in this paper.

- The product type of each batch is known in advance. Each batch specifies a particular product type.
- The required tasks of each product are the same. If a product type does not need a task, the product skips the task.
- The tasks are the same as the ones in the original flow line. The number of tasks is $W$.
- In the original flow line, each worker is responsible for a task. After dismantling the flow line into a hybrid serusystem, workers assigned to the seru-system can operate all the processing tasks.
- The workers left in the flow line still process the tasks that are originally processed in the original flow line.

The notation definitions are presented as below.
Indices:
$i$ : Index of workers $(i=1,2, \ldots, W)$.
$j$ : Index of serus $(j=1,2, \ldots, J)$.
$n$ : Index of product types $(n=1,2, \ldots, N)$.
$m, s$ : Index of product batches $(m=1,2, \ldots, M)$.
$k$ : Index of the sequence of product batches in a seru $(k=1,2, \ldots, M)$.
$r$ : Index of the sequence of product batches in the flow line $(r=1,2, \ldots, M)$.
Parameters:
$V_{m, n}: 1$, if product type of batch $m$ is $n ; 0$, otherwise.
$B_{m}$ : Size of product batch $m$.
$T_{n}$ : Cycle time of product type $n$ in the original flow line. $\eta_{i}$ : Upper bound on the number of tasks for worker $i$ in a seru. If the number of tasks assigned to worker $i$ is more than $\eta_{i}$, then worker $i$ 's average task time within a seru will be longer than her or his task time within the original flow line.
$\varepsilon_{i}$ : Worker $i$ 's coefficient of influencing level of doing multiple tasks.
$\beta_{m}$ : Skill level of worker $i$ for each task of product type $n$.

Binary variables:
$Y_{i}: 1$, if worker $i$ is left in the flow line; 0 , otherwise.
$X_{i, j}: 1$, if worker $i$ is assigned to seru $j ; 0$, otherwise.
$Z_{m, j, k}: 1$, if product batch $m$ is assigned to seru $j$ in sequence $k ; 0$, otherwise.
$O_{m, r}: 1$, if product batch $m$ is processed in flow line in sequence $r ; 0$, otherwise.

Four binary variables correspond to the four decision processes: worker allocation, seru formation, seru scheduling and flow line scheduling. If the four binary variables are determined, the makespan of hybrid seru-system can be calculated as follows.
$C_{i}=\left\{\begin{array}{c}1+\varepsilon_{i}\left(W-\sum_{j=1}^{W} Y_{i j}-\eta_{i}\right), W>\eta_{i}, \quad \forall i \\ 1, W \leq \eta_{i}\end{array}\right.$
$\mathrm{TC}_{m}=\frac{\sum_{n=1}^{N} \sum_{i=1}^{W} \sum_{j=1}^{J} \sum_{k=1}^{M} V_{m, n} T_{n} \beta_{n, i} C_{i} X_{i, j} Z_{m, j, k}}{\sum_{i=1}^{W} \sum_{j=1}^{J} \sum_{k=1}^{M} X_{i, j} Z_{m, j, k}}$
$\mathrm{FC}_{m}=\frac{B_{m} \mathrm{TC}_{m} W}{\sum_{i=1}^{W} \sum_{j=1}^{J} \sum_{k=1}^{M} X_{i, j} Z_{m, j, k}}$
$\mathrm{FCB}_{m}=\sum_{p=1}^{m-1} \sum_{j=1}^{J} \sum_{k=1}^{m} F C_{p} Z_{m, j, k} Z_{p, j,(k-1)}$
$\mathrm{TL}_{m}=\max _{1 \leq i \leq W}\left(V_{m, n} T_{n} \beta_{n, i} Y_{i}\right), \quad \forall i$
$\mathrm{FL}_{m}=\sum_{n=1}^{N} \sum_{i=1}^{W} V_{m, n} T_{n} \beta_{n, i} Y_{i}+\left(B_{m}-1\right) T L_{m}$
$\mathrm{FLB}_{m}=\left\{\begin{array}{l}\mathrm{FCB}_{m}+\mathrm{FC}_{m}, \quad m \text { is finished later than } s \\ \mathrm{FLB}_{s}+\mathrm{FL}_{s}, \quad m \text { is finished no later than } s\end{array},(s \mid O_{m, r}=1, O_{s,(r-1)}=1, \forall r)\right.$
$C_{\max }=\max _{1 \leq m \leq M}\left(\mathrm{FLB}_{m}+\mathrm{FL}_{m}\right)$
Equation (1) is to calculate the coefficient variation of worker $i$ 's increased task time after line-seru conversion. If the number of worker $i$ 's tasks within a seru is over her/ his upper bound $\eta_{i}$, then the worker will cost more average task time than her/his task time within the original flow line. Equation (2) is to calculate the processing time of product batch $m$ per task in the seru. In a seru, the processing time of product type $n$ is the average processing time of all the workers in the seru. Equation (3) is to calculate the processing time of product batch $m$ in the seru. Equation (4) is to calculate the begin time of product batch $m$ in the seru. Equation (5) is to calculate the worst task time of the workers in the flow line for product batch $m$. Equation (6) is to calculate the processing time of product batch $m$ in the flow line. Equation (7) is to calculate the begin time of product batch $m$ in the flow line. Since the hybrid system has serus and a flow line, $F L B_{m}$ should be the maximum between the
completion time of the prior product batch $s$ in the flow line and the completion time of product batch $m$ in serus. If the completion time of product batch $m$ in serus is later than the completion time of product batch $s$ in the flow line, then $F L B_{m}$ equals $F C B_{m}+F C_{m}$; otherwise, $F L B_{m}$ equals $F L B_{s}+F L_{s}$. Equation (8) is to calculate the makespan of hybrid seru-system, which is the completion time of the last processing batch in the flow line.

## CCA for HSSOP

The HSSOP contains multiple coupled decision-making subproblems, which makes it difficult to solve directly. Therefore, we employ a divide-and-conquer strategy to deal with such a complex problem. According to the four-stage decision process described in 2.1, it is clear that the purpose of worker allocation and seru formation is to build the hybrid seru-system. Therefore, we combine the two decision processes as one sub-problem. Thus, the HSSOP can be divided into three sub-problems: hybrid seru formation (including worker allocation and seru formulation), seru scheduling and flow line scheduling.

For a non-separable problem, strong interdependency between sub-problems definitely causes the difficulty in evaluating the performance [32]. For the HSSOP, to evaluate a complete solution, it should consider three sub-problems jointly, i.e., hybrid seru formation (HSF), seru scheduling
$\mathrm{C}_{\max }=\max _{1 \leq m \leq M}\left(\mathrm{FLB}_{m}+\mathrm{FL}_{m}\right)$
Equation (1) is to calculate the coefficient variation of worker $i$ 's increased task time after line-seru conversion. If the number of worker $i$ 's tasks within a seru is over her/ his upper bound $\eta_{i}$, then the worker will cost more average task time than her/his task time within the original flow line. Equation (2) is to calculate the processing time of product batch $m$ per task in the seru. In a seru, the processing time of product type $n$ is the average processing time of all the workers in the seru. Equation (3) is to calculate the processing time of product batch $m$ in the seru. Equation (4) is to calculate the begin time of product batch $m$ in the seru. Equation (5) is to calculate the worst task time of the workers in the flow line for product batch $m$. Equation (6) is to calculate the processing time of product batch $m$ in the flow line. Equation (7) is to calculate the begin time of product batch $m$ in the flow line. Since the hybrid system has serus and a flow line, $F L B_{m}$ should be the maximum between the
(SS), and flow line scheduling (FLS). A complete solution consists of three partial solutions: partial solution-HSF, partial solution-SS and partial solution-FLS. The description of constructing a complete solution of hybrid seru-system is shown in Fig. 2.

For hybrid seru formation, the makespan depends on both the number of serus and the allocation of workers; for seru scheduling, the makespan depends on the batch assignment and processing sequence in seru-system; for flow line scheduling, the makespan depends on the batch processing sequence in flow line which is affected by the completion time of each batch in seru-system. The HSSOP is so complicated that it cannot be enumerated or solved by mathematical programming in limited time. Heuristic algorithms usually cannot get satisfactory solutions for large-scale instances. Comparatively, evolutionary algorithms can gain satisfactory solutions in limited time and have been successfully applied to pure seru-system [14-18]. Thus, it motivates us to develop an effective evolutionary algorithm to solve the HSSOP with makespan minimization criterion. Since

Fig. 2 A complete solution of hybrid seru-system
![img-2.jpeg](img-2.jpeg)
![img-2.jpeg](img-2.jpeg)

Fig. 3 The representation of a partial solution-HSF
sub-algorithms play important roles in facilitating the integrated algorithm, we design different sub-algorithms for different sub-problems according to their characteristics in this paper. So, we design a special SSEA to determine the number of serus and the allocation of workers, design a special EDA to determine batch assignment and processing sequence in seru-system by learning the distribution of batch processing priority, and design a special FAFP heuristic to determine the batch processing sequence in flow line. Next, we introduce the SSEA, EDA and FAFP in detail.

## The SSEA for hybrid seru formation

For hybrid seru formation, a solution should reflect the worker allocation and seru formation (the number of seru(s) to be constructed and the worker assignment in each seru and flow line). In this paper, solution space is partitioned into several sub-spaces according to the number of serus. Each sub-space contains the partial solution-HSFs with same number of serus. Each solution is encoded as a string with $W+1$ integer value. The $i$ th number of the string implies whether the $i$ th worker is allocated to the flow line or the serus. Integer $j(j>0)$ means that the worker is allocated to seru $j$, and 0 means that the worker is allocated to the flow line. To ensure the feasibly of the partial solution-HSF, each integer value in $[0, J]$ must appear at least once.

An example of a partial solution-HSF is shown in Fig. 3. There are 6 workers, and 3 serus are constructed. A feasible solution $P_{i}$ can be $\{011023\}$, which implies that worker 1 and worker 4 are assigned to the flow line, worker 2 and worker 3 are assigned to seru 1 , worker 5 is assigned in the seru 2 and worker 6 is assigned in the seru 3.

In [21], it is shown that the minimal makespan usually exists in the sub-space-seru with fewer serus by analyzing the features of solution space. With such prior knowledge, an SSEA is designed to evolve hybrid seru formation population for good partial solution-HSFs. The procedure of the SSEA is shown in Fig. 4, which includes population initialization, crossover, and local search.

## Population initialization

Clearly, $W$ workers can construct a hybrid seru-system with at most $W-1$ serus. Therefore, we construct $W-1$ sub-spaces in the initialization phase. Each sub-space contains $Q$ partial solution-HSFs that are generated randomly. Dividing the initial population according to the number of seru, it is helpful to generate diverse initial partial solution-HSFs so as to enhance the capability of global exploration. An example of population initialization with 6 workers is shown in Fig. 5.

## Crossover operators

To evolve the hybrid seru formation, two crossover operators are used for every sub-space. For each sub-space, it finds the best individual $P_{b}$ and the worst individual $P_{w}$. Then, it determines the global best individual $P_{g}$ among all sub-spaces. To exchange the information among different individuals, we design two crossover operators as illustrated in Fig. 6 with examples, where 10 workers, 3 serus, $P_{b}=\{0$ 310213201$}, P_{w}=\{2023102030\}, P_{g}=\{03201$ 30122$}, p 1=6, p 2=4, p 3=7$.

Crossover operator 1: Single point crossover performed on $P_{b}$ and $P_{w}$ to produce a new individual $P_{n}$. To be specific, first a random position p 1 is generated, and then the elements before position p 1 in $P_{b}$ and the elements after position p 1 in $P_{w}$ are combined to form a new individual $P_{n}$.

Crossover operator 2: Multiple-point crossover performed on $P_{g}, P_{b}$ and $P_{w}$. To be specific, first two random positions p 2 and p 3 are generated; then the elements between p 2 and p 3 in $P_{w}$ is reserved to the new individual $P_{n}$, and

![img-3.jpeg](img-3.jpeg)

Fig. 4 The procedure of the SSEA for hybrid seru formation population
![img-4.jpeg](img-4.jpeg)

Fig. 5 An example of population initialization with 6 workers
the elements before p 2 in $P_{g}$ are inherited to $P_{u}$, and the elements after p 3 in $P_{u}$ are taken from $P_{g}$.

If $P_{u}$ is better than $P_{w}$, then replace $P_{w}$ with $P_{u}$ and update $P_{g}$ if necessary.

## Local search in SSEA

In SSEA, if crossover operator 2 fails to improve the worst individual, a local search will be performed on $P_{b}$ for further exploitation. In this paper, the following search operators are used in a hybrid way as Algorithm 1, where $\gamma$ denotes the search depth of local search.

LS-swap: Swap the $p$ th element and the $q$ th element in a string, where $p$ and $q$ are two different integers generated randomly.

LS-insert: Insert the $p$ th element after the $q$ th element in a string.

LS-reverse: Reverse the sub-sequence between the $p$ th element and the $q$ th element in a string.

LS-exchange: Choose two different elements $d$ and $b$ $(0 \leq d<b \leq W-1)$ and then exchange all $d$ and $b$.

Fig. 6 Illustration of two crossover operators
![img-5.jpeg](img-5.jpeg)
(b) Crossover operator 2

```
Algorithm 1 Procedure of local search
Input: a solution \(P\)
    Set \(l=0, k=0\);
    While \(l<j^{\prime}\)
        If \(k=0\)
        Perform LS-swap to get \(P^{\prime}\)
        Else if \(k=1\)
            Perform LS-insert to get \(P^{\prime}\)
        Else if \(k=2\)
            Perform LS-reverse to get \(P^{\prime}\)
        Else if \(k=3\)
        Perform LS-exchange to get \(P^{\prime}\)
        End if
        If \(P>P^{\prime}\)
        \(P=P^{\prime}, k=k+1, l=l+1\)
        End if
        If \(k>3\)
        \(k=0\)
        End if
        End while
Output: the improved solution
```


## EDA for seru scheduling

As a population-based evolutionary algorithm, EDA [33] has been successfully applied to a variety of scheduling problems, such as flow shop scheduling [34-36], flexible job shop scheduling [37], and robotic assembly line balancing [38]. Compared with the crossover and mutation-based evolutionary algorithms such as GA, EDA employs an explicit
probability model for sampling a promising area to achieve exploration.

The seru scheduling should solve two sub-problems, i.e., the batch assignment and the batch sequencing in each seru. To solve this problem, an EDA with local search (EDA-LS) is proposed by fusing the exploration ability of EDA and the exploitation ability of local search. The procedure of the EDA-LS is shown in Fig. 7. Next, we will introduce encoding and decoding, probability model and its updating mechanism, and local search in detail.

## Encoding and decoding of a partial solution-SS

For seru scheduling, it needs to determine the batch assigned to each seru and the batch processing sequence in each seru. Let $\pi$ denote an individual of seru scheduling (a partial solu-tion-SS) encoded as a $J$-dimensional vector $\left[\begin{array}{llll}v_{1} & v_{2} & \ldots & v_{J}\end{array}\right]^{T}$, where $v_{j}$ represents the batch processing sequence in seru $j$. A partial solution-SS can be represented by a batch priority string $\varphi$ with a length of $M$. The element in the batch priority string is denoted by job number. The occurrence of a batch number in $q$ th position of the batch priority string indicates such a batch is processed in $q$ th order.

![img-6.jpeg](img-6.jpeg)

Fig. 7 Procedure of the EDA-LS for seru scheduling

```
Algorithm 2 Procedure of ECFL rule
Input: a batch priority string \(\varphi\)
    For \(j=1\) to \(J\)
        \(N_{j}=0\)
    End for
    For \(q=1\) to \(M\)
        Find the seru \(j\) that can process batch \(\varphi(q)\) with
            the earliest completion time in the flow line.
            \(\pi_{j}\left[N_{j}\right]=\varphi(q)\)
        \(N_{j}=N_{j}+1\)
        End for
Output: a partial solution-SS \(\pi\)
```

To decode a batch priority string $\varphi$ into a partial solutionSS $\pi$, an earliest completion flow line (ECFL) rule shown in Algorithm 2 is designed to assign batches to seru according to the batch priority string $\varphi$. Consider an example with 7 batches and 2 serus, the related data are given in Table 1. An encoded partial solution-SS is illustrated in Fig. 8, while a decoded hybrid seru scheduling is illustrated in Fig. 9.


## Probability model and updating mechanism

A probability model is built to reflect the distribution of the solution space and produce new solutions. The probability model should keep updating by a reasonable mechanism to achieve exploration [39]. In this paper, the probability model and its updating mechanism are designed as follows.

According to the above encoding method, batch priority string directly affects the seru scheduling. Therefore, the following probability model $P(g)$ is designed to sample the batch priority string, where element $\rho_{\vec{w}}(g)$ denotes the probability that batch $b_{j}$ appears in the $i$ th position of the batch priority string at the $g$ th generation. The elements in matrix $P(0)$ are initialized as $\rho_{\vec{w}}(0)=1 / M(\forall i, j)$ for uniform sampling.

$$
P(g)=\left[\begin{array}{ccc}
\rho_{11}(g) & \rho_{12}(g) & \ldots & \rho_{1 M}(g) \\
\rho_{21}(g) & \rho_{22}(g) & \ldots & \rho_{2 M}(g) \\
\vdots & \vdots & \ddots & \vdots \\
\rho_{M 1}(g) & \rho_{M 2}(g) & \ldots & \rho_{M M}(g)
\end{array}\right]
$$

At each generation, a new batch priority string is generated by sampling the probability matrix to determine the position of each batch in the batch priority string. If the position of batch $b_{j}$ has already been determined, the whole elements in $j$ th column of probability matrix $P(g)$ are set as zero. Then, all the elements in $P(g)$ are normalized, which ensures that the sum of each row is 1 . After determining the batch priority string, the processing sequence of batches in each seru can be obtained according to the batch priority string based on the ECFL rule. Thus, an individual is generated.

After generating $E P$ new individuals of seru scheduling at each generation, $E P_{\text {size }}$ elite individuals are selected to update the probability matrix $P(g)$, where $E P_{\text {size }}=\alpha * E P$. The probability matrix $P(g)$ is updated as follows via

Table 1 The processing time of seven batches in two serus and flow line

Fig. 9 An example of hybrid seru scheduling with seven batches and two serus
![img-7.jpeg](img-7.jpeg)
incremental learning which is based on the historical information of the better individuals.
$\rho_{\mathrm{ij}}(g+1)=(1-\beta) \rho_{\mathrm{ij}}(g)+\beta \cdot \frac{1}{E P_{a \mid z e}} \cdot \sum_{h=1}^{E P_{a \mid z e}} I_{i j}^{h}(g)$,
where $\beta \in(0,1)$ denotes the learning rate and $I_{i j}^{h}(g)$ is the indicator function corresponding to the $h$ th elite individual.
$I_{i j}^{h}(g)=\left\{\begin{array}{c}1, \text { if batch } j \text { appears in the } i \text { th position in the batch priority string } \\ 0, \text { otherwise }\end{array}\right.$
in Fig. 10. If hybrid seru formation is determined, $S P T_{m}$ is a constant. Therefore, the makespan of flow line varies as $W T_{m}$. We define the batches with non-zero waiting time as critical batches, e.g., batch 3 , batch 6 , batch 2 and batch 5 in Fig. 10. Let $B_{c}$ be the set of critical batches. Clearly, the makespan of a hybrid seru-system can be reduced by adjusting the position of critical batches in seru-system.

Based on the above analysis, we design three critical batch-based local search operators to adjust the batch prior-
$I_{i j}^{h}(g)$ ity string: LS (1), LS (2) and LS (3) [40, 41]. Each local search operator incorporates a critical batch $b_{c}\left(b_{c} \in B_{c}\right)$ and a randomly selected batch $b_{r}\left(b_{r} \neq b_{c}\right)$.

LS (1): Swap the order of batch $b_{c}$ and batch $b_{r}$ in the batch priority string.
LS (2): Insert batch $b_{r}$ to the position after batch $b_{r}$ in the batch priority string.
LS (3): Invert the sequence between the position of batch $b_{c}$ and batch $b_{r}$ in the batch priority string.

The local search enumerates all feasible positions for better solutions. If a local search operator can generate a better

Fig. 10 Illustration of waiting time and critical batch
![img-8.jpeg](img-8.jpeg)

new individual (defined as a valid operator), then restart enumeration on the new solution; otherwise, employ the next local search operator until all the operators are used. The local search procedure is shown in Algorithm 3. Note that local search is performed only on the elite individuals.

## Cooperation coevolution mechanism

To evaluate the quality of a partial solution, it requires the other information of a complete solution. The quality of a complete solution depends on all the information of three

```
Algorithm 3 Procedure of local search for seru scheduling
Input: an elite individual \(S\)
    Calculate the makespan of hybrid seru-system according to algorithm 1, denoted as \(C_{\max }\) of \(S\).
    Determine the set of critical batches \(B_{c}\).
    For each batch \(b_{i} \in B_{i}\)
    For \(k=1\) to 3
        Implement search operator \(\mathrm{LS}(k)\) and gain a solution of seru scheduling \(S^{\prime}\). Calculate
        \(C_{\max }\) of \(S^{\prime}\).
        If \(C_{\max }\) of \(S^{\prime}\) is improved
            \(S \leftarrow S^{\prime}\)
            Go to line 1
        End if
        End for
    End for
Output: an improved individual.
```


## FAFP heuristic for flow line scheduling

For flow line scheduling, it needs to determine the processing order of batches in the flow line. Batches should be processed in the seru-system before being processed in the flow line. To reduce the waiting time of batches in the flow line, it is inferred that a better makespan can be obtained by setting higher processing priority in the flow line for the batch with earlier completion time in seru-system.

Based on the above analysis, first-arrive-first-process (FAFP) heuristic is designed for the flow line scheduling. To be specific, the batch that first arrives at the flow line is processed first in the flow line. Then, the makespan can be calculated according to the FAFP heuristic given a seru scheduling. The pseudo code is shown in Algorithm 4.
parts. To form a complete solution reasonably, the optimal partial solution of each sub-problem is provided to other sub-problems. The quality of the complete solution is used to evaluate the partial solution in current sub-problem. A cooperation coevolution mechanism is employed to interact information of partial solutions generated by each sub-algorithm.

Since the FAFP heuristic is used in the flow line scheduling, the objective can be calculated when the hybrid seru formation and the seru scheduling are determined. The population of seru scheduling evolves by EDA. For evaluating the quality of a partial solution-SS, the best hybrid seru formation is used as a partial solution-HSF and the flow line scheduling determined by FAFP heuristic is used as a partial solution-SLS. The best partial solution-SS in the

```
Algorithm 4 The calculation of \(C_{\max }\) according to FAFP heuristic
    For batches in seru scheduling, calculate the completion time of batches in each seru \(\left(F C B_{b i}+F C_{b i}\right)\).
    Sort the batches in an ascending order according to the completion time in seru-system \(B^{\prime}=\)
    \(\left\{b_{1}^{\prime}, b_{2}^{\prime}, \ldots, b_{l}^{\prime}, \ldots, b_{k}^{\prime}\right\}\).
    Set \(C_{\max }=F C_{b i}{ }^{\prime}\)
    For \(i=1\) to \(N\)
        If \(F C B_{b i}{ }^{\prime}+F C_{b i}{ }^{\prime}>F L B_{b i-1}{ }^{\prime}+F L_{b i-1}{ }^{\prime}\)
            \(C_{\max }=F C B_{b i}{ }^{\prime}+F C_{b i}{ }^{\prime}+F L_{b i}{ }^{\prime} ;\)
        Else
            \(C_{\max }=C_{\max }+F L_{b i}{ }^{\prime} ;\)
        End if
    End for
```

![img-9.jpeg](img-9.jpeg)

Fig. 11 The cooperation of sub-algorithms
evolution process of seru scheduling population is denoted as the best seru scheduling. Subsequently, the population of hybrid seru formation evolves by SSEA. For evaluating the quality of a partial solution-HSF, the best seru scheduling is used as a partial solution-SS and the partial solution-SLS is
determined by FAFP heuristic. The best partial solution-HSF in the process of evolution is denoted as the best hybrid seru formation. With the mechanism of sharing best individuals shown in Fig. 11, populations coevolve so that the search capability of the integrated algorithm can be enhanced.

However, there may exist a mismatch of seru number in the process of evaluating partial solution-HSFs. To be specific, a partial solution-HSF and the best partial solution-SS cannot form a feasible complete solution when their seru numbers are different. Thus, we design a batch reassignment rule (BRR) to avoid the mismatch between partial solutions for generating legal solutions. To be specific, a batch sequence in the flow line is determined by the FAFP heuristic with the partial solution-SS. According to this batch sequence, batches are assigned to the seru with the earliest completion time. If there are multiple serus with same completion time, select one randomly. The procedure of the BRR is shown in Algorithm 5.

```
Algorithm 5 Procedure of the BRR
Input: a partial solution-SS \(\pi^{\prime}\), the seru num of partial solution-HSF \(J\)
    For batches a partial solution-SS \(\pi^{\prime}\), calculate the completion time in each seru.
    Sort the batches in an ascending order according to the completion time \(B=\left\{b_{1}, b_{2}, \ldots, b_{l}, \ldots, b_{N}\right\}\).
    For \(k=1\) to \(J\)
        \(N_{K}=0, \pi_{K}(0)=0, R_{K}=0\)
    End for
    For \(i=1\) to \(N\)
    \(I=\arg _{N} \min \left\{R_{K}\right\}\)
        \(N_{I}=N_{I}+1\)
        \(\pi_{l}\left(N_{I}\right)=b_{l}\)
        \(R_{I}=R_{I}+F C_{b l}\)
    End for
Output: a partial solution-SS \(\pi\)
```


# The procedure of CCA 

With the above designs, the whole procedure of CCA is shown in Algorithm 6.

```
Algorithm 6 Procedure of the CCA
    Input: An instance with \(M\) batches and \(W\) workers.
        Initialize:
            Randomly generate a partial solution-HSF as the best partial solution-HSF \(P^{\prime}\).
            Randomly generate a partial solution-SS as the best partial solution-SS \(\pi^{\prime}\).
            Randomly generate a complete solution as the best solution \(S^{\prime}\).
        Do
            Evolve the population of hybrid seru formation with \(\pi^{+}\)by SSEA, BRR and FAFP, and update the best
            partial solution-HSF \(P^{\prime}\)
            Evolve the population of seru scheduling with \(P^{\prime}\)
            continue with \(\pi^{+}\)by EDA and FAFP, and update the best partial
            solution-SS \(\pi^{+}\)and the best solution \(S^{\prime}\).
            Until terminal condition is met.
    Output: The best solution \(S^{\prime}\)
```

Table 2 Data of worker's level of skill $\left(B_{m}\right)$
Table 3 Coefficient of influencing level of skill to multiple tasks for workers $\left(\varepsilon_{j}\right)$
Table 4 Data of batches

Table 5 Parameter values

In the initialization phase, a partial solution-HSF, a partial solution-SS, and a complete solution are randomly generated as the best partial solution-HSF $P^{*}$, the best partial solution-SS $\pi^{*}$, and the best solution $S^{*}$.

Then, the population of hybrid seru formation evolves by SSEA (in 3.1). When evaluating each individual in the population, the individual is combined with $\pi^{*}$ and the partial solution-FLS generated by BRR (in 3.4) and FAFP (in 3.3) to form a complete solution. Then, the best partial solutionHSF $P^{*}$ and the best solution $S^{*}$ are updated if necessary.

Next, the population of seru scheduling evolves by EDA (in 3.2). When evaluating each individual in the population, the individual is combined with $P^{*}$ and the partial solutionFLS generated by FAFP (in 3.3) to form a complete solution. Then, the best partial solution-SS $\pi^{*}$ and the best solution $S^{*}$ are updated if necessary.

Due to the information sharing in two populations, they coevolve iteratively until the termination criterion is met.

Table 6 Orthogonal array and ARVs
## Computational results and comparisons

## Experimental settings

Since there are no existing instances on hybrid seru-system, a set of instances are produced by extending the existing line-hybrid seru-system conversion instances [21] as follows. There are five product types, and $T_{n}=1.8, \eta_{i}=10$. The data of $\beta_{n i}, \varepsilon_{i}$ and batches are given in Tables 2, 3 and 4 , respectively, which are expanded on the basis in [21]. For an instance with $W$ workers and $M$ batches, we use
the following data from Tables 2, 3, 4, the first $W$ rows in Table 2, the first $W$ columns in Table 3, and the first $M$ batches in Table 4. Thus, a total of 20 combinations are generated with $M \in\{10,20,30,40,50\}, W \in\{5,10,20$, 30\}. We code the algorithm in C\# and run it on a PC with an Intel Core i5-1035G7 CPU @ 1.2-GHz under Microsoft Windows 10. Consider that different scales of instances need different computation time, we use $0.4 \times M \times W$ s CPU time as the stopping criterion for the CCA in following tests. In the CCA, EDA terminates once it reaches 20 generations and SSEA terminates once the optimal solution remains unchanged for 20 consecutive generations.

## Parameter settings

Clearly, a large value of population size in EDA is helpful for sufficient exploration. However, an overlarge value will result in long convergence time and a small value may lead to insufficient evolution. Besides, an appropriate size of sub-space in SSEA is important to balance the local intensification ability and the running time. According to a large amount of preliminary experiment and investigation, we set the population size of EDA as 50 and the size of sub-space as 10 . In addition to the above parameters, the CCA contains three other key parameters: the rate of elite solutions $\alpha$ and the learning rate $\beta$ in EDA, and the search depth of local search $\gamma$ in SSEA. To investigate the influence of such parameters, the Taguchi method of design-of-experiment (DOE) [42] is implemented. Four factor levels are employed for each parameter as Table 5. An orthogonal array $L_{16}\left(4^{3}\right)$ is chosen to generate the combinations of different values.

A total of 20 instances are used for the investigation. For each instance, the CCA with each combination $t$ is run ten times independently to obtain the average objective value

Fig. 12 Main effect of each parameter
![img-10.jpeg](img-10.jpeg)

Table 7 Comparisons of CCA with CCAnoBRR, SSEAnoLS-EDAFAFP and SSEA-EDAnoLS-FAFP
Note: The best value is indicated in bold
$\bar{C}_{i}$. The best average objective value $\bar{C}_{\text {best }}$ among 16 combinations is used as a reference value. The relative percentage deviation (RPD) of each combination $t$ is calculated as follows:
$\mathrm{RPD}_{t}=\left(\bar{C}_{i}-\bar{C}_{\text {best }}\right) / \bar{C}_{\text {best }} \times 100$.
Thus, the average of $\mathrm{RPD}_{t} \mathrm{~s}$ on 20 instances is obtained as the average response value (ARV) for combination $t$. Clearly, a smaller value of ARV means a better parameter combination. The orthogonal array and the ARVs are listed in Table 6. The main effect of each parameter is shown in Fig. 12.

From the results, it can be seen that the rate of elite solutions $\alpha$ is the most influential parameter, while $\beta$ and $\gamma$ rank the second and the last. A small value of $\alpha$ will result in insufficient learning from elite individuals in each generation, while a larger value will lead to slow convergence. The value of learning rate $\beta$ controls the learning speed of EDA. A large value gains a faster learning speed. However, an overlarge value will lead to a premature convergence. A moderate value of $\gamma$ is beneficial to balance the exploitation intensification and the time consumption. According to above investigation, we choose the following setting for further tests: $\alpha=1.06, \beta=0.15, \gamma=15$.

## Effect of BRR and local search

To demonstrate the effectiveness of the BBR during the iteration of CC mechanism, we compare the CCA (i.e., SSEA-EDA-FAFP) with BRR to the CCA without BRR (CCAnoBRR). The process of CCAnoBRR to solve the mismatch of seru number between partial solution-HSFs and a partial solution-SS is as follows: allocate $s$ th batch processing sequence $(s=1,2, \ldots, N S S)$ to $j$ th seru $(j=(s+N S F$ $1) \% N S F+1)$, where $N S S$ is the seru number of seru scheduling, $N S F$ is the seru number of seru formation, and $\%$ represents the modulus operator. To evaluate the effectiveness of local search during the evolution process of SSEA

Fig. 13 Boxplot of the RPD with or without BRR and local search
![img-11.jpeg](img-11.jpeg)

CC SSEAnoLS-EDA-FAFP SSEA-EDAnoLS-FAFP CCA-noBRR

Table 8 Comparisons between CCA and other algorithms
Note: The best value is indicated in bold
and EDA, we compare the CCA to CCA without local search in SSEA (SSEAnoLS-EDA-FAFP) and CCA without local search in EDA (SSEA-EDAnoLS- FAFP). In SSEAnoLS-EDA-FAFP, if crossover operator 2 fails to achieve improvement, search the next sub-space without applying local search to the best individual in current sub-space. In SSEA-EDAnoLS-FAFP, the elite individuals will be directly used to update the probability model of seru scheduling without further improvement by the local search.

Each instance is run ten times independently to obtain the average objective value $C_{v}$. The best average objective value $C_{b}$ among four algorithms is used as the reference objective value. For each run, the following relative percentage deviation (RPD) of makespan is calculated. The RPD values of different algorithms are shown in Table 7. In addition, Fig. 13 shows the boxplot of all RPD values obtained by the four algorithms.
$\mathrm{RPD}=\left(\bar{C}_{v}-\bar{C}_{b}\right) / \bar{C}_{b} \times 100$

From Table 7, it can be seen that the RPDs obtained by CCA are superior to the other three algorithms on most instances. The CCA is able to obtain the best solutions consistently on 17 out of 20 instances. From Fig. 13, it can be seen that the algorithms with the BRR are much better than that without the BRR. Compared with the

SSEAnoLS-EDA-FAFP and the SSEA-EDAnoLS-FAFP, the results obtained by CCA are better. Besides, the variation of RPD value obtained by CCA is smaller than that of the other algorithms. Therefore, the BRR and local search are effective in achieving better and more robust results.

## Comparisons with other algorithms

According to the results in [11-13, 15-17], GA is of good performance in dealing with different scheduling problems in pure seru-system. To test the performance of CCA (i.e., SSEA-EDA-FAFP), the existing genetic algorithm for pure seru-system is employed for comparison. To be specific, the recent GA in [15] is adopted for seru formation. Thus, we construct two algorithms with CC mechanism, i.e., GA-EDA-FAFP and GA-GA-FAFP. To be specific, in GA-EDAFAFP, the GA with local search in [15] is used to evolve the population of hybrid seru formation, and the remaining settings are the same as CCA. In GA-GA-FAFP, a GA with local search is developed to evolve the population of seru scheduling. The representation of seru scheduling and the local search are the same as those in 3.2.1, and the evolution process includes tournament selection, order crossover [43] and mutation by swapping two gene positions. The rest settings of GA-GA-FAFP are the same as GA-EDA-FAFP. Similarly, we run each algorithm ten times independently on each instance and record the best solution as the final

solution. The following Imp is used to measure the improvement by a certain algorithm after dismantling the original flow line into the hybrid seru-system.
$\operatorname{Imp}=\left(C_{A}^{*}-C^{*}\right) / C_{A}^{*} \times 100$
where $C^{*}$ denotes the makespan of the hybrid seru-system obtained by an algorithm, and $C_{A}^{*}$ denotes the makespan of the original flow line, which is calculated based on Eq. (6).

Clearly, a larger value of Imp means a better performance achieved by the algorithm. The results of different algorithms are given in Table 8. It can be seen that the CCA obtains the best solutions among three algorithms on 15 out of 20 instances, while GA-EDA-FAFP obtains best objective values only on 8 instances. Comparatively, the improvement by GA-GA-FAFP is the worst among all. Therefore, it is concluded that CCA has a better performance than other algorithms in solving the HSSOP.

## Conclusion

This paper addresses a complex hybrid seru-system scheduling problem with the makespan minimization criterion, which contains several strongly coupled decision-making processes. The problem is decomposed in three sub-problems: hybrid seru formation, seru scheduling and flow line scheduling. For each sub-problem, suitable optimization algorithm is designed according to the characteristics of the sub-problems, and different local search procedures are designed for different sub-problems to enhance exploitation. The sub-algorithms work in an integrated framework with a cooperative coevolution mechanism to explore good solutions and a batch reassign rule to guarantee legal solutions. Extensive comparisons show that the designed local search and batch reassign rule are effective. It also shows that the proposed algorithm is superior to the existing algorithms for seru-system scheduling problem.

The future work will focus on the adaptive cooperative optimization of different sub-problems. Learning-based mechanism will be considered in designing more powerful solution algorithms. It is also interesting to generalize the work to the multi-objective optimization of hybrid serusystem by considering total tardiness, labor time, and energy consumption [44].

Acknowledgement This study is supported by the National Science Fund for Distinguished Young Scholars of China (No. 61525304) and the National Natural Science Foundation ofChina (No. 61873328).

## Declarations

Conflict of interest The authors declare that we have no conflict of interest.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
