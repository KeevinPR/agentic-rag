# Online Learning in Estimation of Distribution Algorithms for Dynamic Environments 

André R. Gonçalves*, Fernando J. Von Zuben ${ }^{\dagger}$<br>School of Electrical and Computer Engineering<br>University of Campinas (Unicamp)<br>Campinas, SP, Brazil<br>\{*andreric, ${ }^{\dagger}$ vonzuben\}@dca.fee.unicamp.br


#### Abstract

In this paper, we propose an estimation of distribution algorithm based on an inexpensive Gaussian mixture model with online learning, which will be employed in dynamic optimization. Here, the mixture model stores a vector of sufficient statistics of the best solutions, which is subsequently used to obtain the parameters of the Gaussian components. This approach is able to incorporate into the current mixture model potentially relevant information of the previous and current iterations. The online nature of the proposal is desirable in the context of dynamic optimization, where prompt reaction to new scenarios should be promoted. To analyze the performance of our proposal, a set of dynamic optimization problems in continuous domains was considered with distinct levels of complexity, and the obtained results were compared to the results produced by other existing algorithms in the dynamic optimization literature.


Index Terms-Online learning; mixture model; estimation of distribution algorithms; optimization in dynamic environments.

## I. INTRODUCTION

Evolutionary algorithms (EAs) have been applied successfully to a variety of optimization problems. Such problems are generally considered to be stationary, i.e., the objective function and other aspects of the formulation does not change over time. However, it is common to face scenarios in which some aspects of the optimization problem varies with time, such as the presence of a nonstationary objective function and/or a time-varying constraint set. Under these circumstances, the location of the optimal solution in the search space might change with time as well. As practical examples, we may cite a scheduling problem in which new jobs arrive over time, and vehicle routing problems where the cost to travel from one location to another is nonstationary. Thus, standard evolutionary algorithms, which are basically built to deal with stationary problems, tends to produce a poor performance in dynamic environments, due to the absence of reaction mechanisms when facing new conditions.

To be adapted to dynamic environments, EAs should be endowed with specific (implicit or explicit) operators devoted to the maintenance of diversity in the population, and mainly to avoid stagnation. Some of these additional operators, as pointed out by [1], should promote: (i) generation of diversity after a change; (ii) maintenance of diversity throughout the execution; (iii) employment of memory to store and recall useful information from the recent past; and (iv) execution of
a multipopulation search to track multiple local optima in the fitness landscape.

Trying to implement at least part of the aforementioned functionalities, several evolutionary approaches have been developed and extended to deal with dynamic environments. Among them, we can cite genetic algorithms [2], [3], particle swarm optimization [4], [5], artificial immune systems [6], [7] and estimation of distribution algorithms (EDAs) [8]-[10].

In this paper, we introduce an inexpensive EDA to the optimization of dynamic environments in continuous domains. This approach employs an online learning version of a mixture model, augmented by an automatic control of the number of components and by an operator to promote population diversity. The purpose is to make the search mechanism effective even in multimodal and time-varying fitness landscapes, by properly applying a concise model of the information from the previous iterations. This paper is organized as follows: Section II presents a brief introduction to estimation of distribution algorithms. In Section III, mixture models, the ExpectationMaximization (EM) algorithm and an online version of EM are described. The details of the proposed algorithm are presented in Section IV. A generator of dynamic environments in continuous search spaces, to be considered in the experiments, is depicted in Section V. Section VI discusses the obtained results on a number of dynamic optimization problems. Concluding remarks and further steps of the research are outlined in Section VII.

## II. Estimation of distribution Algorithm

Estimation of distribution algorithms (EDAs) are evolutionary methods that use estimation of distribution techniques, instead of genetic operators, to guide the search for better solutions. These algorithms were motivated by some shortcomings of genetic algorithms, more specifically the absence of a proper mechanism for detecting and preserving building blocks [11].

The key aspect in EDAs is how to estimate the true distribution of promising solutions. In fact, the estimation of the joint probability distribution associated with the variables that form the search space is the main distinctive component of EDAs. Once estimated the joint probability distribution, new candidate solutions are generated obeying the obtained distribution. Though essential to characterize an EDA, this

estimation is generally the most computationally intensive step of the algorithm. So, a compromise between accuracy of estimation and computational cost should be considered. Figure 1 shows the general framework of EDAs.

Step 1. Generate a random initial population $S_{0}(X)$. Set $t \leftarrow 0$. Step 2. Evaluate individuals from $S_{t}(X)$.
Step 3. Select a set of promising solutions, $S^{\prime} \subset S_{t}(X)$.
Step 4. Estimate the probability model $P(X)$ from $S^{\prime}$.
Step 5. Sample $S_{t+1}(X)$ from the probability model $P(X)$.
Step 6. Set $t \leftarrow t+1$ and return to step 2.
Fig. 1. A general framework for an EDA.
The already presented EDAs differ from each other basically by the way that the estimation of the probability model is made. They are classified according to the complexity of the probability model adopted: without dependencies, bivariate dependencies, multivariate dependencies and mixture models [12].
In this paper, the focus is on a class of EDAs for continuous optimization, based on an online version of a mixture model.

## III. Mixture MODELS

