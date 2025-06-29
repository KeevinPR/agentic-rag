# Bayesian Inference in Estimation of Distribution Algorithms 

Marcus Gallagher, Ian Wood, Jonathan Keith and George Sofronov


#### Abstract

Metaheuristics such as Estimation of Distribution Algorithms and the Cross-Entropy method use probabilistic modelling and inference to generate candidate solutions in optimization problems. The model fitting task in this class of algorithms has largely been carried out to date based on maximum likelihood. An alternative approach that is prevalent in statistics and machine learning is to use Bayesian inference. In this paper, we provide a framework for the application of Bayesian inference techniques in probabilistic model-based optimization. Based on this framework, a simple continuous Bayesian Estimation of Distribution Algorithm is described. We evaluate and compare this algorithm experimentally with its maximum likelihood equivalent, $\mathrm{UMDA}_{v}^{G}$.


## I. INTRODUCTION

Estimation of Distribution Algorithms (EDAs) [1], [2], [3] construct a probability distribution $p(\mathbf{x})$ over the search space $\mathcal{X}$ of an optimization problem and adaptively learn this model to drive the search process. Generally speaking, a probability density function is used to generate a sample of candidate solutions at each iteration of the algorithm. This sample is evaluated with respect to the objective function of the problem. A subset of the best points in the sample are selected and used to modify the search distribution so that (with higher probability) improved solutions are produced by sampling from the distribution in next generation. In the Cross-entropy method [4], selected points are used to modify the search distribution so as to decrease the KullbackLeibler divergence from a degenerate distribution over the (estimated) optimal solution to the search distribution. EDAs can also be viewed in terms of a stochastic minimization process on the K-L divergence [5]. EDAs and the CrossEntropy method are closely related and several instances of EDAs can be seen as equivalent to the Cross-Entropy method, depending on the choice of density function and implementation details of the algorithms.

The model fitting task within each iteration of an EDA is typically carried out by a maximum likelihood estimation procedure. An alternative statistical framework is provided by Bayesian inference. In recent years, Bayesian techniques have become increasingly widely used in the fields of machine learning and statistics. Surprisingly however, Bayesian inference has so far received very little attention in the EDA literature.

[^0]Often, the family and structure of the model used in an EDA is fixed (e.g. a set of Bernoulli distributions to generate the bitstrings in the PBIL algorithm [6], or a factorized Gaussian distribution over a continuous search space in the UMDA ${ }_{v}$ algorithm [2]). For EDAs that use probabilistic graphical models, search is often performed to determine the model configuration. For example, the "Bayesian Optimization Algorithm" (BOA) [7] is an EDA that uses a Bayesian network as its density model. The structure of the network model is typically found using a greedy search over a suitable metric. While some of these metrics are derived from Bayesian modelling assumptions (e.g the BDe and BGe metrics [2]), their use in EDAs is quite different from performing Bayesian inference. Bayesian network parameters in EDAs are typically estimated from the data (the selected best points from the sample) using a maximul likelihood approach. Hence (despite the implications of its name), BOA does not involve Bayesian inference in its modelling process.

In this paper, we develop a framework for the application of Bayesian inference techniques for model fitting in EDAs (BayEDAs). Based on this framework, a simple continuous Bayesian Estimation of Distribution Algorithm is described. We evaluate and compare this algorithm experimentally with its maximum likelihood equivalent, $\mathrm{UMDA}_{v}^{G}$.

The general idea of applying Bayesian inference in the context of EDAs has to some extent been considered (see [8] and the references therein). Zhang describes the notion of Bayesian inference in a canonical algorithm, and gives an example of using this idea by considering a prior based on the Boltzmann distribution for model parameters. Zhang discusses possibilities for the implementation of various modelling steps in this canonical algorithm but no specific algorithms are implemented or experimentally evaluated. An example is subsequently presented using a Helmholtz machine as the density model.

