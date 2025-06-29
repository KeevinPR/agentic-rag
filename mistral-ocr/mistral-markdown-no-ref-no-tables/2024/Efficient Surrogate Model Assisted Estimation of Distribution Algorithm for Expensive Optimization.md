# Efficient Surrogate Model Assisted Estimation of Distribution Algorithm for Expensive Optimization 

JIN SHANG ${ }^{\odot 1}$, GUIYING LI ${ }^{\odot 2}$, HAO HAO ${ }^{\odot 3}$, AND YUFANG ZHANG ${ }^{\odot 1}$<br>${ }^{1}$ Control Technology Institute, Wuxi Institute of Technology, Wuxi 214121, China<br>${ }^{2}$ School of Mechanical \& Electrical Engineering, Heilongjiang University, Harbin 150080, China<br>${ }^{3}$ Institute of Natural Science, Shanghai Jiao Tong University, Shanghai 200240, China<br>Corresponding author: Guiying Li (liguiying@hlju.edu.cn)

This work was supported by Jiangsu Province University Science and Technology Innovation Team Project.


#### Abstract

In recent years, several surrogate assisted evolutionary algorithms (SAEAs) have been proposed to solve expensive optimization problems. These problems lack explicit expressions and are characterized by high invocation costs. SAEAs leverage surrogate models to accelerate convergence towards the optimal region and reduce the number of function evaluations. While Gaussian Processes (GPs) are widely used due to their robustness and capability of providing uncertainty estimates, their applicability becomes limited in scenarios involving a large number of samples or high-dimensional spaces. This is due to their cubic time complexity in relation to the number of samples, which results in prohibitive computational demands for large-scale problems. To address the challenge, this work presents an efficient surrogate model-assisted estimation of the distribution algorithm (ESAEDA). This method employs a random forest as a surrogate model and combines it with a GP-hedge acquisition strategy to ensure the efficiency and accuracy of model-assisted selection. An improved EDA model called the variable-width histogram model with some unevaluated solutions is used to generate new solutions. To demonstrate the benefits of the proposed method, we compared ESAEDA with several state-of-the-art surrogate-assisted evaluation algorithms and the Bayesian optimization method. Experimental results demonstrate the superiority of the proposed algorithm over these comparison algorithms for two well-known test suites.


INDEX TERMS Artificial intelligence, optimization algorithm, random forest.

## I. INTRODUCTION

In some real-world applications, the box-constrained problem is computationally expensive and is considered a black-box function because its inner workings are difficult to trace and it can only be accessed based on its inputs and outputs. The expensive evaluation cost, coupled with the lack of a closed-form objective function, poses significant challenges to traditional numerical and heuristic optimization methods.

Classical optimization methods, such as linear programming and convex optimization, may not always be suitable for addressing the aforementioned problems due to their

[^0]reliance on favorable function properties [1]. As a result, there has been growing interest in the use of derivative-free or heuristic optimization methods [2], [3], [4], which do not rely on strong assumptions or closed-form dependencies of the optimization problem. Among these methods, evolutionary algorithms (EAs) show promise due to their trial-and-error strategies, but their effectiveness heavily relies on fitness values (objective values) to guide the search [5]. Therefore, frequent evaluations of the objective function pose challenges in practice, especially in expensive black-box optimization problems [6], [7].

In recent years, Surrogate-Assisted Evolutionary Algorithms (SAEAs) have emerged as a promising approach to tackling expensive optimization problems. In SAEAs, the


[^0]:    The associate editor coordinating the review of this manuscript and approving it for publication was Qiang Li ${ }^{\circledR}$.

surrogate model replaces the expensive real function evaluations. Since surrogate modeling and prediction require much less computational budget than directly using the expensive real black-box function, the approach can significantly reduce the optimization cost. SAEAs consist of two significant operators, namely the reproduction operator and the model-assisted selection operator. The former is responsible for exploring the search space, while the latter is accountable for selecting promising offspring solutions. The two operators alternate their execution, driving the population towards the optimal region.

In current research on SAEAs, a significant amount of work has been focused on studying model-assisted operators. Based on the type of model, this can be divided into three categories. The first category is regression-based SAEAs, which use a model to map a decision variable vector to its corresponding objective value. Popular surrogate models used for this type of SAEA include polynomial regression [8], radial basis function (RBF) networks [9], and Gaussian processes (GPs) [10]. The second category is classificationbased SAEAs, where solutions are assigned labels based on their quality. Surrogate models used in this paradigm include support vector machines [11], artificial neural networks [12], and fuzzy K-nearest neighbors [2]. The third category is relation-based SAEAs. Loshchilov et al. [13] argue that comparison-based optimization algorithms like evolutionary algorithms require surrogate models that are also comparison-based. This is because the relational model is used to learn the comparative relationships between solutions. While supervised learning methods can be used to learn these relationships, the key difference is that the relations between solutions (i.e., superiority or inferiority) are learned as features, rather than features of a single solution. For example, in [13] and [14], surrogate models are used to predict the ranks of solutions. In another study [15], a convolutional neural network (CNN) is proposed to approximate the difference in fitness function values between two solutions, rather than directly approximating the fitness of a solution. Recently, Hao et al. [5], [16] proposed a series of methods to learn the relationship between pairs of solutions.

