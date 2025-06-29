# An efficient estimation of distribution algorithm with rank-one modification and population reduction 

Yongsheng Liang ${ }^{\mathrm{a}}$, Zhigang Ren ${ }^{\mathrm{a}, *}$, Miao $\mathrm{He}^{\mathrm{b}}$, Lin Wang ${ }^{\mathrm{c}}$, Jianfu Cao ${ }^{\mathrm{d}}$, An Chen ${ }^{\mathrm{a}}$, Bei Pang ${ }^{\mathrm{a}}$<br>${ }^{a}$ Department of Automation Science and Technology, School of Electronic and Information Engineering, Xi'an Jiaotong University, Xi'an, PR China<br>${ }^{b}$ Xi'an Aircraft Certification Center, Airworthiness Certification Center of CAAC, Xi'an, PR China<br>${ }^{c}$ School of Information Science and Technology, Northwest University, Xi'an, PR China<br>${ }^{d}$ Guangdong Xi'an Jiaotong University Academy, PR China

## A R T I C L E I N F O

Keywords:
Estimation of distribution algorithms
Premature convergence
Rank-one modification population reduction

## A B STR A C T

As a type of model-based metaheuristic, estimation of distribution algorithms (EDAs) show certain advantages over other metaheuristics by using statistical learning method to estimate the distribution of promising solutions. However, the commonly-used Gaussian EDAs (GEDAs) usually suffer from premature convergence that severely limits their efficiency. In this paper, we first attempt to enhance the performance of GEDA by improving its model estimation method. The new estimation method shifts the weighted mean of high-quality solutions towards the fitness improvement direction and estimates the covariance matrix by taking the shifted mean as the center. Theoretical analyses show that the new covariance matrix is essentially a rank-one modification (R1M) of the original one. It could effectively adjust both the search scope and the search direction of GEDA, and thus improving the search efficiency. Furthermore, considering the importance of the population size tuning in GEDA, we develop a population reduction (PR) strategy which linearly reduces the population size throughout the evolution. By this means, the exploration and exploitation ability of GEDA could be balanced better in different search stages and a more proper utilization of limited computation resource can be achieved. Combining GEDA with the R1M and PR strategies, a novel EDA variant named EDA-R1M-PR is developed. The performance of EDA-R1M-PR was comprehensively evaluated and compared with that of several state-of-the-art evolutionary algorithms. Experimental results indicate that the R1M and PR strategies effectively enhance the global optimization ability of GEDA and the resultant EDA-R1M-PR significantly outperforms its competitors on a set of benchmark functions.

## 1. Introduction

In recent decades, a great number of bio-inspired evolutionary algorithms (EAs) have been developed and applied to solve various kinds of optimization problems. Estimation of distribution algorithm (EDA) (Mühlenbein and Paaß, 1996; Larrañaga and Lozano, 2001) can be considered as a special kind of EA that merges a genetic algorithm (GA) with statistical learning method. Different from GA which employs the mutation and crossover operators to generate offspring, EDA explicitly builds a probabilistic model based on some promising solutions and produces offspring by sampling the learned model. Benefiting from the learnable probabilistic model, EDA is endowed with special advantages over other algorithms and is capable of solving a broad array of problems in both discrete and continuous domains (Hauschild and Pelikan, 2011; Chen et al., 2017a; Gao and de Silva, 2018). This study mainly
focuses on EDAs for continuous optimization.
The probabilistic model plays a crucial role in EDA. By far, many kinds of probabilistic models such as Gaussian model (Ren et al., 2018), Cauchy model (Sanyang and Kaban, 2014) and Histogram model (Ding et al., 2008) have been integrated into EDAs, among which the Gaussian model is most widely adopted by continuous EDAs. According to the variable dependencies, Gaussian EDAs (GEDAs) can be further classified into the following three categories. 1) Univariate GEDA which assumes all variables are independent. Examples of this category are univariate marginal distribution algorithm in continuous domain $\left(\right.$ UMDA $\left._{n}\right)$ (Larrañaga et al., 1999) and iterated density-estimation evolutionary algorithm (IDEA) (Bosman and Thierens, 2000). 2) Bivariate GEDA which only takes some pairwise variable interactions into account. Representative algorithm of this class is mutual information maximization and input clustering (MIMIC) (De Bonet et al., 1997). 3)

[^0]
[^0]:    * Corresponding author at: Department of Automation Science and Technology, School of Electronic and Information Engineering, Xi'an Jiaotong University, No. 28 Xianning West Road, Xi'an, Shaanxi, 710049, PR China.

    E-mail address: renzg@mail.xjtu.edu.cn (Z. Ren).

Multivariate GEDA considering interactions among multiple variables. Bayesian optimization algorithm (BOA) (Pelikan et al., 1999) and estimation of multivariate normal density algorithm (EMNA ${ }_{p}$ ) (Larrañaga and Lozano, 2001) belong to this class.

The model-based approach enables EDA to capture the important characteristics of promising solutions and thus facilitate it converging to the optimum. However, the traditional GEDA usually suffers from a tendency to prematurely converge to locally optimal solutions. It was revealed both experimentally and theoretically that a major cause for this drawback is the fast-decreasing of variable variances. To address this issue, Yuan and Gallagher (2005) suggested maintaining all the variances greater than 1. Grahl et al. (2006) proposed an adaptive variance scaling strategy (AVS) which dynamically enlarges or reduces the variance according to the state of the evolution. It is notable that AVS would only be activated when the algorithm is searching on a slope-like solution region and the techniques of correlation triggering rule (Grahl et al., 2006) and standard deviation ratio (SDR) (Bosman et al., 2007) were developed to identify such structure. Besides directly adjusting variances, Handa (2007) introduced a mutation operator into EDA to maintain the population diversity and alleviate premature convergence. Gao and Silva (Gao and de Silva, 2016) designed an extreme elitism selection method to enrich the population diversity by highlighting the roles of some other elite solutions besides the best one.

Since the performance of EDA is highly dependent on its probabilistic model, the model learning method becomes a key element. GEDA usually employs the maximum-likelihood (ML) estimation method to estimate its Gaussian model based on some high-quality solutions. Unfortunately, it was shown that the main search direction of the traditional GEDA tends to become orthogonal to the fitness improvement direction on slope-like regions. This defect was first noted by Cai et al. (2007), and they made the first remedy with a novel variance scaling strategy. To obtain a reasonable variance scaling factor, they tried to measure the divergence between the distribution of the selected solutions in current generation and the distribution of the population in next generation, and then calculate the scaling factor by minimizing the cross entropy between the two distributions. Although this remedy takes effect on some functions, its performance was reported not to be as competitive as AVS (Bosman et al., 2008). Ren et al. (2018) suggested an anisotropic adaptive variance scaling (AAVS) strategy that was shown to be able to deal with the above problems more effectively. Different with other scaling strategies that adjust all the variances with a same factor, AAVS anisotropically tunes the variances along different eigendirections according to the learned structure characteristics. In this way, AAVS is capable of adjusting both the search scope and direction of GEDA simultaneously, and thus greatly enhances its performance. Besides tuning the variances of the Gaussian model learned in traditional way, some other researchers attempted to directly ameliorate the model learning method. CMA-ES (Hansen and Ostermeier, 2001), which can be viewed as a special GEDA, employs the weighted good solutions in current generation and the mean of last generation to update its covariance matrix. The modified estimation method effectively increases the variances in the evolution direction, which endows CMA-ES with better search directions. (Bosman et al., 2008) developed an anticipated mean shift (AMS) strategy which shifts some solutions along the direction of mean shift. After that, these shifted and some other unshifted solutions in current generation as well as the elitist solutions in previous generations are all used to estimate the covariance matrix. Combining AMS with the aforementioned AVS and SDR, they proposed an efficient EDA variant named adapted maximum-likelihood Gaussian model-iterated density-estimation evolutionary algorithm (AMaLGaM) (Bosman et al., 2008). Experimental results indicated that AMaLGaM could obtain better search direction and search scope than traditional GEDA during the evolution and is very competitive with the famous CMA-ES.

