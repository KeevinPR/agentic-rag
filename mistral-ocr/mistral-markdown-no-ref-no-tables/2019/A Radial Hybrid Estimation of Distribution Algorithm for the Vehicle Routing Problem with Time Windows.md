# A hybrid estimation of distribution algorithm for the vehicle routing problem with time windows 

Ricardo Pérez-Rodríguez ${ }^{\mathrm{a}, *}$, Arturo Hernández-Aguirre ${ }^{\mathrm{b}}$<br>${ }^{a}$ CONACTT - CIMAT, A.C. Bartolomé de las Casas 314, Barrio la Estación, 20259 Aguascalientes, Ags, Mexico<br>${ }^{\mathrm{b}}$ CIMAT, A.C. Jalisco s/n, Valenciana, 36240 Guanajuato, Gto, Mexico

## A R T I C L E I N F O

Keywords:
Estimation of distribution algorithm
Mallows distribution
Vehicle routing problem
Combinatorial optimization

## ABSTRACT

The Vehicle Routing Problem (VRP) seeks to find minimum-travel routes for a set of vehicles. The routes contain a set of customers with known demands. Each vehicle departs and arrives at the same depot. In the vehicle routing problem with time windows (VRPTW), each vehicle has to arrive in a specific time window with each customer and also each vehicle has to return to the depot before a due time. In this research, the use of an estimation of distribution algorithm to solve the problem is proposed. The algorithm uses the generalized Mallows distribution as a probability model to describe the distribution of the solution space. HombergerGehring's instances are used as input and test parameters in order to show that the modification of the generalized Mallows distribution mentioned is able to produce competitive sequences for the VRPTW against some other estimation of distribution algorithms used in permutation-based optimization problems.

## 1. Introduction

The vehicle routing problem (VRP) exists in many logistics enterprises as a real-world problem. The VRP arises in the field of transportation, distribution, and logistics. The distribution of merchandise is an example where the VRP and its variants arise. In some market sectors, transportation means a high percentage of the price to goods. In addition, in some economics sectors, the transportation of merchandise is considered a logistics issue. Therefore, the utilization of computerized methods for transportation often results in significant savings ranging from five per cent to twenty per cent of the total costs, as reported in Toth and Vigo (2001). The VRP has attracted the attention of a large number of researchers and practitioners. The practical characteristic of the VRP makes its study interesting. There are important advances and new challenges that have been raised in the last number of years due to technological innovations such as global positioning systems and radio frequency identification. The portfolio of techniques for modeling and solving the standard VRP and its many variants has advanced significantly. Researchers and practitioners have developed faster, more accurate solution algorithms and better models that give them the ability to solve large-scale problems.

The VRP is defined on an undirected network $G=(V, E)$ with a vertex set $V=[0,1,2, \cdots, n]$ and an edge set $E$. Vertex 0 is the depot, to be consistent with Homberger-Gehring's (2005) instances. Each other
vertex $i>0$ represents a customer that requires a nonnegative demand $q_{i}$ with a known service time $s_{i}$, and each edge has a non-negative travel time $t_{i j}=t_{j i}$. The VRP consists of determining a set of $m$ vehicle trips of minimum total travel time, such that each vehicle starts and ends at the depot, each customer is visited exactly once, and the total demand handled by any vehicle does not exceed the vehicle's capacity $Q$. The VRP with time windows (VRPTW) is a variant of the VRP with additional time constraints. Here, the service of a customer should begin within a time window $\left[a_{i}, b_{i}\right]$. The vehicle should not arrive earlier than time $a_{i}$ and no later than time $b_{i}$. A vehicle arriving before time $a_{i}$ will produce a waiting time. A vehicle arriving after time $b_{i}$ will incur a delay time. All vehicles scheduled have to return to the depot within $\left[0, b_{i}\right]$ where $b_{i}$ is the maximal operation time for each vehicle.

A complete formulation of the mathematical integer linear programming model for the VRPTW was developed by Toth and Vigo (2001). The aforementioned formulation is detailed below based on the seventh chapter of the Toth and Vigo (2001) book.

The depot is represented by the nodes 0 and $n+1$ to be consistent with Toth and Vigo (2001). All feasible vehicle routes correspond to paths in $G=(V, E)$ that start from node 0 and end at node $n+1$. A time window is associated with nodes 0 and $n+1$, i.e., $\left[a_{n}, b_{n}\right]=\left[a_{n+1}, b_{n+1}\right]=[E, L]$, where $E$ and $L$ represent the earliest possible departure from the depot and the latest possible arrival at the depot, respectively. Moreover, zero demands and service times are

[^0]
[^0]:    * Corresponding author.

    E-mail address: ricardo.perez@cimat.mx (R. Pérez-Rodríguez).

defined for these two nodes, that is, $d e_{0}=d e_{n+1}=s_{0}=s_{n+1}=0$. Two types of variables exist in this formulation: flow variables $x_{i j k}(i, j) \in A, k \in K$, equal to 1 if arc $(i, j)$ is used by vehicle $k$ and 0 otherwise, and time variables $w_{i k}, i \in V, k \in K$, specifying the start of service at node $i$ when serviced by vehicle $k$.
$\min \sum_{k \in K} \sum_{\langle i, j\rangle \in A} d i_{i j} x_{i j k}$
(VRPTW.1)
subject to
$\sum_{k \in K} \sum_{j \in \Delta^{n}(i)} x_{i j k}=1 \quad \forall i \in N$
(VRPTW.2)
$\sum_{j \in \Delta^{n}(0)} x_{i j k}=1 \quad \forall k \in K$
(VRPTW.3)
$\sum_{i \in \Delta^{n}(j)} x_{i j k}-\sum_{i \in \Delta^{n}(j)} x_{j i k}=0 \quad \forall k \in K, j \in N$
(VRPTW.4)
$\sum_{i \in \Delta^{n}(n+1)} x_{i, n+1, k}=1 \quad \forall k \in K$
(VRPTW.5)
$x_{i j k}\left(w_{i k}+s_{1}+t_{i j}-w_{j k}\right) \leq 0 \quad \forall k \in K,(i, j) \in A$
$\left\langle\left\langle\left\langle\left\langle x_{i j k} \leq w_{i k} \leq w_{j k} \leq b_{1} \sum_{j \in \Delta^{n}(i)} x_{i j k} \quad \forall k \in K, i \in N\right.\right.\right.$
(VRPTW.7)
$E \leq w_{i k} \leq L k \in K, i \in[0, n+1]$
$\sum_{i \in A} d e_{i} \sum_{j \in \Delta^{n}(i)} x_{i j k} \leq C \forall k \in K$
(VRPTW.9)
$x_{i j k} \in[0,1] \forall k \in K,(i, j) \in A$
(VRPTW.10)
The objective function (VRPTW.1) expresses the total distance. Given $N=V /(0, n+1)$ represents the set of customers. Constraints (VRPTW.2) restrict the assignment of each customer to exactly one vehicle route. Next, constraints (VRPTW.3)-(VRPTW.5) characterize the flow on the path to be followed by vehicle $k$. Additionally, constraints (VRPTW.6)-(VRPTW.9) guarantee schedule feasibility with respect to time considerations and capacity aspects, respectively. Note that for a given $k$, constraints (VRPTW.7) force $w_{i k}=0$ whenever customer $i$ is not visited by vehicle $k$. Finally, conditions (VRPTW.10) impose binary conditions on the flows variables.

In this research, the hard type time window is considered. It means that it is not possible to arrive after the possible time at each vertex, i.e., $b_{i}$. In order to get feasible solutions an example is provided. At the beginning of Fig. 1 an example of a sequence of vertices (permutation) $S$ of six vertices without route delimiters, i.e., $S=(1,4,5,2,3,6)$, viewed as a giant tour is shown. Each vertex has a demand in brackets and a time window in square brackets. To simplify, travel times are here equal to distances, i.e., $d_{i j}=t_{i j}$ for each edge $[i, j]$. Table 1 details the data for the instance used in Fig. 1. In addition, Fig. 1 gives an example of splitting and is shown at the lower part of Fig. 1. The splitting scheme satisfies the set of constraints for the VRPTW, i.e., it ensures that all the vertices are assigned to a single vehicle. Furthermore, it takes care of the requirement that the sequence of vertices must respect precedence, i.e., the precedence relationships between the vertices of the sequence are not violated. In addition, the solution depicted in Fig. 1 guarantees that multiple vertices cannot be visited at the same time on any possible vehicle. The auxiliary graph is given in the middle of Fig. 1, assuming a vehicle capacity $Q=50$. Each arc represents a feasible trip. For example, arc 1 models the trip reduced to vertex 1: its length 165.71 is twice the length of edge $[0,1]$ and the corresponding service time at vertex 1 . Another example, arc $[1,4]$ is not represented, since a delay occurs when a vehicle can reach the vertex 4 , at time 897.8. All the other trips, which are not represented, violate either vehicle capacity or the time window. Finally, Bellman's algorithm determines the shortest path, and determines the number of vehicles used. The labels computed are given above each node. The number of vehicles used is 4 . The lower
part of the figure shows the resulting solution, with departure times in brackets.

