# A Gaussian Estimation of Distribution Algorithm With Random Walk Strategies and Its Application in Optimal Missile Guidance Handover for Multi-UCAV in Over-the-Horizon Air Combat 

XIAOFEI WANG ${ }^{\odot}$, HUI ZHAO, TONG HAN, ZHENGLEI WEI ${ }^{\odot}$, YAJUN LIANG ${ }^{\odot}$, AND YINGTONG LI<br>Institute of Aeronautics Engineering, Air Force Engineering University, Xi'an 710038, China<br>Corresponding author: Xiaofei Wang (wxf825421673@163.com)

This work was supported in part by the National Natural Science Foundation of China under Grant 61601505, in part by the Natural Science Foundation of Shaanxi Province under Grant 2016JQ6050 and Grant 2017JM6078, and in part by the Aeronautical Science Foundation of China under Grant 20155196022 and Grant 20175196019.


#### Abstract

To overcome the premature convergence caused by the ill-distribution of solutions in the basic Gaussian estimation of distribution algorithm (GEDA), this paper explores a novel GEDA variant with random walk strategies, namely RW-GEDA. In RW-GEDA, the weighted maximum likelihood estimation method is used to estimate the Gaussian distribution. The new candidates are sampled using a shifted mean to enhance exploration performance. When the algorithm stagnates, two random walk strategies, namely, Gaussian random walk and Lévy walk, are activated to enrich the population diversity. Moreover, RW-GEDA is executed in an Eigen coordinate framework to promote the evolution towards the dominant region. The performance of RW-GEDA is evaluated by using the CEC 2014 test suite and compared with other top algorithms from different communities as well as promising GEDA extensions. The statistical results demonstrate the competitive performance of our proposed RW-GEDA in terms of efficiency and accuracy. In addition, RW-GEDA is applied to solve the optimal missile guidance handover problem. To fill the gap in solving this problem, a novel missile guidance advantage model is established, and the optimal missile guidance handover is determined by optimizing the control variables of unmanned combat aerial vehicles. The validity and practicability of the problem model as well as the accuracy and efficiency of RW-GEDA are demonstrated by the experimental results.


#### Abstract

INDEX TERMS Gaussian estimation of distribution algorithm, CEC 2014, numerical optimization, air combat, UCAV.


## I. INTRODUCTION

The characteristics of real-world optimization problems are multimodal, nonconvex, disconnected and oscillated, which make traditional gradient-based algorithms difficult to optimize. With rapid improvements in computation ability, evolutionary computing has demonstrated tremendous progress in the field of real-numerical optimization over the past decades,

The associate editor coordinating the review of this manuscript and approving it for publication was Lubin Chang.
and is increasingly regarded as the most efficient way to address these NP hard problems.

Evolutionary computing techniques mostly involve metaheuristic optimization algorithms and are applied in various fields. In recent years, a new class of optimization algorithms, called estimation of distribution algorithm (EDA) [1], has rapidly developed in the field of evolutionary computing and has been widely applied to solve real-world problems [2]-[4]. Although the EDA is a type of evolutionary algorithm, there are significant differences between the EDA and traditional methods. In traditional evolutionary algorithms, the

population represents a set of solutions for the optimization problem, and each individual in the population has a corresponding fitness value. Selection, crossover and mutation operations are used to simulate the operation of natural evolution, and the problem is solved iteratively. The EDA does not have traditional crossover and mutation evolution operations but instead uses the learning and sampling of probabilistic models. An EDA describes the spatial distribution of the superior candidate solutions through a probabilistic model and establishes a descriptive solution from the macro perspective of the group with statistical learning. The probability distribution models in EDA can identify the features of promising solutions and determine the location of better solutions to evolve the population. Generally, EDAs can be divided into discrete EDAs and continuous EDAs, which are used in different types of problems. This paper considers the single-objective optimization of continuous problems by using a Gaussian probability model in which the variables follows a Gaussian distribution. According to the variable dependencies, the Gaussian EDA (GEDA) can be further categorized into three groups, including univariate GEDA [5], bivariate GEDA [6], and multivariate GEDA [1], among which multivariate GEDA shows competitive performance on most types of problems.

For GEDA, both the distribution scope and evolutionary direction have important roles in the efficiency. At the beginning of this field of research, scholars found that the variances that determine the search scope would shrink rapidly in the later stage of optimization, which led to the algorithm falling into a local optimum. Therefore, Grahl et al. [7] proposed correlation-triggered adaptive variance scaling (CT-AVS) to overcome the disadvantages of the original adaptive variance scaling (AVS) which may decrease the convergence speed when the solved problems do not require scaling. Similarly, Cai et al. [8] proposed another method, cross-entropy adaptive variance scaling (CE-AVS), to overcome imprecise structure learning. The eigenvalues of the estimated covariance matrix were studied by Dong and Yao [9] to change the search scope. Moreover, Liu et al. [10] combined principal component analysis (PCA) with GEDA. The Covariance Matrix Adaptation Evolution Strategy (CMA-ES) [11] is a promising GEDA with rank-1 and rank- $\mu$ updating. Nevertheless, it has a complex framework and less capability for ill-shaped multimodal problems.

Further research has revealed that the efficiency of GEDA depends not only on the size of the variance, but also the evolutionary directions. Bosman et al. [12] advised that premature convergence is more likely to occur if the search direction does not have intervention because the main search direction tends to become perpendicular to the fitness improvement direction. Their team introduced the standard deviation ratio (SDR) [13] and anticipated mean shift (AMS) [12] strategies for the EDA and provided the well-known AMaLGaM algorithm with a combination of AVS, SDR, and AMS [14]. In recent work, Ren et al. [15] proposed using an improved anticipated mean shift (AMS) technique to shift the mean
value of the selected solutions to efficiently adjust the search scope and the direction. Another GEDA variants explored by them is $\mathrm{EDA}^{2}[16]$, using an archive that can save more promising solutions to adjust the evolution direction. Their recent research [17] also proposed a novel variances adjustment technique, which has the advantage of tuning the variances and main search direction of GEDA simultaneously.

Another limitation of GEDA is that the distribution of the solution space is easily over fitted when learning the probability model during the evolutionary process. As Yuan [18] noted, diversity maintenance plays a key role in the success of EDAs. To overcome this defect, Liang et al. [19] proposed an inferior solution repairing (ISR) operator using remedy inferior solutions to the obtain the covariance matrix. Xu [20] combined the EDA with a chaos perturbation strategy to improve the local search ability. Chen et al. [21] presented a fast-interactive estimation of distribution algorithm (IEDA) using the domain knowledge of a personalized search. Fang et al. [22] developed a mean shift strategy in the EDA. Auger and Hansen [23] developed a restart CMA-ES with increasing population size (IPOP-CMAES). Karshenas et al. [24] studied the use of regularized model learning in GEDA. Santana et al. [25] improved on the EDA using new selection strategies. Two studies [26], [27] adopted Copula theory and a probabilistic graphical model, respectively, instead of the Gaussian model to establish the distribution. The techniques of detecting promising areas [28] and niching [29], [30] were introduced to improve the performance of EDAs in solving multimodal problems.

The above reviewed works that aimed at improving the performance of GEDA mainly focus on three aspects: the scaling of distribution variances, intervention of the evolutionary direction and maintaining population diversity. Most research has improved the exploration capability of GEDA from one or two aspects. However, the current probability model improvement methods are not sufficient to avoid premature convergence, especially for complex multimodal problems. Additionally, the validation of their work is insufficient without a comparison with the current top algorithms. On other hand, most of the above GEDA variants request a large population size to maintain the exploration performance. In each iteration, only a few superior solutions are utilized to update the covariance matrix, and the rest are abandoned which causes computation waste. Moreover, a large population size leads to fewer iterations, and thus, the convergence performance may be poor with limited function evaluations.

In this work, we propose a novel modified GEDA from the above three aspects with two random walk strategies, named RW-GEDA. First, a weighted maximum likelihood estimation method is used to improve the quality of the estimated mean and generate a covariance matrix. Moreover, a shifted mean integrating the information from the whole and the individual is utilized in sampling new population to enhance the exploration performance. If the algorithm stagnates, then the two random walk strategies, i.e., Gaussian random walk and

Lévy walk, are activated to enrich the population diversity. Additionally, the sample process is executed in an eigen coordinates framework to promote the evolution towards the dominant region. The performance of RW-GEDA with a smaller population size is benchmarked using the CEC 2014 test suite, and the experimental results are compared with some promising GEDA variants as well as other state-of-the-art algorithms from different communities. Moreover, the proposed RW-GEDA is applied to solve a complex real-world optimization problem, an optimal missile guidance handover problem for multi-UCAV in over-the-horizon (OTH) air combat. To address this complex real-time engineering problem, a novel missile guidance advantage model and missile guidance assignment model are established. Finally, the feasibility of the problem model and the performance of RW-GEDA are analyzed based on experimental results.

