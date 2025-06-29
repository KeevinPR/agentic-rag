# Accepted Manuscript 

Anisotropic Adaptive Variance Scaling for Gaussian Estimation of Distribution Algorithm

Zhigang Ren, Yongsheng Liang, Lin Wang, Aimin Zhang, Bei Pang, Biying Li

PII:
DOI:
Reference:
S0950-7051(18)30052-2
10.1016/j.knosys.2018.02.001

KNOSYS 4209

To appear in:
Knowledge-Based Systems

Received date:
12 September 2017
Revised date:
25 January 2018
Accepted date:
1 February 2018

Please cite this article as: Zhigang Ren, Yongsheng Liang, Lin Wang, Aimin Zhang, Bei Pang, Biying Li, Anisotropic Adaptive Variance Scaling for Gaussian Estimation of Distribution Algorithm, Knowledge-Based Systems (2018), doi: 10.1016/j.knosys.2018.02.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# [Title Page] 

## Anisotropic Adaptive Variance Scaling for Gaussian Estimation of Distribution Algorithm

Zhigang Ren ${ }^{\mathrm{a}}$, Yongsheng Liang ${ }^{\mathrm{a}}$, Lin Wang ${ }^{\mathrm{b}}$, Aimin Zhang ${ }^{\mathrm{a}}$, Bei Pang ${ }^{\mathrm{a}}$, Biying $\mathrm{Li}^{\mathrm{a}}$<br>${ }^{a}$ Department of Automation Science and Technology, School of Electronic and Information Engineering,<br>Xi'an Jiaotong University, Xi'an, China<br>${ }^{\mathrm{b}}$ School of Information Science and Technology, Northwest University, Xi'an, China

## Correspondence information:

Corresponding author name: Zhigang Ren
Affiliation: Department of Automation Science and Technology, School of Electronic and Information Engineering, Xi'an Jiaotong University

Permanent address: No. 28 Xianning West Road, Xi'an Shaanxi, 710049, P.R. China
Email address: renzg@mail.xjtu.edu.cn
Telephone number: +86 14630237679
![img-0.jpeg](img-0.jpeg)

# Anisotropic Adaptive Variance Scaling for Gaussian Estimation of Distribution Algorithm 

Zhigang Ren ${ }^{\mathrm{a}, *}$, Yongsheng Liang ${ }^{\mathrm{a}}$, Lin Wang ${ }^{\mathrm{b}}$, Aimin Zhang ${ }^{\mathrm{a}}$, Bei Pang ${ }^{\mathrm{a}}$, Biying $\mathrm{Li}^{\mathrm{a}}$<br>${ }^{a}$ Department of Automation Science and Technology, School of Electronic and Information Engineering, Xi'an Jiaotong University, Xi'an, China<br>${ }^{\mathrm{b}}$ School of Information Science and Technology, Northwest University, Xi'an, China


#### Abstract

Traditional Gaussian estimation of distribution algorithms (EDAs) are confronted with issues that the variable variances decrease fast and the main search direction tends to become perpendicular to the improvement direction of the fitness function, which reduces the search efficiency of Gaussian EDAs (GEDAs) and makes them subject to premature convergence. In this paper, a novel anisotropic adaptive variance scaling (AAVS) technique is proposed to improve the performance of traditional GEDAs and a new GEDA variant named AAVS-EDA is developed. The advantages of AAVS over the existing variance scaling strategies lie in its ability for tuning the variances and main search direction of GEDA simultaneously, which are achieved by anisotropically scaling the variances along different eigendirections based on corresponding landscape characteristics captured by a simple topology-based detection method. Besides, AAVS-EDA also adopts an auxiliary global monitor to ensure its convergence by shrinking all the variances if no improvement is achieved in a generation. The evaluation results on 30 benchmark functions of CEC2014 test suite demonstrate that AAVS-EDA possesses stronger global optimization efficiency than traditional GEDAs. The comparison with other state-of-the-art evolutionary algorithms also shows that AAVS-EDA is efficient and competitive.


Keywords: Gaussian estimation of distribution algorithm; premature convergence; search direction; anisotropic adaptive variance scaling

[^0]
[^0]:    * Corresponding author. E-mail address: renzg@mail.xjtu.edu.cn

# 1. Introduction 

As a special class of evolutionary algorithm (EA) [1], estimation of distribution algorithm (EDA) [2-4] is characterized by the way of generating new solutions, i.e., sampling solutions according to a probability distribution, but not through crossover and mutation operators as other kinds of EAs. The probability distribution employed in each generation is generally estimated from the relatively high-quality solutions obtained in previous generations. It can capture the structure of the problem being solved to a certain extent and consequently guide the algorithm to more promising solution regions. During the past few decades, EDAs attracted much research effort and achieved great success in both combinatorial and continuous domains [5,6]. In this paper, EDAs for continuous domain are studied.

Continuous EDAs usually adopt Gaussian probability model [3,4] and histogram model [7] as the basic probability model. According to the way in representing variable dependencies, Gaussian models for EDAs can be further categorized into three kinds. The simplest one is the univariate model which neglects all the variable dependencies. A representative algorithm with this type of model is the univariate marginal distribution algorithm (UMDA ${ }_{c}$ ) [3,4]. A slightly more sophisticated model is the one that just considers some important variable dependencies. To identify these dependencies, Bayesian factorization is usually employed $[3,8]$. The multivariate model takes all the variable dependencies into account. A representative algorithm of this type is estimation of multivariate normal density algorithm $\left(\mathrm{EMNA}_{\mathrm{z}}\right)[4]$.

Although possessing clear physical concept, traditional Gaussian EDAs (GEDAs) often suffer from premature convergence [8,11-15]. Early improvement studies attributed this defect to the rapid shrink of variances and developed many variance scaling strategies. Ocenasek et al. [8] proposed a variance adaption operator for the mixed Bayesian optimization algorithm [9] based on the well-known 1/5-success-rule [10]. Yuan and Gallagher [11] claimed that the performance of GEDA could be improved on certain problems by compulsively keeping the variances at a value of at least 1. Pošík [12] suggested enlarging variances by a

