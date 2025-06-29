# A Self-adaptive Mixed Distribution Based Uni-variate Estimation of Distribution Algorithm for Large Scale Global Optimization 

Yu Wang and Bin Li


#### Abstract

Large scale global optimization (LSGO), which is highly needed for many scientific and engineering applications, is a very important and very difficult task in optimization domain. Various algorithms have been proposed to tackle this challenging problem, but the use of estimation of distribution algorithms (EDAs) to it is rare. This chapter aims at investigating the behavior and performances of univariate EDAs mixed with different kernel probability densities via fitness landscape analysis. Based on the analysis, a self-adaptive uni-variate EDA with mixed kernels (MUEDA) is proposed. To assess the effectiveness and efficiency of MUEDA, function optimization tasks with dimension scaling from 30 to 1500 are adopted. Compared to the recently published LSGO algorithms, MUEDA shows excellent convergence speed, final solution quality and dimensional scalability.


## 1 Introduction

Considered as a kind of classical yet extremely difficult task, large scale global optimization (LSGO) has attracted more and more research interest in recent years [21, 31]. LSGO problems have numerous scientific and engineering applications, such as designing large scale electronic systems, scheduling problems with large number of resources, vehicle routing in large scale traffic networks, gene detection in bioinformatics, etc. Therefore, effective LSGO algorithms are in high demand.

Inherently, the nonlinear characteristics of the practical applications usually include discontinuous prohibited zones, ramp rate limits, and nonsmooth or convex

[^0]
[^0]:    Yu Wang $\cdot$ Bin Li
    Nature Inspired Computation and Application Laboratory (NICAL), University of Science and Technology of China
    e-mail: wyustc@mail.ustc.edu.cn, binli@ustc.edu.cn

cost functions. Historically, a number of algorithms, including both mathematical and evolutionary algorithms, have been proposed to handle LSGO problems $[5,10,15,17,23,26,32,33,36,37,38,42,43]$. Various evolutionary algorithms (EAs) have been developed, in which significant progress has been observed [20] compared to the mathematical algorithms. The major advantages of these EAs over other classical methods can be summarized as: 1) prior knowledge of the search problem is not necessary for EAs, while for mathematical approaches the highly nonlinear characteristic of the problem must be approximated beforehand; 2) they work with a population of candidate solutions and can handle LSGO problems automatically through a single run. However, almost all of these approaches inevitably suffer from the "curse of dimensionality", which means poor performances on LSGO problems.

Without loss of generality, LSGO problems considered in this chapter can be stated as follows:

$$
\begin{aligned}
& \operatorname{minimize} F(\mathbf{x})=f\left(x_{1}, x_{2}, \ldots, x_{D}\right) \\
& \text { subject to } \mathbf{x} \in X
\end{aligned}
$$

where $X \subset R^{D}$ denotes the decision space with $D$ dimensions; $\mathbf{x}=\left\{x_{1}, x_{2}, \ldots, x_{D}\right\} \in$ $R^{D}$ is the decision variable vector; $f: X \rightarrow R$ stands for a real-valued continuous objective function for mapping from $D$ dimensional space to 1 dimensional fitness value $F(\mathbf{x})$. The dimensions of LSGO problems considered in this chapter are more than 100. Hence, the purpose of the approaches is to search for the minimized solution in such a large dimensional space. If $X$ is a closed and connected region in $R^{D}$, we call eq. (1) continuous LSGO.

In the previous works on LSGO, developing more effective operators for EAs has attracted much research attention. The successful implementations consist of selfadapting strategies for parameter setting, modification of the classical EA operators, etc. The reason of making these modifications is that the classical operators are usually developed for low-dimensional task and they lose their efficiency for highdimensional tasks. Their performances on LSGO problems cannot be measured effectively [31]. Recently, this field has attracted increased research attention and the typical approaches include population reduction for differential evolution (DE) [5], Dynamic multi-swarm PSO [43], and estimation of distribution algorithm (EDA) with mixed sampling operator [33]. For these approaches, the LSGO problems are optimized as an entire body, which means no divide-and-conquer methods are used. Actually, the implementation of specific operators is attributed to strengthening the algorithm's capability for higher dimensional tasks.

The classical EDAs have been proven to be effective on most classical test functions with less than 100 dimensions [11]. However, EDAs also suffer from the "curse of dimensionality", which implies that their performances deteriorate quickly as the search space increases in dimensions [33]. In this chapter, the difficulties associated with EDAs in solving LSGO problems will be discussed. Then, a heavy tail distribution based sampling (also called mutation in the evolutionary computation domain) operator will be analyzed, and introduced into a Gaussian based EDA to improve its performance. Compared to classical Gaussian distribution based operators, the heavy

tail distribution based operators have demonstrated better exploration and faster convergence speed on most test problems. Some typical examples include fast evolutionary programming (FEP) [40], fast evolution strategy (FES) [41], fast simulated annealing (FSA) [30], evolutionary programming using Lévy mutation (LEP) [13] and estimation of distribution algorithm with heavy tail distribution based sampling (LSEDA-gl) [33]. Due to the success of the above algorithms, the heavy tail distribution based sampling operator is regarded as a promising EA technique to tackle some difficult problems. In this chapter, the evovabilities of different sampling operators are investigated via a technique called fitness landscape portrait (FLP). Based on this analysis, a self-adaptive mixed model uni-variate EDA (MUEDA) is proposed. In order to evaluate the performance of MUEDA, it is tested on typical function optimization problems with dimensionality scaling from 30 to 1500 .

