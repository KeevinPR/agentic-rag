# Transfer Learning based Dynamic Multiobjective Optimization Algorithms 

Min JIANG, Senior Member, IEEE, Zhongqiang HUANG, Liming QIU, Wenzhen HUANG, and Gary G. YEN, Fellow, IEEE


#### Abstract

One of the major distinguishing features of the Dynamic Multiobjective Optimization Problems (DMOPs) is that optimization objectives will change over time, thus tracking the varying Pareto-Optimal Front (POF) becomes a challenge. One of the promising solutions is reusing "experiences" to construct a prediction model via statistical machine learning approaches. However, most existing methods neglect the non-independent and identically distributed nature of data to construct the prediction model. In this paper, we propose an algorithmic framework, called Tr-DMOEA, which integrates transfer learning and population-based evolutionary algorithms (EAs) to solve the DMOPs. This approach exploits the transfer learning technique as a tool to generate an effective initial population pool via reusing past experience to speed up the evolutionary process, and at the same time any population based multiobjective algorithms can benefit from this integration without any extensive modifications. To verify this idea, we incorporate the proposed approach into the development of three well-known evolutionary algorithms, nondominated sorting genetic algorithm II (NSGAII), multiojective particle swarm optimization (MOPSO), and the regularity model-based multiobjective estimation of distribution algorithm (RM-MEDA). We employ twelve benchmark functions to test these algorithms as well as compare them with some chosen state-of-the-art designs. The experimental results confirm the effectiveness of the proposed design for DMOPs.


Index Terms-Dynamic multiobjective optimization, Domain adaption, Dimensionality reduction, Transfer learning, Evolutionary Algorithm.

## I. INTRODUCTION

One of the essential characteristics of Dynamic Multiobjective Optimization Problems (DMOPs) [1] is that objective functions will vary over time or under different environments. This underlying problem characteristic bears significant implications for real-world applications [2]. A good example is dynamic portfolio optimization problem, which is common in deregulated electricity markets in which the operations of different power stations are controlled and coordinated to maximize profit while minimizing risk. There are various uncertainties in a deregulated electricity market, including spot market prices, load obligations, and strip/option prices [3].
M. JIANG, L. QIU are with the Department of Cognitive Science and Technology and Fujian Key Lab. of Machine Intelligence and Robotics, Xiamen University, China, Fujian, 361005. M. JIANG is also a visiting scholar at Oklahoma State University. Z. HUANG is working for SUNGFOR technolgies company, Shenzhen, China and W. HUANG is currently a master student with the Institute of Automation of the Chinese Academy of Sciences, Beijing, China. E-mail: minjiang@xmu.edu.cn.
G. YEN is with the School of Electrical and Computer Engineering, Oklahoma State University. G. YEN is the corresponding author and E-mail: gyen@okstate.edu.

Manuscript received Nov 14, 2016; revised XXXX, XX, 201X.

The values for some of these factors change over time, and it is ordinary to optimize for the market price every hour. However, the optimization approaches including populationbased metaheuristics often find extreme difficulty to address the challenge since that the POF of a DMOP may change when the environment changes. Solving the DMOPs efficiently and effectively has become an important research issue in evolutionary computation community [4, 5].

In recent years, a great deal of progress has been made and different types of algorithms have been proposed. In all of these methods, one class of approaches, the prediction based, has gained much attention. This class of approaches allows evolutionary algorithm (EA) and machine learning to be seamlessly integrated. After deriving a prediction model via machine learning techniques, the EAs can sustain the needed performance even if the environment changes over time. For example, in [6], the authors proposed a memory-based EA which introduced two kinds of prediction models. The first one used the linear/nonlinear regression model to predict when the environment would change while the second model was based on Markov chains which was used to forecast changes. In [7], the authors suggested integrating motion information into an EA, such that the algorithm can track a time-changing optimum. In [8], the authors proposed a Kalman-extended genetic algorithm, and this algorithm was developed to determine when to re-evaluate an existing individual, when to produce a new individual, and which individual to re-evaluate.

The basic idea of these methods is "keeping track of good (partial) solutions in order to reuse them under periodically changing environment" [7]. If we consider this view from a statistical point of view, this idea implies that the solutions of a dynamic optimization problem obey an identical distribution. In other words, the solutions which are used to construct the prediction model and the solutions forecasted by the prediction model meet the Independent Identical Distribution (IID) hypothesis to some extent. This assumption undoubtedly simplifies the complexity of the problem, however we have to understand there is an appreciable difference between the good, but out-of-date solutions and the proper and newly generated solutions, especially under a dynamic environment. That is to say, the changing POF may lead to the different distributions of the training samples and the predicted samples, and this problem is very difficult for the traditional machine learning methods.

The findings from machine leaning community [9] already showed that a prediction model built by traditional machine learning methods leaves much room to be desired when the

training samples and the predicted samples fail to meet the IID hypothesis. Transfer learning [9] allows the distribution of data used in training and testing to be different and it is becoming a useful weapon to overcome this difficulty. Therefore, the dynamic multiobjective optimization algorithms based on traditional machine learning methods, especially the prediction based algorithms, can also have significant performance improvements by overcoming the limitation caused by the IID, and transfer learning approach is a powerful tool we can use to improve performance of EAs for DMOPs.

In this paper, we argue that integrating transfer leaning approaches [9] into an EA can offer significant benefits to performance and robustness for designing better Dynamic Multiobjective Evolutionary Algorithms (DMOEAs). We adopt a domain adaptation method ${ }^{1}$, called transfer component analysis [10], to construct a prediction model. This model uses the gained knowledge of finding Pareto optimal solutions, but not the population, to generate an initial population pool for the optimization function at the next time. Based on this initial population pool, the optima of the changed environment can be found more efficiently and effectively. The proposed domain adaptation learning approach can be easily incorporated into any evolutionary-based multiobjective optimization algorithms. Please note that in this research, the dynamic refers to that objective functions will vary over time or under different environments.

Indeed, how to detect and identify dynamic changes is a crucial part of solving dynamic multiobjective optimization problems. However, in this paper, our focus is placed solely on how EA can quickly re-optimize a given dynamic optimization problem once the change is been detected and identified. This is in a similar spirit as those studies in fault tolerant control where focus is placed exclusively on designing a controller capable of accommodating the dynamic changes, leaving the fault detection and identification to be addressed separately.

The contribution of this research is the integration between transfer learning and classical evolutionary multiobjective optimization algorithms. This combination provides two benefits. First, the advantages of the EAs are preserved in the improved design for DMOPs. Secondly, the proposed design can significantly improve the search efficiency via reusing past experience which is critical for solving the DMOPs. An algorithm requires too much computing resources, often making it difficult to solve large-scale problems. The experiments also validate the assumption that the population plays a very important role for tracking dynamic optima, and [11, 12] proves it from the theoretical point of view.

The rest of this paper is organized as follows: In Section II, we will introduce some basic concepts of dynamic optimization problems first and then discuss the existing works in this field. At the beginning of Section III, we will present some background on transfer learning, domain adaptation learning, and then introduce the transfer component analysis method in detail. After that we will propose the Transfer learning based Dynamic Multi-Objective Evolutionary optimization Algorithm, Tr-DMOEA. In Section IV, we will

[^0]present the experimental results of incorporating our approach to improve three well-known MOEAs: NSGA-II, MOPSO and RM-MEDA, specifically for DMOPs and all of the algorithms were tested on the IEEE CEC 2015 benchmark problems set. In Section V, we will draw a summary of this paper and outline the future research directions.

## II. Preliminary Studies and Related Research

## A. Dynamic Multi-objective Optimization

Formally, a dynamic multiobjective optimization problem is defined as:

$$
\begin{aligned}
\text { Minimize } F(x, t)= & \left\langle f_{1}(x, t), f_{2}(x, t), \ldots, f_{M}(x, t)\right\rangle \\
& \text { s.t. } x \in \Omega
\end{aligned}
$$

where $x=\left\langle x_{1}, x_{2}, \ldots, x_{n}\right\rangle$ is the decision vector and $t$ is the time or environment variable. $f_{i}(x, t): \Omega \rightarrow$ $\mathbb{R}(i=1, \ldots, M), \Omega=\left[L_{1}, U_{1}\right] \times\left[L_{2}, U_{2}\right] \times \cdots \times\left[L_{n}, U_{n}\right]$. $L_{i}, U_{i} \in \mathbb{R}$ are the lower and upper bounds of the $i$-th decision variable, respectively. Please note that dynamic environments can be classified in different ways. For an in-depth description, the readers are referred to [6].
Definition 1. [Dynamic Decision Vector Domination] At time $t$, a decision vector $x_{1}$ Pareto dominate another vector $x_{2}$, denoted by $x_{1} \succ_{t} x_{2}$, if and only if:

$$
\left\{\begin{array}{l}
\forall i=1, \ldots, M, \quad f_{i}\left(x_{1}, t\right) \leq f_{i}\left(x_{2}, t\right) \\
\exists i=1, \ldots, M, \quad f_{i}\left(x_{1}, t\right)<f_{i}\left(x_{2}, t\right)
\end{array}\right.
$$

Definition 2. [ Dynamic Pareto-optimal Set ] Both $x$ and $x^{*}$ are decision vectors, and if a decision vector $x^{*}$ is said to be nondominated at time $t$ if and only if there is no other decision vector $x$ such that $x \succ_{t} x^{*}$ at time $t$. The Dynamic Pareto-Optimal Set (DPOS) is the set of all Pareto optimal solutions at time $t$, that is:

$$
D P O S=\left\{x^{*} \mid \nexists x, x \succ_{t} x^{*}\right\}
$$

Definition 3. [Dynamic Pareto-optimal Front] At time $t$, the Dynamic Pareto-Optimal Front (DPOF) is the corresponding objective vectors of the DPOS.

$$
D P O F=\left\{F\left(x^{*}, t\right) \mid x^{*} \in D P O S\right\}
$$

For an ideal dynamic multiobjective algorithm, it must be able to find a set of solutions as close as possible to the changing Pareto-optimal Front and at the same time, the set of solutions should be as diverse as possible.

## B. Related Works

Much progress [4, 13, 14, 15] has been made in the DMOPs field in recent years, and most existing algorithms can be classified into the following categories: Increasing/Maintaining Diversity methods, Memory based methods, Multi-population based methods, and Prediction based methods.

The increasing diversity methods tend to add variety to the population by using a certain type of methodology when the environment change was detected. For example, Cobb et al. proposed the triggered hypermutation method [16], and the


[^0]:    ${ }^{1}$ a branch of transfer learning.

basic idea of this method is that when change is identified, the mutation rate would be increased immediately, and this would make the converged population divergent again. This approach calls for some improvements, and one of them is that the mutation rate is in a state of uncontrolled change during the whole process, and this ultimately results in reduced performance of the algorithm. Therefore, Vavak et al. [17] presented a mutation operator, called variable local search (VLS), to address the problem. The strategy that the VLS adopted was to gradually increase the mutation rate. Yen et al. [18] proposed a dynamic EA which relocates the individuals based on their change in function value due to the change in the environment and the average sensitivities of their decision variables to the corresponding change in the objective space. This approach can avoid the drawbacks of previous methods to a certain extent.

Most of the methods in the maintaining diversity category assume that avoiding population convergence can help the algorithm track the changing optimum as soon as possible, and maintain diversity as one of the effective means to that end. Grefenstette [19] proposed a Random Immigrants Genetic Algorithm (RIGA), and the method replaces some individuals in the population randomly. The idea of the RIGA is that introducing new genetic materials into the population can avoid the whole population converging toward a small area in the process of evolution. However, the drawback of the primitive immigrant method was the fitness values of the introduced individuals were usually low, so large amounts are eliminated during the selection stage, and as a result, it is very difficult to introduce different genes into the population. For solving this problem, Yang [20, 21] proposed the hybrid immigrants scheme, memory-based immigrants [22] and elitismbased immigrants [22], and these methods are effective for dealing with periodically changing DMOPs. However, if the knowledge about the dynamic environment is limited, they would obtain a greatly reduced efficiency.

Dynamic NSGA-II (DNSGA-II) [23] proposed by Deb et al. also shares a similar idea, and this method handles the DMOPs by introducing diversity when change is detected. There are two versions of the proposed DNSGA-II and they are respectively known as DNSGA-II-A and DNSGA-II-B. In the DNSGA-II-A, the population is replaced by some individuals with new randomly created solutions, while in the DNSGA-II-B, diversity was guarded by replacing a percentage of the population with mutated solutions.

Memory mechanism enables EAs to record past information, and when it detects changes have occurred, stored information can be reused to improve the performance of the algorithm. Existing research showed that memory-based approaches tend to be more effective on the DMOPs with periodically changing environments.

Branke [24] proposed a direct memory scheme where the best individuals in the population will be saved in an archive, and when the algorithm detects a change, those saved individuals can be retrieved and returned to the population to replace the same number of individuals. In [25], the author proposed a co-evolutionary multiobjective algorithm which hybridizes competitive and cooperative mechanisms to
solve the DMOPs. In this algorithm, the out-of-date archived solutions are replaced by an external population. In [26], the authors presented an algorithm called MS-MOEA to tackle the challenges of DMOPs. In the method, adaptive genetic and differential operators were used to speed up the convergence speed and a Gaussian local search operator was employed to prevent from premature convergence. At the same time the fast hyper-volume strategy [27] was proposed to achieve a better starting population when changes occur frequently. The above methods meet some problems, e.g. slow convergence and poor diversity, when the environment changes. As a result the authors in [28] proposed an adaptive hybrid population management strategy using memory, local search and random strategies to effectively handle environment dynamicity in DMOPs. The special feature of this algorithm is that it can adjust the number of memory and random solutions to be used according to the change severity.

The Multi-population strategy is considered as one efficient solution for the DMOPs, especially for the multiple peaks and the competing peaks problems. Branke et al. [29] proposed the self-organizing scouts method, and this method splits the population into scout and base populations, and the two populations are responsible for exploitation and exploration respectively. In other words, the base population searches for the optimal solution and if the base population finds a peak, then the scout population is generated to track the change of this new peak. Li and Yang [30] employed a multi-population particle swarm optimization (PSO) algorithm to solve multiple peaks problems. In their method, a population uses evolutionary programming, which shows a better global search ability when compared to other EAs, to explore the most hopeful areas in the whole search space, and at the same time, several subpopulations use the fast PSO algorithm to find the local optima. Yang [31] used hierarchical clustering technique to divide the population into different subpopulations, and the main advantage of this design is that the initial individuals of the subpopulations can be generated automatically according to the fitness landscape.

In general, a good dynamic optimization algorithm should be able to track the changing optimal solution even under high severity and frequency of changes. It must be able to reuse as much information available from previous generations to speedup the optimization search. As a result, in recent years the prediction-based DMOPs algorithms have received much attention. This class of methods predicts the state of the changing environment typically using the information that already exists and some forms of machine learning techniques, and then makes a decision such that the algorithms can accommodate the changes in advance. This is one of the reasons why the prediction-based approaches can improve performance of an algorithm handling the DMOPs, compared with other types of approaches.

Bosman [32] believed that the decision made at one point would affect the optima obtained in the future, so for the dynamic optimization problems, he proposed an algorithmical framework which integrated machine learning, statistic learning, and evolutionary computation, and this framework can effectively predict what the state of environment is going to

be. In [7], the authors suggested that the state of an optimum should contain the location and the speed information, so the Kalman filter technique can be used to estimate the state of the system and the error. The authors proposed an EA to measure the state of the past optimum and then use the Kalman filter to obtain an estimated value of the optimum in the next time instance.

Stroud [8] proposed the Kalman-extended Genetic Algorithm (KGA), and the basic idea of the KGA was that two types of uncertainties surrounded the estimated value of an individual in a dynamical environment. The first type of uncertainty is produced by the dynamic of the environment while the second type was related to the evaluation of individuals. For the different situations, the KGA has two different ways to update the covariances, and uses the Kalman filter technique to predict the two uncertainties which allows the algorithm to work well in a dynamic environment.

In [33], Zhou et al. presented an algorithm, called Population Prediction Strategy (PPS), to predict a whole population instead of predicting some isolated points. There are two key concepts here: center point and manifold. Whenever a change is detected, the algorithm uses a sequence of center points obtained from the search progress to predict the next center point, and at the same time, the previous manifolds are used to estimate the next manifold. The main problem of this method is that, it is difficult to obtain historical information at the beginning stage, and this may lead to poor convergence.

Recently, there are some works exploiting knowledge reuse techniques or machine learning in evolutionary computation that have been proposed. In [34], the authors propose an approach based on transfer learning and genetic programming to solve complex image classification problems. The basic idea of the proposed algorithm is that the knowledge learned from a simpler subtask is used to solve a more complex subtask, and reusing knowledge blocks are discovered from similar as well as different image classification tasks during the evolutionary process. In [35], the authors present a genetic programminglike representation to identify building blocks of knowledge in a learning classifier system, and the proposed method can extract useful building blocks from simpler and smaller problems and reuse them to learn more complex multiplexer problem. In [36], the authors present an evolutionary memetic computing paradigm that is capable of learning and evolving knowledge meme that traverses two different but related problem domains, capacitated vehicle routing problem and capacitated arc routing problem, for greater search efficiency. Experimental results show that evolutionary optimization can benefit from this approach.

However, we are not exactly sure if the data we using to construct the prediction model and the data we are going to predict by the above model obey a similar distribution. Conversely, the real-world applications repeatedly reminded us that, it is not wise to assume the IID hypothesis as a prerequisite, especially for the DMOPs. Unfortunately, most of the existing methods often assume that the solutions at different times have an IID structure, and we believe that this assumption is one of main reasons for the failure of existing DMOEA algorithms. After all, a poor prediction model is very
likely to bring the search process to a hopeless place, which means actual results will be worse than a method which does not use predictive technique, if the prediction model turn out to be inaccurate.

We believe that historical information about the POF or POS is very useful, and the reason is that for a DMOP, the POSs or POFs at different times may not be exactly the same, but they must be correlated. Therefore we conjecture that an appropriate use of the information extracted from the obtained POS or POF will bring great benefits to track the changing POF, but at the same time, we must admit the rationality and the generality of the assumption of nonindependently and identically distributed data. From these basic points of view, we propose a framework which integrates transfer learning and EAs for solving the DMOPs. Two of the major advantages of the proposed approach are as follows: at first, the proposed method does not assume IID hypothesis as a prerequisite, and it is enabled to escape serious consequences of an unsuitable model. Secondly, this approach is designed to generate a population-building prediction model, so that any population-based optimization algorithms may benefit from this integration without any extensive modification.

## III. TRANSFER LEARNING BASED DYNAMIC MULTI-OBJECTIVE OPTIMIZATION ALGORITHM

In this section, we propose a transfer learning based dynamic optimization algorithm. Our motivation is that the solutions of a dynamic optimization problem under different environments obey different probability distributions, and these distributions are not identical but are correlated. If we can map these different distributions into a latent space, and in this space the distributions are as "similar" as possible, then we can use the available solutions to generate an initial population, such that the solutions under a new environment can be computed with low computational cost. In principle, this design is a reuse process of the knowledge we already obtained.

Before giving the details of the proposed approach, we need to introduce background information of the domain adaptation learning we will use it in our design.

## A. Transfer Component Analysis

Briefly speaking, Domain Adaptation Learning (DAL) [37, 38, 39], a branch of transfer learning, is to reuse the knowledge acquired from a source domain to perform a task in a target domain, which is related to, but distinct from the source domain. In the context of this research, a domain includes a sample space $\mathcal{X}$ and the corresponding marginal distribution $P(X)$, where $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\} \subseteq \mathcal{X}$. We say that two domains are different, which means they have different sample spaces and the marginal distributions are different.

The researchers [40] believe that it is a promising solution using the DAL to find a good representation to decrease the difference between the distributions of source and target domains. Gretton et al. [41] noted that the distance between two different distributions can be evaluated by a particular function, and in the Reproducing Kernel Hilbert Space (RKHS),

