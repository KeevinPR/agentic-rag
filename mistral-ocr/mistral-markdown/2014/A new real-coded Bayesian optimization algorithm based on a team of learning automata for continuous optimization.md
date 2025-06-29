# A new real-coded Bayesian optimization algorithm based on a team of learning automata for continuous optimization 

Behnaz Moradabadi $\cdot$ Hamid Beigy


#### Abstract

Estimation of distribution algorithms have evolved as a technique for estimating population distribution in evolutionary algorithms. They estimate the distribution of the candidate solutions and then sample the next generation from the estimated distribution. Bayesian optimization algorithm is an estimation of distribution algorithm, which uses a Bayesian network to estimate the distribution of candidate solutions and then generates the next generation by sampling from the constructed network. The experimental results show that the Bayesian optimization algorithms are capable of identifying correct linkage between the variables of optimization problems. Since the problem of finding the optimal Bayesian network belongs to the class of NP-hard problems, typically Bayesian optimization algorithms use greedy algorithms to build the Bayesian network. This paper proposes a new real-coded Bayesian optimization algorithm for solving continuous optimization problems that uses a team of learning automata to build the Bayesian network. This team of learning automata tries to learn the optimal Bayesian network structure during the execution of the algorithm. The use of learning automaton leads to an algorithm with lower computation time for building the Bayesian network. The experimental results reported here show the preference of the proposed algorithm on both uni-modal and multi-modal optimization problems.


Keywords Estimation of distribution algorithms $\cdot$ Bayesian optimization algorithm $\cdot$ Learning automata

[^0]
[^0]:    B. Moradabadi $(\boxtimes) \cdot$ H. Beigy

    Department of Computer Engineering, Sharif University of Technology, Tehran, Iran
    e-mail: behnazmoradabadi@gmail.com; moradabadi@ce.sharif.edu
    H. Beigy
    e-mail: beigy@sharif.edu

# 1 Introduction 

In order to make a strongly search algorithm in evolutionary computing, a sort of evolutionary algorithms has been proposed. Genetic algorithm is a type of stochastic optimization techniques influenced by genetics and natural evolution [1]. In each generation of Genetic algorithm, a set of candidate solutions is selected and the new generation is produced using recombination (crossover) and mutation operators. Public, fixed, problem-independent mutation and recombination operators frequently lead to miss the knowledge of the relationship between variables, which is called building blocks, and result in convergence to local optima [2]. The building blocks are sub-problems of the optimization problem that show the relations and dependencies among the variables of the problem. In order to solve the above mentioned problem, the estimation of distribution algorithms (EDAs) are proposed [3]. These algorithms are stochastic optimization algorithms that construct an explicit probabilistic model from the candidate solutions found from the previous generations. Then, the new solutions are produced by sampling the constructed probabilistic model. Finally, the next generation will be produced from the sampled solutions using the replacement operator. This process is repeated until the stopping criteria have been reached. Several EDAs have been proposed for solving discrete and continuous problems [4, 5]. Extended compact genetic algorithm (ECGA) [6], factorized distribution algorithm (FDA) [7], and Bayesian optimization algorithm (BOA) [8] are examples of EDA algorithms proposed for discrete optimization problems. Estimation of Gaussian networks algorithm (EGNA) [9], mixed Bayesian optimization algorithm (MBOA) [10], (mixed) iterative density-estimation evolutionary algorithms (mIDEAs) [11], real-coded Bayesian optimization algorithm (rBOA) [12], and Bayesian networks and Gaussian mixture model (GMM) [13] are examples of EDA algorithms for continuous optimization problems.

In EGNA, a Gaussian network is constructed in each generation by the means of a scoring metric and the new generation is sampled from the constructed network [9]. The EGNA only uses one single-peak Gaussian model and hence is not appropriate for solving complex problems [9]. The MBOA tries to learn a Bayesian network from the selected individuals [10]. The structure of this network is a set of decision trees with univariate normal-kernel leaves. The MBOA generates one decision tree for each variable and then uses these decision trees to separate the problem space. The mIDEAs exploit Bayesian information criterion to select a probabilistic model and then employ a mixture of normal distributions to fit the model [11]. The mIDEAs use a mixture of normal distributions by clustering the candidate solutions and hence cannot preserve the population building block crossover (PBBC). PBBC is a kind of population-wise building-block crossover that uses a probability distribution calculated from the building-blocks [3, 4]. In the sampling phase, mIDEAs select a distribution (a cluster) of a mixture of normal distributions and generate the new individuals from it. Hence, these algorithms cannot realize the PBBC unless one cluster contains most of building blocks. In rBOA, the promising solutions are selected from the current population using a parent selection method, and a Bayesian network is constructed to model the distribution of the promising solutions [12]. Then the new individuals are sampled from the constructed Bayesian network using the following procedure. In the sampling

phase, the sub-trees (building blocks of the problem) of the Bayesian network are extracted and the whole solutions of each sub-tree are clustered to make a mixture of normal distributions. The new partial solutions of each sub-tree are sampled from the corresponding mixture of normal distributions. Finally, the new individuals are merged into the main population and replaced some of the old ones. The above steps are repeated until some stopping criteria are satisfied [12]. Unlike mIDEAs, which consider a mixture of normal distributions of the population in the model sampling phase, rBOA uses a mixture of normal distributions of each building block in the model sampling phase. So, rBOA can better preserve the PBBC in comparison to the mIDEAs in continuous optimization problems.

Bayesian networks and Gaussian mixture model (GMM) is an evolutionary continuous optimization algorithm that uses a Bayesian network to model the dependencies between the variables of the problem. Then, one GMM is adopted to model the probability distribution of each sub-problem and the new generation is produced from the GMM of each sub-problem [13].

In [14, 15], an improved version of real-coded Bayesian optimization algorithm, called IrBOA, has been proposed. The IrBOA utilizes an adaptive clustering method to decompose the problem space into multiple Bayesian networks. Each Bayesian network has its own structure and parameters. The adaptive clustering method results in searching the problem space efficiently in the starting generations of the algorithm and also improves the quality of solutions with realizing the PBBC in the next generations of the algorithm. The use of adaptive clustering leads to realizing the PBBC; because when the diversity of solutions is decreased, the number of clusters is also decreased. Hence, a fewer number of Bayesian networks is generated and more building blocks are aggregated in one Bayesian network [14].

In many EDAs, generating the model of the dependencies and independences of the variables of a problem is considered as a bottleneck; because in many situations, finding the best model corresponding to the candidate solutions is a difficult combinatorial problem. Usually, many EDAs use greedy algorithms to create the model. So, using some techniques for generating a model is a valuable context in EDAs.

On the other hand, learning automaton (LA) is an adaptive decision making unit that tries to learn the optimal action from a set of allowable actions by interacting with a random environment [16]. In each step, it selects an action from its action-set. The action selection in the LA is based on a probability distribution over the actionset. The selected action is applied to the environment and then a reinforcement signal is produced by the environment. LA updates the probability distribution of its actions according to both reinforcement signal and a learning algorithm and again chooses an action. These steps are repeated until LA converges to some action.

In this paper, we propose a new real-coded Bayesian optimization algorithm based on the learning automaton, called LA-rBOA, to optimize the real-valued functions in continuous domains. The proposed algorithm uses a team of LAs to build the Bayesian network. For a successful application, the rBOA must learn a network that reflects the linkage of the problem properly. The problem of learning the structure of a network based on a scoring metric is a difficult combinatorial problem [17]. So, there is no known polynomial-time algorithm to determine the optimal structure of a Bayesian network with respect to the most scoring metrics and usually a simple greedy

algorithm is used to generate the Bayesian network [18]. This paper utilizes a team of LAs to produce the Bayesian network instead of the greedy algorithms. It uses one LA for each possible edge in the Bayesian network. Each LA determines either the corresponding edge should be appeared in the Bayesian network or not. The Bayesian network is built according to the selected actions of learning automata. Using LA for generating Bayesian network leads to generating Bayesian network in lower computation time. Then the new individuals are sampled from the constructed Bayesian network. Finally, the probability distribution of actions of each LA is updated according to the impact of the corresponding edge in the produced Bayesian network. Because of the nature of LA, it tries to learn the optimal behavior and so the optimal Bayesian network structure. These steps are repeated until the action of each LA converges to some value. The experimental results show that the LA-rBOA is superior to the some EDAs such as IrBOA and mIDEA and some other population based algorithms $[13,19,20]$ in term of accuracy and performance.

The rest of the paper is organized in the following way. Section 2 explains the Bayesian Networks and LA is described briefly in Sect. 3. Section 4 presents the proposed real-coded Bayesian optimization algorithm based on a team of LAs and Sect. 5 reports the experimental results obtained with the LA-rBOA. The paper concludes with a conclusion given in Sect. 6.

# 2 Bayesian networks 

A Bayesian optimization algorithm constructs a Bayesian network using a set of promising solutions and then samples the next generation from the constructed Bayesian network [21]. Various algorithms can be used to build the Bayesian network. Also there is a variety of methods can be used to measure the quality of the constructed network. Many of these metrics can use the prior information about the problem to improve the quality of the network and the efficiency of the algorithm [21].

