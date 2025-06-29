# An Estimation of Distribution Algorithm for Minimizing the Makespan in Blocking Flowshop Scheduling Problems 

Bassem Jarboui ${ }^{1}$, Mansour Eddaly ${ }^{1}$, Patrick Siarry ${ }^{2}$, and Abdelwaheb Rebaï ${ }^{1}$<br>${ }^{1}$ FSEGS, route de l'aéroport km 4.5, B.P. No. 1088, Sfax 3018, Tunisie<br>bassem_jarboui@yahoo.fr, eddaly.mansour@gmail,<br>abdelwaheb.rebai@fsegs.rnu.tn<br>${ }^{2}$ LiSSi, Université de Paris 12, 61 avenue du Général de Gaulle, 94010 Créteil, France<br>siarry@univ-paris12.fr

Summary. This chapter addresses to the blocking flowshop scheduling problem with the aim of minimizing the makespan. An Estimation of Distribution Algorithm, followed by a local search procedure, after the step of creating a new individual, was developed in order to solve this problem. Our comparisons were performed against representative approaches proposed in the literature related to the blocking flowshop scheduling problem. The obtained results have shown that the proposed algorithm is able to improve 109 out of 120 best known solutions of Taillard's instances. Moreover, our algorithm outperforms all competing approaches in terms of solution quality and computational time.

## 1 Introduction

In the nature, the evolution of species in a population, through the sexual reproduction, was formulated by Charles Darwin (T. Back, 1996). It can be modelled by means of three mechanisms: recombination (or crossover), mutation and selection. The process of recombination occurs during meiosis resulting from crossover between parental chromosomes. Through this process, the offspring inherit different combinations of genes from their parents. The mutation arises from errors of copying in genetic materials during cell division. It creates changes into offspring's chromosomes. Under selection, individuals with best traits tend to have more luck to survive and reproduce for further generations. Evolutionary algorithms (EAs) are a class of algorithms that use computers to simulate the natural evolution of species to solve hard optimization problems through evolving a population of candidate solutions. EAs have proved their performance against classical techniques of optimization (Fogel, 1995). Several algorithms are included in this class such as the Genetic Algorithm (GA), which is the most popular. Neighbouring nature-inspired approaches are Ant Colony Optimization, Particle Swarm Optimization, etc.

Recently, a new EA was introduced by Mühlenbein and Paaß in (Mühlenbein and Paaß, 1996), called Estimation of Distribution Algorithm (EDA). It constitutes a new tool of evolutionary algorithms (Larranaga P. and Lozano J.A., 2002), based on the

probabilistic model learned from a population of individuals. Starting with a population of individuals (candidate solutions), generally randomly generated, this algorithm selects good individuals with respect to their fitness. Then a new distribution of probability is estimated from the selected candidates. Next, new offspring are generated from the estimated distribution. The process is repeated until the termination criterion is met. In the literature, diverse versions of EDAs were developed, depending on the chosen probabilistic model. The EDAs can be classified into three classes: EDAs with no dependencies between the variables, EDAs with two-order dependencies and EDAs with multiple dependencies between the variables.

EDAs have been employed for solving combinatorial optimization problems. So, several successful applications were proposed such as: quadratic assignment problem (Zhang et al., 2006), 0-1 knapsack problem (Hui Li et al., 2004), n-queen problem (Paul TK and Iba H, 2002), travelling salesman problem (Robles et al., 2006) and hybrid flowshop scheduling problem (Salhi et al., 2007). In recent works, the EDAs were devoted to solve multi-objective optimization problems (Zhang et al. 2008, Hui Li et al., 2004).

In this work, we propose to adopt this new technique for solving the blocking flowshop scheduling problem. In this variant of flowshop scheduling, there is a set of $n$ jobs that must be processed on a set of $m$ machines in the same order. While the storage is not allowed, when a job is completed on a machine, the latter is blocked until a free next machine becomes available. Blocking constraints takes place because of the automation of new production systems and the use of the robotic manufacturing. Typical areas are chemical and pharmaceutical industries, where a partially completed job cannot quit the machine on which it is processed, while downstream machines are busy (Grabowski and Pempera, 2007). Grabowski and Pempera (2000) have presented a real case of scheduling client orders in a building industry that produces concrete blocks. Also, Hall and Sriskandarajah (1996) have presented a review of applications of blocking scheduling models. They have indicated that blocking environment occurs from characteristics of the process technology itself or from the lack of the storage capacity between the machines. They have proved that this problem is strongly NP-complete for $m=3$, where the makespan $\left(C_{\max }\right)$ is a measure of performance.

