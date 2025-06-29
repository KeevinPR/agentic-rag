# Efficient Resource Minimization Scheme for Network Coding-Assisted Multicast System 

Seyed Amin Hejazi, M. Naeem and D. C. Lee ${ }^{1}$, Senior Member, IEEE


#### Abstract

In this paper, we consider the problem of minimizing the resources used for network coding (MRUNC) while achieving the desired throughput in a multicast system. The problem of minimizing the number of network coding links is NP-hard. In this paper we propose a low- complexity Estimation of Distribution Algorithm (EDA) for MRUNC. Our EDA is applicable to the network with and without cycles. The numerical results show the effectiveness of the proposed method over previously proposed algorithms.


Index Terms:- Estimation of Distribution Algorithm (EDA), Network Coding, Max-Flow.

## I. INTRODUCTION

THE main challenge in communication networks can be summarized as increasing the throughput of information transmission while minimizing the cost of the system. The network topology and link capacities limit the throughput of information flow within a data network. Recently, network coding [1][2] has been receiving much attention as an interesting way of increasing the throughput. Furthermore, network coding has been successfully applied to computer networks [3], wireless sensor networks [3], and peer-to-peer systems [4].

The basic idea of network coding is well presented in the seminal paper by Ahlswede, et. al. [1]. It has been shown that the throughput of the information flow from the source to sinks in the multicast system can be improved by intermediate nodes' activity of encoding the outgoing messages on the basis of the incoming messages. In [5], Li et al. further showed that linear network coding is sufficient to achieve the optimal throughput in the multicast system.

A classic example that illustrates the power of network coding is shown in Fig. 1, where each link has unit capacity. The achievable throughput in multicasting from source $s$ to sinks d 1 and d 2 in the network A of Fig. 1, with network coding, is 2. Fig. 1 illustrates that node $a$ in network A encodes the message that is transmitted from node $a$ to node $b$ through linear operation $\alpha+\beta$. Fig. 1 also illustrates that sink d1 can obtain both messages $\alpha$ and $\beta$ by performing linear operations from messages $\alpha$ and $\alpha+\beta$, which come through links $(m, d 1)$ and $(b, d 1)$, respectively.

[^0]Similarly, sink $d 2$ can obtain both messages $\alpha$ and $\beta$ by performing linear operations from message $\beta$, which comes through link ( $n, d 2$ ) and message $\alpha+\beta$, which comes through link ( $b, d 2$ ). Each of nodes d 1 and d 2 can obtain both messages $\alpha$ and $\beta$, so the throughput can be 2 per unit message transmission time. It turns out that network A cannot achieve multicast throughput 2 without network coding. It has been proven in [1] that multicast throughput of $h$ can be achieved from source $s$ to sinks $d 1, d 2 \ldots d l$ if

$$
h=\min _{s} \max _{\text {max }} \text { flow }(s, d l)
$$

where max_flow $(s, d l)$ denotes the maximum flow from node $s$ to $d l$ in the graph. However, this statement does not prescribe which links should employ network coding, like link $(a, b)$ in Fig. 1. For the purpose of reducing cost and complexity, it is desired to achieve a specified multicast throughput with as small number of coding links as possible. It is computationally complex to determine a minimal set of nodes where coding is required. It can be shown that the problem of minimizing the number of coding links to achieve a specified thorughput is $N P$-hard [6].
![img-0.jpeg](img-0.jpeg)

Fig. 1. Sample Networks
There are heuristic algorithms that try to find a small set of coding links that achieve a specified multicast rate toward the goal of minimizing the number of coding links [7][8][9][10]. Among these, the genetic algorithms presented by Kim et al. in [9] [10] appear to perform the best in terms of the number of coding links. Genetic algorithms are heuristic in nature, so they find a suboptimal solution.

In the present paper, we propose another evolutionary algorithm, Estimation-of-Distribution algorithm (EDA), for finding a small set of coding links that achieve the specified multicast throughput. EDA creates a new population from the probability distribution estimated from previous generations instead of string manipulation [13] of GA. No significant parameter tuning is required for EDA as compared to other Evolutionary Algorithms (EAs). Our experiments with EDA show that the number of coding links is significantly reduced compared to the aforementioned methods. Moreover, the optimal solution is derived much faster and within a smaller number of iterations.


