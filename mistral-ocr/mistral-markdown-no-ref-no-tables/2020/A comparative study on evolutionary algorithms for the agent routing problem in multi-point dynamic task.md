# A comparative study on evolutionary algorithms for the agent routing problem in multi-point dynamic task 

Sai Lu<br>School of Automation, Beijing Institute of Technology, Beijing, China<br>Email: 2220170505@bit.edu.cn

## Bin Xin*

Key Laboratory of Intelligent Control and
Decision of Complex Systems,
Beijing Institute of Technology,
Beijing, China
Email: brucebin@bit.edu.cn
*Corresponding author

## Lihua Dou

Beijing Advanced Innovation Center for
Intelligent Robots and Systems,
Beijing Institute of Technology,
Beijing, China
Email: doulihua@bit.edu.cn

## Ling Wang

Department of Automation,
Tsinghua University,
Beijing, China
Email: wangling@tsinghua.edu.cn


#### Abstract

The agent routing problem in multi-point dynamic task (ARP-MPDT) proposed recently is a novel permutation optimisation problem. In ARP-MPDT, a number of task points are located at different places and their states change over time. The agent must go to the task points in turn to execute the tasks, and the execution time of each task depends on the task state. The optimisation objective is to minimise the time for the agent to complete all the tasks. In this paper, five evolutionary algorithms are redesigned and tried to solve this problem, including a permutation genetic algorithm (GA), a variant of the particle swarm optimisation (PSO) and three variants of the estimation of distribution algorithm (EDA). In particular, a dual-model EDA (DM-EDA) employing two probability models was proposed. Finally, comparative tests confirm that the DM-EDA has a stronger adaptability than the other algorithms though GA performs better for the large-scale instances.

Keywords: multi-point dynamic task; estimation of distribution algorithm; EDA; dual-model.

Reference to this paper should be made as follows: Lu, S., Xin, B., Dou, L. and Wang, L. (2020) 'A comparative study on evolutionary algorithms for the agent routing problem in multi-point dynamic task', Int. J. Automation and Control, Vol. 14, Nos. 5/6, pp.571-592.

Biographical notes: Sai Lu received his BS from the Harbin Engineering University, Harbin, China in 2017, and he is currently pursuing his MAEng in Beijing Institute of Technology, Beijing, China. His current research interests include manufacturing scheduling and intelligent optimisation methods.

Bin Xin received his BS in Information Engineering and PhD in Control Science and Engineering, both from the Beijing Institute of Technology, Beijing, China in 2004 and 2012, respectively. He was an Academic Visitor at the Decision and Cognitive Sciences Research Centre, University of Manchester from 2011 to 2012. He is currently a Professor with the School of Automation, Beijing Institute of Technology. His current research interests include search and optimisation, evolutionary computation, combinatorial optimisation and multi-agent systems. He is an Associate Editor of the Journal of Advanced Computational Intelligence and Intelligent Informatics and the journal Unmanned Systems.

Lihua Dou received her BS, MS and PhD in Control Theory and Control Engineering from the Beijing Institute of Technology, Beijing, China in 1979, 1987 and 2001, respectively. She is currently a Professor at the Control Science and Engineering at State Key Laboratory of Intelligent Control and Decision of Complex Systems, School of Automation, Beijing Institute of Technology. Her research interests include multi-objective optimisation and decision, pattern recognition and image processing.

Ling Wang received his BSc and PhD from the Department of Automation, Tsinghua University, China in 1995 and 1999, respectively. Now, he is a Full Professor at the Department of Automation, Tsinghua University. His research interests include theories and algorithms for intelligent optimisation and scheduling. He has authored five academic books and over 200 refereed papers. He was a recipient of the Outstanding Paper Award at the International Conference on Machine Learning and Cybernetics in 2002, Best Paper Award at International Conference on Intelligent Computing in 2011, Top Cited Article Award by Engineering Applications of Artificial Intelligence (Elsevier), National Natural Science Award (second place) in 2014, Science and Technology Award of Beijing City in 2008, and Natural Science Award (first place in 2003 and second place in 2007) nominated by the Ministry of Education (MOE) of China.

This paper is a revised and expanded version of a paper entitled 'A comparative study on evolutionary algorithms for the agent routing problem in multi-point dynamic task' presented at Intelligent Simulation Optimization and Scheduling, Changsha, China, 14-16 September 2018.

# 1 Introduction 