the computational cost of the evaluation can be reduced. Based on this observation, Gretton et al. [41, 42] proposed a nonparametric distance estimation method called Maximum Mean Discrepancy (MMD) to differentiate distributions in the RKHS [43]. The MMD measures the discrepancy between two distributions by computing the difference of the mean values for the source domain and target domain. The advantages of the MMD approach is its simplicity and accuracy.
Definition 4. (Maximum Mean Discrepancy [41]): Let $p$ and $q$ be two Borel probability measures defined on a domain $\mathcal{X}$; and $X=\left\{x_{1}, \cdots, x_{m}\right\}$ and $Y=\left\{y_{1}, \cdots, y_{n}\right\}$ be two observations drawn from $p$ and $q$ respectively. Let $\mathcal{F}$ be a class of functions $f: \mathcal{X} \rightarrow \mathbb{R}$, then the maximum mean discrepancy (MMD) can be defined as:

$$
\operatorname{MMD}(\mathcal{F}, p, q):=\sup _{f \in \mathcal{F}}\left(\frac{1}{m} \sum_{i=1}^{m} f\left(x_{i}\right)-\frac{1}{n} \sum_{i=1}^{n} f\left(y_{i}\right)\right)
$$

In a Reproducing Kernel Hilbert Space, $f$ can be written as $f(x)=\langle\phi(x), f\rangle$, where $\phi(x): \mathcal{X} \rightarrow \mathcal{H}$. So the empirical estimate of MMD can be rewritten as:

$$
\operatorname{MMD}(\mathcal{F}, p, q):=\left\|\frac{1}{m} \sum_{i=1}^{m} \phi\left(x_{i}\right)-\frac{1}{n} \sum_{i=1}^{n} \phi\left(y_{i}\right)\right\|_{\mathcal{H}}^{2}
$$

By using the so-called "kernel trick"[44], we can rewrite Equation (2) as

$$
\begin{aligned}
& \operatorname{MMD}(\mathcal{F}, p, q):=\sum_{i=1}^{m} \sum_{j=1}^{n} \operatorname{tr}\left[\hat{K}\left(\frac{1}{m \times m} L_{i i}-\frac{1}{m \times n} L_{i j}\right.\right. \\
& \left.\left.-\frac{1}{n \times m} L_{j i}+\frac{1}{n \times n} L_{j j}\right)\right] \\
& :=\operatorname{tr}(\hat{K} L),
\end{aligned}
$$

where $\operatorname{tr}(A)$ refers to the trace of the matrix $A$, and the matrix

$$
\hat{K}=\left(\begin{array}{cc}
\hat{K}_{X, X} & \hat{K}_{X, Y} \\
\hat{K}_{Y, X} & \hat{K}_{Y, Y}
\end{array}\right) \in \mathbb{R}^{(m+n) \times(m+n)}
$$

$\hat{K}_{X, Y}$ is a kernel matrix with $k_{i, j}=\kappa\left(x_{i}, y_{j}\right)=\phi\left(x_{i}\right)^{T} \phi\left(y_{j}\right)$, where $\kappa(\cdot, \cdot)$ is a kernel function and $\phi(\cdot)$ is a feature mapping function. This matrix reflects data similarity in the domains $X$ and $Y . \hat{K}_{X, X}, \hat{K}_{Y, X}$ and $\hat{K}_{Y, Y}$ have the similar meanings. Matrix $L$ contains the coefficients to scale matrix according to Equation (2) and its elements are as follows.