Additionally, Table 2 and Fig. 2 present an alternative sequence for the aforementioned instance. Based on Fig. 2, the performance is improved using the alternative sequence.

As the VRP, the VRPTW requires special attention from researchers due to its peculiar complexity and interesting usefulness in real-logistics cases. Surveys of solution methods for VRPTW are available in Golden and Assad (1986), Desrochers, Lenstra, Savelsbergh, and Soumis (1988), Solomon and Desrosiers (1988), and Bräysy and Gendreau (2005). Developments can be found in Potvin and Rousseau (1993), Rochat and Taillard (1995), Thangiah, Osman, Vinayagamoorthy, and Sun (1995), Potvin and Bengio (1996), Homberger and Gehring (1999), Cordeau, Laporte, and Mercier (2001), Tan, Lee, Zhu, and Ou (2001), Berger and Barkaoui (2004), Cordeau, Laporte, and Mercier (2004) and Mester, Bräysy, and Dullaert (2007). Recent surveys on VRP and its variants can be found in Braekers, Ramaekers, and Van Nieuwenhuyse (2016), Montoya-Torres, López-Franco, Nieto-Isaza, Felizzola-Jiménez, and Herazo-Padilla (2015), Gendreau, Ghiani, and Guerriero (2015), and Koç, Bektas, Jabali, and Laporte (2016).

Evolutionary algorithms have been considered competitive procedures for tackling the VRP problem and its variants. A relatively new paradigm of evolutionary algorithms is the estimation of distribution algorithms (EDA) introduced by Mühlenbein and Paaß (1996). Compared with other evolutionary algorithms, the EDA reproduces new population without using traditional evolutionary operators. In the EDA, a probability model of the most promising area is built by statistical information based on the search experience. The aforementioned information is represented by all the values contained in the solution vectors, i.e., the parents (Fig. 3(a)). Each element belonging to the solutions is considered as a variable. Identifying the values that each element (variable) has taken, it is possible to build the charts shown in (Fig. 3(a)). A probability model is used to generate new individuals (Fig. 3(b)). It is called a sampling process. Each element of a new solution is obtained through the cumulative distribution of all possible values in the corresponding element (variable). A uniform random number is used to select the value in the element. It is computed for each element of the offspring (Fig. 3(b)). The EDA makes use of the probability model to describe the distribution of the solution space. The updating process reflects the evolutionary trend of the population (Wang, Wang, Xu, Zhou, \& Liu, 2012). To describe the distribution of the solution space, the EDA tries to determine the relationship or interaction among variables of the problem as a primary objective. Different estimations of the relationships mentioned are shown in Fig. 3(c). In some cases, the possible values for each element are not influenced by the values of the rest of the elements, i.e., without interaction. In other cases, the possible values for each element might be influenced by the values of some element, i.e., bivariate interaction. Finally, the possible values for each element might be influenced by the values of more than two elements, i.e., multiple interactions. Identifying the best estimation of the interaction is the main goal in this kind of algorithm.

The traditional evolutionary operators are replaced by the probability model that is built with information on relationships and interactions among variables. The main idea is to learn and benefit from the interaction among variables by estimating the distribution of the population and sample from this distribution of the offspring. However, how can we improve the estimation of the relationships among variables of the problem? How does the above mentioned estimation affect the performance of the algorithm? Different and diverse ways to estimate the relationships among variables have been proposed, such as the Mutual Information Maximizing Input Clustering algorithm (MIMIC) based on De Bonet, Isbell, and Viola (1997). The MIMIC uses the entropy concept to estimate the relationships (Fig. 4(a)). The Combining Optimizers with Mutual Information Trees Algorithm (COMIT) is based on Baluja and Davies (1997). The COMIT uses the mutual information

![img-0.jpeg](img-0.jpeg)

Depot $[0,1351]$
![img-1.jpeg](img-1.jpeg)

Fig. 1. Illustration of a sequence for the VRPTW.
concept to estimate the relationships (Fig. 4(b)). The Bayesian Optimization Algorithm (BOA) is based on Pelikan, Goldberg, and CantúPoz (1998). The BOA uses the Bayesian Dirichlet metric to measure of how well the network models the data (Fig. 4(c)).

Although the interaction may or may not be present, generally this is explicitly unknown even in small size VRPTW problems. In this research, an EDA is proposed in order to show that the estimation of any
relationship and interaction between vertices on the sequence of the VRPTW solution can be improved. Such a relationship should be used and exploited in order to get competitive solutions. In addition, any probability model should be able to represent the characteristics exhibited by the parents as a distribution of the solution space. Therefore, the EDA proposed should not have to need to hold members of the population to keep track and inherit the characteristics exhibited by the

Table 1
Data for the instance used in Fig. 1.
Table 2
Data for the instance used in Fig. 2.
![img-2.jpeg](img-2.jpeg)
![img-3.jpeg](img-3.jpeg)

Fig. 2. Illustration of an alternative sequence for the VRPTW.
parents mentioned in each generation as in other algorithms. In particular, the genetic algorithms with specific crossover and mutation operators have been proposed in order to preserve partial information of the members of the population. Research by Potvin (1993), Hwan (2002), Larranaga, Kuijpers, Murga, Inza and Dizdarevic (1999) and Prins (2004) are examples of those algorithms. The proposed EDA should guarantee that the characteristics will persist for all members of
the population in the evolutionary progress of the probability model proposed. Meanwhile, the probability model is updated in each generation with the potential individuals of the new population. In such an iterative way, the population evolves, and satisfactory solutions can be obtained (Wang et al., 2012).

The reason for proposing an EDA for the VRPTW is to show that a better estimation of any relationship and interaction between vertices

![img-4.jpeg](img-4.jpeg)

Fig. 3. Estimation of distribution algorithm main procedure.
![img-5.jpeg](img-5.jpeg)
b)

Fig. 4. Different types of estimation of distribution algorithms.
on the sequence of the VRPTW solution can be improved using an explicit probability distribution. Such information allows for the avoidance of using the traditional evolutionary operators for permutationbased problems. The contribution of this research is to implement an EDA to identify, by statistical information, the distribution of the solution space and indicate any interaction between the vertices and their positions on the vehicle routing sequences. Therefore, we use the Mallows distribution model in this research to obtain a better estimate of the relationships between the vertices. The Mallows model was initially proposed by Mallows (1957) and later improved upon by Fligner and Verducci (1986) through the generalized Mallows distribution (GMD). A more extensive explanation of the GMD characteristics is
found in Fligner and Verducci (1986) and Fligner and Verducci (1988). More recently, Ceberio, Irurozki, Mendiburu, and Lozano (2014) contributed to an initial application of the GMD to solve the flow-shop scheduling problem (FSP) coupled with an EDA.

As a popular model for rankings (Meilă, Phadnis, Patterson, \& Bilmes, 2007), the GMD is suitable to utilize if there is a need to rank $k$ vertices, in the vehicle routing problem, according to some criteria. The main challenge is to characterize suitable solutions on a random set of rankings, i.e., sequences of the VRPTW. In the GMD, the main process for ranking, the sequences, is to decompose it into $k-1$ stages, i.e., $k-1$ positions (or columns) as shown in Fig. 5.

The GMD, as in other models, establishes a probability that one vertex is preferred to another in a specified stage, i.e., position, in the solution. Therefore, as a basic model, the most preferred vertex is chosen in the first stage with a high probability. After that, the best of remaining vertices is chosen in the second stage, with the corresponding probability, and so on until the last vertex is chosen by default. Then, each sequence of the VRPTW solution will produce a ranking. Different models have been proposed in order to compute a proper estimate of the probability of choosing a particular vertex at any stage. However, the analytic intractability of such models is a major difficulty to use in a real-world problem. The GMD avoids the analytical difficulties by assuming that the accuracy of the choice made at any stage is independent of the accuracies in the other stages (Fligner \& Verducci, 1988). In order to avoid the analytical difficulties mentioned above, the GMD uses a central ranking, i.e., a consensus ranking. It is obtained from a random set of vectors, sequences of the VRPTW. A conventional definition of the central ranking is it minimizes the total number of disagreements with rankings contained in the set of rankings

