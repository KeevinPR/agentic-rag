# Clustering and Learning Gaussian Distribution for Continuous Optimization 

Qiang Lu and Xin Yao, Fellow, IEEE


#### Abstract

Since the Estimation of Distribution Algorithm (EDA) was introduced, different approaches in continuous domains have been developed. Initially, the single Gaussian distribution was broadly used when building the probabilistic models, which would normally mislead the search when dealing with multimodal functions. Some researchers later constructed EDAs that take advantage of mixture probability distributions by using clustering techniques. But their algorithms all need prior knowledge before applying clustering, which is unreasonable in real life. In this paper, two new EDAs for continuous optimization are proposed, both of which incorporate clustering techniques into estimation process to break the single Gaussian distribution assumption. The new algorithms, Clustering and Estimation of Gaussian Network Algorithm based on BGe metric and Clustering and Estimation of Gaussian Distribution Algorithm, not only show great advantage in optimizing multimodal functions with a few local optima, but also overcome the restriction of demanding prior knowledge before clustering by using a very reliable clustering technique, Rival Penalized Competitive Learning. This is the first time that EDAs have the ability to detect the number of global optima automatically. A set of experiments have been implemented to evaluate the performance of new algorithms. Besides the improvement over some multimodal functions, according to the No Free Lunch theory, their weak side is also showed.


Index Terms—Clustering, estimation of distribution algorithm, Gaussian distribution.

## I. INTRODUCTION

ESTIMATION OF Distribution Algorithms (EDAs) are population based search algorithms that generate new population from the estimated distribution based on current promising solutions. Compared with the other evolutionary algorithms (e.g., GA), the crucial change is that both crossover and mutation operators are substituted by the estimation process. The effectiveness of EDAs have been evaluated by many works, both in combinatorial optimization [1]-[8] and in continuous optimization [9]-[15]. Basically, continuous optimization by EDAs can be summarized into the following framework.

1) Initialize a population of $N$ individuals randomly $\rightarrow D_{0}$.
2) Select $\mathrm{Se} \leq N$ individuals from $D_{t-1}(t=1,2, \ldots)$ according to a selection method $\rightarrow D_{t-1}^{\mathrm{Se}}$.
3) Estimate $n$-dimensional probability density function (pdf) based on $D_{t-1}^{\mathrm{Se}} \rightarrow p_{t}(\vec{x})=p\left(\vec{x} \mid D_{t-1}^{\mathrm{Se}}\right)$.

[^0]4) Sample $N$ new individuals from $p_{t}(\vec{x})$, form new population by partially or fully replacing the current population $\rightarrow D_{t}$.
5) Stop if some stopping criterion is reached, go to step 2 otherwise.
Early EDAs for continuous optimization presumed that selected vector is a random sample from a single Gaussian distribution. This assumption makes these algorithms unsuccessful when dealing with multimodal problems. For a multimodal function, the promising solutions selected by some fitness based selection scheme normally tend to form several groups, and each group encompasses one of the local optima. Under this condition, the estimated distribution-according to this single Gaussian distribution assumption-will be far from the real one. Thus, new populations generated based on this wrong estimation would be likely to be in the wrong search area, and either resulting in a slow convergence or more seriously misleading the search to a local optimum other than the global optimum. Some researchers have noticed this problem and constructed several EDAs using Gaussian mixture distributions [16]-[19] by incorporating clustering techniques.

Two new EDAs, taking advantage of data clustering techniques to break the single Gaussian distribution assumption, are proposed in this paper. Unlike previous EDAs that also use mixture distributions, the clustering approaches used in the proposed EDAs do not need prior knowledge to work. Both algorithms are evaluated on a set of selected functions for performance assessment. The results show that they can perform very well when dealing with multimodal functions that do not contain too many local optima. And on the other hand, due to the use of a Rival Penalized Competitive Learning (RPCL) clustering technique [20], [21], for the first time EDAs have the ability to detect the number of global optima automatically. According to the No Free Lunch theory [22], the weakness of the new algorithms are also analyzed. The new algorithms are denoted as "Clustering and Estimation of Gaussian Network Algorithm based on BGe metric" $\left(\mathrm{CEGNA}_{\mathrm{BGe}}\right)$ and "Clustering and Estimation of Gaussian Distribution Algorithm" (CEGDA) respectively in this paper.

The rest of this paper is organized as follows. Section II gives a brief review of EDAs for continuous optimization, and illustrates why clustering is needed and how it can be used to break the single Gaussian distribution assumption. Section III introduces RPCL and shows its automatic number selection ability by comparing with another clustering approach, k-Means. Section IV presents two new EDAs: $\mathrm{CEGNA}_{\mathrm{BGe}}$ and CEGDA. Section V presents the experimental results on a set of functions to assess the performance of the proposed EDAs. Section VI gives the final conclusion and discusses the topics for future research.