This rest of our paper is organized as follows: The mathematical presentation of the proposed RW-GEDA is described in Section 2. In Section 3, numerical experiments of the CEC 2014 test are presented, and the statistical results are discussed. RW-GEDA is applied in solving an optimal missile guidance handover problem in Section 4. Finally, Section 5 offers the main conclusions of this work and notes directions for future study.

## II. PROPOSED RW-GEDA

## A. REVIEW OF THE BASIC GEDA

As a model-based evolutionary algorithm, GEDA assumes that the optimal solutions obey a Gaussian probability distribution, and uses the probability distribution estimated from the superior solutions in the current generation to sample new candidates, thus driving the evolution of the algorithm. The basic steps of GEDA are described as follows.

Step 1. Set the algorithm parameters and initialize the population.
Step 2. Evaluate the current solutions according to the objective function.
Step 3. Select superior solutions to estimate the Gaussian probability distribution model.
Step 4. Sample the new population according to the Gaussian probability distribution model and evolve the algorithm.
Thus, for the continuous GEDA with an $n$ degree of freedom column vector x , the joint probability density function of the Gaussian probability distribution model can be parameterized by the mean $\mu$ and the covariance matrix $\boldsymbol{C}$ as

$$
G_{(\boldsymbol{\mu}, \mathbf{C})}=\frac{(2 \pi)^{-\pi / 2}}{(\operatorname{det} \mathbf{C})} \exp \left(-(\mathbf{X}-\boldsymbol{\mu})^{\mathrm{T}}(\mathbf{C})^{-1}(\mathbf{X}-\boldsymbol{\mu}) / 2\right)
$$

where

$$
\begin{aligned}
& \boldsymbol{\mu}=\frac{1}{|\mathbf{S}|} \sum_{i=1}^{|\mathbf{S}|} \mathbf{s}_{i}, \quad \mathbf{s}_{i} \in \mathbf{S} \text { and } \mathbf{S} \subset \mathbf{X} \\
& \mathbf{C}=\frac{1}{|\mathbf{S}|} \sum_{i=1}^{|\mathbf{S}|}\left(\mathbf{s}_{i}-\boldsymbol{\mu}\right)\left(\mathbf{s}_{i}-\boldsymbol{\mu}\right)^{\mathrm{T}}
\end{aligned}
$$

![img-0.jpeg](img-0.jpeg)

FIGURE 1. The change of probability density ellipsoid in basic GEDA.
The symbol $\boldsymbol{S}$ in (2) and (3) represents the set of select superior solution vectors. The new candidate for the $i$ th solution is sampled in each iteration by

$$
\mathbf{x}_{i}=\boldsymbol{\mu}+\mathbf{y}_{i}, \mathbf{y}_{i} \sim N(0, \mathbf{C})
$$

The basic GEDA suffers from two deficiencies [17]: 1) The variance in each degree decreases rapidly with the iterations of the algorithm; 2) The evolution direction tends to be perpendicular to the descent direction of the objective function value. These two defects are illustrated in Fig. 1. The equiprobability density surface of the population generated following the multivariate Gaussian distribution is a super ellipsoid. The eigenvector of $\boldsymbol{C}$ corresponds to the direction of the ellipsoid axis; and the eigenvalue of $\boldsymbol{C}$ equals the square of the length of each axis, as shown in Fig. 1. The excellent solutions selected by GEDA in each iteration are mainly distributed in the semi-ellipsoid formed by the original probability density ellipsoid cut by the objective function isoline. The long axis of the semi-ellipsoid is parallel to the objective function isoline; accordingly, the long axis of the newly estimated probability density ellipsoid is parallel to the objective function isoline, that is, it tends to be perpendicular to the improved direction of the objective function. On the other hand, there are more samples near the center of the original probability density ellipsoid in the semi-ellipsoid and fewer samples far from the center, and thus, the newly estimated distribution will shrink naturally according to these samples. This characteristic of the traditional GEDA greatly reduces the search efficiency of the algorithm, leading to premature convergence even in the sloping region.

Thus, we propose our RW-GEDA with a modification of the ill-shaped distribution focusing on three aspects: estimated distribution amending, evolutionary directions adjustment and population diversity enrichment. More details are presented in the next subsection.

## B. MATHEMATICAL PRESENTATION OF RW-GEDA

In the traditional GEDA, the mean value is typically calculated using the maximum likelihood estimation (MLE)

method [1] as shown in (2). In our RW-GEDA, we utilize a weighted MLE to emphasize those promising solutions.

$$
\boldsymbol{\mu}=\sum_{i=1}^{|\mathbf{S}|} \omega_{i} \mathbf{s}_{i}, \mathbf{s}_{i} \in \mathbf{S} \text { and } \mathbf{S} \subset \mathbf{X}
$$

where

$$
\omega_{i}=\ln (|\mathbf{S}|+1) /\left(\sum_{i=1}^{|\mathbf{S}|}(\ln (|\mathbf{S}|+1)-\ln (i))\right)
$$

The weight coefficients are arranged in descending order: $\omega_{1}>\omega_{2}>\ldots>\omega_{|S|}$. The select superior solution vectors are also arranged from the most fitted to the least consistent with the weight coefficients. The weighted MLE can make the estimated mean closer to those promising solutions and improve its quality. The size of set $\boldsymbol{S}$ is diverse in different studies. In our work, the first half of the superior solutions are considered to estimate the distribution, which means

$$

where $N P$ indicates the population size. The covariance matrix calculated using the weighted mean has the same form as (3).

In the traditional GEDA, only select superior solutions participate in the estimation of the distribution. The information of the other inferior solutions is neglected, which causes computation waste. Additionally, the performance of GEDA is highly associated with its mean value and covariance matrix as shown in (4). Thus, a shifted mean containing the overall distribution information and individual information is employed to diversify the distribution and make full use of the population information. Considering the quality differences between the superior solutions and the inferior solutions, the forms of the shifted mean are different. First, the population is sorted based on their fitness to distinguish the superior and inferior solutions.

$$
P_{\text {rank }}(i)=\left(N P-\operatorname{rank}\left(f\left(\mathbf{x}_{i}\right)\right)+1\right) / N P
$$

If $P_{\text {rank }}(i)>0.5$, the $i$ th solution $\boldsymbol{x}_{i}$ is considered a superior solution and selected in set $\boldsymbol{S}$, otherwise, $\boldsymbol{x}_{i}$ is regarded as an inferior solution. For a superior solution, its shifted mean is denoted as

$$
\boldsymbol{\mu}_{S}=(1-r) \cdot x_{i}+r \cdot \boldsymbol{\mu}, \quad r \sim U(0,1)
$$

This shifted mean is a random weighting of the estimated mean and individual to enrich the distribution diversity. However, it is quite different for an inferior solution as shown in (10).

$$
\boldsymbol{\mu}_{\mathrm{S}, j}=\boldsymbol{\mu}_{j}+r \cdot\left(\boldsymbol{\mu}_{j}-\mathbf{x}_{i, j}\right), \quad r \sim U(0,1)
$$

where $j$ denotes the $j$ th dimension. As shown in Fig. 1, the estimated mean is more fitted than an inferior solution and locates closer to the optimal solution. Thus, a vector from an inferior solution to the estimated mean is a descent direction of the objective function value and can be utilized to repair the
![img-1.jpeg](img-1.jpeg)

FIGURE 2. Different distribution of the shifted mean for an inferior solution in two coordinate systems.
inferior solution. Thus, the new candidate for each solution is sampled using its corresponding shifted mean as

$$
\mathbf{x}_{i}=\boldsymbol{\mu}_{\mathrm{S}}+\mathbf{y}_{i}, \quad \mathbf{y}_{i} \sim N(0, \mathbf{C})
$$

To promote the evolution towards the dominant region, we execute the sampling in an eigen coordinates framework. The eigen coordinates system is obtained by rotating the normal coordinates system using the eigendirection matrix $\boldsymbol{B}$ that is derived from the eigenvalue decomposition of covariance matrix $\boldsymbol{C}$.

$$
\mathbf{C}=\mathbf{B D B}^{\mathrm{T}}
$$

In (12), $\boldsymbol{D}=\operatorname{diag}\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{\text {dim }}\right) . \lambda_{i}$ is the $i$ th eigenvalue and 'dim' means the degrees of freedom of the variables (dimensions of the problem). $\boldsymbol{B}=\left(v_{1}, v_{2}, \ldots, v_{\text {dim }}\right)$ is the eigendirection matrix in which the eigendirection vectors correspond to the axial directions of the probability density ellipsoid. The vectors in eigen coordinates are accessed as

