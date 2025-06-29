# Choosing the right algorithm with hints from complexity theory 

Shouda Wang ${ }^{\mathrm{a}}$, Weijie Zheng ${ }^{\mathrm{b}, *}$, Benjamin Doerr ${ }^{\mathrm{a}, *}$<br>${ }^{a}$ Laboratoire d'Informatique (LIK), École Polytechnique, CNRS, Institut Polytechnique de Paris, Palaiseau, Paris, France<br>${ }^{\mathrm{b}}$ School of Computer Science and Technology, International Research Institute for Artificial Intelligence,<br>Harbin Institute of Technology, Shenzhen, Shenzhen, China

## A R T I C L E I N F O

Article history:
Received 23 September 2022
Received in revised form 12 June 2023
Accepted 21 November 2023
Available online 24 November 2023

Keywords:
Runtime analysis
Complexity theory
Metropolis algorithm
Estimation-of-distribution algorithm
Black-box optimization

## A B S T R A C T

Choosing a suitable algorithm from the myriads of different search heuristics is difficult when faced with a novel optimization problem. In this work, we argue that the purely academic question of what could be the best possible algorithm in a certain broad class of black-box optimizers can give fruitful indications in which direction to search for good established heuristics. We demonstrate this approach on the recently proposed DLB benchmark. Our finding that the unary unbiased black-box complexity is only $O\left(n^{2}\right)$ suggests the Metropolis algorithm as an interesting candidate and we prove that it solves the DLB problem in quadratic time. We also prove that better runtimes cannot be obtained in the class of unary unbiased algorithms. We therefore shift our attention to algorithms that use the information of more parents to generate new solutions and find that the significance-based compact genetic algorithm can solve the DLB problem in time $O(n \log n)$.
(c) 2023 The Author(s). Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

## 1. Introduction

Randomized search heuristics such as stochastic hillclimbers, evolutionary algorithms, ant colony optimizers, or estimation-of-distribution algorithms (EDAs) have been very successful at solving optimization problems for which no established problem-specific algorithm exists. As such, they are applied massively to novel problems for which some understanding of the problem and the desired solution exists, but little algorithmic expertise.

When faced with a novel optimization problem, one has the choice between a large number of established heuristics (and an even larger number of recent metaphor-based heuristics [2]). Which of them to use is a difficult question. Since implementing a heuristic and adjusting it to the problem to be solved can be very time-consuming, ideally one does not want to experiment with too many different heuristics. For that reason, a theory-guided prior suggestion could be very helpful. This is what we aim at in this work. We note that the theory of randomized search heuristics has helped to understand these algorithms, has given suggestions for parameter settings, and has even proposed new operators and algorithms (see the textbooks [3-7] or the tutorial [8]), but we are not aware of direct attempts to aid the initial choice of the basic algorithm to be used (as with experimental work, there always is the indirect approach to study the existing results and try

[^0]
[^0]:    * Extended version of a paper in the proceedings of IJCAI 2021 [1]. This version, besides more details, contains all mathematical proofs.
    * Corresponding authors.

    E-mail addresses: zhengwj13@tisnghua.org.cn, zhengweijie@hit.edu.cn (W. Zheng).

to distill from them some general rule which algorithms perform well on which problems, but in particular for the theory domain it is not clear how effective this approach is at the moment).

What we propose in this work is a heuristic approach building on the notion of black-box complexity, first introduced by Droste, Jansen, Tinnefeld, and Wegener [9] (journal version [10]). In very simple words, the (unrestricted) black-box complexity of an optimization problem is the performance of the best black-box optimizer for this problem. It is thus a notion not referring to a particular class of search heuristics such as genetic algorithms or EDAs. Black-box complexity has been used successfully to obtain universal lower bounds. Knowing that the black-box complexity of the Needle problem is exponential [10], we immediately know that no genetic algorithm, ant colony optimizer, or EDA can solve the Needle problem in subexponential time. With specialized notions of black-box complexity, more specific lower bounds can be obtained. The result that the unary unbiased black-box complexity of the OneMax benchmark is at least of the order $n \log n$ [11] implies that many standard mutation-based evolutionary algorithms cannot optimize OneMax faster than this bound.

With a more positive perspective, black-box complexity has been used to invent new algorithms. Noting that the unary unbiased black-box complexity of OneMax is $\Omega(n \log n)$, but the two-ary (i.e., allowing variation operators taking two parents as input) unbiased black-box complexity is only $O(n)$ [12], a novel crossover-based evolutionary algorithm was developed in [13]. Building on the result that the unary unbiased $\lambda$-parallel black-box complexity of the OneMax problem is only $O\left(\frac{n \lambda}{\log \lambda}+n \log n\right)$ [14,15], dynamic, self-adjusting, and self-adapting EAs obtaining this runtime have been constructed [14, 16,17].

In this work, we also aim at profiting from the guidance of black-box results, however not by designing new algorithms, but by giving an indication which of the existing algorithms could be useful for a particular problem. Compared to the approach taken in [13], we can thus profit from the numerous established and well-understood algorithms and avoid the risky and time-consuming road of developing a new algorithm.

In simple words, what we propose is trying to find out which classes of black-box algorithms contain fast algorithms for the problem at hand. These algorithms may well be artificial as we use them only to determine the direction in which to search for a good established algorithm for our problem. Only once we are sufficiently optimistic that a certain property of black-box algorithms is helpful for our problem, we regard the established heuristics in this class and see if one of them indeed has a good performance.

To show that this abstract heuristic approach towards selecting a good algorithm can indeed be successful, we regard the DeceivingLeadingBlocks (DLB) problem recently proposed by Lehre and Nguyen [18]. Lehre and Nguyen conducted rigorous runtime analyses of several classic evolutionary algorithms, all leading to runtime guarantees of order $O\left(n^{3}\right)$ with optimal parameter choices. For the EDA univariate marginal distribution algorithm (UMDA), a runtime guarantee of $O\left(n^{2} \log n\right)$ was proven in [19]. No other proven upper bounds on runtimes of randomized search heuristics on the DLB problem existed prior to this work. With only these results from only two prior works, it is safe to call the DLB problem relatively novel and thus an interesting object for our investigation.

Finding more efficient randomized search heuristics: We note that the classic algorithms regarded in [18] are all elitist evolutionary algorithms or non-elitist algorithms with parameter settings that let them imitate an elitist behavior. This choice was natural given the weaker understanding of non-elitist algorithms and the fact that not many theoretical works could show a convincing advantage of non-elitist algorithms (see Section 3.4.2). To obtain a first indication whether it is worth investigating non-elitist algorithms for this problem, we show two results. (i) We prove that the $(1+1)$ elitist unbiased black-box complexity of the DLB problem is $\Omega\left(n^{3}\right)$. (ii) We show that there is a simple, artificial, $(1+1)$-type non-elitist unbiased black-box algorithm solving the DLB problem in quadratic time. These two findings motivate us to analyze the existing $(1+1)$-type non-elitist heuristics. Among them, we find that the Metropolis algorithm [20] with a suitable temperature also optimizes DLB in time $O\left(n^{2}\right)$. We note that there are very few runtime analyses on the Metropolis algorithm (see Section 3.4.1), so it is clear that a synopsis of the existing runtime analysis literature would not have easily suggested this algorithm.

To direct our search for possible further runtime improvements, we first show that the unary unbiased black-box complexity of DLB is at least quadratic. Consequently, if we want to stay in the realm of unbiased algorithms (which we do) and improve beyond quadratic runtimes, then we necessarily have to regard algorithms that are not unary, that is, that generate offspring using the information from at least two parents. That this is possible, at least in principle, follows from our next result, which is an artificial crossover-based algorithm that solves DLB in time $O(n \log n)$. While, together with the previously shown lower bound, it is clear that this performance relies on the fact that offspring are generated from the information of more than one parent, the working principles of this algorithm also include a learning aspect. The algorithm optimizes the blocks of the DLB problem in a left-to-right fashion, but once a block is optimized, it is never touched again. Such learning mechanisms are rarely found in standard evolutionary algorithms, but are the heart of EDAs with their main goal of learning a distribution that allows sampling good solutions. Note that the distribution in an EDA carries information from many previously generated solutions, hence EDAs necessarily generate new solutions based on the information of many parents. For these reasons, we focus on EDAs. We do not find a classic EDA for which we can prove that it solves the DLB problem in subquadratic time, but we succeed for the significance-based EDA [21] and we show that it optimizes the DLB problem in a runtime of $O(n \log n)$ with high probability.

Overall, these results demonstrate that our heuristic theory-guided approach towards selecting good algorithms for a novel problem can indeed be helpful. We note in particular that the previous works on the DLB problem have not detected

that the Metropolis algorithm is an interesting candidate for solving this problem. Our experimental analysis confirms a very good performance of the Metropolis algorithm, but suggests that the runtimes of the EDAs suffer from large constants hidden by the asymptotic analysis.

To avoid a possible misunderstanding, let us stress that our target is to find an established search heuristic for our optimization problem. From the above discourse one could believe that we should simply stick to the artificial black-box algorithm that we found. If our only aim was solving the DLB problem, this would indeed be feasible. Such an algorithm, however, would most likely lack the known positive properties of established search heuristics such as robustness to noise and dynamic changes of the problem data, reusability for similar problems, and adjustability to restricted instance classes. For that reason, our target in this work is definitely to find an established heuristic and not an particular algorithm customtailored to a problem.

We note that the results and methods used in this works lie purely in the theory domain. We therefore followed the traditional approach [22] of regarding benchmark problems simple enough that they can be rigorously analyzed with mathematical means. In return, we obtain proven results for infinite numbers of problem instances (here, the DLB problem for all problem dimensions $n \in 2 \mathbb{N}$ ), which hopefully extend in spirit also to problems which are too complicated to be analyzed with mathematical means.

We believe that our approach, in principle and in a less rigorous way, can also be followed by researchers and practitioners outside the theory community. Our basic approach of (i) trying to find a very good algorithm, chosen from all possible black-box optimization algorithms, to solve a given problem or to overcome a particular difficulty and then (ii) using this artificial and problem-specific algorithm as indicator for which established search heuristics could be promising, can also be followed by experimental methods and by non-rigorous intuitive considerations.

The remainder of the paper is organized as follows. Section 2 discusses black-box optimization, black-box complexity, the DLB problem, and two probabilistic tools to be used later. Sections 3 and 4 demonstrate our approach on the DLB problem. We first observe that non-elitist $(1 \star 1)$ type algorithms in principle can improve the $O\left(n^{3}\right)$ runtime of known elitist algorithms to a quadratic runtime and find the Metropolis algorithm as an established heuristic showing this performance. By going beyond unary unbiased algorithms, we then obtain a further improvement to a complexity of $O(n \log n)$, first via an artificial algorithm and then via the significance-based compact genetic algorithm. Our experimental discussion is shown in Section 5, and Section 6 concludes this paper.

# 2. Preliminaries 

Following the standard notation, we write $[\ell . . m]:=[\ell, \ell+1, \ldots, m]$ for all $\ell, m \in \mathbb{N}$ such that $\ell \leq m$. In this paper we consider pseudo-Boolean optimization problems, that is, problems of maximizing functions $f$ defined on the search space $(0,1)^{n}$, where $n$ is a positive integer. A bit string (also called a search point) is an element of the set $[0,1]^{n}$ and is represented as $x=\left(x_{1}, \ldots, x_{n}\right)$. For any set $S=\left\{s_{1}, \ldots, s_{|S|}\right\} \subseteq\{1 . . n\}$ with $s_{i}<s_{j}$ for $i<j$, we write $x_{S}:=\left(x_{s_{1}}, \ldots, x_{s_{|S|}}\right)$. In the context of evolutionary algorithms, we sometimes refer to a bit string as an individual and we use $x^{(t)}$ to denote an individual at time $t$, in which case $x_{i}^{(t)}$ is used to represent the $i$-th component of the individual $x^{(t)}$. To simplify the notation, whenever we write $m$ where an integer is required, we implicitly mean $\lceil\mathrm{m}\rceil:=\min \{k \in \mathbb{N} \mid k \geq m\}$.

### 2.1. Black-box optimization and runtime

In (discrete) black-box optimization, we assume that the optimization algorithms do not have access to an explicit description of the instance of the problem to be solved. Instead, their only access to the instance is via a black-box evaluation of search points. Classic black-box optimization algorithms include hill-climbers, the Metropolis algorithm, simulated annealing, evolutionary algorithms, and other bio-inspired search heuristics.

A general scheme for a black-box algorithm $A$ is given in Algorithm 1. It starts by generating a random search point according to a given probability distribution and evaluating it. It then repeats generating (and evaluating) new search points based on all information collected so far, that is, based on all previous search points together with their fitnesses. While in practice, naturally, this iterative procedure is stopped at some time, in theoretical investigations it is usually assumed that this loop is continued forever. In this case, the runtime, also called optimization time, $T:=T_{A}(f)$ of the algorithm $A$ on the problem instance $f:\{0,1\}^{n} \rightarrow \mathbb{R}$ is the number of search points evaluated until (and including) for the first time an optimal solution of $f$ is generated (and evaluated). In the notation of Algorithm 1, we have $T_{A}(f)=1+\inf \left\{t \mid x^{(t)} \in \arg \max f\right\}$. If the algorithm $A$ is randomized (which most black-box optimizers are), then the runtime $T$ is a random variable and often only its expectation $E[T]$ is analyzed. For an optimization problem, that is, a set $\mathcal{F}$ of problem instances $f$, the worst-case expected optimization time $\sup _{f \in \mathcal{F}} E\left[T_{A}(f)\right]$ is an often regarded quality measure of the algorithm $A$.

Most black-box algorithms for practical reasons do not exploit this scheme to its full generality, that is, they do not store all information collected during the process or they do not sequentially generate one search point after the other based on all previous information, but instead generate in parallel several search points based on the same set of information. For our analyses, we nevertheless assume that the search points are generated in some specified order and that each search point is evaluated immediately after being generated.

```
Algorithm 1: Template of a black-box algorithm for optimizing an unknown function \(f:\{0,1\}^{\mathrm{n}} \rightarrow \mathbb{R}\). Without ex-
plicit mention, we assume that each search point \(x^{(t)}\) is evaluated immediately after being generated. As runtime of
such an (infinitely running) algorithm we declare the number of search points evaluated until an optimum of \(f\) is
    evaluated for the first time.
    Generate a search point \(x^{(0)}\) according to a given distribution \(\mathcal{D}^{(0)}\) on \(\{0,1\}^{\mathrm{n}}\);
    for \(t=1,2,3, \ldots\) do
    Depending on \(f\left(x^{(0)}\right), \ldots, f\left(x^{(t-1)}\right)\) and \(x^{(0)}, \ldots, x^{(t-1)\), choose a probability distribution \(\mathcal{D}^{(t)}\) on \(\left\{0,1\right\}^{\mathrm{n}} ;\)
    Sample \(x^{(t)}\) from \(\mathcal{D}^{(t)} ;\)
```


# 2.2. Unbiasedness 

Unless a specific understanding of the problem at hand suggests a different approach, it is natural to look for optimization algorithms that are invariant under the symmetries of the search space. This appears so natural that, in fact, most algorithms have this property without that this has been discussed in detail.

The first to explicitly discuss such invariance properties for the search space $\{0,1\}^{\mathrm{n}}$ of bit strings (see, e.g., [23] for such a discussion for continuous search spaces) were Lehre and Witt in their seminal paper [11]. They coined the name unbiased for algorithms respecting the symmetries of the hypercube $\{0,1\}^{\mathrm{n}}$. Such algorithms treat the bit positions $i \in[1 . . n]$ in a symmetric fashion and, for each bit position, do not treat the value 0 differently from the value 1 . It follows that all decisions of such algorithms may not depend on the particular bit string representation of the search points they have generated before. Rather, all decisions can only depend on the fitnesses of the search points generated. This implies that all search points the algorithm has access to can only be generated from previous ones via unbiased variation operators. This observation also allows to rigorously define the arity of an algorithm as the maximum number of parents used to generate offspring. Hence mutation-based algorithms have an arity of one and crossover-based algorithms have an arity of two. We note that sampling a random search point is an unbiased operator with arity zero.

Since these are important notions that also help to classify different kinds of black-box algorithms, let us make them precise in the following.

Definition 1. A $k$-ary variation operator $V$ is a function that assigns to each $k$-tuple of bit strings in $\{0,1\}^{\mathrm{n}}$ a probability distribution on $\{0,1\}^{\mathrm{n}}$. It is called unbiased if

- 

$$
\begin{aligned}
& \forall x^{1}, \ldots, x^{k} \in\{0,1\}^{\mathrm{n}}, \forall y, z \in\{0,1\}^{\mathrm{n}}, \\
& \quad \operatorname{Pr}\left[y=V\left(x^{1}, \ldots, x^{k}\right)\right]=\operatorname{Pr}\left[y \oplus z=V\left(x^{1} \oplus z, \ldots, x^{k} \oplus z\right)\right], \\
& \forall x^{1}, \ldots, x^{k} \in\{0,1\}^{\mathrm{n}}, \forall y \in\{0,1\}^{\mathrm{n}}, \forall \sigma \in \mathcal{S}_{\mathrm{n}}, \\
& \quad \operatorname{Pr}\left[y=V\left(x^{1}, \ldots, x^{k}\right)\right]=\operatorname{Pr}\left[\sigma(y)=V\left(\sigma\left(x^{1}\right), \ldots, \sigma\left(x^{k}\right)\right)\right],
\end{aligned}
$$