Among the various surrogate models highlighted in the literature, GPs have emerged as the preferred surrogate model for SAEAs due to their reliable modeling capabilities and accurate estimation of model response uncertainty. The combination of Gaussian Processes with acquisition functions, also known as model management strategies [17], allows for effective balancing of exploration and exploitation trade-offs, enabling SAEAs to exhibit powerful global optimization abilities when tackling expensive black-box optimization problems. However, due to the high computational cost of GPs modeling, which is scaled cubically concerning the number of data points [18], it is not suitable for medium-to-large scale problems, which has limited the development of SAEAs.

In terms of reproduction operators, current SAEAs employ methods such as genetic algorithms (GA) [12], differential evolution (DE) [19], and particle swarm optimization (PSO)
[20] as operators for producing new solutions. These operators have all demonstrated good global search capabilities in SAEAs. However, another type of population-based solution generation operator has not been widely used in SAEAs, namely the distribution estimation algorithm (EDA) [21]. This method models the current population and generates new solutions through sampling. By utilizing global information to guide population search, it exhibits stronger global optimization capabilities, potentially enhancing the search efficiency of SAEAs.

Cai et al. [22] explore event-triggered consensus in multiagent systems, highlighting efficiency in communication and computation, crucial for cooperative control in distributed systems. He et al. [23] introduce the Dynamic Opinion Maximization Framework (DOMF) for social networks, addressing the dynamic nature of user opinions and challenges like non-monotonicity and non-submodularity. They present a blockchain-based solution for secure data offloading in healthcare, combining blockchain technology with deep reinforcement learning for enhanced data privacy and computational efficiency [24]. Cai et al. [25] focus on adaptive control in heterogeneous systems, improving real-time response and synchronization, essential for managing multi-agent system behaviors. Zhong et al. [26] introduce a surrogate ensemble-assisted hyper-heuristic algorithm designed to tackle expensive optimization problems. It combines multiple surrogate models to estimate the fitness of potential solutions, enhancing the efficiency and accuracy of finding optimal solutions. This method is particularly useful in scenarios where traditional optimization techniques fall short due to computational expense or complexity. Pan et al. [27] present a hybrid optimization algorithm that integrates surrogate models with evolutionary strategies. It aims to reduce computational costs while solving expensive optimization challenges, demonstrating significant improvements in both speed and solution quality. The approach provides a promising direction for addressing complex problems in various engineering fields. Chen et al. [28] detail a surrogate model-assisted algorithm for multi-objective optimization with an application in wind farm layout design. By incorporating Sparse Gaussian Process models, the algorithm achieves high accuracy and computational efficiency, showcasing its capability to enhance wind farm performance and its applicability to real-world engineering problems. He et al. [29] present a reinforcement-learningbased approach for competitive opinion maximization in signed social networks. The authors develop a two-phase model incorporating an activated dynamic opinion model and a reinforcement-learning-based seeding process to identify and influence key individuals in social networks, optimizing the spread of opinions against competitive opinions. The results confirm the method's effectiveness in achieving superior opinion propagation across various datasets.

In SA-EDA [30], a GPs assisted EDA algorithm is proposed, which utilizes a variable-width histogram (VWH) to represent the distribution of the population. Due to its

focus on the potentially optimal regions, this VWH exhibits good performance on expensive black-box problems. However, due to the use of Gaussian processes as the surrogate model, the algorithm still faces challenges related to the curse of dimensionality and high computational complexity. To address these issues, this paper proposes an efficient surrogate assisted EDA, called ESAEDA. The main contributions of this algorithm are as follows:

- We introduce an efficient surrogate model-assisted estimation of distribution algorithm (ESAEDA) that employs a random forest as the surrogate model. This choice is pivotal as it significantly reduces the training budget compared to traditional Gaussian processes, thereby enhancing computational efficiency without compromising accuracy.
- ESAEDA incorporates multiple acquisition strategies to optimize model-assisted selection. This method leverages the predictive power of the surrogate model to select promising solutions from a pool of candidates, thereby reducing the number of expensive function evaluations needed.
- A distinctive feature of our approach is the incorporation of unevaluated solutions in the updating of the probability model. This technique allows for a richer exploration of the solution space, potentially uncovering superior solutions that might not be immediately evident through evaluated solutions alone.
- To improve the search capability on low-dimensional problems, we integrate the Powell method, a derivativefree optimization technique. This integration is specifically tailored to enhance the exploration capabilities of ESAEDA, particularly in scenarios where traditional methods may falter due to limited solution evaluations.
Section II provides an overview of related works. Section III presents a detailed description of the proposed method. Section IV empirically studies the new method with other comparisons on two widely used test suites. Finally, Section V concludes this paper and discusses some future works.


