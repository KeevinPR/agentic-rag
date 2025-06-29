# Dynamic Optimization of Chemical Engineering Problems Using Affinity Propagation Based Estimation of Distribution Algorithm 

Na Luo, Wei Feng, Xiaoqiang Wang, Feng Qian*<br>Key Laboratory of Advanced Control and Optimization for Chemical Processes, Ministry of Education<br>East China University of Science and Technology<br>Shanghai,China<br>fqian@ecust.edu.cn


#### Abstract

Dynamic optimization has attracted much attention for its wide applications in engineering problems. However, it is still a challenge for high nonlinear, multi-dimensional and multimodal problems. Estimation of Distribution Algorithm was proposed in which probabilistic models extracted relevant features of the complex search space and then generated new individuals during optimization. In order to decrease the dependences among control variables in dynamic optimization, affinity propagation was applied to cluster the individuals in evolutionary iterations. In each cluster, the probabilistic density function of Gaussian mixture model refined the promising spaces with high quality solutions and avoided the random combination of different control variables. To evaluate the performance of the new approach, three dynamic optimization problems of chemical process are used as cases comparing with three state-of-the-art global optimization methods. The results showed that the new approach could achieve the best solution in most cases with less computational effort and higher efficiency.


Keywords-Dynamic optimization; Estimation of distribution algorithm; Chemical process; affinity propagation; Gaussian mixture model.

## I. INTRODUCTION

Dynamic Optimization Problems (DOPs) are widely spread in chemical engineering applications. In general, it is typical to find a predefined performance index to subject to certain specification over a time interval. The DOP can be described as follows:

$$
\begin{gathered}
\min J(u)=\Phi\left[x\left(t_{f}\right)\right]+\int_{t=0}^{t=t_{f}} \Psi[x(t), u(t), t] d t \\
\text { s.t. } \quad \varphi(x(t), u(t), t)=0 \\
\dot{x}(t)=f(x(t), u(t), t)
\end{gathered}
$$

where $x$ and $u$ are called state variables and control variables respectively. $J(u)$ is defined as the objective function. $\Phi$ and $\Psi$ are the general function relationship and the function vector separately. $t_{f}$ is the end time. The control variables $u(t)$ and the state variables $x(t)$ as well as their derivatives with respect to time $\dot{x}(t)$ appear continuous in this problem. This kind of problem is known as Differential-Algebraic Equation (DAE) problem, which consists of differential equations that describe the dynamic behavior of the system and algebraic equations that ensure some relations. A variety of approaches have been studied in order to obtain the optimal solution of the DAE problems.

These approaches can be grouped into two general classes: the indirect and direct approach. The indirect or variational approaches obtain the optimality using the first order necessary conditions in Pontryagin's Maximum Principle. A review of the indirect approaches can be found in [1]. Different from indirect methods, direct approaches convert the original problem into a finite-dimensional one, usually a nonlinear programming problem (NLP). Usually, these NLPs can be solved by variations of Successive Quadratic Programming (SQP). Biegler[2] proposed an efficient reduced space SQP approach for DOPs in which the number of state variables is much larger than the number of control variables. Dynamic programming was also proved feasible[3] in DOPs. A systematic backward search method was used to find the optimal path after time and control variables were discretized to a predefined number of values. However, when the number of discritization became large, computation increases rapidly. Iterative dynamic programming[4] was proposed to avoid this difficulty. Using coarse grid points and region-reduction strategy, computation efficiency promoted and numerical accuracy increased. But when state variables were also discretized, it was still troublesome.

Comparing with dynamic programming, it was unnecessary to discretize states variables when evolutionary algorithms were applied in DOPs. Furthermore, control profile at all time stages could be optimized simultaneously. Genetic Algorithm (GA) was the first to solve DOPs. Pham[5] applied GA in DOPs by using several novel reproductive operators including shift, smoothing, extrapolation and swapping. Modified differential evolution algorithm was also tried by Lee[6] through employing a local search to enhance the computational efficiency and modifying heuristic constraints to systematically reduce the size of the search space. Angira[7] applied trigonometric differential evolution algorithm for solving DOPs to enhance convergence speed. Simulated annealing algorithm was also applied[8] in determining operation policies of a binary distillation[9]. As a low computational algorithm, ant colony algorithm had a potential for DOPs[10]. Zhang[11] developed iterative ant-colony algorithm to gradually approximate the optimal control profile. Likewise, population-based probability distribution estimation was applied in tackling constrained multistage complex process DOPs with special solution migration and penalty assignment techniques integrated[12]. Recently, hybrid algorithms such as improved particle swarm optimization with successive quadratic programming[13] were proposed which balanced the speed of convergence and the ability of escaping local optimal.