where $\oplus$ represents the exclusive-or operator and $\mathcal{S}_{\mathrm{n}}$ represents the symmetric group on $n$ letters and we write $\sigma(x)=\left(x_{\sigma(1)}, \ldots\right.$, $\left.x_{\sigma(n)}\right)$ for all $\sigma \in \mathcal{S}_{\mathrm{n}}$ and $x \in\{0,1\}^{\mathrm{n}}$.

By definition, a $k$-ary operator can simulate $\ell$-ary operators if $\ell \leq k$. It is also immediate that the only 0 -ary operator is the operator that generates a search point in $\{0,1\}^{\mathrm{n}}$ uniformly at random. As a special case, 1 -ary unbiased variation operators are more often called unary unbiased variation operators and sometimes referred to as mutation operators in the context of evolutionary computation.

Unary unbiased variation operators admit a simple characterization, namely that sampling from the unary unbiased operator is equivalent to sampling a number $r \in[0 . . n]$ from some distribution and then flipping exactly $r$ bits chosen uniformly at random. This is made precise in the following lemma, which was proven in [24, Lemma 1], but which can, in a more general form, already be found in [25].

Lemma 2. Let $D$ be a probability distribution on $[0 . . n]$. Let $V_{D}$ be the unary variation operator which for each $x \in\{0,1\}^{\mathrm{n}}$ generates $V_{D}(x)$ by first sampling a number $r$ from $D$ and then flipping $r$ random bits in $x$. Then $V_{D}$ is a unary unbiased variation operator.

Conversely, let $V$ be a unary unbiased variation operator on $\{0,1\}^{\mathrm{n}}$. Then there is a probability distribution $D_{V}$ on $[0 . . n]$ such that $V=V_{D_{V}}$.

Building on the notion of a $k$-ary unbiased variation operator, we can now define what is a $k$-ary unbiased black-box algorithm (Algorithm 2). For the reasons given at the beginning of this section, in this work we shall only be interested in unbiased algorithms (possibly with unrestricted arity).

```
Algorithm 2: Template of a \(k\)-ary unbiased black-box algorithm for optimizing an unknown function \(f:\{0,1\}^{\mathrm{n}} \rightarrow \mathbb{R}\).
1 Generate \(x^{(0)}\) uniformly at random;
2 for \(t=1,2,3, \ldots\) do
    3 \(\quad\) Based solely on \(f\left(x^{(0)}\right), \ldots, f\left(x^{(t-1)}\right)\), choose a \(k\)-ary unbiased variation operator \(V\) and \(i_{1}, \ldots, i_{k} \in\{0 . . t-1\}\);
4 \(\quad\) Sample \(x^{(t)}\) from \(V\left(x^{(i_{1} 1)}, \ldots, x^{(i_{k} 1)}\right)\);
```


# 2.3. Black-box complexity 

To understand the difficulty of a problem for black-box optimization algorithms, inspired by classical complexity theory, Droste, Jansen, and Wegener [10] (preliminary version [9], see also [26] for a recent survey) defined the black-box complexity of a problem $\mathcal{F}$ as the smallest worst-case expected runtime a black-box algorithm $A$ can have on $\mathcal{F}$, that is,

$$
\inf _{A} \sup _{f \in \mathcal{F}} E\left[T_{A}(f)\right]
$$

where $A$ runs over all black-box algorithms in the infimum.
Just by definition, the black-box complexity is a universal lower bound on the performance of any black-box algorithm. The result that black-box complexity of the Needle problem is $2^{n-1}+0.5$ [10, Theorem 1] immediately implies that no hillclimber, evolutionary algorithm, ant colony optimizer, etc. can solve the Needle problem in subexponential expected time.

Conversely, the black-box complexity can also serve as a trigger to search for better black-box algorithms. For example, in [13] the observation that the black-box complexity of the OneMax problem is only $\Theta(n / \log n)[27,10,28]$ (albeit witnessed by a highly artificial algorithm) whereas most classic evolutionary algorithms have a $\Theta(n \log n)$ runtime or worse, was taken as starting point to design a novel evolutionary algorithm solving the OneMax problem in time asymptotically better than $n \log n$. This algorithm, called $(1+(\lambda, \lambda))$ GA, has shown a good performance both in experiments [29-31] and in other mathematical analyses $[31-38]$.

In this work, as discussed in the introduction, we shall also use the black-box complexity as a trigger towards more efficient solutions to black-box optimization problems, however, not by suggesting new algorithms, but by suggesting the general type of algorithm that might be most suited for the problem and thus helping to choose the right algorithm among the many existing black-box algorithms. Compared to triggering the design of new algorithms, this might be the more effective road for people "merely" applying black-box algorithms. In fact, we shall argue that this road, despite the theorybased notion of black-box complexity, is in fact not too difficult to follow also for people without a background in algorithm theory.

### 2.4. The DLB function and known runtimes

We now define the DLB function, which is the main object of our study and was first introduced by Lehre and Nguyen in their recent work [18].

To define the DLB function, the $n$-bit string $x$ is divided, in a left-to-right fashion, into $\frac{n}{2}$ blocks of size of 2 . The function value of $x$ is determined by the longest prefix of 11 blocks and the following block. The blocks with two 1 s in the prefix contribute each a value of 2 to the fitness. The DLB function is deceptive in that the next block contributes a value of 1 when it contains two 0 s , but contributes only 0 when it contains one 1 and one 0 . The optimum is the bit string with all 1 s .

The DLB function is defined on $\{0,1\}^{n}$ only for $n$ even. We therefore assume in the following that $n$ is even whenever this is required.

For all $x \in\{0,1\}^{n}$, we formally define the DLB function in the following way. We consider blocks of the form $\left(x_{2 \ell+1}, x_{2 \ell+2}\right)$. If $x \neq(1, \ldots, 1)$, then let $\left(x_{2 m+1}, x_{2 m+2}\right)$ be the first block that is not a 11 block, that is, $m=\inf \{\ell \mid x_{2 \ell+1} \neq$ 1 or $x_{2 \ell+2} \neq 1\}$. We call such a block a critical block. Then the DLB function is defined via

$$
\operatorname{DLB}(x)= \begin{cases}2 m+1 & \text { if } x_{2 m+1}+x_{2 m+2}=0 \\ 2 m & \text { if } x_{2 m+1}+x_{2 m+2}=1 \\ n & \text { if } x=(1, \ldots, 1)\end{cases}
$$

In other words, the DLB function counts twice the number of consecutive 11 blocks until it reaches a critical block, which counts for 1 if it is of the form 00 and counts for 0 if it is of the form 01 or 10 . Hence the search points $x=$ $(1, \ldots, 1,0,0, x_{2 \ell+1}, \ldots, x_{n})$ with $\ell \in\left[1 \ldots \frac{n}{2}\right]$ and $x_{2 \ell+1}, \ldots, x_{n} \in\{0,1\}$ are the local maxima of the DLB function. The unique global maximum of the DLB function is $x^{k}=(1, \ldots, 1)$.

In a similar fashion we define the Honest Leading Blocks (HLB) function, which will be used as potential function in some proofs using drift analysis. The DLB function being deceptive and unable to discern a 01 critical block from a 10 critical block, the HLB function also treats 01 and 10 critical blocks equally, but is honest with the fact that 01 and 10 critical

blocks are better than a 00 critical block in the sense that such search points are closer to the global maximum $(1, \ldots, 1)$. Formally speaking, the HLB function with parameter $\delta \in(0,2)$ is defined by

$$
\operatorname{HLB}_{\delta}(x):= \begin{cases}2 m & \text { if } \operatorname{DLB}(x)=2 m+1 \\ 2 m+2-\delta & \text { if } \operatorname{DLB}(x)=2 m \\ n & \text { if } \operatorname{DLB}(x)=n\end{cases}
$$

where $m$ is an integer in $\left\{0,1, \ldots, \frac{n}{2}-1\right\}$.
We now review the most relevant known runtime results for this work. Lehre and Nguyen [18] proved that, always assuming that the mutation rate used by the algorithm is $\chi / n$ for a constant $\chi>0$, the expected runtime of the $(1+\lambda)$ EA on the DLB problem is $O\left(n \lambda+n^{3}\right)$ and that the expected runtime of the $(\mu+1)$ EA on the DLB problem is $O\left(\mu n \log n+n^{3}\right)$. They also proved that the expected runtime of the $(\mu, \lambda)$ EA on the DLB function is $O\left(n \lambda \log \lambda+n^{3}\right)$ under the conditions that for an arbitrary constant $\delta>0$ and a constant $c$ sufficiently large, we have $\lambda>c \log n$ and $\mu<\frac{2 \rho^{-2 \delta}}{1+\delta}$. Furthermore, they showed that, with a good choice of the parameters, genetic algorithms using $k$-tournament selection, $(\mu, \lambda)$ selection, linear selection, or exponential ranking selection, also have an $O\left(n \lambda \log \lambda+n^{3}\right)$ expected runtime on the DLB problem.

From looking at the proofs in [18], it appears natural that all algorithms given above have a runtime of at least $\Omega\left(n^{3}\right)$ on the DLB problem, but the only proven such result is that Doerr and Krejca [19] showed that the $(1+1)$ EA with mutation rate $1 / n$ solves the DLB problem in $\Theta\left(n^{3}\right)$ expected fitness evaluations. In Theorem 10, we extend this result to all $(1+1)$ elitist unary unbiased black-box algorithms.

As opposed to these polynomial runtime results, Lehre and Nguyen pointed out in [18] a potential weakness of the Univariate Marginal Distribution Algorithm (UMDA). They proved that the UMDA selecting $\mu$ fittest individuals from $\lambda$ sampled individuals has an expected runtime of $e^{\Omega(\mu)}$ on the DLB problem if $\frac{\mu}{c} \geq \frac{14}{1000}$ and $c \log n \leq \mu=o(n)$ for some sufficiently large constant $c>0$, and has expected runtime $O\left(n \lambda \log \lambda+n^{3}\right)$ if $\lambda \geq(1+\delta) e \mu^{2}$ for any $\delta>0$. However, Doerr and Krejca [19] pointed out that this negative finding can be overcome with a different parameter choice and that with a population size large enough to prevent genetic drift [39,40], the UMDA solves the DLB problem efficiently. To be precise, they proved that the UMDA optimizes the DLB problem within probability at least $1-\frac{n}{n}$ within $\lambda\left(\frac{n}{2}+2 e \ln n\right)$ fitness evaluations if $\mu \geq c_{\mu} n \ln n$ and $\mu / \lambda \leq c_{\lambda}$ for some $c_{\mu}, c_{\lambda}$ sufficiently large or small, respectively.

Since there is an apparent similarity between the DLB function and the classic LeAdingONes benchmark function, we recall the definition of the latter. The LeAdingones function is defined for all $x \in\{0,1\}^{n}$ by $\sum_{r \in[1 . . n]} \prod_{s \in[1 . . r]} x_{s}$. Right from the definitions, we see that the functions DLB and LeAdingONes are very similar, indeed, we have $\mid$ LeAdingONES $(x)-\operatorname{DLB}(x) \mid \leq 1$ for all $x \in[0,1]^{n}$. The main difference is that DLB has non-trivial local optima which could render its optimization harder.

Due to the similarity between the DLB and LeAdingones problems, it will be useful to compare the runtimes on these two problems. The LeAdingones problem was proposed in [41] as an example of a unimodal problem which simple EAs cannot solve in $O(n \log n)$ time. The correct asymptotic runtime of the $(1+1)$ EA of order $\Theta\left(n^{2}\right)$ was determined in [22]. The precise runtime of the $(1+1)$ EA was independently determined in [42,43]. Precise runtimes of various other variants of the $(1+1)$ EA were given in [44]. The runtime of the $(\mu+\lambda)$ EA with $\mu$ at most polynomial in $n$ on LeAdingones is $\Theta\left(\mu n \log n+n^{2}\right)$ [45], the one of the $(1+\lambda)$ EA with $\lambda$ at most polynomial in $n$ is $\Theta\left(\lambda n+n^{2}\right)$. For the $(\mu+\lambda)$ EA, only a lower bound of $\Omega\left(\frac{2 n}{\log (n / n)}\right)$ is known [14,15]. The runtime of the $(1+(\lambda, \lambda))$ GA with standard parameterization $p=\lambda / n$ and $c=1 / \lambda$ is $\Theta\left(n^{2}\right)$ regardless of the value of $\lambda \in[1 . . n / 2]$ and this also with dynamic parameter choices [33]. Consequently, for a large number of elitist algorithms, the runtime is $\Theta\left(n^{2}\right)$ when suitable parameters are used. In [46], Doerr and Lengler have shown that all $(1+1)$-elitist algorithms need $\Omega\left(n^{2}\right)$ fitness evaluations in expectation to solve the LeAdingones problem. This result implies the lower bounds in [22,42-44] when ignoring constant factors.

For non-elitist algorithms, the picture is less clear. Upper bounds have been shown for various algorithms, also some using crossover, when the selection pressure is high enough [47-50], but none of them beats the $\Omega\left(n^{2}\right)$ barrier. When the selection pressure is small, many non-elitist algorithm cannot optimize any function with unique optimum in subexponential time $[51,52]$.

Upper bounds were also shown for the runtime of the estimation-of-distribution algorithms UMDA and PBIL in [53,54] and for the ant-colony optimizers 1-ANT and MMAS in [55,56], but again none could show a runtime better than quadratic in $n$.

A runtime better than quadratic, and in fact of order $O(n \log n)$ was shown for the three non-classical algorithms CSA [57], scGA [58], and sig-cGA [21]. The first two of these, however, are highly inefficient on the OneMax benchmark and thus might be overfitted to the LeAdingones problem.

The unrestricted black-box complexity of the LeAdingones class is $\Theta(n \log \log n)$, as witnessed by a highly problemspecific algorithm in [59].

# 2.5. Probabilistic tools 

We now collect two probabilistic tools used in the remainder of this work. The additive drift theorem is commonly used to derive upper (resp. lower) bounds on the expected runtime of an algorithm from lower (resp. upper) bounds on the expected increase of a suitable potential. It first appeared in the analysis of evolutionary algorithms in He and Yao's work [60,61], in which they implicitly used the optional stopping theorem for martingales. The following version can be found in

Lengler's survey [62]. It was first proven in Lengler and Steger's work [63] via an approach different from the one He and Yao used.

Theorem 3 ([62], Theorem 2.3.1). Let $\left(h_{t}\right)_{t \geq 0}$ be a sequence of non-negative random variables taking values in a finite set $\mathcal{S} \subseteq$ $[0, n]$ such that $n \in \mathcal{S}$. Let $T:=\inf \left\{t \geq 0 \mid h_{t}=n\right\}$ be the first time when $\left(h_{t}\right)_{t \geq 0}$ takes the value $n$. For all $s \in \mathcal{S}$, let $\Delta_{t}(s):=$ $E\left[h_{t+1}-h_{t} \mid h_{t}=s\right]$. Then the following two assertions hold.

- If for some $\delta>0$ we have $\Delta_{t}(s) \geq \delta$ for all $s \in \mathcal{S} \backslash\{n\}$ and all $t$, then $E[T] \leq E\left[n-h_{0}\right] \delta^{-1}$.
- If for some $\delta>0$ we have $\Delta_{t}(s) \leq \delta$ for all $s \in \mathcal{S} \backslash\{n\}$ and all $t$, then $E[T] \geq E\left[n-h_{0}\right] \delta^{-1}$.

Chernoff-Hoeffding inequalities [64,65], often just called Chernoff bounds, are a standard tool in the analysis of random structures and algorithms. In this work we will use the following variance-based additive Chernoff bound (see, e.g., [66, Theorem 1.10.12]).

Theorem 4. (variance-based additive Chernoff inequality) Let $X_{1}, \ldots, X_{n}$ be independent random variables and suppose that for all $i \in[1 . . n]$, we have $\left|X_{i}-E\left[X_{i}\right]\right| \leq 1$. Let $X:=\sum_{i=1}^{n} X_{i}$ and $\sigma^{2}:=\operatorname{Var}[X]=\sum_{i=1}^{n} \operatorname{Var}\left[X_{i}\right]$. Then for all $\lambda \in\left(0, \sigma^{2}\right)$,

$$
\operatorname{Pr}[X \geq E[X]+\lambda] \leq e^{-\frac{\lambda^{2}}{2 \sigma^{2}}} \text { and } \operatorname{Pr}[X \leq E[X]-\lambda] \leq e^{-\frac{\lambda^{2}}{2 \sigma^{2}}}
$$

# 3. From elitist to non-elitist algorithms 

Previous works have shown that the expected runtime of the $(1+1)$ EA on the DLB problem is $\Theta\left(n^{3}\right)$, see [18, Theorem 3.1] for the upper and [19, Theorem 4] for the lower bound (following from the precise computation of the expected runtime there).

In this section, we extend this lower bound and show that any $(1+1)$-elitist unary unbiased black-box algorithm has a runtime of at least $\Omega\left(n^{3}\right)$. This result will motivate us to study non-elitist $(1+1)$-type algorithms, which will lead to the discovery that the Metropolis algorithm can solve the DLB problem significantly faster.

### 3.1. Elitist algorithms suffer from the fitness valleys

### 3.1.1. $(\mu+\lambda)$-elitist black-box complexity

We start by making precise the elitist black-box complexity model we regard. Since it might be useful in the future, we first define our model for general $(\mu+\lambda)$-elitism, even though our main result in this section only considers $(1+1)$-elitist algorithms.

