# A Distance-Based Ranking Model Estimation of Distribution Algorithm for the Flowshop Scheduling Problem 

Josu Ceberio, Ekhine Irurozki, Alexander Mendiburu, and Jose A. Lozano, Member, IEEE


#### Abstract

The aim of this paper is two-fold. First, we introduce a novel general estimation of distribution algorithm to deal with permutation-based optimization problems. The algorithm is based on the use of a probabilistic model for permutations called the generalized Mallows model. In order to prove the potential of the proposed algorithm, our second aim is to solve the permutation flowshop scheduling problem. A hybrid approach consisting of the new estimation of distribution algorithm and a variable neighborhood search is proposed. Conducted experiments demonstrate that the proposed algorithm is able to outperform the state-of-the-art approaches. Moreover, from the 220 benchmark instances tested, the proposed hybrid approach obtains new best known results in 152 cases. An in-depth study of the results suggests that the successful performance of the introduced approach is due to the ability of the generalized Mallows estimation of distribution algorithm to discover promising regions in the search space.


Index Terms-Estimation of distribution algorithms, generalized Mallows model, permutation flowshop scheduling problem, permutations-based optimization problems.

## I. INTRODUCTION

SINCE Johnson published his work on the two-machine flowshop in 1954 [1], numerous papers have dealt with the flowshop scheduling problem. Early research on this topic was highly theoretical and focused mainly on exact methods. In 1976, Garey et al. [2] proved that this problem is NPcomplete for more than two machine instances, and thus, stated the difficulty of achieving optimal solutions. In later decades, the problem was extensively addressed in the literature [3], [4]. A simplified version of this problem is the permutation flowshop scheduling problem (PFSP) [4], where the goal is to find the optimal sequence of $n$ jobs that must be processed in $m$ machines. Even though the PFSP was formulated in the 1950s,

[^0]it is still a meaningful research topic due to its strong engineering background. Initially, the most common optimization criterion in the PFSP was the total completion time of the jobs, also called makespan. However, the minimization of the total flow time (TFT) has captured the attention of the scientific community since it is more relevant than the makespan for the current dynamic production environments. The TFT measures the sum of the times that each job remains in the flowshop. Thus, minimizing the TFT can lead to the stable utilization of resources, rapid turn-around of jobs, and minimization of work-in-progress inventory costs [5].
The literature contains evidence of a wide variety of strategies that approach the PFSP with respect to the TFT criterion (PFSP-TFT). Exact algorithms accurately work out the optimal solution. However, they are computationally costly and, with the exception of small size examples (instances up to 10-15 jobs), exact algorithms cannot be used in a reasonable time span. Examples of such methods are branch and bound approaches [6], [7]. Besides the exact methods, heuristic procedures such as constructive heuristics [5], [8]-[13] and composite heuristics [10], [14]-[16] have also been proposed. Unfortunately, such heuristics have shown a poor performance when solving PFSP instances of 50 jobs or more.
Advances in metaheuristic optimization supplied the research community with new techniques to tackle combinatorial optimization problems. As proof of these advances, we found a wide variety of strategies in the literature for solving the PFSP, such as local search [17]-[19], simulated annealing [20], tabu search [21]-[23], genetic algorithms (GAs) [24]-[28], particle swarm optimization [29]-[32], ant colony optimization [33]-[36], or estimation of distribution algorithms (EDAs) [37]. Currently, the literature points to the hybrid approaches, such as those published by Costa et al. [variable neighborhood search 4 - (VNS $\left.{ }_{4}\right)$ ] [19] and Xu et al. [asynchronous genetic algorithm (AGA)] [26], as the cutting-edge algorithms for optimizing the PFSP-TFT. In the first case, the authors propose the combination of a VNS with a constructive algorithm called $\operatorname{LR}(n / m)$ [10]. In the second case, a GA is hybridized with VNS. Additionally, to guide the initial population, $\operatorname{LR}(n / m)$ is also used.
In this paper, we go deeper into the development of EDAs, proposing a new EDA for permutation-based optimization problems and testing its performance on the PFSP-TFT.


[^0]:    Manuscript received June 18, 2012; revised October 11, 2012 and February 26, 2013; accepted April 24, 2013. Date of publication April 29, 2013; date of current version March 28, 2014. This work was supported in part by the Basque Government's programs Saiotek and Research Groups 20132018 under Grant IT-609-13, the Ministry of Science and Technology under Grant TIN2010-14931, COMBIOMED network in computational biomedicine (Carlos III Health Institute), and the European Commission's NICaiA Project under Grant PIRSES-GA-2009-247619. The work of Josu Ceberio was supported by a grant from the Basque Government. The work of Ekhine Irurozki was supported by the MICINN under Grant BES-2009-029143.

    The authors are with the Intelligent Systems Group, Department of Computer Science and Artificial Intelligence, University of the Basque Country UPV/EHU, Gipuzkoa 20018, Spain (e-mail: josu.ceberio@ehu.es; ekhine.irurozki@ehu.es; alexander.mendiburu@ehu.es; ja.lozano@ehu.es). Digital Object Identifier 10.1109/TEVC.2013.2260548

EDAs are a type of population-based optimization algorithm that, at each generation, learn a probabilistic model from a set of promising solutions. The new offspring is then obtained by sampling the probabilistic model.

Recently, they have become a strong alternative for solving optimization problems from diverse domains [38]-[43]. Apart from the work of Jarboui [37], other EDA-based approaches have been also proposed for solving similar permutationcoded scheduling problems [44]-[46]. However, a recently published review on EDAs for permutation-based optimization problems [47] claimed that the performance of the existing EDAs could be further improved. The authors argue that most of the existing EDAs were originally designed for solving integer or real-valued domain problems, and were later adapted to deal with permutation-based problems. Among the EDAs specifically designed for permutation-based problems, Tsutsui [48], [49] introduced two of the most successful proposals: the edge histogram-based sampling algorithm (EHBSA) and node histogram-based sampling algorithm (NHBSA). In that review [47], the experimental study demonstrated that these two algorithms were the most competitive EDAs for solving permutation-based problems. Nonetheless, in [47] the authors suggest that implementing specific probability models on rankings could improve the performance of EDAs on permutationbased problems.

Along the same research line, [50] introduced the Mallows EDA, the first preliminary attempt to apply a probabilistic model that estimates an explicit probability distribution in the domain of permutations. The Mallows model is a distancebased exponential probabilistic model considered analogous to the Gaussian probability distribution over the space of permutations. The results reported in [50] showed that Mallows EDA is able to outperform EHBSA and NHBSA for the PFPS with the makespan criterion.

In this paper, we go a step further by proposing a generalization of the Mallows model [51] in the framework of EDAs. The resulting algorithm, called generalized Mallows (GM) EDA (GM-EDA), introduces the first serious attempt to apply parametric models for permutation domains, such as the GM model, for solving permutation-based problems with EDAs.

In order to demonstrate the validity of our proposal, we approach the PFSP-TFT with a hybrid version of the GMEDA. The hybrid GM-EDA is a two-stage algorithm. In the first stage, it runs the GM-EDA, and the resulting individual is used as the initial solution for the VNS employed in the second stage. Experimental results show that the hybrid GMEDA is competitive with the state-of-the-art algorithms, since it is able to obtain new best known results in 152 instances of the 220 tested.

The remainder of the paper is organized as follows. In the following section, the formulation of the PFSP is given. In Section III, the GM model is described in detail. Section IV introduces the GM-EDA. In Section V, the performance of the GM-EDA over some PFSP instances is studied. Our hybrid proposal for solving the PFSP and its application to several benchmark instances is introduced afterward, in Section VI. We carry out a thorough discussion of the results
in Section VII. Finally, some conclusions and ideas for future work are presented in Section VIII.

