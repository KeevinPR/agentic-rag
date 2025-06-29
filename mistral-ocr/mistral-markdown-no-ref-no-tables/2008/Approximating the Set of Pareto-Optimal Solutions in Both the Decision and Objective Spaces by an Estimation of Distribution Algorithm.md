# Approximating the Set of Pareto-Optimal Solutions in Both the Decision and Objective Spaces by an Estimation of Distribution Algorithm 

Aimin Zhou, Qingfu Zhang, Senior Member, IEEE, and Yaochu Jin, Senior Member, IEEE


#### Abstract

Most existing multiobjective evolutionary algorithms aim at approximating the Pareto front ( PF ), which is the distribution of the Pareto-optimal solutions in the objective space. In many real-life applications, however, a good approximation to the Pareto set (PS), which is the distribution of the Paretooptimal solutions in the decision space, is also required by a decision maker. This paper considers a class of multiobjective optimization problems (MOPs), in which the dimensionalities of the PS and the PF manifolds are different so that a good approximation to the PF might not approximate the PS very well. It proposes a probabilistic model-based multiobjective evolutionary algorithm, called MMEA, for approximating the PS and the PF simultaneously for an MOP in this class. In the modeling phase of MMEA, the population is clustered into a number of subpopulations based on their distribution in the objective space, the principal component analysis technique is used to estimate the dimensionality of the PS manifold in each subpopulation, and then a probabilistic model is built for modeling the distribution of the Pareto-optimal solutions in the decision space. Such a modeling procedure could promote the population diversity in both the decision and objective spaces. MMEA is compared with three other methods, KP1, Omni-Optimizer and RM-MEDA, on a set of test instances, five of which are proposed in this paper. The experimental results clearly suggest that, overall, MMEA performs significantly better than the three compared algorithms in approximating both the PS and the PF.


Index Terms-Estimation of distribution algorithm, multiobjective optimization, Pareto optimality, principal component analysis.

## I. INTRODUCTION

THIS PAPER considers the following continuous multiobjective optimization problem (continuous MOP):

$$
\begin{array}{cc}
\operatorname{minimize} & F(x)=\left(f_{1}(x), \ldots, f_{m}(x)\right)^{T} \\
\text { subject to } & x \in \prod_{i=1}^{n}\left[a_{i}, b_{i}\right]
\end{array}
$$

where $-\infty<a_{i}<b_{i}<+\infty$ for all $i=1, \ldots, n$. $\prod_{i=1}^{n}\left[a_{i}, b_{i}\right] \subset R^{n}$ is the decision space, and $x=$

[^0]( $x_{1}, \ldots, x_{n})^{T} \in R^{n}$ is the decision variable vector. $F$ : $\prod_{i=1}^{n}\left[a_{i}, b_{i}\right] \rightarrow R^{m}$ consists of $m$ real-valued continuous objective functions $f_{i}(x), i=1, \ldots, m . R^{m}$ is the objective space.

Let $u=\left(u_{1}, \ldots, u_{m}\right)^{T}, v=\left(v_{1}, \ldots, v_{m}\right)^{T} \in R^{m}$ be two vectors; $u$ is said to dominate $v$, if $u \neq v$ and $u_{i} \leq v_{i}$ for all $i=1, \ldots, m . x^{*}$ is called (globally) Pareto-optimal if there is no other $x$ such that $F(x)$ dominates $F\left(x^{*}\right)$. The set of all the Pareto-optimal points, denoted by PS, is called the Pareto set (PS). The image of the PS on the objective space, $\mathrm{PF}=\left\{y \in R^{m} \mid y=F(x), x \in \mathrm{PS}\right\}$, is called the Pareto front (PF) [1], [2].

Most existing multiobjective evolutionary algorithms (MOEAs) aim at approximating PFs [2]-[16]. However, in some real-world applications, particularly when the preference (i.e., utility function) of a decision maker is not clearly defined, a good approximation to both the PF and the PS should be required by the decision maker for facilitating their decision making as argued in [17]-[20]. For example, if two objectives $f_{1}$ and $f_{2}$ are much more important than objective $v$ in engineering design, one often needs to first optimize $f_{1}$ and $f_{2}$ and obtain a good approximation to both the PF and the PS, then finds from the approximate PS a solution that optimizes $v$ subject to certain constraints as their final solution. In some cases, a good approximation to the PF might not approximate the PS well. Two typical classes of continuous MOPs, in which the approximation of their PSs should be carefully addressed, are as follows.

1) Class I: A finite number of different points in the PS may have the same image in the PF under the mapping $F$ from the PS to the PF, but the PS and the PF are of the same dimensionality. ZDT6 [21], Jin1 [22], and the SYM-PART instances [23] are test instances in this class. In all these instances, the PS consists of a number of disconnected continuous $(m-1)$-D manifolds.
2) Class II: The PF is an $(m-1)$-D continuous manifold and the PS is a continuous manifold of a higher dimensionality. All the inverse images of a point in the PF could constitute a nonzero-dimensional continuous manifold. Some WFG test instances [24] belong to this class. For example, in WFG6 with some parameter setting, the PF is a 1-D continuous curve in the objective space, while the PS is a 2-D rectangle. The inverse image of a point in the PF is a 1-D curve in the decision space.


[^0]:    Manescript received July 1, 2008; revised January 11, 2009 and April 6, 2009; accepted April 8, 2009. Current version published September 30, 2009.
    A. Zhou is with the Department of Computer Science and Technology, East China Normal University, Shanghai 200241, China (e-mail: amzhou@cs.ecnu.edu.cn).
    Q. Zhang is with the School of Computer Science and Electronic Engineering, University of Essex, Colchester, CO4 3SQ, U.K. (e-mail: qzhang@essex.ac.uk).
    Y. Jin is with the Honda Research Institute Europe, Offenbach 63073, Germany (e-mail: yaochu.jin@honda-ri.de).
    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

