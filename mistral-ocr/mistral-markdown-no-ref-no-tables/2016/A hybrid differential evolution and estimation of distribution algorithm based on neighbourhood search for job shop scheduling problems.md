# A hybrid differential evolution and estimation of distribution algorithm based on neighbourhood search for job shop scheduling problems 

Fuqing Zhao ${ }^{\mathrm{a}, \mathrm{b} *}$, Zhongshi Shao ${ }^{\mathrm{a}}$, Junbiao Wang ${ }^{\mathrm{b}}$ and Chuck Zhang ${ }^{\mathrm{c}}$<br>${ }^{a}$ School of Computer and Communication Technology, Lanzhou University of Technology, Lanzhou, China; ${ }^{b}$ Key Laboratory of Contemporary Design \& Integrated Manufacturing Technology, Ministry of Education, Northwestern Polytechnical University, Xi'an, China; ${ }^{c}$ H. Milton Stewart School of Industrial \& Systems Engineering, Georgia Institute of Technology, Atlanta, GA, USA

(Received 24 August 2014; accepted 2 April 2015)


#### Abstract

Job shop scheduling problem (JSSP) is a typical NP-hard problem. In order to improve the solving efficiency for JSSP, a hybrid differential evolution and estimation of distribution algorithm based on neighbourhood search is proposed in this paper, which combines the merits of Estimation of distribution algorithm and Differential evolution (DE). Meanwhile, to strengthen the searching ability of the proposed algorithm, a chaotic strategy is introduced to update the parameters of DE. Two mutation operators are adopted. A neighbourhood search (NS) algorithm based on blocks on critical path is used to further improve the solution quality. Finally, the parametric sensitivity of the proposed algorithm has been analysed based on the Taguchi method of design of experiment. The proposed algorithm was tested through a set of typical benchmark problems of JSSP. The results demonstrated the effectiveness of the proposed algorithm for solving JSSP.


Keywords: estimation of distribution algorithm; differential evolution algorithm; neighbourhood search; hybrid optimisation; job shop scheduling

## 1. Introduction

The job shop scheduling problem (JSSP) is one of the most complicated combinatorial optimisation problems (Garey, Johnson, and Sethi 1976). In JSSP, there are $n(n \geq 1)$ jobs to be processed through $m(m \geq 1)$ machines. Each job must pass through each machine only once. Each job could be processed through the machines in a special order, and there are no precedence constraints among different jobs. Each machine can process at most one operation at the same time. There is no set-up or tardiness cost. Each machine has full efficiency. Moreover, the processing time of each operation is fixed and known. In this paper, the minimisation of makespan is selected as the objective, which is to find a schedule to minimise the time required to complete all jobs.

JSSP has been demonstrated to be a strongly NP-hard problem (Garey, Johnson, and Sethi 1976), and it cannot be exactly solved in a reasonable computational time. At first, mathematical methods (Qing-Dao-Er-Ji and Wang 2012) were used to solve JSSP, such as shifting bottleneck procedure, branch and bound and dynamic programming. However, due to the complexity of JSSP, it is unrealistic to solve even a medium-sized problem using reasonable time. Thus, others began to use meta-heuristics to solve JSSP. These methods (Gao et al. 2011) mainly include taboo search, genetic algorithm, simulated annealing, ant colony optimisation, artificial immune system, particle swarm optimisation (PSO) and memetic algorithm, etc. Compared with the mathematical methods, the meta-heuristics make better trade-off between solution quality and computational time, which can be relatively easy to implement and conveniently be adapted to different kinds of scheduling problems. However, the single meta-heuristic neither has an effective local search mechanism for accurately searching near solutions nor global exploration to fully explore the solution space. In order to overcome these drawbacks, estimation of distribution algorithm (EDA) based on global information search and differential evolution (DE) algorithm based on local information search will be incorporated to solve JSSP in this paper.

EDA is a new evolutionary search method. EDA explicitly learns and builds a probabilistic model to capture the parental distribution. Offspring individuals are sampled from the probabilistic model (Hauschild and Pelikan 2011). EDA is good at the automatic discovery and exploitation of problem regularities. A population evolves with intensive communication among all of the promising individuals, readily extracts promising region of search space (Pelikan, Goldberg, and Lobo 2002). Therefore, EDA has strong global exploration, it can be considered as a strongly cooperative

search method. EDA has been combined with other optimisation algorithms to solve the practical problems (Bai et al. 2012; Ou-Yang and Utamima 2013).

DE algorithm is an optimisation algorithm based on the theory of swarm intelligence (Das and Suganthan 2011). The operations of DE algorithm include mutation, crossover and selection (Das and Suganthan 2011). It solves the optimum problems through competition and cooperation of the population. DE algorithm is easily carried out, has good local search capability, memories the best solution of all individuals and shares the internal information of the population. At present, many improvement measures have been applied to enhance the search ability of DE (Basu 2014; Singh and Srivastava 2014).

In this research, a hybrid differential evolution and estimation of distribution algorithm based on neighbourhood search is proposed (NS-HDE/EDA) to solve JSSP. In NS-HDE/EDA, EDA and DE are selected as two suboptimisation algorithms. Two mutation operators are employed as mutation strategy. The chaotic parameter control (CPC) strategy of reference Wang, Li, and Lai (2009) is employed to enhance the performance of DE. Meanwhile, a neighbourhood search (NS) based on blocks on critical path is proposed to enhance the search ability of the proposed algorithm.

The remainder of the paper is organised as follows. Section 2 reviews recent studies on the JSSP of minimising makespan. Section 3 describes the framework of NS-HDE/EDA. Section 4 discusses the computational study on our algorithm and the parametric sensitivity of our algorithm. Finally, conclusions and future research are drawn in Section 5.

# 2. Literature review 

The JSSP is among the hardest combinatorial problems. Not only it is complicated, but it is one of the worst NPcomplete class members. Variety of literatures discusses JSSP of minimising makespan with meta-heuristic algorithms which include Tabu search (TS, Ferdinando and Emanuela 1998; Meeran and Morshed 2012), simulated annealing (Elmi, Solimanpur, and Topaloglu 2011), genetic algorithm (Wang 2003), shuffled frog leaping (Cai and Xia 2010), artificial neural networks (Wang and Qi-Di 2007), PSO (Sha and Hsu 2006) and so on.