## II. Problem Formulation

In the permutation flowshop scheduling problem [52], [53], $n$ jobs $(i=1, \ldots, n)$ have to be scheduled on $m$ machines $(j=1, \ldots, m)$ in such a way that a criterion is minimized. A job consists of $m$ operations and the $j$ th operation of each job must be processed on machine $j$ for a given specific processing time without interruption. The processing times are fixed, nonnegative values and every job is available at time zero. At a given time, a job can start on the $j$ th machine when its $(j-1)$ th operation has finished on machine $(j-1)$, and machine $j$ is free.

As introduced previously, our objective is to find a sequence of jobs such that the total flow time is minimized. In this case, the sequence of $n$ jobs is codified as a permutation function $\sigma$ from $\{1, \ldots, n\}$ onto $\{1, \ldots, n\}$, where $\sigma(i)$ is the rank assigned to job $i, i=1, \ldots, n$, and $\sigma^{-1}(i)$ denotes the job at rank $i$ in $\sigma$ (referred also as $\sigma(i)$ ). For instance, the sequence $\sigma=(231)$ denotes that job 1 is ranked in the second position $(\sigma(1)=2)$, job 2 is ranked third, and job 3 is ranked first. An alternative description of a ranking is given by the associated ordering, denoted in this case as $\sigma^{-1}=\langle 312\rangle$.

Equation (1) expresses mathematically the concept of TFT for a ranking $\sigma$ of jobs, where $c_{\sigma(i), m}$ stands for the completion time of job $\sigma\langle i\rangle$ at machine $m$

$$
F(\sigma)=\sum_{i=1}^{n} c_{\sigma(i), m}
$$

Being that $p_{\sigma(i), j}$ is the processing time required by job $\sigma(i)$ in machine $j$, the completion time of job $\sigma(i)$ on machine $j$ can be recursively calculated as

$$
c_{\sigma(i), j}= \begin{cases}p_{\sigma(i), j} & i=j=1 \\ p_{\sigma(i), j}+c_{\sigma(i-1), j} & i>1, j=1 \\ p_{\sigma(i), j}+c_{\sigma(i), j-1} & i=1, j>1 \\ p_{\sigma(i), j}+\max \left\{c_{\sigma(i-1), j}, c_{\sigma(i), j-1}\right\} & i>1, j>1\end{cases}
$$

## III. GENERALIZED MALLOWS MODEL

Until the 1950s, probability models for permutations were not extensively developed. The psychology domain was the first that demanded specific models to efficiently manage probability distributions over permutations. Early works proposed Thurstonian [54] and uniform models. At the end of the decade, a probabilistic model for permutations called the Mallows [55] model was introduced. The Mallows model is a probabilistic model that has been considered as analogous over permutations to the Gaussian distribution: they are both exponential unimodal models defined by two parameters, the mean and the variance.

Despite having been proposed in the late 1950s, it is a lively model that has recently received the attention of the statistical and machine learning communities, and has been

applied to problems from diverse fields, such as recommender systems [56], multilabel classification [57], [58], data modeling [59], clustering [60], and computer vision [61].

Under this model, the probability value of every permutation $\sigma \in \mathbb{S}_{n}$ (where $\mathbb{S}_{n}$ stands for the set of $n$ ! permutations of $n$ items) depends on just two parameters: a spread parameter $\theta$ and the distance to a central permutation $\sigma_{0}$, which is calculated by a particular metric $D\left(\sigma, \sigma_{0}\right)$. Formally, the Mallows model is defined as

$$
P(\sigma)=\psi(\theta)^{-1} \exp \left(-\theta D\left(\sigma, \sigma_{0}\right)\right)
$$

where $\psi(\theta)$ is a normalization constant.
When $\theta$ equals 0 , (3) assigns equal probability to every permutation $\sigma$ in $\mathbb{S}_{n}$. The larger the value of $\theta$, the more peaked the distribution becomes around the central permutation (we do not consider the situation $\theta<0$ ). The second parameter is the central ranking $\sigma_{0}$. This model assigns every permutation $\sigma \in \mathbb{S}_{n}$ a probability that decays exponentially with respect to its distance to this central permutation $\sigma_{0}$. In this way, $P(\sigma)$ can be considered as an exponential nonuniform distancebased ranking model.

The distance metric with which the Mallows model is traditionally coupled in the literature (and is used in this manuscript) is Kendall's $\tau$. Denoted as $D_{\tau}(\sigma, \pi)$, it measures the number of pairs of items for which $\sigma$ and $\pi$ have opposing ordering. An equivalent definition for Kendall's- $\tau$ is the minimum number of adjacent transpositions needed to bring $\sigma^{-1}$ into $\pi^{-1}$

$$
\begin{aligned}
D_{\tau}(\sigma, \pi)=|\{(i, j): i<j & ,(\sigma(i)<\sigma(j) \wedge \pi(i)>\pi(j)) \\
& \vee(\pi(i)<\pi(j) \wedge \sigma(i)>\sigma(j))\}|
\end{aligned}
$$

Kendall's- $\tau$ has the right invariant property since $D_{\tau}(\sigma, \pi)=$ $D_{\tau}(\sigma \gamma, \pi \gamma)$ for every permutation $\gamma \in \mathbb{S}_{n}$, where $\sigma \gamma$ stands for the composition of the permutations $\sigma$ and $\gamma$, and is defined as $\sigma \gamma(i)=(\sigma \circ \gamma(i))=\sigma(\gamma(i))$. Thus, by right invariance, when $\gamma=\pi^{-1}, D_{\tau}(\sigma, \pi)$ can be simplified as $D_{\tau}\left(\sigma \pi^{-1}, e\right)$ (also denoted as $D_{\tau}\left(\sigma \pi^{-1}\right)$ ), where $e$ stands for the identity permutation $e=(123 \ldots n)$.

The analogies between the Gaussian and the Mallows distributions can be seen by looking at Fig. 1. In this figure, every permutation in $\sigma \in \mathbb{S}_{5}$ (the set of 120 permutations of five items) is placed on the $x$-axis and their probability values for different $\theta$ are plotted. The central permutation $\sigma_{0}$ is that with the highest probability value in the middle of the $x$-axis. For representation purposes, all the individuals at the same distance from $\sigma_{0}$ have been equally divided into two groups and drawn on the $x$-axis in each side of the central permutation.

Among the many proposals, the GM model [51] is the most popular extension of the Mallows model. This extension requires the metric to be decomposed into $n-1$ terms in such a way that it can be expressed as $D\left(\sigma, \sigma_{0}\right)=\sum_{j=1}^{n-1} S_{j}\left(\sigma, \sigma_{0}\right)$, where $S_{j}\left(\sigma, \sigma_{0}\right)$ is related with the $j^{\text {th }}$ position of the permutation. The central ranking $\sigma_{0}$ in the GM model is also the permutation with the highest probability mass. However, instead of a single spread parameter $\theta$, the GM model uses
![img-0.jpeg](img-0.jpeg)

Fig. 1. Probability value for each permutation in $\mathbb{S}_{5}$ for different values of the spread parameter $\theta$.
$n-1$ spread parameters $\boldsymbol{\theta}=\left(\theta_{1}, \theta_{2}, \ldots, \theta_{n-1}\right)$, each $\theta_{j}$ affecting a particular position $j$ of the permutation. The GM model is thus given by

$$
P(\sigma)=\psi(\boldsymbol{\theta})^{-1} \exp \left(\sum_{j=1}^{n-1}-\theta_{j} S_{j}\left(\sigma, \sigma_{0}\right)\right)
$$

