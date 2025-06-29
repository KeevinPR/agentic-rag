# A hybrid evolutionary algorithm with guided mutation for minimum weight dominating set 

Sachchida Nand Chaurasia $\cdot$ Alok Singh

Published online: 23 April 2015
(c) Springer Science+Business Media New York 2015


#### Abstract

This paper presents a hybrid evolutionary algorithm with guided mutation ( $\mathrm{EA} / \mathrm{G})$ to solve the minimum weight dominating set problem (MWDS) which is $\mathcal{N} \mathcal{P}$ hard in nature not only for general graphs, but also for unit disk graphs (UDG). MWDS finds practical applications in diverse domains such as clustering in wireless networks, intrusion detection in adhoc networks, multidocument summarization in information retrieval, query selection in web databases etc. EA/G is a recently proposed evolutionary algorithm that tries to overcome the shortcomings of genetic algorithms (GAs) and estimation of distribution algorithms (EDAs) both, and that can be considered as a cross between the two. The solution obtained through EA/G algorithm is further improved through an improvement operator. We have compared the performance of our hybrid evolutionary approach with the state-of-the-art approaches on general graphs as well as on UDG. Computational results show the superiority of our approach in terms of solution quality as well as execution time.


Keywords Constrained optimization $\cdot$ Dominating set $\cdot$ Estimation of distribution algorithm $\cdot$ Evolutionary algorithm $\cdot$ Guided mutation $\cdot$ Heuristic

## 1 Introduction

For any graph, a dominating set is a set of nodes such that each node of the graph either belongs to the dominating

[^0]set or is adjacent to a node in the dominating set. A minimum dominating set is a dominating set with minimum cardinality. Use of dominating sets is widespread in wireless networks for clustering and forming a virtual backbone for routing, and several efficient centralized and distributed algorithms have been proposed for this purpose in the literature, e.g. $[2,3,5,10,16]$. However, all these approaches work under the assumption that all nodes are the same in all respects. These approaches may not yield good results in heterogeneous environments where the capabilities of the nodes differ. For example, different nodes may have different residual energy, allotted bandwidth or transmission range. Under these circumstances, instead of minimizing the cardinality of the dominating set, it is more appropriate to minimize the weighted sum of the nodes present in the dominating set. This problem of minimizing the weighted sum of the nodes present in the dominating set is called the minimum weight dominating set problem. Both minimum dominating set problem (MDS) and the minimum weight dominating set problem (MWDS) are $\mathcal{N} \mathcal{P}$-hard [6].

Many approaches have been proposed in the literature for MWDS problem, but most of them are for unit disk graphs (UDG) which are used to model wireless networks. In UDG, nodes lie on an Euclidean plane and an edge exists between a pair of nodes, if and only if the Euclidean distance between them does not exceed a fixed threshold. A characteristic feature of UDG is that the number of independent neighbors of a node is polynomially bounded. To form a backbone for adhoc wireless networks, Wang et al. [15] proposed new centralized and distributed approximation algorithm, where node has some cost and a minimum weight dominating set is created. These approaches assume that node weights are smooth, i.e., ratio of weights of adjacent node does not exceed a fixed constant. Dai et al. [4] proposed a


[^0]:    S. N. Chaurasia $\cdot$ A. Singh ( $\boxtimes$ )

    School of Computer and Information Sciences, University of Hyderabad, Hyderabad 500 046, India
    e-mail: alokcs@uohyd.ernet.in
    S. N. Chaurasia
    e-mail: mc10pc13@uohyd.ernet.in

$5+\epsilon$-approximation algorithm to form a minimum weight dominating set for UDG. This goal is achieved in two steps. In the first step, the plane in which the nodes of the UDG lie is partitioned into $k \mu \times k \mu$ blocks, where $\mu=\frac{\sqrt{2}}{k}$ and $k$ is some large integer constant, and in the second step, each block is partitioned into $k^{2}$ squares. Finally, results of both the steps are combined to get a minimum weight dominating set. Another $4+\epsilon$-approximation scheme [20] is based on a polynomial-time dynamic programming algorithm for the minimum weight chromatic disk cover problem. Last two approaches do not assume node weights to be smooth. Zhu et al. [19] proposed another polynomial time approximation scheme to form a minimum weight dominating set for UDG, where the weights of the nodes in the graph are smooth.

However, use of MWDS is not limited to clustering and routing in wireless networks. In fact, MWDS has applications in several diverse domains. It finds application in gateway placement in a wireless mesh network. A polynomial time near-optimal algorithm is proposed in [1] to recursively compute minimum weight dominating set in each iteration, so as to minimize the number of gateways and also satisfy the QoS (quality of service) requirements. During the installation of wavelength division multiplexing optical-networks, MWDS is used to minimize the number of full wavelength converters required in order to cut down the installation cost and to subdue the technological limitations [7]. MWDS was also used in determining the nodes in an adhoc network where intrusion detection software for squandering detection needs to be installed [14]. Shen et al. [12] used the concept of dominating sets in information retrieval for the task of multi-document summarization. In this approach, first a graph is constructed where nodes represent the sentences from various documents and an edge exists between two sentences if they are similar. Then a minimum dominating set is computed over this graph to get a summary of all the documents. The application of MWDS is extended to the task of query selection, so as to harvest the data records from hidden web database efficiently [17]. For this purpose each web database is modeled as an undirected attribute-value graph (AVG) and the task of the optimal query selection for the web database is shown equivalent to solving MWDS in corresponding AVG. In none of the applications cited in this paragraph, we can assume the underlying graph to be UDG. However, all the approximation schemes available in the literature work for UDG only, and therefore, these schemes cannot be used for aforementioned applications. In fact, underlying graphs in these applications vary depending on the situation and as a result only those approaches, which can be applied to any general graph can be used. In the absence of the approximation schemes for general graphs, heuristics and metaheuristics are attractive alternatives.