$$
\begin{cases}\boldsymbol{\mu}^{(E)} & =B^{\mathrm{T}} \boldsymbol{\mu} \\ x_{i}^{(E)} & =B^{\mathrm{T}} x_{i}\end{cases}
$$

Thus, the sampling in the eigen coordinate framework is presented as

$$
\begin{cases}\boldsymbol{\mu}_{S}^{(E)}=(1-r) \cdot x_{i}^{(E)}+r \cdot \boldsymbol{\mu}^{(E)}, \quad r \sim U(0,1) \\ \text { If } P_{\text {rank }}(i)>0.5 \\ \boldsymbol{\mu}_{S, \mathbf{j}}^{(E)}=\boldsymbol{\mu}_{j}^{(E)}+r \cdot\left(\boldsymbol{\mu}_{j}^{(E)}-x_{i, \mathbf{j}}^{(E)}\right), \quad r \sim U(0,1) \text { else } \\ \mathbf{x}_{i}^{(E)}=\mu_{S}^{(E)}+D \mathbf{z}_{i}, \mathbf{z}_{i} \sim N(0, \mathbf{I}) \end{cases}
$$

The eigen coordinates can release the relationship between different axes in normal coordinates. As denoted in (14), the mean shift is operated on whole vectors for a superior solution, so it possesses rotation invariance. However, the mean shift for an inferior solution is operated for each dimension of the solution vector, thus leading to a difference between the two coordinate systems, as illustrated in Fig. 2. The distribution of an obtained shifted mean is closer to the dominant region in eigen coordinates than that in normal

coordinates, which can benefit the convergence of the algorithm. The efficiency of the eigen coordinate framework is discussed in the next section.

The above improvements are based on the covariance matrix which may lead to a sharp decline in the population diversity at a later stage. A new search tool must be developed that is dependent on the covariance matrix to enrich the population diversity and reshape the ill-distribution of the solutions. In our RW-GEDA, we employ random walk strategies to enhance the exploration performance when the algorithm falls into stagnation. Random walk strategies are probabilistic models that involve strong simplifications of real animal movements [31], and have been widely used in many modern evolution algorithms, such as the grey wolf optimizer (GWO) [32], [33], cognitive behavior optimization algorithm (COA) [34], virus colony search (VCS) [35], and hummingbirds optimization algorithm (HOA) [36], to perform random exploration. Gaussian random walk and Lévy flight are the two main random walk strategies that have been shown to be surprisingly efficient for random searches in unknown circumstances and have been successfully adjusted to a wide range of empirical data. However, these two strategies have different characteristics.

Gaussian random walk follows a Gaussian distribution, which is by far the most popular because many physical variables, including light intensity, errors or uncertainty in measurements, as well as many other processes, obey Gaussian distribution. It can make full use of the local solution space to generate promising candidates in the area of interest and is employed as an efficient way to improve the exploitation performance of the algorithm. In RW-GEDA, a disturbed Gaussian random walk strategy in the eigen coordinate framework is carried out guidance from the best solution.

$$
\begin{aligned}
\mathbf{x}_{i}^{(E)}= & \operatorname{Gaussian}\left(\mathbf{x}_{\text {Best }}^{(E)}, \sigma\right)+r_{1} \cdot \mathbf{x}_{\text {Best }}^{(E)} \\
& -r_{2} \cdot \mathbf{x}_{i}^{(E)}, r_{1}, r_{2} \sim U(0,1) \\
\boldsymbol{\sigma}= & \left|\mathbf{x}_{\text {Best }}^{(E)}-\mathbf{x}_{i}^{(E)}\right|
\end{aligned}
$$

where $\boldsymbol{x}_{\text {Best }}$ indicates the best solution obtained thus far. Similar to (10), because the variance in the Gaussian distribution is related to the coordinate difference in each dimension, the distributions of sampling in different coordinate systems are quite different. As shown in Fig. 3, the distribution scope in eigen coordinates is more acceptable than that in normal coordinates.

Unlike Gaussian random walk, Lévy walk is a random procedure and has a random step determined based on another important distribution that is the so-called Lévy distribution [37]. It is regarded as the most efficient method to explore the nondestructive space [38]. Moreover, Lévy walk is widely used as a predation behavior among the natural organisms, such as macaques, sharks and modern hunter gatherers. According to one study [39], Lévy walk is the optimal exploration behavior to search for randomly distributed objects. In this regard, it is advantageous to improve
![img-2.jpeg](img-2.jpeg)

FIGURE 3. Different distribution obtained from Gaussian random walk in two coordinate systems.
the ability of RW-GEDA to explore the search space. Lévy walk typically generates random steps from the individual location. However, in our RW-GEDA, Lévy walk is carried out with a center of the current optimal solution to perform a local exploration, which can help balance the exploration and development performance of the algorithm. According to the Mantegna strategy [40], the new candidate generated following the Lévy walk can be calculated using

$$
\mathbf{x}_{i}^{(E)}=\mathbf{x}_{\text {Best }}^{(E)}+\alpha \otimes \operatorname{Lévy}(s) \otimes\left(\mathbf{x}_{\text {Best }}^{(E)}-\mathbf{x}_{i}^{(E)}\right)
$$

With regard to (18), $s=\mu /|\nu|^{1 / \beta}$ denotes the step size, and $\alpha$ is the scale factor and in the range of $[-1,1]$. The values of $\beta$ have significance in determining the shape of the Lévy distribution [41], [42]. Longer jump steps are generated with a smaller $\beta$ value; otherwise, a larger $\beta$ value can generate smaller jump steps. In this study, we set $\alpha=0.05$, and $\beta=0.5$ to help generate longer jumps to avoid stagnation. $\mu$ and $v$ are parameters that obey the following two different normal distributions, $N\left(0, \sigma_{\mu}\right)$ and $N\left(0, \sigma_{v}\right)$ :