## II. RELATED WORK

## A. ESTIMATION OF DISTRIBUTION ALGORITHM

Estimation of distribution algorithms (EDAs) is a distinct evolutionary computation paradigm that employs probabilistic models to guide population search, unlike traditional genetic operators such as crossover or mutation. In EDAs, variable linkages are typically represented using Bayesian networks, which are learned from data using statistical and machine learning techniques. For EDAs to generate high quality samples, it is imperative to have a suitable Bayesian network model. Based on the variable linkages, Bayesian network models in EDAs can be classified into three categories [3]: univariate models, bivariate models, and multivariate models. Univariate histogram marginal models are a class of simple univariate histogram models that model
![img-0.jpeg](img-0.jpeg)

FIGURE 1. Illustration of random forest.
the distribution of the population using histograms. Decision variables are assumed to be independent and the joint probability of the variables is fully factorized as:

$$
P(\mathbf{x})=\prod_{j=1}^{n} P\left(x_{j}\right)
$$

where is the $j$ th variable of. In modeling, The data is divided into several bins according to a certain method, and each bin represents a probability interval. The probability weight of each bin is calculated based on the ratio of the number of samples it contains to the total number of samples. Four types of histogram models can be used to model for each dimension [3], [31], [32], including equal-width histogram (EWH) models, equal-height histogram (EHH) models, cluster-based histogram (CBH) models, and variable-width histogram (VWH) models. Among them, VWH models pay more attention to the potential optimal region in an EDA with cheap and expensive local search methods (EDALS) [3], providing stronger convergence speed and therefore serving as the basic model for the generation operator in this paper.

## B. SURROGATE MODEL

This study centers on the application of surrogate models in machine learning, with particular emphasis on random forests as a viable option due to their lower computational complexity in comparison to Gaussian processes. Figure 1 illustrates a schematic diagram of the random forest algorithm, which involves averaging multiple decision trees to decrease variances in a given dataset. The decision trees are trained on various subsets of the data, enabling robust and accurate predictions. For dataset $\mathcal{D}=\left\{\mathbf{x}_{1}, \mathbf{x}_{2}, \ldots, \mathbf{x}_{N}\right\}$, The bagging method is repeated ( $B$ times) to sample from $\mathcal{D}$ with put-backs and then train the tree model on these samples. After training, the prediction of a testing point x can be achieved by averaging the predictions of all individual regression trees on x . The predicted value is defined as follows.

$$
\hat{f}(\mathbf{x})=\frac{1}{B} \sum_{b=1}^{B} f_{b}(\mathbf{x})
$$

The predictions of all regression trees on x can be used as an estimate of the uncertainty.

$$
\sigma(\mathbf{x})=\sqrt{\frac{1}{B} \sum_{b=1}^{B}\left(f_{b}(\mathbf{x})-f^{\prime \prime}\right)}
$$

Random forests have gained widespread popularity in various practical fields due to their robust data fitting capabilities and relatively lower computational complexity. As a result, RF has been increasingly utilized as a surrogate model in various areas such as trauma systems [33], deep neural network optimization [34], and combinatorial optimization [35]. In this study, we utilize RF to fit black-box objective functions and reduce computational costs, with the ultimate goal of assisting the EDA in optimization.

## III. PROPOSED METHOD

## A. ALGORITHM FRAMEWORK

ESAEDA is presented in Algorithm 1. Its components are explained as follows.

## 1) INITIALIZATION

$N$ initial solutions are obtained by sampling from the search space $\Pi_{i=1}^{n}\left[a_{i}, b_{i}\right]$ using the Latin hypercube sampling method (LHS) [36]. Each of these solutions undergoes evaluation by the real expensive function $f(\cdot)$ and is subsequently stored in the archive $\mathcal{A}$. The count of evaluated solutions, denoted by fes, is updated accordingly. Based on the current population $\mathcal{P}$, a probability distribution model $P_{V W H}(X)$ is constructed [3].

## 2) STOPPING CONDITION

The termination criterion is defined as the number of real function evaluations exceeding the pre-specified maximum limit, denoted by $F E_{\max }$.

## 3) SURROGATE MODEL TRAINING

The surrogate model $\mathcal{M}$ is trained using the archive $\mathcal{A}$. Given the low complexity of the random forest, all solutions that stored in the archive are utilized to train the model.

## 4) GENERATE SOLUTIONS

The new N solutions are composed of two parts, where $\mathcal{Q}_{I}$ is generated by sampling from the $P_{V W H}(X)$, while $\mathcal{Q}_{H}$ is produced by local search on the current population $\mathcal{P}$. According to [3], this approach combines both global and local population information to enhance the quality of the offspring solutions.

## 5) SURROGATE ASSISTED SELECTION

