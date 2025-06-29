# Interval-based ranking in noisy evolutionary multi-objective optimization 

Hossein Karshenas $\cdot$ Concha Bielza $\cdot$ Pedro Larrañaga

Received: 9 May 2013
(c) Springer Science+Business Media New York 2014


#### Abstract

As one of the most competitive approaches to multi-objective optimization, evolutionary algorithms have been shown to obtain very good results for many realworld multi-objective problems. One of the issues that can affect the performance of these algorithms is the uncertainty in the quality of the solutions which is usually represented with the noise in the objective values. Therefore, handling noisy objectives in evolutionary multi-objective optimization algorithms becomes very important and is gaining more attention in recent years. In this paper we present $\alpha$-degree Pareto dominance relation for ordering the solutions in multi-objective optimization when the values of the objective functions are given as intervals. Based on this dominance relation, we propose an adaptation of the non-dominated sorting algorithm for ranking the solutions. This ranking method is then used in a standard multi-objective evolutionary algorithm and a recently proposed novel multi-objective estimation of distribution algorithm based on joint variable-objective probabilistic modeling, and applied to a set of multi-objective problems with different levels of independent noise. The experimental results show that the use of the proposed method for solution ranking allows to approximate Pareto sets which are considerably better than those obtained when using the dominance probability-based ranking method, which is one of the main methods for noise handling in multi-objective optimization.


[^0]
[^0]:    Electronic supplementary material The online version of this article (doi:10.1007/s10589-014-9717-1) contains supplementary material, which is available to authorized users.
    H. Karshenas ( $\boxtimes$ ) C. Bielza $\cdot$ P. Larrañaga

    Computational Intelligence Group, Facultad de Informática, Universidad Politécnica de Madrid, Campus de Montegancedo, 28660 Boadilla del Monte, Madrid, Spain
    e-mail: hosseinkarshenas@gmail.com

Keywords Noisy optimization $\cdot$ Interval analysis $\cdot$ Evolutionary algorithms $\cdot$ Multiobjective optimization $\cdot$ Joint probabilistic modeling $\cdot$ Estimation of distribution algorithm

# 1 Introduction 

Many of the real world optimization problems are often best characterized by more than one objective. When trying to solve these problems, several, possibly conflicting, criteria should be fulfilled simultaneously. Let $\mathcal{F}=\left\{f_{1}, \ldots, f_{m}\right\}$ be the set of objective functions for a problem, where each objective function is defined as $f_{j}: \mathbb{D} \mapsto \mathbb{R}$, and assume that all of the objectives should be minimized. $\mathbb{D}$ determines the set of feasible value-settings for the vector of input variables $\boldsymbol{X}=\left(X_{1}, \ldots, X_{n}\right)$ and sometimes it is referred to as the decision space. Then an unconstrained continuous multi-objective optimization problem (MOP) is defined as

$$
\min _{\boldsymbol{x} \in \mathbb{D} \subseteq \mathbb{R}^{n}} \boldsymbol{f}(\boldsymbol{x})=\left(f_{1}(\boldsymbol{x}), \ldots, f_{m}(\boldsymbol{x})\right)
$$

The objective functions of an MOP map the solutions in $\mathbb{D}$ to another space which is called the objective space of the problem.

In general, with more than one objective function, the optimum solution to the MOP in Eq. (1) is not unique anymore, even if the constituting objective functions are not multi-modal. The presence of conflicting objectives implies that trying to improve one of the objectives will result in worse values for some other. Thus, the goal of a multiobjective optimization algorithm is to search for solutions which result in an optimal trade-off between different objectives of the problem. One of the most frequently used approaches is to employ the notion of Pareto optimality [1] and the corresponding Pareto dominance relation [2].

Definition 1 (Pareto Dominance) Let $\boldsymbol{x}$ and $\boldsymbol{y}$ be two solutions of the MOP defined in Eq. (1) in the decision space $\mathbb{D}$. Then $\boldsymbol{x}$ Pareto dominates $\boldsymbol{y}$, denoted as $\boldsymbol{x} \prec \boldsymbol{y}$, if and only if:

1. $\forall f_{j} \in \mathcal{F} \quad f_{j}(\boldsymbol{x}) \leq f_{j}(\boldsymbol{y})$, and
2. $\exists f_{k} \in \mathcal{F} \quad f_{k}(\boldsymbol{x})<f_{k}(\boldsymbol{y})$.

Pareto dominance defines a partial order between the solutions, i.e. an irreflexive, antisymmetric and transitive relation. Using this relation, the solutions to an MOP can be ranked into a number of disjoint Pareto non-dominated sets (or Pareto sets for short) where every two solutions in the same set either have exactly equal objective values or are incomparable in terms of Pareto dominance. The corresponding projections of these Pareto sets onto the objective space are called Pareto non-dominated fronts (similarly Pareto fronts for short). The best Pareto set containing optimal trade-off solutions (no other solution in $\mathbb{D}$ dominates them) is called the Pareto optimal set, and its projection onto the objective space is called the Pareto optimal front. In general, the number of solutions in the Pareto optimal set can be exponentially large or even infinite in the case of continuous domains and thus multi-objective optimization algorithms try to obtain a good approximation of this set.

Because of the complexity of solving MOPs, a promising approach which is gaining an increasing interest is to use evolutionary algorithms (EAs), giving rise to evolutionary multi-objective optimization (EMO) algorithms [3-6], otherwise known as multi-objective EAs. Although these algorithms do not ensure the optimality of the solutions compared with some of the conventional mathematical optimization techniques, they have been successfully applied to many complex real-world MOPs. Beside their simple mechanism which motivates their wide-spread use in different applications, another advantage of these algorithms encouraging their use for multi-objective optimization is their population-based search allowing them to simultaneously explore several regions of the search space, finding a set of trade-off solutions in contrast to a single solution, in an individual run.

Estimation of distribution algorithms (EDAs) [7-10] are a relatively recent class of EAs developed by using probabilistic modeling in the framework of EAs. They have proven to be promising optimization algorithms for many difficult problems with high computational complexity. These algorithms explore the search space by building a probabilistic model from a set of selected candidate solutions. This probabilistic model is then used to sample new candidate solutions in the search space. As the result, these algorithms will provide a model expressing the regularities of the problem structure, as well as the final solutions. EDAs have also been used for multi-objective optimization [11-13], where the model building in EDAs is combined with a multiobjective solution ranking and selection mechanism to solve MOPs.

A feature of many real-world problems is the existence of noise, which can appear as variable or environmental change, or/and as uncertainty in the objective values. Many of the methods that are proposed for solution ranking in EMO algorithms are based on the Pareto dominance relation. When EMO algorithms based on Pareto dominance relation are used for solving these problems, the noise in objective values can mislead the algorithm by selecting inferior solutions that are considered good because of noise, and discarding good solutions that are necessary for directing the search to promising areas. One of the ways to deal with noisy objectives is to assume each objective returns an interval of values for a solution. This interval can be obtained by considering the range of error or amount of noise in the system, or from a set of values obtained from multiple reevaluations of a solution in different conditions. Considering an interval of values instead of a single value allows the EMO algorithm to take into account the extent of noise in the objectives when selecting solutions for recombination.

In this paper we introduce a new solution ranking, called $\alpha$-degree Pareto dominance, for EMO algorithms applied to noisy problems when independently computed objective functions return intervals. This new relation for ranking the solutions allows the intervals to overlap each other, and determines the dominance among solutions based on the extent to which their corresponding intervals are better than those of other solutions. The method can also be extended to the case where only some of the objective functions of the MOP are noisy. This solution ranking method is then integrated into a standard multi-objective EA and MBN-EDA [14], a multi-objective EDA based on joint variable-objective probabilistic modeling, for finding the solutions of noisy MOPs.

The rest of paper is organized as follows. In the next section we briefly review some of the methods proposed in the literature for noise handling in EMO algo-

rithms. Section 3 introduces the $\alpha$-degree Pareto dominance relation, discusses some of its properties, and proposes a solution ranking method based on this relation. In Sect. 4, MBN-EDA and its joint probabilistic modeling of variables and objectives are described. The details of the experiments and their results are presented and discussed in Sect. 5. Finally, Sect. 6 concludes the paper and gives some lines of future work.

# 2 A review on EMO with noise 

The topic of EMO under uncertainty and noise has gained a lot of attention in the past few years, and many studies and methods are reported in the literature. In general, as explained by Jin and Branke [15], three different types of noise handling can be identified in EAs. First, the population-based search in these algorithms, by itself, implicitly deals with certain levels of noise in objective values. The average quality of a population or subgroups of the population, presenting certain subspaces, is less susceptible to noise. Therefore, the larger the population is, the better the algorithm can overcome the noise in the quality of solutions for finding the optimal solutions. However, the existence of several objectives in a multi-objective scenario reduces the effectiveness of EAs in noise handling [16]. Second approach is to explicitly reevaluate each solution of the population several times to obtain a better estimation of its objective values. Although this approach greatly increases the computational cost of optimization, it is inevitable for some of the problems where the objective values are obtained as the result of simulations. A third approach is to consider the noise in objective values in the selection step of EAs. This is usually done by modifying the solution ranking method, assuming a level of uncertainty in the objective values.

As explained before, noise can exist in the values of the input variables, the outputs of the objective functions or even both. There are some works on EMO algorithms considering the former type of noise, i.e. noise in the input values, which is sometimes referred to as robust optimization and its aim is to find solutions with the highest stability in their objective values. Soares et al. [17] optimized the worst noisy objective values of the solutions in a min-max formulation using interval analysis. To decrease the amount of uncertainty in the intervals they propose to recursively divide the intervals into halves, resulting in a grid which is placed on the objective space and is used to compute the worst objective values of the solutions. The grid also serves as a niching method, penalizing the solutions that are very close in the objective space. The noise is introduced in the input variables using an uncertainty vector which is incorporated in the definition of the objective functions. Goh et al. [18] offered a classification of the noisy MOPs depending on the effect of noise on the Pareto front, Pareto set and landscape of the problem. Based on this classification, they proposed some guidelines for designing challenging MOPs for robust optimization, and introduced a Gaussian landscape generator for this purpose using a number of basis functions.

Most of the algorithms proposed for EMO in noisy environments consider the second type of noise, i.e. noise in the objective values, since this type of noise is harder to deal with. In this type of MOPs it is usually assumed that the objective values are distorted by an additive noise value. Almost all EMO algorithms reviewed

in this section consider a Gaussian noise model for the objective values of the tested MOPs, unless otherwise mentioned.

One of the earliest and well-known approaches to deal with noisy objectives when comparing two solutions in multi-objective optimization is to use probabilistic dominance, considering the probability that one solution dominates another [19,20]. This approach has been successfully used for optimization in some of the real world problems like designing the shape of acoustic noise attenuation barriers with several receiver points [21]. Since this method is considered as a main reference in many later works on noisy objectives, we explain it here in more detail.

