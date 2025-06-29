# A novel ensemble estimation of distribution algorithm with distribution modification strategies 

Xiaofei Wang ${ }^{1} \cdot$ Yintong $\mathrm{Li}^{2} \odot \cdot$ Yajun Liang ${ }^{3} \cdot$ Bi $\mathrm{Wu}^{1} \cdot$ Yongbo Xuan ${ }^{1}$<br>Received: 19 April 2022 / Accepted: 11 January 2023 / Published online: 20 March 2023<br>(c) The Author(s) 2023


#### Abstract

The canonical estimation of distribution algorithm (EDA) easily falls into a local optimum with an ill-shaped population distribution, which leads to weak convergence performance and less stability when solving global optimization problems. To overcome this defect, we explore a novel EDA variant with an ensemble of three distribution modification strategies, i.e., archive-based population updating (APU), multileader-based search diversification (MSD), and the triggered distribution shrinkage (TDS) strategy, named $\mathrm{E}_{3}$-EDA. The APU strategy utilizes historical population information to rebuild the search scope and avoid ill-shaped distributions. Moreover, it continuously updates the archive to avoid overfitting the distribution model. The MSD makes full use of the location differences among populations to evolve the sampling toward promising regions. TDS is triggered when the search stagnates, shrinking the distribution scope to achieve local exploitation. Additionally, the $\mathrm{E}_{3}$-EDA performance is evaluated using the CEC 2014 and CEC 2018 test suites on 10-dimensional, 30-dimensional, 50-dimensional and 100-dimensional problems. Moreover, several prominent EDA variants and other top methods from CEC competitions are comprehensively compared with the proposed method. The competitive performance of $\mathrm{E}_{3}$-EDA in solving complex problems is supported by the nonparametric test results.


Keywords Estimation of distribution algorithm $\cdot$ CEC 2014 $\cdot$ CEC 2018 $\cdot$ Numerical optimization

## Introduction

Evolutionary computation is an important field of numerical optimization. Due to the insensitivity of the characteristics of the objective function, evolutionary algorithms are considered effective for solving nonconvex optimization and NP-hard problems. The estimation of distribution algorithm (EDA) [1], as one of the traditional evolutionary computation techniques, has received considerable research attention over the past two decades. In contrast to the traditional evolutionary algorithms that use crossover, mutation and selection

[^0]mechanisms, EDA has a unique evolutionary process [2]. It estimates the probability distribution model of selected solutions and evolves the whole population iteratively. The Gaussian distribution model is typically used with the EDA to solve problems in the continuous domain. According to the structure of the Gaussian probability model and the relationships among variables, EDAs can be classified as univariate [3], bivariate [4], or multivariate [5] models. The multivariate Gaussian distribution model used in EDA and its variants is competitive in various real world applications [6-10].

The EDA extracts the features of the population location from a macro perspective, and its generation relies heavily on the estimated distribution model. However, the variances in the distribution of the fitness descent directions shrink rapidly in its later stages [11, 12]. Moreover, the basic EDA has no local search mechanism to enhance the population diversity, causing it to be easily affected by ill-shaped distributions. Specifically, when addressing multimodal problems, the EDA cannot capture the appropriate characteristics of a problem effectively through the unimodal Gaussian distribution model. Thus, the traditional EDA struggles with premature convergence and is easily trapped


[^0]:    $\boxtimes$ Xiaofei Wang
    wxf825421673@163.com
    Yintong Li
    yintongli0007@163.com
    1 Beijing Blue Sky Innovation Center for Frontier Science, Beijing 100085, China
    2 Aviation Engineering School, Air Force Engineering University, Xi'an 710038, China
    3 China Aerodynamics Research and Development Center, Mianyang 621000, Sichuan, China

in stagnate conditions. To address these drawbacks, many studies have been performed in recent decades, as reviewed in the next section. However, according to the results of single-objective optimization competitions organized by the IEEE Congress on Evolutionary Computation (IEEE CEC) in recent years, EDA extensions have been unable to achieve top performances in solving those complex benchmarks. Nevertheless, due to its unique model-based features, the EDA can be useful as a supplement to other algorithms. Note that all of the recent champion algorithms utilized the covariance matrix adaptation technique, such as HSES [13], ELSHADE-SPACMA [14] (in CEC 2018), EBOwithCMAR [15] (in CEC 2017), and UMOEAsII [16] (in CEC 2016). In these promising hybrid methods, the EDA provides a unique search framework to capture problem features, while other search mechanisms favorably supplement the EDA in enriching population diversity and performing efficient local searches.

However, the EDA's potential is not limited to its application as a hybrid algorithm. The property of the distribution characteristics has not been fully exploited. First, the role of historical distribution information in modifying the abnormal distribution of the population is inefficiently developed. Second, the application of the best or the leader solutions in directing the search operation toward dominant regions has not received widespread attention. In addition, the function of inferior solutions in enhancing population diversity is always neglected. These areas of potential improvement leave room for us to further explore the characteristics of the EDA and make full use of the population distribution information to enhance the algorithm performance.

In this study, we focus on the improvement of the EDA distribution model from the above aspects and explore a new, improved EDA for solving single-objective optimization problems using three modification strategies. The main innovation points can be summarized as the following three points:
a. Archive-based population updating (APU) We propose a distribution model estimation strategy based on historical distribution information. An archive is designed to store successive generations of solutions, and promising individuals are selected from this archive to form a new population and estimate the distribution model. This operator is called archive-based population updating (APU), which makes full use of historical population information. Using APU, the selected excellent individuals from different generations can expand the variances in the search scope. Nevertheless, the continuous archive updates following the first-in first-out rule can effectively avoid the over computation of several best solutions that result in the distribution model overfitting and loss of population diversity.
b. Multileader-based search diversification (MSD) We develop a multileader-based search diversification (MSD) strategy to utilize the location difference among the population to diversify search scope. The MSD contains two different search strategies. First, the mean point is prompted using a leader solution randomly selected from a set where several of the most promising solutions are preserved. On the other hand, the candidate is generated around a disturbed mean point. Using the MSD strategy, the advantage of leader solutions in directing the evolution is fully utilized. Furthermore, the sampling scopes are diversified with different mean points and can effectively enhance the algorithm's exploration behavior, thus avoiding the ill-shaped unimodal distribution model misleading the population into stagnation.
c. Triggered distribution shrinkage (TDS) We study a triggered distribution shrinkage (TDS) strategy to scale the search scope when the algorithm falls into stagnation. This mechanism is designed to decrease the search scope and evolve the algorithm to focus on local exploration and improve the convergence performance.
We assemble the above three search strategies in the EDA to obtain the $\mathrm{E}_{3}$-EDA. The algorithm focuses on singleobjective optimization problem optimization, which is the basic issue of a new evolutionary algorithm and the foundation of other complex extensions, such as multi-objective algorithms, constrained algorithms, and parallel algorithms. To verify the effectiveness of our proposal, the well-known CEC 2014 and CEC 2018 test suites are used for benchmarking. Both tests are carried out with 10-dimensional, 30-dimensional, 50-dimensional and 100-dimensional (10D, 30D, 50D and 100D) functions. Additionally, the top methods in the CEC 2014 and CEC 2018 competitions, including LSHADE-EpSin [17], UMOEAsII [16], L-SHADE [18], HSES [13], LSHADE-RSP [19], ELSHADE-SPACMA [14], EBOwithCMAR [15], in addition to two promising EDA variants, MLS-EDA [20] and ACSEDA [21], are employed to perform in competitions with $\mathrm{E}_{3}$-EDA.

This study is organized as follows. In Sect. "Related advances in EDA research", the basic EDA is presented, and its related achievements are reviewed. In Sect. "E3-EDA search behavior description", the search behaviors of $\mathrm{E}_{3^{-}}$ EDA are described mathematically. Section "Experimental study using modern IEEE CEC benchmarks" details the experimental research. First, a parametric study is carried out to determine $\mathrm{E}_{3}$-EDA's optimal parameter settings. Then, the influence of different search mechanisms on algorithm convergence performance is revealed. Finally, the performance of $\mathrm{E}_{3}$-EDA is evaluated using the CEC 2014 and CEC 2018 benchmarks. Nonparametric tests are also adopted to compare $\mathrm{E}_{3}$-EDA with the top algorithms. Finally, the findings of this study are concluded in Sect. "Conclusions".

