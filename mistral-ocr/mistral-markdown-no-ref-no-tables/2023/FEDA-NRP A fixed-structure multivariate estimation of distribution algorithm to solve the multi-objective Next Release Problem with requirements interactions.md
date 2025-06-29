# FEDA-NRP: A fixed-structure multivariate estimation of distribution algorithm to solve the multi-objective Next Release Problem with requirements interactions 

Víctor Pérez-Piqueras, Pablo Bermejo ${ }^{\circ}$, José A. Gámez<br>Universidad de Castilla-La Mancha, Escuela Superior Ingeniería Informática s/n, Albacete, 02071, Spain

## A R TICLE INFO

MSC:
68 T 20
Keywords:
Next Release problem
Estimation of distribution algorithms
Evolutionary multi-objective search
Search-based software engineering
Bayesian networks
Agile

## A B STRACT

In the development of a software product, the Next Release Problem is the selection of the most appropriate subset of requirements (tasks) to include in the next release of the product, such that the selected subset maximises the overall satisfaction of the stakeholders and minimises the total cost. Furthermore, in most cases, requirements or tasks cannot be developed independently, as there are dependencies between them, which must be respected in the selection for the next release. In this paper, we approach the Next Release Problem as a constrained bi-objective optimisation problem. The main contribution is the design of an Estimation of Distribution Algorithm that exploits domain knowledge, i.e. the dependencies between the requirements, to define the structure of a Bayesian network that models the relationships between the binary variables (requirements) to be optimised. The use of a Bayesian network with a fixed structure reduces the complexity of the search process, since it is unnecessary to learn the structure at each iteration of the algorithm. Moreover, it ensures that the sampled individuals are always valid with respect to the required dependencies. The second main contribution is the generation of a corpus of synthetic datasets with cost estimations derived from agile and classic management methodologies. Standard multi-objective metrics are computed in order to assess our proposal and compare it with other evolutionary multi-criterion optimisation algorithms, determining that it is the optimal choice when dealing with complex datasets.

## 1. Introduction

Software projects, both new development and enhancement projects, go through a series of phases during their life cycle. Among these phases are requirements elicitation, requirements selection, design, implementation, testing, deployment, etc. Many of these steps may be tedious, difficult to succeed in or very time-consuming; thus, a new set of techniques has been developed over the last two decades in order to alleviate these problems. Concretely, the Search-Based Software Engineering (SBSE) paradigm (Harman et al., 2012a) refers to the reformulation of software engineering problems into new or traditional search-based optimisation algorithms, which find optimal or near-optimal solutions in a search space. The main reason for this reformulation is that many problems in software engineering need to optimise two or more objectives, resulting in computationally intractable problems which do not allow for an exhaustive search. The definition of software engineering problems as optimisation ones opens the door to the use of a plethora of classic and novel methods:, such as genetic algorithms (Katoch et al., 2021), particle swarm optimisation (Gad, 2022), ant colony optimisation (Dorigo et al., 2006) and estimation of distribution algorithms (Larrañaga and Lozano, 2001).

This work deals with the software development phase of requirements selection, known as the Next Release Problem (NRP) (Bagnall et al., 2001; Iqbal and Alam, 2021), one of the five most common Search-Based Software Engineering (SBSE) problems (Chen and Li, 2023). The NRP addresses the task of selecting a subset of requirements to be delivered in the next release or increment of the product, optimising certain objectives while fulfilling given restrictions. The NRP needs to be solved under any software project management methodology; that is, requirements selection is a problem to be solved in both classic (PMI, 2021; Imani, 2017) and agile (Beck, 1999; Schwaber and Sutherland, 2020) methodologies. In a classic or plan-driven approach, a large and complete set of requirements is previously elicited and then, for each release of the final product, a subset of these requirements needs to be selected under certain restrictions. When the development of a software product is being managed in an agile or value-driven manner, the NRP needs to be solved more frequently (at least once per increment) and, although the cardinality of the requirements set could be lower than in classic methods, this set is updated continuously and an NRP solution is thus not valid after a few days or weeks. Furthermore, some projects

[^0]
[^0]:    ${ }^{8}$ Corresponding author.
    E-mail address: Pablo.Bermejo@uclm.es (P. Bermejo).

scale agile teams and the set of requirements grows as large as in classic projects but still with the same update rate.

The basic formulation of the NRP mixes the objectives to be optimised, commonly minimising cost and maximising satisfaction, into a single objective in order to facilitate or simplify the search process. A budget $B$ is then used to limit the search, establishing as many instances of the problem for the same dataset as values are set for $B$. Subsequently, NRP started to be addressed as a multi-objective problem (MONRP) (Zhang et al., 2007; Durillo et al., 2009; Geng et al., 2018; Rahimi et al., 2022), in such a way that objectives are not mixed. Solutions are then collected in Pareto fronts using the dominance criteria, and returned to the decision-maker in order to evaluate which fits best, given the current situation of the project. In the MONRP version of the problem, the search with a budget $B$ is not typically limited, mainly because solution objectives are not merged, so the decision-maker can visually choose the desired satisfaction/cost ratio.

The method to deal with search objectives is not the only feature that distinguishes the formulation of NRP; the management of requirements dependencies is also particular (del Sagrado et al., 2015; Hamdy and Mohamed, 2019). Some planned requirements may imply the previous or posterior development of other requirements, or they may be mutually exclusive. Thus, the NRP does not only need to maximise satisfaction while minimising cost, but this must also be done while respecting certain constraints between requirements. This makes it a NP-hard problem, as proven in Almeida et al. (2018), and so it has been commonly solved with metaheuristic optimisation search algorithms, such as ACO (del Sagrado et al., 2015), PSO (Hamdy and Mohamed, 2019), GRASP (Pérez-Piqueras et al., 2022), Simulated Annealing (Baker et al., 2006) and NSGA-II (Durillo et al., 2011). Non metaheuristic approaches based on integer programming (Dong et al., 2022) and pursuing anytime behaviour (Domínguez-Ríos et al., 2019) have also been proposed. However, almost no attention has been focused on the use of Estimation of Distribution Algorithms (EDAs) (Larrañaga and Lozano, 2002). This is striking in view of the results obtained by this family of methods in a related problem such as feature selection (Guyon and Elisseeff, 2003; Abdollahzadeh and Gharehchopogh, 2022), both in its singleobjective (Bermejo et al., 2011) and multi-objective versions (Maza and Tosabria, 2019). In fact, it was only very recently that the first approach to the NRP using EDAs appeared (Pérez-Piqueras et al., 2023), but the proposal is limited to the use of univariate EDAs, which cannot explicitly deal with requirements dependencies.

In this work, we propose the FEDA-NRP (Fixed-structure EDA) algorithm, which takes advantage of the EDA search properties and of the fact that all dependencies among requirements in the Next Release Problem are known in advance. Furthermore, the preferred application niche for FEDA-NRP will be complex problems, with a large number of requirements and dependencies between them, since this is where exploiting domain knowledge directly in the algorithm will be a major advantage. The main contributions of this work are the following:
(i) The development of a multivariate estimation of distribution algorithm (FEDA-NRP) to cope with the constrained bi-objective next release problem. The prior knowledge domain is used to construct a Bayesian network that models the requirement dependencies, thus avoiding the structural learning phase and accelerating the efficiency of the algorithm. Furthermore, all individuals sampled from this model are valid with respect to the constraints provided (dependencies).
(ii) The generation of a public corpus of synthetic datasets with different complexities in the number of requirements and dependencies, and different project management context (classic and agile cost estimation). We hope that this corpus can be used as a reference in future studies, so it is available in a public repository. ${ }^{1}$

[^0](ii) A comprehensive comparative experimental study to assess the strengths and weaknesses of FEDA-NRP with respect to state-of-the-art algorithms dealing with the bi-objective next release problem, which follows the guidelines and suggestions from recent literature for fair comparison of multi-objective search algorithms (Ishibuchi et al., 2022) and comparing the most suggested quality metrics (Li et al., 2020). It should be noted here that all algorithms are adapted in the sampling or selection phase to respect the constraints (dependencies) provided.
(iv) The code of FEDA-NRP and the rest of the algorithms used in the comparison are publicly available, as well as the scripts needed to reproduce the experiments included in this work. ${ }^{2}$

In the following sections, we will explain a number of concepts in greater detail: We introduce the single and multi-objective NRP (Section 2.1) and then the management of requirements dependencies (Section 2.2). Next, in Section 3 we present an overview of the state of the art, citing classic and recent related works. Then, in Section 4 we present our proposed method FEDA-NRP, giving further detail with an example in Section 4.3. Our experimental framework is decomposed into several parts: First, Section 5.1 presents the process to sample a new corpus of public datasets; Sections 5.4, 5.2 and 5.5 provide the fine-grained details about the evaluation metrics, algorithms and experiment configuration. Reproducibility information is described in Section 5.6. Finally, Section 5.7 presents the quality metrics and visual indicators computed to assess the goodness of the compared algorithms, and, in Section 6, we summarise the main conclusions and propose future work.