Because of the right invariance property, $S_{j}\left(\sigma, \sigma_{0}\right)$ can be rewritten as $S_{j}\left(\sigma \sigma_{0}^{-1}, e\right)=S_{j}\left(\sigma \sigma_{0}^{-1}\right)$. In the particular case of the Kendall's- $\tau$ distance, the $S_{j}$ terms are denoted by $V_{j}$, and are defined as $V_{j}(\pi)=\sum_{i=j+1}^{\sigma} I[\pi(j)>\pi(i)]$, where $I[$ cond $]$ equals one when the condition cond equals true, and 0 otherwise. Basically, $V_{j}(\pi)$ is the number of positions of the permutation on the right of $j$ with values smaller than $\pi(j)$. It follows from the definition that $V_{j}(\pi)$ ranges from 0 to $n-j$ for $1 \leq j<n$.

Taking into account that $D_{\tau}(\pi)=\sum_{j=1}^{n-1} V_{j}(\pi)$, (4) can be written as

$$
P(\sigma)=\psi(\boldsymbol{\theta})^{-1} \exp \left(\sum_{j=1}^{n-1}-\theta_{j} V_{j}\left(\sigma \sigma_{0}^{-1}\right)\right)
$$

for every $\sigma \in \mathbb{S}_{n}$. It is worth noting that one can uniquely determine any permutation $\pi$ with the $n-1$ integers $V_{1}(\pi), \ldots, V_{n-1}(\pi)$ in which the Kendall's- $\tau$ distance $D_{\tau}(\pi)$ decomposes.

Under the uniform distribution, the $V_{j}(\pi)$ variables that define a permutation are independent and, as a consequence [51], the probability distribution of the random variables $V_{j}\left(\sigma \sigma_{0}^{-1}\right)$ under the GM model given by (5) can be written as

$$
P\left(V_{j}\left(\sigma \sigma_{0}^{-1}\right)=r_{j}\right)=\frac{\exp \left(-\theta_{j} r_{j}\right)}{\psi_{j}\left(\theta_{j}\right)} \quad r_{j} \in\{0, \ldots, n-j\}
$$

Furthermore, the normalization constant $\psi(\boldsymbol{\theta})$, which if calculated naïvely requires $n$ ! sums, can be simplified as the product of $n-1$ terms

$$
\psi(\boldsymbol{\theta})=\prod_{j=1}^{n-1} \psi_{j}\left(\theta_{j}\right)=\prod_{j=1}^{n-1} \frac{1-\exp \left(-\theta_{j}(n-j+1)\right)}{1-\exp \left(-\theta_{j}\right)}
$$

The most important consequence of (6) and (7) is that, when the GM model considers the Kendall's- $\tau$ distance, it can be expressed as a multistage ranking model [62]. This means that the process of constructing a permutation has $n-1$ stages and the probabilities at a given stage depend only on the current stage, i.e., at stage $j$ the probability $P\left(V_{j}(\pi)\right)$. Equivalently, the value of $V_{j}(\pi)$, is not affected by the decisions made at previous stages, and in the same way this decision will not affect posterior stages. This property implies that the probability distribution of a given permutation $\sigma$ with $\boldsymbol{V}\left(\sigma \sigma_{0}^{-1}\right)=\left(r_{1}, \ldots, r_{n-1}\right)$ can be factorized as

$$
P(\sigma)=\prod_{j=1}^{n-1} P\left(V_{j}\left(\sigma \sigma_{0}^{-1}\right)=r_{j}\right)
$$

## A. Learning and Sampling the GM model

In order to introduce the GM model into the framework of EDAs, it is necessary to be able to learn the parameters of the model and sample new solutions from it in an efficient way. In this section we detail how we carry out both processes, which are intended to maintain a tradeoff between time complexity and accuracy.

The most common way of learning the parameters of probability distributions is by means of the maximum likelihood estimation (MLE) principle. The MLE parameters, given a sample of $N$ permutations $\left\{\sigma_{1}, \ldots, \sigma_{N}\right\}$, are the parameters $\sigma_{0}$ and $\boldsymbol{\theta}$ that maximize the likelihood function (we consider its logarithm)

$$
\begin{aligned}
\ln L\left(\sigma_{1}, \ldots, \sigma_{N} \mid \theta, \sigma_{0}\right) & =\ln P\left(\sigma_{1}, \ldots, \sigma_{N} \mid \boldsymbol{\theta}, \sigma_{0}\right)= \\
& -N \sum_{j=1}^{n-1}\left[\theta_{j} \bar{V}_{j}-\ln \left(\psi_{j}\left(\theta_{j}\right)\right)\right]
\end{aligned}
$$

where

$$
\bar{V}_{j}=\frac{1}{N} \sum_{i=1}^{N} V_{j}\left(\sigma_{i} \sigma_{0}^{-1}\right)
$$

There are several heuristics and exact methods to simultaneously obtain the parameters $\boldsymbol{\theta}$ and $\sigma_{0}$ [63], [64]. However, for the sake of time efficiency (this process is repeated at each generation inside the EDA), we have divided the learning process into two stages, dealing first with the calculation of the central ranking $\sigma_{0}$ and then with the spread parameters $\boldsymbol{\theta}$.

Maximizing the log-likelihood with respect to $\sigma_{0}$ given a sample of $N$ permutations $\left\{\sigma_{1}, \ldots, \sigma_{N}\right\}$ is equivalent to minimizing $\sum_{j=1}^{n-1} \theta_{j} \bar{V}_{j}\left(\sigma_{i} \sigma_{0}^{-1}\right)$. If all $\theta_{j}$ were equal (the case of the Mallows model) this problem would be the same as that of minimizing the sum of the distances with every permutation in the sample, which is a well known NP-hard problem [65], referred to as consensus ranking. The first stage of the learning process consists of computing an approximation to the consensus ranking by using the Borda algorithm [66], which is carried out in $O(n \times N)$. Borda is a simple yet accurate algorithm that calculates the average permutation of a given sample, which is, in fact, a consistent estimator of the consensus ranking [62]. Its pseudo-code is given in Algorithm 1. In [67] several methods

```
Algorithm 1 Borda Algorithm for Calculating \(\delta_{0}\)
    Input: A sample of \(N\) permutations \(\left\{\sigma_{1}, \ldots, \sigma_{N}\right\}\)
    For \(j 1\) to n
        \(\pi(j)=\sum_{i=1}^{N} \sigma_{i}(j) / N\)
    end For
    visited \(=\{ \}\)
    For \(j 1\) to n
        \(\min _{-} i \leftarrow \arg \min \{\pi(i) \mid i \notin\) visited \(\}\)
        \(\delta_{0}(\min _{-} i)=\bar{j}\)
        visited \(\leftarrow\) visited \(\cup \min _{-} i\)
    end For
    Output: \(\delta_{0}\)
```

for the consensus ranking problem are compared, concluding that Borda is one of the most efficient algorithms.

Once the consensus ranking $\delta_{0}$ is approximated, the second stage of the learning process consists of computing the dispersion parameters $\theta_{j}$ for the previously computed $\delta_{0}$. The maximum likelihood estimators of the dispersion parameters given the central ranking are given by solving

$$
\bar{V}_{j}=\frac{n-1}{\exp \left(\theta_{j}\right)-1}-\frac{n-j+1}{\exp \left(\theta_{j}(n-j+1)\right)-1}
$$