$$
\left\{\begin{array}{l}
\sigma_{\mu}=\left(\frac{\Gamma(1+\beta) \sin (\pi \beta)}{\Gamma((1+\beta) / 2) \beta 2^{(\beta-1) / 2}}\right)^{1 / \beta} \\
\sigma_{v}=1
\end{array}\right.
$$

When the algorithm stagnates, the population no longer uses the estimated distribution for sampling, but rather each individual in the population randomly uses one of the two random walk strategies to generate new individuals. After obtaining the new candidate in the eigen coordinate system, it is still necessary to rotate it into the normal coordinates system to calculate its fitness value.

$$
\mathbf{x}_{i}=\mathbf{B} \mathbf{x}_{i}^{(E)}
$$

In RW-GEDA, we set a criterion judging the stagnation of the population, i.e., if the mean fitness value of the first half of the promising solutions remains unchanged, the algorithm is regarded as having stagnated, and the random walk strategy

```
Algorithm 1 The Procedure of RW-GEDA
    Initialize population \(N P\) and \(\tau=0.5\);
    Set \(F E s=0\), generate initial population \(\boldsymbol{X}\) randomly;
    Evaluate population; \(F E s=F E s+N P\);
    Update the best solution \(\boldsymbol{x}_{\text {Best }}\) obtained so far;
    Output \(f\left(\boldsymbol{x}_{\text {best }}\right)\) if \(F E s \geq M a x F E s\), end the algorithm; else
    Estimate weighted mean \(\mu\), covariance matrix \(\boldsymbol{C}\) according to first \(N P \cdot \tau\) solutions by (3), (5), (6) and (7);
    Calculate the decomposition of covariance matrix \(\boldsymbol{C}\) by (12)
    For each solution \(\boldsymbol{x}_{i}\)
        Rotate \(\boldsymbol{x}_{i}\) to eigen coordinates and obtain \(\boldsymbol{x}_{i}^{(E)}\) by (13)
        If algorithm stagnates
            \(\boldsymbol{x}_{i}^{(E)}\) is updated using Gaussian random walk or
            Lévy walk randomly by (16) or (18),
            otherwise,
            Calculate \(P_{\text {rank }}(i)\),
            \(\boldsymbol{x}_{i}^{(E)}\) is updated using estimated distribution by
            (14) and (15),
            end if;
            Rotate new \(\boldsymbol{x}_{i}^{(E)}\) to normal coordinates by (20),
            Calculate \(f\left(\boldsymbol{x}_{i}\right)\),
            \(F E s=F E s+1\),
            End for.
    Go to step 3.
```

will be activated.

$$
\begin{aligned}
& \text { if } \frac{1}{|\mathbf{S}|} \sum_{i=1}^{|\mathbf{S}|} f\left(\mathbf{s}_{i}(t+1)\right) \\
& \quad=\frac{1}{|\mathbf{S}|} \sum_{i=1}^{|\mathbf{S}|} f\left(\mathbf{s}_{i}(t)\right) \text {, algorithmstagnates }
\end{aligned}
$$

The elitism strategy is widely used in evolution algorithms to guarantee the global convergence performance [43]. In our proposed RW-GEDA, a greedy elitism strategy is employed to select the best population from the sire generation and the filial generation. This mechanism can preserve more promising solutions which benefits estimating the distribution. The pseudo code of the proposed RW-GEDA is described below.

## III. NUMERICAL EXPERIMENT USING CEC 2014 BENCHMARKS

Along with the rapid development of optimization algorithms, modern benchmarks have also been developed to be more challengeable and are employed to evaluate the performance of novel algorithms. Different from the classic benchmarks whose global optimum can be easily obtained, these modern versions are always asymmetrical, shifted and rotated with ill-shaped distributions, and the different properties around the multiple local optimums make these participants difficult to deal with. Thus, a continuous unconstrained numerical benchmark set, the CEC 2014 test suite, is employed to evaluate the performance of our proposed RW-GEDA in comparison with other state-of-the-art algorithms. The CEC 2014 test suite consists of 30 benchmarks
that can be categorized into four groups: F1 to F3 are unimodal functions, and F4 to F16 are multimodal functions, which are all nonseparable; F17 to F22 are hybrid functions whose variables are randomly divided into subcomponents with different basic functions, which make it more difficult to reach the global optimum; and F23 to F30 are the most complex composition functions whose basic functions are generated in a random sequence. More details about these 30 benchmarks are provided in [44]. In general, the complexity of these four groups is gradually increasing, thus leading to greater difficulty faced by the algorithms during optimization. As recommended by the proposer of the CEC 2014 test suite, each benchmark is evaluated with max function evaluations (MaxFEs) equal to $D \times 10,000 . D$ is the dimensionality of the test suite and set equal to 30 in this work. For convenience, the same search range is defined for all functions: $[-100,100]^{D}$. To reduce the randomness, 51 runs are executed independently for each benchmark. The solution results of the algorithm are recorded using an error measure, defined as $f\left(\boldsymbol{x}_{\text {Best }}\right)-f\left(\boldsymbol{x}^{*}\right)$, where $\boldsymbol{x}_{\text {Best }}$ is the best solution obtained by the algorithm in an experiment and $\boldsymbol{x}^{*}$ is the global optimum of the test function. Additionally, the optimum is obtained if the error is less than 1e-08.

As asserted in [45], there are three indispensable criteria that must be addressed to propose a new real-parameter optimization method: a comparison with state-of-the-art methods from different communities is always requested; a standard comparison methodology is advisable, including complete modern test functions and the same running conditions; and the advantages that the new proposal exhibits must

be specified. Thus, to demonstrate the efficiency of our proposal, we proved two group comparisons with different competitors. In the first group, five other state-of-theart algorithms from different communities are incorporated to make comparisons, including L-SHADE [46], AAVSEDA [17], VCS [35], COA [34] and BLPSO5 [47]. In the second group, five promising GEDAs are utilized as competitors, i.e., $\operatorname{EMNA}_{\mathrm{Z}}[1]$, AMaLGaM [14], IPOP-CMAES [23], $\mathrm{EDA}^{2}[16]$ and ISR-EDA [19]. Finally, we added a third comparison to reveal the efficiency of the different components in our modification.

## A. COMPARISON OF RW-GEDA WITH STATE-OF-THE-ART ALGORITHMS FROM DIFFERENT COMMUNITIES

The participants in this competition are top representatives in their own families. L-SHADE was the winner of the CEC 2014 competition. In contrast to the original differential evolution (DE) algorithm, L-SHADE combines SHADE with adaptive $F$ and $C R$, and it reduces its population size during the optimization process. Its variants have achieved great success in different competitions (SPS-L-SHADE-EIG [48] in CEC 2015, LSHADE-EpSin [49] in CEC 2016, LSHADESPACMA [50] and LSHADE-cnEpSin [51] in CEC 2017). Since 2014, L-SHADE has been regarded as a point of reference when designing novel algorithms and contributing to the real-parameter optimization field. AAVS-EDA is one of the most advanced GEDA versions. It utilizes the AAVS to adjust the size of variances by detecting the fitness landscape. Its outperformance has been verified using the CEC 2014 testbed. VCS is a hybrid CMA-ES with a combination of the Gaussian random walk and DE strategy, and its superior performance has been proven by a comparison with several other algorithms using 30D CEC 2014 benchmarks. COA is a novel developed ABC variant with a use of Gaussian random walk and Lévy walk, and outperforms several other popular algorithms on the 30D CEC2014 test suite. BLPSO5 is a powerful modified PSO algorithm based on a biogeographybased learning strategy. It is evaluated on CEC 2014 benchmarks and exhibits promising performance compared with other well-organized PSO algorithms.

TABLE 1. Parameter settings of six algorithms.

To make a fair comparison, all six algorithms are run 51 independent times for each benchmark for the $30 D$ test with the restricted MaxFEs $30 \times 10,000$. The parameter settings of each algorithm including the proper population size are set as in their original research and tabulated in Table 1.

The sources of the MATLAB codes of these six algorithms are provided in Appendix A. Specifically, all experiments are performed on a computer with a 2.80 GHz Intel (R) Core (TM) i7-7700HQ processor and 8GB of RAM. MATLAB 2018a is used for this programming.

The simulation results obtained by RW-GEDA are provided in Appendix B to be a reference for other studies. The statistical results containing the mean and standard deviation (SD) are provided in Tables 2. The bold data are considered the best solution according to the derived mean value. In this test, for unimodal functions F1 to F3, the global optimum can be achieved by RW-GEDA, L-SHADE and AAVS-EDA in each run, which demonstrates the efficiency of these three algorithms in solving ill-conditioned functions. In dealing with the multimodal function experiment, RW-GEDA exhibits a promising performance among these six algorithms with the best scores on F4, F5, F6, F7, F12, F14 and F15; L-SHADE outperforms others in F4, F7, F8, F10 and F16; and AAVS-EDA performs competitively on F7, F9 and F13. For hybrid functions, our proposed RW-GEDA can obtain the best solutions for F17 and F19. L-SHADE ranks top on F21 and F22, and AAVS-EDA gains the first rank on F18 and F20. The results are different for composition functions F23 to F30, where RW-GEDA, VCS and COA are the three best outperforming algorithms. Each of them ranks first on five benchmarks, i.e., F23, F24, F25, F26 and F30 for RW-GEDA and F23, F24, F25, F27, F28 for VCS and COA. However, the other three algorithms, L-SHADE, AAVS-EDA and BLPSO5, have poor performance on these eight complex benchmarks. Overall, our proposed RW-GEDA achieved best performance on more than half of the benchmarks with different characteristics in the CEC 2014 test, which demonstrates the efficacy of our method in solving different types of problems.

To make more comprehensive comparisons in a statistical manner, a Wilcoxon signed rank test and a Friedman test with an associated post hoc test are carried out. The results of the Wilcoxon signed rank test are provided in Table 3. This manner reveals the performance differences of a pair of compared algorithms and ranks them according to their rankings, which are subsequently aggregated according to their sign. In Table 3, symbol ' $\mathrm{R}+$ ' presents the sign for RW-GEDA and ' $R-$ ' for the other competitor. If the p-value is less than the significance level $(\alpha=0.05)$, then the hypothesis is not supported which means a difference exists between the two algorithms. Additionally, in the last rows of Appendix B2, ' + 'means that RW-GEDA is superior to the competitor, whereas '-'indicates poorer performance; and the ' $\%$ ' sign means that the performance of the algorithm is statistically similar to that of our proposal. According to the last row, RW-GEDA offers competitive performance to L-SHADE and AAVS-EDA in this test, and outperforms other three algorithms.

To determine the difference in multiple algorithms, the Friedman test is applied based on the derived mean values. A lower rank means a greater outperformance of

TABLE 3. Comparison of the statistical results derived from six state-of-the-art algorithms for cec 2014 benchmarks in 300 test.

TABLE 3. The results of the wilcoxon signed ranks test based on the solutions derived from six algorithms for each benchmark in 300 test with $\mathbf{5 1}$ independent runs $(\sigma=0.05)$.


TABLE 4. Mean ranks derived from the friedman test with $\sigma=0.05$.

a. 1) P-value computed by the Friedman test is: 1.3287 e-06. Chi-square is 35.2705
2) P-value computed by the Iman-Davenport test is: 1.2864 e-05.

the algorithm. The mean ranks of six competitors derived from the Friedman test are provided in Table 4. It can be seen that our proposed RW-GEDA ranks first with little advantage
ahead of L-SHADE, followed by the other algorithms in the following order: AAVS-EDA, VCS, BLPSO5 and COA. The chi-square with 5 DOFs is 35.2705 and the