In addition to overcoming the shortcomings, many other techniques were also introduced into EDA to improve its performance. Zhou et al.
(2015) combined EDA with cheap and expensive local search methods to improve its exploitation ability. Li et al. (2011) designed a subspace EDA to enhance the model learning and sampling efficiency by implementing the two operations in a selected subspace of all variables at each generation. For accelerating the search process, Chen et al. (2017a) proposed a fast interactive EDA which takes advantage of the domain knowledge of personalized search to reduce the initial search space to a preferred subspace. Yang et al. (2017) combined EDA with clustering strategy to strengthen its performance on multimodal problems. EDA was also scaled up to solve high-dimensional problems by taking advantage of the random matrix theory (Kabán et al., 2016). Furthermore, EDAs have been merged with some other kinds of EAs such as particle swarm optimization (PSO) (Ahn et al., 2012), differential evolution (DE) (Zhao et al., 2016) and artificial bee colony algorithm (ABC) (Xu et al., 2015) to develop hybrid algorithms that perform better than the original ones. There are also a variety of EDAs that were specially developed for different kinds of applications. Shi et al. (2019) proposed an adaptive EDA to derive the optimal plan of multi-policy insurance investment. Wu and Wang (2018) employed a multi-model EDA to deal with the energy efficient scheduling problem in cloud computing system.

Despite so many improvement works on the models of EDAs, fewer theoretical studies were conducted on EDAs. Grahl et al. (2005) studied the convergence behaviour of UMDA ${ }_{n}$ with truncation selection on monotonous functions, and showed that the algorithm could only travel a limited distance in the solution space and the distance solely relies on the selection pressure. Chen et al. (2010) investigated the computational time complexity of UMDA ${ }_{n}$ with respect to the population size on two typical unimodal functions. Lima et al. (2011) analyzed the relationship between the probabilistic models learned by BOA and the underlying problem structure to improve the model accuracy. Rastegar (2010) studied the convergence probability of two simple univariate EDAs and showed a sufficient condition for the convergence of the two algorithms on a specific class of functions.

Through the above related works, it can be seen that EDA has received considerable research effort in the past decades and its efficiency has been enhanced significantly from different perspectives. However, along with the advantages of these improved EDAs, there are still some shortcomings. First, some of the EDA variants, such as the famous CMAES and AMaLGaM, are accompanied by complicated algorithm framework and many free parameters, which may affect their robustness and limit their applicability. Second, most of the EDAs are improved by using different heuristic strategies and their performances are usually verified through specified experiments, but they generally lack theoretical analyses. The existing theoretical studies mainly focus on analyzing the characteristics of basic EDAs. They are of significance to reveal the properties of EDAs, but may not have strong practicability to improve their search efficiency. Third, most existing EDAs still adopt a fixed population size during the whole evolution, which leaves room for improvement. As a key element, the population size has a fundamental influence on the performance of EDA, especially its convergence rate. A larger population size encourages wider exploration of the solution space but reduces the convergence speed. On the other hand, a smaller population size could quicken the convergence, but may increase the risk of falling into local optimal regions. In different search stages, the population size should be dynamically adjusted to balance the exploration and exploitation ability of the algorithm. To achieve better adjustment of the population sizes of EAs, several adaptive population resizing methods have been successfully developed for algorithms like GA (Lobo and Lima, 2007), CMA-ES (Auger and Hansen, 2005), PSO (de Oca et al., 2011) and DE (Tanabe and Fukunaga, 2014). So it is of significance to develop an adaptive population resizing strategy for EDA to further enhance its performance.

To address the above issues, we proposed a novel GEDA with RankOne Modification and Population Reduction strategies (EDA-R1M-PR). Theoretical and experimental studies are both conducted to prove and

verify the effectiveness of the proposed strategies and the resultant algorithm. The main contributions of this work are summarized as follows:
(1) Improve the model estimation method of GEDA with a simple and efficient mean shift strategy. This strategy directly shifts the weighted mean of selected solutions towards more promising solution regions, then estimates the covariance matrix of Gaussian model by taking the shifted mean as the center. The operation not only keeps the simplicity of ML estimation but also significantly enhances the search ability of GEDA.
(2) Theoretically show that the essence of the improved covariance matrix is rank-one modification (R1M) of the original one. Taking advantage of the analytical properties of Gaussian model, we further prove that the R1M operation could effectively adjust the search scope and main search direction of GEDA simultaneously, and thus greatly improve its performance.
(3) Design a population reduction strategy for GEDA, which linearly reduces the population size at each generation throughout the evolution. In the earlier search stage, a larger population size is capable of locating promising solution regions more precisely; while in the latter search stage, a relatively smaller population size is beneficial to improve the convergence speed thus facilitating the algorithm finding the optimal solution. In this way, the exploration and exploitation ability of GEDA could be balanced better in different search stages and a more proper utilization of computation resource can be achieved.

The rest of this paper is organized as follows. Section 2 describes the basic knowledge of GEDA. Section 3 presents the proposed EDA-R1MPR algorithm in detail. Section 4 provides the experimental results and analyses. The conclusions are finally given in Section 5 along with future work.

## 2. Basic GEDA

First proposed by Mühlenbein and Paaß (1996), EDA inherits the basic framework of GA, but employs a probabilistic model to extract statistical information of good solutions and produces new solutions by sampling the learned model. The general framework of EDA is outlined in Algorithm 1. After initialization, EDA executes an iterative process of evaluation (step 3), selection (step 4), model building (step 5) and sampling (step 6) until a predefined stopping criterion is met.

```
Algorithm 1: General framework of EDA
    - Initialize parameters, set \(t=0\), and generate the initial population \(P^{\prime}\);
    - while the stopping criterion is not met do
    - Evaluate population \(P^{\prime}\) and update the best solution \(b\) obtained so far;
    - Select promising solutions \(S^{\prime}\) from \(P^{\prime}\) according to a selection rule;
    - Build a new probability model \(G^{\prime}\) based on \(S^{\prime}\);
    - Generate a new population \(P^{\prime+1}\) by sampling from \(G^{\prime}\) and update \(t=t+1\);
    - end
    - returub.
```

Most continuous EDAs employ Gaussian model to describe the distribution of good solutions. The probability density function of Gaussian model can be presented by the following notation:
$G_{(\mu, C)}(x)=\frac{1}{(2 \pi)^{n / 2}\left(\operatorname{det} C\right)^{1 / 2}} e^{-\frac{1}{2}(x-\mu)^{2}\left(C^{\prime}\right)^{-1}(x-\mu)}$
where $\boldsymbol{x}$ is an $n$-dimensional variable vector, $\boldsymbol{\mu}$ and $C$ are the mean and covariance matrix (CM) of $\boldsymbol{x}$, respectively. To establish this model, we need to estimate $\boldsymbol{\mu}$ and $C$ from some selected solutions. Maximumlikelihood (ML) estimation method is a commonly adopted approach. For a given set of selected solutions $S^{\prime}$, the ML estimates for $\boldsymbol{\mu}$ and $C$ are given by the following formulas respectively:
$\hat{\boldsymbol{\mu}}^{t}=\frac{1}{\left(S^{\prime}\right)} \sum_{i=1}^{\left(S^{\prime}\right)} S_{i}^{t}$
$C^{\prime}=\frac{1}{\left(S^{\prime}\right)} \sum_{i=1}^{\left(S^{\prime}\right)}\left(S_{i}^{t}-\hat{\mu}^{t}\right)\left(S_{i}^{t}-\hat{\mu}^{t}\right)^{2}$
in which $\left|\cdot\right|$ represents the cardinality of a set.
The Gaussian model estimated with Eqs. (2) and (3) uses a full CM and is adopted by many GEDAs like $\mathrm{EMNA}_{\mathrm{g}}$. This model keeps all the variable dependencies that it could ensure rotation-invariance and usually performs well on problems with significant dependencies. While a limitation of this model is that it requires a large number of solutions to properly estimate the CM since there are up to $0.5\left(n^{2}+n\right)$ parameters in it. Existing GEDAs using full CM generally adopt a constant and relatively large population size throughout the evolution, which may limit their search efficiency. This is because, on the one hand, a constant and large population size reduces the number of iterations of GEDA if only limited computation resource is available. On the other hand, the population size has great influence on the convergence behavior of GEDA, a constant value for it means that GEDA cannot well balance the exploration and exploitation ability in different search stages. Thus, the population size setting method in GEDA leaves room for improvement.

Furthermore, as mentioned above that traditional GEDA would generally suffer from two drawbacks: 1) variable variances decrease fast; 2) the main search direction of GEDA tends to become orthogonal to improvement direction of the fitness function. Fig. 1 explains the reasons for the two drawbacks by presenting the evolution of the probability density ellipsoid (PDE) of GEDA in two successive generations on a slope-like region. PDE is determined by the mean and CM of the Gaussian model and could reflect the search center and search range of GEDA. The major axis direction of PDE presents the main search direction of GEDA. As shown in Fig. 1, the new PDE obtained by ML estimation describes the distribution of selected solutions well. However, it is not the actual distribution but the direction of improvement that is of significance in order to find better solutions on slope-like regions. Due to the selection pressure and the property of Gaussian model that it generally produces more solutions near its mean, the new PDE estimated by these selected solutions will generally shrink and its
![img-0.jpeg](img-0.jpeg)

