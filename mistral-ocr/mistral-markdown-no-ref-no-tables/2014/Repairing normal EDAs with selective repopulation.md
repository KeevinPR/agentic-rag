# Repairing normal EDAs with selective repopulation 

S. Ivvan Valdez P. *, Arturo Hernández, Salvador Botello<br>Centre for Research in Mathematics (CIMAT) A.C., C. Jalisco S/N, Mineral de Valenciana, Guanajuato, Gto., C.P. 36000, Mexico

## A R T I C L E I N F O

Keywords:
Normal multivariate EDA
Diversity
Weighted estimators
Evolutionary computation
Global optimization

A B S T R A C T

The standard Estimation of Distribution Algorithm (EDA), usually, suffers from premature convergence due to an inherent inability to maintain an adequate variance and to preserve diverse candidate solutions. Normal multivariate EDAs have especially shown a lack of exploration even for convex objective functions. This article introduces several techniques which can be used to enhance the standard Normal multivariate EDA performance. The most important ones are based on (1) pre-selecting the candidate solutions to be evaluated, (2) replacing only a fraction of the population and (3) computing weighted estimators of the mean and covariance matrix. The resulting Normal EDA is competitive with similar approaches, as it is evidenced by statistical comparisons.
(c) 2013 Elsevier Inc. All rights reserved.

## 1. Introduction

The Estimation of distribution algorithm framework was initially proposed as a probability model of the genetic algorithms (GAs) operators [1,2]. Researchers then discovered several advantages of tackling hard optimization problems in this way, for instance: automated learning of self-adapted parameters, usually computed by using Maximum Likelihood (ML) estimators [1-4]. Additionally, researchers pointed out that EDAs could tackle the learning-linkage problem by using structural learning to estimate variable dependencies [1]. In summary, EDAs intend to capture sufficient information to perform the search, via the estimation of the structure and parameters of a probability distribution. According to this paradigm there are several interesting questions that arise when investigating the EDAs performance:

1. What if the estimation and/or predefined search distribution (the parametric model used to search) has an inherent undesired bias resulting in underexplored regions?
2. What if the search distribution is incapable of representing the structure of the solutions in the selected set?

The first question is not referred to the bias needed to perform the search, but a bias inserted due to the model or the parameter computation, for instance: a research article reports that EDAs reduce the variance naturally in the estimation step by a factor $1-1 / N$ in each generation ( $N=$ population size) [5], when using ML estimators. Related to the second question, EDAs in continuous search spaces usually assume Normality of the adequate search distribution [1,6]. While the general frameworks of standard EDAs assume that the adequate search distribution, is the underlying distribution of the selected set [7,3]. According to these premises, several conditions must be accomplished in order to guarantee that the optimum will be found: (1) the structure, position, and density of the selected set must contain the adequate and sufficient information to find the optimum, (2) the Normal distribution must be capable of capturing such position, structure and density. If none or only one of these statements is achieved, then, it is quite possible that the algorithm never finds the optimum.

[^0]
[^0]:    * Corresponding author.

    E-mail addresses: ivvan@cimat.mx (S.I. Valdez P.), artha@cimat.mx (A. Hernández), botello@cimat.mx (S. Botello).

By structure of the selected set we refer to information in the selected set that can be used to infer the contour-lines and variable relationships in the objective function [8]. Notice that, even if we have captured adequately the structure or variable dependencies (for example by a covariance matrix), additionally we need to pose adequately the probability mass (for example by posing the mean in a Normal distribution). In the case of the Normal distribution, the density is well defined by the covariance matrix and mean, but, for example, in the case of Normal mixtures, each single Normal could be weighted or sampled in agreement with the promising region it covers. That is to say, the density could be defined proportionally to the objective function. In ideal EDAs, the characteristics of: structure, position and density of the selected set are directly related with the fitness/objective function [7]. The selected set is posed in the regions with the best objective value, the structure and density depends on a threshold or a probability of selecting and generating solutions which (ideally) depends on the objective value. In many cases the Normal distribution can not reproduce all the mentioned characteristics. Researchers have deal with the lacks of ML-estimator, basically, by increasing the population diversity[9]. Nevertheless a broad range of algorithms and research articles have dealt with this issue, we group the most representative ones as follows:

Variance scaling [10,6,11,12]. These proposals intend to avoid premature convergence of the Normal EDA. Notice that the Normal EDA only favors the region around the mean, hence, the Normal distribution only can represent single-mode function landscapes with ellipsoidal shapes of the promising region. In addition, the current selected set also has an inherent uncertainty about the function landscape and optimum position. Increasing the variance can help diminish these disadvantages, by covering a wider region, and promote sampling unexplored regions.

