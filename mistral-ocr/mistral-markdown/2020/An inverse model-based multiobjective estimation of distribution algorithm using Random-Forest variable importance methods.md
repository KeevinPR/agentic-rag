# An inverse model-based multiobjective estimation of distribution algorithm using Random-Forest variable importance methods 

Pezhman Gholamnezhad | Ali Broumandnia (1) Vahid Seydi

Department of Computer, South Tehran Branch, Islamic Azad University, Tehran, Iran

## Correspondence

Ali Broumandnia,Department of Computer, South Tehran Branch, Islamic Azad University, Ahang St, Blv South-Nabard, Tehran, Iran
Email: broumandnia@gmail.com


#### Abstract

Most existing methods of multiobjective estimation of distributed algorithms apply the estimation of distribution of the Pareto-solution on the decision space during the search and little work has proposed on making a regression-model for representing the final solution set. Some inverse-model-based approaches were reported, such as inversed-model of multiobjective evolutionary algorithm (IM-MOEA), where an inverse functional mapping from Pareto-Front to Pareto-solution is constructed on nondominated solutions based on Gaussian process and random grouping technique. But some of the effective inverse models, during this process, may be removed. This paper proposes an inversed-model based on random forest framework. The main idea is to apply the process of random forest variable importance that determines some of the best assignment of decision variables $\left(x_{n}\right)$ to objective functions $\left(f_{m}\right)$ for constructing Gaussian process in inversed-models that map all nondominated solutions from the objective space to the decision space. In this work, three approaches have been used: classical permutation, Naïve testing approach, and novel permutation variable importance. The proposed algorithm has been tested on the benchmark test suite for evolutionary algorithms [modified Deb K, Thiele L, Laumanns M, Zitzler E (DTLZ)

and Walking Fish Group (WFG)] and indicates that the proposed method is a competitive and promising approach.

KEYWORDS
estimation of distribution algorithm, Gaussian process, inverse modeling, multiobjective optimization, random forest variable importance

# 1 | INTRODUCTION 

## 1.1 | Background

Random forests are a general tool for classification with high dimensional data and apply for ranking candidate predictors based on variable importance measure. They provide two simple methods for feature selection: mean decrease impurity (MDI) and mean decrease accuracy. Also there are two importance measure for ranking predictor variables: the Gini importance and the permutation importance. In Gini importance, with removing any association between the response and a predictor variable, the prediction accuracy is changed and large change illustrates that the predictor variable is important. But there is no natural cut off that can be discriminated important and nonimportant variables. For this purpose, some methods were proposed that are permutation-based and need the repeated computation of forests. That's it for high-dimensional setting typically containing thousands of candidate predictor, which have a very high computing time. Also, the predictor variables contains variables that do not have their "own" effect on the response, but are related with the response due to their relationship with truly influential predictor variables. Regarding the values variable importance, the negative values or values of zero, illustrate that variable does not improve the trees' predictive strength, because the error rates are similar or even larger when applying unchanged version of the variable. In contrast, a positive value for the variable importance, express that the variable at least some improves the trees' predictive strength, because the error rates are smaller when applying the original version of the variable for deriving tree predictions. However it cannot be deduced that a positive value for the variable importance demonstrates a relative value. A new computationally fast heuristic procedure of a variable importance test is applied that is suitable for high dimensional data where many variables do not carry any information. This approach is based on a modified version of permutation variable importance measure which is taken from cross-validation procedure. ${ }^{1}$

The performances of multiobjective evolutionary algorithms (MOEAs) depend partly on the genetic operator or selection strategy. ${ }^{2,3}$ For this purpose, estimation of distribution algorithms (EDAs) was developed to solve optimization problems. ${ }^{4-6}$ The basic idea of EDAs is making a stochastic model from the parental distribution in the decision-maker and to produce offspring individuals by sampling from the model. Instead of genetic operators, these algorithms produce new candidate solutions from a probabilistic model, which is learnt from a set of promising solutions.

Typically the EDA-based MOEA, based on their estimation models, are divided in to two groups: The first group is the Bayesian network-based EDAs and the second group is often known as the mixture probability model-based EDAs. The main difference between EDAs and most arbitrary evolutionary algorithms is that in evolutionary algorithms new candidate solutions are produced using an implicit distribution, defined by one or more variation operators, whereas EDAs use explicit probability distribution encoded by a Bayesian network, a multivariate normal distribution, or another model class. Most multiobjective EDAs, concentrate on the estimation distribution of the PS in the decision space in search and represent the final Pareto optimal solutions, in template of the set, such as an archive. But they still had some challenge such as time consuming, and have strict requirement of the training data, and with increase of dimensionality the decision variable, the performance sharply is decreased. Hence In recent years, the surrogate-assisted evolutionary algorithms (SAEAs) have been applied in order to solve the multiobjective EDAs. ${ }^{7}$ The surrogate model is used when evaluating of fitness is computationally and cannot be easily measured and it is necessary simulation to evaluate. But they still had some challenges such as the choice of surrogate model, Problem of increasing dimension in decision variables and it is impossible to determine what should be predicted by the surrogate. But little work has been reported on making a regression model for showing the final solution set. Some primary work has reported where piecewise linear models were made to represent the solution set attained by an MOEA, leading the improve quality of the solutions. ${ }^{8}$ Most recently, an inverse functional mapping from Parento-Front (PF) to Pareto-solution (PS) was made based on the approximate PS generated by MOEAs at the end of evolutionary optimization. ${ }^{9,10}$ In this method, the inverse model is not used during the optimization. Also, the inverse modeling based on MOEA (IM-MOEA), was proposed that mapped nondominated solutions from the object space (PF) to the decision space (PS). ${ }^{11}$ In this method, the $m$-input $n$-output multivariate inverse model is parsed in to $m \times n$ multivariate models, which considerably facilitates the model making and removes the requirement for dimensionality reduction. Then each univariate inverse model, discovered by a Gaussian process and a random grouping method. ${ }^{12,13}$

# 1.2 | Related work 

Many multiobjective EDAs are suggested from single objective EDAs, but from the first group (eg, the Bayesian network-based EDAs), for example, multiobjective Bayesian optimization algorithm (BOA) was proposed to create a Bayesian network as a model in order to generate offspring. ${ }^{14} \mathrm{~A}$ related work was proposed to predict the model by augmentation of Pareto ranking approach and BOA. ${ }^{15}$ Also, a Bayesian multiobjective was proposed whose model is made over the solutions selected by $\epsilon$-Pareto ranking method. ${ }^{16}$ In addition, in order to select a subset of solutions serving for a regression decision tree, an improved nondominated sorting approach was applied by decision tree-based multiobjective EDA to learn the model. ${ }^{17}$ Recently, in order to addressing many objective optimization problems, the multidimensional Bayesian network was suggested. ${ }^{18}$ In second group (eg, the mixture probability model-based EDAs), the multiobjective mixture-based iterated density estimation evolutionary algorithm using the mixed probability distributions in order to sampling well-distributed solutions. ${ }^{19}$ The multiobjective Parzen-based EDA learns from the Gaussian and Cauchy kernels to create its model. ${ }^{20}$ The multiobjective hierarchical BOA for discrete multiobjective optimization problems (MOPs) was proposed. ${ }^{21}$ Also, the multiobjective extended compact genetic algorithm applied a marginal product model as the mixture of the

probability model. ${ }^{22}$ Furthermore, the regularity model-based multiobjective estimation of distribution algorithm (RM-MEDA), was suggested which the decision vectors are mapped from the $n$-dimensional decision space to the ( $M-1$ )-D hidden space using a local principal component analysis. ${ }^{2}$ In recent years, the SAEAs have been applied in order to solve the multiobjective EDAs. ${ }^{7}$ Recently, Pan et al suggested a classification-based surrogate-assisted evolutionary algorithm (CSEA) that applies an artificial neural network instead of approximating the objective values in order to learn the dominance relationship between a candidate solution and a set of reference solutions. ${ }^{23}$ Also, the IM-MOEA, was proposed that mapped nondominated solutions from the object space (PF) to the decision space (PS). ${ }^{11}$ This algorithm is completely different from the SAEAs. ${ }^{24,25}$ The SAEAs build a map from the decision space to objective space and estimate the fitness of candidate solutions and helpful when no explicit fitness function exist or fitness functions are expensive computationally. While, the inverse models, have been suggested to approximate the distribution of the Pareto optimal solutions. Also a random grouping method used in this process (IM-MOEA) for dealing with large-scale optimization in order to reduce the number of required inverse models. ${ }^{26,27}$ But some of the effective inverse models, during the random grouping, may be removed. Also, random grouping method, removes the chance of allocated decision variables, to other objective spaces randomly. In addition, this method cannot determine the best assignment of decision variables $\left(x_{n}\right)$ to objective functions $\left(f_{m}\right)$. The idea of IM-MOEA has extended in order to solve MOPs with irregular PFs in a dynamic environment. ${ }^{28}$ In this model instead of using Gaussian process, a simple linear model has been applied in order to simplify the inverse modeling process. Also some approaches has concentrated on the PF modeling only, such as the Pareto-adaptive $\epsilon$-dominance-based algorithm. ${ }^{29}$ The rest of this paper is formed as follows: The next section is motivation and contributions. The problem statement is presented in Section 3 and briefly is reviewed some background necessary in the paper. The proposed algorithm is described in Section 4. Section 5 illustrates experimental analysis of applying algorithm, results, and computational complexity. Finally, conclusions and future work are given in Section 6.

# 2 | MOTIVATION AND CONTRIBUTIONS 

It can be seen that the basic idea in these algorithms is the replacement of heuristic operators with machine learning models such as regression models (eg, the Gaussian process), clustering models or classification models. So, recently, the model-based evolutionary algorithms (MBEAs) have been suggested in three groups: ${ }^{6}$ The EDAs, surrogate-assisted evolutionary algorithms and the inversed-models to map from the objective space to the decision space. In this paper, we concentrate on the inversed-model from the MBEAs and a new approach, based on an inversed model of Gaussian process and random forest framework, is proposed: random forest variable importance based on the inversed model of estimation of distribution algorithm (RFVI-IMEDA) in which a Gaussian process and random forest variable importance algorithm ${ }^{30,31}$ is used for mapping nondominated solutions from the objective space (PF) to the decision space (PS). Briefly, the Gaussian process is applied for estimating fitness values and random forest feature importance method is used to determine the best assignment of decision variables $\left(x_{n}\right)$ to objective functions $\left(f_{m}\right)$ in inverse model process. In fact, the importance of a variable $x_{n}$ in decision space for predicting $f_{m}$ is determined by random forest feature importance and variables are selected that are most importance. Therefore, the suggested method depends on a group of multiobjective EDAs that use probabilistic models instead of genetic conversions to generate offspring.

# 3 | PROBLEM STATEMENT 

