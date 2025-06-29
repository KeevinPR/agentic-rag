# An Estimation of Distribution Algorithm With Filtering and Learning 

Lixin Tang ${ }^{\oplus}$, Senior Member, IEEE, Xiangman Song, Jiyin Liu ${ }^{\ominus}$, and Chang Liu ${ }^{\oplus}$, Member, IEEE


#### Abstract

Estimation of distribution algorithm (EDA) is an efficient population-based stochastic search technique. Since it was proposed, many attempts have been made to improve its performance in the context of nonlinear continuous optimization. However, the success of EDA depends on the accuracy of modeling, the effectiveness of sampling, and the ability of exploration. An effective EDA often needs to take some measures to adjust the model and to guide sampling. In this article, we propose a novel EDA which applies the idea of Kalman filtering to revise the modeling data and a learning strategy to improve sampling. The filtering scheme modifies the modeling data set using an estimation error matrix based on historic solution data. During the sampling process, the learning strategy determines the region to sample next based on the sampling outcomes so far, instead of completely random sampling. The proposed EDA also employs a multivariate probabilistic model based on copula function and can quickly reach the promising area in which the optimal solution is likely to be located. A collection of general benchmark functions are used to test the performance of the proposed algorithm. Computational experiments show that the EDA is effective.


Note to Practitioners-In many process industries, there exist black-box operation optimization problems and large-scale nonlinear optimization problems with variable coupling. For these problems, it is difficult to establish mechanism models between input and output. However, real-time data can be measured from the system through sensors. We can utilize this process information to optimize the system so as to attain the desired objective. In this article, we propose a novel estimation of distribution algorithm (EDA) which applies a filtering scheme

Manuscript received February 17, 2020; revised May 9, 2020; accepted June 5, 2020. Date of publication December 22, 2020; date of current version July 2, 2021. This article was recommended for publication by Associate Editor K. Liu and Editor S. A. Reveliotis upon evaluation of the reviewers' comments. This work was supported in part by the National Key Research and Development Program of China under Grant 2016YFB0901900, in part by the Major International Joint Research Project of the National Natural Science Foundation of China under Grant 71520107004, in part by the Major Program of National Natural Science Foundation of China under Grant 71790614, in part by the Fund for Innovative Research Groups of the National Natural Science Foundation of China under Grant 71621061, and in part by the 111 Project under Grant B16009. (Corresponding author: Lixin Tang.)
Lixin Tang is with the Key Laboratory of Data Analytics and Optimization for Smart Industry, Ministry of Education, Northeastern University, Shenyang 110819, China (e-mail: lixintang@mail.neu.edu.cn).
Xiangman Song is with the Liaoning Engineering Laboratory of Operation Analytics and Optimization for Smart Industry, State Key Laboratory of Synthetical Automation for Process Industries, Northeastern University, Shenyang 110819, China (e-mail: sxm123121@163.com).
Jiyin Liu is with the School of Business and Economics, Loughborough University, Loughborough LE11 3TU, U.K. (e-mail: j.y.liu@lboro.ac.uk).
Chang Liu is with the Liaoning Key Laboratory of Manufacturing System and Logistics, Northeastern University, Shenyang 110819, China (e-mail: lc1987328@126.com).
This article has supplementary downloadable material available at https://ieeexplore.ieee.org, provided by the authors.
Color versions of one or more of the figures in this article are available online at https://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TASE.2020.3019694
to revise the modeling data and a learning strategy to improve sampling, which can solve the problems with the characteristics of nonlinearity, variable coupling, and large scale. Computational experiments show that the EDA is effective. In the future, the proposed algorithm can be applied to some practical optimization problems such as operation optimization in blast furnace, which is considered as a continuous production process with variable coupling. The algorithm has the potential to help optimizing the process control parameters.

Index Terms-Estimation of distribution algorithm (EDA), filtering, learning sampling, multivariate probabilistic model.

## I. INTRODUCTION

INTELLIGENT algorithms have become very popular for solving optimization problems and are studied widely in the practical problems [1]-[4]. Estimation of distribution algorithms (EDAs) are evolutionary algorithms based on estimation and sampling from probabilistic models. The first EDA was developed by Mühlenbein and Paaß [5], and several improved EDAs have been proposed in recent years. Gaussian distribution is commonly used for modeling in continuous EDAs. Univariate Marginal Distribution Algorithm with Gaussian models for continuous domains (UMDA $\underset{\mathrm{G}}{\mathrm{G}}$ ) [6], the earliest proposed univariate Gaussian-based EDA, is easy to implement due to its ignoring the dependence of all variables. But it is difficult to solve problems in which the variables have strong dependence with each other. Estimation of Multivariate Normal Algorithm (EMNA ${ }_{\text {global }}$ ) [6] was proposed to overcome this. It used a conventional maximum likelihood estimated multivariate Gaussian distribution. Later, Eigenspace EDA (EEDA) [7] was proposed to improve the poor explorative capability. Besides, EDAs based on complex Gaussian distribution are proposed to solve multimodal and intractable problems. Some are with Gaussian mixture distribution [8]-[10]. Considering premature convergence of the traditional Gaussian EDAs, EDA ${ }^{2}$ was proposed to deal with it [11]. EDAs have also been used in hybrid algorithms. An algorithm combining Differential Evolution (DE) and EDA was proposed for the global continuous optimization problem [12], and it used an offspring generation scheme, which was similar to the DE crossover. For large-scale optimization problems, EDA with Model Complexity Control (EDA-MCC) [13] performed well using a specially designed multivariate model. Gaussian models can furnish useful information to search the optimal solution, but they cannot always provide an accurate distribution of promising solutions.

Increasingly, EDAs based on different models have been studied. With the capacity of describing arbitrary multimodality, the Histogram models in EDAs [14]-[18] are more flexible than Gaussian models. However, the complexity can be

increased with problem size on account of multiple variable dependencies [19]. Some EDAs can learn the structure and parameters of the model in each generation. The factorized distribution algorithm (FDA) [20] can extract a factorization structure from a priori knowledge of the problem. EDAs based on Bayesian networks [21] using directed acyclic graphical models can update local parameters according to the conditional probability distributions. Based on Markov random fields, Distribution Estimation using Markov random fields (DEUM) [22] presented a fitness modeling approach to estimating the parameters of the model. Clustering techniques [23] and other statistical methods, such as some variants of the expectation-maximization (EM) algorithm [24], have been used to learn mixtures of distributions in EDAs. These EDAs have given greater emphasis to the modeling structure. But the frameworks of these EDAs are all similar and the historic individual information has not been utilized fully.

In recent years, EDAs have been proposed to deal with many practical problems. A Pareto-based EDA was developed to solve a multiobjective flow-shop scheduling problem [25]. Using a mixed probability distribution model and an adaptive scheme, a new EDA was proposed to solve a multipolicy insurance investment problem [26].

In this article, a novel estimation of distribution algorithm with filtering and learning (EDA-FL) is proposed to solve continuous optimization problems more effectively. The contributions of our proposed algorithm are as follows.

1) A new EDA framework incorporating filtering is proposed. The idea of Kalman filtering is adopted to modify some individuals, which in turn affect the model, using an estimation error matrix from historic information.
2) A sampling strategy with learning is proposed. Using this strategy, the decision on where to sample is made according to the statistical information about the objective values of sampled individuals to avoid completely random sampling.
To illustrate the effectiveness, the proposed algorithm is tested through computational experiments on benchmark functions.

The rest of this article is organized as follows. Section II presents the background knowledge, including EDA, copulas, and Kalman filtering. Section III describes the fundamental ideas of the EDA-FL algorithm. Experimental studies are shown in Section IV. Finally, conclusions are given in Section V.

## II. BACKGROUND

## A. Estimation of Distribution Algorithm