In general, evolutionary algorithms have been widely used in DOPs.

Certainly, improvement on evolutionary algorithms should be taken when DOPs need to be solved efficiently and accurately. Pham[14] used statistical analysis to generate progressive step reduction and improved the efficiency of the algorithm. Region reduction strategy was chosen by Asgari[15] to obtain more accurate results. Liu[16] applied orthogonal collocation to decrease the combination of different control variables and encoded chromosome for improvement of search efficiency with soft constraint strategy. In short, the search space should be oriented to promising area without considering mutual dependence of control variables. Comparing with other evolutionary algorithms, Estimation of Distribution Algorithm (EDA)[17] is based on probability distribution estimation. In EDAs, relevant features of the search space are extracted using a probabilistic model, which is later employed to generate new points. In this way, the search is easily oriented to promising areas. As the key factor, many probability models are proposed for real-world problems. For the best performance, time-dependent dynamic problems require its own probability model construction method to direct the optimization course. In this paper, various strategies are investigated to limit the research area and an improved EDA is used to solve dynamic problems efficiently.

This paper is organized as follows. Section 2 reviews different kinds of EDAs proposed for solving general optimization problems. In section 3, an improved approach named AffEDA is illustrated for dynamic problems. To increase the independence of individual, affinity propagation is applied to cluster individuals. In each cluster, Gaussian mixture model is applied to construct the probabilistic model and generate new individuals, which avoids the random combination of different control variables. Section 4 presents three dynamic optimization cases for experiments and obtains results. The performance and computation efficiency are also analyzed comparing with other evolutionary algorithms. In the end, conclusions are drawn.

## II. A GENERAL REVIEW OF AFFINITY PROPAGATION BASED ESTIMATION OF DISTRIBUTION ALGORITHM

EDA was originally proposed as a new evolutionary algorithm.. It evolves towards the promising area of the search space using the probabilistic and statistical theory. There are four main steps: selecting individuals, building probabilistic model, sampling from the model and replacing some individuals. Different probabilistic models are applied in EDAs. According to the probabilistic models, EDAs are categorized into three classes. The first class of EDAs uses a product of independent univariate probabilities, such as the probabilistic incremental learning (PBIL)[18], the compact genetic algorithm (CGA)[19] and the univariate marginal distribution algorithm (UMDA)[20], in which variables are assumed independent. In the second-class EDAs, the variables are disposed as bivariate dependences and the probabilistic model is developed based on Bayesian deduction. This class includes the mutual information maximization for input clustering (MIMIC)[21], the combining optimizers with mutual information trees algorithm (COMIT)[22] and the bivariate marginal distribution algorithm (BMDA)[23]. The third class which includes the extended compact genetic algorithm
(ECGA)[24], the Bayesian optimization algorithm (BOA)[25] and the factorized distribution algorithm (FDA)[26] uses multivariate dependent Bayesian network to build the probability model. In continuous domain, Gaussian model is widely used for its simplicity. Based on these combinatory optimization algorithms, UMDAC[27], PBILC[28], MIMICC[27], EGNAee[27] are the extensions of UMDA, PBIC, MIMIC, EGNA to continuous domain based on Gaussian network.

Estimation of Distribution Algorithm based on Affinity Propagation (AffEDA) was first proposed by Santana[29]. This method learns marginal product models using affinity propagation and takes the matrix of mutual information between the variables as the similarity measure. Through grouping the variables in non-overlapping sets, strong interacting variables are contained in the same set. A general outline of AffEDA is as follows:

1) Initialize M individuals randomly and evaluate the fitnesses;
2) Select $\mathrm{N}(\mathrm{N}<\mathrm{M})$ individuals according to a selection method and save some as the elite individuals;
3) Compute the mutual information between every pair of variables;
4) Apply Affinity clustering algorithm to obtain a marginal product model $p(x, t)$;
5) Sample M individuals according to the distribution $p(x, t)$;
6) Partially replace some new individuals by the elite individuals.
7) Stop if some stopping criterion is reached, else go to step 2 .

AffEDA solves a given optimization problem by evolving a population of individuals towards promising zones of the search space. Such an evolution is mainly based on iteration between two steps: Select fit individuals from the current population, and combine the selected individuals in order to create an offspring population and partially replace the current one. For different problems, the interactions of variables are made clear using affinity clustering. By testing some benchmark functions, the AffEDA performs well. But for dynamic optimization problems, it is not so easy to find the solutions as usual.

## III. AFFEDA FOR DYNAMIC OPTIMIZATION

For dynamic optimization, AffEDA needs to be modified to handle time-dependent dynamic problems. The main frame of AffEDA for dynamic problems includes: (i) discretizing time interval; (ii) constructing the probabilistic model and searching optimal control profile of the discrete system; (iii) returning to step (ii) for next iteration until reaching convergence. In all of these three steps, the important modification is the new construction of the probabilistic model.

### 3.1 Discretization of time horizon

To solve the dynamic optimization problems directly, the time interval is uniformly divided into $n$ stages. So the $i$ th time stage is $\left[t_{i}, t_{i+1}\right]$ where $t_{1}=0$ and $t_{n+1}=t_{f}$. Control variables are discredited into a profile according to the time interval. Assumed that there are $m$ control variables, the optimization objective is to identify the optimal values from $m \times n$ discretized system inputs. It is obvious that if all possible inputs are calculated, the computation complexity is

large. So the relationship of decision variables should be considered to decrease the computation.

In order to improve the performance, it is feasible to reduce the search region during the iteration of the optimization. Different from general formula to decrease the limit of variables, AffEDA determines the range of the control profile using the probabilistic model. AFFEDA generates a population of complete solutions before any solution quality evaluation and the probabilistic model construction. And the inputs in all time stages are actually simultaneously optimized. In the next iteration, the individuals will be used for constructing the probabilistic model. Using AffEDA, a route of a single variable $u$ with $n$ time intervals is illustrated in Fig.1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Discretization of time interval
In Fig.1, the profile has $n$ elements, each of which represents a feasible control strategy at a time stage. Around the heavy line is the variance of the control profile. That represents the range of the control profile in which the control profile has some probability to choose the value. Different from the other algorithms, the control profile is not just a determined line but a line with variance. In the next section, cluster method is used to make the algorithm concentrate on the mean value of the variables and decrease the computation complexity.

### 3.2 Probabilistic model construction

In order to construct the probabilistic model of the individuals, two questions should be considered. One is the selection method of the samples. The other question is how to construct the probabilistic model. In this paper, learning the mutual information of the probabilistic model is by a clustering method known as affinity propagation which referred the method proposed by Santana [29]. As the probabilistic model, Gaussian Mixture model is chosen.

## - 3.2.1 Selection scheme

The initialization of the population is usually random. From the generated population, selection is performed to choose promising individuals. There are many selection methods, such as truncation, tournament selection or roulette wheel selection. During the selection course, the determination of the selection size is important. With small selection size, promising points may be excluded. On the contrary, the large selection size may increase the learning overhead.

Generally, the truncation selection is used. In truncation selection, individuals are sorted according to their fitness. Only a certain percentage of individuals are selected with which probability model is constructed. The parameter for truncation selection is the truncation ratio which indicates the proportion of the population to be selected. The ratio takes values ranging
from $0.1-0.5$. Individuals below the truncation threshold do not produce offspring.

- 3.2.2 Clustering with affinity propagation

Affinity propagation is a new developed clustering method which is proposed by Frey[30]. Different from the popular $k$ -centers clustering technique, the affinity propagation method recursively transmits real-valued messages along edges of the network and is not sensitive to initial selection of exemplars. In affinity propagation, there are three definitions: similarity $s(i, k)$, responsibility $r(i, k)$ and availability $a(i, k)$.