[^0]:    ${ }^{1}$ The authors are with the School of Engineering Science at Simon Fraser University, Burnaby, BC V5A 1S6 Canada. (e-mail:shejazi@sfu.ca; mnaeem@sfu.ca; dchlee@sfu.ca).

## II. Problem Formulation

As in [9-10], we model the network by a directed multigraph $G=(V, E)$, where each link has a unit capacity and connections with larger capacities are represented by multiple unit capacity links [2]. Only integer flows are allowed, so for our network, there is either no flow or a unit rate of flow on each link. This formulation enables the graph decomposition method [10] to facilitate the optimization formulation. Modeling a network by a direct multi-graph with unit-capacity links is not too restrictive if the link capacities are discrete. We consider a single source multicast scenario in which a single source $s \in V$ wishes to transmit data at given rate $R$ to a set $T \subset V$ of receiver nodes (sinks), where $|T|=d$. The rate $R$ is said to be achievable if there exists a network coding scheme that enables all $d$ sinks to receive the information correctly. Our optimization problem is to find a minimal set of coding links that achieve multicast rate $R$. We only consider linear coding because linear coding is sufficient for minimizing the number of coding links to achieve a specified multicast throughput [5]. For network coding, we do not need to consider outgoing links from a node that has less than two incoming links. Such outgoing links cannot perform a linear operation on different messages coming through different incoming links. For coding links, we only need to consider outgoing links from the nodes with multiple incoming links. We refer to a node with multiple incoming links as a merging node.

Now, we define our optimization variables and the objective function. For each merging node with $d_{r n}>1$ incoming links and $d_{\text {out }}>0$ outgoing links, we define a binary variable $a_{i j}$ to each pair of the $i \in\left\{1, \ldots, d_{r n}\right\}$-th incoming link and the $j \in\left\{1, \ldots, d_{\text {out }}\right\}$-th outgoing link. $a_{i j}=1$ indicates that the messages from incoming link $i$ contribute to the linearly coded output message forwarded through outgoing link $j$. $a_{i j}=0$ indicates that the messages from incoming link $i$ are not considered in encoding a message to be forwarded through outgoing link $j$. For the $j$ th outgoing link, we refer to the set of associated binary variables $a_{j}=\left(a_{i j}\right)_{i \in\left\{1, \ldots, d_{r n}\right\}}$ (block) as a coding vector (Fig. 2). Network coding is required over link $j$ if $\left\|a_{j}\right\|_{0}=\sum_{i \in\left\{1, \ldots, d_{r n}\right\}} a_{i j} \geq 2$. Our optimization problem is:
$\min \sum_{j \in \hat{E}} q_{j}\left(a_{j}\right)$
SUBJECT TO: transmit data at given rate $R$ to $d$ receiver nodes where

