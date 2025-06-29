# An Estimation of Distribution Algorithm-Based Hyper-Heuristic for the Distributed Assembly Mixed No-Idle Permutation Flowshop Scheduling Problem 

Fuqing Zhao ${ }^{\oplus}$, Bo Zhu, and Ling Wang ${ }^{\ominus}$, Member, IEEE


#### Abstract

The distributed assembly mixed no-idle permutation flowshop scheduling problem (DAMNIPFSP), a common occurrence in modern industries like integrated circuit production, ceramic frit production, fiberglass processing, and steel-making, is a new model that considers mixed machines with noidle restrictions as well as conventional machines. This article introduces an estimation of distribution algorithm-based hyperheuristic (EDA-HH) to solve the DAMNIPFSP. Ten simple heuristic rules as low-level operations are utilized to search the solution space. The estimation of distribution algorithm is integrated into the framework of hyper-heuristic as the high-level strategy to control the low-level heuristics sequence in the solution space. The destruction and construction procedures are conducted on products and jobs in order to enhance the exploitation competence of EDA-HH. The computational simulation is carried out and the experimental results show that the proposed EDAHH is significantly superior to the competitors in the statistical sense. The results of the $\mathbf{8 1 0}$ large-scale problem instances show the effectiveness of the EDA-HH in solving the DAMNIPFSP. Moreover, the CPLEX solver is utilized to verify the correctness of the model with some small instances.


Index Terms-Distributed assembly scheduling, estimation of distribution, hyper-heuristic, mixed no-idle flowshop.

## I. INTRODUCTION

SCHEDULING is an extremely important topic in manufacturing systems [1], [2]. A robust scheduling scheme may increase the efficacy and efficiency of industrial processes. Besides, an effective optimization algorithm for scheduling problems is a crucial method to enhance the efficiency of manufacturing processing. Under the background

[^0]of market competition and economic globalization, the application of distributed manufacturing and distributed assembly system is an irreversible trend [3]. The collaborative production is inevitable and important for the manufacturing industry enterprise considering the technical and economic factors [4]. Therefore, it is significantly important to study the optimization method for the scheduling problem under the distributed environment.

The distributed scheduling arises under the background of globalization. Distributed shop scheduling problems can be classified into the following categories: distributed parallel machine scheduling [5], distributed flow shop scheduling [6], [7], distributed job shop scheduling [8], distributed hybrid flow shop scheduling [9], [10], and distributed flexible job shop scheduling [11]. The distributed flow shop scheduling problem (DFSP) is a hot topic that attracted much attention from researchers.

The distributed manufacturing systems overcome the drawbacks of traditional production in a single factory [12], and performed with an advantage in product quality, production cost, and risk management [13], [14]. However, these advantages come along with the much higher scheduling difficulty in the distributed manufacturing environment. In the distributed manufacturing system, solutions must be discovered for two coupling problems, i.e., assignment of the jobs to the factories and the job sequence in the factories. The distributed permutation flowshop scheduling problem (DPFSP) is already an NP-hard problem according to the conclusion of [15].

The distributed assembly flowshop scheduling problem (DAFSP) exists in many manufacturing systems. Since the pioneering work of Hatami et al. [16], many DAFSP-related works have been published. Wang and Wang [17] first proposed an estimation of distribution algorithm (EDA)-based algorithm for the distributed assembly permutation flowshop scheduling problem (DAPFSP). Hatami et al. [18] investigated the DAPFSP under the constraint of sequence-dependent setup times (DAPFSP-SDST). Two constructive heuristics, a metaheuristic based on variable neighborhood decent, and a simplified iterated greedy algorithm have been developed for DAPFSP-SDST. In [19], the backtracking search is introduced as the control strategy under the framework of the hyperheuristic. The effectiveness of the algorithm was verified on the DAPFSP. Sang et al. [20] first considered the total flowtime in the DAPFSP. A cooperative water wave optimization (WWO) is presented by Zhao et al. [21] for addressing the


[^0]:    Manuscript received 26 December 2022; accepted 27 April 2023. Date of publication 17 May 2023; date of current version 18 August 2023. This work was supported in part by the National Natural Science Foundation of China under Grant 62063021 and Grant 62273193; in part by the High-Level Foreign Experts Project of Gansu Province under Grant 22JR10KA007; in part by the Key Research Programs of Science and Technology Commission Foundation of Gansu Province under Grant 21YF5WA086; in part by the Lanzhou Science Bureau Project under Grant 2018-rc-98; and in part by the Project of Gansu Natural Science Foundation under Grant 21JR7RA204. This article was recommended by Associate Editor D. O. Olson. (Corresponding authors: Fuqing Zhao; Ling Wang.)

    Fuqing Zhao and Bo Zhu are with the School of Computer and Communication Technology, Lanzhou University of Technology, Lanzhou 730050, China (e-mail: zhaofq@lut.edu.cn; 1532116227@qq.com).

    Ling Wang is with the Department of Automation, Tsinghua University, Beijing 100084, China (e-mail: wangling@tsinghua.edu.cn).

    This article has supplementary material provided by the authors and color versions of one or more figures available at https://doi.org/ 10.1109/TSMC.2023.3272311.

    Digital Object Identifier 10.1109/TSMC. 2023.3272311

