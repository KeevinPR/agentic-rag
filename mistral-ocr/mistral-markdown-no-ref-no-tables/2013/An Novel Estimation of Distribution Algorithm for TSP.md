# An Novel Estimation of Distribution Algorithm for TSP 

Fahong Yu ${ }^{1, a}$, Weizhi Liao ${ }^{1,2,4, b}$ and Meijia Chen ${ }^{3, c}$<br>${ }^{1}$ College of Mathematics and Information Engineering, Jiaxing University, Jiaxing, China<br>${ }^{2}$ Guangxi Experiment Centre of Science and Technology,Guangxi University,Nanning 530004, China<br>${ }^{3}$ center of economic managing experiment, Jiaxing University, Jiaxing, China<br>${ }^{4}$ College of Computer and Information Engineering, Guangxi Teachers Education University, Nanning, China<br>${ }^{a}$ fhyu520@126.com, ${ }^{\text {b }}$ weizhiliao2002@yahoo.com.cn, ${ }^{\text {c }}$ mjchen9930@yahoo.cn

Keywords: traveling salesman problem, estimation of distribution algorithms, probabilistic model


#### Abstract

Estimation of distribution algorithms (EDAs) is a method for solving NP-hard problem. But it is hard to find global optimization quickly for some problems, especially for traveling salesman problem (TSP) that is a classical NP-hard combinatorial optimization problem. To solve TSP effectively, a novel estimation of distribution algorithm (NEDA ) is provided, which can solve the conflict between population diversity and algorithm convergence. The experimental results show that the performance of NEDA is effective.


## Introduction

TSP Problem is the most prominent problem in combinatorial optimization; it is a classical NP-hard problem. It has attracted a lot of researchers from various fields, including mathematic, operations research, physics, biology and artificial intelligence, etc. It is the hotspot of research in the optimization field.

There are various many proposed optimization algorithm for solving TSP. Generally, the enumeration is a straightforward method by enumerating all combinations and selecting the shortest distance as the optimal solution. However, the huge amount of computation becomes insurmountable obstacle. Evolutionary algorithm such as algorithm genetic algorithm [1], ant colony algorithm [4], simulated annealing algorithm [2], artificial neural networks, and particle swarm algorithm [3] provides a new evolutionary mode, which opens up new ideas for the traveling salesman problem. Estimation of Distribution Algorithms (EDA) as a stochastic optimization search algorithm based on statistical learning can be used to solving TSP. But specific to TSP, the research is extremely less [4]. This paper proposes an improved estimation of distribution algorithms (NEDA ) for TSP.

## TSP Mathematics Model

First of all, the TSP problem used in this paper is a problem that the traveling salesman must visit every city in his territory exactly once and then return to the starting point. The study of this paper is given the cost of travel between every two cities and the aim is to find the minimum total cost of the entire tour in all possible paths. Its mathematics model is as follows.

$$
\begin{aligned}
& \min \sum_{i \neq j} d_{i, j} x_{i, j} \\
& \text { s.t } \sum_{j=1}^{n} x_{i, j}=1 \quad i=1,2, \cdots n \\
& \sum_{i=1}^{n} x_{i, j}=1 \quad j=1,2, \cdots n \\
& \sum_{i, j \in S} x_{x, j} \leq|S|-1 \quad 2 \leq|S| \leq n-2, S \subset\{1,2, \cdots, n\}
\end{aligned}
$$

$$
x_{i, j} \in\{0,1\} \quad i, j=1,2, \cdots, n \quad i \neq j
$$

Among them, the decision variable $x_{i, j}=1$ in (5) means the businessman's route includes the route from city $i$ to city $j$ while $x_{i, j}=0$ means the businessman has not choose the path. Goal function (1) requires the sum of distances is the minimum. Equation (2) requires businessman come out from city $i$ for one time; Equation (3) requires the businessman-entering city $j$ for only one time. Equation (2), (3) can only guarantee passing each city at a time, but can't guarantee that there is not a circuit. Equation (4) Requires businessman's route cannot form a circuit in any subset of cities and $|S|$ stands for the number of elements in the set $S$.

# Improved Estimation of Distribution Algorithm for TSP 

A proper probability model is the key for EDAs to solve TSP. In this paper, an improved estimation of distribution algorithm was proposed. First of all, select some dominant individuals from the population and constructs the probability matrix for all pairwise adjacent mode. Higher frequency a mode, greater the proportion in the pattern matrix. Finally, sample some new individuals from the mode matrix repeatedly.
(1) Initialize population

