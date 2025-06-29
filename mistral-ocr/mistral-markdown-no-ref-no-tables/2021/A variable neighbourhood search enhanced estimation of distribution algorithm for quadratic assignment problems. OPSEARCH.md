# A variable neighbourhood search enhanced estimation of distribution algorithm for quadratic assignment problems 

T. G. Pradeepmon ${ }^{1,2}$ (D) $\cdot$ Vinay V. Panicker ${ }^{1}$ (D) $\cdot$ R. Sridharan ${ }^{1}(D)$

Accepted: 13 August 2020
(c) Operational Research Society of India 2020


#### Abstract

Quadratic Assignment Problem (QAP) is one of the most complex combinatorial optimization problems. Many real-world problems such as printed circuit board design, facility location problems, assigning gates to airplanes can be modelled as QAP. Problems of size greater than 35 is not able to solve optimally using conventional optimization methods. This warrants the use of evolutionary optimization methods for obtaining optimal or near optimal solutions for QAPs. This work proposes a hybridization on a univariate Estimation of Distribution Algorithm, namely the Population Based Incremental Learning Algorithm (PBILA), with Variable Neighbourhood Search (VNS) for solving QAPs. The proposed algorithm is employed to solve benchmark instances of QAP and the results are reported. The results of this work reveals that PBILA on its own is not efficient for solving the QAPs. However, when hybridised with VNS, the algorithm performs well providing best known solutions for 95 test instances out of the 101 instances considered. For most of the test instances, the percentage deviation is less than one percentage. The overall average percentage deviation of the obtained solutions from the best-known solutions is $0.037 \%$, which is a significant improvement when compared with state-of-the-art algorithms.


Keywords Quadratic assignment problem $\cdot$ Estimation of distribution algorithms $\cdot$ Variable neighbourhood search

[^0]
[^0]:    Vinay V. Panicker
    vinay@nitc.ac.in
    1 Department of Mechanical Engineering, National Institute of Technology Calicut, Kozhikode, Kerala, India
    2 Department of Mechanical Engineering, Muthoot Institute of Technology and Science, Ernakulam, Kerala, India

# 1 Introduction 

The Quadratic Assignment Problem (QAP) was introduced by Koopmans and Beckmann [61] as a model for the allocation of indivisible resources. Since then, the QAP has been used for modelling applications such as backboard wiring [91], economic problems [55], facility locations [44], turbine balancing [85], placement of electronic components [40], scheduling [78], typewriter keyboard and control panel design [58], university examination scheduling [4], hospital planning [56] and many more. In spite of the extensive research on this problem, QAP still remains as one of the hardest combinatorial optimization problems and is well known for its diverse applications $[8,38,45]$.

Garey and Johnson [47] proved that QAP is NP-Hard and thus, there is no polynomial time algorithm that can solve the problem. QAP instances of size larger than 35 are considered to be very large and cannot be solved in reasonable computational time [8]. QAP is also proven to be very difficult to obtain an approximate solution for large instances with guaranteed performance [52]. The exact QAP solution algorithms are based primarily on dynamic programming, plane algorithm cutting, and branch-and-bound algorithms. Of these, only branch-and-bound algorithms are guaranteed to obtain an optimal solution, which is also guaranteed for size problems below 30 [66], while heuristic and metaheuristic methods provide near-optimal solutions within an acceptable computational time. The set of benchmark instances provided by various researchers are used for assessing the performance of these algorithms. Some of the familiar heuristic and metaheuristics algorithms reported in the literature include Simulated Annealing [72], Genetic Algorithms [5], Tabu Search [31], Ant Colony Optimization [57], Neural Networks [99], Memetic Algorithms [19] and Iterated Local Search [86] and these have been successful in solving QAP, at least to a near optimal solution. In Zaied and Shawky [107], Burkard et al. [26] and Loiola et al. [67] present detailed reviews on QAP with formulations, application areas and solution methodologies.

