# Linkages Detection in Histogram-Based Estimation of Distribution Algorithm 

Nan Ding ${ }^{1}$ and Shude Zhou ${ }^{2}$<br>${ }^{1}$ Department of Electronic Engineering, Tsinghua University, Beijing, 100084<br>China<br>${ }^{2}$ China Academy of Electronics and Information Technology, Beijing, 100041<br>China


#### Abstract

In this chapter, we review two methods that deal with the linkage detection in the Histogram-based Estimation of Distribution Algorithms; one is based on probabilistic graphical models, and the other is based on space transformation. The two methods deal with the linkage in the optimization problem with different accuracy and with different computational complexity. Probabilistic graphical model is generally more accurate but always associated to high-cost, while transformation is the opposite. In the following, we will mainly discuss the way to reduce the complexity of the method based on probabilistic graphical model and the way to obtain the transformation which captures the dominant linkage of the problem.


## 1 Introduction

Estimation of distribution algorithms (EDAs) are a class of evolutionary algorithms that use probabilistic model of promising solutions found so far to obtain new candidate solutions of optimized problems. One of the charming characteristics of this evolutionary paradigm is that the joint probability density can explicitly represent correlation among variables [1,16]. It is verified by several researchers [2] that multivari-ate-dependency EDAs have the potential ability to optimize hard problems with strong nonlinearity. However, it is also noted that how to efficiently learn the complex probabilistic model is a bottleneck problem. Therefore, obtaining a good balance between the complication of probabilistic models and the efficiency of learning method is a key factor for designing new EDAs.

In continuous domain, the predominant probabilistic model applied by EDAs is based on Gaussian probability distribution. Continuous EDAs based on multivariate Gaussian distribution have polynomial computational complexity. However, the inherent shortcoming of Gaussian-based EDA is that the unimodal model is too rough and thus is likely to mislead the search to a local optimum when solving complex optimization problems. Although clustering techniques such as Gaussian mixture model, Gaussian kernel model are considered to conquer this shortcoming in the literature, their complicated probabilistic distributions make it more difficult to estimate the linkage information, and thus the computational complexity increases remarkably.

Histogram model is another alternative probabilistic model in the continuous EDA. It is also called a kind of discretization of the continuous problem. In comparison with

unimodal Gaussian model, histogram probabilistic model is able to represent multiple local optima by bins of different heights. Histogram model has already been used in previous work [3-11,13,14]. For example, marginal histogram models are applied in the FWH [7] by S. Tsutsui et al. and the histogram-based EDA (HEDA) [8,9] by N. Ding et al. B. Yuan et al. [11] also proposed the HEDA as an extension of the PBIL [12]. Q. Zhang et al. introduce EDA/L [14] in which several local search strategies are employed in a marginal histogram model.

In those above algorithms, the complete probability is approximated by the product of the marginal probability of each variable, that is to say, the linkages of the variables are discarded. However, as we know, when optimizing problems with bounded epistasis, the linkage information should be given prior consideration in the process of the evolutionary algorithms. The IDEA [4,5] based on histogram model (IDEA-H) by P.A.N. Bosman et al. used the multivariate histogram model to consider the variable linkage, but they also remarked that the complexity of the IDEA-H grows exponentially when expressing joint probability of multiple random variables.

The aim of the chapter is to conquer the linkage problem of HEDA from two aspects: one is based on probabilistic graphical models (PGM), where the multivariate histogram model is considered; and the other is based on space transformation, where the marginal distribution is built in the transformed space. PGM takes the Markov properties into account, where the variable is independent of each other when given its neighbors in the graphical models, thus it avoids estimating the complete probability. Space transformation works under the assumption that a decent transformation from the original space may cancel out some of the dominant linkages among the variables. The two methods deal with the variables linkages of the optimization problem with different accuracy and with different computational complexity. Probabilistic graphical model is generally more accurate but always associated to high-cost, while transformation is the opposite.

We also want to acknowledge that P. Pošík in [18] had a general introduction to the real-valued evolutionary algorithm on the use of probabilistic model and coordinate transform, which is really helpful to our work. The chapter here would mostly focus on the Histogram-based EDA and would contain the specific concerns about the histogram model.

This chapter is organized as follows. Section 2 briefly reviews the HEDA, especially the marginal HEDA. In Section 3, HEDA based on probabilistic graphical models is introduced and especially we discuss how to reduce its computational complexity. Section 4 is about HEDA based on space transformation.