To the best of our knowledge, only two metaheuristic approaches have been proposed in the literature for MWDS. Jovanovic et al. [8] developed an ant colony optimization (ACO) algorithm which was inspired by the ant-colony optimization approach of Shyu et al. [13] for the minimum weight vertex cover problem and tested it on general graphs. This ACO approach will be referred to as Raka-ACO subsequently. Potluri and Singh [11] proposed four greedy heuristics, a hybrid genetic algorithm and two versions of hybrid ant-colony optimization algorithm for MWDS. The solutions obtained through the genetic algorithm and the ACO algorithms are improved further though a minimization heuristic. The genetic algorithm uses steady-state population replacement method, selects parents using binary tournament selection and employs fitness-based crossover and simple bit flip mutation to produce offspring. Hereafter, this hybrid genetic algorithm will be referred to as HGA. Except for pheromone initialization, the two ACO versions are same in all other respects. Starting with an empty set $S$, these two ACO versions construct dominating set by performing a random walk on the graph and adding the nodes visited to $S$ until $S$ becomes a dominating set. The next node to be visited is selected based on pheromone concentration on the nodes. The first version of ACO initializes all pheromone trails to the same value without any bias, whereas the second version uses a pre-processing step to initialize the pheromone trails according to the quality and compositions of the solutions generated in the preprocessing step. The first version will be referred to as ACO-LS and the second version as ACO-PP-LS subsequently. All the approaches presented in [11] have been tested on the same general graph instances as used in [8]. In addition, some UDG instances have also been used. HGA, ACO-LS and ACO-PP-LS approaches obtained much better results in comparison to Raka-ACO. In fact, three of the four greedy heuristics presented also outperformed Raka-ACO. As far as the relative performance of HGA, ACO-LS and ACO-PPLS approaches are concerned, HGA obtained better quality solutions with increase in average node degree and graph size, but at the expense of much larger execution time. There is not much difference in solution quality of ACO-LS and ACO-PP-LS, but ACO-PP-LS is faster than ACO-LS.

In this paper, we present a hybrid approach comprising evolutionary algorithm with guided mutation (EA/G) and an improvement operator for MWDS. EA/G is a relatively recent evolutionary technique developed by Zhang et al. [18] that uses a guided mutation operator to produce offspring (solutions). This operator uses a combination of global statistical information about the search space and the location information of the solutions found so far to generate the offspring. Zhang et al. [18] used EA/G to solve the maximum clique problem. The success of EA/G in solving the standard benchmark instances of the maximum clique

problem has motivated us to develop an EA/G approach for MWDS. In addition, we present the modified version of a greedy heuristic proposed in [11] and use it inside our hybrid EA/G approach for the initial solution generation and repairing an infeasible solution. We have compared our hybrid EA/G approach with the approaches presented in $[8,11]$ on the same benchmark instances as used in $[8$, 11]. In comparison to these approaches, our hybrid approach obtained better quality solutions in shorter time.

The remainder of this paper is organized as follows: Section 2 formally defines the minimum weight dominating set problem and introduces the notational conventions used in this paper. Section 3 describes the proposed modifications in one of the heuristics of [11]. Section 4 provides an overview of EA/G. Our hybrid EA/G approach is presented in Section 5. Section 6 reports the computational results and provide a comparative analysis of our hybrid EA/G approach vis-à-vis existing approaches for MWDS. Finally, Section 7 outlines some concluding remarks and directions for future research.

## 2 Problem formulation

In an undirected graph $G=(V, E)$, where $V$ is the set of nodes and $E$ is the set of edges, two nodes $u$ and $v$ are called neighbor of each other or adjacent to each other, iff, there exists an edge between them, i.e., $(u, v) \in E$. A dominating set $D \subseteq V$ is a set of nodes such that each node $v \in V$ either belongs to $D$ or is neighbor of at least one node in $D$. Any node belonging to $D$ is called a dominating node or dominator. Any node not in $D$ is called a dominatee or non-dominating node. The minimum dominating set problem (MDS) seeks a dominating set on $G$ whose cardinality is least among all the possible dominating sets on $G$. In minimum weight dominating set problem (MWDS), a weight is assigned to each node of $V$ through a weight function $w: V \rightarrow \mathfrak{R}^{+}$and the goal is to find a dominating set with the minimum sum of node weights. More formally, MWDS seeks $\underset{D \in D S}{\arg \min } \sum_{v \in D} w(v)$, where $D S$ is the set of all dominating sets of $G$. Both MDS and MWDS have been proven to be $\mathcal{N} \mathcal{P}$-hard [6]. In fact, MWDS is a generalization of MDS as it reduces to MDS when $w(v)=1 \forall v \in$ $V$. Important notational conventions used in this paper are
given in Table 1. Additional notational conventions will be introduced as and when required.

## 3 Heuristic