constant factor. Grahl et al. [13] proposed an adaptive variance scaling (AVS) strategy which increases the variances when the best solution improves, otherwise reduces them. Nevertheless, AVS does not directly tune variances in each generation unless it identifies that the algorithm is traversing a slope. To achieve this, Grahl and his coworkers successively developed two identification strategies, i.e., the strategies based on correlation triggering [13] and standard deviation ratio (SDR) [14]. Cai et al. [15] developed a different type of variance scaling method named cross entropy adaptive variance scaling, which calculates the scaling factor by minimizing the cross entropy between the current probability model and the predicted model for the next generation.

Besides directly tuning variances, some researchers achieved variance scaling by modifying the eigenvalues of the estimated covariance matrix. Wagner et al. [16] proposed an eigenspace EDA (EEDA) which adjusts variances by replacing the minimum eigenvalue with the maximum one. Dong et al. [17] developed an eigen decomposition framework for multivariate GEDA and claimed that most variance scaling methods by then could be unified within their framework by applying different eigenvalue tuning strategies. Liu et al. [18] introduced principal component analysis into EDA (PCA-EDA) and tried to avoid premature convergence by regulating the maximum eigenvalue.

It is easily comprehensible that the efficiency of GEDA depends not only on its search scope, but also on its search directions. Unfortunately, it has been shown that, without fine intervention, the main search direction of GEDA tends to become perpendicular to the fitness improvement direction [15,19], which greatly reduces its search efficiency. To remedy this defect, some researchers made beneficial attempts by improving the estimation method for the covariance matrix. The covariance matrix adaptation evolution strategy (CMA-ES) [20], which can be considered as a special EDA, employs a sophisticated covariance matrix estimation method, where the rank- $\mu$-update operator updates the covariance matrix using the weighted high-quality solutions in the current generation and the corresponding mean in the last generation. By this means, the variance along the gradient direction can be increased. Bosman et al. [19] proposed an

anticipated mean shift (AMS) operator which estimates the covariance matrix by shifting part of selected solutions along the anticipated gradient direction such that the main search direction can be corrected to a certain extent. Bosman et al. integrated AVS, SDR and AMS together and developed a powerful EDA variant known as AMaLGaM [19]. Ren et al. [21] improved the original AMS operator by directly shifting the mean of selected solutions and taking the shifted mean as the center when estimating the covariance matrix. Liang et al. [22] recently reported an enhanced GEDA, in which the inferior solutions in current generation are repaired and utilized to estimate the covariance matrix such that the search directions could be adaptively adjusted.

In addition to scaling variances and improving the covariance matrix estimation method, extensive efforts have been made to enhance the performance of EDA. Xu [23] combined EDA with chaos perturbation operator for the purpose of enhancing the population diversity. Chen et al. [24] proposed a fast interactive EDA which extracts user's preference on the decision variables from historical information to reduce the initial search space to a preferred subspace such that the search process can be accelerated. Fang et al. [25] developed a mean shift strategy to speed up the convergence of EDA. Zhou et al. [7] suggested combining EDA with cheap and expensive local search. Auger and Hansen [26] developed a restart CMA-ES with increasing population size (IPOP-CMAES). Although IPOP-CMAES was developed a decade years ago, it was recently reported that IPOP-CMAES is still competitive with many other state-of-the-art EAs proposed in recent years [27]. Karahenas et al. [28] investigated the effect of regularization method on the model learning process of GEDA. Santana et al. [29] tried to improve EDA with the help of new selection strategies. Instead of using Gaussian and histogram model, [30-32] adopted particle filter, Copula theory and probabilistic graphical model, respectively, to capture the distribution of good solutions. Aiming at seeking multiple solutions, the techniques of detecting promising areas [33] and niching [34,35] were introduced to EDA to enhance its performance on multimodal problems. Moreover, EDAs have been integrated with other EAs like particle swarm optimization (PSO) [36] and differential evolution (DE) [37] to fuse their

advantages together. Theoretical researches have also been done to characterize the behaviors of EDA. Rastegar [38] analyzed the convergence probability of two univariate EDAs and showed a sufficient condition for the convergence. Echegoyen et al. [39] comprehensively studied the relationship between the behaviors of EDA and the solution space of optimization problems.

To sum up, EDAs have been improved significantly in the past decades, but there are still some shortcomings. So far, most existing variance scaling strategies are able to adjust the search scope of GEDA, but can hardly change its search directions. This is one of the key issues that severely restrict the performance of GEDA, but has not been fully recognized and studied. Consequently, few related work was reported in recent years. CMA-ES and AMaLGaM achieve great success by comprehensively regulating their search scopes and directions. However, their algorithmic frameworks are so complex that it is too difficult for practitioners to understand the mechanisms therein, not to mention setting corresponding parameters. As for some other EDA variants, their performance also highly depends on the search efficiency of basic EDA, then it is hopeful that they would be further improved if the efficiency of EDA can be increased.

Taking enhancing EDA with some simple operations as the goal, this paper proposes an anisotropic adaptive variance scaling (AAVS) strategy and develops a novel GEDA variant named as AAVS-EDA. Different from most existing variance scaling strategies which adjust all the variances by a same factor, AAVS first captures the landscape of the problem being solved along each eigendirection with a simple topology-based detection method, then adaptively tunes the variances along different directions according to the corresponding detection results. If a slope is detected along an eigendirection, then AAVS enlarges the corresponding variance. On the contrary, if a valley is detected, then AAVS keeps the corresponding variance unchanged. By this means, the search speed along a slope can be quickened, and the fine search around a valley can be achieved. More importantly, profiting from its anisotropic scaling, AAVS is able to make the main search direction of EDA naturally become consistent with the fitness improvement direction.