The agent routing problem in the multi-point dynamic task (ARP-MPDT) is a novel permutation combinatorial optimisation problem ( Lu et al., 2018). In this problem, the agent visits all task points distributed at different locations only once and completes each task with dynamic state. When the state of each task changes over time, the time cost for the agent to finish the task will change dynamically. The agent spends time on moving between two task points and executing each task. We call the two parts as the travelling time and the execution time, respectively. The objective is to find an agent's route to minimise the total time consisting of the travelling time and the execution time. If the execution time is neglected, we can find that ART-MPDT will degenerate into the travelling salesman problem (TSP) (Chen and Chen, 2011; Tang et al., 2013). Therefore, TSP can be considered as a special case of ARP-MPDT. As a NP-hard problem, ARP-MPDT has been rarely researched. However, many real-world tasks can be abstracted as ARP-MPDT such as fire fighting, disaster relief and large area searching.

Different evolutionary algorithms are tried and designed to solve this problem including estimation of distribution algorithm (EDA), genetic algorithm (GA) and particle swarm optimisation (PSO) algorithm. Evolutionary algorithms have been widely applied in different areas (Panigrahi et al., 2007; Bhaduri and Banerjee, 2011; Abderrezek et al., 2019; Chaudhary et al., 2015). Currently, in order to effectively solve nonlinear equations system (NES), a general framework based on the dynamic repulsion technique and evolutionary algorithms was proposed (Gong et al., 2018; Liao et al., 2018). As a rising evolutionary algorithm, EDA is an effective optimisation method to solve combinatorial optimisation problems (Lozano et al., 2006; Wang and Fang, 2012; Wang et al., 2013). The node histogram matrix (NHM) was introduced and it is suitable to solve the quadratic assignment problem (QAP) and the linear ordering problem (LOP) very well (Ceberio et al., 2012). The edge histogram matrix (EHM) was also introduced, and it matches the TSP and the flow shop scheduling problem (FSSP) better than NHM. In this paper, in view of the coexistence of execution time and travelling time in ARPMPDT, the EDA employing both NHM and EHM (DM-EDA) is proposed to solve the agent routing problem (Zhong et al., 2010). The selection ratio of the two models is regulated dynamically. In GA, an adaptive crossover operator and a mutation operator are designed to adjust the crossover probability and the mutation probability of each chromosome, respectively. The random key technique in continuous PSO is applied to transform the continuous search space to a permutation-based space (Baioletti et al., 2017).

In this paper, the problem was described in detail firstly. Then, the five algorithms were successively designed to solve this problem, and the data results were comprehensively analysed. Finally, the stronger adaptability of DM-EDA than the other algorithms was confirmed.

## 2 Problem description

In order to simplify the model of the problem and highlight the research focus, the actual task model will be simplified and the key parameters are extracted. So, before the models are established, the following assumptions are made:

a The agent moves at a constant speed on a two-dimensional plane where all task points are located.
b The agent moves between any two task points along a straight line.
c The agent has a constant capacity and is able to complete all tasks.
d The agent leaves from its initial position at $t=0$ to execute its first task.
e After reaching a task point, the agent will reduce the state of the current task to a threshold which means the task is completed.
f Before the current task is completed, the agent is not allowed to go to another task point.

# 2.1 Problem model 

The APP-MPDT can be described as follows. There are multiple tasks which have different initial states to be carried out in different locations. The agent must go to each task point to perform the task. The state of each task changes over time, and its dynamic model can be defined by two parameters: the initial state and the state growth index. After the agent starts to execute the task, the state of this task will decrease because the growth index of the state is changed by the agent. When the state of the task is lower than a threshold, the agent completes this task and leaves for another task point. The agent needs to find a task execution sequence to minimise the total time of completing all tasks.

Table 1 Notations of the model parameters
In this paper, the dynamic model of task $i$ is defined as an exponential function which is determined by $S_{i}, \alpha_{i}$ and $\beta$. The formula is as follows:

$$
S_{i}(t)= \begin{cases}S_{i}(0) \cdot e^{\alpha_{i} \cdot t} & t \leq t_{i}^{r} \\ S_{i}\left(t_{i}^{r}\right) \cdot e^{\left(\alpha_{i}-\beta\right) \cdot\left(t-t_{i}^{r}\right)} & t>t_{i}^{r}\end{cases}
$$

where $i=1,2, \ldots, n$. According to this dynamic model, the execution time $\Delta t_{i}$ can be calculated according to the following formula as long as $t_{i}^{r}$ is given.

$$
\Delta t_{i}=\frac{\ln (\xi)-\ln \left(S_{i}\left(t_{i}^{r}\right)\right)}{\alpha_{i}-\beta}
$$

