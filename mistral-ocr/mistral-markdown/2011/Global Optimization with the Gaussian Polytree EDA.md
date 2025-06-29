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

| Function | 2-D | 4-D | 8-D | 10-D | 20-D | 40-D | 80-D |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\mathcal{F}_{1}$ | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| $\mathcal{F}_{2}$ | 96.6 | 96.6 | 93.3 | 90.0 | 96.6 | 90.0 | 86.6 |
| $\mathcal{F}_{3}$ | 96.6 | 93.3 | 86.6 | 86.6 | 93.3 | 96.6 | 93.3 |
| $\mathcal{F}_{4}$ | 100 | 90.0 | 96.6 | 100 | 100 | 100 | 100 |
| $\mathcal{F}_{5}$ | 90.0 | 93.3 | 93.3 | 100 | 96.6 | 100 | 100 |
| $\mathcal{F}_{6}$ | 96.6 | 90.0 | 83.3 | 80.0 | 63.3 | 70.0 | 60.0 |
| $\mathcal{F}_{7}$ | 100 | 100 | 96.6 | 93.3 | 73.3 | 26.6 | 0.0 |
| $\mathcal{F}_{8}$ | 80.0 | 73.3 | 83.3 | 86.6 | 83.3 | 90.0 | 100 |
| $\mathcal{F}_{9}$ | 73.3 | 83.3 | 96.6 | 100 | 100 | 100 | 100 |

Table 2. Number of evaluations performed by the Gaussian polytree EDA needed to reach the target error in 30 repetitions (see stopping conditions)

