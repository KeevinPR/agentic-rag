# Analysis of Bayesian Network Learning Techniques for a Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm: a case study on MNK Landscape 

Marcella S. R. Martins ${ }^{1}$ - Mohamed El Yafrani ${ }^{2}$ (1) $\cdot$ Myriam Delgado ${ }^{1}$ Ricardo Lüders ${ }^{1}$ ・ Roberto Santana ${ }^{3}$ ・ Hugo V. Siqueira ${ }^{1}$ ・ Huseyin G. Akcay ${ }^{4}$ ・ Belaïd Ahiod ${ }^{5}$<br>Received: 5 November 2019 / Revised: 9 October 2020 / Accepted: 11 January 2021 /<br>Published online: 6 February 2021<br>(c) The Author(s), under exclusive licence to Springer Science+Business Media, LLC part of Springer Nature 2021


#### Abstract

This work investigates different Bayesian network structure learning techniques by thoroughly studying several variants of Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm (HMOBEDA), applied to the MNK Landscape combinatorial problem. In the experiments, we evaluate the performance considering three different aspects: optimization abilities, robustness and learning efficiency. Results for instances of multi- and many-objective MNK-landscape show that, score-based structure learning algorithms appear to be the best choice. In particular, $\mathrm{HMOBEDA}_{k 2}$ was capable of producing results comparable with the other variants in terms of the runtime of convergence and the coverage of the final Pareto front, with the additional advantage of providing solutions that are less sensible to noise while the variability of the corresponding Bayesian network models is reduced.


Keywords Many-objective optimization $\cdot$ Estimation of distribution algorithms $\cdot$ Structure learning techniques $\cdot$ Robustness

## 1 Introduction

According to Bennett and Parrado-Hernández (2006), the fields of machine learning and mathematical programming are increasingly intertwined. We have observed a great synergy between them in the past few years, with optimization problems taking place at the heart of most machine learning approaches and machine learning being used to improve several optimization algorithms.

[^0]
[^0]:    $\boxtimes$ Marcella S. R. Martins marcella@utfpr.edu.br

    Extended author information available on the last page of the article

Estimation of distribution algorithm (EDA) (Mühlenbein and Paab 1996) is a class of evolutionary algorithm (EA) that explores the search space by building a probabilistic model from a set with the current best candidate solutions. Since new solutions are sampled from the probabilistic model, evolution is guided toward more promising areas of the search space. Playing a central role in the connection between optimization heuristics and machine learning approaches, EDAs based on Probabilistic graphical models (PGMs) (Lauritzen 1996) combine evolutionary optimization with graph and probability theories giving rise to powerful optimizers based on mathematical foundations for multivariate statistical modeling. PGMs are widely used in evolutionary optimization, especially in EDAs when interactions among variables are considered (Multivariate EDAs). EDAs based on PGM have gained attention from the evolutionary optimization community as they can provide more useful information about decision variables compared to other EAs.

EDAs have achieved a good performance for several problems including environmental monitoring network design (Kollat et al. 2008), protein side chain placement problem (Santana et al. 2008) and table ordering (Bengoetxea et al. 2011). They have also been applied to solve the multi-objective Knapsack Problem (Shah and Reed 2011), multi-objective optimization problems (MOPs) in a noisy environment (Shim et al. 2013) and combinatorial many-objective optimization problems (MaOPs) (Martins et al. 2018). Usually they integrate both the model building and sampling techniques into evolutionary optimizers using special selection schemes (Khan et al. 2002). Recently, the role of the probabilistic model has been extended to model the dependencies between variables and objectives (Karshenas et al. 2014). In addition, EDAs can be notably enhanced by adding a local optimizer that can refine the solutions found by sampling from the PGM (Marti et al. 2008; Martins et al. 2017, 2018).

In this work, we study this type of enhancement in the context of many-objective optimization (Ribeiro et al. 2020), investigating the approach called Hybrid Multiobjective Bayesian Estimation of Distribution Algorithm (HMOBEDA) (Martins et al. 2018, 2017), using a PGM based on the joint probabilistic modeling of decision variables, objectives, and parameters of the local optimizer. Structure learning methods have been extensively studied in Cooper and Herskovits (1992), Tsamardinos et al. (2003), Tsamardinos et al. (2006), Santhanam and Wainwright (2012) resulting in several algorithms in various settings. However, most of these works are focused on learning the PGM structure while ignoring the performance of the optimization algorithm.

The main goal in this paper is to investigate PGM structure learning techniques considering the data provided by several variants of an optimization algorithm (HMOBEDA). Each variant results from a different Bayesian Network (BN) learning method. The data considered here are the best candidate solutions obtained during the evolutionary process from each variant. Exploring the structure learning algorithms can lead to more efficient methods considering the differences in the structural information they capture and their sensibility to noisy solutions. One of the main contributions of this paper is the analysis of the behavior and performance of the algorithms variants considering three different aspects: multi-criteria optimization, robustness and learning capabilities. We aim to evaluate the learning algorithms considering (i) optimization performance based on run time, convergence and coverage of the final Pareto

fronts; (ii) robustness based on sensibility to noise; (iii) learning capacity based on accuracy to recover the problem structure (for instance, in terms of the Structural Hamming Distance (SHD) (Tsamardinos et al. 2006) from the target model). This analysis is particularly novel and relevant since we address many-objective optimization problems, and HMOBEDA is one of few algorithms that learns and exploits relationships between objectives and variables as well as the parameters of an embedded local search procedure.

In this work, we compare the K2 algorithm (Cooper and Herskovits 1992), the HillClimbing using K2-metric (HC-K2) (Moran et al. 2009), the Incremental Association Markov Blanket (IAMB) (Tsamardinos et al. 2003), the PC-algorithm (PC) (Colombo and Maathuis 2014) and the Max-Min Hill Climbing (MMHC) (Tsamardinos et al. 2006). These methods are applied to the Bayesian networks modeling phase in HMOBEDA. The idea is to contrast different score-based, constraint-based and hybrid learning techniques when applying PGM in the context of multi-objective optimization. For this, we address a combinatorial problem, namely the Multi-objective NK-landscape (MNK) model which has been recently explored in other works in the literature (Aguirre and Tanaka 2007; Santana et al. 2015). In particular, EDAs that use different types of probabilistic models, including Bayesian networks, have already been investigated for MNK problems (Martins et al. 2018, ?). The hypervolume and Inverted Generational Distance (IGD) indicators are considered for the statistical analysis of the results.

This paper is organized as follows. Section 2 provides a brief introduction to Multi-objective optimization, Bayesian Network concepts and the addressed MNK-Landscape model. Section 3 details the HMOBEDA. Results from numerical experiments are shown and discussed in Sect. 4 with conclusions and future directions presented in Sect. 5.

# 2 Background 

This section presents some basic concepts and background information about the main topics addressed in this paper. Thus, a review on multi-objective optimization and Bayesian networks is presented, and the addressed benchmarking problem is revisited.

### 2.1 Multi-objective optimization

Real-world problems are generally characterized by several competing objectives. While in the case of single-objective optimization one optimal solution is usually required to solve the problem (Puchta et al. 2016, 2020; Santos et al. 2017), this is not true in multi-objective optimization (Ribeiro et al. 2020). The standard approach to solve this difficulty lies in finding all possible trade-offs among the multiple, competing objectives.

A general MOP includes decision variables, objective functions, and constraints, where objective functions and constraints are functions of the decision variables (Zitzler and Thiele 1999). Mathematically, a maximization MOP can be defined as:

$$
\begin{aligned}
& \max _{\mathbf{x}} \mathbf{z}=\mathbf{f}(\mathbf{x})=\left(f_{1}(\mathbf{x}), f_{2}(\mathbf{x}), \ldots, f_{R}(\mathbf{x})\right) \\
& \text { subject to } \\
& \mathbf{h}(\mathbf{x})=\left(h_{1}(\mathbf{x}), h_{2}(\mathbf{x}), \ldots, h_{k}(\mathbf{x})\right) \leq 0 \\
& \mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{Q}\right) \in X \\
& \mathbf{z}=\left(z_{1}, z_{2}, \ldots, z_{R}\right) \in Z
\end{aligned}
$$