![img-6.jpeg](img-6.jpeg)

Fig. 5. An example of a probability distribution associated with the space of possible solutions.
(Ali \& Meilă, 2012). The GMD uses the Kendall's metric to compute the total number of disagreements mentioned above. The Kendall's metric has been the measure of choice in many recent applications centered on the analysis of ranked data (Cohen, Schapire, \& Singer, 1998). To estimate a suitable central ranking is a difficult task, since the problem is NP-hard even for only four items (Bartholdi, Tovey, \& Trick, 1989; Cohen et al., 1998). Nevertheless, once a central ranking is computed, the GMD produces a multistage model in order to estimate the probabilities in each stage.

Although the EDA was originally designed to solve integer or realvalued domain problems, it cannot produce a feasible solution from a probability model built on a permutation-based representation (Larrañaga \& Lozano, 2001). Furthermore, the EDA requires being adapted to deal with permutation-based problems by means of a modification in the algorithm process. Then, the implementation of a specific probability model for this issue would be more competitive against other models. The Mallows model (1957) is a distance-based exponential probabilistic model considered analogous to the Gaussian probability distribution over the space of permutations. In the Mallows distribution, the probability value of each permutation $\sigma \in T_{\sigma}$ (where $T_{\sigma}$ stands for the set of $n$ ! permutations of items) depends on just two parameters: a spread parameter $\theta$ and the distance to a central permutation $\sigma_{0}$. This model assigns to each permutation $\sigma$ a probability that decays exponentially with respect to its distance to the central permutation $\sigma_{0}$. In this way, $P(\sigma)$ can be considered as an exponential non-uniform distance-based ranking model (Ceberio et al., 2014). Both parameters, i.e., the spread parameter $\theta$ and the central permutation $\sigma_{0}$, are estimated. Therefore, different estimates of the parameters mentioned should be considered in order to get a better performance to solve combinatorial optimization problems such as VRPTW.

Contrary to current research where diverse techniques and approaches have been proposed in order to solve the problem that is being examined, this paper contributes to the state of the art as follows:

- To introduce the GMD, detailed in Fligner and Verducci (1986) research, for the VRPTW as a way of estimating an explicit probability distribution in the domain of permutations for any EDA.
- To apply the GMD coupled with an EDA, called HMEDA (Hybrid Mallows Estimation of Distribution Algorithm), for solving the VRPTW on a multi-objective perspective.
- To propose a different way of improving the estimation of the central permutation $\sigma_{0}$ in the GMD process using a Pareto-front approach to help the HMEDA to find better solutions for the VRPTW.
- The purpose of this research is to propose a different experimental technique to enhance the performance of the algorithm mentioned above for solving the VRPTW using a Pareto-front approach.

The proposed algorithm has a wide range of applications for automotive, aerospace, chemical, metallurgical, pharmaceutical, and food industries, among others. The users of this contribution are academics, engineers, managers, and practitioners related to the transportation of merchandise.

The remainder of this paper is organized as follows: in Section 2, the related work is depicted. In Section 3, the proposed HMEDA is detailed. In Section 4, computational results and comparison with other multiobjective and recent algorithms are presented. Section 5 shows a simulation and preliminary implementation. Finally, the concluding remarks are made in Section 6.

## 2. Related work

### 2.1. Exact methods

Exact methods often perform very poorly, i.e., in some cases taking days or more to find moderately decent, let alone optimal, solutions even to fairly small instances (El-Sherbeny, 2010).

The Lagrangiana relaxation-based methods are used in Fisher, Jörnsten, and Madsen's (1997) research. The column generation approach is used for the first time in Agarwal, Mathur, and Salkin (1989) to solve the VRP problem, while Desrosiers, Soumis, and Desrochers (1984) used the column generation approach to solve the m-TSP with time windows. In Desrosiers et al. (1984) research, the column generation approach is used for the first time to solve the VRPTW, and a

more effective version of the same model with the addition of valid inequalities solves more instances to optimality in Desrochers, Desrosiers, and Solomon (1992) research.

The dynamic programming approach for VRPTW is presented for the first time in Kolen, Rinnooy-Kan, and Trienkens (1987) and Christofides and Beasley (1984) uses the dynamic programming paradigm to solve the VRP. In Kolen et al. (1987) problems up to 15 customers are solved by this method.

The algorithm of Kohl and Madsen (1997) uses branch-and-bound to achieve optimality. Each node $\alpha$ in the branch-and-bound tree corresponds to three sets: $\mathrm{F}(\alpha)$ which the set is of fixed feasible routes starting and finishing at the depot, $\mathrm{P}(\alpha)$ which is a partially built route starting at the depot and $\mathrm{C}(\alpha)$ denotes the set of customers forbidden to be next on $\mathrm{P}(\alpha)$. Branching is done by selecting a customer $i$ that is not forbidden, that is $i C(\alpha)$, and that does not appear on any route, that is iF $(\alpha) \cup \mathrm{P}(\alpha)$. Branching decisions are taken on route-customer allocations. Then two branches are generated: one in which the partially build route $\mathrm{P}(\alpha)$ is extended by $i$ and one where $i$ is forbidden as the next customer on the route that is added to $\mathrm{C}(\alpha)$. Customer $i$ is chosen as the customer the partial route $\mathrm{P}(\alpha)$ was extended with in the calculation that lead to the lower bound of node $\alpha$. At each branch-and-bound node dynamic programming is used to calculate a lower bound on all feasible solutions defined by $\mathrm{F}(\alpha), \mathrm{P}(\alpha)$ and $\mathrm{C}(\alpha)$.

### 2.2. Evolutionary algorithms

Variants of Genetic Algorithms (GA) have been proposed to address the VRPTW, a problem known to be NP-hard. Potvin and Bengio (1996) propose a GA for the VPRTW that directly applies genetic operators to solutions, thus avoiding coding issues. The cheapest insertion heuristic proposed by Solomon (1987) is used to create the initial population. The fitness values of the proposed approach are based on the number of vehicles and the total route time of each solution. The selection process is stochastic and highly biased towards the best solutions. For this purpose, a linear ranking scheme is implemented. The linear ranking scheme prevented individuals, with significantly better fitness values than average, from dominating the selection process. During the recombination phase, two parent solutions are merged into a single one, to guarantee the feasibility of the new solution. Two types of crossover operators are used, namely a route-based and a sequence-based crossover. The route-based crossover replaced one route of parent solution P2 with a route of parent solution P1. However, in the sequence-based crossover only a randomly defined end part in a route of parent-solution P1 has been replaced by a set of customers served by a route of parent solution P2. A repair operator is proposed to remove duplicates and insert missing customers into the solution. Finally, in order to locally optimize the solution, a mutation operator based on Or-opt exchanges is considered.

Wang, Tong, and Li (2007) address the dynamic vehicle routing problem with time windows. The authors present an approach to the search for the best routes in a dynamic network. A dynamic route evaluation model for modeling the responses of vehicles to changing traffic information, a modified Dijkstra's double bucket algorithm for finding the real-time shortest paths, and an improved evolutionary algorithm for searching the best vehicle routes in the dynamic network are proposed. In the representation, a modified form of random keys is employed. A solution vector, called chromosome, consists of genes and each gene represents a customer node. The customer nodes have fixed gene positions in the chromosomes and the order in which they are visited is determined by sorting based on the gene values. The random keys have information about the vehicle number used for a service and the value for sorting, where the digit before the point represents the vehicle number and the digit after the point are used as sort keys to decode visiting sequences. The proposed approach has been evaluated by simulation experiments. It has been found that the proposed approach is quite efficient in finding real-time best vehicle routes where
the customer nodes and network information change dynamically.
Kamkar, Poostchi, and Totonchi (2010) introduce a cellular Genetic Algorithm (cGA) to solve the VRPTW. It is a GA subclass where the population diversity and exploration are enhanced thanks to the existence of small overlapped neighborhoods. The population is structured in a specific topology, so that individuals may only interact with their neighbors. This kind of structured algorithm is well suited for complex problems. For the representation of individuals, an integer string of length N is used, where N is the number of customers. Each gene contains the integer node number assigned to that customer originally, and the sequence of the genes is the order of visiting those customers. Tournament selection is used. The authors employ the PMX crossover and inverse mutation for the variation process. The benchmark of Solomon (1987) is selected for testing the proposed cGA and compares them with some other algorithms. The results demonstrate that the proposed cGA has the potential to solve these kinds of problems. However, only a few genetic-based approaches exploit knowledge provided by the problem or by the structure of the solutions computed during the evolutionary process to explore the solution space.