To ensure convergence, AAVS-EDA also adopts an auxiliary global monitor which shrinks all the variances if no improvement is achieved in a generation. Thanks to these fine properties, AAVS-EDA shows desirable performance on a variety of benchmark functions.

The remainder of this paper is organized as follows. Section 2 briefly reviews the basic knowledge of GEDA. Section 3 describes AAVS and the resulting AAVS-EDA in detail. Section 4 presents the experiment settings and analyzes the experiment results. The conclusions are finally drawn in Section 5.

# 2. Basic Knowledge of GEDA 

As a model-based EA, EDA assumes that good solutions approximately obey a certain probability distribution over the solution space. During the search process, it tries to learn this distribution and generate new solutions according to the learning results [2-4]. The general framework of EDA is outlined in

## Algorithm 1.

EDA usually starts with an initial population which is filled with some randomly generated solutions. After the evaluation, those relatively good solutions are selected generally according to a truncation selection rule. Then a new probability model is built to produce solutions for the next generation. EDA executes this iterative process of evaluation, selection, model building, and solution sampling until meeting the stopping criterion.

[^0]
[^0]:    Algorithm 1. The general framework of EDA.
    1: Initialize parameters, set $t=0$ and generate initial population $\boldsymbol{P}^{t}$;
    2: Evaluate population $\boldsymbol{P}^{t}$ and update the best solution $\boldsymbol{b}^{t}$ obtained so far;
    3: Output $\boldsymbol{b}^{t}$ if the stopping criterion is met;
    4: Select promising solutions $\boldsymbol{S}^{t}$ from $\boldsymbol{P}^{t}$;
    5: Build a probability model $G^{t+1}$ based on $\boldsymbol{S}^{t}$;
    6: Generate a new population $\boldsymbol{P}^{t+1}$ by sampling from $G^{t+1}$;
    7: Set $t \leftarrow t+1$, goto step 2 .

Continuous EDAs generally employ Gaussian model as the basic probability distribution model. The Gaussian probability density function for an $n$-dimensional random vector $\boldsymbol{x}$ can be parameterized by its mean $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{C}$ as follows:

$$
G_{(\boldsymbol{\mu}, \boldsymbol{C})}(\boldsymbol{x})=\frac{(2 \pi)^{-n / 2}}{(\operatorname{det} \boldsymbol{C})^{1 / 2}} \exp \left(-(\boldsymbol{x}-\boldsymbol{\mu})^{\mathrm{T}}(\boldsymbol{C})^{-1}(\boldsymbol{x}-\boldsymbol{\mu}) / 2\right)
$$

The mean vector and the covariance matrix totally have $0.5 n^{2}+1.5 n$ free parameters, which are generally estimated from the selected solutions using the maximum likelihood (ML) estimation method. For a selected solution set $\boldsymbol{S}$, the ML estimations of $\boldsymbol{\mu}$ and $\boldsymbol{C}$ are

$$
\begin{aligned}
& \bar{\mu}=\frac{1}{|\boldsymbol{S}|} \sum_{i=1}^{|\mathrm{M}|} \boldsymbol{S}_{i} \\
& \overline{\boldsymbol{C}}=\frac{1}{|\boldsymbol{S}|} \sum_{i=1}^{|\mathrm{M}|}\left(\boldsymbol{S}_{i}-\overline{\boldsymbol{\mu}}\right)\left(\boldsymbol{S}_{i}-\overline{\boldsymbol{\mu}}\right)^{\mathrm{T}}
\end{aligned}
$$

The Gaussian model estimated by Eqs. (2) and (3) takes the dependencies between all pairs of variables into account. It ensures rotation-invariance and is capable of capturing some complex structure characteristics of the solution space [19], hence is widely used by existing GEDAs.

Once $\overline{\boldsymbol{\mu}}$ and $\overline{\boldsymbol{C}}$ are obtained, the search characteristics of GEDA are determined. They can be geometrically described by a probability density ellipsoid (PDE) related with $\overline{\boldsymbol{\mu}}$ and $\overline{\boldsymbol{C}}$ [40]. As shown in Fig. 1, PDE takes $\overline{\boldsymbol{\mu}}$ as its center which is also the search center of GEDA. The axis directions of PDE are accordant with the eigendirections of $\overline{\boldsymbol{C}}$. They determine the search directions of GEDA. The axis lengths of PDE, i.e., the standard deviations along eigendirections, equal the square roots of corresponding eigenvalues. They determine the search scope of GEDA.

From Fig. 1, it can be seen that the good solutions selected in each generation are mainly located within a semiellipsoid which is the intersection of the current PDE and a function contour surface determined by the selection rule. The major axis of this semiellipsoid tends to parallel to the corresponding function contour surface, so does the major axis of the PDE estimated by the solutions within the semiellipsoid. This means

that the major axis of the new PDE, i.e., the main search direction of GEDA, will gradually become perpendicular to the fitness improvement direction. On the other hand, the solutions within the semiellipsoid are mainly distributed in the region near the center of the current PDE, then the new PDE estimated by these solutions will naturally shrink. With improper search directions and rapid shrinking search scope, traditional GEDA certainly cannot achieve desirable optimization results.
![img-1.jpeg](img-1.jpeg)

Fig.1. Schematic for the change of PDE in traditional GEDA
Based on the above explanation, it is easy to understand that if we enlarge the search scope with most existing AVS strategies which generally multiply the covariance matrix by a factor [13], the relative magnitudes of eigenvalues remain unchanged, then the ill-shaped PDE cannot be adjusted. EEDA and PCAEDA achieve variance scaling by regulating the minimum eigenvalue and the maximum one, respectively. They can indeed adjust the shape of PDE, but may waste part of search effort in the futile search directions or make the main search direction too aggressive.

# 3. GEDA with Anisotropic Adaptive Variance Scaling 

