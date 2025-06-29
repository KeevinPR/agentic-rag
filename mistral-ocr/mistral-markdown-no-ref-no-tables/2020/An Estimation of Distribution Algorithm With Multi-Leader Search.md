# An Estimation of Distribution Algorithm With Multi-Leader Search 

XIAOFEI WANG*, (Member, IEEE), TONG HAN, AND HUI ZHAO<br>Aeronautics Engineering College, Air Force Engineering University, Xi'an 710038, China<br>Corresponding author: Xiaofei Wang (wxf825421673@163.com)


#### Abstract

The estimation of distribution algorithm (EDA) is a well-known stochastic search method but is easily affected by the ill-shaped distribution of solutions and can thus become trapped in stagnation. In this paper, we propose a novel modified EDA with a multi-leader search (MLS) mechanism, namely, the MLS-EDA. To strengthen the exploration performance, an enhanced distribution model that considers the information of population and distribution is utilized to generate new candidates. Moreover, when the algorithm stagnates, the MLS mechanism will be activated to perform a local search and shrink the search scope. The performance of the MLS-EDA in addressing complex optimization problems is verified using the CEC 2014 and CEC 2017 testbeds with 30D, 50D and 100D tests. Several modern algorithms, including the top-performing methods in the CEC 2014 and CEC 2017 competitions, are considered as competitors. The competitive performance of our proposed MLS-EDA is discussed based on the comparison results.


#### Abstract

INDEX TERMS Estimation of distribution algorithm, real-numerical optimization, CEC 2014, CEC 2017, evolutionary computation.


## I. INTRODUCTION

The last few decades have seen tremendous progress in the field of evolutionary computation. As one of the most effective tools for solving NP-hard problems, evolutionary computation has received widespread attention and has been extensively researched worldwide. The main ideas of evolutionary computation derive from the laws of physics and chemistry, the activities and phenomena of natural organisms, and human behaviors. The algorithms are designed to solve optimization problems in accordance with such natural laws through various means. The traditional representative optimizers include the genetic algorithm (GA) [1], the neural network (NN) [2], particle swarm optimization (PSO) [3] and differential evolution (DE) [4]. Many experts and scholars have continuously devoted themselves to the study of evolutionary algorithms and have proposed numerous novel, well-established methods, such as the grey wolf optimizer (GWO) [5], ant lion optimizer (ALO) [6], teaching-learning-based optimization (TLBO) [7], virus colony search (VCS) [8], Harris hawks optimization (HHO) [9] and nuclear reaction optimization (NRO) [10]. Moreover, research on

[^0]evolutionary algorithms involves not only exploring new search frameworks but also improving and applying existing algorithms; this latter direction of algorithm development has also led to the emergence of a wide variety of methods, such as L-SHADE [11], CPI-JADE [12], DOLTLBO [13] and GEDGWO [14].

Estimation of distribution algorithm (EDA) [15], as one of the traditional evolutionary computation techniques, has undergone considerable development over the past two decades. In contrast to traditional evolutionary algorithms, which uses crossover, mutation and selection mechanisms, the EDA possesses a unique characteristic in that it estimates the probability distribution model of selected solutions and iteratively evolves the whole population. The Gaussian distribution model is typically used in EDA to solve problems in the continuous domain. According to the structure of the Gaussian probability model and the relationships between variables, EDAs can be classified into univariate [16], bivariate [17] and multivariate [15] models, and the competitive performance of multivariate Gaussian distribution model, which is the topic of our research, has been verified in various applications compared with the other two methods. However, when solving multimodal problems, an EDA cannot effectively capture the features of such a problem through an


[^0]:    The associate editor coordinating the review of this manuscript and approving it for publication was Jenny Mahoney.

estimated Gaussian distribution model. Moreover, the variances of the distribution in the slope directions may shrink rapidly in a later stage of optimization [18]. Thus, the traditional EDA tends to suffer from premature convergence and can easily become trapped in stagnation.

To overcome these deficiencies, many improvements to the EDA have been made, which can be categorized into three types: distribution model modifications, population diversity enrichment and algorithm hybridization. Based on the fact that the multivariate Gaussian distribution model is determined by its estimated mean and covariance matrix, studies were initially carried out on modifications to the distribution model. Grahl et al. [19] developed a correlation -triggered adaptive variance scaling (CT-AVS) strategy to scale the variances. Soon after, the same authors investigated another triggering method for adaptive variance scaling named standard deviation ratio (SDR) [20]. Based on these foundations, the well-known AMaLGaM [21] algorithm combining AVS, SDR and anticipated mean shift (AMS), was proposed [22]. Further studies were conducted by Ren and his teammates [23], who expanded the AMS strategy to consider the mean quality. Moreover, they explored a novel AVS strategy with anisotropic adjustment based on the local fitness landscape [18]. Their other work was EDA ${ }^{2}$ [24], in which an archive is adopted to store more promising solutions to revise the distribution scope. Other representative EDA modifications of this type are the covariance matrix adaptation evolution strategy (CMA-ES) [25] and its variants. The CMA-ES has a complex framework that uses "rank-1" and "rank $-\mu$ " update strategies. The IPOP-CMA-ES [26] is a promising CMA-ES variant that uses a restart strategy to enrich the population diversity. Currently, the NBIPOP-aCMA-ES [27], based on the BIPOP-CMA-ES [28] and active CMA-ES [29], is widely identified as the most efficient CMA-ES variant. Although the NBIPOP-aCMA-ES exhibits outstanding performance, it suffers from a relatively high computational burden due to its complex search mechanism [30].

Yuan reported that maintaining population diversity plays a key role in EDA performance [31]. Thus, the second method of avoiding premature convergence is to combine an EDA with diverse search mechanisms that can effectively enrich population diversity. Huang et al. [32] employed a simulated annealing method as a local search strategy in an EDA. In Miquélez's work [33], the Bayesian classifier method and an EDA were combined to establish a probability model and solve a continuous optimization problem. The effectiveness of incorporating a regularized learning model into an EDA was studied by Karshenas et al. [34]. Copula theory [35] and a probabilistic graphical model [36] have also been utilized in an EDA and applied to samples. In RWGEDA, random walk strategies were incorporated into an EDA [37]. Moreover, the effects of the promising area detection technique and niching method on EDA performance improvement have been addressed by various studies [38]-[40].

Hybridizing EDA with other optimization algorithms to fully exploit their respective advantages is also regarded an
effective strategy for improving performance. Qi et al. [41] integrated an EDA with PSO to solve the water distribution problem. In three studies [42]-[44], DE has been utilized as a local search method to develop new hybrid algorithms. Sun and Gu [45] proposed a hybrid evolutionary algorithm combining an EDA and cuckoo search (CS) to solve scheduling problem.

