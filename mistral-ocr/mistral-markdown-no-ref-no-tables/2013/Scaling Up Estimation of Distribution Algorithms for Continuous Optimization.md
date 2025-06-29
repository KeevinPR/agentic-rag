# Scaling Up Estimation of Distribution Algorithms for Continuous Optimization 

Weishan Dong, Tianshi Chen, Peter Tiño, and Xin Yao, Fellow, IEEE


#### Abstract

Since estimation of distribution algorithms (EDAs) were proposed, many attempts have been made to improve EDAs' performance in the context of global optimization. So far, the studies or applications of multivariate probabilistic modelbased EDAs in continuous domain are still mostly restricted to low-dimensional problems. Traditional EDAs have difficulties in solving higher dimensional problems because of the curse of dimensionality and rapidly increasing computational costs. However, scaling up continuous EDAs for large-scale optimization is still necessary, which is supported by the distinctive feature of EDAs: because a probabilistic model is explicitly estimated, from the learned model one can discover useful properties of the problem. Besides obtaining a good solution, understanding of the problem structure can be of great benefit, especially for black box optimization. We propose a novel EDA framework with model complexity control (EDA-MCC) to scale up continuous EDAs. By employing weakly dependent variable identification and subspace modeling, EDA-MCC shows significantly better performance than traditional EDAs on high-dimensional problems. Moreover, the computational cost and the requirement of large population sizes can be reduced in EDA-MCC. In addition to being able to find a good solution, EDA-MCC can also provide useful problem structure characterizations. EDA-MCC is the first successful instance of multivariate model-based EDAs that can be effectively applied to a general class of up to 500-D problems. It also outperforms some newly developed algorithms designed specifically for large-scale optimization. In order to understand the strengths and weaknesses of EDA-MCC, we have carried out extensive computational studies. Our results have revealed when EDA-MCC is likely to outperform others and on what kind of benchmark functions.


Index Terms-Estimation of distribution algorithm, large-scale optimization, model complexity control.

[^0]
## I. INTRODUCTION

ESTIMATION of distribution algorithms (EDAs) [1], [2] have been intensively studied in the context of global optimization. Compared with traditional evolutionary algorithms (EAs) such as genetic algorithms (GAs) [3], there is neither crossover nor mutation operator in EDA. Instead, EDA explicitly builds a probabilistic model of promising solutions in a search space. Then, new solutions are sampled from the model that presents extracted global statistical information from the search space. EDA uses the model as guidance of reproduction to find better solutions. Actually, any EA has an underlying probabilistic model explaining its reproduction behaviors. But in traditional EAs, the underlying model is usually implicitly expressed through evolutionary operators. Once the model is explicitly presented, the algorithm can then be classified as an instance of EDA. EDAs were proposed originally for combinatorial optimization. Research on EDAs has been extended from discrete domain to continuous optimization, and much progress has been made. In this paper, we focus on EDAs in a single objective continuous optimization domain.

Many studies on EDA have been done in the last decade. In general, so far there are two major branches of continuous EDAs. One is based on Gaussian distribution model, which is the most widely used and intensively studied [2], [4][11]. The other major branch is based on histogram models [6], [12]-[19]. However, most of the existing studies have the common problem that the performance of EDA is only validated on relatively low-dimensional problems (often much smaller than hundreds of variables). The performance of EDA on higher dimensional problems (e.g., 500-D) is rarely studied. On the other hand, large-scale optimization using other EAs has already become a hot topic in recent years [20]-[23].

As we can see in the following sections, the reason for this is not that researchers simply ignored EDA, but that continuous EDAs have difficulties in high-dimensional search space. Due to relying on learning a model from samples, EDAs heavily suffer from the well-known curse of dimensionality [24]. If considering multidependencies of variables to solve nonseparable problems more effectively, traditional EDAs' fast increasing computational costs also make them impractical to real-world applications. In this paper, we propose a novel EDA framework with model complexity control (MCC), named EDA-MCC, to scale up EDA for continuous optimization. By employing weakly dependent variable identification (WI)


[^0]:    Manuscript received February 26, 2011; revised January 8, 2013; accepted February 8, 2013. Date of publication February 14, 2013; date of current version November 26, 2013. This work was supported in part by EPSRC under Grant EP/J017515/1 to X. Yao, by the National Natural Science Foundation of China under Grant 61100163 to T. Chen, and by the China Scholarship Council under a Scholarship to W. Dong to support his visit to the University of Birmingham, where part of this work was done. The work of X. Yao was also supported by the Royal Society Wolfson Research Merit Award. The work of P. Tiño was supported by a BBSRC Grant BB/H012508/1.
    W. Dong was with the Key Laboratory for Complex Systems and Intelligence Science, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China. He is now with IBM Research-China, Beijing 100193, China (e-mail: weishan.dong@gmail.com).
    T. Chen is with the Institute of Computing Technology, Chinese Academy of Sciences, Beijing 100190, China (e-mail: chemianshi@ict.ac.cn).
    P. Tiño and X. Yao are with the Centre of Excellence for Research in Computational Intelligence and Applications, School of Computer Science, University of Birmingham, Birmingham B15 2TT, U.K. (e-mail: p.tino@cs.bham.ac.uk; x.yao@cs.bham.ac.uk). Digital Object Identifier 10.1109/TEVC.2013.2247404

and subspace modeling (SM) in EDA-MCC, we can explicitly control the model complexity to establish a tradeoff between: 1) the performance that may benefit from a complex model and 2) the computational and population complexities that grow rapidly with the problem size and the model complexity. By doing so, EDA-MCC can suffer less from the curse of dimensionality. Experimental comparisons on 13 well-known benchmark functions validate the effectiveness and efficiency of EDA-MCC. We find that EDA-MCC have significant advantages over traditional EDAs when solving large-scale nonseparable problems with few local optima (up to 500-D in experiments) in terms of solution quality and computational cost. The significant difference between EDA-MCC and traditional EDAs with model complexity penalization is also discussed. According to the No Free Lunch Theorem [25], the limitations of EDA-MCC are also analyzed.

If traditional EDAs are not appropriate for large-scale optimization, why do we still strive to scale it up? Our motivation is based on a distinctive advantage of applying EDA compared with other EA: users can discover useful properties of the problem from the learned probabilistic model. Since the model is explicitly built in EDA, it is feasible to observe the learned model structure and its parameters to understand some natures of the problem. For simple univariate (marginal distribution) model-based EDAs, because the interdependencies among variables are completely ignored, it is almost impossible to extract information representing the interdependency of variables or other structural information. On the other hand, multivariate model-based EDAs have such potentials. In EDAMCC, multidependency is maintained to retain the potentials, while with the degree of model complexity explicitly controlled. To the best of our knowledge, EDA-MCC is the first attempt at scaling up multivariate model-based EDA for largescale continuous optimization (up to 500-D problems).

The remainder of this paper is organized as follows. In Section II, the difficulties of traditional EDAs on high-dimensional problems are analyzed, especially for Gaussian-based EDAs. In Section III, WI and SM for EDA-MCC are presented in the context of Gaussian model. The difference between EDAMCC and previous EDAs with model complexity penalization is also discussed. Experimental studies on 50-500-D problems are given in Section IV. In Section V, the dependence of EDA-MCC on its WI and SM parameters is investigated. The scalability of EDA-MCC is studied in Section VI. In Section VII, random partitioning-based SM is compared with a clustering-based SM, the advantage of random partitioning in high-dimensional search space is verified. The problem structure characterization capability of EDA-MCC is demonstrated in Section VIII. In Section IX, the interactions between WI and SM are analyzed. Conclusions are drawn in Section X, and future work is discussed.

## II. Difficulties of EDAs on High-Dimensional PROBLEMS

## A. Related Work

A typical EDA flow is shown in Fig. 1. Each individual in the population presents a solution. One iteration of the loop refers to one generation of evolution.

## EDA

Initialize a population $\mathcal{P}$ by generating $M$ individuals randomly.
Repeat until a stopping criterion is met.

1) Select $m \leq M$ individuals from $\mathcal{P}$.
2) $f(\vec{x}) \leftarrow$ Estimate a probability density function from the selected individuals.
3) $\mathcal{P}^{\prime} \leftarrow$ Sample a number of individuals from $f(\vec{x})$.
4) Combine $\mathcal{P}$ and $\mathcal{P}^{\prime}$ to create the new $\mathcal{P}$.

Fig. 1. Typical EDA flow.

The primary difference between different EDAs is the probabilistic model adopted. When adopting a Gaussian distribution model, the $f(\widehat{x})$ in Fig. 1 has the form of a normal density that is defined by a mean vector $\widehat{\mu}$ and a covariance matrix $\boldsymbol{\Sigma}$. The earliest proposed Gaussian-based EDAs are based on simple univariate Gaussian, such as UMDA ${ }_{\mathrm{c}}^{G}$ [2] and $\mathrm{PBIL}_{\mathrm{c}}$ [4]. In these EDAs, all variables are regarded independent of each other. The simplicity of such models makes them easy to implement and the algorithms are characterized by a low level of computational complexity. Also due to the simplicity, they may have difficulties in solving problems whose variables have strong interdependencies. To remedy this, several EDAs based on multivariate Gaussian have been proposed, such as EMNA ${ }_{\text {global }}$ [2], normal IDEA [5], [6], and EGNA [2], [7]. EMNA ${ }_{\text {global }}$ adopts a conventional maximum likelihood estimated multivariate Gaussian distribution defined by $\widehat{\mu}$ and $\boldsymbol{\Sigma}$. In normal IDEA and EGNA, after obtaining the maximum likelihood estimation (MLE) of $\widehat{\mu}$ and $\boldsymbol{\Sigma}$, a graphical factorization, that is, a Bayesian factorization (i.e., a Gaussian network) is constructed, usually by greedy search. Constructing graphical factorization introduces additional computational complexity along with MLE, but the computational time in solution sampling can be reduced. On the other hand, if we want to sample new solutions from a conventional multivariate Gaussian distribution as in EMNA global, decomposing $\boldsymbol{\Sigma}$ is a must [26]. Since these EDAs are essentially based on the same multivariate Gaussian distribution, their performances are similar-at least no significant superiority of one over another has been reported so far. ${ }^{1}$ Later, some extensions of these EDAs have been proposed to improve their poor explorative ability, such as EEDA [8], CT-AVS-IDEA [9], and SDR-AVSIDEA [10]. These EDAs scale $\boldsymbol{\Sigma}$ according to some criterions after MLE. A comparative study of different covariance matrix scaling strategies can be found in [11]. Besides these single Gaussian-based EDAs, EDAs adopting Gaussian mixture distribution [27]-[33] have been proposed for solving multimodal and hard deceptive problems. Hybrid optimization algorithms based on Gaussian EDAs have also been proposed [34], [35].

Interestingly, previous studies have shown that although Gaussian models cannot always offer an accurate estimation of

[^0]
[^0]:    ${ }^{1}$ Some comparisons between EMNA global and EGNA can be found in [2]. However, few comparisons involving normal IDEA have been made.

the true distribution of promising solutions, they can nevertheless provide useful information for guiding the global search on many unimodal and some, but not all, multimodal problems. So far no satisfactory explanation of this phenomenon has been presented in the literature. It will be interesting in the future to study when a multimodal problem is easy or hard for a given single Gaussian-based EDA, e.g., by using recently proposed analytical approaches [36]-[39]. However, except for univariate Gaussian-based EDAs, most (if not all) existing studies of multivariate Gaussian-based EDAs are restricted to low-dimensional problems.

Continuous EDAs using histogram models include several EDAs based on univariate histogram [6], [12], [13], [15], [18] and some based on multivariate histogram [14], [16], [17], [19]. Histogram models are more flexible than Gaussian models because of the convenience to describe arbitrary multimodality. However, if considering multiple variable dependencies such as full interdependency, the required number of bins can increase exponentially with problem size [40], which makes multivariate histogram models hard to be applied to large-scale nonseparable problems in practice. Although some efforts have been made to improve the scalability of multivariate histogram model-based EDAs [14], [16], most existing results of these EDAs are also restricted to lowdimensional problems ( $\leq 50-\mathrm{D}$, even lower than multivariate Gaussian-based EDAs).
To the best of our knowledge, there have been only a few attempts of studying continuous EDA on large-scale ( $\geq 500$ D) problems, including: 1) a univariate model based EDA, LSEDA-gl, proposed by Wang and Li [41]; 2) application of UMDA ${ }_{k}^{G}$ and EGNA as logistic regression regularizers on a "large $k$ (genes), small $N$ (samples)" microarray classification problem, proposed by Bielza et al. [42]; 3) study of parallel implementation of EGNA $_{E E}$ on sphere function, proposed by Mendiburu et al. [43]; and 4) studies of a Gaussian EDA, namely AMaLGaM, on up to 1000-D problems done by Bosman [44]. However, these attempts have their limitations. LSEDA-gl is a univariate EDA where a mixed Gaussian and Lévy distribution is adopted. As discussed, it lacks the capability of modeling multidependencies. In [42], a multivariate EDA was utilized as a parameter optimizer of a logistic regression model with (order of) 500 parameters, trained via constrained maximum likelihood. The parameters were constrained to certain intervals, effectively regularizing the model. However, the general performance of the multivariate EDA on broader types of high-dimensional problems is still unknown. In [43], the study focuses on the parallel multivariate EDA's performance in terms of speed up of execution time but not on solution quality, and only one test function is involved in experiment. In [44], variants of AMaLGaM (with or without memory) using univariate Gaussian, Bayesian factorized (multivariate) Gaussian, and multivariate Gaussian with full covariance matrix were tested on problems up to 1000-D, 400-D, and 200-D, respectively. As can be seen, multivariate models' higher complexities reduce the size of applicable problems. In this paper, from a totally different perspective from [44], we propose a novel scalable multivariate EDA framework that is simpler in design yet capable of
solving even larger problems. An open and important question is: Can we expect promising performance and moderate computational cost of multivariate EDAs on larger scale problems?

## B. Curse of Dimensionality

