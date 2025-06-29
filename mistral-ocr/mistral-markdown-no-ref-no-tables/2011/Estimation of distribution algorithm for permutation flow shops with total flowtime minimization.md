# Estimation of distribution algorithm for permutation flow shops with total flowtime minimization ${ }^{\ominus}$ 

Yi Zhang a,b, Xiaoping Li a,b,»<br>${ }^{a}$ School of Computer Science $\mathcal{E}$ Engineering, Southeast University, 211189 Nanjing, PR China<br>${ }^{\text {b }}$ Key Laboratory of Computer Network and Information Integration (Southeast University), Ministry of Education, 211189 Nanjing, PR China

## A R T I C L E I N F O

Article history:
Received 16 February 2010
Received in revised form 30 November 2010
Accepted 12 January 2011
Available online 18 January 2011

Keywords:
Estimation of distribution algorithm
Permutation flow shops
Total flowtime
Meta-heuristic

## A B S T R A C T

In this paper, an Estimation of Distribution Algorithm (EDA) is proposed for permutation flow shops to minimize total flowtime. Longest Common Subsequence (LCS) is incorporated into the probability distribution model to mine good "genes". Different from common EDAs, each offspring individual is produced from a seed, which is selected from the population by the roulette method. The LCS between the seed individual and the best solution found so far is regarded as good "genes", which are inherited by offspring with a probability less than 100\% to guarantee the population diversity. An effective Variable Neighborhood Search (VNS) is integrated into the proposed EDA to further improve the performance. Experimental results show that the inheritance of good "genes" obtained by LCS can improve the performance of the proposed EDA. The proposed hybrid EDA outperforms other existing algorithms for the considered problem in the literature. Furthermore, the proposed hybrid EDA improved 42 out of 90 current best solutions for Taillard benchmark instances.
(c) 2011 Elsevier Ltd. All rights reserved.

## 1. Introduction

The permutation flow shops (also called permutation flow shop scheduling problem, PFSP for short) has attracted the attentions of many researchers, since Johnson (1954) first introduced it. The target is to discover a permutation of jobs, which are processed over machines with the same machine sequence, in order to optimize one or more performance measures. It is well known that total flowtime minimization leads to stable or uniform utilization of resources, rapid turn-around of jobs and minimization of in-process inventory (French, 1982; Rajendran, 1994).

The PFSP can be denoted as F:prmu: $\sum C_{j}$ which was proved to be NP-hard by Garey, Johnson, and Sethi (1976). Naturally, a practical method is to find a solution as good as possible in acceptable computation time by heuristics rather than to discover an optimal solution. Heuristics can be divided into two classes, constructive and composite. Famous constructive heuristics are BES(LR)(Liu \& Reeves, 2001), WY (Woo \& Yim, 1998), RZ (Rajendran \& Ziegler, 1997) and FL (Framinan \& Leisten, 2003), in which RZ is always used as an inser-tion-based local search method. IH1-IH7 (Allahverdi \& Aldowaisan, 2002), IH7-FL (Framinan \& Leisten, 2003), FLR1 and FLR2 (Framinan, Leisten, \& Ruiz, 2005), ICH1-ICH3(Li, Wang, \& Wu, 2009) are all good composites. As well, meta-heuristics are applied for the considered problem. Vempati, Chen, and Bulllngton (1993) first used a Genetic

[^0]Algorithm (GA) for the considered problem. Zhang, Li, and Wang (2009) proposed a hybrid GA (HGA), in which artificial chromosome is constructed to mine good "genes" implicated in the population. Experimental results showed that this method helps HGA to obtain high performance but much computation time spent. Tseng and Lin (2009) presented a hybrid GA (named HGAYT in this paper), in which two local search methods response for a small and a large neighborhood, respectively. Their experimental results showed that HGAYT is very effective, and discovered many best solutions for the Taillard benchmark instances (1993). Rajendran and Ziegler $(2004,2005)$ presented four Ant-colony Algorithms (ACOs), including the famous PACO and M-MMAS. As well as based on pheromone trail intensities, offspring individuals are produced from a seed, i.e. the best solution found so far. This method benefits the four ACOs to be effective. Tasgetiren, Liang, Sevkli, and Gencyilmaz (2007) Jarboui, Ibrahim, Siarry, and Rebai (2008) investigated a Particle Swarm Optimization algorithm (PSO), called PSOvns and HCPSO respectively, which found many best solutions for the first 90 Taillard benchmark instances. Dong, Huang, and Chen (2009) constructed an Iterated Local Search algorithm (ILS). ILS starts with an initial solution, and then the local search is conducted until no improvement obtained. A perturbation operator is executed to make it jump out of the local optimal. Such a procedure is repeated until the termination criterion is satisfied. ILS is simple and effective, with the performance mostly depending on the effectiveness of the local search. Pan, Tasgetiren, and Liang (2008) proposed a hybrid Discrete Differential Evolutionary algorithm (DDERLS), which is integrated with an effective local search method. Jarboui, Eddaly, and Siarry (2009)


[^0]:    This manuscript was processed by Area Editor T.C. Edwin Cheng.

    * Corresponding author. Tel.: +86 25 52090916.

    E-mail address: xpli@seu.edu.cn (X. Li).

proposed an EDA (named JEDA for short in this paper), in which the probability distribution model was constructed based on the relative orders of jobs and similar blocks of jobs. As well, JHEDA was constructed by combining a Variable Neighborhood Search (JVNS for short) with JEDA. As reported in the literature, relationships among the above meta-heuristics are summarized as follows: (1) PSOvns outperforms PACO and M-MMAS; (2) HGA, ILS, HCPSO, HGAYT, DDERLS and JHEDA are all better than PSOvns; (3) DDERLS and JHEDA are better than HCPSO; (4) JHEDA outperforms HGA.

In fact, EDAs were proposed based on an estimation of distribution recently. EDA is population-based, similar to GA but without crossover and mutation operators. Instead, EDA explicitly extracts the global statistical information from the elite set selected from the parent population. A probability distribution model is constructed to sample new solutions and replace partial or all of the parent population. The well-known EDAs are population-based incremental learning (PBIL) (Baluja, 1994), univariate marginal distribution algorithm (UMDA) (Mühlenbein, 1998), mutual information maximization for input clustering (MIMIC) (De Bonet \& Viola, 1997), combining optimizers with mutual information trees (COMIT) (Baluja \& Davies, 1998), Bayesian optimization algorithm (BOA) (Pelikan, Goldberg, \& Cantu, 1999), Bayesian evolutionary algorithm (BEA) (Zhang, 1999), iterated density estimation evolutionary algorithm (IDEA) (Bosman \& Thierens, 2001), and global search based on reinforcement learning agents (GSBRL) (Miagkikh \& Punch, 1999). Considering the location information of solutions found so far, Zhang, Sun, and Tsang (2005) proposed an EDA called EA/G, in which a new operator (Guided Mutation, GM for short) was constructed to generate offspring individuals. In GM, all elements of the best solution found so far can be inherited by the offspring individuals probabilistically. By this method, EA/G outperforms the famous algorithm MIMIC. Theoretically, the convergence of PBIL, UMDA and FDA was proved by Hohfeld and Rudolph (1997), Mühlenbein (1998), Zhang and Mühlenbein (2004), respectively. As well, EDAs have been applied in many areas, such as pattern recognition (Inza, Larranaga, \& Etxeberria, 2000; Cesar, Bengoetxea, Bloch, \& Larrangaga, 2005), software testing (Sagarna \& Lozano, 2005), cancer classification (Blanco, Larranaga, \& Inza, 2004), and operational research (Zhang, Sun, Tsang, \& Ford, 2004).