The surrogate model $\mathcal{M}$ aids in two tasks. Firstly, utilizing a multiacquisition strategy based on the predicted value $f$ (mathbfx) and uncertainty $\sigma(\mathbf{x}$ to select the optimal solution $\mathcal{Q}_{\text {best }}$. Secondly, relying on the model predicted values, the top $N / 2$ solutions are chosen as the unevaluated good solutions.

Algorithm 1 Pseudocode of Main Framework
Input: $N$ (population size); $F E_{\max }$ (maximum number of FEs);
$n^{\prime}$ (threshold for using the Powell method).
// Initialization
$1 \mathcal{P} \leftarrow \boldsymbol{L H S}(N)$.
$2 \mathcal{A} \leftarrow \mathcal{P}$.
3 fes $\leftarrow N$.
$4 P_{V W H}(X) \leftarrow \boldsymbol{E D A}(\mathcal{P})$.
5 while fes $\leftarrow N \leq F E_{\max }$ do
//Surrogate model training
$6 \mathcal{M} \leftarrow \boldsymbol{T}$ raining $(\mathcal{A})$.
// Generate new solutions
$7 \mathcal{Q}_{I} \leftarrow \operatorname{Sample}\left(P_{V W H}(X)\right)$.
$8 \mathcal{Q}_{H} \leftarrow \operatorname{localsearch}(\mathcal{P})$.
$9 \mathcal{Q} \leftarrow$ Combination $\left(\mathcal{Q}_{I}, \mathcal{Q}_{H}\right)$.
// Surrogate assisted selection
$10 \quad \mathcal{Q}_{\text {best }}, \mathcal{Q}^{\prime} \leftarrow \boldsymbol{S A} \_\boldsymbol{S e l e c t i o n}(\mathcal{Q}, \mathcal{M})$.
// Update archive
$11 \mathcal{A} \leftarrow \mathcal{A} \cup \boldsymbol{E v a l u a t i o n}\left(\mathcal{Q}_{\text {best }}\right)$.
$12 \quad$ fes $\leftarrow$ fes +1 .
// Improve solution by Powell method
13 if improving and $n \leq n^{\prime}$ then
$14 \quad \mathcal{Q} \leftarrow \boldsymbol{P o w e l l}(\mathcal{A})$.
$15 \quad \mathcal{A} \leftarrow \mathcal{A} \cup \mathcal{Q}$.
$16 \quad$ fes $\leftarrow$ fes $+|\mathcal{Q}|$.
17 end
// Selection for next generation
$18 \mathcal{P} \leftarrow \mathcal{A}_{1: N}$.
// Update probability model
$19 P(X) \leftarrow \operatorname{Model}\left(\mathcal{P}, \mathcal{Q}^{\prime}\right)$.
20 end
Output: $\mathcal{A}_{\text {best }}$ (the optimum solution).

## 6) UPDATE ARCHIVE

The current best solution $\mathcal{Q}_{\text {best }}$ is evaluated using the real fitness function and stored in the archive $\mathcal{A}$.

## 7) IMPROVE SOLUTION BY POWELL METHOD

Powell method [37] is a derivative-free optimization algorithm that can effectively improve the convergence of our algorithm. Due to the significant fitness evaluation budget required by this method, which increases with the search dimension, we have devised a simple condition to activate it. Specifically, the Powell method will be used once when the search space dimension is no greater than 20 and there is no improvement in the $\mathcal{A}$ continuity for 10 iterations. All solutions evaluated during this process will be saved in $\mathcal{A}$.

## 8) SELECT SOLUTIONS FOR NEXT GENERATION

The next population $\mathcal{P}$ is formed by selecting the optimal N solutions based on the objective value from $\mathcal{A}$.

## 9) UPDATE PROBABILITY MODEL

The new EDA model will be updated, and the population will be derived from two parts. One part is the population $\mathcal{P}$ selected based on the real function values, while the other part is the population $\mathcal{Q}^{\prime}$ selected based on the surrogate model. This approach can further accelerate the convergence of the population towards the optimal region in next iteration.

The ESAEDA algorithm encompasses several principal components: initialization, training of the surrogate model, generation of new solutions, surrogate-assisted selection, archive updates, and updates to the probability model. The initialization phase predominantly utilizes Latin hypercube sampling, manifesting a time complexity of $\mathcal{O}(n)$, where $N$ signifies the size of the population. In the training of the surrogate model, a Random Forest method is employed, which incurs an approximate time complexity of $\mathcal{O}(M N \log (N))$, $M$ being the number of trees involved. The generation of new solutions hinges on the probability distribution model of the current population, entailing a time complexity of $\mathcal{O}(N D)$, with $D$ representing the dimensionality of the problem at hand. For the surrogate-assisted selection phase, the time complexity scales as $\mathcal{O}(M N D)$. Meanwhile, the tasks of updating the archive and the probability model are marked by high efficiency, each showcasing a time complexity of $\mathcal{O}(N)$. These integral steps collectively constitute the computational backbone of the ESAEDA algorithm as outlined in this study.

Algorithm 1 and SAEDA [30] share some similar processes, but to improve algorithm efficiency, we have the following main differences: 1) utilizing a random forest as a surrogate model to reduce modeling overhead, 2) using the Powell method to compensate for the degradation of search ability in low-dimensional spaces (compared to SAEDA), and 3) using unevaluated solutions to accelerate the search speed of the algorithm. In the following sections, we will provide further details regarding the new solution generation and offspring solutions selection techniques employed in our proposed algorithm.