Equation (11) does not have a closed form expression but can be numerically solved by standard iterative algorithms for convex optimization. In this case, we use the Newton-Raphson algorithm. Since the number of iterations performed by this algorithm depends on the initial solution assigned, its time complexity cannot be exactly determined. However, when the initial solution is a good approximation, $O((\log h) F(h))$ is close to the real time-complexity. $F(h)$ denotes the cost of calculating the $f(x) / f^{\prime}(x)$ term with a $h$-digit precision in the Newton-Raphson algorithm (note that $h<<n$ ). ${ }^{1}$ Since we have $n-1$ spread parameters, the overall time-complexity of estimating the $\theta_{j}$ parameters is $O((n-1) \times(\log h) F(h))$ [68].

In relation to the sampling process, in (8) we showed that the probability distribution defined by the GM model can be factorized into $n-1$ terms. From a computational point of view, this decomposition turns out to be a very efficient way of sampling the probability distribution, a necessary condition in the context of EDAs. The process of generating the new offspring followed by drawing the $\boldsymbol{V}\left(\sigma_{s} \sigma_{0}^{-1}\right)$ vectors with the distribution in (8) and (6), $1 \leq s \leq N-1$. Then, by applying the algorithm proposed by Meila et al. [63], the corresponding permutation $\left(\sigma_{s} \sigma_{0}^{-1}\right)^{-1}$ is obtained (see pseudocode in Algorithm 2). Finally, each permutation $\sigma_{s}$ is obtained by inverting and composing with the consensus ranking $\sigma_{0}$, $\left(\left(\sigma_{s} \sigma_{0}^{-1}\right)^{-1}\right)^{-1} \sigma_{0}=\sigma_{s} \sigma_{0}^{-1} \sigma_{0}=\sigma_{s}$. The overall sampling procedure of a solution is carried out in $O\left(n^{2}\right)$.

In order to illustrate the conversion from $\boldsymbol{V}(\pi)$ to $\pi^{-1}$, Fig. 2 introduces an example.

The sampling step in the EDA takes time $O\left(n^{2} \times(M-\right.$ 1)), because $M-1$ the number of new solutions sampled at each generation. Since the complexity of the sampling step is higher than that of the learning step, Borda- $O(n \times N)$ and

[^0]
[^0]:    ${ }^{1}$ The precision parameter $h$ is set to $10^{-4}$.

```
Algorithm 2 Conversion from \(V(\pi)\) to \(\pi^{-1}\)
    Input: A vector of \(V(\pi)\)
    Create an empty list \(\pi^{-1}\)
    Insert \(n\) in position 0
    For \(j=n-1: 1\) in decreasing order
        Insert \(j\) in position \(V_{j}\) of \(\pi^{-1}\)
    end For
    Output: \(\pi^{-1}\)
Algorithm 3 Generalized Mallows EDA
    \(D_{0} \leftarrow\) Generate \(M\) individuals at random.
    \(t \leftarrow 1\)
    Do \{
        \(D_{t-1} \leftarrow\) Evaluate individuals.
        \(D_{t-1}^{S e} \leftarrow\) Select \(N \leq M\) individuals from \(D_{t-1}\).
        \(\hat{\sigma}_{0} \leftarrow\) Estimate the consensus ranking from \(D_{t-1}^{S e}\).
        \(\hat{\boldsymbol{\theta}} \leftarrow\) Estimate the spread parameters from \(D_{t-1}^{S e}\) and \(\hat{\sigma}_{0}\).
        \(D_{t} \leftarrow\) Sample \(M-1\) individuals from \(p_{t}(\sigma)=\) \(p\left(\sigma \mid D_{t-1}^{S e}, \hat{\sigma}_{0}, \hat{\boldsymbol{\theta}}\right)\) to create the new population.
        \}Until (Stopping criterion is met)
    Input: \(V(\pi)=(2,0,1)\)
        insert \(n=4 \quad\) in \(\quad 0 \quad \rightarrow \quad \pi^{-1}=(\mathbf{4})\)
        insert \(j=3 \quad\) in \(\quad V_{0}(\pi)=1 \quad \rightarrow \quad \pi^{-1}=(\mathbf{4} \mathbf{3})\)
        insert \(j=2 \quad\) in \(\quad V_{0}(\pi)=0 \quad \rightarrow \quad \pi^{-1}=(\mathbf{2} 43)\)
        insert \(j=1 \quad\) in \(\quad V_{1}(\pi)=2 \quad \rightarrow \quad \pi^{-1}=(\mathbf{2} 413)\)
    Output: \(\pi^{-1}=(2413)\)
```

Fig. 2. Given the $V(\pi)$ vector, permutation $\pi^{-1}$ is built.

Newton-Raphson- $O((n-1) \times(\log h) F(h))$, then the overall time complexity of a generation of the GM-EDA is dominated by this term and is $O\left(n^{2} \times(M-1)\right)$.

## IV. GENERALIZED MALLOWS EDA

GM-EDA is basically a classical EDA where the probabilistic model used is the GM model introduced in the previous section. In Algorithm IV the general outline of the GM-EDA is described.

The behavior of the GM-EDA not only depends on the general parameters of a classical EDA (population size, selection mechanism, stopping criterion, etc.) but also on the specific parameters of the probabilistic model used. In this particular case, the vector $\boldsymbol{\theta}$ is the set of parameters that determines the shape of the GM model, and thus, it is closely related to the behavior of the EDA. Therefore, before applying the algorithm in a general setting, we consider it very valuable to analyze its behavior in relation to these parameters.

In order to understand such behavior, we analyze the evolution of the GM model through the generations. To do that, we carried out a preliminary experiment studying the average value of the vector $\boldsymbol{\theta}$ at each generation. The first instances of Taillard's PFSP benchmark of size 20, 50, and 100 introduced in Section V are used. The general parameters of the GM-EDA are also described in the next section.

According to the results shown in Fig. 3, in the initial generations the average $\boldsymbol{\theta}$ values are close to 0 for all the instances, denoting a diverse population, which is reasonable taking into account the random initialization procedure. As the generations move forward, the average $\boldsymbol{\theta}$ values increase rapidly, reaching values of up to 500 . In the smallest size instances-those with 20 or 50 jobs-the average $\boldsymbol{\theta}$ values converge much faster than for instances of 100 jobs. However, in all the cases, the results indicate that, after a certain amount of generations, the convergence of the population accelerates dramatically.

With the aim of understanding the meaning of the average $\boldsymbol{\theta}$ values seen in Fig. 3, we studied the probability assigned to the consensus ranking $\sigma_{0}$ in relation to $\boldsymbol{\theta}$ (the GM model considers $n-1$ spread parameters, but for the sake of simplicity, we set the same value for all $\theta_{j}$ ). According to the results shown in Fig. 4, for $\boldsymbol{\theta}$ values below 2, the probability of $\sigma_{0}$ is close to 0 , thus encouraging an exploration stage. However, once a threshold is reached, the probability assigned to $\sigma_{0}$ increases quickly, leading the algorithm to an exploitation phase.

In the view of the results in Fig. 4, when $\theta$ takes values higher than 10 the probability of $\sigma_{0}$ is almost 1, and Fig. 3 shows that in the first few generations of the EDA, such a threshold is easily reached. In order to prevent the EDA from getting stuck, and to enhance the exploration ability of the model, we decided to set an upper bound value $\theta_{\text {upper }}$ to the spread parameters so that a trade off between exploitation and exploration is guaranteed.

## V. GENERALIZED MALLOWS EDA FOR PFSP

As mentioned previously, in order to analyze the performance of the new GM-EDA, we apply our proposal to an extensively studied problem in the literature, the permutation flowshop scheduling problem with respect to the total flowtime criterion. Although several algorithms have been presented in the literature, in order to obtain a real feedback, we compare our approach with the best two state-of-the-art algorithms: AGA [26] and VNS $_{4}$ [19].

