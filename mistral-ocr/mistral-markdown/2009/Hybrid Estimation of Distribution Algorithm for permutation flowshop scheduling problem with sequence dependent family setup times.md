# Hybrid Estimation of Distribution Algorithm for permutation flowshop scheduling problem with sequence dependent family setup times 

Mansour Eddaly ${ }^{1}$, Bassem Jarboui ${ }^{1}$, Radhouan Bouabda ${ }^{1}$, Abdelwaheb Rebai ${ }^{2}$<br>${ }^{1}$ University of Sfax, FSEGS, route de l'aroport km 4, Sfax 3018, Tunisie (eddaly.mansour@gmail.com, bassem_jarboui@yahoo.fr, radhouan.bouabda@gmail.com)<br>${ }^{2}$ University of Sfax, ESC, route de l'aroport km 4, Sfax 3018, Tunisie (abdelwaheb.rebai@fsegs.rnu.tn)


#### Abstract

This paper addresses to the scheduling in manufacturing cell environment with sequence dependent family setup times in a flow shop with respect to the makespan criterion. Since this is a NP-hard problem, we present an estimation of distribution algorithm as an evolutionary algorithm for solving it. In order to improve the quality of solution of our algorithm, we propose a hybridization with an iterated local search algorithm. The computational experiments show that our algorithm is better than the evolutionary algorithms proposed in the literature. Moreover, it seems able to provide good results in short computational time.


Keywords: manufacturing cell, flowshop, sequence dependant family, estimation of distribution algorithm, iterated local search.

## 1. Introduction

Since the early 1960's, the development of Cellular Manufacturing (CM), as one of Group Technology (GT) subsets, has received much attention of practitioners and researchers in the manufacturing systems. The major issues are the reduction of the complexity and the increase of the productivity of job shops [1]. Operationally, the CM consists in arranging a set of similar jobs into part families. These similarities concern the jobs setups, machinery requirements and operations. In [1] many industrial applications have been cited in CM environments such that chip producing, metal fabricating, and manual assembly industries. Hendizadeh et al. [2] have presented a detailed literature review of the scheduling of cellular manufacturing systems. In this paper we consider the scheduling of CM environment while processing the jobs with the same setup family together. Moreover, in each family, there is a set of n jobs that must be processed on a set of m in the same order without pre-emption (no interruption is allowed). Such cells are known as flowline cells or pure flowshop manufacturing cells [3]. This problem occurs when the time required to shift from one part (job) to another is negligible or included in the processing times. However, the time required to shift from one family to another is high and cannot be neglected. A comprehensive review can be found in [4] for the flowshop scheduling problems with setup times. They have included the problem under consideration in sequence dependent family setup times (SDFST) category. Schaller et al. [3] have presented a real world application in the manufacturing printing circuit boards where the use of CM technology is highly required. Garey and Johnson [5] have showed that this problem is strongly NP-hard with respect to the makespan criterion. This is justifying the choice of approximate algorithms more than exact methods for solving this problem. Schaller et al. [3] have developed lower bounds for solving this problem under minimizing the makespan. The obtained results have showed that the branch and bound based proposed lower bounds is efficient for the test problems with small sizes. However, when the number of families or the number of machines increases, the performance of the lower bounds decreases. Also, sev-
eral constructive heuristics have been proposed in [3]. The computational results have showed that, for scheduling the jobs within families, the called $\overline{\text { CDSheuristic }}$ [6] is the best one. Besides, the NEH heuristic [7] is the most efficient regarding the scheduling job families. França et al. [8] have presented two evolutionary algorithms: a Genetic Algorithm (GA) and a Memetic Algorithm (MA). The computational results showed that these two algorithms outperform existing best heuristic. In addition MA presents a slight superiority according to the GA. Hendizadeh et al. [2] have proposed a Tabu Search (TS) algorithm (TS). They have employed the Simulated Annealing algorithm (SA) concepts for balancing between intensification and diversification of the search's direction. Their results have showed that the proposed algorithm, in average, outperforms the constructive heuristic of [3] in terms of solution quality but not in terms of CPU times. Moreover, the TS algorithm and the MA of Frana et al. [8] appear similar in average. Lin et al. [9] have proposed three different metaheureuistics including SA, GA and TS for solving this problem. It's noted that the proposed SA and GA outperform MA of and Frana et al. [8] and TS of Hendizadeh et al. [2] both regarding the solution quality and the CPU times.
Recently, a novel evolutionary technique, called Estimation of Distribution Algorithm (EDA) has been proposed by Mühlenbein and Paa/F [10]. For generating a new individual, EDA uses a probabilistic model learned from a population of individuals. Therefore, a distribution of probability is estimated from the selected candidates from the initial population and then new offspring is generated according to this distribution.
In this paper an EDA is developed for solving the flowshop scheduling problem with sequence dependent family setup times. Moreover, an Iterated Local Search algorithm is probabilistically added to the EDA aiming to enhance the quality of the solution. The remainder of this paper is organized as follows: section 2 presents the mathematical formulation of the problem; section 3 presents the proposed EDA. The computational results are presented in section 4. Finally, the conclusion is given in section 5.

