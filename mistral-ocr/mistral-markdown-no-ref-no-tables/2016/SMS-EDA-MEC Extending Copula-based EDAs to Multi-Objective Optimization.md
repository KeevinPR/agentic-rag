# SMS-EDA-MEC: Extending Copula-based EDAs to Multi-Objective Optimization 

Luis Martí* ${ }^{\dagger}$, Harold D. de Mello Jr. $\ddagger$, Nayat Sanchez-Pi $\ddagger$ and Marley Vellasco ${ }^{\S}$<br>*Universidade Federal Fluminense, Niterói (RJ) Brazil<br>${ }^{\dagger}$ TAO team, CNRS/INRIA/LRI, Université Paris-Saclay, Paris, France.<br>${ }^{\ddagger}$ Universidade do Estado do Rio de Janeiro, Rio de Janeiro (RJ) Brazil<br>${ }^{\S}$ Pontifícia Universidade Católica do Rio de Janeiro, Rio de Janeiro (RJ) Brazil


#### Abstract

It can be argued that in order to produce a substantial improvement in multi-objective estimation of distribution algorithms it is necessary to focus on a particular group of issues, in particular, on the weaknesses derived from multiobjective fitness assignment and selection methods, the incorrect treatment of relevant but isolated (precursor) individuals; the loss of population diversity, and the use of 'general purpose' modeling algorithms without taking note of the particular requirements of the task. In this work we introduce the $\mathcal{S}$-Metric Selection Estimation of Distribution Algorithm based on Multivariate Extension of Copulas (SMS-EDA-MEC). SMS-EDA-MEC was devised with the intention of dealing with those issues in mind. It builds the population model relying on the comprehensive Clayton's copula and incorporates methods for automatic population restarting and for priming precursor individuals. The experimental studies presented show that SMS-EDA-MEC yields better results than current and 'traditional' approaches.


## I. INTRODUCTION

Many real-world optimization problems involve more than one objective function to be optimized simultaneously. These type of problem is known as multi-objective optimization problems (MOPs). In the general case, finding the solution of a MOP is an $N P$-complete problem [1]. Because of that, metaheuristic approaches are necessary. MOP-related research has seen a great deal of development as a result of the involvement of the evolutionary computation community. This fact has lead to the creation of multi-objective evolutionary algorithms (MOEAs) (cf. [2]).

The scalability issues of MOEAs with regard to the number of objective functions problems have triggered a sizable amount of research that aims to provide alternative approaches that can properly handle what has been denominated as the many-objective problems.

The inclusion of learning as part of the search process has been pointed out as a relevant alternative to "traditional" MOEAs [3]. Multi-objective estimation of distribution algorithms (MOEDAs) [4] are one of those alternatives, as they are capable of learning the problem structure. Estimation of distribution algorithms (EDAs) replace the application of evolutionary operators with the creation of a statistical model of the fittest elements of the population in a process known as model building. This model is then sampled to produce new elements.

However, MOEDAs have not yielded the anticipated results. An analysis of this issue [5] lead us to distinguish a number
of possible shortcomings, in particular: i) weaknesses derived from multi-objective fitness assignment and selection methods; ii) the incorrect treatment of precursor individuals - that is, relatively isolated and relevant individuals-; iii) the loss of population diversity; and iv) the use of 'general purpose' modeling algorithms for model building without taking into account that MOPs have particular requirements that should be addressed.

In recent years different EDA models based on copula theory [6], [7] have been proposed. However, in spite of its a priori advantages, there has been paid relatively little attention to the application of copula-based approaches to multiobjective optimization. For instance, Gaussian and $t$ copulas have already been used in optimization, mainly in the variable space to estimate distribution in evolutionary algorithms [8], [9]. Similarly, [10] focused on objective space by proposing a first estimation of the Pareto front relying on Archimedean copulas. [11], [12] also focused on Archimedean copulas for their ability to model dependence in high dimensions with only one parameter, which has the positive effect of speeding up multi-objective optimization computation time.

In this paper we propose a novel MOEDA algorithm: the $\mathcal{S}$ Metric Selection Estimation of Distribution Algorithm based on Multivariate Extension of Copulas (SMS-EDA-MEC). SMS-EDA-MEC deals with the above issues by combining the successful $\mathcal{S}$-metric selection mechanism [13] with an augmented version of the (single-objective) Estimation of Distribution Algorithm based on Multivariate Extension of Copulas (EDA-MEC) [14] which relies on Clayton's copula [15] and is complemented with heuristics meant to avoid loss of population diversity and to promote search by priming precursor individuals.