To generate a good approximation to both the PS and the PF of an MOP, an MOEA should arguably have an effective mechanism to encourage and maintain the population diversity, not only in the objective space as most MOEAs do, but also in the decision space. For this reason, Deb and Tiwari [25] introduced the crowding distance in the decision space into the nondominated sorting scheme in Omni-Optimizer, which is a generalization of NSGA-II [26], for promoting the population diversity in the decision space. Chan and Ray [27] suggested using two selection operators in MOEAs; one encourages the diversity in the objective space and the other does so in the decision space. They implemented KP1 and KP2, two algorithms using these two selection operators. It should be pointed out that the MOPs that KP1, KP2, and OmniOptimizer attempt to deal with are of Class I. Preuss et al. [28] and Rudolph et al. [23] also proposed to use a restart strategy for finding a good approximation to the PS of an MOP of Class I. To the best of our knowledge, no effort has been made for dealing with problems of Class II. The major purpose of this paper is to study how to approximate both the PS and the PF of an MOP of Class II.
In [14], we studied a "regular" continuous MOP in which both the PF and the FS are piecewise ( $m-1$ )-D continuous manifolds, and proposed RM-MEDA, which is an estimation of distribution algorithm (EDA) for approximating its PF. In this paper, we generalize the idea of RM-MEDA and propose a probabilistic model-based multiobjective evolutionary algorithm, called MMEA, for approximating the PS and the PF of an MOP of Class II simultaneously. MMEA has the following features.

1) The population diversity in the decision space is promoted in its reproduction generator, instead of in the selection operators as in Omni-Optimizer, KP1, and KP2. The non-dominated sorting (NDS) selection, which is used in RM-MEDA, is employed in MMEA.
2) To build a probabilistic model of promising solutions, the population is divided, based on their distribution in the objective space, into a number of subpopulations. Therefore, the population diversity in the objective space can be promoted. To ease the burden of tuning the number of subpopulations, a random strategy is used for setting it.
3) The principal component analysis (PCA) technique is used to estimate the dimensionality of the PS manifold in each subpopulation, and then a probabilistic model can be built for modeling the distribution of promising solutions in the decision space. In such a way, the population diversity in the decision space can be encouraged.
The rest of the paper is organized as follows: Section II gives the details of the algorithm. Section III presents the performance metrics and the test instances, some of which are proposed in this paper for the first time. Section IV compares MMEA with KP1, Omni-Optimizer, and RM-MEDA on these test instances. More discussions on the ability of MMEA are provided in Section V. Section VI concludes this paper and suggests some future research topics.

## II. Algorithm

## A. Framework

At each generation, the proposed algorithm, MMEA, maintains:

1) a population of $N$ solutions (i.e., points in $\prod_{i=1}^{n}\left[a_{i}, b_{i}\right]$ )

$$
x^{1}, \ldots, x^{N}
$$

2) their function values: $F\left(x^{1}\right), \ldots, F\left(x^{N}\right)$.

MMEA adopts the following widely used EDA framework.
Phase 1 Initialization: Generate an initial population $P$ and compute the $F$-values of these solutions in $P$.
Phase 2 Modeling: Build a model for modeling the distribution of the individuals in $P$.
Phase 3 Reproduction: Generate a set of new solutions $Q$ by sampling from the model built in Phase 2 and compute the function values of these solutions in $Q$.
Phase 4 Selection: Select $N$ solutions from $P \cup Q$ and replace all the solutions in $P$ by them.
Phase 5 Stopping Condition: If a stopping condition is met, stop and return all the solutions in $P$ and their corresponding $F$-values. Otherwise, go to Phase 2.
In the following, we give and discuss the details of modeling, reproduction, and selection.

## B. Modeling

In a successful algorithm for approximating both the PS and the PF of (1), the individuals in its population should approximate the PS in the decision space and their images should converge to the PF in the objective space as the search goes on. Therefore, one could model the PS and the PF based on information extracted from the population. Such models can be further used for sampling new good solutions. This idea has been used to some extent in RM-MEDA. The problem that RM-MEDA was designed for is a "regular" continuous MOP, in which both the PS and the PF are of the same dimensionality. In this paper, the same idea is used in the modeling phase of MMEA for dealing with an MOP of Class II.

The modeling phase in MMEA works as follows.
Step 1 Building a Utopian PF: Based on information from the current population $P$, build an $(m-1)-\mathrm{D}$ simplex in the objective space as a Utopian PF.
Step 2 Determining the Number of Subpopulations: Determine $K$, the number of subpopulations used in modeling the PS.
Step 3 Selecting Reference Points: Set $Y^{1}, \ldots, Y^{K}, K$ points which are uniformly spread on the Utopian PF in the objective space, to be $K$ reference points.
Step 4 Clustering: Cluster the population $P$ into $K$ subpopulations $P^{1}, \ldots, P^{K}$.
Step 5 Principal Component Analysis and Modeling: Perform PCA on each subpopulation $P^{k}, k=$ $1, \ldots, K$ and build a model for it.
In the following, we give the details of the major steps in the above modeling phase.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of building a Utopian PF in the case of two objectives. (a) Find the extreme points and initialize simplex $S$, (b) Move $S$ along its normal direction, and (c) Enlarge $S$.

1) Building a Utopian PF: We assume that the PF of the MOP in question is of $(m-1)$-D. Therefore, it is reasonable to use an $(m-1)$-D simplex as a Utopian PF. The following procedure is used to construct such a simplex $S$.

Step 1.1 For $i=1, \ldots, m$, find the individual solution $z^{i}$ in $P$ such that $z^{i}$ is a nondominated solution in $P$ and it has the largest $f_{i}$ function value among all the nondominated solutions in $P$.
Step 1.2 Initialize $S$ as the $(m-1)$-D simplex with vertexes $F\left(z^{1}\right), \ldots, F\left(z^{m}\right)$ in the objective space. Move $S$ along its normal direction to a position such that (a) no point in $S$ can be dominated by any solutions in $P$, and (b) the moved distance should be as short as possible.
Step 1.3 Let $A_{1}, \ldots, A_{m}$ be the vertexes of the moved simplex $S$. Compute the center of $S$

$$
O=\frac{1}{m} \sum_{i=1}^{m} A_{i}
$$

Then enlarge $S$ by moving its vertexes

$$
A_{i}:=A_{i}+\left[(1+\alpha)^{\frac{1}{\alpha-1}}-1\right]\left(A_{i}-O\right)
$$

