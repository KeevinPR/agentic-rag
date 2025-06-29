# MOPED: A Multi-objective Parzen-Based Estimation of Distribution Algorithm for Continuous Problems 

Mario Costa ${ }^{1}$ and Edmondo Minisci ${ }^{2}$<br>${ }^{1}$ Department of Electronics, Polytechnic of Turin, C.so Duca degli Abruzzi, 24, 10129 Turin, ITALY<br>mario.costa@polito.it<br>${ }^{2}$ Department of Aerospace Engineering, Polytechnic of Turin, C.so Duca degli Abruzzi, 24, 10129, Turin, ITALY<br>edmondo_minisci@yahoo.it


#### Abstract

An evolutionary multi-objective optimization tool based on an estimation of distribution algorithm is proposed. The algorithm uses the ranking method of non-dominated sorting genetic algorithm-II and the Parzen estimator to approximate the probability density of solutions lying on the Pareto front. The proposed algorithm has been applied to different types of test case problems and results show good performance of the overall optimization procedure in terms of the number of function evaluations. An alternative spreading technique that uses the Parzen estimator in the objective function space is proposed as well. When this technique is used, achieved results appear to be qualitatively equivalent to those previously obtained by adopting the crowding distance described in non-dominated sorting genetic algorithm-II.


## 1 Introduction

The extensive use of evolutionary algorithms in the last decade demonstrated that an optimization process can be obtained by combining effects of interactive operators such as selection - whose task is mainly to identify the best individuals in the current population - and crossover and mutation, which try to generate new and better solutions starting from the selected ones. But, if the mimicking of natural evolution in living species has been a source of inspiration of new strategies, the attempt to copy natural techniques as they are sometimes introduces a great complexity without a corresponding improvement of algorithms performance. Moreover standard evolutionary algorithms can be ineffective when problems exhibit a high level of interaction among variables. This is mainly due to the fact that recombination operators are likely to disrupt promising sub-structures of optimal solutions.

Alternatively, in order to make a rational use of the evolutionary metaphor and/or to create optimization tools that are able to handle very hard problems (with several parameters, with difficulties in linkage learning, deceptive), some algorithms have been proposed that automatically learn the structure of the search space. Following this way, several works, based on explicit probabilistic-statistic tools, have been carried out.

Generally, these methods, starting from results of current populations, try to identify a probabilistic model of the search space, and crossover and mutation operators are replaced with sampling. Those methods have been named Estimation of Distribution Algorithms (EDAs).

Most EDAs have been developed to manage optimization processes for monoobjective, combinatorial problems, but several works regarding problems in continuous domains have been proposed.

We can distinguish three types of EDAs depending on the way the probabilistic model is built: a) without dependences among variables ([1] - [4]); with bivariate dependences among variables ([5] - [7]); c) with multivariate dependences ([8] [10]).

Recently, EDAs handling multi-objective optimizations have been proposed. References [11] and [12] respectively extend the mono-objective version in [10] and [8]. They describe the algorithms and present some results when applied to well known test problems.

In this paper we propose a multi-objective optimization algorithm for continuous problems that uses the Parzen method to build a probabilistic representation of Pareto solutions, with multivariate dependences among variables.

Notwithstanding main features can be used for single-objective optimization, because of future practical applications in our case the algorithm has been directly developed for multi-objective problems. Similarly to what was done in [12] for multiobjective Bayesian Optimization Algorithm (BOA), the already known and implemented techniques of Non Dominated Sorting Genetic Algorithm II (NSGA-II) [13] are used to classify promising solutions, while new individuals are obtained by sampling from the Parzen model.

The Parzen method, as introduced in the next section, can appear analogous to the normal kernel method described and used in [10]. Actually, the two methods are different and, even if both put kernels on each sampled point, our method uses classical Parzen dictates to set terms of the covariance matrix (non-diagonal) of kernels in order to directly approximate the joint Probability Density Function (PDF).

A brief introduction on the general problem of building probabilistic models is followed by a description of the main characteristics of the Parzen method. In section 3 the structure of the algorithm and the practical implementation are discussed; results of application to test cases are detailed and an alternative spreading technique is briefly described. A final section of concluding remarks summarizes the present work and indicates future developments.