As part of the proposal we present a discussion on current MOEDA issues and drawbacks and how to overcome them. We formally described SMS-EDA-MEC and its components and a series of experiments on community-accepted benchmarks. These experiments are devised to study the influence of each of the improvements that are put forward as part of the proposal and to compare our approach with comparable state-of-the-art and 'classical' algorithms.

The rest of the paper is organized as follows. It first introduces the theoretical support matters that are required for correctly understanding the proposal. Subsequently, in Section

III, we describe the essential elements of EDA-MEC, as they are central to our proposal. Next, SMS-EDA-MEC is then presented in Section IV. Following that, in Section V, we present the experimental results that have been carried out. Finally, in Section VI, some final remarks are put forward.

## II. Foundations

In this section we briefly describe the theoretical pillars that support our proposal.

## A. Multi-Objective Optimization

A MOP can be expressed as the problem in which a set of objective functions $f_{1}(\boldsymbol{x}), \ldots, f_{M}(\boldsymbol{x})$ should be jointly optimized;

$$
\min \boldsymbol{F}(\boldsymbol{x})=\left\langle f_{1}(\boldsymbol{x}), \ldots, f_{M}(\boldsymbol{x})\right\rangle ; \boldsymbol{x} \in \mathcal{S}
$$

where $\mathcal{S} \subseteq \mathbb{R}^{n}$ is known as the feasible set and could be expressed as a set of restrictions over the decision set, in our case, $\mathbb{R}^{n}$. The image set of $\mathcal{S}$ produced by function vector $\boldsymbol{F}(\cdot), \mathcal{O} \subseteq \mathbb{R}^{M}$, is called feasible objective set or criterion set.

The solution to these type of problems is a set of trade-off points. The optimality of a solution can be expressed in terms of the Pareto dominance relation.

Definition 1 (Pareto dominance relation): For the optimization problem specified in (1) and having $\boldsymbol{x}, \boldsymbol{y} \in \mathcal{S}, \boldsymbol{x}$ is said to dominate $\boldsymbol{y}$ (expressed as $\boldsymbol{x} \prec \boldsymbol{y}$ ) iff $\forall f_{j}, f_{j}(\boldsymbol{x}) \leq f_{j}(\boldsymbol{y})$ and $\exists f_{i}$ such that $f_{i}(\boldsymbol{x})<f_{i}(\boldsymbol{y})$.

Definition 2 (non-dominated subset): In problem (1) and having the set $\mathcal{A} \subseteq \mathcal{S}$. $\overline{\mathcal{A}}$, the non-dominated subset of $\mathcal{A}$, is defined as

$$
\overline{\mathcal{A}}=\left\{\boldsymbol{x} \in \mathcal{A} \mid \nexists \boldsymbol{x}^{\prime} \in \mathcal{A}: \boldsymbol{x}^{\prime} \prec \boldsymbol{x}\right\}
$$

The solution of (1) is $\overline{\mathcal{S}}$, the non-dominated subset of $\mathcal{S}$. $\overline{\mathcal{S}}$ is known as the efficient set or Pareto-optimal set [16]. The Pareto-optimal front, $\overline{\mathcal{O}}$, is the image of $\overline{\mathcal{S}}$ in the feasible objective set.

If problem (1) has certain characteristics, e. g., linearity or convexity of the objective functions or convexity of $\mathcal{S}$, the efficient set can be determined by mathematical programming approaches [16]. However, in the general case, finding the solution of (1) is an $N P$-complete problem [1]. In this case, heuristic or metaheuristic methods, like evolutionary algorithms, can be applied in order to have solutions of practical value at an admissible computational cost.

## B. $\mathcal{S}$-Metric Selection Evolutionary Multiobjective Optimization Algorithm

The $\mathcal{S}$-metric selection evolutionary multiobjective optimization algorithm (SMS-EMOA) [13] is an steady-state algorithm. Which means that, in every iteration, only one individual is created and only one has to be deleted from the population in each generation.

The key element of SMS-EMOA is the method for determining which element of the population will be substituted by the offspring. This is done, by applying a non-domination
ranking. From the individuals that are dominated by the rest of the population, one individual is selected such that it has the minimum contribution to the hypervolume [17] of the set. This individual is to be removed from the population and substituted by a new individual generated by the usual variation operators. It may happen, that there is only one non-dominated front (all individuals are non-dominated). In this case, the individual with least hypervolume contribution is selected.

## C. MOEAs Stagnation Detection and Stopping Criteria