## 2. Problem Formulation

In a flowshop scheduling problem with sequence dependent family setup times, it's assumed that in each family $f(f=1,2, \ldots, F)$ there is a set of $n_{f}$ jobs must to be processed on a set of $m$ machines where the processing sequence of the jobs is the same for all machines. In particular, we suppose that the job setup times within each family are included in the job processing times. However, if a family $f$ follows another $f^{\prime}$ immediately in the family sequence, the time required for switching from $f^{\prime}$ to $f$ on machine $i(i=1,2, \ldots, m)$ is denoted by $s_{[f \mid f^{\prime} \mid i}$. Also, we denote by $D_{f, j, i}$ and $p_{f, j, i}$ the departure time (starting time) and the processing time of the job $j\left(j=1,2, \ldots, n_{f}\right)$ on the machine $i$ in the family $f$ successively. Similarly, we denote by $D_{[f \mid j] i}$ and $p_{[f \mid j] i}$ the departure time and the processing time of the job at the $j^{\text {th }}$ position in the job sequence on the machine $i$ in the $f^{\text {th }}$ position in the family sequence successively. The makespan $\left(C_{\max }\right)$ can be found through the recursive expression according to the departure times as follows:
$D_{[1][1] 1}=s_{[1][1] 1}$
$D_{[1][1] i}=\max \left\{s_{[1][1] i}, D_{[1][1] i-1}+p_{[1][1] i-1}\right\}$
$i=2,3, \ldots, m$
$D_{[1][j] 1}=D_{[1][j-1] 1}+p_{[1][j-1] 1} j=2,3, \ldots, n_{1}$
$D_{[1][j] i}=\max \left\{D_{[1][j-1] i}+p_{[1][j-1] i}, D_{[1][j-1] i}+\right.$
$\left.p_{[1][j] i-1}\right\} j=2,3, \ldots, n_{1} i=2,3, \ldots, m$
$D_{[f][1] 1}=D_{[f-1]\left[n_{f-1}\right] 1}+p_{[f-1]\left[n_{f-1}\right] 1}+s_{[f][f-1] 1}$
$f=2,3, \ldots, F$
$D_{[f][j] 1}=D_{[f][j-1] 1}+p_{[f][j-1] 1} f=2,3, \ldots, F$
$j=2,3, \ldots, n_{f}$
$D_{[f][1] i}=\max \left\{D_{[f][n_{f-1}] i}+p_{[f][n_{f-1}] i}+\right.$
$\left.s_{[f][f-1] i}, D_{[f][1] i-1}+p_{[f][1] i-1}\right\} f=2,3, \ldots, F$
$i=2,3, \ldots, m$
$D_{[f][j] i}=\max \left\{D_{[f][j-1] i}+p_{[f][j-1] i}, D_{[f][j] i-1}+\right.$
$\left.p_{[f][j] i-1}\right\} f=2,3, \ldots, F j=2,3, \ldots, n_{f} i=2,3, \ldots, m$
Thus
$C_{\max }=D_{[F][n_{f}] m}+p_{[F][n_{f}] m}$

## 3. The proposed EDA

The section discusses the framework of our proposed EDA for solving the flowshop scheduling problem with sequence dependent family setup times under the minimization of the makespan criterion.

### 3.1. Encoding scheme and initial population