| $\mathcal{F}_{1}$ | Dim | Best | Worst | Mean | Median | SD |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 2 | 5.3700 e 2 | 8.2500 e 2 | 7.3300 e 2 | 7.5200 e 2 | 6.2433 e 1 |
|  | 4 | 1.5340 e 3 | 1.8090 e 3 | 1.6739 e 3 | 1.6770 e 3 | 5.9753 e 1 |
|  | 8 | 3.4780 e 3 | 3.9450 e 3 | 3.7791 e 3 | 3.7980 e 3 | 9.5507 e 1 |
| $\mathcal{F}_{1}$ | 10 | 4.6760 e 3 | 5.1220 e 3 | 4.8663 e 3 | 4.8690 e 3 | 9.2939 e 1 |
|  | 20 | 1.0744 e 4 | 1.1258 e 4 | 1.1048 e 4 | 1.1069 e 4 | 1.3572 e 2 |
|  | 40 | 2.4931 e 4 | 2.5633 e 4 | 2.5339 e 4 | 2.5308 e 4 | 1.8670 e 2 |
|  | 80 | 5.7648 e 4 | 5.8966 e 4 | 5.8510 e 4 | 5.8574 e 4 | 3.1304 e 2 |
|  | 2 | 8.1800 e 2 | 3.2950 e 3 | 1.0650 e 3 | 1.0115 e3 | 4.2690 e 2 |
|  | 4 | 2.1280 e 3 | 5.8800 e 3 | 2.3583 e 3 | 2.2495 e 3 | 6.6716 e 2 |
|  | 8 | 4.7180 e 3 | 1.0001 e 5 | 8.2475 e 3 | 4.8910 e 3 | 1.7363 e 4 |
| $\mathcal{F}_{2}$ | 10 | 6.0830 e 3 | 2.0292 e 4 | 7.2357 e 3 | 6.3480 e 3 | 2.9821 e 3 |
|  | 20 | 1.4060 e 4 | 2.4260 e 4 | 1.4686 e 4 | 1.4303 e 4 | 1.8168 e 3 |
|  | 40 | 3.1937 e 4 | 5.1330 e 4 | 3.4468 e 4 | 3.2749 e 4 | 5.4221 e 3 |
|  | 80 | 7.4495 e 4 | 1.2342 e 5 | 8.0549 e 4 | 7.5737 e 4 | 1.2893 e 4 |
|  | 2 | 8.8000 e 2 | 3.5210 e 3 | 1.0819 e 3 | 1.0145 e 3 | 4.6461 e 2 |
|  | 4 | 2.2600 e 3 | 7.2280 e 3 | 2.6692 e 3 | 2.4375 e 3 | 9.8107 e 2 |
|  | 8 | 5.2700 e 3 | 1.5503 e 4 | 6.3378 e 3 | 5.5220 e 3 | 2.3176 e 3 |
| $\mathcal{F}_{3}$ | 10 | 6.9430 e 3 | 1.3732 e 4 | 7.9081 e 3 | 7.1060 e 3 | 2.0858 e 3 |
|  | 20 | 1.5956 e 4 | 2.6813 e 4 | 1.6900 e 4 | 1.6237 e 4 | 2.6287 e 3 |
|  | 40 | 3.6713 e 4 | 5.4062 e 4 | 3.7592 e 4 | 3.7017 e 4 | 3.1153 e 3 |
|  | 80 | 8.4462 e 4 | 1.1823 e 5 | 8.7323 e 4 | 8.5144 e 4 | 8.2764 e 3 |
|  | 2 | 8.8300 e 2 | 1.1120 e 3 | 9.9520 e 2 | 9.8900 e 2 | 5.8534 e 1 |
|  | 4 | 1.8830 e 3 | 5.8250 e 3 | 2.3616 e 3 | 1.9990 e 3 | 1.1030 e 3 |
|  | 8 | 4.0430 e 3 | 9.3870 e 3 | 4.4143 e 3 | 4.2545 e 3 | 9.4333 e 2 |
| $\mathcal{F}_{4}$ | 10 | 5.1480 e 3 | 5.6070 e 3 | 5.4052 e 3 | 5.4285 e 3 | 1.1774 e 2 |
|  | 20 | 1.1633 e 4 | 1.2127 e 4 | 1.1863 e 4 | 1.1861 e 4 | 1.0308 e 2 |
|  | 40 | 2.6059 e 4 | 2.6875 e 4 | 2.6511 e 4 | 2.6487 e 4 | 2.2269 e 2 |
|  | 80 | 5.9547 e 4 | 6.1064 e 4 | 6.0308 e 4 | 6.0302 e 4 | 3.6957 e 2 |
|  | 2 | 9.7300 e 2 | 3.6130 e 3 | 1.3396 e 3 | 1.1155 e 3 | 7.4687 e 2 |
|  | 4 | 2.2230 e 3 | 6.0680 e 3 | 2.6141 e 3 | 2.3760 e 3 | 9.0729 e 2 |
|  | 8 | 5.0060 e 3 | 1.0809 e 4 | 5.5754 e 3 | 5.2045 e 3 | 1.4230 e 3 |
| $\mathcal{F}_{5}$ | 10 | 6.4820 e 3 | 6.9730 e 3 | 6.7031 e 3 | 6.7075 e 3 | 1.1929 e 2 |
|  | 20 | 1.4687 e 4 | 2.7779 e 4 | 1.5381 e 4 | 1.4983 e 4 | 2.3449 e 3 |
|  | 40 | 3.3287 e 4 | 3.4203 e 4 | 3.3852 e 4 | 3.3865 e 4 | 2.0564 e 2 |
|  | 80 | 7.6250 e 4 | 7.8009 e 4 | 7.7247 e 4 | 7.7359 e 4 | 3.8967 e 2 |
|  | 2 | 8.7100 e 2 | 2.9510 e 3 | 1.0655 e 3 | 9.9550 e 2 | 3.5942 e 2 |
|  | 4 | 2.1480 e 3 | 5.5960 e 3 | 2.5739 e 3 | 2.2475 e 3 | 1.0015 e 3 |
|  | 8 | 4.8380 e 3 | 1.6298 e 4 | 6.0937 e 3 | 5.0160 e 3 | 2.6565 e 3 |
| $\mathcal{F}_{6}$ | 10 | 6.3130 e 3 | 2.3031 e 4 | 8.1936 e 3 | 6.5415 e 3 | 3.8264 e 3 |
|  | 20 | 1.4455 e 4 | 6.0814 e 4 | 2.0558 e 4 | 1.4919 e 4 | 1.0252 e 4 |
|  | 40 | 3.3222 e 4 | 6.2568 e 4 | 3.9546 e 4 | 3.3955 e 4 | 9.2253 e 3 |
|  | 80 | 7.6668 e 4 | 1.0019 e 5 | 8.6593 e 4 | 7.8060 e 4 | 1.1221 e 4 |
|  | 2 | 4.4400 e 2 | 6.2100 e 2 | 5.2970 e 2 | 5.3450 e 2 | 5.1867 e 1 |
|  | 4 | 9.7500 e 2 | 1.2580 e 3 | 1.1103 e 3 | 1.1100 e 3 | 6.8305 e 1 |
|  | 8 | 2.2360 e 3 | 7.3335 e 4 | 4.7502 e 3 | 2.4010 e 3 | 1.2953 e 4 |
| $\mathcal{F}_{7}$ | 10 | 2.9530 e 3 | 9.9095 e 4 | 7.7189 e 3 | 3.1475 e 3 | 1.8871 e 4 |
|  | 20 | 6.8480 e 3 | 1.0011 e 5 | 3.1933 e 4 | 7.2465 e 3 | 4.1782 e 4 |
|  | 40 | 1.6741 e 4 | 1.0017 e 5 | 7.7923 e 4 | 1.0003 e 5 | 3.7343 e 4 |
|  | 80 | 1.5001 e 5 | 1.5024 e 5 | 1.5010 e 5 | 1.5008 e 5 | 7.1759 e 1 |
|  | 2 | 6.7000 e 2 | 3.8730 e 3 | 1.3424 e 3 | 8.5950 e 2 | 1.0699 e 3 |
|  | 4 | 1.8780 e 3 | 8.8220 e 3 | 3.2186 e 3 | 2.2065 e 3 | 1.8858 e 3 |
|  | 8 | 4.6880 e 3 | 1.0773 e 4 | 5.7467 e 3 | 4.8275 e 3 | 2.1246 e 3 |
| $\mathcal{F}_{8}$ | 10 | 5.9350 e 3 | 1.2863 e 4 | 7.0149 e 3 | 6.1555 e 3 | 2.2485 e 3 |
|  | 20 | 1.3228 e 4 | 2.6804 e 4 | 1.5504 e 4 | 1.3667 e 4 | 4.3446 e 3 |
|  | 40 | 2.9959 e 4 | 8.3911 e 4 | 3.3521 e 4 | 3.0451 e 4 | 1.0781 e 4 |
|  | 80 | 6.8077 e 4 | 7.0542 e 4 | 6.9092 e 4 | 6.9069 e 4 | 4.7975 e 2 |
|  | 2 | 1.0560 e 3 | 4.2000 e 3 | 2.0126 e 3 | 1.3910 e 3 | 1.1536 e 3 |
|  | 4 | 3.1980 e 3 | 7.5810 e 3 | 4.0188 e 3 | 3.4055 e 3 | 1.4445 e 3 |
|  | 8 | 7.4930 e 3 | 1.4390 e 4 | 7.9337 e 3 | 7.7140 e 3 | 1.2243 e 3 |
| $\mathcal{F}_{9}$ | 10 | 9.6110 e 3 | 1.0325 e 4 | 1.0013 e 4 | 9.9930 e 3 | 1.5436 e 2 |
|  | 20 | 2.2342 e 4 | 2.3122 e 4 | 2.2776 e 4 | 2.2780 e 4 | 1.9712 e 2 |
|  | 40 | 5.1413 e 4 | 5.2488 e 4 | 5.1852 e 4 | 5.1827 e 4 | 2.4254 e 2 |
|  | 80 | 1.1796 e 5 | 1.2033 e 5 | 1.1896 e 5 | 1.1904 e 5 | 5.3493 e 2 |