Definition 2 (Dominance Probability [19,20]) Let $\boldsymbol{U}=\boldsymbol{f}(\boldsymbol{x})$ and $\boldsymbol{V}=\boldsymbol{f}(\boldsymbol{y})$ be two vectors of random variables representing the objective values returned for two solutions $\boldsymbol{x}$ and $\boldsymbol{y}$ of a noisy MOP in decision space $\mathbb{D}$. Then the probability that $\boldsymbol{x}$ dominates $\boldsymbol{y}$ is given by:

$$
P(\boldsymbol{x} \prec \boldsymbol{y})=\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} \rho_{\boldsymbol{U}}(\boldsymbol{t})\left(1-\Psi_{\boldsymbol{V}}(\boldsymbol{t})\right) d \boldsymbol{t}
$$

where $\rho_{\boldsymbol{U}}(\cdot)$ denotes the joint probability distribution for the output of objective functions given solution $\boldsymbol{x}$, and $\Psi_{\boldsymbol{V}}(\cdot)$ is the cumulative probability distribution for the output of objective functions given solution $\boldsymbol{y}$.

Based on the probability of dominance, ranking strategies like the mean dominance probability [20] is used to order the solutions with noisy objective values. [19] also tested this approach when the noise is introduced to the input values, showing the ability of this method for handling noise in both input variables and output objective functions. Bui et al. [22] adopted probabilistic dominance in NSGA-II [23] and compared it with a version of this algorithm which is based only on reevaluation of objectives. They also proposed a fitness inheritance method to reduce the complexity of reevaluating the objectives. In a separate work [24], they performed a comparative study of the noise handling capability of the original versions of NSGA-II and SPEA2 [25] in the presence of different noise levels, using several performance measures. [26] proposed a Bayesian method for obtaining an estimation of the Gaussian noise variance when computing the probability of dominance between two solutions. They considered different scenarios like unknown, constant and variable noise for the objective values.

Many of the EMO algorithms proposed for noise handling try to extend the existing solution ranking and selection methods by considering noise in the values of the objectives. Büche et al. [27] proposed a noise-tolerant EA using the Pareto strengthsbased solution ranking method [28] assigning a lifetime (number of generations) to the solutions in the archive depending on their strengths. This lifetime is used to determine which solutions are to be reevaluated or to be used for updating the archive in order to limit the influence of noisy objective values and outliers. They claim that elitism does not necessarily result in faster convergence when noise is present in multi-objective optimization. The proposed algorithm is applied to find an optimal flow of fuel in the burner of a gas turbines.

Babbar et al. [29] modified NSGA-II to include neighbors of the non-dominated solutions in the first Pareto front. Neighboring solutions are determined using the mean

and variance of the objective values for each solution, estimated from the reevaluation of the solutions. Solutions that are reevaluated less than a predetermined number of times during the evolution are considered as outliers and removed from the final Pareto set.

Goh and Tan [30] proposed three techniques for noise handling in an EMO algorithm which uses a two-part, discrete-continuous, representation for the solutions. The first technique consists of incorporating the direction of population movement along evolution into the generation of new solutions. The second technique is stretching or shrinking the search domain of each variable depending on the behavior of the algorithm in the current phase of evolution. The third technique is to assume objective values are given as fuzzy numbers and then use two newly proposed dominance relations, called necessity and necessity-possibility, to update the archive of non-dominated solutions maintained by the algorithm.

Eskandari and Geiger [31] considered the expected values of the objective functions and proposed the stochastic dominance relation for ranking the solutions. In the selection process, the solutions are divided into two sets depending on whether they are stochastically dominated. The set of stochastically dominated solutions are further ordered by considering the expected strength of each solution depending on both how many solutions it dominates and by how many solutions it is dominated. To detect the algorithm convergence in noisy environments they proposed to monitor the rate of hypervolume indicator growth.

Bui et al. [32] proposed the use of adaptive non-overlapping hyper-spheres which are locally moved in the search space to reduce the effect of noise. The motivation is that the average objective values of the solutions in a neighborhood of the search space provide a better approximation of the direction of movement during evolution. A particle swarm optimization based algorithm is used to update the center and radius of the hyper-spheres in the search space. The algorithm also deploys an archive of solutions and its corresponding hyper-sphere to represent the global behavior of the population.

Syberfeldt et al. [33] proposed a method to increase the efficiency of solution reevaluations. When comparing two solutions in the non-dominated sorting algorithm [23], if the confidence in the differences between their objective values are less than a specific level, then one of them is reevaluated more to increase the level of confidence. Different Pareto sets are assigned different values of minimum confidence level, and since during evolution the rank of solutions in the population changes, implicit dynamism is introduced during evolution as each solution is reevaluated. The proposed method is also applied to two real-world problems related to optimization in engine manufacturing lines. Instead of discarding old evaluations of a solution in a noisy problem, Park and Ryu [34] proposed an accumulating approach which combines old evaluations with the new reevaluation of a solution to improve the expected value estimation of objective functions.

Another approach taken by some of the proposed methods is to use decision maker (DM) provided information for EMO in the presence of noise. Mehnen et al. [35] used desirability functions to include both the preferences of DM and to reduce the effect of noise. Instead of performing the search in the objective space, they optimize the expected value of the desirability functions computed from noisy objectives. The

final Pareto front is obtained by either applying the inverse desirability functions on the approximated front or computing the objective values of the final Pareto set. The method is used to find the working parameters of an industrial cutting tool. Woźniak [36] proposed to use a number of reference points provided by DM, each accompanied with a weight vector showing the importance of the objectives, to select fitter solutions in the search process. To maintain the population diversity only one of the solutions in each neighborhood, defined by a predefined neighborhood radius, is selected. The method is then applied for the design of a motor speed controller.

In addition to the noise in objective values, Kaji et al. [37] studied the effect of noise in constraint functions of a constrained MOP, trying to reduce the number of infeasible solutions selected in the Pareto set. For this purpose they form a history of solutions and estimate the value of objective and constraint functions by a locally weighted ridge regression of second order. The weights are defined using a Gaussian kernel. A safety margin is also introduced to the constraint functions and dynamically adjusted depending on the variance of the estimated constraint values.

Basseur and Zitzler [38] proposed an indicator-based EMO algorithm for noisy environments, considering the presence of noise in both the objective functions and the input variables. They proposed methods to estimate the expected value of the epsilon indicator for ranking the solutions. A uniform noise is assumed for both inputs and outputs. Boonma and Suzuki [39] considered different types of distributions like Gaussian, uniform and Poisson for the noise model. Assuming that the quality of each solution is represented with several reevaluations of its objectives, they used a support vector machine to determine the confidence level in these objective values. The coverage metric is used to determine the dominance between two solutions after their values are classified as statistically reliable. The confidence level for accepting the objective values of the solutions is dynamically adjusted during evolution according to the disorder among objective values, which is computed with an entropy-based function.

Table 1 summarizes the reviewed algorithms.

# $3 \alpha$-Degree Pareto dominance 

Most of the methods reviewed in the previous section for handling the noise when selecting a subset of solutions, only consider singular objective values. Although these singular values maybe obtained as the result of averaging over several reevaluations, they still do not directly take into account the extent of the noise in the values. We also saw that some of the proposed methods optimize the expected values of the objectives and consider the variance of the objective values, implicitly assuming a type of confidence interval for the objective values. A closely related approach is the possibilistic dominance method [30], where objective values are considered to be fuzzy numbers. In this section we propose a method for directly comparing any kind of intervals, not necessarily confidence intervals, which also takes into account interval widths (representing the amount of noise). Moreover, the proposed method can deal with MOPs consisting of both singular and interval objectives.

Table 1 Summary of the EMO methods for noisy environments

|  | Method | Noise type | Noise location |
| :--: | :--: | :--: | :--: |
| Teich [20] | Probabilistic Dominance | Uniform | Output |
| Hughes [19] | Probabilistic Dominance | Gaussian | Input, Output |
| Büche et al. [27] | Lifetime-Based Archiving | Gaussian | Output |
| Babbar et al. [29] | Objective Space Neighborhood | Gaussian | Output |
| Bui et al. [22] | Fitness Inheritance in Reevaluations | Gaussian | Output |
| Fieldsend and Everson [26] | Noise Variance Estimation | Gaussian | Output |
| Basseur and Zitzler [38] | Indicator Value Estimation | Uniform | Input, Output |
| Goh and Tan [30] | Necessity and Necessity-Possibility Dominance | Gaussian | Output |
| Mehnen et al. [35] | Desirability Functions Optimization | Gaussian | Output |
| Woźniak [36] | Weighted Reference Points | Gaussian | Output |
| Boonma and Suzuki [39] | Confidence-Based Solution Comparison | Gaussian, Uniform, Poisson | Output |
| Bui et al. [32] | Search Space Neighborhood | Gaussian | Output |
| Eskandari and Geiger [31] | Stochastic Dominance | Gaussian | Output |
| Kaji et al. [37] | Value Estimation with Locally Weighted Ridge Regression | Gaussian | Output, <br> Constraints |
| Soares et al. [17] | Worst-Case Analysis | Gaussian | Output |
| Syberfeldt et al. [33] | Confidence-Based Reevaluations | Gaussian | Output |
| Park and Ryu [34] | Reevaluation Accumulation | Gaussian | Output |

One way to deal with the noise in an MOP when the objective values are represented with intervals is to extend the Pareto dominance definition (Definition 1). In the following definitions we assume that the set of objectives $\mathcal{F}$ is partitioned into two disjoint subsets of objectives with singular values $\mathcal{F}_{S}$, and noisy objectives with interval values $\mathcal{F}_{I}$, such that $\mathcal{F}_{S} \cup \mathcal{F}_{I}=\mathcal{F}$ and $\mathcal{F}_{S} \cap \mathcal{F}_{I}=\emptyset$.

Definition 3 (Extended Pareto Dominance) Let $\left\lfloor f_{j}(\boldsymbol{x})\right\rfloor$ and $\left\lceil f_{j}(\boldsymbol{x})\right\rceil$ respectively represent the lower and upper bounds of the interval value returned for solution $\boldsymbol{x} \in \mathbb{D}$, by the noisy objective function $f_{j} \in \mathcal{F}_{I}$, i.e. $U_{j}$ lies in the interval $\left[\left\lfloor f_{j}(\boldsymbol{x})\right\rfloor,\left\lceil f_{j}(\boldsymbol{x})\right\rceil\right]$. Then, solution $\boldsymbol{x}$ is said to strictly dominate solution $\boldsymbol{y}$, denoted as $\boldsymbol{x} \prec_{e} \boldsymbol{y}$, if and only if:

1. $\forall f_{j} \in \mathcal{F}_{S} \quad f_{j}(\boldsymbol{x}) \leq f_{j}(\boldsymbol{y})$, and
2. $\forall f_{j} \in \mathcal{F}_{I} \quad\left\lceil f_{j}(\boldsymbol{x})\right\rceil \leq\left\lfloor f_{j}(\boldsymbol{y})\right\rfloor$, and
3. $\left(\exists f_{k} \in \mathcal{F}_{S} \quad f_{k}(\boldsymbol{x})<f_{k}(\boldsymbol{y}) \quad\right.$ or $\quad \exists f_{k} \in \mathcal{F}_{I} \quad\left\lceil f_{k}(\boldsymbol{x})\right\rceil<\left\lfloor f_{k}(\boldsymbol{y})\right\rfloor$ ).

This definition treats interval values similar to the way it considers singular values and only allows a solution to dominate other solutions if its corresponding interval values, returned by noisy objective functions, are strictly better than those of other

solutions. In real-world noisy MOPs, such a requirement is hardly satisfied. A further extension is to relax this strict requirement and allow the intervals to have some degree of overlapping.

Definition 4 ( $\alpha$-Degree Pareto Dominance) Assume the same notations as those of Definition 3. Then, solution $\boldsymbol{x}$ is said to dominate another solution $\boldsymbol{y}$ with a degree $\alpha \in(0,1]$, denoted as $\boldsymbol{x} \prec_{\alpha} \boldsymbol{y}$, if and only if:

1. $\forall f_{j} \in \mathcal{F}_{S} \quad f_{j}(\boldsymbol{x}) \leq f_{j}(\boldsymbol{y})$, and
2. $\forall f_{j} \in \mathcal{F}_{I} \quad \operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y}) \geq \alpha$, and
3. $\left(\exists f_{k} \in \mathcal{F}_{S} \quad f_{k}(\boldsymbol{x})<f_{k}(\boldsymbol{y}) \quad \vee \quad \exists f_{k} \in \mathcal{F}_{I} \quad \operatorname{deg}_{k}(\boldsymbol{x}, \boldsymbol{y})>\alpha\right)$,
where $\operatorname{deg}_{j}(\cdot, \cdot)$ gives the degree that a solution dominates another with respect to the noisy objective function $f_{j} \in \mathcal{F}_{I}$

$$
\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})=\min \left\{1, \max \left\{0, \frac{\left\lfloor f_{j}(\boldsymbol{y})\right\rfloor-\left\lfloor f_{j}(\boldsymbol{x})\right\rfloor}{\left\lceil f_{j}(\boldsymbol{x})\right\rceil-\left\lfloor f_{j}(\boldsymbol{x})\right\rfloor}\right\}\right\}
$$

Intuitively, $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})$ computes the percentage of the interval obtained for solution $\boldsymbol{x}$ that is not overlapped by the interval obtained for solution $\boldsymbol{y}$ in objective $f_{j} \in \mathcal{F}_{I}\left(\right.$ i.e. $\left.1-\frac{\left\lceil f_{j}(\boldsymbol{x})\right\rceil-\left\lfloor f_{j}(\boldsymbol{y})\right\rfloor}{\left\lceil f_{j}(\boldsymbol{x})\right\rceil-\left\lfloor f_{j}(\boldsymbol{x})\right\rfloor}\right)$. Thus, only the segment of the interval obtained for solution $\boldsymbol{x}$ that is better than the best point in the interval obtained for solution $\boldsymbol{y}$ (i.e. its lower bound, when minimizing objectives) is taken into account. If $\alpha=1$, then Definition 4 is reduced to Definition 3. Definition 4 allows a solution to dominate other solutions when its corresponding interval values are partially better than those of other solutions.

Figure 1 shows some examples of possible placements of two intervals and the corresponding values of the $\operatorname{deg}_{j}(\cdot, \cdot)$ function. Figure 1a shows a situation where the interval for solution $\boldsymbol{x}$ is strictly better than the other solution, resulting in $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})=1$. Figure 1 b , c show cases when the two intervals partially overlap with $0<\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})<1$. Finally, Fig. 1d shows an example of the situation when intervals completely overlap, i.e. $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})=0$. With higher values of $\alpha$, a solution can only dominate other solutions if a major segment of its corresponding interval values are better than the best points of the interval values corresponding to other solutions. Thus, higher values of $\alpha$ place a stricter condition for accepting a solution as non-dominated.

# 3.1 Properties 

In this section we show some of the properties of the $\alpha$-Degree Pareto Dominance (Definition 4) which will allow us to use it for solution ordering.

Proposition $1 \alpha$-Degree Pareto dominance defines a partial relation, i.e. with irreflexivity, antisymmetry and transitivity properties, on the space of candidate solutions.

Proof Since no $\boldsymbol{x} \in \mathbb{D}$ exists that satisfies $\boldsymbol{x} \prec_{\alpha} \boldsymbol{x}$ for any $\alpha \in(0,1]$, the relation is irreflexive. To see the antisymmetry of the relation, assume $\boldsymbol{x} \prec_{\alpha} \boldsymbol{y}$. If $\exists f_{j} \in \mathcal{F}_{S}$

![img-0.jpeg](img-0.jpeg)

Fig. 1 Examples of interval values and the resulting degrees of dominance. a $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})=1$, b $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})=0.75, \mathbf{c} \operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})=0.5, \mathbf{d} \operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})=0$
such that $f_{j}(\boldsymbol{x})<f_{j}(\boldsymbol{y})$ then $\boldsymbol{y} \prec_{\alpha} \boldsymbol{x}$. If $\exists f_{j} \in \mathcal{F}_{I}$ such that $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})>\alpha$, then by definition of $\operatorname{deg}_{j}(\cdot, \cdot)$ in Eq. (3) if $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})>0$ then $\operatorname{deg}_{j}(\boldsymbol{y}, \boldsymbol{x})=0$ and therefore $\boldsymbol{y} \prec_{\alpha} \boldsymbol{x}$ for any $\alpha \in(0,1]$.

For transitivity, assume that $\boldsymbol{x} \prec_{\alpha} \boldsymbol{y}$ and $\boldsymbol{y} \prec_{\alpha} \boldsymbol{z}$. Then we have $\forall f_{j} \in \mathcal{F}_{S}, f_{j}(\boldsymbol{x}) \leq$ $f_{j}(\boldsymbol{y})$ and $f_{j}(\boldsymbol{y}) \leq f_{j}(\boldsymbol{z})$. Therefore, $f_{j}(\boldsymbol{x}) \leq f_{j}(\boldsymbol{z}), \forall f_{j} \in \mathcal{F}_{S}$. Similarly, we have $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{z}) \geq \alpha, \forall f_{j} \in \mathcal{F}_{I}$, because if $\forall f_{j} \in \mathcal{F}_{I}$ such that $\left\lfloor f_{j}(\boldsymbol{x})\right\rfloor<\left\lfloor f_{j}(\boldsymbol{y})\right\rfloor$ and $\left\lfloor f_{j}(\boldsymbol{y})\right\rfloor<\left\lfloor f_{j}(\boldsymbol{z})\right\rfloor$, then we have $\left\lfloor f_{j}(\boldsymbol{x})\right\rfloor<\left\lfloor f_{j}(\boldsymbol{z})\right\rfloor, \forall f_{j} \in \mathcal{F}_{I}$. Now, given either $\exists f_{j} \in \mathcal{F}_{S}$ such that $f_{j}(\boldsymbol{x})<f_{j}(\boldsymbol{y})$ or $\exists f_{j} \in \mathcal{F}_{I}$ such that $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})>\alpha$ (similarly $\exists f_{j} \in \mathcal{F}_{S}$ such that $f_{j}(\boldsymbol{y})<f_{j}(\boldsymbol{z})$ or $\exists f_{j} \in \mathcal{F}_{I}$ such that $\operatorname{deg}_{j}(\boldsymbol{y}, \boldsymbol{z})>\alpha$ ) we can respectively conclude either $\exists f_{j} \in \mathcal{F}_{S}$ such that $f_{j}(\boldsymbol{x})<f_{j}(\boldsymbol{z})$ or $\exists f_{j} \in \mathcal{F}_{I}$ such that $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{z})>\alpha$, which completes the proof of proposition.

The partial relation defined by $\alpha$-degree Pareto dominance allows to readily adopt the terms of $\alpha$-degree Pareto optimal solution, $\alpha$-degree Pareto optimal set, $\alpha$-degree Pareto optimal front and $\alpha$-degree Pareto non-dominated set for noisy MOPs, in the same way they are defined using the conventional Pareto dominance relation. The $\alpha$-degree Pareto dominance relation also has interesting properties when different confidence levels are considered for the objective values. To see this, lets assume that

the values returned by noisy objective functions for solution $\boldsymbol{x}$ are confidence intervals given in the form of

$$
\left(\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{x})\right)-\varepsilon_{\gamma}\left(f_{j}(\boldsymbol{x})\right), \hat{\mathbb{E}}\left(f_{j}(\boldsymbol{x})\right)+\varepsilon_{\gamma}\left(f_{j}(\boldsymbol{x})\right)\right)
$$

where $\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{x})\right)$ represents an estimation of the expected value of the $j$ th objective function for solution $\boldsymbol{x}$ and

$$
\varepsilon_{\gamma}\left(f_{j}(\boldsymbol{x})\right)=z_{\frac{1-\gamma}{2}} \hat{\sigma}\left(f_{j}(\boldsymbol{x})\right)
$$

is the half-width [31] of the confidence interval computed according to a specific confidence level $\gamma$. Here, $z_{(1-\gamma) / 2}$ denotes the value for which $\Phi\left(Z>z_{(1-\gamma) / 2}\right)=$ $\frac{1-\gamma}{2}$, where $\Phi(Z)$ is the cumulative standard Gaussian (or t-student) distribution. $\hat{\sigma}\left(f_{j}(\boldsymbol{x})\right)$ is the estimation for the standard deviation of mean objective value. With confidence intervals, the definition of $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})$ for a noisy objective $f_{j} \in \mathcal{F}_{I}$ can be rewritten as

$$
\begin{aligned}
& \operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})=\min \left\{1,\right. \\
& \left.\max \left\{0, \frac{\left(\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{y})\right)-\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{x})\right)\right)-\left(\varepsilon_{\gamma}\left(f_{j}(\boldsymbol{y})\right)-\varepsilon_{\gamma}\left(f_{j}(\boldsymbol{x})\right)\right)}{2 \varepsilon_{\gamma}\left(f_{j}(\boldsymbol{x})\right)}\right\}\right\}
\end{aligned}
$$

According to this definition, the degree that a solution outperforms another solution with respect to a noisy objective $f_{j} \in \mathcal{F}_{I}$ is determined by the differences in both expected values and half-widths. The following propositions show how the change in the confidence level $\gamma$ or dominance degree $\alpha$ affects the $\alpha$-degree Pareto dominance relation.

