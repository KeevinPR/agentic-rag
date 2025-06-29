# The Improved Estimation of Distribution Algorithms for Community Detection 

Zhou Ben-Da ${ }^{1,2}$<br>${ }^{1}$ School of Finance \& Mathematics, West Anhui<br>University, Lu’an Anhui, China<br>${ }^{2}$ Financial Risk Intelligent Control and Prevention<br>Institute,West Anhui University,Lu'an, Anhui, China<br>e-mail: bendazhou@163.com<br>Zhao Pan ${ }^{1,2}$<br>${ }^{1}$ School of Finance \& Mathematics, West Anhui<br>University, Lu'an Anhui, China<br>${ }^{2}$ Financial Risk Intelligent Control and Prevention<br>Institute,West Anhui University,Lu'an, Anhui, China<br>e-mail: zhaopan@163.com

## Zhang JinBo ${ }^{1,2}$

${ }^{1}$ School of Finance \& Mathematics, West Anhui University, Lu'an Anhui, China
${ }^{2}$ Financial Risk Intelligent Control and Prevention Institute,West Anhui University,Lu'an, Anhui, China
e-mail: jinbozhang@163.com


#### Abstract

Based on the analysis of local monotonic of modularity function, this paper designs a fast and effective mutation operator, and then proposes an improved Estimation of Distribution Algorithm (EDA) for solving community detection problem. The proposed algorithm is tested on basic network and big scale complex network. Experimental results show that this algorithm can get 0.4198 for the average $Q$ function while running 100 times, has better performance than Girvan-Newman(GN) algorithm, Fast Newman (FN) algorithm and Tasgin Genetic Algorithm (TGA).

Keywords-community detection; estimation of distribution algorithms(EDA); complex network; mutation with local search(LSM)


## I. INTRODUCTION

At present, studies of the basic statistical properties of complex networks have attracted the attention of many researchers from different fields. Thus, complex network analysis has become one of the most important interdisciplinary research areas ${ }^{[1-4]}$. The characteristics of nodes that belong to a specific class are the same in a network, which is also the case for the clustering characteristics, where nodes are more closely connected with nodes in the same class, whereas connections with different types of nodes are rare. The process of identifying each class in a network is known as network clustering (or network community detection). The study of this problem has major value for applications as well as theoretical significance because it has been used widely for Web community mining, protein function analyses, the prediction of metabolic pathways, and other uses ${ }^{[5-6]}$. In general, the evaluation function used to measure the network community structure is the module function proposed by Newman ${ }^{[6]}$ in 2004 (also known as the $Q$ function). The use of the $Q$ function as an objective function method for detecting the community structure of networks has increased since its proposal, although the maximum of the $Q$ function is NP-complete ${ }^{[7]}$. However, genetic algorithms (GAs), simulated annealing
(SA), and other intelligent optimisation methods have been applied successfully to solve this problem ${ }^{[8-11]}$.

Estimation of distribution algorithms (EDAs) are a new type of random optimisation algorithm, which are used increasingly in the field of evolutionary computation ${ }^{[12-14]}$. These methods combine GA theory and statistical learning rules and make full use of the global information related to a population to establish a probability distribution model for an individual space. The probability models are learned and sampled to generate a new solution, which facilitates population evolution ${ }^{[14]}$. EDAs can avoid certain GA operations such as crossover and mutation, which can improve their problem-solving capacity. However, EDAs cannot use local information directly during the evolution process because they lack a control mechanism for determining the local optimal solution. In this study, we propose a new distributed estimation algorithm to solve the community detection problem (EDA with LSM, LSMEDA) based on the analysis of the monotonicity of the $Q$ function, where the $Q$ function is used as a community detection quality metric. Further, gene mutation in the GA depends on the monotonicity of a $Q$ function designed for local search and mutation with the EDA, which improves the updating properties of the probability model.

## II. THE $Q$ FUNCTION AND ITS PROPERTIES

The design of the $Q$ function is based on the observation that as the network community structure becomes more obvious, the difference between it and random networks increases ${ }^{[7-11]}$. The specific details of the $Q$ function are described as follows.
Assume that we are given the undirected and unweighted network $N(V, E)$, the vertex set of $V$, and the set of edges of $E$, where $V$ is clustered (divided) into a number of communities. If we suppose that $R(i)$ are the community tags of node $i$, and the set $\operatorname{Cr}(i)$ is the community node set that $i$ belongs to, then the $Q$ function is expressed as