Table 3. Set of convex functions of Experiment 1

| Name | Alias | Definition |
| :-- | :-- | :-- |
| Sphere | $\mathcal{F}_{1}$ | $\sum_{i=1}^{N} X_{i}^{2}$ |
| Ellipsoid | $\mathcal{F}_{2}$ | $\sum_{i=1}^{N} 10^{6 \frac{i-1}{N-1}} X_{i}^{2}$ |
| Cigar | $\mathcal{F}_{3}$ | $X_{1}^{2}+\sum_{i=2}^{N} 10^{6} X_{i}^{2}$ |
| Tablet | $\mathcal{F}_{4}$ | $10^{6} X_{1}^{2}+\sum_{i=2}^{N} X_{i}^{2}$ |
| Cigar Tablet | $\mathcal{F}_{4}$ | $X_{1}^{2}+\sum_{i=2}^{N-1} 10^{4} X_{i}^{2}+10^{8} X_{N}^{2}$ |
| Two Axes | $\mathcal{F}_{6}$ | $\sum_{i=1}^{[N / 2]} 10^{6} X_{i}^{2}+\sum_{i=[N / 2]}^{N} X_{i}^{2}$ |
| Different Powers | $\mathcal{F}_{7}$ | $\sum_{i=1}^{N}\left|X_{i}\right|^{2+10 \frac{i-1}{N-1}}$ |
| Parabolic Ridge | $\mathcal{F}_{8}$ | $-X_{1}+100 \sum_{i=2}^{N} X_{i}^{2}$ |
| Sharp Ridge | $\mathcal{F}_{9}$ | $-X_{1}+100 \sqrt{\sum_{i=2}^{N} X_{i}^{2}}$ |

