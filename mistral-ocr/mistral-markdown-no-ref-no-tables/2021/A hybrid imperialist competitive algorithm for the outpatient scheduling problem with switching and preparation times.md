# A hybrid imperialist competitive algorithm for the outpatient scheduling problem with switching and preparation times 

Hui Yu ${ }^{1}$, Jun-qing Li ${ }^{1,2^{*}}$, Yu-yan Han ${ }^{2}$, Hong-yan Sang ${ }^{2}$<br>1. School of Information Science and Engineering, Shandong Normal University, Jinan 250014, China<br>2. School of Computer, Liaocheng University, Liaocheng 252059, China<br>*Corresponding author's e-mail: lijunqing@lcu-cs.com


#### Abstract

In recent years, outpatient scheduling problem has attracted much attention. This paper considers the outpatient scheduling problem as an extension of the flexible job shop scheduling problem (FJSP), where the patient is considered as a job. Then, to solve the outpatient scheduling problem, a hybrid imperialist competitive algorithm (HICA) is proposed. In the proposed algorithm, the simulated annealing (SA) algorithm and estimation of distribution algorithm (EDA) are embedded to improve the quality of the solution. Furthermore, the two realistic constraints, i.e., switching time and preparation time of patients are also considered to make the problem closer to the reality. Finally, to verify the performance of the proposed HICA, different outpatient scheduling problem instances are randomly generated and used for simulation tests. Four efficient algorithms, including imperialist competitive algorithm (ICA), improved genetic algorithm (IGA), EDA, and modified artificial immune algorithm (MAIA), are selected for detailed comparisons. The simulation results confirm that the proposed algorithm can solve the outpatient scheduling problem with high efficiency.


Key Words: Flexible job shop scheduling, Outpatient scheduling, Imperialist competition algorithm, Simulated annealing algorithm, Estimation of distribution algorithm

## 1 Introduction

Hospitals are critical elements of health care systems and access to their services is very competitive around the world. As the core department of hospital, outpatient service is considered as the "door face" of the hospitals, accounting for a large proportion of hospitals' expenditures and profitability. Outpatient service, however, is very challenging due to its conflicted preferences and priorities from many stakeholders and limited resources to meet the needs [1]. In response, scheduling is introduced to optimize outpatient visits.

Scheduling problems have been investigated in recent years and have been utilized in many practical problems [2]. This study focuses on the outpatient scheduling problem that consider the switching and preparation times of patients. The seemingly simple task of scheduling patients into the consultation session of a doctor is key in ensuring cost-effective health care and patient satisfaction [3]. Therefore, effective outpatient scheduling is important for hospitals to treat patients quickly and efficiently and to use their resources wisely. By more efficiently utilizing the existing hospital resources, it may be possible to increase the number of patients a hospital would otherwise treat, or reduce the number of resources that are required to meet given demands [4].

The layout of the problem we study and processing route

[^0]of patients lends itself well to the flexible job shop scheduling problem. To tackle this outpatient scheduling problem with switching and preparation times, a hybrid imperialist competitive algorithm (HICA) is developed. In the algorithm, first, the diversified assimilation strategy is adopted to enhance the exploitation abilities. After assimilation, the simulated annealing (SA) algorithm and estimation of distribution algorithm (EDA) are embedded to improve the global search ability of the algorithm. Then, four kinds of neighborhood search strategies are introduced to generate new promising solutions. Two different probability models in EDA are employed to enhance the global search abilities. Finally, the empires invasion strategy is proposed to alter the power of the empires, and therefore the population diversity capabilities can be enhanced. Due to the intractability of the model on large instances, a position-based mathematical model is adopted and we employ an exact solver IBM ILOG CPLEX to calculate the model.

## 2 Problem Description

To apply a FJSP approach it is necessary to treat patients as jobs, stages of seeking medical treatment and medical resources correspond to operations and machines. There are a set of patients $J=\left(J_{1}, \ldots, J_{n}\right)$ and a set of medical resources $M=\left\{M_{1}, \ldots, M_{m}\right\}$. Each independent patient $J_{j}$ consists of a sequence of $n_{j}$ stages of seeking medical treatment $O_{j, q}$, where $q=1, \ldots, n_{j}$. Each stage can be processed by a set of medical resources in a certain sequence. Then, the two realistic constraints, i.e., the switching time and preparation time of patients are considered. For convenience of description, the following symbols are defined:


[^0]:    ${ }^{*}$ This research is partially supported by National Science Foundation of China under Grant 61773192, 61803192, and 61773246, Shandong Province Higher Educational Science and Technology Program (J17KZ005), and major Program of Shandong Province Natural Science Foundation (ZR2018ZB0419).

$C_{n u} \geq C_{c, u} \quad \forall j \in\{1,2, \ldots, n\}$

$$
X_{c, u, c, u, v, v}[0,1]
$$

The objective function is to minimize the makespan. Constraint (1) ensures that each stage of seeking medical treatment uniquely occupies one position on one medical resource among all of the available medical resource. Constraint (2) guarantees that each position of each medical resource is occupied once. Constraint (3) ensures that each stage of seeking medical treatment is operated by an available medical resource. Constraint (4) ensures that $O_{C, q-1}$ is processed by medical resource $k$ when $O_{C, q}$ is processed by medical resource $i$. Constraint (5) is logical precedence constraints that take into account the switching and preparation times of patients. Constraint sets (6)-(7) ensure that each medical resource processes only one stage of seeking medical treatment of patient at a time. Constraint (8) defines the makespan, and constraint (9) defines the values of the decision variables.

## 3 Proposed Algorithm

### 3.1 Framework of HICA

For solving the outpatient scheduling problem in hospital systems, we propose a hybrid ICA, named HICA. The main components of HICA are described in this section. The framework of the HICA is shown in Algorithm 1.

## Algorithm 1. HICA

Generate initial populations.
Construct the initial empires.
While the stopping criterion is not met do
for $x=1$ to $N i m$ do
Mutation strategy.
If $x=1$ do
Assimilation strategy.
else
Assimilation strategy change.
end
Update the empires.
Execute the empires invasion strategy.
end
end

# 3.2 Encoding Scheme 

Encoding explains how to represent a real solution. In this paper, we use the encoding scheme proposed by Zhang et al. [5]. The solution consists of two parts: medical resource selection (MRS) and the treatment stage sequence (TSS), as illustrated in Fig. 1. The MRS part stores the available medical resource number, while the TSS part contains the patient number. Moreover, in the MRS part, the local selection was adopted. In the TSS part, the sequence of all the stages is randomly determined.

![img-0.jpeg](img-0.jpeg)

Fig. 1: Representation of a solution.

### 3.3 Initialization of Empires

In the HICA, countries with better objective functions are imperialists and others are the colonies of these imperialists. The population size (Pop) includes several imperialists ( $\mathrm{Nim})$ and their colonies ( Ncl ). The number of colonies in each empire is expressed as $N C_{t}$, where $x=1,2, \ldots, \mathrm{Nim}$.
pop $=\operatorname{Nim}+N c l$
The roulette wheel selection procedure is used to calculate the power of each imperialist as

$$
\operatorname{power}(x)=\frac{1}{\operatorname{makespan}(x)}
$$

The calculation of the power of the imperialists (colnum) can be normalized as follows.

$$
\operatorname{colnum}(x)=N c l \cdot \frac{\operatorname{power}(x)}{\sum_{t=1}^{T_{\min }} \operatorname{power}(x)}
$$

### 3.4 Mutation Strategy

Mutation is a strategy adopted by imperialists to reduce duplication and increase diversity of solutions. Through many experiments, it could be found that mutation for solutions with higher fitness often obtain better solutions. Therefore, the probability formula of mutation is described as follows:

$$
\eta=\left\{\begin{array}{ll}
1 & F \leq F_{\text {avg }} \\
1-\frac{F-F_{\text {avg }}}{2\left(F_{\text {avg }}-F_{\min }\right)} & F>F_{\text {avg }}
\end{array}\right.
$$

where $\eta$ is the individual's mutation probability, $F$ is the individual's fitness, $F_{\text {avg }}$ is the average individual's fitness, and $F_{\min }$ is the worst individual's fitness. Better individual fitness increases the mutation probability of the individual, enlarges the search space of the individual, and avoids falling into a locally optimal solution. Worse individual fitness reduces the mutation probability of the individual.
We use different mutation methods depending on the component. For the MRS part, mutation is performed by randomly changing the available medical resource of the relevant stage. For the TSS part, the crossover operation is conducted.

### 3.5 Diversified Assimilation Strategy

In the process of assimilation, for the MRS part, the two-point crossover [6] is adopted. First, two points of the imperialist are randomly selected. Then, the elements between the two points are inserted into the corresponding positions of the new colony, and the remaining positions insert the elements of the old colony. For the TSS part adopts the POX crossover proposed by Lee et al. [7]. First, several
numbers are selected at random. Then, the numbers selected from the imperialist are inserted into the new colony, and the remaining numbers are inserted into the new colony according to the position of the old colony.

After assimilation, the enhanced global search heuristic which includes the simulated annealing (SA) algorithm and estimation of distribution algorithm (EDA) is developed. SA can jump out of the local optimal solution and finally tend to the global optimal solution. In the SA, the improving move will be accepted, while the worse move is accepted with a certain probability to help the algorithm escape from the local optima. Therefore, $\lfloor\alpha \times N C_{s}\rfloor$ good colonies improve through the SA strategy. EDA is a relatively new paradigm in the field of evolutionary computation. Due to its effectiveness and global search ability, EDA has already been applied to solve combinatorial optimization problems. $\lfloor\beta \times N C_{s}\rfloor$ poor colonies improve through the global search of the EDA, where $\alpha$ and $\beta$ represent the ratio of colonies improved through SA and EDA, respectively.

### 3.6 Updating of Empires

Through the iterations, colonies may obtain greater power than their imperialists. In this case, the colony with greatest power becomes the new imperialist, colonies under the old imperialist are assigned to the new imperialist, and the old imperialist becomes a colony of the new imperialist. Then, the worst empire is updated by EDA.

### 3.7 Empires Invasion

As empires develop, great changes occur in each empire. To gain more powerful power, some empires may conduct empires invasion strategy, that is, the empire occupies the colonies of other empires to change power.

### 3.8 Neighborhood Structures

The neighborhood structures $N_{1}, N_{2}, N_{3}$, and $N_{4}$ are described below. Neighborhood structure $N_{1}$ is performed by replacing a randomly selected position of the MRS part. Neighborhood structure $N_{2}$ acts on the TSS part, selecting two elements in a random manner and swapping them. Neighborhood structure $N_{3}$ is performed by selecting two positions $r_{1}$ and $r_{2}$ at random, where $r_{1}<r_{2}$, the element is inserted at position $r_{2}$ before $r_{1}$ in the MRS part. Neighborhood structure $N_{4}$ generates a new solution by performing one swap operation two times in the TSS part (Fig. 2).
![img-1.jpeg](img-1.jpeg)

Fig. 2: Examples of neighborhood structures

### 3.9 Simulated Annealing Algorithm

Annealing rate is another important module of the SA. Annealing rate has a significant relation with the acceptance probability of inferior solutions, which can directly affect the speed and accuracy of the SA. The SA algorithm

terminates when the temperature recedes to the specified temperature. The annealing rate function is as follows:
$T(\lambda)=\delta \times T(\lambda-1)$
where $\delta \in(0,1)$ is an annealing rate coefficient; $T(\lambda)$ and $T(\lambda-1)$ are current annealing temperature and previous annealing temperature, respectively; $\lambda$ is the iteration number. The main steps of SA are shown in Algorithm 2.

## Algorithm 2. SA

Input: good colonies
Output: the optimized solution
for $y=1$ to the number of good colonies do
if $T>\Delta T$ do
Execute the neighborhood structure to create a new solution, as discussed in this paper.
if the fitness of the new solution $<$ the current best solution do
Accept this new solution.
else
Calculate the probability of accepting the new solution $(r r)$.
if $r r>0$ do
Accept the worst solution.
end
end
Update the current temperature by (14).
end
end

### 3.10 Estimation of Distribution Algorithm

EDA is a relatively new paradigm in the field of evolutionary computation, which employs explicit probability distributions in optimization [8]. Instead of using the conventional crossover and mutation operations of regular genetic algorithms, EDA adopts a probabilistic model learned from a population of selected individuals to produce new solutions at each generation. Meanwhile, the probability model is updated in each generation with the potential individuals of the new population. In such an iterative way, the population evolves, and finally satisfactory solutions can be obtained [9].

In this paper, two probability matrices $P_{1}$ and $P_{2}$ are designed for the MRS and TSS parts. The element $M_{i, q, i}(L)$ of the MRS probability matrix $P_{1}$ represents the probability of processing stage $O_{j, q}$ is processed by medical resource $i$ in generation $L . m_{j, q}$ represents the array of available medical resources for the $q^{\text {th }}$ stage of seeking medical treatment of patient $j$. The probability matrix $P_{1}$ is initialized as follows:
$M_{j, q, i}(0)=\left\{\begin{array}{ll}\frac{1}{m_{j, q}} & \text { if } O_{j, q} \text { can be processed by medical resource } i \\ 0 & \text { else }\end{array}\right.$
Element $H_{j, f}(L)$ of TSS probability matrix $P_{2}$ represents the probability that patient $j$ will appear at position $f$ in generation $L$, while $Q$ represents the total number of stages in the TSS part. The probability matrix $P_{2}$ is initialized as $H_{j, f}(0)=1 / \mathrm{Q}$, which ensures that the entire solution space can be sampled uniformly. And then, the probability matrices $P_{1}$ and $P_{2}$ are updated according to the following equations:
$M_{j, q, i}(L+1)=(1-\theta) M_{j, q, i}(L)$
$H_{j, f}(L+1)=(1-\sigma) H_{j, f}(L)$
where $\theta, \sigma \in(0,1)$ are the learning rates of $P_{1}$ and $P_{2}$ respectively.
Sampling is performed through probabilistic models $P_{1}$ and $P_{2}$ to generate new individuals. The main steps of EDA are shown in Algorithm 3.

Algorithm 3. EDA
Input: poor colonies
Output: the optimized solution
While stopping criteria are not satisfied do
for $y=1$ to the number of poor colonies do
A new solution is generated from random sampling of the probabilistic models $P_{1}$ and $P_{2}$.
Compare the newly generated solution to the previous one.
If the new solution is better do
Accept this new solution.
end
end
end

## 4 Simulation Analysis

This section evaluates the effectiveness of the proposed HICA on outpatient scheduling problem. All numerical experiments have been conducted on a Lenovo PC with a 3.3-GHz processor and 4-GB memory running Windows 7. The FJSP approach has been coded in C++ to add speed and robustness.

### 4.1 Experimental Parameters

The algorithm has four important parameters: the country size pop, the ratio of the imperialist to countries Nim/pop, the ratio of good colonies improved through SA $\alpha$, and the ratio of poor colonies improved through the EDA $\beta$. The levels of each parameter are listed in Table 1. To evaluate the influence of these parameters on the performance of the HICA, the DOE (Design of Experiment) Taguchi method [10] was used, in which an orthogonal array $L_{1 h}$ is constructed. Then, for each parameter combination, the proposed algorithm independently ran 30 times, and the average fitness value of the algorithm was collected as the response variable. Finally, a factor level trend chart for the four parameters was created based on the obtained data. As seen in Fig. 3, when pop is at level 2, Nim/Pop is at level 1, $\alpha$ is at level 2 , and $\beta$ is at level 1 , the proposed algorithm shows the best performance.

### 4.2 Performance Comparison with Exact Solver CPLEX

To verify the quality of the algorithm for solving outpatient scheduling problem, this section compares HICA and IBM ILOG CPLEX algorithm. The settings for the precision solver were configured as follows. The maximum number of threads was 3 , and the time limit was set to 3 h . For the HICA, due to its ability to obtain a satisfactory solution within an acceptable time, a maximum CPU time of 30 s was applied as a stop criterion. Then, 18 small-scale examples of outpatient scheduling problems are randomly generated based on the practical problems.

Table 1: Key parameter levels.
![img-4.jpeg](img-4.jpeg)

Fig. 3: Factor level trends for the four key parameters.
With an increase in the number of patients and stages, there is an exponential increase in time to solve the problem to optimality on CPLEX because of the NP-hard property [11]. Thus, for the other instances, the optimal solutions cannot be obtained on CPLEX within 3 h . Table 2 presents the comparison results between the proposed algorithm and the CPLEX solver. The first column lists the instance name, the second column lists the best fitness values for each instance. The fitness values for each instance are provided in the fourth and fifth columns, while the sixth and seventh columns provide the deviation of the objective value of each algorithm compared with the best value.

Table 2: Comparison results for the CPLEX solver and HICA.
The following observations can be made from Table 2. (i) For solving the given 18 instances, HICA obtained higher quality solutions than the CPLEX solver. (ii) CPLEX did not solve large-scale examples better than HICA.

### 4.3 Efficiency of the mutation strategy

To verify the effectiveness of the proposed mutation strategy, we performed detailed comparisons of the two
algorithms, namely, the algorithm with all of the components of the proposed HICA except for the proposed mutation strategy (hereafter called the HICA_NMS) and the proposed HICA with all of the components. To determine whether the resulting comparisons were significantly different, we performed a multifactor analysis of variance (ANOVA) [12]. The confidence level was set to $95 \%$. When the p-value was less than 0.05 , the difference between the algorithms was significant, and Fig. 4 indicates that our strategy is effective.
![img-3.jpeg](img-3.jpeg)

Fig. 4: ANOVA of the mutation strategy

### 4.4 Efficiency of the Diversified Assimilation Strategy

Three variants of HICA were constructed. HICA1 did not include the SA strategy, but the remainder of the content was consistent with the HICA. The difference between HICA2 and HICA was that the EDA was eliminated from HICA. HICA3 with the canonical assimilation strategy as described in [13]. The parameters were set, and the running environment was the same as for HICA. Each calculation instance is executed 30 times independently, each for 30 s . Fig. 5 presents the ANOVA results obtained by comparing the four algorithms. It can be concluded from Fig. 5 that the proposed diversified assimilation strategy can obtain significantly better results.
![img-4.jpeg](img-4.jpeg)

Fig. 5: ANOVA results of HICA and its variants

### 4.5 Efficiency of the Empires Invasion Strategy

The empires invasion strategy discussed is another contribution to the proposed algorithm. To evaluate its performance, we compared the following two algorithms: HICA_NEI with all the components except the empires invasion strategy and HICA with all components discussed in Section 3. All other components of the two compared algorithms were identical. Fig. 6 provides ANOVA comparisons of the two methods. The figure indicates that there are significant differences between the compared

methods and that the proposed empires invasion strategy enhances the performance of the proposed algorithm.
![img-5.jpeg](img-5.jpeg)

Fig. 6: ANOVA of the empires invasion strategy

### 4.6 Comparison with Other Algorithms

To further evaluate the performance of the proposed HICA, we selected the following algorithms for comparison: ICA [13], improved GA (IGA) [14], EDA [15], and modified AIA (MAIA) [16]. The five compared algorithms were used to perform 30 independent runs, adopting the same maximum elapsed CPU time of 30 s as the termination criterion. The average fitness values for each instance were collected for detailed comparison. Fig. 7 presents the ANOVA results of the average solutions of the five comparison algorithms, from which it can be concluded that the HICA has better performance in solving the problems studied.
![img-6.jpeg](img-6.jpeg)

Fig. 7: ANOVA results for comparing multiple algorithms

## 5 Conclusion

This study addresses the outpatient scheduling problem with switching time and preparation time. The problem is an extension of the FJSP, where patients are treated as jobs, the stages of seeking medical treatment and the medical resources correspond to the operations and machines. To solve the problem, the HICA is proposed. In the proposed algorithm, first, the diversified assimilation strategy is adopted to enhance the exploitation abilities. After assimilation, the enhanced global search heuristic, which includes the simulated annealing (SA) algorithm and estimation of distribution algorithm (EDA), is developed to improve the global search ability of the algorithm. Then, four kinds of neighborhood search strategies are introduced to generate new promising solutions. Two different probability models in EDA are employed to enhance the global search abilities. Finally, the empires invasion strategy is proposed to increase the diversity of the population.

Future work will focus on the following aspects: i) adding other practical constraints or optimizing multiple objectives in the outpatient scheduling problem; ii) considering the
insertion and handling of acute patients; iii) improving the balance between the algorithm's development and exploration abilities.