Fig. 1. The evolution of PDE in traditional GEDA.

major axis is inclined to become perpendicular to the fitness improvement direction. As a result, GEDA is unlikely to obtain fine search scope and search direction in this situation.

## 3. GEDA with rank one modification and population reduction

As shown in Fig. 1, the search center, search scope and main search direction of GEDA are determined by the center, shape and major axis direction of the PDE, respectively. It is hoped that the PDE could be located in promising solution regions, its shape could automatically adapt to the structural characteristics of the solution space, and the direction of its major axis can be parallel to the desired fitness improvement direction. To achieve the above goals, we first tried to improve the estimation method for the mean and CM with a mean shift strategy and showed that the essence of the improved CM is the rankone modification (R1M) of the original one. Then the effectiveness of the R1M operation was theoretically proved. Moreover, we designed a population reduction (PR) strategy for the proposed GEDA with R1M (EDA-R1M) to further enhance its performance, and the resultant algorithm was finally named as EDA-R1M-PR.

### 3.1. Mean estimation method

The traditional ML estimator shown in Eq. (2) calculates the mean as the average of selected solutions. However, the goal of estimating the mean is not to calculate the real center of selected solutions, but to obtain a more promising search center for GEDA. Thus, we estimate the mean as the weighted average of selected solutions:
$\bar{\mu}^{i}=\frac{\sum_{t=1}^{|S|}\left\{\log \left(\left|S^{t}\right|+1\right)-\log (i)\right\}\left|S_{i j}^{t}\right|}{\sum_{t=1}^{|S|}\left\{\log \left(\left|S^{t}\right|+1\right)-\log (i)\right\}}$
where $S_{i j}^{t}$ denotes the ith best solution in the selected solution set $S^{t}$. It can be seen from Eq. (4) that better solutions are endowed with larger weights, then the estimated mean $\bar{\mu}^{i}$ will be pulled towards relatively high-quality solutions to get a better search center. Our preliminary experiments showed that $\bar{\mu}^{i}$ usually performs better than the original $\bar{\mu}^{i}$.

To further accelerate the search process, we try to shift $\bar{\mu}^{i}$ towards the evolution direction as follows:
$\hat{\delta}^{i}=\bar{\mu}^{i}-\bar{\mu}^{i-1}$
$\bar{\mu}^{i}=\left\{\begin{array}{l}\bar{\mu}^{i}+\eta \hat{\delta}^{i}, \operatorname{lf}\left(\bar{\mu}^{i}+\eta \hat{\delta}^{i}\right)<f\left(\bar{\mu}^{i}\right) \\ \bar{\mu}^{i}, \text { otherwise }\end{array}\right.$
where $\bar{\mu}^{i}$ represents the shifted mean in the $t$ th generation, it is the real mean used for sampling new solutions. $\hat{\delta}^{i}$ is the difference between $\bar{\mu}^{i}$ and $\bar{\mu}^{i-1}$, it reflects the evolution direction. $\eta$ is a shifting factor which should be greater than 0 and $f(\cdot)$ is the objective function to be minimized. Eq. (6) attempts to update $\bar{\mu}^{i}$ with $\bar{\mu}^{i}+\eta \hat{\delta}^{i}$ providing that $f\left(\bar{\mu}^{i}+\eta \hat{\delta}^{i}\right)$ is smaller than $f\left(\bar{\mu}^{i}\right)$. The purpose of this operation is to exploit the inertia of the evolution direction thus speeding up the search process. A proper value for $\eta$ could help GEDA finding a more promising search center for the next generation. It is however non-trivial to set the value of $\eta$, especially for black box optimization problems. Considering that the purpose of shifting the mean is to get a relatively better search center, rather than finding the optimal value for the mean. In addition, the mean shift operation would also consume some fitness evaluations. Keeping the two principles in mind, we designed a simple line search method to roughly find a proper value for the mean. As shown in Algorithm 2, the line search method tries to shift the mean along the evolution direction step by step until it is unable to find a better value for $\bar{\mu}^{i}$ or the maximum step size $\eta_{\max }$ is reached. Note that $\eta_{\max }$ should not be set too large for sake of saving computation resource and
avoiding disturbing the algorithm too much. According to our preliminary experimental results, we suggest setting $\eta_{\max }=5$.

```
Algorithm 2: Line search method
Input: \(\bar{\mu}^{i}, \hat{\delta}^{i}\) and \(\eta_{\max }\)
Output: \(\bar{\mu}^{i}\)
    \(1 \bar{\mu}^{i}=\bar{\mu}^{i}, \eta=0_{i, j}\)
    2 while \(\left.f\left(\bar{\mu}^{i}, \hat{\delta}^{i}\right)<f\left(\bar{\mu}^{i}\right) \& \& \eta<\eta_{\max }\right.\) do
    \(3 \bar{\mu}^{i}=\bar{\mu}^{i}+\hat{\delta}^{i}\)
    \(4 \eta=\eta+1 ;\)
    5 end
```


### 3.2. Covariance matrix estimation method

CM of Gaussian model affects the search scope and search direction of GEDA. However, the CM estimated by the traditional ML estimator may result in the PDE aligned in the worst way. Considering that the CM of a random vector equals its second-order central moment, a convenient way to re-align PDE is to change the reference mean. Since we have obtained a more promising mean $\bar{\mu}^{i}$ through the above mean shift operation, it is reasonable to improve the CM estimation method by replacing the mean $\bar{\mu}^{i}$ with $\bar{\mu}^{i}$ :
$\hat{C}^{i}=\frac{1}{\left|S^{t}\right|} \sum_{i=1}^{\left|S^{t}\right|}\left(S_{i}^{t}-\bar{\mu}^{i}\right)\left(S_{i}^{t}-\bar{\mu}^{i}\right)^{2}$
Compared with the CM obtained with traditional ML estimator, the PDE of $\hat{C}^{i}$ will be naturally elongated along the direction of $\left(\bar{\mu}^{i}-\bar{\mu}^{i}\right)$ and the estimated variable variances would also be increased providing that $\bar{\mu}^{i} \neq \bar{\mu}^{i}$. In the following, we will show that $\hat{C}^{i}$ is essentially the rank-one modification of the original $\hat{C}^{i}$. Then the properties of $\hat{C}^{i}$ will be discussed. It will be shown that the new estimation method for CM could adaptively adjust the search scope and search direction of GEDA and thus improve its search efficiency.

For the convenience of derivation, we omit " $t$ " in the variables and equations below. For each generation, it can be known from Eqs. (4)-(6) that $\hat{\mu}$ is not worse than $\bar{\mu}$ and $\bar{\mu}$ is usually better than $\bar{\mu}$, then $\hat{\mu}$ would generally be better than $\bar{\mu}$ with high probability. Then, $\hat{\delta}=\hat{\mu}-\bar{\mu}$ represents a fitness improvement direction. We can transform Eq. (7) as follows:
$\hat{C}=\frac{1}{|S|} \sum_{i=1}^{|S|}\left(S_{i}-\bar{\mu}\right)\left(S_{i}-\bar{\mu}\right)^{\mathrm{T}}$
$=\frac{1}{|S|} \sum_{i=1}^{|S|}\left(S_{i}-\bar{\mu}-\hat{\delta}\right)\left(S_{i}-\bar{\mu}-\hat{\delta}\right)^{\mathrm{T}}$
$=\frac{1}{|S|} \sum_{i=1}^{|S|}\left(S_{i}-\bar{\mu}\right)\left(S_{i}-\bar{\mu}\right)^{\mathrm{T}}-\frac{1}{|S|} \sum_{i=1}^{|S|}\left(S_{i}-\bar{\mu}\right) \hat{\delta}^{\mathrm{T}}$
$-\frac{1}{|S|} \hat{\delta} \sum_{i=1}^{|S|}\left(S_{i}-\bar{\mu}\right)^{2}+\hat{\delta} \hat{\delta}^{\mathrm{T}}$
$=\hat{C}+\hat{\delta} \hat{\delta}^{\mathrm{T}}$
Eq. (8) means that $\hat{\mathbf{C}}$ is the rank-one modification of $\hat{\mathbf{C}}$ (Bunch et al., 1978), that is why we named the improved estimation method as rankone modification of the original CM. And we can give the following theorems and corollaries

Theorem 1: For a given set of selected solutions, if $\hat{\mu} \neq \bar{\mu}$, then the volume of the PDE determined by $\hat{\mathbf{C}}$ is not less than that of the PDE determined by $\hat{\mathbf{C}}$.

Proof: According to the properties of Gaussian distribution, the axis directions of PDE are accordant with the eigendirections of CM, and the lengths of the semiaxes $a_{d}(d=1,2, \ldots, n)$ are equal to the square roots of corresponding eigenvalues $\lambda_{d}$, i.e. $a_{d}=\sqrt{\lambda_{d}}$. Based on the conclusion in (Zhao, 2013), the volume of PDE is proportional to the product of the lengths of its semiaxes. Denote the eigenvalues of $\hat{\mathbf{C}}$ and $\hat{\mathbf{C}}$ as $\hat{\lambda}_{d}$ and

$\hat{\lambda}_{d}(d=1,2, \ldots, n)$, respectively, then a necessary and sufficient condition for Theorem 1 is: $\prod_{d=1}^{n} \hat{\lambda}_{d} \geq \prod_{d=1}^{n} \hat{\lambda}_{d}$ when $\hat{\boldsymbol{\mu}} \neq \hat{\boldsymbol{\mu}}$.

To prove the above condition, we first conduct eigendecomposition on $\hat{\mathbf{C}}$. From Eq. (3), it can be seen that $\hat{\mathbf{C}}$ is a real symmetric matrix and is positive semidefinite. Then $\hat{\mathbf{C}}$ can be decomposed as $\hat{C}=\hat{Q} \hat{A} \hat{Q}^{\mathrm{T}}$, in which $\hat{A}=\operatorname{diag}\left(\hat{\lambda}_{1}, \hat{\lambda}_{2}, \ldots, \hat{\lambda}_{n}\right), 0 \leq \hat{\lambda}_{1} \leq \hat{\lambda}_{2} \leq \ldots, \leq \hat{\lambda}_{n}$ and $\hat{\mathbf{Q}}$ is a orthogonal matrix composed of the eigenvectors of $\hat{\mathbf{C}}$. Let $\boldsymbol{p}=\hat{Q}^{\mathrm{T}} \hat{\boldsymbol{\delta}}$, then we have:
$\hat{Q}^{\mathrm{T}} \hat{C} \hat{Q}=\hat{Q}^{\mathrm{T}}\left(\hat{C}+\hat{\delta} \hat{\delta}^{\mathrm{T}}\right) \hat{Q}$
$=\hat{Q}^{\mathrm{T}} \hat{C} \hat{Q}+\left(\hat{Q}^{\mathrm{T}} \hat{\delta}\right)\left(\hat{Q}^{\mathrm{T}} \hat{\delta}\right)^{\mathrm{T}}$
$=\hat{A}+\boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}$
It is clear that $\hat{A}+\boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}$ is the rank-one modification of $\hat{\mathbf{A}}$. Lemma 1.4 in reference Yin (2003) discussed the characteristic polynomial of diagonal matrix with rank-one modification. Based on the result in Lemma 1.4 Yin (2003), we can derive the characteristic polynomial of $\hat{A}+\boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}$, namely the characteristic polynomial of $\hat{\mathbf{C}}$, as follows:

$$
\begin{aligned}
& F(\lambda)=\prod_{d=1}^{n}\left(\lambda-\hat{\lambda}_{d}\right) \\
& =\operatorname{det}\left(\lambda I-\hat{A}-\boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}\right) \\
= & \operatorname{det}(\lambda I-\hat{A}) \operatorname{det}\left(I-(\lambda I-\hat{A})^{-1} \boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}\right) \\
= & \prod_{d=1}^{n}\left(\lambda-\hat{\lambda}_{d}\right)\left(1-\sum_{k=1}^{n} \frac{\boldsymbol{p}_{k}^{2}}{\lambda-\hat{\lambda}_{k}}\right) \\
= & \prod_{d=1}^{n}\left(\lambda-\hat{\lambda}_{d}\right)-\sum_{k=1}^{n}\left(\boldsymbol{p}_{k}^{2} \prod_{d=1, d \neq k}^{n}\left(\lambda-\hat{\lambda}_{d}\right)\right)
\end{aligned}
$$

where $I$ represents the $n$-dimensional identity matrix. Set $\lambda=0$ in Eq. (10), then we have:
$\prod_{d=1}^{n} \hat{\lambda}_{d}=\prod_{d=1}^{n} \hat{\lambda}_{d}+\sum_{k=1}^{n}\left(\boldsymbol{p}_{k}^{2} \prod_{d=1, d \neq k}^{n} \hat{\lambda}_{d}\right)$
$\geq \prod_{d=1}^{n} \hat{\lambda}_{d}$
So Theorem 1 is proved.
Corollary 1: For a given set of selected solutions $\mathbf{S}$, if $\hat{\boldsymbol{\mu}} \neq \hat{\boldsymbol{\mu}}$ and $\mathbb{S} \mathbb{S}>n$, then the volume of the PDE determined by $\hat{\mathbf{C}}$ is greater than that of the PDE determined by $\hat{\mathbf{C}}$.

Proof: Considering that $\hat{Q}^{\mathrm{T}}$ in Eq. (9) is an orthogonal matrix, then $\boldsymbol{p}=\hat{Q}^{\mathrm{T}} \hat{\delta} \neq 0$ if $\hat{\delta}=\hat{\boldsymbol{\mu}}-\hat{\boldsymbol{\mu}} \neq 0$. This implies $\boldsymbol{p}_{k} \neq 0$ for some $k=1,2, \ldots, n$. On the other side, all the solutions in $\mathbf{S}$ are independently selected, then $\hat{\mathbf{C}}$ is positively definite with probability 1 if $\mathbb{S} \mathbb{S}>n$ (Xie and Chen, 1990). That is to say, $\hat{\lambda}_{d}>0$ for each $d=1,2, \ldots, n$. Taking the above two results related with Eq. (11) into account, it can be known that $\sum_{k=1}^{n}\left(\boldsymbol{p}_{k}^{2} \prod_{d=1, d \neq k}^{n} \hat{\lambda}_{d}\right)>0$ and $\prod_{d=1}^{n} \hat{\lambda}_{d}>\prod_{d=1}^{n} \hat{\lambda}_{d}$.

Corollary 2: For a given set of selected solutions, the greater the Mahalanobis distance between $\hat{\boldsymbol{\mu}}$ and $\hat{\boldsymbol{\mu}}\left(\hat{\delta}^{\mathrm{T}} \hat{C}^{-1} \hat{\delta}\right)$ is, the greater the volume of the PDE determined by $\hat{\mathbf{C}}$ will be.

Proof: Let us reconsider Eq. (11):

$$
\begin{aligned}
& \prod_{d=1}^{n} \hat{\lambda}_{d}=\prod_{d=1}^{n} \hat{\lambda}_{d}+\sum_{k=1}^{n}\left(\boldsymbol{p}_{k}^{2} \prod_{d=1, d \neq k}^{n} \hat{\lambda}_{d}\right) \\
& =\prod_{d=1}^{n} \hat{\lambda}_{d}\left(1+\sum_{k=1}^{n}\left(\boldsymbol{p}_{k}^{2} / \hat{\lambda}_{k}\right)\right) \\
& =\prod_{d=1}^{n} \hat{\lambda}_{d}\left(1+\boldsymbol{p}^{\mathrm{T}} \hat{A}^{-1} \boldsymbol{p}\right) \\
& =\prod_{d=1}^{n} \hat{\lambda}_{d}\left(1+\hat{\delta}^{\mathrm{T}} \hat{\delta} \hat{A}^{-1} \hat{Q}^{\mathrm{T}} \hat{\delta}\right) \\
& =\prod_{d=1}^{n} \hat{\lambda}_{d}\left(1+\hat{\delta}^{\mathrm{T}} \hat{C}^{-1} \hat{\delta}\right)
\end{aligned}
$$

So we can know that $\prod_{d=1}^{n} \hat{\lambda}_{d}$ is positively correlated with $\hat{\delta}^{\mathrm{T}} \hat{C}^{-1} \hat{\delta}$, so does the volume of the PDE determined by $\hat{\mathbf{C}}$.

Remark 1: Corollary 1 theoretically gives a necessary and sufficient condition for assuring that the volume of the PDE determined by $\hat{\mathbf{C}}$ is greater than the volume of the PDE determined by $\hat{\mathbf{C}}$. According to the above analyses, EDA-R1M adopts $\hat{\boldsymbol{\mu}}$ as the center, which is usually better than and not equal to $\hat{\boldsymbol{\mu}}$. On the other side, the population size of EDA-R1M and traditional multivariate GEDA are generally much greater than the problem dimension, then the number of selected solutions could usually satisfy $\mathbb{S} \mathbb{S}>n$. So Corollary 1 is generally tenable in EDA-R1M, which means that, for the same set of selected solutions, the exploration ability of EDA-R1M is usually greater than that of the traditional GEDA.