$$
Q=\frac{1}{2 m} \sum_{i, j}\left(\left(A_{i j}-\frac{k_{i} k_{j}}{2 m}\right) \times \delta(r(i), r(j))\right)
$$

where the adjacency matrix of the network is $A=\left(A_{i j}\right)_{n \times n}$, $\delta(u, v)=\left\{\begin{array}{ll}1 & u=v \\ 0 & u \neq v\end{array}\right.$, the degree of node $i$ is $k_{i}$, and the total number of edges is m .

The $Q$ function is the difference between the number of edges in the actual network within the community and a completely randomly connected community with the expected number.

In the following section, we start from the local viewpoint to analyze the $Q$ function; thus, we simplify equation (1) as follows:

$$
\left\{\begin{array}{l}
Q=\frac{1}{2 m} \sum_{v} f(i) \\
f(i)=\sum_{i \neq v_{i j}}\left(A_{i j}-\frac{k_{i} k_{j}}{2 m}\right)
\end{array}\right.
$$

The $Q$ function can be expressed by the function $f(i)$ of all nodes. Obviously, $f(i)$ can be understood as follows: the difference between the actual number of connections within the community and the expected number of connections in a randomly connected community. Thus, from the local viewpoint, $f(i)$ can measure the community structure of the network. The following discussion considers the related properties of $f(i)$.

Property 1: For any $i$ that belongs to $V, f(i)$ is only related to the community to which node $i$ belongs.

Proof: For $f(i)=\sum_{j \neq v_{i j}}\left(A_{i j}-\frac{k_{j} k_{j}}{2 m}\right)$, this formula is the sum of $j$, which is apparently only related to the nodes.

Property 2: The value of $Q$ function increases monotonically with $f(i)$.

Proof: Assume that the network $N=(V, E), C=\left\{c_{r}(i)\right.$, $\left.c_{(i j)}, \ldots, c_{(i q)}\right\}$ is a community division. $c_{r(i)}$ contains the nodes labelled with $r(i)$. For any $i$ that belongs to $V$, the community label is $r(i)$, and the corresponding community is $c_{r(i)}$. Suppose that only the community label of $i$ changes from $r(i)$ to $r(j)(r(i) \neq r(j))$, whereas the other nodes do not change, which forms a new community structure $\mathrm{C}^{\prime}$. Thus, $C^{\prime}$ contains $c_{r(i)}^{\prime}=c_{r(i)} /\{i\}$ and $c_{r(j)}^{\prime}=c_{r(j)} \cup\{i\}$. By combining function $f$ in formula (2), the definition of the $Q$ function, and Property 1 , the $f$ function value will be the corresponding changes, i.e. the set $c=c_{r(i)} \cup c_{r(j)}, c^{\prime}=c_{r(i)}^{\prime} \cup c_{r(j)}^{\prime}$. Of course, we have $c=c^{\prime}=c_{r(i)}^{\prime} \cup c_{r(j)} \cup\{i\}$; hence, we can discuss the changes in the value of function $f$ in $c$.

1) For any s in $c_{r(i)}^{\prime}$, there is:

$$
\Delta f_{s}=\sum_{i \neq v_{i j}}\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)-\sum_{i \neq v_{i j}}\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)
$$

for $c_{r(i)}^{\prime}=c_{r(i)} /\{i\}$; thus, $\Delta f_{s}=-\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)$. For any $q$ in $c_{r(i)}$, there is:

$$
\Delta f_{q}=\sum_{i \neq v_{i j}}\left(A_{q i}-\frac{k_{q} k_{i}}{2 m}\right)-\sum_{i \neq v_{i j}}\left(A_{q i}-\frac{k_{q} k_{i}}{2 m}\right)
$$

