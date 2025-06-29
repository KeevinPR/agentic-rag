# A regularity model-based multiobjective estimation of distribution algorithm with reducing redundant cluster operator 

Yong Wang a,b, Jian Xiang a,b,$\cdot$, Zixing Cai ${ }^{\text {a,b }}$<br>${ }^{a}$ School of Information Science and Engineering, Central South University, Changsha 410083, PR China<br>${ }^{\mathrm{b}}$ Hunan Engineering Laboratory for Advanced Control and Intelligent Automation, Changsha 410083, PR China


#### Abstract

Aregularity model-based multiobjective estimation of distribution algorithm (RM-MEDA) has been proposed for solving continuous multiobjective optimization problems with variable linkages. RM-MEDA is a kind of estimation of distribution algorithms and, therefore, modeling plays a critical role. In RM-MEDA, the population is split into several clusters to build the model. Moreover, the fixed number of clusters is recommended in RM-MEDA when solving different kinds of problems. However, based on our experiments, we find that the number of clusters is problem-dependent and has a significant effect on the performance of RM-MEDA. Motivated by the above observation, in this paper we improve the clustering process and propose a reducing redundant cluster operator (RRCO) to build more precise model during the evolution. By combining RRCO with RM-MEDA, we present an improved version of RM-MEDA, named IRM-MEDA. In this paper, we also construct four additional continuous multiobjective optimization test instances. The experimental results have shown that IRM-MEDA outperforms RM-MEDA in terms of efficiency and effectiveness. In particular, IRM-MEDA performs on average $31.67 \%$ faster than RM-MEDA.


## 1. Introduction

Many optimization problems involve not one but several objectives which should be optimized simultaneously. This kind of problems is considered as multiobjective optimization problems (MOPs). In this paper, we consider the following continuous MOPs: minimize $\quad \bar{y}=\bar{f}(\bar{x})=\left(f_{1}(\bar{x}), f_{2}(\bar{x}), \ldots, f_{m}(\bar{x})\right)$
where $\bar{x}=\left(x_{1}, \ldots, x_{n}\right) \in X \subseteq R^{n}$ is the decision vector, $X$ is the decision space, $\bar{y} \in Y \subseteq R^{m}$ is the objective vector, and $Y$ is the objective space.

There are some basic definitions in multiobjective optimization, which are introduced as follows.

Definition 1. Given two decision vectors $\bar{a}=\left(a_{1}, \ldots, a_{n}\right)$ and $\bar{b}=$ $\left(b_{1}, \ldots, b_{n}\right)$, if $\forall i \in\{1, \ldots, m\}, f_{i}(\bar{a}) \leq f_{i}(\bar{b})$ and $\exists j \in\{1, \ldots, m\}, f_{j}(\bar{a})<$ $f_{j}(\bar{b})$, we say $\bar{a}$ Pareto dominates $\bar{b}$, denoted as $\bar{a}<\bar{b}$.

Definition 2. A decision vector $\bar{x} \in X$ is called Pareto optimal solution if there does not exist another decision vector $\bar{x}^{\prime} \in X$ such that $\bar{x}^{\prime} \prec \bar{x}$.

[^0]Definition 3. The Pareto set (PS) is the set of all the Pareto optimal solutions:
$P S=\{\bar{x} \in X \mid \neg \exists \bar{x}^{\prime} \in X, \bar{x}^{\prime} \prec \bar{x}\}$
The solutions in the PS are also called nondominated solutions.
Definition 4. The Pareto front $(P F)$ is the set of the objective vectors of all the Pareto optimal solutions:
$P F=\{\bar{f}(\bar{x}) \mid \bar{x} \in P S\}$
For MOPs, in most cases, we cannot find a single solution to optimize all the objectives at the same time. Therefore, we have to balance them and find a set of optimal tradeoffs, i.e., Pareto set $(P S)$ in the decision space and Pareto front $(P F)$ in the objective space, respectively. Since evolutionary algorithms (EAs) deal with a group of candidate solutions simultaneously, it seems to be natural to use EAs for finding a group of Pareto optimal solutions when solving MOPs. Vector evaluation genetic algorithm (VEGA), introduced by Schaffer [1] in 1980s, is the first actual implementation of EAs to solve MOPs. After that, a considerable number of multiobjective evolutionary algorithms (MOEAs) have been proposed due to increasing interest in solving MOPs by EAs.

The development of MOEAs can be briefly divided into three generations [2,3]. In the first generation of MOEAs, Pareto ranking and fitness sharing are the most common techniques adopted by MOEAs. There are some paradigms in this generation, for


[^0]:    * Corresponding author at: School of Information Science and Engineering, Central South University, Changsha 410083, PR China.

    E-mail addresses: ywang@csu.edu.cn (Y. Wang), xiangjiancsu@gmail.com (J. Xiang).

example: nondominated sorting genetic algorithm (NSGA), proposed by Srinivas and Deb [4], is based on several layers of classifications of the individuals as suggested by Goldberg [5] and uses crowding distance to maintain the diversity of the population. Niched-Pareto genetic algorithm (NPGA), proposed by Horn et al. [6], employs tournament selection based on Pareto dominance and fitness sharing to keep the diversity. Fonseca and Fleming [7] introduced a multiobjective genetic algorithm (MOGA).

The second generation of MOEAs is characterized by the elitism preservation, which usually stores the nondominated individuals into a predefined archive (also called external population). It is necessary to note that incorporating the elitism into MOEAs can facilitate the convergence of the population. Zitzler and Thiele [8] proposed strength Pareto EA (SPEA), which uses an archive to store the nondominated solutions found so far and adopts clustering to prune the archive if the number of nondominated individuals in the archive exceeds a predefined value. Zitzler et al. [9] also proposed an improved version of SPEA, referred as SPEA2. Compared with SPEA, SPEA2 has the following three properties: (1) a new fitness assignment strategy, (2) a density estimation technique, and (3) a novel archive truncation method. Knowles and Corne [10] presented Pareto archive evolutionary strategy (PAES), which uses $(1+1)$-ES to generate offspring. In PAES, the offspring is compared with the parent and the previously archived nondominated individuals for survival. Moreover, PAES divides the objective space into grids, the aim of which is to maintain the diversity of the population. Inspired by PAES, Corne et al. further developed PESA [11] and PESA-II [12]. Deb et al. [13] proposed an improved version of NSGA, called NSGA-II, by incorporating a fast nondominated sorting approach and a crowding-comparison approach.