In this section, we present an improved version of a heuristic (viz. heuristic 2) which has been presented in [11]. Actually, four different heuristics have been presented in [11]. The reason for choosing heuristic 2 is that among these four heuristics, it performed the best. In all these heuristics, initially, all nodes are assumed to have color WHITE. Starting with an empty set $D$, these heuristics build a dominating set by iteratively adding a node to $D$ till it satisfies the property of a dominating set. A node that is added to $D$ is re-colored BLACK and all its neighbors are re-colored GREY. Obviously, with this coloring scheme, a heuristic stops when no WHITE node exists. The manner in which the nodes are selected for inclusion into the partially constructed dominating set leads to different heuristics. We have made two modifications in heuristic 2 of [11]. Suppose $D$ is the the partially constructed dominating set, then $S=V-D$ is the set from which next node is added to the dominating set $D$. Also suppose $c: V \rightarrow\{0,1\}$ is a function such that $c(v)=1$, iff color of node $v$ is WHITE at present, 0 otherwise. Our first modification utilizes closed neighborhood instead of open neighborhood while choosing the next node to be added to the dominating set. In heuristic 2 of [11], to determine the next node to be added to the dominating set, the sum of weights of WHITE nodes belonging to open neighborhood of each node $u \in S$ (1) is first calculated and then next node is selected using (2), whereas in our heuristic, sum of weights of WHITE nodes belonging to the closed neighborhood of each node $u \in S$ is first calculated (3) and then next node to be added is determined using (4). The motivation for using the closed neighborhood instead of the open neighborhood lies in the fact that when a node to be added is itself WHITE, its weight should be added to the sum of the weights of its neighboring WHITE nodes because addition of this node in the partially constructed dominating set not only satisfies the property of the dominating set with respect to the neighboring WHITE nodes of this node adjacent but also with respect to this node itself, i.e., once this node is added, each node belonging to the closed neighborhood of this node will be either adjacent to a

Table 1 Notational Convention

![img-0.jpeg](img-0.jpeg)

Fig. 1 Input graph. Initially, all nodes are colored WHITE and weight $=0$
node in the dominating set or itself present in the dominating set.
$W(u) \leftarrow \sum_{v \in O N(u)} w(v) \times c(v)$
$v \leftarrow \arg \max _{u \in S} \frac{W(u)}{w(u)}$
$\bar{W}(u) \leftarrow \sum_{v \in C N(u)} w(v) \times c(v)$
$v \leftarrow \arg \max _{u \in S} \frac{\bar{W}(u)}{w(u)}$
Figures 1, 2, 3, 4, 5, 6, 7 illustrate our first modification with the help of an example. Figure 1 shows an undirected
![img-1.jpeg](img-1.jpeg)

Fig. 2 Node 2 is selected by both heuristics and weight $=94$
![img-2.jpeg](img-2.jpeg)

Fig. 3 Node 0 is selected by both heuristics and weight $=162$
connected weighted graph with 15 nodes where the number inside a circle indicates the ID of the node represented by that circle and the number outside a circle indicates the weight of the corresponding node. All nodes are colored WHITE in this figure to show the initial state. Both the heuristics select node 2 during the first iteration for inclusion into the partially constructed dominating set. Node 2 is colored BLACK now and after that all the neighbors of node 2 , viz. nodes $9,3,11$ and 6 are colored GREY. This situation is shown in Fig. 2. Both the heuristics continue to select identical nodes for three more iterations leading to the further inclusion of node 0,7 and 13 in that order to the partially constructed dominating set.

Figures 3, 4, 5 depict the partially constructed dominating set at the end of each of these three iterations. The
![img-3.jpeg](img-3.jpeg)

Fig. 4 Node 7 is selected by both heuristics and weight $=242$

![img-4.jpeg](img-4.jpeg)

Fig. 5 Node 13 is selected by both heuristics and weight $=323$
partially constructed dominating set depicted in Fig. 5 has weight 323. Now, the only WHITE node is node 8 . Our heuristic selects node 8 as it has the maximum ratio of 1 as per (4) in the next iteration and produces a dominating set with nodes $2,0,7,13$ and 8 , and total weight 407 , which is shown in Fig. 6.

Heuristic 2 of [11], on the other hand, returns GREY node 14 to cover WHITE node 8 , and produces a dominating set with nodes $2,0,7,13$ and 14 , and total weight 434 , which is shown in Fig. 7. As open neighborhood is used here, so node 8 ironically has the minimum ratio of 0 and node 14 has the maximum ratio of $\frac{84}{111}$ as per (2), and, that is why node 14 is selected. It is to be noted that even if we swap the weights of node 8 and 14 , our heuristic will select the appropriate node according to the changed scenario. In
![img-5.jpeg](img-5.jpeg)

Fig. 6 Node 8 is selected with our heuristic and weight $=407$
![img-6.jpeg](img-6.jpeg)

Fig. 7 Node 14 is selected with heuristic of [11] and weight $=434$
the changed scenario node 8 will have the weight of 111 and node 14 will have the weight of 84 . Under this situation node 14 has the maximum ratio of $\frac{111}{84}$ and node 8 again has the ratio 1 as per (4), so our heuristic will correctly select node 14 . In this case, however, heuristic 2 of [11] will also select node 14 .

Our second modification is a tie-breaking rule. Actually, when there are more than one node satisfying (4), then the next node to be added is selected using this tie-breaking rule. Suppose $S^{\prime}$ is the set of nodes satisfying (4), then our heuristic computes the number of WHITE nodes belonging to the closed neighborhood of each node $u \in S^{\prime}(5)$ and then the next node to be added is determined using (6). In case there is more than one node satisfying even (6), then the next node to be added is selected arbitrarily from among these nodes. The motivation behind this tie-breaking rule lies in experimental observation that using this rule helps in getting better results on more instances.
$w d(u) \leftarrow \sum_{v \in C N(u)} c(v)$
$v \leftarrow \arg \max _{u \in S^{\prime}} \frac{w d(u)}{w(u)}$
Hereafter, original heuristic 2 of [11] will be referred to as Heu_A and our improved version as Heu_I.

## 4 Overview of EA/G

An evolutionary algorithm with guided mutation (EA/G) [18] is a recent addition to the family of evolutionary algorithms. Zhang et al. [18] developed EA/G with the intention of removing, as far as possible, the drawbacks of the genetic algorithms (GAs) and the estimation of distribution

