# Estimation of distribution algorithm with path relinking for the blocking flow-shop scheduling problem 

Zhongshi Shao ${ }^{\mathrm{a}}$, Dechang $\mathrm{Pi}^{\mathrm{a}, \mathrm{b}}$ and Weishi Shao ${ }^{\mathrm{a}}$<br>${ }^{a}$ College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing, PR China; ${ }^{\text {b }}$ Collaborative Innovation Center of Novel Software Technology and Industrialization, Nanjing, PR China


#### Abstract

This article presents an effective estimation of distribution algorithm, named P-EDA, to solve the blocking flow-shop scheduling problem (BFSP) with the makespan criterion. In the P-EDA, a Nawaz-Enscore-Ham (NEH)based heuristic and the random method are combined to generate the initial population. Based on several superior individuals provided by a modified linear rank selection, a probabilistic model is constructed to describe the probabilistic distribution of the promising solution space. The path relinking technique is incorporated into EDA to avoid blindness of the search and improve the convergence property. A modified referenced local search is designed to enhance the local exploitation. Moreover, a diversitymaintaining scheme is introduced into EDA to avoid deterioration of the population. Finally, the parameters of the proposed P-EDA are calibrated using a design of experiments approach. Simulation results and comparisons with some well-performing algorithms demonstrate the effectiveness of the P-EDA for solving BFSP.


## ARTICLE HISTORY

Received 15 November 2016 Accepted 22 June 2017

## KEYWORDS

Flow-shop scheduling with blocking; estimation of distribution algorithm; path relinking; makespan

## 1. Introduction

The traditional permutation flow-shop scheduling problem (PFSP) with infinite buffer capacity has been extensively investigated over the past 60 years (Vallada and Ruiz 2010; Shao and Pi 2016; Wang et al. 2017). However, in practice, owing to technological requirements or process characteristics, the buffer capacity between two consecutive machines may be totally absent. The traditional PFSP becomes the blocking flow-shop scheduling problem (BFSP) (Ronconi and Henriques 2009). In such cases, the job has to be blocked on its machine until its next machine is free (Ribas, Companys, and Tort-Martorell 2011; Han, Gong, Jin, et al. 2016). Many modern production systems can be modelled as BFSPs when no buffers exist between consecutive machines, such as in the iron and steel industry (Gong, Tang, and Duin 2010), serial manufacturing processes (Koren, Wang, and Gu 2017), robotic cells (Ribas, Companys, and Tort-Martorell 2015) and the chemical industry (Merchan and Maravelias 2016). Hence, it is necessary to develop effective and efficient approaches for such problems.

BFSP with the makespan criterion is a typical NP-hard problem when the number of machines is larger than two (Hall and Sriskandarajah 1996). With increasing problem size, the BFSP becomes more and more complicated and is difficult to solve completely. Therefore, to tackle this challenge, many constructive heuristics, such as profile fitting (PF), Nawaz-Enscore-Ham (NEH) and MinMax

[^0]
[^0]:    CONTACT Dechang Pi nuaacs@126.com
    (C) Supplemental data for this article can be accessed at https://doi.org/10.1080/0305215X.2017.1353090

(MM), which use some specific rules to assign a priority index to each job to construct a scheduling permutation, were proposed. Moreover, Ronconi (2004) presented two constructive heuristics, i.e. MME and PFE, which combined NEH with PF and MM, respectively. The author showed that the performances of both MME and PFE outperformed the NEH heuristic over the instances with 500 jobs and 20 machines. Companys, Ribas, and Mateo (2010) improved the NEH heuristic by using several different priority rules and tie-breaking strategies. Wang et al. (2012) proposed a modified NEH heuristic based on the average value and standard deviation of the processing time. Pan and Wang (2012) introduced the concept of weight value into PF and presented two new constructive heuristics, i.e. profile fitting (wPF) and the Pan-Wang (PW) heuristic. They also combined them with NEH and proposed three improved constructive heuristics, namely PF-NEH, wPF-NEH and PWNEH. Wang, Pan, and Tasgetiren (2010) proposed an improved NEH heuristic named NEH_WPT, which sorted jobs in non-decreasing order of the sum of their processing times on all machines.

Some metaheuristics have also been proposed to solve the BFSP with the makespan criterion to obtain better solutions. Wang et al. (2010) proposed a hybrid discrete differential evolution (HDDE) algorithm in which a new mutation and crossover operator were developed. To improve the efficiency of the whole algorithm, the authors also presented a speed-up method to evaluate the insert neighbourhood. Lin and Ying (2013) presented a revised artificial immune system (RAIS) algorithm based on the features of artificial immune systems and the annealing process of simulated annealing algorithms. Pan et al. (2013) proposed a high-performing memetic algorithm (MA). In the MA, a path-relinking-based crossover operator, a referenced local search (RLS) and a procedure for controlling diversity were used. Han, Gong, and Sun (2014) proposed a hybrid algorithm named DE-ABC, which combined the discrete artificial bee colony (ABC) with differential evolution (DE). In DEABC , the mutation and crossover operators of discrete DE were used by the employed bee operator of ABC. Ding et al. (2016) proposed an iterated greedy algorithm based on some new block properties of BFSP. Han et al. (2016) proposed a modified fruit fly optimization (MFFO) algorithm, which employed three key operators, i.e. a problem-specific heuristic, a neighbourhood strategy and a speed-up insert-neighbourhood-based local search. Besides the above metaheuristics, other highperforming metaheuristics have been proposed to solve the problem under consideration. These include two tabu searches (Grabowski and Pempera 2007), a dynamic multi-swarm particle swarm optimization (DMS-PSO) (Liang et al. 2011), an iterated greedy algorithm (IG) (Ribas, Companys, and Tort-Martorell 2011), an improved artificial bee colony (IABC) (Han et al. 2012), a hybrid modified global-best harmony search (hmgHS) (Wang, Pan, and Tasgetiren 2011), a three-phase algorithm (TPA) (Wang et al. 2012), a discrete particle swarm optimization (DPSO) (Wang and Tang 2012), a discrete self-organizing migrating algorithm (DSOMA) (Davendra and Bialic-Davendra 2013) and variable neighbourhood searches (VNSs) (Ribas, Companys, and Tort-Martorell 2013). From the previous research, it can be seen that the superiority of these high-performing approaches can be attributed to an effective constructive heuristic to generate initial solutions with good quality, and the combination of global search and local search strategies to achieve an appropriate balance between exploration and exploitation. However, these approaches have their shortcomings. On the one hand, if the metaheuristics adopt a single individual as the population, such as in IG, TPA and VNS, a great deal of time will be consumed for the quality of solutions to reach a high level. On the other hand, several metaheuristics, such as DMS-PSO, MA, IABC, hmgHS and the genetic algorithm (GA), employ the idea of swarm intelligence to find the global optimum. This mechanism can effectively enrich the search directions by means of multiple individuals, but it takes a lot of effort to evolve the whole population through different evolutionary operators. In particular, the metaheuristics based on swarm intelligence often have poor performance on large-scale discrete optimization problems. Therefore, a well-known metaheuristic called the estimation of distribution algorithm (EDA) is introduced in this article and adapted with some distinctive evolutionary strategies to overcome the above problems.

EDA is a stochastic optimization technique based on statistical learning (Hauschild and Pelikan 2011) which has been developed to solve a variety of optimization problems, such as arc routing problems (Wang et al. 2015), production scheduling (Shao, Pi, and Shao 2017), water distribution

