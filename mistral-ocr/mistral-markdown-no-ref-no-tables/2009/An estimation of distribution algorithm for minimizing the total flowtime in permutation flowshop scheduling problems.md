# An estimation of distribution algorithm for minimizing the total flowtime in permutation flowshop scheduling problems 

Bassem Jarboui ${ }^{a}$, Mansour Eddaly ${ }^{a}$, Patrick Siarry ${ }^{\mathrm{b}, *}$<br>${ }^{a}$ FSEGS, route de l'ahreport km 4, Sfax 3018, Tunisia<br>${ }^{b}$ LISSI, Université de Paris 12, 61 avenue du Général de Gaulle, 94010 Créteil, France

## A R T I C L E I N F O

Available online 21 November 2008
Keywords:
Estimation of distribution algorithm
Variable neighbourhood search
Scheduling
Permutation flowshop
Flowtime

## A B S T R A C T

In this work we propose an estimation of distribution algorithm (EDA) as a new tool aiming at minimizing the total flowtime in permutation flowshop scheduling problems. A variable neighbourhood search is added to the algorithm as an improvement procedure after creating a new offspring. The experiments show that our approach outperforms all existing techniques employed for the problem and can provide new upper bounds.
(c) 2008 Elsevier Ltd. All rights reserved.

## 1. Introduction

In a permutation flowshop scheduling problem (PFSP), there is a set of $n$ jobs that must be processed on a set of $m$ machines in the same order, such that each job is processed on machine 1 in first place, machine 2 in second place, $\ldots$, and machine $m$ in the last place. Gupta and Stafford [1] have presented a review of developments in flowshop scheduling over the last fifty years. They have listed the assumptions regarding the flowshop scheduling problem in general and the permutation flowshop scheduling problem in particular. The processing times are fixed, known in advance and have non-negative values. All jobs are available for processing at time 0 and all machines are available over the scheduling period. In addition, each machine can process at most one job and each job can be processed on at most one machine. Besides, no pre-emption is allowed, i.e., once the processing of a job on a machine has started, it must be completed without interruption. The most common criteria are the makespan and the total flowtime. This paper addresses the total flowtime (TFT) performance measure. This criterion measures the time a job stays in the system, minimizing that time leads to maximizing the utilization of resources. Concerning its complexity, the PFSP has been proved to be NP-complete in the strong sense for more than two machines (Garey et al. [2]).

Diverse approaches were proposed to solve this problem with respect to TFT criterion, including exact algorithms such as branch and bound algorithm (Chung et al. [3], Velde [4], Bansal [5], Ignal and Schrage [6]), constructive heuristics (Woo and Yim [7], Framinan

[^0]and Leisten [8], Liu and Reeves [9], Ho and Gupta [10], Framinan et al. [11], Rajendran [12], Allahverdi and Aldowaisan [13], Li et al. [14]) and metaheuristics like genetic algorithm (GA) (Vempati et al. [15], Zhang et al. [16]), ant colony optimization (ACO) (Gajpal and Rajendran [17], Rajendran and Ziegler [18]) and particle swarm optimization (PSO) (Jarboui et al. [19], Tasgetiren et al. [20]).

Estimation of distribution algorithm (EDA) was introduced by Mühlenbein and Paaß [21]. It constitutes a new tool of evolutionary algorithms (Larranaga and Lozano [22]) based on the probabilistic model learned from a population of individuals. Starting with a population of individuals (candidate solutions), generally generated randomly, this algorithm selects good individuals with respect to their fitness. Then a new distribution of probability is estimated from the selected candidates. Next, new offspring is generated from the estimated distribution. The process is repeated until the termination criterion is met.

In order to improve the quality of EDA solution, it is recommended to use a local search algorithm (Lozano et al. [23]). We propose to use the variable neighbourhood search (VNS) (Mladenović and Hansen [24], Hansen and Mladenović [25]) to improve the performance of our EDA.

This paper is organized as follows: Section 2 presents a formulation of the permutation flowshop scheduling problem. Section 3 describes the basic estimation of distribution algorithm. The EDA for the PFSP is presented in Section 4. Section 5 presents the hybrid EDA. The computational results are presented in Section 6 and a conclusion is given in Section 7.

## 2. The permutation flowshop scheduling problem (PFSP)

In a PFSP, there is a set of $n$ jobs to be processed through a set of $m$ machines, where each job $j(j=1,2, \ldots, n)$ passes through