In this chapter each solution is represented by two permutations. The first permutation represents the family vectors where the $f^{\mathrm{t}} h$ case indicates the family located on the position $f$ in the family sequence. The second one represents the permutation of jobs within each family, where the $j^{\mathrm{t}} h$ number denotes the job located on position $j$. In order to grant the diversification of the algorithm, the $P$ individuals of the initial population are generated randomly.

### 3.2. Selection

The procedure of selection adopted in our algorithm consists of two phases. First, the individuals of the initial population are sorted, in an increasing order, according to their
objective functions. Second, $M$ individuals are selected from the subset of $20 \%$ of best individuals from the sorted list.

### 3.3. Estimation of the probability

In order to generate new individual, the EDA constructs a probabilistic model based on the selected individuals. We propose to build a probabilistic model for generating both the family sequence and the job sequence. As in [11] our estimated probabilities depend on the structure of sequences of selected individuals. Therefore, both the order of the family (job) and the similar blocks of families (jobs) are greatly considered. First we create the new family sequence by using the following parameters:

- $\eta_{f g}$ be the number of times where the family $f$ is located before or on the position $g$ in the subset of the selected sequences plus a constant $\delta_{1}^{f}$. Thus, $\eta_{f g}$ indicates the importance of the order of the families in the family sequence.
- $\mu_{f[g-1]}$ be the number of times where the family $f$ come after the family on the position $f^{\prime}-1$ in the subset of the selected sequences plus $\delta_{2}^{f}$. $\mu_{f[g-1]}$ highlights the importance of the similar blocks of families in the family sequences. In such way, we prefer to conserve the similar blocks as much as possible.
- $\Omega_{g}^{f}$ is the set of families not already scheduled until position $g$.
Thus, the probability for locating the family $f$ on the position $g$ in the sequence of new individual is calculated as follows:

$$
\pi_{f g}=\frac{\eta_{f g} \times \mu_{f[g-1]}}{\sum_{i \in \Omega_{g}} \eta_{f g} \times \mu_{f[g-1]}}
$$

Then, given the resulted family sequence, we create the new job sequences by a similar way. Therefore, we redefine the same parameters as above $\left(\eta_{j k}, \delta_{1}^{j}, \mu_{j[k-1]}, \delta_{2}^{j}\right.$ and $\left.\Omega_{k}^{j}\right)$ while modifying family sequence by job sequence. So, within each family $f$, the estimated probability of selection the job $j$ on the $k^{\mathrm{t}} h$ position in the new job sequence is obtained following this formula:

$$
\pi_{j k}=\frac{\eta_{j k} \times \mu_{j[k-1]}}{\sum_{i \in \Omega_{k}} \eta_{i k} \times \mu_{i[k-1]}}
$$

### 3.4. Iterated Local Search Algorithm

In order to improve the solution provided by the EDA, we propose to use an Iterated Local Search (ILS) algorithm [12]. This algorithm is a local search based algorithm characterised by its simplicity of implementation. Its previous application to hard combinatorial optimization problems, such as quadratic assignment problem [13], graph coloring [14], vehicle routing problem [15] and permutation flowshop scheduling problem [16], are qualified as successful. For each created individual, we calculate the probability which decides if the ILS algorithm will be applied this individual. This probability was proposed by Jarboui et al. [11], it depends on the quality of the new solution.

Let $\sigma_{\text {current }}$ and $f\left(\sigma_{\text {current }}\right)$ denote the sequence of the new individual and its makespan respectively. Also, we denote by $\sigma_{\text {best }}$ and $f\left(\sigma_{\text {best }}\right)$ the best solution found by the algorithm and its objective function value. The probability of application of the ILS algorithm is defined as follows: $p r o b=\max \left[\exp \left(\frac{R D}{\alpha}\right), \epsilon\right]$ where $R D=$ $\left(\frac{f\left(\sigma_{\text {current }}\right)-f\left(\sigma_{\text {best }}\right)}{f\left(\sigma_{\text {best }}\right)}\right)$. The basic framework an ILS algorithm consists of two main components: the local search procedures and the perturbation.
In our algorithm we use two local procedures for the family sequence as well as for the job sequence. We note that each procedure is applied to the family sequence and then for the job sequence within each family successively. The first procedure consists in inserting all pairs of families (jobs) in all possible positions in $\sigma_{\text {algorithm }}$. We denote by $\sigma_{1}$ the obtained local optima from the insert moves. Next, $\sigma_{2}$ is obtained by the second local search after permuting all pairs of families (jobs) in $\sigma_{\text {current }}$. If $\sigma_{2}$ is better than $\sigma_{1}$ then the latter is replaced by the former and we return to the first procedure. These procedures continue to perform until no possible improvement.
As in the local search phase, the same way of perturbation is employed to both the family and the job sequence. Therefore, at each iteration of the ILS algorithm, two distinct positions are selected at random from the family (job) sequence and the families on these positions are exchanged. The ILS algorithm will terminate after a maximal number of iterations.

