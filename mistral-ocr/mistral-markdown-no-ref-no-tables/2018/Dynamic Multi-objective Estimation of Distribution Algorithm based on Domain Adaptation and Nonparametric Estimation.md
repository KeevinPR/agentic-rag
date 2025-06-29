# Dynamic Multi-objective Estimation of Distribution Algorithm based on Domain Adaptation and Nonparametric Estimation 

Min Jiang a,b, Liming Qiu a,b, Zhongqiang Huang a,b, Gary G. Yen c,*

${ }^{a}$ Department of Cognitive Science and Technology, Xiamen University, China
${ }^{\mathrm{b}}$ Fujian Key Laboratory of Brain-like Computing and Application, Xiamen University, China
${ }^{c}$ School of Electrical and Computer Engineering, Oklahoma State University, 202 Engineering South, Stillwater, OK 74078, USA

## A R T I C L E I N F O

Article history:
Received 6 September 2017
Revised 28 December 2017
Accepted 29 December 2017
Available online 2 January 2018

## Keywords:

Dynamic multi-objective optimization
Domain adaption
Nonparametric statistics
Importance sampling
Transfer learning

## A B S T R A C T

Although dynamic optimization and multi-objective optimization have made considerable progress individually, solving dynamic multi-objective optimization problems remains a monumental challenge since their multiple, conflicting objectives could change over time. In this paper, we propose a Domain Adaptation and Nonparametric Estimation-based Estimation of Distribution Algorithm, called DANE-EDA, to solve dynamic multi-objective optimization problems. Notable features of the proposed algorithm include the importance sampling, nonparametric density estimation, probabilistic prediction, and a domain adaptation technique seamlessly unified under an innovative framework. The design takes full advantage of the powerful Monte-Carlo method and transfer learning technique. This kind of combination will help the proposed algorithm to maintain a delicate explorationexploitation trade-off from temporal and spatial perspectives. At the same time, it will help the proposed algorithm to overcome the shortcomings caused by transfer learning, specifically, the loss of the diversity. After proving convergence and analyzing the computational complexity of the DANE-EDA, we compare the proposed method with nine EDAs or dynamic multi-objective optimization algorithms on twelve different test instances. The experimental results affirm the effectiveness of the proposed method in addressing dynamic multi-objective optimization problems.
(c) 2018 Elsevier Inc. All rights reserved.

## 1. Introduction

Many real-world problems not only need to optimize multiple competing objectives simultaneously, but also are characterized by time-varying objective functions or dynamic environments. These problems are called Dynamic Multi-objective Optimization Problems (DMOPs). A typical scenario where DMOPs arises comes from job shop scheduling. In these problems, new job demands may arrive or machines may break down or wear out during operation [6]. Therefore, the job schedules should be dynamically modified to accommodate conflict, while meeting the multiple objectives of maximizing the yield and minimizing material waste. Another convincing example is dynamic portfolio management, which is a common optimization problem in modern finance [27]. This problem aims to obtain an optimal allocation of assets to maximize profit, while minimizing risk of investment. In engineering, dynamic portfolio optimization problems are common in deregulated

[^0]
[^0]:    * Corresponding author.

    E-mail addresses: minjiang@xmu.edu.cn (M. Jiang), gyen@ukstate.edu (G.G. Yen).

electricity markets in which the operations of different power stations are controlled and coordinated to maximize profit and minimize risk. Obviously, a good solution of the DMOPs often leads to significant economic benefits.

Although multi-objective optimization and dynamic optimization (mainly for single-objective) have separately made much progress, solving a given DMOP remains a challenging research topic, especially by means of analytic approaches. Therefore designing different heuristic algorithms remains appealing to the scientific community [33]. As a meta-heuristic approach, the Estimation of Distribution Algorithm (EDA) [24] combines statistical machine learning with a population-based evolution heuristic. Most EDAs usually establish a probabilistic model using statistical machine learning methods and then use this model to generate the next population. Different from traditional evolutionary algorithms which heavily rely upon proper designs of crossover and mutation operations, the learning and sampling procedures over probabilistic models in EDAs determine the effectiveness and efficiency of the performance. Many researchers [14] believe that the EDAs can provide unique advantages which other meta-heuristic methods do not have for solving optimization problems, particularly for handling high dimensionality or complex optimization tasks.

Significant progress has been made in the EDA field recently. For example, the multi-objective Bayesian Optimization Algorithm (mBOA), proposed by Khan et al. [20], combines the Bayesian Optimization Algorithm (BOA) [31] with the Nondominated Sorting Genetic Algorithm (NSGA-II) for solving multi-objective optimization problems. In essence, this algorithm wants to achieve some kind of exploration-exploitation balance by imposing proper selection pressures, and the Bayesian network plays a crucial role in this process. The multi-objective hierarchical BOA (mohBOA), proposed by Pelikan et al. [32], also adopts a similar procedure originated from NSGA-II to select possible candidate individuals. The unique design of mohBOA is that, after candidate individuals are selected, mohBOA finds the clusters of promising solutions by k-means clustering algorithm and uses restricted tournament replacement to merge the newly obtained clusters with the old population by using restricted tournament replacement to generate the next population. The experiments show that mohBOA can solve the onemax-zeromax and trap5-invtrap5 [32] in low-order polynomial time. Shah et al. [35] proved that $\epsilon$-hBOA, an $\epsilon$-dominance hierarchical BOA, outperforms two chosen evolutionary algorithms in solving multi-objective d-dimensional knapsack problems. However, most of the existing EDA methods have room for improvement when solving the dynamic multi-objective optimization problems.

In recent years, the prediction-based approach [28] has drawn more attention from the field of dynamic optimization. This class of methods predicts the changing optimization functions typically using some machine learning techniques, and then make a prediction of where it is more hopeful to find a "good" solution, such that the algorithms can accommodate the changes in advance. This is one of the reasons the prediction-based approaches can substantially improve performance of an algorithm handling the DMOPs. As expected, it will be a promising approach to enhance the performance of the dynamic estimation distribution algorithms by combining the EDA algorithms with a machine learning technology [19].

However, traditional machine learning methods are often based on an assumption that the samples used to build the model, and the samples to be tested by the model follow the same distribution, which is the so-called Independent Identically Distributed (IID) hypothesis. Under dynamic environments, this hypothesis is very difficult to be satisfied, so that is one of the major reasons why the existing prediction-based methods leave much room to be desired when the training samples and the predicted samples fail to meet the IID hypothesis. In many cases, a poor prediction model can improve nothing but causes more trouble to the host algorithm.

Transfer learning techniques [30] allows the distribution of data used in training and testing to be different and it is becoming a useful weapon to overcome this difficulty. So a combination of transfer learning with DMOP algorithm will be promising since that historical information about the Pareto-optimal Front (POF) or Pareto-optimal Set (POS) is very useful. The reason is that for a DMOP, the POSs or POFs at different times are correlated, but not exactly the same.

Unfortunately at the same time, this combination also causes some problems. One of the problems is that the samples are clustered in the latent space created by the transfer learning method [29], which leads to a poor diversity in the solutions of the corresponding multi-objective optimization problem.

In this paper, a Domain Adaptation and Nonparametric Estimation based EDA, called DANE-EDA, is proposed to solve dynamic multi-objective optimization problems. The motivation of the proposed algorithm comes in two main parts. In one hand, we want to preserve merits of the estimation distribution algorithms and the transfer leaning [17], which means DANE-EDA predicts the changing Pareto front via reusing past "knowledge". On the other hand, we strive to overcome the shortcomings caused by transfer learning, i.e., the loss of diversity in solutions by means of nonparametric statistic and importance sampling methods.

The main contribution of the proposed EDA rests on that the importance sampling, nonparametric density estimation, and domain adaptation are unified seamlessly under an innovative framework to solve dynamic multi-objective optimization problems. More specifically, this algorithm assigns each individual (solution) a sparseness value obtained by a domain adaptation method and a nonparametric probabilistic density estimation method, and then filters offspring out by using an importance sampling. The design takes full advantage of the powerful Monte-Carlo method and transfer learning technique, and this kind of combination will help the proposed algorithm to maintain a delicate exploration-exploitation trade-off from temporal and spatial perspectives. At the same time, it will help the proposed algorithm to overcome the shortcomings caused by transfer learning, i.e., the loss of the diversity.

We hope this process achieves the exploration-exploitation balance in both time and spatial dimensions, and two techniques are used to achieve this goal. At first, we use the domain adaptation approach to reuse knowledge at different points in time. On the other hand, we adapt an important sampling method, such that we can generate and select can-

didate solutions at different points in space, and that is the reason we say that the proposed method wants to keep the exploration-exploitation tradeoff from temporal and spatial perspectives at the same time during searching the POF.