[^0]:    * Corresponding author.

    E-mail addresses: bassem_jarboui@yahoo.fr (B. Jarboui), eddaly.mansour@gmail.com (M. Eddaly), siarry@univ-paris12.fr (P. Siarry).

the machines $1,2, \ldots, m$ in that order, without interruption of the processing (no pre-emption). Referring to the notation of Graham et al. [26] $(\alpha / \beta / \gamma)$, the PFSP for TFT criterion is denoted by $F /$ permu/TFT. Let $p_{i j}$ be the processing time for the job $j$ on the machine $i(i=1,2, \ldots, m)$, and $C_{i j}$ denote the completion time of job $j$ on machine $i$. Then $C_{[j] i}$ is the completion time of the job scheduled in the $j$ th position in the sequence on machine $i . C_{[j] i}$ is computed as: $C_{[j] i}=p_{[j] i}+\max \left|C_{[j] i-1}, C_{[j-1] i}\right|$. So, we can obtain the TFT as follows: $T F T=\sum_{j=1}^{n} C_{[j] m}$.

## 3. Estimation of distribution algorithm (EDA)

In 1996, a new tool of evolutionary algorithms, called "Estimation of Distribution Algorithm" (Mühlenbein and Paaß [21], Larranaga and Lozano [22]), was proposed. Unlike other approaches of evolutionary algorithms, EDA uses neither crossover nor mutation. Therefore, it generates new offspring according to a probabilistic model learned from a population of parents. The main steps of the canonical EDA are described as follows (Lozano et al. [23]): first, a random initial population is commonly used. Second, a subpopulation of $Q$ parent individuals is selected with a selection method based on the fitness function. Third, the probability of distribution of the selected parents is estimated by a probabilistic model. Fourth, new offspring are generated according to the estimated probability. Finally, some individuals in the current population are replaced with new generated offspring. These steps are repeated until one stopping criterion is met. In the combinatorial context, several EDA applications were developed, such as knapsack problem, travelling salesman problem, clustering and jobshop scheduling problems (Larranaga and Lozano [22]).

## 4. Our proposed EDA for PFSP

For solving the PFSP with respect to the TFT minimization, our proposed solution algorithm is based on the EDA. A new way for the design of the probabilistic model is proposed and the framework of the algorithm is introduced hereafter for discussion.

### 4.1. Solution representation and initial population

The well-known job based encoding scheme is frequently used in the literature of the PFSP, so it is also used in our algorithm. In this representation, the $j$ th number in the permutation denotes the job located in position $j$. In order to guarantee the diversification in the population, we use an initial random population of $P$ individuals, uniformly distributed.

### 4.2. Selection

In our algorithm we adopted the selection procedure of Reeves [27] for solving the flowshop scheduling problem. We describe this procedure as follows:
(i) first, for each individual $p$, calculate the fitness value $f(p)=$ $1 / T F T(p)$; (ii) second, the individuals of the initial population are sorted in ascending order according to their fitness, i.e. the individual with a higher TFT value will be at the top of the list. Finally, the selection of parents is made relatively to the probability:
$\operatorname{prob}(r)=\frac{2 r}{P(P+1)}$
where $r$ is the rank of the $r$ th individual in the sorted list.

### 4.3. Probabilistic model and creation of new individuals

The probabilistic model constitutes the main issue for EDA and the performance of the algorithm is closely related to it (Lozano et al. [23]), the best choice of the model is crucial. This step consists in building an estimation of distribution for the subset of $Q$ selected individuals. In our algorithm, we determine the estimation of distribution model while taking into account both the order of the job in the sequence and the similar blocks of jobs presented in the selected parents.

Let:

- $\eta_{j k}$ be the number of times of appearance of job $j$ before or in the position $k$ in the subset of the selected sequences augmented by a given constant $\delta_{1}$. The value of $\eta_{j k}$ refers to the importance of the order of the jobs in the sequence.
- $\mu_{[j k-1]}$ be the number of times of appearance of job $j$ immediately after the job in the position $k-1$ in the subset of the selected sequences augmented by a given $\delta_{2} . \mu_{j[k-1]}$ indicates the importance of the similar blocks of jobs in the sequences. In such way, we prefer to conserve the similar blocks as much as possible.

We note that $\delta_{1}$ and $\delta_{2}$ are two parameters used for the diversification of the solutions. Indeed, we employed these parameters in order to slow down the convergence of the algorithm.

- $\Omega_{k}$ : the set of jobs not already scheduled until position k .