Proposition 2 Any reduction in the confidence level of the interval values given by noisy objective functions in $\mathcal{F}_{I}$ does not affect $\boldsymbol{x} \prec_{\alpha} \boldsymbol{y}$, if for every objective function $f_{j} \in \mathcal{F}_{I}$ we have $\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{x})\right)<\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{y})\right)$.
Proof We only consider noisy objectives in $\mathcal{F}_{I}$ here because the change in confidence level does not affect singular values. Let $\boldsymbol{x} \prec_{\alpha}^{y} \boldsymbol{y}$ denote that solution $\boldsymbol{x}$ dominates solution $\boldsymbol{y}$ with a degree $\alpha$, when the confidence level in the interval value of all noisy objectives in $\mathcal{F}_{I}$ is at least $\gamma$.

Assuming $\boldsymbol{x} \prec_{\alpha}^{\gamma_{1}} \boldsymbol{y}$ implies that

$$
\begin{aligned}
& \forall f_{j} \in \mathcal{F}_{I}, \quad \frac{\left(\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{y})\right)-\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{x})\right)\right)-\left(\varepsilon_{\gamma_{1}}\left(f_{j}(\boldsymbol{y})\right)-\varepsilon_{\gamma_{1}}\left(f_{j}(\boldsymbol{x})\right)\right)}{2 \varepsilon_{\gamma_{1}}\left(f_{j}(\boldsymbol{x})\right)} \geq \alpha \\
& \quad \Rightarrow \frac{\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{y})\right)-\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{x})\right)}{2 z_{\frac{1-\gamma_{1}}{2}} \hat{\sigma}\left(f_{j}(\boldsymbol{x})\right)}-\frac{\hat{\sigma}\left(f_{j}(\boldsymbol{y})\right)-\hat{\sigma}\left(f_{j}(\boldsymbol{x})\right)}{2 \hat{\sigma}\left(f_{j}(\boldsymbol{x})\right)} \geq \alpha .
\end{aligned}
$$

Changing the confidence level does not influence the second quotient above. The numerator of the first quotient is positive because of the proposition assumption and, since $z_{\frac{1-\gamma_{1}}{2}}>z_{\frac{1-\gamma_{2}}{2}}, \forall \gamma_{2}<\gamma_{1}$, this quotient will become larger if confidence level decreases to $\gamma_{2}$. Therefore, for all $f_{j} \in \mathcal{F}_{I}$

$$
\begin{aligned}
& \frac{\left(\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{y})\right)-\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{x})\right)\right)-\left(\varepsilon_{\gamma_{2}}\left(f_{j}(\boldsymbol{y})\right)-\varepsilon_{\gamma_{2}}\left(f_{j}(\boldsymbol{x})\right)\right)}{2 \varepsilon_{\gamma_{2}}\left(f_{j}(\boldsymbol{x})\right)}> \\
& \frac{\left(\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{y})\right)-\hat{\mathbb{E}}\left(f_{j}(\boldsymbol{x})\right)\right)-\left(\varepsilon_{\gamma_{1}}\left(f_{j}(\boldsymbol{y})\right)-\varepsilon_{\gamma_{1}}\left(f_{j}(\boldsymbol{x})\right)\right)}{2 \varepsilon_{\gamma_{1}}\left(f_{j}(\boldsymbol{x})\right)} \geq \alpha
\end{aligned}
$$

which means $\boldsymbol{x} \prec_{\alpha}^{\gamma_{2}} \boldsymbol{y}$.
Now, let $\mathcal{P} \mathcal{S}_{\alpha}^{\gamma}$ denote the $\alpha$-degree Pareto optimal set imposed by $\alpha$-degree Pareto dominance relation $\prec_{\alpha}^{\gamma}$, when the confidence level in the interval values returned by the noisy objectives is at least $\gamma$.

Corollary 1 If $\gamma_{2}<\gamma_{1}$, then $\mathcal{P} \mathcal{S}_{\alpha}^{\gamma_{2}} \subset \mathcal{P} \mathcal{S}_{\alpha}^{\gamma_{1}}$.
Proof Assume that there exists a solution $\boldsymbol{y}$ such that $\boldsymbol{y} \in \mathcal{P} \mathcal{S}_{\alpha}^{\gamma_{2}}$ and $\boldsymbol{y} \notin \mathcal{P} \mathcal{S}_{\alpha}^{\gamma_{1}}$. This means that there exists a solution $\boldsymbol{x} \in \mathcal{P} \mathcal{S}_{\alpha}^{\gamma_{1}}$ such that $\boldsymbol{x} \prec_{\alpha}^{\gamma_{1}} \boldsymbol{y}$. By Proposition 2, we know that this implies $\boldsymbol{x} \prec_{\alpha}^{\gamma_{2}} \boldsymbol{y}$. But the last relation means that $\boldsymbol{y} \notin \mathcal{P} \mathcal{S}_{\alpha}^{\gamma_{2}}$ which contradicts the hypothesis.

Proposition 3 The $\alpha$-degree Pareto dominance relation between solutions is preserved when the dominance degree $\alpha$ is decreased.

Proof It is trivial since if $\alpha_{2}<\alpha_{1}$ then $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y}) \geq \alpha_{1}$ implies that $\operatorname{deg}_{j}(\boldsymbol{x}, \boldsymbol{y})>\alpha_{2}$, for any two solutions $\boldsymbol{x}, \boldsymbol{y}$ and every objective function $f_{j} \in \mathcal{F}_{I}$.

Corollary 2 If $\alpha_{2}<\alpha_{1}$, then $\mathcal{P} \mathcal{S}_{\alpha_{2}}^{\gamma} \subset \mathcal{P} \mathcal{S}_{\alpha_{1}}^{\gamma}$.
Proof The same as the proof for Corollary 1.

# 3.2 $\alpha$-Degree non-dominated sorting 

We use $\alpha$-degree Pareto dominance relation to develop a version of the well-known non-dominated sorting algorithm [23] that can be applied for solution ranking in noisy environments, when the objectives are given as intervals. The main steps of this ranking method are shown in Algorithm 1.

The algorithm first orders the solutions into a number of $\alpha$-degree Pareto nondominated sets, by comparing the solutions of the population with the $\alpha$-degree Pareto dominance relation. Then, within each $\alpha$-degree non-dominated set, the solutions are ordered according to their crowding distances in the objective space, which reflects how scattered is each solution in the objective space with respect to the other solutions in the same $\alpha$-degree non-dominated set. In practice, when this ranking method is used

```
Inputs:
    A set of solutions \(P\)
    A dominance degree \(\alpha\)
\(r \leftarrow 0\)
while there are more solutions in \(P\) do
    \(r \leftarrow r+1\)
    \(S_{r} \leftarrow \alpha\)-degree Pareto non-dominated solutions of \(P\)
    \(P \leftarrow P \backslash S_{r}\)
    end while
    for all \(i \in\{1, \ldots, r\}\) do
        \(D_{i} \leftarrow\) Crowding distances of solutions in \(S_{i}\)
        \(S_{i} \leftarrow\) Reorder the solutions in \(S_{i}\) in decreasing value of \(D_{i}\)
    end for
    Output: \(\left\{S_{1}, \ldots, S_{r}\right\}\)
```

Algorithm 1: The $\alpha$-Degree Non-Dominated Sorting Algorithm
with techniques like truncation selection, the crowding distance is computed only for the solutions of the $\alpha$-degree non-dominated set which cannot be added completely to the set of selected solutions.

To compute the crowding distances, the solutions are ordered with respect to each of the objectives individually, and the crowding distance of the solutions with minimum and maximum value for each objective is set to a large number, indicating that these solutions are well scattered with respect to that objective. The crowding distance of other in-between solutions is computed by summing up the normalized distances of each solution to its preceding and succeeding solutions in each objective with respect to the ordering. To order the solutions in each objective dimension, the quick sort algorithm is adapted to work with interval values, comparing two solutions by checking whether $\operatorname{deg}_{j}(\cdot, \cdot)>0$. The value of $\operatorname{deg}_{j}(\cdot, \cdot)$ function is also used as a normalized estimation of the distances between interval values of the solutions in each objective.

# 4 Multi-objective optimization with joint variable-objective probabilistic modeling 

The common practice in most EAs (including EDAs) is to only use the variable values for generating new solutions in the search space. The objective values are used for ranking and selecting a subset of solutions, and apart from that, these algorithms ignore the objective information when generating new solutions. Although this scheme of new solution generation usually offers a relatively good exploration of the search space, the objective information of the selected solutions can be exploited in the new solution generation step of EAs for further improvement, so that the new solutions have better or comparable objective values than their parents.

In the case of EDAs, when objective information is incorporated into probabilistic modeling, the estimated model not only encodes the characteristics of the variable values of the selected solutions, but it also encodes preferences concerning objective values of these solutions. This especially applies to MOPs, where, because of the existence of several objectives, more information about the quality of the solutions is available. EDAs try to represent the problem structure by probabilistically approximat-

![img-1.jpeg](img-1.jpeg)

Fig. 2 An example of a multi-dimensional Bayesian network structure
ing the interactions between variables and how their combination of values influence the objective functions. Incorporating the objective values of the solutions in the modeling step of these algorithms will allow them to obtain a probabilistic approximation of the relationships between objectives as well (e.g. based on the expected value of the objectives).

A multi-objective EDA based on this idea is MBN-EDA [14], which uses multidimensional Bayesian networks (MBNs), a type of Bayesian networks [40] initially used in multi-dimensional classification [41,42], for joint modeling of variables and objectives. Figure 2 shows an example of an MBN structure. In this type of model, the nodes are organized in two separate layers: the top layer comprises objective nodes and the bottom layer contains variable nodes. The set of arcs in the structure is partitioned into three subsets, resulting in the following subgraphs:

- the class subgraph, containing the objective nodes and the interactions between them,
- the feature subgraph, comprising the variable nodes and their relations, and
- the bridge subgraph, depicting the top-down relationships between objective and variable nodes.

The feature subgraph of MBN encodes the relationships between variables like the models learnt by other Bayesian network-based multi-objective EDAs [43-48]. However, the bridge and class subgraphs, encode new types of relationships as the result of joint modeling of variables and objectives. The bridge subgraph shows the interactions between each objective and the variables (selects a subset of relevant variables for each objective), and the class subgraph represents the relationships directly between objectives.

Like other types of Bayesian networks, each node of MBN stores a set of parameters representing the conditional probability distributions for the values of each variable given different value-settings of their parents according to the network structure. In continuous domains, assuming a Gaussian distribution for the joint vector of variables and objectives, $(\boldsymbol{X}, \boldsymbol{Q})=\left(X_{1}, \ldots, X_{n}, Q_{1}, \ldots, Q_{m}\right)$, where $Q_{j}$ is a random variable taking values from the range of the $j$ th objective function, i.e. $Q_{j}=f_{j}(\boldsymbol{X})$, the joint probability distribution encoded in the probabilistic model of MBN-EDA can be represented as

