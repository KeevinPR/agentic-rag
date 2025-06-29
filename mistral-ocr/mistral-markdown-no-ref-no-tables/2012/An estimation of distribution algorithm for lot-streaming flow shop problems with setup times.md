# An estimation of distribution algorithm for lot-streaming flow shop problems with setup times 

Quan-Ke Pan ${ }^{\text {a }}$, Rubén Ruiz ${ }^{\mathrm{b}, *}$<br>${ }^{a}$ College of Computer Science, Liaocheng University, Liaocheng 252059, PR China<br>${ }^{\mathrm{b}}$ Grupo de Sistemas de Optimización Aplicada, Instituto Tecnológico de Informática, Ciudad Politécnica de la Innovación, Edifico 8G, Acc. B. Universitat Politècnica de València, Camino de Vera s/n, 46022 Valencia, Spain

## A R T I C L E I N F O

Article history:
Received 7 July 2010
Accepted 9 May 2011
Processed by Associate editor Zhang
Available online 12 May 2011
Keywords:
Flow shop scheduling
Lot-streaming
Estimation of distribution algorithm
Makespan
Sequence-dependent setup times

## A B S T R A C T

Lot-streaming flow shops have important applications in different industries including textile, plastic, chemical, semiconductor and many others. This paper considers an $n$-job $m$-machine lot-streaming flow shop scheduling problem with sequence-dependent setup times under both the idling and noidling production cases. The objective is to minimize the maximum completion time or makespan. To solve this important practical problem, a novel estimation of distribution algorithm (EDA) is proposed with a job permutation based representation. In the proposed EDA, an efficient initialization scheme based on the NEH heuristic is presented to construct an initial population with a certain level of quality and diversity. An estimation of a probabilistic model is constructed to direct the algorithm search towards good solutions by taking into account both job permutation and similar blocks of jobs. A simple but effective local search is added to enhance the intensification capability. A diversity controlling mechanism is applied to maintain the diversity of the population. In addition, a speed-up method is presented to reduce the computational effort needed for the local search technique and the NEH-based heuristics. A comparative evaluation is carried out with the best performing algorithms from the literature. The results show that the proposed EDA is very effective in comparison after comprehensive computational and statistical analyses.
(c) 2011 Elsevier Ltd. All rights reserved.

## 1. Introduction

The permutation flow shop scheduling problem is one of the most extensively studied combinatorial optimization problems. It has important applications, among others, in manufacturing systems, assembly lines and information service facilities in use nowadays. In a traditional flow shop, there are $n$ jobs that have to be processed on $m$ machines. All jobs visit the machines in the same sequence. Each job is assumed to be indivisible, and thus, it cannot be transferred to the downstream machine until the whole operation on the preceding machine is finished. Nevertheless, this is not the case in many practical environments where a job or lot consists of many identical items. For example, in the fastener production process, jobs are batches of thousands of bolts, dowels, or rivets. The whole batch does not need to be finished in order to move on to the next machine. Another example comes from the electronics and semiconductor production environment where a job comprises thousands of identical electronic components and again it is not necessary to wait for all items in the lot to be completed before moving to the downstream machine. In order to accelerate

[^0]production, a job is allowed to overlap its operations between successive machines by splitting it into a number of smaller sublots and moving the completed portion of the sub-lots to downstream machines [62]. More examples arise in the ceramic tile sector where batches of ceramic tiles are composed of literally thousands of ceramic tiles. When going from the molding and glaze decoration lines to the kiln firing machines, the whole batch of tiles does not need to be fully completed and overlapping is desirable in practice. The process of splitting jobs into sub-lots is usually called lot-streaming, which was first introduced by Reiter [40] and has become one of the most effective techniques used to implement time-based strategies in today's global competition [8,50]. Generally, there are two different production situations when processing the sub-lots of a job, namely, the idling case and no-idling case. In the no-idling case, jobs must be continuously processed without interruptions (i.e., idle time) between any two adjacent sub-lots of the same job. The idling case allows idle time on machines. It is known that makespan based on the idling case is shorter than that based on the no-idling case under the same sub-lot type [8]. However, both cases have their respective practical applications in today's competitive production environments. With regards to the potential benefits of lot streaming, they are mentioned by Truscott [55] as follows: (a) reduction in production lead times (thus, leading to better due-date performance); (b) reduction in work-in-process inventory and associated costs; (c) reductions in interim storage and


[^0]:    * Corresponding author. Tel.: +349638770 07x74946; fax: +34963877499.

    E-mail addresses: panquanke@gmail.com (Q.-K. Pan),
    rruiz@eio.upv.es (R. Ruiz)

space requirements; and (d) reduction in material handling system capacity requirements. Therefore, in recent years, lot streaming has received extensive attention and has been applied to flow shop scheduling problems starting with the work of Tseng and Liao [56].

Setup times involve non-productive operations such as cleaning, obtaining or adjusting tools, fixing or releasing parts to machines and others. Setup times are very important in practice as noted in Allahverdi and Soroush [3]. Although they are not part of the job processing times, these operations have to be done prior to the processing of the jobs. Setup times can be broadly classified in two categories [1], [2]. The first category is referred to as sequence-independent setup, where setups depend only on the machine and on the next job to be processed. The second one is sequence-dependent setup, in which setups depend not only on the job to be processed next but also on its immediately preceding job on the same machine. An example is given by Ruiz and Allahverdi [43]: in the painting industry, after producing a black paint, substantial cleaning must be performed if one intends to produce a white paint, while less cleaning is necessary if a batch of dark gray paint is to be produced. On the other hand, almost no cleaning is required when production is changed from a sub-lot of the black paint to another one of a similar black paint.

This paper considers lot-streaming flow shop scheduling problems with sequence-dependent setup times, with important applications, as commented, in textile, plastic, chemical and semiconductor industries. Without loss of generality, this problem is denoted as $F_{m}, L_{n} / p m n u, S T_{s d} / C_{m a x}$ by using the well known $\alpha / \beta / \gamma$ notation with the extensions of Chang and Chiu [8] and Allahverdi et al. [1], where $S T_{\text {sd }}$ represents the sequence-dependent setup time and $F_{m}$ and $L_{n}$ stand for the $n$-job $m$-machine lotstreaming flow shop configuration. The permutation flow shop scheduling problem under makespan criterion is already NP-Hard as was shown by Garey et al. [12] (for three or more machines, i.e., $m \geq 3$ ). Since we consider lot-streaming and sequence-dependent setup times, the studied problem is also NP-Hard.

Estimation of distribution algorithms (EDA) were introduced by Mühlenbein and Paass [31]. EDA are a class of novel population-based evolutionary algorithms. Unlike traditional evolutionary algorithms, EDA samples new solutions from a probabilistic model which characterizes the distribution of promising solutions in the search space at each generation. Due to its effectiveness and search ability, EDA has recently attracted much attention in the field of evolutionary computation [21], and it has already been applied to solve combinatorial optimization problems, including the flow shop scheduling problem in Jarboui et al. [15] or more complex hybrid flow shop settings in Salhi et al. [48]. Therefore, EDA seems like a promising venue of research for the studied scheduling problem. However, to the best of our knowledge, there is no published work dealing with the lot-streaming version of flow shop scheduling problem using EDA, let alone with sequence-dependent setup times. In this paper we study this important and practical $F_{m}, L_{n} / p m n u, S T_{\text {sd }} / C_{m a x}$ problem. Furthermore, both the no-idling and idling cases are considered. The proposed EDA makes extensive use of some effective techniques like a NEH-based initialization, a sequence-representation-based probabilistic model, diversity measures and an insert-neighborhood-based local search. Computational experiments and statistical comparisons show that the proposed EDA outperforms the best performing algorithms that have recently appeared for solving the lot-streaming flow shop scheduling problem.

The rest of the paper is organized as follows: in Section 2, the literature on the lot-streaming flow shop scheduling problem is reviewed. In Section 3, the lot-streaming flow shop scheduling problem with sequence-dependent setup times is stated and formulated. Section 4 gives a brief introduction to the basic EDA methodology and presents our proposed EDA method in detail. Section 5 contains the calibration of the proposed EDA. The
computational results and comparisons are provided in Section 6. Finally, concluding remarks are presented in Section 7.

## 2. Literature review

Having so many practical applications, lot-streaming has been extensively studied in the academic as well as in the industrial fields since the late 1980s [8]. Some papers deal with single-job lot-streaming problems, where the main goal is to determine the best allocation of sub-lots or the size of each sub-lot so as to minimize some given performance measures.

There are some important theoretical or basic results to highlight. First, Potts and Baker [37] indicated that it was sufficient to use the same sub-lot sizes for all machines as regards makespan criterion. This is an important result for the flow shop problem as different number of sub-lots for the machines would complicate the problems significantly. However, it remains to be seen if this result holds when sequence-dependent setup times are present. Furthermore, Baker and Jia [4] showed that makespan improved with the number of sub-lots. While this is an expected result (the more sub-lots the higher the machine utilization), the paper of Baker and Jia [4] actually quantifies and deeply studies the effect. Lastly, Trietsch and Baker [54] generalized some important structural properties by reviewing the different forms of singlejob lot-streaming in the literature.