for $i=1, \ldots, m$.
$\alpha>0$ is a control parameter. It is easy to work out that the volume of the simplex $S$ is increased by $100 \alpha \%$ in Step 1.3. The major reason why we enlarge $S$ is to guide the algorithm to extend its search in the objective space. When $m$, the number of the objectives, is $2, S$ is a 1-D line segment in the objective space. Fig. 1 illustrates how $S$ is generated in this case.
2) Determining the Number of Subpopulations: To reduce the problem-dependence of $K$, the value of $K$ is uniformly randomly chosen from the set $\left\{1,2, \ldots, K_{\max }\right\} . K_{\max }$ is a control parameter.
3) Selecting Reference Points: It is desirable that reference points uniformly spread on the Utopian PF. Note that the Utopian PF is a simplex; in our implementation, we use the simplex point picking method [29] for selecting reference points.
4) Clustering: For each reference point $Y^{k}$ obtained in Step 3, we select a number of points from $P$ closer to it for forming $P^{k}$ as follows.

Step 4.1 Compute, in the objective space, the Euclidian distances between $Y^{k}$ to all the individual solutions in $P$.
Step 4.2 Select the $\min \{N,[2 N / K]\}$ closest solutions to $Y^{k}$ and let them constitute subpopulation $P^{k}$.
In clustering, different subpopulations may overlap, which could improve the search performance in between different reference points.
5) PCA and Modeling: The individual solutions in subpopulation $P^{k}, k=1, \ldots, K$ should, hopefully, scatter around the PS in the decision space as the search goes on. For simplicity, we can model the subpopulation $P^{k}$ as a hyper-cuboid $\Phi^{k}$ in the decision space and regard each individual in $P^{k}$ as an observation of the following random vector

$$
\bar{\zeta}=\zeta+\varepsilon
$$

where $\zeta$ is uniformly randomly distributed on $\Phi^{k}, \varepsilon \sim$ $N\left(0, \sigma^{k} I\right)$ is an $n$-dimensional zero-mean Gaussian vector, $I$ is the $n \times n$ identity matrix, and $\sigma^{k}>0$.

Now the task is to estimate $\Phi^{k}$ and $\sigma^{k}$. We do it as follows.
Step 5.1 Compute the sample mean and the sample covariance matrix of the individual solutions in $P^{k}$

$$
\bar{x}^{k}=\frac{1}{\left|P^{k}\right|} \sum_{x \in P^{k}} x
$$

and

$$
\operatorname{Cov}^{k}=\frac{1}{\left|P^{k}\right|-1} \sum_{x \in P^{k}}\left(x-\bar{x}^{k}\right)\left(x-\bar{x}^{k}\right)^{T}
$$

where $\left|P^{k}\right|$ is the cardinality of $P^{k}$.
Step 5.2 Compute the eigenvalues of $\operatorname{Cov}^{k}$

$$
\lambda_{1}^{k} \geq \lambda_{2}^{k} \geq \cdots \geq \lambda_{n}^{k}
$$

and their corresponding unity eigenvectors

$$
V_{1}^{k}, V_{2}^{k}, \ldots, V_{n}^{k}
$$

Step 5.3 Set $n^{k}$, the dimensionality of the hyper-cuboid $\Phi^{k}$ to be the smallest integer such that

$$
\sum_{j=1}^{n^{k}} \lambda_{j}^{k} \geq \theta \sum_{j=1}^{n} \lambda_{j}^{k}
$$

where the threshold $0 \leq \theta \leq 1$ is an algorithm parameter.
Step 5.4 Compute the range of the projections of the points in $P^{k}$ onto the first $n^{k}$ principal component directions

$$
l_{j}^{k}=\min _{x \in P^{k}}\left\{\left(x-\bar{x}^{k}\right)^{T} V_{j}^{k}\right\}
$$

and

$$
u_{j}^{k}=\max _{x \in P^{k}}\left\{\left(x-\bar{x}^{k}\right)^{T} V_{j}^{k}\right\}
$$

for $j=1, \ldots, n^{k}$.
Step 5.5 Set

$$
\begin{gathered}
\Phi^{k}=\left\{x \in R^{n} \mid x=\bar{x}^{k}+\sum_{j=1}^{n^{k}} c_{j} V_{j}^{k}\right. \\
l_{j}^{k}-\frac{(1+\beta) \frac{1}{n^{k}}-1}{2}\left(u_{j}^{k}-l_{j}^{k}\right) \leq c_{j} \\
\leq u_{j}^{k}+\frac{(1+\beta) \frac{1}{n^{k}}-1}{2}\left(u_{j}^{k}-l_{j}^{k}\right) \\
\left.j=1, \ldots, n^{k}\right\}
\end{gathered}
$$

where $\beta$ is a control parameter.
Step 5.6 Set

$$
\sigma^{k}=\frac{1}{n-n^{k}} \sum_{j=n^{k}+1}^{n} \lambda_{j}^{k}
$$

The dimensionality of the PS is unknown, neither is that of $\Phi^{k}$. In Step 5.3, the dimensionality of $\Phi^{k}$ is set such that $\Phi^{k}$ holds at least $1000 \%$ of the variation in the solutions in $P^{k}$. In Step 5.5, $\Phi^{k}$ is enlarged along each of the first $n^{k}$ principal component directions such that its volume is $100 \beta \%$ larger than that the smallest $n^{k}$-D hyper-cuboid containing the projections of all the solutions of $P^{k}$ on the space spanned by $V_{1}^{k}, \ldots, V_{n^{k}}^{k}$ from $\bar{x}^{k}$. The motivation behind this extension is to extrapolate the points in $P^{k}$ for searching unexplored promising areas in the decision space. $\varepsilon$ is modeled as a Gaussian noise vector and all its components are i.i.d., which facilitates the sampling procedure.

The reference points in the objective space used in clustering are hopefully uniformly distributed along the PF, therefore they could guide the search to generate a good approximation to the PF in the objective space. The modeling in the decision space attempts to model the PS, which enables the algorithm to generate a set of points for approximating the PS in the decision space.

The three major differences in the modeling phase between RM-MEDA and MMEA are.

