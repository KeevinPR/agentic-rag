# Relational Bayesian Optimization for Permutation 

Bo-Wei Huang<br>Taiwan Evolutionary Intelligence Laboratory National Taiwan University<br>r10921099@ntu.edu.tw<br>Hsu-Chen Liao<br>Taiwan Evolutionary Intelligence Laboratory<br>National Taiwan University<br>r10921118@ntu.edu.tw

## ABSTRACT

Relational Bayesian optimization for permutation (RBOP) is a new permutation estimation of distribution algorithm proposed in this paper. RBOP uses binary relations to represent the common property in permutations. Inspired by the Bayesian optimization algorithm, RBOP first builds a Bayesian network using binary relations. Then, RBOP samples genes using the most certain edge in the Bayesian network. In the scenario of black-box optimization, RBOP aims to solve various permutation problems with a limited number of function evaluations. Experiments show that in terms of average relative percentage deviation, RBOP outperforms edge histogram-based sampling algorithm on quadratic assignment problems, permutation flow shop problems and linear ordering problems. Additionally, RBOP also outperforms both node histogram-based sampling algorithm and kernels of Mallows model using Cayley distance on traveling salesman problems, permutation flow shop problems, linear ordering problems and 6 out of 10 instances of quadratic assignment problems.

## CCS CONCEPTS

- Mathematics of computing $\rightarrow$ Evolutionary algorithms.


## KEYWORDS

permutation, estimation of distribution algorithms, binary relation

## ACM Reference Format:

Bo-Wei Huang, Wen-Zhong Fang, Hsu-Chen Liao, and Tian-Li Yu. 2023. Relational Bayesian Optimization for Permutation. In Genetic and Evolutionary Computation Conference Companion (GECCO '23 Companion), July 15-19, 2023, Lisbon, Portugal. ACM, New York, NY, USA, 4 pages. https://doi.org/10.1145/3583133.3590606

## 1 INTRODUCTION

Permutation problems are commonly encountered in various fields, such as scheduling, resource allocation, DNA sequencing and more. In the past, some researchers attempt to use integer estimation of distribution algorithms (EDAs) to solve permutation problems [3].

[^0]
## Wen-Zhong Fang

Taiwan Evolutionary Intelligence Laboratory
National Taiwan University
r10921071@ntu.edu.tw
Tian-Li Yu
Taiwan Evolutionary Intelligence Laboratory
National Taiwan University
tianliyu@ntu.edu.tw
However, permutation has a unique property of mutual exclusivity constraints, which distinguishes it from the integer domain. Directly applying integer EDA to solve permutation problems is not the best solution.

In 2002, Tsutsui proposed a permutation EDA called the edge histogram-based sampling algorithm (EHBSA) [9] and in 2006 the same author proposed another permutation EDA called the node histogram-based sampling algorithm (NHBSA) [10]. These two algorithms perform well on the traveling salesman problem (TSP) and the quadratic assignment problem (QAP), respectively. Additionally, research [3] has shown that permutation EDAs like EHBSA and NHBSA which are specialized for permutations perform much better on other permutation problems than integer or real value EDAs because they do not encounter the same issues that integer EDAs face.

Afterward, the research of permutation EDAs have primarily deviated into two directions. In one of the directions, researchers firstly encode permutation chromosomes into random keys and then use the encoded chromosomes to solve permutation problems by EDAs. In the other direction, researchers incorporate probabilistic models commonly used in ranking fields into the EDA framework to create new permutation EDAs, which are then used to solve permutation problems.

In the research direction of using encoded chromosomes to solve permutation problems, Bosman et al. proposed the permutation gene-pool optimal mixing evolutionary algorithm (PGOMEA) [2] in 2016 and Wozniak et al. proposed P4 [11] in 2020. Both models achieve good results on the permutation flow shop problems (PFSP). The random key-based EDA (RKEDA) [1] proposed by M. Ayodele in 2018 achieved good results on various permutation problems.

In the research direction of incorporating ranking models into the EDA framework, Ceberio et al. incorporated the Plackett-Luce model into the EDA framework [6] and achieved good results on the linear ordering problems (LOP). Furthermore, Ceberio et al. also incorporated the Mallows model into the EDA framework [5]. In the Mallows model EDA (MMEDA) framework, different permutation distances, such as Cayley, Ulam, Kendall's- $\tau$ and Hamming, result in different performances on permutation problems with different semantics [4].

These previously proposed permutation EDAs show varying performance on problems with different semantics. Under the scenario of black-box optimization, this paper aims to break down the permutations into more fine-grained relations for adapting to the unique semantics of different problems. To achieve this goal, this


[^0]:    Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s).
    GECCO '23 Companion, July 15-19, 2023, Lisbon, Portugal
    (c) 2023 Copyright held by the owner/author(s).

    ACM ISBN 979-8-4007-0120-7/23/07.
    https://doi.org/10.1145/3583133.3590606