network optimization (Qi, Li, and Potter 2016) and vehicle routing (Pérez-Rodríguez and HernándezAguirre 2016). Unlike GAs, which use mutation and crossover operators to generate new individuals, EDA generates offspring through building and sampling explicit probabilistic models of promising candidate solutions. EDA is good at the automatic discovery and exploration of problem regularities. Until now, only Jarboui et al. (2009) have proposed a hybrid EDA to solve the BFSP with the makespan criterion. In this EDA, a probabilistic model is built based on both the order of the jobs in the sequence and the similar blocks of jobs. However, compared with the state-of-the-art metaheuristics, this EDA is uncompetitive. Moreover, some drawbacks of this EDA have been pointed out by Pan and Ruiz (2012a). Therefore, an effective EDA (named P-EDA) is proposed in this article to solve the BFSP with the makespan criterion. In the proposed algorithm, an NEH-based heuristic and the random method are combined to initialize the population. A modified linear rank selection is used to select the superior individuals from the parental population. An effective probabilistic model is constructed to guide the algorithm to search the promising solution space. To enhance the convergence property of EDA and avoid blindness of the search, the path relinking method is incorporated into EDA. A modified referenced local search (mRLS) based on a random trajectory, a speed-up method and a pruning procedure is used to enhance the exploitation capability of the proposed algorithm. Finally, a diversity-maintaining scheme is adopted to avoid the deterioration of the population.

The contributions of this work can be summarized as follows. (1) The path relinking technique is incorporated into EDA to guide the search process. The advantages of using path relinking were confirmed by the experimental results over the benchmark instances of BFSP. (2) The problem that some elite solutions may not be selected in traditional linear rank selection, owing to randomness of sampling, is solved. (2) The shortcoming of the probabilistic model proposed by Pan and Ruiz (2012a) is improved. (3) An mRLS is proposed to enhance the exploitation ability of the EDA. Its effectiveness and contribution to the proposed algorithm are confirmed by experiments. (4) The performance of the proposed P-EDA is evaluated and compared with other well-performing algorithms. The reported computational results show that the proposed algorithm is superior to all of the compared algorithms.

The rest of this article is organized as follows. Section 2 gives a detailed description of the BFSP with the makespan criterion. Section 3 elaborates on the proposed P-EDA. Section 4 shows the computational evaluation of the algorithms with statistical analyses. Finally, conclusions and suggestions for further research are presented in Section 5.

# 2. Problem description 

The BFSP, denoted as $F m \mid$ blocking $\mid C_{\max }$ according to the notation proposed by Graham et al. (1979), can be briefly described as follows: $n$ jobs have to be processed on $m$ machines. Each job has $m$ operations processed on $m$ machines sequentially in the same order. Each job can be only processed on one machine at a time. Each machine can process one job at a time. There are no intermediate buffers between adjacent machines. This means that upon completion of its operation on one machine, the job cannot leave its machine until the next machine is available for processing it. Pre-emption is not allowed. Each job $j$ has a deterministic positive processing time on every machine $i$. Jobs and machines are usable from time zero. The objective usually considered in $F m \mid$ blocking $\mid C_{\max }$ is to determine a sequence for processing all jobs on all machines so that the maximum completion time (called makespan) is minimized.

Let $\pi=\{\pi(1), \pi(2), \ldots, \pi(k), \ldots, \pi(n)\}$ denote a permutation sequence, in which $\pi(k)$ represents the job at the $k$ th position of $\pi$. Let $p_{\pi(i), k}$ denote the processing time of job $\pi(i)$ on machine $k$. The departure time of job $\pi(k)$ on machine $k$ is denoted as $D_{\pi(j), k}$. According to the literature (Ronconi 2004), $C_{\max }$ can be calculated with the following recursive formulations:

$$
\begin{gathered}
D_{\pi(1), 0}=0 \\
D_{\pi(1), k}=D_{\pi(1), k-1}+p_{\pi(1), k} \quad k=1,2, \ldots, m-1
\end{gathered}
$$

$$
\begin{gathered}
D_{\pi(j), 0}=D_{\pi(j-1), 1} \quad j=2,3, \ldots, n \\
D_{\pi(j), k}=\max \left\{D_{\pi(j), k-1}+p_{\pi(j), k-1}, D_{\pi(j-1), k+1}\right\} \quad j=2,3, \ldots, n \quad k=1,2, \ldots, m-1 \\
D_{\pi(j), m}=D_{\pi(j), m-1}+p_{\pi(j), m} \quad j=1,2, \ldots, n
\end{gathered}
$$

Then, the makespan is $C_{\max }(\pi)=D_{\pi(n), m}$. Therefore, the BFSP with the makespan criterion is to find a permutation sequence for processing the jobs such that $C_{\max }\left(\pi^{*}\right)=\min C_{\max }(\pi), \forall \pi \in \Pi$. To clearly explain the process of calculating makespan, a detailed example is provided in the online supplementary material.

# 3. The proposed P-EDA for the BFSP 

### 3.1. Initialization

In the scheduling literature, it is very common to construct a few good initial individuals by effective constructive heuristics and to produce others randomly (Pan et al. 2014; Karthikeyan et al. 2015). NEH is a famous heuristic with excellent performance, which has been used in many algorithms to produce initial solutions in the traditional PFSP (Shao and Pi 2016). However, the longer total processing time may lead to a higher probability of occurrence of blocking in BFSP (Ding et al. 2016), so that the original NEH may not produce good solutions. Hence, an effective heuristic, i.e. PF-NEH, proposed by Pan and Wang (2012) is used to initialize part of the initial solutions to intensify the quality of the initial population. Meanwhile, other initial solutions are randomly generated in the search space to maintain the diversity of the initial population. In the PF-NEH heuristic, the well-known PF heuristic first determines an initial sequence of all jobs. Then, the NEH enumeration procedure is performed on the last $\lambda$ jobs of this sequence. Following Pan and Wang (2012), the parameter $\lambda$ is set to 25 when the problem is larger than 25 jobs and set to $n$ (the number of jobs) for problems with fewer than 25 jobs. The procedure of initializing the population is described in Algorithm 1.

Algorithm 1: Initialization of population
Step 1: Let $P c$ denote the population. Set $P c=\emptyset$ and initialize $\lambda$ and the population size $P S$.
Step 2: Generate a job sequence $\alpha=\left\{\alpha_{1}, \alpha_{2}, \ldots, \alpha_{n}\right\}$ by sorting the total processing time of all jobs in ascending order. Set $l=1$.
Step 3: Apply the PF-NEH heuristic to produce an initial individual through the following steps.
Step 3.1: Let $\beta=\left\{\alpha_{l}\right\}$. Construct a completed job sequence $\beta=\left\{\beta_{1}, \beta_{2}, \ldots, \beta_{n}\right\}$ through the PF heuristic.
Step 3.2: Let $\pi^{*}=\left\{\beta_{1}, \beta_{2}, \ldots, \beta_{n-\lambda}\right\}$.
Step 3.3: For the job in sequence $\beta=\left\{\beta_{1}, \beta_{2}, \ldots, \beta_{n}\right\}$ from position $k=n-\lambda+1$ to $n$, find the best position $j^{*}$ by inserting $\beta_{k}$ into the current partial sequence $\pi^{*}$ to minimize the partial makespan. Then, insert $\beta_{k}$ into sequence $\pi^{*}$ at position $j^{*}$.
Step 3.4: Put $\pi^{*}$ into the population, i.e. $P c=P c \cup \pi^{*}$.
Step 4: If $|P c|==0.1 \times P S$ or $l==n$, then go to Step 5; otherwise, $l=l+1$, return to Step 3.
Step 5: Randomly generate an individual $\pi$ in the solution space. If there are no identical individuals in the current population, add it to the population, i.e. $P c=P c \cup \pi$; otherwise, discard this individual. Note that the similarity between two individuals is defined as follows:

$$
\begin{aligned}
S\left(\pi_{1}, \pi_{2}\right) & =\sum_{i=1}^{n} x_{i}\left(\pi_{1, i}, \pi_{2, i}\right) \\
x_{i}\left(\pi_{1, i}, \pi_{2, i}\right) & = \begin{cases}0 & \text { if } \pi_{1, i}=\pi_{2, i} \\
1 & \text { otherwise }\end{cases}
\end{aligned}
$$

