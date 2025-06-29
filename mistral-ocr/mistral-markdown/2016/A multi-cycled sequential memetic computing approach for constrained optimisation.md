# A multi-cycled sequential memetic computing approach for constrained optimisation 

Jianyong Sun ${ }^{\text {a,b,c, }}$, Jonathan M. Garibaldi ${ }^{\text {c }}$, Yongquan Zhang ${ }^{\text {d }}$, Abdallah Al-Shawabkeh ${ }^{\text {e }}$

${ }^{a}$ School of Computer and Software, Nanjing University of Information Science and Technology, China
${ }^{\text {b }}$ School of Computer Science and Electrical Engineering, University of Essex, Colchester CO4 3SQ, UK
${ }^{c}$ School of Computer Science, The University of Nottingham, Nottingham NG8 1BB, UK
${ }^{\text {d }}$ Department of Applied Mathematics, China Jiliang University, Hangzhou, Zhejiang 310018, China
${ }^{e}$ Faculty of Engineering and Science, University of Greenwich, Kent ME4 4TB, UK

## ARTICLE I N F O

Article history:
Received 18 October 2014
Revised 30 October 2015
Accepted 2 January 2016
Available online xxx

Keywords:
Multi-cycled sequential memetic computing approach
Estimation of distribution algorithm
Constrained optimisation

## A B STRUCT

In this paper, we propose a multi-cycled sequential memetic computing structure for constrained optimisation. The structure is composed of multiple evolutionary cycles. At each cycle, an evolutionary algorithm is considered as an operator, and connects with a local optimiser. This structure enables the learning of useful knowledge from previous cycles and the transfer of the knowledge to facilitate search in latter cycles. Specifically, we propose to apply an estimation of distribution algorithm (EDA) to explore the search space until convergence at each cycle. A local optimiser, called DONLP2, is then applied to improve the best solution found by the EDA. New cycle starts after the local improvement if the computation budget has not been exceeded. In the developed EDA, an adaptive fully-factorized multivariate probability model is proposed. A learning mechanism, implemented as the guided mutation operator, is adopted to learn useful knowledge from previous cycles.

The developed algorithm was experimentally studied on the benchmark problems in the CEC 2006 and 2010 competition. Experimental studies have shown that the developed probability model exhibits excellent exploration capability and the learning mechanism can significantly improve the search efficiency under certain conditions. The comparison against some well-known algorithms showed the superiority of the developed algorithm in terms of the consumed fitness evaluations and the solution quality.
(c) 2016 Elsevier Inc. All rights reserved.

## 1. Introduction

2 The goal of this paper is to develop a memetic algorithm for the constrained optimization problem which is also referred to as nonlinear programming (NLP) [3]. The NLP can be stated as follows:

$$
\min f(\mathbf{x}), \mathbf{x} \in \mathcal{F} \in \mathbb{R}^{n}
$$

[^0]
[^0]:    ${ }^{a}$ Corresponding author at: School of Computer Science and Electrical Engineering, University of Essex, Colchester CO4 3SQ, UK. Tel.: +44 7896118919. E-mail address: jysun@essex.ac.uk, j.sun@greenwich.ac.uk (J. Sun).
    http://dx.doi.org/10.1016/j.ins.2016.01.003
    0020-0255/© 2016 Elsevier Inc. All rights reserved.

where $f(\mathbf{x})$ is the objective function, and $\mathcal{F}$ is the set of feasible solutions that satisfies:

$$
\begin{cases}g_{i}(\mathbf{x}) \leq 0, & i=1, \ldots, q \\ h_{j}(\mathbf{x})=0, & j=q+1, \ldots, m\end{cases}
$$

5 Often, a solution $\mathbf{x}$ is regarded as feasible, if

$$
\begin{cases}g_{i}(\mathbf{x}) \leq 0 & \forall i=1, \ldots, q \\ \left|h_{j}(\mathbf{x})\right|-\varepsilon \leq 0 & \forall j=q+1, \ldots, m\end{cases}
$$

6 where $\varepsilon$ is small positive real number. The NLP can then be restated as (cf. (1)):

$$
\min f(\mathbf{x}), \mathbf{x} \in \mathcal{F}=\left\{\mathbf{x}: \hat{g}_{i}(\mathbf{x}) \leq 0,1 \leq i \leq m\right\}
$$

where $\hat{g}_{i}=g_{i}, 1 \leq i \leq q, \hat{g}_{j}=\left|h_{j}\right|-\varepsilon, j=q+1, \ldots, m$. Many machine learning problems, such as image processing [68], ordinal regression [17,18], robust clustering [55,57], correlation analysis [58], and others, can be formulated as NLP.

One of the main concerns in developing evolutionary algorithms (EAs) for the NLP is on how to select promising parent individuals for offspring reproduction. An effective selection method, or essentially individual ranking, should balance the feasibility and the objective values of the individuals. Note that an individual with small objective function value might not even be feasible. Most of the selection strategies are based on the superiority of feasible solutions over infeasible solutions [49]. However, Jiao et al. [26] found that global optimal solutions are more likely to be found on the boundary between the non-dominated and feasible sets.

Various constraint-handling techniques have been developed for effective ranking. The stochastic ranking (SR) method [51] ranks the individuals by balancing the objective function value and the penalty on constraint violations stochastically. An addition of ranking method developed in [21] ranks various numerical properties of the population such as the values of the objective functions, the constraint violations, and the number of constraint violations, respectively; and aggregates these rankings together as the final ranking criterion. Some authors, e.g. [1,11], proposed to rank individuals based on Pareto dominance relation in a multi-objective perspective. In [2], the authors proposed to adapt the penalty parameters. In [47], the authors proposed to first identify which constraints are effective and then use them to contribute to the fitness evaluation. In [59], the $\varepsilon$-constraint handling method was proposed in which an $\varepsilon$ parameter is applied to control the relaxation of the constrains. A rough penalty method based on the rough set theory was proposed in [32]. The ensembles of these constraint-handling techniques were claimed to reduce the use of fitness evaluations and perform better than algorithms with a single constraint-handling technique in [38]. In [48], the authors studied several existing constraint-handling strategies and proposed several methodologies based on parent-centric and inverse parabolic probability distribution. The authors in [19] found that existing constraint-handling methods are applied to assist but not to guide the search process. They thus proposed the so-called constraint consensus methods to assist infeasible individuals to move towards the feasible region. Interested readers are referred to [41,43] for reviews, and [10,40] for recent advances on constraint-handling.

Another important issue in developing effective EAs for the NLP is on the offspring generation scheme. It is expected that the scheme should be able to explore feasible regions of the NLP in the early stages, and exploit for the global optimum later on. The search abilities of a range of EAs on the NLP (including genetic algorithms [22,63], evolution strategies, evolutionary programming [4], differential evolution [14], particle swarm optimisation [13,20], and many others) have been extensively studied. To the best of our knowledge, the application of EDAs is very limited. In [16], two EDAs coupled with different constraint-handling methods were compared but only on two test problems. The continuous Gaussian model was used in [53] for constrained optimisation.

Besides these research efforts, some researchers have made attempts to develop memetic computing (MC) approaches, i.e. the hybridisation of local optimization and EAs, for the NLP. The MC approach has been well acknowledged as a promising paradigm for dealing with various types of optimization problems [8]. In this paper, we develop a multi-cycled sequential MC framework, where an EDA and a classical constrained optimization algorithm is hybridised sequentially. Further, a simple learning scheme is proposed to learn useful information from previous cycles to improve the search efficiency in latter cycles.

In the rest of the paper, related work on MC is reviewed in Section 2. We then present the multi-cycled sequential MC framework in Section 3. The developed algorithm is presented in Section 4. The experimental results are summarised in Section 5. Section 6 concludes the paper and discusses future work.

# 2. Related work 

The development of the MC approaches has been proceeding in two main directions. On one hand, different metaheuristics are combined to take advantages of their respective strengths. For example, in [29], a combination of fuzzy logic and evolutionary programming is proposed to handle constraints. In [9], evolutionary programming is hybridized with GENOCOP [42] for the NLP. In [64] and [59], GAs are combined with simulated annealing and PSO, respectively, for the NLP. The integration of artificial bee colony and bees algorithm was presented in [61]. In [23], a novel variant of invasive weed optimization was combined as a local refinement procedure within differential evolution [23]. The combination of variability evolution [35] and CMA-ES [36] was proposed in [37] for the NLP.

Please cite this article as: J. Sun et al., A multi-cycled sequential memetic computing approach for constrained optimisation, Information Sciences (2016), http://dx.doi.org/10.1016/j.ins.2016.01.003

On the other hand, classical numerical optimization approaches for the NLP have been hybridized in EAs. One of the main advantages of classical approaches is that they are usually very efficient in locating feasible local optimum, but the search efficiency highly depends on the quality of the initial solution. Starting from a 'bad' solution, a classical approach could either only find an infeasible solution, or need a high computational cost to reach a feasible local optimum. Thus, effective strategies to address when and how to apply the classical approach should be the main considerations in designing a MC approach.

In recent literature (see e.g. [8,45]), the authors considered the MC approaches as a broader subject of memetic algorithms (MAs). They stated that a MA is composed by an evolutionary framework that integrates one or more local search components within the generation cycle of the evolutionary framework; while a MC is simply a hybrid algorithm without a specific structure. As summarised in [44,46], basic MAs can be considered as local minimizer(s) acting on evolutionary population, in which local optimiser(s) is applied to every single individual. From the view of computational cost, it is highly likely that such an indiscriminate strategy will result in a high computational cost. An obvious reason is that some individuals with low fitness cannot survive from the selection operation in the evolution procedure, which means that the improvement efforts will be wasted. Obviously, more uses of local improvements imply more efforts on exploitation. As a result, too much emphasises on exploitation could be placed on the existing EAs, at least in some cases. In other words, the balance of exploration and exploitation may be shifted too much in favour of exploitation.

Some efforts have been made to address this shortcoming. One way is to apply the local optimisers only on a proportion of promising individuals at each generation [46]. However, one can criticise that it is not fair to the other individuals when the selection operation is performed. This is because a local search on a low-quality solution does not necessarily lead to a low-quality local optima, especially in the constraint optimization context [26].

Another way is to apply the local search only after the EA has converged. Under this strategy, to obtain a good algorithm performance, the hope is that the best solution found by the EA is located in the attraction basin of a high-quality solution. Unfortunately, this is not always the case. No scheme in this strategy is provided to escape from the found optimum if it is not global.

In recent literature, a sequential memetic computing (SMC) approach has been implemented [25,56]. In such structure, components in the evolutionary framework and the local optimiser(s) are all considered as operators. The evolution procedure can be considered as a connected structure of those operators. The structure simplifies the MA structure, and has the potential to alleviate the aforementioned problems existed in the MAs. In [25], a single solution evolves till convergence and a parametrised local search improves the solution at different stages with different parameter settings. In [7], a metaheuristic is first applied to find a promising solution and to compute a separability index; two heuristic local optimisers are then selected according to the index to improve the promising solution. In our work [56], an EDA is hybridized with a classical local optimiser under a SMC structure. These papers have shown that a simple SMC approach is highly potential to improve the search efficiency.