In the current research, which belongs to the third generation of MOEAs, some new dominance concepts other than traditional Pareto dominance have been introduced. For instance, Laumanns et al. [14] introduced $\varepsilon$-dominance. Hernández-Díaz et al. [15] proposed an adaptive $\varepsilon$-dominance, which is an improvement of the original $\varepsilon$-dominance [14]. Ben Said et al. [16] proposed $r$-dominance for interactive evolutionary multi-criteria decision making. Brockoff and Zitzler [17] proposed a local dominance scheme to reduce objective dimensionality. In addition, some researchers combined traditional weight vector based techniques with EAs to deal with MOPs [18], [19], [20], [21]. Recently, Zhang and Li [22] proposed a novel MOEA based on decomposition, called MOEA/D, which converts MOPs into a set of scalar optimization subproblems. Moreover, MOEA/D utilizes the neighbor information to produce offspring and optimize the subproblems simultaneously.

Many attempts have also been made to improve the performance of MOEAs by making use of different kinds of EAs as well as swarm intelligence. For example, Coello Coello et al. [23] incorporated Pareto dominance into particle swarm optimization for solving MOPs. Li and Zhang [24] proposed a new version of MOEA/D [22] based on differential evolution. Igel et al. [25] developed a variant of covariance matrix adaptation evolution strategy (CMA-ES) [26] for multiobjective optimization. Ghoseiria and Nadjari [27] presented an algorithm based on multiobjective ant colony optimization to solve the bi-objective shortest path problem. Jamuna and Swarup [28] proposed a multiobjective biogeography based optimization algorithm to design optimal placement of phasor measurement units. Zhang [29] proposed an immune optimization algorithm for dealing with constrained nonlinear multiobjective optimization problems.

Recently, indicator-based MOEAs have also been actively researched in the community of evolutionary multiobjective optimization $[30,31]$.

It can be induced from the Karush-Kuhn-Tucker condition that the PS of a continuous MOP is a ( $m-1$ )-dimensional piecewise continuous manifold in the decision space [32], [33], where $m$ is the number of objectives. Thus, for the continuous biobjective optimization problems (i.e., $m=2$ ), the $P S$ is a piecewise continuous curve; and for the continuous triobjective optimization problems (i.e., $m=3$ ), the $P S$ is a piecewise continuous 2-D surface.

Based on the above regularity, Zhang et al. [34] proposed a regularity model-based multiobjective estimation of distribution algorithm, referred as RM-MEDA. As a kind of estimation of distribution algorithms (EDAs) [35], RM-MEDA employs the ( $m-1$ )dimensional local principal component analysis (( $m-1$ )-D local PCA) [36] to build the model of the $P S$ in the decision space. The ( $m-1$ )-D local PCA is a locally linear approach to nonlinear dimension reduction, which can construct local models, each pertaining to a different disjoint region of the data space. In RM-MEDA, firstly, the ( $m-1$ )-D local PCA divides the population into $K$ ( $K$ is a constant integer) disjoint clusters and computes the central point and principal component of each cluster. Afterward, one model is built based on the corresponding central point and principal component for each cluster. The primary aim of modeling in RM-MEDA is to approximate one of the pieces of the $P S$ by making use of the solutions in one cluster. Ideally, if the number of clusters $K$ is equal to the number of the pieces of the $P S$, each piece of the $P S$ can be approximated by one cluster. In this case, a precise model may be built and the performance of RM-MEDA may be excellent. However, if the number of clusters $K$ is not equal to the number of the pieces of the $P S$; needless to say, the model is not precise.

Since we have no priori knowledge about the number of the pieces of the $P S$ for a MOP at hand, it is very difficult to determine a reasonable value for $K$. Moreover, the setting of $K$ is usually problem-dependent. In particular, based on our experiments, this parameter has a significant effect on the performance of RM-MEDA. Since $K$ is fixed to 5 in RM-MEDA, this setting might not be very effective for different kinds of MOPs. In order to overcome the above drawback of RM-MEDA, we design a reducing redundant cluster operator (RRCO) to enhance the modeling precision of RM-MDEA. By integrating RRCO with RM-MEDA, IRM-MEDA is derived. Extensive experiments have been conducted to compare IRM-MEDA with its predecessor RM-MEDA on a set of biobjective and triobjective test instances with variable linkages (note that variable linkages reflect the interactions among the variables). The experimental results verify that the efficiency and effectiveness of RM-MEDA can be significantly improved by RRCO.

The rest of the paper is organized as follows. Section 2 briefly reviews RM-MEDA. The drawback of modeling in RMMEDA is discussed in Section 3. Section 4 presents the details of RRCO. IRM-MEDA is described in Section 5. The experimental results are reported in Section 6. Finally, Section 7 concludes this paper.

## 2. Review of RM-MEDA

### 2.1. Framework

During the evolution, RM-MEDA maintains:

- a population $P_{t}$ of $N$ individuals: $P_{t}=\left(\hat{x}_{1}, \ldots, \hat{x}_{N}\right)$, where $t$ is the generation number;
- their $\tilde{f}$-values : $\tilde{f}\left(\hat{x}_{1}\right), \ldots, \tilde{f}\left(\hat{x}_{N}\right)$.

RM-MEDA is implemented as follows:

![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of the manifolds of the $P S$ for a biobjective optimization problem. The manifolds $\psi_{1}, \psi_{2}$, and $\psi_{3}$ are used to approximate the $P S, \xi$ is uniformly randomly sampled from $\psi_{i}(i=1, \ldots, 3), \bar{\varepsilon}$ is an $n$-dimensional zero-mean noise vector over $\psi_{i}(i=1, \ldots, 3)$, and $\bar{x}_{i}$ is the center of the $i$ th cluster which corresponds to the $i$ th manifold $\psi_{i}$.

Step 1 Initialization: Generate an initial population $P_{0}$ by randomly sampling $N$ individuals from the decision space $S$ and compute the $\hat{f}$-values of these individuals.
Step 2 Modeling: According to the population $P_{1}$, build the probability model by the $(m-1)$-D local PCA.
Step 3 Sampling: Generate an offspring population $Q_{i}$ by sampling from the probability model established in Step 2 and compute the $\hat{f}$-value of each individual in $Q_{i}$.
Step 4 Selection: Select $N$ individuals from $P_{1}$ and $Q_{i}$ to construct the population $P_{n+1}$ for the next generation.
Step 5 Stopping criterion: If the stopping criterion is satisfied, stop and output the $\hat{f}$-values of the nondominated individuals in the final population, otherwise set $t=t+1$ and go to Step 2 .

It is necessary to note that the selection process in Step 4 is a variant of the nondominated sorting-based selection proposed by Deb et al. [13]. The only difference is that when the number of the selected individuals is larger than $N$, RM-MEDA removes the redundant individuals with the smallest crowding distances one by one and recalculates the crowding distance after removing one individual. From the above framework, it is obvious that modeling is one of the most important steps of RM-MEDA. The details of the modeling will be explained next.

### 2.2. Modeling

RM-MEDA exploits the distribution information of the current population in the decision space to build the model. Thereafter, new solutions will be obtained by sampling from the model. Hopefully, the individuals in the population will be uniformly scattered around the $P S$ in the decision space as search goes on. RM-MEDA envisages the individuals in the population as independent observations of a random vector $\tilde{\xi}$ which can be formulated as follows:
$\tilde{\xi}=\xi+\bar{\varepsilon}$
where $\xi$ is uniformly distributed over a piecewise continuous $(m-1)$-dimensional manifold, and $\bar{\varepsilon}$ is an $n$-dimensional zero-mean noise vector.

One of the aims of modeling is to find the principal curve or surface of the population. For the sake of simplicity, suppose that the centroid of $\xi$ consists of $K$ manifolds: $\psi_{1}, \ldots, \psi_{K}$, each of which is a ( $m-1$ )-dimensional hyper-rectangle. That is to say, $\xi$ is uniformly distributed over these manifolds. An illustration is given in Fig. 1. Suppose that $\xi$ is uniformly randomly sampled from $\psi_{j}(i=1, \ldots$, $K$ ) and $\bar{\varepsilon} \sim N\left(0, \sigma_{i} l\right)$ where $l$ is the $n \times n$ identity matrix and $\sigma_{i}>0$ $(i=1, \ldots, K)$. By doing this, the task of modeling is transformed to estimate $\psi_{j}$ and $\sigma_{i}$.

RM-MEDA firstly splits the population $P_{k}$ into $K$ subpopulations $C_{1}, \ldots, C_{K}$. Then each subpopulation $C_{j}$ is utilized to estimate $\psi_{j}$ and $\sigma_{i}(i \in\{1, \ldots, K\})$. RM-MEDA uses the following procedure to achieve the above purpose:

Step 1
Randomly initialize $L_{i}^{m-1}, i=1, \ldots, K$, to be an affine ( $m-1$ )-dimensional principal subspace containing an individual randomly chosen from the population $P_{k}$.
Step 2 Partition the individuals of $P_{k}$ into $K$ clusters $C_{1}, \ldots, C_{K}$ :
$C_{i}=(\bar{x}) \bar{x} \in P_{k}$, and $\operatorname{dist}\left(\bar{x}, L_{i}^{m-1}\right) \leq \operatorname{dist}\left(\bar{x}, L_{k}^{m-1}\right)$ for all $k \neq i$ )
where $\operatorname{dist}\left(x, L_{i}^{m-1}\right)$ means the Euclidean distance between $\bar{x}$ and its projection in $L_{i}^{m-1}$.
Step 3 Update $L_{i}^{m-1}, i=1, \ldots, K$.
Step 4 Repeat Steps 2 and 3 until no change in partition is made.
In the above procedure, $L_{i}^{m-1}$ is the affine $(m-1)$-dimensional principal subspace of the individuals in $C_{i}$. In Step 3, $L_{i}^{m-1}$ can be updated by the mean and the covariance matrix of the individuals in $C_{i}$. The mean of $C_{i}$ is:
$\bar{x}_{i}=\frac{1}{\left|C_{i}\right|} \sum_{\bar{x} \in C_{i}} \bar{x}$
and the covariance matrix is:
$\operatorname{Cov}=\frac{1}{\left|C_{i}\right|-1} \sum_{\bar{x} \in C_{i}}\left(\bar{x}-\bar{x}_{i}\right)\left(\bar{x}-\bar{x}_{i}\right)^{T}$
In addition, the $j$ th principal component $\tilde{U}_{j}^{j}$ is a unity eigenvector associated with the $j$ th largest eigenvalue of the covariance matrix Cov. Then $L_{i}^{m-1}$ is updated as follows:
$\left(\bar{x} \in R^{n}\right) \bar{x}=\bar{x}_{i}+\sum_{j=1}^{m-1} \alpha_{j} \tilde{U}_{j}^{j}, \alpha_{j} \in R^{n}, \quad j=1, \ldots, m-1\}$

Next, RM-MEDA uses the above clustering results to build the model. RM-MEDA calculates the range of the projections of the individuals of each cluster $C_{i}$ in the first $(m-1)$ principal components:
$I_{j}^{j}=\min _{\bar{x} \in C_{i}}\left(\left(\bar{x}-\bar{x}_{i}\right)^{T} \tilde{U}_{j}^{j}\right)$
and
$u_{i}^{j}=\max _{\bar{x} \in C_{i}}\left(\left(\bar{x}-\bar{x}_{i}\right)^{T} \tilde{U}_{j}^{j}\right)$
where $\bar{x}_{i}$ is the mean, $\tilde{U}_{j}^{j}$ is the $j$ th principal component of the covariance matrix Cov of $C_{i}$, and $j \in\{1, \ldots, m-1\}$.

Then, each $(m-1)$-D manifold $\psi_{i}$ is constructed as follows:
$\psi_{i}=\left\{\bar{x} \in R^{n} \mid \bar{x}=\bar{x}_{i}+\sum_{j=1}^{m-1} \beta_{j} \tilde{U}_{j}^{j}, I_{j}^{j}-0.25\left(u_{i}^{j}-I_{j}^{j}\right) \leq \beta_{j} \leq u_{j}^{j}\right.$

$$
+0.25\left(u_{i}^{j}-I_{j}^{j}\right), \quad j=1, \ldots, m-1\}
$$

It is necessary to note that in order to make a better approximation of the $P S$, RM-MEDA enlarges the range of the projections in each direction $\tilde{U}_{j}^{j}(j=1, \ldots, m-1)$ by $50 \%$.

In addition, $\sigma_{i}$ is set as follows:
$\sigma_{i}=\frac{1}{n-m+1} \sum_{j=m}^{n} \lambda_{i}^{j}$
where $\lambda_{i}^{j}$ is the $j$ th largest eigenvalue of the covariance matrix $C o v$ of $C_{i}$.

Remark 1. As pointed out previously, RM-MEDA is a kind of estimation of distribution algorithms, which exploits the distribution

