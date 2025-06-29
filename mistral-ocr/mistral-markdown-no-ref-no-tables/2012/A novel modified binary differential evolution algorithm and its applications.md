# A novel modified binary differential evolution algorithm and its applications 

Ling Wang*, Xiping Fu, Yunfei Mao, Muhammad Ilyas Menhas, Minrui Fei<br>Shanghai Key Laboratory of Power Station Automation Technology, School of Mechatronics Engineering and Automation, Shanghai University, Shanghai 200072, China

## A R T I C L E I N F O

Available online 6 June 2012
Keywords:
Differential evolution
Binary encoding
Probability estimation operator
Numerical optimization
Multidimensional knapsack problem

## A B S T R A C T

Differential Evolution (DE) is a simple yet efficient global optimization algorithm. However, the standard DE and most of its variants operate in the continuous space, which cannot solve the binarycoded optimization problems directly. To tackle this problem, this paper proposes a novel modified binary differential evolution algorithm (NMBDE) inspired by the concept of Estimation of Distribution Algorithm and DE. A novel probability estimation operator is developed for NMBDE, which can efficiently maintain diversity of population and achieve a better tradeoff between the exploration and exploitation capabilities by cooperating with the selection operator. Furthermore, the parameter study of NMBDE is run and the analysis is performed to improve the global search ability and scalability of algorithm. The effectiveness and efficiency of NMBDE was verified in applications to the numerical optimization and multidimensional knapsack problems. The experimental results demonstrate that NMBDE has the better global search ability and outperforms the discrete binary DE, the modified binary DE, the discrete binary Particle Swarm Optimization and the binary Ant System in terms of accuracy and convergence speed.
(c) 2012 Elsevier B.V. All rights reserved.

## 1. 1 Introduction

Differential Evolution (DE), a population-based stochastic optimizer firstly proposed by Storn and Price in 1995 [1], has become a new research hotspot in evolutionary computation. The standard DE algorithm, which is simple yet efficient in global optimization, has been successfully applied in scientific and engineering fields. As a versatile evolutionary algorithm, DE does not require any gradient information so that it is capable of solving non-convex, nonlinear, non-differentiable and multimodal problems. Moreover, there are only two control parameters in the updating formulas of DE, thus it is easy for implementation and parameter tuning. Literatures have reported that DE is superior to Particle Swarm Optimization (PSO) and real-coded Genetic Algorithm (GA) in some real-world applications [2-4].

Due to its simplicity, robustness and effectiveness, DE has attracted more and more attention in recent years, and a number of improved variants have been proposed. First of all, adaptive parameter tuning strategies have been studied and adopted to enhance the performance of DE. Liu and Lampinen [5] proposed a fuzzy adaptive DE which used fuzzy logic controllers to tune control parameters according to the relative fitness values and individuals of the successive generations. Qin et al. [6] proposed a self-adaptive DE algorithm, which enabled DE to switch between

[^0]four different mutant schemes, and consequently it enhanced the performance of the algorithm. Zhang and Sanderson [7] introduced a new DE by implementing a novel mutation strategy with the optimal external archive and adaptively tuning control parameters. In addition, the hybrids of DE with some deterministic optimization techniques or meta-heuristic algorithms were also well addressed, such as the fusion of DE with the interior point algorithm [8], PSO [9], Harmony Search [10], Clonal Selection algorithm [11] and Estimation of Distribution Algorithm [12]. Hybrid DEs usually outperform the original DE as the differential information provided by DE and the optimization information extracted by the cooperating algorithms are combined and used to guide the search. Besides, some other improved techniques were also presented. For instance, Noman and Iba [13] used an adaptive cross-based local search strategy to accelerate the convergence speed of DE where the length of the local search was adjusted based on a hill-climbing heuristic strategy. This algorithm was reported to outperform the standard DE and improved DEs with other cross-based local search strategies. Rahnamayan et al. [14] proposed an opposition-based DE algorithm using the opposition-based learning for population initialization and generation jumping, in which a new parameter, namely the jumping rate, was introduced and a comprehensive study was performed to verify its effectiveness. Das et al. [15] introduced a modified mutation operator to balance the exploration and exploitation ability of DE by linearly combining two different mutation operators, which is inspired by the neighborhood concept in PSO. So far, DEs have been successfully applied in


[^0]:    * Corresponding author.

    E-mail addresses: wangling@shu.edu.cn, shwl_1212@163.com (L. Wang).
    0925-2312/$ - see front matter $\odot 2012$ Elsevier B.V. All rights reserved.
    http://dx.doi.org/10.1016/j.neucom.2011.11.033

filter designing [16], power system planning [17], neural network training [11,18], graph theory problems [19], etc. More details can be found in [20,21].