Covariance matrix repairing [6]. The covariance matrix repairing schemes can group most of the proposals with a covariance matrix modification. These schemes intend to circumvent numerical problems by detecting and repairing negative or quite small eigen-values in the covariance matrix. They also share similar advantages of variance increasing/scaling.

Using complex models based on Normal mixtures [13-15]. Complex models can better reproduce the structure of the selected set as well as the density associated to each promising region, if there are several of them.

Prediction of moving directions. These approaches belongs to a different kind of enhancements in contrast with the commented above, because the other approaches intend to perform an adequate search by reducing (not so quickly) the exploration area, while the approaches that work with directions often considers that the optimum is distant from the exploration area. For example, Wagner et al. [16], show that, even though, the improvement direction can be inferred from the selected set, the standard Normal EDA (EMNA [1]) samples intensively in a direction with similar objective value than the current population (maximum eigenvalue direction), instead of the direction of maximum improvement (minimum eigenvalue direction). The Eigen-EDA [16] intends to circumvent this problem as well as other approaches, such as the widely studied CMA-ES [17], which summarizes historical improvement directions (evolution path) in the covariance matrix. The anticipated mean-shift [4] computes an improvement direction for the mean, and intends to use this knowledge to accelerate the search process.

For this work we assume that the optimum is inside the exploration region, but not necessarily in the center. This is a reasonable assumption because in many real world problems, we must define the search domain as a priori information. This article presents a proposal of a single-Normal multivariate EDA which tackles all the mentioned issues. For this purpose, we firstly initialize the algorithm with candidate solutions of high diversity, in order to reduce inherent bias and uncertainty of the finite sized selected set. Secondly, we preserve a subset of solutions to capture the function landscape and the promising regions shapes, hence even if the structure of the selected set is not well captured by the Normal distribution, the preserved solutions will be used to reinforce the parameter learning and eventually sample all the promising regions. Thirdly, we intend to compute the adequate density by using weighted estimators, which favors sampling the best known regions. Additionally, our algorithm integrates a mechanism to avoid the evaluation of solutions which are similar to those already known, this is the reason we called our algorithm: Normal based EDA with selective re-population (EDA-SRP).

The article is presented as follows: Section 2 presents the technique to rank solutions according to their diversity, and the methods for the selection and parameter estimation steps. Section 3 presents the Normal EDA proposal. Section 4 presents the numerical experiments and contrasts our proposal with other Normal EDAs. Section 5, presents a general discussion of the algorithm, and contrast the different techniques introduced in this article, in order to analize its individual contribution of each of them. Finally, Section 6 presents the general conclusions and perspectives of future work. Without loss of generality, we refer to a maximization case for all the algorithms and formulas presented in this work.

# 2. Ranking diverse solutions, selection and weight computation 

### 2.1. The maximin algorithm for ranking diverse solutions

The Maximin selection, similar to the presented in this section, was introduced by Valdez et al. [18] for selecting well spread Pareto fronts in multiobjective evolutionary algorithms. The algorithm is named because an individual is selected according to the maximum of the minimum distances to the already selected set.

The Maximin algorithm is used at the beginning of the search process to select the initial population, and during the search process to rank the solutions. In Algorithm 1, Rank represents a diversity value, the most diverse solutions have the minimum values. Our Maximin version uses as input a set of reference points $R$, which is computed as follows:

1. In the initialization procedure, $R$ contains the points in $\bar{X}$ with the minimum and maximum values in each dimension. It is to say, $R$ contains some points in the decision space, which are taken as the minimum and maximum (in the decision space) found in a large sample $\bar{X}$.
2. During the generations, $R$ is the last selected set, computed according the truncation selection explained in the next section.

The value of -0.1 in line 8 , could be any value in $[-1,0)$. In line 6 we set the distance value to -1 for the individuals already ranked. Thus, the -0.1 is only an indicator of which individuals are not ranked yet.

# 2.2. Truncation selection 

In addition to the Maximin algorithm, we use a truncation selection method which promotes that the selected set has a better objective value each generation, it is described in Algorithm 2.

