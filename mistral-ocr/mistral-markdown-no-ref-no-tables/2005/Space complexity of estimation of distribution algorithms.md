# Space Complexity of Estimation of Distribution Algorithms 

Yong Gao<br>ygao@cs.ualberta.ca<br>Department of Computing Science, University of Alberta, Edmonton, Alberta, Canada, T6G 2E8<br>Joseph Culberson<br>joe@cs.ualberta.ca<br>Department of Computing Science, University of Alberta, Edmonton, Alberta, Canada, T6G 2E8


#### Abstract

In this paper, we investigate the space complexity of the Estimation of Distribution Algorithms (EDAs), a class of sampling-based variants of the genetic algorithm. By analyzing the nature of EDAs, we identify criteria that characterize the space complexity of two typical implementation schemes of EDAs, the factorized distribution algorithm and Bayesian network-based algorithms. Using random additive functions as the prototype, we prove that the space complexity of the factorized distribution algorithm and Bayesian network-based algorithms is exponential in the problem size even if the optimization problem has a very sparse interaction structure.


## Keywords

Estimation of distribution algorithms, space complexity, additive fitness functions, graphical models and bayesian networks, treewidth.

## 1 Introduction

The Estimation of Distribution Algorithms (EDAs) are a class of sampling-based genetic algorithms that generate candidate solutions (individuals) by sampling some probability distributions on the solution space. The sampling probability distributions may be modelled as the product of independent marginal distributions, decomposable distributions obtained from the knowledge about the problem's interaction structures, or Bayesian networks constructed from existing samples of solutions (Mühlenbein et al., 1999; Pelikan et al., 1999; Leung et al., 2001; Larrañaga et al., 2000; Larrañaga and Lozano, 2001).

Unlike many other stochastic local search algorithms, such as the standard genetic algorithm (Goldberg, 1989) and simulated annealing (Kirkpatrick et al., 1983), where the sampling distributions are implicitly defined by the random operators, the sampling distribution in EDAs is an explicit component of the algorithm. As a consequence, an EDA's success heavily depends on the representation and estimation of the probability distributions to capture the interaction information of variables of an optimization problem. An investigation of the complexity issues related to the representation of sampling distributions in EDAs will provide much insight into such problems as how to design efficient EDAs and what the limitations of the algorithm are.

In this paper, we report our research into the complexity issues in two typical implementation schemes of EDAs: the factorized distribution algorithm and the Bayesian

network-based algorithm. Using random additive functions as the prototype, we prove that both of the algorithms have a space complexity that is exponential in the problem size even if the optimization problem has a very sparse interaction structure.

The rest of the paper is organized as follows. In Section 2, we introduce the estimation of distribution algorithm and its typical implementations. In Section 3, we introduce additive fitness functions and their random models. We propose some graph-theory-based measures to capture the degree of interaction in an additive fitness function. We then analyze the graphical models used in EDAs to represent the sampling distributions, and identify criteria to characterize the space complexity of EDAs. In Section 4, we prove our results on the space complexity of two typical implementations of EDAs. Section 5 is the conclusion.

# 2 Estimation of Distribution Algorithms 

A genetic algorithm (GA) is a population-based search algorithm that evolves a population of candidate solutions using so-called genetic operators such as selection, mutation, and crossover. The estimation of distribution algorithms (EDAs) are variants of genetic algorithms. Instead of maintaining a candidate population and using genetic operators, EDAs generate feasible solutions by iteratively sampling a probability distribution on the solution space and updating the probability distribution based on the information gathered from the candidate solutions.

In general, an EDA consists of four parts: (1) a search space $X$; (2) a fitness function $f: X \rightarrow[0, \infty)$; (3) a sampling probability distribution $P$ over $X$; and (4) an algorithm to generate and update the sampling distribution $P$. In the rest of this paper, we will assume $X=\{0,1\}^{n}$.

According to the internal representation of the probability distribution, EDAs can be categorized into three classes.

1. Independent distribution algorithm (IDA): a multivariate distribution of an independent product of one-dimensional distributions. IDA is also called the univariate marginal distribution algorithm (UMDA) (Mühlenbein and Mahnig, 1999).
2. Factorized distribution algorithm (FDA) (Mühlenbein et al., 1999): a multivariate distribution represented as a factorized product of low-dimensional distributions; and
3. Bayesian network-based algorithm (BNA): a multivariate distribution represented as a Bayesian network. In fact, this includes the Bayesian Optimization Algorithm (BOA) (Pelikan et al., 1999) and several classes of EDAs, such as the Estimation of Bayesian Network Algorithm (EBNA) (Etxeberria and Larrañaga, 1999; Larrañaga and Lozano, 2001), that learn and use Bayesian networks to represent the probability distributions.

Among the three types, IDA is the simplest in terms of both the space and computational complexity. Furthermore, the formula used to update the sampling distributions can be derived explicitly based on the original mutation and selection operators (Leung et al., 1997). However, IDA is inefficient in, if not incapable of at all, capturing and utilizing the interactions among the variables of the fitness functions. This is the primary reason why recent research has focused on FDA and BNA that can represent distributions with richer interaction structures.

The use of distributions with richer correlation structures, however, comes with a cost. First, both FDA and BNA require more space to represent the distribution;

and second, we need to determine the correct distribution that faithfully represents the interaction among the variables in the fitness functions. An incorrect representation might be much worse than the simple distribution of independent products of onedimensional distributions. In this regard, we are in a situation quite similar to those discussed in the famous "no free lunch theorem" (Wolpert and Macready, 1997; Culberson, 1998).

# 3 Additive Functions, Interaction Graphs, and Graphical Models of Sampling Distributions 

In this paper, we use random models of additive fitness functions as our prototype and characterize the space complexity of EDAs by some graph-theory-based measures. In subsection 3.1, we introduce the random models for additive fitness functions. In subsection 3.2, we discuss some graph-theory-based measures that can be used to capture the variable interaction in an additive fitness function. These measures are based on the concept of treewidth. In subsection 3.3, we analyze the probability models used by EDAs to represent the sampling distributions, and identify natural criteria to characterize the space complexity of EDAs.

### 3.1 Random Models for Additive Functions

A fitness function $f: X=\{0,1\}^{n} \rightarrow[0, \infty)$ is additive if it can be represented as a sum of lower dimensional functions

$$
f(x)=\sum_{c \in \mathcal{C}} f_{c}(x), \quad x=\left\{x_{1}, \ldots, x_{n}\right\} \in X
$$