## 2. The next release problem

In this section, we introduce some necessary concepts related to the NRP. First, we define the Multi-Objective NRP (MONRP) and then explain the concept of requirements dependencies or interactions. We introduce different types of dependencies, which are the most common, and also how to convert some types into others. We also cite relevant works, some of which do not deal with the interaction constraints and others that do.

### 2.1. The (multi-objective) next release problem

The Multi-Objective NRP (MONRP) can be defined by a set $R=$ $\left\{r_{1}, r_{2}, \ldots, r_{n}\right\}$ of $n$ candidate software requirements, which are suggested by a set $C=\left\{c_{1}, c_{2}, \ldots, c_{m}\right\}$ of $m$ clients. In addition, a vector of costs or efforts is defined for the requirements in $R$, denoted $E=\left\{e_{1}, e_{2}, \ldots, e_{n}\right\}$, in which each $e_{i}$ is associated with a requirement $r_{i}$ (Harman et al., 2012b). Each client has an associated weight, $W=$ $\left\{w_{1}, w_{2}, \ldots, w_{m}\right\}$, which measures its importance. Moreover, each client gives an importance value to each requirement, depending on their needs and goals with respect to the software product being developed. Thus, the importance that a requirement $r_{j}$ has for a client $c_{i}$ is given by a value $v_{i j}$, such that a zero value represents client $c_{i}$ having no interest in implementation of the requirement $r_{j}$. An $m \times n$ matrix is used to hold all the importance values in $c_{i j}$. The overall satisfaction provided by a requirement $r_{j}$ is denoted as $S=\left\{s_{1}, s_{2}, \ldots, s_{n}\right\}$ and is measured as a weighted sum of all importance values for all clients, as expressed in Eq. (1):
$s_{j}=\sum_{i=1}^{m} w_{i} \times v_{i j}$
The MONRP involves finding a decision vector $X$, which includes the requirements to be implemented for the next software release, $X \subseteq$ $R$, which contains the requirements that maximise clients satisfaction and minimise development efforts.

[^1]
[^0]:    1 https://doi.org/10.5281/zenodo.7247877 (Pérez-Piqueras et al., 2022).

[^1]:    2 https://github.com/UCLM-SIMD/MONRP/tree/eng_app_si23.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Pareto Front with five non-dominated solutions in MONRP.

The MONRP objectives are expressed in Eqs. (2) and (3):
$M$ asimise $S(X)=\sum_{j \in X} s_{j}$
$M$ inimise $E(X)=\sum_{j \in X} e_{j}$
In addition, requirements in vector $X$ might have to satisfy the constraints of the problem. These constraints are related to the interactions between requirements and to the total effort or budget of the development.

Defining the NRP as a multi-objective (cost-value) optimisation problem has the advantage that a single solution to the problem is not sought, but rather a set of solutions, the Pareto front. In this way, any solution from this set can be chosen by the decision-maker, according to the conditions, situation and restrictions of the software product development.

The Pareto front is a vector or set of configuration values for the decision variables that satisfies the problem constraints and optimises the objective functions. Thus, the Pareto front contains a set of solutions that are not dominated by any other, named non-dominated solutions (NDS). Given a solution vector $x=\left[x_{1}, x_{2}, \ldots, x_{j}\right]$ where $j$ is the number of problem objectives, it dominates a solution vector $y=\left[y_{1}, y_{2}, \ldots, y_{j}\right]$ if and only if $y$ is not better than $x$ for any objective $i=1,2, \ldots, j$. In addition, there must exist at least one objective $x_{i}$ that is better than the corresponding $y_{i}$ of $y$. Conversely, two solutions are non-dominated as long as neither of them dominates the other.

A common practice consists on maintaining an archive of all the non-dominated solutions ( $N D S_{\text {archive }}$ ) found during the search. Solutions in $N D S_{\text {archive }}$ are then used for the evaluation of quality metrics in order to assess the algorithm. Fig. 1 is an example of a Pareto front with an NDS set for MONRP, in which both objectives are normalised so that their value range is $[0,1]$. The value for Satisfaction is reversed so that it may be interpreted in the same sense as Cost; thus, point $(0,0)$ is the ideal point and the nearer the solutions are to this point, the better they are.

### 2.2. Requirements dependencies in NRP

Software development commonly deals with requirements which are dependent on one another, mostly in an inclusive or sometimes in
an exclusive way. When solving the NRP (either in the basic or MONRP version), these dependencies also need to be taken into account. In Carlshamre et al. (2001), authors define several types of dependencies or interactions from the review of several software projects. In del Sagrado et al. (2015), they are paraphrased in the following set of 5 types of requirements interactions:

- Implication (requires; $r_{i} \Rightarrow r_{j}$ ): a given requirement must be implemented before implementing another.
- Combination (AND; $r_{i} \odot_{j}$ ): two requirements should be included in the same release.
- Exclusion (OR): implementing one requirement excludes another.
- Revenue: developing a given requirement changes the value or satisfaction of other requirements.
- Cost: developing a given requirement changes the cost of other requirements.

Carlshamre et al. (2001) suggests that implication and combination interactions are the most important types, and should thus be tackled with higher priority than exclusion and non-functional dependencies. A combination dependency in software development has more of a semantic need than a technological one; that is, sometimes it makes more sense to present two new functionalities together. It is the requires or implication which expresses a hard dependency for technological reasons. In terms of NRP, this means that, having an implication dependency $r_{i} \Rightarrow r_{j}$, if at some step the search algorithm selects $r_{i}$ then $r_{j}$ must also be selected. Since NRP solutions do not rank the selected requirements, making sure that both requirements are selected is enough to solve the implication. Moreover, in order to fulfil an AND dependency $r_{i} \odot r_{j}$ (see Fig. 2(a)), this can be applied in practice as having a new requirement $r_{i, j}$ (Fig. 2(b)), which stands as the delivery of the two requirements together, as done in del Sagrado et al. (2015). Furthermore, in the case of having $r_{i} \odot r_{j}$ and $r_{j} \odot r_{k}$, we can associate the three requirements first as $r_{i, j} \odot r_{k}$ and then join them as $r_{i, j, k}$. Note that as this group of variables is then managed as a single one, it has the side effect of reducing the problem dimensionality. Finally, after transforming this combination interaction, the implications from parents and to children of the resulting requirement is the union of the original ones (Fig. 2(c)). Thus, when designing the search algorithm, the most practical decision is to make it capable of dealing with implication dependencies.

## 3. Related work

The NRP was first formulated by Bagnall et al. (2001). In the current definition of NRP, a subset of requirements has to be selected, with the goal being to meet the clients' needs, minimising development effort and maximising clients' satisfaction. They applied a variety of metaheuristics techniques, such as simulated annealing, hill climbing and GRASP, but combining the objectives of the problem into a singleobjective function. Later, Baker et al. (2006) also solved the NRP as a budget-constrained single-objective version of the problem, similarly to the feature subset selection problem.

Other studies started formulating the NRP as a multi-objective optimisation (MOO) problem, with the first being the proposal of Zhang et al. (2007). This new formulation, known as the Multi-Objective Next Release Problem (MONRP) or Cost-Value Model, is based on Pareto dominance (Coello Coello et al., 2007). In this approach, each objective is tackled separately, exploring the non-dominated solutions (NDS). Many works tackling the MONRP make use of the Pareto Archived Evolutionary Strategy (PAES) (Knowles and Cornes, 1999), as in Chaves-Gonzalez et al. (2015), Chaves-González et al. (2015) and Marghny et al. (2022), consisting of maintaining a $N D S_{\text {archive }}$ found during the search. Finkelstein et al. (2009) also applied multi-objective optimisation considering different measures of fairness.

From the most recent reviews in SBSE, regarding Ramírez et al. (2020), only an EDA application to software testing (Sagarna and

![img-1.jpeg](img-1.jpeg)

Fig. 2. Example of the transformation process for combination interactions.

Lozano, 2005) is referenced; and in Gupta et al. (2016) and Alba et al. (2021) EDA approaches are neither mentioned nor matched to any solution of the NRP. To the best of our knowledge, the first work using EDAs to solve the NRP is Pérez-Piqueras et al. (2023), where the authors solve the NRP with the UMDA and PBIL univariate EDA. In that study, both EDAs outperform genetic algorithms (NSGA-II), and this advantage increases as the number of requirements in the problem instances also gets larger.