We define $\pi_{j k}$ the probability of selection of the job $j$ in the $k$ th position by the following formula: $\pi_{j k}=\eta_{j k} \times \mu_{[j k-1]} / \sum_{i \in \Omega_{k}}\left(\eta_{j k} \times\right.$ $\mu_{[j k-1]}$ ). According to this probability, for each position $k$, we select a job $j$ from the set of not already scheduled jobs in the sequence of a new individual.

### 4.4. Replacement

Replacement is the last phase in the EDA, it consists in updating the population. Therefore, at each iteration, $O$ offspring are generated from the subset of the selected parents. There are many techniques for deciding if the new individuals will be added to the population.

In our algorithm, we compare the new individual with the worst individual in the current population. If the offspring is best than this individual and the sequence of the offspring is unique, then the worst individual is removed from the population and will be replaced with the new individual.

### 4.5. Stopping criterion

The stopping condition indicates when the search will be terminated. Various stopping criteria may be listed, such as maximum number of generations, bound of time, maximum number of iterations without improvement, etc. We set a maximum number of iterations and a maximal computational time in our algorithm.

## 5. Hybrid EDA for PFSP (EDA-VNS)

Aiming at improving the performance of EDA and preventing it from being stuck into a local optimum, a successful way is to hybridize it with local search methods (Lozano et al. [23]). We propose to apply a VNS algorithm (Mladenović and Hansen [24], Hansen and Mladenović [25]) as an improvement procedure after the creation of a new individual.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Pseudo code of swap local search procedure.
procedure insert_local_search $\left(x_{n}\right)$
$x_{\text {loc }}=x_{n} ; \quad / / x_{\text {loc }}$ is the best solution obtained by insert local search procedure
set $i=1 ;$
do
set $j=1 ;$
while $(j \leq n)$
$x^{\prime}=$ permute the jobs in the positions $i$ and $j$ in $x_{\text {loc }}$.
if $\left(T F T\left(x^{\prime}\right)<T F T\left(x_{\text {loc }}\right)\right)$ then // check the improvement of best solution
$x_{\text {loc }}=x^{\prime} ;$
$i=i-1 ;$
$j=1 ;$
else
$j=j+1 ;$
endif
endwhile
$i=i+1 ;$
if $(i>n)$ then $i=1 ;$
until (no possible improvement)
return $x_{\text {loc }} ;$
end
Fig. 2. Pseudo code of insert local search procedure.

### 5.1. Variable neighbourhood search algorithm

For the application of VNS algorithm, we propose to restrict it to a subset of the individuals by employing a probability of improvement that depends on the quality of the related individual. We define this probability as follows:

Let $p^{L}=\max \left(\exp \left(R D / x\right), c\right)$ be the calculated probability for application of VNS where $R D=\left\{f\left(x_{\text {current }}\right)-f\left(x_{\text {best }}\right)\right\} / f\left(x_{\text {best }}\right), x_{\text {current }}$ denotes the created offspring and $x_{\text {best }}$ denotes the best solution found by the algorithm. For each individual, we draw at random a number between 0 and 1 . If this number is less than or equal to $p^{L}$, then we apply VNS to the individual under consideration.

We select two structures of neighbourhoods, called swap_local _search and insert_local_search. The first one leads to all possible swaps of pairs of job's positions (i,l), where $1 \leqslant i<l \leqslant n$, within all parts of solutions (Fig. 1). If the swap moves were performed and a local optimum was found, the second structure of neighbourhood consists of all possible insert moves of pairs of positions of jobs (i,l), within all parts of the so obtained solution (Fig. 2). Then, we return to the swap_local_search with the improved solution as a current solution, i.e., the local optimum resulted after the application of the insert_local_search. We reapply this procedure until no improvement in the solution.

If the obtained solution is better than the best solution, then we replace the latter with the new solution and we reinitialize the number of iterations at 0 , else we increment the number of iterations. Next, we select two distinct positions (i,j) at random following the uniform distribution in the range $[1, n]$ from $x_{\text {best }}$, and the jobs on these positions are exchanged. The whole procedure is repeated as far as reaching the maximal number of iterations (itermax). The pseudo code of the VNS algorithm is given in Fig. 3.

## 6. Computational results

The algorithms were coded in C++ programming language. All experiments were run on a desktop PC with Intel Pentium IV, Windows XP, 3.2 GHz processor and 1 GB memory. For the evaluation of the results, the benchmark problems from Taillard [28] were considered, with $m=5,10$ and 20 and $n=20,50$ and 100 .

