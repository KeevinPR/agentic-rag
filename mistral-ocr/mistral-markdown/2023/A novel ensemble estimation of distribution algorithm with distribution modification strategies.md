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

|  | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=1 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=2 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=3 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=4 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=5 \cdot \mathrm{NP}$ | Mean |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=1$ | 136.3810 | 97.7619 | 92.1905 | 91.9524 | 87.7143 | 101.2000 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 124.4286 | 73.3810 | 62.1429 | 60.7619 | 51.9524 | 74.5333 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 134.7619 | 71.5238 | 76.7619 | 62.1429 | 59.3333 | 80.9048 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 135.0952 | 74.4286 | 66.9524 | 61.9524 | 65.8810 | 80.8619 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 141.9048 | 77.5714 | 73.6190 | 66.5714 | 63.4524 | 84.6238 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 144.2381 | 84.3810 | 68.1429 | 64.2857 | 66.7143 | 85.5524 |
| $\operatorname{Mean}$ | 136.1349 | 79.8413 | 73.3016 | 67.9444 | 65.8413 | 84.6127 |

Table 2 Rankings of algorithms with different $\operatorname{sizel} A l$ and $\operatorname{sizel} L l$ settings when $\mathrm{NP}=12 \cdot D$

|  | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=1 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=2 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=3 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=4 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=5 \cdot \mathrm{NP}$ | Mean |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=1$ | 137.1429 | 91.1429 | 86.5714 | 77.5238 | 67.0476 | 91.8857 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 122.5714 | 64.0000 | $\mathbf{4 3 . 9 5 2 4}$ | 44.2857 | 47.2381 | 64.4095 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 128.2381 | 67.2381 | 51.2857 | 57.5714 | 58.1905 | 72.5048 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 135.7619 | 79.8571 | 52.2857 | 48.2381 | 53.6667 | 73.9619 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 140.0952 | 78.2381 | 49.3333 | 59.5238 | 61.7143 | 77.7810 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 141.6667 | 65.9048 | 55.3810 | 50.2381 | 52.4286 | 73.1238 |
| $\operatorname{Mean}$ | 134.2460 | 74.3968 | 56.4683 | 56.2302 | 56.7143 | 75.6111 |

The bold data indicates the optimal result

Table 3 Rankings of algorithms with different $\operatorname{sizel} A l$ and $\operatorname{sizel} L l$ settings when $\mathrm{NP}=18 \cdot D$

|  | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=1 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=2 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=3 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=4 \cdot \mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A}_{\text {max }}=5 \cdot \mathrm{NP}$ | Mean |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=1$ | 135.8571 | 81.4762 | 71.4762 | 64.5714 | 58.6667 | 82.4095 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 120.2857 | 52.0476 | $\mathbf{3 8 . 2 8 5 7}$ | 45.9048 | 45.8095 | 60.4667 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 123.9048 | 56.5238 | 41.1429 | 49.6667 | 57.9048 | 65.8286 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 128.2857 | 58.9524 | 57.2381 | 50.3333 | 52.1429 | 69.3905 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 131.9524 | 65.3333 | 53.9524 | 48.4762 | 50.2857 | 70.0000 |
| $\operatorname{Sizel} \boldsymbol{L}_{\text {max }}=$ | 133.4762 | 68.7143 | 60.1429 | 51.8571 | 63.9048 | 75.6190 |
| $\operatorname{Mean}$ | 128.9603 | 63.8413 | 53.7063 | 51.8016 | 54.7857 | 70.6190 |

The bold data indicates the optimal result

Table 4 Rankings of algorithms with different size $(A)$ and size $(L)$ settings when $\mathrm{NP}=21-D$

|  | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=1-\mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=2-\mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=3-\mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=4-\mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=5-\mathrm{NP}$ | Mean |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=1$ | 136.0476 | 78.3333 | 62.5714 | 61.7619 | 53.4762 | 78.4381 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 117.6667 | 47.6667 | 46.3810 | 52.1429 | 62.4762 | 65.2667 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 120.6190 | 52.7619 | $\mathbf{4 2 . 5 7 1 4}$ | 47.8095 | 58.8571 | 64.5238 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 124.8095 | 56.7619 | 55.4286 | 58.6667 | 62.9048 | 71.7143 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 124.0952 | 62.7619 | 50.4286 | 50.3333 | 56.5238 | 68.8286 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 122.3333 | 75.6667 | 45.2857 | 60.7143 | 64.2381 | 73.6476 |
| $\operatorname{Mean}$ | 124.2619 | 62.3254 | 50.4444 | 55.2381 | 59.7460 | 70.4032 |

The bold data indicates the optimal result
Table 5 Rankings of algorithms with different size $(A)$ and size $(L)$ settings when $\mathrm{NP}=24-D$

|  | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=1-\mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=2-\mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=3-\mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=4-\mathrm{NP}$ | $\operatorname{Sizel} \boldsymbol{A} \mid_{\max }=5-\mathrm{NP}$ | Mean |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=1$ | 134.5238 | 74.1905 | 65.7619 | 55.0952 | 57.7619 | 77.4667 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 119.8095 | 59.3810 | $\mathbf{4 4 . 6 6 6 7}$ | 60.8571 | 71.9048 | 71.3238 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 124.3810 | 64.1429 | 58.9524 | 75.6667 | 71.2381 | 78.8762 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 123.5714 | 64.2381 | 62.1905 | 65.5238 | 73.6190 | 77.8286 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 124.6667 | 66.9048 | 46.4286 | 67.1429 | 74.8095 | 75.9905 |
| $\operatorname{Sizel} \boldsymbol{L} \mid_{\max }=$ | 120.6667 | 62.8571 | 57.0952 | 66.4762 | 73.0952 | 76.0381 |
| $\operatorname{Mean}$ | 124.6032 | 65.2857 | 55.8492 | 65.1270 | 70.4048 | 76.2540 |

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

| No. | $\mathrm{E}_{3}$-EDA | $\mathrm{E}_{3}$-EDA-1 (without APU) | $\mathrm{E}_{3}$-EDA-2 (without MSD) | $\mathrm{E}_{3}$-EDA-3 (without TDS) | $\mathrm{E}_{3}$-EDA-4 $\left(P_{1}=P_{2}\right.$ <br> $=0.5$ ) | $\mathrm{EMNA}_{g}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Mean $\operatorname{SD}$ | Mean $\operatorname{SD}$ | Mean $\operatorname{SD}$ | Mean $\operatorname{SD}$ | Mean $\operatorname{SD}$ | Mean $\operatorname{SD}$ |
| 01 | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $1.90 \mathrm{e}+07_{6.11 \mathrm{e}+06}$ | $4.99 \mathrm{e}+01_{1.40 \mathrm{e}+02}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $1.79 \mathrm{e}+08_{2.54 \mathrm{e}+07}$ |
| 02 | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $4.88 \mathrm{e}+07_{1.08 \mathrm{e}+08}$ | $1.66 \mathrm{e}+03_{2.17 \mathrm{e}+03}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $2.01 \mathrm{e}+10_{1.15 \mathrm{e}+09}$ |
| 03 | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $9.56 \mathrm{e}+03_{6.53 \mathrm{e}+03}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $1.98 \mathrm{e}+04_{2.42 \mathrm{e}+03}$ |
| 04 | $3.00 \mathrm{e}+00_{8.02 \mathrm{e}+00}$ | $3.16 \mathrm{e}+02_{2.30 \mathrm{e}+01}$ | $7.57 \mathrm{e}+01_{1.99 \mathrm{e}+01}$ | $3.04 \mathrm{e}+00_{1.07 \mathrm{e}+01}$ | $\mathbf{1 . 5 2 e + 0 0}_{2.50 \mathrm{e}+00}$ | $2.28 \mathrm{e}+03_{5.13 \mathrm{e}+02}$ |
| 05 | $\mathbf{2 . 0 0 e + 0 1}_{2.38 \mathrm{e}-01}$ | $2.02 \mathrm{e}+01_{3.07 \mathrm{e}-01}$ | $2.01 \mathrm{e}+01_{1.75 \mathrm{e}-01}$ | $2.10 \mathrm{e}+01_{5.08 \mathrm{e}-02}$ | $\mathbf{2 . 0 0 e + 0 1}_{1.72 \mathrm{e}-01}$ | $2.09 \mathrm{e}+01_{3.90 \mathrm{e}-02}$ |
| 06 | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $6.92 \mathrm{e}+00_{1.59 \mathrm{e}+00}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $5.51 \mathrm{e}+00_{1.17 \mathrm{e}+00}$ |
| 07 | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $7.45 \mathrm{e}+00_{1.12 \mathrm{e}+00}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $2.19 \mathrm{e}+02_{4.53 \mathrm{e}+00}$ |
| 08 | $1.01 \mathrm{e}+00_{8.79 \mathrm{e}-01}$ | $1.51 \mathrm{e}+01_{3.43 \mathrm{e}+00}$ | $8.95 \mathrm{e}+00_{1.99 \mathrm{e}+00}$ | $1.77 \mathrm{e}+02_{1.27 \mathrm{e}+01}$ | $\mathbf{9 . 1 7 e - 0 1 0 . 8 6 e - 0 1}$ | $4.24 \mathrm{e}+01_{1.02 \mathrm{e}+01}$ |
| 09 | $\mathbf{7 . 2 2 e - 0 1 6 . 5 6 e - 0 1}$ | $2.14 \mathrm{e}+01_{1.64 \mathrm{e}+01}$ | $7.43 \mathrm{e}+00_{1.82 \mathrm{e}+00}$ | $1.76 \mathrm{e}+02_{8.43 \mathrm{e}+00}$ | $9.17 \mathrm{e}-01_{7.17 \mathrm{e}-01}$ | $3.33 \mathrm{e}+01_{1.03 \mathrm{e}+01}$ |
| 10 | $\mathbf{2 . 7 2 e + 0 2 6 . 7 7 e + 0 2}$ | $8.04 \mathrm{e}+02_{3.07 \mathrm{e}+02}$ | $3.66 \mathrm{e}+02_{1.86 \mathrm{e}+02}$ | $6.42 \mathrm{e}+03_{2.43 \mathrm{e}+02}$ | $3.13 \mathrm{e}+02_{9.65 \mathrm{e}+02}$ | $9.21 \mathrm{e}+02_{2.98 \mathrm{e}+02}$ |
| 11 | $6.70 \mathrm{e}+01_{7.64 \mathrm{e}+01}$ | $1.34 \mathrm{e}+03_{4.57 \mathrm{e}+02}$ | $5.20 \mathrm{e}+02_{2.55 \mathrm{e}+02}$ | $6.72 \mathrm{e}+03_{2.57 \mathrm{e}+02}$ | $\mathbf{5 . 2 1 e + 0 1 6 . 8 5 e + 0 1}$ | $1.17 \mathrm{e}+03_{1.99 \mathrm{e}+02}$ |
| 12 | $\mathbf{6 . 5 8 e - 0 2}_{3.56 \mathrm{e}-01}$ | $1.32 \mathrm{e}-01_{4.93 \mathrm{e}-02}$ | $8.58 \mathrm{e}-03_{6.39 \mathrm{e}-03}$ | $2.39 \mathrm{e}+00_{3.53 \mathrm{e}-01}$ | $6.67 \mathrm{e}-02_{3.96 \mathrm{e}-01}$ | $2.50 \mathrm{e}+00_{1.79 \mathrm{e}-01}$ |
| 13 | $2.12 \mathrm{e}-01_{4.01 \mathrm{e}-02}$ | $1.86 \mathrm{e}-01_{2.56 \mathrm{e}-02}$ | $2.64 \mathrm{e}-01_{5.31 \mathrm{e}-02}$ | $\mathbf{1 . 4 1 e - 0 1}_{1.80 \mathrm{e}-02}$ | $1.98 \mathrm{e}-01_{3.54 \mathrm{e}-02}$ | $4.81 \mathrm{e}+00_{1.23 \mathrm{e}-01}$ |
| 14 | $3.42 \mathrm{e}-01_{3.67 \mathrm{e}-02}$ | $\mathbf{3 . 4 1 e - 0 1 6 . 5 2 e - 0 2}$ | $3.49 \mathrm{e}-01_{4.55 \mathrm{e}-02}$ | $3.50 \mathrm{e}-01_{4.13 \mathrm{e}-02}$ | $3.49 \mathrm{e}-01_{3.53 \mathrm{e}-02}$ | $1.12 \mathrm{e}+02_{5.50 \mathrm{e}+00}$ |
| 15 | $2.19 \mathrm{e}+00_{5.22 \mathrm{e}-01}$ | $4.51 \mathrm{e}+00_{1.04 \mathrm{e}+00}$ | $2.95 \mathrm{e}+00_{3.12 \mathrm{e}-01}$ | $1.36 \mathrm{e}+01_{9.98 \mathrm{e}-01}$ | $\mathbf{2 . 1 2 e + 0 0}_{6.36 \mathrm{e}+01}$ | $1.13 \mathrm{e}+02_{6.66 \mathrm{e}+01}$ |
| 16 | $\mathbf{6 . 6 6 e + 0 0}_{1.07 \mathrm{e}+00}$ | $9.26 \mathrm{e}+00_{6.17 \mathrm{e}-01}$ | $8.40 \mathrm{e}+00_{4.98 \mathrm{e}-01}$ | $1.26 \mathrm{e}+01_{1.88 \mathrm{e}-01}$ | $6.67 \mathrm{e}+00_{1.09 \mathrm{e}+00}$ | $1.27 \mathrm{e}+01_{1.98 \mathrm{e}-01}$ |
| 17 | $6.23 \mathrm{e}-01_{7.43 \mathrm{e}-01}$ | $3.79 \mathrm{e}+05_{5.86 \mathrm{e}+05}$ | $9.66 \mathrm{e}+01_{6.54 \mathrm{e}+01}$ | $1.11 \mathrm{e}+03_{2.18 \mathrm{e}+02}$ | $\mathbf{5 . 4 8 e - 0 1 6 . 9 5 e - 0 1}$ | $4.33 \mathrm{e}+06_{2.10 \mathrm{e}+06}$ |
| 18 | $\mathbf{5 . 0 0 e - 0 1 6 . 6 7 e - 0 6}$ | $2.58 \mathrm{e}+05_{2.04 \mathrm{e}+05}$ | $1.68 \mathrm{e}+01_{6.09 \mathrm{e}+00}$ | $4.59 \mathrm{e}+01_{5.66 \mathrm{e}+00}$ | $5.00 \mathrm{e}-01_{2.70 \mathrm{e}-03}$ | $2.84 \mathrm{e}+07_{2.91 \mathrm{e}+07}$ |
| 19 | $\mathbf{5 . 9 6 e - 0 1 6 . 2 0 e - 0 1}$ | $6.20 \mathrm{e}+01_{2.13 \mathrm{e}+01}$ | $3.25 \mathrm{e}+00_{5.30 \mathrm{e}-01}$ | $4.07 \mathrm{e}+00_{2.35 \mathrm{e}-01}$ | $6.41 \mathrm{e}-01_{1.81 \mathrm{e}-01}$ | $2.46 \mathrm{e}+01_{1.15 \mathrm{e}+01}$ |
| 20 | $\mathbf{1 . 1 5 e + 0 0}_{2.55 \mathrm{e}-01}$ | $1.42 \mathrm{e}+03_{2.89 \mathrm{e}+03}$ | $4.04 \mathrm{e}+00_{1.55 \mathrm{e}+00}$ | $3.24 \mathrm{e}+01_{2.93 \mathrm{e}+00}$ | $1.18 \mathrm{e}+00_{2.38 \mathrm{e}-01}$ | $4.56 \mathrm{e}+03_{1.54 \mathrm{e}+03}$ |
| 21 | $\mathbf{8 . 8 2 e - 0 1 1 . 2 9 e - 0 1}$ | $3.08 \mathrm{e}+04_{3.93 \mathrm{e}+04}$ | $1.15 \mathrm{e}+02_{9.22 \mathrm{e}+01}$ | $5.96 \mathrm{e}+02_{8.04 \mathrm{e}+01}$ | $4.66 \mathrm{e}+00_{2.72 \mathrm{e}+01}$ | $1.96 \mathrm{e}+05_{1.72 \mathrm{e}+05}$ |
| 22 | $2.68 \mathrm{e}+01_{1.91 \mathrm{e}+01}$ | $4.65 \mathrm{e}+02_{1.85 \mathrm{e}+02}$ | $1.29 \mathrm{e}+02_{4.05 \mathrm{e}+01}$ | $3.91 \mathrm{e}+02_{5.69 \mathrm{e}+01}$ | $\mathbf{2 . 4 3 e + 0 1 1 . 4 8 e + 0 1}$ | $3.17 \mathrm{e}+02_{2.13 \mathrm{e}+02}$ |
| 23 | $\mathbf{3 . 1 5 e + 0 2 0 . 0 0 e + 0 0}$ | $3.44 \mathrm{e}+02_{5.52 \mathrm{e}+00}$ | $\mathbf{3 . 1 5 e + 0 2 2 . 9 4 e - 0 4}$ | $\mathbf{3 . 1 5 e + 0 2 0 . 0 0 e + 0 0}$ | $\mathbf{3 . 1 5 e + 0 2 0 . 0 0 e + 0 0}$ | $3.81 \mathrm{e}+02_{1.77 \mathrm{e}+01}$ |
| 24 | $\mathbf{2 . 1 2 e + 0 2 6 . 7 8 e + 0 0}$ | $2.27 \mathrm{e}+02_{2.57 \mathrm{e}+00}$ | $2.23 \mathrm{e}+02_{1.11 \mathrm{e}+00}$ | $2.12 \mathrm{e}+02_{9.19 \mathrm{e}+00}$ | $2.14 \mathrm{e}+02_{9.31 \mathrm{e}+00}$ | $2.31 \mathrm{e}+02_{2.25 \mathrm{e}+00}$ |
| 25 | $\mathbf{2 . 0 3 e + 0 2 3 . 6 3 e - 0 2}$ | $\mathbf{2 . 0 3 e + 0 2 3 . 7 3 e + 0 0}$ | $\mathbf{2 . 0 3 e + 0 2 2 . 3 7 e - 0 1}$ | $\mathbf{2 . 0 3 e + 0 2 2 . 8 6 e - 0 2}$ | $\mathbf{2 . 0 3 e + 0 2 4 . 3 1 e - 0 2}$ | $2.09 \mathrm{e}+02_{5.23 \mathrm{e}-01}$ |
| 26 | $\mathbf{1 . 0 0 e + 0 2 3 . 3 6 e - 0 2}$ | $\mathbf{1 . 0 0 e + 0 2 4 . 0 0 e - 0 2}$ | $\mathbf{1 . 0 0 e + 0 2 2 . 9 3 e - 0 1}$ | $\mathbf{1 . 0 0 e + 0 2 2 . 3 2 e - 0 2}$ | $\mathbf{1 . 0 0 e + 0 2 2 . 6 9 e - 0 2}$ | $1.08 \mathrm{e}+02_{9.26 \mathrm{e}-01}$ |
| 27 | $3.64 \mathrm{e}+02_{4.80 \mathrm{e}+01}$ | $6.11 \mathrm{e}+02_{6.97 \mathrm{e}+01}$ | $\mathbf{3 . 0 0 e + 0 2 0 . 0 0 e + 0 0}$ | $3.63 \mathrm{e}+02_{4.90 \mathrm{e}+01}$ | $3.76 \mathrm{e}+02_{4.28 \mathrm{e}+01}$ | $5.80 \mathrm{e}+02_{4.46 \mathrm{e}+01}$ |
| 28 | $7.20 \mathrm{e}+02_{1.44 \mathrm{e}+02}$ | $1.40 \mathrm{e}+03_{1.17 \mathrm{e}+02}$ | $\mathbf{3 . 1 6 e + 0 2 6 . 5 7 e + 0 1}$ | $6.97 \mathrm{e}+02_{1.71 \mathrm{e}+02}$ | $7.25 \mathrm{e}+02_{1.32 \mathrm{e}+02}$ | $1.03 \mathrm{e}+03_{1.88 \mathrm{e}+02}$ |
| 29 | $\mathbf{1 . 6 9 e + 0 2 1 . 1 6 e + 0 2}$ | $1.22 \mathrm{e}+05_{1.53 \mathrm{e}+05}$ | $5.03 \mathrm{e}+02_{1.03 \mathrm{e}+02}$ | $1.92 \mathrm{e}+02_{1.80 \mathrm{e}+02}$ | $1.76 \mathrm{e}+02_{1.42 \mathrm{e}+02}$ | $5.11 \mathrm{e}+03_{2.26 \mathrm{e}+03}$ |
| 30 | $\mathbf{3 . 6 0 e + 0 2 3 . 0 2 e + 0 1}$ | $1.35 \mathrm{e}+05_{5.42 \mathrm{e}+04}$ | $4.92 \mathrm{e}+02_{6.25 \mathrm{e}+01}$ | $5.47 \mathrm{e}+02_{2.57 \mathrm{e}+01}$ | $3.65 \mathrm{e}+02_{2.59 \mathrm{e}+01}$ | $8.02 \mathrm{e}+03_{3.57 \mathrm{e}+03}$ |
| Ranks | 1.9500 | 4.6333 | 2.9833 | 3.7167 | 2.1833 | 5.5333 |

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

| Algorithm | Year | Parameter settings |
| :-- | :-- | :-- |
| $\mathrm{E}_{3}$-EDA | - | $\mathrm{NP}=18 \cdot D,|\mathbf{A}|=3 \cdot \mathrm{NP},|\mathbf{L}|=0.1 \cdot \mathrm{NP}$ |
| LSHADE-EpSin | 2016 | $\mathrm{NP}_{\max }=18 \cdot D, \mathrm{NP}_{\min }=4, \mu F=\mu \mathrm{CR}=\mu$ freq $=\mathrm{freq}=0.5, H=5, G_{\mathrm{ls}}=250$ |
| UMOEAsII | 2016 | $\mathrm{NP}_{1, \max }=18 \cdot D, \mathrm{NP}_{1, \min }=4, \mathrm{NP}_{2}=4+(3 \log D), H=6, \mu=\mathrm{NP}_{2} / 2, \sigma=0.3, C S=50$ for $10 \cdot D$ and $30 \cdot D$ or |
| L-SHADE | 2014 | $\mathrm{NP}=18 \cdot D, \mathrm{NP}_{\min }=4, r^{\mathrm{arc}}=2, p=0.1, H=5$ |
| MLS-EDA | 2020 | $\mathrm{NP}=10 \cdot D, \operatorname{size}(\boldsymbol{S})_{\max }=3 \cdot D$ |
| ACSEDA | 2021 | $\mathrm{NP}=800$ for $10 \cdot D, \mathrm{NP}=1300$ for $30 \cdot D, \mathrm{NP}=1800$ for $50 \cdot D$ and $\mathrm{NP}=3200$ for $100 \cdot D, s_{\max }=0.35, s_{\min }=0.1$ |

The parameter settings of all participants follow their literatures as tabulated in Table 7.