The rest of this paper is organized as follows. In Section 2, we briefly introduce background and review related studies. Then we provide a detailed description of the proposed method and theoretical analysis in Sections 3 and Section 4. In Section 5 we describe evaluation standards, test instances and comparative methods. In Section 6, the experimental results and some discussions are presented. In the Section 7, we sum up the main work of this research and future research direction is also highlighted.

# 2. Preliminaries and related works 

### 2.1. Concepts of multi-objective optimization

In this research, dynamic multi-objective optimization problems are considered, that is, their objective functions will change over time. Formally, a dynamic multi-objective optimization problem is defined as:

$$
\begin{aligned}
& \text { Minimize } F(x, t)=<f_{1}(x, t), f_{2}(x, t), \ldots, f_{M}(x, t)> \\
& \text { s.t. } x \in \Omega
\end{aligned}
$$

where $x=<x_{1}, x_{2}, \ldots, x_{n}>$ is the decision vector and $t$ is the time or environment variable. $f_{i}(x, t): \Omega \rightarrow$ $\mathbb{R}(i=1, \ldots, M), \Omega=\left[L_{1}, U_{1}\right] \times\left[L_{2}, U_{2}\right] \times \cdots \times\left[L_{n}, U_{n}\right] . L_{i}, U_{i} \in \mathbb{R}$ are the lower and upper bounds of the ith decision variable, respectively.

Definition 1 (Dynamic Decision Vector Domination). At time $t$, a decision vector $x_{1}$ Pareto dominate another vector $x_{2}$, denoted by $x_{1}>_{t} x_{2}$, if and only if:

$$
\left\{\begin{array}{ll}
\forall i=1, \ldots, M, & f_{i}\left(x_{1}, t\right) \leq f_{i}\left(x_{2}, t\right) \\
\exists i=1, \ldots, M, & f_{i}\left(x_{1}, t\right)<f_{i}\left(x_{2}, t\right)
\end{array}\right.
$$

Definition 2 (Dynamic Pareto-optimal Set). Both $x$ and $x^{*}$ are decision vectors, and a decision vector $x^{*}$ is said to be nondominated at time $t$ if and only if there is no other decision vector $x$ such that $x>_{t} x^{*}$ at time $t$. The Dynamic Pareto-Optimal Set (DPOS) is the set of all Pareto optimal solutions at time $t$, that is:

$$
D P O S=\left\{x^{*} \mid \exists x, x>_{t} x^{*}\right\}
$$

Definition 3 (Dynamic Pareto-optimal Front). At time $t$, the Dynamic Pareto-Optimal Front (DPOF) is the corresponding objective vectors of the DPOS.

$$
D P O F=\left\{F\left(x^{*}, t\right) \mid x^{*} \in D P O S\right\}
$$

Remark 1. If time factor has not been considered, the DPOS and DPOF will be degenerated to Pareto-optimal Set (POS) and Pareto-optimal Front (POF), respectively.

Please note that in the remainder of this paper, we will not intentionally make a clear distinction between DPOS and POS.

### 2.2. Estimation of Distribution Algorithms

The main feature of EDAs [23] is that they incorporate probabilistic modeling into the evolutionary framework for optimization. Instead of individual-based evolution strategy, EDAs use a population-based strategy to evolve the whole population and explore the search space through building and sampling probabilistic models of promising candidate solutions.

Compared to traditional Evolutionary Algorithms (EAs), EDAs possess some unique advantages: 1) they provide explicit probabilistic models, so these models can be analyzed mathematically; 2) a prior knowledge can be incorporated into the models in a more principled way; 3) instead of managing a population through variations, reducing memory requirement in EDAs is highly expected.

Various EDA algorithms have been developed and there are significant differences among them. However, a majority of these designs would generally involve the following two steps:

1. Firstly, a probabilistic model is built for modeling the solution space, usually through the process of population evaluating, candidate selection, and statistical machine learning. This step is called asModel Building.
2. Based on the constructed model, some kind of sampling method is used to generate a new population. We call this step as Sampling.

# 2.3. Related works 

In recent years, DMOPs have drawn lots of attention from researchers [3] in the optimization field, and most existing algorithms can be roughly classified into the following categories: Increasing/Maintaining Diversity methods, Multi-population based methods, Memory based methods, and Prediction based methods.

The increasing diversity methods tend to add variety to the population by using a certain type of methodology when the environment change was detected. For example, Cobb et al. proposed the triggered hypermutation method [8], and the basic idea of this method is that when change is identified, the mutation rate would be increased immediately, and this would make the converged population divergent again. This approach leaves some room for improvements, and one of them is that the mutation rate is in a state of uncontrolled change during the whole process, and this ultimately results in reduced performance of the algorithm. Therefore, Vavak et al. [40] presented a mutation operator, called variable local search (VLS), to address the problem.

The strategy that the VLS adopted was to gradually increase the mutation rate. Yen et al. [42] proposed a dynamic EA which relocates the individuals based on their change in function value due to the change in the environment and the average sensitivities of their decision variables to the corresponding change in the objective space. This approach can avoid the drawbacks of previous methods to a certain extent.

Maintaining diversity is also one of the effective means which can help the algorithm track the changing optimum as soon as possible. Dynamic NSGA-II (DNSGA-II) [11], proposed by Deb et al., handles the DMOPs by introducing diversity when change is detected. There are two versions of the proposed DNSGA-II and they are respectively known as DNSGA-II-A and DNSGA-II-B. In the DNSGA-II-A, the population is replaced by some individuals with new randomly created solutions, while in the DNSGA-II-B, diversity was guarded by replacing a percentage of the population with mutated solutions.

Grefenstette [13] proposed a Random Immigrants Genetic Algorithm (RIGA) also shares a similar idea, and the method replaces some individuals in the population randomly. The idea of the RIGA is that introducing new genetic materials into the population can avoid the whole population converging toward a small area in the process of evolution. However, the drawback of the primitive immigrant method was the fitness values of the introduced individuals were usually low, so large amounts were eliminated during the selection stage, and as a result, it was very difficult to introduce different genes into the population.

Memory mechanism enables EAs to record past information, and when they detect changes have occurred, stored information can be reused to improve the performance of the algorithm. Existing research showed that memory-based approaches tend to be more effective on the DMOPs with periodically changing environments. Branke [5] proposed a direct memory scheme where the best individuals in the population will be saved in an archive, and when the algorithm detects a change, those saved individuals can be retrieved and returned to the population to replace the same number of individuals.

On this basis, the different approaches were presented. In [12], the authors proposed a co-evolutionary multiobjective algorithm which hybridizes competitive and cooperative mechanisms to solve the DMOPs. In this algorithm, the out-of-date archived solutions are replaced by an external population. In [41], the authors presented an algorithm called MS-MOEA to tackle the challenges of DMOPs. In the method, adaptive genetic and differential operators were used to speed up the convergence speed and a Gaussian local search operator was employed to prevent from premature convergence.

The above methods meet some problems when the environment changes. As a result the authors in [2] proposed an adaptive hybrid population management strategy using memory, local search and random strategies to effectively handle environment dynamicity in DMOPs. The special feature of this algorithm is that it can adjust the number of memory and random solutions to be used according to the change severity. In [18], the authors proposed a method called Steady-state and Generational Evolutionary Algorithm (SGEA), and SGEA detects and reacts to changes in a steady state manner. When a change is detected, SGEA reuses a portion of old solutions with good diversity and re-evaluates them.

The Multi-population strategy is considered as one efficient solution for the DMOPs, especially for the multiple peaks and the competing peaks problems. Branke et al. [7] proposed the self-organizing scouts method, and this method splits the population into scout and base populations, and the two populations are responsible for exploitation and exploration respectively. In other words, the base population searches for the optimal solution and if the base population finds a peak, then the scout population is generated to track the change of this new peak.

Li and Yang [25] used a multi-population particle swarm optimization (PSO) algorithm to solve multiple peaks problems. In their method, a population uses evolutionary programming, which shows a better global search ability when compared to other EAs, to explore the most hopeful areas in the whole search space, and at the same time, several subpopulations use the fast PSO algorithm to find the local optima. Yang [43] used the hierarchical clustering technique to divide the population into different subpopulations, and the main advantage of this design is that the initial individuals of the subpopulations can be generated automatically according to the fitness landscape.

A good dynamic optimization algorithm must be able to track the changing optimal solution even under high severity and frequency changes. One of the ways is to reuse information from previous generations to speedup the optimization search. So, the prediction-based DMOPs algorithms have drawn lots of attention. Stroud [39] proposed the Kalman-extended Genetic Algorithm (KGA), and the basic idea of the KGA was that two types of uncertainties surrounded the estimated value of an individual in a dynamical environment. The first type of uncertainty is produced by the dynamic of the environment while the second type was related to the evaluation of individuals. For the different situations, the KGA has two different

ways to update the covariances, and uses the Kalman filter technique to predict the two uncertainties which allows the algorithm to work well in a dynamic environment.