In the present study, Population-Based Incremental Learning Algorithm (PBILA), a member of Estimation of Distribution Algorithms (EDA), is hybridized with Variable Neighbourhood Search (VNS) and the resulting algorithm is applied for solving the QAP. The EDAs are relatively new variants of Genetic Algorithm in which the crossover and mutation operations are omitted and the new members of the population are generated using a probability distribution of the current population. A VNS incorporating three different neighbourhood structures of QAP is employed to intensify the quality of solutions during the iterations of the EDA. The proposed algorithm is then used to solve the benchmark problems taken from the QAP Library [24].

The rest of the paper is organized as follows: In Sect. 2, the related works about state-of-the-art algorithms for solving QAPs are presented. Section 3 explains the solution methodology adopted focussing on the application of EDA for solving QAPs as well as the Variable Neighbourhood Search procedures. Section 4 describes the experimental setup, the benchmark instances of QAP and the results obtained. Section 5 concludes the paper.

# 2 Related work 

The QAP was introduced in 1957 by Koopmans and Beckmann as a mathematical model for the allocation of indivisible resources where the consideration of the cost of interplant transportation is inevitable for the development of price system [61]. Since its introduction, many researchers have been working on it, developing different formulations, finding new areas of application and evolving new methodologies for finding optimal solutions. Koopmans and Beckmann [61] formulated QAP as a maximization problem in integer linear programming approach. Later, many other formulations such as permutation formulation [15], concave quadratic formulation [18], mixed integer linear programming formulation [77], trace formulation [34], graph formulation [106] and quadratic $0-1$ formulation $[17,103]$ are developed.

The QAP is celebrated for its capability to represent a variety of real-world problems such as plant layout [20], backboard wiring on electrical circuits [22], placement algorithms in VLSI design [41], design of typewriter keyboards and control panels [9], hospital and campus planning [7, 50], ordering of runners in a relay race team [54], ranking of archaeological data [62], the analysis of chemical reactions [43] and many more [23]. Many classical combinatorial optimization problems such as travelling salesman problems [33], graph partitioning problems [60] and maximum clique problems [80] can also be formulated as a QAP.

The QAP has been proven to be of NP-Hard nature and there is currently no polynomial time algorithm available that can optimally solve the problem. Thus, the heuristic and metaheuristic algorithms became popular among researchers working on QAP. There are a number of exact, heuristic and metaheuristic algorithms available in the literature that provide exact and near-optimal solutions for QAP instances. The exact algorithms are guaranteed to provide optimal solutions but are limited to solving only small sized problems. The exact methods used to solve QAPs are Branch-and-Bound [2, 21, 29, 49], Dynamic Programming [98] and Cutting plane algorithms [18]. The heuristic algorithms are quick in providing near-optimal solutions. But the gap between the solution obtained and the optimal solution also increases as the problem size increases [79, 105]. Construction methods [11, 42], limited enumeration methods [101] and methods of improvement $[10,64,71]$ are the different categories of heuristic methods. Metaheuristic methods do not guarantee an optimal solution, but in a short time, regardless of the problem size, a near-optimal solution is guaranteed and the solution obtained may also be the optimal one.

Metaheuristic methods are generic iterative procedures for general purposes that guide a heuristic search for promising regions in the solution space of an optimization problem. These methods can be applied to a wide range of optimization problems to make them adapted to a specific problem relatively fewer modifications are required. Generally, these methods are classified into single solution methods and population-based methods. Genetic Algorithm (GA), Simulated Annealing, Tabu Search, Ant Colony Optimization (ACO), etc., and many hybrid algorithms are among the metaheuristic methods. A number of works that use GA

and its variants to solve QAPs have been reported. Tate and Smith [93] reported good results for small instances of QAP by using simple GA. But simple GA is not able to obtain the best-known solutions for larger size problems of size above 20. A number of researchers hybridized GA with other methods to overcome this shortcoming in order to obtain good solutions for higher-sized instances [6, 37, $39,73,74]$. The literature contains a variety of GA variants that have been used to solve QAPs $[6,12,32,94,104]$.

