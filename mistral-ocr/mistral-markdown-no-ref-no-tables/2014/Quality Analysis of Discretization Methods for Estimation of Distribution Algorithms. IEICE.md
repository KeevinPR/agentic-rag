# Quality Analysis of Discretization Methods for Estimation of Distribution Algorithms 

Chao-Hong CHEN ${ }^{\mathrm{Ta} 1}$, Nonmember and Ying-ping CHEN ${ }^{\mathrm{Tb}}$, Member


#### Abstract

SUMMARY Estimation of distribution algorithms (EDAs), since they were introduced, have been successfully used to solve discrete optimization problems and hence proven to be an effective methodology for discrete optimization. To enhance the applicability of EDAs, researchers started to integrate EDAs with discretization methods such that the EDAs designed for discrete variables can be made capable of solving continuous optimization problems. In order to further our understandings of the collaboration between EDAs and discretization methods, in this paper, we propose a quality measure of discretization methods for EDAs. We then utilize the proposed quality measure to analyze three discretization methods: fixed-width histogram (FWH), fixed-height histogram (FHH), and greedy random split (GRS). Analytical measurements are obtained for FHH and FWH, and sampling measurements are conducted for FHH, FWH, and GRS. Furthermore, we integrate Bayesian optimization algorithm (BOA), a representative EDA, with the three discretization methods to conduct experiments and to observe the performance difference. A good agreement is reached between the discretization quality measurements and the numerical optimization results. The empirical results show that the proposed quality measure can be considered as an indicator of the suitability for a discretization method to work with EDAs.


key words: quality analysis, discretization distortion, fixed-width histogram, fixed-height histogram, greedy random split, estimation of distribution algorithm, Bayesian optimization algorithm

## 1. Introduction

Genetic algorithms (GAs) [11], [15] are methodologies inspired by Darwinian evolution and widely applied to realworld problems. In genetic algorithms, good individuals are selected from the current population to generate the next population by using recombination and mutation operators, mimicking the biological genetic operations. According to the theory of design decomposition [12], the key components to the GA success include identifying, reproducing, and exchanging the structure of the solutions. Recombination, one of the main GA operator, mixes the promising subsolutions, called building blocks ( BBs ), and creates the solutions. Because the recombination operator mixes promising sub-solutions and creates new solutions, genetic algorithms work well on the problems which can be implicitly or explicitly decomposed into sub-problems.

In order to appropriately mix genes, the evolutionary algorithms based on utilizing probabilistic models were proposed and developed [19], [26]. In these schemes, instead of

[^0]using regular recombination and mutation operators, the offspring population is created according to the estimated probabilistic model of the selected individuals of the current population. The probabilistic model is expected to reflect the problem structure, and better performance can be achieved via exploring the relationship between genes. These evolutionary algorithms are called estimation of distribution algorithms (EDAs). In EDAs, decision variables are often coded with discrete codes, such as binary codes. To enhance the applicability of EDAs over continuous domains, direct attempts to modify the type of decision variables have been made, including continuous population-based incremental learning with Gaussian distribution [31], real-coded variant of population-based incremental learning with interval updating [32], Bayesian evolutionary algorithms for continuous function optimization [33], real-coded extended compact genetic algorithm based on mixtures of models [18], and the real-coded Bayesian optimization algorithm [1].

Instead of modifying the infrastructure of the algorithm, such as the type of decision variables or the global program flow, as a more general, component-wise approach, discretization methods are employed to cooperate with EDAs [6], [7], [28], [35]. Discretization methods enable EDAs designed for discrete variables to solve continuous optimization problems without the need of altering algorithmic structures. For further information about these two approaches which enable EDAs to handle continuous variables, the reader may refer to [4], [5], [16]. In order to further our understandings of the collaboration between EDAs and discretization methods, as the first step, we wish to quantify the discretization quality and identify the suitability of discretization methods to work with EDAs. Particularly, in this paper, we firstly propose a quality measure of discretization methods and then utilize the proposed quality measure to analyze three discretization methods, fixedwidth histogram (FWH), fixed-height histogram (FHH), and greedy random split (GRS). To observe the performance difference of these discretization methods in action, we integrate Bayesian optimization algorithm (BOA) [27] with the three methods to conduct numerical experiments. A good agreement between the measurements of discretization quality and the numerical results on test functions is obtained. Such an outcome indicates that the proposed quality measure indeed reflects the suitability for a discretization method to work with EDAs.

In the next section, we give a background of this study, including the introduction of EDAs and the three aforemen-