In Algorithm 2 the first threshold $\theta^{0}$ is the worst objective value in the initial population, the new threshold for the generation $t+1$ is computed inside the algorithm. The selected set objective values are asked to be greater than $\theta^{t}$, thus the selected set mean converges to the best individual, due to (most of the time) it is an increasing sequence bounded by the best objective value known so far. In line 1 we obtain the indices of the population decreasingly sorted by its objective value, in line 2 an $\epsilon$ value is computed as $10^{-14}$ times the greatest absolute value among the minimum, maximum, and the difference between minimum and maximum fitness in the population. This $\epsilon$ is used to ensure an increasing mean of the selected set instead of a non-decreasing one if epsilon $=0$. In line 3 we truncate half of the population setting $k$ (selected set size) to $n / 2$. Lines 4 and 5 , remove individuals form the selected set if they are not above the threshold $\theta^{t}$, ensuring that the selected set size is not less than five percent of the population. Notice that the only case when the mean of the selected set could not be an increasing sequence results when the selected set is reduced to five percent of the population. Finally, line 6 recomputes the threshold $\theta^{t}$ as the worst objective value in the selected set, hence the selected set in the next generation must have greater values than $\theta^{t}$.

### 2.3. Computing weights for the parameter estimation

Weighting solutions is an up-to-day topic in EDAs [19]. Evolutionary algorithms, such as recent CMA-ES proposals, have been using weighted estimators, and local meta-models for avoiding the evaluation of candidate solutions [20]. In such proposals, the local meta-model does not depend on the re-weighting process, in contrast, the weights used in our approach for the parameter estimation, are also used for the replacement step, in order to avoid the evaluation of candidate solutions. The weights are computed by simply ranking and normalizing the solutions according to their objective value. The individual with the maximum objective value has the maximum weight $w_{i_{1}}=2 n /(n(n+1))$, the second maximum value has the second maximum weight $w_{i_{2}}=2(n-1) /(n(n+1))$, and so on, until the individual with the minimum objective value with a weight $w_{i_{n}}=2 /(n(n+1))$. In general, for the decreasingly sorted individuals the weights are given by Eq. 1. Remember that I are the indices of the decreasingly sorted selected set. Using Eq. (1) the sum of all the weights is 1 , thus the weights can be seen as a priori probabilities which indicate which data is more or less probable, in this case we are indicating that the best individual is more probable than the worst individual, thus we expect to sample intensively the region around the best individual, because we are indicating explicitly that it is the most probable one.

$$
w_{i_{1}}=\frac{2(n-i+1)}{n(n+1)} \quad \text { for } i=1 . . n
$$

## 3. Normal based EDA with selective re-population (EDA-SRP)

This section introduces a Normal based EDA with selective re-population. It is described in Algorithm 3. In Step 1 a large sample $\bar{X}$, of 6 times $n_{r s}$ times the population size, is uniformly generated. In Step 2 the reference set $R$ is computed as described in Section 2.1. Step 4 performs the Maximim ranking and selects the initial population $X$ of $n_{p o p}$ individuals with the maximum Maximin ranking. Step 5 evaluates the initial population, and Step 6 performs the truncation selection according to Algorithm 2. Steps 7 is the weight computation according to Section 2.3. Step 8 and 9 store the selected set and its objective value. Step 10 computes weighted estimators of the mean $\mu$ and covariance matrix $\Sigma$ according to Eqs. 2 and 3.

$$
\begin{aligned}
& \mu_{i}=\sum_{j \in I} w_{j} x_{j, i} \\
& \Sigma_{i, k}=\sum_{j \in I}\left(x_{j, i}-\mu_{i}\right)\left(x_{j, k}-\mu_{k}\right) w_{j}
\end{aligned}
$$

Step 12 generates a set of candidate solutions $\bar{X}$ of size $n_{r s} \cdot n_{p o p}$. The following steps are especially important for the algorithm in order to maintain and generate diverse solutions: Step 13, computes the Maximin ranking for $\bar{X}$ using the last selected set as reference points. In Steps 14-16, a new ranking Rank $_{i}^{\prime}$ is computed for each $x_{i} \in \bar{X}$, by using the Maximin

ranking of each $s_{i}$ and the value of the weight $w_{s_{i}}$ of the nearest neighbor in the selected set $R$. This rank measures how good a candidate solution can be, regarding the nearest already-evaluated solution, but at the same time, intends to discriminate solutions similar to those already evaluated by using the Maximin ranking. Steps 17 and 18 select and evaluate the solutions with the greatest Rank' which have the indices $J$ (of size $n_{\text {pop }}-n_{S}$ ). Notice that the number of evaluated solutions is less than $n_{\text {pop }}$ (between 50 and 95 percent). Steps 19 and 20, insert the last selected set and the new candidate solutions to the population, in order to perform the current selection.

