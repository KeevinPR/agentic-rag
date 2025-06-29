# Variable Screening for Reduced Dependency Modelling in Gaussian-based Continuous Estimation of Distribution Algorithms 

Krishna Manjari Mishra, Marcus Gallagher<br>School of Information Technology and Electrical Engineering<br>The University of Queensland, Brisbane, Australia, 4072<br>Email: krishna@itee.uq.edu.au, Email: marcusg@itee.uq.edu.au


#### Abstract

Estimation of Distribution Algorithms (EDAs) focus on explicitly modelling dependencies between solution variables. A Gaussian distribution over continuous variables is commonly used, with several different covariance matrix structures ranging from diagonal i.e. Univariate Marginal Distribution Algorithm (UMDA ${ }_{c}$ ) to full i.e. Estimation of Multivariate Normal density Algorithm (EMNA). A diagonal covariance model is simple but is unable to directly represent covariances between problem variables. On the other hand, a full covariance model requires estimation of (more) parameters from the selected population. In practice, numerical issues can arise with this estimation problem. In addition, the performance of the model has been shown to be sometimes undesirable. In this paper, a modified Gaussian-based continuous EDA is proposed, called sEDA, that provides a mechanism to control the amount of covariance parameters estimated within the Gaussian model. To achieve this, a simple variable screening technique from experimental design is adapted and combined with an idea inspired by the Pareto-front in multi-objective optimization. Compared to $\mathrm{EMNA}_{\text {global }}$, the algorithm provides improved numerical stability and can use a smaller selected population. Experimental results are presented to evaluate and compare the performance of the algorithm to $\mathrm{UMDA}_{c}$ and $\mathrm{EMNA}_{\text {global }}$.


## Index Terms

Estimation of Distribution algorithms, Optimization problems, Screening Technique.

## I. Introduction

EDAs are a recent development in the field of evolutionary algorithms [1], [2]. In EDAs a population is approximated with a probability distribution and new candidate solutions are obtained by sampling from this distribution. The aim is to avoid the use of arbitrary operators (such as mutation and crossover) in favor of
explicitly modelling and exploiting the distribution of promising individuals. The model fitting task within each iteration of an EDA is typically carried out by a maximum likelihood estimation procedure. EDAs have been developed for both discrete and continuous problems. Reviews of EDAs can be found in [1], [3], [4]. This paper focuses on continuous EDAs. Most optimization algorithms make some explicit or implicit assumption about the nature of the objective function. In EDAs the interrelations are explicitly expressed through the joint probability distribution associated with the individuals selected at each iteration.

EDAs focus on explicitly modelling dependencies between solution variables. A Gaussian distribution over the variables is commonly used, with several different covariance matrix structures ranging from diagonal $\left(\mathrm{UMDA}_{c}\right)$ to full (EMNA). A diagonal covariance model is simple but is unable to directly represent covariances between problem variables. On the other hand, a full covariance model requires estimation of (more) parameters from the selected population.

There are specific examples where EDAs do not perform well [5] [6] and some numerical issues associated with their implementation can occur [7]. In this paper, a new continuous Gaussian-based EDA, called sEDA, is proposed that introduces a notion of variable importance by adapting a screening technique from experimental design. The algorithm also improves on numerical stability in EDAs by allowing the level of dependency modelling to be controlled.
The remainder of the paper is organized as follows. Section 2 provides an overview of existing continuous Gaussian-based EDAs and reviews issues around the covariance dependency modelling in these algorithms. In Section 3, a modification to the algorithm is proposed, the Screening EDA (sEDA). The implementation of the sEDA and parameter values is described in detail. In Section 4 experimental results are presented evaluating the sEDA and comparing it with $\mathrm{UMDA}_{c}$ and $\mathrm{EMNA}_{\text {global }}$. Section 5 provides a conclusion and summary of the paper.

## 2. Analyzing the existing continuous Gaussian based EDAs based on the interaction of variables.

The continuous (global) optimization problem is to find $\mathbf{x}^{*}$ such that

$$
f\left(\mathbf{x}^{*}\right) \leq f(\mathbf{x}), \forall \mathbf{x} \epsilon S
$$