$$
\rho\left(x_{1}, \ldots, x_{n}, q_{1}, \ldots, q_{m}\right)=\prod_{i=1}^{n} \rho\left(x_{i} \mid \boldsymbol{p} \boldsymbol{a}_{i}\right) \cdot \prod_{j=1}^{m} \rho\left(q_{j} \mid \boldsymbol{p} \boldsymbol{a}_{j}^{\prime}\right)
$$

where $\boldsymbol{P} \boldsymbol{a}_{i} \subseteq\left\{\left\{\boldsymbol{X} \backslash X_{i}\right\} \cup \boldsymbol{Q}\right\}$ and $\boldsymbol{P} \boldsymbol{a}_{j}^{\prime} \subseteq\left\{\boldsymbol{Q} \backslash Q_{j}\right\}$ are the parents of each variable and objective, respectively, according to the MBN structure, and $\boldsymbol{p} \boldsymbol{a}_{i}$ and $\boldsymbol{p} \boldsymbol{a}_{j}^{\prime}$ represent one of their possible value-settings. $\boldsymbol{q}=\left(q_{1}, \ldots, q_{m}\right)$ denotes a possible value-setting for the objective variables $\boldsymbol{Q}=\left(Q_{1}, \ldots, Q_{m}\right)$.

The presence of noise in objective values, represented with intervals, means that in the joint vector $\left(X_{1}, \ldots, X_{n}, Q_{1}, \ldots, Q_{m}\right)$, a subset of objective variables $\boldsymbol{Q}_{I}$, where $I$ is the set of objective function indices in $\mathcal{F}_{I}$, take on interval values. Thus, not all of the values in the joint variable-objective dataset provided for probabilistic modeling are scalar values.

There are some studies in the area of imprecise probabilities and credal sets for estimating a probability distribution for a vector of random variables, when some of these variables take non-scalar values (e.g. set of values or intervals). When Bayesian networks are used to encode this kind of probability distributions they are called credal networks [49]. Because of the inherent complexity of this type of models, the methods proposed for their learning and inference are usually very time consuming.

To be able to iteratively perform the joint modeling of variables and objectives in each generation of MBN-EDA, we have used a simple approach for learning a probabilistic model in the presence of noisy objectives with interval values. Before learning the joint model, all of the interval values are replaced by representative scalar values. For example, when the values returned by noisy objective functions are considered to be confidence intervals, a good representative value for each interval is its estimated expected value, $\widehat{\mathbb{E}}\left(Q_{j}\right)$. This way of scalarization is also justified when taking into account the fact that in joint probabilistic modeling, objective values are only used to obtain an approximation of the influence of objectives on each other and on the variables.

Once the dataset is scalarized, a relatively fast greedy local structure search algorithm [50] is used for learning an MBN from the dataset. The algorithm starts with an initial structure for the network, which can be generated randomly or given based on some prior knowledge of the problem. At each iteration of the algorithm, all possible edge addition, removal and reversal operations that do not violate the constraint for top-down interactions between variable and objective nodes in the bridge subgraph are considered, and the one resulting in the best improvement of a scoring metric is selected and applied to the structure. This step is repeated until no more operations can be found to further improve the scoring metric. If the maximum number of node score evaluations is not reached yet, the structure search is restarted from a new random structure and otherwise the algorithm stops. At the end, the highest scoring Bayesian network in all these sub-searches is returned. We use the Bayesian information criterion (BIC) [51] as the scoring metric, which computes a penalized maximum likelihood of the Bayesian network with respect to the dataset.

New solutions are generated from the estimated MBN using the probabilistic logic sampling (PLS) method [52]. PLS starts with finding an ancestral or topological ordering of the nodes in MBN. In such an ordering, each node appears after its parent nodes

according to the MBN structure. Due to the restrictions imposed on the bridge subgraph in the learning process, all objective nodes appear before variable nodes in the ancestral ordering obtained for an MBN. Next, the conditional probability distributions encoded in the nodes of MBN are sampled one-by-one according to their order of appearance in the ancestral ordering. This means that objective nodes are treated the same as variable nodes and new values are generated for both variables and objectives when sampling the estimated model. In this way, the PLS algorithm can take into account the approximated values for objectives, leading to a sampling which is more consistent with the probabilities encoded in the estimated model. To generate a set of solutions (or samples) from the estimated MBN this sampling process is repeated.

# 5 Experiments 

In this section we perform an experimental study to test the proposed solution ranking method based on $\alpha$-degree Pareto dominance relation and examine the optimization performance of an standard multi-objective EA and MBN-EDA when using this ranking method in noisy MOPs. The problems, noise characteristics and other experimental design features are explained in the following sections.

### 5.1 Noise model

In Sect. 2, we saw that many of the works in the literature simulate the noise in objective functions of an MOP with an additive zero-mean Gaussian distribution:

$$
f_{j}\left(\boldsymbol{x}_{i}\right)+\mathcal{N}\left(0, \sigma_{n}^{2}\right)
$$

where $f_{j}\left(\boldsymbol{x}_{i}\right)$ is the true value of the $j$ th objective function for solution $\boldsymbol{x}_{i}$, and $\sigma_{n}$ controls the level of noise introduced to the objective functions of MOP, which often varies in the range [0.01, 1]. Arnold and Beyer [53] have also studied several other noise models and their influence on the performance of EAs.

As explained earlier, the noise model in Eq. (6), which is used in many of the previous works, results in independent singular noisy values for the objective functions. To obtain interval values for noisy objectives, as it is assumed in this paper, we can draw several random values $\xi_{k}$ from the noise model and use these values to compute a confidence interval, based on a specific confidence level $\gamma$, for each objective function $f_{j}$ and each solution $\boldsymbol{x}_{i}$ :

$$
\left(f_{j}\left(\boldsymbol{x}_{i}\right)+\bar{\xi} \pm z_{\frac{1-\gamma}{2}} \frac{s(\xi)}{\sqrt{K}}\right)
$$

where $K$ is the number of random values drawn from the noise model, and $\bar{\xi}$ and $s(\xi)$ are respectively their mean and standard deviation. However, in practice, using such a method to generate interval values for the noisy objective functions imposes a significant computational overhead to the solution evaluation phase, especially for larger values of $K$. Moreover, this method can reduce the stochasticity of the interval

values generated for the objective functions, as for example with a Gaussian noise model when $K$ increases, the mean and standard deviation of the sampled random values tend to the corresponding parameters of the noise model.

To have a somewhat similar randomness in the generated interval values as in the singular values obtained from Eq. (6), we draw two random values $\xi_{m}$ and $\xi_{s}$ from a Gaussian noise model to compute a confidence interval for each objective function $f_{j}$ and each solution $\boldsymbol{x}_{i}$ :

$$
\left(f_{j}\left(\boldsymbol{x}_{i}\right)+\xi_{m} \pm z_{\frac{1}{2} c} \xi_{s}\right)
$$

These two random values can be generated from two different Gaussian distributions. However, as it is explained in [31], it is more reasonable that the level of noise in $\xi_{m}$ and $\xi_{s}$ increase and decrease correspondingly. In this study we use similar Gaussian distributions for sampling these two values.

# 5.2 WFG test problems 

Huband et al. [54] reviewed many of the benchmark MOPs proposed in the literature like ZDT [6], DTLZ [55] and OKA [56], and based on the analysis of these problems, they proposed a new set of MOPs called the walking fish group (WFG) problems. These MOPs have a diverse set of properties found in real-world problems and, therefore, can be a great challenge for any multi-objective optimization algorithm. Each objective function $f_{j}$ of an MOP in this benchmark is defined as

$$
\min _{z} f_{j}(z)=D \cdot z_{m}+S_{j} \cdot h_{j}\left(z_{1}, \ldots, z_{m-1}\right)
$$

where $D$ and $S_{j}$ are scaling factors and $h_{j}(\cdot)$ is a shape function, meaning that it will determine the shape of the Pareto optimal front of an MOP (e.g. concave, convex, etc.) together with the shape functions in the definition of other objective functions of that MOP. $z=\left(z_{1}, \ldots, z_{m}\right)$ is an $m$-dimensional vector of parameters obtained by applying a number of transformation functions, like shifting, biasing or reduction, to the $n$-dimensional input solution $\boldsymbol{x} \in \mathbb{D}$.

We have selected 5 MOPs of this benchmark for our experiments in this paper. Theses problems are WFG1, WFG2, WFG3, WFG7 and WFG9, and cover different shapes for the Pareto optimal front. WFG1 has a mixed convex-concave optimal front shape, WFG2 has a disconnected convex front, and WFG3 has a degenerated linear front. WFG7 and WFG9 problems have a concave Pareto optimal front. Besides different shapes, the objective functions of these MOPs have various properties like inseparability, multi-modality and deception. We consider three objectives and 10 variables for all of the MOPs. Noise is introduced to the output of all three objective functions in each MOP using Eq. (8), resulting in a confidence interval for each solution in the search space.

### 5.3 Experimental design

In the experiments performed in this section, we study and compare two solution ranking methods when the noisy objective values are given as intervals. The first

method is the proposed $\alpha$-degree non-dominated sorting algorithm (Algorithm 1), hereafter referred to as degree ranking (DR), and tested with three different dominance degrees: $\alpha \in\{0.1,0.5,0.9\}$. As the second method, we adopt probabilistic ranking (PR) [19], based on dominance probability (Definition 2), which is often used as a reference solution ranking method in the studies on multi-objective optimization in noisy environments, and ranks each solution $\boldsymbol{x}_{i}$ as follows:

$$
\operatorname{rank}_{P R}\left(\boldsymbol{x}_{i}\right)=\sum_{k=1}^{N} P\left(\boldsymbol{x}_{k} \prec \boldsymbol{x}_{i}\right)+\frac{1}{2} \sum_{k=1}^{N} P\left(\boldsymbol{x}_{k} \equiv \boldsymbol{x}_{i}\right)-\frac{1}{2}
$$

where

$$
P(\boldsymbol{x} \equiv \boldsymbol{y})=1-P(\boldsymbol{x} \prec \boldsymbol{y})-P(\boldsymbol{x} \succ \boldsymbol{y})
$$

represents the probability that neither $\boldsymbol{x}$ nor $\boldsymbol{y}$ dominate each other, and $N$ is the population size. The last term in Eq. (10) is subtracted so that

$$
\sum_{k=1}^{N} \operatorname{rank}_{P R}\left(\boldsymbol{x}_{k}\right)=\frac{N(N-1)}{2}
$$