Burkard and Rendl [25] were the first to use Simulated Annealing to solve QAPs and it was refined by Connolly [30]. Additional Simulated Annealing applications for QAP resolution can be found in [82, 84, 102]. Parallel Simulated Annealing implementations can be found in [81] to improve performance (in some cases up to $50-100$ times better performance can be achieved by parallelization). Simulated Annealing's performance comparison with Tabu Search can be found in Battiti and Tecchiolli [16] and it is argued that Simulated Annealing performs better for comparatively fewer iterations. But, as the complexity of the problem instance increases, more iterations are needed and, in that case, Simulated Annealing is outperformed by Tabu Search. Skorin-Kapov [89] made the first implementation of Tabu Search to solve QAP. Tabu Search is the main candidate for the parallelisation of QAP resolution algorithms and hardware implementations [92]; Matsui et al. [31, 69, 100, 109]. Drezner [36] extended the concentrated tabu search to include more permissible moves for the quadratic assignment problem. There are two extensions suggested and tested. James et al. [59] introduced a cooperative parallel tabu search algorithm (CPTS) where processors exchange information over the course of the QAP solution algorithm.

Gambardella et al. [46] proposed the first implementation of ACO to solve QAP using a HAS-QAP system coupled with a local search. See and Wong [88] provide an in-depth review of ACO concepts, their application, and various ACO algorithms or variants developed to solve QAPs. The literature contains a number of hybrid metaheuristics and variants of simple algorithms. Tseng and Liang [97] proposed a hybrid metaheuristic called ANGEL combining ACO, GA and a local search method with two main phases, namely the ACO phase and GA phase. Over one hundred instances of QAP benchmarks have been tested and the results show that with a high success rate, the proposed algorithm can achieve the optimal solution. Song et al. [90] proposed the Neural Meta-Memes Framework as a combination of various algorithms, namely Tabu Search, Simulated Annealing, Iterated Local Search, and Genetic Algorithm and the proposed framework has been successfully applied to QAPs.

# 3 Solution methodology 

### 3.1 Estimation of distribution algorithms

Estimation of distribution algorithms (EDAs) [13, 63, 68) are a set of relatively new algorithms that explore the solution space by sampling the probabilistic model constructed from the favourable solutions evolved till now. They are considered to

be variants of genetic algorithms in which the reproduction operations, crossover and mutation are replaced with probabilistic sampling. EDAs belong to the class of population-based stochastic optimization algorithms. As in other population-based algorithms, the EDAs also start with an initial random population sampled from the set of all permissible solutions. The members of the population are then ranked according to their fitness value-higher the fitness, better the solution. The subset of most promising solutions is selected from this ranked population using a selection operator. Then the algorithm constructs a probabilistic model from the selected set of promising solutions. The new set of solutions for the next generation is sampled from this model and the algorithm repeats until the termination criterion is satisfied and returns the best solution found over the generations. The common termination criteria adopted are a maximum number of iterations, homogeneous population, or lack of improvement in the solutions for a certain number of iterations. Figures 1 and 2 represent the pseudocode and flowchart for general EDA respectively.

Based on this general procedure, researchers have developed a number of different algorithms for various categories of optimization problems. The basic categorization of EDAs is done based on the complexity of the probabilistic models demonstrating the relationship between the variables. The broad categories of EDAs consist of univariate, bivariate and multivariate models. There are multiple algorithms in each of these categories and a short review of them is given in the succeeding subsections. The different aspects of EDAs have been studied by many and can be obtained from the works of Hauschild and Pelikan [53], Ceberio et al. [27], Pelikan et al. [83] and Santana et al. [87].

# 3.2 Population-based incremental learning algorithm 