information of the population to generate the next population. CMA-ES, proposed by Hansen and Ostermeier [26], also incorporates the distribution information of the population into evolution strategy (ES). CMA-ES adopts the following formulation to generate new solutions:
$\tilde{x}_{i, t+1}=\tilde{m}_{t}+\tilde{\sigma}_{t} \times N\left(\mathbf{0}, \mathbf{C}_{i}\right), \quad i=1, \ldots, \lambda$
where $t$ is the generation number, $\tilde{x}_{i, t+1}$ is the ith offspring, $N\left(\mathbf{0}, \mathbf{C}_{i}\right)$ is a multivariate normal distribution with zero mean and covariance matrix $\mathbf{C}_{i}, \tilde{m}_{t}$ is the mean value of the search distribution, and $\tilde{\sigma}_{t}$ is the overall standard deviation (i.e., the step-size).

Clearly, both Eqs. (4) and (13) contain two terms. However, there are some significant differences between RM-MEDA and CMA-ES. Firstly, in Eq. (4) $\tilde{\boldsymbol{\xi}}$ is uniformly distributed over some manifolds, while in Eq. (13) $\tilde{m}_{t}$ is the mean value of the $\mu$ best individuals at generation $t$. Secondly, when generating the next population, RM-MEDA mainly uses the eigenvectors and eigenvalues of the covariance matrix of the last population, nevertheless, in CME-ES the cumulative evolution path is utilized to update the covariance matrix $\mathbf{C}_{i}$ and the standard deviation $\tilde{\sigma}_{t}$.

## 3. The drawback of modeling in RM-MEDA

According to the introduction in Section 2, we can see that modeling is a very important process in RM-MEDA. Moreover, more promising solutions may be generated by sampling from a more precise model. Since the PS of the continuous MOPs is a piecewise continuous ( $m-1$ )-dimensional manifold, RM-MEDA firstly partitions the population $P_{t}$ into $K$ clusters $C_{1}, \ldots, C_{K}$ by making use of the ( $m-1$ )-D local PCA, with the aim of estimating one manifold $\psi_{i}$ with one cluster $C_{i}$. However, a question which naturally arises is: how to determine the value of $K$ ? In RM-MEDA, $K$ is set to a constant integer (i.e., 5). However, needless to say, different shapes of the PS may require different number of clusters, and thus, require different values of $K$.

Suppose that the PS of a MOP is shown in Fig. 1. Clearly, in this case if $K$ is set to 3 , the $\psi_{i}$ obtained by modeling can approximate one of the pieces of the PS effectively. However, if $K$ is not equal to 3 , what will be the corresponding result then? Next, we will discuss the influence of the value of $K$ on the performance.

As shown in Fig. 2, the PS is a piecewise continuous 1-D sine curve:
$x_{i}=\sin \left(2 \pi x_{1}\right), \quad i=2,3, \ldots, n, \quad 0 \leq x_{1} \leq 1$
where $n$ is the dimension of the decision space. For simplicity, we assume that $n$ is equal to 2. In Fig. 2, the dots denote the individuals which uniformly scatter around the PS.
![img-2.jpeg](img-2.jpeg)

Fig. 2. The $P S$ is a piecewise continuous 1-D sine curve, and some individuals are uniformly distributed around the $P S$.

Clearly, in this case, three manifolds $\psi_{i}(i=1,2$, and 3$)$ can approximate the sine curve effectively. That is, 3 is a suitable value for the number of clusters $K$. Fig. 3(a) shows the result of clustering by the ( $m-1$ )-D local PCA with $K=3$ and Fig. 3(b) exhibits the $\psi_{i}$ ( $i=1,2$, and 3) computed by Eq. (11). We can see from Fig. 3 that the $P S$ can be approximated by $\psi_{i}(i=1,2$, and 3$)$ very well. However, it should be emphasized that the clustering with the ( $m-1$ )-D local PCA has some randomness and, therefore, we cannot get the same clustering result if the clustering is applied repeatedly. It is because the ( $m-1$ )-D local PCA begins with $K$ randomly selected initial points (see Step 1 in Section 2.2) and the clustering result depends on the initial points to a certain degree. When $K$ is set to 3 in our experiments, Fig. 3 shows the typical clustering result.

When $K$ is set to 2 which is smaller than actually required, two typical clustering results are shown in Figs. 4 and 5. From Figs. 4 and 5, we can see that the estimated manifolds $\psi_{i}(i=1$ and 2) cannot approximate the PS very well. In particular, as shown in Fig. 5, few better solutions could be sampled from the model built for each cluster. Hence, in this case the performance of the algorithm will significantly degrade. More importantly, maybe the algorithm could not convergence to the $P S$ because of the incorrect approximation.

Remark 2. If the number of clusters is smaller than required, the model built will be incorrect, and thus, results in a side influence on the performance of the algorithm.

On the other hand, how about the number of clusters larger than required? Figs. 6-8 show three typical clustering results with $K=5$.
![img-2.jpeg](img-2.jpeg)

Fig. 3. The results of clustering and modeling with $K=3$. (a) The result of clustering. (b) The manifolds $\psi_{i}(i=1,2$ and 3$)$ built from the clusters.

![img-6.jpeg](img-6.jpeg)

Fig. 4. The results of clustering and modeling with $K=2$. (a) The result of clustering. (b) The manifolds $\psi_{1}(i=1$ and 2$)$ built from the clusters.
![img-4.jpeg](img-4.jpeg)

Fig. 5. The results of clustering and modeling with $K=2$. (a) The result of clustering. (b) The manifolds $\psi_{1}(i=1$ and 2$)$ built from the clusters.
![img-5.jpeg](img-5.jpeg)

Fig. 6. The results of clustering and modeling with $K=5$. (a) The results of clustering. (b) The models $\psi_{1}(i=1, \ldots, 5)$ built from the clusters.
![img-6.jpeg](img-6.jpeg)

Fig. 7. The results of clustering and modeling with $K=5$. (a) The results of clustering. (b) The models $\psi_{1}(i=1, \ldots, 5)$ built from the clusters.

![img-7.jpeg](img-7.jpeg)

Fig. 8. The results of clustering and modeling with $K=5$. (a) The results of clustering. (b) The models $\psi_{i}(i=1, \ldots, 5)$ built from the clusters.