where $\mathbf{x}=\left(x_{1}, \ldots, x_{Q}\right)$ is a $Q$-dimensional decision variable vector defined in a universe $X ; \mathbf{z}$ is the objective vector, with $R$ objectives, where each $f_{r}(\mathbf{x})$ is a singleobjective function, $Z$ is the objective space and $\mathbf{h}(\mathbf{x}) \leq 0$ is the set of constraints which determines a set of feasible solutions $X_{f}$. When $R$ is greater than three, the problem is referred to as a Many Objective Optimization Problem (MaOP). These problems are usually more challenging than the problems with $R \leq 3$ due to the higher dimensionality of the objective space and the existence of many conflicting objective functions.

The set of MOP and MaOP solutions includes decision vectors for which the corresponding objective vectors cannot be improved in any dimension without degradation in another-these decision vectors are called the Pareto optimal set. The idea of Pareto optimally is based on the Pareto dominance. In a maximization problem, a solution $\mathbf{u}$ dominates a solution $\mathbf{v}$ if $f_{r}(\mathbf{u}) \geq f_{r}(\mathbf{v})$ for all $r \in\{1,2,3, \ldots, R\}$, and $f_{r}(\mathbf{u})>f_{r}(\mathbf{v})$ for some $r \in\{1,2,3, \ldots, R\}$. A solution is Pareto optimal if it is not dominated by any other feasible solution.

The set of non-dominated solutions (the Pareto set) lies, in the objective space, on a surface known as Pareto optimal front. The goal of the optimization is to find a representative set of solutions with the corresponding objective vectors along the Pareto optimal front.

Generating the Pareto set can be computationally expensive and it is often infeasible due to the computational complexity of the problems. For this reason, a number of stochastic search strategies such as Evolutionary algorithms and Estimation of distribution algorithms have been developed. These approaches usually do not guarantee the identification of optimal trade-offs, instead, they try to find a good approximation. Because these algorithms are population-based, they are able to approximate the whole Pareto front of a MOP in a single run.

# 2.2 Bayesian networks 

Claimed as a paradigm shift in the field of evolutionary computation, EDAs employ explicit probability distributions (Larrañaga and Lozano 2001). Among the most general probabilistic models for discrete variables used in EDAs are Bayesian networks. In this sub-section, we briefly describe some techniques used for learning the structure of Bayesian networks.

Bayesian networks are addressed in this paper for modeling multinomial data with discrete variables and generate new solutions using the particular conditional probability (Henrion 1988) described by Eq. 2:

$$
p\left(y_{m}^{k} \mid \mathbf{p a}_{m}^{j, B}\right)=\theta_{y_{m}^{k} \mid \mathbf{p a}_{m}^{j, B}}=\theta_{m j k}
$$

Fig. 1 Bayesian network structure example with $M=5$ random variables
![img-0.jpeg](img-0.jpeg)
where $\mathbf{Y}=\left(Y_{1}, \ldots, Y_{M}\right)$ is a vector representation of $M$ random variables and $y_{m}$ the $m$-th component of it; $B$ is the structure and $\Theta$ a set of local parameters; $\mathbf{P a}_{m}^{B}$ represents the set of parents of the variable $Y_{m}$, where $\mathbf{p a}_{m}^{j, B} \in\left\{\mathbf{p a}_{m}^{1, B}, \ldots, \mathbf{p a}_{m}^{t_{m}, B}\right\}$ denotes a particular combination of values for $\mathbf{P a}_{m}^{B}, t_{m}$ is the total number of different possible instantiations of the parent variables of $Y_{m}$ given by $t_{m}=\prod_{Y_{v} \in \mathbf{P a}_{m}^{B}} s_{v}, s_{v}$ is the total of possible values (states) that $Y_{v}$ can assume. The parameter $\theta_{m j k}$ represents the conditional probability that variable $Y_{m}$ takes its $k$-th value $\left(y_{m}^{k}\right)$, knowing that its parent variables have taken their $j$-th combination of values $\left(\mathbf{p a}_{m}^{j, B}\right)$. This way, the parameter set is given by $\Theta=\left\{\boldsymbol{\theta}_{1}, \ldots, \boldsymbol{\theta}_{m}, \ldots \boldsymbol{\theta}_{M}\right\}$, where $\boldsymbol{\theta}_{m}=\left(\theta_{m 11}, \ldots, \theta_{m j k}, \ldots, \theta_{m, t_{m}, s_{m}}\right)$ and $M$ is the total number of nodes in the BN. Figure 1 represents a Bayesian network whose structure $B$ is defined by a directed graph with $M=5$ nodes representing 5 random variables. In this example the parents of all variables are given by $\mathbf{P a}_{1}^{B}=\emptyset, \mathbf{P a}_{2}^{B}=\left\{Y_{1}\right\}, \mathbf{P a}_{3}^{B}=\left\{Y_{1}\right\}, \mathbf{P a}_{4}^{B}=\left\{Y_{2}, Y_{3}\right\}$ and $\mathbf{P a}_{5}^{B}=\left\{Y_{2}\right\}$. Assuming that each variable $Y_{m}$ could assume values $\{0,1\}$, we would have $s_{v}=2, \forall v$. Considering, for example, the specific variable $Y_{4}$, we would have $t_{4}=4$, then $\boldsymbol{\theta}_{4}=\left(\theta_{4(00) 0}, \theta_{4(01) 0}, \theta_{4(10) 0}, \theta_{4(11) 0}, \theta_{4(00) 1}, \theta_{4(01) 1}, \theta_{4(10) 1}, \theta_{4(11) 1}\right)$, where $\theta_{4\left(j_{2} j_{3}\right) k}$ is the conditional probability that variable $Y_{4}$ takes its $k$-th value ( 0 or 1 ), knowing that its parent variables have taken $\left(j_{2} j_{3}\right)$ combination of values. Therefore, for all nodes in Fig. 1 a total of 22 conditional probabilities should be estimated: 2 for $Y_{1}, 8$ for $Y_{4}$ and 4 for each remaining variable.

The parameters of $\Theta$ and $B$ are usually unknown, and to determine them the literature presents two possibilities: Maximum Likelihood Estimate (MLE) and Bayesian Estimate. In this work, we address the last method.

In terms of BN structures learning process, some authors proposed different methods. We highlight three approaches: score-based learning, constraint-based learning, and hybrid methods (Yuan and Malone 2013).

Score-based techniques apply heuristic optimization methods to sort the structures selecting the one which maximizes the value of a scoring metric. The simple greedy search algorithm, local hill-climbing, simulated annealing, tabu search, K2 algorithm and evolutionary computation are important representatives of this class. In what follows we will discuss two scoring metrics to be used with Score-based techniques.

According to Scanagatta et al. (2019), one of the most adopted scores is the Bayesian Dirichlet equivalence (BDe) metric (Buntine 1991; Cooper and Herskovits 1992;

Heckerman et al. 1995), which measures the posterior probability of a chosen BN given the available data. It assumes the Dirichlet distribution (with parameters $\alpha_{m j k}$ ) as prior probability and a uniform prior distribution of all possible structures (Larrañaga et al. 2012).

The BDe metric is defined by Eq. 3:

$$
p(B \mid P o p)=\prod_{m=1}^{M} \prod_{j=1}^{t_{m}} \frac{\Gamma\left(\alpha_{m j}\right)}{\Gamma\left(\alpha_{m j}+N_{m j}\right)} \prod_{k=1}^{s_{m}} \frac{\Gamma\left(\alpha_{m j k}+N_{m j k}\right)}{\Gamma\left(\alpha_{m j k}\right)}
$$

where $N_{m j k}$ is the number of observations in the data set $P o p$ for which $Y_{m}$ assumes the $k$-th value given the $j$-th combination of values from its parents, with $\mathbf{N}_{m j}=$ $\left\{N_{m j 1}, \ldots, N_{m j s_{m}}\right\}, \Gamma(x)=(x-1)$ ! and $\alpha_{m j k}=\sum_{k=1}^{s_{m}} \alpha_{m j k}$. The product over $j \in\left\{1, \ldots, t_{m}\right\}$ runs for all combinations of parents of $Y_{m}$ and the product over $k \in\left\{1, \ldots, s_{m}\right\}$ runs for all possible values of $Y_{m}$. The Dirichlet parameter $\alpha_{m j k}$ stands for prior information about the number of instances that have $Y_{m}$ set to its $k$-th value and the set of parents of $Y_{m}$ is instantiated to its $j$-th combination. In the so-called K2 metric (Cooper and Herskovits 1992) for instance, parameters $\alpha_{m j k}$ are set to 1 as there is no prior information about the problem, and Eq. 3 reduces to Eq. 4:

$$
p(B \mid P o p)=\prod_{m=1}^{M} \prod_{j=1}^{t_{m}} \frac{\left(s_{m}-1\right)!}{\left(N_{m j}+s_{m}-1\right)!} \prod_{k=1}^{s_{m}}\left(N_{m j k}\right)!
$$

Constraint-based learning methods typically use statistical tests to identify conditional independence relations from the data and build a BN structure that best fits those relations. Some examples are the Incremental Association Markov Blanket (IAMB) (Tsamardinos et al. 2003) and PC-Stable implementation algorithm (PC) (Colombo and Maathuis 2014), the most commonly used among constraintbased ones (Scutari et al. 2018).

Hybrid methods combine the two approaches: it uses conditional independence tests to reduce the search space, and at the same time, it applies network scores to find out the optimal network structure. An important algorithm of this class is the MaxMin Hill Climbing (MMHC) (Tsamardinos et al. 2006), in which constraint-based learning is used to create a skeleton graph and the score-based is addressed to find a high-scoring network structure, a subgraph of the skeleton.

# 2.3 MNK-landscape problem 

The single NK fitness landscapes is a family of combinatorial problems proposed in Kauffman (1993) aiming at exploring the way in which the neighborhood structure and the strength of the interactions between neighboring variables (subfunctions) are linked to the search space ruggedness.

Let $\mathbf{X}=\left(X_{1}, \ldots, X_{N}\right)$ denote a vector of discrete variables and $\mathbf{x}=\left(x_{1}, \ldots, x_{N}\right)$ an assignment to the variables.

An NK fitness landscape is defined by the following components:

Table 1 Example of subfunction assignments for the neighborhood structure shown in Fig. $2(r=1)$

| $f_{1, q}\left(x_{q}, \Pi_{1}\left(x_{q}\right)\right)$ | Values of $\left(x_{q}, \Pi_{1}\left(x_{q}\right)\right)$ |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
| $f_{1,1}\left(x_{1}, x_{3}, x_{4}\right)$ | 0.58 | 0.18 | 0.74 | 0.12 | 0.97 | 0.42 | 0.16 | 0.71 |
| $f_{1,2}\left(x_{2}, x_{5}, x_{6}\right)$ | 0.23 | 0.17 | 0.13 | 0.95 | 0.17 | 0.15 | 0.16 | 0.31 |
| $f_{1,3}\left(x_{3}, x_{2}, x_{4}\right)$ | 0.94 | 0.34 | 0.28 | 0.31 | 0.97 | 0.03 | 0.87 | 0.97 |
| $f_{1,4}\left(x_{4}, x_{2}, x_{5}\right)$ | 0.01 | 0.51 | 0.06 | 0.67 | 0.31 | 0.47 | 0.57 | 0.41 |
| $f_{1,5}\left(x_{5}, x_{1}, x_{6}\right)$ | 0.81 | 0.74 | 0.61 | 0.30 | 0.71 | 0.54 | 0.71 | 0.21 |
| $f_{1,6}\left(x_{6}, x_{1}, x_{3}\right)$ | 0.03 | 0.13 | 0.17 | 0.94 | 0.17 | 0.18 | 0.27 | 0.08 |

- Number of variables, $N$.
- Number of neighbors per variable, $K$.
- A set of neighbors, $\Pi\left(X_{q}\right) \in \mathbf{X}$, for $X_{q}, q \in\{1, \ldots, N\}$ where $\Pi\left(X_{q}\right)$ contains $K$ neighbors.
- A subfunction $f_{q}$ defining a real value for each combination of values of $X_{q}$ and $\Pi\left(X_{q}\right), q \in\{1, \ldots, N\}$.

Both the subfunction $f_{q}$ for each variable $X_{q}$ and the neighborhood structure $\Pi\left(X_{q}\right)$ are randomly set.

For a set of given parameters, the problem consists in finding the global maximum of the function $z_{N K}(\mathbf{x})$.

The MNK-landscape problem is a multi-objective version of the NK fitness landscape model with $R$ objectives (Aguirre and Tanaka 2004), $\mathbf{z}(\mathbf{x})=\left(z_{1}(\mathbf{x}), z_{2}(\mathbf{x}), \ldots\right.$, $\left.z_{R}(\mathbf{x})\right): \mathcal{B}^{N} \rightarrow \mathcal{R}^{R}$. Each objective function is determined by a different instance of an NK-landscape, over the same binary string $\mathbf{x}$, where $N$ is the number of variables ${ }^{1}$, $R$ is the number of objectives, $z_{r}(\mathbf{x})$ is the $r$-ith objective function, and $\mathcal{B}=\{0,1\}$. $\mathbf{K}=\left\{K_{1}, \ldots, K_{R}\right\}$ is a set of integers where $K_{r}$ is the neighborhood size in the $r$-th landscape.

The MNK-landscape problem can be formulated as follows:

$$
\begin{aligned}
& \max _{\mathbf{x}} \mathbf{z}(\mathbf{x})=\left(z_{1}(\mathbf{x}), \ldots, z_{R}(\mathbf{x})\right) \\
& \text { subject to } \mathbf{x} \in\{0,1\}^{N} \\
& \text { with } \\
& z_{r}(\mathbf{x})=\frac{1}{N} \sum_{q=1}^{N} f_{r, q}\left(x_{q}, \Pi_{r}\left(x_{q}\right)\right) \\
& r \in\{1, \ldots R\} \\
& q \in\{1, \ldots N\}
\end{aligned}
$$

where the fitness contribution $f_{r, q}$ of variable $x_{q}$ is a real number in $[0,1]$ drawn from a uniform distribution.

Table 1 presents an example of sub-function values for a particular landscape for one specific objective ( $r=1$, for example), with $N=6$ and $K_{1}=2$ with a neighborhood structure shown in Fig. 2.

[^0]
[^0]:    ${ }^{1}$ The number of variables $N$ is noted $Q$ in Sects. 3 and 4.

Fig. 2 Example of neighborhood structure $(r=1)$
![img-1.jpeg](img-1.jpeg)

In this particular example the objective function for one objective among others ( $r=$ 1) in a multi-objective optimization can be expressed by $z_{1}(\mathbf{x})=\frac{1}{N}\left(f_{1,1}\left(x_{1}, x_{3}, x_{4}\right)+\right.$ $\left.f_{1,2}\left(x_{2}, x_{5}, x_{6}\right)+f_{1,3}\left(x_{3}, x_{2}, x_{4}\right)+f_{1,4}\left(x_{4}, x_{2}, x_{5}\right)+f_{1,5}\left(x_{5}, x_{1}, x_{6}\right)+f_{1,6}\left(x_{6}, x_{1}, x_{3}\right)\right)$. Suppose $\mathbf{x}=(0,1,1,0,0,1)$, the objective function for this objective is represented by $z_{1}(\mathbf{x})=\frac{1}{6}\left(f_{1,1}(0,1,0)+f_{1,2}(1,0,1)+f_{1,3}(1,1,0)+f_{1,4}(0,1,0)+\right.$ $\left.f_{1,5}(0,0,1)+f_{1,6}(1,0,1)\right)$, and considering the subfunctions from Table 1, it results in $z_{1}(\mathbf{x})=\frac{1}{6}(0.74+0.15+0.87+0.06+0.74+0.18)=0.46$. More details and examples about the MNK-landscape model can be found in Santana et al. (2015).

# 3 Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm (HMOBEDA) 

HMOBEDA is a hybrid EDA approach introduced in Martins et al. (2016) ${ }^{2}$. The term hybrid refers to the inclusion of local search (LS) mechanisms into its PGM-based framework to improve the performance and allow the algorithm to better refine the search process.