[^0]:    Manuscript received August 27, 2013.
    Manuscript revised December 21, 2013.
    ${ }^{1}$ The authors are with the Department of Computer Science, National Chiao Tung University, Hsinchu, Taiwan.
    a) E-mail: chchen@nclab.tw
    b) E-mail: ypchen@nclab.tw

    DOI: 10.1587/transinf.E97.D.1312

tioned discretization methods. Section 3 proposes the quality measure of discretization methods and analyzes the three methods by using the proposed measure. The numerical experiments of the three methods integrated with BOA on test functions are presented and discussed in Sect. 4, followed by the summary and conclusions in Sect. 5.

## 2. Background

In this section, we will give an overview of estimation of distribution algorithms. Then, three discretization methods, fixed-width histogram, fixed-height histogram, and greedy random split, are described.

### 2.1 Estimation of Distribution Algorithms

Estimation of distribution algorithms (EDAs) [19], [20], [23], [26] solve problems by building probabilistic models on promising solutions and generating offspring of the next generation from the model. EDAs replace the regular genetic operators, such as crossover and mutation, with the construction and sampling of probabilistic models. In EDAs, at each generation, the selection operator selects good individuals from the current population, and a probabilistic model is constructed based on these selected individuals. Then, a new population is generated by sampling the built model. An EDA scheme can be algorithmically outlined as

1. Initialize a population randomly.
2. Apply the selection operator on the population.
3. Build a probabilistic model from the selected individuals.
4. Generate a new population by sampling the model.
5. Stop if the termination criterion is satisfied.
6. Return to step 2 .

According to [26], EDAs can be broadly categorized into three types. (1) No interaction: Each variable is modeled independently. These algorithms include the population-based incremental learning (PBIL) [2], the compact genetic algorithm (cGA) [14], and the univariate marginal distribution algorithm [23]. (2) Pairwise interaction: For these algorithms, pairwise interactions between variables are assumed, such as mutual-informationmaximizing input clustering (MIMIC) [9], Baluja's dependency tree approach [3], and the bivariate marginal distribution algorithm (BMDA) [29]. (3) Multivariate interaction: These algorithms adopt models that can explore multivariate interactions, such as the extended compact genetic algorithm (ECGA) [13], the Bayesian optimization algorithm (BOA) [25], the estimation of Bayesian network algorithm (EBNA) [10], the factorized distribution algorithm (FDA) [22], the learning version of FDA (LFDA) [21] and the incremental Bayesian optimization algorithm (iBOA) [30]. With learning the dependencies among variables, the algorithms in this category can achieve better performance in certain sets of problems.

### 2.2 Discretization Methods

Discretization methods can be utilized to transform optimization problems from the continuous domain into the discrete domain and to provide an interface between problems and solvers in different domains. After being discretized, solution individuals in the continuous domain are encoded with certain discrete codes, such as binary strings or integer vectors. Then, EDAs originally designed for handling discrete decision variables can optimize transformed continuous problems. In this study, we consider only the discretization methods which divide the search space into intervals. The probability of search points in each interval are assumed to be uniformly distributed. A scheme to integrate discretization into EDAs can be outlined as

1. Initialize a population randomly.
2. Conduct discretization to encode the population.
3. Apply the selection operator on the population.
4. Build a probabilistic model from the selected individuals.
5. Generate a new population by sampling the model.
6. Sample the coded intervals to create the continuous offspring.
7. Stop if the termination criterion is satisfied.
8. Return to step 2 .

In the remainder of this section, we will introduce two elementary discretization methods, fixed-width histogram (FWH) and fixed-height histogram (FHH) [17], [35], and a simple randomized discretization method, greedy random split (GRS).

### 2.2.1 Fixed-Width Histogram

In fixed-width histogram, each dimension is divided into several equal-width intervals, which are usually called bins. Each bin is assigned a discrete code or an integer. Each realvalued individual is coded with the code or integer assigned to the bin. If the search space for a dimension is $[L, U)$, a $k$-bin FWH will divide this interval into $k$ bins with equalwidth, $(U-L) / k$, and the range of the $i$ th bin is

$$
\left[L+\frac{(i-1)(U-L)}{k}, L+\frac{i(U-L)}{k}\right)
$$

for $i=1, \ldots, k$. Figure 1 shows three different variables discretized by a 5 -bin FWH. The fixed width of each bin is 40 .

### 2.2.2 Fixed-Height Histogram

Fixed-height histogram is similar to FWH, but instead of fixing the bin size, the "height" of each bin is fixed, i.e., each bin contains the same number of search points. If the points are concentrated in some regions, there will be more bins in these regions to equalize the number of search points. Figure 2 shows three different variables discretized by a 5-