distributed assembly no-idle flowshop scheduling problem (DANIFSP). Zhang et al. [22] proposed a matrix cubebased EDA for the energy-efficient DAPFSP (EEDAPFSP). Huang et al. [23] presented a two-phase evolution algorithm for the multiobjective DAPFSP.

Pan and Ruiz [24] proposed the mixed no-idle permutation flowshop scheduling problem (MNIPFSP), which is more conform to the realistic scenario than the conventional NIPFSP. Rossi and Nagano [29] built the mathematical model for MNIPFSP and proposed an acceleration method for calculating the insertions. To address the MNIPFSP, the authors designed an effective iterated greedy algorithm and the computational results on a total of 1750 instances show the superiority of the algorithm. Recently, Rossi and Nagano [25], [26], [27] conducted the research on this topic further, including introducing the setup times on regular machines in MNIPFSP. The distributed mixed no-idle flowshop (DMNIFSP) was first studied in [28]. The authors introduced the cloud theory-based temperature reduction acceptance criterion in the iterated greedy method (CTBIG) to enhance the search capability of the algorithm. Compared with the classical iterated greedy algorithm, the CTBIG performed better on the test instances. Rossi and Nagano [29] first attempted to consider the setup times in the DMNIPFSP and they enhanced the quality of the solutions through the newly designed reconstruction strategy.

This article aims to find a promising result for the distributed assembly MNIPFSP (DAMNIPFSP). As a generalization of DANIFSP, the work related to the DAMNIPFSP is very limited. The DAMNIPFSP has strong constraint conditions. First of all, the operation on the job sequence needs to avoid randomness to satisfy the assembly condition of products. Second, the mixed no-idle constraint makes it more difficult to solve the problem than the permutation constraint or no-idle constraint. Finally, the distributed factory makes the problem become difficult. The DAMNIPFSP combines the DMNIPFSP [28] with assembly systems. There are three subproblems to consider: factory assignment, product scheduling, and job scheduling.

The difference between the DANIFSP and DMNIPFSP is that the DAMNIPFSP considers the mixed no-idle restriction, which is more conformed to a real production scenario than the DANIFSP. In practice, the start times of jobs must be delayed to satisfy the no-idle constraint in some industries. Due to the reason of technique and economics, it is unfeasible to stop a machine between jobs. However, the assumption of all the machines in a factory are no-idle machines is unreasonable. Therefore, it is worth researching the model that is close to the practice. In fact, real production scenarios existed at present, such as integrated circuit production, ceramic frit production, fiberglass processing, steel making industry, and the production of truck engine blocks in a foundry [24], [30], [31], [32] are worth to be considered deeply. In these production scenarios, only some machines are very expensive, and it is necessary to avoid idling at all costs. As aforementioned, the DAMNIPFSP is likewise NP-hard when $n>f$.

In this article, inspired by the learning mechanism of EDA and versatility of hyper-heuristic, an EDA algorithm-based hyper-heuristic (EDA-HH) for the DAMNIPFSP is proposed. The EDA algorithm is integrated into the framework of

TABLE I
REVIEW OF WORLS FOR THE DISTRIBUTED ASSEMBLY SCHEDULING

hyper-heuristic as the control strategy. The knowledge of the problem is utilized implicitly by the way of building a probability model rather than the explicit representation of knowledge. The low-level heuristics play a critical role in the algorithm because they are applied to the solution space directly. In order to enhance the exploitation of the proposed EDA-HH, the destruction and construction are applied in the hyper-heuristic scheme. The main contributions are summarized below.

1) The EDA is utilized as a high-level heuristic for solving the DAMNIPFSP.
2) A group heuristics rules are developed to explore the solution space. The simulated annealing (SA) operator is introduced to enhance the fine search capability.
3) A probability updating mechanism is developed for EDA-HH to achieve incremental learning.
The remainder of this article is structured as follows: Section II provides a systematic review of the related works. In Section III, the mathematical model of DAMNIPFSP is established and the numerical illustration is provided in the supplementary materials. Section IV presents a detail of the proposed EDA-HH. In Section V, a comprehensive evaluation is conducted on the proposed algorithm through comparative experiments and statistical analysis. The conclusion of this article and some interesting directions are discussed in Section VI.

## II. Related Work

The DAFSP is evolved from the DFSP (i.e., there is not only the distributed factory constraint but also the assembly constraint). In recent years, the related works about the DAFSP are mainly focused on the DAPFSP and the makespan objective. Table I provides a review of the DAFSP, which

contains mathematical models, optimization objectives, and solving methods. Note that the last line of the table is the research contents of this article.

Many methods have been developed for the DAPFSP with the objective of makespan criterion. The details of these works are presented in [16], [17], [19], [37], [38], [39], [40], [41], and [42]. Besides, Yang et al. [33] proposed a memetic algorithm, which combined with the scatter search, for the DAPFSP with the objective of total tardiness. Huang et al. [34] considered the total flowtime in the DAPFSP. Zhao et al. [2] considered the blocking constraint and total tardiness criterion in the DAFSP model. The knowledge of the problem was utilized in the enhanced WWO to balance the exploration and exploitation. Each individual in the population selects search strategy adaptively to obtain a promising solution. Yang and Li [35] presented a knowledge-driven constructive heuristic for the DABFSP with the makespan criterion. Shao et al. [36] considered the no-idle constraint in the DPFSP. The ILS and VNS are adopted in their research. Additionally, the assignment rule $\mathrm{NR}_{a}$ is first proposed for the constructive heuristic. In [43], a backtracking search algorithm (BSA)based method is proposed to solve the DANWFSP with the makespan criterion.