In contrast to this previous work, we isolate the idea of using Bayesian inference in model-based optimization. It is then possible to derive specific Bayesian algorithms based on probability density functions commonly used in the EDA literature which can be directly applied in various optimization settings. BayEDAs therefore have a direct connection with maximum-likelihood based EDAs and the cross-entropy method.

A brief outline of the paper is as follows. In Section II we develop a framework for the application of Bayesian inference in EDAs. Section III presents an instantiation of this framework with a continuous EDA based on a univariate Gaussian density model. Experimental results are reported in Section IV to provide insight into the behaviour of the algorithm, demonstrate it's feasibility and compare it with


[^0]:    Marcus Gallagher is with the School of Information Technology and Electrical Engineering, University of Queensland 4072, Australia (email: marcusg@itee.uq.edu.au). Ian Wood is with the School of Mathematical Sciences, Queensland University of Technology, GPO Box 2434 Brisbane QLD 4001 Australia (email: wood@itee.uq.edu.au). Jonathan Keith is with the School of Mathematical Sciences, Queensland University of Technology, GPO Box 2434 Brisbane QLD 4001 Australia (email: j.keith@qut.edu.au). George Sofronov is with the Department of Mathematics, University of Queensland 4072, Australia (email:georges@maths.uq.edu.au).

TABLE I
GENERAL PSEUDOCODE FRAMEWORK FOR AN EDA.

Given: population size $M$, selection parameter $\tau$
BEGIN (set $t=0$ ) Generate $M$ individuals at random
REPEAT for $t=1,2, \ldots$ until stopping criterion is met Select $M_{\text {std }}<M$ individuals via truncation selection Maximise the likelihood $p(D \mid \theta)$ to obtain a point estimate $\hat{\theta}$ Sample $M$ individuals from $p_{t}(\mathbf{x} \mid \hat{\theta})$
$t=t+1$
ENDREPEAT

UMDA ${ }_{c}^{G}$. Some related work concerning Bayesian inference and optimization is discussed in Section V. Finally, Section VI presents some conclusions and outlines directions of future work.

## II. Maximum Likelihood and Bayesian Model Fitting in EDAs

## A. Framework

Consider the optimization problem

$$
\min (f(\mathbf{x})), \mathbf{x} \in \mathcal{X}
$$

where $f(\mathbf{x})$ is the fitness or objective function, $\mathbf{x}$ is an individual solution point and $\mathcal{X}$ is the feasible search space. EDAs build a probabilistic model $p_{t}()$ over $\mathcal{X}$ at each generation $t$ of the algorithm based on selected individuals. Pseudocode for an EDA is shown in Table I.

The probabilistic model in Table I is specified by a vector of parameters $\theta$. The parameters in an EDA model are typically estimated as the maximum likelihood values

$$
\hat{\theta}=\arg \max _{\theta} p\left(\left\{\mathbf{x}^{1}, \ldots, \mathbf{x}^{M_{\text {std }}}\right\} \mid \theta\right)
$$

An alternative to model fitting is provided by Bayesian Statistics. In the Bayesian framework, a prior distribution $p(\theta)$ is specified, reflecting our belief about the model parameters before seeing any data. Once a set of data $D=$ $\left\{\mathbf{x}^{1}, \ldots, \mathbf{x}^{M_{\text {std }}}\right\}$ is observed, we update our belief using Bayes rule

$$
p(\theta \mid D)=\frac{p(D \mid \theta) p(\theta)}{p(D)}
$$

where $p(\theta \mid D)$ is the posterior distribution over the model parameters. The posterior predictive distribution for a future data point $\mathbf{x}$ is then obtained by integrating over the model parameters:

$$
\begin{aligned}
p(\mathbf{x} \mid D) & =\int p(\mathbf{x}, \theta \mid D) d \theta \\
& =\int p(\mathbf{x} \mid \theta, D) p(\theta \mid D) d \theta \\
& =\int p(\mathbf{x} \mid \theta) p(\theta \mid D) d \theta \\
& \propto \int p(\mathbf{x} \mid \theta) p(D \mid \theta) p(\theta) d \theta
\end{aligned}
$$