The formal determination of convergence or optimality criteria in MOPs (and MOEAs, for that matter) is often impossible when gradient information is not available. This is a common situation in real-world application. Because of that, sophisticated heuristic stopping criteria have become a subject of intensive research [18]. The on-line convergence detection criterion (OCD) [18] is a robust method for convergence detection. OCD computes a set of performance indicators applying them on a given number of consecutive populations. Relying on the values of the performance indicators, OCD determines if they have remained stable in a non-progress state applying an statistical hypothesis test. In this work we use OCD to determine if the algorithm has become stagnated and, therefore, a part of the population should be restarted.

## D. Multi-Objective Estimation of Distribution Algorithms

As already mentioned in the previous section, estimation of distribution algorithms (EDAs) are a class of optimization algorithms that combine evolutionary computation, statistical modeling, and machine learning. The most important step and bottleneck- of EDAs is estimating the joint probability distribution associated with the variables from the most promising solutions determined by the evaluation function. One main advantage of EDAs is that the search distribution may encode dependences between the domain problem parameters, thus performing a more effective search.

Multi-objective optimization EDAs (MOEDAs) are the extensions of EDAs to the multi-objective domain. Most MOEDAs are a modification of existing EDAs whose fitness assignment strategy has been replaced by a previously existing method used by MOEAs.

## E. Copulas

The concept of copulas was introduced by Sklar [6], but remained largely dormant until it was applied to finance only many years later [7]. Currently, copulas constitute a very useful tool for allowing the construction of multivariate models that adequately characterize linear and nonlinear dependencies between the variables of a problem.

Formally, a function $C\left(u_{1}, \ldots, u_{n}\right):[0,1]^{n} \rightarrow[0,1]$ is an $n$-dimensional copula if it satisfies axiomatic conditions related to boundary conditions and increasing property [19]. Thus, copula $C$ is a distribution function in $[0,1]^{n}$ that has marginal uniform functions $u_{k} \in(0,1)$, with $k=1, \ldots, n$.

According to Sklar's theorem [6], a joint cumulative distribution function (JCDF), $F$, of random variables $X_{1}, X_{2}, \ldots, X_{n}$, with continuous marginal distributions

$F_{1}, F_{2}, \ldots, F_{n}$, respectively, can be characterized by a single $n$-dimensional dependence function or copula $C$, such that for all vectors $\boldsymbol{x} \in \mathbb{R}^{n}$ :

$$
F\left(x_{1}, x_{2}, \ldots, x_{n}\right)=C\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \ldots, F_{n}\left(x_{n}\right)\right)
$$

As an alternative representation, (2) can be written in the inverted form. For any vector $\boldsymbol{u} \in[0,1]^{n}$ :

$$
\begin{gathered}
C\left(u_{1}, u_{2}, \ldots, u_{n}\right)=\boldsymbol{F}\left[F_{1}^{-1}\left(u_{1}\right), F_{2}^{-1}\left(u_{2}\right), \ldots\right. \\
\left.F_{n}^{-1}\left(u_{n}\right)\right]
\end{gathered}
$$

where $C_{F}$ denotes the copula associated with $F$ and $F^{-1}(\boldsymbol{u})=$ $\inf \left\{x \in \mathbb{R} \mid F_{i}\left(x_{i}\right) \geq \boldsymbol{u}\right\}$ with $i=1, \ldots, n$, constitutes the generalized inverse function of $F$. Then $x_{1}=F_{1}^{-1}\left(u_{1}\right) \sim$ $F_{1}, \ldots, x_{n}=F_{n}^{-1}\left(u_{n}\right) \sim F_{n}$. It follows that an $n$-copula is a multivariate distribution with all $n$ univariate margins being uniformly distributed as $U(0,1)$.

A particular group of copulas that has proved useful in empirical modeling is the Archimedean class. In addition to the fact that many parametric copulas are Archimedean, their most common subclasses can i) be expressed in an explicit closed form and ii) capture wide ranges of dependence. Nevertheless, this type of copula is not directly derived from Sklar's theorem. For the bivariate case, this copula holds the following representation:

$$
C\left(u_{1}, u_{2}\right)=\varphi^{-1}\left(\varphi\left(u_{1}\right)+\varphi\left(u_{2}\right)\right)
$$

where $u_{1}, u_{2} \in(0,1), \varphi(\cdot)$ is known as a generator function of the copula, and $\varphi^{-1}$ is its inverse.

Different generator functions yield different Archimedean copulas when plugged into (4). Several Archimedean copula families are described in [19]; most of them depend on a single parameter $\theta$ that controls the dependence structure and is embedded in the functional form of the generator. Quantifying dependence is relatively straightforward for Archimedean copulas because Kendall's $\tau$ simplifies to a function of the generator function.