Bosman [4] considered that a decision made at one point would affect the optima obtained in the future, so for the dynamic optimization problems, he proposed an algorithmical framework which integrated machine learning, statistical learning, and evolutionary computation, and this framework can effectively predict what the state of environment is going to be. In [34], the authors suggested that the state of an optimum should contain the location and the speed information, so the Kalman filter technique can be used to estimate the state of the system and the error. The authors proposed an EA to measure the state of the past optimum and then use the Kalman filter to obtain an estimated value of the optimum in the next time instance.

In [46], Zhou et al. presented an algorithm, called Population Prediction Strategy (PPS), to predict a whole population instead of predicting some isolated points. There are two key concepts in the research: center point and manifold. Whenever a change is detected, the algorithm uses a sequence of center points obtained from the search progress to predict the next center point, and at the same time, the previous manifolds are used to estimate the next manifold. The main problem of this method is that, it is difficult to obtain historical information at the beginning stage, and this may lead to poor convergence.

In [28], the authors proposed a dynamic multiobjective evolutionary algorithm, MOEA\D-KF, which used a Kalman filter (KF) to predict the moving optima in the decision space. The novelty of the approach is that a scoring scheme is designed to hybridize the KF prediction with a random reinitialization method. The predictions help to guide the search toward the changed optima, thereby accelerating convergence.

In [49], the authors proposed a prediction strategy based on center points and knee points (CKPS) consisting of three mechanisms for solving dynamic multiobjective optimization problems. The first mechanism is a method of predicting the non-dominated set based on the forward-looking center points, and the second one is to introduce the knee point set to predict accurately the location and distribution of the Pareto front after an environmental change. Finally, an adaptive diversity maintenance strategy was proposed for generating some random individuals of the corresponding number according to the degree of difficulty of the problem to maintain the diversity of the population. In [1], the authors proposed a continuous genetic algorithm to solve the second-order boundary value problems where smooth solution curves are used throughout the evolution of the algorithm.

In [26], a modified co-evolutionary multi-swarm particle swarm optimizer is proposed to solve dynamic multi-objective optimization problem. In the proposed framework, the number of swarms (PSO) is determined by the number of the objective functions, and all of these swarms utilize an information sharing strategy to evolve cooperatively. At the same time, the authors developed a velocity update rule and an effective boundary constraint technique during evolution of each swarm. Finally, a similarity detection operator is used to detect whether a change has occurred, followed by a memory based dynamic mechanism to response to the change.

The EDA field yields remarkable results and we just review the researches related to our work. Briefly speaking, estimation of distribution algorithms are stochastic optimization techniques which explore the space of potential solutions via probabilistic models of candidate solutions. MBN-EDA, in short for Multi-dimensional Bayesian Network based Estimation of Distribution Algorithm, proposed by Karshenas [19] builds a joint model, multidimensional Bayesian network of variables and objectives. Both the variables and the objectives are encoded in this model. MBN-EDA not only captures the dependencies between variables, but also between objectives and variables. Gaussian Bayesian networks and regularization techniques are employed in MBN-EDA to obtain a more robust estimation and a sparse structure.

It is well known that the Pareto set of a continuous MOPs is a piecewise continuous $m-1$ dimensional manifold. Based on this property, Zhang et al. proposed a Regularity Model-based Multi-objective Estimation of Distribution Algorithm, RMMEDA [44], which uses local Principal Component Analysis (PCA) to build a model in $m-1$ dimensional manifold, where $m$ is the number of objectives. In this algorithm, the population is partitioned into several disjoint clusters using local PCA and the manifold is estimated upon these. However, the RM-MEDA does not use the location information of individuals and may easily fail in the problems with many local Pareto fronts.

Non-parametric probabilistic models also have received great interest among the researchers. For example, MultiObjective Parzen-based EDA (MOPEDA) [10] applies a Parzen estimator, a non-parametric method, to approximate the probability density of solutions on the Pareto front. In this approach, a mixture of uni-modal kernel functions is learned by Parzen estimator, and both Gaussian and Cauchy distributions are adopted alternatively during evolution.

In some situations, it is very difficult to judge whether a solution is an optimal solution or not. However, it is relatively easy to discern a dominated solution from those who are not. Generating-filtering strategy offers effective assistance to respond to the situations. The basic idea behinds the strategy is when the impossible options are removed, the difficulty of solution-finding becomes far easier. The EDAs based on this strategy [47] usually emphasize the cooperation between population generating and population filtering, and avoid building a model explicitly or using a predefined model, so in this sense an algorithm based on the Generating-filtering strategy will have advantage over traditional EDAs.

However, the generating-filtering strategy alone remains very difficult to solve the dynamic multi-objective optimization problems effectively. The reason is that the dynamic multi-objective optimization problem not only needs to search in a large solution space, but also because the optimization objectives are changing constantly. The proposed DANE-EDA not only works with the generating-filtering strategy [47], it also combines the nonparametric density estimation and the importance sampling together, such that DANE-EDA can assume the advantages from both Monte-Carlo methods and nonparametric statistical methods.

It is worth noting that some EDA-based methods are also promising for solving DMOPs. For example, we proposed an EDA [15] which constructs a probabilistic model to predict the trend of the best solutions, so as to promote the search speed for finding the POF. In this approach, one of the purposes is to achieve the diversity of population from the spatial point of view. The research can be regarded as the initial point of the work presented here. The trend prediction model is taken as the static part of the proposed algorithm, and that is to say the probabilistic model is used to generate new offspring. However, there are significant differences between the two approaches. At first, we use rigorous mathematical arguments to improve probabilistic models presented in [15], thus we can carry on property analysis for the proposed algorithm. What is more, the EDA-based prediction method is combined with a transfer learning method, such that the proposed method can remain both the advantages of EDA method and transfer learning approach, and the experimental results show that this combination provides significant performance gains for solving different benchmark functions.

It is obvious that transfer learning techniques will benefit the DMOP algorithms greatly since for a DMOP, the POSs or POFs at different times are correlated, but they are not be exactly the same. Therefore a prediction model built by a transfer learning method will be much better than the prediction model which is created by traditional machine learning methods. However, in another respect, we found that transfer learning, especially for the domain adaptation, often lead to the diminishing diversity in solutions. The proposed approach, DANE-EDA, not only can benefit from the advantages of transfer learning, but also overcome the disadvantages caused by the transfer learning.

# 3. The DANE-EDA 

In the beginning of this section, the framework of DANE-EDA is depicted, and after that three components of the proposed algorithm are introduced in detail: nonparametric density estimation based importance sampling, the probabilistic inertial prediction model, and transfer learning based initial population generation.

### 3.1. The algorithm framework

A formal definition of a hyper-solution is as follows:
Definition 4. For an optimization problem with $M$ objective functions, a hyper-solution is a tuple $P=\langle x, d\rangle$, where $x$ is an $n$-dim vector representing the solution of the multiobjective optimization problem and $d$ is an $n$-dim unit vector representing the direction of the hyper-solution.

The direction $d$ of the hyper-solution can be used to update the probabilistic inertial prediction model, which will be described in Section 3.3, and this model will produce more good offspring which can approach the POF more quickly.

The proposed algorithm, the DANE-EDA, can be divided into two parts: the static part and the dynamic part. Figs. 1 and 2 are used to illustrate the two parts respectively. Please note that the DANE-EDA never stops since we assume that the dynamic optimization problem is constantly running in need of solutions.

Those operations in static part are time independent, and it can be regarded as one iteration when time is fixed. This part involves the following steps: At first, DANE-EDA generates some hyper-solutions (the black points in the Fig. 1(a)), and then it calculates the Non-dominated set ${ }^{1}$ (the red points in the Fig. 1(b)). In the subsequent step, the DANE-EDA estimates the probability density of the distribution which corresponds to the Non-dominated set via a nonparametric kernel density estimation method, and then the proposed algorithm will select one hyper-solution by using important sampling (the Fig. 1(c)), and the principle is that the hyper-solution with high sparseness value can get more chances to be selected and vice versa. After this step, the DANE-EDA will feed the selected hyper-solution into the proposed prediction model to generate some new hyper-solutions (the black points in the Fig. 1(d)), and the next step will get updated Non-dominated set (Fig. 1(e)) according to the hyper-solutions. The program will loop continuously until the termination condition is satisfied.

At the next clock step, the environment will change and the objective functions will be different. At this moment, the DANE-EDA will use a technique, Transfer leaning based Initial Population Generator (Tr-IPG for short), to produce an initial population to search for the POS under the new environment. Fig. 2 illustrates the key ideas of this part. The upper-left is a distribution which the solutions at time $t$ obey, and upper-right is a distribution that the solutions at time $t+1$ follow. These two distributions come from the same optimization function, although the optimization functions will change over time, that is to say they are not exactly the same, but there is a correlation between the two distributions due to the existence of the common parts of the function at different moment. The Tr-IPG procedure can be used to map two distributions into a latent space, such that the two distributions are as similar as possible. Thus the POS obtained at the time $t$ can be used to construct a population to search for the POS of the optimization function at the time $t+1$.