$$
q_{j}\left(a_{j}\right)=\left\{\begin{array}{ll}
1, & \text { if }\left\|a_{j}\right\| \geq 2 \\
0, & \text { otherwise }
\end{array}\right.
$$

and $\hat{E}$ denotes the set of links that are outgoing from a merging node.

## III. A BRIEF InTRODUCTION to EDA

Evolutionary algorithms have been often used to solve difficult optimization problems. Candidate solutions to an optimization problem are represented as individuals in the population. In EAs the cost function value of a candidate solution to the optimization problem indicates the fitness of the individual in the concept of natural selection [11]. Unlike other evolutionary algorithms, in EDA a new population of
individuals in each iteration is generated without crossover and mutation operators. Instead, in EDA a new population is generated based on a probability distribution, which is estimated from the best selected individuals of previous iteration [12].
In general, conventional EDAs can be characterized by parameters and notations $\left(I_{s}, F, \Delta_{l}, \eta_{l}, \beta_{l}, p_{l}, \Gamma, I_{T o r}\right)[13]$ where

1. $I_{s}$ is the space of all potential solutions (entire search space of individuals).
2. $F$ denotes a fitness function.
3. $\Delta_{l}$ is the set of individuals (population) at the $l_{\text {th }}$ iteration.
4. $\eta_{l}$ is the set of best candidate solutions selected from set $\Delta_{t}$ at the $l_{\text {th }}$ iteration.
5. We denote $\beta_{l} \equiv \Delta_{l}-\eta_{l} \equiv \Delta_{l} \cap \eta_{l}^{\prime}$. where $\eta_{l}^{\prime}$ is the complement of $\eta_{l}$.
6. $p_{l}$ is the selection probability. The EDA algorithm selects $p_{l}\left|\Delta_{l}\right|$ individuals from set $\Delta_{t}$ to make up set $\eta_{l}$.
7. We denote by $\Gamma$ the distribution estimated from $\eta_{l}$ (the set of selected candidate solutions) at each iteration
8. $I_{T o r}$ are the maximum number of iteration

In conventional EDAs, each individual is designated by a binary string of length $n$ ( $n$-dimensional binary vector). We denote $X=\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ as an individual by a binary row vector, $x_{i} \in\{0,1\}$. An EDA maintains a population of individuals in each iteration. We denote the number of individuals in population by $\left|\Delta_{l}\right|$. Population $\Delta_{l}$ can be specified by the following matrix:

$$
X=\left(\begin{array}{c}
X^{1} \\
X^{2} \\
\vdots \\
X^{\left|\lambda_{1}\right|}
\end{array}\right)=\left(\begin{array}{cccccc}
x_{1}^{1} & x_{2}^{1} & \vdots & x_{n}^{1} \\
x_{1}^{2} & x_{2}^{2} & \vdots & x_{n}^{2} \\
\cdots & \cdots & \cdots & \cdots \\
x_{1}^{\left|\lambda_{1}\right|} & x_{2}^{\left|\lambda_{2}\right|} & \vdots & x_{n}^{\left|\lambda_{n}\right|}
\end{array}\right)
$$

where superscript $j$ in the row vector $X^{j}=\left(x_{1}^{j}, x_{2}^{j}, x_{3}^{j}, \ldots, x_{n}^{j}\right)$ indexes an individual in the population. A typical EDA is described in the following steps:

Step 0: Generate initial population $\Delta_{0}$. The initial population ( $\left|\Delta_{0}\right|$ individuals) is typically obtained by sampling according the uniform (equally likely) distribution [12]:

$$
\begin{aligned}
& p\left(\theta_{1}, \theta_{2}, \cdots, \theta_{n}\right)=\prod_{i} p_{i}\left(\theta_{i}\right) \\
& \quad \forall i=1,2, \ldots, n, \text { and } p_{i}\left(\theta_{i}=1\right)=p_{i}\left(\theta_{i}=0\right)=0.5
\end{aligned}
$$

For iterations $l=1,2, \ldots$, follow steps 1 through 6
Step 1: Evaluate the individuals in the current population $\Delta_{l-1}$ according to the fitness function $F$. Sort the candidate solutions (individuals in the current population) according to their fitness orders.

Step 2: If the best candidate solution satisfies the convergence criterion or the number of iterations exceeds its limit $I_{T o r}$, then terminate; else go to step 3.

[^0]
[^0]:    2 In conventional EDAs, the joint probability distribution from which the initial population is sampled is a product of ' $n$ ' univariate marginal probability distributions, each following a Bernoulli distribution with parameter value equal to 0.5 . Later in this paper, we present different methods of generating the initial population).

Step 3: Select the best $p_{i} \Delta_{i-1}$ candidate solutions (individuals) from current population $\Delta_{i-1}$. This selection is accomplished according to the sorted candidate solutions.

Step 4: Estimate the probability distribution $p\left(\theta_{1}, \theta_{2}, \cdots, \theta_{n}\right)$ on the basis of $\left|\eta_{i-1}\right|$ best candidate solutions. We denote this estimation by

$$
\Gamma=P\left(\theta_{1}, \theta_{2}, \cdots, \theta_{n} \mid \eta_{i-1}\right)
$$

Step 5: Generate new $\left|\Delta_{i-1}\right|-\left|\eta_{i-1}\right|$ individuals on the basis of this new estimated probability distribution $\Gamma$. Replace the bad $\left|\beta_{i-1}\right|$ individuals with newly generated $\left|\Delta_{i-1}\right|-\left|\eta_{i-1}\right|$ individuals.