When $\varphi(t)=t^{-\theta}-1$, a family of the Clayton's bivariate copula [15] is generated. It is one of the most frequently used and best known Archimedean copulas in empirical applications and takes the form

$$
C\left(u_{1}, u_{2}\right)=\left(u_{1}^{-\theta}+u_{2}^{-\theta}-1\right)^{-1 / \theta}
$$

The Clayton family has lower-tail dependence $2^{-1 / \theta}$ but does not have upper-tail dependence. In this copula, the perfect dependence among the random variables occurs when $\theta \rightarrow \infty$, while $\theta=1$ indicates total independence among the variables. The Clayton copula's parameter is often estimated via Kendall's $\tau[19]$ :

$$
\tau=\frac{\theta}{\theta+2}
$$

An additional advantage of Archimedean copulas is that they can be easily used to generate multivariate distributions from extensions of Archimedean 2-copulas. Although, the simplest method used in this work is named an exchangeable multivariate Archimedean copula (EAC), it poses a limitation:
the dependence structure between any pair of variables is described by the same parameter $\theta$, regardless of dimension. In this respect, copulas created by the nesting of Archimedean copula generators and pair-copulas models [20] are more flexible.

## F. Copula-based Estimation of Distribution Algorithms

In recent years, a new approach for developing EDAs to solve real-valued optimization problems has been developed based on copula theory, the Copula-based Estimation of Distribution Algorithms (CEDAs). The first attempt to associate copulas with EDAs was a technical report [21]. Since then, a considerable number of CEDAs have been proposed in the literature. See [22] to a review. Nonetheless, most EDAs are applicable to single-objective problems and only a few CEDAs have been proposed to deal with multi-objective problems.

In CEDAs, the step for estimating the probabilistic model is divided into two parts: i) estimating the marginal distributions, $F_{i}$, for $i=1, \ldots, n$, and ii) estimating the dependence structure. Typically, a specific distribution is assumed to be the correct distribution for each marginal distribution, and its parameters are estimated based on maximum likelihood. In other cases, kernel density estimators (KDE), marginal empirical distributions or estimators based on Kendall's inversion were used.

After the marginal distributions are estimated, the selected population is transformed into uniform variables in the interval $(0,1)$ by evaluating each cumulative marginal distribution. This transformed population is then used to estimate a copulabased model $C$ that describes the dependence among the variables.

## III. The EDA BASED ON Multivariate Extension of Copulas

The Estimation of Distribution Algorithm based on Multivariate Extension of Copulas (EDA-MEC) [14] is a Copulabased EDA that implements two approaches to also address the previously described issues of restarting and precursor individuals handling. In this work we extend EDA-MEC to the multi-objective problem domain. Therefore, it is convenient to describe the single-objective version first.

The use of copulas in EDAs can simplify their operation, once the construction of the probability models is performed in less time and with greater accuracy than other estimation techniques. Since a copula completely determines the dependence structure of variables and the multivariate distribution $F$ is obtained by (2), the issue of estimating the probabilistic model of a copula-based EDA is split into two parts:

1) selecting or building the copula $C$, and
2) estimating each univariate marginal $F_{i}$ for $i=1, \ldots, n$. After estimating the probabilistic model, the next step is sampling it to generate the new solutions. In order to do this, the algorithm generates a random vector $\left\{u_{1}, u_{2}, \ldots, u_{n}\right\} \in$ $[0,1]^{n}$ that follows $C$ (basic property of the copula theory). Next, the $x_{i}$ values are calculated by the inverse function of their corresponding marginal, i.e., $x_{i}=F^{-1}\left(u_{i}\right)$, thereby

generating a new individual $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ that is a sample that follows the multivariate distribution $F$.

Thus, the most significant differences between copula-based EDAs reside in the steps of learning, construction and sampling of the probabilistic model. [14] generated a random variable $\left\{u_{1}, u_{2}, \ldots, u_{n}\right\}$ from the Clayton's copula using the Marshall and Olkin's method for constructing multivariate copulas [7], [23]. The dependence parameter $(\theta)$ was estimated dynamically with an alternative and less computationally intense method compared to other copula-based EDAs. In this method, the correlation matrix for all variables is calculated using the current population as the data inputs. Subsequently, it was possible to calculate Kendall's $\tau$ and to obtain the parameter $\theta$ for Clayton's copula using (6).

Additionally, EDA-MEC incorporates a restarting method proposed in [14], [24] to maintain the population diversity and avoid the premature convergence. Whenever the perfect dependence among the random variables occurs $(\theta \rightarrow \infty)$, the best individual is retained, a population's percentage is restarted uniformly in the feasible set, and the remaining population is restarted uniformly within the limits of the best individual variables at that generation. Nevertheless, the population size is not changed after a restarting that differ from the mechanisms cited previously. Subsequently, a new rank matrix is calculated.

