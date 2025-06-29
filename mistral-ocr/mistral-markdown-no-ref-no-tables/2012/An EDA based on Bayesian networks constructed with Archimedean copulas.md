# An EDA Based on Bayesian Networks Constructed with Archimedean Copulas 

Mario Rogelio Flores Méndez and Ricardo Landa<br>Information Technology Laboratory<br>CINVESTAV Tamaulipas<br>Cd. Victoria, Tamaulipas, MEXICO<br>Email: mflores@tamps.cinvestav.mx, rlanda@tamps.cinvestav.mx


#### Abstract

In this paper, an estimation of distribution algorithm that adopts a copula Bayesian network as probabilistic graphic model is presented. Multivariate Archimedean copula functions with one parameter are used to model the dependences between variables and the beta distribution is used to describe the univariate marginals. The learning process of the Bayesian network is assisted through a simple technique that relies on the associative property of Archimedean copulas, the use of Kendall's tau coefficient for measuring relations between variables and the relation between tau coefficients and bivariate Archimedean copulas. This paper presents the proposal, together with some initial experiments, which show encouraging results.


Keywords-numerical optimization; estimation of distribution algorithm; Archimedean copulas

## I. INTRODUCTION

Optimization is a task present in many fields of human activity. Optimization problems range from very easy to solve to quite challenging problems, especially for classical methods. This is the case when metaheuristics are valuable.

A possible source for hardness of problems is when the number of decision variables increases, particularly if the interdependences between variables are strong.

Estimation of distribution algorithms (EDAs) are a special type of metaheuristics, which aim is to extract information about the probability distribution an evolutionary algorithm would follow when generating new solutions (sampling), building a probabilistic model. Additionally, the model can be constructed trying to capture the relations between variables, and thus taking advantage of the characteristics of the problem.

However, in the literature of state of the art, the reader can notice the predominant use of probabilistic graphical models in EDAs due to the good results they exhibit, but at the same time, exists a lack of them in EDAs that use copulas. Similarly, most of the work up to the date in EDAs that use copulas, only adopts one copula throughout the entire algorithm, which restricts the kind of dependences that can be described and exploited by the algorithm.

Such situations are the main motivations of this work. Here, we propose the use of a copula bayesian network, which is a probabilistic graphical model recently proposed and not yet implemented in numerical EDAs. However, results of their use on combinatorial EDAs are very promising.

Other type of networks are also good options for numerical optimization, such as Bayesian networks or Gaussian networks, so it is worth trying a new probabilistic model. On the other hand we employ three copulas from the Archimedean family to describe different types of dependences, with the aim of the algorithm to capture a wide range of relations between variables.

The rest of the paper is organized as follows: in Section II, the state of the art is summarized; in Section III, some concepts needed for the current proposal are enumerated; in Section IV, the proposed approach is described; in Section V are shown some preliminary results obtained by this proposal; finally, in Section VI, some conclusions are metioned, together with some work that remains to be done and future research ideas.

## II. PREVIOUS WORK

In this section a brief review of the state of the art is presented. Such techniques are grouped according to the approach for representing the search space and the complexity for representing the relations between variables.

## A. Discretization of the Search Space

This type of approaches make divisions of each decision variable, basically by the use of histograms. In [1], [2], [3] the authors propose the use of fixed length or fixed height histograms. In [4] a technique for discretizing on demand is proposed, on models for combinatorial optimization.

## B. Direct Representations

1) Without Dependences: Here, variables are supposed to be independent from one another, so the joint density function of vector $\vec{x}=\left[x_{1}, x_{2}, \ldots, x_{n}\right]$ of decision variables can be factorized as $p(\vec{x})=\prod_{i=1}^{n} p\left(x_{i}\right)$. In [5] the authors kept a vector for the mean of each variable, while a single overall standard deviation is stored. Some extensions of this work include the use of standard deviations for each variable [6], or the use of intervals [7].

Moreover, in [8], [9] is proposed to perform statistical test for each variable at each generation, with the aim to find the density function that best fits each variable. After that, the parameters are estimated.

2) Bivariate Dependences: Relations are represented in these approaches, but only for pairs of variables. A continuous variable version of [10] is proposed in [8], [9], with two-variable Gaussian functions as model.

In [11], [12], the authors propose and approach with Gaussian copulas with a single parameter, obtained by maximum likelihood, and then the sampling of new individuals is performed by the Monte Carlo method. Clayton and Ali-Mikhail-Haq Archimedean copulas and conditional sampling are implemented in [12], [13]. Empirical marginal functions with fixed parameter copulas are proposed in [14] (with Gumbel copulas) and [15] (with Clayton copulas). In [16] the authors propose a dependency tree as graphical model (represented as a string) with bivariate copulas selected and estimated by maximum likelihood.
3) Multivariate Dependences: Here, relations among multiple variables are represented. For example, the algorithms [8] use Gaussian networks which parameters are obtained by maximum likelihood.