TABLE II
GENERAL PSEUDOCODE FRAMEWORK FOR A BAYESIAN EDA.

Given: population size $M$, selection parameter $\tau$
BEGIN (set $t=0$ ) Generate $M$ individuals at random
REPEAT for $t=1,2, \ldots$ until stopping criterion is met
Select $M_{\text {std }}<M$ individuals via truncation selection
Calculate the model posterior $p_{t}(\theta \mid D)$
Sample $M$ individuals from $p_{t}(\mathbf{x} \mid D)$ $t=t+1$
ENDREPEAT

As mentioned above, in EDAs we need to be able to sample from $p_{t}(\mathbf{x} \mid D)$ to generate the population at generation $t+1$. A standard technique in Bayesian data analysis to do this is to sample from the joint distribution $p(\mathbf{x}, \theta \mid D)$, giving predicted observations $\left(\mathbf{x}^{1}, \theta^{1}\right), \ldots,\left(\mathbf{x}^{M}, \theta^{M}\right)$. Discarding the sample parameter vectors leaves us with a sample $x^{1}, \ldots, x^{M}$ drawn from the marginal distribution $p(\mathbf{x} \mid D)$. The joint distribution can sometimes be sampled from directly and otherwise can be sampled via Markov Chain Monte Carlo sampling of the unnormalised distribution $p(\mathbf{x} \mid \theta) p(D \mid \theta) p(\theta)$. General pseudocode for a Bayesian EDA is shown in Table II.

It is evident that an implementation of this Bayesian EDA framework will involve making choices for the type of model used (which specifies $p(\mathbf{x} \mid \theta)$ and the prior distribution $p(\theta)$ ). These choices are dependent on the type of problem to be solved (e.g continuous versus discrete solution variables). For some cases the calculation of the model posterior and posterior predictive distribution can be carried out simply, while other choices may require more sophisticated Markov Chain Monte Carlo sampling techniques.

## III. APPLICATION TO FACTORIZED-MODEL CONTINUOUS EDAs

The simplest and most widely developed model in EDAs is a factorized product of univariate marginal distributions

$$
p(\mathbf{x})=\prod_{i=1}^{m} p\left(x_{i}\right)
$$

A number of continuous EDAs $\left(\mathbf{x} \in \mathbb{R}^{n}\right)$ have been developed using the factorized probability model given in (2). For the remainder of this paper we focus on continuous EDAs that utilize a univariate Gaussian distribution

$$
p\left(x_{i} \mid \mu_{i}, \sigma_{i}^{2}\right)=\frac{1}{\sqrt{2 \pi} \sigma_{i}} e^{-\frac{1}{2}\left(\frac{\mu_{i}-\mu_{i}}{\sigma_{i}}\right)^{2}}
$$

The learning/model estimation problem in this case requires a method for calculating the mean $\mu_{i}$ and variance $\sigma_{i}$ parameters of $p\left(x_{i}\right)$. The standard model is to use a different $\sigma_{i}$ parameter for each search dimension, leading to elliptical contours of equal probability with the constraint that the principal axes of these ellipses must be parallel to one of the coordinate axes of the space.

## A. Continuous UMDA

The extension of the Univariate Marginal Distribution Algorithm (UMDA) [9] to continuous search spaces: $\mathrm{UMDA}_{c}^{G}$ [10], follows the general EDA framework of Table I and employs the model from (3). In $\mathrm{UMDA}_{c}^{G}$, the mean parameters for the next generation are set as the sample mean of the selected population

$$
\mu_{i, t}=\bar{x}=\frac{1}{M_{\text {sel }}} \sum_{j=1}^{M_{\text {sel }}} x_{i}^{j}
$$

and the standard deviation (variance) parameters are set as the sample standard deviation (variance) of the selected population