Population Based Incremental Learning Algorithm (PBILA) is one of the simplest EDAs, which assumes no dependence among the variables. The statistical model in use is a real-valued vector with each element independently representing the probability of assigning value 1 to each corresponding bit in a binary string (candidate

```
1}\Phi_{0}\leftarrow\mathrm{ Generate the initial population (p individuals)
2 Evaluate the population \Phi
3 k=1
4 Repeat
    a. Ww-l}\leftarrow\mathrm{ Select q \leq p individuals from \Phi_{k-1}
    b. Estimate a new model }\mu\mathrm{ from W}
    c. Wnew}\leftarrow\mathrm{ Sample p individuals from }\mu
    d. Evaluate Wnew
    e. Ww}\leftarrow\mathrm{ Select m individuals from \Phi_{k-1} \cup W
    f. k=k+1
    Until stop condition
```

Fig. 1 Pseudocode of general EDA

![img-0.jpeg](img-0.jpeg)

Fig. 2 Flow chart of general EDA
solution). PBILA starts with a probability vector with all elements set to 0.5 , which means that each bit in a generated individual is set to 0 or 1 with equal probability. During evolution, the value of each element is updated using the best individual in the population and the probability value drifts away from 0.5 , modifying its estimation of the structure of good individuals. Typically, PBILA will converge to a vector with each element close to 0 or 1 . During each generation, the probability vector is updated as per the equation $\Pi(t+1)=(1-\alpha) \cdot \Pi(t)+\alpha \cdot X_{\text {Best }}$, where $\Pi(t)$ represents the probability vector for $t$ th generation, $\alpha$ represents the learning factor, and $X_{\text {Best }}$ is the best solution in the current population. But instead of using the best solution alone, the proposed algorithm uses all solutions in the current generation to update the probability vector. This is continued till the probability vector when rounded, becomes a valid solution [13]. Figure 3 depicts the pseudocode of population based incremental learning algorithm.

There are two decision parameters to be set, viz. (i) The value of the learning rate parameter $(\alpha)$ and (ii) the number of individuals used to update the vector. In the current algorithm, $\alpha$ is set to 0.4 , and the number of individuals is set to half the population size.

# 3.3 Variable neighbourhood search 

The Variable Neighbourhood Search (VNS) is an advancement over the iterated local search method. The VNS was introduced by Mladenovic and Hansen [75] for solving the travelling salesman problem. Since then, many researchers have

1. Initialize a probability vector $\Pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right\}$ with $1 / n$ at each position. Here, each $\pi_{i}$ represents the probability of 1 for the $i^{\text {th }}$ position in the solution.
2. Generate population $\Phi$ of $p$ solutions by sampling probabilities in $\Pi$.
3. Select set $\Psi$ from $\Phi$ consisting of $q$ promising solutions, where $q<=p$.
4. Estimate univariate marginal probabilities $\pi\left(x_{i}\right)$ for each $x_{i}$.
5. For each $i$, update $\pi_{i}$ using $\pi_{i}=\pi_{i}+a\left(\pi\left(x_{i}\right)-\pi_{i}\right)$.
6. Go to step 2 until the termination criterion is met.

Fig. 3 Pseudocode of the population based incremental learning algorithm
adopted VNS to solve several different combinatorial optimization problems. The VNS works with a set of predefined neighbourhood structures of the problem under consideration. By systematically and sequentially exploring these neighbourhoods, VNS finds better solutions. It starts with a single solution known as the incumbent solution. A local search is then employed on the incumbent solution to explore one of its predefined neighbourhoods. The resulting solutions from the local search are compared with the incumbent solution and the best solution found so far becomes the incumbent solution. If the incumbent solution changes during the local search, the local search restarts with the new incumbent solution. If no better solution is found during the local search, the neighbourhood structure changes to the next neighbourhood structure and the local search on this new structure is done. Thus, by systematically and sequentially changing the neighbourhood and using local search, VNS directs the search in a promising direction to obtain better and better solutions [51]. Figure 4 represents the pseudocode for the general VNS algorithm.

The neighbourhood structures selected for implementations in the present research are insertion neighbourhood, swap neighbourhood and 3-permute