# 2 Parzen Method 

When dealing with continuous-valued random variables, most statistical inferences rely on the estimation of PDFs and/or associated functionals from a finite-sized sample. Whenever something is known in advance about the PDF to be estimated, it is worth exploiting that knowledge as much as we can in order to shape a specialpurpose estimator. In fact any additional information we are able to implement in the estimator as a built-in feature is equivalent to some effective increase in the sample size. Otherwise stated, in so doing we improve the estimator's efficiency.

In the statistician's wildest dream some prime principles emerge and dictate that the true PDF must belong to a certain parametric family of model PDFs. This restricts the set of admissible solutions to a finite-dimensional space, and cuts the problem down to the identification of the parameters thereby introduced. In fact parametric estimation is so appealing that few popular families of model PDFs are applied almost everywhere even in lack of any guiding principle, and often little effort is made to check their actual faithfulness. On the other hand, a serious check has to rely on composite hypothesis tests that are like to be computationally very expensive.

While designing an EDA for general-purpose multi-objective optimization there is really no hint on how the true PDF should look like. For instance, that PDF could well have several modes, whereas most popular models are uni-modal. The possible occurrence of multiple modes is usually handled through mixtures of uni-modal kernel PDFs. Since the "correct" number of kernels is not known in advance, the size of the mixture is optimized (e.g. by data clustering) just like any other parameter: that is, the weight and the inner parameters of each kernel.

The usage of mixtures does however not alleviate us from worrying about faithfulness. Otherwise stated, the choice of the parametric family the kernels belong to still matters. In fact the overall number of parameters (and therefore the number of kernels) must grow sub-linearly with the sample size $n$, or else the variance of the resulting estimator would not vanish everywhere as $n \rightarrow \infty$, thus precluding ubiquitous converge to the true PDF in the mean square sense. But if that condition is met, then even a single "wrong" kernel can spoil convergence wherever it injects some bias. This is nothing but another form of the well-known bias-variance dilemma.

The Parzen method [14] pursues a non-parametric approach to kernel density estimation. It gives rise to an estimator that converges everywhere to the true PDF in the mean square sense. Should the true PDF be uniformly continuous, the Parzen estimator can also be made uniformly consistent. In short, the method allocates exactly $n$ identical kernels, each one "centered" on a different element of the sample. In contrast with parametric mixtures, here no experimental evidence is spent to identify parameters. This is the reason why the presence of so many kernels does not inflate the asymptotic variance of the estimator. As a consequence, the detailed shape of the kernels is irrelevant, and the faithfulness problem is successfully circumvented. Of course some restrictions are in order: here is a brief explanation.

Let $z$ be a real-valued random variable. Let $p^{z}(\cdot): \Re \rightarrow \Re, \cup\{0\}$ be the associated PDF. Let $\boldsymbol{D}_{n}=\left\{z_{1}, \ldots, z_{n}\right\}$ be a collection of $n$ independent replicas of $z$. The empirical estimator $\hat{\boldsymbol{p}}_{n}^{E}(\cdot)$ of $p^{z}(\cdot)$ based on $\boldsymbol{D}_{n}$ is defined as follows:

$$
\forall z \in \Re \quad \hat{\boldsymbol{p}}_{n}^{E}(z)=\frac{1}{n} \sum_{i=1}^{n} \delta\left(z-z_{i}\right)
$$

The estimator just defined is unbiased everywhere but it converges nowhere to $p^{z}(\cdot)$ in the mean square sense because $\operatorname{Var}\left[\hat{\boldsymbol{p}}_{n}^{E}(z)\right]=\infty$ irrespective of both $n$ and $z$. This last result is not surprising, since the Dirac's delta is not squared integrable.

The Parzen estimator $\hat{\boldsymbol{p}}_{n}^{S}(\cdot)$ of $p^{z}(\cdot)$ based on $\boldsymbol{D}_{n}$ is obtained by convolving the empirical estimator with some squared integrable kernel PDF $g_{s}(\cdot)$ :