Most NRP works, such as Durillo et al. (2011), Jiang et al. (2010) and Coello Coello et al. (2007), do not treat requirements dependencies. The first approaches that solve the single-objective NRP handling dependencies are authored by del Sagrado et al. (2011) and Souza et al. (2011), adapting global search algorithms based on Ant Colony Systems. Both proposals operate by representing dependencies in a graph that is also used to perform the search. In subsequent works, del Sagrado et al. (2015) also tackled requirements dependencies in the multi-objective version of the NRP, by formally defining graphs which represent all dependency types, reconstructing them, so that, in the end, only implication dependencies are present in the graph. Thus, during the search, they remove connections between a selected requirement and its $O R$-related requirements. Apart from ACO, other swarm-based approaches have been considered to deal with the MONRP by using implications dependencies, such as particle swarm optimisation (Hamdy and Mohamed, 2019) and artificial bee colony (Chaves-Gonzalez et al., 2015).

## 4. FEDA-NRP: a multi-objective EDA capable of using the a priori known structural relations between requirements dependencies for the NRP

In Pérez-Piqueras et al. (2023), the authors use univariate EDAs to cope with the MONRP. However, univariate EDAs are unable to explicitly manage requirement interactions, i.e. dependencies. This drawback can be overcome by using more complex EDA models, which explicitly manage dependencies between problem variables. In fact, n-variate EDAs (e.g. EBNA Larrañaga et al., 2000 and BOA Pelikan et al., 1999)
learn a probabilistic graphical model at each iteration in order to capture the underlying dependencies in the current population. However, this would be needless in the MONRP because the dependencies are one of the inputs (constraints) to the problem, and are thus known from the very beginning. In this section, we first briefly introduce some notions about EDAs, and then present our proposal, FEDA, a multivariate EDA with a fixed structure of dependencies to cope with the MONRP.

### 4.1. Estimation of distribution algorithms

Stochastic global search algorithms are expected to capture the underlying interdependencies among items under selection, in this case, requirements. That is why evolutionary algorithms such as GA and EDA typically obtain better results than local search ones.

In the EDA, the search is not guided by the use of genetic operators but by machine learning and inference processes. Thus, in EDA, the goal is to use the best individuals in the population as instances to learn the joint probability distribution (JPD) over the set of variables to be optimised, that is, the inclusion or not of requirements, in our case. This probability distribution explicitly collects the relationships between the variables in the best individuals, and so sampling from it should theoretically produce a better subset of individuals (population). However, the JPD is intractable even for a small number of variables, and thus Bayesian networks (BNs) (Koller and Friedman, 2009) emerge as the perfect candidate to model the JPD, given that their combination of graph and probability theory allows them to properly factorise the JPD. Furthermore, many machine learning and simulation algorithms are available in the literature to deal with BNs. Therefore, in practice, BNs constitute the core of EDAs, giving rise to different algorithms depending on the degree of probabilistic dependencies allowed to be modelled by the BN.

Formally, univariate EDAs assume that the $n$-dimensional JPD factorises as a product of $n$ marginal and independent probability distributions, that is $p_{i}(x)=\prod_{i=1}^{n} p_{i}\left(x_{i}\right)$. The canonical representative of this idea is the Univariate Marginal Distribution Algorithm (UMDA) (Mühlenbein, 1997). UMDA ${ }^{\mathrm{a}}$, i.e. the adaptation of UMDA to the multiobjective case, starts by creating a random population, and at each

generation it selects the non-dominated individuals of the population, learns the probability model $p_{i}$ from them, and samples a new population using $p_{i}$. In contrast to UMDA, in which populations are transformed into a probability model whose only purpose is to sample new populations, the Probability Based Incremental Learning (PBIL) (Baluja, 1994) algorithm attempts to create a probability model which can be considered a prototype for high evaluation vectors for the function space being explored. In a manner similar to the training of a competitive learning network, the values in the probability model are gradually shifted towards representing those in high evaluation vectors.

As mentioned, in order to explicitly manage the requirements interdependencies, more complex EDAs are needed, that is, EDAs able to cope with multivariate dependencies among the variables to be optimised. This is the case of the Estimation of Bayesian Networks Algorithm (EBNA) (Larrañaga et al., 2000) which uses an unconstrained Bayesian Network (BN) (Koller and Friedman, 2009) to model the dependencies between the variables. In a BN, the joint probability distribution is factorised as:

$$
p\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid \text { Parents }\left(x_{i}\right)\right)
$$

which means that a marginal probability distribution $p_{j}\left(x_{i}\right)$ is estimated for each configuration $j$ of values for Parents $\left(x_{i}\right)$. Thus, the number of parameters to be estimated (and stored) grows exponentially on the number of parents. If $x_{i}$ has no parents, a single marginal probability distribution is estimated.

In EBNA, at each iteration, the algorithm learns a BN from a dataset consisting of the best evaluated individuals in the current population. This BN is then sampled in order to obtain a new population. It is worth noting here that while the BN structure learning from data is an NP-hard problem, sampling from it can be performed with linear complexity on the number of variables.

### 4.2. FEDA-NRP

In both the basic formulations of NRP and the multi-objective MONRP, a common input available before solving the problem is the set of requirements dependencies or interactions. In Section 2.2 we saw that, of the different types of interactions, implication $r_{i} \Rightarrow r_{j}$ and combination $r_{i} \odot r_{j}$ are the most important, with it being possible to eliminate the latter by merging the two requirements together in the same delivery (see example in Fig. 2). Furthermore, implications of the type Finish-to-Start (PMI, 2021) are the most common type of interaction in software projects, since they are internal hard-logic dependencies with a technological sense and are usually provided by the development team.

Therefore, we can assume that the set of requirements and their dependencies, known in advance, can be described in the form of a directed acyclic graph (DAG), $G=(R, E)$, where $R$ is the set of requirements and $E$ is the set of edges which codifies the dependencies among them. For instance, $G=\left\{R=\left\{r_{0}, r_{1}, r_{2}, r_{4}\right\}, E=\left\{r_{0} \Rightarrow\right.\right.$ $\left.r_{2}, r_{1} \Rightarrow r_{2}, r_{2} \Rightarrow r_{4}\right\}$ ), represents a domain with 5 requirements $\left\{r_{0}, r_{1}, r_{2}, r_{3}, r_{4}\right\}$, such that requirements $r_{0}, r_{1}$ and $r_{3}$ do not depend on any other requirement, while $r_{2}$ is directly affected by the inclusion of $r_{0}$ or $r_{1}$ in the selection of requirements, and $r_{4}$ is directly affected by the inclusion of $r_{2}$. Fig. 3 shows the resulting graph $G$.

The availability of the requirements graph as domain knowledge is of great importance because it actually represents the structure of a BN modelling the interdependencies between all the requirements. Therefore, we can avoid the most computationally demanding process in a multivariate EDA, i.e. structural learning, because parameter learning can be done in a very efficient manner once the structure is known. However, we can go one step further by simplifying the complexity of the BN model considered. To do so, we must be aware of the semantics induced by the set of dependencies between the requirements. Thus, we can observe that the inclusion of requirement $r_{i} \in$ Parents $\left(r_{j}\right)$ in
![img-2.jpeg](img-2.jpeg)

Fig. 3. Graph example with a prefixed structure for requirements dependencies.
the selected set of requirements is enough to force also the inclusion of $r_{j}$ in the selection, regardless of whether the other requirements in Parents $\left(r_{j}\right)$ have been included. On the other hand, we must consider that $r_{j}$ can be selected even if no element of Parents $\left(r_{j}\right)$ has been selected. This behaviour is well known in the BN literature under the name of leaky binary noisy-OR gate (see e.g. Rohmer (2020) and Onisko et al. (2001)):
"Consider a set of $n$ possible causes $\left\{x_{1}, \ldots, x_{n}\right\}$ for an effect $y$, such that, each cause $x_{i}$ can produce effect $y$ with probability $p_{i}$ independently of the presence of any other subset of causes. Furthermore, there is a leak probability, $p_{0}$, of the effect being true even if all the causes are false".

The advantage of using this type of gate to model a relation $\left(x_{i}\right)$ Parents $\left(x_{j}\right)$ in a BN is that only $\left\{\right.$ Parents $\left.\left(x_{j}\right)\right\}+1$ parameters are needed instead of $2^{\left\{\text {Parents }\left(x_{j}\right)\right\}}$. In our problem, we can go even further, because as a dependency $r_{i} \Rightarrow r_{j}$ means a deterministic relation, that is, $p\left(r_{j} \mid r_{i}\right)=1$, then $p_{1}=p_{2}=\cdots=p_{n}=1$, and we only have to store the leak probability $p_{0}$ of $r_{j}$ being true (selected) when all its parents are false (non selected). As a result, our proposal FEDANRP has the same learning and space complexity as a univariate EDA algorithm, e.g. UMDA, as we only have to estimate and store vector of length $n$, probs[ ], containing a single parameter for each requirement: probs $[i]=p\left(r_{i}=1\right)$.

Having described the probabilistic graphical model and its advantages, which can be used as basis for our proposal FEDA-NRP (Fixed dependency model Estimation of Distribution Algorithm for the NRP) to cope with the MONRP, we now describe the main FEDA-NRP parts/steps, showing its pseudocode in Algorithm 2.

