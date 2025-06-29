# An improved NSGA-II algorithm for multi-objective lot-streaming flow shop scheduling problem 

Yu-Yan Han ${ }^{\mathrm{a}}$, Dun-wei Gong ${ }^{\mathrm{a} *}$, Xiao-Yan Sun ${ }^{\mathrm{a}}$ and Quan-Ke Pan ${ }^{\mathrm{b}}$<br>${ }^{a}$ School of Information and Electrical Engineering, China University of Mining and Technology, Xuzhou, China; ${ }^{\mathrm{b}}$ School of<br>Computer Science, Liaocheng University, Liaocheng, China

(Received 7 May 2013; accepted 19 September 2013)


#### Abstract

Crossover and mutation operators in NSGA-II are random and aimless, and encounter difficulties in generating offspring with high quality. Aiming to overcoming these drawbacks, we proposed an improved NSGA-II algorithm (INSGA-II) and applied it to solve the lot-streaming flow shop scheduling problem with four criteria. We first presented four variants of NEH heuristic to generate the initial population, and then incorporated the estimation of distribution algorithm and a mutation operator based on insertion and swap into NSGA-II to replace traditional crossover and mutation operators. Last but not least, we performed a simple and efficient restarting strategy on the population when the diversity of the population is smaller than a given threshold. We conducted a serial of experiments, and the experimental results demonstrate that the proposed algorithm outperforms the comparative algorithms.


Keywords: NSGA-II; lot-streaming flow shop; multi-objective optimisation; heuristic rule; estimation of distribution algorithm; restarting strategy

## 1. Introduction

The lot-streaming flow shop (LSFS) scheduling problem, one representative branch of traditional flow shop schedule problems, is a simplified model of various real schedule problems, such as manufacturing systems, assembly lines, information service facilities, as well as chemical, textile, plastics and semiconductor industries (Pan, Pan, and Sang 2010). The main goal of the LSFS scheduling problem is to determine either the best allocation of sub-lots or the size of each sub-lot so as to minimise some given performance measures. Thus, developing effective and efficient methods to solve the above problems is of significance in theory and applications (Pan and Ruiz 2012). Different from traditional flow shops, LSFS splits a given job into several sub-lots, and each is transferred to the downstream machine after it is completed in the current one, thereby reducing the production cycle and waiting time, accelerating the manufacturing process and enhancing the production efficiency.

In the development of solving LSFS scheduling problem with single objective, efforts of some significant research of meta-heuristics have been made, such as genetic algorithm (GA), harmony search (HS), artificial bee colony (n) and estimation of distribution algorithm (EDA). Defersha and Chen (2012) proposed a method for solving the flexible LSFS scheduling problem with several jobs in multi-stage consisting of unrelated parallel machines. In this work, the authors constructed a mathematical model using integer programming and designed a parallel GA to solve the above model. The experimental results showed that the parallel implementation extremely improved the computational performance. Kim and Jeong (2009) presented an adaptive GA for the flexible LSFS scheduling with no-wait. In this study, the authors adopted four methods, that is, position-based crossover, local search-based mutation, iterative hill-climbing and adaptive regulation of GA parameters to improve the algorithm's performance, and the experimental results showed the proposed algorithm outperformed other GAs. Pan et al. (2010) designed a novel discrete HS algorithm for scheduling LSFS to minimise the makespan objective. To improve the algorithm's exploitation ability, the authors applied a local search into discrete HS algorithm, and the effectiveness and efficiency of the proposed algorithm were demonstrated by comparing with the existing composite ones, GA, ant colony optimisation (ACO) and the threshold accepting (TA) algorithm. Karaboga (2005) firstly proposed the ABC algorithm for continuous function optimisation. Given the above algorithm is of simple structure, strong convergence, more and more researchers have applied it to solve the flow shop scheduling problem. Lei and Guo (2013) adopted a modified ABC algorithm to solving the job shop with LSFS

[^0]
[^0]:    *Corresponding author. Email: dwgong@vip.163.com

scheduling problem. In this work, employed and onlooker bees adopted the swap and insertion operators to produce new solutions, and the proposed algorithm adopted the elite solution to replace with the worst ones without considering the scouts. Recently, Pan and Ruiz (2012) developed an EDA for the LSFS problem with sequence-dependent set-up time. The experimental results showed that the proposed EDA was more effective than discrete ABC algorithm (Pan et al. 2011), ACO (Marimuthu, Ponnambalam, and Jawahar 2009), discrete particle swarm optimisation (Tseng and Liao 2008) and hybrid GA (Yoon and Ventura 2002).

However, production managers concern not only the scheduling problem with only one objective, but also the one with several objectives, such as makespan, tardiness time, earliness time, the total flow time and idle time of machines in various real-world applications. LSFS with single objective is insufficient; thus, multi-objective LSFS plays a key role in practical scheduling problems (Zhang et al. 2010). The well-known NSGA-II algorithm, firstly presented by Deb (2000), is one of effective evolutionary algorithms for multi-objective optimisation problems whose three main operators are fast non-dominated sorting, fast crowded distance estimation and simple crowded-based comparison Deb et al. (2002). In the light of its simplicity, good convergence and diversity, NSGA-II has caused much attention and a wide range of successful applications, such as customer churn prediction in telecommunications (Huang, Buckley, and Kechadi 2010), expansion planning (Murugan, Kannan, and Baskar 2009), economic and emission dispatch (Dhanalakshmi et al. 2011), estimation of prediction intervals of scale deposition rate in oil and gas equipments (Ronay et al. 2013), shape optimisation of axisymmetric cavitators in supercavitating flows (Shafaghat et al. 2011) and flow shop scheduling problems (Tseng and Liao 2008). The existing NSGA-II for solving the flow shop scheduling problems is commonly improved through modifying the non-dominated sorting or selection strategy. Zhang et al. (2010) designed an improved non-dominated sorting NSGA-II for the multi-objective flexible job shop scheduling problem, which is effective when both the rank and the crowed distance of the current two individuals are equal. Liu and Huang (2013) developed a new pre-selection method to obtain the minimal overall outsourcing cost and supply risk probability, which reduces the probability of design change at the stage of product production. However, the above algorithms did not consider the modification of the crossover and mutation operators, which guide the population towards the Pareto front, and thus decrease their effectiveness. In addition, to the best of our knowledge, there is few published work dealing with the multi-objective flow shop scheduling problem, especially the LSFS one, by using NSGA-II. So, it is considerably necessary to design an improved NSGA-II for the multi-objective LSFS problem.

EDA proposed by Muhlenbein and Paass (1996) has been widely studied by experts in evolutionary computation (Jarboui, Eddaly, and Siarry 2009). Because of its effectiveness, the EDA has been successfully applied to solve the permutation flow shop scheduling problem (Jarboui, Eddaly, and Siarry 2009; Zhang and Li 2011), the global continuous optimisation problem (Sun, Zhang, and Edward 2005), the nurse scheduling problem (Aickelin and Li 2007), LSFS problems (Pan and Ruiz 2012) and so on. The basic EDA mainly includes the following four steps (Larraaga and Lozano 2002). First, select PS promising solutions from the original population according to their fitness and then put them into a candidate population, $\left|\eta_{i j}\right|_{\text {PS }+n}$. Second, build a probability distribution model, $\left|\xi_{i j}\right|_{n \times n}$, based on the above population. Third, generate a new offspring, $\pi_{\text {new }}$, through learning and sampling from the constructed probabilistic model, and evaluate its fitness. Last, update the original population as follows: if $\pi_{\text {new }}$ is better than the worst one of the original population, denoted as $\pi_{w}$, then replace $\pi_{w}$ with $\pi_{\text {new }}$. In the multi-objective LSFS scheduling problem, EDA can take full advantage of valuable information of non-dominated solutions to construct a probabilistic model and then estimate the probability distribution of good chromosomes to generate promising offspring. So, we embedded EDA into NSGA-II instead of traditional crossover operator so as to lead the population towards the Pareto-optimal front.