where $S \subseteq R^{n}$ is the set of feasible solutions, $f(\mathbf{x})$ is the fitness or objective function and $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)$ is an individual or candidate solution vector.

Table 1. General EDA Algorithm.

```
BEGIN (set \(t=0\) )
Generate initial population (uniformly in \(S\) )
REPEAT until stopping criterion is met
    Evaluate \(f\left(\mathbf{x}^{i}\right)\) for each individual \(\mathbf{x}^{i}\) in population
    Selection
    Build probabilistic model \(p_{t}(\mathbf{x})\) based on selected individuals
    Generate new population by sampling from \(p_{t}(\mathbf{x})\)
    \(t=t+1\)
ENDREPEAT
END
```

EDAs are one class of metaheuristics that have been developed to solve optimization problems. The general pseudo-code framework for an EDA is shown in Table 1. In EDAs, the initial population is generated randomly in the search space. Selection is typically done via the truncation method. A probability density estimator is then used to model the promising regions of the search space through maximum likelihood estimates which is subsequently used for generating the candidate solutions for the next generation. The family and structure of the model used in an EDA is typically fixed (e.g. a set of Bernoulli distributions to generate the bit strings in the PBIL algorithm [8], or a factorized Gaussian distribution over a continuous search space in the $\mathrm{UMDA}_{\mathrm{c}}$ algorithm [1]).

A number of different types of density estimation models have been used in EDAs for both discrete and continuous search spaces. In the continuous domain, the Gaussian distribution is the most widely used model [1], [9], [10]. Other models considered include semi-parametric, e.g. mixture models [11] and non-parametric, e.g. histograms and kernel density estimators [12]-[15]. In this paper, we focus on Gaussian EDA models although the contributions are likely to be extendable to other models. A Gaussian distribution over the variables is commonly used, with several different covariance matrix structures ranging from diagonal (e.g. in the $\mathrm{UMDA}_{\mathrm{c}}$ ) to full (e.g. EMNA).

The continuous Univariate Marginal Distribution Algorithm $\left(\mathrm{UMDA}_{\mathrm{c}}\right)$ was introduced by Larrañaga et al. [16]. A factorized Gaussian model (i.e. a diagonal covariance matrix) is used which assumes all the variables are independent to each other. The model parameters are estimated by using maximum likelihood. This algorithm
is easy to apply and computationally efficient. But the model may have difficulty in solving problems where the variables have strong dependencies.

To address this limitation, multivariate Gaussian models have been proposed. Estimation of Multivariate Normal Algorithm ( $\mathrm{EMNA}_{\text {global }}$ ) is an example, where dependencies between all pairs of variables are modelled. In $\mathrm{EMNA}_{\text {global }}$, the mean and covariance matrix are also computed via maximum likelihood [1]. The computational cost is higher than $\mathrm{UMDA}_{\mathrm{c}}$.

In practice, numerical issues can arise with the EDA model estimation problem [7]. The covariance matrix, which is estimated by using maximum likelihood in $\mathrm{EMNA}_{\text {global }}$ is positive semi-definite by its definition. But in practice this is not guaranteed because of finite precision computation. There will be computation error or numerical issues arising when the sample used to estimate the model does not adequately span all dimensions of the search space, which is especially likely when the sample size is relatively small compared to the problem dimensionality. Various methods and techniques (e.g. eigen-value tuning strategies) have been proposed in [7], [9] in order to avoid the ill-posed condition of the covariance matrix. Eigen-decomposition EDA (EDEDA) described in [9] is one of the techniques to repair the ill-posed covariance matrix. The experimental results in [7], [9] show that the values from different covariance repairing methods avoid the numerical difficulties and give good results with respect to best solution found as well as using less number of sample size as compared to classical EDAs.

The performance of EDA model has also been shown to be sometimes undesirable [5], [6]. In some landscapes, EDAs do not perform very well due to the premature shrinking of the variance at an exponential rate. Eg., in slope like regions of the search space, described in [6] and in elliptical surface which is described in [5], premature convergence is likely to occur. In these cases, the direction of descent is much more important than selected solutions. Different techniques have been introduced in [5], [6] e.g. Adaptive Variance Scaling (AVS), Anticipated Mean Shift (AMS), Covariance Matrix Adaptation(CMA) etc. to overcome this issue.