A $(\mu+\lambda)$-elitist algorithm uses a parent population of size $\mu$. In each iteration, it generates from it $\lambda$ offspring and determines the next parent population by choosing $\mu$ best individual from the $\mu+\lambda$ parents and offspring. Hence the term "elitist" refers to the restriction that the next parent population has to consist of $\mu$ best individuals. Ties can be broken arbitrarily, in particular, in case of ties there is no need to prefer offspring.

We shall further only regard algorithms that are unbiased in the sense of Lehre and Witt [11] (see Section 2.2). This in particular means that the algorithm has never access to the bit string representation of individuals (except from using unbiased variation operators and computing the fitness). Consequently, all choices done by the algorithm such as choosing parents for the creation of offspring, choosing variation operators, and selecting the next parent population can only rely on the fitnesses of the individuals created so far. Finally, as variation operators we shall only allow unary (mutation) operators (see Definition 1).

In summary, we obtain the $(\mu+\lambda)$-elitist unary unbiased black-box algorithm class described in Algorithm 3. It is similar to the $(\mu+\lambda)$-elitist model proposed in [67]. Different from [67], we do not require that the algorithm only has access to a ranking of the search points. We note that for an elitist algorithm, adding this restriction or not does not change a lot. The more significant restriction to [67] is that we require the algorithm to be unary unbiased. We do so since we are trying to first explore simple heuristics, and unary unbiased black-box algorithms are among the most simple search heuristics. Nevertheless, to ease the language, we shall in the remainder call our algorithms simply $(\mu+\lambda)$-elitist algorithms, that is, we suppress the explicit mention of the unary unbiasedness.

For a $(\mu+\lambda)$-elitist algorithm $A$, we recall that the runtime $T_{A}(f)$ on the maximization problem $f$ is by definition the number of fitness evaluations performed until a maximum of $f$ is evaluated for the first time. The $(\mu+\lambda)$-elitist black-box complexity of the optimization problem of $f$ is defined to be

$$
\inf _{A} E\left[T_{A}(f)\right]
$$

where $A$ runs through all $(\mu+\lambda)$ unary unbiased black-box algorithms (Algorithm 3).

```
Algorithm 3: Template of a ( \(\mu+\lambda\) )-elitist unary unbiased black-box algorithm, \((\mu+\lambda\) )-elitist algorithm for short,
for optimizing an unknown function \(f:\{0,1\}^{n} \rightarrow \mathbb{R}\).
1 Generate \(\mu\) search points \(x^{(0, i)}, i \in[1 . . \mu]\), independently and uniformly at random;
\(2 X \leftarrow\left\{x^{(0, i)} \mid i \in[1 . . \mu]\right\}\)
3 for \(t=1,2,3, \ldots\) do
    Choose \(\lambda\) individuals \(p_{1}, \ldots, p_{s}\) from \(X\);
    Choose \(\lambda\) unary unbiased operators \(V_{1}, \ldots, V_{s}\);
    Sample \(q_{1}, \ldots, q_{s}\) from \(V_{1}\left(p_{1}\right), \ldots, V_{s}\left(p_{s}\right)\) respectively;
    \(X \leftarrow\) a selection of \(\mu\) best individuals from \(X \cup\left\{q_{1}, \ldots, q_{s}\right\}\)
```


# 3.1.2. Independence of irrelevant bits 

We start our analysis with a simple lemma showing that bit positions that did not have an influence on any fitness evaluation are independently and uniformly distributed. This lemma is similar to [11, Lemma 1].

Lemma 5. Let $f:\{0,1\}^{n} \rightarrow \mathbb{R}, c \in \operatorname{Im} f$, and $I \subset[1 . . n]$. Let $Z=\left\{z \in\{0,1\}^{n} \mid \forall i \notin I: z_{i}=0\right\}$. Assume that for all $y \in\{0,1\}^{n}$ with $f(y) \leq c$, we have $f(y \oplus z)=f(y)$ for all $z \in Z$.

Then for any $(\mu+\lambda)$-elitist algorithm and any $k \in[1 . . \mu]$, conditioning on the event

$$
E_{t, c}:=\left\{\max _{j \in[1 . . \mu]} f\left(x^{(t, j)}\right)=c\right\}
$$

the bits $x_{i}^{(t, k)}, i \in I$, are all independent and uniformly distributed in $\{0,1\}^{\frac{1}{2}}$
Proof. We consider the joint distribution of the random variables

$$
\left(x^{(x, j)}\right)_{x \in[0, t], j \in[1 . . \mu]}
$$

under the condition $E_{t, c}$. By the hypothesis and the mechanisms of $(\mu+\lambda)$-elitist algorithms, $\left(x^{(x, j)}\right)_{x \in[0 . t], j \in[1 . . \mu]}$ and $\left(x^{(x, j)} \oplus z\right)_{x \in[0 . t], j \in[1 . . \mu]}$ are identically distributed for any $z \in Z$.

In particular, for any $k \in[1 . . \mu]$ and any $z \in Z, x^{(t, k)}$ and $x^{(t, k)} \oplus z$ are identically distributed. From this we deduce that for any $x \in\{0,1\}^{n}$,

$$
\operatorname{Pr}\left[x^{(t, k)}=x\right]=2^{-|I|} \operatorname{Pr}\left[x_{[1 . . n] \backslash t}^{(t, k)}=x_{[1 . . n] \backslash I}\right]
$$

Therefore, under the condition $\left\{x_{i}^{(t, k)}=x_{i}, \forall i \in[1 . . n] \backslash I\right\}$ where $x_{i}, i \in[1 . . n] \backslash I$, are prescribed bit values, the bits $x_{i}^{(t, k)}, i \in I$, are all independent and uniformly distributed in $\{0,1\}$, which implies the claim.

We apply the above lemma to the optimization of the DLB function.
Lemma 6. Let $m \in\left[0 . . \frac{n}{2}-1\right]$. For any $(\mu+\lambda)$-elitist algorithm and any $k \in[1 . . \mu]$, conditioning on the event

$$
\left\{\max _{j \in[1 . . \mu]} \operatorname{DLB}\left(x^{(t, j)}\right)=2 m\right\}
$$

or on the event

$$
\left\{\max _{j \in[1 . . \mu]} \operatorname{DLB}\left(x^{(t, j)}\right)=2 m+1\right\}
$$

the bits $x_{i}^{(t, k)}, i=[2 m+3 . . n]$, are all independent and uniformly distributed in $\{0,1\}$.
Proof. It suffices to take $c=2 m$ ( $c=2 m+1$ for the second case) and $I=[2 m+3 . . n]$ in the preceding lemma.

### 3.1.3. Runtime analysis of $(1+1)$ elitist unary unbiased EAs

This section is devoted to proving that the $(1+1)$-elitist black-box complexity of the DLB problem is $\Omega\left(n^{3}\right)$. To this end we use drift analysis and take the HLB function as potential.

We start with an estimate of the influence of the so-called free-riders, that is, we estimate that the expected potential of a random string with $2 m+2$ leading ones is at most $2 m+4$.

[^0]
[^0]:    ${ }^{1}$ We use this language here and in the remainder to express that the bits $x_{i}, i \in I$, are mutually independent, independent of all other bits of $x$, and uniformly distributed in $\{0,1\}$.

Lemma 7. Let $m \in\left[0 \ldots \frac{n}{2}-1\right]$. Let $x$ be a random bit string such that $x_{i}=1$ for all $i \in[1 . .2 m+2]$ and such that the bits $x_{i}, i \in$ $[2 m+3 . . n]$ are independent and uniformly distributed in $\{0,1\}$. Then for any $\delta \in[0,2]$ we have

$$
E\left[\operatorname{HLB}_{\delta}(x)\right] \leq 2 m+4
$$

Proof. The statement clearly holds for $m=\frac{n}{2}-1$ since in this case $x=(1, \ldots, 1)$ and $\operatorname{HLB}_{\delta}((1, \ldots, 1))=n<n+2$. Now we proceed by backwards induction on $m$. Suppose that the conclusion holds for all $m=k+1, \ldots, \frac{n}{2}-1$. For $m=k$ we compute

$$
\begin{aligned}
& E\left[\operatorname{HLB}_{\delta}(x)\right] \\
& \quad=\frac{1}{4}(2 k+2)+\frac{1}{2}(2 k+4-\delta)+\frac{1}{4} E\left[\operatorname{HLB}_{\delta}(x) \mid x_{2 k+3}=x_{2 k+4}=1\right]
\end{aligned}
$$

The induction hypothesis can be applied to the last term, yielding

$$
E\left[\operatorname{HLB}_{\delta}(x)\right] \leq \frac{1}{4}(2 k+2)+\frac{1}{2}(2 k+4-\delta)+\frac{1}{4}(2 k+6) \leq 2 k+4
$$

By induction, this proves the lemma.
We now estimate the expected progress in one iteration, first in the case that the parent has an even DLB value (Lemma 8), then in the case that it is a local optimum (Lemma 9).

Lemma 8. Let $m \in\left[\frac{n}{4} \ldots \frac{n}{2}-1\right]$. Let $x$ be a random bit string such that $\operatorname{DLB}(x)=2 m$ and that the bits $x_{i}, i \in[2 m+3 . . n]$ are independent and uniformly distributed in $\{0,1\}$. Let $y$ be a random bit string generated from $x$ via a unary unbiased variation operator $V$. Let

$$
Y:=\left(\operatorname{HLB}_{\delta}(y)-\operatorname{HLB}_{\delta}(x)\right) \mathbb{1}_{\operatorname{DLB}(y) \geq \operatorname{DLB}(x)}
$$

Then we have

$$
E[Y] \leq \frac{2 \delta}{n}
$$

Proof. Denote by $r_{V}$ the random variable describing the number of bits the operator $V$ flips in its argument. Using Lemma 2, we can decompose the expectation by conditioning on the value of $r_{V}$ :

$$
E[Y]=\sum_{r=1}^{n} E\left[Y \mid r_{V}=r\right] \operatorname{Pr}\left[r_{V}=r\right]
$$

By symmetry we assume that $x_{2 m+1}=1$ and $x_{2 m+2}=0$. We use $F_{2 m+1}\left(F_{2 m+2}\right.$ resp. $)$ to denote the event in which $x_{2 m+1}$ ( $x_{2 m+2}$ resp.) is the only bit that has been flipped among the first $2 m+2$ bits of $x$. We observe that $\{Y<0\}=F_{2 m+1}$ and $\{Y>0\}=F_{2 m+2}$. It follows that

$$
\begin{aligned}
& E\left[Y \mid r_{V}=r\right] \\
& =E\left[Y \mid r_{V}=r, F_{2 m+1}\right] \operatorname{Pr}\left[F_{2 m+1} \mid r_{V}=r\right] \\
& \quad+E\left[Y \mid r_{V}=r, F_{2 m+2}\right] \operatorname{Pr}\left[F_{2 m+2} \mid r_{V}=r\right] \\
& =(\delta-2) \operatorname{Pr}\left[F_{2 m+1} \mid r_{V}=r\right] \\
& \quad+E\left[\operatorname{HLB}_{\delta}(y)-(2 m+2-\delta) \mid r_{V}=r, F_{2 m+2}\right] \operatorname{Pr}\left[F_{2 m+2} \mid r_{V}=r\right]
\end{aligned}
$$

Conditioning on the event $\left\{r_{V}=r\right\} \cap F_{2 m+2}$, the random bit string $y$ has only 1 s in its first $2 m+2$ bit positions and the other bits of $y$ are independent and uniformly distributed in $\{0,1\}$. Lemma 7 thus gives that

$$
E\left[\operatorname{HLB}_{\delta}(y) \mid r_{V}=r, F_{2 m+2}\right] \leq 2 m+4
$$

Therefore we have

$$
\begin{aligned}
& E\left[Y \mid r_{V}=r\right] \\
& \quad \leq(\delta-2) \operatorname{Pr}\left[F_{2 m+1} \mid r_{V}=r\right]+(\delta+2) \operatorname{Pr}\left[F_{2 m+2} \mid r_{V}=r\right]
\end{aligned}
$$

Now we analyze the two probabilities

$$
\begin{aligned}
\operatorname{Pr}\left[F_{2 m+1} \mid r_{V}=r\right] & =\operatorname{Pr}\left[F_{2 m+2} \mid r_{V}=r\right] \\
& =\binom{n-2 m-2}{r-1}\binom{n}{r}^{-1}=: D_{r}
\end{aligned}
$$

We calculate for $r-1 \leq n-2 m-2$ that

$$
\begin{aligned}
\frac{D_{r+1}}{D_{r}} & =\frac{\binom{n-2 m-2}{r}\binom{n}{r+1}^{-1}}{\binom{n-2 m-2}{r}\binom{n}{r}^{-1}}=\frac{(r+1)(n-2 m-1-r)}{r(n-r)} \\
& =\frac{n-2 m-1-2(n+1) r}{r(n-r)}+1
\end{aligned}
$$

Since $r \geq 1$ and $m \geq \frac{n}{4}$, we have

$$
n-2 m-1-2(m+1) r \leq n-4 m-3<0
$$

This implies that $\frac{D_{r+1}}{D_{r}}<1$. Noting also that $D_{r}=0$ for $r>n-2 m-2$, we see that $D_{r}$ is decreasing in $r$. Consequently, we have

$$
D_{r} \leq D_{1}=\frac{1}{n}
$$

for all $r \geq 1$. Combining this with (2) and (3), we obtain

$$
E\left[Y \mid r_{V}=r\right] \leq 2 \delta D_{r} \leq \frac{2 \delta}{n}
$$

for all $r \geq 1$. Substituting this into (1), the conclusion follows.
Lemma 9. Let $m \in\left[\frac{n}{3}, \frac{n}{2}-1\right]$. Let $x$ be a random bit string such that $\operatorname{DLB}(x)=2 m+1$ and that the bits $x_{i}, i \in[2 m+3 . . n]$, are independent and uniformly distributed in $\{0,1\}$. Let $y$ be a random bit string generated from $x$ by a unary unbiased variation operator $V$. Let $Y:=\left(\operatorname{HLB}_{\delta}(y)-\operatorname{HLB}_{\delta}(x)\right) \mathbb{1}_{\operatorname{DLB}(y) \geq \operatorname{DLB}(x)}$. Then we have

$$
E[Y] \leq \frac{16}{n^{2}}
$$

Proof. Since $\operatorname{DLB}(x)=2 m+1, \operatorname{DLB}(y) \geq \operatorname{DLB}(x)$ implies $\operatorname{HLB}_{\delta}(y) \geq \operatorname{HLB}_{\delta}(x)$. Thus $Y$ is always non-negative and we can decompose $E[Y]$ into a product of two terms

$$
E[Y]=E\left[\operatorname{HLB}_{\delta}(y)-\operatorname{HLB}_{\delta}(x) \mid Y>0\right] \operatorname{Pr}[Y>0]
$$

First we bound the term $E\left[\operatorname{HLB}_{\delta}(y)-\operatorname{HLB}_{\delta}(x) \mid Y>0\right]$. Under the condition $Y>0$, we know that $y_{i}=1$ for $i \in[1 . .2 m+2]$, while the $y_{i}, i \in[2 m+3 . . n]$, are still independent and uniformly distributed in $\{0,1\}$. Lemma 7 then implies that $E\left[\operatorname{HLB}_{\delta}(y) \mid\right.$ $Y>0] \leq 2 m+4$, thus we have

$$
E\left[\operatorname{HLB}_{\delta}(y)-\operatorname{HLB}_{\delta}(x) \mid Y>0\right] \leq 2 m+4-2 m=4
$$

On the other hand, to bound $\operatorname{Pr}[Y>0]=\operatorname{Pr}[\operatorname{DLB}(y)>\operatorname{DLB}(x)]$ we invoke Lemma 2 and compute

$$
\begin{aligned}
& \operatorname{Pr}[\operatorname{DLB}(y)>\operatorname{DLB}(x)] \\
& =\sum_{r=2}^{n-2 m} \operatorname{Pr}\left[r_{V}=r\right] \operatorname{Pr}[\operatorname{DLB}(y)>\operatorname{DLB}(x) \mid r_{V}=r] \\
& =\sum_{r=2}^{n-2 m} \operatorname{Pr}\left[r_{V}=r\right]\binom{n-2 m-2}{r-2}\binom{n}{r}^{-1} \\
& \leq \max _{2 \leq r \leq n-2 m}\binom{n-2 m-2}{r-2}\binom{n}{r}^{-1}
\end{aligned}
$$

where $r$ can be restricted to $2 \leq r \leq n-2 m$ since otherwise $Y$ would certainly be zero. With $E_{r}:=\binom{n-2 m-2}{r-2}\binom{n}{r}^{-1}$, we have

$$
\frac{E_{r+1}}{E_{r}}=\frac{2(n-m-(m+1) r)}{(r-1)(n-r)}+1<1
$$

by our hypothesis $n-3 m \leq 0$ and $r \geq 2$. As in Lemma 8 we conclude that $E_{r}$ is decreasing in $r$ and

$$
\begin{aligned}
& \operatorname{Pr}[Y>0] \\
& =\operatorname{Pr}[\operatorname{DLB}(y)>\operatorname{DLB}(x)] \leq \max _{2 \leq r \leq n-2 m} E_{r}=E_{2}=\binom{n}{2}^{-1} \leq \frac{4}{n^{2}}
\end{aligned}
$$

