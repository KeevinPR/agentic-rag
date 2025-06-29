# Analysis of Computational Time of Simple Estimation of Distribution Algorithms 

Tianshi Chen, Student Member, IEEE, Ke Tang, Member, IEEE,<br>Guoliang Chen, and Xin Yao, Fellow, IEEE

NOTE: This paper was part of the Special Issue on Evolutionary Algorithms Based on Probabilistic Models that should have appeared in the IEEE Transactions on Evolutionary Computation, Vol. 13, No. 6, December 2009 .

Abstract-Estimation of distribution algorithms (EDAs) are widely used in stochastic optimization. Impressive experimental results have been reported in the literature. However, little work has been done on analyzing the computation time of EDAs in relation to the problem size. It is still unclear how well EDAs (with a finite population size larger than two) will scale up when the dimension of the optimization problem (problem size) goes up. This paper studies the computational time complexity of a simple EDA, i.e., the univariate marginal distribution algorithm (UMDA), in order to gain more insight into EDAs complexity. First, we discuss how to measure the computational time complexity of EDAs. A classification of problem hardness based on our discussions is then given. Second, we prove a theorem related to problem hardness and the probability conditions of EDAs. Third, we propose a novel approach to analyzing the computational time complexity of UMDA using discrete dynamic systems and Chernoff bounds. Following this approach, we are able to derive a number of results on the first hitting time of UMDA on a well-known unimodal pseudo-boolean function, i.e., the LeadingOnes problem, and another problem derived from LeadingOnes, named BVLeadingOnes. Although both problems are unimodal, our analysis shows that LeadingOnes is easy for the UMDA, while BVLeadingOnes is hard for the UMDA. Finally, in order to address the key issue of what problem characteristics make a problem hard for UMDA, we discuss in depth the idea of "margins" (or relaxation). We prove theoretically that the UMDA with margins can solve the BVLeadingOnes problem efficiently.

Index Terms- Computational time complexity, estimation of distribution algorithms, first hitting time, heuristic optimization, univariate marginal distribution algorithms.

[^0]
## I. INTRODUCTION

ESTIMATION of distribution algorithms (EDAs) [25], [28] are population-based stochastic algorithms that incorporate learning into optimization. Unlike evolutionary algorithms (EAs) that rely on variation operators to produce offspring, EDAs create offspring through sampling a probabilistic model that has been learned so far in the optimization process. Obviously, the performance of an EDA depends on how well we have learned the probabilistic model that tries to estimate the distribution of the optimal solutions. The general procedure of EDAs can be summarized in Table I. In recent years, many variants of EDAs have been proposed. On one hand, they have been shown experimentally to outperform other existing algorithms on many benchmark test functions. On the other hand, there were also experimental observations that showed EDAs did not scale well to large problems. In spite of a large number of experimental studies, theoretical analysis of EDAs has been few, especially on the computational time complexity of EDAs.

The importance of the time complexity of EDAs was recognized by several researchers. Mühlenbein and SchlierkampVoosen [31] studied the convergence time of constant selection intensity algorithms on the ONEMAX function. Later, Mühlenbein [27] studied the response to selection equation of the univariate marginal distribution algorithm (UMDA) on the ONEMAX function through experiments as well as theoretical analysis. Pelikan et al. [32] studied the convergence time of Bayesian optimization algorithm on the ONEMAX function. Rastegar and Meybodi [35] carried out a theoretical study of the global convergence time of a limit model of EDAs using drift analysis, but they did not investigate any relations between the problem size and computation time of EDAs. In addition to convergence time, the time complexity of EDAs can be measured by the first hitting time (FHT), which is defined as the first time for a stochastic optimization algorithm to reach the global optimum. Although recent work pointed out the significance of studying the FHT of EDAs [29], [33], few results have been reported. Droste's results [8] on the compact genetic algorithm (cGA) are a rare example. He analyzed rigorously the FHT of cGA with population size 2 [14] on linear functions. The other example is González's doctoral dissertation [13], where she analyzed the FHT of EDAs on the pseudo-boolean injective function using the analytical Markov chain framework proposed by He and Yao [17]. González [13] proved an important result that the worst-case mean FHT


[^0]:    Manuscript received November 26, 2007; revised October 28, 2008, February 5, 2009, and May 10, 2009. Current version published January 29, 2010. This work was supported in part by the National Natural Science Foundation of China under Grants 60533020 and U0835002, the Fund for Foreign Scholars in the University Research and Teaching Programs (111 Project) in China under Grant B07033, and an Engineering and Physical Science Research Council Grant EP/C520696/1 in the U.K.
    T. Chen, K. Tang, and G. Chen are with the Nature Inspired Computation and Applications Laboratory, School of Computer Science and Technology, University of Science and Technology of China, Hefei, Anhui 230027, China (e-mail: cetacy@mail.ustc.edu.cn; ketang@ustc.edu.cn; glchen@ustc.edu.cn). X. Yao is with the Nature Inspired Computation and Applications Laboratory, School of Computer Science and Technology, University of Science and Technology of China, Hefei, Anhui 230027, China, and also with the Center of Excellence for Research in Computational Intelligence and Applications, School of Computer Science, University of Birmingham, Edgbaston, Birmingham B15 2TT, U.K. (e-mail: x.yao@cs.bham.ac.uk). Digital Object Identifier 10.1109/TEVC.2009.2040019

TABLE I
GENERAL PROCEDURE OF EDA

```
\(\xi_{1} \leftarrow N\) individuals are generated by the initial probability distribution;
    \% Beginning of the 0th generation.
\(t \leftarrow 1 ; \quad \%\) End of the 0th generation.
REPEAT
\(\xi_{t}^{(s)} \leftarrow M\) individuals are selected from the \(N\) individuals in \(\xi_{t} ;\)
    \% Beginning of the \(t\) th generation \((t \geq 1)\).
    \(p\left(x \mid \xi_{t}^{(s)}\right) \leftarrow\) The joint probability distribution is estimated from \(\xi_{t}^{(s)}\);
    \(\xi_{t+1} \leftarrow N\) individuals are sampled from \(p\left(x \mid \xi_{t}^{(s)}\right)\);
    \(t \leftarrow t+1 ; \quad \%\) End of the \(t h\) generation.
UNTIL THE STOPPING CRITERION IS MET.
```

$\xi_{t}$ and $\xi_{t}^{(s)}$ are the populations before and after selection at the $t$ th generation.
is exponential in the problem size for four commonly used EDAs. However, no specific problem was analyzed theoretically. Instead, González et al. [10] studied experimentally the mean FHT of three different types of EDAs, including the UMDA, on the Linear function, LEADINGONES function [4], [7], [16], [37], and UnIMAX (long-path) function [22].

This paper concerns theoretical analysis of the FHT of EDAs on the optimization problems with a unique global optimum. First, we provide a classification of problem hardness based on the FHT of EDAs, so that we can relate the problem characteristics to EDAs. This is very important for investigating the principles of when to use which EDAs for a given problem. Given such a classification (with respect to an EDA), we then investigate the relationship between EDAs probability conditions and problem hardness. Specifically, the time complexity of a simple EDA, the UMDA with truncation selection, is analyzed on two unimodal problems. The first problem is the LEADINGONES problem [37], which has frequently been studied in the field of time complexity analysis of EAs [7], [16]-[18]. The other problem is a variant of LEADINGONES, namely BVLEADINGONES.

Our analysis can be briefly summarized from two aspects. First, we propose a general approach to time complexity analysis of EDAs with finite populations. In the domain of EDAs, lots of theoretical results are based on infinite population assumption (e.g., [3], [11], [45]), while few consider the more realistic scenario that employs finite populations. Though we restrict our analysis to UMDA, our approach may also be useful for other EDAs. Second, both LEADINGONES and BVLEADINGONES are unimodal problems, and hence are usually expected to be easy for EDAs [11]. Our analysis confirms that LEADINGONES is easy for the UMDA studied. However, we interestingly find that BVLEADINGONES is hard for the UMDA. To deal with this issue, we relax the UMDA by the so-called margins, and prove that BVLEADINGONES becomes easy for this relaxed version of UMDA.

The rest of the paper is organized as follows. Section II discusses why FHT is more appropriate for time complexity analysis of EDAs and presents the classification of problem hardness and the corresponding probability conditions for EDAs. Section III presents the new approach to analyzing EDAs with finite populations and describes the UMDA studied in this paper. Then, UMDA is analyzed on LEADINGONES and BVLEADINGONES problems in Sections IV and V, respectively. Section VI studies the relaxation form of the UMDA on
the BVLEADINGONES problem. Finally, Section VII concludes the paper.

## II. Time Complexity Measures for EDAs

## A. How to Measure the Time Complexity of EDAs

The concept of "convergence" is often used to measure the limit behaviors of EAs, including EDAs, which was derived from the concept of convergence of random sequences [37]. For EDAs, the following formal definition of "convergence" was given by Zhang and Mühlenbein [45]:

If $\lim _{t \rightarrow \infty} \bar{F}(t)=g^{*}$ holds for a given EDA, where $\bar{F}(t)$ is the average fitness of individuals in the $t$ th generation and $g^{*}$ is the fitness of the global optimum, then we say that the EDA converges to the global optimum.
There has been some work concerning such convergence of EDAs [12], [30]. It is worth noting that the above definition of convergence requires all individuals of a population to reach the global optimum. If we assume that an EDA on a problem converges to the global optimum, we can then measure the EDAs time complexity using the minimal number of generations that is needed for it to converge. This concept is called the convergence time (CT), denoted by $T$ in this paper. For EDAs, the CT is formally defined by

$$
T \triangleq \min \left\{t ; p\left(x^{* \mid} \mid \xi_{t}^{(s)}\right)=1\right\}
$$

where $x^{*}$ is the global optimum of a given problem, and $\xi_{t}^{(s)}$ is the population after selection at the $t$ th generation. $p\left(x^{*} \mid \xi_{t}^{(s)}\right)$ is the estimated probability (of generating $x^{*}$ ) by the EDA at the $t$ th generation.

In addition to CT, the FHT is also a commonly used concept for measuring the time complexity of EAs [16], [17]. The FHT [16], [17], [43], denoted by $\tau$, is defined for the general procedure of EDA shown in Table I

$$
\tau \triangleq \min \left\{t ; x^{*} \in \xi_{t+1}\right\}
$$

where $\xi_{t+1}$ is the population generated at the end of $t$ th generation. In the domain of EA, the FHT records the smallest number of generations needed to find the optimum, which is by a factor $N$ smaller than another commonly used measure named number of fitness evaluations, where $N$ is the number of fitness evaluations in every generation [9]. As González pointed out in [13], the FHT can also be used to measure the time complexity of EDAs.

Since EDAs are stochastic algorithms, both CT $T$ and FHT $\tau$ are random variables. Noting that the FHT measures the time for the global optimum to be found for the first time, thus the CT is no smaller than FHT

$$
T \geq \tau
$$

which implies a natural way to bound CT from below by FHT or bound FHT from above by the CT.

In practical optimization, we are most interested in the time spent in finding the global optimum, not in waiting for the whole population to converge to the global optimum. Hence, the FHT is a better measure for analyzing the time complexity of the EDAs. It is worth noting that for a given EDA on a problem, it may have a small FHT but large CT. In other words, the population may take a long time (even infinite) to converge to the global optimum. In such cases, the analysis of FHT is still valid while the analysis of CT is rather uninteresting. It is possible that an EDA could find the global optimum efficiently (in polynomial time), but the population does not converge to the global optimum. We will discuss such an example in Section VI.

## B. Probability Conditions for EDA-Hardness

In order to understand better the relationship between problem characteristics and algorithmic features of an EDA, we introduce a problem classification for a given EDA. However, we should introduce some notations first.

Denote $\operatorname{Poly}(n)$ as the polynomial function class of the problem size $n$ and $\operatorname{SuperPoly}(n)$ as the super-polynomial function class of the problem size $n$. For a function $f(n)$ (where $f(n)>1$ always holds, and when $n \rightarrow \infty, f(n) \rightarrow \infty$ ), denote the following:

1) $f(n)<\operatorname{Poly}(n)$ and $g(n)=\frac{1}{f(n)} \succ \frac{1}{\operatorname{Poly}(n)}$ if and only if $\exists a, b \in \mathbb{R}^{*}, n_{0} \in \mathbb{N}: \forall n>n_{0}, f(n) \leq a n^{b}$;
2) $f(n) \succ \operatorname{SuperPoly}(n)$ and $g(n)=\frac{1}{f(n)} \prec \frac{1}{\operatorname{SuperPoly}(n)}$ if and only if $\forall a, b \in \mathbb{R}^{*}: \exists n_{0} \in \mathbb{N}: \forall n>n_{0}, f(n)>a n^{b}$.
Based on the above definitions, we know that " $<$ " and " $>$ " imply " $<$ " and " $>$ " respectively, when $n$ is sufficiently large. Poly(n) [SuperPoly(n)] implies that there exists a monotonically increasing function that is polynomial (super-polynomial) in the problem size $n$. Note that $g(n)=\frac{1}{f(n)} \in(0,1)$, and its asymptotic form $g(n) \succ \frac{1}{\operatorname{Poly}(n)}$ or $g(n) \prec \frac{1}{\operatorname{SuperPoly}(n)}$, can be used to measure the asymptotic order of a probability (e.g., the probability of generating a certain individual), since a probability always takes its value in the interval $[0,1] .{ }^{1}$ Then we provide the following problem classification for a given EDA.
${ }^{1}$ For $g(n) \in[0,1]$, there are more detailed asymptotic orders in the interval $[0,1]:$
3) $\frac{g(n) \prec \frac{1}{\operatorname{SuperPoly}(n)}}{2) \frac{1}{\operatorname{Poly}(n)} \prec g(n) \prec 1-\frac{1}{\operatorname{Poly}(n)} \quad\left[\right.$ if and only if $\left.\exists a_{1}, b_{1}, a_{2}, b_{2} \in \mathbb{R}^{*}\right]$, $n_{0}, n_{1} \in \mathbb{N}: \forall n>\max \left\{n_{0}, n_{1}\right\}, 1 /\left(a_{1} n^{b_{1}}\right) \leq g(n) \leq 1-1 /\left(a_{2} n^{b_{2}}\right)\right]$;
4) $g(n)>1-\frac{1}{\operatorname{SuperPoly}(n)}\left[\right.$ if and only if $\forall a, b \in \mathbb{R}^{*}: \exists n_{0} \in \mathbb{N}: \forall n>n_{0}$, $g(n) \geq 1-1 /\left(a n^{b}\right)$
If necessary, these detailed asymptotic orders can be obtained by considering the regions $c \pm \frac{1}{\operatorname{Poly}(n)}$ and $c \pm \frac{1}{\operatorname{SuperPoly}(n)}$, where $0<c<1$.
5) EDA-easy Class. For a given EDA, a problem is EDA-easy if, and only if, with the probability of $1-1 /$ Super Poly( $n$ ), the FHT needed to reach the global optimum is polynomial in the problem size $n$.
6) EDA-hard Class. For a given EDA, a problem is EDAhard if, and only if, with the probability of $1 / \operatorname{Poly}(n)$, the FHT needed to reach the global optimum is superpolynomial in the problem size $n$.
The above classification can be considered as a direct generalization of the following EA-hardness classification for EAs proposed by He and Yao [18].
7) EA-easy Class. For a given EA, a problem is EA-easy if, and only if, the mean FHT needed to reach the global optimum is polynomial in the problem size $n$.
8) EA-hard Class. For a given EA, a problem is EA-hard if, and only if, the mean FHT needed to reach the global optimum is super-polynomial in the problem size $n$.
We see that He and Yao's classification for EAs is based on mean FHT, while our classification for EDAs concerns more detailed characteristics of the probability distribution of FHT. Given a problem, if the FHT of an EDA is polynomial with a probability super-polynomially close to 1 (the probability will be called "an overwhelming probability" in the following parts of the paper), then we can say that in most of independent runs, the EDA can find the optimum of the problem efficiently. On the other hand, if the FHT of an EDA is super-polynomial with a probability that is polynomially large. i.e., $1 / \operatorname{Poly}(n)$, then it is very likely that the EDA cannot find the optimum of the problem efficiently. A similar idea can be found in [42], which defined efficiency measures for randomized search heuristics.

From the definition of expectation in probability theory, we know that for an algorithm, the problems belonging to the EDA-hard class in our classification will still be hard under the classification based on mean FHT. But our classification defines EDA-easy differently from the classification based on mean FHT. In practice, it is possible that an EDA finds the optimum efficiently in most of the independent runs, while spends extremely long time in the other runs. This kind of problems will considered to be "hard" cases if using mean FHT for classification. However, in our classification, such problems are considered to be easy cases, which is more likely to fit the practitioners' point of view.

We now establish conditions under which a problem is EDA-hard (or EDA-easy) for a given EDA. Let $\mathbb{P}(\tau=t)$ $(t \in \mathbb{N})$ be the probability distribution of the FHT, which is determined by the probabilistic model at the $t$ th generation. An EDA can be regarded as a random process $K=\left\{K_{t}: t \in \mathbb{N}\right\}$, where $K_{t}$ is the probabilistic model (including the parameters) maintained at the $t$ th generation. Obviously, $K_{t}$ implies the probability of generating the global optimum in one sampling at the $t$ th generation, denoted by $P_{t}^{*}$

$$
\forall t \in \mathbb{N}: K_{t} \vdash P_{t}^{*}
$$

Meanwhile, to obtain the probability distribution of the FHT $\tau$, we let $P_{t}^{*}$ be the probability of generating the global optimum in one sampling at the $t$ th generation, conditional on the event $\tau \geq t$ (i.e., the global optimum has not been

generated before the $t$ th generation). Consequently, we obtain the following lemma:

Lemma 1: The probability distribution of the FHT $\tau$ satisfies

$$
\forall t \geq 0: \mathbb{P}(\tau=t)=\left(1-\left(1-P_{t}^{\prime}\right)^{N}\right) \prod_{j=0}^{t-1}\left(1-P_{j}^{\prime}\right)^{N}
$$

Proof: Let $x^{*}$ be the global optimum. As Table I and (2), we also let $\xi_{t+1}$ be the generated population at the end of $t$ th generation $(t \in \mathbb{N})$. According to the FHT defined in (2), for any $t \in \mathbb{N}^{+}$we have