$$
\sigma_{i, t}=s=\sqrt{\frac{1}{M_{\text {sel }}} \sum_{j=1}^{M_{\text {sel }}}\left(x_{i, j}-\bar{x}\right)}
$$

At any given generation, $\mu_{i, t}$ and $\sigma_{i, t}$ represent the maximum likelihood estimates for the mean and standard deviation of each marginal distribution $p\left(x_{i} \mid \mu_{i}, \sigma_{i}^{2}\right)$.

The initial population $(t=0)$ is generated from a uniform distribution across the feasible search space. In the first generation, $\mu_{i, 0}$ and $\sigma_{i, 0}$ are estimated based on selected points from this random population. $\mathrm{UMDA}_{c}^{G}$ uses truncation selection: a fraction $\tau$ of the population with the best objective function values are retained for building/adapting the search model ${ }^{1}$. Therefore, only two algorithm parameters must be specified for an implementation of $\mathrm{UMDA}_{c}^{G}$ : the population size $M$ and the selection parameter $\tau$.

## B. BayEDA ${ }_{c \mathrm{G}}$ : A Continuous Bayesian EDA based on a univariate Gaussian model

Using the factorized model from (2) above, a Bayesian EDA can be specified (here for simplicity we use $x$ to refer to any one of the solution components $x_{i}$ in a multidimensional problem). For a univariate Gaussian (Normal) model distribution, Bayesian inference can readily be carried out: the resulting expressions given here are drawn from Gelman et. al [11]. We consider the simplest case of a noninformative (flat) prior for the model parameters, expressing no preference for any particular values for the model parameters before observing any data. In this case, inference depends only on the data (selected individuals). The standard noninformative prior is uniform on $\left(\mu, \log \sigma^{2}\right)$ or

$$
p\left(\mu, \sigma^{2}\right) \propto\left(\sigma^{2}\right)^{-1}
$$

The joint posterior can be factorised as

$$
p\left(\mu, \sigma^{2} \mid D\right)=p\left(\mu \mid \sigma^{2}, D\right) p\left(\sigma^{2} \mid D\right)
$$

In this case, the marginal density for $\sigma$ is

$$
\sigma^{2} \mid D \sim \operatorname{Inv}-\chi^{2}\left(n-1, s^{2}\right)
$$

[^0]Table III
ALGORITHM: BayEDA ${ }_{c \mathrm{G}}$.

Given: population size $M$, selection parameter $\tau$
BEGIN (set $t=0$ ) Generate $M$ individuals uniformly in $S$
REPEAT for $t=1,2, \ldots$ until stopping criterion is met
Select $M_{\text {sel }}=\operatorname{Round}(M \cdot \tau)$ individuals via truncation selection
Calculate sample mean $\bar{x}$ and variance $s^{2}$ of D to update model
Sample $M$ individuals from $p_{t}(\mathbf{x} \mid D, \theta)$ :
FOR i=1:M
Draw sample variance $\hat{\sigma}^{2} \sim \operatorname{Inv}-\chi^{2}\left(M_{\text {sel }}-1, s^{2}\right)$
Draw sample mean $\hat{\mu} \sim N\left(\bar{x}, \hat{\sigma}^{2} /\left(M_{\text {sel }}-1\right)\right)$
Draw new individual $\mathbf{x}_{i} \sim N\left(\hat{\mu}, \hat{\sigma}^{2}\right)$
ENDFOR
ENDREPEAT
END
where $s^{2}$ is the sample variance of the data. The conditional density for $\mu$ is

$$
\mu \mid D, \sigma^{2} \sim N\left(\bar{x}, \sigma^{2} / M_{\text {sel }}\right)
$$

where $\bar{x}$ is the sample mean of the data $D$.
The predictive distribution for $\hat{x}$ given the data, $\mu$ and $\sigma$ is

$$
\hat{x} \mid D, \mu, \sigma^{2} \sim N\left(\mu, \sigma^{2}\right)
$$