HMOBEDA uses a probabilistic model based on Bayesian networks for the objectives, variables and local search parameters to sample new individuals. Therefore, every solution is represented by a joint vector containing $Q+R+L$ elements denoted $\mathbf{y}=(\mathbf{x}, \mathbf{z}, \mathbf{p})=\left(X_{1}, \ldots, X_{Q}, Z_{1}, \ldots, Z_{R}, P_{1}, \ldots, P_{L}\right)$, where $\left(X_{1}, \ldots, X_{Q}\right)$ are the decision variables, $\left(Z_{1}, \ldots, Z_{R}\right)$ are the objectives and $\left(P_{1}, \ldots, P_{L}\right)$ are the LS parameters. The general scheme of the HMOBEDA is presented in Fig. 3.

### 3.1 HMOBEDA main steps

In the context of the addressed MNK-landscape problem, the Initialization phase loads the problem instance for a given $M, N$ and $K$ (both the subfunctions and the neighborhood structure are obtained from a uniform distribution) and randomly generates an initial population. Each solution is a binary string of size $N=Q$ and the corresponding objectives are calculated through the MNK-landscape model.

A Local Search based on the Hill Climbing procedure is used to generate a neighborhood for each solution at each iteration. The best found solution is updated at each iteration once a neighboring solution with a better fitness is found (first improvement strategy).

[^0]
[^0]:    ${ }^{2}$ The source codes are available at https://bitbucket.org/marcella_engcomp/hmobeda.

![img-2.jpeg](img-2.jpeg)

Fig. 3 The HMOBEDA framework

In order to select a total of $N_{P G M}$ individuals from the current population, the Non-dominated Sorting (ND) (Srinivas and Deb 1994) technique is applied. After ND organizes the population based on a set of PFs (the second PF is dominated by the first, the third by the second and so on...), the Selection procedure randomly selects two solutions and the one positioned in the best front is chosen. If they lie on the same front, it chooses that solution with the greatest crowding distance (Deb et al. 2002).

Aiming to learn the probabilistic model, the BN structure and parameters are estimated in the PGM Learning block. Different algorithms can be considered: in this work we compare several structure learning algorithms running over the set of $N_{P G M}$ best individuals. This way the BN structure encodes a factorization of the joint probability distributions or the probability mass function (pmf) given by:

$$
p(\mathbf{y})=\prod_{r=1}^{R} p\left(z_{r} \mid \mathbf{p a}_{r}^{B}\right) \cdot \prod_{q=1}^{Q} p\left(x_{q} \mid \mathbf{p a}_{q}^{B}\right) \cdot \prod_{l=1}^{L} p\left(p_{l} \mid \mathbf{p a}_{l}^{B}\right)
$$

where $\mathbf{p a}_{r}^{B}, \mathbf{p a}_{q}^{B}$ and $\mathbf{p a}_{l}^{B}$ represent combinations of values for the parents of objective, decision variable and LS parameter nodes respectively, with $\mathbf{P a}_{q}^{B} \subseteq\left\{Z_{1}, \ldots Z_{R}\right\}$, $\mathbf{P a}_{l}^{B} \subseteq\left\{Z_{1}, \ldots Z_{R}\right\}, \mathbf{P a}_{r}^{B}=\emptyset$, which means $p\left(z_{r} \mid \mathbf{p a}_{r}^{B}\right)=p\left(z_{r}\right)$ for $r=1, \ldots, R$. Therefore, according to Eq. 6 and Fig. 3, the BN adopted in HMOBEDA is a naive model which does not consider arcs among variables $Z, X$ or $P$. Other models could be adopted like the Hierarchical Bayesian Optimization Algorithm (Pelikan et al. 2003) which has been reported to be more suitable to deal with dependencies between variables, objectives and to automatically control the application of local search operators. However, expanding the PGM model is out of the scope of this paper.

In the Sampling block, the obtained PGM is used to sample the set of new individuals. As discussed in Martins et al. (2017), Martins et al. (2018), the main advantage of using the HMOBEDA framework, is that not only decision variables, but also LS parameters can be obtained through the Sampling block. Note that a naive Bayesian model is adopted to facilitate the sampling process: fixing objective values as target evidences enables the estimation of their associated decision variables and LS parameters. Therefore, after sampling, decision variables $\left(X_{1}, \ldots, X_{Q}\right)$ and LS parameters

$\left(P_{1}, \ldots, P_{L}\right)$ more related to the objectives fixed as evidences can be drawn for each new individual.

HMOBEDA considers evidences fixed as combinations (all of them with the same probability of occurrence) of maximum and minimum values for the objectives, i.e., the ideal point $Z^{* 3}$ plus the estimated extreme points of the current approximation of the Pareto front. These values are uniformly distributed according the number of objectives in each generation (excluding the combination with minimum values for all objectives).

Finally, objectives $\left(Z_{1}, \ldots, Z_{R}\right)$ are calculated based on the fitness function (in the case of surrogate assisted approaches, PGM can also be used to sample the objective values or the least squares method can provide objective value approximations). The union of the sampled and the current populations in the Survival block is used to create the new population for the next generation, and the main loop continues until the stop condition is achieved.

In this paper, we present seven variants of HMOBEDA using different score, constraint and hybrid-based PGM learning techniques: $\mathrm{HMOBEDA}_{k 2}, \mathrm{HMOBEDA}_{h c-k 2}$, $\mathrm{HMOBEDA}_{i a m b}, \mathrm{HMOBEDA}_{p c}, \mathrm{HMOBEDA}_{m m h c}, \mathrm{HMOBEDA}_{\text {sparse }}$ and $\mathrm{HMOBEDA}_{t a b u} . \mathrm{HMOBEDA}_{k 2}$ uses the score based K2 algorithm as the structure learning technique; $\mathrm{HMOBEDA}_{h c-k 2}$ is also score-based which considers Hill-Climbing using K2-metric (HC-K2); $\mathrm{HMOBEDA}_{i a m b}$ and $\mathrm{HMOBEDA}_{p c}$ use constraint-based methods applying, respectively, PC-Stable implementation algorithm (PC) and Incremental Association Markov Blanket (IAMB); $\mathrm{HMOBEDA}_{m m h c}$ is a hybrid approach based on Max-Min Hill Climbing (MMHC) algorithm and in this paper we apply K2 as its score metric; $\mathrm{HMOBEDA}_{\text {sparse }}$ is score-based approach based on sparse regularization (Aragam et al. 2019) and $\mathrm{HMOBEDA}_{\text {tabu }}$ is also a score-based which uses Tabu as a search strategy (Russell Stuart and Norvig 2009). $\mathrm{HMOBEDA}_{\text {sparse }}$ and $\mathrm{HMOBEDA}_{\text {tabu }}$, both, consider BDe as their score metric (Heckerman et al. 1995).

The choice of these structure learning approaches is based on their adoption in the recent literature (Martins et al. 2017; Ding and Zhuang 2018; Scutari et al. 2018; Tsagris 2019). They also represent examples of popular and state-of-the-art score-based, constraint-based and hybrid approaches of structure learning algorithms according to Scutari (2009).

In this paper, every new BN structure is learned from scratch at each iteration. In the future, we can explore strategies using a previous BN to improve the computational time such as in Pelikan et al. (2008). Moreover, metrics and procedures can be used to evaluate the accuracy of the model with respect to a reference underlying problem structure (Pelikan and Hauschild 2012; Lima et al. 2011; Echegoyen et al. 2007; Brownlee et al. 2012). Although most authors agree that capturing important problem interactions is beneficial for the model, others acknowledge this accuracy but consider that complex models might be inefficient for the evolutionary search (Echegoyen et al. 2011). Note that our BN model includes not only the objectives and variables of the

[^0]
[^0]:    ${ }^{3}$ Usually high values for maximization problems: the ideal point $Z^{*}$ is the maximum value of each objective achieved so far.

problem, but also the parameters of the algorithm. Therefore, the learning of problem structure can be considered in the future as well.

# 4 Experiments and results 

In this section, we compare HMOBEDA variants obtained from BN structure learning algorithms discussed in the previous section: score-based (HMOBEDA $\mathrm{A}_{k 2}$, $\mathrm{HMOBEDA}_{h c-k 2}, \mathrm{HMOBEDA}_{\text {sparse }}$ and $\mathrm{HMOBEDA}_{\text {tabu }}$ ), constraint-based (HMOBEDA ${ }_{i a m b}$ and $\mathrm{HMOBEDA}_{p c}$ ), and a score-constraint-based hybrid method (HMOBEDA ${ }_{m m h c}$ ).