Due to the LSFS problem has such characteristics as constraint conditions, dynamic nature, large scale, complex computation, studies on the LSFS problem with multiple objectives are relatively less than the one with single objective. Several objectives must be simultaneously considered in practical problems; therefore, it is necessary to design an algorithm for the LSFS scheduling problem with four objectives. Three main contributions of the proposed algorithm are drawn. First, the variants of NEH (Nawaz, Enscore, and Ham 1983) heuristics are adopted to construct four initial individuals with good performance Secondly, EDA is embedded in the NSGA-II algorithm to generate good offspring. Finally, the restart strategy is employed to avoid the proposed algorithm trapping in local optima.

The rest of this paper is organised as follows. After this brief introduction, in Section 2, the LSFS scheduling problem is stated. Section 3 describes the proposed algorithm. In Section 4, the evolutionary metrics are introduced, and the experimental results are provided in Section 5. Finally, the paper ends with some conclusions in Section 6.

# 2. LSFS scheduling problem 

The LSFS scheduling problem can be formulated as follows (Pan and Ruiz 2012). There are $n(\pi=$ $\{\pi(1), \pi(2), \ldots, \pi(n)\})$ jobs and $m$ machines. Each job $\pi(i) \in \pi$ is processed on each of $m$ machines in the same series.

Table 1. Illustration of notations.
Each job can be split into several sub-lots, and each sub-lot has different processing time on different machines. The constraints of the LSFS scheduling problem can be described below. (1) The job can be processed at the $j$ th machine only when all sub-lots of the forgoing job are completed at the machine; (2) At any time, each machine can process at most one sub-lot, and each sub-lot can be processed on at most one machine at the same time; (3) All sub-lots of the same job $\pi(i) \in \pi$ should be continuously processed. Any two adjacent sub-lots of job $j$ allow idle time at the same stage. Both the set-up time and the sub-lot transportation time are included in the processing time. In order to clearly describe the LSFS scheduling problem and well explain the mathematical model, Table 1 illustrates the meaning of all notations.

Figure 1 shows a Gantt comparison between traditional flow shop and LSFS with 2 jobs and 3 machines. Suppose that jobs 1 and 2 contain 3 and 2 sub-lots, respectively, and the processing time of each sub-lot is as follows.

$$
\left[P_{e, t}^{\prime}\right]_{3 \times 3}=\left[\begin{array}{lll}
p_{1,1}^{\prime} & p_{1,2}^{\prime} & p_{1,3}^{\prime} \\
p_{2,1}^{\prime} & p_{2,2}^{\prime} & p_{2,3}^{\prime} \\
p_{3,1}^{\prime} & p_{3,2}^{\prime} & p_{3,3}^{\prime}
\end{array}\right]=\left[\begin{array}{lll}
2 & 4 & 3 \\
2 & 4 & 3 \\
2 & 4 & 3
\end{array}\right] \quad\left[P_{e, t}^{\prime}\right]_{2 \times 3}=\left[\begin{array}{lll}
p_{1,1}^{\prime} & p_{1,2}^{\prime} & p_{1,3}^{\prime} \\
p_{2,1}^{\prime} & p_{2,2}^{\prime} & p_{2,3}^{\prime}
\end{array}\right]=\left[\begin{array}{lll}
1 & 5 & 2 \\
1 & 5 & 2
\end{array}\right]
$$

As shown in Figure 1, the process of traditional flow shop scheduling problem is illustrated by an instance with two jobs and three machines with their job processing time of $\{6,12,9\}$ and $\{2,10,4\}$, respectively. If none of these jobs is split into sub-lots, the completion time will be 32 . Whereas, when each of these jobs is split into some sub-lots of equal size, the completion time is reduced to 26 . Thus, in this example, lot-streaming can reduce the manufacturing time by about $19 \%$.

While evaluating the performance of the LSFS scheduling problem, a manager often considers the following four objectives, that is, the makespan, the total flow time, idle time of all machines and the earliness time. The makespan intuitively reflects the completion time produced by different schedulings under some constraints. The total flow time
![img-0.jpeg](img-0.jpeg)

Figure 1. Gantt comparison between traditional flow shop and LSFS.

![img-1.jpeg](img-1.jpeg)

Figure 2. Computation of makespan, idle time and total flow time.
embodies the strict requirement for the whole flow time of all jobs, whereas the earliness time expresses the user requirement for ahead of schedule. The idle time reflects whether the machines can take full advantage of resource or not.

Hence, in view of practical production, this study formulates the LSFS scheduling problem as an optimisation one with the above four objectives. These objectives can be calculated as follows, and a Gantt for calculating the makespan, the total flow time and idle time is illustrated in Figure 2.

Let a job permutation $\pi=\{\pi(1), \pi(2), \ldots, \pi(n)\}$ represent the sequence of jobs to be processed, and the start time of the first sub-lot of the first job on the first machine be equal to zero, that is, $S_{\pi(1), 1,1}=0$.