## B. NEW SOLUTION GENERATION

In EAs, the quality of newly generated solutions directly affects the efficiency of the algorithm search. In this work, new solutions are generated through a combination of EDA and local search, and the Powell method is used to further improve the quality of low-dimensional spaces.

In this study, we utilize a variable-width histogram (VWH) model, as proposed by Zhou et al. [3], to serve as a probabilistic model. This approach focuses on identifying and exploiting promising regions within the search space, which is essential for achieving improved performance on expensive optimization problems. Rather than utilizing traditional crossover and mutation operators, the new population $\mathcal{Q}_{I}$ is generated by sampling from the probability distribution $P(X)$ of the current population $\mathcal{P}$. The VWH model represents a univariate model, where the $n$ dimensions of the solution vector $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ are assumed to be independent
![img-1.jpeg](img-1.jpeg)

FIGURE 2. Illustration of VWH model for population on early and late search stage.
of each other. The model can be expressed mathematically using (2), where $P_{j}\left(x_{j}\right)$ denotes the marginal probability function of the $j^{\text {th }}$ variable $x_{j}$.

In modeling, to partition the search space $\left[a_{j}, b_{j}\right]$ of the $j^{\text {th }}$ variable, a total of $M$ bins are created, denoted by $\left[a_{j, m}, a_{j, m}+\right.$ $1), m=0,1, \ldots, M-2$ and $\left[a_{j, M-1}, a_{j, M}\right]$, where $a_{j, 0}=a_{j}$ and $a_{j, M}=b_{j}$. The bins from the 2 nd to the $(M-1)^{\text {th }}$ are of equal width, focusing on the distribution of the current population. The size of each bin is determined based on the number of solutions falling in the current interval. The first and last two bins of the search space without solutions still have a very low probability to avoid premature convergence. Figure 2 illustrates the basic idea of VWH with different population distributions. The probability defined by $\prod_{j=1}^{n}\left[a_{j, 1}, a_{j, M-1}\right]$ is higher than other no-solutions space, which focuses more on the promising search areas, especially when the population converges to a small area (see Figure 2 (b)).

To generate a new solution $\mathbf{x}$, the probability distribution $P(X)$ is used to sample each component $x_{j}, j=1, \ldots, n$ independently. For each component, a bin is selected based on its corresponding probability function $P_{j}\left(x_{j}\right)$. Then, a value is randomly sampled within the boundaries of the selected bin to obtain the current $x_{j}$. This process is repeated for each component to obtain a complete solution $\mathbf{x}$. A variablewidth histogram (VWH) model, which partitions the search space into bins, is used as the probability distribution model. The size of each bin is determined by the number of solutions falling within that interval, with the bins in the middle focusing on the distribution of the current population. This approach focuses more on promising search areas and improves the performance of the SAEAs on expensive problems. In addition to using evaluated solutions in the archive to update the VWH model, this work also uses unevaluated solutions $\mathcal{Q}^{\prime}$ selected by the surrogate model to update the probability model, which improves the quality of newly sampled solutions and makes the VWH model work better in SAEAs.

Another part of the solutions will be generated by local search (Algorithm 1 line 8). This is achieved by using the method proposed in EDALS [3], which constructs a lightweight quadratic approximation model based on the parent population $\mathcal{P}$, and then generates $\mathcal{Q}_{I I}$ based on the

quadratic approximation model. Finally, $\mathcal{Q}_{I}$ and $\mathcal{Q}_{I I}$ are randomly combined with a certain probability, following the ratio of 0.8 for $\mathcal{Q}_{I}$ and 0.2 for $\mathcal{Q}_{I I}$ as proposed in [3] and [30]. Local search serves as a supplement to the EDA search.

In ESAEDA, we utilized RF as a surrogate model to improve the algorithm execution speed. However, surpassing the Gaussian process assisted EDA (SA-EDA) [30] in low-dimensional space became a challenging task. Therefore, we applied the Powell method (Algorithm 1 line 8) [37] to further enhance the quality of solutions. Due to the consumption of the evaluation budget required for this method and its increase with the dimensionality of the search space, we restricted its use to low-dimensional cases.

## C. OFFSPRING SELECTION