$$
L(i, j)=\left\{\begin{array}{cc}
\frac{1}{m \times m}, & x_{i}, x_{j} \in X \\
\frac{1}{n \times n}, & x_{i}, x_{j} \in Y \\
-\frac{1}{m \times n}, & \text { otherwise }
\end{array} .\right.
$$

On the basis of the MMD, Pan et al. proposed a dimension reduction method [10] called Maximum Mean Discrepancy Embedding (MMDE) to (1) find a low-dimensional space to reduce the difference between source and targets distributions as well as (2) to preserve the main statistical properties, maximization of data variance in the first extracted orthogonal components of the original data $X$ and $Y$. In MMDE, the kernel function $\kappa$ is learned (or optimized) from the data,
which makes it computationally expensive, so the authors in [10] proposed other dimension reduction-based methods called Transfer Component Analysis (TCA) and its Semi-Supervised version of TCA, SSTCA, to transform the problem of learning an entire kernel matrix to a low-rank matrix $W$ instead.

Now let us consider how to obtain the martix $W$ by using the TCA method. Suppose that $W$ is a $(m+n) \times d$ matrix. For any vector $x$, let $\phi(x)=W^{T} \kappa_{x} \in \mathbb{R}^{d}$, where $\phi(\cdot)$ is a feature mapping function. Let $\kappa_{x}=$ $\left[\kappa\left(x_{1}, x\right), \ldots, \kappa\left(x_{m}, x\right), \kappa\left(y_{1}, x\right), \ldots, \kappa\left(y_{n}, x\right)\right]^{T}$, and the matrix $\hat{K}$ in Equation (4) can be transformed as follows.

$$
\begin{aligned}
\hat{K}= & {\left[\phi\left(x_{1}\right), \ldots, \phi\left(x_{m}\right), \phi\left(y_{1}\right), \ldots, \phi\left(y_{n}\right)\right]^{T} \times } \\
& {\left[\phi\left(x_{1}\right), \ldots, \phi\left(x_{m}\right), \phi\left(y_{1}\right), \ldots, \phi\left(y_{n}\right)\right] } \\
= & {\left[W^{T} \kappa_{x_{1}}, \ldots, W^{T} \kappa_{x_{m}}, W^{T} \kappa_{y_{1}}, \ldots, W^{T} \kappa_{y_{n}}\right]^{T} \times } \\
& {\left[W^{T} \kappa_{x_{1}}, \ldots, W^{T} \kappa_{x_{m}}, W^{T} \kappa_{y_{1}}, \ldots, W^{T} \kappa_{y_{n}}\right] } \\
= & {\left[\kappa_{x_{1}}, \ldots, \kappa_{x_{m}}, \kappa_{y_{1}}, \ldots, \kappa_{y_{n}}\right]^{T} W W^{T} } \\
& {\left[\kappa_{x_{1}}, \ldots, \kappa_{x_{m}}, \kappa_{y_{1}}, \ldots, \kappa_{y_{n}}\right] } \\
= & K^{T} W W^{T} K \\
= & K W W^{T} K
\end{aligned}
$$

Please note that the matrix $K$ is a symmetric matrix, so $K^{T}=K$, and then $\operatorname{tr}(\hat{K} L)=\operatorname{tr}\left(K W W^{T} K L\right)$. According to the property of the trace of a matrix, we can rewrite Equation (3) as follows.

$$
\begin{aligned}
\operatorname{MMD}(\mathcal{F}, p, q) & =\operatorname{tr}(\hat{K} L) \\
& =\operatorname{tr}\left(K W W^{T} K L\right) \\
& =\operatorname{tr}\left(W^{T} K L K W\right)
\end{aligned}
$$

Now the optimization problem for the TCA algorithm can be written as follows:

$$
\begin{array}{ll}
\underset{W}{\operatorname{argmin}} & \mu \cdot \operatorname{tr}\left(W^{T} W\right)+\operatorname{tr}\left(W^{T} K L K W\right) \\
\text { subject to } & W^{T} K H K W=\mathbf{I}
\end{array}
$$

where $H=\mathbf{I}-\frac{1}{m+n} \mathbf{1} \mathbf{1}^{T}$ and $\mathbf{I}$ is a $(m+n) \times(m+n)$ identity matrix. $W^{T} W$ is a regularization term. $\mathbf{1}$ is a $(m+n) \times 1$ all-ones matrix. $m$ and $n$ represent the numbers of samples in the source and target domains, respectively. $\mu$ is the tradeoff parameter. This optimization problem can be transformed into a trace maximization problem. According to the method presented in [45], the trace maximization problem can be solved by the Generalized Eigenvalue Decomposition (GED), and the solution is composed of the $d$ leading eigenvectors. The pseudo-code of TCA is given in Algorithm 1.

## B. Tr-DMOEA

Dynamic multiobjective optimization problem is a computationally expensive task. This implies that it requires a lot of computational resources to search for the varying POS at a certain time. If the knowledge about the POS and POF can be reused to predict future POFs or POSs under different environments, this usually implies performance improvement as well as less computational resource consumption. As a result,

## Algorithm 1: TCA

Input: Source domain $X$; target domain $Y$; a kernel function $\kappa(\cdot, \cdot)$;
Output: Matrix $W$
1 Construct the Kernel Matrix $\tilde{K}$, the Matrix $L$, and the Matrix $H$ according to (4), (5) and (8) ;
2 Construct the Matrix $W$ by using the $d$ leading eigenvectors of $(K L K+\mu I)^{-1} K H K$;
3 return the matrix $W$;
we believe that the prediction-based dynamic multiobjective optimization algorithm presents a promising solution.

However, the existing algorithms generally neglect the assumption of Non-Independent Identically Distributed (NonIID), and it is obvious that the individuals under different environments obey different distributions. This also means that those dynamic optimization algorithms based on the traditional machine learning approach leave much room for improvement. So we put forward the use of the domain adaptation technique to develop a novel DMOEA.

The approach developed is to map different distributions that the solutions obey at different times into a new latent space via the domain adaptation method. In the latent space, the MMD value of different distributions will be as small as possible while variance of the data will be kept the same. In other words, we will make those distributions that the solutions under different environments obey as similar as possible in the latent space, so we can map the POF we have obtained into the space, and then use those mapped solutions to construct a population which will be used to search for the POF under a new environment.

In the following Tr-DMOEA algorithm, $F_{t}$ is the current dynamic optimization function assuming its POF has already been found. $F_{t+1}$ is the optimization function at the next time. The major part of the algorithm, Tr-IPG, utilizes the POF at time $t$ and the transfer learning method to generate a population which can be used to search for the POF at time $t+1$. More specifically, we take the obtained Paretooptimal Front (POF) at time $t$ as a source domain; the feasible solutions of the next time, time $t+1$, as the target domain, and then construct a mapping function $\varphi$ by using the domain adaptation approach. This mapping function will embed the distributions that the source and target domain obey separately into a latent space, and in that space the difference between the two distributions will become as small as possible. From this, we can use the POF already found to generate an initial population which can be used to search for the POF of the next moment.

In order to help the readers quickly grasp the basic idea of the algorithm Tr-IPG, Figure 1 has been presented to illustrate the key elements of the algorithm. This diagram describes the operational process from Line 6 to Line 15 of the Tr-IPG.

Please note that the input to the TCA are the samples from the solutions at time $t$ and $t+1$, and its output is a transformation matrix $W$. We can use the matrix $W$ to construct the latent space. The Step 1 (i.e., the upper left

Algorithm 2: Tr-IPG: Transfer Learning based Initial Population Generator
Input: The Dynamic Optimization Function $F_{t+1}(\cdot)$; the POF of the function $F_{t}(\cdot)$ at time $t, P O F_{t}=$ $\left\{p_{1}, \ldots p_{m}\right\}$; a kernel function $\kappa(\cdot, \cdot)$.
Output: A population Pop-init.
1 Initialization;
2 For the optimization functions $F_{t}(\cdot)$ and $F_{t+1}(\cdot)$, randomly generate two sets of the solutions $X_{s}$ and $Y_{t}$;

$$
/ * \text { Remark } 1 \text { */ }
$$

3 Calculate the objective values of the optimization functions $F_{t}\left(X_{s}\right)$ and $F_{t+1}\left(Y_{t}\right)$
$4 \mathrm{~W} \leftarrow \operatorname{TCA}\left(\left\{F_{t}\left(X_{s}\right)\right\},\left\{F_{t+1}\left(Y_{t}\right)\right\}, \kappa\right)$
$5 P L S \leftarrow \emptyset ; / *$ Remark 2
6 for every $p \in P O F_{t}$ do
$7 \quad \kappa_{p} \leftarrow\left[\kappa\left(F_{t}\left(X_{s}(1)\right), p\right), \ldots, \kappa\left(F_{t+1}\left(Y_{t}\left(n_{t}\right)\right), p\right)\right]^{T}$
$8 \varphi(p) \leftarrow W^{T} \kappa_{p}$
$9 \quad P L S=P L S \cup\{\varphi(p)\}$
10 end
11 for every $l \in P L S$ do
$12 \quad x \leftarrow \operatorname{argmin}\left\|\varphi\left(F_{t+1}(x)\right)-l\right\| / *$ Remark $3 \quad * /$
13 Pop-init $=$ Pop-init $\cup\{x\}$;
14 end
15 return Pop-init ;
corner of the diagram) depicts the process of mapping the POF at time $t$ into the latent space, and the Steps 2 and 3 describe how to search for an initial population which can be used to solve the dynamic optimization at time $t+1$.

Remark 1. The numbers of the elements of $X_{s}$ and $Y_{t}$ are predefined. Let $\left|X_{s}\right|=n_{s}$ and $\left|Y_{t}\right|=n_{t}$. In general, more sampling often means a better result, but it also needs to pay a higher computational cost, so the decision about how many solutions needed to be produced in this step depends on the resources available.

Remark 2. $P L S$ is the acronym of Particle in the Latent Space and it can be regared as a set of the mapped solutions in the latent space.

Remark 3. We want to find a decision variable $x$, such that in the latent space, $\varphi\left(F_{t+1}(x)\right)$ is closet to $l \in P L S$ in the latent space. This also means that we need to solve a single objective optimization problem here, and any single objective optimization algorithm can be applied to solve the problem. In this research, we use the Interior Point Algorithm to solve the problem.

What the Tr-IPG algorithm outputs is a population, so it is not difficult to find that we can combine any type of population-based optimization algorithms with the Tr-IPG to obtain a transfer learning based dynamic multiobjective EA.

Remark 4. For the TCA algorithm, the major time is spent on eigenvalue decomposition. It takes $O\left(d\left(m_{1}+m_{2}\right)^{2}\right)$ time when $d$ nonzero eigenvectors are to be extracted, where $m_{1}$ and $m_{2}$ are the numbers of the solutions which are generated

![img-0.jpeg](img-0.jpeg)

Figure 1: The key steps of the Tr-IPG algorithm. Step 1: Map the obtained POF into the latent space; Step 2: Find individuals for $F_{t+1}(\cdot)$; Step 3: Generate initial population pool for the problem $F_{t+1}(\cdot)$.
to construct the latent space. The Tr-IPG spends $O\left(n_{1}\right)$ time to map an individuals in the $P O F_{t}$ to the latent space and we use the Interior Point Algorithm to find an indidvidual in the objective space of $F_{t+1}(\cdot)$. For the primal dual interior point method, suppose the constraint matrix $A$ has $n$ rows and $m$ columns, and $n<m$, it has $O(\sqrt{m} L)$ iterations and $O\left(m^{3} L\right)$ arithmetic operations, where $L$ is total number of bits of the input.

Example 1. A specific numerical example is helpful in understanding how the Tr-IPG algorithm works. For example, we employ the Tr-IPG algorithm to solve the FDA4 problem, which is a three-objective dynamic optimization problem. Let us suppose that the POF of the FDA4 problem [46] at time $t, P O F_{t}$, has been found and $p \in P O F_{t}$. The Tr-IPG uses the TCA algorithm to obtain a mapping function $\varphi(\cdot)$, and this mapping function is utilized to map the $p$ into a twentydimensional latent space ${ }^{2}$, and it means that $l=\varphi(p)$ is a twenty-dimensional vector. After that the Tr-IPG algorithm will find a solution $x$ for the FDA4 problem at time $t+1$, and this solution $x$ satisfies the requirement that it is nearest to $l$ in the latent space. The Tr-IPG will output the solution $x$ as one of the individuals of the initial population which can be used to solve the FDA4 problem at time $t+1$.

## IV. EMPIRICAL Study

Practically speaking, the proposed approach is compatible with any type of population-based optimization algorithms. As a case study, in our experiments, we select three wellrepresented algorithms with different operating metaphors to verify our approach. The first one is the NSGA-II [47] and it is a multiobjective genetic algorithm that applies nondominated

[^0]Algorithm 3: Tr-DMOEA: Transfer Learning based Dynamic Multi-objective Evolutionary Algorithm
Input: The Dynamic Optimization Function $F(X)$; a population based multiobjective algorithm MOA; a kernel function $\kappa(\cdot, \cdot)$.
Output: the POFs of $F(X)$.
1 Initialization ;
2 Use MOA to solve $F_{0}(X)$ to get a $P O F_{0}$;
3 for $t=1$ to $n$ do
4 Next-Pop $=\operatorname{Tr}-\operatorname{IPG}\left(F_{t}(\cdot), P O F_{(t-1)}, \kappa(\cdot, \cdot)\right)$; /* When a change occurred, we use Tr-IPG to generate an init population. */
$P O F_{t}=\operatorname{MOA}($ Next-Pop $)$;
6 return $P O F_{t}$;
7 end
sorting and crowding distance. The second multiobjective optimization algorithm is based on particle swarm optimization and it is simply called as MOPSO [48]. The third one is the RM-MEDA [49], which is a regularity model based multiobjective estimation of distribution algorithm.

The three corresponding algorithms with the proposed transfer learning are called Tr-NSGA-II, Tr-MOPSO, and Tr-RMMEDA, respectively for dynamic optimization. It should be noted that the original designs, NSGA-II, MOPSO, and RMMEDA are not appropriate for dynamic optimization. It is not difficult to find that these three algorithms belong to different categories, but all of them are well-developed, so it can strengthen the persuasive power and the confidence level to incorporate the proposed technology. At the same time, we also compare the new algorithms with other state-of-art designs.

One thing we need to emphasize is that in all our ex-


[^0]:    ${ }^{2}$ The dimensionality of the latent space depends on the parameters of the TCA algorithm.

periments, the parameters are set the same. In other words, for these twelve test functions and three different algorithms, we have used the same parameters and do not tune the parameters in TCA under different configurations for a better performance.

## A. Performance Metrics, Testing Functions and Settings

In this research, we use four performance metrics, the Inverted Generational Distance (IGD) and its variants, the Reactivity measure (React) and its variants, to evaluate the quality of the solutions obtained by these competing algorithms.

1) The inverted generational distance (IGD) [50] is a metric to quantify the performance of a multiobjective optimization algorithm. Let $P^{*}$ be the set of uniformly distributed Pareto optimal solutions in the POF and $P$ represent the POF obtained by the algorithm, the definition of the IGD is

$$
\operatorname{IGD}\left(P^{*}, P, C\right)=\frac{\sum_{v^{*}} \in P^{*} \min _{v \in P}\left\|v^{*}-v\right\|}{\left|P^{*}\right|}
$$

If we want the value of IGD to be as small as possible, the $P$ should be close enough to $P^{*}$. In other words, the IGD depicts the difference between the ideal POF and the POF obtained by the competing algorithms.
Please note that the definition of the IGD is slightly different from the original one, and the major difference is the parameter $C$ in Equation (9). The parameter $C$ is a combination of the benchmark functions parameters. We call it as configuration of the benchmark functions. The configurations we used in our experiments are described in Table II.
2) One variant of the IGD, called MIGD, can also be used to evaluate dynamic multiobjective optimization algorithms [51, 52], and it takes the average of the IGD values in some time steps over a run as the performance metric, given by

$$
\operatorname{MIGD}\left(P^{*}, P, C\right)=\frac{1}{|T|} \sum_{t \in T} \operatorname{IGD}\left(P_{t}^{*}, P_{t}, C\right)
$$

where $P_{t}^{*}$ and $P^{t}$ represent the points set of the ideal POF and the approximate POF obtained by the algorithm at time $t$. We also want to evaluate those algorithms under different environments, so a novel metric, DMIGD, is defined based on the MIGD, and the definition of the DMIGD is as follows:

$$
\operatorname{DMIGD}\left(P^{*}, P, C\right)=\frac{1}{|E|} \sum_{C \in E} \operatorname{MIGD}\left(P_{t}^{*}, P_{t}, C\right)
$$

where $|E|$ is the number of the different environments experienced. In our experiments, we choose eight different configurations. As a result, $|E|$ equals to eight. What we want to point out is that the DMIGD can evaluate a dynamic optimization algorithm from a highlevel view and it bears a significant difference with the MIGD since the MIGD just considers the dynamics in one environment.
3) The reactivity measure (React) [53] is used to measure the robustness of an algorithm, and its definition is as follows:

$$
\operatorname{React}_{s}(t, C)=\min \left\{t^{\prime}-t \mid t<t^{\prime} \in \mathbb{N}, \frac{\operatorname{acc}\left(t^{\prime}\right)}{\operatorname{acc}(t)} \geq 1-\varepsilon\right\}
$$

where $\operatorname{acc}(t)=\frac{H V(P O F(t))}{\max H V(P O F)}$ implies the accuracy rate of computing the POF at time $t$, and $H V$ refers to the value of Hypervolume [54]. The React describes how quickly a dynamic optimization algorithm can recover from a change, or convergence speed after changes. The value of the React is the smaller the better. We also want to evaluate the algorithms on a macro-scale, so we derive two additional metrics based on the React,

$$
\begin{gathered}
\operatorname{MReact}_{s}(T, C)=\frac{1}{|T|} \sum_{t \in T} \operatorname{React}_{s}(t, C) \\
\operatorname{DMReact}_{s}(T, C)=\frac{1}{|E|} \sum_{C \in E} \operatorname{MReact}_{s}(T, C)
\end{gathered}
$$

The MReact value can be considered as an average of the React values at different time points, but under the same configuration; DMReact is an average of the MReact values over different configurations considered.

In the experiments, we apply the IEEE CEC 2015 Benchmark problems set in Table I as test functions and the problem set has twelve testing functions [46]. In the definitions, the decision variables are $x=\left(x_{1}, \ldots, x_{n}\right)$ and $t=\frac{1}{n_{t}}\left\lfloor\frac{\tau_{T}}{n_{t}}\right\rfloor$, where $n_{t}, \tau_{T}$, and $\tau_{t}$ are the severity of change, maximum number of iterations, and frequency of change, respectively. Table II describes the different combinations of $n_{t}, \tau_{t}$, and $\tau_{T}$. Please note that for each $n_{t}-\tau_{T}$ combination, there will be $\frac{\tau_{T}}{\tau_{t}}$ environment changes. In other words, in all of our experiments, there are altogether twenty changes for the twelve dynamic problems.

The POFs of the testing functions have different shapes and each function belongs to a certain DMOPs type. Fig. 2 describes the true POFs of the twelve testing functions and we let the functions change three times. Type I implies POS changes, but POF does not change; Type II means that the POS and the POF change as well; Type III refers to the condition where the POF changes, but the POS does not change. From Table I, we can find that the POF of the functions could be non-convex, convex, isolated, deceptive, continuous or discontinuous. FDA4 and FDA5 are 3-objective functions while all of the remaining are 2-objective functions.

The dimensions of the decision variables are from 10 to 30-dimension. Please note that the $\mathrm{A}, \mathrm{B}$ and C values for the functions $\mathrm{FDA5}_{i s o}, \mathrm{FDA}_{\text {dec }}, \mathrm{DMOP}_{i s o}$ and $\mathrm{DMOP}_{d e c}$ are set to $\mathrm{G}(\mathrm{t}), 0.001$ and 0.05 respectively.

In all of the experiments, we set the population size to 200 and in each generation every algorithm will generate no more than 200 solutions. As mentioned above, we force each benchmark function to change 20 times, and in every change, we let the population carry out 50 iterations.

For the TCA parameters, we set the Gaussian kernel function to the default value and the expected dimensionality was set to be 20 . The value of $\mu$ was set to 0.5 .

![img-1.jpeg](img-1.jpeg)

Figure 2: The true POFs of the twelve testing functions. The red, green and blue lines depict the true POFs at the time steps zero, one and two, respectively.

Table I: The Benchmark Functions

| Name | Dim. | \# of Obj. | Type |
| :-- | --: | :--: | :-- |
| FDA4 | 12 | 3 | TYPE I |
| FDA5 | 12 | 3 | TYPE II |
| FDA5 $_{A w e}$ | 12 | 3 | TYPE II |
| FDA5 $_{d e c}$ | 12 | 3 | TYPE II |
| DIMP2 | 10 | 2 | TYPE I |
| DMOP2 | 10 | 2 | TYPE II |
| DMOP2 $_{A w e}$ | 10 | 2 | TYPE II |
| DMOP2 $_{d e c}$ | 10 | 2 | TYPE II |
| DMOP5 | 10 | 2 | TYPE I |
| HE2 | 30 | 2 | TYPE III |
| HE7 | 10 | 2 | TYPE III |
| HE9 | 10 | 2 | TYPE III |

Table II: Configurations of the Benchmark Functions Parameters

|  | $n_{t}$ | $T_{t}$ | $T_{T}$ |
| :-- | :-- | :-- | :-- |
| C1 | 10 | 5 | 100 |
| C2 | 10 | 10 | 200 |
| C3 | 10 | 25 | 500 |
| C4 | 10 | 50 | 1000 |
| C5 | 1 | 10 | 200 |
| C6 | 1 | 50 | 1000 |
| C7 | 20 | 10 | 200 |
| C8 | 20 | 50 | 1000 |

## B. Experimental Results

1) IGD Metric: For each benchmark function, we perform tests under eight different configurations which are listed in Table II. Each function will change 20 times, and after each change the algorithms would return a POS, and then we calculated the IGD, MIGD, and DMIGD values, respectively.

The detailed results of these experiments are described in twelve tables, and Supplemental Material contains those tables. These tables recorded the MIGD values of the algorithms running on different testing functions under different environments. In these tables, the "ROC" refers to the ratio of change of the MIGD values and we used bold face to identify those experiments where performance has been improved.

For the convenience of the readers and at the same time owing to space constraints, we summarize these experimental results in three tables, Table III, Table IV And Table V. These three tables illustrate the rate of change of the three new algorithms compared to their original designs. For example, the value of the first row (under C1 configuration) and the first column (under FDA4) of Table III is 61.32 , and this shows that the Tr-NSGA-II algorithm improves the NSGA-II algorithm by $61.32 \%$ when dealing with the FDA4 problem under the Configuration C1.

Please note that our experimental results are obtained without explicitly tuning the parameters one by one, and if we
adjust the parameters separately for different algorithms, we have reason to believe that we can get better experimental results. The reason that we did not tune the parameters specifically for getting better results is that the twelve test functions are not exactly the same, so we can set different parameters to obtain the best performance for each test function. For example, we can construct different latent spaces for the twelve benchmark functions individually via setting different parameters of the TCA method. However, we think that this one-by-one-adjustment strategy does not effectively explain the advantages of our approach since almost all algorithms can obtain a better performance via such parameter-tuning, and this makes no contribution to explain the superiority of the proposed algorithm.

We tabulate all the experimental results and obtain the following observations. For the NSGA-II, the overall effective rate of the Tr-NSGA-II was $78 \%$ (i.e., 75 cases with improving performance out of 96 total tests), of which 33 testing cases increased by more than $50 \%, 38$ increased by $5 \%-50 \%$ and 4 cases improved by $0-5 \%$; for the MOPSO, the total effective rate was $70 \%$ (i.e., 67 cases with improving performance out of 96 total tests), including 29 testing cases improved by more than $50 \%, 33$ performance improved by $5 \%-50 \%$, and five improved by $0-5 \%$; For the RM-MEDA, the total effective rate was $73 \%$ (i.e., 70 cases with improving performance out of 96 total tests), including 23 of the test cases increasing by

Table III: The Ratio of Change of MIGD Value between Tr-NSGA-II and NSGA-II

| ROC(\%) | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| FDA4 | $\mathbf{6 1 . 3 2}$ | $\mathbf{6 2 . 1 5}$ | $\mathbf{5 9 . 4 2}$ | $\mathbf{5 9 . 6 0}$ | $\mathbf{7 8 . 5 7}$ | $\mathbf{7 9 . 7 5}$ | $\mathbf{5 6 . 1 7}$ | $\mathbf{6 1 . 0 2}$ |
| FDA5 | $\mathbf{4 1 . 1 3}$ | $\mathbf{3 7 . 8 0}$ | -14.36 | $\mathbf{1 4 . 4 5}$ | $\mathbf{3 7 . 1 2}$ | $\mathbf{3 9 . 0 4}$ | $\mathbf{2 0 . 3 9}$ | $\mathbf{3 3 . 0 9}$ |
| FDA5 $_{i s o}$ | -48.91 | -17.37 | -31.83 | -31.98 | -20.14 | -28.66 | -2.44 | -6.15 |
| FDA5 $_{d e c}$ | $\mathbf{1 9 . 8 3}$ | $\mathbf{1 7 . 0 9}$ | $\mathbf{2 6 . 0 6}$ | $\mathbf{4 0 . 2 3}$ | $\mathbf{2 2 . 5 2}$ | $\mathbf{3 . 0 7}$ | $\mathbf{5 1 . 8 8}$ | $\mathbf{4 1 . 3 4}$ |
| DIMP2 | $\mathbf{3 0 . 7 0}$ | $\mathbf{4 2 . 4 1}$ | $\mathbf{3 9 . 5 7}$ | $\mathbf{3 4 . 6 1}$ | $\mathbf{4 7 . 3 0}$ | $\mathbf{3 8 . 6 9}$ | $\mathbf{3 7 . 5 7}$ | $\mathbf{4 4 . 5 4}$ |
| DMOP2 | $\mathbf{7 4 . 9 7}$ | $\mathbf{6 6 . 5 2}$ | $\mathbf{7 8 . 4 3}$ | $\mathbf{6 7 . 0 1}$ | -676.29 | $\mathbf{8 8 . 9 6}$ | $\mathbf{6 1 . 2 2}$ | $\mathbf{7 2 . 6 5}$ |
| DMOP2 $_{i s o}$ | -4.84 | -4.46 | -6.81 | -3.18 | -7.54 | -13.79 | -2.98 | -2.48 |
| DMOP2 $_{d e c}$ | $\mathbf{4 4 . 9 1}$ | $\mathbf{5 1 . 2 5}$ | $\mathbf{4 4 . 3 9}$ | $\mathbf{4 0 . 1 3}$ | $\mathbf{2 3 . 2 6}$ | $\mathbf{4 2 . 4 5}$ | $\mathbf{4 5 . 6 6}$ | $\mathbf{2 5 . 5 8}$ |
| DMOP3 | $\mathbf{7 2 . 7 0}$ | $\mathbf{7 3 . 6 1}$ | $\mathbf{8 3 . 5 0}$ | $\mathbf{5 7 . 6 5}$ | -514.50 | $\mathbf{4 . 3 2}$ | $\mathbf{7 4 . 1 8}$ | $\mathbf{7 6 . 2 9}$ |
| HE2 | $\mathbf{2 . 7 3}$ | -17.45 | $\mathbf{1 . 6 7}$ | $\mathbf{5 . 8 6}$ | $\mathbf{6 7 . 4 5}$ | $\mathbf{7 7 . 0 1}$ | $\mathbf{2 8 . 0 7}$ | -19.57 |
| HE7 | $\mathbf{5 7 . 1 0}$ | $\mathbf{5 8 . 5 7}$ | $\mathbf{5 9 . 4 5}$ | $\mathbf{6 1 . 5 7}$ | $\mathbf{5 3 . 4 7}$ | $\mathbf{5 8 . 3 4}$ | $\mathbf{5 7 . 7 7}$ | $\mathbf{6 1 . 9 8}$ |
| HE9 | $\mathbf{1 4 . 7 9}$ | $\mathbf{1 3 . 0 2}$ | $\mathbf{1 6 . 6 4}$ | $\mathbf{1 2 . 9 9}$ | $\mathbf{1 4 . 9 8}$ | $\mathbf{1 4 . 6 1}$ | $\mathbf{1 6 . 1 4}$ | $\mathbf{1 5 . 4 9}$ |