In this paper, a modified Gaussian-based continuous EDA is proposed, called sEDA, that provides a mechanism to control the amount of covariance parameters estimated within the Gaussian model. To achieve this, a simple variable screening technique from experimental design is adapted and combined with an idea inspired by the Pareto-front in multi-objective optimization. Compared to $\mathrm{EMNA}_{\text {global }}$, the algorithm provides improved numerical stability and can use a smaller selected population. Experimental results are presented to evaluate and compare the performance of the algorithm to $\mathrm{UMDA}_{\mathrm{c}}$ and $\mathrm{EMNA}_{\text {global }}$.

## 3. Variable Screening in an EDA

In this Section we introduce a Screening EDA (sEDA). The main idea of the algorithm is to allow a degree of dependency modelling as a trade-off between the $\mathrm{UMDA}_{\mathrm{e}}$ model (no covariance) and the $\mathrm{EMNA}_{\text {global }}$ model (full covariance matrix), to try and capture the advantages and limit the potential problems of both approaches. Hence, the sEDA uses a multivariate Gaussian model where the covariance matrix contains some degree of "sparseness". On each generation, some variables are selected to be modelled using covariance terms between them while others are fixed at $\sigma_{i j}=0$. The immediate question is to determine a way of selecting which variables to model covariance between.

### 3.1. Measuring the Strength or Importance of Dependencies Between the Variables Using Elementary Effects

A number of techniques for identifying variable interactions and importance have been developed and applied in the field of experimental design and particularly in the model-based engineering design. A simple technique proposed by Morris in 1991 [17] is based on measuring the mean and standard deviation of perturbations of individual variables for a given problem, calculated via so-called elementary effects terms.

The elementary effect for the $i$ th variable, $E_{i}(\mathbf{x})$, is defined as follows. Let $\Delta$ be a pre-determined amount to perturb each variable. For a given $\mathbf{x}$
$E_{i}(\mathbf{x})=\frac{f\left(x_{1}, x_{2}, \ldots, x_{i-1}, x_{i}+\Delta, x_{i+1}, \ldots, x_{n}\right)-f(\mathbf{x})}{\Delta}$
where $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is a given starting or "baseline" vector in the solution space. The perturbations, $\Delta$ are by default determined according to a full factorial sampling grid of some fixed resolution or increment size. In other words, for each variable $x_{i}$, over some fixed range and increment size, the value of $x_{i}$ is changed and $f$ is recalculated, producing a sample or set of values of $E_{i}(\mathbf{x})$.

Given a set of elementary effect values, the mean, $\bar{E}_{i}(\mathbf{x})$, and standard deviation, $\operatorname{std}\left(E_{i}(\mathbf{x})\right)$ over the sample can be calculated. A high value of $\bar{E}_{i}(\mathbf{x})$ then indicates a variable that has a large average influence on the value of $f$. A high value of $\operatorname{std}\left(E_{i}(\mathbf{x})\right)$ indicates that variable $x_{i}$ has a fluctuating influence on the value of $f$, which may indicate that it is involved in interactions with other variables [18]. Either or both may be important. In engineering design, these values are typically examined manually to inform decisions, e.g. about which variables to include in a model [19].

### 3.2. Incorporating Variable Screening in an EDA

To incorporate elementary effect values into an EDA, two main decisions must be made. The first is how to
calculate the $E_{i}(\mathbf{x})$ values themselves, which will happen on each generation of the sEDA. Using a sampling plan such as a full factorial design requires the specification of a grid of some predetermined resolution, perturbing each $\mathbf{x}^{i}$ along vertices in the grid and evaluating $f$ at these points. We propose a simpler alternative here using only the selected population. Specifically, the mean of the selected population is calculated for each dimension $x_{i}$. The population, $P_{b d}$ is then formed by creating new solution vectors where the mean value is substituted in turn for each problem variable (e.g. $\mathbf{x}^{\mathbf{i}}=x_{i}, \ldots, x_{i-1}, m_{i}, x_{i+1}, \ldots, x_{n}$ ). This produces $n M_{s e l}$ new solutions, which are evaluated using $f$.