1) RM-MEDA uses the local PCA [30] technique to partition the population into several clusters. In contrast, MMEA in this paper selects the subpopulation centers from the Utopian PF and performs clustering based on the distances in the objective space, which is computationally cheaper. Moreover, the local PCA could not be applied in MMEA since the dimensionality of the PS manifold must be predetermined in the local PCA and it is unknown in the problems MMEA aims to solve.
2) The number of clusters is preset in RM-MEDA, while MMEA in this paper chooses the number of subpopulations randomly, which lightens the burden of tuning this control parameter.
3) In modeling each subpopulation, RM-MEDA sets the dimensionality of the PS manifold to be $(m-1)$, while MMEA needs to estimate it. This difference is due to the fact that these two algorithms are for different MOPs.

## C. Sampling

A new solution $x$ is generated in Phase 4 of MMEA as follows.

Step 1 Uniformly randomly generate an integer $k$ from $\{1,2, \ldots, K\}$.
Step 2 Uniformly randomly generate a point $x^{\prime}$ from $\Phi^{k}$. Generate a noise vector $\varepsilon^{\prime}$ from $N\left(0, \sigma^{k} I\right)$.
Step 3 Set $y=x^{\prime}+\varepsilon^{\prime}$, and let the new solution $x$ as

$$
x_{j}= \begin{cases}y_{j}, & \text { if } a_{j} \leq y_{j} \leq b_{j} \\ \frac{1}{2}\left(z_{j}+a_{j}\right), & \text { if } y_{j}<a_{j} \\ \frac{1}{2}\left(z_{j}+b_{j}\right), & \text { if } y_{j}>b_{j}\end{cases}
$$

where $j=1, \ldots, n$, and $z$ is a randomly selected solution from the subpopulation $P^{k}$.
In our implementation, the above procedure is repeated $N$ times for generating $N$ solutions in Phase 4.

## D. Selection

The selection operator used in the experimental studies is the NDS selection, which is a variant of non-dominated sorting scheme [26] proposed in [14]. It works as follows.

Step 1 Set $Q=P \cup Q$ and $P=\emptyset$.
Step 2 Partition $Q$ into different fronts $F_{1}, \ldots, F_{l}$ by using the fast non-dominated sorting approach [26]. Set $k=0$.

Do

$$
\begin{gathered}
k=k+1 \\
P=P \cup F_{k}
\end{gathered}
$$

Until $|P| \geq N$.
Step 3 While $|P|>N$, Do
For all the individual members in $F_{k} \cap P$, compute their crowding distances in $F_{k} \cap P$. Remove the element in $F_{k} \cap P$ with the smallest crowding distance from $P$. In the case when there is more than one member with the smallest crowding distance, randomly choose one and remove it.

In Step 2, the NDS selection partitions $Q$ into different fronts $F_{1}, \ldots, F_{l}$ such that the $j$ th front $F_{j}$ contains all the non-dominated solutions in $\{P \cup Q\} \backslash\left(\cup_{i=1}^{j-1} F_{i}\right)$. Therefore, there is no solution in $\{P \cup Q\} \backslash\left(\cup_{i=1}^{j-1} F_{i}\right)$ that could dominate a solution in $F_{j}$.
The crowding distance, used in Step 3, of point $x$ is defined as the average side length of the largest $m$-D rectangle in the objective space subject to two constraints: (a) each of its sides is parallel to a coordinate axis and (b) $F(x)$ is the only interior point of the rectangle among all the points in $\{F(y) \mid y \in F_{k} \cap$ $P\}$. A solution with a larger crowding distance is given priority to be selected since it could increase the population diversity in the objective space.

## III. Test Instances and Performance Metrics

## A. Test Instances

MMEA is for approximating both the PS and the PF of an MOP of Class II. WFG instances are the only Class II instances that we have found in the literature. Two WFG instances: WFG6 and WFG7, have been used in our experiments. Based on the experiments in [24], the PFs of WFG7 could be "easily" and "quickly" found by NSGA-II, while WFG6 is "hard" for NSGA-II. It can be because the objectives in WFG7 are separable while it is not the case in WFG6. The PSs of these two test instances are a 2-D rectangle in the decision space when their control parameters are set as in Table I. To study the behaviors of MOEAs on nonlinear PSs, we have designed several new MOP test instances of Class II with nonlinear PSs. All these test instances are listed in Table I. Figs. 2 and 3 plot their PFs and the projections of their PSs onto lower dimensional spaces.

## B. Performance Metrics

The inverted generational distance (IGD) metric [14], [31] and hypervolume difference ( $I_{H}^{-}$) metric [32] are used to assess the algorithm performances in our experimental studies.
Let $P^{*}$ be a set of uniformly distributed Pareto-optimal points in the PF (or PS). Let $P$ be an approximation to the PF (or the PS). The $I G D$ metric is defined as follows:

$$
I G D\left(P^{*}, P\right)=\frac{\sum_{v \in P^{*}} d(v, P)}{\left|P^{*}\right|}
$$

where $d(v, P)$ is a distance between $v$ and $P$ and $\left|P^{*}\right|$ is the cardinality of $P^{*}$.
We denote $I G D$ metric as $I G D F$ when $P^{*}$ is a set of points in the PF and $d(v, P)$ is the Euclidian distance in the objective space, and as IGDX when $P^{*}$ is a set of points in the PS and $d(v, P)$ is the Euclidian distance in the decision space.
The $I_{H}^{-}$metric is defined as

$$
I_{H}^{-}\left(P^{*}, P\right)=I_{H}\left(P^{*}\right)-I_{H}(P)
$$

where $I_{H}(P)$ is the hypervolume between the set $P$ and a bounded reference point [33].
Both the $I G D$ metric and the $I_{H}^{-}$metric measure convergence and diversity. To have low $I G D$ and $I_{H}^{-}$values, $P$ must be close to the PF (or PS) and cannot miss any part of the whole PF (or PS).