The mean and SD values derived from the six algorithms are recorded in Tables 8, 9, 10 and 11. for the $10 \cdot D, 30 \cdot D$, $50 \cdot D$ and $100 \cdot D$ tests, respectively. For the first three unimodal functions, $\mathrm{E}_{3}$-EDA, MLS-EDA and ACSEDA show their robustness in finding the optimal values in all the $10 \cdot D$, $30 \cdot D$ and $50 \cdot D$ tests. For the multimodal functions, $\mathrm{E}_{3}$-EDA, LSHADE-EpSin and UMOEAsII are the top three methods in terms of accuracy. Specifically, in $30 \cdot D, \mathrm{E}_{3}$-EDA wins more than half of these 13 problems. The remaining L-SHADE, MLS-EDA and ACSEDA are less competitive, but all three methods can reach the optimal result on F7 regardless of the dimensionality. Additionally, for the hybrid functions F17-F22, our $\mathrm{E}_{3}$-EDA exhibits its superiority because it performs best on more than half of the benchmarks in four groups of tests except the $10 \cdot D$ test. The hybrid functions are partially separable problems that are close to real-world optimization problems. The domination of $\mathrm{E}_{3}$-EDA in solving this set of tasks verifies its potential in real world applications. As in solving the last eight composite functions, LSHADE-EpSin and UMOEAsII are the two competitive algorithms in all tests. MLS-EDA outperforms the other methods in the 30D test. Our $\mathrm{E}_{3}$-EDA has similar performance to L-SHADE and surpasses ACSEDA. From an overall view, according to the mean error data, our $\mathrm{E}_{3}$-EDA wins 13 out of 30 benchmarks in the 10D test, 17 in the $30 \cdot D$ test, 14 in the $50 \cdot D$ test and 6 in the $100 \cdot D$ test.

According to the mean error results, the performance of the six competitors on different types of test functions is statistically compared in Table 12. On this basis, $\mathrm{E}_{3}$-EDA has great advantages over other methods in solving hybrid problems and performs competitively in solving unimodal and multimodal functions. ACSEDA, UMOEAsII and LSHADEEpSin perform best in solving unimodal, multimodal, and composite tests, respectively.

To further demonstrate the superiority of our algorithm in a comprehensive manner, nonparametric tests are performed. Table 13 presents pairwise comparison results using the Wilcoxon signed-rank test for CEC 2014 10-D, 30-D,
$50 \cdot D$ and $100 \cdot D$ tests. The symbols " $\pm / \approx$ " indicate that our $\mathrm{E}_{3}$-EDA has superior, inferior, or similar performance in comparison with other methods based on the evaluated mean error values in Tables 8, 9, 10 and 11. In the following two columns, the symbol " $R+$ " denotes the magnitude with which $\mathrm{E}_{3}$-EDA can surpass the competitor, and " $R$-" expresses the opposite effect. The rightmost column records the $p$ value derived from the Wilcoxon signed-rank test. If the $p$ value is greater than the significance level $(\alpha=0.05)$, the comparison of the two algorithms is regarded to be statistically insignificant. Otherwise, $\mathrm{E}_{3}$-EDA is concluded to be better or worse based on the " $R+$ " magnitude. As seen in Table 14, E3-EDA has notable superiority compared with MLSEDA and ACSEDA in the $10 \cdot D$ test, outmatches L-SHADE and ACSEDA in the $30 \cdot D$ test, and surpasses L-SHADE and MLS-EDA in the $100 \cdot D$ test.

Moreover, the Friedman test is operated to perform a multiple comparison and rank these six algorithms according to their comprehensive performance. The ranking results for the three tests are presented in Table 14. $\mathrm{E}_{3}$-EDA ranks best among the six algorithms with values of 3.0167 in the 30D test, 3.1167 in the $50 \cdot D$ test and 2.8500 in the $100 \cdot D$ test, and ranks second with a score of 3.1000 in the $10 \cdot D$ test. The outperformance of $\mathrm{E}_{3}$-EDA is supported by the nonparametric studies in the CEC 2014 test, which demonstrates that our developed three search components are conducive to improving the algorithm performance.

In addition to the evidence provided by these optimization results, the execution time is another crucial issue to evaluate the algorithm's effectiveness. The average time consumptions in the same platform derived from all six participants on each benchmark in the CEC 2014 three tests are recorded in Appendix D. On this basis, Table 15 parallels the average time consumption of the six algorithms in different dimensional tests. According to these results, ACSEDA and L-SHADE are the two most efficient algorithms. Our $\mathrm{E}_{3}$-EDA has similar computational efficiency to MLS-EDA and is superior to UMOEAsII and LSHADE-EpSin. Although $\mathrm{E}_{3}$-EDA is not the most efficient algorithm; it has fewer gaps with ACSEDA

Table 8 Experimental results derived from six algorithms in the CEC 2014 10-D test

| No. | Type | $\mathrm{E}_{3}$-EDA | LSHADE-EpSin | UMOEAsII | L-SHADE | MLS-EDA | ACSEDA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ |
| 01 | Unimodal functions | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 02 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 03 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 04 | Multimodal functions | 2.82e+01 ${ }_{1.40 \mathrm{e}+01}$ | 3.48e+01 ${ }_{1.53 \mathrm{e}+01}$ | $\mathbf{2 . 7 1 e - 0 1}_{1.20 \mathrm{e}+00}$ | 2.83e+01 ${ }_{1.40 \mathrm{e}+01}$ | 2.47e+01 ${ }_{1.58 \mathrm{e}+01}$ | 3.48e+01 ${ }_{0.00 \mathrm{e}+00}$ |
| 05 |  | $\mathbf{1 . 3 3 e + 0 1 9 . 6 6 e + 0 0}$ | 1.64e+01 ${ }_{7.63 \mathrm{e}+00}$ | 1.75e+01 ${ }_{6.83 \mathrm{e}+00}$ | 1.43e+01 ${ }_{6.71 \mathrm{e}+00}$ | 2.01e+01 ${ }_{1.04 \mathrm{e}+00}$ | 1.38e+01 ${ }_{9.67 \mathrm{e}+00}$ |
| 06 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | 1.71e-06 ${ }_{1.32 \mathrm{e}-06}$ |
| 07 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | 1.05e-07 ${ }_{3.24 \mathrm{e}-07}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | 2.31e-03 ${ }_{4.26 \mathrm{e}-03}$ | 1.05e-01 ${ }_{1.19 \mathrm{e}-01}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 08 |  | 9.48e-02 ${ }_{2.99 \mathrm{e}-01}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | 2.16e+01 ${ }_{3.53 \mathrm{e}+00}$ | 3.21e-02 ${ }_{1.79 \mathrm{e}-01}$ |
| 09 |  | 2.84e-01 ${ }_{4.61 \mathrm{e}-01}$ | 1.74e+00 ${ }_{6.79 \mathrm{e}-01}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | 2.06e+00 ${ }_{8.44 \mathrm{e}-01}$ | 2.17e+01 ${ }_{3.71 \mathrm{e}+00}$ | 6.42e-02 ${ }_{3.57 \mathrm{e}-01}$ |
| 10 |  | 1.49e+01 ${ }_{5.88 \mathrm{e}+00}$ | 7.81e-03 ${ }_{2.13 \mathrm{e}-02}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | 1.56e-02 ${ }_{3.61 \mathrm{e}-02}$ | 1.06e+03 ${ }_{1.45 \mathrm{e}+02}$ | 1.09e+00 ${ }_{2.86 \mathrm{e}+00}$ |
| 11 |  | $\mathbf{1 . 3 9 e + 0 0}_{3.54 \mathrm{e}+00}$ | 2.53e+01 ${ }_{3.24 \mathrm{e}+01}$ | 3.35e+01 ${ }_{4.10 \mathrm{e}+01}$ | 2.20e+01 ${ }_{2.14 \mathrm{e}+01}$ | 9.60e+02 ${ }_{1.67 \mathrm{e}+02}$ | 2.22e+00 ${ }_{4.58 \mathrm{e}+00}$ |
| 12 |  | $\mathbf{7 . 2 0 e - 0 4}_{3.03 \mathrm{e}-03}$ | 7.07e-02 ${ }_{1.77 \mathrm{e}-02}$ | 3.22e-02 ${ }_{2.35 \mathrm{e}-02}$ | 6.33e-02 ${ }_{5.18 \mathrm{e}-02}$ | 1.15e+00 ${ }_{1.89 \mathrm{e}-01}$ | 1.19e+00 ${ }_{1.73 \mathrm{e}-01}$ |
| 13 |  | 5.22e-02 ${ }_{2.31 \mathrm{e}-02}$ | 4.46e-02 ${ }_{1.24 \mathrm{e}-02}$ | 3.72e-02 ${ }_{1.51 \mathrm{e}-02}$ | $\mathbf{2 . 2 5 e - 0 2}_{9.05 \mathrm{e}-03}$ | 1.02e-01 ${ }_{2.66 \mathrm{e}-02}$ | 4.27e-02 ${ }_{8.59 \mathrm{e}-03}$ |
| 14 |  | 3.57e-01 ${ }_{6.12 \mathrm{e}-02}$ | 7.97e-02 ${ }_{3.33 \mathrm{e}-02}$ | $\mathbf{7 . 0 8 e - 0 2}_{1.85 \mathrm{e}-02}$ | 7.51e-02 ${ }_{3.39 \mathrm{e}-02}$ | 1.22e-01 ${ }_{5.32 \mathrm{e}-02}$ | 2.45e-01 ${ }_{8.82 \mathrm{e}-02}$ |
| 15 |  | 3.51e-01 ${ }_{3.47 \mathrm{e}-01}$ | 3.47e-01 ${ }_{6.90 \mathrm{e}-02}$ | $\mathbf{2 . 6 8 e - 0 1}_{8.05 \mathrm{e}-02}$ | 5.18e-01 ${ }_{1.85 \mathrm{e}-01}$ | 1.65e+00 ${ }_{3.46 \mathrm{e}-01}$ | 4.71e-01 ${ }_{5.03 \mathrm{e}-01}$ |
| 16 |  | $\mathbf{3 . 4 6 e - 0 1}_{2.53 \mathrm{e}-01}$ | 1.02e+00 ${ }_{2.84 \mathrm{e}-01}$ | 9.10e-01 ${ }_{3.45 \mathrm{e}-01}$ | 6.62e-01 ${ }_{3.41 \mathrm{e}-01}$ | 1.71e+00 ${ }_{3.36 \mathrm{e}-01}$ | 1.36e+00 ${ }_{2.14 \mathrm{e}-01}$ |
| 17 | Hybrid function | 3.45e-01 ${ }_{2.41 \mathrm{e}-01}$ | 2.74e+01 ${ }_{4.03 \mathrm{e}+01}$ | 7.81e-01 ${ }_{1.14 \mathrm{e}+00}$ | 6.36e-01 ${ }_{6.31 \mathrm{e}-01}$ | 7.53e+00 ${ }_{8.63 \mathrm{e}+00}$ | $\mathbf{3 . 0 2 e - 0 1}_{1.68 \mathrm{e}-01}$ |
| 18 |  | $\mathbf{2 . 2 2 e - 0 1}_{1.96 \mathrm{e}-01}$ | 2.81e-01 ${ }_{3.58 \mathrm{e}-01}$ | 3.09e-01 ${ }_{2.86 \mathrm{e}-01}$ | 2.49e-01 ${ }_{3.62 \mathrm{e}-01}$ | 2.96e-01 ${ }_{3.28 \mathrm{e}-01}$ | 3.37e-01 ${ }_{1.82 \mathrm{e}-01}$ |
| 19 |  | $\mathbf{4 . 8 4 e - 0 2}_{2.49 \mathrm{e}-02}$ | 2.96e-01 ${ }_{4.24 \mathrm{e}-01}$ | 1.33e-01 ${ }_{1.72 \mathrm{e}-01}$ | 6.32e-02 ${ }_{3.07 \mathrm{e}-02}$ | 3.41e-01 ${ }_{2.74 \mathrm{e}-01}$ | 8.24e-01 ${ }_{4.55 \mathrm{e}-01}$ |
| 20 |  | 4.13e-01 ${ }_{1.93 \mathrm{e}-01}$ | 2.47e-01 ${ }_{2.14 \mathrm{e}-01}$ | $\mathbf{1 . 8 8 e - 0 1}_{1.36 \mathrm{e}-01}$ | 3.50e-01 ${ }_{2.10 \mathrm{e}-01}$ | 4.21e-01 ${ }_{2.58 \mathrm{e}-01}$ | 4.94e-01 ${ }_{1.16 \mathrm{e}-01}$ |
| 21 |  | 4.05e-01 ${ }_{3.26 \mathrm{e}-01}$ | 1.69e+00 ${ }_{4.17 \mathrm{e}+00}$ | $\mathbf{2 . 5 4 e - 0 1}_{2.59 \mathrm{e}-01}$ | 4.70e-01 ${ }_{2.83 \mathrm{e}-01}$ | 5.72e-01 ${ }_{5.72 \mathrm{e}-01}$ | 6.27e-01 ${ }_{2.54 \mathrm{e}-01}$ |
| 22 |  | 5.45e+00 ${ }_{8.85 \mathrm{e}+00}$ | 1.45e-01 ${ }_{1.27 \mathrm{e}-01}$ | 6.56e-02 ${ }_{3.06 \mathrm{e}-02}$ | $\mathbf{5 . 6 8 e - 0 2}_{4.25 \mathrm{e}-02}$ | 2.84e+01 ${ }_{2.49 \mathrm{e}+00}$ | 1.87e+01 ${ }_{5.27 \mathrm{e}+00}$ |
| 23 | Composition functions | 3.29e+02 ${ }_{0.00 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | 2.00e+02 ${ }_{0.00 \mathrm{e}+00}$ | 3.29e+02 ${ }_{0.00 \mathrm{e}+00}$ | 3.29e+02 ${ }_{0.00 \mathrm{e}+00}$ | 3.29e+02 ${ }_{0.00 \mathrm{e}+00}$ |
| 24 |  | $\mathbf{1 . 0 1 e + 0 2}_{1.62 \mathrm{e}+00}$ | 1.06e+02 ${ }_{3.30 \mathrm{e}+00}$ | 1.06e+02 ${ }_{2.53 \mathrm{e}+00}$ | 1.08e+02 ${ }_{1.38 \mathrm{e}+00}$ | 1.22e+02 ${ }_{2.36 \mathrm{e}+00}$ | 1.01e+02 ${ }_{2.36 \mathrm{e}+00}$ |
| 25 |  | 1.31e+02 ${ }_{3.39 \mathrm{e}+01}$ | 1.24e+02 ${ }_{2.92 \mathrm{e}+01}$ | $\mathbf{1 . 0 5 e + 0 2}_{5.64 \mathrm{e}+00}$ | 1.37e+02 ${ }_{4.52 \mathrm{e}+01}$ | 1.53e+02 ${ }_{6.34 \mathrm{e}+00}$ | 1.95e+02 ${ }_{6.34 \mathrm{e}+00}$ |
| 26 |  | $\mathbf{1 . 0 0 e + 0 2}_{1.73 \mathrm{e}-02}$ | $\mathbf{1 . 0 0 e + 0 2}_{1.10 \mathrm{e}-02}$ | $\mathbf{1 . 0 0 e + 0 2}_{1.05 \mathrm{e}-02}$ | $\mathbf{1 . 0 0 e + 0 2}_{7.93 \mathrm{e}-03}$ | $\mathbf{1 . 0 0 e + 0 2}_{7.80 \mathrm{e}-03}$ | $\mathbf{1 . 0 0 e + 0 2}_{7.80 \mathrm{e}-03}$ |
| 27 |  | 2.05e+02 ${ }_{2.01 \mathrm{e}+02}$ | 5.08e+01 ${ }_{8.90 \mathrm{e}+01}$ | 1.32e+00 ${ }_{2.84 \mathrm{e}-01}$ | $\mathbf{1 . 2 2 e + 0 0}_{3.08 \mathrm{e}-01}$ | 1.63e+02 ${ }_{4.17 \mathrm{e}+01}$ | 2.83e+02 ${ }_{4.17 \mathrm{e}+01}$ |
| 28 |  | 4.11e+02 ${ }_{6.21 \mathrm{e}+01}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | 2.00e+02 ${ }_{0.00 \mathrm{e}+00}$ | 3.80e+02 ${ }_{3.54 \mathrm{e}+01}$ | 4.19e+02 ${ }_{3.23 \mathrm{e}+01}$ | 3.82e+02 ${ }_{3.23 \mathrm{e}+01}$ |
| 29 |  | 2.19e+02 ${ }_{1.40 \mathrm{e}+01}$ | $\mathbf{2 . 0 0 e + 0 2}_{1.46 \mathrm{e}+00}$ | 2.22e+02 ${ }_{5.79 \mathrm{e}-01}$ | 2.22e+02 ${ }_{2.24 \mathrm{e}-01}$ | 2.16e+02 ${ }_{5.16 \mathrm{e}-01}$ | 2.22e+02 ${ }_{5.16 \mathrm{e}-01}$ |
| 30 |  | 4.70e+02 ${ }_{2.46 \mathrm{e}+01}$ | $\mathbf{3 . 2 4 e + 0 2}_{1.46 \mathrm{e}+02}$ | 4.65e+02 ${ }_{9.70 \mathrm{e}+00}$ | 4.63e+02 ${ }_{7.00 \mathrm{e}-01}$ | 4.83e+02 ${ }_{1.80 \mathrm{e}+01}$ | 4.71e+02 ${ }_{1.80 \mathrm{e}+01}$ |

The bold data indicates the optimal result
based on the recorded results in addressing low-dimensional problems.

## Comparison with HSES, LSHADE-RSP, ELSHADE-SPACMA, EBOwithCMAR and ACSEDA using the CEC 2018 test suite

To further verify the effectiveness of our proposal, another test using the CEC 2018 testbed is carried out. Five competitors are employed to make a comparison, including HSES, LSHADE-RSP, ELSHADE-SPACMA, EBOwithCMAR and ACSEDA. HSES, LSHADE-RSP, and ELSHADE-SPACMA are the top three methods of the CEC 2018 test. EBOwithCMAR is the champion of the CEC 2017 competition. ACSEDA represents a novel EDA variant. The parameters of each algorithm are assigned according to the original work, as shown in Table 16. LSHADE-RSP is coded using the C version. Its experimental data are taken from its original work. For the other five algorithms, all 29 benchmarks in CEC 2018 are evaluated 51 times with a fixed evaluation number of $D \times 10,000$. The statistical data, including the mean error and SD values, are presented in Tables 17, 18,19 and 20.

The first two unimodal functions are easily addressed because all participants can access the acceptable error values in all tests. In addition, for the following seven multimodal functions, $\mathrm{E}_{3}$-EDA, EBOwithCMAR and ACSEDA are the top three algorithms in solving $10-D$ problems. Moreover,

Table 9 Experimental results derived from six algorithms in the CEC 2014 30-D test

| No. | Type | $\mathrm{E}_{3}$-EDA | LSHADE-EpSin | UMOEAsII | L-SHADE | MLS-EDA | ACSEDA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ |
| 01 | Unimodal functions | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 02 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 03 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 04 | Multimodal functions | $7.61 \mathrm{e}+00_{1.33 \mathrm{e}+01}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $5.09 \mathrm{e}+00_{5.11 \mathrm{e}+00}$ |
| 05 |  | $\mathbf{2 . 0 0 e + 0 1}_{1.90 \mathrm{e}-01}$ | $2.01 \mathrm{e}+01_{2.19 \mathrm{e}-02}$ | $\mathbf{2 . 0 0 e + 0 1}_{1.878 \mathrm{e}-03}$ | $2.01 \mathrm{e}+01_{5.86 \mathrm{e}-02}$ | $\mathbf{2 . 0 0 e + 0 1}_{2.69 \mathrm{e}-02}$ | $2.09 \mathrm{e}+01_{6.42 \mathrm{e}-02}$ |
| 06 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $3.23 \mathrm{e}-02_{2.21 \mathrm{e}-01}$ | $6.89 \mathrm{e}-08_{4.92 \mathrm{e}-07}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 07 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 08 |  | $1.07 \mathrm{e}+00_{9.92 \mathrm{e}-01}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $2.80 \mathrm{e}+01_{6.28 \mathrm{e}+00}$ | $2.97 \mathrm{e}+00_{1.82 \mathrm{e}+00}$ |
| 09 |  | $\mathbf{5 . 8 5 e - 0 1}_{7.22 \mathrm{e}-01}$ | $1.34 \mathrm{e}+01_{1.98 \mathrm{e}+00}$ | $9.32 \mathrm{e}-01_{8.01 \mathrm{e}-01}$ | $8.78 \mathrm{e}+00_{5.88 \mathrm{e}+00}$ | $2.34 \mathrm{e}+01_{8.23 \mathrm{e}+00}$ | $2.71 \mathrm{e}+00_{1.56 \mathrm{e}+00}$ |
| 10 |  | $8.11 \mathrm{e}+01_{1.54 \mathrm{e}+02}$ | $3.27 \mathrm{e}-03_{8.71 \mathrm{e}-03}$ | $\mathbf{2 . 4 5 e - 0 3}_{6.77 \mathrm{e}-03}$ | $4.08 \mathrm{e}-03_{9.39 \mathrm{e}-03}$ | $2.09 \mathrm{e}+03_{6.08 \mathrm{e}+02}$ | $3.43 \mathrm{e}+01_{7.46 \mathrm{e}+01}$ |
| 11 |  | $\mathbf{5 . 2 3 e + 0 1}_{7.19 \mathrm{e}+01}$ | $1.17 \mathrm{e}+03_{1.67 \mathrm{e}+02}$ | $1.30 \mathrm{e}+03_{2.46 \mathrm{e}-02}$ | $1.13 \mathrm{e}+03_{4.87 \mathrm{e}+02}$ | $2.38 \mathrm{e}+03_{7.34 \mathrm{e}+02}$ | $1.30 \mathrm{e}+02_{1 / 14 \mathrm{e}+02}$ |
| 12 |  | $\mathbf{5 . 7 5 e - 0 3}_{5.03 \mathrm{e}-03}$ | $1.61 \mathrm{e}-01_{2.28 \mathrm{e}-02}$ | $8.79 \mathrm{e}-02_{4.66 \mathrm{e}-02}$ | $9.61 \mathrm{e}-02_{4.24 \mathrm{e}-02}$ | $2.07 \mathrm{e}-02_{5.74 \mathrm{e}-02}$ | $2.45 \mathrm{e}+00_{2.92 \mathrm{e}-01}$ |
| 13 |  | $2.32 \mathrm{e}-01_{3.63 \mathrm{e}-02}$ | $1.37 \mathrm{e}-01_{2.03 \mathrm{e}-02}$ | $1.05 \mathrm{e}-01_{2.93 \mathrm{e}-02}$ | $4.77 \mathrm{e}-02_{1.08 \mathrm{e}-02}$ | $2.09 \mathrm{e}-01_{3.79 \mathrm{e}-02}$ | $\mathbf{8 . 9 0 e - 0 2}_{2.01 \mathrm{e}-02}$ |
| 14 |  | $3.51 \mathrm{e}-01_{3.82 \mathrm{e}-02}$ | $\mathbf{1 . 9 5 e - 0 1}_{2.73 \mathrm{e}-02}$ | $2.34 \mathrm{e}-01_{2.78 \mathrm{e}-02}$ | $2.82 \mathrm{e}-01_{3.01 \mathrm{e}-02}$ | $2.05 \mathrm{e}-01_{4.13 \mathrm{e}-02}$ | $3.03 \mathrm{e}-01_{5.10 \mathrm{e}-02}$ |
| 15 |  | $2.39 \mathrm{e}+00_{4.33 \mathrm{e}-01}$ | $2.31 \mathrm{e}+00_{2.23 \mathrm{e}-01}$ | $\mathbf{1 . 9 2 e + 0 0}_{3.85 \mathrm{e}-0}$ | $2.80 \mathrm{e}+00_{6.18 \mathrm{e}-01}$ | $3.05 \mathrm{e}+00_{6.12 \mathrm{e}-01}$ | $2.67 \mathrm{e}+00_{4.02 \mathrm{e}-01}$ |
| 16 |  | $\mathbf{6 . 5 0 e + 0 0}_{8.77 \mathrm{e}-01}$ | $8.22 \mathrm{e}+00_{4.57 \mathrm{e}-01}$ | $9.03 \mathrm{e}+00_{6.11 \mathrm{e}-01}$ | $7.50 \mathrm{e}+00_{9.43 \mathrm{e}-01}$ | $9.56 \mathrm{e}+00_{6.45 \mathrm{e}-01}$ | $8.88 \mathrm{e}+00_{4.72 \mathrm{e}-01}$ |
| 17 | Hybrid function | $\mathbf{6 . 1 3 e - 0 1}_{5.07 \mathrm{e}-01}$ | $1.50 \mathrm{e}+02_{6.59 \mathrm{e}+01}$ | $1.35 \mathrm{e}+02_{6.91 \mathrm{e}+01}$ | $2.11 \mathrm{e}+02_{1.11 \mathrm{e}+02}$ | $2.39 \mathrm{e}+01_{1.93 \mathrm{e}+01}$ | $7.54 \mathrm{e}+01_{5.60 \mathrm{e}+01}$ |
| 18 |  | $\mathbf{5 . 3 9 e - 0 1}_{2.95 \mathrm{e}-01}$ | $5.00 \mathrm{e}+00_{2.09 \mathrm{e}+00}$ | $6.11 \mathrm{e}+00_{2.91 \mathrm{e}+00}$ | $5.96 \mathrm{e}+00_{2.48 \mathrm{e}+00}$ | $5.37 \mathrm{e}+00_{2.37 \mathrm{e}+00}$ | $5.24 \mathrm{e}+00_{3.56 \mathrm{e}+00}$ |
| 19 |  | $\mathbf{6 . 3 8 e - 0 1}_{4.69 \mathrm{e}-01}$ | $2.64 \mathrm{e}+00_{6.13 \mathrm{e}-01}$ | $3.03 \mathrm{e}+00_{7.93 \mathrm{e}-01}$ | $2.72 \mathrm{e}+00_{6.33 \mathrm{e}-01}$ | $1.38 \mathrm{e}+00_{8.71 \mathrm{e}-01}$ | $2.87 \mathrm{e}+00_{7.45 \mathrm{e}-01}$ |
| 20 |  | $\mathbf{1 . 2 1 e + 0 0}_{1.81 \mathrm{e}-01}$ | $2.18 \mathrm{e}+00_{1.09 \mathrm{e}+00}$ | $3.74 \mathrm{e}+00_{1.47 \mathrm{e}+00}$ | $3.18 \mathrm{e}+00_{1.37 \mathrm{e}+00}$ | $3.80 \mathrm{e}+00_{1.67 \mathrm{e}+00}$ | $1.49 \mathrm{e}+00_{4.53 \mathrm{e}-01}$ |
| 21 |  | $\mathbf{9 . 0 0 e - 0 1}_{1.62 \mathrm{e}-01}$ | $9.92 \mathrm{e}+01_{7.28 \mathrm{e}+01}$ | $7.62 \mathrm{e}+01_{6.97 \mathrm{e}+01}$ | $8.22 \mathrm{e}+01_{7.51 \mathrm{e}+01}$ | $1.04 \mathrm{e}+01_{2.04 \mathrm{e}+01}$ | $4.45 \mathrm{e}+01_{6.09 \mathrm{e}+01}$ |
| 22 |  | $\mathbf{2 . 3 1 e + 0 1}_{8.59 \mathrm{e}+00}$ | $5.42 \mathrm{e}+01_{5.23 \mathrm{e}+0}$ | $3.19 \mathrm{e}+01_{2.44 \mathrm{e}+01}$ | $2.85 \mathrm{e}+01_{2.09 \mathrm{e}+01}$ | $8.21 \mathrm{e}+01_{6.22 \mathrm{e}+01}$ | $7.08 \mathrm{e}+01_{5.97 \mathrm{e}+01}$ |
| 23 | Composition functions | $3.15 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $3.15 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $3.15 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ |
| 24 |  | $2.11 \mathrm{e}+02_{9.61 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2}_{1.66 \mathrm{e}-07}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $2.24 \mathrm{e}+02_{1.19 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2}_{3.81 \mathrm{e}+00}$ | $2.13 \mathrm{e}+02_{1.06 \mathrm{e}+01}$ |
| 25 |  | $2.03 \mathrm{e}+02_{4.06 \mathrm{e}-02}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $2.03 \mathrm{e}+02_{4.61 \mathrm{e}-02}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $2.03 \mathrm{e}+02_{2.52 \mathrm{e}-02}$ |
| 26 |  | $\mathbf{1 . 0 0 e + 0 2}_{4.16 \mathrm{e}-02}$ | $\mathbf{1 . 0 0 e + 0 2}_{1.86 \mathrm{e}-02}$ | $\mathbf{1 . 0 0 e + 0 2}_{2.50 \mathrm{e}-02}$ | $\mathbf{1 . 0 0 e + 0 2}_{1.21 \mathrm{e}-02}$ | $\mathbf{1 . 0 0 e + 0 2}_{1.89 \mathrm{e}-02}$ | $\mathbf{1 . 0 0 e + 0 2}_{1.57 \mathrm{e}-02}$ |
| 27 |  | $3.14 \mathrm{e}+02_{3.48 \mathrm{e}+01}$ | $2.08 \mathrm{e}+02_{2.72 \mathrm{e}+01}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $3.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $3.01 \mathrm{e}+02_{8.88 \mathrm{e}+00}$ |
| 28 |  | $7.27 \mathrm{e}+02_{1.30 \mathrm{e}+02}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $2.11 \mathrm{e}+02_{8.13 \mathrm{e}+01}$ | $8.42 \mathrm{e}+02_{1.46 \mathrm{e}+01}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.79 \mathrm{e}+00}$ | $8.42 \mathrm{e}+02_{2.07 \mathrm{e}+01}$ |
| 29 |  | $1.93 \mathrm{e}+02_{1.57 \mathrm{e}+02}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $7.17 \mathrm{e}+02_{3.81 \mathrm{e}+00}$ | $7.16 \mathrm{e}+02_{1.00 \mathrm{e}+00}$ | $\mathbf{1 . 1 8 e + 0 2}_{1.34 \mathrm{e}+01}$ | $7.35 \mathrm{e}+02_{2.80 \mathrm{e}+01}$ |
| 30 |  | $3.65 \mathrm{e}+02_{3.80 \mathrm{e}+01}$ | $\mathbf{2 . 0 0 e + 0 2}_{0.00 \mathrm{e}+00}$ | $9.03 \mathrm{e}+02_{2.73 \mathrm{e}+02}$ | $1.15 \mathrm{e}+03_{5.58 \mathrm{e}+02}$ | $3.65 \mathrm{e}+02_{2.84 \mathrm{e}+01}$ | $1.91 \mathrm{e}+03_{7.80 \mathrm{e}+02}$ |