[^0]:    Manuscript received August 31, 2003; revised February 29, 2004 and April 21, 2004. This paper was recommended by Guest Editor Y. Jin
    The authors are with the School of Computer Science,University of Birmingham, Birmingham B15 2TT, U.K. (e-mail: Q.Lu@cs.bham.ac.uk; X.Yao@cs.bham.ac.uk). Digital Object Identifier 10.1109/TSMCC.2004.841914

## II. Breaking Single Gaussian Distribution ASSUMPTION BY CLUSTERING

The EDA was first introduced as an approach for combinatorial optimization with binary string representation. While not long after this new pattern was created, various EDAs for continuous optimization were constructed.

Based on the complexity of the probabilistic model used for learning the distribution of the selected individuals, EDAs can be categorized into four classes. Algorithms belonging to the first class assume that the variables are independent of each other and the joint probability density function for $n$-dimensional vector $\vec{x}=\left(x_{1}, \ldots, x_{n}\right)$ can be factorized according to $p(\vec{x})=\prod_{i=1}^{n} p\left(x_{i}\right)$, e.g., $\mathrm{PBIL}_{\mathrm{c}}[9], \mathrm{SHCLVND}[10], \mathrm{UMDA}_{\mathrm{c}}$ [13]; in class two, pairwise dependencies are considered, which means given a permutation $\pi=\left(i_{1}, \ldots, i_{n}\right)$, the joint density function can be represented as the product of one univariate density function and $n-1$ pairwise conditional density functions, denoted as $p(x)=p\left(x_{i_{1}}\right) \cdot p\left(x_{i_{2}} \mid x_{i_{1}}\right) \cdot \cdots \cdot p\left(x_{i_{n}} \mid x_{i_{n-1}}\right)$, such as $\operatorname{MMIC}_{\mathrm{c}}$ [13]; approaches of the third class take any multivariate interdependencies into account, the examples are $\mathrm{EGNA}_{\mathrm{DGe}}, \mathrm{EGNA}_{\mathrm{oc}}[12],[13]$ et al. EDAs of the last class use mixture distributions for conquering multimodal functions, like IDEA [19].

EDAs in the first three classes introduced above have a common feature, which is they all assume that the data used for estimation comes from one single Gaussian distribution. This simplification, on one hand, makes it easy to import some theories for building the model, but on the other hand, the drawback is obvious. If the distribution of those selected individuals is far from a single Gaussian distribution, the result of estimation will definitely mislead the search along a wrong direction.

The shape of a Gaussian distribution is like that of a sphere with the density increasing from the periphery to the core. Because multimodal functions have multiple local optima, intuitively the selected better fitness individuals will not just surround one position, but disperse to form several separated groups. So from this point of view, multimodal functions are the most probable unsuitable cases for single Gaussian distribution assumption.

A simple constructed bimodal function is used to illustrate this deduction. Considering minimizing the following function:

$$
F_{\text {Tost }}(\vec{x})= \begin{cases}\left(x_{1}-5\right)^{2}+\left(x_{2}+5\right)^{2} & x_{1} \geq 0 \\ \left(x_{1}+5\right)^{2}+\left(x_{2}-5\right)^{2} & x_{1}<0\end{cases}
$$

where $\vec{x}=\left(x_{1}, x_{2}\right)$. Apparently it has two local optima, $(5,-5)$ and $(-5,5)$, which are also the global minima. Selecting 1000 individuals from a randomly generated population in $[-10,10]$ (population size $=5000)^{1}$, and the distribution is shown in Fig. 1. There are two blocks of data, each of which surrounds one of the global minima. First, the estimation method in $\mathrm{UMDA}_{\mathrm{c}}$ [13] was used. It assumes that the distribution is a single Gaussian and the variables are independent of each other. Based on its estimation result, which

[^0]![img-0.jpeg](img-0.jpeg)

Fig. 1. Distribution of selected 1000 individuals based on the bimodal function (1).
![img-1.jpeg](img-1.jpeg)

Fig. 2. Distribution of generated 1000 individuals based on the estimation over data in Fig. 1 using $\mathrm{UMDA}_{\mathrm{c}}$.
is $\mathcal{N}\left((-0.097,-0.063),\left[\begin{array}{ll}5,28 & 0 \\ 0 & 5,30\end{array}\right]\right), 1000$ new individuals are generated by simulation, and the distribution is shown in Fig. 2. Obviously, the estimation is far from the real distribution of the data set.