1. Select the set of neighbourhood structures $n_{k}$ with $k=1, \ldots, k_{\max }$, that will be used in the search.
2. Provide an initial solution $x$.
3. Set $k:=1$
4. Until $k=k_{\max }$, repeat the following steps:
a. generate a point $x^{\prime}$ at random from the $k^{\text {th }}$ neighbourhood of $x$.
b. apply some local search method with $x^{\prime}$ as the initial solution; denote the obtained local optimum as $x^{\prime \prime}$.
c. if the solution thus obtained is better than the incumbent solution, move there $\left(x:=x^{\prime \prime}\right)$, and continue the search with the current neighbourhood structure; otherwise, set $k:=k+1$.

Fig. 4 Pseudocode of variable neighbourhood search

neighbourhood. Since mutation is considered as the neighbourhood search procedure in GA, most of the neighbourhood structures for permutation problems are the result of mutation operations. The neighbourhood structures considered in this case are obtained through mutation operations on permutation representation of QAP. The three neighbourhood structures are explained in the following subsections.

# 3.4 Insertion neighbourhood 

The insertion neighbourhood is based on insertion mutation. In insertion mutation, an element is randomly chosen from the parent string and is inserted into a randomly selected place [70]. For example, consider the parent string (1 2345 6), and suppose that the randomly selected element is 3 . Then, 3 is removed and inserted back into the string in a randomly selected position, say after 6 . Hence, the resulting offspring is (1 24563 ). The insertion neighbourhood is obtained by inserting all the elements in all the possible positions of the incumbent solution. Thus, in the above example, there are 30 members in the insertion neighbourhood. The pseudocode for obtaining insertion neighbourhood is shown in Fig. 5.

### 3.5 Swap neighbourhood

The swap neighbourhood is based on swap mutation operator. The swap mutation operator randomly selects two elements in the parent string and exchanges them [14]. For example, consider the parent solution string represented by (1 2345 6), and suppose that the second and the fifth elements are randomly selected and swapped which results in the solution string as (1 53426 ). The swap neighbourhood is obtained by selecting all the possible combinations of two elements from the incumbent solution and swapping the two selected elements. For the above example, there are 15 members in the swap neighbourhood. The pseudocode for swap neighbourhood is provided in Fig. 6.

```
INS_pseudo_code
{
    For each element X; in position i of the solution do
    {
    Insert X; in all possible positions other than i in the solution.
    }
}
```

Fig. 5 Pseudocode of insertion neighbourhood generation

```
SNS_pseudo_code
{
    For each position i in the solution
    For each position j >= i+1 in the solution do
    {
    Exchange or swap the elements in positions i and j.
    }
}
```

Fig. 6 Pseudocode of swap neighbourhood generation

# 3.6 3-Permute neighbourhood 

The 3-permute neighbourhood is based on the 3-permute mutation operation. In 3-permute mutation, three consecutive elements are selected randomly and the permutations of these elements replace the initial three elements in the parent string. As a result of this process, there will be five new offsprings and the best among them is selected. For example, consider the parent string (1 23456 ), and select the three consecutive members 1,2 , and 3 . The permutations of these members are: (1 3 2), (2 13 ), (2 3 1), (3 1 2), and (3 2 1). Insert these sub-strings one by one to replace the three members 1,2 , and 3 to generate the neighbourhood members like (1 32456 ), (2 13456 ), (2 31456 ), etc. The 3-permute neighbourhood is generated by selecting all possible combination of three consecutive members in the parent string. All the possible permutations are then inserted back one by one into the incumbent solution to form the 3-permute neighbourhood members. The pseudocode for swap neighbourhood is provided in Fig. 7.

```
3PNS_pseudo_code
{
    For i=1 to (n-2)
    {
    P = Permute [X(i), X(i+1), X(i+2)];
    For j = 1 to 5
    {
        Replace [X(i), X(i+1), X(i+2)] in incumbent solution with P(j);
    }
    }
}
```

Fig. 7 Pseudocode of 3-permute neighbourhood generation

# 3.7 The proposed algorithm 