$$
\begin{aligned}
& \mathbb{P}(\tau=t)=\mathbb{P}\left(x^{*} \in \xi_{t+1}, x^{*} \notin \xi_{t}, \ldots, x^{*} \notin \xi_{2}, x^{*} \notin \xi_{1}\right) \\
& =\mathbb{P}\left(x^{*} \in \xi_{t+1}, x^{*} \notin \xi_{t}, \ldots, x^{*} \notin \xi_{2} \mid x^{*} \notin \xi_{1}\right) \\
& \quad \cdot \mathbb{P}\left(x^{*} \notin \xi_{1}\right) \\
& =\mathbb{P}\left(x^{*} \in \xi_{t+1}, x^{*} \notin \xi_{t}, \ldots, x^{*} \notin \xi_{3} \mid x^{*} \notin \xi_{2}, x^{*} \notin \xi_{1}\right) \\
& \quad \cdot \mathbb{P}\left(x^{*} \notin \xi_{2} \mid x^{*} \notin \xi_{1}\right) \mathbb{P}\left(x^{*} \notin \xi_{1}\right) \\
& =\mathbb{P}\left(x^{*} \in \xi_{t+1} \mid x^{*} \notin \xi_{t}, \ldots, x^{*} \notin \xi_{1}\right) \mathbb{P}\left(x^{*} \notin \xi_{1}\right) \\
& \quad \prod_{j=1}^{t-1} \mathbb{P}\left(x^{*} \notin \xi_{j+1} \mid x^{*} \notin \xi_{j}, \ldots, x^{*} \notin \xi_{1}\right) \\
& =\mathbb{P}\left(x^{*} \in \xi_{t+1} \mid \tau \geq t\right) \prod_{j=0}^{t-1} \mathbb{P}\left(x^{*} \notin \xi_{j+1} \mid \tau \geq j\right) \\
& =\left(1-\left(1-P_{t}^{\prime}\right)^{N}\right) \prod_{j=0}^{t-1}\left(1-P_{j}^{\prime}\right)^{N}
\end{aligned}
$$

where $N$ is the population size, the item $1-\left(1-P_{t}^{\prime}\right)^{N}$ is the probability that the optimum is found at the $t$ th generation, conditional on the event $\tau \geq t$, and the item $\prod_{j=0}^{t-1}\left(1-P_{j}^{\prime}\right)^{N}$ is the probability that the optimum has not been found before the $t$ th generation. Combining the above result with the fact $\mathbb{P}(\tau=0)=1-\left(1-P_{0}^{\prime}\right)^{N}$, we have proven the lemma.

Moreover, let us consider the following lemma:
Lemma 2: If $\mathbb{P}(\tau \prec \operatorname{Poly}(n)) \succ 1-\frac{1}{\text { SuperPoly( } n)}$, then $\exists t^{\prime} \leq$ $\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+1$ such that

$$
\mathbb{P}\left(\tau=t^{\prime}\right) \succ \frac{1}{\operatorname{Poly}(n)}
$$

Proof: Assume that $\forall t \leq\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+1, \mathbb{P}(\tau=$ $t) \prec \frac{1}{\text { SuperPoly( }}(n)$, then we know that

$$
\begin{aligned}
& \max \{\mathbb{P}(\tau=t) ; t \leq\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+1\} \\
& \quad \prec \frac{1}{\text { SuperPoly( } n)} .
\end{aligned}
$$

Hence, we can obtain

$$
\begin{aligned}
& \mathbb{P}(\tau \leq\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+1) \\
& =\sum_{t=0}^{\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+1} \mathbb{P}(\tau=t) \\
& \leq\left(\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+2\right)
\end{aligned}
$$

$$
\begin{aligned}
& \cdot \max \left\{\mathbb{P}(\tau=t) ; t \leq\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+1\right\} \\
& \prec \frac{\operatorname{Poly}(n)}{\text { SuperPoly( } n)} .
\end{aligned}
$$

Now we can estimate the expectation of the FHT $\tau$

$$
\begin{aligned}
& \mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]=\sum_{t=0}^{+\infty} t \mathbb{P}(\tau=t \mid \tau \prec \operatorname{Poly}(n)) \\
= & \sum_{t=0}^{P o l y(n)} \frac{t \mathbb{P}(\tau=t, \tau \prec P o l y(n))}{\mathbb{P}(\tau \prec P o l y(n))} \\
= & \sum_{t=0}^{P o l y(n)} \frac{t \mathbb{P}(\tau=t)}{\mathbb{P}(\tau \prec P o l y(n))} \geq \sum_{t=0}^{P o l y(n)} t \mathbb{P}(\tau=t) \\
= & \sum_{t=0}^{|\mathbb{E}[\tau \mid \tau \prec P o l y(n)]\rceil+1} t \mathbb{P}(\tau=t) \\
& +\sum_{t=|\mathbb{E}[\tau \mid \tau \prec P o l y(n)]\rceil+2}^{P o l y(n)} t \mathbb{P}(\tau=t) \\
& >(\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+2) \\
& \quad \cdot \mathbb{P}(P o l y(n) \succ \tau>\lceil\mathbb{E}[\tau \mid \tau \prec P o l y(n)]\rceil+1) \\
= & (\lceil\mathbb{E}[\tau \mid \tau \prec P o l y(n)]\rceil+2)(\mathbb{P}(\tau \prec P o l y(n)) \\
& -\mathbb{P}(\tau \leq\lceil\mathbb{E}[\tau \mid \tau \prec P o l y(n)]\rceil+1)) \\
= & (\lceil\mathbb{E}[\tau \mid \tau \prec P o l y(n)]\rceil+2) \\
& \cdot\left(1-\frac{1}{\text { SuperPoly( } n)}-\frac{\text { Poly( } n)}{\text { SuperPoly( } n)}\right) \\
& >(\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+2)-\frac{\text { Poly( } n)}{\text { SuperPoly( } n)} \\
& -\frac{\text { Poly( } n) \text { Poly( } n)}{\text { SuperPoly( } n)} .
\end{aligned}
$$

As $n \rightarrow \infty, \frac{\text { Poly( } n)}{\text { SuperPoly( } n)} \rightarrow 0$ and $\frac{\text { Poly( } n) \text { Poly( } n)}{\text { SuperPoly( } n)} \rightarrow 0$. Hence, there exists a sufficiently large problem size $n$ such that

$$
\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]>\lceil\mathbb{E}[\tau \mid \tau \prec \operatorname{Poly}(n)]\rceil+1
$$

which is an obvious contradiction. So we have proven the lemma.

Formally, an optimization problem can be denoted by $I=$ $(\Omega, f)$, where $\Omega$ is the search space and $f$ the fitness function. Following He et al. [19], we use $\mathcal{P}=(\Omega, f, \mathcal{A})$ to indicate an algorithm $\mathcal{A}$ on a fitness function $f$ in the search space $\Omega$. Let the FHT of $\mathcal{A}$ on $I$ be $\tau(\mathcal{P})$. The following theorem describes the relation between EDA-hardness and probability $P_{t}^{*}$.

Theorem 1: For a given $\mathcal{P}$, if the population size $N$ of the EDA $\mathcal{A}$ is polynomial in the problem size $n$, then:

1) if $I$ is EDA-easy for $\mathcal{A}$, then $\exists t^{\prime \prime} \leq\lceil\mathbb{E}[\tau(\mathcal{P}) \mid \tau(\mathcal{P}) \prec$ $\operatorname{Poly}(n)]\rceil+1$ such that

$$
P_{t^{\prime \prime}}^{*} \succ \frac{1}{\operatorname{Poly}(n)}
$$

2) if $\forall t=t(n) \prec P o l y(n), P_{t}^{*} \prec \frac{1}{\text { SuperPoly( } n)}$.
3. $\quad$ then $I$ is EDAhard for $\mathcal{A}$.
Proof: Note that the second part of this theorem is a corollary of the first part. We only need to prove the first part.

According to Lemma 1, we have

$$
\mathbb{P}(\tau(\mathcal{P})=i)<1-\left(1-P_{i}^{\prime}\right)^{N}
$$

On the other hand, according to Lemma 2, we know that $\exists t^{\prime} \leq$ $\lceil\mathbb{E}[\tau(\mathcal{P}) \mid \tau(\mathcal{P}) \prec \operatorname{Poly}(n)]\rceil+1$ such that

$$
\mathbb{P}\left(\tau(\mathcal{P})=t^{\prime}\right) \succ \frac{1}{\operatorname{Poly}(n)}
$$

Thus, we can define $t^{\prime \prime}$ as follows:

$$
\begin{gathered}
t^{\prime \prime}=\min \left\{t^{\prime} ; t^{\prime} \leq\lceil\mathbb{E}[\tau(\mathcal{P}) \mid \tau(\mathcal{P}) \prec \operatorname{Poly}(n)]\rceil+1,\right. \\
\left.\mathbb{P}\left(\tau(\mathcal{P})=t^{\prime}\right) \succ \frac{1}{\operatorname{Poly}(n)}\right\}
\end{gathered}
$$

Since $\mathbb{P}\left(\tau(\mathcal{P})=t^{\prime \prime}\right) \succ \frac{1}{\operatorname{Poly}(n)}$, we have

$$
1-\left(1-P_{t^{\prime}}^{\prime}\right)^{N} \succ \frac{1}{\operatorname{Poly}(n)}
$$

Let us assume that $P_{t^{\prime}}^{*} \prec \frac{1}{\text { SuperPol (n) }}$. Here we let $\mathcal{E}$ represent the event "the global optimum is generated in one sampling at the $t^{\prime \prime}$-th generation," then according to the definitions of $P_{t^{\prime}}^{*}$ and $P_{t^{\prime}}^{\prime}$ mentioned in Section II-B, we obtain the following inequality:

$$
\begin{aligned}
& P_{t^{\prime}}^{*}=\mathbb{P}(\mathcal{E}) \geq \mathbb{P}\left(\mathcal{E}, \tau(\mathcal{P}) \geq t^{\prime \prime}\right) \\
= & \mathbb{P}\left(\mathcal{E} \mid \tau(\mathcal{P}) \geq t^{\prime \prime}\right) \mathbb{P}\left(\tau(\mathcal{P}) \geq t^{\prime \prime}\right) \\
= & P_{t^{\prime}}^{*} \mathbb{P}\left(\tau(\mathcal{P}) \geq t^{\prime \prime}\right)
\end{aligned}
$$

Meanwhile, (7) implies that

$$
\mathbb{P}\left(\tau(\mathcal{P}) \geq t^{\prime \prime}\right) \geq \mathbb{P}\left(\tau(\mathcal{P})=t^{\prime \prime}\right) \succ \frac{1}{\operatorname{Poly}(n)}
$$

Combining (9) and (10) together, we know that $P_{t^{\prime}}^{*} \prec$ $\frac{1}{\text { SuperPoly( }}$ yields $P_{t^{\prime}}^{*} \prec \frac{1}{\text { SuperPoly( }}$.
Now $\forall f(n) \prec \operatorname{Poly}(n)$, we estimate

$$
\lim _{n \rightarrow \infty} \frac{1-\left(1-P_{t^{\prime}}^{\prime}\right)^{N}}{1 / f(n)}
$$

where $N=N(n) \prec \operatorname{Poly}(n)$ is the population size of the EDA. Equation (11) can be calculated as follows:

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \frac{1-\left(1-P_{t^{\prime}}^{\prime}\right)^{N(n)}}{1 / f(n)} \\
& =\lim _{n \rightarrow \infty} \frac{1-\left(\left(1-P_{t^{\prime}}^{\prime}\right)^{\frac{1}{P_{t^{\prime}}}}\right)^{P_{t^{\prime}} N(n)}}{1 / f(n)} \\
& =\lim _{n \rightarrow \infty}\left(f(n)-f(n) e^{-P_{t^{\prime}}^{\prime} N(n)}\right) \\
& =\lim _{n \rightarrow \infty}\left(f(n)-f(n)\left(1-P_{t^{\prime}}^{\prime} N(n)\right.\right. \\
& \left.\left.+\frac{\left(P_{t^{\prime}}^{\prime} N(n)\right)^{2}}{2}+o\left(\left(P_{t^{\prime}}^{\prime} N(n)\right)^{2}\right)\right)\right) \\
& =\lim _{n \rightarrow \infty} f(n) P_{t^{\prime}}^{\prime} N(n)-\lim _{n \rightarrow \infty} \frac{f(n)\left(P_{t^{\prime}}^{\prime} N(n)\right)^{2}}{2} \\
& -\lim _{n \rightarrow \infty} o\left(f(n)\left(P_{t^{\prime}}^{\prime} N(n)\right)^{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \prec \lim _{n \rightarrow \infty} \frac{\operatorname{Poly}^{2}(n)}{\text { SuperPoly( } n)}-\lim _{n \rightarrow \infty} \frac{\operatorname{Poly}^{3}(n)}{\text { SuperPoly }^{2}(n)} \\
& -\lim _{n \rightarrow \infty} o\left(\frac{\operatorname{Poly}^{3}(n)}{\text { SuperPoly }^{2}(n)}\right)=0
\end{aligned}
$$

Hence, we know that $1-\left(1-P_{t^{\prime}}^{\prime}\right)^{N}$ is smaller than $\frac{1}{f(n)} \succ \frac{1}{\operatorname{Poly}(n)}$ when $n \rightarrow \infty$. In other words

$$
1-\left(1-P_{t^{\prime}}^{\prime}\right)^{N} \prec \frac{1}{\text { SuperPoly( }}(n)
$$

where we obtain a contradiction to (8).
So we have

$$
P_{t^{\prime}}^{*} \succ \frac{1}{\operatorname{Poly}(n)}
$$

The theorem is proven.
The theorem above provides us with two simple probability conditions related to the problem classification in terms of EDA-hardness. Later, we will use this theorem to obtain more specific results related to EDA-hardness for the UMDA.

## III. Time Complexity Analysis of EDAs With Finite POpulation Sizes

## A. A General Approach to Analyzing EDAs With Finite Population Sizes

In the domain of EA, several different approaches have been proposed for analyzing theoretically the FHT, such as drift analysis [16], [18], analytical Markov chain [17], Chernoff bounds [7], [23], [24], and convergence rate [15], [43]. Some of them have been applied to EDAs as well. González used the analytical Markov chain to study the worst case exponential FHT of some EDAs [13]. Droste employs drift analysis and Chernoff bounds to analyze the time complexity of cGA (with a population size of two) on linear pseudo-boolean functions [8]. However, those existing techniques might not be sufficient for time complexity analysis of EDAs, because EDAs do not use any variation operators (e.g., mutation and crossover) but rely on sampling successive probabilistic models. Hence, some new ideas are needed to deal with probabilistic models.

One of the main difficulties of analyzing probabilistic models is due to the errors brought by the random sampling processes. Such random errors may occur when a probabilistic model is updated via random sampling. An intuitive idea of handling the random errors is to assume infinite population sizes for EDAs. This assumption has been adopted in the most existing literature, such as the well-known example of OneMAX given by Mühlenbein and Schlierkamp-Voosen [31], and Zhang's convergence analysis of EDAs [45]. Two exceptions are the aforementioned Droste's results on cGA [8] and González's general worst case analysis of EDAs [13].

In this section, we will provide a general approach to analyzing theoretically EDAs with finite population sizes. The approach is closely related to Chernoff bounds and the discrete dynamic system model of population-based incremental learning (PBIL) [1]. PBIL is a more general version of UMDA and its discrete dynamic system model was first presented by González et al. [11]-[13]. Assume there is a function $\mathcal{G}: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$, then $A(t+1)=\mathcal{G}(A(t))(t=0,1, \ldots)$ is called

a discrete dynamic system [39]. In [11]-[13], two discrete dynamic system were discussed. The first one considered PBIL as a function $\mathcal{G}_{1}:[0,1]^{n} \rightarrow[0,1]^{n} . \mathcal{G}_{1}$ includes the random effects. Hence, even if the initial probability distribution and algorithm parameters of PBIL are fixed, the system is still stochastic. This is an exact model of PBIL, but hard to analyze directly. So the authors considered the second dynamic system with the function $\mathcal{G}_{2}:[0,1]^{n} \rightarrow[0,1]^{n}$, which removes the random effects by assuming an infinite population size and thereby becomes deterministic. Although the deviation (caused by the random sampling errors) between the two dynamic systems has been estimated, so as to study the fixed point of the first dynamic system by investigating that of the second system, their method does not relate the deviation to the computation time of PBIL. Hence, it is not applicable to time complexity analysis.

Although González et al. [11]-[13] did not analyze the time complexity of EDAs, their mathematical models (using the discrete dynamic systems) can be used to develop a feasible approach to analyzing the time complexity of EDAs. Such an approach can be summarized by two major steps.

1) Build an easy-to-analyze discrete dynamic system for the EDA. The idea is to de-randomize the EDA and build a deterministic ${ }^{2}$ dynamic system.
2) Analyze the deviations caused by de-randomization. Note that EDAs are stochastic algorithms. Concretely, tail probability techniques, such as Chernoff bounds, can be used to bound the deviations.
In this paper, we will use UMDA as an example of EDAs to illustrate the analysis of EDAs time complexity using the above approach. The analysis will show that our approach provides a feasible way of estimating the random errors brought by finite populations in UMDA, and thus shed some light on analyzing other EDAs with finite populations. However, it should be noted that much work remains to be done to achieve such a goal.

## B. Univariate Marginal Distribution Algorithm

The UMDA was originally proposed as a discrete EDA [28], [44]. As one of the earliest and simplest EDAs, UMDA has attracted a lot of research attention. The UMDA studied in this paper adopts binary encoding and one of the most commonly used selection strategies-the truncation selection, which is described below.

Sort the N individuals in the population by their fitness from high to low. Then select the best M of them for estimating the probability distribution.
The general procedure of UMDA studied in our paper is shown in Table II, where $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right) \in\{0,1\}^{n}$ represents an individual, $p_{t, i}(1)\left(p_{t, i}(0)\right)$ is the estimated marginal probability of the $i$ th bit of an individual to be 1 ( 0 ) at the $i$ th generation. We can also define the indicators $\delta\left(x_{i} \mid 1\right)$ as follows:

$$
\delta\left(x_{i} \mid 1\right) \triangleq \begin{cases}1, & x_{i}=1 \\ 0, & x_{i}=0\end{cases}
$$

[^0]The marginal probabilities $p_{t, i}(1)$ and $p_{t, i}(0)$ are given by

$$
p_{t, i}(1) \triangleq \frac{\sum_{\mathbf{x} \in \mathcal{E}^{\circ}} \delta\left(x_{i} \mid 1\right)}{M}, \quad p_{t, i}(0) \triangleq 1-p_{t, i}(1)
$$

Let

$$
\mathbf{P}_{t}(\mathbf{x}) \triangleq\left(p_{t, 1}\left(x_{1}\right), p_{t, 2}\left(x_{2}\right), \ldots, p_{t, n}\left(x_{n}\right)\right)
$$

where $\mathbf{P}_{t}(\mathbf{x})$ is a probability vector, which is made up of $n$ random variables (that is because, UMDA is a stochastic algorithm). Then the probability of generating individual $\mathbf{x}$ in the $i$ th generation is

$$
p_{t}(\mathbf{x})=\prod_{i=1}^{n} p_{t, i}\left(x_{i}\right)
$$

## C. Analyzing Time Complexity of UMDA

The UMDA given in the former section can be analyzed following the general idea presented in Section III-A. First, we define a function $\gamma:[0,1]^{n} \rightarrow[0,1]^{n}$ such that $\gamma=\mathcal{S} \circ \mathcal{D}$, where $\mathcal{S}:[0,1]^{n} \rightarrow[0,1]^{n}$ is the function that represents the effect of selection, and $\mathcal{D}:[0,1]^{n} \rightarrow[0,1]^{n}$ is the function that is used in eliminating the stochastic effects of the random sampling. Then we obtain a deterministic discrete dynamic system $\left(\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right) ; t=0,1, \ldots\right)$ related to the marginal probabilities of generating the global optimum

$$
\begin{aligned}
\hat{\mathbf{P}}_{0}\left(\mathbf{x}^{*}\right) & =\mathbf{P}_{0}\left(\mathbf{x}^{*}\right) \\
\hat{\mathbf{P}}_{t+1}\left(\mathbf{x}^{*}\right) & =\gamma\left(\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)\right)=\mathcal{S}\left(\mathcal{D}\left(\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)\right)\right) \\
\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right) & =\gamma^{t}\left(\hat{\mathbf{P}}_{0}\left(\mathbf{x}^{*}\right)\right)
\end{aligned}
$$