The algorithm requires as problem parameters the number of variables $n_{\text {var }}$, and the vectors of inferior and superior limits respectively $x_{\text {inf }}, x_{\text {sup }}$. The possible stopping criteria are: a minimum covariance matrix norm $\epsilon_{\text {tot }}$, the maximum number of evaluations max $_{\text {cred }}$, maximum desired value of the objective function $f_{\text {max }}$, and as user given parameters: the population size $n_{\text {pop }}$ and $n_{s i}$ a resampling rate (see Step 12). Possibly the best stopping criterion is the covariance matrix norm, because it indicates the exploration capacity of the algorithm. The purpose of the other stopping criteria is the comparison with reported results. The next section performs several experiments and comparisons in order to provide evidence of the EDA-SRP performance.

# 4. Experiments and comparison with other Normal EDAs 

In this section we present several comparisons with other Normal based EDAs. The functions used for the comparisons are shown in Table 1.

Comparison with the NichingEDA, classical Normal EDAs and the EigenEDA. The NichingEDA [21] intends to solve the problem of representing the structure or shape of the most promising regions by using Niches, each of them is linked with a probability distribution. Then, some information is shared by using evolutionary operators. Some of the results in the comparison of the NichingEDA are presented here, including unimodal and multimodal objective functions. The results include the $\operatorname{UMDA}_{i=1}^{n}[1]$, the $\operatorname{EMNA}_{\text {global }}[1]$ and the EEDA [16] which is similar to EMNA but with a mechanism to enlarge the variance in the direction of the minimum eigenvalue. Additionally, we compared the EDA-SRP with the CEGNA $_{\text {BCE }}[22]$, CEGDA[22] and NichingEDA for the Schewfel $f_{\theta}$ problem, this is a challenging problem with multiple local minima. The results for this last comparison are also borrowed from [21].

Comparison settings: The comparison uses the Sphere, Ackley, Rosenbrock and Schwefel problems. In domains of $[-100,100],[-32,32],[-30,30]$ and $[-500,500]$ respectively. A stopping criterion of the maximum number of evaluations is applied as $5 \mathrm{e} 5,5 \mathrm{e} 5,5 \mathrm{e} 6,4 \mathrm{e} 5$. The population size is 2000 for all the problems.

EDA-SPR settings: The population size is 500 for the Sphere, Ackley and Rosenbrock functions. For the Schwefel $f_{\theta}$ problem the population size is 210 . The stopping criterion is the number of function evaluations in order to perform a fair comparison. The resampling rate is 3 for all the experiments, except for the Schwefel which is 4.

Comments about the test: Table 2 shows that the EDA-SRP accurately solves all the problems. In addition, the results are similar or better than the delivered by other approaches.

For the Schwefel problem the results in Table 3 shows that the algorithm has a competitive performance, although the EDA-SRP does not find the optimum, it performs better than the others. Most of the cases the algorithm stops because of

Table 1
Test problems used in comparisons.

Table 2
Comparison of classical Normal base EDAs (UMDA and EMNA) and enhanced Normal EDAs (EEDA and Niching EDA) with the EDA with selective repopulation (EDA-SRP). Mean and (standard deviation) of the best function value found in 30 runs.
Table 3
Comparison of mixture-Normal base EDAs (CEGNA ${ }_{R G}$, and CEDNA) and Niching EDA with the EDA with selective repopulation (EDA-SRP). For the Schwefel $f_{8}$ problem in 30 dimensions. Best, mean and standard deviation of the best function value found in 30 runs.

the number of evaluations, that is to say the norm of covariance matrix is not close to 0 , hence, the experiment suggests using a bigger population and number of evaluations in order to improve the quality of the results. As can be observed the parameters are not hard to tune, and/or they are robust in the sense that the same parameter values deliver competitive results for different problems in this test.

The following subsection analyzes the EDA-SRP general aspects and gives recommendations about parameter settings.

# 5. General discussion 

Using the Rosenbrock function in 2 dimensions we graphically analyze the effects of the estimation/selection steps. Table 4 shows several typical generations of the algorithm. In Table 4(a) the initial large sample $X$ is shown with small dots (see Step 1, Algorithm 3), using the Maximin algorithm we select the initial population which is shown with big dots in Table 4(a) and with small dots in Table 4(b). As can be seen, the initial population are individuals with high diversity, well spread over the whole search space.