The PBILA employed here is the same as that described in Sect. 3.2. The pseudocode for the proposed PBILA-VNS is shown in Fig. 8. Here, all the members of the population undergo the VNS procedure before the elite solutions are selected and thus VNS intensifies the search procedure.

### 3.7.1 Illustration of the proposed PBILA-VNS algorithm

Initialize a probability matrix $\Pi$ as $n \times n$ matrix with all values set to $1 / n$. Here, each $(i, j)$ element in the matrix represents the probability that $i$ th department is located in $j$ th location.

$$
\Pi=\left[\begin{array}{lllllll}
1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 \\
1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 \\
1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 \\
1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 \\
1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6
\end{array}\right]
$$

Generate population $\Phi=\left\{\begin{array}{lllllll}5 & 2 & 1 & 4 & 6 & 3 \\ 2 & 3 & 5 & 6 & 1 & 4 \\ & & & \vdots & & & \\ 3 & 5 & 6 & 2 & 1 & 4\end{array}\right\}$ of $p$ solutions by sampling probabilities in $\Pi$.

Run VNS on each of the $p$ solutions.

$$
\Phi=\left\{\begin{array}{lllllll}
3 & 1 & 2 & 4 & 6 & 5 \\
4 & 6 & 5 & 3 & 1 & 2 \\
& & \vdots & & & \\
6 & 5 & 2 & 4 & 1 & 3
\end{array}\right\}
$$

Calculate the objective function value.

1. Initialize a probability vector $\Pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right\}$ with $1 / n$ at each position. Here, each $\pi_{i}$ represents the probability of 1 for the $i^{\text {th }}$ position in the solution.
2. Generate population $\Phi$ of $p$ solutions by sampling probabilities in $\Pi$.
3. Apply VNS on each of the members in the population.
4. Select set $\Psi$ from $\Phi$ consisting of $q$ promising solutions, where $q \diamond=p$.
5. Estimate univariate marginal probabilities $\pi(x)$ for each $x$.
6. For each $i$, update $\pi_{i}$ using $\pi_{i}=\pi_{i}+a\left(\pi\left(x_{i}\right)-\pi_{i}\right)$
7. Go to step 2 until the termination criterion is met.

Fig. 8 Pseudocode of the PBILA-VNS algorithm

$$
\Omega=\left\{\begin{array}{c}
20253 \\
20253 \\
\vdots \\
20361
\end{array}\right\}
$$

Select set $\Psi$ from $\Phi$ consisting of $q$ promising solutions, where $q \leq p$.

$$
\Psi=\left\{\begin{array}{cccccc}
1 & 3 & 2 & 6 & 4 & 5 \\
4 & 6 & 5 & 3 & 1 & 2 \\
& & \vdots & & & \\
6 & 4 & 5 & 1 & 3 & 2
\end{array}\right\}
$$

Estimate univariate marginal probabilities $\pi_{(i, j)}^{\prime}$ for each $(i, j)$ using $\Psi$.
For calculating univariate marginal probabilities, convert each solution in $\Psi$ to the corresponding permutation matrix. For example,

$$
\left[\begin{array}{lllllll}
1 & 3 & 2 & 6 & 4 & 5
\end{array}\right]=\left[\begin{array}{llllll}
1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0
\end{array}\right]
$$

Add the permutation matrices and divide it by $n$ to obtain $\Pi^{\prime}$

$$
\text { i.e., } \Pi^{\prime}=\frac{1}{12}\left[\begin{array}{cccccc}
2 & 0 & 5 & 2 & 0 & 3 \\
5 & 0 & 2 & 3 & 0 & 2 \\
0 & 7 & 0 & 0 & 5 & 0 \\
3 & 0 & 2 & 5 & 0 & 2 \\
2 & 0 & 3 & 2 & 0 & 5 \\
0 & 5 & 0 & 0 & 7 & 0
\end{array}\right]
$$