The performance measure employed in our numerical study was $\Delta_{\text {average }}$, the average relative percentage deviation in TFT:
$\Delta_{\text {average }}=\frac{\sum_{i=1}^{R}\left(\frac{\text { Heu }_{i}-\text { Best }_{\text {known }}}{\text { Best }_{\text {known }}}\right.}{R} \times 100)$

procedure $V N S\left(x_{n}\right)$

$$
\begin{aligned}
& x_{\text {best }}=x_{n} ; \\
& x_{\text {curve }}=x_{n} ; \\
& \text { do } \\
& \text { do } \\
& x^{\prime} \quad=\text { swap }_{-} \text {local }_{-} \text {search }\left(x_{\text {curve }}\right) ; \\
& x_{\text {curve }}=\text { insert }_{-} \text {local }_{-} \text {search }\left(x^{\prime}\right) \text {; } \\
& \text { until (no possible improvement) } \\
& \text { if }\left(T F T\left(x_{\text {curve }}\right)<T F T\left(x_{\text {best }}\right)\right) \text { then } \quad / / \text { check the improvement of best solution } \\
& x_{\text {best }}=x_{\text {curve }} ; \\
& \text { endif } \\
& x_{\text {curve }}=x_{\text {best }} ; \\
& \text { find } i \text { and } j \text { randomly and permute the jobs in the positions } i \text { and } j \text { in } x_{\text {curve }} \\
& \text { until (stopping criterion is found) } \\
& \text { return } x_{\text {best }} ; \\
& \text { end }
\end{aligned}
$$

Fig. 3. Pseudo code of VNS algorithm.

Table 1
Best known solutions

where $\mathrm{Heu}_{i}$ is the solution given by any of the $R$ replications of the considered algorithms and Best ${ }_{\text {known }}$ is the best known solution provided so far by an existing algorithm for the specified problem or by one of our proposed algorithms. Table 1 shows the best known solution for each instance and the corresponding algorithms that have provided it. We note that the bold numbers indicate that the best known solutions were provided by one of our proposed algorithms.

The heuristics used for benchmarking are the representative heuristics available in the literature of the PFSP with respect to the TFT criterion. These approaches consist of composite heuristics GA of Vempati et al. [15], BES (LR) of Liu and Reeves [9], ant colony algorithms (M-MMAS and PACO) of Rajendran and Ziegler [18], particle swarm algorithm (PSOvns) of Tasgetiren et al. [20], combinatorial particle swarm optimization algorithm (H-CPSO) of Jarboui
et al. [19], hybrid genetic algorithm (HGA) of Zhang et al. [16] and the composite heuristic (ICH2 ) of Li et al. [14].

### 6.1. Comparison of the proposed EDA with GA

In this section, we perform a comparison of our EDA, without VNS algorithm, with a GA, thus, we have implemented the GA of Vempati et al. [15]. We note that, to the best of our knowledge, this is the only GA, without hybridization process, developed for the PFSP for minimizing the TFT criterion.

Here, the parameters of the EDA were fixed experimentally as follows: $P=60, \delta_{1}=\delta_{2}=4 / n$, the number of the selected parents $Q=3$, the number of offspring generated $O=3$. The number of replications of each algorithm was set to $R=100$.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Comparison results between EDA and GA for $(20 \times 5)$ instances.
![img-3.jpeg](img-3.jpeg)

Fig. 5. Comparison results between EDA and GA for $(20 \times 10)$ instances.
![img-3.jpeg](img-3.jpeg)

Fig. 6. Comparison results between EDA and GA for $(20 \times 20)$ instances.

Table 2
Comparison of EDA and GA
Table 3
Results for the instances with $n=20, m=5,10$ and 20

Figs. 4-6 present the results obtained by both algorithms in the generation space for the benchmarks with 20 jobs $(\lfloor 20 \times 5\rfloor,\lfloor 20 \times$ 10) and $(20 \times 20)$ ). They report the average percentage deviation according to the number of generations for EDA and GA. In fact, the EDA outperforms the GA of Vempati et al. [15] in term of solution quality. Furthermore, EDA can provide high quality solutions rapidly over the first 200 generations.

Table 2 shows the results obtained by EDA and GA after 1000 generations tested on the 90 benchmark problems from Taillard. Although EDA is better than GA of Vempati et al. [15] in term of solution quality, the GA appears more efficient in terms of CPU time because it requires a linear time to create
new individual, whereas this task requires $O\left(n^{2}\right)$ time for the EDA.

### 6.2. Relative performances of VNS and EDA-VNS