more than $50 \%, 39$ lifting $5 \%$ to $50 \%$, and 8 improved by 0 - $5 \%$.

These experimental results demonstrate that the transfer learning technique can improve the performance of the existing multiobjective EAs appreciably without significant modifications for solving the DMOPs. On the other hand, we would like to point out that most of the testing cases of performance degradation came from two functions - FDA5 $_{i s o}$ and DMOP2 $_{i s o}$. The common characteristic of these two functions is the isolated POFs, so we suspect that the reason why the performance is poor for the two benchmark functions is inappropriate parameters settings.

We also compare the DMIGD value with some chosen state-of-the-art designs, including Multidimensional Bayesian Network based Estimation Distribution Algorithm (MBN-EDA) [55], Random immigrants strategy based multiobjective Differential evolutionary algorithm with Decomposition (RND) and the Kalman Filter prediction based DMOEA (MOEA/DKF) [51, 52], and the results are depicted in Table VI. The experimental results show that the transfer learning based algorithms have much better performance over different problem characteristics in these benchmark functions. Even compared with chosen state-of-the-art algorithms, these transfer learning based algorithms can be much more efficient.
2) React Metric: Table VII depicts the DMReact values of all competing algorithms. We found that the Tr-NSGAII and Tr-MOPSO have shown improvements, which suggest that, at least at this parameters setting, the proposed approach can improve the adaptability of the NSGA-II and the MOPSO under dynamic environments. However the robustness of the RM-MEDA seems to be reduced, and one reason we envision is that the TCA method have coincidently reduced the diversity of the solutions. So how to improve the diversity and the
robustness at the same time is an interesting topic for the future research. The optimal choice of the parameter setting will be a topic in our future research.

## V. CONCLUSION AND FUTURE WORKS

In this paper, we propose an approach of exploiting a transfer learning technique to enhance the performance of dynamic multiobjective evolutionary algorithms. Our idea is that the solutions of a given DMOP at different times have different distributions, though there are some relationships between these probability distributions, they are not identical. This is a typical non-independent identically distributed (NonIID) problem, and classical machine learning methods are difficult to solve it.

For this reason, it is not surprise to understand why the traditional dynamic optimization algorithms designed based on classical machine learning find it hard to achieve satisfactory performance. To overcome these problems, we employ the techniques from the transfer learning to develop an algorithmic framework, which creates benefits for a variety of populationbased dynamic multiobjective evolutionary algorithms.

In our approach, we consider different probability distributions that the solutions obey at various times as the source and target domains, respectively. We can exploit the gained POF from the source domain to improve computational efficiency in searching for the POF at the next time instance. To achieve this goal, the transfer learning technique is applied to find a latent space where the global feature, MMD value, of the source and target domains is as small as possible. Meanwhile the major statistical characteristics of the data, i.e., the variance will remain unchanged. In this way, we can use the obtained POS to construct an initial population which can be employed

Table IV: The Ratio of Change of MIGD Value between Tr-MOPSO and MOPSO

| $\operatorname{ROC}(\%)$ | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| FDA4 | 18.01 | 16.44 | 15.85 | 17.34 | 14.15 | 13.09 | 18.98 | 18.88 |
| FDA5 | 43.09 | 56.21 | 25.44 | 21.56 | 60.00 | 57.88 | 29.65 | 23.78 |
| FDA5 $_{i s o}$ | $-11.03$ | $-7.58$ | $-2.12$ | $-1.49$ | $-12.51$ | $-5.11$ | $-6.98$ | $-8.00$ |
| FDA5 $_{d e c}$ | 17.54 | 30.66 | 50.61 | 23.97 | 10.64 | 11.78 | 28.18 | 20.68 |
| DIMP2 | 86.54 | 88.36 | 93.05 | 94.73 | 73.76 | 87.17 | 83.68 | 89.37 |
| DMOP2 | 92.85 | 96.77 | 96.51 | 94.93 | $-478.53$ | 78.24 | 26.14 | 84.36 |
| DMOP2 $_{i s o}$ | $-0.26$ | 2.55 | 1.64 | 2.82 | $-0.01$ | $-0.04$ | $-0.58$ | 3.31 |
| DMOP2 $_{d e c}$ | 89.96 | 93.98 | 93.92 | 96.53 | 92.54 | 92.10 | 97.14 | 96.66 |
| DMOP3 | $-296.04$ | 54.28 | 19.34 | 28.14 | $-1371.99$ | 94.39 | 51.00 | 26.72 |
| HE2 | 14.04 | 34.03 | 11.11 | 34.34 | 38.46 | 36.01 | $-1.96$ | 14.06 |
| HE7 | 2.88 | $-3.40$ | $-1.78$ | $-0.49$ | 13.96 | 8.11 | $-14.43$ | $-9.12$ |
| HE9 | $-11.81$ | $-11.45$ | $-12.29$ | $-14.04$ | $-37.00$ | $-33.30$ | $-16.15$ | $-13.57$ |

by any population-based optimization algorithms to find the POS of the next time instance.

We applied the proposed idea to improve three well-known multidobjective optimization algorithms: NSGA-II, MOPSO, and RM-MEDA. The enhanced algorithms are compared with the original designs and some chosen competing algorithms on a well-adopted benchmark set which involves twelve testing functions. Almost all the experimental results validate that introducing the transfer leaning technique into the dynamic optimization algorithm can greatly improve the quality of the solutions and robustness of the algorithms. This line of research proposed herein can be regarded as a new avenue for designing effective and efficient evolutionary algorithms for DMOPs. A rich body of machine learning techniques can inspire further innovations in solving real-world application [56] with various degrees of complexities and uncertainties.

## ACKNOWLEDGMENT

This work was supported by the National Natural Science Foundation of China (No.61003014 and No.61673328) and Foundation of Xiamen University's President (No. 20720150150). The first author also wants to thank China Scholarship Council (No. 20150631505) and Oklahoma State University for providing funding and facilities to support his research as a visiting scholar. We are very grateful to Miss Arrichana Muruganantham for providing the code of [51] and Mr. Minmin Wang for experimental assistance.

## REFERENCES

[1] M. Farina, K. Deb, and P. Amato, "Dynamic multiobjective optimization problems: test cases approximations, and applications," IEEE Transactions on Evolutionary Computation, vol. 8, no. 5, pp. 425-442, oct 2004.
[2] C. Cruz, J. R. González, and D. A. Pelta, "Optimization in dynamic environments: a survey on problems methods and measures," Soft Comput, vol. 15, no. 7, pp. 1427-1448, dec 2010.
[3] J. Xu, P. B. Luh, F. B. White, E. Ni, and K. Kasiviswanathan, "Power portfolio optimization in deregulated electricity markets with risk management," IEEE Transactions on Power Systems, vol. 21, no. 4, pp. 1653-1662, 2006.
[4] T. T. Nguyen, S. Yang, and J. Branke, "Evolutionary dynamic optimization: A survey of the state of the art," Swarm and Evolutionary Computation, vol. 6, pp. 1-24, oct 2012.
[5] M. Daneshyari and G. G. Yen, "Cultural-based particle swarm for dynamic optimisation problems," International Journal of Systems Science, vol. 45, no. 7, pp. 1284-1304, 2012.
[6] A. Simões and E. Costa, "Prediction in evolutionary algorithms for dynamic environments," Soft Comput, vol. 18, no. 8, pp. 1471-1497, oct 2013.
[7] C. Rossi, M. Abderrahim, and J. C. Díaz, "Tracking moving optima using Kalman-based predictions," Evolutionary Computation, vol. 16, no. 1, pp. 1-30, mar 2008.
[8] P. Stroud, "Kalman-extended genetic algorithm for search in nonstationary environments with noisy fitness evaluations," IEEE Transactions on Evolutionary Computation, vol. 5, no. 1, pp. 66-77, 2001.
[9] S. J. Pan and Q. Yang, "A survey on transfer learning," IEEE Transactions on, Knowledge and Data Engineering, vol. 22, no. 10, pp. 13451359, 2010.
[10] S. J. Pan, I. W. Tsang, J. T. Kwok, and Q. Yang, "Domain adaptation via transfer component analysis," IEEE Transactions on Neural Networks, vol. 22, no. 2, pp. 199-210, 2011.
[11] D.-C. Dang, T. Jansen, and P. K. Lehre, "Populations can be essential in dynamic optimisation," in Proceedings of the 2015 on Genetic and Evolutionary Computation Conference - GECCO, Association for Computing Machinery (ACM), 2015.
[12] D. Dang, T. Jansen, and P. K. Lehre, "Populations can be essential in tracking dynamic optima," Algorithmica, pp. 1-21, 2016.
[13] C. Raquel and X. Yao, "Dynamic multi-objective optimization: a survey of the state-of-the-art," in Studies in Computational Intelligence. Springer Science mathplus Business Media, 2013, pp. 85-106.
[14] R. Azzouz, S. Bechikh, and L. B. Said, "Dynamic multi-objective optimization using evolutionary algorithms: a survey," in Recent Advances in Evolutionary Multi-objective Optimization. Springer Nature, aug 2016, pp. 31-70.
[15] C.-K. Goh and K. C. Tan, "Dynamic evolutionary multi-objective optimization," in Evolutionary Multi-objective Optimization in Uncertain Environments. Springer Science mathplus Business Media, pp. 125152.
[16] H. G. Cobb, "An investigation into the use of hypermutation as an adaptive operator in genetic algorithms having continuous, time-dependent