Although all of the studies discussed above improved EDA performance from various perspective, several deficiencies still remain that require improvement:

- In most EDA variants, the available of population information is not fully exploited. First, the information of the current best solution in each iteration is not utilized. Furthermore, the role of promising solutions in enhancing the local search ability of an EDA has not received much attention. Moreover, the remaining solutions that are not utilized in constructing the distribution model are always neglected or abandoned. All these factors increase the computational cost.
- Developing a novel efficient mechanism for enriching the population diversity that does not rely on the distribution model, which can be achieved by taking advantage of the results derived in each generation, is still an urgent problem for EDA improvement.
- For a hybrid EDA, switching among sub-algorithms with different search mechanisms complicates the task of balancing the exploration and exploitation processes. Additionally, hybridization may lead to a more complex execution framework, which will increase the computational cost. Moreover, hybrid algorithms tend to have more parameters that require adjustment, which will reduce the parameter sensitivity of such an algorithm.
Both the deficiencies described above and the development prospects of EDAs in the field of evolutionary computation due to their model-based characteristics prompt us to propose new algorithms of this type. EDAs are currently playing an increasingly important role in algorithm development. From CEC 2016 to CEC 2018, most of the top algorithms were based on the use of distribution models for sampling, such as UMOEAII [46] in 2016, EBOwithCMAR [47] in 2017, and HSES [48] in 2018. In contrast to these promising EDA-based variants, we propose a novel nonhybrid EDA variant using a multi-leader search (MLS) mechanism in an eigen coordinate system, called the MLS-EDA. The novel characteristics and features of our MLS-EDA can be attributed to the following two mechanisms.
- For each individual in the population, an enhanced distribution model that considers population location differences is utilized to produce new candidates. This mechanism makes full use of the current population information to improve the distribution model and avoid wasted computation. Moreover, this mechanism can diversify the search scope, thus helping to maintain population diversity.
- When the algorithm stagnates, the capacity of the archive will be adaptively enlarged to store more current

leader solutions. For each individual, a leader solution in the archive is randomly selected to guide the individual performing the local search in a different dominant region. Thus, the MLS mechanism will be achieved. This mechanism can exploit multiple high-quality solutions to increase the diversity of the search scope and reduces the dependence on an ill-shaped distribution of solutions; thus, this mechanism exhibits strong exploration behavior when the algorithm stagnates.
The performance of our MLS-EDA in solving complex benchmarks is evaluated using the CEC 2014 and CEC 2017 testbeds with $30 D, 50 D$ and $100 D$ tests, and the experimental results are compared with those of several other well-established algorithms, including the winner of the CEC 2014 test, L-SHADE, and the two top algorithms in CEC 2017, HSES and ELSHADE-SPACMA. Moreover, several modern EDAs, including VCS and RWGEDA, are employed to further demonstrate the efficiency of our modification.

The rest of this study is organized as follows: Section 2 presents a brief description of the original EDA and a detailed introduction to the MLS-EDA. In Section 3, the performance of the MLS-EDA is evaluated on the complex CEC 2014 and CEC 2017 test suites, and the results are statistically analyzed and compared. In the final section, the conclusions and prospects of this research are presented.

## II. MLS-EDA

## A. REVIEW OF THE BASIC EDA

The EDA is a model-based algorithm in which the solution vectors follow a Gaussian probability distribution model as follows:
$G_{(\boldsymbol{\mu}, \boldsymbol{C})}=\frac{(2 \pi)^{-\pi / 2}}{(\operatorname{det} \boldsymbol{C})} \exp \left(-(\boldsymbol{X}-\boldsymbol{\mu})^{\mathrm{T}}(\boldsymbol{C})^{-1}(\boldsymbol{X}-\boldsymbol{\mu}) / 2\right)$
where

$$
\begin{aligned}
& \boldsymbol{\mu}=\frac{1}{|\boldsymbol{A}|} \sum_{i=1}^{|\boldsymbol{A}|} \boldsymbol{x}_{i}, \quad \boldsymbol{x}_{i} \in \boldsymbol{A} \text { and } \boldsymbol{A} \subset \boldsymbol{X} \\
& \boldsymbol{C}=\frac{1}{|\boldsymbol{A}|} \sum_{i=1}^{|\boldsymbol{A}|}\left(\boldsymbol{x}_{i}-\boldsymbol{\mu}\right)\left(\boldsymbol{x}_{i}-\boldsymbol{\mu}\right)^{\mathrm{T}}, \quad \boldsymbol{x}_{i} \in \boldsymbol{A} \text { and } \boldsymbol{A} \subset \boldsymbol{X}
\end{aligned}
$$

The symbol $\boldsymbol{A}$ in (2) and (3) denotes a selected set of highquality solutions. The EDA uses an estimated Gaussian distribution based on the selected superior solutions in set $\boldsymbol{A}$ to iteratively generate new solutions, thus driving the algorithm to complete the optimization process. In this way, the new generation is produced as follows:

$$
\boldsymbol{x}_{i}=\boldsymbol{\mu}+\boldsymbol{y}_{i}, \quad \boldsymbol{y}_{i} \sim N(0, \boldsymbol{C})
$$

In the standard EDA, the selected high-quality solutions are mainly distributed in the hyperellipsoid of the original probability distribution and tend to lie closer to the dominant region. The long axis of the probability distribution hyperellipsoid estimated from these solutions will be perpendicular
![img-0.jpeg](img-0.jpeg)

FIGURE 1. The variance in the non-descent direction is gradually enlarged, while the variance in the descent direction is gradually reduced.
to the descent direction of the function value. Fig. 1 shows an illustration of this phenomenon. Consequently, as the number of iterations increases, the main search direction of the algorithm become increasingly perpendicular to the descent direction of fitness, resulting in an ill-conditioned distribution of solutions, which allows the algorithm to easily fall into a local optimum. To overcome this defect, we have developed a modified EDA with multiple mechanisms, which is discussed in the following section.

## B. DESCRIPTION OF THE MLS-EDA

The modifications proposed in the MLS-EDA consist of four components: a) a weighted maximum likelihood estimation (MLE) method to improve the mean point quality, b) a distribution enhancement strategy (DES) to diversify the distribution scope, c) an MLS mechanism to eliminate stagnation, and d) tan eigen coordinate framework to modify the direction of evolution. Further details are presented as follows.

## 1) WEIGHTED MAXIMUM LIKELIHOOD ESTIMATION METHOD

