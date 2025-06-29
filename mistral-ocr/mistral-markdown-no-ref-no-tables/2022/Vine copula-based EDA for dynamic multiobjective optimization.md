# Vine copula-based EDA for dynamic multiobjective optimization 

Abdelhakim Cheriet ${ }^{1}$ (1)

Received: 7 April 2020 / Revised: 22 October 2020 / Accepted: 30 October 2020
(c) Springer-Verlag GmbH Germany, part of Springer Nature 2020


#### Abstract

Dynamic Multiobjective Problems cover a set of real-world problems that have many conflicting objectives. These problems are challenging and well known by the dynamic nature of their objective functions, constraint functions, and problem parameters which often change over time. In fact, dealing with these problems has not been investigated in detail using the Estimation of Distribution Algorithms (EDAs). Thus, we propose in this paper an EDA-based on Vine Copulas algorithm to deal with Dynamic Multiobjective Problems (DMOPs). Vines Copulas are graphical models that represent multivariate dependence using bivariate copulas. The proposed Copula-based Estimation of Distribution Algorithm, labeled Dynamic Vine-Copula Estimation of Distribution Algorithm (DynVC-EDA), is used to implement two search strategies. The first strategy is an algorithm that uses the model as a memory to save the status of the best solutions obtained during the current generation. The second strategy is a prediction-based algorithm that uses the history of the best solutions to predict a new population when a change occurs. The proposed algorithms are tested using a set of benchmarks provided with CEC2015 and the Gee-Tan-Abbass. Statistical findings show that the DynVC-EDA is competitive to the state-of-the-art methods in dealing with dynamic multiobjective optimization.


Keywords Evolutionary algorithm $\cdot$ Copula $\cdot$ Vine-copula $\cdot$ EDA $\cdot$ Dynamic multiobjective optimization

## 1 Introduction

In various fields of science and technology, optimization problems have two or more objectives that should be optimized simultaneously. These problems are called Multiobjective Optimization Problems (MOPs) [14], and their solution involves the design of algorithms that are different from those adopted for solving single-objective optimization problems.

In the absence of reference information, there is no unique or straightforward way to determine if a given solution is better than others in multiobjective optimization. The notion of optimality most commonly adopted in such context is the one called Pareto optimality. Pareto optimality leads to trade-offs among the objectives in MOPs. Thus, the solution of MOPs is usually a set of acceptable trade-off optimal solutions called Pareto optimal set. Compared to traditional

[^0]algorithms, evolutionary algorithms (EAs) have shown good results in solving problems in many research areas, including engineering, biology, robotics [51], classification and clustering [2, 3], machine learning [5], information retrievals [4] and optimization. Namely, Non-dominated Sorting Genetic Algorithm (NSGA2) [18], Strength Pareto Evolutionary Algorithm (SPEA2) [68] and Multiobjective Evolutionary Algorithm based on Decomposition (MOEA/D) [63] has been proposed and then widely used for solving MOPs in the last decade.

After demonstrating their usefulness in finding multiple Pareto-optimal solutions for static multiobjective optimization problems, there is a growing need for solving Dynamic Multiobjective Optimization Problems (DMOPs) using Evolutionary Algorithms [21]. A dynamic optimization problem involves objective functions, constraint functions, and problem parameters, that change with time [17]. This class of problems is more challenging than static MOPs since they combine the known difficulties of obtaining a diverse set of solutions with the dynamic changes that occur on the objective functions. That is, optimal solutions will vary, following the change of the objective function that varies over time.


[^0]:    1) Abdelhakim Cheriet

    Abdelhakim.cheriet@univ-ouargla.dz
    1 Department of Computer Science and Information Technologies, Kasdi Merbah University of Ouargla, Ouargla, Algeria

Recently, Estimation of Distribution Algorithms (EDAs) [37], a subclass of evolutionary algorithms, has seen an increasing number of applications to different kinds of optimization problems. EDAs can be seen as an entirely new paradigm of evolutionary computation, which is a combination of statistical learning theory and stochastic optimization algorithm, without the use of conventional evolutionary operators such as crossover and mutation. EDA works by estimating the probabilistic distribution of the selected population and describes its evolutionary trend directly from a macroscopic point of view. It has been shown that EDA exhibits some special characteristics of the concise concept and good global searching ability [37].

Hence, EDAs have been successfully extended to solve multiobjective optimization problems [39, 43, 47]. The performance of an EDA highly depends on how well it estimates and samples the probability distribution. A wide variety of EDAs using probabilistic graphical modeling techniques to estimate and sample the probability distribution have been proposed in the literature (e.g. [20, 38, 48]) and still the subject of active research. However, EDAs using probabilistic graphical modeling techniques may spend too much time on learning the probability distribution of the candidate solutions.

The essential component and distinguishing characteristic of an EDA is its probabilistic model. These probabilistic models depend on the representation of the problem and the type of interactions to capture. One of the practical probabilistic models that have been used in EDA is copula [44], especially in case of problems with continuous representations.

Copula was introduced by Sklar [50] as a tool for constructing multi-variate distributions and it was successfully used in many research [13, 41]. According to copula theory, a joint probability distribution can be decomposed into $n$ marginal probability distributions and a copula function. A joint probability distribution can be constructed utilizing a copula function and the marginal probability distributions of every variable.

Multi-variate Archimedean copula [59] is a variant of the Archimedean copulas family, which has attracted particular interest due to their ability to model dependence in high dimensions with only one parameter. They have also been used as probabilistic models for EDAs [59]. However, learning high-dimensional copulas requires more complex estimation procedures that can also be more time-consuming compared to bi-variate models. To deal with this issue, the authors in [11, 12] have proposed to use a Vine copula model that is characterized by the positive effect of speeding up multiobjective optimization computation time.

One of the bi-variate models based on copulas that provide high flexibility for modeling multi-variate distributions is the vine copula. In simple terms, a vine copula is a set of nested trees where each edge in a tree represents
a dependence relationship that is encoded with a copula function.

In this paper, we introduce the Dynamic Vine Copulabased Estimation of Distribution Algorithm (labeled DynVC-EDA), which learns a vine model with Archimedean copulas to solve dynamic multiobjective problems. The vine model is used to describe the distribution and dependencies between the variables of the obtained Pareto solutions.

In this proposition, we introduce two strategies labeled DynVC-EDA-M and DynVC-EDA-P. The first strategy (DynVC-EDA-M) is represented by an algorithm that uses the vine model as a memory to save the status of the best solutions obtained during the current generation. The second strategy (DynVC-EDA-P) is a prediction-based algorithm that uses the history of the best obtained solutions to predict a new population when a change occurs (i.e. an algorithm that predicts upcoming changes on the problem).

Convergence and diversity metrics are used to evaluate the performance of the proposed algorithms. We tested DynVC-EDA on a set of dynamic benchmark traditionally used by the community, namely the FDA benchmarks [21], CEC2015 benchmarks [30], and the new Gee-Tan-Abbass (GTA) benchmarks [24]. We used DynVC-EDA along with the well known multiobjective evolutionary algorithm based on decomposition (MOEA/D) [62] as candidates examples to select the best solution in every iteration. MOEA/D decomposes a multiobjective optimization problem into several single-objective optimization sub-problems and then optimize these sub-problems. MOEA/D uses many decomposition methods; in this paper, we choose to use Tchebycheff as a decomposition method [62].