Step 6: Go to step 1 and repeat the steps
We followed the steps of the above pseudo code for our EDA implementation problem. In our experimentation, for estimation (5), we used a simple scheme of estimating the marginal distributions separately and using product form

$$
\begin{aligned}
& \Gamma=p\left(\theta_{1}, \theta_{2}, \cdots, \theta_{n} \mid \eta_{i-1}\right)=\prod_{i=1}^{n} p_{i}\left(\theta_{i} \mid \eta_{i-1}\right) \\
& \quad=\prod_{i=1}^{n}\left(\frac{\sum_{j=1}^{m-1} \delta\left(x_{i}^{j}=\theta_{i} \mid \eta_{i-1}\right)}{\left|\eta_{i-1}\right|}\right)
\end{aligned}
$$

where $\delta$ is an indicator function and it can be expressed as

$$
\delta\left(x_{i}^{j}=\theta \mid \eta_{i-1}\right)=\left\{\begin{array}{l}
1 \text { if } x_{i}^{j}=\theta \\
0 \text { otherwise }
\end{array}\right.
$$

Even with this simple application of EDA, the simulation results show that the performance of EDA is better than previously proposed algorithms. In addition, we were able to modify this basic EDA algorithm and even further improve the algorithm's performance.

## IV. COMPONENTS OF EDA FOR OUR PROBLEM

## A. Individual Representation

Each individual (a candidate solution) is represented by acollection of binary vectors (strings) $\left\{a_{j} \mid J \in \bar{E}\right\}$. Forexample, if we have just two merging nodes $v 1$ and $v 2$ in the network, we can represent an individual as shown in Fig. 2. Vector (or binary string) $a_{j}$ indicates whether outgoing link $J$ is allowed to code.

## B. Fitness Function and Constraint Check

It is natural to use the objective function in optimization problem (2) as the fitness function of our EDA. If a candidate solution (an individual in EDA) does not satisfy the constraint in (2), we disregard that candidate as a valid solution and replace it with a feasible candidate, as will be explained in the following sections. We now discuss how to check if a candidate solution $\left\{a_{j} \mid J \in \bar{E}\right\}$ satisfies the constraint.

Note that the maximum achievable multicast rate is (1) if all links are allowed to be a coding link. However, this statement does not say what the achievable multicast rate is if we prevent a particular set of links from being a coding link. A candidate solution $\left\{a_{j} \mid J \in \bar{E}\right\}$ precludes every link $J$ with property $\llbracket a_{j} \rrbracket<2$ from coding. In order to examine the achievability of a specified multicast rate for a particular
![img-1.jpeg](img-1.jpeg)

Fig.2. represent blocks of individuals for nodes $v 1$ and $v 2$ Final Stage candidate solution $\left\{a_{j} \mid J \in \bar{E}\right\}$, we can construct a new graph on the basis of multigraph $G=(V, E)$ and candidate solution $\left\{a_{j} \mid J \in \bar{E}\right\}$ and then run max-flow from the source to each sink.
This new graph is constructed by decomposition of each merging node that is not a sink as follows:

Let us now decompose each merging node as follows to interpret network coding in the graph theoretic framework. Consider a node $v$ with $d_{i n}(\geq 2)$ incoming links $\left({ }^{d_{1}}, \cdots, d_{d_{m}}\right)$ and $d_{\text {out }}$ outgoing links $\left({ }^{b_{1}}, \ldots, b_{\text {dout }}\right)$. Let us first decompose the node by introducing $d_{i n}$ incoming auxiliary nodes $\left({ }^{k_{1}}, \ldots, k_{d_{i n}}\right)$ and redirect node $v$ 's $d_{i n}$ incoming links to each of the incoming auxiliary nodes (see Fig. 3). Similarly, we create $d_{\text {out }}$ outgoing auxiliary nodes $\left(h_{1}, \ldots, h_{\text {dout }}\right)$ and let node $v$ 's $d_{\text {out }}$ outgoing links to be the only outgoing links of each of the outgoing auxiliary nodes. We then introduce a link between each pair of incoming and outgoing auxiliary nodes [10].

Then, there is a one-to-one correspondence between the set of binary variables in coding vectors and the set of the introduced links between auxiliary nodes [10]. Fig. 3 shows this correspondence for node $v 1$ in Fig. 2.

After the decomposing procedure, we test the feasibility of the individual as following:, 1) deleting first, all the introduced links between auxiliary nodes associated with 0 in the Individual and 2) then calculating the max-flow between the source and each of the $d$ sinks [10]. Note that by using decomposition method, all the outgoing auxiliary nodes with more than one input are considered as coding nodes. Having this, it's possible to get the maximum achievable multicast rate by finding the minimum of the individual max flow bounds between source and each of the links
If an outgoing auxiliary node has only one incoming link, we can delete that node and connect directly its incoming link

