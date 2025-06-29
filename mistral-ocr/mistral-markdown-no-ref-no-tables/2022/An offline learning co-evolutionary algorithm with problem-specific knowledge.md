# An offline learning co-evolutionary algorithm with problem-specific knowledge 

Fuqing Zhao ${ }^{\mathrm{a}, *}$, Bo Zhu ${ }^{\mathrm{a}}$, Ling Wang ${ }^{\mathrm{b}}$, Tianpeng Xu ${ }^{\mathrm{a}}$, Ningning Zhu ${ }^{\mathrm{a}}$, Jonrinaldi Jonrinaldi ${ }^{\mathrm{c}}$<br>${ }^{a}$ School of Computer and Communication, Lanzhou University of Technology, Lanzhou 730050, China<br>${ }^{\mathrm{b}}$ Department of Automation, Tsinghua University, Beijing 10084, China<br>${ }^{\mathrm{c}}$ Department of Industrial Engineering, Universitas Andalas, Padang 25163, Indonesia

## A R T I C L E I N F O

Keywords:
Fitness landscape
Random forest
Offline-learning
Estimation of distribution
Differential evolution


#### Abstract

The meta-heuristics is an effective way to solve the complex optimization problems. However, the applicability of meta-heuristic is restricted in real applications due to the various characteristics of the corresponding problems. An offline learning co-evolutionary algorithm (OLCA) based on the fitness landscape analysis that introduces the Gaussian estimation of distribution algorithm (EDA) and a variant of differential evolution (DE) for enhancing the search ability, is proposed for complex continuous real-valued problems. The relationship between strategies and fitness landscapes is established by using offline learning of a random forest. The suitable strategy is determined based on the properties of the fitness landscape trained by a random forest before the beginning of the evolutionary process. The proposed OLCA is tested by using the CEC 2017 benchmark test suite and is compared with several state-of-the-art algorithms. The results show that the proposed OLCA is efficient and competitive for solving complex continuous optimization problems. In addition, the effectiveness of the proposed OLCA is also verified by using 19 IEEE CEC 2011 benchmark problems for tackling real-world problems.


## 1. Introduction

Optimization problems are an important domain in computer science, management sciences, and engineering applications since various real problems are essentially aimed at achieving optimal configurations [1]. The complex continuous optimization problems are usually expressed as minimizing the objective function $\operatorname{Min} f(x)$ and the optimal solution vector $x=\left(x_{1}, x_{2}, \ldots x_{l}, \ldots x_{D}\right)$, where $D$ denotes the dimension of the problem [2]. It is notable that the difficulty of computation increases exponentially with an increase in the number of dimensions. The complex continuous optimization problems are characterized by non-linear, non-convex, multi-modal, non-differentiable, and non-separable variables [3,4]. The traditional mathematical methods have a strong theoretical foundation and work well on linear, integer programming problems. However, the mathematical methods are unable to efficiently solve the complex optimization problems with the aforementioned properties. The gradient information is utilized frequently in the mathematical approach for finding a satisfactory solution. The black-box optimization problems without gradient information are hard to solve based on the mathematical methods [5]. The meta-heuristics are an effective way to overcome the shortcomings of mathematical methods.

Various meta-heuristics have been presented in literature to address the complex optimization problems [6,7] including genetic algorithm (GA) [8,9], differential evolution (DE) [10-13], particle swarm optimization (PSO) $[14,15]$, and estimation of distribution algorithm (EDA) $[16,17]$. As compared to mathematical methods, meta-heuristics are more robust, less demanding for rigorous mathematical formulations, and require no gradient information. Besides, meta-heuristics usually operate on a population (implicit parallelism), thus being less prone to the local optima [18]. Although the proposed meta-heuristics have achieved satisfactory results, different meta-heuristics have different biases. It is noteworthy that no algorithm performs best in all the cases as stated by the no free lunch theorem [19].

The selection of appropriate algorithm based on the different characteristics of the problem is a feasible way to solve the optimization problems [20,21]. The selection of an algorithm based on an intelligent policy to achieve the co-evolution between various algorithms is an effective way for the no free lunch theorem dilemma [22]. Note that meta-heuristics only focus on the algorithm itself and ignore the characteristics of the optimization problems. The fitness landscape analysis techniques provide an effective way to understand the features of problems. Although the fitness landscape is often adopted to determine

[^0]
[^0]:    a Corresponding author.

    E-mail address: fzhao2000@hotmail.com (F. Zhao).

the complexity of an optimization problem, there are very few works that utilize the fitness landscape for designing algorithms [23].

Machine learning has become a powerful tool for addressing problems in various fields. Although meta-heuristics and machine learning techniques are developed for different purposes, they are adopted to perform common tasks such as feature selection or solving optimization problems [24]. Meta-heuristics and machine learning techniques frequently interact to improve their search or learning capabilities [25]. The machine learning community uses meta-learning for the automatic selection of algorithms. Meta-learning aims to understand the relationship between the problem features and the performance of an algorithm. Considering the learning style of meta-learning, the process of algorithm selection is classified into two types, including online and offline learning [26]. The offline learning aims to construct the problem-algorithm mapping based on a set of training samples, and predicts the problem-algorithm mapping for unseen data samples. The advantage of offline learning is the low computational cost once the training process is completed [27]. There are few works presented in literature that apply meta-learning to complex continuous optimization problems.

In order to effectively address the aforementioned problems in the complex real-valued optimization problems, a co-evolutionary algorithm that integrates EDA and DE as the primary search strategies, based on the fitness landscape analysis is proposed in this work. The EDA and DE are embedded in an offline learning co-evolutionary algorithm (OLCA) to adapt various optimization problems with different properties. The main contributions of this work are presented below.
(1) An OLCA that introduces EDA and DE based on the fitness landscape is proposed to solve complex continuous optimization problems.
(2) The fitness landscape analysis technique is embedded in the proposed OLCA to extract the structural information of the problems and to guide the prediction of the random forest.
(3) A random forest is introduced to establish the problem-algorithm mapping based on offline learning. The search behavior of OLCA is analyzed with a visualized methodology to intuitively observe the execution process of the algorithm.

The rest of this paper is organized as follows. Section 2 presents the literature review, including the improvement history of EDA and DE, fitness landscape analysis techniques, and offline learning for optimization problems. Section 3 illustrates the framework of proposed OLCA and the training of a random forest based on the fitness landscape. Section 4 reports the experimental results and analysis. Finally, the paper is summarized in Section 5 and the future work is discussed.

## 2. Related works

The estimation of distribution algorithm (EDA) as an evolutionary algorithm was first proposed by H.Mühlenbein and G.Paap in 1996 [28]. EDA is characterized by the way of generating offspring, i.e., sampling solutions based on a probability distribution instead of through crossover and mutation operators as generated in other kinds of evolutionary algorithms. During the past few decades, EDAs have been applied widely in both combinatorial and continuous domains [28]. There are various models that have been introduced in EDAs, such as the Gaussian model, Cauchy model, and histogram model, to describe the distribution of high-quality solutions. The Gaussian EDAs (GEDA) are generally classified into three categories based on the variable dependencies, i.e., (1) univariate EDA that assumes that all the variables are independent [30], (2) bivariate EDA that only considers some pairwise variable interactions [31], and (3) multivariate EDA that considers the interactions among multiple variables [32].

Although GEDAs possess a huge potential for solving complex optimization problems, they often suffer from premature convergence. This
defect is attributed to the rapid shrinking in the variances. Various improvements have been performed to address this defect. Ocenasek et al. [33] proposed a new evolution strategy that combines the mixed Bayesian optimization algorithm and variance adaption. Grahl et al. [34] proposed an adaptive variance scaling (AVS) strategy, which tunes the variances when it identifies that the algorithm is traversing a slope. The authors developed two identification strategies, i.e., the strategies based on correlation triggering and standard deviation ratio (SDR). Few researchers achieved variance tuning by modifying the eigenvalues of the estimated covariance matrix instead of performing variance scaling directly $[35,36]$.