algorithms (EDAs). Both GAs and EDAs are population based evolutionary approaches. GAs conventionally use genetic operators, such as crossover and mutation, to produce offspring (solutions) from selected parents. In order to produce offspring, GAs directly utilize the location information of the solutions found so far. However, no global information about the search space is used to produce the offspring. As a matter of fact, this global information can be extracted in GAs using all the solutions produced so far since the beginning. Here, by location information of a solution, we mean the information that can uniquely characterize a solution in the space of all possible solutions, e.g., in case of MWDS, the location information consists of the set of nodes present in a solution as this information can uniquely characterize the dominating set represented by that solution. Rather than using genetic operators, EDAs rely on a probability model to produce offspring. This probability model characterizes the distribution of promising solutions at each generation, and, offspring are produced by sampling this model. This probability model is updated at each generation using the global statistical information extracted from the population members present in that generation. EDAs do not directly utilize the location information of the solutions found so far.

An ideal algorithm should take into account both the factors, viz. global information about the search space and location information of the solution found so far, while producing offspring. EA/G was developed by Zhang et al. [18] exactly with this intention. EA/G employs a mutation operator called guided mutation (GM) to produce offspring. In guided mutation, an offspring is created partly by sampling a probability model characterising global statistical information and partly by copying elements from its parent, i.e.,offspring are produced by taking into account the global statistical information as well as the location information of the solutions found so far.

Zhang et al. [18] proposed EA/G approach in the context of maximum clique problem. Computational results demonstrated the superiority of EA/G approach over other evolutionary approaches in solving the maximum clique problem. Motivated by the success of EA/G in solving the maximum clique problem, we have developed an EA/G approach for MWDS, which is described in the next section.

## 5 Hybrid EA/G approach for MWDS

We have developed a hybrid approach to MWDS combining EA/G algorithm with an improvement operator. The solutions generated through EA/G algorithm are passed through the improvement operator in a bid to improve them further. Hereafter, we will refer to our hybrid EA/G approach with
improvement operator as EA/G-IR (EA/G with improvement operator). Before starting our EA/G-IR approach, we precompute the set of neighbors for each node $v \in V$. The salient features of our EA/G-IR approach for MWDS are described in the subsequent subsections.

### 5.1 Solution encoding

Subset encoding has been used to represent a solution, i.e., each solution is represented directly by the set of the nodes it contains.

### 5.2 Initial solution

First member of the initial population is always constructed through our heuristic (see Section 3). The remaining members of the initial population are also constructed in the same manner as in our heuristic except for the fact that during each iteration (4) (and (6) if needed) is used for selecting the next node for inclusion in the partially constructed dominating set with probability $\pi_{i}$, otherwise the next node is selected randomly. Each member of the initial population, irrespective of how it got constructed, is passed through an improvement operator in a bid to improve it further.

Pseudo-code for constructing an initial solution except first solution is presented in Algorithm 1.

```
    // Initially all nodes in V are colored minTE
    \(I=\bar{V}\);
    \(W_{i}=V\);
    \(W D=\Phi\);
    while \(W_{i} \neq \Phi\) do
        Generate a random number \(r\) such that \(0 \leq r \leq 1\);
        if \(r<\pi\) then
            \(v=\operatorname{argmax} \frac{W_{i} w_{i}}{w r}\);
        else
            \(v=\operatorname{random}\left(W_{i}\right)\);
        end
        if \(r \in \operatorname{WHITE}\) then
            \(\left(W_{i} \leftarrow W_{i} ;\{r\}\right.\);
        end
        \(w d(v)=\left\{u: u \in O N(v) \cap W_{i}\right\}\);
        \(W_{i} \leftarrow W_{i} ; w d(v)\);
        \(W D \leftarrow W D ;\{v\}\);
        make \(v\) BLACK;
        make all vertices \(E w d(v)\) GREY;
        \(I \leftarrow I \backslash\{r\}\);
        end
    return \(W D\);
```

5.3 Initialization and update of the probability vector

Like [18], we have also used a univariate marginal distribution (UMD) model to maintain the distribution of the promising solutions in the search space. In this model, a probability vector $p=\left\{p_{1}, p_{2}, \ldots, p_{|V|}\right\} \in[0,1]^{|V|}$ is used to characterize the distribution of the promising solutions in the search space, where $|V|$ is the cardinality of

$V$, i.e., number of nodes in the graph. Each $p_{i} \in p$ gives the probability of node $i$ of $V$ to be present in a dominating set. Our guided mutation operator (described in Section 5.4) uses this probability vector to generate offspring at each generation $g$. This probability vector is initialised using the $N_{c}$ initial solutions. The pseudo-code for initializing a probability vector $p$ is given in Algorithm 2.

```
Algorithm 2: The pseudo-code for initializing a probability vector \(p\)
Compute \(\mathrm{n}_{i} \leftarrow \operatorname{number}\) of initial solutions containing node \(v, v v \in V\).
Compute \(p_{i} \leftarrow \frac{N_{c}}{d_{i}} v v \in V\).
```

At each generation $g$, a parent set parent $(g)$ is formed by selecting the best $\frac{N_{c}}{d}$ solutions from current population $\operatorname{pop}(g)$. Once parent $(g)$ is formed, it is used for updating the probability vector $p$. The pseudo-code for updating the probability vector is given in Algorithm 3, where $\lambda \in(0,1]$ is the learning rate, and it governs the contribution of the solutions in parent $(g)$ to the updated probability vector $p$, i.e., the higher the value of $\lambda$, the greater the contribution of the solutions in parent $(g)$.

```
Algorithm 3: The pseudo-code for updating a probability vector \(p\) in generation
    g
    Compute \(\mathrm{n}_{i} \leftarrow\) number of solutions in parent(g) containing node \(v, v v \in V\).
    Compute \(p_{i} \leftarrow(1-\lambda) p_{v}+\lambda \frac{N_{c}}{d_{i}} v v \in V\).
```


### 5.4 Guided mutation (GM) operator