EDA is an evolutionary algorithm that uses a probability model based on the distribution of good individuals in the current population to generate individuals of the next generation. The probability model also changes as the population evolves in the search process. Unlike in other evolutionary algorithms, in EDA, each individual in the new generation is not generated by mutation and crossover operations on the individuals of the old generation. Instead, the evolution is at the "macro" level. So, EDA emphasizes on the global information in the search process and has a strong exploration capability.

## Estimation of Distribution Algorithm

1: Set values of parameters; Set generation number $k=0$;
2: Randomly generate an initial feasible population Pop(0);
3: While stopping criterion is not satisfied Do
4: $\quad$ Select the best individuals from population Pop( $k$ );
5: $\quad$ Estimate a probability distribution;
6: $\quad$ Sample a number of individuals from the distribution
7: $\quad$ Combine the modeling individuals with the sampled individuals to form the new population $\operatorname{Pop}(k+1)$;
8: $\quad$ Increment generation number $k=k+1$;
9: End while
Fig. 1. Pseudo-code of EDA.
EDA works iteratively, as shown in Fig. 1, where Pop represents population or a set of individuals. In this article, we use bold capital letters for matrices or populations, e.g., $\mathbf{A}$ and Pop ${ }^{\text {mod }}$. Vectors and individuals are represented by lowercase bold characters, e.g., $\mathbf{u}$ and $\mathbf{x}_{\text {best }}$. The main steps of EDA are described as follows.

1) Selection: Selection aims to obtain a set of good individuals from the current population. It is expected that the selected individuals can describe the solution space accurately and comprehensively. The most widely used selection method is the truncation selection.
2) Modeling: Using a statistical method, the probabilistic model is constructed based on the relevant statistical information extracted from the selected individuals.
3) Sampling: In the sampling step, a set of individuals called sampled individuals is generated from the constructed probabilistic model. The sampling method is dependent on the modeling method used.
4) Combination: In every generation, the offspring population is often obtained by combining the modeling individuals and sampled individuals. In addition, individuals generated randomly according to the uniform distribution in the search space can also be added into the offspring population. The commonly used stopping criterion is the number of fitness evaluations ( $n-F E s$ ) reaching a predefined maximum value.

## B. Copulas

A concise definition of copulas is given in [27]: a copula is a multivariate probabilistic distribution function $C(\bullet)$ of $D$-dimensional random vector $\mathbf{u}=\left(u_{1}, \ldots, u_{D}\right)$ on the unit hypercube $[0,1]^{D}$ with some properties. As can easily be seen, the most well-known copula is the independence distribution function

$$
C\left(u_{1}, \ldots, u_{D}\right)=\prod_{i=1}^{D} u_{i}
$$

There are two important copulas, which are interesting in practical applications, namely, Gaussian-copula and empiricalcopula. Their marginal distributions are Gaussian and empirical distributions, respectively. Other copulas include $t$-copula, Clayton-copula, Gumbel-copula, and Frank-copula [27].

The key theorem was introduced by Nelsen [28] to separate the effect of dependence from the effect of marginal distributions in a copula.

For a $D$-dimensional random vector $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{D}\right)$, its joint distribution function being $F(\mathbf{x})$ with the marginal distributions $u_{d}=F_{d}\left(x_{d}\right), d=1, \ldots, D$, there exists a copula $C(\mathbf{u})$, which is a multivariate distribution function of vector $\mathbf{u}=\left(u_{1}, u_{2}, \ldots, u_{D}\right)$ in $[0,1]^{D}$. The following equality was set up and the proof was given in [28]:

$$
\begin{aligned}
C\left(u_{1}, \ldots, u_{d}\right) & =F\left(x_{1}, \ldots, x_{d}\right) \\
& =F\left(F_{1}^{-1}\left(u_{1}\right), \ldots, F_{d}^{-1}\left(u_{d}\right)\right)
\end{aligned}
$$

where $F_{d}^{-1}\left(u_{d}\right)=\sup \left\{x_{d} \mid F_{d}\left(x_{d}\right) \leq u_{d}\right\}$.
With the analysis above, each $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ can be generated in two steps. The first step is to generate a random vector $\mathbf{u}=\left(u_{1}, u_{2}, \ldots, u_{D}\right)$ with the copula function. In the second step, vector $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ is generated using the common inverse function of the marginal distribution of each variable, i.e., $x_{d}=F_{d}^{-1}\left(u_{d}\right), d=1, \ldots, D$.

In recent years, many EDAs using copulas as probabilistic models (copula-EDAs) have been proposed. Based on the copula theory, a framework of EDA was proposed in [29] to solve 2-D optimization problems. Archimedean-copula, Gumbel-copula, and Gaussian-copula have all been used in multivariate EDAs [30]-[34], which were tested on problems of low dimensions in small scale experiments. The maximum likelihood estimation was used in a copula-EDA to estimate the parameters of copula [35]. An EDA based on Gaussian copulas was proposed in [36] to solve multiobjective problems and applied to RFID network planning. An EDA using multivariate extension of the Archimedean copula was presented in [37]. A hybrid algorithm was proposed in [38] combining Archimedean copula-based EDA and artificial bee colony algorithm to achieve faster convergence. A new EDA based on parallel copula was also proposed to improve the efficiency [39]. These algorithms were tested on a small number of benchmark functions. To deal with the major drawbacks, including too much emphasis on parameters and premature convergence, a new EDA based on multivariate elliptical copulas was presented, where the parameters were estimated and a population diversity technique was used [40]. EDAs have also been applied to solve problems in practical settings. For example, an EDA was proposed in [41] to solve problems involving various types of constraints, while EDAs were applied in [42] and [43] to solve flow-shop scheduling problems.

## C. Kalman Filtering Process

Kalman filtering [44] is a recursive estimator that uses a series of predictions and observations to make estimation of unknown variables.

For a discrete-time linear system, Kalman filtering model is used to predict the true state $\mathbf{x} \in \mathbb{R}^{n}$ at time $k$ from the state at $(k-1)$ according to a linear stochastic difference equation

$$
\mathbf{x}(k)=\mathbf{A} \mathbf{x}(k-1)+\mathbf{B} \boldsymbol{\vartheta}(k)+\mathbf{w}(k)
$$

## The Kalman filtering process

1: Set initial values $\mathbf{x}(0)$ and $\mathbf{P}(0)$ for state variable and error covariance; Set generation number $k=1$.
2: While stopping criterion is not satisfied Do
3: $\quad$ Predict:
Project the state ahead $\mathbf{x}^{-}(k)$;
Project the error covariance ahead $\mathbf{P}^{-}(k)$;
4: Observe and Revise:
Compute the gain $\mathbf{g}(k)$;
Update the state $\mathbf{x}(k)$;
Update the error covariance $\mathbf{P}(k)$;
$k=k+1$
5: End while
Fig. 2. Kalman filtering process.
At time $k$ an observation $\mathbf{y} \in \mathbb{R}^{m}$ of the true state is given by

$$
\mathbf{y}(k)=\mathbf{H} \mathbf{x}(k)+\mathbf{v}(k)
$$

where $\mathbf{A}$ is the state-transition matrix which is applied to the previous state, $\mathbf{B}$ is the coefficient matrix for the control input $\boldsymbol{\vartheta} \in \mathbb{R}^{l}, \mathbf{H}$ is known as the observation matrix, $\mathbf{w}(k)$ is the process noise, and $\mathbf{v}(k)$ is observation noise.

The Kalman filtering process can be described in Fig. 2, where $\mathbf{x}^{-}(k)$ is the predicted state, $\mathbf{P}^{-}(k)$ is the predicted error covariance, $\mathbf{g}(k)$ is the Kalman gain, $\mathbf{x}(k)$ is the revised state, and $\mathbf{P}(k)$ is the posteriori error covariance. $\mathbf{x}(0)$ and $\mathbf{P}(0)$ are the initial values of the state variable and the error covariance, respectively.

