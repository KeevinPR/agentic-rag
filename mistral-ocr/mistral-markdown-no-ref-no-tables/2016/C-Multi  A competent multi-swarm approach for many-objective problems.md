# C-Multi: A competent multi-swarm approach for many-objective problems 

Olacir R. Castro Jr. ${ }^{\text {a, }}$, Roberto Santana ${ }^{\text {b }}$, Aurora Pozo ${ }^{\text {a }}$<br>${ }^{a}$ Computer Science Department, Federal University of Paraná (UFPR), PO 19081, 81531-970 Curitiba, Brazil<br>${ }^{\text {b }}$ Intelligent Systems Group, Department of Computer Science and Artificial Intelligence, University of the Basque Country (UPX/EHU),<br>Paseo Manuel de Lardizabal 1, 20080 San Sebastián, Guipúzcoa, Spain

## A R T I C L E I N F O

Article history:
Received 27 March 2015
Received in revised form
18 June 2015
Accepted 19 June 2015
Available online 11 November 2015
Keywords:
Particle swarm optimization
Many-objective
Estimation of distribution algorithm
Competent algorithm

## A B S T R A C T

One of the major research topics in the evolutionary multi-objective community is handling a large number of objectives also known as many-objective optimization problems (MaOPs). Most existing methodologies have demonstrated success for problems with two and three objectives but face significant challenges in many-objective optimization. To tackle these challenges, a hybrid multi-swarm algorithm called C-Multi was proposed in a previous work. The project of C-Multi is based on two phases; the first uses a unique particle swarm optimization (PSO) algorithm to discover different regions of the Pareto front. The second phase uses multiple swarms to specialize on a dedicate part. On each subswarm, an estimation of distribution algorithm (EDA) is used to focus on convergence to its allocated region. In this study, the influence of two critical components of C-Multi, the archiving method and the number of swarms, is investigated by empirical analysis. As a result of this investigation, an improved variant of C-Multi is obtained, and its performance is compared to I-Multi, a multi-swarm algorithm that has a similar approach but does not use EDAs. Empirical results fully demonstrate the superiority of our proposed method on almost all considered test instances.
(c) 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Recently, as many real-world applications involve four or more objectives [1], the evolutionary multi-objective optimization (EMO) community has focused its attention to handle large number of objectives (Many-objective optimization problems, MaOPs). Since, several studies pointed that Pareto based algorithms scale poorly in MaOPs [2-4] because of the increase in the number of non-dominated solutions which deteriorates the selection pressure compromising the convergence to the Pareto front and diversity of the solutions.

In a previous work [5] we presented a hybrid algorithm called C-Multi to deal with this challenge. The project of C-Multi is based on two phases: the first uses a unique particle swarm optimization algorithm (PSO) [6] to discover the different regions of the Pareto front. The second phase uses multiple swarms to specialize on a dedicate part. On each swarm, an estimation of distribution algorithm (EDA) [7] is used to focus on convergence to its allocated region. The study featured a comparative study involving the

[^0]C-Multi and the I-Multi algorithms using the DTIZ [8] family of benchmark problems. I-Multi is a multi-swarm algorithm that has a similar project to C-Multi but does not incorporate probabilistic modeling to the search as C-Multi does. The result of the comparison was that C-Multi achieved good results in some problems, but performed poorly in general.

Here, in this study, our goal is to investigate the following hypothesis: $H_{1}$ the performance of C-Multi can be further improved by an appropriate adjustment of two critical components of the algorithm; the type of archiving method, and the number of swarms. We initially hypothesized that finding a robust setting for these two components, together with the use of EDAs, could enhance C-Multi and help it to overcome I-Multi in the general case. To investigate this hypothesis, firstly we conducted two studies on the impact of C-Multi components. One of them evaluated the effect of the archiver used in the multi-swarm phase of the algorithm. The other assessed the effect of the number of sub-swarms. Next, we conducted extensive experimentation to compare the performances of C-Multi, enhanced with our findings from the previous studies, and I-Multi. Moreover, we compared both algorithms to a state-of-the-art algorithm called MOEA/DDRA [9] in order to assess the effectiveness of the new algorithm. The obtained results indicate that C-Multi can be a competitive


[^0]:    * Corresponding author.

    E-mail addresses: olacirjr@gmail.com (O.R. Castro Jr.), roberto.santana@ehu.es (R. Santana), aurora@inf.ufpr.br (A. Pozo).

algorithm and the use of EDAs is a promising area in manyobjective optimization.