## Related advances in EDA research

The basic EDA evolves the search scope by learning the distribution characteristics of the selected superior solutions. The mean value $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{C}$ of the Gaussian distribution model are determined using maximum likelihood estimation (MLE) as follows:
$\boldsymbol{\mu}=\frac{1}{|\boldsymbol{S}|} \sum_{i=1}^{|\boldsymbol{S}|} \boldsymbol{x}_{i}, \quad \boldsymbol{x}_{i} \in \boldsymbol{S}$ and $\boldsymbol{S} \subset \boldsymbol{X}$,
$\boldsymbol{C}=\frac{1}{|\boldsymbol{S}|} \sum_{i=1}^{|\boldsymbol{S}|}\left(\boldsymbol{x}_{i}-\boldsymbol{\mu}\right)\left(\boldsymbol{x}_{i}-\boldsymbol{\mu}\right)^{\mathrm{T}}, \quad \boldsymbol{x}_{i} \in \boldsymbol{S}$ and $\boldsymbol{S} \subset \boldsymbol{X}$
where the symbol $\boldsymbol{S}$ is a set containing the selected superior solutions and $|\boldsymbol{S}|$ is its cardinality. Then, population sampling is carried out using the mean point and covariance matrix as follows:
$\boldsymbol{x}_{i}=\boldsymbol{\mu}+\boldsymbol{y}_{i}, \quad \boldsymbol{y}_{i} \sim N(0, \boldsymbol{C})$.
The estimated distribution model is crucial to algorithm performance. When the population distribution becomes abnormal, the algorithm has no mechanism to maintain population diversity, which leads the main search direction to be gradually perpendicular to the descent direction of the objective function value, thus causing the algorithm to fall into local stagnation. This deficiency was first noted in [22], where Cai et al. studied an adaptive variance scaling (AVS) method. In [23, 24], Grahl et al. proposed a correlationtriggered AVS (CT-AVS) mechanism and another trigger technique called SDR. On this basis, a well-known EDA named AMaLGaM was proposed in 2013 [25]. However, this method scaled the variances without differences, and thus, the search scope cannot be readily directed toward the fitness descent directions. Ren et al. equipped EDA with anisotropic AVS (AAVS-EDA) [11]. The advances of AAVSEDA over AMaLGaM were supported by their experimental study. Although AAVS-EDA can anisotropically scale the variances based on fitness landscape detection, one concern is that the trial points are not limited to the input domain, which leads to unreliable detection. Their other work, $\mathrm{EDA}^{2}$, employed an archive to preserve the superior solutions of successive generations [12]. This mechanism uses the distribution differences among distinct generations to increase the variance in the fitness descent direction and effectively avoid a problematic distribution. Similarly, Yang et al. [21] proposed ACSEDA with an adaptive covariance scaling strategy for covariance estimation.

However, all elements in the archive participate in the distribution estimation, which requires additional time consumption. The more widely accepted EDA variant is the covariance matrix adaptation evolution strategy (CMA-ES)
[26]. CMA-ES utilizes the "rank-1" update and the "rank$\mu$ " update to estimate the covariance matrix and adopts a cumulative step length adjustment to scale the distribution scope adaptively. Its promising variants, IPOP-CAM-ES [27] and NBiPOP-aCMA-ES [28], were the top methods in the CEC 2005 and CEC 2013 competitions, respectively. However, they incur a greater computational burden than other approaches due to their complex search framework.

In addition to modifications to the distribution model, many other search operators have been adopted in EDAs to enrich the population diversity. In our previous work [20], the MLS-EDA utilizes a multi-leader search strategy to enhance population diversity and avoid premature convergence. In [29], the EDA was equipped with a simulated annealing technique to enhance local exploration performance. Miquélez et al. [30] employed a Bayesian classifier method to estimate the probability model. Their proposal exhibited competitive performance in solving continuous optimization problems. The effectiveness of a regularized learning method in EDA modification was reported by Karshenas [31]. The copula theory [32] and a probabilistic graphical model [33] were also employed in the EDA for sampling. In RWGEDA, random walk strategies were utilized to strengthen the EDA's exploration performance [34]. Moreover, the effects of the promising area detection technique and niching method on EDA performance improvement have been addressed by various studies $[5,35]$.

Combining EDA with other optimization algorithms to fully leverage their advantages is regarded as another effective way to improve search performance. A hybrid of the EDA with PSO was explored by Qi et al. [36] to address the real world optimization problem. Furthermore, several studies have been carried out to combine DE and EDA [37, 38]. The statistical results demonstrated that their proposals outperformed other approaches. Moreover, in Sun's work [39], a hybrid technique combining EDA and CS was implemented to solve a scheduling problem.

The above review indicates that EDA development has progressed through different aspects. For the EDA variants, the properties of each element of solution information are not fully utilized. For example, poor solution information that is not involved in model construction is directly discarded. The function of elite solutions in promoting algorithms to search for different dominant regions has not been explored. For the remaining EDA studies, the improvements employed different search mechanisms or algorithms to compensate for the lack of population diversity in the basic EDA. These developments were accompanied by a complex implementation framework and additional free parameters, which reduce the algorithm's efficiency and robustness. In contrast to previous studies, our $\mathrm{E}_{3}$-EDA utilizes APU, MSD and TDS strategies to modify the distribution model rather than employ other

![img-0.jpeg](img-0.jpeg)

Fig. 1 Workflow diagram of $\mathrm{E}_{3}$-EDA
search mechanisms or sub-algorithms. The proposed modifications make full use of historical and current population information to enhance the basic EDA optimization and convergence performance.

## $\mathrm{E}_{3}$-EDA search behavior description

The $\mathrm{E}_{3}$-EDA search framework integrates APU, MSD and TDS with the basic EDA, as illustrated in Fig. 1. In each generation, the first NP best-performing solutions from the archive are selected to participate in distribution model estimation. Then, TDS is activated to shrink the variances of the covariance matrix to strengthen the exploitation capacity only if the algorithm is determined to be in stagnation. In MSD, two different search behaviors are employed to modify the mean point to diversify the search scope. After sampling, the APU strategy updates the new population based on an archive to avoid the overuse of the determined best solutions. The detailed descriptions of $\mathrm{E}_{3}$-EDA are denoted below.

## APU strategy

In the APU strategy, continuous $n$ generations of population information are retained in an archive, i.e., $A^{t}=X^{t} \cup X^{t-1} \cup$ $\cdots \cup X^{t-n+1}$. The first NP of the best-performing individuals is selected from the archive $\boldsymbol{A}^{t}$ as the new population to estimate the Gaussian distribution model as follows:

$$
\left\{\begin{array}{l}
\boldsymbol{\mu}=\frac{1}{N P} \sum_{i=1}^{N P} \omega_{i} \boldsymbol{x}_{i} \\
\boldsymbol{C}=\frac{1}{N P} \sum_{i=1}^{\mathrm{NP}}\left(\boldsymbol{x}_{i}-\boldsymbol{\mu}\right)\left(\boldsymbol{x}_{i}-\boldsymbol{\mu}\right)^{T}
\end{array}\right.
$$

In (4), $\omega_{i}$ is the weight coefficient of the weighted maximum likelihood estimation used to calculate the mean value, which is denoted as follows:
![img-1.jpeg](img-1.jpeg)

Fig. 2 Using the old high-quality solutions many more times leads to a loss of population diversity for decreasing the variance along the descent direction
$\omega_{i}=\ln (N P+1) /\left(\sum_{i=1}^{N P}(\ln (N P+1)-\ln (i))\right)$.
If the $i$ th superior solution has a better fitness value than the $k$ th, i.e., $f\left(\boldsymbol{x}_{i}\right)<f\left(\boldsymbol{x}_{k}\right)$, the values of their weight coefficients are opposite as $\omega_{i}>\omega_{k}$. Compared with the truncation selection in CMA-ES, the gap of weight coefficients in APU is smaller. The purpose of this setting is to overcome the overreliance on the better solutions during the distribution estimation. Moreover, more solutions selected from different generations can rebuild the search scope, thus modifying the overfitted model. Therefore, the new candidates are generated following the newly estimated Gaussian distribution model as follows:
$\boldsymbol{x}_{i}=\boldsymbol{\mu}+\boldsymbol{y}_{i}, \quad \boldsymbol{y}_{i} \sim N(0, \boldsymbol{C})$.
The newly generated population is indicated as $\boldsymbol{X}^{t+1}$. Then, the new archive is updated as $A^{t+1}=X^{t+1} \cup X^{t} \cup$ $\cdots \cup X^{t-n+2}$, meaning that the oldest population information is abandoned. Then, the new population is chosen from $\boldsymbol{A}^{t+1}$ to evolve the algorithm iteratively. In this behavior, the old population is discarded in archive updating even if they contain some excellent individuals. This principle is considered to avoid the defect of premature convergence, which is inherited in the unimodal distribution model, as illustrated in Fig. 2. During the iterations, using the old high-quality solution many more times will make the long axis of the distribution model gradually perpendicular to the descent direction of the fitness value, which will lead the algorithm into a stagnated state. This phenomenon can be avoided by properly removing these old high-quality solutions, as presented in Fig. 3. After cutting off several old candidates, the distribution of the new high-quality solutions has good diversity, which can increase the sampling range.

Moreover, the distribution model of offspring sampling is calculated based on the information of the parent population, which is composed of the first NP historical optimal solutions

![img-2.jpeg](img-2.jpeg)

Fig. 3 Through the APU strategy, the old solutions are abandoned and the enlarged new search scope can promote the algorithm searching in different promising regions
![img-3.jpeg](img-3.jpeg)

Fig. 4 The locations of the high-quality solutions in the archive are diverse
in updated archive $\boldsymbol{A}$. These high-quality solutions from different generations may be distributed in multiple dominant regions, as illustrated in Fig. 4. The new high-quality solutions in the population will increase the sampling range of the distribution model, which will enhance the algorithm's exploration ability and population diversity.

## MSD strategy

In our previous work [20], we utilized the individual information in the group for local search. On this basis, the MSD strategy is developed to diversify the distribution scope using the current best performing solutions (also called leader solutions) or the population location differences to modify the mean point. It provides two different search behaviors. The first one utilizes the multiple leader solution to direct the mean point shift as indicated below:
$\boldsymbol{\mu}_{M S D i}=\left(\boldsymbol{\mu}+\boldsymbol{L}_{i}\right) / 2$,
where $\boldsymbol{L}_{j}$ is a randomly selected member in set $\boldsymbol{L}$, which contains several top leader solutions. Set $\boldsymbol{L}$ has a variable capacity. Initially, only the current best solution is selected in set $\boldsymbol{L}$. Once the algorithm stagnates, the capacity of $\boldsymbol{L}$ expands
to store the best two solutions. Until its capacity arrives at its predefined maximum value, the capacity no longer changes.

It is difficult for the basic EDA to capture the characteristics of a multimodal problem effectively through a unimodal distribution model, which makes the algorithm susceptible to falling into a local optimum. In this behavior, these leader solutions may be scattered in different dominant regions, thus leading the diversified shifted mean points to perform a full global detection of the search area; this beneficially increases the sampling range and avoids the failure mode of algorithm stagnation. Since the population of each generation is updated from archive $\boldsymbol{A}$, the elements in set $\boldsymbol{L}$ are changed, which effectively ensures the diversity of population sampling.

In the other search behavior of MSD, the mean point of the $i$ th solution is shifted on each dimension using its individual location information, as described below:

$$
\begin{aligned}
\boldsymbol{\mu}_{M S D i}= & \left(\boldsymbol{\mu}+\boldsymbol{x}_{i}\right) / 2+\left(\boldsymbol{\mu}-\boldsymbol{x}_{i}\right) \cdot \boldsymbol{B} \cdot \boldsymbol{r}_{1 \times D} \cdot \boldsymbol{B}^{T} \\
& \boldsymbol{r}_{j} \sim U(0,1)
\end{aligned}
$$

where $\boldsymbol{r}$ is a $1 \times D$ vector and $D$ represents the problem dimensionality. $\boldsymbol{B}$ is the eigenvector matrix obtained from the decomposition of covariance matrix $\boldsymbol{C}$.
$\boldsymbol{C}=(\boldsymbol{B} \cdot \boldsymbol{D}) \cdot(\boldsymbol{B} \cdot \boldsymbol{D})^{T}$.
The $\boldsymbol{\mu}_{\mathrm{MSD}}$ is a product of a disturbance around the estimated mean point. When solving the multimodal problem, it is difficult to determine the promising search region. The current inferior solution may be located near the global optimum and can be converted into a superior solution at the next moment. Thus, we utilize the location information of all individuals to disturb the mean point. The modification along the axis of the probability density ellipsoid is achieved using the eigenvector matrix, which is helpful for shifting the mean point on the descent direction of the fitness value. The advantage of using eigen coordinates has been argued in [40, 41].

After using Eqs. (7) or (8) to obtain the improved mean point, the new individual sampling is formulated as follows:
$\boldsymbol{x}_{i}=\boldsymbol{\mu}_{M S D i}+\boldsymbol{y}_{i}, \quad \boldsymbol{y}_{i} \sim N(0, \boldsymbol{C})$.
The substantial difference between these two behaviors of the mean point in MSD, as presented in Eqs. (7) and (8), lies in the direction of mean point modification. In the first behavior, the search center moves toward the determined best-performing solutions. When the unimodal Gaussian model can capture the descent direction of the fitness value, shifting the mean point to the elite individuals is the same as promoting the distribution model in the descent direction, which is conducive to the algorithm's convergence

performance. In the second behavior, the search center is accessed using the individual information. Since the members of the population are selected from the archived $\boldsymbol{A}$, the distribution of solutions derived from different generations is scattered. Various solutions are used to disturb the mean point to realize the diversification of the distribution model, which can considerably enhance the ability to explore the solution space. In other words, Eq. (7) is advantageous to the algorithm when the distribution model obtains the dominant evolution direction, while Eq. (8) is advantageous to the algorithm to eliminate local stagnation when dealing with multimodal problems. However, it is difficult to determine which behavior is better during algorithm execution. Therefore, we present a mechanism to adaptively adjust the selection probabilities of the two behaviors in MSD according to the proportion of high-quality offspring generated using Eqs. (7) or (8).

If the probability of each individual choosing Eqs. (7) and (10) for sampling is $P_{1}$, then the probability of choosing other behavior is $P_{2}$, and $P_{1}+P_{2}=1$ (initially, $P_{1}=P_{2}$ $=0.5$ ). After population renewal, the number of offspring obtained by Eqs. (7) and (10) renewal is $\mathrm{NP}_{1}$, the number of individuals superior to their parents is $\mathrm{SNP}_{1}$, and the ratio of dominant offspring is $\mathrm{SR}_{1}$ :
$\mathrm{SR}_{1}=\mathrm{SNP}_{1} / \mathrm{NP}_{1}$.
In the same way, $\mathrm{SR}_{2}$ is the ratio of the promising offspring generated using Eqs. (8) and (10):
$\mathrm{SR}_{2}=\mathrm{SNP}_{2} / \mathrm{NP}_{2}$.
If $\mathrm{SR}_{1}$ is greater than $\mathrm{SR}_{2}$, it indicates that the effect of the first search behavior of MSD is better than the other. In the next generation, the value of $P_{1}$ should be increased appropriately, and the selection probability of the two techniques should be adjusted to the following:
$\left\{\begin{array}{l}P_{1}=\frac{\left(P_{1}+\left(1-P_{1}\right) \cdot \mathrm{SR}_{1} /\left(\mathrm{SR}_{1}+\mathrm{SR}_{2}\right)\right)}{\left(1+\left(1-P_{1}\right) \cdot \mathrm{SR}_{1} /\left(\mathrm{SR}_{1}+\mathrm{SR}_{2}\right)\right)}, \quad \text { if } \mathrm{SR}_{1}>\mathrm{SR}_{2} . \\ P_{2}=1-P_{1}\end{array}\right.$
In the same way, if $\mathrm{SR}_{1}$ is smaller than $\mathrm{SR}_{2}$, it indicates that the sampling using Eqs. (8) and (10) is better. In the next generation, the value of $P_{2}$ should be increased appropriately, and the selection probability of the two behaviors should be adjusted as follows:
$\left\{\begin{array}{l}P_{2}=\frac{\left(P_{2}+\left(1-P_{2}\right) \cdot \mathrm{SR}_{2} /\left(\mathrm{SR}_{1}+\mathrm{SR}_{2}\right)\right)}{\left(1+\left(1-P_{2}\right) \cdot \mathrm{SR}_{2} /\left(\mathrm{SR}_{1}+\mathrm{SR}_{2}\right)\right)}, \quad \text { if } \mathrm{SR}_{2}>\mathrm{SR}_{1} . \\ P_{1}=1-P_{2}\end{array}\right.$
To avoid the extinction of either search behavior, the probabilities of the two methods in MSD take a boundary as follows:
$\left\{\begin{array}{l}P_{1}=\min \left(0.95, P_{1}\right), P_{1}=\max \left(0.05, P_{1}\right) \\ P_{2}=\min \left(0.95, P_{2}\right), P_{2}=\max \left(0.05, P_{2}\right)\end{array}\right.$.

## TDS strategy

Both APU and MSD can enlarge the search scope. They can improve the algorithm's exploration performance but contribute little to the convergence performance. In $\mathrm{E}_{3}$-EDA, the TDS strategy is adopted to narrow the search area by scaling the variances when the algorithm falls into stagnation:
$\left[\boldsymbol{D}^{2}\right]_{\text {diagonal }}=\left(1-\mathrm{FEs} / \mathrm{FEs}_{\max }\right) \cdot\left[\boldsymbol{D}^{2}\right]_{\text {diagonal }}$,
where FEs are the function evaluations and $\mathrm{FEs}_{\max }$ is the maximum boundary. As presented in Eq. (16), the search range decreases with additional iterations, which makes the algorithm focus on local exploitation in the late stage. On the other hand, we set the evaluation criteria of algorithm stagnation as follows: if the average fitness value of the first half of the superior individuals in the current population is not less than the average value of the previous generation, the algorithm is trapped in stagnation. When the algorithm stagnates, the covariance matrix is no longer updated. Only the search variances are shrunk until the algorithm does not meet the stagnant standard. This setting can reduce the computational burden in the covariance matrix calculation.

Moreover, to ensure $\mathrm{E}_{3}$-EDA's convergence performance, the best result is updated after each generation. The flowchart of the execution framework of $\mathrm{E}_{3}$-EDA is illustrated in Fig. 5.

## The differences between $\mathrm{E}_{3}$-EDA and MLS-EDA

Generally, $\mathrm{E}_{3}$-EDA is an extended study based on our previous MLS-EDA. In MLS-EDA, we found that utilizing population diversity can effectively improve the EDA performance. Inspired by this, we have modified the MLS in $\mathrm{E}_{3}$ EDA, i.e., the newly proposed MSD adopts new search strategies and a statistical based search behavior adaptive selection method, which are different from the mechanisms adopted in MLS-EDA. Furthermore, only using the current population information still would have caused some restrictions on the population diversity. Thus, the APU strategy is investigated to utilize the historical distribution information to enhance the exploration performance. Through the ensemble of APU, MSD and TDS, a more efficient $\mathrm{E}_{3}$-EDA is achieved.

Fig. 5 Flowchart of $\mathrm{E}_{3}$-EDA
![img-4.jpeg](img-4.jpeg)

## Time complexity analysis of $\mathrm{E}_{3}$-EDA

The computational time complexity is an important issue for evaluating the efficiency of an evolutionary algorithm. The calculation efficiency of the EDA is affected mainly by the calculation of the covariance matrix. $\mathrm{E}_{3}$-EDA is an EDAbased algorithm, but it has little difference compared with the basic EDA in terms of computation cost. As described above, in each iteration, all members of the population participate in covariance matrix estimation, as in Eq. (4). The time complexity of this part is $O\left(D^{2} \cdot \mathrm{NP}\right)$, where $D$ is the dimensions of the problem. Moreover, the decomposition of the covariance matrix using the Jacobi method has a complexity of $O\left(D^{3}\right)$. In population updating, sampling is executed in each dimension for all individuals, which leads to a
computational cost of $O(\mathrm{NP} \cdot D)$. Therefore, the maximum time complexity of $\mathrm{E}_{3}$-EDA is determined by $O\left\{D^{2} \times\right.$ $\max (D, \mathrm{NP})$ \}. Additionally, according to the execution process in Fig. 2, the computational cost for updating the covariance matrix can be avoided when the algorithm stagnates. Under this condition, our $\mathrm{E}_{3}$-EDA achieves a time complexity less than $O\left\{D^{2} \times \max (D, \mathrm{NP})+\mathrm{NP} \cdot D\right\}$ in each iteration.

## Experimental study using modern IEEE CEC benchmarks

Using benchmarks to verify the performance is an indispensable part of developing a new evolutionary algorithm. Since 2005, IEEE CEC has proposed several challenging benchmarks on different aspects and has held algorithm

Table 1 Rankings of algorithms with different size $\left|\boldsymbol{A}\right|_{\text {max }}$ and size $\left|\boldsymbol{L}\right|_{\text {max }}$ settings when $\mathrm{NP}=12 \cdot D$
Table 2 Rankings of algorithms with different $\operatorname{sizel} A l$ and $\operatorname{sizel} L l$ settings when $\mathrm{NP}=12 \cdot D$
The bold data indicates the optimal result

Table 3 Rankings of algorithms with different $\operatorname{sizel} A l$ and $\operatorname{sizel} L l$ settings when $\mathrm{NP}=18 \cdot D$
The bold data indicates the optimal result

Table 4 Rankings of algorithms with different size $(A)$ and size $(L)$ settings when $\mathrm{NP}=21-D$
The bold data indicates the optimal result
Table 5 Rankings of algorithms with different size $(A)$ and size $(L)$ settings when $\mathrm{NP}=24-D$
The bold data indicates the optimal result
competitions every year. The CEC 2014 and CEC 2018 test suites are two modern and challenging sets of benchmarks for a single-objective optimization algorithm. The CEC 2014 test suite consists of 30 functions, which can be categorized into four types: unimodal functions F1-F3, multimodal functions F4-F16, hybrid functions F17-F22 and composite functions F23-F30. Similarly, the CEC 2018 testbed contains 29 benchmarks with F2 excluded, and it is also divided into four groups: unimodal functions F1 and F2, multimodal functions F4-F10, hybrid functions F11-F20 and composite functions F21-F30. These four types of test functions have different characteristics, and the difficulty of obtaining the optimal solution gradually increases. The distinction between CEC 2014 and CEC 2018 is that the basic functions used are different, which makes the problems have different features. More details about these two sets of testbeds are explained in [42] and [43], respectively.

Because the CEC test is a black-box problem, its result is recoded using the error value between the best value
determined by the algorithm and the optimal value as $f(\boldsymbol{x})$ $f\left(\boldsymbol{x}^{*}\right)$. The optimal value is determined when the error value is less than $1 \mathrm{e}-08$. The maximum function evaluation is related to the problem dimensionality $D$ and set to $D \times 10,000$. All simulations in this section are implemented on a laptop with an i7-8700HQ processor $(2.20 \mathrm{GHz})$ and 16 GB memory. The software MATLAB 2018a is utilized for coding and running.

In this section, we first use the CEC 2014 test suite with 30D problems to determine the optimal parameter settings of $\mathrm{E}_{3}$-EDA. Then, the contributions of the proposed modifications are discussed. Finally, the performance of $\mathrm{E}_{3}$-EDA is compared with that of the top methods in CEC competitions using the CEC 2014 and CEC 2018 testbeds.

## $\mathrm{E}_{3}$-EDA parametric study

The tuning of parameters plays a substantial role in influencing the performance of an evolutionary algorithm. If an algorithm possesses many free parameters, it is difficult to

determine its optimal values for different problems, which limits the algorithm's robustness and applicability. In $\mathrm{E}_{3}$ EDA, only three parameters need to be discussed in terms of obtaining optimal settings: the population size (NP), the maximum size of archive $\boldsymbol{A}\left(\operatorname{Sizel} \boldsymbol{A}\right)_{\max }$, and the maximum size of set $\boldsymbol{L}\left(\operatorname{Sizel} \boldsymbol{L}\right)_{\max }$. In the basic EDA, a large population size is always desired to maintain the search diversity. In $\mathrm{E}_{3}$-EDA, five values of population size are used, namely, NP $=12 \cdot D, 15 \cdot D, 18 \cdot D, 21 \cdot D$, and $24 \cdot D$, where $D$ denotes the problem dimensionality. Archive $\boldsymbol{A}$ retains population information of successive generations; therefore, its optimal size is related to the population size, i.e., $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=$ NP, 2-NP, $3-\mathrm{NP}, 4-\mathrm{NP}$, and $5-\mathrm{NP}$. The set $\boldsymbol{L}$ preserves several top leader solutions to inform the mean point modification. Its optimal value is determined from six cases: $\operatorname{Sizel} \boldsymbol{L}_{\max }=1,0.1-\mathrm{NP}$, $0.2 \cdot \mathrm{NP}, 0.3 \cdot \mathrm{NP}, 0.4 \cdot \mathrm{NP}$, and $0.5 \cdot \mathrm{NP}$. When the size of $\boldsymbol{L}$ equals 1 , only the best solution is utilized. While the size of $\boldsymbol{L}$ is set to $0.5-\mathrm{NP}$, the first half of the best population is preserved. We associate the parameter assignment with the problem size so that $\mathrm{E}_{3}$-EDA can adaptively adjust its parameter values when dealing with problems of different dimensions. This step is performed to reduce the parameter sensitivity of the algorithm and avoid the parameter adjustment burden.

In this investigation, CEC 2014 benchmarks are employed to evaluate the $\mathrm{E}_{3}$-EDA performance with $150(5 \times 5 \times 6)$ different parameter settings. The experiments are carried out with 30D problems, and each problem is run for 51 times independently. The maximum function evaluation is fixed at 300,000. To save space, we do not provide the optimization results of the 150 algorithms. However, the Friedman test is performed to rank the results to reveal the differences. Since the three free parameters are related to the population size, we analyze the influence of the other two parameter settings on the algorithm performance with different NP values. For NP set to $12 \cdot D, 15 \cdot D, 18 \cdot D, 21 \cdot D$, and $24 \cdot D$, the influence of the parameters $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}$ and $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}$ on the algorithm performance is tabulated in Tables 1, 2, 3, 4 and 5. The ranking differences are illustrated in Figs. 6, 7, 8, 9 and 10. With the population size NP taking these five different values, most of the best points are accompanied by the parameter $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}$ being equal to $3-\mathrm{NP}$ and $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}$ being equal to $0.1-\mathrm{NP}$. The best parameter settings occur at NP $=18 \cdot D, \operatorname{Sizel} \boldsymbol{A}_{\max }=$ 3-NP, and $\operatorname{Sizel} \boldsymbol{L}_{\max }=0.1 \cdot \mathrm{NP}$, as shown in Table 3, where the statistical ranking value is the lowest at 38.2857 .