$(E G N A) . E G N A$ is interesting for this comparison because it is a graph with continuous variables built with scoring metrics such as the Bayesian information criteria $(B I C)$. The precision matrix is created from the graph structure which allows none or more parents to any node. Therefore, the Gaussian polytree and the $E G N A$ allow several parents.
The experimental settings are the following:
Population size. For a problem in $l$ dimensions, the population is $2 \times\left(10\left(l^{0.7}\right)+\right.$ 10) $[2]$

Stopping conditions. Maximum number of fitness function evaluations is: $3 \times 10^{5}$; or target error smaller than $1 \times 10^{-6}, 30$ repetitions. Also stop when no improving larger than $1 \times 10^{-13}$ is detected after 30 generations and the mean of $l$ standard deviations, one for each dimension, is less than $1 \times 10^{-13}$.

The set of test functions is shown in Table 4. Experiments were performed for dimensions 10 and 50. The comparison for the Sphere function is shown in Figure 5, for the Rosenbrock function in Table 6, for the Griewangk in Table 7, and for the Ackley function in Table 8.

Table 4. Set of test functions of Experiment 2

| Name | Alias | Definition | Domain |
| :-- | :-- | :-- | :-- |
| Sphere | $\mathcal{F}_{1}$ | $\sum_{i=1}^{N} X_{i}^{2}$ | $-600 \leq X_{i} \leq 600$ |
| Rosenbrock | $\mathcal{F}_{2}$ | $\sum_{i=1}^{N-1}\left[\left(1-X_{i}\right)^{2}+100\left(X_{i+1}-X_{i}^{2}\right)^{2}\right]$ | $-10 \leq X_{i} \leq 10$ |
| Griewangk | $\mathcal{F}_{4}$ | $\sum_{i=1}^{N} \frac{X_{i}^{2}}{4000}-\prod_{i=1}^{N} \cos \left(\frac{X_{i}}{\sqrt{ }}\right)+1$ | $-600 \leq X_{i} \leq 600$ |
| Ackley | $\mathcal{F}_{5}$ | $-20 \exp \left(-0.2 \sqrt{\frac{1}{N} \sum_{i=1}^{N} X_{i}^{2}}\right)$ | $-10 \leq X_{i} \leq 10$ |
|  |  | $-\exp \left(\frac{1}{N} \sum_{i=1}^{N} \cos \left(2 \pi X_{i}\right)\right)+20+e$ |  |

Table 5. Comparative for the Sphere function with a dimension of 10 and 50 (optimum fitness value $=0$ )

| Dimension | Algorithm | Best | Evaluations |
| :--: | :--: | :--: | :--: |
|  | $E G N A_{B I C}$ | $2.5913 \mathrm{e}-5 \pm 3.71 \mathrm{e}-5$ | $77162.4 \pm 6335.4$ |
| 10 | $E G N A_{B G e}$ | $7.1938 \mathrm{e}-6 \pm 1.78 \mathrm{e}-6$ | $74763.6 \pm 1032.2$ |
|  | $E G N A_{e e}$ | $7.3713 \mathrm{e}-6 \pm 1.98 \mathrm{e}-6$ | $73964 \pm 1632.1$ |
|  | PolyG | $7.6198 \mathrm{e}-7 \pm 1.75 \mathrm{e}-7$ | $4723.9 \pm 78.7$ |
| 50 | $E G N A_{B I C}$ | $1.2126 \mathrm{e}-3 \pm 7.69 \mathrm{e}-4$ | $263869 \pm 29977.5$ |
|  | $E G N A_{B G e}$ | $8.7097 \mathrm{e}-6 \pm 1.30 \mathrm{e}-6$ | $204298.8 \pm 1264.2$ |
|  | $E G N A_{e e}$ | $8.3450 \mathrm{e}-6 \pm 1.04 \mathrm{e}-6$ | $209496.2 \pm 1576.8$ |
|  | PolyG | $8.9297 \mathrm{e}-7 \pm 8.05 \mathrm{e}-8$ | $32258.4 \pm 274.1$ |