As shown in these figures, among all the manifolds, three manifolds can be used to estimate the distribution of the $P S$ while there are two redundant manifolds. For example, $\psi_{4}$ and $\psi_{5}$ are two redundant manifolds in Fig. 6. Usually, the points sampled from $\psi_{4}$ and $\psi_{5}$ are inferior solutions. It is very difficult for these inferior solutions to survive into the next generation. Moreover, the more the inferior individual solutions are generated at each generation, the more the number of function evaluations might be wasted. In addition, from Fig. 7 it is clear that $\psi_{1}, \psi_{2}$, and $\psi_{5}$ approximate the same part of the $P S$ and, consequently, they can be reduced to just one. As shown in Fig. 8, the second cluster includes only one point. Indeed, it is not an effective cluster and the occurrence of this phenomenon is due to the inappropriate clustering number.
Remark 3. If the number of clusters is larger than required, although the $P S$ can be approximated by the model built, there exist some redundant and incorrect manifolds, which have a side effect on the convergence speed and the convergence quality of the algorithm.

Conclusion: According to the above analysis, we can conclude that if the number of clusters used in RM-MEDA is inappropriate, the performance of RM-MEDA will degrade to a certain degree. Particularly, when the number of clusters is smaller than required, the model is always built incorrectly. In this case, RM-MEDA could not converge to the true $P S$. On the other hand, if the number of clusters is larger than required, some redundant manifolds will be generated, which results in the deterioration of the convergence speed and the convergence quality. In general, under the condition that the number of clusters is inappropriate, the performance of RM-MEDA with the number of clusters larger than required is superior to that of RM-MEDA with the number of clusters smaller than required. Maybe this is the reason why in RM-MEDA the number of clusters is set to a slightly big value (i.e., 5), which is larger than required for all the test instances in [34].

## 4. Reducing redundant cluster operator

Although RM-MEDA usually sets the number of clusters with a big value, as analyzed previously, a big value will also have a side effect on the performance. Moreover, the setting of the number of clusters is usually problem-dependent. In order to overcome the above drawback of RM-MEDA, we propose a reducing redundant cluster operator (RRCO) in this paper. In the following, the details of RRCO are introduced.

According to the discussion in Section 3, if there exist some redundant clusters, two particular phenomena may occur: (1) the cluster has only one point (as shown in Fig. 8); and (2) some overlapped manifolds approximate the same part of the $P S$, see for example, $\psi_{1}, \psi_{2}$, and $\psi_{5}$ in Fig. 7 , and $\psi_{3}$ and $\psi_{4}$ in Fig. 8 .

RRCO is designed to address the above two particular phenomena. After implementing the local PCA, we obtain $K$ clusters $C_{1}, \ldots$, $C_{K}$ and $K$ manifolds $\psi_{1}, \ldots, \psi_{K}$. Then, RRCO works as follows:

Step 1 Set $A=\left\{\psi_{i}, \ldots, \psi_{K}\right\}$
Step 2 For $i=1: K$
Step 3 If $C_{i}$ only contains one individual, then $A=A \backslash \psi_{i}$;
Step 4 End For
Step 5
$L=0$;
Step 6 While $|A|>0$
Step 7 Choose the first manifold from $A$, denoted as $\psi^{\prime}$ and $A=A \backslash \psi^{\prime}$;
Step 8 For $i=1:|A|$
Step 9 If both condition 1 and condition 2 (these two conditions will be explained later) are satisfied for the $i$ th manifold in $A$ and $\psi^{\prime}$, store this manifold to $B$;
Step 10 End For
Step 11 $A=A \backslash B$;
Step 12 $L=L+1$;
Step 13 End While
Step 14 $K=L$.
During the evolution, we adjust $K$ by RRCO at each generation and use the updated $K$ as the new number of clusters for the next generation.

In RRCO, we use the included angle of two manifolds to identify the overlapped manifolds. When a MOP has $m$ objectives, the included angle is computed between $(m-1)$-D hyper-rectangle. Thus, the included angle is computed between two lines for a biobjective optimization problem, and the included angle is computed between two planes for a triobjective optimization problem. In general, if the included angle of two manifolds is less than a predefined value $\theta$, we consider that these two manifolds overlap with each other. Note, however, that the included angle between parallel manifolds is also very small. As shown in Fig. 9 (this figure is obtained from Fig. 8(b) by eliminating the sine curve, cluster 1,
![img-8.jpeg](img-8.jpeg)

Fig. 9. Illustration of the overlapped manifolds and the parallel manifolds.

cluster 3, cluster 4, and cluster 5), the included angle between the manifolds $\psi_{3}$ and $\psi_{4}$ which overlap with each other is small, while the included angle between the manifolds $\psi_{1}$ and $\psi_{5}$ which are parallel with each other is also very small. Therefore, if we only use the included angle of two manifolds to judge whether these two manifolds overlap with each other, some errors may arise.

Next, Fig. 9 is employed as an example to explain how to identify the overlapped manifolds and the parallel manifolds. In Fig. 9, points $a, b, c$, and $d$ are the central points of the fourth, third, first, and fifth clusters, respectively. The included angle between line segment $\overline{a b}$ and the manifold $\psi_{3}$ or the manifold $\psi_{4}$ is relatively small, so we consider that $\psi_{3}$ and $\psi_{4}$ are overlapped manifolds. However, the included angle between line segment $\overline{c d}$ and the manifold $\psi_{1}$ or the manifold $\psi_{5}$ is relatively large, so we can conclude that $\psi_{1}$ and $\psi_{5}$ are parallel manifolds. Based on the above analysis, we use the following conditions to distinguish the overlapped manifolds and the parallel manifolds:

Condition 1: $\left\langle\psi_{j}, \psi_{j}\right\rangle<\theta$
Condition 2: $\min \left(\left\langle\overline{C P_{0}^{c}}, \psi_{i}\right\rangle,\left\langle\overline{C P_{0}}, \psi_{j}\right\rangle\right)<\left\langle\psi_{i}, \psi_{j}\right\rangle$, where $\overline{C P_{0}}$ denotes the line segment between $C P_{i}$ and $C P_{j}$, and $C P_{i}$ and $C P_{j}$ are the central points of the clusters $C_{i}$ and $C_{j}$, respectively.

In the above two conditions, $\left\langle\psi_{i}, \psi_{j}\right\rangle$ denotes the included angle between $\psi_{i}$ and $\psi_{j},\left\langle\overline{C P_{0}^{c}}, \psi_{i}\right\rangle$ denotes the included angle between $\overline{C P_{0}}$ and $\psi_{i}$, and $\left\langle\overline{C P_{0}}, \psi_{j}\right\rangle$ denotes the included angle between $\overline{C P_{0}}$ and $\psi_{j}$. In this paper, $\theta$ is a threshold value and is set to $(3 / 180) \pi$. If both condition 1 and condition 2 are satisfied, the manifolds $\psi_{i}$ and $\psi_{j}$ are considered overlapped, while if condition 1 is satisfied and condition 2 is unsatisfied, the manifolds $\psi_{i}$ and $\psi_{j}$ are considered parallel. The method to compute the included angle between arbitrary dimension hyper-planes in the Euclidean space is given in Appendix A.

