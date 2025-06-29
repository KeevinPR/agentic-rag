# Global Optimization with the Gaussian Polytree EDA 

Ignacio Segovia Domínguez, Arturo Hernández Aguirre, and Enrique Villa Diharce<br>Center for Research in Mathematics<br>Guanajuato, México<br>\{ijsegoviad,artha, villadi\}@cimat.mx


#### Abstract

This paper introduces the Gaussian polytree estimation of distribution algorithm, a new construction method, and its application to estimation of distribution algorithms in continuous variables. The variables are assumed to be Gaussian. The construction of the tree and the edges orientation algorithm are based on information theoretic concepts such as mutual information and conditional mutual information. The proposed Gaussian polytree estimation of distribution algorithm is applied to a set of benchmark functions. The experimental results show that the approach is robust, comparisons are provided.


Keywords: Polytrees, Estimation of Distribution Algorithm, Optimization.

## 1 Introduction

The polytree ia a graphical model with wide applications in artificial intelligence. For instance, in belief networks the polytrees are the de-facto graph because they support probabilistic inference in linear time [13. Other applications make use of polytrees in a rather similar way, that is, polytrees are frequently used to model the joint probability distribution (JPD) of some data. Such JPD is also called a factorized distribution because the tree encodes a joint probability as a product of conditional distributions.

In this paper we are concerned with the use of polytrees and their construction and simulation algorithms. Further more, we asses the improvement that polytrees bring to the performance of Estimation of Distribution Algorithms (EDAs). As mentioned the polytree graphs have been applied by J. Pearl to belief networks [13], but also Acid and de Campos researched them in causal networks [1], 14. More recently, M. Soto applied polytrees to model distributions in EDAs and came up with the polytree approximation distribution algorithm, known as PADA [11. However, note that in all the mentioned approaches the variables are binary. The goal of this paper is to introduce the polytree for continuous variables, that is, a polytree in continuous domain with Gaussian variables and its application to EDAs for optimization. The proposed approach is called the Gaussian Polytree EDA. Polytrees with continuous variables have been studied

by Ouerd [12], 9]. In this paper we extend a poster presented [16] and we further develop the work of Ouerd [12]. We introduce two new algorithmic features to the gaussian polytree: 1) a new orientation principle based on conditional mutual information. We also prove that our approach is correct, 2) overfitting control of the model through a comparison of conditional and marginal mutual information strengths. The determination of the threshold value is also explained.

This paper is organized as follows. Section 2 describes two polytree algorithms in discrete variables; Section 3 explains how to build a Gaussian polytree while Section 4 provides the implementation details. Section 5 describes two sets of experiments and provides a comparison with other related approaches. Section 6 provides the conclusions and lines of future research.

# 2 Related Work 

A polytree is a directed acyclic graph (DAG) with no loops when the edges are undirected (only one path between any two nodes) [6, 8]. For binary variables the polytree approximation distribution algorithm (PADA) is the first work to propose the use of polytrees in estimation distribution algorithm [11]. The construction algorithm of PADA uses (marginal) mutual information and conditional mutual information as a measure of the dependency. Thus, a node $X_{k}$ is made head to head whenever the conditional mutual information $\operatorname{CMI}\left(X_{i}, X_{j} \mid X_{k}\right)$ is greater than the marginal mutual information $M I\left(X_{i}, X_{j}\right)$ ). Thus, the head to head node means that the information shared by two nodes $X_{i}, X_{j}$ increases when the third node $X_{k}$ is included. For overfitting control two parameters $\epsilon_{1}, \epsilon_{2}$ aim to filter out the (weak) dependencies. However no recommendations about how to set these parameters is given in the PADA literature.