where $\mathcal{C}$ is a collection of subsets of $\left\{x_{1}, \cdots, x_{n}\right\}$. For each $c \in \mathcal{C}, f_{c}(x)$ only depends on the variables in $c$, and is thus called a local fitness function. The order $k$ of an additive fitness function $f$ is the size of the largest variable set in $\mathcal{C}$. Since we can always make the variable sets the same size by merging and/or adding dummy variables, we will assume throughout the rest of the paper that $\mathcal{C}$ consists of variable sets of size $k$. This gives us the uniform additive fitness function of order $k$. Many optimization problems studied over the years can be modelled as a special type of additive fitness functions. Examples include NK landscapes (Kauffman, 1989; Gao and Culberson, 2002; Kallel et al., 2001), the spin-glass model (Martin et al., 2001; Mezard and Parisi, 2003), deceptive functions (Goldberg et al., 1993), constraint satisfaction problems (CSPs) (Braunstein et al., 2003), etc.

Random models of search and optimization problems have been extensively used in the study of the typical behavior of search algorithms and in the generation of benchmark problems for performance evaluation (Cook and Mitchell, 1997; Gent et al., 1999; Martin et al., 2001). To define a random model for additive fitness functions, we need to describe how the variable set of each local fitness function is chosen and how the values of a local fitness function are assigned. Formally, we use

$$
\mathcal{F}(n, k)=\sum_{c \in \mathcal{C}} f_{c}(x)
$$

to denote the random model where

1. $\mathcal{C}$ consists of a collection of subsets of variables selected randomly according to a probability distribution from all the $\binom{n}{k}$ possible subsets of variables; and

2. the fitness values of each local fitness function are assigned randomly and independently according to a distribution on $[0,1]$.

In this paper, we make no specific assumption about the distributions of the fitness value. For the selection of the subsets of variables, we focus on the following random model:
Definition 3.1. The pure random model $\mathcal{F}(n, m, k)$,

$$
\mathcal{F}(n, m, k)=\sum_{c \in \mathcal{C}} f_{c}(x)
$$

is a random additive fitness function where $\mathcal{C}$ consists of $m$ subsets of variables selected randomly without replacement from $\binom{n}{k}$ possible size-k subsets of variables.

Another model that provides a restricted scope of interaction is also of interest for comparison purposes.
Definition 3.2. The neighborhood model $\mathcal{N}(n, k)$ is defined as

$$
\mathcal{N}(n, k)=\sum_{j=1}^{n} f_{j}\left(x_{j}, \Pi\left(x_{j}\right)\right)
$$

where $\Pi\left(x_{j}\right) \subset\left\{x_{i}, 1 \leq i \leq n, i \neq j\right\}$ is the neighborhood of $x_{j}$ with the size $\left|\Pi\left(x_{j}\right)\right|=k-1$.
If the neighborhood $\Pi\left(x_{j}\right)$ is selected randomly without replacement from $\left\{x_{i}, 1 \leq\right.$ $i \leq n, i \neq j\}$, we get the model of NK landscapes with random neighborhoods. If $\Pi\left(x_{j}\right)$ is defined to be $x_{j}$ 's nearest $k-1$ neighboring variables, i.e.,

$$
\Pi\left(x_{i}\right)=\left\{x_{\left(\left(n+i-\frac{k}{2}\right) \bmod n\right)}, \cdots, x_{\left(\left(n+i+\frac{k}{2}\right) \bmod n\right)}\right\}
$$

we get the model of NK landscapes with adjacent neighborhoods. Details about these NK landscape models can be found in (Gao and Culberson, 2002; Gao and Culberson, 2003).

# 3.2 Interaction Graphs of Additive Functions 

The interaction among different variables in a fitness function plays an important role in the study of the typical complexity of optimization problems. In additive functions, the interactions are encoded in the internal structures of the local fitness functions and the relations among the collection of subsets of variables of local fitness functions. These interactions can be represented as an interaction graph.
Definition 3.3. The interaction graph of an additive fitness function

$$
f(x)=\sum_{c \in \mathcal{C}} f_{c}(x), \quad x=\left\{x_{1}, \ldots, x_{n}\right\}
$$

is a graph $G_{f}=G_{f}(V, E)$ where the vertex set $V=\left\{x_{1}, \ldots, x_{n}\right\}$ corresponds to the set of variables, and $\left(x_{i}, x_{j}\right) \in E$ if and only if there is a subset $c \in \mathcal{C}$ such that $x_{i} \in c$ and $x_{j} \in c$.

The interaction graph of an additive fitness function captures all the interactions among the variables. A knowledge about these interactions is critical in understanding the complexity and designing appropriate algorithms to solve the problems. For example, if the interaction graph is a tree, then a linear time algorithm readily exists to solve the problem. As yet another example, if the interaction graph can be decomposed

into several connected components, then a viable approach is to first solve the subproblems represented by the connected components and then combine the obtained partial solutions together.

The concepts of the treewidth and the tree decomposition of a graph generalize the concept of a tree and characterize the degree to which a graph has a tree-like structure (Kloks, 1994). These concepts provide a viable way to characterize the degree of interaction in an optimization problem. We discuss these concepts briefly below and refer interested readers to the works (Bodlaender, 1997; Kloks, 1994; Bouchitt and Todinca, 2001) for more details. The treewidth of a graph can be defined in terms of the $l$-tree.

Definition 3.4. (Kloks, 1994) l-Trees are defined recursively as follows:

1. A clique with $l+1$ vertices is an l-tree;
2. Given an l-tree $T_{n}$ with $n$ vertices, an l-tree with $n+1$ vertices is constructed by adding to $T_{n}$ a new vertex which is made adjacent to an l-clique of $T_{n}$ and non-adjacent to the rest of the vertices.

Definition 3.5. (Kloks, 1994) A graph is called a partial l-tree if it is a subgraph of an l-tree. The treewidth of a graph $G$ is the minimum value $l$ for which $G$ is a partial l-tree.

The treewidth of a graph has an equivalent definition based on the concept of tree decomposition.
Definition 3.6. (Kloks, 1994) A tree decomposition of a graph $G=(V, E)$ is a pair $\mathcal{D}=(\mathcal{S}, \mathcal{T})$ where $\mathcal{S}=\left\{S_{i}, i \in I\right\}$ is a collection of subsets of vertices of $G$ and $\mathcal{T}=(I, F)$ is a tree with one node for each element in $\mathcal{S}$, such that