Since EDAs completely rely on probabilistic models built from finite data samples, they must suffer from the well-known curse of dimensionality [24]. The more flexible and complex the model is, the more data it requires to yield a reliable estimation and to sustain enough good performance. According to the curse of dimensionality theory, the amount of data to sustain a given spatial density increases exponentially with the dimensionality of the search space. This will adversely impact any method based on spatial density, unless the data follows certain simple distributions. Obviously the latter condition is not always satisfied in practice. The population size of EDA has to grow quickly as the problem size grows to sustain good performance. Since EDA tries to learn some global statistical information from $m$ sampled data (i.e., individuals selected from the population of $M$ individuals, see Fig. 1), $m$ has to be sufficiently large, which also requires a large population size $M$ when some level of selection pressure needs to be maintained. Of course, the demand of the increasing population size can be of different levels when models have different levels of complexity. For simple univariate EDAs, when solving an $n$-dimensional problem, it estimates $n 1-\mathrm{D}$ distributions independently. When population size $M$ is large enough for estimating these $n$ distributions and finding good enough solution, $M$ does not necessarily grow as $n$ grows. However, for multivariate models, the more degrees of freedom make them usually require larger population sizes, which can be validated from our experiments. When the problem size is large, EDAs with complex multivariate models can become inapplicable because the large population size may consume considerable computational resources (see Section II-C). There is an urgent need for techniques that can reduce the required computational resources without affecting (too much) the precisions of learning a probabilistic model.

Since previous results (e.g., [6]) have shown that: 1) Gaussian models suffer less from the curse of dimensionality than histogram models, which is reasonable because Gaussian models usually have much fewer degrees of freedom, and 2) single Gaussian models have fewer degrees of freedom than Gaussian mixture models, in the following sections, we focus on using single multivariate Gaussian models to scale up EDA. Univariate Gaussian models are also involved in analysis and experiments. However, it should be noticed that our conclusions can be generalized and are not restricted only to Gaussian models. Although previous research has shown that single Gaussian model-based EDAs can perform well on many unimodal and multimodal problems, they still have known limitations other than the effect of the curse of dimensionality. Specifically, Gaussian EDAs using MLE are supposed to have poor explorative ability. Theoretical analysis of UMDA ${ }_{k}^{G}$ [45], [46] proved that the maximal distance that the mean of the population can move across the search space is bounded, and the algorithm is guaranteed to converge since the population

TABLE I
SUMMARY OF ONE-GENERATION COMPUTATIONAL COMPLEXITY


variance converges to zero. Although theoretical analysis have not been developed, similar results of multivariate Gaussianbased EDAs using MLE were also observed in experimental studies [9], [11], [28], [47]. Therefore, several Gaussianbased EDAs with covariance matrix scaling [8]-[10] were proposed. But the effectiveness of these techniques in very high-dimensional search space still lacks validation.

## C. Computational Cost

Besides the curse of dimensionality, computational cost of an EDA (especially multivariate EDA) can also restrict its application to large-scale problems. In an EDA, if excluding fitness evaluation, the model estimation and subsequent solution sampling determine its overall computational complexity, which also depends on the model complexity. In general, univariate EDAs have lower level of computational complexity than multivariate EDAs. Empirical studies can show that, even for problems whose fitness function evaluation is not too timeconsuming, multivariate EDAs' overall runtime can become unacceptable in practice. Here we consider the computational complexity brought by the model within one generation. For two representative EDAs of different model complexities: a univariate Gaussian EDA, UMDA ${ }_{c}^{G}$ [2], and a multivariate Gaussian EDA, EMNA ${ }_{\text {global }}$ [2], analytical computational complexities in terms of data access are given as below. Suppose the current model is estimated from the selected individuals of the last generation. $M$ denotes the population size, and $m$ denotes the number of selected individuals, $m=\tau M$, usually $0.3 \leq \tau \leq 0.5$ [2], [28]. The computational complexities of UMDA ${ }_{c}^{G}$ and EMNA $_{\text {global }}$ are shown in Table I. For detailed computation please see Appendix A.

UMDA ${ }_{c}^{G}$ and any other univariate Gaussian EDAs share the same model structure and only differ in the way the model parameters are updated. These EDAs share mostly the same level of computational complexity. However, different multivariate Gaussian EDAs have different computational complexities. As mentioned above, EMNA global estimates model via MLE and sampling solutions via decomposition of covariance matrix, while normal IDEA and EGNA build a graphical factorization after MLE, and then fit the parameters of the factorization and sample solutions by traversing the graph. The MLE in all three is exactly the same, and thus, they share a same computational complexity in this step. For the latter steps, EMNA global's computational complexity is easy to analyze since decomposing a covariance matrix constantly costs cubic time with problem size. Whereas the graphical factorization in normal IDEA and EGNA can be obtained by several different structure search algorithms, whose computational complexities depend on the specific algorithms and the data samples. After obtaining the structure, in normal IDEA, the conditional
variances of the factorization are computed by the inverse of covariance matrix [5], which costs the same computational complexity as decomposing a covariance matrix. We can infer that normal IDEA's computational complexity is higher than that of EMNA global. In EGNA, the parameters of Gaussian network are computed in a different way, making the computational cost difficult to establish analytically. Literature on EGNA did not provide analytical computational complexity either. Also, considering the fact that multivariate Gaussianbased EDAs with covariance matrix scaling have additional computations, here we choose EMNA global as the representative of all multivariate Gaussian EDAs to analyze the computational complexity. The analysis of EMNA global approximately gives a lower bound of all multivariate Gaussian EDAs.

As mentioned above, when a univariate model is sufficient for solving a problem, $M$ and $m$ do not necessarily grow as $n$ grows. Table I shows that, in this case, the overall computational cost of univariate EDAs, such as UMDA ${ }_{c}^{G}$, can grow linearly with $n$. Although the model's simplicity can restrict its performance, its computational cost grows mildly. On the other hand, the overall computational cost of multivariate Gaussian EDAs, such as EMNA global, grows much faster. Although [9] reported that a necessary $M$ grows approximately with $\sqrt{n}$ for normal IDEA, in practice it is usually true that $M>m>n$. Overall computational cost of a typical multivariate Gaussian EDA thus grows at least with $O\left(n^{3}\right)$. In Section IV, more illustrative comparisons of CPU time will be made by experimental studies.

## III. SCALING UP EDA: EDA-MCC

In short, there are three requirements to be met to scale up multivariate model-based EDA to large-scale problems.

1) Multivariate search needs to be preserved as much as possible.
2) Computational cost must be acceptable and grow mildly.
3) Running with small population sizes is preferred.

It can be seen that the differences in performance and computational complexity between EDAs using univariate Gaussian and multivariate Gaussian models are essentially relevant to the complexity of the Gaussian model. Intuitively, univariate Gaussian has simple structure and lower computational cost, but has difficulty in characterizing complicated interdependencies between variables. Multivariate Gaussian has complex structure and thus higher computational cost, but can effectively model interdependencies between variables. There is a need for an appropriate tradeoff between model complexity and computational cost such that an EDA can have promising performance on nonseparable problems with mild computational costs. We propose to reach such an attractive tradeoff in an EDA by two steps: WI and SM. The resulting EDA framework is called EDA-MCC.

## A. Weakly Dependent Variable Identification (WI)

A multivariate Gaussian represents the (linear) interdependencies between variables by their covariances. According to the definition of covariance, we have

$$
\operatorname{cov}\left(X_{i}, X_{j}\right)=E\left(\left(X_{i}-\mu_{i}\right)\left(X_{j}-\mu_{j}\right)\right)
$$

![img-0.jpeg](img-0.jpeg)
(a)
![img-1.jpeg](img-1.jpeg)
(b)
![img-2.jpeg](img-2.jpeg)
(c)

Fig. 2. Demonstrations of 2-D Gaussian distributions with different correlation coefficients. The contours denote the Gaussian densities. In every subfigure, each of the two variables has a standard deviation equal to 1 ; so, here the correlation coefficient equals the covariance. (a) Correlation $=0$. (b) Correlation $=0.3$. (c) Correlation $=0.9$.
where $\operatorname{cov}\left(X_{i}, X_{j}\right)$ is the covariance between variables $X_{i}$ and $X_{j}, i, j=1, \ldots, n, E$ is the expected value operator. We also have

$$
\operatorname{corr}\left(X_{i}, X_{j}\right)=\frac{\operatorname{cov}\left(X_{i}, X_{j}\right)}{\sigma_{i} \sigma_{j}}
$$

where $\operatorname{corr}\left(X_{i}, X_{j}\right)$ is the linear correlation coefficient between $X_{i}$ and $X_{j}, \sigma_{i}$ and $\sigma_{j}$ are the standard deviations of $X_{i}$ and $X_{j}$ respectively, $\sigma_{i}>0, \sigma_{j}>0, i, j=1, \ldots, n$. According to the definition, a correlation coefficient cannot exceed 1 in absolute value. Thus, correlation coefficients can also be seen as normalized covariances.

Suppose during the evolutionary process of a multivariate Gaussian EDA, if at some generation, the correlation coefficients are close to zero, which means the observed linear dependencies between variables are weak, then the distribution that the model can learn will be little different from a univariate Gaussian. The algorithm's exhibited behavior in this generation does not differ much from a univariate Gaussian EDA, either. Fig. 2 shows an example of 2-D Gaussian distribution with different correlation coefficients. As can be seen, there is a tradeoff between: 1) the computational complexity and requirement of population size that increase with respect to a more complex model, and 2) the performance that potentially benefits from a complex model. In this case, we find that switching the current model to a univariate Gaussian can greatly reduce the computational complexity and the requirement of population size without significantly affecting the performance. In a way, the algorithm can ignore the weak correlations so that the search effort could be focused on stronger ones. Inspired by this, we first identify those approximately independent (weakly dependent/correlated) variables, and then apply a simple univariate model on them. We call this strategy the WI.

Weakly dependent variables can be identified by first calculating an $n \times n$ global correlation matrix, then picking out variables whose absolute values of correlation coefficients to all the other variables are no larger than a threshold $\theta$ $(0 \leq \theta \leq 1)$. The set of such weakly dependent variables, denoted by $\mathcal{W}$, is defined as

$$
\mathcal{W}=\left\{X_{i} \mid\left|\operatorname{corr}\left(X_{i}, X_{j}\right)\right| \leq \theta, \forall j=1, \ldots, n, j \not \equiv i\right\}
$$

## WI

1) Calculate an $n \times n$ global correlation matrix $\boldsymbol{C}$ based on $m_{\text {corr }}$ individuals. $\boldsymbol{C}_{i j}=\operatorname{corr}\left(X_{i}, X_{j}\right), i, j=$ $1, \ldots, n$.
2) Use $\boldsymbol{C}$ to construct $\mathcal{W}$ according to (3).
3) Estimate a univariate model for $\mathcal{W}$ based on the $m$ selected individuals.

Fig. 3. Main flow of weakly dependent variable identification (WI).

As can be seen, applying a univariate model on $\mathcal{W}$ implies explicitly removing the dependencies on the variables in $\mathcal{W}$, which can reduce the computational complexity. If a proper $\theta$ exists, a good tradeoff between the gain in computational cost and the loss of model precision can be found.

In contrast to weakly dependent, the rest of the variables are regarded as strongly dependent. The set of strongly dependent variables, denoted by $\mathcal{S}$, is defined as

$$
\mathcal{S}=\left\{X_{i} \mid X_{i} \notin \mathcal{W}, i=1, \ldots, n\right\}
$$

Let $\mathcal{V}$ denote the set of all variables $\mathcal{V}=\left\{X_{i} \mid i=1, \ldots, n\right\}$. Obviously, we have $\mathcal{V}=\mathcal{W} \cup \mathcal{S}$ and $\emptyset=\mathcal{W} \cap \mathcal{S}$.

Note that if we use a global correlation matrix for the purpose of identifying $\mathcal{W}$, we do not need a large number of samples as we do for estimating a reliable global covariance matrix for the purpose of guiding the search, even though computing a correlation matrix is essentially of no difference with computing a covariance matrix. Because the precision of covariance matrix directly impacts the sampling procedure and thus influences the algorithm's behavior, it does require a sufficiently large amount of data with respect to problem size. However, if we just use a correlation matrix for a coarse learning such as identifying weakly dependent variables, its precision does not directly influence the sampling. Later we will see that, with working with SM, a small sample size for WI (100 for 50-500-D problems) can be sufficient, which also helps reduce the computational cost of EDA-MCC.

Let $m_{\text {corr }}$ denote the sample size for constructing a global correlation matrix $\boldsymbol{C}$. The main flow of WI is depicted in

## SM

1) Construct $\mathcal{S}$ according to (4).
2) Randomly partition $\mathcal{S}$ into $\lceil|\mathcal{S}| / c\rceil$ non-intersected subsets: $\mathcal{S}_{1}, \mathcal{S}_{2}, \ldots, \mathcal{S}_{\lceil|\mathcal{S}| / c\rceil}$, where $c$ is a user specified parameter defining the maximal size of a subset $(1 \leq c \leq n)$.
3) Estimate a multivariate model for each subset based on the $m$ selected individuals.

Fig. 4. Main flow of subspace modeling (SM).

Fig. 3. Here, the term weakly dependent/correlated is not a strictly defined term as in the statistics domain. Whether a variable is classified into $\mathcal{W}$ or not is determined by both the correlation matrix at hand and the user specified parameter $\theta$. The correlation matrix reflects the observed information in the search space, while different values of $\theta$ can reflect the user's confidence on the univariate model. The larger $\theta$ is, the more probable that more variables are optimized by the univariate model. Then, less computational cost and a smaller population size may be required. In this paper, we find a proper value of $\theta=0.3$ for EDA-MCC (see Sections IV-VI) such that: 1) the model precision is only slightly worse; 2) the computational complexity and the requirement of population size are greatly reduced; and 3) the overall performance of EDA-MCC can be significantly better than the previous EDAs, at least on the 13 problems investigated in experiments.

Note that for non-Gaussian EDAs, weakly dependent may not be identical to weakly correlated. If applying WI to non-Gaussian models, the identification method may need redefinition. One can also imagine other ways of defining weakly/strongly dependent variables. For instance, the variables can be classified as weakly or strongly dependent by considering their correlation with the function to be optimized. The idea of separating weakly dependent variables from strongly dependent ones in this context is interesting and worth further consideration in the future. However, as typically done in EDA implementations, our definition of weak/strong dependency is restricted to variables only (within the context of building a local Gaussian model on the variables) and the model does not reflect any correlation between a variable and the function value.