# 3. The multi-cycled sequential memetic computing structure 

We observe that existing SMC approaches do not take an EA as a single operator. Rather, the EA operators and local optimiser(s) are connected sequentially within an evolutionary framework. Obviously, an EA takes some inputs (e.g. fitness function, algorithmic parameters, etc.) and outputs some solutions, which is similar to what other operators (such as crossover and mutation operators in GA) do. In this paper, we propose to use a complete EA as an operator; and connect it with local optimiser(s) sequentially. Further, we propose to employ the combination of EA and local optimiser(s) multiple times until the computational budget has been reached. If we consider the composition of EA and local optimiser as a cycle, we end up with a multi-cycled SMC structure.

Under the multi-cycled SMC structure, firstly, we do not apply local optimisers to any individual during the EA search procedure. This avoids wasting computational resources on unpromising individuals under the MA structure. Secondly, the multiple-cycle structure can provide a mechanism to improve search efficiency. That is, we can gradually accumulate useful knowledge from previous cycles, and apply them in later cycles to either escape from previously found local optima, or to accelerate the exploitation. To the best of our knowledge, no MC-based algorithms have been proposed to take the multicycled structure, which means no learning mechanisms have ever been studied. Moreover, no efforts have been carried out to apply the multi-cycled SMC structure for the NLP.

The above multi-cycled SMC approach for optimisation problems can be summarised in Algorithm 1. In the algorithmic framework, $\Theta_{1}$ and $\Theta_{2}$ are the parameters of the EA and the local optimiser, respectively, and $c$ is the cycle index. At each cycle, EvolutionaryAlgorithm( $\Theta_{1}$, history) takes the history information into account, and returns the best solution found (denoted as $\mathbf{x}_{c}$ ) in line 3. In the first cycle, no history information is available, we thus set history $=\emptyset$ (line 1). LocalSearch( $\mathbf{x}_{c}, \Theta_{2}$ ) improves $\mathbf{x}_{c}$ to a local optimum $\mathbf{x}_{c}^{*}$ (which is called the cycle best solution) in line 4. The global best solution $\mathbf{x}^{*}$ is updated after the local improvement (line 5). Useful information $S$ is then learned from the current cycle by LearningFromHistory() (line 6). The cycle index and the history information are updated hereafter (line 7). A new cycle starts if the computational budget has not been exceeded. The global best solution $\mathbf{x}^{*}$ is returned on termination.

```
Algorithm 1 Multi-cycled sequential memetic computing framework.
Require: parameters \(\Theta_{1}\) and \(\Theta_{2}\)
Ensure: The best solution found \(x^{\circ}\)
    Initialization. Set \(c=0\), history \(=\emptyset\);
    while computational budget has not been exceeded, do
        \(\mathbf{x}_{c}=\) EvolutionaryAlgorithm( \(\Theta_{1}\), history);
        \(\mathbf{x}_{c}^{*}:=\operatorname{LocalSearch}\left(x_{i}, \Theta_{2}\right)\);
        \(\mathbf{x}^{*}:=\min \left\{\mathbf{x}_{i}^{*}, 1 \leq j \leq c\right\}\);
        \(S:=\operatorname{LearningFromHistory(}) ;\)
        \(c:=c+1\); history \(:=\) history \(\rfloor j S\).
    end while
```

Algorithm 2 Multivariate adaptive probability model.
Require: The selection population $\mathcal{P}^{s}(t)=\left\{\mathbf{x}^{1}(t), \ldots, \mathbf{x}^{K}(t)\right\}$
Ensure: The probability $p(\mathbf{x} ; t)$.

1: for $1 \leq i \leq n$ do
Find $\ell_{i}^{\min }\left(\ell_{i}^{\max }\right)=\min (\max )\left\{x_{i}^{k}(t), 1 \leq k \leq K\right\}$;
3: Assign a small probability to the intervals $\left[\ell_{i}^{\min }-\epsilon_{i}, \ell_{i}^{\min }\right]$ and $\left[\ell_{i}^{\max }, \ell_{i}^{\max }+\epsilon_{i}\right]$, and a big probability to $\left[\ell_{i}^{\min }, \ell_{i}^{\max }\right]$.
4: end for

# 4. The working algorithm 

In this section, we present a simple working algorithm according to the generic scheme proposed in the above section. An estimation of distribution algorithm (EDA) is proposed as the EA operator. As well known, in an EDA, offspring are generated by sampling from a probability model, which is constructed from selected promising individuals, at each generation. The probability model is to represent the statistical information extracted from the selected promising solutions. The way to construct the probability model differentiates the EDA instantiations. Readers are referred to [28] for detailed descriptions of these EDAs.

### 4.1. Adaptive probability model and multiple sampling strategy

In existing EDAs, the probability model for real variables is usually assumed to be a Gaussian distribution [28], a Gaussian mixture [5], or a histogram [62,67]. In this paper, we propose to construct a full-factorised adaptive multivariate model. That is, we assume $p(\mathbf{x} ; t)=\prod_{i=1}^{n} p\left(x_{i} ; t\right)$ where $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)^{\mathrm{T}}$. The construction of $p(\mathbf{x} ; t)$ is presented in Algorithm 2, where a selected population containing a set of $K$ individuals $\mathcal{P}^{s}(t)$ is the input. First, the range of the $i$-th variable in $\mathcal{P}^{s}(t)$ is sought, denoted as $\left[\ell_{i}^{\min }, \ell_{i}^{\max }\right]$ (line 1 ); then the range is expanded with a small positive number $\epsilon_{i}$; different probabilities are assigned to the range interval $\left[\ell_{i}^{\min }, \ell_{i}^{\max }\right]$ and the expanded intervals $\left(\left[\ell_{i}^{\min }-\epsilon_{i}, \ell_{i}^{\min }\right]\right.$ and $\left[\ell_{i}^{\max }, \ell_{i}^{\max }+\epsilon_{i}\right]$ ) (line 3).

The developed EDA exhibits several new features in model construction and sampling. First, a uniform distribution is assumed over the range interval $\left[\ell_{i}^{\min }, \ell_{i}^{\max }\right]$. This is meant to preserve the diversity during the search. Second, the expansion intervals $\left[\ell_{i}^{\min }-\epsilon_{i}, \ell_{i}^{\min }\right]$ and $\left[\ell_{i}^{\max }, \ell_{i}^{\max }+\epsilon_{i}\right]$ are meant to address the premature convergence problem. Finally, we propose to use a multiple sampling strategy to make the sampling more effective, which is meant to address the sampling noise problem.

To the best of our knowledge, in almost all EDAs, the number of sampled offspring from the probability model $p(\mathbf{x} ; t)$ is usually less than, or equal to, the population size. However, it is well known that to accurately characterise $p(\mathbf{x} ; t)$, a large sampling size is needed [50]. Therefore, statistically speaking, a small sample size will result in high sampling noise, which might falsely guide the evolutionary search. That is, the search may be leaded to possibly non-promising areas. The problem will become much serious when $p(\mathbf{x} ; t)$ is complex. To address this problem, we propose to generate a number of offspring which is $k(>1)$ (we call it the sampling factor) times of the population size.

### 4.2. The learning from previous cycles

An important contribution of the proposed framework is that it enables the learning from previous cycles to improve the search efficiency in latter cycles. This section presents a simple learning method.

The most important message we obtained from previous cycles is the location information of the global best $\mathbf{x}^{\circ}$. This information should be incorporated in the new cycle. One possible way to take advantage of the location information is to combine it in the sampling procedure by using the guided mutation method [66]. Algorithm 3 describes the guided mutation in detail, where $\lceil A\rceil$ represents the rounding of $A$ to the nearest integers greater than or equal to $A$. Basically speaking, the guided mutation generates an offspring by copying a part of $\mathbf{x}^{\circ}$, and filling the other part by sampling from a probability model.

# ARTICLE IN PRESS 

Algorithm 3 Guided mutation operator.
Require: a template solution $\mathbf{x}^{*}$, a real number $0 \leq \alpha \leq 1$ and a probability model $p(\mathbf{x} ; t)=\prod p\left(x_{j} ; t\right)$.
Ensure: An offspring $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)^{\mathrm{T}}$.
1: Set $U=[1,2, \ldots, n]$ and $N:=\lceil\alpha n\rceil$; Randomly select a set of indices $V \subset U$ with $|V|=N$;
2: For an index $i \in V$, set $x_{i}:=x_{i}^{*}$; For an index $j \in U \backslash V$, sample a value $y$ from the probability model $p\left(x_{j} ; t\right)$, set $x_{j}:=y$;
3: Return $\mathbf{x}$

The underlying rationale behind the guided mutation is closely related to the so-called proximity optimality principle (POP) [15], which has been explicitly or implicitly applied in almost all meta-heuristics. The POP states that good solutions have similar structure. By using the guided mutation operator, some elements of the global best solution is statistically retained during the search. Under certain conditions, retaining these location information will improve the algorithmic search efficiency. We will discuss the condition in Section 4.5.

### 4.3. Selection and replacement

The selection process has been widely studied in the constrained evolutionary optimisation literature, mostly based on constrain-handling techniques. Selection methods based on penalty methods will bias the search, while those based on multi-objective approaches will not. However, as stated in [52], the unbiased search does not necessarily improve the search efficiency. Since local optimisers usually work better on a feasible solution than on an infeasible solution, we prefer to use a selection method that favours feasible solutions. Here, the selection method, called the over-penalised approach in [52], is adopted in this paper.

In the over-penalised approach, the feasible individuals are ranked higher than the infeasible individuals. The feasible solutions are sorted according to their objective function values $f$. The infeasible individuals are ranked according to the penalty function values $\psi$, which is defined as $\psi(x)=f(\mathbf{x})+\sum_{j} g_{j}^{*}(\mathbf{x})^{\beta}$ where $g_{j}^{*}(\mathbf{x})=\max \left\{0, g_{j}(\mathbf{x})\right\}$, and $\beta=2$.

Regarding replacement, we again adopt the over-penalised selection approach to form new population. At each generation, the best individuals are used to construct the probability model and passed to the new population, while the rest of the new population is replaced by the best offspring sampled from the constructed probability model.

### 4.4. The local optimiser

We adopt a classical optimisation method developed for the NLP, called DONLP2 (abbreviation for 'DO NonLinear Programming') [54] to improve the best solution found by the EDA. DONLP2 is based on the sequential quadratic programming method (SQP), in which fully regularised mixed constrained sub-problems are used to deal with non-regular constraints. It incorporates techniques including a slightly modified Pantoja-Mayne update for the Hessian of the Lagrangian, a variable dual scaling and an improved Armijo-type step size algorithm to improve the search efficiency of the SQP.