```
procedure GRS([\ell, u),C)
    max-heap INTERVAL-HEAP
    \(N \leftarrow\) population size
    INTERVAL-HEAP.insert([\ell, u), N)
        while INTERVAL-HEAP.size() \(<C\) do
            \(\left(\left[\ell^{\prime}, u^{\prime}\right), N^{\prime}\right) \leftarrow\) INTERVAL-HEAP.pop()
            \(m \leftarrow \operatorname{random}\left[\ell^{\prime}, u^{\prime}\right)\)
            \(N_{\ell^{\prime}} \leftarrow\) number of individuals in \(\left[\ell^{\prime}, m\right)\)
            \(N_{u^{\prime}} \leftarrow\) number of individuals in \(\left[m, u^{\prime}\right)\)
            INTERVAL-HEAP.insert \(\left(\left[\ell^{\prime}, m\right), N_{\ell^{\prime}}\right)\)
            INTERVAL-HEAP.insert \(\left(\left[m, u^{\prime}\right), N_{u^{\prime}}\right)\)
        end while
        return INTERVAL-HEAP
```

14: end procedure
$\triangleright$ Split interval $[\ell, u)$ into $C$ interval
$\triangleright$ Create an empty max-heap [8]
$\triangleright$ Insert the whole search region with key $N$
$\triangleright$ Obtain the interval which contains most individuals
$\triangleright$ Randomly determine the split point

Fig. 3 Pseudo code for greedy random split.
![img-0.jpeg](img-0.jpeg)
![img-1.jpeg](img-1.jpeg)
![img-2.jpeg](img-2.jpeg)
(a) Population \#1: 5-bin FHH.
![img-3.jpeg](img-3.jpeg)

Fig. 2 Three variables discretized by a 5 -bin FHH.
bin FHH. The fixed height of each bin is 2 .

### 2.2.3 Greedy Random Split

Greedy random split (GRS) is a simple randomized discretization method, of which the main idea is to always randomly split the interval which contains most samples. To implement GRS, we use a heap [8] to store intervals and using the number of individual which is in that interval as key. Thus, we can obtain the interval which contains most samples quickly and then split that interval into two at random. We continue the split step until the demanded number of in-
tervals is reached. The pseudo code of GRS is shown in Fig. 3.

## 3. Quality of Discretization Methods

In this section, we propose a quality measure of discretization methods and use the proposed measure to analyze the quality of fixed-width histogram, fixed-height histogram, and greedy random split. To the best of our limited knowledge, there is no other similar measure for quantitatively evaluating the quality of discretization methods working with EDAs. Hence, this study can be considered as a start of this line of research, which is definitely worth pursuing.

### 3.1 Quantitative Evaluation

Because EDAs build probabilistic models based on the selected individuals and discretization methods transform continuous individuals into discrete ones, if a discretization method introduces a lot of distortion into the original population, the probabilistic model built on such a distorted population must be inappropriate for the purpose of model building, and the performance of the whole integrated optimization framework should be greatly reduced. According to this point of view, we propose the use of distortion distance between the original population and the discretized population to quantitatively evaluate the quality of discretization methods. The distortion distance is formulated as

$$
\int_{L}^{U}\left|p(x)-p^{*}(x)\right| d x
$$

where $L$ and $U$ are the lower bound and the upper bound of a search interval, $p^{*}(x)$ is the probability density function of the original population distribution, and $p(x)$ is the probability density function of the population distribution discretized by the discretization method to be evaluated. The range of distortion distance calculated with Eq. (1) is interval $[0,2]$. Distortion distance 0 means the two population distributions are identical, and distortion distance 2 means the two population distributions are disjoint.

We use the defined distortion distance to measure the

distortion caused by discretization. Smaller distortion distance means less distortion is introduced to the population. Thus, the resultant (discrete) population should be more similar to the original (continuous) one. According to the scheme of integrating discretization methods into EDAs, if the input for an EDA, i.e., the discrete population, is similar to the original, continuous one, the EDA should be able to accomplish its task. Otherwise, the employed EDA might not be able to handle the problem due to the distortion introduced by discretization. Hence, Eq. (1) is utilized to quantitatively measure the quality of discretization methods.

### 3.2 Quality Analysis of Fixed-Width Histogram

With the proposed quality measure, we firstly analyze the discretization quality of fixed-width histogram in this section. We will analytically derive the quality of FWH and confirm the derived quality measurement with numerical experiments. Let $N\left(0, \sigma^{2}\right)$ be Gaussian distribution with variance $\sigma^{2}, \varphi_{0, \sigma^{2}}(x)$ be the probability density function, and $\Phi_{0, \sigma^{2}}(x)$ be the cumulative distribution function. For simplicity, we normalize $N\left(0, \sigma^{2}\right)$ into interval $[-10.0,10.0)$ to obtain a new distribution $N^{\prime}\left(0, \sigma^{2}\right)$. The new probability density function is