As mentioned already, $G M$ operator uses both global statistical information stored in the form of probability vector $p$ and location information of the solutions found so far for generating new solutions. $G M$ operator is applied on the best solution $b_{s}$ in the current population to generate new solutions. The pseudo-code for generating a new solution through $G M$ operator is given in Algorithm 4, where $\beta$ is an adjustable parameter in $[0,1]$ and $D$ is a new solution constructed through $G M$ operator whose nodes are either sampled from probability vector $p$ or directly copied from best solution $b_{s}$ in parent $(g)$. Parameter $\beta$ controls the relative contribution of probability vector $p$ and best solution $b_{s}$ in the generation of a new solution. As the value of $\beta$ increases, more nodes of $D$ are sampled from probability vector $p$. On the other hand, as the value of $\beta$ decreases, more nodes are directly copied from $b_{s}$. There is no guarantee of the feasibility of the solution $D$ generated through $G M$ operator, i.e., $D$ may not be a dominating set. Therefore, every solution $D$ generated through $G M$ operator is checked for feasibility and if $D$ is found to be infeasible, then it is passed through a repair operator which transforms $D$ into a feasible solution. This repair operator is described in the next section.

```
Algorithm 4: The pseudo-code of generating a solution through GM operator
    \(D \leftarrow \mathrm{~d}:\)
    foreach node \(v \in V\) do
        Generate a random number \(r_{i}\) such that \(0 \leq r_{i} \leq 1\);
        if \(r_{i}<\beta\) then
            Generate a random number \(r_{i}\) such that \(0 \leq r_{i} \leq 1\);
            if \(r_{i}<\rho_{i}\) then
                \(D \leftarrow D_{i} \cup\{v\}\);
            end
        else
            if \(v \in b_{s}\) then
                \(D \leftarrow D_{i} \cup\{v\}\);
            end
        end
    end
return \(D\)
```


### 5.5 Repair operator

The repair operator is applied only on an infeasible solution. Our repair operator is quite different from the repair heuristic of [11] and computationally much more efficient. In the repair heuristic of [11], initially, $S$ is the set of $V \backslash D$ nodes, where $V$ is the set of nodes and $D$ is the infeasible solution to be repaired. The repair heuristic iteratively selects a node from $S$ as per (2) and adds it to $D$ after deleting it from $S$. This process is repeated till $D$ becomes a dominating set. Actually, set $S$ also contains those GREY nodes which have no neighboring WHITE node. Such GREY nodes can never be selected for inclusion in $D$, but in every iteration of repair heuristic used in [11], corresponding ratios needed for Eq. 2 are calculated even for these GREY nodes. From the empirical observations, it is found that there are a large number of such GREY nodes in $S$ which unnecessarily increases the computational burden of the repair heuristic used in [11]. To overcome this shortcoming, in our repair operator, we begin by computing the set of WHITE nodes $W_{n}$, i.e., $W_{n}$ contain those nodes which are not the neighbor of any node in the infeasible solution $D$. Then in every iteration, we initialize set $S$ to the closed neighborhood of a randomly chosen node in $W_{n}$. With this initialization of $S$ in every iteration, the cardinality of set $S$ is always much smaller, especially for graphs with a large number of nodes. In every iteration, after initializing $S$, our repair operator selects a node from set $S$ using (4) (and (6) if needed) and includes it into the infeasible solution $D$. In addition, after each iteration in our repair operator, we delete all those nodes from $W_{n}$ which are no longer WHITE. This further helps in speeding-up the repair operator. These iterations continue until no WHITE nodes are left, i.e., until $D$ becomes feasible. In the repair heuristic of [11], with probability $p_{h}$ (which was set to 0.70 ), the infeasible solution is repaired as mentioned already, and otherwise it is repaired randomly, i.e., some infeasible solutions are repaired by selecting the node from $S$ in a totally random manner. This is done to maintain the diversity of the population as the other approach was purely greedy. Our repair operator is a proper mix of randomness and greediness. As such, all solutions are repaired as described

above, and no infeasible solution needs to be repaired in a purely random manner just for the sake of diversity. The pseudo-code of repair operator is presented in Algorithm 5.

```
Algorithm 5: The pseudo-code of repair operator
    // D is an infeasible solution on which repair operator is
    applied
    W
    while W
        \(W_{r} \neq \emptyset\) do
            \(W_{r} \neq \operatorname{random}\left(W_{0}\right) ;\)
            \(S \leftarrow C N\left(v_{1}\right) ;\)
            \(v=\operatorname{argmax} \frac{W_{r}}{w d} ;\)
            \(w d(v)=\left\{u: u \in C N\left(v\right) \cap W_{0}\right\} ;\)
            make + BLACK;
            \(D \leftarrow D \backslash\{v\}\} ;\)
            make all vertices \(C w d(v) \backslash\{v\}\) GREY;
            \(W_{0} \leftarrow W_{0} \backslash w d(v)\} ;\)
        end
    return D ;
```


### 5.6 Improvement operator

All feasible solutions are passed through an improvement operator in a bid to further improve the solution. Our improvement operator removes redundant nodes from a dominating set $W D$. A node $v \in W D$ is redundant if $C N(v) \subseteq\left(\cup_{u \in D \backslash\{v\}} O N(u)\right)$, i.e., all nodes in $O N(v)$ are either in $W D$ or the neighbor of a node in $W D \backslash\{v\}$ and $v$ is the neighbor of a node in $W D$. If node $v$ is redundant, then it can be removed from $W D$ without affecting the dominating set property of $W D$. Our improvement operator begins by computing the set of redundant node, then an iterative process takes over, where during each iteration, the redundant node, having the highest ratio of its weight to its degree, is deleted from the dominating set, and the set of redundant nodes is recomputed. The iterative process stops when the set of redundant nodes becomes empty. Clearly, our improvement operator follows a greedy strategy. The pseudo-code of our improvement operator is given in Algorithm 6 where $W D$ is the input dominating set and $R_{r}$ is the set of redundant nodes in $W D$. This is different from Minimization heuristic of [11] where during each iteration, the redundant node to be deleted is either chosen based on highest ratio of weight of a node to its degree or chosen randomly from the set of redundant nodes. In every iteration, the first strategy is used with probability $p_{r}$ (which was set to 0.60 ), and otherwise the random strategy is used. Our improvement operator follows the greedy strategy always. We have experimented with random strategy also, but the greedy approach produced better solution in comparison to the combination of greedy and random strategies of [11].