Table 6. Comparative for the Rosenbrock function with a dimension of 10 and 50 (optimum fitness value $=0$ )

| Dimension | Algorithm | Best | Evaluations |
| :--: | :--: | :--: | :--: |
|  | $E G N A_{B I C}$ | $8.8217 \pm 0.16$ | $268066.9 \pm 69557.3$ |
| 10 | $E G N A_{B G e}$ | $8.6807 \pm 5.87 \mathrm{e}-2$ | $164518.7 \pm 24374.5$ |
|  | $E G N A_{e e}$ | $8.7366 \pm 2.23 \mathrm{e}-2$ | $301850 \pm 0.0$ |
|  | PolyG | $7.9859 \pm 2.48 \mathrm{e}-1$ | $18931.8 \pm 3047.6$ |
| 50 | $E G N A_{B I C}$ | $50.4995 \pm 2.30$ | $301850 \pm 0.0$ |
|  | $E G N A_{B G e}$ | $48.8234 \pm 0.118$ | $301850 \pm 0.0$ |
|  | $E G N A_{e e}$ | $48.8893 \pm 1.11 \mathrm{e}-2$ | $301850 \pm 0.0$ |
|  | PolyG | $47.6 \pm 1.52 \mathrm{e}-1$ | $81692.2 \pm 6704.7$ |

Table 7. Comparative for the Griewangk function with a dimension of 10 and 50 (optimum fitness value $=0$ )

| Dimension | Algorithm | Best | Evaluations |
| :--: | :--: | :--: | :--: |
|  | $E G N A_{B I C}$ | $3.9271 \mathrm{e}-2 \pm 2.43 \mathrm{e}-2$ | $301850 \pm 0.0$ |
| 10 | $E G N A_{B G e}$ | $7.6389 \mathrm{e}-2 \pm 2.93 \mathrm{e}-2$ | $301850 \pm 0.0$ |
|  | $E G N A_{e e}$ | $5.6840 \mathrm{e}-2 \pm 3.82 \mathrm{e}-2$ | $301850 \pm 0.0$ |
|  | PolyG | $3.6697 \mathrm{e}-3 \pm 6.52 \mathrm{e}-3$ | $60574.3 \pm 75918.5$ |
| 50 | $E G N A_{B I C}$ | $1.7075 \mathrm{e}-4 \pm 6.78 \mathrm{e}-5$ | $250475 \pm 18658.5$ |
|  | $E G N A_{B G e}$ | $8.6503 \mathrm{e}-6 \pm 7.71 \mathrm{e}-7$ | $173514.2 \pm 1264.3$ |
|  | $E G N A_{e e}$ | $9.1834 \mathrm{e}-6 \pm 5.91 \mathrm{e}-7$ | $175313.3 \pm 965.6$ |
|  | PolyG | $8.9551 \mathrm{e}-7 \pm 6.24 \mathrm{e}-8$ | $28249.8 \pm 227.4$ |

Comments to Experiment 2. The proposed Gaussian polytree EDA reaches better values than the $E G N A$ requiring lesser number of function evaluations in all function (except for the Rosenbrock were both show a similar performance).

Table 8. Comparative for the Ackley function with a dimension of 10 and 50 (optimum fitness value $=0$ )

| Dimension | Algorithm | Best | Evaluations |
| :--: | :--: | :--: | :--: |
| 10 | $E G N A_{B I C}$ | $5.2294 \pm 4.49$ | $229086.4 \pm 81778.4$ |
|  | $E G N A_{B G e}$ | $7.9046 \mathrm{e}-6 \pm 1.39 \mathrm{e}-6$ | $113944 \pm 1632.2$ |
|  | $E G N A_{e e}$ | $74998 \mathrm{e}-6 \pm 1.72 \mathrm{e}-6$ | $118541.7 \pm 2317.8$ |
|  | PolyG | $8.3643 \mathrm{e}-7 \pm 1.24 \mathrm{e}-7$ | $5551.5 \pm 104.0$ |
| 50 | $E G N A_{B I C}$ | $19702 \mathrm{e}-2 \pm 7.50 \mathrm{e}-3$ | $288256.8 \pm 29209.4$ |
|  | $E G N A_{B G e}$ | $8.6503 \mathrm{e}-6 \pm 3.79 \mathrm{e}-7$ | $282059.9 \pm 632.1$ |
|  | $E G N A_{e e}$ | $6.8198 \pm 0.27$ | $301850 \pm 0.0$ |
|  | PolyG | $9.4425 \mathrm{e}-7 \pm 4.27 \mathrm{e}-8$ | $36672.9 \pm 241.0$ |