The offspring in common EDAs are generated by creating and sampling a probabilistic model of promising solutions in the decision space. Then these samples mapped from decision space to objective space via the objective functions. In IM-MOEA, given the distributions of current parents in the decision space, namely $P\left(X^{p}\right)$, and in the objective space, $P\left(Y^{p}\right)$, the conditional probability distribution of $P\left(X^{p} \mid Y^{p}\right)$, is estimated and can be approximated by a probabilistic inverse model, that mapped nondominated solutions from the object space (PF) to the decision space (PS). To generate offspring, this method, produces samples in the objective space based on the information of the objective values of the current parent population, marked by $Y^{n}$. Then $Y^{n}$, using $P\left(X^{p} \mid Y^{p}\right)$ are mapped back to the decision space using the Bayes' theorem that has been described in Section 3.2:

$$
P\left(X^{o}\right)=\frac{P\left(X^{p} \mid Y^{p}\right) P\left(Y^{o}\right)}{P\left(Y^{p} \mid X^{p}\right)}
$$

where $P\left(X^{p} \mid Y^{p}\right)$, is a priori knowledge. These offspring are incorporated with the current parent population, from which parents for the next generation will be selected. ${ }^{11}$ It is hard to estimate the $m$-input and $n$-output inverse model $P\left(X^{p} \mid Y^{p}\right)$, where $m$ and $n$ are, respectively, the number of objectives and decision variables. As regards all decision variables are independent of each other. This method uses random grouping strategy, where multiple decision variables are randomly grouped together to be derived from the same objective using inverse models. It divides all of objective space into a number of subspaces, which can be approximated as follows:

$$
P(X \mid Y) \approx \prod_{i=1}^{N}\left(P\left(x_{i} \mid f_{j}\right)+\epsilon_{j, i}\right)
$$

where $j=1,2, \ldots, m, m>2$, and it is assumed that $\epsilon(j, i) \sim N\left(0,\left(\delta_{n}\right)^{2}\right)$, is a Gaussian noise. As a result, The Gaussian process can be applied to the inverse models that has been described in Section 3.1. In this way:

$$
P\left(x_{i} \mid f_{j}\right)=N\left(0, C+\left(\sigma_{n}\right)^{2} I\right)
$$

In order to raise the population diversity, polynomial mutation operator is used to all the sampled individuals. ${ }^{32}$ Figure 1 shows the framework of IM-MOEA.

In IM-MOEA, some of the effective inverse models, during this process, may be removed. For example, a 10-dimensional three objective optimization problem, three groups of models will be created. If $L=2$, due to the random grouping method, $x_{2}, x_{4}$, belonged to group $1, x_{1}, x_{6}$, to group 2 , and $x_{5}, x_{8}$, to the third group. Thus the first group includes the following two inverse models: $p\left(x_{2} \mid f_{1}\right), p\left(x_{4} \mid f_{1}\right)$, the second group includes $p\left(x_{1} \mid f_{2}\right), p\left(x_{6} \mid f_{2}\right)$, and the third group includes $p\left(x_{5} \mid f_{3}\right), p\left(x_{8} \mid f_{3}\right)$. As a result, the values of the allocated decision variables $\left(x_{1}, x_{2}, x_{4}, x_{5}, x_{6}\right.$ and $x_{8}$ ) will be change with new values created by the inverse models, and the values of the other four decision variables ( $x_{3}, x_{7}, x_{9}$ and $x_{10}$ ) will stay unchanged. In this example, when $x_{2}, x_{4}$ allocated to $f_{1}$, the chances of assigning $x_{2}$ and $x_{4}$ to $f_{2}$ and $f_{3}$, disappear. Also, when $x_{1}$ and $x_{6}$ allocated to $f_{2}$, the chances of assigning $x_{5}$ and $x_{8}$, to $f_{1}$ and $f_{2}$, disappear. Thus random grouping method, removes the chance of allocated decision variables, to other objective spaces randomly. In addition, this method cannot determine the best assignment of $x_{n}$ to $f_{m}$ and its function is based on random

![img-0.jpeg](img-0.jpeg)

FIG URE 1 The framework of inversed-model of multiobjective evolutionary algorithm [Color figure can be viewed at wileyonlinelibrary.com]
assignment. The random forests methods can be used to identify predictor variables are the most important and termed as random forest feature importance. ${ }^{33}$ In this section, some background concepts are presented.

# 3.1 | Gaussian process 

A Gaussian process is a set of random variables indexed by time or space, such that every finite set of those random variables has a multivariate normal distribution, that is, every finite linear mixture of them is normally distributed. ${ }^{34}$ The distribution of a Gaussian process is the joint distribution of all those (infinitely many) random variables and also it is a distribution over functions with a continuous domain, for example, time or space, that is mean GP defines a distribution over functions of the form $f: x \rightarrow \mathbb{R}$, which is completely specified by mean function $\mu(x)$ and covariance function $k\left(x, x^{\prime}\right)$ using the following equation:

$$
f(x) \sim \operatorname{GP}\left(\mu(x), k\left(x, x^{\prime}\right)\right)
$$

In probability theory and statistics, covariance is a measure of how much two variables change together, and the covariance function or kernel, describes the spatial or temporal covariance of a random variable process or field. For a random field or stochastic process $Z(x)$ on a domain $D$, a covariance function $C(X, Y)$ gives the covariance of the values of the random field at the two locations $X$ and $Y$ using the following equation:

$$
C(x, y)=\operatorname{cov}(Z(x), Z(y))
$$