The rest of this chapter is organized as follows: In section 2, the principle and a brief review of EDAs are provided. The mathematical characteristics of Gaussian and heavy tail distributions are analyzed. Then, the main contributions of this work are presented. In section 3, a general FLP analysis is carried out to investigate the evolvability of different sampling operators in the low-dimension problems. After that, a self-adaptive uni-variate EDA with mixed kernels is proposed. In section 4, discussion of the experimental studies with dimensions ranging from 30 to 1500 is presented. Following which, the scalability and efficiency of MUEDA are presented. In section 5, several general conclusions are drawn and emphasized. In section 6, the future research directions of this area are outlined.

# 2 Related Work 

### 2.1 Estimation of Distribution Algorithms

The notion of modeling the search space was first proposed in the statistics and machine learning domain. Recently, many works within the Evolutionary Computation community have employed probabilistic models to describe the solution space [11]. These methods have come to be known as EDAs. It has been reported in various works that EDAs have been applied with significant success to many numerical and combination optimization problems in the past few years. Optimization by EDAs can be summarized into two major steps:

- Model the promising area of solution space of the optimization problem by learning from the superior solutions found thus far;
- Generate the population (i.e., offspring) for the next generation by sampling based on the estimated probabilistic model and then, replace the old population (i.e., parents) partially or fully.

These two steps can be regarded as a population-based version of the classical generate-and-test method [39]. As is shown in Fig. 1, there are no classical crossover or mutation operators in EDAs in contrast to traditional GA. The main operators of EDAs are as follows: selection involves selecting good solutions from the entire

Fig. 1 A general flowchart of EDA
![img-0.jpeg](img-0.jpeg)
population by truncation or league strategy; modeling involves building the probabilistic model to simulate the landscape of the problem; and generation is to sample the new population based on the probabilistic model. The evolution dynamics of EDAs depend on the distribution of the population directly. Therefore, the major advantage of EDAs is that they can explicitly extract useful structural information to efficiently generate new individuals, which results in faster convergence speed compared to GA [33].

In the EDA domain, modeling the structure of the optimization problem accurately has recently been an area of great concern. To overcome the disadvantages of limited learning ability of uni-variate EDAs, such as population-based incremental learning algorithm (PBIL) [25], stochastic hill climbing by vectors of normal distributions (SHCLVND) [24] and continuous uni-variate marginal distribution algorithm (UMDAc) [12], EDAs whose dependencies are considered in terms of pairwire or multiwire when building probabilistic model have been proposed. Some of the more successful approaches are mutual information maximizing input clustering (MIMIC) [12], estimation of Gaussian networks algorithm by edge exclusion (EGNAee) [12], estimation of Gaussian networks algorithm by BGe metric (EGNA ${ }_{\text {BGe }}$ ), clustering and estimation of Gaussian distribution algorithm (CEGDA) [16], etc. The learning ability of the EDAs is always considered as the major indicator of the performance for the above-mentioned algorithms. However, the fundamental task of EDAs is to search for the global optimum of the given optimization problem, rather than to simply model the structure of the optimization accurately. Furthermore, the computational cost of constructing a complex model is too expensive for LSGO problems, whose dimensions are usually more than 100. For example, the computational cost of generating the covariance matrix for iterated density estimation algorithm (IDEA) [1, 2, 4, 7] increases exponentially. The reported studies on

extending EDAs to LSGO domain are scarce so far. The emphasis of heavy tail based EDA in this work is therefore on extending EDAs to the LSGO domain.

# 2.2 Mathematical Characteristics of Heavy Tail Distribution 

In the above reviewed EDA works, Gaussian probabilistic distribution has been widely adopted in continuous optimization. In this work, a low proportion of heavy tail stable distribution is incorporated in order to strengthen the search ability of EDAs for LSGO problems.

Definition: Consider a process represented by a set $Y_{t}$ of identically distributed random variables. If the sum of these random variables has the same probability distribution as individual random variables, then this process is called stable [13].

The Gaussian process is a typical example of a stable process with finite second moment, which would lead to a characteristic scale and the Gaussian behavior for the probability density through the central limit theorem [13]. The probability density of Gaussian distribution with mean 0 and variance $\sigma$ is defined as follows:

$$
N(0, \sigma)=\frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{x^{2}}{2 \sigma^{2}}}
$$

Different to Gaussian probability distribution whose variance can be denoted as a finite scalar, a class of probability distributions with an infinite second moment that also yields a stable process were discovered by P. Lévy in the 1930s [14]. The formal representation for such a class of probability can be expressed as follows $[6,14]:$

$$
\mathbb{L}_{\alpha, \gamma} y=\frac{1}{\pi} \int_{0}^{\infty} e^{-\gamma q^{\alpha}} \cos (q y) d q \quad y \in \mathbf{R}
$$

where $\gamma$ is the scaling factor satisfying $\gamma>0$, and $\alpha$ controls the shape of the distribution, requiring $0<\alpha<2$. More analytic details about the Lévy distribution are available in $[6,13,14]$. Although the analytic form of the integral is still unknown for general $\alpha$, the shapes generated by Lévy distributions with different $\alpha$ values are known: the length of the tail is inversely proportional to the value of $\alpha$. The Cauchy probability distribution adopted in FEP, is a special case of the Lévy probability distribution with $\alpha=1$. For the limit of $\alpha=2$, the distribution is reduced to the classical Gaussian distribution which is not included in Lévy probability distribution class. The Cauchy density with median 0 and upper quartile $\tau$ can be denoted as follows:

$$
C(0, \tau)=\frac{1}{\pi} \frac{\tau^{2}}{x^{2}+\tau^{2}}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2 Comparison among Gaussian, Cauchy and Mixed distributions in terms of the density function (up left) and the distributions of 10000 sampled points

The comparison between Gaussian and Cauchy probability density is shown in Fig. 2. It is apparent that the characteristic of infinite second moment in Cauchy probability provides a much wider distribution.

Since it is rather difficult to generate random numbers under different Lévy probability distributions except Cauchy distribution [13], several works adopt a mixed distribution, which combines the Gaussian distribution with Cauchy distribution by a suitable proportion to simulate the desired distribution. Some successful examples are [27] and [33]. These special mixed sampling density functions can be expressed as:

$$
f_{M}=(1-\eta) \frac{1}{\sqrt{2 \pi}} e^{-\frac{x^{2}}{2}}+\eta \frac{1}{\pi} \frac{1}{x^{2}+1}
$$

where $\eta$ stands for the mixed proportion that can be tuned to any scalar between 0 and 1 . In this chapter, $\eta=0.1$ is used for analysis without statement. After investigating the mixed distribution in [13, 27, 33], it was observed that $\eta=0.1$ favors more problems than any other value of $\eta$. For heavy distribution

based sampling operator, the sampling distribution in classical uni-variate EDA $(N(\mu, \sigma)=\mu+\sigma N(0,1))$ is replaced by:

$$
N_{M}(\mu, \sigma)=\mu+\sigma(1-\eta) N(0,1)+\sigma \eta C(0,1)
$$

The density of 10000 sampled points by Gaussian, Cauchy and Mixed probability distribution are compared in Fig. 2. In contrast to the widest distribution sampled by Cauchy, it can be observed that the shape of a 2-D Gaussian distribution is like that of a sphere with the density increasing from the periphery towards the core. Similar observation can be made for mixed distribution but the sampling region is much wider. The mixed distribution is expected to achieve a more reasonable balance between exploration and exploitation theoretically.

# 2.3 Analysis of Heavy Tail Distribution in Evolutionary Computation 

### 2.3.1 Fast Evolutionary Programming

In 1996, Yao X [40] proposed an important EP version named FEP, which replaces the Gaussian mutation in classical EP (CEP) with the Cauchy mutation. This change leads the individuals to make a much longer jump, which results in a significantly faster convergence speed when the global optima is far from the initial point. It was shown that the FEP outperforms CEP in terms of convergence speed in most test functions and the accuracy of the result in the multimodal functions [40].

Due to the excellent performance of FEP, [35] and [40] investigated the differences of expected length between Cauchy mutation and Gaussian mutation. The existing analysis methods of different probability operators focus on the properties of the operators themselves (i.e., properties related to the operators closely only). The expected length of Gaussian mutation jump with $\sigma=1$ is calculated as follows:

$$
E_{G}(x)=2 \int_{0}^{+\infty} x \frac{1}{\sqrt{2 \pi}} e^{-\frac{x^{2}}{2}} d x=\frac{2}{\sqrt{2 \pi}}=0.80
$$

and the expected length of Cauchy mutation jump is calculated as:

$$
E_{C}(x)=2 \int_{0}^{+\infty} x \frac{1}{\pi} \frac{1}{x^{2}+1} d x=+\infty
$$

Under the 1-D space, it is obvious that the Cauchy probability operator extends the expected sampling region to an infinite area. Therefore, a general conclusion has been made in [40]: Gaussian mutation is much more localized than Cauchy mutation. However, benefiting from the proportion of Cauchy probability incorporated into it, the mixed operator $\left(E_{M}(x)=+\infty\right)$ also exhibits the ability of sampling population widely. There is no remarkable difference between mixed sampling operator

and Cauchy sampling operator in expected sampling length theoretically. Thus, in the following section, a much more effective analysis tool FLP is adopted to distinguish the differences between different operators.

# 2.3.2 Heavy Tail Distribution Analysis 

An important work which tries to answer the question: when do the important tail distributions help? is presented in [9]. The most important contributions of this work come from two hypotheses and their proofs, which can be summarized as: although the heavy tail distributions have stronger ability of maintaining diversity, they inevitably get lost in huge dimensional space, which will be proven to be worth discussing in the following section. The experimental analysis in [9] was carried out to study the behaviors of ES on Rastrigin function optimization with different distributions based mutation operators. Obviously, the viewpoint of the first hypothesis that heavy tail distributions are good at maintaining diversity is absolutely true. In our work, however, the heavy tail distributions are also proven to work in large dimension problems empirically, which is remarkably inconsistent to the second hypothesis.

### 2.4 Major Contribution

Based on the above review and discussion, the contributions and differences of this chapter compared to the previous work are summarized as follows:

- The tool fitness landscape portrait (FLP) [28] was proposed over over 5 years ago. Besides the random search, it has not attracted much interest in analyzing the specific EA operators, such as crossover, mutation, etc. In our work, this effective analysis tool is implemented to analyze the expected behaviors of different kernel distribution sampling operators in low dimensional spaces. Based on the analysis, some valuable suggestions on designing appropriate sampling operator are presented theoretically.
- LSGO problems are considered as a difficult task in the optimization domain. In this work, an effective algorithm called the self-adaptive MUEDA is proposed for the large scale and complex optimization problems.