In our experiments, 1000 points, in which $f_{1}$ or $t$ taking 1000 equidistant values from their lower bounds to their upper bounds, are selected from the respective PFs of $F 1-F 6$ to be $P^{*}$ for computing the $I G D F$ metrics. $50 \times 50=2500$ points in the PF of $F 7$ with $s, t=0 / 49 \times \pi / 2,1 / 49 \times$ $\pi / 2, \ldots, 49 / 49 \times \pi / 2$, are taken to form $P^{*}$ for computing the $I G D F$ metric for experiments on $F 7.50 \times 50=2500$ points in the respective PSs of $F 1-F 5$, in which $x_{1}$ and $x_{2}$ take 50 equidistant values from their lower bounds to their upper bounds respectively, are taken to form $P^{*}$ for computing the IGDX metrics. $25 \times 25 \times 25=15625$ points in the respective PSs of $F 6$ and $F 7$, in which $x_{1}, x_{2}$, and $x_{3}$ take 25 equidistant values from their lower bounds to their upper bounds, respectively, are taken to be $P^{*}$ for computing the IGDX metrics. In calculating the $I_{H}^{-}$values, the bounded reference point is chosen to be $(2.4,4.5)^{T}$ for $F 1$ and $F 2$, $(1.2,1.2)^{T}$ for $F 3-F 6$ and $(1.2,1.2,1.2)^{T}$ for $F 7$.

## IV. EXPERIMENTAL RESULTS

## A. Experimental Settings and Algorithms in Comparison

The studies in [23], [27], [28] have shown that popular MOEAs, such as PAES [34], NSGA-II [26], and SPEA2 [35], cannot approximate both the PF and the PS simultaneously since these methods cannot maintain the population diversity in the decision space. MOEA/D, which is a recent MOEA based on aggregation proposed in [14], [36], cannot do so either for the same reason. In our experiments, we compare MMEA with KP1 [27] ${ }^{1}$ and Omni-Optimizer [25]. ${ }^{2}$ As mentioned in Introduction, both KP1 and Omni-Optimizer try to approximate both the PF and the PS of an MOP by promoting the population diversity in the decision space in their selection operators. The simulated binary crossover (SBX) [37] and the polynomial mutation [38] are used in these two methods for generating offspring. Since MMEA is based on RMMEDA [14], we also compare MMEA with RM-MEDA on these problems.

Table II lists all the parameter settings in our experiments. The population in each algorithm is initialized uniformly and randomly in the decision space. All the following results are based on 20 independent runs of each algorithm on each test instance.

## B. F1-F2

$F 1$ and $F 2$ have the same PS, which is a 2-D rectangle parallel to the $x_{1}-x_{2}$ space. The objectives are nonseparable in $F 1$ but separable in $F 2$ [24]. The means and standard deviations can be found in Table III of the $I_{H}^{-}, I G D F$, and IGDX values of the 20 final populations obtained by each algorithm for $F 1$ and $F 2$. Figs. 4 and 5 show, in the objective and decision spaces, the distribution of the final solutions obtained in the runs with the lowest $I G D F$ and $I G D X$ values of each algorithm for these two test instances, respectively.

[^0]
[^0]:    ${ }^{1}$ We use KP1 in this paper because the experimental results in [27] have shown that KP1 is slightly better than KP2.
    ${ }^{2}$ The $\mathrm{C}++$ source codes of KP1 was obtained from its authors and OmniOptimizer was implemented by ourselves.

TABLE I
Test Instances Used in Our Experiments: F1, F2 Are WFG Instances, F3-F7 Are New Designed Test Instances. $x=\left(x_{1}, \ldots, x_{n}\right)$. All These Instances Belong to Class II

![img-1.jpeg](img-1.jpeg)

Fig. 2. PFs and the PSs for $F 1-F 4$. (a) $F 1$, (b) $F 2$, (c) $F 3$, and (d) $F 4$. Left: the PFs in the objective space. Middle: the projections of the PSs onto the $x_{1}-x_{2}$ space. Right: the projections of the PSs onto the $x_{1}-x_{3}$ space for $F 1$ and $F 2$, and onto the $\left[\left(x_{1}+x_{2}\right) / 2\right]-x_{3}$ space for $F 3$ and $F 4$.

It is clear from Table III that in terms of the $I G D F$ metric, MMEA is significantly better than the three other algorithms on these two test instances, and in terms of $I_{H}^{-}$metric MMEA performs better than the three other competitors on $F 1$ but slightly worse than KP1 on $F 2$. The plots in Figs. 4 and 5
show that all the four algorithms can approximate the PF very well and the final populations with the lowest IGDF values, obtained by MMEA approximate the PFs slightly better than those obtained Omni-Optimizer and KP1. It should be pointed out that Figs. 4 and 5 do not contradict with Table III. Figs. 4

![img-2.jpeg](img-2.jpeg)

Fig. 3. PFs and the PSs for $F 5-F 7$. (a) $F 5$, (b) $F 6$, and (c) $F 7$. Left: PFs in the objective space. Middle: the projections of the PSs onto the $x_{1}-x_{2}$ space for F5, and onto the $x_{1}-x_{2}-x_{3}$ space for F6 and F7. Right: the projections of the PSs onto the $\left[\left(x_{1}+x_{2}\right) / 2\right]-x_{3}$ space for $F 5$, and onto the $\left[\left(x_{1}+x_{2}+x_{3}\right) / 3\right]-x_{4}$ space for F6 and F7.
and 5 give the distributions of the final populations with the lowest $I G D$ values while, Table III shows the mean/std of the $I G D$ and $I_{H}^{-}$values.

In terms of the $I G D X$ metric, Table III shows that MMEA significantly outperforms the three other algorithms. Actually, one could visually distinguish from Fig. 4 the differences in approximation quality in the $x_{1}-x_{2}$ and $x_{1}-x_{3}$ spaces between MMEA and the three other methods on $F 1$ and $F 2$ : the distributions of the final population found by MMEA are more diverse and uniform that those obtained by the three others. These results indicate that MMEA could tackle MOPs with linear PSs like $F 1$ and $F 2$.

## C. F3-F7

All these test instances have nonlinear PSs in the decision space. The dimensionality of the PSs of $F 3-F 5$ is 2 while that of $F 6$ and $F 7$ is 3 .