This subsection outlines the methodology employed for training and implementing a surrogate model for selecting candidate solutions from the current offspring population $\mathcal{Q}$ in the context of ESAEDA. The surrogate model is used to replace the expensive function, as outlined in (3). The prediction result obtained by multiple trees is utilized to estimate the modeling uncertainty of the current point, as denoted in (4). To determine the final $\mathcal{Q}_{\text {best }}$ solution, multiple acquisition functions' selection results are aggregated using the GPHedge method [38]. Additionally, top $N / 2$ population $\mathcal{Q}^{\prime}$ is selected based on the predicted value $\hat{f}(\cdot)$ by RF, which is subsequently used to update the VWH model.

In this work, acquisition functions are utilized to balance exploitation and exploration in the search process by selecting a promising solution $\mathcal{Q}_{\text {best }}$ based on the mean ( $\mu$ or $\hat{f}$ ) and variance $(\sigma)$ of the surrogate model predictions. To enhance the robustness of surrogate-assisted selection, the GP-hedge method is used to dynamically select a strategy from the three typical acquisition functions: expected improvement (EI), probability improvement (PI), and lower confidence bound (LCB), formulated in (5), (6), and (7), respectively. Here, $\mathbf{x}^{*}$ represents the current best solution in the archive, $\Phi(\cdot)$ is the standard normal distribution probability density function, and $\beta$ balances the expectation and variance in LCB. In the $t$-th generation, $\mathbf{x}_{E I}^{*}, \mathbf{x}_{P I}^{*}$, and $\mathbf{x}_{L C B}^{*}$ denote the optimal solutions that satisfy $\mathbf{x}_{E I}^{*}=\arg \max (E I(\mathbf{x})), \mathbf{x}_{P I}^{*}=$ $\arg \max (P I(\mathbf{x}))$, and $\mathbf{x}_{L C B}^{*}=\arg \min (L C B(\mathbf{x}))$, where $\mathbf{x} \in \mathcal{Q}$. GP-hedge selects a solution as $\mathcal{Q}_{\text {best }}$ based on the probability of the gains obtained by the three strategies in the previous $t-1$ generations. When $t=1$, a solution is randomly selected from the three candidates. The details of calculating the gains can be found in GP-Hedge.

$$
\begin{aligned}
E I(\mathbf{x}) & =\left(\mu(\mathbf{x})-\mathbf{x}^{*}\right) \Phi\left(\frac{\mu(\mathbf{x})-\mathbf{x}^{*}}{\sigma(\mathbf{x})}\right) \\
& +\sigma(\mathbf{x}) \Phi\left(\frac{\mu(\mathbf{x})-\mathbf{x}^{*}}{\sigma(\mathbf{x})}\right) \\
P I(\mathbf{x}) & =\Phi\left(\frac{\mathbf{x}^{*}-\mu(\mathbf{x})}{\sigma(\mathbf{x})}\right) \\
L C U(\mathbf{x}) & =-(\mu(\mathbf{x})-\sqrt{\beta} \sigma(\mathbf{x}))
\end{aligned}
$$

Moreover, using the approximate value $\hat{f}$ provided by the surrogate model, the new population $\mathcal{Q}$ is sorted in ascending order, and the top half of solutions are selected as the promising candidates without real evaluation to update the VWH model.

## IV. EXPERIMENTAL COMPARISON

To evaluate the effectiveness of the proposed methods, experiments were conducted on the LZG [27] and YLL [39] test suites in both 20 and 50 dimensions, along with some state-of-the-art methods, including surrogate model assisted algorithms, Bayesian optimization algorithms, and general evolutionary algorithms. The study included ablation experiments on two crucial components of the ESAEDA algorithm, called the Powell method and the VHW model with unevaluated solutions. Additionally, the runtime performance of ESAEDA is compared with some GPs assisted algorithms.

## A. EXPERIMENTAL SETTINGS

## 1) TEST SUITES

For the empirical study, two test suites were used. The first was the LZG test suite, which includes four test functions, namely Ellipsoid, Rosenbrock, Ackley, and Griewank. These functions have unimodal, gully, and multimodal landscapes. The second test suite used was the YLL test suite, which contains functions $f 1-f 4$ with unimodal landscapes, $f 5, f 8-$ $f 13$ with multimodal landscapes, $f 6$ with a step landscape, and $f 7$ with random noise. The problems in both test suites were evaluated in dimensions $n=20$ for small-scale and $n=50$ for median-scale.

## 2) ALGORITHM IN STUDY

Six algorithms are chosen for empirical study, namely CMAES [4], FCPS-CoDE [2], EDALS [3], SAMSO [28], Skopt, GPEME [27], and SA-EDA [30]. These algorithms can be divided into three categories:

- Basic EDA: CMA-ES and EDALS are two general EDAs, that are not specially designed for expensive optimization.
- Bayesian optimization: Skopt is an efficient global optimization algorithm in the Bayesian optimization (BO) framework. It applies GPs as the surrogate model.
- Surrogate assisted EAs: FCPS-CoDE uses a fuzzy K nearest neighbor based classification model to evaluate candidate solutions. GPEME uses GPs to evaluate candidate solutions. SAMSO is a surrogate assigned particle swarm optimization with RBF. SA-EDA is a GPs assisted EDA.