## 3 Fitness Landscape Analysis and Self-adaptive Mixed Probability Distribution Based Uni-Variate Estimation of Distribution Algorithm

In this section, the evolvability analysis of different kernel probability distributions is presented in terms of fitness landscape analysis on low dimensional landscapes. Based on the theoretical analysis, an effective self-adaptive heavy tail based sampling operator is proposed to strengthen the search ability of uni-variate EDAs.

# 3.1 Fitness Landscape Analysis 

In fitness landscape analysis, the optimization problems can be expressed as a set of landscapes containing one or more optima [29, 34]. Based on the number of the optima, we also classify the landscapes into smooth or rugged problems. Evolution can thus be viewed as the movement of the population, represented by a set of points (genotypes), towards lower (fitter) areas of the landscape [28]. In order to explore the evolvability of different probability based operators, we adopt partial FLP technique to test the ability of sampling population on more promising regions by different operators on two typical landscapes.

FLP that was derived from comprehensive local view for sampling is adopted as an effective tool to analyze the evolvability of given operator on special landscapes. The metric selected for describing the evolvability of different operators is defined as follows:

$$
\begin{aligned}
& \operatorname{flag}(x)= \begin{cases}1, & \text { if } f(x) \leq f\left(x_{g}\right) \\
0, & \text { otherwise }\end{cases} \\
& E_{e v}\left(x_{g}\right)=\frac{\int_{-\infty}^{+\infty} f_{o p e}(x) \cdot \operatorname{flag}(x) d x}{\int_{-\infty}^{+\infty} f_{o p e}(x) d x}
\end{aligned}
$$

where evolvability $E_{e v}\left(x_{g}\right)$ of solution $x_{g}$ with fitness $f_{\text {ope }}\left(x_{g}\right)$ for the EA operator ope is directly tied to the probability of solution $x_{g}$ not generating offspring of lower fitness.

Since the difficulty of searching global optimum related to the structure of the fitness landscape closely is now clear, two typical fitness landscapes (i.e. sphere landscape and rugged landscape), which include most of the existing landscapes, are chosen to evaluate the evolvability of Gaussian, Cauchy and mixed probability sampling operators.

### 3.1.1 Smooth Landscape

The evolvability of sampling operators with $\sigma=1$ is tested on the region intercepted by $[-10,10]$ for the sphere landscape shown in Fig. 3 (left). The evolvability metric curve line which is generated for each mean value moving from -10 to 10 by eq.(10) is shown in Fig. 3 (right). The sphere landscape is especially adopted to evaluate the evolvability of different sampling operators on smooth problems.

It can be observed from the evolvability curve that the Gaussian sampling operator provides the best evolvability for the whole region. Accordingly, the evolvability of Cauchy sampling operator decreases sharply while the global optimum is still far away, and this delays the convergence speed significantly. This may be the reason for the unsolved question in $[9,35]$ that Gaussian leads to a faster convergence speed than Cauchy for Sphere problem. Benefiting from the property of Gaussian distribution, the mixed sampling operator is equipped with similar evolvability as Gaussian sampling operator, which is remarkably better than Cauchy sampling operator by itself.

![img-2.jpeg](img-2.jpeg)

Fig. 3 Sphere landscape on the left and evolvability curve line graph on the right

# 3.1.2 Nonsmooth Landscape 

It has been known that evolvability on rugged landscape mainly depends on the capability of escaping from the local optima. Consider the rugged landscape $(f(x)=$ $\cos (x)-\frac{x}{20})$ shown in Fig. 4 (left). We intercept one local optimal basin $[0,2 \pi]$ for analysis. Curve lines of evolvability generated by different sampling operators with mean value moving from 0 to $2 \pi$ are also generated by eq. (10).

It is apparent that the evolvability of Gaussian sampling operator worsens sharply near the local optimum, which means that its evolvability shrinks quickly towards the local optimum. By comparison, Cauchy sampling operator demonstrates the best ability of escaping from the local optima. Therefore, the incorporation of low proportional Cauchy distribution highly improves the evolvability of mixed sampling operator. Therefore, the mixed sampling operator keeps a steady high probability of escaping from the local optima and thus, maintains the evolvability effectively.
![img-3.jpeg](img-3.jpeg)

Fig. 4 Sphere landscape on the left and evolvability curve line graph on the right

Based on the above fitness landscape analysis, the mixed operator shows superior ability in both moving quickly towards the global optimum on smooth landscape and maintaining evolvability on rugged landscape globally. Compared to the classical Gaussian sampling operator, the sampling area of the mixed sampling operator exceeds the Gaussian model. In such case, the balance between learning and optimization is well handled. Therefore, it seems to be a promising way to develop more robust EDA by using mixed sampling operator.

# 3.2 Algorithm 

Compared with the mutation operators of GA, ES and EP that mutate the individuals, the sampling operator of EDA mutates the distribution of the whole population in each generation. To strengthen the global search ability, a mixed Gaussian and Lévy distribution is adopted here, which is similar to [33].

Based on the above analysis, a new self-adaptive uni-variate EDA is proposed here. In order to reduce the complexity of conducting the probabilistic model, the uni-variate EDA whose variables are considered independently is adopted in our algorithm. Similar to UMDAc [12], the joint probabilistic distribution over a set of random variables $x=\left\{x_{i}\right\}$ where $\mathrm{i}=1,2 \ldots D$ for $D$ dimensional space is defined as follows:

$$
P(\mathbf{x})=\prod_{i=1}^{D} P\left(x_{i}\right)
$$

The probability distribution used to model each variable $P\left(x_{i}\right)$ is a single mixed Gaussian and Cauchy distribution. In contrast to iterated density estimation algorithm (IDEA) [1] developed by Bosman which requires computing all elements of covariance matrix to adapt an arbitrary Gaussian, MUEDA abandons adapting the non-diagonal elements in covariance matrix, which remarkably reduces the computational cost for LSGO problems. The updated rule for $P(x)$ is defined as follows:

$$
P_{t+1}(\mathbf{x})=(1-\theta) \cdot P_{t}(\mathbf{x})+\theta \cdot P_{t}^{\prime}(\mathbf{x})
$$

where $P_{t}^{\prime}(\mathbf{x})$ is exactly the estimated joint probability distribution for the superior solutions of $\tau$ generation under the classical Gaussian distribution and $\theta$ stands for the learning intensity coefficient. Hence, the candidates for the $t+1$ generation are produced based on $P_{t}(\mathbf{x})$. Similar to UMDAc, the model for UMDAc is built by the current population only, which means that the learning coefficient $\theta$ is 1 .

The details of mixed distribution and the strategy for generating each candidate are shown as:

$$
\begin{gathered}
\text { randnum }=\text { rand } \\
P_{m}=\frac{10 \cdot \text { randnum }}{D} \\
N_{L}= \begin{cases}0.9 \cdot N(0,1)+0.1 \cdot C, & \text { if } D<100 \\
\left(1-P_{m}\right) \cdot N(0,1)+P_{m} \cdot C, & \text { otherwise }\end{cases}
\end{gathered}
$$

$$
X_{j i}=\bar{X}_{i}+\sqrt{\delta_{i}} \cdot N_{L}
$$

In eq.(13), $N(0,1)$ stands for the Gaussian distribution with mean 0 and standard deviation $1 ; C$ denotes the Cauchy distribution with $t=1 ; D$ is the dimensional size of the problem; randnum is generated randomly based on uniform distribution between $(0,1)$. The probability distribution for creating each offspring on different dimensional size is self-adapted as shown in eq.(13): a smaller mixed probability $P_{m}$ is adopted for a larger dimensional size. In eq.(14), the $i$ th element of $j$ th individual is sampled under mixed Gaussian and Lévy distribution model $N_{L}$, where $\bar{X}_{i}$ stands for the $i$ th element of the mean vector. Compared with UMDAc, whose sampling operator is denoted as $X_{j i}=\bar{X}_{i}+\sqrt{\delta_{i}} \cdot N(0,1)$, the standard Gaussian probability $N(0,1)$ is replaced with the mixed Gaussian and Lévy distribution $N_{L}$.

The flow of MUEDA is described as follows:

# Input: 

- LSGO problem;
- a termination condition;

Output: The solution with best fitness value.
Flow of MUEDA:
Step 0) Initialization:

- Step 0.0) Set population size $N P=(\log (D)-3) \times 50$, selection size $N=$ $(\log (D)-3.5) \times 15$ and weight vector $W$.
- Step 0.1) Randomly initialize the population $X_{0}$.
- Step 0.2) Set $t=0$.


## Step 1) Reproduction and update:

- Step 1.0) Reproduction: Sample the new candidates by specific EA operator.
- Step 1.1) Set $t=t+1$.
- Step 1.2) Selection: Select $N$ best individuals by truncation strategy.
- Step 1.3) Update: Update the model with the selected individuals (eq.(6)).

Step 2) Standard Deviation Control Strategy (STDC) Then, if termination condition is met, go to step 3, else go to step 1.
Step 3) Terminate and output the GO.
It has been observed that one crucial problem that prevents uni-variate Gaussian based EDAs from biasing the search population towards a better region is that the standard deviation of some variables often shrinks to zero quickly while the global optimum is still far away [33]. In step 2, we introduce the standard deviation control strategy (STDC) to improve the exploration ability of uni-variate Gaussian based EDA. The main idea of STDC is to estimate a common threshold of standard deviations for all variables during the optimization process to control their shrinking speeds and therefore, to control the decreasing level of diversity dynamically. In more detail, the variables with lower standard deviation values than the corresponding thresholds will be forced to set their standard deviations to the corresponding

thresholds. The weighted mean of the standard deviations of all variables is used as the threshold here. The details of STDC are shown as follows:

```
Pseudo code of STDC
    begin STDC
        for j=1:D
            if \(\delta(j)<W(j) \times \bar{\delta}\)
                \(\delta(j)=W(j) \times \bar{\delta}\)
                /* \bar{\delta}\) is the mean of variances */
                /* W is a weight vector */
            end if
        end for
    end
```

After analyzing a great deal of $W$ values for each dimensionality setting, we calculate the value of $W$ in an adaptive way shown as in eq. (15) for problems of different $D$ s:

$$
\begin{gathered}
W(i)=0.55-e^{l g\left(\frac{D}{10^{2}}\right)} \\
\text { for } \quad i=1,2, \ldots, D
\end{gathered}
$$

The metric $W$ is determined by $D$ only, which means a larger $W$ is adopted for problems with lower $D$. It is observed that lower $W$ value is adopted for larger $D$. Eq. (15) is used because the metric $W$ is generally hard for the inexperienced users to choose.