# 6 Conclusions 

In this paper we described a new EDA based on Gaussian polytrees. A polytree is a rich modeling structure that can be built with moderate computing costs. At the same time the Gaussian polytree is found to have a good performance on the tested functions. Other algorithms have shown convergence problems on convex functions and need special adaptations that the Gaussian polytree did not need. The new sampling method favors diversity of the population since it is based on the covariance matrix of the parent nodes and the children nodes. Also the proposed selection strategy applies low selection pressure to the individuals therefore improving diversity and delaying convergence.

## References

1. Acid, S., de Campos, L.M.: Approximations of Causal Networks by Polytrees: An Empirical Study. In: Bouchon-Meunier, B., Yager, R.R., Zadeh, L.A. (eds.) IPMU 1994. LNCS, vol. 945, pp. 149-158. Springer, Heidelberg (1995)
2. Bosman, P.A.N., Grahl, J., Thierens, D.: Enhancing the performance of maximumlikelihood gaussian edas using anticipated mean shift. In: Proceedings of BNAIC 2008, the Twentieth Belgian-Dutch Artificial Intelligence Conference, pp. 285-286. BNVKI (2008)
3. Chow, C.K., Liu, C.N.: Approximating discrete probability distributions with dependence trees. IEEE Transactions on Information Theory IT-14(3), 462-467 (1968)
4. Darwiche, A.: Modeling and Reasoning with Bayesian Networks. Cambridge University Press (2009)
5. Dasgupta, S.: Learning polytrees. In: Proceedings of the Fifteenth Annual Conference on Uncertainty in Artificial Intelligence (UAI 1999), pp. 134-141. Morgan Kaufmann, San Francisco (1999)
6. Edwards, D.: Introduction to Graphical Modelling. Springer, Berlin (1995)
7. Grahl, P.A.B.J., Rothlauf, F.: The correlation-triggered adaptive variance scaling idea. In: Proceedings of the 8th Annual Conference on Genetic and Evolutionary Computation, GECCO 2006, pp. 397-404. ACM (2006)
8. Lauritzen, S.L.: Graphical models. Clarendon Press (1996)

9. Ouerd, B.J.O.M., Matwin, S.: A formal approach to using data distributions for building causal polytree structures. Information Sciences, an International Journal 168, 111-132 (2004)
10. Neapolitan, R.E.: Learning Bayesian Networks. Prentice Hall series in Artificial Intelligence (2004)
11. Ortiz, M.S.: Un estudio sobre los Algoritmos Evolutivos con Estimacion de Distribuciones basados en poliarboles y su costo de evaluacion. PhD thesis, Instituto de Cibernetica, Matematica y Fisica, La Habana, Cuba (2003)
12. Ouerd, M.: Learning in Belief Networks and its Application to Distributed Databases. PhD thesis, University of Ottawa, Ottawa, Ontario, Canada (2000)
13. Pearl, J.: Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference. Morgan Kaufmann Publishers Inc., San Francisco (1988)
14. de Campos, L.M., Moteos, J., Molina, R.: Using bayesian algorithms for learning causal networks in classification problems. In: Proceedings of the Fourth International Conference of Information Processing and Management of Uncertainty in Knowledge-Based Systems (IPMU), pp. 395-398 (1993)
15. Rebane, G., Pearl, J.: The recovery of causal poly-trees from statistical data. In: Proceedings, 3rd Workshop on Uncertainty in AI, Seattle, WA, pp. 222-228 (1987)
16. Segovia-Dominguez Ignacio, H.-A.A., Enrique, V.-D.: The gaussian polytree eda for global optimization. In: Proceedings of the 13th Annual Conference Companion on Genetic and Evolutionary Computation, GECCO 2011, pp. 69-70. ACM, New York (2011)