If $S\left(\pi_{1}, \pi_{2}\right)<\varepsilon$, it means that these two individuals are similar. To adequately search the whole solution space, $\varepsilon$ is set to zero to make the population distribute in the whole solution space as much as possible.
Step 6: Repeat Step 5 until the population has $P S$ individuals.
In the above procedure, the jobs with different total processing times are used as the initial job of the PF-NEH heuristic to generate $0.1 \times P S$ different initial solutions. These initial solutions are not only of good quality but also different from each other. This strategy is chosen since if most individuals were randomly generated in the search space and only one individual was much better than the others, it would spend too much time in exploiting the area around these individuals to make them achieve a high level of quality in one iteration. As a result, the ability of the algorithm to perform more iterations would diminish. In particular, improvement of these random individuals using an exhausted local search method would consume a great deal of time and effort. The main computational burden of the PF-NEH can be attributed to the insertion process of Steps 3.1-3.4. In the insertion procedure of PF-NEH, $(2 n-\lambda+1) \lambda / 2$ partial sequences should be evaluated, which gives a total computational complexity of $O\left(m n^{3}\right)$. In this article, the speed-up method (Wang et al. 2010) is used to evaluate these partial sequences, so the PF-NEH can be completed in $O\left(m n^{2}\right)$ computational efforts compared with $O\left(m n^{3}\right)$ for the original PF-NEH.

# 3.2. Selection 

The construction of a probabilistic model of EDA depends on an elite set of individuals which are selected from the parental population using a selection operator. The linear rank selection operator has been extensively used in the selection procedure of EDA (Jarboui et al. 2009). In the traditional linear rank selection operator, the individuals are selected according to their rank in the population. The rank of the individuals is first transformed to the cumulative probability. Then, the individuals in the population are selected through sampling. However, there is a problem in this selection procedure. If only a few individuals are selected to construct the probabilistic model, some superior individuals in the population may not be selected since the random numbers (pseudo-random numbers) generated by the computer probably will not fall into the cumulative probabilistic intervals of these superior individuals. That is to say, the best individual in the population may not be selected or participate in the construction phase of the probabilistic model, which would result in an imprecise probabilistic model. Therefore, to choose those individuals with good quality, a modified linear rank selection operator is presented in this article. Two selection methods are used in this selection operator. One is based on elite selection, which ensures that the best individual or the top few best individuals will certainly be selected. The other is based on traditional linear rank selection, which ensures that those individuals participating in construction of the probabilistic model have a certain level of diversity so that the offspring individuals are different from each other. Hence, this modified linear rank selection operator can be used to construct an accurate probabilistic model and thereby obtain an offspring population with high quality and diversity. Algorithm 2 displays the procedure of the new selection operator.

Algorithm 2: Modified linear rank selection
Step 1: Let $\Pi_{e}=\emptyset$ and $l=P S . P S$ is the population size. The individuals in population $P c=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{P S}\right\}$ are sorted in descending order of their makespan. The selection probability of each individual can be calculated as follows:

$$
p\left(\pi_{i}\right)=\frac{r_{i}}{\sum_{\pi_{i} \in P c} r_{i}}
$$

![img-0.jpeg](img-0.jpeg)

Figure 1. The procedure of the modified linear rank selection operator.
where $\pi_{i}$ denotes the $i$ th individual and $r_{i}$ denotes its rank. Obviously, $\pi_{i}$ with $r_{i}=P S$ is the best one in the current population, which has a high probability of being selected.
Step 2: Calculate the cumulative probabilistic sumProbability for the $i$ th individual in the population according to sumProbability $(i)=\operatorname{sumProbability}(i-1)+p\left(\pi_{i}\right)$, where sumProbability $(0)=0$.
Step 3: Generate two uniformly random numbers $\delta_{1}$ and $\delta_{2}$ in the interval $[0,1]$.
Step 4: If $\delta_{1}<\delta_{2}$, then select the individual $\pi_{i}$ with $r_{i}=l$, put it into $\Pi_{e}$, i.e. $\Pi_{e}=\pi_{i} \cup \Pi_{e}$, set $l=l+1$, and go to Step 5; otherwise, generate a uniformly random number $\sigma$ in the interval $[0,1]$, and find the cumulative probability interval which satisfies sumProbability $(i-1) \leq$ $\sigma<\operatorname{sumProbability}(i), i=1,2,3, \ldots, n$ according to this random number. Set $\pi_{k}=\pi_{i}$ and put $\pi_{k}$ into $\Pi_{e}$, i.e. $\Pi_{e}=\pi_{k} \cup \Pi_{e}$.
Step 5: Repeat Steps 3-4 until $\Pi_{e}$ has $P S$ individuals.
To further describe the procedure of the modified linear rank selection operator, an example (number of jobs $=5, P S=8$ ) is given in Figure 1. In Figure 1, eight individuals are first ranked according to their makespan and then the cumulative probability for each individual is calculated according to its rank. Afterwards, the individuals in the population are selected based on the cumulative probability or rank. For example, generate two random numbers, e.g. $\delta_{1}=0.43$ and $\delta_{2}=0.12, \delta_{1}<\delta_{2}$, and one individual is selected based on the cumulative probability. A uniformly random number $\sigma=0.31$ is generated, which is in $\{0.278,0.417)$, so the individual $\{2,3,5,4,1\}$ is selected and saved into the new population. Then, generate two random numbers again, e.g. $\delta_{1}=0.25$ and $\delta_{2}=0.06, \delta_{1}>\delta_{2}$, and one individual is selected based on rank. So, the first best individual is selected and saved into the new population. Constantly switch the two cases above in a random way until the new population has $P S$ individuals.

# 3.3. Probabilistic model and sampling method 

The conventional EDAs use the probabilistic model to guide the exploration of the search space. Therefore, it is crucial for a high-powered EDA to build an effective probabilistic model. To address lot-streaming flow-shop scheduling problems with set-up times, Pan and Ruiz (2012a) proposed an effective probabilistic model with consideration of both job orders in the sequence and similar job blocks of the selected elite individuals. In their probabilistic model, the probability of placing job $i$ at position $k$ of the offspring, i.e. $\xi_{i, k}$, is calculated as follows:

$$
\xi_{i, k}= \begin{cases}\frac{\rho_{i, k}}{\sum_{l \in \Omega_{k}} \rho_{j, l}} & k=1 \\ \frac{1}{2}\left(\frac{\rho_{i, k}}{\sum_{l \in \Omega_{k}} \rho_{j, l}}+\frac{\tau_{f, j}}{\sum_{l \in \Omega_{k}} \tau_{f, l}}\right) & k=2,3, \ldots, n\end{cases}
$$

where $\rho_{i, k}$ denotes the number of times job $i$ appears before or at position $k$ in the selected individuals, $\tau_{j^{\prime}, i}$ denotes the number of times that job $i$ appears immediately after job $j^{\prime}$ in position $k-1$, and $\Omega_{k}$ is the set of jobs not scheduled until position $k$.

The above method of constructing a probabilistic model has a disadvantage when it is applied to solve the flow-shop scheduling problem. When the diversity of the population becomes poor and the individuals in the population are very similar, the matrix of job blocks tends to be sparse. This may mean that the number of times that job $i$ in $\Omega_{k}$ appears immediately after job $j^{\prime}$ in position $k-1$ equals zero, i.e. $\tau_{j^{\prime}, i}=0$, so that there exists an illegal case, i.e. $\sum_{l \in \Omega_{k}} \tau_{j^{\prime}, l}=0$. However, the authors did not mention how to handle this illegal case. Therefore, to overcome this shortcoming, a modified probabilistic model is presented to determine $\xi_{i, k}$ as

$$
\xi_{i, k}= \begin{cases}\frac{\rho_{i, k}}{\sum_{l \in \Omega_{k}} \rho_{j, l}} & k=1 \\ \frac{1}{2}\left(\frac{\rho_{i, k}}{\sum_{l \in \Omega_{k}} \rho_{j, l}}+\eta_{j^{\prime}, k}^{i}\right) & k=2,3, \ldots, n\end{cases}
$$

where $\eta_{j^{\prime}, k}^{i}$ is the probability of job $i$ in unscheduled job set $\Omega_{k}$ appearing immediately after job $j^{\prime}$ in position $k-1$, which is defined as follows:

$$
\eta_{j^{\prime}, k}^{i}= \begin{cases}\frac{\tau_{j^{\prime}, l}}{\sum_{l \in \Omega_{k}} \tau_{j^{\prime}, l}} & \sum_{l \in \Omega_{k}} \tau_{j^{\prime}, l}=0 \\ \frac{1}{\left|\Omega_{k}\right|} & \sum_{l \in \Omega_{k}} \tau_{j^{\prime}, l} \neq 0\end{cases}
$$

where $\left|\Omega_{k}\right|$ is the size of unscheduled jobs. In Equation (11), when $\sum_{l \in \Omega_{k}} \tau_{j^{\prime}, l}=0$, a block is artificially allocated for each unscheduled job, i.e. $\tau_{j^{\prime}, l}=1, l \in \Omega_{k}$, so that each unscheduled job has the same probability of appearing after job $j^{\prime}$ in position $k-1$, i.e. $\frac{1}{\sum_{l \in \Omega_{k}} \tau_{j^{\prime}, l}}=\frac{1}{\left|\Omega_{k}\right|}$. This treatment would effectively avoid the loss of information of similar job blocks caused by poor diversity and enhance the self-disturbance of the probabilistic model. Based on Equation (10), the job assigned to a specific position $k$ in the sequence can be determined by the probability of $\xi_{i, k}$.

To generate a job sequence with high quality, a new sampling method is developed based on the probabilistic model above. After determining the assignment probability of each job according to Equation (10), one specific job can be selected by a roulette wheel selection method for the current position. The detailed procedure of generating a new individual is shown in Algorithm 3.

# Algorithm 3: Sampling method 

Step 1: Set the position index $k=1, \pi=\emptyset$. Let $\Omega=\{\Omega(1), \Omega(2), \ldots, \Omega(n)\}$ denote the unassigned jobs set.
Step 2: Calculate the probabilistic vector $P=\left\{\xi_{\Omega(1), k}, \xi_{\Omega(2), k}, \ldots, \xi_{\Omega(n-k+1), k}\right\}$ for position $k$ using Equation (10).
Step 3: Construct a roulette wheel vector $r w$ based on $P$, i.e. $r w(0)=0, r w(j)=r w(j-1)+\xi_{\Omega(j), k}$, $j=1,2, \ldots, n-k+1$.
Step 4: Generate a rand number $r$ in the interval $[0,1]$. If $r w(j-1)<r<r w(j)$, then $\pi(k)=\Omega(j)$, and remove $\Omega(j)$ from $\Omega$, i.e. $\Omega=\Omega \backslash \Omega(i)$.
Step 5: If $k==n$, then output $\pi$; otherwise, $k=k+1$ and return to Step 2.

### 3.4. Path relinking

EDA generates new individuals using the probabilistic model. Although it has been proven that EDA can converge to the global optimum (Zhang and Mühlenbein 2004), two weaknesses mean that the

convergence property of EDA is not excellent. First, it is very difficult to build an exact probabilistic model based on a limited population. Secondly, owing to the randomness of sampling, the new individuals may deviate from the centre of the probabilistic model so that the fitness of these individuals is very poor. This leads to blindness of the search when using the probabilistic model to guide the search process. To overcome these drawbacks, a search technique named path relinking, proposed by Glover and Laguna (2007), is used to guide the search process. Path relinking is mostly used as a local search procedure. It can generate a set of new individuals or offspring between two good individuals. In this work, path relinking is used to revise the individuals that deviate from the centre of the probabilistic model and improve the convergence property of EDA. In path relinking, given two selected individuals, the original individual $\alpha$ and the guide individual $\beta$, a series of movements (i.e. swap moves or insertion moves) is performed on these two individuals to transform $\alpha$ to $\beta$. Each time, a movement is carried out and an intermediate individual is obtained. With increasing movements, the obtained intermediate individual becomes very similar to $\beta$ and very different from $\alpha$. Finally, all obtained intermediate individuals are evaluated and the individual with the lowest makespan will be selected. Note that the set of moves from individual $\alpha$ to $\beta$ is not the same as from $\beta$ to $\alpha$ (Vallada and Ruiz 2010). However, if $\alpha$ is very similar to $\beta$, there exists one exceptional case that needs only one move from $\alpha$ to $\beta$. No intermediate individuals are obtained. To avoid this situation, Pan et al. (2013) proposed a method that performed a random insertion or swap move on $\beta$ to ensure that a new individual is generated. Therefore, in the path relinking in the present study, to ensure the diversity of the search, the swap move is used as the main transforming tool, while the insertion move is used to ensure that at least one new individual is generated. It should be noted that the guide individual, i.e. $\beta$, comes from the best individual in the population, while the original individual, i.e. $\alpha$, is generated by sampling from the probabilistic model. The procedure of path relinking is described in Algorithm 4.

Algorithm 4: Path relinking
Step 1: Set path set $\Pi_{p}=\emptyset, k=1, \pi=\alpha$.
Step 2: For each position $k=1$ to $n$, if $\pi(k) \neq \beta(k)$, find the position $p$ of job $\beta(k)$ in the individual $\pi$ and swap the job in position $k$ with $p$ for the individual $\pi$. If $\pi \neq \beta$, save the individual $\pi$ into $\Pi_{p}$; otherwise, go to Step 3.
Step 3: If $\Pi_{p}$ is empty, randomly select two positions $p_{1}$ and $p_{2}$ in $\beta, p_{1} \neq p_{2}$, and insert the job in position $p_{1}$ before the job in position $p_{2}$. Then, put the generated individual into $\Pi_{p}$; otherwise, go to Step 4.
Step 4: Evaluate all individuals in $\Pi_{p}$ and return the one with the lowest makespan.
It can be observed from the procedure of path relinking above that its time complexity depends on the differences between the original and the guide individual. In the worst case, the sequence of the original individual is completely contrary to the guide individual. A total of $n / 2$ intermediate individuals will be generated and their evaluation will consume $O\left(m n^{2} / 2\right)$. In the best case, the original individual only needs to generate an intermediate individual to obtain the guide individual, so the time complexity is $O(m n)$. In the exceptional case, no intermediate individuals are generated and only one mutation individual is generated by executing a random insertion move, which needs $O(n)$ to execute the insertion move and $O(m n)$ for evaluation. However, the path relinking would not consume much computational time. This is because, in the proposed algorithm, the original individual is generated by sampling from the probabilistic model. The guide individual is the best individual in the population. The probabilistic model has extracted the features of the superior individuals in the population. Therefore, the individuals generated by sampling from the probabilistic model are similar to the best solution in the population but different from each other. Hence, only a few intermediate individuals are generated between the original and the guide individual. Meanwhile, the best individual

![img-1.jpeg](img-1.jpeg)

Figure 2. An example of path relinking.
in the population is selected as the guide individual, which ensures that the generated intermediate individuals are of good quality.

To clearly illustrate the procedure of path relinking, an example with two permutations $\alpha=$ $\{3,1,4,5,2\}$ and $\beta=\{2,3,4,1,5\}$ is considered in Figure 2. According to the rule of path relinking, for the individual $\alpha$, job 3 on position 1 will be swapped with job 2 on position 5 . Then, a new intermediate individual $\{2,1,4,5,3\}$ is generated. At the same time, swap job 1 on position 2 with job 3 on position 5 , and another individual $\{2,3,4,5,1\}$ is generated. Lastly, swap job 5 on position 4 with job 1 on position 5 , generating $\beta$. Two intermediate individuals, i.e. $\{2,1,4,5,3\}$ and $\{2,3,4,5,1\}$, are obtained.

# 3.5. Local search 