to its outgoing link without changing any of the max-flows. We also delete an auxiliary node which has no incoming link. If all $d$ max-flows are at least $R$, rate $R$ is achievable. We can calculate the fitness value (number of coding links) for each candidate by counting the number of remaining outgoing auxiliary nodes [10].
![img-2.jpeg](img-2.jpeg)

Fig.3. Decomposition of node $v i$ in Fig. 2 with $d_{i u}=3$ and $d_{\text {out }}=2$.

## V. IMPROVEMENTS TO EDA

In this section, we discuss improvements we made to EDA for optimization problem (2). We discuss generating the initial population for problem (2) and then other two novel elements designed specifically for the problem.

## A. Generating the Initial Population

The initial population is typically constructed randomly such that each component of the individual is assigned 0 or 1 with equal probabilities. Note, however, that the size of the population in EDA is usually much smaller than the size of the entire search space, and thus it is quite likely that randomly generated initial population may contain no feasible solution or very small number of feasible solutions. Our method of dealing with this problem is to include in the initial population many individuals that calls for many coding links. We make sure that some portions (e.g., $x \%$ ) of the initial population consist of individuals $\left\{a_{j} \mid J \in \bar{E}\right\}$ such that the number of vector components in $\left\{a_{j} \mid J \in \bar{E}\right\}$ with value 1 exceeds some fraction (e.g., $y \%$ ) of the total number of vector components. For sufficiently high percentages $x$ and $y$, the initial population can include many feasible solutions, although their fitness values may not be good. Significant performance improvement was shown in EDA after employing this method.

## B. Block-Wise-Modified Representation and Operators

Note that each candidate solution to optimization problem (2) is represented by a collection of binary vectors (strings) $\left\{a_{j} \mid J \in \bar{E}\right\}$. We denote the dimension of vector $a_{j}, j \in \bar{E}$ by $k_{j}$ Then, the search space for optimization (2) is $\prod_{j \in \bar{E}} 2^{k_{j}}$, including the infeasible candidates. However, we can reduce this search space. For an arbitrary link $J \in \bar{E}$, as long as $\left\|a_{j}\right\|_{1} \geq 2$, then link $J$ contributes 1 to the cost function in (2) as a coding link. Among all strings with property $\left\|a_{j}\right\|_{1} \geq 2$, the string of all 1's achieves the highest max-flow (1) in the graph constructed by decomposition described in section IV.B. Therefore, for the purpose of optimization (2), we only need to consider the string of all 1's
in place of considering all strings with property $\left\|a_{j}\right\|_{1} \geq 2$. Similarly, the string of all 0 's and a string having only one element of value 1 , both contribute none to the cost function of (2), but the latter achieves no less max-flow. Therefore, the string of all 0 's need not to be considered. In our method, as candidate values of $a_{j}$, we only consider the string of all 1 ' and the strings having only single element of value 1 . That is, we only consider strings, $(100 \ldots 0),(010 \ldots 0), \ldots .,(00 \ldots 01)$, and (11 1...1). This reduces the number of candidates as vector $a_{j}$ to $k_{j}+1$, and the size of the entire search space to $\prod_{j \in \bar{E}}\left(k_{j}+1\right)$. This methods significantly speed up our EDA algorithm, and this is also a slight improvement from "BlockWise Representation and Operators" in [10], which results in the search space of size $\prod_{j \in \bar{E}}\left(k_{j}+2\right)$. We call our method "Block-Wise-Modified Representation and Operators".