However, the standard DE and most of its improved variants operate in the continuous space, which are not suitable for solving binary-coded combinational optimization problems. Therefore, several binary DE algorithms were proposed to extend the applications of DE. He and Han [22] presented a binary DE based on Artificial Immune System (AIS-DE), in which the scaling factor was treated as a random bit-string and the trial individuals were generated by Boolean operators. An extra threshold parameter was introduced to improve the performance but weaken the flexibility of AIS-DE as it was significantly problem dependent. Later, Wu and Tseng [23] improved the Boolean mutation operator based on the binary bit-string framework and developed a modified binary DE (MBDE) algorithm. Gong and Tuson [24] proposed a binary-adapted DE (BADE) where the scaling factor was regarded as the probability of the scaled difference bit to take on " 1 ". However, AIS-DE, MBDE and BADE discarded the updating formulas of the standard DE and generated new individuals based on different Boolean operators. Inspired by angle modulated PSO algorithm, Pamparâ et al. [25] proposed a new binary DE named angle modulated DE (AMDE). In AMDE, standard DE was adopted to update the four real-coded parameters of angle modulated function which was used to generate the binary-coded solutions by sampling till the global best solution was found. Thus AMDE actually worked in the continuous space. Chen et al. [26] developed a discrete binary differential evolution (DBDE) where the sigmoid function used in discrete binary Particle Swarm Optimization algorithm (DBPSO) [27] was directly taken to convert the real individuals to bit strings. DBDE searches in the binary space directly so that it is easy to implement, but it is very sensitive to the setting of control parameters. Moreover, the value transformed by the sigmoid function is not symmetrical in DBDE, which results in the deterioration of global searching ability.

In this work, a novel modified binary DE (NMBDE) is proposed which develops a novel probability estimation operator to generate the offspring individuals. On the one hand, NMBDE reserves the updating strategy of the standard DE so that the excellent characteristics of DE such as ease of implementing and tuning parameters are inherited. On the other hand, the proposed probability estimation operator can keep the diversity of population better and is robust to the setting of parameters. Therefore, NMBDE offers a new efficient methodology for discrete binary optimization problems.

This paper is organized as follows. Section 2 gives a brief review of the standard DE. The proposed NMBDE is introduced in detail in Section 3. Then the parameter setting of algorithm is discussed in Section 4. Section 5 presents the applications of NMBDE to the numerical optimization and MKP, where the comparisons of NMBDE with four other binary-coded optimization algorithms, i.e., MBDE, DBDE, DBPSO and the binary Ant System (BAS) [28] on a suite of benchmark functions and MKP instances are conducted. Finally, conclusions are remarked in Section 6.

## 2. The standard DE

The population of the standard DE consists of a group of floating-point encoded vectors randomly initialized in the continuous space. Three evolutionary operators, i.e., the mutation operator, the crossover operator and the selection operator are commonly used for DE to update the population. In the evolutionary process, the mutation operator and crossover operator are used to generate the new trail individual, and the selection
operator chooses the better one between the target individual and its trial alternative for the next generation by comparing their fitness values.

Mutation: There are several mutation schemes in DE, and "DE/ rand/I" as Eq. (1) is the most popular one.
$u_{i j}^{t+1}=x_{t, j}^{t}+F \otimes\left(x_{t, j}^{t}-x_{t, j}^{t}\right)$
In Eq. (1), $u_{i j}$ is the element of the mutant individual $u_{i} ; F$ is the scaling factor which is a positive constant; $t$ is the index of generation; $x_{t, j}, x_{t, j}$ and $x_{t, j}$ are three bits of the randomly chosen individuals with index $r_{1} \neq r_{2} \neq r_{3} \neq i$.

Crossover: The trial individual $v_{i}$ is generated by crossing the target individual $x_{i}$ with its mutant counterpart $u_{i}$. The widely used binomial crossover is defined as the following equation:
$v_{i j}^{t+1}= \begin{cases}u_{i j}^{t+1}, & \text { if }(\text { rand } j \leq C R) \text { or }(j=\text { rand }(i)) \\ x_{i j}^{t}, & \text { otherwise }\end{cases}$
where $v_{i j}$ is the element of the trial individual $v_{i}$ and $C R$ is the crossover probability ranged in $(0,1)$. The randj are a stochastic number uniformly distributed within $(0,1)$; rand $(i)$ are a random integer within $1,2, \ldots, N$ where $N$ is the length of individual; $j$ is the index of the dimensionality with $j=1,2, \ldots, N$.

Selection: The selection operator is defined as the following equation:
$x_{i}^{t+1}= \begin{cases}v_{i}^{t+1}, & \text { if } f\left(v_{i}^{t+1}\right)<f\left(v_{i}^{t}\right) \\ x_{i}^{t}, & \text { otherwise }\end{cases}$
As shown in Eq. (3), the trial individual $v_{i}$ replaces the target individual $x_{i}$ if its fitness value is better. Otherwise, the target individual is reserved in the next generation. Therefore, the population is updated according to these three operators.

## 3. Novel modified binary differential evolution