Subsequently, $x_{i}$ new individuals are generated using the calculated dependence parameter and the samples $\mathbf{u}$ from the Clayton's copula. This offspring population is merged with the parents. After that, the worst individuals are selected from the merged population and removed from it.

After a transformation in the samples generated in the next step, precursors $r_{n}=F_{n}^{-1}\left(1-u_{n}\right)$ are generated. According to [14] the precursor individuals correspond to samples of a new probability distribution is obtained as a variation of the learned one so as to generate individuals with a lower probability of appearing in the evolutionary process. This concept has been used to determine the inverse probability for discrete variables [25] and explore other regions of the search space which helps to avoid premature convergence. It consists of using the information which is contained in the probabilistic model to generate individuals which introduces diversity. It must be highlighted that the precursor individuals do not necessarily have to be obtained from the complement of samples; they can be generated from any process able to explore other regions of the search space.

Finally, the $r_{n}$ individuals replace the worst individuals from the resulting population. This entire process is repeated until a stop condition is attained, and the best individual is found.

## IV. $\mathcal{S}$-METric SELECTION EDA-MEC

The $\mathcal{S}$-Metric Selection EDA-MEC (SMS-EDA-MEC) extrapolates the concepts developed for EDA-MEC to the multiobjective optimization problem domain by combining it with the multi-objective $\mathcal{S}$-metric selection mechanism. Although the ideas put forward by EDA-MEC are valid in the multi-
objective case some modifications are necessary to deal with the particularities of the problem.

## A. Restarting in the Multi-Objective Case

In EDA-MEC, the need for restarting is established by either the difference between the values of the objective function of the best and worst individuals being too small, the loss of population diversity, or after a given number of iterations had passed. The first condition can not be directly extrapolated to the multi-objective domain. Instead, what is necessary is to determine when progress towards the Pareto-optimal front is taking place too slow pace. That situation can be detected with the OCD stopping criteria described in Section II-C. OCD can be configured in such way as to not detect convergence in the most strict way but to detect (momentarily) stagnation situations that might be good candidates for restarting. Similarly, SMS-EDA-MEC extends the idea of population diversity by measuring the approximated volume of the convex hull [26] defined by the individuals in feasible set. In this point, it should be mentioned that other diversity indicators could be used. They will be explored in future works.

After the conditions for restart are met, care should be taken not to make an excessively aggressive restart. In EDAMEC the whole population with the exception of the best individual was restarted. In the multi-objective case, there is more than one optimal solution and hence, equally good (non-dominated) individuals represent different trade-off of the objective functions. Therefore restarting, although needed should substitute a relatively small amount of individuals.

Taking these arguments into consideration, in SMS-EDAMEC restarting takes place by generating two sets of restarted individuals, $\mathcal{P}_{\text {local }}^{\text {restarted }}$ that does a 'local' restart and its 'global' counterpart, $\mathcal{P}_{\text {global }}^{\text {restarted }}$, such that

$$
\left|\mathcal{P}_{\text {local }}^{\text {restarted }}\right|=\left|\mathcal{P}_{\text {local }}^{\text {restarted }}\right|=\frac{\left\lceil\nu n_{\text {pop }}\right\rceil}{2}
$$

where $\nu$ is the restarting percentile that control how much of the population is to be substituted by restarted individuals.
$\mathcal{P}_{\text {local }}^{\text {restarted }}$ is created by sampling a uniform distribution on the interval of the feature set currently occupied by the population $\mathcal{P}$ as,

$$
\mathcal{P}_{\text {local }}^{\text {restarted }}=\left\{x \sim U\left(\ell^{\text {lower }}, \ell^{\text {upper }}\right)\right\}
$$