The remaining of this paper is organized as follows: the next section presents related works. Some background concepts are described in Section 3. Section 4 presents the C-Multi algorithm. Experimental studies to investigate the influence of components of C-Multi, as well as an empirical study comparing it to I-Multi and MOEA/D-DRA are reported in Section 5. And finally, Section 6 presents the conclusions.

## 2. Related works

Multi-Objective Evolutionary Algorithms (MOEAs) modify EAs by incorporating a selection mechanism that is based on Pareto optimality and by adopting a diversity preservation mechanism that avoids the convergence to a single solution [10]. Although most of the studies on MOPs have focused on problems that have a small number of objectives, practical optimization problems involve a large number of criteria [11]. Therefore, research efforts have been oriented toward investigating the scalability of these algorithms with respect to the number of objectives [12]. Several studies have shown that MOEAs scale poorly in MaOPs [12], [13]. The main reason for this scaling property is that the number of nondominated solutions increases exponentially with the number of objectives. The following consequences occur: First, the search ability deteriorates because it is not possible to impose preferences for selection purposes, since most elite preserving mechanisms of MOEAs employ Pareto dominance as a major selection criterion. Second, the number of solutions that are required for approximating the entire Pareto front increases, therefore, in a highdimensional objective space a limited number of solutions are likely to be far away from each other.

Among the studies presented in the literature, several papers address the issues of Many-Objective Optimization and deserve to be highlighted. In [14], an extension of the NSGA-II algorithm applied to MaOPs is presented. The new algorithm, known as NSGA-III, uses a set of reference points that are aimed at guiding the search toward the Pareto front without losing diversity. These points help the convergence and the diversity of the algorithm. Basically, the proposed algorithm builds niches for each reference point. Thus, the specialization of the algorithm enables convergence, and the different niches enable diversification. With these goals, the authors proposed a new density estimator that calculates the concentration of solutions around the reference points. Solutions that are close to less crowded reference points obtain an advantage in the selection process, similar to the crowding distance in NSGA-II. The NSGA-III was compared to MOEA/D [15], a decomposition based algorithm, and the best results were presented for different many-objective scenarios. More recently, in [16] a unified framework exploits dominance and decomposition based approaches from NSGAII and MOEAD/D to tackle MaOPs. The results of this unified framework have demonstrated its capability to find a well converged and well distributed approximation of the Pareto front.

In spite of the existence of different studies that address MaOPs, until very recently, most of these research studies focused on a small group of algorithms, often the NSGA-II or MOEA/D. In our project, the behavior of the PSO in MaOPs is investigated, since this approach has shown to be very efficient both in singleobjective and in multi-objective optimization problems from different domains [17], [18]. Its idea of moving across the search space towards the best solutions found so far while keeping a diverse population, points to the convenience of applying this method to MaOPs, where convergence and diversity are needed for a good coverage of the Pareto front. Therefore, PSO is a suitable algorithm for continuous many-objective optimization, but it is still underexplored in the literature.

In this direction, it can be mentioned the work presented in [4] that investigates several archiving methods, among them the Ideal and Multi-level Grid Archiving (MGA) [19]. The Ideal archiving method increases the convergence of the non-dominated solutions towards the Pareto-optimal front. On the other hand, the MGA approach obtains good diversity of solutions. The conclusion of the work highlights the main challenge of MaOPs: convergence to the true Pareto front and diversity of the obtained solutions covering the entire Pareto front. Recently, to overcome this limitation, researches proposed the use of multiple swarms. I-Multi algorithm [3] combines Ideal and MGA archivers in a multi-swarm search. This algorithm uses these two archiving methods at different phases of the process: first, the MGA is used in a single swarm, and after the obtained front is split and different swarms are executed in parallel using Ideal archiver. I-Multi algorithm presents good results in terms of convergence to the Pareto front and diversity of the obtained solutions on a set of MaOP benchmark problems.

These researches motivated our previous work [5] where the main goal was to explore other strategies of combination of these good elements in the design of algorithms for MaOPs. In [5], a possible alternative for the second phase of the I-Multi was investigated. The algorithm C-Multi was proposed whose main feature was to use an EDA [7]. EDAs have the capacity of achieving good convergence by generating solutions learned from the shape of the Pareto front. This work is an extension of the investigation presented in [5]. Our goal is to investigate if the performance of CMulti can be enhanced by a more appropriate choice of its components. To evaluate the behavior of the algorithm, we compare to I-Multi, an algorithm that is similar to C-Multi but does not incorporate EDAs as part of the optimization process and to MOEA/ D-DRA, a highly efficient method recently introduced in [9] as an improvement to MOEA/D [15].