## B. Subspace Modeling (SM)

Suppose we only have a small population size $M$ (and thus $m$ ), and $|\mathcal{S}|$ is still too large for $m$ samples to give a reliable estimation for a multivariate Gaussian model. To obtain better overall performance, as a tradeoff, we project the $m$ points to several subspaces of the $n$-dimensional search space, then build model and sample solutions on subspaces. When it is impractical to further increase $m$, building subspace models and using their combination to approximate the global estimation can be a good choice. We call it the SM, whose flow is shown in Fig. 4. Each subset of $\mathcal{S}$, i.e., group of variables, corresponds to a subspace. All the $m$ samples are


Fig. 5. Example of approximated global covariance matrix on $\mathcal{S}$ after performing SM. $\mathcal{S}=\left\{X_{1}, \ldots, X_{8}\right\}, c=3 .\left(X_{k 1}, \ldots, X_{k 8}\right)$ is a random permutation of $\left(X_{1}, \ldots, X_{8}\right)$. The three subsets of $\mathcal{S}$ are $\mathcal{S}_{1}=\left\{X_{k 1}, X_{k 2}, X_{k 3}\right\}$, $\mathcal{S}_{2}=\left\{X_{k 4}, X_{k 5}, X_{k 6}\right\}$, and $\mathcal{S}_{3}=\left\{X_{k 7}, X_{k 8}\right\}$.
projected to $\lceil|\mathcal{S}| / c\rceil$ subspaces, ${ }^{2}$ and we build a multivariate model for each subspace. The capacity $c$ indicates the maximal size of a subspace. It represents to what extent we trust the $m$ samples to give reliable estimation. By dividing the variables into several separated subspaces and projecting the samples to lower dimensional subspaces, the EDA only considers the local dependencies among variables belonging to the same subspace, and the density of samples for each subspace will increase. This technique probably offers a feasible way for alleviating the growth of population size with respect to a growing problem size, which will be validated by our experimental results in later sections.

After randomly partitioning $\mathcal{S}$, variables of different subsets are regarded independently. When we use a multivariate Gaussian to model each subspace, combination of all subspace Gaussian models can be seen as an approximation to the global Gaussian estimation on $\mathcal{S}$. The global mean vector on $\mathcal{S}$ is still identical to the combination of subspace models, but the global covariance matrix is approximated by a block diagonal matrix whose main diagonal blocks are the subspace covariance matrices. Fig. 5 shows an example. If $|\mathcal{S}| \leq c$, the variables can be kept together within one group. If $|\mathcal{S}|>c$, it means that the size of current $\mathcal{S}$ is beyond the capability of a global multivariate model that $m$ samples can estimate according to the user's experience or preference. Therefore, we have to make a concession by explicitly eliminating some dependencies between variables while keeping the rest. As will be shown later, WI and SM are performed in every generation, thus the random partition is not fixed throughout evolution. Variables from different subsets in current generation have the chance to be grouped in one subset and keep their interactions in the next generations. When sampling a new individual, its variables in $\mathcal{S}$ are sampled from the subspace models they belong to. Then they are concatenated with those sampled variables in $\mathcal{W}$. The evaluation of a newly sampled individual is the same as in traditional EDA.

The random subspace partitioning method proposed here is a simple and the most straightforward one. Experiments will show that although we use only the simplest SM method, it indeed significantly improves EDAs' performance on largescale problems. Of course, more sophisticated subspace partitioning can be developed. For example, $\mathcal{S}$ can be divided into several clusters of variables according to the correlation coefficients, and each cluster is regarded a subspace. However,

[^0]
[^0]:    ${ }^{2}$ For a real number $x,\lceil x\rceil$ is the smallest integer $y$, such that $y \geq x$.

it can be imagined that such techniques also heavily suffer from the curse of dimensionality. With a finite sample size, we cannot expect good clustering in very high-dimensional space. Section VII will present comparison between the random subspace partitioning and a clustering-based one. Experiments will show that the simple random partitioning can perform significantly better on large problems.

## C. Model Complexity Control: WI + SM

By incorporating WI and SM within the EDA framework, we explicitly control the model complexity: 1) WI reduces the model complexity by approximation of univariate model, and 2) SM further reduces the complexity of the multivariate part of the model by approximation of subspace models. Let $\mathcal{S}_{k}$ $(1 \leq k \leq\lceil|\mathcal{S}| / c\rceil)$ denote a subset of $\mathcal{S}$ and vector $\vec{s}_{k}$ denote realizations of the variables in $\mathcal{S}_{k}$. After performing WI and SM, the final joint pdf has the form

$$
f(\vec{x})=\prod_{X_{i} \in W} g_{i}\left(x_{i}\right) \prod_{k=1}^{\lceil|\mathcal{S}| / c\rceil} h_{k}\left(\vec{s}_{k}\right)
$$

where $g_{i}(\cdot)$ is the univariate pdf of variable $X_{i}$, and $h_{k}(\cdot)$ is the multivariate pdf of variables in $\mathcal{S}_{k}$. For instance, we can assign $g_{i}(\cdot)$ to a univariate Gaussian as (6) and assign $h_{k}(\cdot)$ to a multivariate Gaussian as (8).

Based on WI + SM, the main flow of the proposed EDA framework, namely EDA with model complexity control (EDA-MCC), is given in Fig. 6. The WI and SM steps in Fig. 6 are essentially the same as Figs. 3 and 4. As discussed above, for the purpose of coarse learning, $m_{\text {corr }}$ does not need to be as large as $m$. So we sample $m_{\text {corr }}$ individuals out of the $m$ selected individuals to calculate correlation matrix $\boldsymbol{C}$. Because duplicate samples cannot contribute to correlation estimation, sampling without replacement is adopted. Experiments in Sections IV-VI will show that a small $m_{\text {corr }}=100$ can work fine for problem sizes up to 500-D.

The comparison of computational complexity of EDAMCC, UMDA ${ }_{c}^{G}$, and EMNA ${ }_{\text {global }}$ is shown in Table II. For details of computation please refer to Appendix B. Because $m_{\text {corr }} \leq m$ and $c \leq n$, in a same number of generations, EDA-MCC's computational complexity is always between the complexities of a typical univariate Gaussian EDA and a typical multivariate one. Besides, if EDA-MCC requires smaller $m$ and $M$, the computational cost can be further reduced. Specifically, in experiments, we will apply a UMDA ${ }_{c}^{G}$ model as (6) for variables in $\mathcal{W}$, and an EEDA model mentioned in Section II for each subset of $\mathcal{S}$. EEDA [8] is a multivariate Gaussian EDA using covariance matrix scaling. After performing MLE, EEDA scales the covariance matrix by resetting its minimum eigenvalue to its maximum eigenvalue. EEDA regards the direction of the eigenvector with the minimum eigenvalue as an approximation to the fitness function's gradient. Previous studies [11], [35] have shown that by enlarging the variance along this direction, EEDA can have better explorative ability than EMNA ${ }_{\text {global }}$ and require smaller population sizes. Since the covariance matrix scaling can be done in $O(n)$ [11], EEDA has roughly the same computational complexity as EMNA global when using the

## EDA-MCC

Initialize a population $\mathcal{P}$ by generating $M$ individuals randomly.
Repeat until a stopping criterion is met.

1) Select $m \leq M$ individuals from $\mathcal{P}$.
2) Randomly sample $m_{\text {corr }} \leq m$ individuals from the $m$ selected individuals without replacement.
3) Build a model using WI+SM, as (5):
a) WI:
i) Calculate the correlation matrix $\boldsymbol{C}$ based on the $m_{\text {corr }}$ sampled individuals, $\boldsymbol{C}_{i j}=$ $\operatorname{corr}\left(X_{i}, X_{j}\right), i, j=1, \ldots, n$, as (2).
ii) Construct $\mathcal{W}$ based on $\boldsymbol{C}$, as (3).
iii) $\forall X_{i} \in \mathcal{W}$, estimate a univariate model $g_{i}(\cdot)$ based on the $m$ selected individuals.
b) SM:
i) Construct $\mathcal{S}$, as (4).
ii) Randomly partition $\mathcal{S}$ into $\lceil|\mathcal{S}| / c\rceil$ nonintersected subsets: $\mathcal{S}_{1}, \mathcal{S}_{2}, \ldots, \mathcal{S}_{\lceil|\mathcal{S}| / c\rceil}$, $1 \leq c \leq n$.
iii) Estimate a multivariate model $h_{k}(\cdot)$ for each subset $\mathcal{S}_{k}$ based on the $m$ selected individuals, $k=1, \ldots,\lceil|\mathcal{S}| / c\rceil$.
4) $\mathcal{P}^{\prime} \leftarrow$ Sample new individuals: Sample from $g_{i}(\cdot)$ and $h_{k}(\cdot)$ independently, then combine sampled variables into one reproduced individual.
5) Combine $\mathcal{P}$ and $\mathcal{P}^{\prime}$ to create the new $\mathcal{P}$.

Fig. 6. Main flow of EDA-MCC.
![img-3.jpeg](img-3.jpeg)

Fig. 7. Demonstration of model structures after applying traditional approaches and WI + SM, respectively. Each circle represents a variable and directed edges represent the dependency. (a) Previous approaches. (b) WI + SM.
same parameters. Therefore, the computational complexity analysis of EDA-MCC in Table II still holds.

## D. Difference Between EDA-MCC and EDAs with Model Complexity Penalization

Several other approaches for controlling/penalizing the model complexity in EDAs have also been proposed. For instance, EGNA $_{E E}$ [2] uses the edge exclusion test to control the structure complexity of a Gaussian network, or uses the BGe (Bayesian Gaussian equivalence) metric and local search to

TABLE II
COMPARISON OF ONE-GENERATION COMPUTATIONAL COMPLEXITY


learn the structure. Normal IDEA [28] uses the BIC (Bayesian Information Criterion) metric to penalize the complexity of a normal pdf factorization. Real-coded Bayesian Optimization Algorithm (rBOA) [30]-[32] also employs Bayesian factorization with BIC metric and greedy search, but in contrast to EGNA and normal IDEA, it fits Gaussian mixture model instead of a single Gaussian. There are significant differences between EDA-MCC and these approaches.

1) Fig. 7 shows typical model structures after applying previous approaches' model estimation and WI + SM. Compared with WI + SM, previous approaches can be seen as implicitly controlling the model complexity. Therefore, model estimation in these approaches often leads to a large connected graph, although some dependencies between variables are removed. This means that the variables are still modeled by a big multivariate model. ${ }^{3}$ In contrast, WI + SM explicitly partitions the variables into several separated groups with a size limit (parameter $c$ ). Then a number of small models are applied to $\mathcal{W}$ and subsets of $\mathcal{S}$. The failure of a big model on large problems can be seen from the fact that few results of previous algorithms on problems having hundreds of variables are reported. A possible explanation is that it is due to the curse of dimensionality and the computational complexity issues. As $n$ grows, a big model's performance quickly deteriorates and its computational cost also rapidly increases.
2) Previous approaches are mostly trying to precisely learn a complex global structure from data, which is in fact impractical in high-dimensional space. They also involve complicated computation that makes the computational complexity of EDAs become even higher. On the other hand, if WI + SM is used, the global structure is just roughly learned. Since it is too hard to perform good global learning in high-dimensional space, WI + SM tries to perform good learning in divided subspaces to give a better approximated global estimation. Fortunately, the controlling parameters $\theta$ and $c$ both have explicit physical implications that can be interpreted and set easily (Section V will give more discussions on these parameters and empirical guidelines of setting them). WI and SM do not introduce additional timeconsuming computation into EDA. They can even help reduce the overall computational complexity. But we can also imagine that if the global structure can be
[^0]successfully learned under some conditions, WI + SM will not outperform traditional approaches.
3) Compared with previous approaches, WI + SM is more flexible in terms of introducing different search strategies into EDAs. For example, probabilistic models other than Gaussian can also be applied to $\mathcal{W}$ and $\mathcal{S}$. Applying different models on different subsets of $\mathcal{S}$ for diversity consideration is also feasible. This allows the easy development of new EDAs and hybrid algorithms. But in this paper we only discuss Gaussian models.

## IV. EXPERIMENTAL STUDIES

## A. Experimental Setup

1) Involved Algorithms: Four algorithms are involved in experimental comparisons: UMDA ${ }_{c}^{G}$ [2], EMNA $_{\text {global }}$ [2], EEDA [8], and EDA-MCC. As extensions of the analyses on computational complexity, we select UMDA ${ }_{c}^{G}$ as a representative of univariate Gaussian EDAs, and EMNA ${ }_{\text {global }}$ as a representative of multivariate Gaussian EDAs. Both algorithms are based on MLE. Since many theoretical studies, experimental comparisons and real-world applications of these two EDAs have been made [2], [7], [8], [11], [15]-[19], [29], [34], [35], [41]-[43], [45], [46], [48]-[51], comparing them makes sense. EEDA is included as a representative of multivariate Gaussian EDAs using covariance matrix scaling. It can be seen as an extension of EMNA $_{\text {global }}$, making it easy to implement based on EMNA $_{\text {global }}$. In EDA-MCC, we apply a UMDA ${ }_{c}^{G}$ model for variables in $\mathcal{W}$, and an EEDA model for each subset of $\mathcal{S}$. Such an implementation can yield fair comparisons with UMDA ${ }_{c}^{G}$, EMNA $_{\text {global }}$, and EEDA. To fairly compare CPU time cost, all algorithms are implemented with $\mathrm{C}++$ using a same template design and they share the same basic data structures and numerical computation library. They only differ on model estimation and solution sampling modules.
2) Test Functions: Test functions are listed in Table III. They are selected from classical benchmarks in [7], [52] and CEC2005 special session [53]. All 13 functions are minimization problems. For details of the CEC2005 functions, including the shifted global optima and the transformation matrices, etc., please refer to [53]. These functions contain several comparison pairs, from which we can see whether an algorithm is sensitive to the shifted or rotated function landscape. The 13 functions can also be classified into three groups:
3) separable unimodal problems: $F_{1}$ and $F_{2}$;
4) nonseparable problems with only a few ( $\leq 2$ ) local optima: $F_{3}-F_{10}$;
5) multimodal problems with many local optima: $F_{11}-F_{13}$.
6) Common Parameter Settings: For traditional EDAs such as UMDA ${ }_{c}^{G}$, EMNA $_{\text {global }}$, and EEDA, besides $\tau$ representing