The bold data indicates the optimal result
$\mathrm{E}_{3}$-EDA wins all benchmarks except F4 in the $30-D$ test and ranks first on F7, F9 and F10 in the $50-D$ trial. HSES obtains the best results on F4 in all four groups of tests. Furthermore, all six algorithms perform robustly on F6 and F9. For the hybrid functions in the 10D test, EBOwithCMAR obtains better results than the other algorithms, while $\mathrm{E}_{3}$-EDA performs best on F14. For the $30-D$ test, ACSEDA obtains the best result only on F16. The best values of the remaining 9 functions are accessed by our $\mathrm{E}_{3}$-EDA. The advantage of our $\mathrm{E}_{3}$-EDA is the highest in each row. In the $50-D$ test, $\mathrm{E}_{3}$-EDA is the best performing algorithm with the best values on F11, F12, F13, F16, F18 and F19. HSES ranks at the top on F14 and F15, while ACSEDA ranks first on F17 and F20. In the $100-D$ test, $\mathrm{E}_{3}$-EDA is also proven to be the best problem
solver by winning on F12, F13, F15, F16 and F19. For the last group of 10 composite functions, $\mathrm{E}_{3}$-EDA wins on more than half of the functions except in the 10D test.

In general, EBOwithCMAR is the top algorithm in the $10-D$ test, while our $\mathrm{E}_{3}$-EDA has prominent advantages over the other five algorithms in the remaining three tests. Specifically, $\mathrm{E}_{3}$-EDA obtains the best results for almost all 29 benchmarks in the $30-D$ test except F4, F16, F21, F28, F29 and F30. In the $50-D$ test, $\mathrm{E}_{3}$-EDA ranks first on 17 out of 29 benchmarks. Moreover, $\mathrm{E}_{3}$-EDA obtains as many as 13 results better than other algorithms in the $100-D$ test.

To compare the performance of different algorithms more clearly in solving different types of problems, Table 21 compares the ranking results of the six algorithms. $\mathrm{E}_{3}$-EDA

Table 10 Experimental results derived from six algorithms in the CEC 2014 50-D test

| No | Type | $\mathrm{E}_{3}$-EDA | LSHADe-EpSin | UMOEAsII | L-SHADE | MLS-EDA | ACSEDA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ |
| 01 | Unimodal functions | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\begin{aligned} & 2.95 \mathrm{e}-03_{1.65 \mathrm{e}-02} \\ & 0.00 \mathrm{e}+\mathbf{0 0}_{\mathbf{0 . 0 0 e + 0 0}} \end{aligned}$ | $\begin{aligned} & 1.53 \mathrm{e}-03_{0.00 \mathrm{e}+00} \\ & 0.00 \mathrm{e}+\mathbf{0 0}_{\mathbf{0 . 0 0 e + 0 0}} \end{aligned}$ | $\begin{aligned} & 1.32 \mathrm{e}+03_{1.68 \mathrm{e}+03} \\ & 0.00 \mathrm{e}+\mathbf{0 0}_{\mathbf{0 . 0 0 e + 0 0}} \end{aligned}$ | $\begin{aligned} & \mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}} \\ & 0.00 \mathrm{e}+\mathbf{0 0}_{\mathbf{0 . 0 0 e + 0 0}} \end{aligned}$ | $\begin{aligned} & \mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}} \\ & 0.00 \mathrm{e}+\mathbf{0 0}_{\mathbf{0 . 0 0 e + 0 0}} \end{aligned}$ | $\begin{aligned} & \mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}} \\ & 0.00 \mathrm{e}+\mathbf{0 0}_{\mathbf{0 . 0 0 e + 0 0}} \end{aligned}$ |
| 02 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 03 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 04 | Multimodal functions | $7.42 \mathrm{e}+01_{1.74 \mathrm{e}+01}$ | $4.35 \mathrm{e}+01_{4.81 \mathrm{e}+01}$ | $\mathbf{3 . 2 7 e + 0 1 _ { 4 . 6 7 e + 0 1 }}$ | $4.29 \mathrm{e}+01_{4.56 \mathrm{e}+01}$ | $\mathbf{5 . 5 9 e - 0 1 _ { 4 . 6 0 e - 0 1 }}$ | $9.02 \mathrm{e}+01_{8.48 \mathrm{e}+00}$ |
| 05 |  | $\mathbf{2 . 0 0 e + 0 1 _ { 1 . 6 8 e - 0 1 }}$ | $2.03 \mathrm{e}+01_{3.16 \mathrm{e}-02}$ | $\mathbf{2 . 0 0 e + 0 1 _ { 1 . 8 5 e - 0 4 }}$ | $2.02 \mathrm{e}+01_{6.40 \mathrm{e}-02}$ | $\mathbf{2 . 0 0 e + 0 1 _ { 4 . 4 2 e - 0 2 }}$ | $2.11 \mathrm{e}+01_{3.72 \mathrm{e}-02}$ |
| 06 |  | $4.40 \mathrm{e}-047.86 \mathrm{e}-05$ | $3.07 \mathrm{e}-02_{1.23 \mathrm{e}-01}$ | $2.52 \mathrm{e}-01_{5.44 \mathrm{e}-01}$ | $2.39 \mathrm{e}-01_{5.44 \mathrm{e}-01}$ | $\mathbf{3 . 7 6 e - 0 5 _ { 6 . 2 7 e - 0 5 }}$ | $5.23 \mathrm{e}-05_{1.47 \mathrm{e}-05}$ |
| 07 |  | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ |
| 08 |  | $3.36 \mathrm{e}+00_{1.91 \mathrm{e}+00}$ | $\mathbf{0 . 0 0 e + 0 0}_{1.22 \mathrm{e}-08}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $\mathbf{0 . 0 0 e + 0 0}_{\mathbf{0 . 0 0 e + 0 0}}$ | $3.71 \mathrm{e}+01_{1.34 \mathrm{e}+01}$ | $2.70 \mathrm{e}+00_{1.63 \mathrm{e}+00}$ |
| 09 |  | $2.19 \mathrm{e}+00_{1.24 \mathrm{e}+00}$ | $2.99 \mathrm{e}+01_{5.03 \mathrm{e}+00}$ | $4.34 \mathrm{e}+00_{1.67 \mathrm{e}+00}$ | $1.11 \mathrm{e}+01_{4.31 \mathrm{e}+00}$ | $3.63 \mathrm{e}+01_{1.48 \mathrm{e}+01}$ | $\mathbf{2 . 1 5 e + 0 0}_{1.31 \mathrm{e}+00}$ |
| 10 |  | $5.53 \mathrm{e}+02_{1.30 \mathrm{e}+03}$ | $5.28 \mathrm{e}-02_{2.65 \mathrm{e}-02}$ | $4.28 \mathrm{e}-01_{4.64 \mathrm{e}-01}$ | $\mathbf{4 . 8 5 e - 0 2 _ { 2 . 6 5 e - 0 2 }}$ | $5.05 \mathrm{e}+03_{9.03 \mathrm{e}+02}$ | $9.62 \mathrm{e}+01_{1.20 \mathrm{e}+02}$ |
| 11 |  | $2.04 \mathrm{e}+02_{1.45 \mathrm{e}+02}$ | $3.06 \mathrm{e}+03_{3.01 \mathrm{e}+02}$ | $3.46 \mathrm{e}+03_{5.47 \mathrm{e}+02}$ | $3.87 \mathrm{e}+03_{1.03 \mathrm{e}+03}$ | $4.38 \mathrm{e}+03_{1.11 \mathrm{e}+03}$ | $\mathbf{1 . 0 9 e + 0 2 _ { 1 . 1 8 e + 0 2 }}$ |
| 12 |  | $\mathbf{1 . 3 5 e - 0 2 _ { 1 . 6 0 e - 0 2 }}$ | $2.06 \mathrm{e}-01_{2.53 \mathrm{e}-02}$ | $1.05 \mathrm{e}-01_{5.80 \mathrm{e}-02}$ | $1.13 \mathrm{e}-01_{4.33 \mathrm{e}-02}$ | $2.36 \mathrm{e}-02_{2.82 \mathrm{e}-02}$ | $3.25 \mathrm{e}+00_{2.73 \mathrm{e}-01}$ |
| 13 |  | $3.61 \mathrm{e}-01_{4.04 \mathrm{e}-02}$ | $2.02 \mathrm{e}-01_{2.04 \mathrm{e}-02}$ | $1.43 \mathrm{e}-01_{3.73 \mathrm{e}-02}$ | $\mathbf{7 . 3 0 e - 0 2 _ { 1 . 2 2 e - 0 2 }}$ | $3.42 \mathrm{e}-01_{2.60 \mathrm{e}-02}$ | $1.55 \mathrm{e}-01_{1.85 \mathrm{e}-02}$ |
| 14 |  | $3.56 \mathrm{e}-01_{4.16 \mathrm{e}-02}$ | $\mathbf{1 . 9 1 e - 0 1 _ { 2 . 0 7 e - 0 2 }}$ | $3.05 \mathrm{e}-01_{2.12 \mathrm{e}-02}$ | $3.59 \mathrm{e}-01_{2.38 \mathrm{e}-02}$ | $2.51 \mathrm{e}-01_{1.65 \mathrm{e}-02}$ | $2.72 \mathrm{e}-01_{5.43 \mathrm{e}-02}$ |
| 15 |  | $\mathbf{4 . 4 5 e + 0 0 _ { 5 . 0 3 e - 0 1 }}$ | $5.48 \mathrm{e}+00_{5.19 \mathrm{e}-01}$ | $5.39 \mathrm{e}+00_{8.60 \mathrm{e}-01}$ | $5.49 \mathrm{e}+00_{8.93 \mathrm{e}-01}$ | $4.77 \mathrm{e}+00_{1.19 \mathrm{e}+00}$ | $4.83 \mathrm{e}+00_{1.48 \mathrm{e}+00}$ |
| 16 |  | $\mathbf{1 . 3 3 e + 0 1 _ { 1 . 1 2 e + 0 0 }}$ | $1.66 \mathrm{e}+01_{4.44 \mathrm{e}-01}$ | $1.82 \mathrm{e}+01_{8.67 \mathrm{e}-01}$ | $1.52 \mathrm{e}+01_{1.39 \mathrm{e}+00}$ | $1.94 \mathrm{e}+01_{8.06 \mathrm{e}-01}$ | $1.79 \mathrm{e}+01_{4.62 \mathrm{e}-01}$ |
| 17 | Hybrid function | $\mathbf{4 . 5 5 e + 0 0 _ { 1 . 0 8 e + 0 0 }}$ | $3.81 \mathrm{e}+02_{2.08 \mathrm{e}+02}$ | $1.11 \mathrm{e}+03_{2.98 \mathrm{e}+02}$ | $1.42 \mathrm{e}+03_{3.70 \mathrm{e}+02}$ | $2.50 \mathrm{e}+02_{1.70 \mathrm{e}+02}$ | $1.20 \mathrm{e}+02_{1.02 \mathrm{e}+02}$ |
| 18 |  | $\mathbf{5 . 4 8 e - 0 1 _ { 1 . 4 5 e - 0 1 }}$ | $1.87 \mathrm{e}+01_{6.40 \mathrm{e}+00}$ | $7.45 \mathrm{e}+01_{2.01 \mathrm{e}+01}$ | $9.47 \mathrm{e}+01_{1.37 \mathrm{e}+01}$ | $6.08 \mathrm{e}+00_{2.42 \mathrm{e}+00}$ | $7.90 \mathrm{e}+00_{4.05 \mathrm{e}+00}$ |
| 19 |  | $\mathbf{6 . 2 6 e + 0 0 _ { 1 . 3 6 e + 0 0 }}$ | $9.97 \mathrm{e}+00_{1.12 \mathrm{e}+00}$ | $9.32 \mathrm{e}+00_{1.95 \mathrm{e}+00}$ | $6.30 \mathrm{e}+00_{5.66 \mathrm{e}-01}$ | $8.17 \mathrm{e}+00_{9.59 \mathrm{e}-01}$ | $1.13 \mathrm{e}+01_{8.76 \mathrm{e}-01}$ |
| 20 |  | $\mathbf{1 . 8 6 e + 0 0 _ { 3 . 2 7 e - 0 1 }}$ | $6.10 \mathrm{e}+00_{1.80 \mathrm{e}+00}$ | $1.54 \mathrm{e}+01_{5.74 \mathrm{e}+00}$ | $1.25 \mathrm{e}+01_{3.79 \mathrm{e}+00}$ | $7.92 \mathrm{e}+00_{2.16 \mathrm{e}+00}$ | $1.90 \mathrm{e}+00_{5.19 \mathrm{e}-01}$ |
| 21 |  | $\mathbf{6 . 0 4 e + 0 0 _ { 2 . 3 7 e + 0 1 }}$ | $3.04 \mathrm{e}+02_{1.30 \mathrm{e}+02}$ | $\mathbf{4 . 7 1 e + 0 2 _ { 1 . 3 9 e + 0 2 }}$ | $\mathbf{5 . 1 1 e + 0 2 _ { 1 . 3 2 e + 0 2 }}$ | $\mathbf{2 . 7 6 e + 0 2 _ { 1 . 4 3 e + 0 2 }}$ | $1.80 \mathrm{e}+02_{8.36 \mathrm{e}+01}$ |
| 22 |  | $8.04 \mathrm{e}+01_{1.48 \mathrm{e}+02}$ | $1.08 \mathrm{e}+02_{6.20 \mathrm{e}+01}$ | $1.61 \mathrm{e}+02_{1.07 \mathrm{e}+02}$ | $4.25 \mathrm{e}+01_{3.98 \mathrm{e}+01}$ | $2.03 \mathrm{e}+02_{8.58 \mathrm{e}+01}$ | $\mathbf{3 . 5 3 e + 0 1 _ { 3 . 0 7 e + 0 1 }}$ |
| 23 | Composition functions | $3.44 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2 _ { 0 . 0 0 e + 0 0 }}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $3.44 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2 _ { 0 . 0 0 e + 0 0 }}$ | $3.44 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ |
| 24 |  | $2.67 \mathrm{e}+02_{1.81 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2 _ { 2 . 9 8 e - 0 0 }}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.75 \mathrm{e}+02_{8.88 \mathrm{e}-01}$ | $\mathbf{2 . 0 0 e + 0 2 { } _ { 0 . 0 0 e + 0 0 }}$ | $2.68 \mathrm{e}+02_{1.55 \mathrm{e}+00}$ |
| 25 |  | $2.05 \mathrm{e}+02_{0.02 \mathrm{e}-02}$ | $\mathbf{2 . 0 0 e + 0 2 _ { 0 . 0 6 e + 0 0 }}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.05 \mathrm{e}+02_{3.29 \mathrm{e}-01}$ | $2.05 \mathrm{e}+02_{1.09 \mathrm{e}-01}$ | $2.05 \mathrm{e}+02_{0.49 \mathrm{e}-02}$ |
| 26 |  | $\mathbf{1 . 0 0 e + 0 2 _ { 4 . 3 9 e - 0 2 }}$ | $\mathbf{1 . 0 0 e + 0 2 { 3 . 8 3 e - 0 2 }}$ | $\mathbf{1 . 0 0 e + 0 2 { 2 . 3 6 e - 0 2 }}$ | $\mathbf{1 . 0 0 e + 0 2 { 2 . 5 5 e - 0 2 }}$ | $\mathbf{1 . 0 0 e + 0 2 { 2 . 5 5 e - 0 2 }}$ | $1.00 \mathrm{e}+02_{5.28 \mathrm{e}-02}$ |
| 27 |  | $3.02 \mathrm{e}+02_{9.89 \mathrm{e}+00}$ | $2.04 \mathrm{e}+02_{1.96 \mathrm{e}+01}$ | $\mathbf{2 . 0 0 e + 0 2 _{ 0 . 0 0 e + 0 0 }}$ | $3.41 \mathrm{e}+02_{3.50 \mathrm{e}+01}$ | $3.00 \mathrm{e}+02_{4.19 \mathrm{e}-02}$ | $2.96 \mathrm{e}+02_{2.92 \mathrm{e}+00}$ |
| 28 |  | $1.04 \mathrm{e}+03_{9.5 \mathrm{e}+01}$ | $\mathbf{2 . 0 0 e + 0 2 { 0 . 0 0 e + 0 0 }}$ | $\mathbf{2 . 0 0 e + 0 2 _{ 0 . 0 0 e + 0 0 }}$ | $1.11 \mathrm{e}+03_{2.66 \mathrm{e}+01}$ | $8.93 \mathrm{e}+02_{3.39 \mathrm{e}+02}$ | $1.15 \mathrm{e}+03_{5.80 \mathrm{e}+01}$ |
| 29 |  | $3.51 \mathrm{e}+02_{8.62 \mathrm{e}+00}$ | $\mathbf{2 . 0 0 e + 0 2 { 0 . 0 0 e + 0 0 }}$ | $8.02 \mathrm{e}+02_{3.73 \mathrm{e}+01}$ | $8.13 \mathrm{e}+02_{4.48 \mathrm{e}+01}$ | $3.39 \mathrm{e}+02_{6.00 \mathrm{e}+00}$ | $8.39 \mathrm{e}+02_{4.75 \mathrm{e}+01}$ |
| 30 |  | $1.14 \mathrm{e}+04_{3.78 \mathrm{e}+02}$ | $\mathbf{2 . 0 0 e + 0 2 { 0 . 0 0 e + 0 0 }}$ | $8.66 \mathrm{e}+03_{4.62 \mathrm{e}+02}$ | $8.60 \mathrm{e}+03_{3.74 \mathrm{e}+02}$ | $8.61 \mathrm{e}+03_{2.73 \mathrm{e}+02}$ | $8.68 \mathrm{e}+03_{4.68 \mathrm{e}+02}$ |