Considering that we have a dataset $x$, such that $x=$ $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$, we may proceed to divide it into $K$ subsets, also denoted components, so that each one has a mixture coefficient $\pi_{k}$, such that $0 \leq \pi_{k} \leq 1$ and $\sum_{k=1}^{K} \pi_{k}=1$. Subsequently, we define a probability density function (pdf) for each subset, denoted $f_{k}$. The parameter vectors $\Theta_{k}$ of each pdf, $k=\{1, \ldots, K\}$, will composed a single parameter vector $\Theta$ and are estimated from the available dataset. Therefore, the proposed probability model combines pdfs, each one associated with a component (subset of the dataset), thus producing a mixture model. When a Gaussian pdf is applied to fit each subset, the estimator is known as a Gaussian mixture model [13].
The task of obtaining the parameters of each probability density function, denoted parameter estimation, can be solved with several approaches. The maximum likelihood approach is the standard one for mixture models [13]. The likelihood of the dataset, given the parameters of the pdfs, is defined as the conditional probability $p(x \mid \Theta)$, which we generalize as $f(x ; \Theta)$, to denote any density function $f$ with parameters in $\Theta$. Considering that the data are independent and identically distributed (iid), we can define the joint data likelihood as $\prod_{j} f\left(x_{j} ; \Theta\right)$. Using the logarithmic transformation, we define the log-likelihood function as [14]:

$$
L(\Theta)=\ln \prod_{j} f\left(x_{j} ; \Theta\right)=\sum_{j} \ln f\left(x_{j} ; \Theta\right)
$$

The objective of the estimator is to define a vector of parameters, $\hat{\Theta}$, that maximizes the function in (1). The necessary condition for optimality is:

$$
\frac{\partial L(\Theta)}{\partial \Theta}=0
$$

This concept provides the basis for the derivation of a learning algorithm for the parameters of the mixture model, generally performed by the expectation-maximization (EM) algorithm [15]. EM is a powerful method to find maximum likelihood solutions to models with latent variables [13].

## A. Online version of EM algorithm

An online version of the EM algorithm is motivated by the necessity of processing data streams, in which the data are coming in a sequential and continuous way. So, the traditional EM algorithm becomes impractical due to the requirement that the whole data be available at each iteration of the algorithm.

The online variant of the EM used here is based on the work of Nowlan [16]. This algorithm summarizes all data item by a vector of sufficient statistics that can be incrementally updated. After that, this vector is used to compute the parameters of the mixture model. Sufficient statistics is a function $s(\cdot)$ of the samples that contains all the information relevant to estimate some parameters [14]. The EM steps of these online variant, described in [17], are shown in Fig. 2, where $Z$ is the unobserved variables, $X$ is the observed data, $\hat{s}^{(t)}$ is the vector of sufficient statistics at time $t, E_{\hat{P}_{t}}$ denotes the expectation with respect to the distribution over the range of unobserved variable $Z$, and $0<\gamma<1$ is a decay constant.

E-step: Select the next data item, $i$, for updating.
Set $\hat{s}_{i}^{(t)}=E_{\hat{P}_{t}}\left[s_{i}\left(z_{i}, x_{i}\right)\right]$, for $\hat{P}_{i}\left(z_{i}\right)=P\left(z_{i} \mid x_{i}, \Theta^{(t-1)}\right)$.
Set $\hat{s}^{(t)}=\gamma \hat{s}^{(t-1)}+\hat{s}_{i}^{(t)}$.
M-step: Set $\Theta^{(t)}$ to the $\Theta$ with maximum likelihood given $\hat{s}^{(t)}$.
Fig. 2. Online version of EM algorithm [16].
The algorithm uses statistics computed as an exponentially decaying average of recently-visited data points. In accordance with [17], online variants of the EM algorithm will not converge to the exact answer, but are able to converge to the vicinity of the correct answer more rapidly than standard EM, once chosen an appropriate value for $\gamma$. In the context of optimization, this drawback can be alleviated by the exploration capability of the search space provided by the evolutionary algorithm.

## IV. Mixture MODEL WITH ONLINE LEARNING FOR OPTIMIZATION IN DYNAMIC ENVIRONMENTS

In this section, we describe an estimation of distribution algorithm based on an Online Gaussian Mixture Model, labeled $\mathrm{EDA}_{\text {OGM }}$ and designed for continuous optimization in dynamic environments.

In order to achieve high performance in multimodal problems, it is necessary to use multiple Gaussian distributions, each one devoted to one promising region of the search space, thus producing a mixture model. However, when these models are implemented for dynamic problems, there is a concern about the computational cost of the training algorithm for the mixture model.

In accordance with [18], unless the dynamic change is of a high intensity, it is expected that better solutions are achieved by continuously adapting the current solutions to a changing environment, usually reusing the information gained in the near past. Thus, in Fig. 3 we propose an online learning algorithm capable of aggregating information from the past and current conditions of the environment, incorporating it into the mixture model.

The use of past information, besides the current one, seems to be relevant to mixture models, because the more pertinent data is available to estimate the fitness landscape, the more accurate the model tends to be.

The parameter $\gamma$ (see Fig. 2) defines for how long the information will be preserved to estimate the vector of sufficient statistics. Reducing $\gamma$, less information from the past will be stored in the mixture model. So, we can choose a $\gamma$ value coherent with the ratio of change in the environmental conditions. The contribution of each data item to the mixture model, over time, will be reduced by a geometric progression with ratio $\gamma$.

The $\mathrm{EDA}_{\text {OGMm }}$ algorithm is outlined in Fig. 3, where $N$ is the number of individuals in population, $\eta$ is the percentage of population used to estimate the promising regions in the search space and $K$ is the number of components in the mixture model.