[^0]:    ${ }^{3}$ In rBOA, the global pdf is factorized as a product of linear combinations of subproblems, which are still essentially fragments of a Gaussian network, and thus can be interconnected via overlapping variables. Even if they are the maximal compound subproblems [31] that are totally separated from each other, there is no explicit control on the size of a subproblem. It may also result in big multivariate subproblems.

TABLE III
TEST FUNCTIONS USED IN EXPERIMENTS

* Note that the transformation matrix $\boldsymbol{M}$ in $F_{9}$ and $F_{12}$ is not the population size $M$.

The domains of function $F_{7}$ and $F_{11}$ are changed from original definitions in [52] to make them consistent with the domains of $F_{8}$ and $F_{12}$, respectively. $F_{4}$ and $F_{6}$ are shifted version of $F_{3}$ and $F_{5}$, respectively. The shifted global optima are generated following the same way of [53].
the selection pressure, the only parameter is the population size $M$. Given a fixed maximal number of fitness evaluations (max. \#eval) as in many real-world applications, a larger $M$ may offer better learning, but also reduces the maximal number of generations in the meantime, and vice versa for smaller $M$. People are aware of the tradeoff between population size and number of generations, and understand that the balance between the two factors, which may even vary from problem to problem, has significant influence on the performance of EDAs. As in most (if not all) studies on EDAs, our investigation does not emphasize the setting of population size. Instead, for each EDA, we always apply four settings of population size, $M \in\{200,500,1000,2000\}$, aimed at releasing promising performance of the algorithms as much as possible on every problem. In experiments, for each algorithm, given a problem with a specific problem size $n$, we compare the average best solutions obtained among the four population sizes, and choose the best result. The population size leads to the best result is also recorded for comparison. All algorithms use $\tau=0.5$ in all tests (thus $m=M / 2$ ). The initial populations are always generated uniformly within the search space. Elitist approach is adopted for all algorithms, i.e., only one best individual is survived into the next generation, together with $(M-1)$ newly sampled individuals they constitute a new generation. All these settings are widely used when studying these EDAs in previous publications. For each problem, we test problem sizes $n \in\{50,100\}$. The max. \#eval is set according to [53], i.e., max. \#eval $=10000 \times n$. Algorithms are terminated only when their \#eval exceed this limit. The results are averaged over 25 independent runs. All experiments are done on a P4 2.40 GHz computer with 512 MB RAM.
4) Parameters of EDA-MCC: Through all experiments of EDA-MCC, we set $m_{\text {corr }}=100, \theta=0.3$ for WI. We regard $m_{\text {corr }}=100$ points as enough to calculate the correlation coefficients between any pair of variables (a pair of variables
implies a 2-D space). We set $\theta=0.3$ here because it is a popular threshold to define weakly correlated in the context of statistics. In our experience, we have also observed that WI can be sensitive to the value of $\theta$. For example, a small value of $\theta=0.15$ may result in an empty $\mathcal{W}$, i.e., all of the variables are regarded as strongly correlated with each other, which makes WI a null operation. Large $\theta=0.6$ may lead to $\mathcal{W}=\mathcal{V}$, i.e., EDA-MCC degrades itself into a UMDA ${ }^{G}$ and discards all the dependencies among variables. To release the power of EDA-MCC most, there must be an optimal $\theta$ given a problem and other parameters. Different problems and other parameters may also lead to different optimal value of $\theta$. As mentioned above, $\theta$ can reflect the user's confidence on univariate model. To have reasonable analysis on the effects of WI, we set a constant and moderate value of $\theta=0.3$ for all tests. Here our aim is to demonstrate that EDA can benefit from WI, whereas which value of $\theta$ benefits EDA most on a specific problem can be an independent issue. For SM, we set $c=20$. In practice, the settings of $c$ can be determined by $m$ according to user's preference and experience. In normal cases, if a larger $m$ can be applied, $c$ can also be set larger, and vice versa. When $m$ is large enough to give a reliable estimation on the entire $n$-dimensional space, we can set $c=n$, which implies that we fully trust the global estimation rather than approximating it by combination of subspace models. But meanwhile, we should also afford the computational complexity. On the other hand, a smaller $c$ can significantly reduce the computational complexity. Users can weigh the pros and cons and then set c. Parameters $m_{\text {corr }}, \theta$, and $c$ all have explicit physical implications. Their values are either bounded or can be determined with the guidance of other predetermined parameters or user's preference. It should be straightforward to set these parameters when applying EDA-MCC to a new problem. In Section V, the influence of different $\theta$ and $c$ will be investigated. Empirical guidelines of setting EDA-MCC parameters will also be given.

TABLE IV
Solution Quality Comparison


* The value of Asymp. Sig. (two-tailed) $<0.05$ when compared with the results of EDA-MCC.
${ }^{\dagger}$ The value of Asymp. Sig. (two-tailed) $<0.001$ when compared with the results of EDA-MCC.
$\ddagger$ The value of Asymp. Sig. (two-tailed) $<0.001$ when compared with the results of EDA-MCC.
The results are divided into three groups according to the problem properties. The means and standard deviations of $F(\bar{x})-F(\bar{x} *)$ for 25 runs are reported. If the value is below $1 \mathrm{e}-12$, we regard it as zero. The best result (with the minimal mean value) is bolded in each row. Results of EDA-MCC are compared with others algorithms' by nonparametric Mann-Whitney $U$ test. The significance level is shown by markers ( ${ }^{*},{ }^{\dagger}$, and $\S$ ). No marker implies no significant difference.
![img-4.jpeg](img-4.jpeg)

Fig. 8. Comparison of average CPU time on $F_{2}, F_{8}$, and $F_{11}$. (a) $F_{2}$ : shifted sphere. (b) $F_{8}$ : shifted Rosenbrock. (c) $F_{11}$ : Rastrigin.

## B. Experimental Results

We record the difference between the best fitness that an algorithm can find and the known global optimum, i.e., $F(\bar{x})-F(\bar{x} *)$. The value is always non-negative for minimization problems. The smaller it is, the better an algorithm performs. The means and standard deviations of $F(\bar{x})-F(\bar{x} *)$ for each algorithm in each test are summarized in Table IV. If $F(\bar{x})-F(\bar{x} *)<1 \mathrm{e}-12$, then we regard it as zero, i.e., the global optimum is reached. If multiple results among the four-population-size tests reach the optimum, we report the one exhibiting the fastest convergence. Table V shows the corresponding population sizes of the algorithms. Because the

CPU time comparisons on different problems are similar, we only show the CPU time comparisons on selected functions $F_{2}, F_{8}$ and $F_{11}$ in Fig. 8.

## C. Discussion and Analysis

1) Separable Unimodal Problems: The separable and unimodal structures of $F_{1}$ and $F_{2}$ can facilitate univariate model-based EDAs in solving the problems although this is not always the case. Our experiments show that, in our case, UMDA ${ }^{\mathrm{G}}$ and EDA-MCC perform well. However, EMNA ${ }_{\text {global }}$, which relies on global multivariate estimation, exhibits significant performance degradation as $n$ grows. EEDA also performs

TABLE V
POPULATION SIZE COMPARISON


Population sizes used by the algorithms to generate the results in Table IV are shown. On each problem, the smallest population size is marked in bold.
well due to its better explorative ability than EMNA global, but not as good as UMDA ${ }_{c}^{G}$ and EDA-MCC on 100-D $F_{2}$. Overall, EDA-MCC performs the best among all the multivariate EDAs with statistical significance, and it performs as well as UMDA ${ }_{c}^{G}$. Also note that EMNA global and EEDA can perform worse when the optimum is shifted away (in $F_{2}$ ) from the center of search space (in $F_{1}$ ).

Although the CPU time of an algorithm may depend on population sizes and thus different number of generations, it reflects the computational time needed to exert an algorithm's best performance. We can find that UMDA ${ }_{c}^{G}$ costs the least CPU time whereas EMNA global and EEDA cost the most. EDA-MCC's CPU time grows faster than UMDA ${ }_{c}^{G}$ but slower than EMNA global and EEDA. Since $F_{1}$ and $F_{2}$ are easy for UMDA ${ }_{c}^{G}$ model, the required population size indeed grows mildly. However, the population sizes of EMNA global and EEDA keep at high levels. EDA-MCC's requirement of large population size is significantly relaxed due to WI + SM. Meanwhile, EDA-MCC shows significantly better performance.
2) Nonseparable Problems with Only A Few Local Optima: This group of functions are either unimodal or only have two local optima, which implies the problems have clear inner structures. The nonseparable properties pose significant difficulties for UMDA ${ }_{c}^{G}$. We can see that UMDA ${ }_{c}^{G}$ fails to perform the best on any test. On the other hand, EDA-MCC performs the best on all tests except 50-D $F_{10}$. EMNA global performs the worst and EEDA performs generally between UMDA ${ }_{c}^{G}$ and

TABLE VI
COMPARISON BETWEEN EEDA AND EDA-MCC ON 50-D-200-D $F_{10}$


Population sizes used are shown in brackets. In each row, the significantly better result (determined by nonparametric Mann-Whitney $U$ test) is shown in bold. For all results of EEDA, the value of asymp. sig. (two-tailed) $<$ 0.001 when compared with the results of EDA-MCC.
![img-5.jpeg](img-5.jpeg)

Fig. 9. Average CPU time of EEDA and EDA-MCC on $F_{10}$.

EDA-MCC. Note that $F_{4}, F_{6}$, and $F_{8}$ are shifted versions of $F_{3}, F_{5}$, and $F_{7}$, respectively. On the unshifted versions, although UMDA ${ }_{c}^{G}$ and EEDA perform significantly worse than EDA-MCC, the solutions they found are not too bad. However, once the global optima are shifted away, their performance become much worse. EMNA global has a similar issue and it always performs the worst. Among all, only EDA-MCC shows robust performance to the shifts of the global optima.

The CPU time costs are similar to that of previous group of functions. EDA-MCC's CPU time grows much slower than EMNA global and EEDA. Although UMDA ${ }_{c}^{G}$ costs the least CPU time, it always performs worse than EDA-MCC. EDA-MCC also needs the smallest population sizes in most cases, except on 50-D $F_{8}$. As we can see on $F_{12}$ in the next group that, the best population size of EDA-MCC and EEDA can sometimes fluctuate as $n$ grows. This can be explained as that since they have better explorative ability, they can benefit from either a) large population sizes, or b) large budget of number of generations (by applying a small population size). However, for UMDA ${ }_{c}^{G}$ and EMNA global that fully relies on MLE, the population sizes usually keep increasing as $n$ grows.

In this group, $F_{7}-F_{10}$ are relatively hard problems that no algorithm achieves satisfying solutions. But to the best of our knowledge as well as we can see in the following 500-D tests that no known algorithm can find good solutions on these problems, and EDA-MCC is in fact the best so far in general. Among these problems, $F_{10}$ 's global optimum is on the bounds of the domain, which requires explorative ability the most among all 13 problems. On 50-D $F_{10}$, EEDA performs the best since it has a global guidance of the gradient and a relatively good estimation can be obtained. On the other hand, because EDA-MCC partitions the search space, search along the approximated global gradient is not

so effective as EEDA. But as the problem size grows to 100D, EDA-MCC significantly outperforms EEDA. This confirms the effectiveness of using subspace models to approximate the global estimation. In higher dimensional space where a precise global estimation is hard to obtain, approximating the global estimation by combination of subspace models can achieve better performance for EDA. To further verify the effectiveness of the combination of subspace models, we extend our experiments on $F_{10}$ to 150-D and 200-D to compare EEDA and EDA-MCC. Experimental settings are the same as previous ones. The comparison is shown in Table VI and Fig. 9. We can see that if $n$ grows even larger, combination of subspace models can be significantly better than a poor global model. EDA-MCC not only finds significantly better solutions, but also scales to larger problems better, i.e., with a much slower increase in CPU time cost.

On this group of functions, UMDA ${ }_{c}^{G}$ cannot perform as well as EDA-MCC, but its computational cost is always much lower. One may wonder whether a bigger CPU time budget for UMDA ${ }_{c}^{G}$ would lead to superior performances over EDAMCC. In Fig. 10 we plot the averaged evolutionary curves of 25 runs for all algorithms in 100-D tests to give an answer. We can see that the evolutionary curves of UMDA ${ }_{c}^{G}$ all quickly become flat as the algorithm proceeds. This implies the fact that even given more CPU time, UMDA ${ }_{c}^{G}$ cannot find better solution but converges to a suboptimal one.

Another possible reason why UMDA ${ }_{c}^{G}$ does not perform well is that the population sizes applied are still not large enough. Therefore, we further test even larger population sizes $M \in$ $\{4000,8000,16000\}$ (and still $m=M / 2$ ) for UMDA ${ }_{c}^{G}$ on 100D functions in this group. Results on representative functions are summarized in Table VII. We can see that larger population sizes do not help UMDA ${ }_{c}^{G}$ obtain better results. To be specific, only on $F_{8}$ the result using $M=4000$ becomes a little better, but still much worse than EDA-MCC. On other functions, large population sizes perform even worse. This implies that the failure of UMDA ${ }_{c}^{G}$ on these functions is primarily due to its model simplicity, either larger population sizes or longer CPU time budget may not lead to better performance.