for $c_{r(j)}^{\prime}=c_{r(j)} \cup\{i\}$; thus, $\Delta f_{q}=\left(A_{q i}-\frac{k_{q} k_{i}}{2 m}\right)$.
For node $i$ : node $i$ that belonged to $c_{r(i)}$ now belongs to $c_{r(i)}^{\prime}$;
thus, $\quad \Delta f_{i}=\sum_{j \neq v_{i j}}\left(A_{i j}-\frac{k_{j} k_{j}}{2 m}\right)-\sum_{j \neq v_{i j}}\left(A_{i j}-\frac{k_{i} k_{j}}{2 m}\right)$ and, as defined by formula (2), we have:

$$
\begin{aligned}
& \Delta Q=\frac{1}{2 m}\left(\sum_{i \neq v_{i j}}\Delta f_{s}+\sum_{j \neq v_{i j}} \Delta f_{q}+\Delta f_{i}\right) \\
& =\frac{1}{2 m}\left(\sum_{q \neq v_{i j}}\left(A_{q i}-\frac{k_{q} k_{j}}{2 m}\right)-\sum_{i \neq v_{i j}}\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)+\Delta f_{i}\right)
\end{aligned}
$$

Because $c_{r(j)} \cup\{i\}=c_{r(j)}^{\prime}$ and $c_{r(i)}^{\prime} \cup\{i\}=c_{r(i)}$, we have:

$$
\sum_{q \neq v_{i j}}\left(A_{q i}-\frac{k_{q} k_{j}}{2 m}\right)+\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)=\sum_{q \neq v_{i j}}\left(A_{q i}-\frac{k_{q} k_{j}}{2 m}\right)
$$

In addition,

$$
\begin{aligned}
& \sum_{i \neq v_{i j}}\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)+\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)=\sum_{i \neq v_{i j}}\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right) ; \text { thus, } \\
& \Delta Q=\frac{1}{2 m}\left(\sum_{q \neq v_{i j}}\left(A_{q i}-\frac{k_{q} k_{j}}{2 m}\right)+\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)\right. \\
& \left.-\sum_{i \neq v_{i j}}\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)-\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)+\Delta f_{i}\right) \\
& =\frac{1}{2 m}\left(\sum_{q \neq v_{i j}}\left(A_{q i}-\frac{k_{q} k_{j}}{2 m}\right)-\sum_{i \neq v_{i j}}\left(A_{i i}-\frac{k_{i} k_{j}}{2 m}\right)+\Delta f_{i}\right) \\
& =\frac{1}{2 m}\left(\Delta f_{i}+\Delta f_{i}\right)=\frac{\Delta f_{i}}{m}
\end{aligned}
$$

Thus, the value of the $Q$ function increases monotonically with $f_{i}$.

Note: Property 2 illustrates that the other node labels in the network are invariant. If a change in the node $i$ label increases the value of $f(i)$, the $Q$ function of the entire network will also increase in value.

## III. ESTIMATION OF DISTRIBUTION AlGORITHMS

## A. Individual Coding and Fitness Function Design

The methods used to encode community detection algorithms generally involve string encoding and graphbased encoding ${ }^{[13]}$. Compared with graph-based encoding, the application of string coding to the network community structure is more intuitive and efficient ${ }^{[13]}$. Let $n$ be the number of vertices in $N$ and suppose that $R=\{r(1), r(2), \ldots, r(n)\}$ is a division of the network community (chromosome), where $r(i)$ is the vertex $i$ that corresponds to the community tags (an integer). For vertices $i$ and $j$ in the network, $r(i)=r(j)$ indicates that $i$ and $j$ are in the same community, otherwise $i$ and $j$ are located in different communities.

EDAs select the best individual on the basis of a fitness function, where the network module function can quantitatively evaluate the pros and cons of the network community structure. In the present case, the $Q$ function is

used as the fitness function to evaluate the merits of an individual.

## B. Probability Matrix and Its Update Method