We sum the data values in Tables 1, 2, 3, 4 and 5 by rows or columns. Then, taking the mean value, we can perform a statistical analysis on the influence of the parameters $\operatorname{sizel} \boldsymbol{A}_{\text {max }}$ or $\operatorname{sizel} \boldsymbol{L}_{\max }$ independently on the algorithm performance under different population sizes, as presented in Figs. 11 and 12, respectively. It can be concluded that the optimal values of parameter $\operatorname{sizel} \boldsymbol{A}_{\text {max }}$ and $\operatorname{sizel} \boldsymbol{L}_{\max }$ are $3-\mathrm{NP}$ and $0.1-\mathrm{NP}$, respectively. Moreover, the curve variations in Fig. 11 are greater than those in Fig. 12, which can be summarized as

![img-5.jpeg](img-5.jpeg)

Fig. 6 When NP $=12 \cdot D$, the best ranking value 51.9524 is obtained at $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=5 \cdot \mathrm{NP}$ and $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=0.1 \cdot \mathrm{NP}$

![img-6.jpeg](img-6.jpeg)

Fig. 7 When NP $=15 \cdot D$, the best ranking value 43.9524 is obtained at $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=5 \cdot \mathrm{NP}$ and $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=0.1 \cdot \mathrm{NP}$