Given the elementary effect values and their sample mean and standard deviation, the second decision to be made is how to use them to determine covariance matrix structure to be used in the sEDA model. To do this, we utilize the concepts of dominance and Pareto optimality from multi-objective optimization (see, e.g. chapter 9 of [20]). We consider the mean and standard deviation of elementary effects as two different (aka decision-making) criteria. One solution is said to dominate the other if its score is at least as high for all objectives, and is strictly better for at least one. Let $\mathbf{x}^{a}$ and $\mathbf{x}^{b}$ have $n$ objectives as a $n$-dimensional vector $\mathbf{a}$. Using the $\succeq$ symbol to indicate domination, $A \succeq B$ is defined as:

$$
\begin{gathered}
\mathbf{x}^{a} \succeq \mathbf{x}^{b} \Leftrightarrow \forall i \in\{1, \ldots, n\} a_{i} \geq b_{i} \\
\text { and } \exists i \in\{1, \ldots, n\}, a_{i}>b_{i}
\end{gathered}
$$

All non-dominated solutions possess the attribute that their quality cannot be increased with respect to any of the objective functions without detrimentally affecting one of the others. In the presence of constraints, such solutions usually lie on the edge of the feasible regions of the search space. The set of all non-dominated solutions is called the Pareto set or the Pareto front.

In the sEDA, a fixed fraction $\eta$ of the variables need to be selected for covariance modelling. Variables that belong to the Pareto set are selected first. If more variables are required, then those which have the minimum (Euclidean) distance to the Pareto front are selected. On the other hand, if the number of variables on the Pareto front is greater than required, then a random subset of these variables is selected.

The complete sEDA algorithm is summarized in Table 2. The critical steps of the algorithm are as described above. Three algorithm parameters must be specified for implementation: the population size $M$, the selection parameter $\tau$ and the variable screening/selection parameter $\eta$. sEDA uses truncation selection: a fraction $\tau$ of the population with the best objective function values are retained for building/adapting the search model. ${ }^{1}$. The mean $m$ of the selected population is then calculated for

1. Rounding if $M \cdot \tau$ is not an integer.

expanding the population. This expanded population is then used to calculate elementary effects values and their mean $(\bar{E}(\mathbf{x}))$ and standard deviation $\operatorname{std}(E(\mathbf{x}))$ values. After selecting variables with respect to the Pareto set of the mean and standard deviation of $E$, the covariance matrix for the EDA model is formed as a sparse matrix, with non-zero covariance terms for selected variables. This is used in combination with the EDA mean vector (estimated from the selected expanded population) and the model is then used to generate the new population as in a standard EDA. The process is repeated until some stopping criterion is met.

## Table 2. sEDA Algorithm.

```
Given: Population size \(M\), dimension size \(n\), selection parameter \(\tau\),
    model selection parameter \(\eta\), and \(B=\operatorname{Round}(n \cdot \eta)\),
    where \(B\) is the number of best variables.
BEGIN (set \(t=0\) )
Initialize population \(P\) by generating \(M\) individuals uniformly in \(S\)
REPEAT FOR \(t=1,2, \ldots\) UNTIL stopping criterion is met
Evaluate \(f\) for population \(P\).
Selection: \(M_{\text {sel }}=\operatorname{Round}(M \cdot \tau)\) individuals from \(P\).
Let selected population \(=P_{\text {sel }}\).
Calculate sample mean \(\tilde{m}\) of \(P_{\text {sel }}\).
Calculate \(P_{\text {tot }}\) by expanding \(P_{\text {sel }}\), successively replacing variable
\(1, \ldots, n\) with \(m_{i}\)
Evaluate \(f\) for new individuals in \(P_{\text {tot }}\) population.
Selection: \(M_{\text {tot }}^{\text {sel }}=\operatorname{Round}\left(n \cdot M_{\text {sel }} \cdot \tau\right)\) individuals from \(P_{\text {tot }}\).
Let new selected population be \(P_{\text {tot }}^{\text {sel }}\).
Calculate Elementary Effect \(E\) of the fitness function of \(P_{\text {tot }}^{\text {sel }}\).
Calculate the mean \(\mu\) of the \(P_{\text {tot }}^{\text {sel }}\).
Calculate standard deviation \(\operatorname{std}(E)\) and mean \(\bar{E}\)
Determine the Pareto optimal solutions \(p_{o}\) using \(\operatorname{std}(E)\) and \(\bar{E}\)
as two objective function.
If \(p_{o}>B\), randomly choose \(B\) solutions from \(p_{o}\).
If \(p_{o}<B\), select/add \(B-p_{o}\) solutions nearest to the Pareto front
When \(p_{o}==B\), then
Build \(\Sigma_{t}\) using covariance terms for the \(B\) selected variables
Build \(\Sigma_{t}\) using variance terms for the \(n-B\) variables
\(\theta=\operatorname{cov}(\eta)+\operatorname{var}(100-\eta)\).
\(p(\mathbf{x}) \leftarrow(\theta, \mu)\)
Generate \(P\) new population by sampling from \(p(\mathbf{x})\).
ENDREPEAT
END
```