1. $\bigcup_{i \in I} S_{i}=V$,
2. for all the edges $(v, w) \in E$ there exists a subset $S_{i} \in \mathcal{S}$ such that both $v$ and $w$ are in $S_{i}$, and
3. for each vertex $v \in V$, the set of nodes $\left\{i \in I ; v \in S_{i}\right\}$ forms a subtree of $\mathcal{T}$.

The width of the tree decomposition $\mathcal{D}=(\mathcal{S}, \mathcal{T})$ is $\max _{i \in I}\left(\left|S_{i}\right|-1\right)$. And the treewidth of a graph is the minimum width over all tree decompositions of the graph.

The treewidth has yet another equivalent definition based on the minimum width of a graph and the notion of vertex elimination in a graph. It is also called the induced width in the literature (See, for example, (Dechter, 1999)).
Definition 3.7. Let $G=(V, E)$ be a graph and $\pi=\left(x_{1}, \cdots, x_{n}\right)$ be an ordering of the vertices.

1. The width $w(x, \pi)$ of a vertex $x$ under the ordering $\pi$ is the number of its preceding neighbors. The width $w(\pi)$ of the ordering $\pi$ is the maximum width of all the vertices under the ordering, i.e.,

$$
w(\pi)=\max _{x \in V} w(x, \pi)
$$

2. The induced graph $G(\pi)$ of $G$ under the ordering $\pi$ is obtained by processing the vertices recursively according to the ordering $\pi$ from $x_{n}$ to $x_{1}$. At each step $i$, all the neighbors of $x_{i}$ that precede $x_{i}$ according to $\pi$ are made adjacent and then $x_{i}$ is marked as processed. This process is called the vertex elimination.

3. The induced width $w^{*}(G, \pi)$ of $G$ under the ordering $\pi$ is the width of the induced graph $G(\pi)$ of $G$. The induced width $w^{*}(G)$ of $G$ is the minimum induced width over all the vertex orderings.

Given a graph $G$ and a vertex ordering $\pi$, one can obtain a tree decomposition by (1) forming the induced graph $G(\pi)$; (2) identifying all the (maximum) cliques of $G(\pi)$; and (3) building a tree of this set of cliques in linear time that satisfies all the requirements of a tree decomposition.

In many applications, it is desirable to find a tree decomposition with a minimum width. This problem is NP-complete and has been an interesting research topic in graph theory and artificial intelligence. See, for example, (Bodlaender, 1997; Kloks, 1994; Bouchitt and Todinca, 2001; Becker and Geiger, 1996) and the references therein for more details.
Example 3.1. Figure 1 shows a graph $G(V, E)$ with 5 vertices $(A, B, C, D, E)$ and two of its tree decompositions. The tree decomposition to the right of the graph has a width 2 and the one below the graph has a width 3. The treewidth of the graph is 2.
![img-0.jpeg](img-0.jpeg)

Figure 1: Examples of Tree Decompositions.

Based on the interaction graph, we can measure the degree of the variable interaction in an additive fitness function using the treewidth.
Definition 3.8. Let $f\left(x_{1}, \cdots, x_{n}\right)$ be an additive fitness function with the interaction graph $G_{f}$.

1. The treewidth $\omega(f)$ of $f$ is defined to be the treewidth of $G_{f}$.
2. Given an ordering $\pi$ of the variables, the width $w(f)$ and the induced width $w^{*}(f)$ are defined respectively to be the width and induced width of $G_{f}$ under $\pi$.

# 3.3 Graphical Models for Sampling Distributions of EDAs 

In stochastic search algorithms, new candidates are usually generated according to a sampling distribution. For some algorithms such as standard genetic algorithms and

simulated annealing, the sampling distribution is implicitly defined via random operators, and thus the representation is not an issue. For algorithms like EDAs where the sampling distribution is an explicit component of the algorithm, the representation of the sampling distribution is one of the most critical issues that one has to face. Without any assumptions and knowledge about the optimization problems to be modelled, the only way to represent a distribution on $X=\{0,1\}^{n}$ is to use a probability table of $2^{n}$ cells. This exponential representation is, of course, not a favorable one.

The independent distribution algorithm (IDA) is the simplest in terms of both the space of representation and computational cost. IDA models the sampling distribution as a product of $n$ one-dimensional marginal distributions. However, IDA is inefficient in, if not incapable of, capturing and utilizing the interactions among the variables of the fitness functions. This is the primary reason why recent research has focused on FDA and BNA that can represent distributions with richer interaction structures.

In order to use sampling distributions to capture the knowledge about the interaction and guide the search, the representation of the sampling distribution has to be effective and efficient, which we may summarize as the following two basic requirements:

1. (Effectiveness) The higher the fitness $f(x)$, the higher the probability $p(x)$. This can be formulated as

$$
p(x) \propto f(x)
$$

2. (Space Efficiency) The representation of $p(x)$ should be as efficient as possible. A straightforward representation of $p(x)$ is a probability table of $2^{n}$ cells. This exponential space requirement, however, is not feasible even for a fitness function of moderate dimensions.

To fulfill these requirements, the modelling of the sampling distributions has to utilize the interactions depicted in the interaction graph of the fitness functions. This can be accomplished by using the graphical model developed in the study of probabilistic reasoning and multivariate statistics (Pearl, 1988; Whittaker, 1989).

The concepts of a dependency map and an independency map play important roles in the theory of graphical models. We present these concepts below in the context of interaction graphs of additive functions.
Definition 3.9. Let $f$ be an additive fitness function with the interaction graph $G_{f}(V, E)$ and let $P$ be a probability distribution.

- $G_{f}$ is said to be a dependency map (or D-map) of $P$ if for all disjoint subsets of variables $X, Y, Z$, we have that $X$ and $Y$ are conditionally independent given $Z$ only if $Z$ separates $X$ and $Y$ in $G_{f}$.
- $G_{f}$ is said to be an independency map (or I-map) of $P$ iffor all disjoint subsets of variables $X, Y, Z$, we have that $Z$ separates $X$ and $Y$ in $G_{f}$ only if $X$ and $Y$ are conditionally independent given $Z$;
- $G_{f}$ is a perfect map of $P$ if it is both a D-map and an I-map.

It has been proved that for any graph $G$, there exists a probability distribution $P$ such that $G$ is a perfect map (see Section 3.2.3 of (Pearl, 1988)).

In the following, we will discuss how EDAs model the sampling distributions to capture the variable interactions, paying particular attention to the space complexity.