## 4. Computational experiments

Tab. 1: Computational results of local search based algorithms

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| C0119 | 0.00 | 0.07 | 1.17 | 0.00 | 0.07 | 1.17 | 0.00 | 0.07 | 1.17 | 0.00 | 0.07 | 1.17 | 0.00 | 0.07 |
| L0034 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 |
| L0034 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 |
| L0035 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 |
| L0036 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 |
| L0037 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 |
| L0038 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 |
| L0039 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.06 |
| L0039 | 0.11 | 0.46 | 0.97 | 31.7 | 0.00 | 0.46 | 0.77 | 27.79 | 0.12 | 0.61 | 1.25 | 27.99 | 0.12 | 0.61 |
| L0040 | 0.00 | 0.09 | 1.80 | 31.2 | 0.00 | 0.58 | 1.42 | 32.49 | 0.11 | 0.92 | 1.77 | 32.28 | 0.11 | 0.92 |
| M0U01 | 0.00 | 0.38 | 3.57 | 7.3 | 0.00 | 0.35 | 3.26 | 2.59 | 0.00 | 0.35 | 3.26 | 2.11 | 0.00 | 0.35 |
| M0U04 | 0.00 | 0.59 | 2.30 | 14.9 | 0.00 | 0.56 | 2.23 | 1.79 | 0.00 | 0.56 | 2.23 | 1.34 | 0.00 | 0.56 |
| M0U44 | 0.00 | 0.78 | 2.51 | 20.4 | 0.00 | 0.59 | 2.27 | 3.23 | 0.00 | 0.59 | 2.27 | 2.71 | 0.00 | 0.59 |
| M0U51 | 0.00 | 0.50 | 2.10 | 17.1 | 0.00 | 0.45 | 2.05 | 4.83 | 0.00 | 0.45 | 2.05 | 4.01 | 0.00 | 0.45 |
| M0U56 | 0.00 | 0.90 | 3.12 | 25.1 | 0.00 | 0.86 | 3.03 | 5.53 | 0.00 | 0.88 | 3.03 | 4.77 | 0.00 | 0.88 |
| M0U61 | 0.00 | 0.40 | 1.72 | 17.8 | 0.00 | 0.37 | 1.21 | 6.76 | 0.00 | 0.44 | 1.45 | 5.76 | 0.00 | 0.44 |
| M0U68 | 0.00 | 0.40 | 1.62 | 22.8 | 0.00 | 0.36 | 1.39 | 10.64 | 0.00 | 0.48 | 1.62 | 1.46 | 1.46 | 1.46 |
| M0U68 | 0.00 | 1.10 | 2.98 | 28.8 | 0.00 | 0.96 | 2.89 | 10.55 | 0.00 | 1.15 | 2.89 | 15.86 | 0.00 | 1.15 |
| M0U108 | 0.00 | 1.17 | 3.05 | 31.3 | 0.00 | 0.78 | 1.77 | 27.79 | 0.16 | 1.30 | 2.55 | 27.26 | 0.16 | 2.55 |
| M0U1010 | 0.15 | 1.22 | 3.71 | 31.9 | 0.15 | 0.98 | 2.36 | 32.64 | 0.19 | 1.41 | 2.73 | 32.35 | 0.19 | 2.73 |
| S0U55 | 0.00 | 0.31 | 2.46 | 8.8 | 0.00 | 0.31 | 2.42 | 2.59 | 0.00 | 0.31 | 2.42 | 2.12 | 0.00 | 2.12 |
| S0U34 | 0.00 | 0.96 | 6.62 | 16.9 | 0.00 | 0.82 | 2.86 | 1.79 | 0.00 | 0.82 | 2.86 | 1.41 | 0.00 | 1.41 |
| S0U69 | 0.00 | 0.64 | 2.91 | 17.0 | 0.00 | 0.57 | 2.82 | 2.19 | 0.00 | 0.60 | 2.82 | 2.54 | 0.00 | 2.54 |
| S0U55 | 0.00 | 0.94 | 2.55 | 26.8 | 0.00 | 0.90 | 2.29 | 4.73 | 0.00 | 0.94 | 2.29 | 4.03 | 0.00 | 2.29 |
| S0U96 | 0.00 | 1.63 | 3.99 | 28.6 | 0.00 | 1.53 | 3.80 | 5.47 | 0.00 | 1.63 | 3.80 | 4.79 | 0.00 | 4.79 |
| S0U65 | 0.00 | 1.03 | 3.45 | 24.6 | 0.00 | 0.96 | 3.23 | 6.78 | 0.00 | 1.02 | 3.23 | 3.82 | 0.00 | 3.82 |
| S0U68 | 0.29 | 2.14 | 4.53 | 30.9 | 0.29 | 1.76 | 3.46 | 10.66 | 0.29 | 2.12 | 4.12 | 15.85 | 0.29 | 1.76 |
| S0U108 | 0.72 | 1.97 | 3.13 | 31.9 | 0.48 | 1.53 | 2.64 | 27.86 | 0.86 | 2.02 | 2.98 | 27.30 | 0.86 | 2.02 |
| S0U1010 | 0.68 | 2.05 | 4.60 | 32.4 | 0.59 | 2.14 | 3.53 | 32.68 | 0.68 | 2.86 | 4.16 | 32.59 | 0.68 | 2.86 |
| Average | 0.06 | 0.03 | 2.67 | 21.7 | 0.03 | 0.72 | 2.20 | 10.96 | 0.08 | 0.85 | 2.43 | 10.34 | 0.08 | 2.43 |