The rest of the paper is organized as follows: Sect. 2 describes the background of the problem addressed in this proposal. We also provide some concepts and definitions related to the dynamic multiobjective problem. Then, we introduce some relevant concepts from the copula theory, which plays a primary role in this work. Section 3 explains the proposed dynamic multiobjective optimization methods. Both the memory-based algorithm, and the prediction-based algorithm are presented in details. Section 4 describes the design of experiments, introduces the benchmarks and the metrics used for evaluating this work. Section 5 discusses the results achieved by the proposed algorithms in comparison to other methods. Finally, we conclude the paper in Sect. 6.

## 2 Background

### 2.1 Dynamic multiobjective optimization

Most real-world problems are multiobjective and often they are dynamic and in continuous change over time. These changes affect the objective function, the problem instances,

and/or the objective constraints. In the literature, researchers usually define optimization problems that change over time as dynamic problems or time-dependent problems [42].

### 2.1.1 Problem definition

Definition 1 A dynamic multiobjective problem can be represented as the following multiobjective optimization problem [21]. Let $t$ be the time variable, $\mathbf{V}$ and $\mathbf{W}$ be n-dimensional and m-dimensional continuous or discrete vector spaces, $\mathbf{g}$ and $\mathbf{h}$ be two functions defining inequalities and constraints, and $\mathbf{f}$ be a function from $\mathbf{V} \times t$ to $\mathbf{W}$. A dynamic multiobjective minimization problem with $m$ objectives $f_{1}, \ldots, f_{m}$ is defined in Eq. (1):
$\min _{v \in V} f=\left(f_{1}(v, t), \ldots, f_{m}(v, t)\right)$
s.t $g(v, t) \leq 0$ and $h(v, t)=0$

Definition 2 Considering a minimization problem, a decision vector $\mathbf{u}$ dominates $\mathbf{v}$ at time $t(\mathbf{u}<\mathbf{v})$ iff $f_{i}(\mathbf{u}, t)<f_{i}(\mathbf{v}, t), \forall i \in\{1, \ldots, m\}$.

Definition 3 The solution of a multiobjective problem is a set of solutions which are not dominated by any other solution at a specific time $t$. We call this set the Pareto Optimal Solutions POS at time $t$. The image of this set in the objective space forms the Pareto Optimal Front POF at time $t$.

### 2.1.2 Types of dynamic problems

Concerning the way POS and POF change, there are four possible ways a problem can demonstrate a time-varying change according to [21]:

1. The POS (optimal decision variables) changes, whereas the POF (optimal objective values) does not change.
2. Both POS and POF change.
3. POS does not change, whereas POF changes.
4. Both POS and POF do not change, although the problem can change.

### 2.2 Copula theory

Sklar [50] introduced the functions of the copula as a powerful tool to model the dependency between variables. Copula-based methods do not require all hypotheses about the probability distribution of the data. The method exploits the linear and non-linear relations between two or more variables using a copula function on an empirical bi-variate or multi-variate distribution. Finally, new data that are compatible with the previous derived dependency structure can be simulated with a cumulative distribution function given by this copula.

### 2.2.1 Sklar's theorem

Sklar theorem [50] indicates that a copula $C$ attaches a given multi-variate distribution function to their univariate marginals. In a bi-variate distribution, and for the conjoint distribution $F_{X Y}(x, y)$ with the univariate marginal distribution functions $F_{X}(x)$ and $F_{Y}(y)$, there exists a copula $C$.
$F_{X Y}(x, y)=C\left(F_{X}(x), F_{Y}(y)\right)=C(u, v)$
$C:[0,1]^{2} \rightarrow[0,1]$
If $C$ is a copula and $F_{X}$ and $F_{Y}$ are distribution functions, $F_{X Y}$ can be defined as a conjoint distribution with $F_{X}$ and $F_{Y}$. The probability density function (PDF) of the bi-variate distribution $f_{X, Y}(x, y)$ is represented in Eq. (4):
$f_{X Y}(x, y)=C\left(F_{X}(x), F_{Y}(y)\right) \cdot f_{X}(x) \cdot f_{Y}(y)$
where $f_{X}(x)$ and $f_{Y}(y)$ are the univariate marginals of $X$ and $Y$. The copula is unique when the marginals are continuous.

### 2.2.2 Copula characteristics

Some copula characteristics are given by Genest and Rivest [26] and resumed as follows. In the bi-variate case, a copula is represented as a function $C$ from $[0,1]^{2}$ to $[0,1]$ with $\forall u, v \in[0,1]$ :
$C(u, 0)=C(0, v)=0$
$C(u, 1)=u$ and $C(1, v)=v$
A copula is an increasing function $\forall u_{1}, u_{2}, v_{1}, v_{2} \in[0,1]$ with $u_{1} \leq u_{2}$ and $v_{1} \leq v_{2}$ gives
$C\left(u_{2}, v_{2}\right)-C\left(u_{2}, v_{1}\right)-C\left(u_{1}, v_{2}\right)-C\left(u_{1}, v_{1}\right) \geq 0$
A copula is a continuous function:
$\left|C\left(u_{2}, v_{2}\right)-C\left(u_{1}, v_{1}\right)\right| \leq\left|u_{2}-u_{1}\right|-\left|v_{2}-v_{1}\right|$
An important class of copulas are the Archimedean copulas [26]. This class is characterized by the ease with which they can be constructed and the nice properties they possess. Archimedean copulas are defined by:
$C(u, v)=\psi^{-1}(\psi(u)+\psi(v))$
where $\psi$ is the generator of the copula.
There are three Archimedean copulas in common use: the Clayton, Frank, and Gumbel (Fig. 1).

The Clayton copula is an asymmetric Archimedean copula, exhibiting greater dependence in the negative tail than in the positive. This copula is given by:

Fig. 1 Archimedean copulas samples
![img-0.jpeg](img-0.jpeg)
$C_{\theta}(u, v)=\max \left(\left[u^{-\theta}+v^{-\theta}-1\right]^{1 / \theta}, 0\right)$
And its generator is:
$\psi_{\theta}(t)=\frac{1}{\theta}\left(t^{-\theta}-1\right)$
where $\theta \in[-1, \infty) \backslash\{0\}$. The relationship between Kendall's $\tau$ and the Clayton copula parameter $\theta$ is given by $\hat{\theta}=\frac{2 \tau}{1-\tau}$

Frank copula is a symmetric Archimedean copula given by:
$C_{\theta}(u, v)=-\frac{1}{\theta} \log \left[1+\frac{\left(e^{-\theta \alpha}-1\right)\left(e^{-\theta v}-1\right)}{e^{-\theta}-1}\right]$
And its generator is:
$\psi_{\theta}(t)=-\log \left(\frac{\exp (-\theta t)-1}{\exp (-\theta)-1}\right)$
where $\theta \in(-\infty, \infty) \backslash\{0\}$, the relationship between Kendall's $\tau$ and the Frank copula parameter $\theta$ is given by $\tau=1+\frac{2}{\theta}\left(D_{1}(\theta)-1\right)$ where $D_{1}(\theta)=\frac{1}{\theta} \int_{0}^{\theta} \frac{t}{e^{t}-1} d t$ is a Debye function of order one [26].