The comparison is performed over MNK-landscape instances using the Hypervolume $\left(\mathrm{HV}^{-}\right)$indicator and the IDG metric. The traditional Hypervolume (HV) measures the space (considering a reference point) which is dominated by at least one point in the approximated Pareto front provided by a solution set of an algorithm, while $\mathrm{HV}^{-}$ considers the difference between the hypervolume from both the solution set and the reference set. The IGD metric is the average distance from every point in the Pareto front associated with the reference set to the nearest point in the approximated Pareto front. So, smaller values of $\mathrm{HV}^{-}$and IGD correspond to high quality solutions of the non-dominated sets in terms of convergence (measured by $\mathrm{HV}^{-}$) and coverage (measured by IGD) when compared with the reference set. The Pareto optimal front for each instance of the addressed problem is not known. Therefore, we use a reference set which is constructed by gathering all non-dominated solutions from all the HMOBEDA variants over all executions.

MNK-landscape instances are sampled using different ruggedness factors $K \in$ $\{2,4,6,8,10\}$, number of objectives $R \in\{2,3,5,8\}$ and sizes $N=Q \in$ $\{20,50,100\}$. A total of 60 instances are generated, one for each combination of $K, R$ and $N$. The same strategy is adopted in Martins et al. (2018).

As shown in previous works (Martins et al. 2018, 2017, 2016, 2017), the BN parameters $\Theta$ are estimated by Bayesian Estimate using Dirichlet prior. For all HMOBEDA variants, structure learning algorithms set parent nodes as objectives in the Bayesian network. This is because, fixing the objective values as target evidences allows a straightforward estimation of their associated decision variables and LS parameters.

The parameters for all HMOBEDA variants considered in this section are: population size $P o p=100$, number of selected individuals $N_{P G M}=P o p / 2$ for building the PGM, and number of sampled individuals $N_{s m p}=10 * N$. The LS online configuration of HMOBEDA variants during the evolution has the following elements in vector $\mathbf{p}$ : number of LS iterations $N_{\text {iter }} \in\{5,6 \ldots, 20\}$ i.e., 16 possible discrete values between 5 and 20 ; type of neighbor fitness calculation $T_{F n b h} \in\{1,2\}$ with 1 being a linear combination of objectives and 2 being alternating objectives (i.e., one by one for each LS iteration); neighborhood type $T_{n b h} \in\{1,2\}$ with 1 corresponding to defining double bit-flip operator and 2 being the single bit-flip from 0 to 1 . These parameters have been defined experimentally in previous works (Martins et al. 2017, 2016).

![img-3.jpeg](img-3.jpeg)

Fig. 4 Average run-times (min) for each instance and HMOBEDA variant

The stopping condition is the maximum number of fitness evaluations $\left(\operatorname{Max}_{\text {eval }}\right)$ including repair procedures and LS iterations. All algorithms stop when the total number of fitness computations achieves 200, 000 evaluations. A total of 30 independent executions of each algorithm is performed for each instance of the addressed problem to get average performance metrics.

Shapiro-Wilk normality test is used to verify whether the performance metric results are normally distributed and the analysis of variance test (ANOVA) is used in this case. In the case of non-normal distribution, Kruskal-Wallis (de Mattos Neto et al. 2020) and Dunn-Sidak's post-hoc tests are considered when performing multiple comparisons. Mann-Whitney-Wilcoxon (Santana et al. 2019) test is used when only two approaches are compared.

# 4.1 Optimization performance: multicriteria analysis 

In this section, we aim to compare the learning structure algorithm considering three different performance criteria: computational cost, PF convergence and PF coverage, measured by run-times, $\mathrm{HV}^{-}$and IGD, respectively.

The average run-times (min) for each instance and variant are presented in Fig. 4. They are averaged over 30 executions of the variant in each instance. We notice that score-based algorithms present the lowest (for $\mathrm{HMOBEDA}_{k 2}$ ) and the highest (for $\mathrm{HMOBEDA}_{h c-k 2}$ ) computational run-times. The Kruskal-Wallis and Dunn-Sidak's post-hoc tests are applied with a significance level $\alpha=5 \%$, indicating that, for almost all instances, the differences are statistically significant. Note that Fig. 4 shows runtimes increase according to the instance complexity as expected for all algorithms, but $\mathrm{HMOBEDA}_{k 2}$ requires less computational effort than other algorithms.

![img-4.jpeg](img-4.jpeg)

Fig. 5 Boxplot of a $\mathrm{HV}^{-}$and $\mathbf{b}$ IGD values averaged over 60 instances for each HMOBEDA variant

Aiming to evaluate if the lowest computational cost required by $\mathrm{HMOBEDA}_{k 2}$ yields to poor performance in terms of convergence and coverage, we conducted experiments comparing the hypervolume and distances of the resulting PFs with the reference PF. Figure 5a, b show the boxplots of hypervolume difference $\mathrm{HV}^{-}$and IGD metric values averaged over 60 instances for each HMOBEBA variant. These plots show that $\mathrm{HMOBEDA}_{k 2}$ has a similar performance when compared to the others with regards to $\mathrm{HV}^{-}$and IGD.

In addition, by considering each individual instance with 30 independent executions of each algorithm, the Kruskal-Wallis and Dunn-Sidak's post-hoc tests with a significance level $\alpha=5 \%$ show that there is no statistically significant differences from $\mathrm{HMOBEDA}_{k 2}$ to the others for most instances regarding both $\mathrm{HV}^{-}$indicator and IGD metric.

Based on the previous results, under multicriteria analysis, we conclude that $\mathrm{HMOBEDA}_{k 2}$ is the best option because it dominates the others in one criterion (run-times) without degenerating the other two (convergence and coverage).

# 4.2 Robustness performance: sensibility analysis 

In this section, we are interested in verifying the capability of the BN models to provide solutions less sensitive to noise. In this work, a solution is robust if small perturbations around it do not affect significantly the corresponding objective values (Meneghini et al. 2016). In this paper, this is accomplished by a sensibility analysis performed by (i) sampling a set of solutions coded into the final BN model for each execution and (ii) adding noise to them to evaluate the new Pareto front. Robust solutions are then identified if minor changes are observed in the resulting noisy Pareto front. The sensibility analysis encompasses the following steps.

1. Capture the final BN model and sample a set of $N_{\text {smp }}^{\text {end }}=1000 *$ Pop solutions called Pop $_{s}$ where $P o p$ is the population size;
2. Apply a perturbation/noise on each solution vector $\mathbf{x}$ of $P o p_{s}$, and compute a noisy solution set $P o p_{s n}$. Because this paper addresses a combinatorial problem, the noise is represented by a double bit-flip from 0 to 1 on the decision variable vectors of $P o p_{s}$. The probability for a solution to be mutated using a double bit-flip is defined as $p_{s n}=0.15$;

Fig. 6 Example (one execution) of approximated Pareto fronts $P F_{s}$ in blue and $P F_{s n}$ in red for 2 objectives, $N=20$ and $K=8$. Overlapping points are shown in black (Color figure online)
![img-5.jpeg](img-5.jpeg)
3. Non-dominated solutions are then obtained from sets $P o p_{s}$ and $P o p_{s n}$.
4. Compute the pmf function given by Eq. 6 for each non-dominated solution. This solution is represented by a circle proportional to its marginal probability; $P\left(Z_{1}=\right.$ $\left.z_{1}, \ldots, Z_{M}=z_{M}\right)$ (Martins et al. 2017);
5. For robustness evaluation purposes, select solutions with high probability (e.g. $p_{\text {limit }}>0.5$ ).
The selected solutions are used to build two approximated Pareto fronts $P F_{s n}$ and $P F_{s}$ with and without noise, respectively. An example of such Pareto fronts is shown in Fig. 6.