AGA hybridizes a GA with VNS. The algorithm starts initializing the population randomly, with the exception of one solution, which is calculated with the constructive algorithm $\operatorname{LR}(n / m)$ [10]. At each iteration, $N / 2$ pairs of individuals in the population ( $N$ being the population size) are selected uniformly at random and submitted to an asynchronous crossover operator. The asynchronous crossover operator consists of three steps: 1) an enhanced VNS (eVNS) is applied to the parent individuals; 2) a twice two-point crossover (TTP) is performed with the resulting solutions of the eVNS; and 3) the individuals obtained from the crossover are again submitted to the eVNS. The asynchronous behavior of the operator is due to the number of improvements permitted in the local search procedures in the eVNS, the second call being much more powerful than the first. The best two individuals obtained from the crossover operator are added to the new population. Additionally, when all the individuals in the population have the same TFT value, the population is restarted randomly, keeping only the best solution in the new population.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Convergence of average $\boldsymbol{\theta}$ values for the first instances of the $20 \times 5,20 \times 10,20 \times 20,50 \times 5,50 \times 10,50 \times 20,100 \times 5,100 \times 10$, and 100 $\times 20$ configurations of Taillard's benchmark.

The recently published paper of Costa et al. [19] introduces an exhaustive analysis of different variations of the VNS, concluding that $\mathrm{VNS}_{4}$ (the version proposed in [19]) is the most successful. $\mathrm{VNS}_{4}$ explores solutions alternating between the insert neighborhood (considered as the main neighborhood) and the interchange neighborhood. The insert operator considers all those solutions as its neighbors that can be obtained by moving a job into another position. The swap operator considers those solutions as its neighbors that can be obtained by swapping a pair of jobs. When a local optima for both neighborhoods is reached, a shake procedure is performed to escape from that area of the search space. The shake consists of random insert movements of 14 jobs in the individual. In addition, $\mathrm{VNS}_{4}$ also starts from an initial solution provided by the constructive algorithm $\operatorname{LR}(n / m)$ [10].

As it has not been possible to obtain the original codes of AGA and $\mathrm{VNS}_{4}$ from the authors, we have implemented both proposals. The implementation of AGA and $\mathrm{VNS}_{4}$ was made honestly by following the indications of the respective papers. ${ }^{2}$ All the algorithms were coded in C++ programming language and the experimentation was conducted on a cluster of 20 nodes, each of them equipped with two Intel Xeon X5650 CPUs and 48 GB of memory.

Regarding the experimentation benchmark, AGA, VNS $_{4}$, and GM-EDA were tested using Taillard's [69] benchmark. This benchmark gathers 120 instances with the following configurations of $n$ jobs $\times m$ machines: $20 \times 5,20 \times 10$, $20 \times 20,50 \times 5,50 \times 10,50 \times 20,100 \times 5,100 \times 10,100$ $\times 20,200 \times 10,200 \times 20$, and $500 \times 20$ (ten instances of each).

## A. Parameter Settings

The parameters employed by GM-EDA are the following.

1) Population size is set to $10 n$.
2) Truncation selection mechanism is applied by choosing the best $10 \%$ of individuals $(n)$.
3) $10 n-1$ individuals are sampled at each new generation.
[^0]![img-2.jpeg](img-2.jpeg)

Fig. 4. Probability assigned to $\sigma_{0}$ for different $\boldsymbol{\theta}$ and $n$ values.
4) Elitism criteria is followed.
5) Restart mechanism: as seen in the literature, the elitism criteria and truncation selection implemented in this approach may lead the algorithm to loss diversity in the population. In order to prevent GM-EDA from getting stuck, a restart mechanism is applied when the fitness of all individuals in the population is the same. The restart mechanism generates a new population by applying a shake procedure over the best individual found so far. The shake procedure consists of five random insert movements of jobs around their current position (the five preceding and five succeeding locations are considered). The seed individual used is not added to the population in order to avoid super-individual effects.
6) The upper bound value for $\boldsymbol{\theta}$ was calculated by testing which value of $\theta_{\text {upper }}$ makes the GM-EDA perform the best over the first instance of each $n \times m$ configuration. Different $\theta_{\text {upper }}$ between $\theta_{\min }$ and $\theta_{\max }$ in steps of 0.1 were studied [the average value of ten repetitions of the GM-EDA was calculated (see Appendix)].
7) As regards the stopping criterion, AGA authors proposed setting an execution time of $n \times m \times 0.4 \mathrm{~s}$, as suggested in many other previous works. As this value is strongly related to the hardware used for the experiments and to the quality of the code, we think that the total number


[^0]:    ${ }^{2}$ Both programs, as well as supplementary material can be obtained from http://www.sc.ehu.es/ccwhayes/members/jceberio/GMEDA.html.

of evaluations is a much better criterion. In order to set a maximum number of evaluations, we run AGA for each instance for $n \times m \times 0.4 \mathrm{~s}$, recording the number of evaluations (see Appendix). These values were used throughout the experiments as the stopping criterion for GM-EDA, AGA, and VNS 4 .
The parameters of AGA and $\mathrm{VNS}_{4}$ have been set following the indications of their respective papers (with the exception of the stopping criterion).

## B. Taillard's Benchmark Results

Each algorithm-instance pair is run 20 times. The performance measure employed in our study is the average relative percentage deviation (ARPD)

$$
A R P D=\left(\sum_{i=1}^{20} \frac{\left(\text { Algorithm }_{i}-\text { Best) } \times 100}{\text { Best }}\right) / 20
$$

with Algorithm ${ }_{i}$ being the solution found by the algorithm in the $i$ th repetition and Best the best known solution for the instance under study. The ARPD results of the executions are summarized in Table I. Results in bold denote the algorithm that obtained the lowest relative error among the compared approaches. The results marked as $\left(^{*}\right)$ denote that, at least once, the best result (also shown in the table) has been achieved. The best results in italics denote new best known solutions.

As can be observed in Table I, the efficiency of the algorithms varies with respect to the size of the problem. For instances of size 20, AGA and $\mathrm{VNS}_{4}$ obtain the optimal results in all the cases. GM-EDA, meanwhile, achieves the optimal result in 22 instances of 30 . When comparing instances of $50,100,200$, and 500 , AGA clearly outperforms $\mathrm{VNS}_{4}$ and GM-EDA. ${ }^{3}$

Although the results of GM-EDA for the medium-large instances are noncompetitive, it is worth noting the ability of GM-EDA to achieve optimal solutions for the smallest size instances. Referring to the literature in the field, hybrid approaches are generally the best performing proposals when facing real problems, since they sum the abilities of the combined algorithms.

## VI. HyBRID GENERALIZED MALLowS EDA

In this section, we introduce the Hybrid GM-EDA (HGMEDA). The HGM-EDA is proposed as a two-stage algorithm, which in the first stage executes the GM-EDA previously introduced and in the second stage applies a VNS to the solution provided by GM-EDA. Since VNS is the most preferred algorithm seen in the literature with which hybridize, in the following section we introduce the specific design of the VNS that we propose for hybridization.

[^0]
## Algorithm 4 Variable Neighborhood Search (VNS)