The proposed AAVS-EDA follows the basic framework of EDA, but contains two distinctive algorithmic strategies, i.e., AAVS and an auxiliary global monitor. This section will present them in sequence and then give the complete procedure of AAVS-EDA.

# 3.1 Anisotropic adaptive variance scaling 

From the discussion in section 2, it can be known that the reason for the low efficiency of most existing AVS strategies lies in that they emphasize adjusting the search scope of GEDA, but consider little about its search directions. Different from them, AAVS takes both search elements into account. It is a common view that the local landscape of a problem can be characterized by a slope or a valley [12-14], and if a slope is detected, enlarging variances will facilitate quickening the search process. However, it is improper to brusquely claim an algorithm is searching a slope or a valley. Taking the situation shown in Fig. 1 as an example, GEDA is searching a slope along the minor axis of PDE, but is searching a valley along the major axis since the solutions along this axis become worse as they move away from the center. Therefore, it makes sense that the variances along different eigendirections should be adaptively adjusted according to corresponding landscapes. AAVS achieves this in the following way:

First, eigendirections are obtained by conducting eigendecomposition on the initially estimated covariance matrix $\overline{\boldsymbol{C}}$. From Eq. (3), it can be seen that $\overline{\boldsymbol{C}}$ is a real symmetric matrix, then it is nonnegative definite and can be decomposed as follows:

$$
\overline{\boldsymbol{C}}=\boldsymbol{V} \boldsymbol{D} \boldsymbol{V}^{\mathrm{T}}
$$

where $\boldsymbol{V}=\left[\boldsymbol{v}_{1}, \boldsymbol{v}_{2}, \ldots, \boldsymbol{v}_{n}\right]$ with each column $\boldsymbol{v}_{i}(i=1,2, \ldots, n)$ representing a eigenvector of $\overline{\boldsymbol{C}}$, $\boldsymbol{D}=\operatorname{diag}\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n}\right)$ with each $\lambda_{i}(i=1,2, \ldots, n)$ representing the eigenvalue corresponding to $\boldsymbol{v}_{i}$. According to the property of Gaussian distribution, it can be known that $\lambda_{i}$ equals the variance along the direction of $\boldsymbol{v}_{i}$.

To detect the local landscape of a problem, several detection methods have been developed [33-35,41]. The most widely used one is the topology-based hill-valley method [41]. Its key idea consists in that, for a line segment connecting two solution points $\boldsymbol{r}$ and $\boldsymbol{l}$, if there exists a point $\boldsymbol{m}$ on the line segment $\boldsymbol{r l}$ whose fitness value is better than those of both $\boldsymbol{r}$ and $\boldsymbol{l}$, then a valley along the line segment $\boldsymbol{r l}$ is identified. However, it is impractical to directly apply hill-valley method in AAVS since it requires many sample

points. Considering that the estimated mean $\overline{\boldsymbol{\mu}}$ lies in the center of the PDE and is the common point connecting all the eigendirections, AAVS examines the solution points on both sides of $\overline{\boldsymbol{\mu}}$ along each eigendirection instead of examining the interior points connecting two given points. Concretely, for each eigendirection $\boldsymbol{v}_{i}(i=1,2, \ldots, n)$, AAVS generates two symmetrical points centered on $\overline{\boldsymbol{\mu}}$ as follows:

$$
\left\{\begin{array}{l}
\boldsymbol{l}_{i}=\overline{\boldsymbol{\mu}}-\delta_{i} \boldsymbol{v}_{i} \\
\boldsymbol{r}_{i}=\overline{\boldsymbol{\mu}}+\delta_{i} \boldsymbol{v}_{i}
\end{array}\right.
$$

where $\delta_{i}$ denotes the sampling step size along $\boldsymbol{v}_{i}$. Taking $\overline{\boldsymbol{\mu}}$ as an interior point connecting $\boldsymbol{l}_{i}$ and $\boldsymbol{r}_{i}$, AAVS considers a slope is identified along $\boldsymbol{v}_{i}$ if $\boldsymbol{l}_{i}, \boldsymbol{r}_{i}$ and $\overline{\boldsymbol{\mu}}$ satisfy:

$$
\min \left\{f\left(\boldsymbol{l}_{i}\right), f\left(\boldsymbol{r}_{i}\right)\right\}<f(\overline{\boldsymbol{\mu}})<\max \left\{f\left(\boldsymbol{l}_{i}\right), f\left(\boldsymbol{r}_{i}\right)\right\}
$$

where $f(\cdot)$ represents the fitness function of the problem being solved.
According to some preliminary experimental results, it is found that the sampling step size $\delta_{i}$ has great influence on the structure learning results and it is difficult to set a fixed value to adapt different eigendirections and different search situations. To alleviate this issue, AAVS sets $\delta_{i}$ in a random way, i.e., samples a value for each eigendirection $\boldsymbol{v}_{i}$ from the corresponding single dimensional Gaussian distribution $N\left(0, \lambda_{i}\right)$. It is worth to mention that, with this setting, AAVS cannot ensure to provide the right detection results every time, but this setting still makes sense that it facilitate AAVS getting helpful structure information in most cases since AAVS mainly focuses on examining local structure of a single dimensional subspace and the randomly generated $\delta_{i}$ can cover the local solution region well.

For each eigendirection $\boldsymbol{v}_{i}$, if a slope is identified, then AAVS enlarges the corresponding eigenvalue $\lambda_{i}$ for the purpose of encouraging further exploration and quickening the search process. On the other hand, if a valley is identified, AAVS keeps the corresponding eigenvalue unchanged, so that the excellent performance of GEDA on valley-like regions can be preserved. Formally, each $\lambda_{i}(i=1,2, \ldots, n)$, i.e., the variance along each eigendirection, is tuned as follows:

$$
\lambda_{i} \leftarrow \begin{cases}\alpha \cdot \lambda_{i}, & \text { if a slope is detected along } v_{i} \\ \lambda_{i}, & \text { otherwise }\end{cases}
$$

where $\alpha$ is a scaling factor greater than 1 . A smaller value of $\alpha$ makes no significant influence. On the contrary, a larger value of $\alpha$ encourages faster exploration speed along an eigendirection, but may cause serious imbalance among different directions. We will discuss the influence of $\alpha$ in detail in section 4.1.

```
Algorithm 2. The pseudocode of AAVS
    1: Perform eigendecomposition on \(\overline{\boldsymbol{C}}: \overline{\boldsymbol{C}}=\boldsymbol{V D V}^{\mathrm{T}}\);
    2: Evaluate \(\bar{\mu}\);
    3: For each eigenvector \(\boldsymbol{v}_{i}(i=1,2, \ldots, n)\)
    4: Sample step size \(\delta_{i}\) from \(N\left(0, \lambda_{i}\right)\);
    5: Sample two solutions \(I_{i}\) and \(r_{i}\) according to Eq. (5) and evaluate them;
6: Detect local landscape based on \(I_{i}, r_{i}\) and \(\bar{\mu}\) and Eq. (6);
7: If a slope is identified
8: \(\quad \lambda_{i} \leftarrow \alpha \cdot \lambda_{i}\);
9: End if
10: End for
```

Algorithm 2 lists the pseudocode of AAVS, where three remarks need to be highlighted. First, AAVS tunes all the variances independently and adaptively according to the detection results along corresponding eigendirections. This is also the reason why we name it anisotropic adaptive variance scaling. Second, a single run of AAVS does not change the eigendirections of $\overline{\boldsymbol{C}}$, but running AAVS in successive generations can reshape PDE such that the major axis of PDE would gradually become consistent with the fitness improvement direction. The main reason lies in that slopes provide the main fitness improvement directions, AAVS enlarges the axes along slopes, and the new sampled solutions around these axes are more likely to be selected to estimate the new covariance matrix, which further makes this kind of axes approach to the fitness improvement directions. As a result, the search efficiency of GEDA can be substantially increased. Finally, the excellent performance of AAVS is obtained at the cost of sampling two additional solutions for detecting the local landscape along each eigendirection. Nevertheless, the additional sampling quantity is acceptable compared with the general setting of population size in multivariate GEDA.

![img-2.jpeg](img-2.jpeg)

Fig. 2. PDE and the generated solutions: (a) current PDE, (b) PDE tuned by traditional AVS and (c) PDE tuned by AAVS.

To demonstrate the effectiveness of AAVS in adjusting PDE, a schematic experiment is designed. Suppose GEDA is employed to minimize a two dimensional function $f(\boldsymbol{x})=x_{0}^{2}+x_{1}^{2}$ and the search range is set to $[0,8] \times[0,8]$. Fig. 2(a) shows the contour map of this test function, together with the PDE of the current Gaussian distribution and the solutions generated by it. It is clear that the fitness landscape along the direction $x_{0}=x_{1}$ is a slope, the one along the direction $x_{0}=-x_{1}$ is a valley, and the current PDE is illshaped. After applying the traditional AVS and the new proposed AAVS, the resulting PDEs and the new solutions generated by them are shown in Fig. 2(b) and Fig. 2(c). It can be seen from Fig. 2(b) that when traditional AVS are employed, variances along both directions are increased. As a result, the exploration range of GEDA is enlarged, but most solutions are generated along the direction $x_{0}=-x_{1}$ since the PDE is still ill-shaped. When AAVS is applied as shown in Fig. 2(c), only the variance along the direction $x_{0}=x_{1}$ is increased since a slope can be detected along this direction. As a result, PDE is reshaped to a certain extent and more solutions are generated along the fitness improvement direction.

# 3.2 Global monitor 

As illustrated above, AAVS indeed facilitates enhancing the search efficiency of GEDA. However, it is found that if exclusively performed, AAVS may sometimes cause GEDA unable to converge. The reason is twofold: First, AAVS occasionally provides the wrong detection results since it makes the detection decision just based on three solution points. Second, the optimal solutions of some problems are located at the intersection between a slope and the search boundary. For both cases, enlarging variances is ineffectual, especially at the late searching stage.

As it is difficult to overcome the defects mentioned above point to point, here we remedy them with a global monitor. Its key idea lies in that no matter under what circumstance the variances are improperly enlarged, GEDA could hardly get better solutions, then we just need to reduce all the variances in these cases. To be specific, the global monitor first calculates the average fitness value of the selected solutions (AFV) in each generation as follows:

$$
\mathrm{AFV}=\frac{1}{|\boldsymbol{S}|} \sum_{i=1}^{|\boldsymbol{S}|} f\left(\boldsymbol{S}_{i}\right)
$$

then shrinks all the variances if AFV is not improved compared with the one in the last generation:

$$
\boldsymbol{D} \leftarrow\left\{\begin{array}{l}
\boldsymbol{D}, \quad \text { if } \mathrm{AFV} \text { is improved } \\
\beta \cdot \boldsymbol{D}, \text { otherwise }
\end{array}\right.
$$

where $\beta$ is a shrinking factor. Considering that AAVS enlarges the variances along slopes by a factor of $\alpha$, then the convergence of GEDE can be guaranteed if $\beta$ is limited within $(0,1 / \alpha]$. We suggest setting $\beta=1 / \alpha$ for simplicity. It is notable that the selected solutions have been evaluated at the selection phase, thus the calculation of AFV is very straightforward. In addition, compared with AVS that just examines the improvement of the best solution obtained so far, AFV can provide much more stable result. Fig. 3 illustrates the relationship between AAVS and the global monitor. For an decomposed covariance matrix $\overline{\boldsymbol{C}}$, its eigenvalue matrix $\boldsymbol{D}$ is first adjusted by AAVS. Then the global monitor checks whether AFV is improved. If it is not, the global monitor shrinks $\boldsymbol{D}$ before outputting it.

![img-3.jpeg](img-3.jpeg)

Fig. 3. The relationship between AAVS and the global monitor.

# 3.3 The procedure of AAVS-EDA 

AAVS and the global monitor can be easily integrated into the traditional GEDA. The detailed procedure of the resulting EDA variant AAVS-EDA is described in Algorithm 3. It should be noted that AAVS-EDA employs the commonly used truncation selection rule in step 5, and just generates $p-1$ new solutions for a population of size $p$ in step 10 since it maintains the best solution in each generation to the next generation. It can be known that the computation complexity of AAVS and the global monitor is $O(n)$ while the computation complexity for estimating the covariance matrix is $O\left(n^{2}\right)$. Therefore, the overall computation complexity of AAVS-EDA is not greater than that of the traditional multivariate GEDAs.

## Algorithm 3. The procedure of AAVS-EDA.

1: Initialize population size $p$ 'truncation ratio $\tau$ and scaling factor $\alpha$;
2: Set $t=0$, generate initial population $\boldsymbol{P}^{i}$ randomly;
3: Evaluate population $\overline{\boldsymbol{P}^{i}}$ and update the best solution $\boldsymbol{b}^{i}$ obtained so far;
4: Output $\boldsymbol{b}^{i}$ if the stopping criterion is met;
5: Select the best $\lfloor\tau p\rfloor$ solutions in $\boldsymbol{P}^{i}$ and store them in $\boldsymbol{S}^{i}$;
6: Estimate mean $\overline{\boldsymbol{\mu}}^{t+1}$, covariance matrix $\overline{\boldsymbol{C}}^{t+1}$ according to $\boldsymbol{S}^{i}$ and Eqs. (2) and (3);
7: Tune $\overline{\boldsymbol{C}}^{t+1}$ according to AAVS described by Algorithm 2;
8: Tune $\overline{\boldsymbol{C}}^{t+1}$ according to the global monitor described by Eqs. (8) and (9);
9: Build a probability model $G^{t+1}$ based on $\overline{\boldsymbol{\mu}}^{t+1}$ and $\overline{\boldsymbol{C}}^{t+1}$;
10: Generate $p-1$ new solutions by sampling from $G^{t+1}$ and store them into $\boldsymbol{A}^{t+1}$;
11: Set $\boldsymbol{P}^{t+1} \leftarrow \boldsymbol{A}^{t+1} \ldots \boldsymbol{b}^{t}$;
12: Set $t \leftarrow t+1$, goto step 3 .

# 4. Experimental study 

This section aims to experimentally investigate the influences of parameters, the effectiveness of AAVS and the auxiliary global monitor, and the efficiency of AAVS-EDA. To achieve this, CEC2014 test suite was employed [42]. It contains 30 benchmark functions (denoted as $f_{1} \cdot f_{30}$ ) which can be classified into four kinds: $f_{1} \cdot f_{3}$ are unimodal functions, $f_{4} \cdot f_{16}$ are simple multimodal functions, $f_{17} \cdot f_{22}$ are hybrid functions and $f_{23} \cdot$ $f_{30}$ are composition functions. These functions are all single-objective minimization problems and their detailed description can be found in the literature [42]. In our experiments, the dimension of each test function was set to 30 , the allowed maximum number of function evaluations (FEs) was conventionally set to $300,000,25$ independent runs were conducted for each function, and the performance of an algorithm on each function was evaluated according to the function error value (FEV) of the best solution obtained, i.e., the difference between its objective value and that of the global optimal solution. Note that, for AAVS-EDA, the number of FEs consumed by AAVS was also counted into the allowed FE number, and for all the algorithms tested, the FEVs smaller than $10^{-8}$ were seen as zero.

### 4.1 Influences of parameters

There are three parameters in AAVS-EDA, including population size $p$, selection ratio $\tau$ and the enlarging factor $\alpha$. As for $p$ and $\tau$, they are common parameters of most GEDAs and their influences have been extensively studied [4,19]. In AAVS-EDA, we directly set them as $p=1000$ and $\tau=0.35$ which are conventional values adopted by other GEDAs. This section mainly focuses on investigating the influence of enlarging factor $\alpha$. We tested AAVS-EDA on a variety of benchmark functions with different $\alpha$ values varying from 1.5 to 2.5 at an interval of 0.1 . Taking unimodal function $f_{2}$, multimodal function $f_{6}$ and hybrid function $f_{18}$ as examples, Fig. 4 shows the performance variation of AAVS-EDA with respect to $\alpha$.

![img-4.jpeg](img-4.jpeg)

Fig. 4. Performance of AAVS-EDA with different $\alpha$ values on (a) $f_{2}$, (b) $f_{6}$ and (c) $f_{18}$.

From Fig. 4, three observations can be made: 1) When $\alpha$ changes from 1.5 to 2.5 , the variations of average FEVs obtained by AAVS-EDA on each function are all within an order of magnitude, which means that the performance of AAVS-EDA has certain robustness to the change of $\alpha$; 2) AAVS-EDA performs pretty well on $f_{2}$ and $f_{6}$ within a wide range of $\alpha$, but performs slightly worse when $\alpha$ becomes larger than 2.3 and 1.8 , respectively; 3) The performance of AAVS-EDA on the hybrid function $f_{18}$ does not show significant variation trend when $\alpha$ varies. In order to balance the performance of AAVS-EDA on different kinds of functions, we suggest setting $\alpha$ within the range $(1.5,1.8)$. In the experiments described below, it was set to 1.7 .