## 4. Experiments

### 4.1. Selection Parameter Settings for sEDA

sEDA contains two selection parameters, $\tau$ and $\eta$, which is described above. Setting these values is important for experimental results. In this set of experiment, different combinations tried for $\tau$ and $\eta$ are $((0.3,0.3)$, $(0.3,0.5),(0.5,0.3),(0.5,0.5))$. With these values, sEDA is tested using 6 different 10-D benchmarking functions, which are the first 6 functions from the Real-Parameter

Black-Box Optimization Benchmarking (BBOB) experiment set [21]. sEDA is implemented with population size of 500 and 300000 function evaluations. The algorithm is terminated when difference between the best fitness value found and the global optimum is less than or equal to $1 \mathrm{e}-08$ or the algorithm attains the maximum allowed number of function evaluations.

Table 3 lists mean and standard deviation of the best fitness values found over 30 runs for different combination of $\tau$ and $\eta$. Best results with minimal mean value are represented in bold font. It is discovered from Table 3 that, out of 6 functions, 5 functions are better when $\tau=0.3$ and $\eta=0.3$.

In order to check the behavior between different combination, a two-tailed $t$ test of the null hypothesis has been used (assumed unequal variances). Test has been done between the best fitness values found by $(0.3,0.3)$ combination with 3 other different combination for each function.

From the set of experiments on different combinations and doing $t$ test, we come to the conclusion in the following way. The best result obtained is not statistically significant for $(0.3,0.3)$ and $(0.3,0.5)$ combination, where as in most of the cases, the result of $(0.3,0.3)$ combination has statistically significant difference for $(0.5,0.5)$ combination. Except function F6, values of other functions show no statistical difference for $(0.3,0.3)$ and $(0.5,0.3)$ combination. Although, the $t$ test does not clearly give any idea about the better combination, given the results presented, based on best results with minimum mean value (even the results have very little difference), we set the value of $\tau$ and $\eta$ as 0.3 and 0.3 respectively for sEDA in the remainder of the paper.

### 4.2. Evaluation of sEDA and Comparisons

In the following experiments, we are considering 2 sets of problems. One is a set of commonly used artificial test functions (Sphere, Griewangk, Ackleys, Rosenbrock, Schwefel) which is described in Table 4. Here all are minimization problems. The second set of problem is Circle in a square (CiaS) packing problems, which is an example of real world problem.

The objective of the CiaS problem is to maximize the common radius of $n_{c}$ non-overlapping circles contained in the unit square. Let $C\left(z^{i}, r\right)$ be the circle with center $z^{i}$ and radius $r$, where $z^{i}=\left(x_{i}, y_{i}\right) \in \mathbb{R}^{2}$, then the problem can be formalized as follows:

$$
\begin{gathered}
r_{n}=\max r \\
C\left(z^{i}, r\right) \subseteq D \quad i=1, \ldots, n_{c} \\
C^{i n t}\left(z^{i}, r\right) \cap C^{i n t}\left(z^{j}, r\right)=\Phi ; \forall i \neq j
\end{gathered}
$$