## 3. Preliminaries

In this section, we first introduce some basic knowledge about many-objective optimization. Then, we briefly introduce the general mechanism of multi-objective particle swarm optimization (MOPSO) and I-Multi that are related to our work. Finally, we review basic knowledge about EDAs.

### 3.1. Many-objective optimization

Multi-objective optimization problems (MOPs) require the simultaneous optimization (maximization or minimization) of two or more objective functions. These objectives are usually in conflict, so these problems do not have only one optimal solution (as in single objective optimization problems), but a set of them. This set of solutions is usually found using Pareto optimality theory.

A general unconstrained MOP can be defined as optimizing $\vec{f}(\vec{x})=\left(f_{1}(\vec{x}), \ldots, f_{m}(\vec{x})\right)$, where $\vec{x} \in \Omega$ is an $n$-dimensional decision variable vector $\vec{x}=\left(x_{1}, \ldots, x_{n}\right)$ from a universe $\Omega$, and $m$ is the number of objective functions.

An objective vector $\vec{f}(\vec{x})$ dominates a vector $\vec{f}(\vec{y})$, denoted by $\vec{f}(\vec{x}) \leq \vec{f}(\vec{y})$ (in case of minimization) if and only if $\vec{f}(\vec{x})$ is partially less than $\vec{f}(\vec{y})$ i.e., $\forall i \in\{1, \ldots, m\}, f_{i}(\vec{x}) \leq f_{i}(\vec{y}) \wedge$ $\exists i \in\{1, \ldots, m\}: f_{i}(\vec{x})<f_{i}(\vec{y})$.

A vector $\vec{f}(\vec{x})$ is non-dominated if there is no $\vec{f}(\vec{y})$ that dominates $\vec{f}(\vec{x})$. If $\vec{f}(\vec{x})$ is non-dominated, $\vec{x}$ is Pareto optimal. The set of Pareto optimal solutions is called Pareto optimal set, and

the image of these solutions in the objective space is called Pareto front [10].

MaOPs are a type of MOPs that present more than three objective functions to be optimized simultaneously. Several studies have indicated that Pareto based algorithms scale poorly in MaOPs [2], [3], [4]. The main reason for this is that the number of nondominated solutions greatly increases with the number of objectives. As a consequence, the search ability of the algorithms is deteriorated because it is not possible to impose preferences for selection purposes.

### 3.2. MOPSO

PSO [6] is a stochastic meta-heuristic based on the movement of bird flocks looking for food, created to optimize nonlinear functions. In this method a swarm (population) of particles (solutions) moves across the search space (evolves) guided by personal and social leaders.

To expand the PSO to solve multi-objective problems, and create a multi-objective particle swarm optimization (MOPSO) [20] algorithm, some modifications are needed. The first of them is the creation of an external archive (repository) to store the better (non-dominated) solutions found so far, another modification is in the leader selection scheme, which has to choose from a set of equally good leaders according to some criterion. As the number of non-dominated solutions may become very large, an archiving method is needed to prune the repository and keep only a predefined number of solutions, discarding some non-dominated solutions according to its criterion.

A MOPSO that has shown very good results in the literature is the Speed-constrained Multi-objective PSO (SMPSO) [21]. It was noted that in some conditions the velocity of the particles in a MOPSO can become too high, generating erratic movements towards the limits of the decision space. To avoid such situations, SMPSO presents a velocity constriction mechanism based on a factor $\chi$ that varies based on the values of the influence coefficients of personal and global leaders ( $C_{1}$ and $C_{2}$ respectively). In SMPSO the (global) leader selection method uses a binary tournament based on the Crowding Distance metric from [22], and the archiving strategy also uses the Crowing Distance.

As the global leaders are selected from the repository, its size and content (managed by the archiving method) have a great impact on the results, especially in MaOPs, where the number of non-dominated solutions quickly increases. In [4] several archiving methods were compared in the optimization of MaOPs. The methods that do not limit the number of solutions in the Pareto set presented better results, and among the methods that limit the size of the archive, the Ideal [4] and MGA [19] stand out.