In this paper, we propose an EDA (PEDA for simplicity) for the considered problem. In PEDA, the Longest Common Subsequence (LCS), which discovers the common information between two given sequences, is incorporated into the probability distribution model in order to mine good "genes". This idea is inspired by the fact that good "genes" mining can help GAs to obtain high performance, such as GAs given by Ruiz, Maroto, and Alcaraz (2006) and Zhang et al. (2009). Different from common EDAs, each offspring individual in PEDA is produced from a seed, selected from the current population by the roulette method. The LCS between the seed individual and the best solution found so far is considered as good "genes". However, we found that good "genes" inherited completely could deteriorate the population diversity after testing the GAs given by Ruiz et al. (2006) and Zhang et al. (2009). Though the former is efficient for PFSP with makespan minimization originally, we transformed it for the considered problem in the testing. Therefore, good "genes" should be inherited by offspring with a probability $i(i \in(0,1))$ in order to guarantee the population diversity. In addition, a new VNS is presented based on the JVNS (Jarboui et al., 2009) and employed as the local search to further improve the performance. Experimental results show that the LCS helps PEDA to outperform JEDA. The hybrid PEDA (PHEDA for short) is better than all of the existing algorithms for the considered problem in the literature, and can provide some new upper bounds of the benchmark instances given by Taillard (1993).

The rest of this paper is organized as follows: Section 2 gives a brief description of PFSP with total flowtime minimization. PEDA
along with VNS are introduced in Section 3. A full performance evaluation and comparison is shown in Section 4, followed by conclusions in Section 5.

## 2. Description of $F: \operatorname{prmu}: \sum C_{j}$

PFSP is an important combinational optimization problem with characteristics described below:

- $n$ jobs are processed on $m$ machines;
- each job has $m$ operations processed on $m$ machines $M_{1}, \ldots, M_{m}$ sequentially with the same order;
- each operation has predetermined processing time;
- each machine can process one operation exclusively at a time;
- preemption is not allowed;

Let $\Omega=\left\{j_{1}, \ldots, j_{n}\right\}$ be the job set and $\pi$ be a permutation of $n$ jobs, which can be denoted as $\left(\pi_{[1]}, \ldots, \pi_{[n]}\right)$ in which $\pi_{[i]} \in \Omega$ is the $i$ th $(i=1, \ldots, n)$ job in $\pi$. To represent the start of a schedule, a dummy job $\pi_{[0]}$ is introduced and added to the first slot in $\pi$ with zero processing times, i.e. $\pi$ can also be represented as $\left(\pi_{[0]}, \pi_{[1]}, \ldots, \pi_{[n]}\right)$. Let $C_{1, \pi_{i j}}$, be the completion time of job $\pi_{[k]}$ on machine $i$, and $C_{1, \pi_{i j}}=0 . t_{i, j}$ denotes the processing time of job $j(j=0,1, \ldots, n)$ on machine $i(i=1,2, \ldots, m)$. Then $C_{i, \pi_{i j}}$, can be calculated as follows:
$C_{i, \pi_{i j}}= \begin{cases}C_{1, \pi_{[k-1]}}+t_{1, \pi_{i j}}, & i=1, \quad k=1, \cdots, n \\ \max \left(C_{i-1, \pi_{i j}}, C_{i, \pi_{[k-1]}}\right)+t_{i, \pi_{i j}}, & i=2, \cdots, m, \quad k=1, \cdots, n\end{cases}$
The total flowtime $F(\pi)$ can be calculated by $F(\pi)=\sum_{k=1}^{\pi} C_{m, \pi_{i j}}$.

## 3. Proposed estimation of distribution algorithm

Generally, EDAs contain the following steps.

1. Initialization: initial the population and parameters.
2. Probability model construction: select part of the population to generate the elite set, from which the probability model is constructed.
3. Offspring production: sample from the probability model to produce offspring.
4. Local search (optional): act the local search on offspring individuals.
5. Replacement: replace part/all of the individuals in the population by the offspring.
6. Termination criterion check: if the termination criterion is not met, go to step 2 .

Based on the above framework, the proposed hybrid EDA is described in details below.

### 3.1. Representation, population initialization and selection

Permutations of jobs are simply used to encode individuals, which is frequently adopted in the literature. In order to guarantee the diversity of the initial population (denoted as $P_{c}$ ), all the individuals are generated randomly. Such a method is also adopted by Tseng and Lin (2009), and Jarboui et al. (2009). The best $\alpha \times 100 \%(\alpha \in(0,1])$ of the population are selected to construct the elite set (represented as $\Pi_{\pi}$ ), i.e. $\left\lfloor\alpha\left|P_{c}\right|\right\rfloor=\left|\Pi_{\pi}\right|$.

### 3.2. Probability model

### 3.2.1. Global statistical information extraction

The probability distribution model is built based on the global statistic information which is extracted from the elite set. In PEDA,

the "voting" procedure, used by Zhang et al. (2009) \& Chang et al. (2007) as well, is adopted to extract the global statistical information. As details about the "voting" procedure were described by Zhang et al. (2009) \& Chang et al. (2007), respectively, we just summarize some key steps here. For $\pi \in \Pi_{e}$, the number of each job at each position is counted and recorded in a $(n+1)=(n+1)$ "dominance matrix" $M$, in which $M_{[i \mid j j]}=0(i=0,1, \ldots, n)$ and $M_{[i \mid j] j}=0$ $(j=1,2, \ldots, n)$, and $M_{[i \mid j] j}$ denotes the number of job $i$ positioning at slot $j$ in $\Pi_{e}$. Additionally, each $\pi \in \Pi_{e}$ is given a weight according to its objective function (i.e. total flowtime) so that better individuals contribute more greatly to the "dominance matrix". Let $\pi_{m}$ $\left(\pi_{m} \in \Pi_{e}\right)$ be the individual with the worst objective function (i.e., largest total flowtime) in the current elite set, $\pi^{\prime}$ the best solution found so far, the weight of any $\pi \in \Pi_{e}$ can be calculated as follows:
$w_{\pi}=\frac{F\left(\pi_{m}\right)-F(\pi)}{F\left(\pi^{\prime}\right)}$
According to Eq. (2), it is obvious that individuals with lower total flowtime are given larger weights, and the "voting" procedure with the complexity $O\left(n\left(\Pi_{e}\right)\right)$ is described below:

1. $\operatorname{VOTING}\left(\Pi_{e}\right)$ :
2. For each $\pi \in \Pi_{e}$
3. For each position $j$ in $\pi$
4. If $\left(\pi_{[j]}\right.$ is job $\left.i\right)$
5. $\quad M_{[i \mid j]}=M_{[i \mid j]}+w_{\pi}$
6. Return $M$.
7. End VOTING
3.2.2. Longest Common Subsequence (LCS)