The DAPFSP-SDST is a more realistic model than the classical DAPFSP. Hatami et al. [18] and Song and Lin [44] considered the DAPFSP-SDST with the makespan criterion. The DAPFSP with multiobjectives is investigated in [22] and [23]. From Table I, although the DAMNIPFSP exists in many manufacturing scenarios, the research about DAMNIPFSP is very limited.

The EDA is a novel and potential meta-heuristic. The way of generating the offspring is different from the other evolution algorithms [45], which produce a new population through the crossover and mutation operators [46]. The most important module of the EDA is the probability model, which is constructed through superior individuals. The information implicit in the probability model assists to obtain a promising population for the next iteration [40], [47]. Various algorithms based on the mechanism of EDA have been developed for shop scheduling problems [17], [48], [49], [50], [51], [52], [53]. From the previous literature, it is noteworthy that the EDA is promising for solving the shop scheduling problem, however, the computational and statistical results show that the CPU time spent by the EDA is larger than the other compared algorithms several or hundreds of times. The reason is that the population size used in the EDA usually larger than the other meta-heuristics and the EDA manipulates the jobs directly in the shop scheduling problems. In our study, the EDA is integrated into the framework of the hyper-heuristic to address the DAMNIPFSP.

The hyper-heuristic is a promising research topic, which is an approach that boosts the versatility of the search algorithm [54], [55]. However, the related research on the hyperheuristic for solving the flowshop scheduling problem is very limited. In [54], the SA was integrated into the framework of the hyper-heuristic to solve the job shop scheduling problems. The SA is adopted to train the low-level heuristic to

TABLE II
Notation Used in the Model


solve the instances. The test results exhibit the superior of the suggested algorithm. In [56], the PSO is brought into the hyper-heuristic and the PSO is utilized to optimize the parameters for dispatching rules. Song and Lin [44] considered a combination of genetic programming and the hyper-heuristic (GP-HH) to address the DAPFSP. In each generation of the evolution, GP can make the low-level heuristic search in a promising direction. The review and analysis mentioned above inspired our work.

## III. Problem Definition and Model

## A. Notation Definition

The notations used in the model of DAMNIPFSP are listed in Table II.

The mathematical model of DAMNIPFSP is extended from the DAPFSP [16] and MNIPFSP [24]. The model of DAMNIPFSP is more conformed to a practical production scenario than the previous models.

## B. Problem Definition

As aforementioned, the DAMNIPFSP is a generalization of the DANIPFSP, which is assumed that all of the machines in a factory have a no-idle constraint. The production and assembly stages are essential procedures of the DAMNIPFSP. There are three subproblems that need to be considered: 1) factory assignment; 2) product scheduling; and 3) job scheduling. The DAMNIPFSP under consideration in this article meets the following key assumptions.

1) There is more than one flowshop factory. All factories are mixed no-idle flow shops. There are $n$ independent jobs processed on $m$ machines based on the same workflows and $n, m$, and $F$ are known.
2) The processing capacity of each flowshop is known in advance and the flowshops are isomorphism.
3) Initially, all jobs are available. To meet the no-idle restriction, some jobs must be delayed in their execution. During the procedure, jobs cannot be moved to other factories.
4) Each machine can process only one job at a time and each job can be processed by only one machine at a time. The processing procedure cannot be broken off since it starts.
5) The setup time, which is sequence-independent, is neglected or included in the processing time of each job.
6) There are no breakdowns and each machine is always available.
7) During the first stage, the type of the machines is a combination of the no-idle and normal machines.
8) The assembly process begins only after all the jobs of a product have been performed in the production stage.
The illustration of the DAMNIPFSP is shown in Fig. 10 of the supplementary material.
The mixed-integer linear programming model for DAMNIPFSP is formulated as follows:

$$
\begin{aligned}
& \text { Minimize } C_{\max } \\
& \text { Subject to } \\
& \sum_{k=1}^{n} \sum_{f=1}^{F} X_{j, k, f}=1 \forall j \\
& \sum_{j=1}^{n} \sum_{f=1}^{F} X_{j, k, f} \leq 1 \forall k \\
& C_{i, k, f} \geq \sum_{j=1}^{n} X_{j, k, f} \cdot P_{i, j} \forall f, i=1, k=1 \\
& C_{i, k, f} \geq C_{i-1, k, f}+\sum_{j=1}^{n} X_{j, k, f} \cdot P_{i, j} \forall f, k, i \in\{2,3, \ldots, m\} \\
& C_{i, k, f} \geq C_{i, k-1, f}+\sum_{j=1}^{n} X_{j, k, f} \cdot P_{i, j} \forall f \\
& k \in\{2,3, \ldots, n\}, i \in M-M^{\prime} \\
& C_{i, k, f}=C_{i, k-1, f}+\sum_{j=1}^{n} X_{j, k, f} \cdot P_{i, j} \forall f \\
& k \in\{2,3, \ldots, n\}, i \in M^{\prime}
\end{aligned}
$$