Note that the performance of GEDA not only depends on its search scope but also on the direction of search. There are few works that show that the main search direction of GEDA tends to become orthogonal to the improvement direction of the fitness functions [37]. In [38], a powerful variant of EDA variant known as AMaLGaM is developed based on the anticipated mean shift (AMS) technique. It estimates the covariance matrix by shifting part of the selected solutions along the anticipated gradient direction, such that the main search direction is improved to a certain extent. Liang et al. [39] proposed a variant of EDA called $\mathrm{EDA}^{2}$. In this work, a historical memory mechanism, which conserves a certain number of populations generated in the former generations, is developed to estimate the covariance matrix of the Gaussian model. This mechanism contributes to the EDA for discovering a more promising search space. The covariance matrix adaption evolution strategy (CMA-ES) [40] is a special EDA that employs the rank- $\mu$-update operator to increase the variance along the direction of gradient.

Additionally, extensive efforts have been made to improve the efficiency of EDA. Dong et al. [41] presented a novel framework based on EDA and model complexity control (EDA-MCC). This framework for the first time designed an EDA based on a multivariate model that can be applied to 500D problems. In [40], a weakly dependent variable identification and subspace modeling technique are employed to solve high dimensional problems. In addition, this method also provides the structural information of the problems and saves the computational resources. Zhao et al. [42] developed a new hybrid optimization algorithm that combines the EDA with a differential evolution based on chaos theory. In cDE/EDA, the chaos strategy was integrated in the differential evolution to strengthen the search ability of the DE. In cDE/EDA, the value of $F, C R$, and $\gamma$ (the decisive factor) was updated during the search process based on the chaotic operation. The parameter $\gamma$ determines the proportion of individuals that perform the mutation operation. Ren et al. [43] proposed a new EDA variant named AAVS-EDA that adopts a novel anisotropic adaptive variance scaling (AAVS) technique to strengthen the performance of the traditional EDA. The AAVS-EDA not only adjusts the search scope of the EDA but also considers the improvement of main search directions. Furthermore, an auxiliary global monitor was introduced to assist the AAVS-EDA to converge to a promising area based on a shrinking variable variance if no improvement is achieved in a generation. Tang et al. [44] integrated Kalman filtering to revise the data generated by the Gaussian model to construct an accurate model. Furthermore, a learning strategy is proposed to improve the sampling operation in accordance with the sampling outcomes.

The canonical DE algorithm consists of four basic steps, including initialization, mutation, crossover, and selection. Recently, various variants of DE are developed to resolve continuous optimization and combinatorial optimization problems. DE has emerged as one of the most powerful and versatile evolutionary optimizers [45]. Although, it is difficult to classify the DE methods under a well-defined taxonomy since some of the improvements combine the multiple mechanisms together, these approaches can be roughly classified into two categories, including DE methods with strategies and control parameters adaptions and hybrid DE algorithms.

The self-adaptive differential evolution algorithm (SaDE) is proposed to address the issue of basic DE being intensely dependent on the pa-

rameters [46]. The authors present a learning strategy to choose a suitable mutation strategy among "rand/1/bin" and "current to best/2/bin" based on a probability formulation. Moreover, the crossover rate $C R$ and scale factor $F$ of the control parameters are adapted based on the success histories of the generated trial vectors. Wu et al. [47] proposed a novel variant of DE with multi-population-based ensemble of mutation strategies (MPEDE). In MPEDE, three mutation strategies, including "current-to-pbest/1", "current-to-rand/1", and "rand/1", are executed in each generation. The amount of population is regarded as a resource for rewarding the winner mutation strategy. Zhang and Sanderson [48] presented an adaptive DE with an optional external archive called JADE. In JADE, a new mutation strategy denoted "DE/current-to-pbest" with an external archive is implemented to guide the direction of the search. Furthermore, the update of the $F$ and $C R$ is performed based on a self-adaptive approach. Tanabe and Fukunaga [49] presented an improved JADE named success-history-based adaptive DE (SHADE), which updates the parameters based on the historical memory of successful parameters settings. The SHADE not only enhances the robustness of JADE but also leads to the future parameter selection. The LSHADE that adopted a linear population size reduction (LPSR) method is proposed to improve the SHADE [50]. The LPSR reduces the population size in each generation according to a linear function and alleviates the wastage of computation resources.

The blending of DE and other algorithms is an effective way to enhance the performance of an algorithm [45]. Elsayed et al. [51] hybridized differential operators of DE with real code GA to solve the problems presented in CEC 2011 competition. The hybrid technique performed the best on the competition problems. Boussaïd et al. [52] proposed a synergy between DE and biogeography-based optimization (BBO) for implementing optimal power allocation in wireless sensor networks. Li et al. [53] proposed a new hybrid algorithm based on the DE framework that integrates the key features of CMA-ES. In this algorithm, a trial vector is generated by using a DE/rand/1/bin strategy followed by an evolution path mutation of CMA-ES. Rakshit et al. [54] proposed an adaptive memetic search algorithm that uses a hybrid DE and local reinforcement learning based refiner to solve the multi-robot path planning problem. Poikolainen and Neri [55] proposed a DE variant, which combined the regular DE and Hooke-Jeeves method based local search. In this algorithm, the number of solutions Np is selected uniformly from the search space to refine and form the initial population. Then, the offspring for the next iteration is generated by using a DE mutation strategy.

The concept of the fitness landscape was proposed by Wright in 1932 to provide an intuitive picture of the evolution process of an algorithm [56]. Recently, the research on the fitness landscapes has developed rapidly not only in theory but also in the applications of optimization and machine learning. In [57], the authors reviewed the study of fitness landscape analysis techniques based on the previous works and summarized 33 methods. In addition, the random walk algorithms are often applied in fitness landscape analysis techniques to capture the structural features of space [58]. In [59], Malan et al. reviewed the random walks in general and random walks in fitness landscapes. They proposed a progressive random walk algorithm that used the multiple walks to sample neighborhood structure in continuous multi-dimensional spaces.

The fitness landscape analysis techniques are roughly classified into four categories. First, the techniques related to the modality and global structure. The local optima network (LON) is proposed by Ochoa et al. to represent the global structure of the search space [60]. The relationship between the characters of attraction basin and LON is investigated in [59]. The search trajectory network (STN) is presented by Malan et al. to visualize the behavior of different meta-heuristics [61]. The STN is established based on the data obtained from the process of the algorithm running without extra sampling. Second, the techniques that consider the ruggedness and neutrality. Malan and Engelbrecht proposed the ruggedness of information entropy (RIE) to quantify the ruggedness of continuous landscapes [62]. Vanneschi et al. proposed the measure on
neutral networks to analyze the characteristics of genetic programming Boolean landscape. Third, techniques that consider the level of searchability. The exploratory landscape analysis (ELA) of continuous search space is proposed by Mersmann et al. [63]. The six low-level features, including convexity, $y$-distribution, levelset, meta-model, local search, and curvature are defined by a sample of random solutions. The test results obtained on the BBOB'09/10 contest illustrate the successful prediction of predefined function groups. The local multiobjective landscape feature is proposed by Liefooghe et al. to solve multi-objective combinatorial optimization problems [64]. This method provides an effective way to evaluate the influence of problem features on the performance of the algorithms. In addition, the authors also study the importance of ruggedness and multimodality to describe the landscape of multi-objective combinatorial optimization problems. Lastly, the techniques that consider quantifying epistasis and deception. In [65], the maximum entropic epistasis (MEE) is proposed to quantify the interactions between the variables. The experimental results obtained by using 24 multi-dimensional continuous optimization functions show the robustness of this method. The bit-wise epistasis is proposed by Fonlup et al. to show the dependence between variables [66]. In [67], the epistasis variance is proposed as an estimate of the amount of non-linearity in the function. The epistasis variance is calculated based on a linear composition of a string solution from its bits. Despite a large number of techniques that are developed to analyze the characteristics of the fitness landscape, there are few research works that have applied the fitness landscape analysis technique for enhancing the performance of the algorithm.