The distance between $P_{j}$ and $P_{k}$ is $D_{j, k}$, and it can be calculated according to the formula:

$$
D_{j, k}= \begin{cases}\sqrt{\left(x_{j}-x_{k}\right)^{2}+\left(y_{j}-y_{k}\right)^{2}} & j \neq k \\ \infty & j=k\end{cases}
$$

where $j, k=0,1,2, \ldots, n$. The solution of this problem can be represented as a permutation. The search space can be denoted as follows:

$$
\mathbf{z}=\{z(1), z(2), \ldots, z(n) \mid z(i) \in\{1,2, \ldots, n\}, z(i) \neq z(j), \forall i \neq j\}
$$

The schedule of the agent to perform all tasks can be expressed as the following form:

$$
T=\left\{\left(t_{z(1)}^{r}, t_{z(1)}^{l}\right),\left(t_{z(2)}^{r}, t_{z(2)}^{l}\right), \ldots,\left(t_{z(n)}^{r}, t_{z(n)}^{l}\right)\right\}
$$

Given the task access sequence, the schedule of the agent can be calculated one by one from the first variable in $T$ according to the following formulas:

$$
\begin{aligned}
& t_{z(1)}^{r}=\frac{D_{0, z(1)}}{V} \\
& t_{z(i)}^{l}=t_{z(i)}^{r}+\Delta t_{z(i)} \quad i=1,2, \ldots, n \\
& t_{z(i+1)}^{r}=t_{z(i)}^{l}+\frac{D_{z(i), z(i+1)}}{V} \quad i=1,2, \ldots, n-1
\end{aligned}
$$

The objective of this problem is to minimise the total time of executing all tasks. In the other words, the time to leave the last task point needs to be the shortest. The optimisation model of ARP-MPDT is given as follows:

$$
\min f(\mathbf{Z})=t_{z(n)}^{l}
$$

subject to:

$$
\begin{aligned}
& \alpha_{i} \leq \beta \quad \forall i=1,2, \ldots, n \\
& S_{i}\left(t_{i}^{l}\right) \leq \xi \quad \forall i=1,2, \ldots, n \\
& t_{z(i)}^{r} \leq t_{z(i)}^{l} \leq t_{z(i+1)}^{r} \leq t_{z(i+1)}^{l} \quad i=1,2, \ldots, n-1
\end{aligned}
$$

where equation (9) defines the objective function and $t_{z(n)}^{l}$ can be calculated by equations (6), (7) and (8). Equation (10) guarantees that each task can be completed by the agent, and the formula constrains the existence of the solution. Equation (11) means that the agent is not allowed to leave for another point until the current task is finished and the states of task points can be calculated successively by equations (1) and (6).

Equation (12) is the basic constraint of the schedule which ensures the validity of the solution.

# 3 EDAs for ARP-MPDT 

### 3.1 Overview of EDA

EDA is an effective optimisation method to solve permutation optimisation problems (Zhou and Sun, 2007). Its basic procedure is as follows:

Step 1 Initialise a population and the probability model randomly.
Step 2 Calculate the fitness value of each individual.
Step 3 Select individuals (samples) into dominant group according to the selection strategy.

Step 4 Update the probability model using the samples.
Step 5 Generate new individuals according to the sampling strategy.
Step 6 Judge the termination condition. If the termination condition is satisfied, stop the algorithm and output results. Otherwise, go to Step 2.

EDA searches in the solution space by sampling the probability model which expresses the statistical information of the solutions which have better fitness values. So, it is vital to select a suitable probability model of EDA to reflect the problem feature. In EDAs for the permutation optimisation problem, NHM or EHM is frequently-used to collect different statistical information of dominant solutions.

In ARP-MPDT, all of the task points and the available paths between any two task points constitute a graph. Each task access sequence corresponds to the group which consists all the task points and the directed paths from the first task point to the last task point in graph. NHM reflects the absolute position information of task points in the graph, and EHM reflects the statistics of the directed paths in the graph.

In ARP-MPDT, the total time consists the execution time of each task and the travelling time. The execution time depends on the state information of the task and $t_{i}^{r}$, and the travelling time relies on the length of each path. Therefore, it is unreasonable to choose one from NHM and EHM without prior knowledge. For example, when the execution time tasks up most of the total time in an ARP-MPDT, the agent's travelling time is not a primary element. It is better to select NHM as the probability model of EDA to collect the information of individuals in dominant group. Conversely, EHM is suitable for the instance when the travelling time tasks up most of the total time.