In the $\operatorname{BayEDA}_{\mathrm{cG}}$ algorithm, sampling from the posterior predictive distribution $p(\hat{x} \mid D)$ can be easily carried out in a three-step process. Firstly, a sample $\hat{\sigma}^{2}$ is drawn from (6), then this sample is used to draw a sample $\hat{\mu}$ from (7) and finally both samples are used to draw a sample $\tilde{x}$ from (8). The process is repeated $M$ times to produce the population for use in the next generation.

The algorithm is summarized in Table III. Note that for implementation purposes, a random draw y from an inverse$\chi^{2}$ distribution can be obtained by firstly drawing a sample z from the $\chi^{2}$ distribution and applying $y=s^{2} / z$. The $\chi^{2}$ distribution is also a special case of the gamma distribution (see [11] for details).

## IV. EXPERIMENTAL RESULTS

In this Section we present simulation results for the $\mathrm{BayEDA}_{\mathrm{cG}}$ algorithm, using several standard test functions, and for comparison results for $\mathrm{UMDA}_{c}^{G}$ on the same functions. Since $\operatorname{BayEDA}_{\mathrm{cG}}$ and $\mathrm{UMDA}_{c}^{G}$ use the same (factorised Gaussian) model and data (while differing in the way inference is performed on the model parameters), we would expect the two algorithms to produce results that are similar in a number of respects. Our main aim is to gain some insight into the behaviour of the $\mathrm{BayEDA}_{\mathrm{cG}}$ algorithm rather than attempting to claim state-of-the-art performance on these problems. Therefore, we make no attempt to tune the parameters of the algorithms to these problems. The test functions used are listed in Table IV. While these functions have some limitations, they are commonly used and sufficient here for illustrative purposes.

Firstly we consider a simple unimodal problem (the 1-D Sphere function) to show the experimental convergence of the algorithm compared to $\mathrm{UMDA}_{c}^{G}$. For each algorithm,


[^0]:    ${ }^{1}$ Rounding if $N \cdot \tau$ is not an integer.

TABLE IV
TEST FUNCTIONS USED IN THE EXPERIMENTS

![img-0.jpeg](img-0.jpeg)

Fig. 1. Best-so-far performance curves for $\mathrm{BayEDA}_{c \mathrm{G}}$ and $\mathrm{UMDA}_{c}^{G}$ on the 1-D Sphere function. Shown are average performance and (average + standard deviation) curves.
$M=40$ and $\tau=0.9$. 100 trials were conducted over 100 generations, with results shown as mean and standard deviations over these trials. Figure 1 shows the performance of each algorithm as a function of generations (in terms of best solution value found so far). While the performance is fairly similar, $\mathrm{BayEDA}_{c \mathrm{G}}$ attains a lower value on average. Progress for $\mathrm{UMDA}_{c}^{G}$ appears to converge after about 15 generations, compared to around 20 generations for BayEDA $_{c \mathrm{G}}$. The standard deviations on the curves for each algorithm are almost identical.

Figures 2 and 3 show the evolution of the model parameters for each algorithm. Note that for BayEDA ${ }_{c G}$ these are first averaged over the $M$ model parameter samples generated and used when sampling from the posterior predictive distribution of each population. Apart from a fluctuation in standard deviation around generation 5-15, the curves for the $\mu$ parameters are very similar (Figure 2). In Figure 3 however, we see a slower convergence for the BayEDA ${ }_{c G} \sigma^{2}$ estimate compared to that of $\mathrm{UMDA}_{c}^{G}$. This explains the improved performance of BayEDA $_{c \mathrm{G}}$ in Figure 1. The model sampling
![img-1.jpeg](img-1.jpeg)