$$
\varphi_{0, \sigma^{2}}^{\prime}(x)=\frac{\varphi_{0, \sigma^{2}}(x)}{\Phi_{0, \sigma^{2}}(10.0)-\Phi_{0, \sigma^{2}}(-10.0)}
$$

and the new cumulative distribution function is

$$
\Phi_{0, \sigma^{2}}^{\prime}(x)=\frac{\Phi_{0, \sigma^{2}}(x)}{\Phi_{0, \sigma^{2}}(10.0)-\Phi_{0, \sigma^{2}}(-10.0)}
$$

We will use the distribution $N^{\prime}\left(0, \sigma^{2}\right)$ to model the original, continuous population distribution and examine the quality of discretization methods. The different values of the standard deviation $\sigma$, as shown in Fig. 4, are used to model the level of population convergence. Large values of $\sigma$ are considered as the initial population distribution, in which the individuals are uniformly generated, and small values of $\sigma$ are considered as the distribution of the population which converges, in which almost all the individuals are close to each other.
![img-4.jpeg](img-4.jpeg)

Fig. 4 The probability density function $\varphi_{0, \sigma^{2}}^{\prime}(x)$ with $\sigma=10,5$, and 1 .

### 3.2.1 Analytical Quality Measurement

Firstly, we begin with obtaining the analytical distortion distance of FWH with bin size $K$, which is assumed to be even without loss of generality, when a population modeled with $N^{\prime}\left(0, \sigma^{2}\right)$ is discretized by FWH. After discretization, the population distribution created by FWH has $K$ intervals, $I_{1}, I_{2}, \cdots, I_{K}$. The interval corresponds to the $i$ th bin is $I_{i}=\left[I_{i}, u_{i}\right)$, where

$$
l_{i}=-10.0+\frac{20.0 \times(i-1)}{K}
$$

and

$$
u_{i}=-10.0+\frac{20.0 \times i}{K}
$$

Since the probability is uniform within each interval, the density of the $i$ th bin is $d_{i}$, where

$$
\begin{aligned}
d_{i} & =\frac{\Phi_{0, \sigma^{2}}^{\prime}\left(u_{i}\right)-\Phi_{0, \sigma^{2}}^{\prime}\left(l_{i}\right)}{u_{i}-l_{i}} \\
& =\frac{\Phi_{0, \sigma^{2}}^{\prime}\left(u_{i}\right)-\Phi_{0, \sigma^{2}}^{\prime}\left(l_{i}\right)}{\frac{20.0}{K}} \\
& =\frac{K\left(\Phi_{0, \sigma^{2}}^{\prime}\left(u_{i}\right)-\Phi_{0, \sigma^{2}}^{\prime}\left(l_{i}\right)\right)}{20.0}
\end{aligned}
$$

Because $N^{\prime}\left(0, \sigma^{2}\right)$ is symmetric and $K$ is even, we know that in each interval $\varphi_{0, \sigma^{2}}^{\prime}(x)$ is monotonically increasing (or decreasing if $i>K / 2$.) Hence, the distortion distance can be obtained as

$$
\begin{aligned}
\sum_{i=1}^{K} & \left(\left|\left(m_{i}-l_{i}\right) d_{i}-\left(\Phi_{0, \sigma^{2}}^{\prime}\left(m_{i}\right)-\Phi_{0, \sigma^{2}}^{\prime}\left(l_{i}\right)\right)\right|\right. \\
& \left.+\left|\left(u_{i}-m_{i}\right) d_{i}-\left(\Phi_{0, \sigma^{2}}^{\prime}\left(h_{i}\right)-\Phi_{0, \sigma^{2}}^{\prime}\left(m_{i}\right)\right|\right)\right)
\end{aligned}
$$

where $m_{i}=\varphi_{0, \sigma^{2}}^{\prime-1}\left(d_{i}\right)$. Since there are two solutions of $\varphi_{0, \sigma^{2}}^{\prime-1}\left(d_{i}\right)$, we always take the one in $\left[I_{i}, u_{i}\right)$.

The distortion distance of FWH with 8, 16, and 32 bins are shown in Fig. 5. The $x$-axis represents the standard de-
![img-5.jpeg](img-5.jpeg)

Fig. 5 The distortion distance of FWH obtained analytically. The $x$-axis is the value of standard deviation, and the $y$-axis is the distortion distance.

viation varied from 10.0 to 0.1 to model the level of population convergence. From Fig. 5, we can observe that large bin sizes lead to small distortion distances, i.e., less distortion. Such a result agrees with our intuition. When the distribution is almost uniform, the resultant population distribution created by FWH has a very small distortion distance from the original population distribution. However, when the population converges, i.e., $\sigma \rightarrow 0$, the distortion distance of FWH becomes very large.