![img-7.jpeg](img-7.jpeg)

Fig. 8 When NP $=18 \cdot D$, the best ranking value 38.2857 is obtained at $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=5 \cdot \mathrm{NP}$ and $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=0.1 \cdot \mathrm{NP}$
follows: the influence of the value of parameter $\operatorname{sizel} \boldsymbol{A}_{\text {max }}$ on algorithm performance is greater than that of parameter $\operatorname{sizel} \boldsymbol{L}_{\text {max }}$. By summing all the values in Tables 1, 2, 3, 4 and 5 , we can compare the effects of different population sizes on the algorithm's performance. The satisfactory settings of NP are $18 \cdot D$ and $21 \cdot D$, with a minimal difference between the two ranking values of 70.619 and 70.4032 , respectively. We

![img-8.jpeg](img-8.jpeg)

Fig. 9 When NP $=21 \cdot D$, the best ranking value 42.5714 is obtained at $\operatorname{Sizel} \boldsymbol{A} \mid \max =5 \cdot \mathrm{NP}$ and $\operatorname{Sizel} \boldsymbol{L} \mid \max =0.1 \cdot \mathrm{NP}$
![img-9.jpeg](img-9.jpeg)

Fig. 10 When NP $=24 \cdot D$, the best ranking value 44.6667 is obtained at $\operatorname{Sizel} \boldsymbol{A} \mid \max =5 \cdot \mathrm{NP}$ and $\operatorname{Sizel} \boldsymbol{L} \mid \max =0.1 \cdot \mathrm{NP}$
![img-10.jpeg](img-10.jpeg)

Fig. 11 Ranking variations of different values of $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }$
choose $18 \cdot D$ as the optimal population size because a larger population size can increase the computational cost since the maximum time complexity is $O\left\{D^{2} \times \max (D, \mathrm{NP})\right\}$. In summary, the optimal parameter settings of $\mathrm{E}_{3}$-EDA are NP $=$ $18 \cdot D, \operatorname{sizel} \boldsymbol{A} \mid_{\max }=3 \cdot \mathrm{NP}$ and $\operatorname{sizel} \boldsymbol{L} \mid \max =0.1 \cdot \mathrm{NP}$.
![img-11.jpeg](img-11.jpeg)

Fig. 12 Ranking variations of different values of $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }$

## Investigation of the influence of $\mathrm{E}_{3}$-EDA search behavior

In this subsection, we investigate the influence of three different search behaviors on the optimization results and convergence performance of $\mathrm{E}_{3}$-EDA. First, four $\mathrm{E}_{3}$-EDA variants are designed, namely, $\mathrm{E}_{3}$-EDA-1, $\mathrm{E}_{3}$-EDA-2, $\mathrm{E}_{3}$ -EDA-3, and $\mathrm{E}_{3}$-EDA-4; compared with the original $\mathrm{E}_{3}$-EDA, the first three algorithms remove the APU, MSD, and TDS mechanisms, respectively. In $\mathrm{E}_{3}$-EDA-4, the two behaviors in MSD are randomly selected (which means $P_{1}=P_{2}=0.5$ ) instead of using the adaptive probability adjustment mechanism. Moreover, the basic multivariate Gaussian EDA, i.e., $\mathrm{EMNA}_{\mathrm{g}}$, is considered a competitor to verify the effectiveness of our proposed modifications. The performances of the six algorithms are evaluated using the CEC 2014 testbed with 30D problems. 51 independent evaluations are made for each benchmark with the same algorithm parameter settings, i.e., NP $=18 \cdot D, \operatorname{sizel} \boldsymbol{A} \mid \max =3 \cdot \mathrm{NP}$ and $\operatorname{sizel} \boldsymbol{L} \mid \max$ $=0.1 \cdot$ NP. In addition, $\mathrm{FEs}_{\max }$ is constrained at 300,000 , and the experimental results are recorded in Table 6. The last row in Table 6 shows the rank difference among the six algorithms according to the Friedman test. $\mathrm{E}_{3}$-EDA, with all three search mechanisms integrated, obtains the best rank value of $1.9500 . \mathrm{E}_{3}$-EDA-4 is the next-best-scoring algorithm, achieving a rank value of 2.1833 . The next followers are $\mathrm{E}_{3}$-EDA-2 and $\mathrm{E}_{3}$-EDA-3, with rank values of 2.9833 and 3.7167 , respectively. The last two methods are $\mathrm{E}_{3}$-EDA1 and $\mathrm{EMNA}_{\mathrm{g}}$ with the poorest ranks of 4.6333 and 5.5333, respectively. The worse the ranking value of the algorithm, the more substantial the influence of the missing part on the algorithm performance. APU is the most important component to ensure the high performance of $\mathrm{E}_{3}$-EDA. It considers and uses the historical distribution information to support the estimation of the current distribution model, while effectively avoiding an ill-conditioned distribution caused by the algorithm using only the current solution information. Comparing the optimization results of $\mathrm{E}_{3}$-EDA and $\mathrm{E}_{3}$-EDA-3, it can be