$$
\begin{aligned}
& s(i, k)=-\left\|x_{i}-x_{k}\right\| \\
& r(i, k) \leftarrow s(i, k)-\max _{k^{\prime}, s, t, k^{\prime} \neq k}\left\{a\left(i, k^{\prime}\right)+s(i, k^{\prime})\right\} \\
& a(i, k) \leftarrow \min \left\{0, r(k, k)+\sum_{i^{\prime}, s, t, k^{\prime} \neq i, k}\left\{0, r(i^{\prime}, k)\right\}\right\}
\end{aligned}
$$

The similarity $s(i, k)$ indicates how well the data point with index $k$ is suited to be the exemplar for data point $i$. When the goal is to minimize the squared error, each similarity is set to a negative squared error (Euclidean distance). The responsibility $r(i, k)$, sent from data point $i$ to candidate the exemplar point k , reflects the accumulated evidence for how the well-suited point $k$ is to serve as the exemplar for point $i$, taking into account other potential exemplars for point $i$. The availability $a(i, k)$, sent from the candidate exemplar point $k$ to point $i$, reflects the accumulated evidence for how appropriate it would be for point $i$ to choose the point $k$ as its exemplar, taking into account the support from other points that the point $k$ should be an exemplar.

In the first iteration, because the availabilities are zero, $r(i, k)$ is set to the input similarity between point $i$ and point $k$ as its exemplar, minus the largest of the similarities between point $i$ and other candidate exemplars. This competitive update is data-driven and does not take into account how many other points favor each candidate exemplar. In later iterations, when some points are effectively assigned to other exemplars, their availabilities will drop below zero as prescribed by the update rule below. These negative availabilities will decrease the effective values of some of the input similarities $s\left(i, k^{\prime}\right)$ in the above rule, removing the corresponding candidate exemplars from competition. For $k=i$, the responsibility $r(k, k)$ is set to the input preference that the point $k$ be chosen as an exemplar, $s(k, k)$, minus the largest of the similarities between point $i$ and all other candidate exemplars. This self-responsibility reflects accumulated evidence that the point $k$ is an exemplar, based on its input preference tempered by how ill-suited it is to be assigned to another exemplar.

## - 3.2.3 Gaussian Mixture Model

A probabilistic model needs to be constructed each iteration. The model should be able to estimate the probability distribution of promising solutions so that the new individuals have a potential to be better ones. Further, the model should be constructed based on the solutions in the current iteration, which can be treated as a sample drawn from an unknown probability distribution. In order to construct a model for dynamic problems, Gaussian Mixture Model (GMM) is selected.

GMM is a parametric probability density function represented as a weighted sum of Gaussian component

densities[31]. With $M$ component Gaussian densities, a Gaussian mixture model is given by the equation:

$$
p(x \mid \lambda)=\sum_{i=1}^{M} \omega_{\lambda} \mathrm{g}\left(x \mid \mu_{i}, \Sigma_{i}\right)
$$