IGDF and $I H^{-}$are for measuring the approximation quality in the decision space. The t-test results in Table III suggest that on $F 3-F 7$, in terms of these two metrics, MMEA performs significantly better than KP1 and Omni-Optimizer, but does not always outperform RM-MEDA. It is confirmed to a certain extent by plots in Figs. 6-10: on F3-F6, that the final solutions with the lowest IGDF values obtained by MMEA and RM-MEDA approximate the PFs very well while Omni-Optimizer and KP1 always miss part of the PFs; on $F 7$, it is clear that MMEA and RM-MEDA provide better approximations than Omni-Optimizer and KP1, although none could approximate the PF very well. In terms of the IGDX metric, it is evident from Table III that MMEA outperforms the three other algorithms on $F 3-F 7$, except RM-MEDA on F7. Figs. 6-9 also reveal that the solutions generated by MMEA, are distributed more uniformly in the decision space than those obtained by the three other ones. Table III shows

TABLE II
EXPERIMENTAL SETTINGS FOR $F 1-F 7$

TABLE III
Statistical Results on F1-F7 (mean $\pm$ std.) " + " in Parenthesis: The One-Side t-Test Indicates That the Metric Value Is Larger Than That Obtained by MMEA at the 95\% Significance Level. "-" in Parenthesis Means a Failure in the t-Test to Reject the Null Hypothesis. In the One-side t-Test, the Null Hypothesis Is That Both Metrics Values in Test Are From the Same Normal Distribution, and the Alternative Hypothesis Is That the Metric Value in MMEA Is Smaller Than That Obtained by Another Algorithm

that RM-MEDA slightly outperforms MMEA in terms of all the performance metrics on $F 7$. One cannot tell, however, any big difference in approximation quality between RM-MEDA and MMEA from Fig. 10. The reason why MMEA could not outperform RM-MEDA on $F 7$ might be that neither of these two algorithms converges and has not yet started refining their solutions within the given number of function evaluations.

KP1 and Omni-Optimizer promote the population diversity in their selection operators and mainly use the SBX, which was originally proposed for single objective optimization,
to generate new solutions. RM-MEDA assumes that the PS dimensionality is $m-1$. MMEA estimates the dimensionality and the shape of the PS and attempts to make the new solutions uniformly distribute around the estimated PS. Our experiments have suggested that reproduction operators are of crucial importance in MOEAs for approximating both the PS and the PF and one should use their problem-specific knowledge in designing reproduction operators in MOEAs. The major reason that KP1 and Omni-Optimizer fail in F3-F7 might be that the SBX is not suitable for an MOP with

![img-3.jpeg](img-3.jpeg)

Fig. 4. Best approximations obtained by four algorithms for $F 1$ : (a) Omni-Optimizer, (b) KP1, (c) RM-MEDA, and (d) MMEA. Left: the distributions of the final solutions in the objective space obtained in the runs with the lowest IGDF values by four respective algorithms. Middle: the distributions of the final solutions in the $x_{1}-x_{2}$ space obtained in the runs with the lowest IGDX values. Right: the distributions of the final solutions in the $x_{1}-x_{3}$ space obtained in the runs with the lowest IGDX values.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Best approximations obtained by four algorithms for F2: (a) Omni-Optimizer, (b) KP1, (c) RM-MEDA, and (d) MMEA. Left: the distributions of the final solutions in the objective space obtained in the runs with the lowest $I G D F$ values by four respective algorithms. Middle: the distributions of the final solutions in the $x_{1}-x_{2}$ space obtained in the runs with the lowest IGDX values. Right: the distributions of the final solutions in the $x_{1}-x_{3}$ space obtained in the runs with the lowest IGDX values.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Best approximations obtained by four algorithms for F3: (a) Omni-Optimizer, (b) KP1, (c) RM-MEDA, and (d) MMEA. Left: the distributions of the final solutions in the objective space obtained in the runs with the lowest IGDF values by three respective algorithms. Middle: the distributions of the final solutions in the $x_{1}-x_{2}$ space obtained in the runs with the lowest IGDX values. Right: the distributions of the final solutions in the $\left[\left(x_{1}+x_{2}\right) / 2\right]-x_{3}$ space obtained in the runs with the lowest IGDX values.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Best approximations obtained by four algorithms for $F 4$ : (a) Omni-Optimizer, (b) KP1, (c) RM-MEDA, and (d) MMEA. Left: the distributions of the final solutions in the objective space obtained in the runs with the lowest IGDF values by three respective algorithms. Middle: the distributions of the final solutions in the $x_{1}-x_{2}$ space obtained in the runs with the lowest IGDX values. Right: the distributions of the final solutions in the $\left[\left(x_{1}+x_{2}\right) / 2\right]-x_{3}$ space obtained in the runs with the lowest IGDX values.

![img-7.jpeg](img-7.jpeg)

Fig. 8. Best approximations obtained by four algorithms for F5: (a) Omni-Optimizer, (b) KP1, (c) RM-MEDA, and (d) MMEA. Left: the distributions of the final solutions in the objective space obtained in the runs with the lowest IGDF values by three respective algorithms. Middle: the distributions of the final solutions in the $x_{1}-x_{2}$ space obtained in the runs with the lowest IGDX values. Right: the distributions of the final solutions in the $\left[\left(x_{1}+x_{2}\right) / 2\right]-x_{3}$ space obtained in the runs with the lowest IGDX values.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Best approximations obtained by four algorithms for F6: (a) Omni-Optimizer, (b) KP1, (c) RM-MEDA, and (d) MMEA. Left: the distributions of the final solutions in the objective space obtained in the runs with the lowest IGDF values by three respective algorithms. Middle: the distributions of the final solutions in the $x_{1}-x_{2}-x_{3}$ space obtained in the runs with the lowest IGDX values. Right: the distributions of the final solutions in the $\left[\left(x_{1}+x_{2}+x_{3}\right) / 3\right]-x_{4}$ space obtained in the runs with the lowest IGDX values.

![img-9.jpeg](img-9.jpeg)