The Gumbel copula is an asymmetric Archimedean copula, exhibiting greater dependence on the positive tail than on the negative one. This copula is given by:
$C_{\theta}(u, v)=\exp \left[-\left((-\log (u))^{\theta}+(-\log (v))^{\theta}\right)^{1 / \theta}\right]$
And its generator is:
$\psi_{\theta}(t)=(-\log (t))^{\theta}$
where $\theta \in[1, \infty)$. The relationship between Kendall's $\tau$ and the Gumbel copula parameter $\theta$ is given by $\hat{\theta}=\frac{1}{1-\tau}$

### 2.2.3 Copula simulation

Copulas have a direct application in the simulation of the dependent variables. We present the general procedure to simulate bi-variate dependents variables. First, we start by a short description of what is a pseudo-inverse of a distribution function.
![img-1.jpeg](img-1.jpeg)

Definition 4 Let $F$ be a univariate distribution function. A pseudo-inverse of $F$ is function [19] $F^{[-1]}: \mathbb{I} \rightarrow \mathbb{R}$ such that for $t \in \mathbb{I}$ :
$F^{[-1]}(t)=\inf \{x: F(x) \geq t\}=\sup \{x: F(x) \leq t\}$
A general algorithm to generate new samples $(x, y)$ of a pair of random variables $(X, Y)$ with the marginals $F_{X}, F_{Y}$, joint distribution $F_{X Y}$, and a copula $C$ is defined as follows. Initially, we generate a pair of observations $(u, v)$ of random variables $(U, V)$ and compute the copula $C$. Then, using the inverse transformation method, we transform $(u, v)$ to $(x, y)$ using :
$x=F_{X}^{[-1]}(u)$
$y=F_{Y}^{[-1]}(v)$
To generate the pair $(u, v)$ we perform the following steps:

- Sample from independent random variables $u, t$ uniformly in $\mathbb{I}$.
- Define $v=C^{[-1]}(t)$.

The generate pair is then $(u, v)$.

### 2.2.4 Vine Copulas

Though copulas can represent a wide variety of dependence relationships between pairs of variables, their extension to represent multi-variate distributions is cumbersome. Multi-variate copulas are not sufficiently flexible to represent dependence structures for which all pairs of variables share the same type of dependence. Pair copula constructions [1, 16] are an effective alternative to build multi-variate dependence models using bi-variate copulas. They can be represented using a particular type of graphical model called vine graphical model or simply vine [8, 53].

A vine on $n$ variables is a nested set of trees $T_{1}, \ldots, T_{n-1}$, where the edges of tree $j$ are the nodes of the $j+1$-th tree, with $j=1, \ldots, n-2$. Two special cases of vines are canonical vines (C-vines) and drawable vines (D-vines). In C-vines, for each tree $T_{j}$ there is a unique node connected to $n-j$ edges. In D-vines, for each tree $T_{j}$, there is no node that is connected to more than two edges.

The C-vine density is given by Eq. (18):
$f\left(x_{1}, \ldots, x_{n}\right)=\prod_{k=1}^{n} f\left(x_{k}\right) \prod_{j=1}^{n-1} \prod_{i=1}^{n-j} c_{j, j+i \mid i, \ldots, j-1}$,
and the D-vine density is defined by Eq. 19:
$f\left(x_{1}, \ldots, x_{n}\right)=\prod_{k=1}^{n} f\left(x_{k}\right) \prod_{j=1}^{n-1} \prod_{i=1}^{n-j} c_{i, i+j \mid i+1, \ldots, i+j-1}$,
where $j$ represents the trees and $i$ denotes the edges.
The arguments of the pair-copulas in (18) and (19) are conditional distributions of the form $F(x \mid \mathbf{v})$ determined by the subscripts of the copula. In [46] it is shown that:
$F(x \mid \mathbf{v})=\frac{\partial C_{x, v_{j} \mid \mathbf{v}_{-j}}\left(F\left(x \mid \mathbf{v}_{-\mathbf{j}}\right), F\left(v_{j} \mid \mathbf{v}_{-\mathbf{j}}\right)\right)}{\partial F\left(v_{j} \mid \mathbf{v}_{-\mathbf{j}}\right)}$
where $C_{x, v_{j} \mid \mathbf{v}_{-\mathbf{j}}}$ is a bi-variate copula distribution function, $\mathbf{v}$ is an n-dimensional vector, $v_{j}$ is one component of $\mathbf{v}$ and $\mathbf{v}_{-\mathbf{j}}$ denotes the $\mathbf{v}$-vector excluding the $j$ component.

When $x$ and $v$ are uniform the recursive evaluation of $F(x \mid \mathbf{v})$ can be expressed as:
$h(x, v, \theta)=F(x \mid v)=\frac{\partial C_{x v}(x, v, \theta)}{\partial_{v}}$
where $h$ is a function defined to facilitate the computation of $F(x \mid v)$ and $\theta$ denotes the set of parameters for the copula of the joint distribution of $x$ and $v$.

### 2.3 Related work

In this section, we present the state-of-the-art methods related to our topic. First, we overview the evolutionary based methods proposed for Dynamic Optimization Problems. Then, we present copula-based approaches for the Estimation of Distribution Algorithms.

### 2.3.1 Evolutionary algorithms for dynamic multiobjective optimization

There are two main approaches to deal with dynamic multiobjective problems. The first one approach regroups memory-based algorithms, and the second one regroups prediction-based algorithms.

The memory-based algorithms use memory to store information from past generations. The stored information will guide the search process in future generations or when a change occurs in the problem. The memory-based approach was successfully applied in many research papers. For instance, the Dynamic Competitive Cooperative CO-EA [27] used an external population as a memory. The memory is used with the addition population archive to store
information related to Pareto Front (PF). The Adaptive Population Management-Based Dynamic NSGA2 [7] is based on a technique that measures the severity of change. If the severity of change is small, the memory is used. Otherwise, a random restart is used instead of a memory. The algorithm uses this technique to guarantee a better convergence speed. The Multi-strategy Ensemble MOEA [60], similarly to [7], uses memory when a change occurs to obtain a new population by generating solutions randomly within the bounds of the search space and solutions generated by the Gaussian local search operator from the stored solution in that memory.

The second main class of techniques is the predictionbased algorithms. These algorithms aim to predict the new Pareto Front (i.e. the Pareto solutions) based on the information related to the prior history of changes. The prediction procedure is the main characteristic that differentiates a prediction-based algorithm from other algorithms. In the Population Prediction Strategy (PPS) proposed in [66], the authors divided the Pareto Solution (PS) into a center point and a manifold. When a change occurs, the algorithm predicts the next center from the history of all center points, and the next manifold is predicted from the previous manifolds. The manifold concept used in this paper is the same used in the RM-MEDA algorithm [65]. The authors of the Kalman Filter Assisted MOEA/D-DE Algorithm (MOEA/D-KF) [40] used a Kalman Filter-based prediction model, which is applied to the whole population to direct the search towards the new Pareto solution.