Another approach is that in [17], which can be adapted for continuous or combinatorial problems. The distribution is truncated with the value of the worst individual in previous generation, and just a fraction of the population is replaced. Mixed integer problems are also tackled in [18], where each probability distribution is modeled by a dependency tree, and each leaf represents a normal distribution.

In [12] the authors adopted empirical copulas, together with a method [19] for first building a copula, and then use it for sampling new individuals. Archimedean copulas are used in [20], with parameters fixed a priori, and a conditional sampling method. In [21] the authors propose the use of a regular vine as a graphical model, Gaussian copulas obtained by maximum likelihood and beta marginal distributions. A more recent approach is [22], with empirical marginals and Archimedean copulas (Gumbel or Clayton).
4) Mixed Distributions: Models with mixed density functions are also possible, aiming for more flexibility in the representation. For example, in [23] each variable is represented as a sum of several Gaussian distribution components. Another proposal [24] is to group solutions and then construct a Gaussian network for each group, also using mixed Gaussian distributions.
5) Adaptive Algorithms: Another promising option is to implement special mechanisms in order to select the different parts of the algorithm, from the type of graphical model or the type of copulas used, to even switch between different algorithms.

The algorithm proposed in [25] selects at each iteration the type of graphical model and the inference method associated with it, in order to approximate the distribution on variables and their dependences.

Selecting from different algorithms at running time fall in the area of hyper-heuristics. So, a hyper-heuristic is proposed in [26], where the selection is from a collection

Table I
Three types of copulas adopted
of different algorithms without dependences, with bivariate dependences, and with multivariate dependences.

## III. ReLeVant Concepts

In this section, some concepts related with the proposed work are presented.

## A. Archimedean Copulas

Definition 1. An Archimedean copula of $n$ variables is the function $C\left(u_{1}, u_{2}, \ldots, u_{n}\right)=\varphi^{-1}\left(\varphi\left(u_{1}\right)+\varphi\left(u_{2}\right)+\right.$ $\left.\ldots+\varphi\left(u_{n}\right)\right)$, where the so-called strict generator $\varphi(\cdot)$ is a function $\varphi: I \rightarrow R_{>0}$, continuous, decreasing and convex, such that $\varphi(1)=0$ and $\varphi(0)=+\infty$

Archimedean copulas are symmetric: $C(v, z)=C(z, v)$, as well as associative: $C(C(v, z), u)=C(v, C(z, u))$.

Moreover, they are related with Kendall's tau coefficient, as stated in [27]:

$$
\tau=4 \int_{I} \frac{\varphi(v)}{\varphi^{\prime}(v)} d v+1
$$

Our proposal is to make use of such property, and use several, adaptively selected, copulas. The most representative copulas were selected: Clayton, Frank and Gumbel. The functions and other properties of such copulas are showed in Table I. The density function of the copulas has the form: $c=\varphi^{-(n)}\left(C\left(u_{1}, u_{2}, \ldots, u_{n}\right)\right) \prod_{i=1}^{n} \varphi^{\prime}\left(u_{i}\right)$. The expressions for the $i$-th derivative of the inverse of the generator are taken from [28].

## B. Copula Bayesian Network

As probabilistic graphic model, we adopted a copula Bayesian network. A probabilistic graphic model consists of a directed acyclic graph, which represents the conditional dependences of the variables; and a set of local generalized probability distributions, given the obtained relations between variables.

Definition 2. A copula Bayesian network $C=\left(G, \Theta_{C}, \Theta_{f}\right)$ represents the joint density $f_{X}(x) . G$ is a directed acyclic graph, $\Theta_{C}$ is a set of local density functions $c_{i}\left(F\left(x_{i}\right),\left\{F\left(\mathbf{p a}_{i k}\right)\right\}\right)$ associated with the nodes of $G$ having at least one parent. $\Theta_{f}$ is the set of parameters representing the marginal densities $f\left(x_{i}\right)$. This way, $f_{X}(x)$ is parameterized as $f_{X}(x)=\prod_{i} R_{c_{i}}\left(F\left(x_{i}\right),\left\{F\left(\mathbf{p a}_{i k}\right)\right\}\right) f\left(x_{i}\right)$.

Further details can be found in [29].

## IV. PROPOSED APPROACH

As mentioned above, we propose the use of a copula Bayesian network as probabilistic model, which allow us the adoption of multiple types of copulas. The method score+search is used for learning the structure. Such method is based on a greedy search and the BIC metric for estimating the fitness of the structure [30].

As proposed in [24], the construction of the structure starts with an empty graph, and then test edge by edge, selecting that which contributes with more information according to the metric adopted. Once the edge has been added, it is necessary to remove such edges that form cycles.

