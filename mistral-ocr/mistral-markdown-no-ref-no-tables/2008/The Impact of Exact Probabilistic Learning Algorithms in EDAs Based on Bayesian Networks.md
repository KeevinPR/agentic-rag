# The Impact of Exact Probabilistic Learning Algorithms in EDAs Based on Bayesian Networks 

Carlos Echegoyen ${ }^{1}$, Roberto Santana ${ }^{1}$, Jose A. Lozano ${ }^{1}$, and Pedro Larrañaga ${ }^{2}$<br>${ }^{1}$ Intelligent Systems Group<br>Department of Computer Science and Artificial Intelligence<br>University of the Basque Country<br>Paseo Manuel de Lardizabal 1, 20018 Donostia - San Sebastian, Spain<br>\{carlos.echegoyen,roberto.santana, ja.lozano\}@ehu.es<br>${ }^{2}$ Department of Artificial Intelligence, Technical University of Madrid, 28660 Boadilla del Monte, Madrid, Spain<br>pedro.larranaga@fi.upm.es


#### Abstract

Summary. This paper discusses exact learning of Bayesian networks in estimation of distribution algorithms. The estimation of Bayesian network algorithm (EBNA) is used to analyze the impact of learning the optimal (exact) structure in the search. By applying recently introduced methods that allow learning optimal Bayesian networks, we investigate two important issues in EDAs. First, we analyze the question of whether learning more accurate (exact) models of the dependencies implies a better performance of EDAs. Secondly, we are able to study the way in which the problem structure is translated into the probabilistic model when exact learning is accomplished. The results obtained reveal that the quality of the problem information captured by the probability model can improve when the accuracy of the learning algorithm employed is increased. However, improvements in model accuracy do not always imply a more efficient search.


## 1 Introduction

In estimation of distribution algorithms (EDAs) [21, 30] linkage learning, understood as the ability to capture the relationships between the variables of the optimization problem, is accomplished by detecting and representing probabilistic dependencies using probability models. EDAs are evolutionary algorithms that do not employ classical genetic operators such as mutation or crossover. Instead, machine learning methods are used to extract relevant features of the search space. The collected information is represented using a probabilistic model which is later employed to generate new points. During the sampling or generation step, the statistical dependencies between the variables are used for the construction of the new solutions.

In EDAs, the ability of learning an accurate representation of the relationships between the variables is related to the class of probabilistic models used

[^0]
[^0]:    Y.-p. Chen, M.-H. Lim (Eds.): Linkage in Evolutionary Computation, SCI 157, pp. 109-139, 2008. springerlink.com
    (c) Springer-Verlag Berlin Heidelberg 2008

and the methods employed to learn them. One class of model that has been extensively applied in EDAs is Bayesian networks [18]. Among the benefits of EDAs that use this type of models [14, 28, 33, 45] is that the complexity of the learned structure depends on the characteristics of the data (selected individuals). Additionally, the Bayesian networks learned during the search are suitable for human interpretation, aiding the discovery of unknown information about the problem structure.

Although, in the case of EDAs that use Bayesian networks, the role of the parameters that penalize the complexity of the networks has been studied [28, 32], a detailed analysis of the accuracy of the methods used for finding the best network and its influence in the behavior of EDAs has not been conducted. An initial attempt to investigate this problem was presented in [13], where exact Bayesian learning was introduced to EDAs.

Methods that do exact Bayesian structure learning [12, 20, 42, 43] compute, given a set of data and a prespecified score (in our case, the BIC score [41]), the network structure that optimizes the score. Since the problem of learning the optimal Bayesian network is NP-hard [6], these methods set constraints on the maximum number of variables and/or cases they can deal with. Usually, dynamic programming algorithms are used to learn the structure.

In this chapter, we extend the preliminary results presented in [13] and provide evidence that the methods for learning optimal (exact) Bayesian networks can be very useful to analyze the relationship between the search space and the structure of the learned probabilistic models. The advantage of using methods that learn exact models is because alternative approximate methods commonly applied to learn the models in EDAs are very often able to find only suboptimal solutions. Therefore, using exact learning makes it easier to investigate to what extent approximate learning algorithms are responsible for the loss in accuracy in the mapping between the problem structure and the model structure. In general, an exact learning algorithm can serve as a different framework to investigate the influence of the EDA components in the ability of the probability models to capture the problem structure.

The chapter is organized as follows. In the next section, Bayesian networks are presented, the general procedures to learn these networks from data are also discussed. In Section 3, we focus on the type of search strategies used to find the Bayesian network structure. Approximate and exact learning methods are analyzed. Section 4 introduces the EBNA algorithm. In Section 5, the experimental framework and functions used to evaluate the exact and local learning methods used by EBNA are introduced. Sections 6 and 7 respectively present experimental results on the time complexity analysis and convergence reliability of the two EBNA variants. Section 8 analyzes ways for using the Bayesian networks learned by EBNA as a source of problem knowledge and presents experimental results for several functions. Work related to our proposal is analyzed in Section 9. The conclusions of our paper are presented in Section 10.

# 2 Bayesian Networks 

### 2.1 Notation

Let $X$ be a random variable. A value of $X$ is denoted $x . \mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$ will denote a vector of random variables. We will use $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)$ to denote an assignment to the variables. We will work with discrete variables. The joint probability mass function of $\mathbf{x}$ is represented as $p(\mathbf{X}=\mathbf{x})$ or $p(\mathbf{x}) . p\left(\mathbf{x}_{S}\right)$ will denote the marginal probability distribution for $\mathbf{X}_{S}$. We use $p\left(X_{i}=x_{i} \mid X_{j}=\right.$ $x_{j}$ ) or, in a simplified form, $p\left(x_{i} \mid x_{j}\right)$, to denote the conditional probability distribution of $X_{i}$ given $X_{j}=x_{j}$.

Formally, a Bayesian network [5] is a pair $(S, \boldsymbol{\theta})$ representing a graphical factorization of a probability distribution. The structure $S$ is a directed acyclic graph which reflects the set of conditional (in)dependencies among the variables. The factorization of the probability distribution is codified by $S$ :

$$
p(\mathbf{x})=\prod_{i=1}^{n} p\left(x_{i} \mid \mathbf{p a}_{i}\right)
$$

where $\mathbf{p a}_{i}$ denotes a value of variable $\mathbf{P a}_{i}$, the parent set of $X_{i}$ (variables from which there exists an arc to $X_{i}$ in the graph $S$ ), while $\boldsymbol{\theta}$ is a set of parameters for the local probability distributions associated with each variable. If the variable $X_{i}$ has $r_{i}$ possible values, $x_{i}^{1}, \ldots, x_{i}^{r_{i}}$, the local distribution $p\left(x_{i} \mid \mathbf{p a}_{i}^{j}, \boldsymbol{\theta}_{i}\right)$ is an unrestricted discrete distribution:

$$
p\left(x_{i}^{k} \mid \mathbf{p a}_{i}^{j}, \boldsymbol{\theta}_{i}\right) \equiv \theta_{i j k}
$$

where $\mathbf{p a}_{i}^{1}, \ldots, \mathbf{p a}_{i}^{q_{i}}$ denote the values of $\mathbf{P a}_{i}$ and the term $q_{i}$ denotes the number of possible different instances of the parent variables of $X_{i}$. In other words, the parameter $\theta_{i j k}$ represents the probability of variable $X_{i}$ being in its $k$-th value, knowing that the set of its parent variables is in its $j$-th value. Therefore, the local parameters are given by $\boldsymbol{\theta}_{i}=\left(\left(\left(\theta_{i j k}\right)_{k=1}^{r_{i}}\right)_{j=1}^{q_{i}}\right)$.

### 2.2 Learning Bayesian Networks from Data

There are different strategies to learn the structure of a Bayesian network. We focus on a method called "score + search" which is the one used in the experiments presented in this paper. In this strategy, given a set of data $D$ and a Bayesian network whose structure is denoted by $S$, a value (score) which evaluates how well the Bayesian network represents the probability distribution of the database $D$ is assigned. Different scores can be used. In this work we have used the Bayesian Information Criterion score (BIC) [41] (based on penalized maximum likelihood).

A general formula for a penalized maximum likelihood score can be written as follows:

$$
\log p(D \mid S, \hat{\boldsymbol{\theta}})-f(N) \operatorname{dim}(S)
$$

where $\operatorname{dim}(S)$ is the dimension-number of parameters needed to specify the model- of the Bayesian network with a structure given by $S$. Thus:

$$
\operatorname{dim}(S)=\sum_{i=1}^{n} q_{i}\left(r_{i}-1\right)
$$

and $f(N)$ is a non negative penalization function. The Jeffreys-Schwarz criterion, sometimes called BIC [41], takes into account $f(N)=\frac{1}{2} \log N$. Thus the $B I C$ score can be written as follows:

$$
B I C(S, D)=\log \prod_{w=1}^{N} \prod_{i=1}^{n} p\left(x_{w, i} \mid \mathbf{p a}_{i}^{S}, \hat{\boldsymbol{\theta}}_{i}\right)-\frac{1}{2} \log N \sum_{i=1}^{n} q_{i}\left(r_{i}-1\right)
$$

To find the Bayesian network that optimizes the score implies solving an optimization problem. This can be done with exhaustive or heuristic search algorithms. In Section 3, we analyze two variants for finding the Bayesian network structures. Each structure is evaluated using the maximum likelihood parameters.

# 2.3 Learning of the Parameters 

Once the structure has been learned, the parameters of the Bayesian network are calculated using the Laplace correction:

$$
\hat{\theta}_{i j k}=\frac{N_{i j k}+1}{N_{i j}+r_{i}}
$$

where $N_{i j k}$ denotes the number of cases in $D$ in which the variable $X_{i}$ has the value $x_{i}^{k}$ and $\boldsymbol{P} \boldsymbol{a}_{i}$ has its $j^{\text {th }}$ value, and $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$.

## 3 Methods for Learning Bayesian Networks

Once we have defined a score to evaluate Bayesian networks, we have to set a search process to find the Bayesian network that maximizes the score given the data. Approximate and exact methods can be used.

### 3.1 Learning an Approximate Model

In practical applications, we need to find an adequate model structure as quickly as possible. Therefore, a simple algorithm which returns a good structure, even if not optimal, is preferred. An algorithm that fulfills these criteria is Algorithm B [4] which is typically used by most of Bayesian network based EDAs. Algorithm B is a greedy search which starts with an arcless structure and, at each step, adds the arc with the maximum improvement in the score. The algorithm finishes when there is no arc whose addition improves the score.

# 3.2 Learning the Exact Model 

Since learning the Bayesian network structure is an NP-hard problem, for a long time the goal of learning exact Bayesian networks was constrained to problems with a very reduced number of variables. In [20], an algorithm for learning the exact structure in less than super-exponential complexity with respect to $n$ is introduced for the first time.

In [42], the most efficient method so far is presented and it is used in our work. This algorithm is feasible for $n<33$ and it was shown to learn a best network for a data set of 29 variables.

In that work, the Bayesian network structure $S$ is defined as a vector $\mathbf{S}=$ $\left(S_{1}, . ., S_{n}\right)$ of parent sets, where $S_{i}$ is the subset of $\mathbf{X}$ from which there are arcs to $X_{i}$, for example $S_{1}$ is the parent set of $X_{1}$. Another necessary concept is the variable ordering. This is simply the variables of $\mathbf{X}$ in a determined order. In this order, the $i^{t h}$ element is denoted by $o r d_{i}$. Therefore, the structure $\mathbf{S}=\left(S_{1}, . ., S_{n}\right)$ is said to be consistent with an ordering ord when all the parents of the node precede the node in the ordering.

Another important concept in the algorithm is the sink node. Every DAG has at least one node with no outgoing arcs, so at least one node is not a parent of any other node. These nodes are called sinks of the network.

In this algorithm, the data set D is processed in a particular way and it uses two kinds of data tables. Given $\mathbf{W} \subseteq \mathbf{X}$, first it is defined the contingency table $C T(\mathbf{W})$ to be a list of the frequencies of different data-vectors $d^{\mathbf{W}}$ in $D^{\mathbf{W}}$, where $D^{\mathbf{W}}$ is the data set for $\mathbf{W}$ variables. However, the main task is to calculate conditional frequency tables $C F T\left(X_{i}, \mathbf{W}\right)$ that record how many times different values of the variable $X_{i}$ occur together with different vectors $d^{\mathbf{W}-\left\{X_{i}\right\}}$ in the data.

On the other hand, many popular scores such as BIC, AIC and BDe can be decomposed to local scores:

$$
\operatorname{score}(S)=\sum_{i=1}^{n} \operatorname{score}_{i}\left(S_{i}\right)=\sum_{i=1}^{n} \operatorname{score}\left(C F T\left(X_{i}, S_{i}\right)\right)
$$

Thus, the score of the network is the sum of the local scores that only depend on the conditional frequency table for one variable and its parents. Algorithm 1 presents the main steps of the method:

The first step is the main procedure and the only one for which data is needed. It starts by calculating the contingency table for all the variables $\mathbf{X}$ and continues calculating contingency tables for all smaller variable subsets, marginalizing variables out of the contingency table. After that, for each contingency table, the conditional frequency table is calculated for each variable appearing in the contingency table. These conditional frequency tables can then be used to calculate the local scores for any parent set given a variable. All the $n 2^{n-1}$ local scores are stored in a table which will be the basis of the algorithm.

Having calculated the local scores, the best parents for $X_{i}$ given a candidate set $C$ are either the whole candidate set $C$ itself or one of the smaller candidate

```
Algorithm 1. Exact learning algorithm
1 Calculate the local scores for all \(n 2^{n-1}\) different (variable, variable
    set)-pairs
2 Using the local scores, find best parents for all \(n 2^{n-1}\) (variable,
    variable set)-pairs
3 Find the best sink for all \(2^{n}\) variable sets
4 Using the results from Step 3, find a best ordering of the variables
5 Find a best network using results computed in Steps 2 and 4
```

sets $\{C \backslash\{c\} \mid c \in C\}$. It must be computed for all $2^{n-1}$ variable sets (parent candidate sets) related with $X_{i}$.

Step 3 of the algorithm is based on the following observation: The best network $G^{*}$ for a variable set $W$ must have a sink $s$. As $G^{*}$ is a network with the highest score, sink $s$ must have incoming arcs from its best possible set of parents. In this way, the rest of the nodes and the arcs must form the best possible network for variables $W \backslash\{s\}$. Therefore, the best sink for $\mathbf{W}, \operatorname{sink}^{*}(\mathbf{W})$, is the node that maximizes the sum between the local score for $s$ and the score for the network $S$ without node $s$.

When we have the best sinks for all $2^{n}$ variable sets, it is possible to yield the best ordering ord* in reverse order. Then, for each position from $|\mathbf{X}|$ to 1 , in ord $_{i}^{*}$ we have to store the best sink for the set $\bigcup_{j=i+1}^{|\mathbf{X}|}\left\{\operatorname{ord}_{j}^{*}(\mathbf{X})\right\}$.

Having a best ordering and a table with the best parents for any candidate set, it is possible to obtain a best network consistent with the given ordering. For the $i^{\text {th }}$ variable in the optimal ordering, the best parents from its predecessors are picked.

More details about the algorithm can be found in [42]. We use an implementation of Algorithm 1 given by the authors ${ }^{1}$. The computational complexity of the algorithm is $o\left(n^{2} 2^{n-2}\right)$. The memory requirement of the method is $2^{n+2}$ bytes and the disk-space requirement is $12 n 2^{n-1}$ bytes.

# 4 Estimation of Distribution Algorithms Based on Bayesian Networks 

The estimation of Bayesian networks algorithm (EBNA) allows statistics of unrestricted order in the factorization of the joint probability distribution. This distribution is encoded by a Bayesian network that is learned from the database containing the selected individuals at each generation. It has been applied with good results to a variety of problems [3, 19, 23, 24, 25]. Other algorithms based

[^0]
[^0]:    ${ }^{1}$ The C++ code of this implementation is available from http://www.cs.helsinki.fi/u/tsilande/sw/bene/download/

```
\(\operatorname{ABNA}_{B I C}\)
\(B N_{0} \leftarrow\left(S_{0}, \boldsymbol{\theta}^{0}\right)\) where \(S_{0}\) is an arc-less DAG, and \(\boldsymbol{\theta}^{0}\) is uniform
\(p_{0}(\mathbf{x})=\prod_{i=1}^{n} p\left(x_{i}\right)=\prod_{i=1}^{n} \frac{1}{r_{i}}\)
\(D_{0} \leftarrow\) Sample \(M\) individuals from \(p_{0}(\mathbf{x})\) and evaluate them
t \(\leftarrow 1\)
do \(\{\)
    \(D_{t-1}^{S e} \leftarrow\) Select \(N\) individuals from \(D_{t-1}\)
    \(S_{t}^{*} \leftarrow\) Using a search method find one network structure accord-
        ing to the BIC score
        \(\boldsymbol{\theta}^{t} \leftarrow\) Calculate \(\theta_{i j k}^{t}\) using \(D_{t-1}^{S e}\) as the data set
        \(B N_{t} \leftarrow\left(S_{t}^{*}, \boldsymbol{\theta}^{t}\right)\)
        \(D_{t} \leftarrow\) Sample \(M\) individuals from \(B N_{t}\) and evaluate them
    \} until Stopping criterion is met
```

on the use of Bayesian networks have been proposed in [28, 33, 45]. A pseudocode of EBNA is shown in Algorithm 2.

In the experiments presented in this paper, EBNA uses truncation selection and the number of selected individuals equals half of the population. The best solution at each generation is passed to the next population, therefore, at each generation $N-1$ new solutions are sampled. The stopping criterion is changed according to the type of experiments conducted.

# 5 Experimental Framework and Function Benchmark 

To investigate the impact of exact learning in the behavior of Bayesian network based EDAs, we compare the EBNA versions that use the two different Bayesian network learning schemes described in Section 3. We call them EBNA-Exact and EBNA-Local.

We used three different criteria to compare the algorithms. The time complexity, the convergence reliability and the way in which probabilistic dependencies are represented in the structure of the Bayesian network. In this section, we introduce a set of functions that represent different classes of problems and which are used in the following sections to test the behavior of EDAs.

### 5.1 Function Benchmark

Let $u(\mathbf{x})=\sum_{i=1}^{n} x_{i}, f(\mathbf{x})$ be a unitation function if $\forall \mathbf{x}, \mathbf{y} \in\{0,1\}^{n}, u(\mathbf{x})=$ $u(\mathbf{y}) \Rightarrow f(\mathbf{x})=f(\mathbf{y})$. A unitation function is defined in terms of its unitation value $u(\mathbf{x})$, or in a simpler way $u$.

Function OneMax:

$$
\operatorname{OneMax}(\mathbf{x})=\sum_{i=1}^{n} x_{i}=u(\mathbf{x})
$$

Unitation functions are also useful for the definition of a class of functions where the difficulty is given by the interactions that arise among subsets of variables. One example of this class of deceptive functions is $f_{3 \text { deceptive }}$ [15]:

$$
f_{3 \text { deceptive }}(\mathbf{x})=\sum_{i=1}^{i=\frac{n}{2}} f_{d e c}^{3}\left(x_{3 i-2}, x_{3 i-1}, x_{3 i}\right)
$$

where $f_{d e c}^{3}$ is defined as:

$$
f_{d e c}^{3}(u)= \begin{cases}0.9 \text { for } u=0 \\ 0.8 \text { for } u=1 \\ 0.0 \text { for } u=2 \\ 1.0 \text { for } u=3\end{cases}
$$

Function SixPeaks is a modification of the FourPeaks problem [1] and it can be defined mathematically as:

$$
\operatorname{SixPeaks}(\mathbf{x}, t)=\max \{\operatorname{tail}(0, \mathbf{x}), \operatorname{head}(1, \mathbf{x}), \operatorname{tail}(1, \mathbf{x}), \operatorname{head}(0, \mathbf{x})\}+\mathcal{R}(\mathbf{x}, t)
$$

where

$$
\begin{aligned}
& \operatorname{tail}(b, \boldsymbol{x})=\text { number of trailing } b \text { 's in } \boldsymbol{x} \\
& \operatorname{head}(b, \boldsymbol{x})=\text { number of leading } b \text { 's in } \boldsymbol{x}
\end{aligned}
$$

$$
\mathcal{R}(\boldsymbol{x}, t)= \begin{cases}n & \text { if } \operatorname{tail}(0, \boldsymbol{x})>t \text { and } \operatorname{head}(1, \boldsymbol{x})>t \text { or } \\ 0 & \text { tail }(1, \boldsymbol{x})>t \text { and } \operatorname{head}(0, \boldsymbol{x})>t \\ 0 & \text { otherwise }\end{cases}
$$

The goal is to maximize the function. For an even number of variables this function has 4 global optima, located at the points:

$$
(0, \ldots, 0,1, \ldots, 1)(0, \ldots, 0, \overbrace{1, \ldots, 1}^{t}) \overbrace{(1, \ldots, 1}^{t}, 0, \ldots, 0)(1, \ldots, 1, \overbrace{0, \ldots, 0}^{t})
$$

These points are very difficult to reach because they are isolated. On the other hand, two local optima $(0,0, \ldots, 0),(1,1, \ldots, 1)$ are very easily reachable. The value of $t$ was set to $\frac{n}{2}-1$.

The Parity function [8] is a simple $k$-bounded additively separable function that has been used to investigate the limitations of linkage learning by probabilistic modeling. It can be seen as a generalization of the XOR function and the Walsh transform. In this case we will work with the concatenated parity function

(CPF) [8]. It is said that this problem is hard for EDAs in general. The Parity function can be defined mathematically as:

$$
\operatorname{parity}(\mathbf{x})= \begin{cases}C_{\text {even }} & \text { if } u(\mathbf{x}) \text { is even } \\ C_{\text {odd }} & \text { otherwise }\end{cases}
$$

where $C_{\text {even }}$ and $C_{\text {odd }}$ are parameters of the function. The CPF is defined as $m$ concatenated parity sub-functions,

$$
C P F(\mathbf{x})=\sum_{i=0}^{m-1} \operatorname{parity}\left(x_{i k+1}, \ldots, x_{i k+k}\right)
$$

Where $k$ is the size for each sub-function. As in [8], we use $k=5, C_{\text {odd }}=5$ and $C_{\text {even }}=0$. Notice that there are $2^{n-m}$ solutions where the function reaches the global optima.

Function Cuban5 [29] is a non-separable additive function. The second best value of this function is very close to the global optimum.

$$
\begin{aligned}
& \text { Cuban } 5(\mathbf{x})= \\
& F_{\text {cuban1 }}^{5}\left(s_{0}\right)+\sum_{j=0}^{m}\left(F_{\text {cuban } 2}^{5}\left(s_{2 j+1}\right)+F_{\text {cuban1 }}^{5}\left(s_{2 j+2}\right)\right)
\end{aligned}
$$

where

$$
s_{i}=x_{4 i} x_{4 i+1} x_{4 i+2} x_{4 i+3} x_{4 i+4} \text { and } n=4(2 m+1)+1
$$

$$
F_{\text {cuban1 }}^{3}(\mathbf{x})=\left\{\begin{array}{l}
0.595 \text { for } \mathbf{x}=000 \\
0.200 \text { for } \mathbf{x}=001 \\
0.595 \text { for } \mathbf{x}=010 \\
0.100 \text { for } \mathbf{x}=011 \\
1.000 \text { for } \mathbf{x}=100 \\
0.050 \text { for } \mathbf{x}=101 \\
0.090 \text { for } \mathbf{x}=110 \\
0.150 \text { for } \mathbf{x}=111
\end{array}\right.
$$

$$
\begin{aligned}
& F_{\text {cuban1 }}^{5}(\mathbf{x})= \\
& \begin{cases}4 F_{\text {cuban1 }}^{3}\left(x_{1}, x_{2}, x_{3}\right) & \text { if } x_{2}=x_{4} \text { and } x_{3}=x_{5} \\
0 & \text { otherwise }\end{cases} \\
& F_{\text {cuban } 2}^{5}(\mathbf{x})=\left\{\begin{array}{ccc}
u(\mathbf{x}) & \text { for } & x_{5}=0 \\
0 & \text { for } x_{1}=0, x_{5}=1 \\
u(\mathbf{x})-2 & \text { for } x_{1}=1, x_{5}=1
\end{array}\right.
\end{aligned}
$$

# The HP protein model 

In our experiments we also use a class of coarse-grained protein folding model called the hydrophobic-polar (HP) model [11].

![img-0.jpeg](img-0.jpeg)

Fig. 1. An optimal solution of the HP model for sequence $H P H P P H H P H P P H P H H P P H P H$. The optimal energy corresponding to this sequence is -9 .

Under specific conditions, a protein sequence folds into a native 3-d structure. The problem of determining the protein native structure from its sequence is known as the protein structure prediction problem. To solve this problem, a protein model is chosen and an energy is associated to each possible protein fold. The search for the protein structure is transformed into the search for the optimal protein configuration given the energy function.

The HP model considers two types of residues: hydrophobic (H) residues and hydrophilic or polar (P) residues. In the model, a protein is considered as a sequence of these two types of residues, which are located in regular lattice models forming self-avoided paths. Given a pair of residues, they are considered neighbors if they are adjacent either in the chain (connected neighbors) or in the lattice but not connected in the chain (topological neighbors). The total number of topological neighboring positions in the lattice $(z)$ is called the lattice coordination number. Figure 1 shows one possible configuration of sequence $H P H P P H H P H P P H P H H P P H P H$ in the HP model.

A solution $\mathbf{x}$ can be interpreted as a walk in the lattice, representing one possible folding of the protein. We use a discrete representation of the solutions. For a given sequence and lattice, $X_{i}$ will represent the relative move of residue $i$ in relation to the previous two residues. Taking as a reference the location of the previous two residues in the lattice, $X_{i}$ takes values in $\{0,1, \ldots, z-2\}$, where $z-1$ is the number of movements allowed in the given lattice. These values respectively mean that the new residue will be located in one of the $z-1$ numbers of possible directions with respect to the previous two locations. If the encoded solution is self-intersecting, it can be repaired or penalized during the evaluation step using a recursive repairing procedure introduced in [9]. Therefore, values for $X_{1}$ and $X_{2}$ are meaningless. The locations of these two residues are fixed.

For the HP model, an energy function that measures the interaction between topological neighbor residues is defined as $\epsilon_{H H}=-1$ and $\epsilon_{H P}=\epsilon_{P P}=0$. The HP problem consists of finding the solution that minimizes the total energy. More details about the representation and function can be found in [40].

# 6 Time Complexity Analysis 

In our case, the time complexity analysis will refer to the study of the average number of generations needed by EBNA-Local and EBNA-Exact to find the optimum.

Experiments were conducted for three functions, OneMax, $f_{\text {3deceptive }}$ and SixPeaks. In the first function, there are no interactions between the variables. In the rest, interactions arise between variables that belong to the same definition set of the function.

To determine the average number of generations to find the optimum needed by EBNA-Local and EBNA-Exact, we start with a population of 10 individuals and the population size is increased by 10 until a maximum population size of 150 is reached. For each possible combination of function, number of variables $n$, and population size $N, 50$ experiments are conducted. For each execution of the algorithm, a maximum of $10^{5}$ evaluations are allowed.

For the OneMax function we conducted experiments for $n \in\{15,20\}$. In order to increase the accuracy of the curves shown in the first figure, for $n=15$ we exceptionally conducted 100 experiments. The original idea was to evaluate, under the dimension constraints imposed by the exact learning algorithm, the scalability of both EBNA versions with $n \in\{10,12,15,20\}$. Nevertheless, in this work we only present the results achieved for the last two sizes. The results of the experiments for $n=15$ are shown in Figures 2 (a) and the average results for $n=20$ are shown in Figure 2 (b).

The analysis of Figure 2 reveals that both algorithms exhibit the same time complexity pattern. However, EBNA-Exact needs, in general, a higher number of evaluations than EBNA-Local to find the optimal solution for the first time. The difference in the number of generations is less evident when the population size approaches 150 . For this simple function, it seems that the error in the learning of the model, introduced by the approximate learning algorithm, is beneficial for the search.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Time complexity analysis for function OneMax,(a) $n=15$ and (b) $n=20$

![img-2.jpeg](img-2.jpeg)

Fig. 3. Time complexity analysis for function $f_{3 \text { deceptive }}$, (a) $n=15$ and (b) $n=18$
![img-3.jpeg](img-3.jpeg)

Fig. 4. Time complexity analysis for function SixPeaks, (a) $n=14$ and (b) $n=16$

In Figure 3 we can observe that both algorithms have an identical curve. For this function, and for the values of $n$ investigated, the influence of the exact learning is not relevant. We can anticipate that the structures learned by both algorithms are similar. For this function, a small population size determines many generations are necessary to reach the optimum.

For the SixPeaks function, the optimal value is reached in a significantly lower number of generations as can be appreciated in Figure 4. It can also be observed that EBNA-Local is able to reach the optimum earlier than EBNAExact. From this analysis we deduce that for SixPeaks function, the structures learned by both algorithms could be different. We will later further analyze this behavior of the algorithms when discussing the structures of the models they learn for the $f_{3 \text { deceptive }}$ and SixPeaks functions.

To illustrate the complexity of the function and to study in more detail the algorithms, we introduce Figures 5 and 6 which show the total number of executions needed by each algorithm in order to succeed, i.e. to find the optimum. It should be noticed that in every run, the maximum number of evaluations is bounded by $10^{5}$. This constraint strongly influences the behavior of the algorithms.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Number of executions, for each population size, in order to obtain one optimal value for $f_{3 \text { deceptive }}$ function, (a) $n=15$, (b) $n=18$
![img-5.jpeg](img-5.jpeg)

Fig. 6. Number of executions, for each population size, in order to obtain one optimal value for SixPeaks function, (a) $n=14$, (b) $n=16$

# 7 Convergence Reliability 

In the analysis of the convergence reliability, we focus on the critical population size needed by the EDAs to achieve a predefined convergence rate. In the experiments conducted, the goal was to determine the minimum population size needed by the two different variants of EBNA to find the optimum in 20 consecutive experiments. We investigated the behavior of the algorithms for functions Cuban5 $(n=13)$, SixPeaks $(n \in\{10,12,14\})$ and $f_{3 \text { deceptive }}(n \in\{9,12,15\})$.
The algorithm begins with a population size $N=16$ which is doubled until the optimal solution has been found in 20 consecutive experiments. The maximum number of evaluations allowed is $10^{4}$. For each function and value of $n, 25$ experiments are carried out. Table 1 shows the mean and standard deviation of the critical population size found.

Table 1 shows that for function Cuban5, EBNA-Exact requires a slightly higher population size than EBNA-Local. The picture is drastically changed for functions SixPeaks and $f_{3 \text { deceptive }}$, for which EBNA-Exact needs a much smaller

Table 1. Mean, standard deviation and p-value of the critical population size for different functions and number of variables

population size. This difference is particularly evident for function SixPeaks. Another observation is that the standard deviation of EBNA-Local is always higher than that of EBNA-Exact. Since the only difference between EBNAExact and EBNA-Local is in the class of algorithm used to learn the models, the difference of behaviors is due to the ability of EBNA-Exact to learn a more accurate model of the dependencies. Therefore, at least for functions SixPeaks and $f_{3 d e c e p t i v e}$, learning a more accurate model determines a better performance of EBNA.

To determine if the population sizes obtained for each algorithm are significantly different, we have carried out a Student's t-test over the two sets of 25 population sizes for each function and value of $n$. In the last column of Table 1, the probability values of the test are reported.

If we consider a significance level of 0.05 , we would have to reject the null hypotesis for all cases except for Cuban 5 where there are not significant differences. An explanation of the similar behavior achieved with both algorithms for Cuban 5 will be presented in the next section, where the structures of the probabilistic models learned by the algorithms are studied. Moreover, for SixPeaks, using the highest value of $n$, and for $f_{3 d e c e p t i v e}$, using the two highest problem sizes, the difference between the algorithms is statistically significant at the $1 \%$ level.

# 8 Problem-Knowledge Extraction from Bayesian Networks 

The objective of this section is to show a number of ways in which knowledge about the problem structure can be extracted from the analysis of the Bayesian networks learned by EBNA. In particular, we investigate the difference between the structures learned using exact and approximate learning algorithms. We also analyze the changes in the pattern (number and type) of the dependencies captured by the algorithms during their evolution.

# 8.1 Probabilistic Models as a Source of Knowledge About the Problem 

Although the main objective in EDAs is to obtain a set of optimal solutions, the analysis of the models learned by the algorithms during the evolution can reveal previously unknown characteristics of the problem. There is a variety of information that can be obtained from the analysis of the models. Just to cite a few examples, it could be possible to extract:

- A description of sets of dependent or interacting variables.
- Probabilistic information about most likely configurations for subsets of the problem variables which can be translated into most-probable partial solutions of the problem.
- Evidence on the existence of different types of problem symmetry.
- Identification of conflicting partial solutions in problems with frustration.
- In addition, by considering the change of the models during the evolution (a dynamical perspective), it is also possible to identify patterns in the formation of optimal structures.

A central problem in EDAs is the design of methods for extracting and interpreting this information from the models. There are a number of approaches that have been proposed to treat this issue for different classes of probabilistic models used in EDAs. We postpone a review of some of these approaches for the next section and focus now on the extraction of information from Bayesian networks. We identify three main sources of information:

1. The structure of the Bayesian network: By inspecting the topological characteristics of the graphs (e.g. most frequent arcs), we identify structural relationships between the variables.
2. The probabilistic tables of the Bayesian networks: By analyzing the probability associated to variables linked in the network, it is possible to identify promising and also poor configurations of the partial solutions.
3. Most probable configurations given the network: These are the solutions with the highest probability given the model. Thus, they condense the structural and parametrical information stored by the Bayesian network and have not necessarily been generated during the evolution of the EDA.

In this paper we focus on the analysis of network structures.

### 8.2 Analysis of the Bayesian Structures Learned by EBNA

To investigate the type of dependencies learned by EBNA-Exact and EBNALocal, we saved the structures of the Bayesian networks learned during the evolutionary process by both variants of the algorithm for functions $f_{3 \text { deceptive }}$, SixPeaks, Cuban5, CPF and Protein.

In all the following experiments, we start by running EBNA-Local and EBNAExact and choose 30 executions in which the optimum was found and the algorithms did not converge in the first generation. The stopping criterion is a

maximum number of $10^{5}$ evaluations. In each of these experiments, the structures of the Bayesian networks learned in each generation are stored. From the structures, the frequency in which each arc appeared in the Bayesian network was calculated. Since we are not interested in the direction of the dependencies, we add the frequency of the two arcs that involves the same pair of variables. The matrices that store this information are called frequency matrices.

Two different ways of showing the information contained in the frequency matrices are used. The first way to represent the frequencies is using images where lighter color indicate a higher frequency. As another means to visualize the patterns of interactions, we use contour maps in which dependencies with a similar frequency are joined with lines. In this way, it is possible to identify areas of similar strength of dependency. In addition, the number of contours is a parameter that can be tuned to focus the attention on the set of the strongest dependencies.

In the following, for each function and variant of EBNA employed, two figures are shown. The first figure shows the image graph of the dependencies learned by the model in the last generation and contained in the corresponding frequency matrix. The second figure shows the contour graph corresponding to a matrix that stores all the arcs learned by all the models during the evolution. We call this second matrix the cumulative frequency matrix. In order to fairly compare both algorithms using the contour figures, we normalized the frequencies of the arcs by the highest value among the two cumulative matrices learned by each algorithm. The normalized values are later discretized in ten levels. This way the contour lines refer to the same levels of frequencies.

# Results for $f_{\text {3deceptive }}$ and SixPeaks functions 

In the initial experiments we use functions $f_{\text {3deceptive }}(n=15)$ and SixPeaks $(n=16)$. We relate the behavior exhibited by these functions and analyze some patterns identified in the structures of the models learned. We also try to link the behavior in both studies.

We start by using a population size of 150 , which was the highest population size used on the complexity experiments shown in previous sections. Figure 7 and 8 respectively show the frequency matrices corresponding to EBNA-Local and EBNA-Exact for function $f_{\text {3deceptive }}$. Both algorithms are able to capture the dependencies corresponding to the problem interactions. This fact may explain the similar behavior exhibited in the time complexity experiments.

It can be noticed that the models include a number of additional spurious correlations which are not determined by the function structure. This is particularly evident for the EBNA-Exact algorithm and is explained by the fact that exact learning is more sensitive to the overfitting of the data when the population size is small. Therefore, we increase the population size to $N=500$ and repeat the same experiment for this function. The frequency matrices obtained are shown in Figures 9 and 10. They reveal the effect of increasing the population size in the dependencies learned. It can be appreciated that spurious correlations

![img-6.jpeg](img-6.jpeg)

Fig. 7. Frequency matrices calculated from the models learned by EBNA-Local for function $f_{3 \text { deceptive }}$ with $N=150$ (a) Last generation (b) All generations
![img-7.jpeg](img-7.jpeg)

Fig. 8. Frequency matrices calculated from the models learned by EBNA-Exact for function $f_{3 \text { deceptive }}$ with $N=150$ (a) Last generation (b) All generations
have almost disappeared from the models. Both algorithms are able to learn an accurate model with a population size of $N=500$.

We conduct a similar analysis for function SixPeaks. Figures 11 and 12 respectively show the frequency matrices calculated for EBNA-Local and EBNAExact with a population size $N=150$. It can be seen that both algorithms are unable to learn the accurate structure. As in the case of the $f_{3 \text { deceptive }}$ function, EBNA-Exact learns more spurious dependencies than EBNA-Local. This fact is specially evident in Figure 12. In this case the patterns of dependencies is spread along the matrix while dependencies learned by EBNA-Local are grouped around the diagonal. This fact may explain the better results achieved by EBNA-Local in the time complexity experiments done for this function.

Insufficient population size might be the main reason that explains the poor quality in the mapping between the function structure and the model structure.

The experiments presented in [13] showed that EBNA-Exact was able to learn an accurate model for function SixPeaks with a smaller number of variables.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Frequency matrices calculated from the models learned by EBNA-Local for function $f_{\text {3deceptive }}$ with $N=500$ (a) Last generation (b) All generations
![img-9.jpeg](img-9.jpeg)

Fig. 10. Frequency matrices calculated from the models learned by EBNA-Exact for function $f_{\text {3deceptive }}$ with $N=500$ (a) Last generation (b) All generations
![img-10.jpeg](img-10.jpeg)

Fig. 11. Frequency matrices calculated from the models learned by EBNA-Local for function SixPeaks with $N=150$ (a) Last generation (b) All generations

![img-11.jpeg](img-11.jpeg)

Fig. 12. Frequency matrices calculated from the models learned by EBNA-Exact for function SixPeaks with $N=150$ (a) Last generation (b) All generations
![img-12.jpeg](img-12.jpeg)

Fig. 13. Frequency matrices calculated from the models learned by EBNA-Local for function SixPeaks with $N=500$ (a) Last generation (b) All generations
![img-13.jpeg](img-13.jpeg)

Fig. 14. Frequency matrices calculated from the models learned by EBNA-Exact for function SixPeaks with $N=500$ (a) Last generation (b) All generations

Therefore, we repeat the experiment using a population size $N=500$. Results are shown in Figures 13 and 14.

The image graph reveals that by increasing the population size EBNA-Exact is able to learn a very accurate structure. The model learned captures all the short-order dependencies of the function. This fact is corroborated by inspecting the contour graph in Figure 14 (b) where there is evidence that exact learning has gains in accuracy with respect to a smaller population size. On the other hand, EBNA-Local does not achieve a similar improvement. Furthermore, the accuracy of the approximation is lower than when a population size $N=150$ was used, as can be seen comparing Figures 11 and 13.

# Cuban5 function 

We analyze the Cuban5 function $(m=1, n=13)$. For $m=1$, Cuban5 is equal to the sum of three subfunctions:

$$
\operatorname{Cuban} 5(\mathbf{x})=F_{\text {cuban1 }}^{5}\left(s_{0}\right)+F_{\text {cuban2 }}^{5}\left(s_{1}\right)+F_{\text {cuban1 }}^{5}\left(s_{2}\right)
$$

The interactions are determined by two different functions, $F_{\text {cuban1 }}^{5}$ and $F_{\text {cuban2 }}^{5}$. Therefore, we expect Cuban5 to exhibit a different pattern of interactions than those previously analyzed. As in previous experiments, we start with a population size $N=150$. The frequency matrices corresponding to EBNA-Local and EBNA-Exact are respectively shown in Figures 15 and 16.

It can be seen in the images calculated from the frequency matrices of the last generation that only some of the dependencies determined by function $F_{\text {cuban1 }}^{5}$ are captured by both algorithms. However, the cumulative frequencies clearly show the existence of dependencies related to function $F_{\text {cuban2 }}^{5}$. There are no important differences between the two EDAs.

The frequency matrices obtained by increasing the population size to $N=500$ are shown in Figures 17 and 18. In this case, the dependencies determined by function $F_{\text {cuban2 }}^{5}$ are easier to recognize in the frequency matrices of the last
![img-14.jpeg](img-14.jpeg)

Fig. 15. Frequency matrices calculated from the models learned by EBNA-Local for function Cuban5 with $N=150$ (a) Last generation (b) All generations

![img-15.jpeg](img-15.jpeg)

Fig. 16. Frequency matrices calculated from the models learned by EBNA-Exact for function Cuban5 with $N=150$ (a) Last generation (b) All generations
![img-16.jpeg](img-16.jpeg)

Fig. 17. Frequency matrices calculated from the models learned by EBNA-Local for function Cuban5 with $N=500$ (a) Last generation (b) All generations
![img-17.jpeg](img-17.jpeg)

Fig. 18. Frequency matrices calculated from the models learned by EBNA-Exact for function Cuban5 with $N=500$ (a) Last generation (b) All generations

generation. However, although the population sizes have grown, for this function both algorithms have learned a similar structure. This fact could explain the results achieved in the study of the convergence reliability presented in Section 7.

# Results for the $C P F$ function 

The $C P F$ function represents another interesting class of functions. It has been shown that Bayesian network based EDAs such as BOA are deceived by this function. Being $C P F$ a decomposable function of bounded complexity, BOA has an exponential scaling for it. Furthermore, in [8] it is shown that increasing the population size does not always produce an improvement in the algorithm's behavior. Authors point to the fact that the learning algorithm used by BOA may fail to detect the higher order type of interactions that occurs in the $C P F$ function.

We will investigate whether there are differences between exact and local learning for the $C P F$ function with parameters: $n=15, k=5, c_{\text {odd }}=5$ and $c_{\text {even }}=0$. For these parameters, the optimum can be reached in $2^{12}$ different points. As a consequence, it is very likely that EBNA reaches the global solution in the first generation. On the other hand, the limitations of the exact learning algorithm do not allow to deal with a higher number of variables. Therefore, we will only analyze the models learned in the first generations of the EDAs, disregarding whether the optimum has been found or not. The models have been calculated using 30 independent experiments.

We start with a population size $N=150$. For this value and higher values of the population size, none of the algorithms was able to recover any type of structure. However, for $N=1000$, EBNA-Exact was able to detect some structure. The frequency matrices calculated for EBNA-Local and EBNA-Exact are shown in Figure 19.

Surprisingly, EBNA-Exact was able to recover an almost perfect structure while EBNA-Local was not. These results reveal that, for problems such as
![img-18.jpeg](img-18.jpeg)

Fig. 19. Frequency matrices calculated from the models learned in the first generation of the EDAs for function $C P F$ with $N=1000$ (a) EBNA Local (b) EBNA-Exact

$C P F$, an accurate learning of the model might be essential to recover the correct structure of the problem. It also shows, that even with exact learning, the population size required to discover the problem structure is higher than for the other additive functions considered.

# HP protein model 

The HP model has served as a benchmark for studying different issues related with the behavior of EDAs [35, 38, 40]. It is a non-binary, nondecomposable problem for which extensive investigation using evolutionary and other heuristic algorithms have been conducted (see [10, 40] and references therein). We use one instance of the HP model to investigate the impact of exact learning. Figure 1 shows one optimal folding for the chosen sequence HPHPPHHPHPPHPHPPHPH.

In the evaluation of the HP model, two variants are considered. In the first one, infeasible individuals are assigned a penalty. In the second variant, individuals are first repaired and after that the HP function (from now on Protein function) is used to evaluate them. In all the experiments conducted for the Protein function, $N=200$ and 50 independent experiments of EBNA-Local and EBNAExact were run.

Since the Protein function is not decomposable, a detailed description of the problem structure is not available and we can not contrast the dependencies learned with a perfect model of the interactions. However, previous research on the application of EDAs to the HP problem [40] has shown that important dependencies between adjacent variables arise. These dependencies are in part determined by the codification used, in which each residue's position depend on the position of the previous two. Thus, the objective of our experiments is twofold. Firstly, to compare the class of models learned by EBNA-Local and EBNA-Exact. Secondly, to investigate the effect that the application of the repair mechanism has in the number and patterns of the interactions learned by the EDAs.
![img-19.jpeg](img-19.jpeg)

Fig. 20. Frequency matrices calculated from the models learned by EBNA-Local for function Protein, repairing procedure with $N=200$ (a) Last generation (b) All generations

![img-20.jpeg](img-20.jpeg)

Fig. 21. Frequency matrices calculated from the models learned by EBNA-Exact for function Protein, repairing procedure with $N=200$ (a) Last generation (b) All generations
![img-21.jpeg](img-21.jpeg)

Fig. 22. Frequency matrices calculated from the models learned by EBNA-Local for function Protein, without repairing procedure with $N=200$ (a) Last generation (b) All generations
![img-22.jpeg](img-22.jpeg)

Fig. 23. Frequency matrices calculated from the models learned by EBNA-Exact for function Protein, without repairing procedure with $N=200$ (a) Last generation (b) All generations

![img-23.jpeg](img-23.jpeg)

Fig. 24. Number of dependencies learned, by EBNA-Exact and EBNA-Local, at each generation for the Protein function, (a) with repairing procedure (b) without repairing procedure

Figures 20 and 21 respectively show the frequency matrices learned by EBNALocal and EBNA-Exact when the repairing procedure is applied. Figures 22 and 23 show frequencies corresponding to the variant in which the repairing procedure is not applied.

An analysis of the figures reveal that EBNA-Exact learns a pattern of interactions more localized around the diagonal representing the dependencies between adjacent variables. The dependencies found by EBNA-Local are more spreadout, away from the diagonal.

We also observe some differences due to the application of the repairing procedure. These differences are particularly noticeable from the analysis of the contour graphs. Taking as an accuracy criterion the connectness of the adjacent variables in the problem representation, we see that repairing helps EBNA-Local to learn more accurate structures. Without repairing, the pattern of interactions is more fragmented. However, repairing does not help EBNA-Exact, which is able to recover a more connected structure without the application of the repairing procedure.

We also analyze the number of dependencies learned by the algorithms at each generation. Figures 24 (a) and (b) respectively show the sum, for the 50 experiments, of the number of dependencies learned by EBNA-Exact and EBNALocal with and without the application of the repairing procedure.

EBNA-Local and EBNA-Exact have a similar behavior. In the initial generations, the number of dependencies learned increases until a maximum is reached and then the number of dependencies starts to diminish.

# 9 Related Work 

In [3], an empirical comparison of EBNAs that use different learning algorithms has been presented. Also in [44] different variants of learning algorithms have been evaluated in the context of EDAs that use polytree models (a constrained

class of Bayesian networks). The use of exact learning algorithms of Bayesian networks was introduced to EDAs in [13], where preliminary results were presented.

Our work is part of an ongoing research trend that investigates the relationship between the problem structure and the class of structure learned during the search by the probabilistic models. A number of researchers have studied the most frequent dependencies learned by the probabilistic models in EDAs and analyzed their mapping with the function structure [2, 22, 27, 34, 37]. A promising related idea is the use of the dependency relationships represented by the probabilistic model to define functions with a desired degree of interactions [31].

The relationship between problem structure and dependencies is analyzed from two different perspectives in [36]. First, using Pearson's chi-square statistics as a measure of the strength of the interactions between pairs of variables in EDAs, the arousal of dependencies due to the selection operator is shown. Secondly, it is shown that for some problems, only a subset of the dependencies may be needed to solve the problem.

More recently, some work has been devoted to analyzing the way in which the different components of the EDA influence the arousal of dependencies [16] and to use the probabilistic models obtained by EDAs to speed up the solution of similar problems in the future [17]. However, the accuracy of the learning algorithm to recover the problem structure from the data has not been investigated in these papers. For instance, for the spin glass problem used as testbeds in [16], most of the dependencies found by hBOA are short dependencies between neighbors in the grid but some long range interactions also appear. We point out that the approximate learning algorithm may produce models that are only an approximate representation of the actual dependencies that arise in the population. The error introduced by the learning method in the estimation of the dependencies should also be taken into account.

# 10 Conclusions 

In this work we have accomplished a detailed analysis of the use of exact learning of the Bayesian network structure in the study of EDAs. We have conducted systematic experiments for several functions. Results show that the type of learning algorithm (whether exact or approximate) may produce significant differences in the class of models learned and in the performance of the EBNA. This fact is important because usually Bayesian network models learned using approximate algorithms are thought to accurately reflect the dependencies that arise in the population. As the example of the $C P F$ function illustrates, this might not be the case for functions with a particular type of higher order dependencies.

On the other hand, we have shown that whenever the size of the problem is manageable, exact learning of Bayesian networks is a more appropriate option for theoretical analysis of the probabilistic dependencies. We have shown that the analysis of the probabilistic models can reveal the effect that some EDA

components, such as repairing procedures, have in the arousal of dependencies. By using exact learning, we have confirmed the critical effect that an inadequate population size may have to capture an accurate probabilistic model.

Among the trends for future research we identify the followings:

- Design of feasible approaches to apply Bayesian network exact learning algorithms to problems with a higher number of variables. A possible alternative will treat these problems by initially identifying interacting sets of variables of manageable size and applying exact learning in each set to obtain a more accurate model of the interactions. Efficient methods for clustering the variables according to the mutual information have already been applied in EDAs [39].
- Application of more advanced techniques for extracting and visualizing the information contained in the models. As the importance of using the information contained in the probabilistic models learned by EDAs is acknowledged, it becomes more necessary to apply more advanced tecniques for information extraction and data visualization.
- Use of the most probable configurations to investigate the influence of the learning algorithms and other EDA components. Procedures that use the probabilistic models learned by EDAs either take advantage of the problem structure or use the probabilistic tables corresponding to some sets of marginal and conditional probabilities. However, information contained in the models can, in many cases, be translated into a set of most probable configurations (with their associated probabilities), which are usually not generated during the evolution. Most probable configurations can help to improve EDA behavior [26] but they could also be used to investigate the algorithms and extract relevant problem information.
- Another way to improve the results of the learning algorithms, particularly of the exact variant, in the discovery of accurate models, could be to increase the quality of the information contained in the population size. Research on this direction has been reported in [7].
- Exact learning could be used to investigate the effects that the existence of constraints, such as those imposed by repairing procedures, have in the arousal of dependencies: Constrained problems remain an important challenge for EDAs. While it is generally difficult to represent the constraints in the probabilistic model, the use of repairing procedures may introduce undesired bias in the construction of solutions. By investigating the structure of the model, it could be possible to detect the bias introduced and conceive ways of correcting it.

Finally, we emphasize that the study of the relationship between the problem structure and the dependencies captured by the probabilistic model should provide answers for the fundamental question of how to select appropriate probabilistic models to optimize a given problem in the framework of EDAs.

# Acknowledgments 

This work has been partially supported by the Etortek, Saiotek and Research Groups 2007-2012 (IT-242-07) programs (Basque Government), TIN2005-03824 and Consolider Ingenio 2010 - CSD2007-00018 projects (Spanish Ministry of Education and Science) and COMBIOMED network in computational biomedicine (Carlos III Health Institute).