TABLE 5. Mean time cost derived from six algorithms (second).


p-value is $1.3287 \mathrm{e}-06$, less than the significance level $\alpha=0.05$, which indicates significant differences among these six techniques. To evaluate the superiority of our proposal, an Iman-Davenport test with a post hoc test is carried out. Iman-Davenport test[52] is a less conservative alternative, with statistics distributed according to the F-distribution with $(k-1)$ and $(k-1)(N-1)$ degrees of freedom.

$$
F_{F}^{2}=\frac{(N-1) \chi_{F}^{2}}{N(K-1)-\chi_{F}^{2}}
$$

In (21), $K$ denotes the number of competitors and equals 6 in this test. $N$ indicates the 30 CEC2014 benchmarks. Thus, the DOFs of the F-distribution are 5 and 145 in ImanDavenport test. The associated post hoc test used in our study is the Nemenyi test [53], which uses a critical difference (CD) value to evaluate the difference between six algorithms based on their mean ranks derived from the Friedman test. The CD is evaluated as

$$
C D=q_{\alpha} \sqrt{k(k+1) / 6 N}
$$

The critical value $q_{\alpha}$ can be obtained from a statistical table of the F-distribution. In this test, $q_{\alpha}$ is 2.2768 and the CD equals 1.0997 with a significance level $\alpha=0.05$. The differences among RW-GEDA and the other five algorithms are illustrated in Fig. 4. The similar-performing algorithms are connected using the CD value. As shown in Fig. 4, RW-GEDA has no significant difference from L-SHADE or AAVE-EDA, but dominates the other three algorithms. As a novel GEDA variant, the proposed RW-GEDA with novel modifications exhibits superior performance on the CEC 2014 test suite compared to various types of state-of-the-art algorithms.
![img-3.jpeg](img-3.jpeg)

FIGURE 4. Algorithm multiple comparisons; the algorithms are connected using the CD value with less difference.

Computational cost is another key issue when evaluating the success of an optimization algorithm. The average time costs for all competitors in CEC 2014 test with 30D are presented in Table 5. To more represent the difference in the time consumption of different algorithms more intuitively, a radar plot based on the ranks of the time cost is presented in Fig. 5. The smaller the circle is, the more efficient the algorithm. L-SHADE requires less time in this test. Our proposed RW-GEDA has a similar time cost to AAVS-EDA, but is more efficient than VCS, COA or BLPSO5. Compared with AAVS-EDA, our RW-GEDA can obtain better performance with a smaller population size, which can help the algorithm converge in solving a real-time optimization problem with a limitation of fewer MaxFEs. From the above analysis, our RW-GEDA exhibits promising performance on the 30D CEC 2014 test in terms of the efficiency and accuracy.

## B. COMPARISON OF RW-GEDA WITH PROMISING GEDA VARIANTS

In this subsection, we employ five others representative GEDA variants as competitors to verify the efficiency of our proposal. $\mathrm{EMNA}_{\mathrm{g}}$ is the basic GEDA and used as the standard. AMaLGaM improves the basic GEDA by using

TABLE 6. Comparison of the statistical results derived from six geda algorithms for cec 2014 benchmarks in 30d test.


The experimental data are obtained from [16].
The experimental data are obtained from [19].
![img-4.jpeg](img-4.jpeg)
![img-5.jpeg](img-5.jpeg)

FIGURE 5. Ranks of mean time cost obtained from six algorithms.
a mean shift strategy and an adaptive variance scaling strategy and is one of the most superior EDAs at present. IPOPCMAES is argued to be the most successful GEDA, though it was first proposed fourteen years ago [45]. $\mathrm{EDA}^{2}$ is a recently developed GEDA using an archive to restore more superior solutions to rectify the ill-shaped distribution and
successfully reduce the population size. ISR-EDA uses a repair strategy to enhance the performance of neglected inferior solutions. We directly select experimental data from the open literatures for this comparison, instead of performing new simulation experiments. The results derived from RWGEDA and these five competitors are shown in Table 6. For the first type of benchmarks F1 to F3, all competitors except $\mathrm{EMNA}_{\mathrm{g}}$ can obtain the optimum in each run, confirming that these well-established GEDA variants can successfully modify the ill-shaped distribution compared with the basic $\mathrm{EMNA}_{\mathrm{g}}$ in solving ill-conditioned functions. For the multimodal benchmarks, RW-GEDA ranks first on F4, F5, F6, F7, F12 and F14, which demonstrates its efficacy in solving such problems. IPOP-CMAES also shows its outperformance with the best results on six functions, F4, F7, F8, F9, F15 and F16. For the hybrid testbed, $\mathrm{EDA}^{2}$ exhibits its superiority on most of the six benchmarks except for F19. However, our RW-GEDA performs best for the last eight composition functions. The last row of Table 5 presents overall pairwise comparisons of RW-GEDA and other GEDAs based on the mean value, where ' + ' indicates that RW-GEDA surpasses the compared algorithm, ' - ' indicates worse performance, and ' $\approx$ ' denotes that the performance of the competitor is similar to that of RW-GEDA. RW-GEDA obviously outperforms all

TABLE 7. Mean ranks derived from friedman test for six gedas with $\alpha=0.05$.

a. 1) P-value computed by the Friedman test is: $4.9968 \mathrm{e}-12$. Chi-square is 57.0251
2) P -value computed by the Iman-Davenport test is: $1.6048 \mathrm{e}-13$.
![img-6.jpeg](img-6.jpeg)

FIGURE 6. Algorithm multiple comparisons; the algorithms are connected using the CD value with less difference.
the competitors as indicated by the large number of ' + ' symbols.

To demonstrate the differences among these six GEDAs in a statistical method, the Friedman test and the post hoc test are performed as presented in Table 7 and Fig. 6, respectively. Since we can obtain only the mean and SD in the open literature, we no longer use the Wilcoxon signed rank test to compare the algorithms in pairs on each benchmark. In the Friedman test, our RW-GEDA ranks on top with a p-value equal to $4.9668 \mathrm{e}-12$. The DOF of this post hoc test is the same as that of the test in the previous subsection. Thus, the CD value is equal to 1.0997 as well. As illustrated in Fig. 6, all five GEDA variants have less significant difference in this test but far outperform than the basic EMNA $_{R}$. The proposed RW-GEDA with a novel search mechanism can perform competitively compared with those promising GEDA variants, which verifies the efficiency of our modification.

# C. ALGORITHM COMPONENTS ANALYSIS 

As described in Section 2, our modification mainly consists of four parts: 1) a weighted MLE to estimate the distribution; 2) a shifted mean to diversify the distribution; 3) two random walk strategies to enrich the population diversity; 4) an eigen coordinates framework to adjust the evolution directions. In this subsection, we perform an experiment to reveal the influence of different modifications on the performance of RW-GEDA. Thus, we propose four novel RW-GEDA variants removing corresponding modifications; i.e., Algorithm 1 uses the normal MLE to estimate the distribution, Algorithm 2 employs the estimated mean with no shift to sample new candidates, Algorithm 3 removes the random walk strategies, and Algorithm 4 is executed in the normal coordinate framework. Table 8 provides the statistical results derived from each version for 30D problems from the CEC 2014 test with the same population size of $12 D$. The last row provides the mean rank of these five algorithms obtained from the Friedman test $(\alpha=0.05)$ based on the mean values. The lower the ranking of the algorithm is, the greater the impact of the missing part on the performance of the algorithm. It is obvious that overall, RW-GEDA ranks top. Algorithm 2 ranks last, which proves the significant effect of mean shift
strategy on the performance of the algorithm. The random walk strategies show great influence on the algorithm as well for the Algorithm 3 ranks fourth. Thus, the best performance of RW-GEDA can only be achieved by integrating the four parts of the modifications.

## IV. MULTI-UCAV OPTIMAL MISSILE GUIDANCE HANDOVER BASED ON RW-GEDA

The application of a real-world optimization problem is the aim and outcome when developing optimization methods. In this section, we employ RW-GEDA to solve the multiUCAV dynamic missiles guidance handover problem in OTH air combat. UCAV has been widely used in combat in recent years due to its advantages of "zero casualties", high maneuverability and low visibility. Moreover, multi-UCAV cooperative operation can better adapt to the complexity and diversity of air combat tasks in the current networked environment, and meet the tactical requirements of situation sharing, task coordination and cooperative attack.