# 4.2 Effectiveness of AAVS and the global monitor 

To verify the effectiveness of AAVS and the auxiliary global monitor, we compared AAVS-EDA with $\mathrm{EMNA}_{g}$ [4] which is a representative of traditional multivariate GEDA. Both algorithms share the same algorithmic components except for AAVS and the auxiliary global monitor. To achieve a fair comparison, the population size and the selection ratio of $\mathrm{EMNA}_{g}$ were all set the same as those of AAVS-EDA. Besides FEV, another two indicators were adopted to show the performance differences between AAVS-EDA and $\mathrm{EMNA}_{g}$, including the length of PDE's major axis and the cosine value of the acute angle (denoted as $\theta$ ) between PDE's major axis and the steepest descent direction of the test function. Here the steepest descent

direction is defined as the direction from PDE's center to the global optimal solution. These two new indicators reflects the search scope and the main search direction of GEDA to a great extent, respectively. Figs. $5 \sim 7$ present the corresponding evolution curves, where functions $f_{2}, f_{6}$ and $f_{18}$ are taken as examples.

It can be observed from Fig. 5 that, for all the three functions, the length of the major axis derived from AAVS-EDA is always larger than that of $\mathrm{EMNA}_{g}$ in their early search stages, which means that AAVS indeed endows AAVS-EDA with stronger exploration ability. This facilitates AAVS-EDA keeping larger search scope and locking the global optimal solution region. For functions $f_{2}$ and $f_{6}$, AAVS-EDA rapidly shrinks its search scope in the middle search stage since no slope can be detected any more, which enables AAVS-EDA to conduct fine search within the locked solution regions and finally get desirable solutions. From Fig. 5(c), it can be seen that AAVS-EDA keeps a larger search scope throughout the entire search process for the hybrid function $f_{18}$. The main reason lies in that the fitness landscape of $f_{18}$ is so complex that AAVS-EDA cannot find a definitely promising solution region with relatively limited number of FEs. Nevertheless, the final best solution it obtained is still much better than the one obtained by $\mathrm{EMNA}_{g}$.
![img-5.jpeg](img-5.jpeg)