### 2.3. Hybridization-based algorithms

Other approaches are the hybridization-based algorithms that have been widely implemented. In Bräysy, Dullaert, and Gendreau (2004) present methods that hybridize ideas of evolutionary algorithms with some other search techniques, such as Tabu Search (TS) or Simulated Annealing (SA). These techniques have been also used to solve the VRPTW. Most of the hybrid methods presented have used local search mutation instead of the random mutation operators. In the first phase, either the cheapest insertion heuristic or the sectoring based genetic algorithm creates an initial solution. The second phase is applied to one of the following search procedures that use the $\lambda$-interchange mechanism: a local search descent procedure, an SA algorithm or a hybrid SA and TS, where TS is combined with the SA-based acceptance criterion to decide which moves to accept from the candidate list. The main feature of the local search procedures is that unfeasible solutions with penalties are allowed if considered attractive (Bräysy et al., 2004).

Selma, Prins, Yalaoui, and Reghioui (2013) deal with the two-dimensional loading capacitated VRPTW, which is a realistic extension of the well-known VRP. It consists of determining vehicle trips to deliver rectangular objects to a set of customers with known time windows, using a homogeneous fleet of vehicles, while ensuring a feasible loading of each vehicle used. Firstly, six heuristics are designed to quickly compute good solutions for realistic instances. The solutions are obtained by combining algorithms for the VRPTW with heuristics for packing rectangles. Then, a Memetic Algorithm (MA) is developed to improve the heuristic solutions. In this research, a chromosome is considered as a sequence of $n$ clients, without trip delimiters. This sequence can be interpreted as a giant tour where the vehicle capacity, the time windows, and the loading constraints are relaxed. It permits reusing classical crossover operators designed for the traveling salesman problem (TSP). The Prins (2004) procedure to split the giant tour unfeasible tours is used in this research. The quality and efficiency of the proposed heuristics and metaheuristic are evaluated by adding time windows to a set of instances.

### 2.4. Local search-based algorithms

Local search-based algorithms and their variants are another alternatives for the VRPTW. Cordeau et al. (2001) have introduced a simple TS procedure for the VRPTW and two of its extensions, namely Peri-odic-VRPTW (PVRPTW) and Multi-depot VRPTW (MDVRPTW). An important feature of the approach is the possibility of exploring unfeasible solutions during the search. Bräysy and Gendreau (2005) have reported a classical two-phase mechanism to solve the VRP and the VRPTW. The initial solution is first generated using the savings

heuristic. Then, intra-route local searches (2-opt and Or-opt) and three inter-route operators guided with TS are used to refine the solution.

Rochat and Taillard (1995) present a probabilistic technique to diversify, intensify and parallelize a local search adapted for solving vehicle routing problems. This technique may be applied to a very wide variety of vehicle routing problems and local searches. It is shown that efficient first level taboo searches for vehicle routing problems may be significantly improved with this technique. Moreover, the solutions produced by this technique may often be improved by a post-optimization technique presented in this paper too. The solutions of nearly 40 problem instances of the literature were improved.

Homberger and Gehring (2005) introduce a two-phase hybrid metaheuristic for the VRPTW. The objective function of the VRPTW considered here combines the minimization of the number of vehicles (primary criterion) and the total travel distance (secondary criterion). The aim of the first phase is the minimization of the number of vehicles by means of a ( $\mu, \lambda$ )-evolution strategy, whereas in the second phase the total distance is minimized using a TS algorithm. The two-phase hybrid metaheuristic was subjected to a comparative test on the basis of 356 problems from the literature with sizes varying from 100 to 1000 customers. The derived results show that the proposed two-phase approach is very competitive.

Créput, Koukam, and Hajjam (2007) presented an evolutionary algorithm embedding self-organizing maps (SOM) as operators to address the VRPTW. The approach has extended and improved SOM-based neural networks (NN) applications to the VRPTW. From the point of view of NN, the evolutionary framework introduced a level of supervision; however, it corresponded to a selection principle at a higher level with the aim of allowing simplicity and flexibility and favored further parallel implantations. Operators have a similar structure based on closest point findings and simple moves performed in a Euclidean plane.

Diverse works have presented parallel co-operative methodologies in which several agents communicate through a pool of feasible solutions. The agents consist of a simple construction and local search algorithms and different metaheuristic methods, namely evolutionary algorithms and TS. The evolutionary algorithms use a probabilistic mutation and the well-known edge recombination and order crossovers, while the TS procedures are adaptations of Cordeau et al. (2001). The fitness value of solutions is based on the number of vehicles, distance and waiting times. The pool is initialized with a set of four simple construction heuristics: least successor, double-ended nearest neighbor, multiple fragments (which adds sequentially the shortest arcs) and shortest arc hybridizing (a probabilistic version of the previous). The initial and final solutions are post-optimized with an ejection chain procedure and well-known 2-opt, 3-opt, and Or-opt improvement heuristics. Alternative approaches are ant colony, bee and bat algorithms. Most of them belong to population-based algorithms with particular features.

### 2.5. The multi-objective approach

Ombuki, Ross, and Hanshar (2006) represent the VRPTW as a multiobjective problem and present a genetic algorithm solution using the Pareto ranking technique. The authors use a direct interpretation of the VRPTW as a multi-objective problem, in which the two objective dimensions are the number of vehicles and total cost (distance). An advantage of this approach is that it is unnecessary to derive weights for a weighted sum scoring formula. This prevents the introduction of solution bias towards either of the problem dimensions. The authors argue that the VRPTW is most naturally viewed as a multi-objective problem, in which both vehicles and cost are of equal value, depending on the needs of the user. A result of their research is that the multi-objective optimization genetic algorithm returns a set of solutions that fairly consider both of these dimensions. Their approach is quite effective, as it provides solutions competitive with the best known in the literature,
as well as new solutions that are not biased toward the number of vehicles. A set of well-known benchmark data are used to compare the effectiveness of the proposed method for solving the VRPTW.

Chand and Mohanty (2011) proposed a multi objective genetic algorithm (MOGA) for the VRPTW in order to minimize the number of vehicles used, the total distances traveled by the vehicles, and the time window violation (routing time). In their approach, a chromosome representing route of length $N$, where $N$ is the number of customers in a particular problem instance. A gene in a given chromosome indicates the original node number assigned to a customer, while the sequence of genes in the chromosome indicates the order of visitation of customers. For crossover and mutation operators, best cost route crossover techniques and exchange mutation procedures are used respectively. The authors use dominance-information of the individuals of the population by calculating for each individual $i$ the number of alternatives $X_{i}$ from which this individual is dominated. Individuals that are not being dominated by others should receive a higher fitness value than individuals that are being dominated. The authors did experimental results using the Solomon's data set.

Kumar, Thansekhar, Saravanan, and Amali (2014) detailed a fitness aggregated genetic algorithm (FAGA) to solve the multi objective problem. The fitness considered in this research is: the number of vehicles used, the total distances traveled by the vehicles, and the route balance. The algorithm mentioned uses specialized operators like selection based on aggregate fitness value, and the best cost route crossover. The algorithm was tested on a large number of Solomon's benchmarks for a biobjective model that is a minimization of the total distance travelled and the total number of vehicles used. After validation, the third objective that is route balance is incorporated into the bi-objective model and it is observed that FAGA produces better-balanced routes without affecting the total distance travelled and total number of vehicles used.

### 2.6. Recent work

Afifi, Dang, and Moukrim (2016) propose a simulated annealingbased algorithm for the VRPTW and synchronized visits (VRPTWSyn), where each client requires simultaneous visits from different vehicles as the main characteristic. The algorithm uses local improvement methods to deal with the problem mentioned above. Berghida and Boukra (2015) present an enhanced biogeography-based optimization algorithm (EBBO) for the HVRPMBTW (vehicle routing problem with a heterogeneous fleet, mixed backhauls, and time windows). The available vehicles have different capacities and costs. Two types of customers are served, i.e., linehaul and backhaul customers. The authors combine the biogeography-based optimization (BBO) approach with a simulated annealing algorithm to enhance solution quality. The approach mentioned produces satisfactory results compared to other approaches such as particle swarm optimization (PSO). de Armas and Melián-Batista (2015) detail a dynamic vehicle routing problem in the Canary Islands, Spain, where the demands can be either known at the beginning of the planning horizon or dynamically revealed during it. The research considers a fixed heterogeneous fleet of vehicles, customer priorities and vehicle/customer constraints. This work proposes a general variable neighborhood search (GVNS) as a meta-heuristic procedure. Nalepa and Blocho (2016) introduce an adaptive memetic algorithm for the VRPTW (AMA-VRPTW) to minimize the total travel distance. The parameters of the algorithm, including the population size, selection scheme and the number of offspring, are adjusted dynamically during the search. The performance of the algorithm is investigated in a sensitivity analysis.