|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| C0119 | 0.00 | 0.07 | 1.17 | 0.00 | 0.07 | 1.17 | 0.00 | 0.07 | 1.17 | 0.00 | 0.07 | 1.17 | 0.00 | 0.07 |
| L0034 | 0.00 | 0.32 | 2.45 | 10.1 | 0.00 | 0.33 | 2.30 | 2.09 | 0.00 | 0.33 | 2.44 | 0.03 | 0.33 | 2.44 |
| L0034 | 0.00 | 0.20 | 1.88 | 10.1 | 0.00 | 0.20 | 1.98 | 2.29 | 0.00 | 0.20 | 1.97 | 0.00 | 0.20 | 1.97 |
| L0035 | 0.00 | 0.28 | 1.86 | 12.1 | 0.00 | 0.28 | 1.83 | 1.01 | 0.00 | 0.28 | 1.86 | 0.22 | 1.86 | 0.22 |
| L0036 | 0.00 | 0.31 | 2.42 | 11.1 | 0.00 | 0.30 | 2.37 | 4.21 | 0.00 | 0.31 | 2.43 | 0.24 | 2.43 | 0.24 |
| L0039 | 0.00 | 0.31 | 1.82 | 15.1 | 0.00 | 0.32 | 2.37 | 10.97 | 0.00 | 0.31 | 2.43 | 0.28 | 2.43 | 0.28 |
| L0040 | 0.00 | 0.19 | 1.56 | 15.3 | 0.00 | 0.21 | 1.55 | 12.90 | 0.00 | 0.20 | 1.57 | 0.33 | 1.57 | 0.33 |
| L0041 | 0.00 | 0.38 | 2.61 | 24.7 | 0.00 | 0.38 | 2.65 | 24.59 | 0.00 | 0.39 | 1.86 | 1.18 | 1.18 | 1.18 |
| L0042 | 0.00 | 0.47 | 1.19 | 29.8 | 0.00 | 0.43 | 1.12 | 39.59 | 0.00 | 0.42 | 1.01 | 3.28 | 1.01 | 3.28 |
| L0043 | 0.00 | 0.77 | 2.27 | 29.5 | 0.00 | 0.62 | 1.43 | 43.61 | 0.00 | 0.57 | 1.44 | 5.98 | 0.00 | 5.98 |
| M0U01 | 0.00 | 0.37 | 3.57 | 7.1 | 0.00 | 0.35 | 3.26 | 2.54 | 0.00 | 0.36 | 3.57 | 0.01 | 0.35 | 3.57 |
| M0U34 | 0.00 | 0.56 | 2.29 | 13.1 | 0.00 | 0.56 | 2.25 | 2.09 | 0.00 | 0.57 | 2.30 | 0.03 | 0.56 | 2.30 |
| M0U69 | 0.00 | 0.85 | 1.12 | 16.2 | 0.00 | 0.86 | 2.05 | 2.54 | 0.00 | 0.86 | 2.53 | 0.08 | 0.86 | 2.53 |
| M0U10 | 0.00 | 0.45 | 2.08 | 13.1 | 0.00 | 0.46 | 2.05 | 7.38 | 0.00 | 0.45 | 2.10 | 0.31 | 2.08 | 0.31 |
| M0U36 | 0.00 | 0.36 | 3.12 | 10.0 | 0.00 | 0.45 | 3.03 | 4.20 | 0.00 | 0.45 | 3.12 | 1.00 | 0.00 | 3.12 |
| M0U65 | 0.00 | 0.36 | 1.24 | 24.0 | 0.00 | 1.00 | 3.33 | 10.86 | 0.00 | 1.24 | 2.73 | 1.00 | 0.00 | 3.73 |
| S0U68 | 0.00 | 1.28 | 2.72 | 29.1 | 0.00 | 1.31 | 2.65 | 12.82 | 0.00 | 0.99 | 3.45 | 1.17 | 0.00 | 3.45 |
| M0U69 | 0.00 | 0.99 | 2.94 | 27.3 | 0.00 | 0.99 | 2.89 | 23.83 | 0.00 | 1.00 | 2.94 | 1.38 | 0.00 | 3.38 |
| M0U108 | 0.00 | 0.86 | 1.80 | 30.1 | 0.00 | 0.82 | 2.24 | 39.66 | 0.00 | 0.78 | 1.63 | 6.86 | 0.00 | 6.86 |
| M0U1010 | 0.15 | 1.15 | 2.53 | 30.8 | 0.15 | 0.98 | 2.82 | 43.71 | 0.15 | 0.97 | 2.42 | 5.53 | 0.00 | 5.53 |
| S0U55 | 0.00 | 0.51 | 2.47 | 7.1 | 0.00 | 0.51 | 2.42 | 2.55 | 0.00 | 0.51 | 2.48 | 0.07 | 0.51 | 2.48 |
| M0U34 | 0.00 | 0.03 | 2.94 | 13.1 | 0.00 | 0.02 | 2.86 | 2.71 | 0.00 | 0.03 | 2.94 | 0.07 | 0.51 | 2.94 |
| M0U69 | 0.00 | 0.57 | 2.48 | 13.0 | 0.00 | 0.62 | 2.82 | 2.32 | 0.00 | 0.58 | 2.91 | 0.10 | 0.58 | 2.91 |
| S0U93 | 0.00 | 0.92 | 2.08 | 26.0 | 0.00 | 0.93 | 2.28 | 7.37 | 0.00 | 0.92 | 2.35 | 0.56 | 0.56 | 2.35 |
| S0U96 | 0.00 | 0.36 | 3.08 | 25.4 | 0.00 | 0.35 | 3.00 | 4.20 | 0.00 | 0.35 | 2.00 | 0.64 | 0.64 | 2.00 |
| S0U65 | 0.00 | 0.99 | 3.44 | 24.0 | 0.00 | 1.00 | 3.33 | 10.86 | 0.00 | 1.24 | 2.73 | 1.00 | 0.00 | 2.73 |
| S0U68 | 0.00 | 1.28 | 2.72 | 29.1 | 0.00 | 1.31 | 2.65 | 12.82 | 0.00 | 0.99 | 3.45 | 1.17 | 0.00 | 3.45 |
| M0U69 | 0.00 | 1.65 | 3.11 | 30.3 | 0.25 | 1.88 | 3.54 | 23.82 | 0.25 | 1.79 | 3.46 | 2.57 | 2.57 | 2.57 |
| S0U108 | 0.72 | 1.77 | 2.9 | 30.7 | 0.72 | 1.51 | 2.83 | 39.65 | 0.48 | 1.49 | 2.71 | 8.50 | 0.00 | 8.50 |
| S0U1010 | 0.59 | 2.33 | 3.65 | 30.6 | 0.59 | 2.18 | 3.33 | 43.75 | 0.59 | 2.08 | 3.42 | 12.93 | 0.00 | 12.93 |
| Average | 0.06 | 0.76 | 2.37 | 28.4 | 0.06 | 0.74 | 2.31 | 15.76 | 0.05 | 0.72 | 2.32 | 1.87 |  |  |