Recently, many more papers have developed innovative meta-heuristic algorithms for this type of JSSP. For example, Huang and Liao (2008) presented a hybrid ant colony optimisation algorithm with the taboo search algorithm for JSSP, which employs a novel decomposition method inspired by the shifting bottleneck procedure and a mechanism of occasional reoptimisations of partial schedules. Hasan et al. (2009) designed three priority rules, namely partial reordering, gap reduction and restricted swapping, which were used as local search techniques to develop a memetic algorithm. Wong et al. (2010) presented an improved bee colony optimisation algorithm with big valley landscape exploitation (BCBV) as a biologically inspired algorithm to solve the JSSP. The BCBV algorithm simulated the bee foraging behaviour, where information of newly discovered food source is communicated via waggle dances. Pan et al. (2010) proposed a discrete differential evolution (DDE) algorithm with operation-based representation to solve JSSP, which adopts a newly designed mutation and crossover operators. Within this algorithm, an effective local search based on the newly obtained neighbourhoods is presented and imbedded in the DDE algorithm to enhance the local search ability. He et al. (2010) proposed an EDA with probability model based on permutation information of neighbouring operations to solve this classical JSSP. Seo and Kim (2010) proposed an ant colony optimisation algorithm with parameterised search space for job shop problem. The problem is modelled as a disjunctive graph where arcs connect only pairs of operationsrelated rather than all operations are connected in pairs to mitigate the increase of the spatial complexity. Gao et al. (2011) proposed an efficient MA with a novel local search. Within the local search, a systematic change of the neighbourhood is carried out to avoid trapping into local optimal. And two neighbourhood structures are designed by exchanging and inserting based on the critical path. Wang and Tang (2011) proposed an improved adaptive genetic algorithm for solving the JSSP which was inspired from hormone modulation mechanism, and then the adaptive crossover probability and adaptive mutation probability are designed. Sels, Craeymeersch, and Vanhoucke (2011) presented a genetic algorithm and a scatter search procedure to solve JSSP. The scatter search algorithm splits the population of solutions in a diverse and highquality set to exchange information between individuals in a controlled way. It has a positive influence on the important balance between intensification and diversification. Qing-Dao-Er-Ji and Wang (2012) proposed a new hybrid genetic algorithm to solve JSSP, who designed some genetic operators and a mixed selection operator based on the fitness value and the concentration value to increase the diversity of the population. Banhamsakun, Sirinaovakul, and Achalakul (2012) proposed an effective scheduling method based on Best-so-far Artificial Bee Colony which biases the solution direction towards the Best-so-far solution rather a neighbouring solution and then use the method to solve JSSP. Li (2012) presented an improve quantum genetic algorithm based on the quantum algorithm theory and quantum chromosome coding knowledge as well as the traditional genetic algorithm for JSSP. Gholami and Sotskov (2013) presented an adaptive algorithm with a learning stage for solving the parallel machines job shop problem. A learning stage tends to produce knowledge about a

benchmark of priority dispatching rules allowing a scheduler to improve the quality of a schedule, which may be useful for a similar scheduling problem. Ponsich and Coello Coello (2013) combined DE with TS to solve the JSSP. A competitive neighbourhood is included within the TS with the aim of determining if DE is able to replace the restart features that constitute the main strengths of i-TSAB. Wang and Duan (2014) proposed a hybrid biogeography-based optimisation (HBBO) algorithm for JSSP. Biogeography-based optimisation (BBO) was a new bio-inspired computation method that was based on the science of biogeography. The BBO algorithm adopted two searching mechanisms including migration and mutation to guarantee the candidates in the search space converge to global optimum solution in faster computational time with stable running process. HBBO algorithm combined the chaos theory and 'searching around the optimum' strategy with the basic BBO to speed up the convergence rate and increase the diversity of candidates in the next running step. Chassaing et al. (2014) addressed JSSPs with an objective of minimising makespan while satisfying a number of hard constraints. An efficient GRASP $\times$ ELS approach was introduced for solving this problem. Zhao et al. (2014) proposed a chemotaxis-enhanced bacterial foraging optimisation to solve the JSSP. The new approach was based on a new chemotaxis with the DE operator which aims at solving the tumble failure problem in the tumble step and accelerates the convergence speed of the original algorithm. Murovec (2015) focused on the evaluation of moves for the local search of the job shop problem with the makespan criterion, which introduced an alternative evaluation that relied on a surrogate quantity of the move's potential, which was related to, but not strongly coupled with, the bare criterion. Zhao et al. (2015) employed the shuffled complex evolution (SCE) algorithm to solve the job shop problem. Due to the drawbacks of poor solution and lower convergence rate of the basic SCE algorithm, a new strategy was used to change the individual's evolution in the basic SCE algorithm. The strategy makes the new individual closer to best individual in the current population. Peng, Lü, and Cheng (2015) incorporated a TS procedure into the framework of path relinking (PR) to proposed TS/PR algorithm. TS/PR is able to improve the upper bounds for 49 out of the 205 tested instances, and it solves a challenging instance that has remained unsolved for over 20 years.

Here, we only list a partial of recent literature. It was not a surprise with the new techniques emphasis substantial progress was made in recent period, which shall be called as the boom period for the new algorithms to JSSP, some of the most innovating algorithms were formulated. Although JSSP is an open topic and many researchers have studied it, many of these methods usually trap into local solution and could not get the global optimum. Therefore, the research on the JSSP is still an important issue in the field of production scheduling.

# 3. The proposed algorithm for JSSP 

### 3.1 Notations for the proposed algorithm