Schwarze and Voß (2015) analyze a VRP extension. It is motivated by an application in airport ground control where time issues play a major role. The research includes an extensive numerical study with load-balancing aspects as well as a multi-objective analysis. Soenpracha, Mungwattana, and Manieri (2015) considers the customer demand as uncertain in a mix-VRPTW. The research examines meta-

heuristic algorithms based on a genetic algorithm and an adaptation of a greedy search hybridized with inter-route neighborhood search methods. Yang, Guo, and Liu (2015) investigate and compare heuristic algorithms for the VRPTW. These heuristic algorithms combine three classical heuristic algorithms with the cross exchange method and the 2-opt exchange heuristic respectively. Barbucha (2014) proposes a new approach for the VRPTW. It integrates the asynchronous team paradigm with the island-based evolutionary algorithm concept. The process of solving the problem is carried out by the set of agents, each representing a heuristic algorithm. Agents are grouped in teams working in islands. Each team of agents periodically communicates with other teams by sharing a promising result. Gan, Kuang, and Niu (2014) present the multi-type vehicle routing problem with time windows (MTVRPTW). The research considers both multiple types of the vehicle and the uncertain number of vehicles of various types. Six variants of particle swarm optimization (PSO) are used. Li, Li, and Pardalos (2016) study the multi-depot vehicle routing problem with time windows under shared depot resources (MDVRPTWSDR). In this research, the depot where the vehicle ends is flexible. Thus, it is not entirely the same as the depot that it starts from. The authors implement a hybrid genetic algorithm with adaptive local search.

Recent authors have used well recognized and published methodologies with some modifications in order to solve the VRPTW. Figliozzi (2010) offers an algorithm based on route construction and improvement. The algorithm mentioned can be applied sequentially to solve the VRP with Soft Time Windows (VRPSTW) and Hard Time Windows (VRPHTW). Soft time windows are useful when the customers may be incapable or unwilling to set precise time windows in advance and simply prefer the flexibility to alter their pickup or delivery requests. Computational results detail the performance of the proposed algorithm against other well recognized and published solution methods using the Solomon (1987) benchmark problems.

Tas, Dellaert, van Woensel, and Kok (2013) study a vehicle routing problem with soft time windows and stochastic travel times. The authors propose a TS method, a well-recognized and published methodology, to solve the problem mentioned. The Solomon (1987) instances were used to obtain competitive final solutions. In the first phase of the algorithm, an initial solution is constructed by Solomon (1987) a heuristic method. In the second phase, the initial solution is improved by a TS method based on research by Cordeau et al. (2001). In the third phase, a post-optimization method is applied to improve the solution obtained by the second phase.

Vidal, Crainic, Gendreau, and Prins (2013) address efficiently a wide range of large-scale VRP variants. The authors highlight that the most successful approaches to solving the VRPTW involve local search improvement procedures based on arc- and node-exchange neighborhoods. The authors indicate that the most competitive results are currently offered by the hybrid genetic algorithm (HGA) to solve VRP variants. The HGA combines well recognized and published methodologies such as powerful route minimization procedures, effective edge assembly cross operators, and extremely efficient local search procedures. These methods stand out in terms of simplicity and wider applicability. The authors conclude that the design of efficient localsearch methods should be investigated to obtain suitable solutions.

The review mentioned above clearly underlines several gaps in the actual state of the art. The algorithms mentioned have greedy procedures to obtain promising solutions. The performance of the algorithms is implicit in the greedy procedures. Therefore, the greedy procedures are replaced by an explicit probability distribution over the set of permutations using the Mallows (1957) model. With this change, we have control to characterize the solution space explicitly. In addition, most current algorithms tackle the problem with the cluster-first routesecond strategy, i.e., the procedures mentioned above determine clusters of customers compatible with the constraints, and solve the routing problem for each cluster. However, the opposite approach, called routefirst cluster-second, builds a giant tour covering all customers and splits
it into feasible trips, as shown Fig. 1. This opposite approach has nevertheless led to successful meta-heuristics for various vehicle routing problems in the last decade (Prins, Lacomme, \& Prodhon, 2014). In addition, the solution representation used in specific cross operators have a strong impact on the efficiency and scalability of metaheuristics for the VRPTW. In a traditional approach to the solution representation, the vertices are independent of each other. It means that any vertex can be relocated to another position in the sequence (giant tour) in order to get better solutions. However, most published papers consider that the rest of the vertices are not necessarily affected (influenced) by the relocating processes because nobody knows if a dependency situation exists among them. Finally, although different algorithms have been proposed in order to solve the VRPTW problem successfully, these published algorithms consider the vertices independent of each other. It could be disadvantageous if a relation or interaction among vertices in the problem exists. To preserve any relationship or interaction using a probability model is the objective and has not been considered in all the current research. To the best of our knowledge, probability models by means of an EDA have not been used to tackle the VRPTW problem.

## 3. HMEDA - for the VRPW

The traditional permutation-based representation is adopted in this research. The representation mentioned is a giant tour of all the locations of the customers, i.e., in each position on the representation a vertex is depicted. Therefore, a representation is simply a sequence of vertices (permutation) $S$ of $n$ vertices without route delimiters. If a vehicle could visit all customers one by one, the representation would detail the order in which the vehicle could perform the sequence. The fitness F(S) of $S$ is the number of vehicles and the total distance used in the solution. This representation without route delimiters is suitable for using traditional evolutionary operators as highlighted in the research of Prins (2004). However, in this research, the traditional operators are not required in order to get competitive offspring.

To explain the representation, we provide an example by considering a problem with 7 vertices as shown in Table 3. Fig. 6 illustrates the representation used in this research.

Based on Fig. 6, a vehicle goes to vertex (customer location) number five at the beginning, after which it goes to vertex number four, and so on until it goes back to the depot (vertex zero), which does not show in the solution representation in this research.

The initial population are arrays of $M$ vectors, where $M=1000$, of size $n$ vertices each one. Each vector is initialized as a random permutation of vertices (customers).

### 3.1. Pareto-front construction phase

In each generation, a Pareto-front approach is built with the population. A Pareto-front approach is considered in this research based on Kacem, Hammadi, and Borne (2002). The optimality notion in the Pareto approaches can be formulated as follows: the Pareto-optimal set is formed by non-dominated solutions. $x$ vector dominates $y$ vector if

## Table 3

Data used in Fig. 6.


![img-7.jpeg](img-7.jpeg)

Fig. 6. Illustration of a sequence (giant tour) for the VRPTW.
$\forall 1 \leq q \leq L, f_{q}(x) \leq f_{q}(y)$ where $f_{q}($.$) is the q$ th objective function, $L$ is the number of objective functions and at least one index $r$ exists such that $f_{r}(x)<f_{r}(y)$. A solution is non-dominated if it is not dominated by any other solution. Fig. 7 details the fitness of two feasible solutions as a Pareto-optimality approach example. A non-dominated set of solutions in each generation is found and used for the selection process, as well as for the improvement of the central permutation estimate $\alpha_{0}$ in the GMD process.

The selection process takes the subset $N$ from $M$ parents (where $N<M$ ) chosen by a tournament selection which is executed based on where the candidate solutions are located on the Pareto-front approach. Different cases are possible as follows: if a solution is feasible and another is infeasible, the feasible solution is preferable. If a solution is non-dominated and another is dominated, the non-dominated solution is preferable. If both solutions are non-dominated, the solution that belongs to a better Pareto-front layer is preferable.

In order to determine which Pareto-front layer belongs to each nondominated solution, we calculate two entities: (1) domination count $n_{p}$, the number of solutions which dominate the solution $p$, and (2) $S_{p}$, a set of solutions that the solution $p$ dominates. All solutions in the first nondominated front will have their domination count as zero. Now, for each solution $p$ with $n_{p}=0$, we visit each member $(q)$ of its set $S_{p}$ and reduce its domination count by one. In doing so, if for any member $q$ the domination count becomes zero, we put it on a separate list $Q$. These members belong to the second non-dominated front. Thus, the above procedure is continued with each member and the third front is identified. This process continues until all fronts are identified.

### 3.2. Probability model proposed