In Multi-level Grid Archiving (MGA) [19], when the repository becomes full, the objective space is divided into boxes and every solution in the archive has a box index. In a subsequent step, the domination relationships between the boxes are determined. If the new solution to be added belongs to one of the dominated boxes, it is not included in the repository, otherwise one of the solutions that have dominated box index is removed randomly. If there is no dominance relation between the boxes, the objective space is split again into smaller boxes until at least one dominated box is found. In this way, the number of boxes in MGA can change automatically at each iteration to adapt to the characteristics of the objective space.

In the Ideal [4] archiver, when the repository becomes full a process is triggered. Firstly, the ideal point of the repository is computed. The ideal point is a vector that has the best values for all objectives. Then, the Euclidean distance from each solution in the archive to the ideal point is computed. The solution that has the highest distance is removed.

### 3.3. I-Multi

Recently a new MOPSO called I-Multi [3] was proposed. I-Multi is a MOPSO designed to deal with MaOPs and that uses multiple swarms to cover different areas of the objective space. Its search procedure can be divided into two phases: diversity and multiswarm searches. In the first phase, a diversity search is performed using SMPSO [21] with the MGA archiver [19] to generate a set of well-distributed non-dominated solutions (basis front) for multiswarm initialization. Multi-swarm search begins using the basis front to assign a seed to each sub-swarm and around each seed (within a specified search region), a population of solutions is randomly generated to form a sub-swarm.

During a predefined number of iterations each sub-swarm runs independently, using the SMPSO with the Ideal archiver [4] to enhance its convergence. After that, the repository of each subswarm is integrated to the basis front so, only the non-dominated solutions regarding all repositories are kept. At the end of this process, the basis front is split into sub-swarms as before. This process of joining and splitting the fronts is called split iteration, and it is repeated a predefined number of times. This process enables an indirect communication between the sub-swarms.

In [3], three methods are presented to define the seed and the archive of each sub-swarm. In this work the I-Multi centroid is used, where the basis front is split into clustered groups (using a K-Means algorithm in the decision space) and the centroid of each group is chosen as seed for each sub-swarm. The solutions of each cluster are stored in the repository of each swarm. The number of clusters is defined as the same number of swarms. In this strategy, the archive is updated with all solutions clustered in the same cluster of the seed.

### 3.4. Estimation of distribution algorithms

In spite of the success of the Evolutionary Algorithms (EAs), they face difficulties in some real-world problems that exhibit characteristics like non-linearity, ill-conditioning and deception. Often, EAs' poor behavior in these problems can be explained by the fact that they do not properly consider the dependencies and relationships between decision variables and are not able to thoroughly exploit the information obtained so far.

The use of probabilistic graphical models (PGMs) [23] in EAs offers a systematic way of acquiring and representing problem regularities. In this approach, and in order to generate new solutions, the traditionally applied genetic operators are replaced by learning and sampling from probabilistic models. Machine learning methods are applied to learn the PGMs from the selected solutions, and sampling strategies serve to generate the new solutions from the models. The incorporation of probabilistic modeling in EAs has led to a new paradigm known as competent EAs or EDAs [24], [7].

General EDAs iterate three steps until some termination criterion is satisfied: select good solutions from a population, estimate the probability distribution from the selected individuals (learn a model) and generate new solutions (sample) from the estimated distributions (model).

The EDA used in this work is the real-coded Bayesian optimization algorithm (rBOA) [25], a continuous, real-coded version of the Bayesian optimization algorithm (BOA) [26]. BOA is one of the most efficient and extensively applied EDAs [27], able to represent higher order dependencies between discrete variables by means of Bayesian networks. rBOA inherits some of the suitable attributes of BOA. Our choice of rBOA was also motivated by its good results in previous applications and extensive documentation. Its pseudocode is presented through Algorithm 1.

## Algorithm 1. rBOA.

//Step 1: Initialization
$P=$ generateRandomPopulation()
for $i=1$ to $I t$ do
// Step 2 : Selection
$S=$ selectPromisingCandidates $(P)$
// Step 3 : Learn
$M=$ learnProbabilisticModel $(S)$
// Step 4 :
$O=$ generateOffspring $(M)$
// Step 5 :
$P=$ generateNewPopulation $(O, P)$
end for
return bestFrom $(P)$

In this algorithm, firstly a population $P$ is randomly generated, then for a predetermined number of iterations (It) promising candidate solutions are selected from the whole population to be used in the learning phase to create a probabilistic model $M$. A set of offspring solutions is sampled from this probabilistic model and the new population is updated based on the previous one and the set of new offspring solutions. At the end of the iterations, the better solution from the population is returned as a result of the algorithm.