In a word, on this group of nonseparable functions, EDAMCC performs significantly the best. UMDA ${ }_{c}^{G}$ fails on all problems because of its model simplicity. EMNA ${ }_{\text {global }}$ and EEDA cannot perform well in high-dimensional tests.
3) Multimodal Problems with Many Local Optima: These functions all have a huge number of local optima, which results in highly complicated function landscape and makes the problems hard to solve. Using the same sample size, the estimated multivariate model cannot be as reliable as on the previous group of problems. The results coincide with this intuition. Although $F_{11}$ is separable, results show that it is not easy to solve for multivariate Gaussian EDAs. A previous study [11] has shown that if a small population size is applied, EMNA ${ }_{\text {global }}$ and EEDA cannot perform well on this problem, and EEDA may even perform worse than EMNA ${ }_{\text {global }}$. The huge number of local optima can mislead the multivariate search and the covariance matrix scaling. UMDA ${ }_{c}^{G}$ performs the best and EMNA ${ }_{\text {global }}$ the second on this function. Both EEDA and EDA-MCC adopting covariance
matrix scaling fail to reach the optimum. Applying a rotation to $F_{11}$ makes $F_{12}$ nonseparable. Even the global optimum of $F_{12}$ is shifted, compared with the results on $F_{11}$ (see Table IV), surprisingly UMDA ${ }_{c}^{G}$ still outperforms the others, whereas EMNA global becomes much worse. EEDA and EDAMCC approximately hold the solution quality. Intuitively, nonseparable problem is hard for UMDA ${ }_{c}^{G}$. However, the results reveal that high-dimensional $F_{12}$ is even much harder for multivariate Gaussian model. On expanded multimodal function $F_{13}, \mathrm{UMDA}_{c}^{G}$ again performs the best. It seems that the complicated problem structure of this group of functions poses similar difficulties to EDA-MCC, and simple algorithms such as UMDA ${ }_{c}^{G}$ can be good enough on these problems. CPU time comparisons on these problems are similar to previous ones that EDA-MCC's CPU time is always between UMDA ${ }_{c}^{G}$ and EMNA ${ }_{\text {global }}$. Since EDA-MCC based on WI + SM cannot perform well, its required population size also becomes large.
4) The Failure of EDA-MCC and the Success of UMDA ${ }_{c}^{G}$ on $F_{11}-F_{13}$ : To further analyze the failure of EDA-MCC and the success of UMDA ${ }_{c}^{G}$ on $F_{11}-F_{13}$ (three problems sharing the common property of having a huge number of local optima), additional experiments are presented here. Generally speaking, the experiments concern two characteristics of EDAs that may be closely related to the performance on these problems. Our goal is to find the intrinsic reasons that prevent EDA-MCC from performing well.

The first characteristic we take into account is the model complexity of EDA. On a specific problem, a multivariate Gaussian EDA does not necessarily outperform a univariate Gaussian EDA. The failures of several multivariate Gaussian EDAs and the success of univariate Gaussian EDA (UMDA ${ }_{c}^{G}$ ) on $F_{11}, F_{12}$, and $F_{13}$ probably imply that using high dependency degree (i.e., high model complexity) for these problems is no longer effective. If such an intuition can be validated, then the failures of EDA-MCC are very likely to attribute to the failures of high dependency degree, not the novel WI + SM techniques adopted by EDA-MCC. Therefore, we test explicitly controlling the dependency degree by changing $c$, i.e., from original settings $c=20$ to $c=2$. Note that if $c=1$, EDA-MCC will perform exactly the same as UMDA ${ }_{c}^{G}$, and $c=2$ restricts the multivariate dependencies to the minimal degree that at most dependencies of two variables are considered. We also add 10-D tests to see what happens in low dimension. Note that for 10-D tests, $c=20$ is essentially identical to $c=10$ since all variables can be included.

Another characteristic that may influence the performance of an EDA is the base multivariate model, which also indicates the method of estimating the probabilistic model. UMDA ${ }_{c}^{G}$ adopts MLE, and EMNA global model is more similar to the UMDA ${ }_{c}^{G}$ model than the others because of also using MLE. UMDA ${ }_{c}^{G}$ 's promising performance on the three problems may indicate that MLE is more efficient than covariance matrix scaling on these problems. Therefore, we replace the EEDA model with the EMNA global model in EDA-MCC to test the effect of base model. By crossing over the settings of base multivariate model and $c$, we have four candidates to be compared with UMDA ${ }_{c}^{G}$ : 1) EDA-MCC with EEDA model,

![img-6.jpeg](img-6.jpeg)

Fig. 10. Evolutionary curves on 100-D $F_{5}, F_{5}, F_{8}, F_{9}$, and $F_{10}$. Curves of $F_{4}, F_{6}, F_{7}$ are similar to that of $F_{5}, F_{5}, F_{8}$, respectively, and thus are omitted. (a) $F_{3}$. (b) $F_{5}$. (c) $F_{8}$. (d) $F_{9}$. (e) $F_{10}$.

TABLE VII
RESULTS OF UMDA ${ }_{c}^{G}$ USING LARGE POPULATION SIZES ON 100-D $F_{5}, F_{5}, F_{8}, F_{9}$, AND $F_{10}$

Results of EDA-MCC and UMDA ${ }_{c}^{G}$ using $M=2000$ are also directly included from Table IV. On each problem, the value of asymp. sig. (two-tailed) $<0.001$ when any UMDA ${ }_{c}^{G}$ result is compared with EDA-MCC result using nonparametric Mann-Whitney $U$ test.

TABLE VIII
COMPARISON OF DIFFERENT BASE MULTIVARIATE MODELS AND DIFFERENT SUBSPACE SIZES

* The value of Asymp. Sig. (two-tailed) $<0.05$ when compared with the results of UMDA ${ }_{c}^{G}$.
${ }^{\dagger}$ The value of Asymp. Sig. (two-tailed) $<0.01$ when compared with the results of UMDA ${ }_{c}^{G}$.
$\S$ The value of Asymp. Sig. (two-tailed) $<0.001$ when compared with the results of UMDA ${ }_{c}^{G}$.
The best results for each row are shown in bold. Results of UMDA ${ }_{c}^{G}$ are compared with results of each of the other four implementations of EDA-MCC by nonparametric Mann-Whitney $U$ test. The significance level is shown by markers $\left(^{*},{ }^{\dagger}\right.$, and $\S$ ). No marker implies no significant difference.

$c=20$; 2) EDA-MCC with EEDA model, $c=2$; 3) EDAMCC with EMNA ${ }_{\text {global }}$ model, $c=20$; and 4) EDA-MCC with EMNA $_{\text {global }}$ model, $c=2$. Still, for each implementation, four population sizes are applied in each test. The best result among the four population size tests is reported. The comparisons are summarized in Table VIII.

We can find that in 10-D tests, there is no significant difference among candidate algorithms. EDA-MCC can be as good as UMDA ${ }_{c}^{G}$. In 50-D and 100-D tests, different degrees of multidependencies does not help EDA-MCC achieve as good performance as UMDA ${ }_{c}^{G}$, no matter that the base model is EEDA model or EMNA model. This implies that on these problems, if the computational resources (max. \#eval) are limited, utilizing multidependencies among variables may not be an effective strategy. To be specific, as long as considering the multidependencies, even only with the minimal degree ( $c=2$ ), the search is misled by the complex function landscape. As $n$ grows, this effect becomes more serious. Nevertheless, changing from EEDA model to EMNA ${ }_{\text {global }}$ model does help to find better solutions, although the results are not always as good as UMDA ${ }_{c}^{G}$. It implies that, when $n$ is large, the "radical" covariance matrix scaling can be easily misled by the complex function landscapes. On the other hand, the more "conservative" MLE performs better. Covariance matrix scaling is more effective only when $n$ is small. Of course, discussions here are restricted to our predefined population sizes and the max. \#eval. Since EDA-MCC can perform as good as UMDA ${ }_{c}^{G}$ on low-dimensional 10-D tests, we guess that with extremely large population size and sufficiently large budget of max. \#eval, EDA-MCC has the potential to come up with or even outperform UMDA ${ }_{c}^{G}$. But considering the fast increasing number of local optima and the fast increasing complexity of the function landscape as $n$ grows, EDA-MCC's requirement of population size and \#eval to outperform UMDA ${ }_{c}^{G}$ will also increase tremendously. This can also be explained by the effect of the curse of dimensionality. Therefore, when facing problems with many local optima, it may be computationally too expensive to apply a multivariate search and expect good performance. In this case, a cheap and simple univariate algorithm such as UMDA ${ }_{c}^{G}$ can be a better choice given limited computational resources.

## D. Summary So Far

It is discovered by the above experiments that compared with traditional EDAs, EDA-MCC shows remarkable effectiveness and efficiency on high-dimensional nonseparable problems with only a few local optima. On simple separable problems, EDA-MCC is comparable with UMDA ${ }_{c}^{G}$. But on problems with too many local optima, it does not work as well as simple UMDA ${ }_{c}^{G}$. In any case, EDA-MCC offers a partial solution to the three requirements raised at the beginning of Section III.

1) The multivariate Gaussian-based search is preserved in EDA-MCC, which leads to promising performance on large-scale nonseparable problems.
2) Computational cost of EDA-MCC is usually lower than traditional multivariate Gaussian EDAs; its CPU time cost also grows much slower as problem size grows.
3) EDA-MCC can work with small population sizes for large-scale optimizations.
Conditions under which EDA-MCC may succeed or fail can also be summarized.
4) In low-dimensional search space with sufficient data, where the global estimation is sufficiently precise, EDAMCC may not be better than traditional EDAs.
5) In high-dimensional search space with sparse data only, where the global estimation is far from precise, EDAMCC can be more effective. However, if the function landscape has a huge number of local optima as in $F_{11}-F_{13}$, EDA-MCC as well as traditional multivariate Gaussian EDAs will fail. In this case, simple univariate Gaussian EDAs can be more effective and efficient.
6) The success of EDA-MCC does not mean that it can escape from the curse of dimensionality. EDA-MCC just suffers less from it by explicitly controlling the model complexity. If using a fixed finite population size, EDA-MCC and any other EDAs relying on learning will inevitably fail in extremely high-dimensional search space.
We also note that although EDA-MCC can have better performance than traditional EDAs, in some cases (e.g., on problems $F_{9}$ and $F_{10}$ ), none of the candidates perform well enough to find a high quality solution. More effective and efficient search strategies for large-scale optimization are still to be developed.

## E. Experimental Results on 500-D Functions

Now, we further enlarge the problem size of $F_{1}-F_{13}$ to 500-D, and compare EDA-MCC with traditional EDAs and several optimization algorithms specifically designed for large-scale optimization. The involved traditional EDAs include UMDA ${ }_{c}^{G}$ and $\operatorname{MIMIC}_{c}^{G}$ [2]. MIMIC ${ }_{c}^{G}$ is also a Gaussian EDA, whose model complexity is between UMDA ${ }_{c}^{G}$ and those multivariate Gaussian EDAs. The variable dependency in MIMIC ${ }_{c}^{G}$ is a chain-shaped structure with bivariate conditional Gaussian densities. Multivariate Gaussian EDAs such as EMNA ${ }_{\text {global }}$, EEDA, and EGNA, are not included because their CPU time on any of the 500-D functions is too long to be acceptable.

Recently, Yang et al. [54] proposed a cooperative coevolution framework for large-scale optimization, and an algorithm named DECC-G, which uses differential evolution (DE) as the base algorithm in the framework, was proposed. DECCG also adopts variable partitioning strategy, but within the cooperative coevolution framework, when DECC-G is activating the variables of one group, all the other variables are fixed. The evaluation of currently activated variables are calculated in the context of fixing other variables. In EDAMCC, though variables are also grouped into several subsets, their optimizations are simultaneous and synchronized. EDAMCC is not an instance of cooperative coevolution. In [54], DECC-G has been compared with three other algorithms, SaNSDE, FEPCC, and DECC-O, on several 500-D and 1000D functions, and it shows outstanding performance compared

TABLE IX
CompAriSONS of 500-D TESTS

$\S$ The value of Asymp. Sig. (two-tailed) $<0.001$ when compared with the results of EDA-MCC.
For each problem, the best result is bolded. Since results of SaNSDE, FEPCC, DECC-O, and DECC-G in [54] only contain mean performance, we are not able to give standard deviations. Results of EDA-MCC are compared with results of UMDA ${ }_{c}^{G}$, MIMIC ${ }_{c}^{G}$, and sep-CMA-ES, respectively, by nonparametric Mann-Whitney $U$ test. The significance level is indicated by marker $\S$. Some results of FEPCC are not reported in [54], and are thus left blank. Two-tailed Friedman test shows that all algorithms (except FEPCC whose data is not available) are not equivalent at the significance level of 0.05 . Post-hoc Nemenyi tests demonstrate that EDA-MCC outperforms SaNSDE, DECC-O, and MIMIC ${ }_{c}^{G}$ at the significance level of 0.05 [55]. Moreover, according to one-tailed Wilcoxon signed ranks tests, EDA-MCC outperforms UMDA ${ }_{c}^{G}$ at the significance level of 0.15 . At the same significance level, EDA-MCC does not significantly outperform DECC-G and sep-CMA-ES.
with other algorithms. Here, we compare EDA-MCC with the results reported in [54]. ${ }^{4}$

Another algorithm, sep-CMA-ES, recently proposed by Ros and Hansen [56], is also included in the comparison. Because the original CMA-ES is incapable of handling problems with more than several hundred dimensions [57], sep-CMAES was developed only using a diagonal covariance matrix in a Gaussian model while keeping the original covariance matrix adaptation. Several recent studies (e.g., [56] and [57]) investigated its performance on problems larger than 500-D. Although sep-CMA-ES uses a diagonal covariance matrix as well as UMDA ${ }_{c}^{G}$, their model estimations are far different. One major difference is that sep-CMA-ES relies on cumulation of the information gathered in the evolution path to model the covariance matrix, which is mainly heuristic-based, and thus only requires a very small population size. In contrast, a typical EDA, such as UMDA ${ }_{c}^{G}$, estimates the covariance matrix only by samples in current generation with MLE, which is learningbased; thus, it usually requires a much larger population size than sep-CMA-ES does. As will be seen later in experiments, this could lead to significantly different performance. We use recommended parameters of sep-CMA-ES [56] to conduct the comparison, with population size $\lambda=4+\lfloor 3 \ln (n)\rfloor$ (i.e., 22 when $n=500$ ), selected size $\mu=\left\lfloor\frac{\lambda}{2}\right\rfloor$, initial standard deviation (step size $\sigma$ ) identical to one third of the search interval, and initial search point the center of the search space. The implementation of sep-CMA-ES is derived from a C version of CMA-ES. ${ }^{5}$

Following [54], we set the max. \#eval to $2.5 \mathrm{e}+06$. The population size of DECC-G is 100 and its subcomponent dimension is 100 for all tests. For the parameters of SaNSDE, FEPCC, and DECC-O please refer to [54]. For UMDA ${ }_{c}^{G}$ and MIMIC ${ }_{c}^{G}$,