where $\hat{\mathbf{P}}_{t}(\mathbf{x})=\left(\hat{p}_{t, 1}\left(x_{1}\right), \ldots, \hat{p}_{t, n}\left(x_{n}\right)\right)$ is the marginal probability vector of the deterministic system for generating an individual $\mathbf{x}$, and $\mathbf{x}^{*}$ is the global optimum. Since UMDA is usually initialized with a uniform distribution, we consider $\hat{\mathbf{P}}_{0}(\mathbf{x})=\mathbf{P}_{0}(\mathbf{x})=\left(\frac{1}{2}, \ldots, \frac{1}{2}\right)$ in this paper. Correspondingly, the probability of generating an individual $\mathbf{x}$ is

$$
\hat{p}_{t}(\mathbf{x})=\prod_{i=1}^{n} \hat{p}_{t, i}\left(x_{i}\right)
$$

Note that $p_{t}(\mathbf{x})$ in the former section corresponds to the original UMDA, while $\hat{p}_{t}(\mathbf{x})$ is obtained from the deterministic dynamic system after de-randomization. Following the first step of our general approach, we need to estimate the time complexity of the de-randomized UMDA.

To relate the time complexity result obtained by the deterministic system to the original UMDA, we should estimate the deviation of the de-randomized UMDA from the original UMDA. Since time complexity of the former totally depends on $\left\{\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right) ; t=0,1, \ldots\right\}$, such deviation arises from the difference between $\left\{\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right) ; t=0,1, \ldots\right\}$ and $\left\{\mathbf{P}_{t}\left(\mathbf{x}^{*}\right) ; t=0,1, \ldots\right\}$. Ideally, we want to exactly calculate the difference between the two sequences of marginal probability vectors. However, this is a non-trivial work (if not impossible). Alternatively, we resort to estimating the probabilities that the deviations are smaller than some specific values. Two crucial lemmas for this task are given below.


[^0]:    ${ }^{2}$ In our discussions, "deterministic" is always in the sense that we have fixed the initial values of all the parameters of the non-self-adaptive EDA.

TABLE II
Univariate Marginal Distribution Algorithm (UMDA) With Truncation Selection

$$
\begin{aligned}
& p_{0, t}\left(x_{i}\right) \leftarrow \text { Initial values }(\forall i=1, \ldots, n) \\
& \xi_{1} \leftarrow N \text { individuals are sampled according to the distribution } \\
& p_{0}(\mathbf{x})=\prod_{i=1}^{n} p_{0, t}\left(x_{i}\right) \\
& t \leftarrow 1 ; \\
& \text { REPEAT } \\
& \xi_{t}^{(s)} \leftarrow \text { The best } M \text { individuals are selected from the } N \text { individuals in } \xi_{t}(N>M) \\
& p_{t, t}(1) \leftarrow \frac{\sum_{\mathbf{x}, x_{i}^{(s)}} p_{t, t}(1)}{M}, p_{t, t}(0) \leftarrow 1-p_{t, t}(1) \quad(\forall i=1, \ldots, n) \\
& \xi_{t+1} \leftarrow N \text { individuals are sampled according to the distribution } \\
& p_{t}(\mathbf{x})=\prod_{i=1}^{n} p_{t, t}\left(x_{i}\right) \\
& t \leftarrow t+1 ; \\
& \text { UNTIL THE STOPPING CRITERION IS MET }
\end{aligned}
$$

Lemma 3 ([26]): Chernoff Bounds. Let $X_{1}, X_{2}, \ldots, X_{k} \in$ $\{0,1\}$ be $k$ independent random variables (take the value of either 0 or 1 ) with a same distribution

$$
\forall i \neq j: \mathbb{P}\left(X_{i}=1\right)=\mathbb{P}\left(X_{j}=1\right)
$$

where $i, j \in\{1, \ldots, k\}$. Let $X$ be the sum of those random variables, i.e., $X=\sum_{i=1}^{k} X_{i}$, then we have:

1) $\forall 0<\delta<1$

$$
\mathbb{P}(X<(1-\delta) \mathbb{E}[X])<e^{-\mathbb{E}[X] \delta^{2} / 2}
$$

2) $\forall \delta \leq 2 e-1$

$$
\mathbb{P}(X>(1+\delta) \mathbb{E}[X])<e^{-\mathbb{E}[X] \delta^{2} / 4}
$$

Lemma 4 ([21], [38]): Consider sampling without replacement from a finite population $\left(X_{1}, \ldots, X_{N}\right) \in\{0,1\}^{N}$. Let $\left(Y_{1}, \ldots, Y_{M}\right) \in\{0,1\}^{M}$ be a sample of size $M$ get randomly without replacement from the whole population, $Y^{(M)}$ and $X^{(N)}$ be the sums of the random variables in the sample and population, respectively, i.e., $Y^{(M)}=\sum_{i=1}^{M} Y_{i}$ and $X^{(N)}=$ $\sum_{i=1}^{N} X_{i}$, then we have

$$
\begin{aligned}
\mathbb{P}\left(Y^{(M)}-\frac{M X^{(N)}}{N} \geq M \delta\right) & \leq e^{-\frac{2 M \delta^{2}}{1-\left(M-1\right) / N}} \\
& <e^{-2 M \delta^{2}} \\
\mathbb{P}\left(\left|Y^{(M)}-\frac{M X^{(N)}}{N}\right|>M \delta\right) & \leq 2 e^{-\frac{2 M \delta^{2}}{1-\left(M-1\right) / N}} \\
& <2 e^{-2 M \delta^{2}}
\end{aligned}
$$

where $\delta \in[0,1]$ is some constant. ${ }^{3}$
Another issue that will be involved in our further analysis is to estimate the probability of the following events:

$$
\forall t \in \mathbb{N}_{0}: p_{t}\left(\mathbf{x}^{*}\right) \oplus \hat{p}_{t}\left(\mathbf{x}^{*}\right)
$$

where $\oplus \in\{\leq, \geq\}$. As we will show soon, they can be handled on the basis of estimation of the probabilities of deviations. Finally, before presenting the case studies in detail, it should be noted that we always consider finite population sizes throughout this paper. Although we will sometimes utilize a statement like "when the problem size becomes sufficiently large," that does not mean that we assume infinite population

[^0]sizes, it is merely used to obtain the asymptotic order of a function of the problem size $n$. The main difference is that the infinite population assumption implies infinite population sizes for all problem sizes (so that the random sampling errors are removed), while in our case the population size will be infinite only if the problem size has become infinite.

## IV. WORST CASE ANALYSIS OF UMDA ON THE LEADINGONES PROBLEM

The first maximization problem we investigate is called the LEADINGONES problem, formally defined as follows:

$$
\operatorname{LEADINGONES}(\mathbf{x}) \triangleq \sum_{i=1}^{n} \prod_{j=1}^{i} x_{j}, \quad x_{j} \in\{0,1\}
$$

The global optimum of LEADINGONES is $\mathbf{x}^{*}=(1, \ldots, 1)$. The fitness of an individual is determined by the number of the leading 1-bits in the individual, and it is not influenced by any bits right to the leftmost 0 -bit of the individual. The value of the bits right to the leftmost 0 -bit will not influence the output of fitness-based selection operators in EAs. Due to this characteristic, a population will begin to converge to 1 at a bit if the bits left to it have almost converged to 1 's, and thus a sequential convergence phenomenon, namely Domino convergence [3], [36], [41], will happen.

In the literature of EDAs, the LEADINGONES problem has been investigated empirically [10], but no rigorous theoretical result exists. This section will provide the first theoretical result that put a sound foundation to the time complexity analysis of the UMDA on this problem.

First, we introduce the following concept.
Definition 1 ( $b$-Promising Individual): In the population that contains $N$ individuals, the $b$-promising individuals are those individuals with fitness no smaller than a threshold $b$.

Since the UMDA adopts the truncation selection, we have the following lemma.

Lemma 5: For the UMDA with truncation selection, the poportion of the $b$-promising individuals after selection at the $r$ th generation satisfies

$$
Q_{t, b}^{(s)}= \begin{cases}\frac{Q_{t, b} N}{M}, & Q_{t, b} \leq \frac{M}{N} \\ 1, & Q_{t, b}>\frac{M}{N}\end{cases}
$$


[^0]:    ${ }^{3}$ The first inequality can be found in Corollary 1.1 in [38], or a similar form can be found in [21], and the second inequality is in (3.3) in [38].

where $Q_{t, b} \leq 1$ is the proportion of the $b$-promising individuals before the truncation selection.

Define the $i$-convergence time $T_{i}$ to be the number of generations for a discrete EDA to converge to the globally optimal value on the $i$ th bit of the solution. It is defined formally as

$$
T_{i} \triangleq \min \left\{t ; p_{t, i}\left(x_{t}^{*}\right)=1\right\}
$$

Let $T_{0}=0$.
Moreover, in the following parts of the paper, we use the notation " $\omega$ " to demonstrate the relationship between the asymptotic orders of two functions [5], [24]. Given two positive functions of the problem size $n$, say $f=f(n)$ and $g=g(n), f=\omega(g)$ holds if and only if $\lim _{n \rightarrow \infty} g(n) / f(n)=0$. Now we reach the following theorem.

Theorem 2: Given the population sizes $N=\omega\left(n^{2+\alpha} \log n\right)$, $M=\omega\left(n^{2+\alpha} \log n\right)$ (where $\alpha$ can be any positive constant) and $M=\beta N(\beta \in(0,1)$ is some constant), for the UMDA with truncation selection on the LEADINGONES problem, initialized with a uniform distribution, at least with the probability of

$$
\left(1-n^{-\omega\left(n^{2+\alpha}\right) \delta^{2}}\right)^{\bar{\tau}}\left(1-n^{-\left(1-\left(\frac{1}{2}\right)^{1+\frac{\alpha}{2}}\right)^{2} \omega(1)}\right)^{2(n-1) \bar{\tau}}
$$

its FHT satisfies

$$
\tau<\bar{\tau}=\frac{n\left(\ln \frac{\tau M}{N}-\ln (1-\delta)\right)}{\ln (1-\delta)+\ln \left(\frac{N}{M}\right)}+2 n
$$

where $\delta \in\left(\max \left\{0,1-\frac{2 M}{N}\right\}, 1-\frac{M}{N}\right)$ is a positive constant, and $\bar{\tau}$ represents an upper bound ${ }^{4}$ of the random variable $\tau$. In other words, the LEADINGONES problem is EDA-easy for the UMDA.

Proof: The basic idea of the proof is based on the approach outlined in the former section. We first de-randomize the UMDA. Since the LEADINGONES problem is associated with the domino convergence property, we can further divide the optimization process into $n$ stages. The $i$ th stage starts when all bits at the left side of the $i$ th bit have converged to 1 's, and ends when the $i$ th bit has converged. Suppose generation $t+1$ belongs to the $i$ th stage, then the marginal probabilities at the generation are

$$
\begin{gathered}
\hat{\mathbf{P}}_{t+1}\left(\mathbf{x}^{*}\right)=\gamma_{t}\left(\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)\right)=\left(\hat{p}_{t, 1}\left(x_{t}^{*}\right), \ldots, \hat{p}_{t, i-1}\left(x_{t-1}^{*}\right)\right. \\
{\left[G \hat{p}_{t, i}\left(x_{t}^{*}\right)\right], R \hat{p}_{t, i+1}\left(x_{t+1}^{*}\right), \ldots, R \hat{p}_{t, n}\left(x_{n}^{*}\right)\right)}
\end{gathered}
$$

where $\mathbf{x}^{*}=\left(x_{1}^{*}, \ldots, x_{n}^{*}\right)=(1, \ldots, 1)$ is the global optimum of the LEADINGONES problem, $G=(1-\delta) \frac{n^{\alpha}}{M}\left(\delta \in\left(\max \{0,1-\right.\right.$ $\left.\left.\frac{2 M}{N}\right\}, 1-\frac{M}{N}\right)$ is a constant), and $R=(1-\eta)\left(1-\eta^{\prime}\right)\left(\eta<1\right.$ and $\eta^{\prime}<1$ are positive functions of the problem size $n$ ). We consider three different cases in the above equation.

1) $j \in\{1, \ldots, i-1\}$. In the deterministic system above, the marginal probabilities $\hat{p}_{t, j}\left(x_{t}^{*}\right)$ have converged to 1 , thus at the next generation they will not change.
2) $j=i$. In the deterministic system above, the marginal probability $\hat{p}_{t, i}\left(x_{t}^{*}\right)$ is converging, and we use the factor $G=(1-\delta) \frac{N}{M}$ to demonstrate the impact of selection
pressure on this converging marginal probability, ${ }^{5}$ where $\frac{N}{M}$ represents the influence of the selection operator (see Lemma 5).
3) $j \in\{i+1, \ldots, n\}$. The $j$ th bits of individuals are not exposed to selection pressure, and we use the factor $R=$ $(1-\eta)\left(1-\eta^{\prime}\right)$ to demonstrate the impact of genetic drift ${ }^{6}$ on these marginal probabilities.
In Case 3, we consider the $j$ th marginal probability $p_{., j}\left(x_{t}^{*}\right)$ $(j \in\{i+1, \ldots, n\})$ which is not affected by the selection pressure. This is rather pessimistic, because the UMDA tends to preserve the value of $x_{t}^{*}=1$ that leads to higher fitness, and thus tends to increase $p_{., j}\left(x_{t}^{*}\right)$. Utilizing the idea mentioned in (15), we will study the time complexity of the UMDA by studying the above deterministic system, and estimate the deviation between the deterministic system and the real UMDA in terms of the probability that the stochastic marginal probabilities of the UMDA are bounded by the corresponding deterministic marginal probabilities of the deterministic system. Before our analysis, we first provide the formal definition of the deterministic system.

With $\hat{\mathbf{P}}_{0}\left(\mathbf{x}^{*}\right)=\left(\frac{1}{2}, \ldots, \frac{1}{2}\right)$, we have

$$
\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)=\gamma_{t}^{t-T_{i-1}}\left(\hat{\mathbf{P}}_{T_{i-1}}\left(\mathbf{x}^{*}\right)\right)
$$

where $T_{i-1}<t \leq T_{i}(i=1, \ldots, n)$. Since $\left\{\gamma_{t}\right\}_{t=1}^{n}$ derandomizes the whole optimization process, $\left\{T_{i}\right\}_{i=1}^{n}$ in the above equation are no longer random variables. For the sake of clarity, we rewrite the above equation as

$$
\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)=\gamma_{t}^{t-\bar{T}_{i-1}}\left(\hat{\mathbf{P}}_{\bar{T}_{i-1}}\left(\mathbf{x}^{*}\right)\right)
$$

where $\bar{T}_{i-1}<t \leq \bar{T}_{i}(i=1, \ldots, n)$. As we will show immediately, $\bar{T}_{i}(1 \leq i \leq n)$ is an upper bound of the random variable $T_{i}$ with some probability. Since $T_{n} \geq \tau$, our task finally becomes calculating the $\bar{T}_{n}$ and the probability that $\bar{T}_{n}$ holds as an upper bound of $T_{n}$.

Now we present the proof in detail. First, we estimate $\bar{T}_{1}$ and $T_{1}$ for the UMDA, which is the first stage of our analysis. Consider the 1-promising individuals. Note that the first bits of the 1-promising individuals are 1's. The sampling procedure of the UMDA can be considered as a large number of events resulting in either 0 or 1 . Hence, when $p_{t-1,1}(1) \leq \frac{M}{N(1-\delta)}$, for the sampling procedure of the UMDA, by noting Lemma 5, we can apply Chernoff bounds to obtain the following:

$$
\begin{aligned}
& \mathbb{P}\left(M p_{t, 1}(1) \geq(1-\delta) p_{t-1,1}(1) N \mid p_{t-1,1}(1) \leq \frac{M}{N(1-\delta)}\right) \\
& \quad>1-e^{-\frac{p_{t-1,1}(1) N}{2} \delta^{2}}
\end{aligned}
$$

where $N=\omega\left(n^{2} \log n\right)$, thus the probability above is superpolynomially close to 1 , i.e., an overwhelming probability. An

[^0]
[^0]:    ${ }^{5}$ The notation " [ ]" can be interpreted as follows: given $a>1,[a]=1$; given $a \in(0,1),[a]=a$. For the sake of brevity, we will omit this notation but implicitly restrict the value of a probability not to exceed 1 in the following parts of the paper.
    ${ }^{6}$ When there is no selection pressure, the proportion of alleles in a population with finite genes will fluctuate due to the errors brought by random sampling. For more details, one can refer to [6], [41].

TABLE III
Calculation of Probability That $p_{0,1}(1)$ Is Lower Bounded by $\bar{p}_{0,1}(1)$

$$
\begin{aligned}
& \mathbb{P}\left(p_{0,1}(1) \geq \bar{p}_{0,1}(1) \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right) \\
& =\sum_{\forall t^{\prime}<t \leqslant q_{t^{\prime}} \in\left\{0, \frac{1}{M}, \frac{1}{M}, \ldots, 1\right\}} \mathbb{P}\left(p_{0,1}(1) \geq G^{r} p_{0,1}(1), p_{t-1,1}(1)=a_{t-1}, \cdots, p_{1,1}(1)=a_{1} \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right) \\
& >\mathbb{P}\left(p_{0,1}(1) \geq G p_{t-1,1}(1), \cdots, p_{1,1}(1) \geq G p_{0,1}(1) \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right) \\
& =\mathbb{P}\left(p_{t-1,1}(1) \geq G p_{t-2,1}(1), \cdots, p_{1,1}(1) \geq G p_{0,1}(1) \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right) \\
& \mathbb{P}\left(p_{0,1}(1) \geq G p_{t-1,1}(1) \mid p_{t-1,1}(1) \geq G p_{t-2,1}(1), \cdots, p_{1,1}(1) \geq G p_{0,1}(1), p_{0,1}(1)=\bar{p}_{0,1}(1)\right) \\
& =\mathbb{P}\left(p_{1,1}(1) \geq G p_{0,1}(1) \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right) \\
& \prod_{k=2}^{r} \mathbb{P}\left(p_{k, 1}(1) \geq G p_{k-1,1}(1) \mid p_{k-1,1}(1) \geq G p_{k-2,1}(1), \cdots, p_{1,1}(1) \geq G p_{0,1}(1), p_{0,1}(1)=\bar{p}_{0,1}(1)\right) \\
& =\mathbb{P}\left(p_{1,1}(1) \geq G p_{0,1}(1) \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right) \\
& \prod_{k=2}^{r} \mathbb{P}\left(p_{k, 1}(1) \geq G p_{k-1,1}(1) \mid p_{k-1,1}(1) \geq \bar{p}_{k-1,1}(1)=G^{k-1} \bar{p}_{0,1}(1)\right) \\
& >\prod_{k=1}^{r}\left(1-e^{-\bar{p}_{k-1,1}(1) N \bar{p}^{2} / 2}\right)>\prod_{k=1}^{r}\left(1-e^{-G^{k-1} \bar{p}_{0,1}(1) N \bar{p}^{2} / 2}\right)>\left(1-e^{-\bar{p}_{0,1}(1) N \bar{p}^{2} / 2}\right)^{\prime}
\end{aligned}
$$