# 2 Histogram-Based Estimation of Distribution Algorithm and Its Marginal Case 

The histogram-based estimation of distribution algorithm (HEDA) has a main framework as follow:

1. Initialize the histogram model
2. Generate population $P(t)$ by sampling on the histogram model.
3. Evaluate and rank the population $P(t)$.

4. Update the histogram model according to the selected individuals $P^{\prime}(t)$.
5. Return to step 2 if not terminated.

The marginal histogram model has a general form of

$$
P\left(Z_{0}, \ldots, Z_{l-1}\right)=\prod_{i=0}^{l-1} P\left(Z_{i}\right)
$$

In Eq.(1), each $P\left(Z_{i}\right)(i=0, \ldots, l-1)$ denotes a 1-variate histogram model.
The core of marginal histogram-based estimation of distribution algorithm is to estimate the marginal distributions of $P\left(Z_{i}\right)(i=0, \ldots, l-1)$ and then to generate new individuals by sampling on $P\left(Z_{i}\right)$ for each variable. The FWH [7] and the sur-shrHEDA [9] both belong to this class of HEDA. We now have a brief review of these two algorithms.

In the FWH, the height of each bin in each variable $Z_{i}$ is proportional to the count of the selected individuals in it. To sample each variable of the new individual, firstly a bin is sampled according to the heights of the bins of the variable, and then the real value of that variable of the new individual is uniformly sampled in the domain of the bin. Since the height of the bin can be normalized to be equal to the probability of the bin, in the later description we will no longer differentiate the two phrases "the height of the bin" and "the probability of the bin".

In the sur-shr-HEDA, two specific strategies for HEDA, the surrounding effect and the shrinking strategy were developed to conquer the two drawbacks of the HEDA. The initial population should be large enough to sample the variables with a lot of bins; otherwise, many bins will never get a chance to be sampled. The solution accuracy is greatly influenced by the width of bins and highly accurate solutions can only be achieved by setting enough number of bins.

With surrounding effect, if an individual in a certain bin No. $i$ is selected, not only the No. $i$ bin gets an improvement on its height, but the surrounded bins, i.e. the No. $(i+1)$ and No. $(i-1)$ bins, also get the minor improvements (always the height of its surrounded bin times the surrounding factor) on their heights respectively. Using the surrounding effect, those bins with heights of zero have the opportunity to be sampled. Furthermore, it has been shown in our previous work that the HEDA with surrounding effect can find the best bins near the current sampled bins with hill-climbing during the search process. That ensures the algorithm to find the optimal bin with small population, even when the number of bins is large.

For the shrinking strategy, if the height of the highest bin of a variable is over the threshold value, the domain of that variable will shrink to the domain of that highest bin, and the new domain will be divided into bins as the initial step of the algorithm. Since the searching space gradually shrinks, using the shrinking strategy will make the solution accurate enough.

Experimental results have already shown that the HEDA combining both the surrounding effect and the shrinking strategy performs excellently in continuous optimization, especially, in those problems with multiple local optima. [9]

Marginal histogram-based estimation of distribution algorithm is frequently applied in practice for its simplicity and efficiency. However, the obvious drawback of the marginal probability estimation is that it loses the ability to detect any variable

linkages of the problem. This drawback is serious in the problems that variables are strongly dependent with each other.

In the following, we supply two solutions for this problem. The first is by applying probabilistic graphical model; the second is by applying a space transformation.

# 3 HEDA Based on Probabilistic Graphical Models 

Applying probabilistic graphical models (PGM) in HEDA was first put forward by P.A.N. Bosman in his IDEA-H [4] (If we regard HEDA as a special case of discrete EDAs, the history of applying probabilistic graphical model is even longer, for example, see [3].) In the analysis of the IEDA-H, Bosman regarded that the computational complexity of the IDEA-H grows exponentially with the maximum number of the variables that a variable conditionally depends on, which becomes the bottleneck of the IDEA-H. Recently, an accelerated algorithm, which is called the dHEDA, with polynomial complexity dictated by the size of the population, was proposed in [10]. Since the computational complexity is the main concern for HEDA based on PGM, we will discuss the dHEDA in details.

### 3.1 General Framework