The Pareto fronts provided by the two populations $P o p_{s}$ and $P o p_{s n}$ are compared each other by their respective $\mathrm{HV}^{-}$indicators and IGD metrics. It aims at investigating how sensitive are the most probable solutions provided by each PGM learning technique. The results are shown in Fig. 7 and 8 as linear regressions in red with the corresponding $\beta$ coefficient, and the quadrant bisector in black. Note that $\mathrm{HMOBEDA}_{k 2}$ and $\mathrm{HMOBEDA}_{h c-k 2}$ have coefficients (in bold) close to the bisector.

The data used in the scatter plots are average values over 30 executions of each algorithm in each instance given by Tables 2 and 3 of the Appendix. The Mann-Whitney-Wilcoxon test with $\alpha=5 \%$ is applied for the statistical analysis of the results. There are no statistically significant differences between $P F_{s}$ and $P F_{s n}$ for $\mathrm{HMOBEDA}_{k 2}$ and $\mathrm{HMOBEDA}_{h c-k 2}$ in almost all instances.

Based on the results of Figs. 7 and 8 supported by the statistical analysis of Tables 2 and 3, $\mathrm{HMOBEDA}_{k 2}$ and $\mathrm{HMOBEDA}_{h c-k 2}$ are less sensitive to noise. Therefore, the structure learning algorithm implemented by K2 and HC-K2 can provide a robust PGM model for HMOBEDA. However, $\mathrm{HMOBEDA}_{h c-k 2}$ is time consuming as shown in Fig. 4.

# 4.3 Learning performance: PGM variability analysis 

In this section, the learning capability of each algorithm is evaluated based on the distance between the PGM and a target model using the Structural Hamming Distance (SHD) (Tsamardinos et al. 2006).

![img-6.jpeg](img-6.jpeg)

Fig. 7 Linear regression of average $\mathrm{HV}^{-}$indicators $\left(\mathrm{PF}_{k}\right.$ versus $\left.\mathrm{PF}_{k n}\right)$ in red for each HMOBEDAvariant: a $\mathrm{HMOBEDA}_{k 2}$ with $\mathbf{f i}=\mathbf{1 . 1 4 7 8}, \mathbf{b} \mathrm{HMOBEDA}_{p c}$ with $\beta=1.2426$, c $\mathrm{HMOBEDA}_{m m b c}$ with $\beta=1.2459$, d $\mathrm{HMOBEDA}_{i a m b}$ with $\beta=1.2404$, e $\mathrm{HMOBEDA}_{h c-k 2}$ with $\mathbf{f i}=\mathbf{1 . 1 6 1 3}, \mathbf{f}$ HMOBEDA ${ }_{s p a r s e}$ with $\beta=1.2420, \mathrm{~g} \mathrm{HMOBEDA}_{t a b u}$ with $\beta=1.2410$ (Color figure online)

![img-7.jpeg](img-7.jpeg)

Fig. 8 Linear regression of average IGD metrics $\left(\mathrm{PF}_{x}\right.$ versus $\left.\mathrm{PF}_{y n}\right)$ in red for each HMOBEDAvariant: a $\mathrm{HMOBEDA}_{k 2}$ with $\mathbf{f i}=\mathbf{1 . 1 5 2 3}, \mathbf{b} \mathrm{HMOBEDA}_{p c}$ with $\beta=1.2452$, c $\mathrm{HMOBEDA}_{m m b c}$ with $\beta=1.2462$, d $\mathrm{HMOBEDA}_{i a m b}$ with $\beta=1.2457$, e $\mathrm{HMOBEDA}_{h c-k 2}$ with $\mathbf{f i}=\mathbf{1 . 1 7 0 6}$, f $\mathrm{HMOBEDA}_{s p a r s e}$ with $\beta=1.2492$, g $\mathrm{HMOBEDA}_{t a b u}$ with $\beta=1.2043$ (Color figure online)

The SHD metric has been chosen due to its popularity to evaluate the learning of Bayesian network structure (Viinikka et al. 2018). This metric requires a reference structure model called target model which is different of the typical reference model used to analyze the accuracy of EDAs (usually the structure of the function or the structure of the problem when it is available). In our case, the challenge is the absence of a previously known target model. Similarly to (Viinikka et al. 2018), we thus used a target model represented by the Bayesian network learned for the best Pareto front (with the best hypervolume $\mathrm{HV}^{-}$) found among all algorithms and executions. Using this target model we expect to compare how far the BN models computed by each algorithm are from the one capable of achieving the best results. For each instance, the target model is chosen among the BN models of the best Pareto fronts found by all algorithms and executions, i.e., the target model is defined as the 'best one' among 210 BNs ( 30 executions of each seven algorithms) with the best $\mathrm{HV}^{-}$. This means that the BN corresponding to the best Pareto front (regarding hypervolume) among these 210 ones is selected as the target model for a given instance.

Therefore, we perform in this section a variability analysis among PGM structures. Furthermore, we evaluate each PGM learning technique based on its ranking, i.e., the number of times it achieves the minimum distance from the target model then the second minimum distance, and so on. In other words, we compare individual BN models directly from each execution and compute the quality of each learning technique based on the distance of its resulting BN from a target model.

The SHD metric compares the structure of learned and target networks (Tsamardinos et al. 2006). We define the SHD as the number of operations required to match the learned and target networks using add, remove and reverse (edges) operations. A ranking of HMOBEDA variants is then computed for each problem instance based on the number of times an algorithm presents the best SHD values over 30 executions. Figure 9 shows the histogram of the rank distributions for each HMOBEDA variant considering all problem instances.

According to Fig. 9a, b, we notice that $\mathrm{HMOBEDA}_{k 2}$ and $\mathrm{HMOBEDA}_{h c-k 2}$ are ranked in the first four positions with better results for $\mathrm{HMOBEDA}_{k 2}$ (greater number of times being in the first rank). Similarly to the previous sections, $\mathrm{HMOBEDA}_{k 2}$ appears as the best option as it provides BN structures close to the PGM target model more often. By approaching the target model more often, $\mathrm{HMOBEDA}_{k 2}$ is expected to better represent the underlying relationship among objectives, variables, and parameters that provides better optimization results with even less computational effort.

Based on the experiments, we conclude that $\mathrm{HMOBEDA}_{k 2}$ outperformed the other variants because, in spite of using less computational time (see Fig. 4), it provides comparable optimization results, less sensitive solutions to noise, and BN structures close to the target model more often.

# 5 Conclusion 

In this paper we have explored different BN learning techniques for a hybrid EDA which is based on a joint Bayesian network model of variables, local search parameters and objectives applied to multi- and many-objective combinatorial optimization. We

![img-8.jpeg](img-8.jpeg)
![img-9.jpeg](img-9.jpeg)
(g) $\mathrm{HMOBEDA}_{t a b u}$

Fig. 9 Histogram for the HMOBEDA variants: number of times the corresponding algorithm presents the ranks $1,2,3,4,5,6$ and 7 along the 30 executions considering all instances: a $\mathrm{HMOBEDA}_{k 2}$, b $\mathrm{HMOBEDA}_{p c}$, c $\mathrm{HMOBEDA}_{m m h c}$, d $\mathrm{HMOBEDA}_{i a m b}$, e $\mathrm{HMOBEDA}_{h c-k 2}$, f $\mathrm{HMOBEDA}_{s p a r s e}$, and g $\mathrm{HMOBEDA}_{t a b u}$

have modified the original HMOBEDA to build other versions with different score-, constraint- and hybrid-based learning techniques: $\mathrm{HMOBEDA}_{k 2}, \mathrm{HMOBEDA}_{h c-k 2}$, $\mathrm{HMOBEDA}_{i a m b}, \mathrm{HMOBEDA}_{p c}$ and $\mathrm{HMOBEDA}_{m m h c}$.

In the experiments, we have analyzed the performance of each of those HMOBEDA variants on instances of the MNK-landscape problem with 2, 3, 5 and 8 objectives considering the hypervolume $\left(\mathrm{HV}^{-}\right)$indicator and the Inverted Generational Distance (IGD) metric.

For the instances considered in this work, we observed that, under a multicriteria optimization analysis, $\mathrm{HMOBEDA}_{k 2}$ has outperformed the others in one performance criterion (run times) without decreasing the other two (convergence and coverage of its resulting Pareto fronts). Besides, a direct comparison based on the Structural Hamming Distance (SHD), between BN models generated at the end of the evolutionary process and a target BN, revealed better models (close to the target one) for $\mathrm{HMOBEDA}_{k 2}$. We believe that, this result emphasizes the better learning capability of $\mathrm{HMOBEDA}_{k 2}$ when compared with the other variants.

