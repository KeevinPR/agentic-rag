# A discrete artificial bee colony algorithm for the total flowtime minimization in permutation flow shops 

M. Fatih Tasgetiren ${ }^{\mathrm{a}}$, Quan-Ke Pan ${ }^{\mathrm{b}, *}$, P.N. Suganthan ${ }^{\mathrm{c}}$, Angela H-L Chen ${ }^{\mathrm{d}}$<br>${ }^{a}$ Department of Industrial Engineering, Yasar University, Bornova, Izmir, Turkey<br>${ }^{\text {b }}$ College of Computer Science, Liaocheng University, Liaocheng, 252059, PR China<br>${ }^{c}$ School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore<br>${ }^{d}$ The Department of Finance, Nanya Institute of Technology, Taoyuan 320, Taiwan, ROC

## A R T I C L E I N F O

Article history:
Received 16 February 2010
Received in revised form 4 April 2011
Accepted 10 April 2011
Available online 21 April 2011

Keywords:
Permutation flowshop scheduling problem
Iterated greedy algorithm
Discrete differential evolution algorithm
Discrete artificial bee colony algorithm
Estimation of distribution algorithm
Genetic local search

## A B S T R A C T

Obtaining an optimal solution for a permutation flowshop scheduling problem with the total flowtime criterion in a reasonable computational timeframe using traditional approaches and optimization tools has been a challenge. This paper presents a discrete artificial bee colony algorithm hybridized with a variant of iterated greedy algorithms to find the permutation that gives the smallest total flowtime. Iterated greedy algorithms are comprised of local search procedures based on insertion and swap neighborhood structures. In the same context, we also consider a discrete differential evolution algorithm from our previous work. The performance of the proposed algorithms is tested on the wellknown benchmark suite of Taillard. The highly effective performance of the discrete artificial bee colony and hybrid differential evolution algorithms is compared against the best performing algorithms from the existing literature in terms of both solution quality and CPU times. Ultimately, 44 out of the 90 best known solutions provided very recently by the best performing estimation of distribution and genetic local search algorithms are further improved by the proposed algorithms with short-term searches. The solutions known to be the best to date are reported for the benchmark suite of Taillard with longterm searches, as well.
(c) 2011 Elsevier Inc. All rights reserved.

## 1. Introduction

Flowshop scheduling is among the most prevalent problems in the field of deterministic scheduling in engineering industries [3,14,22,29,47]. The permutation flowshop represents a particular case in which solutions are represented by the permutations of $n$ jobs, i.e., $\pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right\}$. Each job comprises a set of $m$ operations that must be performed by different machines. Each machine can process only one operation at a time. While all jobs have the same permutations on every machine, these jobs, once initiated, cannot be interrupted (preempted), and the release times of all jobs are zero. Given the processing time $p_{i k}$ for job $j$ on machine $k$, we consider the total flowtime criterion as the objective function to be minimized.

In the above specified context, $F\left(\pi_{j}\right)$, denoted by the flowtime of job $\pi_{j}$, is equivalent to the completion time $C\left(\pi_{j}, m\right)$ of job $\pi_{j}$ on the last machine $m$ because the release times of all jobs are zero. As a result, the total flowtime $\operatorname{TFT}(\pi)$ of a permutation $\pi$ can be computed by summing up flowtimes or completion times of all jobs and defined as $\operatorname{TFT}(\pi)=\sum_{j=1}^{m} F\left(\pi_{j}\right)=$ $\sum_{j=1}^{m} C\left(\pi_{j}, m\right)$. Then the optimal permutation $\pi^{-}=\left\{\pi_{1}^{-}, \pi_{2}^{-}, \ldots, \pi_{n}^{-}\right\}$in the set of all permutations of $\Pi$ is determined by

[^0]
[^0]:    * Corresponding author.

    E-mail addresses: fatih.tasgetiren@yasar.edu.tr (M.F. Tasgetiren), panquanke@gmail.com (Q.-K. Pan), epmsugan@ntu.edu.sg (P.N. Suganthan), achen@nanya.edu.tw (A.H-L Chen).

$\operatorname{TFT}\left(\pi^{*}\right) \leqslant \operatorname{TFT}(\pi)$ for each permutation $\pi$ belonging to $\Pi$. Under these specifications, the completion time for the $n$-job and $m$ machine problem is computed as follows:

$$
\begin{aligned}
& C\left(\pi_{1}, 1\right)=p_{\pi_{1}, 1} \\
& C\left(\pi_{j}, 1\right)=C\left(\pi_{j-1}, 1\right)+p_{\pi_{j}, 1} \quad j=2, \ldots, n \\
& C\left(\pi_{1}, k\right)=C\left(\pi_{1}, k-1\right)+p_{\mu_{1}, k} \quad k=2, \ldots, m \\
& C\left(\pi_{j}, k\right)=\max \left\{C\left(\pi_{j-1}, k\right), C\left(\pi_{j}, k-1\right)+p_{\pi_{j}, k}\right\} \quad j=2, \ldots, n ; \quad k=2, \ldots, m
\end{aligned}
$$