In the literature, various approaches were developed to solve the permutation flowshop scheduling problem under blocking constraints, including branch and bound algorithm (B\&B) (Levner, 1969, Suhami and Mah, 1981, Ronconi, 2005, Company and Mateo, 2007), constructive heuristics (McCormick et al., 1989, Leisten, 1990, Abadi et al., 2000, Ronconi and Armentano, 2001, Ronconi, 2004), genetic algorithm (GA) (Caraffa et al., 2001) and tabu search (TS) (Grabowski and Pempera, 2007).

The remaining of this chapter is organized as follows: section 2 presents the Estimation of Distribution Algorithm and its variants; section 3 presents the existing works with EDA in combinatorial optimization. The blocking flowshop is described in section 4 Our proposed algorithm is presented in section 5 Section 6 presents the computational results and conclusion is given in section 7

# 2 Estimation of Distribution Algorithm (EDA) 

EDA is an evolutionary algorithm proposed by Mühlenbein and Paaß in 1996. Instead of recombination and mutation, EDA generates new individuals with respect to a probabilistic model, learned from the population of parents.

# 2.1 Basic EDA 

The general framework of the basic EDA can be presented as follows (Mühlenbein and Paaß, 1996). Starting with a randomly generated initial population, one selects a subpopulation of M parent individuals through a selection method based on the fitness function. Next, one estimates the probability of distribution of the selected parents with a probabilistic model. Then, one generates new offspring, according to the estimated probability distribution. Finally, some individuals in the current population are replaced with new generated offspring. These steps are repeated until one stopping criterion is met. The pseudo-code of the canonical EDA is given in Figure 1.

## Basic EDA

Generate an initial population of P individuals;
do

- Select a set of $Q$ parents with a selection method;
- Build a probabilistic model for the set of selected parents;
- $\quad$ Create new $P_{1}$ offspring according to the estimated probability distribution;
- Replace some individuals in the current population with new individuals;
while a stopping criterion is not met

Fig. 1. Canonical version of EDA

Three classes of EDA were developed, according to the chosen probabilistic model. The first class consists of models which don't take into account the dependencies between variables of candidate solutions, i.e. all variables are independent. The second class assumes at most two-order dependencies between these variables and the last class assumes multiple dependencies between the variables.

### 2.2 EDAs with No Dependencies

Let $X_{i}, i=1,2, \ldots ., n$, be a random variable and $x_{i}$ its possible realization and let $p\left(X_{i}=x_{i}\right)=p\left(x_{i}\right)$ the mass probability of $X_{i}$ over the point $x_{i}$. By analogy, we denote by $\mathbf{X}=\left\{X_{1}, X_{2}, \ldots ., X_{n}\right\}$ a set of $n$-dimensional random variables, $\mathbf{x}=\left\{x_{1}, x_{2}, \ldots ., x_{n}\right\}$ its possible realizations and $p(\mathbf{X}=\mathbf{x})=p(\mathbf{x})$ the joint mass probability of $\mathbf{X}$ over the point $\mathbf{x}$.

In this class of EDAs, it is assumed that the $n$-dimensional joint probability distribution is calculated through the product of the marginal probabilities of $n$ variables, as follows:

$$
p(x)=\prod_{i=1}^{n} p\left(x_{i}\right)
$$

In other hand, the hypothesis of interaction between the variables is rejected.
Among the EDAs included in this class we can cite: Bit-Based Simulated Crossover (BBSC) of Syswerda (1993), Population-Based Incremental Learning (PBIL) of Baluja (1994), Compact Genetic Algorithm (CGA) of Harik et al. (1998) and Univariate Marginal Distribution Algorithm (UMDA) of Mühlenbein et al. (1998).

Although these approaches have provided better results for some problems, their assumption seems to be inexact for difficult optimization problems, where we cannot exclude the interdependencies between the variables completely (Paul TK and Iba H, 2002).

# 2.3 EDAs with Two-Order Dependencies 