In this algorithm, the real number coding was selected. The coding of a city can be set as $x_{i}^{t}=\left(x_{i 1}^{t}, x_{i 2}^{t}, \cdots x_{i n}^{t}\right), i \in\{1,2, \cdots, N\}$ and the distribution of each city probability is initialized as $1 / n$. the probability distribution matrix is presented as $L_{N \times n}^{\prime}$.

$$
L_{N \times n}^{\prime}=\left[\begin{array}{cccc}
x_{11}^{t} & x_{12}^{t} & \cdots & x_{1 n}^{t} \\
x_{21}^{t} & r_{22}^{t} & \cdots & x_{2 n}^{t} \\
\vdots & \vdots & \vdots & \vdots \\
x_{N 1}^{t} & x_{N 2}^{t} & \cdots & x_{N n}^{t}
\end{array}\right]
$$

(1) constructing probability distribution matrix

The course is main to count the adjacent mode frequency statistics of optimal solutions and constructed adjacent pattern matrix $R_{n \times n}$.

$$
R_{n \times n}^{t}=\left[\begin{array}{cccc}
0 & r_{12}^{t} & \cdots & r_{1 n}^{t} \\
r_{21}^{t} & r_{22}^{t} & \cdots & r_{2 n}^{t} \\
\vdots & \vdots & \vdots & \vdots \\
r_{n 1}^{t} & r_{n 2}^{t} & \cdots & r_{n n}^{t}
\end{array}\right]
$$

Where the variable $I$ donates the generation and the variable $r_{i j}^{t}$ donates the probability that the $j$-th city is exist at back of the $i$-th city.

$$
r_{i j}^{t}= \begin{cases}\frac{1}{M} \sum_{k=1}^{M} \delta_{i j}\left(x_{k}^{t}\right), & i \neq j \\ 0, & i=j\end{cases}
$$

Where $i=1,2, \cdots, n: \quad j=1,2, \cdots, n$. The express $\frac{1}{M} \sum_{k=1}^{M} \delta_{i j}\left(x_{k}^{t}\right)$ donates the frequency of the dominant groups in the adjacent mode $i j$.

Algorithm 1 described the framework of the proposed algorithm as follow.
Setp1: Initialize population. Uniform sampling individuals of size $n$;
Setp2: calculate the fitness of each individual in population $\operatorname{Pop}(t)$ according tsp mathematics model;

Setp3: Select $m$ individuals from $\operatorname{Pop}(t)$ as a set $D_{s}$;
Setp4: Construct the probability mode matrix;
Setp5: Sample $n-m$ new individuals and combine the $n-m$ new individuals with m individuals in step 3 to be a next generation population;

Setp6: If termination condition is met, the algorithm will go to end; otherwise, go to step2.

# Experiments and Results Analysis 

For NEDA, assume that the size of population is 50 and take the 100 TSP problem as an example. The computational process is shown in Fig. 1 and the final result is 21282.
![img-0.jpeg](img-0.jpeg)
$\mathrm{t}=0$, length $=150220$
![img-1.jpeg](img-1.jpeg)
$\mathrm{t}=32$, length $=21354$
Fig. 1 The computational process for TSP problem of 100 cities
Fig. 1 has shown the computational process from beginning to the end. In the computational process, we can see the result tend to optimum quickly. It still has cross path when at generation 20 and already very close to global optimization at generation 32. Fig. 1 shows the result is accurate and reliable.

In order to further verify the performance of NEDA, we have also chosen other TSP problems[10] as the test sets. Runs NEDA 20 times each. The results are in table 1.

Table 1 The part results of NEDA
View from table 1, NEDA has achieved the better operation result in the examples above and the stability of NEDA is good. But the algorithms cannot all get the best solution every time. The main reason is the setting of termination conditions of NEDA .

# Conclusions 

In this paper, an improved estimation of distribution algorithm for TSP was proposed. NEDA is an improved algorithm with efficiency and excellent performance in solving traveling salesman problem. On the whole, the proposed algorithm can achieve satisfied solutions, the stability of the algorithm is good and the convergence speed is fast. There is also some problems need further study such as dynamic TSP and others.

## Acknowledgment.

This research is supported by supported by Guangxi Experiment Centre of Science and Technology under grant No. LGZXKF201208.

# Mechatronics, Robotics and Automation 

10.4028/www.scientific.net/AMM.373-375

## An Novel Estimation of Distribution Algorithm for TSP

10.4028/www.scientific.net/AMM.373-375.1089