$\sum_{l=0}^{h} Y_{l, s}=1 \forall s$
$\sum_{s=0}^{h} Y_{l, s} \leq 1 \forall l$
$\mathrm{CA}_{s} \geq C_{m, j}+p p_{s}-\left(1-G_{j, s}\right) \cdot L \forall j, s$
$C_{k} \geq \mathrm{CA}_{l}-\left(1-Y_{l, k}\right) \cdot L \forall l, k$
$C_{k} \geq C_{k-1}+p p_{l}-\left(1-Y_{l, k}\right) \cdot L \forall l, k>1$
$C_{\max } \geq C_{k} \forall k$
$C_{i, k, f} \geq 0 \forall i, k, f$
$\mathrm{CA}_{s} \geq 0 \forall s$
$X_{j, k, f} \in\{0,1\} \forall j, k, f$
$Y_{l, s} \in\{0,1\} \forall l, s, l \neq s$
$G_{j, s} \in\{0,1\} \forall j, s$.
Equation (1) indicates the optimization objective of the problem. Constraint (2) defines that a job can not appear at more than one factory at the same time. Constraint (3) clarifies that a job can appear at only one position in a certain factory. Constraints (4) and (5) assure that job $j$ processing in the current machine cannot begin until job $j$ processing in the preceding machine is completed. On regular machines, the completion time relationship between adjacent jobs satisfies the constraint (6). Constraint set (7) specifies that the completion time of a job at an idle machine is equal to its processing time plus the completion time of the preceding job in the permutation. Constraints (8) and (9) ensure that each product in the assembly procedure has just one predecessor and no more than one following product. The product assembly satisfies the constraint set (10), which stipulates the assembly stage only starts after the production stage is finished. Constraint (11) defines the completion time of jobs on the assembly line. Constraint (12) stipulates the sequential relationship of the products. Constraint (13) defines the makespan (i.e., the maximum completion time) refers to the completion time of the last product on the machine of the assembly stage. It is obvious that minimizing the makespan can reduce the total production run and save production resources [16], [57]. Constraints (14)-(18) indicate the domain of the decision variables. The CPLEX solver is adopted to verify the mathematical model and the details can be seen in the supplementary material.

## IV. Estimation of Distribution Algorithm-Based HyPER-Heuristic

The first published research that applied EDA for DPFSP is presented by Wang et al. [51]. They developed a memetic algorithm that embedded the EDA, which possesses an extended sampling mechanism, to address the DAPFSP [17]. In contrast to sophisticated algorithms that contain problem-specific knowledge, the EDA's key characteristic is its evolutionary mechanism based on a probability model.

The EDA is made up of a few phases. First, the initial population is created by using a uniform distribution. Then the truncated selection approach is employed on the population to select superior individuals according to the fitness values.

## Algorithm 1: Procedure of EDA-HH

1 Inputs: The population size $p s$, the annealing rate $\xi$, the truncation rate $\tau$, the destruction length of products $d$, the destruction length of jobs $d j$;
2 Initialize the population randomly and assign a random low-level heuristic sequence for each individual; Initialization the probability matrix $P$;
3 Apply the improved LLHs successively to each individual;
4 Calculate $C_{\max }$ of individuals;
5 While the terminal condition is not met do
6 Generate the superior population by truncation selection;
7 Calculate the cumulative probability;
8 Generate the next generation of low-level heuristic sequences by the roulette wheel selection for individuals;
9 Update the probability matrix through the incremental learning method;
10 Apply the improved LLHs successively to each individual;
11 Calculate $C_{\max }$ of individuals;
12 Perform the destruction and construction to the best solution obtained currently; Retain the best result and solution;
13 End while
14 Output: The best result and scheduling solution.

The probability model can be established by the statistical magnitude of the selected superior individuals. Following the completion of the modeling, a collection of individuals is drawn from the generated model.

To solve the DAMNIPFSP, the EDA-HH is proposed in this part. The EDA-HH framework is presented initially, followed by the solution representation and initialization, lowlevel heuristics, destruction and construction, and updating mechanism.

## A. Framework of the EDA-HH

This section describes the details of the framework of the proposed algorithm. The execution procedure of the EDAHH is illustrated in Fig. 16 (supplementary materials). The pseudocode of EDA-HH is presented in Algorithm 1.

The estimation of distribution method is used as a highlevel heuristic technique in the EDA-HH to manipulate the low-level heuristics. The low-level heuristics are responsible for the fine search in the solution space, whereas EDA is used to search the solution space indirectly by regulating the lowlevel heuristics. The primary technique of the EDA-HH is as follows.

1) The starting population is formed at random, with each heuristic appearing only once in each individual.
2) To identify a solution, each low-level heuristic is applied sequentially to the solution space. The best solution evolved by low-level heuristics sequence is utilized to
![img-0.jpeg](img-0.jpeg)

Fig. 1. Encoding scheme.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Decoding scheme.
evaluate each individual, and the solution is decoded to obtain a workable schedule to calculate the objective.
3) By sorting individuals and employing truncation selection, the superior subpopulation is obtained. The information from the superior low-level heuristic sequence is used to build the probability model, and the next generation is obtained by sampling the probability model.
4) The destruction and construction phases are applied to the best solution provided by the preceding step to obtain a more promising neighborhood solution.

## B. Solution Encoding and Decoding Schemes