A high-level overview of FEDA-NRP, as depicted in Fig. 4, performs as follows. The population of individuals, defined by requirements and dependencies (see Section 4.2.1), is firstly initialised following the ancestral order of the BN structure. The algorithm manages two different archives of non-dominated solutions: a local one containing the NDS in the current population and a global one that contains the NDS visited (and currently being non-dominated) from the first iteration up to the current one. The main loop updates a global set of NDS with the current population (see Section 4.2.2), which will be returned at the end of the execution, as well as a local set of NDS, while the termination condition is not met. The probability model previously defined (see Section 4.2.3) is updated using the local set of NDS (see Section 4.2.5). Then, a new population is sampled using the probability model (see Section 4.2.4). Sampled individuals will respect the BN dependencies structure and will thus not require repairing.

![img-3.jpeg](img-3.jpeg)

Fig. 4. High-level overview diagram of FEDA-NRP.

### 4.2.1. Individual representation

As in the rest of population-based algorithms used to solve the MONRP, each solution (individual) is represented by a vector of booleans of length $n=|R|$, where the $i$ th value indicates the inclusion or not of a requirement $r_{i}$ in the next release.

### 4.2.2. NDS

FEDA-NRP applies a PAES strategy, and so non-dominated solutions found during the search are stored. In particular, two archives are maintained: a global one, $n d s_{\text {archive }}$, containing all the non-dominated solutions visited; and a local one, $n d s_{\text {local }}$, which contains the nondominated solutions in the current population. $n d s_{\text {local }}$ will be used as the dataset to learn the parameters of the probabilistic model at each FEDA-NRP iteration.

### 4.2.3. Model initialisation

Our probabilistic graphical model probModel is a $B N$ formed by the graphical structure $G$ and the probabilities probs[ ]. The graphical structure $G$ to be used is obtained from the problem domain, as dependencies between the requirements are provided as input $(G)$. The leaky binary noisy-OR is used to model all the nodes having a non-empty set of parents.

With respect to the parameters needed, a uniform distribution is used to initialise the probability of each requirement, i.e. probs $[i]=$ $p\left(r_{i}=1\right)=0.5$, for $i=1, \ldots, n$.

### 4.2.4. Sampling

As is common in multivariate EDAs, probabilistic logic sampling (PLS) (Henrion, 1988) is used, adapted, in our case, to the use of leaky noisy-OR gates.

First, an ancestral order $\sigma$ with respect to $G$ is needed. That is, an ordering of the requirements such that $r_{i}$ cannot precede any of its parents. The existence of at least one ancestral order for the variables in $G$ is guaranteed because $G$ is a DAG. In our notation, $\sigma[i]=r_{i}$ means
that requirement $r_{i}$ is placed in the $i$ th position of the ordering. For instance, in the graph depicted in Fig. 3, a possible topological ordering is $\sigma=\left[r_{3}, r_{0}, r_{1}, r_{2}, r_{4}\right]$.

To obtain a new sample $s$, we apply Algorithm 1, which iterates over the requirements following the ordering stored in $\sigma$. If the requirement $r_{i}$ has no parents in $G$, then it is selected (i.e. $s[i]=1$ ) if a random number generated in $[0,1]$ is smaller than or equal to $\rho\left(r_{i}=1\right)\left(\operatorname{probs}[i]\right)$. On the other hand, if $r_{i}$ has parents in $G$, then we are sure they have been previously visited by the sampling process because of the ancestral ordering, and thus its sampled values are already stored in $s$. If so, we select the values in $s$ corresponding to Parents $\left(r_{i}\right)_{G}\left(s^{\left\{\text {Parents }_{G} \mid s_{i}\right)}\right)$ and if this (sub)vector contains at least one value equal to 1 , then $r_{i}$ is selected because of the dependencies. Otherwise, we proceed as in the no-parents case, sampling from the leak probability stored in probs $[i]$.

### 4.2.5. Learning

As described in previous sections, there is no need for structural learning in FEDA-NRP, because the graph structure is predefined (or fixed) by the dependencies between requirements. Therefore, only parameter learning is needed.

Because of the use of the leaky noisy-OR gate to model the nodes corresponding to requirements with parents, we only have to estimate the probability vector probs[ ] of length $n$, with:
$\operatorname{probs}[i]= \begin{cases}p\left(r_{i}=1\right) & \text { if Parents }\left(r_{i}\right)=\emptyset \\ p\left(r_{i}=1 \mid \text { all parents }=0\right) & \text { if Parents }\left(r_{i}\right) \neq \emptyset\end{cases}$
Therefore, all the probabilities required can be computed using e.g. maximum likelihood estimation (MLE) from the frequencies obtained in a single pass over the data (subset of individuals). However, there is a special case that should be treated with caution, which is that of a requirement $r_{i}$ whose value is 0 in all the individuals that constitute the dataset, that is, $r_{i}$ is never selected. If we use MLE in

```
procedure GrzSource( $p r o b$ Model $=(G=(R, E)$, probs $) ; \sigma)$
    \(s \leftarrow\{0,0, \ldots, 0\}\)
    \(P \leftarrow \operatorname{initPop}(G)\)
    evaluate \((P)\)
    for \(j=0\) to \(\{R)\) do
        \(r_{j} \leftarrow \sigma[j]\)
        if Parents \(_{i j}\left(r_{j}\right) \neq \emptyset\) then
            if \(s^{\left\{\text {Parents }_{i j} \mid r_{j}\right\}}\) contains at least a 1 then
                \(s[j] \leftarrow 1\)
            else if \((r a n d o m(\{0,1\}) \leq \operatorname{probs}\{i\})\) then
                \(s[j] \leftarrow 1\)
            end if
        else
            if \((r a n d o m(\{0,1\}) \leq \operatorname{probs}\{i\})\) then
                \(s[j] \leftarrow 1\)
            end if
        end if
    end for
    return \(s\)
end procedure
```

Algorithm 2 FEDA-NRP pseudocode
procedure FEDA( $G$, popSize, iterations)
$n d s_{\text {archive }} \leftarrow \emptyset$
$\sigma \leftarrow$ ancestralOrdering $(G)$
probModel $\leftarrow$ initProbabilisticModel $(G)$ for $i=0$ to iterations do
$P \leftarrow$ samplePop(probModel, $\sigma$, popSize)
evaluate $(P)$
$n d s_{\text {local }} \leftarrow$ getLocalNDS $(P)$
$n d s_{\text {archive }} \leftarrow$ updateNDS $\left(n d s_{\text {local }}\right)$
probModel $\leftarrow$ learnProbModel(probModel, $n d s_{\text {local }}$ )
end for
return $n d s_{\text {archive }}$
end procedure
this case, $P\left(r_{i}=1\right)$ will be zero, and thus solutions selecting $r_{i}$ will no longer be obtained. Therefore, to avoid this undesired behaviour, we keep the value of probs[i] unchanged, that is, the value is not modified in the learning step. Evidently, some other possibilities are available, such as smoothing (e.g. Laplace) for parameter estimation, but this one has worked properly for the problem at hand.

### 4.2.6. FEDA-NRP scheme

Finally, using the previously described processes as building blocks, the pseudocode of FEDA-NRP is shown in Algorithm 2. As can be observed, FEDA-NRP follows a PAES strategy, that is, as explained in Section 2.1, an $N D S_{\text {archive }}$ is maintained along the whole process, being updated with the set of non-dominated solutions found at each iteration.

### 4.3. Example

This section provides an example based on the dependencies codified by the graph $G$ shown in Fig. 3, considering $\left\{r_{3}, r_{0}, r_{1}, r_{2}, r_{4}\right\}$ as the ancestral ordering for sampling.

### 4.3.1. Model initialisation

Given $G$ in Fig. 3, prior probabilities for selecting requirements without parents and leak probabilities for selecting requirements with parents are set to 0.5 . Thus, probs $=\{0.5,0.5,0.5,0.5,0.5\}$.

### 4.3.2. Population sampling

Let us detail the sampling of an individual by using Algorithm 1 and $\sigma=\left\{r_{3}, r_{0}, r_{1}, r_{2}, r_{4}\right\}$. We start with $s=\{0,0,0,0,0\}$.
$\sigma\{0\}=r_{3}$. As $r_{3}$ has no parents in $G$, we sample a random uniform number in $\{0,1\}$, say $u=0.72$. As $u \leq p\left(r_{3}=1\right) ?(0.72 \leq 0.5 ?)$ is false, $s[3]$ remains 0 .