Some symbols used mostly through this paper are summarised as follows:
$n \quad$ number of jobs
$m \quad$ number of machines
$o_{i j} \quad$ the $j$ operation of the job $i$
$J_{i} \quad$ the $i$ th job
$M_{i} \quad$ the $i$ th machine
$t \quad$ the $t$ th generation
$\boldsymbol{X}_{i} \quad$ the population of $i$ th iteration
$\boldsymbol{X}_{i}^{\prime}(i) \quad$ the $i$ th individual of the population of $i$ th iteration
$\boldsymbol{x}_{i} \quad$ the $i$ th individual in population
$x_{i j} \quad$ the $j$ th dimension of the $i$ th individual
$\mu_{j} \quad$ the mean of the $j$ th dimension in current population
$\sigma_{j} \quad$ the standard of the $j$ th dimension in current population
$F_{t} \quad$ the value of the scale factor of $t$ th iteration
$C R_{t} \quad$ the value of the crossover rate of $t$ th iteration
$\gamma_{t} \quad$ the value of the differential decisive factor of $t$ th iteration
$v_{i}^{t} \quad$ the $i$ th mutation individual in $t$ th generation
$v_{i j}^{t} \quad$ the $j$ th dimension of the $i$ th mutation individual in $t$ th generation
$\boldsymbol{u}_{i j}^{t} \quad$ the $j$ th dimension of the $i$ th crossover individual in $t$ th generation
rand a real number between 0 and 1 with uniform distribution
$\pi \quad$ the integer conversion sequence of the individual in population
$\pi_{i j}^{t} \quad$ the $d$ th dimension of the $i$ th conversion sequence
Block $_{i}$ the $i$ th critical sub-block

# 3.2 Encoding and decoding 

The operation-based representation is employed to encode a schedule in this paper. This encoding method uses permutation generated by all job's number to encode a schedule. For an $n$-job $m$-machine JSSP problem, its coding sequence is made up of job's number with the length of $n \times m$, the sequence shows the order of jobs be processed on the machine and a job's sequence is represented by its job's number. For an encoding sequence [2 11132233 3], where 1, 2, 3 represents the job's number of job $J_{1}, J_{2}, J_{3}$, and the order represents the operation would be processed on the given machine. The encoding sequence is described as $\left[\begin{array}{llllllllll}\sigma_{21}, & \sigma_{11}, & \sigma_{12}, & \sigma_{13}, & \sigma_{31}, & \sigma_{22}, & \sigma_{23}, & \sigma_{32}, & \sigma_{33}\end{array}\right]$, where $\sigma_{i j}$ presents the $j$ operation of the job $i$.

NS-HDE/EDA is a continuous space algorithm, while JSSP's solution space is discrete. Thus, to reasonably map continuous space to discrete space, the sequence mapping is adopted. A detailed three-job three-machine JSSP example is used to illustrate this procedure. The three-job three-machine JSSP includes three jobs $\left(J_{1}, J_{2}, J_{3}\right)$ and three machines $\left(M_{1}, M_{2}, M_{3}\right)$. Since each job must go through each machine and each machine has three jobs, it has 9 ! possible ways for this type of JSSP to complete all jobs according to the encoding method. The encoding individual must cover all possible ways. As we must cover 9 ! possible ways, nine random numbers are generated in interval $[0,1]$ as an individual. Suppose that a feasible individual in the continuous space is $[0.965,0.517,0.971,0.957,0.485,0.800,0.142,0.422$, 0.916], as shown in sequence 1 in the Figure 1. The numbers in sequence 1 are sorted from small to large and their position index will be recorded. This feasible individual can be encoded to an integer series $[7,2,8,5,6,9,4,1,3]$ as sequence 2 according to their position index. Then according to their values in the integer series, each number in it will be brought into the equation $\pi_{d}^{\prime}=\left\lceil\phi_{d}^{\prime} / m\right\rceil, \phi_{d}^{\prime}$ is the number in the sequence 2 and $\lceil\bullet\rceil$ is round up to an integer. So it can be transformed to integer series $[3,1,3,2,2,3,2,1,1]$, as shown in sequence 3 . The sequence 3 is corresponding to an operation sequence 4 .

Through scanning the encoding sequence from left to right, a schedule plan can be obtained by decoding. The operation should be shifted to left as compact as possible to decrease the idle time. Since superfluous idle time can be inserted between operations, an encoding sequence can be decoded into an infinite number of schedules. Therefore, active schedule is adopted in this paper, which has been verified and denoted that it contains optimal schedule in a Venn diagram (Pinedo 2008). Meanwhile, only the active schedule is considered in the decoding approach to reduce the search space.

### 3.3 Estimation of distribution algorithm

EDA employs explicitly probability distribution in optimisation. EDA emphasises the global exploration and has fast convergence rate, but its local exploitation ability is relatively limited. Therefore, the global exploration ability of EDA is employed in this paper. In EDA, Gaussian distribution is selected as probability model, and the incremental learning method as its updating way. Gaussian distribution builds a probability model by calculating the mean and standard deviation of the population, which reflects the feature of population. The incremental learning method utilises a part of special individuals to update the mean and standard deviation, which enhances the exploitation ability of EDA so that the population is not quickly trapped into local optima. In our EDA, we choose truncation selection method (Heinz and Dirk 1993) to select special individuals. In the truncation selection method, the candidate solutions are ordered by fitness, and some proportion, $p$, (e.g. $p=1 / 2,1 / 3$, etc.), of the fittest individuals are selected and reproduced $1 / p$ times, then a large population will produced, whose size is great than the original population. The new population will be selected from the above large population randomly; the individuals in this new population are special individuals. To further explain this procedure in detail, we give an example in Figure 2. The procedure of EDA is illustrated as follows:
![img-0.jpeg](img-0.jpeg)

Figure 1. An example of the encoding process.

![img-1.jpeg](img-1.jpeg)

Figure 2. The procedure of truncation selection method.

# Algorithm 1. (EDA) 

Step 0. Initialisation.
Step 0.1. Randomly initialize the population $\boldsymbol{X}_{0}$ of size NP.
Step 0.2. Set $t=0$, where $t$ is the current generation.
Step 1. Compute the mean $\mu_{j}$ and standard deviation $\sigma_{j}$ of the current population $\boldsymbol{X}_{i}$ with Equation (1).

$$
\mu_{j}=\frac{\sum_{i=1}^{N P} x_{i j}}{N P}, \quad \sigma_{j}=\sqrt{\frac{\sum_{i=1}^{N P}\left(x_{i j}-\mu_{j}\right)^{2}}{N P}}
$$