Combining (5), (6) and (7), we obtain $E[Y] \leq \frac{16}{n^{2}}$.
With the estimates on the change of the potential HLB above, we can now easily prove the main result of this section. By taking $\delta=\Theta\left(\frac{1}{n}\right)$ suitably, we ensure that the expected gain of the potential in one iteration is only $O\left(\frac{1}{n^{2}}\right)$, at least in a sufficiently large range of the potential space. To have a small progress in the whole search space, as necessary to apply the additive drift theorem, we regard the potential $h_{t}=\operatorname{HLB}_{\delta}\left(x^{(t+S)}\right)$, where $S$ denotes the first time that $x^{(t)}$ has an HLB value not less than $\frac{2 n}{3}$. This potential also has a drift of only $O\left(\frac{1}{n^{2}}\right)$ and thus the additive drift theorem easily gives the lower bound of $\Omega\left(n^{3}\right)$.

Theorem 10. The $(1+1)$-elitist black-box complexity of the DLB problem is $\Omega\left(n^{3}\right)$.
Proof. Consider any $(1+1)$-elitist algorithm $A$. Let $x^{(t)}$ denote the individual at time $t$. By a slight abuse of notation we write $\frac{2 n}{3}$ to denote the even integer $\min \left\{\ell \in 2 \mathbb{N} \mid \ell \geq \frac{2 n}{3}\right\}$. First we observe that $\operatorname{Pr}\left[\operatorname{HLB}\left(x^{(0)}\right) \geq \frac{2 n}{3}\right]=\Theta\left(2^{-\frac{3}{3} n}\right)$. In the following we work under the condition $\mathcal{C}:=\left\{\operatorname{HLB}\left(x^{(0)}\right)<\frac{2 n}{3}\right\}$. Under this condition, $S:=\min \left\{t \in \mathbb{N} \mid \operatorname{HLB}\left(x^{(t)}\right) \geq \frac{2 n}{3}\right\}$ is strictly positive. Let $T:=\min \left\{t \in \mathbb{N} \mid \operatorname{HLB}\left(x^{(t)}\right) \geq n\right\}+1$ be the runtime of $A$. We will use the additive drift theorem (Theorem 3) to prove $E[T-S \mid \mathcal{C}]=\Omega\left(n^{3}\right)$, from which the claim follows via

$$
E[T] \geq \operatorname{Pr}[\mathcal{C}] E[T \mid \mathcal{C}] \geq(1-o(1)) E[T-S \mid \mathcal{C}]
$$

For a $\delta$ to be specified later, we regard the potential $h_{t}=\operatorname{HLB}_{\delta}\left(x^{(t+S)}\right)$. Note that because of the elitism of our algorithm, we have $h_{t} \geq \frac{2 n}{3}$ for all $t \geq 0$. Let $m \in\left[\frac{n}{3}, \frac{n}{2}-1\right]$.

Lemma 6 implies that when conditioning on the event $\left\{h_{t}=2 m+2-\delta\right\}=\left\{\operatorname{DLB}\left(x^{(t+S)}\right)=2 m\right\}$, the bits $x_{i}^{(t+S)}, i \in$ $[2 m+3 . . n]$, are independent and uniformly distributed in $[0,1]$. Let $y$ be a bit string obtained by applying a unary unbiased variation operator to $x^{(t+S)}$. Lemma 8 then applies to $y$ and $x^{(t+S)}$, yielding

$$
E\left[\left(\operatorname{HLB}_{\delta}(y)-\operatorname{HLB}_{\delta}\left(x^{(t+S)}\right)\right) \mathbb{1}_{\operatorname{DLB}(y) \geq \operatorname{DLB}\left(x^{(t+S)}\right)} \mid \mathcal{C}\right] \leq \frac{2 \delta}{n}
$$

Since the term on the left-hand side is the expected increase in the HLB function during an iteration, we have in fact proven that $\Delta_{t}(2 m+2-\delta):=E\left[h_{t+1}-h_{t} \mid h_{t}=2 m+2-\delta, \mathcal{C}\right] \leq \frac{2 \delta}{n}$ for any $t$.

For the case $\left\{h_{t}=2 m\right\}$ we proceed in the same manner (except that we use Lemma 9 instead of Lemma 8) to obtain $\Delta_{t}(2 m) \leq \frac{16}{n^{2}}$ for any $t$. By setting $\delta$ to $\frac{8}{n}, \Delta_{t}(s) \leq \frac{16}{n^{2}}$ holds for any possible $h_{t}$ value $s$.

Recall that $\frac{2 n}{3}$ denotes the smallest even integer not less than it. By the definition of $S$ and by Lemma $6, x^{(S)}$ is a random bit string satisfying $x_{i}^{(S)}=1$ for $i \in\left[1 . . \frac{2 n}{3}\right]$ and such that $x_{i}^{(S)}, i \in\left[\frac{2 n}{3}+1 . . n\right]$, are independent and uniformly distributed in $\{0,1\}$. Thus we have $E\left[h_{0}\right]=E\left[\operatorname{HLB}_{\delta}\left(x^{(S)}\right)\right]=\frac{2 n}{3}+O(1)$ by virtue of Lemma 7. The additive drift theorem (Theorem 3) then yields

$$
E[T-S \mid \mathcal{C}] \geq \frac{n-\frac{2 n}{3}-O(1)}{16 / n^{2}}=\Theta\left(n^{3}\right)
$$

which finishes the proof with (8).

# 3.2. The unary unbiased black-box complexity of the DLB problem is at most quadratic 

In the preceding section we have seen that elitism does not ease optimizing the DLB problem. This section, therefore, is devoted to investigating the best possible expected runtime on the DLB problem without elitism. To be more precise, we show that the unary unbiased black-box complexity of the DLB problem is $O\left(n^{2}\right)$. This result will be complemented by a matching lower bound (Theorem 18) in Section 3.5.

We recall the definition of a $k$-ary unbiased black-box algorithm (Algorithm 2) from Section 2.2. The $k$-ary unbiased black-box complexity of a problem is defined as the infimum expected runtime of a $k$-ary unbiased black-box algorithm on this problem, that is,

$$
\inf _{A} E\left[T_{A}(f)\right]
$$

where $A$ runs through all $k$-ary unbiased black-box algorithms.

Let $V$ be the unary unbiased operator such that $V(x)$ is obtained from flipping one bit of $x$. Then the additive drift theorem implies that the $(1+1)$-elitist black-box algorithm using $V$ as variation operator has an expected runtime of $O\left(n^{2}\right)$ on the LO problem. By a small adjustment of this $(1+1)$-elitist black-box algorithm, we exhibit a simple unary unbiased black-box algorithm that solves the DLB problem in expected time $\Theta\left(n^{2}\right)$. This inspires our investigation on the expected runtime of the Metropolis algorithm in Section 3.3.

Lemma 11. The unary unbiased black-box complexity of the DLB problem is $O\left(n^{2}\right)$.
Proof. We present a simple algorithm and then show that its expected runtime is indeed $O\left(n^{2}\right)$. Throughout the algorithm we only use the unary unbiased operator $V$ that flips exactly one randomly chosen bit.

The algorithm is initialized by generating a search point $x^{(0)}$ at random in $\{0,1\}^{n}$. In generation $t$, we generate a bit string $y=V\left(x^{(t)}\right)$. If $\operatorname{DLB}\left(x^{(t)}\right)$ is even and $\operatorname{DLB}\left(x^{(t)}\right)<\operatorname{DLB}(y)$ we accept $y$ as new search point, i.e., $x^{(t+1)}:=y$. If $\operatorname{DLB}\left(x^{(t)}\right)$ is odd and $\operatorname{DLB}\left(x^{(t)}\right)<2+\operatorname{DLB}(y)$, we also accept $y$ as new search point, i.e., $x^{(t+1)}:=y$. In all other cases, we reject $y$, i.e., $x^{(t+1)}:=x^{(t)}$.

Now we show that this algorithm finds the optimum of the DLB problem in time $O\left(n^{2}\right)$. We define the potential at time $t$ as $k_{t}=\operatorname{HLB}_{2}\left(x^{(t)}\right)$. In the case where $k_{t}=2 m$, that is, $\operatorname{DLB}\left(x^{(t)}\right)$ is odd, we have a 00 critical block and the probability that we flip one of its two zeros is $\frac{2}{n}$, yielding an expected gain of at least $\frac{2}{n} \cdot \frac{1}{2}=\frac{1}{n}$ in the potential. In the case where $k_{t}=2 m+\frac{1}{2}$, that is, $\operatorname{DLB}\left(x^{(t)}\right)$ is even, the critical block contains exactly one zero and one one. If the bit with value 0 is flipped, we increase the potential from $2 m+\frac{1}{2}$ to at least $2(m+1)$. If the bit with value 1 is flipped, we reduce the potential from $2 m+\frac{1}{2}$ to 2 m . All other bit-flips are not accepted or do not change the potential. Consequently, the expected gain in potential is at least $\frac{1}{n}\left(2(m+1)-\left(2 m+\frac{1}{2}\right)\right)+\frac{1}{n}\left(2 m-\left(2 m+\frac{1}{2}\right)\right)=\frac{1}{n}$. Since the potential needs to be increased by at most $n$, the additive drift theorem (Theorem 3) establishes $\frac{n}{1 / n}=n^{2}$ as an upper bound for the expected runtime of this algorithm on the DLB function.

We remark that the artificial algorithm defined in the proof is a $(1+1)$-type unbiased algorithm, therefore we have the following stronger result.

Theorem 12. The $(1+1)$-type unbiased black-box complexity of the DLB problem is $O\left(n^{2}\right)$.

# 3.3. The Metropolis algorithm performs well on the DLB problem 

Inspired by the analysis in the preceding sections, we expect that certain non-elitist $(1+1)$-type unbiased search heuristics outperform elitist EAs on the DLB problem. In fact, we will prove now that the Metropolis algorithm (simulated annealing with a fixed temperature) can solve the DLB problem within $\Theta\left(n^{2}\right)$ fitness evaluations in expectation. This performance coincides with the unary unbiased black-box complexity of the DLB function (Theorem 18).

The Metropolis algorithm is a simple single-trajectory optimization heuristic. In contrast to elitist algorithms like randomized local search or the $(1+1)$ EA, it can accept inferior solutions, however only with a small probability that depends on the degree of inferiority and an algorithm parameter $\alpha \in(1, \infty)$.

More precisely, the maximization version of the Metropolis algorithm works as follows. It starts with a random initial solution $x^{(0)}$. In each iteration $t=1,2, \ldots$, it generates a random neighbor $y$ of the current search point $x^{(t-1)}$. When working with a bit string representation (as in this work), such a neighbor is obtained from flipping in $x^{(t-1)}$ a single bit chosen uniformly at random. If $f(y) \geq f\left(x^{(t-1)}\right)$, then the algorithm surely accepts $y$ as new search point $x^{(t)}:=y$. If $y$ is inferior to $x^{(t-1)}$, it accepts $y\left(x^{(t)}:=y\right)$ only with probability $\alpha^{f(y)-f\left(x^{(t-1)}\right)}$ and otherwise rejects it $\left(x^{(t)}:=x^{(t-1)}\right)$. We note that the probability $\alpha^{f(y)-f\left(x^{(t-1)}\right)}$ for accepting an inferior solution is often written as $\exp \left(\left(f(y)-f\left(x^{(t-1)}\right)\right) / k T\right)$ for a "temperature parameter" $k T$, but clearly the two formulations are equivalent. The pseudocode for this algorithm is given in Algorithm 4.

```
Algorithm 4: Metropolis algorithm for maximizing a function \(f:\{0,1\}^{n} \rightarrow \mathbb{R}\).
Generate a search point \(x^{(0)}\) uniformly in \(\{0,1\}^{n}\);
for \(t=1,2,3, \ldots\) do
    Choose \(i \in[1, n]\) uniformly at random and obtain \(y\) from flipping the \(i\)-th bit in \(x^{(t-1)}\);
    if \(f(y) \geq f\left(x^{(t-1)}\right)\) then
        \(x^{(t)} \leftarrow y ;\)
    else
        Choose \(b \in\{0,1]\) randomly with \(\operatorname{Pr}\left\{b=1\right\}=\alpha^{f(y)-f\left(x^{(t-1)}\right)} ;\)
        if \(b=1\) then
            \(x^{(t)} \leftarrow y ;\)
        else
            \(x^{(t)} \leftarrow x^{(t-1)} ;\)
```

Now we show that the Metropolis algorithm with sufficiently large parameter $\alpha$ can solve the DLB problem in time quadratic in $n$. To this end, we show the following elementary lemma.

Lemma 13. For all $\alpha>\sqrt{2}+1$,

$$
C(\alpha):=\frac{2}{\alpha}\left(\frac{1}{2}-2 \sum_{k=1}^{\infty} k \alpha^{-2 k}\right)
$$

is a strictly positive constant.
Proof. We observe that

$$
\alpha^{-2} \sum_{k=1}^{\infty} k \alpha^{-2 k}=\sum_{k=1}^{\infty} k \alpha^{-2(k+1)}=\sum_{k=2}^{\infty}(k-1) \alpha^{-2 k}
$$

Subtracting $\sum_{k=1}^{\infty} k \alpha^{-2 k}$ from both sides of the equation yields

$$
\left(\alpha^{-2}-1\right) \sum_{k=1}^{\infty} k \alpha^{-2 k}=\sum_{k=2}^{\infty}-\alpha^{-2 k}-\alpha^{-2}=-\sum_{k=1}^{\infty} \alpha^{-2 k}=-\frac{\alpha^{-2}}{1-\alpha^{-2}}
$$

which implies

$$
\sum_{k=1}^{\infty} k \alpha^{-2 k}=\frac{\alpha^{-2}}{\left(1-\alpha^{-2}\right)^{2}}=\frac{\alpha^{2}}{\left(\alpha^{2}-1\right)^{2}}
$$

Hence we have

$$
C(\alpha)=\frac{2}{\alpha}\left(\frac{1}{2}-2 \frac{\alpha^{2}}{\left(\alpha^{2}-1\right)^{2}}\right)=\frac{\alpha^{4}-6 \alpha^{2}+1}{\alpha\left(\alpha^{2}-1\right)^{2}}
$$

For all $\alpha>\sqrt{2}+1$, we have $\alpha^{4}-6 \alpha^{2}+1>0$, which implies $C(\alpha)>0$.
We now show the main result of this section that the Metropolis algorithm can optimize the DLB function in quadratic time if the selection pressure is sufficiently high, that is, $\alpha$ is a large enough constant.

Theorem 14. The expected runtime of the Metropolis algorithm on the DLB problem is at most $\frac{\alpha^{2}}{C(\alpha)}$, provided that the parameter $\alpha$ satisfies $\alpha>\sqrt{2}+1$.

To prove this result, we need to argue that the negative effect of accepting solutions further away from the optimum is outweighed by the positive effect that a critical 00 -block can be changed into a critical block 01 or 10 despite the fact that this decreases the DLB value. To achieve this, we design a suitable potential function, namely the HLB function introduced in Section 2.4 with parameter $\delta=\frac{3}{2}$ and show that each iteration (starting with a non-optimal search point) in expectation increases this potential by $\Omega\left(\frac{1}{n}\right)$. With this insight, the additive drift theorem immediately gives the claim.

Proof of Theorem 14. We denote by $x^{(t)}$ the search point obtained at the end of iteration $t$. To apply drift analysis we take $\mathrm{HLB}_{\frac{3}{2}}$ as potential and abbreviate $\mathrm{HLB}_{\frac{1}{2}}\left(x^{(t)}\right)$ by $h_{t}$. Recalling that the Metropolis algorithm generates each Hamming neighbor $y$ of $x^{(t-1)}$ with equal probability $\frac{1}{n}$, but accepts this only with probability $\alpha^{\min [0, f(y)-f\left(x^{(t-1)}\right)]}$, we compute for each $m \in\left[0, \frac{0}{2}-1\right]$ that