Table 6 Comparison results of the four $\mathrm{E}_{3}$-EDA variants

The bold data indicates the optimal result
The Chi-square of the Friedman test is 92.7140 , and the $p$ value is $1.8069 \mathrm{e}-18$
found that the TDS strategy can enhance the algorithm performance to solve the multimodal complex problem. TDS can shrink the search scope to help the algorithm perform local exploitation. In addition, $\mathrm{E}_{3}$-EDA has better performance than $\mathrm{E}_{3}$-EDA-2 in solving unimodal functions, which proves that MSD can effectively evolve the search to the dominant region. Furthermore, the gap between $\mathrm{E}_{3}$-EDA and $\mathrm{E}_{3}$-EDA-4 is less than others. The proportion adaptive change trends of the two mechanisms included in MSD on different benchmarks can be found in Appendix A. According to the
statistics of the test results, the mean value of $P_{1}$ in the whole test is 0.4949 and that of $P_{2}$ is 0.5051 . Although both values are close to 0.5 , as seen in Appendix A, the change in trend of $P_{1}$ and $P_{2}$ are different on different functions, as well as different stages of the same function. The advantage of $\mathrm{E}_{3}$ EDA compared with $\mathrm{E}_{3}$-EDA-4 verifies the rationality and effectiveness of our adaptive scaling strategy Eqs. (11)-(15).

Moreover, we study the effect of the three search mechanisms on the convergence performance of the algorithm. We select eight test functions with considerable differences in

![img-12.jpeg](img-12.jpeg)

Fig. 13 Convergence analysis on F1
![img-13.jpeg](img-13.jpeg)

Fig. 14 Convergence analysis on F9
![img-14.jpeg](img-14.jpeg)
(a) Mean error value convergence plot
![img-15.jpeg](img-15.jpeg)
(b) Mean $D_{\mathrm{E}}$ convergence plot
![img-16.jpeg](img-16.jpeg)
(b) Mean $D_{\mathrm{E}}$ convergence plot

Fig. 15 Convergence analysis on F11

Table 6 to analyze the convergence of the algorithm. These eight benchmark functions are F1, F9, F11, F15, F17, F21, F27 and F29. We plot the convergence curves to compare the convergence performance of the four algorithms in Fig. 13a, $14,15,16,17,18,19$ and 20a. The convergence performance of the population distribution is analyzed using the variant of the mean value of the Euclidean distance between the pop-
ulation and its current optimal individual, as presented in Figs. 13b, 14, 15, 16, 17, 18, 19 and 20b. The mean value of the Euclidean distance is calculated as follows:

![img-17.jpeg](img-17.jpeg)

Fig. 16 Convergence analysis on F15
![img-18.jpeg](img-18.jpeg)

Fig. 17 Convergence analysis on F17
![img-19.jpeg](img-19.jpeg)
![img-20.jpeg](img-20.jpeg)
(b) Mean $D_{\mathrm{E}}$ convergence plot
![img-21.jpeg](img-21.jpeg)
(b) Mean $D_{\mathrm{E}}$ convergence plot
![img-22.jpeg](img-22.jpeg)

Fig. 18 Convergence analysis on F21
$\operatorname{Mean} D_{\mathrm{E}}=\frac{1}{\mathrm{NP}} \sum_{i=1}^{\mathrm{NP}}\left(\boldsymbol{x}_{i}-\boldsymbol{x}_{\text {best }}\right)$.

Figures 13a, 14, 15, 16, 17, 18, 19 and 20a show that the convergence speed of the different algorithms is approximately the same as their population distribution shrinking
speed. Among the four algorithms, without the MSD strategy, $\mathrm{E}_{3}$-EDA-2 has the fastest convergence speed. This is due to the MSD strategy in the other three algorithms expanding the search scope, which delays the convergence performance. However, the absence of the MSD search behavior in $\mathrm{E}_{3}$ -EDA-2 leads to its incomplete exploration of the solution space, which makes its performance inferior to $\mathrm{E}_{3}$-EDA in

![img-23.jpeg](img-23.jpeg)

Fig. 19 Convergence analysis on F27
![img-24.jpeg](img-24.jpeg)

Fig. 20 Convergence analysis on F29
the optimization results of the eight benchmarks. The convergence rate and the convergence of the population distribution of $\mathrm{E}_{3}$-EDA-1 and $\mathrm{E}_{3}$-EDA-3 are poorer than those of the basic $\mathrm{E}_{3}$-EDA, but the reasons for this are different. The absence of the APU strategy makes the $\mathrm{E}_{3}$-EDA-1 algorithm unable to capture the problem characteristics effectively, resulting in an abnormal distribution of the population. However, due to the absence of the TDS strategy, the search range of $\mathrm{E}_{3}$ -EDA-3 is too large, precluding effective convergence to the dominant region. Generally, with an ensemble of three strategies, $\mathrm{E}_{3}$-EDA achieves the best performance in terms of both the optimization results and the convergence performance. According to the above analysis of the test results, the ranking of the influence of the three strategies on the algorithm performance from large to small is APU $>$ TDS $>$ MSD.

## Comparison with LSHADE-EpSin, UMOEAsII, L-SHADE, MLS-EDA and ACSEDA using the CEC 2014 test suite

To assess the performance of our $\mathrm{E}_{3}$-EDA in solving the numerical optimization problem, the CEC 2014 and CEC
![img-25.jpeg](img-25.jpeg)
(b) Mean $D_{\mathrm{E}}$ convergence plot
![img-26.jpeg](img-26.jpeg)
2018 test suites are employed as benchmarks. Both sets of benchmarks are evaluated in $10-D, 30-D, 50-D$, and $100-D$. The maximum function evaluation numbers are set to 10 $\times 10,000,30 \times 10,000,50 \times 10,000$ and $100 \times 10,000$, respectively. Each function runs 51 times independently. The error values are recorded statistically in Appendices B and C, including the best, worst, median, mean, and standard deviation (SD) values. As the complexity and scale of the problem increase, the error values of the solutions become larger, especially in addressing the last two types of hybrid and composite benchmarks.

To further evaluate the performance of our method, we employ several state-of-the-art algorithms that perform competitively in the CEC 2014 test: LSHADEEpSin, UMOEAsII, L-SHADE, MLS-EDA and ACSEDA. LSHADE-EpSin and UMOEAsII won the first two places for the CEC 2014 competition held in 2016. L-SHADE is the basic version of LSHADE-EpSin and was the winner of the CEC 2014 competition held in 2014. MLS-EDA and ACSEDA are two recently developed promising EDA variants. The superior performance of these five competitors was verified using CEC 2014 benchmarks in their original works.

Table 7 Parameter settings of $\mathrm{E}_{3}$-EDA, LSHADE-EpSin, UMOEAsII, L-SHADE, MLS-EDA and ACSEDA in the CEC 2014 test

The parameter settings of all participants follow their literatures as tabulated in Table 7.