Different EDAs can be characterized by the method of learning a probabilistic model (Step 3) and its performance is affected directly by the efficiency of this model learning. In general, the learning of probabilistic models consists of two tasks: model selection and model fitting. Model selection determines the structures of promising probabilistic models and model fitting estimates the conditional probability distributions with regard to the found structures [28,29].

rBOA model selection obtains a Bayesian factorization, which is represented by a directed acyclic graph called Bayesian factorization graph where the nodes and edges identify the corresponding variables and its conditional dependencies respectively. Two components determine the model selection step: a scoring metric and a search procedure. The scoring metric assesses the quality of the structure of the Bayesian factorization graph and the search procedure efficiently traverses the space of all feasible structures for finding the best one with regard to the given scoring metric. BOA and rBOA employ a Bayesian Information Criterion (BIC) [30] as the scoring metric and an incremental greedy algorithm as the search procedure [25].

In rBOA model fitting, a set consisting of a node and its parents in the Bayesian factorization graph represents a component subproblem of decomposable problems. For efficiency, maximal connected sub-graphs of a Bayesian factorization graph are considered as sub-problems and must be independently fitted. Mixture models are employed and the aim of using them is twofold: comprehending the type of dependency between variables and traversing the search space effectively. Each mixture component can model the linearity of the variables, thus they can approximate any type of dependency by a combination of piecewise linear interaction models [25].

## 4. Competent Multi-swarm

This section presents a hybrid algorithm called Competent Multi-swarm (C-Multi). The feature that distinguishes C-Multi from the other previously introduced multi-swarm algorithms is
the incorporation of a model-based search component implemented using rBOA [25]. C-Multi combines the strengths of two efficient algorithms: I-Multi [3] and rBOA. I-Multi presents a high diversity of solutions through the use of multiple swarms to spread its particles across the front. rBOA is able to achieve a good convergence by generating solutions learned from the shape of the Pareto front. By hybridizing these two algorithms, C-Multi is able to have a better performance, especially in hard problems.

As the project of I-Multi, the project of C-Multi is based on two phases: the first uses a unique PSO to discover the different regions of the Pareto front. The second phase uses multiple swarms to specialize on a dedicate part. On each swarm, an EDA is used to focus on convergence to its allocated region.

In the first phase, a traditional SMPSO [21] with the MGA [19] archiver is used to obtain a diverse set of non-dominated solutions (basis front). Next, the multi-swarm phase begins by splitting the basis front in NS sub-fronts (set as parameter) by using the KMeans algorithm. Each sub-swarm is initialized with a seed (centroid of the cluster) and the non-dominated solutions contained in a sub-front. This seed is used to define the bounds to truncate the solutions (if necessary) to make sure each sub-swarm will explore only a limited region avoiding overlaps.

In each loop of the multi-swarm phase, the non-dominated solutions of each sub-swarm are used by rBOA to learn a model. Next, the model is sampled to create a new population (or replace a previous one) for the sub-swarm. Then, the population of the sub-swarm is added to the front if the criteria of the archiver are satisfied, ending the loop.

## Algorithm 2. C-Multi.

//Phase 1: Diversity search
$F_{\mathrm{b}}=$ Run-MGA-SMPSO( )
//Phase 2: Multi-swarm search
for $s=1$ to $S I$ do
$\vec{F}=$ SplitFront $\left(F_{b}\right)$
for $k=1$ to $N S$ do
for $i=1$ to $I t$ do
$\mid P_{k}=\operatorname{rBOA}\left(F_{k}\right)$
$\mid$ Truncate $\left(P_{k}\right)$
Evaluate $\left(P_{k}\right)$
$\mid F_{k}=\operatorname{Archiver}\left(P_{k}\right)$
endfor
endfor
$F_{b}=$ Non - dominated $(\vec{F})$
end for
return $F_{b}$

During the multi-swarm phase, the loops above are interrupted a predefined number of times (SI, set as parameter) to perform a split iteration. In this procedure, the fronts of all sub-swarms are merged into a single basis front (only the non-dominated solutions concerning all fronts are kept) that is split as before. Then, the multi-swarm phase is restarted. The goal of the split iterations is to allow an indirect communication between the sub-swarms in addition to eliminating duplicated solutions across the fronts. A pseudo-code of C-Multi is presented through Algorithm 2.

In this algorithm, firstly the diversity phase is conducted by running the SMPSO algorithm with the MGA archiver for a predefined number of iterations to obtain a well diversified basis front $\left(F_{b}\right)$.