Apart from these theoretical results, many papers have been published where different lot-streaming flow shop settings and objectives are studied. Many of them are now discussed in chronological order. Kropp and Smunt [19] presented optimal sub-lot size policies and two heuristic methods for flow time minimization in a flow shop setting with no additional constraints. Vickson and Alfredsson [60] studied the effect of batch transfer in a two-machine and special three-machine flow shop problems with unit-size sublots. Cetinkaya [7] proposed an optimal transfer batch and scheduling algorithm for a two-stage problem with separated setup, processing and removal times. Vickson [59] examined a twomachine problem involving setup and sub-lot transfer times with respect to both continuous and integer valued sub-lot sizes and some exact algorithms were presented. Sriskandarajah and Wagneur [51] presented an efficient heuristic for solving the problem of simultaneous lot-streaming and scheduling of multiple products in a two-machine no-wait flow shop. For the $m$-machine lot-streaming flow shop problem, Kumar et al. [20] extended the approach presented by Sriskandarajah and Wagneur [51] to the $m$-machine case. Later, Kalir and Sarin [16] proposed a bottleneck minimal idleness heuristic to sequence a set of batches to be processed in equal sub-lots for minimizing makespan. Yoon and Ventura [63] developed sixteen pairwise interchange methods to optimize the mean weighted absolute deviation from due dates. To the best of our knowledge, this is the first study about lot-streaming flow shop involving due dates. Bukchin et al. [6] examined the optimal solution properties and developed a solution procedure for a twomachine flow shop scheduling problem with sub-lot detached setups and batch availability. Liu [23] proposed a heuristic method for discrete lot streaming with variable sub-lots in a flow shop. Kalir and Sarin [17] developed a near optimal solution procedure for the determination of the number of sub-lots as well as the sequence in a flow shop lot streaming problem with sub-lot-attached setups.

Zhang et al. [64] developed two heuristic algorithms for the multi-job lot-streaming problem in a two-stage hybrid flow shop with the objective to minimize the mean completion time of the jobs. Marimuthu and Ponnambalam [26] proposed a genetic algorithm (GA) and a simulated annealing (SA) for lot streaming in a two-machine flow shop to minimize makespan. Liu et al. [24] studied the multi-product variable lot streaming in a flow shop.

A hybrid heuristic was applied for determining product sequences, lot streaming reallocation machines, and lot streaming ranges by combining a tabu search (TS) with simulated annealing (SA). Additionally, a linear programming model was used to find the minimal makespan and lot streaming for each machine and each product. Feldmann and Biskup [10] provided a mixed integer programming formulation for the multi-product lot streaming problem in a permutation flow shop with intermingling of sublots from different jobs. While in this paper we do not consider intermingling, (where not all sub-lots of the same job follow one another in a sequence), it is a very promising venue of research.

Recently, more complex single-job lot-streaming problems were addressed. Liu [22] investigated the continuous version of the problem and provided optimal and heuristic solution methods for the general problem. Edis and Ornek [9] proposed a heuristic by combining simulation and tabu search to minimize the makespan for a single-product multistage stochastic flow shop problem with consistent sub-lot types and discrete sub-lot sizes. Kim and Jeong [18] proposed a self-adaptive genetic algorithm for scheduling a flow shop problem with no-wait flexible lot-streaming constraints, where the splitting of order quantities of different products into sub-lots and alternative machines with different processing times was dealt with. Martin [30] presented a hybrid genetic algorithm/mathematical programming approach for a multi-family flow shop scheduling problem with lot streaming.

Most of the literature studies the lot streaming flow shop scheduling problem with fixed sizes of sub-lots under the nonintermingled case. For example, Yoon and Ventura [63] presented a hybrid genetic algorithm (HGA) to minimize the mean weighted absolute deviation of job completion times from their due dates. Tseng and Liao [56] developed a discrete particle swarm optimization (DPSO) algorithm. It was shown by the authors that their DPSO algorithm performed much better than the HGA proposed by Yoon and Ventura [63] for solving 900 randomly generated instances. More recently, Pan et al. [33] presented a discrete artificial bee colony (DABC) algorithm which outperformed both previous DPSO and HGA algorithms. Marimuthu et al. [27,28,29] applied a tabu search (TS), simulated annealing (SA), hybrid genetic algorithm (HGA), ant colony optimization (ACO) and threshold accepting (TA) algorithms, respectively, to deal with both makespan and total flow time criteria for a flow shop problem involving setup times. For multiobjective problems, Huang and Yang [14] presented a scheduling mechanism and an ant colony optimization heuristic for an overlap manufacturing problem with various ready times and sequence-dependent setup times.

As we can see from the previous review, and to the best of our knowledge, no metaheuristic has been applied to minimize the makespan in the $n$-job $m$-machine lot-streaming flow shop problem with sequence-dependent setup times. A comprehensive review of scheduling problems involving lot-streaming can be found in Chang and Chiu [8] and in Sarin and Jaiprakash [50].

## 3. Lot-streaming flow shop scheduling problem

This paper considers an $n$-job $m$-machine lot-streaming flow shop scheduling problem. The statement of the problem and an illustrative example are described in this section.

### 3.1. Statement of the problem

We assume that each job $j$ can be split into a number $f(j)$ of smaller sub-lots with equal size such that $f(j)$ is the same for all machines. This follows the research work of Yoon and Ventura [62], Yoon and Ventura [63], Tseng and Liao [56], Marimuthu et al. [27,28,29]. Once the processing of a sub-lot on its preceding
machine is completed, it can be transferred to the downstream machine immediately. However, all $f(j)$ sub-lots of job $j$ should be processed continuously as no intermingling is allowed. A separable sequence-dependent setup time is necessary for the first sublot of each job $j$ before it can be processed on any machine $k$. Furthermore, at any time, each machine can process at most one sub-lot and each sub-lot can be processed on at most one machine. Let the processing time of each sub-lot of job $j$ on machine $k$ be $p\left(k, j\right)$, and the setup time of job $j$ on machine $k$, after having processed job $j^{\prime}$ is $s\left(k, j^{\prime}, j\right)$. For simplicity, let $s\left(k, j, j\right)$ represent the setup time of job $j$ if it is the first job to be proceeded in the machine. The objective is to find a sequence with the optimal sublot starting and completion times to minimize the makespan.