For each $(i, j)$, update $\Pi$ using $\pi_{(i, j)}=\pi_{(i, j)}+\alpha\left(\pi_{(i, j)}^{\prime}-\pi_{(i, j)}\right)$.
![img-1.jpeg](img-1.jpeg)

Repeat steps $2-5$ until the termination criterion is satisfied. The termination criterion used is the number of iterations and its value is $10 \times$ number of facilities. Save the solution with the lowest cost. There are multiple solutions for the above problem with a total cost of 20,253 and one of them is (1 32564 ).

# 4 Computational study 

The QAP library, QAPLIB (http://anjos.mgi.polymtl.ca/qaplib/ or https://www.opt. math.tugraz.at/qaplib/) provides a number of benchmark instances of QAPs presented by Burkard et al. [24]. The test instances can be categorised into four depending on the type of instances they represent. The four types are as follows:

- Type I-Unstructured and randomly generated instances
- Type II—Instances with grid distances
- Type III—Real-life instances
- Type IV—Real-life like instances.

Out of the total 134 problems provided in the QAP library, 101 problems which include the QAPs of size up to 50 are considered in the present research.

The algorithms are coded in MATLAB and the programme is run in PCs with Intel Core i3 Processor with 4 GB RAM and running on windows 7. Each problem is solved ten times and the best, worst and average results are reported. The percentage deviation from the known best solution is also calculated. The results are given in Tables 1, 2, 3 and 4.

Tables 1, 2, 3 and 4 provide the results obtained while solving the QAP benchmark instances of category Type I to Type IV respectively using the PBILA and PBILA-VNS algorithms.

Out of the total 101 test instances solved PBILA is able to obtain BKS for only six problems whereas PBILA-VNS is able to obtain BKS for 95 problems. For 49 test instances the PBILA-VNS is able to get the known best solution in all the ten trials. Only for a single problem the minimum solution obtained showed a deviation of more than one percent. From this comparison itself, it is evident that the hybridization of PBILA with VNS improves the efficiency of PBILA. Out of the six problems for which the best known solution was not obtained, five belong to the Type I category and one to the Type II category. Moreover, the PBILA-VNS is able to provide best known solution for all the real-life instances (Type III category) and real-life like instances (Type IV category).

### 4.1 Comparison with state-of-the-art algorithms

In order to compare the performance of the proposed PBILA-VNS algorithm, it is compared with some of the recent state-of-the-art algorithms published in the literature. The algorithms considered for the comparative analysis are:

1. Backtracking Search Algorithm (BSA) [108]
2. BSA with Iterated Local Search (BSAL) [108]
3. MultiStart Hyper-heuristic Algorithm (MSH-QAP) [35]
4. Great deluge and tabu search hybrid with two-stage memory support (TMSGDQAP) [1]

![img-2.jpeg](img-2.jpeg)

![img-3.jpeg](img-3.jpeg)

5. Parallel Hybrid Algorithm (PHA) [95]
6. Fully Informed Parallel Genetic Algorithm (QAP-IPGA) [96]
7. Biogeography-Based Optimization Algorithm hybridized with Tabu Search (BBOTS) [65]
8. Breakout Local Search Algorithm using OpenMP (BLS-OpenMP) [8]
9. Graphics Processing Unit Algorithm using Level-2 Reformulation-Linearization Technique (GPU-QAP) [48]
10. Improved Hunting Search Algorithm (IHuS) [3]
11. Eight variants of Evolutionary Algorithm Using Conditional Expectation Value (PMX, PMX2, OX, OXI, POX, POX2, MUT and MUT1) [28]
12. Parallel Water Flow Algorithm with Local Search (WFA) [76].

The performance of PBILA-VNS is compared with that of algorithms available in literature and the results are provided in Table 5, 6, 7 and 8.

Table 5 provides the comparison of the algorithms with respect to their ability to solve the Type I QAP instances. MSH-QAP proposed by Dokeroglu and Cosar [35] is the only algorithm which provides solutions to all the Type I test instances considered for the study and the algorithm is able to provide BKS for 18 test instances and the PBILA-VNS is able to provide BKS for 15 test instances out of the 20 test instances considered. Thus, MHS-QAP outperforms the PBILA-VNS it terms of their ability to obtain the BKS for Type I QAP instances. The average percentage deviation of the obtained solutions from the best-known solutions of Type I test instances is $0.19 \%$.

Table 6 provides the comparison of PBILA-VNS with other algorithms available in literature, in terms of their ability to obtain optimal solutions for test instances falling under the category of Type II. Only TMSGD-QAP proposed by Acan and Ünveren [1] reports percentage deviations from BKS for all the 23 test instances considered in this study. PBILA-VNS and TMSGD-QAP report the same percentage deviation for 22 test instances and for a single test instance the PBILA-VNS fails to obtain the BKS while the TMSGD-QAP is successful. The average percentage deviation of the obtained solutions from the best-known solutions of Type II test instances is $0.01 \%$.

The performance comparison of PBILA-VNS with other algorithms in the literature in terms of solving the Type III category of test instances is presented in Table 7. Fifty test instances of category Type III are considered in this study and PBILA-VNS is able to obtain the BKS for all the test instances. The algorithms MHS-QAP, TMSGD-QAP and WFA reported the BKS for all the 50 test instances and thus PBILA-VNS performs equally with these algorithms. None of the other algorithms reported in the literature report the solution for all the 50 test instances of Type III considered in this study and thus it can be deduced that PBILA-VNS is performing better than other algorithms.

Table 8 depicts the comparative performance of EDA-VNS with other algorithms available in the literature in terms of solving Type IV test instances. For all the eight test instances considered, EDA-VNS is able to obtain the BKS. The MHS-QAP and WFA are the only other algorithm which report solutions for all the test instances and both are able to obtain the BKS for all the test instances under consideration.

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)