MA was run on a PC Pentam II 200 MHz processor and 125 MB RAM. (França et al.,2005)
GA was run on a PC Pentam IV 2.4GHz processor and 512MB RAM. (Lao et al.,2009)

## 1. $\boldsymbol{\text { SSU }}$, 2. $\boldsymbol{\text { Medium }}$ Setups (MSU) and Large Setups

(LSU). A Detailed description of these problem tests is given in [3] and França et al. [8]. Algorithm EDA was coded in C++ and run on a PC with Pentium 4, 3 GHz processor, with 512 Mb of RAM.
In order to properly set the values of tuning parameters, EDA was run several times. Therefore, we set $\mathrm{P}=60$ (the size of initial population), $\mathrm{M}=3$ (the number of selected individuals), $\delta_{1}^{1}=\delta_{2}^{1}=\frac{4}{P}, \delta_{3}^{1}=\delta_{4}^{1}=\frac{4}{6}$, $\mathrm{N}_{\mathrm{P}}$ parameter $\alpha$ used in the probability of application of the ILS algorithm is fixed according to $R D$ and $p r o b$. Assuming that with a $p r o b=0.5$, we accept a sequence with a $C_{\text {max }}$ higher than the best value while $R D$ is less than or equal to $1 \%$. So, $\alpha=\frac{R D}{1 \mathrm{~s}}=\frac{0.81}{\log (p r o b)}=\frac{0.81}{\log (0.5)}$, thereafter we determined prob according to this formula $p r o b=\max \left[\exp \left(\frac{R D}{1 \mathrm{~s}}\right),\right]$ with $\mathrm{s}=0.01$. Finally, we set a run time of 30 seconds as a termination criterion of our algorithm.
For each class of instances, we define a performance measure of each algorithm by the average relative percentage of improvements $\Delta_{\text {average }}=\frac{\sum_{i=1}^{30} p_{i}}{30}$ of the makespan obtained by the heuristic algorithm i with respect to the lower bound values of Schaller et al. [3]. $\Delta_{\text {min }}$ and $\Delta_{\text {max }}$ denote, respectively, the minimum and the maximum relative percentage of improvements over each class of instances. tavg reports the average CPU times of different algorithms in seconds.
The results given in Table 1 are those obtained by the local search based approaches in the literature. The first column provides the results of The TS algorithm (TS(2)) of Hendizadeh et al. [2]. The second column and the third column show, respectively, the results of Simulated Annealing (SA) and TS algorithm (TS(1)) developed by Lin et al. [9]. Table 2 summarizes the results obtained by evolutionary algorithms including the Memetic Algorithm (MA) of Frana et al. [8], GA of Lin et al. [9] and our proposed EDA algorithms.
From Table 2, the values of $\Delta_{\text {min }}, \Delta_{\text {average }}$ and $\Delta_{\text {max }}$