This ranking method defines a total ordering between the solutions of population, allowing to sort the solutions based on the ranks assigned by $\operatorname{rank}_{P R}(\cdot)$.

To simplify dominance probability computation in multi-objective case, which involves multivariate integration, the objective functions are assumed to be statistically independent [19,20], and therefore the dominance probability in Eq. (2) is approximated as:

$$
P(\boldsymbol{x} \prec \boldsymbol{y})=\prod_{j=1}^{m} P\left(U_{j}<V_{j}\right)
$$

where $U_{j}=f_{j}(\boldsymbol{x})$ and $V_{j}=f_{j}(\boldsymbol{y})$ are the random variables representing the $j$ th objective values returned for two solutions $\boldsymbol{x}$ and $\boldsymbol{y}$. Moreover, when noise is modeled as a Gaussian distribution, Hughes [19] proposed an approximation of the univariate integration required in the computation of $P\left(U_{j}<V_{j}\right)$ to further reduce the computational complexity of the overall solution ranking:

$$
\begin{aligned}
P\left(U_{j}<V_{j}\right) & =\frac{1}{2}-\frac{1}{2} \operatorname{erf}\left(\frac{U_{j}-V_{j}}{\sigma_{V} \sqrt{2+2\left(\frac{\sigma_{U}}{\sigma_{V}}\right)^{2}}}\right) \\
& \approx \frac{1}{2}-\frac{1}{2} \tanh \left(\frac{U_{j}-V_{j}}{0.8 \sigma_{V} \sqrt{2+2\left(\frac{\sigma_{U}}{\sigma_{V}}\right)^{2}}}\right)
\end{aligned}
$$

where $\sigma_{U}$ and $\sigma_{V}$ are the standard deviations of the random variables $U_{j}=f_{j}(\boldsymbol{x})$ and $V_{j}=f_{j}(\boldsymbol{y})$, respectively. When objective values are given as confidence intervals, the estimated expected values and half-widths are used as approximations for $U_{j}$ and

$V_{j}$ and their standard deviations in the computation of dominance probability with Eq. (12).

These ranking methods are used in MBN-EDA to rank and select a subset of solutions for offspring generation with probabilistic modeling. A deterministic binary tournament selection with replacement strategy is employed to select $50 \%$ of the population solutions.

For better comparison, we have also included a standard EMO algorithm based on NSGA-II [23] in the experimentation which uses simulated binary crossover [57] and polynomial mutation [58] for offspring generation and search space exploration. We refer to this algorithm simply as EA in contrast to MBN-EDA which will be indicated as EDA in the experimental results. Both of the algorithms use an elitist replacement strategy, a population of 50 solutions and stop after 300 generations. The initial population is generated randomly in both algorithms by uniform sampling from the variables domain.

For each of the five MOPs tested in our experiments, we have studied three different levels of noise and confidence: $\sigma_{n} \in\{0.01,0.1,1\}$ and $\gamma \in\{0.90,0.95,0.99\}$. Therefore, all together, there are $5 \times 3 \times 3 \times 2 \times 4=360$ different possible combinations for the experiments. For each combination, 10 independent runs are performed. To evaluate the results of experiments, we have used 5 different quality measures: hypervolume [28], inverted generational distance (IGD) [59], epsilon indicator [60], relative maximum spread [30] and Schott's spacing [61]. In the evaluation process, the Pareto set approximated by each algorithm is used to obtain a noiseless Pareto front which is then used to compute any of these indicators. For this purpose the objective values (without the influence of the noise model) are computed for the solutions in the approximated Pareto sets, resulting in the corresponding noiseless Pareto fronts. Therefore, the noisy Pareto fronts approximated by the algorithms in the course of evolution might be (and usually are) better than the noiseless Pareto fronts, especially for higher levels of noise.

Given a Pareto set approximation $A$, its hypervolume indicator value with respect to a set $R$ of reference points in the objective space, denoted as $I_{h}(A, R)$, is given as

$$
I_{h}(A, R)=\bigcup_{\boldsymbol{x} \in A} H(\boldsymbol{f}(\boldsymbol{x}), R)
$$

where $H(\boldsymbol{a}, B)$ indicates the (hyper-)volume between point $\boldsymbol{a}$ and the points of set $B$ in the objective space. A higher value for this indicator implies a better Pareto set approximation. We use a single reference point, often called the nadir point, with a value of 100 for all objectives to compute this indicator.

IGD indicator accounts for both the diversity of the approximated front as well as its convergence to the Pareto optimal front. Given a set of points $F^{*}$, representing a well-distributed sampling of the Pareto optimal front of an MOP, the IGD value for a Pareto set approximation $A$ is computed as:

$$
I G D_{F^{*}}(A)=\frac{\sum_{\boldsymbol{r} \in F^{*}} \min _{\forall \boldsymbol{x} \in A} \mathrm{~d}(\boldsymbol{r}, \boldsymbol{f}(\boldsymbol{x}))}{\left|F^{*}\right|}
$$

where $\mathrm{d}(\cdot, \cdot)$ gives the Euclidean distance between the two points in objective space. A smaller value for this indicator means a better approximation. A sampling of 10, 000 points is used for representing the Pareto optimal front of the MOPs when computing the values of this indicator. The description of the other three quality indicators is given in the supplementary Online Resource of the paper.

# 5.4 Results 

Tables 2, 3, 4, 5, 6, 7, 8, 9, 10, and 11 show the mean and standard deviation of the hypervolume and IGD indicator values for the final Pareto solutions obtained with different combinations of the two algorithmic frameworks and the studied ranking methods, for the tested MOPs. The corresponding figures showing the average values of hypervolume, IGD, epsilon, relative maximum spread and Schott's spacing indicators for the Pareto solutions obtained along the evolution path are given in the supplementary Online Resource of the paper.

With the increase in the noise level, the change in the position of intervals with respect to the original noiseless values of the objective function will be higher, and also the length of intervals increases. Besides, increasing the confidence level results in wider intervals. Therefore, as the level of noise increases the value of objective functions are more distorted. Because of this, we focus the analysis of the results on the common patterns for the average behavior of the algorithms on different instances (with different levels of noise and confidence) of the tested problems.

In the objective functions of WFG1 problem, the input variables are greatly biased, making an even exploration of the search space very difficult, especially in the presence of noise. According to the employed quality indicators, the solution ranking provided by DR method (with different degrees of dominance) allows to obtain better approximations of Pareto set on most of the problem instances. As the noise level increases, the quality of the Pareto sets obtained using each of the two ranking methods become closer. The increase in the noise level also blurs the differences in the performance of the algorithms using different degrees of dominance for DR method. Moreover, the increase in the confidence level has less influence on DR method when using a high dominance degree like $\alpha=0.9$.

A closer inspection of the Pareto fronts obtained for WFG1 problem shows that the algorithms are not able to obtain a well covering approximation of the Pareto optimal front. This can also be seen by the values obtained for the relative maximum spread indicator (see the supplementary Online Resource). Actually, EA completely minimizes this indicator along the evolution path for smaller noise levels, as a result of the high bias in the objectives. However, the joint modeling adopted in EDA allows a better exploration of this problem's search space, at least for lower noise levels, which is also reflected by the values obtained for hypervolume and IGD indicators.

The results obtained for WFG2 problem (Tables 4, 5) also show that the Pareto sets approximated with DR method are superior to those obtained using PR method. When a higher degree of dominance is used for the DR method, the performance of the algorithms with respect to the different quality indicators are more sensitive to the increase in the length of the intervals, i.e. when increasing the level of noise or

![img-2.jpeg](img-2.jpeg)

![img-3.jpeg](img-3.jpeg)

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

confidence. In the last objective of this problem, the variables are considered to be correlated and therefore, employing model learning to find out this relationships helps EDA to obtain better Pareto set approximations under different levels of noise and confidence. Considering the values obtained by hypervolume and IGD indicators on the one hand and relative maximum spread indicator (see the supplementary Online Resource) on the other hand, we can conclude that although the Pareto fronts approximated by EA are better spread, but these fronts are farther from the Pareto optimal front than those obtained by EDA.

Very similar results to those of the previous problem are obtained for WFG3 problem. The difference in the average performance of the algorithms using PR and DR methods are clearer on this problem, and it can be seen that the solution ranking provided by PR method completely misguides the algorithms during evolution for approaching the Pareto optimal set according to the quality indicators, even with small levels of noise and confidence (see Tables 6, 7). The DR method using smaller dominance degrees results in relatively better algorithm performance on different levels of noise and confidence with respect to the quality indicators used. The indicators values also show that EA obtains relatively better results on WFG3 problem, though for larger noise levels the results obtained by EDA are comparable or better than those reached by EA.

The objective functions of WFG7 problem are separable and unimodal, with bias in the optimum values for some of the variables. The results obtained with DR method on this problem outperform those of PR method with a relatively great margin, although the increase in the noise level reduces the effectiveness of this ranking method, especially when using it with EDA. Again, the Pareto fronts approximated with lower dominance degrees for DR method are better. However, it can be seen that when the confidence level increases the performance of the algorithms using a high level of dominance degree is less affected. In general, the search with EA results in relatively better Pareto front approximations comparing with the fronts obtained by EDA-based search according to the quality indicators values. Moreover, with the increase in the level of noise or confidence, which makes the problem harder, the results obtained by the two algorithmic frameworks become comparable.

The objective functions of WFG9 problem in contrast to those of the previous problem are non-separable and multi-modal, with multi-modality being deceptive towards local optima for some of the objectives. As a result introducing noise to the objectives of this problem will make it very difficult to solve. The indicator values computed for the approximated Pareto fronts show that the proposed DR method outperforms solution ranking based on dominance probability, though with the increase in the noise level the difference in the results obtained by the two methods gradually diminishes.

According to the results (Tables 10, 11), lower dominance degrees like $\alpha=0.1$ and $\alpha=0.5$ allow a better ranking of solutions in DR method. Moreover, on the contrary to the previous problem, when the confidence level is increased DR method with higher dominance degree $(\alpha=0.9)$ is also greatly affected. As it is shown in the supplementary Online Resource, for this problem both EDA and EA based search with DR method are able to cover a high percentage of the Pareto optimal front (more than $80 \%$ ). Comparing these two algorithmic frameworks, it is observed that

the Pareto fronts approximated by EDA are comparable or better to those obtained by EA, depending on the quality indicator. This better performance can be explained by the ability of the proposed EDA to capture the relationships between variables of the problem, which is necessary for finding the solutions.

# 5.5 Effect of population size 

In addition to the previous experimentations, to make sure that our findings generalize to larger population sizes we have studied the effect of population size on the performance of the algorithms. For this purpose, different combinations of algorithmic frameworks and ranking methods are applied for optimization on a specific problem instance with different population sizes and the final noiseless Pareto fronts are compared. The experiments are conducted using WFG1 problem with noise level $\sigma_{n}=0.1$ and confidence level $\gamma=0.95$ while testing the algorithms with the following population sizes: $N \in\{50,100,150,200,250,300\}$. Figures 3 and 4 respectively show the hypervolume and IGD indicators values for final noiseless Pareto fronts approximated with different population sizes.