The most important algorithmic parameters of the DONLP2, i.e. $\Theta_{2}$ in Algorithm 1, include $\tau_{0}$ which gives a bound describing how much the unscaled penalty-term (the $L_{1}$-norm of the constraint violation) may deviate from zero and $\delta_{0}$ which is a binding constraint. In our experimental simulations, we set $\tau_{0}=1.0$ and $\delta_{0}=0.2$ as suggested in [54]. Moreover, we do not calculate the analytical form of the gradients and Hessian of the Lagrangian, but using numerical differentiation. The used NFEs for computing the differentials are included in the calculation of the overall NFEs in the sequel reports.

### 4.5. Remarks on thealgorithmic framework and the working algorithm

In this section, we discuss the pros and cons of the algorithmic framework, and the condition that the working algorithm will be effective.

### 4.5.1. The algorithmic framework

In the sequel, we assume that there are a limited number of feasible local optima ${ }^{1} \mathbf{x}_{i}^{*}, 1 \leq i \leq M$ in terms of the fitness function $\lambda(\mathbf{x})=f(\mathbf{x})$. They can be sorted in a descending order, denoted as $\mathbf{x}_{1}^{*}, \mathbf{x}_{2}^{*}, \ldots, \mathbf{x}_{M}^{*}$ where $\lambda\left(\mathbf{x}_{1}^{*}\right) \geq \lambda\left(\mathbf{x}_{2}^{*}\right) \geq \cdots \geq$ $\lambda\left(\mathbf{x}_{M}^{*}\right)$.

In the sequel, we define

$$
\phi\left(\mathbf{x}_{i}^{*}\right)=\left\{\mathbf{x}^{*} \mid \exists j \in\{1,2, \ldots, \mathrm{n}\} \backslash\{i\} \text {, s.t. }\left|x_{j}^{*}-x_{i j}^{*}\right|<\varepsilon\right\}
$$

where $\varepsilon$ is very small positive number. That is, $\phi\left(\mathbf{x}_{i}^{*}\right)$ contains the optima that is close to the $i$-th optimal solution. Further, we introduce the condition

$$
\phi\left(\mathbf{x}_{i}^{*}\right) \bigcap \phi\left(\mathbf{x}_{j}^{*}\right) \neq \emptyset \text { for } j>i
$$

[^0]
[^0]:    ${ }^{1}$ Readers that are interested in the theoretical analysis on the collaboration between global search and local search please refer to [33,34], in which the concept of local search zones are defined and studied. Here, we only consider local optima rather than the local search zones since local optimiser is considered as a black-box in the SMC structure, and its application only result in local optima.

    Please cite this article as: J. Sun et al., A multi-cycled sequential memetic computing approach for constrained optimisation, Information Sciences (2016), http://dx.doi.org/10.1016/j.ins.2016.01.003

![img-0.jpeg](img-0.jpeg)

Fig. 1. The demonstration of the solution path using the problem instance $g_{02}$ as an example.
which indicates that the two optima $\mathbf{x}_{i}^{*}$ and $\mathbf{x}_{i}^{*}$ have common elements. This can be seen as the mathematical formalisation of the POP. Note that the condition (3) also implies that $\phi\left(\mathbf{x}_{i}^{*}\right) \neq \emptyset$ for all $i, 1 \leq i \leq M$. This can be proved by using contradiction as follows. Suppose for some $i, \phi\left(\mathbf{x}_{i}^{*}\right)=\emptyset$. Then for all $j>i, \phi\left(\mathbf{x}_{i}^{*}\right) \cap \phi\left(\mathbf{x}_{i}^{*}\right)=\emptyset$, which contradicts the condition.

Moreover, we can see that if such a condition holds, a solution path exists under the proposed multi-cycled SMC structure. That is, starting from a local optimum $\mathbf{x}_{i_{1}}^{*}, i_{1} \in\{1, \ldots, M\}$, a better local optimum $\mathbf{x}_{i_{2}}^{*}, i_{2}>i_{1}$ can be found at further cycles since $\phi\left(\mathbf{x}_{i_{1}}^{*}\right) \cap \phi\left(\mathbf{x}_{i_{2}}^{*}\right) \neq \emptyset$. Applying the evolutionary cycle $K$ times, we will end up with a sequence of local optima $\mathbf{x}_{i_{1}}^{*}, \ldots, \mathbf{x}_{i_{k}}^{*}$, or a 'solution path', with

$$
\phi\left(\mathbf{x}_{i_{1}}^{*}\right) \cap \phi\left(\mathbf{x}_{i_{2}}^{*}\right) \neq \emptyset, i_{j}<i_{k} ; \text { and } \lambda\left(\mathbf{x}_{i_{1}}\right) \leq \lambda\left(\mathbf{x}_{i_{1}}\right)
$$

Hence, we call Eq. (3) as the "solution path" condition.
The above discussion suggests that the multi-cycled SMC structure will be effective on problem instances that satisfy the solution path condition. It also suggests that if $\phi\left(\mathbf{x}_{i}^{*}\right) \cap \phi\left(\mathbf{x}_{i}^{*}\right)=\emptyset$, the effectiveness of the framework is thus doubtful on those problem instances since the information learned from history has no help for future search.

### 4.5.2. The working algorithm

According to [65], an EDA with truncation selection converges if the truncation threshold (i.e. the percentage of individuals being selected to the next generation) is less than 1 . The over-penalised selection approach can be considered as a truncation selection with adaptive threshold. The threshold will be always smaller than 1 since not all individuals will be passed to the new generation. Therefore, we can conclude that the proposed EDA converges to a solution $\mathbf{x}_{t}(t)$ at the $t$-th cycle. Under the proposed structure, $\mathbf{x}_{t}(t)$ is improved by the DONLP2 to obtain $\mathbf{x}_{t}^{*}(t)$ at generation $t$. It has been proved in [54] that the DONLP2 holds a local convergence property. Therefore, $\mathbf{x}_{t}^{*}(t)$ is a local optimum.

According to previous discussion, if for some problem instances, the solution path condition holds, we can see that the guided mutation operator will be very efficient in finding a better optimum in the solution path since it can stochastically retain some location information of the present local optimum.

Fig. 1 shows the solutions (four local optima and the global optimum) found by the developed algorithm on $g_{02}$ in five cycles. The objective function values of the local optima are shown in the legend. From Fig. 1, we can see that many variables (including $x_{1-2}, x_{4-5}, x_{7-8}, x_{11-20}$ ) of the local optima take similar values to the global optimum. In latter cycles, the rest variables $\left(x_{3,6,9,10}\right)$ are gradually modified. This example shows that the "solution path" condition holds for $g_{02}$.

## 5. Experimental results

In the developed algorithm, called the multi-cycled evolutionary (MCEA) algorithm, the parameters (i.e. $\Theta_{1}$ ) of the EDA include the population size $M$, the selection size $K$, the sampling factor $k$, the guided mutation parameter $\alpha$, and the expansion parameter $\epsilon$. The expansion in each dimension of the search space is set to be $\epsilon_{i}=\frac{b_{i}-a_{i}}{M}, 1 \leq i \leq n$ where $a_{i}$ and $b_{i}$ are the lower and upper bound, respectively. This setting is to eliminate the effect of the variable scales in different coordinates. Regarding the criterion to decide when a new cycle starts, in our implementation, new cycle starts if the number of generations is more than 30 ; and in consecutive 5 generations, ${ }^{2}$ there are no better solutions found.

In this section, firstly we analyse the effects of the proposed EDA components to the algorithmic performance and the algorithm's sensitivity to the parameters. We then compare the developed algorithm with some well-known algorithms including the winners of the CEC 2006 and 2010 competitions. Readers are referred to [30] and [39] for detailed problem definitions.

[^0]
[^0]:    ${ }^{2}$ These values used here were chosen based on experiments we carried out for the test problems.

Table 1
Experimental results obtained by the MCEA, the MCEH and MCEG on the test problems except $g_{00}$ and $g_{23}$.

| Function | MCEA |  |  | MCEH |  |  | MCEG |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | \# succ_run | NFE | \#cycle | \#succ_ | NFE | \#cycle | \#succ_run | NFE | \#cycle |
| $g_{01}$ | 1.00 | 5774 | 4.16 | 1.00 | 8606 | 8.20 | 1.00 | 7232 | 7.12 |
| $g_{02}$ | 1.00 | 74,030 | 33.16 | 1.00 | 59,712 | 30.76 | 0.00 | 500,000 | 112.36 |
| $g_{03}$ | 1.00 | 1326 | 1.00 | 1.00 | 3346 | 2.36 | 1.00 | 3346 | 2.36 |
| $g_{04}$ | 1.00 | 412 | 1.00 | 1.00 | 433 | 1.00 | 0.92 | 40,470 | 86.08 |
| $g_{05}$ | 1.00 | 417 | 1.00 | 1.00 | 398 | 1.00 | 1.00 | 381 | 1.00 |
| $g_{06}$ | 1.00 | 467 | 1.00 | 0.96 | 20,385 | 58.12 | 1.00 | 196 | 1.00 |
| $g_{07}$ | 1.00 | 2207 | 1.00 | 1.00 | 1432 | 1.00 | 1.00 | 1368 | 1.00 |
| $g_{08}$ | 1.00 | 458 | 2.56 | 1.00 | 416 | 2.08 | 1.00 | 450 | 2.56 |
| $g_{09}$ | 1.00 | 1030 | 2.08 | 1.00 | 416 | 1.00 | 1.00 | 1480 | 1.00 |
| $g_{10}$ | 1.00 | 13,359 | 1.00 | 1.00 | 37,859 | 1.48 | 1.00 | 33,533 | 1.32 |
| $g_{11}$ | 1.00 | 174 | 1.00 | 1.00 | 155 | 1.00 | 1.00 | 174 | 1.00 |
| $g_{12}$ | 1.00 | 196 | 1.00 | 1.00 | 198 | 1.00 | 1.00 | 197 | 1.00 |
| $g_{13}$ | 1.00 | 1065 | 1.88 | 1.00 | 506 | 1.00 | 1.00 | 1501 | 3.00 |
| $g_{14}$ | 1.00 | 3642 | 2.68 | 1.00 | 7590 | 9.40 | 0.00 | 500,000 | 731.24 |
| $g_{15}$ | 1.00 | 292 | 1.00 | 1.00 | 303 | 1.08 | 1.00 | 277 | 1.00 |
| $g_{16}$ | 0.96 | 22,058 | 26.56 | 0.96 | 21,587 | 23.44 | 1.00 | 25,311 | 31.12 |
| $g_{17}$ | 0.80 | 257,115 | 73.24 | 0.76 | 266,865 | 63.04 | 0.92 | 353,855 | 35.76 |
| $g_{18}$ | 1.00 | 7657 | 7.04 | 1.00 | 4150 | 3.72 | 1.00 | 3893 | 2.92 |
| $g_{19}$ | 1.00 | 4078 | 1.00 | 1.00 | 2617 | 1.00 | 1.00 | 2846 | 1.00 |
| $g_{21}$ | 1.00 | 34,152 | 8.12 | 0.88 | 180,512 | 39.16 | 0.56 | 359,339 | 54.72 |
| $g_{23}$ | 1.00 | 4321 | 1.36 | 1.00 | 3403 | 1.00 | 1.00 | 2388 | 1.60 |
| $g_{24}$ | 1.00 | 181 | 1.00 | 1.00 | 164 | 1.00 | 1.00 | 239 | 1.40 |