NMBDE adopts the binary coding scheme and each individual is represented by a bit string denoted as $p x_{i}=p x_{0} \cdot\left|p x_{i j} \in 0,1\right.$; $i=1,2, \ldots, N P: j=1,2, \ldots, N$, where $N P$ is the population size and $N$ is the dimensionality of solution. NMBDE reserves the updating formulas of the standard DE, including the mutation operator, the crossover operator and the selection operator. Since the standard mutant operator generates real-coded vectors not bit strings, a new probability estimation operator is proposed to tackle this problem in NMBDE, into which the mutant operator is integrated.

### 3.1. Probability estimation operator

Inspired by the idea of population based incremental learning (PBIL) algorithm [29], a novel probability estimation operator is proposed and utilized to build the probability model $P\left(p x_{i}\right)=$ $\left(p x_{i, 1}, p x_{i, 2}, \ldots, p x_{i, N}\right)$, which is used to generate the binary-coded mutated individual in NMBDE. However, different from PBIL, NMBDE constructs the multiple probability models at each iteration according to the information extracted from the parent individuals by using the mutant operator. The probability estimation operator $P\left(p x_{i}^{t}\right)$ is defined as the following equation:
$\left\{\begin{array}{l}P\left(p x_{i j}^{t+1}\right)=1 /\left[1+e^{-2 b \times k k 0-0.5 i /(1+2 F)}\right] \\ M O=p x_{t, j}^{t}+F \otimes\left(p x_{t, j}^{t}-p x_{t, j}^{t}\right)\end{array}\right.$
where $F$ is the scaling factor; $p x_{t, 1}^{t}, p x_{t, 2}^{t}$ and $p x_{t, j}^{t}$ are the $j$-th bits of three randomly chosen individuals; $b$, called bandwidth factor, is a positive real constant. As seen, the mutant operator of the standard DE represented as MO is reserved and embedded into

the probability estimation operator in NMBDE. The developed probability estimation operator uses the standard mutation operator to derive the differential information of three parent
![img-0.jpeg](img-0.jpeg)

Fig. 1. The operating of probability estimation operator in NMBDE.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Flowchart of the NMBDE algorithm.
individuals to construct the probability distribution model of the mutant individual to be bit " 1 ". The bandwidth factor $b$ tunes the range and shape of the probability distribution model, and an appropriate $b$ value can improve the search efficiency and maintain population diversity simultaneously.

Then, the corresponding mutant individual $p u_{i}^{t+1}$ of the current target individual $p x_{i}^{t}$ is generated as Eq. (5) according to the probability estimation vector $P\left(p x_{i}^{t}\right)$,
$p u_{i j}^{t+1}= \begin{cases}1, & \text { if } \operatorname{rand}_{i} \leq P\left(p x_{i j}^{t+1}\right) \\ 0, & \text { otherwise }\end{cases}$
where $\operatorname{rand}_{i}^{t}$ ) is a random number; $P\left(p x_{i j}^{t+1}\right)$ is the $j$-th component of the probability vector of the $i$-th target individual.

The mechanism of NMBDE to produce the mutant individual can be depicted in Fig. 1.

### 3.2. Crossover operator

The crossover operator is used to produce the trail individual $p v_{i}=\left(p v_{i, 1}, p v_{i, 2}, \ldots, p v_{i, N}\right)$ by mixing the target individual and its mutant individual. The trial vector $p v_{i}$ can be obtained according to the following equation:
$p v_{i j}^{t+1}= \begin{cases}p u_{i j}^{t+1}, & \text { if }(r \text { and } j \leq C R) \text { or }(j=r \text { and } i) \\ p x_{i j}^{t}, & \text { otherwise }\end{cases}$

Table 1
Probability of being " 1 " for the mutant individual of NMBDE with different values of $F$ and $b=6$.
Table 2
Numerical benchmark functions.

where $r$ and $j, C R$ and $r$ and $i \in\{1,2, \ldots, N\}$ are identical to those defined in standard DE. When a random number is less than the predefined $C R$ or the index $j$ is equal to the random index $r$ and $i$, $p v_{i j}^{r+1}$ takes the value of $p u_{i j}^{r+1}$; otherwise, it is set equal to $p x_{i j}^{r}$. From Eq. (6), it is obvious that at least one bit of the trial individual is inherited from the mutant individual so that NMBDE is able to avoid duplicating individuals and effectively search within the neighborhood.

### 3.3. Selection operator

The selection operator is adopted to determine whether a trial individual can survive in the next generation in NMBDE. $p v_{i}^{t+1}$ replaces $p x_{i}^{t}$ and passes to the next population if its fitness value is better than that of the target individual $p x_{i}^{t}$; otherwise the original individual $p x_{i}^{t}$ is reserved as shown in Eq. (7). Therefore, the selection operator is also called one to one
![img-2.jpeg](img-2.jpeg)

Fig. 3. The success rates of NMBDE with different settings of $F$ and $C R$. (a) $f_{1}$, (b) $f_{2}$, (c) $f_{3}$, (d) $f_{4}$, (e) $f_{5}$ and (f) $f_{7}$.