In the design of an optimization algorithm, the representation of a solution is critical. The individual of EDA-HH is comprised of a solution and the low-level heuristics sequence. The low-level heuristics are employed on the individuals to evolve at each iteration. For solving the DAMNIPFSP, the two-level representation is adopted in this article. Note that the jobs for the same product are intended to be tightly linked during the two stage. An example is provided in Fig. 1 to illustrate the diagram of the solution encoding scheme.

To decide the assignment of tasks to factories, an effective decoding rule is known as $\mathrm{NR}_{2}$ [16] is used. A job $j$ is assigned to the factory which has the lowest $C_{\max }$ after including job $j$. The diagram of the solution decoding scheme is presented in Fig. 2. The job sequence can then be decoded to a workable schedule, and the completion time is computed.

## C. Probability Model and Updating Mechanism

The distinction between EDA and other evolutionary algorithms is that EDA generates the next generation using a probability model [58]. The probability model in this study

is built as a probability matrix $P$ to obtain the information inherent in the low-level heuristics sequence.
The element of the probability matrix, $p_{i, j}^{g}$, indicates the probability that a low-level heuristic $j$ appears before or in position $i$ at generation $g$. The value of $p_{i, j}^{g}$ denotes the significance of a low-level heuristic in determining the sequence of low-level heuristics. For all $i$ and $j$ values, $p_{i, j}^{0}$ is set to $1 / \theta$, implying that the entire low-level heuristics space can be sampled equally. $\theta$ is the total number of low-level heuristics.
New individuals are generated in each generation of the EDA-HH by sampling the low-level heuristics space based on the probability matrix. For each position $i$ a low-level heuristic $j$ is chosen with the probability $p_{i, j}$. If a low-level heuristic $j$ appears, it signifies that the low-level heuristic $j$ has previously been used. The $j$ th column of the probability matrix $P$ is then set to zero, and all elements of $P$ are normalized so that each row sums to 1 . A low-level heuristic sequence is built until all of the low-level heuristics are available.
In addition, the probability updating mechanism is developed in this study to achieve incremental learning. The probability matrix $P$ is updated according to the following formula:

$$
\begin{aligned}
p_{i, j}^{g+1} & =(1-\alpha) p_{i, j}^{g}+\alpha\left(\sum_{k=1}^{p s} p_{i, j}^{k} / i \times p s^{\prime}\right) \forall i, j \\
I_{i, j}^{k} & =\left\{\begin{array}{l}
1, \text { if LLH appears before or in position } i \\
0, \text { otherwise }
\end{array}\right.
\end{aligned}
$$

where $\alpha \epsilon(0,1)$ is the learning rate, which is set to 0.5 in this article. $p s^{\prime}$ signifies the number of individuals of the superior population. The procedure for updating the probability matrix is illustrated in Fig. 15 (supplementary materials).
Different from the other evolutionary algorithm that iteratively maintains the building block through crossover and mutation procedures, the probability model of EDA can catch the structural characteristic of the problem and evolve the next generation by implicitly utilizing the information from the superior population. In this article, the probability model is utilized in the policy space instead of the solution space. This statistic-learning mechanism is employed to learn promising policies rather than operate the job sequence.

## D. Low-Level Heuristics

Low-level heuristics are commonly accepted as an essential component of a hyper-heuristic. To a considerable extent, whether a hyper-heuristic can obtain a promising result is dependent on the search capability of the low-level heuristics [59]. In this section, ten low-level heuristics are devised to build the collection of LLHs, which are described in detail below.

1) Select two distinct products randomly and exchange their positions. The relative positions between jobs belonging to the same product will keep unchanged.
2) Select two distinct products randomly and put the former after the latter. The relative positions between jobs belonging to the same product will keep unchanged.

## Algorithm 2: LLH

1 The initial temperature is set to $T_{0}$
$2 \pi=\varphi$
3 The LLH is applied on $\pi$ to generate $\pi^{\prime}$
4 While $T_{0}>T_{f}$
5 The LLH is applied on $\pi^{\prime}$ to generate $\pi^{\prime \prime}$
6 If $\Delta T<0\left(\Delta T=C_{\max }\left(\pi^{\prime \prime}\right)-C_{\max }\left(\pi^{\prime}\right)\right)$ then
$T_{0} \pi^{\prime}=\pi^{\prime \prime}$
Else
If $\operatorname{rand}(0,1)<\exp \left(-\Delta T / T_{0}\right)$ then
$10 \pi^{\prime}=\pi^{\prime \prime}$
End if
End if
$T_{0}=\xi \times T_{0}$
End while
If $C_{\max }\left(\pi^{\prime}\right)<C_{\max }(\varphi)$ then
$\varphi=\pi^{\prime}$
End if
10 return $\varphi$
3) Select two distinct products randomly and put the latter before the former. The relative positions between jobs belonging to the same product will keep unchanged.
4) Select two positions randomly in product permutation and place the products between the two positions in reverse order. The relative positions between jobs belonging to the same product will keep unchanged.
5) Select two adjacent positions randomly in product permutation and swap the corresponding products. The first and last positions in a permutation are regarded as the adjacent positions. The relative positions will maintain between jobs belonging to the same product.
6) Select a product from the permutation and select two distinct job positions of the product. Swap the corresponding jobs.
7) Select a product randomly from the permutation and select two distinct job positions of the product. Put the latter job before the former job.
8) Select a product randomly from the permutation and select two distinct job positions of the product. Put the former job after the latter job.
9) Select a product randomly from the permutation and select two distinct job positions of the product. Place the jobs between the two positions in reverse order.
10) Select a product randomly from the permutation and select two adjacent job positions of the product. Swap the corresponding jobs.
Before conducting job-related LLHs, a product is randomly picked to ensure that jobs belonging to the same product are not split after the LLHs. Furthermore, SA is included in each LLH to improve the performance of the fine search. The improved LLH is executed according to Algorithm 2. The product or job sequence that needs to be processed is denoted by $\varphi . \xi$ is the annealing rate. The beginning temperature is presented by $T_{o}$ and the terminal temperature is presented by $T_{f}$.