In this paper, three variants of EDA with different probability models are designed to solve ARP-MPDT. In EDA1 and EDA2, NHM and EHM are used respectively to describe the feature of this problem and generate new solutions by sampling. Both NHM and EHM are employed in EDA3. All of these algorithms select samples by the truncation selection and initialise the populations by sampling initial probability models. Because of the difference of the probability models in the three EDAs, the methods of updating and sampling probability models are different.

The methods of updating and sampling probability models in EDAs are shown in the following sections.

The notations of EDAs are explained as follows:
$G_{N H M}$ node histogram matrix
$G_{E H M}$ edge histogram matrix
$\lambda \quad$ the selection ratio coefficient of NHM to EHM
$Z \quad$ population containing individuals generated by using NHM and EHM
$N \quad$ the population size
$N_{Z} \quad$ the number of individuals generated by the probability models
$\eta \quad$ proportion of samples to population
$Z_{b} \quad$ the group of samples for updating NHM and EHM
$N_{b} \quad$ the number of individuals in $Z_{b}$
$Z_{e} \quad$ the group in which individuals are generated using EHM
$Z_{n} \quad$ the group in which individuals are generated using NHM
$g_{\max } \quad$ the maximum number of iterations
$g \quad$ the identifier of iteration.

# 3.2 EDA1 

### 3.2.1 Initialisation

In this paper, the initial $G_{N H M}$ is related to the state growth index of each task. It can be initialised as follows:

$$
G_{N H M}=\left[G_{N H M}(i, j)\right]_{i \in \times n}=\left[\begin{array}{cccc}
\alpha_{1} & \alpha_{2} & \cdots & \alpha_{n} \\
\alpha_{1} & \alpha_{2} & \cdots & \alpha_{n} \\
\vdots & \vdots & \ddots & \vdots \\
\alpha_{1} & \alpha_{2} & \cdots & \alpha_{n}
\end{array}\right]
$$

### 3.2.2 Updating NHM

It is necessary to introduce $F_{n}$ as the frequency matrix to save frequency data of $Z_{b}$. $F_{n}$ can be initialised as follows:

$$
F_{n}=\left[F_{n}(i, j)\right]_{i \in \times n}=\left[\begin{array}{cccc}
0 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 0
\end{array}\right]
$$

$I_{n}^{k}(i, j)$ is the indicator function corresponding to the $k^{\text {th }}$ individual in $Z_{b}$ :