where, $i=1,2, \ldots, \mathrm{NP}, j=1,2, \ldots, D, D$ is the number of dimension, NP is the population size and $\boldsymbol{x}_{\boldsymbol{i}}=\left(\boldsymbol{x}_{\boldsymbol{i} \boldsymbol{I}}, \boldsymbol{x}_{\boldsymbol{i} 2}, \ldots, \boldsymbol{x}_{\boldsymbol{i} j}, \ldots \boldsymbol{x}_{\boldsymbol{i} \boldsymbol{D}}\right)$ is the $i$ th individual.
Step 2. Use truncation selection method to select a promising population from the current population to compute standard deviation $\sigma_{j}^{k}$ with Equation (2).

$$
\sigma_{j}^{k}=\sqrt{\frac{\sum_{i=1}^{k}\left(x_{i j}-\mu_{j}\right)^{2}}{N P}}
$$

where $k$ is the number of selection population, $k=\lfloor\eta \times \mathrm{NP}\rfloor, \eta$ is the selection probability, $\lfloor\bullet\rfloor$ is rounded down.
Step 3. Update $\mu_{j}$ and $\sigma_{j}$ with the incremental learning method with Equation (3) and Equation (4), respectively.

$$
\begin{gathered}
\mu_{j}=(1-\alpha) \mu_{j}+\alpha\left(x_{\text {best } 1, j}+x_{\text {best } 2, j}-x_{\text {worst }, j}\right) \\
\sigma_{j}=(1-\alpha) \sigma_{j}+\alpha \sigma_{j}^{k}
\end{gathered}
$$

where $x_{\text {best1 }}, x_{\text {best2 }}, x_{\text {worst }}$ is the best, the second best and worst individual in the current population, $\alpha$ is the learning rate.
Step 4. Build the probability distribution model $P(\boldsymbol{x})$ with Equation (5).

$$
P(\boldsymbol{x})=\prod_{j=1}^{D} f_{N}\left(x_{j} ; \mu_{j} ; \sigma_{j}\right)=\prod_{j=1}^{D} \frac{1}{\sqrt{2 \pi \sigma_{j}}} e^{\frac{1}{2}\left(\frac{x_{j}-\mu_{j}}{\sigma_{j}}\right)^{2}}
$$

where $\boldsymbol{x}=\left(\boldsymbol{x}_{\boldsymbol{I}}, \boldsymbol{x}_{\boldsymbol{2}}, \ldots, \boldsymbol{x}_{\boldsymbol{j}}, \ldots \boldsymbol{x}_{\boldsymbol{D}}\right)$ is a single individual, $j=1,2, \ldots, D, D$ is the number of dimension and $N$ is the normal distribution or Gaussian distribution.
Step 5. Sample the new population $\boldsymbol{X}_{t+1}$ by the probabilistic model $P(\boldsymbol{x})$.
Step 6. Set $t=t+1$.
Step 7. If termination condition is not met, go to Step 1 ; otherwise end EDA.
In the above EDA, $\mu_{j}$ and $\sigma_{j}$ are the parameters of the model. $\mu_{j}$ restricts centre of the population. $\sigma_{j}$ controls the diversity of the population and the convergence rate. EDA controls the exploration-exploitation trade-off by the strategies of Equations (3) and (4). The single parent does not jump directly to a desirable location, but rather makes a very small step towards this desirable location. The population will maintain a long-term memory which can provide tiny decision information to the later period of evolution.

# 3.4 Differential evolution algorithm 

DE algorithm (Das and Suganthan 2011) is an evolutionary algorithm based on vector. DE adopts the similar concept of jump in NS by adding weighted vectors to the target vector to control the evolutionary variation. Therefore, DE has strong exploitation ability and can generate the local information. We select DE as another sub algorithm. In DE algorithm, there are two important parameters that are the scale factor $F$ and the crossover rate $C R . F$ decides the scaling of the differential vector produced by differential mutation. It has important influence on the performance of the algorithm, which includes convergence speed and population diversity. $C R$ affects the diversity of population for the next generation. On the one side, if the value of $C R$ becomes larger and larger, the performance of local search ability and the convergence rate tend to become better and better. On the other hand, the smaller value of $C R$ leads to the better performance on maintaining the population diversity and enhancing global search ability. In order to further accelerate the convergence rate and strengthen the search ability of DE, a chaotic strategy named CPC (Wang, Li, and Lai 2009) is introduced. $F$ and $C R$ are updated by Equations (6) and (7), so that $F$ and $C R$ values spread between $[0,1]$ in the whole region throughout the search process.

At present, there are many versions for DE's mutation operator, which can be expressed by $\mathrm{DE} / x / y / z$ (Storn and Price 1997). $x$ describes the base vector selection type which includes rand, current, best and so on; rand means a randomly chosen population vector; current means the base vector comes from the current individual; best means the vector of lowest cost from the current population; $y$ represents the number of differentials, which is an integer; $z$ is the type of crossover operator, which includes bin and exp; bin means a binomial distribution for recombination; exp means the exponential distribution for recombination. In our DE algorithm, we selected two classical mutation operators which are shown in Equation (9) DE/rand/1 (Das and Suganthan 2011) and Equation (10) DE/current-to-best/1 (Bai et al. 2012). $\mathrm{DE} /$ rand/1 can effectively maintain the diversity of the population. $\mathrm{DE} /$ current-to-best/1 is used to accelerate the convergence rate. Here, a binomial distribution is selected by crossover operator, so the type of crossover operator is bin. The differential decisive factor $\gamma$ is utilised to adjust the proportion of two mutation operators. Such updating way aims at restricting the mutation rate appropriately. The procedure of DE is displayed as follows.

## Algorithm 2. (DE):

Step 0. Initialization.
Step 0.1. Randomly initialise the population $\boldsymbol{X}_{0}$ of size NP.
Step 0.2. Set $t=0$, where $t$ is the current generation.
Step 0.3. Initialize $C R_{0}$ and $\gamma_{0}$.
Step 1. Update parameters.
Step 1.1. Update the scale factor $F$.

$$
F_{t+1}=4 \times C R_{t} \times\left(1-C R_{t}\right)
$$

Step 1.2. Update the crossover rate $C R$.