In addition, our analysis of robust solutions coded into the BN models has concluded that $\mathrm{HMOBEDA}_{k 2}$ and $\mathrm{HMOBEDA}_{h c-k 2}$ produce solutions that are less sensitive to noise compared to the other HMOBEDA variants. However, as $\mathrm{HMOBEDA}_{k 2}$ requires less computing time it can be considered the best option to provide BN models to HMOBEDA.

An interesting future research direction is using other types of PGM as hBOA. Moreover, in addition to the operators addressed in this work, other EDA parameters could be considered, as well as the effectiveness of learning the problem structure for an efficient search. Another direction to be considered in the future is the expansion of the analysis for different MNK parameters and configurations. Fitness landscape analysis could also be useful to acquire knowledge about the behavior and performance of structure learning algorithms for different types of instances. Finally, the work can be extended to other problems such as the multi-objective knapsack and multi-objective clustering problems.

Acknowledgements M. Delgado acknowledges CNPq, grants 309935/2017-2 e 439226/2018-0. R. Santana acknowledges support by the TIN2016-78365-R (Spanish Ministry of Economy, Industry and Competitiveness), PID2019-104966GB-I00 (Spanish Ministry of Science and Innovation), the IT-1244-19 (Basque Government) program and project 3KIA (KK-2020/00049) funded by the SPRI-Basque Government through the ELKARTEK program.

# Appendix 

Tables 2 and 3 present the respective $\mathrm{HV}^{-}$indicator and IGD metric to the approximated Pareto fronts provided by the two populations $P F_{s}$ and $P F_{s n}$. The values are averaged over the results of 30 executions of each algorithm. The Mann-WhitneyWilcoxon test with $\alpha=5 \%$ is applied for the statistical analysis of the results. Values of $P F_{s}$ and $P F_{s n}$ for each algorithm and instance with background in light blue have no statistically significant differences. The values in bold correspond to the best values for the paiwise comparison between $P F_{s}$ and $P F_{s n}$ for each HMOBEDA variant.

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

# References 

Aguirre, H.E., Tanaka, K.: Insights on properties of multiobjective MNK-landscapes. In: Proceedings of the 2004 Congress on Evolutionary Computation, vol. 1, pp. 196-203. IEEE, Portland (2004)
Aguirre, H.E., Tanaka, K.: Working principles, behavior, and performance of MOEAs on MNK-landscapes. Eur. J. Oper. Res. 181(3), 1670-1690 (2007)
Aragam, B., Gu, J., Zhou, Q.: Learning large-scale Bayesian networks with the sparsebn package. J. Stat. Softw. 91(11), 1-38 (2019)
Bengoetxea, E., Larrañaga, P., Bielza, C., Del Pozo, J.F.: Optimal row and column ordering to improve table interpretation using estimation of distribution algorithms. J. Heurist. 17(5), 567-588 (2011)
Bennett, K.P., Parrado-Hernández, E.: The interplay of optimization and machine learning research. J. Mach. Learn. Res. 7, 1265-1281 (2006)
Brownlee, A.E., McCall, J.A., Pelikan, M.: Influence of selection on structure learning in Markov network EDAs: an empirical study. In: Proceedings of the 14th Annual Conference on Genetic and Evolutionary Computation, pp. 249-256 (2012)
Buntine, W.: Theory refinement on Bayesian networks. In: Uncertainty Proceedings, pp. 52-60. Elsevier (1991)

Colombo, D., Maathuis, M.H.: Order-independent constraint-based causal structure learning. J. Mach. Learn. Res. 15(1), 3741-3782 (2014)
Cooper, G., Herskovits, E.: A Bayesian method for the induction of probabilistic networks from data. Mach. Learn. 9(4), 309-347 (1992)
Deb, K., Agrawal, S., Pratab, A., Meyarivan, T.: A fast and elitist multi-objective genetic algorithm: NSGAII. IEEE Trans. Evolut. Comput. 6, 182-197 (2002)

Ding, F., Zhuang, Y.: Distributed Bayesian network learning algorithm using storm topology. Int. J. Grid Distrib. Comput. 11(4), 113-126 (2018)
de Mattos Neto, P.S., Marinho, M.H., Siqueira, H., de Souza Tadano, Y., Machado, V., AntoniniAlves, T., de Oliveira, J.F.L., Madeiro, F.: A methodology to increase the accuracy of particulate matter predictors based on time decomposition. Sustainability 12(18), 7310 (2020)
Echegoyen, C., Lozano, J.A., Santana, R., Larrañaga, P.: Exact Bayesian network learning in estimation of distribution algorithms. In: 2007 IEEE Congress on Evolutionary Computation, pp. 1051-1058. IEEE (2007)

Echegoyen, C., Zhang, Q., Mendiburu, A., Santana, R., Lozano, J.A.: On the limits of effectiveness in estimation of distribution algorithms. In: 2011 IEEE Congress of Evolutionary Computation (CEC), pp. 1573-1580. IEEE (2011)
Heckerman, D., Geiger, D., Chickering, D.: Learning Bayesian networks: the combination of knowledge and statistical data. Mach. Learn. 20(3), 197-243 (1995)
Henrion, M.: Propagating uncertainty in Bayesian networks by probabilistic logic sampling. In: Machine Intelligence and Pattern Recognition, vol. 5, pp. 149-163. Elsevier (1988)
Karshenas, H., Santana, R., Bielza, C., Larrañaga, P.: Multiobjective estimation of distribution algorithm based on joint modeling of objectives and variables. IEEE Trans. Evol. Comput. 18, 519-542 (2014)
Kauffman, S.A.: The Origins of Order: Self-organization and Selection in Evolution. Oxford University Press, New York (1993)
Khan, N., Goldberg, D.E., Pelikan, M.: Multi-objective Bayesian optimization algorithm. Technical report, University of Illinois at Urbana-Champaign, Illinois Genetic Algorithms Laboratory-Tech Report no.2002009, Urbana, IL (2002)
Kollat, J.B., Reed, P., Kasprzyk, J.: A new epsilon-dominance hierarchical Bayesian optimization algorithm for large multiobjective monitoring network design problems. Adv. Water Resour. 31(5), 828-845 (2008)

Larrañaga, P., Karshenas, H., Bielza, C., Santana, R.: A review on probabilistic graphical models in evolutionary computation. J. Heuristics 18(5), 795-819 (2012)
Larrañaga, P., Lozano, J.A.: Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Kluwer Academic Publishers, New York (2001)
Lauritzen, S.L.: Graphical Models. Oxford Clarendon Press, Oxford (1996)
Lima, C.F., Lobo, F.G., Pelikan, M., Goldberg, D.E.: Model accuracy in the Bayesian optimization algorithm. Soft. Comput. 15(7), 1351-1371 (2011)

Marti, L., Garcia, J., Berlanga, A., Molina, J.M.: Model-building algorithms for multiobjective EDAs: directions for improvement. In: IEEE Conference on Evolutionary Computation. CEC'2008, pp. 28432850. IEEE, Piscataway, NJ (2008)