# The Factorized Distribution Algorithm (FDA) 

FDA directly uses the interaction graph, or an estimated interaction graph, of the additive fitness function to model the sampling distribution (Mühlenbein and Mahnig, 1999). For arbitrary fitness functions of which the exact interaction structure is usually unknown, an estimated interaction graph can also be used. Given an additive fitness function $f$ and its interaction graph $G_{f}=G_{f}(V, E)$ with $V=\left\{x_{1}, \cdots, x_{n}\right\}$, FDA constructs a probability distribution $p(x)$ satisfying

1. $G_{f}$ is an I-map of $p(x)$; and
2. $p(x)$ can be represented as a factorized product of the form

$$
p(x)=\frac{\prod_{S \in \mathcal{S}} p_{S}(x)}{\prod_{S, T \in \mathcal{S}} p_{S \cap T}(x)}
$$

where $\mathcal{S}$ is the collection of subsets of variables in a tree decomposition of $G_{f}$ and $p_{S}(x)$ is the marginal distribution over the subset of variables $S \in \mathcal{S}$.

In the original definition of the FDA (Mühlenbein et al., 1999), the factorized product representation of $p(x)$ can be either approximated or exact. In an approximated factorized product, the collection of subsets $\mathcal{S}$ does not necessarily form a tree decomposition of the interaction graph. For the purpose of investigating the space complexity, we require that the factorization is always exact.

Let $f(x)=\sum_{c \in \mathcal{C}} f_{c}(x)$ be an additive fitness function with $\max _{c \in \mathcal{C}}|c|<k$, i.e., each local fitness function depends on at most $k$ variables. If the collection of subsets of variables, $\mathcal{C}$, satisfies the running intersection property, or equivalently it forms a tree decomposition of the interaction graph, then an exact factorized representation can be built on $\mathcal{C}$ with a space requirement of $O\left(2^{k}\right)$ (Mühlenbein et al., 1999). However, as has also been mentioned in (Mühlenbein et al., 1999), such a class of additive fitness functions is very limited. Otherwise, to get an exact factorized representation, one has to find a tree decomposition of the interaction graph, and the resulting exact factorization will have a space complexity exponential in the width of the tree decomposition. Our analysis in this paper will show that for a random additive fitness function, the space complexity of an exact factorization is exponential in the number of the variables even if the interaction structure of the function is sparse.

Below are a few examples to illustrate the concepts of tree decomposition and the factorized representation of a probability distribution.
Example 3.2. Consider three additive fitness functions defined on the variables $x=$ $\left\{x_{1}, x_{2}, x_{3}, x_{4}\right\}$ :

$$
\begin{aligned}
f_{A}(x) & =f_{1}\left(x_{1}, x_{2}\right)+f_{2}\left(x_{2}, x_{3}\right)+f_{3}\left(x_{3}, x_{4}\right) \\
f_{B}(x) & =f_{1}\left(x_{1}, x_{2}\right)+f_{2}\left(x_{2}, x_{3}\right)+f_{3}\left(x_{3}, x_{4}\right)+f_{4}\left(x_{4}, x_{1}\right) \\
f_{C}(x) & =f_{1}\left(x_{1}, x_{2}, x_{3}\right)+f_{2}\left(x_{1}, x_{2}, x_{4}\right)+f_{3}\left(x_{2}, x_{3}, x_{4}\right)
\end{aligned}
$$

(1) The interaction graph $G$ of $f_{A}$ is simply a path over four vertices

$$
x_{1}-x_{2}-x_{3}-x_{4}
$$

$G$ has a treewidth of 1 and an optimal tree decomposition of $G$ is $\mathcal{T}=$ $\left\{\left(x_{1}, x_{2}\right),\left(x_{2}, x_{3}\right),\left(x_{3}, x_{4}\right)\right\}$. A probability distribution $p(x)$ defined on $G$ can thus be represented as a factorized product of the form

$$
p(x)=\frac{p\left(x_{1}, x_{2}\right) p\left(x_{2}, x_{3}\right) p\left(x_{3}, x_{4}\right)}{p\left(x_{2}\right) p\left(x_{3}\right)}
$$

(2) The interaction graph of $f_{B}$ is a cycle

$$
x_{1}-x_{2}-x_{3}-x_{4}-x_{1}
$$

and has a treewidth 2. A tree decomposition is

$$
\mathcal{T}=\left\{\left(x_{1}, x_{2}, x_{4}\right),\left(x_{2}, x_{3}, x_{4}\right)\right\}
$$

and a probability distribution defined on the interaction graph can be represented as a factorized product of the form

$$
p(x)=\frac{p\left(x_{1}, x_{2}, x_{4}\right) p\left(x_{2}, x_{3}, x_{4}\right)}{p\left(x_{2}, x_{4}\right)}
$$

(3) The interaction graph is a 4-clique. Its treewidth is three with the only possible tree decomposition $\mathcal{T}=\left\{\left(x_{1}, x_{2}, x_{3}, x_{4}\right)\right\}$, and consequently, the only possible factorized representation of a probability distribution $p(x)$ is

$$
p(x)=p\left(x_{1}, x_{2}, x_{3}, x_{4}\right)
$$

For the function $f_{A}(x)$, the factorized representation of $p(x)$ truthfully reflects the conditional independence in the interaction graph. For the function $f_{B}(x)$, the best factorized distribution one can have only partially reflects the conditional independence in the interaction graph. Also, for $f_{B}(x)$, we need to use three-dimensional distributions, while for $f_{A}(x)$, two-dimensional distributions are enough. For $f_{C}(x)$, there is no conditional independence available and one is forced to represent a distribution by enumerating the probability of each possible configuration of the variables.

The space complexity of FDAs depends exponentially on the width of the tree decomposition used in the factorized representation of $p(x)$. Recall that the width of a tree decomposition is defined as $\max _{S \in \mathcal{S}}(|S|-1)$ where $\mathcal{S}$ is the collection of subsets of variables in the tree decomposition. This is because FDAs need $\Omega\left(2^{|S|}\right)$ space to represent each factorized component $p_{S}(x)$. For an interaction graph, there are many different tree decompositions with different width, and the treewidth of the interaction graph is defined to be the minimum of the width of different tree decompositions. It follows that the space complexity of an FDA is exponential in the treewidth of the interaction graph. Therefore, we can have
Definition 3.10. The space complexity $F_{f}$ of an FDA for an additive function $f$ is defined to be