## 5. IRM-MEDA

By combining RRCO with RM-MEDA, we present an improved version of RM-MEDA, referred as IRM-MEDA. The framework of IRM-MEDA is the same as that of RM-MEDA except that IRM-MEDA uses RRCO to update $K$. In RM-MEDA, $K$ is fixed during the evolution, whereas IRM-MEDA dynamically adjusts $K$ by extracting some information from the result of clustering at each generation.

IRM-MEDA performs as follows:
Step 1 Initialization: Randomly generate an initial population $P_{0}=\left(\bar{x}_{1}, \bar{x}_{2}, \ldots, \bar{x}_{N}\right)$ and initialize $K$ (i.e., the number of clusters).
Step 2 Modeling: Use the local PCA to build the model.
Step 3 Modify the value of $K$ by RRCO.
Step 4 Sampling: Generate the offspring population $Q_{i}$ by sampling from the model built.
Step 5 Selection: Select $N$ individuals from $P_{i}$ and $Q_{i}$ to construct the next population $P_{i+1}$.
Step 6 Stopping criterion: If the stopping criterion is satisfied, stop and output the $\hat{f}$-values of the nondominated individuals of the final population, otherwise go to Step 2.
The procedures of initialization, modeling, sampling, and selection in IRM-MEDA are exactly the same as in RM-MEDA. It is necessary to note that during the sampling, firstly the volume of each manifold $\psi_{i}$ is computed, and then the probability that a new solution is generated around $\psi_{i}$ is proportional to the volume of $\psi_{i}$. When generating a new solution, the parameter $\beta_{i}$ in Eq. (11) is randomly chosen between $I_{i}^{t}-0.25\left(u_{i}^{t}-I_{i}^{t}\right)$ and $u_{i}^{t}+0.25\left(u_{i}^{t}-I_{i}^{t}\right)$. The interested reader can refer to [34] for details.

## 6. Experimental study

### 6.1. Test instances

In this paper, we use ten test instances (F1-F10) to verify the effectiveness of IRM-MEDA. The main information of these ten test instances is summarized in Table 1. Test instances F1-F6 are taken from [34]. Since the primary purpose of RM-MEDA is to approximate the $P S$ of MOPs by taking advantage of the $(m-1)$-D local PCA, we construct four additional test instances (i.e., F7-F10) with various $P S$ structures to further compare RM-MEDA with IRM-MEDA. It is necessary to note that the $P S$ structures of F7-F10 are more complex than that of the other six test instances and, therefore, F7-F10 pose a great challenge for both RM-MEDA and IRM-MEDA. The $P S$ of these ten test instances has been introduced in Table 1.

In terms of the way of variable linkages, these test instances can be divided into two categories: test instances with linear variable linkages (i.e., F1-F3) and test instances with nonlinear variable linkages (i.e., F4-F10).

Remark 4. Test instances F1, F4, F7, and F8 are variants of ZDT1 [37] and test instances F2 and F5 are variants of ZDT2 [37]. According to the Theorem 1 in [38], F1, F2, F4, F5, F7, and F8 in this paper have the $P S\left(x_{1}, x_{2}^{*}, x_{3}^{*}, \ldots, x_{n}^{*}\right)$, where $x_{2}^{*}, x_{3}^{*}, \ldots, x_{n}^{*}$ are the solutions of $g(\bar{x})$, respectively, and $x_{1}$ can take any value in $[0,1]$. Test instances F3 and F6 are variants of DTLZ2 [39]. According to the explanation in [39], F3 and F6 in this paper have the $P S\left(x_{1}, x_{2}, x_{3}^{*}, \ldots, x_{n}^{*}\right)$, where $x_{2}^{*}, \ldots, x_{n}^{*}$ are the solutions of $g(\bar{x})$, respectively, and $x_{1}$ and $x_{2}$ can take any value in [0,1]. Test instances F9 and F10 are variants of test instances F2 and F9 in [24], respectively. According to the Theorem 1 on F2 and F9 in [24], F9 in this paper has the $P S\left(x_{1}, x_{2}^{*}, x_{3}^{*}, \ldots, x_{n}^{*}\right)$, where $x_{2}^{*}, x_{3}^{*}, \ldots, x_{n}^{*}$ are equal to $\sin \left(2 \pi x_{1}\right)$, respectively, and $x_{1}$ can take any value in $[0,1]$, and F10 in this paper has the $P S\left(x_{1}, x_{2}^{*}, x_{3}^{*}, \ldots, x_{n}^{*}\right)$, where $x_{2}^{*}, x_{3}^{*}, \ldots, x_{n}^{*}$ are equal to $\cos \left(2 \pi x_{1}\right)$, respectively, and $x_{1}$ can take any value in $[0,1]$.

### 6.2. Performance indicators

In this paper, two performance indicators are adopted to compare RM-MEDA and IRM-MEDA.

The first performance indicator measures the convergence speed of an algorithm. When computing the convergence speed of an algorithm, we need to design a stopping criterion. Once the stopping criterion is satisfied, the algorithm is considered convergent and the procedure should halt. Since the purpose of the solution of a MOP is to find the $P S$, the image of which in the objective space is called $P F$, the stopping criterion is based on the reasonable approximation of true $P F$. Let $P^{*}$ be a set of points uniformly distributed on the true $P F$, and $P$ a set of points which are the image of the nondominated individuals of the population in the objective space. In this paper, firstly the hyper-volume (HV) values [8], [40] are calculated for $P^{*}$ and $P$, respectively. Afterward, we follow the approach introduced by Nebro et al. [41] to determinate the stopping criterion. In [41], once the HV value of $P$ attains or surpasses the $98 \%$ of the HV value of $P^{*}$, i.e.,

$$
\frac{H V(P)}{H V\left(P^{*}\right)}<98 \%
$$

we consider that a reasonable approximation the true $P F$ has been obtained. Under this condition, the algorithm terminates and the number of function evaluations (FES) is recorded. In Eq. (15), $H V(P)$ denotes the hyper-volume surrounded by $P$ and a fixed reference point, and $H V\left(P^{*}\right)$ denotes the hyper-volume surrounded by $P^{*}$ and a fixed reference point. We use the mean and standard derivation of FES among 20 independent runs as the first performance indicator

Table 1
The main information of test instances.