In modern warfare, the combined missile guidance mode, i.e., "inertial guidance + instruction correction midcourse guidance + active homing terminal guidance" is generally adopted for a medium/long range air-to-air missile in OTH air combat, but this guidance mode is highly dependent on the guidance from UCAV. If the UCAV is attacked or its communication link is disturbed, it must forfeit the missile guidance, thus leading to the loss of the target. However, with the condition of multi-UCAV cooperative operation, the guidance power handover among the collaborators can maintain the optimal guidance of the missile. More specifically, a multi-UCAV formation enters the combat airspace following the command and guidance of the ground command center, and information sharing is realized through data links among the formation. If the enemy targets are detected, each target is allocated to a UCAV according to their relative situation information. When the distance between the UCAV and its assigned target satisfy the missile attacking area, the missile is launched. During the midcourse guidance of the missile, the UCAV is requested to illuminate the target by radar to provide guidance command to missile, which may lead to it being discovered and attacked by enemy aircraft. If this UCAV is threatened by the enemy, it may abandon the guidance to ensure survival. In this case, the guidance power should be handed over to another UCAV that may have the best guidance superiority. Therefore, the study of the dynamic missile guidance handover of multi-UCAV can greatly improve not only the damage performance and overall air combat effectiveness, but also the flexibility of tactics.

TABLE 8. Comparison of the performance derived from different ne-geda versions.


a. P-value computed by the Friedman test is: $34.9773 \mathrm{e}-10$. Chi-square is 50.0662 .

Few existing studies have been proposed to solve this realtime optimization problem. Diao et al. [54], [55] solved the abnormal abrupt change in missile overload that is merged in the process of handover. Their other work [56] proposed the concept of the missile guidance advantage and established a cooperative decision-making model, but they did not solve the missile guidance handover as an optimization process. Fei et al. [57] utilized a particle swarm auction hybrid algorithm to solve the missile guidance handover problem with a simple situation model. Based on their work, a more detailed guidance advantage model is established by Zhou et al. [58], whereas they solved this problem as a binary optimization and did not specify the motion states of the UCAVs during the process.

This problem is a continuous dynamic programming problem, which is typically solved using the rolling horizon method. To maintain the maximum guidance advantage of a UCAV at the sampling point or to obtain the optimal attacking state of a UCAV relative to the target at sampling, it is necessary to optimize the UCAV's motion state in the sampling time domain, that is, to optimize the control variables in the UCAV's motion model. In other words, the focus of our research is not the optimal guidance assignment at a certain sample point, but maintaining the maximum guidance advantage throughout the entire attack
process, which is closer to the actual combat situation, contributes to the autonomous combat of UCAV, and fills in the gap in this aspect of the research. Thus, in our study, we employ RW-GEDA to optimize the continuous motions of UCAVs to maintain the optimal missile guidance advantages during the combat process. The contribution of our work and difference from previous studies are illustrated in Fig. 7.

First, the mathematical model for solving this problem is described below.

# A. MATHEMATICAL MODEL OF OPTIMAL MISSILE GUIDANCE HANDOVER 

## 1) UCAV PLANE MOTION MODEL

In OTH air combat, the influence of the horizontal distance on the situation is far greater than that of the altitude. Thus, a simplified plane motion model with a fixed altitude is reasonable and is applied to simulate the motion of the enemy target and UCAV described as follows:

$$
\left\{\begin{array}{l}
\hat{x}_{i}=v_{i} \cos \psi_{i} \\
\dot{y}_{i}=v_{i} \sin \psi_{i} \\
\dot{\psi}_{i}=g \tan \phi_{i} / v_{i}
\end{array}\right.
$$

where $\left(x_{i}, y_{i}\right)$ indicates the plane location of the $i$ th UCAV; $v_{i}$ represents its velocity, $\psi_{i}$ and $\phi_{i}$ are the heading angle and

![img-7.jpeg](img-7.jpeg)

FIGURE 7. The main novelty of our research on missile guidance problem.
rolling angle, respectively; and $g$ denotes the gravitational acceleration. In OTH air combat, the velocity is usually at its maximum value to rapidly approach the enemy; thus, for the $i$ th UCAV, the state variables consist of $\left(x_{\mathrm{i}}, y_{\mathrm{i}}, v_{\max }, \psi_{i}\right)$; and the only control variable is the rolling angle $\phi_{i}$. Considering the UCAV performance limitation, the rolling angle should satisfy its dynamic constraints.

$$
\left|\phi_{i}\right| \leq \phi_{\max }
$$

## 2) SITUATION ADVANTAGE MODELS

To evaluate the states of the UCAVs at sampling points, it is necessary to construct a situation advantage model for evaluation. The missile guidance advantage is related to the situations among the UCAVs, missiles and targets. First, the target situation advantage models related to the states of the UCAV and target, including the following a), b) and c) parts, are established in this subsection.
![img-8.jpeg](img-8.jpeg)

FIGURE 8. Relative situation of UCAV to target.
The relative situation of the UCAV to the target is illustrated in Fig. 8. LOC indicates the line-of-sight. $D$ is the distance between the UCAV and target. $V_{\mathrm{u}}, V_{\mathrm{t}}$ and $V_{\mathrm{r}}$ represent
the UCAV velocity, target velocity and relative velocity, respectively. $Q_{\mathrm{A}}, Q_{\mathrm{a}}$ and $Q_{\mathrm{r}}$ indicate the UCAV aspect angle, target approaching angle and the angle between $V_{\mathrm{r}}$ and LOC. In this model, the radar detection area, missile attacking area and missile non-escaping area are used to divide different advantageous regions. As shown in Fig. 8, $R_{\mathrm{rmax}}$, $R_{\mathrm{mmax}}$ and $R_{\mathrm{kmax}}$ are denoted as the maximum radius of the radar detection area, missile attacking area and missile nonescaping area. When the OTH air combat is simplified as plane motion, the situation advantage is usually evaluated from three aspects: angle situation, distance situation and velocity situation. Previous studies [59]-[61] established the independent multiple situation models. In practice, there are strong interconnections among these situations, which were typically neglected in those studies.

## a: ANGLE SITUATION ADVANTAGE

In OTH air combat, the angle advantage of the UCAV should be maintained to track the target effectively and avoid being attacked. For the aspect angle $Q_{\mathrm{A}}$, the angle situation will be worse with a larger $Q_{\mathrm{A}}$, which will lead to a greater offaxis missile angle, thus leading to a short range of attacking area. However, a large range of attacking area will be obtained with a greater $Q_{\mathrm{a}}$. Thus, the advantages of aspect angle and approaching angle are described with the consideration of the maximum radar detection angle $\left(q_{\mathrm{r}}\right)$, maximum missile offaxis angle $\left(q_{\mathrm{m}}\right)$, maximum angle of non-escaping zone and relative position.