Authors in [64] proposed a Novel Prediction Strategies for Dynamic Multiobjective Optimization (PBDMO). The proposal combines the RM-MEDA algorithm with a new prediction-based reaction mechanism. PBDMO reacts effectively to any change occurs on the problem, by generating three sub-populations using different strategies.

Other methods have been proposed in the literature, notably the work entitled Reinforcement Learning-based Dynamic Multiobjective Evolutionary Algorithm (RLDMOEA) proposed in [69], which uses Reinforcement learning technique to learn better evolutionary behaviors from environment information, when identifying different severity level in the problem changes.

### 2.3.2 Copula-based estimation of distribution algorithms

Copulas models have been used in Estimation of Distribution Algorithms (EDAs) [28]. An early application of copulas in EDAs was presented in [54], where the multivariate Gaussian copula was proposed to model dependencies between the variables. In that proposal, different types of univariate marginal distributions could be used for each variable. The introduced EDA was compared to the UMDA (Uni-variate Marginal Distribution Algorithm) on a set of

(static) single-objective functions showing superior results. Other variants of multi-variate Gaussian copula EDAs have been proposed in $[23,34]$.

A variant of Copulas, called Archimedean copulas, is also used in modeling EDAs. Initially, bi-variate Archimedean copulas were used to optimize problems in two dimensions [59]. Exchangeable Archimedean copulas are an extension of bi-variate Archimedean copulas dedicated to multi-variate distributions. The exchangeable Archimedean copulas were applied to problems of larger dimensions [22, 57]. Archimedean copulas have also been used to build EDAs that factorize the distributions [15].

The closest methods to our proposition are EDAs that use vine-copulas to model the distribution of the best solutions [45, 46, 52]. Specifically, authors in [52] have proposed C-vines (Canonical vines) and D-vines (Drawable vines) as variants of vine-copulas to model distributions in EDAs. Since the cost of constructing full vines increases with the number of variables, the authors proposed to use a truncation strategy, i.e., trees are only built-up to a given level. The strategy was based on metrics that penalize the complexity of the models. The D-vine EDA, proposed by Salinas et al. [45], was tested with several benchmark functions demonstrating good results. In [55], four undirected graphical models based on copula theory were investigated in the context of EDAs to address a molecular docking problem. The authors reported that the vine-based algorithms produce more efficient results than the other tested variants. Recently, some new proposals investigate the application of copula models to multiobjective problems $[9,10]$.

Though, Copulas and vine-copulas have been proposed for EDAs, None of these efforts was dedicated to use this in Dynamic Multiobjective Problems. Thus, we target DMOPs using Vine-copulas with the introduction of algorithms that uses a memory-like mechanism and a prediction-based scheme on the previous history of evolution.

To summarize, while previous applications of copulas and vine-copulas have been proposed, none of these models have been applied to dynamic multiobjective problems. Also, they do not use a memory-like mechanism or the previous history of the evolution as the algorithms introduced in this paper do.

## 3 A Copula-based estimation of distribution algorithm for dynamic MOPs

EDAs use many ways to estimate the distribution of the best solutions. Different methods of estimations are comprehensively introduced in [29]. In this context, copula-based models are good candidates to optimize complex functions [10, 44, 58]. We propose to use the copula model created in the estimation step to generate new solutions near the PS (Pareto

Solutions) Thus, we introduce two approaches to find good solutions when a change occurs in the objective function. The first approach is a memory-based algorithm that uses the created copula model as a memory to store the best solutions found to the current generation before a change is detected. Then, use it as an initial population to guide the search. The second approach is a prediction-based algorithm that uses the history of the occurred changes to create a copula model in order to predict the next best solution.

### 3.1 The memory-based DynVC-EDA algorithm

The main idea of the memory-based algorithm is to use a memory of the best solutions obtained as an initial population instead of random initialization. This initialization is used when a change in the problem is detected. Mainly, memory-based algorithms reported in the literature [6] use an explicit memory. By explicit memory, we mean that the memory stores the best individuals found and then use them to create an initial population for the new configuration of the optimization problem. However, in our proposition, we use a vine-copula as a model of the best individuals found (i.e. The best solutions) as a memory. This concise representation reduces the size of the used memory. In addition, the model is expected to capture the common characteristic of the best solutions. Finally, generating new solutions using the model will add some random components that are useful for exploration. Therefore, this will help to diversify the initial population.

```
Algorithm 1: Dynamic Vine Copula-based EDA
    \(\mathrm{Q}_{0} \leftarrow\) Initialization \(\left(\mathrm{N}_{0}\right) ;\)
    \(\mathrm{NDSet}_{0} \leftarrow \operatorname{Sorting}\left(\mathrm{Q}_{0}\right) ;\)
    \(\mathrm{P}_{0} \leftarrow\) SelectFromNDS(N);
    \(1 \mathrm{t} \leftarrow 1 ;\)
    while Not termination criteria do
        if Change Detected then
            \(\mathrm{C}_{\mathrm{t}} \leftarrow\) EstimateModel \(\left(\mathrm{P}_{\mathrm{t}-1}\right) ;\)
            \(\mathrm{P}_{\text {imp }} \leftarrow\) GenerateSolutions \(\left(\mathrm{C}_{\mathrm{t}}\right) ;\)
        end
        \(\mathrm{NDSet}_{t} \leftarrow \operatorname{ApplyMOEAD}\left(\mathrm{P}_{\text {imp }} \cup \mathrm{NDSet}_{t-1}\right) ;\)
        \(\mathrm{P}_{\mathrm{t}} \leftarrow\) SelectFromNDS(N);
        \(\mathrm{NDSet}_{t} \leftarrow \mathrm{P}_{\mathrm{t}} ;\)
        \(\mathrm{t} \leftarrow \mathrm{t}+1 ;\)
    end
    Return NDSet \(_{t} \mathrm{C}\);
```

As a typical evolutionary algorithm, our proposed method has two main steps; the Selection and the Reproduction. In the first step, we use the MOEA/D to select the best solution, which will be used in the reproduction. In the second step, the copula model is applied to estimate then to generate new individuals. When a change occurs in the problem, the algorithm uses the obtained copula model to generate

individuals and use them as an initial population in the next generation. A pseudo-code of the estimation of distribution algorithm using a copula for a dynamic multiobjective problem is illustrated in Algorithm 1.

Initially, we create a population $\mathbf{P}_{\mathbf{0}}^{\mathbf{t}}=\left[\mathbf{x}_{1}^{\mathbf{t}}, \ldots, \mathbf{x}_{\mathbf{m}}^{\mathbf{t}}\right]^{T}$ where $\mathbf{x}_{i}^{\mathbf{t}}, i=1, \ldots, m$ represents the $i$ individual at time $t$. Every individual $\mathbf{x}_{i}^{\mathbf{t}}=\left(x_{i 1}^{t}, \ldots, x_{m}^{t}\right)$, where $x_{m 0 t} \leq x_{i j} \leq x_{m i t}$. In the selection step, we use the algorithms MOEA/D with Tchebycheff or Boundary Intersection (BI) [62]. This step returns a set of individuals that will be used in the reproduction. We call $\mathbf{P}_{\text {set }}^{\mathbf{t}}$ the set of the individuals at time $t$ resulting from the selection process operated on the precedent population. For the first generation, we use the initial population at time $t=0, \mathbf{P}^{\mathbf{0}}$. We have $\mathbf{P}$ defined as the following:

$$
\begin{aligned}
& \mathbf{P}_{\text {set }}^{\mathbf{t}}=\begin{array}{cccc}
x_{11} & x_{12} & \cdots & x_{1 n} \\
x_{21} & x_{22} & \cdots & x_{2 n} \\
\vdots & \vdots & \ddots & \vdots \\
x_{m 1} & x_{m 2} & \cdots & x_{m n}
\end{array}
\end{aligned}
$$

The reproduction step contains two main stages, the creation of the copula model and the generation of the individuals. First, we create the copula model by considering every individual $\mathbf{x}_{i}^{\mathbf{t}}$ as an observation $i$. Thus, we see the set $\mathbf{P}_{\text {set }}^{\mathbf{t}}$ as a set of observations of a vector of random variables. This set of observations is considered to follow a joint distribution function. The copula model creation step aims to estimate this joint distribution.

As we have previously explained, the inputs of the first step are the $n$-dimensional selected solutions, so we should use a multi-variate copula to model it. However, there is a different way to model a multi-variate copula [35]. In this work, we use a class of copula known as Vine-Copula, especially C-vine class, and the vine is truncated in the first level to gain more efficiency.

We start the creation of the model step by estimating the parameters for all bi-variate copulas, as it is described in [35]. There exist many methods to estimate copula parameters. Those methods include the fully parametric maximum likelihood method [61], the semi-parametric maximum pseudo-likelihood (MPL) method [25], the inference functions for margins method [35], the inversion of Kendall's tau estimator [61], and the inversion of Spearman's $\rho$ estimator [61]. We select to use in this paper the MPL method since it has outperformed other methods in several studies [36, 56].

After estimating the parameters of the vine-copula, we proceed to the sampling step. First, we use the modeled vinecopula to generate samples $U_{i}=\left(u_{1 i}, u_{2 i}, \ldots, u_{i n}\right)$, where $u_{i j} \in[0,1]$ as described in Sect. 2.2.4 by the same procedure as described in [35]. Then, we take the generated $U_{i}$ values and fit them to the solutions space $\Omega$.

To fit the generated values to the space solutions $\Omega$, we use a Kernel Density Estimation method (KDE) [49]. The kernel density estimation takes a set of observations and then estimates for every observation a probability value according to a specific kernel function [49]. To do this, we create the set $O$ as follows:

$$
\begin{aligned}
X_{\text {sel }} & =\left\{X^{1}, X^{2}, \cdots, X^{K}\right\} \\
X^{i} & =\left(x_{0}^{i}, x_{1}^{i}, \cdots, x_{n}^{i}\right), \text { where } x_{i}^{i} \in\left\{x_{i_{\max }}, x_{i_{\max }}\right\} \\
O & =\left\{o_{1}, o_{2}, \ldots, o_{n}\right\}, \text { where } o_{l}=\left\{x_{l 1}, x_{l 2}, \ldots, x_{l K}\right\}
\end{aligned}
$$

We denote as $o_{l}$ observations which contain the elements of the column $l$ of the solution in the set $X_{\text {sel }}$ (selected solutions). We estimate the density of the observation in $o_{l}$ using the Kernel Density Estimation (KDE) method. The result of the KDE for the $o_{l}$ observations is a set $\hat{V}_{l}=\left\{\hat{v}_{l 1}, \hat{v}_{l 2}, \ldots, \hat{v}_{l K}\right\}$ where $\hat{v}_{l i}$ represents the estimated density of the observation $o_{l i}$. After estimating the density of all the set $O$ using the same procedure that we used to estimate the $o_{l}$ observations, we start the step of interpolation.

The aim of the interpolation step is to create an inverse cumulative distribution function (icdf). The icdf function is defined from $[0,1]$ to $\mathbb{R}$. For the interpolation method, we take the set $\hat{V}_{l}$ as an input $X$ vector and $o_{l}$ as an output $Y$ vector. We get a function $f_{l}$ that gives $x_{l i}=f_{l}\left(\hat{v}_{l i}\right)$ where $\hat{v}_{l i} \in[0,1]$ and $x_{l i} \in\left[x_{i_{\max }}, x_{i_{\max }}\right]$.

After creating the interpolation function, labeled inv_cdf in Algorithm 2, we produce the new solutions using the generated sample $U$ and the inv_cdf function. For every column $l$, we apply a function $f_{l}$ for all elements in $U_{l}$, where $U_{l}$ are the elements of the $l$-th parameters for all the set $U$. The application of $f_{l}$ gives us a set $X_{l}^{\prime}$ where $X_{l}^{\prime}=\left\{x_{l 1}^{\prime}, x_{l 2}^{\prime}, \ldots, x_{l K^{\prime}}^{\prime}\right\}$ and $K^{\prime}$ is the number of the sampled solutions, $x_{l i}^{\prime}=f_{l}\left(U_{l i}\right)$. The result of this step is $n$ number of vector, and the new population is:
$P^{\prime}=\left\{X_{1}^{\prime}, X_{2}^{\prime}, \ldots, X_{n}^{\prime}\right\}$
$P^{\prime}=\left[\begin{array}{ccc}x_{11}^{\prime} & \ldots & x_{1 n}^{\prime} \\ \vdots & \ddots & \vdots \\ x_{K^{\prime} 1}^{\prime} & \ldots & x_{K^{\prime} n}^{\prime}\end{array}\right]$
a row $\left(x_{i 1}^{\prime}, x_{i 2}^{\prime}, \ldots, x_{i n}^{\prime}\right)$ from the matrix $P^{\prime}$ represents a newly generated solution.

We use the result of the density estimation to create an interpolation function between the values in $[0,1]$ and its probability density function (inverse CDF). Then, we apply this function for every generated value obtained by sampling the vine-copula. The result of this step is a new set of generated solutions in $\Omega$. Algorithm 2 summarizes the essential steps of this phase.

```
Algorithm 2: Generate Solutions
for in \(\{\{0,1, \cdots, n\}\) do
    \(y=\) kernel_density \(\left(X_{i}\right)\);
    inv_cdf \(=\) interpolate \(\left(y, X_{i}\right)\);
    \(s=\operatorname{inv} \cdot \operatorname{cdf}\left(u x_{i}\right)\);
    Result.append \((s)\);
end
return Result;
```


### 3.2 The prediction-based DynVC-EDA algorithm

In this section, we describe how the algorithm reacts when the problem is changed. Our algorithm uses a predictionbased scheme to reinitialize a population to guide the search process. The basic idea of the prediction-based algorithm is to utilize history information to predict an initial population that is close to the new PS. To achieve this goal, we store - at least two changes - the history of the best solutions found up to the current generation. And when a new change is detected, we use the saved set of solutions to create a copula model. This copula model is employed to predict the new Pareto solution and use it as an initial population.