Let a job permutation $\pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right\}$ represent the sequence of jobs to be processed, and $S T(k, j, e)$ and $C T(k, j, e)$ denote the earliest start time and the earliest completion time of the eth sub-lot of job $j$ on machine $k$, respectively. $C_{\max }(\pi)$ denotes the makespan of the schedule under permutation $\pi$. Then, for the idling case, $C_{\max }(\pi)$ can be calculated as follows:
$\left\{\begin{array}{l}S T\left(1, \pi_{1}, 1\right)=s\left(1, \pi_{1}, \pi_{1}\right) \\ C T\left(1, \pi_{1}, 1\right)=S T\left(1, \pi_{1}, 1\right)+p\left(1, \pi_{1}\right) \\ S T\left(k, \pi_{1}, 1\right)=\max \left(C T\left(k-1, \pi_{1}, 1\right), s\left(k, \pi_{1}, \pi_{1}\right)\right), \quad k=2,3, \ldots, m \\ C T\left(k, \pi_{1}, 1\right)=S T\left(k, \pi_{1}, 1\right)+p\left(k, \pi_{1}\right), \quad k=2,3, \ldots, m\end{array}\right.$
$\left\{\begin{array}{l}S T\left(1, \pi_{1}, e\right)=C T\left(1, \pi_{1}, e-1\right), \quad e=2,3, \ldots, l\left(\pi_{1}\right) \\ C T\left(1, \pi_{1}, e\right)=S T\left(1, \pi_{1}, e\right)+p\left(1, \pi_{1}\right), \quad e=2,3, \ldots, l\left(\pi_{1}\right) \\ S T\left(k, \pi_{1}, e\right)=\max \left(C T\left(k-1, \pi_{1}, e\right), C T\left(k, \pi_{1}, e-1\right)\right), \quad e=2,3, \ldots, l\left(\pi_{1}\right), k=2,3, \ldots, m \\ C T\left(k, \pi_{1}, e\right)=S T\left(k, \pi_{1}, e\right)+p\left(k, \pi_{1}\right), \quad e=2,3, \ldots, l\left(\pi_{i}\right), k=2,3, \ldots, m\end{array}\right.$
$\left\{\begin{array}{l}S T\left(1, \pi_{i}, 1\right)=C T\left(1, \pi_{i-1}, l\left(\pi_{i-1}\right)\right)+s\left(1, \pi_{i-1}, \pi_{i}\right), \quad i=2,3, \ldots, n \\ C T\left(1, \pi_{i}, 1\right)=S T\left(1, \pi_{i}, 1\right)+p\left(1, \pi_{i}\right), \quad i=2,3, \ldots, n \\ S T\left(k, \pi_{i}, 1\right)=\max \left(C T\left(k-1, \pi_{i}, 1\right), C T\left(k, \pi_{i-1}, l\left(\pi_{i-1}\right)\right)+s\left(k, \pi_{i-1}, \pi_{i}\right)\right), \\ i=2,3, \ldots, n, k=2,3, \ldots, m \\ C T\left(k, \pi_{i}, 1\right)=S T\left(k, \pi_{i}, 1\right)+p\left(k, \pi_{i}\right), i=2,3, \ldots, n, k=2,3, \ldots, m\end{array}\right.$
$\left\{\begin{array}{l}S T\left(1, \pi_{i}, e\right)=C T\left(1, \pi_{i}, e-1\right), \quad i=2,3, \ldots, n, e=2,3, \ldots, l\left(\pi_{i}\right) \\ C T\left(1, \pi_{i}, e\right)=S T\left(1, \pi_{i}, e\right)+p\left(1, \pi_{i}\right), \quad i=2,3, \ldots, n, e=2,3, \ldots, l\left(\pi_{i}\right) \\ S T\left(k, \pi_{i}, e\right)=\max \left(C T\left(k-1, \pi_{i}, e\right), C T\left(k, \pi_{i}, e-1\right)\right), \\ i=2,3, \ldots, n, e=2,3, \ldots, l\left(\pi_{i}\right), k=2,3, \ldots, m \\ C T\left(k, \pi_{i}, e\right)=S T\left(k, \pi_{i}, e\right)+p\left(k, \pi_{i}\right), \quad i=2,3, \ldots, n, e=2,3, \ldots, l\left(\pi_{i}\right), k=2,3, \ldots, m\end{array}\right.$
$C_{\max }(\pi)=C T\left(m, \pi_{n}, l\left(\pi_{n}\right)\right)$
Correspondingly, $C_{\max }(\pi)$ for the no-idling case is calculated as follows:
$\left\{\begin{array}{l}S T\left(1, \pi_{1}, 1\right)=s\left(1, \pi_{1}, \pi_{1}\right) \\ C T\left(1, \pi_{1}, l\left(\pi_{1}\right)\right)=S T\left(1, \pi_{1}, 1\right)+l\left(\pi_{1}\right) \times p\left(1, \pi_{1}\right)\end{array}\right.$
$\left\{\begin{array}{r} S T\left(k, \pi_{1}, 1\right)=\max \left\{s\left(k, \pi_{1}, \pi_{1}\right), S T\left(k-1, \pi_{1}, 1\right)+p\left(k-1, \pi_{1}\right)\right. \\ C T\left(k-1, \pi_{1}, l\left(\pi_{1}\right)\right)-\left(l\left(\pi_{1}\right)-1\right) \times p\left(k, \pi_{1}\right)\right), \quad k=2,3, \ldots, m \\ C T\left(k, \pi_{1}, l\left(\pi_{1}\right)\right)=S T\left(k, \pi_{1}, 1\right)+l\left(\pi_{1}\right) \times p\left(k, \pi_{1}\right), \quad k=2,3, \ldots, m\end{array}\right.$
$\left\{\begin{array}{r}S T\left(1, \pi_{i}, 1\right)=C T\left(1, \pi_{i-1}, l\left(\pi_{i-1}\right)\right)+s\left(1, \pi_{i-1}, \pi_{i}\right), \quad i=2,3, \ldots, n \\ C T\left(1, \pi_{i}, l\left(\pi_{i}\right)\right)=S T\left(1, \pi_{i}, 1\right)+l\left(\pi_{i}\right) \times p\left(1, \pi_{i}\right), \quad i=2,3, \ldots, n\end{array}\right.$
$\left\{\begin{array}{r} S T\left(k, \pi_{i}, 1\right)=\max \left(S T\left(k-1, \pi_{i}, 1\right)+p\left(k-1, \pi_{i}\right)\right. \\ C T\left(k-1, \pi_{i}, l\left(\pi_{i}\right)\right)-\left(l\left(\pi_{i}\right)-1\right) \times p\left(k, \pi_{i}\right), \\ C T\left(k, \pi_{i-1}, l\left(\pi_{i-1}\right)\right)+s\left(k, \pi_{i-1}, \pi_{i}\right)\right), \quad i=2,3, \ldots, n ; k=2,3, \ldots, m \\ C T\left(k, \pi_{i}, l\left(\pi_{i}\right)\right)=S T\left(k, \pi_{i}, 1\right)+l\left(\pi_{i}\right) \times p\left(k, \pi_{i}\right), \quad i=2,3, \ldots, n ; k=2,3, \ldots, m\end{array}\right.$

$C_{\max }(\pi)=\operatorname{CT}\left(m, \pi_{n}, l\left(\pi_{n}\right)\right)$
Then the objective of the lot streaming flow shop scheduling problem with makespan criterion is to find a permutation $\pi^{*}$ in the set of all permutations $\Pi$ such that
$C_{\max }\left(\pi^{*}\right) \leq C_{\max }(\pi), \quad \forall \pi \in \Pi$
In equation set (1), the first and third equations specify the earliest start time for the first sub-lot of job $\pi_{1}$, where both the completion time of the sub-lot on the previous machine and the setup time of the job on the current machine are considered. The second and fourth equations calculate the completion times, making sure that preemption of jobs is not allowed. Equation set (2) controls the earliest start time and the earliest completion time for the successive sub-lots of job $\pi_{1}$, which ensure that sub-lots of the same job are processed continuously. Equation sets (3) and (4) contain the calculations for the sub-lots of the following jobs in the sequence. When calculating the start time for the first sub-lot of a job in set (3), we take into account the completion time of the previous job on the current machine, the completion time of the sub-lot on the previous machine, and the setup time of the job on the current machine. Finally, from Eq. (5), we can see that the makespan is equivalent to the completion time of the last sub-lot of the last job $\pi_{n}$ on the last machine.

Equation sets (6)-(10) consider the makespan for the no-idling case. In sets (6) and (7), the top equations give the earliest start time for the first sub-lot of job $\pi_{1}$. We can see that the earliest start time is equal to the maximum value among the setup time of the job on the current machine, the completion time of the first sub-lot on the previous machine, and the difference between the completion time of the whole job on the previous machine and the total processing time of the whole job on the preceding machine except the last sub-lot, which ensures that no idling interruption time exists between any two adjacent sub-lots of the same job. The bottom equations calculate the earliest completion time for the last sub-lot of job $\pi_{1}$. Sets (8) and (9) control the calculation of the subsequent jobs in the permutation. Different from sets (6) and (7), we need consider the completion time of the last sub-lot of the previous job on the preceding machine when calculating the earliest start time.

### 3.2. Illustrative example

The following example illustrates the calculation for a four-job, three-machine instance with a given permutation $\pi=[1,2,3,4]$. Let us give the necessary data for the example:
$[f(j)]_{1>4}=[2,2,1,2]$, i.e., jobs 1,2 and 4 contain two sub-lots and job 3 , just one sub-lot
$\left\{p(k, j)\right\}_{3>4}=\left[\begin{array}{llll}4 & 3 & 2 & 5 \\ 2 & 2 & 2 & 3 \\ 2 & 2 & 3 & 5\end{array}\right]$
$\left[s\left(k, f_{1} j\right)\right]_{3>4>5}=\left\{\left[\begin{array}{llll}2 & 1 & 2 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 2 & 1 & 2 \\ 2 & 1 & 1 & 1\end{array}\right]\right.$ $\left.\left[\begin{array}{llll}2 & 1 & 1 & 1 \\ 2 & 2 & 2 & 2 \\ 2 & 2 & 2 & 2 \\ 1 & 2 & 1 & 1\end{array}\right]\right.$ $\left.\left[\begin{array}{llll}2 & 1 & 2 & 2 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 2 \\ 1 & 2 & 2 & 1\end{array}\right]\right\}$
For the idling case, the makespan is calculated below and the Gantt chart is shown in Fig. 1
$\operatorname{ST}(1,1,1)=s(1,1,1)=2$
$\operatorname{CT}(1,1,1)=\operatorname{ST}(1,1,1)+p(1,1)=2+4=6$
$\operatorname{ST}(2,1,1)=\max \{\operatorname{CT}(1,1,1), s(2,1,1)\}=\max \{6,2\}=6$
$\operatorname{CT}(2,1,1)=\operatorname{ST}(2,1,1)+p(2,1)=6+2=8$
$\operatorname{ST}(3,1,1)=\max \{\operatorname{CT}(2,1,1), s(3,1,1)\}=\max \{8,2\}=8$
$\operatorname{CT}(3,1,1)=\operatorname{ST}(3,1,1)+p(3,1)=8+2=10$
$\operatorname{ST}(1,1,2)=\operatorname{CT}(1,1,1)=6$
$\operatorname{CT}(1,1,2)=\operatorname{ST}(1,1,2)+p(1,1)=6+4=10$
$\operatorname{ST}(2,1,2)=\max \{\operatorname{CT}(1,1,2), \operatorname{CT}(2,1,1)\}=\max \{10,8\}=10$
$\operatorname{CT}(2,1,2)=\operatorname{ST}(2,1,2)+p(2,1)=10+2=12$
$\operatorname{ST}(3,1,2)=\max \{\operatorname{CT}(2,1,2), \operatorname{CT}(3,1,1)\}=\max \{12,10\}=12$
$\operatorname{CT}(3,1,2)=\operatorname{ST}(3,1,2)+p(3,1)=12+2=14$
$\operatorname{ST}(1,2,1)=\operatorname{CT}(1,1,2)+s(1,1,2)=10+1=11$
$\operatorname{CT}(1,2,1)=\operatorname{ST}(1,2,1)+p(1,2)=11+3=14$
$\operatorname{ST}(2,2,1)=\max \{\operatorname{CT}(1,2,1), \operatorname{CT}(2,1,2)+s(2,1,2)\}=\max \{14,12+1\}=14$
$\operatorname{CT}(2,2,1)=\operatorname{ST}(2,2,1)+p(2,2)=14+2=16$
$\operatorname{ST}(3,2,1)=\max \{\operatorname{CT}(2,2,1), \operatorname{CT}(3,1,2)+s(3,1,2)\}=\max \{16,14+1\}=16$
$\operatorname{CT}(3,2,1)=\operatorname{ST}(3,2,1)+p(3,1)=16+2=18$ and so on until $C_{\max }=\operatorname{CT}(3,4,2)=40$
For the no-idling case, the makespan is calculated below and the Gantt chart is shown in Fig. 2
$\operatorname{ST}(1,1,1)=s(1,1,1)=2$
$\operatorname{CT}(1,1,2)=\operatorname{ST}(1,1,1)+l(1) \times p(1,1)=2+2 \times 4=10$
$\operatorname{ST}(2,1,1)=\max \{s(2,1,1), \operatorname{ST}(1,1,1)+p(1,1), \operatorname{CT}(1,1,2)-(l(1)-1) \times p(2,1)\}$
$=\max \{2,2+4,10-1 \times 2\}=8$
$\operatorname{CT}(2,1,2)=\operatorname{ST}(2,1,1)+l(1) \times p(2,1)=8+2 \times 2=12$
$\operatorname{ST}(3,1,1)=\max \{s(3,1,1), \operatorname{ST}(2,1,1)+p(2,1), \operatorname{CT}(2,1,2)-(l(1)-1) \times p(3,1)\}$
$=\max \{2,8+2,12-1 \times 2\}=10$
$\operatorname{CT}(3,1,2)=\operatorname{ST}(3,1,1)+l(1) \times p(3,1)=10+2 \times 2=14$
$\operatorname{ST}(1,2,1)=\operatorname{CT}(1,1,2)+s(1,1,2)=10+1=11$
$\operatorname{CT}(1,2,2)=\operatorname{ST}(1,2,1)+l(2) \times p(1,2)=11+2 \times 3=17$
$\operatorname{ST}(2,2,1)=\max \{\operatorname{ST}(1,2,1)+p(1,2), \operatorname{CT}(1,2,2)-(l(2)-1) \times p(2,2), \operatorname{CT}(2,1,2)+s(2,1,2)\}$
$=\max \{11+3,17-1 \times 2,12+1\}=15$
$\operatorname{CT}(2,2,2)=\operatorname{ST}(2,2,1)+l(2) \times p(2,2)=15+2 \times 2=19$
$\operatorname{ST}(3,2,1)=\max \{\operatorname{ST}(2,2,1)+p(2,2), \operatorname{CT}(2,2,2)-(l(2)-1) \times p(3,2), \operatorname{CT}(3,1,2)+s(3,1,2)\}$
$=\max \{15+2,19-1 \times 2,14+1\}=17$
$\operatorname{CT}(3,2,2)=\operatorname{ST}(3,2,1)+l(2) \times p(3,2)=17+2 \times 2=21$, and so on until $C_{\max }=\operatorname{CT}(3,4,2)=42$
![img-0.jpeg](img-0.jpeg)

Fig. 1. Gantt chart for the idling case example.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Gantt chart for the no-idling case example.

## 4. Proposed EDA for the lot-streaming flow shop problem

EDA is a new metaheuristic methodology proposed by Mühlenbein and Paass [31], which is based on populations that evolve within the search process and has a theoretical foundation in probability theory. Instead of using the conventional crossover and mutation operations of regular genetic algorithms, EDA adopts a probabilistic model learned from a population of selected individuals to produce new solutions at each generation. Starting from a population of PS randomly generated individuals, EDA estimates a probabilistic model from the information of the selected $Q$ individuals in the current generation, and represents it by conditional probability distributions for each decision variable. $M$ offspring are then sampled in the search space according to the estimated probabilistic model. Finally, the next population is determined by replacing some individuals in the current generation with new generated offspring. The above steps are repeated until some stopping criterion is reached. The pseudo code for the basic EDA is summarized as follows [21]:

## begin

Generate a population of PS individuals randomly;
Calculate fitness for each individual;
while termination criterion not met, do
Select Q individuals and estimate a probabilistic model;
Sample M offspring from the estimated probabilistic model;
Evaluate the M generated offspring;
Generate new population;

## end while

end
We now detail the proposed EDA for solving the lot-streaming flow shop scheduling problem involving sequence-dependent setup times to minimize makespan. We explain the solution representation, population initialization, probabilistic model, generation of new individuals, population update, local search procedure and a diversity controlling mechanism in the next sections.

### 4.1. Solution representation and population initialization

One of the key issues when designing EDA lies in the solution representation where individuals bear the necessary information related to the problem domain at hand. The permutation based representation indicates the job processing order by machines. This representation has been widely used in the literature for a variety of permutation flow shop scheduling problems [45,58,15]. Therefore, we also employ it in this study.

The EDA method is formed by a population of PS individuals or n-job permutations. To guarantee an initial population with a certain level of quality and diversity, a common trend is to construct a few good individuals by effective heuristics and to produce others randomly. This initialization approach ensures a faster convergence to good solutions, and it is widely used in evolutionary algorithms developed for traditional flow shop scheduling problems [58]. It has been long known that the NEH heuristic [32] is a high performer for flow shop scheduling problems under different scenarios [11,44,38]. In this research, we extend it to handle the studied problem, and obtain two heuristics, referred to as NEH1 and NEH2, respectively. The NEH1 is obtained by modifying the objective evaluation in the basic NEH heuristic with the calculations described in Section 3. NEH1 can be described as follows:

Step 1: An initial permutation $\pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right\}$ is generated by sorting jobs in decreasing sum of their total processing times, i.e., $\Sigma_{k=1}^{m} p(k, j) \times l(j), j=1,2, \ldots, n$.

Step 2: A job permutation is established by evaluating the partial sequences based on the obtained initial order. Suppose a current sequence $\pi^{\prime}=\left\{\pi_{1}^{\prime}, \pi_{2}^{\prime}, \ldots, \pi_{i}^{\prime}\right\}$ is already determined for the first $i$ jobs of the initial permutation $\pi$, then $i+1$ partial sequences are constructed by inserting job $\pi_{i+1}$ into the $i+1$ possible positions of the current sequence. Among these $i+1$ partial sequences, the one with the minimum makespan is kept as the current sequence for the next iteration. This step is repeated by considering job $\pi_{i+2}$ and so on until all the jobs have been scheduled.

NEH2 has the same steps as NEH1 with the exception that the step 1 is modified as explained below:

Step 1: An initial permutation $\pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right\}$ is generated by sorting jobs in decreasing sum of their total processing times and mean setup times, i.e., $\Sigma_{k=1}^{m}((p(k, j) \times l(j)+\sum_{j=1}^{n} s$ $\left.\left(k, j^{\prime}, j\right)\right), n), j=1,2, \ldots, n$.

There are a total of $(n-1)(n+2) / 2$ partial sequences generated in step 2, so the computational complexity is $O\left(m n^{3}\right)$ in both noidling and idling cases using the calculations presented in Section 3. For the basic NEH heuristic, a speed-up method was proposed by Taillard [53] resulting in an improved complexity of $O\left(m n^{2}\right)$. Later, the method was extended to the permutation flow shop problem with setup times [41], no-wait flow shop problem [34,36], no-idle flow shop problem [35], blocking flow shop problem [61] and others. Accelerations are very effective for flow shop problems. Rad et al. [38] stated that a very efficient NEH implementation with accelerations results in CPU times of only 77 ms for instances as large as $500 \times 20$ on a PIV 3.2 GHz PC computer. Non-accelerated versions can take up to 30 s for the same problem size. Therefore, we propose makespan calculation accelerations for the lot-streaming flow shop problem with setup times, which results in NEH1 and NEH2 to have a computational complexity of just $O\left(m n^{2}\right)$. This acceleration is now explained below:

Let $S T b(k, j, e)$ be the latest start time of the $e$ th sub-lot of job $j$ on machine $k$ in the backward pass calculation, that is, we proceed from the end of the sequence to the beginning. The procedure to evaluate the $i+1$ partial sequences when inserting job $\pi_{i+1}$ into the $i+1$ possible positions of the partial permutation $\pi^{\prime}=\left\{\pi_{1}^{\prime}, \pi_{2}^{\prime}, \ldots, \pi_{i}^{\prime}\right\}$ can be simplified in the following way:

Step 1: Get $C T\left(k, \pi_{z}^{\prime}, l\left(\pi_{x}^{\prime}\right)\right)$ for $z=1,2, \ldots, i$ and $k=1,2, \ldots, m$.
Step 2: Get $S T b\left(k, \pi_{z}^{\prime}, 1\right)$ for $z=i, i-2, \ldots, 1$ and $k=m-1$, $m-2, \ldots, 1$.
Step 3: Repeat the following steps until all possible positions $q$, $q=\{1,2, \ldots, i+1\}$, of the permutation $\pi^{\prime}=\left\{\pi_{1}^{\prime}, \pi_{2}^{\prime}, \ldots, \pi_{i}^{\prime}\right\}$ are calculated:

Step 3.1: Insert job $\pi_{i+1}$ into position $q$ and generate a partial permutation $\pi^{\prime \prime}$.
Step 3.2: Calculate $C T\left(k, \pi_{q}^{\prime \prime}, l\left(\pi_{q}^{\prime \prime}\right)\right)$ by using the previously calculated $C T\left(k, \pi_{q-1}^{\prime}, l\left(\pi_{q-1}^{\prime}\right)\right)$, where $k=1,2, \ldots, m$. Note that $\pi_{q}^{\prime \prime}=\pi_{i+1}$.
Step 3.3: The makespan of the permutation $\pi^{\prime \prime}$ is given as follows (see in Figs. 3 and 4):
$C_{\max }\left(\pi^{\prime \prime}\right)=\max _{k=1}^{m}\left(C T\left(k, \pi_{q}^{\prime \prime}, l\left(\pi_{q}^{\prime \prime}\right)\right)+s\left(k, \pi_{q}^{\prime \prime}, \pi_{q}^{\prime}\right)+S T b\left(k, \pi_{q}^{\prime}, 1\right)\right)$
Clearly, both NEH1 and NEH2 heuristics result in a computational complexity of $O\left(m n^{3}\right)$ by using the above procedure to evaluate the generated partial sequences. With the presented

NEH1 and NEH2, we propose a population initialization procedure with both a high quality and a high diversity as follows:

Step 1: Generate an individual using NEH1.
Step 2: Generate an individual using NEH2. If it is different from the individual generated by NEH1, put it into population; otherwise discard it.
Step 3: Randomly produce an individual in the solution space. If it is different from all existing individuals, put it into the population; otherwise discard it. Repeat step 3 until the population has $P S$ individuals.

The $P S$ individuals of the population are always stored in ascending order of their makespan values.

### 4.2. Selection operator and probabilistic model

The probabilistic model construction represents the main part of the EDA method, which is estimated from the genetic information of the individuals chosen from the population by a selection operator. In classic evolutionary algorithms, roulette and tournament selection operators are commonly used. Such selection operators either require fitness and a mapping calculation or the individuals to be continuously compared and sorted. In this paper, we select the $Q$ best individuals from the population to estimate a probabilistic model. Since individuals are stored in ascending order of their makespan values, we can complete the operator by selecting the first $Q$ individuals in the population. This results in a very fast selection operator.

The performance of the EDA is closely related to the probabilistic model, and obviously, a good model can enhance the algorithm's efficiency and effectiveness for optimizing the problem
![img-2.jpeg](img-2.jpeg)

Fig. 3. Insert job ' 4 ' into the second position of the permutation $\pi=\{1,2,3\}$. Idling case.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Insert job ' 4 ' into the second position of the permutation $\pi=\{1,2,3\}$. No-idling case.
considered. Thus, the best choice of the model is crucial for designing an effective EDA. For solving the permutation flow shop scheduling problem with total flow time criterion, Jarboui et al. [15] presented a probabilistic model based on both the order of the jobs in the sequence and on similar blocks of jobs present in the selected individuals, which is described as follows:

Let $\rho_{i, j}$ be the number of times that job $j$ appears before or in position $i$ in the selected individuals, and $\tau_{f, j}(i)$ the number of times that job $j$ appears immediately after job $j^{\prime}$ when job $j^{\prime}$ is in position $i-1$. Then, $\eta_{i, j}=\delta_{1} \times \rho_{i, j}$ and $\mu_{f, j}(i)=\delta_{2} \times \tau_{f, j}(i)$ indicate the importance of the order of jobs and of the similar blocks of jobs in the selected sequences, respectively, where $\delta_{1}$ and $\delta_{2}$ are two parameters used for the diversification of the solutions. Then, the probability for positioning job $j$ in the $i$ th position of the offspring is determined by
$\xi_{i, j}=\frac{\eta_{i, j} \times \mu_{f, j}(i)}{\sum_{l \in \Omega(i)} \eta_{i, l} \times \mu_{f, j}(i)}$
where $\Omega(i)$ is the set of jobs not scheduled until position $i$ and $j^{\prime}$ is the job in the $(i-1)$ th position of the offspring.

There are some shortcomings in the EDA model presented by Jarboui et al. [15]. First, as shown in Ruiz et al. [45], there are many similar blocks of jobs within the individuals' sequences in the latter stages of evolutionary methods. If these blocks are disrupted, the algorithm has a high probability to produce offspring with worse makespan values. These similar blocks may occupy the same positions or different positions. However, only the blocks in the same positions are considered by Jarboui et al. [15]. Second, according to the definition of $\tau_{f, j}(i)$, it is equal to zero when $i=1$, since job $j$ is the first job in the sequence and no job $j^{\prime}$ is located before it. This results in the probability of selection of any job $j$ in the first position to be always equal to zero. In other words, the first job of the offspring is determined randomly and not according to genetic information. Finally, if at an early stage of the algorithm there are not enough blocks in the same position, and $\tau_{f, j}(i)$ is equal to zero for most of jobs, only a few jobs with $\tau_{f, j}(i)>0$ are selected for producing offspring. Thus, the population easily looses diversity. To address the above shortcomings, we present a new probabilistic model, which is now detailed:

Let $\lambda_{f, j}$ represent the number of times that job $j$ appears immediately after job $j^{\prime}$ in the selected individuals, which indicates the importance of similar blocks of jobs not only in the same positions but also in different positions as well. Then, the probability of placing job $j$ in the $i$ th position of the offspring is given by
$\xi_{i, j}= \begin{cases}\frac{\rho_{i, j}}{\sum_{l \in \Omega(i)} \rho_{i, l}} & i=1 \\ \frac{\left(\left(\rho_{i, j}\right) /\left(\sum_{l \in \Omega(i)} \rho_{i, l}\right)+\left(\lambda_{f, j}\right) /\left(\sum_{l \in \Omega(i)} \lambda_{f, j}\right)\right)}{2} & i=2,3, \ldots, n\end{cases}$
An example with four jobs is used to illustrate the presented probabilistic model. Suppose the selected individuals are $\pi(1)=\{1,2,3,4\}, \pi(2)=\{2,3,4,1\}$ and $\pi(3)=\{1,4,2,3\}$. Therefore, $\rho_{i, j}$ and $\lambda_{f, j}$ are given below
$\left[\rho_{i, j}\right]_{4 \times 4}=\left[\begin{array}{llll}2 & 1 & 0 & 0 \\ 2 & 2 & 1 & 1 \\ 2 & 3 & 2 & 2 \\ 3 & 3 & 3 & 3\end{array}\right], \quad\left[\lambda_{f, j}\right]_{4 \times 4}=\left[\begin{array}{cccc}-1 & 1 & 0 & 1 \\ 0 & - & 3 & 0 \\ 0 & 0 & - & 2 \\ 1 & 1 & 0 & -\end{array}\right]$
Then, we calculate the probability of selection of each job in $\Omega(1)=\{1,2,3,4\}$ for the first position as follows: $\xi_{1,1}=2 /$ $(2+1)=0.67, \quad \xi_{1,2}=1 /(2+1)=0.33, \quad \xi_{1,3}=0 /(2+1)=0, \quad \xi_{1,4}=0 /$ $(2+1)=0$.

Suppose job 1 was selected for the first position and $\Omega(2)=\{2,3,4\}$, then we calculate the probability of section of each

job in $\Omega(2)=\{2,3,4\}$ as follows:
$\xi_{2,2}=(2 /(2+1+1)+1 /(1+0+1)) / 2=0.5$
$\xi_{2,3}=(1 /(2+1+1)+0 /(1+0+1)) / 2=0.125$
$\xi_{2,4}=(1 /(2+1+1)+1 /(1+0+1)) / 2=0.375$

### 4.3. Generation of new individuals and population update

Inspired by the algorithm developed by Rajendran and Ziegler [39] and the DPSO algorithm by Tseng and Liao [56], we present a procedure to generate a new sequence $\pi^{\prime}=\left\{\pi_{1}^{\prime}, \pi_{2}^{\prime}, \ldots, \pi_{n}^{\prime}\right\}$. Starting from an empty sequence, the procedure constructs $\pi^{\prime}$ by choosing a job for the first position, followed by choice of the second job, and so on. The pseudo code of the constructing procedure is given as follows:

```
begin
    for i=1 to n do
        if rand \} \< \varepsilon\ then
        Choose the first unscheduled job in the reference
        sequence.
    else
        Select job j according to probability \xi \cup.
    endif
    endfor
end
```

In the above procedure, $\varepsilon$ is a control parameter; rand () is a function returning a random number sampled from a uniform distribution between 0 and 1 . The reference sequence is randomly chosen from the selected individuals for estimating the probabilistic model. When rand () $\geq \varepsilon$, we randomly select $\theta$ jobs from the unscheduled job set and the job with the largest $\xi_{i j}$ is put into the $i$ th position of the new sequence $\pi^{\prime}$. To generate $M$ offspring, the above procedure is repeated $M$ times so to sample $M$ offspring from the probabilistic model.

Another aspect considered in the EDA is the population update for the next generation. To maintain the diversity of the population and to avoid cycling the search, the population is updated in the following way [45]:

Step 1: Set $i=1$.
Step 2: If offspring $i$ is better than the worst individual of the population and if there is no other identical individual in the population, replace the worst individual by $i$, otherwise, discard $i$.
Step 3: Set $i=i+1$, if $i \leq M$, go to step 2 ; otherwise stop the procedure.

### 4.4. Local search

It is natural to add a local search into the EDA to carry out intensification. We employ a local search based on the job insertion operator, which is very suitable for performing a fine local search and that is commonly used to produce a neighboring solution in the flow shop literature [46,58]. In this local search, a job is extracted from its original position in the sequence and reinserted in all other $n$-1 possible positions. If a better makespan value is found, the solution is replaced. We repeat the procedure until no improvements are found. According to the extraction order of jobs in the first step, the local search can be classified as referenced local search [34] and local search without order [46]. Let $\pi^{0}=\left\{\pi_{1}^{0}, \pi_{2}^{0}, \ldots, \pi_{n}^{0}\right\}$ denote the best job sequence found so far, and $\pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right\}$ be a sequence that undergoes
local search. Then the referenced local search is described as follows:

Step 1: Set $i=1$ and a counter Cnt to 0 .
Step 2: Find job $\pi_{i}^{0}$ in permutation $\pi$ and record its position.
Step 3: Take out job $\pi_{i}^{0}$ from its original position in $\pi$. Then insert it in another different position of $\pi$, and adjust the permutation accordingly by not changing the relative positions of the other jobs. Consider all the possible insertion positions and denote the best obtained sequence as $\pi^{*}$.
Step 4: If $\pi^{*}$ is better than $\pi$, then set $\pi=\pi^{*}$ and Cnt $=0$; otherwise set $C n t=C n t+1$.
Step 5: If Cnt $<n$, let $i=\left\{\begin{array}{ll}i+1 & i<n \\ 1 & n\end{array}\right.$, and go to step 2 ,
otherwise output the current permutation $\pi$ and stop.

The local search without order is sensibly different:
Step 1: Set counter Cnt $=0$.
Step 2: Remove a job at random from its original position in $\pi$ without repetition. Then insert it in another different position of $\pi$, and adjust the permutation accordingly by not changing the relative positions of the other jobs. Consider all the possible insertion positions and denote the best obtained sequence as $\pi^{*}$.
Step 3: If $\pi^{*}$ is better than $\pi$, then let $\pi=\pi^{*}$.
Step 4: Let Cnt $=\operatorname{Cnt}+1$. If Cnt $<n$, go to step 2 .
Step 5: If the permutation $\pi$ was improved in the above steps 1 through 4 , then go to step 1 ; otherwise output the current permutation and $\pi$ stop.

We test both the referenced local search and the local search without order in our study. The local search is applied to each generated offspring with a probability $P_{0}$, that is, local search is applied if a random number uniformly generated in the range of $[0,1]$ is less than $P_{0}$. In addition, the local search is also applied to the best individual after the initialization of the population. Obviously, the previously proposed speed-up procedure is used in the presented local search methods.

### 4.5. Diversity controlling mechanism

Invariably, as the population of the EDA evolves over generations, its diversity diminishes and the individuals in the population become very similar. This results in search stagnation. To overcome this problem, as did in the literature [45,58], a restart mechanism is applied when the diversity value falls below a given threshold value $\gamma$. In the restart mechanism, the $20 \%$ best individuals are kept from the current population and the remaining $80 \%$ are generated randomly. At the same time, to reduce the computation, the diversity value is calculated at least 100 generations after the algorithm restarts. In addition, we present a very simple method to evaluate the diversity of the population based on both the job order and on similar blocks of jobs in the sequences of the current population as follows:

Step 1. Calculate the matrix $\left\{\phi_{i j}\right\}_{n \times n}$ as
$\left[\phi_{i j}\right]_{n \times n}=\left[\begin{array}{cccc}\phi_{1,1} & \phi_{1,2} & \cdots & \phi_{1, n} \\ \phi_{2,1} & \phi_{2,2} & \cdots & \phi_{2, n} \\ \cdots & \cdots & \ddots & \cdots \\ \phi_{n, 1} & \phi_{n, 2} & \cdots & \phi_{n, n}\end{array}\right]$
where $\phi_{i j}$ is the number of times that job $j$ appears at position $i$.

Step 2: Calculate matrix $\left[\lambda_{j, j}\right]_{n \times n}$ as follows:
$\left[\lambda_{j, j}\right]_{n \times n}=\left[\begin{array}{cccccc}-\lambda_{1,2} & \cdots & \lambda_{1, n} \\ \lambda_{2,1} & - & \cdots & \lambda_{2, n} \\ \cdots & \cdots & \ddots & \cdots \\ \lambda_{n, 1} & \lambda_{n, 2} & \cdots & -\end{array}\right]$
recall that $\lambda_{j, j}$ represents the number of times that job $j$ appears immediately after job $j^{\prime}$.
Step 3: Count the number of elements which are larger than zero in $\left[\phi_{i, j}\right]_{n \times n}$, and denote it as $\alpha$.
Step 4: Count the number of elements which are larger than zero in $\left[\lambda_{j, j}\right]_{n \times n}$, and denote it as $\beta$.
Step 5: The diversity value of the population div is then computed as follows:
$\operatorname{div}=\left(\frac{\alpha-n}{n \times \min (n, P S-1)}+\frac{\beta-(n-1)}{(n-1) \times \min (n-1, P S-1)}\right) / 2$
Hence, div gives a very simple diversity measure with a value between zero and one. Obviously, the higher the div value is, the more diverse the population is. A value close to one indicates a very diverse population where each job occupies different positions and no similar blocks of jobs exist among the individuals. On the other hand, a value close to zero means that all individuals are very similar or identical. A simple example is given by considering a population of three individuals with four jobs: $\pi(1)=\{1,2,3,4\}$, $\pi(2)=\{2,3,4,1\}$ and $\pi(3)=\{1,4,2,3\}$. Firstly, we calculate $\left[\phi_{i, j}\right]_{n \times n}$ and $\left[\lambda_{j, j}\right]_{n \times n}$ as follows:
$\left[\phi_{i, j}\right]_{4 \times 4}=\left[\begin{array}{cccccc}2 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 1\end{array}\right], \quad\left[\lambda_{j, j}\right]_{4 \times 4}=\left[\begin{array}{cccccc}-1 & 0 & 1 \\ 0 & - & 3 & 0 \\ 0 & 0 & - & 2 \\ 1 & 1 & 0 & -\end{array}\right]$
Then we get $\alpha=11$ and $\beta=6$.
Finally, we obtain $\operatorname{div}=((11-4) /(4 \times \min (4,3-1))+(6-3) /$ $((4-1) \times \min (4-1,3-1))) / 2=0.69$.

## 5. Calibration of the proposed EDA

Considering all previous sections, the proposed EDA method goes as follows:

Step 1: Set the algorithm parameters $P S, Q, M, P_{N}, \varepsilon, \theta, \gamma$. Let gen $=1$.
Step 2: Initialize the population and evaluate each individual. Step 3: Perform local search to the best individual in the initial population.
Step 4: Select $Q$ best individuals and estimate the probabilistic model.
Step 5: Sample and generate $M$ offspring from the probabilistic model.
Step 6: Perform local search to each offspring in $M$ with probability $P_{N}$.
Step 7: Evaluate the offspring and update the population.
Step 8: Check the diversity of the population if gen $>100$. If the diversity level is less than $\gamma$, perform restart procedure, and set gen $=0$; otherwise set gen $=$ gen +1 .
Step 9: If the stopping criterion is reached, return the best solution found so far and stop; otherwise, go to step 4.

As we can see, the proposed EDA depends on 8 parameters. Therefore, we need to carry out a calibration in order to set them to appropriate values. We first carefully decide the ranges of parameters according to the existing literature, like carried out by Ruiz et al. [45] and by Vallada and Ruiz [58], among many others
and also according to our past experience. Then, we conduct a preliminary experiment to determine the levels for each parameter. In the experiment, we try several typical values for each parameter by simply fixing others, and select the best two or three for calibration in our calibration experiment to keep the aforementioned calibrations at a manageable level. Next, we employ a Design of Experiments approach where each parameter is a controlled factor as follows: population size (PS) tested at three levels, 10, 30 and 50 . Selection size $(Q)$ tested at two levels, 5 and 10. Offspring number $(M)$ tested at two levels, 5 and 10. Probability to apply local search $\left(P_{N}\right)$ tested at two levels, 0.15 and 0.30. Local search type with two variants, referenced local search and local search without order. Parameter $(\varepsilon)$ (generation of new individuals from Section 4.3) tested at two values, 0.7 and 0.9. Parameter $(\theta)$ (also from Section 4.3) tested at two values, 2 and 5. Finally, we have the diversity threshold $(\gamma)$ tested at 0.3 and 0.5 values. This results in a total of $3 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2=$ $2=384$ different combinations, i.e., 384 different configurations for the proposed EDA. All the 384 configurations are tested in a full factorial experimental design with a termination criterion of maximum elapsed CPU time of $t=50 \times n \times(m / 2) \mathrm{ms}$. This termination allows for more time as the number of jobs and machines increases, and has been used in Ruiz et al. [45] and by Vallada and Ruiz [58] and by many others. Each algorithm is tested with a small set of 24 randomly generated instances. The number of jobs and machines for each instance are chosen randomly from the following sets $n \in\{10,30,50,70,90,110\}$ and $m \in\{5,10,15,20\}$. Following Yoon and Ventura [62] and Tseng and Liao [56], the related data for the instances is given by discrete uniform distributions as follows: $l(j) \in U\{1,6\}, p(k, j) \in U\{1,31\}$ and $s(k, j, j) \in U\{1,31\}$. For each instance, 5 difference replicates are run. Therefore, the total number of results is $384 \times 24 \times$ $5=46,080$. Two sets of experiments are conducted: one for the idling and another for the no-idling case.

The proposed EDA procedure is coded in Visual C++ 6.0 and all the 384 configurations are run on a cluster of 30 blade servers each one with two Intel XEON E5420 processors running at 2.5 GHz and with 16 GB of RAM memory. Each processor has four cores and the experiments are carried out in virtualized Windows XP machines, each one with one virtualized processor and 2 GB of RAM memory. As a response variable for the experiment, we measure the relative percentage increase (RPI)
$R P l\left(c_{i}\right)=\left(c_{i}-c^{*}\right) / c^{*} \times 100$
where $c_{i}$ is the makespan value generated in the $i$ th replication by a given algorithm configuration, and $c^{*}$ is the best objective value found by any of the algorithm configurations. Note that for this problem there are no known effective exact techniques and comparing against an optimum solution is not possible. Due to the sequence-dependent setup times, lower bounds are extremely weak and the results would be difficult to analyze. Instead of carrying out a comparison against the best solution given by an algorithm, we tried to obtain better solutions by running the best tested method for an extended period of time. This resulted in negligible differences so we preferred to compare algorithms against the best solution given by them.

All results are analyzed by means of the Analysis of Variance (ANOVA) technique, a very powerful statistical approach that allows us to set the different parameters at statistically significant values among the tested ones. This approach has been followed in Ruiz et al. [45], Ruiz and Stutzle [46], Ribas et al. [42], among many others.

The results of both calibration experiments (idling and noidling) are very similar. All 8 controlled factors (parameters of the proposed DEA) are statistically significant at a $95 \%$ confidence level. The ANOVA table with the full results is not shown here due

![img-4.jpeg](img-4.jpeg)

Fig. 5. Means plot and $95 \%$ Tukey HSD confidence intervals for the calibration experiment in the idling case, factor $\varepsilon$.
to reasons of space. However, all experimental results are available upon request from the authors. Let us picture just one result for the most significant factor in the idling experiment, which is factor $\varepsilon$, whose means plot and $95 \%$ Tukey Honest Significant Difference (HSD) confidence intervals are given in Fig. 5.

As we can see, a level of 0.9 for the factor $\varepsilon$ is statistically better (and by a wide margin) than the value 0.7 . This means that in the generation of offspring, it is much better to use the proposed probabilistic model than the reference solution.

After the calibration experiments, we set the parameters as follows for both the idling and no-idling cases: $\varepsilon=0.9, P S=10$, $\theta=5, Q=10, \gamma=0.3, P_{N}=0.15, M=10$, Local search is referenced local search (factors in order of statistical relevance).

It might be argued that the presented EDA can be further improved by trying consecutive rounds of tuning a few significant parameters and fixing the rest to the best combination found in the above full factorial experiment. We have tried consecutive rounds of tuning by setting $\varepsilon$ from 0.85 to 1.0 with a step equal to 0.01 and other parameters unchanged. The experimental results show that the EDA with $\varepsilon=0.95$ produces better results than with $\varepsilon=0.9$. However, these differences are not large (about 0.2\%) and have little relevance in reality. Therefore, to avoid the problem of over-calibration, we adopt the parameters calibrated by the previous ANOVA.

## 6. Computational results and comparisons

Several metaheuristics exist in the literature for solving $n$-job $m$-machine lot-streaming flow shop scheduling problems. Although none of them considers sequence-dependent setup times, we have carried out a comprehensive re-implementation and adaptation work of most published related material for comparisons. Marimuthu et al. [27,28,29] presented seven methods including a tabu search (which we denote by TS), simulated annealing with insertion neighborhood $\left(\mathrm{SA}_{\mathrm{I}}\right)$, simulated annealing with swap neighborhood $\left(\mathrm{SA}_{\mathrm{E}}\right)$, hybrid genetic algorithm (HGA), ant colony optimization (ACO), threshold accepting with insertion neighborhood $\left(\mathrm{TA}_{\mathrm{I}}\right)$ and threshold accepting with swap neighborhood $\left(\mathrm{TA}_{\mathrm{E}}\right)$ to minimize both mak $n \times$ mespan and total flow time for an $n$-job $m$-machine lot-streaming flow shop problem involving attached setup times. By numerical comparison, the authors claimed that their algorithms were effective and efficient for the problem considered. Tseng and Liao [56] developed a discrete particle swarm optimization (DPSO) algorithm for an $n$-job $m$-machine lot-streaming flow shop scheduling problem with the objective to minimize the mean weighted absolute deviation of job completion times from their due dates, and it was demonstrated by the authors that their DPSO algorithm performed much
better than the HGA proposed by Yoon and Ventura [63] for solving 900 randomly generated instances. More recently, Pan et al. [33] presented a discrete artificial bee colony (DABC) algorithm for the problem considered by Tseng and Liao [56] and Yoon and Ventura [62], which outperformed the previously commented DPSO and HGA methods. We compare the proposed EDA with the above 9 state-of-the-art algorithms, i.e., TS, SA, $\mathrm{SA}_{\mathrm{n}}$, HGA, ACO, $\mathrm{TA}_{\mathrm{I}}$ and $\mathrm{TA}_{\mathrm{e}}$ by Marimuthu et al. [27,28,29], the DPSO algorithm by Tseng and Liao [56], and the DABC algorithm by Pan et al. [33], for solving the problem considered in this paper. We also compare with a recently presented EDA (denoted as $\mathrm{EDA}_{\mathrm{I}}$ ) by Jarboui et al. [15], which was a new state-of-the-art algorithm for minimizing the total flow time in the permutation show shop scheduling problem and provided new upper bounds for 49 out of 90 Taillard benchmark instances. Since the above algorithms are not designed for the problem considered here, we adapt them by using the makespan calculation presented in Section 3, including all accelerations, whenever possible. For the proposed EDA in this paper, we also test it without the speed up procedure (denoted as $\mathrm{EDA}_{\mathrm{n} 0}$ ) and without local search (denoted as $\mathrm{EDA}_{\mathrm{n} \mathrm{E}}$ ), to show the effect of the speed-up and local search procedures.

To test all the methods ( 13 in total), we employ a completely different benchmark as the one used before for calibration. The reason is simple: testing with the same benchmark used for calibration would lead to biased results. We use 28 different problem sizes $n \times m$, where $n=30,50,70,90,110,130,150$, and $m=5,10,15,20$. For each $n \times m$ combination, 10 different instances are randomly generated. As a result, the benchmark has 280 instances. The related data for the instances is given by the discrete uniform distributions as follows: $h j) \in U\{1,6\}, p(k, j) \in U\{1,31\}$ and $s\left(k, j^{\prime}, j\right) \in U\{1,31\}$. All the algorithms were coded in Visual C++ and executed on the same cluster of machines employed for the calibration. For the EDA, we adopt the parameters and operators calibrated in Section 5, whereas for the other algorithms, the parameters are fixed to those given in the literature. Note that calibration is a fine-tuning process and algorithms are not expected to behave entirely different after calibrations.

To make a fair comparison, all the compared algorithms adopt the same maximum elapsed CPU time limit of $t=n \times(m / 2) \times \rho \mathrm{~ms}$ as a termination criterion, where $\rho$ has been tested at three values: 100, 200 and 300. For each of the 280 instances, 5 independent replications are carried out and for each replication, the RPI is calculated. In addition, the average RPI (ARPI) over each problem size and the overall mean ARPI is also calculated as statistics for the solution quality.

Note that there are 13 algorithms, 280 instances and 5 replications for a total of 18,200 results for each value of $\rho$ (54,600 results in total). The comparisons are carried out both for the idling as well as for the no-idling cases.

### 6.1. Comparison under the no-idling case

The computational results are reported in Tables 1-3. Note that each cell contains the averages of the 5 replicates for each one of the 10 instances of each $n \times m$ combination ( 50 values averaged at each cell).

It can be easily seen from Table 1 that, for the shortest elapsed CPU time of $\rho=100$, the proposed EDA is the best performed with the lowest ARPI of just $0.25 \%$, which is significantly smaller than all other results. More interestingly, the EDA achieves the best ARPI values for all 28 problem sizes as well. Compared with the EDA, the $\mathrm{EDA}_{\mathrm{n} 5}$ yields much worse ARPI values for all the 28 problem sizes and a much larger overall ARPI value, which suggests that taking advantage of the speed-up method in the proposed EDA is very beneficial. However, $\mathrm{EDA}_{\mathrm{n} 5}$ is still better than all other methods. On the other hand, both EDA and $\mathrm{EDA}_{\mathrm{n} 5}$

Table 1
Comparison of algorithms at no-idling case $(\rho=100)$.
Table 2
Comparison of algorithms, no-idling case $(\rho=200)$.
significantly improve each ARPI value generated by the $\mathrm{EDA}_{n L}$, which demonstrates the effectiveness of incorporating a local search into the EDA variant. In other words, the superiority of the

Table 3
Comparison of algorithms, no-idling case ( $\rho=300$ ).
![img-5.jpeg](img-5.jpeg)

Fig. 6. Means plot and 95\% Tukey HSD confidence intervals for the interaction between the algorithms, the maximum elapsed CPU time $\rho$ and the no-idling/idling cases.

The computational results with $\rho=200$ and 300 are reported in Tables 2 and 3, respectively. It is clear from these tables that the results are again favorable.

The presented EDA makes extensive use of some advanced techniques such as an efficient population initialization, a newly designed probabilistic model, a diversity controlling mechanism, and hybridization with local search. These techniques are in favor of the EDA transferring the building blocks of jobs in parents to offspring, maintaining diversity of population, having higher local exploitation ability. In addition, the presented speed-up technology makes the EDA much more effective. Thus the EDA can achieve better performance than the other algorithms at several different levels. Note that in the comprehensive experiments, EDA
is compared against other EDA methods (EDA) and other GAs. Basically, the differences in efficiency and effectiveness cannot be solely attributed to the fact that we are presenting an EDA method but more precisely to the efficient and effective instantiation of the EDA method for the considered problem.

### 6.2. Comparison under the idling case

Results for the three different stopping times are given in Tables $4-6$. It is clear from the these results that the proposed EDA outperforms the existing methods of the comparison by a considerable margin for the lot-streaming flow shop scheduling problem with setup times to minimize makespan under the idling case. Quite

Table 4
Comparison of algorithms, idling case $(\rho=100)$.
Table 5
Comparison of algorithms, idling case $(\rho=200)$.
interestingly, the additional elapsed CPU time does not seem to affect the proposed EDA method. The conclusion is that the presented EDA is capable of reaching good solutions very quickly and stagnates around very good solutions that are probably close to optimal.

### 6.3. Statistical assessment of results

While the results in all previous tables show strong differences between the proposed EDA and all the considered methods, it is

Table 6
Comparison of algorithms, idling case $(\rho=300)$.
still necessary to carry out a statistical experiment to attest if the observed differences are indeed statistically significant. We have carried out a full factorial ANOVA where $n, m$, instance number, replicate, $\rho$, the type of algorithm and idling/no-idling factors are considered. There are important statistically significant differences. Fig. 6 shows a three-way interaction between the type of algorithm, the maximum elapsed CPU time factor $\rho$ and idling and no-idling cases. We are now employing a $95 \%$ confidence level and we are using Tukey HSD confidence intervals. Note that overlapping intervals denote a statistically insignificant difference in the plotted means. From the figure it is clear that the proposed EDA produces results that are statistically better than all the considered algorithms. It is also shown that the EDA shows statistically insignificant differences with more allotted CPU time. i.e., $\rho=200$ or $\rho=300$ result in no additional gains. Most other methods improve results with additional elapsed CPU time.

As a result, we can safely conclude that the proposed EDA is a new effective algorithm for the lot-streaming flow shop scheduling problem with sequence-dependent setup times and makespan criterion in both the idling and no-idling cases.

## 7. Conclusions

This paper studies the flow shop scheduling problem under the lot-streaming generalization and with sequence-dependent setup times. The studied objective is makespan minimization. This problem has important applications in textile, plastic, chemical, semiconductor, and many other industries where jobs are actually batches of many identical products to be manufactured. A novel estimation of distribution algorithm (EDA) has been proposed for the problem under both the idling and no-idling cases. To the best of our knowledge, this is the first attempt at solving the problem considered, and this is also the first reported application of EDA for solving lot-streaming flow shop scheduling problems. An extensive comparison has been carried out for the proposed EDA against the best existing metaheuristics developed for lotstreaming flow shop problems, as well as against a recently presented EDA for the traditional flow shop problem with total flow time criterion. According to the computational results and statistical analyses, the proposed EDA clearly outperforms all the other considered algorithms by a considerable margin for the lotstreaming flow shop problem with setup times to minimize makespan.

The superiority of the presented EDA is mainly due to the fact that it extensively uses some advanced techniques such as an efficient population initialization, a newly designed probabilistic model, a diversity controlling mechanism, hybridization with local search, and a speed-up procedure. The population initialization mechanism provides an initial population with a high level of quality and diversity. The presented probabilistic model helps in transferring the building blocks of jobs in parents to offspring. The diversity controlling mechanism aims at maintaining the diversity of the population and without it the algorithm stalled after just a few iterations. The hybridization with local search not only enhances the algorithm's local exploitation ability, but also provides an appropriate balance between exploration of the global search and exploitation of the local search. The presented speed-up method improves the search efficiency by a significant margin.

The proposed EDA can be extended to take into account more realistic aspects of the lot-streaming problem, such as the existence of due dates, machine eligibility, parallel machines, multiple objectives and many others. Late work criteria are being actively studied nowadays, as the study of Sterna [52] attests. The proposed EDA can also be generalized to solve other combinatorial optimization problems including the hybrid flow shop, job shop, the traveling salesman or complex scheduling problems as those studied in Manaa and Chu [25], Ruiz-Torres et al. [47] or Gribkovskaia et al. [13]. Specific hybrid flow shops as the ones

approached in Samarghandi and EIMekkawy [49] or in Besbes et al. [5] are equally interesting. Some other single machine problems with many added constraints, as the one studied in Valente and Schaller [57] seem a promising venue of research for the application of the techniques studied in this paper. Of course, each problem would need special tailoring and experimentation and this is the basis for future research.

## Acknowledgments

This research is partially supported by the National Science Foundation of China (60874075, 70871065), and Science Foundation of Shandong Province in China under Grant BS2010DX005, and Postdoctoral Science Foundation of China under Grant 20100480897. Rubén Ruiz is partially funded by the Spanish Ministry of Science and Innovation, under the project "SMPA-Advanced Parallel Multiobjective Sequencing: Practical and Theoretical Advances" with reference DPI2008-03511/DPI and by the IMPIVA-Institute for the Small and Medium Valencian Enterprise, for the project OSC with references IMIDIC/2008/ 137, IMIDIC/2009/198 and IMIDIC/2010/175.