where $C^{i n t}$ denotes the interior of a circle [22] [23].
Experiments are conducted on 10-D and 50-D versions of the artificial test functions. For the (CiaS) problems

Table 3. Solution quality comparison having different values of $\tau$ and $\eta$ with 6 different function from BBCB. Bold font represents the best result.

* sign, the value of $t$ test ( 2 tailed) $<0.05$, indicates statistically significant difference when compared with results of $(0.3,0.3)$.
- sign, the value of $t$ test ( 2 tailed $)>0.05$, indicates no statistically significant difference when compared with results of $(0.3,0.3)$.
$(n)$, when the results are same.

Table 4. Test functions used in the experiments
experiments are conducted on the number of circles, which is ranging from $2, \ldots, 20$.

The initial population for all the algorithms are generated using same random generation procedure based on a uniform distribution. For 10-D and 50-D functions, the parameters for $\mathrm{UMDA}_{c}$ and $\mathrm{EMNA}_{\text {global }}$ are taken from chapter 8 of [1] i.e, the selection parameter is set to 0.5 and population size is 2000 . For 10-D and 50-D functions, 500 and 1000 population are used respectively by sEDA. Comparing 10-D functions, we set

301850 function evaluations. But when it comes to 50-D functions, 10 times more function evaluations are used. Algorithms are terminated when the difference between the absolute value of the best fitness found and the known global optimum is less than or equal to 1e-08 or it exceeds the given number of function evaluations. For each single test, the result is averaged over 100 independent runs.

For circles in a square problems the results for $\mathrm{UMDA}_{c}$ are taken from [22]. For $\mathrm{EMNA}_{\text {global }}$, the population size $=1000$ and the selection parameter as 0.5 . are taken. For sEDA, the value of $\tau$ and $\eta$ are 0.3 and 0.3 respectively, with the population size equals to 50 times the dimension of the problem, where dimension is defined as $2^{*}$ number of circles in a problem. The number of function evaluations considered is 2000000 . Algorithms are terminated when the difference between the absolute value of best fitness value and the known global optimum is less than equal to 1e-06 or it exceeds the given number of function evaluation. For each test, the result is averaged over 30 independent runs.

The number of function evaluations in each generation are different for different algorithms. In $\mathrm{UMDA}_{c}$ and $\mathrm{EMNA}_{\text {global }}$ the number of function evaluations at each generation is equals to the total number of population considered, where as in sEDA the number of function evaluations in each generation is a function of population size, selection parameter and dimension of the problem. The number of function evaluations at each generation for sEDA is $M+(M * \tau * n)$, where $M$ is the population size, $n$ is the dimensionality of the problem and $\tau$ is the standard truncation ratio.

### 4.3. Results

Table 5 and Table 6 summarizes the results on 10D and 50-D functions using $\mathrm{UMDA}_{c}, \mathrm{EMNA}_{\text {global }}$ and sEDA algorithms. Best fitness value found and the number of evaluations required to reach the final solution is recorded for each of the experiments. The best result with the minimum mean value with respect to fitness as well as number of function evaluations is highlighted in bold font. A $t$-test has been done between best values found by sEDA and 2 other EDAs, (with null hypothesis being that each set of experimental results is drawn from distributions with equal mean (and assumed unequal variances)).
4.3.1. Discussion for 10-D and 50-D functions. Tables 5 and 6 show the comparison of the 3 algorithms using 6 different functions.

Sphere function : In Sphere function, all the variables are independent to each other and equally important to the problem. Although it always facilitates univariate model based EDAs in solving the problems but Tables 5 and 6 show that, the performance of sEDA and $\mathrm{UMDA}_{c}$ is similar in both 10-D and 50-D dimension. But the

performance of $\mathrm{EMNA}_{\text {global }}$ is significantly degraded. For 10-D Sphere, sEDA requires less number of function evaluations where as requirement of function evaluations are more when dimension increases as compared to 2 other EDAs.