Note that the offline learning is often embedded in meta-heuristics to solve the combinatorial optimization problems, such as flow-shop scheduling problem (FSP) [68-71], traveling salesman problem (TSP) [72], and job-shop scheduling problem (JSP) [73]. In [74], the fitness landscape features, and random forest are utilized for meta-learning and selecting a corresponding algorithm for different quadratic assignment problem (QAP) instances. In [75], an algorithm selection model, based on linear regression is proposed to address the timetabling problem (TTP). In [76], a multilayer perceptron classifier is combined with a wrapper meta-feature selection method to predict a suitable meta-heuristic for given vehicle routing problem (VRP) instances. A data-mining approach combined with GA and PSO is proposed in [77] to address the JSP. In [73], the apriori technique is employed to extract the rules behind the optimal schedules of JSP. In [78], supervised learning is adopted to solve the two-stage stochastic integer programming problems. In [74], artificial neural network and linear regression are utilized to minimize the mean square error between the true and predicted scenarios. In [79], the data-mining-based approach is used to solve the VRP. The authors extract the common characteristics of good solutions and used them for generating the neighbors. The offline learning combined with meta-heuristics can be performed effectively on combinatorial optimization problems. However, there are few research works that have applied meta-heuristics on complex continuous optimization problems.

The aforementioned works show that the EDA and DE have been investigated deeply in the past few years. However, the difference and relationship between EDA and DE are not considered by these works. Instead, most algorithms only focus on the algorithm itself and ignore the characteristics of the problem, thus limiting the performance of these algorithms. The combination of machine learning and evolutionary algorithms provides a suitable way of improving the performance of an algorithm. In addition, the application of the fitness landscape analysis is also helpful in designing the algorithms and for improving the performance of these algorithms. In order to enhance the adaptation of the algorithm to different problems, this work proposes a framework embedded with the fitness landscape analysis and random forest.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The framework of OLCA.

## 3. Offline learning co-evolutionary algorithm

In this section, the proposed OLCA is presented in detail. First, the algorithm portfolio containing improved GEDA and LSHADE is presented and explained in Section 3.1. Then, the implementation process of the proposed OLCA is described step by step. The general framework of the proposed OLCA is provided in Fig. 1. The pseudo-code of the proposed method is presented in Algorithm 3.

### 3.1. Algorithm portfolio

### 3.1.1. Improved GEDA

Inspired by meta-learning and no free lunch theorem, the proposed OLCA consists of two algorithms, i.e., the GEDA and the LSHADE, instead of a single algorithm for solving complex optimization problems.

Generally, EDA consists of four phases including selection, modeling, sampling, and combination. First of all, the truncation selection method is utilized in EDA to obtain a set of good individuals from the total population. The solution space is described comprehensively by the selected individuals. In the second phase, a probabilistic model is constructed based on the information extracted from the selected individuals. After modeling is completed, a set of individuals is sampled from the constructed model. In every generation, the modelled individuals and the sampled individuals are combined to obtain the offspring population.

Generally, the Gaussian model is adopted to describe the solution space in continuous EDAs [29,34,38,40,42]. The probability density
function of the Gaussian model is expressed as follows:

$$
G_{(\beta, C)}(x)=\frac{1}{(2 \pi)^{2}(\operatorname{det} C)!} e^{-\left[(x-\mu)^{T}(C)^{-1}(x-\mu)\right.}
$$

where, $x$ is an $n$-dimensional random vector, $\mu$ is the mean of $x$, and $C$ is the covariance matrix of $x$. The new $\mu$ and $C$ for the next generation are typically estimated by using the following maximum-likelihood (ML) method based on the selected solutions in the current generation:

$$
\begin{aligned}
& \mu^{\prime}=\frac{1}{\left|S^{\prime}\right|} \sum_{i=1}^{|S|^{\prime}} S_{i}^{\prime} \\
& C^{\prime}=\frac{1}{\left|S^{\prime}\right|} \sum_{i=1}^{|S|}\left(S_{i}^{\prime}-\mu^{\prime}\right)\left(S_{i}^{\prime}-\mu^{\prime}\right)^{T}
\end{aligned}
$$

where, $\left|S^{\prime}\right|$ represents the number of selected individuals, $S_{i}^{\prime}$ denotes the $i$ th solution in the selected solution set $S^{\prime}$, and the mean value of $S^{\prime}$ is represented by $\mu^{\prime}$.

There are few works presented in literature that show the employment of ML methods for estimating the Gaussian model makes the main search direction of the EDA orthogonal to the fitness improvement direction on slope-like regions [37]. This issue restricts EDA to discover a promising search area. Thus, a weighted average of candidate solutions is developed in our work to estimate the mean based on the fitness of the candidate solutions. The mean is mathematically expressed as follows:

## Algorithm 1

Linear Search Strategy.

```
Algorithm 1 Linear Search Strategy
    Input: \(\mu^{\mathrm{T}}, \delta_{1}, \delta_{2}\) and \(\eta_{\max }
    Output: \(\hat{\mu}^{\mathrm{T}}\)
    \(\hat{\mu}^{\mathrm{T}}=\mu^{\mathrm{T}}, \eta=0\)
    While \(f\left(\mu^{\mathrm{T}}+\eta\left(\delta_{1}+\delta_{2}\right)\right)<f\left(\mu^{\mathrm{T}}\right) \& \& \eta<\eta_{\max }
    \(\hat{\mu}^{\mathrm{T}}=\mu^{\mathrm{T}}+\eta\left(\delta_{1}+\delta_{2}\right)\)
    \(\eta=\eta+1\)
    end
```

$\mu^{r}=\frac{\sum_{i=1}^{|S|}\left(F I T N E S S-\operatorname{fitness}(i)\right) S_{i}^{r}}{\sum_{i=1}^{|S|}\left(F I T N E S S-\operatorname{fitness}(i)\right)}$
$F I T N E S S=\sum_{i=1}^{|S|} \operatorname{fitness}(i)$
where, $|S|^{i}$ is the number of selected individuals and $S_{i}^{r}$ denotes the $i$ th solution in the candidate solutions.

Line search is a simple algorithm that is introduced in various research to enhance or improve the performance of the algorithm [28, 80-82]. In this paper, a linear search method presented in Algorithm 1 is designed to accelerate the search process as follows:
$\delta_{1}=\mu^{r}-\mu_{0}$
$\delta_{2}=\mu^{r}-\mu_{1}$
$\bar{\mu}^{r}=\left\{\begin{array}{l}\mu^{r}+\eta\left(\delta_{1}+\delta_{2}\right) \text { if } f\left(\mu^{r}+\eta\left(\delta_{1}+\delta_{2}\right)\right)\left(f\left(\mu^{r}\right)\right. \\ \mu^{r} \text { otherwise }\end{array}\right.$
where, $\bar{\mu}^{r}$ denotes the shifted mean in the $r$ th generation. The $\bar{\mu}^{r}$ is used to generate the offspring when the estimation process is finished. $\delta_{1}$ represents the difference between $\mu^{r}$ and $\mu_{0}$ where $\mu^{r}$ is the mean of the candidate solutions and $\mu_{0}$ is the mean of the total population. $\delta_{2}$ represents the difference between $\mu^{r}$ and $\mu_{1}$, where $\mu_{1}$ represents the mean of the individuals that are not selected from the population. $\eta$ is a shifting factor that is greater than or equal to 0 . The purpose of this operation is to balance the exploration and exploitation of the algorithm and to avoid premature convergence. $\eta_{\max }$ is set to 10 in this work.

### 3.1.2. DE with the self-adaptive mechanisms

The differential evolution is a simple but effective algorithm for addressing various optimization problems and is widely used in various works [45]. The main steps of differential evolution comprise mutation, combination, and selection. DE is an evolutionary algorithm based on population. In this work, a variant of DE namely LSHADE [50], which is coevolution with GEDA, is adopted in the proposed OLCA to deal with complex optimization problems. The population in DE is expressed as follows:
$x_{i}^{g}=\left(x_{i, 1}^{g}, x_{i, 2}^{g}, x_{i, 3}^{g} \ldots x_{i, d}^{g} \ldots x_{i, D}^{g}\right)$
where, $g$ is the generation and $x_{i, g}^{g}$ is the $d$ th variable of $i$ th individuals in generation $g$. Note that each variable is in the range of domain space.
$x_{\min } \leq x_{i, d}^{g} \leq x_{\max }$
The type of distribution used in initialization of population is UNIFORM. The initial population of DE is expressed as:
$x_{i, d}^{g}=x_{\min }+r *\left(x_{\max }-x_{\min }\right)$
where, $r$ denotes a uniformly selected random number ranging from $|0$, 1]. After initialization, the mutation operator is applied on each target vector $x_{i}^{g}$ to obtain the mutant vectors. The mutant population is denoted as $V_{i}^{g}=\left\{v_{i}^{g} \mid i=1 \ldots N P\right\}$. In LSHADE, the mutation strategy $D E /$ current $t o-p b e s t / 1$ is used to generate the mutant vectors, and is expressed as follows:
$D E /$ current $-t o-p b e s t / 1: v_{i}^{g}=x_{i}^{g}+F *\left(x_{p b e s t}^{g}-x_{i}^{g}\right)+F *\left(x_{i, 1}^{g}-x_{i, 2}^{g}\right)$

Where, $r 1$ and $r 2$ are random integers in the range of $\left[1, N P_{i}, N P\right.$ is the population size and $F$ is the scale factor preset by the users. The crossover operator is exerted on the mutant vector consequently to produce the trial population. This process is mathematically expressed as follows:
$u_{i, j}^{g}=\left\{\begin{array}{c}x_{i, j}^{g} \text { if } j=j, \text { or } c r \leq C R \\ x_{i, j}^{g} \text { otherwise }\end{array}\right\}=1, \ldots, D$
where, $j_{r}$ is a random integer ranging from the $|1, D|, c r$ is a uniformly distributed random number ranging from $|0,1|$, and $C R \in|0,1|$ is the crossover rate. A selection operator is required to determine the individuals that survive in this generation and pass to the one. The offspring population is generated by using the greedy selection from the trial population and current population based on the fitness values. Because of the selection operator, the generated offspring does not become inferior. The selection operator is expressed as follows:
$X_{i}^{g}=\left\{\begin{array}{c}x_{i, j}^{g} \text { if } f\left(u_{i}^{g}\right) \leq f\left(x_{i}^{g}\right) \\ x_{i}^{g} \text { otherwise }\end{array} i=1, \ldots, N P\right.$
The differential evolution is significantly influenced by the parameters, such as scale factor $F$ and crossover rate $C R$. Therefore, the mechanism for linear population size reduction and parameter adaption based on success history are also introduced to avoid the tunning parameters by users in LSHADE. Due to the loss of diversity in the population during later iterations, the linear population reduction is an effective way to save the computation resources. The mathematical expression of this method is presented as follows:
$N^{g+1}=\operatorname{round}\left(\left(\frac{N_{\min }-N_{\max }}{\text { Max. } N f e s}\right) * \operatorname{nfes}+N_{\text {init }}\right)$
where, $N_{\text {init }}$ and $N_{\text {min }}$ represent the size of the initial population and minimum size of the population respectively. nfes and Max. Nfes are the numbers of fitness evaluations used so far and evaluations of maximum available, respectively. In addition, the parameters are selected adaptively by using the following expressions:
$C R_{i}^{r}=\operatorname{randn}\left(M_{C R, r,}, 0.1\right)$
$F_{i}^{g}=\operatorname{randc}\left(M_{F, c}, 0.1\right)$
where, randn and randc are the random numbers that obey the Gaussian distribution and Cauchy distribution, respectively, and the standard deviations of both distributions are all set to $0.1 . M_{C R}$ and $M_{F}$ represent the parameters of length $H$ stored in the historical memory archive that performed efficiently in the past, and the initial values of $M_{C R}$ and $M_{F}$ are 0.5. For each individual, the parameters $F$ and $C R$ are selected from the memory archive and $r_{i}$ is the index that ranges from $|1, H|$. In each generation, if a trial individual $u_{i}^{g}$ survives to the next generation, the corresponding $F$ and $C R$ are regarded as successful and denoted as $S_{F}$ and $S_{C R}$, separately. The memory update at the end of generation is expressed as follows:
$M_{C R, k}^{g+1}=\left\{\begin{array}{c}\operatorname{mean}_{W A}\left(S_{C R}\right) \text { if } S_{C R} \neq \varnothing \\ M_{C R, k}^{g} \text {, otherwise }\end{array}\right.$
where, mean $_{\text {WA }}\left(S_{C R}\right)$ is the weighted arithmetic mean generated by using the following expression:
$\operatorname{mean}_{\text {WA }}\left(S_{C R}\right)=\sum_{k=1}^{N_{w A}} \omega_{k} * S_{C R, k}$
$\omega_{k}$ is computed as:
$\omega_{k}=\frac{\Delta f_{k}}{\sum_{k=1}^{N_{w A}} \Delta f_{k}}$
$\Delta f_{k}=\left|f\left(u_{k}^{g}\right)-f\left(x_{k}^{g}\right)\right|$
The update of $F$ memory is performed as follows:

![img-1.jpeg](img-1.jpeg)

Fig. 2. RIE values of different functions on 10D.
$M_{F, k}^{i+1}=\left\{\begin{array}{l}\text { mean }_{N L}\left(S_{F}\right) \text { if } S_{F} \neq \varnothing \\ M_{F, k}^{i} \text { otherwise }\end{array}\right.$
where, mean ${ }_{N L}\left(S_{F}\right)$ denotes the Lehmer mean and is computed as follows:
$\operatorname{mean}_{N L}\left(S_{F}\right)=\frac{\sum_{k=1}^{|S_{F}|} \omega_{k} * S_{F, k}^{2}}{\sum_{k=1}^{|S_{F}|} \omega_{k} * S_{F, k}}$
where, $k$ is the index that determines the position of the parameters in the historical memory.

### 3.2. The implementation of the proposed OLCA

### 3.2.1. The framework of OLCA

The framework of OLCA comprises two stages, i.e., the training phase and the testing phase. A random forest [83] is used for training and testing. It is a critical component of OLCA, which has learning and predicting functions. The random forest, which is introduced by Breiman in 2001 for the first time [84], is a collection of classification and regression trees [85]. It is a simple model that using binary splits on
predictor variables to determine outcome predictions. In a random forest, many classification and regression trees are built by utilizing randomly selected training datasets and random subsets of predictor variables to model outcomes. The final results of random forest are determined by aggregating the results of each decision tree and a prediction for each observation is given. The version of random forest used in this work is C4.5, which is an extended form of ID3 [86]. The details of C4.5 is described in Section 3.2.4.

During the training phase, a random walk is used to obtain various landscape points in the domain space. Subsequently, the ruggedness of information entropy is calculated by using these landscape points. GEDA and LSHADE are used as the training functions to determine the training label, i.e., 1 or 2 , for a certain function according to the final results of the two algorithms. Then, the landscape features and training labels are used to establish the problem-algorithm mapping and to form the complete training set. The training process of training is continued until all the decision trees in the random forest are formed.

During the testing phase, a random walk is first applied to the testing functions to obtain new landscape points in the domain space. Then, the ruggedness of information entropy is calculated to form the testing set. The prediction labels are obtained by using the trained random forest

# Algorithm 2 

Random Increasing Walk.

## Algorithm 2 Random Increasing Walk

```
Input: Dimensions, Domain ([-100,100]), Walk Steps = 3000, StepSize = 10
Output: A walk sequence
Initiative an empty array for storing the walk
Produce a random position for the walk (walk[0])
    count \(=0\)
    while count < Walk Steps
    for \(i=1\) : Dimensions
        Generate a random number step in the range [0, Step Size]
        Set walk [count] \(_{i}=\) walk [count] \(_{i-1}+\) step
        If walk [count] \(_{i}\) beyond the maximum bound
        Set walk [count] \(_{i}=\) walk [count] \(_{i}-200\)
        count \(=\) count +1
    end
end
end
```

model.

### 3.2.2. Training samples and testing instances

In order to avoid overfitting, 45 benchmark functions containing 30 CEC 2014 [87] functions and 15 CEC 2015 functions [88] are used to train the random forest, and 30 CEC 2017 [89] functions are used to verify the generalization performance of the random forest model. The CEC benchmark functions are composed of unimodal functions, simple multimodal functions, hybrid functions, and composition functions. These functions have different characteristics and are used to calculate the fitness landscape. They are used for training the random forest.

### 3.2.3. Fitness landscape evaluation

It is difficult to compute a global fitness landscape. Usually, the local fitness landscape is calculated by sampling or random walk in the

Feature Vector $=\left\{H(0), H\left(\frac{\varepsilon^{c}}{128}\right), H\left(\frac{\varepsilon^{c}}{64}\right), H\left(\frac{\varepsilon^{c}}{32}\right), H\left(\frac{\varepsilon^{c}}{16}\right), H\left(\frac{\varepsilon^{c}}{8}\right), H\left(\frac{\varepsilon^{c}}{4}\right), H\left(\frac{\varepsilon^{c}}{2}\right), H\left(\varepsilon^{c}\right)\right\}$
domain space. The ruggedness of information entropy (RIE) adopted in this work is related to the number and distribution of the local optima [62].

The random walk method is used to obtain the fitness features RIE. In this work, the population size of each training function is set to $10 \times D$, and the walk steps and step size are set to 3000 and 10 , respectively. Furthermore, the search domain space is $|-100,100|^{D}$ and the number of evaluations is set to $10^{4} D$, where $D$ is the dimension of the problem.

The method is trained for 30 times independently and the mean value of 30 results are reserved. The ruggedness of information entropy values for 45 training functions are presented in Fig. 2. Although each function has a different curve, similarities exist in the RIE curve of functions that have the same characters. Similarities contribute to the classification of the training set. Therefore, a feature vector consisting of entropy values that comprise nine different values of $\varepsilon$ values form a training sample. The $\varepsilon$ is an important parameter that determines the sensitivity of $H(\varepsilon)$ for different landscapes, where $H$ is the entropy. The random walk strategy used in this work is shown in Algorithm 2. The RIE values for each 10D training function are shown in Fig. 2. The landscape feature vector described in (24) is produced by the ruggedness of information entropy.

### 3.2.4. Training and testing on benchmark

In the proposed OLCA, a random forest is adopted to construct the problem-algorithm mapping on training functions and predict the problem-algorithm mapping for new problem instances. In this work, a C4.5, decision tree that is appropriate for performing classification of continuous features is adopted to construct the random forest. As aforementioned, C4.5 is an improvement version of ID3 algorithm [90]. In C4.5, the information Gain ratio criterion is adopted for decision tree

Table 1
The optimal strategy for training functions.
# Algorithm 3 

OLCA.

## Algorithm 3 OLCA

Set $N P_{Z D A}=4000, \tau=0.3 ; M_{C B}=M_{F}=0.5, A r c h i v e=\varphi, g=1, N P_{G B}^{\max }=180 \times D$;
steps $=3000 ;$ size $=10$
Generate the initial population $\boldsymbol{X}=\left[\boldsymbol{x}_{1}, \boldsymbol{x}_{2}, \boldsymbol{x}_{3} \ldots \boldsymbol{x}_{t} \ldots \boldsymbol{x}_{D}\right]$
Gbest is used to store the best results
Perform a random walk to obtain points in the domain space according to Algorithm 2
Calculate the fitness landscape feature vector according to obtained points
Predict strategy by trained random forest and produce the prediction labels $\{1,2\}$
$n f e s=0, \max _{,} n f e s=10^{4}+D$
While $n f e s \leq \max _{,} n f e s$
if label $=1$
Produce the best $[\tau \times N P]$ solutions by truncation selection
Estimate the mean value by Eq. (4) and (5)
Perform Algorithm 1
Estimate the covariance matrix by Eq. (3)
Generate the new population by the Gaussian model
else (label $=2$ )
$S_{C B}=\varphi ; S_{F}=\varphi$
$r_{i}=$ Select from $[1, H]$ randomly
$C R_{i}^{Z}=\operatorname{randn}\left(M_{C B, r_{i}}, 0.1\right) ; F_{i}^{Z}=\operatorname{randc}\left(M_{F, r_{i}}, 0.1\right)$
Generate the mutant vector by $D E /$ current $\sim$ to $\sim$ pbest $/ 1$
Generate the trial vector
Perform the selection operator
Update $M_{C B}$ and $M_{F}$ based on $S_{C B}, S_{F}$;
Perform the LPSR [50]
end
end
end
$n f e s=n f e s+N P$
return $G b e s t$
classification instead of Gain split criterion [86]. Unlike random forest that builds a few thousand classification trees, C4.5 takes the training data and generates a single tree, and modifies the internal structure leading to a substantial reduction in computational resource and energy usage [91].

In this work, two algorithms are considered as strategies including GEDA and LSHADE to solve the optimization problems. These algorithms are trained on 45 benchmark functions for 51 times independently to identify a suitable algorithm for a certain benchmark problem. The mean value and standard variation are calculated on the training functions with dimensions of $10,30,50$, and 100 . The existence of a significant difference between the two algorithms on a function is identified by using the Friedman-test. As shown in Table 1, both algorithms might perform similarly, which is represented as " $1,2^{\prime \prime}$, on certain functions. Note that only one label (i.e. " 1 " or " 2 ") is selected randomly for training. In Table 1, " 1 " denotes that GEDA obtained better results as compared to LSHADE, and vice versa.

During the testing phase, the landscape features of testing functions are obtained by using the random walk before the execution of the algorithm. Subsequently, an algorithm is predicted for each testing function by classifying the landscape features using trained random forest.

## 4. Experimental results and analysis

### 4.1. Experimental environment and parameter settings

In order to verify the performance of the proposed OLCA, experiments are performed by using the CEC 2017 benchmark functions with different dimensions. The adopted benchmark test suite includes four types of functions including unimodal functions $\left(f_{1} \sim f_{5}\right)$, simple multimodal functions $\left(f_{4} \sim f_{10}\right)$, hybrid functions $\left(f_{11} \sim f_{20}\right)$, and composition functions $\left(f_{21} \sim f_{50}\right)$. It is difficult to find the global optima for the composition functions, which are characterized by multi-modal, non-separable, asymmetrical, processing different properties around different local optima, and different properties for different variable subcomponents. For the sake of fairness, all of the algorithms are executed for the same number of fitness evaluations (MaxFEs is set to 10000

Table 2
The ANOVA results of parameters.
$D$, where $D$ is the dimension) In Algorithm 3, note that the number of evaluations consumed in the calculation of RIE is subtracted from the total number of evaluations. The calculation of RIE can refer to [62]. In addition, we run the process 51 times independently on each function. The experiments are conducted on Microsoft Windows Server 2019 Standard 64-bit Opening System, 2.30 GHz CPU, and PC 64GB of RAM. The programming language is MATLAB 2016a. The source code of OLCA can be downloaded at https://github.com/OmertaZB/Algorithms.git.

We use few state-of-the-art algorithms for performing comparisons. These algorithms include CMA-ES (which is well known in the research community) [92], jSO (which performed well on CEC 2017) [93], LSHADE (which performed well on CEC 2014) [54], iL-SHADE [94], AAVS-EDA [57], PBILc [95], and cDE/EDA [96]. In addition, note that to verify the effectiveness of the random forest on OLCA, the random selection method is utilized to replace the random forest of OLCA namely RSCA is also included in the comparison algorithms.

In this work, the mean value (Mean), and the standard deviation (Std) metrics are adopted as the evaluation criterion. The search capability of the algorithms is reflected by the Mean and the stability of algorithms is represented by Std. The smaller mean or standard deviation represents a better performance. The Std is compared when the mean values of two compared algorithms are the same. The best results are represented in bold. Note that the error value is taken as zero if it is smaller than $10^{-8}$.

![img-2.jpeg](img-2.jpeg)
(a) The Main effects plot.

Fig. 3. Parameter analysis for the OLCA. (a) The Main effects plot. (b) The Interaction plot.

### 4.2. Parameters analysis

In this section, the design of the experiment (DOE) [97] is used to analyze the control parameters. The parameters of DE are adopted from the previous works because the parameters of this type of DE are determined by self-adaption and are executed without manual tuning. Therefore, the critical parameters of the proposed OLCA include population size $(N P)$ and truncation rate $\tau$ of EDA, and the number of decision trees in the random forest $(N T)$. The levels of the chosen parameters are listed as follows: $N P=\{1000.2000 .3000 .4000 .5000 .6000\}, \tau=$ $\{0.1 .0 .2 .0 .3 .0 .4 .0 .5\}$, and $N T=\{2.10 .30 .50 .100\}$. Therefore, there are $6 \times 5 \times 5=150$ combinations of parameters. Each combination contains 30 functions and is executed for runs 30 times. The iterations continue till the termination criterion (exhaustion of maximum functional evaluations) is satisfied. The multifactor analysis of variance (ANOVA), which tests the significance of the difference between two or more samples, is adopted to investigate the experimental results.

As illustrated in Table 2, the two $p$-values of the population size $(N P)$ and $\tau$ are smaller than 0.05 , which means that the adjustment of the two parameters is leads to a significant change in the algorithm with a $95 \%$ confidence level. Moreover, there is an interaction effect between $N P$ and $\tau$. The analysis of parameters for the OLCA, such as the figure of main effects and the interaction figure is shown in Fig. 3. As shown in Fig. 3(a), the best results are obtained when the population size $(N P)$ is set to 4000 , whereas the worst results are obtained when the $N P$ is 1000 , and neutral results are obtained for other settings. The small population size leads to inferior results due to poor diversity of the population. On the other hand, the wastage of computation resources in each iteration if the population size is too large. For the truncation rate $\tau, 0.3$ is the best selection as shown in Fig. 3(a) and the results are worse, $\tau$ has a different value. The truncation rate is critical to the EDA and determines the quality and quantity of the selected solutions. The quality of the selected solutions is ensured if $\tau$ is small. However, the population diversity is lost, which may lead to the algorithm being prone to the local optima. Conversely, the search efficiency is lower if $\tau$ is too large. Although a large $\tau$ enables the algorithm to avoid the local optima, the accuracy of the model is reduced due to more inferior solutions contained in the selected solutions. The algorithm performs effectively if the parameters setting of $N P$ and $\tau$ are 4000 and 0.3 , respectively, as illustrated in the interaction figure. These results match with the results of the main effects plot. In Fig. 3(a), the optimal results are obtained when the number of decision trees is set to 10 , which is not a key parameter according to the ANOVA. Therefore, the optimal combination of the control parameters is $N P=4000, \tau=0.3$, and $N T=10$.

### 4.3. Performance comparison

In order to verify the performance of the proposed OLCA, the simulation are performed by using the CEC2017 benchmark functions. The comparison algorithms include CMA-ES, jSO, LSHADE, iL-SHADE, AAVS-EDA, PBILc, cDE/EDA, and RSCA. The experimental results on

100D are shown in Table 3 and the results for 10D, 30D, and 50D are present in Tables S4-S6 in the supplementary material. W/L/T, i.e. win/ loss/tie, denotes that the other competitor performed better than, worse than, or equal compared with the proposed OLCA on the benchmark test suite.

The comparison results of 9 algorithms on 10D are shown in Table S4. For 3 unimodal functions, the OLCA converges to the global optimal similar to CMA-ES, jSO, LSHADE, iL-SAHDE, and RSCA. AAVSEDA converges to the global value on $f_{2}$ and $f_{3}$. cDE/EDA converges to the global value on $f_{3}$. The performance of the proposed OLCA on all the unimodal functions is always better than or equal to the performance of the compared algorithms. The results show that the proposed OLCA has a strong local search capability. On multimodal functions $f_{4} \sim f_{10}$, the proposed OLCA achieves the best performance. CMA-ES, jSO, LSHADE, iL-SHADE, and RSCA also converge to the global optimum on $f_{4}$. The performance of jSO, LSHADE, iL-SHADE, and PBILc on $f_{6}$ is as good as the performance of OLCA. PBILc also performs well on $f_{7}$. AAVS-EDA converges to the global optimum on $f_{8}$. On $f_{9}$, LSHADE, iL-SAHDE, cDE/EDA, RSCA, and OLCA performed well. The optimization results illustrate that the proposed OLCA performed better than the compared algorithms in terms of global search capability. The OLCA performed best on most of the hybrid functions except $f_{12}, f_{13}$, and $f_{19}$.

The iL-SHADE, jSO and RSCA also obtain the optimal solution on $f_{11}$. The performance of jSO on $f_{12}$ is the best. AAVS-EDA performs better than the other compared algorithms on $f_{13}$. On $f_{19}$, the LSHADE has the best performance. On the composition functions $f_{21} \sim f_{30}$, the performance of the OLCA is still competitive. jSO performs best on $f_{21}$. All the algorithms obtain the same results on $f_{22}$. The proposed OLCA performs best on $f_{23}$.

On $f_{24}$, the CMA-ES performs much better as compared to the other algorithms. The performance of AAVS-EDA on $f_{25}$ is better as compared to the others algorithms. On $f_{26}$, the CMA-ES also performs well. The cDE/EDA performs best for $f_{27}$. The AAVS-EDA obtains a better solution as compared to the other algorithms on $f_{28}$. The proposed OLCA performs well on $f_{29}$. The CMA-ES has the best performance on $f_{30}$. In short, the OLCA performs efficiently well as a whole and has a superior performance to other algorithms. Moreover, the proposed OLCA is competitive when compared with algorithms such as jSO and CMA-ES.

In order to further verify the performance of the proposed OLCA, it is compared with CMA-ES, jSO, LSHADE, iL-SAHDE, AAVS-EDA, PBILc, cDE/EDA, and RSCA on 30D, 50D, and 100D respectively. As illustrated in Tables S5 and S6, CMA-ES, jSO, LSHADE, RSCA, and OLCA perform well with 30D and 50D on the unimodal functions. Considering the problems with 100D, only CMA-ES is able to obtain the global optimum for all the unimodal functions. jSO and LSHADE perform well on $f_{1}$. RSCA and OLCA converge to the global optimum on $f_{1}$ and $f_{3}$. On the problems with 30D, the proposed OLCA performs well on the multimodal and hybrid functions as compared to the other methods. Although jSO, LSHADE, AAVS-EDA, and RSCA perform well on several functions among these two types of problems, their performance as a whole is worse than the proposed OLCA. On the problems with 50D and 100D,

Table 3
Comparison results on 100D benchmark functions.
the proposed OLCA is the most competitive on multimodal functions, hybrid functions, and composition functions. As illustrated by the mean and std values presented in Tables 3 and 54-56, the statistical results show that the proposed OLCA obtains better performance on benchmark functions. No algorithm performs the best on all problems according to the no free lunch theorem. The proposed OLCA shows good performance on several problems and is competitive as compared with the other algorithms.

In summary, the proposed OLCA is competitive compared with its competitors which contain the state-of-the-art. This kind of performance
mainly profits from the combination of the random forest and the fitness landscape analysis. The knowledge that is implied in the fitness landscape is utilized in the algorithm procedure. Therefore, the proposed OLCA can select the appropriate method to adapt to distinct problems.

### 4.4. Behavior analysis of the proposed OLCA

In this work, an experiment is conducted to analyze the search behavior and visualize the execution process of the proposed OLCA for two-dimensional benchmark functions. The execution details of the al-

![img-3.jpeg](img-3.jpeg)

Fig. 4. The convergence curves plot on 10D, 30D, 50D, 100D.
gorithm such as convergence speed and diversity of the population are presented in Figs. 6-8. The fitness landscape figures for $f_{1}, f_{2}, f_{4}, f_{10}, f_{22}$, and $f_{28}$ are also presented to illustrate the search behavior of OLCA. Moreover, the stereogram and planform of each function are also displayed to understand the running process intuitively. The population of OLCA is marked by the red dots. $f_{1}$ and $f_{2}$ are unimodal functions that easily find the global optimal generally. $f_{4}$ and $f_{10}$ are multimodal functions that are unable to find the global optima easily due to the plenty of peaks and valleys. $f_{22}$ and $f_{28}$ denote the composition functions that are unable to obtain the global optima easily because of various attraction basins.

As shown in Fig. 6, $f_{1}$ is a unimodal function with a non-separable, smooth, but narrow ridge. It is difficult to optimize $f_{1}$ for algorithms, which have a poor local search ability, such as PBILc. On the contrary, the proposed OLCA performs well on $f_{1}$ due to good local search ability of EDA and DE. Note that the proposed OLCA has good performance on $f_{1}$ regardless of which component (EDA or DE) is executed. The only difference is that the EDA rapidly converges to the optima while the convergence speed of DE is slow. $f_{2}$ is a unimodal function that is nonseparable and symmetric. The fitness landscape with symmetric rotation of the coordinate system leads to severe algorithmic performance losses [98]. The proposed OLCA has good performance on $f_{2}$ as EDA and DE are insusceptible to coordinate system rotation. Similarly, the convergence speed of the algorithm is fast if the EDA component is executed. It is noteworthy that the proposed OLCA performs much better than some algorithms, such as AAVS_EDA, PBILc, and cDE/EDA, on $f_{2}$ for higher dimensions. $f_{4}$ is a multi-modal function that is a non-separable and has a large number of local optima. The proposed OLCA performs well on $f_{4}$ as the population diversity of the DE component is maintained during the evolution process. $f_{10}$ is a
multi-modal function that is a non-separable and possesses a large number of local optima. In addition, the second better local optimum is far from the global optimum. Note that a high population diversity of an algorithm is required for this type of function. As shown in Fig. 7, the population diversity of EDA is lost due to the rapid reduction in the variance, which makes it far from the global optimum. In contrast, the defect in the DEA is complemented by the DE component. The DE explores multiple attraction basins with the help of mutation and crossover operators, thus enabling it to find the global optimum. In Fig. 8, $f_{22}$ is a composition function, which is multi-modal, non-separable, asymmetrical, and possesses different properties around different local optima.

As shown in the stereogram, there are two attraction basins in the fitness landscape and the global optima lie in the small basin. It is difficult for the EDA to cross the area between the two basins since most individuals in the population in EDA are trapped in the large basin, thus making it difficult to shift the center of the population to a promising area. The location of the mean determines if it is possible to find the global optimum since the population of EDA is generated around the mean. On the contrary, the DE is less affected by the attraction basin as compared to the EDA. Similarly, $f_{28}$ has the same properties as $f_{22}$. The global optimum is hard to discover by the EDA due to the existence of various attraction basins. As compared to EDA, the DE has the advantage of dividing the population automatically. This allows DE to explore different areas of the search space and discover the global optimum. Note that the properties of the fitness landscape are changed with an increase in the number of dimensions. The number of local optima increases exponentially and the difficulty of finding the global optimum increases significantly due to the curse of dimensionality.

In short, the EDA and DE are two algorithms that possess different characteristics. In the proposed framework, the diversity of the

![img-4.jpeg](img-4.jpeg)

Fig. 5. The box plot on 10D, 30D, 50D, 100D.
algorithms is helpful to solve the problems that have various features. The different characteristics of EDA and DE are exploited to discover the global optimum in a large-scale search space.

### 4.5. Effect of random forest on OLCA

In this section, the contribution of random forest in the performance of the proposed OLCA is analyzed. The RSCA as a variant of OLCA adopts random selection for selecting EDA and DE as compared with other algorithms discussed in Section 4.3. As presented in Tables 3 and S4-S6, the performance of the proposed OLCA is better as compared to the RSCA in all dimensions as the selection mechanism of random forest based on fitness landscape analysis has made a correct decision with a
high probability to select a suitable strategy to solve the problem. Note that a single selection method is unable to make the right decision every time. As the algorithm adopts a mechanism that possesses the guidance information, such as fitness landscape rather than a random operation, the performance of the algorithm is overall good. In Fig. 9, the proposed OLCA denoted by a red dotted line is below the RSCA denoted by a blue solid line, especially for $f_{b}, f_{b}$, and $f_{20}$. As shown in Fig. 9, the two lines are close to each other because the two algorithms, including EDA and DE, have a good performance in solving several problems, i.e., the performance of RSCA based on random selection is good as well. As described in section 3.5, the behaviors of the two algorithms are complementary, which means that the two algorithms play their respective roles in different problems.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Stereogram and planform of unimodal functions.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Stereogram and planform of DE running on multimodal functions.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Stereogram and planform of DE running on compositions functions.
![img-8.jpeg](img-8.jpeg)

Fig. 9. Comparison between OLCA and RSCA on 30 functions.

### 4.6. Convergence and stability comparison

In order to further elucidate the convergence speed and stability of the proposed OLCA, one function is selected from each type of benchmark function to plot the convergence speed curves and box plot. According to the definition of CEC 2017, fourteen data samples are selected
from the original experimental results to plot the convergence speed curves. After obtaining the logarithm of the error values, i.e., along longitudinal coordinate-axis $y$, some curves vanish from some point if the data is zero. In order to avoid this situation, the last non-zero data is used to replace those data points that reach zero. Note that some algorithms obtain the predefined accuracy instead of being stagnate. As

![img-9.jpeg](img-9.jpeg)

Fig. 10. The Friedman test results of 100.
shown in Fig. 4, the proposed OLCA denoted as a red line, has a good performance in terms of convergence. Although, there are some algorithms that converge faster than the proposed OLCA, the quality of convergence is worse than the proposed OLCA. A significant distinction is that the proposed OLCA still tries to find the global optimum while the others algorithms converge to the local optima. This occurs during the later stages of these algorithms. The results show that some algorithms are prone to premature convergence and fall into stagnation due to the monotonous mechanism. Generally, an algorithm performs well on some functions while it performs unsatisfactory on others. The proposed OLCA predicts a suitable strategy based on the fitness landscape information to discover a better solution. Fig. 5 presents the box plots that show the stability of the algorithms. One function is selected from each type of benchmark function to perform comparisons. The stability of the proposed OLCA is effective for the four types of benchmark functions. The good stability indicates that a good solution is frequently obtained by the algorithm rather than obtaining it occasionally in each iteration. In addition, the other convergence speed curves and box plots are presented in Figs S1-S8 in the supplementary material.

### 4.7. Non-parametric test

In this section, the non-parametric test, i.e., Friedman and Wilcoxon tests are performed to further assess the proposed OLCA. The Friedman test is a nonparametric statistical method for determining the significant differences in multiple related samples [99]. As shown in Fig. 10 and the Fig. S9 of supplementary information, the mean rank of the OLCA is the smallest in all dimensions, which means that the performance of this algorithm is the best. Note that there is a significant difference between the proposed OLCA and CMA-ES, AAVS-EDA, PBILc, and cDE/EDA with a $90 \%$ confidence level. In addition, there is a significant difference between the proposed OLCA and CMA-ES, PBILc, and cDE/EDA under the $95 \%$ confidence level. Considering the 30-dimensional problems, the mean rank of the OLCA is minimum. Under the $90 \%$ confidence level, the difference between the proposed OLCA and CMA-ES, AAVS-EDA, PBILc, and cDE/EDA is significant. Under the $95 \%$ confidence level, the test results are the same as under the confidence level is $90 \%$. The difference between OLCA and the other algorithms is significant under $90 \%$ confidence level in the 50-dimensional problems. The results show that
only the mean rank of the proposed OLCA is below the critical differences represented by the solid and the dotted lines. Moreover, the results also show that the OLCA performs well on the 50-dimensional problems. As presented in Fig. S9, there exists a significant difference between the proposed OLCA and LSHADE, AAVS-EDA, PBILc, and cDE/EDA in case of 100-dimensional problems, no matter what the confidence level is. On the contrary, there is no significant difference between the OLCA and CMA-ES under the two confidence levels. Note that the mean rank of the proposed OLCA is still smaller as compared to the other algorithms. In conclusion, the OLCA is competitive as compared with its competitors.

The results of the Wilcoxon sign rank test are shown in Tables 4 and S1-S3 of the supplementary material. In Table 4, the number of positive ranks is represented by $R+$ which means the number of compared algorithms that are worse than the proposed OLCA is $R+$. Meanwhile, the number of the negative ranks is represented by $R$ - which means there are $R$ - comparison algorithms that are superior to the OLCA. As shown in Tables 4 and S1-S3, there exists a significant difference in a pairwise algorithm if the $p$-value is smaller than $\alpha$, which is represented by Yes. In case of the 10 and 30-dimensional problems, the proposed OLCA is significantly better as compared to some algorithms but is not significantly better than some other algorithms such as jSO, LSHADE, iL SHADE, and AAVS-EDA. The performance of the proposed OLCA is significantly better than the compared algorithms for the 50- and 100dimensional problems.

In summary, the OLCA is feasible and better than the compared algorithms in solving the benchmark test suite. As compared with other algorithms, this framework of algorithms solves the problem at a higher level, i.e., algorithms are strategies, rather than tuning the parameters of an algorithm or several operators of the algorithm. In addition, the fitness landscape information without prior knowledge about the global optimum is utilized to guide the selection of strategies in the framework. Two algorithms that possess different characteristics are adopted to discover the global optimum. A complementation exists in the two algorithms contributing to the algorithm for solving the problems that have different features.

### 4.8. IEEE CEC2011 real-world benchmark problems test

In this subsection, the capability of the proposed OLCA is further assessed based on the nineteen real-world benchmark problems selected from IEEE CEC 2011. These benchmarks are adopted widely by the researchers for measuring the performance of algorithms proposed for solving the practical problems. The details of nineteen selected benchmark problems from IEEE CEC 2011 are presented in Table S7 of the supplementary materials. The definition of these functions and other details are presented in [100].

The proposed OLCA is compared with state-of-the-art algorithms by using the IEEE CEC 2011 real-world benchmark problems including GA with a new multi-parent crossover (GA-MPC), adaptive differential evolution with optional external archive (JADE), jSO, AAVS-EDA, EDcDE, LSHADE, iL-SHADE, and DE. The parameters of the compared algorithms are obtained from the original works. In order to ensure a fair comparison, all the compared algorithms are simulated by using the same hardware and software configurations. Moreover, all the compared algorithms are executed for 25 epochs independently, and the

Table 4
$p$-value of Wilcoxon's rank-sum test for $D=10$.
Table 5
The statistical results of Wilcoxon's rank-sum test.

Table 6
Comparison results on IEEE CEC 2011 problems.
maximum number of fitness evaluations is set as 150,000 .
A detailed comparison between the proposed OLCA and other counterparts on nineteen real-world problems is shown in Table 6, including Mean and Std values for each function. The statistical results show that the proposed OLCA is superior to GA-MPC which is the winner of IEEE CEC 2011 real-world benchmark problems on 12 functions. The proposed OLCA wins JADE on 16 functions but loses on 1 function. Note that there is a significant difference between the proposed OLCA and JADE in statistical terms. The proposed OLCA outperforms jSO on 9 functions, but it is worse than jSO on 8 functions and shows a tie on 2 functions. Although there is no significant difference between OLCA, LSHADE, and jSO, the proposed OLCA is competitive as compared with LHSADE and jSO, which is the winner of IEEE CEC 2017 benchmark problems. The proposed OLCA performs better on 12 functions as compared with the iL-SHADE. The OLCA is better than AAVS-EDA on 18 functions but loses on 1 function. As compared with cDE/EDA, the
![img-10.jpeg](img-10.jpeg)

Fig. 11. The Friedman test results of compared algorithms on IEEE CEC 2011.

![img-11.jpeg](img-11.jpeg)

Fig. 12. The convergence curves plot of compared algorithms on IEEE CEC 2011.
![img-12.jpeg](img-12.jpeg)

Fig. 13. The box plot of compared algorithms on IEEE CEC 2011.
proposed OLCA shows a superior performance on 18 functions but it has a poor performance on one function. It is noteworthy that the proposed OLCA does not fail against DE on any function.

Table 5 shows the comparison results between the proposed OLCA and other advanced methods based on the Wilcoxon's rank-sum test with a significance level of 0.05 and 0.1 . Although there is no significant difference between the proposed OLCA and some of its competitors (GAMPC, LSHADE, iL-SHADE, and jSO), the OLCA performs well on certain problems. The Friedman test results of all the competitors are demonstrated in Fig. 11. The results show that the proposed OLCA attains the lowest ranking score with 1.84 and has the best performance. All these statistical results illustrate the effectiveness of the proposed OLCA in solving the real-world optimization problems. Based on the convergence curves reported in Fig. 12, it is evident that found that the proposed OLCA performs well on certain problems. The OLCA focuses on the selection of a suitable algorithm for certain problems instead of improving the part of an algorithm. Consequently, the convergence speed of the OLCA is not the best. Similarly, the stability of the proposed OLCA is competitive as compared with other algorithms rather than being the best as illustrated by the boxplots presented in Fig. 13. The other convergence speed curves and box plots are presented in Figs. S10 and S11 in the supplementary material.

Note that the real-world benchmark problems are more challenging to solve as compared to the benchmark functions, such as IEEE CEC 2017. However, the proposed OLCA performs well on these problems as well. There are two main reasons for this performance. First, the two algorithms with different advantages are integrated in the proposed framework of OLCA to boost the adaptability of OLCA for different problems. Secondly, the fitness landscape analysis technique is employed to extract the problem-specific knowledge for the selection of
algorithms for different problems. Furthermore, the machine learning techniques are applied for training the OLCA to establish the problemalgorithm mapping and predict a suitable method for a new problem.

## 5. Conclusions and future work

In this work, an offline learning co-evolutionary algorithm (OLCA) based on the fitness landscape is proposed to address the complex continuous optimization problems. The visualization of executing the algorithms is displayed and utilized to analyze the search behavior of the proposed OLCA. The OLCA is tested on CEC 2017 benchmark test suite to verify the performance and compared with several state-of-the-art algorithms. The mean value and standard variance illustrate that the OLCA is competitive. The non-parametric test is performed to analyze the statistical differences between the pairing algorithms. The test results show that there is a significant difference between the proposed OLCA and compared algorithms. Moreover, the proposed OLCA is tested on CEC 2011 real-world benchmark problems. The results demonstrate that OLCA is competitive as compared with some advanced algorithms. This is because each algorithm is selected as a strategy in the framework and, the performance of the proposed OLCA is dependent on each algorithm. The performance of the OLCA is limited if the selected algorithms selected are similar in terms of searching behavior. In summary, the proposed OLCA is an effective algorithm.

In future work, the framework proposed in this work can be further extended on other algorithms and machine learning models. The integration of other algorithms, mechanisms, and strategies will enhance the performance of the proposed algorithm. The selection of an efficient machine learning model is important for improving the search capability of intelligent algorithms. Moreover, it is a challenging to apply the

fitness landscape analysis technique in practice. The introduction of the fitness landscape contributes in solving the complex problems. In addition, the visualization analysis of algorithms is an interesting direction and helps to design a more efficient algorithm. Furthermore, the performance of the proposed OLCA needs further verification on practical problems.

## CRediT authorship contribution statement

Fuqing Zhao: Funding acquisition, Investigation, Supervision. Bo Zhu: Investigation, Software, Writing - original draft. Ling Wang: Methodology, Resources. Tianpeng Xu: Project administration, Writing - review \& editing. Ningning Zhu: Conceptualization, Formal analysis. Jonrinaldi Jonrinaldi: Visualization.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work was financially supported by the National Natural Science Foundation of China under grant 62063021. It was also supported by the Key talent project of Gansu Province (ZZ2021G50700016), the Key Research Programs of Science and Technology Commission Foundation of Gansu Province (21YF5WA086), Lanzhou Science Bureau project (2018-rc-98), and Project of Gansu Natural Science Foundation (21JR7RA204) , respectively.

## Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.swevo.2022.101148.