paper proposes a general EDA called relational Bayesian optimization for permutation (RBOP). Inspired by the Bayesian optimization algorithm (BOA) [8] in the binary domain, RBOP uses binary relations to represent the characteristic of the permutation problems and constructs a Bayesian network for information from promising chromosomes. The next generation of the population is sampled using the network.

The remainder of this paper is organized as follows. Section 2 details RBOP. Section 3 describes the experiments and demonstrates the results. Section 4 concludes this paper.

## 2 METHODOLOGY

In this section, we first introduce a common property in the permutation domain, which is represented using binary relation. Then, we present the framework of RBOP.

### 2.1 Binary relation

![img-0.jpeg](img-0.jpeg)

Figure 1: An example of using binary relation to represent the relation between genes.

In the permutation domain, there is a common property that can not only express the relative position between two elements and the distance between them, but also the absolute position of an element in the permutation. For instance, in a job scheduling problem, job A may need to be executed 3 jobs after job B. Furthermore, if we already know that job C is the $5_{t h}$ job to be executed, and if job D needs to be executed 3 jobs after job C , then we can conclude that job D is the $8_{t h}$ job to be executed.

RBOP decomposes permutations into the previously mentioned properties and express them using binary relations. If there is a start gene with value $A$ and an end gene with value $B$, and the distance between $A$ and $B$ is $d$, then this relationship is expressed as $(A, d, B)$.

In addition, we use graphs to represent binary relations in the following sections, as shown in Figure 1. Each gene is represented as a node in the graph and is denoted by the tuple (index, value) in Figure 1. The value of the distance between two genes is defined as
the number of positions the end gene is after the start gene. Additionally, we consider each chromosome to have circular properties for consistency in representation. The distance between two genes is formulated as follows:

$$
\text { distance }=\left(\text { end }_{i d x}-\text { start }_{i d x}\right) \quad \bmod l
$$

where end $_{i d x}$ is the index of the end gene, start $_{i d x}$ is the index of the start gene, $l$ is the problem size.

### 2.2 The framework of RBOP

The framework of RBOP is similar to most EDA frameworks, consisting of the learning stage and the sampling stage. During the learning stage, RBOP learns the binary relations from the promising chromosomes and constructs a matrix to store the information.

In the sampling stage, RBOP starts by randomly selecting a parent chromosome from the population and deciding which genes to sample and which to inherit from the parent chromosome. The genes inherited from the parent chromosome serve as start genes to determine the values of genes that need to be sampled. After deciding which parent chromosome is used and which genes need to be sampled, RBOP builds a unique network using the parent chromosome and genes. Figure 3 is an example network constructed using the parent chromosome $P_{T}$ and the binary relation matrix $m$ in Figure 2.

After building the graph, BRBOP uses the edge with the minimum entropy in the graph to sample the gene that needs to be sampled and determine the probability distribution of the possible gene values in a Bayesian manner. After sampling each gene, RBOP removes the edges connected to the previously sampled node in the graph and updates the entropy of the remaining edges.

## 3 TEST PROBLEMS AND EXPERIMENTS

In this section, the test problems used in this paper are introduced. Then, the experiment setup is detailed. Finally, the results between different models on four optimization problems and the discussion are presented.

### 3.1 Test problems

In this subsection, we introduce four widely used [1,3,10] permutation problems, namely TSP, QAP, PFSP and LOP, and their different problem characteristics.

TSP is a classic NP-Complete problem focusing on the adjacency relation of each element in the permutation. The objective of this problem is to find the shortest path that can visit every city exactly once.

QAP emphasizes the absolute position of each element in the permutation. The objective of QAP is to assign facilities to locations such that the sum of the products of the distances and the flow between each facility and location is minimized.

PFSP is a problem that aims to minimize the total time required to complete all jobs using a set of machines. The fitness value in PFSP depends on both the processing time of each job and the order of the previously scheduled jobs [4].

LOP is a maximization problem that the contribution of an index $\pi_{i}$ to the fitness function depends on the previous and posterior indexes to it [3].

![img-3.jpeg](img-3.jpeg)
end gene value