From this simple case, it can be found that when optimizing multimodal problems, if the single Gaussian distribution assumption applies, the estimated distribution can be very poor. In order to overcome this deficiency, clustering techniques are incorporated.

Clustering was used with evolutionary algorithms and some particular EDA algorithms to alleviate the difficulty derived from the existence of symmetry structure in the work of Pelikan and Goldberg [17]. By clustering the selected individuals and processing each cluster separately, the presented approach successfully solves a list of combinatorial problems, e.g., two-max, graph bisection et al. Some other researchers also used clustering in their EDAs for continuous optimization to build mixture distributions.


[^0]:    ${ }^{1}$ The purpose of using this large population size is only for the clarity of illustration.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Distribution of selected 1000 individuals based on the bimodal function (1).
![img-3.jpeg](img-3.jpeg)

Fig. 4. Distribution of generated 1000 individuals based on the clustered estimation over data in Fig. 3 using $\mathrm{UMDA}_{c}$.

So, if we regard the individuals in Fig. 3 as two clusters, the estimated distribution for cluster $D_{1}$ is $\mathcal{N}\left((-5,04,4,99),\left[\begin{array}{lll}1.81 & 0 & \\ 0 & 1,78\end{array}\right]\right)$, and the distribution for cluster $D_{2}$ is $\mathcal{N}\left((4.87,-5.13),\left[\begin{array}{lll}1.83 & 0 & \\ 0 & 1,75\end{array}\right]\right)$. Then another 1000 individuals are generated and the distribution is illustrated in Fig. 4. The accuracy of the estimated distribution is greatly enhanced.

By using clustering the joint probability density function of the selected solutions is assumed to be a finite mixture of multivariate Gaussian density functions. That is

$$
p(\vec{x})=\sum_{i=1}^{k} \alpha_{i} p_{i}(\vec{x}), \quad \sum_{i=1}^{k} \alpha_{i}=1, \quad \alpha_{i} \geq 0
$$

where $p_{i}(\vec{x})$ is a single multivariate Gaussian joint density function.

## III. Prior Knowledge for Clustering

In previous works, clustering approaches normally required prior knowledge, either a predefined cluster number or an estimated minimal distance between different clusters. In [17], [19], a well-known approach, k-Means, was used as the clustering tool. But the number of clusters must be provided before the clustering procedure can be executed. For a practical function, knowing such prior knowledge is usually impossible and unfeasible.

A different clustering technique, RPCL, is used in the proposed algorithms. It can detect the real number of clusters during the clustering process without any prior knowledge. In this following, a comparison between k-Means and RPCL is made. Before showing the comparison results, a quick look at the implementation of these two clustering approaches is necessary.

## A. K-Means Clustering

In k-Means clustering, each cluster is specified by its center vector. For any given number $k$, the clustering process can be summarized as follows.

1) Generate $k$ centers $\vec{m}_{1}, \ldots, \vec{m}_{k}$ randomly.
2) Assign each individual to the nearest center.
3) Update each center to the mean vector of all the individuals assigned to it in last step.
4) If the new center is different to the previous one, repeat from step 2.
5) Otherwise, stop clustering and return the cluster centers.

## B. RPCL

RPCL is a heuristic competitive learning algorithm proposed for clustering, with the favorable feature that it can select the number of clusters during learning automatically [20]. The key idea of RPCL is that for each input $\vec{x}$, not only the winner is updated by a learning rate $\alpha_{c}$ to approach $\vec{x}$, but also the second winner (rival) is de-learned by a de-learning rate $\alpha_{r}$. That is

$$
\begin{aligned}
\vec{m}_{c}^{(t+1)} & =\vec{m}_{c}^{(t)}+\alpha_{c}\left(\vec{x}-\vec{m}_{c}\right) \\
c & =\arg \min _{j} \gamma_{j}\left\|\vec{x}-\vec{m}_{j}\right\|^{2} \\
\vec{m}_{r}^{(t+1)} & =\vec{m}_{r}^{(t)}-\alpha_{r}\left(\vec{x}-\vec{m}_{r}\right) \\
r & =\arg \min _{j \neq c} \gamma_{j}\left\|\vec{x}-\vec{m}_{j}\right\|^{2} \\
\vec{m}_{j}^{(t+1)} & =\vec{m}_{j}^{(t)}, \quad j \neq c, \quad j \neq r
\end{aligned}
$$