$$
\forall z \in \Re \quad \hat{\boldsymbol{p}}_{n}^{S}(z)=\int_{-\infty}^{\infty} \hat{\boldsymbol{p}}_{n}^{E}(x) \frac{1}{h_{n}} g_{S}\left(\frac{z-x}{h_{n}}\right) d x=\frac{1}{n} \sum_{i=1}^{n} \frac{1}{h_{n}} g_{S}\left(\frac{z-z_{i}}{h_{n}}\right)
$$

The kernel acts as a low-pass filter whose "bandwidth" is regulated by the scale factor $h_{n} \in \Re_{s}$. It exerts a "smoothing" action that lowers the sensitivity of $\hat{\boldsymbol{p}}_{n}^{S}(z)$ w.r.t. $\boldsymbol{D}_{n}$ so as to make $\operatorname{Var}\left[\hat{\boldsymbol{p}}_{n}^{S}(z)\right]<\infty \quad \forall z \in \Re$. Thus for any given sample size the larger is the scale factor, the smaller is the variance of the estimator. But the converse is also true: since $\hat{\boldsymbol{p}}_{n}^{S}(z)$ is nothing but a mean, then for any given scale factor the larger is the sample size, the smaller is the variance of the estimator (indeed it is inversely proportional to the sample size). Both statements are in fact special cases of the following property:

$$
\forall z \in \Re \quad \lim _{n \rightarrow \infty} n d_{n}=\infty \Rightarrow \lim _{n \rightarrow \infty} \operatorname{Var}\left[\hat{\boldsymbol{p}}_{n}^{S}(z)\right]=0
$$

On the other hand, the same smoothing action produces an unwanted "blurring" effect that limits the resolution of the approximation. Intuitively the scale factor should therefore vanish as $n \rightarrow \infty$ in order to let the estimator closely follow finer and finer details of the true PDF. Also this last remark finds a precise mathematical rendering in the following property:

$$
\forall z \in \Re \quad \lim _{n \rightarrow \infty} d_{n}=\infty \Rightarrow \lim _{n \rightarrow \infty} E\left[\hat{\boldsymbol{p}}_{n}^{S}(z)\right]=p^{S}(z)
$$

To summarize, the conflicting constraints dictated by the bias-variance dilemma can still be jointly satisfied by letting the scale factor decrease slowly enough as the sample size grows. The resulting estimator converges everywhere to the true PDF in the mean square sense irrespective of the kernel employed, provided that it is squared integrable.

The above results were later extended to the multi-variate case by Cacoullos [15].

# 3 Parzen EDA 

The main idea of the work is the use of the Parzen method to build a probabilistic model and to sample from the estimated PDF in order to obtain new promising solutions. A detailed description of the Multi-Objective Parzen EDa (MOPED algorithm) follows, and some results are presented in order to show capabilities and potentialities of the algorithm.

Moreover, an extensive use of the Parzen method could lead to simplify the overall optimization procedure towards a parameter-less tool. As a first step in this direction, at the end of section we introduce a different spreading technique for solutions in the Pareto front.

# 3.1 General Algorithm 

As summarized in figure 1, the general optimization procedure can be described as follows:

1. Starting: $\mathrm{N}_{\text {ind }}$ individuals are sampled from a uniform $m$-dimensional PDF.
2. Classification \& Fitness evaluation: by using NSGA-II techniques [13], individuals of current population are ranked and ordered in terms of dominance criterion and crowding distance in the objective function. A fitness value, linearly varying from $2-\alpha$ (best individual) to $\alpha$ (worst individual), with $0<\alpha<1$, is assigned to each individual.
![img-0.jpeg](img-0.jpeg)

Fig. 1. General structure of the algorithm
3. Building model \& sampling: on the basis of information given by $\mathrm{N}_{\text {ind }}$ individuals, by means of the Parzen method a probabilistic model of promising search space portion is built. For generic processes can be useful adopting different kernels alternatively from a generation to the other in order to obtain an effective exploration. In this work Gauss and Cauchy distributions are used. Actually, these types of kernel, for their intrinsic characteristics, are complementary and results will show that the use of only one of them could be inefficient for some problems.