TABLE IV
Calculation of Probability That $T_{1}$ Is Upper Bounded by $\bar{T}_{1}$

$$
\begin{aligned}
& \mathbb{P}\left(T_{1} \leq \bar{T}_{1} \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right) \\
& >\mathbb{P}\left(p_{T_{1}-1,1}(1) \geq \frac{M}{N(1-\delta)} \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right)\left(1-e^{-\frac{\bar{p}_{0,1}(1) N}{2} \bar{p}^{2}}\right) \\
& >\mathbb{P}\left(p_{T_{1}-1,1}(1) \geq \bar{p}_{T_{1}-1,1}(1)=G^{T_{1}-1} p_{0,1}(1)>\frac{M}{N(1-\delta)} \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right)\left(1-e^{-\frac{\bar{p}_{0,1}(1) N}{2} \bar{p}^{2}}\right) \\
& >\mathbb{P}\left(p_{T_{1}-1,1}(1) \geq \bar{p}_{T_{1}-1,1}(1) \mid p_{0,1}(1)=\bar{p}_{0,1}(1), \bar{p}_{T_{1}-1,1}(1)>\frac{M}{N(1-\delta)}\right) \\
& \mathbb{P}\left(\bar{p}_{T_{1}-1,1}(1)>\frac{M}{N(1-\delta)} \mid p_{0,1}(1)=\bar{p}_{0,1}(1)\right)\left(1-e^{-\frac{\bar{p}_{0,1}(1) N}{2} \bar{p}^{2}}\right)
\end{aligned}
$$

TABLE V
BOUNDING $N_{i, j}^{(s)}\left(x_{j}^{*}\right)$ From Below With an OVERwhelming Probability

$$
\begin{aligned}
& \mathbb{P}\left(N_{i, j}^{(s)}\left(x_{j}^{*}\right)>\left(1-\eta^{\prime}\right) \frac{(1-\eta) p_{t-1, j}\left(x_{j}^{*}\right) N}{N} M \mid N_{i, j}\left(x_{j}^{*}\right) \geq\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right) p_{t-1, j}\left(x_{j}^{*}\right) N, p_{t-1, j}\left(x_{j}\right)\right) \\
& =\mathbb{P}\left(\frac{(1-\eta) p_{t-1, j}\left(x_{j}^{*}\right) N}{N} M-N_{i, j}^{(s)}\left(x_{j}^{*}\right)<\eta^{\prime} \frac{(1-\eta) p_{t-1, j}\left(x_{j}^{*}\right) N}{N} M \mid N_{i, j}\left(x_{j}^{*}\right) \geq\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right) p_{t-1, j}\left(x_{j}^{*}\right) N, p_{t-1, j}\left(x_{j}^{*}\right)\right) \\
& >1-2 e^{-2(1-\eta)^{2} p_{t-1, j}^{2}\left(x_{j}^{*}\right) \eta^{\prime 2} M}
\end{aligned}
$$

TABLE VI
Calculation of the Joint Probability That $T_{1}$ Is Bounded Above by $\hat{T}_{2}$

$$
\begin{aligned}
& \mathbb{P}\left(T_{2} \leq \hat{T}_{2}, T_{1} \leq \hat{T}_{1}, p_{\hat{T}_{1}, 2}(1) \geq \hat{p}_{\hat{T}_{1}, 2}(1)>\frac{1}{e} \mid p_{0,1}(1)=\hat{p}_{0,1}(1), p_{0,2}(1)=\hat{p}_{0,2}(1)\right) \\
& >\mathbb{P}\left(p_{\hat{T}_{2}-1,2}(1) \geq \frac{M}{N(1-\delta)} \mid p_{0,1}(1)=\hat{p}_{0,1}(1), p_{0,2}(1)=\hat{p}_{0,2}(1), T_{1} \leq \hat{T}_{1}, p_{\hat{T}_{1}, 2}(1) \geq \hat{p}_{\hat{T}_{1}, 2}(1)>\frac{1}{e}\right) \\
& \quad\left(1-e^{-\frac{\left(p h^{2}\right) p_{0}(0,0)}{2 e}}\right)^{\hat{T}_{1}}\left(1-n^{-\left(1-\left(\frac{1}{n}\right)^{1+\frac{e}{2}}\right)^{2} e(1)}\right)^{2 \hat{T}_{1}}\left(1-e^{-\frac{\hat{p}_{\hat{T}_{1}, 2}(1) N}{2} e}\right) \\
& >\mathbb{P}\left(p_{\hat{T}_{2}-1,2}(1) \geq \hat{p}_{\hat{T}_{2}-1,2}(1)=G^{\hat{T}_{2}-\hat{T}_{1}-1} p_{\hat{T}_{1}, 2}(1)>\frac{M}{N(1-\delta)} \mid p_{\hat{T}_{1}, 1}(1)=1, p_{\hat{T}_{1}, 2}(1) \geq \hat{p}_{\hat{T}_{1}, 2}(1)>\frac{1}{e}\right) \\
& \quad\left(1-e^{-\frac{\left(p h^{2}\right) p_{0}(0,0)}{2 e}}\right)^{\hat{T}_{1}}\left(1-n^{-\left(1-\left(\frac{1}{n}\right)^{1+\frac{e}{2}}\right)^{2} e(1)}\right)^{2 \hat{T}_{1}}\left(1-e^{-\frac{\left(p_{\hat{T}_{1}, 2}(1) N}{2} e}\right)} \\
& >\mathbb{P}\left(p_{\hat{T}_{2}-1,2}(1) \geq \hat{p}_{\hat{T}_{2}-1,2}(1) \mid p_{\hat{T}_{1}, 1}(1)=1, p_{\hat{T}_{1}, 2}(1) \geq \hat{p}_{\hat{T}_{1}, 2}(1)>\frac{1}{e}, \hat{p}_{\hat{T}_{2}-1,2}(1)>\frac{M}{N(1-\delta)}\right) \\
& \mathbb{P}\left(\hat{p}_{\hat{T}_{2}-1,2}(1)>\frac{M}{N(1-\delta)} \mid p_{\hat{T}_{1}, 1}(1)=1, p_{\hat{T}_{1}, 2}(1) \geq \hat{p}_{\hat{T}_{1}, 2}(1)>\frac{1}{e}\right) \\
& \quad\left(1-e^{-\frac{\left(p h^{2}\right) p_{0}(0,0)}{2 e}}\right)^{\hat{T}_{1}}\left(1-n^{-\left(1-\left(\frac{1}{n}\right)^{1+\frac{e}{2}}\right)^{2} e(1)}\right)^{2 \hat{T}_{1}}\left(1-e^{-\frac{\left(p h^{2}\right) p_{0}(0,0)}{2} e}\right)
\end{aligned}
$$

TABLE VII
Bounding $N_{t, q}^{(i)}(x_{q}^{*})$ From Above With an Overwhelming Probability

$$
\begin{aligned}
& \mathbb{P}\left(N_{t, q}^{(i)}(x_{q}^{*})<\left(1+\eta^{\prime}\right)^{\frac{(1+\eta) p_{t-1, q}\left(x_{q}^{*}\right) N}{N}} M \mid N_{t, q}\left(x_{q}^{*}\right) \leq\left(1+\left(\frac{1}{n}\right)^{1+\frac{e}{2}}\right) p_{t-1, q}\left(x_{q}^{*}\right) N, p_{t-1, q}\left(x_{q}^{*}\right)\right) \\
= & \mathbb{P}\left(N_{t, q}^{(i)}\left(x_{q}^{*}\right)-\frac{(1+\eta) p_{t-1, q}\left(x_{q}^{*}\right) N}{N} M<\eta^{\prime} \frac{(1+\eta) p_{t-1, q}\left(x_{q}^{*}\right) N}{N} M \mid N_{t, q}\left(x_{q}^{*}\right) \leq\left(1+\left(\frac{1}{n}\right)^{1+\frac{e}{2}}\right) p_{t-1, q}\left(x_{q}^{*}\right) N, p_{t-1, q}\left(x_{q}^{*}\right)\right) \\
> & 1-e^{-2(1+\eta)^{2} p_{t-1, q}^{2}\left(x_{q}^{*}\right) N^{2} M}
\end{aligned}
$$

equivalent form of the equation above is

$$
\begin{aligned}
& \mathbb{P}\left(p_{t, 1}(1) \geq(1-\delta) \frac{\hat{p}_{t-1,1}(1) N}{M} \mid p_{t-1,1}(1) \leq \frac{M}{N(1-\delta)}\right) \\
& >1-e^{-\frac{\left(p_{t-1,1}(1) N}{2} \delta^{2}}}
\end{aligned}
$$

which demonstrates with an overwhelming probability the marginal probability $p_{t, 1}(1)$ is lower bounded by $G p_{t-1,1}(1)=$ $(1-\delta) \frac{\hat{p}_{t-1,1}(1) N}{M}$. Furthermore, given $\hat{p}_{t, 1}(1)=G^{t} \hat{p}_{0,1}(1)$ and $G>1$, we can obtain the inequality in Table III.

We now study the distribution of $T_{1}$. Considering the probability that $T_{1}$ is bounded by a value, say $\hat{T}_{1}$ : given $T_{1}<\hat{T}_{1}$, then according to Lemma 5, at the $\left(\hat{T}_{1}-1\right)$ th generation, the marginal probability $p_{\hat{T}_{1}-1,1}(1)$ should be at least $\frac{M}{N(1-\delta)}$. The above proposition is presented in Table IV, where in (19) the factor $\left(1-e^{-\frac{\hat{p}_{0,1}(1) N}{2} \delta^{2}}\right)$ is added since we apply Chernoff bounds once at the end of the $\left(\hat{T}_{1}-1\right)$ th generation and obtain the probability that $\hat{p}_{\hat{T}_{1}, 1}(1)=1$, under the condition $\hat{p}_{\hat{T}_{1}-1,1}(1) \geq \frac{M}{N(1-\delta)}$. Now let us consider the following item. Noting that $\hat{p}_{\hat{T}_{1}-1,1}(1)$ is deterministic, we
know

$$
\mathbb{P}\left(\hat{p}_{\hat{T}_{1}-1,1}(1)>\frac{M}{N(1-\delta)} \mid p_{0,1}(1)=\hat{p}_{0,1}(1)\right)
$$

must be either 0 or 1 , and we need to find the value of $\hat{T}_{1}$ that makes the probability above 1 . Given that $\hat{p}_{0,1}(1)=\frac{1}{2}$, the condition that $\forall t<\hat{T}_{1}-1: \frac{M}{N(1-\delta)}>\hat{p}_{t, 1}(1)>(1-\delta) \frac{\hat{p}_{t-1,1}(1) N}{M}$ and Lemma 5 together imply the following inequalities.

$$
\begin{aligned}
G^{\hat{T}_{1}-2} \hat{p}_{0,1}(1)= & (1-\delta)^{\hat{T}_{1}-2}\left(\frac{N}{M}\right)^{\hat{T}_{1}-2} \hat{p}_{0,1}(1) \\
& <\frac{M}{N(1-\delta)} \\
G^{\hat{T}_{1}-1} \hat{p}_{0,1}(1)= & (1-\delta)^{\hat{T}_{1}-1}\left(\frac{N}{M}\right)^{\hat{T}_{1}-1} \hat{p}_{0,1}(1) \\
& \geq \frac{M}{N(1-\delta)}
\end{aligned}
$$

Solving the inequalities above, we get

$$
\hat{T}_{1} \leq \frac{\ln \frac{2 M}{N}-\ln (1-\delta)}{\ln (1-\delta)+\ln \left(\frac{N}{M}\right)}+2
$$

where $\delta \in\left(\max \left\{0,1-\frac{2 M}{N}\right\}, 1-\frac{M}{N}\right)$ is a constant, and it is easy to show that $\tilde{T}_{1}=\Theta(1)$. On the other hand, recall the inequalities in Table III, we can continue to estimate the corresponding probability mentioned in (18)

$$
\begin{gathered}
\mathbb{P}\left(T_{1} \leq \tilde{T}_{1} \mid p_{0,1}(1)=\tilde{p}_{0,1}(1)\right) \\
>\mathbb{P}\left(p_{\tilde{T}_{1}-1,1}(1) \geq \tilde{p}_{\tilde{T}_{1}-1,1}(1) \mid p_{0,1}(1)=\tilde{p}_{0,1}(1)\right) \\
\cdot\left(1-e^{-\frac{\tilde{p}_{0,1}(1) N}{2} \tilde{p}}\right) \\
>\left(1-e^{-\frac{\tilde{p}_{0,1}(1) N}{2} \tilde{p}}\right)^{\tilde{T}_{1}}
\end{gathered}
$$

The analysis above tells us, the probability to which the marginal probability converges before the $\tilde{T}_{1}$ th generation $\left(T_{1}<\tilde{T}_{1}\right)$ is at least $\left(1-e^{-\frac{\tilde{T}_{1} \tilde{g}}{2}}\right)^{\tilde{T}_{1}}$. Since $N=\omega\left(n^{2 \pi \alpha} \log n\right)$, $M=\beta N(\beta \in(0,1)$ is a constant) and $\tilde{T}_{1}$ is polynomial in the problem size $n$, we know that the probability is overwhelming.

At every stage, the bits on the right-hand side of the currently converging bit are not exposed to selection pressure. However, we should still consider the errors brought by the repeated sampling procedures in UMDA, which is related to the genetic drift [6], [41].

Take the first stage as an example. The $j$ th bit $(j=2, \ldots, n)$ is affected by genetic drift. First, we utilize Chernoff bounds to study the deviations brought by the random sampling procedures of the UMDA

$$
\begin{gathered}
\mathbb{P}\left(N_{t, j}\left(x_{j}^{*}\right) \geq(1-\eta) p_{t-1, j}\left(x_{j}^{*}\right) N \mid p_{t-1, j}\left(x_{j}^{*}\right)\right) \\
>1-e^{-\frac{\tilde{p}_{t-1, j}(1) N}{2} \eta^{2}} \\
>1-e^{-\frac{\tilde{p}_{t-1, j}(1) N}{2} \eta^{2}}
\end{gathered}
$$

where $\eta$ is a parameter that controls the size of deviation, and $N_{t, j}\left(x_{j}\right)$ is the number of individuals that takes the value $x_{j}$ in their $j$ th bit in the population before selection, $\xi_{j}$. Here we set $\eta=\left(\frac{1}{n}\right)^{1+\frac{n}{2}}$, and obtain

$$
\begin{aligned}
\mathbb{P}\left(N_{t, j}\left(x_{j}^{*}\right) \geq\right. & \left.\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right) p_{t-1, j}\left(x_{j}^{*}\right) N \mid p_{t-1, j}\left(x_{j}^{*}\right)\right) \\
& >1-e^{-\frac{p_{t-1, j}\left(x_{j}^{*}\right) \omega(\log n)}{2}}=1-n^{-\frac{p_{t-1, j}\left(x_{j}^{*}\right) \omega(1)}{2}}
\end{aligned}
$$

Second, we further consider the selection procedure, since it may also bring some deviations. In our worst case analysis, the $j$ th bits of individuals are considered to not be exposed to the selection pressure, then for these bits the selection procedure can be regarded as get a simple random sample of $M$ individuals from a finite population with $N$ individuals [34]. More precisely, since one individual cannot be selected more than once by the truncation selection, this procedure is known as random sampling without replacement from a finite population [34] in the field of statistics. From Lemma 4, we can bound from below the probability such that the number of individuals taking the value $x_{j}^{*}$ on their $j$ th bits after selection [denoted by $N_{t, j}^{(i)}\left(x_{j}^{*}\right)$ ] is lower bounded, which is shown by the inequalities presented in Table V, where $\eta^{\prime}$ is a parameter that controls the size of deviation, and $N_{t, j}^{(i)}\left(x_{j}^{*}\right)=p_{t, j}\left(x_{j}^{*}\right) M$. By
setting $\eta^{\prime}=\eta=\left(\frac{1}{n}\right)^{1+\frac{n}{2}}$, since $M=\omega\left(n^{2 \pi \alpha} \log n\right)$ we obtain

$$
\begin{aligned}
\mathbb{P}\left(p_{t, j}\left(x_{j}^{*}\right)\right. & \left.\geq\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right)^{2} p_{t-1, j}\left(x_{j}^{*}\right) \mid p_{t-1, j}\left(x_{j}^{*}\right)\right) \\
& >\left(1-n^{-p_{t-1, j}\left(x_{j}^{*}\right) \omega(1)}\right) \\
& \left(1-n^{-\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right)^{2} p_{t-1, j}^{2}\left(x_{j}^{*}\right) \omega(1)}\right) \\
& >\left(1-n^{-\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right)^{2} p_{t-1, j}^{2}\left(x_{j}^{*}\right) \omega(1)}\right)^{2}
\end{aligned}
$$

Since the factor $R=\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right)^{2}<1$, for $\forall j=2 \ldots, n$ and $t=1, \ldots, \tilde{T}_{1}$, similar to the analysis shown in Table III, we further obtain

$$
\begin{aligned}
& \mathbb{P}\left(p_{t, j}\left(x_{j}^{*}\right) \geq\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right)^{2 t} p_{0, j}\left(x_{j}^{*}\right)\right. \\
& \left.\quad \mid p_{0, j}\left(x_{j}^{*}\right)=\tilde{p}_{0, j}\left(x_{j}^{*}\right)\right) \\
& >\left(1-n^{-\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right)^{2} \tilde{p}_{t-1, j}^{2}\left(x_{j}^{*}\right) \omega(1)}\right)^{2 t}
\end{aligned}
$$

Given any $t=O(n)$, according to the definition of the deterministic system, we know

$$
\tilde{p}_{t, j}\left(x_{j}^{*}\right) \geq\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right)^{O(n)} \tilde{p}_{0, j}\left(x_{j}^{*}\right)>\frac{1}{e}
$$

holds. The above inequality implies that within the number of generations $t=O(n)$, the probability in (26) is an overwhelming one.

To generalize the above analysis to other stages, let us consider the $i$ th $(i \in\{2, \ldots, n\})$ stage is about to start. Due to the genetic drift, the marginal probability $p_{t, j}\left(x_{j}^{*}\right)$ $(j \in\{i, \ldots, n\})$ has dropped to a lower level than the initial value $\frac{1}{2}$ by multiplying the factor $R^{t}$. We concern the value of $p_{t, i}\left(x_{i}^{*}\right)$. For any $t=O(n)$, similar to (26), the probability that $p_{t, i}\left(x_{i}^{*}\right)$ maintains a level of