- $\sigma[1]=r_{0}$. As $r_{0}$ has no parents in $G$, we sample a random uniform number in $\{0,1\}$, say $u=0.91$. As $u \leq p\left(r_{0}=1\right) ?(0.91 \leq 0.5 ?)$ is false, $s[0]$ remains 0 .
- $\sigma[2]=r_{1}$. As $r_{1}$ has no parents in $G$, we sample a random uniform number in $\{0,1\}$, say $u=0.51$. As $u \leq p\left(r_{1}=1\right) ?(0.51 \leq 0.5 ?)$ is false, $s[1]$ remains 0 .
- $\sigma[3]=r_{2}$. As $r_{2}$ has $\left\{r_{0}, r_{1}\right\}$ as parents, we first check whether $s[0]$ or $s[1]$ are 1 . As this is not the case, we sample a random uniform number in $\{0,1\}$, say $u=0.17$. As $u \leq p\left(r_{2}=1\right) s_{0}=s_{1}=0$ )? $(0.17 \leq 0.5 ?)$ is true, we set $s[2]=1$.
- $\sigma[4]=r_{4}$. As $r_{4}$ has $\left\{r_{2}\right\}$ as parent, we first check whether $s[2]$ is 1. As this is the case we directly set $s[4]=1$.

Therefore, our sample is $s=\{0,0,1,0,1\}$. Let us consider popSize $=$ 6 , and that the sampling process produces:
$P=\{\{0,0,1,0,1\} ;\{0,0,0,0,1\} ;[0,0,1,1,1\} ;\{0,0,0,0,0\} ;$
$[0,1,1,0,1\} ;\{1,1,0,1,1\}\}$

### 4.3.3. Selecting non-dominated solutions

Let us assume that, after evaluating the population, the following set of non-dominated solutions are identified:
$n d s_{\text {local }}=\{\{0,0,1,0,1\} ;\{0,0,0,0,1\} ;\{0,0,0,0,0\} ;\{1,1,0,1,1\}\}$
They will constitute our local archive of NDS as well as the global one, because this is the first iteration of FEDA-NRP.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Marginal/conditional probabilities for each requirement.

### 4.3.4. Probabilistic model learning

By taking $n d s_{\text {incel }}=\{(0,0,1,0,1] ;[0,0,0,0,1] ;[0,0,0,0,0]$; $\{1,1,0,1,1\}\}$ as our dataset, we simply compute the proper frequencies to estimate the new probs vector.

- $\operatorname{probs}\{0\}=p\left(r_{0}=1\right)=\frac{1}{3}=0.25$
- $\operatorname{probs}\{1\}=p\left(r_{1}=1\right)=\frac{1}{3}=0.25$
- $\operatorname{probs}\{2\}=p\left(r_{2}=1 \mid r_{0}=r_{1}=0\right)=\frac{1}{3}=0.33$
- $\operatorname{probs}\{3\}=p\left(r_{3}=1\right)=\frac{1}{3}=0.25$
- $\operatorname{probs}\{4\}=p\left(r_{4}=1 \mid r_{2}=0\right)=\frac{2}{3}=0.67$

Please note that for requirements having a non-empty set of parents ( $r_{2}$ and $r_{4}$ ), only the individuals for which all the parents have a value equal to zero are considered to compute the estimated probability.

Therefore, the new probabilistic model to be used in the next iteration has the fixed graphical structure and parameters probs $=$ $\{0.25,0.25,0.33,0.25,0.67\}$. Fig. 5 shows the result.

## 5. Experimental framework

We performed an exhaustive experimentation not only with our proposed method FEDA-NRP but also, for comparison reasons, with univariate and bivariate EDAs (UMDA, PBIL, MIMIC), and two advanced multi-objective genetic algorithms: AGE-MOEA-II and C-TAEA, all adapted to deal with dependencies. Due to the lack of public NRP datasets, we sampled a corpus with instances of software products managed under different contexts, which also constitutes an important contribution of this work. In the following sections, we introduce the sampling process and the resulting datasets. We then provide some detail about the quality metrics used for the evaluation. Finally, we explain the methodology followed in the execution of the different algorithms and the results obtained.

### 5.1. Datasets

In 2015, Chaves-Gonzalez et al. (2015) explained that due to the privacy policies followed by software development companies, the only two publicly available datasets were those included in their work, which we denote as $p 1$ (Greer and Ruhe, 2004) and $p 2$ (del Sagrado et al., 2015) in Table 1 ( $p$ stands for public). These public datasets have a low number of requirements, and present only a few implication and combination dependencies.

Later, Almeida et al. (2018) dealt with several corpuses of different sizes and interactions complexity: Classic and Realistic datasets (Ren
et al., 2012), and a new corpus of their own sampling. Souza et al. deal with 72 synthetic datasets in Souza et al. (2011), with a number of requirements from $20-50$ and implication interactions with a density of implications of up to $20 \%$ of requirements; however, they are not public yet. Apart from Greer and Ruhe (2004) and del Sagrado et al. (2015), we also found two public datasets in Karim and Ruhe (2014); however their complexity is similar to $p 1$ and $p 2$, and thus we do not consider them, as our goal is to deal with more complex instances.

In the absence of public datasets of higher dimensionality, we decided to sample synthetic datasets with a wide range in the number of requirements, stakeholders, number of implication interactions, density of interactions and average length of implied requirements by the same requirement. The reason we are interested in a large range in the number of requirements is that software projects may contain not only tens of requirements, but in the order of hundreds. This is even more common in projects managed in a plan-driven manner, where requirement elicitation results in a very large output of features to be developed.

Furthermore, we decided to sample datasets related to both projects managed under classic and agile methodologies. Thus, we generated four agile and four classic datasets (named $a X$ and $c X$ ). Lastly, we sampled the $d X$ datasets with a classic management context, similar to in $c X$, but with a greater complexity in requirements and dependencies. Table 1 summarises the different properties of the public and synthetic datasets sampled and used in our experiments. Our corpus can be divided into four kinds of datasets:

- $p X$ datasets: two small datasets used in several works, such as in del Sagrado et al. (2015). $p 1$ comes from a real dataset, and it has very few requirements (20) and also very few dependencies (7). $p 2$, a public synthetic dataset, provides a more realistic dataset in the sense of its complexity, although the number of dependencies and requirements is still quite small.
- aX datasets: commonly, agile projects have a low number of actively managed stakeholders, although the received buy-in in the development of the product is more constant. Thus, $a X$ datasets present a lower number of stakeholders. Since requirements are not decided a priori, with a long elicitation process, requirements and dependencies between them are not typically large for a given minor or functional release. Thus, we produced datasets with few dependencies and requirements. On the other hand, two $a X$ datasets have many requirements. Effort estimations are computed using a Fibonacci scale, similar to common agile estimation techniques.
- cX datasets: classic or plan-driven datasets tend to have many requirements and, due to long and expensive planning, also numerous dependencies. Furthermore, due to usual processes of managing stakeholders interests, it is also common to identify more stakeholders than in agile datasets. Effort values were simulated by using the Function Points (FP) size metric extracted from the 2015 version of the International Software Benchmarking Standards Group ${ }^{5}$ (ISBSG) dataset, using the two highest categorical values from the Unadjusted Function Points rating column, 'New development' from Development type and 'IFPUG 4+' from the Count approach column. This procedure is used to generate percentiles $25,50,75$ of total FP of a classic project, in order to generate a realistic sample of a classic estimation of requirements. This size generation is done by selecting randomly, for a given number of requirements, a list of costs that sums up to the percentile value.
- dX datasets: following the same procedure as in $c X$, we simulate the most complex classic projects, with the largest number of requirements and dependencies. In fact, this is the case in which the MONRP might be of greater help for the decision-maker.

[^0]
[^0]:    ${ }^{5}$ https://www.isbsg.org/.

Table 1
Datasets used in our experiments: 2 public dataset, 4 agile, 4 low scale classic, and 4 large scale classic management.

Table 1 summarises all the datasets used in this work. $\|R\|$ is the number of requirements, out_degree $\left(r_{i}\right)$ is the number of requirements implied by requirement $r_{i}$, and $O$ is the number of requirements with an implication dependency towards one or more requirements, as expressed in Eq. (5). $\% R$ is $O /|R|$, that is, the percentage of requirements in the dataset which imply other(s) requirement(s), and is referred to as density, ranging $[0,1]$. Finally, $\bar{D}$ is the average number of implications in requirements with implication interaction with one or more requirements (Eq. (6)).
$O=\sum_{i=1}^{|R|} I\left(\right.$ out_degree $\left(r_{i}\right)>0$ )
$\bar{D}=\frac{\sum_{i=1}^{|R|} \text { out_degree }\left(r_{i}\right)}{O} r_{i}$
The benchmark of datasets created is publicly available for download in Pérez-Piqueras et al. (2022).

### 5.2. Algorithms

Apart from FEDA, three well-known EDA algorithms form part of our experimentation framework (UMDA, PBIL and MIMIC) and two recent multi-objective genetic algorithms (AGE-MOEA-II and C-TAEA) that are capable of dealing with dependencies. These were found to perform better than the NSGA-II (Deb et al., 2002) and NSGA-III (Deb and Jain, 2014), two advanced versions of NSGA (Srinivas and Deb, 1994), which is commonly used for comparison in MONRP studies.