After evaluation the fittest individuals are selected according to the truncation selection, the selected set is shown with big dots in Table 4(b). Table 4(c) shows the evolution of the population after 10 generations, we generate a large sample (small dots) and then select some of them to repopulate (big dots with a small dot inside). The big dots that have a small dot inside are new individuals selected to repopulate. The big dots without a small dot inside are individuals that have been preserved from the last generation. In Table 4(d) we can observe that the selected set (big dots with a small dot inside) adequately recovers the structure of the function landscape, this selected set will be preserved to the next generation, preserving as well, the information about the function landscape. Table 4(e) shows the population after 100 generations, the algorithm almost converges. At this resolution the population seems collapsed, but if we take a look at Table 4(f) which is a close up, we can see that the selected set (big dots) and the population (small dots) are well distributed in the promising area. These plots show how the EDA-SRP works, the truncation method promotes the convergence and reduction of the search region, the Maximin promotes the diversity in the population and selected set. The plots in this section show that our claims of generating high diversity solutions, and preserving informative solutions are well supported. Table 4(d), shows that the selected set (big dots) are individuals which contain sufficient information to determine the adequate structure, density and position of an adequate search distribution. It is clear that if the Normal distribution could better follow the selected set in Table 4(d) the algorithm becomes more efficient. This last statement is supported by the results, the EDA-SRP approximates the optimum with an error less than $1 \mathrm{e}-10$ using $87341.3 \pm 968.36 .2 .092 \mathrm{e} 6 \pm 1.5 \mathrm{e} 5$ and $280937.4 \pm 19656.7$ function evaluations, for the Sphere, Rosenbrock and Ackley functions respectively. The sphere is the problem which needs the minimum number of function evaluations for the EDA-SRP. That is to say, if the objective function is a single mode function with an ellipsoidal shape (just like the Normal distribution), the optimum is efficiently approached. The problems arise when the structure of the function is different from the structure of the Normal distribution.

### 5.1. Parameter settings

The user-given parameters for the EDA-SRP are the population size and the resampling rate $n_{r s}$. Using the Rosenbrock function, Fig. 1 shows the number of function evaluations needed to reach an objective value of $1 \mathrm{e}-10$, for $n_{r s}=3$ and $n_{r s}=4$. The minimum function evaluations are obtained for a population size of 160 .

As can be seen, this parameter does not have an important impact for this problem, in our experiments it is set to 3 , except for the Schwefel $f_{8}$. The reason is that $n_{r s}$ delivers an objective mean of $-10103.34 \pm 551.6$, which is worst than the one reported in Table 3. The explanation is that an small $n_{r s}$ parameter promotes faster convergence, this is supported by the smaller standard deviation for the Schwefel $f_{8}$ for $n_{r s}=3$. Our experiments suggest that $n_{r s}$ smaller than 3 is only useful for functions such as the sphere, which has a similar structure as the Normal. On the other hand, a $n_{r s}$ larger than 6 has no significant impact on the results, but it has impact on the computational cost. According to the boxplots in Fig. 1 we suggest an $n_{r s}=3$, in general, and $n_{r s}=4$ for multi-modal hard functions.

The second conclusion elucidated from Fig. 1, is that there is an optimal population size for the EDA-SRP. This second conclusion is supported by Fig. 2, the best objective function value is plotted versus the population size, the objective value axis is in log-scale. As can be observed when the population size is large enough the algorithm can find close approximations to the optimum, but the computational cost increases. The algorithm also is stopped if the number of evaluations reaches 1e5, hence some runs with the largest population sizes do not converge. Fig. 2, shows that the most effective population size is

Table 4
Several generations of a typical run of EDA-SRP with the Rosenbrock function.
![img-0.jpeg](img-0.jpeg)
between 160 and 240. Our recommendation is to set a small population size and increase it until the performance does not change. For the sake of completeness the success rate (ratio of successful runs) is $(0.533,0.7,1,0.97,0.87,0.97)$ for the population sizes of $(80,160,240,320,480,960)$ for $n_{\mathrm{rs}}=3$ and 1 e 5 function evaluations. And, $\{0.370 .5710 .930 .870 .77\}$, for $n_{\mathrm{rs}}=4$, the smaller success rate for the last runs can be explained by slower convergence when the re-sampling rate is increased. Finally, the success performance, defined as the mean of function evaluations of successful runs, divided by the suc-

![img-2.jpeg](img-2.jpeg)

Fig. 1. Boxplots for the number of function evaluations versus the population size for 30 independent runs of the EDA-SRP with the 5-D Rosenbrock function. Only successful runs are used (objective value $\leqslant 1 \mathrm{e}-10$ ). (a) Resampling rate $n_{\mathrm{rx}}=3$, (b) $n_{\mathrm{rx}}=4$.
![img-2.jpeg](img-2.jpeg)