The mean and SD values derived from the six algorithms are recorded in Tables 8, 9, 10 and 11. for the $10 \cdot D, 30 \cdot D$, $50 \cdot D$ and $100 \cdot D$ tests, respectively. For the first three unimodal functions, $\mathrm{E}_{3}$-EDA, MLS-EDA and ACSEDA show their robustness in finding the optimal values in all the $10 \cdot D$, $30 \cdot D$ and $50 \cdot D$ tests. For the multimodal functions, $\mathrm{E}_{3}$-EDA, LSHADE-EpSin and UMOEAsII are the top three methods in terms of accuracy. Specifically, in $30 \cdot D, \mathrm{E}_{3}$-EDA wins more than half of these 13 problems. The remaining L-SHADE, MLS-EDA and ACSEDA are less competitive, but all three methods can reach the optimal result on F7 regardless of the dimensionality. Additionally, for the hybrid functions F17-F22, our $\mathrm{E}_{3}$-EDA exhibits its superiority because it performs best on more than half of the benchmarks in four groups of tests except the $10 \cdot D$ test. The hybrid functions are partially separable problems that are close to real-world optimization problems. The domination of $\mathrm{E}_{3}$-EDA in solving this set of tasks verifies its potential in real world applications. As in solving the last eight composite functions, LSHADE-EpSin and UMOEAsII are the two competitive algorithms in all tests. MLS-EDA outperforms the other methods in the 30D test. Our $\mathrm{E}_{3}$-EDA has similar performance to L-SHADE and surpasses ACSEDA. From an overall view, according to the mean error data, our $\mathrm{E}_{3}$-EDA wins 13 out of 30 benchmarks in the 10D test, 17 in the $30 \cdot D$ test, 14 in the $50 \cdot D$ test and 6 in the $100 \cdot D$ test.

According to the mean error results, the performance of the six competitors on different types of test functions is statistically compared in Table 12. On this basis, $\mathrm{E}_{3}$-EDA has great advantages over other methods in solving hybrid problems and performs competitively in solving unimodal and multimodal functions. ACSEDA, UMOEAsII and LSHADEEpSin perform best in solving unimodal, multimodal, and composite tests, respectively.

To further demonstrate the superiority of our algorithm in a comprehensive manner, nonparametric tests are performed. Table 13 presents pairwise comparison results using the Wilcoxon signed-rank test for CEC 2014 10-D, 30-D,
$50 \cdot D$ and $100 \cdot D$ tests. The symbols " $\pm / \approx$ " indicate that our $\mathrm{E}_{3}$-EDA has superior, inferior, or similar performance in comparison with other methods based on the evaluated mean error values in Tables 8, 9, 10 and 11. In the following two columns, the symbol " $R+$ " denotes the magnitude with which $\mathrm{E}_{3}$-EDA can surpass the competitor, and " $R$-" expresses the opposite effect. The rightmost column records the $p$ value derived from the Wilcoxon signed-rank test. If the $p$ value is greater than the significance level $(\alpha=0.05)$, the comparison of the two algorithms is regarded to be statistically insignificant. Otherwise, $\mathrm{E}_{3}$-EDA is concluded to be better or worse based on the " $R+$ " magnitude. As seen in Table 14, E3-EDA has notable superiority compared with MLSEDA and ACSEDA in the $10 \cdot D$ test, outmatches L-SHADE and ACSEDA in the $30 \cdot D$ test, and surpasses L-SHADE and MLS-EDA in the $100 \cdot D$ test.

Moreover, the Friedman test is operated to perform a multiple comparison and rank these six algorithms according to their comprehensive performance. The ranking results for the three tests are presented in Table 14. $\mathrm{E}_{3}$-EDA ranks best among the six algorithms with values of 3.0167 in the 30D test, 3.1167 in the $50 \cdot D$ test and 2.8500 in the $100 \cdot D$ test, and ranks second with a score of 3.1000 in the $10 \cdot D$ test. The outperformance of $\mathrm{E}_{3}$-EDA is supported by the nonparametric studies in the CEC 2014 test, which demonstrates that our developed three search components are conducive to improving the algorithm performance.

In addition to the evidence provided by these optimization results, the execution time is another crucial issue to evaluate the algorithm's effectiveness. The average time consumptions in the same platform derived from all six participants on each benchmark in the CEC 2014 three tests are recorded in Appendix D. On this basis, Table 15 parallels the average time consumption of the six algorithms in different dimensional tests. According to these results, ACSEDA and L-SHADE are the two most efficient algorithms. Our $\mathrm{E}_{3}$-EDA has similar computational efficiency to MLS-EDA and is superior to UMOEAsII and LSHADE-EpSin. Although $\mathrm{E}_{3}$-EDA is not the most efficient algorithm; it has fewer gaps with ACSEDA

Table 8 Experimental results derived from six algorithms in the CEC 2014 10-D test
The bold data indicates the optimal result
based on the recorded results in addressing low-dimensional problems.

## Comparison with HSES, LSHADE-RSP, ELSHADE-SPACMA, EBOwithCMAR and ACSEDA using the CEC 2018 test suite

To further verify the effectiveness of our proposal, another test using the CEC 2018 testbed is carried out. Five competitors are employed to make a comparison, including HSES, LSHADE-RSP, ELSHADE-SPACMA, EBOwithCMAR and ACSEDA. HSES, LSHADE-RSP, and ELSHADE-SPACMA are the top three methods of the CEC 2018 test. EBOwithCMAR is the champion of the CEC 2017 competition. ACSEDA represents a novel EDA variant. The parameters of each algorithm are assigned according to the original work, as shown in Table 16. LSHADE-RSP is coded using the C version. Its experimental data are taken from its original work. For the other five algorithms, all 29 benchmarks in CEC 2018 are evaluated 51 times with a fixed evaluation number of $D \times 10,000$. The statistical data, including the mean error and SD values, are presented in Tables 17, 18,19 and 20.

The first two unimodal functions are easily addressed because all participants can access the acceptable error values in all tests. In addition, for the following seven multimodal functions, $\mathrm{E}_{3}$-EDA, EBOwithCMAR and ACSEDA are the top three algorithms in solving $10-D$ problems. Moreover,

Table 9 Experimental results derived from six algorithms in the CEC 2014 30-D test
The bold data indicates the optimal result
$\mathrm{E}_{3}$-EDA wins all benchmarks except F4 in the $30-D$ test and ranks first on F7, F9 and F10 in the $50-D$ trial. HSES obtains the best results on F4 in all four groups of tests. Furthermore, all six algorithms perform robustly on F6 and F9. For the hybrid functions in the 10D test, EBOwithCMAR obtains better results than the other algorithms, while $\mathrm{E}_{3}$-EDA performs best on F14. For the $30-D$ test, ACSEDA obtains the best result only on F16. The best values of the remaining 9 functions are accessed by our $\mathrm{E}_{3}$-EDA. The advantage of our $\mathrm{E}_{3}$-EDA is the highest in each row. In the $50-D$ test, $\mathrm{E}_{3}$-EDA is the best performing algorithm with the best values on F11, F12, F13, F16, F18 and F19. HSES ranks at the top on F14 and F15, while ACSEDA ranks first on F17 and F20. In the $100-D$ test, $\mathrm{E}_{3}$-EDA is also proven to be the best problem
solver by winning on F12, F13, F15, F16 and F19. For the last group of 10 composite functions, $\mathrm{E}_{3}$-EDA wins on more than half of the functions except in the 10D test.

In general, EBOwithCMAR is the top algorithm in the $10-D$ test, while our $\mathrm{E}_{3}$-EDA has prominent advantages over the other five algorithms in the remaining three tests. Specifically, $\mathrm{E}_{3}$-EDA obtains the best results for almost all 29 benchmarks in the $30-D$ test except F4, F16, F21, F28, F29 and F30. In the $50-D$ test, $\mathrm{E}_{3}$-EDA ranks first on 17 out of 29 benchmarks. Moreover, $\mathrm{E}_{3}$-EDA obtains as many as 13 results better than other algorithms in the $100-D$ test.

To compare the performance of different algorithms more clearly in solving different types of problems, Table 21 compares the ranking results of the six algorithms. $\mathrm{E}_{3}$-EDA

Table 10 Experimental results derived from six algorithms in the CEC 2014 50-D test
The bold data indicates the optimal result
possesses the best performance in solving multimodal, hybrid and composite problems. HSES has robust performance in gaining the best results on unimodal functions.