provided by our algorithm are, respectively, equal to 0.05 , 0.72 and 2.32. Therefore, while comparing our algorithm with the other evolutionary algorithms of the literature such as GA and MA, it's clear that, in average, our algorithm outperforms these algorithms in terms of quality of solutions. Concerning the computational effort, with respect to our used configuration, we find that our $t_{\text {avg }}$ is equal to 1.87 seconds. So, our proposed EDA appears able to provide a good quality of solution in a short time.
Besides, the comparison against the local search based algorithms of the literature shows that the EDA is better than the two TS algorithms while regarding $\Delta_{\text {mon }}, \Delta_{\text {avg }}$ and $\Delta_{\text {max }}$. However EDA and SA are almost similar with a slight superiority in favour of the latter in terms of $\Delta_{\text {max }}$. On other hand, for the instances with large number of families and machines like SSU1010 and MSU1010, we observe that the EDA algorithm is better than SA in average.

## 5. Conclusion and further direction

This paper considered the flowline manufacturing cell scheduling problem with sequence dependent family setup times under the makespan minimization. Due to its hard complexity, there is a considerable amount of approximate methods that addressed this problem. We proposed an estimation of distribution algorithm that exploits the characteristics of order and blocks of a sequencing problem in the step of construction of new individual. An iterated local algorithm is embedded to the EDA for improving the quality of generated offspring. Numerical experiments indicated that our proposed algorithm is better than the evolutionary algorithm proposed in the literature. In addition, our EDA is able to reach good solutions with low computation effort. Further, this algorithm may be applied to solve other variants of the problem by relaxing the constraint of permutation schedules and/or the constraint of dependencies between the families.