To enhance the exploitation of EDA, a local search is implemented to quickly lead the current new individual towards the promising area. To solve the BFSP with the makespan criterion, Wang et al. (2010) presented an RLS, which has been adopted in other algorithms (Wang, Pan, and Tasgetiren 2011; Pan et al. 2013). In RLS, $\pi_{R}=\left\{\pi_{R}(1), \pi_{R}(2), \ldots, \pi_{R}(n)\right\}$ denotes the reference sequence. Usually, the best individual or a random permutation of all jobs is selected as the reference sequence. The process of RLS is shown as follows. Suppose that the current individual is $\pi=\{\pi(1), \pi(2), \ldots, \pi(n)\}$. First, the RLS removes job $\pi_{R}(i), i=1,2, \ldots, n$, from the current individual $\pi$ and inserts it into all possible slots of $\pi$. Then, find the slot $j$ with the lowest makespan and insert job $\pi_{R}(i)$ into the slot $j$ of $\pi$ to generate a new individual $\pi_{2}$. Finally, if $\pi_{2}$ is better than $\pi, \pi$ will be replaced by $\pi_{2}$. Repeat this procedure until no better solutions are obtained.

Such a local search has the disadvantage that once the reference sequence $\pi_{R}$ is given, the search path of RLS becomes deterministic. That is, all movements among jobs are known. This mechanism makes RLS lack an effective self-disturbance ability and has difficulty changing the search path by itself. Therefore, an mRLS is developed in this article. In the mRLS, a random trajectory $r t=\{r t(1), r t(2), \ldots, r t(n)\}$ (i.e. a random permutation of $n$ jobs) is generated to replace the reference sequence. After searching all the track points in $r t$, the search trajectory will be updated. The Fisher-Yates shuffle method (https://en.wikipedia.org/wiki/Fisher-Yates_shuffle) is adopted to update the current trajectory. Therefore, this mechanism can effectively enhance the diversity of the search path. The procedure of the mRLS is shown in Algorithm 5.

## Algorithm 5: Modified RLS

Step 1: Set count $=0, j=0$ and input the individual $\pi$.
Step 2: Randomly generate a trajectory $r t=\{r t(1), r t(2), \ldots, r t(n)\}$.
Step 3: Set $j=j+1$. If $j>n$, then let $j=\bmod (j, n)$ and update the trajectory $r t=\{r t(1), r t(2), \ldots, r t(n)\}$ using the Fisher-Yates shuffle method. $\pi^{\prime} \leftarrow$ Remove job $\pi(r t(j))$ from $\pi$, bestfit $=\infty$.

Step 4: For $i=1$ to $n, \pi_{t} \leftarrow$ the individual by reinserting job $\pi(r t(j))$ in position $i$ of $\pi^{\prime}$. If $C_{\max }\left(\pi_{t}\right)<$ bestfit, set bestpos $=j$ and bestfit $=f\left(\pi_{t}\right)$.
Step 5: If bestfit $<C_{\max }(\pi)$, then $\pi \leftarrow$ insert job $\pi(r t(j))$ at position bestpos of $\pi^{\prime}$, count $=0$; otherwise, count $=$ count +1 .
Step 6: If count $\leq n$, then go back to Step 3; otherwise, stop the procedure and return $\pi$.
It can be seen from Algorithm 5 that the main difference between the mRLS and the original RLS is whether the referenced sequence (or the search trajectory) is updated. For the original RLS, the referenced sequence is fixed. When all jobs in the referenced sequence have been considered, the local search will begin again from the first job of the current referenced sequence. This mechanism may cause repeated searches in the same neighbourhoods and result in low efficiency. For the mRLS, the search trajectory is dynamically updated. When all jobs in the search trajectory have been completed but the whole local search is not finished (i.e. count $\neq n$ ), the search trajectory will be updated at this time. This mechanism can prevent the neighbourhoods from always being explored in the same order. In addition, the Fisher-Yates shuffle method is adopted to update the search trajectory since it can produce unbiased permutations, i.e. every permutation is equally likely. Hence, compared with the original RLS, the mRLS can dynamically and efficiently exploit the search space.

Moreover, to reduce the complexity of evaluating $n$ new individuals generated by reinserting the $\pi(r t(j))$ job into all possible $n$ positions of $\pi^{\prime}$ in Algorithm 5, two accelerating algorithms, i.e. a speedup evaluation (Wang et al. 2010) and a pruning procedure (Wang et al. 2012), are adopted. The speedup evaluation first calculates the departure time $D_{k, j}^{\prime}$ and the tail time $F_{k, j}^{\prime}$ of job $i$ on machine $j$ in $\pi^{\prime}$. Note that the tail time is the duration between the latest starting time of job $i$ on machine $j$ and the end of the operations. Then, insert the job $\pi(r t(j))$ into the $k$ th position of $\pi^{\prime}$ and calculate the departure time $D_{k, j}^{\prime \prime}$ of $\pi(r t(j))$ on each machine. A new individual $\pi_{k}$ is obtained, whose makespan is calculated by

$$
C_{\max }\left(\pi_{k}\right)=\max _{j=1,2, \ldots, m} D_{k, j}^{\prime \prime}+F_{k, j}^{\prime \prime}
$$

Based on the pruning procedure, if one of $D_{k, j}^{\prime \prime}+F_{k, j}^{\prime \prime}$ is larger than the makespan of $\pi, \pi_{k}$ must be no better than $\pi$. So, it is unnecessary to further evaluate $\pi_{k}$ in search of a better schedule. $\pi_{k}$ can be discarded and the next insertion position can be considered. The speed-up method reduces the computational effort of evaluating each insertion from $O(m n)$ to $O(m)$ and the pruning procedure further reduces the computational effort. Therefore, the computational complexity of the mRLS is less than $O\left(m n^{2}\right)$ to evaluate the whole insertion neighbourhood of $\pi$.

# 3.6. Diversity-maintaining scheme 

As the population evolves, its diversity gradually begins to degenerate and the individuals in the population become very similar. If this problem is detected during the evolution, some diversitymaintaining strategies can be used to overcome it, such as generating a new population, replacing some individuals in the current population or applying some moves over several individuals in the current population. Many diversity measures have been presented in the literature (Pan and Ruiz 2012a; Xu et al. 2014). In this work, a method proposed by Vallada and Ruiz (2010) is adopted to calculate the diversity value. In this method, the sum of all positions where two given solutions have different jobs is used to measure similarity. Using this metric, the diversity of the population (Div) can be calculated as follows:

$$
D i v=\frac{1}{n-1} \sum_{k=1}^{n} \sum_{\alpha=1}^{n} \frac{C_{k}(\alpha)}{P S}\left(1-\frac{C_{k}(\alpha)}{P S}\right)
$$

where $C_{k}(\alpha)$ is the number of times that job $\alpha$ appears at a given position $k$ across the population. Therefore, a diversity value between 0 and 1 can be obtained from Equation (13).

Base on the above diversity value, if the diversity value (Div) of the current population falls below a given threshold value $\gamma, 0 \leq \gamma \leq 1$, it means that all individuals are very similar and the population has deteriorated. The current population should be regenerated. In this work, the individuals of the population are first sorted in non-descending order according to their makespan. Then, three schemes are used to regenerate the population with high quality and diversity, as follows: (1) keep the top $20 \%$ best individuals from the sorted list; (2) apply one single random insert operation to each of the intermediate $40 \%$ individuals; and (3) randomly generate $40 \%$ new individuals to replace the last $40 \%$ individuals. To determine an appropriate $\gamma$ value, a calibrated experiment is presented in Section 4.2.

# 3.7. Overview of the P-EDA 

According to the above description, the complete procedure of the proposed P-EDA is described in Algorithm 6. Note that, in contrast to the traditional EDAs, only one new individual is generated in each iteration for the P-EDA. If the new individual is better than the worst individual of the current population and there are no other identical individuals in the current population, the worst individual is replaced by this new individual. Moreover, since only one individual is generated in each iteration, the probabilistic model will be updated for every $P S$ iterations. To reduce the computational complexity, the diversity of the population is also checked every $P S$ iterations.

## Algorithm 6: P-EDA

Step 1: Initialize the population size $P S$ and the diversity threshold $\gamma$ and set $\operatorname{gen}=1$.
Step 2: Initialize the population Pc (described in Algorithm 1) and evaluate each individual of the population.
Step 3: Select $P S$ individuals from the population with the modified linear rank selection (described in Algorithm 2) to generate the elite set $\Pi_{e}$.
Step 4: Estimate the probabilistic model based on the elite set $\Pi_{e}$.
Step 5: Sample the probabilistic model to generate a new individual $\pi$ (described in Algorithm 3).
Step 6: Apply path relinking (described in Algorithm 4) to the new individual $\pi(\alpha)$ and the best individual $(\beta)$ in the population to construct another complete individual $\pi^{\prime}$.
Step 7: Perform the mRLS (described in Algorithm 5) over $\pi^{\prime}$.
Step 8: If $C_{\max }\left(\pi^{\prime}\right)<C_{\max }\left(\pi_{\text {worst }}\right)$ and $\pi^{\prime} \cap P c=\emptyset$, then replace the worst individual $\pi_{\text {worst }}$ in the population $P c$ with $\pi^{\prime}$; otherwise, discard it.
Step 9: If $\bmod (\operatorname{gen}, P S)=0$, then check the diversity of the population with Equation (13). If Div $<$ $\lambda$, then regenerate the population and update the probabilistic model with the procedure in Steps $3-4$.
Step 10: If the termination criterion is reached, then return the best solution found so far and stop the algorithm; otherwise, gen $=$ gen +1 , go back to Step 5.

### 3.8. Computational complexity of P-EDA

Suppose there are $n$ jobs and $m$ machines in the BFSP and the population size is $p$. From the process of P-EDA above, it can be learned that this algorithm is made up of seven parts. The first part is the generation and evaluation of the initial population. Since $0.1 \times p$ initial individuals are generated by PF-NEH, whose time complexity is $O\left(m n^{2}\right)$, and others are randomly generated in the search space, the time complexity of initialization is $O\left(0.1 \mathrm{pmn}^{2}\right)+O(0.9 \mathrm{pmn})$. The second part is the modified linear rank selection, the time complexity of which is mainly decided by the sort method of the individuals in the population. Since the P-EDA is implemented in Java, which uses merging sort, the time complexity of the second part in the worst case is $O(\operatorname{plog}(p))$. The third part is the construction of the probabilistic model, which needs to traverse all individuals in the population to construct an $n \times n$

probabilistic matrix. The time complexity of the third part is $O\left(n^{2}\right)$. The fourth part is the production of offspring, which needs to generate a new individual by sampling from the $n \times n$ probabilistic matrix. Its time complexity is also $O\left(n^{2}\right)$. The fifth part is the path relinking; its time complexity is $O\left(m n^{2} / 2\right)$ in the worst case, as discussed in Section 3.4. For the sixth part, the local search phase consumes at least $O\left(m n^{2}\right)$ to exploit a solution, which can be seen in Section 3.5. For the last part, i.e. the diversity-maintaining scheme, all individuals in the population will be sorted in non-descending order, so its time complexity is $O(\operatorname{plog}(p))$. Note that the local search phase has the maximum time complexity among all parts of the proposed algorithm. According to the analyses above, the time complexity of P-EDA under the condition of $k$ times evolution can be calculated as follows:

$$
\begin{aligned}
O(k, n, m, p)= & O\left(0.1 p m n^{2}\right)+O(0.9 p m n)+O(k)^{*}\left[2^{*} O(p \log p)\right. \\
& \left.+2^{*}\left[O\left(n^{2}\right)+O\left(m n^{2}\right)\right]\right] \\
\approx & O\left(0.1 p m n^{2}\right)+O(k)^{*}\left[O\left(2 n^{2}\right)+O\left(m n^{2}\right)\right] \\
\approx & O\left(0.1 p m n^{2}\right)+O(k)^{*} O\left(m n^{2}\right) \\
\approx & O\left(p m n^{2}\right)+O\left(k m n^{2}\right) \\
= & O\left((p+k) m n^{2}\right)
\end{aligned}
$$

# 4. Computational evaluation 

### 4.1. Experimental set-up

The proposed algorithm and the compared algorithms are coded in Java language. The computational experiments are conducted on a server with two 2.40 GHz Intel ${ }^{\circ}$ Xeon ${ }^{\circ}$ E5-2520 v3 processors (12 cores) and 64 GB of RAM running Windows Server 2008. To compare the performance of PEDA with other methods, the well-known Taillard's benchmark data set (Taillard 1993) is used in the computational experiment. This benchmark contains 12 groups with size varying from 20 jobs and five machines to 500 jobs and 20 machines, where $n \in\{20,50,100,200,500\}, m \in\{5,10,20\}$. Each group consists of 10 instances. However, sets $200 \times 5,500 \times 5$ and $500 \times 10$ are missing, but they have been added by Pan and Ruiz (2012b) to maintain the orthogonality of the experiment. All implemented algorithms are executed in 10 independent replications for each instance. To make a fair comparison, the same elapsed central processing unit (CPU) time, $t=\rho \times m \times n \mathrm{~ms}$, is adopted as the termination criterion, where $\rho$ has three values: 30,60 and 90 .

To evaluate the performance of each algorithm, the average relative percentage deviation (ARPD) (Wang et al. 2010) is computed to measure the quality of the solutions. The ARPD is calculated as follows:

$$
\mathrm{ARPD}=\frac{1}{10} \sum_{i=1}^{10} \frac{C_{i}-C_{R}}{C_{R}} \times 100
$$

where $C_{i}$ is the solution obtained by one of the algorithms on a given instance, and $C_{R}$ is the upper bound from Ribas, Companys, and Tort-Martorell (2011). Since no one has provided the upper bounds for the above three supplementary test sets, the best solutions obtained by the IG of Ribas, Companys, and Tort-Martorell (2011) and implemented by the current authors are used as the upper bounds.

In addition, since the parameters have an important influence on the performance of P-EDA, the design of experiments method (Montgomery 2008) is implemented to determine the best parameters for the proposed algorithm. There are two main parameters for the proposed algorithm, i.e. the population size $(P S)$ and the diversity threshold $(\lambda)$. Interested readers can find the detailed results and analyses of the parameters' calibration in the online supplementary material. The final parameters used in the proposed P-EDA are set as follows: $P S=50$ and $\lambda=0.3$.

Table 1. Statistical results of P-EDA-WPT, P-EDA-R and P-EDA.

Note: P-EDA $=$ estimation of distribution algorithm with path relinking; P-EDA-WPT $=$ P-EDA with Wang, Pan and Tasgetiren heuristic; P-EDA-R $=$ P-EDA without any heuristics.

# 4.2. Effectiveness of population initialization 

The PF-NEH heuristic plays an important role in guiding the P-EDA to quickly converge to the promising area. Therefore, to confirm the contribution of the PF-NEH heuristic for P-EDA, the following experiments are carried out. In the first trial, another constructive heuristic, i.e. NEH_WPT, proposed by Wang, Pan, and Tasgetiren (2011), is used to replace the PF-NEH heuristic to generate an initial solution and other solutions are randomly generated in the search space. Compared with the original NEH, the NEH_WPT adopts the non-decreasing sums of their process time to sort the jobs; this is because jobs with a higher total processing time may block the successive jobs and yield a longer blocking time than jobs with less total processing time for BFSP. P-EDA combined with the NEH_WPT heuristic is referred to as P-EDA-WPT. In the second trial, P-EDA without any heuristics (P-EDA-R) is executed. Lastly, the complete P-EDA is executed. The termination time is set to $\rho=30$. Each algorithm is executed 10 times for each instance. The statistical results are reported in Table 1.

As can be seen from Table 1, P-EDA outperforms P-EDA-R and P-EDA-WPT, which demonstrates that PF-NEH can effectively enhance the performance of the proposed P-EDA. Moreover, the results of P-EDA are better than for P-EDA-WPT, which reveals that PF-NEH can provide better starting points for the proposed P-EDA in comparison with NEH_WPT. This is because PF-NEH generates more than one excellent initial solutions, which can effectively guide the P-EDA to quickly converge to the promising area. NEH_WPT generates only one solution, which has a limited contribution to enhancing the convergence speed of P-EDA. Therefore, through the PF-NEH heuristic and random method, an initial population with high quality and diversity is obtained.

### 4.3. Effectiveness of path relinking

To investigate the effectiveness of path relinking for EDA, a computational experiment is designed as follows. In the first trial, P-EDA with path relinking is executed. In the second trial, P-EDA is executed without path relinking. By comparing the experimental results of these two trials, the contribution of path relinking can be clearly confirmed. The termination criterion for these two algorithms is identically set to $\rho=30$. Each algorithm is run 10 times for each instance. Table 2 reports the comparison results of these two trials.

Table 2. Statistical results of P-EDA and EDA.

Note: P-EDA = estimation of distribution algorithm with path relinking; EDA = estimation of distribution algorithm.
![img-2.jpeg](img-2.jpeg)

Figure 3. 95\% confidence interval (CI) plot of average relative percentage deviation (ARPD) by algorithms $n$ and $m$. EDA $=$ estimation of distribution algorithm; P-EDA $=$ proposed estimation of distribution algorithm.

As can be seen from Table 2, P-EDA obtains a smaller ARPD value of -0.864 compared to the corresponding value of 0.555 for EDA. It can also be seen from Table 2 that the performances of EDA and P-EDA gradually improve with increasing instance size. To illustrate this case, the interactions between $m$ and $n$ with EDA and P-EDA are shown in Figure 3. Notice in this figure that P-EDA is less influenced by $n$, while the behaviour of EDA is significantly different with respect to $n$. Especially for the instances with 50 and 100 machines, EDA performs relatively poorly. It can also be observed that P-EDA and EDA are both less influenced by $m$, but P-EDA performs slightly better when $m$ increases. Therefore, these results demonstrate that path relinking makes a significant contribution to the effectiveness of EDA, especially for large instances.

# 4.4. Effectiveness of local search 

To test the effectiveness of the proposed local search method in P-EDA, three variants of P-EDA are compared, whose abbreviations are defined as follows: (1) P-EDA represents P-EDA with the mRLS; (2) P-EDA/RLS represents P-EDA with the original RLS; and (3) P-EDA/NOL represents PEDA without any local searches. From the experimental results of these three trials, two facts about the local search for P-EDA can be confirmed. One is the contribution of the local search, and the other is

Table 3. Statistical results of P-EDA, P-EDA/RLS and P-EDA/NOL

Note: P-EDA = estimation of distribution algorithm with path relinking; P-EDA/RLS $=$ P-EDA with the original referenced local search; p-EDA/NOL $=$ P-EDA without any local searches.
that the mRLS outperforms the original RLS. These three variants of P-EDA are tested independently with a termination criterion of $\rho=30$. The results are reported in Table 3.

In Table 3, it can be observed that P-EDA achieves a smaller ARPD than P-EDA/RLS and PEDA/NOL, while P-EDA/RLS outperforms P-EDA/NOL. It can be demonstrated that the local search is very important for the performance of P-EDA. Moreover, it also reveals that mRLS is more suitable for P-EDA than the original RLS. In particular, P-EDA/RLS and P-EDA/NOL give the worst performance on the small-scale instances (i.e. $n=20$ and 50). The P-EDA without local search only has a capability for global search and its exploitation is relatively poor. If a solution is trapped in local optima, P-EDA without local search finds it very difficult to escape from local optima. The mRLS enriches the search directions by means of the random trajectory and compensates for the poor exploitation of P-EDA. Thus, it can be concluded that mRLS makes a significant contribution to the effectiveness of P-EDA.

# 4.5. Effectiveness of the diversity-maintaining scheme 

The diversity-maintaining scheme can effectively restart the algorithm. Hence, the function of the adopted diversity-maintaining scheme is verified through experiments. In the experiments, P-EDA is executed with and without the diversity-maintaining scheme (i.e. P-EDA and P-EDA-ND, respectively). The termination time is set to $\rho=30$. Each algorithm is executed 10 times for each instance. The statistical results are given in Table 4.

It can be seen from Table 4 that P-EDA with a diversity-maintaining scheme is better than P-EDA without a diversity-maintaining scheme for all scale instances. The superiorities of the diversitymaintaining scheme can be contributed to using three different strategies to build a new population with high quality and diversity. Meanwhile, considering the diversity of the population after some iterations can further save computational time. Therefore, the adopted diversity-maintaining mechanism can effectively ensure that the population has good diversity.

### 4.6. Comparison of existing algorithms

To verify the effectiveness and efficiency of the proposed P-EDA in searching for better solutions, it was compared with some well-performing algorithms for BFSP with the makespan criterion. These algorithms are HDDE (Wang et al. 2010), hmgHS (Wang, Pan, and Tasgetiren 2011), IABC (Han et al.

Table 4. Statistical results of P-EDA-ND and P-EDA.

Note: P-EDA $=$ estimation of distribution algorithm with path relinking; P-EDA-ND $=$ P-EDA without diversitymaintaining scheme.
2012), DE-ABC (Han, Gong, and Sun 2014), MFFO (Han et al. 2016), IG (Ribas, Companys, and TortMartorell 2011), TPA (Wang et al. 2012), RAIS (Lin and Ying 2013), serial variable neighbourhood search (SVNS) (Ribas, Companys, and Tort-Martorell 2013), MA (Pan et al. 2013) and iterated greedy algorithm with blocking properties (B-IG) (Ding et al. 2016). It is should be noted that since these algorithms were encoded in different programming languages and executed on different computer platforms, and the reported results came from different upper bounds, it is unreasonable to directly compare them according to their reported results in the literature. Thus, to make a fair and reasonable comparison, all compared algorithms are reimplemented with the same programming language and executed in the same computer environment. All algorithms have the same CPU power and time available. To test the efficiency of all the algorithms, the termination criterion $\rho$ has three values: 30 , 60 and 90 . This termination criterion has been used in recent literature on scheduling (Vallada and Ruiz 2010; Ribas, Companys, and Tort-Martorell 2015; Pan and Ruiz 2012b). As suggested in Ribas, Companys, and Tort-Martorell (2013), the parameters of the SVNS are taken as $\beta=0.5, \alpha=0.75$ and $d s=8$. In addition, the PF-NEH heuristic is used to generate the initial solution of SVNS. For the other algorithms, the parameters and initialization procedure are in accordance with the original articles. The results are shown in Tables 5-7, with the minimum ARPD values in bold.

As can be seen from Table 5, where $\rho=30$, the total ARPD obtained by the P-EDA is -0.864 , which is superior to the corresponding values obtained by other algorithms. The P-EDA outperforms the other algorithms for most instance sizes. MA obtains the best performance for the instance sizes $50 \times 5,50 \times 10$ and $50 \times 20$. B-IG achieves the best values on the instance sizes $100 \times 20$ and $200 \times 20$. Regarding the two improved ABC algorithms, the results of DE-ABC are better than IABC. In addition, P-EDA achieves the best performance on the large-scale instances ( 500 machines). For $\rho=60$, it can be found from Table 6 that the results of P-EDA are much lower than those of the other algorithms. For the instance sizes $50 \times 5,50 \times 10$ and $50 \times 20$, MA also has the best performance and this is similar with $\rho=30$. In Table 7, where $\rho=90$, P-EDA is also substantially better than the other algorithms for most instance sizes. For the small-scale instances ( 20 machines), SVNS, B-IG, MA and P-EDA obtain the optimal solutions. It can also be found from these tables that the performance of RAIS, SVNS and B-IG is largely improved with additional CPU time, but this is not enough to compete with the proposed algorithm. Therefore, it can be concluded from the above results that the proposed P-EDA is better than the other algorithms for solving the BFSP with the makespan criterion.

To check whether the differences observed in Tables 5-7 are significant, a multi-factor analysis of variance (ANOVA) is carried out, where the number of jobs $n$, the number of machines $m$, the

Table 5. Statistical results of the compared algorithms $(\rho=30)$.

Note: HDDE $=$ hybrid discrete differential evolution; hmgHS $=$ hybrid modified global-best harmony search; $\mathrm{IABC}=$ improved artificial bee colony; DE-ABC $=$ differential evolution-artificial bee colony; MFFO $=$ modified fruit fly optimization; IG = iterated greedy algorithm; TPA $=$ three-phase algorithm; RAIS $=$ revised artificial immune system; SVNS $=$ serial variable neighbourhood search; MA = mimetic algorithm; B-IG = iterated greedy algorithm with blocking properties; P-EDA $=$ estimation of distribution algorithm with path relinking.

Table 6. Statistical results of the compared algorithms $(\rho=60)$.

Note: For full names of algorithms, see footnote to Table 5.
elapsed CPU time $t$ and algorithm are considered as factors. Table 8 summarizes the significance of these factors and their interactions. It can be seen from this table that these considered factors and their interactions are highly significant ( $p$ value $<0.05$ ). The ANOVA hypotheses are tested by a residual analysis, which shows small departures from normality. Therefore, the results obtained in the ANOVA validate the above conclusions. Figure 4 depicts a $95 \%$ confidence interval plot of the interaction between $t$ and all the compared algorithms. It can be seen from this figure that the total ARPD of almost all algorithms declines with increasing elapsed CPU time, except for TPA. The proposed P-EDA statistically outperforms the other algorithms under the corresponding termination criterion. The total ARPD of TPA when $\rho=90$ is slightly larger than when $\rho=60$, which indicates that TPA has been convergent and that additional CPU time does not translate into much better results. RAIS is more influenced by $t$; this may be because if contains no effective local search, so it requires more time to obtain better solutions.

Table 7. Statistical results of the compared algorithms $(\rho=90)$.

Note: For full names of algorithms, see footnote to Table 5.

# Interval Plot of ARPD 

$95 \%$ CI for the Mean
![img-3.jpeg](img-3.jpeg)

Figure 4. 95\% confidence interval (CI) plot of average relative percentage deviation (ARPD) by all compared algorithms and $t$.

Figures 5 and 6 investigate the interactions between $m$ and $n$ with the compared algorithms. As can be seen from Figure 5, SVNS, MA, RAIS and P-EDA are less influenced by $m$, while the other algorithms have different performances in respect to the $m$ values. It can be observed from Figure 6 that most of algorithms have a progressive reduction in the performance with increasing $n$ value, except for B-IG, MA, SVNS and P-EDA. As $n$ increases, the performances of these four algorithms grow better and better. In particular, P-EDA and MA have good performance on the large-scale instances. The convergence ability is also very important for the proposed algorithm, and some convergence curves and relative analyses are shown in the online supplementary material.

Although all the explanations and details given in the original articles were strictly followed to implement these compared algorithms and closely reproduce the published results, the results obtained here still deviate from the original results since some implemented details were not mentioned in the original articles. Hence, to make the results of the comparison more convincing, the results of P-EDA are also compared with the results reported in the literature. These compared

Table 8. ANOVA results for the comparison of algorithms.

![img-4.jpeg](img-4.jpeg)

Figure 5. 95\% confidence interval (CI) plot of average relative percentage deviation (ARPD) by all compared algorithms and $m$.
algorithms adopt the same performance evaluation method, i.e. Equation (14) and test instances. Test instances come from standard Taillard's benchmarks, which exclude the instance sizes $200 \times 5$, $500 \times 10$ and $500 \times 5$. These compared algorithms are hmgHS, IG, RAIS, TPA, HDDE, SVNS_D, MA and B-IG. The results of these algorithms were obtained from the relevant literature. The termination criterion of P-EDA is set to $\rho=100$. Each instance is independently executed in 10 replications. The comparison results are reported in Table 9.

It can be seen from Table 9 that P-EDA achieves the best ARPD among all the compared algorithms. To be specific, for small-scale instances ( $n=20$ ), HDDE, RAIS, B-IG and P-EDA obtain the best solutions. For the medium-scale instances ( $n=50,100$ ), B-IG obtains the best performance, except for $100 \times 5$. P-EDA outperforms the other algorithms at the considered margin for large-scale instances ( $n=200,500$ ). There are three reasons for this. The first is that the PF-NEH heuristic provides several excellent initial solutions. The second is that the mRLS fully exploits the area around a solution by frequently transforming the search path. The third is that EDA quickly explores the promising area in the solution space. This comparison with the results in the literature confirms that

Interval Plot of ARPD
![img-5.jpeg](img-5.jpeg)

Figure 6. 95\% confidence interval (CI) plot of average relative percentage deviation (ARPD) by all compared algorithms and $n$.

Table 9. Comparison results of the algorithms.
Note: For full names of algorithms, see footnote to Table 5.
the proposed P-EDA is an effective and efficient approach for the BFSP with makespan criterion, especially for the large-scale BFSP.

Since the proposed P-EDA is competitive with other well-performing algorithms, the best solutions obtained by the proposed P-EDA are compared with the results reported in the literature. Some new upper bound solutions have been discovered during the experiments. Table 10 summarizes the comparison results, where the new upper bound solutions obtained by P-EDA are highlighted in bold. Note that the instance sizes of $200 \times 20,500 \times 5$ and $500 \times 10$ are not included in Table 10, since the algorithms in the literature do not consider these instances. In Table 10, the 'source' column represents the methods adopted to obtain the best solution. In the source column, 1 indicates HDDE, 2 indicates IABC, 3 indicates DE-ABC, 4 indicates MFFO, 5 indicates IG, 6 indicates TPA, 7 indicates RAIS, 8 indicates SVNS, 9 indicates MA, 10 indicates B-IG and 11 indicates the proposed P-EDA. As shown in Table 10, all of the compared algorithms achieve 30 best values for the small-scale instances, i.e. $20 \times 5,20 \times 10$ and $20 \times 20$. For the remaining 90 instances, P-EDA provides 59 new unique upper bound solutions, while others come from four of MA, one of MFFO, 14 of SVNS and 12 of B-IG.

Table 10. Upper bound solutions for Tailliard's benchmarks.
These experimental results demonstrate that the proposed P-EDA can generate better results than all of the compared algorithms. Some Gantt charts of the upper bound solutions obtained by P-EDA are shown in the online supplementary material.

# 5. Conclusion 

In this article, an effective EDA, named P-EDA, is proposed for solving the BFSP with the objective of minimizing makespan. In P-EDA, a problem-specific constructive heuristic (PF-NEH) and the random method were combined to initialize the population. A modified linear rank selection was adopted to select superior individuals for EDA. An effective probabilistic model was used to explore the solution space. To improve the convergence property and the blindness of EDA, the path relinking technique was incorporated to guide the search process. A local search method was also introduced to exploit the solution space, and provided an appropriate balance between exploration of the global search and exploitation of the local search. Finally, a diversity-maintaining scheme was used to prevent the deterioration of the population. The influence of parameter settings was investigated using a design of experiments approach. The significant role of path relinking for promoting the performance of EDA was also demonstrated. An extensive comparison of P-EDA against other well-performing algorithms was carried out to validate the performance of P-EDA. The experimental results and statistical analyses showed that P-EDA outperformed the recently published methods by a wide statistical margin. In future research, the P-EDA will be applied to solve the BFSP with the total flow-time criterion, the BFSP with the total tardiness criterion or multi-objective BFSP. With regard

to multi-objective BFSP in particular, to the authors' knowledge, no one has solved this problem so far.

# Disclosure statement 

No potential conflict of interest was reported by the authors.

## Funding

This research was supported by the National Natural Science Foundation of China under [grant number U1433116]; Fundamental Research Funds for the Central Universities under [grant number NP2017208]; Funding of Jiangsu Innovation Program for Graduate Education under [grant number KYLX16_0382]; and Postgraduate Research \& Practice Innovation Program of Jiangsu Province [grant number KYCX17_0287].