where $\vec{m}_{j}$ represents the center of the cluster $j, \alpha_{c}>\alpha_{r}$, and $\gamma_{j}$ being the frequency that $\vec{m}_{j}$ wins the competition up to now. The mechanism of RPCL tries to push its rival far away from the cluster toward which the winner is moving, thus implicitly produces a force which attempts to make sure that each cluster is learned by only one vector. Because the rival may belong to other clusters, de-learning rate usually is much smaller than learning rate. The effect of using this mechanism is that the appropriate number of units will be selected automatically to represent an input data set by gradually driving extra units far away from the data set when the number of units used for learning is larger than the number of clusters in the input data set.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Clustering results with k-Means and original RPCL. (a) $\mathrm{k}-\operatorname{Means}(k=3)$ succeeds in finding three clusters. (b) $\mathrm{k}-\operatorname{Means}(k=3)$ fails in finding three clusters. (c) Original $\operatorname{RPCL}(k=4)$ succeeds in finding three clusters with initialization domain [0.0, 1.0]. (d) Original $\operatorname{RPCL}(k=4)$ succeeds in finding three clusters with initialization domain $[3.0,4.0]$.

The approach introduced above is called original RPCL. It only considers the center of clusters and selects the winner according to distance measure. The riginal RPCL was extended to cluster data sets with complicated shapes via the finite mixture modeling. When the distribution for each cluster is assumed to be a Gaussian $\mathcal{N}\left(m_{i}, \Sigma_{i}\right)$, an adaptive form of RPCL is proposed as follows [21]:

$$
\begin{aligned}
c= & \arg \min _{j} d_{j} \\
r= & \arg \min _{j \neq c} d_{j} \\
d_{j}= & \left(\vec{x}-\vec{m}_{j}\right)^{\prime} \Sigma_{j}^{-1}\left(\vec{x}-\vec{m}_{j}\right) \\
& +\ln \left|\Sigma_{j}\right|-2 \ln \gamma_{j}
\end{aligned}
$$

Updating on parameters $\vec{m}_{j}$ becomes exactly the same with (3). The update of the covariance matrix $\Sigma_{j}$ is as follows:

$$
\begin{aligned}
\Sigma_{c}^{(t+1)} & =\left(1-\alpha_{c}\right) \Sigma_{c}^{(t)}+\alpha_{c}\left(\vec{x}-\vec{m}_{c}\right)\left(\vec{x}-\vec{m}_{c}\right)^{\prime} \\
\Sigma_{j}^{(t+1)} & =\Sigma_{j}^{(t)}, \quad j \neq c
\end{aligned}
$$

## C. Comparison

The test samples are comprised of three clusters, and each cluster has 500 points from a Gaussian distribution, their means are at $(-1.0,1.0),(-1.0,-1.0)$, and $(1.0,-1.0)$ respectively.

For k-Means, the preset number is 3 , and the initial center is generated randomly from the domain $[-0.5,0.5]$. In order to
show the automatic number selection ability, the initial number of clusters for RPCL is set to 4 , and the initial center is generated randomly from two domain, [3.0, 4.0] and [0.0, 1.0], the learning and de-learning rate are set to $\alpha_{c}=0.05, \alpha_{r}=0.002$, respectively.

Even when the right cluster number is given, k-Means cannot guarantee the correct clustering results. From Fig. 5(b), we can see that clustering results of k-Means is very dependent on initial positions. While for RPCL, clustering succeeds on all the independent runs by automatically selecting correct number, even if the initialization domain changes [see Fig. 5(c) and (d)]. Thus, RPCL not only has the unique automatic number selection ability, but also shows better reliability.

## IV. Clustering and Learning Gaussian Distribution Algorithms

Two new EDAs that take advantage of clustering are presented in this section. The first combines original RPCL with $\mathrm{EGNA}_{\mathrm{BGe}}$, so it is called the Clustering and Estimation of Gaussian Network Algorithm based on BGe metric $\left(\mathrm{CEGNA}_{\mathrm{BGe}}\right)$. The other uses adaptive RPCL as both a clustering and estimation approach, and is called the Clustering and Estimation of Gaussian Distribution Algorithm (CEGDA). Both algorithms regard the data as a random sample from a finite mixture of multivariate Gaussian distribution, and multiple interdependencies between variables are considered in both of them.

## A. $\mathrm{CEGNA}_{\text {BGe }}$

The design of this algorithm is to cluster the selected individuals into clusters by original RPCL approach, and for each single cluster, $\mathrm{EGNA}_{\text {BGe }}{ }^{2}$ is used to estimate the distribution. Because of the use of RPCL, prior knowledge is not required, and the actual number will be decided during the clustering process. To be exact, at the beginning of clustering, a small number is assigned as the initial assumed number of clusters, if any extra cluster is found at the end of clustering, the clustering process stops and the left clusters are estimated; otherwise the clustering process is repeated with the cluster number doubled, until the stopping criterion is met. Here, an extra cluster is a cluster whose size is less than a predefined threshold value. For example, if some outliers exist in the data set, RPCL will allocate a unit to it, and the size of this cluster is 1 . But this cluster will not be retained, but discarded as noise information. The new individuals are simulated based on each estimated distribution, and the number of solutions from a certain cluster is proportional to its average fitness.