Fig. 2. Boxplots for the best function value versus the population size for 30 independent runs of the EDA-SRP with the 5-D Rosenbrock function. All runs are used. (a) Resampling rate $n_{\mathrm{rx}}=3$, (b) $n_{\mathrm{rx}}=4$.
cess rate is $\{37153.70,38502.48,43636.77,48807.01,71299.90,87856.55\}$ and $\{142341.60,42728.43,41360.83$, $55620.69,71064.81,116295.65\}$ for $n_{\mathrm{rx}}=3$ and $n_{\mathrm{rx}}=4$. Notice how similar they are for the population size of 160 and 240, this confirms that the performance is robust to the $n_{\mathrm{rx}}$ parameter, and that an adequate population size can be found relatively easily.

# 5.2. Individual contribution of the enhancement techniques 

The goal of this section is twofold: Firstly we present a comparison among the proposal, a standard EDA, and the standard EDA enhanced with the techniques just proposed but once at a time. The purposes of this subsection are: to known what they can be used for, the individual contribution of each of them, and if it is possible to use only one of them which provides an specific behavior according to the problem at hand. Secondly, we show the performance of our proposal with other well known objective functions in order to provide a better understanding of it. The standard EDA used as basis for this comparison works as follows:

Table 5
Test problems used for comparing the effects and impacts in the performance of the different enhancement techniques proposed in this work.

1. Generate an initial population of $n_{\text {pop }}$ individuals by means of the uniform distribution in the search space.
2. Evaluate the population.
3. Select the best $n_{\text {pop }} / 2$ individuals in the population.
4. Estimate a Normal multivariate distribution by using the maximum likelihood estimator of the mean and covariance matrix given the selected set.
5. Sample the Normal model to get $n_{\text {pop }} / 2$ new individuals, evaluate them and combine them with the selected set to obtain the new population.
6. Repeat from step 3 .

The aim of this comparison is not to decide which algorithm performs the best, but to understand the effect contributed by each enhancement. We do not tune the parameters to avoid an unfair comparison, which could lead us to erroneous conclusions, due to the indistinguishable performance of the different versions of the algorithms. Additionally, the stopping criteria are: the covariance matrix norm must be less than $10^{-50}$, the covariance matrix must be numerically positive definite, and the number of evaluations must be less than $50 \times 10^{3}$. We use this values in order to show the performance of the different techniques. If more function evaluations are used, many of the algorithms does seem to perform similar, hence this values help to show the actual performance. The algorithms contrasted in this subsection are the following.

- EDA-Std. The standard EDA implemented as mentioned above.
- EDA-Init. Similar to the EDA-Stp, but modified in the initial population, which is generated according to the proposal in the EDA-SRP to improve the initial diversity and exploration.
- EDA-Rpop. The difference with the EDA-Std is the repopulation step. A large set of candidate solutions is generated, then some of them are rejected as in the EDA-SRP using the Maximin and the nearest neighbor weight. Neither the initialization, nor the weighted estimators, nor the truncation selection of the proposal are used.
- EDA-West. Is the EDA-Std but using the weighted estimators.
- EDA-Trunc. Is the EDA-Std but using the truncation method.
- EDA-SRP. Is the EDA with all the enhancements proposed in this article.

The objective functions used in this tests are show in Table 5. They are well known in global optimization, and most of them have been used to test the performance of Normal Multivariate EDAs [23].

The results are presented using violin plots in Fig. 3. The violin plots represent the density of the best solutions found in 15 independent runs. They deliver an accurate idea about the variance of the solutions and the actual positions. Violin plots can help to compare the density of the best solutions found by different algorithms instead of a single value such as the mean, additionally the mean value can be also graphically compared (the white dot in the middle of the violin). This kind of comparison seems quite fair or at least more complete than a punctual one. For sake of completeness we present the mean and standard deviation of this comparison in Table 6.

# 5.3. Discussion about comparison of different techniques 

Looking at Fig. 3 and Table 6 we can notice that the Ackley function is solved by all the algorithms but the EDA-Rpop which has the component of the selective repopulation. Considering that the EDA-SRP does not converges as close as the other algorithms, we can conclude that the convergence of the algorithms with repopulation is slower than the others. Additionally, we can infer that the EDA-SRP has an extra component which leads it to a faster convergence than the EDA-Rpop. The functions: Cigar, Cigar Tablet, Ellipsoid and Two Axes present a similar pattern, the best performed algorithm in these

![img-3.jpeg](img-3.jpeg)

Fig. 3. Comparison of different techniques used in this paper to improve the EDA performance.