![img-3.jpeg](img-3.jpeg)

Figure 2: An example of a binary relation matrix, where $P_{0}$ to $P_{4}$ on the left represent the 5 chromosomes in the population, and the 3 matrices on the right are constructed from the population on the left. The bias constant 0.1 is added to the elements in the matrices.
![img-3.jpeg](img-3.jpeg)

Figure 3: An example network constructed using the parent chromosome $P_{T}$ and the binary relation matrix in Figure 2. The circular nodes represent the genes inherited from the parent chromosome, and the rectangle nodes represent the genes that need to be sampled. Gene $X$ and gene $Y$ in the parent chromosome are the genes that need to be sampled.

### 3.2 Experiment setup

The experiment aims to find the most general permutation EDA for solving the permutation problems. In the experiment, the performance of the algorithm is measured using the distance between the best solution found by the algorithm and the optimal solution of the problem instance, namely ARPD. The formula for ARPD is as follows:

$$
A R P D=\left(\sum_{i=1}^{n} \frac{\left(\text { Algorithm }_{i}-\text { Best }\right) \times 100}{\text { Best }}\right) \times \frac{1}{n}
$$

where Algorithm $_{i}$ is the best solution found by the model each time, Best is the optimal solution of the problem instance and $n$ is the number of repetitions.

Three permutation EDAs are chosen to compare the performance with RBOP. Firstly, NHBSA and EHBSA are not only milestones
permutation EDAs but are also often used for comparison with other EDAs. Their performance is comparable to or even outperforms that of RKEDA [1], so NHBSA and EHBSA are compared with RBOP. KMMEDA is selected to compare the performance with RBOP because KMMEDA shows the best performance among all variants of MMEDA. In the black-box optimization scenarios, KMMEDA is incorporated with Cayley distance due to its relatively good performance compared to Kendall's- $\tau$ distance on both PFSP and QAP [7].

For fair comparison, we sweep the population size for each model to find the optimal population size for that model. For the problem instances, the experiment selects 10 instances from TSPLIB, QAPLIB, LOLIB, XLOLIB, and Taillard instances.

Table 3 shows the result of RBOP, EHBSA, NHBSA, and KMMEDA on TSP. In comparison to NHBSA and KMMEDA, RBOP produces solutions that are closer to the optimal solution in all TSP instances.

Table 1: The performance (ARPD) of RBOP, EHBSA, NHBSA, and KMMEDA on TSP.
Table 4 shows the result of RBOP, EHBSA, NHBSA, and KMMEDA on QAP. For QAP, RBOP outperforms EHBSA in all instances, KMMEDA in 6 out of 10 instances, and even NHBSA in 6 out of 10 instances. This demonstrates that the absolute relation in the permutations can be effectively decomposed.

Tables 5 and 6 show the results of RBOP, EHBSA, NHBSA, and KMMEDA on PFSP and LOP. Although the problem characteristics of PFSP and LOP are not as clearly decomposable into smaller

Table 2: The performance (ARPD) of RBOP, EHBSA, NHBSA, and KMMEDA on QAP.
relations as TSP and QAP, RBOP finds the closest solutions in all instances of PFSP and finds the closest solutions in larger instances of LOP. This proves that even if the problem characteristics are not clear, RBOP can still solve permutation problems well by decomposing the problem into smaller relations.

Table 3: The performance (ARPD) of RBOP, EHBSA, NHBSA, and KMMEDA on PFSP.
Table 4: The performance (ARPD) of RBOP, EHBSA, NHBSA, and KMMEDA on LOP.
## 4 CONCLUSION

RBOP proposed in this paper utilizes binary relations to adaptively represent the characteristic of the permutation problem and uses the relations as conditional probabilities to construct a Bayesian network from promising chromosomes. To distinguish the important relations from the others, RBOP uses Shannon's entropy to decide which relations are used for sampling new chromosomes. The experiment shows that RBOP obtains the lowest ARPD on average among TSP, QAP, PFSP, and LOP. Hence, when the problem is unknown, RBOP provides relatively closer solutions to the optimal compared to EHBSA, NHBSA, and KMMEDA for solving permutation problems. This paper demonstrates another effort to find a unified model for permutation problems, other than the Mallows distribution. As for future work, we would like to continue our investigation toward finding a more unified adaptive model for permutation problems with different semantics.

## ACKNOWLEDGMENTS

The authors would like to thank the support by the National Science and Technology Council in Taiwan under grant No. NSTC 111-2221-E002-189 and National Taiwan University under grant No. 112L891103.