The same $C(x, y)$ is called auto covariance function in two instances: in time series (to indicate exactly the same concept except that $x$ and $y$ refer to locations in time rather than in space), and in multivariate random fields (to refer to the covariance of a variable with itself, as opposed to the cross covariance between two different variables at different locations, $\operatorname{cov}\left(Z\left(x_{1}\right), Y\left(x_{2}\right)\right) .{ }^{35}$

A function is a valid covariance function if and only if this variance is nonnegative for all possible choices of $N$ and weights $w_{1}, \ldots, w_{n}$. A function with this property is called positive definite. ${ }^{36}$ Ultimately Gaussian processes translate as taking priors on functions and the smoothness of these priors can be induced by the covariance function. If we expect that for "near-by" input points $x$ and $x^{\prime}$ their corresponding output points $y$ and $y^{\prime}$ to be "near-by" also, then the assumption of continuity is present. If we wish to allow for significant displacement then we might choose a rougher covariance function. ${ }^{37}$ There are a common covariance functions, such as constant, linear, Gaussian noise, squared exponential, Orenstein-Uhlenbeck, Matern, periodic and rational quadratic. ${ }^{38}$

# 3.2 | Bayesian linear regression 

In statistics, linear regression is a linear scheme for modeling the relationship between a scalar dependent variable $y$ and one or more expository variables (or independent variables) defined $x$. The case of expository variable is termed simple linear regression. For more than one expository variable, the process is termed multiple linear regression. ${ }^{39}$ In linear regression, the communications are patterned using linear predictor functions whose unknown model parameters are approximated from the data. Here, let $S=\left\{x^{(i)}, y^{(i)}\right\}_{(i=1)}^{n}$ be a training set of i.i.d examples from some unknown distribution. The regression model is described by using the following equation:

$$
y=f(X)+\epsilon
$$

The goal is to estimate the regression function $f($.$) , to make prediction of y,=f\left(X_{*}\right)$, with parametric (Maximum Likelihood, Bayesian inference [parametric model $f_{w}(x)$ ]) or nonparametric methods (Kernel regression [Nadaraya-Watson estimator], GP regression), which in linear regression using the following equation:

$$
y=X W+\epsilon
$$

where

$$
y=\left(\begin{array}{c}
y_{1} \\
y_{2} \\
\cdot \\
\cdot \\
\cdot \\
y_{n}
\end{array}\right), \quad X=\left(\begin{array}{c}
X_{1}^{T} \\
X_{2}^{T} \\
\cdot \\
\cdot \\
\cdot \\
X_{n}^{T}
\end{array}\right)=\left(\begin{array}{cccc}
1 & x_{11} & \ldots & x_{1 p} \\
1 & x_{21} & \ldots & x_{2 p} \\
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot \\
1 & x_{n 1} & \ldots & x_{n p}
\end{array}\right), \quad W=\left(\begin{array}{c}
w_{1} \\
w_{2} \\
\cdot \\
\cdot \\
w_{n}
\end{array}\right), \quad \epsilon=\left(\begin{array}{c}
\epsilon_{1} \\
\epsilon_{2} \\
\cdot \\
\cdot \\
\epsilon_{n}
\end{array}\right)
$$

The Bayesian linear regression is a procedure to linear regression in which the statistical analysis is assumed within the context of Bayesian inference. When the regression pattern has error that have a normal distribution, and if a particular form of prior distribution is assumed, explicit results are available for the posterior probability distributions of the model's parameters. ${ }^{40}$ In Equation (7), $\epsilon$, is a normal with mean zero and $\delta^{2}$ variance, $N\left(0, \delta^{2} I\right)$, and $W$ is a multivariate Gaussian, and let $Z_{x}=X W$, which $Z_{x}$, is a GP. These two variables are independent of each other and therefore $y=Z+\epsilon$, is multivariable Gaussian process. As a result: $y \sim N\left(\mu+0, K+\delta^{2} I\right)$,

where, $K+\delta^{2} I$, is covariance. We can divide $y$ in two parts $y_{a}=\left(\begin{array}{c}y_{1} \\ y_{l} \\ y_{l}\end{array}\right)$ and $y_{b}=\left(\begin{array}{c}y_{l+1} \\ \vdots \\ y_{n}\end{array}\right)$. Similarly we can consider the mean and variance as follows: $\mu=\binom{\mu_{a}}{\mu_{b}}$ and $\sum^{-1}=K=\left(\begin{array}{ll}k_{a a} & k_{a b} \\ k_{b a} & k_{b b}\end{array}\right)$. As we know, in regression, we have some observed data at some $X_{i}$ and $y_{i}$ that's here $y_{b}$ and $y_{a}$, is unobserved data. So, we like to get the posterior predictive distribution on the $y$ 's corresponding to $X_{1}, \ldots, X_{l}$, that given these $y^{\prime} s, y_{i+1}, \ldots, y_{n}$. A number of useful properties of multivariate Gaussian as follows:
a. Normalization. The density function normalizes, that is, $\int_{x} P(x, \mu, \Sigma) d x=1$.
b. marginalizaton. The marginal densities,

$$
P\left(x_{A}\right)=\int_{x_{B}} p\left(x_{A}, x_{B} ; \mu \sum\right) d x_{B}=\int_{x_{A}} p\left(x_{A}, x_{B} ; \mu \sum\right) d x_{A}
$$

are Gaussian:

$$
x_{A} \sim N\left(\mu_{A}, \sum_{A A}\right), x_{B} \sim N\left(\mu_{B}, \sum_{B B}\right)
$$

# c. Conditioning. 

The conditional densities:

$$
p\left(x_{A} \mid x_{B}\right)=\frac{p\left(x_{A}, x_{B} ; \mu, \Sigma\right)}{P\left(x_{B}\right)}=\frac{p\left(x_{A}, x_{B} ; \mu, \Sigma\right)}{\int_{x_{A}} p\left(x_{A}, x_{B} ; \mu, d \Sigma\right) d x_{A}}
$$

Due to the Equation (4) and multivariate Gaussian process:

$$
\begin{aligned}
P\left(y_{A} \mid y_{B}\right) & =\frac{p\left(y_{A}, y_{B} ; \mu, \Sigma\right)}{\int_{y_{A}} p\left(y_{A}, y_{B} ; \mu, \Sigma\right) d y_{A}} \\
& =\frac{1}{\int_{y_{A}} p\left(y_{A}, y_{B} ; \mu, \Sigma\right) d y_{A}} \cdot\left[\frac{1}{(2 \pi)^{m}} \exp \left(-\frac{1}{2}(y-\mu)^{T} \Sigma^{-1}(y-\mu)\right)\right] \\
& =\frac{1}{Z_{1}} \exp \left\{-\frac{1}{2}\left(\left[\begin{array}{l}
y_{a} \\
y_{b}
\end{array}\right]-\left[\begin{array}{l}
\mu_{a} \\
\mu_{b}
\end{array}\right]^{\top}\left[\begin{array}{ll}
V_{a a} & V_{a b} \\
V_{b a} & V_{b b}
\end{array}\right]\left(\left[\begin{array}{l}
y_{a} \\
y_{b}
\end{array}\right]-\left[\begin{array}{l}
\mu_{a} \\
\mu_{b}
\end{array}\right]\right)\right\}
\end{aligned}
$$

where $Z_{1}$ is a proportionality constant which does not depend on $y_{a}$. To simplify this phrase:

$$
\begin{aligned}
\left(\left[\begin{array}{l}
y_{a} \\
y_{b}
\end{array}\right]-\left[\begin{array}{l}
\mu_{a} \\
\mu_{b}
\end{array}\right]^{T}\left[\begin{array}{lll}
V_{a} a & V_{a} b \\
V_{b} a & V_{B} B
\end{array}\right]\left(\left[\begin{array}{l}
y_{a} \\
y_{b}
\end{array}\right]-\left[\begin{array}{l}
\mu_{a} \\
\mu_{b}
\end{array}\right]\right)\right)= & \left(y_{a}-\mu_{a}\right)^{T} V_{a a}\left(y_{a}-\mu_{a}\right)+\left(y_{a}-\mu_{a}\right)^{T} V_{a b}\left(y_{b}-\mu_{b}\right) \\
& +\left(y_{b}-\mu_{b}\right)^{T} V_{b a}\left(y_{a}-\mu_{a}\right)+\left(y_{b}-\mu_{b}\right)^{T} V_{b b}\left(y_{b}-\mu_{b}\right)
\end{aligned}
$$

With preserving only sections dependent on $y_{a}$ and using the rule that $V_{a b}=V_{b a}^{T}$, we have:

$$
P\left(Y_{a} \mid Y_{b}\right)=\frac{1}{Z_{2}} \exp \left(-\frac{1}{2}\left[y_{a}^{T} V_{a a} y_{a}-2 y_{a}^{T} V_{a a} \mu_{a}+2 y_{a}^{T} V_{a b}\left(y_{b}-\mu_{b}\right)\right]\right)
$$

where $Z_{2}$ is a new proportionality constant not depending on $y_{a}$. Finally, using the completion of squares argument, ${ }^{41}$ we have:

$$
P\left(Y_{a} \mid Y_{b}\right)=\frac{1}{Z_{3}} \exp \left(-\frac{1}{2}\left(y_{a}-\mu^{\prime}\right)^{T} V_{a a}\left(y_{a}-\mu^{\prime}\right)\right)
$$

where $Z_{3}$ is again a new proportionality constant which does not depend on $y_{a}$, and $\mu^{\prime}=\mu_{a}+$ $V_{a b} V_{b b}^{(-1)}\left(y_{b}-\mu_{b}\right)$. If $A=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right] \rightarrow A^{-1}=\frac{1}{\operatorname{det}(A)}\left[\begin{array}{cc}d & -b \\ -c & a\end{array}\right]=\frac{1}{(a d-b c)}\left[\begin{array}{cc}d & -b \\ -c & a\end{array}\right]$. Thus:

$$
\left[\begin{array}{ll}
V_{a a} & V_{a b} \\
V_{b a} & V_{b b}
\end{array}\right]^{-1}=\frac{1}{V_{a a} V_{b b}-V_{a b} V_{b a}}\left[\begin{array}{cc}
V_{b b} & -V_{a b} \\
-V_{b a} & V_{b b}
\end{array}\right]
$$

Given that, $C=K+\delta^{2} I$, we have:

$$
\begin{gathered}
P\left(y_{a} \mid y_{b}\right)=N\left(y_{a} \mid m, D\right) \\
m=\mu_{a}+V_{a b} V_{b b}^{-1}\left(y_{b}-\mu_{b}\right)=\mu_{a}+k_{a b}\left(k_{b b}+\delta^{2} I\right)^{-1}\left(y_{b}-\mu\right) \\
D=V_{a a}-V_{a b} V_{b b}^{-1} V_{b a}=\left(k_{a a}+\delta^{2} I\right)-k_{a b}\left(k_{b b}+\delta^{2} I\right)^{-1} k_{b a}
\end{gathered}
$$

# 4 THE PROPOSED ALGORITHM 

## 4.1 | Framework of the proposed algorithm

The IM-MOEA uses the random grouping method in order to parse high-dimensional optimization problems into a number of low dimensional subproblems, without a prior knowledge of the nonseparability of a problem. In this algorithm, we replace three methods of random forest variable importance with random grouping in order to prevent the elimination of some effective inverse models and losing the chance of allocated decision variables, to other objective spaces randomly:

1. The classical permutation variable importance random forest method that has been described in Section 4.2.
2. The random forest naïve variable importance method that has been described in Section 4.3.
3. The random forest cross-validation variable importance method that has been described in Section 4.4.

![img-1.jpeg](img-1.jpeg)

FIG URE 2 The schematic illustration of the basic idea in proposed algorithm [Color figure can be viewed at wileyonlinelibrary.com]

In addition, random grouping process cannot determine the best assignment of $x_{n}$ to $f_{m}$ and its performance is based on random assignment. In fact, the importance of a variable $x_{n}$ in decision space for predicting $f_{m}$ is determined by random forest feature importance and variables are selected that are most importance. This paper proposes a new model-based on random forest, in order to determine the best assignment of $x_{n}$ to $f_{m}$. When the distribution of each gene $\left(x_{i}\right)$ over any of fitness functions $\left(f_{j}\right)$, are known, the best distributions can be select and it is not necessary to be assigned $x_{n}$ to $f_{m}$ randomly. On other hands, for decision variables assigned to the same group, their correlations can be implicitly increased by selecting the best distributions. Given $m$ objectives, $m$ groups of inverse models will be made for each subpopulation, where all models in group $j, 1 \leq j \leq m$, apply $f_{j}$ as the variable. In each group, $L$ decision variables will be selected by suggested method to build inverse models using $f_{j}$ as the variable, where $L \ll n$ is a parameter to be determined. The schematic illustration of the basic idea in the proposed algorithm is shown in Figure 2. In IM-MOEA, the Gaussian process (GP) and Bayesian linear regression is used to estimate decomposed univariate probability distribution, $P_{k}\left(x_{i} \mid f_{j}\right), 1 \leq i \leq$ $n, 1 \leq j \leq m, 1 \leq k \leq K$, for each subpopulation and it assumes that there are $N_{k}$ individuals (data pairs) overall for training m groups of inverse models. In proposed algorithms, each groups of inverse models are trained through variable importance of random forest. The univariate probability distribution, $P_{k}\left(x_{i} \mid f_{j}\right)$, is calculated according to Equation (19), in which the mean and variance of the Gaussian distribution, are obtained according to Equations (15) and (16). The overall algorithm framework of the proposed method, based on random forest feature importance, is illustrated in Algorithm 1. In each generation, population is divided in to a number of subpopulations based on predefined reference points in the objective space. Then selection is done within each subpopulation and using NSGA-II, the individuals in each subpopulation sorts into a number of nondominated fronts and a crowding distance is applied. Then an inversed model based on random forest feature importance is made for each subpopulation for reproduction. Offspring individuals reproduced by all subpopulations are put together with the parents in the present generation to form the population for the next generation.

Algorithm 1. The overall algorithm framework of the proposed method, based on random forest
Initialization: randomly initialize population, define K reference vectors for subpopulation creation.
/*main loop*/
while termination condition is not satisfied do
partition of the combined population: partition the combined population $P(t)$ by associating the solutions with the $K$
predefined reference vectors;
Nondominated Sorting and Selection: create sub parent populations $P^{1}(t), \ldots, P^{K}(t)$;
for $k=1$ to K do
Inverse Modeling: for each sub population $P^{k}(t)$, apply the variable importance of Random Forest method to
determine the best assignment of $x_{n}$ to $f_{m}$ in each group, which inverse models are to be build; training a

Gaussian process with Bayesian linear regression for each inverse model;
Reproduction: reproduce new candidate solutions, $O^{k}(t)$, for each subpopulation by sampling the objective space using
the inverse models; perform mutation on the sampled candidate solutions;
Update the combined population: $P(t+1)=\bigcup_{(k=1)}^{K}\left(P^{k}(t) \cup O^{k}(t)\right)$;
end for
$t=t+1$;
end while

Algorithm 2 uses the random forest naïve variable importance method and the individuals in each subpopulation sorts into a number of nondominated fronts and a crowding distance is applied for each subpopulation of nondominated solutions. Then the random forest naive variable importance is applied to determine the best assignment of $x_{n}$ to $f_{m}$ in each group and null distribution is approximated based on the observed nonpositive importance scores, while in classical random forest variable importance, some values of variable importance were negative or close to zero and do not improve the trees' predictive strength. In fact, with the random forest naive variable importance, the importance of all $x_{n}, n=1, \ldots, n$, is determined for each of the $f_{m}, m=1, \ldots, m$ in each subpopulation and then $x_{i}$ are chosen for each $f_{m}$ which are higher variable importance than other $x_{n}$. Then an inversed model is made based on the selected $x_{i}$ for each $f_{m}$, for each subpopulation in order to reproduction.

Algorithm 3 uses the random forest cross-validation variable importance method and apply twofold cross-validation in order to assignment of the best $x_{n}$ to $f_{m}$ in each group of subpopulation. In this method, each subpopulation that are sorted into a number of nondominated fronts and a crowding distance, are divided into two sets with equal size randomly and each set generates a random forest. Then two forests are applied to compute the hold out variable importance. The null distribution for the hold-out variable importance is approximated based on the observed nonpositive importance scores. Therefore, the Naïve testing approach is applied in this method. In fact, in this method, the $x_{i}$ are chosen for each $f_{m}$ which are higher variable importance than other $x_{n}$. Then an inversed model is made based on the selected $x_{i}$ for each $f_{m}$, for each subpopulation in order to reproduction. This method is appropriate for high dimensional data.

Algorithm 2. The overall algorithm framework of the proposed method, based on random forest naïve variable importance

Initialization: randomly initialize population, define $K$ reference vectors for subpopulation creation.
/*main loop*/
while termination condition is not satisfied do
partition of the combined population: partition the combined population $P(t)$ by associating the solutions with the $K$
predefined reference vectors;
Nondominated Sorting and Selection: create sub parent populations $P^{1}(t), \ldots, P^{K}(t)$;
for $k=1$ to K do
Inverse Modeling: for each subpopulation $P^{k}(t)$, apply the variable importance of Random Forest Naive method
to determine the best assignment of $x_{n}$ to $f_{m}$ in each group, which inverse models are to be build; training a

Gaussian process with Bayesian linear regression for each inverse model;
Reproduction: reproduce new candidate solutions $O^{k}(t)$ for each subpopulation by sampling the objective space using
the inverse models; perform mutation on the sampled candidate solutions;
Update the combined population: $P(t+1)=\bigcup_{(k=1)}^{K}\left(P^{k}(t) \cup O^{k}(t)\right)$;
end for
$t=t+1$;
end while

# 4.2 | Classical permutation variable importance random forest 

Decision trees are a public method for different machine learning tasks. But, in particular, when trees are grown very deep, tend to learn highly immethodical patterns. They over fit their training sets, that is, have low bias, but very high variance. Random forests are a way of averaging multiple deep decision trees, trained on different parts of the same training set, with the goal of reducing the variance. Therefore, Random Forest is an ensemble method that operate by making a collection of decision trees at training time and creating the class that is classification or mean prediction (regression) of the individual trees. ${ }^{42}$ This algorithm is a flexible, even without hyper parameter tuning, a great result most of the time and it can be used for both classification and regression tasks. ${ }^{43}$ Leo Breiman suggested a method of making a forest of uncorrelated trees via a classification and regression tree (CART) like procedure, which combined with randomized node optimization and bagging. Also, he combined several components, which formed the basis of modern style of random forests, in particular using out-of bag error, as an estimate of generalization error and measuring variable importance via permutation. The training algorithm for random forests uses the general methods of bootstrap aggregating, also called bagging, in order to tree learners. Through bagging approach, resampling is used for the generation of each tree in the forest. A bagging subset of the training dataset is generated to train each tree in the forest. In fact, on average, each tree uses two-thirds of training dataset. The unused elements are called the out-of-bag (OOB) samples and this elements can be applied for validation. Given a training set $X=x_{1}, \ldots, x_{n}$ with responses $Y=y_{1}, \ldots, y_{n}$, through bagging approach,

$B$ times selects a random sample with replacement of the training set and fits trees to these samples:

For $b=1 \ldots B$ :

1. Sample, with replacement, $n$ training examples from $\mathrm{X}, \mathrm{Y}$; call these $X_{b}, Y_{b}$.
2. Train a classification or regression tree $f_{b}$ on $X_{b}, Y_{b}$.
end For

Algorithm 3. The overall algorithm framework of the proposed method, based on random forest cross-validation variable importance

Initialization: randomly initialize population, define $K$ reference vectors for subpopulation creation.
/*main loop*/
while termination condition is not satisfied do
partition of the combined population: partition the combined population $P(t)$ by associating the solutions with the $K$
predefined reference vectors;
Non-dominated Sorting and Selection: create sub parent populations $P^{1}(t), \ldots, P^{K}(t)$;
for $k=1$ to K do
Inverse Modeling: for each sub population $P^{k}(t)$, apply the variable importance of Random Forest

Cross-validation method to determine the best assignment of $x_{n}$ to $f_{m}$ in each group, which inverse models are to be
build; training a Gaussian process with Bayesian linear regression for each inverse model;

Reproduction: reproduce new candidate solutions $O^{k}(t)$ for each subpopulation by sampling the objective space using
the inverse models; perform mutation on the sampled candidate solutions;
Update the combined population: $P(t+1)=\bigcup_{(k=1)}^{K}\left(P^{k}(t) \cup O^{k}(t)\right)$;
end for
$t=t+1 ;$
end while

After training, predictions for samples $x^{\prime}$ which have not been seen, can be generated by averaging the predictions from all the individual regression trees on $x^{\prime}$ using the following equation:

$$
\hat{f}=\frac{1}{N} \sum_{b=1}^{B} f_{b}\left(x^{\prime}\right)
$$

Or by taking the majority vote in the case of classification trees. This bagging procedure results to better model performance, because it reduces the variance of the model, without growing the bias. Additionally, an estimate of the uncertainty of prediction can be built as the SD of the predictions from all the individual regression trees on $x^{\prime}$ using the following equation:

$$
\delta=\sqrt{\sum_{b=1}^{B}\left(f_{b}\left(x^{\prime}\right)-\hat{f}\right)^{2} / B-1}
$$

The number of samples/trees, B, is a free parameter. An optimal number of trees B can be detected through cross-validation ${ }^{44}$ or by observing OOB error. ${ }^{45}$ Cross-validation or out-of-sample testing is any of different similar model validation methods for evaluating how a result of a statistical analysis will generalize to an independent dataset. OOB error also named OOB estimate, is method of measuring the prediction error of random forests, that using bootstrap aggregation (bagging) to subsample data samples used for training. OOB is the mean prediction error on each training sample $x_{i}$, using only the trees that did not have $x_{i}$ in their bootstrap sample. Subsampling lets one to define an OOB estimate of the prediction efficiency improvement by assessing predictions on those observations which were not applied in the making of the next base learner. The OOB samples can be applied to estimate the importance of each variable and create a rank for them. For each tree and its respective OOB samples, the accuracy of this set, is computed and then randomly a variable among samples is permuted and the accuracy of new set is recomputed. It allows you to have a relevance comparison metric as variable importance measure.

Another way to generate an importance rank is, on each tree and each node split, to compute the split improvement by the Gini index measure and use these values to compare the importance of variables.

Breiman $(2001,2002)$ suggested to measure the importance of a variable $X_{m}$ for predicting $Y$ with Equation (20) through adding up the weighted impurity decreases $p(t) i \Delta\left(s_{i}, t\right)$ for all nodes t where $X_{m}$ is applied, and then is averaged over all $N_{T}$ trees in the forest:

$$
\operatorname{Imp}\left(X_{m}\right)=\frac{1}{N_{T}} \sum_{T} \sum_{t \in T: v\left(S_{i}\right)=X_{m}} p(t) i \Delta\left(s_{i}, t\right)
$$

where $p(t)$ is the relative amount of $\frac{N_{T}}{N}$ samples who achieved $t$ and, $v\left(s_{i}\right)$ is the variable used in splits $s_{i}$. When we apply Gini index as impurity function, this measure is known as Gini importance or Mean Decrease Gini and this equation is called the MDI.

Suppose that we have a set of categorical input variables $V=\left\{X_{1}, \ldots, X_{p}\right\}$ and a categorical output $Y$ and the joint (Shannon) entropy of a set of $V$, is defined by the following equation:

$$
H(X)=-\sum_{x \in X} P_{X}(x) \log _{2} P_{X}(x)
$$

and the mean conditional entropy of a set of random variables $V$, given the values of variables $Y$, is defined by the following equation:

$$
H(X \mid Y)=-\sum_{x \in X} \sum_{y \in Y} P_{X, Y}(x, y) \log _{2} P_{X,}(x, y)
$$

In probability theory and information theory, the mutual information of two random variables, is a measure to show the degree of mutual dependence between the two variables. More specifically, it quantifies the amount of information acquired about one random variable through observing the other random variable. This concept is related with the entropy of a random variable. As shown in Figure 3, additive and subtractive relationships different information measures associated with correlated variables $X$ and $Y$. The space contained by both circles is the joint entropy $H(X, Y)$. The circle on the left (red and violet), is the individual entropy $H(X)$, with the red being the conditional entropy $H(X \mid Y)$. The circle on the right (blue and violet) is $H(Y)$, with the blue being $H(Y \mid X)$. The violet is mutual information $I(X ; Y)$.

FIGURE 3 The relation between mutual information and entropy [Color figure can be viewed at wileyonlinelibrary.com]
![img-2.jpeg](img-2.jpeg)

The mean conditional mutual information between the set of random variables $X=$ $\left\{X_{1}, \ldots, X_{p}\right\}$ and the set of random variables $Y=\left\{Y_{1}, \ldots, Y_{q}\right\}$, given the values of the third set of random variables $Z=\left\{Z_{1}, \ldots, Z_{r}\right\}$, is defined by the following equation:

$$
\begin{aligned}
H(X ; Y \mid Z) & =H(X \mid Z)-H(X \mid Y, Z)=H(Y \mid Z)-H(X \mid Y, Z) \\
& =-\sum_{x \in X} \sum_{y \in Y} \sum_{z \in Z} P_{X, Y, Z}(x, y, z) \log _{2} \frac{P_{X \mid Z}(x \mid z) P_{Y \mid Z}(y \mid z)}{P_{X, Y \mid Z}(x, y \mid z)}
\end{aligned}
$$

And also remind the chaining rule the following equation:

$$
I(X, Z ; Y \mid W)=I(X ; Y \mid W)+I(Z ; Y \mid W)+I(Z ; Y \mid W, X)
$$

And symmetry of the conditional mutual information between sets of random variables are as following equation:

$$
I(X ; Y \mid Z)=I(Y ; X \mid Z)
$$

Given a training sample $\Gamma$ of $N$ joint observations of $X_{1}, \ldots, X_{p}, Y$ independently drawn from the joint distribution $P\left(X_{1}, \ldots, X_{p}, Y\right)$. A randomized and fully developed tree is a decision tree in which each node $t$ is partitioned using a variable $X_{j}$ chosen uniformly at random among those not yet applied at the parent nodes of $t$, where each node $t$ is split in to $\left|X_{j}\right|$ subtrees, that is, one for each possible value of $X_{j}$, and where the recursive construction process stops only when all $P$ variables have been applied along the current branch. Each node has a left and right child and impurity measure of each node is equal the following equation:

$$
i(t)-P_{L} \cdot i\left(N_{L}\right)-\left(1-P_{L}\right) \cdot i\left(N_{R}\right)
$$

where $N_{L}$ and $N_{R}$ are impurity measure of left and right node and $P_{L}$ is the proportion of samples which are assigned in to left node and $\left(1-P_{L}\right)$ is the proportion of samples which are assigned in to right node. Using the entropy $H(Y \mid t)=-\sum_{j} P_{j \mid t} \log _{2} P(j \mid t)$ as impurity measure $i(t)$, the importance of a variable $X_{j}$, can be rewritten in terms of mutual information using the following equation:

$$
\operatorname{Imp}\left(X_{j}\right)=\frac{1}{M} \sum_{m=1}^{M} \sum_{t \in \varphi_{m}} P(t) I\left(Y ; X_{j} \mid t\right)
$$

As the size of training sample grows to infinity, $P(t)$ turns in to the probability that an object attains node $t$, that is, a probability $P(B(t)=b(t))$, where $B(t)=\left(X_{\left(i_{1}\right)}, \ldots, X_{\left(i_{k}\right)}\right)$ is a subset of $k$ variables tested in the branch from the root node to the parent of $t$ and $b(t)$ is the vector of values of these variables. As, the number of $M$ randomize trees grows to infinity, the importance of a variable $X_{j}$ can be written using the following equation:

$$
\operatorname{Imp}\left(X_{j}\right)=\sum_{B \subseteq V^{-j}} \sum_{B \in X_{i_{1}}, \ldots, X_{i_{k}}} \alpha\left(B, b, X_{j}, p\right) P(B=b) I\left(Y ; X_{j} \mid B=b\right)
$$

where $b$ is a set of values for the variables in $B$, and $\alpha\left(B, b, X_{j}, p\right)$ is the probability that a node $t$ (at depth $k$ ) in a randomize tree tests the variables $X_{j}$, which is equal to a branch with a path defined, that leading to $t$, through all $k$ variables $X_{\left(i_{1}\right)}, \ldots, X_{\left(i_{k}\right)} \in B$ and their corresponding values in $b$ and the probability of this branch is equal to the probability of choosing (uniformly at random) $X_{\left(i_{1}\right)}$ at the root node as remaining $X_{\left(i_{2}\right)}, \ldots, X_{\left(i_{k}\right)}$ variables in the subtree corresponding to the value $X_{\left(i_{1}\right)}$ of $X_{\left(i_{1}\right)}$ defined in $b$. It is certain that the root node is split in to $\left|X_{\left(i_{1}\right)}\right|$ subtrees. Then the probability of testing $X_{j}$ at the end of this branch is equal to the probability of choosing $X_{j}$ among the remaining $p-k$ variables. By recursion, we have the following equation:

$$
\frac{1}{p} \frac{1}{p-1} \ldots \frac{1}{p-k+1} \frac{1}{p-k}=\frac{(p-k)!}{p!} \frac{1}{p-k}
$$

Since the order along which the variables appear in the branch is of no importance, $\alpha\left(B, b, X_{j}, p\right)$ in Equation (29), actually includes all $k$ ! ways of making a branch composed of the variables and values in $B$ and $b$ :

$$
\alpha\left(B, b, X_{j}, p\right) P(B=b) I\left(Y ; X_{j} \mid B=b\right)=k!\frac{(p-k)!}{p!} \frac{1}{p-k}=\frac{1}{C_{p}^{k}} \frac{1}{p-k}
$$

From this expression, $\alpha\left(B, b, X_{j}, p\right)$ depends only on the size $k$ of $B$ and the number $p$ of variables. So, by grouping in the previous equation of $\operatorname{Imp}\left(X_{j}\right)$ in Equation (30) conditioning variable subsets $B$ according to their sizes and using the definition of conditional mutual information, $\alpha$ can be factored out:

$$
\operatorname{Imp}\left(X_{j}\right)=\sum_{k=0}^{p-1} \frac{1}{C_{p}^{k}} \frac{1}{p-k} \sum_{B \in P_{k}\left(V^{-j}\right)} I\left(X_{j} ; Y \mid B\right)
$$

where $V^{(-j)}$ denotes the subset $V \backslash\left\{X_{j}\right\}$, and $P_{k}\left(V^{(-j)}\right)$ is the set of subsets of $V^{(-j)}$ cardinality $k$ and $I\left(X_{j} ; Y \mid B\right)$ is the conditional mutual information of $X_{j}$ and $Y$ given the variables in $B$, which can be calculated by Equation (22).

A variable (eg, $\operatorname{Imp}\left(X_{j}\right)$ ) is called related if after the random permutation, the errors of tree prediction or accuracy of prediction increase significantly. Regarding the values variable importance, the negative values or values of zero, illustrate that variable does not improve the trees' predictive strength, because the error rates are similar or even larger when applying unchanged version of the variable. In contrast, a positive value for the variable importance expresses that the variable at least some improves the trees' predictive strength, because the error rates are smaller when applying the original version of the variable for deriving tree predictions. However it cannot be deduced that a positive value for the variable importance demonstrates a relative value. For

this purpose a test procedure is required. The testing approach of Altmann et al was proposed as a heuristic in order to modify biased importance measures, such as the Gini importance measure. Also, the $P$-values are computed from importance scores. With this feature, the user can select related variables. In the first step of this process, the variable importance scores are computed for all variables. In the second step, for variables that are not associated with the response, the importance scores are obtained by randomly permuting the response variable in order to split any continuity between the response variable and all predictor variables. Then a new random forest is created and the importance scores for the predictor variables is computed. This process is repeated $s$ times. The importance scores can be considered as the unknown null distribution. The $S$ importance scores are applied for computing the $P$-value for variables. For this purpose, the fraction of $S$ importance scores that are greater than the original importance score, is computed. Also, it can be assumed a parametric distribution such as the Gaussian, Log-normal, or Gamma distribution for the importance scores of irrelevant predictor variables. The parameters of each distribution are computed by the maximum likelihood estimate. This approach is called parametric approach.

# 4.3 | Random forest naïve variable importance 

In this method, a new heuristic approach is proposed in which the null distribution is approximated based on the observed non-positive importance scores. For this purpose, the variable importance null distribution reflects the observed negative and zero importance scores on the y -axis. Let $M_{1}=\left\{V I_{j} \mid V I_{j}<0 ; j=1 \ldots p\right\}$ defines the observed negative variable importance scores and $M_{2}=\left\{V I_{j} \mid V I_{j}=0 ; j=1 \ldots p\right\}$ defines the observed variable importance scores that are equal zeros and $P$ defines the number of candidate predictors. In this method, a new importance score is defined which multiplying the negative importance scores by $-1: M_{3}=\left\{-V I_{j} \mid V I_{j}<0 ; j=\right.$ $1 \ldots p\}=-M_{1}$. Therefore, the null distribution $\hat{F}_{0}$ is obtained as the empirical cumulative distribution function of $M=M_{1} \cup M_{2} \cup M_{3}$. This method is not appropriate for all type of data and data should include a large number of variables without effect.

## 4.4 | Random forest cross-validation variable importance

This method does not apply the OOB observation and uses the cross-validation procedure. The data is split into $k$ sets that have equal size. Then $k$ forests is constructed where the $l$ th forest is created based on observations that are not part of the $l$ th set. The simplest type of cross-validation results for $k=2$, so that each of the two sets is once applied for generating the forest and once for deriving importance scores. This method is known as twofold cross-validation or hold out method. Therefore, the data is divided into two sets with equal size randomly and each set generates a random forest. Then two forests are applied to compute the hold out variable importance. The null distribution for the hold-out variable importance is approximated based on the observed non-positive importance scores. Also, the Naïve testing approach is applied in this method. For this purpose the sets is defined: $M_{1}=\left\{V I_{j}^{H O} \mid V I_{j}^{H O}<0 ; j=1 \ldots p\right\}$ for all negative importance scores, $M_{2}=\left\{V I_{j}^{H O} \mid V I_{j}^{H O}=0 ; j=1 \ldots p\right\}$ for all importance scores of zeros and $M_{3}=$ $\left\{-V I_{j}^{H O} \mid V I_{j}^{H O}<0 ; j=1 \ldots p\right\}=-M_{1}$ for all negative importance scores multiplied by -1 and consider the empirical cumulative distribution function $\hat{F}_{0}$ of $M=M_{1} \cup M_{2} \cup M_{3}$. This method uses the difference in error rates before and after randomly permuting the values of the considered variable and called random forest cross-validation.

# 5 | EXPERIMENTAL ANALYSIS 

In this section, some tests have been conducted in order to show the performance of the three proposed methods at a wide range of parameters and proposed methods are tested and compared with IM-MOEA, CSEA, and RM-MEDA on the two groups of benchmark tests: the modified test instances of ZDT and DTLZ, and The WFG test suite.

## 5.1 | Test sets

The three proposed methods is tested on two sets of MOPs, the modified test instances of ZDT and DTLZ, which introduced in Reference $2\left(F_{1} t o F_{10}\right)$ which is used for results of IM-MOEA ${ }^{11}$ and the linkage between the decision variables as the following equations:

$$
\begin{gathered}
x_{i} \rightarrow\left(1+\alpha \frac{i}{n}\right) x_{i} \\
x_{i}^{2} \rightarrow\left(x_{i}^{\frac{1}{1+\beta_{0}^{2}}}\right)
\end{gathered}
$$

where $i$ is the index of each decision variable, and $\alpha$ and $\beta$ are two control parameters and are equal to $\alpha=5$ and $\beta=3$, and the number of decision variables is put to $n=30$. In this test problem F1 has a linear PF and test problem F3 has many local PFs and one global PF in order to check an MOEA's ability to converge to the global PF. The test problem F4 checks an MOEA's ability in order to maintain a good distribution of solutions. Both test problems F5 and F6 have a curve PF. The test problem F7 has a disconnected set of Pareto-optimal regions in roder to maintain subpopulation in different Pareto-optimal regions.

The WFG test suite, containing nine test problems (WFG1 to WFG9). ${ }^{46}$ We use three-objective WFG test instances whose pareto set has a dimentionality of four. The number of decision variables of WFG functions is put to 104. Both test problems of WFG1 and WFG7 are separable and unimodal. The nonseparable reduction of WFG6 and WFG9 is more difficult than that of WFG2 and WFG3, the multimodality of WFG4 has larger "hill sizes" and is thus more difficult than that of WFG9.

## 5.2 | Performance metrics

A simple way to evaluate the quality of solution sets is Quality indicators (QIs). In general, QIs can be classified in to six categories: ${ }^{47}$ (i) QIs for convergence, (ii) QIs for spread, (iii) QIs for uniformity, (iv) QIs for cardinality, (v) QIs for both spread and uniformity, and (vi) QIs for incorporated quality of the four quality aspects. There are two classes of convergence in QIs: one is to evaluate the Pareto dominance relation between solutions or sets and two is to evaluate the distance of a solution set to the PF. The GD indicator measures the quadratic mean of the Euclidean distances of solutions set to the nearest point on the PF. ${ }^{48}$ Spread quality is related to the area of a solution set covering. The pure diversity (PD) summarizes the dissimilarity of each solution to the remaining solutions of a solution set. ${ }^{49}$ Quality indicators for uniformity evaluate how uniformly a set's solutions are distributed and measuring the variation of the distance between the

solutions, such as spacing (SP). ${ }^{50}$ QIs for cardinality add a different nondominated solution to the set under regard should improve the evaluation result. The QIs for spread and uniformity are closely related and can be used together to show the diversity of solution sets and classified into two groups: distance-based indicators and region division-based indicators. The region division-based QIs partitions a special space into many equal size cells and then computes the number of cells having solutions of the set. Some of them considers grid-like cells which partition the space into many hyperboxes, such as diversity metric (DM). ${ }^{51}$ QIs for all quality aspects cover convergence, spread, uniformity, and cardinality and they can be classified into two groups: distance-based QIs that measures the distance of PF to the solution set under consideration, such as inverted generational distance (IGD) ${ }^{2,52}$ and volume-based QIs that measures the size of volume and is specified by the consideration solution set in conjunction with some specifications, such as hypervolume (HV). ${ }^{53}$

# 5.3 | Parameter studies 

In this work, QIs of GD, PD, DM, HV, and IGD are applied to measure the performance on test instances F1 to F10 (most of whih are biobjective MOPs) and 500 uniformly distributed points are selected from the PF of each test instance to be $P^{*}$. Also, IGD and HV is applied to measure the performance on the three objective WFG test instances, and the reference point $y^{*}=(2.5,4.5,6.5)$ is used to for all instances.

## 5.4 | Parameter setting

For all the competing algorithms, the same parameter setting of problems is applied. Parameter adjustments for these compared algorithm as shown in Table 1. The population size is adjusted to 100 for proposed algorithm and IM-MEDA, RM-MEDA, and CSEA. We carried out 20 independent runs for each compared algorithm on each test instance. The final condition for each algorithm is adjusted to a maximum of 100000 fitness evaluations for all the test instances.

## 5.5 | Evaluation and comparison of algorithms

In this section, the performance of three proposed methods are compared with the IM-MOEA, ${ }^{11}$ that is to construct Gaussian process-based inverse model using the random grouping technique that map all found nondominated solutions from the objective space to the decision space, RM-MEDA, plan a reproduction operator by explicitly modeling the regularity in the distribution of Pareto optimal solutions and CSEA, use a artificial neural network in order to predict the dominance relationship between candidate solutions and reference solutions instead of approximating the objective values separately.

TABLE 1 Parameter settings of the four algorithms in comparison

| Algorithm | IM-MOEA- <br> RF-CV | IM-MOEA- <br> RF-Naive | IM-MOEA- <br> RF | IM-MOEA | RM- <br> MEDA | CSEA |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Parameter settings | $K=10$ | $K=10$ | $K=10$ | $K=10$ | $k=5$ | $k=5$ |

The Wilcoxon rank sum test is adapted to compare the results obtained by our proposed algorithm and the other four algorithms at an importance level of 0.05 . In the tables that summarize the statistical results, the first and second lines illustrate the mean values and the SDs, respectively. As a result of Wilcoxon rank sum test, a + labeled means that the compared algorithm is better than the proposed algorithm; by contrast, a - labeled means that the proposed algorithm is better than the compared algorithm; while $\mathrm{a} \approx$ labeled means that there is no statistically significant difference between the result obtained by the proposed algorithm and the compared algorithm.

# 5.6 | Results 

### 5.6.1 | The GD values

The GD indicator in Table 2 compares the statistical results of QIs for investigating of convergence on WFG1 to WFG9 that acquired by the six algorithms.

It can be illustrated that the convergence of the proposed algorithm (eg, IMMOEA-RF-CV, IMMOEA-RF-Naive, and IMMOEA-RF) on functions of WFG is better than CSEA, IM-MOEA, and RMMEDA. The IMMOEA-RF-CV is better than IMMOEA and RMMEDA in four cases and six cases, respectively. Also, IMMOEA-RF is better than both IM-MOEA and RM-MEDA in eight cases. Is is observed that the proposed algorithm is better than the CSEA. IMMOEA-RF-Naive has the best performance compared to all of the algorithms compared, as well as among the proposed algorithms. Therefore, the convergence rate of proposed is better than the other algorithms compared and the quadratic mean of the Euclidean distances of solutions set in proposed algorithms to the nearest point on the PF is better result than IM-MOEA in inversed modeling and CSEA in surrogate assisted evolutionary algorithms (SAEAs).

### 5.6.2 | The PD values

The PD indicator in Table 3 compares the statistical results of QIs for investigating of spread on function of IM-MOEA, that acquired by the six algorithms.

It can be illustrated that the spread of the proposed algorithm (eg, IMMOEA-RF-CV, IMMOEA-RF-Naive, and IMMOEA-RF) on IM-MOEA functions is better than IM-MOEA and RMMEDA, and CSEA. The IM-MOEA-RF has only a worse performance and in four cases than the IM-MOEA and the RMMEDA, respectively. The IMMOEA-RF-CV is better than the IMMOEA-RF-Naive in two cases and are equal in five cases and it is better than the IMMOEA-RF in only four cases and in fact the IMMOEA-RF is overall better than the IMMOEA-RF-CV. The comparison of two algorithms IMMOEA-RF-Naive and IMMOEA-RF shows that the IMMOEA-RF-Naive is better than the IMMOEA-RF in three cases and are equal in four cases. Also CSEA has weakest results among the algorithms compared. In general, the comparison of three algorithms (eg, IMMOEA-RF-CV, IMMOEA-RF-Naive, and IMMOEA-RF) shows that the IMMOEA-RF-Naive performs better than three other proposed methods in spread and has the least amount of the dissimilarity of each solution to the remaining solutions of a solution set.

![img-3.jpeg](img-3.jpeg)

![img-4.jpeg](img-4.jpeg)

# 5.6.3 | The DM values 

The DM indicator in Table 4 compares the statistical results of QIs for investigating of spread and uniformity on WFG1 to WFG9, that acquired by the six algorithms.

It can be illustrated that the spread and uniformity of the proposed algorithm (eg, IMMOEA-RF) on functions of WFG is better than the IMMOEA and RMMEDA in three and in four cases are equal. Also, the IMMOEA-RF is better than the IMMOEA-RF-CV and the IMMOEA-RF-Naive. Given that the spread rate of proposed methods is better, it can deduce that uniformity of IMMOEA-RF-CV and IMMOEA-RF-Naive are weaker than IMMOEA-RF, IMMOEA, RMMEDA, and CSEA, but uniformity of IMMOEA-RF is best in comparison of all compared algorithms.

### 5.6.4 | The HV values

The HV indicator in Table 5 compares the statistical results of QIs for investigating of all quality aspects (eg, convergence, spread, uniformity, and cardinality) on functions of IMMOEA, that acquired by the six algorithms. Also, Figure 4 shows the resulting HV curves of F1 to F9, in which the horizontal and vertical axes are test instances and HV values, respectively.

It can be illustrated that all quality aspects (eg, convergence, spread, uniformity, and cardinality) of the proposed algorithm (eg, IMMOEA-RF-CV, IMMOEA-RF-Naive, and IMMOEA-RF) on functions of IM-MOEA is better than the IM-MOEA, REMMEDA, and CSEA. So altogether, the proposed algorithm is better than IM-MOEA and in general. Also, the comparison of these three proposed methods illustrates that they have almost the same performance. In F6 and F8, which the RMMEDA has better performance, both function are nonlinear variable linkage and also F6 is nonuniformly distributed. The CSEA has weakest results among the algorithms compared.

Table 6 shows the statistical results of WFG1 to WFG9 that acquired by the six algorithms in terms of HV values on 104-D. Also, Figure 5 shows the resulting HV curves of WFG1 to WFG9, in which the horizontal and vertical axes are test instances and HV values, respectively.

It can be illustrated that the three proposed methods have the better overall performance and the best results are acquired by IMMOEA-RF-Naive on WFG2, WFG3, and WFG7. The IMMOEA-RF-CV and the IMMOEA have the same performance, but the IMMOEA-RF-CV has a better performance than the RMMEDA. Also the performance of CSEA is better than IM-MOEA and REMMEDA. The nondominated solutions resulting in the best HV among the 20 runs acquired by each algorithm on WFG7 are displayed in Figure 6.

On Figure 6, it is observed that solutions acquired by three proposed algorithms on WFG7 have better convergence and distribution than other compare algorithms, confirming the better performance illustrated by HV.

### 5.6.5 | The IGD values

Table 7 shows the statistical results of F1 to F10 that acquired by the six algorithms in terms of IGD values. Also, Figure 7 shows the resulting IGD curves of F1 to F9, in which the horizontal and vertical axes are test instances and IGD values, respectively.

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

FIGURE 4 Statistical results of hypervolume values obtained by each algorithm in comparison on 30-D F1 to F9 [Color figure can be viewed at wileyonlinelibrary.com]

- IMMOEA-RF-CV $\square$ IMMOEA-RF-Naive $\square$ IMMOEA-RF $\square$ IMMOEA $\square$ RMMEDA $\square$ CSEA

It can be illustrated that the three proposed methods have the better overall performance and the best result are acquired by IMMOEA-RF-Naive and IMMOEA-RF on F3, F4, F7, and F10 and F5, F8, and F9, respectively, which have strong linear and nonlinear correlations between the decision variables and highly multimodal test instances. The IMMOEA-RF-Naive and the IMMOEA-RF have a performance than the IMMOEA-RF-CV, but the IMMOEA-RF-CV has a better performance than the IM-MOEA and the RMMEDA. The CSEA has weakest results among the algorithms compared.

The IGD indicator in Table 8 compares the statistical results of QIs for investigating of all quality aspects (eg, convergence, spread, uniformity, and cardinality) on WFG1 to WFG9, that acquired by the five algorithms. Also, Figure 8 shows the resulting IGD curves of WFG1 to WFG9, in which the horizontal and vertical axes are test instances and IGD values, respectively. It can be illustrated that all quality aspects (eg, convergence, spread, uniformity, and cardinality) of three proposed algorithms (eg, IMMOEA-RF-CV, IMMOEA-RF-Naive, and IMMOEA-RF) on functions of WFG1 to WFG9 is better than the IMMOEA. In WFG1, the IMMOEA-RF-Naive and IMMOEA-RF are better than IMMOEA-RF-CV and RMMEDA has the worst performance. In WFG2 and WFG3 the performance of IMMOEA-RF-CV, IMMOEA-RF-Naive and IMMOEA-RF is better than IMMOEA and RMMEDA. In WFG4 the IMMOEA has the best performance and the RMMEDA has the worst performance. Also, the performance of three proposed algorithms is approximately equal to the IMMOEA. In WFG5 and WFG6 the IMMOEA-RF has the best performance. IN WFG7 and WFG8, the IMMOEA-RF-Naive has the best performance. In WFG9, IMMOEA-RF has the best performance and the performance of IMMOEA-RF-CV and IMMOEA-RF-Naive is approximately equal to the IMMOEA-RF. Also the performance of CSEA is better than IMMOEA and REMMEDA.

# 5.7 | Review of compared benchmarks 

Table 9 shows the relation ship of categories and benchmarks. In order to cover all categories, the behavior of HV and DM performance metrics is selected and evaluated on our test sets.

In order to evaluate the HV and DM for the six algorithms, the HV values of F2, F3, and WFG4 are shown in Figures 9, 10, and 11, respectively, and the DM values of F2, F3, and WFG4 are plotted in Figures 12, 13, and 14, respectively. By looking at the diagrams in Figures 4 and 5,

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

FIGURE 5 Statistical results of hypervolume values obtained by each algorithm in comparison on 104-D WFG1 to WFG9 [Color figure can be viewed at wileyonlinelibrary.com]
it can be seen that the three proposed algorithms perform better than the three compared algorithms in seven out of nine test functions in Figure 4, and in four out of nine test functions in Figure 5, which overall perform better about $61 \%$ in the HV performance metric. It can illustrate that convergence, spread and cardinality of three proposed algorithms is better than REMMEDA and CSEA. Also these proposed algorithms have better HV than IMMOEA. In these plots, the rate of HV on IMMOEA is weaker than the three proposed algorithms. Therefore the proposed algorithms have better performance than three comparison algorithms.

Also, it can illustrate that the spread and uniformity of three proposed algorithms are faster and better than IMMOEA, RMMEDA and CSEA and three proposed algorithms have similar DM rates. But according to diagram of DM and HV, it seem that the uniformity of these proposed algorithms is weaker than REMMEDA and CSEA. Also, according to the results shown in the tables, these proposed algorithms is suitable for large-scale problems in decision variables. In IMMOEA test instances the dimension of decision variables is equal to 30 and in WFG test instances the dimension of decision variables is equal to 104. The advantages and disadvantages of the proposed algorithms are shown in Table 10.

In general, it can illustrate that the convergence, spread and cardinality proposed algorithm is better than three compared algorithms, but the uniformity is not smooth. The reason why these parameters are better in the proposed algorithm than in IMMOEA is that in this algorithm, we replace three methods of random forest variable importance with random grouping in order to prevent the elimination of some effective inverse models and losing the chance of allocated decision variables, to other objective spaces randomly: the classical permutation variable importance random forest method, the random forest naïve variable importance method and random forest cross validation variable importance method. In addition, random grouping process, cannot determine the best assignment of $x_{n}$ to $f_{m}$ and its performance is based on random assignment. In fact, the importance of a variable $x_{n}$ in decision space for predicting $f_{m}$ is determined by random forest feature importance and variables are selected that are most importance. This paper proposes a new model-based on random forest, in order to determine the best assignment of $x_{n}$ to $f_{m}$. When the distribution of each gene $\left(x_{i}\right)$ over any of fitness functions $\left(f_{i}\right)$, are known, the best distributions can be select and it is not necessary to be assigned $x_{n}$ to $f_{m}$ randomly. On other hands, for decision variables assigned to the same group, their correlations can be implicitly increased by selecting the best distributions and the better HV criterion shows this. In the classical permutation variable importance random forest method, there is no natural cut off that can be discriminated important and nonimportant variables. Also, the predictor variables contain variables that do not

![img-10.jpeg](img-10.jpeg)

FIG URE 6 The nondominated solutions with the best hypervolume values obtained by each algorithm among 20 runs in the objective space on 104-D WFG7 [Color figure can be viewed at wileyonlinelibrary.com]

![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)
■IMMOEA_RF_CV ■IMMOEA_RF_Naive ■IMMOEA_RF ■IMMOEA ■RMMEDA ■CSEA

FIGURE 7 Statistical results of inverted generational distance values obtained by each algorithm in comparison on 30-D F1 to F9 [Color figure can be viewed at wileyonlinelibrary.com]
have their "own" effect on the response but are related to the response due to their relationship with truly influential predictor variables. Regarding the values variable importance, the negative values or values of zero, illustrate that variable does not improve the trees' predictive strength, because the error rates are similar or even larger when applying an unchanged version of the variable. In contrast, a positive value for the variable importance, express that the variable at least some improves the trees' predictive strength, because the error rates are smaller when applying the original version of the variable for deriving tree predictions. However it cannot be deduced that a positive value for the variable importance demonstrates a relative value. For this purpose, the random forest naïve variable importance method and random forest cross-validation variable importance method are suggested.

# 6 | CONCLUSIONS 

In this paper, an IM-MOEA with Random Forest (eg, IMMOEA-RF-CV, IMMOEA-RF-Naive, and IMMOEA-RF) has been proposed. The idea is to apply the process of random forest variable importance with a random grouping that determines the best assignment of $x_{n}$ to $f_{m}$ in inverse model process. The reason for using this process is that some of the effective inverse models may be removed randomly in IM-MOEA, while the feature importance of them that removed, may be higher than the values that selected. Also, random grouping assignment, removes the chance of allocated decision variables, to other objective spaces, while the decision variable $x_{n}$ maybe more feature importance for several $f_{n}$. In addition, IM-MOEA cannot determine the best assignment of $x_{n}$ to $f_{m}$ and its function is based on random assignment, while the random forests method can be used to identify predictor variables are the most important and termed as random forest feature importance. Using this method on IM-MOEA, that is, IM-MOEA-RF creates samples in the

![img-13.jpeg](img-13.jpeg)

![img-14.jpeg](img-14.jpeg)

- IMMOEA_RF_CV $\square$ IMMOEA_RF_Naive $\square$ IMMOEA_RF $\square$ IMMOEA $\square$ RMMEDA $\square$ CSEA

FIGURE 8 Statistical results of inverted generational distance values obtained by each algorithm in comparison on 104-D WFG1 to WFG9 [Color figure can be viewed at wileyonlinelibrary.com]

TABLE 9 Relationship of categories with the performance metrics

| Category | Performance Metrics |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | HV | IGD | DM | GD | PD | SP |
| Convergence | $\checkmark$ | $\checkmark$ |  | $\checkmark$ |  |  |
| Spread | $\checkmark$ | $\checkmark$ | $\checkmark$ |  | $\checkmark$ |  |
| Cardinality | $\checkmark$ |  |  |  |  |  |
| Uniformity |  |  | $\checkmark$ |  |  | $\checkmark$ |

Abbreviations: DM, diversity metric; HV, hypervolume; IGD, inverted generational distance; PD, pure diversity; SP, spacing.

FIGURE 9 The hypervolume value on F2 for six comparison algorithms [Color figure can be viewed at wileyonlinelibrary.com]
![img-15.jpeg](img-15.jpeg)

![img-16.jpeg](img-16.jpeg)

FIGURE 10 The hypervolume value on F3 for six comparison algorithms [Color figure can be viewed at wileyonlinelibrary.com]

FIGURE 11 The hypervolume value on WFG4 for six comparison algorithms [Color figure can be viewed at wileyonlinelibrary.com]

FIGURE 12 The diversity metric value on F2 for six comparison algorithms [Color figure can be viewed at wileyonlinelibrary.com]

FIGURE 13 The diversity metric value on F3 for six comparison algorithms [Color figure can be viewed at wileyonlinelibrary.com]
![img-17.jpeg](img-17.jpeg)

TABLE 10 The advantages and disadvantages of the proposed algorithms

## Advantages

Suitable for large-scale problems in decision variables.
It can determine the best assignment of $x_{n}$ to $f_{m}$ in regression model (in IM-MOEA, this process is randomize).

The best distributions of $x_{n}$ to $f_{m}$ can be selected in regression model.

Increase of their correlations.
The effective inverse models, have not be removed.
Increase rate of convergence,spread and cardinality.

## Disadvantages

The rate of uniformity performance metric is not better than compared algorithms, because the Gaussian distribution is more suitable for the exploitation stage owing to its narrow sampling range. Therefore in order to improve the uniformity performance, in future work, other distributions can be used, such as the Cauchy distribution along with the Gaussian distribution.

objective space in creating offspring, which is very convenient for generating solutions in preferred regions. The proposed method performs robustly competitive on a variety of test instances compared to four representative MOEAs, as long as the shapes of Pareto set are not too complex. The rate of uniformity performance metric is not better than compared algorithms, because the Gaussian distribution is more suitable for the exploitation stage owing to its narrow sampling range. Therefore in order to improve the uniformity performance, in future work, other distributions can be used, such as the Cauchy distribution along with the Gaussian distribution. The computational efficiency of proposed method is not ideal and it is worth further investigation to decrease the run time in solving small to medium optimization problems as future work. Also, its potential ability this method to solve many-objective optimization problems. The proposed method can be applied in the interdisciplinary fields for future research directions. Some of these are as follows: modeling and optimization of flexible manufacturing systems, ${ }^{54}$ visual analytics solution for scheduling processing phases, ${ }^{55}$ the number of out-of-cash ATMs and duration of out-of-cash status, ${ }^{56}$ optimization of hybrid wind and solar renewable energy system, ${ }^{57}$ optimization of parquetting of the concentrator of photovoltaic thermal module, ${ }^{58}$ verifying the gaming strategy of self-learning game, ${ }^{59}$ optimization of the process of anaerobic bioconversion of liquid organic wastes, ${ }^{60}$ efficiency optimization of indoor air disinfection by radiation exposure for poultry breeding. ${ }^{61}$

# ACKNOWLEDGMENTS 

Financial support from research office of Department of Computer, South Tehran Branch, Islamic Azad University is acknowledged.

## ORCID

Ali Broumandnia (2) https://orcid.org/0000-0001-5145-2013

## REFERENCES

1. Janitza S, Celik E, Boulesteix A-L. A computationally fast variable importance test for random forests for high-dimensional data. ADAC. 2018;12(4):885-915.
2. Zhang Q, Zhou A, Jin Y. RM-MEDA: a regularity model-based multiobjective estimation of distribution algorithm. IEEE Trans Evol Comput. 2008;12(1):41-63.
3. Krishnamoorthy Murugan, Suresh Sailakshmi, Alagappan Solaiappan. Deep learning techniques and optimization strategies in big data analytics: automated transfer learning of convolutional neural networks using Enas algorithm. Paper presented at: Proceedings of the Deep Learning Techniques and Optimization Strategies in Big Data Analytics. IGI Global; 2020:142-153.
4. Krejca Martin. Theoretical analyses of evolutionary algorithms with a focus on estimation of distribution algorithms. Proceedings of the 10th Ph. D. Retreat of the HPI Research School on Service-oriented Systems Engineering; 2018, Vol. 111:129.
5. Gao S, Silva CW. Estimation distribution algorithms on constrained optimization problems. Applied Mathematics and Computation. 2018;339:323-345.
6. Cheng R, He C, Jin Y, Yao X. Model-based evolutionary algorithms: a short survey. Complex Intell Syst. 2018;4(4):283-292.
7. Allmendinger R, Emmerich MTM, Hakanen J, Jin Y, Rigoni E. Surrogate-assisted multicriteria optimization: complexities, prospective solutions, and business case. J Multi-Criteria Decis Anal. 2017;24(1-2):5-24.
8. Jin Yaochu, Sendhoff Bernhard. Connectedness, regularity and the success of local search in evolutionary multi-objective optimization. Paper presented at: Proceedings of the 2003 Congress on Evolutionary Computation, 2003 CEC'03; 2003:1910-1917; IEEE.
9. Giagkiozis Ioannis, Fleming Peter J. Increasing the density of available Pareto optimal solutions; 2012.
10. Giagkiozis I, Fleming PJ. Pareto front estimation for decision making. Evol Comput. 2014;22(4):651-678.

11. Cheng R, Jin Y, Narukawa K, Sendhoff B. A multiobjective evolutionary algorithm using Gaussian process-based inverse modeling. IEEE Trans Evol Comput. 2015;19(6):838-856.
12. Schulz E, Speekenbrink M, Krause A. A tutorial on Gaussian process regression: modelling, exploring, and exploiting functions. J Math Psychol. 2018;85:1-16.
13. Ma X, Li X, Zhang Q, et al. A survey on cooperative co-evolutionary algorithms. IEEE Trans Evol Comput. 2018;23(3):421-441.
14. Khan N, Goldberg DE, Pelikan M. Multi-objective Bayesian optimization algorithm (IlliGAL Report No. 2002009). Urbana, IL: University of Illinois at Urbana-Champaign, Illinois Genetic Algorithms Laboratory; 2002.
15. Schwarz J, Ocenasek J. Multiobjective bayesian optimization algorithm for combinatorial problems: theory and practice. Neural Netw World. 2001;11(5):423-442.
16. Laumanns Marco, Ocenasek Jiri. Bayesian optimization algorithms for multi-objective optimization. Paper presented at: Proceedings of the International Conference on Parallel Problem Solving from Nature; 2002:298-307; Springer.
17. Zhong Xiaoping, Li Weiji. A decision-tree-based multi-objective estimation of distribution algorithm. Paper presented at: Proceedings of the 2007 International Conference on Computational Intelligence and Security (CIS 2007); 2007:114-11/8; IEEE.
18. Karshenas H, Santana R, Bielza C, Larranaga P. Multiobjective estimation of distribution algorithm based on joint modeling of objectives and variables. IEEE Trans Evol Comput. 2013;18(4):519-542.
19. Bosman PAN. Thierens Dirk. Multi-objective optimization with diversity preserving mixture-based iterated density estimation evolutionary algorithms. Int J Approx Reason. 2002;31(3):259-289.
20. Costa Mario, Minisci Edmondo. MOPED: a multi-objective parzen-based estimation of distribution algorithm for continuous problems. Paper presented at: Proceedings of the International Conference on Evolutionary Multi-Criterion Optimization; 2003:282-294; Springer.
21. Pelikan Martin, Sastry Kumara, Goldberg David E. Multiobjective HBOA, clustering and scalability. Tech. rep., Proceedings of the Genetic and Evolutionary; 2005.
22. Sastry Kumara, Goldberg David E, Pelikan Martin. Limits of scalability of multiobjective estimation of distribution algorithms. Paper presented at: Proceedings of the 2005 IEEE Congress on Evolutionary Computation; 2005:2217-2224; IEEE.
23. Pan L, He C, Ye T, Wang H, Xingyi Z, Yaochu J. A classification-based surrogate-assisted evolutionary algorithm for expensive many-objective optimization. IEEE Trans Evol Comput. 2018;23(1):74-88.
24. Jin Y. Surrogate-assisted evolutionary computation: recent advances and future challenges. Swarm Evol Comput. 2011;1(2):61-70.
25. Liu B, Zhang Q, Gielen GGE. A Gaussian process surrogate model assisted evolutionary algorithm for medium scale expensive optimization problems. IEEE Trans Evol Comput. 2013;18(2):180-192.
26. Li X, Yao X. Cooperatively coevolving particle swarms for large scale optimization. IEEE Trans Evol Comput. 2011;16(2):210-224.
27. Yang Z, Tang K, Yao X. Large scale evolutionary optimization using cooperative coevolution. Inf Sci. 2008;178(15):2985-2999.
28. Gee SB, Tan KC, Alippi C. Solving multiobjective optimization problems in unknown dynamic environments: an inverse modeling approach. IEEE Trans Cybern. 2016;47(12):4223-4234.
29. Tian Y, Wang H, Zhang X, Jin Y. Effectiveness and efficiency of non-dominated sorting for evolutionary multi-and many-objective optimization. Complex Intell Syst. 2017;3(4):247-263.
30. Louppe G, Wehenkel L, Sutera A, Geurts P. Understanding variable importances in forests of randomized trees. In: Burges CJC, Bottou L, Welling M, Ghahramani Z, Weinberger KQ, eds. Advances in neural information processing systems. Red Hook, NY: Curran Associates, Inc.; 2013:431-439.
31. Couronné R, Probst P, Boulesteix A-L. Random forest versus logistic regression: a large-scale benchmark experiment. BMC Bioinform. 2018;19(1):270.
32. Zhou Aimin, Zhang Qingfu, Zhang Guixu. A multiobjective evolutionary algorithm based on decomposition and probability model. Paper presented at: Proceedings of the 2012 IEEE Congress on Evolutionary Computation; 2012:1-8; IEEE.
33. Denisko D, Hoffman MM. Classification and interaction in random forests. Proc Natl Acad Sci. 2018;115(8):1690-1692.

34. Rasmussen CE. Gaussian processes in machine learning. Summer School on Machine Learning. New York, NY: Springer; 2003:63-71.
35. Wackernagel H. Multivariate Geostatistics: An Introduction with Applications. Berlin, Heidelberg / Germany: Springer Science \& Business Media; 2013.
36. Cressie N. Statistics for spatial data: Wiley series in probability and statistics Wiley-interscience. John Wiley and Sons, New York, NY 1993;15:105-209.
37. Barber D. Bayesian Reasoning and Machine Learning. Cambridge, MA: Cambridge University Press; 2012.
38. Rasmussen Carl Edward, Williams Christopher KI. Gaussian Processes for Machine Learning; 2006.
39. Freedman DA. Statistical Models: Theory and Practice. Cambridge, MA: Cambridge University Press; 2009.
40. Umlauf Nikolaus, Adler Daniel, Kneib Thomas, Lang Stefan, Zeileis Achim. Structured additive regression models: An R interface to BayesX. Working Papers in Economics and Statistics; 2012.
41. Do Chuong B. Gaussian Processes. Stanford University, Stanford, CA; 2017. Accessed December 5, 2007.
42. Pham H, Olafsson S. Bagged ensembles with tunable parameters. Comput Intell. 2019;35(1):184-203.
43. Singh PK, Sarkar R, Nasipuri M. Correlation-based classifier combination in the field of pattern recognition. Comput Intell. 2018;34(3):839-874.
44. Kohavi Ron. A study of cross-validation and bootstrap for accuracy estimation and model selection. Ijcai; 1995:1137-1145; Montreal, Canada.
45. James G, Witten D, Hastie T, Tibshirani R. An Introduction to Statistical Learning. New York, NY: Springer; 2013.
46. Huband S, Hingston P, Barone L, While L. A review of multiobjective test problems and a scalable test problem toolkit. IEEE Trans Evol Comput. 2006;10(5):477-506.
47. Li M, Yao X. Quality evaluation of solution sets in multiobjective optimisation: A survey. ACM Comput Surv (CSUR). 2019;52(2):26.
48. Van Veldhuizen David A, Lamont Gary B. Evolutionary computation and convergence to a pareto front. Paper presented at: Late Breaking Papers at the Genetic Programming 1998 Conference; 1998:221-228.
49. Wang H, Jin Y, Yao X. Diversity assessment in many-objective optimization. IEEE Trans Cybern. 2016;47(6):1510-1522.
50. Schott Jason R. Fault Tolerant Design Using Single and Multicriteria Genetic Algorithm Optimization No. AFIT/CI/CIA-95-039. Air force inst of tech Wright-Patterson afb OH; 1995.
51. Goli A, Zare HK, Tavakkoli-Moghaddam R, Sadegheih A. Multiobjective fuzzy mathematical model for a financially constrained closed-loop supply chain with labor employment. Comput Intell. 2019;36(1):4-34.
52. Zhou Aimin, Zhang Qingfu, Jin Yaochu, Tsang Edward, Okabe Tatsuya. A model-based evolutionary algorithm for bi-objective optimization. Paper presented at: Proceedings of the 2005 IEEE Congress on Evolutionary Computation; 2005:2568-2575; IEEE.
53. Deb K. Multi-Objective Optimization Using Evolutionary Algorithms. Hoboken, NJ: John Wiley \& Sons; 2001.
54. Lechuga, G. P., \& Sánchez, F. M. Modeling and optimization of flexible manufacturing systems: a stochastic approach. Paper presented at: Proceedings of the International Conference on Intelligent Computing \& Optimization; 2018:539-546; Springer.
55. Thomas J Joshua, Belaton Bahari, Khader Ahamad Tajudin. Visual analytics solution for scheduling processing phases. Paper presented at: Proceedings of the International Conference on Intelligent Computing \& Optimization; 2018:395-408; Springer.
56. Ozer Fazilet, Toroslu Ismail Hakki, Karagoz Pinar, Yucel Ferhat. Dynamic Programming Solution to ATM Cash Replenishment Optimization Problem. Paper presented at: Proceedings of the International Conference on Intelligent Computing \& Optimization; 2018:428-437; Springer.
57. Geleta Diriba Kajela, Manshahia Mukhdeep Singh. Optimization of hybrid wind and solar renewable energy system by iteration method. Paper presented at: Proceedings of the International Conference on Intelligent Computing \& Optimization; 2018:98-107; Springer.
58. Sinitsyn Sergey, Panchenko Vladimir, Kharchenko Valeriy, Vasant Pandian. Optimization of Parquetting of the Concentrator of Photovoltaic Thermal Module. Paper presented at: Proceedings of the International Conference on Intelligent Computing \& Optimization; 2019:160-169; Springer.
59. Zaw Hein Htoo, Hlaing Swe Zin. Verifying the gaming strategy of self-learning game by using PRISM-games. Paper presented at: Proceedings of the International Conference on Intelligent Computing \& Optimization; 2019:148-159; Springer.

60. Kovalev Andrey, Kovalev Dmitriy, Panchenko Vladimir, Kharchenko Valeriy, Vasant Pandian. Optimization of the process of anaerobic bioconversion of liquid organic wastes. Paper presented at: Proceedings of the International Conference on Intelligent Computing \& Optimization; 2019; :170-176; Springer.
61. Dovlatov Igor, Yuferev Leonid, Pavkin Dmitriy. Efficiency optimization of indoor air disinfection by radiation exposure for poultry breeding. Paper presented at: Proceedings of the International Conference on Intelligent Computing \& Optimization; 2019:177-189; Springer.

How to cite this article: Gholamnezhad P, Broumandnia A, Seydi V. An inverse model-based multiobjective estimation of distribution algorithm using Random-Forest variable importance methods. Computational Intelligence. 2020;1-39.
https://doi.org/10.1111/coin. 12315