Based on the related work section mentioned above, traditional evolutionary operators are used to produce a new population, i.e., performing two main processes (crossing and mutation) to different permutations (parents) in order to build a new permutation (child). These processes have an implicit contribution on the performance of the algorithm used. However, we do not have control to characterize the solution space. Therefore, those processes are replaced by an explicit probability distribution over the set of permutations using the Mallows model in this research.

The Mallows model was initially proposed by Mallows (1957), and later improved by Fligner and Verducci (1986) through the generalized Mallows distribution (GMD). The Mallows model and the GMD can be used to solve permutation-based optimization problems. More recently, Ceberio et al. (2014) contribute with an initial application of the GMD to solve the flowshop scheduling problem coupled with EDAs.

Formally, the Mallows model is defined as
$P(\sigma)=\psi(\tilde{v})^{-1} \exp \left(-\tilde{v} D\left(\sigma, \alpha_{0}\right)\right)$
where $\tilde{v}$ is a spread parameter, and $D\left(\sigma, \alpha_{0}\right)$ is the distance from $\sigma$ to the central permutation $\alpha_{0}$, where $\psi(\tilde{v})$ is a normalization constant. In the present work, Kendall's $\cdot \tau$ is the distance metric with which the Mallows model is coupled.

Let's consider $\alpha_{0}=\left(\begin{array}{cccccccc}1 & 2 & 3 & 4 & 5 & 6\end{array}\right)$ as a central permutation, i.e., a Giant tour. The number of elements in $\alpha_{0}$ is based on the detailed example in Table 3 and Fig. 6.

![img-8.jpeg](img-8.jpeg)

Fig. 7. A graphical representation fitness of two feasible solutions as a Pareto-optimality approach.

Let $\sigma_{1}=\left(\begin{array}{cccccc}1 & 4 & 5 & 2 & 3 & 6 \\ 1 & 1 & 2 & 3 & 4\end{array}\right)$ as another Giant tour with $D\left(\sigma_{2}, \sigma_{0}\right)=4$

$$
\text { Let } \sigma_{2}=\left(\begin{array}{cccccc}
5 & 4 & 2 & 1 & 3 & 6 \\
5 & 4 & 2 & 1
\end{array}\right) \text { with } D\left(\sigma_{2}, \sigma_{0}\right)=8
$$

Based on Mallows model, every permutation $\sigma_{i}$ gets a probability that decays exponentially with respect to its distance to the central permutation $\sigma_{0}$. Therefore, $\sigma_{2}$ has less probability than $\sigma_{1}$. Fig. 8 depicts a visual representation of the previously detailed example.

The GMD decomposes Kendall's $\tau$ distance metric into $m-1$ terms in such a way that it can be expressed as $D\left(\sigma, \sigma_{0}\right)=D_{\tau}\left(\sigma, \sigma_{0}\right)=\sum_{q=1}^{m-1} V_{q}\left(\sigma, \sigma_{0}\right)$. The GMD is given as follows
$P(\sigma)=\psi(\boldsymbol{\theta})^{-1} \exp \left(\sum_{q=1}^{m-1}-\tilde{u}_{q} V_{q}\left(\sigma, \sigma_{0}\right)\right)$
where $V_{q}\left(\sigma, \sigma_{0}\right)$ is the number of positions on the right of $q$ with values smaller than the current position on the permutation $\left(\sigma, \sigma_{0}\right)$. Based on the example above, for $\sigma_{1}$, the $V_{q}\left(\sigma_{1}, \sigma_{0}\right)$ values for the $q$ th position is detailed below


The same procedure to identify the Kendall's $\tau$ distance metric in $\sigma_{2}$, i.e., the $V_{q}\left(\sigma_{2}, \sigma_{0}\right)$ values for the $q$ th position is detailed below


Instead of a single spread parameter $\tilde{v}$ as in the Mallows distribution, the GMD uses $m-1$ spread parameters $\tilde{v}=\left(\tilde{v}_{1}, \tilde{v}_{2}, \ldots, \tilde{v}_{m-1}\right)$, every $\tilde{u}_{q}$ affecting a particular position $q$ of the permutation. Based on Fligner and Verducci (1988), it is possible to determine any permutation $\left(\sigma, \sigma_{0}\right)$
with the $m-1$ integers $V_{1}\left(\sigma, \sigma_{0}\right), \ldots, V_{m-1}\left(\sigma, \sigma_{0}\right)$ in which Kendall's- $\tau$ distance $D_{\tau}\left(\sigma, \sigma_{0}\right)$ decomposes. Under the uniform distribution, the $V_{q}\left(\sigma, \sigma_{0}\right)$ variables that define a permutation are independent (Fligner \& Verducci, 1986), and as a consequence, the probability distribution of the random variables $V_{q}\left(\sigma, \sigma_{0}\right)$ under the GMD given by Eq. (2) can be written as
$P\left(V_{q}\left(\sigma, \sigma_{0}\right)=r_{q}\right)=\frac{\exp \left(-\tilde{v}_{q} r_{q}\right)}{\tilde{u}_{q}\left(\tilde{v}_{q}\right)} \quad r_{q} \in\{0, \ldots, m-q\}$
The normalization constant $\psi(\boldsymbol{\theta})$ in the GMD can be simplified as the product of $m-1$ terms
$\psi(\boldsymbol{\theta})=\prod_{q=1}^{m-1} \tilde{u}_{q}\left(\tilde{v}_{q}\right)=\prod_{q=1}^{m-1} \frac{1-\exp \left(-\tilde{v}_{q}(m-q+1)\right)}{1-\exp \left(-\tilde{v}_{q}\right)}$
where $m$ is the total number of items in the permutation. When the GMD considers Kendall's- $\tau$ distance, it can be expressed as a multi-stage ranking model (Fligner \& Verducci, 1988). Therefore, the probability distribution of a given permutation $\sigma$ is given as
$P(\sigma)=\prod_{q=1}^{m-1} P\left(V_{q}\left(\sigma, \sigma_{0}\right)=r_{q}\right)$
where $r_{q}$ is a possible value for the $q$ position on the $V_{q}$.
The first stage consists of computing an approximation of the central permutation $\sigma_{0}$. Although the behavior of the GMD depends on the spread vector $\tilde{v}$ that determines the shape of the distribution (Ceberio et al., 2014), future research is aimed at improving the estimation of the central permutation $\sigma_{0}$ to enhance the performance of the algorithm. To avoid losing diversity through modification in the central permutation is the goal. In this research, when a non-dominated set of solutions is found in the Pareto-front approach mentioned above, the corresponding vectors of the non-dominated set of solutions are used as an input


![img-9.jpeg](img-9.jpeg)

Fig. 8. A visual representation of the Kendall's $\rightarrow$ distance metric.
parameter by the Borda algorithm (1784) to get a better approximation to the central permutation $\sigma_{0}$. To the best of our knowledge, a modification on the parameter described has not been developed for these kinds of algorithms. The following procedure details an example in order to estimate the central permutation $\sigma_{0}$ with the Borda algorithm using the corresponding vectors of the non-dominated set of solutions.

```
Pseudocode 1. Central permutation computation \(\sigma_{0}\)
\(\mathrm{m} \leftarrow\) number of vertices
\(\mathrm{M} \leftarrow\) Individuals
from the non - dominated set of permutations \(\left[\sigma_{0}, \cdots, \sigma_{M}\right]\)
for \(\mathrm{j}=1\) to m
Compute \(\pi(j)=\sum_{i=1}^{M} \sigma_{i}(j) / M\)
Endfor
visited \(=\{\varnothing\}\), auxiliary array
for \(\mathrm{j}=1\) to m
Find the lowest value from \(\pi(i)\)
index \(\leftarrow \arg \min \left\{\pi(i) \circ \varnothing \text { visited }\right\}\)
Building \(\sigma_{0} \cdots\)
\(\sigma_{i}\) (index) \(=\mathrm{j}\)
visited \(=\) visited \(\cup\) index
Endfor
```

Once the central permutation $\sigma_{0}$ is approximated using the Pareto-front
approach, the second stage consists of computing the dispersion parameters $\tilde{v}_{j}$ by solving
$\tilde{V}_{j}=\frac{1}{\exp \left(\tilde{v}_{0}\right)-1}-\frac{m-q+1}{\exp \left(\tilde{v}_{0}(m-q+1)\right)-1}, q=1: m-1$
where $\tilde{V}_{0}=\frac{1}{q} \sum_{i=1}^{q} V_{0}\left(\sigma_{i} \sigma_{0}\right)$
With the spread parameter vector generated $\boldsymbol{\theta}$ and the central permutation estimated $\sigma_{0}$, it is possible to create the probability matrix called P to obtain new $\boldsymbol{V}\left(\sigma, \sigma_{0}\right)$ vectors by Eq. (3). The element $p_{i q}(l)$ of the probability matrix P represents the probability that vertex $j$ requires $r$ number of adjacent transpositions required to match the vertex $j$ in the same $q$ th position as the central permutation $\sigma_{0}$ at generation $l$.