$$
p_{t, i}\left(x_{i}^{*}\right) \geq\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right)^{O(n)} \tilde{p}_{0, i}\left(x_{i}^{*}\right)>\frac{1}{e}
$$

is super-polynomially close to 1 (an overwhelming probability).

According to (27), we know that $p_{t, i}\left(x_{i}^{*}\right)$ is above $\frac{1}{e}$ with an overwhelming probability. Consequently, the joint probability that the first bit has converged to 1 and the genetic drift cannot reduce $p_{\tilde{T}_{1,2}}(1)$ to be smaller than $\frac{1}{e}$ by the end of the first stage is

$$
\left(1-e^{-\frac{\left(\omega^{2} n \log n\right) \tilde{g}}{2}}\right)^{\tilde{T}_{1}}\left(1-n^{-\left(1-\left(\frac{1}{n}\right)^{1+\frac{n}{2}}\right)^{2} \omega(1)}\right)^{2 \tilde{T}_{1}}
$$

which is again an overwhelming probability. Now we have finished the analysis of the first stage.

As the dynamic system we described at the beginning of the proof, in the second stage, for $\tilde{T}_{1}<t \leq \tilde{T}_{2}$, we have

$$
\tilde{p}_{t, 2}(1)=G \tilde{p}_{t-1,2}(1)
$$

Given $\tilde{T}_{1}$ and the corresponding marginal probabilities, we consider the joint probability that $T_{2}$ is bounded above by $\tilde{T}_{2}$ by inequalities presented in Table VI.

Let us consider the following item of the probability estimated in Table VI:

$$
\begin{gathered}
\mathbb{P}\left(\hat{p}_{T_{2}-1,2}(1)>\frac{M}{N(1-\delta)} \mid p_{\hat{T}_{1}, 1}(1)=1\right. \\
\left.p_{\hat{T}_{1}, 2}(1) \geq \hat{p}_{T_{1}, 2}(1)>\frac{1}{e}\right)
\end{gathered}
$$

since $\left[\hat{p}_{1,2}(1)\right]_{\substack{\infty<\varepsilon}}^{\infty}$ is a deterministic sequence, the above item must be either 0 or 1 . Noting that $\hat{p}_{T_{1}, 2}(1)>\frac{1}{e}$, given the condition that $\forall t: \hat{T}_{1}<t<\hat{T}_{2}-1: \frac{M}{N(1-\delta)}>\hat{p}_{1,2}(1)=$ $(1-\delta) \frac{\hat{p}_{t-1,2}(1) N}{M}$, we can solve the following inequalities to obtain $\hat{T}_{2}$

$$
\begin{gathered}
G^{\hat{T}_{2}-\hat{T}_{1}-2} \hat{p}_{T_{1}, 2}(1) \\
=\left((1-\delta)\left(\frac{N}{M}\right)\right)^{\hat{T}_{2}-\hat{T}_{1}-2} \hat{p}_{T_{1}, 2}(1)<\frac{M}{N(1-\delta)} \\
G^{\hat{T}_{2}-\hat{T}_{1}-1} \hat{p}_{T_{1}, 2}(1) \\
=\left((1-\delta)\left(\frac{N}{M}\right)\right)^{\hat{T}_{2}-\hat{T}_{1}-1} \hat{p}_{T_{1}, 2}(1) \geq \frac{M}{N(1-\delta)}
\end{gathered}
$$

Moreover, another item in (22)

$$
\begin{aligned}
& \mathbb{P}\left(p_{T_{2}-1,2}(1) \geq \hat{p}_{T_{2}-1,2}(1) \mid p_{T_{1}, 1}(1)=1\right. \\
& \left.p_{T_{1}, 2}(1) \geq \hat{p}_{T_{1}, 2}(1)>\frac{1}{e}, \hat{p}_{T_{2}-1,2}(1)>\frac{M}{N(1-\delta)}\right)
\end{aligned}
$$

should be estimated. This can be done similarly as we have done in Table III. Then we obtain that

$$
T_{2}<\hat{T}_{2} \leq \frac{2 \ln \frac{e M}{N}-2 \ln (1-\delta)}{\ln (1-\delta)+\ln \left(\frac{N}{M}\right)}+4
$$

holds with the probability [the product of the items mentioned in (22)]

$$
\left(1-e^{-\frac{\omega\left(\operatorname{Im} \log \alpha\right) g t}{N}}\right)^{\hat{T}_{2}}\left(1-n^{-\left(1-\left(\frac{1}{e}\right)^{1+\frac{\alpha}{2}}\right)^{2} \omega(1)}\right)^{2 \hat{T}_{1}}
$$

The above analysis can be readily extended to other stages. To be specific, at the $i$ th stage, the $i$-promising individuals are taken into account. We have

$$
\hat{p}_{t, i}(1)=G \hat{p}_{t-1, i}(1)
$$

For induction, assume that at the $(i-1)$ th stage

$$
\begin{aligned}
& T_{i-1}<\hat{T}_{i-1} \leq \frac{(i-1) \ln \frac{e M}{N}-(i-1) \ln (1-\delta)}{\ln (1-\delta)+\ln \left(\frac{N}{M}\right)} \\
& +2(i-1)
\end{aligned}
$$

holds with the probability

$$
\begin{aligned}
& \left(1-e^{-\frac{\left(\omega\left(\operatorname{Im} \log \alpha\right) g t\right)^{2}}{2}}\right)^{\hat{T}_{i-1}} \\
& \prod_{k=1}^{i-2}\left(1-n^{-\left(1-\left(\frac{1}{e}\right)^{1+\frac{\alpha}{2}}\right)^{2} \omega(1)}\right)^{2 \hat{T}_{k}}
\end{aligned}
$$

To estimate $\hat{T}_{i}$, we solve the following inequalities:

$$
\begin{gathered}
G^{\hat{T}_{i}-\hat{T}_{i-1}-2} \hat{p}_{T_{i-1}, i}(1) \\
=(1-\delta)^{\hat{T}_{i}-\hat{T}_{i-1}-2}\left(\frac{N}{M}\right)^{\hat{T}_{i}-\hat{T}_{i-1}-2} \hat{p}_{T_{i-1}, i}(1) \\
<\frac{M}{N(1-\delta)} \\
G^{\hat{T}_{i}-\hat{T}_{i-1}-1} \hat{p}_{T_{i-1}, i}(1) \\
=(1-\delta)^{\hat{T}_{i}-\hat{T}_{i-1}-1}\left(\frac{N}{M}\right)^{\hat{T}_{i}-\hat{T}_{i-1}-1} \hat{p}_{T_{i-1}, i}(1) \\
\geq \frac{M}{N(1-\delta)}
\end{gathered}
$$

where $\hat{p}_{T_{i-1}, i}(1)>\frac{1}{e}$ [similar to (27)], since $\hat{T}_{i-1}=O(n)$ [our assumption for induction in (29) shows that it is $O(n)$ ]. Similar to the discussion at the second stage, we can get that

$$
T_{i}<\hat{T}_{i} \leq \frac{i \ln \frac{e M}{N}-i \ln (1-\delta)}{\ln (1-\delta)+\ln \left(\frac{N}{M}\right)}+2 i
$$

holds with the probability

$$
\begin{gathered}
\left(1-e^{-\frac{\omega\left(\operatorname{Im} \log \alpha\right) g t}{N}}\right)^{\hat{T}_{i}} \\
\cdot \prod_{k=1}^{i-1}\left(1-n^{-\left(1-\left(\frac{1}{e}\right)^{1+\frac{\alpha}{2}}\right)^{2} \omega(1)}\right)^{2 \hat{T}_{k}}
\end{gathered}
$$

Finally, the FHT $\tau$ is upper bounded by

$$
\tau<\hat{T}_{n}=\frac{n\left(\ln \frac{e M}{N}-\ln (1-\delta)\right)}{\ln (1-\delta)+\ln \left(\frac{N}{M}\right)}+2 n
$$

with a probability of

$$
\begin{gathered}
\left(1-e^{-\frac{\omega\left(\operatorname{Im} \log \alpha\right) g t}{2}}\right)^{\hat{T}_{n}} \\
\prod_{k=1}^{n-1}\left(1-n^{-\left(1-\left(\frac{1}{e}\right)^{1+\frac{\alpha}{2}}\right)^{2} \omega(1)}\right)^{2 \hat{T}_{k}} \\
>\left(1-n^{-\omega\left(n^{2 \omega}\right) g^{2}}\right)^{\hat{T}_{n}} \\
\cdot\left(1-n^{-\left(1-\left(\frac{1}{e}\right)^{1+\frac{\alpha}{2}}\right)^{2} \omega(1)}\right)^{2(n-1) \hat{T}_{n}}
\end{gathered}
$$

which is an overwhelming probability.
In the proof above, we have proven that a bound holds for the FHT with an overwhelming probability. Furthermore, the proof also shows the convergence of UMDA on LEADINGONES: the UMDA will converge to the optimum with an overwhelming probability. The convergence property is ensured by using population sizes of $\omega\left(n^{2+\sigma} \log n\right)$, and considering all the random sampling errors in the pessimistic way.

## V. Best Case Analysis of UMDA on the BVLeadingOnes Problem

The previous section has shown that the LEADINGONES problem is EDA-easy for the UMDA. In this section, we will study another maximization problem that is unimodal but EDA-hard for the UMDA. The problem, which is called BVLEADINGONES (BVLO for short), can be regarded as the

LEADINGONES problem with one bit's variation. It is defined as follows:

$$
\operatorname{BVLO}(\mathbf{x})= \begin{cases}\mathrm{LO}(\mathbf{x})+n, & \mathrm{LO}(\mathbf{x}) \leq n-1, x_{n}=0 \\ \mathrm{LO}(\mathbf{x}), & \mathrm{LO}(\mathbf{x})<n-1, x_{n}=1 \\ 3 n, & \mathrm{LO}(\mathbf{x})=n\end{cases}
$$

where $\forall i=1, \ldots, n: x_{i} \in\{0,1\}$ and LO stands for LEADINGONES. The BVLEADINGONES is a unimodal function whose global optimum is $\mathbf{x}^{*}=\left(x_{1}^{*}, \ldots, x_{n}^{*}\right)=(1, \ldots, 1)$. In this section, we will prove that BVLEADINGONES is EDAhard for the UMDA.

Let us look at (30) again. The $n$th bits of the individuals are exposed to the selection pressure from the very beginning. During the optimization process, an individual whose last bit is 0 always has higher fitness than any individuals with its last bit being 1 , unless the first $n-1$ bits of the latter are all 1 's. In other words, the $n$th marginal probability $p_{-n}\left(\bar{x}_{n}^{*}\right)$ starts converging to 1 from the beginning of optimization, where $\bar{x}_{n}^{*}=1-x_{n}^{*}=0$. Once $p_{-n}\left(\bar{x}_{n}^{*}\right)$ reaches 1 , the UMDA will miss the global optimum forever. Therefore, we need to check whether an individual whose first $n-1$ bits are all 1's can be generated before $p_{-n}\left(\bar{x}_{n}^{*}\right)$ reaches 1 .

We start from analyzing the converging speed of the first $n-1$ bits of individuals, given polynomial population sizes $M=\omega\left(n^{2+\alpha} \log n\right), N=\omega\left(n^{2+\alpha} \log n\right)$ (where $\alpha$ can be any positive constant), and $M=\beta N(\beta \in(0,1)$ is some constant) for the UMDA. These bits can be classified into two categories. The first category is exposed to the selection pressure, and the second one is affected by the genetic drift. Unlike the previous section, here we analyze from an optimistic viewpoint: all bits of the first category will converge in one generation, and the genetic drift will promote the marginal probabilities of generating the optimal value on the remaining bits. We first consider the genetic drift of a typical marginal probability, say $p_{-q}\left(x_{q}^{*}\right)$ (the $q$ th bits belong to the second category). Using Chernoff bounds to study the deviations brought by the random sampling procedures, we have

$$
\begin{aligned}
\mathbb{P}\left(N_{t, q}\left(x_{q}^{*}\right) \leq(1+\eta) p_{t-1, q}\left(x_{q}^{*}\right) N \mid p_{t-1, q}\left(x_{q}^{*}\right)\right) \\
>1-e^{-\frac{P_{t-1, q}\left(x_{q}^{*}\right) N}{4}-\eta^{2}}
\end{aligned}
$$

where $\eta$ is a parameter that controls the size of deviation, and $N_{t, q}\left(x_{q}^{*}\right)$ is the number of individuals that takes the value $x_{q}^{*}$ in their $q$ th bit in the population before selection. Set $\eta=\binom{1}{n}^{1+\frac{\eta}{2}}$, we obtain

$$
\begin{aligned}
& \mathbb{P}\left(N_{t, q}\left(x_{q}^{*}\right) \leq\left(1+\binom{1}{n}^{1+\frac{\eta}{2}}\right) p_{t-1, q}\left(x_{q}^{*}\right) N\right. \\
& \left.\quad p_{t-1, q}\left(x_{q}^{*}\right)\right) \\
& >1-e^{-\frac{P_{t-1, q}\left(x_{q}^{*} \log \log n\right)}{4}}=1-n^{-\frac{P_{t-1, q}\left(x_{q}^{*} \log (1)}{4}}
\end{aligned}
$$

The selection procedure may also bring some deviations. Since the $q$ th bits of individuals are not exposed to the selection pressure, then for these bits the selection procedure can be regarded as Simple Random Sampling without replacement.

Lemma 4 can be used to estimate the probability that the number of individuals taking the value $x_{q}^{*}$ on their $q$ th bits after selection [denoted by $N_{t, j}^{(s)}\left(x_{q}^{*}\right)$ ] is bounded from above, which is lower bounded by $1-e^{-2(1+\eta)^{2} p_{t-1, q}^{2}\left(x_{q}^{*}\right) \eta^{2} M}$ estimated by (23) in Table VII, where $\eta^{\prime}$ is a parameter that controls the size of deviation, and $N_{t, q}^{(s)}\left(x_{q}^{*}\right)=p_{t, q}\left(x_{q}^{*}\right) M$. Let $\eta^{\prime}=\eta=\binom{1}{n}^{1+\frac{\eta}{2}}$, since $M=\omega\left(n^{2+\alpha} \log n\right)$ we get

$$
\begin{aligned}
\mathbb{P}\left(p_{t, q}\left(x_{q}^{*}\right)\right. & \leq\left(1+\binom{1}{n}^{1+\frac{\eta}{2}}\right)^{2} p_{t-1, q}\left(x_{q}^{*}\right) \mid p_{t-1, q}\left(x_{q}^{*}\right) \\
& >\left(1-n^{-p_{t-1, q}\left(x_{q}^{*} \log (1)}\right) \quad\right. \\
& \left.\cdot\left(1-n^{-\left(1+\left(\frac{1}{n}\right)^{1+\frac{\eta}{2}}\right)^{2} p_{t-1, q}^{2}\left(x_{q}^{*} \log (1)\right.}\right)\right. \\
& >\left(1-n^{-\left(1+\left(\frac{1}{n}\right)^{1+\frac{\eta}{2}}\right)^{2} p_{t-1, q}^{2}\left(x_{q}^{*} \log (1)\right.}\right)^{2}
\end{aligned}
$$

Since $R=\left(1+\binom{1}{n}^{1+\frac{\eta}{2}}\right)^{2}>1$ (thus we know that $\hat{p}_{t-1, q}\left(x_{q}^{*}\right)>\hat{p}_{0, q}\left(x_{q}^{*}\right)$ in the above inequality), similar to the analysis shown in Table III, we further have

$$
\begin{aligned}
& \mathbb{P}\left(p_{t, q}\left(x_{q}^{*}\right) \leq\left(1+\binom{1}{n}^{1+\frac{\eta}{2}}\right)^{2 t} p_{0, q}\left(x_{q}^{*}\right)\right. \\
& \left.\quad p_{0, q}\left(x_{q}^{*}\right)=\hat{p}_{0, q}\left(x_{q}^{*}\right)\right) \\
& >\left(1-n^{-\left(1+\left(\frac{1}{n}\right)^{1+\frac{\eta}{2}}\right)^{2} \hat{p}_{0, q}\left(x_{q}^{*} \log (1)\right.}\right)^{2 t}
\end{aligned}
$$

Given any polynomial $t$, the above probability is an overwhelming one. Specifically, $\forall t=O(n), p_{t, q}\left(x_{q}^{*}\right)$ is upper bounded as

$$
\begin{aligned}
& p_{t, q}\left(x_{q}^{*}\right) \leq\left(1+\binom{1}{n}^{1+\frac{\eta}{2}}\right)^{O(n)} \hat{p}_{0, q}\left(x_{q}^{*}\right) \\
& =\frac{1}{2}+\Theta\left(\frac{1}{\alpha^{c / 2}}\right)+o\left(\frac{1}{\alpha^{c / 2}}\right)<c<1
\end{aligned}
$$

with an overwhelming probability (where $c$ is some positive constant, and the $q$ th bits are not exposed to the selection pressure).

Another key issue of our analysis is the time $T_{n}^{*}$ for the $n$th marginal probability $p_{-n}\left(\bar{x}_{n}^{*}\right)$ to converge to 1 . We can prove the following lemma.

Lemma 6: The number of generations required by the marginal probability $p_{-n}\left(\bar{x}_{n}^{*}\right)$ to converge to 1 , i.e. $T_{n}^{*}$, is upper bounded by

$$
U=\frac{\ln \frac{2 M}{N}-\ln (1-\delta)}{\ln (1-\delta)+\ln \left(\frac{M}{M}\right)}+2
$$

with an overwhelming probability, if no global optimum is generated before the $U$ th generation, where $\delta \in\left(\max \left[0,1-\frac{2 M}{N}\right], 1-\frac{M}{N}\right)$ is a positive constant.

The proof is provided in the Appendix. Given polynomial population sizes $M=\omega\left(n^{2+\alpha} \log n\right), N=\omega\left(n^{2+\alpha} \log n\right)$ (where $\alpha$ can be any positive constant), and $M=\beta N(\beta \in(0,1)$ is some constant), Lemma 6 implies that $U=\Theta(1)$. Now we reach the following theorem.

Theorem 3: Given polynomial population sizes $M=$ $\omega\left(n^{2+\alpha} \log n\right), N=\omega\left(n^{2+\alpha} \log n\right)$ (where $\alpha$ can be any positive constant), and $M=\beta N(\beta \in(0,1)$ is some constant), the FHT

of the UMDA with truncation selection on the BVLEADINGONES problem is infinity with an overwhelming probability. In other words, the UMDA with truncation selection cannot find the optimum of the BVLEADINGONES problem with an overwhelming probability.

Proof: We have proven that the number of generations required for $p_{-n}\left(\bar{x}_{n}^{*}\right)$ to reach 1 (denoted by $T_{n}^{\prime}$ ) is upper bounded by a constant function $U$ with an overwhelming probability, under the condition that no global optimum is generated before the $U$ th generation. We now further prove that the probability that no global optimum is generated before the $U$ th generation is also overwhelming.

As mentioned before, we classify the first $n-1$ bits of individuals into two categories. The first category, which contains the bits being exposed to the selection, further contains two types of bits. The first type contains the bits which have already converged to the optimal values, and the second type contains the bits that are exposed to the selection pressure but have not converged to the optimal values yet. In our best case analysis, for the bits of the second type, we consider that only one generation is needed for the corresponding marginal probabilities (to the optimal values) to converge. In other words, before the $U$ th generation, the marginal probabilities (of the first $n-1$ bits of individuals) are either 1 or no more than the constant $c$. Noting that $U=\Theta(1)$, according to (31), $c \in\left(\frac{1}{2}, 1\right)$, and it demonstrates the result of genetic drift within $O(n)$ generations.

From an optimistic viewpoint, we further consider that in every generation, besides the marginal probability $p_{-n}\left(\bar{x}_{n}^{*}\right)$, at most $\log ^{2} n$ other marginal probabilities ${ }^{7}$ are also converging with an overwhelming probability. $\log ^{2} n$ is used here because the joint probability of generating $\log ^{2} n$ consecutive 1's (so as to produce the selection pressure on the corresponding bits) by $\log ^{2} n$ non-converged marginal probabilities is no more than $c^{\log ^{2} n}$, which is super-polynomially small.

The above result implies that the probability of generating the global optimum in one generation is also superpolynomially small. Noting that $U=\Theta(1)$, then the probability of generating the optimum before the $U$ th generation is also super-polynomially small. Combining this probability with the conditional probability mentioned in Lemma 6, we know that the joint probability that no global optimum is generated before the $U$ th generation, and $p_{-n}\left(\bar{x}_{n}^{*}\right)$ converges to 1 no later than the $U$ th generation, is super-polynomially close to 1 , i.e., an overwhelming probability. Combining with the fact that once the $n$th marginal probability $p_{-n}\left(x_{n}^{*}\right)$ has already converged to 0 , the probability of finding the optimum will drop to 0 , we have proven the theorem.

According to Theorem 1, given polynomial population sizes $M=\omega\left(n^{2 \text { int }} \log n\right)$ and $N=\omega\left(n^{2 \text { int }} \log n\right)(M=\beta N, \beta \in$ $(0,1)$ is a constant.), BVLEADINGONES is EDA-hard for the UMDA.

For the sake of consistence, we also provide the formal description of the deterministic dynamic system utilized in this section. Considering the $i$ th stage $\left(i \leq \min \left\{T_{n}^{\prime}, \frac{n-1}{\log ^{2} n}\right\}\right)$

[^0]which starts when all the marginal probabilities $p_{-k}\left(x_{k}^{*}\right)$ ( $k \leq$ $\left.(i-1) \log ^{2} n\right\}$ ) have just converged to 1 and ends when all the marginal probabilities $p_{-j}\left(x_{j}^{*}\right)\left(j \leq i \log ^{2} n\right)$ have just converged to 1 , we can obtain $\hat{\mathbf{P}}_{t+1}\left(\mathbf{x}^{*}\right)$ by defining $\gamma_{i}$ as follows.

$$
\begin{gathered}
\hat{\mathbf{P}}_{t+1}\left(\mathbf{x}^{*}\right)=\gamma_{i}\left(\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)\right)= \\
\left(\hat{p}_{t, 1}\left(x_{1}^{*}\right), \ldots, \hat{p}_{t,(i-1) \log ^{2} n}\left(x_{(i-1) \log ^{2} n}^{*}\right), 1, \ldots, 1\right. \\
R \hat{p}_{t, i \log ^{2} n+1}\left(x_{i \log ^{2} n+1}^{*}\right), \ldots, R \hat{p}_{t, n-1}\left(x_{n-1}^{*}\right) \\
\left.1-G\left(1-\hat{p}_{t, n}\left(x_{n}^{*}\right)\right)\right)
\end{gathered}
$$

where $R=(1+\eta)\left(1+\eta^{\prime}\right)\left(\eta<1\right.$ and $\eta^{\prime}<1$ are positive functions of the problem size $n$ ), and $G=(1-\delta) \frac{N}{M}$ ( $\delta \in$ $\left.\left(\max \left\{0,1-\frac{2 M}{N}\right\}, 1-\frac{M}{N}\right)\right.$ is a constant). In the above equation, we consider four different cases.

1) $j \in\left\{1, \ldots,(i-1) \log ^{2} n\right\}$. In the deterministic system above, the marginal probabilities $\hat{p}_{t, j}\left(x_{j}^{*}\right)$ have converged to 1 , thus at the next generation they will not change.
2) $j \in\left\{(i-1) \log ^{2} n+1, \ldots, i \log ^{2} n\right\}$. In the deterministic system above, the marginal probabilities $\hat{p}_{t, j}\left(x_{j}^{*}\right)$ are converging to the optimum, and they will converge in one generation in the best case analysis.
3) $j \in\left\{i \log ^{2} n+1, \ldots, n-1\right\}$. The $j$ th bits of individuals are not exposed to selection pressure, and we use the factor $R=(1+\eta)\left(1+\eta^{\prime}\right)$ to demonstrate the impact of genetic drift in the deterministic system above.
4) $j=n$. The marginal probability $\hat{p}_{t, n}\left(\bar{x}_{n}^{*}\right)=1-\hat{p}_{t, n}\left(x_{n}^{*}\right)$ is converging, and we use the factor $G=(1-\delta) \frac{N}{M}$ to demonstrate the impact of selection pressure on this converging marginal probability in the deterministic system above, which is a best case style for $\hat{p}_{t, n}\left(x_{n}^{*}\right)$.
With $\hat{\mathbf{P}}_{0}\left(\mathbf{x}^{*}\right)=\left(\frac{1}{2}, \ldots, \frac{1}{2}\right)$, noting that one stage actually refers to one generation (thus $i=t$ ), we have