A Gaussian polytree is a factorized representation of a multivariate normal distribution [10, 4]. Its JPDF is a product of Gaussian conditional probabilites times the product of the probabilities of the root nodes $(R)$, as follows: $\operatorname{JPDF}\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{\forall i \in R} P\left(X_{i}\right) \prod_{\forall j \notin R} P\left(X_{j} \mid p a\left(X_{j}\right)\right)$. A recent approach uses a depth first search algorithm for edge orientation [9]. Based on the previous work of Rebane and Pearl [15, 13], Ouerd at al. assume that a Chow \& Liu algorithm is ran to deliver a dependence tree from the data 9]. Then they propose to orient the edges by traversing the dependence tree in a depth first search order. Articulation points and causal basins must be detected first. With their approach they try to solve four issues (not completely solved by Rebane and Pearl) such as how to traverse the tree, and what to do with the edges already traversed. For edge orientation their algorithm performs a marginal independence test on the parents $X$ and $Y$ of a node $Z$ to decide if $Z$ has $X$ and $Y$ as parents. If they are independent the node $Z$ is a head to head node.

## 3 Building the Gaussian Polytree

In the following we describe the main steps needed to construct a Gaussian polytree.

1. The Gaussian Chow \& Liu tree. The first step to construct a Gaussian polytree is to construct a Gaussian Chow $\mathcal{G}$ Liu dependence tree (we use the same approach of the binary dependence tree of Chow \& Liu [3). Recall mutual information is the measure to estimate dependencies in Chow \& Liu algorithm. The algorithm randomly chooses a node and declares it the root. Then the Kruskal algorithm is used to create a maximum weight spanning tree. The tree thus created maximizes the total mutual information, and it is the best approximation to the true distribution of the data whenever that distribution comes from a tree like factorization. A Gaussian Chow \& Liu tree is created in a way similar to the discrete variables case. Mutual information is also the maximum likelihood estimator, and whenever a multivariate normal distribution is factorized as the product of second order distributions the Gaussian Chow \& Liu tree is the best approximation. For normal variables, mutual information is defined as:

$$
M I(X, Y)=-\frac{1}{2} \log \left(1-r_{x, y}^{2}\right)
$$

The term $r_{x, y}$ is the Pearson's correlation coefficient which for Gaussian variables is defined as:

$$
r_{x, y}=\frac{\operatorname{cov}(x, y)}{\sigma_{x} \sigma_{y}}
$$

2. Edge orientation. The procedure to orient the edges of the tree is based on the orienting principle [15]: if in a triplet $X-Z-Y$ the variables $X$ and $Y$ are independent then $Z$ is a head to head node with $X$ and $Y$ as parents, as follows: $X \rightarrow Z \leftarrow Y$. Similarly, if in a triplet $X \rightarrow Z-Y$ the variables $X$ and $Y$ are independent then $Z$ is a head to head node with $X$ and $Y$ as parents: $X \rightarrow Z \leftarrow Y$; otherwise $Z$ is the parent of $Y: X \rightarrow Z \rightarrow Y$.
In this paper we propose information theoretic measures such a conditional mutual information (CMI) and (marginal) mutual information (MI) to estimate the dependency between variables.
Proposed orientation based on information measures: for any triplet $X-Z-Y$, if $\operatorname{CMI}(X, Y \mid Z)>M I(X, Y)$ then $Z$ is a head to head node with $X$ and $Y$ as parents, as follows: $X \rightarrow Z \leftarrow Y$.
Proof. We shall prove that the proposed measure based on mutual information finds the correct orientation. That is, (in Figure 1 the four possible models made with three variables are shown), model $M_{4}$, head to head, is the correct one for $\operatorname{CMI}(X, Y \mid Z)>M I(X, Y)$.
The quality of the causal models shown in the Figure 1 can be expressed by its log-likelihood. If the parents of any node $X_{i}$ is the set of nodes $p a\left(X_{i}\right)$, the negative of the log-likelihood of a model $M$ is [5]:

$$
-l l(M)=\sum_{i=1}^{n} H\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

where $H\left(X_{i} \mid p a\left(X_{i}\right)\right)$ is the conditional entropy of $X_{i}$ given its parents $p a\left(X_{i}\right)$. It is well known that the causal models $M_{1}, M_{2}$ and $M_{3}$ are equivalent,

![img-0.jpeg](img-0.jpeg)

Fig. 1. The causal models that can be obtained with three variables $X, Y$ y $Z$. (a) Model $M_{1}$. (b) Model $M_{2}$. (c) Model $M_{3}$. (d) Model $M_{4}$.
or indistinguishable in probability [15]. The negative log-likelihood are the Equations 4, 5 and 6 , respectively.

$$
\begin{aligned}
-l l\left(M_{1}\right)= & H(X)+H(Z \mid X)+H(Y \mid Z) \\
= & H(X, Z)+H(Y, Z)-H(Z) \\
& -H(X, Y, Z)+H(X, Y, Z) \\
= & H(X, Y, Z)+C M I(X, Y \mid Z) \\
-l l\left(M_{2}\right)= & H(Z)+H(X \mid Z)+H(Y \mid Z) \\
= & H(X, Z)+H(Y, Z)-H(Z) \\
& +H(X, Y, Z)-H(X, Y, Z) \\
= & H(X, Y, Z)+C M I(X, Y \mid Z) \\
-l l\left(M_{3}\right)= & H(Y)+H(Z \mid Y)+H(X \mid Z) \\
= & H(X, Z)+H(Y, Z)-H(Z) \\
& -H(X, Y, Z)+H(X, Y, Z) \\
= & H(X, Y, Z)+C M I(X, Y \mid Z)
\end{aligned}
$$

For the head to head model $\left(M_{4}\right)$, the negative of the log-likelihood is Equation 7.

$$
\begin{aligned}
-l l\left(M_{4}\right) & =H(X)+H(Y)+H(Z \mid X, Y) \\
& =H(X)+H(Y)+H(X, Y, Z)-H(X, Y) \\
& =H(X, Y, Z)+M I(X, Y)
\end{aligned}
$$

The best model is that one with the smallest negative log-likelihood or smallest summation of conditional entropy. When is the negative log-likelihood of Model $M_{4}$ smaller than the log-likelihood of model $M_{1}$ or $M_{2}$ or $M_{3}$ ?

$$
H(X, Y, Z)+M I(X, Y)<H(X, Y, Z)+C M I(X, Y \mid Z)
$$

The answer is in Equation 8. When the conditional mutual information $C M I(X, Y \mid Z)$ is larger than $M I(X, Y)$ the model $M_{4}$ has smaller negative log-likelihood value, therefore, $M 4$ is the "best".

In this work, the edge orientation principle runs on the depth first search algorithm [9]. The principle is applied to every pair of parent nodes in the

following way. Assume node $A$ has nodes $B, C$, and $D$ as candidate parents. There are 3 triplets to test: $B-A-C, B-A-D$ and $C-A-D$. As soon as a pair agrees with the proposed orientation principle, the edges are oriented as a head to head node. When the next triplet is tested but one of the edges is already directed the new test do not modify its direction.
The equation to compute the conditional mutual information of Gaussian variables is:

$$
\operatorname{CMI}(X, Y \mid Z)=\frac{1}{2} \log \left[\frac{\sigma_{x}^{2} \sigma_{y}^{2} \sigma_{z}^{2}\left(1-r_{x z}^{2}\right)\left(1-r_{y z}^{2}\right)}{\left|\Sigma_{x y z}\right|}\right]
$$

3. Over-fitting control. The inequality
$M I(X, Y)<C M I(X, Y \mid Z)$ could be made true due to the small biases of the data and creating false positive parents. As a rule, the larger the allowed number of parents the larger the over-fitting. Multi parent nodes are great for polytrees but these nodes and their parents must be carefully chosen. A hypothesis test based on a non parametric bootstrap test over the data vectors $X, Y$ and $Z$ can be performed to solve the over-fitting problem. In this approach we used the statistic $\hat{\theta}=\overline{C M I\left(X^{*}, Y^{*} \mid Z^{*}\right)-\overline{M I\left(X^{*}, Y^{*}\right)}}$, the significance level $5 \%$, null hypothesis $H_{0}=\overline{C M I\left(X^{*}, Y^{*} \mid Z^{*}\right)} \leq \overline{M I\left(X^{*}, Y^{*}\right)}$ and alternative hypothesis $H_{1}=\overline{C M I\left(X^{*}, Y^{*} \mid Z^{*}\right)}>\overline{M I\left(X^{*}, Y^{*}\right)}$. However this approach is computationally expensive. A better approach would be based on a threshold value but which value? Hence the question is: how many times the $C M I$ must be larger than the $M I$ as to represent true parents? Which is a good threshold value?. Empirically we solve this question by randomly creating a huge database of triplet-vectors $X, Y$ and $Z$ (from random gaussian distributions) that made true the inequality $M I(X, Y)<C M I(X, Y \mid Z)$. Within this large set there are two subsets: triplets that satisfy the null hypothesis and those that not. We found out that false parents are created in $95 \%$ of the cases when $\frac{C M I(X, Y \mid Z)}{M I(X, Y)}<3$. Therefore the sought threshold value is 3 . Thus a head to head node is created whenever $\frac{C M I(X, Y \mid Z)}{M I(X, Y)} \geq 3$.

# 4 Aspects of the Gaussian Polytree EDA 

In the previous section we explained the algorithm to build a gaussian polytree. An Estimation Distribution Algorithm was created using our model. Two aspects of the Gaussian polytree EDA are important to mention.

1. Data simulation. The procedure to obtain a new population (or new samples) from a polytree follows the common strategy of sampling from conditional Gaussian variables. If variable $X_{i}$ is conditioned on $Y=\left\{X_{j}, X_{k}, \ldots, X_{z}\right\}$, with $X_{i} \notin Y$, their conditional Gaussian distribution:

$$
\mathcal{N}_{X_{i} \mid Y=\mathbf{y}}\left(\mu_{X_{i} \mid Y=\mathbf{y}}, \Sigma_{X_{i} \mid Y=\mathbf{y}}\right)
$$

can be simulated using the conditional mean

$$
\mu_{X_{i} \mid Y=\mathbf{y}}=\mu_{X_{i}}+\Sigma_{X_{i} Y} \Sigma_{Y Y}^{-1}\left(\mathbf{y}-\mu_{Y}\right)
$$

and the conditional covariance:

$$
\Sigma_{X_{i} \mid Y=\mathbf{y}}=\Sigma_{X_{i} X_{i}}-\Sigma_{X_{i} Y} \Sigma_{Y Y}^{-1} \Sigma_{Y X_{i}}
$$

The simulation of samples at time $t$ follows the gaussian polytree structure. If $X_{i}^{t}$ has no parents then $X_{i}^{t} \sim \mathcal{N}\left(\mu_{X_{i}^{t-1}}, \Sigma_{X_{i}^{t-1}}\right)$; otherwise $X_{i}^{t}$ follow the gaussian distribution conditioned to $Y=\mathbf{y}^{t-1}$. This method adds exploration to the gaussian polytree EDA. Notice it is different of common ancestral sampling.
2. Selection. In EDAs truncation selection is commonly used. Our approach differs. We select the $K$ best individuals whose fitness is better than the average fitness of the entire population. By including all members of the population the average gets a poor value. Then the selection pressure is low and many different individuals (high diversity) are selected and used as information to create the next polytree.

# 5 Experiments 

The Gaussian polytree EDA is tested in two sets of benchmark functions.

### 5.1 Experiment 1: Convex Functions

This set of 9 convex functions was solved using the IDEA algorithm adapted with mechanisms to avoid premature convergence and to improve the convergence speed [7, 2]. The functions are listed in Table 3. In [7] the mechanism increases or decreases the variance accordingly to the rate the fitness function improves. In [2] the mechanism computes the shift of the mean in the direction of the best individual in the population. These mechanism are necessary due to premature convergence of the IDEA algorithm. Notice that the Gaussian polytree EDA does not need any additional mechanism to converge to the optimum. 30 runs were made for each problem.

Initialization. Asymmetric initialization is used for all the variables: $X_{i} \in$ $[-10,5]$.
Population size. For a problem in $l$ dimensions, the population is $2 \times\left(10\left(l^{0.7}\right)+\right.$ 10) [2]

Stopping conditions. Maximum number of fitness function evaluations is reached: $1.5 \times 10^{5}$; or target error smaller than $1 \times 10^{-10}$; or no improving larger than $1 \times 10^{-13}$ is detected after 30 generations and the mean of $l$ standard deviations, one for each dimension, is less than $1 \times 10^{-13}$.

The Figure 2 shows the best number of evaluations needed to reach the target error for dimensions $2,4,8,10,20,40$, and 80 . The success rate VS the problem dimensionality is listed in Table 1 and Table 2 details the number of evaluations found in our experiments.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Best number of evaluations VS problem dimensionality

Comments to Experiment 1. Note that the increment in the number of evaluations increases proportional to the increment in the dimensionality of the problem. The gaussian polytree EDA maintains a high success rate of global convergence, even in dimension 80. Out of these functions, just the different powers function (and slightly the two axes) were difficult to solve.

# 5.2 Experiment 2: Non-convex Functions 

In this experiment we use four functions that Larrañaga and Lozano tested with different algorithms, including the estimation of Gaussian network algorithm

Table 1. Success rate of functions ( $\%$ ) VS problem dimensionality
Table 2. Number of evaluations performed by the Gaussian polytree EDA needed to reach the target error in 30 repetitions (see stopping conditions)
Table 3. Set of convex functions of Experiment 1
$(E G N A) . E G N A$ is interesting for this comparison because it is a graph with continuous variables built with scoring metrics such as the Bayesian information criteria $(B I C)$. The precision matrix is created from the graph structure which allows none or more parents to any node. Therefore, the Gaussian polytree and the $E G N A$ allow several parents.
The experimental settings are the following:
Population size. For a problem in $l$ dimensions, the population is $2 \times\left(10\left(l^{0.7}\right)+\right.$ 10) $[2]$

Stopping conditions. Maximum number of fitness function evaluations is: $3 \times 10^{5}$; or target error smaller than $1 \times 10^{-6}, 30$ repetitions. Also stop when no improving larger than $1 \times 10^{-13}$ is detected after 30 generations and the mean of $l$ standard deviations, one for each dimension, is less than $1 \times 10^{-13}$.

The set of test functions is shown in Table 4. Experiments were performed for dimensions 10 and 50. The comparison for the Sphere function is shown in Figure 5, for the Rosenbrock function in Table 6, for the Griewangk in Table 7, and for the Ackley function in Table 8.

Table 4. Set of test functions of Experiment 2
Table 5. Comparative for the Sphere function with a dimension of 10 and 50 (optimum fitness value $=0$ )

Table 6. Comparative for the Rosenbrock function with a dimension of 10 and 50 (optimum fitness value $=0$ )

Table 7. Comparative for the Griewangk function with a dimension of 10 and 50 (optimum fitness value $=0$ )

Comments to Experiment 2. The proposed Gaussian polytree EDA reaches better values than the $E G N A$ requiring lesser number of function evaluations in all function (except for the Rosenbrock were both show a similar performance).

Table 8. Comparative for the Ackley function with a dimension of 10 and 50 (optimum fitness value $=0$ )

# 6 Conclusions 

In this paper we described a new EDA based on Gaussian polytrees. A polytree is a rich modeling structure that can be built with moderate computing costs. At the same time the Gaussian polytree is found to have a good performance on the tested functions. Other algorithms have shown convergence problems on convex functions and need special adaptations that the Gaussian polytree did not need. The new sampling method favors diversity of the population since it is based on the covariance matrix of the parent nodes and the children nodes. Also the proposed selection strategy applies low selection pressure to the individuals therefore improving diversity and delaying convergence.