Fig. 10. Best approximations obtained by four algorithms for $F 7$ : (a) Omni-Optimizer, (b) KP1, (c) RM-MEDA, and (d) MMEA. Left: the distributions of the final solutions in the objective space obtained in the runs with the lowest IGDF values by three respective algorithms. Middle: the distributions of the final solutions in the $x_{1}-x_{2}-x_{3}$ space obtained in the runs with the lowest IGDX values. Right: the distributions of the final solutions in the $\left[\left(x_{1}+x_{2}+x_{3}\right) / 3\right]-x_{4}$ space obtained in the runs with the lowest IGDX values.

TABLE IV
Regular Test Instances. Their PSs and PFs Are With the Same Dimensionality


nonlinear PSs. Actually, if two parent solutions are Paretooptimal (i.e., in the PS), it is very likely that their offspring under the SBX are far away from the PS. Since RM-MEDA tries to use an $(m-1)$-D manifold to approximate the PS, the final solutions obtained by it for biobjective test instances, as shown in Figs. 6-9, are distributed along 1-D manifolds in the decision space.

## V. More Discussions

## A. Can MMEA Solve Regular MOPs?

MMEA was designed for solving an MOP of Class II, in which the dimensionality of its PS is not lower than the number of the objectives and unknown. In fact, MMEA uses the PCA technique to estimate the PS dimensionality before modeling the PS. Now a question arises whether MMEA can effectively solve a regular MOP in which the PS is an $(m-1)$-D continuous manifold in the decision space. To address this issue, we have compared MMEA with RMMEDA on a set of regular MOP test instances with linear
and nonlinear variable linkages introduced in [14], which are given in Table IV.
The experimental setting are the same as in [14]:

1) the number of variables $n=30$;
2) the population size for each algorithm $N=100$ for two objective instances, and 200 for three objective instances;
3) the number of generations is 100 for ZZJ08-F1, ZZJ08$F 2, \mathrm{ZZJ} 08-F 5$, and ZZJ08-F6; 1000 for ZZJ08-F3 and ZZJ08-F7; and 200 for ZZJ08-F4 and ZZJ08-F8;
4) the number of clusters in RM-MEDA $K=5$;
5) $\alpha, \beta, \theta$ and $K_{\max }$ in MMEA are the same as in Table II.

All the following results are based on 20 independent runs of each algorithm on each test instance. In our experiments, 1000 points, in which $x_{1}$ taking 1000 equidistant values from their lower bounds to their upper bounds, are selected from the respective PFs of ZZJ08-F1 - ZZJ08-F3 and ZZJ08-F5 - ZZJ08-F7 to form $P^{*}$. $50 \times 50=2500$ points in the PF of ZZJ08-F4 and ZZJ08-F8 with $x_{1}, x_{2}=$

TABLE V
Statistical Results on Regular MOPs (mean $\pm$ std.)." + " in Parenthesis: The One-Side t-Test Indicates That the Metric Value in RM-MEDA Is Larger Than That Obtained by MMEA at the 95\% Significance Level. "-" in Parenthesis Means a Failure in the t-Test to Reject the Null Hypothesis

$0 / 49,1 / 49, S, \ldots, 49 / 49$, are taken to form $P^{*}$ for experiments on ZZJ08-F4 and ZZJ08-F8. The bounded reference point is chosen to be $(1.5,1.5)^{T}$ for $F 1-F 3$ and $F 5-F 7$, and $(1.5,1.5,1.5)^{T}$ for $F 4$ and $F 8$ in calculating $I_{H}^{-}$values.

Table V gives the means and standard deviations of the $I_{H}^{-}$ and $I G D F$ values of the 20 final populations obtained by RMMEDA and MMEA for all the eight test instances. Figs. 11 and 12 show, in the objective space, the distribution of the final solutions obtained in the runs with the lowest IGDF values of the two algorithms for these test instances, respectively.

It is clear from Table V that MMEA is significantly better than RM-MEDA on all the instances in terms of the $I_{H}^{-}$ metric, and MMEA significantly outperforms or is not worse than RM-MEDA in terms of IGDF metric on these eight instances. The difference between the best approximations of RM-MEDA and those of MMEA in Figs. 11 and 12 can hardly be visually distinguished. These results imply that although MMEA is designed for Class II problems, its performance is not worse than RM-MEDA on regular MOPs.

## B. Can MMEA Deal With an MOP of Class I?

An MOP of Class II has a continuous PS of dimensionality larger than $m-1$, while the PS of an MOP of Class I consists of a number of disconnected continuous manifolds. To investigate the ability of MMEA to tackle MOPs in Class I, we have tested MMEA on DT05-F4.4 [25], in which the two objectives to be minimized are as follows:

$$
\begin{aligned}
& f_{1}(x)=\sum_{i=1}^{n} \sin \left(\pi x_{i}\right) \\
& f_{2}(x)=\sum_{i=1}^{n} \cos \left(\pi x_{i}\right)
\end{aligned}
$$

and the search space is $[0,6]^{n}$. The PF of DT05-F4.4 is

$$
f_{2}=-\sqrt{25-f_{1}^{2}}, \quad f_{1} \in[-5,0]
$$

and its PS consists of $3^{n}$ disconnected parts, each of which is a line segment.

In our experiment on DT05-F4.4, $n$, the number of decision variables, is set to be 5 , and $N$, the population size is 1000 as in [25]. All the other parameter settings are the same as in Section IV. Fig. 13 presents the final population obtained in the run with the lowest IGDF value among 20 independent runs. Clearly, MMEA has not produced a satisfactory approximation to the PS. This could be attributed to the fact that population clustering in MMEA is based on the distance in the objective space, which prevents it from distinguishing the different parts of the DT05-F4.4 PS in the decision space and thus cannot find a good approximation to its PS.

## C. Sensitivity of Control Parameters

In the following, taking $F 3$ as an example, we investigate the sensitivity of the four control parameters in MMEA.