As the results show, with larger population sizes better indicator values can be reached, although the difference is not significant. The distinction between the quality of the fronts approximated by DR and PR methods becomes clearer when the population size increases, showing that with DR method better results can be obtained in both algorithmic frameworks and with different values of the dominance degree. Indeed with EA, as the population size increases the difference in the quality of the fronts approximated with different values of dominance degree almost fade away while becoming considerably superior to the fronts approximated with PR method, according to the quality indicators used. The results also show that the direct manipulation of solutions in EA-based search is more affected by the increase in population size comparing with the model learning in the EDA-based search. This can be explained by the fact that the model learning method employed in this algorithm (using regularization techniques) is designed to be less sensible to the dimensionality of the training data. Furthermore, it can be seen that in this algorithmic framework strict condition for accepting solutions as non-dominated (i.e. when $\alpha=0.9$ ) in DR method results in better Pareto fronts as the population size increases.

### 5.6 Discussion

The values of the quality indicators for the Pareto sets obtained along the evolution path (see the supplementary Online Resource), show how the population of different algorithm versions evolve. In general, based on the change in the values of these indicators during evolution, we can see that the solution ranking provided by DR method guides the optimization in the correct direction through the search space of the tested MOPs, with some exceptions like WFG1 and WFG3 when a high level of noise exists. On the contrary, when PR method is used for ranking the solutions, the algorithm is misguided in the search space of many of the tested problems. In probabilistic dominance the probability that a solution dominates another solution is

![img-12.jpeg](img-12.jpeg)

Fig. 3 Average Hypervolume values of the Pareto fronts obtained for WFG1 problem with different population sizes when noise level is $\sigma_{\mathrm{H}}=0.1$ and confidence level is $\gamma=0.95$
computed based on the distribution of corresponding intervals of the two solutions. In a multi-objective scenario, when these probabilities are summed up in Eq. (10) and due to the complex combinations that the distributions might have, the ranks generated for

![img-13.jpeg](img-13.jpeg)

Fig. 4 Average IGD values of the Pareto fronts obtained for WFG1 problem with different population sizes when noise level is $\sigma_{n}=0.1$ and confidence level is $\gamma=0.95$
the solutions can be very close or even equal, increasing the possibility of discarding good solutions in the selection process.

Moreover, the approximation used in Eq. (12) to compute probabilistic dominance because of the high computational complexity of the original formulation naturally

produces small probability values, which in turn can increase the previous effect (generation of similar ranks). It is worth mentioning that even computing the approximation of dominance probability requires considerably more time than deciding dominance between solutions using $\alpha$-degree Pareto dominance. Furthermore, our experimental results show that since confidence level is not considered in probabilistic dominance, with the increase in confidence level the ranking provided based on dominance probabilities is not able to correctly guide the search.

When using DR method, the Pareto fronts approximated with smaller to medium values of dominance degree $\alpha$ are better on most of the tested problems with different levels of noise and confidence. On the one hand, smaller values of $\alpha$ allow higher degrees of overlapping between intervals, meaning that the solutions can dominate each other easier. With small values of $\alpha$, according to Corollary 2 the ratio of dominated solutions increases and therefore more solutions become comparable, resulting in a finer ordering of the solutions by the employed $\alpha$-degree non-dominated sorting algorithm. This increase in the number of comparable solutions seems to compensate for the lack of strict decisions on the quality of the solutions. On the other hand, strict decisions about solution dominance allow only very good solutions to enter the $\alpha$-degree non-dominated set, while causing many solutions to become incomparable. Based on the experimental results, with a combination of the previous two effects which is achieved when using medium values of dominance degree (e.g. $\alpha=0.5$ ), better Pareto set can be approximated on many of the tested MOPs and for different levels of noise and confidence. When the population size increases and more solutions are available in the ranking step, the latter effect (strict decisions) becomes more usable, enhancing the elitism selection in $\alpha$-degree non-dominated sorting algorithm.

Similarly, as the confidence level of the intervals (i.e. the values of the objective functions) decreases, more and more solutions become dominated (Corollary 1), and thus the solutions will be ordered in a larger number of $\alpha$-degree non-dominated sets during the first step of Algorithm 1, essentially leading to better solution ranking. Therefore, when DR method is used in the optimization, the Pareto sets approximated for lower confidence levels are usually better, according to the quality indicator values. Taking more strict decisions by using high dominance degrees (e.g. $\alpha=0.9$ ) when the confidence level increases, reduces the number of $\alpha$-degree non-dominated sets found in the first step of Algorithm 1, and thus the ordering of the solutions will depend more on their crowding distance computed in the second step of $\alpha$-degree non-dominated sorting algorithm. For some of the tested problems (e.g. WFG1 and WFG7), such an ordering with high $\alpha$ values seems to be less affected as the confidence level increases.

Based on our analysis and experimental results obtained with different values of dominance degree, we can say that when working with low levels of noise and confidence that result in smaller interval values and in small populations, smaller values of the $\alpha$ parameter can cause the algorithm to advance better in the noise-affected search space. However, with larger intervals as the values of objective functions and when larger population sizes are available, setting $\alpha$ to larger values can help to faster reach better solutions during the search.

# 6 Conclusions 

In real-world multi-objective optimization, the value of objective functions may involve noise and thus do not correctly represent the quality of solutions. Populationbased EAs, which are one of the most successful methods in solving MOPs, have inherent abilities to deal with small levels of noise in objective values. However, with larger noise levels, especially when there are several conflicting objectives to be optimized, specific considerations are needed to perform successful optimization.

We considered noisy objective values given as intervals and proposed $\alpha$-degree Pareto dominance to deal with this type of values for the objective functions. This relation allowed to determine the dominance between solutions even when there is a specific degree of overlapping between some of the interval values, which is controlled by parameter $\alpha$. The similarity between this dominance relation and the conventional Pareto dominance allowed related terminology, like Pareto optimal set, to be easily defined. Assuming confidence intervals with a specific confidence level as the values of the noisy objective functions, we studied some of the properties of $\alpha$-degree Pareto dominance. It was shown that the $\alpha$-degree dominance relations defined between solutions are unaffected when the confidence level $\gamma$ or dominance degree $\alpha$ are reduced, and that such a reduction decreases the size of Pareto optimal set.

Based on this relation, $\alpha$-degree Pareto non-dominated sorting algorithm, an adaptation of the well-known non-dominated sorting algorithm in noisy domains with interval values, was proposed and integrated into a multi-objective EDA based on joint probabilistic modeling of variables and objectives to find the solutions of noisy MOPs. The algorithm was tested on a set of MOPs where noisy objective values are given as intervals, and its solution ranking and search space exploration were respectively compared with a reference ranking method based on dominance probability and standard EA operators for continuous optimization.

The analysis of the approximated Pareto sets with five different quality indicators based on the corresponding noiseless Pareto fronts showed that the proposed solution ranking method based on $\alpha$-degree Pareto dominance relation allows the algorithms to achieve considerably better results comparing with the well-known probabilistic ranking method on the tested problems and for increasing levels of noise and confidence. We discussed how the change in the dominance degree and confidence level changes comparability of the solutions using $\alpha$-degree Pareto dominance relation and saw that small to medium degrees of dominance allow better ranking of the solutions on most of the tested instances. Moreover, depending on the specific properties of the MOPs, the quality indicator values showed that the joint probabilistic modeling of variables and objectives allowed MBN-EDA to find Pareto set approximations for some of the tested problems that are superior to those approximated by the standard multi-objective EA in different levels of noise.

As future works, other forms of degree function $\operatorname{deg}_{j}(\cdot, \cdot)$ can be studied for determining the overlapping between intervals by for example taking into account the distribution of the values in the intervals. Moreover, it would be worth considering the correlations between objectives and their noise values in the ranking procedure. A starting point for this line of research is to use the model learning similar to the one used in MBN-EDA. Dynamic adjustment of the dominance control parameter, $\alpha$, is

also an interesting future research. We also intend to apply the developed methodology on a real-world problem. Specifically, we are considering the application of the proposed approach to the feature subset selection problem in machine learning and data mining tasks. The objectives of this problem are uncertain and can very naturally be represented as intervals. This would also require adapting the joint probabilistic modeling to domains with discrete variables and objective values given as intervals.

Acknowledgments This work has been partially supported by TIN2010-20900-C04-04 and Cajal Blue Brain projects (Spanish Ministry of Economy and Competitiveness).

# References 