## E. Destruction and Construction Phases

This effective mechanism is introduced into our research. The related works published at present illustrate the significance of destruction and construction phases for every IG algorithm [31], [60], [61]. There are two types of destruction for the solution of the DAMNIPFSP, i.e., the destruction and construction of jobs and products. The destruction length for products and jobs are denoted by $d$ and $d j$, respectively. The removed products and jobs must then be reinserted to create a complete product permutation and job sequence. Jobs from the same product are not divided to minimize assembly completion time delays. Jobs pertaining to the same product are designated in the same color, as shown in Figs. 12 and 13 of the supplementary material.

In this article, the elitism strategy is adopted in the destruction and reconstruction phase. The destruction and reconstruction are only performed on the current best solution. On the one hand, this strategy can improve the current optimum, and save computational resources on the other hand.

## V. COMPUTATIONAL RESULTS

## A. Experimental Setup

In this section, the computational simulation is implemented to test the performance of the EDA-HH. At present, there is no standard DAMNIPFSP test set. The test set generated by ourselves can be download at https://pait.baidu.com/s/1hD1FgcWcDzMiCbWuzNVkrA?pwd $=1 \mathrm{wg} 0$. The large-scale benchmark instances are utilized in our experiments. There are 810 large-scale instances which is the combinations of $n \in\{100,200,500\}, m \in\{5,10,20\}$, $f \in\{4,6,8\}$, and $t \in\{30,40,50\}$. Where the number of jobs, machines, factories, and products are indicated by $n, m$, $f$, and $t$, respectively. In our study, seven combinations of machine constraints with different proportions as suggested by Pan and Ruiz [24] were used to test algorithms. The last group set, setting all the machines are no-idle machines, is excluded from our experiments. The CPU time is adopted as the stopping criterion in experiments. The max CPU time is set to $T=c \times m \times n$ milliseconds, where $c=\{20,40,60\}$. Five state-of-the-art algorithms are utilized to compare with the proposed EDA-HH on the benchmark test suite. All experiments are implemented by using Java (jdk12.0.2) language in IntelliJ IDEA. To evaluate the performance of the proposed EDA-HH and other comparison algorithms, experimental results are evaluated by the average relative percentage deviation (ARPD) as follows:

$$
A R P D=\frac{1}{R} \sum_{i=1}^{R} \frac{\mathrm{Cmax}_{i}-\mathrm{Cmax}_{*}}{\mathrm{Cmax}_{*}} \times 100 \%
$$

where $R$ is the execution times of each algorithm. The result of $i$ th run is denoted by $\mathrm{Cmax}_{i}$ and $\mathrm{Cmax}_{*}$ indicates the best result obtained currently.

## B. Parameter Calibration

This section calibrates the parameter of the EDA-HH to perform at its best performance. The critical parameters of
![img-2.jpeg](img-2.jpeg)

Fig. 3. Parameter analysis for the EDA-HH.
EDA-HH include the population size ( $p s$ ), truncation rate $\tau$, annealing rate $\xi, d$, and $d j$. Various values for each parameter are as follows: $p s=\{5,10,15,20\}, \tau=$ $\{0.2,0.3,0.4,0.5\}, \xi=\{0.6,0.7,0.8,0.9\}, d=\{2,3,4,5\}$, and $d j=\{5,6,7,8,9\}$. Therefore, there are $4 \times 4 \times 4 \times 4 \times$ $5=1280$ combinations of parameters. There are 81 instances selected based on various combinations from the benchmark for this experiment. The proposed algorithm with a different combination of parameters is executed five times.

The design of the experiment (DOE) [62] is implemented to investigate the influence of the control parameters on the proposed EDA-HH. The analysis of variance (ANOVA) is employed to analyze the experimental results. The results of ANOVA are presented in Table X (supplementary materials). As can be seen in Table X, the pvalue of the four parameters reflect that all the four parameters are significantly affect the experimental results. From Table X, there exist interaction effects among some parameters. The main effects plot is shown in Fig. 3 and the interaction plots for parameters are shown in Fig. 14 (supplementary materials).