Table V: The Ratio of Change MIGD Value between Tr-RM-MEDA and RM-MEDA

| ROC(\%) | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| FDA4 | 21.47 | 22.74 | 22.42 | 22.91 | 25.75 | 27.71 | 22.32 | 23.08 |
| FDA5 | 54.07 | 59.96 | 61.66 | 57.40 | 76.55 | 69.49 | 56.24 | 54.71 |
| $\mathrm{FDA5}_{i s o}$ | $-0.29$ | $-0.09$ | 0.08 | $-0.30$ | 1.81 | $-0.06$ | $-0.63$ | $-0.08$ |
| $\mathrm{FDA5}_{d e c}$ | 39.69 | 33.15 | 37.16 | 35.83 | 65.97 | 65.59 | 41.72 | 45.66 |
| DIMP2 | 5.91 | $-8.53$ | $-2.03$ | $-3.49$ | $-1.08$ | 1.01 | $-2.33$ | $-4.57$ |
| DMOP2 | $-827.79$ | $-52.71$ | 37.53 | 33.36 | $-3.34$ | $-1.67$ | 21.07 | $-13.04$ |
| DMOP2 $_{i s o}$ | $-0.01$ | $-0.09$ | $-0.05$ | $-0.06$ | 0.01 | $-0.01$ | 0.07 | $-0.09$ |
| DMOP2 $d e c$ | 53.72 | 64.32 | 51.05 | 60.02 | 1.39 | 3.85 | 57.93 | 49.28 |
| DMOP3 | 24.65 | 22.08 | $-25.15$ | 0.49 | $-0.45$ | $-0.79$ | 10.75 | 27.48 |
| HE2 | 86.81 | 87.01 | 86.74 | 88.01 | 89.99 | 89.59 | 88.42 | 87.91 |
| HE7 | 13.31 | 21.82 | 21.40 | 20.29 | 19.23 | 14.87 | 21.32 | 22.57 |
| HE9 | 7.48 | 7.61 | 6.95 | 6.91 | 8.35 | 7.53 | 6.74 | 5.43 |

nonstationary environments," Tech. Rep. Technical Report AIC-90-001, 1990.
[17] F. Vavak, T. C. Fogarty, and K. Jukes, "A genetic algorithm with variable range of local search for tracking changing environments," in Parallel Problem Solving from Nature - PPSN IV. Springer Science mathplus Business Media, 1996, pp. 376-385.
[18] Y. Woldesenbet and G. Yen, "Dynamic evolutionary algorithm with variable relocation," IEEE Transactions on Evolutionary Computation, vol. 13, no. 3, pp. 500-513, jun 2009.
[19] J. Grefenstette, "Genetic algorithms for changing environments," in Parallel Problem Solving from Nature 2. Elsevier, 1992, pp. 137-144.
[20] S. Yang and R. Tinós, "A hybrid immigrants scheme for genetic algorithms in dynamic environments," International Journal of Automation and Computing, vol. 4, no. 3, pp. 243-254, jul 2007.
[21] M. Mavrovouniotis and S. Yang, "Genetic algorithms with adaptive immigrants for dynamic environments," in 2013 IEEE Congress on Evolutionary Computation. Institute of Electrical \& Electronics Engineers (IEEE), jun 2013.
[22] S. Yang, "Genetic algorithms with memory- and elitism-based immigrants in dynamic environments," Evolutionary Computation, vol. 16, no. 3, pp. 385-416, Sep 2008.
[23] K. Deb, U. B. R. N., and S. Karthik, "Dynamic multi-objective optimization and decision-Making using modified NSGA-II: a case study on hydro-thermal power scheduling," in Lecture Notes in Computer Science. Springer Science mathplus Business Media, pp. 803-817.
[24] J. Branke, "Memory enhanced evolutionary algorithms for changing optimization problems," in Proceedings of the 1999 Congress on Evolutionary Computation. Institute of Electrical and Electronics Engineers (IEEE).
[25] C.-K. Goh and K. C. Tan, "A competitive-cooperative coevolutionary paradigm for dynamic multiobjective optimization," IEEE Transactions on Evolutionary Computation, vol. 13, no. 1, pp. 103-127, feb 2009.
[26] Y. Wang and B. Li, "Multi-strategy ensemble evolutionary algorithm for dynamic multi-objective optimization," Memetic Comp., vol. 2, no. 1, pp. $3-24$, sep 2009.
[27] L. While, P. Hingston, L. Barone, and S. Huband, "A faster algorithm for calculating hypervolume," IEEE transactions on evolutionary computation, vol. 10, no. 1, pp. 29-38, 2006.
[28] R. Azzouz, S. Bechikh, and L. B. Said, "A dynamic multi-objective evolutionary algorithm using a change severity-based adaptive population management strategy," Soft Comput, aug 2015.
[29] J. Branke, T. Kaussler, C. Smidt, and H. Schmeck, "A Multi-population
approach to dynamic optimization problems," in Evolutionary Design and Manufacture. Springer Science mathplus Business Media, 2000, pp. 299-307.
[30] C. Li and S. Yang, "Fast Multi-Swarm Optimization for Dynamic Optimization Problems," in 2008 Fourth International Conference on Natural Computation. Institute of Electrical and Electronics Engineers (IEEE), 2008.
[31] S. Yang and C. Li, "A clustering particle swarm optimizer for locating and tracking multiple optima in dynamic environments," IEEE Transactions on Evolutionary Computation, vol. 14, no. 6, pp. 959-974, dec 2010.
[32] P. A. N. Bosman, "Learning and anticipation in online dynamic optimization," in Studies in Computational Intelligence. Springer Science mathplus Business Media, 2007, pp. 129-152.
[33] A. Zhou, Y. Jin, and Q. Zhang, "A population prediction strategy for evolutionary dynamic multiobjective optimization," IEEE Transactions on Cybernetics, vol. 44, no. 1, pp. 40-53, jan 2014.
[34] M. Iqbal, B. Xue, H. Al-Sahaf, and M. Zhang, "Cross-domain reuse of extracted knowledge in genetic programming for image classification," IEEE Transactions on Evolutionary Computation, to be published.
[35] M. Iqbal, W. N. Browne, and M. Zhang, "Reusing building blocks of extracted knowledge to solve complex, large-scale boolean problems," IEEE Transactions on Evolutionary Computation, vol. 18, no. 4, pp. $465-480,2014$.
[36] L. Feng, Y.-S. Ong, M.-H. Lim, and I. W. Tsang, "Memetic search with interdomain learning: A realization between cvtp and carp," IEEE Transactions on Evolutionary Computation, vol. 19, no. 5, pp. 644-658, 2015.
[37] S. Ben-David, J. Blitzer, K. Crammer, A. Kulesza, F. Pereira, and I. W. Vaughan, "A theory of learning from different domains," Machine learning, vol. 79, no. 1-2, pp. 151-175, 2010.
[38] V. M. Patel, R. Gopalan, R. Li, and R. Chellappa, "Visual domain adaptation: an overview of recent advances," IEEE signal processing magazine, vol. 32, pp. 53-69, 2015.
[39] M. Jiang, W. Huang, Z. Huang, and G. G. Yen, "Integration of global and local metrics for domain adaptation learning via dimensionality reduction," IEEE Transactions on Cybernetics, vol. 47, no. 1, pp. 38-51, 2017.
[40] S. Ben-David, J. Blitzer, K. Crammer, F. Pereira et al., "Analysis of representations for domain adaptation," Advances in neural information processing systems, vol. 19, p. 137, 2007.
[41] A. Gretton, K. M. Borgwardt, M. Rasch, B. Schölkopf, and A. J. Smola,

Table VI: DMIGD Values of Different Algorithms

| DMIGD | NSGA-II | Tr-NSGA-II | MOPSO | Tr-MOPSO | RM-MEDA | Tr-RM-MEDA | MBN-EDA | RND | MOEA/D-KF |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| FDA4 | 0.2634 | 0.0858 | 0.0732 | 0.0609 | 0.0680 | 0.0520 | 0.43 | 0.1698 | 0.1913 |
| FDA5 | 0.3301 | 0.2306 | 0.2131 | 0.1196 | 0.2089 | 0.0776 | 0.51 | 0.5323 | 0.4963 |
| $\mathrm{FDA}_{5 \text { iso }}$ | 0.1048 | 0.1292 | 0.1106 | 0.1181 | 0.0650 | 0.0649 | 0.64 | 0.1433 | 0.1465 |
| $\mathrm{FDA}_{5 \text { dec }}$ | 0.5923 | 0.4559 | 0.2746 | 0.2139 | 0.5779 | 0.3275 | 1.27 | 0.5403 | 0.5476 |
| DIMP2 | 3.8986 | 2.3502 | 2.3684 | 0.2937 | 4.8892 | 4.9769 | 6.97 | 17.9537 | 22.9536 |
| DMOP2 | 0.4202 | 0.3439 | 0.2129 | 0.2538 | 4.5942 | 4.7130 | 1.4 | 1.4329 | 3.0619 |
| $\mathrm{DMOP}_{2 \text { iso }}$ | 0.0325 | 0.0358 | 0.0319 | 0.0318 | 0.0290 | 0.0290 | 2.56 | 0.0315 | 0.0316 |
| $\mathrm{DMOP}_{2 \text { dec }}$ | 0.6303 | 0.3930 | 0.4192 | 0.0254 | 0.1449 | 0.0940 | 2.89 | 9.0504 | 9.2188 |
| DMOP3 | 0.8851 | 1.0133 | 0.2851 | 0.2650 | 4.5897 | 4.6177 | 1.38 | 0.0697 | 0.0836 |
| HE2 | 0.2096 | 0.1501 | 0.0847 | 0.0640 | 0.8451 | 0.1017 | 0.83 | 0.0744 | 0.0745 |
| HE7 | 0.0946 | 0.0390 | 0.0582 | 0.0583 | 0.0428 | 0.0342 | 0.21 | 0.1787 | 0.2365 |
| HE9 | 0.2954 | 0.2508 | 0.2459 | 0.2887 | 0.2565 | 0.2383 | 0.36 | 0.3432 | 0.4108 |