In the basic EDA, the MLE method is used to estimate the mean point, as shown in (2). In our MLS-EDA, a weighted MLE method is employed to calculate the weighted mean point, an approach that has been proven to be more efficient in many studies [14], [23], [25].

$$
\boldsymbol{\mu}=\sum_{i=1}^{|\boldsymbol{A}|} \omega_{i} \boldsymbol{x}_{i}, \quad \boldsymbol{x}_{i} \in \boldsymbol{A} \text { and } \boldsymbol{A} \subset \boldsymbol{X}
$$

where

$$
\omega_{i}=\ln (|\boldsymbol{A}|+1) /\left(\sum_{i=1}^{|\boldsymbol{A}|}(\ln (|\boldsymbol{A}|+1)-\ln (i))\right)
$$

In (6), the $\omega_{i}$ are the weight coefficients, arranged in descending order relative to the solution quality in set $\boldsymbol{A}$. The weighted MLE method places greater emphasis on superior solutions in distribution estimation, thus improving the mean point quality. As done in most EDA variants, the top half of

the population is selected in set $\boldsymbol{A}$ [25], [37]; accordingly, $|\boldsymbol{A}|=N P / 2$, where $N P$ denotes the population size.

## 2) DISTRIBUTION ENHANCEMENT STRATEGY

In (5), only the half of the solutions of the highest quality is employed to construct the distribution model, while the remaining inferior solutions are abandoned. To avoid this computational waste and to consider the differences in location between the superior and inferior solutions, a novel sampling method using a DES in an eigen coordinate system is explored.

First, each solution is judged as either a superior or inferior solution according to its fitness ranking in the population, which is calculated as

$$
\begin{aligned}
P_{\text {rank }}(i)=1+\left(1-\left(f\left(x_{i}\right)\right)_{\text {rank }}\right) / N P, & \\
& \left(f\left(\boldsymbol{x}_{i}\right)\right)_{\text {rank }} \in[1,2, \ldots, N P]
\end{aligned}
$$

The $i$ th solution will be regarded as a superior solution only if its fitness ranking $P_{\text {rank }}(i)$ is greater than 0.5 ; otherwise, it is an inferior solution. Since sampling is performed in an eigen coordinate framework, the solution vectors must be transformed from the normal coordinate system into the eigen coordinate system. The solution vectors in the eigen coordinates can be determined as follows:

$$
\left\{\begin{array}{l}
\boldsymbol{\mu}^{(\mathrm{E})}=\boldsymbol{B}^{\mathrm{T}} \boldsymbol{\mu} \\
x_{i}^{(\mathrm{E})}=\boldsymbol{B}^{\mathrm{T}} \boldsymbol{x}_{i}
\end{array}\right.
$$

where the symbol E indicates a vector expressed in eigen coordinates. $\boldsymbol{B}$ is the eigendirection matrix and obtained through the decomposition of $\boldsymbol{C}$, as shown in (9).

$$
\boldsymbol{C}=(\boldsymbol{B D})(\boldsymbol{B D})^{\mathrm{T}}
$$

Generally, a superior solution is usually located closer to the global optimum point than the mean point, as illustrated in Fig. 1. Thus, the mean point can be enhanced by moving it towards the high-quality solution as follows:

$$
\boldsymbol{\mu}_{j}^{(\mathrm{E})}=\boldsymbol{\mu}_{j}^{(\mathrm{E})}+r \cdot\left(\boldsymbol{x}_{i, j}^{(\mathrm{E})}-\boldsymbol{\mu}_{j}^{(\mathrm{E})}\right), \quad r \sim U(0,1)
$$

The subscript $j$ in (10) denotes the $j$ th dimension. Thus, a new candidate is produced as follows:

$$
\boldsymbol{x}_{i, j}^{(\mathrm{E})}=\boldsymbol{\mu}_{j}^{(\mathrm{E})}+\boldsymbol{D}_{j} y_{i, j}, \quad y_{i, j} \sim N(0,1)
$$

$\boldsymbol{D}$ in (11) is a vector of the square root of the eigenvalues, i.e., $\boldsymbol{D}=\left(\sqrt{\lambda_{1}}, \sqrt{\lambda_{2}}, \ldots, \sqrt{\lambda_{\text {dim }}}\right)$, which is obtained as shown in (9). As shown in (10), the enhanced mean point contains information on both the distribution and the individual solution; thus, the distribution scope can be diversified, as shown in Fig. 2, which is helpful for solving multimodal problems. Moreover, because (10) is executed on each dimension individually, it can take advantage of the difference between the normal coordinates and the eigen coordinates, as presented in Fig. 2. Because the eigen coordinate system can eliminates the dependence among the different axes, the probable distribution of the shifted mean point in the
![img-2.jpeg](img-2.jpeg)

FIGURE 2. The enhanced mean point is obtained by moving the mean point towards a superior solution.
![img-2.jpeg](img-2.jpeg)

FIGURE 3. The enhanced mean point is obtained by moving the mean point away from the inferior solution.
eigen coordinates (in red) is more satisfactory than that in the normal coordinates (in green).

On the other hand, an inferior solution is usually located outside of the fitness contour across the mean point. Accordingly, a new candidate solution can be generated by enhancing the mean point by moving it away from such an inferior solution, as shown in (12) and (13).

$$
\begin{aligned}
& \boldsymbol{\mu}_{j}^{(\mathrm{E})}=\boldsymbol{\mu}_{j}^{(\mathrm{E})}+r \cdot\left(\boldsymbol{\mu}_{j}^{(\mathrm{E})}-\boldsymbol{x}_{i, j}^{(\mathrm{E})}\right), \quad r \sim U(0,1) \\
& \boldsymbol{x}_{i, j}^{(\mathrm{E})}=\boldsymbol{\mu}_{j}^{(\mathrm{E})}+\boldsymbol{D}_{j} y_{i, j}, \quad y_{i, j} \sim N(0,1)
\end{aligned}
$$

## 3) MULTI-LEADER SEARCH MECHANISM

Unlike the CMA-ES, the basic EDA has a poor ability to modify its ill-shaped distribution of solution. Thus, the basic EDA cannot easily eliminate local stagnation. To overcome this deficiency by enhancing the population diversity of the basic EDA, we propose the MLS mechanism, which is executed only when the algorithm stagnates. If the distribution model shows no change compared with the previous generation, i.e., the first half of the population is not updated, then the algorithm is considered to be trapped in stagnation and the MLS mechanism is activated.

The core idea of the MLS technique is to perform a local search based on multiple top solutions as leaders. In our MLS mechanism, an archive (denoted by $\boldsymbol{S}$ ) with an adaptive size is designed and employed to store the current dominant solutions. Initially, the size of $\boldsymbol{S}$ is equal to 1 , meaning that

![img-3.jpeg](img-3.jpeg)

FIGURE 4. The MLS mechanism can generate an efficient local search around the selected leader.
the single current best solution is stored. When the algorithm stagnates for the first time, the number of solutions in archive $\boldsymbol{S}$ is increased by 1 , meaning the two current best solutions are stored, and so on. When $\boldsymbol{S}$ reaches its predefined maximum size, its capacity will no longer be expanded. The next time that the algorithm stagnates, the size of the archive will be restored to the initial state and will not change, meaning that once again, only the single best solution is stored in $\boldsymbol{S}$. The maximum size of $\boldsymbol{S}$ is set equal to three-times the dimensionality of the problem, as is discussed in the next section.

To sufficiently balance the exploration and exploitation performance, this mechanism incorporates two different search behaviors. If the $i$ th solution is not selected in set $\boldsymbol{S}$, i.e., if $P_{\text {rank }}(i)<1-|\boldsymbol{S}| / N P$, then the MLS mechanism is executed around a selected dominant solution, as shown in (14).

$$
\begin{aligned}
\boldsymbol{x}_{i}^{(\mathrm{E})} & =\boldsymbol{x}_{\text {leader }}^{(\mathrm{E})}+\boldsymbol{y}_{i}\left(\boldsymbol{x}_{\text {leader }}^{(\mathrm{E})}-\boldsymbol{x}_{i}^{(\mathrm{E})}\right)+r_{1} \cdot \boldsymbol{x}_{\text {leader }}^{(\mathrm{E})}-r_{2} \cdot \boldsymbol{x}_{i}^{(\mathrm{E})} \\
\boldsymbol{y}_{i} & \sim N(0, \boldsymbol{I}), \quad r_{1}, r_{2} \sim N(0,1), \boldsymbol{x}_{\text {leader }} \in \boldsymbol{S}
\end{aligned}
$$

In (14), $\boldsymbol{x}_{\text {leader }}$ is a leader solution and is randomly selected from archive $\boldsymbol{S}$. The local search area in the eigen coordinate system is satisfactory, as illustrated in Fig. 4. As the number of instances of convergence stagnation increases, exploration is performed based on more dominant solutions in archive $\boldsymbol{S}$. Because these dominant solutions may be located in different promising regions, the local search expressed in (14) can improve the exploration behavior of the algorithm in different dominant regions.

Otherwise, when the $i$ th solution is selected in set $\boldsymbol{S}$, i.e., when $P_{\text {rank }}(i)>1-|\boldsymbol{S}| / N P$, the corresponding candidate is sampled using a shrunken distribution model. This alternative behavior of the MLS mechanism is executed as follows:

$$
\begin{gathered}
\boldsymbol{x}_{i}^{(\mathrm{E})}=\boldsymbol{x}_{i}^{(\mathrm{E})}+\left|z_{i}\right| \cdot\left(\boldsymbol{x}_{\text {leader }}^{(\mathrm{E})}-\boldsymbol{x}_{i}^{(\mathrm{E})}\right)+\boldsymbol{D}^{\boldsymbol{t}} \boldsymbol{y}_{i} \\
z_{i} \sim N(0,1), \boldsymbol{y}_{i} \sim N(0, \boldsymbol{I}), \quad \boldsymbol{x}_{\text {leader }} \in \boldsymbol{S}
\end{gathered}
$$

where

$$
\boldsymbol{D}^{\boldsymbol{t}}=\boldsymbol{D} \cdot\left(1-F E s / F E s_{\max }\right)
$$

The first two terms in (15) represent local exploitation around the $i$ th solution using the location difference between
![img-4.jpeg](img-4.jpeg)

FIGURE 5. The MLS mechanism can generate an efficient mean point around at selected leader. $\left|z_{i}\right|$ is used to ensure that half of the distribution ellipsoid in the descent direction is retained.
the $i$ th solution itself and a randomly selected dominant solution. This search scope derived from the first two terms in (15) in the eigen coordinates is illustrated in Fig. 5. The absolute value of $z_{i}$ is used as a truncation setting, which ensures that half of the search scope near the dominant area is preserved. In fact, this process also relies on the use of a leader solution for local search to generate the distribution mean point, thus enhancing the distribution and even the diversity of the population. As presented in (16), the elements of vector $\boldsymbol{D}$ decrease as the number of evaluations increases, thereby reducing the search scope. Thus, in later search stages, the MLS mechanism focuses on a more precise local search around the randomly selected leader solution.

Both search behaviors expressed in (14) and (15) utilize a leader solution as the center around which to execute local exploitation. The critical difference is that the former behavior uses a location difference to generate new solutions, while the latter behavior uses a reduced distribution scope for sampling. In other words, both search behaviors in the MLS mechanism are designed to achieve the same end.

Finally, the newly obtained solution is transformed into the normal coordinates through rotation as follows:

$$
\boldsymbol{x}_{i}=\boldsymbol{B} \cdot \boldsymbol{x}_{i}^{(\mathrm{E})}
$$

To ensure the global convergence performance of the MLSEDA, a greedy technique is utilized to preserve the superior solutions in both the current population and the newly produced population, thereby preventing the loss of high-quality solutions in the sire generation. The pseudocode for the MLSEDA is presented below, and the execution process of the algorithm is visually summarized in Fig. 6.

## C. COMPUTATIONAL TIME COMPLEXITY ANALYSIS OF THE MLS-EDA

The main factor that typically limits the application of EDA is the high computational cost, which is related to the dimensionality of the problem. In our MLS-EDA, the time complexity of updating the covariance matrix as expressed in (3), is $\mathrm{O}\left(D^{2} \cdot N P / 2\right)$. Moreover, we use the Jacobi method to decompose the covariance matrix, as expressed in (9), with a time complexity of $\mathrm{O}\left(D^{3}\right)$. In the population update process,

![img-5.jpeg](img-5.jpeg)

FIGURE 6. Flowchart of the MLS-EDA.
sampling is executed in each dimension for all individuals, thus leading to a computational cost of $\mathrm{O}(N P \cdot D)$. Therefore, the maximum time complexity of the MLS-EDA is by $\mathrm{O}\left\{D^{2} \times \max (D, N P / 2)\right\}$. Additionally, according to the execution process depicted in Fig. 6, the computational cost of updating the covariance matrix updating can be avoided when the algorithm stagnates. Under these conditions, our MLS-EDA has similar efficiency to the original EDA with a time complexity less than $\mathrm{O}\left\{D^{2} \times \max (D, N P / 2)\right\}$ in each iteration.

## III. EXPERIMENTAL STUDY USING MODERN CEC 2014 AND CEC 2017 TESTBEDS

There are no standard criteria for convincing verification of the real contributions of a novel algorithm in the field of evolutionary computation. We believe that three conditions are indispensable. First, comparison with advanced algorithms from various families is mandatory. Second, the use of a complete set of modern complex benchmarks, including the same conditions and parameter settings, is suggested. Finally, the advantages of the proposed algorithm should be properly specified. Thus, we employ the challenging CEC 2014 and CEC 2017 test suites to assess the performance of the MLS-EDA and carry out two comparisons. In the first experiment, six promising algorithms from various families that participated in CEC 2014 are applied to demonstrate the superior performance of our proposed algorithm. In the second comparison, seven modern methods, including the topperforming algorithms in CEC 2017, are considered as competitors.

The CEC 2014 test suite contains 30 benchmarks (denoted by F1 to F30), while the CEC 2017 suite consists of 29 benchmarks (excluding F2). The tests in these two sets possess different characteristics and, accordingly, can be categorized into four groups. Further descriptions of these two test suites are provided in [49] and [50]. As recommended by the organizers, each benchmark should be independently run 51 times with the same maximum function evaluations ( $F E s_{\max }$ ) to ensure a fair evaluation. The value of $F E s_{\max }$ is set to $D \times 10,000$, where $D$ denotes the dimensionality of the problem. In this paper, we carry out a full comparison using $30 D, 50 D$ and $100 D$ problems. The results are recorded in the form of error values between the derived optimal result and the global optimal result, where the global optimum is determined to be achieved with an error value less than 1e-08. All simulations reported in this paper were run in the same hardware environment: a laptop (with a $2.20 \mathrm{GHz} \mathrm{i} 7-8700 \mathrm{HQ}$ CPU and 16 GB of memory) and MATLAB 2018a was employed for coding and execution.

```
Algorithm MLS-EDA
    1: Initialization: \(N P, \boldsymbol{S}, F E s=0\) and \(F E s_{\max } ;\)
    2: Produce the initial population \(\boldsymbol{X}\) and evaluate, \(F E s=F E s+N P\);
    3: Update the best solution \(\boldsymbol{x}_{\text {Best }}\) in the present generation;
    4: While \(F E s \geq F E s_{\max }\), output \(f\left(\boldsymbol{x}_{\text {best }}\right)\) and terminate the search process; otherwise
    6: Update the distribution model, including \(\boldsymbol{\mu}\) and \(\boldsymbol{C}\) using the half of the solutions of the highest quality in \(\boldsymbol{A}\), by means
    of (5), (6) and (3);
    7: Calculate the eigenvalue decomposition of \(\boldsymbol{C}\) using (9);
    8: For each solution \(x_{i}\)
        Calculate \(P_{\text {rank }}(i)\);
        Rotate \(\boldsymbol{x}_{i}\) into the eigen coordinate system and determine \(\boldsymbol{x}_{i}^{(\mathrm{E})}\) using (8);
        If the algorithm falls into stagnation
            Update the size of archive \(S\);
            If \(P_{\text {rank }}(i)<1-|\boldsymbol{S}| / N P\)
                Update \(\boldsymbol{x}_{i}^{(\mathrm{E})}\) using the MLS behavior as expressed in (14);
            Else
                Update \(\boldsymbol{x}_{i}^{(\mathrm{E})}\) using the MLS behavior as expressed in (15) and (16);
            End if
        Otherwise
        If \(P_{\text {rank }}(i)>0.5\)
            Update \(\boldsymbol{x}_{i}^{(\mathrm{E})}\) using the enhanced mean as expressed in (10) and (11);
            Else
                Update \(\boldsymbol{x}_{i}^{(\mathrm{E})}\) using the enhanced mean as expressed in (12) and (13);
            End if
        End if
        Rotate candidate \(\boldsymbol{x}_{i}^{(\mathrm{E})}\) into the normal coordinate system by (17);
        Calculate the fitness \(f\left(\boldsymbol{x}_{i}\right)\);
        End for
    9: \(F E s=F E s+N P\) and go to step 3;
```

In Appendix, we present the experimental results obtained on the CEC 2014 and CEC 2017 test suites, respectively, for $30 D, 50 D$ and $100 D$ tests using the MLS-EDA with the population size set to $10 \cdot D$ and the maximum size of set $S$ set to $3 \cdot D$. These statistical results, including the best, worst, median, mean and standard deviation (SD) error values, can be referenced in future studies. Moreover, the convergence performances achieved on these two test suites is illustrated in Appendices B and D. Since the values of parameters $N P$ and $|\boldsymbol{S}|_{\max }$ in the MLE-EDA need to be determined, we analyze the optimal parameter settings for the MLS-EDA before presenting the comparisons with other techniques.

## A. PARAMETER SENSITIVITY ANALYSIS OF THE MLS-EDA

The parameter sensitivity of an evolutionary algorithm is essential when addressing different problems. The MLS-EDA has two key parameters: the population size $N P$ and the maximum size of set $\boldsymbol{S}$. In this section, we present two experimental studies to investigate the optimal parameter values using the CEC 201430 D test suite. All benchmarks are run 51 times with $F E s_{\max }=300,000$ to obtain the mean error value, and the results are presented for comparison in Tables 1 and 2.

In Table 1, the results for five population sizes, $N P=6 \cdot D, 8 \cdot D, 10 \cdot D, 12 \cdot D$ and $14 \cdot D$, are given. The last row in Table 1 indicates the ranks of these five settings according to the Friedman test. The best performance is achieved by the algorithm with $N P=10 \cdot D$. As the population size decreases or increases, the performance of the algorithm will decrease accordingly. The reason for this phenomenon is that a small population size cannot provide sufficient support to precisely capture the problem characteristics, whereas a larger population size will cause the number of iterations to decrease, thus compromising the convergence performance. Moreover, a larger population size can result in a greater computational cost since the maximum time complexity is $\mathrm{O}\left\{D^{2} \times \max (D, N P / 2)\right\}$.

In Table 2, the rankings are assessed for settings of $|\boldsymbol{S}|_{\max }=1, D, 2 \cdot D, 3 \cdot D, 4 \cdot D$ and $5 \cdot D$. When the value of $|\boldsymbol{S}|_{\max }$ is set to 1 , this indicates that only the single best solution is considered for local exploitation in the MLS mechanism. According to the statistical results presented in the last row of Table 2, this setting leads to the worst behavior. In contrast, a larger size of $\boldsymbol{S}$ can significantly improve the algorithm's performance. All of the remaining five settings are acceptable, but $|\boldsymbol{S}|_{\max }=3 \cdot D$ yields the most promising results, as indicated by its highest ranking.

TABLE 1. Mean error results achieved by the MSL-EDA with different population sizes on the CEC 2014 test suite for 30D problems.


The chi-square from the Friedman test is 29.1461 , and the p -value is $7.2998 \mathrm{e}-06$.

Overall, the optimal parameter settings of the MLS-EDA are $N P=10 \cdot D$ and $\left|\boldsymbol{S}\right|_{\max }=3 \cdot D$. Notably, we have defined both of these parameters relative to the dimensionality of the problem, which is convenient for ensuring the use of parameter settings based on equivalent criteria when the algorithm is applied to solve problems of different dimensionalities. However, according to the no-free-lunch theorem, no single algorithm can be used to satisfactorily solve all problems. The optimal parameters demonstrated here are still not universally adequate, and additional application experience will be needed to further optimize these parameters.

## B. MRE-EDA MODIFICATION COMPONENT ANALYSIS

In the previous subsection, the optimal parameter values are determined. In this part, we further analyze the influence on the algorithm's performance exerted by the different search behaviors driven by our modifications. As described in Section 2, our improvements mainly consist of two components, i.e., the DES and the MLS mechanism. Thus, three EDA variants are designed by removing one or both of these components, as presented in Table 3. These three variants, along with the MLS-EDA itself, are benchmarked for $30 D$ problems using the CEC 2014 testbed. The same parameter settings are adopted, with 51 independent runs and the values of $F E s_{\max }$ fixed at 300,000 . Table 4 presents the statistical results, and the last row indicates the differences in performance among the four MLS-EDA variants. Clearly, our original MLS-EDA with both components achieves the best performance in this experiment. For the other algorithms, a lower ranking corresponds to a greater impact of the lost component on algorithm performance. Algorithm 2 and Algorithm 3 rank second and third, respectively. According to their rankings, there is little difference in performance between these two MLS-EDA variants. The poorest performance is exhibited by Algorithm 1, with both modifications removed. Specifically, as seen from the results in Table 4, the MLS mechanism improves the algorithm's performance in addressing the complex hybridization and composition benchmarks, while the DES significantly enhances the algorithm's ability to solve shifted and rotated problems. From these points of view, our proposed improvements substantially enhance the convergence performance of the basic EDA.

## C. COMPARISON WITH SIX MODERN ALGORITHMS FROM DIFFERENT FAMILIES ON THE CEC 2014 TESTBED

In this subsection, six promising modern algorithms, namely, EMNA $_{\mathrm{g}}$ [15], RWGEDA [37], DOLTLBO [13], VCS [8], CPI-JADE [12] and L-SHADE [11], are considered as

TABLE 2. Mean error values achieved by the MSL-EDA with different maximum sizes of the set $\boldsymbol{S}$ on the CEC 2014 test suite for 30D problems.


The chi-square of Friedman test is 14.1106 , the p -value is $1.4922 \mathrm{e}-02$.
competitors to demonstrate the efficiency of our MLS-EDA. $\mathrm{EMNA}_{\mathrm{g}}$ is a basic multivariate Gaussian EDA, which we use to verify the efficiency of our modifications. RWGEDA is our recently developed EDA variant. DOLTLBO is a successful extension of TLBO. VCS is a well-established hybrid algorithm combining the CMA-ES and DE. CPI-JADE is a modification of JADE using a new framework. L-SHADE is an advanced DE algorithm whose variants have demonstrated championship performance in successive CEC competitions. We selected these six algorithms as competitors not only because they are relatively new members of their respective families but also because of their promising performance on the CEC 2014 benchmarks. The parameter settings play a key role in algorithm performance. To ensure fair comparisons, the parameter settings of the other six algorithms in this experiment are adopted in accordance with their respective source literature, as tabulated in Table 5. Each problem of different dimensionalities in this experiment is independently run 51 times to overcome the influence of randomness, with a fixed value of $F E s_{\max }=D \times 10,000$, where $D=30,50$ and 100. The simulation results for the tests with these three dimensionalities are presented in Tables 15 to 17, respectively, in Appendix E.

As presented in Table 15, the MLS-EDA, RWGEDA, CPIJADE and L-SHADE perform robustly in addressing the

TABLE 3. MLS-EDA variants with different search components.


unimodal problems in the $30 D$ test. L-SHADE performs better for solving the multimodal benchmarks, while our MLSEDA shows significant advantages in solving the last two groups of functions.

According to the results for the $50 D$ test in Table 16, the MLS-EDA and RWGEDA performs better in solving F1 to F3. For the multimodal functions F4 to F16, L-SHADE and MLS-EDA are the top two methods, with the best performance on seven and six benchmarks, respectively. Similar to the results in $30 D$ test, the MLS-EDA outperforms the other algorithms in dealing with hybrid functions. However, VCS and DOLTLBO show competitive performance in solving the composite benchmarks.

Notably, the advantages of the MLS-EDA are reduced when solving high-dimensional problems. Nevertheless, from an overall perspective, the MLS-EDA maintains its competitiveness when dealing with multimodal problems.

TABLE 4. Rankings of the four MLS-EDA variants on the CEC 2014 test suite for 30D problems.


The chi-square of the Friedman test is 42.8280 , and the p -value is $2.6769 \mathrm{e}-09$.

TABLE 5. Parameter settings of the seven algorithms in the CEC 2014 test.

L-SHADE performs better in optimizing the first three types of benchmarks, whereas VCS and DOLTLBO are the two best-performing algorithms when faced with composite functions.

The Wilcoxon signed rank test and the Friedman test are carried out to statistically evaluate the efficacy of our proposed algorithm. The pairwise comparison results according to the Wilcoxon signed rank test with $\alpha=0.05$ are presented in Table 6. In this table, "R+" denotes the magnitude by which the MLS-EDA can surpass a competitor, and "R-" represents the opposite effect. The rightmost column of Table 6 summarizes the overall comparisons, where the " + " entry indicates the number of cases in which the MES-EDA shows superior performance relative to the algorithm considered for comparison, the " - " entry indicates the number of cases of inferior performance, and the " $\sim$ " entry indicates

TABLE 6. Comparison results of the Wilcoxon signed rank test $(\alpha=0.05)$.


the number of cases of similar performance. As shown by the statistical results of the $30 D$ and $50 D$ tests, our MLS-EDA outperforms all six competitors, with the " + " value always being the highest, but has a less significant advantage over

TABLE 7. Rankings of the seven algorithms on the CEC 2014 testbed based on the Friedman test $(\sigma=0.05)$.


a. The chi-square is $9.15 \mathrm{e}+01$, and the p -value is $1.46 \mathrm{e}-17$.
b. The chi-square is $9.17 \mathrm{e}+01$, and the p -value is $1.32 \mathrm{e}-17$.
c. The chi-square is $7.65 \mathrm{e}+01$, and the p -value is $1.89 \mathrm{e}-14$.

TABLE 8. Mean time costs of the seven algorithms on the CEC 2014 testbed (in second).


L-SHADE, with the p-value being greater than 0.05 . In the $100 D$ test, MLS-EDA surpasses EMNA $_{\mathrm{g}}$, RWGEDA and DOLTLBO and performs similarly to VCS and CPI-JADE, but it is somewhat inferior to L-SHADE.

In addition to the pairwise comparisons above, a multiple comparison method, the Friedman test, is performed based on the mean values. Table 7 presents the rankings of the seven algorithms according to the Friedman test $(\alpha=0.05)$ for the three problem dimensionalities. The MLS-EDA ranks in first place on the $30 D$ and $50 D$ tests with the smallest ranking value, while L-SHADE ranks best on the $100 D$ tests. The last row of this table shows the ranking performances of the algorithms on all three test sets in terms of a synthetically calculated score, denoted by SR. SR is calculated in accordance with the rank values in the first three rows of Table 7, as shown in (18).

$$
S R=\left(\text { Rank }_{30 D}+\text { Rank }_{50 D}+\text { Rank }_{100 D}\right) / 3
$$

Based on the SR value, the MLS-EDA is the best performing method among the seven algorithms. The CEC 2014 winner L-SHADE ranks second by a small margin. The remaining algorithms rank as follows, from best to worst: RWGEDA, CPI-JADE, VCS, DOLTLBO and $\mathrm{EMNA}_{\mathrm{g}}$. To further highlight the performance differences among the algorithms in this experiment, the post hoc Iman Davenport test was carried out based on the SR results. Further details about this method are provided in [14] and [51]. The critical difference (CD) value calculated in the post hoc test is 1.1998 . A detailed illustration of the significant differences between different competitors in terms of the CD values according to the mean rank values is presented in Fig. 7. No significant difference exists between two algorithms if the average ranking difference between them is less than the CD value. As shown in Fig. 7, the MLS-EDA ranks first in this test and performs similarly to L-SHADE. Moreover, the MLS-EDA shows significantly superior performance compared with the remaining five algorithms, especially $\mathrm{EMNA}_{\mathrm{g}}$. This significant superiority
![img-6.jpeg](img-6.jpeg)

FIGURE 7. Multiple comparisons based on the post hoc Iman Davenport test.
demonstrates the value of the contributions of this work in modifying the basic EDA.

In addition to solution quality, execution efficiency is another important factor in algorithm evaluation. The average time cost of seven algorithms on the same platform for each benchmark are presented in Appendix F. Moreover, the average time consumption results for each algorithm on the tests of all three dimensionalities is calculated in Table 8. The symbol ST represents a time score calculated to compare the efficiency of these seven algorithms as expressed in (19).

$$
S T=\left(T_{30 D}+T_{50 D}+T_{100 D}\right) / 3
$$

In this experiment, CPI-JADE is the most efficient algorithm. The time consumption of MLS-EDA is higher than that of the basic $\mathrm{EMNA}_{\mathrm{g}}$ because of its associated modifications, but the difference is small. The performance of RWGEDA is similar to that of the MLS-EDA, while VCS and DOLTLBO are the two algorithms with the lowest efficiency.

## D. COMPARISON WITH SEVERAL WELL-ESTABLISHED METHODS ON THE CEC 2017 TESTBED

To adequately highlight the performance of our proposed method, tests on the CEC 2017 benchmarks with dimensionalities of $30 D, 50 D$ and $100 D$ are also performed, and corresponding comparisons with advanced modern algorithms are presented in this subsection. The algorithm considered for comparison with the MLS-EDA here are EMNA $_{\mathrm{g}}$, NRO [10], MRDE [52], RWGEDA [37], ELSHADE-SPACMA

TABLE 9. Parameter settings of the eight algorithms on the CEC 2017 test.


TABLE 10. Comparison results of the WILCOXON signed rank test $(\boldsymbol{\alpha}=0.05)$.

[53], ACoS-JADE [54] and HSES [48]. NRO is a promising physical-based optimizer that performed well in the CEC 2017 test, MRDE is a newly developed DE variant, RWGEDA and ACoS-JADE are two covariance-matrixbased algorithms, and ELSHADE-SPACMA and HSES are the two top performers in the CEC 2018 competitions. The parameter settings of each algorithm are adopted in accordance with the respective original work, as shown in Table 9. All 29 benchmarks in the CEC 2017 testbed are evaluated 51 times with a predefined evaluation number of $D \times 10,000$, where $D=30,50$ and 100. The statistical data, including the mean and SD error values, are presented in Tables 19 to 21, in Appendix G.

As observed in Table 19, the MLS-EDA outperforms the basic EMNA $_{\mathrm{g}}$ in solving the unimodal benchmarks. However, NRO shows great superiority on the $30 D$ test, achieving the best mean values on almost all of the benchmarks except F12, F25 and F28. By contrast, for the $50 D$ test, as shown in Table 20, NRO is significantly affected by the problem dimensionality, whereas HSES achieves first rank in more cases. Our MLS-EDA performs better on F1, F3, F9, F27 and F28. When addressing the $100 D$ problems, HSES and our MLS-EDA are the two best-performing algorithms, as presented in Table 21.

As in the previous experiment, the Wilcoxon signed rank test is carried out to evaluate the pairwise differences between the MLS-EDA and the other competitors, as shown in Table 10. The symbols in this table have same meanings as in Table 6. In the $30 D$ test, our MLS-EDA exhibits performance similar to that of ELSHADE-SPACMA and HSES and surpasses EMNA $_{\mathrm{g}}$, MRDE, RWGEDA and ACoS-JADE, but it is outperformed by NRO. In the $50 D$ and $100 D$ tests, the MLS-EDA achieves a higher ' + ' count than any of the other algorithms except HSES.

Furthermore, the Friedman test is carried out to rank these eight algorithms according to their performance in the tests of all three dimensionalities. Table 11 presents the ranking results based on the Friedman test $(\alpha=0.05)$. According to these ranking values, NRO is the winner on the $30 D$ test and HSES performs the best on the $50 D$ and $100 D$ tests. Although our MLS-EDA is not the best-performing algorithm on any of the three test sets, it shows robust performance earning second place in all three competitions. Moreover, when the SR calculation is used to determine the overall ranking of the eight algorithms, the winner of the CEC 2018 competition, HSES similarly ranks the best in this experiment. Our MLSEDA lags behind HSES by only a small margin, ranking second. Benefiting from its out performance on $30 D$ test, NRO ranks third. The other algorithms rank as follows, from best to worst: ELSHADE-SPACMA, RWGEDA, ACoS-JADE, MRDE and EMNA $_{\mathrm{g}}$.

Fig. 8 illustrates the significant differences between the different algorithms based on the Iman Davenport test. The CD value is 1.3219 . Clearly, the MLS-EDA shows little difference from HSES, NRO and ELSHADE-SPACMA but surpasses RWGEDA, MRDE, ACoS-JADE and EMNA $_{\mathrm{g}}$.

Although HSES achieves the best overall score on the benchmarks in the CEC 2017 test suite, it is not the most efficient method according to the execution time costs reported in Appendix H. Table 12 shows the average amounts of time required by these eight algorithms to solve the benchmarks of different dimensionalities. The differences between the efficiencies of the various algorithms can be more clearly

TABLE 11. Rankings of the eight algorithms on the CEC 2017 testbed based on the Friedman test $(\alpha=0.05)$.


a. The chi-square is $1.28 \mathrm{e}+02$, and the p -value is $1.81 \mathrm{e}-24$.
b. The chi-square is $1.10 \mathrm{e}+02$, and the p -value is $7.59 \mathrm{e}-21$.
c. The chi-square is $1.34 \mathrm{e}+02$, and the p -value is $8.17 \mathrm{e}-26$.

TABLE 12. Mean time costs of the eight algorithms on the CEC 2017 testbed (in second).


TABLE 13. Error values obtained with the MLS-EDA on the CEC 2014 30D, 50D and 100D tests.

seen from the ST results. The basic EMNA $_{\mathrm{g}}$ requires the least time, while the MLS-EDA performs more efficiently than any of the other methods except EMNA $_{\mathrm{g}}$. HSES ranks last with a substantially greater time cost. These findings also reflect a bottleneck problem hindering the development of new algorithms. Better algorithm performance is typically achieved by means of a more complex algorithm structure, which will cause more time to be required to run the algorithm. However, our MLS-EDA shows advantages in both accuracy and speed. Thus, our MLS-EDA, with its new search mechanisms, exhibits competitive performance on the CEC 2017 test suite.

Through the above two experiments, the superiority of the MLS-EDA has been fully demonstrated. Here, we clarify the difference between the MLS-EDA and RWGEDA. These two algorithms have similar execution frameworks, but their search mechanisms are different. In RWGEDA, the random

ELSIADE-SPACMA
![img-7.jpeg](img-7.jpeg)

FIGURE 6. Multiple comparisons based on the post hoc Iman Davenport test.
walk strategies only utilize the best solution to conduct the local search. This feature is not appropriate for our MLS-EDA, as confirmed by its weakness as demonstrated in the above study on parameter sensitivity. Instead, the MLS mechanism that employs more high-quality solutions is more efficient. Furthermore, the newly developed MLS-EDA shows more promising performance than RWGEDA does on the CEC 2014 and CEC 2017 tests in terms of both accuracy and efficiency. In some sense, the MLS-EDA is a superior development of the RWGEDA.

![img-8.jpeg](img-8.jpeg)

FIGURE 9. Convergence performance of the MLS-EDA on the CEC 2014 30D, 50D and 100D tests.

![img-9.jpeg](img-9.jpeg)

FIGURE 9. (Continued) Convergence performance of the MLS-EDA on the CEC 2014 30D, 50D and 100D tests.

TABLE 14. Error values obtained with the MLS-EDA ON the CEC 2017 30D, 50D and 100D tests.


![img-10.jpeg](img-10.jpeg)

FIGURE 10. Convergence performance of the MLS-EDA on the CEC 2017 30D, 50D and 100D tests.

![img-11.jpeg](img-11.jpeg)
![img-12.jpeg](img-12.jpeg)
(b) Multimodal functions F4 to F10
![img-13.jpeg](img-13.jpeg)

FIGURE 10. (Continued) Convergence performance of the MLS-EDA on the CEC 2017 30D, 50D and 100D tests.
TABLE 15. Mean errors obtained from seven algorithms on the CEC 201430 D TEST.

TABLE 16. Mean errors obtained from seven algorithms on the CEC 2014 S0D test.

TABLE 17. Mean errors obtained from seven algorithms on the CEC 2014100D test.


TABLE 18. Comparison of the computational efficiencies of the seven algorithms on the CEC 2014 test suite.

TABLE 19. Mean errors obtained from eight algorithms on the CEC 2017302I test.


## IV. CONCLUSION

As a novel extension of EDA, the framework of our proposed MLS-EDA based on DES and MLS mechanisms is described in this paper. Based on experimental evaluation, the optimal algorithm parameter values are discussed,
and the efficiency of the developed search mechanisms in improving the behavior of the algorithm is verified, demonstrating that our modifications play an active role in improving the algorithm performance and avoiding premature convergence.

TABLE 20. Mean errors obtained from eight algorithms on the CEC 2017 S0D test.


TABLE 21. Mean errors obtained from eight algorithms on the CEC 2017100D test.

The optimization ability of our MLS-EDA has been benchmarked using the CEC 2014 and CEC 2017 test suites. Both experiments are carried out using 30D, 50D and 100D problems. According to the statistical results,
our MLS-EDA shows high efficiency and accuracy in both test suites. Moreover, our method shows competitiveness performance relative to other top-performing algorithms,

TABLE 32. Comparison of the computational efficiencies of the eight algorithms on the CEC 2017 test suite.


Two possibilities should be addressed in future work. First, the MLS mechanism used in the MLS-EDA is an efficient local exploration method that can also be employed to enhance the performance of other algorithms. Second, although our MLS-EDA has shown promising performance in addressing small- and medium-scale problems in this study, the time complexity of MLS-EDA, which is related to the problem dimensionality, will limit its applicability in high-dimensional cases. Developing a more efficient EDA framework with a lower time complexity will require further investigation.

## APPENDIXES APPENDIX A

See Table 13.

## APPENDIX B

See Figure 9.

## APPENDIX C

See Table 14.

## APPENDIX D

See Figure 10.

## APPENDIX E

EXPERIMENTAL RESULTS ACHIEVED BY THE MLS-EDA, EMNA $_{8}$, RWGEDA, DOLTLBO, VCS, CPI-JADE AND L-SHADE ON THE CEC 2014 TEST SUITE

See Tables 19-17.

## APPENDIX H COMPARISON OF THE COMPUTATIONAL COSTS OF THE EIGHT METHODS ON THE CEC 2017 TEST SUITE

See Table 22.