$$
F_{f}=2^{\omega(f)}
$$

where $\omega(f)$ is the treewidth of $f$ as in Definition 3.8.

# Bayesian network-based algorithm (BNA) 

BNA models the sampling distribution by a Bayesian network (Larrañaga et al., 2000; Pelikan et al., 1999). A Bayesian network is a directed acyclic graph $B=B(V, E)$ where $V$ corresponds to the set of variables and a directed edge from $x_{i}$ to $x_{j}$ indicates

that the variable $x_{j}$ depends on the variable $x_{i}$ (Pearl, 1988). In order to identify an appropriate complexity measure for BNAs, we need to formalize the notion of Bayesian networks that can be used to capture the variable interaction in an additive fitness function.

Let us start with the concept of $d$-separation in a directed graph.
Definition 3.11. (Section 3.3.1, (Pearl, 1988)) Let $X, Y$, and $Z$ be three disjoint subsets of vertices in a directed acyclic graph $D . Z$ is said to d-separate $X$ from $Y$ if along every undirected path between a vertex in $X$ and a vertex in $Y$, there is a vertex $w$ satisfying one of the following two conditions: (1) $w$ has converging edges, i.e., edges on the path that meet head-to-head at $w$, and none of $w$ or its descendants are in $Z$, or (2) $w$ does not have converging edges and $w$ is in $Z$.

A directed acyclic graph $B=B(V, E)$ is called an I-map of a probability distribution $P$ if for any disjoint subsets of variables $X, Y, Z$, the d-separation of $X$ and $Y$ by $Z$ in the graph $B(V, E)$ implies the conditional independence of $X$ and $Y$ given $Z$. A directed acyclic graph is a minimal I-map if no edge can be deleted without destroying the I-mapness.
Definition 3.12. Let $f$ be an additive fitness function with the interaction graph $G_{f}(V, E)$ and let $P_{f}$ be the probability distribution such that $G_{f}$ is a perfect-map of $P_{f}$. A directed acyclic graph $B$ is called a Bayesian network for $f$ if it is a minimal I-map of $P_{f}$.

The following theorem shows how to construct a Bayesian network under a given variable ordering $\pi=\left(x_{1}, \cdots, x_{n}\right)$. Let $G_{f}$ be the interaction graph of $f$ and let $U_{i}(\pi)=$ $\left(x_{1}, \cdots, x_{i-1}\right)$. A Markov boundary $B_{i}(\pi)$ of $x_{i}$ with respect to $U_{i}(\pi)$ is a minimal subset such that (1) $B_{i}(\pi) \subset U_{i}(\pi)$; and (2) $B_{i}(\pi)$ separates $x_{i}$ and $U_{i}(\pi) \backslash B_{i}(\pi)$ in $G_{f}$ (Pearl, 1988).
Theorem 3.1. (Section 3.3.1, (Pearl, 1988)) Let $G_{f}=G_{f}(V, E)$ be an interaction graph of an additive fitness function $f(x)$. For each $i \geq 1$, let $B_{i}(\pi)$ be a Markov boundary of $x_{i}$ with respect to $U_{i}(\pi)$. Then the directed acyclic graph specified by the parent sets

$$
P a\left(x_{i}\right)=B_{i}(\pi), \quad i \geq 1
$$

is a Bayesian network of $f$. Furthermore, if the probability distribution $P_{f}$ is strictly positive, then the Bayesian network given above is unique under $\pi$.

From Theorem 3.1, we can see that for a given ordering of variables, there is a unique Bayesian network that captures the conditional independence depicted in the interaction graph of the fitness function. To represent this Bayesian network, we need a table for each variable $x_{i}$ to store the conditional probabilities $P\left(x_{i} \mid P a\left(x_{i}\right)\right)$. It follows that the space complexity to represent this Bayesian network is $\Omega\left(\max _{i}\left|B_{i}(\pi)\right|\right)$.

Similar to the case of the treewidth in FDA, there are many different orderings of the variables, each of which gives us a different value of $\max \left(\left|B_{i}(\pi)\right|\right)$. Since a Bayesian network is a minimal I-map, we may define the space complexity of BNAs using $\max _{i}\left|B_{i}(\pi)\right|$.

Definition 3.13. The space complexity $B_{f}$ of a BNA for a given additive function $f$ is defined as

$$
B_{f}=2^{\bar{w}(f)}
$$

where $\bar{w}(f)=\min _{\pi} \max _{1 \leq i \leq n}\left|B_{i}(\pi)\right|$ and $B_{i}(\pi)$ is the Markov boundary of $x_{i}$ under the ordering $\pi$.

It should be mentioned that the above definition of space complexity of BNAs is based on the assumption that Bayesian networks in a BNA are constructed to reflect the exact conditional independence in a fitness function, and we do not consider the situations where BNAs use some machine learning procedures to construct an approximating Bayesian network with less space requirement.
Example 3.3. Consider the additive fitness function

$$
f(x)=f_{a}\left(x_{1}, x_{2}\right)+f_{b}\left(x_{1}, x_{3}\right)+f_{c}\left(x_{2}, x_{4}\right)+f_{d}\left(x_{3}, x_{4}\right)
$$

Its interaction graph $G_{f}$ is a cycle $x_{1}-x_{2}-x_{4}-x_{3}-x_{1}$. According to Theorem 3.1, the Bayesian network for the variable ordering $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$ is shown in Figure 2(a). The Bayesian network in Figure 2(b) is not the true Bayesian network of $f$ because it encodes the conditional independency of $x_{3}$ and $x_{2}$ given $x_{1}$ alone, which is not specified in the interaction graph of $f$. Of course, it is highly possible that BNAs with some machine-learning mechanisms may construct the Bayesian network of Figure 2(b).
![img-1.jpeg](img-1.jpeg)

Figure 2: Examples of Bayesian networks of an additive fitness function.

In the next section, we will investigate the space complexity of FDAs and BNAs by evaluating the size of the treewidth and minimum width of random additive functions. We close this section by providing a discussion to justify why EDAs have to truthfully encode the interaction structures in the interaction graph. For a given additive fitness function $f: X=\{0,1\}^{n} \rightarrow[0,1]$, consider the following Boltzman-like distribution

$$
p_{f}(x)=\frac{1}{Z} \exp (f(x)), \quad Z=\int_{X} \exp (f(x)) d x
$$