$$
\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)=\gamma_{t} \circ \gamma_{t-1} \ldots \circ \gamma_{1}\left(\hat{\mathbf{P}}_{0}\left(\mathbf{x}^{*}\right)\right)
$$

where $t \leq \min \left\{T_{n}^{\prime}, \frac{n-1}{\log ^{2} n}\right\}$. Since $\left\{\gamma_{t}\right\}_{t=1}^{1}$ de-randomizes the whole optimization process, $T_{n}^{\prime}$ in the above equation is no longer random variable. For the sake of clarity, we rewrite the above equation as

$$
\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)=\gamma_{t} \circ \gamma_{t-1} \ldots \circ \gamma_{1}\left(\hat{\mathbf{P}}_{0}\left(\mathbf{x}^{*}\right)\right)
$$

where $t \leq \min \left\{\tilde{T}_{n}^{\prime}, \frac{n-1}{\log ^{2} n}\right\} \leq \min \left\{U, \frac{n-1}{\log ^{2} n}\right\}$.

## VI. A MODIFIED UMDA: RELAXATION by MARGINS

So far we have seen both EDA-easy and EDA-hard problems for the UMDA. This section will analyze more in-depth the relationship between EDA-hardness and the algorithms. The BVLEADINGONES problem, which has proven to be EDA-hard for the UMDA with finite populations, will be employed as the target problem in this section. We will show that a simple "relaxed" version of UMDA with truncation


[^0]:    ${ }^{7}$ For the sake of brevity, we assume that $\log ^{2} n$ is an integer and thus omit the notation " 1 ."

selection can solve the BVLEADINGONES problem efficiently. The "relaxation" is implemented by adding some "margins" to the marginal probabilities of the UMDA. That is, the highest level the marginal probabilities can reach is $1-\frac{1}{M}$ and the lowest level the marginal probabilities can drop to is $\frac{1}{M}$. Any marginal probabilities higher than $1-\frac{1}{M}$ are set to be $1-\frac{1}{M}$, and any marginal probabilities lower than $\frac{1}{M}$ are set to be $\frac{1}{M}$. We denote such a UMDA with margin as UMDA $_{M}$. The margins here aim to avoid the premature convergence, which is similar to the upper and lower bounds of the pheromone information in Max-Min Ant System [40] and Laplace correction [2]. It is noteworthy that we are not trying to propose a new algorithm here. Instead, by an example, we are trying to demonstrate theoretically that some approaches proposed to avoid premature convergence of EDAs, can actually help to promote the performance of the algorithms.

We have seen in the previous section that the original UMDA cannot solve BVLEADINGONES efficiently. Interestingly, by adding the margins, the UMDA $_{M}$ can solve BVLEADINGONES efficiently. The following theorem summarizes the main result.

Theorem 4: Given polynomial population sizes $N=$ $\omega\left(n^{2 \pi \alpha} \log n\right), M=\omega\left(n^{2 \pi \alpha} \log n\right)$ (where $\alpha$ can be any positive constant) and $M=\beta N(\beta \in(0,1)$ is some constant), then for any constant $\delta$ that satisfies $\delta \in\left(\max \left\{0,1-\frac{2 M}{N}\right\}, 1-e^{\frac{-\delta \cdot M}{N}}\right)$ (where $\epsilon(n)=\frac{M}{n}$ ), the first hitting time $\tau$ of the UMDA $_{M}$ with truncation selection (initialized with a uniform distribution) satisfies

$$
\begin{aligned}
\tau<\bar{\tau}=\frac{\left(\ln \frac{\epsilon(M-1)}{N}-\ln (1-\delta)\right) n \epsilon(n)+n}{\epsilon(n) \ln (1-\delta)+\epsilon(n) \ln \left(\frac{N}{M}\right)-1} \\
+\frac{M}{N} \ln ^{2} n+2 n
\end{aligned}
$$

with the overwhelming probability

$$
\begin{aligned}
& \left(1-n^{-e^{-1 /(\omega)_{\omega}\left(n^{2 \pi \alpha}\right) \beta^{2} / 2 \alpha}}\right)^{2 \bar{\tau}} \\
& \quad\left(1-n^{-\left(1-\left(\frac{1}{2}\right)^{1+\frac{\alpha}{2}}\right)^{2} \omega(1)}\right)^{2(n-1) \bar{\tau}} \\
& \quad\left(1-\left(\frac{1}{e}\right)^{\omega(\ln n)}\right)
\end{aligned}
$$

Proof: In order to proof the above theorem, we define $n+1$ random variables $t_{0}$ and $t_{i}(i=1, \ldots, n)$ as follows:

$$
\begin{aligned}
& t_{0} \triangleq \min \left\{t ; p_{t, n}\left(\bar{x}_{n}^{*}\right)=1-\frac{1}{M}\right\} \\
& t_{i} \triangleq \min \left\{t ; p_{t, i}\left(x_{i}^{*}\right)=1-\frac{1}{M}\right\}
\end{aligned}
$$

The proof follows our basic idea introduced in Section III-A, and thus is similar to the proof of Theorem 2. However, the maximal value that a marginal probability can reach drops to $1-\frac{1}{M}$, and the minimal value that a marginal probability can reach increases to $\frac{1}{M}$. We will then de-randomize the UMDA $_{M}$.

In the analysis, we ignore the possibility that the optimum is found before the $t_{0}$ th generation (which will make the FHT smaller), and we divide the optimization process into $(n+1)$ th stages. The $1^{\text {st }}$ stage begins when the optimization begins, and ends when the marginal probability $\bar{p}_{., n}\left(\bar{x}_{n}^{*}\right)$ reaches $1-\frac{1}{M}$
for the first time. The $2^{\text {nd }}$ stage follows the $1^{\text {st }}$ stage, and ends when the marginal probability $\bar{p}_{., 1}\left(x_{1}^{*}\right)$ reaches $1-\frac{1}{M}$ for the first time. The $q$ th stage $(q \in\{2, \ldots, n\})$ begins when the marginal probability $\bar{p}_{., q-2}\left(x_{q-2}^{*}\right)$ reaches $1-\frac{1}{M}$ for the first time, and ends when the marginal probability $\bar{p}_{., q-1}\left(x_{q-1}^{*}\right)$ reaches $1-\frac{1}{M}$ for the first time.

Let us consider the deterministic system. Suppose generation $t+1$ belongs to the $i$ th stage $(i \in\{1, \ldots, n+1\})$, then the marginal probabilities at this generation are updated from the marginal probabilities at generation $t$ by $\gamma_{i}$. When $i=1$, we have

$$
\begin{gathered}
\hat{\mathbf{P}}_{t+1}\left(\mathbf{x}^{*}\right)=\gamma_{1}\left(\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)\right)= \\
\left(R \bar{p}_{t, 1}\left(x_{1}^{*}\right), \ldots, R \bar{p}_{t, n-1}\left(x_{n-1}^{*}\right)\right. \\
\left.1-G_{1}\left(1-\bar{p}_{t, n}\left(x_{n}^{*}\right)\right)\right)
\end{gathered}
$$

where $R=(1-\eta)\left(1-\eta^{\prime}\right)\left(\eta<1\right.$ and $\eta^{\prime}<1$ are positive functions of the problem size $n$ ), and $G_{1}=(1-\delta) \frac{N}{M}$ $\left(\delta \in\left(\max \left\{0,1-\frac{2 M}{N}\right\}, 1-e^{\frac{-\delta \cdot M}{N}}\right)\right.$ is a constant). In the above equation, we consider two different cases.

1) $j \in\{1, \ldots, n-1\}$. In the deterministic system above, the $j$ th bits of individuals are not exposed to selection pressure, and we use the factor $R=(1-\eta)(1-\eta^{\prime})$ to demonstrate the impact of genetic drift on these marginal probabilities.
2) $j=n$. In the deterministic system above, the marginal probability $\bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)=1-\bar{p}_{t, n}\left(x_{n}^{*}\right)$ is increasing, and we use the factor $G_{1}=(1-\delta) \frac{N}{M}$ to demonstrate the impact of selection pressure on the increasing marginal probability $\bar{p}_{., n}\left(\bar{x}_{n}^{*}\right)\left(\bar{p}_{t+1, n}\left(\bar{x}_{n}^{*}\right)=G_{1} \bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)\right.$, thus $\bar{p}_{t+1, n}\left(x_{n}^{*}\right)=$ $1-G_{1} \bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)=1-G_{1}\left(1-\bar{p}_{t, n}\left(x_{n}^{*}\right)\right.$ holds $)$.
When $i \in\{2, \ldots, n\}$, we have

$$
\begin{gathered}
\hat{\mathbf{P}}_{t+1}\left(\mathbf{x}^{*}\right)=\gamma_{i}\left(\hat{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)\right) \\
=\left(\bar{p}_{t, 1}\left(x_{1}^{*}\right), \ldots, \bar{p}_{t, i-2}\left(x_{i-2}^{*}\right)\right. \\
\left.G_{2} \bar{p}_{t, i-1}\left(x_{i-1}^{*}\right), R \bar{p}_{t, i}\left(x_{i}^{*}\right), \ldots\right. \\
R \bar{p}_{t, n-1}\left(x_{n-1}^{*}\right), \bar{p}_{t, n}\left(x_{n}^{*}\right)\right)
\end{gathered}
$$

where $G_{2}=(1-\delta)\left(1-\frac{1}{M}\right)^{n} \frac{N}{M}\left(\delta \in\left(\max \left\{0,1-\frac{2 M}{N}\right\}, 1-e^{\frac{-\delta \cdot M}{N}}\right)\right.$ is a constant), and $R=(1-\eta)\left(1-\eta^{\prime}\right)\left(\eta<1\right.$ and $\eta^{\prime}<1$ are positive functions of the problem size $n$ ). In the above equation, we consider four different cases for the deterministic system above.

1) $j \leq i-2, j \in \mathbb{N}^{+}$. The marginal probabilities $\bar{p}_{t, j}\left(x_{j}^{*}\right)$ have reached $1-\frac{1}{M}$, and at the next generation they will not change (we will soon prove this).
2) $j=i-1$. The marginal probability $\bar{p}_{t, j}\left(x_{j}^{*}\right)$ is increasing, and we use the factor $G_{2}=(1-\delta)\left(1-\frac{1}{M}\right)^{n} \frac{N}{M}$ to demonstrate the impact of selection pressure on this increasing marginal probability.
3) $j \in\{i, \ldots, n-1\}$. The $j$ th bits of individuals are not exposed to selection pressure, and we use the factor $R=$ $(1-\eta)\left(1-\eta^{\prime}\right)$ to demonstrate the impact of genetic drift on these marginal probabilities.
4) $j=n$. The marginal probabilities $\bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)$ and $\bar{p}_{t, n}\left(x_{n}^{*}\right)$ have reached $1-\frac{1}{M}$ and $\frac{1}{M}$ respectively, and at the next

TABLE VIII
Calculation of Probability That $t_{0}$ Is Upper Bounded by $\tilde{t}_{0}$

$$
\begin{aligned}
& \mathbb{P}\left(t_{0} \leq \tilde{t}_{0} \mid p_{0, n}\left(\tilde{x}_{n}^{*}\right)=\tilde{p}_{0, n}\left(\tilde{x}_{n}^{*}\right)\right) \\
> & \mathbb{P}\left(p_{\tilde{t}_{0}-1,1}(1) \geq \frac{M-1}{N(1-\delta)} \mid p_{0, n}\left(\tilde{x}_{n}^{*}\right)=\tilde{p}_{0, n}\left(\tilde{x}_{n}^{*}\right)\right)\left(1-e^{-\frac{\tilde{t}_{0, n}(1) N}{\delta} \tilde{p}}\right) \\
& >\mathbb{P}\left(p_{\tilde{t}_{0}-1,1}(1) \geq \tilde{p}_{\tilde{t}_{0}-1,1}(1)=G^{\tilde{t}_{0}-1} p_{0, n}\left(\tilde{x}_{n}^{*}\right)>\frac{M-1}{N(1-\delta)} \mid p_{0, n}\left(\tilde{x}_{n}^{*}\right)=\tilde{p}_{0, n}\left(\tilde{x}_{n}^{*}\right)\right)\left(1-e^{-\frac{\tilde{t}_{0,1}(1) N}{\delta} \tilde{p}}\right) \\
& >\mathbb{P}\left(p_{\tilde{t}_{0}-1,1}(1) \geq \tilde{p}_{\tilde{t}_{0}-1, n}\left(\tilde{x}_{n}^{*}\right) \mid p_{0, n}\left(\tilde{x}_{n}^{*}\right)=\tilde{p}_{0, n}\left(\tilde{x}_{n}^{*}\right), \tilde{p}_{\tilde{t}_{0}-1, n}\left(\tilde{x}_{n}^{*}\right)>\frac{M-1}{N(1-\delta)}\right) \\
& \cdot \mathbb{P}\left(\tilde{p}_{\tilde{t}_{0}-1, n}\left(\tilde{x}_{n}^{*}\right)>\frac{M-1}{N(1-\delta)} \mid p_{0, n}\left(\tilde{x}_{n}^{*}\right)=\tilde{p}_{0, n}\left(\tilde{x}_{n}^{*}\right)\right)\left(1-e^{-\tilde{p}_{0, n}\left(\tilde{x}_{n}^{*}\right) N \tilde{\delta}^{2} / 2}\right)
\end{aligned}
$$