In this class, only paired interactions between the variables are taken into account. So, EDAs belonging to this group constitute an extension of the previous one. Therefore, the parametric learning of model, proposed in EDAs with no interaction, becomes structural.

In the literature, several approaches were developed in this class, such as: Mutual Information Maximization for Input Clustering (MIMIC) in De Bonet al. (1997), Combining Optimizers with Mutual Information Trees (COMIT) in Baluja and Davies (1997) and Bivariate Marginal Distribution Algorithm (BMDA) in Pelikan and Mühlenbein (1999).

### 2.4 EDAs with Multiple Dependencies

This last class of EDAs is the most general case, and the leaning process of models proposed here is more complex, because the estimation of joint probability is performed by taking into account an order of dependencies greater than two.

The following approaches of EDAs are included in this class: Factorized Distribution Algorithm (FDA) (Mühlenbein et al., 1999), Estimation of Bayesian Networks Algorithm (EBNA) (Etxeberria and Larranaga, 1999), Bayesian Optimization Algorithm (BOA) (Pelikan et al., 1999), Learning Factorized Distribution Algorithm (LFDA) (Mühlenbein and Mahning, 1999) and the Extended Compact Genetic Algorithm (ECGA) (Harik, 1999).

## 3 Some EDAs for Combinatorial Optimization Problems

Although, EDA was recently invented, the number of its applications in the field of combinatorial optimization increases rapidly. In this section, we will present some applications of EDA to combinatorial optimization problems and we will mainly focus on the constructed probabilistic model for each application.

The Jobshop Scheduling Problem (JSP) was addressed by J. Lozano et al. (in Larrañaga and Lozano, 2002). The authors have selected some variants of EDA and used both continuous and discrete versions. The selected algorithms are UMDA, BBSC, PBIL, MIMIC and EBNA.

The obtained results are comparable to those obtained using GA. In particular the continuous EDAs perform better than the discrete EDAs.

Paul TK and Iba H have proposed, in (Paul TK and Iba H, 2002), an UMDA to solve $n$-queen problem. The objective of this problem is to find a way of putting $n_{q}$ queens ( $n_{q} \geq 4$ ) on a $n_{q} \times n_{q}$ chessboard, such that none of them can capture any other, i.e. two queens cannot share the same row, column or diagonal. A problem's solution $x$ was represented as follows: $\mathbf{x}=\left\{x_{1}, x_{2}, \ldots \ldots, x_{n q}\right\}$, where $x_{i}, 1 \leq i \leq n_{q}$, denotes the column position in row $i$ where the queen $i$ can be put. The initial population was randomly generated while excluding cases where two queens are in the same column or row. The fitness of each individual is calculated as the number of queens that do not share the same diagonal. Next, the first $50 \%$ of individuals (best individuals) were selected according to their fitness. Then, the joint probability was selected using the marginal frequencies of each $x_{i}$ and new individuals were generated according to it. Finally, the elitism was used for the replacement step and the algorithm was stopped when the fitness of the best individual was equal to $n_{q}$. The computational results show that this algorithm is able to reach a good solution in a reasonable amount of time.

Hui et al. (2004) have proposed a hybrid EDA for solving the multiobjective 0-1 knapsack problem. For modelling the joint probability distribution, an UMDA is used. At each generation $t$, an individual is selected, based on the following probability, depending on the set of selected individuals at generation $t-1$ :

$$
p(x, t)=p(x / \text { selected individuals }(t-1))=\prod_{i=1}^{n_{q}} p\left(x_{i}, t\right)
$$

where $x \in\{0,1\}^{n_{q}}$.
The results showed that the EDA performed better than the Genetic Algorithm, both in convergence and in diversity.

Salhi et al. (2007) have proposed an EDA for hybrid flowshop scheduling problem with respect to the makespan criterion. The joint probability $p_{i j}(t)$ denotes the probability that the job $i$ is located on the position $j$ at the generation $t$ $(1 \leq i \leq n$ and $1 \leq j \leq n)$.

This probability was initially set to $1 / n^{2}$ and updated as follows:

$$
p_{i j}(t)=(1-\beta) \frac{1}{N} \sum_{k=1}^{N} I_{i j}\left(\pi_{k}\right)+\beta p_{i j}(t-1)
$$