$$
C R_{t+1}=4 \times F_{t+1} \times\left(1-F_{t+1}\right)
$$

Step 1.3. Update the differential decisive factor $\gamma$.

$$
\gamma_{t+1}=4 \times \gamma_{t} \times\left(1-\gamma_{t}\right)
$$

for $i=1: \mathrm{NP}$
Step 2. Mutation. If rand $>\frac{\gamma_{t+1}}{4}$,

$$
v_{t}^{\prime}=x_{r_{1}}^{\prime}+F_{t+1} \times\left(x_{r_{2}}^{\prime}-x_{r_{3}}^{\prime}\right)
$$

else

$$
v_{t}^{\prime}=\left(F_{t+1}+0.5\right) \times x_{d}^{\prime}+\left(F_{t+1}-0.5\right) \times x_{t}^{\prime}+F_{t+1} \times\left(x_{b}^{\prime}-x_{c}^{\prime}\right)
$$

end
where $x_{r_{1}}^{\prime}, x_{r_{2}}^{\prime}, x_{r_{3}}^{\prime}$ are randomly selected from the current population and $r_{1} \neq r_{2} \neq r_{3} \neq i . x_{d}^{\prime}$ is the best solution of the current population, $\left(x_{b}^{\prime}-x_{c}^{\prime}\right)$ is a random differential vector with $b \neq c$.
Step 3. Crossover.

$$
u_{i j}^{\prime}= \begin{cases}v_{i j}^{\prime}, & \text { if } r \text { and }<\mathrm{CR}_{t+1} \\ x_{i j}^{\prime}, & \text { otherwise }\end{cases}
$$

where $\boldsymbol{x}_{i}^{\boldsymbol{t}}=\left\{\boldsymbol{x}_{i \boldsymbol{t}}, \boldsymbol{x}_{i \boldsymbol{Z}}, \ldots, \boldsymbol{x}_{i \boldsymbol{j}}, \ldots, \boldsymbol{x}_{i \boldsymbol{D}}\right\}$ is the $i$ th individual of the current population, $D$ is the number of dimension, $\boldsymbol{u}_{i}^{\boldsymbol{t}}=\left\{\boldsymbol{u}_{a}^{\boldsymbol{t}}, \boldsymbol{u}_{a}^{\boldsymbol{t}}, \ldots, \boldsymbol{u}_{g}^{\boldsymbol{t}}, \ldots, \boldsymbol{u}_{m}^{\boldsymbol{t}}\right\}$ is the crossover individual, $\boldsymbol{v}_{i}^{\boldsymbol{t}}=\left\{\boldsymbol{v}_{a}^{\boldsymbol{t}}, \boldsymbol{v}_{a}^{\boldsymbol{t}}, \ldots, \boldsymbol{v}_{g}^{\boldsymbol{t}}, \ldots, \boldsymbol{v}_{m}^{\boldsymbol{t}}\right\}$ is the $i$ th mutation individual.
Step 4. Selection.

$$
\boldsymbol{x}_{i}^{t+1}= \begin{cases}\boldsymbol{u}_{i}^{t}, & \text { if } f\left(\boldsymbol{u}_{i}^{t}\right)<f\left(\boldsymbol{x}_{i}^{t}\right) \\ \boldsymbol{x}_{i}^{t}, & \text { otherwise }\end{cases}
$$

where $f(\boldsymbol{\bullet})$ is the fitness value.
end for
Step 5. If termination condition is not met, let $t=t+1$, go to Step 1; otherwise end DE.

# 3.5 The decisive factor 

EDA employs probability distribution to build model, which takes full use of global information to generate offspring and has excellent convergence rate. But poor exploitation ability makes EDA be easily trapped in local optima. DE can use the differential information between vectors (individuals) to jump the local optima and has strong exploitation ability but with low convergence rate. Therefore, EDA and DE are combined by the decisive factor $\zeta$ in this paper. The merits of the above two algorithms are taken for full use. The proposed algorithm balances global exploration and local exploitation.

Through the decisive factor $\zeta$, most of individuals in the population are generated by EDA in the initial evolution. EDA forces the search region to quickly approach a promising area as close as possibly. The minority individuals are generated by DE for maintaining the diversity of the population. These strategies provide the promising area for the later evolution. In the later of evolution, most of individuals in population are generated by DE with the decisive factor $\zeta$ in order to ensure exact search. Nevertheless, as the poor global exploration of DE, EDA generates a little of individuals to maintain the global information and increases their search accuracy. Thus, $\zeta$ is adjusted with Equation (13). When $\zeta$ is larger, EDA plays a leading role. Then $\zeta$ will be gradually lowered in the process of evolution so that DE can occupy dominant position.

$$
\zeta_{t}=e^{-\frac{t}{G_{\max }}}
$$

where $t$ is the current iteration, $G_{\max }$ is the maximum value of iteration.
Figure 3 shows that $\zeta$ becomes smaller with increasing evolutionary iteration, and the probability of EDA becomes smaller, while DE becomes larger. Since the population is large, the way of generating individuals by the probability can make the proportion of each algorithm be well in line with statistical regularity. Thus, the proposed algorithm can resist randomness and the search results are more stable.
![img-2.jpeg](img-2.jpeg)

Figure 3. The curve of the decisive factor.

# 3.6 Local search procedure 

JSSP is a combinatorial optimisation problem and its solution space is limited. But EDA and DE are all continuous algorithms in this paper. According to the encoding scheme, there is a one-to-many relationship between them. So it is insufficient for search ability to simply depend on the hybrid EDA and DE algorithm to solve JSSP. Continuous algorithms do not meticulously search the solution space and one-to-many relationship causes many repeated searching. It consumed a great deal of computational time. Therefore, to reduce the computational time and improve the solution quality, a local search method named a NS based on blocks on critical path is proposed, which is applied to the solutions achieved by the hybrid EDA and DE algorithm. The features of this proposed local search method are discussed in the following subsection.

### 3.6.1 Defining neighbourhood