where $\ell_{i}^{\text {lower }}=\min _{\# \in \mathcal{P}}\left(x_{i}\right)$ and $\ell_{i}^{\text {lower }}=\max _{\# \in \mathcal{P}}\left(x_{i}\right)$ for $i=1, \ldots, n$.

Having $\mathcal{P}_{\text {local }}^{\text {restarted }}$ and $\mathcal{P}_{\text {global }}^{\text {restarted }}$ they are merged with the original population $\mathcal{P}$ by substituting randomly selected individuals from it.

It should be noted that in practical applications it is convenient to disable restarting in the last part of the optimization. For example, in our experiments we included a condition to prevent restarting in the last $10 \%$ of the execution of the algorithm.

## B. The SMS-EDA-MEC Algorithm

The SMS-EDA-MEC algorithm goes by creating an initial population, $\mathcal{P}_{0}$, of $n_{\text {pop }}$ random individuals.

Then, the optimization loop starts by determining if the current population, $\mathcal{P}_{t}$, calls for a restart. This decision is made relying on the $\mathrm{OCD}(\cdot)$ and convex_hull_volume $(\cdot)$ functions as described in Section IV-A and forcing a pause of $\Delta t_{\text {restart }}$ iterations between restarts to avoid continuous restarting. If a restart is required the restarted population is computed by the restart $(\cdot)$ function.

After that the Clayton's copula $C$ is estimated from the population by function estimate_copula $(\cdot)$. This copula is used to synthesize $n_{\text {off }}$ individuals that are united with the current population to form $\mathcal{P}^{\prime}$.

Subsequently, the $\mathcal{S}$-metric selection mechanism is applied to $\mathcal{P}^{\prime}$. That is, individuals are removed from $\mathcal{P}^{\prime}$ until its size reaches $n_{\text {pop }}-\left\lceil\varepsilon n_{\text {pop }}\right\rceil$ Here $\varepsilon$ regulates how many precursor individuals will be kept across iterations. Individuals to be removed are selected by their hypervolume contribution by function worst_individual $(\cdot)$.

At this point, the subset $\Upsilon \subseteq \mathcal{P}_{t}$ containing $\left\lceil\varepsilon n_{\text {pop }}\right\rceil$ precursor individuals are generated as described in Section III using as reference $\mathcal{P}_{t}$ by function precursors $(\cdot)$. The selected precursors, $\Upsilon$ and the selected offspring $\mathcal{P}^{\prime}$ are combined to form to population of the next generation,

$$
\mathcal{P}_{t+1}=\mathcal{P}+\Upsilon
$$

Figure 1 details the aforementioned process as pseudocode.

## V. EXPERIMENTS

This section reports the results of the experiments involving different variants of SMS-EDA-MEC and some of the current state-of-the-art MOEDAs and MOEAs in a set of current community-accepted problems.

As stated, the scope of the experiments is to not only compare our proposal with similar approaches. SMS-EDAMEC implements different features, that is, model building using copulas, the restarting procedure and the selection of precursors. Therefore, it is also important to identify which of those features have a more relevant contribution in a positive outcome. That is why the test includes the complete SMS-EDA-MEC, identified as SMS-EDA-MEC+RP, as it includes restarting and precursors, SMS-EDA-MEC with restart (SMSEDA-MEC+R), SMS-EDA-MEC with precursors (SMS-EDA-MEC+P) and SMS-EDA-MEC without restarting and precursors (SMS-EDA-MEC-RP).

Besides SMS-EDA-MEC, we also tested MONEDA [5], [27], MAMal.GaM-X+ [28], naïve MIDEA [29] MO-CMAES [30] and MrBOA [31] MOEDAs and the SMS-EMOA [13], NSGA-II [2] and NSGA-III [32] MOEAs.

MONEDA and MAMal.GaM-X+ have been included as they put forward approaches to improve MOEDAs by correctly handling precursor and restarting, although. Naïve MIDEA and MrBOA, on the other hand, are well-known and established MOEDAs. It is interesting to compare our results against the ones yielded by SMS-EMOA as it allows to assess the impact of the EDA component as optimization search engine. Similarly, NSGA-II is a popular and well-known MOEA, while NSGA-III builds upon it and uses an approach

## Parameters:

$\triangleright n_{\text {pop }} \in \mathbb{N}$, population size.
$\triangleright n_{\text {off }} \in \mathbb{N}$, number of offspring to generate.
$\triangleright \varepsilon \in[0,1]$, precursor selection percentile.
$\triangleright \nu \in[0,1]$, restarting percentile.
$\triangleright \sigma_{\min } \in \mathbb{R}^{+}$, minimum OCD variance for restarting.
$\triangleright \Delta t_{\mathrm{OCD}} \in \mathbb{N}$, number of iterations to apply OCD.
$\triangleright \gamma \in \mathbb{R}^{+}$, population convex hull volume threshold.
$\triangleright \Delta t_{\mathrm{r}} \in \mathbb{N}$, min. number of iterations before restarts.

## Algorithm:

$t \leftarrow 0, t_{\mathrm{r}} \leftarrow 0, \mathfrak{P} \leftarrow \varnothing$.
$\mathcal{P}_{0} \leftarrow$ random_population $\left(n_{\text {pop }}\right)$.
while not end_condition $\left(\mathcal{P}_{t}\right)$ do
$\mathfrak{P}=\mathfrak{P} \cup\left\{\mathcal{P}_{t}\right\}$.
if $t>\Delta t_{\mathrm{OCD}}$ and
$t-t_{\mathrm{r}}>\Delta t_{\mathrm{r}}$ and
$\left[\mathrm{OCD}\left(\mathfrak{P}, \sigma_{\min }, \Delta t_{\mathrm{OCD}}\right)=\right.$ true or
convex_hull_volume $\left.\left.\left(\mathcal{P}_{t}\right)<\gamma\right]$ then
$t_{\mathrm{r}} \leftarrow t$. // doing restart
$\mathcal{P}_{t} \leftarrow \operatorname{restart}\left(\mathcal{P}_{t},\left\lceil\nu n_{\text {pop }}\right\rceil\right)$.
end if
$C \leftarrow$ estimate_copula $\left(\mathcal{P}_{t}\right)$.
$\mathcal{P}^{\prime} \leftarrow \mathcal{P}_{t} \cup$ sample_copula $\left(C, n_{\text {off }}\right)$.
while $\left|\mathcal{P}^{\prime}\right|>n_{\text {pop }}-\left\lceil\varepsilon n_{\text {pop }}\right\rceil$ do
$\mathcal{P}^{\prime} \leftarrow \mathcal{P}^{\prime} \backslash\left\{\right.$ worst_individual $\left.\left(\mathcal{P}^{\prime}\right)\right\}$.
end while
$\Upsilon \leftarrow$ precursors $\left(\mathcal{P},\left\lceil\varepsilon n_{\text {pop }}\right\rceil\right)$.
$\mathcal{P}_{t+1} \leftarrow \mathcal{O} \cup \Upsilon$.
$t \leftarrow t+1$.
end while
return $\mathcal{P}$, the non-dominated subset of $\mathcal{P}_{t}$.
Figure 1. Algorithmic description of SMS-EDA-MEC. See Table ?? for a description of the functions used.
based on reference points to yield a better performance in higher objective dimensions.

We selected the Walking Fish Group multi-objective problem toolkit [33] as benchmark tests. It describes nine complex problems (from WFG1 to WFG9) that test whether the optimization algorithms are capable of handling different challenges, like separability, multi-modality, deceptive local optima, etc.

Each problem was addressed with 3, 5, 7 and 9 objectives. The number of objective function evaluation was used as stopping criterion, stopping the execution of the algorithm when the number of evaluations reached $10^{3+\frac{M}{2}}$, thus allowing longer runs for more complex problems. Population sizes for the algorithms were to automatically increase with problem dimension as $n_{\text {pop }}=50 \times 10^{\frac{M}{2}}$.

In these experiments, SMS-EDA-MEC was run with $n_{\text {off }}=$ $n_{\text {pop }}, \varepsilon=0.1, \nu=0.1, \sigma_{\min }=10^{-5}, \Delta t_{\mathrm{OCD}}=15, \gamma=10^{-5}$ and $\Delta t_{\text {restart }}=10$. The parameters of the other algorithms were set as in the respective referenced papers. For each algorithm/problem/number-of-objectives combination 30 runs of the algorithm were executed in order to have statistically

valid results.
The stochastic nature of the algorithms prompts the use of statistical tools in order to reach a valid judgement of the quality of the solutions and how different algorithms compare with each other. Box plots [34] are one of such representations and have been repeatedly applied in our context. Although box plots allows a visual comparison of the results and, in principle, some conclusions could be deduced out of them.

Figure 2 shows the results of the experiments in the form of box plots. Examining that figure it becomes evident that SMS-EDA-MEC is able to consistently yield good results across all problems and number of objectives.

Although illustrative, box plots can not be used to reach a definitive conclusion. That is why statistical hypothesis tests are called for. In our case, for each problem/dimension combination, we performed a Kruskal-Wallis test [35] with the indicator values yielded by each algorithm's run. In this context, the null hypothesis of this test is that all algorithms are equally capable of solving the problem. If the null hypothesis was rejected, which was actually the case in all instances of the experiment, the Conover-Inman procedure [36] was applied in a pairwise manner to determine whether one algorithm had significantly better results than another. A significance level, $\alpha$, of 0.05 , corrected using the Dunn-Šidák correction was used for all tests.

The separate results of the tests in tabular form could not be included in the paper because of the imposed length restrictions ${ }^{1}$. It is evident, that, in any case, comprehensive analysis of the results is rather difficult as it implies cross-examining and comparing the results presented separately. That is why we decided to adopt a more integrative representation such as the one proposed in [37]. That is, for a given set of algorithms $A_{1}, \ldots, A_{K}$, a set of $P$ test problem instances $\Phi_{1, m}, \ldots, \Phi_{P, m}$, configured with $m$ objectives, the function $\delta(\cdot)$ is defined as

$$
\delta\left(A_{i}, A_{j}, \Phi_{p, m}\right)= \begin{cases}1 & \text { if } A_{i} \gg A_{j} \text { solving } \Phi_{p, m} \\ 0 & \text { in other case }\end{cases}
$$

where the relation $A_{i} \gg A_{j}$ defines if $A_{i}$ is significantly better than $A_{j}$ when solving the problem instance $\Phi_{p, m}$, as computed by the statistical tests previously described.

Relying on $\delta(\cdot)$, the performance index $P_{p, m}\left(A_{i}\right)$ of a given algorithm $A_{i}$ when solving $\Phi_{p, m}$ is then computed as

$$
P_{p, m}\left(A_{i}\right)=\sum_{j=1 ; j \neq i}^{K} \delta\left(A_{i}, A_{j}, \Phi_{p, m}\right)
$$

This index intends to summarize the performance of each algorithm with regard to its peers.

Figures 3a and 3b exhibit the results computing the performance indexes grouped by problems and dimensions.

[^0]Figure 3a represents the mean performance indexes yielded by each algorithm when solving each problem in all of its configured objective dimensions,

$$
\bar{P}_{p}\left(A_{i}\right)=\frac{1}{|\mathcal{M}|} \sum_{m \in \mathcal{M}} P_{p, m}\left(A_{i}\right)
$$

Similarly, Figure 3b presents the mean values of the index grouped by for each feasible objective set dimension,

$$
\bar{P}_{m}\left(A_{i}\right)=\frac{1}{P} \sum_{p=1}^{P} P_{p, m}\left(A_{i}\right)
$$

with $m=\{3,5,7,9\}$.
These figures lead to solid conclusions. They allow us to assert that SMS-EDA-MEC with restarting and precursors has consistently outperformed the other approaches. It is also noticeable the importance of restarting and precursors. Both SMS-EDA-MEC+R and SMS-EDA-MEC+P yielded better results than the 'plain' (-RP) version. The only case where SMS-EDA-MEC was outperformed by other algorithm was by MONEDA, an algorithm that also has as working principle the correct handling of precursors.

## VI. Final Remarks

The present paper introduced the $\mathcal{S}$-Metric Selection EDAMEC (SMS-EDA-MEC), which is the extension to the multiobjective domain of the Estimation of Distribution Algorithm based on Multivariate Extension of Copulas (EDA-MEC). SMS-EDA-MEC constructs its model of the population relying on the Clayton's copula and includes a process for automatic population restarting to overcome early stagnation and a novel mechanism to prioritize precursor areas of the feasible set. These features have rendered SMS-EDA-MEC capable of outperforming the other approaches included in the experiments.

In spite of the promising results obtained so far further studies are necessary. More experiments are necessary in order to gain a better comprehension of the proposed algorithm. In one hand, different test problems must be addressed to realize if the results obtained here can be generalized. On the other hand, it is also of interest to further scale the problems to more objective functions. The analysis of the behavior of the algorithms in those situations might lead to their adaptation to the problem.

From a theoretical perspective some points still need to be explored. For example, a computational cost and complexity study is necessary in order to grasp the resource consumption of SMS-EDA-MEC when advancing into higher dimensions. Because of its reliance on computationally demanding components, like the hypervolume indicator, it is necessary to assess lower-cost variants, like the approximation of the hypervolume via Monte Carlo sampling. On the other hand, more model building approaches based on copulas should be studied. Such models could be found by doing a more exhaustive survey or by proposing completely new ones. If such approaches show themselves as efficient as the one described here, it would help to corroborate the working hypothesis of this contribution.


[^0]:    ${ }^{1}$ The tables with the results of the statistical tests are available online at http://lmarti.com/smsedamec-cec2016.

![img-0.jpeg](img-0.jpeg)

Figure 2. Box plots produced by the experiments organized by number of objectives $(M=\{3,5,7,9\})$ and problem.
![img-1.jpeg](img-1.jpeg)
(a) Mean values of the performance index grouped by problem.
(b) Mean values of the performance index grouped by number of objectives.

Figure 3. Summaries of the statistical hypothesis tests grouped by problem and by number of objectives.

# ACKNOWLEDGMENT 

This works has been partially supported by the National Counsel of Technological and Scientific Development (CNPq)

BJT Project 407851/2012-7 and Carlos Chagas Filho Research Support Foundation (FAPERJ) APQ1 Project 211.451/2015. Authors want to thank the reviewers for their fruitful and

encouraging comments. The source code open and available at http://lmarti.com/smsedamec-cec2016.