```
Input: The best solution obtained by GM-EDA, \(\sigma_{\text {best }}\).
    \(\sigma^{C} \leftarrow \sigma_{\text {best }}\)
    Do \(\{\)
    Do \(\{\)
    \(\sigma^{S} \leftarrow \operatorname{LocalOpt}\left(N_{S}, \sigma^{C}\right)\)
    \(\sigma^{I} \leftarrow \arg \min _{\sigma \in N_{I}\left(\sigma^{S}\right)} f(\sigma)\)
    \(\sigma^{C} \leftarrow \sigma^{I}\)
    \} Until (no improvement) /* a local optimum is found */
    If \(\left(f\left(\sigma^{C}\right)<f\left(\sigma_{\text {best }}\right)\right)\) Then
        \(\sigma_{\text {best }} \leftarrow \sigma^{C}\)
    Else
        \(\sigma^{C} \leftarrow \sigma_{\text {best }}\)
        \(\operatorname{Shake}\left(\sigma^{C}\right)\)
    \} Until (MaxEvaluations are reached)
    Output: \(\sigma_{\text {best }}\)
```


## A. Variable Neighborhood Search

The VNS approach that we propose in this paper explores solutions combining the two most used neighborhoods in the literature: the interchange neighborhood and the insert neighborhood.

The interchange neighborhood $\left(N_{S}\right)$ considers that two permutations are neighbors if one is obtained by interchanging two elements in the other. It is formally defined as

$$
N_{S}(\sigma)=\left\{\sigma^{\prime} \mid \sigma_{k}^{\prime}=\sigma_{k}, \forall k \neq i, j, \sigma_{i}^{\prime}=\sigma_{j}, \sigma_{j}^{\prime}=\sigma_{i}\right\}
$$

On the other hand, two solutions are neighbors under the insert neighborhood $\left(N_{I}\right)$ if one is obtained by moving an element of the other solution to a different place. It is formally defined as

$$
\begin{aligned}
& \sigma^{\prime} \in N_{I}(\sigma) \Leftrightarrow \exists i, j \in\{1, \ldots, n\} \text { with } i \neq j \text { s.t. } \\
& \left\{\begin{array}{l}
\left(\sigma_{k}^{\prime}=\sigma_{k}, k<i \wedge k>j\right) \wedge, \\
\left(\sigma_{k}^{\prime}=\sigma_{k+1}, i \leq k<j\right) \wedge, \\
\sigma_{j}^{\prime}=\sigma_{i}
\end{array}\right. \\
& \left\{\begin{array}{l}
\left(\sigma_{k}^{\prime}=\sigma_{k}, k<i \wedge k>j\right) \wedge \\
\left(\sigma_{k}^{\prime}=\sigma_{k-1}, i<k \leq j\right) \wedge, \\
\sigma_{i}^{\prime}=\sigma_{j}
\end{array}\right.
\end{aligned}
$$

The VNS performs as follows (see pseudo-code in Algorithm 4). In a first step, a greedy local search procedure is carried out using the interchange neighborhood $\left(\operatorname{LocalOpt}\left(N_{S}, \sigma^{C}\right)\right.$ ) until a local optimum is reached $\left(\sigma^{S}\right)$. In the next step, the algorithm chooses the best neighbor of $\sigma^{S}$ in $N_{I}$.

The algorithm repeats this procedure until a local optimum is found for both neighborhoods. If the obtained solution $\sigma^{C}$ is better than that found by the VNS so far, the best solution $\left(\sigma_{\text {best }}\right)$ is updated. Next, a shake procedure, similar to that employed in the restart mechanism, is applied (this time ten jobs are shifted instead of five). The whole process is repeated until the maximum number of evaluations is reached.


[^0]:    ${ }^{3}$ The results reported by Costa et al. [19] do not match those observed in this experimentation. The authors in their paper report better results for $\mathrm{VNS}_{4}$ and worse results for AGA.

TABLE I
ARPD ReSultS for TAILlard's Benchmark Instances. ReSultS in Bold DENTE the Approach With the Lowest ARPD. ReSultS MAKKED * DENOTE THE OPTIMUM OR BEST VALUE THAT WAS ACHIEVED AT LEAST ONCE AMONG THE 20 REPETITIONS PERFORMED. BEST RESULTS IN ITALICS DENOTE NEW BEST KNOWN SOLUTIONS


## B. Experimentation

In order to study the performance of HGM-EDA, we repeat the previous experimentation.

1) Parameter Tuning: Since HGM-EDA is a two stage algorithm, the number of evaluations assigned to each stage is set to half of the maximum allowed. In addition, the number of restarts allowed for GM-EDA has been limited to $10 n$ (these parameters have been decided without any previous experiment). In the case that the criterion on restarts is fulfilled before half of the evaluations have run, the remaining evaluations will be performed by the VNS as well. The rest of the parameters are set as described in Section V.
2) Taillard's Benchmark Results: We evaluate AGA, $\mathrm{VNS}_{4}$, GM-EDA, VNS (the version used in the hybrid approach), and HGM-EDA algorithms over the instances of Taillard's benchmark. Each algorithm - instance pair is run 20 times. The best result and ARPD values are summarized in Table I.

According to those results, from the 120 Taillard's benchmark instances tested, HGM-EDA finds the best TFT solution for 85 instances (for which 48 are new best known solutions), AGA for 70 and $\mathrm{VNS}_{4}$ for 31 . Regarding the ARPD results, AGA is the best in 88 instances, HGM-EDA in 62, and $\mathrm{VNS}_{4}$ in 30 out of 120 instances.

In order to state whether there exist statistical differences among the results, we applied a nonparametric Friedman's test to the best TFT results obtained by the AGA, $\mathrm{VNS}_{4}$, and HGM-EDA algorithms among the 20 repetitions for each $n \times m$ configuration. A level $\alpha=0.05$ of significance was set. The statistical test reported significant differences between the algorithms for some configuration types. Therefore, a post-hoc method was used to carry out all pairwise comparisons and determine which algorithms stand out from the rest of the approaches. In particular, Shaffer's static procedure is used, as suggested for such cases in [70]. Again, the significance level was fixed to $\alpha=0.05$. The statistical analysis confirmed the following points.

1) No significative difference was found for instances of size 20 between AGA, $\mathrm{VNS}_{4}$, and HGM-EDA.
2) AGA and HGM-EDA perform better than $\mathrm{VNS}_{4}$ for instances with 50 and 100 jobs. However, no statistical differences were found to distinguish between AGA and HGM-EDA.
3) HGM-EDA is the best algorithm for solving instances of 200 jobs, followed by AGA, with $\mathrm{VNS}_{4}$ in third place.
4) Finally, AGA and $\mathrm{VNS}_{4}$ outperform HGM-EDA for instances of size 500 . However, the test does not determine which of them is better.
To demonstrate that the contribution of GM-EDA is essential for an efficient performance of the hybrid approach, VNS was also evaluated independently in this experiment. The obtained results prove that, when run separately, each stage of the hybrid approach, GM-EDA and VNS, does not perform as well as when they are run combined.
5) Random Benchmark Results: From the previous experiments, it can be observed that HGM-EDA performs better as the size of the problem enlarges. However, for problems of
size 500, HGM-EDA does not work as expected. In order to analyze this behavior, we decided to create new instances to fill the gap between 200 and 500. 100 new instances were proposed with the following configurations: $250 \times 10,250$ $\times 20,300 \times 10,300 \times 20,350 \times 10,350 \times 20,400 \times$ $10,400 \times 20,450 \times 10$, and $450 \times 20$ (ten instances for each configuration). ${ }^{4}$ The processing times of the jobs were generated uniformly at random (integer values between 1 and 100 as reported by Taillard [69]).

We executed 20 independent runs. $\theta_{\text {upper }}$ and the maximum number of evaluations for the stopping criterion were calculated following the same procedure explained for Taillard's benchmark (see the Appendix).

According to the results (see Table II), HGM-EDA obtains the best TFT solution for 67 instances and AGA for 33 . On the other hand, $\mathrm{VNS}_{4}$ was not successful in any of the cases. Regarding the ARPD, HGM-EDA is the best in 61 instances out of 100 and AGA in 39.