1) The Effect of $\alpha$ : We have tried different values of $\alpha$ : $0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8$, and 2.0 for MMEA on $F 3$. The settings of the other control parameters are the same as in Section IV. Fig. 14 shows the average IGDF and IGDX metrics versus the different values of $\alpha$, respectively. It is clear that MMEA works very well when $0.4 \leq \alpha \leq 2.0$. It also indicates that MMEA performs poorly if $\alpha$ is too small. This could be due to the fact that a small value of $\alpha$ might reduce the exploration ability of MMEA.
2) The Effect of $\beta$ : We have tried different values of $\beta$ : $0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8$, and 2.0 for MMEA on $F 3$. The settings of the other control parameters are the same as in Section IV. Fig. 15 shows the average IGDF and IGDX metrics v.s. the different values of $\beta$, respectively. Clearly, IGDX value is more sensitive to $\beta$ than IGDF. This is not a surprise since $\beta$ is mainly for extending the search in the decision space. It is also evident that MMEA works well in terms of both IGDX and IGDF metrics if $0.8 \leq \beta \leq 2$.
3) The Effect of $\theta$ : We have tried different values of $\theta$ : $0.5,0.6,0.7,0.75,0.8,0.85,0.9,0.95$, and 1.0 on $F 3$. The settings of the other parameters are the same as in Section IV.

![img-10.jpeg](img-10.jpeg)

Fig. 11. Approximations with the lowest $I G D F$ values obtained by RM-MEDA on regular MOPs.
![img-11.jpeg](img-11.jpeg)

Fig. 12. Approximations with the lowest $I G D F$ values obtained by MMEA on regular MOPs.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Best approximation obtained in the 20 runs with the lowest $I G D F$ value by MMEA for DT05-F4.4. Left: the distribution of the final solutions in the objective space. Middle: the distribution of the final solutions in the $x_{1}-x_{2}$ space. Right: the distribution of the final solutions in the $x_{3}-x_{4}$ space.

Fig. 16 shows the average $I G D F$ and $I G D X$ metrics versus the different values of $\theta$, respectively. It is clear from this figure that MMEA can approximate the PF of $F 3$ if $0.5 \leq \theta \leq 0.95$ and it can approximate the PS of $F 3$ if $0.75 \leq \theta \leq 0.95$.

When $\theta=1.0$, the performance of MMEA becomes very poor. The reason might be that in such a case, MMEA implicitly assumes that the dimensionality of the PS is $n$ and set $\sigma^{4}$ to be zero in Step 5.6 in PCA and Modeling;

![img-13.jpeg](img-13.jpeg)

Fig. 14. Average IGD metrics of the 20 final approximations versus $a$ in MMEA on $F 3$.
![img-14.jpeg](img-14.jpeg)

Fig. 15. Average IGD metrics of the 20 final approximations versus $\beta$ in MMEA on $F 3$.
![img-15.jpeg](img-15.jpeg)

Fig. 16. Average IGD metrics of the 20 final approximations versus $\theta$ in MMEA on $F 3$.
as a result, the search ability of MMEA has been reduced significantly.
4) The Effect of $K_{\max }$ : In our experiment, we have tried the different values of $K_{\max }: 10,15,20,25,30,35,40$, 45 , and 50. It is evident from Fig. 17 that MMEA could approximate the PF of $F 3$ very well when $K_{\max } \geq 15$. However, when $K_{\max }>35$, the approximation quality in the decision space will decrease. It implies that with too many subpopulations, MMEA could not correctly estimate the shape of the PS.

From the above experiments, we can also conclude that for each of these four control parameters, there is a reasonably large range such that MMEA works well.

## D. CPU Time Cost

We have also recorded the CPU time used by each algorithm on $F 1-F 7$. The average CPU time ${ }^{3}$ used by the four

[^0]
[^0]:    ${ }^{3}$ The four algorithms are implemented in $\mathrm{C}++$, and they are executed in Thinkpad X60s with Intel Core Duo CPU L2400 1.66GHz, 2GB RAM, and Windows Vista.

![img-16.jpeg](img-16.jpeg)

Fig. 17. Average IGD metrics of the 20 final approximations versus $K_{\max }$ in MMEA on $F 3$.
TABLE VI
The Average CPU Time (in seconds) Used by Four Algorithms on $F 1-F 7$


algorithms are given in Table VI. Clearly, RM-MEDA needs much more CPU time than the three others. KP1 is the fastest in terms of CPU times. MMEA and Omni-Optimizer require about the same CPU time. The reason why MMEA is faster than RM-MEDA might be that the PCA used in MMEA requires much less CPU time than the local PCA used in RM-MEDA.

## VI. CONCLUSION

A good approximation to both the PS and the PF of an MOP might be required in some real-world applications. A good approximation to the PF of an MOP might not represent a good approximation to the PS, for example, when the MOP in question is of Class I or II. Some effort has been made to approximate both the PS and the PF of an MOP of Class I. This paper represents a first attempt to do so for an MOP of Class II.

MMEA proposed in this paper generalizes the idea used in RM-MEDA to an MOP of Class II for approximating its PS and PF simultaneously. In the modeling phase of MMEA, the population is clustered into a number of subpopulations based on their distribution in the objective space, the PCA technique is then used to estimate the dimensionality of the PS manifold in each subpopulation, and then a probabilistic model is built for modeling the distribution of promising solutions in the decision space. We argue that such a modeling procedure could promote the population diversity in both the decision and objective spaces. New solutions are sampled from the model thus built. The population for the next generation is selected by the NDS selection. The comparison between MMEA and the three other algorithms, KP1, Omni-Optimizer, and RMMEDA, on seven test instances, five of which were proposed
in this paper, has been made in this paper. Our empirical results have clearly indicated that MMEA has a big advantage over the three other algorithms in approximating both the PS and the PF of an MOP of Class II. We have investigated the ability of MMEA to deal with a regular MOP and an MOP of Class I. We have also studied the sensitivity of control parameters in MMEA.

The future research topics along this line may include:

1) extension of MMEA to constrained MOPs, and MOPs under dynamic and/or noisy environment for approximating both their PS and PF [39]-[41];
2) study of the scalability of MMEA to the numbers of decision variables and objectives [42]-[44];
3) use of other machine learning methods in MMEA [45]-[47];
4) combination of other techniques, particularly, traditional mathematical programming methods and new ideas in MOEAs, with MMEA for improving the algorithm performance.
The C++ code of MMEA can be downloaded from Q. Zhang's homepage: http://dces.essex.ac.uk/staff/qzhang/.