$$
\begin{aligned}
& E\left[h_{t}-h_{t-1} \mid h_{t-1}=2 m+\frac{1}{2}\right] \\
& \quad \geq \frac{1}{n}\left(2 m+2-\left(2 m+\frac{1}{2}\right)\right)+\frac{1}{n}\left(2 m-\left(2 m+\frac{1}{2}\right)\right) \\
& \quad+\sum_{k=0}^{m-1} \frac{2}{n} \alpha^{2 k-2 m}\left(2 k+\frac{1}{2}-\left(2 m+\frac{1}{2}\right)\right) \\
& \quad=\frac{1}{n}+\frac{2}{n} \sum_{k=1}^{m} \alpha^{-2 k}(-2 k)=\frac{2}{n}\left(\frac{1}{2}-2 \sum_{k=1}^{m} k \alpha^{-2 k}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
& E\left[h_{t}-h_{t-1} \mid h_{t-1}=2 m\right] \\
& \quad \geq \frac{2}{n} \frac{1}{\alpha}\left(2 m+\frac{1}{2}-2 m\right)+\sum_{k=0}^{m-1} \frac{2}{n} \alpha^{2 k-2 m-1}\left(2 k+\frac{1}{2}-2 m\right) \\
& \quad=\frac{2}{n \alpha} \frac{1}{2}+\sum_{k=1}^{m} \frac{2}{n \alpha} \alpha^{-2 k}\left(\frac{1}{2}-2 k\right)>\frac{2}{n \alpha}\left(\frac{1}{2}-2 \sum_{k=1}^{m} k \alpha^{-2 k}\right)
\end{aligned}
$$

We have shown in Lemma 13 that $\frac{1}{2}-2 \sum_{k=1}^{\infty} k \alpha^{-2 k}>0$ for all $\alpha>\sqrt{2}+1$. Thus for any $s \neq n$,

$$
\begin{aligned}
& E\left[h_{t}-h_{t-1} \mid h_{t-1}=s\right] \\
& \quad \geq \frac{2}{n \alpha}\left(\frac{1}{2}-2 \sum_{k=1}^{m} k \alpha^{-2 k}\right) \geq \frac{2}{n \alpha}\left(\frac{1}{2}-2 \sum_{k=1}^{\infty} k \alpha^{-2 k}\right)=\frac{C(\alpha)}{n}
\end{aligned}
$$

The additive drift theorem (Theorem 3) now implies that the expected runtime of Metropolis algorithm on the DLB problem is bounded by

$$
\frac{n}{C(\alpha) / n}=\frac{n^{2}}{C(\alpha)}
$$

which concludes the proof.

# 3.4. Literature review on the Metropolis algorithm and non-elitist evolutionary algorithms 

To put our results on the Metropolis algorithm into context, we now briefly survey the known runtime results on this algorithm and non-elitist evolutionary algorithms, which are surprisingly few compared to the state of the art for elitist search heuristics.

### 3.4.1. Metropolis algorithm

We first note that the Metropolis algorithm is a special case of simulated annealing, which can be described as the Metropolis algorithm using a temperature that is decreasing over time, that is, the parameter $\alpha$ increases over time in the language of Algorithm 4. We refer to [68] for a survey of the main applied results and restrict ourselves to the known theory results. Here the survey of Jansen [69], even though from 2011, still is a good source of information.

Already in 1988, Sasaki and Hajek [70] showed that the Metropolis algorithm (and also its generalization simulated annealing) has an at least exponential worst-case runtime on the maximum matching problem. On the positive side, the Metropolis algorithm with constant temperature (constant $\alpha$ ) can compute good approximate solutions. Analogous results, however, have also been shown for the $(1+1)$ EA by Giel and Wegener [71]. Jerrum and Sorkin [72] showed that the Metropolis algorithm can solve the minimum bisection problem in quadratic time in random instances in the planted bisection model. Wegener [73] provided a simple instance of the minimum spanning tree (MST) problem, which can be solved very efficiently by simulated annealing with a natural cooling schedule, but for which the Metropolis algorithm with any temperature needs an exponential time to find the optimum. A similar result for the traveling salesman problem was given by Meer [74]. In fact, Wegener [73] proved that simulated annealing in polynomial time finds the optimum of any MST instance with $\varepsilon$-separated weights. His conjecture that simulated annealing in polynomial time computes $\varepsilon$-approximations to any instance was recently proven in [75].

Jansen and Wegener [76] proved that the Metropolis algorithm with $\alpha \geq \varepsilon n$, that is, with a very small temperature in the classic language, optimizes the OneMax benchmark in time $O(n \log n)$, a runtime also known for many simple evolutionary algorithms [77,78,45,79]. They further show that this runtime is polynomial if and only if $\alpha=\Omega(n / \log n)$. Consequently, in the classic language, only for very small temperatures (that is, with very low probabilities of accepting an inferior solution) the Metropolis algorithm is efficient on the OneMax benchmark. An extension of this characterization to arbitrary symmetric functions (that is, functions $f$ that can be written as $f(x)=g(\operatorname{OneMax}(x))$ for some $g: \mathbb{R} \rightarrow \mathbb{R}$ ) was given in [80]. While it is interesting that such a characterization could be obtained, the characterization itself remains hard to interpret. Jansen and Wegener [76] further designed several example problems showing different or similar runtimes of the Metropolis algorithm and the $(1+1)$ EA, among them the function $f_{2}$, which can be solved by the Metropolis algorithm with $\alpha=n$, that is, again a very small temperature, in polynomial expected time, whereas the $(1+1)$ EA needs time $n^{\Omega(\log \log n)}$, and another function for which the Metropolis algorithm with any parameter setting has an expected runtime of $\Omega\left(2^{0.275 n}\right)$, whereas the $(1+1)$ EA has an expected runtime of only $\Theta\left(n^{2}\right)$.

In their work on the Metropolis algorithm and the Strong Selection Weak Mutation (SSWM) algorithm, Oliveto, Paixão, Heredia, Sudholt, and Trubenová [81] proposed the Valley problem, which contains a fitness valley with descending slope

of length $\ell_{1}$ and depth $d_{1}$ and ascending slope of length $\ell_{2}$ and height $d_{2}$. This valley is constructed onto a long path function, making this essentially a one-dimensional optimization problem (despite being defined on $[0,1]^{n}$ ). They proved rigorously that the Metropolis algorithm takes an expected number of $n \alpha^{k \times d_{1} i}+\Theta\left(n \ell_{2}\right)$ function evaluations to cross this valley of low fitness when $\alpha$ (in the notation of Algorithm 4, note that the $\alpha$ used in [81] has a different meaning) is at least $\alpha \geq \exp \left(c \max \left\{\ell_{1} / d_{1}, \ell_{2} / d_{2}\right\}\right)$ for a sufficiently large constant $c$. A similar result holds for the SSWM algorithm. Since the $(1+1)$ EA needs time $\Omega\left(n^{\ell_{1}}\right)$ to cross the valley, here the Metropolis and SSWM algorithm are clearly superior.

In their time complexity analysis of the move acceptance hyper-heuristic (MAHH), Lissovoi, Oliveto, and Warwicker [82] also consider the Metropolis algorithm. For the multimodal CLIfF benchmark with constant cliff length $d$, they show that the Metropolis algorithm needs at least an expected number of $\Omega\left(\binom{n}{d}\left(\binom{n}{\log n}\right)^{d-1.5}\right.$ iterations to find the optimum, which is at most a little faster than the $\Theta\left(n^{d}\right)$ runtime of simple mutation-based algorithms. However, this is much worse than the $O(n \log n)$ performance of a self-adjusting $(1, \lambda)$ EA [83] (only proven for $d=n / 3$ ), the $O\left(n^{3}\right)$ runtime of the MAHH [82], the $O\left(\left(n / d\right)^{2} n \log n\right)$ runtime of two self-adjusting fast artificial immune systems [84], and the $O\left(n^{3.9767}\right)$ runtime of the $(1, \lambda)$ EA with the best static choice of $\lambda$ [83] (improving the well-known $O\left(n^{25}\right)$ runtime guarantee [85]), again only for $d=n / 3$. For the multimodal JUMP benchmark, the Metropolis algorithm was shown [82] to have a runtime exponential in $n$ with high probability regardless of the jump size $m$ when the temperature is sufficiently small that the local optimum of the jump function is reached efficiently. This compares unfavorably with the known runtimes of many algorithms, which are all $\Theta\left(n^{m}\right)$ or better, see, e.g., [22,86-89,36,90-95].

In summary, we would not say that these results give a strong recommendation for using the Metropolis algorithm to optimize pseudo-Boolean functions. It excels on the $f_{2}$ function proposed in [76] and the Valley problem proposed in [81], however, problems essentially are one-dimensional problems and thus of a very different structure than most pseudoBoolean problems. The possible $\hat{O}\left(n^{0.5}\right)$ runtime advantage over simple EAs on the CLIfF problem is interesting (if it exists, only a lower bound was shown in [82]), but appears still small when recalling that the runtime of the simple EAs is $\Theta\left(n^{d}\right)$. Hence maybe most convincing result favoring the Metropolis algorithm is the quadratic runtime shown [72] for the random bipartition instances. Here, however, one also has to recall that random instances of $N P$-complete problems can by surprisingly easy. For example, the $(1+1)$ EA can solve random 3-SAT instances in the planted solution model in time $O(n \log n)$ when the clause density is at least logarithmic [96]. These mildly positive results on the Metropolis algorithm have to be contrasted with several negative results, e.g., the exponential runtimes shown in [70,73,74]. Also, the parameter choice seems to be non-trivial. Whereas the best results in [81] are obtained by small values of $\alpha$, recall that the runtime shown there is at least $n \alpha^{\Omega\left(d_{1}\right)}$ and the simple OneMax benchmark can only be optimized in polynomial time when $\alpha$ is as large as $\Omega(n \log n)$.

For reasons of completeness, we note that after the completion of this work a runtime analysis of the Metropolis algorithm on a generalized CLIfF benchmark has appeared [97]. It showed that the Metropolis algorithm for most parameters of the benchmark has a performance inferior to the one of simple elitist algorithms.

# 3.4.2. Non-elitist evolutionary algorithms 

The strategy to not stick with the best-so-far solution to enable the algorithm to leave a local optimum is also wellknown in evolutionary computation. However, also there the rigorous support for such non-elitist algorithms is rather weak.

There is a fairly elaborate methodology to prove upper bounds on the runtime of non-elitist algorithms [47-50], however, these tools so far could mostly be applied to settings where the evolutionary algorithm loses the best-so-far solution so rarely that it roughly imitates an elitist algorithm. A few analyses of particular algorithms point into a similar direction [85, 98]. The existing general lower bound methods for non-elitist algorithms [51,52] in many cases allowed to prove that with just a little more non-elitism, the algorithm has no chance to optimize efficiently any pseudo-Boolean function with unique optimum.

As a concrete example, the standard $(\mu, \lambda)$ EA using mutation rate $\frac{1}{\lambda}$ cannot optimize any pseudo-Boolean function with unique optimum in sub-exponential time if $\lambda \leq(1-\varepsilon) \varepsilon \mu, \varepsilon>0$ any constant [51,52]. However, when $\lambda \geq(1+\varepsilon) \varepsilon \mu$ and $\lambda=\omega(\log n)$, then the $(\mu, \lambda)$ EA optimizes OneMax and Jump functions with constant jump size in essentially the same runtime as the $(\mu+\lambda)$ EA [47,50]. This suggests that there is at most a very small regime in which non-elitism can be successfully exploited. Such a small middle regime was shown to exist when optimizing CLIfF functions via the $(1, \lambda)$ EA. More specifically, Jägersküpper and Storch [85] showed that the $(1, \lambda)$ EA with $\lambda \geq 5 \ln n$ optimizes the CLIfF function with cliff length $n / 3$ in time $\exp (5 \lambda) \geq n^{25}$, whereas elitist mutation-based algorithms easily get stuck in the local optimum and then need at least $n^{n / 3}$ expected time to optimize this CLIfF function. This result was very recently improved and runtime of $O\left(n^{3.9767}\right)$ was shown for the asymptotically best choice of $\lambda$ [83]. For the $(\mu, \lambda)$ EA optimizing jump functions, however, the existence of a profitable middle regime was disproven in [91]. Some more results exist that show situations where only an inefficient regime exists, e.g., when using (1+1)-type hillclimbers with fitness-proportionate selection to optimize linear pseudo-Boolean functions [99] or when using a mutation-only variant of the simple genetic algorithm to optimize OneMax [100]. For the true simple genetic algorithm, such a result exists only when the population size is at most $\mu \leq n^{1 / 4-\varepsilon}$, but there is no proof that the situation improves with larger population size [101].

The few results showing that non-elitism can help to leave local optima include, besides the examples for the Metropolis algorithm discussed in Section 3.4.1 (see the last paragraph of that section for a summary) and the two "small middle

regime" results discussed in the previous paragraph, the following. Dang, Eremeev, and Lehre [102] showed that a nonelitist EA with 3-tournament selection, population size $\lambda \geq c \log n$ for $c$ a positive constant, and bitwise mutation with rate $\chi / n, \chi=1.09812$, can reach the optimum of the multi-modal Funnel problem with parameter $\omega \leq \frac{4}{3} n$ in expected time $O\left(n \lambda \log \lambda+n^{2} \log n\right)$, whereas the $(\mu+\lambda)$ EA and the $(\mu, \lambda)$ EA cannot reach the optimum in time $2^{c^{n}}, c^{c}>0$ a suitable constant, with overwhelming probability. In [103], the same authors defined a class of functions having an exponential elitist $(\mu+\lambda)$ black-box complexity which can be solved in polynomial time by several non-elitist algorithms. Fajardo and Sudholt [83] showed that a self-adjusting variant of the $(1, \lambda)$ EA can optimize Cliff functions in time $O(n \log n)$. Zheng, Zhang, Chen, and Yao [104] proved that the $(1, \lambda)$ EA with offspring population size $\lambda=c \log _{\frac{c}{n-1}} n$ for the constant $c \geq 1$ can reach the global optimum of the time-linkage OneMax function in expected time $O\left(n^{3+\varepsilon} \log n\right)$, while the $(1+\lambda)$ EA with $\lambda \in\left[e^{e}, e^{n^{1 / 3}}\right]$ (as well as the $(1+1)$ EA analyzed in [105]) with $1-\sigma(1)$ probability cannot reach the global optimum in arbitrary long time. Very recently, Jorritsma, Lengler, and Sudholt [106] showed that comma selection offers moderate advantages on randomly perturbed OneMax functions.

More results exist for non-classical algorithms. In [107], the strong-selection weak-mutation process from biology is regarded under an algorithmic perspective. It is shown that when setting the two parameters of this algorithm right, then it optimizes the $\operatorname{Cliff}_{d}$ function, $d=\omega(\log n)$, in time $(n / \Omega(1))^{d}$, which is faster than the $(1+1)$ EA by a factor of $\exp (\Omega(d))$. It also optimizes the slightly artificial Balance function with high probability in time $O\left(n^{2.5}\right)$, whereas the $(1+1)$ EA takes weakly exponential time. In [82], a runtime analysis of the move-acceptance hyper-heuristic (MAHH) is performed. This can be seen as a variant of the Metropolis algorithm, where the probability of accepting an inferior solution is an algorithm parameter independent of the degree of inferiority. If this probability is chosen sufficiently small, then the MAHH optimizes all Cliff functions in time $O\left(n^{k}\right)$, significantly beating all other results on this function class. For the $\operatorname{Jump}_{k}$ function, however, the MAHH is not very effective. For all $k=\sigma(\sqrt{n})$ and all values of the acceptance parameter $p$, a lower bound of $\Omega\left(\frac{n^{2 k-1}}{(2 k-1)!}\right)$ was proven in [108]. We note that aging as used in artificial immune systems can also lead to non-elitism and has been shown to speed-up leaving local optima, see, e.g., [109,110,84,111]. Since the concept of aging has not found many applications in heuristic search outside the small area of artificial immune systems used as optimizers, we omit a detailed discussion. Finally, we note that restarts obviously lead to algorithms that can be called non-elitist. We also discuss these not further since we view them, similar as parallel run or racing techniques, rather as mechanisms to be added to basic optimization heuristics. Overall, these examples prove that non-elitism can be helpful, but from their sparsity in the large amount of research on randomized search heuristics, their specificity, and their sometimes still high runtimes, we would not interpret them as strong indication for trying non-elitist approaches early.

# 3.5. A lower bound for the unary unbiased black-box complexity 

In this section we will show that the expected runtime of any unary unbiased black-box algorithm on the DLB problem is $\Omega\left(n^{2}\right)$, which together with the upper bound of Section 3.2 proves that the unary unbiased black-box complexity of the DLB problem is $\Theta\left(n^{2}\right)$. This result is very natural given that Lehre and Witt [11] have proven the same lower bound for the unary unbiased black-box complexity of the LO problem, which appears rather easier than the DLB problem.

To this end, we first prove the following lemma, which affirms that for a search point in a certain range of LO values, the probability of obtaining a search point with better fitness after one step is $O\left(\frac{1}{n}\right)$.

Lemma 15. Suppose that $n$ is an even integer and that $m$ is an integer such that $\frac{n}{4}<m<\frac{n}{4}$. Let $x$ be a bit string and let $\ell:=\mid\{j \in$ $\left[1 . .2 m+2\left\lfloor x_{j}=1\right\rfloor\right]$ designate the number of ones in the leading $2 m+2$ bit positions of $x$. We suppose that $1 \leq \ell \leq 2 m+1$. Then for any unary unbiased operator $V$, we have $\operatorname{Pr}\{\operatorname{LO}(V(x)) \geq 2 m+2\} \leq \frac{2}{n}$.

Proof. We assume that for some $r \in[0 . . n], V$ is the unary unbiased operator that flips $r$ bit positions chosen uniformly at random from the bit string. The conclusion for the general case then follows by applying the law of total probability and Lemma 2 .

We furthermore assume that $2+2 m-\ell \leq r \leq n-\ell$ since otherwise the claim is trivial. Indeed, $r<2+2 m-\ell$ implies $r+\ell<2 m+2$. Since $r+\ell$ is an upper bound on the number of ones $V(x)$ has in the first $2 m+2$ positions, we obtain $\operatorname{LO}(V(x))<2 m+2$ with probability 1 . If $r>n-\ell$, then at least one of the bits $x_{j}=1, j \in[1 . .2 m+2]$, is flipped, also resulting in $\operatorname{LO}(V(x))<2 m+2$.

The event $\{\operatorname{LO}(V(x)) \geq 2 m+2\}$ happens if and only if all bits $x_{j}$ such that $x_{j}=1$ and $j \in[1 . .2 m+2]$, are not flipped, and all bits $x_{j}=0, j \in[1 . .2 m+2]$, are flipped. Among all $\binom{n}{r}$ ways of flipping $r$ bit positions in $x$, exactly $\binom{n-2 m-2}{r-(2 m+2-r)}$ of them flip all the 0 s in the leading $2 m+2$ bit positions and leave all the 1 s in the leading $2 m+2$ bit positions unchanged. Hence the probability $D_{\ell}(r)$ of the event $\{\operatorname{LO}(V(x)) \geq 2 m+2\}$ is given by

$$
D_{\ell}(r)=\frac{\binom{n-2 m-2}{r-(2 m+2-r)}}{\binom{n}{r}}=\frac{(n-r) \cdots(n-r-\ell+1) \cdot r \cdots(r-2 m+\ell-1)}{n \cdots(n-2 m-1)}
$$

From our assumptions, with the variables $n, m$ and $r$ fixed, we have

$$
\ell \in[\max \{1,2 m+2-r\} \ldots \min \{2 m+1, n-r\}] .
$$

For $\ell \in[\max \{1,2 m+2-r\} . . \min \{2 m, n-r-1\}]$, we compute

$$
\frac{D_{\ell+1}(r)}{D_{\ell}(r)}=\frac{2\left(\frac{n}{2}+m-\ell-r\right)+1}{r-2 m+\ell-1}+1
$$

We conclude that $D_{\ell+1}(r)>D_{\ell}(r)\left(D_{\ell+1}(r)<D_{\ell}(r)\right.$ resp. $)$ is equivalent to $\frac{n}{2}+m \geq \ell+r\left(\frac{n}{2}+m<\ell+r\right.$ resp. $)$. To proceed we distinguish three cases regarding the value of $r$.

Case $r \in\left[1 . . \frac{n}{2}-m-1\right]$.
Since $\ell \leq 2 m+1$ (equation (9)), we have $\ell+r \leq 2 m+1+\frac{n}{2}-m-1=\frac{n}{2}+m$, which implies $\frac{D_{\ell+1}(r)}{D_{\ell}(r)}>1$ for all $\ell \in$ $[1 . .2 m+1]$. It follows that $D_{\ell}(r) \leq D_{2 m+1}(r)$ for all $\ell \leq 2 m+1$.

Case $r \in\left[\frac{n}{2}-m . . \frac{n}{2}+m\right]$.
In this case $\frac{D_{\ell+1}(r)}{D_{\ell}(r)}>1$ for $\ell \leq \frac{n}{2}+m-r$ and $\frac{D_{\ell+1}(r)}{D_{\ell}(r)}<1$ for $\ell>\frac{n}{2}+m-r$, from which we conclude $D_{\ell}(r) \leq D_{\frac{n}{2}+m-r+1}(r)$.
Case $r \in\left[\frac{n}{2}+m+1 . . n-1\right]$.
In this case $\ell+r>r>\frac{n}{2}+m$, therefore $D_{\ell+1}(r)<D_{\ell}(r)$. Since $\ell$ is at least 1 , we have $D_{\ell}(r) \leq D_{1}(r)$.
In short, we have established that

$$
D_{\ell}(r) \leq \begin{cases}D_{2 m+1}(r), & r \in\left[1 . . \frac{n}{2}-m-1\right] \\ D_{\frac{n}{2}+m-r+1}(r), & r \in\left[\frac{n}{2}-m . . \frac{n}{2}+m\right] \\ D_{1}(r), & r \in\left[\frac{n}{2}+m+1 . . n-1\right]\end{cases}
$$

By the definition of $D_{\ell}(r)$, we have

$$
\begin{aligned}
& D_{2 m+1}(r)=\binom{n-2 m-2}{r-1}\binom{n}{r}^{-1} \\
& D_{\frac{n}{2}+m-r+1}(r)=\frac{(n-r) \cdots\left(\frac{n}{2}-m\right) \cdot r \cdots\left(\frac{n}{2}-m\right)}{n \cdots(n-2 m-1)} \\
& D_{1}(r)=\frac{(n-r) \cdot r(r-1) \cdots(r-2 m)}{n \cdots(n-2 m-1)}
\end{aligned}
$$

We observe that $D_{2 m+1}(r)$ is in fact the $D_{r}$ that appeared in (3) of Lemma 8 . Since we have proven $D_{r} \leq \frac{1}{n}$ for $r \geq 1$ in (4) of Lemma 8 , the same estimate holds for $D_{2 m+1}(r)$, i.e., $D_{2 m+1}(r) \leq \frac{1}{n}$ for $r \geq 1$.

For $D_{1}(r), r \in\left[\frac{n}{2}+m \ldots n-1\right]$, a straightforward calculation shows

$$
\frac{D_{1}(r+1)}{D_{1}(r)}=\frac{2 m n+n-1-(2 m+2) r}{(r-2 m)(n-r)}+1
$$

Thus $D_{1}(r)<D_{1}(r+1)$ when $r<r^{*}:=\frac{2 m n+n-1}{2 m+2}$ and $D_{1}(r)>D_{1}(r+1)$ when $r>r^{*}$. This implies

$$
\begin{aligned}
D_{1}(r) & \leq D_{1}\left(\left\lceil r^{*}\right\rceil\right)=\frac{n-\left\lceil r^{*}\right\rceil}{n} \frac{\left\lceil r^{*}\right\rceil}{n-1} \cdots \frac{\left\lceil r^{*}\right\rceil-2 m}{n-2 m-1} \\
& <\frac{n-r^{*}}{n}=\frac{1}{2 m+2}\left(1+\frac{1}{n}\right) \leq \frac{1}{\frac{n}{2}+2}\left(1+\frac{1}{n}\right) \leq \frac{2}{n}
\end{aligned}
$$

where in the second last inequality we used the hypothesis $m>\frac{n}{4}$.
For $D_{\frac{n}{2}+m-r+1}(r), r \in\left[\frac{n}{2}-m . . \frac{n}{2}+m\right]$, we have

$$
\frac{D_{\frac{n}{2}+m-r}(r+1)}{D_{\frac{n}{2}+m-r+1}(r)}=\frac{2 r-n+1}{n-r}+1
$$

Hence $D_{\frac{n}{2}+m-r+1}(r)$ decreases with respect to $r$ when $\frac{n}{2}-m \leq r \leq \frac{n}{2}-1$ and increases when $\frac{n}{2} \leq r \leq \frac{n}{2}+m$. Therefore we have for $r \in\left[\frac{n}{2}-m . . \frac{n}{2}+m\right]$

$$
D_{\frac{n}{2}+m-r+1}(r) \leq \max \left\{D_{2 m+1}\left(\frac{n}{2}-m\right), D_{1}\left(\frac{n}{2}+m\right)\right\}
$$

Since it has already been shown that both $D_{2 m+1}(r), r \geq 1$, and $D_{1}(r), r \in\left[\frac{n}{2}+m \ldots n-1\right]$, are bounded by $\frac{2}{n}$, the same bound holds for $D_{\frac{n}{2}+m-r+1}(r), r \in\left[\frac{n}{2}-m \ldots \frac{n}{2}+m\right]$. We thus conclude

$$
\operatorname{Pr}[\operatorname{LO}(V(x)) \geq 2 m+2]=D_{\ell}(r) \leq \frac{2}{n}
$$

Let $\mathbf{1}$ denote $(1, \ldots, 1) \in\{0,1\}^{n}$. Following the standard notation, we write $\lceil i\rceil_{2}:=\{k \in 2 \mathbb{Z} \mid k \geq i\}$ for all $i \in \mathbb{R}$. We recall that $\mathrm{HLB}_{2}(x)$ simply denotes the number of blocks equal to 11 counted from left to right. In the next lemma we will give a lower bound of $\Omega\left(n^{2}\right)$ on the unary unbiased black-box complexity of the DLB problem by considering the potential

$$
h_{t}=\min \left\{2\left\lceil\frac{n}{3}\right\rceil, \max _{s \in[0 . t]}\left\{\left\lceil\frac{n+1}{2}\right\rceil_{2}, \mathrm{HLB}_{2}\left(x^{(s)}\right), \mathrm{HLB}_{2}\left(\mathbf{1}-x^{(s)}\right)\right\}\right\}
$$

that is, the maximum of the $\mathrm{HLB}_{2}$ value of $x^{(s)}, s \in[0 . . t]$, and the $\mathrm{HLB}_{2}$ value of $\mathbf{1}-x^{(s)}, s \in[0 . . t]$, capped into the interval $\left[\left\lceil\frac{n+1}{2}\right\rceil, 2\left\lceil\frac{n}{3}\right\rceil\right]$. The preceding lemma enables us to show that for any unary unbiased black-box algorithm, the expected gain in potential (11) at each iteration is $O\left(\frac{1}{n}\right)$. The additive drift theorem will then imply the $\Omega\left(n^{2}\right)$ lower bound. Before conducting this proof, let us quickly derive a statement similar to Lemma 6, namely that all bits with an index higher than $2 m+2$ are uniformly distributed when $h_{t}$ is at most $m$.

Lemma 16. Consider a run of a unary unbiased black-box algorithm on the DLB problem. Let $x^{(0)}, x^{(1)}, \ldots$ be the search points generated in a run of this algorithm, following the notation of Algorithm 2. Conditional on $h_{t} \leq m$, we have that for each $s \in[0 . . t]$ the random variables $x_{i}^{(s)}, i \in[2 m+3 . . n]$ are independent and uniformly distributed in $\{0,1\}$.

We omit a formal proof of this statement since it is very similar to the proof of Lemma 5. The main argument is that the event $h_{t}$ implies that no search point ever sampled up to iteration $t$ has the $(m+1)$-st block completed. Consequently, bits with index higher than $2 m+2$ have no influence on the run of the algorithm up to this point.

Lemma 17. The unary unbiased black-box complexity of the DLB problem is $\Omega\left(n^{2}\right)$.
Proof. Consider any unary unbiased black-box algorithm, let $x^{(t)}$ be the search point at time $t$. Let $T:=\min \{t \in \mathbb{N} \mid$ $\left.\max \left\{\mathrm{HLB}_{2}\left(x^{(t)}\right), \mathrm{HLB}_{2}\left(\mathbf{1}-x^{(t)}\right)\right\} \geq 2\lceil\frac{n}{3}\rceil\right\}$ be the first time the $\mathrm{HLB}_{2}$ value of a search point or its complement is at least $2\left\lceil\frac{n}{3}\right\rceil$. We will use the additive drift theorem (Theorem 3) to prove $E[T]=\Omega\left(n^{2}\right)$, from which the claim follows since $T$ is a trivial lower bound for the runtime.

Let $t<T$ and let $\mathcal{C}_{m}$ be the event $\left\{h_{t}=2 m\right\}$ for $m \in\left[\frac{1}{2}\left\lceil\frac{n+1}{2}\right\rceil_{2} \cdot\left\lceil\frac{n}{3}\right\rceil-1\right]$. By definition of $h_{t}$ and $T$, one of the events $\mathcal{C}_{m}$ holds. We now estimate $E\left[h_{t+1}-h_{t} \mid \mathcal{C}_{m}\right]$. Let $x^{(s)}, s \in[0 . . t]$, be the individual chosen in iteration $t+1$ to generate $x^{(t+1)}$ (see line 4 of Algorithm 2, note that here we have $k=1$ ). Let $\ell:=\left|\{i \in[1 . .2 m+2] \mid x_{i}^{(s)}=1\}\right|$ be the number of the ones in the leading $2 m+2$ bit positions of $x^{(s)}$. Then $1 \leq \ell \leq 2 m+1$ because otherwise $h_{t}$ would be not less than $2 m+2$.

If $h_{t+1}>h_{t}$, then either $x^{(t+1)}$ has no less than $2 m+2$ leading ones or it has no less than $2 m+2$ leading zeros, i.e.,

$$
\begin{aligned}
& \left\{h_{t+1}>h_{t}\right\} \cap \mathcal{C}_{m} \\
& =\left(\left\{\mathrm{HLB}_{2}\left(x^{(t+1)}\right)>2 m\right\} \cap \mathcal{C}_{m}\right) \dot{\cup}\left(\left\{\mathrm{HLB}_{2}\left(\mathbf{1}-x^{(t+1)}\right)>2 m\right\} \cap \mathcal{C}_{m}\right)
\end{aligned}
$$

Lemma 15 shows that the first scenario happens with probability at most $\frac{2}{n}$, that is,

$$
\operatorname{Pr}\left[\mathrm{HLB}_{2}\left(x^{(t+1)}\right)>2 m \mid \mathcal{C}_{m}\right] \leq \frac{2}{n}
$$

We recall that $x^{(t+1)}$ is obtained from some $x^{(s)}, s \in[0 . . t]$, via a unary unbiased operator. By Lemma 16, the $x_{i}^{(s)}, i \in$ $[2 m+3 . . n]$, are all independent and uniformly distributed in $\{0,1\}$ because of the condition $\mathcal{C}_{m}=\left\{h_{t}=2 m\right\}$. If we condition further on the event $\left\{\mathrm{HLB}_{2}\left(x^{(t+1)}\right)>2 m\right\} \cap \mathcal{C}_{m}$, then $x_{i}^{(t+1)}, i \in[2 m+3 . . n]$, are all independent and uniformly distributed in $\{0,1\}$ and $x_{i}^{(t+1)}=1$ for $i \in[1 . .2 m+2]$. Hence Lemma 7 can be applied to $x^{(t+1)}$, yielding

$$
\begin{aligned}
& E\left[h_{t+1}-h_{t} \mid \mathrm{HLB}_{2}\left(x^{(t+1)}\right)>2 m, \mathcal{C}_{m}\right] \\
& \quad \leq E\left\{\mathrm{HLB}_{2}\left(x^{(t+1)}\right)-2 m \mid \mathrm{HLB}_{2}\left(x^{(t+1)}\right)>2 m, \mathcal{C}_{m}\right\} \\
& \quad \leq 2 m+4-2 m=4
\end{aligned}
$$

For the second scenario, we consider $\mathbf{1}-x^{(s)}$ and $\mathbf{1}-x^{(t+1)}$ instead of $x^{(s)}$ and $x^{(t+1)}$ to obtain

$$
\operatorname{Pr}\left[\mathrm{HLB}_{2}\left(\mathbf{1}-x^{(t+1)}\right)>2 m \mid \mathcal{C}_{m}\right] \leq \frac{2}{n}
$$

and

$$
E\left[h_{t+1}-h_{t} \mid \mathrm{HLB}_{2}\left(\mathbf{1}-x^{(t+1)}\right)>2 m, \mathcal{C}_{m}\right] \leq 4
$$

Combining the two scenarios, we have

$$
\begin{aligned}
E\left[h_{t+1}-h_{t} \mid \mathcal{C}_{m}\right] & =\operatorname{Pr}\left[h_{t+1}>h_{t} \mid \mathcal{C}_{m}\right] E\left[h_{t+1}-h_{t} \mid h_{t+1}>h_{t}, \mathcal{C}_{m}\right] \\
& \leq 2 \cdot \frac{2}{n} \cdot 4=\frac{16}{n}
\end{aligned}
$$

Now we examine the expected initial value of the potential. First we observe that $\operatorname{Pr}\left[\max \left\{\mathrm{HLB}_{2}\left(x^{(0)}\right), \mathrm{HLB}_{2}\left(\mathbf{1}-x^{(0)}\right)\right\} \geq \frac{n}{2}\right]=$ $O\left(2^{-\frac{n}{2}}\right)$ since $x^{(0)}$ is generated uniformly at random in $\{0,1\}^{n}$. Thus

$$
E\left[h_{0}\right] \leq\left[\frac{n+1}{2}\right]_{2}+O\left(n 2^{-\frac{n}{2}}\right)=\frac{n}{2}+O(1)
$$

The additive drift theorem (Theorem 3) thus implies

$$
E[T] \geq \frac{2 n / 3-n / 2-O(1)}{16 / n}=\Theta\left(n^{2}\right)
$$

Combining Lemma 11 with Lemma 17, we have proven the following theorem.
Theorem 18. The unary unbiased black-box complexity of the DLB problem is $\Theta\left(n^{2}\right)$.

# 4. Beyond unary unbiased algorithms 

We recall that in this work we are generally looking for unbiased algorithms as this is most natural when trying to solve a novel problem without much problem-specific understanding. In Sections 3 and 3.2, we have discussed unary unbiased algorithms. Our theory-guided approach has suggested the Metropolis algorithm, which with a $\Theta\left(n^{2}\right)$ runtime improved over the $O\left(n^{3}\right)$ runtime guarantee previously shown for various classic unbiased evolutionary algorithms. Our $\Omega\left(n^{2}\right)$ lower bound for all unary unbiased algorithms, however, also shows that further improvements are not possible with unary unbiased algorithms, and raises the question if algorithms of higher arity are more powerful for the DLB problem.

Following our theory-guided approach, we first exhibit in Section 4.1 that the binary unbiased black-box complexity of the DLB problem is $O(n \log n)$. We did not find a natural binary unbiased black-box algorithm for which we could show an $o\left(n^{2}\right)$ runtime, but by resorting to unrestricted arities, which allows for estimation-of-distribution algorithms, we detected that the significance-based compact genetic algorithm (sig-cGA) [21] has a runtime of $O(n \log n)$ with high probability (Section 4.2).

### 4.1. Unbiased black-box algorithms of higher arity

In this section we will exhibit a binary unbiased black-box algorithm (Algorithm 5) whose runtime on the DLB problem is $O(n \log n)$. Our algorithm builds on two ideas used in [12, Section 5] to design an $O(n \log n)$ binary unbiased black-box algorithm for the LO function: (i) We use a pair $(x, y)$ of search points such that the bits $i$ with $x_{i}=y_{i}$ are exactly the ones for which we know that the optimum also has this bit value in this bit position. (ii) We conduct a random binary search in $\{i \in[1 . . n] \mid x_{i} \neq y_{i}\}$ to find in logarithmic time a bit position such that flipping this bit in either $x$ or $y$ (which one will be visible from the fitness) sets it to the value the optimum has in this position. This operation increases the number of correctly detected bits by one. Different from the situation in [12], in our setting such a good bit value cannot always be detected from a fitness gain (due to the deceptive nature of the DLB problem). We overcome this by regarding the $\mathrm{HLB}_{1}$ function instead. Note that there is a (non-monotonic) one-to-one relation between the fitness values of DLB and $\mathrm{HLB}_{1}$. Hence a black-box algorithm for DLB has access also to the $\mathrm{HLB}_{1}$ value of any bit string.

We first recall from [12] the two binary unbiased variation operators randomWhereDifferent $(\cdot, \cdot)$ and switchIfDistanceOne $(\cdot, \cdot)$. The operator
randomWhereDifferent $(\cdot, \cdot)$
takes two bit strings $y$ and $y^{\prime}$ as input and outputs a bit string $z$ of which the components $z_{i}, i \in[1 . . n]$, are determined by the following rule: we have $z_{i}=y_{i}$ if $y_{i}=y_{i}^{\prime}$, and $z_{i}$ is chosen uniformly at random from $\{0,1\}$ if $y_{i} \neq y_{i}^{\prime}$. This operator is also (and better) known as uniform crossover, but to ease the comparison with [12] we keep the notation used there. The operator switchIfDistanceOne $(\cdot, \cdot)$ takes two bit strings $y$ and $y^{\prime}$ as input and outputs $y^{\prime}$ if the Hamming distance between $y$ and $y^{\prime}$ is one, otherwise it outputs $y$.

We now state our black-box algorithm (Algorithm 5). Since, as discussed, any black-box algorithm for the DLB problem also has access to the $\mathrm{HLB}_{1}$ values, we use this function as well in the algorithm description. Algorithm 5 is initialized by generating a random search point $x$ and its complement $y$ (we note that taking the complement is the unary unbiased operator of flipping $n$ bits).

In each iteration of the for loop, we ensure $\operatorname{HLB}_{1}(y) \leq \operatorname{HLB}_{1}(x)$ by exchanging $x$ and $y$ when necessary and run the subroutine in the lines $6-10$, which flips one bit in $y$ in a way that increases the $\mathrm{HLB}_{1}$ value of $y$. To be more precise, the subroutine does a random binary search for such a bit position. At the beginning of the subroutine, $y^{\prime}$ is set to be $x$. In each

iteration of the repeat loop, $y^{\prime \prime}$ is sampled from randomWhereDifferent $\left(y, y^{\prime}\right)$. If $\operatorname{HLB}_{1}\left(y^{\prime \prime}\right)>\operatorname{HLB}_{1}(y)$, then we accept $y^{\prime \prime}$ and attribute its value to $y^{\prime}$, otherwise we refuse $y^{\prime \prime}$ and proceed to the next iteration of the subroutine.

This subroutine terminates when $y^{\prime}$ and $y$ differ only in one bit position. At this moment $y$ is set to be equal to $y^{\prime}$. Now $x$ and $y$ have exactly one more bit in common, which means the number of correctly detected bits is increased by one. By induction, after $i$ iterations of the for loop, $x$ and $y$ agree on $i$ bit positions. After $n$ iterations, $x$ and $y$ are both equal to the optimum.

```
Algorithm 5: A binary unbiased black-box algorithm for maximizing the DLB function.
    1 initialization: generate a search point \(x\) uniformly at random in \(\left[0,1\right]^{n}\) and let \(y\) be the complement of \(x\);
    2 for \(i \in[1 . . n]\) do
        if \(\mathrm{HLB}_{1}(y)>\mathrm{HLB}_{1}(x)\) then \((x, y) \leftarrow(y, x)\);
        \(y^{\prime} \leftarrow x ;\)
        \(\mathrm{H} \leftarrow \mathrm{HLB}_{1}(y)\);
        repeat
            \(y^{\prime \prime} \leftarrow\) randomWhereDifferent \(\left(y, y^{\prime}\right)\);
            if \(\mathrm{HLB}_{1}(y)<\mathrm{HLB}_{1}\left(y^{\prime \prime}\right)\) then \(y^{\prime} \leftarrow y^{\prime \prime}\);
            \(y \leftarrow \operatorname{switchIfDistanceOne}\left(y, y^{\prime}\right) ;\)
        until \(\operatorname{HLB}(y)>H\);
```

To analyze the time complexity of Algorithm 5, we first consider the runtime of the repeat subroutine.
Lemma 19. The subroutine in lines 6-10 of Algorithm 5 finishes in an expected runtime of $O(\log n)$.
Proof. For sake of simplicity we suppose $\mathrm{LO}(y)=2 m+1$ for some $m$ at the beginning of the subroutine, the cases $\operatorname{DLB}(y)=$ $2 m+1$ and $\operatorname{DLB}(y)=\operatorname{LO}(y)=2 m$ can be treated similarly.

Since $\operatorname{HLB}_{1}\left(y^{\prime \prime}\right)>2 m+1=\operatorname{HLB}_{1}(y)$ if and only if $y_{2 \mathrm{~m}+2}^{\prime \prime}=1$ and this second event happens with probability $\frac{1}{2}$ (line 7), the value of $y^{\prime \prime}$ is assigned to $y^{\prime}$ with probability $\frac{1}{2}$.

Now we consider the bit positions, other than the bit position $2 m+2$, on which $y$ and $y^{\prime}$ are different. Since the bit values of $y^{\prime \prime}$ on these positions are chosen at random, the probability that at least half of them coincide with corresponding bit values in $y$ is at least $\frac{1}{2}$ by virtue of symmetry. Therefore, at the end of an iteration of the subroutine, with probability $\frac{1}{4}$ the number of bit positions other than the bit position $2 m+2$, on which $y$ and $y^{\prime}$ are different, is at most half as before. We note that the number of different bits never increases. Hence, we conclude that in expected runtime $O(\log n), y$ and $y^{\prime}$ are only different in bit position $2 m+2$.

As discussed above, $x$ and $y$ are set to the optimum after having run the for loop for $n$ times. Lemma 19 thus implies the following theorem on the binary unbiased black-box complexity of the DLB problem.

Theorem 20. The binary unbiased black-box complexity of the DLB problem is $O(n \log n)$.
Algorithm 5 reveals that the ability to learn how good solutions look like plays an important role in solving the DLB problem. This inspires the study of EDAs, and more specifically, the significance-based EDA proposed by Doerr and Krejca [21] in the following.

# 4.2. Significance-based compact genetic algorithm (sig-cGA) 

Estimation-of-distribution algorithms (EDAs) optimize a function $f:\{0,1\}^{\mathrm{n}} \rightarrow \mathbb{R}$ by evolving a probabilistic model of the solution space $\{0,1\}^{\mathrm{n}}$ in such a direction that this probabilistic model becomes more likely to sample the optimum.

We now present the sig-cGA (Algorithm 6) proposed by Doerr and Krejca [21]. To this end, we first define the notion of frequency vectors. A frequency vector $\tau=\left(\tau_{i}\right)_{i \in[1 . . n]}$ is a vector whose components represent a probability, i.e., $\tau_{i} \in[0,1]$, $i \in[1 . . n]$. A probability distribution on $\{0,1\}^{\mathrm{n}}$ is associated to a frequency vector $\tau$ in the following way: an individual $x \in\{0,1\}^{\mathrm{n}}$ follows this probability distribution if and only if each component $x_{i}$ of $x$ independently follows the Bernoulli distribution of parameter $\tau_{i}$.

The sig-cGA utilizes frequency vectors whose components take values in $\left\{\frac{1}{n}, \frac{1}{2}, 1-\frac{1}{n}\right\}$ to represent a probability distribution on $\{0,1\}^{\mathrm{n}}$ in the above way. For each bit position $i \in[1 . . n]$, the sig-cGA keeps a history $H_{i} \in\{0,1\}^{*}$ for significance inferring that will be explained in detail in the following. In iteration $t$, two individuals, $x$ and $y$, are independently sampled from the probability distribution associated with $\tau^{(t)}$. They are then evaluated under $f$, the one with better fitness is called the winner and is denoted by $z$. In the case of a tie the winner is chosen at random. Now for each $i \in[1 . . n]$, the value of $z_{i}$ is added to the history $H_{i}$. If a statistical significance of 1 ( 0 resp.) is detected in $H_{i}$, then $\tau_{i}^{(t+1)}$ is set to $1-\frac{1}{n}\left(\frac{1}{n}\right.$ resp. $)$ and the history $H_{i}$ is emptied. To be more precise, we define in the following the function $\operatorname{sig}_{e}$ taking values in \{UP, Down, STAY\} and we say that a significance of 1 ( 0 resp.) is detected when $\operatorname{sig}_{e}\left(\tau_{i}^{(t)}, H_{i}\right)=$ UP (DOWN resp.).

For all $\varepsilon, \mu \in \mathbb{R}^{+}$, let $s(\varepsilon, \mu)=\varepsilon \max \{\sqrt{\mu \log n}, \log n\}$. For all $H \in\{0,1\}^{*}$, let $H[k]$ be the string of its last $k$ bits and let $\|H[k]\|_{0}\left(\|H[k]\|_{1}\right.$ resp.) denote the number of zeros (resp. ones) in $H$. Then for all $p \in\left\{\frac{1}{n}, \frac{1}{2}, 1-\frac{1}{n}\right\}$ and $H \in\{0,1\}^{*}$, $\operatorname{sig}_{\varepsilon}(p, H)$ is defined by

$$
\operatorname{sig}_{\varepsilon}(p, H)= \begin{cases}\text { UP } & \text { if } p \in\left\{\frac{1}{n}, \frac{1}{2}\right\} \wedge \exists m \in \mathbb{N}: \\ & \left\|H\left[2^{m}\right]\right\|_{1} \geq 2^{m} p+s\left(\varepsilon, 2^{m} p\right) \\ \text { Down } & \text { if } p \in\left\{\frac{1}{2}, 1-\frac{1}{n}\right\} \wedge \exists m \in \mathbb{N}: \\ & \left\|H\left[2^{m}\right]\right\|_{0} \geq 2^{m}(1-p)+s\left(\varepsilon, 2^{m}(1-p)\right) \\ \text { STAY } & \text { else. }\end{cases}
$$

Algorithm 6: The sig-cGA with parameter $\varepsilon$ and significance function $\operatorname{sig}_{\varepsilon}$ optimizing $f:\{0,1\}^{\mathrm{n}} \rightarrow \mathbb{R}$. By $\circ$ we denote the concatenation of two strings (here only used for appending a single letter to a string).

```
\(t \leftarrow 0\);
for \(i \in\{1 . . n\}\) do \(\tau_{i}^{(0)} \leftarrow \frac{1}{2}\) and \(H_{i} \leftarrow \emptyset\);
repeat
    \(x, y \leftarrow\) offspring sampled with respect to \(\tau^{(t)}\);
    \(z \leftarrow\) winner of \(x\) and \(y\) with respect to \(f\), chosen at random in case of a tie;
    for \(i \in\{1 . . n\}\) do
        \(H_{i} \leftarrow H_{i} \circ z_{i}\)
        if \(\operatorname{sig}_{\varepsilon}\left(\tau_{i}^{(t)}, H_{i}\right)=\mathrm{UP}\) then \(\tau_{i}^{(t+1)} \leftarrow 1-\frac{1}{n}\);
        else if \(\operatorname{sig}_{\varepsilon}\left(\tau_{i}^{(t)}, H_{i}\right)=\operatorname{Down}\) then \(\tau_{i}^{(t+1)} \leftarrow \frac{1}{n}\);
        else \(\tau_{i}^{(t+1)} \leftarrow \tau_{i}^{(t)}\);
        if \(\tau_{i}^{(t+1)} \neq \tau_{i}^{(t)}\) then \(H_{i} \leftarrow \emptyset\);
    \(t \leftarrow t+1\);
```

13 until termination criterion met;

The following lemma (Lemma 2 in [21]) shows that the sig-cGA, with probability at least $1-n^{-\varepsilon / 3} \log _{2} k$, does not detect a significance at a position with no bias in selection, that is, with a high probability it does not detect a false significance.

Lemma 21 (Lemma 2 in [21]). Consider the sig-cGA with $\varepsilon \geq 1$. Let $i \in\{1 . . n\}$ be a bit position and suppose that the distribution of 1 s in $H_{i}$ follows a binomial law with $k$ tries and success probability $\tau_{i}$. Then

$$
\operatorname{Pr}\left[\operatorname{sig}_{\varepsilon}\left(\tau_{i}^{(\mathrm{f})}, H_{i}\right) \neq \operatorname{STAV}\right] \leq n^{-\varepsilon / 3} \log _{2} k
$$

that is, $\tau_{i}$ changes with a probability of at most $n^{-\varepsilon / 3} \log _{2} k$.
The preceding lemma readily implies the following corollary.
Corollary 22. Consider the sig-cGA with $\varepsilon \geq 1$. Let $i \in[1 . . n]$ be a bit position and suppose that the distribution of 1 s in $H_{i}$ follows a binomial law with $k$ tries and a success probability of at least $\tau_{i}$. Then $\tau_{i}$ decreases in an iteration with a probability of at most $n^{-\varepsilon / 3} \log _{2} k$.

# 4.2.1. The Sig-cGA solves the DLB problem in $O(n \log n)$ time 

Now we show that with probability at least $1-O\left(n^{2-\varepsilon / 3} \log ^{2} n\right)$, the sig-cGA samples the optimum of the DLB function within $O(n \log n)$ fitness evaluations (Theorem 26). First we show that when no $\tau_{i}$ is set to $\frac{1}{n}$, the probability of adding a 1 to the history $H_{i}$ in an iteration is at least $\tau_{i}$, which will allow us to use Corollary 22.

Lemma 23. Let $m \in\left[1 . . \frac{n}{2}-1\right]$. Let $\left(\tau_{i}\right)_{i \in[1 . . n]} \in\left\{\frac{1}{n}, \frac{1}{2}, 1-\frac{1}{n}\right\}^{n}$ be a frequency vector. Consider one iteration of the sig-cGA optimizing the DLB function. Let $x$ and $y$ be the two individuals sampled according to $\left(\tau_{i}\right)_{i \in[1 . . n]}$. Then, conditioning on $\{\min \{ \mathrm{DLB}(x), \operatorname{DLB}(y)\} \geq$ $2 m\}$, a 1 is saved in $\mathrm{H}_{2 m+1}$ with probability

$$
\begin{aligned}
& p\left(\tau_{2 m+1}, \tau_{2 m+2}\right) \\
& \quad:=\tau_{2 m+1}\left(-\tau_{2 m+2}^{2}+3 \tau_{2 m+2}+\left(\tau_{2 m+2}^{2}-3 \tau_{2 m+2}+1\right) \tau_{2 m+1}\right)
\end{aligned}
$$

If $\tau_{2 m+1}, \tau_{2 m+2} \in\left\{\frac{1}{2}, 1-\frac{1}{n}\right\}$, then the above term is bounded from below by $\tau_{2 m+1}$. If further $\tau_{2 m+1}=\frac{1}{2}$ and $\tau_{2 m+2} \in\left\{\frac{1}{2}, 1-\frac{1}{n}\right\}$, then the above term is bounded from below by $\frac{n}{10}$.

Proof. Under the condition $\{\min \{D L B(x), \operatorname{DLB}(y)\} \geq 2 m\}$, the bit value saved in $H_{2 m+1}$ is completely determined by the bits $x_{2 m+1}, x_{2 m+2}, y_{2 m+1}$, and $y_{2 m+2}$. In the following we assume $m=0$ for the ease of presentation, but the general result can be obtained in exactly the same way. We calculate

$$
\begin{aligned}
& \operatorname{Pr}\left[1 \text { is saved in } H_{1}\right] \\
& =\operatorname{Pr}\left[x_{1}=x_{2}=1\right] \\
& \quad+\operatorname{Pr}\left[x_{1}=1, x_{2}=0\right]\left(\operatorname{Pr}\left[y_{1}=1\right]+\frac{1}{2} \operatorname{Pr}\left[y_{1}=0, y_{2}=1\right]\right) \\
& \quad+\operatorname{Pr}\left[x_{1}=0, x_{2}=1\right]\left(\operatorname{Pr}\left[y_{1}=y_{2}=1\right]+\frac{1}{2} \operatorname{Pr}\left[y_{1}=1, y_{2}=0\right]\right) \\
& \quad+\operatorname{Pr}\left[x_{1}=0, x_{2}=0\right] \operatorname{Pr}\left[y_{1}=y_{2}=1\right] \\
& =\tau_{1} \tau_{2}+\tau_{1}\left(1-\tau_{2}\right)\left(\tau_{1}+\frac{1}{2}\left(1-\tau_{1}\right) \tau_{2}\right) \\
& \quad+\left(1-\tau_{1}\right) \tau_{2}\left(\tau_{1} \tau_{2}+\frac{1}{2} \tau_{1}\left(1-\tau_{2}\right)\right) \\
& \quad+\left(1-\tau_{1}\right)\left(1-\tau_{2}\right) \tau_{1} \tau_{2} \\
& =\tau_{1}\left(-\tau_{2}^{2}+3 \tau_{2}+\left(\tau_{2}^{2}-3 \tau_{2}+1\right) \tau_{1}\right)
\end{aligned}
$$

Now if $\tau_{1}, \tau_{2} \in\left\{\frac{1}{2}, 1-\frac{1}{n}\right\}$, then

$$
-\tau_{2}^{2}+3 \tau_{2}=-\left(\tau_{2}-\frac{3}{2}\right)^{2}+\frac{9}{4} \geq-\left(\frac{1}{2}-\frac{3}{2}\right)^{2}+\frac{9}{4}=\frac{5}{4}
$$

Thus we have $\tau_{2}^{2}-3 \tau_{2}+1 \leq-\frac{1}{4}<0$ and

$$
\begin{aligned}
\frac{p\left(\tau_{1}, \tau_{2}\right)}{\tau_{1}} & =-\tau_{2}^{2}+3 \tau_{2}+\left(\tau_{2}^{2}-3 \tau_{2}+1\right) \tau_{1} \\
& \geq-\tau_{2}^{2}+3 \tau_{2}+\left(\tau_{2}^{2}-3 \tau_{2}+1\right)\left(1-\frac{1}{n}\right) \\
& =-\frac{1}{n}\left(\tau_{2}^{2}-3 \tau_{2}\right)+1-\frac{1}{n} \\
& \geq-\frac{5}{4 n}+1-\frac{1}{n}=1+\frac{1}{4 n}>1
\end{aligned}
$$

Supposing further that $\tau_{1}=\frac{1}{2}$, we have

$$
\frac{p\left(\tau_{1}, \tau_{2}\right)}{\tau_{1}}=\frac{1}{2}\left(-\tau_{2}^{2}+3 \tau_{2}+1\right) \geq \frac{1}{2}\left(\frac{5}{4}+1\right)=\frac{9}{8}
$$

Corollary 24. If in an iteration of the sig-cGA, the frequency vector is in $\left\{\frac{1}{2}, 1-\frac{1}{n}\right\}^{n}$, then for any $i \in[1 . . n]$, a 1 is saved in $H_{i}$ with probability at least $\tau_{i}$.

Proof. Let $x$ and $y$ be the two individuals sampled in this iteration. Let $i=2 m+1$ for some $m \in\left[1 . . \frac{n}{2}-1\right]$. Then the preceding lemma shows that conditioning on $\{\min \{D L B(x), \operatorname{DLB}(y)\} \geq 2 m\}$, a 1 is saved in $H_{2 m+1}$ with probability at least $\tau_{2 m+1}$. Under the condition $\{\min \{D L B(x), D L B(y)\}<2 m\}$, the probability that a 1 is saved in $H_{2 m+1}$ is equal to the probability $\tau_{2 m+1}$ that a 1 is sampled in this position, because bit $2 m+1$ is not relevant for the selection. Combining the two cases, the claim follows for $i=2 m+1$. The symmetry between $i=2 m+1$ and $i=2 m+2$ concludes the proof.

Lemma 25. Consider the sig-cGA with $\varepsilon>3$. The probability that during the first $k$ iterations at least one frequency decreases is at most $k n^{1-\varepsilon / 3} \log _{2} k$.

Proof. Consider the event that in the first $t$ iterations, no frequency has ever been decreased. Denote its probability by $p^{(t)}$.
Conditioning on this event, Corollary 24 can be applied to verify the hypothesis of Corollary 22, which implies that the conditional probability that no frequency decreases in the $(t+1)$-th iteration is at least $1-n^{1-\varepsilon / 3} \log _{2} k$. Therefore $p^{(t+1)} \geq p^{(t)}\left(1-n^{1-\varepsilon / 3} \log _{2} k\right)$. By induction, $p^{(k)} \geq\left(1-n^{1-\varepsilon / 3} \log _{2} k\right)^{k} \geq 1-k n^{1-\varepsilon / 3} \log _{2} k$.

Theorem 26. The runtime of the sig-cGA with $\varepsilon>6$ on DLB is $O(n \log n)$ with probability at least $1-O\left(n^{2-\varepsilon / 3} \log ^{2} n\right)$.

Proof. By taking $k=O(n \log n)$ in Lemma 25, we obtain that with probability at least $1-O\left(n^{2-\varepsilon / 3} \log ^{2} n\right)$, no frequency decreases in the first $O(n \log n)$ iterations. We condition on this event in what follows.

During the runtime of the sig-cGA, a block $\left(x_{2 m+1}, x_{2 m+2}\right)$ is called critical if $m$ is such that $\tau_{i}=1-\frac{1}{n}$ for all $i \in[1 . .2 m]$, and that $\tau_{2 m+1}=\frac{1}{2}$ or $\tau_{2 m+2}=\frac{1}{2}$. Suppose that such a critical block is created with $\tau_{2 m+1}=\frac{1}{2}$. We prove that the history

of position $2 m+1$ saves 1 s significantly more often than 0 s and hence the frequency $\tau_{2 m+1}$ is set to $1-\frac{1}{n}$ after $O(\log n)$ iterations.

Let $G$ denote the event that we save a 1 in $H_{2 m+1}$ in one iteration. We now calculate a lower bound of $G$ under the condition that no frequency is decreased within first $O(n \log n)$ iterations.

Let $A$ denote the event that at least one of the two individuals sampled in an iteration has a DLB value smaller than $2 m$. When $A$ happens, a 1 is saved in $H_{2 m+1}$ with probability $\tau_{2 m+1}=\frac{1}{2}$. If $A$ does not happen, then the probability of saving a 1 to $H_{2 m+1}$ is equal to $p\left(\tau_{2 m+1}, \tau_{2 m+2}\right)$ defined in (12). Hence we can decompose $\operatorname{Pr}[G]$ as

$$
\operatorname{Pr}[G]=\operatorname{Pr}[A] \tau_{2 m+1}+\operatorname{Pr}[\bar{A}] p\left(\tau_{2 m+1}, \tau_{2 m+2}\right)
$$

Since $\bar{A}$ is equivalent to both individuals have 1 s in the first $2 m$ bit positions, we have $\operatorname{Pr}[\bar{A}]=\left(\left(1-\frac{1}{n}\right)^{2 m}\right)^{2} \geq$ $\left(\left(1-\frac{1}{n}\right)^{n-2}\right)^{2} \geq\left(e^{-1}\right)^{2}=e^{-2}$. With Lemma 23, this implies

$$
\begin{aligned}
\operatorname{Pr}[G] & \geq(1-\operatorname{Pr}[\bar{A}]) \tau_{2 m+1}+\operatorname{Pr}[\bar{A}] \frac{n}{8} \tau_{2 m+1} \\
& \geq\left(1+\frac{1}{8} \operatorname{Pr}[\bar{A}]\right) \tau_{2 m+1}=\left(1+\frac{1}{8} e^{-2}\right) \tau_{2 m+1}
\end{aligned}
$$

since we assumed that $\tau_{2 m+1}=\frac{1}{2}$.
With this lower bound on $\operatorname{Pr}[G]$ we bound the probability that a significance of 1 s in $H_{2 m+1}$ is detected within $k=$ $O(\log n)$ iterations. To this end, we consider the process $X \sim \operatorname{Bin}\left(k,\left(1+e^{-2} / 8\right) \tau_{2 m+1}\right)$, which is stochastically dominated by the actual process of saving 1 s at position $H_{2 m+1}$. It follows from the definition that

$$
\begin{aligned}
& \operatorname{Pr}\left[X \leq k \tau_{2 m+1}+s\left(\varepsilon, k \tau_{2 m+1}\right)\right] \\
& \quad=\operatorname{Pr}\left[X \leq E[X]-\left(\frac{k}{8} e^{-2} \tau_{2 m+1}-s\left(\varepsilon, k \tau_{2 m+1}\right)\right)\right]
\end{aligned}
$$

For $k>64 e^{4} \varepsilon^{2} \tau_{2 m+1}^{-1} \log n=\Theta(\log n)$ we have $s\left(\varepsilon, k \tau_{2 m+1}\right)=\varepsilon \sqrt{k \tau_{2 m+1} \log n}$ and thus $\frac{k}{8} e^{-2} \tau_{2 m+1}-s\left(\varepsilon, k \tau_{2 m+1}\right)>0$. Let $c:=64 e^{4} \varepsilon^{2} \tau_{2 m+1}^{-1}$ and consider $k>4 c \log n$ iterations. We have

$$
s\left(\varepsilon, k \tau_{2 m+1}\right)=\varepsilon \sqrt{k \tau_{2 m+1} \log n}<\varepsilon k \sqrt{\frac{\tau_{2 m+1}}{4 c}}=\frac{\tau_{2 m+1} k}{16 e^{2}}
$$

which implies

$$
\frac{k}{8} e^{-2} \tau_{2 m+1}-s\left(\varepsilon, k \tau_{2 m+1}\right)>\frac{\tau_{2 m+1} k}{16 e^{2}}=: \lambda
$$

and hence

$$
\operatorname{Pr}\left[X \leq E[X]-\left(\frac{k}{8} e^{-2} \tau_{2 m+1}-s\left(\varepsilon, k \tau_{2 m+1}\right)\right)\right] \leq \operatorname{Pr}[X \leq E[X]-\lambda]
$$

We use a Chernoff inequality to calculate an upper bound for this probability. By definition

$$
\operatorname{Var}[X]=k\left(1+e^{-2} / 8\right) \tau_{2 m+1}\left(1-\left(1+e^{-2} / 8\right) \tau_{2 m+1}\right) \geq \lambda
$$

It is straightforward that

$$
\frac{\lambda^{2}}{\operatorname{Var}[X]}>\frac{\lambda^{2}}{k \tau_{2 m+1}}=\frac{k \tau_{2 m+1}}{256 e^{4}}>\frac{c \tau_{2 m+1} \log n}{64 e^{4}}=\varepsilon^{2} \log n
$$

Now the Chernoff inequality (Theorem 4) implies

$$
\operatorname{Pr}[X \leq E[X]-\lambda] \leq \exp \left(\frac{-\lambda^{2}}{3 \operatorname{Var}[X]}\right)<\exp \left(-\frac{\varepsilon^{2}}{3} \log n\right)=n^{-\frac{\varepsilon^{2}}{3}}
$$

We have thus proven that with probability at most $n^{-\frac{\varepsilon^{2}}{3}}, \tau_{2 m+1}$ is not set to $1-\frac{1}{n}$ after $O(k)=O(4 c \log n)=O(\log n)$ iterations. Due to the symmetry between positions $2 m+1$ and $2 m+2$, the same holds true for bit positions $2 m+2$, $m \in\left[1 . . \frac{n}{2}-1\right]$. Hence with probability at most $n^{1-\frac{\varepsilon^{2}}{3}}$, for some $i \in[1 . . n], \tau_{i}$ is not set to $1-\frac{1}{n}$ within the first $O(n \log n)$ iterations, that is, with probability at least $1-n^{1-\frac{\varepsilon^{2}}{3}}$, every $\tau_{i}, i \in[1 . . n]$, is set to $1-\frac{1}{n}$ within the first $O(n k)=O(n \log n)$ iterations.

Once this is achieved, the probability to sample the optimum $\mathbf{1}=(1, \ldots, 1)$ from $\left(\tau_{i}\right)_{i \in[1 . . n]}$ is equal to $\left(1-\frac{1}{n}\right)^{n}>\frac{1}{2 \varepsilon}$. Let $\varepsilon^{\prime}>\frac{\varepsilon}{3}-2$ be a constant. Since we condition on no frequency dropping, the sig-cGA samples $\mathbf{1}$ at least once within $\varepsilon^{\prime} \frac{1}{2}\left(\log \left(\frac{2 \varepsilon}{2 \varepsilon-1}\right)\right)^{-1} \log n=O(\log n)$ iterations with a probability of at least

$$
1-\left(1-\frac{1}{2 \varepsilon}\right)^{\varepsilon^{\prime}\left(\log \left(\frac{2 \varepsilon}{2 \varepsilon-1}\right)\right)^{-1} \log n}=1-n^{-\varepsilon^{\prime}}
$$

Recall that no frequency decreases within the first $O(n \log n)$ iterations with probability at least $1-O\left(n^{2-\varepsilon / 3} \log ^{2} n\right)$. Combining the preceding results, we have proven that the optimum is sampled within $O(n \log n)$ iterations with probability at least

$$
\left(1-O\left(n^{2-\varepsilon / 3} \log ^{2} n\right)\right)\left(1-n^{1-\frac{\varepsilon^{2}}{3}}\right)\left(1-n^{-\varepsilon^{\prime}}\right)=1-O\left(n^{2-\varepsilon / 3} \log ^{2} n\right)
$$

because of the definition of $\varepsilon^{\prime}$ and the inequality $2-\frac{\varepsilon}{3}>1-\frac{\varepsilon^{2}}{3}$.
A reviewer of this work noted that also the significant bit voting algorithm proposed in [112] could have an $O(n \log n)$ runtime on the DLB problem. This algorithm, with population size $\mu \in \mathbb{N}$, works as follows. Initially, all bits are undecided. In each of the $n$ iterations, exactly for one bit a value is decided. This is done via the following procedure. (i) Independently, $\mu$ individuals are sampled. The undecided bits are sampled uniformly at random, the decided ones deterministically take the decided value. (ii) From this sample, $\mu / 3$ individuals with highest fitness are selected. (iii) Among these, an undecided bit position $i \in[1 . . n]$ is selected in which the number of zeros and ones differs maximally. (iv) The $i$-th bit is declared decided, and this is with the more frequently occurring bit value in the selected subpopulation.

It is fairly easy to prove that when the population size $\mu$ is at least logarithmic (with sufficiently large implicit constant), then with high probability in a run of this algorithm on DLB the bits are decided on order of increasing block index, and all decided bits receive the value one. This shows that this algorithm with high probability optimizes DLB in time $O(n \log n)$.

For two reasons we find the sig-cGA a more convincing example of a natural randomized search heuristic. On the one hand, the sig-cGA surely converges, that is, eventually outputs the right solution. On the other hand, more critically, we feel that the significant bit voting algorithm is overfitted to problems that are easily optimized by sequentially fixing one bit value. In fact, we have strong doubts that this algorithm with a logarithmic population size can optimize the OneMax benchmark with a probability higher than $o(1)$, and in fact, higher than $1 / p$ where $p$ is any polynomial in $n$. The reason is that in the first iteration, the selected individuals all have at most $\frac{n}{2}+O(\sqrt{n \log n})$ one-bits. Hence even in the selected population, a fixed bit is one with probability $\frac{1}{2}+O\left(n^{-1 / 2} \sqrt{\log n}\right)$ only. Hence with a logarithmic population size $\mu$, we expect to have both $\mu / 6 \pm o(1)$ zeroes and ones in a fixed bit position (in the selected subpopulation of size $\mu / 3$ ). This gives little hope that the small advantage of the value one is safely detected. We sketched this argument for the first iteration, but the same argument applies to all other iterations. For this reason, it appears very likely that at least one bit-value is set wrongly in the first $n / 2$ iterations. We note that this is not a formal proof since we have not taken into account the (light) stochastic dependencies among the bit positions. We are nevertheless pessimistic that this algorithm has a good performance on problems like OneMax. We note the only mathematical runtime analysis so far for this algorithm considers exclusively the LEAdingONES problem.

# 5. Experiments 

To see how the algorithms compare on concrete problem sizes, we ran the $(1+1)$ EA, UMDA, Metropolis algorithm, and sig-cGA on the DLB function for $n=40,80, \ldots, 200$. We used the standard mutation rate $p=1 / n$ for the $(1+1)$ EA, the population sizes $\mu=3 n \ln n$ and $\lambda=12 \mu$ for the UMDA (as in [19]), and the temperature parameter $\alpha=3$ (greater than $\sqrt{2}+1$ as suggested from Theorem 14) for the Metropolis algorithm. For the sig-cGA, we took $\epsilon=2.5$ since we observed that this was enough to prevent frequencies from moving to an unwanted value, which only happened one time for $n=40$. Being still very slow, for this algorithm we could only perform 10 runs for problem sizes 40, 80, 120, and 160 (Fig. 1).

Our experiments clearly show an excellent performance of the Metropolis algorithm, which was suggested as an interesting algorithm by our theoretical analysis. The two EDAs, however, perform worse than what the asymptotic results suggest. Such a discrepancy between theoretical predictions and experimental results, stemming from the details hidden in the asymptotic notation, has been observed before and is what triggered the research area of algorithm engineering $[113]$.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The median number of fitness evaluations (with the first and third quartiles) of $(1+1)$ EA, UMDA, Metropolis algorithm, and the sig-cGA on DLB with $n \in(40,80,120,160,200)$ in 20 independent runs ( 10 runs for $n \in(40,80,120,160)$ for the sig-cGA). (For interpretation of the colors in the figure(s), the reader is referred to the web version of this article.)

## 6. Conclusion and outlook

To help choosing an efficient randomized search heuristic when faced with a novel problem, we proposed a theoryguided approach based on black-box complexity arguments and applied it to the recently proposed DLB function. Our approach suggested the Metropolis algorithm, for which little theoretical support before existed. Both a mathematical runtime analysis and our experiments proved it to be significantly superior to all previously analyzed algorithms for the DLB problem.

We believe that our approach, in principle and in a less rigorous way, can also be followed by researchers and practitioners outside the theory community. Our basic approach of (i) trying to understand how the theoretically best-possible algorithm for a given problem could look like and then (ii) using this artificial and problem-specific algorithm as indicator for promising established search heuristics, can also be followed by experimental methods and by non-rigorous intuitive considerations.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This work was supported by National Natural Science Foundation of China (Grant No. 62306086), Science, Technology and Innovation Commission of Shenzhen Municipality (Grant No. GXWD20220818191018001), Guangdong Basic and Applied Basic Research Foundation (Grant No. 2019A1515110177).

This work was also supported by a public grant as part of the Investissement d'avenir project, reference ANR-11-LABX-0056-LMH, Agence Nationale de la Recherche, LabEx LMH.