The probability models of EDAs are as follows: independent of the variable type (PBIL, UMDA, and CGA), bivariate correlation type (MIMIC and BMDA), and multivariate correlation type (ECGA, FDA and BOA) [14]. In the present study, we consider a large-scale network; therefore, we use PBIL to represent the solution space. However, traditional PBIL uses binary code; thus, we designed a binary matrix for the community label matrix with $n$ nodes in the network, and we set the maximum value of the network community tag as $K$. The community label matrix of individuals is defined as $F=\left(f_{i j}\right)_{n \in K}$, where $f_{i j} \in\{0,1\}$ and $\sum_{j} f_{i j}=1$. Thus, each node can only be assigned one tag (this can be relaxed, which can solve the problem of overlapping community detection). $f_{i j}=1$ indicates that the community label of node $i$ is $j$, and we define its corresponding probability matrix as $P=\left(p_{i j}\right)_{n \in K}$ for $p_{i j} \in[0,1]$, where $p_{i j}$ indicates the probability of the community tags of node $i$ for $j$, and $\sum_{j} p_{i j}=1$. The update process for the probability matrix proceeds as follows (i.e. the update process for the matrix of individual probabilities).

Suppose that the probability matrix of an individual in generation $t$ is $P(t)=\left(p_{i j}(t)\right)_{n \in K}$. Its corresponding community label matrix is $F(t)=\left(f_{i j}(t)\right)_{n \in K}$. Given that $m$ individuals are selected for updating, the probability $p_{i j}(t+1)$ in generation $(t$ +1 ) that expresses the community tags of node $i$ for $j$ is as follows:

$$
p_{i j}(t+1)=(1-\alpha) p_{i j}(t)+\alpha \frac{\sum_{k} f_{i j}^{k}(t)}{m}
$$

where $f_{i j}^{k}(t)$ represents the community tag of the $k$-th individual node $i$ in generation $t$ 's that needs to be updated for an individual $j$. Thus, $\sum_{k} f_{i j}^{k}(t)$ represents the number of nodes $i$ for which the community tag is $j$ in m individuals, and $\alpha \in(0,1)$ is the speed of learning, where a higher value of $\alpha$ indicates that the algorithm updates and learns more rapidly.

## C. Mutation Operator

An advantage of an EDA is that it describes the search space using a probability model, which is a feasible solution to the global distribution of statistical information ${ }^{[16]}$. However, EDAs lack the capacity for the effective use of the local optimal solution during each generation, while there is also no mechanism for direct control of the local optimal solution ${ }^{[6]}$. Therefore, based on Property 2, we designed a mutation operator to overcome the latter deficiency.

Let $R$ be the variation in a chromosome assuming that node $i$ in $R$ was selected for the mutation operation, and $v(i)$ is a label set of $i$ 's neighbour node. Based on Property 2, it is not necessary to consider all of the nodes in $R$; thus, we select from $v(i)$ to change $i$ 's tag and maximise the function $f(i)$. The detailed algorithm is as follows.

Algorithm 1. Pseudocode of the mutation operator $\boldsymbol{L S M}$ ( $R$ is the individual variation, and $b$ is the gene mutation probability).

## LSM procedure

```
Global \(R, \beta\)
Begin
1 For \(i=1: n\)
2 If \(\operatorname{rand}()<\beta\)
\(v(i) \leftarrow\) The complete neighbour node set of \(i\)
4 label \((i) \leftarrow\) Corresponding label set of a node in \(v(i)\)
5 maxval \(\leftarrow\) Current division that corresponds to \(f_{i}\)
6 For each \(r \in\) label \((i)\)
\(7 \quad f_{i} \leftarrow\) Corresponding value of \(f\) when changing the
label of node \(i\) from \(r(i)\) to \(r\)
\(8 \quad\) If \(f_{i}>\) maxval
\(9 \quad f_{i} \leftarrow\) maxval
\(10 \quad\) label \(\leftarrow r\)
11 End If
12 End For
\(13 \quad r(i) \leftarrow\) label
14 End If
15 End For
```

Clearly, after each mutation operation, the value of $f(i)$ does not decrease; hence, the increase in the value of the $Q$ function can improve the fitness in an effective manner. Indeed, the mutation operator can be viewed as the local search operation of the EDA. Furthermore, if we specify the gene mutation probability $\beta$, a higher value of $\beta$ will increase the variability of the node in R. Thus, $\beta=1$ is the equivalent of a local search for chromosome $R$. This mutation operator can greatly improve the solution space for this algorithm, which ensures the diversity of the population and individuals.

In the present study, $\beta$ takes the reciprocal of the number of different chromosomes in the population, which is small during the initial stage of evolution, but it increases over time to facilitate adaptive adjustment.

## IV. EDA FOR SOLVING THE COMMUNITY DETECTION Problem AND Its PERFORMANCE ANALYSIS