Griewangik function : This is a multimodal and nonseparable function. For 10-D version, sEDA is significantly better than UMDA ${ }_{c}$ and $\mathrm{EMNA}_{\text {global }}$ in terms of best fitness values found as well as number of function evaluations. For 50-D, although the performance of sEDA is better, in terms of minimum mean value of the best fitness but found no significant difference as compared to 2 other algorithms. sEDA requires significantly more number of function evaluations than other 2 EDAs. If sEDA capture the right percent of variables while modelling, then it may outperform other two algorithms significantly in high dimension also.

Ackely function : Ackely has several local minima, hence can be difficult to optimize. The performance of sEDA compared to UMDA ${ }_{c}$ and $\mathrm{EMNA}_{\text {global }}$ is better in terms of minimum average best fitness values but shows no statistically significant difference for both 10-D and 50-D version of the function. But we can conclude that sEDA is better in 10-D because it requires less number of function evaluations as compared to other 2 algorithms. For 50-D Ackely, sEDA requires significantly more number of function evaluations.

Rosenbrock function : Rosenbrock function, is a unimodal but very hard problem. Although sEDA does not attain global optimum, but it outperforms UMDA ${ }_{c}$ and $\mathrm{EMNA}_{\text {global }}$ with significantly better solutions. These 3 algorithms use same number of function evaluations to achieve best fitness values.

Rastrigin function : Rastrigin function which is a multimodal and separable problem shows that the performance of sEDA is degraded significantly as compared to UMDA ${ }_{c}$ and $\mathrm{EMNA}_{\text {global }}$. For 10-D version of the function, $\mathrm{EMNA}_{\text {global }}$ performs better (since adequate population is supplied), while for 50-D version UMDA ${ }_{c}$ performs better (due to separable nature of the problem), but in both the cases sEDA doesn't show its performance very efficiently.

Schwefel function : For 10-D and 50-D Schwefel function, the performance of $\mathrm{EMNA}_{\text {global }}$ surpasses sEDA and UMDA ${ }_{c}$. We can increase the performance of sEDA by modifying the value of $\eta$, since we know clearly from the definition of Schwefel function described in Table 4, that all the variables have interaction with each other. Further discussion is in sub-section 4.4.

### 4.3.2. Results for Circle in a Square (CiaS) Problems.

[22] discussed about the performance of UMDA ${ }_{c}$ and Nelder-Mead simplex algorithm in CiaS problems. Here we compare UMDA ${ }_{c}, \mathrm{EMNA}_{\text {global }}$ and sEDA with number of circles ranging from $2 \ldots 20$, over a fixed number of function evaluations.

Figure 1 shows the performance of UMDA ${ }_{c}$,

Table 5. Solution quality comparison for 10-D problem. Bold font represents the best result.

U stands for UMDA ${ }_{c}$, E stands for $\mathrm{EMNA}_{\text {global }}$, s stands for sEDA. + sign, the value of $t$ test ( 2 tailed) $<0.05$, indicates statistically significant difference when compared with results of sEDA.
- sign, the value of $t$ test ( 2 tailed) $>0.05$, indicates no statistically significant difference when compared with results of sEDA.
( $n$ ), when the results are same.

Table 6. Solution quality comparison for 50-D problem. Bold font represents the best result.

U stands for UMDA ${ }_{c}$, E stands for $\mathrm{EMNA}_{\text {global }}$, s stands for sEDA. + sign, the value of $t$ test ( 2 tailed) $<0.05$, indicates statistically significant difference when compared with results of sEDA.
- sign, the value of $t$ test ( 2 tailed) $>0.05$, indicates no statistically significant difference when compared with results of sEDA.
$(n)$, when the results are same.

$\mathrm{EMNA}_{\text {global }}$ and sEDA on the CiaS problems. The xaxis denotes the problem size $\left(n_{c}\right)$ while the y -axis is a performance ratio given by $d_{n} / f\left(x_{n}\right)$, where $d_{n}$ is the known global optimum and $f\left(x_{n}\right)$ is the solution found by the algorithm. Figure 1 shows that the performance of UMDA ${ }_{c}$ is worst than $\mathrm{EMNA}_{\text {global }}$ and sEDA. But when sEDA is compared with $\mathrm{EMNA}_{\text {global }}$, we found out that up to $n_{c}=4$, the performance is some how