## 3) PARAMETER SETTINGS

In the empirical study, we use the recommended parameters in the original literature for each algorithm for a fair comparison, and the details are given below.

TABLE 1. Statistics of median results obtained by nine comparison algorithms on LZG and YLL test suites with $\mathbf{n}=\mathbf{2 0}$.

- Termination condition: The maximum number of FEs is adopted as the termination condition, set at 500 for all instances.
- Population size: Set $N=30$ for CMA-ES, EDALS and FCPS-CoDE. Set $N=40$ for SAMSO (default set in PlatEMO [40]). Set $N=50$ for GPEME, SA-EDA and ESAEDA.
- Parameters of compared algorithms: default setting according to the original version.
In addition, to demonstrate the effectiveness of the ESAEDA components, two variants were designed as follows:
- ESAEDA*: the Powell method was removed during the iterative process.
- ESAEDA**: the VWH model was updated without using unevaluated solutions.
Each algorithm is executed on each test instance for 30 independent runs to overcome randomness. The first step is to assess the independence of the results obtained by the algorithms on each test instance by the Friedman test [41]. Then the Wilcoxon rank sum test [42] is used to compare the results where ${ }^{+}+{ }^{+},{ }^{-},{ }^{-}$, and ${ }^{-} \sim$ ' in the tables indicate the value obtained by an algorithm is smaller than, greater than,
or similar to that obtained by the ESAEDA based version at a 0.05 significance level. The value in the brackets denotes the corresponding rank.


## B. RESULTS AND ANALYSIS

Table 1 presents the statistical findings of 9 optimization algorithms evaluated on two test suites. The results are provided in terms of p-value by the Friedman test, mean ranks, and the corresponding Wilcoxon rank sum test. The p-value obtained from the Friedman test is much less than 0.05 , indicating a significant difference between the results. The analysis indicates that ESAEDA achieves the best mean rank of 2.53, outperforming the BO algorithm Skopt, which achieves a mean rank of 6.71. The general evolution algorithms, CMAES and EDALS, achieve mean ranks of 7.24 and 3.41, respectively. Among the SAEAs, SA-EDA and GPEME attain the first and second mean ranks in the four comparison algorithms due to the Gaussian process, providing accurate modeling. However, the increased computational overhead associated with these approaches is discussed in the following subsection. The Wilcoxon rank sum test also supports the superiority of ESAEDA as it obtains better optimal solutions than other algorithms in most instances. Importantly, the

![img-2.jpeg](img-2.jpeg)

FIGURE 3. The median runtime performance of 6 algorithms on LZG and YLL test suites.

TABLE 2. Statistics of median results obtained by six comparison algorithms on LEG and YLL test suites with $\mathbf{n}=50$.

Powell method applied in ESAEDA* effectively improves the performance of EDA algorithms in low-dimensional problems. The results of Table 1 indicate significant differences among the algorithms. ESAEDA consistently achieved the best mean rank, outperforming the Bayesian optimization algorithm Skopt and other general and surrogate-assisted evolutionary algorithms. Specifically, ESAEDA showcased superior convergence performance and optimal solution quality in most test instances, signifying its effectiveness over conventional and contemporary approaches.

Due to the limitation of Gaussian process-based methods in median dimension space, we selected a subset of algorithms for 50-dimensional problems, including CMAES, FCPS-CoDE, EDALS, SAMSO, and SA-EDA. As the Powell method does not apply to ESAEDA in 50 dimensions, the variant ESAEDA* was not included in the experiment. Table 2 presents the statistical results, indicating that ESAED outperforms SAMSO, a specifically designed method for large-scale expensive optimization problems, achieving the best mean of 1.82 under 50 problems. Furthermore, ESAEDA also achieved better results than GP assisted EDA, demonstrating its competitive performance. The Wilcoxon rank sum test supports these results, demonstrating ESAEDA's
superior performance in most instances compared to other algorithms. Figure 3 illustrates the convergence performance of all algorithms, with results consistent with those in Table 2. ESAEDA exhibits the best convergence performance on most test instances.

ESAEDA outperforms several state-of-the-art algorithms by demonstrating superior convergence performance on widely used test instances. It achieves significantly better median results compared to other algorithms. The algorithm exhibits remarkable computational efficiency, achieving 1090 times efficiency improvements compared to Gaussian Process-assisted algorithms on problems of varying dimensions (20D and 50D). Besides demonstrating competitive performance in tackling expensive optimization problems, ESAEDA holds promise for extending its application to solve expensive multi-objective optimization problems, thereby presenting a versatile and practical approach for real-world scenarios.

The novel aspect of ESAEDA lies in its unique combination of a random forest surrogate model with the estimation of distribution algorithms, which is not commonly found in existing studies. This combination offers a new pathway to reduce computational costs while maintaining solution

![img-3.jpeg](img-3.jpeg)