From the probabilistic model so determined, $\tau \mathrm{N}_{\text {ind }}$ new individuals are sampled. Fitness values are used to calculate variance of kernels (the fitness values are related to the scale factors introduced in section 2) and to favor sampling from most important kernels.
4. Evaluation: New $\tau \mathrm{N}_{\text {ind }}$ individuals are evaluated in terms of objective functions.
5. Classification \& Fitness evaluation: following NSGA-II criteria, individuals of intermediate population, of which dimension is $(1+\tau) N_{\text {ind }}$, are ordered. A fitness value, linearly varying from $2-\alpha$ (best individual) to $\alpha$ (worst individual), with $0<\alpha<1$, is assigned to each individual.
6. New population: best $\mathrm{N}_{\text {ind }}$ individuals are selected to be next generation.
7. EXIT or NEXT ITER: if convergence criteria are achieved the algorithm stops, otherwise it restarts from point 3.
The algorithm presented above demonstrated satisfactory performance in solving several test cases, when performance is measured in terms of objective function evaluations to obtain a good approximation of the Pareto front. Some results will be shown in the next paragraph.

The still open question is finding an efficient convergence criterion that could be adopted for a generic optimization. That is finding a convergence criterion that guaranties an optimal approximation of Pareto front (efficacy) and requires a number of objective function evaluations as low as possible (efficiency).

Following results show that neither the maximum generation number nor all of the individuals in first class are without gaps. The former because of an extremely low efficiency if a too high maximum number of generations is used, the latter because of premature convergence on a local, non-optimal, front.

Consequently, the maximum generation number is always used. An upper limit for iteration is imposed as suggested from literature results, even if this kind of stopping criterion makes the algorithm inefficient.

# 3.2 Test Cases Results 

In order to have some ideas regarding effectiveness and efficiency of the method, the proposed algorithm has been applied to some well-known test problems taken from literature [16].

For all of test cases 10 independent runs have been performed and results in terms of number of function evaluations are given as average values.

As said in the previous description of the algorithm, in absence of an effective and efficient criterion a maximum number generation criterion has been adopted. In order to allow comparison with obtained results in literature, our results are presented in terms of effective number of iteration, or better, in terms of number of functions evaluations required to obtain the approximation of the optimal front as well. Mainly, results will be compared with those achieved in [11] by using the Multi-objective Mixture-based Iterated Density Estimation Evolutionary Algorithm (MIDEA).

All tests have been run with the same values of the following parameters: a) the number of individuals $\left(\mathrm{N}_{\text {ind }}=100\right)$, the sampling parameter $(\tau=2)$, and the fitness parameter $(\alpha=0.2)$.

For the sake of simplicity, considered problems are reported in Table 1, which for each problem shows type of problem (minimization or maximization) and number of parameters, objective functions and limits of parameters.

Table 1. Test cases problems