Fig. 2. Evolution of model mean parameter values for $\mathrm{BayEDA}_{c \mathrm{G}}$ and $\mathrm{UMDA}_{c}^{G}$ on the 1-D sphere function. Shown are average performance and (average + standard deviation) curves. For BayEDA ${ }_{c G}$ the curves are averages of posterior samples and over runs.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Evolution of model variance parameter values for BayEDA ${ }_{c G}$ and $\mathrm{UMDA}_{c}^{G}$ on the 1-D sphere function. Shown are average performance and (average + standard deviation) curves. For BayEDA ${ }_{c G}$ the curves are averages of posterior samples and standard deviations over runs.
in BayEDA ${ }_{c G}$ introduces a source of variability not present in $\mathrm{UMDA}_{c}^{G}$, which increases the search diversity. For this problem the effect leads to an improvement in performance.

A further illustration of the dynamics of the BayEDA ${ }_{c G}$ model is shown in Figure 4. For this experiment, $M=40$ and $\tau=0.95$ over 100 generations. The graph shows the evolution of a single trial run of the BayEDA model on the 1-D Rastrigin function, in terms of the sampled model parameter values over generations. The model samples follow a trajectory with mean values tending towards the location of the global optimum $(x=0)$ and variance values converging towards zero. However, clustering is evident in the points

![img-3.jpeg](img-3.jpeg)

Fig. 4. A plot of the model posterior samples over a single run of BayEDA ${ }_{v E 2}$ on the 1-D Rastrigin function. Clustering is evident along the mean parameter axis and can be related to the structure of the problem.
on this trajectory, showing that the algorithm spends more time in certain areas of the search space. For reference, the 1-D Rastrigin function is shown in Figure 5 over the range explored by the algorithm. Comparing Figures 4 and 5 it can be seen that the clustering in model samples corresponds to the local minima of the function.

In the Bayesian framework, model parameter values are drawn from the model according to their posterior distribution. This fact can offer an explanation for the result shown in Figure 4. Selection will lead to a representation of the regions on the 1-D Rastrigin function close to each local optimum. This will make more likely the relative probability of Gaussian models with a mean peaked over a local optimum and a variance in proportion to the size of a local basin of attraction. As a consequence, models of such shape and location will tend to appear more frequently in samples from the posterior distribution. The influence of this effect will however depend on the test problem and the algorithm parameters. For this experiment, a very soft selection pressure was used and the initial population was uniform in the range $[-15,5]$. This causes the model to evolve more slowly over the objective function surface and causes it to encounter more locally optimal basins of attraction before locating the region around the global optimum.

Experiments were also conducted on 10-D versions of the test functions given in Table IV. For each problem, 30 trials were conducted. Following the experiments in Chapter 8 of [2], we used $M=2000$ and $\tau=0.5$. For $f_{S p h}$, runs were for 100 generations and for all other functions runs were for 200 generations The results are summarized in Table V.

Overall the results show highly similar performance for the two algorithms. $\mathrm{UMDA}_{v}^{G}$ showed slightly better mean performance in most cases, although the standard deviation of the results for BayEDA ${ }_{v E 2}$ was almost always larger that of $\mathrm{UMDA}_{v}^{G}$ (possibly a result of the model variability
![img-4.jpeg](img-4.jpeg)

Fig. 5. The 1-D Rastrigin function in over the range covered by the results in Figure 4.

TABLE V
PERFORMANCE RESULTS ON 10D VERSIONS OF THE TEST FUNCTIONS.

discussed in the 1-D examples above). As mentioned above, no attempt was made to optimize the values of $M$ and $\tau$ used in BayEDA ${ }_{v E 2}$ - a study of the sensitivity of the performance of the algorithms to the parameter values is outside the scope of this paper. The global optimum for each problem was found with high precision, apart from the Rosenbrock function for which convergence is known to be difficult.

## V. Related Work

The literature concerned with the development of optimization techniques is both large and diverse. Optimization algorithms that construct some kind of statistical model and use this model to influence the search process can be found in areas such as Evolutionary Computation, Metaheuristics, Machine Learning and Engineering Design, as well as in the fields of stochastic and global optimization.