Distributions similar to $p_{f}(x)$ are the building blocks in many studies of search and optimization problems. Concrete examples include the statistical physics approach, the simulated annealing algorithm, and some selection schemes in genetic algorithms (Mezard and Parisi, 2003; Goldberg, 1989; Kirkpatrick et al., 1983). It turns out that this distribution exactly encodes the interaction structures in the interaction graph.
Theorem 3.2. Let $f(x)$ be an additive fitness function with the associated interaction graph $G_{f}=G_{f}(V, E)$. Then, variables $x_{i}$ and $x_{j}$ are not adjacent in $G_{f}$ if and only if the two corresponding variables in the distribution $p_{f}(x)$ are conditionally independent given the rest of the variables.

Proof. Two variables $x_{i}$ and $x_{j}$ are not adjacent in $G_{f}$ if and only if they do not appear in a local fitness function at the same time. Let

$$
f(x)=\sum_{c \in \mathcal{C}} f_{c}(x)
$$

and let $\mathcal{C}_{1}$ be the set of variable sets that contain the variable $x_{j}$. Then, $x_{i}$ and $x_{j}$ are not adjacent if and only if $x_{i}$ does not appear in any local fitness functions indexed by $\mathcal{C}_{1}$. The result follows because two components $x_{i}$ and $x_{j}$ are conditionally independent if and only if $p_{f}(x)$ can be written as $g\left(x_{i}, y\right) * h\left(x_{j}, y\right)$ where $y=\left\{x_{1}, \cdots, x_{n}\right\} \backslash\left\{x_{i}, x_{j}\right\}$.

In (Mühlenbein et al., 1999), a factorization theorem for Boltzmann distributions is proved ${ }^{1}$. The above Theorem 3.2 is slightly different and serves a different purpose-to demonstrate why it is important to capture the independency depicted in the interaction graph.

# 4 Space Complexity of EDAs 

In this section, we study the space complexity of three variants of EDAs using random additive functions as our prototypical model. As we have discussed in Section 3.3, the space complexity of FDAs and BNAs are characterized by some graph-theory-based measures. We will focus on how these measures are related to the degree of interaction of the additive fitness functions. Let us start with the simplest case of the independent distribution algorithm (IDA).
Theorem 4.1. For any fitness function, the independent distribution algorithm (IDA) has a space complexity $O(n)$.

Proof. This is true because for IDAs, one only needs to represent $n$ one-dimensional marginal distributions.

For the NK landscape model with adjacent neighborhoods, we have the following results.
Theorem 4.2. Let $f(x)$ be an instance of the neighborhood model with adjacent neighborhood $\mathcal{N}(n, k)$. Then, the space complexity of FDA is $F_{f}=2^{\Theta(k)}$.

Proof. Since the interaction graph $f$ has cliques of size $k+1$, its treewidth should be no less than $k$. We prove the theorem by constructing a tree decomposition with a treewidth $2 k$. Let $V=\left\{x_{1}, \cdots, x_{n}\right\}$ be the set of vertices, and let $V_{0}=\left\{x_{1}, \cdots, x_{k}\right\}$. We construct $S=\left\{X_{i}, i \geq 1\right\}$, a collection of subsets of the variables, as follows:

$$
\begin{aligned}
X_{1}= & \left\{x_{1}, \cdots, x_{k+1}\right\} \cup V_{0} \\
X_{2}= & \left\{x_{2}, \cdots, x_{k+2}\right\} \cup V_{0} \\
& \cdots \\
X_{N-k}= & \left\{x_{N-k}, \cdots, x_{N}\right\} \cup V_{0} \\
X_{N-k+1}= & \left\{x_{N-k+1}, \cdots, x_{N}, x_{1}\right\} \cup V_{0} \\
X_{N-k+2}= & \left\{x_{N-k+2}, \cdots, x_{N}, x_{1}, x_{2}\right\} \cup V_{0} \\
& \cdots \\
X_{N}= & \left\{x_{N}, x_{1}, x_{2}, \cdots, x_{k}\right\} \cup V_{0}
\end{aligned}
$$

[^0]
[^0]:    ${ }^{1}$ We thank one of the referees for pointing out this paper and the theorem.

and define a tree structure on $S$ by assigning an edge between each of the pairs $\left(X_{i}, X_{i+1}\right), 1 \leq i \leq N-1$. It is easy to verify that the collection of subsets of variables and the tree structure specified in the above form a tree decomposition with a width $2 k$.

To investigate the space complexity of FDAs for NK landscapes with random neighborhoods and pure random model for additive fitness functions, we need some results from the study of treewidth.

In (Kloks, 1994), it is shown that a necessary condition for a graph to have a treewidth at most $l$ is that the graph has a balanced $l$-partition. We only give the definition of balanced $l$-partitions. The establishment of the necessary condition can be found in (Kloks, 1994).
Definition 4.1. (Kloks, 1994) Let $G(V, E)$ be a graph with $|V|=n$. A partition $(S, A, B)$ of $V$ is a balanced l-partition if the following conditions are satisfied:

1. $|S|=l+1$;
2. $\frac{1}{3}(n-l-1) \leq|A|,|B| \leq \frac{2}{3}(n-l-1)$; and
3. $S$ separates $A$ and $B$, i.e., there are no edges between vertices of $A$ and vertices of $B$.

The theorem below deals with the space complexity of an FDA for NK landscapes with random neighborhoods.
Theorem 4.3. Let $f(x)$ be an instance of the neighborhood model with random neighborhood $\mathcal{N}(n, k)$. Then, with probability asymptotic to 1 , the space complexity of $F D A$ is $F_{f}=2^{\Omega(n)}$.

Proof. Similar to the proof of Theorem 4.4, and can be found in (Gao and Culberson, 2003).

For the more general random models of additive functions, we have
Theorem 4.4. Let $f(x)$ be an instance of the pure random model $\mathcal{F}(n, m, k)$. Then, with probability asymptotic to 1 , the space complexity $F_{f}$ of $F D A$ is $2^{\Omega(n)}$ if $\frac{m}{n}>\frac{\ln 2}{k \ln 3-\ln \left(1+2^{\epsilon}\right)}$, i.e., $\frac{m}{n}>\frac{\epsilon}{k}$ for a constant $\epsilon>0$.

Proof. Let $G_{f}=G_{f}(V, E)$ be the interaction graph of $f(x)$ and $\omega(f)$ be the treewidth of the interaction graph $G$. We prove that there is a $0<\delta<1$ such that