From Fig. 3, it can be seen that $p s$ has a significant impact on the test instances and the best results can be obtained when the $p s$ is set to 15 . The setting of $p s$ needs to tradeoff the diversity of the population and the computation resources. As can be seen in Fig. 3, a greater value of $\xi$ leads to a lower ARPD. A large $\xi$, on the other hand, will result in a significant computational cost. The truncation rate $\tau$ determines the proportion of the superior individuals comprises in the population. The results show that EDA-HH can obtain more promising results than the other settings when $\tau$ equals 0.3 . The setting of $\tau$ needs to consider trading off the diversity of the population and search efficiency. The small value of $\tau$ can ensure the quality of the selected individuals but lost the diversity and vice versa. To avoid the loss of accuracy of the probability model, the setting of $t$ is usually smaller than 0.5 . The interaction plots show that the EDA-HH performed well when the parameters setting of $p s, \xi, d$, and $d j$ are $15,0.8,4$, and 6 , respectively. Through the above analysis, the parameters setting are suggested as follows: $p s=15, \xi=0.8, \tau=0.3$, $d=4$, and $d j=6 . T_{0}$ and $T_{f}$ are set to 2 and 1 , respectively.

## C. Comparative Experimental Analysis

In this part, the suggested EDA-HH is compared against the algorithms for the DAPFAP from the literature. We choose the best-competing algorithms from the DAPFSP literature

TABLE III
PARAMETER CONFIGURATION OF OTHER ALGORITHMS

![img-6.jpeg](img-6.jpeg)

Fig. 4. Interval plot of EDA-HH and competitors.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Box plot of the algorithms.
because there is just one DAMNIPFSP approach proposed so far. The techniques listed below have been completely reimplemented: RIG [1], BS-HH [19], TDIWO [20], HDIWO [20], and HDIWOp [20]. We rigorously reimplement the above algorithms based on the original paper. The parameter configuration of these algorithms, which is listed in Table III, is taken from the original literature to ensure the optimal performance of the algorithm. All algorithms are executed five times under the same CUP time $T=c \times m \times n$. The ARPD values of the six algorithms on the large-scale instances are listed in Table IX (supplementary materials). The results are grouped based on $n, m, f$, and $t$. Table IX shows that the proposed EDA-HH performed best on large-scale instances.

From Fig. 4 and Fig. 19 (supplementary materials), the proposed EDA-HH has the advantage compared with other algorithms. The box plots of these algorithms are shown in Fig. 5 and Fig. 20 (supplementary materials). From the smallest interquartile range (IQR) and compact outliers of EDA-HH, the EDA-HH has small fluctuation and strong stability. Based on the comprehensive analysis, the proposed EDA-HH performed better than the other competitors in terms of efficiency and stability.
![img-5.jpeg](img-5.jpeg)

Fig. 6. ARPD versus ACPU of compared algorithms on benchmark instances.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Friedman test results on $c=20$.
Furthermore, the average CPU (ACPU) running time on the instances with 100 jobs is given in Table IV. Note that each algorithm is executed for five epochs for each instance to compute the ACPU. From Table IV, the ARPD of the proposed EDA-HH is the smallest by comparison. For ACPU, the HDIWO performs best on large-scale instances. The ACPU results of the proposed EDA-HH are slightly inferior to the HDIWO. Although the proposed EDA-HH consumes more computational effort, it is acceptable due to the obtained scheduling solutions with high quality. As shown in Fig. 6, the proposed EDA-HH can maintain the balance of the ARPD and ACPU, and can perform competitively on time effort. The ACPU time is defined as follows:

$$
A C P U_{j}=\left(\sum C P U_{i, j}\right) / I
$$

where $I$ is the number of instances and $\mathrm{CPU}_{i, j}$ denotes CPU time (in seconds) that algorithm $j$ consumes in instance $i$.

## D. Nonparametric Test

In this section, two nonparametric tests are adopted to evaluate the performance of the proposed EDA-HH and the experimental results are statistically analyzed to understand the difference among comparison algorithms.

The Friedman results of the compared algorithms are shown in Table V. The average ranking of the proposed EDA-HH is smaller than the other competitors. The results illustrated that the proposed EDA-HH performed with an advantage in the comparison of the competitors on large-scale instances and show that the differences are significant in the statistical sense. Fig. 7 and Fig. 18 (supplementary materials) exhibit the visualized statistical test results. Note that Bonferroni-Dunn's method is employed as a post hoc procedure to calculate the

TABLE IV
ARPD Versus ACPU Results of COMPARED Algorithms


TABLE V
Friedman-Test Results


TABLE VI
Wilcoxon ReSults OF THE AlGorithms

critical difference (CD) as show in (23). In (23), $k$ is the number of comparison algorithms and $N$ is the number of instances. The calculation of $q_{\alpha}$ is detailed in [63]

$$
\mathrm{CD}=q_{\alpha} \sqrt{\frac{k(k+1)}{6 N}}
$$

As can be seen in Table VI, the results of the Wilcoxon sign rank test show the proposed EDA-HH performed more effectively than the competitors under the $90 \%$ and $95 \%$ confidence levels. In Table VI, $R+$ means that the EDA-HH performed better than the comparison algorithms on $\mathrm{R}+$ instances, and $R$ - indicates that the other algorithm performed better than EDA-HH. The "Yes" in Table VI illustrated that there exists a significant difference when EDA-HH compared with the other competitors.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Interval plot of interaction between compared algorithms and instance characteristics.