In order to state whether there exist statistical differences among the algorithms, we applied the same statistical test as before, obtaining the following results.

1) HGM-EDA is the best algorithm for solving instances of 250,300 , and 350 jobs, followed by AGA, with $\mathrm{VNS}_{4}$ in third place.
2) AGA and HGM-EDA outperform $\mathrm{VNS}_{4}$ for instances of $400 \times 10$. However, no statistical differences were found to distinguish between AGA and HGM-EDA.
3) For configurations $400 \times 20$ and $450 \times 10$, AGA is statistically the best, followed by $\mathrm{VNS}_{4}$, and HGM-EDA in third position.
4) Finally, AGA and $\mathrm{VNS}_{4}$ outperform HGM-EDA for instances of $450 \times 20$. However, the test does not determine which of them is better.

## C. Additional Experimentation

As previously mentioned, in this paper we considered optimizing PFSP with respect to the TFT due to its complexity and relevance for the current production environments. However, taking into account that the makespan is also an interesting criterion when optimizing the PFSP, we decided to carry out some additional executions with GM-EDA and HGM-EDA for the Taillard's PFSP instances with the makespan criterion. The results were summarized in a short report and uploaded to the website as additional material.

Considering that the complexity of the proposed algorithm is higher than that of its competitors, we carried out some additional experiments using the execution time as the stopping criterion. A report with the results and some conclusions was uploaded at the Website as additional material.

## VII. DISCUSSION

In the previous section, we saw that HGM-EDA is a strong alternative to optimize PFSP. However, the unexpected performance observed for the largest instances deserves a

[^0]
[^0]:    ${ }^{4}$ Both Taillard's benchmark and random benchmark can be obtained from http://www.sc.ehu.es/ccwbayes/members/jceberio/GMEDA.html.

TABLE II
ARPD ReSults for TAillard's Benchmark Instances. ReSults in Bold Denote the Approach With the Lowest ARPD. ReSults Marked * Denote the Optimum or Best Value that was Achieved at Least Once Among the 20 Repetitions Performed


thorough study. In this section we go deeper into this topic and propose methods to improve the efficiency of HGM-EDA.

## A. Why Does the Performance of HGM-EDA Decrease for the Largest Instances?

In Table II, we can see that the fitness difference between HGM-EDA and AGA increases from configuration $400 \times 20$ onward, which favors AGA. Since HGM-EDA is based on GM-EDA, we analyze two aspects of HGMEDA: the performance of GM-EDA against AGA and the contribution of each stage of the hybrid approach to the optimization.

To study the performance of GM-EDA versus AGA, in Fig. 5 the ARPD between GM-EDA and AGA is introduced.

This time, for each instance $i$ within the set of instances of a given configuration, we consider the best result of the 20 runs performed by GM-EDA and AGA, called $G M-E D A_{i}^{\text {best }}$ and $A G A_{i}^{\text {best }}$, respectively. Then, we calculate the ARPD for each $n \times m$ configuration (note that each configuration contains a set of ten instances)

$$
\mathrm{ARPD}=\left(\sum_{\mathrm{i}=1}^{10} \frac{\left(\mathrm{GMEDA}_{\mathrm{i}}^{\text {best }}-\mathrm{AGA}_{\mathrm{i}}^{\text {best }}\right) \times 100}{\mathrm{AGA}_{\mathrm{i}}^{\text {best }}}\right) / 10
$$

According to the results, GM-EDA shows a regular ARPD below 0.02 with respect to AGA up to configuration $350 \times 10$. The low deviation described for such instances coincides with the good performance of HGM-EDA. However, the results

![img-3.jpeg](img-3.jpeg)

Fig. 5. Average relative percentage deviation between the best results obtained by GM-EDA and AGA in the ten instances of each configuration.
![img-4.jpeg](img-4.jpeg)

Fig. 6. Contribution ratios performed by each stage of HGM-EDA: GMEDA and VNS. Ratios were calculated averaging results obtained from 20 independent runs over the first instance of each configuration $n \times m$. Note that the ratio axis is only shown from 0.5 to 1 .
for configurations from $400 \times 20$ onward show a dramatic increase of ARPD. In fact, the largest differences in Fig. 5 match the poor results seen for HGM-EDA for such instances.

The results observed suggest that HGM-EDA relays its performance to the ability of GM-EDA to find promising solutions. As HGM-EDA is a two-stage algorithm, in the following lines we propose a study of the contribution ratio of each stage on the final solution. For this analysis, we consider three particular solutions from HGM-EDA: the best individual of the first population of GM-EDA ( $\mathrm{Sol}_{\text {init }}$ ), the solution returned by GM-EDA when the first stage finishes $\left(\mathrm{Sol}_{\text {GMEDA }}\right)$, and the final solution returned by the VNS in the second stage of the HGM-EDA (Sol $_{\text {final }}$ ). The contribution ratios (CR) are computed as $C R_{\text {GMEDA }}=\left(\text { Sol }_{\text {init }}-\text { Sol }_{\text {GMEDA }}\right) / \text { Sol }_{\text {final }}$ and $C R_{\text {VNS }}=\left(\text { Sol }_{\text {GMEDA }}-\text { Sol }_{\text {final }}\right) / \text { Sol }_{\text {final }}$. The ratios were calculated averaging the results obtained from 20 independent runs over the first instance of each configuration instance set. The results are shown in Fig. 6.

The plotted results support the conclusion that we had come to previously: GM-EDA is the stage of the algorithm that conditions the performance of HGM-EDA. While improvement ratios for instances between 20 and 200 jobs show a
![img-5.jpeg](img-5.jpeg)

Fig. 7. Convergence ratio of average $\boldsymbol{\theta}$ values to $\theta_{\text {upper }}$ at the end of the execution. First instance of each configuration type was selected.
regular contribution around 0.9 for GM-EDA, the results for the instances from $400 \times 20$ onward are significantly lower.

## B. Why Does GM-EDA Become Less Competitive Than AGA for the Largest Instances?

Since the GM model determines the effect of GM-EDA, we analyze the convergence of the probabilistic model when optimizing the largest instances. As mentioned in Section IV, the vector $\boldsymbol{\theta}$ determines the exploration or intensification behavior of the GM model when optimizing. Therefore, in this new experiment, we examine the average value of the dispersion parameters $\boldsymbol{\theta}$ obtained at the end of the executions. In this case, the first instance of each configuration $n \times m$ was studied. For comparison purposes, the results are normalized to the range $[0,1]$ by dividing the average $\boldsymbol{\theta}$ calculated for each instance, with the $\theta_{\text {upper }}$ set in each case.

According to the results shown in Fig. 7, in instances up to $300 \times 10$, the average $\boldsymbol{\theta}$ converged to the $\theta_{\text {upper }}$ set. However, in larger instances, the average $\boldsymbol{\theta}$ values do not achieve values higher than 0.7 in each case. This means that the convergence of the model did not even reach $70 \%$ of the upper bound fixed to each configuration type.

This experiment suggests that the GM model learned was in an exploration phase (taking into account Fig. 4) when stopped, instead of intensifying around the promising area.

Alternatively, examining the initialization of AGA in detail, we realized that the constructive heuristic employed, $\operatorname{LR}(n / m)$ (also in $\mathrm{VNS}_{4}$ ), has a decisive contribution when solving largescale instances. Some preliminary experiments showed that the performance of AGA and $\mathrm{VNS}_{4}$ was significantly worse when $\operatorname{LR}(n / m)$ was removed from the procedure.