Define $\pi \leq \pi_{A}$ to represent that $\pi$ is a subsequence of $\pi_{A}$. The common subsequence can be defined below:
Definition 1 (Cormen, Leiserson, Rivest, \& Stein, 2006). For two given sequence $\pi_{A}$ and $\pi_{B}, \pi$ is a sequence, if $\pi \leq \pi_{A}$ and $\pi \leq \pi_{B}, \pi$ is a common sequence between $\pi_{A}$ and $\pi_{B}$.

Definition 2 (Cormen et al., 2006). For two given sequence $\pi_{A}$ and $\pi_{B}, \Pi_{A B}$ is the set of all common sequence of $\pi_{A}$ and $\pi_{B}$, the longest one in the $\Pi_{A B}$ is the longest common subsequence.

Let $\pi_{A,[s]}$ denote the $i$ th element in the $\pi_{A}$, and $\pi_{A}^{\prime}$ be the sequence including the first $i$ number of elements, i.e. $\pi_{A}^{\prime}=\left(\pi_{A,[1]}, \pi_{A,[2]}, \ldots\right.$, $\pi_{A,[i]}$, the following property describes the LCS structure (Cormen et al., 2006).

Property 1 (Cormen et al., 2006). For two given sequence $\pi_{A}=$ $\left(\pi_{A,[1]}, \pi_{A,[2]}, \ldots, \pi_{A,[p]}\right)$ and $\pi_{B}=\left(\pi_{B,[1]}, \pi_{B,[2]}, \ldots, \pi_{B,[q]}\right), \pi_{C}=\left(\pi_{C,[1]}, \pi_{C,[2]}, \ldots, \pi_{C,[k]}\right)$ is the LCS between $\pi_{A}$ and $\pi_{B}$.
(1) If $\pi_{A,[p]}=\pi_{B,[q]}$, then $\pi_{A,[p]}=\pi_{B,[q]}=\pi_{C,[k]}$ and $\pi_{C}^{p-1}$ is the LCS between $\pi_{A}^{p-1}$ and $\pi_{B}^{p-1}$.
(2) If $\pi_{A,[p]} \neq \pi_{B,[q]}$ and $\pi_{A,[p]} \neq \pi_{C,[k]}$, then $\pi_{C}$ is the LCS between $\pi_{A}^{p-1}$ and $\pi_{B}$.
(3) If $\pi_{A,[p]} \neq \pi_{B,[q]}$ and $\pi_{B,[q]} \neq \pi_{C,[k]}$, then $\pi_{C}$ is the LCS between $\pi_{A}$ and $\pi_{B}^{p-1}$.

The proof was given by Cormen et al. (2006). Property 1 shows that how to generate the LCS between two given sequence $\pi_{A}$ and $\pi_{B}$ depends on three sub-problems: (1) generating the LCS between $\pi_{A}^{p-1}$ and $\pi_{B}^{p-1}$, (2) generating the LCS between $\pi_{A}^{p-1}$ and $\pi_{B}$, and (3) generating the LCS between $\pi_{A}$ and $\pi_{B}^{p-1}$. Furthermore, the recursion procedure implies that sub-problems (2) and (3) depend on the sub-problems of sub-problem (1). This means the LCS generating procedure has the overlapped sub-problem characteristic. So,

Dynamic Programming (DP) can be used to generate the LCS between two given sequences.

Define a $(p+1) \times(q+1)$ matrix $c$, in which $c_{[i \mid j]}$ represents the length of the LCS between $\pi_{A}^{\prime}$ and $\pi_{B}^{\prime}$. And, $c_{[p \mid[q]}$ is the length of the LCS between $\pi_{A}$ and $\pi_{B}$. If $i=0$ or $j=0$, the length of the LCS is 0 . Based on Property 1 , the length of the LCS can be calculated by the following recursive formulation: (seen in Cormen et al. (2006))

$$
c_{[i \mid j]}= \begin{cases}0 & \text { if } i=0 \text { OR } j=0 \\ c_{[i-1 \mid j-1]}+1 & \text { if } \pi_{A,[i]} \equiv \pi_{B,[j]} \text { AND } i, j>0 \\ \max \left(c_{[i-1 \mid j]}, c_{[i \mid j-1]}\right) & \text { if } \pi_{A,[i]} \neq \pi_{B,[j]} \text { AND } i, j>0\end{cases}
$$

Based on Formulation (4), the matrix $c$ can be obtained by the following procedure (Cormen et al., 2006).

1. LENGTH_LCS $\left(\pi_{A}, \pi_{B}\right)$
2. $p \leftarrow\left|\pi_{A}\right| ; q \leftarrow\left|\pi_{B}\right|$.
3. $c_{[i \mid j j] \leftarrow} 0(i=1,2, \cdots, p), c_{[i \mid j] j] \leftarrow} 0(j=0,1, \cdots, q)$.
4. For $i \leftarrow 1$ to $p$
5. For $j \leftarrow 1$ to $q$
6. If $\left(\pi_{A,[i]}=\pi_{B,[j]}\right)$ then $c_{[i \mid j] \leftarrow c_{[i-1 \mid j-1]}+1, b_{[i \mid j] \leftarrow} \cdots \cdots "}$.
7. Else if $\left(c_{[i-1 \mid j]}\right) \geqslant c_{[i \mid j-1]}$ ) then $c_{[i \mid j] \leftarrow c_{[i-1 \mid j]}, b_{[i \mid j] \leftarrow} " \uparrow "$.
8. Else $c_{[i \mid j] \leftarrow} c_{[i \mid j-1]}, b_{[i \mid j] \leftarrow} \cdots " \leftarrow "$.
9. Return $c$ and $b$.
10. END LENGTH_LCS

It is obvious that the complexity of this procedure is $O(p q)$. Besides the matrix $c$, a $(p+1) \times(q+1)$ matrix $b$ is also constructed, which records the "path" to generate the LCS. The generation of LCS starts from $b_{[p \mid[q]}$ and follows the arrow symbols (i.e. " $\backslash$ ", " $\uparrow$ " or " $\leftarrow$ ") $b_{[i \mid j]}$ records. $b_{[i \mid j]}=$ " $\backslash$ " implying $\pi_{A,[s]}=\pi_{B,[s]}$ is one element of the LCS. The following recursive procedure (Cormen et al., 2006) is adopted to generate the LCS when matrixes $b$ and $c$ have already been obtained by the LENGTH_LCS procedure.

1. FLCS_OUTPUT $\left(b, \pi_{A} j, j, \pi_{C}\right) /{ }^{\prime} i=0,1, \cdots, p$ and $j=0,1, \cdots, q^{\prime} j$
2. If $(i=0$ or $j=0)$ then return.
3. If $\left(b_{[i \mid j]}=" \backslash " /\right)$ then FLCS_OUTPUT $\left(b, \pi_{A}, i-1, j-1, \pi_{C}\right)$, add $\pi_{A,[s]}$ into $\pi_{C}$.
4. If $\left(b_{[i \mid j]}=" \uparrow " /\right)$ then FLCS_OUTPUT $\left(b, \pi_{A}, i-1, j, \pi_{C}\right)$.
5. If $\left(b_{[i \mid j]}=" \leftarrow " /\right)$ then FLCS_OUTPUT $\left(b, \pi_{A}, i, j-1, \pi_{C}\right)$.
6. END FLCS_OUTPUT

In the procedure, $\pi_{C}$ is an input sequence with the value of "Null". When the procedure finishes, $\pi_{C}$ is the LCS. Since either $i$ or $j$ decreases in each recursion, the complexity of FLCS_OUTPUT is $O(p+q)$. The following complete procedure generates the LCS between two given sequences $\pi_{A}$ and $\pi_{B}$.

1. FLCS $\left(\pi_{A}, \pi_{B}\right)$
2. Use LENGTH_LCS $\left(\pi_{A}, \pi_{B}\right)$ to generate the two matrixes $b$ and $c$.
3. $\pi_{C} \leftarrow$ Null.
4. Perform FLCS_OUTPUT $\left(b, \pi_{A}, p, q, \pi_{C}\right)$ to construct $\pi_{C}$.
5. Return $\pi_{C}$.

## 6. END FLCS

It is obvious that the complexity of FLCS is $O(p q)$. For the considered problem, each sequence is a job permutation with the length $n$. Therefore, the complexity of FLCS becomes $O\left(n^{2}\right)$. An example is used to show the details of FLCS. In this example, $\pi_{A}=(1,2,3,4,5,6,7)$ and $\pi_{B}=(2,5,3,7,4,6,1)$. Fig. 1 shows the two matrixes $b$ and $c$ obtained by the procedure LENGTH_LCS.

In Fig. 1, the cell at the position $(i, j)$ (i.e. the $i$ th row and the $j$ th column) records the $c_{[i \mid j]}$ and the arrow symbol in $b_{[i \mid j]}$. The length

Fig. 1. The matrixes $b$ and $c$ obtained by LENGTH_LCS.
of the LCS between $\pi_{A}$ and $\pi_{B}$ is 4 , which is recorded in the cell at $(7,7)$. The generation of LCS starts from the cell at $(7,7)$ as well, and follows the arrow symbol recorded in cells until reaching the cell at $(1,0)$. As a result, a path (highlighted in Fig. 1) is constructed. In this path, the cells containing the arrow symbol " $\because$ " correspond to the elements of LCS. So, the LCS $(2,3,4,6)$ can be obtained, which is shown in bold in Fig. 1.

### 3.3. Offspring production

Based on the probability distribution model, each offspring individual in PEDA is produced from a seed. The $\beta \times 100 \%(\beta \in(0,1])$ of the current population are selected by the roulette method to construct a seed set $\Pi_{s}\left[\left|\Pi_{s}\right|=\left\lfloor\beta\left|P_{s}\right|\right\rfloor\right)$, without a replication. The LCS between each $\pi_{k} \in \Pi_{s}(k=1,2, \ldots,\left|\Pi_{s}\right|)$ and the best solution found so far $\pi^{*}$ is regarded as good "genes", and denoted as $\pi_{k}^{\prime}$. By experiments, we find that good "genes" completely inherited by offspring always deteriorates the population diversity, while testing both the GAs given by Ruiz et al. (2006) \& Zhang et al. (2009). The former, originally for the PFSP with makespan minimization, was transformed to the considered problem in our testing. The replacement of the GA (Ruiz et al., 2006) is also used in the proposal. Results showed that all the individuals in the final population were similar. And, when the second condition (see Section 3.4) was removed from the replacement, more than $90 \%$ individuals in the final population are identical to the final solution. For the latter, over $95 \%$ individuals in the final population are identical to the final solution. These facts indicate that completely inheriting good "genes" by offspring deteriorates the population diversity, and results in premature and poor performances. To guarantee the population diversity, good "genes" (i.e. $\pi_{k}^{\prime} \cdot(k=1,2, \ldots,\left|\Pi_{s}\right|)$ ) are inherited by offspring with a probability $\lambda(\lambda \in(0,1))$ in this paper. Let $\pi_{k, j j}$ be the $j$ th job in $\pi_{k}$. For any $\pi_{k} \in \Pi_{s}(k=1,2, \ldots,\left|\Pi_{s}\right|)$, if $\pi_{k, j j} \in \pi_{k}^{\prime}(j=1,2, \ldots, n)$, job $\pi_{k, j j}$ is copied to the position $j$ in the offspring individual $\pi_{n}$ with a probability $\lambda$. Then, each unassigned position $j$ in $\pi_{n}$ is set as the job $i$, which is selected from the unscheduled job set $\Omega_{u}$ with the probability $\sum_{n=0}^{\mathrm{M}_{\mathrm{su}}} \mathrm{M}_{\mathrm{s}, j}$. The offspring production procedure can be described as follows:

1. PRODUCTION $\left(\pi_{k}, \pi_{k}^{\prime}\right)$
2. $\pi_{n} \leftarrow$ Null. /"offspring initialization*/
3. For $j \leftarrow 1$ to $n$
4. Generate a uniform distributed random number $\mu(\mu \in$ $[0,1])$.
5. If $\left(\pi_{k, j j} \in \pi_{k}^{\prime}\right.$ AND $\mu \in \lambda)$
6. Insert $\pi_{k, j j}$ to the position $j$ of $\pi_{n}$.
7. $\Omega_{u} \leftarrow \Omega_{u}-\left(\pi_{k, j j}\right)$.
8. For each unassigned position $j$ in $\pi_{n}$
9. Select job $i$ from $\Omega_{u}$ with probability $\sum_{n=0}^{\mathrm{M}_{\mathrm{su}}} \mathrm{M}_{\mathrm{s}, j}$.
10. Insert job $i$ to the position $j$ of $\pi_{n}$.
11. $\Omega_{u} \leftarrow \Omega_{u}-\{i\}$.
12. Return $\pi_{n}$.
13. End PRODUCTION

Since the "dominance matrix" $M$ and the LCS $\pi_{k}^{\prime \prime}(k=1,2, \ldots$, $\left|\Pi_{s}\right|)$ have already been generated prior to PRODUCTION, the complexity of PRODUCTION is $O\left(n^{2}\right)$.

### 3.4. Replacement

In the proposed PEDA, the replacement procedure given by Ruiz et al. (2006) is adopted, and it was also used by Jarboui et al. (2009). An offspring individual replaces with the worst one in the current population as long as both of the following conditions being satisfied: (1) it is better than the worst one, and (2) no identical one already existing in the current population. It is obvious that this replacement not only improves the population quality but also keeps the population diversity.

### 3.5. Local search

To further improve the performance, a Variable Neighborhood Search algorithm (VNS) is employed as the local search in PHEDA. VNS is acted on offspring individuals with a probability Penh (Penh $\in[0,1]$ ) to balance the global search and the local search. Two effective neighborhood local search methods, insert_local_search and swap_local_search introduced by Jarboui et al. (2009), are adopted in VNS. However, the perturbation operator in JVNS generally conducted on the best solution found so far traps JVNS

into the local optimal. Therefore, an acceptance criterion is added to the proposed VNS. As well, a perturbation operator is incorporated by repeating $d$ rounds the following procedure: randomly removing a job from the current permutation and reinserting it at a random position. This procedure is quite different from the perturbation operator in the IG given by Ruiz \& Stützle (2007, 2008), in which $d$ jobs are removed randomly to generate a list, and all the jobs in this list are reinserted sequentially by the NEH way (Nawaz, Enscore, \& Ham, 1983).

In the proposed VNS, insert_local_search and swap_local_search are iterated on the current sequence $\pi_{c}$ until no improvement could be made. If the obtained solution $\pi_{r}$ is better than the best so far $\pi_{c}^{\prime \prime}$ in VNS (maybe $\pi_{c}^{\prime}$ is different from $\pi^{\prime \prime}$ ), $\pi_{r}$ is absolutely accepted. Set $\pi_{c}^{\prime} \leftarrow \pi_{r}$, and conduct the perturbation operator on $\pi_{r}$. The resulted sequence updates $\pi_{c}$. Otherwise when $F\left(\pi_{r}\right) \geqslant$ $F\left(\pi_{c}^{\prime}\right), \pi_{r}$ is accepted only with probability $\gamma(\gamma \in(0,1])$. The above procedure is repeated until the termination criterion is satisfied. Similar to that of Jarboui et al. (2009), the termination criterion is set as 50 consecutive iterations without improvement. The perturbation operator and VNS are given below:

1. PERTURBATION $(\pi)$
2. $\pi_{c} \leftarrow \pi$.
3. For $i \sim 1$ to $d$
4. A job is randomly removed from $\pi_{c}$ and reinserted into $\pi_{c}$.
5. Return $\pi_{o}$.
6. End PERTURBATION
7. $\operatorname{VNS}(\pi)$
8. $\pi_{r} \leftarrow \pi, \pi_{c} \leftarrow \pi, \pi_{c}^{\prime} \leftarrow \pi$.
9. While (termination is not satisfied)
10. While (improvement obtained)
11. $\pi^{\prime} \leftarrow$ insert_local_search $\left(\pi_{c}\right)$.
12. $\pi_{c} \leftarrow$ swap_local_search $\left(\pi^{\prime}\right)$.
13. If $\left(F\left(\pi_{c}\right) \times F\left(\pi_{r}\right)\right)$ then $\pi_{r} \leftarrow \pi_{c}$.
14. If $\left(F\left(\pi_{r}\right) \subset F\left(\pi_{c}^{\prime}\right)\right)$ then
15. $\pi_{c}^{\prime} \leftarrow \pi_{r}$.
16. $\pi_{r} \leftarrow$ PERTURBATION $\left(\pi_{r}\right)$.
17. $\pi_{c} \leftarrow \pi_{r}$.
18. Else
19. Generate a uniform distributed random number $\mu(\mu \in[0,1])$.
20. If $(\mu \leqslant \gamma)$ then
21. $\pi_{r} \leftarrow$ PERTURBATION $\left(\pi_{r}\right)$.
22. Else
23. $\pi_{r} \leftarrow$ PERTURBATION $\left(\pi_{r}^{\prime}\right)$.
24. $\pi_{c} \leftarrow \pi_{r}$.
25. Return $\pi_{r}^{\prime}$.
26. End VNS

### 3.6. Description of the proposed EDA

From the above analysis, the proposed EDA can be formally described as follows.

1. EDA:
2. Initial parameters $\alpha, \beta, \gamma, \lambda, d$ and Penh.
3. Generate population $P_{c}$ and select the best one as $\pi^{\prime \prime}$.
4. While (termination is not satisfied)
5. Select the best $\left\{\alpha \mid P_{c} \mid\right\}$ individuals from $P_{c}$ and construct $\Pi_{c}$.
6. $M \leftarrow \operatorname{VOTING}\left(\Pi_{c}\right)$.
7. Select $\left\{\beta \mid P_{c}\right\}$ individuals from $P_{c}$ to generate $\Pi_{c}$ by the roulette method.
8. For each $\pi_{k}$ in $\Pi_{c}\left\lceil\left\ulcorner k=1,2, \cdots,\right| \Pi_{c}\right\ulcorner\ulcorner$
9. $\pi_{k}^{\prime \prime} \leftarrow F L C S\left(\pi_{k}, \pi^{\prime}\right)$.
10. $\pi_{o} \leftarrow$ PRODUCTION $\left(\pi_{k}, \pi_{k}^{\prime \prime}\right)$.
11. VNS is performed on $\pi_{o}$ with probability Penh.
12. Apply the replacement to update $P_{c}$.
13. Select the best one in $P_{c}$ as $\pi^{\prime \prime}$.
14. Return $\pi^{\prime \prime}$.
15. End EDA

## 4. Computational results

In the section, parameters of PHEDA are determined by experiments. Performance is evaluated by comparing it with other existing good algorithms for the considered problem.

### 4.1. Parameter determination

Parameters $\alpha, \beta, \gamma, \lambda, d$ and Penh should be well determined. $\alpha$ exerts influence on the elite set, which provides information for the probability distribution model. A small $\alpha$ may lead insufficient information provided. On the other side, a large one indicates some poor individuals participate in the "voting" and send "bad messages" to the "dominance matrix". $\beta$ determines the size of the seed set, each of which will be matched with the best solution found so far to mine good "genes". A small $\beta$ leads to obtain only a few good "genes" while a large value implies that poor individuals could be involved in. $\gamma$ is the acceptance probability. The larger value it is, the more poor individuals may be accepted with high probabilities. And, a low value decreases the effects of the acceptance criterion. $\lambda$ is the probability of good "genes" inherited by offspring. A large value deteriorates the population diversity. On the contrary, good "genes" may be lost. $d$ determines the perturbation strength. The larger it is, the more powerful the strength is. Penh is the probability of local search conducted on offspring individuals, which balances the global search and the local search. In this paper, the famous Design of Experiments (DoE) approach (Montgomery, 2000) is adopted to investigate the best parameter setting for the proposal. The value domains of these parameters are set as $\alpha \in(0.1,0.3,0.5), \beta \in(0.1,0.2,0.3), \gamma \in(0.01,0.03,0.05), \lambda \in$ $(0,0.2,0.5,0.8,1.0), d \in(1,2,3)$ and Penh $\in(0.01,0.015,0.03)$, respectively. So, there are $5 \times 3^{3}=1215$ combinations totally, all of which are tested. The two specific situations with $\lambda=0$ and $\lambda=1$ are included with the purpose to show the impacts of $\lambda, \lambda=0$ means no good "genes" inheritance, whereas $\lambda=1$ denotes good "genes" are inherited by offspring completely, which is similar to the GAs given by Ruiz et al. (2006) \& Zhang et al. (2009).

PHEDA is implemented in Java and tested on a PC with P4 2.93 GHz CPU \& 512M Memory. The Taillard (1993) benchmark instances are considered, which contains 12 groups with size $(n \times m)$ varying from $20 \times 5$ to $500 \times 20$. Each group has 10 instances, and there are 120 instances totally. In the literature, it can be investigated that many recent meta-heuristics (four ACOs given by Rajendran \& Ziegler (2004, 2005), PSOvns introduced by Tasgetiren et al. (2007), HCPSO developed by Jarboui et al. (2008), DDERLS proposed by Pan et al. (2008), ILS constructed by Dong et al. (2009), JHEDA investigated by Jarboui et al. (2009) and HGAYT presented by Tseng \& Lin (2009)) are only tested on the first 90 instances, so is the proposed PHEDA. ARPD is adopted to evaluate the performance.
$A R P D=\sum_{i=1}^{R}\left(\frac{\left(S_{i}-S_{\text {best }}\right) \times 100}{S_{\text {best }}}\right) / R$
In Eq. (5), for each instance, $S_{i}$ denotes the solution generated by the compared algorithms, $R$ is the number of replications and $S_{\text {best }}$ represents the best one among the results obtained by all the compared algorithms during the $R$ replications. Due to the same $S_{\text {best }}$ used, ARPD reflects the performance of algorithms. The lower

![img-0.jpeg](img-0.jpeg)

Fig. 2. Means plot for Penh factor, 95.0\% LSD intervals.
![img-1.jpeg](img-1.jpeg)

Fig. 3. Means plot for $\gamma$ factor, $95.0 \%$ LSD intervals.
![img-2.jpeg](img-2.jpeg)

Fig. 4. Means plot for $\alpha$ factor, $95.0 \%$ LSD intervals.

ARPD is, the higher the performance is. In the experiment, $R=10$ and the termination criterion is set as $(n \times m / 2) \times 30 \mathrm{~ms}$ maximum computation time. Setting the time limitation in this way allows the more computation time as the job number or the machine number increases. And, this method is also adopted by many researchers,
such as Jarboui et al. (2009), Ruiz \& Stützle (2007, 2008) \& Ruiz et al. (2006). The experimental results are analyzed by the multifactor analysis of variance (ANOVA) method. In the experiment, the three main hypotheses (normality, homoskedasticity and independence of the residuals) are checked and accepted. The $p$-values

![img-3.jpeg](img-3.jpeg)

Fig. 5. Means plot for $\beta$ factor, $95.0 \%$ LSD intervals.
![img-4.jpeg](img-4.jpeg)

Fig. 6. Means plot for $d$ factor, $95.0 \%$ LSD intervals.
![img-5.jpeg](img-5.jpeg)

Fig. 7. Means plot for $\lambda$ factor, $95.0 \%$ LSD intervals.
in the experiment are all close to zero, so analyzing the $p$-values is rarely useful. Instead, the F-ratio is focused on, which denotes the ratio between the variance explained by a factor and the unexplained variance. The greater the F-ratio is, the more effect the
factor has on the response variable. Note that the interactions among more than two factors are not considered, since their F-ratios are quite small. The factor with the greatest F-ratio is first analyzed, followed by the second one, and so on. The greatest

![img-6.jpeg](img-6.jpeg)

Fig. 8. Means plot for the interaction between $\lambda$ and $\gamma, 95.0 \%$ LSD intervals.

Table 1
Performance comparisons between PEDA and JEDA (no local search hybridized).

Table 2
Performance comparisons on Taillard benchmark instances.

$F$-ratio corresponds to the factor Penh, and the means plot with the Least Significant Difference (LSD) intervals (at the 95\% confidence level) is given in Fig. 2.

Fig. 2 illustrates that PHEDA with Penh $=0.01$ obtains the significantly best performance, while that with Penh $=0.03$ yields the worst effectiveness.

The factor $\gamma$ has the second greatest $F$-ratio, and the means plot with LSD intervals (at the 95\% confidence level) is given in Fig. 3.

Fig. 3 shows that PHEDA with $\gamma=0.01$ obtains the significantly best performance. PHEDA with a large $\gamma$ value of 0.05 generates the

Table 3
Performance comparisons between PHEDA and HGAYT.

worst effectiveness, and the reason lies in that many poor individuals are accepted.

The three factors ( $\alpha, \beta$ and $d$ ) have similar $F$-ratios, and the means plots with LSD intervals (at the 95\% confidence level) are given in Figs. 4-6, respectively.

In Fig. 4, it can be seen that PHEDA with $\alpha=0.3$ obtains the significantly best performance. $\alpha=0.1$ yields the worst effectiveness and the reason is that only a few individuals participate in the "voting" procedure and the information is insufficient to construct the probability model. Fig. 5 shows that PHEDA with $\beta=0.2$ obtains the significantly best performance. In Fig. 6, it can be seen that PHEDA with $d=2$ generates the best effectiveness, significantly.

The last factor is $\lambda$, and the means plot with LSD intervals (at the 95\% confidence level) is given in Fig. 7.

In Fig. 7, it can be seen that PHEDA with $\lambda=0.8$ achieves the significantly best performance. PHEDA with $\lambda=0$ generates the worst effectiveness, which implies that the inheritance of good "genes" improves the performance. The performance with $\lambda=1$ is significantly worse than that with $\lambda=0.8$, which indicates that completely inheriting the good "genes" deteriorates the performance.

Interactions between factors are considered as well. The interaction between $\lambda$ and $\gamma$ is focused on, and the means plot with LSD intervals (at the 95\% confidence level) is given in Fig. 8. The other interactions between factors are not studied, since their F -ratios are very small. Fig. 8 illustrates that PHEDA obtains the best performance with the combination of $\lambda=0.8$ and $\gamma=0.01$, which conforms to the previous conclusion.

According to the above analysis, all the six parameters are selected as follows: $\alpha=0.3, \beta=0.2, \gamma=0.01, \lambda=0.8, d=2$ and Penh $=0.01$.

Table 4
Best known solutions for the first 90 Taillard benchmark instances.
# 4.2. Performance of PEDA 

PEDA is compared with JEDA (Jarboui et al., 2009), which is also implemented in Java. Parameters of JEDA are set as $\delta_{1}=\delta_{2}=4 / n$, $Q=O=3$ and the population size is 60 , which are identical to those used in the paper (Jarboui et al., 2009). And, parameters of PEDA are set as above with the population size being 60 as well for fair comparison. Both algorithms are tested on the same PC with P4 2.93 GHz CPU \& 512M Memory. The first 90 Taillard benchmark
instances are also tested, and the termination criteria for both the algorithms are identically set as $(n \times m / 2) \times 30 \mathrm{~ms}$ maximum computation time. $R=100$ is consistent with that of Jarboui et al. (2009). Results are presented in Table 1.

Table 1 shows that PEDA outperforms JEDA for each group as well as the average on the nine groups, which implies that the incorporation of LCS for good "genes" mining leverages PEDA with high effectiveness. Good "genes" inherited by offspring individuals with the probability $\lambda=0.8$ can maintain the population diversity.

Table 5
Performance comparisons between PEDA_GM and PEDA (no local search hybridized).

This is another important factor benefiting the high performance of PEDA.

### 4.3. Performance of PHEDA

In this subsection, the performance of PHEDA is evaluated by comparing it with other existing meta-heuristics for the considered problem in the literature, including ILS (Dong et al., 2009), DDERLS (Pan et al., 2008), HGAYT (Tseng \& Lin, 2009), and JHEDA (Jarboui et al., 2009). As aforementioned in Section 1, all of these four algorithms outperform PSOvns (Tasgetiren et al., 2007). DDERLS and JHEDA are better than HCPSO (Jarboui et al., 2008), whereas it is claimed that JHEDA outperforms HGA (Zhang et al., 2009). Therefore, PSOvns, HCPSO and HGA are not compared in this paper.

Besides the proposed PHEDA, all the compared algorithms are implemented in Java with identical parameters to those in their papers. The population sizes of DDERLS, JHEDA and PHEDA are all set as 30 and the termination criteria for all of the algorithms are identically set as $(n \times m / 2) \times 90 \mathrm{~ms}$ maximum computation time. The first 90 Taillard benchmark instances are tested as well. $R=5$, which is consistent with most of papers in the literature. Results are given in Table 2.

Table 2 illustrates that PHEDA obtains the best performance both on average and for each group. All the compared algorithms yield good solutions for the first three groups with small sizes, and PHEDA achieves the best performance for ARPD being 0. PHEDA also obtains the best effectiveness for the rest groups, especially for the largest size one (i.e. $100 \times 20$ ). Its ARPD (0.291) is much lower than those of JHEDA ( 0.665 ), ILS (1.231) and DDERLS (1.812). The performance of JHEDA is just inferior to that of PHEDA on average. ILS outperforms DDERLS, which obtains good solutions for the first three groups, whereas rather poor results for the rest ones with large sizes.

To compared with HGAYT, PHEDA is performed again for 10 replications, i.e. $R=10$, which is consistent with Tseng \& Lin (2009). Both algorithms obtain good results for the first three groups, so the rest six groups with large sizes ( $\{50,100\} \times$ $\{5,10,20\}$ ) are mainly tested. In ARPD, $S_{\text {best }}$ represents the upper bounds given by Tseng \& Lin (2009). Additionally, Tseng \& Lin (2009) presented the average total flowtime ("Avg" for short) obtained during their experiments, which can be used directly to calculate the ARPD by the following equation:
$A R P D=\frac{A v g-S_{\text {best }}}{S_{\text {best }}} \times 100 \%$
It is obvious that Eq. (6) is equivalent to Eq. (5), which is used for performance evaluation in this paper. Tseng and Lin used a PC with a CPU AMD K7 1.83 GHz \& 512M Memory, which is reported to be comparable with a computer with CPU P4 2.60 GHz \& 256M Memory (Tseng \& Lin, 2009). So, it seems that our computer (CPU P4 2.93 GHz \& 512M Memory) is a little better than the one used by Tseng
and Lin, but it is well-known that the efficiency of Java is much lower than that of C++. Therefore, totally, our testing environment can be considered to be comparable with that of Tseng \& Lin (2009). In fact, this comparison method was also adopted by Tseng \& Lin (2009) to evaluate the efficiency of their hybrid GA. The termination criterion of PHEDA is set as maximum computation time with values summarized in Table 3.

In Table 3, computation times of HGAYT are all summarized from the paper (Tseng \& Lin, 2009). Table 3 illustrates that PHEDA obtains better performance in shorter computation time than HGAYT does on average. PHEDA generates the best solutions for all testing groups except the $50 \times 5$ group. Furthermore, the best solutions found by the proposed PHEDA are given and compared with the best solutions found so far which were reported by Tseng \& Lin (2009), Dong et al. (2009), Pan et al. (2008), \& Jarboui et al. (2009). The best solutions so far and the corresponding algorithms for the Taillard benchmark instances are shown in Table 4, which illustrates that PHEDA obtains 72 best solutions for the first 90 Taillard benchmark instances, and 42 are newly discovered. By comparing these with the upper bounds given by Tseng \& Lin (2009), it is obvious that PHEDA outperforms HGAYT greatly.

### 4.4. Effectiveness of the proposed PRODUCTION operator

To evaluate the effectiveness of the proposed PRODUCTION operator, it is compared with the GM operator given by Zhang et al. (2005). The main ideas of GM lie in: (1) in each generation, offspring individuals are generated from the same seed, the best solution found so far, (2) elements of each offspring individual are either copied from the corresponding elements of the best solution found so far with probability $\theta$, or sampled from the probability model with probability $1-\theta$. Accordingly, a new GM operator (called PRODUCTION_GM) is constructed for the problem considered in this paper, as GM given by Zhang et al. (2005) is used by an EDA for the maximum clique problem. Let $\pi^{*}$ be the best solution found so far, $\Omega_{n}$ be the set of unassigned jobs, and $\pi_{u}$ represent the offspring individual. For each position $j(j=1,2, \ldots, n)$ in $\pi^{*}$, insert $\pi_{j j}^{*}$ to the position $j$ of $\pi_{u}$ with the probability $\theta$. Then, each unassigned position $j$ in $\pi_{u}$ is set as the job $i$, which is selected from the unscheduled job set $\Omega_{n}$ with probability $\frac{M_{j, i j}}{\sum_{i=0}^{n} M_{j, i j}}$. The PRODUCTION_GM is formally described as follows: $\sum_{i=0}^{n} \pi_{i, j j}$.

1. PRODUCTION_GM $\left(\pi^{*}\right) /$ "the seed is always the best solution found so far $\pi^{*}$ ".
2. $\pi_{u} \leftarrow$ Null. /"offspring initialization"/
3. For $j \leftarrow 1$ to $n /$ "inherit elements of $\pi^{*}$ by the offspring individual"/
4. Generate a uniform distributed random number $\mu(\mu \in$ $[0,1])$.
5. If $(\mu \in \theta)$
6. Insert $\pi_{j j}^{*}$ to the position $j$ of $\pi_{u}$.
7. $\quad \Omega_{n} \leftarrow \Omega_{n}-\left\{\pi_{j j}^{*}\right\}$.
8. For each unassigned position $j$ in $\pi_{u} /$ " sample from the probability model" $/$
9. Select job $i$ from $\Omega_{n}$ with probability $\frac{M_{i, i j}}{\sum_{i=0}^{n} M_{i, j j}}$.
10. $\Omega_{n} \leftarrow \Omega_{n}-\{i\}$.
11. Return $\pi_{u}$.
12. End PRODUCTION_GM

By using PRODUCTION_GM and keeping the other operators unchanged, a new EDA is constructed and named as PEDA_GM. And, the hybrid PEDA_GM is called PHEDA_GM for simplicity. It should be noted that, in PEDA_GM and PHEDA_GM, instead of constructing the seed set $\Pi_{i}\left[\left|\Pi_{i}\right|=|\beta| P_{i}| | \right)$, PRODUCTION_GM is performed $|\beta| P_{i}| |$ rounds. As well, DoE and ANOVA are also adopted to deter-

mine the parameters of PEDA_GM and PHEDA_GM. $\theta \in\{0,0.2,0.5,0.8,1.0\}$ and other parameter domains are identical to those in Section 4.1. So, there are $5 \times 3^{5}=1215$ combinations totally, all of which are tested. In this experiment, $R=5$ and the termination criterion is set as $(n \times m / 2) \times 2 \mathrm{~ms}$ maximum computation time. Similar to the above analysis, the best parameter setting is determined as follows: $\alpha=0.3, \beta=0.2, \gamma=0.03, \theta=0.5$, $d=2$ and Penh $=0.01$.

PEDA_GM is compared with PEDA. The population sizes of both algorithms are set as 30. The first 90 Taillard benchmark instances are also tested, and the termination criteria for both the algorithms are also set as $(n \times m / 2) \times 30 \mathrm{~ms}$ maximum computation time. $R=5$, and the results are shown in Table 5.

Table 5 shows that PEDA outperforms PEDA_GM for each group as well as the average on the nine groups. The performance of PEDA is better than that of PEDA_GM for nearly $39 \%$ $((3.59-2.19) / 3.59 \times 100 \%)$, on average.

PHEDA_GM is compared with PHEDA. The population sizes of both algorithms are set as 30. The first 90 Taillard benchmark instances are also tested, and the termination criteria for both the algorithms are identically set as $(n \times m / 2) \times 90 \mathrm{~ms}$ maximum computation time. $R=5$, and the results are shown in Table 6.

Table 6 illustrates that the effectiveness of PHEDA is much better than that of PHEDA_GM. According to Tables 5 and 6 , it can be concluded that the proposed PRODUCTION is much more effective than PRODUCTION_GM, which adopts the main ideas of GM given by Zhang et al. (2005). In PRODUCTION, all the offspring individuals are generated from different seeds, which are selected from the current population by the roulette method. And, PRODUCTION only considers the LCS between the seed individual and the best solution found so far as good "genes", which are inherited by the off-

Table 6
Performance comparisons between PHEDA_GM and PHEDA (local search hybridized).

spring individuals probabilistically. This method not only inherits good "genes" by the offspring individuals but also keeps the diversity of population. On the other side, in PRODUCTION_GM and GM, for each generation, all the offspring individuals are generated from the same seed: the best solution found so far. And, PRODUCTION_GM and GM consider all the elements of the best solution found so far as good "genes", and inherit them by the offspring individuals probabilistically. So, the generated offspring individuals are quite similar, and the diversity of the population decreases very fast, which deteriorates the performance. To verify this conclusion, another experiment is conducted to explore the diversity of the population during the evolution. The genotype diversity defined by Zhu (2003) is adopted, which can be described below:

Definition 3. Zhu, 2003The genotype diversity of the population can be defined as

$$
\begin{aligned}
\text { Diversity }\left(P_{c}\right)= & \frac{1}{\left|P_{c}\right|\left(\left|P_{c}\right|-1\right) \cdot n} \\
& \times \sum_{\pi_{A}, \pi_{B}, \pi_{C}, \pi_{A}=\pi_{B}} \operatorname{Hamming}\left(\pi_{A}, \pi_{B}\right)
\end{aligned}
$$

where $\operatorname{Hamming}\left(\pi_{A}, \pi_{B}\right)=\sum_{i=1}^{n} f n\left(\pi_{A, i j}, \pi_{B, i j}\right)$ and $f n\left(\pi_{A, i j}, \pi_{B, i j}\right)=$ $\left\{\begin{array}{ll}0, & \pi_{A, i j}=\pi_{B, i j} .\end{array}\right.$ It is obvious that the maximum of $\operatorname{Ham}$ $\operatorname{ming}\left(\pi_{A}, \pi_{B}\right)$ is $n$, so $\operatorname{Diversity}\left(P_{c}\right)$ is restricted in [0,1]. The larger Diversity $\left(P_{c}\right)$ is, the higher the diversity of the population $P_{c}$ is. PEDA, PEDA_GM, PHEDA and PHEDA_GM are performed on the first 90 Taillard benchmark instances, and each instance is tested five times. The termination criterion is set as 200 maximum generations, and Diversity $\left(P_{c}\right)$ of every 10 generations is calculated and recorded. The obtained Diversity $\left(P_{c}\right)$ are averaged over all the instances, and the experimental results are shown in Figs. 9 and 10.

Figs. 9 and 10 illustrate that the population diversities of both PEDA_GM and PHEDA_GM decrease very fast while those of PEDA and PHEDA decrease in a moderate way. This conforms to the above conclusions.

### 4.5. Effectiveness of the proposed PERTURBATION operator

To explore the effectiveness of PERTURBATION, an experiment is designed. By replacing PERTURBATION of proposed PHEDA with the perturbation operator of IG, a new algorithm (PHEDA_IG) is constructed and compared with PHEDA. Parameters of PHEDA_IG are determined by an experiment similar to that in Section 4.1. The
![img-7.jpeg](img-7.jpeg)

Fig. 9. Population diversity comparison between PEDA and PEDA_GM.

![img-8.jpeg](img-8.jpeg)

Fig. 10. Population diversity comparison between PHEDA and PHEDA_GM.

Table 7
Performance comparisons between PHEDA_IG and PHEDA (local search hybridized).

number of removed jobs in the perturbation operator is 3 (i.e. $d=3$ ), and the other parameters are identical to those of PHEDA. The population sizes of both algorithms are set as 30 . The first 90 Taillard benchmark instances are used as well, and the termination criteria for both the algorithms are set as $(n \times m / 2) \times 90 \mathrm{~ms}$ maximum computation time. $R=5$. The results are shown in Table 7 .

Table 7 shows that PHEDA outperforms PHEDA_IG for each group. Both algorithms generate good effectiveness for the two small size groups ( $20 \times 5$ and $20 \times 10$ ), whereas PHEDA obtains better solutions than PHEDA_IG for large size ones. This implies that the proposed PERTURBATION operator is more effective than that of IG, particularly for the large size instances.

## 5. Conclusions

In this paper, an Estimation of Distribution Algorithm (PEDA) was proposed for permutation flow shops with total flowtime minimization. To guarantee the diversity, all the individuals in the initial population were generated randomly. The Longest Common Subsequence (LCS) was incorporated into the probability distribution model to mine good "genes". Different from common EDAs, each offspring individual in PEDA was produced from a seed, selected from the current population by the roulette method. The LCS between the seed individual and the best solution found so far was considered as good "genes", and would be inherited by offspring with a probability, less than $100 \%$, to guarantee the population diversity. To further improve the performance, an effective Variable Neighborhood Search (VNS) was incorporated into PEDA to form a hybrid EDA called PHEDA.

Experimental results showed that the proposed PEDA outperforms JEDA, and PHEDA is better than other existing algorithms
for the considered problem. Moreover, PHEDA found 72 best solutions for the first 90 Taillard benchmark instances, in which 42 were newly discovered. Good "genes" mined by LCS can improve the performance of both PEDA and PHEDA.

## Acknowledgments

This work is supported by the Scientific Research Foundation of Graduate School of Southeast University under Grant No. YBJJ0930, the Research and Innovation Program of Universities in Jiangsu Province under Grant No. CX098_053Z, the National Natural Science Foundation of China (under Grant Nos. 60973073 and 60873236) and the National High Technology Research and Development Program of China (863 program) under Grant No. 2008AA04Z103.