Remark 2: Corollary 2 shows that if we want to improve the exploration ability of EDA-R1M, we need to increase the Mahalanobis distance between $\hat{\boldsymbol{\mu}}$ and $\hat{\boldsymbol{\mu}}\left(\hat{\delta}^{\mathrm{T}} \hat{C}^{-1} \hat{\delta}\right)$, i.e. increase $\boldsymbol{p}^{\mathrm{T}} \hat{A}^{-1} \boldsymbol{p}$. For a given set of selected solutions, $\hat{\mathbf{C}}$ and $\hat{\mathbf{A}}$ are both determined. So we could only increase $\boldsymbol{p}^{\mathrm{T}} \hat{A}^{-1} \boldsymbol{p}$ by increasing the sub-components of $\boldsymbol{p}$, i.e. $p_{k}(d=1,2, \ldots, n)$, which are the projections of $\hat{\delta}$ on the eigenvectors of $\hat{\mathbf{C}}$. According to Eq. (6), we can alter the position of $\hat{\boldsymbol{\mu}}$ by adjusting the shifting factor $\eta$. A larger value for $\eta$ could move $\hat{\boldsymbol{\mu}}$ to a farther position, and thus increase $\hat{\delta}$ and improve the exploration ability of EDA-R1M.

Theorem 2: For a given set of selected solutions, if $\hat{\boldsymbol{\mu}} \neq \hat{\boldsymbol{\mu}}$, then the angle between $\hat{\delta}$ and the major axis of the PDE determined by $\hat{\mathbf{C}}$ is not greater than the angle between $\hat{\delta}$ and the major axis of the PDE determined by $\hat{\mathbf{C}}$.

Proof: Without loss of generality, it can be assumed that the eigenvalues of $\hat{A}+\boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}$ satisfy $0 \leq \hat{\lambda}_{1} \leq \hat{\lambda}_{2} \leq \ldots, \leq \hat{\lambda}_{n}$. Denote the major eigenvectors of $\hat{A}+\boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}$ and $\hat{\mathbf{A}}$ as $\hat{\boldsymbol{q}}$ and $\hat{\boldsymbol{q}}$ respectively, where the major eigenvector means the eigenvector with the greatest eigenvalue. According to Eq. (9), $\hat{A}+\boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}$ and $\hat{\mathbf{A}}$ are the orthogonal transformations of $\hat{\mathbf{C}}$ and $\hat{\mathbf{C}}$ by taking $\hat{Q}^{\mathrm{T}}$ as the transformation matrix, respectively. Then Theorem 2 is equivalent to proving that if $\hat{Q}^{\mathrm{T}} \hat{\delta}=\boldsymbol{p} \neq 0$, then $\angle(\boldsymbol{p}, \hat{\boldsymbol{q}}) \leq \angle(\boldsymbol{p}, \hat{\boldsymbol{q}})$. Besides, since the major axis of a PDE is undirected, there will be two angles between it and $\boldsymbol{p}$. Here we only focus on analyzing the smaller angle between them, so we can assume that $\boldsymbol{p}^{\mathrm{T}} \hat{\boldsymbol{q}} \geq 0, \boldsymbol{p}^{\mathrm{T}} \hat{\boldsymbol{q}} \geq 0$.

Case 1: If $\boldsymbol{p}^{\mathrm{T}} \hat{\boldsymbol{q}}=0$, then $\angle(\boldsymbol{p}, \hat{\boldsymbol{q}})=90^{\circ}$. Since $\angle(\boldsymbol{p}, \hat{\boldsymbol{q}}) \leq 90^{\circ}$, then we can know that $\angle(\boldsymbol{p}, \hat{\boldsymbol{q}}) \leq \angle(\boldsymbol{p}, \hat{\boldsymbol{q}})$.

Case 2: If $\boldsymbol{p}^{\mathrm{T}} \hat{\boldsymbol{q}} \neq 0$, then $\hat{\lambda}_{n}>\hat{\lambda}_{n}$ and $\boldsymbol{p}^{\mathrm{T}} \hat{\boldsymbol{q}} \neq 0$. The reasons lie in that: First, $\hat{A}+\boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}$ is the rank-one modification of $\hat{\mathbf{A}}$, then $\hat{\lambda}_{d} \geq \hat{\lambda}_{d}(d=1,2, \ldots, n)$; Second, the projection of $\boldsymbol{p}$ on $\hat{\boldsymbol{q}}$ is not equal to zero as $\boldsymbol{p}^{\mathrm{T}} \hat{\boldsymbol{q}} \neq 0$, thus $\hat{\lambda}_{n}>\hat{\lambda}_{n}$ (Bunch et al., 1978). Furthermore, consider the definition of eigenvalue:
$\left(\hat{A}+\boldsymbol{p} \boldsymbol{p}^{\mathrm{T}}\right) \hat{\boldsymbol{q}}=\hat{\lambda}_{n} \hat{\boldsymbol{q}}$
If $\boldsymbol{p}^{\mathrm{T}} \hat{\boldsymbol{q}}=0$ in Eq. (13), then we have $\hat{A} \hat{\boldsymbol{q}}=\hat{\lambda}_{n} \hat{\boldsymbol{q}}$. It means that $\hat{\lambda}_{n}$ is also the eigenvalue of $\hat{\mathbf{A}}$, this is contradictory with the former conclusion $\hat{\lambda}_{n}>\hat{\lambda}_{n}$. So $\boldsymbol{p}^{\mathrm{T}} \hat{\boldsymbol{q}} \neq 0$. Besides, we can also derive from Eq. (13) that $\hat{\boldsymbol{q}}=\left(\hat{\lambda}_{n} \boldsymbol{I}-\hat{\boldsymbol{A}}\right)^{-1} \boldsymbol{p} \boldsymbol{p}^{\mathrm{T}} \hat{\boldsymbol{q}}$.

Set 1 in Eq. (10) as $\hat{\lambda}_{n}$, then

$$
\begin{aligned}
& F\left(\hat{\lambda}_{n}\right)=\left(1-\sum_{d=1}^{n} \frac{\boldsymbol{p}_{k}^{2}}{\hat{\lambda}_{n}-\hat{\lambda}_{d}}\right) \prod_{d=1}^{n}\left(\hat{\lambda}_{n}-\hat{\lambda}_{d}\right) \\
& =0 \\
& \Rightarrow \sum_{d=1}^{n} \frac{\boldsymbol{p}_{k}^{2}}{\hat{\lambda}_{n}-\hat{\lambda}_{d}}=1 \\
& \Rightarrow 1 \geq \frac{\boldsymbol{p}_{k}^{2}}{\hat{\lambda}_{n}-\hat{\lambda}_{n}}>0
\end{aligned}
$$

Then:

$$
\begin{aligned}
& \cos \angle(\boldsymbol{p}, \hat{\boldsymbol{q}})=\frac{\boldsymbol{p}^{T} \hat{\boldsymbol{q}}}{\|\boldsymbol{p}\|\|\hat{\boldsymbol{q}}\|}=\frac{\boldsymbol{p}^{T} \hat{\boldsymbol{q}}}{\|\boldsymbol{p}\|\left(\hat{\lambda}_{n} I-\hat{A}\right)^{2} \boldsymbol{p}\left\|\boldsymbol{p}^{T} \hat{\boldsymbol{q}}\right.} \\
& =\frac{\|\boldsymbol{p}\|\left(\sqrt{\sum_{d=1}^{n} \frac{p_{d}^{2}}{\hat{\lambda}_{n}-\hat{\lambda}_{d}}\right)^{2}}\right.}{2 \frac{\left|\boldsymbol{p}_{z}\right|}{\|\boldsymbol{p}\|\left(\sqrt{\hat{\lambda}_{n}-\hat{\lambda}_{n}\right) \sum_{d=1}^{n} \frac{p_{d}^{2}}{\hat{\lambda}_{n}-\hat{\lambda}_{d}}\right)^{2}} \geq \frac{\left|\boldsymbol{p}_{z}\right|}{\|\boldsymbol{p}\|\left(\hat{\lambda}_{n}-\hat{\lambda}_{n}\right) \sum_{d=1}^{n} \frac{p_{d}^{2}}{\hat{\lambda}_{n}-\hat{\lambda}_{n}\left(\hat{\lambda}_{n}-\hat{\lambda}_{d}\right)}}$
\end{aligned}
$$

So we can know that $\angle(\boldsymbol{p}, \hat{\boldsymbol{q}}) \leq \angle(\boldsymbol{p}, \hat{\boldsymbol{q}})$. Combining the results of Case 1 and Case 2, Theorem 2 is proved.

Remark 3: In Case $1\left(\boldsymbol{p}^{T} \hat{\boldsymbol{q}}=0\right)$, it can be drawn that $\hat{\lambda}_{n}$ and $\hat{\boldsymbol{q}}$ are also the eigenvalue and eigenvector of $\hat{A}+\boldsymbol{p} \boldsymbol{p}^{T}$, respectively. The reason lies in that when $\|\boldsymbol{p}\|$ is relatively small, it would only have very slight influence on the eigenvalues. In this circumstance, $\hat{\lambda}_{n}$ may remain to be the major eigenvalue of $\hat{A}+\boldsymbol{p} \boldsymbol{p}^{T}$, thus $\hat{\lambda}_{n}=\hat{\lambda}_{n}$ and $\angle(\boldsymbol{p}, \hat{\boldsymbol{q}})=\angle(\boldsymbol{p}, \hat{\boldsymbol{q}})=90^{\circ}$. With respect to Case $2, \angle(\boldsymbol{p}, \hat{\boldsymbol{q}})=\angle(\boldsymbol{p}, \hat{\boldsymbol{q}})=0^{\circ}$ would happen only when $\boldsymbol{p}_{z}^{2}=\hat{\lambda}_{n}-\hat{\lambda}_{n}, \boldsymbol{p}_{z}=0(d=1,2, \ldots, n-1)$, i.e. $\boldsymbol{p}$ is parallel to $\hat{\boldsymbol{q}}$. In most other cases, we can have $\angle(\boldsymbol{p}, \hat{\boldsymbol{q}})<\angle(\boldsymbol{p}, \hat{\boldsymbol{q}})$. Since the major axis of PDE (the major eigenvector of covariance matrix) determines the main search direction of GEDA, Theorem 2 implies that the main search direction of GEDA will be more close to the fitness improvement direction when employing $\hat{\mathbf{C}}$ as the covariance matrix.

Through Theorem 1 and Theorem 2, we theoretically show that EDA with R1M (EDA-R1M) has greater search scope and better main search direction than the traditional GEDA. Thus it is reasonable to believe that the search efficiency of EDA-R1M could be greatly improved. In addition, Corollary 2 and Remark 2 show that the exploration ability of EDA-R1M could be adjusted by tuning the shifting factor $\eta$, so we employ a simple line search method shown in Algorithm 2 to adaptively get a proper value for $\eta$.

### 3.3. Population reduction strategy

As a type of population-based optimization algorithm, the tuning of population size plays a substantial role in affecting the performance of EDA. A large population size could improve the exploration degree to the solution region dominated by the current probabilistic model, but would slow down the convergence process. In addition, it would also reduce the number of iterations if only limited computation resource is available, which further restricts the convergence ability. On the other hand, a small population size could quicken the convergence, but may increase the risk of premature convergence. Existing EDAs usually adopt a constant population size throughout the evolution and can hardly balance the exploration and exploitation ability in different search stages. Furthermore, GEDAs using full CM generally need a relatively large population size to estimate a proper model, which would consume much computation resource at each generation and thus limit their performance, as discussed in Section 2.

To remedy the above deficiencies, we attempted to develop a dynamic population size tuning strategy for EDA. On the one hand, it is hoped that the strategy could dynamically adjust the population size in different stages. In the earlier search stage, a larger population size could help EDA more accurately capture the characteristics of the solution space and locate promising regions. In the latter search stage, the algorithm may have converged to local solution regions. In this situation, a smaller population size is preferred to accelerate the convergence. On the other hand, the population size tuning strategy should be easy to operate in order to reduce the computation burden. In existing researches, population size tuning methods based on some simple and deterministic rules, such as monotonically increasing or decreasing the population size, have been found to be very effective to enhance the
performance of several other kinds of EAs (de Oca et al., 2011; Tanabe and Fukunaga, 2014). Considering the above reasons, we designed a population reduction strategy for EDA to dynamically change its population size. At each generation, we apply the following equation to calculate the new population size for next generation:
PS $^{t+1}=\operatorname{Round}\left[\mathrm{PS}_{\max }-\left(\mathrm{PS}_{\max }-\mathrm{PS}_{\min }\right) \frac{\mathrm{FEs}^{t}}{\mathrm{FEs}_{\max }}\right]$
where $P S^{t+1}$ denotes the population size in $(t+1)$ th generation, $P S_{\max }$ and $P S_{\min }$ are the defined maximum and minimum population size, respectively. FEs $^{t}$ and $\mathrm{FEs}_{\max }$ denote the consumed total number of fitness evaluations (FEs) in the first $t$ generations and the allowed maximum number of evaluations, respectively. Round $(t)$ is a rounding function. At the first generation, the initial population size is equal to $P S_{\max }$. After that, the population size is decreased linearly until it reach the defined minimum value $P S_{\min }$.

PS $_{\text {max }}$ and PS $_{\text {min }}$ play different roles in affecting the performance of EDA. $P S_{\max }$ directly affects the exploration ability of EDA at the earlier search stage. A larger value for it could encourage the exploration but may reduce the convergence rate. While a smaller value for $P S_{\max }$ would make it lose its effect. We will experimentally analyse the effect of $P S_{\max }$ in Section 4.1. As for $P S_{\min }$, on the one hand, it should be as small as possible to accelerate the convergence at the latter stage; on the other hand, it need to ensure that EDA could properly estimate the Gaussian model based on the current population. Considering that the full CM of Gaussian model totally has $0.5\left(n^{2}+n\right)$ parameters need to be estimated, we suggest setting $P S_{\min }=0.5\left(n^{2}+n\right)$.

### 3.4. Procedure of EDA-R1M-PR

Integrating the new model estimation method and the population reduction strategy into GEDA, we can get the procedure of EDA-R1MPR presented in Algorithm 3. In steps 1 and 2, EDA-R1M-PR initializes the parameters and generates the initial population randomly and uniformly in the solution space. In steps 4 and 5 , the population are evaluated and a set of promising solutions are selected using the truncation selection rule. Then in steps 6-8, the new mean $\hat{\boldsymbol{\mu}}^{t}$ and covariance matrix $\hat{C}^{t}$ are estimated according to the improved estimation method and a new Gaussian model is built. Before sampling new solutions for the next generation, the population size is decreased using the population reduction strategy in step 9 . We also employ an elitism strategy by maintaining the best solution in current generation to the next generation in step 11, so only $\left(P S^{t+1}-1\right)$ new solutions are generated in step 10. The above steps are iterated until a stopping criterion is met, such as the $\mathrm{FEs}_{\max }$ is reached or the algorithm cannot find better solution in a number of consecutive generations.

Compared to the traditional ML estimation method, the improved model estimation method doesn't increase the computation complexity in the model building process. The computation complexity of the linear population reduction strategy is just $O(1)$. So the overall computation complexity of EDA-R1M-PR is the same with that of the traditional multivariate GEDA.

[^0]
[^0]:    Algorithm 3: Procedure of EDA-R1M-PR
    1 Initialize selection ratio $r, \eta_{\max }, P S_{\max }$ and $P S_{\min }$;
    2 Set $t=0$, population size $P S^{t}=P S_{\max }$, generate the initial population $P^{t}$;
    3 while the stopping criterion is not met do
    4 Evaluate population $P^{t}$ and update the best solution $\boldsymbol{b}$ obtained so far;
    5 Select the best ; $r P S^{t}$; solutions from $P^{t}$ and store them into $S^{t}$;
    6 Estimate $\hat{\boldsymbol{\mu}}^{t}$ according to Eqs. (4)-(6) and Algorithm 2;
    7 Estimate $\hat{C}^{t}$ according to Eq. (7);
    8 Build a new probabilistic model $G^{t}$ based on $\hat{\mu}^{t}$ and $C^{t}$;
    9 Compute the new population size $P S^{t+1}$ according to Eq. (16);
    10 Generate $\left(P S^{t+1}-1\right)$ new solutions by sampling from $G^{t}$ and store them into $A^{t}$;
    11 Set $P^{t+1}=A^{t} \cup \boldsymbol{b}$ and update $t=t+1$;
    12 end
    13 retumb

## 4. Experimental studies

In this section, EDA-R1M-PR was tested on a set of 30 benchmark functions from IEEE CEC 2014 (Liang et al., 2013) to evaluate its effectiveness. These functions are shifted and rotated to ensure the solving difficulty, and they could be classified into four classes, including unimodal functions $f_{1}-f_{3}$, multimodal functions $f_{4}-f_{16}$, hybrid functions $f_{17}-f_{23}$, and composition functions $f_{23}-f_{30}$. More details of these functions can be found in (Liang et al., 2013).

In our experiments, each algorithm was tested on these functions with 30 dimensions (30D) and 50 dimensions (50D). 25 independent runs were conducted on each function with $\mathrm{FEs}_{\max }=10,000-D$ as the stopping criterion for each run. The function error value $\left(f(\boldsymbol{b})-f\left(\boldsymbol{x}^{*}\right)\right)$ of each run was recorded to evaluate the performance of an algorithm, where $\boldsymbol{b}$ is the obtained best solution and $\boldsymbol{x}^{*}$ is the optimal one. Note that the function error value (FEV) smaller than $10^{-6}$ was reported as zero.

### 4.1. Influence of parameters

There are four parameters in EDA-R1M-PR, including the truncation selection ratio $\tau$, shifting factor $\eta$, and the maximum population size $P S_{\max }$ and minimum population size $P S_{\min }$. The selection ratio was conventionally set as $\tau=0.35$. The value for the shifting factor $\eta$ could be adaptively obtained by the line search method presented in Algorithm 2 in Section 3.1. The value for $P S_{\min }$ was discussed in Section 3.3. In this section, we mainly focus on analyzing the influence of $P S_{\max }$. To achieve that, we tested EDA-R1M-PR on a variety of functions with different $P S_{\max }$ values. For brevity, only the results on two functions, i.e. unimodal function $f_{2}$ and multimodal function $f_{9}$, with 30D and 50D were reported.

Figs. 2 and 3 show the performance of EDA-R1M-PR on the two functions with 30D and 50D, respectively. It can be seen from Figs. 2(a) and 3 (a) that EDA-R1M-PR could obtain the optimum of $f_{2}$ with a wide range of $P S_{\max }$ values and its performance only deteriorates a little on $f_{2}$
![img-3.jpeg](img-3.jpeg)
(a) $f_{2}$
with 50D when $P S_{\max }=6000$. As for multimodal function $f_{9}$, EDAR1M-PR could also find the near optimal solution and its performance gradually becomes better with the increase of $P S_{\max }$. From Figs. 2 and 3, we can conclude that EDA-R1M-PR is rather robust to the change of $P S_{\max }$. A larger value for $P S_{\max }$ is helpful to enhance the exploration ability, and thus improves the performance on multimodal functions. On the other side, it also slows down the convergence speed on unimodal functions. To balance the performance of EDA-R1M-PR on different classes of functions, we set $P S_{\max }=100-D$ in the following experiments.

### 4.2. Effectiveness analysis

In this section, the effectiveness of the rank-one modification and the population reduction strategies is analyzed. For the convenience of analysis, we implemented two variants of EDA-R1M-PR:

1) EDA-R1M: the variant of EDA-R1M-PR without employing the population reduction strategy. Instead of using dynamic population size as EDA-R1M-PR, EDA-R1M sets its population size to a constant value, which is 1000 for functions with 30D and 2000 for functions with 50D. The comparison between EDA-R1M and EDA-R1M-PR could reflect the effectiveness of the population reduction strategy.
2) quasi-EDA-R1M: a variant strictly accompanying with EDA-R1M. It is developed only for verifying the effectiveness of the new CM estimation method (rank-one modification operation), but not for optimizing the test functions. At each generation, quasi-EDA-R1M estimates its covariance matrix based on the same solutions with EDA-R1M, but employs the traditional ML estimator described in Eqs. (2) and (3) instead of the improved estimation method described in Eqs. (4)-(6). Consequently, the efficiency of the R1M operation could be revealed by comparing the estimated CMs of EDA-R1M and quasi-EDA-R1M since the two algorithms use the same set of selected solutions but different estimation methods to estimate the CM.
![img-3.jpeg](img-3.jpeg)
(b) $f_{9}$