Similarly to the memory-based algorithm, we use vinecopula due to its ability to model a high dimensional dependency. The type of copula used is a C-vine copula truncated at the first level. As it is described in Sect. 2.2.4, every node in the tree of the vine is a bi-variate copula. Every bi-variate copula $C_{t}$ models the dependency between the $i$ th parameter of all PS at time $t-1$ and the $i$ th parameter of all PS at time $t$.

Let $P S^{t-1}$ and $P S^{t}$ be the PS at the time $t-1$ and $t$ respectively. We mean by $t$ the time when a change occurs. The method consists of creating $n$ bi-variate copulas
$\operatorname{Model}\left(P S^{t-1}, P S^{t}\right)=\left(C_{0}, C_{1}, \ldots, C_{n}\right)$.

Table 1 The characteristics of the used benchmarks in the experiments

For example, $C_{0}$ model the dependence between $x_{j 0}^{t-1}$ and $x_{j 0}^{t}$ where $j \in\{0,1, \ldots, k\}, k$ is the number of the selected solutions in the PS. If we take the same notation in Eq. (23) that represents the population as a matrix, for every copula $C_{i}\left(X_{i}, Y_{i}\right), X_{i}$ that represents the column $i$ of the matrix representation of PS at time $t-1$ and $Y_{i}$ that represents the column $i$ of the matrix representation of PS at time $t$. The result of this modeling process is $n$ copulas, and the next step is the use of the set of copulas to generate the new solutions.

## 4 Experimentation results and analysis

In this section, we report the experimentation results conducted for evaluating the diversity and convergence of the proposed algorithms (DynVC-EDA-M and DynVC-EDA-P).

### 4.1 Benchmark function for dynamic optimization problem

Some of the significant challenges in the field of dynamic multiobjective optimization (DMOO) are the lack of a standard set of benchmark functions. Recently, some of these challenges have been addressed: a comprehensive overview of existing dynamic multiobjective optimization problems was presented in [31]. The characteristics of an ideal benchmark function suite were proposed with a set of DMOPs are suggested in [31]. Moreover, a comprehensive overview of performance measures currently used for DMOO is detailed in [32, 33]. In addition, authors in [24] developed a number of GTA problems targeting dynamic modality, trade-off connectivity, and PF degeneration.

To test the efficiency of the proposed algorithms, we conducted different experiments using a set of benchmarks


Table 2 The mean value of the MIGD for the 30 runs on a set of the CEC2015 benchmarks

Bold indicates the best value

Table 3 Mean of the MIGD metric for the dynamic CEC2015 benchmarks for $n_{t}=10, \tau_{t}=25$ and $\tau_{T}=500$ in 30 runs

Bold indicates the best value
that are usually used to evaluate new solving algorithms in the area of dynamic multiobjective optimization. The CEC2015 set of benchmarks introduced in [30] provides a set of benchmarks to compare the new algorithms with the classical ones. More specifically, we have selected the FDA4, FD5, DIMP2, DMOP2, DMOP3, HE2, HE7 and HE9 benchmarks from CEC2015. In addition to the previous benchmarks, we tested the proposal on a new set of benchmark named GTA benchmarks presented in [24]. For all experiments, we perform 30 runs with different combinations of parameters.

### 4.2 Performance measures

To assess the efficiency of the proposed algorithm, we apply an extensively used quality indicator: the inverted generational distance (IGD) for all used benchmark.

Let $P^{i x}$ be a set of uniformly distributed Pareto optimal points in the $P F^{i}$. Let $P^{k}$ be an approximation of $P F^{i}$. The IGD metric is defined as:
$I G D\left(P^{i x}, P^{k}\right)=\frac{\sum v \in P^{i x} d\left(v, P^{k}\right)}{\left|P^{i x}\right|}$

Fig. 2 IGD over iteration for the HE2 and HE7 benchmarks with different $n_{t}$ and $r$ values
![img-4.jpeg](img-4.jpeg)
(a) HE2, $n_{t}=10, \tau_{t}=25$
![img-3.jpeg](img-3.jpeg)
(b) HE2, $n_{t}=1, \tau_{t}=10$
![img-4.jpeg](img-4.jpeg)
(c) HE7, $n_{t}=10, \tau_{t}=25$
where
$d\left(v, P^{t}\right)=\min _{v \in P^{t+}}| | F(v)-F(u) \|$
is the distance between $v$ and $P^{t}$, and $\left|P^{t+}\right|$ is the cardinality of $P^{t+}$. The IGD metric can measure both diversity and convergence. To have a low IGD value, $P^{t}$ must be very close to $P F^{T}$ and cannot miss any part of the whole $P F^{T}$ [66].

We use the average of the IGD values "MIGD" (Mean IGD) in a number of steps over a run as described in [66]. The MIGD metric is given by equation:
$M I G D=\frac{1}{|T|} \sum_{t \in T} I G D\left(P^{t+}, P^{t}\right)$
where $T$ is a set of discrete-time points in a run, and $|T|$ is the cardinality of $T$. A lower value of the modified inverted generational distance (MIGD) metric would assist in evaluating the tracking ability, as the approximated Pareto front obtained from the algorithm with the changing POF is measured before every change.

### 4.3 Parameter settings and algorithms

The parameters of the used MOEAs in the experiment were referenced from their original papers. Some key parameters in these algorithms are set as follows:

Fig. 3 IGD over iteration for the HE9 and DMOP3 benchmarks with different $n_{t}$ and $\tau$ values
![img-5.jpeg](img-5.jpeg)
(a) $\mathrm{DMOP} 3, n_{t}=10, \tau_{t}=10$
![img-6.jpeg](img-6.jpeg)
(b) $\mathrm{HE} 9, n_{t}=10, \tau_{t}=10$
![img-7.jpeg](img-7.jpeg)
(c) $\mathrm{HE} 9, n_{t}=10, \tau_{t}=25$

- Population size The number of individuals we use in the experimentation is set to 100 for all algorithms.
- Maximum number of generations We denote this parameter as $\tau_{T}$, and we consider $\tau_{T} \in\{100,200,500,1000\}$
- Dynamic configuration $\left(n_{t}, \tau_{t}\right)$ For these parameters, we use the same configuration used in CEC2015 competition [30].

In addition to the proposed DynVC-EDA-M and DynVC-EDA-P algorithms, we use other algorithms, from competitive methods, to show the quality of the proposal and compare results with state-of-the-art algorithms. These competitive algorithms are the following:

- $R M-M E D A$ It is used in the PPS algorithm [66].
- RND In this algorithm, the population is randomly initialized every time a change occurs.
- DNSGA2 A dynamic version of the NSGA2 proposed by Deb et al. in [17].
- MOEA/D The variant used in [67]. It continues the execution without considering the changes.


## 5 Results and discussions

We show in this section the results obtained from the experiments. The first set of experiments is conducted using the CEC2015 benchmarks, and the second one uses the GTA(a,m) benchmarks. Table 1 presents the characteristics of all used benchmarks in many points of view, such as the

Fig. 4 IGD over iteration for the DMOP2 benchmark with different $n_{t}$ and $\tau$ values
![img-8.jpeg](img-8.jpeg)
(b) $n_{t}=10, \tau_{t}=5$
![img-9.jpeg](img-9.jpeg)
convexity, modality, POS changes, and the continuity of the Pareto Optimal Front (POF).