## A. Objective Function Models

A different approach to model-based optimization is to construct a model using not only selected points visited during the search, but also the corresponding objective functions values for those points searched. Newton's method is a simple and well-known example of this class of techniques, fitting a local quadratic model at each iteration of the algorithm and directing the search using the optimum of the model (Sequential quadratic programming techniques generalise this idea) [12]. Response surface methodology [13]

also utilizes optimization procedures that fit a low-order polynomial regression model to the $\left(\mathrm{x}_{t i}, S\left(\mathrm{x}_{t i}\right)\right.$ data and use simple calculus to estimate the optima from the polynomial. Experimental design techniques are an important part of response surface approaches.

Stochastic process models of the objective function have also been widely considered as response surfaces and in model-based optimization, dating back to an algorithm introduced by Kushner in 1964 based on a 1-D Weiner process [14]. Subsequent work includes that of Stuckman [15], the Bayesian approach to global optimization of Mockus [16] and the P-algorithm of Zilinskas [17]. In engineering design, more sophisticated stochastic process models have been employed as response surfaces for model-based optimization. In particular, kriging models have received attention [18]. These techniques produce a surrogate model of the objective function, together with a value for the confidence of the model at any point $\mathbf{x}$. Together with information about the current best solution found, this confidence information is used to define criteria that indicate the expected utility of searching future points in the search space [19].

Previous work on model-based optimization can also be found in artificial intelligence and machine learning. Moore and Schneider use locally weighted regression to build a model of the objective function using all points evaluated during the search [20]. Boyan and Moore propose the STAGE algorithm [21], which learns an "evaluation function" which aims to predict the outcome of a local search algorithm. This evaluation function model is then used to guide future search.

## VI. CONCLUSIONS

We have presented a new approach to model fitting in EDAs based on Bayesian inference, a method which utilizes prior distributions on model parameters and generates each successive population from the posterior predictive distribution. A simple implementation of this framework, $\mathrm{BayEDA}_{\mathrm{cG}}$ using a Gaussian model with a noninformative prior was detailed and experimentally compared against the frequentist alternative, UMDA ${ }_{c}^{G}$. The $\mathrm{BayEDA}_{\mathrm{cG}}$ method outperformed the UMDA ${ }_{c}^{G}$ method on an example 1-dimensional optimization problem. Its performance on five 10-dimensional example problems was overall very similar to that of UMDA ${ }_{c}^{G}$. The differences between the two results are primarily due to the slightly larger variance of the $\mathrm{BayEDA}_{\mathrm{cG}}$ model.

We believe that there is considerable scope for future work in developing Bayesian techniques in EDAs. While the $\mathrm{BayEDA}_{\mathrm{cG}}$ implementation described here is a continuous univariate model, multivariate models and/or models for discrete variables exist in the Bayesian literature and should be readily applicable to EDAs. In principle, Bayesian EDAs could be developed using many of the other probabilistic models commonly used in discrete and continuous EDAs (though some implementations will be more complex than others). Furthermore, the Bayesian framework opens up the possibility of utilizing prior distributions in the context of optimization. Although this paper only considers a simple
noninformative prior over univariate Gaussian model parameters, informative priors may be useful to incorporate knowledge about optimization problems (e.g constraints) in a consistent way, something that is not possible with EDAs employing maximum-likelihood parameter estimation. In addition, conjugate priors can be utilized to produce efficient implementations of Bayesian inference for many commonly used distributions.

## ACKNOWLEDGMENT

The authors would like to thank Dirk Kroese for contributing to the development of this work and related discussion. Ian Wood would like to acknowledge the support of the ARC Center for Complex Dynamic Systems and Control. Jonathan Keith and George Sofronov would like to acknowledge the support of an Australian Research Council (ARC) Discovery Grant (DP0556631) and additionally for JK a National Medical and Health Research Council (NHMRC) project grant (389892).