A Bayesian network $\mathrm{M}=(\zeta, \theta)$ consists of a structure $\zeta$ and a set of parameters $\theta$. The structure of a network is described by a directed acyclic graph with a set of nodes corresponding to the problem variables and a set of edges corresponding to the conditional dependencies between variables. The parameters of the network $(\theta)$ is a set of probability distributions that is described as a product of probability density functions. Learning the structure of Bayesian networks has two components [5]: a scoring metric and a search procedure. Scoring metric evaluates the quality of the constructed Bayesian network. In other words, it determines how much the structure of the constructed Bayesian network fits the promising solutions. Search procedure determines an algorithm to find a network that better fits the promising solutions with respect to a given scoring metric. In the rest of this section, we briefly describe each of these two components.

### 2.1 Scoring metric

There is a variety of metrics proposed for evaluation of Bayesian networks such as Bayesian metrics, Minimum description length metrics, and Bayesian information

criterion, to mention a few. Bayesian metrics measure the quality of the Bayesian network by computing a marginal likelihood of the Bayesian network with respect to the given data and inherent uncertainties [5, 12, 21]. Minimum description length metrics are based on the assumption that the number of regularities in the data encoded by a model is somehow proportional to the amount of data compression allowed by the model [21]. The Bayesian information criterion (BIC) is a criterion for model selection among a finite set of models and it is based on the likelihood function.

Let's consider a $d$-dimensional real-value optimization problem. The joint probability density function (pdf) of this optimization problem can be written according to Eq. (1):

$$
f_{M(\zeta, \theta)}(Y)=\prod_{i=1}^{d} f_{i \hat{\sigma}}\left(Y_{i} \mid \Pi_{i}\right)
$$

where $Y=\left(Y_{1}, \ldots, Y_{d}\right)$ represents a vector of real-valued random variables, $\Pi_{i}$ is the set of parents of node $\mathrm{Y}_{\mathrm{i}}$, the set of nodes from which there exists an edge to $\mathrm{Y}_{i}$, and $f_{i \hat{\sigma}}\left(Y_{i} \mid \Pi_{i}\right)$ is the conditional pdf of $\mathrm{Y}_{i}$ given $\Pi_{\mathrm{i}}$ with parameters $\theta_{i}[5,12,21]$. Let $S=\left(Y^{0}, Y^{1}, \ldots, Y^{|S|-1}\right)$ be the set of promising solutions, the BIC metric is given by the following equation:

$$
B I C\left(f_{M(\zeta, \theta)}, S\right)=-\ln \left(\prod_{j=0}^{|S|-1} f_{M(\zeta, \theta)}\left(\mathrm{Y}^{\mathrm{j}}\right)\right)+\gamma \ln (|S|)|\theta|
$$

where $\gamma$ regularizes the extent of penalty [12]. This metric is a combination of the model fitting error and the model complexity and must be minimized. Since the minimal negative log-likelihood is equivalent to minimal entropy, Eq. (2) can be rewritten as the following equation

$$
B I C\left(f_{M(\zeta, \theta)}, S\right)=|S| H\left(f_{M(\zeta, \theta)}(Y)\right)+\gamma \ln (|S|)|\theta|
$$

where $\mathrm{H}\left(\mathrm{f}_{\mathrm{M}(\zeta, \theta)},(\mathrm{Y})\right)$ represents the differential entropy of $\mathrm{f}_{\mathrm{M}(\zeta, \theta)}(\mathrm{Y})[12,22,23]$. In order to search the problem space efficiently, a (joint) mixture distribution is used for modeling the promising solutions. Hence, Eq. (3) can be rewritten as:

$$
B I C\left(f_{M(\zeta, \theta)}, S\right)=\sum_{j=0}^{k}\left|S_{j}\right| H\left(f_{M\left(\zeta, \theta_{j}\right)}(Y)\right)+k \gamma \ln (|S|)\left|\theta_{j}\right|
$$

where k is the number of mixture components, $\left|\mathrm{S}_{\mathrm{j}}\right|$ is the expected number of the promising solutions drawn from a probability distribution $\mathrm{H}\left(\mathrm{f}_{\mathrm{M}\left(\zeta, \theta_{j}\right)}(\mathrm{Y})\right)$, and $\left|\theta_{\mathrm{j}}\right|$ is the size of the parameters of jth mixture component [22, 23].

# 2.2 Search procedure 

Given a scoring metric, the problem of learning the structure of a Bayesian network belongs to the class of NP-hard problems and there is no known polynomial-time

algorithm for finding the best network structure corresponding to most scoring metrics [17]. Usually, a simple, greedy algorithm is used to build the network [18, 23]. The greedy algorithm adds an edge with the greatest improvement of the current network quality in each step until no more improvement is possible. The initial network structure can be a graph with no edges; also, it can take advantage of using the prior information such as using the best tree computed by the polynomialtime maximum branching algorithm [5, 18]. Since Bayesian networks are acyclic graphs, after each operation, the graph structure must be validated and all cycles must be removed from the constructed graph [12, 24, 25].

# 3 Learning automata 

Learning automaton is an adaptive decision making device that tries to learn the optimal action from a set of allowable actions in an unknown random environment [16]. This process is done by interacting between an automaton and a random environment. At each time $t$, the automaton selects an action, $\alpha(t)$ using its action probability distribution, $p(t)$, and applies the selected action to the random environment. Then, the random environment generates a stochastic reinforcement signal, $\beta(t)$, to the automaton [14]. The automaton updates the action probability distribution using both the reinforcement signal and a learning algorithm. Figure 1 shows the interaction between a learning automaton and its environment. Learning automaton based on to its action-set can be classified into two major classes: finite action-set LA (FALA) and continuous action-set LA (CALA) [26-28]. FALA has finite action-set but CALA has actions chosen from real line. For an $r$-action FALA, the action probability distribution is represented by an $r$-dimensional probability vector and is updated by the learning algorithm. For a CALA, the action probability distribution is represented by a continuous function and this function is updated by the learning algorithm at any time. Learning automata have been used successfully in many applications such as routing and call admission control in computer network [29, 30], solving NP-Complete problems [31-33], and too many other applications [26, 34-39]. For further information about LA please refer to [39].

## 4 The proposed real-coded Bayesian optimization algorithm

The problem of finding the optimal Bayesian network corresponding to the variables dependencies of a problem belongs to the class of NP-hard problems, and Bayesian

Fig. 1 The interaction between learning automaton and the environment
![img-0.jpeg](img-0.jpeg)

optimization algorithms typically use greedy algorithms to generate Bayesian networks; these greedy algorithms take long execution time. In this section, we propose a new real-coded Bayesian optimization algorithm (LA-rBOA), which is based on a team of learning automata for building the Bayesian network. The proposed algorithm uses a team of learning automata to choose the structure of the Bayesian network instead of using a greedy algorithm. This algorithm leads to decreasing the execution time for constructing Bayesian network. The proposed algorithm has two main phases: model building and sampling phases as described below. In model building phase, the team of learning automata chooses a structure and then based on the effectiveness of each edge a separate reinforcement signal is produced. Finally the team of learning automata updates the action probability vectors of all learning automata according to the received signal and a learning algorithm. The effectiveness of the each edge is estimated by using the promising solutions of the current generation. After building the structure of the network, in sampling phase the offspring are generated by sampling from the constructed network. Finally, the new population is selected according to the fitness evaluation. The pseudo code of the proposed algorithm is given in Algorithm 1. In the following sections, we describe the model building and the model sampling phases in detail.

```
Algorithm 1: Pseudo code of the proposed algorithm (LA-rBOA)
    1: Let \(d\) be dimension of the problem, \(N p\) be population size, and \(m\) be the number of LAs, i . e . \(m=d *(d-1)\);
    2: Let \(t\) be the generation counter and initially set to 0 and \(M a x_{N F C}\) be the total number of generations.
    3: Create a random population of \(N p\) individuals.
    4: Set the initial actions probability distribution of each learning automaton to be uniform.
    5: while \(t<M a x_{N F C}\) do
        Generate LAs' action, \(\left(\alpha_{1}(\mathrm{t}), \alpha_{2}(\mathrm{t}), \ldots, \alpha_{m}(\mathrm{t})\right)\).
        Build the structure of the Bayesian network based on LAs' actions and remove all cycles from the constructed network
        Select \(t \%\) individuals from population based on their fitness.
        Update the actions probability distribution of each learning automaton \(A_{j}\) based on the reinforcement signal \((\beta(j, t))\).
        Extract all trees (sub-problems) in the constructed Bayesian network.
        Cluster the partial solutions corresponding to each tree (sub-problem) and assign a score \(v(l, r)\) to cluster \(C_{i}\) of tree \(r\).
        for \(n=1\) to \(N p\) do
            for \(r=1\) to number of sub-problems do
            Select a cluster \(C_{i}\) of sub-problem \(r\) based on the coefficient score \(v(l, r)\)
            Generate the partial solution of nth individual based on the conditional normal distribution of cluster \(C_{i}\).
            end for
            Merge all partial solutions together to create a new individual.
        end for
        Merge the new and the old generations, evaluate its fitness, and choose the best \(N p\) individuals as the new generation.
        Set \(t=t+1\)
    21: end while
```