### 3.2.2 Empirical Quality Measurement

After deriving the analytical quality measurement of FWH, we use a series of numerical experiments to calculate the empirical quality measurements. The goal to obtain both the analytical and empirical quality measurements is two-fold: (1) We would like to confirm the results with approaches of totally different natures, because sometimes analytical results might not be computationally obtained. In order to ensure that the analytical quality measurement derived in this study can be practically realized, numerical sampling procedures should be employed to check if similar quality measurements can be calculated. (2) For advanced, complicated discretization methods, analytical quality measurements might not be easy to derive. In such cases, numerical sampling procedures can always be employed to calculate empirical quality measurements. After being confirmed in the cases of elementary discretization methods, the proposed quality measure may therefore be empirically obtained for advanced, complicated discretization methods.

Figure 6 shows the empirical quality measurements and compares the empirical results to the analytical results. In the series of experiments, different numbers of samples are generated from the distribution $N^{\prime}\left(0, \sigma^{2}\right)$, which models the population distribution, and taken as the input population of FWH. Numerical sampling procedures are used to calculate the distortion distance between $N^{\prime}\left(0, \sigma^{2}\right)$ and the distribution of the resultant population created by FWH. We examine the situations involving 1000, 10000, and 100000 samples with bin sizes 8,16 , and 32 . The standard deviation is varied from 10.0 to 0.1 with a step of 0.1 . For each experimental setting, we perform 50 independently runs and record the mean of calculated distortion distances. As we can observe in Figs. 6 (a) (8 bins), 6 (b) (16 bins), and 6 (c) (32 bins), if the number of samples is sufficiently large, the empirical and analytical results are in a very good agreement.

### 3.3 Quality Analysis of Fixed-Height Histogram

In this section, the discretization quality of fixed-height histogram is analytically derived and empirically obtained as FWH was in the previous section.

### 3.3.1 Analytical Quality Measurement

Firstly, we will derive an equation of distortion distance of
![img-6.jpeg](img-6.jpeg)

Fig. 6 The empirical quality measurements obtained with 1000, 10000, and 100000 samples and the analytical quality measurement of FWH.

FHH with bin size $K$, which is assumed to be even without loss of generality. After discretization, the population distribution created by FHH has $K$ intervals $I_{1}, I_{2}, \cdots, I_{K}$. The interval that corresponds to the $i$ th bin is $I_{i}=\left[I_{i}, u_{i}\right)$, where

$$
I_{i}=\Phi_{0, \sigma^{2}}^{\prime-1}\left(\frac{i-1}{K}\right), \quad u_{i}=\Phi_{0, \sigma^{2}}^{\prime-1}\left(\frac{i}{K}\right)
$$

Since the probability is uniform within each interval, the density of the $i$ th bin is $d_{i}$, where

$$
d_{i}=\frac{\Phi_{0, \sigma^{2}}^{\prime}\left(u_{i}\right)-\Phi_{0, \sigma^{2}}^{\prime}\left(l_{i}\right)}{u_{i}-l_{i}}=\frac{\frac{i}{K}-\frac{i-1}{K}}{u_{i}-l_{i}}=\frac{1}{K\left(u_{i}-l_{i}\right)}
$$

Because $N^{\prime}\left(0, \sigma^{2}\right)$ is symmetric and $K$ is even, in each in-

![img-7.jpeg](img-7.jpeg)

Fig. 7 The distortion distance of FHH obtained analytically. The $x$-axis is the value of standard deviation, and the $y$-axis is the distortion distance.
terval $\varphi_{0, \sigma^{2}}^{t}(x)$ is monotonically increasing (or decreasing if $i>K / 2$ ). Hence, the distortion distance can be computed as

$$
\begin{aligned}
\sum_{i=1}^{K} & \left(\left|\left(m_{i}-l_{i}\right) d_{i}-\left(\Phi_{0, \sigma^{2}}^{t}\left(m_{i}\right)-\Phi_{0, \sigma^{2}}^{t}\left(l_{i}\right)\right)\right|\right. \\
& \left.+\left|\left(u_{i}-m_{i}\right) d_{i}-\left(\Phi_{0, \sigma^{2}}^{t}\left(h_{i}\right)-\Phi_{0, \sigma^{2}}^{t}\left(m_{i}\right)\right)\right|\right)
\end{aligned}
$$

where $m_{i}=\varphi_{0, \sigma^{2}}^{t-1}\left(d_{i}\right)$, and we also take $m_{i}$ as the one in $\left[l_{i}, u_{i}\right)$.

