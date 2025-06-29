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

# References 

1. Acan, A., Ünveren, A.: A great deluge and tabu search hybrid with two-stage memory support for quadratic assignment problem. Appl. Soft Comput. 36, 185-203 (2015)
2. Adams, W.P., Johnson, T.A.: Improved linear programming based lower bounds for the quadratic assignment problem. DIMACS Ser. Discrete Math. Theor. Comput. Sci. 16(1), 43-75 (1994)
3. Agharghor, A., Riffi, M.E., Chebihi, F.: Improved hunting search algorithm for the quadratic assignment problem. Indones. J. Electr. Eng. Comput. Sci. 14(1), 143-154 (2019)
4. Ahmad, F., et al.: Quadratic assignment approach for optimization of examination scheduling. Appl. Math. Sci. 9(130), 6449-6460 (2015)
5. Ahmed, Z.H.: A multi-parent genetic algorithm for the quadratic assignment problem. OPSEARCH, 1-19 (2015a)
6. Ahmed, Z.H.: An improved genetic algorithm using adaptive mutation operator for the quadratic assignment problem. In: Paper Presented at 38th International Conference on Telecommunications and Signal Processing (TSP), 2015, IEEE, 1-5 (2015b)
7. Ahuja, R.K., Orlin, J.B., Tiwari, A.: A greedy genetic algorithm for the quadratic assignment problem. Comput. Oper. Res. 27(10), 917-934 (2000)
8. Aksan, Y., Dokeroglu, T., Cosar, A.: A stagnation-aware cooperative parallel breakout local search algorithm for the quadratic assignment problem. Comput. Ind. Eng. 103, 105-115 (2017)
9. Amico, M.D., et al.: The single-finger keyboard layout problem. Comput. Oper. Res. 36(11), 30023012 (2009)
10. Anderson, E.J.: Mechanisms for local search. Eur. J. Oper. Res. 88(1), 139-151 (1996)
11. Arkin, E.M., Hassin, R., Sviridenko, M.: Approximating the maximum quadratic assignment problem. Inf. Process. Lett. 77(1), 13-16 (2001)
12. Azarbonyad, H., Babazadeh, R.: A genetic algorithm for solving quadratic assignment problem (QAP). Comput. Res. Reposit. abs/1405.5050 (2014)
13. Baluja, S.: Population-based incremental learning: a method for integrating genetic search based function optimization and competitive learning. Technical Report. Carnegie Mellon University (1994)
14. Banzhaf, W.: The "molecular" traveling salesman. Biol. Cybern. 64(1), 7-14 (1990)
15. Barvinok, A., Stephen, T.: The distribution of values in the quadratic assignment problem. Math. Oper. Res. 28(1), 64-91 (2003)
16. Battiti, R., Tecchiolli, G.: Simulated annealing and tabu search in the long run: a comparison on QAP tasks. Comput. Math. Appl. 28(6), 1-8 (1994)
17. Bazaraa, M.S., Sherali, H.D.: Bender's partitioning scheme applied to a new formulation of the quadratic assignment problem. Naval Res. Logist. Q. 27(1), 29-41 (1980)
18. Bazaraa, M.S., Sherali, H.D.: On the use of exact and heuristic cutting plane methods for the quadratic assignment problem. J. Oper. Res. Soc. 33(11), 991-1003 (1982)
19. Benlic, U., Hao, J.-K.: Memetic search for the quadratic assignment problem. Expert Syst. Appl. 42(1), 584-595 (2015)
20. Bozorgi, N., Abedzadeh, M.: A multiple criteria facility layout problem using data envelopment analysis. Manag. Sci. Lett. 1, 363-370 (2011)
21. Brixius, N.W., Anstreicher, K.M.: Solving quadratic assignment problems using convex quadratic programming relaxations. Optim. Methods Softw. 16(1-4), 49-68 (2001)
22. Brixius, N.W., Anstreicher, K.M.: The Steinberg Wiring problem. Paper presented at Grötschel, M. (ed.) The Sharpest Cut: The Impact of Manfred Padberg and His Work, Philadelphia, USA: Society for Industrial and Applied Mathematics (MOS-SIAM Series on Optimization), pp. 293-307 (2004)
23. Burkard, R.E., Dell'Amico, M., Martello, S.: Assignment Problems. Society for Industrial and Applied Mathematics, Philadelphia (2009)
24. Burkard, R.E., Karisch, S.E., Rendl, F.: QAPLIB—a quadratic assignment problem library. J. Global Optim. 10(4), 391-403 (1997)
25. Burkard, R.E., Rendl, F.: A thermodynamically motivated simulation procedure for combinatorial optimization problems. Eur. J. Oper. Res. 17(2), 169-174 (1984)
26. Burkard, R.E., et al.: The Quadratic Assignment Problem. Paper presented at Du, D.-Z., Pardalos, P. (eds) Handbook of Combinatorial Optimization, Springer US, pp. 1713-1809 (1998)
27. Ceberio, J., et al.: A review on estimation of distribution algorithms in permutation-based combinatorial optimization problems. Prog. Artif. Intel. 1(1), 103-117 (2012)