- AGE-MOEA-II (Adaptive Geometry Estimation based MOEA II) (Panichella, 2022) is presented and evaluated, being found it outperforms (in the hypervolume indicator) four multi- and manyobjective evolutionary algorithms, using a novel method to model the non-dominated front.
- C-TAEA (Li et al., 2019), an Evolutionary Algorithm that maintains two archives (one for convergence and the other for diversity) during a constrained search, outperforming in a benchmark of multi- and many-objective problems with a relatively small number of variables (requirements if applied to MONRP).

Since datasets $p 1$ and $p 2$ contain combination interactions $\left(r_{i} \varnothing_{j}\right)$, those dependencies were eliminated by joining both requirements in a new one $r_{i, j}$, as in del Sagrado et al. (2015). The two genetic algorithms are explicitly designed to deal with dependencies.

The five competing algorithms, UMDA, PBIL, MIMIC, AGE-MOEA-II and C-TAEA, were adapted to deal with implication dependencies in a straightforward manner. Thus, after generating a set of individuals, if an individual contains $r_{i}$ with $r_{i} \Rightarrow r_{j}$, then $r_{j}$ is also set in the individual vector of selected requirements.

FEDA-NRP and all the competing algorithms maintain the $N D S_{\text {archive }}$ through their execution. Since the competing algorithms were adapted, we refer to them as UMDA ${ }^{\circledR}$, PBIL $^{\circledR}$, MIMIC $^{\circledR}$, AGE-MOEA$\mathrm{II}^{\circledR}$ and C-TAEA ${ }^{\circledR}$.

### 5.3. Evaluation indicators

The following are some of the most commonly applied and reliable quality metrics used to assess both convergence and diversity of solutions:

- Hypervolume (HV) (Zitzler and Thiele, 1998). This is the most widely used metric to assess Pareto fronts in multi-objective problems in SBSE. It denotes the space covered by the set of nondominated solutions. In order to compute it, a reference point is needed, which should be the same for all algorithms under comparison.
- Unique Nondominated Front Ratio (UNFR) (Li et al., 2020). This metric requires computing a Pareto reference (PRef), which is a set of non-dominated solutions obtained by merging all Pareto fronts returned by the algorithms being evaluated after their execution. Thus, UNFR measures the ratio of solution points in the PRef that belong to the solution set of the evaluated algorithm. That is, it measures the contribution (from 0 to 1 ) of an algorithm to the PRef.
- Generational Distance+ (GD+) (Veldhuizen and Lamont, 1998). This covers the convergence aspect of the quality of a solution set, measuring the Euclidean distance of the solution set to the ideal PRef. Consequently, this metric is to be minimised. For each solution, its GD is the minimum of the distances to each point in the Pareto front. In order to make GD compliant with Pareto dominance, GD+ enhances GD by measuring distances between points, using only the objective coordinates that are superior in the PRef to those from the solutions set being measured.
- $\Delta$-Spread (Deb, 2001). This measures the dispersion of the solutions in the Pareto front. Thus, the smaller the $\Delta$ value is for a set of non-dominated solutions, the better (more uniform).

HV may serve as a general representation of the four quality aspects, but the other three metrics give a more granular detail of spread and uniformity ( $\Delta$-Spread), convergence (GD+), and cardinality related to the PRef (UNFR).

### 5.4. Evaluation

Since datasets are sampled using different scales for agile and classic types, evaluation of Satisfaction and Cost of each solution vector is computed with a prior scaling of requirement value and cost, using a min-max normalisation. Consequently, all non-dominated solutions returned by the executed algorithms are in the range $[0,1]$.

Based on guidance by Ishibuchi et al. $(2022,2020)$ for fair comparison, we compute all metrics from a subset selection of solutions from the resulting $N D S_{\text {archive }}$. Concretely, we run a hypervolume-based greedy forward subset selection to choose 10 solutions.

With regard to HV, it is always computed using the same reference point. In order to decide an appropriate reference point, we drew on the guidance in Li et al. (2020) to set the HV reference point in a bi-objective problem:
re $f_{x}=$ nadir $r_{x}+$ range $r_{x} / 10$
re $f_{y}=$ nadir $r_{y}+$ range $r_{y} / 10$
The nadir point is the worst point found by algorithms during a search. Since we normalise both Satisfaction and Cost, our worst value is 1 for both metrics (Satisfaction is plotted as $1-$ Satisfaction). Range is the difference between the best and worst point found. The best possible value for each metric is 0 , so the $x$ and $y$ values of the reference point for both goals are set as:
re $f_{x}=r e f_{y}=1+(1-0) / 10=1.1$

Regarding the GD+ metric, the necessary PRef is a proxy set for the ideal Pareto front. Thus, we build the PRef filtering the non-dominated solutions set from a pool made of all the $N D S_{\text {archive }}$ sets found by all the algorithms executed under all the hyperparameter configurations detailed in Section 5.5.

Finally, it is worth mentioning an important aspect of the UNFR metric. In the case of this work, since the PRef is obtained from such a great number of algorithms and configuration combinations (see Section 5.5), it presents a high number of solutions. Furthermore, each algorithm is not evaluated using all solutions from its corresponding $N D S_{\text {archive }}$, but using a selected subset of 10 points from its corresponding $N D S_{\text {archive }}$. Thus, the UNFR value for each algorithm tends to be quite low, and the maximum possible is never 1 , since $|P R e f| \gg 10$. In any event, greater UNFR values are desirable.

### 5.5. Experiment configuration

Each algorithm is executed 30 times. After each execution, a set $S$ of 10 solutions is selected from $N D S_{\text {archive }}$ to compute HV and $\Delta$ Spread metrics. In the case of GD+ and UNFR, they cannot be computed until the PRef is constructed; that is, until the 30 executions for all algorithms have finished. Then, GD+ and UNFR are computed from the set $S$ obtained in each execution. Finally, all the metrics are averaged over the 30 runs.

Lastly, with respect to the hyperparameter configuration of algorithms (population size, maximum number of generations, ...), we follow the recommendations in Ishibuchi et al. (2022), which suggest that algorithms should be run under their best possible configuration. Thus, the experimental results for algorithms shown in Section 5.7 come from the 30 executions of each algorithm under its best configuration found. Appendix contains the range of values for each hyperparameter, and we identify the best configuration found for each algorithm after evaluating a grid search over all the hyperparameters. Two hyperparameters are common in all algorithms (Population Size and Number of Iterations), with values: Population Size $=(100,200$, $500,700,1000)$ and \#Iterations $=(50,100,200,300,400)$. All algorithms yield their best results (measured by HV) when using a Population Size $=1000$, the maximum value among the 5 given for this hyperparameter. With respect to the number of iterations, all algorithms but UMDA ${ }^{\circledR}$ need many iterations to converge, usually the maximum (400) or almost the maximum (300 in FEDA) value among the possible ones. UMDA ${ }^{\circledR}$ seems to converge very quickly, since in 7 out of 14 datasets it yields its best results with just 100 or fewer generations, in both agile and classic projects.

### 5.6. Reproducibility

All experiments were run under the same runtime environment. The machines used had 32 Gb of RAM, of which only 8 Gb were used, and two 3.00 GHz 4-core Intel Xeon E5450 processors. The operating system used was a CentOS Linux 7 with a 64-bit architecture. All the algorithms and the experimentation setup were implemented by the authors of this work using Python 3.8.8, with the exception of the AGE-MOEA-II and C-TAEA algorithms, which were run using the Python-based Pymoo package (Blank and Deb, 2020). All our code is available at the following repository: https://github.com/UCLM-SIMD/MONRP/tree/eng app_ai23; the sampled datasets are also available at the following repository: https://doi.org/10.5281/zenodo. 7247877 (Pérez-Piqueras et al., 2022). Additional packages and libraries used to support numeric operations, metric calculations and data visualisation can be found in the list of package requirements inside the GitHub repository, with the following being the most important packages: matplotlib, numpy, pandas, scipy, pymoo.

Table 2
Quality metrics in datasets: public $(\rho X)$ and agile $(\alpha X)$.

### 5.7. Results

We ran the six algorithms under comparison (FEDA, UMDA ${ }^{\circledR}$, PBB $^{\text {a }}$, MIMIC ${ }^{\circledR}$, AGE-MOEA-II ${ }^{\circledR}$ and C-TAEA ${ }^{\circledR}$ ) using their best hyperparameter configuration found (see Appendix), and run over our corpus of 14 datasets (Section 5.1).

In this section, we provide the values obtained for each dataset in the four quality metrics (HV, UNFR, GD+, Spread) and the mean cardinality of the final $N D S_{\text {archive }}$. We also show a visual indicator (scatter plot) for qualitative assessment.

## Quality metrics

In Tables 2, 3 and 4, for each dataset, we highlight in bold the best metric value among the six algorithms.

The most important and widely used quality metric in the literature is HV, since it is Pareto compliant and summarises the four dimensions to be assessed on solution vectors.