## C. Greedy Sweep-Modified

Greedy Sweep [10] is an operator that can be used to generate a number of more candidate solutions from the currently best candidate solution after evaluating all the members in the population in each iteration. It can be regarded as a local search. In [10], Greedy Sweep subjects each vector $a_{j}, j \in \bar{E}$ in the currently best individual to its local search mechanism. We suggest modifying this method. In our modified method, which we call "Greedy Sweep-modified," we skip the vectors having only single element of value 1 in the Greedy Sweep operation.

## VI. EXPERIMENTAL RESULTS

The parameters used for the experiments are as follows: Population size $\left(|\Delta_{0}\right)$ is 200 and the number of the best candidate solutions selected from set $\Delta_{0}$ is 10 , which is $5 \%$ of population size. In the experiment results, we demonstrate the performance of EDA with block-wise/Greedy Sweep and Block-Wise-Modified/Greedy Sweep-Modified methods by carrying out simulations on various network topologies. We also compare our results with two previously proposed approaches by M. Kim et al. [9], [10] to minimize coding vectors. These methods use GA and are known as Minimal 1 and Minimal 2. For Minimal 1, the algebraic method [9] is used without "Block-Wise representation and operators" and "Greedy Sweep" methods. For Minimal 2, the decomposition method is used with "Block-wise representation and operators" and "Greedy Sweep" methods. For each of the four methods, the best and the average values obtained from 20 random trials are shown in Table I. We use two types of network topologies for our simulations.

Network topology I: Suppose that link $w$ in network $A$ in Fig. 1 has capacity 2 , which can be represented by two parallel links in the multi-graph. Fig. 4 illustrates a network in which a number of copies of network $A$ are cascaded such that the source of each subsequent copy of $A$ is replaced by an earlier copy of sink. This topology can be viewed as overlaying network A of Fig. 1 on each node of the binary tree in Fig. 4 b). We can expand the size of the network by overlaying network $A$ on nodes of a larger binary treee.g., 31 copies of $A$ and $4,8,16$, and 32 sinks, respectively. We use

Table 1. Number of Coding Links Calculated

binary trees containing 3, 7 (as illustrated by Fig. 4 c), 15, andthese networks for our simulation. In all these networks, the maximum multicast rate 2 is achievable without coding, so the minimal number of coding links that achieve multicast rate 2 is zero. Therefore, the minimum value of 0 for optimization (2) can be used as a benchmark.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Network toplogy I
Network topology II: In the second set of sample networks, two topologies generated by the algorithm in [14] are employed with the following parameters: ( 50 nodes, 87 links, 10 sinks, rate 5) and ( 75 nodes, 156 links, 15 sinks, rate 7) employed.

In our experiments, we have presented the performance of EDA and GA and their improvements (such as Greedy Sweep Modified, Block-wise-modified Representation, etc.) Table I. shows that the block-wise-modified representation and operators, clearly outperform the block-wise counterpart in all aspects. It is observed that the EDA with block-wise-modified and Greedy Sweep-Modified outperform the EDA with Blockwise and Greedy Sweep. We can also observe that the performance of EDA is at least as good and often better than that of both Minimal 1 [9] and Minimal 2 [10] both in terms of the best and the average values (the number of coding links). More impressively, EDAs produce solutions with a smaller number of coding links and a smaller number of iterations than GAs (Minimal 1 and Minimal 2).
Our proposed EDA method outperforms the algorithms introduced in Minimal 1 and Minimal 2 methods, while providing a comparable computational complexity.

## VII. CONCLUSIONS AND FUTURE WORK

In this paper, we presented EDAs for minimizing network coding resources problem. The simple model, low
implementation complexity, and resistance to being trapped in a local minimum, all make EDA a suitable candidate for solving the problem of minimizing network coding resources.
There are several topics for further research. i.e., we may further improve the centralized algorithm, by a smarter management of population such that it converges faster to a better solution. EDA components of the proposed approach, such as the method for constructing the initial population, can be further specialized for the problem at hand to improve the algorithm's performance.