[^0]population size $M=2000$ and selected size $m=1000$ are adopted. In EDA-MCC, still we use UMDA ${ }_{c}^{G}$ model for $\mathcal{W}$ and EEDA model for subsets of $\mathcal{S}$. We set population size $M=200$, selected size $m=100, m_{\text {corr }}=100, \theta=0.3$, and $c=100$ for all tests. If $M=200$ is too small for solving a problem, we consequently test $M=500$ and $M=1000$ to see whether better performance can be obtained while keeping the selection pressure. We highly trust the small population sizes that for $c=100$ dimensional subspace, we still have confidence in the subspace models. The result is that EDA-MCC needs $M=1000$ on $F_{3}, F_{4}$, and $F_{10}$, and only $M=200$ on all other functions. Other experimental settings are the same as previous ones. Detailed comparisons are summarized in Table IX.

On the simplest separable $F_{1}$ and $F_{2}$, EDA-MCC, UMDA ${ }_{c}^{G}$, DECC-O, DECC-G, and sep-CMA-ES perform very well. On the second group of nonseparable functions $F_{3}-F_{10}$, EDAMCC and sep-CMA-ES show the most stable good performance. Interestingly, although sep-CMA-ES only adopts diagonal covariance matrix, it performs generally well on these nonseparable functions, which was also reported in [57]. But only on two Ronsenbrock functions ( $F_{7}$ and $F_{8}$ ) it significantly outperforms EDA-MCC, whereas EDA-MCC significantly outperforms sep-CMA-ES on $F_{3}, F_{4}$, and $F_{10}$. Both EDA-MCC and sep-CMA-ES reach the global optimum on $F_{5}$ and $F_{6}$. On $F_{9}$, although sep-CMA-ES has a little better average performance, there is no significant difference with EDA-MCC's. If we compare DECC-G with EDA-MCC, only on $F_{3}$ and $F_{7}$, DECC-G performs better than EDAMCC. But DECC-G is rather sensitive to the shifted global optimum. On the shifted functions $F_{4}$ and $F_{8}$, EDA-MCC performs well holding almost the same performance, whereas DECC-G becomes much worse. Similar situations happen on $F_{11}$ and its shifted rotated version $F_{12}$. EDA-MCC is not sensitive to the shifted and rotated function landscape as DECC-G is.


[^0]:    ${ }^{4}$ Results on $F_{4}-F_{9}$ are not available in [54]. These results are obtained by running the source code provided by the authors of [54].
    ${ }^{5} \mathrm{http}: / / \mathrm{www} . \mathrm{ki} . \mathrm{hr}^{\mathrm{**}}$ hansen/cmaes_c.tar.

TABLE X
Performance COMPARISONS OF DiffERENT $\theta$ AND $c$ ON 100-D $F_{2}$. RESULTS ARE AVERAGED OVER 25 RUNS

TABLE XI
Performance COMPARISONS of DiffErent $\theta$ AND $c$ ON 100-D $F_{8}$. RESULTS are AVERAGED OVER 25 RUNS

For the last group of functions $\left(F_{11}-F_{13}\right)$, having a huge number of local optima, as analyzed above, UMDA ${ }_{c}^{G}$ shows clear advantage in general. On $F_{13}$, DECCO and UMDA ${ }_{c}^{G}$ performs much better than the others. This is consistent with previous observations. Because DECC-O optimizes the function of one variable at a time within the cooperative coevolution framework, its behaviors are similar to some extent, to UMDA ${ }_{c}^{G}$. Therefore, they should be more effective on these problems. The exception that DECC-O fails on $F_{12}$ can be explained by its sensitiveness to the shifted global optimum. As for sep-CMA-ES, although it also uses univariate model, its performance on $F_{11}-F_{13}$ is far worse than UMDA ${ }_{c}^{G}$. This seems to be due to the heuristics by which the covariance matrix is estimated in sep-CMA-ES. The results show that the standard "conservative" MLE adopted in UMDA ${ }_{c}^{G}$ can be more effective than the heuristics adopted in sep-CMA-ES on large-scale problems with many local optima.

We also find that MIMIC ${ }_{c}^{G}$ fails to perform the best on any problem. Due to more suffering from the curse of dimensionality, it is neither as effective as UMDA ${ }_{c}^{G}$ on problems that simple univariate model can already handle, nor as good as EDA-MCC on nonseparable problems with clear structure. The results again validate our analysis on the difficulties of traditional EDAs in high-dimensional search spaces.

Generally speaking, EDA-MCC, with a relatively small population size, shows robust performance on these 500-D problems, especially on nonseparable problems with only a few local optima. It performs statistically better than SaNSDE, DECC-O, UMDA ${ }_{c}^{G}$, and MIMIC ${ }_{c}^{G}$. Although DECC-G also performs generally well, its sensitiveness to shifted global optimum is evidently a disadvantage. Sep-CMA-ES also performs generally well, notably on nonseparable problems $\left(F_{5}-F_{8}\right)$, which is interesting considering the univariate nature of the Gaussian model. This could be a topic worthy of study in future work. In a word, we can say that EDA-MCC is the first successful application of multivariate EDA on a general class (13 in total) of 500-D problems since continuous EDAs have been proposed. Moreover, compared with other EAs, EDA-MCC and UMDA ${ }_{c}^{G}$ show their significant superiority on

8 out of the 13 functions, implying the advantages of using probabilistic models and statistical learning for optimization. Also note that we did not tune the parameters of EDA-MCC further on specific problems. Its potential performance can be even better on real-world large-scale problems.

## V. INFLUENCE OF PARAMETERS $\theta$ AND $c$

In this section, the dependence of EDA-MCC on the newly introduced parameters $\theta$ and $c$ are investigated. Guidelines of setting these parameters are also given.

## A. Influence Tests

A separable function $F_{2}$ and a nonseparable function $F_{8}$ are selected from the 13 test functions (Table III) as demonstration. Different combinations of $\theta$ and $c$ are tested on the two functions with problem size $n=100$, where $\theta \in$ $\{0.2,0.25,0.3,0.35,0.4\}$ and $c \in\{5,10,20,30,40,50\}$. The population size and selected size are adopted from previous experiments of EDA-MCC and kept fixed, i.e., $M=1000, m=$ 500 for $F_{2}$, and $M=500, m=250$ for $F_{8}$. The performance comparison of combinations of $\theta$ and $c$ are summarized in Tables X and XI.

From the results we can see that on separable $F_{2}$, as long as $\theta \leq 0.3$, different $c$ does not change the performance. But when $\theta>0.3$, the performance becomes a little unstable. Note that because current implementation of EDA-MCC uses EEDA model on subsets of $\mathcal{S}$, even when adopting a large $\theta$, as long as $\mathcal{S}$ is not empty, EDA-MCC performs differently from UMDA ${ }_{c}^{G}$. When variable dependencies are overly eliminated by large $\theta$, according to the definition of covariance matrix scaling, the performance can become unstable since the gradient is likely to be poorly approximated. But generally speaking, on separable problems different $\theta$ and $c$ do not have much impact on EDA-MCC's performance.

On nonseparable $F_{8}$, only when $\theta \leq 0.3$, different $c$ does not much change the best performance thus far, except when combining with a very small $c$. Large $\theta(>0.3)$ can make $\mathcal{S}$ easily become empty, which is hazardous to solving nonseparable problems. Large $c$ is not harmful for solving

![img-7.jpeg](img-7.jpeg)

Fig. 11. Scalability results of EDA-MCC on $F_{1}$ and $F_{5}$. (a) \#eval on $F_{1}$. (b) CPU time on $F_{1}$. (c) \#eval on $F_{5}$. (d) CPU time on $F_{5}$.
nonseparable problems, although it may cost longer CPU time as analyzed before. However, too small $c$ has similar effect of large $\theta$ that the dependencies between variables are overly eliminated. Since the partition of $\mathcal{S}$ is random, considering the nonseparability, it further makes covariance matrix scaling fail together with a small $\theta$. We can conclude that too large $\theta$ is hazardous for nonseparable problems. Also, a too small $c$ is not recommended either because it has similar effect to a large $\theta$.

Generally, setting $\theta$ around 0.3 is good for these problems. With such a $\theta$, the value of $c$ does not impact overall performance much when population size is sufficiently large, but may lead to different CPU time cost according to Table II.

## B. Guidelines of Setting $\theta$ and $c$

Intensive experiments in Section IV have suggested that, in most cases, a population size no larger than 2000 (and often, only 200) is sufficient for EDA-MCC to obtain satisfactory results on problems no larger than 500-D. Besides, a constant selection pressure $\tau=0.5$ and a constant $m_{\text {corr }}=100$ also seems enough for dealing with these $50-500-\mathrm{D}$ problems. With such settings, $\theta$ around 0.3 will be good in most cases. For the value of $c$, considering: 1) the CPU time cost is very often necessary to care about in lots of real-world applications, and 2) a too large $c$ close to $n$ (especially when $n$ is very large) also requires a sufficiently large population size to have reliable subspace model estimation and thus increases the computational cost, we suggest to set $c$ a linear fraction of the problem size $n$, e.g., $c=n / 5$. Note that as shown in the above influence tests, when the population size is sufficiently
large, different $c$ impacts little on performance but may result in different CPU time efficiency for problem solving. In the next section, we will demonstrate the scalability of EDA-MCC under these parameter setting guidelines.

## VI. SCALABILITY OF EDA-MCC

In this section, we study the scalability of EDA-MCC in terms of CPU time cost and number of function evaluations (\#eval) needed to reach the global optimum. On different problems, the scalability of EDA-MCC may be different. Here, two test functions, separable $F_{1}$ and nonseparable $F_{5}$, on which EDA-MCC can find the global optimum with acceptable time, are selected for empirical studies on problem sizes $n \in\{100,200,300,400,500\}$. The algorithm terminates only when the global optimum is reached. We also use the four population size settings as in Section IV, and select the result with the least \#eval for plotting. Interestingly, EDA-MCC with population size $M=200$, is always the fastest in reaching the optimum in these tests. And, results with the least \#eval also always cost the least CPU time among the four population size tests. We set $\tau=0.5$, $m_{\text {corr }}=100, \theta=0.3$, and $c=n / 5$ as Section V suggests. All results are averaged over 25 independent runs and obtained on a computer with Intel Core2 2.66 GHz CPU and 3GB RAM. Fig. 11 depicts the \#eval and the CPU time (mean and error bars) needed in solving the two problems.

Under the above parameter settings, we find that the \#eval needed to find the global optimum grows mildly for the two benchmarks. On simple separable $F_{1}$, the growing speed even decreases as $n$ grows. On nonseparable $F_{5}$, it grows approx-

## SM-GC

1) Construct $\mathcal{S}$ according to (4).
2) Partition $\mathcal{S}$ into non-intersected subsets $\mathcal{S}_{1}, \mathcal{S}_{2}, \ldots, \mathcal{S}_{k}, 1 \leq k \leq n$ :
a) $i \leftarrow 1$.
b) Repeat until $\mathcal{S}=\emptyset$.
i) Find two variables $X_{1}, X_{2} \in \mathcal{S}$ maximizing $\left|\operatorname{corr}\left(X_{1}, X_{2}\right)\right|>\theta$. Exit current loop if not found.
ii) Create $\mathcal{S}_{i} \leftarrow\left\{X_{1}, X_{2}\right\}$. $\mathcal{S} \leftarrow \mathcal{S} \backslash \mathcal{S}_{i}$.
iii) Repeat while $\left|\mathcal{S}_{i}\right|<c$, where $c$ defines the maximal size of a subset $(2 \leq c \leq n)$.
A) Find a variable $X \in \mathcal{S}$ maximizing $\left|\operatorname{corr}(X, Y)\right|>\theta$, where $\forall Y \in \mathcal{S}_{i}$. Exit current loop if not found.
B) $\mathcal{S}_{i} \leftarrow \mathcal{S}_{i} \bigcup\{X\}$. $\mathcal{S} \leftarrow \mathcal{S} \backslash\{X\}$.
iv) $i \leftarrow i+1$.
c) If $\mathcal{S} \neq \emptyset$, estimate a univariate model for the rest variables in $\mathcal{S}$.
3) Estimate a multivariate model for each subset based on the $m$ selected individuals.

Fig. 12. Subspace modeling by greedy clustering (SM-GC). Note that the partition step is changed from original SM and minimal value of $c$ is changed to 2 since there is no need to cluster if $c=1$. Parameter $\theta$ here is the same as defined in (3).
imately lineally as $n$. On both problems, the CPU time costs needed also grow mildly, that is, approximately quadratically. The small intervals between the error bars in Fig. 11 also imply the stable performance of EDA-MCC. In a word, EDAMCC shows good scalability on the two problems investigated, at least for problem sizes $\leq 500$-D. Since the experiments in Section IV have demonstrated that EDA-MCC can have better performance and need less CPU time than traditional multivariate Gaussian EDAs on large-scale problems, we can expect EDA-MCC to have better scalability than traditional multivariate Gaussian EDAs in general.

## VII. Subspace Modeling By Clustering Variables

In EDA-MCC, we randomly partition $\mathcal{S}$ into subspaces in SM. One may ask whether a more sophisticated way of partitioning $\mathcal{S}$ can be applied, e.g., partitioning subspaces by clustering the variables in $\mathcal{S}$ based on the strength of the interdependencies. Intuitively, such a method should work well when sample size is large enough compared with the problem size $n$. But as $n$ grows very large (e.g., $n=500$ ) and only a small sample size is available (e.g., population size $M=200$ and selected size $m=100$ ), its performance may not be as good as random partition since any learning method, including unsupervised clustering, will be greatly affected by the curse of dimensionality. In this section, we replace the SM in EDA-MCC with a greedy clustering method named SMGC (Subspace Modeling by Greedy Clustering), and compare
it with original EDA-MCC. The new resulting algorithm is called EDA-MCC-GC.