| Type \& $m$ | Objective functions | Limits |
| :--: | :--: | :--: |
| $\min , m=3$ | $\operatorname{MOP2}\left\{\begin{array}{l} f_{1}(x)=1-\exp \left(-\sum_{i=1}^{m}\left(x_{i}-\frac{1}{\sqrt{m}}\right)^{2}\right) \\ f_{2}(x)=1-\exp \left(-\sum_{i=1}^{m}\left(x_{i}+\frac{1}{\sqrt{m}}\right)^{2}\right) \end{array}\right.$ | $\begin{aligned} & -4 \leq x_{i} \leq 4, \\ & \mathrm{i}=1, \ldots, m \end{aligned}$ |
| $\min , m=3$ | $\operatorname{MOP4}\left\{\begin{array}{l} f_{1}(x)=\sum_{i=1}^{m-1}\left(-10 \exp \left(-0.2 \sqrt{x_{i}^{2}+x_{i+1}^{2}}\right)\right) \\ f_{2}(x)=\sum_{i=1}^{m}\left(x_{i}\right)^{0.8}+5 \sin \left(x_{i}\right)^{3}\end{array}\right.$ | $\begin{aligned} & -5 \leq x_{i} \leq 5, \\ & \mathrm{i}=1, \ldots, m \end{aligned}$ |
| $\min , m=10$ | $\operatorname{EC4}\left\{\begin{array}{l} f_{1}(x)=x_{1} \\ f_{2}(x)=g\left(1-\sqrt{\frac{x_{1}}{g}}\right) \\ g(x)=91+\sum_{i=2}^{m}\left(x_{i}^{2}-10 \cos \left(4 \pi x_{i}\right)\right) \end{array}\right.$ | $\begin{aligned} & 0 \leq x_{i} \leq 1 ; \\ & -5 \leq x_{i} \leq 5, \\ & \mathrm{i}=2, \ldots, m \end{aligned}$ |
| $\min , m=10$ | $\operatorname{EC6}\left\{\begin{array}{l} f_{1}(x)=1-\exp \left(-4 x_{1}\right) \sin \left(6 \pi x_{1}\right)^{6} \\ f_{2}(x)=g\left(1-\left(\frac{f_{1}}{g}\right)^{2}\right) \\ g(x)=1+\theta\left(\sum_{i=2}^{m} \frac{x_{i}}{9}\right)^{0.25} \end{array}\right.$ | $\begin{gathered} 0 \leq x_{i} \leq 1, \\ \mathrm{i}=1, \ldots, m \end{gathered}$ |

Figure 2 shows one of the fronts obtained for the MOP2 problem. The process stops after 15 iterations, that means 3,100 function evaluations, but from graphical results displayed during the run, it is possible to see that solutions remain the same after 9.75 (average value) iterations, or 2,062 function evaluations. For this problem MIDEA gives an approximation of the optimal front after 3,754 function evaluations.

In figure 3 one of the fronts obtained for the MOP4 problem is shown in the upper left corner. The other three parts of the figure represent the marginal bivariate PDFs of variables when normal kernels are used. The triple structure of the approximated front can be identified from every marginal PDF, even if for this run it is more evident in the $x_{i}-x_{s}$ PDF.

For this problem a maximum number of iterations is set equal to 55 (11,100 function evaluations), but still in this case in order to have a stable configuration of

the solutions a less number of iterations is needed, which is 44.9 ( 9,090 function evaluations). In [11] MIDEA requires 10,762 function evaluations in the best case when objective clustering is adopted.
![img-2.jpeg](img-2.jpeg)

Fig. 2. Obtained non-dominated solutions on MOP2 problem
![img-2.jpeg](img-2.jpeg)

Fig. 3. MOP4 problem. In the left upper corner non-dominated solutions in the objective plain are shown. The other three parts of the figure show the marginal bivariate PDFs of problem's variables when normal kernels are used

Problems EC4 and EC6 are more complex and a presentation of relative results allows a deeper discussion of advantages and gaps of the proposed algorithm.

EC6 is presented as a problem that tests the ability of algorithms to spread solutions on the whole front. MOPED demonstrates to be able to cover the entire optimal range, even if most of runs produce one or two sub-optimal solutions on the left part of the Pareto front. What happens is similar to the results of the Strength Pareto Evolutionary Algorithm (SPEA) when applied to the same problem as reported in [13].

For both EC4 and EC6 we know that achievement of optimal front corresponds to $g(x)=1$. Therefore, for these problems we adopted the following exit criterion: when the $g(x)$ value averaged on the whole population is $\leq 1.01$, this allows to have an error less that $1 \%$.

For EC6 problem we imposed 15,000 maximum function evaluations, but the convergence criterion related to $g(x)$ function has been reached after approximately 8,300 evaluations. For this problem MIDEA needs 8,426 function evaluations to obtain the front with no clustering, but better results (2,284 evaluations) can be obtained if conditionals dependencies among variables are not learned.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Obtained non-dominated solutions on EC6 problem. Most of obtained fronts display some sub-optimal solutions
![img-4.jpeg](img-4.jpeg)

Fig. 5. Obtained non-dominated solutions on EC4 problem

Problem EC4 is the hardest in terms of number of function evaluations needed to reach the true optimal front. Because of the form of the functions to optimize, process tends to get stuck on sub-optimal fronts.

Results demonstrate that the optimal solution (figure 5 shows one of the fronts) can be obtained after 153,710 function evaluations, with a minimum value of 66,100 in one of the ten runs, and a maximum of 244,100 , when the upper limit of function evaluations is set to 300,000 . In this case MIDEA needs at the best $1,019,330$ function evaluations when objective clustering is used. For this problem ignoring conditional dependences among variables can be useful for MIDEA as well; with a mixture of univariate factorizations caching the front needs only 209,635 evaluations.

For EC4 problem NSGA-II acts much better than both the algorithms (MOPED and MIDEA) [13]. It is able to bring the population to the front with less then 25,000 evaluations if an ad hoc parameter setting is used.

From figure 6, which shows a general trend of $g(x)$ function, it is possible to see how the process goes on. Ranges with null slope mean a transitorily convergence on a local Pareto-optimal front. In order to allow some comparison we monitored the $g(x)$ function and it reaches the value of 3 after 40,862 objective function evaluations.
![img-5.jpeg](img-5.jpeg)

Fig. 6. General trend of $g(x)$ function for EC4 problem. On the left the trend during the whole process is shown. On the right side, last part of the process allows a deeper comprehension of difficulties in terms of function evaluation to jump from a local front to a better one
![img-6.jpeg](img-6.jpeg)

Fig. 7. General trend of $g(x)$ function for EC6 problem when only Cauchy PDF is used

As anticipated in the previous paragraph describing the algorithm, use of only one type of kernel (with other parameters and structures fixed) could make the procedure ineffective or, at the most, inefficient. Figure 7 represents the $g(x)$ function trend on EC6 problem, when in the structure algorithm Cauchy PDF is the only used kernel. Clearly, in this case the optimization process has difficulties to converge to the optimal front, even if we allow a higher number of function evaluations.

On the other hand some results allow thinking that a different scheduling sequence of kernels could provide results better than presented ones. It will be subject of future investigations.

# 3.3 Alternative Spreading Technique 

In the original version of the algorithm, in order to spread solutions on the whole Pareto optimal front the crowding distance technique is used as described in reference [13]. Alternatively it is possible to use Parzen itself to measure the degree of crowding of solutions in order to favour most isolated individuals.

In section 2, where Parzen method is described, we can see that probability density in a point of the $m$-variable space is related to density of kernels around the point. In this way, if we estimate the PDF. of solutions in the space of objective functions, instead that in the space of $m$ variables, and we evaluate the probability density for each solution, we actually measure the crowding. This technique replaces the local crowding distance used in NSGA-II by a global one. Studies of theoretical main differences between local and global crowding measure are still in progress. However, the proposed method demonstrates to be able to spread solutions in the front for EC6 problem (figure 8 shows one of the obtained fronts).
![img-7.jpeg](img-7.jpeg)

Fig. 8. Obtained non-dominated solutions on EC6 problem when Parzen is used to spread solutions in the Pareto front

## 4 Conclusions

Here we have presented a new estimation of distribution algorithm that is able to manage multi-objective problems following Pareto criterion. The algorithm uses the

Parzen method in order to create a non-parametric, model-independent probabilistic representation of promising solutions in the search space. Results obtained when the algorithm is applied to well-known test cases show good performance of the optimization process in terms of the number of objective function evaluations and in the spreading of solutions on the whole front.

Showed results allow some comparisons with the best ones obtained in [11] by using MIDEA which appears to be the most similar algorithm. Except for the EC4 problem the reported values are fairly similar. But both works lack a measure of the degree of approximation of the true Pareto front. This could allow deeper considerations.

In this paper an alternative method to spread solutions is also proposed. It uses the Parzen method in the objective space to identify crowding level of individuals. Results are comparable with those obtained through NSGA-II crowding measure.

Contrary to previous works, in this paper we do not attempt to identify a conditionally independent structure in the genome. We know that this may increase the efficiency of the Parzen estimator. It is our intention to address this important point in the future along a frequentist approach with minor changes in the underlying philosophy. In fact the hypothesis testing inherent in the frequentist approach allows the user to impose a known error of the first kind.

For that said above, this work can be seen as the first step towards a more complex and efficient algorithm able to manage multi-objective optimization problems, with constraints too.

# References 

1. Mühlenbein, H., The equation for the response to selection and its use for prediction, Evolutionary Computation 5(3), pp. 303-346, 1998.
2. Baluja, S., Population based incremental learning: A method for integrating genetic search based function optimization and competitive learning (Tech. Rep. No. CMU-CS-94-163). Pittsburgh, PA: Carnegie Mellon University, 1994.
3. Harik, G. R., Lobo, F. G., and Goldberg, D. E., The compact genetic algorithm, In Proceedings of the International Conference on Evolutionary Computation 1998, pp. 523528, Piscataway, NJ: IEEE Service Center, 1998.
4. Sebag, M., Ducoulombier, A., Extending population-based incremental learning to continuous search spaces, In Parallel Problem Solving from Nature PPSN V, pp. 418-427, Berlin: Springer Verlag, 1998
5. De Bonet, J. S., Isbell, C. L., and Viola, P., MIMIC: Finding optima by estimating probability densities. In Mozer, M. C., Jordan, M. I., \& Petsche, T. (Eds.), Advances in Neural Information Processing Systems, Vol. 9, pp. 424, The MIT Press, Cambridge, 1997.
6. Baluja, S., Davies, S., Using optimal dependency-trees for combinatorial optimization: Learning the structure of the search space. In Proceedings of the 14th International Conference on Machine Learning, pp. 30-38, Morgan Kaufmann, 1997.
7. Pelikan, M., Mühlenbein, H., The bivariate marginal distribution algorithm. In Roy, R., Furuhashi, T., \& Chawdhry, P. K. (Eds.), Advances in Soft Computing Engineering Design and Manufacturing, pp. 521-535, London: Springer-Verlag, 1999.
8. Mühlenbein, H., Mahnig, T., The Factorized Distribution Algorithm for Additively Decomposed Functions, Proceedings of the 1999 Congress on Evolutionary Computation, pp. 752-759, 1999,

9. Pelikan, M., Goldberg, D. E., and Cant'u-Paz, E. (1999). BOA: The Bayesian optimization algorithm. In Banzhaf, W., Daida, J., Eiben, A. E., Garzon, M. H., Honavar, V., Jakiela, M., \& Smith, R. E. (Eds.), Proceedings of the Genetic and Evolutionary Computation Conference GECCO-99, Vol. I, pp. 525-532. Orlando, FL, Morgan Kaufmann Publishers, San Francisco, CA, 1999.
10. Bosman, P.A.N., Thierens, D., Expanding from discrete to continuous estimation of distribution algorithms: The IDEA, in M. Schoenauer, K. Deb, G. Rudolph, X. Yao, E. Lutton, J.J. Merelo, and H.-P. Schwefel, eds., Parallel Problem Solving from Nature, pp 767-776, Springer, 2000.
11. Thierens, D., Bosman, P.A.N., Multi-Objective Mixture-based Iterated Density Estimation Evolutionary Algorithms L. Spector, E.D. Goodman, A. Wu, W.B. Langdon, H.-M. Voigt, M. Gen, S. Sen, M. Dorigo, S. Pezeshk, M.H. Garzon and E. Burke, editors, Proceedings of the Genetic and Evolutionary Computation Conference - GECCO-2001, pages 663670, Morgan Kaufmann Publishers, 2001.
12. Khan, N., Goldberg, D.E., and Pelikan, M., Multi-Objective Bayesian Optimization Algorithm, IlliGAL Report No. 2002009, March 2002.
13. Deb, K., Pratap, A., Agarwal, S., and Meyarivan, T., A fast and elitist Multiobjective Genetic Algorithm: NSGA-II, IEEE Transactions on Evolutionary Computation, Vol. 6, No. 2, April 2002.
14. Parzen, E., On Estimation of a Probability Density Function and Mode, Ann. Math. Stat., Vol. 33, pp. 1065-1076, 1962.
15. Cacoullos, T., Estimation of a Multivariate Density, Ann. Inst. Stat. Math., Vol. 18, pp. $179-189,1966$.
16. Deb, K., Multi-Objective Genetic Algorithm: Problem Difficulties and Construction of Test Problems, Evolutionary Computation, Vol. 7, No. 3, pp. 205-230, The MIT Press, 1999.