Fig. 2. Performance of EDA-R1M-PR with different $P S_{\max }$ values on functions with 30D.
![img-3.jpeg](img-3.jpeg)

Fig. 3. Performance of EDA-R1M-PR with different $P S_{\max }$ values on functions with 50D.

![img-4.jpeg](img-4.jpeg)

Fig. 4. The variation of the length of PDE's major axis on functions with 30D.

In addition to the above two variants, two other existing algorithms, i.e. EMNA ${ }_{\mathrm{R}}$ (Larrañaga and Lozano, 2001) and AMaLGaM (Bosman et al., 2008) are also included in the comparison. EMNA ${ }_{R}$ is a representative of the traditional multivariate GEDA. AMaLGaM is an efficient GEDA variant employing the techniques of AVS, SRD and AMS. The population size and selection ratio of EMNA $_{R}$ and AMaLGaM are all set to the same with that of EDA-R1M to make a fair comparison. AMaLGaM also employs a full covariance matrix and its other parameters are all set to the same values in its original paper (Bosman et al., 2008).

Fig. 4 presents the variation of the length of PDE's major axis on two functions with 30D, respectively. It can be seen from Fig. 4 that the length of the major axis of EDA-R1M is generally not smaller than that of quasi-EDA-R1M during the whole evolution, especially in the initial stage. This conclusion is also valid for other non-major axes, which is consistent with the conclusion in Theorem 1. Fig. 5 shows the variation of the cosine of the angle between the major axis and $\hat{\delta}$ (denoted as $\cos \left(\vartheta_{1}\right)$ ). The results in Fig. 5 indicate that the value of $\cos \left(\vartheta_{1}\right)$ obtained by EDA-R1M is always no less than the value obtained by quasi-EDAR1M. That is to say, the angle between $\hat{\delta}$ and the major axis of the PDE of EDA-R1M is not greater than that of quasi-EDA-R1M. This phenomenon is in line with the conclusion in Theorem 2. The results in Figs. 4 and 5 demonstrate that the R1M operation could actually enlarge the search scope and help the algorithm find better main search direction.

Fig. 4 also shows the variation of the length of the major axis of EMNA $_{R}$. It can be observed that the major axis length of EDA-R1M is
![img-5.jpeg](img-5.jpeg)
usually larger than that of EMNA $_{R}$ in the earlier search stage, which is beneficial to explore promising solution regions. While in the latter stage, the major axis length of EDA-R1M quickly decreases and its search effort is focused in a relatively small region. As a result, the exploitation ability of EDA-R1M is improved to refine the quality of promising solutions more efficiently. To further demonstrate the performance difference between EDA-R1M and EMNA $_{R}$, Fig. 6 presents the variation of the cosine of the angle between the PDE's major axis and the steepest descent direction (denoted as $\cos \left(\vartheta_{2}\right)$ ) of the two algorithms on functions with 30D, where the steepest descent direction is defined as the direction from the current mean to the optimal solution $\left(\mathbf{x}^{\circ}-\hat{\mu}\right)$. As shown in Fig. 6(a), EDA-R1M could always achieve larger cosine value than EMNA $_{R}$ on $f_{2}$, and it could find the steepest descent direction after only a few generations. As for $f_{9}$, EDA-R1M also obtains better search direction than EMNA $_{R}$ in the earlier search stage. Fig. 7 present the variation of the FEV obtained by EDA-R1M and EMNA $_{R}$, it is clear that EDA-R1M demonstrates excellent performance on $f_{2}$, and also achieves far better results than EMNA $_{R}$ on $f_{9}$ even though they are both trapped into local optima.

Fig. 7 also shows the evolution of the FEV derived from EDA-R1MPR and AMaLGaM. The effectiveness of the population reduction strategy could be verified by comparing the performance of EDA-R1M and EDA-R1M-PR. It can be observed from Fig. 7(a) that both EDA-R1M and EDA-R1M-PR obtain the optimal solution of $f_{2}$, with the former keeping a fast improvement tendency and the latter gradually improving its convergence rate by reducing the population size. Although the population reduction strategy slows down the convergence in the
![img-6.jpeg](img-6.jpeg)

Fig. 5. The variation of the cosine of the angle between the major axis and $\hat{\delta}$ on functions with 30D.

![img-7.jpeg](img-7.jpeg)