In this section, we discuss the relative performances of our proposed algorithms (VNS, EDA-VNS) compared with existing approaches. All the parameters of the algorithms are set experimentally: $P=10, \delta_{1}$ and $\delta_{2}$ are equal to $4 / n, Q=3$ and $O=3$. We fixed parameter $\alpha$ according to the relative deviation $R D$ between the current solution and the best solution found by the algorithm and the

Table 4
Results for the instances with $n=20, m=5,10$ and 20

calculated probability $p^{c}$. Numerically, $p^{c}=0.5$ leads to accepting a sequence with a TFT superior by $1 \%$ relatively to the best value of TFT found. So, $\alpha=R D / \log \left(p^{c}\right)=0.01 / \log (0.5)$, thereafter we determined $p^{c}$ according to this formula: $p^{c}=\max \left(\exp (R D / \alpha), \varepsilon\right)$ with $\varepsilon=0.01$. The maximum number of iterations of VNS algorithm (itermax) was set at 50. In our case, we set a maximal computational time equal to $n=m \times 0.4$ seconds as a stopping criterion. We set the number of replications of our algorithms to $R=5$, similarly to the compared approaches.

Tables 1-6 show the results provided by our proposed approaches (VNS and EDA-VNS) compared with the results given by BES (LR) of Liu and Reeves [9], ant colony algorithms (M-MMAS and PACO) of Rajendran and Ziegler [18], particle swarm optimization algorithm (PSOvns) of Tasgetiren et al. [20] and combinatorial particle swarm optimization algorithm (H-CPSO) of Jarboui et al. [19].

As seen in Table 1, our VNS and EDA-VNS have in total improved 49 solutions among 90. Therefore, 26 out of 49 best known solutions were generated by VNS algorithm, whereas 24 were generated by EDA-VNS. Moreover, both algorithms were able to reach all best known solutions. In addition, most significantly improved solutions of EDA-VNS occur in large instances ( $n=50$ and 100) with 50 improved instances out of 60.

Tables 3-5 present the minimum, average and maximum deviations of different approaches, over 5 runs, for the instances with $n=$ $20, n=50$ and $n=100$, respectively. In average, it was shown through $\Delta_{\text {max }}$ performance measure that the worst solutions provided by EDA-VNS are better than or equal to the best solutions found by BES(LR), MMAS and PACO over 5 runs. Also, $\Delta_{\text {max }}$ of EDA-VNS is less than or equal to the best results of PSOvns and H-CPSO, for 78 in-
stances and 68 instances, respectively. Table 3 shows that EDA-VNS can reach the best solutions over the five runs for all instances with $n=20$. This result proves the robustness of EDA-VNS for the instances with small sizes.

By comparing EDA-VNS and VNS, it was shown that, in average, EDA-VNS performs better than VNS algorithm for the instances with a size lower than 100 jobs, but for the remaining sizes (Table 5), VNS outperforms EDA-VNS for the instances with $m=5$ and 10 and these two algorithms are very close for $m=20$. In term of $\Delta_{\min }$, in average, the EDA-VNS and VNS results are globally very similar. The standard deviation values of the relative percentage of difference in the solutions $\left(\Delta_{\text {std }}\right)$ are provided to give an idea about the robustness of the algorithms. $\Delta_{\text {std }}$ values of EDA-VNS are smaller than the ones of VNS for all experimental runs (Tables 3-5), thus the hybridization process provides more stability to the algorithm. Concerning the CPU times, VNS and EDA-VNS appear similar in average (Table 6).

Now, we present the comparative results between our EDA-VNS and HGA of Zhang et al. [16] and ICH2 of Li et al. [14]. This comparative study was based on the values of $\Delta_{\text {average }}$ computed according to the upper bounds given in Zhang et al. [16]. Table 7 summarizes the results found using EDA-VNS, HGA and ICH2, in term of the average value, for each instance size. It appears that EDA-VNS outperforms HGA and ICH2 for all sizes of instances.

## 7. Conclusion

An EDA for the PFSP was presented in this work with the objective to minimize the TFT. The initial population is generated randomly. The probabilistic model built focuses on both the importance of the

Table 5
Results for the instances with $n=50, m=5,10$ and 20

Table 6
Computational times of the VNS and EDA-VNS algorithms

Table 7
Comparison of EDA-VNS with ICH2 and HGA

order of the jobs in the sequences and the similar blocks of jobs presented in the selected parents. After creating new individuals based on the estimated model, we introduced an improvement procedure by using a VNS algorithm. The experiments show that our algorithms outperform other methods employed for the problem. For the small benchmarks, EDA-VNS is better than VNS but, for the large ones, VNS is superior both in terms of solution quality and computational time.