What we want to point out is that one of the major procedures of the static part is to help the dynamic part to overcome the problem caused by transfer learning - the diminishing diversity in the solutions.

[^0]
[^0]:    ${ }^{1}$ Non-dominated set is also called Pareto Set (PS), and the non-dominated front is denoted by PF in this paper.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The static part of DANE-EDA. (a) To generate some solutions randomly. (b) To calculate the non-dominated set (c) To select an individual from the non-dominated set via important sampling. (d) To generate some new hyper-solutions around the individual just selected by using the probabilistic inertial model (e) To update the Pareto set and the Pareto front. (For interpretation of the references to color in the text, the reader is referred to the web version of this article.)
![img-1.jpeg](img-1.jpeg)

Fig. 2. The dynamic part of DANE-EDA. This part maps the distributions at $t$ (the upper-left) and $t+1$ (the upper-right) into a latent space, in which the two distributions will be as similar as possible.

# 3.2. Nonparametric density estimation based importance sampling 

The primary function of Nonparametric Estimation based Importance Sampling (NEIS) is to filter out "the less important hyper-solutions" with higher probability, such that the remaining hyper-solutions can be used to generate the offspring. During the filtering procedure, the principle we followed is "maintaining diversity" from temporal and spatial perspectives.

The basic idea of our method is to assign an importance weight, called sparseness, to every hyper-solution in the nondominated set, and the weight can be considered as a probability value and it will change over time. The hyper-solutions with higher sparseness values will have a better chance of producing more offspring than the hyper-solutions with lower sparseness values.

In this research we employ kernel density estimation to calculate the sparseness value, and its definition is as follows:
Given a set of hyper-solutions $D P=\left\{p_{1}, \ldots, p_{n}\right\}$, where $p_{i}=<x_{i}, d_{i}>\ldots(1 \leq i \leq n)$ is a hyper-solution. The probability density of a hyper-solution $p_{k}$ is calculated by kernel density estimation, that is:

$$
\operatorname{Density}\left(p_{k}\right)=\frac{1}{n h} \sum_{i=1}^{n} \kappa\left(\frac{x_{k}-x_{i}}{h}\right)
$$

where $\kappa(\cdot$.$) is a kernel function [36], and Gaussian kernel function is used in this research. The parameter h$ adjusts the bandwidth of the probabilistic density curve. In other words, the probability density curve will be smooth when $h$ is large, and conversely the curve is steep if the parameter is small.

The probability density describes the degree of congestion, which means if the value of the probability density is high, there are more hyper-solutions within this area; if the value is low, there are fewer hyper-solutions around. Sparseness of a hyper-solution is defined with the probability density.

Remark 2. Unlike the other algorithms, we change the parameter $h$ dynamically, which means in the initial phase, this parameter is set to a large value and it decreases with the progressive of time. Just like we point it out above, the probability density curve is smooth when the value of $h$ is large, and the smooth curve means the difference of density value between different hyper-solutions is quite small, so in the next sampling step, every hyper-solution has an almost-same chance to be selected. Later, when $h$ is set to a small value, and a small part of individuals will have a bigger probability to be chosen, and that is to say, the space for sampling is in the constant change. This is one of the reasons we said that we want to keep the exploration-exploitation tradeoff from the perspectives of spatial and time.

Definition 5. The sparseness of the hyper-solution $p_{k}$ is defined by the reciprocal of the probability density:

$$
\operatorname{Sparseness}\left(p_{k}\right)=\frac{1}{\operatorname{Density}\left(p_{k}\right)}
$$

We would like to make a few remarks here. EDAs generally believe that the Pareto-optimal set follows a certain type of distribution, and some researchers believe that the generating-filter strategy can find this distribution out more effectively than the building-sampling strategy [14]. At the same time, the exploration-exploitation tradeoff strategy has been proven to be an element of solving multi-objective optimization problems, and our idea is to generate more offspring in those areas with lower probability density values to implement the strategy.

More importantly, Importance Sampling is one of the most fundamental techniques for the Monte-Carlo algorithms, and it will help us to overcome a shortcoming caused by the transfer learning technique - the diminishing diversity in the solutions.

We assign each hyper-solution an importance weight, sparseness, to control the probability density of the offspring it can produce. Those hyper-solutions with higher weights have higher probabilities of producing more offspring. It is assumed that each hyper-solution is randomly selected, i.e., $x_{i}$ follows a uniform distribution $U\left(x_{i}\right)=1 / n$, so let

$$
s\left(x_{i}\right)=\operatorname{Pr}\left(x_{i} \text { is selected }\right)=\frac{\operatorname{sparseness}\left(x_{i}\right)}{\sum_{k} \operatorname{sparseness}\left(x_{k}\right)}
$$

be the importance distribution. The probability of the number of the offspring produced by the hyper-solution $x_{i}$ is proportional to $s\left(x_{i}\right)$. According to this analysis, an importance sampling approach based on nonparametric density estimation is designed, and the Procedure NEIS details the approach.

### 3.3. Probabilistic inertial prediction model

After choosing a hyper-solution, we need an effective means to produce more good offspring. A probabilistic inertial prediction model is presented in this section to achieve the goal. The input of this model is the individual selected by the method described in the above subsection and the output of this model is a set of hyper-solutions. Based on this model, a multi-objective optimization algorithm is proposed.

It consists of two parts to produce an offspring: (i) the distance between the offspring and its parents and (ii) the direction of the hyper-solution. In our method, how to determine the distance is relatively simple, a value $\lambda$ is sampled from a normal distribution directly, i.e., $\lambda \sim N\left(0, h \cdot r^{n}\right)$, where $h$ is the initial bandwidth in Eq. (2), $r$ is the attenuation coefficient

Procedure: NEIS $(P)$.
Input: $P$ : a set of hyper-solutions;
Output: a hyper-solution;
1 for each individual $p_{i}$ in $P$ do
2 | Calculate Sparseness $\left(p_{i}\right)$ by Formula (3);
3 end
4 Construct the probabilistic distribution $s$ by Formula (4);
s Sample an individual $p_{k}$ from distribution $s$;
5 return $p_{k}$
![img-2.jpeg](img-2.jpeg)

Fig. 3. Example of Sampling in Inertial Distribution. The angle between $u$ and $v_{1}$ is smaller than the angle between $v_{2}$ and $u$. The angle between $u$ and $u_{3}$ is the largest.
and $n$ is the number of iterations. Please note that this distance is gradually decreased. We do this because we believe that it echoes the concept of the exploration-exploitation tradeoff. In the beginning, the searching area is large, and then the search quality can be improved gradually over time.

For the problem of how to decide the direction of the offspring hyper-solution, a special distribution is proposed, called Probabilistic Inertial Distribution (PID), to solve it. Before describing our method in detail, the definition of the probability inertia distribution is given at first.

Definition 6 (Probabilistic Inertial Distribution, PID). Given a vector $u \in \mathbb{R}^{n}$, the probabilistic inertial distribution measures the probability of the angle $\theta$ between the sampled vector $v$ and $u$ :

$$
\operatorname{PID}_{u}^{\mathrm{n}, \mathrm{P}}(\theta)=\frac{e^{-\alpha \theta}}{\int_{0}^{\pi} e^{-\alpha \theta} \mathrm{d} \theta}, \quad \theta \in[0, \pi]
$$

where $a \in \mathbb{R}^{+}$. $u$ is called the inertial vector.
Remark 3. Please note that there is an infinite number of vectors whose angle to u is $\theta$ (the cone in Fig. 3), and we will present an algorithm to select a vector $v$ from them. The function of parameter $a$ is to control the steepness of the curve.

The purpose of PID is to sample a new vector $v$ according to $u$. By definition, the probability will decrease when $\theta$ increases. Notice that if $a \rightarrow 0$, the PID distribution converges to a uniform distribution, that is:

$$
\lim _{a \rightarrow 0} \operatorname{PID}_{u}^{\mathrm{n}, \mathrm{P}}(\theta)=\operatorname{Uniform}([0, \pi])
$$

Example 1. As shown in Fig. 3, $u$ is the inertial vector and three new vectors $v_{1}, v_{2}$ and $v_{3}$ are sampled from a given PID distribution according to $u$. The probability that $v_{1}$ is selected is higher than that of $v_{2}$ since the angle between $u$ and $v_{1}$ is smaller than the angle between $v_{2}$ and $u$. Obviously, the probability that $v_{3}$ is selected is the smallest among the three vectors.

Definition 7 (Standard Inertial Distribution). The distribution $\lim _{a \rightarrow 0} \operatorname{PID}_{u}^{\mathrm{n}, \mathrm{P}}(\theta)$ is called the standard inertial distribution $P_{0}$.