```
Algorithm 6: The pseudo-code of improvement operator
    \(R_{r} \leftarrow\left\{v: v \in W D \text { and } C N(v) \subseteq\left(\cup_{u \in D \backslash\{v\}} O N(u)\right)\right.\);
    while \(\left(R_{r} \neq \emptyset\right)\) do
        \(v=\operatorname{argmax} \frac{W D}{w d(v)} ;\)
        \(W D \leftarrow W D \backslash\{v\} ;\)
        \(R_{r} \leftarrow\left\{v: v \in W D\right.\) and \(C N(v) \subseteq\left(\cup_{u \in D \backslash\{v\}} O N(u)\right) ;\)
        end
    return W D ;
```

5.7 Other features

Zhang et al. [18] puts best $\frac{N_{r}}{2}$ solutions of $\operatorname{pop}(g)$ into parent $(g)$ and creates $\frac{N_{r}}{2}$ new solutions in every generation. The population for the next generation is formed using $\frac{N_{r}}{2}$ solutions in parent $(g)$ and $\frac{N_{r}}{2}$ newly created solutions. On the other hand, in our approach, parent $(g)$ is formed using best $\frac{N_{r}}{4}$ solutions of $\operatorname{pop}(g)$, and $\frac{N_{r}}{2}$ new solutions are produced in every generation. Best $\frac{3 \frac{N_{r}}{2}}{4}$ solutions of $\operatorname{pop}(g)$ along with $\frac{N_{r}}{4}$ newly created solutions constitute $\operatorname{pop}(g+1)$ in our approach. We have also tried the same strategy as [18], but our strategy gave better results.

If in a generation, all solutions are found to be identical, then we reinitialize the population in the same manner as described in Section 5.2.

The pseudo-code of our EA/G-IR approach for MWDS problem is given in Algorithm 7.

```
Algorithm 7: EA/G-IR Approach for MWDS
    1 At generation \(g \leftarrow 0\), an initial population \(p o p(g)\) consisting of \(N_{r}\) solutions \(\left(N_{r}\right.\) should be divisible by 4) are generated in a manner described in Section 5.2;
    2 Initialize the probability vector \(p\) for all nodes using Algorithm 2;
    3 Select best \(\frac{N_{r}}{2}\) solutions from \(\operatorname{pop}(g)\) to form a parent set parent \((g)\), and then
    update the probability vector \(p\) using Algorithm 3;
    4 Apply the GM operator \(\frac{N_{r}}{2}\) times on the best solution \(b_{v}\) in parent \((g)\) in order to
    generate \(\frac{N_{r}}{2}\) new solutions. A repair operator is applied to each generated
    solution, if necessary, and then an improvement operator is applied to each
    generated solution to improve the solution fitness. Add all \(\frac{N_{r}}{2}\) newly generated
    solutions along with best \(\frac{N_{r}}{2}\) parent \((g)\) solutions to form \(\operatorname{pop}(g+1) \text {. If the }\) stopping condition is met, return the dominating set with the minimum weight found so far ;
    \(g \leftarrow g+1 ;\)
    6 If all solutions are identical, then reinitialize \(\operatorname{pop}(g)\), and go to step 2 ;
    7 Go to step 3 ;
```


## 6 Computational results

In this section we present the computational results of our EA/G-IR approach for MWDS and compare them with the state-of-the-art approaches. In the literature, three sets of instances were used to evaluate the performance of different algorithms, viz. Type I, Type II and unit disk graphs (UDG). Type I and Type II instances were generated by Jovanovic et al. [8]. Type I and Type II instances consist of undirected connected weighted graphs. For Type I instances, the weights of the nodes are randomly distributed in the closed interval $\left[20,70\right]$. For Type II instances, weights are randomly distributed in the closed interval $\left[1, d c(v)^{2}\right]$, where $d c(v)^{2}$ is square of the degree of the node $v$. For both Type I and Type II instances, the number of nodes varies from 50 to 1000 and the number of edges varies from 50 to 20000. 10 instances were generated for each combination of the number of nodes $(|V|)$ and the number of edges $(|E|)$. The number of edges is also varied while keeping the number

of nodes same so as to observe the variation in the solution with the number of edges. A total of 530 instances $(53 \times 10)$ were generated for each of Type I and Type II datasets leading to a grand total of 1060 instances in these two datasets.

UDG instances were generated by Potluri and Singh [11] using the topology generator of [9]. The nodes are distributed randomly in an area of $1000 \times 1000$ units. The number of nodes in these instances belong to $\{50,100,250,500,750,1000\}$. Transmission range of all
nodes is fixed to either 150 or 200 units. Similar to Type I and Type II instances, 10 instances are generated for each combination of number of nodes and the transmission range. This leads to a total of 120 UDG instances.

Our EA/G-IR approach for MWDS has been implemented in C and executed on an Intel core i5-2400 processor based system with 4 GB RAM running under Fedora 16 at 3.10 GHz . gcc 4.6.3-2 compiler with O3 flag has been used to compile the C program for our approach. In all computational experiments with our approach, we have used

Table 2 Results of Heu_A, Heu_I, Raka-ACO, HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G for small \& medium size Type I instances
NA indicate that result is not available for that instance