Fig. 9 depicts a visual example, for only two positions on the sequence, in the probability matrix P. Based on the previous example above, the $r_{0}$ possible values, for a new $\boldsymbol{V}\left(\sigma, \sigma_{0}\right)$ vector, will be between 0 and $m-q$, where $q$ represents the positions on the sequence.

For each $q$ th position, the probability of each $r_{0}$ value, i.e., $p_{i q}$, refers to the importance of an operation for a specific position of the per-mutation-based representation. For all $j(j=1,2, \cdots, m)$ and $q(q=1,2, \cdots, m-1)$.

In this way, this research characterizes the space of possible solutions explicitly through the estimation of the probability that a vertex, for a specific position of the permutation-based representation, is selected.

Probability matrix
$\mathrm{q}=1$, i.e., first position on the sequence
$\begin{array}{llllllll}\text { r } & 0 & 1 & 2 & 3 & 4 & 5\end{array}$
$\mathrm{p}(\mathrm{r})$ .653221 .228771 .0801203 .0280598 .0098271 .0000008$
![img-10.jpeg](img-10.jpeg)
$\mathrm{q}=2$, i.e., second position on the sequence
$\begin{array}{llllllll}\text { r } & 0 & 1 & 2 & 3 & 4\end{array}$
$\mathrm{p}(\mathrm{r})$ .68619 .220339 .070752 .0227188 .0000001$
![img-11.jpeg](img-11.jpeg)

Fig. 9. A probability matrix example.
![img-12.jpeg](img-12.jpeg)

Fig 10. GMD process for the VRPTW problem.

The process of generating the new valid permutations is decoding the $\boldsymbol{V}\left(\sigma, \sigma_{0}\right)$ vectors. This research uses the Meilă et al. (2007) algorithm for transforming the vectors mentioned above in valid permutations. The following procedure represents an example to get a valid permutation.

```
Pseudocode 2. Meilă et al. (2007) procedure
m - number of vertices
Let a sample vector V \(\left(\sigma, \sigma_{0}\right)=2,0,1\)
therefore m: \(=4\)
insert m in \(0 \rightarrow\left(\sigma, \sigma_{0}\right)^{-1}=4\)
insert j: \(=3\) in \(V_{j:}=1 \rightarrow\left(\sigma, \sigma_{0}\right)^{-1}=4,3\)
insert j: \(=2\) in \(V_{j:}=0 \rightarrow\left(\sigma, \sigma_{0}\right)^{-1}=2,4,3\)
insert j: \(=1\) in \(V_{j:}=2 \rightarrow\left(\sigma, \sigma_{0}\right)^{-1}=2,4,1,3\)
Every permutation \(\sigma\) is obtained by inverting a composing
with the central permutation \(\left.\sigma_{0},\left(\left(\sigma, \sigma_{0}\right)^{-1}\right)^{-1} \sigma_{0}=\sigma \sigma_{0}^{-1} \sigma_{0}=\sigma\right.\)
```

Finally, Fig. 10 details the overall process for GMD process mentioned above.

### 3.3. Split criteria

Once the sequence of vertices (permutation) $S$ of $n$ vertices without route delimiters is obtained by the GMD, a procedure should be done in

Table 4
Comparison of results with Homberger and Gehring (2005) instances.

![img-13.jpeg](img-13.jpeg)

Fig. 11. Performance of the algorithms for the number of vehicles.
order to get the feasible routes for all vehicles required. The best partition of the sequence of vertices mentioned can be computed using an optimal splitting procedure. The procedure of Labadi, Prins, and Mohamed (2008) is used in this research. As the authors explain, the procedure computes the shortest path in an auxiliary graph $H$ containing one dummy node 0 and $n$ other nodes corresponding to the $n$ vertices. Each subsequence of vertices $\left(S_{i}, S_{i+1}, \ldots, S_{j}\right)$ corresponding to a feasible trip is modelled by a weighted arc $(i-1, j)$ in $H$. Note that any trip that violates time windows or vehicle capacity is discarded at this level. The shortest path from node 0 to node $n$ in $H$ can be computed using Bellman's algorithm for directed acyclic graphs. It indicates where to split $S$ to get an optimal solution, subject to the order imposed

Table 5
Comparison of the results.
![img-14.jpeg](img-14.jpeg)

Fig. 13. Comparison of results using boxplots.
by S. Fig. 1 gives an example of splitting for the instance defined by Table 1.

Finally, the HMEDA procedure to solve the VRPTW is illustrated below.

# Dunnett multiple comparison test for the VRPTW 

![img-15.jpeg](img-15.jpeg)

Fig. 12. Dunnett multiple comparison test.

Table 6
Distribution of the results.

* Rest of data.


## Pseudocode 3. HMEDA framework for the VRPTW

$D_{0} \leftarrow$ Generate M individuals
$\mathrm{t}:=1$
Do
$\mathrm{D}_{\mathrm{t}-1} \leftarrow$ Evaluate individuals
(number of vehicles and total distance traveled by the vehicles used)
$P_{t-1} \leftarrow$ Compute Pareto front from $D_{t-1}$
$\mathrm{Dn}_{\mathrm{t}-1} \leftarrow$ Select N individuals from $\mathrm{Dn}_{\mathrm{t}-1}$
Compute a matrix, called P matrix, from $\mathrm{Dn}_{\mathrm{t}-1}$
Estimate central permutation $\sigma_{0}$ from $P_{t-1}$
Estimate spread parameters $\hat{\sigma}$ from $\mathrm{Dn}_{t-1}$ and $\sigma_{0}$
$\mathrm{Dn}_{\mathrm{t}} \leftarrow$ Sample M individuals from P matrix
$D_{t} \leftarrow$ Find best individuals from $\mathrm{Dn}_{t-1} \cup \mathrm{Dn}_{t}$
$\mathrm{t}:=\mathrm{t}+1$
Until (stopping criterion is met)

## 4. Results and comparison

### 4.1. Comparison with a standard benchmarking dataset

In order to validate the scientific relevance of this paper, we compare the HMEDA results with others in a general and standard
![img-16.jpeg](img-16.jpeg)

Fig. 15. Comparative results with recent algorithms.
benchmarking dataset, i.e., Homberger and Gehring (2005) instances. These instances can be found at https://www.sintef.no/projectweb/ top/vrptw/homberger-benchmark/200-customers/.

The instances consider different factors such as geographical data, the number of customers serviced by a vehicle; the percent of timeconstrained customers, and tightness and positioning of the time windows. The geographical data are randomly generated in problem sets R 1 and R 2 , clustered in problem sets C 1 and C 2 , and a mix of random and clustered structures in problem sets by RC1 and RC2. Therefore, there are six sets of problems in Homberger and Gehring (2005) instances. The travel times equal the corresponding distances.

The instances mentioned above are used as input data for the comparison. The experiments are executed in a Lanix ${ }^{\circledR}$ Titan HX 4200 computer, Intel ${ }^{\circledR}$ Core $^{\mathrm{TM}} \mathrm{i} 7$ processor, 3.4 GHz , 8 GB of RAM, Windows ${ }^{\circledR}$ 10 for 64 bits to run every instance. $\mathrm{C}++$ language is used for the

Dunnett multiple comparison test for the VRPTW
![img-17.jpeg](img-17.jpeg)

Fig. 14. Statistical test.

![img-18.jpeg](img-18.jpeg)

Fig. 16. Dunnett statistical test.
![img-19.jpeg](img-19.jpeg)

Fig. 17. Geographical distribution for distributed cities and distribution center in Jalisco Province.
implementation for all the comparisons. To account for the stochastic nature of the HMEDA, we run 30 trials for all the dataset. Each trial contains 50 generations, 1000 solution vectors belonging to each generation. We measure the relative percentage increase (RPI) as:
$\operatorname{RPI}\left(c_{i}\right)=\left(c_{i}-c^{*}\right) / c^{*}$
where $c_{i}$ is the number of vehicles obtained in the $i$ th replication, and $c^{*}$ is the best number of vehicles found and reported in the literature. The distribution of the experimental results in every interval is presented in

![img-20.jpeg](img-20.jpeg)

Table 8
Data for the bread routing problem.

Table 9
Multiple comparisons of means: Dunnett test for the bread routing problem.