With respect to the datasets with the lowest complexity, that is, those with fewer than 200 requirements ( $\rho 1-a 2, c 1, c 2$ ), it can be observed that there is no clear winner for the HV metric; with AGEMOEA-II ${ }^{\circledR}$ being that with more wins (three out of six datasets). On the other hand, FEDA-NRP is the winner in the case of the datasets with the highest complexity in terms of number of requirements $(|R|)$ and $O$ (see Table 1). Our proposed FEDA-NRP reaches the highest hypervolume in all cases but one ( $\alpha 4$ with 200 requirements, .802 vs .805 in MIMIC). That is, as the number of requirements and requirements interactions increases, FEDA-NRP is able to find better solution subsets than the other algorithms. Furthermore, the greatest outperformance of FEDA-NRP with respect to the other algorithms is in $d X$ datasets that represent classic-managed software products, with this scenario

Table 3
Quality metrics in classic $(c X)$ datasets.

Table 4
Quality metrics in complex classic $(d X)$ datasets.

being where the MONRP is most commonly applied and more useful due to the need for long-term planning. Fig. 6 shows the mean HV for each algorithm as the number of requirements increases. Together with requirements, the number and density of dependencies also increases. Thus, the search space is more difficult to explore since it is much more restricted. Consequently, the diversity of solutions tends to decrease as well as the HV. In the case of a larger number of requirements (200 and 300), FEDA-NRP presents a better average HV than the other algorithms. This difference in HV (distance from the FEDA-NRP brown line to the other lines) increases with the number of requirements. This can be better appreciated in Fig. 7, which shows the difference in the mean HV, between FEDA-NRP and each of the other algorithms, ordered by number of requirements. As can be seen, this difference increases in all cases when the number of requirements exceeds 100, particularly in the case of $\mathrm{PBIL}^{a}$ and the two recent multi-objective
![img-5.jpeg](img-5.jpeg)

Fig. 6. Mean hypervolume in datasets with the same number of requirements.
![img-6.jpeg](img-6.jpeg)

Fig. 7. FEDA-NRP diverges from the rest of algorithms, in terms of hypervolume, as the number of requirements increases.
algorithms AGE-MOEA-II ${ }^{a}$ and C-TAEA ${ }^{a}$. It is also of interest to mention that only when datasets have more than 100 requirements does FEDANRP start to diverge from MIMIC ${ }^{a}$. With 300 requirements, FEDA-NRP is not just superior in HV to all algorithms, but is also much faster than its main competitors (AGE-MOEA-II ${ }^{a}$, C-TAEA ${ }^{a}$, and MIMIC ${ }^{a}$ ), as explained later in the Time discussion.

Looking at Table 4, it might seem that FEDA-NRP obtains the best HV values because of the high cardinality of the final $N D S_{\text {archive }}$ obtained. However, as previously stated, all the metrics are computed from a subset of the same size (10). Thus, it is worth recalling here that in pursuit of a fair comparison (see Section 5.4) all quality metrics are computed from solution sets of the same size.

Nevertheless, in complex datasets and when the focus is not set on HV but on quality metrics that measure just one of the four measurement aspects of non-dominated sets, AGE-MOEA-II ${ }^{a}$ performs the best in terms of UNFR and GD+, and UMDA ${ }^{a}$ performs the best in terms of $\Delta$-Spread. With respect to these metrics, it is again worth mentioning that, as explained in Section 5.4, since PRef is computed from all the solutions found by all the algorithms, the UNFR computed for a given algorithm is always very low and far from 1. For example, in dataset $p 1$, the PRef is made up of 38 points. Since each execution of an algorithm returns a 10 -points subset from the resulting $N D S_{\text {archive }}$, its maximum UNFR possible is $10 / 38=0.2632$.

## Statistical analysis of quality metrics

For each metric, we run the Friedman test, a non-parametric group test for dependent samples (the same 14 datasets are used as input in the 6 algorithms). When the Friedman test detects a significant

Table 5
Mean values for each algorithm in less and more complex datasets.

difference between the compared algorithms, a post hoc test is run: pairwise comparisons with Wilcoxon signed-rank test, with correction of the $p$-value for multiple comparisons reducing the false discovery rate. A significance level of $5 \%$ was used. Table 5 shows the mean value obtained for each metric, distinguishing between simple datasets ( $\leq 100$ requirements) and the most complex datasets ( $\geq 200$ requirements). If the post-hoc test shall be run (because the Friedman test is significant), then we mark with - the algorithm with the best mean value, and then with * the algorithms found to be statistically different from the control algorithm in the post-hoc tests. Thus, if an algorithm is not marked with ${ }^{*}$, it is not significantly different from the control. Conclusions vary from simple to complex datasets; that is, the best performing algorithms depend on the number of requirements and dependencies. When dealing with simple datasets ( $p 1, p 2, a 1, a 2, c 1$ and $c 2$ ), the posthoc tests find no algorithm to be statistically worse than the control algorithm, in any of the quality indicators.

In the case of algorithms with more dependencies and requirements ( $a 3, a 4, c 3, c 4, d 1-d 4$ ), which is the target of our proposal, FEDA-NRP obtains the highest HV, being significantly better than UMDA, PBIL, MIMIC, AGE-MOEA-II and C-TAEA (all the algorithms). In the case of our interest lying in metrics which solely reflect one quality dimension with respect to closeness to PRef, then AGE-MOEA-II is the one which performs the best. That is, it finds most of its solutions close to, or on, the PRef, but as can been seen in the visual indicators (plots), this is at the cost of finding medium or high Cost solutions. However, although not shown here for the sake of clarity, the execution time of AGEMOEA-II, together with C-TAEA, is much greater than that of any of the other algorithms. This, supports us in recommending FEDA-NRP rather than any of the other algorithms in our experimental framework (see Time discussion below) for the case of problems (software projects) with a high number of requirements to be planned.

As a final comment on these results, let us analyse the role played by the type of BN used as graphical model in the different EDAs considered. If we focus on the degree of dependencies allowed, we can order the models as FEDA-NRP (multivariate) > MIMIC (bivariate) > UMDA and PBIL (univariate). Thus, comparing them can be viewed as a sort of ablation study where, at each step, we reduce the number of dependencies allowed, thus simplifying the graphical model. From the results in Table 5 , in particular for the complex cases, which are the main target of this proposal, we can observe that the rank is exactly FEDA-NRP $>$ MIMIC $>$ UMDA $>$ PBIL. Therefore, as expected, the expressiveness of the Bayesian networks considered plays a key role in the behaviour of the corresponding EDA.

## Visual indicator with plotting of solution subsets

Apart from quality metrics, visual indicators are also useful not only to qualitatively assess the goodness of the solutions subsets, but also to compare the regions in which each algorithm behaves the best. If the decision-maker prefers middle or knee solutions, algorithms with
![img-7.jpeg](img-7.jpeg)

Fig. 8. Visual indicator of algorithm searches for dataset $a 1$.
high HV would again be the best choice. In this work, we present three plots as visual indicators for three datasets with different number of requirements: $a 1(|R|=50), c 3(|R|=200)$ and $d 3(|R|=300)$, although the complete set of images is available in the public repository. ${ }^{3}$ In Figs. 8-10, for each algorithm, we show the $S$ found in one of the 30 executions. Since $|S|$ is set to 10 , we plot the Pareto Front with a line across the 10 points. Evidently, statistical tests and values in tables are computed from the 30 executions. The PRef constructed is plotted in order to qualitatively assess the goodness of each algorithm with respect to the optimal Pareto front, and is also constructed using all the points from all the execution for all algorithms, thus seeking to define an ideal Pareto Front.

Fig. 8 shows that in the case of a small dataset, all the algorithms are capable of searching through the balanced (knee) solutions area. PBIL ${ }^{a}$, MIMIC ${ }^{a}$ and FEDA-NRP are the only ones that find close solutions in the areas that minimise the Cost of development, while FEDA-NRP is the only one capable of finding extreme solutions in the area of Satisfaction maximisation. Similar behaviour is observed in the rest of the datasets with a low number of attributes. With this case being more common in agile project management, because requirements are created dynamically, any of the mentioned algorithms would be a good choice to solve the MONRP in such contexts. As shown in Table 5, in less complex datasets, there is no significant difference for HV, and so a good choice would be to use the fastest of the four mentioned algorithms, which are FEDA-NRP and PBIL ${ }^{a}$ (see Time discussion below).

With regards to classic management datasets with greater complexity in terms of requirements and dependencies, we can observe the behaviour of the algorithms in Figs. 9 and 10. The scatter plot in Fig. 9 shows that PBIL ${ }^{a}$ only remains close to PRef in the Cost minimisation area, and is unable to find solutions in the balanced (knee) or maximisation (extreme right) zones for Satisfaction. Thus, its performance in terms of HV decreases drastically with the increase in the complexity of the project, which is exactly the opposite in the case of FEDA. As can be seen, AGE-MOEA-II ${ }^{a}$ and C-TAEA ${ }^{a}$ solutions both fail at minimising Cost and can only maximise Satisfaction; furthermore, not only does FEDA-NRP find balanced solutions close to PRef, but is also able to find solutions along the entire search space, returning solutions which minimise Cost, maximise Satisfaction or balances both objectives.