## A. Improved EDA for Solving the Community Detection Problem

Algorithm 2. LSMEDA algorithm.
LSMEDA procedure
Begin
$1 \quad D_{j}^{0} \leftarrow$ Randomly generate M individuals as the initial groups

2 Calculate the fitness values of $M$ individuals
3 If the end condition is not satisfied
$4 \quad D_{j}^{s} \leftarrow$ Select $m=\gamma M(0<\gamma<1)$ individuals as the dominant groups
$5 \quad D_{j}^{r s} \leftarrow$ Randomly select $m^{r}=\lambda M(0<\lambda<1)$ individuals from m for the LSM operation

$6 D_{j}^{* s} \leftarrow D_{j}^{s s}$ and the remaining individuals of $D_{j}^{s}$ form a new dominant group
7 According to the probability matrix update rule, (3) updates the probability matrix $D_{j}^{* s}$ and retains the best individual
9 Based on the probability matrix $M$ times sampling, go to step 3 to obtain a new generation of the population

10 Else
11 over
12 End If
Note: The probability matrix is obtained with a uniform distribution during initialisation, i.e. $p_{i}=1 / K$. Thus, the probabilities of assigning nodes different labels are equal at the beginning of the algorithm.

First, the LSMEDA algorithm generates the initial population before iteratively performing selection, performing local search variation LSM, learning to build the probability model, executing a sampling operation that corresponds to the dominant individual, and producing the next generation of groups. The probability model is established to implement the global search capacity. The LSM corresponds to a local search function with a local optimisation mechanism. The operator is selected using a 'survival of the fittest' mechanism, where the fittest chromosomes are used as the population in the next generation. Thus, the LMEDA algorithm performs global and local search in an effective manner.

## B. Algorithm Performance Analysis Units

Conclusion 1: The LSM operator does not decrease the value of the fitness function of the variant chromosome $\boldsymbol{Q}$.

Proof: According to the algorithm flow, the variant gene $i$ of chromosome $R$ is operated on by the LSM, and the tag aims to maximise $f(i)$, whereas the other node label does not change. According to Property 2, this conclusion is correct.

Conclusion 2: The time complexity of the LSM operator is $O(n c)$.

Proof: If the network has n nodes, the average degree of the nodes in the network is $k$, the average community scale of $R$ is $C$, and complex networks can be represented as a sparse graph. According to the algorithm, line 6 ensures that the algorithm has the highest time complexity (i.e. take all of the neighbour tags of the variation vertex and compute the function values at the same time). During actual operation, the neighbour tag of node $i$ 's tag may be repeated, so the average time required to calculate the value of $f(i)$ must be less than or equal to $K$. According to Property 1, only the community information is required to calculate $f(i)$; thus, the average time required to calculate $f(i)$ is $c$; therefore, the time complexity of the algorithm does not exceed $O(\beta k n c)$ because the number of variant nodes is approximately $\beta n . k$ and $\beta$ are constants, so the complexity of the algorithm should be $O(n c)$.

Conclusion 3: The time complexity of the LSMEDA algorithm is also $O(n c)$.

Proof: If the network has n nodes, the average degree of the nodes in the network is $k$. Let $c$ be the average community scale of the variant chromosome $R$, and it
performs algebra with $L$. The highest time complexity in this algorithm is line 5, while the runtime of the other steps is less than or equal to $O(n)$. Line 5 in the algorithm has $\lambda L M$ times variation at most; thus, the execution time of the mutation operator is $O(c n)$. This means that the time required for line 5 does not exceed $O(\lambda L M c n)$, when $k$ is a constant, the population scale is $M$, the executive algebra is $L$, and the parameter g is also regarded as a constant. Therefore, the algorithm's time complexity is $O(c n)$.

## V. EXPERIMENTAL CONCLUSION AND ANALYSIS

In our quantitative analysis of the LSMEDA algorithm, we used a benchmark network and a real large-scale network for testing and verification. The experimental environment used to implement the algorithm was as follows: an Intel(R) Core(TM) M450 processor running at $2.40 \mathrm{GHz}, 6.00 \mathrm{~GB}$ of memory, a 320-GB hard disk, Microsoft Windows 764 -bit operating system, and the Matlab 7.10 programming environment.