$$
I_{n}^{k}(i, j)=\left\{\begin{array}{l}
1, \text { if task } i \text { is the } j^{\text {th }} \text { task finished in the } k^{\text {th }} \text { individual in } Z_{b} \\
0, \text { otherwise }
\end{array}\right.
$$

The procedure of collecting information is showed in equation (16):

$$
F_{n}(i, j)=\sum_{k=1}^{N_{b}} I_{n}^{k}(i, j)
$$

The formula of updating $G_{N H M}$ is as follows:

$$
G_{N H M}(i, j)=\left(1-\mu_{n}\right) \cdot G_{N H M}(i, j)+\mu_{n} \cdot \frac{F_{n}(i, j)}{N_{b}}
$$

where $\mu_{n} \in(0,1)$ denotes the learning rate and $i, j=1,2, \ldots, n$.

# 3.2.3 Sampling method 

The access sequence of each individual is obtained by the roulette wheel. The procedure of generating a new individual based on $G_{N H M}$ is as follows:
Step 1 Set $i=1$.
Step 2 Select task point $k$ according to the elements in the line $i$ of $G_{N H M}$ by the roulette wheel. Let $\mathbf{z}(i)=k$.

Step 3 Set all the elements of the column $k$ in $G_{N H M}$ to zero.
Step 4 Let $i=i+1$ and repeat Steps 2 and 3 until all of the task points are selected.

### 3.3 EDA2

### 3.3.1 Initialisation

In this case, the travelling time dominates the total time and EHM suits this case. $G_{E H M}$ can be initialised as follows:

$$
G_{E H M}=\left[G_{E H M}(i, j)\right]_{n \times n}=\frac{1}{D_{i, j}}
$$

### 3.3.2 Updating EHM

Introduce $F_{e}$ as the frequency matrix to save the frequency information of $Z_{b} . F_{e}$ can be initialised as follows:

$$
F_{e}=\left[F_{e}(i, j)\right]_{n \times n}=\left[\begin{array}{cccc}
0 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 0
\end{array}\right]
$$

$I_{n}^{k}(i, j)$ is the indicator function corresponding to the $k^{\text {th }}$ individual in $Z_{b}$ :

$$
I_{e}^{k}(i, j)=\left\{\begin{array}{l}
1, \text { if task } i \text { is before task } j \text { in the } k^{\text {th }} \text { individual in } Z_{b} \\
0, \text { otherwise }
\end{array}\right.
$$

The procedure of collecting information is showed in equation (21):

$$
F_{e}(i, j)=\sum_{k=1}^{N_{e}}\left\{I_{e}^{k}(i, j)+I_{e}^{k}(j, i)\right\}
$$

The formula of updating $G_{E H M}$ is as follows:

$$
G_{E H M}(i, j)=\left(1-\mu_{e}\right) \cdot G_{E H M}(i, j)+\mu_{e} \cdot \frac{F_{e}(i, j)}{N_{b}}
$$

where $\mu_{e} \in(0,1)$ denotes the learning rate and $i, j=1,2, \ldots, n$.

# 3.3.3 Sampling method 

The roulette wheel is used to sample the probability model to get the access sequence of each individual. The procedure of generating a new individual based on $G_{E H M}$ is as follows:

Step 1 Set $i=1$.
Step 2 Select task point $k$ according to the elements in the line $i$ of $G_{E H M}$ by the roulette. Let $\mathbf{z}(i)=k$.

Step 3 Set all the elements of the column $k$ in $G_{E H M}$ to zero.
Step 4 Let $i=k$ and repeat Steps 2 and 3 until all of the task points are selected.

### 3.4 EDA3

In EDA3, both NHM and EHM are employed to collect the information of individuals and generate new population in which the number of individuals is fixed. EDA3 uses the methods of updating and sampling in EDA1 and EDA2 for reference.

However, because of the coexistence of NHM and EHM, it is necessary to determine the number of individuals generated from NHM and EHM. Therefore, the coefficient $\lambda(g), \lambda \in[0.05,0.95]$ denotes the selection ratio of NHM to EHM in the $g^{\text {th }}$ iteration. This updating method assumes that $\lambda(0)=0.5$. It means that without the prior knowledge, the chance of selecting NHM and EHM is equal. The updating rule is showed as follows:

$$
\lambda(g+1)=\left(1-\mu_{\lambda}\right) \cdot \lambda(g)+\mu_{\lambda} \cdot \frac{\frac{N_{e}}{\lambda(g)}}{\frac{N_{n}}{1-\lambda(g)}+\frac{N_{e}}{\lambda(g)}}
$$

where $\mu_{\lambda}$ denotes the learning rate which is designed to avoid premature convergence. $N_{n}$ is the number of individuals in $Z_{n}$, and $N_{e}$ is the number of individuals in $Z_{e}$.

# 4 GA for ARP-MPDT 

### 4.1 Overview of GA

GA is a random parallel search method which is based on natural selection and genetic inheritance (Zhou et al., 2018; Larrañaga et al., 1999). In GA, individuals (solutions) are represented by character strings or matrices which are often referred as chromosomes. GA relies on the loop of the selection operator, the crossover operator and the mutation operator to find the individual with the best genetic material from the search space.

The procedure of the basic GA is showed as following:
Step 1 Initialise the population of chromosomes.
Step 2 Evaluate the fitness of each chromosome.
Step 3 Select parents from the current population via the selection operator.
Step 4 Choose a pair of parents to execute the crossover operator to create offspring.
Step 5 Execute the mutation operator according to the mutation probability.
Step 6 Judge the termination condition. If the condition is satisfied, stop the algorithm and output the results. Otherwise, go to Step 2.

In this paper, the tournament selection operator is applied to select the population of parents. Through comparing the fitness values of two individuals selected randomly from the population, the better individual will be selected into the population of parents to generate new individuals.

### 4.2 Crossover operator

In order to increase the population diversity in early iteration of GA, the crossover operator should be carried out for more individuals to enhance the global searching ability. However, at the later stage of iteration, in order to keep the better individuals, the crossover probability should be reduced. Therefore, an adaptive adjustment strategy of the crossover operator of each chromosome is introduced. The $i^{\text {th }}$ chromosome in the $g^{\text {th }}$ iteration can be expressed as $S_{i}(g)=\left(S_{i 1}(g), S_{i 2}(g), \ldots, S_{i n}(g)\right)$.

We set the fitness function as $f_{i}(g)=1 / f\left(S_{i}(g)\right)$, and the larger fitness means the better chromosome.

The crossover probability of each chromosome changes as follows:

$$
P c_{i}(g)= \begin{cases}P c_{\max }-\left(P c_{\max }-P c_{\min }\right) \cdot\left(\frac{g}{2 \cdot g_{\max }}+\frac{f_{i}(g)-\text { ave } f i(g)}{2 \cdot\left(\max _{-} f_{i}(g)-\text { ave } f i(g)\right)}\right), & \\ & f_{i}(g)<\text { ave } f i(g) \\ P c_{\max }, & f_{i}(g)<\text { ave } f i(g)\end{cases}
$$

where $P c_{i}(g)$ is the crossover probability of the $i^{\text {th }}$ chromosome, $P c_{\text {max }}$ and $P c_{\text {min }}$ are the maximum value and the minimum value of probabilities. ave $f_{i}(g)$ is the average value of all the fitness values and $\max f_{i}(g)$ is the maximum value of all the fitness in the $g^{\text {th }}$ iteration. In this way, the crossover probability of each chromosome in the $g^{\text {th }}$ iteration can be calculated.

Select two chromosomes $S_{i}(g), S_{j}(g)$ randomly and judge whether the crossover operator will be carried out or not according to the crossover probabilities of both chromosomes.

The crossover operator can be described as follows:
Step 1 Select a continuous gene segment $S s_{i}$ randomly from $S_{i}(g)$.
Step 2 Replace the gene segment of $S_{i}(g)$ with $S s_{i}$ at the same position. The new chromosome completed the crossover operator is the new chromosome called $S c_{i}(g)$.

Step 3 It is hard to ensure that $S c_{i}(g)$ is a permutation. Therefore, it is necessary to adjust the genes of $S c_{i}(g)$.
Step 3.1 Check each gene of $S c_{i}(g)$ which is not in $S s_{i}$ whether is the same as the genes in $S s_{i}$.
Step 3.2 If $k^{\text {th }}$ gene conflict with the gene in $S s_{i}$ and the same gene is located at the $p^{\text {th }}$ position in $S_{i}(g)$, replace $k^{\text {th }}$ gene in $S c_{i}(g)$ with the $p^{\text {th }}$ gene in $S_{i}(g)$.

# 4.3 Mutation operator 

An adaptive mutation operator is introduced to improve the population diversity. The population diversity will decrease with iteration. Therefore, the mutation probability of each increases with iteration. The mutation probability changes as follows:

$$
P m(g)=P m_{\min }+\left(P m_{\max }-P m_{\min }\right) \cdot \frac{g}{g_{\max }}
$$

where $P m(g)$ is the mutation probability in the $g^{\text {th }}$ iteration, $P m_{\max }$ and $P m_{\min }$ are the maximum value and the minimum value of probabilities, respectively. Each chromosome is determined whether to be mutated or not according to the mutation probability. Two genes in the chromosome will switch their positions according to the mutation operator.

## 5 PSO for ARP-MPDT

### 5.1 Overview of PSO

PSO was introduced by Kennedy and Eberhart (1995). PSO is a popular presently swarm inspired method in computational intelligence. The inspiration comes from the study of social behaviour of birds flocking. PSO regards each individual as a particle without mass and volume. These particles are located in the $n$-dimensional space and the positions of the particles are potential solutions to the problem. These particles move at a changing speed in search space to find the best solution. The speed of each particle will be adjusted adaptively through the motion experiences from itself and population. In this paper, a random key technique is applied to transform the search space of continuous PSO to permutation-based space of ARP-MPDT.

The position of particle $i$ after the $g^{\text {th }}$ iteration is $X_{i}(g)=\left(X_{i 1}(g), X_{i 2}(g), \ldots, X_{i 3}(g)\right)$, and the speed is $V_{i}(g)=\left(V_{i 1}(g), V_{i 2}(g), \ldots, V_{i 3}(g)\right)$. The particle $i$ will update its speed and position according to the following formulas.

$$
\begin{aligned}
& V_{i}(g+1)=\omega \times V_{i}(g)+c_{1} \times r_{1} \times\left(\text { pbest }_{i}-X_{i}(g)\right)+c_{2} \times r_{2} \times\left(\text { gbest }-X_{i}(g)\right) \\
& X_{i}(g+1)=X_{i}(g)+V_{i}(g)
\end{aligned}
$$

where $\omega$ is the inertia weight. $c_{1}, c_{2}$ are learning rates and $r_{1}, r_{2}$ are random numbers. pbest $_{i}$ is the best position currently found so far of particle $i$ and gbest is the best position currently found so far of all the particles. In PSO, $c_{1}$ and $c_{2}$ are important in searching.

The procedure of the basic PSO is shown as following:
Step 1 Initialise randomly the position and speed of each particle.
Step 2 Calculate the fitness value of each particle and find out pbest $_{i}$ and gbest.
Step 3 Update the speed and the position according to equations (26) and (27).
Step 4 Judge the termination condition. If the condition is satisfied, stop the algorithm and output the results. Otherwise, go to Step 2.

# 5.2 Random key 

Initially, PSO was introduced for continuous search spaces. However, in this paper, the PSO algorithm is focused on finding the best permutation in discrete space. Therefore, random key decoder is introduced to support the application of PSO to permutation optimisation problem.

The random key creates a unidirectional mapping from the continuous space of PSO to the discrete solution space of ARP-MPDT. That means the solution to ARP-MPDT can be represented by the position of a particle of PSO.

Define the transformation from continuous space to permutation space as follows:

$$
Z=R(X)
$$

where $Z$ is a solution to ARP-MPDT in discrete space and $X$ is the position of a particle in continuous space. The transformation strategy of the random key will sort the elements in $X$ according to the size of each element in ascending order. For example, if $X_{i}=(1.2,3.5$, $0.9,0.5,2.8)$, after sorting, the new sequence will be $(0.5,0.9,1.2,2.8,3.5)$. From this sequence, it is easy to find that 1.2 in $X_{i}$ is at the third place in new sequence. Therefore, 3 corresponds to 1.2 , and similarly 5 corresponds to 3.5 . In this way, the permutation which reflects the position in new sequence of each elements in $X_{i}$ is $Z=(3,5,2,1,4)$.

### 5.3 PSO with random key

The flowchart of PSO algorithm employing the random key technique for ARP-MPDT is illustrated in Figure 1.

In this way, PSO algorithm will search the better positions in continuous space. These positions will be transformed to permutations to calculate the objective function values. Then, pbest $_{i}$ and gbest can be found out via the objective function to update the positions and speeds of all the particles.

Figure 1 Flowchart of PSO for ARP-MPDT
![img-0.jpeg](img-0.jpeg)

# 6 Experimental studies 

In the following section, we introduce the setup of the experiments and the analysis of the results. Table 2 shows the execution parameters set of the EDAs. Table 3 shows the execution parameters set of the GA. Table 4 shows the parameters set of PSO. In this paper, sensitivity analyses of key parameters are executed to enhance the performance in the following section, and the other parameters are set empirically. In order to ensure the fairness of design of experiments, the value of the common parameters in these algorithms is kept the same.

Eleven instances are randomly generated to compare the five algorithms. Each instance has different agent parameters and different task parameters. The agent parameters include the initial position, the capability parameter and the speed. The task

parameters consist of the number of the tasks, the position, the initial state, and the state growth index of each task. The data have been uploaded on https://github.com/oksaisai/IJAAC.

Table 2 Parameters setting of the EDAs

Table 3 Parameters setting of the GA

Table 4 Parameters setting of the PSO

For each algorithm and problem instance, 20 runs have been completed. These tests were carried out on a computer configured as Inter(R) Xeon(R) CPU E5-2620 v4, 32 GB RAM, Windows 7 operation system.

# 6.1 Parametric sensitivity analysis 

In this section, several tests are carried out to analyse the sensitivity of different algorithms to part of their key parameters. An instance where the number of tasks is 8 was tested by different algorithms with different parameters.

EDAs whose learning rate is set to the member in $(0.1,0.2, \ldots, 0.9)$ successively are used to solve the instance. The optimisation results of EDAs are shown in Figure 2, Figure 3 and Figure 4. It is easy to find that a smaller learning rate of EDAs makes them perform better.

PSO using different $c_{1}$ and $c_{2}$ is applied to solving the instance. The results are shown as the three-dimensional graph in Figure 5. From Figure 5, we can find that most areas with better objective values are located at the place where $c_{1}$ is larger and $c_{2}$ is smaller; for instance, $c_{1}=3$ and $c_{2}=0.6$.

Figure 2 Sensitivity analysis in EDA1 (see online version for colours)
![img-2.jpeg](img-2.jpeg)

Figure 3 Sensitivity analysis in EDA2 (see online version for colours)
![img-2.jpeg](img-2.jpeg)

Figure 4 Sensitivity analysis in EDA3 (see online version for colours)
![img-3.jpeg](img-3.jpeg)

Figure 5 Sensitivity analysis in PSO (see online version for colours)
![img-4.jpeg](img-4.jpeg)

# 6.2 Comparative experiments 

In this section, a large number of experiments are carried out. The five algorithms are applied to solving the eleven instances. Table 5 shows the average value and standard deviation of the objective value and running time of each experiment. The value before ' $\pm$ ' of the first data in each unit is the average objective value and the value after ' $\pm$ ' is the standard deviation. The value before ' $\pm$ ' of the second data in each unit is the average time consumption and the value after ' $\pm$ ' is the standard deviation.

In Table 5, from the data of EDAs, we can find that EDA1 performs better than EDA2 in the larger-scale tests. However, the performance of EDA1 in small-scale tests is worse than EDA2. EDA3 which employs the EHM and NHM has a better search performance. EDA3 can follow closely the best objective value of the other EDAs or performs better than them. The adaptability of the EDA employing single probability model for different instances is poor. From the above analysis, we know that the objective function value consists of the execution time and the travelling time. NHM and EHM are suitable for different instances. This is the reason why the optimisation effects of EDA1 and EDA2 for different instances are different. EDA3 with both of them can adapt to these instances well than the others.

Comparing EDAs, GA and PSO, we can find that for the small-scale instances, EDAs have better performance than the others. However, GA performs well in the large-scale tests. PSO has the worst performance in these algorithms. Compared with GA, EDAs rely on the probability model and the probability model needs a lot of the samples of the better solutions. So, the speed of the convergence will decline. In small-scale tests, the travelling time dominates the whole time, and that results in good effects of EDA2 which considers the edge information. As the scale of the problem increases, the task execution time gradually dominates the total time. So, the performance of EDA1 gradually improved than EDA2. Considering the two factors comprehensively, EDA3 showed strong adaptability in many instances. Because of the lack of mutation operation, it is difficult for EDAs to jump out of the local optimal solution in the large-scale tests. Compared to the other algorithms, PSO applying the random key technique performs worse because of the high inherent redundancy, though consuming shorter running time.

In order to observe the optimisation process and the dynamic changes of key parameters in the algorithms in more detail, the following graphs are shown. The convergence curves of objective value via different algorithms are shown in Figure 6. Comparing the two graphs, it is obvious that EDA2 whose effect is better in Figure 6(a) was unable to adapt to the instance in Figure 6(b). EDA3 and GA had better performances in different instance. In EDA3, an adaptive adjustment strategy is designed and the selection ratio $\lambda$ is the key parameter. The change curve of $\lambda$ is shown in Figure 7. We can find that $\lambda$ tends to 1 which means EDA3 will use EHM more because the individuals generated from EHM have better objective values. In GA, the crossover probability is also adaptively adjusted and its change curve is shown in Figure 8. Overall, from these graphs, EDA3 showed great adaptability and GA had a faster convergence speed.

![img-5.jpeg](img-5.jpeg)

Figure 6 Convergence curves in different instances, (a) $n=30$ (b) $n=100$ (see online version for colours)
![img-6.jpeg](img-6.jpeg)
(a)
![img-7.jpeg](img-7.jpeg)
(b)

Figure 7 The curve of $\lambda$ in EDA3 (see online version for colours)
![img-8.jpeg](img-8.jpeg)

Figure 8 The curve of crossover probability in GA
![img-9.jpeg](img-9.jpeg)

# 7 Conclusions 

In this paper, five algorithms are designed to solve the novel problem, ARP-MPDT. The objective function value is given by the travelling time and the dynamic execution time. After being tested in 11 instances, the EDA3 employing NHM and EHM is demonstrated the better adaptability to ARP-MPDT than the other EDAs. The selection proportion of NHM and EHM contributes much to the better performance. GA has a stronger competitiveness in large-scale instances. PSO has poor effect in searching the solution space. In the future, for EDAs, the adoption of local search and knowledge should be taken into consideration.

## Acknowledgements

This work was supported in part by the National Key R\&D Program of China (2018YFB1308000), in part by the National Outstanding Youth Talents. Support Program under Grant 61822304, in part by the National Natural Science Foundation of China under Grant 61673058, in part by the NSFC-Zhejiang Joint Fund for the Integration of Industrialization and Informatization under Grant U1609214, in part by the Foundation for Innovative Research Groups of the National Natural Science Foundation of China under Grant 61621063, and in part by the Projects of Major International (Regional) Joint Research Program of NSFC under Grant 61720106011.