$$
\begin{aligned}
& \eta_{Q_{A}} \\
& =\left\{\begin{array}{c}
0.2-0.2 \cdot\left(Q_{A}-q_{r}\right) /\left(180^{\circ}-q_{r}\right) \\
q_{r} \leq Q_{A} \\
0.6-0.4 \cdot\left(Q_{A}-q_{m}\right) /\left(q_{r}-q_{m}\right) \\
q_{m} \leq Q_{A}<q_{r} \\
0.9-0.3 \cdot\left(Q_{A}-q_{k}\right) /\left(q_{m}-q_{k}\right) \\
q_{k} \leq Q_{A}<q_{m} \\
1-0.1 \cdot Q_{A} / q_{k}, Q_{A}<q_{k}
\end{array}\right. \\
& \eta_{Q_{a}} \\
& =\left\{\begin{array}{c}
0.3+0.7\left(180^{\circ}-q_{r}-Q_{a}\right) /\left(180^{\circ}-q_{r}\right) \\
Q_{a} \leq 180^{\circ}-q_{r} \\
0.3-0.3\left(q_{r}+Q_{a}-180^{\circ}\right) / q_{r}, 180^{\circ}-q_{r}<Q_{a}
\end{array}\right.
\end{aligned}
$$

The influences of the aspect angle and approaching angle have a strong relationship with the angle situation advantage, so the angle situation model is established as

$$
\eta_{Q}=\eta_{Q_{\mathrm{A}}} \eta_{Q_{\mathrm{a}}}
$$

The variation of $\eta_{\mathrm{Q}}$ with $Q_{\mathrm{A}}$ and $Q_{\mathrm{a}}$ is illustrated in Fig. 9.

## b: DISTANCE SITUATION ADVANTAGE

The missile attacking area is closely related to the target conditions, especially its approaching angle $Q_{\mathrm{a}}$. Generally, the actual boundary of the missile attacking area varies with the approaching angle; i.e., the maximum boundary is

![img-9.jpeg](img-9.jpeg)

FIGURE 9. Angle situation variation; $\mathbf{q r}=80^{\circ}, \mathbf{q m}=45^{\circ}, \mathbf{q k}=30^{\circ}$.
![img-10.jpeg](img-10.jpeg)

FIGURE 10. Distance situation variation; $R_{r}=120 \mathrm{~km}, R_{m}=90 \mathrm{~km}$, $R_{k}=60 \mathrm{~km}$.
obtained with the maximum relative speed at the head-on attack, the second is at the side attack, and the minimum is at the tail chase. Based on these characteristics, the distance situation advantage model is denoted as
$\eta_{D}$

$$
= \begin{cases}10.5 \mathrm{e}^{-D / R_{r}}, & R_{r} \leq D \\ 0.5 \mathrm{e}^{-\left(D-c R_{m}\right) /\left(R_{r}-c R_{m}\right)}, & c R_{m} \leq D<R_{r} \\ 2^{-\left(D-c R_{\mathrm{kmax}}\right) /\left(c R_{m}-c R_{\mathrm{kmax}}\right)}, & c R_{\mathrm{kmax}} \leq D<c R_{m} \\ 1, D<c R_{\mathrm{kmax}}\end{cases}
$$

where

$$
c=e^{0.5 \cdot\left(Q_{o}-180^{\circ}\right) / 180^{\circ}}
$$

The influence of $Q_{o}$ on the distance is graphically shown in Fig. 10.

## c: VELOCITY SITUATION ADVANTAGE

In contrast to previous studies on the air combat situation, only the influence of the relative velocity on the air combat situation is considered. As shown in Fig. 11, if the UCAV occupies an angle situation advantage, the distance $D$ between the UCAV and the target is expected to decrease. Thus, the angle between their relative velocity vector and the LOS direction, which is indicated as $Q_{\mathrm{r}}$ in Fig. 11, should be
![img-11.jpeg](img-11.jpeg)

FIGURE 11. Velocity situation variation.
![img-12.jpeg](img-12.jpeg)

FIGURE 12. Relative situation of UCAV and missile.
greater than $90^{\circ}$. Otherwise, $Q_{\mathrm{r}}$ is expected to be less than $90^{\circ}$ to increase their relative distance. Based on this result, the velocity situation advantage by using the arctan function is established as

$$
\begin{aligned}
\eta_{V}=0.5+2 \cdot \operatorname{sgn} & \left(\eta_{Q}-0.5\right) \\
& \cdot \arctan \left(\left(Q_{r}-90^{\circ}\right) / 90^{\circ}\right) / 180^{\circ}
\end{aligned}
$$

In (30), $\operatorname{sgn}(\cdot)$ is a sign function, which is equal to 1 if the UCAV occupies an angle situation advantage $\left(\eta_{Q}>0.5\right), 0$ in equilibrium, and -1 with an inferior angle situation $\left(\eta_{Q}<0.5\right)$. The variation in the velocity situation is shown in Fig. 11.

Considering the coupling of the angle and distance situation in air combat, the overall situation advantage of the UCAV to the target is expressed as

$$
\eta_{\mathrm{T}}=0.7 \cdot \eta_{\mathrm{Q}} \eta_{\mathrm{D}}+0.3 \cdot \eta_{\mathrm{V}}
$$

## d: MISSILE GUIDANCE ADVANTAGE

The relative situation of the UCAV and the missile is shown in Fig. 12. During the process of the missile midcourse guidance, the UCAV not only needs to keep the target tracked, but also needs to deliver the guidance command to the missile. To complete the missile guidance, the relative position of the UCAV and guided missile must satisfy the following three constraints:

![img-13.jpeg](img-13.jpeg)

FIGURE 13. Missile guidance situation variation; $q_{r}=80^{\circ} ; q_{r m}=60^{\circ}$.

1) The missile must be located within the maximum search angle $\left(q_{\mathrm{r}}\right)$ of the radar of the UCAV.
2) The UCAV must be located within the maximum working angle $\left(q_{\mathrm{rm}}\right)$ of the tail antenna of the missile.
3) The missile must not exceed the maximum guidance distance ( $R_{\mathrm{r} \max }$ ) of the UCAV radar.
Thus, the missile angle situation advantage is introduced by using a linear weighted normalization method and its variation is shown in Fig. 13.

$$
\begin{aligned}
\eta_{q} & \\
& = \begin{cases}1-0.5 \cdot\left(q_{\mathrm{A}} / q_{\mathrm{r}}+q_{\mathrm{a}} / q_{\mathrm{rm}}\right) \\
0 \leq q_{\mathrm{A}}<q_{\mathrm{r}}, 0 \leq q_{\mathrm{a}}<q_{\mathrm{rm}} \\
0, & \text { else }\end{cases}
\end{aligned}
$$

The missile distance advantage will decrease as the distance between the missile and the guidance UCAV decreases, which can be modeled as