The framework of $\mathrm{CEGNA}_{\text {BGe }}$ is as follows.

1) Initialize a population of $N$ individuals randomly.
2) Select $S e \leq N$ individuals according to some selection scheme.
3) Cluster the selected individuals into $k$ clusters by original RPCL.
4) Estimate the distribution $P_{i}(x), i=1, \ldots, k$ by $\mathrm{EGNA}_{\text {BGe }}$.
5) Sample $N_{i}\left(\sum_{i=1}^{k} N_{i}=N\right)$ new individuals based on $P_{i}(x)$ to replace the old population, $N_{i}$ is proportional to the average fitness of each cluster.
6) Stop if some stopping criterion is reached, go to 2 otherwise.

## B. CEGDA

The joint density function of a multivariate Gaussian distributions can be written as a product of conditional density functions, each of which belongs to an independent Gaussian distribution. That is

$$
p(x)=\prod_{i=1}^{n} \mathcal{N}\left(\mu_{i}+\sum_{j=1}^{i-1} b_{j i}\left(x_{j}-\mu_{j}\right), \sigma_{i}\right)
$$

where $\mathcal{N}(\mu, \sigma)$ represents a univariate Gaussian density function with mean $\mu$ and standard deviation $\sigma . \mu_{i}$ in (6) is the unconditional mean vector of $x_{i}, \sigma_{i}$ is the conditional standard deviation of $x_{i}$ given values for $x_{1}, x_{2}, \ldots, x_{i-1}$, and $b_{j i}$ is a linear coefficient reflecting the strength of the relationship between $x_{i}$ and $x_{j}$.
Shachter and Kenley [23] described the general transformation from $\vec{\sigma}=\left\langle\sigma_{1}, \ldots, \sigma_{n}\right\rangle$ and $\left\{b_{j i} \mid j<i\right\}$ to the precision matrix $W$ of Gaussian distribution, which is the inverse of covariance matrix. They use the following recursive formula in

[^0]which $W(i)$ denotes the $i \times i$ upper left submatrix of $W, \overrightarrow{b_{i}}$ denotes the $(i-1)$-dimensional column vector $\left(b_{1, i}, \ldots, b_{i-1, i}\right)$, and $\overrightarrow{b_{i}}$ denotes the transposed vector

$$
W(i+1)=\left(\begin{array}{cc}
W(i)+\frac{\vec{b}_{i+1} \vec{b}_{i+1}}{\sigma_{i+1}} & -\frac{\vec{b}_{i+1}}{\sigma_{i+1}} \\
-\frac{\vec{b}_{i+1}}{\sigma_{i+1}} & \frac{1}{\sigma_{i+1}}
\end{array}\right)
$$

This transformation makes it possible to construct a new algorithm. Since adaptive RPCL updates both the mean and the covariance matrix at each step of clustering, and the factorization form of Gaussian can be obtained from mean and covariance matrix using the transformation formula, it means adaptive RPCL can finish clustering and estimation at the same time. A method known as conditioning simulation method is used in both $\mathrm{CEGNA}_{\text {BGe }}$ and CEGDA. Based on (6), $x_{1}$ is generated first, and then generate $x_{2}$ given $x_{1}$, and so on. In summary, the framework of CEGDA is as follows.

1) Initialize a population of $N$ individuals randomly.
2) Select $\mathrm{Se} \leq N$ individuals according to some selection scheme.
3) Cluster the selected individuals into $k$ clusters and return the estimation of the distributions of each cluster $P_{i}(x), i=1, \ldots, k$ by adaptive RPCL.
4) Sample $N_{i}\left(\sum_{i=1}^{k} N_{i}=N\right)$ new individuals based on $P_{i}(x)$ to replace the old population, $N_{i}$ is proportional to the average fitness of each cluster.
5) Stop if some stopping criterion is reached, otherwise go to 2 .

## V. EXPERIMENTAL ANALYSIS

In this section, experimental results on a set of functions are presented to show the performance of $\mathrm{CEGNA}_{\text {BGe }}$ and CEGDA in all aspects, the strongpoint as well as the weakness.

## A. Experimental Design

Six test functions are chosen purposely, two of them are unimodal functions, and the others multimodal.

Sphere [see Fig. 6(a)]

$$
F(\vec{x})=\sum_{i=1}^{n} x_{i}^{2}
$$

SumCan [see Fig. 6(b)]