elitism selection.
$p x_{i}^{t+1}= \begin{cases}p v_{i}^{t+1}, & \text { if } f\left(p v_{i}^{t+1}\right)<f\left(p x_{i}^{t}\right) \\ p x_{i}^{t}, & \text { otherwise }\end{cases}$
In summary, the procedure of NMBDE can be stated as follows:
Step 1: Set control parameters and initialize the population randomly;
Step 2: Generate the binary mutant individuals according to the probability estimation operating as Eq. (4) and Eq. (5);
Step 3: Produce the trial individuals by using the binary crossover operator following Eq. (6);
Step 4: Evaluate the target individual and the corresponding trial individual, and choose the better one to survive into the next generation;
Step 5: If the terminal conditions are met, terminate the iteration; otherwise go to step 2.

Generally, the evolution process terminates if the global optimal solution is found or some exit condition is satisfied, for
instance, the maximum generation is reached or the minimum fitness error is satisfied. The detailed process of NMBDE is depicted in Fig. 2.

## 4. Analysis and discussion

### 4.1. Analysis of the probability estimation operator

Unlike PBB, using the whole population information to construct one probability model, the probability model of NMBDE is built on the three individuals with the mutation operator for each individual. Table 1 shows the corresponding probability models of NMBDE with $F=0.5,1.0$ and 2.0. According to Table 1, we can find that the probability of $(0,1,1),(1,0,1)$ and $(1,1,0)$ with two " 1 " bits and one " 0 " bit are $0.2315,0.0266$ and 0.9975 respectively due to the different sampling order when $F=0.5$. Especially, NMBDE is still able to generate " 1 " bit with a certain probability even when the bits of population are all " 0 "s, and vice versa. These two characteristics of probability estimation operator enable NMBDE to maintain the

Table 3
Experimental results with different bandwidth factor $b$.
population diversity better and escape from the local optima more effectively. Furthermore, the probability model varies with different F. For instance, the probability of being " 1 " is $0.0474,0.1192$ and

Table 4
Parameter settings of NMBDE, DBDE, DBPSO and BAS.
${ }^{*} m$ is the number of ants and $N$ is the length of individuals.
0.2315 for $(0,0,0)$ when $F$ is 0.5, 1.0, and 2.0, respectively. Obviously, $F=2$ is big for NMBDE as the mutation rate achieves 0.2315 which will spoil the performance while a too small $F$ cannot effectively improve the diversity of algorithm. Thus, a proper $F$ as well as $b$ is vital for the search ability of NMBDE, which determines the probability model. However, each probability model is used to create one mutant individual in NMBDE, which is similar to DE, but different from PBIL. Therefore, the risk from wrong probability prediction can be reduced and the optimal information can be maintained effectively with the selection operator.

### 4.2. Parameter analysis

Like standard DE, NMBDE is sensitive to the control parameters, so the value of parameter need be chosen carefully.

Table 5
Results of NMBDE, DBDE, DBPSO, BAS and MBDE on low-dimensional benchmark functions.

Although the parameter setting of DE was discussed and the recommended values were given [30], these values are not appropriate for NMBDE due to the changes in the definition and meaning of parameters. Therefore, it is necessary to conduct the
parameter analysis to understand the mechanism of NMBDE better. However, as the parameter setting is problem dependent, the aim of parameter study here is to find the proper parameter values rather than the optimal values.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Convergence curves of NMBDE, DBDE, DBPSO, BAS and MBDE on the low-dimensional functions.

![img-4.jpeg](img-4.jpeg)

Fig. 4. (continued)

In NMBDE, the crossover rate $C R$ decides the contribution of the mutant individual to the generation of the trial solution; the scaling factor $F$ determines the scale of the differential
information in the mutation operator MO; and the bandwidth factor $b$ tunes the range and shape of the probability estimation operator of NMBDE. Therefore, all three control parameters, i.e.,

![img-5.jpeg](img-5.jpeg)

Fig. 4. (continued)
the crossover rate $C R$, the scaling factor $F$ and the bandwidth factor $b$, have influence on the optimization performance of NMBDE. A suite of 20 well-known functions [14] listed in the Appendix were adopted as the numerical optimization benchmarks in this work, and six of them (i.e., $f_{1}, f_{2}, f_{3}, f_{4}$,
$f_{6}$, and $f_{7}$ ), comprising four unimodal and two multimodal functions, were used for parameter analysis. The characteristics and minima of all functions are presented in Table 2. For a general analysis, the trial-and-error strategy in [31] was adopted for parameter study.

![img-6.jpeg](img-6.jpeg)

Fig. 4. (continued)

Table 6
Results of NMBDE, DBDE, DBPSO, BAS and MBDE on 30-dimensional benchmark functions.

Firstly, the sensitivity of NMBDE on $C R$ and $F$ was test. The bandwidth factor $b$ was set as $b=6.0$. Then $C R$ was tuned from 0.1 to 0.6 with step 0.1 and $F$ was set as $0.2,0.4,0.6,0.8,1.0,2.0$, 5.0 and 10.0 respectively. Each variable was encoded by 20 bits. The population size was 40 and the maximal generation number was set as 3000 . The experiments on each function were repeated 50 times independently.