FIGURE 4. The runtime performance of ESAEDA and its variant on LZG and YLL test suites over 30 independent runs.
quality. Additionally, the innovative use of unevaluated solutions to update the probability model represents a significant departure from conventional approaches, aiming to accelerate convergence without excessive function evaluations.

## C. ROLES OF ESAEDA

In this subsection, we will analyze the key characteristics of the ESAEDA algorithm. First, we will analyze the benefits of adding unevaluated solutions for the probabilistic model. Second, we will analyze the efficiency improvement of using RF as the surrogate model.

The importance of unevaluated solutions in the update of the probability model in ESAEDA is verified in Figure 4. The figure shows the convergence curves of ESAEDA and its variants on some test instances over 30 independent runs. It is
observed that the convergence of the algorithm can be further improved by incorporating unevaluated solutions in the VWH model updating. These solutions, although not evaluated by the real function, are still valuable as they are selected by the surrogate model. These solutions have a positive impact on the convergence of the population, thereby enhancing the quality of the offspring solutions.

Next, the running time of different algorithms on LZG01 is analyzed. Two Gaussian process based algorithms, SA-EDA and GPEME, are selected as a comparator with ESAEDA. All algorithms are run on the same hardware platform (Apple M1pro and 32G Memory). We run each algorithm on the LZG01 under the same function evaluations (fes) for 10 independent runs. The mean CPU time obtained by three algorithms is recorded in Figure 5.

![img-4.jpeg](img-4.jpeg)

FIGURE 5. Bar plot of running time of ESAEDA, SA-EDA and GPEME on LZG01 under 500 fitness evaluations.

Using the computational lightweight surrogate model (For n samples, the complexity of RF is $\mathcal{O}(\operatorname{nlog}(n))$ and the complexity of GPs is $\mathcal{O}\left(n^{3}\right)$ ), the ESAEDA has the lowest computational overhead among all algorithms tested, when executing the same number of iterations.

The proposed ESAEDA distinguishes itself with unique features. It utilizes RF as the surrogate model, significantly reducing computational demands compared to traditional Gaussian Process-based approaches. This adjustment leads to a more efficient resolution of expensive optimization problems. Additionally, ESAEDA employs unevaluated solutions to update its probabilistic model, thereby improving the generation of new solutions and accelerating convergence. Furthermore, the incorporation of the Powell method enhances search capabilities in low-dimensional spaces, addressing potential declines in search efficiency.

## V. CONCLUSION

This paper proposes an efficient surrogate model-assisted estimation of distribution algorithm (ESAEDA) which aims to tackle expensive optimization problems. The use of random forest as a surrogate model instead of Gaussian processes results in significant reductions in computational overhead. The surrogate model works in conjunction with the GP-hedge strategy to identify promising solutions for real evaluations. The improved EDA with unevaluated is used to generate promising solutions. The VWH model focuses on promising areas and accelerating algorithm convergence. Additionally, the enhanced EDA with unevaluated samples is used to generate promising solutions, while the VWH model is utilized to focus on promising areas and accelerate the convergence of the algorithm. Local search and the Powell method are also incorporated to improve the quality of the population.

ESAEDA is benchmarked against several state-of-the-art algorithms on 17 widely used test instances, and the results
indicate that it performs well. Furthermore, the running time of the algorithm is analyzed, and the new method is shown to achieve 10-90 times efficiency improvements compared to Gaussian process assisted algorithms on 20D and 50D problems. This efficiency is a critical advantage in real-world applications where evaluation costs are high. The algorithm's design allows for faster convergence compared to traditional methods and some state-of-the-art algorithms, making it a viable option for expensive optimization problems. Extending ESAEDA to solve expensive multi-objective optimization problems holds promise, and its application to real-world problems is highly desirable.

It is worth noting that the Powell method has been significantly enhanced through integration with contemporary optimization technologies, such as cuckoo search, extending its applicability beyond traditional domains. This synergy has led to more accessible and efficient solutions for various nonlinear optimization issues, as illustrated by initiatives like PRIMA that aim to provide practical, derivative-free optimization frameworks. Moreover, the innovative application of the Powell method in evolutionary algorithms for hyperparameter optimization showcases its extended utility in the realm of machine learning and artificial intelligence. This adapted version, aimed at meeting the specific requirements of hyperparameter tuning in complex computational models, signifies the method's adaptability and potential. In future work, this enhanced Powell method could be applied within ESAEDA to further enhance the method's performance.

The proposed ESAEDA exhibits certain limitations, notably in handling high-dimensional problems due to its reliance on the Powell method, which is primarily effective in low-dimensional scenarios. To address this, future work could explore integrating techniques that enhance high-dimensional search capabilities. Additionally, ESAEDA's performance heavily depends on the accuracy of

the Random Forest surrogate model. An adaptive approach that selects the most suitable surrogate model based on current performance metrics could improve robustness and efficiency across diverse problem landscapes.