28. Chmiel, W.: Evolutionary algorithm using conditional expectation value for quadratic assignment problem. Swarm Evolut. Comput. 46(1), 1-27 (2019)
29. Clausen, J., Perregaard, M.: Solving large quadratic assignment problems in parallel. Comput. Optim. Appl. 8(2), 111-127 (1997)
30. Connolly, D.T.: An improved annealing scheme for the QAP. Eur. J. Oper. Res. 46(1), 93-100 (1990)
31. Czapiński, M.: An effective Parallel Multistart Tabu Search for Quadratic Assignment Problem on CUDA platform. J. Parallel Distrib. Comput. 73(11), 1461-1468 (2013)
32. Day, R.O., Kleeman, M.P., Lamont, G.B.: Solving the multi-objective quadratic assignment problem using a fast messy genetic algorithm. Paper presented at Proceedings of Congress Evolutionary Computation (CEC'03), pp. 2277-2283 (2003)
33. Deineko, V.G., Woeginger, G.J.: A study of exponential neighborhoods for the travelling salesman problem and for the quadratic assignment problem. Math. Program. 87(3), 519-542 (2000)
34. Ding, Y., Wolkowicz, H.: A low-dimensional semidefinite relaxation for the quadratic assignment problem. Math. Oper. Res. 34(4), 1008-1022 (2009)
35. Dokeroglu, T., Cosar, A.: A novel multistart hyper-heuristic algorithm on the grid for the quadratic assignment problem. Eng. Appl. Artif. Intell. 52, 10-25 (2016)
36. Drezner, Z.: The extended concentric tabu for the quadratic assignment problem. Eur. J. Oper. Res. 160(2), 416-422 (2005)
37. Drezner, Z.: Extensive experiments with hybrid genetic algorithms for the solution of the quadratic assignment problem. Comput. Oper. Res. 35(3), 717-736 (2008)
38. Drezner, Z.: The quadratic assignment problem. In: Laporte, G., Nickel, S., Saldanha da Gama, F. (eds.) Location Science. Springer, Cham (2015)
39. Drezner, Z., MisevicIus, A.: Enhancing the performance of hybrid genetic algorithms by differential improvement. Comput. Oper. Res. 40(4), 1038-1046 (2013)
40. Duman, E., Or, I.: The quadratic assignment problem in the context of the printed circuit board assembly process. Comput. Oper. Res. 34(1), 163-179 (2007)
41. Emanuel, B., Wimer, S., Wolansky, G.: Using well-solvable quadratic assignment problems for VLSI interconnect applications. Discrete Appl. Math. 160(4), 525-535 (2012)
42. Fleurent, C., Glover, F.: Improved constructive multistart strategies for the quadratic assignment problem using adaptive memory. Informs J. Comput. 11(2), 198-204 (1999)
43. Forsberg, J.H., et al.: Analyzing Lanthanide-Induced Shifts in the NMR Spectra of Lanthanide(III) Complexes Derived from 1,4,7,10mbox-Tetrakis(N, N-diethylacetamido)-1,4,7,10-tetraazacyclododecane. Inorg. Chem. 34(14), 3705-3715 (1995)
44. Francis, R.L., McGinnis Jr., F., White, J.A.: Facility Layout and Location-An Analytical Approach, 2nd edn. Prentice-Hall, New Jersey (Prentice-Hall International Series in Industrial and Systems Engineering) (1991)
45. Frieze, A.M., Yadegar, J.: On the quadratic assignment problem. Discrete Appl. Math. 5(1), 89-98 (1983)
46. Gambardella, L.M., Taillard, É.D., Dorigo, M.: Ant colonies for the quadratic assignment problem. J. Oper. Res. Soc. 50(2), 167-176 (1999)
47. Garey, M.R., Johnson, D.S.: Computers and Intractability: A Guide to the Theory of NP-Completeness. W.H. Freeman \& Co, New York (1979)
48. Gonçalves, A.D., et al.: A graphics processing unit algorithm to solve the quadratic assignment problem using level-2 reformulation-linearization technique. Informs J. Comput. 29(4), 676-687 (2017)
49. Hahn, P.M., et al.: Tree elaboration strategies in branch and bound algorithms for solving the quadratic assignment problem. Yugoslav J. Oper. Res. 11(1), 41-60 (2001)
50. Hahn, P.M., Krarup, J.: A hospital facility layout problem finally solved. J. Intell. Manuf. 12(5), 487-496 (2001)
51. Hansen, P., Mladenović, N., Pérez, J.M.: Variable neighbourhood search: methods and applications. Ann. Oper. Res. 175(1), 367-407 (2010)
52. Hassin, R., Levin, A., Sviridenko, M.: Approximating the minimum quadratic assignment problems. ACM Trans. Algorithms 6(1), 18:1-18:10 (2009)
53. Hauschild, M., Pelikan, M.: An introduction and survey of estimation of distribution algorithms. Swarm Evol. Comput. 1(3), 111-128 (2011)

54. Heffey, D.R.: Assigning runners to a relay team. Paper presented at Ladany, S.P., Machol, R.E. (eds.) Optimal Strategies in Sports (Studies in management science and systems, volume 5), NorthHolland, Amsterdam: Elsevier North-Holland, pp. 169-171 (1977)
55. Heffley, D.R.: Decomposition of the Koopmans-Beckmann problem. Reg. Sci. Urban Econ. 10(4), $571-580(1980)$
56. Helber, S., et al.: A hierarchical facility layout planning approach for large and complex hospitals. Flex. Serv. Manuf. J. 28(1-2), 5-29 (2016)
57. Hong, G.: A hybrid ant colony algorithm for quadratic assignment problem. Open Electr. Electr. Eng. J. 7(1), 51-54 (2013)
58. İşeri, A., Ekşioğlu, M.: Estimation of digraph costs for keyboard layout optimization. Int. J. Ind. Ergon. 48, 127-138 (2015)
59. James, T., Rego, C., Glover, F.: A cooperative parallel tabu search algorithm for the quadratic assignment problem. Eur. J. Oper. Res. 195(3), 810-826 (2009)
60. Karisch, S.E. (1995) Nonlinear approaches for quadratic assignment and graph partition problems. PhD diss., Technical University Graz, Austria
61. Koopmans, T.C., Beckmann, M.: Assignment problems and the location of economic activities. Econometrica 25(1), 53-76 (1957)
62. Krarup, J., Pruzan, P.: Computer-aided layout design. Paper presented at Balinski, M.L., Lemarechal, C. (eds.) Mathematical Programming in Use, Berlin, Germany: Springer Berlin Heidelberg (Mathematical Programming Studies), pp. 75-94 (1978)
63. Larrañaga, P., Lozano, J.A.: Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Kluwer, Boston, MA (2002)
64. Li, W.J., Smith, J.M.: Theory and methodology: an algorithm for quadratic assignment problems. Eur. J. Oper. Res. 81, 205-216 (1995)
65. Lim, W.L., et al.: A biogeography-based optimization algorithm hybridized with tabu search for the quadratic assignment problem. Comput. Intell. Neurosci. 2016, 1-12 (2016)
66. Loiola, E.M., et al.: A survey for the quadratic assignment problem. Eur. J. Oper. Res. 176(2), $657-690(2007)$
67. Loiola, E.M., et al.: An analytical survey for the quadratic assignment problem, Council for the Scientific and Technological Development, of the Brazilian Gov (2004)
68. Lozano, J.A.: Towards a New Evolutionary Computation: Advances on Estimation of Distribution Algorithms. Springer, New York (2006)
69. Matsui, S., et al.: Exponential chaotic tabu search hardware for quadratic assignment problems using switched-current chaotic neuron IC. Paper presented at Proceedings of IEEE Internationa Joint Conference on Neural Networks, pp. 2221-2225 (2004)
70. Michalewicz, Z.: Genetic Algorithms + Data Structures $=$ Evolution Programs, 3rd edn. SpringerVerlag, London (1996)
71. Misevicius, A.: An intensive search algorithm for the quadratic assignment problem. Informatica 11(2), 145-162 (2000)
72. Misevicius, A.: A modified simulated annealing algorithm for the quadratic assignment problem. Informatica 14(4), 497-514 (2003)
73. Misevicius, A.: An improved hybrid optimization algorithm for the quadratic assignment problem. Math. Model. Anal. 9(2), 149-168 (2004)
74. Misevicius, A., Guogis, E.: Computational study of four genetic algorithm variants for solving the quadratic assignment problem. Paper presented at International Conference on Information and Software Technologies, Springer, pp. 24-37 (2012)
75. Mladenovic, N., Hansen, P.: Variable neighborhood search. Comput. Oper. Res. 24(11), 1097-1100 (1997)
76. Ng, K.M., Tran, T.H.: A parallel water flow algorithm with local search for solving the quadratic assignment problem. J. Ind. Manag. Optim. 15(1), 235-259 (2019)
77. Nyberg, A., Westerlund, T.: Tightening a discrete formulation of the quadratic assignment problem. Chem. Eng. Trans. 32(1), 1309-1314 (2013)
78. Osman, H., Demirli, K.: Economic lot and delivery scheduling problem for multi-stage supply chains. Int. J. Prod. Econ. 136(2), 275-286 (2012)
79. Osman, I.H., Laporte, G.: Metaheuristics: a bibliography. Ann. Oper. Res. 63(5), 511-623 (1996)
80. Pardalos, P.M., Xue, J.: The maximum clique problem. J. Global Optim. 4(3), 301-328 (1994)
81. Paul, G.: An efficient implementation of the simulated annealing heuristic for the quadratic assignment problem. Comput. Res. Reposit. abs/1111.1353 (2011)

82. Paul, G.: A GPU implementation of the simulated annealing heuristic for the quadratic assignment problem. Comput. Res. Reposit. abs/1208.2675 (2012)
83. Pelikan, M., Hauschild, M. W. and Lobo, F. G., Introduction to estimation of distribution algorithms, MEDAL Report. 2012003. Missouri, USA:Missouri Estimation of Distribution Algorithms Laboratory (MEDAL), Department of Mathematics and Computer Science, University of Missouri,Columbia, USA. (2012)
84. Peng, T., Huanchen, W., Dongme, Z.: Simulated annealing for the quadratic assignment problem: a further study. Comput. Ind. Eng. 31(3/4), 925-928 (1996)
85. Pitsoulis, L.S., Pardalos, P.M., Hearn, D.W.: Approximate solutions to the turbine balancing problem. Eur. J. Oper. Res. 130(1), 147-155 (2001)
86. Ramkumar, A.S., et al.: Iterated fast local search algorithm for solving quadratic assignment problems. Robot. Comput. Integr. Manuf. 24(3), 392-401 (2008)
87. Santana, R., Mendiburu, A., Lozano, J.A.: A review of message passing algorithms in estimation of distribution algorithms. Nat. Comput. 15(1), 165-180 (2016)
88. See, P.C., Wong, K.Y.: Application of ant colony optimisation algorithms in solving facility layout problems formulated as quadratic assignment problems: a review. Int. J. Ind. Syst. Eng. 3(6), $644-672$ (2008)
89. Skorin-Kapov, J.: Tabu search applied to the quadratic assignment problem. ORSA J. Comput. 2(1), 33-45 (1990)
90. Song, L.Q., Lim, M.H., Ong, Y.S.: Neural meta-memes framework for managing search algorithms in combinatorial optimization. Paper presented at IEEE Workshop on Memetic Computing (MC), 2011, pp. 1-6 (2011)
91. Steinberg, L.: The backboard wiring problem: a placement algorithm. SIAM Rev. 3(1), 37-50 (1961)
92. Talbi, E.G., Hafidi, Z., Geib, J.M.: A parallel adaptive tabu search approach. Parallel Comput. 24(14), 2003-2019 (1998)
93. Tate, D.M., Smith, A.E.: A genetic approach to the quadratic assignment problem. Comput. Oper. Res. 22(1), 73-83 (1995)
94. Tosun, U.: A new recombination operator for the genetic algorithm solution of the quadratic assignment problem. Proc. Comput. Sci. 32, 29-36 (2014)
95. Tosun, U.: On the performance of parallel hybrid algorithms for the solution of the quadratic assignment problem. Eng. Appl. Artif. Intell. 39, 267-278 (2015)
96. Tosun, U., Dokeroglu, T., Cosar, A.: A robust island parallel genetic algorithm for the quadratic assignment problem. Int. J. Prod. Res. 51(14), 4117-4133 (2013)
97. Tseng, L.Y., Liang, S.C.: A hybrid metaheuristic for the quadratic assignment problem. Comput. Optim. Appl. 34(1), 85-113 (2006)
98. Urban, T.L.: Solution procedures for the dynamic facility layout problem. Ann. Oper. Res. 76, 323342 (1998)
99. Uwate, Y., et al.: Performance of chaos and burst noises injected to the hopfield NN for quadratic assignment problems. IEICE Trans. Fundam. Electr. Commun. Comput. Sci. E87-A(4), 937-943 (2004)
100. Wakabayashi, S., Kimura, Y., Nagayama, S.: FPGA implementation of tabu search for the quadratic assignment problem. Paper presented at Proceedings of IEEE International Conference on Field Programmable Technology (FPT 2006), pp. 269-272 (2006)
101. West, D.H.: Algorithm 608: approximate solution of the quadratic assignment problem. ACM Trans. Math. Softw. 9(4), 461-466 (1983)
102. Wilhelm, M.R., Ward, T.L.: Solving Quadratic Assignment Problems by 'Simulated Annealing. IIE Trans. 19(1), 107-119 (1987)
103. Wu, Z., et al.: Global optimality conditions and optimization methods for quadratic assignment problems. Appl. Math. Comput. 218(11), 6214-6231 (2012)
104. Wu, Y., Ji, P.: Solving the quadratic assignment problems by a genetic algorithm with a new replacement strategy. Int. J. Hum. Soc. Sci. 151-155 (2007)
105. Xia, Y.: An efficient continuation method for quadratic assignment problems. Comput. Oper. Res. 37(6), 1027-1032 (2010)

106. Yamada, S.: A new formulation of the quadratic assignment problem on r-dimensional grid. IEEE Trans. Circuits Syst. I Fundam. Theory Appl. 39(10), 791-797 (1992)
107. Zaied, A.N.H., Shawky, L.A.E.-F.: A survey of the quadratic assignment problem. Int. J. Comput. Appl. 101(6), 28-36 (2014)
108. Zhou, J., et al.: An exact penalty function method for optimising QAP formulation in facility layout problem. Int. J. Prod. Res. 55(10), 2913-2929 (2017)
109. Zhu, W., Curry, J., Marquez, A.: SIMD tabu search for the quadratic assignment problem with graphics hardware acceleration. Int. J. Prod. Res. 48(4), 1035-1047 (2010)

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.