Similarly, the Wilcoxon signed-rank test is performed to conduct a pairwise comparison between $\mathrm{E}_{3}$-EDA and each competitor. The symbols in Table 22 have the same meaning as explained in the previous section. According to the $p$ value recorded in the right column of Table 22, for the $10-D$ test, $\mathrm{E}_{3}$-EDA obtains similar performance to LSHADE-RSP, ELSHADE-SPACMA, and EBOwithCMAR but has substantial dominance to HSES and ACSEDA. For the remaining three tests, $\mathrm{E}_{3}$-EDA surpasses every competitor except HSES and ACSEDA in the $100-D$ test.

Moreover, the Friedman test is carried out to distinguish the differences among the six algorithms. Table 23 provides the rankings of each participant in the four CEC 2018 tests. $\mathrm{E}_{3}$-EDA ranks at the top with the smallest ranking values of 1.9483 in the $30-D$ test, 2.0690 in the $50-D$ test and 2.500 in the $100-D$ test. For the $10-D$ test, LSHADE-RSP performs best, and $\mathrm{E}_{3}$-EDA ranks third, following EBOwithCMAR. From an overall viewpoint of the ranking results of different dimension tests, $\mathrm{E}_{3}$-EDA possesses more competitive performance than other algorithms.

The execution times of all competitors except LSHADERSP are compared in Appendix E, which shows the average time required by these five competitors to optimize each function. Table 24 compares the average amounts of time required

Table 11 Experimental results derived from six algorithms in the CEC 2014 100-D test
The bold data indicates the optimal result
by these eight algorithms to solve the benchmarks of different dimensionalities. ACSEDA is the most efficient algorithm. $\mathrm{E}_{3}$-EDA has similar performance to ELSHADE-SPACMA in terms of time consumption and surpasses the remaining two algorithms.

Through the above experimental studies, the competitive performance of our $\mathrm{E}_{3}$-EDA is fully demonstrated with comparisons of the top methods in CEC competitions. In addition to the superiority in optimization accuracy, our $\mathrm{E}_{3}$-EDA possesses another two advantages. First, $\mathrm{E}_{3}$-EDA has fewer free parameters than other state-of-the-art methods, which can enhance its robustness in dealing with different problems.

On the other hand, the optimal parameter values are determined in the CEC 2014 30-D test, and these settings also support the promising performance of $\mathrm{E}_{3}$-EDA in addressing the CEC 2018 problems, which demonstrates the insensitivity of the algorithm performance to parameter settings. Second, $\mathrm{E}_{3}$-EDA not only achieves the best performance but also shows satisfactory computational efficiency. High efficiency and accuracy are two important indexes for assessing an evolutionary algorithm in practical engineering applications. Thus, our proposal has great potential for addressing real world optimization problems.

Table 12 Performance ranking of six algorithms for different types of test functions in different dimension CEC 2014 tests

The bold data indicates the optimal result

Table 13 Pairwise comparison using the Wilcoxon signed-rank test for the CEC 2014 test $(\alpha=$ 0.05 )

Table 14 Multi-comparison using the Friedman test for the CEC 2014 test $(\alpha=0.05)$
The bold data indicates the optimal result ${ }^{\mathrm{a}} p$ value is $8.26 \mathrm{e}-07$, Chi-square is 36.30 ${ }^{\mathrm{b}} p$ value is $4.40 \mathrm{e}-02$, Chi-square is 11.40 ${ }^{\mathrm{c}} p$ value is $2.97 \mathrm{e}-01$, Chi-square is 6.09 ${ }^{\mathrm{d}} p$ value is $4.02 \mathrm{e}-04$, Chi-square is 22.60

The bold data indicates the optimal result
Table 16 Parameter settings of $\mathrm{E}_{3}$-EDA, HSES, LSHADE-RSP, ELSHADE-SPACMA, EBOwithCMAR, and ACSEDA in the CEC2017 test

## Conclusions

As a newly developed EDA algorithm, the search behaviors of $\mathrm{E}_{3}$-EDA with the ensemble of APU, MSD, and TDS are introduced. APU utilizes historical population information to conduct distribution estimation to avoid ill conditioning. The MSD utilizes the location differences among individuals to extend the search scope toward dominant regions. TDS can shrink the search scope and help the algorithm focus on local exploitation. Through experimental studies, the optimal parameter settings of $\mathrm{E}_{3}$-EDA are established, and the influence of the proposed modifications on the algorithm performance in terms of optimization and convergence are discussed.

The $\mathrm{E}_{3}$-EDA performance is evaluated using the CEC 2014 and CEC 2018 test suites. The $10 \cdot D, 30 \cdot D, 50 \cdot D$, and
$100 \cdot D$ tests are carried out with two sets of problems. Comparisons with the top methods in CEC competitions and other promising EDA variants are performed. According to the nonparametric test results, the performance of $\mathrm{E}_{3}$-EDA with APU, MSD and TDS integrated in solving the two groups of CEC tests is more competitive than the advanced algorithms in terms of accuracy and efficiency, especially outperforming MLS-EDA, which proves the effectiveness of our extended investigation based on previous work to improve the EDA algorithm performance.

Future work can address three aspects. First, the search framework of $\mathrm{E}_{3}$-EDA needs improvement, especially the MSD strategy. The random values in mean point modification must be determined in a more reasonable way. Second, $\mathrm{E}_{3}$-EDA can be further developed with ensembles of other techniques, such as fitness landscape detection and adaptive

![img-27.jpeg](img-27.jpeg)

![img-28.jpeg](img-28.jpeg)

![img-29.jpeg](img-29.jpeg)

![img-30.jpeg](img-30.jpeg)

Table 21 Performance ranking of six algorithms for different types of test functions in different dimension CEC 2018 tests

The bold data indicates the optimal result

Table 22 Pairwise comparison using the Wilcoxon signed-rank test for the CEC 2018 tests

Table 23 Multi-comparison using the Friedman test for the CEC 2018 tests $(\alpha=0.05)$
The bold data indicates the optimal result
${ }^{a} p$ value is $6.43 \mathrm{e}-05$, Chi-square is 26.73
${ }^{b} p$ value is $1.78 \mathrm{e}-07$, Chi-square is 39.62
${ }^{c} p$ value is $2.11 \mathrm{e}-07$, Chi-square is 39.25
${ }^{d} p$ value is $4.18 \mathrm{e}-07$, Chi-square is 37.78

Table 24 Comparison of the computational efficiency for the CEC 2018 tests
population size adjustment. Moreover, it would be highly interesting to explore a hybrid algorithm of $\mathrm{E}_{3}$-EDA with modern DE algorithms, such as L-SHADE. Finally, it is also important to apply $\mathrm{E}_{3}$-EDA to address some challenging real world optimization problems.

Data availability Data can be obtained by contacting the corresponding author Xiaofei Wang.

## Declarations

Conflict of interest The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecomm ons.org/licenses/by/4.0/.

## Appendix

A. The proportion changes of $P_{1}$ and $P_{2}$ on different test functions of CEC 2014 30-D test.

![img-31.jpeg](img-31.jpeg)

![img-32.jpeg](img-32.jpeg)
![img-33.jpeg](img-33.jpeg)
![img-34.jpeg](img-34.jpeg)
![img-35.jpeg](img-35.jpeg)
![img-36.jpeg](img-36.jpeg)
![img-37.jpeg](img-37.jpeg)
![img-38.jpeg](img-38.jpeg)
![img-39.jpeg](img-39.jpeg)
![img-40.jpeg](img-40.jpeg)
![img-41.jpeg](img-41.jpeg)
![img-42.jpeg](img-42.jpeg)

B. Statistical results obtained from the $\mathrm{E}_{3}$-EDA for the CEC 2014 10-D, 30-D, 50-D and 100-D tests.

C. Statistical error results obtained from the $\mathrm{E}_{3}$-EDA for the CEC 2018 10-D, 30-D, 50-D and 100-D tests.



D. Comparison of the computational costs of the six algorithms in the CEC 2014 10-D, 30-D, 50-D and 100-D tests (second).

E. Comparison of the computational costs of the six algorithms in the CEC 2018 10-D, 30-D, 50-D and 100-D tests (second).