Some existing works on standard deviation based triggering of variance scaling have been reported, such as adaptive variance scaling [8] and standard deviation ratio [3]. In these approaches, the scaling of standard deviation is determined by the performance of the latest generation. In contrast, the STDC strategy only enlarges the standard deviations of some variables under an adaptive threshold vector. Therefore, STDC is much simpler.

# 4 Experimental Study 

### 4.1 Classical Function Optimization with Low Dimensionality

The purpose of this experiment is to compare mixed distribution based sampling operator of MUEDA with the Gaussian distribution based classical UMDAc. Moreover, the existing heavy tail distribution based algorithms, including FEP and FES, are adopted to provide the comparison results. The formal definitions of the test functions are summarized in Table 1. Function 1-6 are unimodal problems. Function $7-12$ are multimodal problems, whose landscapes are full of local optima. In this chapter, the initialized population are randomly generated within the bounds for all experiments.

Table 1 Classical benchmark problems to be minimized

Table 2 Experimental results for classical function optimization

Statistical experimental results of 50 runs

For fair comparison, we set the parameters as in [40]. The following parameters are used in this experiment: 1) population size 100 for all algorithms; 2) maximum number of generations: 1500 for function 1 , function 6 , function 9 , function 11 and function 12; 2000 for function 2 and function 10; 3000 for function 7, 5000 for function 3, function 4 and function 8. The statistical experimental results of 50

![img-4.jpeg](img-4.jpeg)

Fig. 5 Evolutionary curves of unimodal problems
independent runs are summarized in Table 2. Fig. 5 and 6 show the optimization curves for the unimodal problems and multimodal problems respectively.

Compared to UMDAc, it is apparent that MUEDA provides significantly better performance in terms of both convergence speed and accuracy of the final result for almost all of the test functions with 30 D . For the unimodal problems functions 1-6, MUEDA always provides the fastest convergence speed. It should be noted that, for function 5, a well-known hard test problem, the MUEDA approaches the true global optimum within the fixed number of generations, while the other algorithms are still struck at local optima after the final generation. The global search ability

![img-5.jpeg](img-5.jpeg)

Fig. 6 Evolutionary curves of multimodal problems
of MUEDA is proven via experiments on multimodal test functions (function 7 function 12). The accurate results (i.e. the error is lower than $10^{-8}$ ) are achieved in all runs on function 9 - function 12. For the problem with noise incorporated function 7, MUEDA also outperforms the other approaches. For function 8, MUEDA cannot achieve satisfactory result, the reason for which will be discussed in the following section. Through this experiment, the advantages of MUEDA on both exploration and exploitation have been clearly demostrated.

# 4.2 Experiments on LSGO Problems 

The benchmark set selected for this experiment consists of 6 test functions defined in [31]. Functions 1 - 3 are unimodal functions and Functions 4 - 6 are multimodal functions. To prevent exploitation of symmetry of the search space and of the typical zero value associated with the global optimum, the local optima of classical functions are shifted to a value different than zero and the function values of the global optima are non-zero. Without loss of generality, maximum fitness evaluation size (MFES) $500 \times D$ is adopted for function 1, 3, 5 and 6 and $5000 \times D$ for function 2 and 4 . The details of standard benchmarks are defined in Table 3. The source codes for these functions are available from http://nical.ustc.edu.cn/cec08ss.php and http://www3.ntu. edu.sg/home/EPNSugan/.

Table 3 Standard benchmark problems of CEC08 to be minimized
# 4.2.1 Comparison among Different Cauchy Proportions Based Algorithm 

In order to illustrate the impacts of different heavy tail distributions, four Cauchy proportion are adopted for comparison: $\eta=0$ (UMDAc), $\eta=0.1$ (constant Cauchy), $\eta=1$ (only Cauchy), and adaptive $\eta$ (eq. (13) for MUEDA). For fair comparison, we choose parameters as consistently as possible. For external parameters, we set $N P=(|\log (D)-3| \times 50)$ and $N=(|\log (D)-3.5| \times 15)$. The statistical experimental results of over 50 runs are summarized in Table 4, in which the best result for each function is in boldface.

Table 4 Experimental results for $100 D$ cec08 function optimization

Statistical experimental results of 25 runs

It is apparent that Cauchy only $(\eta=1)$ distribution based algorithm fails in all problems. Therefore, excessive exploitation is not always beneficial for high dimensional problems. Generally speaking, MUEDA outperforms the other algorithms remarkably in most problems and is followed by UMDAc. For the hard task funcec 2 , it is interesting to note that the result provided by MUEDA is very accurate while all of the other algorithms fail to get close to the global optima. The performances of all algorithms for Rochenbrock problem deteriorate sharply.

![img-6.jpeg](img-6.jpeg)

Fig. 7 Rastrigin problem: landscape on the left and convergence process comparison on the right

The 2-D landscape of Rastrigin problem and variance change process comparison are shown in Fig. 7. It is obvious that the landscape is full of local optima. The above experimental results have shown that UMDAc provides the best result for Rastrigin problem. However, the change curve of variance shows that the population of classical UMDAc just shrinks into a local optimum after a small fitness evaluation size. For this reason, the Gaussian distribution exhibits low evolvability and the final result is no longer reasonable. For the heavy tail distribution based operators, there is a high variance level throughout the search (which appears as a random search). Therefore, heavy tail distribution based operators seem more robust in these landscapes, although the final accuracy is unsatisfactory.

# 4.2.2 Comparison with other LSGO Evolutionary Algorithms 