The distortion distance of FHH with bin size 8, 16, and 32 are shown in Fig. 7. The $x$-axis represents the standard deviation, modeling the level of population convergence, from 10 to 0.1 . Similar to the analytical result derived for FWH, large bin sizes lead to small distortion distances. However, unlike the result for FWH, when the standard deviation goes close to zero (i.e., the population converges), the distortion distance of FHH grows relatively slowly.

### 3.3.2 Empirical Quality Measurement

Empirical quality measurements are also obtained for FHH to confirm the consistence of the analytical and sampling approaches. As described in Sect. 3.2.2, the standard deviation is varied from 10.0 to 0.1 , and the number of samples are 1000, 10000, and 100000. For each experimental setting, 50 independent runs are performed, and the mean of calculated distortion distances is recorded. The results are shown in Figs. 8 (a) (8 bins), 8 (b) (16 bins), and 8 (c) (32 bins), respectively. If the number of samples is sufficiently large, the empirical and analytical results are also in a very good agreement as we observed on FWH.

### 3.4 Quality Analysis of Greedy Random Split

After evaluating the discretization quality of FWH and FHH, we will analyze the discretization quality of greedy random split. The original population distribution is still modeled with $N^{\prime}\left(0, \sigma^{2}\right)$ which is defined and described in Sect.3.2. Because of the complexity of deriving the analytical quality measurement for GRS and the confirmed con-
![img-8.jpeg](img-8.jpeg)

Fig. 8 The empirical quality measurements obtained with 1000, 10000, and 100000 samples and the analytical quality measurement of FHH.
sistence of the analytical and empirical results, we only obtain the empirical quality measurements with similar experiments used in Sects. 3.2.2 and 3.3.2. The standard deviation is varied from 10 to 0.1 , the number of samples are 1000, 10000, and 100000, and each experiment is repeated independently for 50 runs. The empirical quality measures for 8,16 , and 32 bins are shown in Fig. 9.

### 3.5 Discretization Quality Comparison: FWH, FHH, and GRS

According to the quality measurements obtained in previous

![img-9.jpeg](img-9.jpeg)

Fig. 9 The empirical quality measurements obtained with 1000, 10000, and 100000 samples of GRS.
sections, we compare the discretization quality of the three discretization methods: FWH, FHH, and GRS. For simplicity and easiness to observe, we adopt the analytical quality measurements for FWH and FHH and the empirical quality measurements obtained with 100000 samples for GRS. The quality comparison is shown in Fig. 10. More specifically, Figs. 10 (a), 10 (b), and 10 (c) show the distortion distance of FWH, FHH, and GRS with bin sizes 8,16 , and 32 , respectively.

In Fig. 10, we can observe that when the standard deviation is large, the distortion distance of FWH is the smallest for the three tested bin sizes, but when the standard devi-
![img-10.jpeg](img-10.jpeg)

Fig. 10 The discretization quality comparison of FWH, FHH, and GRS.
ation decreases (i.e., the population converges,) the distortion distance of FWH becomes the largest in the three methods. For small bin sizes, FHH has the smallest distortion when the standard deviation is small, and when the bin size increased GRS became better than FHH. This comparison suggests that for 8 bins FHH provides the best quality, for 16 bins GRS is slightly better than FHH, and for 32 bins GRS provides the best quality. We will take one step further to examine the three methods working with two different EDAs on benchmark functions in Sect. 4 to reveal the relationship between the proposed quality measure, i.e., the distortion distance, and the performance of EDAs integrated with these discretization methods.

## 4. Working with EDAs

In this section, we respectively integrate the three investigated discretization methods, FWH, FHH, and GRS with BOA, a representative EDA. We will conduct numerical experiments on test functions to check if the performance benchmarks match the quality measurements. The influence of the adopted discretization methods and the relationship between the proposed quality measure and the performance of different integrations will also be discussed.

### 4.1 BOA Integrated with Discretization

Bayesian optimization algorithm (BOA) is proposed by [25]. In BOA, a Bayesian network is built from the selected individuals and used to generate offspring. In this study, we use BOA with decision graphs [24], [27]. For more details on BOA, please refer to [25], [27]. BOA can be algorithmically outlined as

1. $t \leftarrow 0$, randomly generate initial population $P(0)$
2. Select a set of promising individuals $S(t)$ from $P(t)$
3. Construct network $B$ with a chosen metric and constraints
4. Generate a set of new individuals $O(t)$ according to the joint distribution encoded by $B$
5. Create a new population $P(t+1)$ by replacing some individuals from $P(t)$ with $O(t), t \leftarrow t+1$
6. If the termination criterion is not met, go to step 2

After integrated with discretization, the flow becomes