Next the multi-swarm stage begins. This stage is characterized by $S I$ split iterations, where the basis front $F_{b}$ is split into $N S$

sub-fronts ( $\vec{F}=\left(F_{1}, \ldots, F_{N S}\right)$ ) by using a K-Means algorithm in the decision space. Each of these sub-fronts ( $F_{k}$ ) is composed of a set of non-dominated solutions and a seed (the centroid of the cluster).

Then, for each front, during a predetermined number of iterations, the following procedure is executed: a model is learned for each front $F_{k}$; a new population $P_{k}$ is sampled from this model and its decision vector is truncated (if necessary) to stay within the search region around the seed; the population is evaluated through the objective function; and finally the front $F_{k}$ is updated with the better solutions from the population.

After all sub-swarms were executed independently for several iterations (It), a new split iteration begins. The non-dominated solutions from all the sub-swarms are joined in the basis front $F_{b}$, which is split again into NS sub-swarms and the process repeats. At the end of the algorithm, $F_{b}$ containing all the non-dominated solutions regarding all fronts is returned as result from the algorithm.

The structure of C-Multi is basically the same as the I-Multi, however in the multi-swarm search, instead of using the SMPSO, the rBOA learning method is used to create a model and sample new particles. This replacement of the update method is used to increase the convergence capacity in this stage of the search, causing a moderate increase in the computational cost.

## 5. Empirical study

This session presents the empirical studies conducted involving the C-Multi algorithm. In the experiments, we perform an analysis of some important components of C-Multi, as the archiver used in the multi-swarm stage and the number of sub-swarms. Furthermore the performance of our algorithm is compared to its base algorithm I-Multi [3], and to the state-of-the-art algorithm, winner of the CEC 2009 MOEA contest MOEA/D-DRA [9].

### 5.1. Experimental setup

For the study of the impact of the components of the algorithm, i.e., the archiver (Section 5.2) and the number of swarms (Section 5.3), the problems WFG1, WFG4 and WFG6 were chosen because they are representative of the WFG [31] family of benchmark problems.

The comparison of C-Multi to I-Multi and MOEA/D-DRA used the entire WFG family of problems to analyze the performance of the algorithms in different scenarios. A summary of the characteristics of the problems used is presented in Table 1 adapted from [32]. The WFG test suite poses a significant challenge for algorithms to obtain a well converged and well distributed solution set. These benchmark problems can scale both in number of objectives and in number of decision variables, also the true Pareto optimal front is known.

Table 1
Characteristics of problems.
Table 2
Parameters.
The algorithms were tested using different numbers of objectives to verify how they perform as the number of objectives scales up. The main parameters used for the algorithms are summarized in Table 2.

The parameters $C_{1}$ and $C_{2}$, that control the effect of the personal and global best particles in the velocity respectively, are set according to the recommendation given in the original SMPSO paper [21], by changing these values is possible to control the trade-off between convergence and diversity in the algorithm. The number of decision variables was set according to the recommendation given for the problems in [31], decreasing or increasing the number of decision variables is an easy way of making the problem easier or harder respectively. The complexity factor of the BIC score controls how much the algorithm penalizes the complexity of a probabilistic model, hence impacts on the trade-off between the computational cost and efficiency of the model. The complexity factor of BIC score $\lambda$ as well as the threshold used in the BEND leader algorithm (used for model fitting) is set for rBOA according to the values proposed in its original paper [25]. The leader threshold of BEND algorithm used for model fitting impacts the number of clusters used in this stage, and can impact the ability of the model in efficiently modeling the dependencies between variables.

The number of split iterations as well as the multi-swarm region size was calibrated in [3] and we use the best values found, since they are representative for C-Multi as well. A split iteration can be beneficial for the search, since it removes dominated and repeated solutions as well as promoting communication among the swarms, but it can be prejudicial to the swarm, since it may reduce the number of solutions contained in each swarm, hence there are less particles to be used as guide on the search (on I-Multi) and less solutions available to be learned (on C-Multi). Regarding the multi-swarm region size, if it is increased, more overlaps are expected, hence more repeated solutions may arise among the swarms, and each swarm need to focus its search on a larger area, weakening its specialization ability, on the other hand if we decrease this value, it can create "holes" on the front, or areas that are not covered by any swarm.

The number of iterations (initial and total), the initial size of the population, the maximum size of the repositories and the total number of particles also were set as proposed in [3] since these values can be considered a good compromise between the search exploration capabilities of PSO and its computational cost. Regarding the number of particles per swarm, if the total number is not divisible by the amount of sub-swarms, the remaining particles are distributed among the sub-swarms.