To benchmark MUEDA further, the comparison on larger dimensional (1000 D) problems is carried out. In some recent studies, some algorithms have reported the regular experimental results for the funcec functions. We only take the EA based algorithms into account. The algorithms are listed as follows:

- Efficient Population Utilization Strategy for Particle Swarm Optimizer (EPUSPSO) $[10]$
- Unbiased Evolutionary Programming (UEP) [17]
- Self-Adaptive Differential Evolution algorithm (jDEdynNP-F) [5]
- Dynamic multi-swarm particle swarm optimizer (DMS-PSO) [43]
- Multilevel cooperative coevolution (MLCC) [38]
- Differential Evolution with Self-Adaptive cooperative co-evolution (DEwSAcc) [42]

The statistical analysis is shown in Table 5. In Table 6, the $t$-test results regarding algorithm1 vs algorithm2 are shown as ' + ', '-', 's+' and 's-' when algorithm1 is insignificantly better than, insignificantly worse than, significantly better than, and significantly worse than algorithm2 respectively. For unimodal problems, it is

Table 5 Experimental results for 1000 D cec08 function optimization

Statistical experimental results of 25 runs

Table 6 The $t$-test results of comparing MUEDA with the other algorithms

observed that MUEDA provides accurate results. For 1000 D funcec 1, DMS-PSO outperforms MUEDA in terms of accuracy. For the other algorithms, high-quality results cannot be generated due to the low computational cost. Funcec 2 with high $D$ is an extremely hard task because the variables are non-separable. Although the fitness landscape is very smooth, the fact that only one variable with largest absolute value contributes to fitness value makes it almost impossible to be solved by classical approaches. It is evident that only MUEDA succeeds in converging to a solution with accuracy lower than $10^{0}$ to the true global optimum. For the other algorithms, especially cooperative coevolution based ones, the search is stuck badly, which implies that they are not effective enough to deal with the non-separate LSGO problem. These results are not surprising, because only MUEDA considers modelling the rough structure of the search space. Furthermore, the implementation of mixed distribution makes breaking the common restriction possible.

The multimodal problems become much harder as the dimensionality increases to 1000 . Funcec 3, whose variables are linked to a neighboring one (i.e. Rocenbrock problem), is the hardest task. For this problem, all algorithms fail in all runs. Another difficulty of this problem is that the valley towards the global optimum is very narrow and none of the algorithms could adaptively control the shrinking speed to suit this nonseparate problem. Amongst the compared algorithms, MUEDA demonstrates the most superior performance. For funcec 4, most of the algorithms fail to obtain GO except MLCC. Funcec 5 and 6 can be solved completely by MUEDA. The dominant convergence ability of MUEDA is strongly indicated by all these results.

# 4.2.3 Scalability Study 

In order to study the scalability of MUEDA, we compare it with cooperative coevolution based LSGO approach Cooperative coevolution differential evolution II (DECC-II) on the 1500 dimensional problems. The reasons of selecting DECC-II in this experiment are as follows: 1) the cooperative coevolution appears to be a very promising method and has becomes very popular in LSGO domain [31]; 2) Compared with the classical cooperative coevolution based algorithms FEPCC [15] and CCGA [23], DECC-II has performed better on most problems [36]. In DECC-II, the variables selected for optimization in one iteration are chosen randomly with constant size 100. The other parameters chosen for experiment are the same as [36]. The comparison of evolution process between MUEDA and DECC-II on 1500 dimensional function optimization is shown in Fig. 8, and the comparison of final error between the best solution and true global optimum is shown in Table 7.

It is apparent that for unimodal function 1 and function 2, the proposed algorithm outperforms DECC-II not only in convergence speed, but also in the accuracy of results obtained. This is especially true for function 2 whose variables are linked. Similar conclusion can be drawn for multimodal functions globally, although the results achieved by DECC-II and proposed algorithm on function 4 (i.e. shift Rastrigin) are comparable. The reasons for this result have been analyzed in the first experiment. It is observed that the proposed algorithm works well on function 5 and 6 within such low computational cost even for 1500 D . In summary, the proposed algorithm provides a steady and accurate performance even for problems scaling to 1500 dimensions.

### 4.2.4 Efficiency Study

In the traditional analysis of $[18,19]$, the efficiency of the search method is tested on the problems with different dimensionality setting. Efficiency is defined on number of function evaluations needed to solve the problem [18]. In order to evaluate the efficiency of MUEDA, the results for multimodal problems - Ackley function (function 9 in Table 1) and Giewangk function (function 10 in Table 1) are presented in Table 8, 9 and Fig. 9. Moreover, the effective algorithms DE and PSO are also implemented in order to provide comparison results. For fair comparison, we

![img-7.jpeg](img-7.jpeg)

Fig. 8 Evolutionary curves of 1500 D problems
choose the same population size 200 for all algorithms and the most commonly used extensive parameters for respective algorithms.

It is apparent that the computational cost of MUEDA tends to increase linearly as the dimensionality arises. For DE and PSO, the efficiencies are much less. This is especially true when $D$ is very large. It is evident that handling large scale optimization problems is a difficult task for evolutionary algorithms. Compared to breeder

Table 7 Experimental results for $1500 D$ cec08 function optimization

Statistical experimental results of 25 runs

Table 8 Efficiency test on Ackley function

Termination criterion is $10^{-3}$.

Table 9 Efficiency test on Giewangk function

Termination criterion is $10^{-3}$.