1. Pareto, V.: The new theories of economics. J. Polit. Econ. 5(4), 485-502 (1897)
2. Goldberg, D.E.: Genetic Algorithms in Search, Optimization and Machine Learning, 1st edn. AddisonWesley Longman Publishing Co., Inc., Boston (1989)
3. Abraham, A., Jain, L., Goldberg, R. (eds.): Evolutionary Multiobjective Optimization: Theoretical Advances and Applications. Springer, London (2005)
4. Coello Coello, C.A., Lamont, G.B., Van Veldhuizen, D.A.: Evolutionary Algorithms for Solving Multiobjective Problems, 2nd edn. Springer, Berlin (2007)
5. Deb, K.: Multi-objective Optimization Using Evolutionary Algorithms. Wiley, London (2001)
6. Zitzler, E., Deb, K., Thiele, L.: Comparison of multiobjective evolutionary algorithms: empirical results. Evol. Comput. 8(2), 173-195 (2000)
7. Larrañaga, P., Lozano, J.A. (eds.): Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Kluwer Academic Publishers, Norwell (2001)
8. Lozano, J.A., Larrañaga, P., Inza, I., Bengoetxea, E. (eds.): Towards a New Evolutionary Computation: Advances on Estimation of Distribution Algorithms, vol. 192. Studies in Fuzziness and Soft Computing. Springer (2006)
9. Mühlenbein, H., Paaß, G.: From recombination of genes to the estimation of distributions I. Binary parameters. In: Fourth International Conference on Parallel Problem Solving from Nature (PPSN IV), vol. 1141. Lecture Notes in Computer Science, pp. 178-187. Springer (1996)
10. Pelikan, M.: Hierarchical Bayesian optimization algorithm. Toward a new generation of evolutionary algorithms, vol. 170. In: Studies in Fuzziness and Soft Computing, 1st ed. Springer (2005)
11. Martí, L., Garcia, J., Berlanga, A., Coello Coello, C.A., Molina, J.M.: On current model-building methods for multi-objective estimation of distribution algorithms: shortcomings and directions for improvement. Tech. Rep. GIAA2010E001, Department of Informatics, Universidad Carlos III de Madrid (2010)
12. Pelikan, M., Sastry, K., Goldberg, D.: Multiobjective estimation of distribution algorithms. In: Scalable Optimization via Probabilistic Modeling, vol. 33. Studies in Computational Intelligence, pp. 223-248. Springer (2006)
13. Thierens, D., Bosman, P.A.N.: Multi-objective mixture-based iterated density estimation evolutionary algorithms. In: Conference on Genetic and Evolutionary Computation (GECCO '01), pp. 663-670. Morgan Kaufmann (2001)
14. Karshenas, H., Santana, R., Bielza, C., Larrañaga, P.: Multi-objective estimation of distribution algorithm based on joint modeling of objectives and variables. IEEE Trans. Evol. Comput. 18(4), 519-542 (2014)
15. Jin, Y., Branke, J.: Evolutionary optimization in uncertain environments-a survey. IEEE Trans. Evol. Comput. 9(3), 303-317 (2005)
16. Tan, K., Goh, C.: Handling uncertainties in evolutionary multi-objective optimization. Computational Intelligence: Research Frontiers, vol. 5050. Lecture Notes in Computer Science, pp. 262-292. Springer (2008)
17. Soares, G., Guimaraes, F., Maia, C., Vasconcelos, J., Jaulin, L.: Interval robust multi-objective evolutionary algorithm. In: IEEE Congress on Evolutionary Computation (CEC'09), pp. 1637-1643 (2009)
18. Goh, C., Tan, K., Cheong, C., Ong, Y.: An investigation on noise-induced features in robust evolutionary multi-objective optimization. Expert Syst. Appl. 37(8), 5960-5980 (2010)

19. Hughes, E.: Evolutionary multi-objective ranking with uncertainty and noise. In: Evolutionary Multicriterion Optimization (EMO'01), vol. 1993. Lecture Notes in Computer Science, pp. 329-343. Springer (2001)
20. Teich, J.: Pareto-front exploration with uncertain objectives. In: Evolutionary Multi-Criterion Optimization, vol. 1993. Lecture Notes in Computer Science, pp. 314-328. Springer (2001)
21. Greiner, D., Galván, B., Aznárez, J., Maeso, O., Winter, G.: Robust design of noise attenuation barriers with evolutionary multiobjective algorithms and the boundary element method. In: Evolutionary Multicriterion Optimization, vol. 5467. Lecture Notes in Computer Science, pp. 261-274. Springer (2009)
22. Bui, L.T., Abbass, H.A., Essam, D.: Fitness inheritance for noisy evolutionary multi-objective optimization. In: Conference on Genetic and Evolutionary Computation (GECCO’05), pp. 779-785. ACM (2005)
23. Deb, K., Pratap, A., Agarwal, S., Meyarivan, T.: A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE Trans. Evol. Comput. 6(2), 182-197 (2002)
24. Bui, L.T., Essam, D., Abbass, H.A., Green, D.: Performance analysis of evolutionary multi-objective optimization methods in noisy environments. Complex. Int. 11, 29-39 (2005)
25. Zitzler, E., Laumanns, M., Thiele, L.: SPEA2: Improving the strength Pareto evolutionary algorithm for multiobjective optimization. In: Evolutionary Methods for Design Optimization and Control with Applications to Industrial Problems (EUROGEN '01), pp. 95-100. International Center for Numerical Methods in Engineering (2001)
26. Fieldsend, J., Everson, R.: Multi-objective optimisation in the presence of uncertainty. IEEE Congr. Evol. Comput. (CEC'05) 1, 243-250 (2005)
27. Büche, D., Stoll, P., Dornberger, R., Koumoutsakos, P.: Multiobjective evolutionary algorithm for the optimization of noisy combustion processes. IEEE Trans. Syst. Man Cybern. Part C: Appl. Rev. 32(4), $460-473(2002)$
28. Zitzler, E., Thiele, L.: Multiobjective evolutionary algorithms: a comparative case study and the strength Pareto approach. IEEE Trans. Evol. Comput. 3(4), 257-271 (1999)
29. Babbar, M., Lakshmikantha, A., Goldberg, D.E.: A modified NSGA-II to solve noisy multiobjective problems. In: Genetic and Evolutionary Computation Conference (GECCO’03), pp. 21-27 (2003)
30. Goh, C., Tan, K.: An investigation on noisy environments in evolutionary multiobjective optimization. IEEE Trans. Evol. Comput. 11(3), 354-381 (2007)
31. Eskandari, H., Geiger, C.: Evolutionary multiobjective optimization in noisy problem environments. J. Heuristics 15(6), 559-595 (2009)
32. Bui, L.T., Abbass, H.A., Essam, D.: Localization for solving noisy multi-objective optimization problems. Evol. Comput. 17(3), 379-409 (2009)
33. Syberfeldt, A., Ng, A., John, R.I., Moore, P.: Evolutionary optimisation of noisy multi-objective problems using confidence-based dynamic resampling. Eur. J. Oper. Res. 204(3), 533-544 (2010)
34. Park, T., Ryu, K.R.: Accumulative sampling for noisy evolutionary multi-objective optimization. In: 13th Annual Conference on Genetic and Evolutionary Computation (GECCO'11), pp. 793-800. ACM (2011)
35. Mehnen, J., Trautmann, H., Tiwari, A.: Introducing user preference using desirability functions in multi-objective evolutionary optimisation of noisy processes. In: IEEE Congress on Evolutionary Computation (CEC'07), pp. 2687-2694 (2007)
36. Woźniak, P.: Preferences in evolutionary multi-objective optimisation with noisy fitness functions: hardware in the loop study. In: International Multiconference on Computer Science and Information Technology, pp. 337-346 (2007)
37. Kaji, H., Ikeda, K., Kita, H.: Uncertainty of constraint function in evolutionary multi-objective optimization. In: IEEE Congress on Evolutionary Computation (CEC’09), pp. 1621-1628 (2009)
38. Basseur, M., Zitzler, E.: Handling uncertainty in indicator-based multiobjective optimization. Int. J. Comput. Intell. Res. 2(3), 255-272 (2006)
39. Boonma, P., Suzuki, J.: A confidence-based dominance operator in evolutionary algorithms for noisy multiobjective optimization problems. In: 21st International Conference on Tools with Artificial Intelligence (ICTAI'09), pp. 387-394 (2009)
40. Pearl, J.: Bayesian networks: a model of self-activated memory for evidential reasoning. In: 7th Conference of the Cognitive Science Society, pp. 329-334 (1985)
41. Bielza, C., Li, G., Larrañaga, P.: Multi-dimensional classification with Bayesian networks. Int. J. Approximate Reasoning 52(6), 705-727 (2011)

42. de Waal, P., van der Gaag, L.: Inference and learning in multi-dimensional Bayesian network classifiers. In: Symbolic and Quantitative Approaches to Reasoning with Uncertainty, pp. 501-511 (2007)
43. Ahn, C.W., Ramakrishna, R.S.: Multiobjective real-coded Bayesian optimization algorithm revisited: diversity preservation. In: 9th Annual Conference on Genetic and Evolutionary Computation (GECCO '07), pp. 593-600. ACM (2007)
44. Katsumata, Y., Terano, T.: Bayesian optimization algorithm for multi-objective solutions: application to electric equipment configuration problems in a power plant. IEEE Congr. Evol. Comput. (CEC '03) 2, 1101-1107 (2003)
45. Khan, N., Goldberg, D.E., Pelikan, M.: Multiple-objective Bayesian optimization algorithm. In: Conference on Genetic and Evolutionary Computation (GECCO '02), p. 684. Morgan Kaufmann (2002)
46. Laumanns, M., Očenášek, J.: Bayesian optimization algorithms for multi-objective optimization. In: 7th International Conference on Parallel Problem Solving from Nature (PPSN VII), vol. 2439. Lecture Notes in Computer Science, pp. 298-307. Springer (2002)
47. Pelikan, M., Sastry, K., Goldberg, D.E.: Multiobjective hBOA, clustering, and scalability. In: Conference on Genetic and Evolutionary Computation (GECCO '05), pp. 663-670. ACM (2005)
48. Schwarz, J., Očenášek, J.: Multiobjective Bayesian optimization algorithm for combinatorial problems: theory and practice. Neural Netw. World 11(5), 423-442 (2001)
49. Corani, G., Antonucci, A., Zaffalon, M.: Bayesian networks with imprecise probabilities: theory and application to classification. Tech. Rep. IDSIA-02-10, Dalle Molle Institute for Artificial Intelligence (2010)
50. Buntine, W.: Theory refinement on Bayesian networks. In: 7th Annual Conference on Uncertainty in Artificial Intelligence (UAI '91), pp. 52-60. Morgan Kaufmann (1991)
51. Schwarz, G.: Estimating the dimension of a model. Ann. Stat. 6(2), 461-464 (1978)
52. Henrion, M.: Propagating uncertainty in Bayesian networks by probabilistic logic sampling. In: Second Annual Conference on Uncertainty in Artificial Intelligence (UAI '86), vol. 2, pp. 149-163. Elsevier (1986)
53. Arnold, D., Beyer, H.G.: A general noise model and its effects on evolution strategy performance. IEEE Trans. Evol. Comput. 10(4), 380-391 (2006)
54. Huband, S., Hingston, P., Barone, L., While, L.: A review of multiobjective test problems and a scalable test problem toolkit. IEEE Trans. Evol. Comput. 10(5), 477-506 (2006)
55. Deb, K., Thiele, L., Laumanns, M., Zitzler, E.: Scalable multi-objective optimization test problems. IEEE Congr. Evol. Comput. (CEC '02) 1, 825-830 (2002)
56. Okabe, T., Jin, Y., Olhofer, M., Sendhoff, B.: On test functions for evolutionary multi-objective optimization. In: 8th International Conference on Parallel Problem Solving from Nature (PPSN VIII), vol. 3242. Lecture Notes in Computer Science, pp. 792-802. Springer (2004)
57. Deb, K., Agrawal, B.: Simulated binary crossover for continuous search space. Complex Syst. 9(2), $115-148$ (1995)
58. Deb, K., Goyal, M.: A combined genetic adaptive search (GeneAS) for engineering design. Comput. Sci. Inf. 26(4), 30-45 (1996)
59. Coello Coello, C.A., Cortés, N.C.: Solving multiobjective optimization problems using an artificial immune system. Genet. Program. Evol. Mach. 6, 163-190 (2005)
60. Zitzler, E., Thiele, L., Laumanns, M., Fonseca, C., da Fonseca, V.: Performance assessment of multiobjective optimizers: an analysis and review. IEEE Trans. Evol. Comput. 7(2), 117-132 (2003)
61. Schott, J.R.: Fault Tolerant Design Using Single and Multicriteria Genetic Algorithm Optimization. Master's thesis, Massachusetts Institute of Technology, Department of Aeronautics and Astronautics (1995)