To assess the quality of the Pareto fronts generated by each algorithm, two well-known quality indicators are used: The modification of the Inverted Generational Distance (IGD) known as $I G D_{g}$ [33], and the hypervolume [34]. Up to eight objectives the exact hypervolume calculation was used, and for ten objectives an

approximately 1000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,00

![img-0.jpeg](img-0.jpeg)

Fig. 1. Better approximation fronts obtained using different archivers and the true front.

Since we obtained different results according to problem and objective numbers, is hard to take overall conclusions, hence we included in Tables 7 and 8 the Friedman ranks obtained for the

Table 5
Kruskal-Wallis ranks of the $I G D_{p}$ for different numbers of sub-swarms.

overall analysis of the algorithms. In these tests, the average of the 30 independent runs of each subproblem (problem/objective number) is considered. A significance level of $5 \%$ is considered for this test as well.

These tables indicate that in general when considering the $I G D_{p}$ indicator, the more swarms the better, since except from two cases (60-70 and 80-90), the Friedman ranks decrease as the number of swarms increase, also the better final ranking is obtained with 100 swarms.

Regarding the hypervolume indicator, we see a similar effect, but towards 40 swarms, where the ranks increase as the number of sub-swarms distances from 40, except between 50 and 70. Also, the best final ranking is obtained with 40 swarms.

It is known that $I G D_{p}$ and hypervolume have different characteristics, as demonstrated in this section. Since each one points us to a different setting, in this work we followed the results obtained using the hypervolume due to its stronger mathematical properties.

### 5.4. C-Multi vs. I-Multi vs. MOEA/D-DRA

In this section we compare C-Multi to I-Multi [3] and MOEA/DDRA [9], a state-of-the-art algorithm winner of the CEC 2009 MOEA contest. In this comparison, the entire WFG family of benchmark problems was used to provide an overview of the behavior of the algorithms as the number of objectives scales up.

Table 6
Kruskal-Wallis ranks of the hypervolume for different numbers of sub-swarms.

Table 7
Overall Friedman ranks of the $I G D_{p}$ for different numbers of sub-swarms.

Table 8
Overall Friedman ranks of the hypervolume for different numbers of sub-swarms.

Since the CD archiver had the best overall results for C-Multi, we use it to prune the solutions in the multi-swarm phase of C-Multi. I-Multi used the Ideal archiver as it was designed. In order to keep a fair comparison, we used the same number of sub-swarms (40), for C-Multi and I-Multi. Also we used as stop criterion for all three algorithms the number of fitness evaluations, fixed in 85100 . The results from this experimental study are presented through Tables 9 and 10 that present the Kruskal-Wallis ranks of the $I G D_{p}$ and hypervolume respectively.

Table 9
Kruskal-Wallis ranks of the $I G D_{p}$ for C-Multi, I-Multi and MOEA/D-DRA.
Regarding the $I G D_{p}$ results, for three objectives C-Multi had competitive performance, achieving the best rankings in problems WFG4, WFG6 and WFG9 and tying with I-Multi on WFG5. Besides tying with C-Multi on WFG5, I-Multi only achieved superior performance on WFG2. MOEA/D-DRA outperformed both algorithms on problems WFG1, WFG3, WFG7 and WFG8. For five objectives the results of C-Multi were better, outperforming the other algorithms in problems WFG4, WFG5, WFG7 and WFG8 and tying with I-Multi on WFG1, WFG2 and WFG9. I-Multi, besides tying to C-Multi, outperformed the other algorithms on WFG6. MOEA/DDRA only had better rankings on WFG3.

For eight objectives, C-Multi had better rankings than the other algorithms on WFG4, WFG5, WFG7 and WFG8, and tied with IMulti on WFG2 and WFG6. I-Multi, besides tying with C-Multi, achieved better performance on WFG1, WFG3 and WFG9. MOEA/ D-DRA did not outperformed the others in any problem. For ten objectives, C-Multi only lost to I-Multi on problems WFG1 and WFG9, and tied to it on WFG3 and WFG6. MOEA/D-DRA did not have the best rankings in any problem.

Fig. 2 shows examples of boxplots for the $I G D_{p}$ results obtained by the algorithms. Due to lack of space we only included boxplots for the problem WFG4. From this figure, we can see that for all the numbers of objectives, in general, C-Multi obtained better (smaller) $I G D_{p}$ results, followed closely by C-Multi. MOEA/D-DRA did not achieve good results regarding $I G D_{p}$ on this problem.