Many different algorithms have been proposed over time in an attempt to find the exact solution to minimizing the total flowtime (TFT). Several variants of branch and bound algorithms were developed [4,5,11,41]; Ignall and Scharge [11] were the first to apply the branch and bound scheme based on two lower bounds in the two-machine flow shop problem. Then Bansal [4] extended their idea to the $m$-machine case. Recent publications [5,41] have detailed the development of lower bounding methods either based on Lagrangian relaxation or by introducing slack variables. These exact methods have been successfully implemented in a limited number of small instances due to lengthy execution times. For large instances in the $n$ job and $m$ - machine total flowtime problem, some efficient heuristics have been developed in [2,7,8,10,23,26,31,45]. The NEH constructive method, proposed by Nawaz et al. [28], was claimed to be the best for makespan minimization in flow shops, but not effective for total flowtime minimization. Therefore, to minimize total flowtime, the heuristics in both Woo and Yim [45] and Framinan and Leisten [7] were founded on different insertion schemes from NEH. Furthermore, a composite heuristic proposed by Allahverdi and Aldowaisan [2] adopted the insertion with pair-wise exchange from Framinan and Leisten [7] to improve their solutions. So far, no heuristic is optimal for total flowtime minimization. In comparison to heuristic methods, metaheuristic methods always obtain better results, as they compose many different kinds of algorithmic components [9,12,21,27,32,42,43,46,48]. Very recently, an estimation of distribution algorithm (EDA) hybridized with variable neighborhood search (VNS) has been introduced in [13]. In addition to EDA, two genetic local search algorithms have been proposed in [24,25]. The first one employs a local search called insertion search with cut and repair, denoted by hGLS, and the second one is the genetic algorithm hybridized with a tabu search, denoted by tsGLS. These three algorithms improved almost all the best known solutions in the existing literature.

Among metaheuristics, modeling the collective behavior of self-organized systems and applying these models to solve real-world problems has been ongoing and has become a class of its own, known as swarm intelligence. Earlier works implementing the ant colony optimization (ACO) and particle swarm optimization (PSO) algorithms were conducted to simulate the swarm behavior of ant colonies and flocks of birds, respectively. Recently, some algorithms were proposed by modeling the specific intelligent behaviors of honeybee swarms [1,15-19,29,40,44]. Karaboga in [15-19] introduced an artificial bee colony (ABC) algorithm to optimize multi-variable and multi-modal continuous functions. Numerical comparisons demonstrated that the performance of the ABC algorithm is as competitive as other population-based algorithms with the advantage of employing fewer control parameters [15-19]. Furthermore, a discrete version of the ABC algorithm has been recently applied to the lot-streaming flowshop scheduling problem in [29]. Tereshko attempted to model the forage behavior of a honeybee colony based on reaction-diffusion equations [40]. Wede and Farooq proposed a routing algorithm, called BeeAdHoc, for energy efficient routing in mobile ad hoc networks [44]. Clearly, swarm intelligence can be understood as an algorithmic framework inspired by the aggregate behavior of the social insects and animals [1]. It has drawn the attention of researchers because of its advantages such as scalability, fault tolerance, adaptation, speed, modularity, autonomy, and parallelism [20].

As there is no detailed work that describes the use of the ABC algorithm to deal with the PFSP under the TFT criterion, we present a novel discrete ABC (DABC) algorithm as well as the hybrid version of our previous discrete differential evolution (hDDE) algorithm in [30] in order to solve the PFSP with the TFT criterion in this paper. The proposed algorithms are hybridized with a local search procedure, denoted by LocalSearch() based on swap and insertion neighborhood structures. The main purpose of the hybridization stems from the fact that DABC and DDE carry out the global search by exploration of the search space, whereas local search is responsible for intensifying the search on the local minima. Therefore, the balance in global and local searches has been effectively achieved. Through an experimental analysis, it is shown that the performance of the proposed algorithms is as competitive as the recent three best performing algorithms in terms of solution quality and CPU usage time. Ultimately, 44 out of the 90 best-known solutions recently provided by the EDA, tsGLS, and hGLS algorithms are further improved by the proposed algorithms with short-term search. For long-term search, the new best-known solutions are reported for Taillard's benchmark suite [35].

The remaining paper is organized as follows. Section 2 introduces the DABC; and Section 3 presents the hDDE algorithm. The details of the local search algorithms developed for the PFSP with TFT criterion are provided in Section 4. Section 5 discusses the computational results over benchmark problems. Finally, Section 6 comprises the concluding remarks.

# 2. Discrete artificial bee colony algorithm 

Inspired by the intelligent foraging behaviors of honeybee swarms, Karaboga proposed the artificial bee colony (ABC) algorithm that implemented a new swarm intelligence based optimizer [15-19]. It classifies foraging artificial bees into three groups, namely, employed bees, onlookers, and scouts. An employed bee is responsible for flying to and making

collections from the food source which the bee swarm is exploiting. An onlooker waits in the hive and decides on whether a food source is acceptable or not. This is done by watching the dances performed by the employed bees. A scout randomly searches for new food sources by means of some internal motivation or possible external clue. In the ABC algorithm, each solution to the problem under consideration is called a food source and represented by an $n$-dimensional real-valued vector where the fitness of the solution corresponds to the nectar amount of the associated food resource. As with other intelligent swarm-based approaches, the ABC algorithm is an iterative process. The approach begins with a population of randomly generated solutions (or food sources); then, the following steps are repeated until a termination criterion is met [15-19]:

1. Initialize the foraging process.
2. Send the employed bees to exploit the discovered food sources.
3. Using the onlooker bees, choose the food sources and determine their nectar amounts.
4. Send scouts to search for new food sources.
5. Remember the best food source found so far.
6. If a termination criterion has not been satisfied, go to step 2 ; otherwise stop the procedure and report the best food source found so far.