In general, the HEDA based on PGM share the same framework as any other HEDAs, except that it iteratively updates and samples from $P\left(Z_{0}, \ldots, Z_{l-1}\right)$ under the assumption that:

$$
P\left(Z_{0}, \ldots, Z_{l-1}\right)=P\left(Z_{j_{l-1}}\right) \cdot \prod_{i=0}^{l-1} P\left(Z_{j_{i}} \mid Z_{\pi\left(j_{i}\right.}, \ldots, Z_{\pi\left(j_{i}\right)_{\pi\left(j_{i}\right)=1}}\right)
$$

In Eq.(2), $\left\{Z_{0}, \ldots, Z_{l-1}\right\}=\left\{Z_{j_{0}}, \ldots Z_{j_{l-1}}\right\}$, but they are in different order; while $\left\{Z_{\pi\left(j_{i}\right.}, \ldots, Z_{\pi\left(j_{i}\right)_{\pi\left(j_{i}\right)=1}}\right\} \subseteq\left\{Z_{j_{i+1}}, \ldots Z_{j_{l-1}}\right\}, \mid \pi\left(j_{i}\right) \in k . Z_{i}(i=1, \ldots, l)$ is the discrete random variable which represents the bin indices that take values from $\left\{1, \ldots, n_{b}\right\}$.
![img-0.jpeg](img-0.jpeg)

Fig. 1. $P\left(x_{1}, \ldots, x_{6}\right)=P\left(x_{1}\right) P\left(x_{2} \mid x_{1}\right) P\left(x_{3} \mid x_{1}\right) P\left(x_{4} \mid x_{1}, x_{2}\right) P\left(x_{5} \mid x_{2}, x_{3}\right) P\left(x_{6} \mid x_{5}\right)$

That is to say, the probabilistic graphical model simplifies the complete factorized probability function by assuming the Markov properties of the variables, see Fig.1. as an example. In the expansion of the complete probability, each variable is regarded to be conditionally independent of any other variables given its parent variables (the nodes with an edge pointing to the current node in the graph, for example, $x_{1}$ and $x_{2}$ are both parent variables of $x_{4}$ ). Interested readers may consult to [19] for more knowledge about PGM.

Then the core of the HEDA based on PGM is to estimate each item in the right hand side of Eq.(2). In each generation, there are mainly two jobs to estimate the PGM:

1. The probability density structure (PDS) $\left\{Z_{j_{i}}, Z_{\pi(i), j_{0}}, \ldots, Z_{\pi(i), j_{\pi(i), k+1}}\right\}$ have to be found.
2. The probability density function (PDF) $\left\{P\left(Z_{j_{i}} \mid Z_{\pi(i), j_{0}}, \ldots, Z_{\pi(i), j_{\pi(i), k+1}}\right)\right\}$ and $P\left(Z_{j_{i-1}}\right)$ have to be calculated.

In the following discussion of this section, more details of the above two jobs in the dHEDA are presented.

# 3.2 PDS Search 

In each generation, the PDS $\left\{Z_{j_{i}}, Z_{\pi(i), j_{0}}, \ldots, Z_{\pi(i), j_{\pi(i), k+1}}\right\} \quad(i=0, \ldots, l-1)$, is learnt from the selected individuals. To minimize the difference between Eq.(2) and the complete factorized probabilistic function, like the IDEA-H[4], the dHEDA minimize the following expression when using the Kullback-Leibler (K-L) divergence as a metric:

$$
J\left(Z_{0}, \ldots, Z_{l-1}\right)=H\left(Z_{j_{i-1}}\right)+\sum_{i=0}^{l-2} H\left(Z_{j_{i}} \mid Z_{\pi(i), j_{0}}, \ldots, Z_{\pi(i), j_{\pi(i), k+1}}\right)
$$

where $H(\bullet)$ denotes the entropy. For variable $i$ with $k$ parents, the conditional entropy is calculated by:

$$
H\left(Z_{i} \mid Z_{\pi(i), j_{0}}, \ldots, Z_{\pi(i), k_{l-1}}\right)=H\left(Z_{i}, Z_{\pi(i), j_{0}}, \ldots, Z_{\pi(i), k_{l-1}}\right)-H\left(Z_{\pi(i), j_{0}}, \ldots, Z_{\pi(i), k_{l-1}}\right)
$$

If the variables are of $n_{b}$ bins, the joint entropy of $\left\{Z_{0}, \ldots, Z_{n-1}\right\}$ is calculated by:

$$
H\left(Z_{0}, \ldots, Z_{n-1}\right)=-\sum_{z_{0}=0}^{n_{b}-1} \ldots \sum_{z_{n-1}=0}^{n_{b}-1} P_{Z_{0}, \ldots, Z_{n-1}}\left(z_{0}, \ldots, z_{n-1}\right) \ln \left(P_{Z_{0}, \ldots, Z_{n-1}}\left(z_{0}, \ldots, z_{n-1}\right)\right)
$$

where $P\left(Z_{0}=z_{0}, \ldots, Z_{n-1}=z_{n-1}\right)$ is equal to the summation of the probability factors of those selected individuals that fall into the super-bin $\left(Z_{0}=z_{0}, \ldots, Z_{n-1}=z_{n-1}\right)$ in the dHEDA. Note that we introduce the new term super-bin to avoid confusion with the concept of bin in marginal case. The concept of super-bin is no different from that of bin except that super-bin denotes the bin in more than 1 dimension. We also use $\left(z_{0}, \ldots, z_{n-1}\right)$ as a short hand of $\left(Z_{0}=z_{0}, \ldots, Z_{n-1}=z_{n-1}\right)$ in the following.

In order to find the promising PDS, greedy methods can be employed to minimize $J\left(Z_{0}, \ldots, Z_{l-1}\right)$. It has been verified that without considering the calculation cost of Eq.(3), we can minimize $J\left(Z_{0}, \ldots, Z_{l-1}\right)$ using greedy methods with polynomial computational complexity. For example, Bosman et al. proposed 3 methods for 3 different general structures (chain structure, tree structure and Bayesian Network structure). These graphical models are successful applied in Gaussian-based EDA [4] and exhibit acceptable polynomial computational complexity.

# 3.3 Computation Issue on the K-L Divergence 

The computation issue on the K-L divergence $J\left(Z_{0}, \ldots, Z_{l-1}\right)$ is important because it is the metric to lead the PDS search. It is clear from Eq.(3)(4) that the core of calculating $J\left(Z_{0}, \ldots, Z_{l-1}\right)$ is to calculate the joint entropy. In other words, if the entropy calculation is efficient, it will be also efficient to obtain $J\left(Z_{0}, \ldots, Z_{l-1}\right)$. However, the obstacle in histogram-based EDA is that the computational complexity of direct calculation of $J\left(Z_{0}, \ldots, Z_{l-1}\right)$ using Eq.(5) is unaffordable, because it would take exponential complexity on the maximum number of the parents nodes over all the nodes.

However, it is noticed that the probability of the super-bin $P\left(Z_{0}=z_{0}, \ldots, Z_{n-1}=z_{n-1}\right)$ is non-zero if and only if there are selected individuals in the current generation falling into this super-bin. Since there are only the number of selected individuals $n_{\text {best }}$ for PGM estimation, given any $\left\{Z_{i}, Z_{\pi(i), i_{0}}, \ldots, Z_{\pi(i), i_{\pi(i), i-1}}\right\}$, there exist only at most $n_{\text {best }}$ super-bins with non-zero probability.

According to Eq.(5), the value of the joint entropy is only contributed by those non-zero super-bins. Thus, without altering the result, the expression of joint entropy is rewritten as:

$$
H\left(Z_{0}, \ldots, Z_{n-1}\right)=-\sum_{i=1}^{N} P_{Z_{0}, \ldots, Z_{n-1}}\left(z_{0}^{i}, \ldots, z_{n-1}^{i}\right) \ln \left(P_{Z_{0}, \ldots, Z_{n-1}}\left(z_{0}^{i}, \ldots, z_{n-1}^{i}\right)\right)
$$

In Eq.(6), $N \leq n_{\text {best }}$ indicates the number of non-zero super-bins, and $P_{Z_{0}, \ldots, Z_{n-1}}\left(z_{0}, \ldots, z_{n-1}\right)$ is the probability (height) of super-bin $\left(z_{0}, \ldots, z_{n-1}\right)$ which at least one of the selected individuals falls in. The reason of $N \leq n_{\text {best }}$ is because there might be more than one individual falling into the same super-bin.

So, the process to calculate the entropy of certain joint variables is as following. Initially, $H\left(Z_{0}, \ldots, Z_{n-1}\right)=0$. We first pick an unpicked individual; gain its super-bin $\left(z_{0}^{i}, \ldots, z_{n-1}^{i}\right)$; check if $\left(z_{0}^{i}, \ldots, z_{n-1}^{i}\right)$ exists in the memory if yes we improve the height of super-bin $\left(z_{0}^{i}, \ldots, z_{n-1}^{i}\right)$, if no we create a new super-bin $\left(z_{0}^{i}, \ldots, z_{n-1}^{i}\right)$ and improve its height. After all individuals are picked; we sum up the probability (heights) of the super-bins in the memory times its logarithms and get the entropy.

Now, let us analyze the computational complexity of the calculation of $H\left(Z_{i}, Z_{\pi(i), i_{0}}, \ldots, Z_{\pi(i)_{n-1}}\right)$. The step to find those individuals that belong to the same bin, and to sum up their improvements to get the height of that bin takes $O\left[n_{\text {best }}^{2} \cdot(k+1)\right]$.

Thus, the complexity of $O\left[n_{\text {best }}^{2} \cdot(k+1)\right]$ is taken to calculate $H\left(Z_{i}, Z_{\pi(i)_{\mathrm{t}}}, \ldots, Z_{\pi(i)_{\mathrm{t}-1}}\right)$. Overall, the complexity of $O\left[n_{\text {best }}^{2} \cdot l^{2}\right]$ is taken to calculate $J\left(Z_{0}, \ldots, Z_{l-1}\right)$.

Overall, we can conclude that we are able to find the PDS with polynomial time applying the above method to calculate entropies. This is much tractable than the way that directly applies Eq.(5) to calculate entropies.

# 3.4 PDF Calculation 

It is noticed that all the PDFs are the byproducts of entropy computation. Thus, there is no more extra step for PDF calculation if we save their results during the PDS search.

So far, we have introduced the main framework of the HEDA based on probabilistic graphical model, especially the details of entropy computation because of its importance in computational complexity.

There is something more that needs to be remarked: it seems tricky that the probabilities of many super-bins are equal to zero. Does that mean the later-generation individuals will never get a chance to be sampled in those zero-probability bins (which is obviously unreasonable for its lack of general knowledge)? This is not the case. In fact, in the first step, the sampling process chooses the bins only according to the height of the bin, which means those zero-height bins cannot be chosen; but in the second step, the real-value of the individuals can be sampled out of the chosen bins if we applies a variant surrounding effect. Interested readers might refer to [10] for details.

### 3.5 Experimental Results

We design two experiments: the first is to test the computational efficiency of the accelerated algorithm; the second is to test the performance of the HEDA based on PGM on several benchmark continuous optimization problems.
![img-1.jpeg](img-1.jpeg)

Fig. 2. The computation time to calculate the joint entropy by the dHEDA and the IDEA-H

First, let us examine the computational time of the dHEDA and that of the IDEAH . The experimental results are shown in fig. 2 .

The number of the bins is respectively 20, 30, 40; the number of the variables in the joint entropy is from 1 to 5 ; and the number of the selected individuals is 100 . The reason that we only test at most 5 joint variables is because our PC memory excesses when we try to run the test of 6 joint variables by the IDEA-H with 40 bins. 20 times are run before the average time is calculated. The experiment is based on CPU-Intel Pentium 2.8 GHz .

In Fig.2, we notice that the time by the IDEA-H grows remarkably with the increase of the number of the joint variables. If we check the time in the case of bin=40 in TABLE-IV, the time of 5 joint variables entropy calculation by the IDEA-H is over 100s. On the other hand, the time by the dHEDA increases slowly and remains as a small amount of time $\left(\approx 10^{-3} \mathrm{~s}\right)$.

The other point is the great difference between them in the computational time with the growing number of the bins: the time by the IDEA-H has a distinct grow, but the time by the dHEDA hardly rises.

These experimental results are concordant to our earlier analysis. Recall that the computational complexity for calculating $H\left(Z_{t}, Z_{\pi(t)_{0}}, \ldots, Z_{\pi\left(t_{0, t}\right.}\right)$ is $O\left[\left(n_{b}\right)^{k+1}\right]$ for IDEA-H, but only $O\left[n_{\text {best }}^{2} \cdot(k+1)\right]$ for the dHEDA.

Next, we examine the performance of HEDA based on PGM with three other continuous EDAs: the UMDA $_{c}$, the IDEA-G [4], and the sur-shr-HEDA [9] on 4 benchmark continuous problems: Sphere Function, Summation Cancellation Function, Schwefel-1 Function, and Schwefel-2 Function.

Table 1. Parameter Settings of the 4 Algorithms

Among the 4 algorithms, the UMDA $_{\mathrm{c}}$ and the IDEA-G are based on Gaussian distribution, the sur-shr-HEDA and the dHEDA are based on histogram model; the UMDA $_{\mathrm{c}}$ and the sur-shr-HEDA are marginal HEDAs, the IDEA-G and the dHEDA are HEDA based on PGM. Note that we use the dHEDA to substitute the IDEA-H because of the computational concern. The settings of the 4 algorithms are listed in Table 1.

Among the 4 problems, Sphere Function and Summation Cancellation Function are unimodal, while the other 2 are multimodal. The Sphere Function and Schwefel-1 Function are separable, while the other 2 are non-separable. The problems are listed in Table 2.

Table 2. Problem Descriptions


Each of the algorithms is run for 20 times for each problem, and the mean value, the best case, and the standard deviation for the 20 runs are collected in Table 3.

According to the results in Table 3, we can mainly summarize two points as follows:
The first is that the histogram-based EDAs outperform the Gaussian-based EDAs on the above multimodal problems. For example, in the Schwefel-1 Function (which is always regarded as a typical multimodal test problem), both of the histogram-based EDAs are able to achieve the optimum of the problem, while the Gaussian-based EDAs both fail. The excellent performance made by the histogram-based EDAs agrees to our earlier remarks: it is straightforward for the histogram model to estimate the multimodal distribution. Meanwhile, since the Gaussian-based EDAs are unimodal, their models are too rough to estimate the multimodal problems efficiently.

Table 3. Experimental Results

The second is the contrast between the algorithms based on PDS without linkage and the ones based on PDS with linkage. It appears in the experiment that the dHEDAs outperforms the sur-shr-HEDA in both of the non-separable problems. The IDEA-G outperforms the UMDA $_{\mathrm{c}}$ in the unimodal non-separable problems, but the two algorithms gain the comparable results on those multimodal non-separable problems. In the Summation Cancellation Function, for example, the IDEA-G's mean value is above $10^{4}$ while the UMDA ${ }_{\mathrm{c}}$ is below $10^{1}$; and the dHEDA succeeds all of the times but the sur-shr-HEDA performs unstably with large deviations. This fact clearly illustrates the meaning of the learning of the linkage information in the IDEA-G and the dHEDA.

# 4 HEDA Based on Space Transformation 

Although it has already been introduced the accelerated method in probabilistic graphical models, the complexity burden is comparably large in the HEDA. One much simpler method is to deal with the linkages in marginal case.

The method is based on the space transformation, especially the linear transformation. P. Pošík in $[17,18]$ proposed several successful evolutionary algorithms on the use of space transformation. We will introduce the transformation according to the covariance-matrix of the samples in this section and apply the method in the HEDA. We call that algorithm to be the Marginal Estimation of Distribution Algorithm in

Characteristic Space of Covariance-Matrix (CM-MEDA). Intrinsically, it is equal to preprocessing the samples by PCA in EDA. Similar work can also been found in [15].

# 4.1 Covariance-Matrix of the Samples 

We first review several basic and well-known properties of Covariance-Matrix. The Covariance-Matrix of a set of samples is defined as follows:
Given a set of $m$ samples $\bar{x}_{i}$, where $\bar{x}_{i}=\left(x_{i 1}, x_{i 2}, \ldots, x_{i j}\right)^{T}$
The Covariance-Matrix is defined as

$$
C=\frac{1}{m-1} \sum_{i=1}^{m}\left(\overline{x_{i}}-\bar{x}_{i}\right)\left(\overline{x_{i}}^{T}-\bar{x}_{i}^{T}\right)
$$

And it has the following important properties:

1. The Covariance-Matrix is real and symmetric, that is:

$$
c_{i j} \in R(\forall i, j=1, \ldots, l) \text { and } C=C^{T}
$$

2. The Covariance-Matrix is diagonalizable, that is:

$$
\begin{gathered}
\exists Q, \text { s.t. } C=Q[\lambda] Q^{-1} \\
\text { where }[\lambda]=\operatorname{diag}\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{l}\right)
\end{gathered}
$$

3. All the eigenvectors with different eigenvalues are orthogonal with each other.
4. There exists a matrix $P=\left(\overline{p_{1}}, \overline{p_{2}}, \ldots, \overline{p_{l}}\right)$, which satisfies $C=P[\lambda] P^{-1}$ and all $\overline{p_{i}}$ are orthogonal with each other, that is $P^{T}=P^{-1}$.

Finally, we formulate some important representations. The space defined in $P$ is the characteristic space of the Covariance-Matrix $C$, and each $p_{i}$ is the basis of the space. Clearly, according to Property 2 and Property 4, we have $C=P^{T}[\lambda] P$, where $[\lambda]=\operatorname{diag}\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{l}\right)$.

### 4.2 General Framework

The CM-MEDA is an algorithm which estimates the marginal distribution of the problem on a transformed space: the characteristic space of the Covariance-Matrix of the selected samples.

The algorithm begins with an initialized population that is generated randomly. In each generation, it evaluates the fitness of each sample and selects several promising samples. The above two step has no difference from any other evolutionary algorithms.

Then the CM-MEDA calculates the Covariance-Matrix $C$ on the selected samples and then calculates the matrix $P$, which defines the characteristic space of the Covari-ance- Matrix $C$.

After $P$ is obtained, the selected samples are transformed to the new space by multiplying $P^{T}$, so we can obtain the value on each variable in the new coordinate space. Assuming a selected sample of $x$, this step is finished by $\bar{x}^{T}=P^{T} \cdot \bar{x}$.

The marginal distributions are estimated in the new space. After the marginal distributions of the variables in the new space have been estimated, new $\overline{\bar{x}^{\prime}}$ are sampled according to the estimated distribution in each variable.

At last, we transform the samples back into the initial coordinate space, according to $\stackrel{\bar{\sigma}}{\bar{x}}=\left(P^{-1}\right)^{T} \cdot \overline{\bar{x}^{\prime}}=P \cdot \overline{\bar{x}^{\prime}}$.

Note that when we transform the samples back, some samples might out of constraints. If that happens, we discard those "illegal" samples and resample the new ones. After we have built the new population, we evaluate the fitness and go to the next generation.

In short, the framework of CM-MEDA is as followed:

1. Initialize the population
2. Select the samples with high fitness
3. Calculate the Covariance-Matrix $C$ of the selected samples and build the matrix $P$
4. Transform the selected samples onto the characteristic space of the CovarianceMatrix by $\overline{\bar{x}^{\prime}}=P^{T} \cdot \bar{x}$
5. Estimate the marginal models on the new space according to the distribution of the transformed selected samples
6. Make new samples $\overline{\bar{x}}$ according to the marginal models in the transformed space
7. Transform the new samples from the transformed space back to the original space by $\stackrel{\bar{\sigma}}{\bar{x}}=P \cdot \stackrel{\bar{\tau}}{\bar{x}}$ and check if all the new samples are legal. Resample the illegal samples.
8. Return to step 2 if not terminated.

# 4.3 CM-MEDA in Histogram Case 

In the histogram-based CM-MEDA, the marginal distribution in the transformed space is based on histogram model. There is only one specific concern besides the general framework of the CM-MEDA in the histogram case, that is: How to decide the domain (i.e. upper bound and lower bound) of the histogram model in the transformed space.

We solve this problem in a simple way: the domain of each variable is decided according to the range of the selected samples in each variable. Note that, under this way the algorithm can naturally shrink the domain of the variables. Besides, to avoid loss of generality, we make the domain of the variable be a little larger than the range of the variables. In our algorithm, there is one more bin to the left of the leftmost sample and one more bin to the rightmost sample. The leftmost sample is in the center of the bin it belongs to, and so is the rightmost sample. See Fig. 3 as an illustration.

### 4.4 Relation to Principal Component Analysis

Principal component analysis (PCA) is a method that seeks for a projection which best represents the samples in a least-squares sense [20]. It intrinsically provides a promising way of finding the projections which mostly capture the variance of the

![img-2.jpeg](img-2.jpeg)

Fig. 3. The position of the selected samples and the domain of the bins. Note that the leftmost and the rightmost selected samples are in the center of the bins that they belong to. And there is one more bin to the left of the leftmost sample and one more bin to the right of the rightmost sample.
samples. For example, the first component (the principal component) is the projection that the samples have the maximum variance; the second component is the projection with the maximum variance in the subspace orthogonal to the first component, and etc.

Since the components given in PCA are the same as the eigenvectors of Covari-ance-Matrix in the CM-MEDA, we can alternatively think that the core of the CMMEDA is to find the projections which maximize the variance in the space iteratively, because each eigenvector is the projection which has the maximum variance of the samples in the subspace orthogonal to the eigenvectors with higher eigenvalues. The projection which has the maximum variance of samples is the one which mostly needs estimation in evolutionary optimization, because its ultimate aim is to find one optimal point not a scatter of the samples.

Thus, we infer that the CM-MEDA can improve the convergence of the EDA by making distribution estimation on the set of axes which maximize the variance of the samples from the viewpoint of PCA. Similar work may also refer to [15,16,17].

According to the framework above, we can find that the CM-MEDA has only three more steps than the MEDA: calculation of covariance matrix, calculation of eigenvectors, and transformation. The calculation of covariance matrix takes $O\left(n_{\text {best }} \cdot l^{2}\right)$, where $n_{\text {best }}$ is the number of selected samples, and $l$ is the dimension of the samples. The eigenvectors can be efficiently calculated in $O\left(l^{3}\right)$. And the transformation takes $O\left(l^{2}\right)$. Therefore, it is clear that the CM-MEDA is much faster than the HEDA based on PGM, even the dHEDA. (Recall that it takes $O\left(n_{\text {best }}{ }^{2} \cdot l^{2}\right)$ to calculate K-L divergence in the dHEDA.)

However, we also note that the CM-MEDA can only accurately capture the linear linkages; while the non-linear linkages are always approximated intrinsically. In contrast, the HEDA based on PGM is able to capture more complex relations among variables if less restrictions on its PDS.

# 4.5 Experimental Results 

We provide a brief experiment to compare the CM-MEDA and MEDA in histogram case on 4 continuous optimization problems.

The general settings of the two algorithms are same: the population size is 1000; $20 \%$ of the individuals are selected from the population to estimate the model; the number of the bins in each bin is arbitrarily set to be 100; 40 iterations are run each time. The MEDA use the mechanism of the sur-shr-HEDA to update the histogram model. The surrounding factor is set to be $10 \%$, and the mutation rate is set to be $5 \%$.

The 4 test functions: Fun-1, Fun-2, Schwefel, Rosenbrock are all non-separable and share a similar formulation. The reason that we choose several functions in this

Table 4. Problem Descriptions
Table 5. Experimental Results

formulation is because this formulation of functions is usually hard for Evolutionary Algorithms to solve because of their strong linkages between variables. The problem descriptions are listed in Table 4.

Each of the algorithms is run for 20 times in each problem, and the mean value, the best case, and the standard deviation for the 20 runs are collected in Table 5.

The results in Table 5 verify the superiority of the CM-MEDA in histogram case in those non-separable cases. For example, when solving Schwefel function, the best solution obtained by the CM-MEDA in 20 runs is $1.320 \mathrm{e}-10$, while the best solution of the MEDA is 0.0378 ; the mean value of the CM-MEDA is 0.0015 , while the mean value of the MEDA is 0.0682 .

# 5 Summary and Further Work 

In this chapter, we have reviewed the two methods in HEDA which are able to detect linkage among variables in the optimization problems. Using probabilistic graphical model generally represents the relations more accurately but also is of high-cost; while using space transformation is quite fast, but it only roughly represents the major possible relationships.

There is, however, still much further work in both topics.
The first, for the HEDA, the number of bins in certain problems is always decided arbitrarily in most papers. An alternative method might apply the prior on the bins, such as Dirichlet Process, and then use Bayesian analysis in estimating the model.

The second, for the HEDA based on PGM, it is still interesting to have deeper research on dealing with the case of small number of samples with great number of bins in a joint probability.

The third, for the HEDA based on space transformation, to find a more efficient transformation, or to define the kernel space might allow the algorithm to capture more complex and non-linear linkages.

The fourth, there is little research on comparing the two method above directly. Besides, the attempts to combine the above two methods might have even improved performance, since the space transformation might reduce the number of parents of each nodes in the graphical model.