Table VII: DMReact Value of the Algorithms

| DMREACT | NSGA-II | Tr-NSGA-II | MOPSO | Tr-MOPSO | RM-MEDA | Tr-RM-MEDA |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| FDA4 | 1.9803 | $\mathbf{1 . 7 6 6 4}$ | 1.4934 | $\mathbf{1 . 2 8 9 5}$ | 1.5033 | 1.7072 |
| FDA5 | 1.7204 | $\mathbf{1 . 5 6 2 5}$ | 1.4375 | $\mathbf{1 . 3 0 9 2}$ | 2.9638 | $\mathbf{1 . 6 0 8 6}$ |
| FDA5 $5_{\text {iso }}$ | 1.7105 | $\mathbf{1 . 4 5 3 9}$ | 1.6283 | 1.7039 | 1.0329 | $\mathbf{1 . 0 0 6 6}$ |
| FDA5 $5_{\text {dec }}$ | 1.7928 | 1.8224 | 1.5132 | 1.9375 | 2.5000 | 2.5263 |
| DIMP2 | 2.2697 | 2.2763 | 1.4013 | $\mathbf{1 . 1 1 5 1}$ | 1.9243 | 2.0197 |
| DMOP2 | 2.1645 | $\mathbf{1 . 9 6 7 1}$ | 1.5592 | 1.8487 | 1.5789 | 1.7467 |
| DMOP2 $2_{\text {iso }}$ | 1.4375 | 1.4836 | 1.4704 | $\mathbf{1 . 3 5 8 6}$ | 1.3355 | 1.4605 |
| DMOP2 $2_{\text {dec }}$ | 2.2961 | $\mathbf{2 . 0 1 6 4}$ | 1.5461 | 2.1809 | 1.9309 | 2.1316 |
| DMOP3 | 1.7039 | $\mathbf{1 . 3 8 1 6}$ | 1.5329 | $\mathbf{1 . 3 0 2 6}$ | 1.0987 | 1.1349 |
| HE2 | 2.0428 | $\mathbf{1 . 9 4 7 4}$ | 1.0987 | 1.2862 | 2.1086 | $\mathbf{1 . 4 5 7 2}$ |
| HE7 | 1.0000 | $\mathbf{1 . 0 0 0 0}$ | 1.0000 | $\mathbf{1 . 0 0 0 0}$ | 1.0000 | $\mathbf{1 . 0 0 0 0}$ |
| HE9 | 1.0000 | $\mathbf{1 . 0 0 0 0}$ | 1.0000 | 1.3125 | 1.0000 | $\mathbf{1 . 0 0 0 0}$ |

"A kernel method for the two-sample-problem," in Advances in neural information processing systems, 2006, pp. 513-520.
[42] A. Smola, A. Gretton, L. Song, and B. Schölkopf, "A hilbert space embedding for distributions," in Algorithmic Learning Theory. Springer, 2007, pp. 13-31.
[43] I. Steinwart, "On the influence of the kernel on the consistency of support vector machines," The Journal of Machine Learning Research, vol. 2, pp. 67-93, 2002.
[44] J. Shave-Taylor and N. Cristianini, Kernel methods for pattern analysis. Cambridge university press, 2004.
[45] B. Scholkopft and K.-R. Mullert, "Fisher discriminant analysis with kernels," in Proceedings of the 1999 IEEE Signal Processing Society Workshop Neural Networks for Signal Processing IX, Madison, WI, USA, 1999, pp. 23-25.
[46] M. Helbig and A. Engelbrecht, "Benchmark functions for cec 2015 special session and competition on dynamic multi-objective optimization," Tech. Rep., 2015.
[47] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, "A fast and elitist multiobjective genetic algorithm: Noga-it," IEEE transactions on evolutionary computation, vol. 6, no. 2, pp. 182-197, 2002.
[48] C. C. Coello and M. S. Lechuga, "Mopso: A proposal for multiple objective particle swarm optimization," in Evolutionary Computation, 2002. CEC'02. Proceedings of the 2002 Congress on, vol. 2. IEEE, 2002, pp. 1051-1056.
[49] Q. Zhang, A. Zhou, and Y. Jin, "Rm-meda: A regularity model-based multiobjective estimation of distribution algorithm," IEEE Transactions on Evolutionary Computation, vol. 12, no. 1, pp. 41-63, 2008.
[50] M. R. Sierra and C. A. C. Coello, "Improving pso-based multiobjective optimization using crowding, mutation and $\epsilon$-dominance," in International Conference on Evolutionary Multi-Criterion Optimization. Springer, 2005, pp. 505-519.
[51] A. Muruganantham, K. C. Tan, and P. Vadakkepat, "Solving the IEEE CEC 2015 dynamic benchmark problems using Kalman filter based dynamic multiobjective evolutionary algorithm," in Proceedings

in Adaptation Learning and Optimization. Springer Science mathplus Business Media, nov 2015, pp. 239-252.
[52] A. Muruganantham, K. Tan, and P. Vadakkepat, "Evolutionary Dynamic Multiobjective Optimization Via Kalman Filter Prediction," IEEE Transactions on Cybernetics, vol. 46, no. 12, pp. 2862-2873, Dec 2016.
[53] M. C. Sola, "Parallel processing for dynamic multi-objective optimization," Ph.D. dissertation, Ph. D. thesis, Universidad de Granada, Dept. of Computer Architecture and Computer Technology, Universidad de Granada, Spain, 2010.
[54] A. J. Nebro, F. Luna, E. Alba, B. Dorronsoro, J. J. Durillo, and A. Beham, "Abyss: Adapting scatter search to multiobjective optimization," IEEE Transactions on Evolutionary Computation, vol. 12, no. 4, pp. 439-457, 2008.
[55] H. Karshenas, R. Santana, C. Bielza, and P. Larranaga, "Multiobjective estimation of distribution algorithm based on joint modeling of objectives and variables," IEEE Transactions on Evolutionary Computation, vol. 18, no. 4, pp. 519-542, 2014.
[56] Y. Sun, G. G. Yen, and Z. Yi, "Reference line-based estimation of distribution algorithm for many-objective optimization," KnowledgeBased Systems, vol. 132, pp. 129-143, 2017.
![img-6.jpeg](img-6.jpeg)

Min JIANG (M'11-SM'12) received his bachelor and Ph.D. degrees in computer science from Wuhan University, China, in 2001 and 2007, respectively. Subsequently as a postdoc in the Department of Mathematics of Xiamen University. Currently he is an associate professor in the Department of Cognitive Science and Technology, Xiamen University. His main research interests are Machine Learning, Computational Intelligence and Neural-symbolic Integration. He has a special interest in dynamic multiobjective optimization, machine learning, the software development and in the basic theories of robotics. In 2016, he received the Outstanding Reviewer award from IEEE Transactions on Cybernetics. Dr. Jiang is currently serving as an associate editor for the IEEE Transactions on Cognitive and Developmental Systems and he is the Chair of IEEE CIS Xiamen Chapter.
![img-5.jpeg](img-5.jpeg)

Zhongqiang HUANG received the bachelor and master degree in Cognitive Science and Technology from Xiamen University in 2013 and 2016 respectively. He is currently working as an algorithm engineer at Sangfor cooperation, Shenzhen, China. His research interest includes computational intelligence and machine learning.
![img-6.jpeg](img-6.jpeg)

Wenzhen HUANG received the bachelor degree in Cognitive Science and Technology from Xiamen University, Xiamen, China, in 2014. He is currently a master student with the Institute of Automation of the Chinese Academy of Sciences, Beijing, China. His research interest includes computational intelligence and machine learning.
![img-5.jpeg](img-5.jpeg)

Gary G. YEN (S'87-M'88-SM'97-F'09) received a Ph.D. degree in electrical and computer engineering from the University of Notre Dame in 1992. Currently he is a Regents Professor in the School of Electrical and Computer Engineering, Oklahoma State University (OSU). Before joined OSU in 1997, he was with the Structure Control Division, U.S. Air Force Research Laboratory in Albaquerque. His research interest includes intelligent control, computational intelligence, conditional health monitoring, signal processing and their industrial/defense applications.
Dr. Yen was an associate editor of the IEEE Control Systems Magazine, IEEE Transactions on Control Systems Technology, Automatica, Mechantronics, IEEE Transactions on Systems, Man and Cybernetics, Parts A and B and IEEE Transactions on Neural Networks. He is currently serving as an associate editor for the IEEE Transactions on Evolutionary Computation and the IEEE Transactions on Cybernetics. He served as the General Chair for the 2003 IEEE International Symposium on Intelligent Control held in Houston, TX and 2006 IEEE World Congress on Computational Intelligence held in Vancouver, Canada. Dr. Yen served as Vice President for the Technical Activities in 20052006 and then President in 2010-2011 of the IEEE Computational intelligence Society. He was the founding editor-in-chief of the IEEE Computational Intelligence Magazine, 2006-2009. In 2011, he received Andrew P Sage Best Transactions Paper award from IEEE Systems, Man and Cybernetics Society and in 2014, he received Meritorious Service award from IEEE Computational Intelligence Society.
![img-6.jpeg](img-6.jpeg)

Liming QIU received his bachelor degree from Fujian Agriculture and Forestry University, Fuzhou, China in 2015, and currently he is a master student of the department of cognitive science and technogoly of Xiamen University and a member of the Fujian Key Lab of the Brain-like Intelligent systems. His research interests include multiobjective optimization and evolutionary computation.