In this article, we construct the new EDA framework through prediction, sampling, and revision operations using the idea of Kalman filtering.

## III. PROPOSED AlGORITHM

## A. New EDA Framework Incorporating Filtering

In essence, an optimization problem can be viewed as a system. The solution process of the optimization problem can then be considered as the process of searching for the ideal state of the system guided by observation, for which Kalman filtering is an effective technique. Muruganantham et al. [45] have proposed a new dynamic multiobjective optimization evolutionary algorithms using Kalman filtering, in which a prediction model is designed to learn patterns from past data. In our new EDA, we transform the best individuals in the last population to make predictions of the optimal solution. A set of the best individuals among those in the last population as well as the predicted individuals are then used for modeling. The samples generated can be considered as observed solutions. To improve the accuracy of the solution, having been inspired by the Kalman filtering process, we revise some individuals based on the difference between the predicted and observed data. The revision in turn affects the set of individuals for modeling in the next generation (iteration). Hopefully, this can improve the effectiveness of the model and thus the EDA process. Our new EDA framework with filtering can be outlined as Fig. 3. In the framework, $\operatorname{Pop}(k)$ is the

```
Algorithm 1. Overall Framework of the New EDA
    Input: a stopping criterion;
        D: dimension of problem; \(N P\) : size of population;
        \(\alpha\) : proportion of population used for modeling;
        \(k_{\text {max }} ;\) maximum number of iteration;
        \(\boldsymbol{m}\) : maximum number of iterations without improvement;
        \(n-F E s\) : predefined number of fitness evaluations.
    Output: the best solution for optimization problem.
    /* Construct initial population \(\operatorname{Pop}(0) . * /\)
    \(\operatorname{Pop}(0)=\) INITIALIZATION \((D, N P)\);
    \(k=1 ; / / k\) is the generation counter.
    /* Select a set of modeling individuals, \(\operatorname{Pop}^{\text {mod }}(1)\),
    take the best individual \(\mathbf{x}_{\text {pchext }}(1)\) in \(\operatorname{Pop}^{\text {mod }}(1) . * /\)
    \(\operatorname{Pop}^{\text {mod }}(1)=\operatorname{SELECT}\left(\alpha^{*} N P, \operatorname{Pop}(0)\right)\);
    \(\mathbf{x}_{\text {pchext }}(1)=\operatorname{BEST}\left(\operatorname{Pop}^{\text {mod }}(1)\right)\);
    \(C_{i}(u)=\operatorname{MODEL}\left(\operatorname{Pop}^{\text {mod }}(1)\right) ; / /\) modelling.
    \(\operatorname{Pop}^{\text {sum }}(1)=\operatorname{SAMPLE}\left((1-\alpha) * N P, C_{i}(u)\right) ; / /\) sample (observe).
    /* Form a new population. */
    \(\operatorname{Pop}(1)=\operatorname{COMBINE}\left(N P, \operatorname{Pop}^{\text {mod }}(1), \operatorname{Pop}^{\text {sum }}(1)\right)\);
    /* Calculate error matrix \(\mathbf{P}(1)\) using \(\mathbf{x}_{\text {pchext }}(1)\) and the
    best \(D\) individuals in \(\operatorname{Pop}^{\text {sum }}(1) . * /\)
    \(\mathbf{P}(1)=\operatorname{CAL}\left(\mathbf{x}_{\text {pchext }}(1), \operatorname{Pop}^{\text {sum }}(1)\right)\);
    \(k=2\);
    /* Main loop. */
    While the stopping criterion is not satisfied do
        /* Make NP predictions of the optimal solution. */
        \(\operatorname{Pop}^{\text {pre }}(k)=\operatorname{PREDICT}(N P, \operatorname{Pop}(k-1)) ; / / \text { predict. }\) $\mathbf{x}_{\text {pchext }}(k)=\operatorname{BEST}\left(\operatorname{Pop}^{\text {pre }}(k) \cup \operatorname{Pop}(k-1)\right) ;$
    /* Select the best \(\alpha^{*} N P\) individuals from \(\operatorname{Pop}^{\text {pre }}(k)\),
    and \(\operatorname{Pop}(k-1)\) and \(\operatorname{Pop}^{\text {pre }}(k-1)\), use these for modeling.
    */
        \(\operatorname{Pop}^{\text {mod }}(k)=\operatorname{SELECT}\left(\alpha^{*} N P, \operatorname{Pop}(k-1) \cup \operatorname{Pop}^{\text {pre }}(k-1)\right.\)
        \(\left.\cup \operatorname{Pop}^{\text {pre }}(k)\right)\);
        \(C_{k}(u)=\operatorname{MODEL}\left(\operatorname{Pop}^{\text {mod }}(k)\right)\);
        \(\operatorname{Pop}^{\text {sum }}(k)=\operatorname{SAMPLE}\left((1-\alpha) * N P, C_{k}(u)\right) ; / /\) observe.
        \(\operatorname{Pop}(k)=\operatorname{COMBINE}\left(N P, \operatorname{Pop}^{\text {mod }}(k), \operatorname{Pop}^{\text {sum }}(k)\right)\);
        /* Calculate error gain vector. */
        \(\mathbf{g}(k)=\operatorname{GAIN}\left(\mathbf{P}(k-1), \mathbf{x}_{\text {pchext }}(k-1), \operatorname{Pop}^{\text {sum }}(k-1)\right) ;\)
        /* Revise some of the individuals. */
        \(\operatorname{Pop}^{\text {pre }}(k)=\operatorname{REVISE}\left(\operatorname{Pop}^{\text {pre }}(k), \operatorname{Pop}^{\text {sum }}(k)\right) ;\)
        /* Calculate the error matrix \(\mathbf{P}(k) . * /\)
        \(\mathbf{P}(k)=\operatorname{CAL}\left(\mathbf{x}_{\text {pchext }}(k), \operatorname{Pop}^{\text {sum }}(k)\right)\);
        Set \(k=k+1\).
    End while
```

Fig. 3. New EDA framework with filtering.
population of iteration $k ; \operatorname{Pop}^{\text {mod }}(k), \operatorname{Pop}^{\text {sum }}(k), \operatorname{Pop}^{\text {pre }}(k)$, and $\operatorname{Pop}^{\text {pre }}(k)$ are the sets of modeling, sampled, predicted, and revised individuals, respectively. The names of functions are in capitals and their meanings are obvious.

In each iteration of this framework, the basic EDA steps are listed in normal font. In this article, we introduce a learning strategy to improve the sampling step. The details of the strategy will be presented in Section III-B. We incorporate the idea of Kalman filtering in the framework and the steps related
to filtering are indicated in italic. The EDA search process is clearly not a linear system, thus the same linear transformations used in Kalman filtering for linear systems cannot be directly applied. By defining new error matrix and gain vector based on individuals and their objective values in the EDA process, we propose to use different forms of transformation (still keeping linear) here to achieve similar purpose to those in linear systems. The filtering steps embedded in the EDA framework include prediction, observation, and updating of the gain vector and error matrix. Details are given below in the description of the relevant steps.

1) Initialization and the First Iteration: The function $\operatorname{Pop}(0)=$ INITIALIZATION $(D, N P)$ in Step 1 of the framework initializes the algorithm, which is generating an initial population of $N P$ individuals by drawing the $D$-dimension variable values randomly from uniform distributions over their search ranges. The algorithm then starts iterations.

The first iteration $(k=1)$ is presented separately in the framework (steps 2-7) because some filtering operations need information from previous iteration and so need to be done differently or cannot be done in the first iteration. The main operations in later iterations $(k>1)$ are presented in steps $9-19$ of the framework. The first iteration of the new EDA framework includes two filtering operations, observation (in step 5) and error matrix $\mathbf{P}(k)$ calculation (step 7), which enable the other filtering operations in the next iterations.