Fig. 5. Evolution of the length of PDE's major axis derived from AAVS-EDA and EMNA ${ }_{g}$ on (a) $f_{2}$, (b) $f_{6}$ and (c) $f_{18}$.

![img-6.jpeg](img-6.jpeg)

Fig. 6. Evolution of the cosine value of $\theta$ derived from AAVS-EDA and EMNA, on (a) $f_{2}$, (b) $f_{6}$ and (c) $f_{18}$.
![img-7.jpeg](img-7.jpeg)

Fig. 7. Evolution of FEV derived from AAVS-EDA, EMNA ${ }_{g}$, AMaLGaM and IPOP-CMAES on (a) $f_{2}$, (b) $f_{6}$ and (c) $f_{18}$.

Fig. 6 shows the variation of $\cos (\theta)$ during the evolution process. It is clear that, for all the three functions, AAVS-EDA achieves larger cosine values than EMNA ${ }_{g}$ in most cases, which means that AAVS indeed enables AAVS-EDA to identify better search direction. Especially for $f_{2}$, AAVS-EDA finds the steepest descent direction after only a few generations. As for $f_{18}$, AAVS-EDA also detects better search direction than EMNA ${ }_{g}$ in the early and middle search stages. However, in the late search stage, both algorithms are trapped into local optimal regions, where the main search direction becomes less meaningful.

Fig. 7 shows the evolution curve of FEV, from which it can be observed that AAVS-EDA significantly outperforms EMNA ${ }_{g}$ on all the three functions. Besides EMNA ${ }_{g}$ and AAVS-EDA, Fig. 7 also presents the variation of FEVs obtained by AMaLGaM[19] and IPOP-CMAES[26]. As mentioned in section 1, AMaLGaM is an efficient EDA variant which synthetically adopts the strategies of AMS, AVS and SDR. IPOP-CMAES is an improved CMA-ES variant, which is competitive to many state-of-the-art EAs [27]. To ensure the fairness of the comparison, the AMaLGaM version which adopts the multivariate Gaussian model and a fixed population size was employed in our experiment. Its population size was set the same as that of AAVS-EDA, and all the other parameters were set the same as in [19]. As for IPOP-CMAES, we employed the source code and the default parameter settings provided by the authors of [43, 44]. It can be seen from Fig. 7(a) that AAVS-EDA, AMaLGaM and IPOP-CMAES all perform pretty well on $f_{2}$, where IPOPCMAES finds the global optimum with much fewer FEs. As for $f_{6}$, it can be seen from Fig. 7(b) that AMaLGaM gets stuck earlier; IPOP-CMAES improves AMalGaM and obtains the best solution within the allowed maximum number of FEs, but it still falls into a local optimum finally; Different from these two algorithms, AAVS-EDA keeps an improvement tendency during the whole evolution process. Fig. 7(c) presents the results on hybrid function $f_{18}$, from which it can be observed that all the four algorithms are trapped into local optimal solutions. In spite of this, AAVS-EDA demonstrates satisfying performance since it gets stuck at the latest and finds the best solution among these algorithms tested. It is notable that AAVSEDA still finds better solutions for $f_{18}$ after consuming about half of FEs. The reason is that it has strong exploration ability and identifies a relatively good search direction at that time, which can be clearly illustrated by Fig. 6(c).
4.3 Comparison with other state-of-the-art EAs

To evaluate the performance of AAVS-EDA, this section compares it with EMNA ${ }_{g}$ [4], AMaLGaM [19], IPOP-CMAES [26], CPI-JADE [45] and HHSPSO-GDS [46]. CPI-JADE is a new variant of DE, it