$$
\begin{aligned}
F(\vec{x}) & =1 /\left(10^{-5}+\sum_{i=1}^{n}\left|y_{i}\right|\right) \\
y_{1} & =x_{1} \\
y_{i} & =x_{i}+y_{i-1} \quad i \geq 2
\end{aligned}
$$

TwoPeaks [see Fig. 6(c)]

$$
F(\vec{x})=\sum_{i=1}^{2} \alpha_{i} \mathcal{N}\left(\vec{x}, \mu_{i}, \Sigma_{i}\right)
$$


[^0]:    ${ }^{2}$ For details of the implementation of $\mathrm{EGNA}_{\text {BGe }}$, refer to [12]

![img-5.jpeg](img-5.jpeg)

Fig. 6. Plots of the problems (dimension $=2$ ) to be optimized by continuous EDAs and CEP. (a) Sphere model. (b) SumCan model. (c) TwoPeaks model. (d) ThreePeaks model. (e) Shekel model with five local optima. (f) Schwefel model.
where $\mathcal{N}\left(\vec{x}, \mu_{i}, \Sigma_{i}\right)$ is a multivariate normal distribution, which has $n$-dimensional mean vector $\mu$ and $n \times n$ covariance matrix $\Sigma . \alpha_{1}=1000, \alpha_{2}=900, \mu_{1}=$ $(-10, \ldots,-10), \mu_{2}=(10, \ldots, 10), \Sigma_{i}(i=1,2)$ are diagonal matrices with all the diagonal elements equalling 1. ThreePeaks [see Fig. 6(d)]

$$
F(\vec{x})=\sum_{i=1}^{3} \alpha_{i} \mathcal{N}\left(x, \mu_{i}, \Sigma_{i}\right)
$$

where the same settings with TwoPeaks model plus $\alpha_{3}=$ 500 and $\mu_{3}=(0, \ldots, 0)$.

Shekel ${ }^{3}$ [see Fig. 6(e)]

$$
F(\vec{x})=\sum_{i=1}^{n}\left[\left(\vec{x}-\vec{a}_{i}\right)\left(\vec{x}-\vec{a}_{i}\right)^{T}+\vec{c}_{i}\right]^{-1}
$$

[^0]${ }^{3} n$ is set to 5 in the experiment.


[^0]:    Shekel ${ }^{3}$ [see Fig. 6(e)]

TABLE I
Settings FOR All the Test Functions

TABLE II
EXPERIMENTAL SETTINGS FOR ALL THE TEST AlGORITHMS

Schwefel [see Fig. 6(f)]

$$
F(\vec{x})=\sum_{i=1}^{n}-x_{i} \sin \left(\sqrt{\left|x_{i}\right|}\right)
$$

The particular two-dimensional case for each function is shown in Fig. 6, and the settings are in Table I.

## B. Algorithms Settings

Four EDA approaches, which are UMDA $_{v}$ [12], EGNA $_{\text {BG }}$ [12], CEGNA $_{\text {BG }}$ and CEGDA, and classical EP (CEP) [24] are used on the test functions for comparison purpose.

For each algorithm, the settings are unchanged through all experiments. All mean results were averaged over 30 independent runs. The initial population is generated uniformly at random in the domain specified in the description of each function. The detailed settings are listed in Table II.

In Table II, Population is the number of individuals in each generation, Selection is the number of promising solutions selected from all the individuals in the population based on some predefined selection scheme, and $\alpha_{v}$ and $\alpha_{r}$ are initial learning and de-learning rates used with RPCL.

## C. Results and Analysis

The experimental results are summarized in Tables III-IX. All results have been averaged over 30 independent runs, and the maximal evaluation number for unimodal and multimodal functions are $2 \times 10^{5}$ and $4 \times 10^{5}$, respectively. All the EDA algorithms use truncate selection, while CEP uses tournament selection with tournament size equals to 10 . Specially for $\mathrm{CEGNA}_{\text {BG }}$ and CEGDA, the initial cluster number is set to 2 . Also, the threshold value used with RPCL for deciding which cluster can be discarded is set to $5 \%$ of the size of whole data set.

The analysis is divided into four parts based on different points of view.

TABLE III
EXPERIMENTAL RESULTS FOR THE SPHERE FUNCTION

TABLE IV
EXPERIMENTAL RESULTS FOR THE SUMCAN FUNCTION

TABLE V
EXPERIMENTAL RESULTS FOR THE TWOPEAKS FUNCTION

TABLE VI
EXPERIMENTAL RESULTS FOR THE THREEPEAKS FUNCTION

TABLE VII
EXPERIMENTAL RESULTS FOR THE SHEKEL FUNCTION
With Five Local Optima ( $\mathrm{D}=4$ )