Starting with a single component, $K=1$, the $\mathrm{EDA}_{\text {OGM }}$ tries to add more components, in a constructive fashion whilst it performs a continuous search for new promising regions, keeping in the population the best solutions found so far.

Two other important features of the $\mathrm{EDA}_{\text {OGM }}$ should be highlighted. First, in Step 5, after updating the vector of sufficient statistics, just a single M-step is applied, instead of the complete execution of the online EM algorithm. This is motivated by the work of [10], which has shown an overtime learning mixture model, where the convergence takes place along iterations and not at each iteration. With a single M step, the computational time of the algorithm is significantly reduced.

Secondly, a key feature is the continued analysis of the overlapping components in the mixture model. Overlapping components are Gaussian terms centred at the same promising region of the search space. So, one of the components can be eliminated without reducing the representation capability of the mixture model, thus saving computational resources. We consider that two components are overlapped if the Euclidian distance between their centers is lower than a threshold $\epsilon$. However, any other procedure to detect that two centers are located at the same basin of attraction of the optimization surface may be considered here.

The control of the number of components in the mixture model is made by a rule (Step 5), which is based on the Bayesian information criterion (BIC) score. BIC is usually applied in model selection tasks, i.e., given two models, it indicates which one maximizes the likelihood of the data, given the parameters and complexity of the model (number of parameters to be learned).

Step 1. Generate a random initial population and set $K \leftarrow 1$.
Step 2. Evaluate individuals in the current population.
Step 3. Select $\eta \cdot N$ of the best individuals from the population, using a fitness proportional selection method, like tournament selection.

Step 4. Set $K \leftarrow K+1$, update the vector of sufficient statistics and estimate the distribution of the selected data by applying a single M-step.

Step 5. Calculate the BIC for the new estimated model and verify if this is greater than or equal to the BIC of the best model so far. If so, set $K \leftarrow K-1$.

Step 6. Remove, if existent, components which have converged to the same promising region (overlapped components), keeping only one of them.

Step 7. Sample $\eta \cdot N$ new individuals from the estimated mixture model.

Step 8. Preserve $\frac{(1-\eta) \cdot N}{2}$ from the best solutions deterministically selected.

Step 9. Randomly sample $\frac{(1-\eta) \cdot N}{2}$ new individuals.

Step 10. Set the new population as the union of these three subpopulations: sampled by the model, preserved, and sampled randomly. Return to Step 2.

Fig. 3. Outline of the $\mathrm{EDA}_{\text {OGM }}$ algorithm.
$\mathrm{EDA}_{\text {OGM }}$ uses a user-controllable parameter $\eta$ that defines the proportion of individuals that will be considered on the estimation of distribution and, consequently, how many random immigrants will be introduced in the population (Step 9). If $\eta$ is a high value, $\mathrm{EDA}_{\text {OGM }}$ tends quickly to a local optimum solution, because there is an insufficient number of individuals to promote global exploration. However, for low values of $\eta$, $\mathrm{EDA}_{\text {OGM }}$ possibly faces a slow convergence, which is not suitable for applications in dynamic environments.

An elitist approach is employed (Step 8) to preserve good solutions found so far. Besides that, random immigrants are responsible for the exploratory behavior of the algorithm, aiming at finding new promising regions not yet considered in the mixture model.

## V. EXPERIMENTAL SETTINGS

In order to evaluate the performance of the $\mathrm{EDA}_{\text {OGMM }}$ and to compare with contender algorithms in dynamic optimization problems, we will define a test suite based on the well known Moving Peaks benchmark (MPB) generator introduced by [18], plus a rotation method, instead of random shifting the location of the peaks, as proposed by [19]. The rotation method is motivated by the MPB disadvantages of unequal challenge per change when the position of a peak bounces back from the search boundary [19].

## A. Specification of the dynamic environment generator

The moving peaks generator uses, besides the specific variables to control the changes, six basic parameters to define the dynamic environment: (1) search space range, (2) number of peaks, (3) period between consecutive changes, (4) peaks height range, (5) peaks width range, and (6) dimension range.

The function $f(x, \phi, t)$ to be maximized, with $\phi=$ $(\vec{H}, \vec{W}, \vec{X})$ and where $\vec{H}, \vec{W}$ and $\vec{X}$, and denote the peak height, width and position, respectively, can be expressed as follows:

$$
f(x, \phi, t)=\max _{m} \frac{\vec{H}_{m}(t)}{1+\vec{W}_{m}(t) \cdot \sqrt{\sum_{j=1}^{n} \frac{\left(x_{j}-\vec{X}_{j}^{m}(t)\right)^{2}}{n}}}
$$

where $m$ is the number of peaks and $n$ is the number of dimensions. Here, $\vec{H}_{m}$ and $\vec{W}_{m}$ are the height and the width of the $m$-th peak, respectively, and $\vec{X}_{j}^{m}$ is the position in the $j$-th dimension of the $m$-th peak. The parameters $\vec{W}$ and $\vec{X}$ changes according to seven distinct behaviors $\left(T_{1} \sim T_{7}\right)$ : small step, large step, random, chaotic, recurrent, recurrent with noise and random with dimensional changes (to simulate structural variations). The mathematical definition and parameter values of all change profiles can be seen in [19]. The changes in position $(\vec{X})$ and width $(\vec{W})$ of the peaks are responsible for the dynamic nature of the environment.