where $\pi_{k}$ is the $k^{\text {th }}$ solution of the population at the generation $t(1 \leq k \leq N)$, $I_{i j}=\left\{\begin{array}{ll}1 & \text { if } \pi(i)=j \\ 0 & \text { otherwise }\end{array}\right.$ and $(0 \leq \beta \leq 1)$.

The obtained results were compared with those provided by two heuristic algorithms, a Random Key Genetic Algorithm and a Genetic Algorithm. The results show that EDA outperforms these two algorithms for the considered instances.

# 4 Problem Description 

In a blocking flowshop problem, there is a set of $n$ jobs to be processed on a set of $m$ machines in the same order, while having no intermediate buffers, i.e. a job $j \in\{1,2, \ldots, n\}$ cannot pass from machine $k \in\{1,2, \ldots ., m\}$ to machine $\mathrm{k}+1$ while the latter is busy. Since the makespan is the criterion to be minimized in our case, this problem can be denoted by $F_{m} /$ blocking $/ C_{\max }$ (Graham et al., 1979).

Let $p_{[j] k}$ denote the processing time of the job in the $j^{\text {th }}$ position in the sequence on the machine $k$ and $D_{[j] k}$ denote the departure time (starting time) of the job in the $j^{\text {th }}$ position in the sequence on the machine $k$.

The makespan $\left(C_{\max }\right)$ can be found through the recursive expression of the departure time, as follows:

$$
\begin{aligned}
& D_{[1] 0}=0 \\
& D_{[1] k}=\sum_{i=1}^{k} p_{[1] i} \quad k=1,2, \ldots ., m-1 \\
& D_{[j] 0}=D_{[j-1] 1} \quad j=2,3, \ldots ., n \\
& D_{[j] k}=\max \left\{D_{[j] k-1}+p_{[j] k}, D_{[j-1] k+1}\right\} \quad j=2,3, \ldots ., n, \quad k=1,2, \ldots ., m-1 \\
& D_{[j] m}=D_{[j] m-1}+p_{[j] m} \quad j=1,2, \ldots ., n
\end{aligned}
$$

Thus,

$$
C_{\max }=D_{(n) m-1}+p_{(n) m}
$$

## 5 Hybrid EDA for BFSP

In this section we present in detail an EDA to solve the Blocking Flowshop Scheduling Problem (BFSP), which is aimed at makespan minimization.

### 5.1 Solution Representation

For encoding the solution, we use the well-known representation scheme for the PFSP, that is the permutation of $n$ jobs, where the $j^{\text {th }}$ number in the permutation denotes the job located in position $j$.

# 5.2 Initial Population 

For generating the initial population of $P$ individuals, we propose to generate $P-1$ individuals randomly and we apply NEH algorithm, proposed by Nawaz et al. (1983), for the remaining element.

NEH can be described as follows:
Step1: The jobs are sorted with respect to the decreasing order of sums of their processing times.
Step2: Take the first two jobs and evaluate the two possible schedules containing them. The sequence with better objective function value is taken for further consideration.
Step 3: Take every remaining job in the permutation given in Step 1 and find the best schedule, by placing it at all possible positions in the sequence of jobs that are already scheduled.

### 5.3 Selection

In our algorithm, we adopted the same procedure of selection employed by Reeves (1995) for solving the flowshop scheduling problem. We describe this procedure as follows.

First, for each individual $p$, the fitness value $f(p)=\frac{1}{C_{\max }(p)}$ is calculated, second the individuals of the initial population are sorted in ascending order according to their fitness, i.e. the individual with a higher makespan value will be at the top of the list. Finally, a set of $Q$ individuals are selected from the sorted list.

### 5.4 Construction of a Probabilistic Model and Creation of New Individuals

The probabilistic model constitutes the main issue for an EDA and the performance of the algorithm is closely related to it (Lozano J.A et al., 2006), the best choice of the model is crucial. This step consists in building an estimation of distribution for the subset of $Q$ selected individuals.

In our algorithm, we select at random a sequence of jobs, denoted sr, from the set of $25 \%$ best solutions in the sorted list of sequences. Based on the priority rules of the order of the $q$ first jobs in the $s_{r}$, we determine the estimation of distribution model while taking into account both the order of the jobs in the sequence and the similar blocks of jobs presented in the selected parents. In fact, the parameter $q$ is an intensification parameter because, when it is possible, it leads to maintain the same structure of $q$ first jobs and setting it to a constant value preserves the linearity of the algorithm.

Let:

- $\eta_{j k}$ be the number of times of apparition of job $j$ before or in the position $k$ in the subset of the selected sequences augmented by a given constant $\delta_{1}$. The value of $\eta_{j k}$ refers to the importance of the order of the jobs in the sequence.

$-\mu_{j[k-1]}$ be the number of times of apparition of job $j$ after the job in the position $k-1$ in the subset of the selected sequences augmented by a given $\overline{\mathcal{E}}_{2} \cdot \mu_{j[k-1]}$ indicates the importance of the similar blocks of jobs in the sequences. In such way, we prefer to conserve the similar blocks as much as possible.

We note that $\overline{\mathcal{E}}_{1}$ and $\overline{\mathcal{E}}_{2}$ are two parameters used for the diversification of the solutions. Indeed, we employ these parameters in order to slow down the convergence of the algorithm.

- Let $\Omega_{k}$ be the set of $q$ first jobs not already scheduled following their order in $s_{r}$ until position $k$.

We define $\pi_{j k}$ the probability of selection of the job $j$ in the $k^{\text {th }}$ position by the following formula:

$$
\pi_{j k}=\frac{\eta_{j k} \times \mu_{j[k-1]}}{\sum_{l \in \Omega_{k}} \eta_{l k} \times \mu_{l[k-1]}}
$$

For each position $k$ in the sequence of a new individual, we select a job $j$ among the set of $q$ first jobs not already scheduled, following their order in $s_{r}$ by sampling from the probability distribution $\pi_{j k}$.

# 5.5 Replacement 

Replacement is the last phase in the EDA, it consists in updating the population. Therefore, at each iteration, $O$ offspring are generated from the subset of the selected parents. There are many techniques available to decide if the new individuals will be added to the population.

In our algorithm, we compare the new individual with the worst individual in the current population. If the offspring is best than this individual and the sequence of the offspring is unique, then the worst individual quits the population and is replaced with the new individual.

### 5.6 Stopping Criterion

The stopping condition indicates when the search will be terminated. Various stopping criteria may be listed, such as maximum number of generations, bound of time, maximum number of iterations without improvement, etc. In our algorithm, we set a maximum number of generations and a maximal computational time.

### 5.7 Local Search

To improve the performance of EDA, the successful way is to hybridize it with local search methods (Lozano J.A. et al., 2006). We propose to apply a local search algorithm as an improvement procedure, after the creation of a new individual.

We propose to restrict the application of the local search procedure to a part of individuals by employing a probability of improvement that depends on the quality of the subjected individual. We define this probability as follows:

Let $p^{c}=\exp \left(\frac{R D}{\alpha}\right)$ be the calculated probability for application of local search, where:

$$
R D=\left(\frac{f\left(x_{\text {current }}\right)-f\left(x_{\text {best }}\right)}{f\left(x_{\text {best }}\right)}\right)
$$

with $x_{\text {current }}$ denotes the created offspring and $x_{\text {best }}$ denotes the best solution found by the algorithm. For each individual, we draw at random a number between 0 and 1 . If this number is less than or equal to $p^{c}$, then we apply the local search procedure to the individual under consideration.

At each iteration of the local search procedure, we select one among two kinds of neighbourhoods randomly. The first one leads to choose two distinct positions $(i, j)$ at random, following the uniform distribution in the range $[1, n]$, and the jobs on these positions are exchanged. The second one consists in selecting at random a job $j$ from the sequence and inserting it on a random position $i$. This procedure will be repeated as far as reaching the maximal number of iterations iter $_{\text {max }}$.

# 6 Computational Results 

In this section, we discuss the performance of our proposed algorithms: EDA (without hybridization) and H-EDA. All computations for blocking flowshop scheduling problem, with respect to the makespan criterion, were implemented using C++ program and carried out on an Intel Pentium IV 3.2 GHz , RAM 512 MB based computer, running under Windows XP. In order to evaluate the performances of the proposed algorithms, the Taillard's instances were used for the flowshop scheduling problem (Taillard E., 1993). These instances consist of a set of 120 problems with sizes $m=5,10$ and 20 and $n=20,50,100,200$ and 500 . The performance measure employed in our numerical study was average relative percentage deviation in makespan $\Delta_{\text {average }}$ :

$$
\Delta_{\text {average }}=\frac{\sum_{i=1}^{R}\left(\frac{\text { Heu }_{i}-\text { Best }_{k n o w n}}{\text { Best }_{k n o w n}} \times 100\right)}{R}
$$

where $\mathrm{Heu}_{i}$ is the solution given by any of the R replications of the considered algorithms and Best $_{k n o w n}$ is the best solution provided by a competing algorithm for the specified problem or by one of our algorithms.

The parameters of the algorithms were fixed after a set of preliminary experiments, as follows: $P=60, \delta_{1}=\delta_{2}=4 / n$, the number of the selected parents $Q=3, q=20$, the

number of generated offspring $O=3$. Numerically, $p^{c}=0.5$ leads to accepting a sequence with a makespan superior by $5 \%$ relatively to the best value of makespan found.

So, $\beta=\frac{R D}{\log \left(p^{c}\right)}=\frac{0.01}{\log (0.5)}$ thereafter we determined $p^{c}$ according to this formula:

$$
p^{c}=\exp \left(\frac{R D}{\beta}\right)
$$

The maximum number of iterations of the local search procedure was set to $2 n^{2}$.

# 6.1 Comparison with GA 

For testing the efficiency of our proposed EDA (without local search) against another evolutionary algorithm, we have implemented the GA of Caraffa et al. (2001). For performing a meaningful comparison we have set the same stopping criterion of 1000 generations for both algorithms.

The obtained results for each class of instances, over $R=10$ replications, are given in Table 1. For the small instances, with $n<200$, in average, EDA outperforms GA both in terms of $\Delta_{\text {average }}$ and $\Delta_{\max }$, so, EDA can find better results than GA in average and worst case. Regarding $\Delta_{\text {min }}$ the two algorithms provide almost the same results. Also, for these instances, the range of changes for EDA solutions, i.e. the difference between $\Delta_{\min }$ and $\Delta_{\max }$, is smaller than that range for GA, in average, thus EDA is more robust than GA. For large instances, with $n=200$ and 500, EDA confirms its superiority, in terms of $\Delta_{\text {average }}$ and $\Delta_{\max }$, and it is better than GA for finding the best results $\left(\Delta_{\min }\right)$. Although EDA is better than GA in term of solution quality, the latter appears faster after 1000 generations (Table 6).

Table 1. Comparison between EDA and GA

Table 2. Results of H-EDA for 20 jobs instances

# 6.2 Performance of H-EDA 

The performance of H-EDA is evaluated against the representative approaches developed for the same problem. The competing algorithms are the branch and bound algorithm of Ronconi (2005) and the Tabu Search of Grabowski and Pempera (2007), denoted by RON and TS+M respectively. We set the CPU time limit of each replication to $(n \times m) \times 20 / 3$ seconds.

Table 2 to Table 5 present the results found by our H-EDA. First, in total, our algorithm has improved 109 solutions out of 120 and, even for the 11 remaining instances,

Table 3. Results of H-EDA for 50 jobs instances

it can reach 9 upper bounds found by TS+M. Additionally, the most important improvement occurs for the instances with the size larger than 20. Especially when $n=$ 50, 100 and 200, H-EDA has improved all upper bounds provided by previous approaches. In other hand, concerning the CPU time, in average, when we take into account the difference between the computer characteristics, H-EDA is faster than the TS+M approach (Table 6).

Table 4. Results of H-EDA for 100 jobs instances

Table 5. Results of H-EDA for 200 and 500 jobs instances
Table 6. Computational times

# 7 Conclusion 

In this chapter, we have proposed a hybrid EDA algorithm to minimize the makespan in the blocking flowshop scheduling problem. The probabilistic model built for our EDA depends on both the order of the jobs in the sequence and the similar blocks of jobs presented in the set of selected parents. A local search procedure is added to the EDA as an improvement phase, after creating a new individual. The computational results show that our proposed EDA, without hybridization, performs better than a GA previously developed for the same problem in terms of solution quality. However the GA outperforms our algorithm when 1000 generations are set as stopping criterion for both algorithms.

Also, by comparing the hybrid algorithm against competing approaches available in the literature, it's seen that our algorithm is better than these approaches, both in terms of solution's quality and computational times and it seems able to improve best known solutions.