All the benchmarks are related to a time variable $t$. The time variable ( t ) used in all functions is calculated using the current generation number denoted as $(\tau)$ by
$t=\frac{1}{n_{t}}\left\lfloor\frac{\tau}{\tau_{t}}\right\rfloor$
where $n_{t}$ is the number of distinct steps in one $t$, also known as the severity of change. $\tau_{t}$ represents the number of generations for which the fitness landscape remains fixed, and it is called the change frequency.

### 5.1 Results on CEC2015 benchmarks

The CEC2015 set of benchmarks contains many types of problems. To investigate the behavior of the proposal on
those benchmarks, we perform 30 runs and compare the obtained results for all the algorithms described in Sect. 4.3.

For the configuration $n_{t}=10, \tau_{t}=5$ and $\tau_{T}=100$ DynVC-EDA-P outperforms all the other algorithms on DIMP2, DMOP2, FDA4 and FDA5 benchmarks and get a good result for the DMOP3 and HE2 benchmarks with approximately the same best value obtained by the DNSGA2 algorithm. We can notice for the other configurations in Table 2, that the value of the MIGD is decreased according to the value of $\tau_{t}$. As an example, for the FDA4 the MIGD values are $0.0027,0.0024$ and 0.0020 for $\tau_{t}$ equal to 5,10 and 25 and the same conclusion still correct for the rest of the benchmarks.

Table 3 presents the obtained results using $n_{t}=10$ and $\tau_{t}=10$. The result shows that the two variants of the

Fig. 5 IGD over iteration for the FDA4 benchmark with different $n_{t}$ and $\tau$ values
![img-10.jpeg](img-10.jpeg)
(c) $n_{t}=1, \tau_{t}=10$
proposed algorithm are competitive compared to state-of-the-art algorithms. The RM-MEDA algorithm outperforms the proposed algorithms by a small value. For example, in the HE2 benchmark the obtained MIGD is 0.0020 for both DynVC-EDA-P and DynVC-EDA-M, and the MIGD value for the RM-MEDA is 0.0019 which is approximately the same result. However, the two algorithms DynVC-EDA-P and DynVC-EDA-M outperform RM-MEDA in the remaining benchmarks.

In addition to the mean of MIGD results depicted in Tables 2 and 3, the variation of the IGD metric over
iterations are plotted from Figs. 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12 to 13 . Each figure represents the behavior of the compared algorithms against a specific benchmark when changes occur in the problem. It is important to highlight that as long as the IGD value is decreasing or stable after reaching a low value then the algorithm in question is performing good. In other terms, we can qualify that an algorithm achieves a good PS approximation for DMOPs, if its IGD value remains stable or increases slightly when a change occurs over a period of time. In contrast, the

Fig. 6 IGD over iteration for the FDA5 benchmark with different $n_{t}$ and $\tau$ values
![img-11.jpeg](img-11.jpeg)
(a) $n_{t}=10, \tau_{t}=10$
![img-12.jpeg](img-12.jpeg)
(b) $n_{t}=10, \tau_{t}=5$
![img-13.jpeg](img-13.jpeg)
(c) $n_{t}=1, \tau_{t}=10$
algorithm is not appropriate for DMOPS if its IGD value significantly increases when a change occurs.

Figure 2 presents the variation of the IGD metric over iterations (generation). Figure 2a and b depict results for the HE2 benchmark, and Fig. 2c shows the IGD values for the HE7 benchmark.

The variation of IGD value in Fig. 2a and b shows that DynVC-EDA-M and DynVC-EDA-P (labeled in the plot
as CEDA-M and CEDA-P respectively) can adapt rapidly when a change occurs for the different configuration in HE2 benchmark. For instance, DynVC-EDA-P reached the best IGD value, among other methods, after the 25 iterations (when the change occurred) for the HE2 benchmark as presented in Fig. 2b.

Table 4 The mean value of the MIGD for the 30 runs on the GTAm benchmarks

Bold indicates the best value

Table 5 The mean value of the MIGD for the 30 runs on the GTAa benchmarks

Bold indicates the best value

Similarly to Figs. 2 and 3 shows how close is the approximated Pareto front, obtained by each algorithm, to the Pareto Optimal Front (POF) in every iteration.

Figures 2c and 3b, c show that DynVC-EDA-M and DynVC-EDA-M get a good IGD value (the best PF approximation among others), and when a change occurs DynVC-EDA-M and DynVC-EDA-M maintain approximately the same IGD value, when the other algorithms show an

Fig. 7 IGD over iteration for the GTA1m benchmark with different $n_{t}$ and $\tau$ values
![img-14.jpeg](img-14.jpeg)
(c) $n_{t}=10, \tau_{t}=25$
important increase of the IGD metric. Moreover, in both Figs. 2a and 3a, all the compared algorithms did not obtain a good approximation when the change of the problem occurs. This is due to the nature of DMOP3 problem where the spread of the POF solutions changes over time as shown in Fig. 2a. Thus, all the algorithms cannot adapt effectively to changes due to the severity of change occurrence in the problem within this experiment.

Figure 4 presents the variation of IGD for the DMOP2 benchmark for different configurations. In Fig. 4a, we present the result obtained by using $\tau_{t}=10$. This figure shows
that DynVC-EDA-P (label as CEDA-P in the figure) outperforms all the compared algorithms. The DynVC-EDA-P algorithm adapts in an effective way to the change of the problem and gets better results starting from iteration 75. The proposed DynVC-EDA-M algorithm (label as CEDA-M in the figure) gets better results starting from iteration 100, where the algorithm has more information about solutions on its memory, which can be effectively employed to adapt to the problem dynamic.

The same observation and conclusion remain correct for results in Fig. 4b which represents the IGD value for

Fig. 8 IGD over iteration for the GTA1a benchmark with different $n_{t}$ and $\tau$ values
![img-15.jpeg](img-15.jpeg)

DMOP2 benchmark using $\tau_{t}=5$. As we can see, the proposed algorithms can adapt to problem change after 40 and 50 iterations for the memory-based and the prediction-based algorithm, respectively.

Figure 5 depicts the result of the experiment using the FDA4 benchmark. As it is shown in Fig. 5c, DynVC-EDAM reaches a steady IGD value over time compared to other methods regardless the number of changes occurred on the problem. The same conclusion can be driven from Fig. 6 for the FDA5 benchmark. Using $\tau_{t}=5,10$, and $n_{t}=10$ with FDA4 and FDA5 benchmarks and for both DynVC-EDAM and DynVC-EDA-P, the IGD value remains stable when change occurs on the problem. However, other algorithms like RND or MOEA/D did not reach good stability. In addition, both DynVC-EDA-M and DynVC-EDA-P outperforms DNSGA2 as depicted in the two figures.

### 5.2 Results on GTA benchmarks

The GTAa (addition) and GTAm (multiplication) benchmarks are a class of GTA benchmarks proposed in [24] (the source code of the GTA benchmark and the Pareto front generator can be obtained from the author website. ${ }^{1}$ ) The set of GTA benchmarks ensures many characteristics such as convexity, modality, and discontinuity of the Pareto Front, as shown in Table 1.