![img-8.jpeg](img-8.jpeg)

Fig. 9 Efficiency test on Ackley function on the left and Giewangk function on the right

GA scaling like $D \ln (D)$, MUEDA shows excellent efficiency, which scales linearly. Thus, the advantages of MUEDA on LSGO problems are easily observable.

# 5 Concluding Remarks 

In this chapter, there are two major works, which can be summarized as:

- Via fitness landscape analysis, the expected behaviors and evolvability of Univariate EDAs with different kernel probability distributions based sampling operators are studied in low dimensional spaces. The evolvability change curve analysis reveals that mixing Gaussian with Cauchy distribution may be a promising way to strengthen the search ability.
- Based on the above analysis, a self-adaptive mixed distribution based uni-variate EDA named MUEDA is proposed for both LSGO problems. For the low dimensional problems, MUEDA provides excellent performance. Experimental evidence of large scale global function optimization is demonstrated to illustrate the merits and demerits of the proposed algorithm. Moreover, some scalability study is also carried out to evaluate MUEDA further.

In summary, this work aims at providing both expected and experimental analysis on improving the performances of uni-variate EDAs by designing a more effective sampling operator. As to the experimental results, MUEDA improves the performance of the uni-variate EDA significantly, and the proposed algorithm is good at both exploration and exploitation simultaneously. Particularly, the adaptive mixed distribution based sampling strategy could be simply incorporated into existing EDAs to accelerate the convergence speed and escape from the local optima.

## 6 Future Research Direction

There are still many issues that need to be urgently analyzed, of which the major ones are summarized as follows:

- Although many attempts have been carried out to analyze the characteristics of heavy tail distributions, the comprehensive mathematical properties of the heavy tail probability distributions are subject to suggestion.
- Even though the algorithm performed remarkably better than the classical algorithms, there are still some problems that cannot be completely solved by the proposed algorithm.
- In this chapter, the heavy tail distribution based sampling operator has shown good efficiency based not only on theoretical analysis, but also on the experimental analysis. More attempts are needed to prove the efficiency to the adaptive mixed strategy, such as incorporating the strategy to EP or ES.

Acknowledgements. This work was partially supported by the National Natural Science Foundation of China (Grants No. 60401015, U0835002), the Chinese Academy of Science Special Grant for Postgraduate Research, Innovation and Practice, IEEE Walter Kaplus Student Summer Research Grant, and Graduate Innovation Fund of University of Science and Technology of China.

We are deeply grateful to the reviewers for their invaluable comments which help us improve the quality of the chapter. The first author would like to thank Mr. Aimin Zhou for his warm-hearted help and the invaluable suggestions! Moreover, the authors would like to thank Mr. Xiaolei Chen and Ms. Xuexiao Lai, who helped us a lot in this chapter's preparation.

# Appendix 

## Classical test function 11 and 12

$u$ and $y_{i}$ are defined as follows:

$$
\begin{gathered}
u\left(x_{i}, a, k, m\right)= \begin{cases}k\left(x_{i}-a\right)^{m}, & \text { if } x_{i}>a \\
0, & -a \leq x_{i} \leq a \\
k\left(-x_{i}-a\right)^{m}, & \text { if } x_{i}<-a\end{cases} \\
y_{i}=1+\frac{1}{4}\left(x_{i}+1\right)
\end{gathered}
$$

$f_{11}$ Generalized Penalized Functions

$$
\begin{gathered}
f_{11}=\frac{\pi}{30}\left\{10 \sin ^{2}+\sum_{i=1}^{2} 9\left(y_{i}-1\right)^{2} \cdot[1+\right. \\
\left.10 \sin ^{2}\left(\pi y_{i+1}+\left(y_{n}-1\right)^{2}\right)\right]+\sum_{i=1}^{30} u\left(x_{i}, 10,100,4\right)\}
\end{gathered}
$$

$f_{12}$ Generalized Penalized Functions

$$
\begin{gathered}
f_{12}=0.1\left\{\sin ^{2}\left(\pi 3 x_{1}\right)+\sum_{i=1}^{2} 9\left(x_{i}-1\right)^{2} \cdot[1+\right. \\
\left.\left.\sin ^{2}\left(3 \pi x_{i+1}\right)\right]+\left(x_{n}-1\right)^{2}\left[1+\sin ^{2}\left(2 \pi x_{3} 0\right)\right]\right\}+\sum_{i=1}^{30} u\left(x_{i}, 5,100,4\right)
\end{gathered}
$$

# A List of Terms and Definition 

Heavy tail probability distribution - Different from Gaussian probability distribution whose variance can be denoted as a finite scalar, heavy tail probability distribution stands for a class of probability distributions with an infinite second moment that also yields a stable process.

Estimation of distribution algorithms (EDAs) - The methods that make use of the notion of modeling process as applied in statistics and machine learning domain to

Table 10 Abbreviations used in this chapter
extract the important information to effectively build the space structure belong to EDAs.

Fitness landscape analysis - Fitness landscape analysis considers optimization problems as a set of landscapes containing one or more optima. Evolution can thus be viewed as the movement of the population, represented by a set of points (genotypes), towards lower (fitter) areas of the landscape.

Large scale global optimization - Large scale global optimization defines a suit of global optimization problems with more than 100 variables to be optimized.

Kernel probability distribution - Consider a probability with mean 0 , symmetrical probability distribution and monotonously increasing; then this probability can be used as Kernel probability distribution for EDA.