$N_{c}=100, \beta=0.70, \lambda=0.60$ and $\pi_{i}=0.55$. All these parameter values are chosen empirically after a large number of trials. These parameter values provide good results, though they may not be optimal for all instances. We have allowed our approach to execute for 800 iterations on each instance. In each iteration $\frac{N_{c}}{4}$, i.e., 25 new solutions are generated. So total $800 \times 25=20000$ solutions are generated for each instance which is the same amount generated by the metaheuristic approaches proposed in [11]. ACO of [8] generates 100000 solutions. To get an idea about the role of the improvement operator in finding high quality solutions, we have also implemented another version of our approach where no improvement operator is used. This version will be referred to as EA/G.

We have compared EA/G-IR and EA/G with four different approaches, viz. HGA, ACO-LS \& ACO-PP-LS approaches proposed in [11] and Raka-ACO approach proposed in [8].

Like [8] and [11], we have analysed our results according to the instance groups. By an instance group, we mean the 10 instances with the same number of nodes and edges. An
instance group is characterized by an ordered pair $(|V|,|E|)$. For this analysis, EA/G-IR is executed only once on each instance like the metaheuristic approaches of [8] and [11]. Tables 2, 3, 4, 5 report the results of Heu_A, Heu_I, RakaACO, HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G on Type I and Type II instances, whereas Table 6 does the same for UDG instances except for the fact an instance group here corresponds to 10 instances with the same number of nodes and transmission range. Data for Raka-ACO is taken from [8], where only Type I and Type II instances were used, and therefore, results of Raka-ACO on UDG instances are not reported. Moreover, standard deviations of solution values and average execution times were also not reported in [8] for Raka-ACO and that is why these two quantities for Raka-ACO are not reported. As the C programs for HGA, ACO-LS and ACO-PP-LS were available, so we have re-executed these programs on our system so that execution time of these approaches can be compared directly with our approaches. This re-execution only changed the execution times from those reported in [11]. For each combination of number of nodes $(|V|)$ and number of edges

Table 3 Results of Heu_A, Heu_I, Raka-ACO, HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G for large size Type I instances

NA indicate that result is not available for that instance

( $|E|$ ) (transmission range in case of UDG instances), these tables (Tables 2, 3, 4, 5, 6) report the average solution quality (Mean) and standard deviation of solution values (SD) over 10 instances. All approaches have high standard deviation as these approaches were executed once on each of the 10 instance and the value of the solution varies from one instance to the other. For the two heuristics Heu_A and Heu_I, we have only reported the average solution quality. In all these tables, a result in bold for EA/G-IR indicates
that it is better than all the existing approaches in the literature. '*' indicates that EA/G-IR is worse than the best among HGA, ACO-LS and ACO-PP-LS. A result in bold italic indicates that it is the best result among Heu_A, Heu_I, Raka-ACO, HGA, ACO-LS and ACO-PP-LS. ' $\dagger$ ' indicates that the result of $\mathrm{EA} / \mathrm{G}$ is equal to the best result among HGA, ACO-LS and ACO-PP-LS and ' $\ddagger$ ' indicates that the result of $\mathrm{EA} / \mathrm{G}$ is better than the best result among HGA, ACO-LS and ACO-PP-LS. The results of Heu_I which are

Table 4 Results of Heu_A, Heu_I, Raka-ACO, HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G for small \& medium size Type II instances
NA indicate that result is not available for that instance

Table 5 Results of Heu_A, Heu_I, Raka-ACO, HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G for large size Type II instances

NA indicate that result is not available for that instance

Table 6 Results of Heu_A, Heu_I, HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G for UDG instances
worse than Heu_A are marked with "- -", and those which are better than Heu_A are marked with "++". Average time taken by different approaches is shown in Tables 7, 8, 9, 10, 11. For better analysis of results, instances are divided into two classes, viz. small \& medium size and large size. Instances with 50 to 250 nodes are classified as small \& medium size instances and instances with 300 to 1000 nodes are classified as large size instances.

After comprehensive analysis of results returned by various approaches, following observations can be made:

1. From Tables $2,3,4,5$, it can be observed that EA/GIR outperformed Raka-ACO in terms of solution quality
on all Type I and Type II instance groups by a huge margin. As the graph size increases, the differences in solution quality also increases. As expected, EA/G-IR obtained much better solutions in comparison to Heu_A and Heu_I also on all instance groups including groups of UDG instances.
2. For small \& medium size Type I instances, EA/G-IR performed worse than HGA, ACO-LS and ACO-PPLS on two instance groups ( $(50,50)$ and $(50,750)$ ), worse than best among HGA, ACO-LS and ACO-PPLS for three instance groups ( $(50,100),(100,100)$ and $(150,150)$ ), but equal to ACO-PP-LS for instance group (50, 100), better than HGA and ACO-PP-LS for

Table 7 Average execution time of HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G in seconds on small \& medium size Type I instances

instance group $(100,100)$ and better than HGA for instance group (150, 150). Out of 32 instance groups, average solution quality of EA/G-IR is worse than best among HGA, ACO-LS and ACO-PP-LS on 5 instances, same as best among HGA, ACO-LS and ACO-PPLS on 4 instances and better than best among HGA, ACO-LS and ACO-PP-LS on remaining 23 instance groups.
3. For small and medium size Type II instances, EA/G-IR performed worse than the best among HGA, ACOLS and ACO-PP-LS for instance group (150, 1000), but better than ACO-LS and ACO-PP-LS. Out of 32 instance groups, EA/G-IR is worse than best among