## REFERENCES

[1] Greene TJ, Sadowski RP. "A review of cellular manufacturing assumptions, advantages and design techniques". Journal of Operations Management,Vol.4, pp85-97, 1984.
[2] Hendizadeh SH, Faramarzi H, Mansouri SA, Gupta JND, ElMekkawy TY. "Meta-heuristics for scheduling a flowline manufacturing cell with sequence dependent family setup times". International Journal of Production Economics, Vol. 111, pp593-605, 2008.
[3] Schaller JE, Gupta JND, Vakharia AJ. "Scheduling a flowline manufacturing cell with sequence dependent family setup times". European Journal of Operational Research, Vol. 125, pp324-39, 2000.
[4] Cheng TCE, Gupta JND, Wang G. "A review of flowshop scheduling research with setup times". Production and Operations Management, Vol. 9, pp262-282, 2000.
[5] Garey MR, Johnson DS. "Computers and Intractability: A Guide to the Theory of NP-Completeness". Freeman, San Francisco, CA 1979.
[6] Campbell, HG, Dudek RA, Smith ML. "A heuristic algorithm for the n-job, m-machine sequencing
problem". Management Science, Vol. 16, pp630-637, 1970.
[7] Nawaz M., Enscore E., Ham I. "A heuristic algorithm for the m-machine, n-job flow shop sequencing problem". OMEGA, International Journal of Management Science, Vol. 11, pp91-95, 1983.
[8] França PM, Gupta JND, Mendes AS, Moscato P, Veltink K. "Evolutionary algorithms for scheduling a flowshop manufacturing cell with sequence dependent family setups". Computers and Industrial Engineering, Vol. 48, pp491-506, 2005.
[9] Lin S-W, Ying K-C, Lee Z-J. "Metaheuristics for scheduling a non-permutation flowline manufacturing cell with sequence dependent family setup times". Computers and Operations Research, Vol. 36, pp1110-1121, 2009.
[10] Mühlenbein H, Paa $\beta$ G., "From Recombination of Genes to the Estimation of Distributions I. Binary Parameters". PPSN pp178-187, 1996.
[11] Jarboui B., Eddaly M., Siarry P., "An estimation of distribution algorithm for minimizing the total flowtime in permutation flowshop scheduling problems". Computers and Operations Research, Vol. 36, pp2638-2646, 2008.
[12] Lourenc HR, Martin O, Stützle T. "Iterated local search", in: F. Glover, G. Kochenberger (Eds.), Handbook of Metaheuristics, International Series in Operations Research and Management Science, Vol. 57, Kluwer Academic Publishers, Norwell, MA, pp321353, 2002.
[13] Stützle T. "Iterated local search for the quadratic assignment problem". European Journal of Operational Research Vol. 174, pp1519-1539, 2006.
[14] Caramia M, Dell'Olmo P. "Coloring graphs by iterated local search traversing feasible and infeasible solutions" Discrete Applied Mathematics, Vol. 156, pp201-217, 2008.
[15] Ibarakia T, Imahorib S Nonobec K, Sobued K, Unoe T, Yagiuraf M. "An iterated local search algorithm for the vehicle routing problem with convex time penalty functions". Discrete Applied Mathematics, Vol. 156, pp2050-2069, 2008.
[16] Dong X, Huang H, Chen P. "An iterated local search algorithm for the permutation flowshop problem with total flowtime criterion" Computers and Operations Research, Vol. 36, pp1664-1669, 2009.