TABLE IX
CALCULATION of (34) AND (35)

$$
\begin{aligned}
& G_{2}^{\tilde{t}_{i-1} \tilde{t}_{i-1}-2} p_{\tilde{t}_{i-1}, i}\left(x_{i}^{*}\right)=(1-\delta)^{\tilde{t}_{i-1} \tilde{t}_{i-1}-2}\left(1-\frac{1}{M}\right)^{\left(\tilde{t}_{i}-\tilde{t}_{i-1}-2\right) n}\left(\frac{N}{\tilde{M}}\right)^{\tilde{t}_{i}-\tilde{t}_{i-1}-2} \tilde{p}_{\tilde{t}_{i-1}, i}\left(x_{i}^{*}\right)<\frac{M-1}{N(1-\delta) 1-\frac{1}{M} N} \\
& G_{2}^{\tilde{t}_{i}-\tilde{t}_{i-1}-1} p_{\tilde{t}_{i-1}, i}\left(x_{i}^{*}\right)=(1-\delta)^{\tilde{t}_{i}-\tilde{t}_{i-1}-1}\left(1-\frac{1}{M}\right)^{\left(\tilde{t}_{i}-\tilde{t}_{i-1}-1\right) n}\left(\frac{N}{\tilde{M}}\right)^{\tilde{t}_{i}-\tilde{t}_{i-1}-1} \tilde{p}_{\tilde{t}_{i-1}, i}\left(x_{i}^{*}\right) \geq \frac{M-1}{N(1-\delta) 1-\frac{1}{M} N}
\end{aligned}
$$

generation they will not change (we will soon prove this).
Consider the $(n+1)$ th stage, we have

$$
\begin{gathered}
\tilde{\mathbf{P}}_{t+1}\left(\mathbf{x}^{*}\right)=\gamma_{n+1}\left(\tilde{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)\right) \\
=\left(\tilde{p}_{t, 1}\left(x_{1}^{*}\right), \ldots, \tilde{p}_{t, n-1}\left(x_{n-1}^{*}\right), \tilde{p}_{t, n}\left(x_{n}^{*}\right)\right)
\end{gathered}
$$

where we consider two different cases for this deterministic system.

1) $j \in\{1, \ldots, n-1\}$. The marginal probabilities $\tilde{p}_{t, j}\left(x_{j}^{*}\right)$ have reached $1-\frac{1}{M}$, and at the next generation they will not change (we will soon prove this).
2) $j=n$. The marginal probability $\tilde{p}_{t, n}\left(x_{n}^{*}\right)$ is always no smaller than $\frac{1}{M}$.
With $\tilde{\mathbf{P}}_{0}\left(\mathbf{x}^{*}\right)=\left(\frac{1}{2}, \ldots, \frac{1}{2}\right)$, we have

$$
\tilde{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)=\gamma_{t}^{t-t_{i-2}}\left(\tilde{\mathbf{P}}_{t_{i-2}}\left(\mathbf{x}^{*}\right)\right)
$$

where $t_{i-2}<t \leq t_{i-1}(i=1, \ldots, n+1)$, and we let $t_{-1}=$ 0 represent the beginning of the optimization process. Since $\left\{\gamma_{i}\right\}_{i=1}^{n+1}$ de-randomizes the whole optimization process, $\left\{t_{i}\right\}_{i=0}^{n}$ in the above equation are no longer random variables. For the sake of clarity, we rewrite the above equation as

$$
\tilde{\mathbf{P}}_{t}\left(\mathbf{x}^{*}\right)=\gamma_{t}^{t-\tilde{t}_{i-2}}\left(\tilde{\mathbf{P}}_{\tilde{t}_{i-2}}\left(\mathbf{x}^{*}\right)\right)
$$

where $\tilde{t}_{i-2}<t \leq \tilde{t}_{i-1}(i=1, \ldots, n+1)$. As we will show immediately, $\tilde{t}_{i}(0 \leq i \leq n)$ is an upper bound of the random variable $t_{i}$ with some probability. Once all $\tilde{t}_{i}$ can be estimated, and all the marginal probabilities $p_{t, j}\left(x_{j}^{*}\right)(j=1, \ldots, n)$ have
reached $1-\frac{1}{M}$, the optimum might already be found, or it will take only a few steps to generate the optimum. Thus, if we can prove that once the marginal probabilities $p_{t, j}\left(x_{j}^{*}\right)(j=$ $1, \ldots, n-1)$ have reached $1-\frac{1}{M}$, it will never reduce again, our task finally becomes calculating the $\tilde{t}_{n}$, the probability that $\tilde{t}_{n}$ holds as an upper bound of $t_{n}$.

We now provide the formal proof stage by stage. At the $1^{\text {st }}$ stage, we analyze the case with the $n$th bit. At the $t$ th generation (which belongs to the $1^{\text {st }}$ stage), according to Lemma 5 and Chernoff bounds, we have

$$
\begin{aligned}
& \mathbb{P}\left(p_{t, n}\left(\tilde{x}_{n}^{*}\right) \geq(1-\delta) \frac{p_{t-1, n}\left(\tilde{x}_{n}^{*}\right) N}{M}\right. \\
& \left.\quad \mid p_{t-1, n}\left(\tilde{x}_{n}^{*}\right) \leq \frac{M-1}{N(1-\delta)}\right) \\
& >1-e^{-p_{t-1, n}\left(\tilde{x}_{n}^{*}\right) N \delta^{2} / 2}
\end{aligned}
$$

where $\delta \in\left(\max \left\{0,1-\frac{2 M}{N}\right\}, 1-e^{\frac{1}{n+1} \frac{M}{N}}\right)$ is a positive constant, and $p_{t, n}\left(\tilde{x}_{n}^{*}\right) \leq 1-\frac{1}{M}$ (since the UMDA adopts margins) yields the condition that $p_{t-1, n}\left(\tilde{x}_{n}^{*}\right) \leq \frac{M-1}{N(1-\delta)}$. Similar to Table III in the proof of Theorem 2 we can obtain

$$
\begin{aligned}
\mathbb{P}\left(p_{t, n}\left(\tilde{x}_{n}^{*}\right) \geq\right. & G_{1}^{t} p_{0, n}\left(\tilde{x}_{n}^{*}\right) \mid p_{0, n}\left(\tilde{x}_{n}^{*}\right)=\tilde{p}_{0, n}\left(\tilde{x}_{n}^{*}\right)\right) \\
& >\left(1-e^{-p_{0, n}\left(\tilde{x}_{n}^{*}\right) N \delta^{2} / 2}\right)^{t}
\end{aligned}
$$

Consider the probability that $t_{0}$ is upper bounded by some value, say $\tilde{t}_{0}$, we obtain the inequalities estimated in Table VIII, where in (33) the factor $\left(1-e^{-\tilde{p}_{0, n}\left(\tilde{x}_{n}^{*}\right) N \delta^{2} / 2}\right)$ is

added since we apply Chernoff bounds at the end of the $\left(\bar{t}_{0}-1\right)$ th generation. Now we consider the following item:

$$
\begin{gathered}
\mathbb{P}\left(\bar{p}_{t_{0}-1, n}\left(\bar{x}_{n}^{*}\right)>\frac{M-1}{N(1-\delta)} \mid p_{0, n}\left(\bar{x}_{n}^{*}\right)=\bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)\right) \\
=\mathbb{P}\left(\bar{p}_{t_{0}-1, n}\left(\bar{x}_{n}^{*}\right)>\frac{M-1}{N(1-\delta)}\right)
\end{gathered}
$$

Since $\left\{\bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)\right\}_{t=0}^{\infty}$ is a deterministic sequence, the probability above must be either 0 or 1 . We need to find the value of $\bar{t}_{0}$ that makes the above probability 1 . Given that $\bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)=\frac{1}{2}$, the definition of $\bar{t}_{0}$ (it is an upper bound of $t_{0}$ defined at the beginning of the proof) and the condition that $\forall t<\bar{t}_{0}-1$ : $\frac{M-1}{N(1-\delta)}>\bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)>(1-\delta) \frac{\bar{p}_{t-1, n}\left(\bar{x}_{n}^{*}\right) N}{M}$ together imply

$$
\begin{gathered}
G_{1}^{\bar{t}_{0}-2} \bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right) \\
=\left((1-\delta)\left(\frac{N}{M}\right)\right)^{\bar{t}_{0}-2} \bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)<\frac{M-1}{N(1-\delta)} \\
G_{1}^{\bar{t}_{0}-1} \bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right) \\
=\left((1-\delta)\left(\frac{N}{M}\right)\right)^{\bar{t}_{0}-1} \bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right) \geq \frac{M-1}{N(1-\delta)}
\end{gathered}
$$

Hence, we obtain the value of $\bar{t}_{0}$

$$
\bar{t}_{0} \leq \frac{\ln \frac{2 M-2}{N}-\ln (1-\delta)}{\ln (1-\delta)+\ln \left(\frac{N}{M}\right)}+2
$$

Now we can continue to estimate the probability mentioned in (32), which can provide us the probability that $t_{0}$ is upper bounded by $\bar{t}_{0}$. Similar to (25) in the proof of Theorem 2 according to (36), we can obtain that the probability is at least $\left(1-e^{-p_{0, n}\left(\bar{x}_{n}^{*}\right) N \delta^{2} / 2}\right)^{\bar{t}_{0}}$.

On the other hand, we can deal with the genetic drift in the same way as we did for Theorem 2: since $\bar{t}_{0}=\Theta(1)$, when $t=\bar{t}_{0}$, for the marginal probabilities of other bits, a level of $\frac{1}{e}$ can be maintained at least with the overwhelming probability of

$$
\left(1-e^{-\frac{\left.\operatorname{se} e^{\lambda_{0} \alpha}\right) \operatorname{se} \alpha \mid \delta^{2}}{2 e}}\right)^{\bar{t}_{0}}\left(1-n^{-\left(1-\left(\frac{1}{2}\right)^{1+\frac{1}{2}}\right)^{2} \operatorname{se}(1)}\right)^{2 \bar{t}_{0}}
$$

where the second factor $\left(1-n^{-\left(1-\left(\frac{1}{2}\right)^{1+\frac{1}{2}}\right)^{2}}\right)^{2} \operatorname{se}(1)\right)^{2 \bar{t}_{0}}$ comes from the analysis of genetic drift (please refer to (26) for details). The proof details will be very similar to those in the proof of Theorem 2. For the sake of brevity, we omit the details. Now we have finished the analysis of the $1^{\text {st }}$ stage.

After the marginal probability $p_{-n}\left(\bar{x}_{n}^{*}\right)$ has reached $1-\frac{1}{M}$, i.e., $t \geq \bar{t}_{0}, p_{-n}\left(\bar{x}_{n}^{*}\right)$ will not drop to a level that is smaller than $1-\frac{1}{M}$ again unless the algorithm has found the optimum. In fact, for other marginal probabilities, similar fact also holds. In order to prove it, let us consider the $(i+1)$ th stage $(1 \leq$ $i<n$ ), and we use the factor $G_{2}$ to demonstrate the impact of selection, by which the interactions among bits are taken into account. For the $i$ th bit, at the $k$ th generation, we can investigate the following situation:

$$
\begin{gathered}
p_{k, i}\left(x_{i}^{*}\right)<1-\frac{1}{M} \\
\forall j \leq i-1: p_{k, j}\left(x_{j}^{*}\right)=1-\frac{1}{M}
\end{gathered}
$$

We will then prove that once $\forall 1 \leq j \leq i-1, p_{-j}\left(x_{j}^{*}\right)$ reach $1-\frac{1}{M}$, with an overwhelming probability, none of them will decrease again with an overwhelming probability. Let $r_{k+1}\left(\left(1^{i-1} * * \cdots * 1\right)\right)$ be the proportion of individuals $\left(1^{i-1} * * \cdots * 1\right)$ before selection at the $(k+1)$ th generation, where $*$ must be either 0 or 1 . According to Chernoff bounds, and with $N>M=\epsilon(n) n$, we have