1. $t \leftarrow 0$, randomly generate initial population $P(0)$
2. Conduct discretization to encode each variable of the population.
3. Select a set of promising individuals $S(t)$ from $P(t)$
4. Construct network $B$ with a chosen metric and constraints
5. Generate a set of new individuals $O(t)$ according to the joint distribution encoded by $B$
6. Sample the coded intervals to generate the realvalued individuals in $O(t)$.
7. Create a new population $P(t+1)$ by replacing some individuals from $P(t)$ with $O(t), t \leftarrow t+1$
8. If the termination criterion is not met, go to step 2

### 4.2 Numerical Experiments

We adopt the CEC 2005 benchmark functions [34] to observe the performance difference of BOA integrated with the three discretization methods. The benchmark suite is described briefly in Appendix. For more details, please refer to the original document [34]. The number of dimensions of the benchmark functions is set to 10 to examine FWH, FHH, and GRS with bin sizes 8,16 , and 32 , i.e., the discretized problems are 30,40 , and 50 bits.

The parameters of BOA are given in the following.

Population size $=400$, offspring percentage $=50$, tournament size $=8$, maximum function evaluations $=30000$, and 30 independent runs for each function. The results of BOA are given in Table 1 for each bin size.

In the table, the results of the discretization method that achieves the best performance in each benchmark function are bold-faced, and t-tests are conducted on these results. The results of the other two discretization methods are tested against the best one and are marked by $\times$ if outperformed by the best one with a confidence level at least $95 \%$.

### 4.3 Discussion

According to the experimental results presented in Table 1. BOA with FHH has the best performance when 8 bins are used to encode each variable (outperforming the other two methods on 13 out of 25 functions.) When the bin size increases, the performance of BOA with GRS becomes better compared to the other two methods (outperforming the other two methods on 16 out of 25 functions with 16 bins and on 18 out of 25 functions with 32 bins.)

From Fig. 10 and the discussion in Sect. 3.5, we know that FHH provides the best discretization quality when 8 bins are used. When bin size increases, GRS provides better discretization quality compared to the other two methods. The numerical results of BOA well agree with our discretization quality measure. Given the observed results, we may conclude that there exists a connection between the quality of discretization methods and the performance of EDAs integrated with discretization as well as that the proposed quality measure can reveal such a property and quantitatively assess the discretization methods.

## 5. Summary and Conclusions

In this paper, we proposed a quality measure of discretization methods. Then, we utilized the proposed quality measure to analyze fixed-width histogram (FWH), fixed-height histogram (FHH), and greedy random split (GRS). Analytical measurements were derived for FWH and FHH, and empirical measurements were obtained for FWH, FHH, and GRS. We compared the three methods with three settings ( 8 , 16 , and 32 bins).

In order to study the connection between the quality measure and the performance of EDAs integrated with discretization, we integrated BOA with FWH, FHH, and GRS, respectively, to conduct numerical experiments on test functions. A good agreement between the discretization quality measurements and the numerical optimization results was obtained. As a consequence, this study suggests that there exists a connection between the quality of discretization and the performance of EDAs integrated with discretization as well as that the proposed quality measure provides a quantitative assessment on the suitability for a discretization method to work with EDAs.

The future work along this line includes the use of the proposed quality measure to analyze more discretiza-

Table 1 The numerical results of BOA integrated with FWH, FHH, and GRS ( 8 bins, 16 bins, and 32 bins).

tion methods. Since it has been verified in this study that based on the proposed quality measure, the analytical measurement and the empirical measurement are consistent, for complicated discretization methods, numerical sampling techniques can be adopted to evaluate the discretization quality. Moreover, how to set the bin size should also be carefully studied, since a larger bin size means a larger discretized problem for EDAs. A large bin size, e.g., close to the population size, may greatly influence the algorithmic performance. The resultant probabilistic model will most likely overfit, and hence, a proper ratio should be maintained between the adopted bin size and the population size. Finally, the connection between the discretization quality and the optimization performance should be further investigated. Essential insights and important understandings of the EDA working principles might be revealed.

## Acknowledgments

The work was supported in part by the National Science Council of Taiwan under Grant NSC 101-2628-E-009-024MY3. The authors are grateful to the National Center for High-performance Computing for computer time and facilities.

## Appendix: CEC 2005 Real-Parameter Optimization Benchmark Suite

The benchmark consists of 5 unimodal functions, 9 multimodal functions, and 11 composition functions. Because the last 13 functions are composed by the first 12 functions, we briefly describe the first 12 functions. For more details, including all the predefined values, please refer to the original document [34]. In the following definition, $D$ denotes the number of dimension. $x=\left[x_{1}, x_{2}, \ldots, x_{D}\right]$ is the input, a $D$-dimensional vector. $N(0,1)$ is a random sample from the normal distribution with mean 0 and variance 1 to create noise. $M_{i}$ is a predefined linear transform matrix. $o_{1}=\left[o_{1}, o_{2}, \ldots, o_{D}\right]$ is a predefined shift vector, and $f \_b i a s_{i}$ is a predefined bias.