Table 1 (Continued)

to measure the convergence speed of an algorithm on each test instance. In our experiments, the size of $P^{*}$ is set to 300 and 800 for the biobjective optimization problems and for the triobjective optimization problems, respectively.

The second performance indicator measures the convergence quality of an algorithm. The inverted generational distance (IGD) is employed for this purpose, which is one of the most commonly used performance indicators in MOEAs and can be described as follows [34]:
$D\left(P^{*}, P\right)=\frac{\sum_{v \in P} c \cdot d(v, P)}{\left|P^{*}\right|}$
where $d(v, P)$ denotes the minimum Euclidean distance between $v$ and the points in $P$. IGD indicator computes the average distance from all members in the true $P F$ to their nearest points in $P$. This performance indicator can measure both the diversity and the convergence of the population. $D\left(P^{*}, P\right)=0$ indicates that all the points in $P$ are on the true $P F$ and cover the true $P F$ uniformly.

### 6.3. Experimental results

### 6.3.1. Convergence speed

Firstly, we compare the convergence speed of IRM-MEDA and RM-MEDA in terms of the first performance indicator. The maximal number of FES is set to 30,000 for F1, F2, F4, F5 and F8, to 50,000 for F7, F9, and F10, and to 80,000 for F3 and F6. For test instances with two objectives, the population size is set to 100, and for test
instances with three objectives, the population size is set to 200. 20 independent runs have been performed for each test instance, and the average and standard deviation of the number of FES to satisfy Eq. (15) in each run have been recorded. Table 2 summarizes the experimental results. Wilcoxon's rank sum test at a 0.05 significance level is conducted on the experimental results. In addition, we also use the acceleration rate $(A R)$ to compare the convergence speed, which is defined as follows:
$A R=\frac{A V E_{\text {RM-MEDA }}-A V E_{\text {IRM-MEDA }}}{A V E_{\text {RM-MEDA }}}$
where $A V E_{\text {RM-MEDA }}$ and $A V E_{\text {IRM-MEDA }}$ denote the average number of FES provided by RM-MEDA and IRM-MEDA in Table 2, respectively.

As shown in Table 2, IRM-MEDA performs significantly better than RM-MEDA on all the test instances according to the Wilcoxon's rank sum test. Furthermore, IRM-MEDA saves 20-50\% FES compared with RM-MEDA, and the mean $A R$ is $31.67 \%$.

The above discussion demonstrates that RRCO has the capability to significantly accelerate the convergence of RM-MEDA.

### 6.3.2. Convergence quality

As mentioned above, the IGD indicator is applied to measure both the convergence and diversity of the population. For each test instance, the same number of FES has been performed for both IRMMEDA and RM-MEDA. Based on the results in Table 2, the maximal number of FES for each test instance is set about to the mean number of FES required by IRM-MEDA to achieve the $98 \%$ of the HV

Table 2
Experimental results of IRM-MEDA and RM-MEDA over 20 independent runs for ten test instances in terms of the convergence speed. "Mean FES" and "Std Dev" indicate the average and standard deviation of FES obtained in 20 runs, respectively. "AR" denotes the acceleration rate. Wilcoxon's rank sum test at a 0.05 significance level is performed between IRM-MEDA and RM-MEDA.
"+", "-", and " $\approx$ " denote the performance of IRM-MEDA is better than, worse than, and similar to that of RM-MEDA, respectively.

Table 3
Experimental results of IRM-MEDA and RM-MEDA over 20 independent runs for ten test instances in terms of the IGD indicator. "Mean IGD" and "Std Dev" indicate the average and standard deviation of the IGD indicator obtained in 20 runs, respectively. Wilcoxon's rank sum test at a 0.05 significance level is performed between IRM-MEDA and RM-MEDA.

"+", "-", and " $\approx$ " denote the performance of IRM-MEDA is better than, worse than, and similar to that of RM-MEDA, respectively.
value of the true $P F$. We have performed 20 independent runs for IRM-MEDA and RM-MEDA, and obtained the mean and standard deviation of the IGD indicator as shown in Table 3. In order to ensure the results with statistical confidence, Wilcoxon's rank sum test at a 0.05 significance level has also been performed.

Table 3 demonstrates that IRM-MEDA provides evidently lower IGD values than RM-MEDA for all the test instances. Moreover, the statistical test indicates that IRM-MEDA outperforms RM-MEDA on all the test instances. Therefore, we can conclude that RRCO is able to significantly improve the convergence quality of RM-MEDA.

Figs. 10-13 exhibit the typical nondominated fronts and all the nondominated fronts of 20 independent runs derived from IRMMEDA and RM-MEDA for two representative test instances.

The $P S$ of F5 is a bounded continuous conic curve. In this case, the model built by RM-MEDA might not be reasonable due to the redundant clusters as analyzed in Section 3, which has a negative influence on the convergence speed and the convergence quality of the population. As shown in Figs. 10 and 11, the differences of the nondominated fronts provided by IRM-MEDA and RM-MEDA on F5 are distinct.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Plots of the nondominated individuals of the final populations in a typical run obtained by IRM-MEDA and RM-MEDA in the objective space on F5.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Plots of the nondominated individuals of all the final populations in 20 runs obtained by IRM-MEDA and RM-MEDA in the objective space on F5.

![img-11.jpeg](img-11.jpeg)

Fig. 12. Plots of the nondominated individuals of the final populations in a typical run obtained by IRM-MEDA and RM-MEDA in the objective space on F7.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Plots of the nondominated individuals of all the final populations in 20 runs obtained by IRM-MEDA and RM-MEDA in the objective space on F7.

The $P S$ of F7 is a period continuous sine curve. For this kind of PS, it is very likely for an algorithm to build a wrong model which greatly deviates from the PS of the test instance. Clearly, new trial solutions sampled from the wrong model are often inferior points. These inferior solutions are hard to survive to the next generation and may greatly affect the convergence speed of the population because a lot of FES used to evaluate these inferior solutions will be wasted. Moreover, the redundant clusters will further deteriorate the performance. It can be observed from Figs. 12 and 13 that RMMEDA cannot converge to the $P F$ very well and easily misses some parts of the $P F$.

Based on our observations, when the procedure of IRM-MEDA terminates in each run, the number of clusters (i.e., the parameter $K$ ) achieved by IRM-MEDA is $1,1,1,2,2,3,3,2,3$, and 2 for test instances F1-F10, respectively. The above number of clusters for each test instance is consistent with the actual situation of each test instance.

### 6.4. Comparison with MOEA/D-DE