Some modifications are proposed here in order to speed up the construction of the structure.

- First, the use of the Kendall's tau coefficients to identify correlation between variables and, consequently, creating edges for new copulas. So, we need to keep a table with the different values of tau for any pair of variables. Since the structure only allows positive relations, only positive values of tau are considered.
Addition of variables to an existing copula is also possible with this method, computing the mean of the tau values for each pair composed of a variable already present in such copula and a new candidate variable. Again, valid mean values are only positive.
The BIC metric is used as in the original proposal, for measuring the increment in fitness of the structure.
- The parameter of the copula is commonly estimated by maximum likelihood. But an alternative, less expensive approach can be applied. Certainly, the tau coefficients cannot be used for obtaining the parameter of multivariate copulas in the exact expressions, but, thanks to the associative property of Archimedean copulas, it is possible to average the tau values of all the pairs of variables present in the copula. This is considerably less expensive in CPU time.
- Finally, the adaptive selection of one of the three types of copulas adopted. This can reflect with higher precision, the relations between the affected variables. The type of copula is selected by their likelihood at the time of creation, an then remains fixed by the rest of the process.
For estimating the parameters we adopted the approach proposed in [31], with some minor modifications. The estimation consists on two steps:

1) The estimation of the parameters of the univariate marginal distributions. Such distributions are only beta distributions, and the parameters are the mean $\mu$ and the variance $\sigma^{2}$.
For a softer behavior throughout the process, the estimation is increasingly weighted by the values obtained from previous generations. A method for doing that was proposed in [6]:

$$
\begin{gathered}
\mu_{t+1}=(1-\alpha) \mu_{t}+\alpha \bar{x} \\
\sigma_{t+1}^{2}=(1-\alpha) \sigma_{t}^{2}+\alpha\left(\frac{1}{N-1} \sum_{i=1}^{N}\left(x_{i}-\bar{x}\right)\right)
\end{gathered}
$$

2) The estimation of the parameters of the copulas. This process is commonly performed by maximum likelihood, but we propose the use of the Kendall's tau, as described above.
The overall process of learning of the structure is depicted in Figure 1.

The sampling process is a standard conditional approach, for the multivariate case.

Given that each variable can belong to several copulas, is needed a heuristic in order to decide which copula will be used for sampling. The rules proposed here are:

- If the variable is a child in a copula, such copula is used for sampling.
- If the variable is not a child in any copula, but belongs to some copulas, the copula with already more sampled variables is used.
- If the variable does not belong to any copula, sampling is made at random.


## V. Preliminary Results

## A. Experimental Setup

Five of the problems found in [32] were selected. Such functions present diverse characteristics, and are frequently used in the specialized literature. Such problems are and their characteristics are:

1) Shifted elliptic problem: unimodal, separable.
2) Shifted Rastrigin problem: multimodal, separable.
3) Shifted Ackley problem: multimodal, separable.
4) Shifted 1.2 Schwefel problem: unimodal, nonseparable.

![img-0.jpeg](img-0.jpeg)

Figure 1. Construction of graph structure
5) Shifted Rosenbrock problem: multimodal, nonseparable.
The minimum for all problems is $f(X)=0$. The reported results were obtained from 31 independent runs, with the following parameters:

- Population size: 100.
- Maximum number of generations: 1,000.
- Maximum number of function evaluations: 100,000.
- Maximum number of parents in a copula: 5.
- Selection: 30 individuals.
- Problem size: 10 variables for all problems.
- $\alpha$ for estimation of univariate distributions: from 0.01 to 0.1 , with increments of 0.01 .


## B. Results

The results are shown in Table II. Experiments with higher dimensionalities are currently under way.

The obtained results show that the approach based on multivariate Archimedean copulas is promising, even competitive with other evolutionary algorithms not based on statistical modeling.

## VI. Conclusions and Future Work

This work proposes the use of several type of copulas, adaptively selected during the process. This can increase the precision of reflecting the nature of relations between variables in the problem at hand.

Additionally, the use of Archimedean copulas can provide means for decreasing the computational cost associated with the estimation of the parameters of multivariate copulas.

The use of an incremental rule for estimating the parameters of marginal distributions is very important in this approach, because it promotes exploration and maintains diversity, otherwise quickly lost during the process.

Some preliminary results are presented in this paper, with only 10 variables. Experiments with higher dimensionalities (up to 100) are currently under way. They require a considerable amount of time and space in the respective report, so they are planned for a future publication.

As a future work related with the estimation of marginals, is the self-adaptation of the $\alpha$ value, eliminating the necessity of fine tuning or dynamic rules.

Another future work is related with negative correlations, currently discarded because of the probabilistic model. However, the contribute important information which can be incorporated to the model.