In order to state what the real advantage of including $\operatorname{LR}(\mathrm{n} / \mathrm{m})$ is, we compare the intermediate result calculated by $\operatorname{LR}(\mathrm{n} / \mathrm{m})$ as the first stage of AGA and that of GM-EDA. We define the ARPD between LR and GM-EDA as

$$
\mathrm{ARPD}=\left(\sum_{\mathrm{i}=1}^{10} \frac{\left(\mathrm{LR}_{\mathrm{i}}-\mathrm{GMEDA}_{\mathrm{i}}\right) \times 100}{\mathrm{GMEDA}_{\mathrm{i}}}\right) / 10
$$

$\left(\mathrm{GMEDA}_{\mathrm{i}}\right.$ denotes the average of the fitness value obtained by the GM-EDA in the 20 repetitions.) The results are shown in

![img-6.jpeg](img-6.jpeg)

Fig. 8. Average relative percentage deviation of LR with respect to GMEDA performed at the first stage of HGM-EDA (the average fitness value of 20 repetitions was selected). The ARPD of the ten instances of each configuration was calculated. Note that the ARPD axis is shown from -0.12 to 0.12 . Instances with histograms above 0 denote that the solutions obtained by GM-EDA are, on average, better than those achieved by $\operatorname{LR}(n / m)$ and the opposite when the results obtained are below 0 .

Fig. 8. The values used to calculate the ARPD are the average values of 20 repetitions over each instance.

The results report that the performance of GM-EDA is better than that of $\operatorname{LR}(n / m)$ for instances up to $400 \times 10$. However, for larger instances $\operatorname{LR}(n / m)$ is better. The results suggest that the poor performance seen for larger instances might also be motivated by the random initialization of the initial population of GM-EDA.

## C. Guided HGM-EDA

Previous analysis suggests that the random initialization and the lack of enough evaluations could be the main reasons for the unexpected performance of HGM-EDA in the largest instances (instances from $350 \times 20$ onward). Inspired by the state-of-the-art algorithms that we compared it with, we propose a method for guiding the initialization of the first population, based on $\operatorname{LR}(n / m)$.

As with every constructive algorithm, $\operatorname{LR}(n / m)$ measures the preference to append a job to the current partial solution. For each nonscheduled job, the heuristic calculates an index value that considers the increase of the TFT when the nonscheduled job is appended to the partial solution, and the increase of the TFT to the solution by the averaged processing times of the remaining jobs. The job with the lowest index value is selected to be appended to the partial solution.

In this case, in order to guide the initialization of the first population, we propose a modification of the $\operatorname{LR}(n / m)$ to transform the constructive heuristic into a nondeterministic proposal. A nondeterministic proposal allows the presumable provision of a different seed individual at each repetition of the algorithm. The modification proposed replaces the topranking job selection by sampling a probability distribution inversely proportional to the index value of the jobs in the ranking.

In order to analyze the impact of the guided initialization and the premature stopping of GM-EDA, we compare AGA, HGM-EDA, and Guided HGM-EDA over the first instance

TABLE III
$\theta_{\text {upper }}$ Values and Maximum Number of Evaluations for TAILlard's Benchmark


TABLE IV
$\theta_{\text {upper }}$ Values and Maximum Number of Evaluations for the RANDOM BENCHMARK


of the configurations $400 \times 20,450 \times 10,450 \times 20$, and $500 \times 20$. The algorithms are run from one to eight times, the maximum number of evaluations specified in Appendix. The results are shown in Fig. 9.

It can be seen that Guided HGM-EDA achieves better results than HGM-EDA and outperforms the results of AGA when extending the number of evaluations employed. The successful results achieved by Guided HGM-EDA against AGA and HGM-EDA support the potential of the EDA introduced in this paper and confirm the determinant effect of implementing a guided initialization when dealing with large size instances.

## VIII. CONCLUSION

In this paper, we presented a novel algorithm for dealing with permutation-based problems, called GM-EDA. GM-EDA introduces a probabilistic distance-based ranking exponential model. As this manuscript is the first serious attempt to introduce an EDA of such characteristics, in order to demonstrate the efficiency of the proposed algorithm, it was tested on the well-known permutation flowshop scheduling problem. In particular, a hybrid version of the GM-EDA was proposed (GM-EDA + VNS) to obtain state-of-the-art results.

The experiments carried out showed that the hybrid version of the GM-EDA (HGM-EDA) is the best algorithm for solving the PFSP-TFT. From 220 instances tested (Taillard's and random benchmarks), HGM-EDA obtained the best solution

![img-7.jpeg](img-7.jpeg)

Fig. 9. Average fitness results of ten runs of AGA, HGM-EDA, and guided HGM-EDA over the first instance of the configurations $400 \times 20,450 \times 10$, $450 \times 20$, and $500 \times 20$. The algorithms have been run for one to eight times the maximum number of evaluations (max_eval) specified in the Appendix.
for 152 instances. The analysis of the results concluded that the success of HGM-EDA is due to the ability of GM-EDA to find optimal regions in the search space. Furthermore, the experiments proved that employing a heuristic for initializing the algorithm is preferable than a random initialization, mainly when solving large size instances.

Additional experiments revealed that GM-EDA and HGMEDA are the most time-consuming algorithms among the studied approaches. However, further executions demonstrated that HGM-EDA is still very competitive compared with its competitors when they are executed with the same running time.

The incorporation of the GM model to the framework of EDAs leaves many trends that are worth extending in future work. In the following paragraphs we will briefly mention some of them.

As introduced previously, the GM model is defined by two parameters: the consensus ranking $\sigma_{0}$ and the vector of spread parameters $\boldsymbol{\theta}$. In Section III, we highlighted the difficulty of calculating these parameters exactly, and we proposed approximation methods that permit us to use the GM model in EDAs. However, we believe that there is still room for improvement. More advanced methods for calculating the $\sigma_{0}$ or self-adapting procedures for the estimation of $\boldsymbol{\theta}$ may lead GM-EDA to improve its efficiency.

Another feature of the GM model that deserves a deeper study is that related to how the unimodal property of the model behaves when solving problems/instances with many
global optima. In this sense, mixtures of Mallows models [71] might be considered to optimize different areas of the landscape separately.

In addition, in this proposal, Kendall's $\tau$ distance was considered due to its decomposable properties, which allow us to factorize the GM model, and thus, learn and sample the model efficiently. However, there exist many other metrics that could be developed, such as Cayley, Ulam, or Hamming [72]. In fact, finding the best distance for approaching a certain permutation problem is challenging research.

The inclusion of the information of the instance into the GM model is another interesting issue. Due to the characteristics of the GM model, the inclusion procedure of external information into the model is relatively easy. However, finding the relevant information in the instance is a very hard task.

Regarding the approach for solving the PFSP, there are also other points that should be analyzed to obtain better results: the percentage of evaluations used in each stage of the HGM-EDA, the effect of developing more elaborate population initialization methods, the shake method used in the restart scheme, or the selection of the neighborhoods for the proposed VNS algorithm as a part of HGM-EDA.

Finally, with the aim of ratifying these initial results, we consider it interesting to test the GM-EDA on a wider set of permutation-based problems, such as the quadratic assignment problem or the linear ordering problem.

## APPENDIX

## EXECUTION PARAMETERS

Tables III and IV show the maximum number of evaluations and $\theta_{\text {upper }}$ values used in the experimentation for Taillard's and random benchmarks, respectively. $\theta_{\text {upper }}$ values have been obtained testing different values of $\theta$, starting at $\theta_{\min }$ and ending at $\theta_{\max }$, in steps of 0.1 . Note that only the first instance of each configuration was used to look for the most adequate parameter values.