1) Easy Unimodal Problem: Sphere model has only one global optimum without any local optimum and the variables are independent of each other. Basically it appears rather easy for nearly any evolutionary algorithms. From Table III, it appears that $\mathrm{CEGNA}_{\text {BG }}$ and CEGDA can both perform well on the Sphere function. Actually, because of simplicity, all the test algorithms can find a very good solution at the end. It can

TABLE VIII
Experimental Results for the Shekel Function
With Five Local Optima $(D=30)$

TABLE IX
EXPERIMENTAL RESULTS FOR THE SCHWEFEL FUNCTION

be noticed that among the EDAs, the algorithms with single Gaussian distribution assumption outperform the new proposed algorithms using clustering techniques. Specifically, UMDA $_{\mathrm{c}}$, which does not consider any interdependencies, performs far better than the others. The reason is that for unimodal functions, the single Gaussian distribution assumption is more suitable than the mixture of Gaussian model; moreover, this particular function nicely accords with the no interdependencies assumption. Also, all the algorithms based on distribution estimation have better performance than CEP, which mainly depends on random search.
2) Problem With Strong Interdependencies: The SumCan function is a unimodal function with very strong interdependencies between the variables, and was used in [12] to show the advantage of algorithm EGNA $_{\text {BGc }}$ over UMDA $_{\mathrm{c}}$ and $\mathrm{MIMIC}_{\mathrm{c}}$.

All the EDA algorithms are better than CEP in this specific case, since it is very hard for CEP to find a good solution when fitness value is approximately equal to zero at most points in the search space. Inside the EDA family, UMDA ${ }_{\mathrm{c}}$ performs very badly because it ignores any interdependency information. The most interesting result is that even if $\mathrm{CEGNA}_{\text {BGc }}$ and CEGDA do not assume any independency, they are both outperformed by $\mathrm{EGNA}_{\text {BGc }}$, especially $\mathrm{CEGNA}_{\text {BGc }}$ appears the worst among all the EDA approaches. The reason is that although EGNA $_{\text {BGc }}$ and $\mathrm{CEGNA}_{\text {BGc }}$ use an identical distribution estimation procedure, the data set for estimation is totally different. $\mathrm{EGNA}_{\text {BGc }}$ uses the whole set of selected individuals, while $\mathrm{CEGNA}_{\text {BGc }}$ clusters first and estimates the distribution for each cluster thereafter. With dimension size equal to 10 , it is impossible for all the selected individuals to be selected into one cluster by original RPCL which only use the distance as the measure. As a result, each cluster only comprises of individuals from a very small space, and the new individuals will inevitably be trapped in this area, the whole optimization process will converge undesirably. As for CEGDA, despite it that also uses clustering, it behaves notably better than $\mathrm{CEGNA}_{\text {BGc }}$. In fact, the best
value from CEGDA is very close to the global optimum, which indicates that CEGDA really has captured the interdependencies between the variables. The reason why it cannot find the global optimum may be that the estimated Gaussian distribution, which makes use of adaptive RPCL, is a little less accurate than that of the other method, such as $\mathrm{EGNA}_{\text {BGc }}$. The difference between CEGDA and $\mathrm{CEGNA}_{\text {BGc }}$ comes from the use of adaptive RPCL in CEGDA. In adaptive RPCL, the pure distance measure is substituted by the density measure, which enables each cluster to hold distance data. So in CEGDA, a lot of new individuals farther from the current mean can be generated, which prevents the premature happening like $\mathrm{CEGNA}_{\text {BGc }}$.
3) Multimodal Problems With a Few Local Optima: In this part, the results from three test functions are discussed. These three functions, TwoPeaks, ThreePeaks, and Shekel, are all multimodal functions. Because one important motivation of constructing these two new algorithms is to take advantage of clustering technique to overcome the difficulty in dealing with multimodal functions. Thus, the performance on these three problems can evaluate if this goal has achieved. Compared with $\mathrm{UMDA}_{\mathrm{c}}$ and $\mathrm{EGNA}_{\text {BGc }}$, the two new EDAs show better performance on all three problems. $\mathrm{CEGNA}_{\text {BGc }}$ can reach the global optimum in every run, and although CEGDA cannot guarantee to reach the global optimum on ThreePeaks problem every time, the error is infinitesimal. This little difference between $\mathrm{CEGNA}_{\text {BGc }}$ and CEGDA once again gives some empirical proof to support the deduction based on the results on the SumCan function, which is the estimation by adaptive RPCL is a little bit less accurate than that from $\mathrm{EGNA}_{\text {BGc }}$.