In addition, the multifactor ANOVA, which considers the relationship between various factors and ARPD value, is employed to analyze the test results further. The means plots and interval plots with $95 \%$ confidence are reported in Fig. 8 and Fig. 21 (supplementary materials). From these figures, the performance of all algorithms gets better with the increasing number of jobs and gets worse with the increasing number of machines. As shown in Fig. 21(d), the change of the number of products has not affect the ARPD value and the test result of ED-HH is relatively better than the other algorithms. It is noteworthy that the ARPD is decreased for the proposed EDAHH from the perspective of the time factor. The ARPD of the other compared algorithms is not decreased with the increase of the time factor. The reason for this fact is that the results obtained by the proposed EDA-HH get better with the increase of the time factor, which is contrary to the other compared algorithms. On the other hand, there exist differences between the results of each execution due to the randomness of the

![img-8.jpeg](img-8.jpeg)

Fig. 9. Interval plot on $c=20$.
algorithm. The ARPD value of EDA-HH and the number of factories are inverse ratios. Comprehensively, the above results and analysis demonstrated the effectiveness of the proposed EDA-HH on the DAMNIPFSP with the objective of the $C_{\max }$ criterion.

## E. Effectiveness Analysis of Components

The effect of destruction and construction on the performance of the proposed EDA-HH is analyzed in this section. Initialization, destruction, construction, and acceptance criterion are the four stages of the IG algorithm [24], [64]. The IG relies heavily on destruction and construction. During the destruction phase, various components of the existing solution are taken at random or according to predetermined rules. The removed parts are reinserted into the partial solution based on certain rules to establish a complete solution. In this study, the destruction and construction are incorporated into the EDAHH method to improve algorithm exploitation. As illustrated in Table VII of the supplementary material, the EDA-HH with destruction and construction and the EDA-HH without destruction and construction are tested on the 810 large-scale benchmark instances to verify the effectiveness of the destruction and construction. The configuration of the parameters is adopted according Section V-B and the CPU time of execution is adopted to be the stopping condition in this test. Each algorithm is executed five times independently for the 810 instances.

The ARPD values of the experimental results are listed in Table VII. As shown in Fig. 9 and Fig. 17 (supplementary materials), the EDA-HH with destruction and construction and the EDA-HH without destruction and construction are represented by EDA-HH 1 and EDA-HH 2, respectively. The confidence interval of EDA-HH 1 is not overlapped with the intervals of EDA-HH 2, which means that EDA-HH 1 is statistically better than EDA-HH 2. The results show that the EDA-HH with destruction and construction is significantly superior to another one. From Table VII, Fig. 9, and Fig. 17, the EDA-HH with destruction and construction obtained good performance from the perspective of jobs, machines, factories, and products. Thus, the proposed EDA-HH has good robustness.

## F. Complexity Analysis

The analysis of the computational complexity of the proposed EDA-HH is as follows: the computational
complexity of the task of applying the LLHs (lines 3 and 10) to each individual is $\mathcal{O}\left(p s \cdot A \cdot \log _{\xi} 1 / 2\right)$, where $p s$ is the population size, $A$ is the number of low-level heuristics, and $\xi$ is the annealing rate. The computational complexity of the calculation of cumulative probability (line 7) is $\mathcal{O}(A(A-1))$, where $A$ is the number of low-level heuristics. Updating the probability matrix (line 9) has a computational complexity of $\mathcal{O}\left(A^{2}\right)$. The computational complexity of destruction and construction for products and jobs are $\mathcal{O}\left(d^{3}\right)$ and $\mathcal{O}\left(d j^{3}\right)$, respectively.

## VI. CONCLUSION AND DISCUSSION

The DAMNIPFSP with $C_{\max }$ criteria is considered in this article. We used CPLEX to verify the proposed MILP model of DAMNIPFSP with the makespan criterion. A novel hyper-heuristic is presented to address the DAMNIPFSP. The time-consuming flaw of classic EDA can be alleviated by the EDA-based hyper-heuristic approach. The inclusion of the destruction-construction enhances the exploitation capacity of the proposed EDA-HH. The comparative experiments of EDA-HH and the state-of-the-art algorithm on the largescale benchmark exhibit the effectiveness of the proposed algorithm. To illustrate the substantial difference between the suggested EDA-HH and competitors, the nonparametric test is used. The experimental comparison and statistical analysis show that the proposed EDA-HH is an effective algorithm for addressing the DAMNIPFSP. The proposed EDA-HH still has room for improvement. There are some limitations to the proposed algorithm such as the sole probability model that restrict the performance of the algorithm and more effective low-level heuristics need to be designed. The interaction between the high-level heuristic and the low-level heuristic can be enhanced. Moreover, the performance of the proposed algorithm in the practice needs to be tested. Although the model has advanced significantly, there are still some limitations to it. For instance, it does not take into account multiobjective optimization, complex constraint conditions, and dynamic scenarios.

In the future, other outstanding algorithms and techniques will be introduced to enhance the capability of the components under the framework of the hyper-heuristic. The incorporation of some fitness landscape analysis methods to assess the properties of the problems is an intriguing direction that can boost the performance of the algorithm even further. The redesign of the updating mechanism and enhancement of the probability model is attractive for future research. It is worth noting that the DAMNIPFSP with many assembly factories has not recently been investigated. Furthermore, solving the multiobjective DAMNIPFSP [65] is a challenging job. Especially distributed green scheduling has become a hot topic in the research community. Under the background of globalization and carbon neutrality, manufacturing should not only focus on profit growth but also the harmony between humans and nature. Manufacturing enterprises need to consider reducing industrial pollution such as noise to defend the health of the industrial workers. The combination of reinforcement learning and the scheduling problem is promising.