## B. Varying period between changes and number of peaks

To simulate several types of dynamic environments with several complexity levels, in relation to the frequency of change (measured in terms of the number of fitness evaluations - FEs) and the multimodality (number of peaks), which are controlled in MPB by the period between changes and number of peaks parameters, we build six different scenarios, which are specified in Tab. I.

For each one of the above scenarios, the seven change profiles $\left(T_{1}-T_{7}\right)$ are applied, thus yielding a complete suite of 42 test cases. Scenarios 1 and 2 are highly dynamic, i.e., the fitness landscape changes very quickly and if the algorithm has a very slow convergence rate, probably will get a poor performance. On the other hand, in scenarios 5 and 6 we have more time to reach the optimum, but the algorithms should be able to solve a global optimization problem.

TABLE I
SETTINGS OF DYNAMIC ENVIRONMENTS.

|  | Period between changes <br> (\# of FEs) | Multimodality <br> (\# of peaks) |
| :-- | :--: | :--: |
| Scenario 1 | 5000 | 10 |
| Scenario 2 | 5000 | 50 |
| Scenario 3 | 20000 | 10 |
| Scenario 4 | 20000 | 50 |
| Scenario 5 | 50000 | 10 |
| Scenario 6 | 50000 | 50 |

All test problems were defined in a 10-dimension search space and each decision variable was restricted to belong to the interval $[-5,5]$. The remaining parameters are set as follows: peaks height range is defined in $[10,100]$, peaks width range in $[1,10]$ and dimension range in $[5,15]$. The parameter settings are the same adopted in [20]. The benchmark used in our experiments was, originally, developed to low frequency dynamic environments, where the changes occur each 100.000 FEs. However, the scenarios defined in our experiments vary 20, 5 and 4 times faster, respectively. The objective is to analyze the performance of the algorithms in complex dynamic environments.

## C. Comparative analysis

The following approaches to deal with environments have been considered as contenders:

- Improved Univariate Marginal Distribution Algorithm (IUMDA) [9];
- Three components EDA (Tri-EDA ${ }_{G}$ ) [21];
- Hypermutation genetic algorithm (HGA) [22].

The first two methods are EDAs and the third is a genetic algorithm which generates diversity just after detecting a change, by means of increasing the mutation probability. For selection of the best individuals, HGA and EDA $_{\text {OGMM }}$ use tournament selection with five players, while IUMDA and Tri$\mathrm{EDA}_{G}$ use deterministic selection. HGA employs a Gaussian mutation operator, being necessary to define the standard deviation. The free parameters of each algorithm, used in the experiments, are presented in Tab. II.

For the IUMDA algorithm, $\mu$ is the percentage of the best individuals to be used in an interim population of the algorithm. Several $\mu$ values were tested and $\mu=0.2$ (20 percent of the best individuals) yielded the best results, given the population size considered. The mutation parameter ( $P_{\text {mut. }}$ ) was chosen using a similar procedure.

Concerning the Tri-EDA ${ }_{G}$ algorithm, $\rho$ is the percentage of best individuals selected for updating the parameters of the local exploration multivariate Gaussian distribution (primary model), and $\lambda$ is the percentage of population of the next generation, to be generated by the primary model. Their values are the same as used by the authors in their original paper [21].

For HGA, besides the crossover probability ( $P_{\text {cross. }}$ ), there are two mutation probabilities to be specified: hypermutation

TABLE II
Parameter SETTINGS FOR THE ALGORITHMS.

| Algorithm | Free parameter | Value |
| :--: | :--: | :--: |
| IUMDA | $\mu$ | 0.2 |
|  | $P_{\text {mut. }}$ | 0.01 |
|  | $\sigma_{\text {mut. }}$ | 0.05 |
| Tri-EDA $_{G}$ | $\rho$ | 0.3 |
|  | $\lambda$ | 0.8 |
| HGA | $P_{\text {cross. }}$ | 0.8 |
|  | $P_{\text {mut. }}$ | 0.01 |
|  | $P_{\text {Hyp.mut. }}$ | 0.8 |
|  | $\sigma_{\text {mut. }}$ | 0.05 |
| EDA $_{\text {OGM }}$ | $\eta$ | 0.6 |
|  | $\gamma$ | 0.5 |
|  | $\epsilon$ | 0.01 |

probability ( $P_{\text {Hyp.mut. }}$ ), used if the environment has been changed, and $P_{\text {mut. }}$, which are used elsewhere.

One feature shared by all algorithms is the application of a mechanism to assure that the best individual of the current population is always inserted into the next population.

In all the scenarios studied, the population size is 100 and the execution time (measured by the number of changes) is 60 changes.

All the algorithms and the MPB generator were implemented using the Matlab ${ }^{\circledR}$ numerical computing environment.

The MPB generator is available for download at http://www.cs.le.ac.uk/people/syang/ECiDUE/DBG.tar.gz, in C++ and Matlab ${ }^{\circledR}$ languages, being the last one considered here. All the algorithms being considered were also implemented using Matlab ${ }^{\circledR}$.

## VI. Obtained ReSults

Tables III, IV, V, VI, VII and VIII present the average offline error and standard error, for 20 independent runs, in each one of the six defined scenarios. The offline error metric is the average of the absolute error between the best solution found so far and the global optimum (known) at each time step $t$. The best results are those with highlighted background.

In the case of high frequency changing environments, $\mathrm{EDA}_{\text {OGM }}$ clearly outperforms the contender algorithms. A great advantage of the proposed method is the exploration of several peaks at the same time, thus increasing the probability of finding the global optimum, or at least better local optima. Besides that, we propagate the information from the previous to the current environment, giving to the algorithm the ability to properly adapt to a changing fitness landscape.

Estimation of distribution algorithms have a fast convergence, mainly after detecting a promising region. We may associate the behavior with the one produced by the wellknown Newton's method, which at each iteration approximates the optimization surface by a quadratic function and take a step towards the minimum (or maximum) of that quadratic function. Even though the Gaussian exploration does not implement an explicit gradient descent, it take a step towards

TABLE III
AVERAGE OFFLINE ERROR AND STANDARD ERROR FOR SCENARIO 1.

|  | IUMDA | Tri-EDA $_{G}$ | HGA | EDA $_{\text {OGM }}$ |
| :--: | :--: | :--: | :--: | :--: |
| $T_{1}$ | $77.43(\pm 0.75)$ | $47.64(\pm 1.26)$ | $79.73(\pm 0.88)$ | $6.89(\pm 0.94)$ |
| $T_{2}$ | $76.78(\pm 1.13)$ | $48.75(\pm 1.23)$ | $82.02(\pm 1.01)$ | $16.66(\pm 2.43)$ |
| $T_{3}$ | $62.09(\pm 1.30)$ | $35.91(\pm 1.54)$ | $66.23(\pm 1.36)$ | $18.24(\pm 1.89)$ |
| $T_{4}$ | $76.21(\pm 0.23)$ | $53.06(\pm 0.48)$ | $78.89(\pm 0.08)$ | $9.93(\pm 1.33)$ |
| $T_{5}$ | $77.08(\pm 0.50)$ | $74.51(\pm 0.32)$ | $77.90(\pm 0.91)$ | $37.53(\pm 1.05)$ |
| $T_{6}$ | $73.11(\pm 0.83)$ | $68.34(\pm 0.74)$ | $76.18(\pm 0.58)$ | $38.82(\pm 1.36)$ |
| $T_{7}$ | $60.61(\pm 1.42)$ | $35.92(\pm 2.48)$ | $64.38(\pm 1.74)$ | $24.89(\pm 2.11)$ |

TABLE IV
AVERAGE OFFLINE ERROR AND STANDARD ERROR FOR SCENARIO 2.

|  | IUMDA | Tri-EDA $_{G}$ | HGA | EDA $_{\text {OGM }}$ |
| :--: | :--: | :--: | :--: | :--: |
| $T_{1}$ | $80.18(\pm 1.37)$ | $48.34(\pm 0.49)$ | $83.77(\pm 1.32)$ | $17.60(\pm 1.57)$ |
| $T_{2}$ | $73.00(\pm 0.94)$ | $37.79(\pm 1.34)$ | $77.87(\pm 0.92)$ | $14.43(\pm 1.48)$ |
| $T_{3}$ | $62.98(\pm 1.01)$ | $35.86(\pm 1.27)$ | $68.95(\pm 0.89)$ | $20.36(\pm 2.12)$ |
| $T_{4}$ | $76.36(\pm 0.19)$ | $47.44(\pm 0.57)$ | $78.37(\pm 0 / 08)$ | $18.06(\pm 1.70)$ |
| $T_{5}$ | $78.87(\pm 0.62)$ | $73.47(\pm 0.49)$ | $80.25(\pm 0.83)$ | $44.50(\pm 1.14)$ |
| $T_{6}$ | $74.93(\pm 0.96)$ | $64.61(\pm 0.46)$ | $79.02(\pm 0.92)$ | $49.74(\pm 1.63)$ |
| $T_{7}$ | $65.46(\pm 1.02)$ | $36.80(\pm 1.57)$ | $69.47(\pm 1.12)$ | $32.77(\pm 1.66)$ |

the best solutions found so far. Mixture models extrapolate this employing several Gaussian explorations simultaneously.

We can notice also that, in recurrent changes ( $T_{5}$ and $T_{6}$ ), $\mathrm{EDA}_{\text {OGM }}$ is better than the contenders, but with a smaller margin. Given that the period of the recurrent change, $P$, is 12 (see parameter settings in [20]), i.e., at each 12 changes the optimum goes back to the same position, the information about the first position of the optimum was lost during the execution. In these situations, the use of explicit memories can be an interesting approach. But, for applications where the period is unknown, which is common in real problems, the identification of which best solution, stored in the memory, should be re-inserted into the population is a very hard task. So, in environments where the recurrent period is unknown, maybe one effective way to deal with it is to assume that the changes are random and to perform a global optimization anyway.

TABLE V
AVERAGE OFFLINE ERROR AND STANDARD ERROR FOR SCENARIO 3.

|  | IUMDA | Tri-EDA $_{G}$ | HGA | EDA $_{\text {OGM }}$ |
| :--: | :--: | :--: | :--: | :--: |
| $T_{1}$ | $40.30(\pm 2.84)$ | $11.66(\pm 0.64)$ | $52.94(\pm 5.13)$ | $2.02(\pm 0.19)$ |
| $T_{2}$ | $37.40(\pm 2.27)$ | $14.75(\pm 0.64)$ | $51.19(\pm 3.07)$ | $7.91(\pm 0.92)$ |
| $T_{3}$ | $36.47(\pm 2.26)$ | $14.75(\pm 1.81)$ | $45.22(\pm 1.70)$ | $11.40(\pm 1.82)$ |
| $T_{4}$ | $41.94(\pm 1.12)$ | $13.57(\pm 0.17)$ | $60.01(\pm 0.51)$ | $5.67(\pm 0.22)$ |
| $T_{5}$ | $47.64(\pm 0.55)$ | $47.13(\pm 0.93)$ | $43.38(\pm 0.01)$ | $14.92(\pm 0.81)$ |
| $T_{6}$ | $47.77(\pm 0.61)$ | $38.98(\pm 0.81)$ | $42.66(\pm 0.36)$ | $25.09(\pm 0.98)$ |
| $T_{7}$ | $37.54(\pm 2.24)$ | $17.64(\pm 1.67)$ | $46.71(\pm 2.73)$ | $11.87(\pm 1.46)$ |

In medium frequency changing environments, $\mathrm{EDA}_{\text {OGM }}$ has shown better results than the contenders. Like $\mathrm{EDA}_{\text {OGM }}$, Tri-EDA $_{G}$, which has produced the second best performance, uses a Gaussian exploration too, but only one model (main model) is always active. An optional model is triggered when a new promising region, better than the one indicated by the main model, is found. So, Tri-EDA $_{G}$ jumps from region to

TABLE VI
AVERAGE OFFLINE ERROR AND STANDARD ERROR FOR SCENARIO 4.

|  | IUMDA | Tri-EDA $_{G}$ | HGA | EDA $_{\text {OGM }}$ |
| :-- | :--: | :--: | :--: | :--: |
| $T_{1}$ | $37.57(\pm 1.39)$ | $12.55(\pm 0.70)$ | $51.04(\pm 4.08)$ | $3.57(\pm 0.36)$ |
| $T_{2}$ | $34.68(\pm 1.35)$ | $10.05(\pm 0.49)$ | $47.74(\pm 2.32)$ | $5.54(\pm 0.62)$ |
| $T_{3}$ | $34.85(\pm 1.23)$ | $17.07(\pm 1.45)$ | $43.10(\pm 1.19)$ | $13.95(\pm 1.28)$ |
| $T_{4}$ | $33.23(\pm 0.93)$ | $11.12(\pm 0.23)$ | $53.10(\pm 0.60)$ | $4.84(\pm 0.14)$ |
| $T_{5}$ | $50.21(\pm 0.64)$ | $40.36(\pm 1.46)$ | $45.63(\pm 0.27)$ | $13.40(\pm 0.77)$ |
| $T_{6}$ | $46.55(\pm 1.57)$ | $40.53(\pm 1.11)$ | $44.54(\pm 1.36)$ | $35.10(\pm 1.32)$ |
| $T_{7}$ | $35.73(\pm 1.35)$ | $20.00(\pm 1.45)$ | $43.80(\pm 1.26)$ | $15.10(\pm 1.26)$ |

region, looking for the best one. Based on results obtained by $\mathrm{EDA}_{\text {OGM }}, \mathrm{Tri}-\mathrm{EDA}_{G}$ would possibly get better performance if it could manipulate many active models at the same time.

TABLE VII
AVERAGE OFFLINE ERROR AND STANDARD ERROR FOR SCENARIO 5.

|  | IUMDA | Tri-EDA $_{G}$ | HGA | EDA $_{\text {OGM }}$ |
| :-- | :--: | :--: | :--: | :--: |
| $T_{1}$ | $10.47(\pm 0.85)$ | $6.48(\pm 0.57)$ | $12.51(\pm 1.15)$ | $1.93(\pm 0.24)$ |
| $T_{2}$ | $14.29(\pm 0.97)$ | $11.64(\pm 0.86)$ | $16.86(\pm 1.22)$ | $8.89(\pm 0.85)$ |
| $T_{3}$ | $18.16(\pm 2.09)$ | $15.65(\pm 2.00)$ | $19.68(\pm 1.94)$ | $14.00(\pm 1.95)$ |
| $T_{4}$ | $8.13(\pm 0.11)$ | $7.01(\pm 0.16)$ | $8.86(\pm 0.08)$ | $5.07(\pm 0.07)$ |
| $T_{5}$ | $43.32(\pm 0.01)$ | $40.36(\pm 1.10)$ | $43.25(\pm 0.01)$ | $10.00(\pm 0.41)$ |
| $T_{6}$ | $41.91(\pm 0.65)$ | $36.25(\pm 0.93)$ | $41.44(\pm 0.56)$ | $21.85(\pm 0.90)$ |
| $T_{7}$ | $16.63(\pm 2.37)$ | $15.49(\pm 2.31)$ | $21.76(\pm 2.79)$ | $12.77(\pm 2.28)$ |

TABLE VIII
AVERAGE OFFLINE ERROR AND STANDARD ERROR FOR SCENARIO 6.

|  | IUMDA | Tri-EDA $_{G}$ | HGA | EDA $_{\text {OGM }}$ |
| :-- | :--: | :--: | :--: | :--: |
| $T_{1}$ | $14.17(\pm 2.30)$ | $8.62(\pm 1.16)$ | $13.45(\pm 2.04)$ | $2.61(\pm 0.43)$ |
| $T_{2}$ | $12.96(\pm 1.53)$ | $8.93(\pm 1.00)$ | $13.50(\pm 1.44)$ | $5.93(\pm 0.60)$ |
| $T_{3}$ | $16.19(\pm 1.18)$ | $14.10(\pm 1.81)$ | $16.57(\pm 1.44)$ | $12.33(\pm 1.65)$ |
| $T_{4}$ | $7.34(\pm 0.30)$ | $6.11(\pm 0.12)$ | $6.55(\pm 0.12)$ | $3.37(\pm 0.1)$ |
| $T_{5}$ | $45.03(\pm 0.01)$ | $32.54(\pm 0.86)$ | $45.04(\pm 0.05)$ | $9.39(\pm 0.51)$ |
| $T_{6}$ | $39.72(\pm 1.63)$ | $35.79(\pm 0.83)$ | $39.41(\pm 1.81)$ | $32.85(\pm 0.87)$ |
| $T_{7}$ | $17.42(\pm 0.81)$ | $15.58(\pm 0.60)$ | $18.94(\pm 0.84)$ | $12.97(\pm 0.53)$ |

For scenarios 5 and 6 , the algorithm has more time to find the global optimum. If the algorithm has a fast convergence, but get stuck in a local optimum, probably it will reach poor performance in highly multimodal environments. So, the algorithm should execute a global optimization in a restricted time. Like in the other four scenarios, $\mathrm{EDA}_{\text {OGM }}$ has achieved the best results, followed by Tri-EDA ${ }_{G}$.

In global optimization problems, the mixture model, initially, can cover several peaks and, by means of the selection operator and sampling, the mixture model finds better regions, and focuses on those promising regions. Subsequently, it applies a Gaussian exploration at each region (local optimization), to reach the local optimum.

Figures 4, 5, 6 and 7 present the median convergence behavior, over the 20 independent runs executed, of IUMDA, Tri-EDA $_{G}$, HGA and EDA $_{\text {OGM }}$, respectively, when applied in scenario 2 with random change with dimensional changes $\left(T_{7}\right)$. The performance is measure by means of the ratio between the best solution found and the global optimum. So, the ideal performance would be to stay as close as possible to the value 1 .
![img-0.jpeg](img-0.jpeg)

Fig. 4. Relative performance of the IUMDA algorithm.

In the first environment $(t=1)$, IUMDA finds a good local optimum (the performance achieved a value close to 0.9 ), but it is not able to adapt to the subsequent scenarios, reaching poor solutions in these fitness landscapes. These results showed the impact of the loss in population diversity. In $t=1$, where the algorithm has obtained better results, the population was randomly generated, and for $t>1$, the algorithm cannot insert sufficient diversity in the population. A possible solution is to employ the random immigrants approach at every generation or when an environment change is detected.
![img-1.jpeg](img-1.jpeg)

Fig. 5. Relative performance of the Tri-EDA $_{G}$ algorithm.
Figure 5 shows, clearly, an oscillatory performance of the Tri-EDA $_{G}$ algorithm. This is due to the variation in the number of dimensions of the search space. Decreasing the number of dimensions, the search space is significantly reduced and, given the same population size, the algorithm can achieve a better exploration of the search space, getting better results.

The hypermutation genetic algorithm has a slow convergence rate, which in dynamic environments is extremely undesirable. When the new position of the global optimum is very close to the old position, this approach seems interesting.

The loss of population diversity can be a bottleneck in

![img-2.jpeg](img-2.jpeg)

Fig. 6. Relative performance of the Hypermutation genetic algorithm.
this algorithm too. Despite the hypermutation used to produce certain diversity in the population, the exploration area is limited by the standard deviation parameter $\left(\sigma_{\text {mal. }}\right)$ of the Gaussian mutation operator. An alternative to bypass this problem is to define a new standard deviation parameter or mutate the individual to any location in the search space. In this way, we establish a balance between local exploration, around the best solution found in the previous generation, and exploration of the whole search space.
![img-3.jpeg](img-3.jpeg)

Fig. 7. Relative performance of the $\mathrm{EDA}_{\text {OGM }}$ algorithm.
Oscillatory performance is not clearly evident in $\mathrm{EDA}_{\text {OGM }}$ convergence behavior, different from what happens with the Tri-EDA ${ }_{G}$, reaching consistently better results in high dimensional environments than the other three algorithms.

## VII. CONCLUDING REMARKS

Dynamic environments require that the optimization algorithm adapts quickly to the new environment for tracking the global optimum. So, a continuous modeling of the fitness landscape seems an interesting alternative to keep the algorithm up-to-date.

In this paper, we have introduced an online estimation of the promising regions of the search space, by means of a Gaussian mixture model, and use this estimated model to guide an evolutionary algorithm. The estimation is made by an online version of the Expectation-Maximization algorithm, which maintains a continuously updated mixture model. Here, the dynamism of the process is captured by a vector of sufficient statistics of the best solutions, which are used by a mixture model.

The results has shown that the proposed $\mathrm{EDA}_{\text {OGM }}$ outperforms all the contenders, particularly in high-frequency changing environments (Scenarios 1 and 2).
$\mathrm{EDA}_{\text {OGM }}$ has a fast convergence because it can explore several peaks simultaneously. Each peak is represented by one component in the mixture model. However, comparing the results at high-frequency changing environments (Scenarios 1 and 2) with the ones obtained with the low frequency changing environments (Scenarios 5 and 6), we can detect a less prominent performance in low frequency scenarios, indicating that, once converged, the $\mathrm{EDA}_{\text {OGM }}$ reduces its exploration power. So, a continued control to avoid premature convergence is desirable.

Next steps of the research are: to incorporate a continued convergence control mechanism, to compare $\mathrm{EDA}_{\text {OGM }}$ with other algorithms designed to deal with dynamic environments, to increment the experimental tests aiming at investigating scalability and other aspects related to the relative performance of the proposed algorithm, and to perform a parameter sensitivity analisys.

## ACKNOWLEDGMENT

This work was supported by grants from the So Paulo Research Foundation - FAPESP, process number 2009/067570 , and by the Brazilian National Research Council - CNPq.

## REFERENCES

[1] Y. Jin and J. Branke, "Evolutionary optimization in uncertain environments-a survey," Evolutionary Computation, IEEE Transactions on, vol. 9, no. 3, pp. 303-317, 2005.
[2] R. Tinós and S. Yang, "A self-organizing random immigrants genetic algorithm for dynamic optimization problems," Genetic Programming and Evolvable Machines, vol. 8, no. 3, pp. 255-286, 2007.
[3] S. Yang and X. Yao, "Population-based incremental learning with associative memory for dynamic environments," Evolutionary Computation, IEEE Transactions on, vol. 12, no. 5, pp. 542 -561, 2008.
[4] R. Mendes, J. Kennedy, and J. Neves, "The fully informed particle swarm: simpler, maybe better," Evolutionary Computation, IEEE Transactions on, vol. 8, no. 3, pp. 204-210, June 2004.
[5] X. Li, J. Branke, and T. Blackwell, "Particle swarm with speciation and adaptation in dynamic environments," in Proceedings of the 8th Genetic and Evolutionary Computation Conference, ser. GECCO '06. New York, USA: ACM, 2006, pp. 51-58.
[6] F. de França, F. von Zuben, and L. de Castro, "An artificial immune network for multimodal function optimization on dynamic environments," in Proceedings of the 2005 conference on Genetic and evolutionary computation. ACM, 2005, p. 296.
[7] F. de França and F. Von Zuben, "A dynamic artificial immune algorithm applied to challenging benchmarking problems," in Proceedings of the Eleventh conference on Congress on Evolutionary Computation, ser. CEC'09. Piscataway, NJ, USA: IEEE Press, 2009, pp. 423-430.
[8] S. Yang and X. Yao, "Experimental study on population-based incremental learning algorithms for dynamic optimization problems," Soft Comp., vol. 9, no. 0, pp. 815-834, 2005.

[9] X. Liu, Y. Wu, and J. Ye, "An Improved Estimation of Distribution Algorithm in Dynamic Environments," in Fourth International Conference on Natural Computation. IEEE Computer Society, 2008, pp. 269-272.
[10] A. Gonçalves and F. Von Zuben, "Hybrid evolutionary algorithm guided by a fast adaptive gaussian mixture model applied to dynamic optimization problems," in III Workshop on Computational Intelligence - Joint Conference, 2010, pp. 553-558.
[11] P. Larrañaga and J. Lozano, Estimation of distribution algorithms: A new tool for evolutionary computation. Springer Netherlands, 2002.
[12] P. Larrañaga, "A Review of Estimation of Distribution Algorithms," in Estimation of Distribution Algorithms: A new tool for Evolutionary Computation, P. Larrañaga, J.A. Lozano, Ed. Kluwer Academic Publishers, 2001.
[13] C. Bishop, Pattern Recognition and Machine Learning (Information Science and Statistics), 1st ed. Springer, October 2007.
[14] R. Duda, P. Hart, and D. Stork, Pattern classification, 2nd ed. Wiley, November 2001.
[15] A. Dempster, N. Laird, and D. Rubin, "Maximum Likelihood from Incomplete Data via the EM Algorithm," Journal of the Royal Statistical Society, Series B (Methodological), vol. 39, no. 1, pp. 1-38, 1977.
[16] S. Nowlan, "Soft competitive adaptation: neural network learning algorithms based on fitting statistical mixtures," Ph.D. dissertation, Carnegie Mellon University, Pittsburgh, PA, USA, 1991.
[17] R. Neal and G. Hinton, "A view of the EM algorithm that justifies incremental, sparse and other variants," in Learning in Graphical Models. Kluwer Academic Publishers, 1998, pp. 355-368.
[18] J. Branke, "Memory enhanced evolutionary algorithms for changing optimization problems," in Congress on Evolutionary Computation CEC99, vol. 3, 1999, pp. 1875-1882.
[19] C. Li and S. Yang, "A generalized approach to construct benchmark problems for dynamic optimization," in Proc. of the 7th Int. Conf. on Simulated Evolution and Learning, 2008.
[20] C. Li, S. Yang, T. Nguyen, E. Yu, X. Yao, Y. Jin, H. Beyer, and P. Suganthan, "Benchmark Generator for CEC'2009 Competition on Dynamic Optimization," University of Leicester, Tech. Rep., 2008.
[21] B. Yuan, M. Orlowska, and S. Sadiq, "Extending a class of continuous estimation of distribution algorithms to dynamic problems," Optimization Letters, vol. 2, no. 3, pp. 433-443, 2008.
[22] H. Cobb, "An investigation into the use of hypermutation as an adaptive operator in genetic algorithms having continuous, time-dependent nonstationary environments," Naval Research Laboratory, Tech. Rep., 1990.