improves the performance of classic JADE [47] by implementing the crossover operator in both the original coordinate space and the eigen coordinate space, where the latter is established by decomposing the covariance matrix which is estimated from the cumulative population distribution information with the covariance matrix adaptation strategy developed in CMA-ES. In this sense, CPI-JADE has suitable comparability with AAVS-EDA. HHSPSO-GDS integrates the harmony search algorithm and the global dimension selection strategy into PSO to enhance its exploration and exploitation abilities. Experimental results revealed that HHSPSO-GDS possesses superior performance over many other PSO variants [46]. In short, AMaLGaM, IPOP-CMAES, CPI-JADE and HHSPSO-GDS can be viewed as the state-of-the-art of four kinds of EAs for continuous optimization, i.e., EDA, ES, DE and PSO, respectively. Table 1 reports the mean and standard deviation of FEVs obtained by the 6 algorithms on 30 benchmark functions, where the results of CPI-JADE and HHSPSO-GDS are directly taken from their original papers. Cohen's $d$ effect size [48] is adopted to judge the performance difference between AAVS-EDA and its five competitors. Cohen's $d$ effect size is a popular statistical method for quantifying the difference between two groups of data. It is independent of the sample size and is generally considered "small", "medium", and "large" if its absolute value belongs to $[0.2,0.3),[0.3,0.8)$ and $[0.8,+\infty)$, respectively. From Table 1, it can be observed that:

1) Unimodal functions $f_{1}-f_{5}$ : AAVS-EDA obtains the global optima for three unimodal functions, so do AMaLGaM, IPOP-CMAES and CPI-JADE. The results show that the combination of AAVS and the global monitor results in fine search performance for AAVS-EDA. As for the other two algorithms, HHSPSO-GDS shows better performance than $\mathrm{EMNA}_{g}$, but they both are outperformed by AAVS-EDA on all the three test functions.
2) Simple multimodal functions $f_{4}-f_{16}$ : Among these 13 functions, AAVS-EDA has an edge over AMaLGaM, IPOP-CMAES, CPI-JADE and HHSPSO-GDS on 9, 4, 4 and 7 functions, respectively, but is defeated by them on 2, 7, 8 and 6 functions, respectively. As a whole, AAVS-EDA performs a little worse

than IPOP-CMAES and CPI-JADE on this group of functions, but achieves better performance than EMNA $_{8}$, AMaLGaM and HHSPSO-GDS.
3) Hybrid functions $f_{17}-f_{32}$ : It is obvious that AAVS-EDA performs best among six algorithms on this group of test functions. The results it obtained are all not worse than the ones obtained by the other five algorithms except that HHSPSO-GDS achieves a better solution for $f_{19}$. Especially, AAVS-EDA reduces the mean of FEVs for $f_{18}$ by at least two orders of magnitude.

Table 1. The mean and the standard deviation (mean±standard deviation) of FEVs obtained by 6 algorithms over 25 independent runs on 30 CEC2014 benchmark functions with 30D
"-"," " and " $*$ " respectively denote that the performance of the corresponding algorithm is worse than, better than or similar to that of AAVS-EDA according to Cohen's $d$ effect size.

4) Composition functions $f_{23}-f_{30}$ : The components of these composition functions are so sophisticated that it is hard to find even the near optimal solutions. In spite of this, AAVS-EDA demonstrates superior performance. It performs not worse than $\mathrm{EMNA}_{g}$, AMaLGaM and CPI-JADE on all the eight functions, and is defeated by IPOP-CMAES and HHSPSO-GDS on only three functions. It is notable that the solutions for $f_{29}$ and $f_{30}$ obtained by AAVS-EDA are not only better but also more stable than the ones obtained by the other five algorithms.

The last row of Table 1 lists the number of functions on which AAVS-EDA performs better than, similarly to or worse than each of its competitors. This result demonstrate that AAVS-EDA shows significant advantages over $\mathrm{EMNA}_{g}$, AMaLGaM and CPI-JADE, and slight advantages over IPOP-CMAES and HHSPSO-GDS. In addition, we analyzed the differences between AAVS-EDA and the other five algorithms with Friedman test. Table 2 lists the ranking of the six algorithms obtained by the Friedman test, from which it can be concluded that AAVS-EDA performs best, followed by IPOP-CMAES; HHSPOSGDS, AMaLGaM and CPI-JADE show similar performance to each other, whereas $\mathrm{EMNA}_{g}$ is definitely defeated by the other five algorithms. This conclusion is basically consistent with the one drawn according to Cohen's $d$ effect size.

Table 2. Ranking of 6 algorithms according to the Friedman test.

As a whole, AAVS-EDA is very competitive compared with its competitors which contain four state-of-the-art EAs. This mainly profits from the effectiveness of AAVS which can adaptively adjust the search

scope and directions of AAVS-EDA. Considering AAVS-EDA possesses a simple algorithmic framework and only three parameters which are easy to set, it can be viewed as an efficient and practical EA.

# 5. Conclusions 

This paper presents a new EDA variant named AAVS-EDA for continuous optimization problems. Its main advantages lie in three aspects. First, it explicitly detects the landscape of an optimization problem in eigenspace with a simple topology-based detection method, and reveals that an optimization problem may have different landscape characteristics along different eigendirections. Second, it independently and adaptively adjusts the variable variances along different eigendirections according to the landscape detection results. As a result, both its search scope and search direction can fit well with the characteristics of the problem being solved. This shows great superiority to existing variance scaling strategies since they can only adjust the search scope. Finally, AAVS-EDA introduces an auxiliary global monitor which shrinks variable variances if the average fitness of the selected high-quality solutions does not improve. This helps AAVS-EDA to converge to a promising solution region. The performance of AAVS-EDA was fully tested on a set of 30 benchmark functions. The comparison results with several state-of-the-art EAs verify the efficiency and superiority of AAVS-EDA.

The superiority of AAVS-EDA is obtained at the cost of sampling additional solutions for detecting the landscape in eigenspace. For future research, it is of great significance to study landscape detection method by employing historical solutions. Since landscape information is beneficial to all kinds of EAs, then it is interesting to introduce the idea of AAVS into other EAs like DE and PSO. Moreover, we will extensively evaluate the performance of AAVS-EDA on some challenging optimization problems, including constrained optimization problem, combinatorial optimization problem, and some real world problems [49-52].

# Acknowledgements 

This work was partially supported by the National Natural Science Foundation of China [grant numbers 61105126, 61503300]; and the Postdoctoral Science Foundation of China [grant numbers 2014M560784, 2016T90922].