The process of generating offspring is searching for optimal solutions, and this process has time-varying characteristics. In other words, in the beginning of the search, we often want to seek solutions over a large area. As time passed by, we need to narrow down our search for getting high-quality solutions. This is known as the exploration-exploitation tradeoff. For achieving the exploration-exploitation balance, we propose a concept called inertial distribution's amplitude.

Definition 8 (Amplitude of Inertial Distribution). The amplitude of an inertial distribution $P$ is the KL divergence between $P$ and $P_{0}$ :

$$
\operatorname{AMP}(P)=\operatorname{KL}\left(P, P_{0}\right)=\int_{0}^{\pi} P(\theta) \log \frac{P(\theta)}{P_{0}(\theta)} \mathrm{d} \theta
$$

The amplitude reflects the steepness of the corresponding inertial distribution's curve. When we perform sampling from a distribution with a large amplitude, the vectors which are closer to the inertial vector will be sampled with a higher probability. In contrast, when we carry out sampling from a distribution with a very small amplitude, it is equivalent to sample from a uniform distribution.

The amplitude can be controlled by the parameter $a$ in the Formula (5). So the process of generating offspring can be separated into two phases: start-up phase and refinement phase. In the start-up phase, the amplitude is large, so the efficiency of the algorithm is high. In the refinement phase, the algorithm searches for a better solution in a smaller area since the amplitude will gradually become smaller.

The Procedure GenOffs to be detailed later describes how to generate offspring. The parameter $N$ is a number of offspring the proposed algorithm wants to generate. The value of the number depends on the computing resource available and the problem at hand. The larger the value, the more resources the algorithm requires, and the higher the precision of the solution. After an angle $\theta$ is sampled from the inertial distribution, we will carry out the Procedure Randpick to pick out a vector from an infinite number of vectors whose angle to $u$ is $\theta$. And then a step length is sampled from a normal distribution. The Procedure PIPM depicts a multi-objective optimization algorithm which is based on the Procedure GenOffs.

```
Procedure: Randpick \((u, \theta)\).
    Input: \(u\) : the inertial vector; \(\theta\) : the angle between \(u\) and the sampled vector;
    Output: The sampled vector;
    \(1 D_{u} \leftarrow\) the dimensionality of \(u\);
    2 First_nonzero \(\leftarrow\) the first index of nonzero element in \(u\);
    3 // Construct a linearly independent vector group containing \(u\)
    4 for \(i=1\) to \(D_{u}-1\) do
        if \(i=\) First_nonzero then
            \(\beta_{i} \leftarrow\) a vector with only its \(D_{u}\) th entry being 1 ;
        else
            \(\beta_{i} \leftarrow\) a vector with only its ith entry being 1 ;
            // Get orthogonal basis R
            Apply Gram-Schmidt process over the matrix \(\left[u, \beta_{1}, \ldots, \beta_{D_{u}-1}\right]\) to obtain the orthogonal basis \(R\);
            // Sample from spherical polar coordinates
            Sample a vector \(v\) from \(D_{u}-1\)-dimensional spherical polar coordinates;
            // Transform the sample back to original coordinate space
        end
    end
    return \(R^{-1} \cdot[\cos (\theta) v]^{\mathrm{T}}\)
```


# 3.4. Transfer learning based initial population generator 

The dynamic multi-objective optimization problem is a computation-intensive task which implies it requires a lot of computational resources to search for the POS at a given time. If the knowledge about the POS can be reused to predict future POFs or POSs under different environments, this usually assures performance improvement as well as less computational resource consumption. As a result, we believe that the prediction-based dynamic multi-objective optimization algorithm presents a promising solution.

However, the existing prediction-based algorithms are built on the basis of Independent Identical Distribution (IID) hypothesis, which means that the solutions of a dynamic optimization problems obey an identical distribution. However, it is obvious that the POSs under different environments could follow the different distributions, and this also means that those dynamic optimization algorithms based on the traditional machine learning approach leave much room for improvement. Along this line of thinking, the use of the transfer learning method to develop a novel dynamic estimation of distribution algorithm is proposed.

```
Procedure: GenOffs(POS, \(a, N\) ).
    Input: POS: A set of hyper-solutions; \(a\) : A control parameter; \(N\) : The number of offspring;
    Output: A set of hyper-solutions;
    1 samples \(\leftarrow \emptyset\);
    for \(i=1\) to \(N\) do
        \(p \leftarrow \operatorname{NEIS}(P O S)\);
        Sample \(\theta\) from the distribution \(P I D_{\theta}\);
        \(v=\) Randpick \((p\).direction, \(\theta)\);
        Sample a length \(\lambda\) from \(\operatorname{Norm}(0,1 / \alpha)\) and normalized it to \([0, \infty]\);
    Add a new hyper-solution \(p+\lambda v\) to samples;
    end
    return samples;
```