In this subsection, the performance of IRM-MEDA is compared with that of another state-of-the-art MOEA, named MOEA/D-DE [24] over the ten test functions F1-F10 in this paper. The two performance indicators introduced in Section 6.2 are used to compare IRM-MEDA and MOEA/D-DE. For IRM-MEDA and MOEA/D-DE, 20 independent runs are implemented on each test instance. We use the same parameter settings for MOEA/D-DE as in the original paper. The experimental results are summarized in Tables 4 and 5. Wilcoxon's rank sum test at a 0.05 significance level is conducted on the experimental results.

Table 4
Experimental results of IRM-MEDA and MOEA/D-DE over 20 independent runs for ten test instances in terms of the convergence speed. "Mean FES" and "Std Dev" indicate the average and standard deviation of FES obtained in 20 runs, respectively. "AR" denotes the acceleration rate. Wilcoxon's rank sum test at a 0.05 significance level is performed between IRM-MEDA and MOEA/D-DE.
"+", "--", and " $\sim$ " denote the performance of IRM-MEDA is better than, worse than, and similar to that of MOEA/D-DE, respectively.

From Tables 4 and 5, it is clear that overall IRM-MEDA significantly outperforms MOEA/D-DE. In terms of the convergence speed, IRM-MEDA is faster than MOEA/D-DE on eight test instances, and MOEA/D-DE converges faster than IRM-MEDA only on two test instances. In addition, with respect to the IGD indicator, IRM-MEDA surpasses MOEA/D-DE on seven test functions, and MOEA/D-DE beats IRM-MEDA only on two test functions.

Table 5
Experimental results of IRM-MEDA and MOEA/D-DE over 20 independent runs for ten test instances in terms of the IGD indicator. "Mean IGD" and "Std Dev" indicate the average and standard deviation of the IGD indicator obtained in 20 runs, respectively. Wilcoxon's rank sum test at a 0.05 significance level is performed between IRM-MEDA and MOEA/D-DE.

"+", "--", and " $=$ " denote the performance of IRM-MEDA is better than, worse than, and similar to that of MOEA/D-DE, respectively.

Table 6
Experimental results of IRM-MEDA with varying $\theta$. "Mean IGD" and "Std Dev" indicate the average and standard deviation of the IGD indicator obtained in 20 runs for ten test instances. The best result for each test instance among the compared algorithms is highlighted in boldface.

### 6.5. Sensitivity to the parameter $\theta$ in RRCO

In RRCO, an additional parameter $\theta$ is used. To study the sensitivity of the parameter $\theta$, we test five different values: $(1 / 180) \pi$, $(2 / 180) \pi,(3 / 180) \pi,(5 / 180) \pi$, and $(7 / 180) \pi$. For each value of $\theta$, IRM-MEDA performs 20 runs independently for all the test instances and the IGD indicator is used to assess the performance.

Table 6 demonstrates that IRM-MEDA with $\theta=(3 / 180) \pi$ has the best overall performance. When $\theta$ is set to a relatively smaller value (i.e., $(1 / 180) \pi$ and $(2 / 180) \pi$ ), the performance of the algorithm suffers from slight degeneration for F1, F3, F4, F5, F6, F7, F8, and F10, compared with IRM-MEDA with $\theta=(3 / 180) \pi$. In addition, we also observe that when dealing with F7, F8, F9, and F10 which have more complicated PS, the performance degradation of IRM-MEDA with $(5 / 180) \pi$ occurs, compared with IRM-MEDA with $\theta=(3 / 180) \pi$. In the case of $\theta=(7 / 180) \pi$, the algorithm exhibits the worst performance for F6, F7, and F8.

From the above discussion, $\theta=(3 / 180) \pi$ is recommended for RRCO.

## 7. Conclusion

RM-MEDA [34] is a recently proposed approach for solving MOPs with variable linkages. In order to approximate the PS of MOPs, the ( $m-1$ )-D local PCA is adopted to build the model of the population in RM-MEDA. In this paper, we analyze the drawback of the clustering process in the modeling suggested by RM-MEDA. Based on our analysis, the number of clusters is problem-dependent and has a significant effect on the performance of RM-MEDA.

However, a fixed number of clusters is recommended in [34] for different kinds of problems.

In this paper, we propose an improved version of RM-MEDA, namely IRM-MEDA, by incorporating a reducing redundant cluster operator (RRCO) to dynamically modify the number of clusters during the evolution. RRCO can adaptively decrease the redundant clusters. The experimental results suggest that the performance of IRM-MEDA is significantly better than that of RM-MEDA in terms of the convergence speed and the convergence quality.

It is worth noting that in this paper we only deal with the number of clusters $K$ larger than required since usually we initialize the number of clusters $K$ with a slightly big value when solving MOPs. How to cope with the case that the number of clusters $K$ is smaller than required is one of our future work. In addition, we will apply IRM-MEDA to solve some real-world MOPs in the future. When applying IRM-MEDA to solve real-world MOPs, firstly we need to elaborate the encoding operator. Moreover, some domain-specific knowledge should be extracted and integrated into IRM-MEDA for increasing efficiency and effectiveness.

The source code of IRM-MEDA is written in MATLAB and can be obtained from the first author upon request.

## Acknowledgments

The authors sincerely thank the anonymous reviewers for their constructive and helpful comments and suggestions.

This research was supported in part by the National Natural Science Foundation of China under Grant 60805027, 61175064 and 90820302, and in part by the Research Fund for the Doctoral Program of Higher Education under Grant 200805330005.

## Appendix A.

When dealing with MOPs with $(m+1)$ objectives, after implementing the local PCA, the $m$-dimensional manifolds $\psi_{i} \in R^{m \times n}$, $i=1,2, \ldots, K$ ( $n$ is the dimension of decision space) are obtained and satisfy $\psi_{i} \psi_{i}^{T}=E$. According to the theorem of high dimension Euclidean geometry [42,43], the included angle $\theta$ between $\psi_{i}$ and $\psi_{j}(i, j \in\{1,2, \ldots K)$ and $i \neq j$ ) can be computed as follows:
Step 1 Compute the singular values of $\psi_{i} \psi_{i}^{T}$.
Step 2 If all the $m$ singular values are equal to 1
Step 3 $\quad \theta=0$;
Step 4 Eheif less than $m$ singular values are equal to 1 and the remaining singular values are equal to 0
Step 5 $\quad \theta=\pi / 2$;
Step 6 Ehe
Step 7 $\quad \theta=\arccos (n)$, where $n$ is the largest singular value and less than 1 .
Step 8 End If