The bold data indicates the optimal result
possesses the best performance in solving multimodal, hybrid and composite problems. HSES has robust performance in gaining the best results on unimodal functions.

Similarly, the Wilcoxon signed-rank test is performed to conduct a pairwise comparison between $\mathrm{E}_{3}$-EDA and each competitor. The symbols in Table 22 have the same meaning as explained in the previous section. According to the $p$ value recorded in the right column of Table 22, for the $10-D$ test, $\mathrm{E}_{3}$-EDA obtains similar performance to LSHADE-RSP, ELSHADE-SPACMA, and EBOwithCMAR but has substantial dominance to HSES and ACSEDA. For the remaining three tests, $\mathrm{E}_{3}$-EDA surpasses every competitor except HSES and ACSEDA in the $100-D$ test.

Moreover, the Friedman test is carried out to distinguish the differences among the six algorithms. Table 23 provides the rankings of each participant in the four CEC 2018 tests. $\mathrm{E}_{3}$-EDA ranks at the top with the smallest ranking values of 1.9483 in the $30-D$ test, 2.0690 in the $50-D$ test and 2.500 in the $100-D$ test. For the $10-D$ test, LSHADE-RSP performs best, and $\mathrm{E}_{3}$-EDA ranks third, following EBOwithCMAR. From an overall viewpoint of the ranking results of different dimension tests, $\mathrm{E}_{3}$-EDA possesses more competitive performance than other algorithms.

The execution times of all competitors except LSHADERSP are compared in Appendix E, which shows the average time required by these five competitors to optimize each function. Table 24 compares the average amounts of time required

Table 11 Experimental results derived from six algorithms in the CEC 2014 100-D test