# 4.1 Model building 

This step tries to find a model, $\mathrm{M}=(\zeta, \theta)$, that better fits the promising solutions. Finding the structure of the network has two components: a scoring metric and a search procedure [5, 18, 21, 23]. The proposed algorithm (LA-rBOA) uses the BIC

score given in Eq. (4) for the scoring metric and a team of learning automata to generate the Bayesian network structure as a search procedure. In what follows, we describe the search procedure.

Let $d$ be the dimension of the real-valued optimization problem. Hence, the corresponding Bayesian network has $d$ nodes. Since the Bayesian network is a directed graph, the maximum number of edges of the network with $d$ nodes is $m=d \times(d-1)$. We use a team of $m$ learning automata $\left(\mathrm{A}_{1}, \mathrm{~A}_{2}, \ldots, \mathrm{~A}_{\mathrm{m}}\right)$ with action-set $\{0,1\}$ and each learning automaton is associated to one edge. Let the action of automaton $A_{j}$ at time $t$ denoted by $\alpha_{j}(t)$ and it determines either the corresponding edge should be appeared in the Bayesian network or not. Action $\alpha_{j}(t)=0$ means that the corresponding edge does not appear in the Bayesian network while value $\alpha_{j}(t)=1$ means that the corresponding edge appears in the network. The action probability vector of automaton $A_{j}($ for $j=1,2, \ldots, m)$ at time $t$ is denoted by $p^{j}(t)=\left(p_{0}^{j}(t), p_{1}^{j}(t)\right)$, where $p_{i}^{j}(t)$ is the probability of choosing action $\alpha_{i}$ (for $i=0,1$ ) at time $t$. At the first iteration, because there is no prior information about the problem variables dependencies, we use the uniform probability distribution to select actions; i.e. $p_{i}^{j}(0)=0.5$ (for $j=1,2, \ldots, m$ and $i=0,1$ ). The initial action probability vector for each automaton $A_{j}$ can also be configured based on the prior information about the variables dependencies of the problem. After selecting actions for all learning automata, we use this information to build a Bayesian network structure. The search procedure uses the selected action of each automaton to determine either the corresponding edge must appear in the Bayesian network or not. Now, the constructed Bayesian network structure may have cycles. In order to remove cycles, the search procedure uses depth first search algorithm (DFS) with a random start node to navigate the current structure and mark all of the back edges which point from a node to one of its ancestors After detecting all back edges, the search procedure removes all. Because of choosing a random node in the depth search algorithm, the proposed algorithm has the chance of removing different edges in the execution of the algorithm to choose the structure of the network without biasing to the any edge in the network.

In the next step, the reinforcement signal for $A_{j}$ is calculated based on the estimated influence of the corresponding edge on the score of the constructed Bayesian network. In order to do this, $\tau \%$ of the best current solutions are selected and a reinforcement signal is calculated by the difference between the BIC score of the current Bayesian network and the Bayesian network that is constructed by removing the edge corresponding to $A_{j}$. The estimated influence of the $A_{j}$ at time $t$, $R(j, t)$, is calculated based on the selected promising solutions using the following equation:

$$
R(j, t)=B I C\left(K, f_{M(\zeta, \theta)}(Y), S\right)-B I C\left(K, f_{M(\zeta, \theta)_{-j}}(Y), S\right)
$$

where $B I C\left(K, f_{M(\zeta, \theta)}(Y), S\right)$ is the BIC score of the constructed Bayesian network and $B I C\left(K, f_{M(\zeta, \theta)_{-j}}(Y), S\right)$ is the BIC score of the Bayesian network that is created by removing the edge corresponding to automaton $A_{j}$. Hence, the reinforcement

signal of the $A_{j}$ at time $t,(j, t)$, is the normalized value of $R(j, t)$ calculated using the following equation:

$$
\beta(j, t)=\operatorname{Max}\left(0, \frac{R(j, t)-\operatorname{Min}(j)}{\operatorname{Max}(j)-\operatorname{Min}(j)}\right)
$$

where $\operatorname{Min}(j)$ and $\operatorname{Max}(j)$ are the minimum and maximum of the estimated influence of $A_{j}$ up to time $t$. According to the given reinforcement signal, learning automata with larger reinforcement signal value have more impact on the Bayesian network structure. Then the algorithm updates the action probability distribution of each automaton using the following equation:

$$
p_{i}^{j}(t+1)= \begin{cases}{\left[\left(p_{i}^{j}(t)+(1-\lambda) \beta(j, t)\right)\right] \omega(t)} & \alpha_{j}(t)=i \\ 1-p_{i}^{j}(t) & \alpha_{j}(t) \neq i\end{cases}
$$

where $\lambda$ is a constant parameter and $\omega(t)$ is parameter to guarantee that $p^{j}(t+1)($ for $j=1,2, \ldots, m)$ remains a probability vector.

# 4.2 Model sampling 

After construction of a Bayesian network, new generation is sampled from the Bayesian network. The sampling method of the proposed algorithm is the same as the method used in the improved real-coded BOA algorithm (IrBOA) [14, 15]. In order to do this, first all maximal connected sub-graphs are extracted from the constructed Bayesian network. These sub-graphs determine the sub-problems whose variables have interactions. In order to simplify the presentation, the promising solutions of a sub-problem are called the partial solutions of that sub-problem. Then the partial solutions of each sub-problem are partitioned into some groups using a clustering algorithm. The clustering the partial solutions of each sub-problem results in realizing the non-linearity and searching the space effectively [12, 21]; because the non-linear dependencies can be modeled with a combination of piecewise linear interaction models. Also, the clustering has advantage of searching the problem space efficiently [14, 15]. It considers the partial solutions of each sub-problem independently and so it can implement the population building block crossover (PBBC). For clustering the partial solutions, the algorithm utilizes an adaptive clustering method, $k^{\prime}$-means algorithm [40]. $k^{\prime}$-means clustering is an extended version of $k$-means clustering in which there is no need to determine the number of clusters as a parameter because the correct number of clusters is determined during the execution of the clustering algorithm. $k^{\prime}$-means algorithm uses the density of clusters to determine the correct number of clusters. If the $i$ th cluster, denoted by $C_{i}$, has $n_{i}$ partial solutions in a sub-problem with $N$ partial solutions then the amount information of this cluster denoted by $I\left(C_{i}\right)$, is calculated using the following equation:

$$
I\left(C_{i}\right)=\|\log (n i / N)\|
$$

This information is used to approximate uncertainty about $C_{i}$ [40]. The $k^{\prime}$-means algorithm has two phases: in the first phase, $k^{\prime}$-means uses $k$-means algorithm to

determine the initial cluster centers. The number of initial clusters in $k$. -means is determined with parameter $k^{\prime}$ that is greater than the correct number of clusters [40]. In the second phase, for each partial solution $x t$ and all $k^{\prime}$. clusters, $k^{\prime}$-means calculates the cluster membership function $I(x t, j)$ using Eq. (9):

