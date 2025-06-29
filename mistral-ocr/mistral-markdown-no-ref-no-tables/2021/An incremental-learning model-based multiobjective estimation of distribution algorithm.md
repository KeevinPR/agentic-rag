# An incremental-learning model-based multiobjective estimation of distribution algorithm 

Tingrui Liu ${ }^{\mathrm{a}}$, Xin Li ${ }^{\mathrm{b}}$, Liguo Tan ${ }^{\mathrm{c}, *}$, Shenmin Song ${ }^{\mathrm{a}, *}$<br>${ }^{a}$ Center for Control Theory and Guidance Technology, Harbin Institute of Technology, Harbin 150001, China<br>${ }^{\mathrm{b}}$ Sino-German Robotics School, Shenzhen Institute of Information Technology, Shenzhen 518172, China<br>${ }^{\mathrm{c}}$ Research Center of Basic Space Science, Harbin Institute of Technology, Harbin 150001, China

## A R T I C L E I N F O

Article history:
Received 10 June 2020
Received in revised form 15 March 2021
Accepted 2 April 2021
Available online 8 April 2021

Keywords:
Evolutionary algorithm
Multiobjective optimization
Estimation of distribution
Incremental learning
Gaussian mixture model

## A B S T R A C T

Knowledge obtained from the properties of a Pareto-optimal set can guide an evolutionary search. Learning models for multiobjective estimation of distributions have led to improved search efficiency, but they incur a high computational cost owing to their use of a repetitive learning or iterative strategy. To overcome this drawback, we propose an algorithm for incremental-learning model-based multiobjective estimation of distributions. A learning mechanism based on an incremental Gaussian mixture model is embedded within the search procedure. In the proposed algorithm, all new solutions generated during the evolution are passed to a data stream, which is fed incrementally into the learning model to adaptively discover the structure of the Pareto-optimal set. The parameters of the model are updated continually as each newly generated datum is collected. Each datum is learned only once for the model, regardless of whether it has been preserved or deleted. Moreover, a sampling strategy based on the learned model is designed to balance the exploration/exploitation dilemma in the evolutionary search. The proposed algorithm is compared with six state-of-the-art algorithms for several benchmarks. The experimental results show that there is a significant improvement over the representative algorithms.
(c) 2021 Elsevier Inc. All rights reserved.

## 1. Introduction

In many engineering tasks, the outcome naturally has multiple expected properties. We have a multiobjective optimization problem (MOP) when we do not know how to balance the properties with a priori weight but must consider each of them as a separate objective function. In this case, we have to optimize simultaneously two or more objective functions that may conflict with each other. Thus, there may not be a unique optimal solution that achieves the best outcome for each objective. For MOPs, we aim to find a set of good compromises for the decision maker [1], which is called the Paretooptimal set (PS). The objective vectors of the PS cover the Pareto front (PF).

An evolutionary algorithm, since its population-based nature perfectly matches the solution set required for MOPs, could be adopted to build a representative subset of the PS in a single run. Thus, the multiobjective evolutionary algorithm (MOEA) has become the preferred method for addressing complicated MOPs. Extensive studies have been carried out to design and improve MOEAs in the last three decades. One of the burgeoning trends is integrating a machine learning mechanism into the framework of MOEA [2], because using the knowledge learned from the population would enhance the efficiency of the

[^0]
[^0]:    * Corresponding authors.

    E-mail addresses: liutingrui@126.com (T. Liu), eshing_lie126.com (X. Li), tanliguo@hit.edu.cn (L. Tan), songshenmin@hit.edu.cn (S. Song).

evolutionary search. The PS of a continuous MOP with $m$ objectives is a piecewise continuous ( $m-1$ )-dimensional manifold under mild conditions. Since the manifold property of the PS was reported for RM-MEDA [3], many supervised and unsupervised learning methods, such as Gaussian processes, Bayesian networks, neural networks, restricted Boltzmann machines, and self-organizing maps (SOMs), have been applied to learn and estimate the PS of a MOP to produce high-quality offspring.

Work on learning-based MOEAs focuses on learning the property of the PS, mainly from the following two aspects. On the one hand, a learning model of the manifold structure can be used to approximate the PS directly. For example, local principal component analysis was applied to build a probability distribution for the manifold structure of a PS in RM-MEDA. Zhou et al. [4] proposed a MOEA based on decomposition and probabilistic modeling, in which a multivariate Gaussian model was established to extract information about the local and global distributions to generate offspring. Liu et al. [5] designed a Baldwinian learning operator to obtain the descent direction of an evolutionary search based on a distribution model of the current population. On the other hand, instead of approximating the PS with models, some researchers have designed a mating restriction mechanism based on the manifold property of the PS. These MOEAs divide the population into several subpopulations, in which individuals with high similarity and mutual recombination approximate the PS. Zhang et al. [6] defined neighborhood relationships among solutions by utilizing a SOM to establish the topological structure of the population. Li et al. [7] used the $k$-means clustering algorithm to extract information about the neighborhood relationship for each individual for the mating restriction. Sun et al. [8] designed an indicator based on information from subpopulations. It adaptively indexed the different requirement levels in the exploration/exploitation compromise.

However, the machine learning model in MOEA always has a high computational cost [9], which mainly arises from two factors. First, the iterative strategies used during learning inherently have a high computational cost [7]. The algorithms usually learn the knowledge from the entire population of solutions through multiple iterations until converging to a wellpleasing result. They appear to have little effect early in the evolutionary process, as the initial solutions differ widely from the theoretical optimal solutions [10]. Second, the high computational cost stems from repetitive learning [8]. Some solutions, which survive the fitness selection, are repeatedly used for model learning, despite being unable to provide new knowledge for the model. Repetitive learning does not modify the model, so adds to the computational cost.

To decrease the computational cost, a feasible approach is to have fewer iterations in learning. Zhang et al. [11] adopted a SOM for the entire population, with only one iteration for each generation. However, some solutions survive several environmental selections and are still repeatedly used for SOM learning. Liu et al. [12] proposed that the learning machine is not run unless the population of adjacent generations has no significant similarity. Cheng et al. [13] constructed Gaussian process-based inverse models from the objective space to the decision space to find nondominated solutions. A random grouping technique was used to reduce the number of inverse models. Li et al. [14] incorporated manifold learning into multiobjective optimization. This nonlinear dimensionality-reduction technique extracts the geometric properties of lowdimensional manifolds embedded in the high-dimensional ambient space. However, these approaches still have unnecessary computational costs due to the iterations or repetitive learning when the population approximates the PS.

Inspired by data stream learning [15], an incremental-learning model-based multiobjective algorithm to estimate distributions, named ILME, is proposed and investigated. In ILME, all new solutions generated in the evolutionary process are combined into a data stream, which is called the evolving data stream. Each new generated solution is a datum in the evolving data stream. The evolving data stream is fed into a learning mechanism based on an incremental Gaussian mixture model (IGMM), which is employed to discover the manifold structure of the PS. The parameters of the model are updated continually as newly generated data are collected. Each datum is learned only once by the incremental model, regardless of whether it has been preserved or deleted from the population. Moreover, the sampling strategy based on the learned model is designed to balance the exploration/exploitation dilemma in the evolutionary search.