The algorithm parameters were: maximum iterative algebra $L=100$, population size $\operatorname{PopSize}=500$, mutation probability $\beta=0.6$, learning rate $\alpha=0.1$, truncation selection parameter $\gamma=0.5$, and mutation selection parameter $\lambda=0.5$ ( $50 \%$ of the fittest population was selected as the dominant group, and $50 \%$ of the dominant population's mutations were selected).
![img-0.jpeg](img-0.jpeg)

Figure 1. Community detection accuracy comparison

## A. Computer-generated Network

In 2002, Newman et al. proposed a random network model $R N(a, s, d$, zout $)$ to test the performance of a detection algorithm in a network community ${ }^{[15]}$. The community structures are known in the model, $a$ represents the size of the network community, $s$ represents the number of nodes in each community, $d$ represents the average node degree, and zout represents the average number of edges between nodes inside the community and outside the community. A previous study ${ }^{[17]}$ proposed the use of standard normalised mutual information ( $N M I$ ) to evaluate the accuracy of the clustering effects based on information theory and demonstrated that $N M I$ was fair and reasonable. In the present study, we used the $N M I$ method to evaluate the clustering accuracy of different network community detection algorithms by comparing LSMEDA with popular algorithms such as $\mathrm{GN}^{[3]}, \mathrm{FN}^{[18]}$, and Tasgin's GA (TGA) ${ }^{[6]}$. The results are shown in Figure 1. The random network parameter used in the diagram is $R N(4,32,16$, zout). If zout

is larger, the detection algorithm finds it more difficult to determine the fuzzy network's corresponding community structure.

If zout $>8$, i.e. the average number of edges between communities is greater than the average number of edges within the community, we considered that the network did not have a community structure ${ }^{[5]}$. In the figure, the y -axis represents the clustering accuracy, and the value on the xaxis represents the value of zout. Each data point on the curve represents the average accuracy of the algorithm based on 100 runs. The figure shows that the clustering accuracy of the LSMEDA algorithm was much higher than that of GN, FN, and TGA as zout increased (as the network community structure became increasingly fuzzy). Thus, LSMEDA was obviously the best method. In addition, even when zout $=8$ (the average number of edges between communities was equal to the average number of edges within the community), the LSMEDA algorithm could still detect the community structure, whereas the GN, FN, and TGA algorithms were ineffective.

## B. Real complex networks

In this study, four widely used real networks ${ }^{[19-21]}$ were employed as the test dataset to further verify the validity and advantages of LSMEDA. TABLE I provides brief descriptions of the networks.

TABLE I. NETWORK DATA INFORMATION


Using the real complex networks in TABLE I, we compare the performance of the LSMEDA, GN, FN, and TGA algorithms. TABLE II shows the average $Q$ functions after executing the algorithms 100 times.

TABLE II. COMPARISON OF LSMEDA, GN, FN, AND TGA IN A REAL NETWORK


Table II shows that the LSMEDA algorithm performed better than the other algorithms when detecting communities in real complex networks. For the karate network, the real community structure corresponded to a $Q$ value of 0.3715 , but after executing our algorithm 100 times, we obtained an average $Q$ function value of 0.4198 .

## VI. CONCLUSIONS

In this study, we used the $Q$ function as an objective function, employed string encoding, and designed a community partition matrix and a community tags probability matrix. Based on an analysis of the monotonic
properties of the $Q$ function, we designed a local search variant operator and proposed a new EDA and LSMEDA for solving the community detection problem. The experiments showed that the LSMEDA algorithm had a faster convergence speed and a strong search capacity in largescale complex networks, but it could still obtain high quality results in a rapid manner. In our future work, we intend to analyze and improve the probabilistic model used by the LSMEDA algorithm and apply it to the analysis of gene regulation networks or Web community mining research.

## ACKNOWLEDGMENT

Research partially supported by the Natural Science Foundation of Anhui Province (Project No. 1808085MG224), the Natural Science Key Foundation of the Education Department of Anhui Province (Project No. KJ2017A402), the Soft Science Foundation of Anhui Province (Project No. 1706a02020037), and the Natural Science Key Foundation of West Anhui University (Project No. WXZR201619).