where $x$ is a D-dimensional continuous-valued data vector, $\omega_{\lambda} i=\mathrm{L} \cdots, M$, are the mixture weights, and $\mathrm{g}\left(x \mid \mu_{i}, \Sigma_{i}\right)$, $i=\mathrm{L} \cdots, M$, are the component Gaussian densities. Each component density is a D-variate Gaussian function in the form:
$\mathrm{g}\left(x \mid \mu_{i}, \Sigma_{i}\right)=\frac{1}{(2 \pi)^{D / 2}\left|\Sigma_{i}\right|^{D / 2}} \exp \left\{-\frac{1}{2}\left(x-\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(x-\mu_{i}\right)\right\}$
with mean vector $\mu_{i}$ and covariance matrix $\Sigma_{i}$. The mixture weights satisfy the constraint that $\sum_{i=1}^{M} \omega_{\lambda}=1$. The complete Gaussian mixture model is parameterized by the mean vectors, covariance matrices and mixture weights from all component densities. These parameters are collectively represented by the notation $\lambda=\left\{\omega_{\lambda}, \mu_{i}, \Sigma_{i}\right\}$.

For clusters in section 3.2.2, the GMM mixture weights can be determined by:

$$
\omega_{\lambda}=C_{i} / \sum_{i=1}^{M} C_{i}
$$

where $C_{i}$ is the number of individuals in the $i$ th cluster and $M$ is the number of the cluster. In the $i$ th cluster, the parameters $\mu_{i}, \Sigma_{i}$ are easy to be determined with expectation maximization algorithm.

### 3.3 Update of the population

Update of the population includes two steps: sampling and replacement. Sampling from the probabilistic model serves to generate the new population. In this paper, new population is sampled from Gaussian mixture model. In order to escape from the stagnation due to a very fast decrease of the variance, variances of the Gaussian mixture models are modified with a scale parameter. During the evolution, the sampling procedure is invoked at every generation, except the first one where seeding is applied.

In order to preserve the better solutions in the previous population and promote diversity in the current population, replacement is used. The elitism individual is selected from the previous populations proportional to fitness value and the new population is partially replaced by the elitism set according to the ranking of the fitness values.

### 3.4 Main procedure of AffEDA for dynamic optimization

In summary, given $t_{f}, n_{\max }$ and $n_{\min }$, the main procedure of AffEDA is described as below:

Step 1: Determine the number of iteration $N$, population size $n_{p}$, elitism size $n_{e}$ and selection ratio $\tau$

Step 2: Execute discretization of the time interval and randomly initialize the control variables according to section 3.1

Step 3: Select $\tau \times n_{p}$ individuals according to the fitness value, clustering these individuals using affinity propagation and construct GMM according to section 3.2 and 3.3; keep $n_{e}$ elicit individuals in the current generation.

Step 4: Generate new samples from the GMM, and replace $n_{e}$ worst samples using the elitism.

Step 5: If the stop criteria or the number of iteration $N$ is reached, stop. Else return to Step 3 for the next iteration.

These algorithms are compared in terms of robustness, efficiency and scalability. For each problem, 10 runs of each algorithm are carried out. Considering the randomness of these heuristic methods, solutions are seen as equivalence and successful when they lie in an interval of range $\pm 2 \%$. The robustness is defined as the percentage of successful solutions along different runs. As for the efficiency of algorithms, it considers not only the number of successful solutions, but also the iterative number of generations. The efficiency index is defined as:
$\mathrm{A}_{\text {eff }} \frac{\text { Minimum Generations }}{\text { Average Generations }} \times \frac{\text { number of successful runs }}{\text { number of all runs }}$
With this definition, the efficiency is given by the successful value of iteration numbers. Regarding scalability, it shows the convergence performance when increasing discretization levels with a reasonable increase of the computation effort.

## IV. NUMERICAL EXPERIMENTS

### 4.1 Typical Cases

Three cases are selected to test the proposed method and the procedure. The first and second case is from test problem 4 and 2 in [10] seperately, and the thrid case is from [32] named Park-Ramirez bioreactor.

### 4.2 Parameter setting

In order to test the performance of AffEDA, three process engineering dynamic optimization problems with different levels of complexity are considered in the present study. Control variables are discretized into $n$ control stages according to the time interval and then integrated. Besides compared with the results coming from the references, three other global optimization methods, such as Genetic algorithm (GA), Particle Swarm Optimization (PSO) and Estimation of Distribution Algorithms using full multivariate Gaussian model (EDA-G) are applied as other comparisons. In these algorithms, the population size is set 100 , and the initial population is generated uniformly. The algorithms run until the iteration is large than 100 or the weighted average change in the fitness function value over continuous five generations is less than $10^{-6}$ with the iteration larger than 50 . Other specific parameters are listed in TABLE I.

TABLE I. PARAMITERS SETTING


### 4.3 Results and discussion

For Case 1, the time interval is discretized into 10, 20 and 50 number and control variable is discretized accordingly. With 25 runs for each algorithm, the results of AffEDA comparing with the results from references are shown in TABLE II. It is obvious that the global optimal found by AffEDA is as good as the results in the references. That means that AffEDA also has the strong search ability and can escape from local peaks for this case study.

In order to compare different algorithms in the same platform, the results of GA, PSO, EDA-G and AffEDA with different levels of discretization is presented in TABLE III. For this case, the best and worst solution using AffEDA is the same, which means that AffEDA can converge to the same optima every time. The robust value also illustrates this point. With the highest efficiency, AffEDA can obtain the optimal using the least iteration. With the increase of the time interval, better global optimal can be found using AffEDA while the search performance decreases using other algorithms such as GA. In summary, for this problem, the whole performance of AffEDA is superior to other algorithms.

TABLE II. COMPARISONS BETWEEN AFFEDA AND REFERENCES FOR CASE 1

TABLE III. RESULTS COMPARISON BETWEEN AFFEDA AND OTHER ALGORITHMS FOR CASE 1

For Case 2, the time interval is the same as that in case 1. The results of 10 different runs are shown in TABLE IV comparing with the global optimal from the literature. Clearly, AffEDA can find the smaller point for minimum problem and the obtained optimal is $5 \%$ less than the result using IACA.

Results of different algorithms used in case 2 is shown in TABLE V. In comparison, AffEDA can find the better point. Moreover, its robustness is close to $100 \%$ even if the discretization grows. While using GA, the robustness and efficiency decrease quickly with the increase of discretization. Because PSO searches the space more randomly, it is unsuitable for solving the dynamic problems without adaptation. Though EDA-G has the same structure with AffEDA, the clustering method and the proper probabilistic model direct AffEDA to search the space more effectively and efficiently.

In this paper, the case 3 is solved by discretizing 45 or 150 time intervals. TABLE VI shows the results using AffEDA comparing with results coming from literature. It is obvious that AffEDA is valid for complex dynamic problems. With the increase of time interval, AffEDA can find better solutions than other algorithms.

TABLE IV. COMPARISONS BETWEEN AFFEDA AND REFERENCES FOR CASE 2

TABLE V. COMPARISONS BETWEEN AFFEDA AND OTHER ALGORITHMS FOR CASE 2

The results of AffEDA are compared with other algorithms shown in TABLE VII. For complex dynamic problems, evolutionary algorithm can't find better solutions with the increase of control variable discretizations, because the dimension of the variables increases than the performance of the algorithms. For AffEDA, with the increase of discretization, the robustness still keeps $100 \%$. But the efficiency decreases, which means the more control variables cost more time for function fitness evaluations. In the whole the robustness, efficiency and scalability of AffEDA is superior to other algorithms.

TABLE VI. COMPARISONS BETWEEN AFFEDA AND REFERENCES FOR CASE 3


TABLE VII. COMPARISONS BETWEEN AFFEDA AND OTHER ALGORITHMS FOR CASE 3


In summary, by comparing among different evolutionary algorithms, the performance ranks AffEDA the first place regarding both solving problems and efficiency for the set of case studies considered in this work. Furthermore AffEDA obtained better results for increasing discretization levels practically all cases with a reasonable increase of the

computational effort. In contrast, all other methods experienced convergence difficulties when increasing the number of decision variables.

## V. CONCLUSIONS

In this work, we presented a new probability distribution estimation based algorithm AfEDA for solving dynamic optimization problems. This novel approach introduces affinity propagation which clusters the populations during the evolution. For each cluster, Gaussian mixture model is used for constructing the probabilistic density functions. By comparing with other evolutionary algorithms, AfEDA refines the promising spaces containing high quality solutions. Based on these strategies, AffEDA speeds up the convergence to optimal solutions without performing too many redundant searches. To evaluate the performance of the new approach, three dynamic optimization problems of chemical process are used. For the sake of comparison, these problems were also optimized by several state-of-the-art global optimization methods. The results revealed that AffEDA could achieve the best solution in most cases with the least computational effort. In addition its performance was shown to scale up well with increasing discretization levels of the control variables, allowing the computation of more refined control profiles in reasonable computation times.

## ACKNOWLEDGEMENT

Supported by Major State Basic Research Development Program of China (2012CB720500), National Natural Science Foundation of China (U1162202, 61222303), the Fundamental Research Funds for the Central Universities, Shanghai Municipal Natural Science Foundation(No.13ZR1411500) and Shanghai Leading Academic Discipline Project (B504).