$$
I\left(x_{t}, j\right)=\left\{\begin{array}{lr}
1 & \text { if } j=\underset{i}{\operatorname{argmin}}\left\{d\left(x_{t}, C_{i}\right)\right\} \\
0 & \text { otherwise }
\end{array} i=1,2, \ldots, k t\right.
$$

where $d\left(x_{t}, C_{i}\right)$ is a distance metric and calculated using the following equation:

$$
d\left(x_{t}, C_{i}\right)=x_{t}-C_{i}-\operatorname{Elog}\left(I\left(C_{i}\right)\right)
$$

and E is a constant [40]. Then every paral solution of a sub-problem is grouped into the cluster whose centroid is closest to it based on the cster membership $I(x t, j)$. So, the center of cluster $C_{i}$ is calculated as the mean value of its members as given below:

$$
C_{i}=\frac{1}{\left|C_{i}\right|} \sum_{x_{t} \in C_{i}} x_{t} \quad \text { for }\left(i=1,2, \ldots, k^{\prime}\right)
$$

where $k^{\prime}$ is the current number of clusters. These two phases are repeated until all cluster centers remain fixed for all of the partial solutions [40].

After clustering the partial solutions of each sub-problem, a coefficient score is assigned to each cluster according to the ratio of the number of partial solutions of a cluster in sub-problem $r$ to the whole partial solutions of sub-problem $r$. This score is used as the probability of choosing a cluster to generate partial solutions. In other words, if the partial solutions of sub-problem $r$ are grouped in $k^{\prime}$ clusters and cluster $C_{i}$ has $n_{r, i}$ partial solutions then coefficient score of cluster $C_{i}$ corresponding to the sub-problem $r$ denoted by $v(r, i)$ and written by the following equation.

$$
v(r, i)=\frac{n_{r, i}}{\prod_{i=1}^{k^{\prime}} n_{r, i}}
$$

In order to generate a partial solution corresponding to sub-problem $r$, the LArBOA chooses cluster $C_{i}$ with probability $v(r, i)$. It first employs the normal probability distribution function to the partial solutions of the selected cluster and then generates the new partial solutions from the distribution [12, 21, 23]:

$$
f\left(Y_{0} \mid Y_{1}, Y_{2}, \ldots, Y_{n}\right)=\frac{1}{\sqrt{2 \pi}} e^{-\frac{\left(Y_{0}-n_{0}\right)^{2}}{2 \pi^{2}}}
$$

where $Y_{0}$ is the partial solution that must be produced, $Y_{1}, Y_{2}, \ldots, Y_{n}$ are the parents of $Y_{0}$,

$$
\begin{gathered}
\sigma=\frac{1}{\sqrt{\left(\sum^{-1}\right)_{0,0}}} \\
\mu=\mu_{0}-\frac{\sum_{j=1}^{Y_{n}}\left(Y_{j}-\mu_{j}\right)_{j, 0}}{\left(\sum^{-1}\right)_{0,0}}
\end{gathered}
$$

and $\mu_{\mathrm{j}}$ is the mean of $\mathrm{Y}_{\mathrm{j}}$ and is the inverse of covariance matrix for $\left(\mathrm{Y}_{0} \mid \mathrm{Y}_{1}, \mathrm{Y}_{2}, \ldots, \mathrm{Y}_{\mathrm{n}}\right)$ of cluster $C_{\mathrm{j}}$.

# 5 Experimental results 

In order to evaluate the performance of the proposed algorithm, computer experiments have been conducted and the performance of the proposed algorithm has been compared with the performance of some related algorithms on the standard benchmark test functions (CEC2005 [41] and CEC2011 [42] test functions). In these experiments, we use the quality of solutions, the computation time, and the convergence rate as the performance criteria. In the rest of this section, we first give the test functions and then give a set of six experiments. In the first experiment, we study the sensitivity of the proposed algorithm on its parameters. In the second experiment, the performance of the proposed algorithm compared with the performance of some related EDAs on the CEC2005 test functions. In the third experiment, the performance of the LA-rBOA is compared with the performance of some population based algorithms on the CEC2005 test functions. In the fourth and fifth experiments, the computation time and convergence rate of the LA-rBOA is compared with some EDAs on the CEC2005 test functions, respectively. Finally, in the sixth experiment, the performance of the LA-rBOA is compared with some algorithms used in IEEE CEC2011 competition on the CEC2011 test functions.

### 5.1 Test functions

In order to compare the performance of algorithms CEC2005 and CEC2011 test functions have been used. In what follows, these test functions are given briefly.

### 5.1.1 CEC2005 test functions

This set of test functions is chosen from the benchmark functions used in CEC2005 [41]. This set includes five uni-modal (F1-F5) and twenty multi-modal (F6-F25) functions and the quality of solution is used as the performance measure. Each function in the test suite presents a real-value function that must be minimized and the global optimum of all functions is at the origin. The information of this test suit is given in Table 1. This benchmark has two important parameters: the dimension of each function denoted by $d$ and the shift value of each function denoted by FBias. In the experiments given in the paper, $d$ and FBias are set to 30 and 0 , respectively.

### 5.1.2 CEC2011 test functions

The CEC2011 benchmark has 22 real-world optimization functions and used to evaluate algorithms submitted in IEEE CEC2011 [42]. These problems include a parameter estimation problem for frequency-modulated sound saves (T1); a Lennard-Jones potential problem (T2); a bifunctional catalyst blend control problem (T3); a stirred tank reactor control problem (T4); two Tersoff potential

Table 1 The CEC2005 benchmark functions

| Function | Function name | Range |
| :--: | :--: | :--: |
| F1 | Shifted sphere function | $\begin{gathered} \hline[-100, \\ 100] \end{gathered}$ |
| F2 | Shifted Schwefel's problem | $\begin{gathered} \hline[-100, \\ 100] \end{gathered}$ |
| F3 | Shifted rotated high conditioned elliptic function | $\begin{gathered} \hline[-100, \\ 100] \end{gathered}$ |
| F4 | Shifted Schwefels problem with noise in fitness | $\begin{gathered} \hline[-100, \\ 100] \end{gathered}$ |
| F5 | Schwefels problem with global optimum on bounds | $\begin{gathered} \hline[-100, \\ 100] \end{gathered}$ |
| F6 | Shifted Rosenbrocks function | $\begin{gathered} \hline[-100, \\ 100] \end{gathered}$ |
| F7 | Shifted rotated Griewanks function without bounds | $[0,600]$ |
| F8 | Shifted rotated Ackleys function with global optimum on bounds | $[-32,32]$ |
| F9 | Shifted Rastrigins function | $[-5,5]$ |
| F10 | Shifted rotated Rastrigins function | $[-5,5]$ |
| F11 | Shifted rotated Weierstrass function | $[-0.5,0.5]$ |
| F12 | Schwefels problem 2.13 | $[-\pi, \pi]$ |
| F13 | Expanded extended Griewanks plus Rosenbrocks function (F8F2) | $[-3,1]$ |
| F14 | Shifted rotated expanded Scaffers F6 | $\begin{gathered} \hline[-100, \\ 100] \end{gathered}$ |
| F15 | Hybrid composition function | $[-5,5]$ |
| F16 | Rotated version of hybrid composition function | $[-5,5]$ |
| F17 | Rotated hybrid composition function with noise in fitness | $[-5,5]$ |
| F18 | Rotated hybrid composition function | $[-5,5]$ |
| F19 | Rotated hybrid composition function with a narrow basin for the global optimum | $[-5,5]$ |
| F20 | Rotated hybrid composition function with the global optimum on the bounds | $[-5,5]$ |
| F21 | Rotated hybrid composition function | $[-5,5]$ |
| F22 | Rotated hybrid composition function with high condition number matrix | $[-5,5]$ |
| F23 | Non-continuous rotated hybrid composition function | $[-5,5]$ |
| F24 | Rotated hybrid composition function | $[-5,5]$ |
| F25 | Rotated hybrid composition function without bounds | $[2,5]$ |

minimization problems (T5 and T6); a radar poly-phase code design problem (T7); a transmission network expansion problem (T8); a transmission pricing problem (T9); an antenna array design problem (T10); two dynamic economic dispatch problems (T11.1 and T11.2); five static economic dispatch problems (T11.3-T11.7); three hydrothermal scheduling problems (T11.8-T11.10); and two spacecraft trajectory optimization problems (T12 and T13). For additional information about this set of benchmark functions, please refer to the Ref. [42].

# 5.2 Sensitive analysis 

In this section, we study the effect of each parameter on the performance of the LArBOA. The proposed algorithm has six parameters: (1) Selection strategy method, (2) Parameter $\tau$ in the selection strategy, (3) Population size (Np), (4) Complexity factor in the BIC score $(\gamma)$, (5) The number of Mixture components (k) and (6) The decay Factor in the learning rule of learning automata ( $\lambda$ ). In order to study the effect of one parameter, the values of other parameters are set fixed. The default values of the parameters are listed in the following setting: (1) parent selection method is truncation selection (2) parameter $\tau=20$, (3) population size $(\mathrm{Np})=2,000$, (4) complexity factor of BIC score $\gamma=0.5$, (5) the number of Mixture components $(\mathrm{k})=30$, (6) decay factor of all learning automata be $\lambda=0.4$. In what follows, we study the effect of each parameter on the performance of the algorithm.

The effect of different selection strategies: The goal of this experiment is to study the performance of the LA-rBOA based on different selection strategies. Comparison is based on truncation and tournament selection methods. In tournament selection, $\tau$ individuals are randomly picked from the population and the best one is selected as a candidate solution. In truncation selection the best $\tau \%$ individuals of the population are selected as the candidate solutions. Figure 2a shows the number of function evaluations needed to optimize function F9 with respect to different selection strategies. Based on the results, LA-rBOA has better performance on the truncation selection method than the tournament selection. This parameter also has the same effect on other test functions.

The effect of parameter $\tau$ in the truncation selection: This experiment compares the impact of parameter $\tau$ in truncation selection on the performance of the LArBOA. To do this, parameter $\tau$ is varied from the set $\{20 \%, 40 \%, 60 \%\}$. and the maximum number of function calls is calculated for function F9. Figure 2b presents that the best value of parameter $\tau$ for function F9 is 20 . The same behavior is also observed in other functions.

The effect of population size ( Np ): This experiment compares the impact of parameter Np on the performance of the LA-rBOA. To do this, value of F9 is chosen from the set $\{500,1000,1500, \ldots, 5000\}$ and the results for function F9 are presented. Figure 2c presents the best value of parameter Np for function F9 is between 2,000 and 5,000. This parameter also has the similar effect on other test functions.

The effect of complexity factor in the BIC score $(\gamma)$ : This experiment compares the effect of parameter $\gamma$ on the performance of the LA-rBOA on function F9. Figure 2d shows that the best value of the parameter $\gamma$ for function F9 is between 0.4 and 0.5 . The same behavior was observed on other functions.

The effect of the number of mixture components (K): The influence of the number of mixture components on the performance of the LA-rBOA is studied for function F9 and the result is shown in Fig. 2e. This figure represents that the best value of

![img-1.jpeg](img-1.jpeg)

Fig. 2 Parameters analysis in the LA-rBOA. a Different selection strategies on function F9. b Parameter $\tau$ on function F9. c Population size, Np, on function F9. d Parameter $\gamma$ on function F9. e Mixture components, K, on function F9. f Parameter $\lambda$ on function F9
parameter k , for function F9 is about 30. The same behavior was also seen on other test functions.

The effect of decay factor in the LA learning rule ( $\lambda$ ): Finally, the effect of parameter $\lambda$ on the performance of the LA-rBOA on function F9 is presented in Fig. 2f and it shows that the best value of parameter $\lambda$ for function F9 is between 0.2 and 0.4 . This parameter also has the same effect on other test functions.

# 5.3 Comparison of the LA-rBOA with some EDA algorithms 

In this section, LA-rBOA is compared with the improved real-coded BOA (IrBOA) [14] [15] and the mIDEA [11] on the CEC2005 test functions. Based on No Free Lunch theorem: "for any algorithm any elevated performance over one class of problems is offset by performance over another class" [43]. So, the LA-rBOA tries to solve a class of benchmark functions in term of accuracy and efficiency. For all conducted experiments, the parameters of the LA-rBOA are chosen empirically based on the sensitivity analysis given in the previous section. Parameter setting for the conducted experiments are: (1) parent selection method is truncation selection (2) parameter $\tau=20$, (3) population size $(\mathrm{Np})=2,000$, (4) complexity factor in BIC score $\gamma=0.5$, (5) the number of Mixture components $(\mathrm{k})=30$, (6) decay factor in LA learning rule $\lambda=0.4$. Also, two points should be mentioned: (1) the initial population in all algorithms is created based on the uniform distribution on the constraints of each function, and (2) in order to have a fair comparison, the maximum number of function calls, $\operatorname{Max}_{\mathrm{NFC}}$, is set to $1,500 \times d$.

In this experiment, the parameters setting of the IrBOA and the mIDEA are borrowed from [12, 15]. The results for the LA-rBOA, the IrBOA and the mIDEA on the uni-modal functions F1-F5 are summarized in Table 2. For each function the mean error value and the standard deviation of obtained fitness values on the 50 independent runs are presented. It should be mentioned that for the following tables given in this section, the best results are highlighted. Also, in order to have a better comparison, a set of two-tailed $t$ test were taken; because the $t$ test determines the difference between the means of two independent samples. The $t$ test can be used to check whether the two algorithm means are different and calculated using the following equation:

$$
\mathrm{t}-\operatorname{test}(\mathrm{A} 1, \mathrm{~A} 2)=\frac{\hat{\mathrm{X}}_{1}-\hat{\mathrm{X}}_{2}}{\sqrt{\frac{\mathrm{n}_{1}^{2}}{\mathrm{n}_{1}}+\frac{\mathrm{n}_{2}^{2}}{\mathrm{n}_{2}}}}
$$

where $\hat{X}_{i}, s_{i}^{2}$ and $\mathrm{n}_{\mathrm{i}}$ are the means, standard deviation, and the number of runs of algorithm $i$, respectively. In this experiment, we consider the LA-rBOA as algorithm $A 1$. Hence, if the result of $t$ test between the LA-rBOA and another algorithm is a negative value then the LA-rBOA statistically outperforms another algorithm. The statistical differences between the experiments obtained with the LA-rBOA, the IrBOA, and the mIDEA for functions F1-F5 are listed in the Table 3. Tables 2 and 3 show that in most uni-modal functions, the LA-rBOA clearly outperforms the IrBOA and the mIDEA.

Function F1 is shifted Sphere function, function F2 is shifted Schwefel's problem 1.2, and the function F3 is shifted rotated high conditioned elliptic function. These three functions have different conditions which make F3 to be harder than F2 and F2 to be harder than F1. From the results, we could conclude that LA-rBOA outperforms on the two other algorithms for functions F1 and F2. Also, in function F3, a better result is achieved for the LA-rBOA. Function F4 is shifted Schwefel's problem 1.2 with noise in fitness. Noise in the fitness disturbs the search process. From the results, we observe that the mIDEA and IrBOA are

Table 2 Numerical results for the LA-rBOA, the IrBOA and the mIDEA

| Function | LA-Rboa |  | IrBOA |  | mIDEA |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | Mean | Std | Mean | Std | Mean | Std |
| F1 | $\mathbf{3 . 7 0 e - 1 2}$ | $2.50 \mathrm{e}-11$ | $9.53 \mathrm{e}-10$ | $4.63 \mathrm{e}-10$ | $9.47 \mathrm{e}-9$ | $4.45 \mathrm{e}-9$ |
| F2 | $\mathbf{6 . 3 4 e - 1 1}$ | $5.74 \mathrm{e}-11$ | $6.94 \mathrm{e}-10$ | $1.49 \mathrm{e}-10$ | $9.85 \mathrm{e}-9$ | $1.53 \mathrm{e}-10$ |
| F3 | $\mathbf{2 . 9 6 e - 3 0}$ | $2.82 \mathrm{e}-36$ | $11.0 \mathrm{e}-30$ | $42.01 \mathrm{e}-23$ | $6.87 \mathrm{e}-25$ | $1.40 \mathrm{e}-19$ |
| F4 | $5.52 \mathrm{e}+0$ | $0.80 \mathrm{e}+0$ | $\mathbf{8 . 1 3 e - 7}$ | $1.74 \mathrm{e}-6$ | $1.11 \mathrm{e}-3$ | $4.35 \mathrm{e}-5$ |
| F5 | $\mathbf{5 . 7 1 e - 8}$ | $5.42 \mathrm{e}-11$ | $13.00 \mathrm{e}-2$ | $0.05 \mathrm{e}+0$ | $1.40 \mathrm{e}-1$ | $4.35 \mathrm{e}-2$ |

Table 3 The results of statistical test for the LA-rBOA, the IrBOA and the mIDEA

| Function | IrBOA | mIDEA |
| :-- | :-- | :-- |
| F1 | $\mathbf{- 1 . 1 0 e + 1 1}$ | $\mathbf{- 1 . 2 0 e + 1 0}$ |
| F2 | $\mathbf{- 6 . 1 8 e + 1 1}$ | $\mathbf{- 9 . 1 6 e + 1 2}$ |
| F3 | $\mathbf{- 1 . 1 4 e + 1 5}$ | $\mathbf{- 8 . 7 6 e + 1 4}$ |
| F4 | $2.16 \mathrm{e}+02$ | $2.16 \mathrm{e}+02$ |
| F5 | $\mathbf{- 1 . 3 0 e + 0 3}$ | $\mathbf{- 1 . 8 5 e + 0 3}$ |

superior to the LA-rBOA; because they use the selected solutions for building the Bayesian network directly; but we use them only in the learning rule of LAs to update $p(t)$; hence, for this function LA-rBOA obtains worse result. Function F5 is Schwefels problem 2.6 with global optimum on bounds. For this function, the proposed algorithm is superior to the IrBOA and the mIDEA.

Functions F5 through F25 are multi-modal functions. The results for functions F6-F25 are listed in Table 4. For each function the mean error value and the standard deviation of the obtained fitness values on the 50 independent runs are presented. Also, the statistical test between the experiments obtained with the LArBOA and two other algorithms for functions F6-F25 are shown in Table 5. Function F6 is shifted Rosenbrocks function, a problem between uni-modal and multi-modal function. For this function, the result for the LA-rBOA is better than the IrBOA and the mIDEA. Function F7 is shifted rotated Griewanks function without bounds, only the initialization range is given. Griewanks function is more difficult with low dimension and it is difficult to achieve the global optimum. The LA-rBOA obtains better result in comparison to the IrBOA and the mIDEA. Function F8 is shifted rotated Ackleys function with global optimum on bounds, which has a very narrow global basin and half of the dimensions of this basin are on the bounds. Hence, the search is almost like seeking a needle in a haystack. For this function, the results of the IrBOA and mIDEA are better than LA-rBOA. Functions F9 and F10 are shifted Rastrigins function and shifted rotated Rastrigins function, respectively. These two of functions have a huge number of local optima. The results demonstrate good performance of the LA-rBOA in comparison to the mIDEA and the IrBOA. Function F11 is shifted rotated Weierstrass function and Function F12 is Schwefels problem. For function F11 the mIDEA gets better

Table 4 Numerical results for the LA-rBOA, the IrBOA and the mIDEA

| Function | LA-rBOA |  | IrBOA |  | mIDEA |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Mean | Std | Mean | Std | Mean | Std |
| F6 | 4.37e-10 | $1.51 \mathrm{e}-10$ | $6.31 \mathrm{e}-9$ | $1.14 \mathrm{e}-9$ | $1.75 \mathrm{e}-1$ | $2.20 \mathrm{e}-1$ |
| F7 | 5.9e-11 | $1.74 \mathrm{e}-10$ | $6.48 \mathrm{e}-9$ | $1.46 \mathrm{e}-9$ | $1.50 \mathrm{e}-8$ | $1.15 \mathrm{e}-6$ |
| F8 | $1.98 \mathrm{e}+2$ | $0.10 \mathrm{e}-1$ | 2.00e+1 | $9.62 \mathrm{e}-5$ | $2.00 \mathrm{e}+1$ | $4.97 \mathrm{e}-4$ |
| F9 | 5.17e-7 | $2.56 \mathrm{e}-5$ | $8.25 \mathrm{e}-2$ | $1.43 \mathrm{e}+0$ | $2.79 \mathrm{e}+1$ | $4.56 \mathrm{e}-1$ |
| F10 | 1.57e-4 | $4.25 \mathrm{e}+0$ | $4.60 \mathrm{e}-1$ | $2.73 \mathrm{e}+0$ | $1.17 \mathrm{e}+2$ | $7.11 \mathrm{e}+1$ |
| F11 | $4.36 \mathrm{e}-3$ | $2.10 \mathrm{e}+0$ | $4.44 \mathrm{e}-1$ | $7.21 \mathrm{e}+0$ | 3.29e-3 | $3.65 \mathrm{e}+0$ |
| F12 | 7.64e-13 | $2.98 \mathrm{e}-10$ | $6.8 \mathrm{e}-11$ | $5.66 \mathrm{e}-8$ | $4.15 \mathrm{e}+1$ | $2.49 \mathrm{e}+1$ |
| F13 | 0.04e+0 | $0.34 \mathrm{e}-1$ | $0.54 \mathrm{e}+0$ | $0.98 \mathrm{e}-1$ | $0.52 \mathrm{e}+1$ | $1.32 \mathrm{e}+0$ |
| F14 | 0.98e+1 | $6.95 \mathrm{e}-1$ | $1.05 \mathrm{e}+1$ | $8.45 \mathrm{e}-1$ | $1.38 \mathrm{e}+1$ | $1.90 \mathrm{e}-1$ |
| F15 | $2.85 \mathrm{e}+2$ | $2.34 \mathrm{e}+1$ | 2.44e+2 | $2.12 \mathrm{e}+1$ | $8.76 \mathrm{e}+2$ | $1.95 \mathrm{e}+1$ |
| F16 | 0.14e+1 | $1.75 \mathrm{e}+1$ | $1.35 \mathrm{e}+1$ | $4.06 \mathrm{e}+1$ | $7.15 \mathrm{e}+1$ | $8.10 \mathrm{e}+1$ |
| F17 | $2.02 \mathrm{e}+2$ | $0.99 \mathrm{e}+1$ | $2.92 \mathrm{e}+3$ | $1.44 \mathrm{e}+2$ | 1.56e+2 | $1.58 \mathrm{e}+2$ |
| F18 | 5.36e+1 | $2.01 \mathrm{e}-2$ | $7.23 \mathrm{e}+1$ | $2.22 \mathrm{e}-2$ | $8.30 \mathrm{e}+2$ | $1.61 \mathrm{e}+0$ |
| F19 | $8.35 \mathrm{e}+2$ | $1.32 \mathrm{e}-1$ | $5.35 \mathrm{e}+3$ | $2.12 \mathrm{e}+0$ | 8.31e+2 | $1.47 \mathrm{e}+0$ |
| F20 | 5.12e+0 | $0.65 \mathrm{e}-1$ | $7.32 \mathrm{e}+0$ | $2.98 \mathrm{e}-1$ | $8.31 \mathrm{e}+2$ | $1.32 \mathrm{e}+0$ |
| F21 | $2.50 \mathrm{e}+2$ | $0.52 \mathrm{e}-14$ | 1.40e+2 | $1.11 \mathrm{e}-10$ | $1.59 \mathrm{e}+2$ | $5.44 \mathrm{e}-11$ |
| F22 | 7.45e+0 | $1.20 \mathrm{e}+1$ | $3.32 \mathrm{e}+1$ | $1.57 \mathrm{e}+1$ | $1.56 \mathrm{e}+3$ | $4.83 \mathrm{e}+2$ |
| F23 | 1.93e+1 | $1.04 \mathrm{e}-6$ | $2.44 \mathrm{e}+1$ | $5.42 \mathrm{e}-5$ | $8.66 \mathrm{e}+2$ | $8.07 \mathrm{e}-1$ |
| F24 | 1.03e+1 | $1.12 \mathrm{e}+2$ | $1.53 \mathrm{e}+1$ | $1.42 \mathrm{e}+2$ | $9.12 \mathrm{e}+2$ | $3.89 \mathrm{e}-1$ |
| F25 | 1.52e+1 | $9.21 \mathrm{e}-2$ | $2.43 \mathrm{e}+1$ | $3.26 \mathrm{e}-1$ | $2.13 \mathrm{e}+2$ | $5.50 \mathrm{e}-1$ |

solution in compare two other algorithms but for function F12 the LA-rBOA outperforms the IrBOA and the mIDEA. As mentioned before, our test suite contains uni-modal and multi-modal functions; so, according to the obtained results it is reasonable to say that the LA-rBOA presents evidences to perform better than the IrBOA and the mIDEA.

# 5.4 Comparison of the LA-rBOA with other population based algorithms 

In this section, we compare the performance of the LA-rBOA with some recently population based optimization algorithms: Bayesian network and Gaussian mixture model (BNGMM) [13], Variable sampling ant colony optimization algorithm (SamACO) [19], and self-adaptive global best harmony search (SGHS) [20]. BNGMM is an evolutionary continuous optimization algorithm based on Bayesian network and GMM for continuous optimization problem [13]. SamACO presents an extend version of ACO for solving continuous optimization problems. It focuses on the continuous variable sampling as a method to convert ACO from discrete optimization to continuous optimization [19]. Finally, in SGHS, a new improvisation scheme is proposed [20]. So, the good information captured in the current

Table 5 The results of statistical test for the LA-rBOA, the IrBOA and the mIDEA

| Function | IrBOA | mIDEA |
| :-- | :-- | :-- |
| F6 | $\mathbf{- 1 . 1 1 e + 1 1}$ | $\mathbf{- 9 . 0 4 e + 1}$ |
| F7 | $\mathbf{- 7 . 4 3 e + 1 0}$ | $\mathbf{- 2 . 8 2 e + 5}$ |
| F8 | $4.45 \mathrm{e}+7$ | $4.44 \mathrm{e}+7$ |
| F9 | $\mathbf{- 1 . 0 1 e + 0}$ | $\mathbf{- 3 . 3 5 e + 3}$ |
| F10 | $\mathbf{- 4 . 5 1 e - 1}$ | $\mathbf{- 5 . 7 7 e - 1}$ |
| F11 | $\mathbf{- 1 . 9 5 e - 1}$ | $1.51 \mathrm{e}-3$ |
| F12 | $\mathbf{- 5 . 2 5 e + 5}$ | $\mathbf{- 1 . 6 7 e + 0}$ |
| F13 | $\mathbf{- 1 . 1 6 e + 3}$ | $\mathbf{- 7 . 4 0 e + 1}$ |
| F14 | $\mathbf{- 1 . 4 6 e + 1}$ | $\mathbf{- 1 . 9 3 e + 2}$ |
| F15 | $1.03 \mathrm{e}+0$ | $\mathbf{- 1 . 5 9 e + 1}$ |
| F16 | $\mathbf{- 1 . 5 5 e - 1}$ | $\mathbf{- 2 . 5 5 e - 1}$ |
| F17 | $\mathbf{- 3 . 2 6 e + 0}$ | $4.59 \mathrm{e}-2$ |
| F18 | $\mathbf{- 5 . 2 1 e + 5}$ | $\mathbf{- 7 . 4 9 e + 3}$ |
| F19 | $\mathbf{- 2 . 5 0 e + 4}$ | $4.59 \mathrm{e}+1$ |
| F20 | $\mathbf{- 5 . 9 1 e + 2}$ | $\mathbf{- 1 . 1 8 e + 4}$ |
| F21 | $2.23 \mathrm{e}+23$ | $7.69 \mathrm{e}+23$ |
| F22 | $\mathbf{- 1 . 6 5 e + 0}$ | $\mathbf{- 1 . 6 6 e - 1}$ |
| F23 | $\mathbf{- 4 . 3 4 e + 0}$ | $\mathbf{- 3 . 2 5 e + 4}$ |
| F24 | $\mathbf{- 3 . 8 2 e - 3}$ | $\mathbf{- 1 . 8 0 e + 0}$ |
| F25 | $\mathbf{- 1 . 9 8 e + 3}$ | $\mathbf{- 1 . 5 9 e + 4}$ |

global best solution can be used to create new harmonies [20]. Table 6 shows the results of the LA-rBOA and the BNGMM for four chosen functions with $d=4$. The results of the BNGMM are borrowed from [13]. From the results it can be observed that the LA-rBOA outperforms the BNGMM in all of the used functions.

Table 7 shows the obtained results for functions F6-F10 with $d=30$ and in term of the mean error value and the standard deviation. The results of the SamACO of Table 7 are borrowed from [19]. The results show that the LA-rBOA outperforms the SamACO on the functions F6, F7 and F10.

For SGHS, the results of the mean error value and the standard deviation for five chosen function with $d=30$ are presented in Table 8. It should be mentioned that the results of the SGHS are borrowed from [20]. Based on these results, the LArBOA can obtain better results in most chosen functions because of using variable structures during the run of the algorithm.

# 5.5 The speed of convergence of LA-rBOA 

The comparison of the speed of convergence for eight chosen functions between the LA-rBOA and some related algorithms is presented in Fig. 3. Each sub-figure shows the obtained fitness value from three algorithms through the optimization process. For functions F3, F5, F9, and F10, the LA-rBOA converges faster than two other algorithms. For function F4 the mIDEA has a faster convergence rate based on

Table 6 Numerical results for the LA-rBOA and the BNGMM

Table 7 Numerical results for the LA-rBOA and the SamACO

| Function | LA-rBOA |  |  | BNGMM |
| :-- | :-- | :-- | :-- | :-- |
| F1 | $\mathbf{3 . 4 1 e - 5}$ |  | $1.7 \mathrm{e}-4$ |  |
| F2 | $\mathbf{3 . 7 6 e - 6}$ |  | $5.11 \mathrm{e}-5$ |  |
| F6 | $\mathbf{2 . 8 3 e - 9}$ |  | $3.43 \mathrm{e}-7$ |  |
| F7 | $\mathbf{1 . 1 1 e - 6}$ |  | $3.03 \mathrm{e}+0$ |  |


| Function | LA-rBOA |  | SamACO |  |
| :-- | :-- | :-- | :-- | :-- |
|  | Mean | Std | Mean | Std |
| F6 | $\mathbf{4 . 3 7 e - 1 0}$ | $1.51 \mathrm{e}-10$ | $1.26 \mathrm{e}+2$ | $2.94 \mathrm{e}+2$ |
| F7 | $\mathbf{5 . 9 e - 1 1}$ | $1.74 \mathrm{e}-10$ | $0.02 \mathrm{e}+0$ | $0.01 \mathrm{e}+0$ |
| F8 | $1.98 \mathrm{e}+2$ | $0.10 \mathrm{e}-1$ | $\mathbf{2 0 . 0 e + 0}$ | $4.3 \mathrm{e}-3$ |
| F9 | $5.17 \mathrm{e}-7$ | $2.56 \mathrm{e}-5$ | $\mathbf{1 . 5 9 e - 1 4}$ | $2.6 \mathrm{e}-14$ |
| F10 | $\mathbf{1 . 5 7 e - 4}$ | $4.25 \mathrm{e}+0$ | $270 \mathrm{e}+0$ | $86.9 \mathrm{e}+0$ |

Table 8 Numerical results for the LA-rBOA and the SGHS

| Function | LA-rBOA |  | SGHS |  |
| :-- | :-- | :-- | :-- | :-- |
|  | Mean | Std | Mean | Std |
| F1 | $3.70 \mathrm{e}-12$ | $2.50 \mathrm{e}-11$ | $\mathbf{0 e + 0}$ | $0 \mathrm{e}+0$ |
| F6 | $\mathbf{4 . 3 7 e - 1 0}$ | $1.51 \mathrm{e}-10$ | $21.21 \mathrm{e}+2$ | $39.66 \mathrm{e}-2$ |
| F7 | $\mathbf{5 . 9 e - 1 1}$ | $1.74 \mathrm{e}-10$ | $13.3 \mathrm{e}+1$ | $13.3 \mathrm{e}+0$ |
| F9 | $\mathbf{5 . 1 7 e - 7}$ | $2.56 \mathrm{e}-5$ | $1.86 \mathrm{e}+0$ | $0.3 \mathrm{e}+0$ |
| F10 | $\mathbf{1 . 5 7 e - 4}$ | $4.25 \mathrm{e}+0$ | $98.7 \mathrm{e}+0$ | $3.0 \mathrm{e}+1$ |

Fig. 3b. Also, for function F6, IrBOA has a faster convergence rate. It can be seen from Fig. 3, the LA-rBOA has much faster convergence rate in comparison to the two other algorithms in most of the used test functions. From the results, we can conclude that in most of the test functions the LA-rBOA has faster convergence rate; but in some of them such as function F4 and F6, the LA-rBOA has slower convergence rate. The reason of the slower convergence rate is that the LA-rBOA uses the promising solutions only in the LA learning rule. So, in some of these functions such as function F4 that has noise in fitness, the used LAs converge later than the functions that do not have noise.

# 5.6 The computation time of LA-rBOA 

The LA-rBOA is also compared based on the computation time with the IrBOA and the mIDEA. These algorithms are implemented in MATLAB R2009a in a PC, which has a single CPU of Intel(R) Core(TM)2 Duo 3.33 GHz and a 1 GB memory. Table 9 shows the computation time for three algorithms over 50 independent runs

![img-2.jpeg](img-2.jpeg)

Fig. 3 The speed of convergence for the LA-rBOA, the IrBOA and the mIDEA. a Function F3. b Function F4. c Function F5. d Function F6. e Function F9. f Function F10

Table 9 Computation time (s) comparison

|  | F7 | F8 | F9 | F10 | F11 | F12 | F13 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LA-rBOA | $\mathbf{2 3 . 4 0}$ | $\mathbf{2 1 . 1 4}$ | $\mathbf{2 5 . 5 2}$ | $\mathbf{8 8 . 4 1}$ | $\mathbf{6 8 . 3 0}$ | $\mathbf{7 8 . 1 2}$ | $\mathbf{6 0 . 1 9}$ |
| IrBOA | 60.54 | 55.62 | 71.33 | 99.32 | 84.58 | 80.32 | 98.54 |
| mIDEA | 51.39 | 48.54 | 67.43 | 90.43 | 83.45 | 82.45 | 83.43 |

for seven chosen functions (F7 through F13) from the CEC2005 test suite. It can be seen that the LA-rBOA requires a smaller computation time among two other algorithms. Also, in order to show the relationship between dimensionality and scalability of the LA-rBOA, the computation time of three algorithms for functions

![img-3.jpeg](img-3.jpeg)

Fig. 4 The comparison of computation time with respect to different dimensionality. a Function F7. b Function $F 8$

F7 and F8 are compared in Fig. 4. The dimension of each function is changed from 1 through 120. Based on these figures, it can be seen that the LA-rBOA has very smaller increasing rate than two other algorithms. In Fig. 4a, the LA-rBOA saves about $73 \%$ of the computation time for function F7 in all of dimensions in comparison to the IrBOA and about $59.99 \%$ in comparison to the mIDEA. In Fig. 4b, it can be seen that the LA-rBOA saves more computation time with increasing the dimensionality. For example in dimension 50, it saves $69.3 \%$ of computation time in comparison to the IrBOA and $47.6 \%$ in comparison to the mIDEA; but in dimension 120, it saves $83 \%$ in computation time in comparison to the IrBOA and $62.5 \%$ in comparison to the mIDEA. This may be due to the learning capability of learning automata, it also shows that the network evolves through time and a small modification of the previously learned networks can be used for the future generations.

# 5.7 Comparison of the LA-rBOA on the CEC2011 test functions 

In this section, we compare the performance of the proposed algorithm with the performance some of the best algorithms submitted on IEEE CEC2011 competition on the CEC2011 test functions. For a fair comparison of the LA-rBOA, we evaluate the LA-rBOA with $\operatorname{Max}_{\mathrm{NFC}}=150,000$ to the best algorithms submitted in IEEE CEC2011 on the CEC2011 test functions. Table 10 presents the comparison of the LA-rBOA with the results of the best six algorithms on the 50 independent runs. These results are borrowed from the Ref. [44]. The comparison is done based on the fitness value obtained from the LA-rBOA and the other optimization algorithms. The results show that the LA-rBOA outperforms on T01, T03, T04, T06, T07, T08, T10, T11.3, T11.7, T12.

This table shows that no algorithm outperforms other ones in all functions, but the proposed algorithm has a better result for ten functions out of 22 mentioned functions. Hence, it can be concluded that the proposed algorithm has a better results with respect to other algorithms given in this table.

![img-4.jpeg](img-4.jpeg)

# 6 Conclusion 

This paper presents a new real-coded Bayesian optimization algorithm which uses a team of learning automata to construct the Bayesian network. For each possible edge in the Bayesian network, there is one learning automaton and each learning automaton tries to learn the existence or not existence of the corresponding edge. In each generation, one Bayesian network is constructed based on the action of learning automata. The next generation is sampled from the built Bayesian network and each learning automaton updates its action probability based on the quality of the built Bayesian network. The experimental results reported here show that the proposed algorithm is superior to other related algorithms based on the quality and performance measures. The proposed algorithm has two main features: (1) it builds better networks. This may be due to the learning capability of learning automata and it also shows that the network evolves through time and a small modification of the previously learned networks can be used for future generations. (2) Learning automata have a negligible computational cost for construction of the network, but it improves the quality of the network. In future works, we are trying the use learning automata as an optimization tool. We are trying to design an algorithm based learning automata for optimization and study to its behavior analytically.

Acknowledgments The authors would like to thank reviewers for their time, comments and constructive criticism, which improved the paper.

## References

1. D.E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning (Addison-Wesley, Reading, 1989)
2. D.E. Goldberg, K. Sastry, Genetic Algorithms: The Design of Innovation, 2nd edn. (Springer, Berlin, 2002)
3. J.A. Lozano, P. Larranaga, I. Inza, E. Bengoetxea (eds.), Towards a New Evolutionary Computation: Advances on Estimation of Distribution Algorithms (Springer, Berlin, 2006)
4. M. Pelikan, K. Sastry, E. Cantu-Paz (eds.), Scalable Optimization Via Probabilistic Modeling: From Algorithms to Applications (Springer, Berlin, 2006)
5. M. Pelikan, Bayesian Optimization Algorithm: From Single Level to Hierarchy, Ph.D. Dissertation (University of Illinois at Urbana-Champaign, Urbana, 2002)
6. G. Harik, Linkage Learning in Via Probabilistic Modeling in the ECGA (University of Illinois at Urbana-Champaign, Urbana, 1999)
7. H. Muhlenbein, T. Mahnig, FDA-a scalable evolutionary algorithm for the optimization of additively decomposed functions. Evol. Comput. 7(4), 353-376 (1999)
8. M. Pelikan, BOA: The Bayesian Optimization Algorithm (Springer, Berlin, 2005)
9. P. Larranaga, R. Etxeberria, J.A. Lozano, J.M. Pena, Proceedings of the 2000 Genetic and Evolutionary Computation Conference Workshop Program. Optimization in continuous domains by learning and simulation of Gaussian networks (2000), pp. 201-204
10. J. Ocenasek, J. Schwarz, in Proceedings of the 2nd Euro-International Symposium on Computational Intelligence. Estimation of distribution algorithm for mixed continuous discrete optimization problems (2002), pp. 227-232
11. P.A.N. Bosman, Design and Application of Iterated Density-Estimation Evolutionary Algorithms, Ph.D. Dissertation (Utrecht University, Utrecht, 2003)
12. C.W. Ahn, R.S. Ramakrishna, D.E. Goldberg, Real-Coded Bayesian Optimization Algorithm: Bringing the Strength of BOA into the Continuous World, Lecture Notes in Computer Science, vol. 3102 (Springer, Berlin, 2004), pp. 840-851

13. X. Wei, In Proceedings of the IEEE 10th International Conference of Signal Processing (ICSP). Evolutionary continuous optimization by Bayesian networks and Gaussian mixture model (2010), pp. $1437-1440$
14. B. Moradabadi, H. Beigy, C.W. Ahn, In Proceedings of IEEE Congress on Evolutionary Algorithm. An improved real-coded Bayesian optimization algorithm (2011)
15. B. Moradabadi, H. Beigy, C.W. Ahn, An improved real-coded Bayesian optimization algorithm for continuous global optimization. Int. J. Innov. Comput. Inf. Control 9(6), 2505-2519 (2013)
16. M.A.L. Thathachar, P.S. Sastry, Varieties of learning automata: an overview. IEEE Trans. Syst. Man Cybern. B Cybern. 32, 711-722 (2002)
17. D.M. Chickering, D. Geiger, D. Heckerman, Learning Bayesian Network is NP-hard, Technical Report MSR-TR-94-17 (1994)
18. D. Heckerman, D. Geiger, D.M. Chickering, A Tutorial on Learning with Bayesian Networks, Innovations in Bayesian Networks, Chapter 3 (Springer, Berlin, 2008), pp. 33-82
19. X.M. Hu, J. Zhang, H. Chung, Y. Li, O. Liu, Sam-ACO: variable sampling ant colony optimization algorithm. IEEE Trans. Syst. Man Cybern. B Cybern. 40, 1555-1566 (2010)
20. Q. Pan, P.N. Suganthan, M.F. Tasgetiren, J.J. Liang, A self-adaptive global best harmony search algorithm for continuous. Appl. Math. Comput. 216, 830-848 (2010)
21. M. Gallagher, I. Wood, J. Keith, In Proceedings of the IEEE Congress on Evolutionary Computation. Bayesian inference in estimation of distribution algorithms (2007), pp. 127-133
22. M. Li, D.E. Goldberg, K. Sastry, T.L. Yu, Real-coded ECGA for solving decomposable real-valued optimization problems. Link. Evol. Comput. 157, 61-86 (2008)
23. C.W. Ahn, R.S. Ramakrishna, On the scalability of real-coded Bayesian optimization algorithm. IEEE Trans. Evol. Comput. 12(3), 307-322 (2008)
24. D. Heckerman, D. Geiger, D.M. Chickering, Learning Bayesian Networks: The Combination of Knowledge and Statistical Data, Technical Report MSR-TR-94-09 (Microsoft Research, Redmond, 1995)
25. C.W. Ahn, Advances in Evolutionary Algorithms: Theory, Design and Practice, Studies in Computational Intelligence (Springer, Berlin, 2006)
26. H. Beigy, M.R. Meybodi, A new continuous action-set learning automata for function optimization. J. Franklin Inst. 343, 27 (2006)
27. G. Santharam, P.S. Sastry, M.A.L. Thathachar, Continuous action set learning automata for stochastic optimization. J. Franklin Inst. 331B(5), 607-628 (1994)
28. B.J. Oommen, T.D. Roberts, Continuous learning automata solutions to the capacity assignment problem. IEEE Trans. Comput. 49, 608-620 (2000)
29. M.S. Obaidat, G.I. Papadimitriou, A.S. Pomportsis, H.S. Laskaridis, Learning automata-based bus arbitration for shared-medium ATM switches. IEEE Trans. Syst. Man Cybern. B Cybern. 32, $815-820(2002)$
30. G.I. Papadimitriou, M.S. Obaidat, A.S. Pomportsis, On the use of learning automata in the control of broad-cast networks: a methodology. IEEE Trans. Syst. Man Cybern. B Cybern. 32, 781-790 (2002)
31. H. Beigy, M.R. Meybodi, Cellular learning automata based dynamic channel assignment algorithms. Int. J. Comput. Intell. Appl. 8(3), 287-314 (2009)
32. H. Beigy, M.R. Meybodi, Utilizing distributed learning automata to solve stochastic shortest path problems. Int. J. Uncertain Fuzz Knowl. Based Syst. 14, 591-615 (2006)
33. O.C. Granmo, B.J. Oommen, S.A. Myrer, M.G. Olsen, Learning automata-based solutions to the nonlinear fractional knapsack problem with applications to optimal resource allocation. IEEE Trans. Syst. Man Cybern. B Cybern. 37, 166-175 (2007)
34. H. Beigy, M.R. Meybodi, Adaptive limited fractional guard channel algorithms a learning automata approach. Int. J. Uncertain. Fuzziness Knowl. Based Syst. 17(6), 881-913 (2009)
35. H. Beigy, M.R. Meybodi, A learning automata-based algorithm for determination of the number of hidden units for three layer neural networks. Int. J. Syst. Sci. 40, 101-118 (2009)
36. P.S. Sastry, G.D. Nagendra, N. Manwani, A team of continuous-action learning automata for noisetolerant learning of half-spaces. IEEE Trans. Syst. Man Cybern. B Cybern. 40, 19-28 (2010)
37. H. Beigy, M.R. Meybodi, Learning automata based dynamic guard channel algorithms. J. Comput. Electr. Eng. 37(4), 601-613 (2011)
38. B.J. Oommen, M.K. Hashem, Modeling a student classroom interaction in a tutorial-like system using learning automata. IEEE Trans. Syst. Man Cybern. B Cybern. 40, 29-42 (2010)
39. S. Narendra, K.S. Thathachar, Learning Automata: An Introduction (Prentice-Hall, New York, 1989)
40. K.R. Zälik, An efficient k'-means clustering algorithm. Pattern Recogn. Lett. 29, 1385-1391 (2008)

41. Function definitions and performance criteria for the special session on real-parameter optimization at CEC2005 (2005). http://www.ntu.edu.sg/home/EPNSugan. Accessed Apr 2013
42. Problem Definitions and Evaluation Criteria for CEC 2011 Competition on Testing Evolutionary Algorithms on Real World Optimization Problems. http://www.ntu.edu.sg/home/EPNSugan. Accessed Apr 2013
43. D.H. Wolpert, W.G. Macready, No free lunch theorems for search. IEEE Trans. Evol. Comput. 5(3), 295-296 (1997)
44. Competition on Testing Evolutionary Algorithms on Real-world Numerical Optimization Problems. http://www.ntu.edu.sg/home/EPNSugan. Accessed Apr 2013