![img-13.jpeg](img-13.jpeg)

Thus, combining the results of comparison with the state-of-art algorithms available in the literature, PBILA-VNS is performing equally or better than most of the other algorithms under consideration. There is no single algorithm from the state-of-the-art algorithms considered for comparison performs better than the proposed PBILA-VNS. The overall average percentage deviation of the obtained solutions from the best-known solutions is $0.037 \%$. Moreover, except WFA, none of the other state-of-the-art algorithms reported solutions for 101 QAP benchmark instances considered for this study.

# 5 Conclusion 

In this study, a hybrid algorithm combining PBILA with VNS is proposed to solve one of the most complex combinatorial optimization problems, namely QAP. This study reveals that PBILA on its own fails to obtain the BKS for most of the test instances considered. Out of the total 101 test instances solved PBILA is able to obtain BKS for only six problems. But, when hybridized with VNS, the performance of the algorithm improved drastically. The proposed hybrid algorithm performs well by obtaining the BKS for most of the QAP test instances considered. PBILA-VNS is able to obtain the optimal solution at least once for 95 problems and for 49 test instances the PBILA-VNS is able to get the known best solution in all the ten trials. The results obtained for the PBILA-VNS are then compared with those of the recent state-of-the-art algorithms published in the literature.

From the comparison tables it is found that the proposed algorithm performs better or equally with the algorithms considered for comparison. Thus, this paper opens up a new direction in terms of the design of algorithms for solving complex combinatorial optimization problems. Applying the proposed PBILA-VNS for solving other combinatorial optimization problems can be an extension of this work. Hybridizing PBILA with other local search methods may improve the performance of the algorithm, which can provide a further scope for research.

Authors' contributions All authors contributed to the development of the solution methodologies and the preparation of the manuscript. The first draft of the manuscript and revised manuscript was written by Pradeepmon T. G.; R. Sridharan and Vinay V. Panicker did the editing of the manuscript. All authors read and approved the final manuscript.

Availability of data and material All data used in the work are available in the internet or are adapted from other published materials.

## Compliance with ethical standards

Conflict of interest On behalf of all authors, the corresponding author states that there is no conflict of interest.

Code availability The code used in the work are developed by the authors and can be made available as and when required.