| No. | Type | $\mathrm{E}_{3}$-EDA | LSHADE-EpSin | UMOEAsII | L-SHADE | MLS-EDA | ACSEDA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ | Mean error $_{\text {SD }}$ |
| 01 | Unimodal functions | $1.54 \mathrm{e}-04_{2.59 \mathrm{e}-05}$ | $1.62 \mathrm{e}+04_{8.27 \mathrm{e}+03}$ | $4.11 \mathrm{e}-03_{7.72 \mathrm{e}-04}$ | $1.75 \mathrm{e}+05_{4.37 \mathrm{e}+04}$ | $3.20 \mathrm{e}+02_{3.19 \mathrm{e}-02}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ |
| 02 |  | $1.63 \mathrm{e}-02_{2.08 \mathrm{e}-03}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $2.77 \mathrm{e}-03_{1.29 \mathrm{e}-01}$ | $6.63 \mathrm{e}-07_{6.80 \mathrm{e}-07}$ |
| 03 |  | $2.53 \mathrm{e}-08_{2.97 \mathrm{e}-09}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $1.09 \mathrm{e}-06_{1.78 \mathrm{e}-07}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ |
| 04 | Multimodal functions | $1.55 \mathrm{e}+02_{2.16 \mathrm{e}+01}$ | $1.66 \mathrm{e}+02_{3.22 \mathrm{e}+01}$ | $1.67 \mathrm{e}+02_{3.14 \mathrm{e}+01}$ | $1.65 \mathrm{e}+02_{3.04 \mathrm{e}+01}$ | $1.52 \mathrm{e}+02_{3.97 \mathrm{e}-02}$ | $1.80 \mathrm{e}+02_{3.22 \mathrm{e}+01}$ |
| 05 |  | $2.02 \mathrm{e}+01_{3.51 \mathrm{e}-01}$ | $2.06 \mathrm{e}+01_{2.35 \mathrm{e}-02}$ | $2.00 \mathrm{e}+01_{1.23 \mathrm{e}-04}$ | $2.04 \mathrm{e}+01_{1.61 \mathrm{e}-01}$ | $2.00 \mathrm{e}+01_{1.86 \mathrm{e}-04}$ | $2.13 \mathrm{e}+01_{1.80 \mathrm{e}-02}$ |
| 06 |  | $4.32 \mathrm{e}-01_{3.31 \mathrm{e}-01}$ | $2.70 \mathrm{e}-01_{4.57 \mathrm{e}-01}$ | $8.36 \mathrm{e}+00_{1.80 \mathrm{e}+00}$ | $9.66 \mathrm{e}+00_{2.14 \mathrm{e}+00}$ | $6.69 \mathrm{e}+00_{1.57 \mathrm{e}+00}$ | $6.34 \mathrm{e}-01_{6.86 \mathrm{e}-01}$ |
| 07 |  | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ |
| 08 |  | $2.21 \mathrm{e}+01_{3.17 \mathrm{e}+00}$ | $3.10 \mathrm{e}-03_{1.80 \mathrm{e}-03}$ | $0.00 \mathrm{e}+00_{0.00 \mathrm{e}+00}$ | $1.25 \mathrm{e}-03_{8.63 \mathrm{e}-04}$ | $7.84 \mathrm{e}+02_{2.76 \mathrm{e}+01}$ | $1.04 \mathrm{e}+01_{2.38 \mathrm{e}+00}$ |
| 09 |  | $1.40 \mathrm{e}+01_{3.23 \mathrm{e}+00}$ | $5.70 \mathrm{e}+01_{1.78 \mathrm{e}+01}$ | $2.69 \mathrm{e}+01_{3.85 \mathrm{e}+00}$ | $1.76 \mathrm{e}+01_{2.59 \mathrm{e}+00}$ | $7.44 \mathrm{e}+02_{2.57 \mathrm{e}+01}$ | $6.65 \mathrm{e}+00_{2.83 \mathrm{e}+00}$ |
| 10 |  | $3.52 \mathrm{e}+03_{1.06 \mathrm{e}+03}$ | $1.83 \mathrm{e}+01_{4.03 \mathrm{e}+00}$ | $5.22 \mathrm{e}+01_{7.46 \mathrm{e}+01}$ | $1.84 \mathrm{e}+01_{3.07 \mathrm{e}+00}$ | $1.25 \mathrm{e}+04_{1.32 \mathrm{e}+03}$ | $1.14 \mathrm{e}+03_{4.20 \mathrm{e}+02}$ |
| 11 |  | $2.74 \mathrm{e}+03_{1.06 \mathrm{e}+03}$ | $1.07 \mathrm{e}+04_{4.46 \mathrm{e}+02}$ | $1.13 \mathrm{e}+04_{1.54 \mathrm{e}+03}$ | $9.98 \mathrm{e}+03_{9.20 \mathrm{e}+02}$ | $1.24 \mathrm{e}+04_{6.97 \mathrm{e}+02}$ | $1.67 \mathrm{e}+03_{4.84 \mathrm{e}+02}$ |
| 12 |  | $1.20 \mathrm{e}-01_{5.93 \mathrm{e}-01}$ | $4.12 \mathrm{e}-01_{4.48 \mathrm{e}-02}$ | $2.44 \mathrm{e}-01_{1.31 \mathrm{e}-01}$ | $2.86 \mathrm{e}-01_{8.56 \mathrm{e}-02}$ | $1.91 \mathrm{e}-02_{3.68 \mathrm{e}-02}$ | $3.90 \mathrm{e}+00_{2.45 \mathrm{e}-01}$ |
| 13 |  | $5.42 \mathrm{e}-01_{6.52 \mathrm{e}-02}$ | $3.28 \mathrm{e}-01_{2.50 \mathrm{e}-02}$ | $2.19 \mathrm{e}-01_{3.12 \mathrm{e}-02}$ | $1.35 \mathrm{e}-01_{1.78 \mathrm{e}-02}$ | $4.70 \mathrm{e}-01_{5.49 \mathrm{e}-02}$ | $2.50 \mathrm{e}-01_{2.48 \mathrm{e}-02}$ |
| 14 |  | $3.82 \mathrm{e}-01_{5.61 \mathrm{e}-02}$ | $1.71 \mathrm{e}-01_{1.16 \mathrm{e}+02}$ | $1.22 \mathrm{e}-01_{1.14 \mathrm{e}-02}$ | $3.62 \mathrm{e}-01_{9.97 \mathrm{e}-03}$ | $2.78 \mathrm{e}-01_{4.18 \mathrm{e}-02}$ | $3.03 \mathrm{e}-01_{3.83 \mathrm{e}-02}$ |
| 15 |  | $1.22 \mathrm{e}+01_{1.12 \mathrm{e}+01}$ | $1.64 \mathrm{e}+01_{9.92 \mathrm{e}-01}$ | $1.25 \mathrm{e}+01_{2.73 \mathrm{e}+00}$ | $1.24 \mathrm{e}+01_{1.09 \mathrm{e}+00}$ | $6.38 \mathrm{e}+01_{4.12 \mathrm{e}+00}$ | $1.03 \mathrm{e}+01_{6.29 \mathrm{e}-01}$ |
| 16 |  | $3.41 \mathrm{e}+01_{2.69 \mathrm{e}+00}$ | $3.87 \mathrm{e}+01_{5.12 \mathrm{e}-01}$ | $4.20 \mathrm{e}+01_{1.11 \mathrm{e}+00}$ | $3.69 \mathrm{e}+01_{1.55 \mathrm{e}+00}$ | $4.35 \mathrm{e}+01_{8.64 \mathrm{e}-01}$ | $4.13 \mathrm{e}+01_{6.57 \mathrm{e}-01}$ |
| 17 | Hybrid function | $1.87 \mathrm{e}+02_{6.00 \mathrm{e}+02}$ | $2.06 \mathrm{e}+03_{2.49 \mathrm{e}+02}$ | $4.19 \mathrm{e}+03_{5.03 \mathrm{e}+02}$ | $4.66 \mathrm{e}+03_{6.35 \mathrm{e}+02}$ | $6.70 \mathrm{e}+03_{4.61 \mathrm{e}+02}$ | $7.12 \mathrm{e}+02_{1.55 \mathrm{e}+02}$ |
| 18 |  | $5.65 \mathrm{e}+00_{1.64 \mathrm{e}+00}$ | $9.49 \mathrm{e}+01_{2.41 \mathrm{e}+01}$ | $2.17 \mathrm{e}+02_{1.59 \mathrm{e}+01}$ | $2.37 \mathrm{e}+02_{2.32 \mathrm{e}+01}$ | $2.70 \mathrm{e}+02_{2.34 \mathrm{e}+01}$ | $6.60 \mathrm{e}+01_{1.86 \mathrm{e}+01}$ |
| 19 |  | $7.84 \mathrm{e}+01_{1.74 \mathrm{e}+01}$ | $8.84 \mathrm{e}+01_{8.88 \mathrm{e}-01}$ | $9.47 \mathrm{e}+01_{2.38 \mathrm{e}+00}$ | $9.49 \mathrm{e}+01_{1.39 \mathrm{e}+00}$ | $9.23 \mathrm{e}+01_{5.20 \mathrm{e}-01}$ | $9.15 \mathrm{e}+01_{1.51 \mathrm{e}+00}$ |
| 20 |  | $4.01 \mathrm{e}+00_{6.23 \mathrm{e}-01}$ | $2.18 \mathrm{e}+01_{4.12 \mathrm{e}+00}$ | $1.36 \mathrm{e}+02_{5.01 \mathrm{e}+01}$ | $1.44 \mathrm{e}+02_{3.39 \mathrm{e}+01}$ | $1.82 \mathrm{e}+02_{1.95 \mathrm{e}+1}$ | $6.42 \mathrm{e}+00_{1.55 \mathrm{e}+00}$ |
| 21 |  | $2.54 \mathrm{e}+02_{5.27 \mathrm{e}+02}$ | $6.31 \mathrm{e}+02_{1.98 \mathrm{e}+02}$ | $2.21 \mathrm{e}+03_{5.59 \mathrm{e}+02}$ | $2.35 \mathrm{e}+03_{5.36 \mathrm{e}+02}$ | $3.85 \mathrm{e}+03_{2.89 \mathrm{e}+02}$ | $2.78 \mathrm{e}+02_{1.06 \mathrm{e}+02}$ |
| 22 |  | $4.49 \mathrm{e}+02_{1.37 \mathrm{e}+02}$ | $1.03 \mathrm{e}+03_{2.24 \mathrm{e}+02}$ | $1.16 \mathrm{e}+03_{2.82 \mathrm{e}+02}$ | $8.73 \mathrm{e}+02_{5.36 \mathrm{e}+02}$ | $1.75 \mathrm{e}+03_{5.17 \mathrm{e}+02}$ | $4.55 \mathrm{e}+01_{2.92 \mathrm{e}+01}$ |
| 23 | Composition functions | $3.48 \mathrm{e}+02_{0.44 \mathrm{e}-06}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $3.48 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $3.48 \mathrm{e}+02_{1.24 \mathrm{e}-03}$ | $3.48 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ |
| 24 |  | $3.70 \mathrm{e}+02_{2.00 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $3.96 \mathrm{e}+02_{2.30 \mathrm{e}+00}$ | $3.82 \mathrm{e}+02_{2.94 \mathrm{e}+00}$ | $3.75 \mathrm{e}+02_{2.82 \mathrm{e}+00}$ |
| 25 |  | $2.14 \mathrm{e}+02_{2.51 \mathrm{e}-01}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.15 \mathrm{e}+02_{2.25 \mathrm{e}-01}$ | $2.15 \mathrm{e}+02_{4.73 \mathrm{e}-01}$ |
| 26 |  | $2.00 \mathrm{e}+02_{1.23 \mathrm{e}-04}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $1.76 \mathrm{e}+02_{4.34 \mathrm{e}+01}$ | $2.00 \mathrm{e}+02_{2.96 \mathrm{e}-04}$ |
| 27 |  | $3.09 \mathrm{e}+02_{0.18 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $3.61 \mathrm{e}+02_{2.58 \mathrm{e}+01}$ | $4.57 \mathrm{e}+02_{4.11 \mathrm{e}+01}$ | $3.38 \mathrm{e}+02_{2.97 \mathrm{e}+01}$ |
| 28 |  | $1.83 \mathrm{e}+03_{4.93 \mathrm{e}+02}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $2.33 \mathrm{e}+03_{4.09 \mathrm{e}+01}$ | $3.12 \mathrm{e}+03_{1.00 \mathrm{e}+03}$ | $2.30 \mathrm{e}+03_{8.11 \mathrm{e}+01}$ |
| 29 |  | $6.50 \mathrm{e}+02_{2.30 \mathrm{e}+01}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $9.21 \mathrm{e}+02_{1.62 \mathrm{e}+02}$ | $7.57 \mathrm{e}+02_{4.63 \mathrm{e}+01}$ | $7.12 \mathrm{e}+02_{0.73 \mathrm{e}+00}$ | $1.07 \mathrm{e}+03_{1.39 \mathrm{e}+02}$ |
| 30 |  | $1.94 \mathrm{e}+03_{1.38 \mathrm{e}+02}$ | $2.00 \mathrm{e}+02_{0.00 \mathrm{e}+00}$ | $8.36 \mathrm{e}+03_{1.02 \mathrm{e}+03}$ | $8.23 \mathrm{e}+03_{2.68 \mathrm{e}+02}$ | $6.48 \mathrm{e}+03_{3.87 \mathrm{e}+2}$ | $8.48 \mathrm{e}+03_{9.60 \mathrm{e}+02}$ |

The bold data indicates the optimal result
by these eight algorithms to solve the benchmarks of different dimensionalities. ACSEDA is the most efficient algorithm. $\mathrm{E}_{3}$-EDA has similar performance to ELSHADE-SPACMA in terms of time consumption and surpasses the remaining two algorithms.

Through the above experimental studies, the competitive performance of our $\mathrm{E}_{3}$-EDA is fully demonstrated with comparisons of the top methods in CEC competitions. In addition to the superiority in optimization accuracy, our $\mathrm{E}_{3}$-EDA possesses another two advantages. First, $\mathrm{E}_{3}$-EDA has fewer free parameters than other state-of-the-art methods, which can enhance its robustness in dealing with different problems.

On the other hand, the optimal parameter values are determined in the CEC 2014 30-D test, and these settings also support the promising performance of $\mathrm{E}_{3}$-EDA in addressing the CEC 2018 problems, which demonstrates the insensitivity of the algorithm performance to parameter settings. Second, $\mathrm{E}_{3}$-EDA not only achieves the best performance but also shows satisfactory computational efficiency. High efficiency and accuracy are two important indexes for assessing an evolutionary algorithm in practical engineering applications. Thus, our proposal has great potential for addressing real world optimization problems.

Table 12 Performance ranking of six algorithms for different types of test functions in different dimension CEC 2014 tests

| Type | Dimensions | $\mathrm{E}_{3}$-EDA | LSHADE-EpSin | UMOEAsII | L-SHADE | MLS-EDA | ACSEDA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Unimodal functions | 10D | 1 | 1 | 1 | 1 | 1 | 1 |
|  | 30D | 1 | 1 | 1 | 1 | 1 | 1 |
|  | 50D | 1 | 5 | 4 | 6 | 1 | 1 |
|  | 100D | 5 | 3 | 1 | 4 | 6 | 2 |
| Multimodal functions | 10D | 2 | 4 | 1 | 3 | 6 | 5 |
|  | 30D | 3 | 2 | 1 | 4 | 5 | 6 |
|  | 50D | 1 | 3 | 2 | 3 | 5 | 6 |
|  | 100D | 1 | 4 | 3 | 2 | 6 | 5 |
| Hybrid function | 10D | 1 | 4 | 3 | 2 | 5 | 6 |
|  | 30D | 1 | 3 | 6 | 4 | 5 | 2 |
|  | 50D | 1 | 3 | 5 | 4 | 6 | 2 |
|  | 100D | 1 | 3 | 4 | 5 | 6 | 2 |
| Composition functions | 10D | 4 | 1 | 2 | 3 | 6 | 5 |
|  | 30D | 4 | 2 | 3 | 5 | 1 | 6 |
|  | 50D | 4 | 1 | 2 | 5 | 3 | 6 |
|  | 100D | 3 | 1 | 2 | 4 | 5 | 6 |

The bold data indicates the optimal result

Table 13 Pairwise comparison using the Wilcoxon signed-rank test for the CEC 2014 test $(\alpha=$ 0.05 )

| Dimensions | $\mathrm{E}_{3}$-EDA | $\pm 1 \%$ | $R+$ | $R-$ | $p$ value |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 10D | vs. LSHADE-EpSin | 12/13/5 | 135 | 190 | $4.5934 \mathrm{e}-01(>\alpha)$ |
|  | vs. UMOEAsII | 9/15/6 | 97.5 | 202.5 | $1.3359 \mathrm{e}-01(>\alpha)$ |
|  | vs. L-SHADE | 15/9/6 | 166.5 | 133.5 | $6.3731 \mathrm{e}-01(>\alpha)$ |
|  | vs. MLS-EDA | 20/4/6 | 249 | 51 | $4.6756 \mathrm{e}-03(<\alpha)$ |
|  | vs. ACSEDA | 16/7/7 | 211 | 65 | $2.6400 \mathrm{e}-02(<\alpha)$ |
| 30D | vs. LSHADE-EpSin | 12/12/6 | 147 | 153 | $9.3169 \mathrm{e}-01(>\alpha)$ |
|  | vs. UMOEAsII | 13/11/6 | 166 | 134 | $6.4755 \mathrm{e}-01(>\alpha)$ |
|  | vs. L-SHADE | 17/6/7 | 215 | 61 | $1.9183 \mathrm{e}-02(<\alpha)$ |
|  | vs. MLS-EDA | 13/9/8 | 145 | 108 | $5.4810 \mathrm{e}-01(>\alpha)$ |
|  | vs. ACSEDA | 17/5/8 | 208 | 45 | $8.1420 \mathrm{e}-03(<\alpha)$ |
| 50D | vs. LSHADE-EpSin | 14/12/4 | 160 | 191 | $6.9383 \mathrm{e}-01(>\alpha)$ |
|  | vs. UMOEAsII | 14/11/5 | 170 | 155 | $8.4007 \mathrm{e}-01(>\alpha)$ |
|  | vs. L-SHADE | 18/6/6 | 215 | 85 | $6.3291 \mathrm{e}-01(>\alpha)$ |
|  | vs. MLS-EDA | 13/10/7 | 165 | 111 | $4.1153 \mathrm{e}-01(>\alpha)$ |
|  | vs. ACSEDA | 13/10/7 | 166.5 | 109.5 | $3.8601 \mathrm{e}-01(>\alpha)$ |
| 100D | vs. LSHADE-EpSin | 14/15/1 | 217 | 189 | $7.4988 \mathrm{e}-01(>\alpha)$ |
|  | vs. UMOEAsII | 16/13/1 | 254 | 152 | $2.4550 \mathrm{e}-01(>\alpha)$ |
|  | vs. L-SHADE | 20/8/2 | 316 | 62 | $2.2786 \mathrm{e}-03(<\alpha)$ |
|  | vs. MLS-EDA | 23/6/1 | 385.5 | 49.5 | $2.8036 \mathrm{e}-04(<\alpha)$ |
|  | vs. ACSEDA | 16/12/2 | 252 | 126 | $1.3013 \mathrm{e}-01(>\alpha)$ |

Table 14 Multi-comparison using the Friedman test for the CEC 2014 test $(\alpha=0.05)$

| Dimensions | $\mathrm{E}_{3}$-EDA | LSHADE-EpSin | UMOEAsII | L-SHADE | MLS-EDA | ACSEDA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Rankings |  |  |  |  |  |  |
| $10 \mathrm{D}^{\mathrm{a}}$ | 3.1000 | 3.2333 | 2.5500 | 3.1167 | 4.8167 | 4,1833 |
| $30 \mathrm{D}^{\mathrm{b}}$ | 3.0167 | 3.0833 | 3.3500 | 3.9333 | 3.4667 | 4.1500 |
| $50 \mathrm{D}^{\mathrm{c}}$ | 3.1167 | 3.2667 | 3.4500 | 4.1000 | 3.4167 | 3.6500 |
| $100 \mathrm{D}^{\mathrm{d}}$ | 2.8500 | 2.8833 | 3.2667 | 3.8333 | 4.7167 | 3.4500 |

The bold data indicates the optimal result ${ }^{\mathrm{a}} p$ value is $8.26 \mathrm{e}-07$, Chi-square is 36.30 ${ }^{\mathrm{b}} p$ value is $4.40 \mathrm{e}-02$, Chi-square is 11.40 ${ }^{\mathrm{c}} p$ value is $2.97 \mathrm{e}-01$, Chi-square is 6.09 ${ }^{\mathrm{d}} p$ value is $4.02 \mathrm{e}-04$, Chi-square is 22.60

| Dimensions | $\mathrm{E}_{3}$-EDA | LSHADE-EpSin | UMOEAsII | L-SHADE | MLS-EDA | ACSEDA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Mean time (in second) |  |  |  |  |  |  |
| 10D | 0.7903 | 1.2849 | 1.4370 | 0.7720 | 0.9907 | 0.7501 |
| 30D | 5.9529 | 7.6956 | 6.6493 | 5.6963 | 6.1641 | 5.0922 |
| 50D | 16.9428 | 19.8739 | 17.5009 | 16.2702 | 17.9383 | 14.1098 |
| 100D | 92.5278 | 98.9056 | 93.8175 | 85.3469 | 88.8192 | 65.3479 |

The bold data indicates the optimal result
Table 16 Parameter settings of $\mathrm{E}_{3}$-EDA, HSES, LSHADE-RSP, ELSHADE-SPACMA, EBOwithCMAR, and ACSEDA in the CEC2017 test

| Algorithm | Year | Parameter settings |
| :--: | :--: | :--: |
| $\mathrm{E}_{3}$-EDA | - | $\mathrm{NP}=18 \cdot D,|\boldsymbol{A}|=3 \cdot \mathrm{NP},|\boldsymbol{L}|=0.1 \cdot \mathrm{NP}$ |
| HSES | 2018 | $\mathrm{NP}=80+3 \ln D, M_{\text {step } 1}=200, N_{\text {step } 1}=100, \mathrm{cc}=0.96, I=20, M_{\text {step } 4}=200$ and $N_{\text {step } 4}=160$ for $10 \cdot D$ and $30 \cdot D, M_{\text {step } 4}=450$ and $N_{\text {step } 4}=360$ for $50 \cdot D$ and $100 \cdot D$ |
| LSHADE-RSP | 2018 | $\mathrm{NP}_{\text {max }}=75 \cdot D^{(2 / 3)}, \mathrm{NP}_{\text {min }}=4, H=5, \mu F_{\mathrm{r}}=0.3, \mu C_{\mathrm{r}}=0.8, \mathrm{pb}=0.085+0.085 \mathrm{FEs} / \mathrm{FEs}_{\text {max }}$ |
| ELSHADE-SPACMA | 2018 | $\mathrm{NP}=18 \cdot D, \mathrm{NP}_{\text {min }}=4, c=0.8$, Arc-rate $=1.4, F_{C P}=0.5, p^{\text {init }}=0.3, p^{\text {min }}=0.15, H=5, p=0.1$ |
| EBOwithCMAR | 2017 | $\mathrm{NP}_{1, \text { max }}=18 \cdot D, \mathrm{NP}_{1, \text { min }}=4, \mathrm{NP}_{2, \text { max }}=46.8 \cdot D, \mathrm{NP}_{2, \text { min }}=10, \mathrm{NP}_{3}=4+3 \log D, H=6, \mu=\mathrm{NP}_{2} / 2, \sigma$ $=0.3$, <br> CS $=200$ for $10 \cdot D$ and $30 \cdot D$ or $\mathrm{CS}=300$ for $50 \cdot D$ and $100 \cdot D$ |
| ACSEDA | 2021 | $\mathrm{NP}=800$ for $10 \cdot D, \mathrm{NP}=1300$ for $30 \cdot D, \mathrm{NP}=1800$ for $50 \cdot D$ and $\mathrm{NP}=3200$ for $100 \cdot D, s_{\max }=0.35, s_{\min }$ $=0.1$ |

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

| Type | Dimensions | $\mathrm{E}_{3}$-EDA | HSES | LSHADE-RSP | ELSHADE-SPACMA | EBOwithCMAR | ACSEDA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Unimodal functions | 10D | 1 | 1 | 1 | 1 | 1 | 1 |
|  | 30D | 1 | 1 | 1 | 1 | 1 | 1 |
|  | 50D | 1 | 1 | 1 | 1 | 1 | 1 |
|  | 100D | 6 | 1 | 2 | 3 | 5 | 4 |
| Multimodal functions | 10D | 1 | 3 | 3 | 5 | 2 | 6 |
|  | 30D | 1 | 4 | 5 | 6 | 2 | 3 |
|  | 50D | 2 | 1 | 5 | 5 | 4 | 3 |
|  | 100D | 5 | 1 | 6 | 2 | 4 | 2 |
| Hybrid function | 10D | 4 | 6 | 1 | 3 | 2 | 5 |
|  | 30D | 1 | 4 | 3 | 5 | 6 | 2 |
|  | 50D | 1 | 3 | 4 | 4 | 5 | 2 |
|  | 100D | 1 | 2 | 5 | 4 | 6 | 3 |
| Composite functions | 10D | 4 | 6 | 2 | 3 | 1 | 5 |
|  | 30D | 1 | 6 | 3 | 5 | 2 | 4 |
|  | 50D | 1 | 3 | 3 | 5 | 5 | 2 |
|  | 100D | 1 | 3 | 5 | 4 | 6 | 2 |

The bold data indicates the optimal result

Table 22 Pairwise comparison using the Wilcoxon signed-rank test for the CEC 2018 tests

| $\mathrm{E}_{3}$-EDA |  | $\pm 1 / 2$ | $R+$ | $R-$ | $p$ value |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 10D |  |  |  |  |  |
| vs. HSES |  | 20/5/4 | 286.5 | 38.5 | $8.4761 \mathrm{e}-04(<\alpha)$ |
| vs. LSHADE-RSP |  | 8/15/6 | 87 | 189 | $1.2078 \mathrm{e}-01(>\alpha)$ |
| vs. ELSHADE-SPACMA |  | 12/10/7 | 141 | 112 | $6.3773 \mathrm{e}-01(>\alpha)$ |
| vs. EBOwithCMAR |  | 11/12/6 | 124 | 152 | $6.7025 \mathrm{e}-01(>\alpha)$ |
| vs. ACSEDA |  | 16/7/6 | 222 | 54 | $1.0623 \mathrm{e}-02(<\alpha)$ |
| 30D |  |  |  |  |  |
| vs. HSES |  | 22/1/6 | 260 | 16 | $2.0675 \mathrm{e}-04(<\alpha)$ |
| vs. LSHADE-RSP |  | 20/3/6 | 238 | 38 | $2.3541 \mathrm{e}-03(<\alpha)$ |
| vs. ELSHADE-SPACMA |  | 21/2/6 | 256 | 20 | $3.3173 \mathrm{e}-04(<\alpha)$ |
| vs. EBOwithCMAR |  | 19/4/6 | 246 | 30 | $1.0205 \mathrm{e}-03(<\alpha)$ |
| vs. ACSEDA |  | 21/3/5 | 243 | 57 | $7.8806 \mathrm{e}-03(<\alpha)$ |
| 50D |  |  |  |  |  |
| vs. HSES |  | 19/6/4 | 279 | 46 | $1.7206 \mathrm{e}-03(<\alpha)$ |
| vs. LSHADE-RSP |  | 22/3/4 | 292 | 33 | $3.9136 \mathrm{e}-04(<\alpha)$ |
| vs. ELSHADE-SPACMA |  | 22/3/4 | 294 | 31 | $4.0277 \mathrm{e}-04(<\alpha)$ |
| vs. EBOwithCMAR |  | 22/4/3 | 319 | 33 | $2.9534 \mathrm{e}-04(<\alpha)$ |
| vs. ACSEDA |  | 20/6/3 | 278 | 73 | $9.2273 \mathrm{e}-03(<\alpha)$ |
| 100D |  |  |  |  |  |
| vs. HSES |  | 15/14/0 | 264 | 171 | $3.1467 \mathrm{e}-01(>\alpha)$ |
| vs. LSHADE-RSP |  | 23/6/0 | 403 | 32 | $6.0436 \mathrm{e}-05(<\alpha)$ |
| vs. ELSHADE-SPACMA |  | 21/7/1 | 362 | 44 | $2.9386 \mathrm{e}-04(<\alpha)$ |
| vs. EBOwithCMAR |  | 25/4/0 | 416 | 19 | $1.7691 \mathrm{e}-05(<\alpha)$ |
| vs. ACSEDA |  | 17/12/0 | 289.5 | 145.5 | $1.1195 \mathrm{e}-01(>\alpha)$ |

Table 23 Multi-comparison using the Friedman test for the CEC 2018 tests $(\alpha=0.05)$

| Algorithms | $\mathrm{E}_{3}$-EDA | HSES | LSHADE-RSP | ELSHADE-SPACMA | EBOwithCMAR | ACSEDA |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Rankings |  |  |  |  |  |  |
| $10 \mathrm{D}^{\mathrm{a}}$ | 3.1897 | 4.4828 | $\mathbf{2 . 7 5 8 6}$ | 3.3621 | 2.9138 | 4.2931 |
| $30 \mathrm{D}^{\mathrm{b}}$ | $\mathbf{1 . 9 4 8 3}$ | 4.2759 | 3.6552 | 4.3621 | 3.5172 | 3.2414 |
| $50 \mathrm{D}^{\mathrm{c}}$ | $\mathbf{2 . 0 6 9 0}$ | 3.1724 | 4.0172 | 4.3103 | 4.4310 | 3.0000 |
| $100 \mathrm{D}^{\mathrm{d}}$ | $\mathbf{2 . 5 0 0 0}$ | 2.7069 | 4.3276 | 3.9310 | 4.7241 | 2.8103 |

The bold data indicates the optimal result
${ }^{a} p$ value is $6.43 \mathrm{e}-05$, Chi-square is 26.73
${ }^{b} p$ value is $1.78 \mathrm{e}-07$, Chi-square is 39.62
${ }^{c} p$ value is $2.11 \mathrm{e}-07$, Chi-square is 39.25
${ }^{d} p$ value is $4.18 \mathrm{e}-07$, Chi-square is 37.78

Table 24 Comparison of the computational efficiency for the CEC 2018 tests

| Algorithms | $\mathrm{E}_{3}$-EDA | HSES | LSHADE-RSP | ELSHADE-SPACMA | EBOwithCMAR | ACSEDA |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| Mean times (in second) |  |  |  |  |  |  |
| 10D | 0.4606 | 0.5997 | - | 0.6646 | 1.3154 | 0.2476 |
| 30D | 3.3219 | 3.9298 | - | 3.5474 | 5.9632 | 2.6106 |
| 50D | 10.5447 | 17.1198 | - | 12.8936 | 15.4682 | 8.4956 |
| 100D | 74.1166 | 114.1000 | - | 68.3402 | 91.8002 | 58.7012 |

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

| No. | Types | Dimensionality $=10$ |  |  |  |  | Dimensionality $=30$ |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Best | Worst | Median | Mean | SD | Best | Worst | Median | Mean | SD |
| 01 | Unimodal functions | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 02 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 03 | Multimodal functions | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 04 |  | $0.00 \mathrm{e}+00$ | $3.48 \mathrm{e}+01$ | $3.48 \mathrm{e}+01$ | $2.82 \mathrm{e}+01$ | $1.40 \mathrm{e}+01$ | $2.39 \mathrm{e}-04$ | $5.45 \mathrm{e}+01$ | $1.75 \mathrm{e}+00$ | $7.61 \mathrm{e}+00$ | $1.33 \mathrm{e}+01$ |
| 05 |  | $0.00 \mathrm{e}+00$ | $2.00 \mathrm{e}+01$ | $2.00 \mathrm{e}+01$ | $1.33 \mathrm{e}+01$ | $9.66 \mathrm{e}+00$ | $2.00 \mathrm{e}+01$ | $2.10 \mathrm{e}+01$ | $2.00 \mathrm{e}+01$ | $2.00 \mathrm{e}+01$ | $1.90 \mathrm{e}-01$ |
| 06 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 07 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 08 |  | $0.00 \mathrm{e}+00$ | $9.95 \mathrm{e}-01$ | $0.00 \mathrm{e}+00$ | $9.48 \mathrm{e}-02$ | $2.99 \mathrm{e}-01$ | $0.00 \mathrm{e}+00$ | $3.98 \mathrm{e}+00$ | $9.95 \mathrm{e}-01$ | $1.07 \mathrm{e}+00$ | $9.92 \mathrm{e}-01$ |
| 09 |  | $0.00 \mathrm{e}+00$ | $9.95 \mathrm{e}-01$ | $0.00 \mathrm{e}+00$ | $2.84 \mathrm{e}-01$ | $4.61 \mathrm{e}-01$ | $0.00 \mathrm{e}+00$ | $2.98 \mathrm{e}+00$ | $4.30 \mathrm{e}-08$ | $5.85 \mathrm{e}-01$ | $7.22 \mathrm{e}-01$ |
| 10 |  | $3.96 \mathrm{e}+00$ | $2.57 \mathrm{e}+01$ | $1.50 \mathrm{e}+01$ | $1.49 \mathrm{e}+01$ | $5.88 \mathrm{e}+00$ | $2.06 \mathrm{e}+01$ | $8.91 \mathrm{e}+02$ | $3.63 \mathrm{e}+01$ | $8.11 \mathrm{e}+01$ | $1.54 \mathrm{e}+02$ |
| 11 |  | $1.25 \mathrm{e}-01$ | $1.21 \mathrm{e}+01$ | $3.12 \mathrm{e}-01$ | $1.39 \mathrm{e}+00$ | $3.54 \mathrm{e}+00$ | $2.45 \mathrm{e}-01$ | $2.49 \mathrm{e}+02$ | $7.40 \mathrm{e}+00$ | $5.23 \mathrm{e}+01$ | $7.19 \mathrm{e}+01$ |
| 12 |  | $0.00 \mathrm{e}+00$ | $1.51 \mathrm{e}-02$ | $0.00 \mathrm{e}+00$ | $7.20 \mathrm{e}-04$ | $3.30 \mathrm{e}-03$ | $1.90 \mathrm{e}-04$ | $2.18 \mathrm{e}-02$ | $4.71 \mathrm{e}-03$ | $5.75 \mathrm{e}-03$ | $5.03 \mathrm{e}-03$ |
| 13 |  | $2.37 \mathrm{e}-02$ | $1.09 \mathrm{e}-01$ | $4.94 \mathrm{e}-02$ | $5.22 \mathrm{e}-02$ | $2.31 \mathrm{e}-02$ | $1.47 \mathrm{e}-01$ | $2.98 \mathrm{e}-01$ | $2.34 \mathrm{e}-01$ | $2.32 \mathrm{e}-01$ | $3.63 \mathrm{e}-02$ |
| 14 |  | $2.43 \mathrm{e}-01$ | $4.51 \mathrm{e}-01$ | $3.61 \mathrm{e}-01$ | $3.57 \mathrm{e}-01$ | $6.12 \mathrm{e}-02$ | $2.64 \mathrm{e}-01$ | $4.20 \mathrm{e}-01$ | $3.56 \mathrm{e}-01$ | $3.51 \mathrm{e}-01$ | $3.82 \mathrm{e}-02$ |
| 15 |  | $0.00 \mathrm{e}+00$ | $9.33 \mathrm{e}-01$ | $4.03 \mathrm{e}-01$ | $3.51 \mathrm{e}-01$ | $3.47 \mathrm{e}-01$ | $6.18 \mathrm{e}-01$ | $3.29 \mathrm{e}+00$ | $2.42 \mathrm{e}+00$ | $2.39 \mathrm{e}+00$ | $4.33 \mathrm{e}-01$ |
| 16 | Hybrid function | $9.72 \mathrm{e}-02$ | $1.12 \mathrm{e}+00$ | $2.62 \mathrm{e}-01$ | $3.46 \mathrm{e}-01$ | $2.53 \mathrm{e}-01$ | $5.01 \mathrm{e}+00$ | $1.05 \mathrm{e}+01$ | $6.37 \mathrm{e}+00$ | $6.50 \mathrm{e}+00$ | $8.77 \mathrm{e}-01$ |
| 17 |  | $0.00 \mathrm{e}+00$ | $1.20 \mathrm{e}+00$ | $2.08 \mathrm{e}-01$ | $3.45 \mathrm{e}-01$ | $2.41 \mathrm{e}-01$ | $6.94 \mathrm{e}-02$ | $1.48 \mathrm{e}+00$ | $2.78 \mathrm{e}-01$ | $6.13 \mathrm{e}-01$ | $5.07 \mathrm{e}-01$ |
| 18 | Hybrid function | $1.34 \mathrm{e}-04$ | $5.00 \mathrm{e}-01$ | $9.97 \mathrm{e}-02$ | $2.22 \mathrm{e}-01$ | $1.96 \mathrm{e}-01$ | $5.00 \mathrm{e}-01$ | $1.49 \mathrm{e}+00$ | $5.00 \mathrm{e}-01$ | $5.39 \mathrm{e}-01$ | $1.95 \mathrm{e}-01$ |
| 19 |  | $2.91 \mathrm{e}-02$ | $1.08 \mathrm{e}-01$ | $3.68 \mathrm{e}-02$ | $4.84 \mathrm{e}-02$ | $2.49 \mathrm{e}-02$ | $1.48 \mathrm{e}-01$ | $2.29 \mathrm{e}+00$ | $4.59 \mathrm{e}-01$ | $6.38 \mathrm{e}-01$ | $4.69 \mathrm{e}-01$ |
| 20 |  | $6.14 \mathrm{e}-02$ | $7.71 \mathrm{e}-01$ | $4.99 \mathrm{e}-01$ | $4.13 \mathrm{e}-01$ | $1.93 \mathrm{e}-01$ | $5.00 \mathrm{e}-01$ | $1.64 \mathrm{e}+00$ | $1.20 \mathrm{e}+00$ | $1.21 \mathrm{e}+00$ | $1.81 \mathrm{e}-01$ |
| 21 |  | $6.39 \mathrm{e}-03$ | $1.12 \mathrm{e}+00$ | $3.17 \mathrm{e}-01$ | $4.05 \mathrm{e}-01$ | $3.26 \mathrm{e}-01$ | $5.30 \mathrm{e}-01$ | $1.35 \mathrm{e}+00$ | $9.16 \mathrm{e}-01$ | $9.00 \mathrm{e}-01$ | $1.62 \mathrm{e}-01$ |
| 22 | Composition functions | $1.32 \mathrm{e}-01$ | $2.41 \mathrm{e}+01$ | $7.70 \mathrm{e}-01$ | $5.45 \mathrm{e}+00$ | $8.85 \mathrm{e}+00$ | $2.05 \mathrm{e}+01$ | $8.19 \mathrm{e}+01$ | $2.14 \mathrm{e}+01$ | $2.31 \mathrm{e}+01$ | $8.59 \mathrm{e}+00$ |
| 23 |  | $3.29 \mathrm{e}+02$ | $3.29 \mathrm{e}+02$ | $3.29 \mathrm{e}+02$ | $3.29 \mathrm{e}+02$ | $0.00 \mathrm{e}+00$ | $3.15 \mathrm{e}+02$ | $3.15 \mathrm{e}+02$ | $3.15 \mathrm{e}+02$ | $3.15 \mathrm{e}+02$ | $4.84 \mathrm{e}-13$ |
| 24 |  | $1.00 \mathrm{e}+02$ | $1.06 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.01 \mathrm{e}+02$ | $1.62 \mathrm{e}+00$ | $2.00 \mathrm{e}+02$ | $2.23 \mathrm{e}+02$ | $2.08 \mathrm{e}+02$ | $2.11 \mathrm{e}+02$ | $9.61 \mathrm{e}+00$ |
| 25 |  | $1.00 \mathrm{e}+02$ | $2.01 \mathrm{e}+02$ | $1.21 \mathrm{e}+02$ | $1.31 \mathrm{e}+02$ | $3.39 \mathrm{e}+01$ | $2.03 \mathrm{e}+02$ | $2.03 \mathrm{e}+02$ | $2.03 \mathrm{e}+02$ | $2.03 \mathrm{e}+02$ | $4.06 \mathrm{e}-02$ |
| 26 |  | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.73 \mathrm{e}-02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $4.16 \mathrm{e}-02$ |
| 27 |  | $4.93 \mathrm{e}-01$ | $4.00 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $2.05 \mathrm{e}+02$ | $2.01 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $4.00 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $3.14 \mathrm{e}+02$ | $3.48 \mathrm{e}+01$ |
| 28 |  | $3.57 \mathrm{e}+02$ | $4.99 \mathrm{e}+02$ | $3.60 \mathrm{e}+02$ | $4.11 \mathrm{e}+02$ | $6.21 \mathrm{e}+01$ | $3.00 \mathrm{e}+02$ | $8.49 \mathrm{e}+02$ | $7.75 \mathrm{e}+02$ | $7.27 \mathrm{e}+02$ | $1.30 \mathrm{e}+02$ |
| 29 |  | $1.58 \mathrm{e}+02$ | $2.23 \mathrm{e}+02$ | $2.22 \mathrm{e}+02$ | $2.19 \mathrm{e}+02$ | $1.40 \mathrm{e}+01$ | $1.00 \mathrm{e}+02$ | $7.18 \mathrm{e}+02$ | $1.49 \mathrm{e}+02$ | $1.93 \mathrm{e}+02$ | $1.57 \mathrm{e}+02$ |
| 30 |  | $4.54 \mathrm{e}+02$ | $5.50 \mathrm{e}+02$ | $4.60 \mathrm{e}+02$ | $4.70 \mathrm{e}+02$ | $2.46 \mathrm{e}+01$ | $3.26 \mathrm{e}+02$ | $5.80 \mathrm{e}+02$ | $3.53 \mathrm{e}+02$ | $3.65 \mathrm{e}+02$ | $3.80 \mathrm{e}+01$ |

| No. | Types | Dimensionality $=50$ |  |  |  |  | Dimensionality $=100$ |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Best | Worst | Median | Mean | SD | Best | Worst | Median | Mean | SD |
| 01 | Unimodal functions | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $1.13 \mathrm{e}-04$ | $2.24 \mathrm{e}-04$ | $1.46 \mathrm{e}-04$ | $1.54 \mathrm{e}-04$ | $2.59 \mathrm{e}-05$ |
| 02 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $1.16 \mathrm{e}-02$ | $2.12 \mathrm{e}-02$ | $1.57 \mathrm{e}-02$ | $1.63 \mathrm{e}-02$ | $2.08 \mathrm{e}-03$ |
| 03 | Multimodal functions | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $2.06 \mathrm{e}-08$ | $3.15 \mathrm{e}-08$ | $2.53 \mathrm{e}-08$ | $2.53 \mathrm{e}-08$ | $2.97 \mathrm{e}-09$ |
| 04 |  | $2.25 \mathrm{e}+01$ | $9.81 \mathrm{e}+01$ | $8.35 \mathrm{e}+01$ | $7.42 \mathrm{e}+01$ | $1.74 \mathrm{e}+01$ | $1.26 \mathrm{e}+02$ | $2.03 \mathrm{e}+02$ | $1.43 \mathrm{e}+02$ | $1.55 \mathrm{e}+02$ | $2.16 \mathrm{e}+01$ |
| 05 |  | $2.00 \mathrm{e}+01$ | $2.12 \mathrm{e}+01$ | $2.00 \mathrm{e}+01$ | $2.00 \mathrm{e}+01$ | $1.68 \mathrm{e}-01$ | $2.00 \mathrm{e}+01$ | $2.13 \mathrm{e}+01$ | $2.00 \mathrm{e}+01$ | $2.02 \mathrm{e}+01$ | $3.51 \mathrm{e}-01$ |
| 06 |  | $3.16 \mathrm{e}-04$ | $7.13 \mathrm{e}-04$ | $4.17 \mathrm{e}-04$ | $4.40 \mathrm{e}-04$ | $7.86 \mathrm{e}-05$ | $2.40 \mathrm{e}-01$ | $1.37 \mathrm{e}+00$ | $2.99 \mathrm{e}-01$ | $4.32 \mathrm{e}-01$ | $3.33 \mathrm{e}-01$ |
| 07 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 08 |  | $6.63 \mathrm{e}-05$ | $6.97 \mathrm{e}+00$ | $2.99 \mathrm{e}+00$ | $3.36 \mathrm{e}+00$ | $1.91 \mathrm{e}+00$ | $1.68 \mathrm{e}+01$ | $2.79 \mathrm{e}+01$ | $2.24 \mathrm{e}+01$ | $2.21 \mathrm{e}+01$ | $3.17 \mathrm{e}+00$ |
| 09 |  | $6.90 \mathrm{e}-07$ | $4.98 \mathrm{e}+00$ | $1.99 \mathrm{e}+00$ | $2.19 \mathrm{e}+00$ | $1.24 \mathrm{e}+00$ | $5.17 \mathrm{e}+00$ | $2.19 \mathrm{e}+01$ | $1.39 \mathrm{e}+01$ | $1.40 \mathrm{e}+01$ | $3.23 \mathrm{e}+00$ |
| 10 |  | $6.85 \mathrm{e}+01$ | $9.45 \mathrm{e}+03$ | $2.67 \mathrm{e}+02$ | $5.53 \mathrm{e}+02$ | $1.30 \mathrm{e}+03$ | $1.64 \mathrm{e}+03$ | $6.93 \mathrm{e}+03$ | $3.26 \mathrm{e}+03$ | $3.52 \mathrm{e}+03$ | $1.06 \mathrm{e}+03$ |
| 11 |  | $1.02 \mathrm{e}+01$ | $5.83 \mathrm{e}+02$ | $1.56 \mathrm{e}+02$ | $2.04 \mathrm{e}+02$ | $1.45 \mathrm{e}+02$ | $1.32 \mathrm{e}+03$ | $5.26 \mathrm{e}+03$ | $2.37 \mathrm{e}+03$ | $2.74 \mathrm{e}+03$ | $1.06 \mathrm{e}+03$ |
| 12 |  | $3.65 \mathrm{e}-04$ | $7.07 \mathrm{e}-02$ | $6.37 \mathrm{e}-03$ | $1.35 \mathrm{e}-02$ | $1.60 \mathrm{e}-02$ | $6.35 \mathrm{e}-03$ | $4.27 \mathrm{e}+00$ | $2.97 \mathrm{e}-02$ | $1.20 \mathrm{e}-01$ | $5.93 \mathrm{e}-01$ |
| 13 |  | $2.71 \mathrm{e}-01$ | $4.37 \mathrm{e}-01$ | $3.59 \mathrm{e}-01$ | $3.61 \mathrm{e}-01$ | $4.04 \mathrm{e}-02$ | $3.69 \mathrm{e}-01$ | $6.81 \mathrm{e}-01$ | $5.44 \mathrm{e}-01$ | $5.42 \mathrm{e}-01$ | $6.52 \mathrm{e}-02$ |
| 14 |  | $2.42 \mathrm{e}-01$ | $4.25 \mathrm{e}-01$ | $3.62 \mathrm{e}-01$ | $3.56 \mathrm{e}-01$ | $4.16 \mathrm{e}-02$ | $2.94 \mathrm{e}-01$ | $4.97 \mathrm{e}-01$ | $3.68 \mathrm{e}-01$ | $3.82 \mathrm{e}-01$ | $5.16 \mathrm{e}-02$ |
| 15 |  | $3.47 \mathrm{e}+00$ | $6.05 \mathrm{e}+00$ | $4.41 \mathrm{e}+00$ | $4.45 \mathrm{e}+00$ | $5.03 \mathrm{e}-01$ | $7.53 \mathrm{e}+00$ | $6.70 \mathrm{e}+01$ | $1.02 \mathrm{e}+01$ | $1.22 \mathrm{e}+01$ | $1.12 \mathrm{e}+01$ |
| 16 | Hybrid function | $1.16 \mathrm{e}+01$ | $1.91 \mathrm{e}+01$ | $1.33 \mathrm{e}+01$ | $1.33 \mathrm{e}+01$ | $1.12 \mathrm{e}+00$ | $3.06 \mathrm{e}+01$ | $4.26 \mathrm{e}+01$ | $3.36 \mathrm{e}+01$ | $3.41 \mathrm{e}+01$ | $2.69 \mathrm{e}+00$ |
| 17 |  | $2.54 \mathrm{e}-01$ | $1.22 \mathrm{e}+01$ | $3.42 \mathrm{e}+00$ | $4.55 \mathrm{e}+00$ | $3.00 \mathrm{e}+00$ | $4.26 \mathrm{e}+01$ | $4.38 \mathrm{e}+03$ | $1.02 \mathrm{e}+02$ | $1.87 \mathrm{e}+02$ | $6.00 \mathrm{e}+02$ |
| 18 |  | $4.98 \mathrm{e}-01$ | $1.52 \mathrm{e}+00$ | $5.11 \mathrm{e}-01$ | $5.48 \mathrm{e}-01$ | $1.45 \mathrm{e}-01$ | $2.98 \mathrm{e}+00$ | $1.04 \mathrm{e}+01$ | $5.89 \mathrm{e}+00$ | $5.65 \mathrm{e}+00$ | $1.64 \mathrm{e}+00$ |
| 19 |  | $3.21 \mathrm{e}+00$ | $9.11 \mathrm{e}+00$ | $6.70 \mathrm{e}+00$ | $6.26 \mathrm{e}+00$ | $1.36 \mathrm{e}+00$ | $1.49 \mathrm{e}+01$ | $8.83 \mathrm{e}+01$ | $8.58 \mathrm{e}+01$ | $7.84 \mathrm{e}+01$ | $1.74 \mathrm{e}+01$ |
| 20 |  | $1.37 \mathrm{e}+00$ | $3.22 \mathrm{e}+00$ | $1.77 \mathrm{e}+00$ | $1.86 \mathrm{e}+00$ | $3.27 \mathrm{e}-01$ | $3.19 \mathrm{e}+00$ | $6.02 \mathrm{e}+00$ | $3.90 \mathrm{e}+00$ | $4.01 \mathrm{e}+00$ | $6.23 \mathrm{e}-01$ |
| 21 |  | $7.67 \mathrm{e}-01$ | $1.24 \mathrm{e}+02$ | $1.06 \mathrm{e}+00$ | $6.04 \mathrm{e}+00$ | $2.37 \mathrm{e}+01$ | $3.25 \mathrm{e}+01$ | $2.87 \mathrm{e}+03$ | $1.65 \mathrm{e}+02$ | $2.54 \mathrm{e}+02$ | $5.27 \mathrm{e}+02$ |
| 22 | Composition functions | $2.20 \mathrm{e}+01$ | $5.74 \mathrm{e}+02$ | $2.36 \mathrm{e}+01$ | $8.04 \mathrm{e}+01$ | $1.48 \mathrm{e}+02$ | $3.17 \mathrm{e}+01$ | $2.16 \mathrm{e}+03$ | $4.45 \mathrm{e}+01$ | $4.49 \mathrm{e}+02$ | $7.37 \mathrm{e}+02$ |
| 23 |  | $3.44 \mathrm{e}+02$ | $3.44 \mathrm{e}+02$ | $3.44 \mathrm{e}+02$ | $3.44 \mathrm{e}+02$ | $1.02 \mathrm{e}-12$ | $3.48 \mathrm{e}+02$ | $3.48 \mathrm{e}+02$ | $3.48 \mathrm{e}+02$ | $3.48 \mathrm{e}+02$ | $9.44 \mathrm{e}-06$ |
| 24 |  | $2.59 \mathrm{e}+02$ | $2.72 \mathrm{e}+02$ | $2.68 \mathrm{e}+02$ | $2.67 \mathrm{e}+02$ | $1.81 \mathrm{e}+00$ | $3.66 \mathrm{e}+02$ | $3.75 \mathrm{e}+02$ | $3.70 \mathrm{e}+02$ | $3.70 \mathrm{e}+02$ | $2.00 \mathrm{e}+00$ |
| 25 |  | $2.05 \mathrm{e}+02$ | $2.05 \mathrm{e}+02$ | $2.05 \mathrm{e}+02$ | $2.05 \mathrm{e}+02$ | $5.02 \mathrm{e}-02$ | $2.14 \mathrm{e}+02$ | $2.15 \mathrm{e}+02$ | $2.14 \mathrm{e}+02$ | $2.14 \mathrm{e}+02$ | $2.51 \mathrm{e}-01$ |
| 26 |  | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $4.39 \mathrm{e}-02$ | $2.00 \mathrm{e}+02$ | $2.00 \mathrm{e}+02$ | $2.00 \mathrm{e}+02$ | $2.00 \mathrm{e}+02$ | $1.23 \mathrm{e}-04$ |
| 27 |  | $3.00 \mathrm{e}+02$ | $3.47 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $3.02 \mathrm{e}+02$ | $9.89 \mathrm{e}+00$ | $3.05 \mathrm{e}+02$ | $3.40 \mathrm{e}+02$ | $3.06 \mathrm{e}+02$ | $3.09 \mathrm{e}+02$ | $9.18 \mathrm{e}+00$ |
| 28 |  | $8.55 \mathrm{e}+02$ | $1.26 \mathrm{e}+03$ | $1.08 \mathrm{e}+03$ | $1.04 \mathrm{e}+03$ | $9.54 \mathrm{e}+01$ | $1.39 \mathrm{e}+03$ | $2.78 \mathrm{e}+03$ | $1.56 \mathrm{e}+03$ | $1.83 \mathrm{e}+03$ | $4.93 \mathrm{e}+02$ |
| 29 |  | $3.38 \mathrm{e}+02$ | $3.75 \mathrm{e}+02$ | $3.49 \mathrm{e}+02$ | $3.51 \mathrm{e}+02$ | $8.62 \mathrm{e}+00$ | $5.95 \mathrm{e}+02$ | $6.87 \mathrm{e}+02$ | $6.56 \mathrm{e}+02$ | $6.50 \mathrm{e}+02$ | $2.30 \mathrm{e}+01$ |
| 30 |  | $1.06 \mathrm{e}+04$ | $1.28 \mathrm{e}+04$ | $1.13 \mathrm{e}+04$ | $1.14 \mathrm{e}+04$ | $3.78 \mathrm{e}+02$ | $1.72 \mathrm{e}+03$ | $2.31 \mathrm{e}+03$ | $1.93 \mathrm{e}+03$ | $1.94 \mathrm{e}+03$ | $1.38 \mathrm{e}+02$ |

C. Statistical error results obtained from the $\mathrm{E}_{3}$-EDA for the CEC 2018 10-D, 30-D, 50-D and 100-D tests.

| No. | Types | Dimensionality $=10$ |  |  |  |  | Dimensionality $=30$ |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Best | Worst | Median | Mean | SD | Best | Worst | Median | Mean | SD |
| 01 | Unimodal functions | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 03 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 04 | Multimodal functions | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $1.54 \mathrm{e}-03$ | $8.48 \mathrm{e}+01$ | $5.93 \mathrm{e}+01$ | $5.76 \mathrm{e}+01$ | $1.57 \mathrm{e}+01$ |
| 05 |  | $0.00 \mathrm{e}+00$ | $1.03 \mathrm{e}+00$ | $9.34 \mathrm{e}-02$ | $2.51 \mathrm{e}-01$ | $3.13 \mathrm{e}-01$ | $0.00 \mathrm{e}+00$ | $2.98 \mathrm{e}+00$ | $9.95 \mathrm{e}-01$ | $9.17 \mathrm{e}-01$ | $8.86 \mathrm{e}-01$ |
| 06 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 07 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $3.20 \mathrm{e}+01$ | $3.62 \mathrm{e}+01$ | $3.32 \mathrm{e}+01$ | $3.32 \mathrm{e}+01$ | $1.61 \mathrm{e}-01$ |
| 08 |  | $1.04 \mathrm{e}+01$ | $1.25 \mathrm{e}+01$ | $1.09 \mathrm{e}+01$ | $1.10 \mathrm{e}+01$ | $5.26 \mathrm{e}-01$ | $0.00 \mathrm{e}+00$ | $2.98 \mathrm{e}+00$ | $9.95 \mathrm{e}-01$ | $7.80 \mathrm{e}-01$ | $8.04 \mathrm{e}-01$ |
| 09 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ |
| 10 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $3.58 \mathrm{e}+00$ | $5.23 \mathrm{e}+02$ | $1.21 \mathrm{e}+02$ | $9.35 \mathrm{e}+01$ | $9.79 \mathrm{e}+01$ |
| 11 | Hybrid function | $1.87 \mathrm{e}-01$ | $9.42 \mathrm{e}+00$ | $3.43 \mathrm{e}-01$ | $1.31 \mathrm{e}+00$ | $2.44 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $6.00 \mathrm{e}+01$ | $0.00 \mathrm{e}+00$ | $2.60 \mathrm{e}+00$ | $8.42 \mathrm{e}+00$ |
| 12 |  | $0.00 \mathrm{e}+00$ | $8.50 \mathrm{e}-01$ | $5.46 \mathrm{e}-02$ | $1.83 \mathrm{e}-01$ | $2.56 \mathrm{e}-01$ | $1.39 \mathrm{e}-01$ | $4.86 \mathrm{e}-01$ | $3.47 \mathrm{e}-01$ | $3.28 \mathrm{e}-01$ | $9.00 \mathrm{e}-02$ |
| 13 |  | $0.00 \mathrm{e}+00$ | $6.24 \mathrm{e}-01$ | $4.16 \mathrm{e}-01$ | $3.12 \mathrm{e}-01$ | $1.70 \mathrm{e}-01$ | $0.00 \mathrm{e}+00$ | $1.54 \mathrm{e}+01$ | $1.33 \mathrm{e}+01$ | $9.48 \mathrm{e}+00$ | $6.35 \mathrm{e}+00$ |
| 14 |  | $0.00 \mathrm{e}+00$ | $9.25 \mathrm{e}+00$ | $5.20 \mathrm{e}+00$ | $3.64 \mathrm{e}+00$ | $3.21 \mathrm{e}+00$ | $1.59 \mathrm{e}-06$ | $8.64 \mathrm{e}-06$ | $2.93 \mathrm{e}-06$ | $3.49 \mathrm{e}-06$ | $1.59 \mathrm{e}-06$ |
| 15 |  | $6.49 \mathrm{e}-07$ | $1.69 \mathrm{e}-06$ | $1.27 \mathrm{e}-06$ | $1.19 \mathrm{e}-06$ | $3.13 \mathrm{e}-07$ | $4.14 \mathrm{e}-01$ | $5.65 \mathrm{e}-01$ | $4.90 \mathrm{e}-01$ | $4.83 \mathrm{e}-01$ | $2.52 \mathrm{e}-02$ |
| 16 |  | $5.76 \mathrm{e}-03$ | $5.00 \mathrm{e}-01$ | $4.99 \mathrm{e}-01$ | $3.89 \mathrm{e}-01$ | $1.74 \mathrm{e}-01$ | $8.93 \mathrm{e}-01$ | $5.80 \mathrm{e}+02$ | $2.07 \mathrm{e}+00$ | $6.41 \mathrm{e}+01$ | $1.49 \mathrm{e}+02$ |
| 17 |  | $4.37 \mathrm{e}-01$ | $2.30 \mathrm{e}+00$ | $7.17 \mathrm{e}-01$ | $8.79 \mathrm{e}-01$ | $4.52 \mathrm{e}-01$ | $7.86 \mathrm{e}-01$ | $2.66 \mathrm{e}+01$ | $2.10 \mathrm{e}+01$ | $2.02 \mathrm{e}+01$ | $4.93 \mathrm{e}+00$ |
| 18 |  | $4.03 \mathrm{e}-01$ | $2.17 \mathrm{e}+01$ | $1.84 \mathrm{e}+00$ | $8.65 \mathrm{e}+00$ | $9.83 \mathrm{e}+00$ | $5.00 \mathrm{e}-01$ | $2.05 \mathrm{e}+01$ | $2.05 \mathrm{e}+01$ | $1.73 \mathrm{e}+01$ | $7.32 \mathrm{e}+00$ |
| 19 |  | $2.93 \mathrm{e}-01$ | $5.00 \mathrm{e}-01$ | $5.00 \mathrm{e}-01$ | $4.73 \mathrm{e}-01$ | $6.96 \mathrm{e}-02$ | $5.09 \mathrm{e}-02$ | $2.95 \mathrm{e}+00$ | $1.14 \mathrm{e}+00$ | $1.24 \mathrm{e}+00$ | $7.24 \mathrm{e}-01$ |
| 20 |  | $0.00 \mathrm{e}+00$ | $1.94 \mathrm{e}-02$ | $1.94 \mathrm{e}-02$ | $1.82 \mathrm{e}-02$ | $4.85 \mathrm{e}-03$ | $1.54 \mathrm{e}-03$ | $2.07 \mathrm{e}+01$ | $2.21 \mathrm{e}-01$ | $1.47 \mathrm{e}+00$ | $4.78 \mathrm{e}+00$ |
| 21 | Composition functions | $5.66 \mathrm{e}-05$ | $2.50 \mathrm{e}+01$ | $4.68 \mathrm{e}-01$ | $3.32 \mathrm{e}+00$ | $7.56 \mathrm{e}+00$ | $2.00 \mathrm{e}+02$ | $2.03 \mathrm{e}+02$ | $2.00 \mathrm{e}+02$ | $2.01 \mathrm{e}+02$ | $1.10 \mathrm{e}+00$ |
| 22 |  | $1.00 \mathrm{e}+02$ | $2.03 \mathrm{e}+02$ | $2.00 \mathrm{e}+02$ | $1.93 \mathrm{e}+02$ | $2.52 \mathrm{e}+01$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $3.72 \mathrm{e}-13$ |
| 23 |  | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $8.61 \mathrm{e}-02$ | $3.00 \mathrm{e}+02$ | $3.39 \mathrm{e}+02$ | $3.26 \mathrm{e}+02$ | $3.25 \mathrm{e}+02$ | $1.05 \mathrm{e}+01$ |
| 24 |  | $3.00 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $0.00 \mathrm{e}+00$ | $3.50 \mathrm{e}+02$ | $4.11 \mathrm{e}+02$ | $3.99 \mathrm{e}+02$ | $3.94 \mathrm{e}+02$ | $1.36 \mathrm{e}+01$ |
| 25 |  | $2.68 \mathrm{e}+02$ | $3.28 \mathrm{e}+02$ | $3.11 \mathrm{e}+02$ | $3.11 \mathrm{e}+02$ | $1.72 \mathrm{e}+01$ | $3.87 \mathrm{e}+02$ | $3.87 \mathrm{e}+02$ | $3.87 \mathrm{e}+02$ | $3.87 \mathrm{e}+02$ | $6.85 \mathrm{e}-03$ |
| 26 |  | $3.98 \mathrm{e}+02$ | $4.43 \mathrm{e}+02$ | $3.98 \mathrm{e}+02$ | $4.18 \mathrm{e}+02$ | $2.33 \mathrm{e}+01$ | $2.00 \mathrm{e}+02$ | $7.56 \mathrm{e}+02$ | $4.00 \mathrm{e}+02$ | $4.36 \mathrm{e}+02$ | $1.08 \mathrm{e}+02$ |
| 27 |  | $3.00 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $0.00 \mathrm{e}+00$ | $4.62 \mathrm{e}+02$ | $5.00 \mathrm{e}+02$ | $4.75 \mathrm{e}+02$ | $4.75 \mathrm{e}+02$ | $8.90 \mathrm{e}+00$ |
| 28 |  | $3.90 \mathrm{e}+02$ | $3.95 \mathrm{e}+02$ | $3.94 \mathrm{e}+02$ | $3.94 \mathrm{e}+02$ | $1.14 \mathrm{e}+00$ | $3.00 \mathrm{e}+02$ | $4.14 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $3.17 \mathrm{e}+02$ | $3.63 \mathrm{e}+01$ |
| 29 |  | $3.00 \mathrm{e}+02$ | $6.12 \mathrm{e}+02$ | $3.00 \mathrm{e}+02$ | $3.92 \mathrm{e}+02$ | $1.41 \mathrm{e}+02$ | $4.02 \mathrm{e}+02$ | $4.24 \mathrm{e}+02$ | $4.10 \mathrm{e}+02$ | $4.10 \mathrm{e}+02$ | $5.15 \mathrm{e}+00$ |
| 30 |  | $2.26 \mathrm{e}+02$ | $2.34 \mathrm{e}+02$ | $2.29 \mathrm{e}+02$ | $2.29 \mathrm{e}+02$ | $2.35 \mathrm{e}+00$ | $1.95 \mathrm{e}+03$ | $1.99 \mathrm{e}+03$ | $1.98 \mathrm{e}+03$ | $1.98 \mathrm{e}+03$ | $1.13 \mathrm{e}+01$ |

| No | Types | Dimensionality $=50$ |  |  |  |  | Dimensionality $=100$ |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Best | Worst | Median | Mean | SD | Best | Worst | Median | Mean | SD |
| 01 | Unimodal functions | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $1.11 \mathrm{e}-02$ | $1.99 \mathrm{e}-02$ | $1.48 \mathrm{e}-02$ | $1.51 \mathrm{e}-02$ | $1.90 \mathrm{e}-03$ |
| 03 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $3.97 \mathrm{e}-07$ | $2.17 \mathrm{e}-06$ | $8.75 \mathrm{e}-07$ | $9.23 \mathrm{e}-07$ | $3.39 \mathrm{e}-07$ |
| 04 | Multimodal functions | $1.95 \mathrm{e}+01$ | $1.46 \mathrm{e}+02$ | $2.86 \mathrm{e}+01$ | $4.71 \mathrm{e}+01$ | $3.56 \mathrm{e}+01$ | $1.52 \mathrm{e}+02$ | $2.50 \mathrm{e}+02$ | $2.00 \mathrm{e}+02$ | $2.08 \mathrm{e}+02$ | $2.12 \mathrm{e}+01$ |
| 05 |  | $2.84 \mathrm{e}-06$ | $6.96 \mathrm{e}+00$ | $2.98 \mathrm{e}+00$ | $3.10 \mathrm{e}+00$ | $1.72 \mathrm{e}+00$ | $1.20 \mathrm{e}+01$ | $2.49 \mathrm{e}+01$ | $1.69 \mathrm{e}+01$ | $1.71 \mathrm{e}+01$ | $3.25 \mathrm{e}+00$ |
| 06 |  | $1.20 \mathrm{e}-06$ | $2.71 \mathrm{e}-05$ | $1.05 \mathrm{e}-05$ | $1.23 \mathrm{e}-05$ | $1.04 \mathrm{e}-05$ | $2.27 \mathrm{e}-02$ | $6.82 \mathrm{e}-02$ | $3.63 \mathrm{e}-02$ | $3.85 \mathrm{e}-02$ | $1.02 \mathrm{e}-02$ |
| 07 |  | $5.41 \mathrm{e}+01$ | $6.05 \mathrm{e}+01$ | $5.65 \mathrm{e}+01$ | $5.65 \mathrm{e}+01$ | $1.21 \mathrm{e}+00$ | $1.09 \mathrm{e}+02$ | $1.17 \mathrm{e}+02$ | $1.12 \mathrm{e}+02$ | $1.12 \mathrm{e}+02$ | $1.65 \mathrm{e}+00$ |
| 08 |  | $9.50 \mathrm{e}-07$ | $7.96 \mathrm{e}+00$ | $2.98 \mathrm{e}+00$ | $3.14 \mathrm{e}+00$ | $1.98 \mathrm{e}+00$ | $1.06 \mathrm{e}+01$ | $2.82 \mathrm{e}+01$ | $1.52 \mathrm{e}+01$ | $1.64 \mathrm{e}+01$ | $3.73 \mathrm{e}+00$ |
| 09 |  | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $0.00 \mathrm{e}+00$ | $6.38 \mathrm{e}-07$ | $1.27 \mathrm{e}-06$ | $9.14 \mathrm{e}-07$ | $9.27 \mathrm{e}-07$ | $1.39 \mathrm{e}-07$ |
| 10 |  | $1.23 \mathrm{e}+02$ | $4.70 \mathrm{e}+02$ | $1.31 \mathrm{e}+02$ | $1.49 \mathrm{e}+02$ | $6.46 \mathrm{e}+01$ | $7.79 \mathrm{e}+02$ | $6.60 \mathrm{e}+03$ | $2.15 \mathrm{e}+03$ | $2.49 \mathrm{e}+03$ | $1.39 \mathrm{e}+03$ |
| 11 | Hybrid function | $1.83 \mathrm{e}+01$ | $1.93 \mathrm{e}+01$ | $1.83 \mathrm{e}+01$ | $1.83 \mathrm{e}+01$ | $2.70 \mathrm{e}-01$ | $4.54 \mathrm{e}+00$ | $8.40 \mathrm{e}+01$ | $1.47 \mathrm{e}+01$ | $1.99 \mathrm{e}+01$ | $1.64 \mathrm{e}+01$ |
| 12 |  | $2.50 \mathrm{e}-01$ | $1.38 \mathrm{e}+02$ | $1.69 \mathrm{e}+00$ | $1.12 \mathrm{e}+01$ | $3.05 \mathrm{e}+01$ | $1.30 \mathrm{e}+02$ | $5.75 \mathrm{e}+02$ | $3.08 \mathrm{e}+02$ | $3.15 \mathrm{e}+02$ | $9.91 \mathrm{e}+01$ |
| 13 |  | $2.59 \mathrm{e}-05$ | $8.84 \mathrm{e}+00$ | $1.64 \mathrm{e}+00$ | $2.40 \mathrm{e}+00$ | $2.51 \mathrm{e}+00$ | $1.06 \mathrm{e}+01$ | $4.13 \mathrm{e}+01$ | $1.76 \mathrm{e}+01$ | $2.41 \mathrm{e}+01$ | $1.17 \mathrm{e}+01$ |
| 14 |  | $4.37 \mathrm{e}-04$ | $2.06 \mathrm{e}+01$ | $2.00 \mathrm{e}+01$ | $1.89 \mathrm{e}+01$ | $4.78 \mathrm{e}+00$ | $2.00 \mathrm{e}+01$ | $2.18 \mathrm{e}+01$ | $2.04 \mathrm{e}+01$ | $2.05 \mathrm{e}+01$ | $3.96 \mathrm{e}-01$ |
| 15 |  | $1.71 \mathrm{e}+01$ | $1.82 \mathrm{e}+01$ | $1.72 \mathrm{e}+01$ | $1.72 \mathrm{e}+01$ | $1.40 \mathrm{e}-01$ | $7.90 \mathrm{e}+00$ | $8.14 \mathrm{e}+01$ | $1.52 \mathrm{e}+01$ | $2.57 \mathrm{e}+01$ | $2.36 \mathrm{e}+01$ |
| 16 |  | $2.60 \mathrm{e}+00$ | $1.33 \mathrm{e}+03$ | $5.58 \mathrm{e}+00$ | $8.68 \mathrm{e}+01$ | $1.88 \mathrm{e}+02$ | $1.27 \mathrm{e}+01$ | $1.10 \mathrm{e}+02$ | $1.86 \mathrm{e}+01$ | $2.53 \mathrm{e}+01$ | $1.97 \mathrm{e}+01$ |
| 17 |  | $2.31 \mathrm{e}+01$ | $7.20 \mathrm{e}+02$ | $2.63 \mathrm{e}+01$ | $6.54 \mathrm{e}+01$ | $1.57 \mathrm{e}+02$ | $4.82 \mathrm{e}+01$ | $2.65 \mathrm{e}+03$ | $1.04 \mathrm{e}+02$ | $3.28 \mathrm{e}+02$ | $6.88 \mathrm{e}+02$ |
| 18 |  | $2.05 \mathrm{e}+01$ | $2.10 \mathrm{e}+01$ | $2.05 \mathrm{e}+01$ | $2.06 \mathrm{e}+01$ | $1.14 \mathrm{e}-01$ | $1.49 \mathrm{e}+00$ | $2.26 \mathrm{e}+01$ | $2.10 \mathrm{e}+01$ | $1.44 \mathrm{e}+01$ | $8.33 \mathrm{e}+00$ |
| 19 |  | $1.57 \mathrm{e}+00$ | $6.10 \mathrm{e}+00$ | $3.60 \mathrm{e}+00$ | $3.61 \mathrm{e}+00$ | $7.11 \mathrm{e}-01$ | $9.93 \mathrm{e}+00$ | $1.38 \mathrm{e}+01$ | $1.14 \mathrm{e}+01$ | $1.14 \mathrm{e}+01$ | $7.48 \mathrm{e}-01$ |
| 20 |  | $2.07 \mathrm{e}+01$ | $7.93 \mathrm{e}+02$ | $2.11 \mathrm{e}+01$ | $3.67 \mathrm{e}+01$ | $1.08 \mathrm{e}+02$ | $9.67 \mathrm{e}+01$ | $2.93 \mathrm{e}+03$ | $2.52 \mathrm{e}+02$ | $7.34 \mathrm{e}+02$ | $9.53 \mathrm{e}+02$ |
| 21 | Composition functions | $2.00 \mathrm{e}+02$ | $2.08 \mathrm{e}+02$ | $2.03 \mathrm{e}+02$ | $2.03 \mathrm{e}+02$ | $1.99 \mathrm{e}+00$ | $2.25 \mathrm{e}+02$ | $2.46 \mathrm{e}+02$ | $2.38 \mathrm{e}+02$ | $2.37 \mathrm{e}+02$ | $4.70 \mathrm{e}+00$ |
| 22 |  | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $1.00 \mathrm{e}+02$ | $3.12 \mathrm{e}-08$ | $1.00 \mathrm{e}+02$ | $5.28 \mathrm{e}+03$ | $1.82 \mathrm{e}+03$ | $1.78 \mathrm{e}+03$ | $1.53 \mathrm{e}+03$ |
| 23 |  | $3.80 \mathrm{e}+02$ | $4.07 \mathrm{e}+02$ | $3.90 \mathrm{e}+02$ | $3.91 \mathrm{e}+02$ | $4.26 \mathrm{e}+00$ | $5.19 \mathrm{e}+02$ | $6.05 \mathrm{e}+02$ | $5.42 \mathrm{e}+02$ | $5.46 \mathrm{e}+02$ | $1.51 \mathrm{e}+01$ |
| 24 |  | $4.18 \mathrm{e}+02$ | $4.79 \mathrm{e}+02$ | $4.65 \mathrm{e}+02$ | $4.62 \mathrm{e}+02$ | $1.21 \mathrm{e}+01$ | $7.08 \mathrm{e}+02$ | $8.11 \mathrm{e}+02$ | $7.83 \mathrm{e}+02$ | $7.80 \mathrm{e}+02$ | $1.90 \mathrm{e}+01$ |
| 25 |  | $4.58 \mathrm{e}+02$ | $5.63 \mathrm{e}+02$ | $4.80 \mathrm{e}+02$ | $4.87 \mathrm{e}+02$ | $2.67 \mathrm{e}+01$ | $5.77 \mathrm{e}+02$ | $7.14 \mathrm{e}+02$ | $6.37 \mathrm{e}+02$ | $6.46 \mathrm{e}+02$ | $3.51 \mathrm{e}+01$ |
| 26 |  | $4.00 \mathrm{e}+02$ | $6.16 \mathrm{e}+02$ | $4.00 \mathrm{e}+02$ | $4.16 \mathrm{e}+02$ | $5.41 \mathrm{e}+01$ | $1.29 \mathrm{e}+03$ | $2.40 \mathrm{e}+03$ | $1.95 \mathrm{e}+03$ | $1.95 \mathrm{e}+03$ | $2.10 \mathrm{e}+02$ |
| 27 |  | $4.59 \mathrm{e}+02$ | $5.04 \mathrm{e}+02$ | $4.77 \mathrm{e}+02$ | $4.79 \mathrm{e}+02$ | $1.61 \mathrm{e}+01$ | $5.07 \mathrm{e}+02$ | $5.40 \mathrm{e}+02$ | $5.30 \mathrm{e}+02$ | $5.28 \mathrm{e}+02$ | $7.22 \mathrm{e}+00$ |
| 28 |  | $4.59 \mathrm{e}+02$ | $4.59 \mathrm{e}+02$ | $4.59 \mathrm{e}+02$ | $4.59 \mathrm{e}+02$ | $5.05 \mathrm{e}-13$ | $4.78 \mathrm{e}+02$ | $5.60 \mathrm{e}+02$ | $5.20 \mathrm{e}+02$ | $5.22 \mathrm{e}+02$ | $2.22 \mathrm{e}+01$ |
| 29 |  | $2.90 \mathrm{e}+02$ | $3.19 \mathrm{e}+02$ | $3.01 \mathrm{e}+02$ | $3.02 \mathrm{e}+02$ | $6.09 \mathrm{e}+00$ | $6.38 \mathrm{e}+02$ | $8.73 \mathrm{e}+02$ | $7.74 \mathrm{e}+02$ | $7.56 \mathrm{e}+02$ | $5.80 \mathrm{e}+01$ |
| 30 |  | $6.94 \mathrm{e}+05$ | $8.76 \mathrm{e}+05$ | $7.66 \mathrm{e}+05$ | $7.71 \mathrm{e}+05$ | $4.34 \mathrm{e}+04$ | $2.29 \mathrm{e}+03$ | $2.45 \mathrm{e}+03$ | $2.35 \mathrm{e}+03$ | $2.35 \mathrm{e}+03$ | $3.99 \mathrm{e}+01$ |

D. Comparison of the computational costs of the six algorithms in the CEC 2014 10-D, 30-D, 50-D and 100-D tests (second).

| No. | $\mathrm{E}_{3}$-EDA |  |  |  | LSHADE-EpSin |  |  |  | UMOEAsII |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 10D | 30D | 50D | 100D | 10D | 30D | 50D | 100D | 10D | 30D | 50D | 100D |
| 01 | 0.38 | 2.32 | 6.83 | 44.80 | 0.61 | 3.95 | 8.70 | 47.60 | 0.99 | 2.91 | 7.62 | 45.40 |
| 02 | 0.32 | 1.74 | 5.21 | 38.30 | 0.57 | 3.44 | 7.44 | 42.50 | 0.80 | 2.43 | 4.94 | 39.70 |
| 03 | 0.32 | 1.79 | 5.13 | 37.80 | 0.52 | 3.45 | 7.55 | 42.30 | 0.81 | 2.60 | 4.95 | 38.50 |
| 04 | 0.34 | 1.80 | 5.23 | 37.70 | 0.52 | 3.59 | 7.44 | 39.90 | 0.73 | 2.37 | 5.07 | 36.30 |
| 05 | 0.37 | 2.11 | 6.05 | 40.40 | 0.87 | 4.19 | 8.39 | 43.80 | 0.84 | 2.73 | 5.22 | 42.10 |
| 06 | 3.30 | 28.32 | 77.04 | 333.90 | 4.83 | 16.51 | 42.77 | 377.60 | 4.91 | 16.64 | 42.41 | 354.00 |
| 07 | 0.36 | 2.23 | 6.21 | 42.00 | 0.70 | 3.47 | 7.48 | 44.10 | 0.78 | 2.85 | 5.64 | 42.20 |
| 08 | 0.35 | 1.85 | 4.21 | 21.40 | 0.56 | 3.35 | 7.11 | 24.40 | 0.69 | 2.13 | 3.91 | 18.70 |
| 09 | 0.36 | 2.24 | 6.06 | 40.40 | 0.84 | 4.19 | 8.65 | 42.70 | 0.69 | 2.37 | 5.09 | 41.00 |
| 10 | 0.40 | 1.98 | 4.91 | 23.90 | 0.76 | 4.61 | 9.58 | 30.70 | 0.91 | 3.35 | 6.80 | 28.80 |
| 11 | 0.39 | 2.34 | 6.76 | 43.10 | 0.93 | 4.95 | 10.70 | 41.50 | 1.00 | 3.49 | 7.45 | 43.00 |
| 12 | 1.13 | 8.87 | 24.33 | 115.20 | 2.17 | 6.95 | 15.72 | 125.40 | 2.31 | 5.51 | 13.15 | 119.30 |
| 13 | 0.32 | 1.77 | 4.97 | 36.40 | 0.77 | 3.87 | 7.64 | 31.90 | 0.79 | 2.31 | 4.86 | 28.80 |
| 14 | 0.32 | 1.75 | 4.93 | 36.50 | 0.81 | 3.98 | 7.70 | 37.30 | 0.81 | 2.33 | 4.92 | 33.00 |
| 15 | 0.36 | 2.29 | 6.21 | 42.20 | 0.83 | 4.06 | 8.15 | 43.70 | 0.79 | 2.54 | 5.45 | 42.40 |
| 16 | 0.37 | 2.27 | 6.17 | 41.70 | 0.85 | 4.26 | 8.28 | 45.10 | 0.80 | 3.55 | 7.06 | 42.90 |
| 17 | 0.36 | 2.34 | 6.56 | 37.60 | 0.66 | 4.04 | 8.86 | 37.60 | 1.36 | 3.29 | 6.65 | 36.80 |
| 18 | 0.36 | 1.92 | 5.55 | 39.50 | 0.82 | 3.83 | 8.07 | 43.40 | 0.88 | 2.43 | 4.96 | 38.50 |
| 19 | 0.96 | 7.36 | 20.44 | 99.90 | 1.18 | 6.98 | 15.82 | 105.60 | 1.41 | 5.60 | 14.01 | 101.10 |
| 20 | 0.37 | 2.10 | 5.77 | 40.40 | 0.82 | 3.72 | 7.96 | 33.20 | 1.02 | 2.60 | 5.23 | 28.70 |
| 21 | 0.37 | 2.20 | 6.07 | 32.00 | 0.85 | 3.93 | 8.57 | 35.70 | 0.91 | 2.74 | 5.83 | 32.00 |
| 22 | 0.48 | 2.94 | 8.02 | 47.10 | 0.90 | 4.53 | 9.67 | 48.40 | 0.93 | 2.97 | 6.55 | 47.90 |
| 23 | 0.49 | 4.26 | 14.36 | 104.60 | 0.99 | 7.68 | 20.49 | 105.20 | 1.35 | 6.76 | 18.10 | 100.90 |
| 24 | 0.47 | 3.45 | 9.68 | 68.70 | 1.17 | 6.07 | 15.01 | 70.00 | 1.08 | 5.11 | 12.77 | 66.10 |
| 25 | 0.52 | 4.26 | 13.30 | 84.60 | 1.15 | 6.73 | 17.61 | 87.50 | 1.15 | 5.79 | 15.14 | 86.50 |
| 26 | 3.91 | 31.70 | 89.25 | 436.40 | 4.75 | 23.33 | 62.89 | 480.20 | 5.04 | 22.20 | 60.19 | 454.10 |
| 27 | 3.74 | 31.66 | 89.20 | 436.40 | 4.86 | 21.03 | 57.93 | 472.40 | 5.04 | 20.95 | 57.88 | 450.40 |
| 28 | 0.63 | 5.46 | 18.33 | 138.30 | 1.09 | 8.90 | 23.44 | 143.30 | 1.39 | 7.58 | 20.92 | 139.10 |
| 29 | 1.09 | 8.92 | 26.10 | 145.80 | 1.20 | 9.20 | 23.74 | 156.50 | 1.65 | 9.11 | 23.19 | 149.90 |
| 30 | 0.57 | 4.33 | 13.51 | 88.90 | 0.98 | 7.08 | 17.03 | 87.60 | 1.29 | 6.75 | 16.18 | 86.60 |

|  | L-SHADE |  |  |  | MLS-EDA |  |  |  | ACSEDA |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 10D | 30D | 50D | 100D | 10D | 30D | 50D | 100D | 10D | 30D | 50D | 100D |
| 01 | 0.38 | 2.13 | 5.97 | 35.60 | 0.54 | 2.22 | 6.66 | 39.66 | 0.31 | 1.48 | 3.95 | 21.35 |
| 02 | 0.30 | 1.51 | 4.30 | 28.60 | 0.49 | 1.65 | 5.05 | 33.02 | 0.25 | 0.90 | 2.22 | 14.49 |
| 03 | 0.30 | 1.50 | 4.28 | 28.50 | 0.52 | 1.62 | 4.96 | 32.98 | 0.25 | 0.90 | 2.23 | 14.48 |
| 04 | 0.31 | 1.52 | 4.35 | 28.40 | 0.55 | 1.63 | 5.36 | 33.00 | 0.26 | 0.94 | 2.32 | 14.80 |
| 05 | 0.36 | 1.90 | 5.33 | 32.60 | 0.63 | 2.05 | 6.25 | 37.04 | 0.28 | 1.36 | 3.29 | 18.50 |
| 06 | 3.35 | 27.86 | 76.19 | 325.50 | 4.42 | 27.48 | 78.69 | 326.44 | 2.71 | 28.74 | 79.11 | 322.14 |
| 07 | 0.36 | 1.95 | 5.38 | 32.90 | 0.62 | 2.01 | 6.09 | 37.49 | 0.27 | 1.26 | 3.33 | 18.87 |
| 08 | 0.33 | 1.49 | 3.41 | 12.50 | 0.58 | 1.69 | 4.41 | 18.09 | 0.27 | 1.06 | 2.20 | 9.17 |
| 09 | 0.35 | 1.86 | 5.22 | 32.10 | 0.59 | 2.07 | 6.17 | 36.72 | 0.29 | 1.25 | 3.16 | 18.18 |
| 10 | 0.37 | 1.76 | 4.20 | 16.40 | 0.63 | 1.95 | 5.00 | 21.05 | 0.38 | 1.30 | 2.90 | 12.03 |
| 11 | 0.38 | 2.16 | 6.01 | 36.30 | 0.65 | 2.36 | 6.85 | 40.06 | 0.39 | 1.50 | 3.90 | 21.15 |
| 12 | 1.14 | 8.60 | 23.57 | 107.80 | 1.56 | 8.62 | 24.79 | 111.19 | 0.87 | 8.56 | 23.37 | 99.35 |
| 13 | 0.31 | 1.54 | 4.38 | 28.50 | 0.51 | 1.70 | 5.19 | 32.94 | 0.26 | 0.91 | 2.30 | 14.73 |
| 14 | 0.31 | 1.51 | 4.29 | 28.30 | 0.49 | 1.67 | 5.03 | 32.94 | 0.27 | 0.91 | 2.22 | 14.59 |
| 15 | 0.35 | 1.92 | 5.38 | 32.80 | 0.53 | 2.11 | 6.36 | 37.18 | 0.28 | 1.28 | 3.25 | 18.53 |
| 16 | 0.35 | 1.92 | 5.38 | 33.00 | 0.53 | 2.13 | 6.29 | 37.75 | 0.31 | 1.33 | 3.35 | 18.84 |
| 17 | 0.35 | 2.04 | 5.71 | 34.30 | 0.44 | 2.28 | 7.03 | 38.88 | 0.34 | 1.42 | 3.69 | 20.24 |
| 18 | 0.33 | 1.70 | 4.72 | 30.20 | 0.51 | 1.89 | 5.76 | 34.68 | 0.31 | 1.10 | 2.64 | 16.12 |
| 19 | 0.96 | 7.10 | 19.39 | 90.50 | 1.05 | 7.38 | 20.78 | 94.37 | 0.93 | 6.69 | 18.30 | 78.59 |
| 20 | 0.34 | 1.77 | 4.95 | 31.00 | 0.89 | 2.03 | 5.91 | 35.58 | 0.33 | 1.14 | 2.86 | 16.98 |
| 21 | 0.35 | 1.87 | 5.28 | 32.50 | 0.98 | 2.12 | 6.24 | 37.09 | 0.34 | 1.25 | 3.19 | 18.41 |
| 22 | 0.50 | 2.68 | 7.27 | 40.60 | 0.50 | 2.85 | 8.18 | 44.84 | 0.40 | 2.05 | 5.34 | 26.66 |
| 23 | 0.49 | 4.12 | 13.76 | 103.40 | 0.54 | 5.68 | 26.42 | 105.82 | 0.94 | 2.92 | 9.10 | 57.32 |
| 24 | 0.47 | 3.07 | 9.07 | 59.90 | 0.51 | 3.34 | 18.17 | 63.43 | 0.78 | 2.11 | 6.01 | 34.69 |
| 25 | 0.53 | 4.05 | 12.57 | 86.20 | 0.57 | 5.76 | 13.57 | 90.02 | 0.85 | 2.97 | 8.78 | 50.95 |
| 26 | 3.69 | 31.56 | 89.11 | 428.00 | 3.73 | 30.95 | 91.59 | 422.90 | 3.46 | 31.36 | 89.02 | 379.73 |
| 27 | 3.66 | 31.49 | 88.65 | 426.00 | 3.70 | 36.60 | 91.24 | 423.69 | 3.28 | 31.12 | 87.53 | 377.60 |
| 28 | 0.62 | 5.33 | 17.83 | 131.30 | 0.67 | 8.09 | 19.36 | 133.68 | 0.99 | 3.90 | 12.07 | 74.58 |
| 29 | 1.08 | 8.77 | 25.43 | 139.00 | 1.21 | 8.67 | 26.83 | 141.40 | 1.30 | 7.92 | 22.49 | 105.23 |
| 30 | 0.56 | 4.22 | 12.88 | 87.60 | 0.60 | 4.32 | 13.92 | 90.64 | 0.58 | 3.15 | 9.16 | 52.14 |

E. Comparison of the computational costs of the six algorithms in the CEC 2018 10-D, 30-D, 50-D and 100-D tests (second).

| No. | $\mathrm{E}_{3}$-EDA |  |  |  | HSES |  |  |  | LSHADE-RSP |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 10D | 30D | 50D | 100D | 10D | 30D | 50D | 100D | 10D | 30D | 50D | 100D |
| 01 | 0.30 | 1.73 | 5.29 | 41.15 | 0.41 | 2.27 | 10.14 | 71.04 | - | - | - | - |
| 03 | 0.28 | 1.68 | 5.16 | 41.69 | 0.41 | 2.31 | 9.94 | 72.02 | - | - | - | - |
| 04 | 0.30 | 1.88 | 5.24 | 40.70 | 0.41 | 2.30 | 10.13 | 72.14 | - | - | - | - |
| 05 | 0.34 | 2.10 | 6.14 | 43.23 | 0.44 | 2.59 | 11.18 | 74.77 | - | - | - | - |
| 06 | 0.44 | 3.12 | 9.18 | 55.85 | 0.55 | 3.58 | 14.89 | 87.65 | - | - | - | - |
| 07 | 0.35 | 2.11 | 6.26 | 43.61 | 0.46 | 2.66 | 11.34 | 76.16 | - | - | - | - |
| 08 | 0.35 | 2.13 | 6.31 | 45.04 | 0.46 | 2.77 | 11.40 | 74.33 | - | - | - | - |
| 09 | 0.33 | 2.07 | 6.30 | 44.75 | 0.47 | 2.76 | 11.47 | 76.75 | - | - | - | - |
| 10 | 0.38 | 2.33 | 6.97 | 47.19 | 0.47 | 2.87 | 12.13 | 78.69 | - | - | - | - |
| 11 | 0.34 | 1.94 | 5.75 | 41.54 | 0.45 | 2.55 | 10.54 | 70.25 | - | - | - | - |
| 12 | 0.33 | 2.13 | 6.26 | 43.77 | 0.45 | 2.64 | 11.30 | 73.21 | - | - | - | - |
| 13 | 0.33 | 1.93 | 5.73 | 42.19 | 0.45 | 2.52 | 10.69 | 70.73 | - | - | - | - |
| 14 | 0.43 | 2.47 | 6.92 | 47.34 | 0.55 | 2.90 | 12.21 | 76.48 | - | - | - | - |
| 15 | 0.34 | 1.88 | 5.58 | 41.26 | 0.44 | 2.46 | 10.35 | 70.24 | - | - | - | - |
| 16 | 0.36 | 2.05 | 5.95 | 42.73 | 0.48 | 2.60 | 11.14 | 71.99 | - | - | - | - |
| 17 | 0.48 | 2.89 | 8.32 | 52.18 | 0.89 | 3.48 | 14.26 | 85.76 | - | - | - | - |
| 18 | 0.34 | 2.02 | 6.05 | 43.00 | 0.48 | 2.58 | 10.93 | 72.32 | - | - | - | - |
| 19 | 0.98 | 7.36 | 20.72 | 102.94 | 1.08 | 8.06 | 30.81 | 155.11 | - | - | - | - |
| 20 | 0.49 | 3.08 | 8.74 | 53.03 | 0.80 | 3.53 | 14.94 | 88.25 | - | - | - | - |
| 21 | 0.44 | 3.55 | 11.78 | 90.91 | 0.60 | 4.13 | 18.92 | 136.82 | - | - | - | - |
| 22 | 0.50 | 3.94 | 12.87 | 94.99 | 0.64 | 4.61 | 20.41 | 141.53 | - | - | - | - |
| 23 | 0.53 | 4.33 | 14.67 | 114.75 | 0.66 | 5.00 | 22.98 | 166.70 | - | - | - | - |
| 24 | 0.55 | 4.82 | 15.86 | 118.42 | 0.69 | 5.38 | 24.68 | 171.51 | - | - | - | - |
| 25 | 0.47 | 4.11 | 15.03 | 125.55 | 0.62 | 4.87 | 24.49 | 183.67 | - | - | - | - |
| 26 | 0.58 | 5.18 | 17.85 | 138.82 | 0.72 | 5.90 | 27.17 | 195.65 | - | - | - | - |
| 27 | 0.59 | 5.75 | 20.35 | 160.56 | 0.74 | 6.52 | 31.29 | 223.77 | - | - | - | - |
| 28 | 0.56 | 5.05 | 18.15 | 151.42 | 0.68 | 5.79 | 27.84 | 214.93 | - | - | - | - |
| 29 | 0.57 | 4.15 | 13.37 | 95.57 | 0.70 | 4.87 | 21.32 | 145.99 | - | - | - | - |
| 30 | 1.10 | 8.58 | 28.98 | 145.20 | 1.22 | 9.46 | 37.59 | 210.44 | - | - | - | - |

| No. | ELSHADE-SPACMA |  |  |  | EBOwithCMAR |  |  |  | ACSEDA |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 10D | 30D | 50D | 100D | 10D | 30D | 50D | 100D | 10D | 30D | 50D | 100D |
| 01 | 0.58 | 1.97 | 7.01 | 35.42 | 1.20 | 4.23 | 8.79 | 59.61 | 0.10 | 0.88 | 3.26 | 24.92 |
| 03 | 0.55 | 1.98 | 6.48 | 34.50 | 1.12 | 4.26 | 9.55 | 58.77 | 0.10 | 0.87 | 3.24 | 24.90 |
| 04 | 0.51 | 1.73 | 6.45 | 33.64 | 1.14 | 4.28 | 10.30 | 58.81 | 0.10 | 0.90 | 3.34 | 25.39 |
| 05 | 0.56 | 2.33 | 7.94 | 37.99 | 1.20 | 4.63 | 11.06 | 61.14 | 0.12 | 1.21 | 4.21 | 28.85 |
| 06 | 0.68 | 3.38 | 12.01 | 50.94 | 1.27 | 5.63 | 12.80 | 73.89 | 0.24 | 2.26 | 7.07 | 41.21 |
| 07 | 0.57 | 2.33 | 7.77 | 39.58 | 1.27 | 4.53 | 11.04 | 60.97 | 0.13 | 1.25 | 4.22 | 28.77 |
| 08 | 0.54 | 2.35 | 7.89 | 38.40 | 1.21 | 4.67 | 11.17 | 61.22 | 0.13 | 1.28 | 4.25 | 29.88 |
| 09 | 0.57 | 2.35 | 8.01 | 38.35 | 1.20 | 4.67 | 5.22 | 64.07 | 0.13 | 1.26 | 5.80 | 29.58 |
| 10 | 0.59 | 2.62 | 8.76 | 41.40 | 1.31 | 5.23 | 12.47 | 63.94 | 0.16 | 1.51 | 4.84 | 32.34 |
| 11 | 0.52 | 2.01 | 6.64 | 35.48 | 1.16 | 4.37 | 10.76 | 59.66 | 0.12 | 1.08 | 3.61 | 27.03 |
| 12 | 0.51 | 2.32 | 7.71 | 38.10 | 1.15 | 4.63 | 11.71 | 61.80 | 0.12 | 1.23 | 4.15 | 28.80 |
| 13 | 0.52 | 2.23 | 6.86 | 36.10 | 1.17 | 4.40 | 11.11 | 60.66 | 0.12 | 1.10 | 3.66 | 26.29 |
| 14 | 0.50 | 2.39 | 8.22 | 41.70 | 1.22 | 4.82 | 12.00 | 64.45 | 0.15 | 1.50 | 4.77 | 31.16 |
| 15 | 0.49 | 2.07 | 6.73 | 35.28 | 1.16 | 4.38 | 10.58 | 58.12 | 0.12 | 1.18 | 3.53 | 25.67 |
| 16 | 0.52 | 2.21 | 7.23 | 36.13 | 1.20 | 4.70 | 11.11 | 60.15 | 0.12 | 1.37 | 3.95 | 27.46 |
| 17 | 0.62 | 3.18 | 10.15 | 46.14 | 1.34 | 5.60 | 14.02 | 69.85 | 0.23 | 2.29 | 6.46 | 37.24 |
| 18 | 0.50 | 2.18 | 7.09 | 37.47 | 1.16 | 4.57 | 11.19 | 59.62 | 0.12 | 1.33 | 3.86 | 27.42 |
| 19 | 1.19 | 7.81 | 25.61 | 97.55 | 1.82 | 10.33 | 27.03 | 121.35 | 0.76 | 7.11 | 19.47 | 89.71 |
| 20 | 0.60 | 3.31 | 10.67 | 48.56 | 1.29 | 5.87 | 14.33 | 73.50 | 0.24 | 2.45 | 6.90 | 39.20 |
| 21 | 0.68 | 3.71 | 14.22 | 83.29 | 1.30 | 6.12 | 17.10 | 106.88 | 0.24 | 2.88 | 9.72 | 73.61 |
| 22 | 0.76 | 4.23 | 15.86 | 89.36 | 1.39 | 6.67 | 18.58 | 110.74 | 0.31 | 3.30 | 10.76 | 79.01 |
| 23 | 0.74 | 4.64 | 17.89 | 107.28 | 1.46 | 7.21 | 20.44 | 130.93 | 0.32 | 3.68 | 12.65 | 96.80 |
| 24 | 0.78 | 4.93 | 19.11 | 112.07 | 1.48 | 7.33 | 21.43 | 134.92 | 0.34 | 4.05 | 13.64 | 101.47 |
| 25 | 0.72 | 4.36 | 18.23 | 120.05 | 1.33 | 6.74 | 20.60 | 144.93 | 0.29 | 3.52 | 12.92 | 109.98 |
| 26 | 0.83 | 5.44 | 21.77 | 131.86 | 1.42 | 7.93 | 23.38 | 155.69 | 0.37 | 4.50 | 15.66 | 121.02 |
| 27 | 0.82 | 6.00 | 24.96 | 154.15 | 1.43 | 8.69 | 25.96 | 177.79 | 0.40 | 5.18 | 18.39 | 142.92 |
| 28 | 0.79 | 5.33 | 22.33 | 146.38 | 1.40 | 7.77 | 23.78 | 169.44 | 0.35 | 4.43 | 16.10 | 135.82 |
| 29 | 0.77 | 4.48 | 17.30 | 92.09 | 1.41 | 7.01 | 19.21 | 114.39 | 0.35 | 3.63 | 11.49 | 82.80 |
| 30 | 1.28 | 9.00 | 33.03 | 142.61 | 1.94 | 11.68 | 31.88 | 164.93 | 0.88 | 8.46 | 24.44 | 133.07 |

## References

1. Larrañaga P, Lozano JA (2002) Estimation of distribution algorithms: a new tool for evolutionary computation
2. Wu C, Wang L, Wang J (2021) A path relinking enhanced estimation of distribution algorithm for direct acyclic graph task scheduling problem. Knowl Based Syst 228:107255. https://doi. org/10.1016/j.knosys.2021.107255
3. Wang Y, Li B (2008) A restart univariate estimation of distribution algorithm: Sampling under mixed Gaussian and Lévy probability distribution. In: 2008 IEEE congress on evolutionary computation, CEC 2008. IEEE, pp 3917-3924
4. De Bonet JS, Isbell CL, Viola P (1997) MIMIC: finding optima by estimating probability densities. In: Advances in neural information processing systems, pp 424-430
5. Yang Q, Chen WN, Li Y et al (2017) Multimodal estimation of distribution algorithms. IEEE Trans Cybern 47:636-650. https:// doi.org/10.1109/TCYB.2016.2523000
6. Srikamdee S, Chongstivatana P (2020) Collaborative learning of estimation of distribution algorithms for RNA secondary structure prediction. ECTI Trans Comput Inf Technol 14:92-102. https:// doi.org/10.37936/ecti-cit.2020141.239871
7. Pratap Chandran B, Immanuel Selvakumar A, Shine Let G, Paul Sathiyan S (2021) Optimal model parameter estimation of solar and fuel cells using improved estimation of distribution algorithm. Ain Shams Eng J 12:1693-1700. https://doi.org/10.1016/j.asej.2020. 07.034

8. Arenas ZG, Jimenez JC, Lozada-Chang LV, Santana R (2021) Estimation of distribution algorithms for the computation of innovation estimators of diffusion processes. Math Comput Simul 187:449-467. https://doi.org/10.1016/j.matcom.2021.03.017
9. Du Y, Li J, Luo C, Meng L (2021) A hybrid estimation of distribution algorithm for distributed flexible job shop scheduling with crane transportations. Swarm Evol Comput 62:100861. https://doi. org/10.1016/j.swevo.2021.100861
10. Shi W, Chen WN, Gu T et al (2021) Handling uncertainty in financial decision making: a clustering estimation of distribution algorithm with simplified simulation. IEEE Trans Emerg Top Comput Intell 5:42-56. https://doi.org/10.1109/TETCI.2020.3013652
11. Ren Z, Liang Y, Wang L et al (2018) Anisotropic adaptive variance scaling for Gaussian estimation of distribution algorithm. Knowl Based Syst 146:142-151. https://doi.org/10.1016/j.knosys. 2018.02.001
12. Liang Y, Ren Z, Yao X et al (2020) Enhancing Gaussian estimation of distribution algorithm by exploiting evolution direction with archive. IEEE Trans Cybern 50:140-152. https://doi.org/10.1109/ TCYB. 2018.2869567
13. Zhang G, Shi Y (2018) Hybrid sampling evolution strategy for solving single objective bound constrained problems. In: 2018 IEEE congress on evolutionary computation (CEC). IEEE, pp 1-7
14. Hadi AA, Mohamed AW, Jambi KM (2021) Single-objective realparameter optimization: enhanced LSHADE-SPACMA algorithm. In: Studies in computational intelligence, pp 103-121
15. Kumar A, Misra RK, Singh D (2017) Improving the local search capability of effective butterfly optimizer using covariance matrix adapted retreat phase. In: 2017 IEEE congress on evolutionary computation, CEC 2017—Proceedings. IEEE, pp 1835-1842
16. Elsayed S, Hamza N, Sarker R (2016) Testing united multi-operator evolutionary algorithms-II on single objective optimization problems. In: 2016 IEEE congress on evolutionary computation, CEC 2016. IEEE, pp 2966-2973
17. Awad NH, Ali MZ, Suganthan PN, Reynolds RG (2016) An ensemble sinusoidal parameter adaptation incorporated with L SHADE for solving CEC2014 benchmark problems. In: 2016 IEEE congress on evolutionary computation (CEC). IEEE, pp 2958-2965
18. Tanabe R, Fukunaga AS (2014) Improving the search performance of SHADE using linear population size reduction. In: Proceedings of the 2014 IEEE congress on evolutionary computation, CEC 2014, pp 1658-1665
19. Stanovov V, Akhmedova S, Semenkin E (2018) LSHADE algorithm with rank-based selective pressure strategy for solving CEC 2017 benchmark problems. In: 2018 IEEE congress on evolutionary computation, CEC 2018—Proceedings. IEEE, pp 1-8
20. Wang X, Han T, Zhao H (2020) An estimation of distribution algorithm with multi-leader search. IEEE Access 8:37383-37405. https://doi.org/10.1109/ACCESS.2020.2975468
21. Yang Q, Li Y, Gao X-D et al (2021) An adaptive covariance scaling estimation of distribution algorithm. Mathematics 9:3207. https:// doi.org/10.3390/math9243207
22. Cai Y, Sun X, Xu H, Jia P (2007) Cross entropy and adaptive variance scaling in continuous EDA. In: Proceedings of GECCO 2007: genetic and evolutionary computation conference. ACM Press, New York, pp 609-616
23. Grahl J, Bosman PAN, Rothlauf F (2006) The correlation-triggered adaptive variance scaling IDEA. In: GECCO 2006-genetic and evolutionary computation conference. ACM Press, New York, pp $397-404$
24. Bosman PAN, Grahl J, Rothlauf F (2007) SDR: a better trigger for adaptive variance scaling in normal EDAs. In: Proceedings of GECCO 2007: genetic and evolutionary computation conference, pp 492-499
25. Bosman PAN, Grahl J, Thierens D (2013) Benchmarking parameter-free AMaLGaM on functions with and without noise. Evol Comput 21:455-469. https://doi.org/10.1162/EVCO_ a_00094
26. Hansen N, Ostermeier A (2001) Completely derandomized selfadaptation in evolution strategies. Evol Comput 9:159-195
27. Auger A, Hansen N (2005) A restart CMA evolution strategy with increasing population size. In: 2005 IEEE congress on evolutionary computation, IEEE CEC 2005. Proceedings. IEEE, pp 1769-1776
28. Loshchilov I (2013) CMA-ES with restarts for solving CEC 2013 benchmark problems. In: 2013 IEEE congress on evolutionary computation, CEC 2013, pp 369-376
29. Huang X, Jia P, Liu B (2010) Controlling chaos by an improved estimation of distribution algorithm. Math Comput Appl 15:866-871. https://doi.org/10.3390/mca15050866
30. Miquêlez T, Bengoetxea E, Mendiburu A, Larrañaga P (2007) Combining Bayesian classifiers and estimation of distribution algorithms for optimization in continuous domains. Connect Sci 19:297-319. https://doi.org/10.1080/09540090701725524
31. Karshenas H, Santana R, Bielza C, Larrañaga P (2013) Regularized continuous estimation of distribution algorithms. Appl Soft Comput J 13:2412-2432. https://doi.org/10.1016/j.asoc.2012.11.049
32. Qian B, Li Z, Hu R (2017) A copula-based hybrid estimation of distribution algorithm for m-machine reentrant permutation flowshop scheduling problem. Appl Soft Comput 61:921-934. https:// doi.org/10.1016/j.asoc.2017.08.037
33. PourMohammadBagher L, Ebadzadeh MM, Safabakhsh R (2017) Graphical model based continuous estimation of distribution algorithm. Appl Soft Comput 58:388-400. https://doi.org/10.1016/j. asoc.2017.04.066
34. Wang X, Zhao H, Han T et al (2019) A Gaussian estimation of distribution algorithm with random walk strategies and its application in optimal missile guidance handover for multi-UCAV in over-thehorizon air combat. IEEE Access 7:43298-43317. https://doi.org/ 10.1109/ACCESS. 2019.2908262
35. Li X, Epitropakis MG, Deb K, Engelbrecht A (2017) Seeking multiple solutions: an updated survey on niching methods and their applications. IEEE Trans Evol Comput 21:518-538. https://doi. org/10.1109/TEVC.2016.2638437
36. Qi X, Li K, Potter WD (2016) Estimation of distribution algorithm enhanced particle swarm optimization for water distribution network optimization. Front Environ Sci Eng 10:341-351. https://doi. org/10.1007/s11783-015-0776-z
37. Zhao F, Shao Z, Wang J, Zhang C (2016) A hybrid differential evolution and estimation of distribution algorithm based on neighbourhood search for job shop scheduling problems. Int J Prod Res 54:1039-1060. https://doi.org/10.1080/00207543.2015.1041575
38. Zhao F, Shao Z, Wang J, Zhang C (2017) A hybrid optimization algorithm based on chaotic differential evolution and estimation of distribution. Comput Appl Math 36:433-458. https://doi.org/10. 1007/s40314-015-0237-0
39. Sun Z, Gu X (2017) Hybrid algorithm based on an estimation of distribution algorithm and cuckoo search for the no idle permutation flow shop scheduling problem with the total tardiness criterion minimization. Sustainability 9:953. https://doi.org/10.3390/su9060953
40. Liu ZZ, Wang Y, Yang S, Tang K (2019) An adaptive framework to tune the coordinate systems in nature-inspired optimization algorithms. IEEE Trans Cybern 49:1403-1416. https://doi.org/10. 1109/TCYB. 2018.2802912

41. Wang Y, Li H-X, Huang T, Li L (2014) Differential evolution based on covariance matrix learning and bimodal distribution parameter setting. Appl Soft Comput 18:232-247. https://doi.org/10.1016/j. asoc.2014.01.038
42. Awad NH, Ali MZ, Liang J et al (2016) Problem definitions and evaluation criteria for the CEC 2017 special session and competition on real-parameter optimization
43. Mallipeddi RPNSGW (2010) Problem definitions and evaluation criteria for the CEC 2010 competition on constrained realparameter optimization

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.