Considering the hypervolume, for three objectives, C-Multi outperformed the other algorithms on WFG6 and WFG9. I-Multi had better rankings on WFG4 and tied to MOEA/D-DRA on WFG5. In the remaining problems, MOEA/D-DRA outperformed both algorithms. For five objectives, the three algorithms tied on WFG9, I-Multi achieved better results on WFG6, and MOEA/D-DRA outperformed I-Multi and C-Multi in the remaining problems. For eight and ten objectives, MOEA/D-DRA presents very good results, outperforming both algorithms in all problems.

Table 10
Kruskal-Wallis ranks of the hypervolume for C-Multi, I-Multi and MOEA/D-DRA.
Fig. 3 shows examples of boxplots for the hypervolume results obtained by the algorithms. Due to lack of space we only included boxplots for the problem WFG4. From this figure we can see that in general MOEA/D-DRA had better (higher) hypervolume results, except for three objectives, where I-Multi performed better. For three and five objectives, I-Multi outperforms C-Multi, however for eight and ten objectives C-Multi presents better results than IMulti.

Considering all the results presented, we can conclude that despite the excellent performance of the state-of-the-art MOEA/DDRA regarding the hypervolume, C-Multi can be a very competitive algorithm if we take into account a different quality indicator like $I G D_{p}$. Moreover, in general C-Multi achieved competitive results compared to I-Multi on hypervolume, and outperformed it on $I G D_{p}$.

A possible explanation for this poor performance on hypervolume is that even using an archiver that benefits the diversity, parts of the fronts are not being properly covered by C-Multi, specially the extremes. In general, the results obtained can be considered promising, pointing to the usefulness of keep investigating the hybridization of MOPSO with EDAs for many-objective optimization.

## 6. Conclusion

In this paper, we have built on a previous study where a hybrid algorithm called C-Multi was introduced. C-Multi was designed to meet two conflicting goals in MaOPs: convergence to the Pareto front by using an EDA, and diversity of the solutions by using multi-swarms. In the previous paper, despite presenting good results in some difficult problems, C-Multi had overall poor performance.

To overcome the limitation observed on C-Multi, we have investigated in this paper which is the role of the archiving method and the number of swarms, and how an appropriate selection of these components can enhance the searching capabilities of the algorithm. We have conducted a detailed empirical analysis of the effect of these components.

For the archiving method, we have analyzed how three different archivers (CD, Ideal and MGA) influence the multi-swarm phase of the algorithm. This study indicated that using the Ideal archiver generates the unwanted effect of creating "holes" in the resulting front. Therefore, it was concluded that it is better to use an archiver like CD that guarantees the maintenance of generated extreme solutions of the swarms favoring the diversity of the solutions kept in the archiver.

The second experimental study involved investigating the effect of the number of sub-swarms used in the multi-swarm phase of the search. We used ten different values for the number of sub-swarms: $10,20,30,40,50,60,70,80,90$ and 100 . This study obtained conflicting results regarding the indicators used, hence
![img-1.jpeg](img-1.jpeg)

Fig. 2. $I G D_{p}$ boxplots for WFG4.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Hypervolume boxplots for WFG4.
we configured the algorithm according to the most widely accepted indicator, in this case hypervolume.

Finally, experiments were conducted to compare C-Multi to IMulti and the state-of-the-art MOEA/D-DRA. To consider a variety of difficult optimization scenarios, the entire WFG family of problems for $3,5,8$ and 10 objectives, was used. The results obtained indicate that despite not being able to outperform MOEA/D-DRA in most cases regarding hypervolume, C-Multi had very good results when considering the $I G D_{p}$ indicator. Moreover, C-Multi was able to outperform I-Multi in most cases regarding $I G D_{p}$, and presented competitive results according to hypervolume. A possible explanation for this poor performance on hypervolume is that part of the fronts are not being properly covered by C-Multi, specially the extremes. However, considering the results obtained, we can confirm our original hypothesis concerning the improvement of C-Multi's performance by an appropriate choice of the archiving strategy and the number of sub-swarms.

These results encourage further research on the hybridization between EDAs and MOPSOs to take advantage of their different capabilities to design more adaptive algorithms, able to explore the diverse scenarios that can be found in real-world manyobjective optimization. Future works include using other EDAs to further improve convergence and the combination of decomposition and reference points to promote diversity, specially in the extremes of the search space.