A similar situation can be interpreted from Fig. 10: PBIL ${ }^{a}$ really contributes to the PRef in solutions that minimise Cost until the limit in which balanced (knee) solutions start. Exactly the opposite happens for AGE-MOEA-II ${ }^{a}$ and C-TAEA ${ }^{a}$, which contribute to the PREF in solutions that maximise Satisfaction until the balanced solutions area starts,

[^0]
[^0]:    ${ }^{4}$ https://github.com/UCLM-SIMD/MONRP/tree/eng_app_si23.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Visual indicator of algorithm searches for dataset $c 3$.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Visual indicator of algorithm searches for dataset $d 3$.
which is where FEDA-NRP outperforms in the search process, in terms of closeness to PRef and, in general, in HV. Thus, it is visually clear (corroborated from results in Table 4) that FEDA-NRP would be the best option to be applied in large and complex datasets, specially in those commonly found in classic project management.

We thus prove that our proposed method is able to successfully use the knowledge about dependencies in the learning and sampling phases of EDA, which truly helps to find good solution sets in large datasets while maintaining a linear memory complexity similar to univariate algorithms such as UMDA.

With the help of the visual indicators, we have found that MIMIC ${ }^{a}$, UMDA ${ }^{a}$ and FEDA-NRP algorithms are those that explore the complete width of the search space, with FEDA-NRP being the one that gets closest to PRef, thus obtaining greater HV in the most complex datasets (especially for the classic-management datasets $d X$ ). Also in complex datasets, PBBL and genetic algorithms can only obtain good solutions for one of the objectives (left or right side of the PRef). Regarding UMDA ${ }^{a}$, the solutions it finds are not excessively close to each other, which is why this algorithm obtained the best $\Delta$-Spread values, so its strongest point would be the ability to provide more different solutions to the decision-maker.

## Time

C-TAEA ${ }^{a}$ is the algorithm that takes longest to finish its search, taking from 1.5 (best case) to 2.5 h (worst case). This time does not just depend on the complexity of the dataset, but also on other two issues: (1) the complexity of the algorithm itself and (2) the cardinality

Table A. 6
Number of wins for each set of hyperparameter configurations in the FEDA-NRP algorithm.

Table A. 7
Number of wins for each set of hyperparameter configurations in the AGE-MOEA-II algorithm.
of the $N D X_{\text {archive }}$, which depends on the capability of the algorithm to find non-dominated solutions in the search space. As the number of non-dominated solutions found increases, the filtering of $N D X_{\text {archive }}$ takes longer after each iteration.

The next most time-consuming algorithms are AGE-MOEA-II ${ }^{a}$, which may take up to 50 min to run its search, and MIMIC ${ }^{a}$ with up to 30 min . Then, FEDA-NRP runs it search with a maximum duration of 13 min . Hence, we conclude that, in a real-world context in which plandriven projects (to which $d X$ datasets belong) schedule a very large set of requirements to be delivered in the following months, our results support that FEDA-NRP is the best algorithm to solve the MONRP. It is capable of finding the statistically best solutions in the global quality metric of HV, and is also about twelve times faster than C-TAEA ${ }^{a}$, five times faster than AGE-MOEA-II ${ }^{a}$. FEDA-NRP is also twice as fast as MIMIC ${ }^{a}$, and statistically better in terms of HV, UNFR and GD+. Lastly, FEDA-NRP is the only algorithm that can provide the decision-maker with a variety of candidate solutions which range from both extreme areas (minimise Cost or maximise Satisfaction) to the balanced zones adjacent to the PRef in the search space from which to choose (as shown in the Visual indicators).

## 6. Conclusions and future work

The main contribution of this work is FEDA-NRP, a multivariate EDA to solve the MONRP which explicitly models dependencies between requirements. Embedding the knowledge about requirements interactions in the learning and sampling phases of an EDA helps to obtain good solution sets for the MONRP problem in complex datasets, in terms of hypervolume, balance and cardinality of the number of solutions. The use of the leaky binary noisy-OR gate in the model allows us to maintain a linear complexity while dealing with multivariate information.

The second contribution of the study is the creation of a benchmark of synthetic datasets covering different dimensions of requirements management in agile and classic software projects developments. The variety of this benchmark facilitated the evaluation of the tested algorithms in different regimes. We made this corpus publicly available to promote future research on MONRP, as well as our software to ensure reproducibility and fair comparison. In particular, in this paper, a rigorous experimental evaluation was carried out considering this corpus and involving six algorithms, the main conclusion of which is the superiority of FEDA-NRP over the rest of the tested algorithms when considering the most complex cases and the balance obtained between time required and accuracy of the solutions. It is in the case of complex problems (projects with a large number of requirements)

Table A. 8
Number of wins for each set of hyperparameter configurations in the C-TAEA ${ }^{c}$ algorithm.

Table A. 9
Number of wins for each set of hyperparameter configurations in the UMDA algorithm.

Table A. 10
Number of wins for each set of hyperparameter configurations in the PBIL algorithm.

Table A. 11
Number of wins for each set of hyperparameter configurations in the MIMIC algorithm.
that FEDA-NRP obtained the best HV results of all the algorithms. It is worth noting that its main competitors (in terms of HV) are also EDAs: UMDA and MIMIC, the latter taking twice as long as FEDA-NRP, and UMDA performing worse in terms of UNFR and GD+, besides HV. Another substantial advantage of FEDA-NRP with respect to these EDAs is that it finds the best balanced solutions close to the Pareto Reference, facilitating the decision-maker's choice for a candidate solution.

On the other hand, the main limitation of our proposal is that it requires as input the definition of all dependencies between requirements, although this is also the main motivation of our work. Without explicitly defined dependencies, the Bayesian network would be an empty graph, i.e., all variables would be independent of each other, so FEDA-NRP would be reduced to the UMDA algorithm.

As future work, it would be interesting to measure the complexity added by keeping the $N D S_{\text {archive }}$ updated during the search, and to optimise this process by updating the solution subset selection per iteration, instead of only once after the search has finished.

## CRediT authorship contribution statement

Víctor Pérez-Piqueras: Software, Investigation, Resources, Data curation, Writing - original draft, Writing - review \& editing, Visualization. Pablo Bermejo: Conceptualization, Software, Validation, Formal analysis, Investigation, Writing - original draft, Writing - review \& editing, Visualization, Supervision, Project administration. José A. Gámez: Conceptualization, Investigation, Writing - original draft, Writing review \& editing, Visualization, Supervision, Project administration, Funding acquisition.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

I have shared public links inside the paper to download the code and datasets.

## Acknowledgements

This work has been funded by the project SBPLY/21/180225/ 000062 funded by the Government of Castilla-La Mancha and "ERDF A way of making Europe". This work has also been supported by Universidad de Castilla-La Mancha, Spain and "ERDF A way of making Europe" under project 2023-GRIN-34437. It is also partially funded by MCIN/AEI/10.13039/501100011033 and "ESF Investing your future" through project PID2019-106758GB-C33. We also wish to thank the international Software Benchmarking Standards Group (ISBSG) for allowing us to use the 2015 version of their dataset for research purposes.

## Appendix. Algorithm hyperparameter selection

In this section, we show the range of values for hyperparameters tuned in each algorithm included in our experiments, as well as the number of wins over datasets.

All the algorithms were configured with hyperparameters PopSize $=\{100,200,500,700,1000\}$ and \#Iterations $=\{50,100,200,300$, 400\}. In total, 25 configurations per dataset.

With respect to concrete PBIL ${ }^{c}$ hyperparameters, we fixed learning rate, mutation probability and mutation shift to 0.1. UMDA and MIMIC used a selection scheme based on non-dominance and selection of a fixed number of 50 individuals.

The goodness of a configuration is measured in terms of the HV of the returned $N D S_{\text {archive }}$.

Since our global corpus contains 14 datasets (Table 1), the total number of wins for a given algorithm is 14 . The configuration (row) with more wins is then selected as the configuration of the corresponding algorithm for the experiment results shown in Section 5.7. Please note that there are cases in which a configuration with fewer \#Iterations or \#PopSize than others obtain the same HV; that is, the algorithm converges quickly. In that case, the configuration with less \#Iterations or \#PopSize is considered as the winner.

Tables A.6-A.11 show the results for FEDA, AGE-MOEA-II ${ }^{\mathrm{a}}$, CTAEA ${ }^{\mathrm{c}}$ UMDA ${ }^{\mathrm{d}}$, PBIL ${ }^{\mathrm{e}}$ and MIMIC ${ }^{\mathrm{c}}$, respectively. In each table, the configuration with a greater number of wins can be interpreted as the recommended best configuration, and is that applied in our experiments.