HGA, ACO-LS and ACO-PP-LS on 1 group, equal to best among HGA, ACO-LS and ACO-PP-LS on 11 groups and better than best among HGA, ACO-LS and ACO-PP-LS on 20 groups.
4. EA/G-IR outperformed HGA, ACO-LS and ACO-PPLS on all large size Type I and Type II instance groups except for two large Type I instances group $(300,300)$ and (300, 500), where ACO-PP-LS obtained better solution quality. For both types of instances, difference in solution quality grows with the number of nodes and the degree of the nodes.

It can also be observed that improvement in solution quality by EA/G-IR for small \& medium size instances

Table 8 Average execution time of HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G in seconds on small \& medium size Type II instances

Table 9 Average execution times of HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G in seconds on large Type I instances
is less in comparison to large size instances. Actually, for small size instances, the results obtained by all the approaches are either optimal or are very close to the optimal and that is why EA/G-IR either obtained the same solution or was not able to improve them much. On the other hand, for large size instances, existing approaches could not scale well and their solution quality deteriorates, and that is why EA/G-IR obtained noticeable improvement in solution quality on almost all the instances.
5. For UDG instances, out of 12 instance groups, average solution quality returned by EA/G-IR is equal to the best among HGA, ACO-LS and ACO-PP-LS on 6 groups and better than all three on the remaining 6 groups.

All the observations made so far clearly show the superiority of EA/G-IR over existing approaches in terms of solution quality which again indicates the advantage of using both the global statistical information about the search space as well as location information of the solution generated so far while generating offspring.
6. From Tables $7,8,9,10,11$, we can clearly say that EA/G-IR is much faster than HGA, ACO-LS and

ACO-PP-LS. From these tables, it can also be seen that as the size of the graph increases, the average execution time taken by HGA, ACO-LS and ACO-PP-LS grow faster than that of EA/G-IR. The superiority of EA/G-IR over HGA in terms of execution time is due to the use of subset encoding in EA/GIR in place of bit vector encoding, which is used in HGA, and efficient implementation of repair operator (see Section 5.5). The size of the dominating set is smaller than the total number of nodes present, and as such, the use of subset encoding yields a significant advantage in terms of time over bit vector encoding. ACO-LS and ACO-PP-LS also use subset encoding, but they are slower than EA/G-IR because each solution in ACO-LS and ACO-PP-LS are constructed from scratch by performing a random walk on the graph where the probability vector needs to be updated whenever a node is added to the partially constructed solution.

Combining the observation made here regarding execution times with observations made previously regarding the average solution quality of EA/G-IR compared to HGA, ACO-LS and ACO-PP-LS, we can say that EA/G-IR, in general, returns solutions of better quality

Table 10 Average execution times of HGA, ACO-LS, ACO-PP-LS, EA/G-IR and EA/G in seconds on large Type I instances
in much less time when compared with HGA, ACO-LS and ACO-PP-LS.
7. Another important point about EA/G-IR is its fast rate of convergence. EA/G-IR on most of the instances
reached the best solution after few iterations only. As already mentioned, EA/G-IR generates 20000 solutions for each instance, but on most of the instances, it reached the best solution after generating 300 to 10000

Table 11 Average execution times of HGA, ACO-LS and ACO-PP-LS, EA/G-IR and EA/G in seconds on UDG instances

solutions. Very few instances took more than 15000 solutions to reach the best solution. Especially on Type II instances, it took much fewer iterations to reach the best solution. On most of Type II instances, it has generated less than 5000 solutions to reach the best solution.
8. As far as comparison between Heu_I and Heu_A is concerned, out of a total of 106 groups of Type I and Type II instances where each group contains 10 instances with the same number of nodes and edges, the average solution quality of Heu_I is worse than that of Heu_A on 3 groups, equal to Heu_A on 87 groups and better than Heu_A on 16 groups. For UDG, Heu_I found the same results as Heu_A for all instances. Heu_I could not improve the results of Heu_A for UDG; the reason could be the fewer edges in these graphs. Overall, the results of Heu_I and Heu_A vindicate our two modifications (Section 3).
9. When we compare EA/G with EA/G-IR, we can see that EA/G is quite capable of finding a high quality solution on its own on small and medium size instances. On the majority of these instances, it is able to find solutions as good as or better than HGA, ACO-LS and ACO-PP-LS, all of which use a local search. There is not much difference in solution quality obtained by EA/G and EA/G-IR on most of these instances. On the other hand, on large instances the benefits of the improvement operator are evident as there is a large difference in solution quality between EA/G and EA/G-IR on all the instances. However, this improvement in solution quality comes at the expense of increased execution time. EA/GIR is much slower in comparison to EA/G on large instances.

In Table 2, there are four instance groups where the average solution quality of EA/G is better than EA/G-IR, which seems to be anomalous. However, this is due to the difference in the execution sequence between EA/G and EA/G-IR. Actually, when the solutions obtained by EA/G and EA/G-IR produce offspring through guided mutation, then these may have a different set of white nodes, and as a result, execution sequences in repair operator may be completely different. This difference in execution sequence in some rare cases can produce a solution which is even better than the one obtained through the improvement operator.

## 7 Conclusions

In this paper, we have presented a hybrid approach called EA/G-IR combining the evolutionary algorithm with guided
mutation (EA/G) and an improvement operator for the minimum weight dominating set problem. We have compared the performance of our EA/G-IR approach with the state-of-the-art approaches available in the literature on standard benchmark instances comprising general graphs and unit disk graphs. Computational results clearly show the superiority of EA/G-IR over the state-of-the-art approaches as it is able to find better quality solutions in general in much shorter time.

As a future work, we intend to extend our approach to the connected minimum weight dominating set problem and the capacitated minimum weight dominating set problem. Similar approaches can also be developed for the set covering problem, the minimum weight vertex cover problem and the target coverage problems in wireless sensor networks etc.

Acknowledgments Authors are grateful to two anonymous reviewers for their valuable comments and suggestions which has helped in improving the quality of this paper.