$$
\eta_{D_{\mathrm{m}}}=\left\{\begin{array}{ll}
e^{-3 \cdot D_{\mathrm{m}} / R_{\mathrm{imax}}}, & D_{\mathrm{m}}<R_{\mathrm{imax}} \\
0, & \text { else }
\end{array}\right.
$$

When all of the above three constraints are satisfied, the UCAV can guide the missile. Therefore, the situation advantage of the UCAV to the missile is adopted to integrate the angle situation and distance situation.

$$
\eta_{M}=\eta_{q} \eta_{D_{\mathrm{m}}}
$$

## 3) GUIDANCE ADVANTAGE OF THE UCAV FOR THE MISSILE AND TARGET

Combining the UCAV situation advantages for the missile and target, the synthetic guidance advantage of the UCAV can be obtained as

$$
\eta=\eta_{\mathrm{T}} \eta_{\mathrm{M}}
$$

## B. MISSILES GUIDANCE HANDOVER STRATEGY

Assume there are $N$ UCAVs and $M$ targets $(N \geq M)$ in air space. According to the initial target situation advantage of UCAVs relative to targets, the first superior $M$ UCAV launch missiles to $M$ targets and the $i$ th missile attacks the $i$ th target. Thus, $M$ missiles need to be guided. The guidance advantage matrix is indicated as $\eta_{\left(M \times N\right)}$, and its element $\eta_{i, j}$ denotes the guidance advantage of the $j$ th UCAV to the $i$ th missile and
![img-14.jpeg](img-14.jpeg)

FIGURE 14. Flow chart of the problem optimization.
$i$ th target, which can be calculated by using (34). The goal of the missile guidance handover is to find a set of missile assignment solutions $\boldsymbol{x}$ to maximize the guidance advantage.

$$
F_{\eta}=\max \sum_{i=1}^{N} \sum_{j=1}^{M} x_{i, j} \cdot \eta_{i, j}, x_{i, j} \in\{0,1\}
$$

It should be noted that this paper focuses on investigating the influence of UCAV maneuver decisions on missile guidance assignment. Thus, the maximum guidance advantage function is related to the control variables $\boldsymbol{u}$, and the objective function (36) can be denoted as

$$
\begin{gathered}
F_{\eta}(\mathbf{u})=\max \sum_{i=1}^{N} \sum_{j=1}^{M} x_{i, j} \cdot \eta_{i, j}(\mathbf{u}), x_{i, j} \in\{0,1\} \\
\mathbf{u}=\left[\phi_{1}, \phi_{2}, \ldots, \phi_{N}\right]
\end{gathered}
$$

Additionally, there are several constraints during the missile guidance process. Each UCAV can guide only one missile; thus, different missiles have different guidance UCAVs.

$$
\left\{\begin{array}{l}
\sum_{i=1}^{M} x_{i, j}=1 \\
\sum_{i=1}^{N} x_{i, j}=1 \\
\sum_{i=1}^{N} \sum_{j=1}^{M} x_{i, j}=M
\end{array}\right.
$$

In our model, the value of $\boldsymbol{x}$ is determined by an ergodic method to obtain the optimal assignment plan more quickly. At the same time, because the target maneuvering may lead to a decrease of missile guidance advantage, the remaining $(N-M)$ UCAVs, which do not participate in the missile guidance directly, choose the missiles according to their

maximum guidance advantage to make maneuver decisions and enhance the robustness of the guidance advantage. A flow chart of the solution is shown below.

## C. EXPERIMENTAL RESULTS AND ANALYSIS

As a real-time optimization process, the rolling horizon method is used with a sampling time equal to 1 s . This means that the UCAV formation needs to complete the maneuver decision and guidance handover in a time domain. Suppose that there are five UCAVs that attack three targets. The initial states of the five UCAVs are ( $\left.0 \mathrm{~m}, 4000 \mathrm{~m}, 300 \mathrm{~m} / \mathrm{s}, 90^{\circ}\right)$, $\left(5000 \mathrm{~m}, 0 \mathrm{~m}, 300 \mathrm{~m} / \mathrm{s}, 60^{\circ}\right),\left(10000 \mathrm{~m},-4000 \mathrm{~m}, 300 \mathrm{~m} / \mathrm{s}\right.$, $\left.45^{\circ}\right),\left(15000 \mathrm{~m},-8000 \mathrm{~m}, 30 \mathrm{~m} / \mathrm{s}, 30^{\circ}\right)$ and ( 20000 m , $-12000 \mathrm{~m}, 300 \mathrm{~m} / \mathrm{s}, 0^{\circ}$ ). The initial states of the three targets are $\left(60000 \mathrm{~m}, 45000 \mathrm{~m}, 250 \mathrm{~m} / \mathrm{s}, 180^{\circ}\right),\left(65000 \mathrm{~m}, 40000 \mathrm{~m}\right.$, $\left.250 \mathrm{~m} / \mathrm{s}, 180^{\circ}\right)$ and $\left(70000 \mathrm{~m}, 35000 \mathrm{~m}, 250 \mathrm{~m} / \mathrm{s}, 180^{\circ}\right)$. All three targets perform turning maneuvers with stable rolling angles equal to $45^{\circ}, 36^{\circ}$ and $30^{\circ}$, respectively. The other parameters are set as follows: maximum rolling angle of UCAV $\left|\phi_{\max }\right|=72^{\circ}$, maximum radar search angle of UCAV $q_{\mathrm{r}}=80^{\circ}$; maximum missile attacking angle $q_{\mathrm{m}}=45^{\circ}$; maximum angle of missile non-escaping zone $q_{k}=30^{\circ}$; maximum angle of missile tail radar $q_{\mathrm{rm}}=60^{\circ}$; maximum radar working distance of the UCAV $R_{\mathrm{r}}=120,000 \mathrm{~m}$; maximum missile attacking distance $R_{\mathrm{m}}=90,000 \mathrm{~m}$; maximum distance of missile non-escaping zone $R_{\mathrm{k}}=60,000 \mathrm{~m}$. The velocity of the missile is set to $800 \mathrm{~m} / \mathrm{s}$, and the motion of the missile follows a proportional navigation method with the proportional coefficient $k=5$.

To assess the performance of RW-GEDA in solving this complex real-time optimization problem, VCS, GWO [62] and AAVS-EDA are employed as competitors. VCS exhibits it promising performance in engineering design. GWO has become the most popular algorithm in its source journal and widely applied in engineering optimization. AAVS-EDA is one of the successful GEDA variants. To make a fair comparison, the parameters of the four algorithms are set as: the dimensionality is $D=5$, the population size of RW-GEDA is $N P=12 D=60$, and these of other three techniques are 20,60 and 120 , respectively, and the maximum function evaluations MaxFEs $=4800$. The total simulation time is 55 s ; to reduce the randomness, all experiments are performed 10 times independently.

Fig. 15(a) provides a horizontal view of the air combat situation in the simulation time. At the initial time of optimization, the situation matrix $\eta_{T(M \times N)}$ of the UCAVs to targets calculated by using (31) is

UCAV1 UCAV2 UCAV3 UCAV4 UCAV5


Missile1 is launched by UCAV5 to target1. Missile2 is launched by UCAV4 to target2. Missile3 is launched by UCAV1 to target3.
![img-15.jpeg](img-15.jpeg)

FIGURE 15. Optimal missile guidance handover obtained from RW-GEDA. (a) Horizontal view. (b) Control variables. (c) Missile1 guidance advantage. (d) Missile2 guidance advantage. (e) Missile3 guidance advantage. (f) Missiles guidance assignments. (g) Comparison of the missiles guidance advantages.

![img-16.jpeg](img-16.jpeg)

FIGURE 15. (Continued.) Optimal missile guidance handover obtained from RW-GEDA. (a) Horizontal view. (b) Control variables.
(c) Missile1 guidance advantage. (d) Missile2 guidance advantage. (e) Missile3 guidance advantage. (f) Missiles guidance assignments. (g) Comparison of the missiles guidance advantages.

Under the initial conditions, the targets are located in the UCAVs missile attack area. According to the rule of target assignment, missile1 is launched by UCAV5 to attack target1, missile2 is launched by UCAV4 to attack target2, and missile3 is launched by UCAV1 to attack target3. Although UCAV2 and UCAV3 do not participate in the missile guidance, they also possess the assigned targets to occupy greater situation advantages, i.e., UCAV2 to missile1-target1 and UCAV3 to missile1-target1.

During the guidance process, each UCAV searches for the best situation by optimizing its control variables, and the missile trajectories in different colors that correspond to the colors of the UCAVs, as shown in Fig, 15(a), indicate that the guidance handover is executed in each sampling time and that the missile is guided optimally by different UCAVs.
![img-17.jpeg](img-17.jpeg)

FIGURE 16. Statistical performance comparison. (a) Mean advantage comparison. (b) Computational cost comparison.

Through the optimization of the control variable, each UCAV moves towards its assigned target. Fig. 15(b) presents the variations of the control variables of each UCAV in the simulation. All variables satisfy the constraint so that the optimization results are feasible and reliable.

The guidance advantages of UCAVs for different missiles are shown in Figs. 15(c), 15(d) and 15(e). The guidance advantages of UCAVs to three missiles will vary with the air combat situation, which may lead to an UCAV not maintaining the optimal guidance advantage to its assigned missile. As shown in Fig. 15(c), missile1 is launched by UCAV5, and thus, UCAV5 takes the best guidance advantage at the beginning. Due to the maneuvering of target1, the guidance advantage of UCAV5 gradually decreases and UCAV3 obtains the best guidance advantage from 30 s to 46 s . From 47 s , UCAV4 possesses the best guidance advantage of missile1. The guidance UCAVs for missile2 and missile3 are also selected according to the maximum guidance advantages. These changes of guidance handover are visible using different colors on the missiles trajectories as shown in Fig. 15(a). Moreover, in Figs. 15(d) and 15(e), a situation where the guidance advantage of the UCAV to the missile is 0 . This is because that the UCAV is located outside the working scope of the missile's tail antenna.

On basis of the maximum guidance advantage, the allocated guidance UCAV for each missile at different times is

presented in Fig. 15(f); a comparison of the best guidance advantages with handover is provided in Fig. 15(g). It can be seen that UCAVs can achieve a greater situation advantage with guidance handover than without handover.

To verify the efficiency of our proposed method, GWO, VCS and AAVS-EDA are employed as competitors. For each algorithm, 10 independent runs are performed to reduce randomness. The average missile guidance advantages obtained from 10 operations is statistically compared in Fig. 16(a). RW-GEDA obtains better optimization results than the other three competitors.Additionally, in this real-time optimization problem, the time consumption is another important evaluation indicator. A comparison of the mean time cost is provided in Fig. 16(b). RW-GEDA displays similar performance to GWO and AAVS-EDA in terms of the computational cost, and outperforms VCS. Although there are slight differences between the optimization results of the four algorithms, the optimization time that each algorithm requires satisfies the constraints of a sampling time of 1 s . Overall, the optimizing capacity of RW-GEDA is competitive compared with those of the other three competitors, verifying the superiority and stability of RW-GEDA in the search process.

## V. CONCLUSION

In this study, we develop a novel GEDA extension with novel search mechanisms. Our proposed RW-GEDA is tested by using CEC 2014 benchmarks with a comparison of other state-of-the-art competitive algorithms from different communities. The statistical results show excellent performance of our proposal in terms of the convergence accuracy and computational efficiency.

To solve the optimal missile guidance handover problem of multiple UCAVs in OTH air combat, we describe our novel mathematical models, and RW-GEDA is applied to solve the problem. The simulation results show that UCAVs can maintain better guidance advantages in the combat process through guidance handover, thus verifying the validity of the established model. Moreover, RW-GEDA can solve this problem effectively and competitively compared with other popular algorithms.

As a novel development of the current GEDA, our RWGEDA has fewer tuning parameters and less parameter sensitiveness in solving different problems. However, the limitation in our RW-GEDA is its greater computational cost. In future studies, it is necessary to reduce the calculation and decomposition of the covariance matrix by hybrid other efficient tools.

## APPENDIX

## A. SOURCES OF MATLAB CODES FOR THE ALGORITHMS PARTICIPATING IN SECTION 3

RW-GEDA:
From Cor. Author Wang: wxf825421673@163.com.
L-SHADE:
http://www.pudn.com/Download/item/id/2840416.html.

AAVS-EDA:
From Author Liang: liangyongsheng@stu.xjtu.edu.cn. VCS:
From Cor. Author Li: modern_lee@163.com. COA:
From Cor. Author Li: modern_lee@163.com.
BLPSO5:
https://ww2.mathworks.cn/matlabcentral/fileexchange/ 64074-biogeography-based-learning-particle-swarmoptimization?s_tid= srchtitle.

## B. STATISTICAL RESULTS OF THE MEAN ERROR VALUES DERIVED FROM RW-GEDA FOR THE 30D CEC2014 TEST