The success rates of finding the global optima ( $S R$ ) with different parametric settings are shown in Fig. 3. We can find that both $C R$ and $F$ have influence on the performance of NMBDE. High success rates are obtained when $0.1<C R \leq 0.3$ while the performance of NMBDE greatly deteriorates when $C R \geq 0.4$ for unimodal functions. Compared with $C R$, NMBDE is less sensitive to $F$ and the success rates hardly fluctuate in a wide range of $F$ with a proper $C R$. However, it should avoid setting a too big or too small $F$. Obviously, $C R$ and $F$ have not to be set a big value simultaneously, otherwise the local search ability will be spoiled, which results in poor performances.

Based on the results of Fig. 3, $C R \in(0.1,0.3)$ and $F \in(0.2,5)$ are recommended. In this work, $C R=0.2$ and $F=0.8$ were adopted as the default values. Then the bandwidth factor $b$ was set within $\{0,2,4,6,8,10,20,50,100,200,500,1000\}$ to test its influence on the optimization ability. Four performance indicators were taken into consideration, i.e., $S R$, the mean best fitness value, the standard variance of the best fitness value and the mean generation number (MGN). The experimental results of 50 times independent runs are given in Table 3.

The results in Table 3 show that NMBDE is not very sensitive to the bandwidth factor $b$, but the optimal value of $b$ is obviously problem dependent. For $f_{2}$, NMBDE achieves the best performance when $b$ is less than 4 , while $b$ should be more than 6 for NMBDE on other 5 benchmark functions. Based on an overall analysis of experimental results, we suggest that $b$ is set between 6 and 100, and 20 was selected as the default value for $b$ in our work to achieve a balance performance on various problems.

![img-7.jpeg](img-7.jpeg)

Fig. 5. Convergence curves of NMBDE, DBDE, DBPSO, BAS and MBDE on the 30-dimensional functions.

![img-8.jpeg](img-8.jpeg)

Fig. 5. (continued)

Table 7
Experimental results of NMBDE, DBDE, DBPSO, BAS and MBDE on 10.100 MKP instances.
Table 7 (continued)

# 5. Applications of NMBDE 

### 5.1. Parameter settings

In the following section, NMBDE are used to solve the numerical optimization problems and multidimensional knapsack problems to test its optimization ability. In order to compare the solution quality and performance of NMBDE, four binary-coded optimization algorithms, i.e., DBDE [26], DBPSO [27], BAS [28], and MBDE [23] with the recommended parameter values were applied to the both applications as well. Table 4 lists the parameter settings of all the algorithms.

### 5.2. Numerical optimization

Firstly, NMBDE, DBDE, DBPSO, BAS and MBDE were applied to optimize 20 benchmark functions in low-dimension. Then eight functions of them, which can be extended to high-dimension, were increased to 30-dimensions to verify the optimization ability and scalability of the algorithms. Each variable in the solution vector was encoded by 20 bits.

### 5.2.1. Low-dimensional numerical experiment

For low-dimension tests, the maximum generation and the population size of all algorithms were set to 3000 and 40 respectively, and the experiments were repeated for 100 times independently. The numerical results and the $t$-test results are both given in Table 5 where " + " indicates that NMBDE is significantly better than the compared algorithm at the $95 \%$ confidence; "-" means that NMBDE is significantly worse than
the compared algorithm; and " $\approx$ " represents that the difference is not significant. The convergence curves of four algorithms on parts of the benchmarks are drawn in Fig. 4.

Table 5 shows that NMBDE outperforms DBDE, DBPSO, BAS and MBDE on almost all the test functions in terms of search accuracy and convergence speed. Specifically, NMBDE is only inferior to DBDE and MBDE on $f_{2}$ on $f_{10}$, respectively.

From Fig. 4, it is obvious that NMBDE searches out the better solutions and converges faster than the other algorithms on the majority of functions as the proposed probability estimation operator can provide better global searching ability and prevent NMBDE from trapping in the local optima.

### 5.2.2. High-dimensional numerical experiment

On high-dimensional numerical experiment, the population size of all algorithms was set as $N P=200$ and the maximal generation number was 5000 . The experimental results are listed in Table 6 and the convergence curves of the average best fitness values are displayed in Fig. 5, which show that NMBDE is superior to DBDE, DBPSO, BAS and MBDE on all eight high-dimensional benchmark functions. For $f_{9}, f_{17}, f_{18}, f_{19}$ and $f_{20}$, NMBDE searched out the global optima with $100 \%$ success rate with a faster convergence speed as well as MBDE while DBDE, DBPSO and BAS failed to achieve the global best values. However, the highdimension numerical optimization is a very difficult problem as the search space is expanded to $2^{600}$. NMBDE did not find out the optimal values of $f_{1}, f_{8}$ and $f_{9}$, but its solutions are still better than those of DBDE, DBPSO, BAS and MBDE. Therefore, it is fair to claim that NMBDE has the better optimization ability especially for the complicated problems.