Fig. 6. The variation of the cosine of the angle between the major axis and the steepest descent direction on functions with 30D.
early stage, it is beneficial to explore more promising solution regions and avoid premature convergence. Taking advantage of this property, EDA-R1M-PR could usually achieve better results on relatively complicated multimodal functions like $f_{9}$. As for AMaLGaM, we can see from Fig. 7 that it is outperformed by EDA-R1M and EDA-R1M-PR on both functions.

### 4.3. Comparison with other state-of-the-art EAs

To further assess the efficiency of EDA-R1M-PR, we compare it with AMaLGaM (Bosman et al., 2008), IPOP-CMA-ES (Auger and Hansen, 2005), BL-PSO-5 (Chen et al., 2017b), L-SHADE (Tanabe and Fukunaga, 2014), MVC_E_S_C (Zhang et al., 2017), as well as EDA-R1M. AMaLGaM is a representative of efficient EDA variant. IPOP-CMA-ES improves the famous CMA-ES by restarting CMA-ES with increasing population size when it gets stuck (Auger and Hansen, 2005). IPOP-CMA-ES was showed to be very competitive to many other efficient EAs developed in recent years (García-Martínez et al., 2017). BL-PSO-5 merges PSO with biogeography-based learning strategy. Numeric simulation indicated that BL-PSO-5 outperforms several well-designed PSO variants and EAs (Chen et al., 2017b). L-SHADE improves the success-history based adaptive DE (SHADE) (Tanabe and Fukunaga, 2013) with a linear population size reduction scheme, it is the winner of the CEC 2014 Competition on Real-parameter Single Objective optimization (Tanabe and Fukunaga, 2014). MVC_E_S_C incorporates three efficient DEs including EPSDE (Mallipeddi et al., 2011), SHADE and CoBiDE (Wang et al., 2014) into a multiple variants coordination (MVC) framework,
![img-8.jpeg](img-8.jpeg)
(a) $f_{2}$
which could adaptively select the most suitable optimizer for different search stages and preserve promising solutions for multiple DE optimizers. It was reported that MVC_E_S_C could outperform several up-todata DEs (Zhang et al., 2017). Besides the above algorithms, EDA-R1M is also included in the comparison to comprehensively investigate the effectiveness of the two components of EDA-R1M-PR, i.e. the rank-one modification operation and population reduction strategy.

We employed the source code of IPOP-CMA-ES provided by the author of (Loshchilov, 2013), and directly took the experimental results of BL-PSO-5, L-SHADE and MVC_E_S_C from their original papers. Cohen's $d$ effect size (Cohen, 1988) was employed to measure the performance difference between EDA-R1M-PR and other algorithms. Cohen's $d$ effect size is a simple and robust measure for quantifying the difference between two groups of data, it relies less on the sample size. Generally, a "small", "medium", and "large" effect is considered if the magnitude of effect size falls within $[0.2,0.3),[0.3,0.8)$ and $[0.8$, $+\infty$ ), respectively. Tables 1 and 2 summarize the experimental results of the above seven algorithms on the 30 CEC 2014 benchmark functions with 30D and 50D, respectively, where " + ", " - ", and " = " denote that the result of an algorithm is better than, worse than, and similar to that of EDA-R1M-PR, respectively. Besides, the best results in Tables 1 and 2 are highlighted in bold. From Tables 1 and 2, we can summarize that:

1) For unimodal functions $f_{1} \cdot f_{3}$, EDA-R1M-PR and EDA-R1M obtain the global optima for the three functions with both 30D and 50D, so does IPOP-CMA-ES. AMaLGaM and L-SHADE achieve fine results on these functions with 30D, but they both show performance
![img-9.jpeg](img-9.jpeg)

Fig. 7. The variation of the FEV on functions with 30D.

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

deterioration on one function when $D$ is increased to 50 . MVC_E_S_C finds the optimal solutions of two functions with 30D, but the corresponding number decreases to one when $D=50$. BL-PSO-5 performs worst since it fails to find desirable solutions for the three functions. The results indicate that the model with rank-one modification in EDA-R1M could effectively capture the structural characteristics of the optimization problem and thus improve the search efficiency.
2) For multimodal functions $f_{4}: f_{16}$, EDA-R1M-PR consistently provides the results of higher quality than other algorithms on four functions, i.e. $f_{6}, f_{7}, f_{9}$, and $f_{11}$. When $D=30$, EDA-R1M-PR performs no worse than AMaLGaM on all the 13 functions, and has an edge over IPOP-CMA-ES, BL-PSO-5, L-SHADE, MVC_E_S_C and EDA-R1M on 7, 8, 4, 5 and 8 functions, respectively. When $D=50$, EDA-R1M-PR is statistically better than the above six algorithms on $6,6,6,3,5$ and 7 functions, respectively, and is defeated by them on $3,5,6,9,8$ and 4 functions, respectively. These results indicate that EDA-R1M-PR performs slightly worse than L-SHADE and MVC_E_S_C, but better than the other algorithms on these multimodal functions.
3) Hybrid functions $f_{17}: f_{23}$ are a kind of partial separable functions, which can more closely approximate the real-world optimization problems (Tanabe and Fukunaga, 2014). Clearly, EDA-R1M-PR demonstrates the best performance on this group of functions since it outperforms almost all its competitors on all the 6 functions, except that it is defeated by L-SHADE on $f_{22}$ with 30D and is outperformed by L-SHADE and MVC_E_S_C on $f_{19}$ with 50D. Moreover, the results of EDA-R1M-PR are usually better than that of other algorithms over one order of magnitude.
4) As for composition functions $f_{23}: f_{30}$, the results obtained by the seven algorithms are far away from the optima. Nevertheless, EDAR1M-PR still shows certain superiority over other algorithms. It performs no worse than EDA-R1M on all the 8 functions with both 30D and 50D. Compared to AMaLGaM, BL-PSO-5 and L-SHADE, EDA-R1M-PR is only surpassed by them on 1, 2 and 1 functions with 30D, respectively, and on 1, 1 and 1 function with 50D, respectively. However, EDA-R1M-PR fails to defeat IPOP-CMA-ES and MVC_E_S_C on a majority of functions under both cases of 30D and 50D. The success of the two algorithms can be attributed to the capability to escape from local optima through the restart mechanism in IPOP-CMA-ES and the power of MVC framework.

The last rows of Tables 1 and 2 summarize the comparison results, it is evident that EDA-R1M-PR performs significantly better than AMaLGaM, IPOP-CMA-ES, BL-PSO-5 and EDA-R1M, and has an edge over L-SHADE and MVC_E_S_C. To further detect the performance differences of the above algorithms, the Friedman test was carried out to obtain their rankings on this set of functions. As shown in Table 3, EDAR1M-PR has the best ranking among these algorithms, EDA-R1M also performs surprisingly well and ranks the fourth when $D=30$ and the second when $D=50$.

In summary, EDA-R1M-PR performs the best among the seven

Table 3
Ranking of 7 algorithms on functions with 30D and 50D according to the Friedman test.

algorithms in case of this set of functions with 30D and 50D, which indicates that its two components do play an important role in improving its efficiency. The rank-one modification operation significantly enhances the search ability of GEDA by effectively adjusting the search scope and search direction. The population reduction strategy further improves the performance of EDA-R1M, especially on complicated functions, by taking advantage of its capability to balance the exploration and exploitation with the evolution.

## 5. Conclusion

In this paper, a novel EDA variant named EDA-R1M-PR is proposed for continuous optimization. EDA-R1M-PR first estimates a more promising search center by shifting the weighted mean of high-quality solutions along the fitness improvement direction through an adaptive line search method. Then it estimates a new covariance matrix with the shifted mean as the center, which is essentially the rank-one modification of the original covariance matrix. Theoretical and experimental studies both demonstrate that the R1M operation could effectively adjust the search scope and search direction of GEDA and thus improving its search efficiency. Moreover, we further extend EDA-R1M with a population reduction strategy that linearly reduces the population size throughout the evolution process. The PR strategy could adaptively balance the exploration and exploitation ability of EDA-R1M in different search stages and thus significantly improves its global optimization ability, especially on complicated multimodal functions. Experiments on a set of benchmark functions with 30D and 50D indicate that EDA-R1M-PR is robust to its parameters and competitive to several efficient EAs.

Our future work will focus on further investigating the properties of the rank-one modification operation and reducing the computational complexity of the model updating and sampling process. It is also of significance to evaluate the performance of EDA-R1M-PR on some challenging real-world optimization problems.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China [grant numbers 61873199, 61503300]; the China Post-Doctoral Science Foundation [grant numbers 2014M560784, 2016T90922]; the Fundamental Research Funds for the Central Universities [grant number xxy022019028]; and the Science and Technology Foundation of Foshan, China [grant number 2016AG101813].