It is important for the efficiency and the search quality of the algorithm to select the proper neighbourhood structures. Since the neighbourhood based on the block structure of critical path can avoid unnecessary operations and effectively enhance the performance of the algorithms, it is adopted. The disjunctive graph is employed to describe JSSP to illustrate the neighbourhood structures. A brief example of JSSP is introduced, which is shown in Table 1. Figure 4 presents the model of the disjunctive graph of Table 1. The real arcs to precedence relations, the dashed arcs to pairs of operations performed on the same machine.

For a directed disjunctive graph describing feasible schedule, a key component of it is the critical path, which is the longest path from start 0 to end * and its length represents the makespan. The operations on the critical path are called critical operations, which has important influence on the makespan. Once the start of the critical operation is delayed, the makespan inevitably is also delayed. In Figure 5, the length of the critical path is 15 and the critical path is $0 \rightarrow o_{31} \rightarrow o_{21} \rightarrow o_{22} \rightarrow o_{23} \rightarrow o_{13} \rightarrow *$. A maximal sequence of adjacent critical operations that is processed on the same machine is called a critical block. In Figure 4, the critical operations are $\left\{o_{31}, o_{21}, o_{22}, o_{23}, o_{13}\right\}$, which include two critical blocks $\left\{o_{23}, o_{13}\right\},\left\{o_{31}, o_{21}\right\}$.

Since the makespan of a schedule is impossibly less than the length of its critical path, only several critical operations are moved to improve the makespan. The neighbourhood structures based on blocks on critical path are adopted, which includes two neighbourhood structures swap and insert process. As following detailed:

## Neighbourhood 1: $\boldsymbol{x}=\operatorname{swap}(\boldsymbol{x})$

Step 1. Convert the individual $\boldsymbol{x}$ to the sequence $\boldsymbol{\pi}$ according to the encoding scheme.
Step 2. Find the critical path and the critical block Block $=\left\{\right.$ Block $_{1}$, Block $_{2}, \ldots$, Block $_{j}\}$ of $\boldsymbol{\pi}$, where $j$ is the number of block, $i=1$.
Step 3. Swap the two operations $o_{n}$ and $o_{m}$ in Block ${ }_{i}$ to generate a new sequence $\boldsymbol{\pi}^{\prime}$.
Step 4. If $f\left(\boldsymbol{\pi}^{\prime}\right)<f(\boldsymbol{\pi}), \boldsymbol{\pi}_{\text {best }}=\boldsymbol{\pi}^{\prime}$, where $f(\bullet)$ is the function of calculating makespan.
Step 5. Convert $\boldsymbol{\pi}_{\text {best }}$ to $\boldsymbol{x}_{\text {best }}$. Go back to Step 3, until complete all operation pairs in Block ${ }_{i}$, and then go to Step 6.
Step 6. If $i<j, i=i+1$, go back to step 3 , otherwise, $\boldsymbol{x}=\boldsymbol{x}_{\text {best }}$, return.
Neighbourhood 2: $\boldsymbol{x}=$ insert $(\boldsymbol{x})$
Step 1. Convert the individual $\boldsymbol{x}$ to the sequence $\boldsymbol{\pi}$ according to the encoding scheme.
Step 2. Find the critical path and the critical block Block $=\left\{\right.$ Block $_{1}$, Block $_{2}, \ldots$, Block $_{j}\}$ of $\boldsymbol{\pi}$, where $j$ is the number of block. $i=1$.
Step 3. Insert the operation $o_{n}$ into the front of the operation $o_{m}$ in Block $_{i}$ to generate a new sequence $\boldsymbol{\pi}^{\prime}$.
Step 4. If $f\left(\boldsymbol{\pi}^{\prime}\right)<f(\boldsymbol{\pi}), \boldsymbol{\pi}_{\text {best }}=\boldsymbol{\pi}^{\prime}$, where $f(\bullet)$ is the function of makespan.
Step 5. Convert $\boldsymbol{\pi}_{\text {best }}$ to $\boldsymbol{x}_{\text {best }}$. Go back to Step 3, go back to Step 3, until the all operation in Block ${ }_{i}$ are inserted all other possible positions in Block ${ }_{i}$, and then go to Step 6.
Step 6. If $i<j, i=i+1$, go back to Step 3. Otherwise, $\boldsymbol{x}=\boldsymbol{x}_{\text {best }}$, return.

Table 1. $3 \times 3$ JSSP problem.
![img-6.jpeg](img-6.jpeg)

Figure 4. The model of the disjunctive graph in Table 1.
![img-4.jpeg](img-4.jpeg)

Figure 5. The directed disjunctive graph of the feasible schedule.

Encoding scheme is the mapping from continuous domain to discrete domain, but the above two neighbourhood structures directly handle the operations. Therefore, when the order of the operations is changed, the relevant positions of the individual are also changed to make the individual correspond to the encoding sequence. An example of Table 1 is used to illustrate these processes. The detailed processes are displayed in Figure 6, we suppose the swapped operations are $o_{31}$ and $o_{21}$. In inserting operation, $o_{31}$ is inserted before $o_{21}$.

Sequence 1

Sequence 2

Sequence 3

Sequence 4

Sequence 1
![img-5.jpeg](img-5.jpeg)

Sequence 2

Sequence 3

Sequence 4

Sequence 1
![img-6.jpeg](img-6.jpeg)



(b) Insertion operation

Figure 6. Swapping and insertion operation scheme.

# 3.6.2 Local search procedure 

The procedure of the local search algorithm is displayed as follows. To not consume a significant amount of time on local search, the local search algorithm is applied to the best individual of the current population.

## Algorithm 3. (NS):

Step 1. Input the individual $\boldsymbol{x}$.
Step 2. Using the Neighbourhood 1 to search, $\boldsymbol{x}^{\prime}=\operatorname{swap}(\boldsymbol{x})$.
Step 3. Using the Neighbourhood 2 to search, $\boldsymbol{x}^{\prime \prime}=\operatorname{insert}\left(\boldsymbol{x}^{\prime}\right)$.
Step 4. $\boldsymbol{x}=\boldsymbol{x}^{\prime \prime}$, terminate, return $\boldsymbol{x}$.

### 3.7 The procedure of NS-HDE/EDA