# 221 5.1. Comparison metrics 

The comparison metrics include the success rate (\#succ_run), the average number of fitness evaluation consumed (NFE), and the average number of cycles (\#cycle). Suppose that in total $T$ runs, there are $K$ successful runs. For each run $i$, the consumed NFEs is $N_{i}$ (if not successful, $N_{i}$ is the maximum NFEs allowed) and the number of cycles is $C_{i}$, then the success rate is defined as \#succ_run $=K / T$, the average NFEs is computed as NFE $=\sum_{i=1}^{T} N_{i} / K$, and the average number of cycles is defined as \#cycle $=\sum_{i=1}^{T} C_{i} / T$.

### 5.2. Component analysis

The two aspects that mostly affect the performance of the proposed algorithm are the exploration capability of the probabilistic model, and the learning capability of the guided mutation operator. The component analysis aims to investigate their respective contributions. Moreover, we intend to study the effect of the constraint-handling techniques to the algorithmic performance. The CEC 2006 test problems are used for the analysis. The experimental configurations are set as follows: the positive number to relax the equality constraints is $\varepsilon=0.0001$. the number of runs is 25 and the maximum number of fitness evaluations (NFEs) is 500,000 . At each run, the NFEs needed to find a solution satisfying $f(\mathbf{x})-f\left(\mathbf{x}^{*}\right)<\varepsilon$ are recorded.

### 5.2.1. The probability model

The effect of the probability model can be carried out by adopting different probability models in the proposed EDA. In this study, we compare the histogram model and the Gaussian model with the proposed adaptive model. The resultant algorithms are called MCEH (with histogram model), and MCEG (with Gaussian model), respectively. Those probability models are all fully-factorised multivariate models. In the histogram model, the bound of each variable is divided into 10 subintervals (as suggested in [67]), and the histogram of the selected individuals is normalised to be the probability distribution over these subintervals. The Gaussian model assumes that the selected individuals at each variable follows a Gaussian distribution.

The parameter settings of these algorithms are $M=2 n, k=1$, and $\alpha=0.3$. Table 1 summarises the comparison metrics obtained by the compared algorithms for the test problems except $g_{20}$ and $g_{22}$ (since they do not have feasible solutions).

In Table 1, entries in bold typeset indicate the least NFEs consumed by the algorithms. From Table 1, we see that in 8 out of 20 test problems, the MCEA consumed fewer NFEs than the MCEH; while in 10 out of 22 test problems, the MCEH requires fewer NFEs than that of the MCEA. In 4 out of 22 test problems, the MCEG performs better than the other two. Though it seems that the histogram model performs better in general, it can be seen from Table 1 that the success rates obtained by the proposed model on functions $g_{06,17,21}$ are higher than those obtained by the histogram model. Moreover, if we focus on those functions (including $g_{02,07-09,11,13,16,19,23,24}$ ) that the histogram model has a better performance, it can

Please cite this article as: J. Sun et al., A multi-cycled sequential memetic computing approach for constrained optimisation, Information Sciences (2016), http://dx.doi.org/10.1016/j.ins.2016.01.003

![img-1.jpeg](img-1.jpeg)

Fig. 2. Comparison of different probability model and selection methods in terms of NFEs on $g_{02}$.

Table 2
The experimental results obtained by the MCEA and the MCES.

| Function | MCEA |  |  | MCES |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | \#_run | NFE | \#cycle | \#_run | NFE | \#cycle |
| $g_{01}$ | 1.00 | 5774 | 4.16 | 1.00 | 15,712 | 10.00 |
| $g_{02}$ | 1.00 | 74,030 | 33.16 | 0.64 | 336,461 | 114.24 |
| $g_{03}$ | 1.00 | 1326 | 1.00 | 0.92 | 118,536 | 77.84 |
| $g_{04}$ | 1.00 | 412 | 1.00 | 1.00 | 458 | 1.00 |
| $g_{05}$ | 1.00 | 417 | 1.00 | 1.00 | 398 | 1.00 |
| $g_{06}$ | 1.00 | 467 | 1.00 | 0.92 | 40,264 | 108.68 |
| $g_{07}$ | 1.00 | 2207 | 1.00 | 1.00 | 1576 | 1.00 |
| $g_{08}$ | 1.00 | 458 | 2.56 | 1.00 | 584 | 2.80 |
| $g_{09}$ | 1.00 | 1030 | 1.00 | 1.00 | 1888 | 1.00 |
| $g_{10}$ | 1.00 | 13,359 | 1.00 | 1.00 | 20,939 | 1.20 |
| $g_{11}$ | 1.00 | 174 | 1.00 | 1.00 | 213 | 1.00 |
| $g_{12}$ | 1.00 | 196 | 1.00 | 1.00 | 196 | 1.00 |
| $g_{13}$ | 1.00 | 1065 | 1.88 | 1.00 | 627 | 1.04 |
| $g_{14}$ | 1.00 | 3642 | 2.68 | 1.00 | 51,218 | 38.36 |
| $g_{15}$ | 1.00 | 292 | 1.00 | 1.00 | 349 | 1.00 |
| $g_{16}$ | 0.96 | 22,058 | 26.56 | 0.96 | 24,184 | 23.32 |
| $g_{17}$ | 0.80 | 257,115 | 73.24 | 0.76 | 289,937 | 85.64 |
| $g_{18}$ | 1.00 | 7657 | 7.04 | 1.00 | 2145 | 1.72 |
| $g_{19}$ | 1.00 | 4078 | 1.00 | 1.00 | 3595 | 1.00 |
| $g_{21}$ | 1.00 | 34,152 | 8.12 | 1.00 | 110,405 | 29.96 |
| $g_{22}$ | 1.00 | 4321 | 1.36 | 1.00 | 3522 | 1.00 |
| $g_{24}$ | 1.00 | 181 | 1.00 | 1.00 | 422 | 2.44 |

be seen that except functions $g_{02}, g_{08}$ and $g_{16}$, the average numbers of cycles used by the MCEH and the MCEA to reach the global optimal are all one, which means that it is fairly easy for the histogram and the adaptive model to obtain high-quality initial solutions.

Since the main difference between the compared algorithms is on the probabilistic model used in the EDA, we may conclude that the proposed adaptive model can result in better exploration capability than the others. Fig. 2 shows the boxplots of the NFEs consumed by the MCEA, MCEH and MCEG, respectively, on $g_{02}$.

# 5.2.2. The contribution of the constraint-handling 

258
260
265
261
262
263
264
265
266
267

We now study the effects of the over-penalised selection and the stochastic ranking selection to the algorithm performance. To carry out the comparison, we build an algorithm, called MCES, in which the stochastic ranking selection is used.

In the experiments, the same algorithmic parameters as above are used by the MCEA. For the MCES, the stochastic ranking parameter is set to 0.45 as suggested in [51]. Table 2 lists the comparison metrics obtained by the two algorithms for the test problems except $g_{20}$ and $g_{22}$. Entries in bold typeset are the least NFEs obtained by the compared algorithms.

From Table 2, we can see that in 16 out of 22 test problems, the over-penalised selection approach performs better than the stochastic ranking selection in terms of the NFEs consumed. In terms of the success rate, it can be seen that the overpenalised approach can obtain higher rates than the stochastic ranking approach in all the test problems, except for $g_{16}$ where the success rates are both one. We thus may conclude that the over-penalised constraint-handling technique is more effective than that of the stochastic ranking under the proposed framework.

Please cite this article as: J. Sun et al., A multi-cycled sequential memetic computing approach for constrained optimisation, Information Sciences (2016), http://dx.doi.org/10.1016/j.ins.2016.01.003

Table 3
The experimental results obtained by the MCEA with different sampling factor $k$. Entries in bold typeset are the least NFEs obtained by the algorithm.

| Function | $k=0.5$ |  | $k=1$ |  | $k=1.5$ |  | $k=2$ | $k=2.5$ | $k=3$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | \#succ_rate | NFE | \#succ_rate | NFE | \#succ_rate | NFE | NFE | NFE | NFE |
| $g_{01}$ | 1.00 | 8005 | 1.00 | 5774 | 1.00 | 6549 | 6728 | 5877 | 7136 |
| $g_{02}$ | 1.00 | 73,131 | 1.00 | 74,030 | 1.00 | 68,968 | 38,931 | 55,270 | 69,043 |
| $g_{03}$ | 1.00 | 4829 | 1.00 | 1326 | 1.00 | 3200 | 1895 | 3969 | 3052 |
| $g_{04}$ | 1.00 | 294 | 1.00 | 412 | 1.00 | 591 | 691 | 950 | 1034 |
| $g_{05}$ | 1.00 | 207 | 1.00 | 417 | 1.00 | 514 | 722 | 861 | 1463 |
| $g_{06}$ | 0.88 | 60,175 | 1.00 | 467 | 1.00 | 526 | 366 | 345 | 536 |
| $g_{07}$ | 1.00 | 1193 | 1.00 | 2207 | 1.00 | 2292 | 2373 | 3198 | 3573 |
| $g_{08}$ | 1.00 | 405 | 1.00 | 458 | 1.00 | 1407 | 444 | 656 | 1116 |
| $g_{09}$ | 1.00 | 756 | 1.00 | 1030 | 1.00 | 1092 | 1198 | 1458 | 1700 |
| $g_{10}$ | 1.00 | 13,619 | 1.00 | 13,359 | 1.00 | 4331 | 5570 | 32,087 | 12,716 |
| $g_{11}$ | 1.00 | 92 | 1.00 | 174 | 1.00 | 246 | 302 | 394 | 471 |
| $g_{12}$ | 1.00 | 109 | 1.00 | 196 | 1.00 | 325 | 396 | 487 | 573 |
| $g_{13}$ | 1.00 | 449 | 1.00 | 1065 | 1.00 | 658 | 1406 | 3739 | 3406 |
| $g_{14}$ | 1.00 | 4227 | 1.00 | 3642 | 1.00 | 3542 | 3155 | 11,242 | 6818 |
| $g_{15}$ | 1.00 | 221 | 1.00 | 292 | 1.00 | 336 | 474 | 669 | 966 |
| $g_{16}$ | 0.92 | 41,822 | 0.96 | 22,058 | 0.96 | 21,738 | 1550 | 3000 | 44,211 |
| $g_{17}$ | 0.80 | 257,115 | 0.92 | 181,885 | 0.92 | 145,887 | 89,042 | 93,971 | 110,189 |
| $g_{18}$ | 1.00 | 3416 | 1.00 | 7657 | 1.00 | 4264 | 4338 | 2189 | 6158 |
| $g_{19}$ | 1.00 | 3012 | 1.00 | 4078 | 1.00 | 5078 | 5733 | 6949 | 7843 |
| $g_{21}$ | 1.00 | 44,588 | 1.00 | 34,152 | 1.00 | 48,749 | 48,944 | 17,307 | 52,991 |
| $g_{23}$ | 1.00 | 2274 | 1.00 | 4321 | 1.00 | 3444 | 3315 | 4322 | 5964 |
| $g_{24}$ | 1.00 | 97 | 1.00 | 181 | 1.00 | 404 | 297 | 689 | 500 |

Moreover, in comparison with the results obtained by the MCEH shown in Table 1, one can see that the MCES performs even worse than that of the MECH on most of the test problems. This shows that the exploration capability of the developed EDA does not benefit from the application of the stochastic ranking. Particularly, we can also observe this from the last column in Fig. 2. It shows that the NFEs consumed by the MCES are even more than that of the MCEH.

# 5.3. Sensitivities to the algorithmic parameters 

The main parameters of the working algorithm include the population size $N$, the sampling factor $k$ and the guided mutation parameter $\alpha$. In this section, we investigate the effects of these parameters on the performance of the algorithm.

### 5.3.1. The sampling factor

To test the effects of the sampling factor to the algorithmic performance, we run the algorithm by setting different $k \in$ $(0.5,1,1.5,2,2.5,3)$. The rest parameters are set as $M=2 n$, and $\alpha=0.3$. Table 3 shows the results obtained. In the table, entries in bold typeset are the least NFEs consumed by the algorithm.

In Table 3, we omit the success rates for $k \geq 2$ since they are all one. On one hand, from Table 3, we can see that the MCEA with $k=0.5$ performs the best on most ( 12 out of 22 ) of the test problems in terms of the consumed NFEs. However, as we discussed early in Section 5.2.1, those problems are fairly easy. The good performance of the MCEA with $k=0.5$ might be due to the efficiency of the learning mechanism. On the other hand, if we focus on the functions $g_{06,16,17}$ which are considered as hard, we can see that the best performance is achieved by the MCEA with $k=2$. This indicates that a large sampling size can indeed improve the search efficiency.

Regarding the MCEA with large sampling size (i.e. $k \geq 2$ ), it can be seen that in 19 out of 22 test problems, the MCEA with $k=2$ requires the least NFEs than the MCEA with $k=2.5$ and 3 . This shows that a large sampling factor does not always lead to a competitive performance in terms of computational cost. The sampling factor should be carefully chosen to balance the search efficiency and the computational cost.

We further investigate the interaction between the population size $M$ and the sample factor $k$, using $g_{02}$ as an example. $g_{02}$ is of high-dimensional $(n=20)$, non-linear in both the objective function and the constraints, and multi-modal. Fig. 3 summarises the obtained results. Fig. 3(a) shows the mean NFEs with varied $M \in\{20,40,60,80,100\}$ and $k \in\{0.5,1,1.5,2\}$, while (b) shows the mean number of cycles. From Fig. 3(a), one can see that generally a small sampling size does not always result in a reduced NFEs. Specifically, we can see that in case $k=1$, the consumed NFEs is fewer than that in case $k=0.5$ when the population size is less than 80 . This observation justifies that more samples can reduce the sampling noise in case a small population size is employed, as claimed in Section 4.1. From Fig. 3(b), it can be seen that the number of cycles tends to decrease along with the increase of the population size and the increase of the sampling factor.

![img-2.jpeg](img-2.jpeg)
(a) The interactions of $M$ and $k$ in terms of NFEs.
(b) The interactions of $M$ and $k$ in terms of \#cycles.

Fig. 3. The study of the interactions of the algorithmic parameters $M$ and $k$ to the performance of the MCEA. (a) shows the results in terms of the NFEs; (b) is the results in terms of the number of cycles.

Table 4
The experimental results obtained by the MCEA with different population size $M$. Entries in bold typeset are the least NFEs obtained.

| Function | $M=n$ |  | $M=2 n$ |  | $M=3 n$ |  | $M=4 n$ |  | $M=5 n$ |  | $M=6 n$ |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | NFE | \#cycle | NFE | \#cycle | NFE | \#cycle | NFE | \#cycle | NFE | \#cycle | NFE | \#cycle |
| $g_{01}$ | 5774 | 4.16 | 3745 | 2.64 | 7513 | 3.76 | 4715 | 1.16 | 5205 | 1.00 | 8368 | 1.40 |
| $g_{02}$ | 74,030 | 33.16 | 57,433 | 18.24 | 72,456 | 32.08 | 91,890 | 22.68 | 110,236 | 21.84 | 80,186 | 13.20 |
| $g_{03}$ | 1326 | 1.00 | 2567 | 1.00 | 4106 | 2.36 | 2871 | 1.00 | 3778 | 1.64 | 2709 | 1.00 |
| $g_{04}$ | 412 | 1.00 | 1104 | 1.00 | 691 | 1.12 | 791 | 2.10 | 1106 | 1.08 | 1061 | 1.60 |
| $g_{05}$ | 417 | 1.00 | 353 | 1.00 | 604 | 1.00 | 766 | 1.00 | 718 | 1.00 | 1036 | 1.00 |
| $g_{06}$ | 467 | 1.00 | 426 | 1.00 | 449 | 1.00 | 642 | 1.00 | 515 | 1.00 | 475 | 1.00 |
| $g_{07}$ | 2,207 | 1.00 | 2162 | 1.00 | 2343 | 1.00 | 3101 | 1.00 | 3182 | 1.00 | 5161 | 1.00 |
| $g_{08}$ | 458 | 2.56 | 176 | 1.00 | 658 | 2.76 | 295 | 1.00 | 800 | 2.00 | 663 | 1.48 |
| $g_{09}$ | 1030 | 1.00 | 841 | 1.00 | 915 | 1.00 | 1281 | 1.00 | 1503 | 1.00 | 1631 | 1.00 |
| $g_{10}$ | 13,359 | 1.00 | 12,452 | 1.00 | 21,186 | 1.12 | 12,446 | 1.00 | 17,958 | 1.08 | 21,138 | 1.04 |
| $g_{11}$ | 174 | 1.00 | 153 | 1.00 | 244 | 1.00 | 291 | 1.00 | 370 | 1.00 | 453 | 1.00 |
| $g_{12}$ | 196 | 1.00 | 209 | 1.00 | 315 | 1.00 | 415 | 1.00 | 510 | 1.00 | 580 | 1.00 |
| $g_{13}$ | 1065 | 1.88 | 1566 | 1.00 | 915 | 1.00 | 1875 | 2.04 | 3786 | 3.72 | 8269 | 6.52 |
| $g_{14}$ | 3642 | 2.68 | 3770 | 2.72 | 3578 | 2.72 | 3402 | 2.48 | 3114 | 2.28 | 4146 | 3.04 |
| $g_{15}$ | 292 | 1.00 | 328 | 1.04 | 393 | 1.00 | 527 | 1.00 | 705 | 1.00 | 673 | 1.00 |
| $g_{16}$ | 22,058 | 26.56 | 1326 | 1.00 | 2943 | 1.00 | 3000 | 1.00 | 3282 | 1.00 | 3905 | 1.00 |
| $g_{17}$ | 257,115 | 73.24 | 160,063 | 42.56 | 188,138 | 69.80 | 187,185 | 46.56 | 175,857 | 41.20 | 199,214 | 39.64 |
| $g_{18}$ | 7,657 | 7.04 | 1525 | 1.00 | 3206 | 1.88 | 4311 | 1.60 | 8747 | 3.60 | 8447 | 2.84 |
| $g_{19}$ | 4,078 | 1.00 | 3878 | 1.00 | 5276 | 1.00 | 6.62 | 1.00 | 8116 | 1.00 | 10,178 | 1.00 |
| $g_{21}$ | 34,152 | 8.12 | 23,749 | 11.44 | 34,526 | 13.68 | 65,104 | 18.12 | 88,466 | 21.60 | 54,616 | 15.24 |
| $g_{23}$ | 4321 | 1.36 | 3402 | 1.08 | 3441 | 1.00 | 4032 | 1.20 | 4763 | 1.16 | 4975 | 1.00 |
| $g_{24}$ | 181 | 1.00 | 165 | 1.00 | 318 | 1.36 | 452 | 1.60 | 362 | 1.00 | 462 | 1.08 |

297 In summary, we may conclude that the multiple sampling strategy can indeed improve the search efficiency. But a sampling factor should be carefully chosen to balance the search efficiency and the computational cost. Moreover, the multiple sampling strategy is able to reduce the sampling noise in case a small population size is employed.

# 5.3.2. The guided mutation and the population size 

301
302
303
304
305
306
307
308
310
311

302
303
304
305
306
307
308

309

310

311

312

313

314
315
316

317
318

319
320

321
322

323
324

325
326

327
328

329
330

331
332

333

334
335
336

337
338

339
340

341
342

343
344

345
346

347
348

349
350

351
352

353
354

355
356

357
358

359
360

361
362

363
364

365
366

367
368

369
370

371
372

373

374

375

376

377

378

379

380

381

382

383

384

385

386

387

388

389

390

391

392

393

394

395

396

397

398

399

400

401

402

403

404

405

406

407

408

409

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

500

501

502

503

504

505

506

507

508

509

510

511

512

513

514

515

516

517

518

519

520

521

522

523

524

525

526

527

528

529

530

531

532

533

534

535

536

537

538

539

540

541

542

543

544

545

546

547

548

549

550

551

552

553

554

555

556

557

558

559

600

601

602

603

604

605

606

607

608

609

610

611

612

613

614

615

616

617

618

619

620

621

622

623

624

625

626

627

628

629

630

631

632

633

634

635

636

637

638

639

640

641

642

643

644

645

646

647

648

649

650

651

652

653

654

655

656

657

658

659

660

661

662

663

664

665

666

667

668

669

700

701

702

703

704

705

706

707

708

709

710

711

712

713

714

715

716

717

718

719

720

721

722

723

724

725

726

727

728

729

730

731

732

733

734

735

736

737

738

739

740

741

742

743

744

745

746

747

748

749

750

751

752

753

754

755

756

757

758

759

760

761

762

763

764

765

766

767

768

769

770

771

772

773

774

775

776

777

778

779

780

781

782

783

784

785

786

787

788

789

790

791

792

793

794

795

796

797

798

799

800

801

802

803

804

805

806

807

808

809

810

811

812

813

814

815

816

817

818

819

820

821

822

823

824

825

826

827

828

829

830

831

832

833

834

835

836

837

838

839

840

841

842

843

844

845

846

847

848

849

850

851

852

853

854

855

856

857

858

859

860

861

862

863

864

865

866

867

868

869

870

871

872

873

874

875

876

877

878

879

880

881

882

883

884

885

886

887

888

889

890

891

892

893

894

895

896

897

898

899

900

901

902

903

904

905

906

907

908

909

910

911

912

913

914

915

916

917

918

919

920

921

922

923

924

925

926

927

928

929

930

931

932

933

934

935

936

937

938

939

940

941

942

943

944

945

946

947

948

949

950

951

952

953

954

955

956

957

958

959

960

961

962

963

964

965

966

967

968

969

970

971

972

973

974

975

976

977

978

979

980

981

982

983

984

985

986

987

988

989

990

991

992

993

994

995

996

997

998

999

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

189

190

191

192

193

194

195

196

197

198

199

200

201

202

203

204

205

206

207

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

224

225

226

227

228

229

230

231

232

233

234

235

236

237

238

239

240

241

242

243

244

245

246

247

248

249

250

251

252

253

254

255

256

257

258

259

260

261

262

263

264

265

266

267

268

269

270

271

272

273

274

275

276

277

278

279

280

281

282

283

284

285

286

287

288

289

290

291

292

293

294

295

296

297

298

299

300

291

292

293

294

295

296

297

298

299

300

291

292

293

294

295

296

297

298

299

300

291

292

293

294

295

296

297

298

299

300

291

292

293

294

295

296

297

298

299

300

301

302

303

304

305

306

307

308

309

310

311

312

313

314

315

316

317

318

319

320

321

322

323

324

325

326

327

328

329

330

331

332

333

334

335

336

337

338

339

340

341

342

343

344

345

346

347

348

349

350

351

352

353

354

355

356

357

358

359

360

361

362

363

364

365

366

367

368

369

370

371

372

373

374

375

376

377

378

379

380

381

382

383

384

385

386

387

388

389

390

391

392

393

394

395

396

397

398

399

400

401

402

403

404

405

406

407

408

409

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

491

492

493

494

495

496

497

498

499

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

491

492

493

494

495

496

497

498

499

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

491

492

493

494

495

496

497

498

499

499

491

492

493

494

495

496

497

498

499

499

491

492

493

494

495

496

497

498

499

499

491

492

493

494

495

496

497

498

499

499

491

492

493

494

495

496

497

498

499

499

491

492

493

494

495

496

497

498

499

499

491

492

493

494

495

496

497

498

499

499

499

491

492

493

494

495

496

497

498

499

499

499

491

492

493

494

495

496

497

498

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

499

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

499

499

499

499

499

499

499

499

491

492

493

494

495

496

497

498

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

499

![img-3.jpeg](img-3.jpeg)
(a) The interactions of $M$ and $\alpha$ in terms of NFEs.
(b) The mean NFEs and cycles against $\alpha$.

Fig. 4. The study of the interactions of the algorithmic parameters $M$ and $\alpha$ to the performance of the MCEA. (a) shows the results in terms of the NFEs and (b) is the results in terms of the number of cycles.
result in an accelerated search speed, but also a quick loss of diversity, which will deteriorate the exploration ability and the possibility of escaping from local optima. Therefore, the optimal settings of $M$ and $\alpha$ will be the settings that balance the search speed and diversity.

In our experiment, the study was carried out by varying $\alpha \in\{0.1 \ldots, 0.9\}$ and $M \in\{20,40,60,80,100\}$. Again, $g_{02}$ is used as an example. Fig. 4 summarises the obtained results. Since for all the $\alpha$ settings, the MCEA can successfully locate the global optimum in all runs, we thus do not include the success rate results. Fig. 4(a) shows the average NFEs consumed by the MCEA with different $\alpha$ and $M$ values. From this figure, we can see that the consumed NFEs tend to decrease along with the decrease of the population size for any given $\alpha$. This indicates for $g_{02}$, the loss of diversity due to small population size can be compensated by the learning scheme. Fig. 4(b) shows that the consumed NFEs and the number of cycles increase along with the increase of $\alpha$. This indicates that a large $\alpha$ will limit the exploration ability of the MCEA due to the quick loss of diversity.

# 5.4. Summary on component study 

In summary, we may conclude that (i) the adaptive model can improve the exploration ability of the proposed EDA; (ii) the learning strategy can compensate for the loss of diversity caused by employing a small population size; and (iii) the multiple sampling strategy can improve the search efficiency but need to seek balance with the population size for the best

Table 5
The NFEs consumed by the MCEA, $\varepsilon$-DE, and the other algorithms on the CEC06 test problems.

| Function | MCEA |  |  | $\varepsilon$-DE | Best (Alg.) |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | Min | Mean | Max |  |  |
| $g_{01}$ | 3284 | 6728 | 17,917 | 59,309 | 25,115 (SaDE) |
| $g_{02}$ | 14,654 | 38,930 | 89,309 | 149,827 | 96,222 (MDE) |
| $g_{03}$ | 1773 | 1895 | 1917 | 89,407 | 24,861 (MPDE) |
| $g_{04}$ | 512 | 691 | 891 | 26,216 | 15,281 (GDE) |
| $g_{05}$ | 592 | 724 | 933 | 97,430 | 21,306 (MDE) |
| $g_{06}$ | 270 | 366 | 444 | 7381 | 5202 (MDE) |
| $g_{07}$ | 2035 | 2373 | 3159 | 74,304 | 26,578 (DMS) |
| $g_{08}$ | 331 | 444 | 896 | 1139 | 918 (MDE) |
| $g_{09}$ | 1133 | 1198 | 1235 | 23,121 | 16,152 (MDE) |
| $g_{10}$ | 5071 | 5570 | 5805 | 105,234 | 25,520 (DMS) |
| $g_{11}$ | 292 | 362 | 585 | 16,420 | 3000 (MDE) |
| $g_{12}$ | 382 | 396 | 442 | 4124 | 1308 (MDE) |
| $g_{13}$ | 788 | 1406 | 2998 | 31,096 | 21,723 (MDE) |
| $g_{14}$ | 2601 | 3155 | 3987 | 113,439 | 25,220 (DMS) |
| $g_{15}$ | 447 | 474 | 533 | 83,655 | 10,458 (MDE) |
| $g_{16}$ | 1635 | 1550 | 2270 | 19,122 | 8730 (MDE) |
| $g_{17}$ | 19,345 | 85,478 | 155,419 | 98,860 | 26,364 (MDE) |
| $g_{18}$ | 1948 | 4338 | 7924 | 59,153 | 28,261 (DMS) |
| $g_{19}$ | 4561 | 5732 | 6958 | 356,350 | 21,830 (DMS) |
| $g_{21}$ | 14,513 | 48,944 | 92,988 | 135,142 | 38,217 (PCX) |
| $g_{23}$ | 2212 | 3135 | 3751 | 200,763 | 129,550 (SaDE) |
| $g_{24}$ | 278 | 297 | 380 | 2952 | 1794 (JDE-2) |

Please cite this article as: J. Sun et al., A multi-cycled sequential memetic computing approach for constrained optimisation, Information Sciences (2016), http://dx.doi.org/10.1016/j.ins.2016.01.003

# 5.5. Comparison with EAs on the CEC'06 benchmarks 

In this section, we present the comparison of the MCEA with the algorithms in the CEC'06 competition. Since most of the compared algorithms were successful in all runs, we use the consumed NFEs as the criterion. The experimental results are summarised in Table 5. The minimal, mean and maximum number NFEs in 25 runs for the MCEA are shown in the 'min', 'mean' and 'max' columns, respectively. The column ' $\varepsilon$-DE' shows the average NFEs used by $\epsilon$-DE which is reproduced from [59]. The 'Best(Alg.)' column shows the least NFEs used by the algorithms appeared in the CEC'06 competition. These algorithms are 5aDE [24], MDE [41], MPDE [60], GDE [27], PCX [12], DMS [31] and jDE-2 [6].

From Table 5, it can be seen that the MCEA consumed much fewer NFEs than all the other compared algorithm except for $g_{12}$ where the average NFEs used by the MCEA is more than that of the MDE. However, we may still conclude that on average, the MCEA outperforms these compared EAs in terms of the consumed NFEs on these test problems.

### 5.6. Comparison on the CEC'10 benchmark

In this section, we compared the MCEA with the winner of the CEC'10 competition, called $\epsilon$-Constrained Differential Evolution ( $\epsilon$-DEg), on the CEC'10 test problems. The experimental configurations are the same as those used in CEC'06, except that the maximum NFEs are 200,000 for 10D, and 600,000 for 30D.

Table 6 summarises the statistics (including min, max and median) obtained by the two algorithms. The Wilcoxon rank sum is applied to carry out the hypothesis test at $5 \%$ significance level. In the table, we use notations "+", "-" and " $\sim$ " to denote that the MCEA performs better, worse or similar to the $\epsilon$-DEg in terms of solution quality.

Table 6
The comparison between the developed algorithm and $\epsilon$-DEg on the CEC'10 test problems.

| Prob. | $\epsilon$-DEg |  |  | MCEA |  |  | Hypo. |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Min | Median | Max | Min | Median | Max | Test |
| $D=10$ |  |  |  |  |  |  |  |
| C01 | $-0.747310$ | $-0.747310$ | $-0.738039$ | $-0.747310$ | $-0.747310$ | $-0.747310$ | $+$ |
| C02 | $-2.277710$ | $-2.263489$ | $-2.209323$ | $-2.248475$ | $-2.210387$ | $-2.174758$ | - |
| C03 | 0.0000000 | 0.0000000 | 0.0000000 | 0.000000 | 0.000000 | 0.000000 | - |
| C04 | $-0.000010$ | $-0.000010$ | 0.003319 | $-0.000010$ | $-0.000010$ | $-0.000010$ | $+$ |
| C05 | $-483.610625$ | $-483.610625$ | $-483.610625$ | $-483.610625$ | $-483.610625$ | $-483.610625$ | - |
| C06 | $-578.658607$ | $-578.652619$ | $-578.645017$ | $-588.442757$ | $-588.382059$ | $-584.697207$ | $+$ |
| C07 | 0.0000000 | 0.0000000 | 0.0000000 | 0.000000 | 0.000000 | 0.000000 | - |
| C08 | 0.0000000 | 10.572854 | 10.941538 | 0.000000 | 0.000000 | 0.000000 | $+$ |
| C09 | 0.0000000 | 0.0000000 | 142.078336 | 0.000000 | 7.931077 | 29.736517 | $+$ |
| C10 | 0.0000000 | 0.0000000 | 0.0000000 | 0.000000 | 0.000000 | 0.000000 | - |
| C11 | $-0.001523$ | $-0.001523$ | $-0.001523$ | $-0.001523$ | $-0.001523$ | $-0.001523$ | - |
| C12 | $-570.089884$ | $-426.511353$ | $-0.199246$ | $-158.383888$ | $-59.906748$ | $-39.453016$ | - |
| C13 | $-68.429365$ | $-68.429365$ | $-49.678547$ | $-68.429365$ | $-65.578466$ | $-63.500458$ | $+$ |
| C14 | 0.0000000 | 0.0000000 | 10.844283 | 0.000000 | 0.000705 | 0.0658532 | - |
| C15 | 0.0000000 | 0.0000000 | 4.497445 | 0.079061 | 3.971311 | 4.180293 | - |
| C16 | 0.0000000 | 0.083187 | 0.847118 | 0.000000 | 0.000001 | 0.000002 | $+$ |
| C17 | 0.0000000 | 0.015067 | 0.603958 | 0.000000 | 0.000000 | 0.000001 | $+$ |
| C18 | 0.0000000 | 0.0000000 | 0.0000000 | 0.000000 | 0.000000 | 0.000002 | - |
| $D=30$ |  |  |  |  |  |  |  |
| C01 | $-0.821724$ | $-0.820803$ | $-0.819459$ | $-0.821884$ | $-0.821884$ | $-0.818056$ | $+$ |
| C02 | $-2.180058$ | $-2.151956$ | $-2.131994$ | $-2.247491$ | $-2.223187$ | $-2.199613$ | $+$ |
| C03 | 28.673466 | 28.673467 | 28.673767 | 0.000000 | 0.000000 | 0.000000 | $+$ |
| C04 | 0.003207 | 0.007317 | 0.029206 | $-0.000003$ | $-0.000003$ | $-0.000003$ | $+$ |
| C05 | $-453.965250$ | $-446.129938$ | $-443.650912$ | $-483.610624$ | $-483.610620$ | $-483.610542$ | $+$ |
| C06 | $-528.706201$ | $-527.747125$ | $-527.149398$ | $-590.183769$ | $-572.525932$ | $-492.219758$ | $+$ |
| C07 | 0.0000000 | 0.0000000 | 0.0000000 | 0.000000 | 0.000000 | 0.000000 | - |
| C08 | 0.0000000 | 0.0000000 | 0.0000000 | 0.000000 | 0.000000 | 0.000000 | - |
| C09 | 0.0000000 | 0.0000000 | 85.465484 | 94.993156 | 261.731772 | 516.596882 | - |
| C10 | 32.354417 | 33.129880 | 35.365672 | 0.000000 | 0.000000 | 0.000000 | $+$ |
| C11 | $-0.000337$ | $-0.000288$ | $-0.000238$ | $-0.000392$ | $-0.000392$ | $-0.000392$ | $+$ |
| C13 | $-66.724791$ | $-65.453406$ | $-64.275217$ | $-68.429365$ | $-68.429236$ | $-65.577742$ | $+$ |
| C14 | 0.0000000 | 0.0000000 | 0.0000000 | 3.169514 | 22.578798 | 28.623660 | - |
| C15 | 21.603509 | 21.603763 | 21.603913 | 0.010589 | 2.612249 | 21.603421 | $+$ |
| C16 | 0.0000000 | 0.0000000 | 0.0000000 | 0.000000 | 0.000000 | 0.000003 | - |
| C17 | 0.261621 | 3.331664 | 18.665782 | 0.000000 | 0.000000 | 0.000000 | $+$ |
| C18 | 0.805405 | 39.033089 | 825.543126 | 0.000000 | 0.000000 | 0.000071 | $+$ |

Please cite this article as: J. Sun et al., A multi-cycled sequential memetic computing approach for constrained optimisation, Information Sciences (2016), http://dx.doi.org/10.1016/j.ins.2016.01.003

![img-4.jpeg](img-4.jpeg)

Fig. 5. The convergence plots of the MCEA on C10, C14, C15 and C17. Plots (a)-(d) show the curves of the 10-D test problems; plots (e)-(h) shows the curves of the 30-D test problems.

From Table 6, it can be seen that for the 10D problems, the MCEA performs better than the $\epsilon$-DEg on 8 problems; while the $\epsilon$-DEg performs better on 4 test problems. For the rest problems, they perform similarly. For the 30D problems, the MCEA performs better than the $\epsilon$-DEg on 12 test problems, and worse on 2 test problems. We may conclude that the MCEA performs better than the $\epsilon$-DEg on average. Fig. 5 shows the convergence plots of the MCEA on $C_{10}, C_{14}, C_{15}$ and $C_{17}$, respectively.

Furthermore, we observed that the best solutions found by the MCEA are worse than those found by the $\epsilon$-DEg on $C_{09,14,15}$ at 10D, and $C_{09,14}$ at 30D. However, the worst solutions found by the MCEA are better than the $\epsilon$-DEg on $C_{09,14,15}$ at 10D. This indicates that the performance of the MCEA is more stable than that of the $\epsilon$-DEg. However, the MCEA performs worse than the $\epsilon$-DEg on $C_{09}$ and $C_{14}$ at 30D, but better on $C_{15}$.

So far, the same parameters used for the CEC'06 test problems were applied on the CEC'10 benchmarks. We suspect that the degeneration performance of the MCEA on $C_{09,14,15}$ is because that these parameters are not well configured. To justify,

Table 7
Further results on test problems $C_{09,14,15}$ at 10D and 30D. The first three columns list the results obtained by the common parameters, while the last three columns list the resuts with the optimized parameters.

| Prob. | MCEA |  |  | MCEA with optimized parameters |  |  | Hypo. |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Min | Median | Max | Min | Median | Max | Test |
| $D=10$ |  |  |  |  |  |  |  |
| C09 | 0.000000 | 7.931077 | 29.736517 | 0.000000 | 0.000000 | 4.408181 | $+$ |
| C14 | 0.000000 | 0.000705 | 0.065853 | 0.000000 | 0.000000 | 0.000036 | $+$ |
| C15 | 0.079061 | 3.971311 | 4.180293 | 0.000000 | 0.001066 | 0.073362 | $+$ |
| $D=30$ |  |  |  |  |  |  |  |
| C09 | 94.993156 | 261.731772 | 516.596882 | 0.000000 | 66.931544 | 85.609162 | $+$ |
| C14 | 3.169514 | 22.578798 | 28.623660 | 0.000000 | 0.000037 | 0.005925 | $+$ |

we run the MCEA on $C_{09,14,15}$ at 10D and 30D with different $M$ and $\alpha$ values in search of the optimal settings. We found that the optimal settings for $C_{09}$ at 30 D are $M=n$ and $\alpha=0.2$; for $C_{14}$ at 10 D and 30 D are $M=n$ and $\alpha=0.4$, for $C_{15}$ at 10D are $M=n$ and $\alpha=0.1$. The experimental results are summarised in Table 7. From Table 7, we see that with appropriate parameters, the MCEA's performances were significantly improved as suggested by the hypothesis test. Unfortunately, we cannot find a common parameter setting that is able to achieve quality performance for all benchmark problems.

# 6. Conclusion and future work 

In this paper, we presented a constrained evolutionary algorithm by combining an estimation of distribution algorithm (EDA) and a classical local optimiser under a multi-cycled sequential memetic computing (SMC) structure. Such structure regards a complete EA as an operator, and connects it with a local optimiser sequentially. It clearly decouples the EA and the local optimiser. It also enables the learning from previous cycles to improve the search efficiency of the latter evolutionary searches. In the experiments, we studied the components of the developed EDA to investigate its exploration capability, and investigated the advantages of the proposed learning strategy. The developed algorithm was extensively compared against the winning algorithms in the CEC 2006 and 2010 competition. The comparison results suggest that the proposed algorithm outperforms the compared algorithms on these benchmarks.

From the experimental study, it can be seen that the most significant components that influence the algorithmic performance under the proposed framework are the exploration capability of the EA and the learning capability. The EA should not consider much about the exploitation, but it should be designed to realise quick and broad exploration. The learning mechanism should be able to learn from history to facilitate effective search.

In the developed working algorithm, a full-factorized probability distribution model was developed, where the variable interconnections are not considered. Since the variable interactions have a significant effect on the difficulties of the optimisation problem, it can be expected that a more sophisticated probabilistic model should result in a better performance.

The guided mutation operator is used as the learning mechanism. Our analysis showed that the learning approach can be effective when the "solution path" condition holds, which may not be effective for those that do not hold. In the future, an online learning algorithm which can learn the salience of the variables will be conducted. This could make the learning more intelligent, and the learned knowledge could be more effective in guiding the evolutionary search to promising areas.

## Acknowledgment

JS was supported by the National Natural Science Foundation of China (Nos. 61273313 and 11301494), and by the Key Science and Technology Project of Wuhan under Grant no. 2014010202010108. JS and JMG were also supported by Centre for Plant Integrative Biology (CPIB), BBSRC/EPSRC and BB/D019613/1. YZ was supported by the National Natural Science Foundation of China (No. 11301494 and No. 61573326).

The authors would like to thank Prof. W. Pedrycz, and the anonymous reviewers for their constructive and helpful comments.

## References

[1] A. Aguirre, S. Rionda, C. Coello, G. Lizárraga, Use of Multiobjective Optimization Concepts to Handle Constraints in Genetic Algorithms, vol. 2723 of Lecture Notes in Computer Science, Springer, pp. 573-584.
[2] M. Ali, W. Zhu, A penalty function-based differential evolution algorithm for constrained global optimisation, Comput. Optim. Appl. 54 (2013) 707-739.
[3] D. Bertsekas, Constrained Optimization and Lagrange Multiplier Methods, Athena Scientific, Cambridge, MA, 1996.
[4] M. Bonyadi, X. Li, Z. Michalewicz, A hybrid particle swarm with a time-adaptive topology for constrained optimization, Swarm Evol. Comput. 18 (2014) $22-37$.
[5] P.A.N. Bosman, D. Thierens, Expanding from discrete to continuous estimation of distribution algorithms: the IDEA, in: M. Schoenauer, K. Deb, G. Rudolph, X. Yao, E. Lutton, J.J. Merelo, H.-P. Schwefel (Eds.), Parallel Problem Solving from Nature - PPSN VI. Lecture Notes in Computer Science 1917, 2000, pp. 767-776.
[6] J. Brest, V. Zumer, M. Maučec, Self-adaptive differential evolution algorithm in constrained real-parameter optimization, in: Proceedings of the 2006 IEEE Congress on Evolutionary Computation, Vancouver, BC, Canada, 2006, pp. 215-222.

[7] F. Caraffini, F. Neri, L. Picinali, An analysis on separability for memetic computing automatic design, Inf. Sci. 265 (2014) 1-22.
[8] X. Chen, Y.-S. Ong, M. Lim, K. Tan, A multi-facet survey on memetic computation, IEEE Trans. Evol. Comput. 15 (5) (2011) 591-607.
[9] C.-J. Chung, R. Reynolds, A testbed for solving optimization problems using culture algorithms, in: Proceedings of the Fifth Annual Conference on Evolutionary Programming, MIT Press, Cambridge, Massachusetts, 1996, pp. 225-236.
[10] R. Datta, K. Deb, Evolutionary Constrained Optimization, Springer, 2015.
[11] K. Deb, R. Datta, A fast and accurate solution of constrained optimization problems using a hybrid bi-objective and penalty function approach, in: Proceedings of the 2010 IEEE Congress on Evolutionary Computation, IEEE, Barcelona, 2010, pp. 1-8.
[12] K. Deb, A. Sinha, S. Aravind, A population-based, parent centric procedure for constrained real-parameter optimization, in: Proceedings of the 2006 IEEE Congress on Evolutionary Computation, Vancouver, BC, Canada, 2006, pp. 239-245.
[13] M. Dhadwal, S. Jung, C. Kim, Advanced particle swarm assisted genetic algorithm for constrained optimization problems, Comput. Optim. Appl. 58 (2014) $781-806$.
[14] N. Dong, Y. Wang, A memetic differential evolution algorithm based on dynamic preference for constrained optimization problems , J. Appl. Math. (2014), http://www.hindawi.com/journals/jam/2014/606019/.
[15] F. Glover, M. Laguna , Tabu Search, Kluwer Academic Publisher, Norwell, MA, 1997.
[16] J. Grabl, F. Rothlauf, PolyEDA: combining estimation of distribution algorithms and linear inequality constraints, in: Proceedings of the Genetic and Evolutionary Computation Conference, 2004, pp. 1174-1185.
[17] B. Gu, V. Sheng, K. Tay, W. Romano, S. Li, Incremental support vector learning for ordinal regression, IEEE Trans. Neural Netw. Learn. Syst. 26 (7) (2015a) 1403-1416.
[18] B. Gu, V. Sheng, Z. Wang, D. Ho, S. Osman, S. Li, Incremental learning for $v$-support vector regression, Neural Netw. 67 (2015b) 140-150.
[19] N. Hamza, R. Sarker, D. Essam, K. Deb, S. Elsayed, A constraint consensus memetic algorithm for solving constrained optimization problems, Eng. Optim. 46 (11) (2014) 1447-1464.
[20] X. He, C. Liu, H. Dong, J. Pan, Q. Yan, Particle swarm optimization-based augmented Lagrangian algorithm for constrained optimization problems, J. Softw. Eng. 8 (3) (2014) 169-183.
[21] P. Ho, K. Shimizu, Evolutionary constrained optimization using an addition of ranking method and a percentage-based tolerance value adjustment scheme, Inf. Sci. 177 (2007) 2985-3004.
[22] A. Homaifar, C. Qi, S. Lai, Constrained optimization via genetic algorithms, Simulation 62 (4) (1994) 242-253.
[23] Z. Hu, X. Cai, Z. Fan, An improved memetic algorithm using ring neighbourhood topology for constrained optimization, Soft Comput. 14 (2014) 20232041.
[24] V. Huang, A. Qin, P. Suganthan, Self-adaptive differential evolution algorithm for constrained real-parameter optimization, in: Proceedings of the 2006 IEEE Congress on Evolutionary Computation, Vancouver, BC, Canada, 2006, pp. 17-24.
[25] G. Iacca, F. Neri, E. Mininno, Y.-S. Ong, M.H. Lim, Ockham's razor in memetic computing: three stage optimal memetic exploration, Inf. Sci. 188 (2012) $17-43$.
[26] L. Jiao, L. Li, R. Shang, F. Liu, R. Stoikin, A novel selection evolutionary strategy for constrained optimization, Inf. Sci. 239 (2013) 122-141.
[27] S. Kukkonen, J. Lampinen, Constrained real-parameter optimization with generalized differential evolution, in: Proceedings of the 2006 IEEE Congress on Evolutionary Computation, Vancouver, BC, Canada, 2006, pp. 207-214.
[28] P. Larrahaga, J.A. Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation, Kluwer Academic Publishers, 2002.
[29] T.V. Le, A fuzzy evolutionary approach to constrained optimization problems, in: Proceedings of the Second IEEE Conference on Evolutionary Computation, IEEE, Perth, 1995, pp. 274-278.
[30] J. Liang, T. Runarsson, E. Mezura-Montes, M. Clerc, P. Suganthan, C. Coello, K. Deb, Problem Definitions and Evaluation Criteria for the CEC 2006 Special Session on Constrained Real-Parameter Optimization, Technical Report, Nanyang Technological University, Sigapore, 2006.
[31] J. Liang, P. Suganthan, Dynamic multi-swarm particle swarm optimizer with a novel constraint-handling mechanism, in: Proceedings of the 2006 IEEE Congress on Evolutionary Computation, Vancouver, BC, Canada, 2006, pp. 124-129.
[32] C.-H. Lin, A rough penalty genetic algorithm for constrained optimization, Inf. Sci. 241 (2013) 119-137.
[33] J.-Y. Lin, Y.-P. Chen, Analysis on the collaboration between global search and local search in memetic computation, IEEE Trans. Evol. Comput. 15 (5) (2011) 608-623.
[34] J.-Y. Lin, Y.-P. Chen, When and what kind of memetic algorithms perform well, in: Proceedings of the 2012 IEEE World Congress on Computational Intelligence, IEEE, 2012, pp. 1-8.
[35] A. Maesani, P. Fernando, D. Floreano, Artificial evolution by viability rather than competition, PLoS One 9 (1) (2014) e86831.
[36] A. Maesani, D. Floreano, Viability principles for constrained optimization using a (1+1)-CMA-ES, in: Parallel Problem Solving from Nature, 8672, 2014, pp. 272-281.
[37] A. Maesani, G. Iacca, D. Floreano, Memetic viability evolution for constrained optimization, IEEE Trans. Evol. Comput. PP (99) (2015), doi:10.1109/TEVC. 2015.2428292.
[38] R. Mallipeddi, P. Suganthan, Ensemble of constraint handling techniques, IEEE Trans. Evol. Comput. 14 (4) (2010) 561-579.
[39] R. Mallipeddi, P. Suganthan, Problem Definitions and Evaluation Criteria for the CEC 2010 Competition on Constrained Real-Parameter Optimization, Technical Report, Nanyang Technological University, Singapore, 2010.
[40] E. Mezura-Montes (Ed.), Constraint-Handling in Evolutionary Optimization: volume 198 of Studies in Computational Intelligence Series, Springer, 2009.
[41] E. Mezura-Montes, J. Velázquez-Reyes, C.C. Coello, Modified differential evolution for constrained optimization, in: Proceedings of the 2006 IEEE Congress on Evolutionary Computation, Vancouver, BC, Canada, 2006, pp. 124-12.
[42] Z. Michalewicz, C. Jankow, Handling constraints in genetic algorithms, in: K. Belew, L. Booker (Eds.), Proceedings of the Fourth International Conference on Genetic Algorithms, Morgan Kaufmann Publishers, San Mateo, California, 1991, pp. 151-157.
[43] Z. Michalewicz, M. Schoenauer, Evolutionary algorithms for constrained parameter optimization problems, Evol. Comput. 4 (1) (1996) 1-32.
[44] F. Neri, C. Cotta, Memetic algorithms and memetic computing optimization: a literature review, Swarm Evol. Comput. 2 (2012) 1-14.
[45] F. Neri, C. Cotta, P. Moscato (Eds.), Handbook of Memetic Algorithms: Studies in Computational Intelligence, Springer, 2012.
[46] Q.H. Nguyen, Y.-S. Ong, M.H. Lim, A probabilistic memetic framework, IEEE Trans. Evol. Comput. 13 (3) (2009) 604-623.
[47] S. Oh, C. Ahn, M. Jeon, Effective constraints based evolutionary algorithm for constrained optimization problems, Int. J. Innov. Comput. Inf. Control 8 (6) (2012) 3997-4014.
[48] N. Padhye, P. Mittal, K. Deb, Feasibility perserving constraint-handling strategies for real parameter evolutionary optimization, Comput. Optim. Appl. 468 (2015), doi:10.1007/s10589-015-9752-6.
[49] D. Powell, M. Skolnick, Using genetic algorithms in engineering design optimization with nonlinear constraints, in: Proceedings of the Fifth International Conference on Genetic Algorithms, Morgan Kaufmann, San Mateo, CA, 1993, pp. 424-431.
[50] M. Richey, The evolution of Markov chain Monte Carlo methods, Am. Math. Mon. 117 (5) (2010) 383-413.
[51] T. Runarsson, X. Yao, Stochastic ranking for constrained evolutionary optimization, IEEE Trans. Evol. Comput. 4 (3) (2002) 284-294.
[52] T. Runarsson, X. Yao, Search biases in constrained evolutionary optimization, IEEE Trans. Syst. Man Cybern. - Part C: Appl. Rev. 35 (2) (2005) 233-243.
[53] P. Simionescu, D. Beale, G. Dozier, Constrained optimization problem solving using estimation of distribution algorithms, in: Proceedings of 2004 Congress on Evolutionary Computation, 1, 2004, pp. 296-302.
[54] P. Spellucci, An SQP method for general nonlinear programs using only equality constrained subproblems, Math. Prog. 82 (1998) 413-448.
[55] J. Sun, J. Garibaldi, K. Kenobi, Robust Bayesian clustering for datasets with repeated measures, IEEE/ACM Tran. Comput. Biol. Bioinform. 9 (5) (2012) $1504-1514$.

Please cite this article as: J. Sun et al., A multi-cycled sequential memetic computing approach for constrained optimisation, Information Sciences (2016), http://dx.doi.org/10.1016/j.ins.2016.01.003

[56] J. Sun, J. Garibaldi, N. Krasnogor, Q. Zhang, An intelligent multi-restart memetic algorithm for box constrained global optimization, Evol. Comput. J. 21 (1) (2013) 107-147.
[57] J. Sun, A. Kaban, A fast algorithm for robust mixtures in the presence of measurement errors, IEEE Trans. Neural Netw. 21 (8) (2010) 1206-1220.
[58] J. Sun, S. Keates, Canonical correlation analysis on data with censoring and error information, IEEE Trans. Neural Netw. Learn. Syst. 24 (12) (2013) $1909-1919$.
[59] T. Takahama, S. Sakai, Constrained optimization by the $e$ constrained differential evolution with gradient-based mutation and feasible elites, in: Proceedings of the 2006 IEEE Congress on Evolutionary Computation, Vancouver, BC, Canada, 2006, pp. 308-315.
[60] M.F. Tassetiren, P. Suganthan, A multi-populated differential evolution algorithm for solving constrained optimization problems, in: Proceedings of the 2006 IEEE Congress on Evolutionary Computation, Vancouver, BC, Canada, 2006, pp. 33-40.
[61] H.-C. Tsai, Integrating the artificial bee colony and bees algorithm to face constrained optimization problems, Inf. Sci. 258 (2014) 80-93.
[62] S. Frutssai, M. Pelikan, D. Goldberg, Evolutionary algorithm using marginal histogram models in continuous domain, in: Proceedings of the 2001 Genetic and Evolutionary Computation Conference Workshop, San Francisco, CA, 2001, pp. 230-233.
[63] A. Umbarkar, M. Joshi, P. Sheth, Dual population genetic algorithm for solving constrained optimization problems, Intell. Syst. Appl. 2 (2015) 34-40.
[64] B. Wah, Y. Chen, Hybrid constrained simulated annealing and genetic algorithms for nonlinear constrained optimization, in: Proceedings of the 2001 Congress on Evolutionary Computation, 2, 2001, pp. 925-932.
[65] Q. Zhang, H. Mühlenbein, On the convergence of a class of estimation of distribution algorithms, IEEE Trans. Evol. Comput. 8 (2) (2004) 127-136.
[66] Q. Zhang, J. Sun, E. Tsang, Evolutionary algorithm with the guided mutation for the maximum clique problem, IEEE Trans. Evol. Comput. 9 (2) (2005) $192-200$.
[67] Q. Zhang, J. Sun, E. Tsang, J. Ford, Hybrid estimation of distribution algorithm for global optimisation, Eng. Comput. 21 (1) (2003) 91-107.
[68] Y. Zheng, B. Jeon, D. Xu, Q. Wu, H. Zhang, Image segmentation by generalized hierarchical fuzzy c-means algorithms, J. Intell. Fuzzy Syst. 28 (2) (2015) $961-973$.