Martins, M.S., Delgado, M., Lüders, R., Santana, R., Gonçalves, R.A., de Almeida, C.P.: Exploring the probabilistic graphic model of a hybrid multi-objective Bayesian estimation of distribution algorithm. Appl. Soft Comput. (2018). https://doi.org/10.1016/j.asoc.2018.08.039
Martins, M.S., Delgado, M.R., Lüders, R., Santana, R., Ricardo, Gonçalves, Almeida, C.P.d.: Probabilistic analysis of Pareto Front approximation for a hybrid multi-objective bayesian estimation of distribution algorithm. In: Proceedings of the 2017 Brazilian Conference on Intelligent Systems, BRACIS'17, pp. 384-389 (2017)
Martins, M.S., Delgado, M.R., Santana, R., Lüders, R., Gonçalves, R.A., Almeida, C.P.D.: HMOBEDA: hybrid multi-objective bayesian estimation of distribution algorithm. In: Proceedings of the Genetic and Evolutionary Computation Conference, GECCO'16, pp. 357-364. ACM, New York, NY (2016)
Martins, M.S., El Yafrani, M., Santana, R., Delgado, M.R., Lüders, R., Ahiod, B.: On the performance of multi-objective estimation of distribution algorithms for combinatorial problems. In: IEEE Conference on Evolutionary Computation, CEC'18, pp. 1-8. arXiv:1806.09935 (2018)
Martins, M.S.R., Delgado, M.R.B.S., Lüders, R., Santana, R., Gonçalves, R.A., de Almeida, C.P.: Hybrid multi-objective Bayesian estimation of distribution algorithm: a comparative analysis for the multiobjective knapsack problem. J. Heuristics 8, 1-23 (2017)
Meneghini, I.R., Guimaraes, F.G., Gaspar-Cunha, A.: Competitive coevolutionary algorithm for robust multi-objective optimization: the worst case minimization. In: 2016 IEEE Congress on Evolutionary Computation (CEC), pp. 586-593. IEEE (2016)
Moran, S., He, Y., Liu, K.: Choosing the best Bayesian classifier: an empirical study. IAENG Int. J. Comput. Sci. 36(4), 322-331 (2009)
Mühlenbein, H., Paab, G.: From Recombination of Genes to the Estimation of Distributions I. Binary Parameters. Parallel Problem Solving from Nature. PPSN IV-Lecture Notes in Computer Science, vol. 1411, pp. 178-187. Springer, London (1996)
Pelikan, M., Goldberg, D.E., Tsutsui, S.: Hierarchical bayesian optimization algorithm: toward a new generation of evolutionary algorithms. In: SICE 2003 Annual Conference (IEEE Cat. No. 03TH8734), vol. 3, pp. 2738-2743. IEEE (2003)
Pelikan, M., Hauschild, M.W.: Learn from the past: improving model-directed optimization by transfer learning based on distance-based bias. Missouri Estimation of Distribution Algorithms Laboratory, University of Missouri in St. Louis, MO, United States. Technical Report 2012007 (2012)
Pelikan, M., Sastry, K., Goldberg, D.E.: iBOA: The incremental Bayesian optimization algorithm. In: Proceedings of the 10th Annual Conference on Genetic and Evolutionary Computation, pp. 455-462 (2008)

Puchta, E.D., Lucas, R., Ferreira, F.R., Siqueira, H.V., Kaster, M.S.: Gaussian adaptive PID control optimized via genetic algorithm applied to a step-down dc-dc converter. In: 2016 12th IEEE International Conference on Industry Applications (INDUSCON), pp. 1-6. IEEE (2016)
Puchta, E.D., Siqueira, H.V., Kaster, M.D.S.: Optimization tools based on metaheuristics for performance enhancement in a Gaussian adaptive PID controller. IEEE Trans. Cybern. 50(3), 1185-1194 (2020)
Ribeiro, V.H.A., Reynoso-Meza, G., Siqueira, H.V.: Multi-objective ensembles of echo state networks and extreme learning machines for streamflow series forecasting. Eng. Appl. Artif. Intell. 95, 103910 (2020)

Russell Stuart, J., Norvig, P.: Artificial Intelligence: A Modern Approach. Prentice Hall, Upper Saddle River (2009)

Santana, R., Larrañaga, P., Lozano, J.A.: Combining variable neighborhood search and estimation of distribution algorithms in the protein side chain placement problem. J. Heuristics 14, 519-547 (2008)
Santana, R., Mendiburu, A., Lozano, J.A.: Evolving MNK-landscapes with structural constraints. In: IEEE Congress on Evolutionary Computation. CEC'15, pp. 1364-1371. IEEE, Sendai (2015)
Santana, R., Mendiburu, A., Lozano, J.A.: Multi-objective NM-landscapes. In: Proceedings of the Companion Publication of the 2015 Annual Conference on Genetic and Evolutionary Computation, GECCO'15, pp. 1477-1478. ACM, Orlando, FL (2015)
Santana Jr., C.J., Macedo, M., Siqueira, H., Gokhale, A., Bastos-Filho, C.J.: A novel binary artificial bee colony algorithm. Future Gen. Comput. Syst. 98, 180-196 (2019)
Santhanam, N.P., Wainwright, M.J.: Information-theoretic limits of selecting binary graphical models in high dimensions. IEEE Trans. Inf. Theory 58(7), 4117-4134 (2012)

Santos, P., Macedo, M., Figueiredo, E., Santana, C.J., Soares, F., Siqueira, H., Maciel, A., Gokhale, A., Bastos-Filho, C.J.: Application of pso-based clustering algorithms on educational databases. In: 2017 IEEE Latin American Conference on Computational Intelligence (LA-CCI), pp. 1-6. IEEE (2017)
Scanagatta, M., Salmerón, A., Stella, F.: A survey on Bayesian network structure learning from data. In: Progress in Artificial Intelligence, pp. 1-15 (2019)
Scutari, M.: Learning Bayesian networks with the bnlearn r package. arXiv:0908.3817 (2009)
Scutari, M., Graafland, C.E., Gutiérrez, J.M.: Who learns better Bayesian network structures: constraintbased, score-based or hybrid algorithms? In: International Conference on Probabilistic Graphical Models, pp. 416-427 (2018)
Shah, R., Reed, P.: Comparative analysis of multiobjective evolutionary algorithms for random and correlated instances of multiobjective d-dimensional knapsack problems. Eur. J. Oper. Res. 211(3), 466-479 (2011)

Shim, V.A., Tan, K.C., Chia, J.Y., Al Mamun, A.: Multi-objective optimization with estimation of distribution algorithm in a noisy environment. Evol. Comput. 21(1), 149-177 (2013)
Srinivas, N., Deb, K.: Multiobjective optimization using nondominated sorting in genetic algorithms. Evol. Comput. 2, 221-248 (1994)
Tsagris, M.: Bayesian network learning with the pc algorithm: an improved and correct variation. Appl. Artif. Intell. 33(2), 101-123 (2019)
Tsamardinos, I., Aliferis, C.F., Statnikov, A.R., Statnikov, E.: Algorithms for large scale Markov blanket discovery. In: FLAIRS Conference, vol. 2, pp. 376-380. AAAI Press, St. Augustine, FL (2003)
Tsamardinos, I., Brown, L.E., Aliferis, C.F.: The max-min hill-climbing Bayesian network structure learning algorithm. Mach. Learn. 65(1), 31-78 (2006)
Viinikka, J., Eggeling, R., Koivisto, M., et al.: Intersection-validation: a method for evaluating structure learning without ground truth. Proc. Mach. Learn. Res. 84, 1570-1578 (2018)
Yuan, C., Malone, B.: Learning optimal Bayesian networks: a shortest path perspective. J. Artif. Intell. Res. 48(1), 23-65 (2013)
Zitzler, E., Thiele, L.: Multiple objective evolutionary algorithms: a comparative case study and the strength Pareto approach. IEEE Trans. Evol. Comput. 3, 257-271 (1999)

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

# Affiliations 

## Marcella S. R. Martins ${ }^{1}$, Mohamed El Yafrani ${ }^{2}$ (2) $\cdot$ Myriam Delgado ${ }^{1}$, Ricardo Lüders ${ }^{1}$, Roberto Santana ${ }^{3}$, Hugo V. Siqueira ${ }^{1}$, Huseyin G. Akcay ${ }^{4}$, Belaïd Ahiod ${ }^{5}$

Mohamed El Yafrani
mey@mp.aau.dk
Myriam Delgado
myriamdelg@utfpr.edu.br
Ricardo Lüders
luders@utfpr.edu.br
Roberto Santana
roberto.santana@ehu.es
Hugo V. Siqueira
hugosiqueira@utfpr.edu.br
Huseyin G. Akcay
gokhanakcay@gmail.com

Belaïd Ahiod
ahiod@fsr.ac.ma
1 Federal University of Technology - Paraná (UTFPR), Curitiba, Brazil
2 Operations Research Group, Aalborg University (AAU), Aalborg, Denmark
3 University of the Basque Country (UPV/EHU), San Sebastián, Spain
4 Akdeniz University (AKU), Antalya, Turkey
5 Mohammed V University in Rabat, Rabat, Morocco