![img-0.jpeg](img-0.jpeg)

Figure 1. Median Performance of UMDA ${ }_{c}$, EMNA $_{\text {global }}$ and sEDA on CiaS problem.
similar but when $n_{c}$ increases, the performance of sEDA also increases.

The nature of variables in the CiaS problems is that some variables are equally important and some are dependent on each other. Here, out of the total number of variables only 30 percent of variables are selected for modelling covariance matrix by sEDA. By analysing the results, we can conclude that sEDA captures the importance and dependency of variables in this problem very efficiently.

### 4.4. Examination of sEDA Behaviour

From a stability point of view, sEDA is much more stable than EMNA $_{\text {global }}$. In most of the cases where population size is less, $\mathrm{EMNA}_{\text {global }}$ produces an illconditioned matrix [7] [9] which is a hindrance for obtaining any global solution. Although sEDA uses some characteristics of EMNA $_{\text {global }}$, it doest not produce any ill conditioned matrix.

To repair the ill posed covariance matrix a number of techniques has been found out and implemented which is clearly described in [7], [9]. A comparison table is discussed in [9] which shows different covariance matrix repairing methods. The methods include CMR, ECMR and ECMR0 which is implemented on different artificial test functions. The explanations of algorithms and parameter details are mentioned in [9].

Here we compare sEDA algorithm with the 3 algorithms discussed in [9] using Rosenbrock, Sumcan and $f 9$ functions (described in Table 4). Except Sumcan, other 2 functions are minimization function. sEDA uses same population size and number of function evaluations as described in [9] with $\tau=0.3$ and $\eta=0.3$ as selection ratios. The compare values shown in Table 7 summarizes the average performance of 100 independent runs of each algorithm. Table 7 as well as discussion from [9] revealed that CMR, ECMR and ECMR0 have approximately identical performance. From Table 7, we can conclude that, except Sumcan function, the performance of sEDA is better than other 3 algorithms in terms of the
best fitness values, but sEDA requires more number of function evaluation in each case.

Table 7. Comparision of sEDA, CMR, ECMR and ECMR0. Bold font represents the best result.

As discussed in Section 3, the value of $\eta$ in sEDA determines the number of variables to be selected for covariance modelling.

Hence the value of $\eta$ depends on the problem to be solved and some experimentation is expected to be required to find the optimal value in any given application. he definition in Table 4 for Schwefel function shows that, all the variables are dependent on each other. We can see from Table 5 and 6 that EMNA $_{\text {global }}$ performs very well in Schwefel function. Table 8 shows the comparison

Table 8. Role of $\eta$, in 10-D Schwefel function. Bold font represents the best result.

between EMNA $_{\text {global }}$ and sEDA when $\eta=1$ in a 10-D Schwefel function. The performance of sEDA is better when compared to EMNA $_{\text {global }}$ with respect to the best fitness values as well as function evaluations required to achieve the solution. In other sense we can conclude that the role of $\eta$ is significant if we can know the nature of variables in a problem.

## 5. Conclusion

This paper analysed classical EDAs over continuous variables in terms of dependency of variables and modelling and presented numerical issues as well as common difficulties w.r.t. performance of the model. Using different techniques and theoretical analysis, we have proposed a Gaussian based continuous EDA, called sEDA, a mechanism to control the amount of covariance parameters estimated within the Gaussian model, which clearly gives an idea about the number of dependent variables and important of these variables in a problem. A simple

implementation of this framework, sEDA, has been experimentally compared with $\mathrm{UMDA}_{c}$ and $\mathrm{EMNA}_{\text {global }}$. While considering artificial test functions and real world problems (CiaS problem), sEDA showed significantly better performance in most of the cases. Most of the results are better primarily due to better selection of variables for covariance modelling. The role of $\eta$ is significant if we can know the nature of variables in a problem. The main advantage of sEDA is not only finding a good solution with less number of population, but also gives an idea of variable dependency and importance of the problem. Moreover, it doesn't show ill posed covariance matrix while modelling.