However, the above ABC algorithm, originally designed for the continuous nature of optimization problems, cannot be used for discrete/combinatorial cases; therefore, in this work, some modifications to the above ABC algorithm have been made for the discrete version, as described below.

# 2.1. Initialization 

In the hDDE and DABC algorithms, the solution is represented by a permutation of jobs $\pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right\}$. For $N P$ individuals, the initial population is generated in such a way that the first solution is established by the NEH heuristic of [28], and the rest of the solutions are constructed randomly.

The NEH heuristic has two phases. In the first phase, jobs are ordered in descending sums of their processing times. In the second phase, a job permutation is established by evaluating the partial permutations based on the initial order of the first phase. Suppose a job permutation is already determined for the first $k$ jobs; then, $k+1$ partial permutations are constructed by inserting job $k+1$ in the $k+1$ possible slots of the current permutation. The partial permutation with the minimum total flowtime is kept as the current permutation for the next iteration. Then, job $k+2$ from the first phase is considered. This is repeated until all of the jobs have been sequenced.

### 2.2. Employed bee phase

According to the basic ABC algorithm, the employed bees generate food sources in the neighborhood of their current positions. From prior literature, we know that two common operators, insert and swap, are used to generate neighboring solutions [33]. The insert operator removes a job from its original position $j$ of a permutation $\pi$, and then inserts this job into another position $k$ such that $(k \in(j, j-1])$, whereas the swap operator produces a neighbor by interchanging two jobs of a permutation $\pi$. By adjusting the perturbation strength $p$ of the insert and swap operators as well as the destruction size $d$ of the destruction and construction procedures, denoted as DestructConstruct( $($ ), six neighboring strategies denoted as $S_{i}$ are separately formulated by borrowing them from the iterated greedy (IG_RS) algorithm in [33] and the iterated local search (ILS) algorithm in [6]. These methods are then utilized to generate neighboring food sources for the employed bees as follows:
$S_{1}$ : Performing one insert move $(p=1)$ to a permutation $\pi$.
$S_{2}$ : Performing one swap move $(p=1)$ to a permutation $\pi$.
$S_{3}$ : Performing two insert moves $(p=2)$ to a permutation $\pi$.
$S_{4}$ : Performing two swap moves $(p=2)$ to a permutation $\pi$.
$S_{5}$ : Performing a DestructConstruct( $)$ procedure with the destruction size of $d=8$.
$S_{6}$ : Performing a DestructConstruct( $)$ procedure with the destruction size of $d=12$.
Each method used for generating neighboring food sources may have different performances during the evolution process. Therefore, each food source (individual) in the population is assigned to one of the six strategies to generate a neighboring food source. After generating a neighboring food source, a local search is applied to further improve the solution quality (nectar amount) with a small probability of $p_{L S}=0.01$. As for the selection, a new source will always be accepted if it is better than the current food source, which is similar to the basic ABC algorithm carrying out a greedy selection procedure.

The motivation for assigning one of the six strategies to each individual in the population is derived from the efficacy of the DABC algorithm, which works like a multi-populated algorithm using a different strategy in each sub-population. By employing these strategies, the DABC algorithm implicitly takes advantage of the IG_RS algorithm of [33] and the ILS algorithm of [6]. The destruction size $(d)$ parameter needs to be carefully chosen for the IG_RS algorithm, whereas the

perturbation strength $(p)$ should be determined with care for the ILS algorithm. The perturbation can be achieved by removing a job from a position and inserting it into another position randomly, or by swapping of any two jobs randomly. In the original IG_RS algorithm of [33], detailed experiments have shown that a destruction size of 4 is suggested for the makespan criterion. However, our experiments show that taking a larger destruction size, especially $d=8$, is more effective than smaller sizes for the total flowtime criterion. In addition, taking a larger destruction size of $d=12$ also contributes to the diversification of the population. Regarding the perturbation strength of the ILS algorithm, perturbation values ( $p$ 's) ranging from 1 to 20 were tested, and $p$ values between 4 and 7 were suggested in [6]. However, in our experiments, $p$ values that were within the range of 1 to 2 swap or insert moves generated better results. The number of the employed bees is set to the population size $N P$, and the local search procedure will be explained in detail in Section 4.

# 2.3. Onlooker bee phase 

In the basic ABC algorithm, an onlooker bee selects a food source $\pi_{k}$ depending on its winning probability value, which is similar to roulette wheel selection in GAs [15-19]. However, the tournament selection is widely used in GA applications due to its simplicity and ability to escape from local optima. For this reason, we propose a tournament selection with a size of 2 in the DABC algorithm. In the tournament selection, an onlooker bee selects a food source $\pi_{k}$ in such a way that two food sources are randomly picked up from the population and compared to each other, allowing the better one to be chosen. In addition, an onlooker bee utilizes the same strategy that is used by the employed bee to produce a new neighboring solution. Then, a well-devised local search is employed to further improve the nectar amount of the onlooker bee. If the new food source obtained is better than the current one, the new food source will replace the current one and become a new member in the population. The onlooker bee phase in the DABC algorithm provides the intensification of a local search on the relatively promising solutions chosen with a tournament selection. The aim is to further improve the quality of solutions in the population. This is achieved by applying the assigned strategy to a food source $\pi_{k}$ that is then improved by an effective local search. The number of onlooker bees considered is $2 \times N P$. The local search procedure will be explained in detail in Section 4.

### 2.4. Scout bee phase

In the basic ABC algorithm, a scout bee produces a food source randomly in the predefined search space. This will decrease the search efficacy because the best food source in the population often carries better information than others during the evolution process, and the search space around it could be the most promising region. Therefore, in the DABC algorithm, a tournament selection with the size of 2 is again used to discard the worse of two randomly selected food sources that have been picked out from the population. Then, the scout generates a food source by performing a destruction and construction procedure with a destruction size of $d=4$ on the best solution in the current population. This destructed and constructed solution will be replaced by the food source determined by tournament selection. Therefore, poor solutions in the population will be replaced by the best solution of the perturbations in the current population. There are $0.2 \times N P$ scout bees in this phase.

## 3. Discrete differential evolution algorithm

Differential evolution (DE) is one of the latest evolutionary optimization methods proposed by Storn and Price in [34]. DE is originally a continuous algorithm where individuals are represented by chromosomes based on floating-point numbers. A DE algorithm mutates individuals in such a way that the weighted difference between two randomly selected population members is added to a third member to generate a mutated solution. Then, a trial solution is generated in such a way that the mutated solution is recombined with the target solution. Thereafter, a selection operator is applied to compare the fitness function values of both competing solutions (namely, the target and trial solutions) to determine who can survive for the next generation.

Because of its continuous nature, the DE algorithm cannot tackle discrete/combinatorial optimization problems. To overcome this limitation, Pan et al. [30] and Tasgetiren et al. [39] proposed a simple and novel discrete DE (DDE) algorithm whose solutions are based on discrete job permutations. In the DDE algorithm, the target individual is represented by a permutation of jobs $\pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right\}$. The mutant individual is obtained by perturbing each individual in the target population that is different from the one presented in [30,39]. To obtain the mutant individual, the following equation can be used:

$$
v_{i}^{\prime}= \begin{cases}\operatorname{insert}\left(\pi_{i}^{\prime-1}\right) & \text { if } r<P_{m} \\ \operatorname{swap}\left(\pi_{i}^{\prime-1}\right) & \text { otherwise }\end{cases}
$$

where $\pi_{i}^{\prime-1}$ is the individual in the target population, $P_{m}$ is the perturbation probability, insert is the simple random insertion move, and swap is the simple random interchange of two randomly chosen jobs. A uniform random number $r$ between 0 and 1 is generated. If $r$ is less than $P_{m}$, then the perturbation operator is applied to generate the mutant individual as $v_{i}^{\prime}=\operatorname{insert}\left(\pi_{i}^{\prime-1}\right)$; otherwise, the individual is perturbed by the swap operator as $v_{i}^{\prime}=\operatorname{swap}\left(\pi_{i}^{\prime-1}\right)$. Following the perturbation phase, the trial individual is obtained such that

$$
u_{i}^{t}= \begin{cases}C R\left(v_{i}^{t}, \pi_{i}^{t-1}\right) & \text { if } r<P_{c} \\ v_{i}^{t} & \text { otherwise }\end{cases}
$$

where $C R$ is any type of crossover operator and $P_{c}$ is the crossover probability. In other words, if a uniform random number $r$ is less than the crossover probability $P_{c}$, then the crossover operator is applied to generate the trial individual $u_{i}^{t}=C R\left(v_{i}^{t}, \pi_{i}^{t-1}\right)$. Otherwise, the trial individual is chosen as $u_{i}^{t}=v_{i}^{t}$. By doing so, the trial individual is made from the outcome of the perturbation operator or from the crossover operator. Finally, the selection is based on "survival of the fitter" among the trial and target individuals such that

$$
\pi_{i}^{t}= \begin{cases}u_{i}^{t} & \text { if } f\left(u_{i}^{t}\right)<f\left(\pi_{i}^{t-1}\right) \\ \pi_{i}^{t-1} & \text { otherwise }\end{cases}
$$

# 4. Hybridization with local search 

In order to intensify the search on the local minima and improve the solution quality, both DABC and hDDE are hybridized with some local search methods. For this reason, a well-devised local search algorithm denoted as LocalSearch() is fused into the DABC and hDDE algorithms. The proposed LocalSearch() procedure is based on a systematic application of both insert and swap moves. Because we employ six different strategies in both the employed bee and onlooker bee phases, the DABC algorithm takes advantage of both the IG_RS and ILS algorithms. In other words, some individuals work like an ILS with different perturbation strengths while others imitate an IG_RS with different destruction sizes. For the PFSP with the TFT criterion, we employed the following very effective local search in Fig. 1 embedded in the DABC and hDDE algorithms:

The key procedure of the IG_RS algorithm [33] is the destruction and construction procedure, which is given in Fig. 2. In the destruction step, a given number $d$ of jobs, randomly chosen and without repetition, are removed from the solution,

$$
\begin{aligned}
& \text { procedure } L S(\pi) \\
& \text { flag }=\text { false } \\
& \pi_{0}=\pi \\
& \text { do } \\
& \pi_{1}=\text { InsertLS }\left(\pi_{0}\right) \\
& \pi_{2}=\text { SwapLS }\left(\pi_{1}\right) \\
& \text { if } \quad\left(f\left(\pi_{2}\right)<f\left(\pi_{0}\right)\right) \\
& \text { flag }=\text { true } \\
& \pi_{0}=\pi_{2} \\
& \text { else } \\
& \text { flag }=\text { false } \\
& \text { while }(\text { flag }==\text { true }) \\
& \pi=\pi_{0} \\
& \text { return } \pi \\
& \text { endprocedure }
\end{aligned}
$$

Fig. 1. Local search algorithm.

$$
\begin{aligned}
& \text { procedure DestructConstruct }(\pi, d) \\
& \pi^{D}=\pi^{R}=\text { Destruct }_{d}(\pi) \\
& \pi=\text { Construct }\left(\pi^{D}, \pi^{R}\right) \\
& \text { return } \pi \\
& \text { endprocedure }
\end{aligned}
$$

Fig. 2. Destruction and construction procedure.

$$
\begin{aligned}
& \text { procedure } \quad \text { SwapLS }(\pi) \\
& \pi_{0}=\pi \\
& i=1 \\
& \text { do } \\
& j=i+1 \\
& \text { do } \\
& \pi_{1}=\pi_{0} \\
& \operatorname{swap}\left(\pi_{1}, i, j\right) \\
& \text { if } \quad\left(f\left(\pi_{1}\right)<f\left(\pi_{0}\right)\right) \\
& \pi_{0}=\pi_{1} \\
& i=1 \\
& j=i+1 \\
& \text { else } \\
& j=j+1 \\
& \text { endif } \\
& \text { while }(j<n) \\
& i=i+1 \\
& \text { while }(i<n) \\
& \pi=\pi_{0} \\
& \text { endprocedure }
\end{aligned}
$$

Fig. 3. Swap local search procedure.

$$
\begin{aligned}
& \text { procedure } \operatorname{InsertLS}(\pi) \\
& \pi_{0}=\pi \\
& i=1 \\
& \text { do } \\
& j=i+1 \\
& \text { do } \\
& \pi_{1}=\pi_{0} \\
& \operatorname{insert}\left(\pi_{1}, i, j\right) \\
& \text { if } \quad\left(f\left(\pi_{1}\right)<f\left(\pi_{0}\right)\right) \\
& \pi_{0}=\pi_{1} \\
& i=1 \\
& j=i+1 \\
& \text { else } \\
& j=j+1 \\
& \text { endif } \\
& \text { while }(j<n) \\
& i=i+1 \\
& \text { while }(i<n) \\
& \pi=\pi_{0} \\
& \text { return } \pi \\
& \text { endprocedure }
\end{aligned}
$$

Fig. 4. Insert local search procedure.

$$
\begin{aligned}
& \text { procedure } \operatorname{InsertFPR}(\pi) \\
& \pi_{0}=\pi \\
& k=1 \\
& t=0 \\
& \text { while }(t<n) \\
& \quad k=(k+1) \% n \\
& \pi_{1}=\text { remove job } \pi_{k} \text { from } \pi_{0} \\
& \pi_{2}=\text { best permutation obtained by inserting } \pi_{k} \text { in all possible positions of } \pi_{1} \\
& \text { if } \quad\left(f\left(\pi_{2}\right)<f\left(\pi_{0}\right)\right) \\
& \pi_{0}=\pi_{2} \\
& t=0 \\
& \text { else } \\
& t=t+1 \\
& \text { endif } \\
& \text { endwhile } \\
& \pi=\pi_{0} \\
& \text { return } \pi \\
& \text { endprocedure }
\end{aligned}
$$

Fig. 5. Insert local search procedure with first pivoting rule.
therefore resulting in two partial solutions. The first one $d$ jobs is denoted as $\pi^{R}$ and includes the removed jobs in the order in which they are removed. The second one $n-d$ jobs is the original solution without the removed jobs, which is denoted by $\pi^{D}$. Then, in the construction phase, a constructive heuristic procedure is needed. For this purpose, we employ the NEH insertion heuristic from [28]. In order to reinsert jobs from $\pi^{R}$ into the destructed solution $\pi^{D}$, the first job, $\pi_{1}^{R}$, is inserted into all possible $n-d$ positions in the destructed solution $\pi^{D}$, generating $n-d$ partial solutions. Among these $n-d$ partial solutions (including job $\pi_{1}^{R}$ ), the best partial solution with the minimum total flowtime is chosen and kept for the next iteration. Then, the second job, $\pi_{2}^{R}$, is considered. This is repeated until $\pi^{R}$ is empty or a final solution is obtained. Hence, $\pi^{D}$ is again of size $n$. For details regarding the DestructConstruct() procedure, we refer to Ruiz and Stutzle [33], where the procedure is well-illustrated with an example for the makespan criterion. It should be noted that the DestructConstruct() procedure is used by both algorithms in different ways. In the hDDE algorithm, the DestructConstruct() procedure is first applied to the best solution $\left(\pi_{R}\right)$ in the population with a destruction size of $d=8$. Then, the LocalSearch() procedure, the IG_RS algorithm with a larger destruction size, is used. On the other hand, in the DABC algorithm, the DestructConstruct() procedure is embedded in the strategy set. After applying the assigned strategy to each solution in the population, the LocalSearch() procedure is applied with a small probability $p_{L S}=0.01$ in the employed bee phase and applied to a solution $\pi_{k}$ determined by the tournament selection in the onlooker bee phase.

Similar to those in Jarboui et al. [13], two neighborhood structures, namely InsertLS() and SwapLS(), are considered as our local search procedures. InsertLS() evaluates all possible insert moves of pairs of job position (i,j) as shown in Fig. 3, whereas SwapLS() considers all possible interchange of pairs of job positions (i,j) as shown in Fig. 4. Note that in local search procedures, swap and insert moves are systematically carried out in such a way that if any improvement is made, the search starts from scratch on the improved solution again.

Furthermore, we also employed an insertion procedure denoted as InsertFPR(). In the InsertFPR() procedure, a job is removed from a permutation and inserted into $n-1$ positions; then, the permutation with the best out of the $n-1$ insertions is retained for the next iteration. The same procedure is repeated in a greedy manner for the $n$ number of jobs. The pseudocode of the InsertFPR() procedure is given in Fig. 5.

To further clarify, the DestructConstruct() and LocalSearch() procedures are sequentially applied to the best solution in the target population at each generation in the hDDE algorithm. On the other hand, the SwapLS() and InsertFPR() procedures are sequentially applied to each trial individual generated by the hDDE algorithm with a small probability of $p_{L S}=0.01$. Finally, the pseudocode of the hDDE algorithm is given in Fig. 6.

As for the DABC algorithm, the following computational procedure is used, as also depicted in Fig. 7.

1. Set the parameters, $N P, S_{\max }, p_{L S}$, and $S_{i}$ for each food source.
2. Initialize the population:

a. The first individual is generated by NEH whereas others are randomly established, i.e., $\pi_{1}=N E H\left(\pi_{1}\right)$ and $\pi=\left\{\pi_{2}, \pi_{3}, \ldots, \pi_{N P}\right\}$ and evaluate each solution in the population.
3. Employed bee phase:
a. For $i=1,2, \ldots, N P$, repeat the following sub-steps:
i. Produce a new food source $u_{i}$ for the $i$ th employed bee that is associated with the strategy $S_{i}$ and evaluate the new solution.
ii. If $r<p_{L S}$, perform the InsertFPR( ) and SwapLS( ) procedures on $u_{i}$, sequentially.
iii. If $u_{i}$ is better than $\pi_{i}$, let $\pi_{i}=u_{i}$ and update $\pi_{B}$, the best solution so far.
4. Onlooker bee phase:
a. For $i=1,2, \ldots, 2 \times N P$, repeat the following sub-steps:
i. Select a food source $\pi_{k}$ in the population for the onlooker bee by using the tournament selection (better TFT is chosen).
procedure hDDE
$\pi_{1}=N E H\left(\pi_{1}\right)$
$\pi=\left[\pi_{2}, \pi_{3}, \ldots, \pi_{N P}\right]$
$\pi_{B}=\arg \min _{i=1,2, \ldots, N P}\left(\pi_{i}\right)$
do

$$
\begin{aligned}
& v_{i}=\left\{\begin{array}{l}
\text { insert }\left(\pi_{i}\right) \text { if } r<P_{m} \\
\text { swap }\left(\pi_{i}\right) \text { else } \\
i=1,2, \ldots, N P
\end{array}\right. \\
& u_{i}=C R\left(v_{i}, \pi_{i}\right) \\
& \text { if } \quad\left(r<P_{L S}\right) \\
& u_{i}=\operatorname{Insert}_{\substack{i=1,2, \ldots, N P \\
i=1,2, \ldots, N P}} \\
& u_{i}=\operatorname{SwapLS}\left(u_{i}\right) \\
& \text { if } \quad\left(f\left(u_{i}\right)<f\left(\pi_{i}\right)\right) \\
& \pi_{i}=i \\
& \text { i=1,2,..,Np } \\
& \text { if } \quad\left(f\left(u_{i}\right)<f\left(\pi_{B}\right)\right) \\
& \pi_{B}=u_{i} \\
& \text { endif } \\
& \text { endif } \\
& \text { elseif } \\
& \left(\begin{array}{c}
f\left(u_{i}\right)<f\left(\pi_{i}\right) \\
i=1,2, \ldots, N P
\end{array}\right) \\
& \pi_{i}=u_{i} \\
& \text { endif } \\
& \pi_{B}=\text { DestructConstruct }\left(\pi_{B}, d\right) \\
& \pi_{B}=\text { LocalSearch }\left(\pi_{B}\right) \\
& \text { while(NotTer mination) } \\
& \text { return } \pi_{B} \\
& \text { endprocedure }
\end{aligned}
$$

Fig. 6. hDDE Algorithm.

procedure $D A B C$
$\pi_{1}=N E H\left(\pi_{1}\right)$
$\pi=\left[\pi_{2}, \pi_{3}, . ., \pi_{N P}\right]$
$S_{i}=\operatorname{rand}() \% S_{\max }$
$\pi_{B}=\underset{i=1,2, \ldots, N P}{\arg \min }\left(\pi_{i}\right)$
do
// Employed Bee Phase

$$
\begin{aligned}
& u_{i}=\pi_{i} \\
& \text { i=1,2,..,NP } \\
& u_{i}=S_{i}\left(u_{i}\right) \\
& \text { if } \quad\left(r<p_{L S}\right) \\
& u_{i}=\operatorname{Insert} F P R\left(u_{i}\right) \\
& \text { i=1,2,..,NP } \\
& u_{i}=\operatorname{SwapLS}\left(u_{i}\right) \\
& \text { i=1,2,..,NP } \\
& \text { if } \quad\left(f\left(u_{i}\right)<f\left(\pi_{i}\right)\right) \\
& \pi_{i}=u_{i} \\
& \text { i=1,2,..,NP } \\
& \text { if } \quad\left(f\left(u_{i}\right)<f\left(\pi_{B}\right)\right) \\
& \pi_{B}=u_{i} \\
& \text { i=1,2,..,NP } \\
& \text { endif } \\
& \text { endif } \\
& \text { i! Onlooker Bee Phase } \\
& \pi_{k}=\text { TournamentSelect }\left(\pi_{k} \in N P\right) \\
& u_{k}=S_{k}\left(\pi_{k}\right) \\
& u_{k}=\text { LocalSearch }\left(u_{k}\right) \\
& \text { if } \quad\left(f\left(u_{k}\right)<f\left(\pi_{k}\right)\right) \\
& \pi_{k}=u_{k} \\
& \text { i=1,2,..,2PNP } \\
& \text { if } \quad\left(f\left(u_{k}\right)<f\left(\pi_{B}\right)\right) \\
& \pi_{B}=u_{k} \\
& \text { i=1,2,..,2*NP } \\
& \text { else } \\
& S_{i}=\operatorname{rand}() \% S_{\max }
\end{aligned}
$$

endif
// Scout Bee Phase
$\pi_{k}=$ TournamentSelect $\left(\pi_{k} \in N P\right)$
$u_{k}=$ DestructionConstruction $\left(\pi_{B}, d\right)$
$\pi_{k}=u_{k}$
while(NotTer mination)
return $\pi_{B}$
endprocedure
Fig. 7. DABC Algorithm.

Table 1
Comparison of DABC and hDDE to IG_RS: $T_{\max }=0.4 \times n \times m \mathrm{~s}$.
Table 1 (continued)
Table 2
Two-sided paired $t$-test.
ii. Generate a new solution $u_{k}$ for the onlooker bee by using the strategy $S_{k}$ and apply the LocalSearch() procedure. If $u_{k}$ is better than $\pi_{k}$, let $\pi_{k}=u_{k}$ and update $\pi_{B}$, the best solution found so far.litemiii. If the generated solution $u_{k}$ is not better than the selected $\pi_{k}$, randomly switch to another strategy by re-obtaining $S_{k}=\operatorname{rand}() S S_{\max }$.

# 5. Scout phase: 

a. A tournament selection with a size of 2 is again used to discard the worse of the two randomly selected food sources from the population. Then, the scout generates a food source by performing a DestructConstruct() procedure with a destruction size of $d=4$ to $\pi_{B}$, the best solution in the current population. The obtained solution is replaced with the food source determined by the tournament selection.
6. Memorize the best solution achieved so far.
7. If the termination criterion is reached, return the best solution found so far; otherwise go to Step 3.

## 5. Computational results

The DABC and hDDE algorithms were coded in Visual C++ and run on an Intel Pentium IV 3.0 GHz PC with 512 MB memory. They were applied to the 90 benchmark instances of Taillard in [35] ranging from 20 jobs with 5 machines to 100 jobs with 20 machines. All of the parameters in this study were determined experimentally. Regarding the parameters of the hDDE algorithm, a small population size of $N P=10$ is employed. The destruction and construction procedure with a destruction size of $d=8$ was used in the hDDE algorithm. The crossover and mutation probabilities were taken as 0.9 and 0.5 , respectively. The probability that a local search applied to each trial individual was taken as $p_{t S}=0.01$, and the PTL crossover operator in [30,36-39] was employed. To be fair, especially with Jarboui et al. [13], the same termination criterion is used as $T_{\max }=0.4 \times n \times m$ s for the short-term search, whereas it is fixed at $T_{\max }=3 \times n \times m$ s for the long-term search. Note that a similar machine speed is also used so that the comparisons will be fair enough especially with the EDA algorithm. As for the

Table 3
Comparison to the best performing algorithms: $T_{\max }=0.4 \times n \times m \mathrm{x}$.
Table 3 (continued)
Table 4
Two-sided paired $t$-test for the best performing algorithms.

parameters of the DABC algorithm, the population size was also fixed at $N P=10$. The sizes of employed bees, onlooker bees, and scout bees were $N P=10,2 \times N P$ and $0.2 \times N P$, respectively. Strategies were determined as explained in Section $2 . R=10$ runs were carried out for each problem instance. The minimum (Min), average (Avg), maximum (Max), and standard deviation (Std) of 10 replications are reported and compared to those yielded by the best performing algorithms from the literature.

As both DABC and hDDE algorithms extensively make use of the IG_RS algorithm from [33] in different manners in terms of its parameters, we also coded the traditional IG_RS algorithm with the destruction size of $d=4$. In addition, we employed

Table 5
Computational time of algorithms compared.
Table 6
New best known solutions with CPU time limit of $T_{\max }=3 \times n \times m \mathrm{~s}$.

Table 6 (continued)
the same local search based only on the insertion neighborhood structure as in Ruiz and Stutzle [33]. For the short-term search of $T_{\text {max }}=0.4 \times n \times m \mathrm{~s}$, the computational results are given in Table 1.

As seen in Table 1, the hDDE and DABC algorithms generated significantly better results than the IG_RS algorithm. In particular, for the first 30 instances belonging to $20 \times 5,20 \times 10$, and $20 \times 20$ classes, the DABC and hDDE algorithms were able to find the best-known solutions for each of the 10 replications. In other words, their standard deviations were all zero, whereas IG_RS did not necessarily succeed in finding the best known solutions. In terms of all statistics, DABC and hDDE are superior to IG_RS. However, this conclusion should be tested statistically. For this reason, we carried out a two-sided paired $t$-test for the algorithms compared, with the results shown in Table 2.

Table 2 confirms that hDDE and DABC algorithms are significantly better than IG_RS in every statistic because the $p$ - values were all zero at the $\alpha=0.05$ level. When hDDE and DABC are compared, DABC generated significantly better results than hDDE in terms of Min values because the $p$-value was 0.024 . However, the $t$-test indicates that the DABC and hDDE algorithms were equivalent in terms of Max and Avg values because the $p$-values were higher than the $\alpha=0.05$ level. As for the Std values, the $t$-test indicates that DABC was more robust than hDDE because the $p$-value was equal to 0.004 at the $\alpha=0.05$ level. From this analysis, it can be concluded that the DABC and hDDE algorithms were statistically superior to the IG_RS algorithm.

Table 3 compares the best performing algorithms from prior literature in terms of Min and Avg values because the hGLS and tsGLS algorithms only reported these statistics (EDA reported only Min results).

From Table 3, DABC and hDDE algorithms are clearly shown to be superior to the hGLS and tsGLS algorithms in terms of the quality of the best solutions, i.e., Min results. However, the DABC performance was equivalent to EDA. Again, in terms of Avg results, DABC generated better results than the hGLS and tsGLS algorithms. However, hDDE was very competitive with DABC in the case of Avg values. These conclusions should be tested statistically, too. For this reason, we again carried out a two-sided paired $t$-test for the competing algorithms. The $t$-test results are given in Table 4.

From the $t$-tests in Table 4, it can be concluded that EDA and DABC were statistically equivalent algorithms in terms of Min values because the $p$-value was 0.277 at the $\alpha=0.05$ level. Note that Avg values were not provided for the EDA in [13]. Furthermore, DABC was able to generate statistically better results than tsGLS, hGLS, and hDDE because all of the $p$-values were less than the $\alpha=0.05$ level. In terms of the Avg values, DABC was again statistically superior to both tsGLS and hGLS; however, it was equivalent to hDDE. From the analysis above, it can be concluded that the currently best performing algorithms for PFSP with TFT criterion in the existing literature are the DABC, hDDE, and EDA algorithms. Ultimately, with the short-term search results given in Table 3, 44 out of the 90 best known solutions are further improved by the DABC and hDDE algorithms. These results indicate that the performances of the DABC and hDDE algorithms in terms of obtaining the best-known solutions are quite remarkable.

Table 5 summarizes the computational times of the algorithms compared. From Table 5, the DABC algorithm was the most computationally expensive one. On the other hand, hDDE was very competitive with EDA and VNS from Jarboui et al. [13]. The least expensive one was hGLS from Tseng and Lin [24]. However, the hDDE and DABC algorithms yielded supe-

rior solutions at the expense of only minimally longer CPU times. Furthermore, the long-term search results justify the competitive performance of our algorithms when compared to the best performing EDA, hGLS, and tsGLS algorithms in the existing literature.

The computational results for the long-term search of $T_{\max }=3 \times n \times m \mathrm{~s}$ are given in Table 6 , where the results for hGLS, tsGLS, and EDA were taken from [13], [24], and [25], respectively. The new best-known solutions are reported for almost 60 out of 90 problem instances in Table 5. It should be stated that in Tseng and Lin [24], extremely long runs are carried out for $50 \times 5,50 \times 10$, and $50 \times 20$ instances, and the current best-known solutions are further improved at the expense of extremely increased CPU times. For $50 \times 5$ and $50 \times 10$ instances, Tseng and Lin's runs took 30 min and 75 min per run, respectively. However, our algorithms took only $3 \times 50 \times 5=750 \mathrm{~s}(12.5 \mathrm{~min})$ and $3 \times 50 \times 10=1500 \mathrm{~s}(25 \mathrm{~min})$ per run for the $50 \times 5$ and $50 \times 10$ problems, respectively. Furthermore, it is again interesting to note that in 10 out of 30 problems (i.e., $50 \times 5,50 \times 10$, and $50 \times 20$ problems), our results with the short-term search are even better than the long-term search of Tseng and Lin [24], [25]. When considering the long-term searches, the DABC and hDDE algorithms have further improved 18 out of the 30 best-known solutions of Tseng and Lin [24].

# 6. Conclusions 

In this paper, we considered the applications of the DABC and hDDE algorithms to the PFSP under the TFT criterion. The DABC algorithm is hybridized with a variant of iterated greedy algorithms employing a local search procedure based on insertion and swap neighborhood structures. In addition, we also presented a hybrid version of our previous discrete differential evolution algorithm employing the same local search procedure. To the best of our knowledge, our proposal is the first application of DABC to the PFSP with the TFT criterion. The performances of the proposed algorithms were tested by using Taillard's benchmark suite that is commonly used in the scheduling literature. The proposed algorithms were superior to the traditional IG_RS algorithm, and it has been shown that the performances of the DABC and hDDE algorithms are highly competitive with (if not better than) the best performing estimation distribution and genetic local search algorithms that have appeared recently in the existing literature. Ultimately, 44 out of the 90 best-known solutions provided recently by the EDA, tsGLS, and hGLS algorithms are further improved by the DABC and hDDE algorithms with short-term searches. With longterm searches, the new best-known solutions are reported for all problems in the benchmark suite of Taillard. For future research, DABC will be extended to solve other scheduling problems such as no-wait flowshop, no-idle flowshop, blocking flowshop, etc. in the existing literature.