To calculate $\mathbf{P}(k)$, we first find the best individual $\mathbf{x}_{\text {pchest }}(k)$ in the population using function $\operatorname{BEST}(\bullet)$ (steps 3 and 10), and select the best $D$ individuals among the sampled ones. $\mathbf{P}(k)$ is then calculated as a $D \times D$ matrix with each row being the difference between one of these $D$ individuals and the best individual $\mathbf{x}_{\text {pchest }}(k)$

$$
\begin{aligned}
& \mathbf{P}(k) \\
& =\left[\begin{array}{ccc}
p_{11}(k) & \ldots & p_{1 D}(k) \\
\cdots & \cdots & \cdots \\
p_{D 1}(k) & \ldots & p_{D D}(k)
\end{array}\right] \\
& =\left[\begin{array}{ccc}
x_{\text {pchest }, 1}(k)-z_{1,1}(k) & \ldots & x_{\text {pchest }, D}(k)-z_{1, D}(k) \\
\cdots & \cdots & \cdots \\
x_{\text {pchest }, 1}(k)-z_{D, 1}(k) & \ldots & x_{\text {pchest }, D}(k)-z_{D, D}(k)
\end{array}\right]
\end{aligned}
$$

where $\mathbf{z}_{\mathbf{i}}(k)=\left[z_{i, 1}(k), z_{i, 2}(k), \ldots, z_{i, D}(k)\right], i=1, \ldots, D$, are the best $D$ sampled individuals in $\operatorname{Pop}^{\text {sum }}(k)$. In this step, the error matrix $\mathbf{P}$ is calculated in $O\left(D^{2}\right)$ time.
2) Prediction (Step 10): The optimal solution is predicted by transforming the best individual in the population $\operatorname{Pop}(k-1)$ plus some noise represented by the difference of two randomly selected individuals in the population. This is expressed in the following formula. Function PREDICT( $N P$, $\operatorname{Pop}(k-1))$ in Fig. 3 generates $N P$ predicted solutions in this way and stores them in $\operatorname{Pop}^{\text {pre }}(k)$

$$
\mathbf{x}_{\mathbf{i}}^{-}(k)=\mathbf{A} \mathbf{x}_{\text {best }}(k-1)+\mathbf{A}\left[\mathbf{x}_{\mathbf{a}}(k-1)-\mathbf{x}_{\mathbf{b}}(k-1)\right]
$$

where $\mathbf{x}_{\mathbf{i}}^{-}(k), i=1, \ldots, N P$, is a predicted solution. $\mathbf{A}$ is identity matrix, $\mathbf{x}_{\text {best }}(k-1)$ is the best individual, $\mathbf{x}_{\mathbf{a}}(k-1)$ and $\mathbf{x}_{\mathbf{b}}(k-1), a \neq b$, are two random individuals in the last population $\operatorname{Pop}(k-1)$. To guarantee diversity of predictions,

![img-0.jpeg](img-0.jpeg)

Fig. 4. Obtaining $x_{d}$ from $u_{d}$ using inverses of the distribution.
$\mathbf{A}$ is set to be a diagonal matrix. $p_{0}$ proportion of the diagonal elements of $\mathbf{A}$ are randomly generated from the uniform distribution $U[0,1]$, while all the other diagonal elements are the same with a value between 0 and 1 . Each of $N P$ predicted solutions needs $O(D)$ steps for generating $D$ elements, so this is done in $O(D * N P)$ time.
3) Selection: In steps 3 and 11, the $\alpha$ proportion $(\alpha<1)$ of the best individuals is selected according to their objective function values. Hence, $s=\alpha * N P$ denotes the number of the selected individuals for modeling. In step 11 (iteration 2 onward), the best $\alpha * N P$ are selected among individuals in the population as well as the revised and predicted individuals.
4) Modeling (Steps 4 and 12): Modeling is designed to establish the probability distribution of optimal solution using the selected set of solutions. For all individuals $\mathbf{x}_{\mathbf{i}}=\left(x_{i, 1}\right.$, $\left.x_{i, 2}, \ldots, x_{i, D}\right), i=1, \ldots, s$, in Pop ${ }^{\text {mod }}$, we first sort their elements in each dimension $d$ and denote the $i$ th smallest element in dimension $d$ as $x_{(i), d}, i=1, \ldots, s ; d=1, \ldots, D$. With this information we then calculate $\mathbf{u}=\left(u_{1}, \ldots, u_{d}, \ldots, u_{D}\right)$ as follows. Fig. 4 shows the marginal distribution $F_{d}\left(x_{d}\right)$ being a mixture of empirical distribution and Gaussian distribution, which is a piecewise function. This model allows sample individuals to be outside the area of modeling individuals, which enhances the ability of exploration

$$
\left\{\begin{aligned}
u_{d}\left(x_{(i), d}\right)= & F\left(x_{(1), d}\right)+(i-1) *\left[F\left(x_{(s), d}\right)-F\left(x_{(1), d}\right)\right] /(s-1) \\
& i=1, \ldots, s \\
& F\left(x_{(\cdot), d}\right)= & P\left(x \leq x_{(\cdot), d}, x \sim N\left(\bar{x}, \sigma^{2}\right)\right) \\
& x_{(\cdot), d} \leq x_{(1), d} \text { or } x_{(\cdot), d} \geq x_{(s), d}
\end{aligned}\right.
$$

Each selected individual corresponds to a point in $u$ space. Meanwhile, we divide interval $[0,1]$ into $K$ partitions $S_{1}, \ldots, S_{K}$, and the length of each partition $\delta=1 / K$. So there are $K^{D}$ subcubes. Then the copula density function is defined as

$$
c\left(u_{1}, \ldots, u_{D}\right)=N_{j} / s / \delta^{D}, \quad j \in\left\{S_{1}, \ldots, S_{K}\right\}^{D}
$$

where $N_{j}$ denotes the number of points in certain subcube $j$. As remarked in [46], this step has a time complexity of $\mathrm{O}(D *$ $s * \log s)$.
5) Sampling (Steps 5 and 13): The distribution model in the last step is used to generate $(1-\alpha) * N P$ individuals.

This sampling operation of EDA here also serves as observation operation for filtering. The objective function value of a sampled individual, $f(\mathbf{x})$, can be viewed as a value of the observation variable $\mathbf{y}$ in Kalman filtering. In this article, the method of an interpolation is used as the inverses of the distribution to generate the individual $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{D}\right)$. We first generate a vector $\mathbf{u}=\left(u_{1}, u_{2}, \ldots, u_{D}\right)$. Here, $u_{1}$ is a random variate from the uniform distribution on interval $[0,1]$, while $u_{d}, d=2, \ldots, D$, is generated with the conditional distribution function $C_{d}\left(u_{d} \mid u_{1}, \ldots, u_{d-1}\right)$ considering the relation $C_{d}\left(u_{d} \mid u_{1}, \ldots, u_{d-1}\right)=u_{d}^{*}$, where $u_{d}^{*}, d=2, \ldots, D$, is a random number generated from the uniform distribution on $(0,1]$. For a generated $u_{d}$ that falls in the interval between $u_{d}\left(x_{(i), d}\right)$ and $u_{d}\left(x_{(i+1), d}\right)$, the corresponding $x_{d}$ is in the interval between $x_{(i), d}$ and $x_{(i+1), d}, i=1, \ldots, s-1$, and can be calculated using interpolation as follows:

$$
x_{d}=\left\{\begin{array}{l}
x_{(L), d}, \quad \text { if } u_{d} \leq F\left(x_{(L), d}\right) \\
x_{(L), d}+\left(x_{(1), d}-x_{(L), d}\right)\left(u_{d}-F\left(x_{(L), d}\right)\right) / \\
\left(u_{d}\left(x_{(1), d}\right)-F\left(x_{(L), d}\right)\right) \\
\quad \text { if } F\left(x_{(L), d}\right)<u_{d} \leq u_{d}\left(x_{(1), d}\right) \\
x_{(i), d}+\left(x_{(i+1), d}-x_{(i), d}\right)\left(u_{d}-u_{d}\left(x_{(i), d}\right)\right) / \\
{\left[F^{\prime} /(s-1)\right]} \\
\quad \text { if } u_{d}\left(x_{(i), d}\right)<u_{d} \leq u_{d}\left(x_{(i+1), d}\right), \\
i=1, \ldots, s-1 \\
x_{(s), d}+\left(x_{(U), d}-x_{(s), d}\right)\left(u_{d}-u_{d}\left(x_{(s), d}\right)\right) / \\
\left(F\left(x_{(U), d}\right)-u_{d}\left(x_{(s), d}\right)\right) \\
\quad \text { if } u_{d}\left(x_{(s), d}\right)<u_{d} \leq F\left(x_{(U), d}\right) \\
x_{(U), d}, \quad \text { if } F\left(x_{(U), d}\right)<u_{d}
\end{array}\right.
$$

where

$$
F^{\prime}=u_{d}\left(x_{(s), d}\right)-u_{d}\left(x_{(1), d}\right)
$$

In this step, a random vector $\mathbf{x}$ is generated in $O(D * \log K)$ time. The sampled individuals are then combined with the modeling individuals to form a new population (steps 6 and 14).
6) Calculating the Gain Vector (Function GAIN( $\boldsymbol{\sim}$ ) in Step 15): The gain vector $\mathbf{g}(k)$ is a $D$-dimensional vector with each element being the average error weight of an individual in a specific dimension relative to the error of the objective value. Using $\mathbf{P}(k-1), g_{d}(k), d=1, \ldots, D$, is calculated as follows in (10), shown at the bottom of the next page, where $\mathbf{P}(k-1)$ is the error matrix, $f\left(\mathbf{z}_{\mathbf{i}}(k-1)\right)$ and $f\left(\mathbf{x}_{\text {pchest }}(k-1)\right)$ are the objective values of $\mathbf{z}_{\mathbf{i}}(k-1)$ and $\mathbf{x}_{\text {pchest }}(k-1)$, respectively. This step has a time complexity of $O(D)$.
7) Revision: Employing the error gain vector, the revised individuals can be obtained in step 16 (function REVISE $(\bullet)$ ) using the following formulas. The meaning of the above-defined gain vector makes the revision operation linear

$$
\begin{aligned}
\overline{\mathbf{x}}_{\mathbf{i}}(k) & =\mathbf{x}_{\mathbf{i}}(k)+\mathbf{g}(k)\left[f\left(\mathbf{z}_{\text {best }}(k)\right)-f\left(\mathbf{x}_{\mathbf{i}}(k)\right)\right] \\
\overline{\mathbf{x}}_{\text {pchest }}(k) & =\mathbf{x}_{\text {pchest }}(k)+\mathbf{g}(k)\left[f\left(\mathbf{z}_{\text {best }}(k)\right)-f\left(\mathbf{x}_{\text {pchest }}(k)\right)\right] \\
\overline{\mathbf{z}}_{\mathbf{i}}(k) & =\mathbf{z}_{\mathbf{i}}(k)+\mathbf{g}(k)\left[f\left(\mathbf{x}_{\text {pchest }}(k)\right)-f\left(\mathbf{z}_{\mathbf{i}}(k)\right)\right]
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)

Fig. 5. Influence on modeling individuals by predicting and revising.
where $\mathbf{x}_{\mathbf{i}}(k), i=1, \ldots, N P_{1}$, is the best $N P_{1}$ individuals among the predicted individuals and those in the population $\operatorname{Pop}(k-1) . \mathbf{z}_{\mathbf{i}}(k), i=1, \ldots, N P_{2}$, is the best $N P_{2}$ individuals of the sampled individuals, $\mathbf{z}_{\text {best }}(k)$ is the best sampled individual. $N P_{1}=p_{1} * \alpha * N P$ and $N P_{2}=p_{2} * \alpha * N P$ are determined by selecting the values of parameters $p_{1}(<1)$ and $p_{2}(<1) . \overline{\mathbf{x}}_{\mathbf{i}}(k), \overline{\mathbf{x}}_{\text {pcbest }}(k)$ and $\overline{\mathbf{z}}_{\mathbf{i}}(k)$ are the revised individuals of $\mathbf{x}_{\mathbf{i}}(k), \mathbf{x}_{\text {pcbest }}(k)$ and $\mathbf{z}_{\mathbf{i}}(k)$, respectively. $\mathbf{x}_{\text {pcbest }}(k)$ is obtained in steps 3 and 10 of Algorithm 1. Formula (12) is a special case of (11). The calculations in (11) and (13) generate the revised individuals in $O\left(N P_{1} * D+N P_{2} * D\right)$ time.
8) Calculating Error Matrix: The error matrix is calculated in step 17 (function CAL( $\bullet$ )), using (5).

Overall, in the new EDA framework, we introduced two distinct operations "Predict" and "Revise" which do not exist in the traditional EDA. The potential advantage of this is illustrated in Fig. 5, where the red asterisk represents the optimal solution. As iteration goes on, the individuals in the population may tend to concentrate in a small area. In this case it is difficult for the traditional EDA to evolve further even though the optimal solution is still far away from this area. The prediction and revision operations in the new EDA generate new solutions. The predicted and revised individuals as illustrated in Fig. 5 not only tend to be closer to the optimal solution but also increase the diversity of the population and so makes it evolve further.

## B. Learning Sampling Strategy

The process of EDA takes a long time to reach a good final solution if the sampling is completely random. To search the solution space more efficiently, we use the idea of optimal learning (see [47]) in the sampling process of each generation, i.e., after an initial set of individuals is sampled randomly, each new individual is sampled in a promising region which is determined using the existing individuals. Using learning techniques to improve optimization process becomes popular in recent years. These techniques often consider the special
![img-2.jpeg](img-2.jpeg)

Fig. 6. Four selections of $\left(u_{1}^{*}, u_{2}^{*}\right)$.
features of the optimization problem being solved. For example, in the process of solving a premarshaling problem in [48], a learning model is used to choose the next move. We use optimal learning to improve the sampling process of EDA as a general optimization method.

In the EDA based on copula function, because of the randomization of $u_{1}$ and $u_{d}^{*}, d=2, \ldots, D$, we need sample large number of individuals to get a sufficiently good solution. Trying to improve this, we divide the whole sampling range of each dimension into multiple intervals, from which the vector $\mathbf{u}^{*}=\left(u_{1}^{*}, u_{2}^{*}, \ldots, u_{D}^{*}\right)$ can be generated, where $u_{1}^{*}$ is defined as $u_{1}$ for convenience. Now we divide the range $[0,1]$ into $M$ equal intervals. So the length $L$ of each interval equals $1 / M$. Then $u_{d}^{*}$ can be generated from $M$ alternative intervals $((j-1) \times L, j \times L], j=1, \ldots, M$. Note that the first interval for $u_{1}$ also includes 0 . Consider a simple example with $D=2, M=2$, denote $b:=(0,0.5]$ and $c:=(0.5,1]$. So $\left(u_{1}^{*}, u_{2}^{*}\right)$ can be obtained from four alternative regions: $b b, b c, c b$, and $c c$, as shown in Fig. 6. We can select each region for $\left(u_{1}^{*}, u_{2}^{*}\right)$ and then sample individuals accordingly. Fig. 7 shows the individuals generated when $\left(u_{1}^{*}, u_{2}^{*}\right)$ are sampled from different regions. The axes in Fig. 7 represent the decision variables for this example, $x_{1}$ and $x_{2}$. Suppose the objective function is $x_{1}^{2}+x_{2}^{2}$, Fig. 7 shows that the individuals generated with $\left(u_{1}^{*}, u_{2}^{*}\right)$ sampled from $b c$ and $c c$ are better than those with $\left(u_{1}^{*}, u_{2}^{*}\right)$ from $b b$ and $c b$. So it will be beneficial to find a learning strategy such that promising regions of $u^{*}$ can be identified and individuals are generated accordingly.