Based on the above of encoding scheme, EDA, DE and local search strategy, a NS-HDE/EDA is proposed to solve JSSP. The procedure of NS-HDE/EDA is described as follows:
Algorithm 4. (NS-HDE/EDA):
Step 1. Initialization:
Step 1.0. Randomly generate the initial population $\boldsymbol{X}_{0}$.
Step 1.1. Initialise the learning rate $\alpha, C R_{0}=0.3$ and $\gamma_{0}=0.2$, then let $t=0$. Step 1.3 evaluate the fitness value of each individual in $\boldsymbol{X}_{0}$.
Step 2. Evaluate the fitness value of each individual in $\boldsymbol{X}_{0}$.
Step 3. Conduct the probabilistic mode $P_{i}(\boldsymbol{x})$.
for $i=1: \mathrm{NP}$
Step 4. Generate the new population $\boldsymbol{X}_{t}^{\prime}(\boldsymbol{i})$.
Step 4.0. Generate a random number rand in interval $[0,1]$.
Step 4.1. if rand $<\zeta$,
Generate the new candidate $\mathrm{X}_{t}^{\prime}(i)$ by sampling the probabilistic model $P_{i}$. else

Update $F_{t}, C R_{t}$, with $\gamma_{t}$ Equations (6-8).
Generate the new candidate $\boldsymbol{X}_{t}^{\prime}(\boldsymbol{i})$ by DE operators which include mutation and crossover. end
Step 5. Evaluate fitness value: Evaluate the fitness value of the individual $\boldsymbol{X}_{t}^{\prime}(\boldsymbol{i})$.
Step 6. Selection.

$$
X_{t+1}(i)= \begin{cases}\boldsymbol{X}_{t}(i), & \text { if } f\left(\boldsymbol{X}_{t}(i)\right)<f\left(\boldsymbol{X}_{t}^{\prime}(i)\right) \\ \boldsymbol{X}_{t}^{\prime}(i) & \text { otherwise }\end{cases}
$$

where $f(\cdot)$ is the function of calculating makespan.
end
Step 7. Local search: use Algorithm 3 to search the all best individuals in population $X_{t+1}$.
Step 8. If the stop criterion is satisfied, then stop. Otherwise, let $t=t+1$, and turn to Step 3.
In above procedure, stop criterion includes: (1) the number of generations equals the maximum number of generations; (2) the makespan gets the known lower bound.

## 4. Computational results and comparisons

In order to verify the good performance of NS-HDE/EDA algorithm for JSSP, We consider 123 JSSP benchmarks instances from OR-Library (Beasley 1990). These instances include three classes:
(1) FT06, FT10, FT20 $(n \times m=6 \times 6,10 \times 10,20 \times 5)$ were designed by Fisher and Thompson (1963).
(2) The instance LA01-LA40 $(n \times m=10 \times 5,15 \times 5,20 \times 5,10 \times 10,15 \times 10,20 \times 10,30 \times 10,15 \times 15)$ were designed by Lawrence (1984).
(3) Forty instances of eight different sizes $(n \times m=15 \times 15,20 \times 15,20 \times 20,30 \times 15,30 \times 20,50 \times 15$, $50 \times 20,100 \times 20)$ denoted by (TA) due to Taillard (1993).

The experimental environment includes: MATLAB2010b; Windows 7; Intel Core i5-2450M 2.50 GHz (CPU), 2G RAM.

# 4.1 Parameters analysis 

The parameter settings have significant influence on the performance of the NS-HDE/EDA. NS-HDE/EDA contains some critical parameters: the population size NP, the maximum iteration Maxgens, the learning rate $\alpha$ and the selection probability $\eta$. To investigate the influence of these parameters on the performance of the NS-HDE/EDA, we implement the Taguchi (Montgomery 2008) method of design for the experiment to analyse the parametric sensitivity. FT10 is selected as the benchmark test cases. The various values of NP, Maxgens, $\alpha$ and $\eta$ are listed in Table 2. Table 3 lists the parameter combinations and the obtained average response variable (ARV) values which is the average makespan value obtained by the NS-HDE/EDA. Table 4 lists each parameter's significance rank according to Table 3. In Figure 7, the trend of each parameter for different value is described.

It is observed from Table 4 that NP is the most significant one among them, which illustrated that NP is crucial to the NS-HDE/EDA. The large population can help the EDA to build accurate model. But a large population size will cause an oversize computational budget. Moreover, $\alpha$ ranks the second, which implies it is also an important factor for NS-HDE/ EDA. A small value of $\alpha$ could lead to premature convergence. A large value of $\alpha$ could lead to low convergence rate. From Figure 7, it can be seen that the trend of Maxgens and $\eta$ is relatively flat, which expresses their settings slightly impact on the NS-HDE/EDA. According to the above analysis, the parameters in NS-HDE/EDA are set as follows:

- For all FT instances, LA01-LA15, NP $=20$ and $\alpha=0.05$.
- LA16-LA30, NP $=20$ and $\alpha=0.1$.
- LA31-LA35, NP $=10$ and $\alpha=0.05$.
- LA36-LA40, and all TA instances, NP $=15$ and $\alpha=0.05$.
- $\eta=0.4$, Maxgens $=10,000$.

For FT and LA instances, we run the NS-HDE/EDA 20 times independently. TA is run 10 times.

### 4.2 Results and comparison with other algorithms

Firstly, Relative Error (RE) is defined as follows:

$$
\mathrm{RE}=100 \times(\text { Value }-\mathrm{BKS}) / \mathrm{BKS}
$$

where BKS is the best-known solution or the best-known upper bound (UB), value is the best solution or the mean solution found by NS-HDE/EDA.

Table 5 gives the computational results obtained by NS-HDE/EDA and the comparison with some algorithms reported in literature (Adams, Balas, and Zawack 1988; Della Croce, Tadei, and Volta 1995; Dorndorf and Pesch 1995; Sabuncuoglu and Bayiz 1999; Coello, Rivera, and Cortés 2003; Ombuki and Ventresca 2004; Sha and Hsu 2006; Hasan et al. 2009; He et al. 2010; Pan et al. 2010). The boldface represents that the better solutions obtain the best known. NS-HDE/EDA can find the best-known solution with 22 instances. For the small instance FT06 and LA01-LA15, almost all algorithms can find the best-known solution. LA31-LA35 can be achieved the best-known solution by NS-HDE/ EDA. It also can be seen that the results of NS-HDE/EDA are better than EDA, DDE and $\mathrm{DDE}_{1}$. It shows that the combination of EDA and DE are effective.