Table 6
Mean and (Standard deviation), for different test problems, and algorithms modified with the different techniques proposed in this article.

cases are the EDA-SRP and EDA-Rpop. A common characteristic of these test functions is that the variables have a quite different weight in the objective function, the EDA-Std reduces the variance in all directions equally, as consequence it suffers of premature convergence because it favors the highly weighted variables. The different powers function shows that the truncation method in EDA-Trunc could favor the premature convergence if it is not used together with a technique which favors the exploration. On the other hand, Griewank function in Table 6 shows that the best performed algorithm is the one equipped with the truncation method, and the worst performed algorithm are the ones with the repopulation technique. Summarizing, using the information collected from all the algorithms we can conclude that: the truncation method favors convergence or exploitation of the information, while the repopulation method favors exploration. The weighting procedure equips the EDA with a more efficient estimation-sampling step, in the sense that it consistently shows a lower objective function than the other algorithms, hence, with less function evaluations it estimates better than the others the optimum, note that the violin plot of EDA-West consistently is smaller (low variance) and lower (better objective) than the others. Finally, Rosenbrock function shows that the techniques proposed in this work could result in a balance between exploration and exploitation when used together.

# 6. Conclusions 

The EDA proposed in this work intends to circumvent important issues of classical Normal EDAs, such as diversity preservation and preservation of the necessary information about the fitness landscape. Notice that this proposal does not guarantee that the population or the selected set actually are Normally distributed, because of the selective re-population and preservation of the fittest individuals. Instead, we intend to preserve solutions which indicate the function landscape in the most promising regions, additionally, we intend to sample candidate solutions as diverse as possible. These concepts could be different from the standard estimating and sampling process, which uses parametric distributions to fit the selected set and sample similar solutions to those already known. As a possible negative effect of the EDA-SRP way of working, is the loss of the direct relationship between the search distribution and the population. On the other hand, an advantage is that the Normal distribution is only an engine to generate random candidate solutions, thus we expect similar promising results if other sampling engines are used, or if we apply the same idea in other domains. This means that the ideas in this article can be extended to other kinds of problems and/or algorithms. The EDA-SRP is competitive with similar EDAs and classical approaches as is shown in the experiments performed. We have shown that the obtained results are even better than the results obtained by more complex models based on Normal mixtures. In addition, the EDA-SRP uses a small population size, which indicates that it uses the information better than other approaches, and generates more informative candidate solutions. A small sized population also impacts in the memory and the computational cost used by the algorithm (the Maximin is quadratic with the population size). The experiments conducted suggest that the truncation selection promotes convergence while the Maximin selection leads to a smooth and slow convergence as a payoff of maintaining individuals with high diversity.

Notice that our proposal inserts techniques that are not dependent on a Normal Multivariate model, and in some of the cases, neither to a continuous search space. Hence, the Maximin ranking, the truncation method, the weighted estimators and preselection of candidate solutions to be evaluated, as well as a diverse initialization are ideas that can be used in other population based algorithms.

A conceptual conclusion is the need to look for search engines which intensively sample the most promising regions, while sampling candidate solutions with high diversity. Neither maximum likelihood (ML) estimation, nor some variance

scaling techniques seem to follow this paradigm. Researchers have advised that Normal EDAs must use the covariance matrix which improves the results, instead of the one which fits the selected set [12,8,10,11,23,24]. They also have avoided evaluating all the individuals, by discriminating the non-promising ones, according to predictions delivered by local models [20]. In this article we use the mentioned strategies and add two more: (1) we avoid evaluating individuals that are in regions that have been already evaluated by using the Maximin algorithm and, (2) we preserve valuable information about the objective function structure.

The general conclusion is to generate and to preserve informative individuals. Such informative individuals must provide information that no other individual in the population provides, locally each of them must be isolated, if not, such information is redundant. Furthermore, the information provided by the individuals must be valuable for the search process, that is to say, it must help to elucidate the objective function landscape and, eventually, the optimum position. The EDA-SRP is a proposal that agrees with this conclusion, but obviously, other strategies could be followed to perform similar improvements.

Future work will contemplate a discrete version of the EDA-SRP, the use of Normal mixtures and local meta-models [20] instead of the simple ranking scheme, to reduce the number of function evaluations.