$$
\begin{gathered}
\mathbb{P}\left(r_{k+1}\left(\left(1^{i-1} * * \cdots * 1\right)\right)>(1-\delta)\left(1-\frac{1}{M}\right)^{i}\right. \\
\left.\mid p_{k, n}\left(\bar{x}_{n}^{*}\right)=1-\frac{1}{M}, \forall j \leq i-1: p_{k, j}\left(x_{j}^{*}\right)=1-\frac{1}{M}\right) \\
>1-e^{-\left(1-\frac{1}{M} j^{i} N \delta^{2} / 2\right.}>1-e^{-\left(1-\frac{1}{M}\right)^{n} N \delta^{2} / 2} \\
>1-e^{-\left(1-\frac{1}{n \operatorname{se} \alpha} j^{n} \epsilon(n) n \delta^{2} / 2\right.} \\
\rightarrow 1-e^{-e^{-1 / n \epsilon}\left(\epsilon(n) n \delta^{2} / 2\right.}
\end{gathered}
$$

which is an overwhelming probability when $n \rightarrow \infty$. Since $\delta \in\left(\max \left\{0,1-\frac{2 M}{N}\right\}, 1-e^{\frac{M}{n \operatorname{se}} \frac{M}{N}}\right)$, we know that

$$
\begin{aligned}
& r_{k+1}\left(\left(1^{i-1} * * \cdots * 1\right)\right) \\
& >(1-\delta)\left(1-\frac{1}{M}\right)^{i} \\
& >(1-\delta)\left(1-\frac{1}{M}\right)^{n}>\frac{M}{N}
\end{aligned}
$$

holds with an overwhelming probability $1-e^{-e^{-1 / n \epsilon}\left(\epsilon(n) n \delta^{2} / 2\right.}$. At the same time, it is obvious that the individuals $\left(1^{i-1} * * \cdots * 1\right)$ have the highest fitness in the population. After truncation selection, according to Lemma 5, we obtain that (note that we use margins for the marginal probabilities)

$$
\begin{gathered}
\mathbb{P}\left(\forall j \leq i-1: p_{k+1, j}\left(x_{j}^{*}\right)=1-\frac{1}{M} \mid p_{k, n}\left(\bar{x}_{n}^{*}\right)=1-\frac{1}{M}\right. \\
\left.\forall j \leq i-1: p_{k, j}\left(x_{j}^{*}\right)=1-\frac{1}{M}\right) \\
>1-e^{-e^{-1 / n \epsilon}\left(\epsilon(n) n \delta^{2} / 2\right.}
\end{gathered}
$$

which means with an overwhelming probability, the marginal probabilities $p_{-j}\left(x_{j}^{*}\right)(\forall j \leq i-1)$ will no longer change once they reach $1-\frac{1}{M}$.

Now we consider the $(i+1)$ th stage $(i \leq n-1)$, at which the $i$ th bits of individuals are of our interest. Similar to the case of the $1^{\text {st }}$ stage, in which the marginal probability $\bar{p}_{-n}\left(\bar{x}_{n}^{*}\right)$ is investigated, we can estimate the time that $\bar{p}_{-i}\left(x_{i}^{*}\right)$ reaches $1-\frac{1}{M}$, i.e., $\bar{t}_{i}(1 \leq i<n)$. As presented in Table IX, it is not hard to obtain (34) and (35).

In order to obtain $\bar{t}_{i}$, we need to know $\bar{p}_{t_{i-1}, i}\left(x_{i}^{*}\right)$ so as to solve (34) and (35). It is worth noting that $\bar{p}_{t_{i-1}, i}\left(x_{i}^{*}\right)$ is related to the genetic drift. Similar to what we did in Section IV, when the bits are not exposed to selection pressure, given that $\bar{t}_{i-1}=\theta(n)$, the marginal probability $\bar{p}_{-i}\left(x_{i}^{*}\right)$ will remain to

be as $\frac{1}{e} .{ }^{8}$ Hence, we have $p_{l_{i-1}, i}\left(x_{i}^{*}\right)>\frac{1}{e}$ holds with the overwhelming probability of

$$
\prod_{k=0}^{i-1}\left(1-n^{-\left(1-\left(\frac{1}{e}\right)^{1+\frac{n}{2}}\right)^{2} \omega(1)}\right)^{2 \tilde{t}_{k}}
$$

where the item

$$
\left(1-n^{-\left(1-\left(\frac{1}{e}\right)^{1+\frac{n}{2}}\right)^{2} \omega(1)}\right)^{2 \tilde{t}_{k}}
$$

represents the probability that the $(k+1)$ th marginal probability is at least $\frac{1}{e}$ after genetic drift. Detailed analysis can be found in the proof of Theorem 2.

Now we can solve the equations given in (34) and (35), and get

$$
\begin{gathered}
\tilde{t}_{i}=\tilde{t}_{0}+\sum_{k=1}^{i}\left(\tilde{t}_{k}-\tilde{t}_{k-1}\right) \\
<\frac{(i+1)\left(\ln \frac{e\left(\tilde{t}_{i-1}\right)-\ln (1-\tilde{t})+\frac{1}{\left(\omega_{i}\right)}\right)}{\ln (1-\tilde{t})+\ln \left(\frac{\tilde{t}_{i}}{\tilde{M}}\right)-\frac{1}{\left(\omega_{i}\right)}} \\
+2(i+1)
\end{gathered}
$$

where $i \leq n-1$ holds.
Next, we need to estimate the joint probability that the random variable $t_{i}$ is upper bounded by $\tilde{t}_{i}$. Since similar work has been done in (32) and (33), and (20) in the proof of Theorem 2, we only informally describe it here for the sake of brevity. This joint probability contains four parts.

1) The probability that $\forall k \in\{1, \ldots, i-1\}: t_{k}<\tilde{t}_{k}$. (It can be obtained by induction. For more details, please refer to (20).)
2) The probability that after genetic drift of the $i$ th bit, the marginal probability $p_{l_{i-1}, i}\left(x_{i}^{*}\right)$ is larger than $\frac{1}{e}$. (We have already mentioned it in (39).)
3) The probability that after the marginal probabilities $p_{-j}\left(x_{j}^{*}\right)(j \neq n)$ have reached $1-\frac{1}{M}$, they will never drop to a lower level again. (We can utilize the result given in (38).)
4) The probability that $p_{t, i}\left(x_{i}^{*}\right)$ is lower bounded by $\tilde{p}_{t, i}\left(x_{i}^{*}\right)$ $\left(\tilde{t}_{i-1}<t \leq \tilde{t}_{i}\right)$, given the condition that $p_{l_{i-1}, i}\left(x_{i}^{*}\right) \geq$ $\tilde{p}_{l_{i-1}, i}\left(x_{i}^{*}\right)$.
Now we briefly estimate the probability mentioned in Item 4 (and a more detailed example can be found in Table III in the proof of Theorem 2). As the first step, we consider the relation between $p_{t, i}\left(x_{i}^{*}\right)$ and $p_{t-1, i}\left(x_{i}^{*}\right)$ ( $\tilde{t}_{i-1}<$ $t \leq \tilde{t}_{i}$ ) by applying Chernoff bounds twice. As a result, we obtain the inequalities presented in Table X, where we utilize " $\min$ " to take into account the situation in which $(1-\delta) \frac{\tilde{t}_{i}^{*}}{M} p_{t-1, i}\left(x_{i}^{*}\right) p_{t-1, n}\left(x_{i}^{*}\right) \prod_{j=1}^{i-1} p_{t-1, j}\left(x_{j}^{*}\right)>1-\frac{1}{M}$ holds. In this case, noting that the UMDA has adopted margins, the
${ }^{8}$ For the sake of brevity, we write the results of different stages together. It is noteworthy that the proof here contains no loop, since we can prove the result for different values of $i(i=1, \ldots, n-1$ is the index of bits) one after another as we have done in Theorem 2. Similar to the case of Theorem 2, since $\forall i=1, \ldots, n-1, \tilde{t}_{i}-\tilde{t}_{i-1}=\Theta(1)$, the sum of at most $i$ such items [see (40)] is always $O(n)$, and the impact of genetic drift can be estimated as we have done in Theorem 2 for the $(i+1)$ th bit: at least a level of $1 / e$ can be maintained with an overwhelming probability.
marginal probability $p_{t, i}\left(x_{i}^{*}\right)$ is set to be $1-\frac{1}{M}$. By setting the condition of the above probability as $p_{t-1, i}\left(x_{i}^{*}\right) \geq \tilde{p}_{t-1, i}\left(x_{i}^{*}\right)=$ $G_{2}^{i-\tilde{t}_{i-1}-1} \tilde{p}_{l_{i-1}, i}\left(x_{i}^{*}\right)$, the above inequality further implies that

$$
\begin{gathered}
\mathbb{P}\left(p_{t, i}\left(x_{i}^{*}\right) \geq \min \left\{G_{2} p_{t-1, i}\left(x_{i}^{*}\right), 1-\frac{1}{M}\right\}\right. \\
\left.\mid p_{t-1, i}\left(x_{i}^{*}\right) \geq G_{2}^{i-\tilde{t}_{i-1}-1} \tilde{p}_{l_{i-1}, i}\left(x_{i}^{*}\right)\right) \\
>1-e^{-\left(1-\frac{1}{M} \rho G_{2}^{i-\tilde{t}_{i-1}-1} \tilde{p}_{l_{i-1}, i}\left(x_{i}^{*}\right) N \delta^{2} / 2\right.} \\
>1-e^{-\left(1-\frac{1}{M} \rho \tilde{p}_{l_{i-1}, i}\left(x_{i}^{*}\right) N \delta^{2} / 2\right.} \\
>1-e^{-\left(1-\frac{1}{M} \rho N \delta^{2} / 2 e\right.}
\end{gathered}
$$

holds, where we utilize the facts that $\tilde{p}_{l_{i-1}, i}\left(x_{i}^{*}\right)>\frac{1}{e}$ holds with an overwhelming probability (the consequence of genetic drift. Original analysis can be found before (27), and $G_{2}>1$ (which ensures that $\tilde{p}_{t, i}\left(x_{i}^{*}\right)$ is mono-increasing when the time index $t$ satisfies $\tilde{t}_{i-1}<t \leq \tilde{t}_{i}$ ). As a consequence of the above inequality, similar to Table III in the proof of Theorem 2, we obtain the probability mentioned in Item 4

$$
\begin{gathered}
\left(1-e^{-\left(1-\frac{1}{M} \rho N \delta^{2} / 2 e\right.}\right)^{\tilde{t}_{i}-\tilde{t}_{i-1}} \\
=\left(1-e^{-e^{-1 / \omega_{i} \omega}\left(n^{2 \omega} \log n\right)^{2} / 2 e}\right)^{\tilde{t}_{i}-\tilde{t}_{i-1}}
\end{gathered}
$$

Now combining the probabilities mentioned in Items 1, 2, 3 and 4 together, we can obtain that $t_{i}$ is upper bounded by $\tilde{t}_{i}$ at least with the probability of

$$
\begin{aligned}
& \left(1-n^{-e^{-1 / \omega_{i} \omega}\left(n^{2 \omega} \delta^{2} / 2 e\right.}\right)^{2 \tilde{t}_{i}} \\
& \cdot \prod_{k=0}^{i-1}\left(1-n^{-\left(1-\left(\frac{1}{e}\right)^{1+\frac{n}{2}}\right)^{2} \omega(1)}\right)^{2 \tilde{t}_{k}}
\end{aligned}
$$

As a result, $t_{n-1}$ is bounded by $\tilde{t}_{n-1}$ with the overwhelming probability of

$$
\left(1-n^{-e^{-1 / \omega_{i} \omega}\left(n^{2 \omega} \delta^{2} / 2 e\right.}\right)^{2 \tilde{t}_{n-1}} \cdot \prod_{k=0}^{n-2}\left(1-n^{-\left(1-\left(\frac{1}{e}\right)^{1+\frac{n}{2}}\right)^{2} \omega(1)}\right)^{2 \tilde{t}_{k}}
$$

When all the marginal probabilities $p_{-j}\left(x_{i}^{*}\right)(i \neq n)$ have reached $1-\frac{1}{M}$, the marginal probability $p_{-n}\left(\tilde{x}_{n}^{*}\right)$ will become smaller and smaller and the probability of finding the optimum becomes larger and larger.

Now we consider the $(n+1)$ th stage, in which two events hold: 1) $\tilde{p}_{l_{n-1}, n}\left(x_{n}^{*}\right) \geq \frac{1}{M}$ holds; 2) $\forall t>\tilde{t}_{n-1}, t<\operatorname{Poly}(n), \forall j \leq$ $n-1: p_{t, j}\left(x_{j}^{*}\right)=1-\frac{1}{M}$ holds with an overwhelming probability (38). Thus, there is no genetic drift to be taken into account. Meanwhile, the probability of generating the optimum in one sampling of a generation, conditional on the above two events, is at least $\left(1-\frac{1}{M}\right)^{n-1} \frac{1}{M}=e^{-(n-1) / n e(n)} \frac{1}{M}$, which implies that if the above two events both happen (which is true in the $(n+1)$ th stage), then the optimum will be found within $M \ln ^{2} n$ extra samplings (which generates $M \ln ^{2} n$ new individuals) with the overwhelming probability $1-\left(\frac{1}{e}\right)^{\omega(\ln n)}$. Consequently, after the first $n$ stages, at most $\frac{M}{N} \ln ^{2} n$ generations can guarantee the emergence of the optimum with an overwhelming probability.

TABLE X
BOUNDING $p_{i, i}\left(x_{i}^{*}\right)$ From Below With an OVERwHELming Probability

$$
\begin{aligned}
& \mathbb{P}\left(p_{i, i}\left(x_{i}^{*}\right) \geq \min \left\{(1-\delta) \frac{N}{M} p_{i-1, i}\left(x_{i}^{*}\right) p_{i-1, n}\left(X_{n}^{*}\right) \prod_{j=1}^{i-1} p_{i-1, j}\left(x_{j}^{*}\right), 1-\frac{1}{M}\right\}\right. \\
& \left.\mid p_{i-1, i}\left(x_{i}^{*}\right), p_{i, n}\left(X_{n}^{*}\right)=1-\frac{1}{M}, \forall j \leq i-1: p_{i-1, j}\left(x_{j}^{*}\right)=1-\frac{1}{M}\right) \\
& >\mathbb{P}\left(p_{i, i}\left(x_{i}^{*}\right) \geq \min \left\{(1-\delta) \frac{N}{M}\left(1-\frac{1}{M} p_{i-1, i}\left(x_{i}^{*}\right), 1-\frac{1}{M}\right\} \mid p_{i-1, i}\left(x_{i}^{*}\right)\right)\right. \\
& >1-e^{-\left(1-\frac{1}{M} p_{i-1, i}\left(x_{i}^{*}\right) N \delta^{2} / 2\right.}
\end{aligned}
$$

TABLE XI
Calculation of Probability That $T_{n}^{\prime}$ Is Upper Bounded by $\bar{T}_{n}^{\prime}$

$$
\begin{aligned}
& \mathbb{P}\left(T_{n}^{\prime} \leq \bar{T}_{n}^{\prime} \mid p_{0, n}\left(X_{n}^{*}\right)=\bar{p}_{0, n}\left(X_{n}^{*}\right)\right) \\
& >\mathbb{P}\left(p_{T_{n}^{\prime}-1,1}(1) \geq \frac{M}{N(1-\delta)} \mid p_{0, n}\left(X_{n}^{*}\right)=\bar{p}_{0, n}\left(X_{n}^{*}\right)\right)\left(1-e^{-\frac{\bar{p}_{0,1}(1) N}{2} \delta^{2}}\right) \\
& >\mathbb{P}\left(p_{T_{n}^{\prime}-1,1}(1) \geq \bar{p}_{T_{n}^{\prime}-1,1}(1)=G^{\bar{T}_{n}^{\prime}-1} p_{0, n}\left(X_{n}^{*}\right)>\frac{M}{N(1-\delta)} \mid p_{0, n}\left(X_{n}^{*}\right)=\bar{p}_{0, n}\left(X_{n}^{*}\right)\right)\left(1-e^{-\frac{\bar{p}_{0,1}(1) N}{2} \delta^{2}}\right) \\
& >\mathbb{P}\left(p_{T_{n}^{\prime}-1,1}(1) \geq \bar{p}_{T_{n}^{\prime}-1, n}\left(X_{n}^{*}\right) \mid p_{0, n}\left(X_{n}^{*}\right)=\bar{p}_{0, n}\left(X_{n}^{*}\right), \bar{p}_{T_{n}^{\prime}-1, n}\left(X_{n}^{*}\right)>\frac{M}{N(1-\delta)}\right) \\
& \quad \mathbb{P}\left(p_{T_{n}^{\prime}-1, n}\left(X_{n}^{*}\right)>\frac{M}{N(1-\delta)} \mid p_{0, n}\left(X_{n}^{*}\right)=\bar{p}_{0, n}\left(X_{n}^{*}\right)\right)\left(1-e^{-p_{0, n}\left(X_{n}^{*}\right) N \delta^{2} / 2}\right)
\end{aligned}
$$

Hence, the first hitting time $\tau$ is upper bounded by a deterministic value $\bar{\tau}$

$$
\begin{aligned}
\tau<\bar{\tau}=\frac{\left(\ln \frac{\epsilon(M-1)}{N}-\ln (1-\delta)\right) n \epsilon(n)+n}{\epsilon(n) \ln (1-\delta)+\epsilon(n) \ln \left(\frac{N}{M}\right)-1} \\
+\frac{M}{N} \ln ^{2} n+2 n
\end{aligned}
$$

with the overwhelming probability at least

$$
\begin{aligned}
& \left(1-n^{-e^{-(1 / n)(\epsilon)(\ln (n)^{2} \omega)} \delta^{2} / 2 \epsilon}\right)^{2 \bar{\tau}} \\
& \quad\left(1-n^{-\left(1-\left(\frac{1}{n}\right)^{1+\frac{1}{n}}\right)^{2} \omega(1)}\right)^{2(n-1) \bar{\tau}} \\
& \quad\left(1-\left(\frac{1}{e}\right)^{u(\ln u)}\right)
\end{aligned}
$$

The results in this section show that margins can avoid misleading convergence and leave some chances to the UMDA $_{M}$ to find the global optimum. However, UMDA $_{M}$ cannot converge to the global optimum completely anymore, i.e., the CT becomes infinite. This is an interesting case where the FHT is bounded polynomially in the problem size, but the CT is infinite, and it demonstrates that FHT is a more appropriate measure for EDAs time complexity than CT. It is noteworthy that the idea of margins is quite similar to the Laplace correction [2], which was also proposed to prevent the marginal probabilities from premature convergence. However, since our
purpose here is to demonstrate the influence of forbidding a marginal probability to be 0 or 1 , the slight difference between relaxation and Laplace correction is not investigated.

## VII. CONCLUSION

In this paper, we utilized the FHT to measure the time complexity of EDAs. Based on the FHT measure, we proposed a classification of problem hardness for EDAs and the corresponding probability conditions. This is the first time the general issues related to the time complexity of EDAs were discussed theoretically. After that, a new approach to analyzing the FHT for EDAs with finite population was introduced. Using this approach, we investigated the time complexity of UMDAs as examples.

In this paper, UMDAs were analyzed in depth on two problems: LEADINGONES [37] and BVLEADINGONES. Both of the problems are unimodal. The latter was derived from the former, and inherited the domino convergence property of the former. For the original UMDA, LEADINGONES is shown to be EDA-easy, and BVLEADINGONES is shown to be EDAhard. Comparing the theoretical results of EDAs with those of the EAs', although the first result is similar to EAs', i.e., LEADINGONES is easy, it should be noted that the general case does not hold. That is, a problem that is easy for the EAs could be hard for EDAs, e.g., the BVLEADINGONES problem. However, it is still an open issue to analyze problems that are hard for the EAs but easy for the EDAs.

If the UMDA is further relaxed by margins, BVLEADINGONES will no longer be EDA-hard. Our analysis shows that the margin is helpful for UMDA to avoid wrong convergence and thus significantly increases the performance of UMDA on BVLEADINGONES. This is the first rigorous time complexity evidence that supports the efficacy of relaxations (corrections) of EDAs.

Finally, although we only analyze UMDAs, our approach has the potential for analyzing other EDAs with the finite populations. The general idea is to find a way to simplify the EDAs and then estimate the probability that this simplification holds. However, since different EDAs may have different characteristics, more work needs to be done for the generalization of our approach.

## APPENDIX

Proof of Lemma 6. According to Chernoff bounds, we have

$$
\begin{aligned}
& \mathbb{P}\left(p_{t, n}\left(\bar{x}_{n}^{*}\right) \geq(1-\delta) \frac{p_{t-1, n}\left(\bar{x}_{n}^{*}\right) N}{M}\right. \\
& \left.\quad \mid p_{t-1, n}\left(\bar{x}_{n}^{*}\right) \leq \frac{M}{N(1-\delta)}\right) \\
& >1-e^{-p_{t-1, n}\left(\bar{x}_{n}^{*}\right) N \delta^{2} / 2}, \forall t \leq U
\end{aligned}
$$

where $\delta \in\left(\max \left\{0,1-\frac{2 M}{N}\right\}, 1-\frac{M}{N}\right)$ is a positive constant. Since no global optimum is generated before the $U$ th generation, we have

$$
\bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)=G^{t} p_{0, n}\left(\bar{x}_{n}^{*}\right), \forall t \leq U
$$

where $G=(1-\delta) \frac{N}{M}$, and $\bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)$ is deterministic given the initial value $p_{0, n}\left(\bar{x}_{n}^{*}\right)=\bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)=\frac{1}{2}$. Furthermore, setting $t=$ $U$ in the above equation, by calculation we obtain that

$$
\bar{p}_{U, n}\left(\bar{x}_{n}^{*}\right)=1
$$

Let $\bar{T}_{n}^{o}$ denote the minimal $t$ for $\bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)$ to reach 1 , then the above equation implies $\bar{T}_{n}^{o} \leq U$. We study the probability that the random variable $p_{t, n}\left(\bar{x}_{n}^{*}\right)$ is larger than $\bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right)$. Similar to Table III, $\forall t \leq \bar{T}_{n}^{o}$ we obtain

$$
\begin{aligned}
\mathbb{P}\left(p_{t, n}\left(\bar{x}_{n}^{*}\right)\right. & \left.\geq \bar{p}_{t, n}\left(\bar{x}_{n}^{*}\right) \mid p_{0, n}\left(\bar{x}_{n}^{*}\right)=\bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)\right) \\
& >\left(1-e^{-p_{0, n}\left(\bar{x}_{n}^{*}\right) N \delta^{2} / 2}\right)^{t}
\end{aligned}
$$

By inequalities in Table XI, we estimate the probability that $T_{n}^{o}$ is bounded by $\bar{T}_{n}^{o}$, where in (42) the factor $\left(1-e^{-p_{0, n}\left(\bar{x}_{n}^{*}\right) N \delta^{2} / 2}\right)$ is added since we apply Chernoff bounds at the end of the $\left(\bar{T}_{n}^{o}-1\right)$ th generation. We then consider the following item:

$$
\begin{aligned}
\mathbb{P}\left(\bar{p}_{T_{n}^{*}-1, n}\left(\bar{x}_{n}^{*}\right)>\frac{M}{N(1-\delta)} \mid p_{0, n}\left(\bar{x}_{n}^{*}\right)=\bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)\right) \\
=\mathbb{P}\left(\bar{p}_{T_{n}^{*}-1, n}\left(\bar{x}_{n}^{*}\right)>\frac{M}{N(1-\delta)}\right)
\end{aligned}
$$

According to the definition of $\bar{T}_{n}^{o}$, and noting that $\bar{p}_{T_{n}^{*}-1, n}\left(\bar{x}_{n}^{*}\right)>\frac{M}{N(1-\delta)}$ is deterministic, we know the probability
above is 1 . Thus, we continue to estimate the corresponding probability mentioned in (41)

$$
\begin{aligned}
& \mathbb{P}\left(T_{n}^{o} \leq \bar{T}_{n}^{o} \mid p_{0, n}\left(\bar{x}_{n}^{*}\right)=\bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)\right) \\
> & \mathbb{P}\left(p_{T_{n}^{*}-1, n}\left(\bar{x}_{n}^{*}\right) \geq \bar{p}_{T_{n}^{*}-1, n}\left(\bar{x}_{n}^{*}\right)\right. \\
& \left.\mid p_{0, n}\left(\bar{x}_{n}^{*}\right)=\bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)\right)\left(1-e^{-\frac{\bar{p}_{0, n}(1) N}{2} \delta^{2}}\right) \\
& >\left(1-e^{-\frac{\bar{p}_{0, n}(1) N}{2} \delta^{2}}\right)^{T_{n}^{o}}
\end{aligned}
$$

Since $\bar{T}_{n}^{o} \leq U$, we further get

$$
\begin{aligned}
& \mathbb{P}\left(T_{n}^{o} \leq U \mid p_{0, n}\left(\bar{x}_{n}^{*}\right)=\bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)\right) \\
& >\mathbb{P}\left(T_{n}^{o} \leq \bar{T}_{n}^{o} \mid p_{0, n}\left(\bar{x}_{n}^{*}\right)=\bar{p}_{0, n}\left(\bar{x}_{n}^{*}\right)\right) \\
& >\left(1-e^{-\frac{\bar{p}_{0, n}(1) N}{2} \delta^{2}}\right)^{U}
\end{aligned}
$$

The analysis above tells us, the probability that the marginal probability converges before the $U$ th generation $\left(T_{n}<U\right)$ is at least $\left(1-e^{-\frac{N}{2} \delta^{2}}\right)^{U}$. Since $N=o\left(n^{2+u} \log n\right), M=\beta N(\beta \in$ $(0,1)$ is a constant) and $U$ is polynomial in the problem size $n$, this probability is overwhelming. Hence, we have proven the lemma.

## ACKNOWLEDGMENT

The authors are grateful to Prof. J. A. Lozano for his constructive comments. T. Chen would like to thank Dr. J. He for his kind helps and suggestions over the years.