The details of SM-GC are shown in Fig. 12. SM-GC partitions subspaces in the following steps. First, a pair of variables, whose absolute correlation is the largest among the ones above $\theta$, is picked up from $\mathcal{S}$ as an initial cluster. This implies the pair of variables are the most strongly dependent among all. Then, a variable outside the cluster is selected and added to the cluster, on the condition that its correlation to the existing variables in the cluster is the strongest. The operation iterates until the cluster reaches the maximal size $c$ or no strongly dependent variable can be found from the perspective of the cluster. A cluster refers to a partitioned subspace. Then, the dependencies between the clusters and the rest of the variables in $\mathcal{S}$ are eliminated. An outer loop keeps generating new subspaces in a greedy manner until all variables in $\mathcal{S}$ have been partitioned or when there is no strongly dependent variables left. If after clustering, $\mathcal{S}$ is still nonempty, a univariate model is applied to the rest of the variables since they are now regarded weakly dependent by the algorithm.

We compare EDA-MCC-GC with EDA-MCC on three representative problems: $F_{2}, F_{8}$, and $F_{11}$ with $n \in\{50,100\}$. Population sizes, parameters $\theta$ and $c$ of EDA-MCC-GC, are set the same as used in EDA-MCC in previous 50-D and 500D experiments. Results and parameters used are summarized in Table XII. We can find that on 50-D tests, there is no significant difference between EDA-MCC-GC and EDA-MCC. However, on 500-D tests where a small sample size is applied, EDA-MCC performs significantly better. This verifies our previous discussion that when applied to large-scale problems with a small sample size, partitioning subspaces based on clustering might not be as effective as random partition. Although the illustrative experiments cannot exclude the possibility that some delicate clustering approach might outperform random partition on specific large-scale problems, a clustering approach often requires relatively higher computational cost. In contrast, random partition is simple and efficient, which can be considered a default component of EDA-MCC.

## VIII. Characterization of Problem Properties By EDA-MCC

As our motivation of scaling up EDA, we regard a major advantage of using EDA other than traditional EA is that we can obtain some feedback on the problem properties through observing the probabilistic model learned. We believe that the learned model structure should reflect some underlying properties of the problem. In addition to finding a solution, EDA has its unique capability in this aspect. However, such an advantage of EDA has not been deeply investigated. In a recent paper [58], discrete EDA model has been used to represent interactions between the protein conformations by probability models. But still, rare study has been done on continuous EDA models to characterize the structure of optimization problems.

In EDA-MCC, we can do so by visually analyzing the model structure obtained from WI + SM. When running EDA-MCC in previous experiments, we also record the results of WI

TABLE XII
COMPARISONS BETWEEN EDA-MCC-GC AND EDA-MCC ON 50-D AND 500-D $F_{2}, F_{8}$, AND $F_{11}$


$\S$ The value of Asymp. Sig. (two-tailed) $<0.001$ when compared with the results of EDA-MCC.
For each test, the best result is bolded. Results of EDA-MCC are directly from Tables IV and IX. Results of EDA-MCC are compared with that of EDA-MCC-GC by nonparametric Mann-Whitney $U$ test.
![img-8.jpeg](img-8.jpeg)

Fig. 13. WI results on $F_{1}$ : sphere. The darker the element of $\boldsymbol{Q}$ is, the more times a variable is partitioned into $\mathcal{S}$ at the specific \#eval during the 25 runs. (a) 10-D average \#strong. (b) 30-D average \#strong. (c) 50-D average \#strong. (d) 100-D average \#strong. (e) 10-D $\boldsymbol{Q}$. (f) 30-D $\boldsymbol{Q}$. (g) 50-D $\boldsymbol{Q}$. (h) 100-D $\boldsymbol{Q}$.
![img-9.jpeg](img-9.jpeg)

Fig. 14. WI results on $F_{8}$ : shifted Rosenbrock. The darker the element of $\boldsymbol{Q}$ is, the more times a variable is partitioned into $\mathcal{S}$ at the specific \#eval during the 25 runs. (a) 10-D average \#strong. (b) 30-D average \#strong. (c) 50-D average \#strong. (d) 100-D average \#strong. (e) 10-D $\boldsymbol{Q}$. (f) 30-D $\boldsymbol{Q}$. (g) 50-D $\boldsymbol{Q}$. (h) $100-\mathrm{D} \boldsymbol{Q}$.

![img-10.jpeg](img-10.jpeg)

Fig. 15. WI results on $F_{9}$ : shifted rotated high conditioned elliptic. The darker the element of $\boldsymbol{Q}$ is, the more times a variable is partitioned into $\mathcal{S}$ at the specific \#eval during the 25 runs. (a) 10-D average \#strong. (b) 30-D average \#strong. (c) 50-D average \#strong. (d) 100-D average \#strong. (e) 10-D $\boldsymbol{Q}$. (f) 30-D $\boldsymbol{Q}$. (g) 50-D $\boldsymbol{Q}$. (h) 100-D $\boldsymbol{Q}$.
procedure in every generation. By analyzing these records, we can give in-depth analysis on the problem properties characterization capability of EDA-MCC. We record the number of strongly dependent variables (\#strong), i.e., $|\mathcal{S}|$, and the elements in $\mathcal{S}$. The curves of the average \#strong of multiple ( 25 in all previous experiments) runs during evolution thus can be plotted. Which variables are partitioned into $\mathcal{S}$ can also be plotted by a matrix $\boldsymbol{Q}$. Each row of $\boldsymbol{Q}$ corresponds to a variable. Each column corresponds to one generation. Its element $\boldsymbol{Q}_{i j}$ on the $i$ th row and the $j$ th column, ranging from 0 to 25 , indicates how many runs (out of the 25 runs) partitioned variable $x_{i}$ into $\mathcal{S}$ at generation $j$. Because visually examining matrix $\boldsymbol{Q}$ with 50 or 100 rows is relatively hard for human eyes, we conduct additional 10-D and 30-D experiments for EDA-MCC. Results of 500-D experiments are even harder to read so we omit them here. The 10-D and 30-D tests are based on the same settings as previous 50-D and 100-D experiments in Section IV. Since an $n \in\{10,30\}$ is relatively small, it is easier to visually examine the results and summarize the changing trends as $n$ grows. For the purpose of comparing average \#strong and matrix $\boldsymbol{Q}$ in the same figure more clearly, we transform the column of $\boldsymbol{Q}$, which indicates the number of generations into the number of evaluations (\#eval) in all the following figures. The horizontal axis of average \#strong graphs is also converted to \#eval. Due to the page length limit, here we only report the results on $F_{1}, F_{8}, F_{9}$, and $F_{12}$. Although the results seem to be the solo effect of WI, actually SM plays an important role in working with WI. The interactions between WI and SM will be analyzed in Section IX.

From Fig. 13 we can see that on separable $F_{1}$, \#strong remains at a low level. But as $n$ grows, the level of \#strong also becomes higher. It can be interpreted as the effects of data sparsity in higher dimensional space. Using fixed $\theta$ through all experiments, the size of $\mathcal{W}$ can reduce as the search space enlarges (thus \#strong can increase), because

EDA-MCC may capture some correlations that do not actually exist. The relatively low level of \#strong is consistent with the separability of the problem. Furthermore, the gray levels of matrices $\boldsymbol{Q}$ are nearly uniform, indicating that all the variables in $\mathcal{S}$ are observed to play identical roles for optimizing. It is also consistent with the function's expression.

Fig. 14 shows that EDA-MCC correctly recognizes the problem structures of shifted Rosenbrock $F_{8}$. The variable dependency of the problem is a chain-like structure. The first variable determines the second, the second determines the third, and so on. We can see that WI first identifies the last pair of variables, then it quickly realizes that the first pair of variables are the most important. The structural information of the problem is clearly and precisely identified.

Experiments have shown that EDA-MCC significantly outperforms others on shifted rotated high conditioned elliptic $F_{9}$. Fig. 15 shows that WI always helps EDA-MCC recognize the problem structure. The WI results clearly show that some variables are constantly identified as strongly dependent during evolution (the dark rows of $\boldsymbol{Q}$ ). Furthermore, by checking the expression of $F_{9}$ (see Table III), we can see that the coefficient $\sum_{i=1}^{n}\left(10^{6}\right)^{\frac{i-1}{i-1}}$ before $z_{i}^{2}$ increases exponentially with $i$ given fixed $n$. Thus, among the transformed variables $z_{i}(1 \leq i \leq n)$, $z_{n}$ mostly impacts the function. $F_{9}$ can also be written as

$$
\begin{aligned}
F(\bar{x}) & =\sum_{i=1}^{n}\left(\sqrt{\left(10^{6}\right)^{\frac{i-1}{i-1}}} \cdot z_{i}\right)^{2}+f_{\text {bias }_{3}} \\
& =\sum_{i=1}^{n}\left(\sqrt{\left(10^{6}\right)^{\frac{i-1}{i-1}}} \cdot \sum_{j=1}^{n}\left(x_{j}-o_{j}\right) \boldsymbol{M}_{j i}\right)^{2}+f_{\text {bias }_{3}} \\
& =\sum_{i=1}^{n}\left(\sum_{j=1}^{n}\left(x_{j}-o_{j}\right) \boldsymbol{M}_{j i} \sqrt{\left(10^{6}\right)^{\frac{i-1}{i-1}}}\right)^{2}+f_{\text {bias }_{3}} \\
& =\sum_{i=1}^{n}\left(\sum_{j=1}^{n}\left(x_{j}-o_{j}\right) \boldsymbol{R}_{j i}\right)^{2}+f_{\text {bias }_{3}}
\end{aligned}
$$

![img-11.jpeg](img-11.jpeg)

Fig. 16. Explanations of WI results on $F_{9}$. The coefficients of $z_{i}$ are shown in the first column. Second column demonstrates $\operatorname{Abs}(\boldsymbol{R})$. Third column shows the $n$th column of $\operatorname{Abs}(\boldsymbol{R})$, denoted as $\operatorname{Abs}(\boldsymbol{R})(\because, n)$. The experimental $\boldsymbol{Q}$ results are shown in the last column, which are directly adopted from Fig. 15. We can see that the graphs in the last two columns are similar, especially for lower dimensional tests. (a) 10-D coefficients of $z_{i}$. (b) 10-D $\operatorname{Abs}(R)$. (c) 10-D $\operatorname{Abs}(R)(\because, 10)$. (d) 10-D $\boldsymbol{Q}$ in experiment. (e) 30-D coefficients of $z_{i}$. (f) 30-D $\operatorname{Abs}(R)$. (g) 30-D $\operatorname{Abs}(R)(\because, 30)$. (h) 30-D $\boldsymbol{Q}$ in experiment. (i) 50-D coefficients of $z_{i}$. (j) 50-D $\operatorname{Abs}(R)$. (k) 50-D $\operatorname{Abs}(R)(\because, 50)$. (1) 50-D $\boldsymbol{Q}$ in experiment. (m) 100-D coefficients of $z_{i}$. (n) 100-D $\operatorname{Abs}(R)$. (o) 100-D $\operatorname{Abs}(R)(\because, 100)$. (p) 100-D $\boldsymbol{Q}$ in experiment.
where $\boldsymbol{R}_{j i}=\boldsymbol{M}_{j i} \cdot \sqrt{\left(10^{6}\right)^{\frac{1}{n-1}}}, 1 \leq i, j \leq n . \boldsymbol{M}_{j i}$ is the element of $\boldsymbol{M}$ (value can be found in [53]). Matrix $\boldsymbol{R}$ partly represents to what extent the original variables $\bar{x}$ impact the function value. Roughly speaking, $\boldsymbol{R}_{j i}$ indicates the effect of $x_{j}$ onto $z_{i}$ and thus onto $F(\bar{x})$. Because $F_{7}$ is nonlinear, it is hard to analyze the exact impact of each variable. But since $z_{n}$ mainly impacts the function, we can instead analyze the $n$th column of $\boldsymbol{R}$ that can partly indicate the impact of $\bar{x}$ onto $z_{n}$ and thus onto $F(\bar{x})$ to give a rough analysis. We plot the curves of coefficient $\sqrt{\left(10^{6}\right)^{\frac{1}{n-1}}}$ as subfigures in the first column of Fig. 16. The subfigures in the second column show the absolute value
of matrix $\boldsymbol{R}, \operatorname{Abs}(\boldsymbol{R})$. We use absolute value because both positive or negative coefficients of a variable can influence the function value. The subfigures in the third column show the $n$th column of $\operatorname{Abs}(\boldsymbol{R})$, which is denoted as $\operatorname{Abs}(\boldsymbol{R})(\because, n)$. To compare them with the experimental results $\boldsymbol{Q}$ shown in the last column of Fig. 16, we stretch the widths to make them same size. Here, $\boldsymbol{Q}$ are directly from Fig. 15. We can see that when $n$ is large, the domination of $z_{n}$ becomes weak because the coefficients of $z_{n-1}, z_{n-2}$, etc., approach the coefficient of $z_{n}$. Therefore, the difference between the rough analysis and the experimental results also becomes larger. However, for all four tests, we can always find the evidence that WI

TABLE XIII
COMPARISON AMONG ' 'WI + SM,' ' 'SM ONLY,'' AND 'WI ONLY'' ON 100-D PROBLEMS


$\ddagger$ The value of Asymp. Sig. (two-tailed) $<0.001$ when compared with the results of "WI + SM."
Results are averaged over 25 runs. For each test, the best result is bolded. Results of "WI + SM" are compared with results of "SM Only" and "WI Only," respectively, by nonparametric Mann-Whitney $U$ test.
successfully recognizes the problem structure. Those variables most impacting optimization are correctly identified as dark rows in $\boldsymbol{Q} .{ }^{6}$

Fig. 17 shows the WI results on shifted rotated Rastrigin $F_{12}$. Results here also help explain why UMDA ${ }_{1}^{G}$ performs well on this problem while EDA-MCC fails. By examining the WI results on Rastrigin $F_{11}$ (not shown here), we find that the results are very similar to Fig. 17. Since $F_{11}$ is separable, the results are reasonable. As analyzed above, due to the inefficiency of covariance matrix scaling on this function with a huge number of local optima, EDA-MCC cannot perform well. However, on nonseparable $F_{12}$, WI still fails to recognize the problem structure because the sample size (selected size) is far less enough considering the huge number of local optima. From the information that WI can gather, $F_{12}$ just looks like a separable problem and no useful interdependencies are learned from the samples. As a result, EDA-MCC cannot perform well.

EDA-MCC's remarkable capability of characterizing the problem properties are clearly shown in this section. Although in some cases, EDA-MCC cannot find better solutions than candidate algorithms, its capability of describing the problems' underlying structural information is remarkable throughout the experiments. We regard it as the most valuable aspect of EDA-MCC. However, for $F_{11}-F_{13}$, which has a huge number of local optima, EDA-MCC still has limitation. It should also be noticed that in current implementation of EDA-MCC, we have not tried every possible univariate model on $\mathcal{W}$ and multivariate model on $\mathcal{S}$ other than the two Gaussian models employed. Therefore, even if EDA-MCC correctly characterizes the problem properties, such information may not be fully exploited due to the limitation of Gaussian models. This can possibly explain why in some cases EDA-MCC cannot outperform other algorithms, even with correct problem structure characterization. We have to admit that our results are still restricted within the capability of Gaussian models.

One thing that needs to be addressed is that when solving a real-world problem in practice, a user may not want or be able to run EDA-MCC for multiple times to obtain the problem's structural information. In this case, a recommended way is to allow EDA-MCC for restarts, and aggregate the information collected over multiple trials to generate the $\boldsymbol{Q}$ matrix.

## IX. ROLES OF WI AND SM, AND THEIR INTERACTIONS

In this section, we analyze the roles of WI and SM, and their interactions in EDA-MCC. Besides the implementation of EDA-MCC using WI + SM, we also implement an "SM only" version and a "WI only" version. We compare them with EDA-MCC on 100-D of the 13 test functions to analyze their respective roles. But to save space, we only report comparisons on selected functions $F_{2}, F_{8}-F_{11}$, and $F_{13}$ here. The parameters of "SM only" and "WI only" are exactly the same as the respective settings of SM and WI in previous EDA-MCC experiments. For each test, the population sizes of all three versions are set to the same as the selected best results of EDA-MCC.

The solution results are shown in Table XIII. We can see that when WI + SM performs the best, it usually finds order-of-magnitude better solutions than "SM only" and "WI only." Because "SM only" applies several multivariate models on all variables, the ways dealing with those actually weakly dependent variables are not so efficient. Therefore, it fails to perform the best on any function except the simplest $F_{2}$. On the other hand, "WI only" can perform slightly better than WI + SM on $F_{11}$ and $F_{13}$ and the same as WI + SM on $F_{2}$, but much worse on the others. The average CPU time costs are illustrated in Fig. 18. Although "SM only" cannot find solutions of comparable quality, its CPU time cost is usually acceptable or comparable with WI + SM, whereas "WI only" can cost much more CPU time. Generally speaking, WI + SM shows much more robust performance and moderate computational time cost than "SM only" and "WI only." It is also interesting that "WI only" can perform slightly better than WI + SM on $F_{11}$ and $F_{13}$. This implies that SM does not contribute a bit on these functions. It is consistent with our previous conclusions in Section IV-C4 that subspace partitioning with changing $c$ does not help solve these functions. Without SM, "WI only" can even perform a little better. But when SM is necessary, e.g., on $F_{8}-F_{10}$, "WI only" will fail.

To investigate the interaction between WI and SM in terms of EDA-MCC's capability of characterizing problem structure, we plot the WI results (\#strong and $\boldsymbol{Q}$ matrix) of "WI only" on $F_{8}$ and $F_{11}$ in Fig. 19. WI results of "WI only" on other functions are similar to either of the two. We can see that on problems with strong variable interdependencies like $F_{8}$, without SM, the precision of global multivariate model on $\mathcal{S}$ quickly deteriorates as the search proceeds. It affects not only the solution quality but also the WI procedure. Based on samples drawn from the imprecise global model, WI also becomes so useless that eventually all variables are partitioned into $\mathcal{S}$. It also results in high computational costs in modeling and sampling. On the other hand, when SM does not help as on $F_{11}$, "WI only" can still characterize the problem structure properly and finds solutions with the same or better quality.

We can conclude that SM helps maintain the global precision of the model (though it is approximated with subspace models), and thus helps WI more effectively recognize the problem structure. On the other hand, WI helps to apply suitable modeling and search strategies on weakly dependent and strongly dependent variables respectively, so that EDA-

![img-12.jpeg](img-12.jpeg)

Fig. 17. WI results on $F_{12}$ : shifted rotated Rastrigin. The darker the element of $\boldsymbol{Q}$ is, the more times a variable is partitioned into $\mathcal{S}$ at the specific \#eval during the 25 runs. (a) 10-D average \#strong. (b) 30-D average \#strong. (c) 50-D average \#strong. (d) 100-D average \#strong. (e) 10-D $\boldsymbol{Q}$. (f) 30-D $\boldsymbol{Q}$. (g) 50-D $\boldsymbol{Q}$. (h) 100-D $\boldsymbol{Q}$.
![img-13.jpeg](img-13.jpeg)

Fig. 18. Comparison of CPU time of "WI + SM," "SM only," and "WI only."

MCC can find good solutions effectively. In a word, the success of EDA-MCC, in terms of both the problem structure characterization capability, and the robust performance on large-scale optimization problems, are due to the interaction between WI and SM.

## X. CONCLUSION AND FUTURE WORK

In this paper, we first analyze the difficulties of continuous EDAs in high-dimensional search space. Due to the curse of dimensionality, given a finite population size, the performance of traditional EDAs deteriorates quickly as the problem size grows large. Their computational cost also increases fast when adopting a multivariate model for nonseparable problems. To improve the performance and reduce the computational cost for large-scale optimization, a novel multivariate EDA with model complexity control (EDA-MCC) is proposed. By employing WI and SM techniques, EDA-MCC shows significantly better performance than traditional EDAs on large-scale nonseparable problems (up to 500-D) with only a few local optima. The computational complexity and the requirement of large population sizes can be significantly
![img-14.jpeg](img-14.jpeg)

Fig. 19. Results of WI in "WI only" on $F_{8}$ and $F_{11}$. (a) $F_{8}$ : average \#strong. (b) $F_{11}$ : average \#strong. (c) $F_{8}: \boldsymbol{Q}$. (d) $F_{11}: \boldsymbol{Q}$.
reduced in EDA-MCC. Besides, EDA-MCC exhibits good scalability, and more importantly, the remarkable problem property characterization capability. When solving a problem, EDA-MCC will not only find a solution, but also give users feedback on the problem's structure. Such a capability can be far more valuable than just obtaining a solution. It is especially useful when facing a black box optimization problem. Based on the extracted problem structural information, more efficient algorithms can be designed specifically to give better solutions. The limitations of EDA-MCC are also analyzed. First, in low-dimensional search space where available population size is usually sufficiently large to offer a good global model estimation, EDA-MCC may not be as effective as traditional

EDAs. The advantage of EDA-MCC over traditional EDAs appears in high-dimensional space where a given population size fails to give a reliable global model estimation. Second, when facing large-scale nonseparable problems that have a huge number of local optima, EDA-MCC may not be as effective or efficient as a simple univariate Gaussian EDA. We should note that current discussions and implementation on EDA-MCC are still restricted to Gaussian models. Different base univariate and multivariate models other than Gaussian are still to be tested and analyzed. Moreover, smarter selfadaptive setting of $\theta$ and $c$ is still an interesting issue that is left for our future work.

## APPENDIX A

## COMPUTATIONAL COMPLEXITY OF UMDA ${ }_{c}^{G}$ AND EMNA $_{\text {global }}$

We consider the one-generation computational complexity here. Suppose the current model is built from the selected individuals of the last generation. Vector $\bar{X}$ denotes an individual and $X_{i}$ denotes the $i$ th variable of $\bar{X}$. The problem is $n$-dimensional. $M$ denotes the population size and $m$ denotes the number of selected individuals. Without loss of generality, we assume $\left|\mathcal{P}^{\prime}\right|=|\mathcal{P}|=M$.

1) $U M D A_{c}^{G}$ : Let $\mu_{i}$ and $\sigma_{i}^{2}$ denote the mean and the variance of $X_{i}$, respectively $(i=1, \ldots, n)$. The joint pdf is