For all experiment instances on the GTA benchmarks, we performed 30 runs for each parameter configuration. We calculated the mean of the MIGD values, and we plotted the change of the IGD value over iterations for each benchmark. Table 4 presents these results. This table shows that the proposed DynVC-EDA-P achieves the lowest MIGD

[^0]
[^0]:    ${ }^{1}$ https://github.com/senbong87/dmo_benchmark.

Fig. 9 IGD over iteration for the GTA2m benchmark with different $n_{t}$ and $\tau$ values
![img-16.jpeg](img-16.jpeg)
(a) $n_{t}=10, \tau_{t}=10$
![img-17.jpeg](img-17.jpeg)
(b) $n_{t}=10, \tau_{t}=5$
![img-18.jpeg](img-18.jpeg)
(c) $n_{t}=10, \tau_{t}=25$
value against the other algorithms for the GTA1m, GTA2m, GTA3m, GTA4m, GTA5m, and GTA6m benchmarks.

Moreover, for the GTAa addition results resumed in Table 5, the DynVC-EDA-P algorithm outperforms the other algorithms by achieving the lowest MIGD for the GTA1a, GTA2a and GTA5a benchmarks using the settings $n_{t}=10$, $\tau_{t}=5,10$. Though the RM-MEDA algorithm obtains good MIGD for GTA3a, GTA4a and GTA6a benchmarks when the problem is mixed modality (uni and multi-modal), the

DynVC-EDA-P algorithm obtains good results when the problem is convex and multi-modal or uni-modal.

In addition to the results presented in Table 5, we also plotted the variation of the IGD over iterations for each GTA benchmark. Plotting the IGD over iteration aims to investigate how the algorithms behave when a change occurs during the process of optimization.

Figure 8 shows the obtained results for the GTA1a (addition) benchmark. Figure 8 b presents the results when $\tau_{t}=5$ and it shows that the proposed DynVC-EDA-P (label as

Fig. 10 IGD over iteration for the GTA2a benchmark with different $n_{t}$ and $r$ values
![img-19.jpeg](img-19.jpeg)
(c) $n_{t}=10, \tau_{t}=25$

CEDA-P in the plot) can adapt effectively to the problem change and thus gets a better IGD value against the other algorithms starting from the 40 -th iteration. For $\tau_{t}=25$, Fig. 8c shows that both DynVC-EDA-P and DynVC-EDAM algorithms perform better than competitive algorithms.

Results related to benchmarks GTA2m and GTA2a are presented in Figs. 9 and 10, respectively. For both Figs. 9b and 10b DynVC-EDA-P outperforms the compared algorithms using $\tau_{t}=5$. As shown in Figs. 9c and 10c, with a larger frequency of change $\tau_{t}=25$, the DynVC-EDA-P algorithm performs better than DynVC-EDA-M in the first iterations but after a number of iterations (for example

300 iterations depicted in Fig. 10c), DynVC-EDA-M gets approximately the same result as DynVC-EDA-P because the used memory in the DynVC-EDA-M has more diverse results.

Figures 11 and 12 present the results for the benchmark GTA5 both addition (GTA5a) and multiplication (GTA5m) variants. These results show that the DynVC-EDA-P and DynVC-EDA-M algorithms achieve better results compared to the state-of-the-art algorithms, and they can adapt in an efficient way to the problem changes compared to the other algorithms.

Fig. 11 IGD over iteration for the GTA5a benchmark with different $n_{t}$ and $r$ values
![img-20.jpeg](img-20.jpeg)
(c) $n_{t}=10, \tau_{t}=25$

Figures 13 and 14 present the results for the GTA6 benchmark. In Figs. 13c and 14b we show the results using $n_{t}=1$ and $\tau_{t}=5$, respectively. The results obtained for both benchmarks show that the proposed DynVC-EDA-P maintains a good result each time the problem change. Contrary to the compared algorithms, where they start with a good approximation of the PS, but starting from iteration 50, the compared algorithms cannot maintain a good stability of the IGD metric.

Figures 7 and 8 show the same behavior, for $n_{t}=1$ we see many variations of the IGD over iterations for all compared algorithms. However, the DynVC-EDA-M algorithm
starts with the same results as the other algorithms, then during the time it gets better, as shown in Figs. 7a and 8a. The use of memory can explain this behavior. Every time our algorithm saves more solutions, this will help the vinecopula created from the memory to produce more diverse solutions, so the approximated PF will be more close to the Pareto Optimal Front. Figures 7b, c and 8b, c show the results for the rest of the experiments for GTA1a and GTA1m, the proposal as shown, get more stability of the IGD metric compared to the state-of-art algorithms.

In the case of the GTA6a with $n_{t}=1$, we can see that our algorithm has not a good stability, in terms of the IGD value,

Fig. 12 IGD over iteration for the GTA5m benchmark with different $n_{t}$ and $\tau$ values
![img-21.jpeg](img-21.jpeg)
(c) $n_{t}=10, \tau_{t}=25$
the same as other algorithms. We can explain this behavior by the fact that the severity of the change is significant. Another argument can be that the GTA6m problem has a mixed modality where our algorithm cannot perform well as already explained from the results in Table 4.

## 6 Conclusions

In this work, we have proposed an estimation of distribution algorithm to deal with the multiobjective problem that changes over time. There exist many methods to find a good
approximation of the optimal solutions of the dynamic multiobjective problems. Some methods use memory to store the best solutions and re-use them when a change occurs in the problem, and others try to predict the up-coming optimal solutions according to the change history. Our proposal uses the power of the EDA to deal with the problem changes in two different ways the memory-based or the predictionbased one.

For the two methods, we use the well-known copula to estimate the distribution of the best solutions found so far and to get more advantages of the multi-variate copula. We model them using the vine-copula method. Indeed,

Fig. 13 IGD over iteration for the GTA6a benchmark with different $n_{t}$ and $r$ values
![img-22.jpeg](img-22.jpeg)
(c) $n_{t}=10, \tau_{t}=25$
vine-copula proved a good efficiency when dealing with a high dimension of the modeled solution compared with other methods. After estimating the best solutions using vine-copula, and when a change occurs, we produce new solutions using the created model.

To evaluate the idea behind this work, we have tested it using many benchmarks. We tested it on the CEC2015 benchmarks, FDA problems, and the GTA benchmarks.

Then, we calculate the quality of the obtained results in various parameter configurations using the MIGD metric known in dynamic multiobjective optimization. The obtained results show good qualities compared with state-of-art algorithms. Future work can be the use of the vine-copula model in the class of real-world dynamic multiobjective optimization problems and combinatorial problems.

Fig. 14 IGD over iteration for the GTA6m benchmark with different $n_{t}$ and $\tau$ values
![img-23.jpeg](img-23.jpeg)
(a) $n_{t}=1, \tau_{t}=10$
![img-24.jpeg](img-24.jpeg)
(b) $n_{t}=10, \tau_{t}=5$
![img-25.jpeg](img-25.jpeg)
(c) $n_{t}=1, \tau_{t}=50$

Acknowledgements I want to express my very great appreciation to Professor Roberto Santana for his valuable and constructive suggestions during the planning and development of this research paper. His willingness to give his time so generously has been very much appreciated.