$$
\begin{aligned}
& F_{1}(x)=\sum_{i=1}^{D} z_{i}^{2}+f \_b i a s_{1}, z=x-o_{1} \\
& F_{2}(x)=\sum_{i=1}^{D}\left(\sum_{j=1}^{i} z_{j}\right)^{2}+f \_b i a s_{2}, z=x-o_{2} \\
& F_{3}(x)=\sum_{i=1}^{D}\left(10^{6}\right)^{\frac{i-1}{D-1}} z_{i}^{2}+f \_b i a s_{3}, z=x-o_{3} \\
& F_{4}(x)=\left(\sum_{i=1}^{D}\left(\sum_{j=1}^{i} z_{j}\right)^{2}\right) \times(1+0.4|N(0,1)|) \\
& \quad+f \_b i a s_{4} \\
& \quad z=x-o_{4} \\
& F_{5}(x)=\max \left\{A_{i} x-B_{i}\right\}+f \_b i a s_{5} \\
& A, \text { a } D \times D \text { matrix, and } B \text {, a } D \times 1 \text { vector, } \\
& \text { are predefined. }
\end{aligned}
$$

$$
\begin{aligned}
& F_{6}(x)=\sum_{i=1}^{D-1}\left(100\left(z_{i}^{2}-z_{i+1}\right)^{2}+\left(z_{i}-1\right)^{2}\right) \\
& +f \_b i a s_{6} \\
& z=x-o_{6}+1 \\
& F_{7}(x)=\sum_{i=1}^{D} \cdot \frac{z_{i}^{2}}{4000}-\prod_{i=1}^{D} \cos \left(\frac{z_{i}}{\sqrt{i}}\right)+1+f \_b i a s_{7} \\
& z=\left(x-o_{7}\right) \times M_{7} \\
& F_{8}(x)=-20 \exp \left(-0.2 \sqrt{\frac{1}{D} \sum_{i=1}^{D} z_{i}^{2}}\right) \\
& -\exp \left(\frac{1}{D} \sum_{i=1}^{D} \cos \left(2 \pi z_{i}\right)\right) \\
& +20+e+f \_b i a s_{8}, z=\left(x-o_{8}\right) \times M_{8} \\
& F_{9}(x)=\sum_{i=1}^{D}\left(z_{i}^{2}-10 \cos \left(2 \pi z_{i}\right)+10\right)+f \_b i a s_{9} \\
& z=x-o_{9} \\
& F_{10}(x)=\sum_{i=1}^{D}\left(z_{i}^{2}-10 \cos \left(2 \pi z_{i}\right)+10\right)+f \_b i a s_{10} \\
& z=\left(x-o_{10}\right) \times M_{10} \\
& F_{11}(x)=\sum_{i=1}^{D}\left(\sum_{k=0}^{k m a x}\left(a^{k} \cos \left(2 \pi b^{k}\left(z_{i}+0.5\right)\right)\right)\right) \\
& -D \sum_{k=0}^{k m a x}\left(a^{k} \cos \left(2 \pi b^{k} \cdot 0.5\right)\right)+f \_b i a s_{11} \\
& z=\left(x-o_{11}\right) \times M_{11}, a=0.5, b=3, k m a x=20 \\
& F_{12}(x)=\sum_{i=1}^{D}\left(A_{i}-B_{i}(x)\right)^{2}+f \_b i a s_{12} \\
& z=x-o_{12}
\end{aligned}
$$

$A$ and $B$ are predefined $D \times D$ matrixes
![img-11.jpeg](img-11.jpeg)

Chao-Hong Chen received the B.S. and the M.S. degree in Department of Computer Science from National Chiao Tung University, Taiwan, in 2007 and 2009, and currently studies for the Ph.D. degree in Computer Science at National Chiao Tung University, Taiwan.

![img-12.jpeg](img-12.jpeg)

Ying-ping Chen is currently an Associate Professor in the Department of Computer Science, National Chiao Tung University, Taiwan. His research interests include data grid and MapReduce technologies in distributed computation as well as theories, working principles, and dimensional/facet-wise models in genetic and evolutionary computation. He received the B.S. degree and the M.S. degree in Computer Science and Information Engineering from National Taiwan University, Taiwan, in 1995 and 1997, respectively, and the Ph.D. degree in 2004 from the Department of Computer Science, University of Illinois at Urbana-Champaign, Illinois, USA.