This paper is organized as follows. Section 2 briefly discusses related work and the IGMM. Section 3 describes the algorithmic framework of ILME and its components. The numerical experiments are considered in Section 4. The algorithmic sensitivity of the parameters and further experiments are discussed in Section 5. Section 6 concludes the paper and suggests future research avenues.

# 2. Related work 

### 2.1. Background

A box-constrained continuous MOP could be formulated mathematically as follows:

$$
\begin{array}{ll}
\min & \mathbf{F}(\mathbf{x})=\left(f_{1}(\mathbf{x}), f_{2}(\mathbf{x}), \ldots, f_{m}(\mathbf{x})\right)^{\top} \\
\text { s.t. } & \mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)^{\top} \in \Omega \subset \mathbb{R}^{n}
\end{array}
$$

where $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)^{\top}$ is a $n$-dimensional decision vector. $\Omega$ defines the feasible decision (search) space in the $n$ dimensional decision space $\mathbb{R}^{n} . \mathbf{F}: \Omega \rightarrow \mathbb{R}^{m}$ is a mapping from the decision space to the objective space, which consists of $m$ objective functions. For two solutions $\mathbf{u}, \mathbf{v} \in \Omega, \mathbf{u}$ is said to dominate $\mathbf{v}$ if and only if $f_{i}(\mathbf{u}) \leqslant f_{i}(\mathbf{v})$ for all $i \in\{1,2, \ldots, m\}$ and $\mathbf{F}(\mathbf{u}) \neq \mathbf{F}(\mathbf{v})$. A solution is Pareto optimal if no other solution in $\Omega$ dominates it. The set of all Pareto optimal solutions constitutive of Pareto optimal set (PS), while the objective vectors of PS is named Pareto front (PF), denoted by $\mathrm{PF}=\{\mathbf{F}(\mathbf{x}) \in \mathbb{R}^{m} \mid \mathbf{x} \in \mathrm{PS}\}$.

Many remarkable efforts have been devoted to designing and improving MOEAs for MOPs in the last three decades. Roughly, MOEAs can be based on dominance, a metric, or decomposition. Dominance-based MOEAs adopt the Pareto dominance relationship to maintain convergence preferentially. Other strategies are used to preserve diversity. Examples include NSGA-II [16], PESA-II [17], and NSGA-III [18]. Metric-based MOEAs employ a performance metric (e.g., hypervolume, R2, or $\Delta_{p}$ ) as the optimization objective to guide the selection of solutions. Examples include SMS-EMOA [19], R2-IBEA [20], and DDE [21]. Decomposition-based MOEAs decompose the original MOPs into a set of single-objective optimization problems or simplified MOPs, and optimize them with a collaborative method. Examples include MOEA/D [22], TMOEA/D [23], and MOEA/D-LTD [2]. In addition, MOEAs are often applied to aid decision-making [1].

# 2.2. Multiobjective estimation of distribution algorithms 

The proposed algorithm is type of a multiobjective estimation of distribution algorithm (MOEDA), which is a modified form of the estimation of distribution algorithm (EDA). The modeling method and the fitness assignment function are the two major components of a MOEDA. Its fitness assignment function usually comes from a MOEA, and most often in current research, a Pareto dominance-based approach is used. The modeling method adopted in MOEDA is based either on a mixture of distributions or on a graphical model.

MOEDAs based on graphical models lean mostly upon Bayesian network, which is a graphical expression of the conditional relationships among the stochastic variables. One of the most widely used algorithms is the multiobjective Bayesian optimization algorithm [24], which exploits the fitness assignment of NSGA-II. A hierarchical Bayesian optimization algorithm [25] uses a strength criterion from SPEA, but combines $k$-means in the objective space to improve scalability. By estimating a Gaussian Bayesian network to cluster the solutions, the diversity-preserving multiobjective real-coded Bayesian optimization algorithm [26] transforms the problem variables and utilizes a diversity-preserving selection mechanism, which uses a dynamic crowding and adaptive sharing approach. Martins et al. [27] developed a hybrid multiobjective Bayesian estimation of distribution algorithm (HMOBEDA), which scrutinizes a probabilistic graphic model based on a Bayesian network. The probabilistic graphic model gives the joint probability of decisions, objectives, variables, and configuration parameters to assess the influence of both diversity and convergence along the approximate PF. Martins et al. [28] improved HMOBEDA using the information in the final structure of the probabilistic graphic model. Garrido et al. [29] designed an information-based predictive entropy search for the simultaneous optimization of multiple expensive-to-evaluate blackbox functions under the presence of several constraints.

MOEDAs based on a mixture of distributions explicitly employ a mixture of probability distributions to directly approximate the PS. Bosman et al. [30] proposed multiobjective iterated density estimation algorithms (MIDEAs) as a paradigm for MOEDA, in which a probabilistic model is learned to stimulate the desirable parallel exploration along the PF. Li et al. [31] proposed a hybrid EDA with a joint probability distribution for multiobjective $0 / 1$ knapsack problems. The adaptive variance scaling was enhanced by introducing a standard deviation ratio trigger embedded within the normal mixture distribution in MIDEA [32]. This approach avoids the loss of diversity and premature convergence. Further, adaptive variance scaling has been conjointly employed with an anticipated mean shift in a multiobjective adapted maximum-likelihood Gaussian mixture model (GMM) [33]. Shim et al. [34] introduced a restricted Boltzmann machine, which is an energy-based stochastic neural network, into MOEDA. The energy function of the network is used to construct a probabilistic model. Mohagheghi et al. [35] adopted a Voronoi mesh to construct the stochastic model. Maza et al. [36] integrated the mutual information between random variables as a probabilistic model to guide the search by modeling the redundancy and relevance relations between features in intrusion detection systems.

Apart from the above-mentioned research, "learnable" MOEDA represents a new frontier in research on MOEDA and is a paradigm that integrates MOEDA solvers with knowledge learning to achieve better optimization efficiency and performance. Based on this paradigm, MOEDAs with different learning algorithms, such as manifold learning [37], generative adversarial networks [38], and growing neural gas [9], have been developed. For example, SMEA [11] is a newly proposed competitive MOEA, which learns a self-organizing mapping in decision space to model the PF for assisting the evolutionary search for the PS. MDESL [39] carries out a k-means clustering analysis on the current population to extract knowledge about neighborhood relationships for mating restriction. MOEA/D-LTD [2] uses a Gaussian process-based model to learn the mapping from $(m-1)$ objective functions to the remaining objective function ( $m$ is the number of objectives) for characterizing the estimated PF. As mentioned earlier, these MOEDAs suffer from the problem of high computational cost.

### 2.3. Incremental Gaussian mixture model

IGMMs [15], concept formation algorithms based on unsupervised learning, aim to learn a GMM incrementally from the data stream. IGMMs have excellent modeling ability and can form smooth approximations for arbitrarily shaped densities. They can accommodate components of different sizes and correlation structures. Compared with batch learning, incremental learning does not usually require a significant amount of computing resources. Hence, we use an IGMM in incremental learning for the generated solutions during the evolutionary process. A GMM with $K$ components in a $D$-dimensional space can be defined as follows:

$$
\left\{\begin{array}{l}
p(\mathbf{x} \mid \Theta)=\sum_{k=1}^{K} \pi_{k} \mathscr{N}\left(\mathbf{x} \mid \boldsymbol{\mu}_{k}, \Sigma_{k}\right) \\
\mathscr{N}\left(\mathbf{x} \mid \boldsymbol{\mu}_{k}, \Sigma_{k}\right)=\frac{1}{(2 \pi)^{3 / 2}\left|\Sigma_{k}\right|^{1 / 2}} \exp \left\{-\frac{1}{2}\left(\mathbf{x}-\boldsymbol{\mu}_{k}\right)^{T} \Sigma_{k}^{-1}\left(\mathbf{x}-\boldsymbol{\mu}_{k}\right)\right\} \\
\sum_{k=1}^{K} \pi_{k}=1, \pi_{k} \geqslant 0
\end{array}\right.
$$

where $\Theta=\left\{\pi_{k}, \boldsymbol{\mu}_{k}, \Sigma_{k}\right\}_{k=1}^{K}$ is the set of model parameters and $\pi_{k}$ is the prior of the $k$-th Gaussian component with mean vector $\boldsymbol{\mu}_{k}$ and covariance matrix $\Sigma_{k}$.

# Algorithm 1. Incremental Gaussian Mixture Model 

Require: the existent model parameters $\Theta_{0}=\left\{\pi_{k}^{0}, \boldsymbol{\mu}_{k}^{0}, \Sigma_{k}^{0}\right\}_{k=1}^{K}$, the number of collected data $N$, the newly available data $\left\{\mathbf{x}^{*}\right\}$.
Ensure: the newly model parameters $\Theta=\left\{\pi_{k}, \boldsymbol{\mu}_{k}, \Sigma_{k}\right\}_{k=1}^{K}$.
1: while $\left|L\left(\Theta_{t+1}\right)-L\left(\Theta_{t}\right)\right| \leqslant \Delta$ do
2: E-step: Evaluate the posterior probabilities, i.e. the membership weight of the newly available data $\mathbf{x}^{*}$ in mixture component $K$, by:

$$
p\left(k \mid \mathbf{x}^{*}\right)=\frac{\pi_{k}^{t} \mathscr{N}\left(\mathbf{x}^{*} \mid \boldsymbol{\mu}_{k}^{*}, \Sigma_{k}^{t}\right)}{\sum_{j=1}^{K} \pi_{j}^{t} \mathscr{N}\left(\mathbf{x}^{*} \mid \boldsymbol{\mu}_{j}^{*}, \Sigma_{j}^{t}\right)}, \quad 1 \leqslant k \leqslant K
$$

and compute the expectation vector $E_{k}^{t}$, by:

$$
E_{k}^{t}=N \pi_{k}^{t}, \quad 1 \leqslant k \leqslant K
$$

3: M-step: Re-estimate the parameters using the current responsibilities:

$$
\begin{aligned}
& \pi_{k}^{t+1}=\frac{E_{k}^{t}+p\left(k \mid \mathbf{x}^{*}\right)}{N+1} \\
& \boldsymbol{\mu}_{k}^{t+1}=\frac{E_{k}^{t} \boldsymbol{\mu}_{k}^{t}+\mathbf{x}^{*} p\left(k \mid \mathbf{x}^{*}\right)}{E_{k}^{t}+p\left(k \mid \mathbf{x}^{*}\right)} \\
& \Sigma_{k}^{t+1}=\frac{E_{k}^{t}\left(\Sigma_{k}^{t}+\left(\boldsymbol{\mu}_{k}^{t}-\boldsymbol{\mu}_{k}^{t+1}\right)\left(\boldsymbol{\mu}_{k}^{t}-\boldsymbol{\mu}_{k}^{t+1}\right)^{T}\right)}{E_{k}^{t}+p\left(k \mid \mathbf{x}^{*}\right)}+\frac{p\left(k \mid \mathbf{x}^{*}\right)\left(\mathbf{x}^{*}-\boldsymbol{\mu}_{k}^{t+1}\right)\left(\mathbf{x}^{*}-\boldsymbol{\mu}_{k}^{t+1}\right)^{T}}{E_{k}^{t}+p\left(k \mid \mathbf{x}^{*}\right)}
\end{aligned}
$$

4: Evaluate the log-likelihood:

$$
L\left(\Theta_{t+1}\right)=\sum_{k=1}^{K} p\left(k \mid \mathbf{x}^{*}\right)\left[\ln \pi_{k}^{t+1}+\ln \mathscr{N}\left(\mathbf{x}^{*} \mid \boldsymbol{\mu}_{k}^{*}, \Sigma_{k}^{t}\right)\right]
$$

5: $\quad i \leftarrow i+1$.
6: end while

Algorithm 1 presents the main learning steps in the expectation-maximization algorithm for IGMM. The approach has separate code for the newly arrived data and for the data already fed to learn the model. The assumption is that the set of posterior probabilities $\left\{p\left(k \mid \mathbf{x}_{i}\right)\right\}_{j=1}^{N}$ remains the same when the model parameters are updated for the newly arrived data $\left\{\mathbf{x}^{*}\right\}$. By defining the newly arrived data $\left\{\mathbf{x}^{*}\right\}$ as an increase and the parameters of the learned model as $\left\{\pi_{k}, \boldsymbol{\mu}_{k}, \Sigma_{k}\right\}_{k=1}^{K}$, the model parameters are updated after initialization via an iterative method with two steps: an expectation step (E-step) and a maximization step (M-step). In the E-step (line 2), the posterior probabilities of the component memberships are computed for the newly available data. It then computes the expectation vector for the next step. In the M-step (line 3), using the component-membership posterior probabilities as weights, the parameters $\left\{\pi_{k}, \boldsymbol{\mu}_{k}, \Sigma_{k}\right\}_{k=1}^{K}$ are estimated based on maximizing the log-likelihood function. The E- and M-steps are constantly iterated until the log-likelihood function converges to the termination tolerance $\Delta$, which is a small positive scalar (line 4).

Fig. 1 is a demo of how an IGMM learns from a data stream. The data stream has six different groups, each of which contains 100 data points (from [15]). From demos 1 to 6 , the model is updated continually as the data stream is incrementally

![img-0.jpeg](img-0.jpeg)

Fig. 1. The learning processes of IGMM.
fed into it. After the 6 -th demo, the learning process has efficiently adapted the model to represent the data stream. Unlike an evolving data stream in an evolutionary search, the data stream used in the demo is independent and static. It has a global view of the data, i.e., all data points are randomly accessible. As the data stream is in a permuted order, the model does not change in the demo.

In contrast, the data in an evolving data stream depend on the generation and dynamically change. A window can be defined that slides over the evolving data stream, creating a partial view of the data. For a short window, the data are pseudo-stationary, whereas they converge over a longer time. Moreover, in IGMM, the data are stored and preserved during the learning process. An evolutionary search is an optimization process, and nondominated solutions gradually replace the worst solutions in the population during the evolutionary cycle. Hence, it is necessary to adjust IGMM if it is utilized to extract the structure of evolving data during an evolutionary process.

# 3. Proposed algorithm 

The major motivation for ILME was to integrate an IGMM-based learning mechanism into MOEA, so that it obtains knowledge efficiently. The incremental-learning mechanism takes a stream of solutions sequentially generated during the evolution as training data to model the manifold structure of the PS and establish the neighborhood relationships among solutions. The parameters of the learning model are updated incrementally as newly generated data are collected to reduce the computational cost, unlike the batch approach that is currently used. With the learned model, the offspring production operation, which consists of a sampling strategy and a differential evolution operator, generates new trial solutions toward the whole PF. There is a good guarantee of population diversity in the objective space. An outline of our proposed ILME algorithm is shown in Fig. 2. The detailed steps are given as pseudocode in Algorithms 2-4.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Outline of the ILME.

# Algorithm 2. ILME Framework 

Require: population size $N$, maximum evolutionary generations $\mathscr{I}$ and maximum number of components $K_{\max }$. Ensure: population $\mathscr{P}$.
1: Initialize a population $\mathscr{P}=\left\{\mathbf{x}^{1}, \mathbf{x}^{2}, \cdots, \mathbf{x}^{N}\right\}$ randomly, and set the external archive $\mathscr{A}=\mathscr{P}$.
2: Let each $\mathbf{x}^{i} \in \mathscr{P}$ as a component $\mathscr{C}_{k}$, update the $\mathscr{C}_{k}$ as follow:
$\boldsymbol{\mu}_{k}=\mathbf{x}^{i}, \boldsymbol{\Sigma}_{k}=\mathbf{I}, \pi_{k}=1 / N$.
3: while the termination criteria not met do
4: Count the number of components $K \leftarrow\left|\mathscr{C}_{k}\right|$.
5: Execute a Cholesky decomposition for covariance matrix of the each component $\boldsymbol{\Sigma}_{k}=\boldsymbol{\Lambda}_{k} \boldsymbol{\Lambda}_{k}^{T}, k=1,2, \ldots, K$.
6: for $i=1$ to $N$ do
7: $\quad$ Generate a trial solution $\mathbf{t x}^{i} \leftarrow \operatorname{Solgen}\left(\boldsymbol{\Lambda}_{k}^{i}, \mathscr{C}_{k}, \mathbf{x}^{i}\right)$.
8: Selection and Updating $[\mathscr{A}, \Theta] \leftarrow \operatorname{Selupd}\left(\mathscr{A}, \Theta, \mathbf{t x}^{i}\right)$.
9: end for
10: Update the population $\mathscr{P}=\mathscr{A}$ and pass the GMM parameter set $\Theta$ of $\mathscr{A}$ to $\mathscr{P}$.
11: end while

Pseudocode for ILME is given in Algorithm 2. In ILME, the population $\mathscr{P}$ is initialized randomly in the decision variable space. An external archive $\mathscr{A}$, built to maintain the solutions from the previous population, is assigned from $\mathscr{P}$ (line 1). Each solution is a component of the GMM in the initial population. The covariance matrix and weight coefficient are $\boldsymbol{\mu}_{k}=\mathbf{x}^{i}, \boldsymbol{\Sigma}_{k}=\mathbf{I}$, and $\pi_{k}=1 / N$, respectively (line 2 ). In the evolutionary cycle, first, the number of components is counted (line 4). For each component, a perturbation matrix $\boldsymbol{\Lambda}_{k}$ is generated using a Cholesky decomposition of its covariance matrix $\boldsymbol{\Sigma}_{k}$ (line 5). For each solution in the population, the proposed sampling strategy is utilized to create a trial solution (line 7). Then, the model parameter of the GMM is renewed incrementally with the solution as each new offspring solution is collected (line 8). When each solution in the current population has completed one evolution, the population $\mathscr{P}$ is renewed from the external archive $\mathscr{A}$ and a set of learned model parameters of the GMM is passed to it for the next evolution (line 10). The evolutionary cycles proceed until the termination criterion has been satisfied. Finally, ILME returns the final population.

### 3.1. Solution generation

The sampling strategy is a pivotal part of the trade-off between exploitation and exploration. A routine sampling strategy (RSS) in most EDAs is to add Gaussian noise after sampling from a learned model. Fig. 3(a) shows the search region for the RSS for a GMM with two components in an evaluation search. Fig. 3(a) shows $95 \%$ confidence regions for the parent solutions. The figure implies that the RSS can generate offspring solutions beyond the confidence region with a small probability (only $5 \%$ ), which limits the search ability and readily leads to a loss of diversity in the population in the early stages of the evolution.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Search regions under different sampling strategy. (a) Search region of RSS. (b) Search region of SCSS.

A simple, yet very effective way to overcome this inherent deficiency is to perform a Gaussian perturbation with the new trial solution in the current population. Knowledge from the learned model is used to guide the exploration. Hence, a novel sampling strategy is proposed, called the shared covariance-based advanced sampling strategy (SCSS). It uses information from the learned model. A new trial solution is perturbed using the covariance matrix of the component it belongs to. Fig. 3(b) shows that SCSS can explore beyond the current region, which certainly improves the search ability in exploration. Moreover, a differential evolution (DE) operator is used in the exploitation, especially in the last stage of the evolution. DE has two main control parameters which are the crossover constant $(C R)$ and differentiation factor $(F)$.

# Algorithm 3. Solution Generation (Solgen) Operator 

Require: a current solution $\mathbf{x}$, its perturbation matrix $\boldsymbol{\Lambda}$ and the component $\mathscr{C}_{k}$ it belongs to.
Ensure: a trial solution ts.
1 : if $\operatorname{rand}()<\varepsilon$
2: $\quad$ Sample $\mathbf{z} \in \mathbb{R}^{n}$ from $\mathscr{N}(0, \mathbf{I})$.
3: $\quad$ Generate a trial solution $\mathbf{t s}=\mathbf{x}+\boldsymbol{\Lambda} \mathbf{z}$.
4: else if
5: $\quad$ Generate a trial solution $\mathbf{t s}$ using the DE operator, as follow:

$$
t s_{j}=\left\{\begin{array}{ll}
x_{j}^{\prime}+F \times\left(x_{j}^{\prime \prime}-x_{j}^{\prime \prime}\right) & \text { if } r_{1}<C R \\
x_{j}^{\prime} & \text { otherwise }
\end{array} \quad, j=1,2, \ldots, n\right.
$$

where $\mathbf{x}^{\prime \prime}$ and $\mathbf{x}^{\prime \prime}$ are parent solutions selected from $\mathscr{C}_{k}$, randomly.
6: end if
7: Repair the solution ts, as follow:

$$
t s_{j}^{\prime \prime}= \begin{cases}a_{j} & \text { if } t s_{j}<a_{j} \\ b_{j} & \text { elseif } t s_{j}>b_{j} \\ t s_{3} & \text { otherwise }\end{cases} j=1,2, \ldots, n
$$

where $a_{j}, b_{j}$ are the lower and upper bounds of the $j$-th variables, respectively.
8: Mutate the solution $\mathbf{t s}^{\prime}$, as follow:

$$
t s_{j}^{\prime \prime}= \begin{cases}t s_{3}^{\prime}+\delta_{j} \times\left(b_{j}-a_{j}\right) & \text { if } r_{2}<p_{m} \\ t s_{3}^{\prime} & \text { otherwise } \quad, j=1,2, \ldots, n\end{cases}
$$

with

$$
\delta_{j}= \begin{cases}\left[2 r_{3}+\left(1-2 r_{3}\right)\left(\frac{b_{j}-a_{j}^{\prime}}{b_{j}-a_{j}^{\prime}}\right)^{\frac{n_{m}+1}{n_{m}+1}}\right]^{\frac{n_{m}+1}{n_{m}+1}}-1 & \text { if } r_{3}<0.5 \\ 1-\left[2-2 r_{3}+\left(2 r_{3}-1\right)\left(\frac{r_{3}^{\prime}-a_{3}}{b_{3}-a_{3}}\right)^{\frac{n_{m}+1}{n_{m}+1}}\right]^{\frac{1}{n_{m}+1}} & \text { otherwise }\end{cases}
$$

9: If necessary, repair the solution ts $\leftarrow$ ts ${ }^{\prime \prime}$.

Algorithm 3 shows the solution generation (Solgen) operator used in ILME. SCSS is utilized to produce a new trial solution with probability $\varepsilon$. Otherwise, the DE operator is used (lines 1-6). Then, a boundary repair operation is performed to ensure that the new offspring solution is feasible (line 7). Furthermore, the polynomial mutation operator is utilized on the feasible solution to improve the diversity of the population (line 8). Finally, the same boundary repair mechanism is performed again if necessary (line 9).

### 3.2. Selection and updating

In ILME, for each newly generated solution, first, its dominance relation is checked against each solution in the current external archive. The parameter of the learning model is updated for the new offspring solution only when it is not the worst. Hence, two operations are embedded within the selection and updating (SelUPP) operator in ILME. The superior selection mechanism is from SMS-EMOA [19] and the modification of the IGMM updating mechanism was inspired by agglomerative hierarchical clustering [40], in which pairs of clusters are merged successively when the number of clusters is above a threshold.

# Algorithm 4. Selection \& Updating (SELUPD) Operator 

Require: a trial solution $\mathbf{t s}$, the current external archive $\mathscr{A}$ and its model parameter set $\Theta$.
Ensure: external archive $\mathscr{A}$ and its model parameter set $\Theta$.
1: $\left\{\mathscr{R}^{1}, \mathscr{R}^{2}, \cdots, \mathscr{R}^{L}\right\} \leftarrow$ FastNondominatedSort $(\mathscr{A} \cup\{\mathbf{t s}\})$.
2: if $L>1$
3: Determine $\mathbf{x}^{\prime} \leftarrow \underset{\mathbf{x} \in \mathscr{R}^{L}}{\arg \max } d(\mathbf{x}, \mathscr{A} \cup\{\mathbf{t s}\})$.
4: else if
5: Determine $\mathbf{x}^{\prime} \leftarrow \underset{\mathbf{x} \in \mathscr{R}^{L}}{\arg \min } \Delta_{\varphi}\left(\mathbf{x}, \mathscr{R}^{1}\right)$.
6: end if
7: if $\mathbf{x}^{\prime} \neq \mathbf{t s}$
8: $\mathscr{A} \leftarrow \mathscr{A} \cup\{\mathbf{t s}\} \backslash\left\{\mathbf{x}^{\prime}\right\}$.
9: if $\mathscr{C}_{K}=\varnothing$
10: Delete the component $\mathscr{C}_{K}$, set $K \leftarrow K-1$.
11: else
12: Update the component $\mathscr{C}_{K}$ as follow:

$$
\begin{aligned}
& \pi_{K}=\frac{E_{K}-p\left(\mathbf{x}^{\prime} \mid k\right)}{N-1}, \quad \mu_{k}=\frac{E_{k} \mu_{k}-\mathbf{x}^{\prime} p\left(\mathbf{x}^{\prime} \mid k\right)}{E_{k}-p\left(\mathbf{x}^{\prime} \mid k\right)} \\
& \Sigma_{K}=\frac{E_{k} \Sigma_{K}-p\left(\mathbf{x}^{\prime} \mid k\right)\left(\mathbf{x}^{\prime}-\mu_{k}\right)\left(\mathbf{x}^{\prime}-\mu_{k}\right)^{T}}{E_{K}-p\left(\mathbf{x}^{\prime} \mid k\right)}
\end{aligned}
$$

13: end if
14: Set $K \leftarrow K+1$, construct a new component $\mathscr{C}_{K}$, set $\pi_{K}=1 / N, \boldsymbol{\mu}_{K}=\mathbf{t s}, \Sigma_{K}=\mathbf{I}$.
15: if $K>K_{\max }$
16: $\quad$ Determine: $(\alpha, \beta) \leftarrow \arg \min _{\alpha, \beta, \alpha \in \beta}\left\|\boldsymbol{\mu}_{\alpha}-\boldsymbol{\mu}_{\beta}\right\|$.
17: Merge the component as follows:
$\pi_{\gamma}=\pi_{\alpha}+\pi_{\beta}, \quad \boldsymbol{\mu}_{\gamma}=\frac{\pi_{\alpha} \boldsymbol{\mu}_{\alpha}+\pi_{\beta} \boldsymbol{\mu}_{\beta}}{\pi_{\alpha}+\pi_{\beta}}$
$\Sigma_{\gamma}=\frac{\pi_{\alpha}\left[\Sigma_{\alpha}+\left(\boldsymbol{\mu}_{\alpha}-\boldsymbol{\mu}_{\gamma}\right)\left(\boldsymbol{\mu}_{\alpha}-\boldsymbol{\mu}_{\gamma}\right)^{T}\right]}{\pi_{\alpha}+\pi_{\beta}}+\frac{\pi_{\beta}\left[\Sigma_{\alpha}+\left(\boldsymbol{\mu}_{\beta}-\boldsymbol{\mu}_{\gamma}\right)\left(\boldsymbol{\mu}_{\beta}-\boldsymbol{\mu}_{\gamma}\right)^{T}\right]}{\pi_{\alpha}+\pi_{\beta}}$.
18: end if
19: end if

Details of the selection and updating (SELUPD) operator in ILME are shown in Algorithm 4. After the new trial solution ts is generated, the external archive $\mathscr{A}$ is updated as follows. First, the fast nondominated sorting method derived from NSGA-II [16] is utilized to partition the combined set $\mathscr{A} \cup\{\mathbf{t s}\}$ into $L$ different fronts $\left\{\mathscr{R}^{1}, \mathscr{R}^{2}, \ldots, \mathscr{R}^{L}\right\}$, in which $\mathscr{R}^{i}$ is the $i$-th best front and $\mathscr{R}^{L}$ is the poorest one (line 1). Two strategies are used to determine a candidate solution $\mathbf{x}^{\prime}$, which is eliminated from the combined set: (1) Candidate solution $\mathbf{x}^{\prime}$ has the highest $d(\mathbf{x}, \mathscr{A} \cup\{\mathbf{t s}\})$ in $\mathscr{R}^{L}$ when there is more than one nondominated front in $\mathscr{A} \cup\{\mathbf{t s}\}$. Here, $d(\mathbf{x}, \mathscr{A} \cup\{\mathbf{t s}\})$ is the number of solutions that dominate $\mathbf{x}$ in $\mathscr{A} \cup\{\mathbf{t s}\}$ (line 3). (2) When there is only one nondominated front in $\mathscr{A} \cup\{\mathbf{t s}\}$, the candidate solution $\mathbf{x}^{\prime}$ has the lowest hypervolume (HV) $\Delta_{\varphi}\left(\mathbf{x}, \mathscr{R}^{1}\right)$ (line 5).

If the trial solution $\mathbf{t s}$ is not a candidate solution $\mathbf{x}^{\prime}$, two operations are executed after the environmental selection: (1) eliminating the candidate solution and (2) modifying the parameter of the component. First, $\mathbf{x}^{\prime}$ is removed from the combined set (line 8). The parameter of the component it belongs to is updated, which is a decremental process (lines 9-13). Then, $\mathbf{t s}$ is used as a mean vector to construct a new component (line 14). If the GMM has more than $K_{\max }$ components, the two components with the shortest Euclidean distance between their mean vectors are merged into one, and the parameter is calculated for the merged component (lines 15-18).

### 3.3. Computational complexity

The computational cost of ILME is mainly due to the SeLupD operator. During the incremental learning, each datum is processed at most twice, once when it is processed as a new component that has survived and then if a merged component becomes too close to another component. In the worst case, a newly generated solution is nondominated and there are more than $K_{\max }$ components. The learning process requires $O\left(n K^{2}\right)$ computations to determine the two closest components. In the best case, the newly generated solution is utilized to construct a new component and no learning is required. In contrast,

batch learning, e.g., $k$-means clustering, requires $O(T K N n)$ computations. Here, $T$ is the number of iterations. If $K \leqslant N$, then the computational cost of the proposed incremental-learning mechanism is less than $1 / T$ times that for the batch $k$-means.

Next, we consider the time complexity of the SeLupo operator. First, the fast sorting requires $O\left(m N^{2}\right)$ computations. Second, there are two possible strategies for removing a solution, either by determining the number of solutions or by computing the HV. In the first strategy, the worst-case time complexity is $O\left(m N^{2}\right)$. The computational cost of the HV metric is exponential in $m$ in the worst case, and the run time is $O\left(N^{m}\right)$ in our implementation. Third, merging the two closest components requires $O\left(n N^{3}\right)$ computations at the beginning of the evolutionary process, whereas it requires $O\left(n N K_{n m}^{2}\right)$ computations to find the two closest clusters in almost all generations. In summary, the worst-case time complexity of ILME at each generation is $O\left(N^{m}+K^{2} N n+m N^{2}\right)$, whereas the run time for the best case is $O\left(m N^{2}\right)$.

# 4. Numerical experiments 

In this section, we describe the experimental design used to verify the performance of ILME on test instances (effectiveness and efficiency). We used six classical or newly developed MOEAs for comparison on three groups of 22 test instances with complicated characteristics. They are compared with performance metrics. Then, the parameter settings of the chosen algorithms are given. Finally, the experimental results are presented.

### 4.1. MOEAs for comparison and test instances

Six classical or newly developed MOEAs were chosen as competitive candidates to investigate empirically the performance of ILME. They span the major categories of MOEA in current efforts: (1) a Pareto dominance-based MOEA, NSGA-II [16], (2) a metric-based MOEA, SMS-EMOA [19], (3) a regularity model-based MOEDA, RM-MEDA [3], and (4) three state-of-the-art learning model-based MOEAs: SMEA [11], MOEA/D-LTD [2], and MDESL [39]. Of these algorithms, SMEA learns a SOM to establish a neighborhood to guide solution creation. MOEA/D-LTD has an analytical model based on a Gaussian process that adaptively sets the decomposition method by learning the characteristics of the estimated PF. MDESL applies $k$-means clustering to extract knowledge about the neighborhood relationship in the decision space for mating restriction.

The numerical experiments focus on continuous MOPs with complicated PF shapes. A total of 22 test instances were used to compare ILME with the other six MOEAs: the GLT test suites [41], the tri-objective test instances WFG1-WFG9 [42], and problems RE1-RE7 [43]. These test problems have various characteristics, such as the PF being convex, concave, mixed, disconnected, or degenerate, and the PS having multimodal, biased, deceptive, or nonlinear variable linkage. These pose a significant challenge to MOEA.

### 4.2. Performance metrics

Analyzing the performance of a MOEA essentially boils down to evaluating the approximate front obtained within some computational budget. The performance metrics are scalar quantities that reflect the quality of the scrutinized solution set with respect to some measure.

The averaged Hausdorff distance $\left(\Delta_{p}\right)[21]$ comprises the generational distance and the inverted generational distance. It is particularly useful for evaluating stochastic search algorithms. Let $\mathbf{X}=\left(\mathbf{x}_{1}, \mathbf{x}_{2}, \ldots, \mathbf{x}_{m}\right)$ and $\mathbf{Y}=\left(\mathbf{y}_{1}, \mathbf{y}_{2}, \ldots, \mathbf{y}_{m}\right)$ be finite and non-empty sets. Then, their averaged Hausdorff distance is defined as

$$
\Delta_{p}(\mathbf{X}, \mathbf{Y})=\max \left(\mathrm{GD}_{p}(\mathbf{X}, \mathbf{Y}), \mathrm{IGD}_{p}(\mathbf{X}, \mathbf{Y})\right)
$$

where

$$
\begin{aligned}
\mathrm{GD}_{p}(\mathbf{X}, \mathbf{Y}) & =\left(\frac{1}{M} \sum_{i=1}^{N} \operatorname{dist}_{p}\left(\mathbf{x}_{i}, \mathbf{Y}\right)\right)^{1 / p} \\
\mathrm{IGD}_{p}(\mathbf{X}, \mathbf{Y}) & =\left(\frac{1}{M} \sum_{i=1}^{M} \operatorname{dist}_{p}\left(\mathbf{y}_{i}, \mathbf{X}\right)\right)^{1 / p}
\end{aligned}
$$

and $\operatorname{dist}_{p}\left(\mathbf{x}_{i}, \mathbf{Y}\right)$ is the minimal distance from $\mathbf{x}_{i} \in \mathbf{X}$ to $\mathbf{Y}$ :

$$
\operatorname{dist}_{p}\left(\mathbf{x}_{i}, \mathbf{Y}\right)=\inf _{y \in \mathbf{Y}}\left\|\mathbf{x}_{i}-y\right\|_{p}
$$

In this paper, we choose $p=2$. Let $\mathscr{S}$ be a set of uniformly sampled points in the true PF, and $\mathscr{P}$ be a set of nondominated solutions obtained by an MOEA. We compute $\Delta_{2}\left(\mathscr{S}, \mathscr{P}\right)$ to assess its performance. The smaller $\Delta_{2}$ is, the better $\mathscr{P}$ is.

The Hypervolume (HV) metric [44], [45] measures the volume covered by nondominated solutions. It is generally the region bounded by all points in the approximate front $\mathscr{P}$ with respect to the reference point $\mathbf{r}^{\prime}$. Mathematically, it is defined as:

$$
\mathrm{HV}\left(\mathscr{P}, \mathbf{r}^{-}\right)=\operatorname{VOL}\left(\bigcup_{\mathbf{x} \in \mathscr{P}}\left[f_{1}(\mathbf{x}), \mathbf{r}_{1}\right] \times \ldots \times\left[f_{m}(\mathbf{x}), \mathbf{r}_{m}\right]\right)
$$

where $\mathbf{r}^{-}=\left(r_{1}, \ldots, r_{m}\right)$ is a reference point, which must be dominated by any point in the $\mathrm{PF}_{i}$ and $\operatorname{VOL}(\cdot)$ is the Lebesgue measure. A larger HV value is desirable, as it reflects that the generated approximate front is close to the PF.

# 4.3. Parameter settings 

Different algorithmic descriptions and software implementations can lead to statistically significant differences in the performance of the MOEAs [46]. In order to ensure that different algorithms can be compared in a fair environment, all algorithms are implemented in PlatEMO [47], and the parameters for the algorithms compared were set to the recommended values as reported in their original publications. The DE operator and polynomial mutation [48] were adopted for offspring generation in NSGA-II and SMS-EMOA as suggested in [38]. The reference points were predefined as: $\mathbf{r}=(2,2)^{\top}$ for GLT1 and GLT3, $\mathbf{r}=(2,11)^{\top}$ for GLT2, $\mathbf{r}=(2,3)^{\top}$ for GLT4, $\mathbf{r}=(2,2,2)^{\top}$ for GLT5 and GLT6, $\mathbf{r}=(3,5,7)^{\top}$ for WFG1-WFG9. Note that the recommended settings of the RE problems are used in the numerical experiments. The detailed parameter settings for the different algorithms are listed in Table 1.

### 4.4. Experimental results

In the numerical experiments, each algorithm was run independently 31 times on each test instance. To quantify intuitively the performance of each algorithm, the mean and standard deviation ( $s d$ ) were calculated for each metric. These are listed in the relevant results table (Tables 2-4). The algorithms were ranked for each test instance in ascending (descending) order of $\Delta_{\mathrm{p}}(\mathrm{HV})$. The ranks are shown in square brackets in the tables. The standard deviations are given as subscripts. The Wilcoxon rank-sum (Mann-Whitney) test based on a $5 \%$ significance level was conducted with the mean values of each metric to illustrate the statistical differences. The labels $\uparrow, \S$, and $\approx$ in the tables denote whether ILME is superior, inferior, or similar to that of the algorithm it is compared to, respectively, in terms of the Wilcoxon rank-sum test. Further, the mean ranking, which is a comprehensive indicator for evaluating the performance of an algorithm, was also calculated. The performance of ILME is compared with the other algorithms on the GLT test suites in terms of convergence quality and convergence speed (Fig. 4). The results are visualized in Figs. 5 and 6.

Table 1
Parameter setting of all the compared algorithms.
Table 2
Mean and of of $\Delta_{2}$ metric after 31 independent runs of seven algorithms on the 22 test instances.
Table 3
Mean and sd of HV metric after 31 independent runs of seven algorithms on the 22 test instances.
Table 4
Mean and sd of run times of seven algorithms over 31 independent runs on the 22 test instances.
![img-3.jpeg](img-3.jpeg)

![img-4.jpeg](img-4.jpeg)

Fig. 4. Evolution of the mean and $s d$ of $\Delta_{2}$ obtained by six algorithms over 31 independent runs on the GLT test suites.

Table 2 shows the statistics for the $\Delta_{2}$ metric for the seven algorithms. As can be seen from the table, ILME has significantly better $\Delta_{2}$ values than NSGA-II, SMS-EMOA, RM-MEDA, SMEA, MDSEL, or MOEA/D-LTD for 17, 17, 17, 11, 16, and 21 out of the 22 test instances, respectively. In terms of the overall mean rankings, ILME is best, followed by SMEA, MDSEL, RM-MEDA, SMS-EMOA, MOEA/D-LTD, and NSGA-II. ILME was remarkably better than the other algorithms on the GLT and WFG test suites, except for WFG1 and WFG5, on which ILME had average performance. For the RE problems, ILME was slightly inferior to MDSEL on the RE3-3-1 and RE3-3-1 problems. In summary, ILME is superior to the other algorithms on the GLT and WFG test suites.

![img-5.jpeg](img-5.jpeg)

Fig. 5. Overall final populations obtained by SMEA and ILME on the GLT test suites with 31 independent runs.

Table 3 lists the experimental results for the HV values. It shows that ILME was significantly better than NSGA-II, SMSEMOA, RM-MEDA, SMEA, MDSEL, and MOEA/D-LTD for 17, 19, 17, 14, 15, and 21 out of the 22 test instances, respectively. ILME was in first place, followed by MDSEL, SMEA, RM-MEDA, SMS-EMOA, MOEA/D-LTD, and NSGA-II, in terms of the overall mean rankings. ILME was significantly superior on the GLT and WFG test suites, except for WFG1 and WFG5. For the RE problems, ILME was best for $4,5,4,4,2$, and 7 of 7 tests, worse for $2,1,1,3,7$, and 0 tests, and similar for $1,1,2,0,1$, and 0 tests, respectively, than NSGA-II, SMS-EMOA, RM-MEDA, SMEA, MDSEL, and MOEA/D-Ltd. ILME works particularly well on the GLT and WFG test suites, on average, in terms of HV.

Table 4 summarizes the run times of the seven algorithms on the 22 test instances averaged over 31 independent runs. As can be seen from the table, NSGA-II consumes the least time, whereas the run times increase in order for RM-MEDA, ILME, MDSEL, SMEA, SMS-EMOA, and MOEA/D-Ltd. The run time for NSGA-II was always significantly shorter than those of the other algorithms, simply because NSGA-II has a much lower time complexity, especially in the best case. Even the worstcase time complexity of NSGA-II is equal to or less than that of the other algorithms in their best cases. On the other hand, though the complexity of ILME is higher than that of SMEA, MDSEL, and MOEA/D-LTD in the worst case, ILME almost always spends less time than these three algorithms, especially for the three-objective problems (GLT5 and GLT6). This implies that the learning mechanism of ILME is more effective than those for the other learning-based algorithms.

![img-6.jpeg](img-6.jpeg)

Fig. 6. Representative final populations obtained by SMEA and ILME on the GLT test suites with 31 independent runs.

To investigate the convergence speed, Fig. 4 shows the mean and $s d$ of $\Delta_{2}$ versus the number of evolutionary generations for the seven algorithms for 31 independent runs of the GLT test suites. As can be seen from the figure, ILME has the lowest mean $\Delta_{2}$ values after 300 evolutionary generations for GLT1 and GLT3-GLT5, which confirms that ILME has the overall fastest convergence of the algorithms for the GLT test suites. More specifically, the search efficiency of ILME is superior to that of all the other algorithms on GLT3, GLT5, and GLT6 throughout the evolutionary process. ILME has an average convergence speed early in the evolutionary process for GLT1 and GLT4, when it is particularly inferior to MDSEL and MOEA/D-Ltd. However, ILME converges steadily, whereas the convergence of MDSEL and MOEA/D-LTD slows down. In addition, the search efficiency of ILME is similar to that of SMEA and MDSEL on GLT2, whereas the search efficiency of ILME is close to SMS-EMOA on GLT5.

To demonstrate the superiority of ILME further, we visualize the data for ILME and SMEA, which are the best two algorithms in terms of the mean ranking in Table 2. The data are for 31 independent runs on the GLT1-GLT6 test instances. The overall final populations are illustrated in Fig. 5, whereas Fig. 6 shows representative final populations with median $\Delta_{2}$ values. As can be seen from Fig. 5, the final populations of ILME have converged to the PFs and there is a uniform distribution on the PFs for each test instance. In contrast, SMEA either did not converge to the PFs or the distribution is rather non-uniform. For GLT5 and GLT6, the performance of ILME was obviously superior to SMEA, and the performance of SMEA was inferior to

Table 5
Mean and sd of $\Delta_{2}$ and HV metric after 31 independent runs of four algorithms on the GLT test suites.

![img-7.jpeg](img-7.jpeg)

Fig. 7. Mean $\Delta_{2}$ metric values with 31 runs versus of $K_{\max }$ in ILME for GLT test suites.

ILME for the remaining test instances. Moreover, the representative final populations obtained by the two algorithms are good approximations of the PFs for each instance, although some segments for GLT3 and GLT4 are missing for SMEA. The objective points yielded by ILME in the representative final populations are uniformly placed across the PFs on GLT1GLT6, whereas SMEA failed to provide a uniform distribution of points on the PFs for GLT5 and GLT6. In summary, the approximate fronts achieved by ILME on the GLT test suites have excellent convergence and outstanding diversity.

## 5. Further discussion

### 5.1. Effectiveness of the proposed sampling strategy

SCSS and DE were hybridized in ILME to produce new offspring. To validate the effectiveness of the proposed sampling strategy, three versions of the algorithm (ILME-SCSS, ILME-RSS, and ILME-DE) were compared with ILME. For ILME-SCSS (ILME-RSS and ILME-DE), all the components and settings were the same as for ILME, except that SCSS (RSS and DE) was used to generate solutions. The $\Delta_{2}$ and HV values of the final objective populations obtained by ILME-SCSS, ILME-RSS, ILME-DE, and ILME on the GLT test suites are summarized in Table 5. As can be seen, ILME has 11 out of 12 the best metric values and the top mean rank, which shows that ILME is significantly better than the other versions. To be specific, ILME-SCSS performs better than ILME-RSS, which benefits from its powerful search capability for exploration. The experimental results show that the sampling strategy developed dramatically enhances the performance of ILME.

# 5.2. Sensitivity analysis on algorithmic parameters 

### 5.2.1. Parameter sensitivity analysis of $K_{\max }$

$K_{\max }$ is an important parameter in ILME. It is the maximum number of components in the learning model used to discover the manifold structure of the PS. To study the sensitivity of this parameter, ILME was run on the GLT test suites for $K_{\max } \in\{2,4,6,8,10\}$. As $K_{\max }$ increases, the model to learn the manifold structure of PS becomes more accurate. All the other parameters were the same as in Section 4.3. For each configuration, 31 independent runs were conducted for each instance.

As can be seen from Fig. 7a, the performance of ILME is very robust for different $K_{\max }$ values on the GLT2, GLT5, and GLT6 test instances. However, changes to $K_{\max }$ lead to relatively large performance differences for GLT1, GLT3, and GLT4. In particular, the performance of ILME is average when $K_{\max }$ is too large or too small. In general, a medium $K_{\max }$ value in ILME could result in excellent experimental results with the GLT test suite.

### 5.2.2. Parameter sensitivity analysis of $\varepsilon$

In ILME, the exploitation probability $\varepsilon$ balances the effectiveness of exploitation and exploration. SCSS is used for exploitation with a probability $\varepsilon$, otherwise the DE operator is applied for exploration. ILME was run on the GLT test suites for $\varepsilon \in\{0.2,0.5,0.7,1\}$. As $\varepsilon$ increases, the solution generation method becomes more inclined to use SCSS instead of the DE operator. All the other parameters were the same as in Section 4.3. For each configuration, 31 independent runs were conducted on each instance.

As shown in Fig. 7b, different values of $\varepsilon$ have different effects on the performance of ILME for the GLT1-GLT6 test instances. Overall, the performance of ILME is not sensitive to the exploitation probability $\varepsilon$. Remarkably, ILME performs better with larger $\varepsilon$ values. Its convergence efficiency for the GLT test suites is best when $\varepsilon=0.7$. Note, though, that the optimal value of $\varepsilon$ depends on the problem.

### 5.2.3. Parameter sensitivity analysis of CR and $F$

In ILME, the crossover constant CR controls the effect of the parent on the offspring solutions. The higher CR is, the less effect it has. The differentiation constant $F$ scales the influence of the set of pairs of solutions selected to calculate the mutation value.

We investigated how ILME is influenced by different combinations of the two parameters for GLT1-GLT4, since ILME is not sensitive to the values of these parameters on GLT5 and GLT6, according to our numerical experiments. We tested 16 combinations with four values of $\mathrm{CR} \in\{0.2,0.5,0.7,1\}$ and four values of $F \in\{0.2,0.5,0.7,1\}$. All the other parameters were the same as in Section 4.3. For each configuration, 31 independent runs were conducted on each instance.

Fig. 8 shows the mean $\Delta_{2}$ values for different combination of $C R$ and $F$ on the selected test instances. ILME performed best when both CR and $F$ were large (such as $\mathrm{CR}=0.5,0.7$, or 1 and $F=0.5,0.7$, or 1 ). There were slight fluctuations in performance for the GLT1 and GLT4 test instances. These results demonstrate that large values of CR and $F$ are better. The combination of $\mathrm{CR}=1$ and $F=0.7$ is good for the majority of test instances.
![img-8.jpeg](img-8.jpeg)

Fig. 8. Mean $\Delta_{2}$ metric values with 31 runs versus of $C R$ and $F$ in ILME for GLT1-GLT4 test suites.

# 6. Conclusions 

In this paper, an incremental-learning model-based multiobjective estimation of distribution algorithm, termed ILME, has been proposed for solving MOPs. The incremental-learning model helps to reduce the computational cost of learning knowledge from the properties of the PS. In ILME, each new solution generated during the evolution becomes a datum in the evolving data stream, which is fed incrementally into the learning model to capture adaptively the structure of the PS. The parameters of the model are updated continually as newly generated data are collected. Each datum is learned only once for the model, regardless of whether it has been preserved or deleted. Moreover, a sampling strategy based on the learned model has been designed to balance the exploration/exploitation dilemma in evolutionary searches.

Numerical experiments have been performed to compare the performance of ILME with six representative MOEAs (NSGAII, SMS-EMOA, RM-MEDA, SMEA, MDSEL, and MOEA/D-LTD) for 22 test instances with complex PF or complicated PS structures. This systematic study has demonstrated that ILME outperforms, or is competitive with, the other algorithms in terms of convergence and diversity, as measured by $\Delta_{2}$ and HV. ILME has an average performance on RE problems. Moreover, the effectiveness of the proposed sampling strategy and the sensitivity of the algorithmic parameters have been experimentally investigated.

Future work might involve the implementation of better strategies to reduce the computational costs of MOEA. A potentially important issue in future research is the development of more advanced incremental-learning mechanisms, since the combination of current learning mechanisms and the evolutionary search is inadequate. Moreover, in future work, we will pay more attention to real-world problems [43] and many-objective optimization.

## CRediT authorship contribution statement

Tingrui Liu: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data curation, Writing - original draft, Visualization. Xin Li: Writing - review \& editing, Supervision. Liguo Tan: Project administration, Funding acquisition. Shenmin Song: Project administration, Funding acquisition.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

The authors would like to express sincere appreciation to constructive and valuable comments from anonymous reviewers. This study was funded by the Science Fund for Excellent Young Scholars of Heilongjiang Province (Grant No.: YQ2020F007), National Natural Science Foundation of China (Grant No.: 6191101340), the Defense Industrial Technology Development Program.