Table 6 shows the number of instances solved (NIS) and the RE of all compared algorithms. Meanwhile, the reduction of RE obtained by NS-HDE/EDA with respect to other algorithms is also presented in the last column. We know that the RE of NS-HDE/EDA is only on average $0.8 \%$. So the proposed algorithm yields a significant improvement in solution quality with respect to all other algorithms.

We also compare the NS-HDE/EDA with DDE, EDA and PSO-priority on the convergence rate. Figure 8 describes the evolutionary curves of the instance FT06, FT10, LA01 and LA20. It can be observed that the convergence rate of

Table 2. The various values of the parameters in NS-HDE/EDA.
Table 3. Parameter combinations and ARV values.
Table 4. Parameter rank and response values.

![img-7.jpeg](img-7.jpeg)

Figure 7. The trend of parameters of the NS-HDE/EDA.

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

Table 6. Average relative deviation to the BKS.

NS-HDE/EDA is much better than other algorithms. The global exploration ability of the EDA in NS-HDE/EDA plays a key role, which effectively helps to improve the convergence rate.

For TA problems, we implemented two classical algorithms which are genetic algorithm (GA) and PSO as the compared objects. We implemented a simple GA for solving JSSP. Each individual is represented by a real chromosome, which is encoded by the operation-based representation method. We use POX crossover and INV mutation as reproduction operators. The population size is set to 30 . Then, we implemented a PSO, which is come from reference Lin et al. (2010).

The computational results obtained by NS-HDE/EDA, PSO and GA are summarised in Table 7. The computational results include RE of the best solution (BRE), RE of the average solution (ARE), RE of the worst solution (WRE), the
![img-10.jpeg](img-10.jpeg)

Figure 8. The evolutionary curves for JSSP.

![img-11.jpeg](img-11.jpeg)

average standard deviation of the makspan (ASD) and the average computational time ( $T_{a v}(\mathrm{~s})$ ). The best one for each scale has been marked with boldface. It can be found that, the results obtained by the proposed algorithm are better than the two classical algorithms. The mean ARE value obtained by NS-HDE/EDA is $6.28 \%$ which is lower than the previously obtained results of $17.43 \%$ from PSO and $15.38 \%$ from GA. The graphical representation in Figure 9 shows the BRE values of NS-HDE/EDA, PSO and GA for each TA instance. The BRE values of NS-HDE/EDA are lower than other two algorithms, namely, the best solution of the proposed algorithm is close to the best-known solution which have found at present. Although NS-HDE/EDA does not obtain the best-known solutions at present generations for large problems, the evolutionary trend of the population does not stagnate. That is to say NS-HDE/EDA can further be optimised to obtain the better solutions. The WRE values obtained by NS-HDE/EDA are better than BRE values of PSO and GA. It can be concluded that NS-HDE/EDA is more effective than the compared algorithm. Additionally, the ASD obtained by NS-HDE/EDA is lower than that of obtained with PSO and GA. It demonstrates that the strong robustness of the proposed algorithms. Therefore, NS-HDE/EDA can achieve a good trade-off between global search and local search and is very suitable for JSSP. In particular, the best makespan, the average makespan and the average computational time of each TA instance obtained by NS-HDE/EDA, PSO and GA has been listed in Table A1 of Appendix 1.

By compared with the computational time of the three algorithms in Figure 10, we see that PSO and GA consume comparable amount of time while NS-HDE/EDA requires apparently more time to run. Meanwhile, Table 7 also lists the average CPU time of fixed generations for each scale with three compared algorithms. With increase of problem
![img-12.jpeg](img-12.jpeg)

Figure 9. The RE of NS-HDE/EDA, PSO and GA for TA instance.
![img-13.jpeg](img-13.jpeg)

Figure 10. A comparison of computational time for TA instance.

size, NS-HDE/EDA will consume more time. Due to the fact that, in NS-HDE/EDA, there is about $50 \%$ computation time spent on local search process. Compared with classical GA and PSO, the NS effectively improves the quality of the solution, but it also takes too much computation time.

# 5. Conclusions 

In this paper, we first review recent studies on the JSSP of minimising makespan. Then, a novel hybrid optimisation algorithm, NS-HDE/EDA, was proposed for solving the JSSP with minimisation of makespan as the objective. In NS$\mathrm{HDE} / \mathrm{EDA}$, EDA is integrated with DE by the proposed decisive factor to improve the searching efficiency. Local information and global information are effectively incorporated together. The CPC strategy is introduced to DE to strengthen its search ability. Meanwhile, a local search algorithm, NS, is designed to further search the solutions to improve the quality of the solutions.

The parametric sensitivity of the proposed algorithm was analysed based on the Taguchi method of design of experiment. The proposed algorithm was tested on 123 classical benchmark problems. The computational results and comparisons show that our presented NS-HDE/EDA algorithm is better than the reported approaches in terms of solution quality. However, the performance of the proposed algorithm on the large-scale JSSP was not ideal, especially TA scheduling problems, the obtained results of NS-HDE/EDA algorithm show large gap with the best-known solutions which have found.

Our future researches will include the following topics: First, we will improve the performance of NS-HDE/EDA algorithm and verify its efficiency on large-scale scheduling problem. Second, applying improved NS-HDE/EDA to other kinds of combination optimisation problems may also be a promising direction. Third, due to the consumption of large time in local search, developing novel and effective neighbourhood structures in the local search is meaningful and challenging.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## Funding

This work was financially supported by the National Natural Science Foundation of China [grant number 51365030]. It was also supported by the General and Special Program of the Postdoctoral Science Foundation of China [grant number 2012M521802], [grant number 2013T60889]; the Science Foundation for Distinguished Youth Scholars of Lanzhou University of Technology [grant number J201405]; Lanzhou Science Bureau project [grant number 2013-4-64].

# Appendix 1. 

Table A1. Results using NS-HDE/EDA, PSO, GA for TA instance.
Table A1. (Continued).