### 5.3. Multidimensional knapsack problem

### 5.3.1. Problem definition

The multidimensional knapsack problem (MKP), also called the multi-constraint knapsack problem, is a strongly NP-hard
![img-9.jpeg](img-9.jpeg)

Fig. 6. Convergence curves of NMBDE, DBDE, DBPSO,BAS and MBDE on the MKP instances.

![img-10.jpeg](img-10.jpeg)

Fig. 6. (continued)

![img-11.jpeg](img-11.jpeg)

Fig. 6. (continued)

![img-12.jpeg](img-12.jpeg)

Fig. 6. (continued)

![img-13.jpeg](img-13.jpeg)

Fig. 6. (continued)

defined as the following equations:
$\operatorname{maximize} f(x)=\sum_{j=1}^{n} p_{j} x_{j}$
Subject to $\sum_{j=1}^{n} w_{i j} x_{j} \leq M_{i}$
with $p_{j}>0, w_{i j} \geq 0, M_{i} \geq 0, x_{j} \in 0,1, i=1, \ldots, m ; j=1, \ldots, n$
where $n$ is the number of items; $m$ is the number of knapsack constraints with maximum capacities; $M_{i}$ is the $i$-th maximal resource budget; $w_{i j}$ is the consumption of the $i$-th resource by the $j$-th item; $p_{j}$ is the profit yielded by the $j$-th item. The binary decision variable $x_{j}$ decides the items to be selected. Eq. (8) is the objective function representing the total profit of the selected items and Eq. (9) is the multiple resource constraints.

To deal with the constraints, several methods have been studied and used in evolutionary algorithms to solve MKP [33], such as the repair operator [34,35] and penalty function [36]. The repair operator involving the surrogate relaxation method can transform infeasible solutions into feasible solutions so that it extend the feasible domain and improve the quality of feasible solution which is used in this work.

### 5.3.2. Results and discussions

To investigate the performance of NMBDE, 10.100 MKP instances in the $O B$-library are used as the benchmarks. The control parameters of NMBDE, DBDE, DBPSO, BAS and MBDE are the values given in Section 5.1, but the population size was set to the twice of item number, i.e., $N P=2 n$. The maximum number of iterations was Gmax $=5000$ and 100 independent runs were executed for each MKP instance. The experiment results are shown in Table 7, and the average convergence curves are drawn in Fig. 6.

The results in Table 7 indicate that NMBDE has the best performance on solving the MKP and only NMBDE can search out the global optima on all the 30 instances. Moreover, NMBDE outperforms DBPSO and BAS on all instances while it is inferior to DBDE and MBDE on 3 and 2 cases, respectively. In Fig. 6, we can clearly observe that NMBDE offers the better solution quality and converges to the optima faster than DBDE, DBPSO, BAS and MBDE on most instances.

## 6. Conclusion

This paper presents a novel modified binary DE algorithm for solving binary-coded optimization problems, which is inspired by the concept of Estimation of Distribution Algorithm and standard DE. The updating strategy of the standard DE is reserved in the proposed NMBDE so that the advantages of DE, such as easy implementation and parameter tuning, are inherited. Furthermore, the proposed probability estimation operator can effectively preserve the diversity of population and enhance the global search ability. The efficiency and effectiveness of NMBDE were verified on low-dimensional numerical optimization problems, high-dimensional numerical optimization problems and MKP. The comparisons with discrete binary PSO, binary Ant System, the discrete binary DE and the modified binary DE on the benchmarks demonstrate that NMBDE has the best performances in terms of the search accuracy and convergence speed, especially on the complicated optimization problems.

## Acknowledgment

This work is supported by Research Fund for the Doctoral Program of Higher Education of China (20103108120008), the Projects
of Shanghai Science and Technology Community (10ZR1411800, 10JC1405000 \& 08160512100), National Natural Science Foundation of China (Grant no. 60804052), ChenGuang Plan (2008CG48), Shanghai University "11th Five-Year Plan" 211 Construction Project, Mechatronics Engineering Innovation Group project from Shanghai Education Commission and the Graduate Innovation Fund of Shanghai University (SHUCX102218 and SHUCX112171).

## Appendix. Benchmark functions

(1) Rosenbrock's function:

$$
\begin{aligned}
& \min f_{1}=\sum_{i=1}^{n-1}\left[100 \cdot\left(x_{i}^{2}-x_{i+1}\right)^{2}+\left(1-x_{i}\right)^{2}\right] \\
& \text { subject to }-2.048 \leq x_{i} \leq 2.048
\end{aligned}
$$

The global minimum is located at $(1,1, \ldots, 1), f_{1}^{*}(1,1, \ldots, 1)=0$.
(2) Goldstein \& price problem:

$$
\begin{aligned}
\min f_{2}= & {\left[1+\left(x_{1}+x_{2}+1\right)^{2} \cdot\left(19-14 \cdot x_{1}+3 \cdot x_{1}^{2}-14 \cdot x_{2}+6 \cdot x_{1} \cdot x_{2}\right.\right.} \\
& \left.+3 \cdot x_{2}^{2}\right)\left(30+\left(2 \cdot x_{1}-3 \cdot x_{2}\right)^{2} \cdot\left(18-32 \cdot x_{1}+12 \cdot x_{1}^{2}\right.\right. \\
& \left.\left.+48 \cdot x_{2}-36 \cdot x_{1} \cdot x_{2}+27 \cdot x_{2}^{2}\right]\right)
\end{aligned}
$$

subject to $-2 \leq x_{1}, x_{2} \leq 2$. The global minimum is located at $(0,-1), f_{2}^{*}(0,-1)=3$.
(3) Freudenstein-Roth function:

$$
\begin{aligned}
\min f_{3}= & {\left[-13+x_{1}+\left(\left(5-x_{2}\right) \cdot x_{2}-2\right) \cdot x_{2}\right]^{2} } \\
& +\left[-29+x_{1}+\left(\left(x_{2}+1\right) \cdot x_{2}-14\right) \cdot x_{2}\right]^{2}
\end{aligned}
$$

subject to $-10 \leq x_{1}, x_{2} \leq 10$.
The global minimum is located at $(5,4), f_{3}^{*}(5,4)=0$.
(4) Glankwahmdee's function:
$\min f_{4}=\left(x_{1}^{2}+x_{2}-11\right)^{2}+\left(x_{1}+x_{2}^{2}-7\right)^{2}$, subject to $-10 \leq x_{1}$, $x_{2} \leq 10$. The global minimum is located at $(3,2), f_{4}^{*}(3,2)=0$.
(5) Griewangk's function:

$$
\begin{aligned}
& \min f_{5}=\sum_{i=1}^{n}\left(x_{i}^{2} / 4000\right)-\prod_{i=1}^{n} \cos \left(x_{i} / \sqrt{i}\right)+1 \\
& \text { subject to }-10 \leq x_{i} \leq 10
\end{aligned}
$$

The global minimum is located at the origin $(0,0, \ldots, 0)$. $f_{5}^{*}(0,0, \cdots, 0)=0$
(6) Schaffer F6:

$$
\begin{aligned}
& \min f_{6}=-0.5-\left[\left(\sin \sqrt{x^{2}+y^{2}}\right)^{2}-0.5\right] /\left[1+0.001 \cdot\left(x^{2}+y^{2}\right)\right]^{2} \\
& \quad \text { subject to }-10 \leq x_{1}, x_{2} \leq 10
\end{aligned}
$$

The global maximum is located at the origin. $f_{6}^{*}(0,0, \cdots$, $0)=-1$.
(7) Shubert problem:

$$
\begin{aligned}
& \min f_{7}=\left\{\sum_{i=1}^{5} i \cdot \cos [(i+1) \cdot x+i]\right\} \cdot\left\{\sum_{i=1}^{5} i \cdot \cos [(i+1) \cdot y+i]\right\} \\
& \quad \text { subject to }-10 \leq x_{1}, x_{2} \leq 10
\end{aligned}
$$

There are 18 global minimal solutions. $f_{7}^{*} \approx-186.730908$
(8) Dixon function:

$$
\begin{aligned}
& \min f_{8}=\left(x_{1}-1\right)^{2}+\sum_{i=2}^{n} i\left(2 x_{i}^{2}-x_{i-1}\right)^{2} \\
& \quad \text { subject to }-10 \leq x_{i} \leq 10
\end{aligned}
$$

(9) The global minimum is located at the origin. $f_{8}^{*}(1,0, \cdots, 0)=0$ Pathological function:

$$
\begin{aligned}
\min f_{9}= & \sum_{i=1}^{n-1}\left(0.5+\frac{\sin ^{2} \sqrt{100 x_{i}^{2}+x_{i+1}^{2}}-0.5}{1+0.001\left(x_{i}^{2}-2 x_{i} x_{i+1}+x_{i+1}^{2}\right)^{2}}\right) \\
& -100 \leq x_{1}, x_{2} \leq 100
\end{aligned}
$$

The global minimum is located at $(0,0, \ldots, 0) . f_{9}^{*}(0,0, \cdots, 0)=0$
(10) Ackley's function:
$\min f_{10}=-20 \cdot e^{-0.2 \cdot \sqrt{(1 / \pi) \cdot \sum_{i=1}^{n} x_{i}^{2}}}-e^{(1 / \pi) \cdot \sum_{i=1}^{n} \cos (2 \cdot \pi \cdot x_{i})}+20+e$, subject to $-32 \leq x_{i} \leq 32$.

The global minimum is located at $(0,0, \ldots, 0) . f_{10}^{*}$ $(0,0, \cdots, 0)=0$
(11) Levy function 5 :

$$
\begin{aligned}
\min f_{11}= & \left\{\sum_{i=1}^{5} i \cdot \cos [(i-1) \cdot x+i]\right\} \cdot\left\{\sum_{i=1}^{5} i \cdot \cos [(i+1) \cdot y+i]\right\} \\
& +\left[(x+1.42513)^{2}+(y+0.80032)^{2}\right] \\
& \text { subject to }-10 \leq x_{1}, x_{2} \leq 10
\end{aligned}
$$

The global minimum is located at $(-1.3068,-1.4248)$. $f_{11}^{*}(-1.3068,-1.4248) \approx-176.1375$
(12) Camel back-6 six hump problem:

$$
\begin{aligned}
& \min f_{12}=\left(4-2.1 \cdot x_{1}^{2}+\frac{x_{1}^{4}}{3}\right) \cdot x_{1}^{2}+x_{1} \cdot x_{2}+\left(-4+4 \cdot x_{2}^{2}\right) \cdot x_{2}^{2} \\
& \text { subject to }-10 \leq x_{1}, x_{2} \leq 10
\end{aligned}
$$

There are four global minimal solutions $( \pm 0.0898$, $\pm 0.7126) \cdot f_{12}^{*} \approx-1.03162845$.
(13) Alpine function:

$$
\min f_{13}=-\left[\prod_{i=1}^{n} \sin \left(x_{i}\right)\right] \cdot \sqrt{\prod_{i=1}^{n}\left(x_{i}\right)}, \quad \text { subject to } 0 \leq x_{i} \leq 10
$$

The global maximum is located at $(7.917,7.917)$. $f_{12}^{*}(7.917,7.917) \approx-7.8856$.
(14) Levy function 3:

$$
\min f_{14}=\left\{\sum_{i=1}^{5} i \cdot \cos [(i-1) \cdot x+i]\right\} \cdot\left\{\sum_{i=1}^{5} i \cdot \cos [(i+1) \cdot y+i]\right\}
$$

subject to $-10 \leq x_{1}, x_{2} \leq 10$.
There are 18 global minimal solutions. $f_{14}^{*} \approx-174.5417$.
(15) Beale function:

$$
\begin{aligned}
& \min f_{15}=\left(1.5-x_{1}+x_{1} x_{2}\right)^{2}+\left(2.25-x_{1}+x_{1} x_{2}^{2}\right)^{2} \\
& \quad+\left(2.625-x_{1}+x_{1} x_{2}^{2}\right)^{2}
\end{aligned}
$$

subject to $-4.5 \leq x_{1}, x_{2} \leq 4.5$.
The global minimum is located at $(3,0.5) . f_{15}^{*}(3,0.5)=0$.
(16) Hartman 3 problem:

$$
\begin{aligned}
& \min f_{16}=-\sum_{i=1}^{4}\left(c_{i} e^{-\sum_{i=1}^{3} a_{i} / x_{i}-p_{i} i}\right), \text { subject to } 0 \leq x_{i j} \leq 1 \\
& c=\left[\begin{array}{c}
1 \\
1.2 \\
3 \\
3.2
\end{array}\right], \quad a=\left[\begin{array}{cccc}
3 & 10 & 30 \\
0.1 & 10 & 35 \\
3 & 10 & 30 \\
0.1 & 10 & 35
\end{array}\right]
\end{aligned}
$$

$$
p=\left[\begin{array}{cccc}
0.3689 & 0.117 & 0.2673 \\
0.4699 & 0.4387 & 0.747 \\
0.1091 & 0.8732 & 0.5547 \\
0.03815 & 0.5743 & 0.8828
\end{array}\right]
$$

The global minimum is located at $(0.114614,0.555649$, 0.852547$)$.
$f_{16}^{*}(0.114614,0.555649,0.852547)=-3.86278^{*}$
(17) Sphere function:
$\min f_{17}=\sum_{i=1}^{n} x_{i}^{2}$, subject to $-10 \leq x_{i} \leq 10$. The global minimum is located at the origin. $f_{17}^{*}(0,0, \cdots, 0)=0$
(18) Sum squares function:
$\min f_{18}(x)=\sum_{i=1}^{n} i x_{i}^{2}$, subject to $-5.12 \leq x_{i} \leq 5.12$. The global minimum is located at the origin. $f_{18}^{*}\left(0,0, \cdots, 0\right)=0$
(19) Sum of different power:
$\min f_{19}=\sum_{i=1}^{n}\left|x_{i}\right|^{(i+1)}$, subject to $-1 \leq x_{i} \leq 1$. The global minimum is located at the origin. $f_{19}^{*}\left(0,0, \cdots, 0\right)=0$
(20) Schwefel's poblem 2.22:

$$
\min f_{20}=\sum_{i=1}^{n}\left|x_{i}\right|+\prod_{i=1}^{n}\left|x_{i}\right|, \quad \text { subject to }-10 \leq x_{i} \leq 10
$$

The global minimum is located at the origin. $f_{20}^{*}$ $\left(0,0, \cdots, 0\right)=0$