Procedure: PIPM $\left(F_{t}(X), \operatorname{Pop}, h, r, N\right)$.
Input: $F_{t}(X)$ : a DMOP at time $t$; Pop: the initialized population; $h$ : the initialized bandwidth; $r$ : the initialized attenuation coefficient; $N$ the number of samplings;
Output: TempPOS: the POS of $F_{t}(X)$;
1 Get $P O S^{0}$ and $P O F^{0}$ by Pop;
2 samples $=$ GenOffs $(P o p .1 / h, N)$;
3 Get POS ${ }^{1}$ and $P O F^{1}$ by samples;
$4 P O F=P O F^{0}$;
5 $P O F^{\prime}=P O F^{1}$;
6 TempPOS $=P O S^{1}$;
7 while $\Delta\left(P O F, P O F^{\prime}\right)>\varepsilon$ do
8 /* The definition of $\Delta$ please refer to Equation (8).
9 samples $=$ GenOffs $\left(\right.$ TempPOS, $1 / h, N)$;
$10 \quad P O F=P O F^{\prime}$;
11 Get TempPOS and $P O F^{\prime}$ by samples;
$12 \quad h=h * r$;
13 end
14 return TempPOS;

Pan et al. proposed a dimension reduction-based method [29] called Transfer Component Analysis (TCA), to find a lowdimensional space to reduce the difference between source and targets distributions as well as to preserve the main statistical properties, maximization of data variance. Procedure TCA is a sketch of the TCA algorithm, and interested readers can refer to [29].

Procedure: TCA $(X, Y, \kappa)$.
Input: $X, Y$ : the training samples of the source and target domains; $\kappa(\cdot, \cdot)$ : the kernel function;
Output: $W$ : a transformation matrix;
1 Construct the Kernel Matrix $\tilde{K}$, the coefficient Matrix $L$, and the centering Matrix $H$;
2 Construct the Matrix $W$ by using the $d$ leading eigenvectors of $(K L K+\mu I)^{-1} K H K$;
3 return the matrix $W$;

In the following Tr-IPG procedure, $F_{t}(\cdot)$ is the current dynamic optimization function assuming its POS has already been found. $F_{t+1}$ is the optimization problem we want to solve at the next time instance. The major part of the algorithm, Tr -IPG, utilizes the POF at the time $t$ and the transfer learning method to generate a population which can be used to facilitate in searching for the POS at the time $t+1$.

More specifically, the obtained Pareto-optimal Front (POF) at the time $t$ is regarded as a source domain; the probable solutions of the next time, the time $t+1$, as the target domain, and then construct a mapping function $\varphi$ by using the domain adaptation approach. This mapping function will embed the distributions that the source and target domains obey separately into a latent space, and in that space the difference in distributions will become as small as possible. From this, the POS already found can be used to generate an initial population which can be used to search for the POS of the next instance.

```
Procedure: \(\operatorname{Tr}-\operatorname{IPG}\left(F_{t+1}, P O F_{t}, \kappa\right)\).
    Input: The Dynamic Optimization Function \(F_{t+1}(\cdot) ; P O F_{t}=\left\{p_{1}, \ldots, p_{m}\right\}\) and it is the POF of the function \(F_{t}(\cdot)\) at the
        time \(t\); a kernel function \(\kappa(\cdot, \cdot)\);
    Output: A population Pop-init;
    1 Initialization;
    2 For the optimization functions \(F_{t}(\cdot)\) and \(F_{t+1}(\cdot)\), randomly generate two sets of the solutions \(X_{k}\) and \(Y_{t} ; \quad / /\) Remark 4
    3 Calculate the objective values of the optimization functions \(F_{t}\left(X_{k}\right)\) and \(F_{t+1}\left(Y_{t}\right)\);
    \(4 W \leftarrow \operatorname{TCA}\left\{\left[F_{t}\left(X_{k}\right)\right],\left\{F_{t+1}\left(Y_{t}\right)\right\}, \kappa\right\}\);
    5 PLS \(\leftarrow \emptyset ; / /\) Remark 5
    6 for every \(p \in \operatorname{POF}_{t}\) do
    \(7 \quad \kappa_{t} \leftarrow\left[\kappa\left(F_{t}\left(p_{1}\right), F_{t}(p)\right), \cdots, \kappa\left(F_{t}\left(p_{m}\right), F_{t}(p)\right)\right]^{T}\);
    \(8 \quad \varphi\left(F_{t}(p)\right) \leftarrow W^{T} \kappa_{t}\);
    \(9 \quad P L S=P L S \cup\left\{\varphi\left(F_{t}(p)\right)\right\}\);
    10 end
    11 for every \(I \in P L S\) do
    \(12 \quad x \leftarrow \operatorname{argmin}_{x}\left\|\varphi\left(F_{t+1}(x)\right)-I\right\| / /\) Remark 6
    13 Pop-init = Pop-init \(\cup\{x\} ;\)
    14 end
    15 return Pop-init;
```

Remark 4. The numbers of the samples in $X_{k}$ and $Y_{t}$ are predefined. In general, more sampling often means a better result, but it also needs to pay a higher computational cost, so the decision about how many samples needed to be produced in this step depends on the resource available.

Remark 5. PLS (in short for POF in the Latent Space) is a set of the mapped solutions in the latent space.
Remark 6. We want to find a decision variable $x$, such that in the latent space, $\varphi\left(F_{t+1}(x)\right)$ is closest to $I \in P L S$ in the latent space. This also means that we need to solve a single objective optimization problem here, and any single objective optimization algorithm can be applied to solve the problem. In this research, the Interior Point Algorithm is used to solve the problem.

What the Tr-IPG algorithm outputs is a population, so it can be used as an initial population to search for the POS of the next instance. Please note that we setup a parameter, called the bandwidth $h$, in our algorithm to control the variances of sampling distributions and the amplitude of PID, and we have discussed the details of the parameter $h$ below Eq. (2). The whole process of DANE-EDA is shown in Algorithm 1.

```
Algorithm 1: DANE-EDA: Domain Adaptation and Nonparametric Estimation based EDA.
    Input: The Dynamic Multi-objective Optimization Function \(F(X) ; N\) : the number of samplings; a kernel function
        \(\kappa(\cdot, \cdot)\);
    Output: \(s\) : the POSs of \(F(X)\) at different times;
    1 Randomly initiate the \(N\) individuals as the \(P o p_{0}\);
    2 Initiate bandwidth \(h\);
    3 Initiate attenuation coefficient \(r\);
    4 \(\operatorname{POS}_{0}=\operatorname{PIPM}\left(F_{0}(X), \operatorname{Pop}_{0}, r, h, N\right)\);
    5 Get \(\operatorname{POF}_{0}\) by \(\operatorname{POS}_{0}\);
    \(6 s=\operatorname{POS}_{0}\);
    7 for \(t=1\) to \(n\) do
        Initiate attenuation coefficient \(r\);
        Next-Pop \(=\operatorname{Tr}-\operatorname{IPG}\left(F_{t}(X), \operatorname{POF}_{t-1}, \kappa(\cdot, \cdot)\right)\);
        \(\operatorname{POS}_{t}=\operatorname{PIPM}\left(F_{t}(X)\right.\), Next-Pop, \(\left.r, h, N\right)\);
        Get \(\operatorname{POF}_{t}\) by \(\operatorname{POS}_{t}\);
        \(s=\operatorname{POSs} \cup \operatorname{POS}_{t}\);
    13 end
    14 return \(s\);
```

# 4. The property analysis for the DANE-EDA algorithm 

In this section, convergence and computational complexity of the proposed algorithm are analyzed.

### 4.1. Convergence analysis

Let's start with the stop condition. We define the following measurement to evaluate the distance of two point sets $P_{1}$ and $P_{2}$ in the objective space:

$$
\Delta\left(P_{1}, P_{2}\right)=\frac{\sum_{p \in P_{1}} \min _{q \in P_{1}}\|p-q\|_{2}+\sum_{p \in P_{2}} \min _{q \in P_{1}}\|p-q\|_{2}}{\left|P_{1}\right|+\left|P_{2}\right|}
$$

$\Delta\left(P_{1}, P_{2}\right)$ can be used to depict the closeness of two Pareto fronts. If $P_{1}$ and $P_{2}$ are identical, then $\Delta\left(P_{1}, P_{2}\right)=0$.
Next, the convergence of DANE-EDA algorithm will be proved . More precisely, we will prove that a sequence of the Pareto Fronts (PFs) computed by the DANE-EDA algorithm is almost sure convergence to a value.
Definition 9. We say that a sequence of $X_{n}$ converges almost surely toward $X$ means that

$$
\operatorname{Pr}\left(\lim _{n \rightarrow \infty} X_{n}=X\right)=1
$$

It is usually denoted by

$$
\lim _{n \rightarrow \infty} X_{n} \xrightarrow{\text { a.s. }} X
$$

Theorem 1. Let $P O F_{n}$ be the Pareto front got by the DANE-EDA algorithm at the nth iteration, then

$$
\lim _{n \rightarrow \infty} \Delta\left(P O F_{n}, P O F_{n+1}\right) \xrightarrow{\text { a.s. }} 0
$$

Proof. For any hyper-solution $p$ generated by the DANE-EDA at the nth iteration, the distance between $p$ and its offspring $p^{\prime}$ satisfies:

$$
\begin{aligned}
& \lim _{n \rightarrow \infty}\left|p^{\prime}-p\right| \\
= & \lim _{n \rightarrow 0}\left|\lambda_{n} u_{n}\right| \\
= & \lim _{n \rightarrow 0}\left|\lambda_{n}\right|
\end{aligned}
$$

where $u_{n}$ is the $n$-iteration's unit direction vector and $\lambda_{n}$ is the corresponding step length.
Since $\lambda_{n} \sim N\left(0, h_{0} r^{n}\right)$, where $h_{0}$ is the initial bandwidth ( $h$ is defined in Eq. (2)) and $r$ is the attenuation coefficient, we have

$$
\mathrm{E}\left|\lambda_{n}\right|^{2}=\mathrm{D} \lambda_{n}=h_{0} r^{n}
$$

where D is variance.
Using Markov's inequality, the following bound can be obtained, for any given positive real number $\varepsilon$,

$$
\operatorname{Pr}\{|\lambda|>\varepsilon\} \leq \frac{\mathrm{E}|\lambda|^{2}}{\varepsilon^{2}}
$$

So

$$
\begin{aligned}
& \sum_{n=1}^{\infty} \operatorname{Pr}\left\{\left|\lambda_{n}\right|>\varepsilon\right\} \\
\leq & \sum_{n=1}^{\infty} \frac{\mathrm{E}|\lambda|^{2}}{\varepsilon^{2}} \\
= & \sum_{n=1}^{\infty} \frac{h_{0}}{\varepsilon^{2}} r^{n}, r \in(0,1) \\
= & \frac{h_{0}}{\varepsilon^{2}(1-r)} \\
< & \infty
\end{aligned}
$$

By the Borel-Cantelli Lemma [21],

$$
\lim _{n \rightarrow \infty}\left|p^{\prime}-p\right| \xrightarrow{\text { a.s. }} 0
$$

Let $d(p, q)$ be a distance ${ }^{2}$ between $p$ and $q$ in the objective space. Now, according to Eq. (9), for every $p \in P O F_{n}$, we have:

$$
0 \leq \lim _{n \rightarrow \infty} \min _{q \in P O F_{n+1}} d(p, q) \leq \lim _{n \rightarrow \infty} d\left(p, p^{\prime}\right) \xrightarrow{\text { a.s. }} 0
$$

similarly, for every $q \in P O F_{n+1}$, we have:

$$
\lim _{n \rightarrow \infty} \min _{p \in P O F_{n}} d(p, q) \xrightarrow{\text { a.s. }} 0
$$

According to Eq. (8), we obtain that:

$$
\lim _{n \rightarrow \infty} \Delta\left(P O F_{n}, P O F_{n+1}\right) \xrightarrow{\text { a.s. }} 0
$$

# 4.2. Computational time analysis 

At first, let us analyze the static part of the proposed algorithm. Suppose there are $m$ objectives, and evaluating each objective costs $O(1)$ time, then evaluating multiple objectives cost $O(m)$ time. In the proposed algorithm, in every iteration, we sample at most $n$ individuals. For each individual, $O(n)$ time is needed to sample it, so the complexity of sampling at each iteration is $O\left(n^{2}\right)$. If $P$ steps are needed to reach the stopping criteria, then the complexity of the static part of the proposed algorithm is $O\left(m n^{2} P\right)$. For the dynamic part of the algorithm, the main computational time is spent on eigenvalue decomposition. It takes $O\left(d\left(n_{1}+n_{2}\right)^{2}\right)$ time when $d$ nonzero eigenvectors are to be extracted, where $n_{1}$ and $n_{2}$ are the numbers of the solutions which are generated to construct the latent space. Overall, DANE-EDA takes $O(n)+O\left(m n^{2} P\right)+$ $O\left(d\left(n_{1}+n_{2}\right)^{2}\right.$ time to solve an $m$-objective dynamic optimization problem for every time change.

## 5. Comparison studies

### 5.1. Comparison algorithms

In this research, we compare the DANE-EDA with some chosen state-of-the-art estimation of distribution algorithms. The EGNA algorithm was proposed in [22], and this EDA is based on structure learning and simulation of Gaussian networks. The MBN-EDA [19] is a multi-objective estimation of distribution algorithm and uses the multi-dimensional Bayesian network as its probabilistic model to capture the dependencies between decision variables and target variables. RM-MEDA [44] is a regularity model-based multi-objective estimation of distribution algorithm which assumes that the Pareto set is a piece-wise continuous $(m-1)$-dimensional ( $m$ is the number of objectives) manifold and applies local principal component analysis algorithm to model such a model.

We also compare the proposed algorithm with other dynamic multi-objective optimization algorithms. A random reinitialization method (RND) [28] is implemented as a baseline. MOEA:D-KF was presented in [28], Dynamic NSGA-II (DNSGA-II) [11], the Population Prediction Strategy (PPS) [46] and Multi-objective Optimization algorithm based on Particle Swarm Optimization (MOPSO) [9].

### 5.2. Performance metric

We use five performance metrics, variants of Inverted Generation Distance (IGD), a modified Inverted Generation Distance (IGD*), Coverage Scope (CS), Reactivity measure (React), and Hypervolume (Hv), tailored specifically for measuring performance of Dynamic Multi-objective Evolutionary Algorithms. These performance metrics have been adopted widely to quantify the performance of Dynamic Multi-objective Evolutionary algorithms.

- The Inverted Generational Distance (IGD) [37] is used to measure the performance of multi-objective optimization algorithms. Let $P^{*}$ be the uniformly distributed true Pareto-optimal front and $P$ be the Pareto front acquired by the algorithm. The IGD value is defined as follows:

$$
\operatorname{IGD}\left(P^{*}, P, C\right)=\frac{\sum_{\left|v^{\prime} \in P^{\prime}\right|} \min _{v \in P}\left\|v^{\prime \prime}-v\right\|}{\left|P^{*}\right|}
$$

A smaller IGD value implies a better performance. Please note that the definition of the IGD is slightly different from the original one, and the major difference is the parameter $C$ in Eq. (11). The parameter $C$ is a combination of the benchmark functions parameters. We call it as configuration of the benchmark functions. The configurations in our experiments are described in Table 1.

[^0]
[^0]:    ${ }^{2}$ In this paper, the Euclidean distance is used as $d(p, q)$.

Table 1
Environment settings.

The MIDG, in short for the Mean value of IGDs, is used to evaluate dynamic multi-objective optimization algorithms, and it takes the average of the IGD values in some time steps over a run as the performance metric, given by

$$
\operatorname{MIGD}\left(P^{\star}, P, C\right)=\frac{1}{|T|} \sum_{t \in T} \operatorname{IGD}\left(P^{\star t}, P^{t}, C\right)
$$

where $P^{\star t}$ and $P^{t}$ represent the points set of the real POF and the POF obtained by the underlying algorithm at the time $t$.
Considering the changing environments a dynamic multi-objective evolutionary algorithm has to perform in, DMIGD, is defined based on MIGD over all considered changing configurations:

$$
\operatorname{DMIGD}\left(P^{\star}, P, C\right)=\frac{1}{|E|} \sum_{C \in E} \operatorname{MIGD}\left(P^{\star t}, P^{t}, C\right)
$$

where $|E|$ is the number of the different environments and in this research the $|E|$ equals eight. What we want to point out is that the DMIGD can evaluate a dynamic optimization algorithm from a high-level view and it has a significant difference with the MIGD since the MIGD just consider the dynamics in one environment.

- Inverted Generational Distance Plus (IGD+) [16]. Since IGD is not Pareto compliant, it is possible that misleading Pareto incompliant results are obtained. IGD+ considers the Pareto dominance relation between a solution and a reference point when their distance is calculated.

$$
d_{\text {IGD+ }}\left(v^{\star}, v\right)=\sqrt{\sum_{k=1}^{m}\left(\max \left\{v_{k}^{\star}-v_{k}, 0\right\}\right)^{2}}
$$

where $m$ is the number of the objects. If the obtained solution $v$ is dominated by the point $v^{\star}$ in the true Pareto-optimal front, $d_{\text {IGD+ }}\left(v^{\star}, v\right)$ is equal to the Euclidean distance between $v^{\star}$ and $v$. Based on this, the definition of IGD+ is given below:

$$
\operatorname{IGD}+\left(P^{\star}, P, C\right)=\frac{\sum_{v^{\star} \in P^{\star}} \min _{v \in P} d_{\text {IGD+ }}\left(v^{\star}, v\right)}{\left|P^{\star}\right|}
$$

$P^{\star}$ is the uniformly distributed true Pareto-optimal front and $P$ is the obtained Pareto front through the algorithm. The parameter $C$ is a combination of the benchmark functions parameters. DMIGD+ has a similar meaning to the DMIGD. A smaller DMIGD+ value implies a better performance.

- Coverage Scope (CS) [45] is used to measure the diversity of solutions. The CS value of $P$ is defined by:

$$
\operatorname{CS}(P)=\frac{1}{|P|} \sum_{i=1}^{|P|} \max \left\{\left\|f\left(x_{i}\right)-f\left(x_{j}\right)\right\|\right\}
$$

where $P$ is the obtained optimal Pareto front. $x_{i}, x_{j} \in P$ with $i \geq 1$ and $j \leq|P|$. This index describes the diversity of the solution set. A larger CS value indicates a better diversity. Its variant, DMCS, has a similar meaning to the DMIGD.

- Reactivity measure (React) [38] is used to measure the robustness of algorithms. The definition is given below:

$$
\operatorname{React}(t)=\min \left\{t^{\prime}-t \mid t<t^{\prime} \in \mathbb{N}, \frac{\operatorname{acc}\left(t^{\prime}\right)}{\operatorname{acc}(t)} \geq 1-\varepsilon\right\}
$$

where $\operatorname{acc}(t)=\frac{\operatorname{Hv}(\text { POF })(1)}{\max \operatorname{Hv}(\text { POF })}$ represents the accuracy of Pareto front at time $t$, and Hv means Hypervolume [48]. This index describes the needed time to recover the Pareto front. Smaller React value indicates better robustness. Its variant, DMReact, has a similar meaning to the DMIGD.

- Hypervolume [48] has been gaining a lot of interest in recent years and it is a set measure reflecting the volume enclosed by a Pareto front approximation. Let $P$ be a non-dominated set and the hypervolume indicator for $P$, denoted as $\operatorname{Hv}(P)$, is

Table 2
Characteristics of the test functions.

dependent upon the reference point $r=\left(r_{1}, r_{2}, \ldots, r_{k}\right)$ and is formalized as

$$
H v(P)=L e b\left(\bigcup_{x \in P}\left[f_{1}(x), r_{1}\right] \times \cdots \times\left[f_{k}(x), r_{k}\right]\right)
$$

where $L e b(P)$ is the Lebesgue measure of the set $P$, and $\left[f_{1}(x), r_{1}\right] \times\left[f_{2}(x), r_{2}\right] \times \cdots \times\left[f_{k}(x), r_{k}\right]$ is the hypercube containing all criterion vectors that are weakly dominated by the elements $x \in P$ and themselves dominate the reference point $r$. The non-dominated set which has a relatively uniform and widely distribution would have a larger corresponding Hypervolume value. DMHv has a similar meaning to the DMIGD.

# 5.3. Test instances and experimental settings 

The IEEE CEC 2015 benchmark problems set was chosen as test functions and the problem set has twelve testing functions. The POFs of the testing functions have different shapes and each function belongs to a certain DMOPs type. Fig. 4 describes the true POFs of the twelve testing functions and we let the functions change three times.

In the definitions, the decision variables are $x=\left(x_{1}, \ldots, x_{n}\right)$ and $t=\frac{1}{n!}\left\lvert\, \frac{\tau_{T}}{N}\right.$, where $n_{t}, \tau_{T}$, and $\tau_{T}$ are the severity of change, maximum number of iterations, and frequency of change respectively. Table 1 describes the different combinations of $n_{t}, \tau_{T}$, and $\tau_{T}$ used in our experiments. Please note that, for each $n_{t}-\tau_{T}$ combination, there will be $\frac{\tau_{T}}{N}$ environment changes. In other words, in all of our experiments, there are altogether five changes for the twelve dynamic problems.

The POFs of the testing functions have different shapes and each function belongs to a certain DMOPs type. For example, the POF of the functions could be non-convex, convex, isolated, deceptive, continuous or discontinuous. Table 2 describes the types of the testing functions. Type I implies POS changes, but POF does not change; Type II means that the POS and the POF change as well; Type III means that the POF changes, but the POS does not change.

FDA4 and FDA5 are 3-objective functions while all of the remaining are 2-objective functions. FDA5 $5_{i o}$ is a Type II DMOP and its POF is isolated and non-convex. Spread of solutions in the POF of this function changes over time. FDA5 dec is also a Type II DMOP but has a deceptive and non-convex POF. DIMP2 is a Type I DMOP and it has a convex POF. dMOP2 is a Type II DMOP and its POF changes from convex to concave, and vice versa. dMOP2 ${ }_{i o}$ is also a Type II DMOP and has an isolated POF. dMOP2 dec has a deceptive POF and its POF changes from convex to concave and vice versa. dMOP3 is a Type I DMOP. It has a convex POF and spread of the POF changes over time. HE7 and HE9 are type III DMOPs and their POS are not dependent on time. HE2 is also a type III DMOP, and it has discontinuous POF, with various disconnected continuous sub-regions.

The dimensions of the decision variables are from 10 to 30 . Please note that the $\mathrm{A}, \mathrm{B}$ and C values for the functions FDA5 $5_{i o}, \mathrm{FDA} 5_{\text {dec }}, \mathrm{dMOP} 2_{\text {iso }}$ and $\mathrm{dMOP} 2_{\text {dec }}$ are set to $\mathrm{G}(\mathrm{t}), 0.001$ and 0.05 respectively.

In all of the experiments, the population size is set to 200 and in each generation every algorithm will generate no more than 200 solutions. For the TCA parameter, we set the Gaussian kernel function as the default and the expected dimensionality was set to be 20. The value of $\mu$ was set to 0.5 . The specific parameter settings follow instructions in the original papers. In EGNA [22], truncation selection is chosen as the selection method. MBN-EDA [19] uses profit gain ordering as ranking method. In RM-MEDA [44], the number of clusters in local PCA algorithm is set to be 5.

Please note that our experimental results are obtained without explicitly tuning the TCA algorithm's parameters one by one, and if we adjust the parameters specifically for different test functions, we have reason to believe that we can obtain better experimental results. The reason that we did not tune the parameters separately for getting better results is that the twelve test functions are not exactly the same, so we can set different parameters to get the best performance for each test function. For example, we can construct different latent spaces for each of the twelve benchmark functions individually via setting different parameters of the TCA method. However, we think that this one-by-one-adjustment strategy does not effectively explain the versatility of the proposed design.

![img-3.jpeg](img-3.jpeg)

Fig. 4. The true POFs of the twelve testing functions.

Table 3
Statistical results of the proposed algorithm, DANE-EDA, and nine chosen competing algorithms in term of DMIGD performance metric.

Table 4
Statistical results of the proposed algorithm, DANE-EDA, and nine chosen competing algorithms in term of DMIGD+ performance metric.

Table 5
Statistical results of the proposed algorithm, DANE-EDA, and nine chosen competing algorithms in term of DMCS performance metric.

# 6. Results and discussion 

### 6.1. Comparison results

For each benchmark functions, eight different $n_{f}-r_{f}$ combinations listed in Table 1 are tested and the different performance metrics are calculated. Owing to space limitation, we just report DMIGD, DMCS, DMReact and DMHv values in Tables 3-7. These values are obtained by averaging different changes and then averaging over different configurations. In Tables 3, 4, 5, 6 and 7, bold face implies the underlying results are the best among all competing algorithms.

Table 3 records the DMIGD values of the algorithms running on different testing functions under different configurations. For the twelve test functions, the DANE-EDA achieves the best results in FDA5 ${ }_{\text {iter }}$, FDA5 ${ }_{\text {dec }}$, DIMP2, HE7 and HE9, at the same time, for the other four benchmark functions, FDA4, FDA5, dMop2 ${ }_{\text {iter }}$ and HE2, the performance of the proposed algorithm is very near that of the best algorithm. The experiments show that the proposed algorithm is competitive at handling the Types II and III DMOPs or the problems that its POF changes over time since these test functions belong in these types.

We think that the reason why DANE-EDA has advantages in dealing with POF-changing optimization problems is largely due to the transfer learning-based initial population generation method. In other words, our method establishes a link between the POF at the time $t$ and the POF at the time $t+1$, and the experiments prove that our idea, the transfer learning

Table 6
Statistical results of the proposed algorithm, DANE-EDA, and nine chosen competing algorithms in term of DMReact performance metric.

Table 7
Statistical results of the proposed algorithm, DANE-EDA, and nine chosen competing algorithms in term of DMHv performance metric.

plus estimation of distribution algorithm, can effectively improve the performance of handling dynamic multi-objective optimization problems.

The performance quantified according to DMCS is given in Table 5. In four cases, dMOP2, dMOP2 $2_{\text {dec }}$, HE7 and HE9, the performance of the DANE-EDA is the best among all competing algorithms, and MOPSO and MOEA\&D-KF each win the three other test functions.

According to the definitions, we know that dMOP2 is a type II DMOP and its time-varying POS is sinusoidal in nature. dMOP2 $2_{\text {list }}$ and dMOP2 $2_{\text {dec }}$ consist of isolated and deceptive POF respectively, and we have mentioned HE2, HE7 and HE9 above. By observing the common characteristics of these functions, we believe that the reason why DANE-EDA has better performance over these functions according to DMCS metric is that the nonparametric density estimation based importance sampling method has played a role, especially the integration of the sampling method and the transfer learning is particularly applicable to the Type II or Type III dynamic multi-objective optimization problems.

In addition, as shown in Table 5, we can find that DANE-EDA is not tailored specifically for DMOPs with isolated POF. This may be because the isolated POFs are usually flat and DANE-EDA cannot move fast and cover the whole POF since the bandwidth parameter is decreasing over time.

Table 6 gives out the DMReact performance for each method. The value is also averaged over time and changes. As we described in its definition, the value depicts the time needed for an algorithm to recover the Pareto front as environment has changed, and it is an index for robustness of an algorithm. The DANE-EDA achieves the best results in FDA4, HE7 and HE9, while comes near the top performers in FDA5, dMOP2 $2_{\text {dec }}$ and HE2 testing functions.

The statistical values of DMHv for DANE-EDA in comparison with other nine algorithms are presented in Table 7. These data indicate that the DANE-EDA performs the best in five benchmark functions, and at the same time, for the HE2, dMOP3, and FDA5 $5_{\text {list }}$ functions, there is little difference in performance between the proposed algorithm and the best ones. This result indicates that the diversity of solutions can be improved by combining importance sampling with transfer learning. We can see that in almost all cases the DANE-EDA algorithm have achieved relatively good results.

Our views on this issue are as follows. In one respect, probabilistic inertia model can help to obtain more heuristic information from environment and speed up the updating process of searching for Pareto front, leading to better performance (smaller DMIGD value). Meanwhile, the step width and sampling angle of the model will reduce robustness of the algorithm in some sense since it would need some time to adjust the parameters when environment changes.

# 7. Conclusion 

In this article, a novel estimation distribution algorithm, DANE-EDA, is proposed for solving dynamic multi-objective optimization problems. The uniqueness of the proposed algorithm is that it makes an attempt at unifying importance sampling, nonparametric density estimation, probabilistic prediction mechanism and domain adaptation technique under one framework, so that it can take the advantage of Monte-Carlo method and transfer learning technologies.

The merits of this seamless integration are reflected in two aspects. First, the transfer learning based initial population generation method can make the algorithm reuse the knowledge gained, such that the efficiency of the dynamic multiobjective optimization algorithm is improved. Secondly, transfer learning will inadvertently deteriorate the diversity in solutions, and we suspect that this is due to the latent space mapping. However, the non-parametric probability density estimation based importance sampling can overcome this problem as well as preserve the exploration-exploitation tradeoff in some degree.

After presenting a detailed description of the algorithm, the convergence and analysis of the computational complexity of the proposed algorithm are proved. In the experimental part, the IEEE CEC 2015 benchmark problems set is taken as test functions and the problem set has twelve testing functions. The proposed algorithm and the other nine state-of-theart algorithms have been evaluated by five performance metrics. The experimental results show that the convergence and diversity of the proposed algorithm is promising, but at the same time, we also find that the robustness and computational speed of the algorithm remain a critical issue to be improved. However, we believe this line of research proposed herein inspires further innovations in solving real-world application with various degrees of complexities and uncertainties.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (No. 61673328). The first author also wants to thank China Scholarship Council (No. 20150631505) and Oklahoma State University for providing funding and facilities to support his research as a visiting scholar.