$$
\begin{aligned}
& \left\{\begin{array}{l}
S_{\pi(1), 1,1}=0 \\
C_{\pi(1), 1,1}=S_{\pi(1), 1,1}+p_{\pi(1), 1}
\end{array}\right. \\
& \left\{\begin{array}{l}
S_{\pi(1), t, 1}=C_{\pi(1), t-1,1} \\
C_{\pi(1), t, 1}=S_{\pi(1), t, 1}+p_{\pi(1), t}
\end{array}\right. \\
& t=2,3, \ldots, m \\
& \left\{\begin{array}{l}
S_{\pi(1), 1, e}=C_{\pi(1), 1, e-1} \\
C_{\pi(1), 1, e}=S_{\pi(1), 1, e}+p_{\pi(1), 1} \\
e=2,3, \ldots, l_{\pi(1)}
\end{array}\right. \\
& \left\{\begin{array}{l}
S_{\pi(1), t, e}=\max \left\{C_{\pi(1), t-1, e}, C_{\pi(1), t, e-1}\right\} \\
C_{\pi(1), t, e}=S_{\pi(1), t, e}+p_{\pi(1), t} \\
e=2,3, \ldots, l_{\pi(1)} ; t=2,3, \ldots, m
\end{array}\right. \\
& \left\{\begin{array}{l}
S_{\pi(i), 1,1}=C_{\pi(i-1), 1, l_{\pi(i-1)}} \\
C_{\pi(i), 1,1}=S_{\pi(i), 1,1}+p_{\pi(1), 1} \\
i=2,3, \ldots, n
\end{array}\right. \\
& \left\{\begin{array}{l}
S_{\pi(i), t, 1}=\max \left\{C_{\pi(i), t-1,1}, C_{\pi(i-1), t, l_{\pi(i-1)}}\right\} \\
C_{\pi(i), t, 1}=S_{\pi(i), t, 1}+p_{\pi(i), t} \\
i=2,3, \ldots, n ; t=2,3, \ldots, m
\end{array}\right. \\
& \left\{\begin{array}{l}
S_{\pi(i), 1, e}=C_{\pi(i), 1, e-1} \\
C_{\pi(i), 1, e}=S_{\pi(i), 1, e}+p_{\pi(i), 1} \\
i=2,3, \ldots, n ; e=2,3, \ldots, l_{\pi(i)}
\end{array}\right. \\
& \left\{\begin{array}{l}
S_{\pi(i), t, e}=\max \left\{C_{\pi(i), t-1, e}, C_{\pi(i), t, e-1}\right\} \\
C_{\pi(i), t, e}=S_{\pi(i), t, e}+p_{\pi(i), t} \\
i=2,3, \ldots, n ; e=2,3, \ldots, l_{\pi(i)} ; t=2,3, \ldots, m
\end{array}\right. \\
& \min f_{1}(\pi)=\min \left(C_{\max }(\pi)\right)=C_{\pi(n), m, l_{\pi(n)}} \\
& \min f_{2}(\pi)=\min \left(\operatorname{Idle}_{\max }(\pi)\right)=\sum_{i=1}^{m}\left(C_{\pi(n), t, l_{\pi(n)}}-\sum_{i=1}^{n} \sum_{l=1}^{l_{\pi(i)}} p_{\pi(i), t}\right)
\end{aligned}
$$

$$
\begin{gathered}
\min f_{3}(\pi)=\min \left(\mathrm{TFT}_{\max }(\pi)\right)=\mathrm{TFT} 1+\mathrm{TFT} 2=\sum_{i=1}^{n} C_{\pi(i), m, f_{\pi(i)}} \\
\min f_{4}(\pi)=\max \left(0, d_{i}-C_{\pi(i), m, f_{\pi(i)}}\right)
\end{gathered}
$$

![img-2.jpeg](img-2.jpeg)

Figure 3. Flowchart of the proposed algorithm.

# Procedure Initialization() 

Input:
Parameters: $k$ refers to the number of jobs in a subsequence. $\mathrm{f}_{\mathrm{i}}$ refers to the $j$ th objective, $\mathrm{j}=\{1,2,3,4\}$.
set: $\mathrm{k}=0, \pi^{*}=\Phi ; j=1 ; \mathrm{f}_{\mathrm{i}}\left(\pi^{*}\right)=\Phi$.
Output: initial population
Begin
Step 1. Computer the total time, $\mathrm{T}_{i}=\sum \mathrm{C}_{\pi(i), i<j, j, \pi} \mathrm{i}=\{1,2, \cdots, n\}$ on all machines for each job according to equations $1-8$, and obtain a sequence, $\pi=\{\pi(1), \pi(2), \cdots, \pi(n)\}$, by sorting jobs according to the total processing time in a descendant order.
Step 2. Take the first two jobs from $\pi$, evaluate the values of $f_{i}$ of two possible subsequences, and select the better as the current sequence $\pi^{*}$. Set $\mathrm{k}=2$.
Step 3. Set $k=k+1$, take the $k$ th job from $\pi$, and obtain $k$ subsequences by inserting it into $k$ possible positions of the current sequence $\pi^{*}$, then select the subsequence with the minimal $\mathrm{f}_{\mathrm{i}}\left(\pi^{*}\right)$ as the current sequence $\pi^{*}$.
Step 4. If $k<n$, go to Step 3; otherwise, let $\pi_{i}=\pi^{*}$, and go to Step 5.
Step 5. Set $j=j+1$. If $j<4$, go to Step 2 ; otherwise, obtain four sequences, $\pi_{1}, \pi_{2}, \pi_{3}, \pi_{4}$, and go to Step 6 .
Step 6. the rest different PS-4 individuals are randomly generated in the search space.
End
Figure 4. Pseudo code of the initializing population.

```
for \(i=1\) to \(P S\)
    if( \(\operatorname{rand}()<p c\) )
        Perform EDA to generate the offspring
    else
        Take out a parent individual and perform the mutation operation based on the insertion and
        swap operators
    end if
end for
```

Figure 5. Pseudo code of the generating offspring.

# 3. The proposed NSGA-II algorithm 

Although individuals comparison, non-dominated sorting and selection operator of the exiting NSGA-II algorithms for multi-objective flow shop problem have been modified and showed the superiority to generate a good offspring, two critical operators, that is, crossover and mutation, have not been further researched. Traditional crossover and mutation operators are of randomness and aimlessness and cannot guarantee to generate offspring with a high quality, which reduces the convergence rate and influences the algorithm's efficiency. Therefore, an improved NSGA-II algorithm imbedding EDA is adopted in this paper to enhance the diversity, speed up the convergence of the population and to seek for a Pareto-optimal set $U^{*}$ to minimise the above four objectives in the LSFS scheduling problem. The flowchart of the proposed algorithm is illustrated in Figure 3, and its detailed process is stated as follows.

### 3.1 Initialising population

Good seeds can generate candidates of the optimisation problem with high quality, which improves the efficiency of the whole algorithm. A rapid convergence can be obtained if a candidate makes one of the objectives minimal in an initial population for solving the multi-objective optimisation problem. Therefore, the above idea is employed in this study, that is, four variants of well-known NEH heuristics, called vNEH, are adopted to minimise makespan, the total flow time, the idle time of machines and the earliness time, respectively. It is worth noting that candidates in the proposed algorithm are represented as discrete job permutations. Let $P S$ be the population size. Four solutions, $\pi_{1}, \pi_{2}, \pi_{3}, \pi_{4}$, can be yielded by performing the proposed vNEH, and the rest $P S-4$ individuals in the search space are randomly generated. The details of vNEH are stated in Figure 4.

To simply illustrate the aforementioned steps, an example for generating good seeds is given here. Suppose that there are six jobs, denoted as $\pi(i)=i, i=\{1,2, \ldots, 6\}$, whose numbers of associated sub-lots are $\{6,5,6,3,6,6\}$, respectively. These jobs are processed on three machines, and their processing time is $\{12,8,9\},\{29,1,26\}$, $\{23,12,28\},\{14,31,24\},\{16,7,10\}$ and $\{6,29,4\}$, respectively.
(1) The total processing time of each job can be calculated as $\{169,318,353,238,216,364\}$ according to Equations (1)-(8); then, the sequence in the descendant order is $\pi=\{6,3,2,4,5,1\}$.
(2) The first two jobs in $\pi$, that is, 6 and 3 , are first taken; and their two possible permutations, that is, $\{3,6\}$ and $\{6,3\}$, are evaluated with the first objective, named makespan, as $f_{1}(\{3,6\})=328, f_{1}(\{6,3\})=360$. The subsequence with a smaller makespan is selected as the current sequence, $\pi^{*}$, and therefore, $\pi^{*}=\{3,6\}$.
(3) Let $k=3$, the third job in $\pi$, that is, 2 , is taken and three possible permutations, that is, $\{2,3,6\},\{3,2,6\}$ and $\{3,6,2\}$, are evaluated with objective $f_{1}$ as $f_{1}(\{2,3,6\})=473, f_{1}(\{3,2,6\})=467$ and $f_{1}(\{3,6,2\})=458$, and the best subsequence is chosen as the current one, $\pi^{*}$, and therefore, $\pi^{*}=\{3,6,2\}$.
(4) Similarly, the rest jobs are yielded as follows:

$$
\begin{aligned}
& k=4, \quad f_{1}(\{4,3,6,2\})=500, f_{1}(\{3,4,6,2\})=553, f_{1}(\{3,6,4,2\})=571, f_{1}(\{3,6,2,4\})=530 . \quad \pi^{*}= \\
& \{4,3,6,2\}
\end{aligned}
$$

$k=5, f_{1}(\{5,4,3,6,2\})=596, f_{1}(\{4,5,3,6,2\})=596, f_{1}(\{4,3,5,6,2\})=591, f_{1}(\{4,3,6,5,2\})=563$, $f_{1}(\{4,3,6,2,5\})=560, \pi^{*}=\{4,3,6,2,5\}$
$k=6, f_{1}(\{1,4,3,6,2,5\})=632, f_{1}(\{4,1,3,6,2,5\})=632, f_{1}(\{4,3,1,6,2,5\})=628, f_{1}(\{4,3,6,1,2,5\})=$ $618, f_{1}(\{4,3,6,2,1,5\})=614, f_{1}(\{4,3,6,2,5,1\})=614, \pi^{*}=\{4,3,6,2,1,5\}$;

Lastly, the complete sequence with the smallest makespan is obtained, and therefore, $\pi_{1}=$ $\pi^{*}=\{4,3,6,2,1,5\}$.

(5) Set $j=2,3,4$, respectively. The rest good seeds with the smallest total flow time, the idle time and the earliness time are generated, respectively, that is, $\pi_{2}=\{6,5,1,3,4,2\}, \pi_{3}=\{4,1,5,3,6,2\}$ and $\pi_{4}=\{4,1,5,2,3,6\}$.

# 3.2 Generate the offspring 

Crossover and mutation operators play an important role, whose contribution is that the offspring inherits from the excellent farther chromosomes. Due to the multi-objective optimisation problem has many non-dominated solutions with a high quality, taking full advantage of the valuable information of non-dominated solutions will lead the population towards the Pareto-optimal front. The merit of EDA lies in that it can utilise the information of non-dominated solutions to construct a probabilistic model and then estimate the probability distribution of good chromosomes to build M offspring. To this end, EDA is adopted to generate offspring instead of the traditional crossover operator in this paper.

In addition, Insertion, swap and inverse operators are commonly used to produce a promising neighbouring solution, which can enhance the exploitation of an algorithm by slightly disturbing the current solution. Given the insertion and swap operators are superior to the inverse one (Wang and Zheng 2003), the former two are considered as the mutation operators in this paper. The detailed process is illustrated in Section 3.2.2.

To sum up, in the light of the performance of EDA in exploration and that of the insertion and swap operators in exploitation, EDA with the probability of $p c$ and the insert and swap operators with $1-p c$ probability are employed to generate the offspring, with the purpose of leading the population towards the Pareto-optimal front during the evolution. The general framework of generating the offspring is given as follows (Figure 5).

### 3.2.1 EDA

The detailed description of EDA for LSFS scheduling problem is given as follows (Pan and Ruiz 2012):
Select $P S$ promising solutions to put into the candidate population $\left[\eta_{i, j}\right]_{P S \times n}$. All non-dominated solutions obtained at each iteration are considered as the candidate individuals. If the number of non-dominated solutions, $Q$, is equal to $P S$, then put all these non-dominated solutions into $\left[\eta_{i, j}\right]_{P S \times n}$; if $Q$ is less than $P S$, then the rest $P S-Q$ individuals are selected by using tournament selection with size 2 to conduct the candidate population as well as $Q$ non-dominated solutions.

Build a probabilistic model $\left[\zeta_{i, j}\right]_{n \times n}$ whose aim is to improve the algorithm's efficiency and effectiveness for optimising the LSFS scheduling problem (Pan and Ruiz 2012). The probabilistic model obtained by Han et al. (2012) is

```
Initialize \(\left[\rho_{i, j}\right]_{\text {non }}=0 ; \quad\left[\beta_{f, j}\right]_{\text {non }}=0\)
    for \(i=1\) to \(n\)
        for \(j=1\) to \(P S\)
            \(\rho[i][\eta[j][i]]=\rho[i][\eta[j][i]]+1 ;\)
        endfor
    endfor
    for \(j=1\) to \(P S\)
        for \(i=1\) to \(j o b-1\)
            if \(([\mid=\mathrm{i})\)
                \(\beta[\eta[j][i]][\eta[j][i+1]=\beta[\eta[j][i]][\eta[j][i+1]+1 ;\)
                endif
            endfor
endfor
```

Figure 6. Pseudo code of the generating elements of two matrixes.

adopted in this paper. According to information of the candidate population $\left[\eta_{i j}\right]_{P S \times n}$, two matrixes, named $\left[\rho_{i j}\right]_{n \times n}$ and $\left[\beta_{i, j}\right]_{n \times n}$, are established based on the order of jobs in the permutation and the similar blocks of jobs, respectively.

$$
\left[\rho_{i, j}\right]_{n \times n}=\left[\begin{array}{cccc}
\rho_{1,1} & \rho_{1,2} & \ldots & \rho_{1, n} \\
\rho_{2,1} & \rho_{2,2} & \ldots & \rho_{2, n} \\
\ldots & \ldots & \ldots & \ldots \\
\rho_{n, 1} & \rho_{n, 2} & \ldots & \rho_{n, n}
\end{array}\right] \quad\left[\beta_{f, j}\right]_{n \times n}=\left[\begin{array}{cccc}
\beta_{1,1} & \beta_{1,2} & \ldots & \beta_{1, n} \\
\beta_{2,1} & \beta_{2,2} & \ldots & \beta_{2, n} \\
\ldots & \ldots & \ldots & \ldots \\
\ldots & \beta_{n, 1} & \beta_{n, 2} & \ldots & \beta_{n, n}
\end{array}\right]
$$

where $\rho_{i, j}$ is the number of times that job $j$ appears in position $i$ in the selected sequences, and $\beta_{f, j}$ the number of times that job $j$ appears immediately after job $f$. The elements of $\left[\rho_{i, j}\right]_{n \times n}$ and $\left[\beta_{i, j}\right]_{n \times n}$ can be obtained according to Figure 6 .

The probability of each job, $\xi_{i, j}$, in sequence $\pi$ is calculated according to the following equation:

$$
\xi_{i, j}= \begin{cases}\frac{\rho_{i, j}}{\sum_{i \in \mu(i)} \rho_{i, i}} & i=1 \\ \frac{\rho_{i, j}}{\sum_{i \in \mu(i)} \rho_{i, i}}+\frac{\beta_{f, j}}{\sum_{i \in \mu(i)} \beta_{f, j}} & i=2,3, \ldots, n\end{cases}
$$

where $\mu(i)$ is the unscheduled sequence set, and $i$ the position that job $j$ appears in the sequence.
Generate new offspring. Let the new solution be empty, that is, $\pi_{\text {new }}=\phi$. First, regard the $i$ th sequence of the original population as the unscheduled sequence $\mu(i)$, and then, the first job of the new sequence, $\pi_{\text {new }}$, is obtained as follows. Randomly take 5 jobs from the unscheduled sequence and compute their probabilities according to Equation (13). Followed that the job with the largest probability among the 5 jobs is picked up and viewed as the first job of the new sequence. Second, set $i=i+1$, and a new subsequence $\mu(i)$ is constructed by deleting the selected job from $\mu(i-1)$. Calculate the probability of each job in $\mu(i)$ according to Equation (13), and put the job with the largest probability into the $i$ th position of $\pi_{\text {new }}$. Repeat the second step until $\pi_{\text {new }}$ is a legal and complete sequence.

In this section, an example for constructing the new offspring is given as follows. Suppose that there are 7 selected sequences in the candidate population, $\left[\eta_{i, j}\right]_{P S \times n}(P S=7)$, and each has 7 jobs. The candidate population, $\left[\rho_{i, j}\right]_{n \times n}$ and $\left[\beta_{i, j}\right]_{n \times n}$, are given as follows:
$\left[\eta_{i, j}\right]_{7 \times 7}=\left[\begin{array}{cccccc}2 & 6 & 1 & 4 & 7 & 5 & 3 \\ 7 & 2 & 5 & 1 & 4 & 4 & 6 \\ 3 & 2 & 7 & 6 & 5 & 4 & 1 \\ 1 & 4 & 7 & 2 & 6 & 5 & 3 \\ 2 & 3 & 4 & 7 & 6 & 5 & 1 \\ 5 & 3 & 7 & 6 & 4 & 1 & 2 \\ 4 & 1 & 7 & 5 & 3 & 2 & 6\end{array}\right] \quad\left[\rho_{i, j}\right]_{7 \times 7}=\left[\begin{array}{cccccc}1 & 2 & 1 & 1 & 1 & 0 & 1 \\ 1 & 2 & 2 & 1 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 & 1 & 0 & 4 \\ 1 & 1 & 0 & 1 & 1 & 2 & 1 \\ 0 & 0 & 1 & 2 & 1 & 2 & 1 \\ 1 & 1 & 1 & 1 & 3 & 0 & 0 \\ 2 & 1 & 2 & 0 & 0 & 2 & 0\end{array}\right] \quad\left[\beta_{f, j}\right]_{7 \times 7}=\left[\begin{array}{cccccc}
- & 1 & 0 & 3 & 0 & 0 & 1 \\
0 & - & 1 & 0 & 1 & 3 & 1 \\
0 & 2 & - & 1 & 0 & 1 & 1 \\
3 & 0 & 1 & - & 0 & 0 & 1 \\
2 & 0 & 4 & 1 & - & 0 & 0 \\
1 & 0 & 0 & 1 & 3 & - & 0 \\
0 & 2 & 0 & 0 & 2 & 3 & -
\end{array}\right]$

Let $\mu(1)=\{1,2,3,4,5,6,7\}, \pi_{\text {new }}=\phi$
(a) Let $i=1$, randomly select 5 jobs from $\mu(1)$, for example, $2,3,5,6,7$, and compute their probabilities.

$$
\begin{aligned}
& \xi_{1,2}=2 /(1+2+1+1+1+0+1)=0.286 \\
& \xi_{1,3}=1 /(1+2+1+1+1+0+1)=0.143 \\
& \xi_{1,5}=1 /(1+2+1+1+1+0+1)=0.143 \\
& \xi_{1,6}=0 /(1+2+1+1+1+0+1)=0 \\
& \xi_{1,7}=1 /(1+2+1+1+1+0+1)=0.143
\end{aligned}
$$

The job with the largest probability among the 5 jobs is picked up, that is, $\pi_{\text {new }}=\{2\}$.
(b) Let $i=i+1$, the unscheduled subsequence $\mu(i)$ consists of the remaining of $\mu(i-1)$, that is, $\mu(i)=\{1,3,4,5,6,7\}$. Next, calculate the probability of each job in $\mu(i)$ :

![img-3.jpeg](img-3.jpeg)

Figure 7. Insert_ $f(\pi, p 1, p 2)$, insert_ $b(\pi, p 1, p 2)$ and $\operatorname{swap}(\pi, p 1, p 2)$.

$$
\begin{aligned}
& \xi_{2,1}=(1 /(1+2+1+0+1+0)+0 /(0+1+0+1+3+1))=2=0.100 \\
& \xi_{2,3}=(2 /(1+2+1+0+1+0)+1 /(0+1+0+1+3+1))=2=0.283 \\
& \xi_{2,4}=(1 /(1+2+1+0+1+0)+0 /(0+1+0+1+3+1))=2=0.100 \\
& \xi_{2,5}=(0 /(1+2+1+0+1+0)+1 /(0+1+0+1+3+1))=2=0.083 \\
& \xi_{2,6}=(1 /(1+2+1+0+1+0)+3 /(0+1+0+1+3+1))=2=0.375 \\
& \xi_{2,7}=(0 /(1+2+1+0+1+0)+1 /(0+1+0+1+3+1))=2=0.083
\end{aligned}
$$

Put the job with the largest probability into $\pi_{\text {new }}$, that is, $\pi=\{2,6\}$. If $i<n(n=7)$, go to step (b); otherwise, stop the process.

# 3.2.2 Mutation 

The insertoperator has two ways, named forward insertion, insert_ $f$, and backward insertion, insert_b. As shown in Figure 7, insert_ $f$ randomly selects two different positions, $p 1$ and $p 2$. If $p 1<p 2$, all jobs between position $p 1+1$ and $p 2$ move forward a position in turn. At last, put the original job in position $p 1$ into position $p 2$. As for insert_b, randomly select two different positions, $p 1$ and $p 2$. When $p 1<p 2$, all jobs between position $p 1+1$ and $p 2$ move backward a position in turn. With respect to the swap operator, randomly select two different positions from the sequence, and interchange their corresponding jobs.

Insert and swap operators are commonly used to generate neighbouring solutions for flow shop scheduling problems (Wang 2003) and have been demonstrated as superior to the inverse neighbourhood (Ruiz and Thomas 2008). In this section, six strategies based on insert and swap operators are proposed on this account: (1) perform insert_ $f$ once; (2) apply insert_b one time; (3) conduct the swap operator once; (4) employ insert_ $f$ twice; (5) use insert_b two times; and (6) execute the swap operator twice.

Generally speaking, more strategies generate different solutions with a larger probability than a single strategy and avoid the population trapping in local optima, we randomly chose one of the above six strategies to generate a new offspring.

### 3.3 Environmental selection

The environmental selection of NSGA-II mainly includes constructing a non-dominated set and picking up PS individuals. To speed up the convergence and maintain the diversity of the population, the selection operator based on the crowed distance developed by Deb et al. (2002) is utilised, and its detailed steps are given in Figure 8.

### 3.4 Restart strategy

The diversity of the population may diminish at certain generations, and many job sequences in the population may become very similar, which leads to the stagnation of the population's evolution. To overcome the above problem, when

Begin
Step 1. Initialize variables
$\operatorname{num}[r]=0, r=1, \mathrm{f}=$ false, $\mathrm{F}=\left\{\mathrm{F}_{1}, \mathrm{~F}_{2}, \ldots\right\} \%$ The array num denotes the number of non-dominated solutions, and $r$ the rank of each solutions; variable $f$ flags whether the solution has been selected or not. F is a bounded set to save the solutions of each rank.
Step 2. Combine the father with offspring populations and sort non-dominated solutions while( the flags of all solutions are equal to false) do

$$
\mathrm{F}_{i}=\phi
$$

for $i=1$ to $\mathrm{PS}+\mathrm{PS}$

$$
\text { if }\left(\pi_{i} . \mathrm{f}==\text { falseand } \pi_{i} \prec \forall \pi_{i}\right) \mathrm{j} \in\{1,2, \ldots, \mathrm{PS}+\mathrm{PS}\} \cap \mathrm{j} \neq \mathrm{i} \text { then }
$$

The rank of $\pi_{i}$ is equal to $r$, that is, $\pi_{i} \cdot \operatorname{rank}=r$;

$$
\begin{aligned}
& \mathrm{F}_{i}=\mathrm{F}_{i} \cup \pi_{i} \\
& \operatorname{num}[\mathrm{r}]=\operatorname{num}[\mathrm{r}]+1 \\
& \pi_{i} . \mathrm{f}=\text { true }
\end{aligned}
$$

end if
end for

$$
\mathrm{r}=\mathrm{r}+1
$$

end do
Step 3. Set $\mathrm{P}=\phi, \mathrm{r}=1$;
Step 4. Select PS individual as new farther population
while $(|\mathrm{P}| \neq \mathrm{PS})$ do
if $(\operatorname{num}[\mathrm{r}]+|\mathrm{P}|<\mathrm{PS})$ then
$\mathrm{P}=\mathrm{P} \cup \mathrm{F}_{i} \quad \mathrm{r}=\mathrm{r}+1 ;$
else if $(\operatorname{num}[\mathrm{r}]+|\mathrm{P}|>P S)$
The bounded sets $\mathrm{F}_{i}$ are taken and sorted according to makespan in a descendent order. Compute the crowded distance of each solution in $\mathrm{F}_{i}$ according to following equation:

$$
\operatorname{distance}\left(\pi_{i}\right)=\sum_{s=0}^{S-1} \sum_{k=1}^{S}\left(\mathrm{f}_{s+1, k}-\mathrm{f}_{s-1, k}\right)
$$

The $\mid \mathrm{PS}-\operatorname{num}[\mathrm{r}] \mid$ solutions with the largest crowding distance will be picked up and put in $\mathrm{p} ;$ break;
else
$\mathrm{P}=\mathrm{P} \cup \mathrm{F}_{i} ;$ break;
end if
end do
End

Figure 8. Pseudo code of environmental selection.
the diversity falls below a given threshold, $\gamma$, adopting a restart strategy based on the ideas adopted by the authors in (Pan and Ruiz 2012 and Ruiz et al. 2006) is much more necessary. The detailed steps are stated as follows:

Step 1: Two matrixes, $\left[\rho_{i, j}\right]_{n \times n}$ and $\left[\beta_{i, j}\right]_{n \times n}$, are constructed using the same method as in Section 3.2.1 with the exception that $\left[\rho_{i, j}\right]_{n \times n}$ and $\left[\beta_{i, j}\right]_{n \times n}$ record information of the current population.
Step 2: Count the number of elements larger than zero in $\left[\rho_{i, j}\right]_{n \times n}$ and denote it as $\theta$.
Step 3: Count the number of elements larger than zero in $\left[\beta_{i, j}\right]_{n \times n}$ and denote it as $\eta$.
Step 4: Compute the diversity of the current population according to the following formula presented by the authors in (Pan and Ruiz 2012).

$$
\text { diversity }(P)=\left(\frac{\theta-n}{n \times \min (P S, n)}+\frac{\eta-(n-1)}{(n-1) \times \min (n-1, P S-1)}\right) / 2
$$

Step 5: If diversity $(P)<\gamma$, put the $40 \%$ non-dominated solutions chosen from the current non-dominated set into the current population, and the rest are randomly generated.
In this section, two simple examples about the diversity are given. Suppose that there are four sequences in the current population, $P$. The population and the two matrixes are shown as follows:

Example 1:

$$
\begin{aligned}
& P=\left[\begin{array}{llll}
1 & 2 & 3 & 4 \\
1 & 2 & 3 & 4 \\
1 & 2 & 3 & 4 \\
1 & 2 & 3 & 4
\end{array}\right] \quad|\rho|_{4 \times 4}=\left[\begin{array}{llll}
4 & 0 & 0 & 0 \\
0 & 4 & 0 & 0 \\
0 & 0 & 4 & 0 \\
0 & 0 & 0 & 4
\end{array}\right] \quad|\beta|_{4 \times 4}\left[\begin{array}{llll}
0 & 4 & 0 & 0 \\
0 & 0 & 4 & 0 \\
0 & 0 & 0 & 4 \\
0 & 0 & 0 & 0
\end{array}\right] \\
& \text { diversity }(P)=\left(\frac{4-4}{4 \times \min (4,4)}+\frac{3-(4-1)}{(4-1) \times \min (4-1,4-1)}\right) / 2=0
\end{aligned}
$$

Example 2:

$$
\begin{aligned}
& P=\left[\begin{array}{llll}
1 & 2 & 3 & 4 \\
2 & 1 & 4 & 3 \\
3 & 4 & 2 & 1 \\
4 & 3 & 1 & 2
\end{array}\right] \quad|\rho|_{4 \times 4}=\left[\begin{array}{llll}
1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1
\end{array}\right] \quad|\beta|_{4 \times 4}=\left[\begin{array}{llll}
0 & 2 & 0 & 1 \\
2 & 0 & 1 & 0 \\
1 & 0 & 0 & 2 \\
0 & 1 & 2 & 0
\end{array}\right] \\
& \text { diversity }(P)=\left(\frac{16-4}{4 \times \min (4,4)}+\frac{8-(4-1)}{(4-1) \times \min (4-1,4-1)}\right) / 2=0.65
\end{aligned}
$$

It can be seen from the above examples that the diversity is in the range of zero to one. When the sequences of the population are every similar or identical, the diversity trends or equals to zero, as shown in Example 1. However, as shown in Example 2, all sequences of the population are different, that is, different jobs occupy different positions, and no similar job blocks exist among these sequences, so the diversity trends to one. It can be observed that the larger the diversity, the more diverse the population. Another mentionable thing is that the diversity is computed when the number of iterations is larger than or equal to 100 , which can reduce the computation overhead.

# 3.5 Summarising the proposed algorithm 

With the above approaches, the proposed algorithm can be summarised as follows:
Step 1: Set the values of such parameters as $P S$ (the population size), $p c$ (the crossover probability), $\gamma$ (the diversity threshold) and time (the maximal computation time), and let $t=0$ (the number of iterations).
Step 2: Initialise the population using the method in Section 3.1, and evaluate each solution in the population according to formula 1 to 8 .
Step 3: Repeat the following steps, until the termination condition is satisfied.
Step 3.1: Generate the new offspring by adopting EDA with the probability of $p c$ and the insert and swap operators with $1-p c$ probability presented in Section 3.2.
Step 3.2: Perform the environment selection operator based on non-dominated sorting and the crowed distance by using the method in Section 3.3.
Step 3.3: Update the archive and father population, and save the limited non-dominated solutions obtained so far.
Step 3.4: Let $t=t+1$. If the number of iterations is greater than or equal to 100 , compute the diversity of the current population. If the diversity is smaller than the given threshold, apply the restart strategy to initialise the current population according to Section 3.4 , and set $t=0$.

## 4. Evolution metric

In general, non-dominated solutions have a close relationship with the Pareto-optimal front; thus, the quality of these non-dominated solutions is very important to evaluate the performance of an algorithm. In this paper, the following four

metrics are employed to evaluate the obtained non-dominated solutions: the number of obtained non-dominated solutions, the ratio of non-dominated solutions, the average distance between the non-dominated solutions to the reference solutions, and the spread and the distribution of the obtained non-dominated solutions. Denote the non-dominated solutions set obtained by $j$ th $(j \in\{1,2,3,4\})$ algorithm as $S_{j}$, where $S_{j} \in N D S\{I N S G A-I I, N S G A-I I, D H S, T A\}$. Let $S$ be the union of all non-dominated solution sets. It is worth mentioning that the true Pareto front is often not known for a multi-objective optimisation problem, so a reference set is used to evaluate the performance of an algorithm in the literature (Pan et al. 2009). In this work, the Pareto-optimal front of the best-so-far solutions obtained by all these algorithms is regarded as the reference set $S^{*}$.

# 4.1 The number of non-dominated solutions, $N\left(S_{j}\right)$ 

The non-dominated solutions obtained by the $j$ th algorithm are compared with the union of all non-dominated solutions $S$, and the number of solutions in $S_{j}$ that are not dominated by any solution in $S$ is counted. Its definition is as follows (Pan et al. 2009):

$$
N\left(S_{j}\right)=\left|x^{\prime} \in S_{j}\right| \exists x^{\prime} \prec 1 / y, \quad y \in S, x \neq y \mid \quad S=\bigcup_{j=1,2,3,4} S_{j}
$$

It can be seen from Equation (16) that the larger the metric $N\left(S_{j}\right)$, the better the $j$ th algorithm.

### 4.2 The ratio of non-dominated solutions, $R\left(S_{j}\right)$

The value of $R\left(S_{j}\right)$, equal to the ratio of $N\left(S_{j}\right)$ to $\left|S_{j}\right|$, is used to evaluate the quality of solutions in $S_{j}$ (Pan et al. 2009). The value of $R\left(S_{j}\right)$ is in the range of zero to one, and if $R\left(S_{j}\right)=0$, it means that any solution in $S_{j}$ is dominated by some solution(s) in $S$; when $R\left(S_{j}\right)=1$, it shows that any solution in $S_{j}$ is not dominated by solutions in $S$; with respect to $0<R\left(S_{j}\right)<1$, it refers that there exist some solutions in $S_{j}$ not dominated by any solution in $S$. Thus, the larger the metric $R\left(S_{j}\right)$, the better the quality of $S_{j}$.

### 4.3 The average distance between the Pareto-optimal front and solution set $S_{j}$

The metric $\mathrm{D}\left(S_{j}\right)$ shows the shortest normalised average distances between reference solutions and the set $S_{j}$, which reflects the convergence of the solutions in the algorithm $S_{j}$ towards to the Pareto-optimal front (Pan et al. 2009). The smaller the $D\left(S_{j}\right)$, the better approximation to the reference set. The equation is shown as follows.

$$
\begin{gathered}
D\left(S_{j}\right)=\frac{1}{\left|S^{*}\right|} \sum_{j \in S^{*}} d_{j}\left(S_{j}\right) \\
d_{j}\left(S_{j}\right)=\min _{x \in S_{j}}\left\{\sqrt{\sum_{k=1}^{4}\left(\frac{f_{k}(x)-f_{k}(y)}{f_{k}^{\max }(\bullet)-f_{k}^{\min }(\bullet)}\right)^{2}}\right\}
\end{gathered}
$$

where $f_{k}(\bullet)$ denotes the $k$ th objective value; and $f_{k}^{\max }(\bullet)$ and $f_{k}^{\min }(\bullet)$ are the minimum and maximum of the $k$ th objective value in the reference set $S^{*}$, respectively. The $\left|S^{*}\right|$ is the number of reference solutions in $S^{*}$.

### 4.4 The spread of non-dominated solutions

The $S C\left(S_{j}\right)$ is utilised to measure the performance of non-dominated solutions in distribution in the objective space (Veldhuizen and Lamont 2000). Its definition is stated as follows:

$$
\begin{gathered}
S C\left(S_{j}\right)=\sqrt{\frac{1}{\left|S_{j}\right|-1} \sum_{i=1}^{\left|S_{j}\right|}\left(\bar{d}-d_{i}\right)^{2}} \\
d_{i}=\min _{j \in\left\{1,2, \ldots,\left|S_{j}\right|\right\}}\left(\sum_{k=1}^{4}\left|f_{k}^{i}(x)-f_{k}^{j}(x)\right|\right) \quad x \in S_{j} \quad i \in\left\{1,2, \ldots,\left|S_{j}\right|\right\} \cap i \neq j
\end{gathered}
$$

$$
\bar{d}=\frac{1}{\left|S_{j}\right|} \sum_{i=1}^{\left|S_{j}\right|} d_{i}
$$

where $d_{i}$ is the Euclidean distance between $x$ and its nearest neighbour. As can be observed from Equation (18), the variance value $S C\left(S_{j}\right)=0$ reflects the uniform distribution of solutions in $S_{j}$. On the contrary, $S C\left(S_{j}\right)$ explains the irregular distribution of solutions in $S_{j}$. So, the smaller the value of $S C\left(S_{j}\right)$, the more uniform the non-dominated solutions.

# 5. Experiments 

The experiments are conducted to evaluate the performance of the proposed algorithm in this section. All algorithms are written with $\mathrm{C}++$ and implemented in a PC with Pentium(R) Dual 2.8 GHZ and 2G memory. Each instance is independently run 5 times, and its average computational time is also reported. Following Veldhuizen and Lamont (2000) and Tseng and Liao (2008), the data for the instances of the LSFS scheduling problem are given by discrete uniform distributions.

### 5.1 Experimental setting

- The population size, $P S$, the crossover probability, $p c$, and the size of the external archive are set to 20, 0.6 and 100 , respectively.
- The numbers of jobs and machines for each instance are randomly chosen from the following sets $n \in\{10,30,50,70,90,110\}$ and $m \in\{5,10,15,20\}$, respectively.
- For each instance, the maximal computation time is set to $m \times n$ milliseconds.
- Set the due date of each job as $d_{i}=\operatorname{rand}() \%(15 \times m+1)+15 \times n$.
- Let the number of sub-lots of each job $\pi(i)$ be $l_{\pi(i)}=\operatorname{rand}() \% 6+1$.
- The processing time of job $i$ on machine $t$ is set as $P_{\pi(i), t}=\operatorname{rand}() \% 31+1$.

Table 2. Performance of proposed vNEH strategy and random one.

Table 3. Performance of six strategies of mutation operator in $D\left(S_{i}\right)$ and $R\left(S_{f}\right)$.

# 5.2 Experimental results 

Han (2012) developed the discrete HS (DHS) algorithm for solving the multi-objective LSFS scheduling problem, with providing better results than NEH algorithm. Marimulthu et al. (2009) presented the TA algorithm for the same problem. In this paper, the proposed algorithm (INSGA-II, for short) is compared with these existing algorithms in the literature, that is, DHS, TA and the basic NSGA-II. Meanwhile, all parameters commonly used in these algorithms are set the same values as those in their original paper. The experimental results are shown in the following tables and figures.

### 5.2.1 Performance of initialisation strategies

To evaluate the performance of the proposed vNEH, Table 2 reports the performance of vNEH and the random strategy on the premise of the same parameters, where the column of 'vNEH' represents the data corresponding to the proposed vNEH strategies and that of 'Random' refers to the data corresponding to randomly initialising the population.

As can be observed from Table 2, with respect to the ratio of the non-dominated solutions and the distance between the reference set and the solution set, there are $80 \%$ non-dominated solutions yielded by the proposed vNEH strategies, and the distance is 0.1 , whereas those obtained by the random strategy are $40 \%$ and 0.46 , respectively, on the premise of the same computational time. So, the proposed initialisation strategies can generate solutions with high quality and accelerate the convergence of the population.

### 5.2.2 Performance of proposed mutation operator

To evaluate the performance of the six strategies, Table 3 lists the data of such indicators as the ratio of non-dominated solutions and the distance between the reference set and the solution set, where ' $r m$ ' $(m=1,2,3,4,5,6)$ represents the data corresponding to the $m$ th strategy of the proposed mutation operator.

From Table 3, (1) for the indicator of $D\left(S_{f}\right)$, the value obtained by using the fourth strategy is smaller than those of the rest strategies, followed by the value of $r 1$ and $r 2$. The sixth strategy is the worst, suggesting that the insert operator has a good performance in convergence; (2) with respect to the indicator of $R\left(S_{f}\right)$, the value obtained by using the sixth strategy is larger than those of the rest strategies, followed by the value of $r 1$ and $r 5$, indicating that the swap operator

Table 4. The number of solutions in $S_{j}$ obtained by INSGA-II, NSGA-II, DHS and TA algorithms.

Table 5. Number of non-dominated solutions $N\left(S_{j}\right), R\left(S_{j}\right)$ and $D\left(S_{j}\right)$ of the INSGA-II, NSGA-II, DHS and TA algorithms.

![img-4.jpeg](img-4.jpeg)

Figure 9. Scatter $S C\left(S_{j}\right)$ of INSGA-II, NSGA-II, DHS and TA algorithms.
can generate more non-dominated solutions than the insert operator. Since insert and swap operators show good performances from various indicators, we randomly chose one of these six strategies to generate a promising offspring.

# 5.2.3 Performance of INSGA-II, NSGA-II, DHS and TA algorithms 

The number of solutions in $S_{j}, N\left(S_{j}\right), R\left(S_{j}\right), D\left(S_{j}\right)$ and $S C\left(S_{j}\right)$ produced by INSGA-II, NSGA-II, DHS and TA algorithms is reported in Tables 4 and 5, respectively. The bottom rows of these tables give the mean values of the corresponding metrics.
(1) Table 4 presents the average (AVG), the minimal (MIN) and the maximal (MAX) numbers of solutions in $S_{j}$ obtained by INSGA-II, NSGA-II, DHS and TA, respectively, in 5 independent runs. It can be clearly found from Table 4 that the overall AVG (86.4), MAX (88.8) and MIN (87.6) yielded by INSGA-II are much better than those generated by NSGA-II, DHS and TA algorithms in the same computation time. The reason why INSGA-II is better than the other algorithms is that the proposed algorithm can take full of the non-dominated solutions to generate excellent offspring and the insertion and swap operators to disturb old individuals.
(2) The superiority of INSGA-II over NSGA-II, DHS and TA algorithms is further demonstrated by Table 5 in terms of $N\left(S_{j}\right)$ and $R\left(S_{j}\right)$. Combining Tables 4 and 5, in the average, $91 \%$ non-dominated solutions yielded by INSGA-II are not dominated by any other solution in $S$, significantly more than those obtained by NSGAII, DHS and TA algorithms. Especially, for large size instances, such as $70 \times 15,90 \times 5,90 \times 10,110 \times 20$, the value of $R\left(S_{j}\right)$ generated by INSGA-II is equal to $100 \%$. Thus, it can be concluded that the proposed algorithm yields more non-dominated solutions with high quality than the comparative ones.
(3) As mentioned before, due to the true Pareto front of an optimisation problem is difficult to find, a reference solution set is necessary to compute the performance measure $D\left(S_{j}\right)$. Table 5 reports the shortest distance, $D\left(S_{j}\right)$, between the achieved non-dominated solutions and the reference set. Within the same computational time, the average distance produced by INSGA-II is 0.02 , whereas those obtained by NSGA-II, DHS and TA algorithms are $2.37,0.24$ and 2.52 , respectively. Therefore, with respect to the average distance, it is evident that INSGA-II performs better than the comparative ones for all instances.
(4) Figure 9 gives a more intuitive illustration on the spread of neighbourhood vectors of achieved non-dominated solutions. As Figure 8 shows, for almost all instances, the non-dominated solutions generated by INSGA-II are uniformly distributed. It is worth noting that the spread of NSGA-II is highly not uniform. The reason is that NSGA-II is suitable for solving continuous optimisation problems, but hardly for generating discrete values. So, NSGA-II is less effective and efficient for the LSFS scheduling problem. Based on the data of

![img-5.jpeg](img-5.jpeg)

Figure 10. Optimal solution of the $10 \times 5$ instance $\left(f_{1}=597, f_{2}=541, f_{3}=3210, f_{4}=138\right)$ obtained by INSGA-II.
![img-6.jpeg](img-6.jpeg)

Figure 11. Optimal solution of the $10 \times 5$ instance $\left(f_{1}=599, f_{2}=554, f_{3}=3922, f_{4}=18\right)$ obtained by INSGA-II.

Table 5 and Figure 9, the superior performance of the proposed algorithm in convergence and distribution can be justified.
(5) In addition, Gantt charts of the two test instances, $10 \times 5$ and $10 \times 20$, are showed in Figures 10, 11 and 12 in the light of the non-dominated solutions obtained by INSGA-II, respectively. Figures 9 and 10 show two scheduling results of the $10 \times 5$ instance, corresponding to the following two optimal solutions $\{7,8,9,4,3$, $10,6,1,2,5\}$ and $\{6,7,9,4,8,3,1,2,10,5\}$. The due dates of job $i, i \in\{1,2, \ldots, 10\}$, are $\{191,218,189$, $170,205,178,199,168,156,157\}$, and the numbers of sub-lots of these jobs are $\{2,1,4,3,1,1,4,6,6,2\}$. Figure 12 illustrates the Gantt chart of the $10 \times 20$ instance, corresponding to the optimal solution $\{1,6,8$, $10,5,9,4,3,2,7\}$. The due dates of job $i, i \in\{1,2, \ldots, 10\}$, are $\{191,442,410,388,315,357,346,441,417$, 335\}, and the numbers of sub-lots of these jobs are $\{6,5,5,4,1,1,6,3,2,2\}$.

In summary, Tables 4 and 5 give us a clear illustration that the non-dominated solutions obtained by INSGA-II have better quality. The superiority of the proposed algorithm attributes to EDA and the insertion and swap operators, by which its capabilities in exploration and exploitation are improved.

# 5.2.4 Wilcoxon two-sided rank sum test 

Table 6 reports the two-side Wilcoxon rank sum tests of null hypothesis of INSGA-II, NSGA-II, DHS and TA algorithms with significant level of $5 \%$. The test is equivalent to a MANN-Whitney U-test. In Table 6, there are two values, that is, $p$ and $h$ values, where $p$ is the probability of observing the given result if the null hypothesis is true. When $h$

![img-7.jpeg](img-7.jpeg)

Figure 12. Optimal solution of the $10 \times 20$ instance $\left(f_{1}=1126, f_{2}=7643, f_{3}=7452, f_{4}=21\right)$ obtained by INSGA-II.

Table 6. The Wilcoxon two-sided rank sum test results of INSGA-II, NSGA-II, DHS and TA algorithms.

equals 1 , it indicates that the results obtained by the two compared algorithms are significantly different. If $h$ is equal to 0 , the difference between the two algorithms is not significant at $5 \%$ significant level. As shown in Table 6, the $p$ value is approximately equal to 0 and the $h$ value is exactly equal to 1 , suggesting that INSGA-II is significantly different from the other comparative algorithms in terms of $D\left(S_{j}\right)$.

# 5.2.5 Sensitivity study on parameter pc 

Hereinafter, there is a parameter, $p c$, which controls whether the offspring individual undergoes EDA or not. Obviously, pc is an important parameter for INSGA-II. Therefore, investigating the effect of $p c$ by doing experiments is much necessary. Without loss of generality, the value of pc changes from 0 to 1.0 with the step size of 0.1 . The benchmark instances and the parameter settings are kept the same as in Section 5.1. The comparative results in terms of the quality and the distribution of non-dominated solutions are shown in Figures 12 and 13.

![img-8.jpeg](img-8.jpeg)

Figure 13. Sensitivity study of pc with respect to the ratio of non-dominated solutions.
![img-9.jpeg](img-9.jpeg)

Figure 14. Sensitivity study of pc from the viewpoint of the distribution of non-dominated solutions.
Figure 13 reports that the trajectory tendency is relatively stable when the value of $p c$ is in the range of $[0,0.2]$, and then, the ratio of non-dominated solutions gradually decreases to a low level. When $p c$ is equal to 0.6 , the above ratio is greater than the others, suggesting that EDA can take full advantage of valuable information of non-dominated solutions to estimate the probability distribution of good chromosomes to generate promising offspring. When the value of $p c$ is in the range of $[0.7,1]$, the value of $R\left(S_{j}\right)$ becomes small along with the increase of $p c$. Specifically, $p c=1$ represents that there is no mutation operator and the whole algorithm only adopts EDA to generate offspring, which will result in obtaining local optimal of the optimisation problem. Thus, we set the value of pc as 0.6 in this study. Similar experiments are done from the viewpoint of the distribution of non-dominated solutions. Figure 14 shows that when pc is equal to 0.6 , the SC value is smaller than the others. The above experimental results demonstrate that the performance of INSGA-II is sensitive to its parameter.

# 6. Conclusions 

LSFS scheduling problems with single objective are not sufficient in modern manufacturing environments, and the multi-objective LSFS scheduling problems play a key role in real-world applications. Therefore, developing effective strategies for the multi-objective ones is necessary and significant.

In recent years, NSGA-II has attracted much attention in the community of evolutionary optimisation. However, the applications of NSGA-II in practical problems are not fully investigated. Thus, an improved NSGA-II is proposed to

solve the multi-objective LSFS scheduling problem in this study. The characteristics of the proposed algorithm lie mainly in the following three aspects: (1) four variants of NEH heuristics are designed to form initial individuals with a good performance in the initialisation phase; (2) EDA taking full advantage of valuable information of non-dominated solutions and the mutation operators based on insertion and swap are embedded in the proposed algorithm to generate good offspring; (3) an efficient restarting strategy is employed to maintain the diversity of the population and avoids the population trapping in local optima.

The performance of INSGA-II proposed in this paper is evaluated on a set of 24 instances and compared with NSGA-II, DHS and TA algorithms. The experimental results demonstrated the superiority of the proposed algorithm in terms of the quality and distribution of non-dominated solutions. It is worth mentioning that the outperformance of the proposed algorithm attributes to EDA and mutation operators, by which its capabilities in exploration and exploitation are improved.

There are also some limitations in our work. The exploitation capability of multi-objective evolutionary algorithms should be further considered. The future work is to apply INSGA-II to solve other scheduling problems with different objectives.

# Funding 

This research is partially supported by Natural Science Foundation of China under Grant Nos. 61105063, 61075061, 61104179 and 61174187, the Fundamental Research Funds for the Central Universities and Research, Innovation Project for College Graduates of Jiangsu Province with Granted No. CXZZ13 0932, Basic scientific research foundation of Northeast University under Grant N110208001, starting foundation of Northeast University under Grant 29321006 and Science Foundation of Liaoning Province in China (2013020016).