```
Algorithm 1: Maximin algorithm to rank solutions according their diversity.
    Input:
    R Set of reference points, where \(r_{j} \in R, j=1 . . n r\);
    \(X\) Points to be ranked, where \(x_{i} \in X, i=1 . . n x\);
    near Number of dimensions.
    for \(i=1 . . n x\) do
    \(d_{i}=\min _{j}\left(\right.\) euclidian_distance \(\left.\left(x_{i}, r_{j}\right)\right)\);
    for \(i=1 . . n x\) do
        \(i^{\max }=k\) such that \(d_{k} \geq d_{i} \forall i \in\{1,2, . ., n x\}\)
        \(\operatorname{Rank} k_{i \max }=i\)
        \(d_{i \max }=-1\)
        for \(j=1 . . n x\) do
            if \(d_{j}>-0.1\) then
            \(\left.\quad d_{j}=\min \left(d_{j}\right.\right.\), euclidian_distance \(\left.\left(x_{i \max }, x_{j}\right)\right)\)
    Output:
    Rank A rank attached to each point in the \(X\) set;
```

Algorithm 2: Truncation method to ensure an increasing mean (bounded by an increasing sequence) of the objective function and convergence to the elite individual. Maximization case.

# Input: 

$F$ vector of objective function values of size $n$;
$\theta^{t}$ a threshold, for the first selection $\theta^{0}=\min (F)$;
$1 I \leftarrow \operatorname{sort}(F$, decreasing,return_index $)$;
$2 \epsilon \leftarrow 1 e-14\left(\max \left(\left|F_{I_{0}}\right|,\left|F_{I_{n}}\right|,\left|F_{0}-F_{n}\right|\right)\right)$;
a $k \leftarrow n / 2$;
4 while $k>0.05 n \& F_{I_{k}}<\left(\theta^{t}+\epsilon\right)$ do
$5 \quad k \leftarrow k-1$
$6 \theta^{t+1} \leftarrow F_{I_{k}}$;
Output:
$I_{1: k}$ vector of indexes of selected individuals of size $k$;
$\theta^{t+1}$ threshold for the next selection;

# Algorithm 3: Normal multivariate EDA with selective repopulation. 

$1 \hat{X} \leftarrow \operatorname{uniform}\left(6 n_{r s} \cdot n_{\text {pop }}, x_{\text {inf }}, x_{\text {sup }}\right)$;
$2 R \leftarrow$ reference_points $\left(\hat{X}, x_{\text {inf }}, x_{\text {sup }}\right)$;
$3 n_{S} \leftarrow \operatorname{sizeof}(R)$;
$4 X \leftarrow \operatorname{maximin} \_$selection $(\hat{X}, R)$;
$5 F \leftarrow \operatorname{evaluation}(X)$;
$6 I \leftarrow$ truncation_selection $(F)$;
$7 W \leftarrow$ weight_computation $(F[I])$;
$8 R \leftarrow X[I]$;
$9 F_{R} \leftarrow F[I]$;
10 Compute $\mu$ and $\Sigma$ using $W$;
11 while $|\Sigma|>\epsilon_{\text {tol }} \& \max _{\text {eval }}<n_{\text {eval }}$ do
$12 \quad \hat{X} \leftarrow \operatorname{Normal}\left(n_{r s} \cdot n_{\text {pop }}, \Sigma, \mu, x_{\text {inf }}, x_{\text {sup }}\right)$;
$13 \quad \operatorname{Rank}^{\text {maximin }} \leftarrow \operatorname{maximin} \_$ranking $(\hat{X}, R)$;
//Computing a rank to select the individuals to be evaluated
for $j=1 . . n_{\text {pop }}$ do
$k=$ nearest_neighbor $\left(R, \bar{x}_{j}\right)$;
Rank $k_{j}^{*}=\frac{\left(n_{S}\right)}{\operatorname{Rank}_{j}^{\text {maximin }}}$
//Copying the first $\left(n_{\text {pop }}-n_{S}\right)$ indices to $J$
$J \leftarrow \operatorname{sort}\left(\right.$ Rank $^{*}$, decreasing,return_index $\left)[1:\left(n_{\text {pop }}-n_{S}\right)\right]$;
$F \leftarrow \operatorname{evaluation}(\hat{X}[J])$;
//Repopulating
$X \leftarrow R \cup \hat{X}[J]$;
$F \leftarrow F_{R} \cup \hat{F}$;
$I \leftarrow$ truncation_selection $(F)$;
$x_{\text {best }} \leftarrow X[I \mid 0]]$
$R \leftarrow X[I]$
$F_{R} \leftarrow F[I]$
$n_{S} \leftarrow \operatorname{sizeof}(R)$;
$W \leftarrow$ weight_computation $(F)$;
Compute $\mu$ and $\Sigma$;
Output:
$x_{\text {best }}$ Best optimum approximation.