$$
\lim _{n} \operatorname{Pr}\{\omega(f) \leq \delta n\}=0
$$

From (Kloks, 1994), a necessary condition for a graph to have a treewidth at most $l$ is that the graph must have a balanced $l$-partition. Let $\mathcal{P}$ be the set of all the $l$-partitions of the vertex set $V$ that satisfies the first two conditions of the definition of balanced partition (Definition 4.1). For a given $P=(S, A, B) \in \mathcal{P}$, define a random variable $I_{P}$ as follows:

$$
I_{P}= \begin{cases}1, & \text { if } P \text { is a balanced partition } \\ 0, & \text { otherwise }\end{cases}
$$

Note that $I_{P}=1$ if and only if there are no edges between vertices in $A$ and vertices in $B$ in the interaction graph $G_{f}$.

Let $N=\binom{n}{k}$ be the number of possible subsets of variables for local fitness functions of size $k$, and let $N_{P}$ be the number of possible local fitness functions whose $k$ defining variables are either in $A \bigcup S$ or in $B \bigcup S$. Let $a=|A|$, we have

$$
\begin{aligned}
N_{P} & =\binom{a+l+1}{k}+\binom{n-a}{k}-\binom{l+1}{k} \\
& \leq\binom{a+l+1}{k}+\binom{n-a}{k}
\end{aligned}
$$

and thus,

$$
\begin{aligned}
\frac{N_{p}}{N} & \leq \frac{(a+l+1) \cdots(a+l+1-k+1)}{n(n-1) \cdots(n-k+1)} \\
& +\frac{(n-a) \cdots(n-a-k+1)}{n(n-1) \cdots(n-k+1)} \\
& \leq\left(\frac{a+l+1}{n}\right)^{k}+\left(\frac{n-a}{n}\right)^{k} \\
& =\frac{(a+l+1)^{k}+(n-a)^{k}}{n^{k}}
\end{aligned}
$$

Write $y=\frac{l+1}{n}$ and consider the function $h(a)=(a+l+1)^{k}+(n-a)^{k}$ defined on the interval

$$
\left[\frac{1}{3}(n-l-1), \frac{2}{3}(n-l-1)\right]
$$

Since $h^{\prime}(a)=0$ at $a=\frac{1}{2} n(1-y)$. If $y=\frac{l+1}{n}$ is sufficiently small, then, $h(a)$ is maximized at $a=\frac{1}{3}(n-l-1)$. Therefore, we have

$$
\begin{aligned}
\frac{N_{p}}{N} & \leq \frac{1}{n^{k}}\left(\left(\frac{1}{3} n+l+1\right)^{k}+\left(\frac{2}{3} n+l+1\right)^{k}\right) \\
& =\left(\frac{1}{3}\right)^{k}(1+3 y)^{k}+\left(\frac{2}{3}\right)^{k}\left(1+\frac{3}{2} y\right)^{k} \\
& \leq\left(\left(\frac{1}{3}\right)^{k}+\left(\frac{2}{3}\right)^{k}\right)(1+3 y)^{k}
\end{aligned}
$$

It follows that

$$
E\left\{I_{P}\right\} \leq \frac{\binom{N_{P}}{m}}{\binom{N}{m}} \leq\left(\left(\frac{1}{3}\right)^{k}+\left(\frac{2}{3}\right)^{k}\right)^{m}(1+3 y)^{k m}
$$

Let $I=\sum_{P \in \mathcal{P}} I_{P}$. By its definition, we have

$$
\begin{aligned}
|\mathcal{P}|= & \binom{n}{l+1} \sum_{\frac{1}{3}(n-l-1) \leq a \leq \frac{2}{3}(n-l-1)}\binom{n-l-1}{a} \\
& \leq\binom{n}{l+1} 2^{n}
\end{aligned}
$$

It follows that the expectation of $I$ satisfies

$$
\begin{aligned}
& E\{I\}=\sum_{P \in \mathcal{P}} E\left\{I_{P}\right\} \\
& \leq\binom{ n}{l+1} 2^{n}\left(\left(\frac{1}{3}\right)^{k}+\left(\frac{2}{3}\right)^{k}\right)^{m}(1+3 y)^{k m}
\end{aligned}
$$

Recall that $0<y=\frac{l+1}{n}<1$. We obtain from Stirling's formula that

$$
\binom{n}{l+1} \sim \frac{1}{\sqrt{2 \pi y(1-y) n}}\left(\frac{1}{y^{y}(1-y)^{1-y}}\right)^{n}
$$

And hence,

$$
\begin{aligned}
E\{I\} \leq & \frac{1}{\sqrt{2 \pi y(1-y) n}}\left(\frac{2}{y^{y}(1-y)^{1-y}}\right)^{n} \\
& \cdot\left(\left(\frac{1}{3}\right)^{k}+\left(\frac{2}{3}\right)^{k}\right)^{m}(1+3 y)^{k m}
\end{aligned}
$$

Notice that

$$
\lim _{y \rightarrow 0} \frac{2}{y^{y}(1-y)^{1-y}}=2
$$

For any $\frac{m}{n}>c$ with $c$ satisfying

$$
\left(\left(\frac{1}{3}\right)^{k}+\left(\frac{2}{3}\right)^{k}\right)^{c}<\frac{1}{2}
$$

let $y=\frac{l+1}{n}$ be small enough so that

$$
\frac{2}{y^{y}(1-y)^{1-y}}\left(\left(\frac{1}{3}\right)^{k}+\left(\frac{2}{3}\right)^{k}\right)^{c}(1+3 y)^{k c}<1
$$

and let $\delta=y$, we have

$$
\begin{aligned}
\lim _{n} \operatorname{Pr}\{\omega(f) \leq \delta n\} & \leq \lim _{n} \operatorname{Pr}\{I>0\} \\
& \leq \lim _{n} E[I]=0
\end{aligned}
$$

that is, (14) is true. The theorem is proved.
For the space complexity of BNAs, we need to evaluate the value of $\bar{w}(f)$ (see Definition 3.13). We show in the following that $\bar{w}(f)$ is actually equal to the induced width $w^{*}(f)$ of $f$, and consequently the treewidth of $f$.

First, we establish two lemmas on the induced width of a general graph. Let $G=$ $G(V, E)$ be a graph and $\pi=\left(x_{1}, \cdots, x_{n}\right)$ be an ordering of the vertices. For each $1 \leq$ $i \leq n$, define