Based on the above discussions, a learning sampling strategy is proposed to search for better individuals rapidly. Similar to statistical learning, this learning updates the distribution information of the objective value after taking a sample. It then uses the distribution information to select the best region to sample next. The concept of knowledge gradient (KG) introduced in [49] can be applied to mathematically identify which alternative should be sampled next. This is done by determining the region where sample is likely to improve the current best outcome. If the prior distributions of the objective value in the independent alternatives have the same variance and sample error but different means, then the alternative with

$$
g_{d}(k)=\frac{\sum_{i=1}^{D}\left(P_{i, d}(k-1)\right)}{\sum_{i^{\prime}=1}^{D} \sum_{i=1}^{D}\left|P_{i, i^{\prime}}(k-1)\right| \sum_{i=1}^{D}\left(f\left(\mathbf{z}_{\mathbf{i}}(k-1)\right)-f\left(\mathbf{x}_{\text {pcbest }}(k-1)\right)\right) / D}
$$

![img-3.jpeg](img-3.jpeg)

Fig. 7. Sampling individuals $\left(x_{1}, x_{2}\right)$ in different regions.

## Learning sampling strategy

Input: $D ; N P ; C_{d}(u) ; \alpha$;
$M$ : number of equal intervals of range $[0,1]$;
$\alpha_{1}$ : sampling proportion after making a decision;
$n_{\text {max }}:$ maximum number of sampling decisions;
Output: the sampled population Pop ${ }^{\text {sum }}(k)$.
/* Sample an initial set of individuals in generation $k$ of Algorithm $1^{* /}$

1: Pop ${ }^{\text {sum }}(k)=\operatorname{SAMPLE}((1-\alpha) * N P, C_{d}(u))$;
/* Denote the distribution information $\left(\mu_{\alpha_{1,1}}^{*},\left(\sigma_{\alpha_{1,1}}^{*}\right)^{2}\right)$ of each $u_{d, j}^{*}$ in the $j^{\text {th }}$ interval of the $d^{\text {th }}$ dimension as DIST $_{d j} * /$
2: Initialize DIST $_{d j}$ using $\operatorname{Pop}^{\text {sum }}(k)$;
3: $n=1 ; / / n$ is the iteration counter.
4: While $n \leq n_{\max }$ do
5: Make the $n^{\text {th }}$ sampling decision using DIST $_{d j}$, which has complexity $O\left(D^{*} M\right)$.
6: $\quad$ Pop $^{\text {D }}=\operatorname{SAMPLE}\left(\alpha_{1}^{*}(1-\alpha) * N P, C_{d}(u)\right)$ using the $n^{\text {th }}$ sampling decision. Each individual is generated in $\mathrm{O}\left(D^{*} \log K\right)$ time;
7: Add $\operatorname{Pop}^{\text {D }}$ into $\operatorname{Pop}^{\text {sum }}(k)$;
8: Calculate DIST $_{d j}$ using $\operatorname{Pop}^{\text {sum }}(k)$. This is done in $\left(D^{*} M^{*} N P / 2\right)$ time.
9: Set $n=n+1$.
10: End while
11: Keep the best $(1-\alpha) * N P$ individuals in $\operatorname{Pop}^{\text {sum }}(k)$ and delete others.

Fig. 8. Pseudo-code of learning sampling strategy.
the best mean should be chosen to sample. But the choice should also depend on the variance and the alternatives with larger variance could be attractive choices as sampling there could get a better objective value. The KG gets its name because in a sense it points in the direction of maximal information by taking an expectation of the difference between the current mean and the mean after choosing to sample a certain alternative.

So the task of the learning sampling is to make a decision, which is to select an interval from $M$ distinct intervals for each $u_{d}^{*}, d=1, \ldots, D$. The learning sampling strategy can be outlined as Fig. 8, where $\alpha_{1}$ is the sampling proportion after making a sampling decision; $n_{\max }$ is the maximum number of sampling decisions. The details are described as follows.

The first step of the learning sampling is to sample an initial set of individuals and calculate the prior distribution of
objective function value according to the statistical information of the individuals located in the $j$ th interval of the $d$ th dimension. We assume the prior distribution is a normal distribution with mean $\mu_{u_{d, j}^{*}}^{0}$ and variance $\left(\sigma_{u_{d, j}^{*}}^{0}\right)^{2}$ for each alternative $u_{d, j}^{*}, j=1, \ldots, M$. In the Bayesian view we define $\beta_{u_{d, j}^{*}}^{0}$ as the precision of our belief, which is the inverse of the variance in our estimate $\mu_{u_{d, j}^{*}}^{0}$ of the true mean.

Starting from this initial information, we make a sequence of subsequent sampling decisions, $\left(u_{d, j}^{*}\right)^{1},\left(u_{d, j}^{*}\right)^{2}, \ldots$ Consider the sampling decision $\left(u_{d, j}^{*}\right)^{n}, n=1,2, \ldots$ Assume the sampling error of measuring alternative $u_{d, j}^{*}$ is $\varepsilon_{u_{d, j}^{*}}^{n} \sim N\left(0,1 / \beta_{u_{d, j}^{*}}^{n}\right)$, where $\beta_{u_{d, j}^{*}}^{n}$ is precision of sample, and the resulting sample observation is

$$
\hat{y}_{u_{d, j}^{*}}^{n}=\mu_{u_{d, j}^{*}}^{n-1}+\varepsilon_{u_{d, j}^{*}}^{n}
$$

Because decisions are made sequentially, so the mean and precision can be updated by $\left(u_{d, j}^{*}\right)^{1}, \hat{y}_{u_{d, j}^{*}}^{1}, \ldots,\left(u_{d, j}^{*}\right)^{n}, \hat{y}_{u_{d, j}^{*}}^{n}$. The updating formula is

$$
\left\{\begin{array}{l}
\mu_{u_{d, j}^{*}}^{n}=\frac{\beta_{u_{d, j}^{*}}^{n-1} \mu_{u_{d, j}^{*}}^{n-1}+\beta_{u_{d, j}^{*}}^{n} \hat{y}_{u_{d, j}^{*}}^{n}}{\beta_{u_{d, j}^{*}}^{n-1}+\beta_{u_{d, j}^{*}}^{n}} \\
\beta_{u_{d, j}^{*}}^{n}=\beta_{u_{d, j}^{*}}^{n-1}+\beta_{u_{d, j}^{*}}^{n}
\end{array}\right.
$$

The state of knowledge before the $n$th sampling is defined as

$$
S_{d, j}^{n-1}=\left(\mu_{u_{d, j}^{*}}^{n-1}, \beta_{u_{d, j}^{*}}^{n-1}\right), \quad j=1, \ldots, M
$$

If we stop measuring now, we would pick the mean of best interval

$$
V\left(S_{d, j}^{n-1}\right)=\max _{u_{d, j}^{*}} \mu_{u_{d, j}^{*}}^{n-1}, \quad j=1, \ldots, M
$$

Now if we choose measuring alternative $u_{d, j}^{*}$ as the decision, $\left(u_{d, j}^{*}\right)^{n}$, the next state will be $S_{d, j}^{n}=S\left(S^{n-1},\left(u_{d, j}^{*}\right)^{n-1}, \hat{y}_{u_{d, j}^{*}}^{n}\right)$. The best interval would be identified by

$$
V\left(S_{d, j}^{n}\right)=\max _{u_{d, j}^{*}} \mu_{u_{d, j}^{*}}^{n}, \quad j=1, \ldots, M
$$

We would like to choose $u_{d, j}^{*}$ to maximize the expected value of (18). We can also think of (18) as choosing $u_{d, j}^{*}$ to maximize the expected incremental value

$$
v_{u_{d, j}^{*}}^{\mathrm{KG}, n}=E\left[V\left(S_{d, j}^{n}\right)\right]-V\left(S_{d, j}^{n-1}\right)
$$

Equation (19) is viewed as the KG.
The interval to be sampled at the $n$th sampling for each variable $j$ can be determined by

$$
\left(u_{d, j}^{*}\right)^{n}=\arg \max _{j} v_{u_{d, j}^{*}}^{\mathrm{KG}, n}
$$

In our learning sampling strategy, we start by computing the change in the variance of our estimate of $\mu_{u_{d, j}^{*}}^{n}$ given our state of knowledge $S_{d, j}^{n}$

$$
\begin{aligned}
\left(\hat{\sigma}_{u_{d, j}^{*}}^{n}\right)^{2} & =\operatorname{Var}\left[\mu_{u_{d, j}^{*}}^{n}-\mu_{u_{d, j}^{*}}^{n-1}\right] \\
& =\left(\sigma_{u_{d, j}^{*}}^{n-1}\right)^{2}-\left(\sigma_{u_{d, j}^{*}}^{n}\right)^{2} \\
& =\frac{\left(\sigma_{u_{d, j}^{*}}^{n-1}\right)^{2}}{1+\left(1 / \beta_{u_{d, j}^{*}}^{n}\right)^{2} /\left(\sigma_{u_{d, j}^{*}}^{n-1}\right)^{2}}
\end{aligned}
$$

![img-4.jpeg](img-4.jpeg)

Fig. 9. Process of iterations in different regions on $x_{1}^{2}+x_{2}^{2}$.

We then compute normalized influence of decision $\left(u_{\alpha, j}^{n}\right)^{n}$, calculated by current estimate of the value of $\mu_{\alpha_{d, j}}^{n}$, and the best of the rest, and the number of standard deviations, given by

$$
\zeta_{\alpha_{d, j}}^{n}=-\left|\left(\mu_{\alpha_{d, j}^{n}}^{n-1}-\max _{\alpha_{d, j}^{n} \neq \alpha_{d, j}^{n}} \mu_{\alpha_{d, j}^{n}}^{n-1}\right) / \tilde{\sigma}_{\alpha_{d, j}^{n}}^{n}\right|
$$

Next, we use a standard formula given by

$$
f(\zeta)=\zeta \Phi(\zeta)+\varphi(\zeta)
$$

where $\Phi(\zeta)$ and $\varphi(\zeta)$ are the cumulative probability function and the density function, respectively, of the standard normal distribution. Finally, the KG is given by

$$
v_{\alpha_{d, j}^{k}}^{\mathrm{KG}, n}=\left(\tilde{\sigma}_{\alpha_{d, j}^{n}}^{n}\right)^{2} f\left(\zeta_{\alpha_{d, j}^{n}}^{n}\right)
$$

Then we can make the sampling decision according to (20).
As Fig. 9 shows, the solution obtained by learning sampling strategy is better than other methods with the same number of iterations.

For the complexity, we remark that the learning sampling strategy has $O\left(n_{\max } D \cdot M \cdot N P / 2\right)+O(D \cdot \log K(1-\alpha) N P)+$ $O\left(n_{\max } D \cdot M\right)$ steps. Note that $M, K$, and $n_{\max }$ are small constants. So the time complexity is $O(c D \cdot N P)$, here $c$ is a small positive integer.

## IV. EXPERIMENTAL STUDIES

In order to test the performance of the proposed algorithm, a comprehensive series of benchmark functions of 10/30/50/100/500 dimensions are used. The algorithms are developed using C\# language on the platform of Microsoft Visual Studio 2005. All experiments are carried out on a Lenovo personal computer with $3.30-\mathrm{GHz}$ Intel CPU and 4-GB RAM.

## A. Test Problems

1) CEC 2013 Benchmark Suite: The 28 benchmark functions in the CEC 2013 benchmark suite are utilized to evaluate the algorithm performance, among which $F_{1}$ to $F_{5}$ are unimodal functions; $F_{6}$ to $F_{20}$ are basic multimodal functions; $F_{21}$ to $F_{28}$ are composition functions. The problem definitions and evaluation criteria can be obtained from [50].

TABLE I
Parameters of the Proposed Algorithm


2) Scaling-Up Test Functions: To further test the performance and the universality of our proposed algorithm, the 13 classical functions are selected from [13] and used. They are presented in Table IV in supplementary material, which can be found in the supplementary file of this article. These are minimization problems and can be classified into three groups as follows. $F_{29}$ and $F_{30}$ are separable unimodal problems; $F_{31}$ to $F_{37}$ belong to nonseparable problems with only a few local optima; $F_{38}$ to $F_{41}$ are multimodal problems with many local optima. $F_{30}, F_{32}, F_{34}, F_{36}$, and $F_{39}$ are the shifted or rotated function of $F_{29}, F_{31}, F_{33}, F_{35}$, and $F_{38}$, respectively, and the values of the shifted global optima and the transformation matrices can be obtained in [51]. More details about these functions can be found in [51] and [52].

## B. Comparison Strategies and Metrics

For each algorithm in this article, we use $x^{*}$ and $x^{\prime}$ to indicate the known optimum solution and the best solution obtained when the stopping criterion is satisfied, respectively. Therefore, the function error value $\left(F\left(x^{\prime}\right)-F\left(x^{*}\right)\right)$ is employed to evaluate the algorithms' performance, and if the value is below $1 \mathrm{e}-8$, we see it as zero. The mean and variance are calculated through many independent runs for CEC 2013 benchmark functions and the scaling-up test functions. In each run the algorithms are executed for dimension $\times 10000$ FEs [51] and dimension $\times 11000$ FEs [13] on the two classes of problems, respectively. This setting is the same for all algorithms tested. The mean error and the corresponding standard deviation are calculated and presented in the numerical results tables, where the best mean error value is shown in bold for each benchmark function. The standard deviation appears after the " $\pm$ " sign. Because of the space limitation, some tables are placed in the supplementary file of this article.

To get a direct indication of the performance of our proposed algorithm, the number of the best results in each test group are listed at the bottom of the numerical results tables.

To obtain a statistical conclusion, the two-sided Wilcoxon rank sum test [53] is employed to evaluate the performance between EDA-FL and other algorithms. The value of significance level is set to be 0.05 . The marks " +," " -," and " $=$ " indicate that the compared algorithm is superior to EDA-FL, EDA-FL performs better, and there is no statistically significant difference between EDA-FL and compared algorithm, respectively.

TABLE II
Mean and Standard Deviations of Benchmark Test Functions for Parameter Analysis


TABLE III
Mean and Standard Deviations of Results on 10-D Benchmark Test Functions

Moreover, to evaluate the performance of the convergence, the convergence curves about the mean error values of the best solutions for each algorithm are presented.

To have a reliable and fair comparison, the experimental results of all competitor algorithms are the reported data from the original articles or the websites of authors.

## C. Parameter Analytics

In our proposed algorithm with filtering framework only (EDA-F), the step of prediction has great influence, where A is a diagonal matrix with $D \times D$ dimension. The diagonal elements represent the noise level. To increase the randomness of noise, we set $p_{0}$ is 0.1 . The constant values of the diagonal

![img-5.jpeg](img-5.jpeg)

Fig. 10. Influence on modeling individuals by predicting and revising on the function (a) $F_{2}$, (b) $F_{7}$, (c) $F_{16}$, and (d) $F_{28}$.
elements are set as 0.9 . Similarly, the step of revision plays an important role in our algorithm. The performance has great differences for different combinations of $p_{1}$ and $p_{2}$ values.
![img-6.jpeg](img-6.jpeg)

Fig. 11. Convergence sketches of the function (a) $F_{2}$, (b) $F_{7}$, (c) $F_{16}$, and (d) $F_{28}$.

To obtain the best combination, we test some representative functions with different $p_{1}$ and $p_{2}$. The other parameters for the algorithm are given in Table I. The means and standard

![img-7.jpeg](img-7.jpeg)

Fig. 12. Number of cases on which each algorithm performs the best in the comparison between EDA-FL and state-of-the-art DE algorithms.
deviations for ten runs are listed in Table II. As Table II shows, when the best prediction individual is revised through (12), the algorithm achieves the best solutions in 14 cases for 10/30/50 dimension. Regarding the total number of the best solutions obtained by the algorithm with other parameter settings, $\left(p_{1}=0, p_{2}=0\right),\left(p_{1}=0.05, p_{2}=0.05\right),\left(p_{1}=0.1\right.$, $p_{2}=0$ ), and $\left(p_{1}=0.2, p_{2}=0.4\right)$, are $9,10,7$, and 6 , respectively.

Result Analysis: When $p_{1}=0$ and $p_{2}=0$ indicating that there are no revised individuals going into modeling individuals set, the performance is not good. This proves that the operation "Revise" in filtering is effective to improve the performance. When the values of $p_{1}$ and $p_{2}$ increase to large values, the performance shows a decreasing trend. The root cause of this is that the revised individuals can increase the diversity of the modeling population. When the individuals are revised too much, the precision of distribution will decrease.

## D. Experimental Results

1) Experiment Series 1 (Evaluation on the Strategies): In our proposed algorithm, there are two innovation points: a new framework with filtering and a strategy of learning sampling. To evaluate the performance of them, three versions of the algorithm, EDA, EDA-F, and EDA-FL, are tested on CEC 2013 benchmark functions with 10-D. The parameters are set as in Table I. The means and standard deviations for ten runs are presented in Table III. The best result (with the minimal mean value) is bolded in each row. The results indicate that EDA-F is better than EDA and EDA-FL is superior to EDA-F according to the number of best solutions. To further demonstrate the performance and mechanism of filtering, a class of experiments is executed to display the locations of current population, predicted individuals, revised individuals, and optimal solution in certain iteration. Fig. 10 shows the influence on modeling individuals by predicting and revising on 2-D function $F_{2}, F_{7}, F_{16}$, and $F_{28}$. The red asterisk denotes the optimal solution. The yellow square box and green triangle indicate the predicted individuals and revised individuals, which tend to be closer to the optimal solution. The convergence sketches on 10-D function $F_{2}, F_{7}, F_{16}$, and $F_{28}$ are presented in Fig. 11, where we can see that EDA-FL has a quick convergence speed.

Result Analysis: In our new EDA, the potential advantage of the two distinct operations "Predict" and "Revise" is illustrated
![img-8.jpeg](img-8.jpeg)

Fig. 13. Statistical significance results of comparison between EDA-FL and other EDAs on (a) 10-D, (b) 30-D, and (c) 50-D problems, respectively.
in Fig. 10. The predicted and revised individuals not only tend to be closer to the optimal solution but also increase the diversity of the population and so make it evolve further. Moreover, when adding the learning sampling strategy, our algorithm converges faster. This point is consistent with the idea of getting a good sample through learning.
2) Experiment Series 2 (Comparison of EDA-FL With Other State-of-the-Art Evolutionary Algorithms for CEC 2013 Benchmark Suite With 10/30/50 Dimension): To embody the competitiveness of our proposed algorithm, in this section, we compare the proposed EDA-FL with three DE algorithms that have outstanding performance, among the state-of-theart intelligent algorithms, including composite DE (CoDE)

![img-9.jpeg](img-9.jpeg)

Fig. 14. Number of cases on which each algorithm performs the best in the comparison between EDA-FL and other EDAs.
[54], Adaptive DE with optional external archive algorithm (JADE) [55], and DE algorithm with Strategy Adaptation (SaDE) [56]. The parameters are set as in Table I. The means and standard deviations for ten runs are presented in Tables V-VII, which can be found in the supplementary file of this article. The results of CoDE, JADE, and SaDE are from [53]. Fig. 12 shows the number of cases on which each algorithm performs the best in the comparison between EDA-FL and state-of-the-art DE algorithms. To show the performance more clearly, the statistical significance results are summarized in Fig. 13.

Result Analysis: With great exploitation ability, our proposed algorithm has great advantages on the unimodal function $F_{1}-F_{5}$. Besides, when the dimension increases to 50, the algorithm outperforms all other three algorithms, showing that our proposed algorithm EDA-FL has strong competitiveness.
3) Experiment Series 3 (Comparison With Other EDAs and Further Algorithms for the Scaling-Up Benchmark Functions With 50/100/500 Dimension): Four algorithms are involved in experimental comparisons for 50-D/100-D/500-D: UMDA ${ }_{c}^{\mathrm{G}}$ [6], EMNA ${ }_{\text {global }}$ [6], EEDA [7], and EDA-MCC [13]. UMDA ${ }_{c}^{\mathrm{G}}$ is a univariate Gaussian EDA, and EMNA global is multivariate Gaussian EDA. Because the two EDAs have been studied theoretically and experimentally and applied in real-world, it makes sense comparing them with our proposed algorithm. EDA-MCC has been proposed to solve the large-scale optimization problem, so it is significant to be compared. Two other algorithms, Mutual Information Maximization for Input Clustering to continuous domains where the underlying probability model for every pair of variables is assumed to be a bivariate Gaussian (MIMIC ${ }_{c}^{\mathrm{G}}$ ) and separable Covariance Matrix Adaptation Evolution Strategy (sep-CMA-ES), are included in the comparison for 500-D, because they have good performance for high dimension problems [13]. The means and standard deviations for ten runs are presented in Tables VIII-XI, which can be found in the supplementary file of this article. The best result (with the minimal mean value) is bolded in each row. Fig. 14 shows the number of cases on which each algorithm performs the best in the comparison between EDA-FL and other EDAs. And the statistical significance results are summarized in Fig. 15.

Result Analysis: With great exploitation ability, our proposed algorithm has great advantages on the unimodal function
![img-10.jpeg](img-10.jpeg)

Fig. 15. Statistical significance results of comparison between EDA-FL and other EDAs on (a) 50-D, (b) 100-D, and (c) 500-D problems, respectively.
$F_{1}-F_{5}$. Again, the algorithm gives clearly better results than the other algorithms in high dimension (500-D). The results indicate that our proposed algorithm is effective.

## V. CONCLUSION

In this article, we have proposed a new EDA-FL to solve nonlinear continuous optimization problem. First, we propose a new EDA framework incorporating filtering where the idea of Kalman filtering is adopted to modify some individuals, which in turn affect the model, using an estimation error matrix from historic information. Then, a sampling strategy with learning is proposed. Using this strategy, the decision on where to sample is made according to the statistical information about the objective values of sampled individuals to avoid completely random sampling. Computational experiments on

a collection of general benchmark functions with different dimensions demonstrate that the EDA-FL is effective.

Given the promising results of introducing the filtering and learning mechanisms in EDA, further research could be done to improve the filtering operations and the learning strategy. Another direction could be to apply the new EDA to problems in practice and problems with discrete variables.