$$
f(\vec{x})=\prod_{i=1}^{n} f_{N}\left(x_{i} ; \mu_{i}, \sigma_{i}^{2}\right)=\prod_{i=1}^{n} \frac{1}{\sigma_{i} \sqrt{2 \pi}} e^{-\frac{\left(x_{i}-\mu_{i}\right)^{2}}{2 \sigma_{i}^{2}}}
$$

- Model estimation.

Estimate $\left(\mu_{i}, \sigma_{i}^{2}\right)$ for $X_{i}(i=1, \ldots, n)$ :

1) Traverse $m$ selected individuals to estimate $\mu_{1}, \ldots, \mu_{n}: O(n m)$.
2) Traverse $m$ selected individuals to estimate $\sigma_{1}^{2}, \ldots, \sigma_{n}^{2}: O(n m)$.
Overall complexity: $O(n m)$.

- Sampling new solutions.

For $X_{i}$, we need to generate a standard normal random number $\zeta$, then do

$$
x_{i} \leftarrow \mu_{i}+\zeta \cdot \sigma_{i}
$$

Since such an operation is fast, we suppose sampling one variable costs $O(1)$, thus $O(n)$ is needed for $n$ variables. Repeating $M$ times to create $\mathcal{P}^{\prime}$ costs $O(n M)$.
Overall complexity: $O(n M)$.
2) $E M N A_{\text {global }}$ : Let $\vec{\mu}$ and $\boldsymbol{\Sigma}$ denote the $n$-dimensional mean vector and the $n \times n$ covariance matrix, respectively. The joint pdf is

$$
f(\vec{x})=f_{N}(\vec{x} ; \vec{\mu}, \boldsymbol{\Sigma})=\frac{1}{(2 \pi)^{\frac{n}{2}}|\boldsymbol{\Sigma}|^{\frac{1}{2}}} e^{-\frac{1}{2}(\vec{x}-\vec{\mu})^{T} \boldsymbol{\Sigma}^{-1}(\vec{x}-\vec{\mu})}
$$

- Model estimation.

1) Traverse $m$ selected individuals to estimate $\vec{\mu}$ : $O(n m)$.
2) Traverse $m$ selected individuals to estimate $\boldsymbol{\Sigma}$ : $O\left(n^{2} m\right)$.

Overall complexity: $O\left(n^{2} m\right)$.

- Sampling new solutions.

1) Before first time sampling, we need $O\left(n^{3}\right)$ to decompose $\boldsymbol{\Sigma}$ such that $\boldsymbol{\Sigma}=\boldsymbol{H} \boldsymbol{H}^{T}$ [26].
2) To sample a new solution, we need to generate a standard normal random vector $\vec{\zeta}$, then do

$$
\vec{x} \leftarrow \vec{\mu}+\vec{\zeta} \cdot \boldsymbol{H}
$$

Primary cost here is the $O\left(n^{2}\right)$ matrix multiplications. Repeating $M$ times to create $\mathcal{P}^{\prime}$ costs $O\left(n^{2} M\right)$.
Note that for EMNA $_{\text {global }}$, usually $M>n$ in practice, which means the population size is usually larger than the problem size. Therefore, the overall complexity of sampling is dominated by $O\left(n^{2} M\right)$ in second step.
Overall complexity: $O\left(n^{2} M\right)$.

## APPENDIX B

## COMPUTATIONAL COMPLEXITY OF EDA-MCC

Computation here using the same premises in Appendix A. We give the one-generation computational complexity of EDA-MCC. Here all $g_{i}(\cdot)$ are univariate Gaussian models, and all $h_{k}(\cdot)$ are multivariate Gaussian models.

- Model estimation.

1) Sampling $m_{\text {corr }}$ individuals from $m$ selected individuals: $O\left(m_{\text {corr }}\right)$.
2) Traverse $m_{\text {corr }}$ sampled individuals to calculate the global correlation matrix $\boldsymbol{C}: O\left(n^{2} m_{\text {corr }}\right)$.
3) Traverse $\boldsymbol{C}$ to construct $\mathcal{W}: O\left(n^{2}\right)$.
4) Building $g_{i}(\cdot)$ and $h_{k}(\cdot)$.

Consider two extreme situations:

- When $\mathcal{W}=\mathcal{V}$, all $n$ variables are identified as "weakly dependent":
a) Building $g_{i}(\cdot), i=1, \ldots, n$ :

Same order as UMDA ${ }_{c}^{G}$ model estimation, $O(n m)$.
b) No need to build $h_{k}(\cdot)$.

- When $\mathcal{W}=\emptyset$, all $n$ variables are identified as "strongly dependent":
a) No need to build $g_{i}(\cdot)$.
b) Building $h_{k}(\cdot), k=1, \ldots,\lceil n / c\rceil$ :

Same order as building a $c$ dimensional EMNA $_{\text {global }}$ model $\lceil n / c\rceil$ times, $O\left(c^{2} m\right.$. $n / c)=O(c n m)$.
Thus, the overall complexity is between

$$
O\left(n^{2} m_{\text {corr }}\right)+O(n m)
$$

and

$$
O\left(n^{2} m_{\text {corr }}\right)+O(c n m)
$$

Also note that $1 \ll m_{\text {corr }} \leq m, 1 \leq c \leq n$.

- Sampling solutions.

Consider two extreme situations:

- When $\mathcal{W}=\mathcal{V}$, all $n$ variables are sampled from $g_{i}(\cdot), i=1, \ldots, n$ :

1) Sampling from $g_{i}(\cdot), i=1, \ldots, n$ : Same order as UMDA ${ }^{G}$ solution sampling, $O(n M)$.
2) No need to sample from $h_{k}(\cdot)$.

- When $\mathcal{W}=\emptyset$, all $n$ variables are sampled from $h_{k}(\cdot), k=1, \ldots,\lceil n / c\rceil$ :

1) No need to sample from $g_{i}(\cdot)$.
2) Sampling from $h_{k}(\cdot), k=1, \ldots,\lceil n / c\rceil$ :

Same order as sampling from a $c$ dimensional EMNA global model $\lceil n / c\rceil$ times, $O\left(c^{2} M \cdot n / c\right)=$ $O(c n M)$.
Thus, the overall complexity is between

$$
O(n M)
$$

and

$$
O(c n M)
$$

## ACKNOWLEDGMENT

The authors are grateful to Dr. Zhenyu Yang, Dr. Yang Yu, Dr. Tapabrata Ray, and Dr. Lu Wang for their insightful comments that helped improve this paper, and to Dr. Alexander Mendiburu who kindly provided the source codes of MIMIC ${ }^{G}$ and EGNA.