Table 4. It is clear from the table that the results of the HMEDA algorithm are comparatively concentrated, which is mainly in the range of $[0,0.03]$, over the best solution found, i.e., number of vehicles, for all the instances. Based on the results, the HMEDA is a suitable approach for solving real-world routing problems.

### 4.2. Comparison with other estimation of distribution algorithms

The MIMIC algorithm, the COMIT algorithm, and the BOA algorithm are proposed as a benchmark for comparison with the HMEDA scheme. These EDAs try to capture the problem structure with more precision and attempt to integrate higher-order interactions to enhance the solution quality. The abovementioned instances are used as input data for the algorithms. The experiments are executed in the same computer and language specification.

Based on the results detailed below, the modification of the GMD using the Pareto approach is able to detect competitive sequences for the VRPTW. Fig. 11 details the performance of the algorithms, based on the RPI, when we analyze the number of vehicles. The HMEDA scheme outperforms all the algorithms used in the comparison.

A Dunnett test was executed to show the performance of the HMEDA scheme. Dunnett's test is a multiple comparison procedure after a significant ANOVA result. It compares means from several experimental groups (algorithms) against a specific control group mean (the HMEDA scheme) to examine if there are significant statistical differences (Montgomery, 1997). Fig. 12 states that there is a
statistically significant difference between the algorithms by means of a Dunnett test. The HMEDA scheme outperforms all the algorithms used in the comparative.

### 4.3. Comparison with multi-objective algorithms

Furthermore, in order to enhance the novelty of the HMEDA, we consider evaluating the HMEDA with the multi-objective algorithms proposed by Srinivas and Deb (1994) called NSGA, and by Deb, Pratap, Agarwal, and Meyarivan (2002) called NSGA-II as a benchmark for comparison with the HMEDA scheme. The code of the proposed algorithms are obtained from the Kanpur Genetic Algorithms Laboratory web. Again, the aforementioned instances are used as input data for the algorithms. The experiments are executed in the same computer and language specification.

Two conflicting objectives are analyzed: the number of vehicles and the total distance traveled by the vehicles used. The aim is to prevent a solution from assigning too much vertices on a single vehicle and to keep the balance of traveled distance distribution over the vehicles. The objectives mentioned above are used as input data to find the response variable for the experiment, i.e., we compute the area obtained from the best Pareto-front after running every algorithm.

We measure the RPI using the same Eq. (7), i.e., $c_{i}$ is the area obtained from the best Pareto-front obtained in the $i$ th replication by a given algorithm configuration, and $c^{v}$ is the best area found by any of the algorithm configurations. Note that for this problem, there are no known effective or exact techniques, and comparison with an optimal solution is not possible. Table 5 depicts the mean and standard deviation metrics for all the algorithms used for the comparison of over 30 independent runs per instance.

Fig. 13 includes three box plots: the NSGA, the NSGA-II, and the HMEDA performance after running all the instances. As we can see, the HMEDA is competitive in order to identify the best-performing ones. Although the GMD process is enough to find suitable solutions, the Pareto-approach helps to improve the results when the non-dominated solutions are considered in the GMD process. The HMEDA results report how the performance of the algorithm is improved.

The distribution of the experimental results in each interval is presented in Table 6. It is clear from the table that the results of the HMEDA algorithm are comparatively concentrated, which is mainly in the range of $[0,0.03]$, similar to the results of the other algorithms. In addition, we analyze whether there is a statistically significant difference between the averages of the algorithms. Fig. 14 depicts the statistical test, i.e., the Dunnett test. As we can see, the proposed HMEDA is competitive. There is a difference between the HMEDA with the other algorithms for the VRPTW. We confirm that the hybridization between the GMD process and the Pareto-front approach is suitable for the EDA scheme. Thus, the HMEDA algorithm in terms of solving the VRPTW is more robust than the other algorithms.

### 4.4. Comparison with recent algorithms for the VRPTW

Based on the previous results in the last comparison mentioned above, recent algorithms are proposed as a benchmark for comparison with the HMEDA scheme, i.e., the Figliozzi (2010) algorithm, the Tas et al. (2013) algorithm, and the Vidal et al. (2013) algorithm. Again, the instances mentioned in the previous section are used as input data for the algorithms. The experiments are executed in the same computer and language specification. Fig. 15 shows the performance of these algorithms based on the aforementioned RPI. As we can see, the performance of the proposed algorithm, i.e., the HMEDA outperforms all the algorithms used in the comparative (see Fig. 16).

## 5. Simulation and preliminary implementation

There is a bread company from México that sells to different cities

![img-21.jpeg](img-21.jpeg)

Fig. 18. Dunnett multiple comparison test for the bread routing problem.
![img-22.jpeg](img-22.jpeg)

Fig. 19. Geographical distribution for the new locations of the bread company.
through the Guadalajara distribution center in Jalisco Province (Guadalajara is the capital of Jalisco Province), and their locations are distributed as shown in Fig. 17. The distances between customers are obtained directly on the road as detailed in Table 7. Data for the bread
routing problem is depicted in Table 8.
A comparison is made between the recent algorithms and the proposed HMEDA over 30 days. The comparison is shown in Table 9, which lists the p-value of the Dunnett test. Fig. 18 details that the proposed

Table 10
Multiple comparisons of means: Dunnett test for the new locations of the bread routing problem.
algorithm is competitive in real-world routing problems.
Furthermore, the bread company is considering extending its scope to other cities. The new locations are shown in Fig. 19. More than one hundred cities are located in this scenario. A new comparison, as a simulation with diverse demands, is made between the aforementioned recent algorithms and the proposed HMEDA. The comparison is shown in Table 10, which indicates the p-value of the Dunnett test. Finally, Fig. 20 shows that the proposed algorithm is competitive in real-world routing problems. There is a statistically significant difference between all the algorithms used in the comparison and the HMEDA scheme. The HMEDA outperforms all the algorithms used in the comparison.

Finally, the time efficiency of the algorithms is detailed below. As we can see, the HMEDA outperforms all the algorithms used in the comparison (see Fig. 21).

## 6. Conclusions and future research

This paper discusses the VRPTW, which considers additional time constraints. Here, the service of a customer should begin within a time window $\left[a_{i}, b_{i}\right]$. The vehicle should not arrive earlier than time $a_{i}$ and no later than time $b_{i}$. A vehicle arriving before time $a_{i}$ will produce a waiting time. A vehicle arriving after time $b_{i}$ will incur a delay. To solve this problem, we propose the HMEDA application scheme. By means of numerical experiments, this approach generates competitive solutions.

This novel research concludes that the GMD can be coupled with the EDA scheme in order to solve combinatorial optimization problems,
![img-23.jpeg](img-23.jpeg)

Fig. 21. Time efficiency.
such as the VRPTW from a multi-objective perspective. By using the Pareto-front approach, it is possible to obtain better solutions for the VRPTW. The computational results establish that the different probability models used for the VRPTW with large data sets are suitable. The Pareto-front approach is not only used for obtaining the best solutions for the HMEDA scheme, it is also used to propose a different way of improving the estimation of the central permutation $\sigma_{k}$ in the GMD process. The HMEDA provides an effective estimate of the vertices at the positions in the sequence vector for the VRPTW.

Moreover, the HMEDA scheme proposed guarantees that the characteristics will persist for all members of the population in the evolutionary progress of the probability model proposed, i.e., the GMD.

Furthermore, the HMEDA scheme is a new option for the aforementioned approach, called route-first cluster-second.

Explicit probability distributions in the domain of permutations for the VRPTW should be considered in future research. Estimating relationships for other related dynamic routing issues, e.g., vehicle
![img-24.jpeg](img-24.jpeg)

Fig. 20. Dunnett multiple comparison test for the bread company considering extending its scope to other cities.

maintenance, new vertices, and online environments, should be reconsidered in light of these results. Since the HMEDA presents stability, it appears very suitable for implementation in software systems for practical purposes. Further research directions may deal with an extension of the HMEDA for building effective modules for specific users in the industry. Finally, the HMEDA might be used in other types of VRP.
This research is focused on only one type of vehicle, i.e., a homogeneous fleet of vehicles. Therefore, a heterogeneous fleet of vehicles appears to vary significantly in dynamic environments. Assigning the right vehicles to the right vertices may also affect travel time. This remains research to be carried out in the future. Furthermore, our research should be expanded to account for other delay factors, such as traffic, windows in drivers, and other changes that can be addressed by developing a dynamic version of the EDA.

## Acknowledgements

We would like to express our gratitude to all the reviewers for their comments in improving the manuscript.