Besides correctly finding one global optimum, the automatic number selection feature of RPCL can make it possible to find the exact number of global optima provided the solving problem only has a few local optima. In order to illustrate the autonomic number selection ability in a clearer way, the optimization process for the 2-dimensional ThreePeaks function by $\mathrm{CEGNA}_{\text {BGc }}$ is traced, and the distributions of selected individuals at different stage are shown in Fig. 7. At generation 1, just after the initialization, the selected individuals are located in the space rather uniformly. Until generation 5, the population has begun to gather into three groups, two around global optima separately and the middle one around the local optimum. Because at each generation, new individuals are generated in proportion to the average fitness of each cluster, more individuals around global optimum are simulated and the size of the cluster representing local optimum decreases step by step. At generation 10, it can be noticed that only two clusters are left, each of which contains a global optimum. Similar processes occur when optimizing TwoPeaks and Shekel functions. This process fully indicates that making use of the automatic number selection ability of RPCL, $\mathrm{CEGNA}_{\text {BGc }}$ and CEGDA have the ability to detect the number of global optima automatically if the number of local optima is small.

CEP performs poorly on TwoPeaks and ThreePeaks problems due to the same reason when applied to SumCan function, which is the needle-in-stack alike landscape. For the Shekel function, CEP can find the global optimum in $13(d=4)$ and $5(d=30)$ runs out of 30 , and some local optima are found in the other runs.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Demonstrate how $\mathrm{CEGNA}_{\text {BG }}$, can automatically detect the number of global optima of ThreePeaks function. (a) Distribution of selected 500 individuals at generation 1. (b) Distribution of selected 500 individuals at generation 5. (c) Distribution of selected 500 individuals at generation 10.
4) Multimodal Problems With Many Optima: Schwefel function contains many local optima. The results show that $\mathrm{UMDA}_{\mathrm{c}}$ is the worst, $\mathrm{EGNA}_{\mathrm{BGe}}$ is the best and the other three hold comparable behavior. Due to the large number of local optima, under practical conditions, the global optimum can hardly be detected, every selected cluster normally contains data from the neighborhood of different local optima. Because EDAs use estimated distribution to guide the search, and an accurate distribution estimation needs enough samples, when the number of local optima is very large, the population size has to be very large in order to capture every local optimum, which is impractical.
5) Effect of Automatic Number Selection: Finally, the algorithm presented by Pelican and Goldberg [17] is used here to examine the effect of automatic number selection to the result of optimization. This algorithm is equivalent with $\mathrm{k}-$ Mesus $+$ $\mathrm{UMDA}_{\mathrm{c}}$ (called $\mathrm{CUMDA}_{\mathrm{c}}$ in the following context). Apply the new EDAs accompanying with $\mathrm{CUMDA}_{\mathrm{c}}$ to the Shekel function $(\mathrm{d}=30)$, and the results are summarized in Table X. The cluster number provided to k-Means equals $4,5,6,10$, respectively, the population size and selection size are 2000 and 1000.

It appears that even if you give a larger number than the number of local optima, it cannot guarantee that the global optimum can be found. The reason is that the clustering result of k -Means relies on the initialization, which means using a larger number can produce the same clustering result as the result from using a smaller number. Overall, the ability of automatic number selection provided by RPCL shows significant advantage over the previous used clustering techniques.

TABLE X
EXPERIMENTAL RESULTS FOR EXAMINING THE EFFECT OF AUTOMATIC NUMBER SELECTION


## VI. CONCLUSION

This paper proposes two new EDAs for continuous optimization, $\mathrm{CEGNA}_{\text {BGe }}$ and CEGDA, and analyzes the strongpoint and weakness of them through a set of experiments. The improvement of the new algorithms over the existing ones is twofold: the first improvement is by incorporating clustering technique, the new algorithms can solve multimodal functions with a few local optima very successfully, while those EDAs using the single Gaussian distribution assumption cannot solve effectively; the second advantage is by making use of the automatic number selection ability of RPCL, new algorithms for the first time in EDAs have the ability to detect the number of global optima automatically, no prior knowledge is needed for the algorithms to work. At the same time, it is also found that if a multimodal function has too many local optima, it appears hard for the new algorithms to conquer.

Besides these common features, $\mathrm{CEGNA}_{\text {BGe }}$ and CEGDA also have some differences between them. $\mathrm{CEGNA}_{\text {BGe }}$ is easy to cause the optimization process to converge prematurely under some particular conditions (e.g., SumCan function). CEGDA does not have this deficiency, but as a result of doing the clustering and estimation concurrently using adaptive RPCL, when facing a data set with strong interdependencies between the variables, its estimated result is slightly less accurate compared with the other estimation model.

Up to now, most research works use Gaussian distribution as model to construct new algorithms in EDA category. The other distributions can be considered in the future work.