$$
\begin{gathered}
A_{i}=\left\{x_{j} ; x_{j} \text { is adjacent to } x_{i}, \quad 1 \leq j<i\right\} \\
C_{i}=\left\{x_{j} ;\right. \text { There is a path } x_{i} x_{i_{1}} \cdots x_{i_{k}} x_{j} \\
\text { s.t. }\left\{x_{i_{1}}, \cdots, x_{i_{k}}\right\} \subset\left\{x_{i+1}, \cdots, x_{n}\right\}, \quad 1 \leq j<i\}
\end{gathered}
$$

and let $B_{i}=A_{i} \cup C_{i}$.

Lemma 4.1. For each $1 \leq i \leq n, B_{i}$ separates $x_{i}$ and $\left\{x_{1}, \cdots, x_{i-1}\right\} \backslash B_{i}$ and is minimal with respect to $\left\{x_{1}, \cdots, x_{i-1}\right\}$.
Proof. For any $x_{m} \in\left\{x_{1}, \cdots, x_{i-1}\right\} \backslash B_{i}$, let $x_{i} x_{i_{1}} \cdots x_{i_{k}} x_{m}$ be a path connecting $x_{i}$ and $x_{m}$. Assume $x_{i_{p}}$ is the first variable in $\left\{x_{i_{1}}, \cdots, x_{i_{k}}\right\}$ that belongs to $\left\{x_{1}, \cdots, x_{i-1}\right\}$. If $p=1$, then $x_{i_{p}} \in A_{i}$; Otherwise, $x_{i_{p}} \in C_{i}$. It follows that $B_{i}$ separates $x_{i}$ and $\left\{x_{1}, \cdots, x_{i-1}\right\} \backslash B_{i}$ in the graph $G$. Since removing any vertex $x$ from $B_{i}$ will either make $x$ directly adjacent to $x_{i}$, or leave a path that connects $x_{i}$ and $x$, but does not pass through $\left\{x_{1}, \cdots, x_{i-1}\right\}, B_{i}$ is minimal.

Lemma 4.2. Let $w^{*}(G, \pi)$ be the induced width of $G$ under the ordering $\pi$, then

$$
\max _{1 \leq i \leq n}\left|B_{i}\right|=w^{*}(G, \pi)
$$

Proof. Let $G_{i}(\pi)$ be the graph after $\left(x_{i+1}, \cdots, x_{n}\right)$ have been eliminated, and let $N_{i}$ be the set of neighbors of $x_{i}$ in $G_{i}(\pi)$. We prove that $N_{i}=B_{i}$.

By the definition, we have $A_{i} \subset N_{i}$ and $C_{i} \subset N_{i}$, and consequently $B_{i} \subset N_{i}$. To establish the opposite inclusion, consider a variable $x \in N_{i}$. If $x$ is adjacent to $x_{i}$ in $G$, then $x \in A_{i}$; Otherwise, there must be a $j>i$ such that $x \in N_{j}$ and $x_{i} \in N_{j}$. Based on this fact and by induction on $i$, we can show that there is a path $x_{i} x_{i_{1}} \cdots x_{i_{k}} x$ such that $\left\{x_{i_{1}}, \cdots, x_{i_{k}}\right\} \subset\left\{x_{i+1}, \cdots, x_{n}\right\}$. It follows that $x \in C_{i}$.

Based on the above two lemmas, we have the following result, showing that the space complexity of BNAs is also exponential in the treewidth.
Theorem 4.5. For any additive fitness function $f$ and a perfect map $P_{f}$ of $G_{f}$ that is strictly positive, $\bar{w}(f)=\min _{\pi} \max _{1 \leq i \leq n}\left|B_{i}(\pi)\right|$, as defined in Definition 3.13, is equal to the treewidth of $f$.

Proof. Let $\pi$ be a variable ordering and $B(V, E)$ be the unique Bayesian network with $\operatorname{Pa}\left(x_{i}\right)=B_{i}(\pi)$ as given in Theorem 3.1. Based on the above two lemmas, we have $\max _{1 \leq i \leq n}\left|B_{i}(\pi)\right|$ is equal to the induced width $w^{*}(f, \pi)$. Taking the minimum over all the variable orderings completes the proof.

From the above result and similar to the proof of Theorem 4.4, we have
Theorem 4.6. Let $f(x)$ be an instance of the pure random model $\mathcal{F}(n, m, k)$. Then, with probability asymptotic to 1 , the space complexity $B_{f}$ of BNA is $2^{\mathrm{fl}(n)}$ if $\frac{m}{n}>\frac{\ln 2}{k \ln 3-\ln \left(1+2^{\epsilon}\right)}$, i.e., $\frac{m}{n}>\frac{\epsilon}{k}$ for a constant $\epsilon>0$.

# 5 Conclusions 

In this paper, we have discussed in detail the space complexity of two typical implementation schemes of the estimation of distribution algorithm. We identified criteria to characterize the space complexity of these implementations. Using random additive functions as our prototype, we prove that the space complexities of the factorized distribution algorithm and the Bayesian optimization algorithm are both exponential in the problem size even if the optimization problem has a very sparse interaction structure.

Our results should not be viewed as purely negative results. Similar to what has been shown in a related work on the tractability of constraint satisfaction and Bayesian network inference problems (Gao, 2003), results presented in the current paper only indicate that EDAs have their limitations and only work well in a part of the problem space where the interaction structure (i.e., the linkage structure) has a bounded

treewidth. In the literature, there have been many studies that emphasize the importance of linkage in the design of efficient genetic algorithms (Heckendorn and Wright, 2003; Yu and Goldberg, 2004). It would be interesting to further investigate the relations between the treewidth of interaction structures and the efficiency of general genetic algorithms that make use of linkage-identification methods.

The analysis in the current paper is based on pure random models of additive fitness functions. Similar random models have also been widely used in the recent study of the typical complexity and phase transitions of NP-complete problems (Kirkpatrick and Selman, 1994; Cook and Mitchell, 1997; Martin et al., 2001). In the past several years, it has been found that many real-world interaction structures such as the Internet and gene interaction can be better modelled as power-law random graphs (Dorogovtsev and Mendes, 2002). It is interesting to investigate the treewidth in these power-law graphs and to identify situations where the interaction graph of an optimization problem follows the power-law distribution. Also, for many real-world optimization problems, the interaction structure is actually unknown, and identifying these unknown interaction structures is also an interesting research topic (Heckendorn and Wright, 2003).

# Acknowledgments 

We thank the anonymous reviewers for their valuable comments.
