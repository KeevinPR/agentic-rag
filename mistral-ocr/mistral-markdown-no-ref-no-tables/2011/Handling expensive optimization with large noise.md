# Handling Expensive Optimization with Large Noise 

Rémi Coulom<br>Grappa, SequeL, Université Charles-de-Gaulle, Lille, France Remi.Coulom@univ- lille3.fr<br>Nataliya Sokolovska TAO-INRIA,LRI, UMR 8623 CNRS - Université Paris-Sud, Orsay, France nataliya@lri.fr

## ABSTRACT

We present lower and upper bounds on runtimes for expensive noisy optimization problems. Runtimes are expressed in terms of number of fitness evaluations. Fitnesses considered are monotonic transformations of the sphere function. The analysis focuses on the common case of fitness functions quadratic in the distance to the optimum in the neighbourhood of this optimum-it is nonetheless also valid for any monotonic polynomial of degree $p>2$. Upper bounds are derived via a bandit-based estimation of distribution algorithm that relies on Bernstein races called R-EDA. It is an evolutionary algorithm in the sense that it is based on selection, random mutations, with a distribution (updated at each iteration) for generating new individuals. It is known that the algorithm is consistent (i.e. it converges to the optimum asymptotically in the number of examples) even in some non-differentiable cases. Here we show that: (i) if the variance of the noise decreases to 0 around the optimum, it can perform well for quadratic transformations of the norm to the optimum, (ii) otherwise, a convergence rate is slower than the one exhibited empirically by an algorithm called Quadratic Logistic Regression (QLR) based on surrogate models - although QLR requires a probabilistic prior on the fitness class.

## Categories and Subject Descriptors

F.m [Theory of Computation]: Miscellaneous; I.2.8 [Artificial Intelligence]: Problem Solving, Search

## General Terms

Theory

[^0]PRilipe Rolet<br>TAO-INRIA,LRI, UMR 8623<br>CNRS - Université Paris-Sud, Orsay, France rolet@lri.fr<br>Olivier Teytaud<br>TAO-INRIA,LRI, UMR 8623<br>CNRS - Université Paris-Sud, Orsay, France<br>teytaud@lri.fr

## Keywords

Noisy optimization, Bernstein races, Runtime analysis.

## 1. INTRODUCTION

" Noisy optimization" means that the result of a fitness evaluation at a given point is a random variable, whose probability distribution depends only on the location of the point-this noise model will be detailed in Section 2, as well as the class of fitnesses that we address. Expensive means that each fitness call is considered costly: for example, evaluating the fitness of an individual might involve the building and testing of a prototype, or hours of simulations. Therefore, an expensive optimization algorithm's performance is measured by the number of fitness calls required to find the optimum with a given precision, rather than considering the computational time required by the algorithm to function.

## State of the art

Using evolutionary algorithms and Estimation of Distribution algorithms (EDAs) to deal with noisy fitnesses is a topic that has been substantially discussed in the literature. Notably, many question the idea that repeatedly evaluating the same points in order to average values and decrease noise variance is effective, as compared to, for instance, simply increasing the population size $[13,7,14,1,3]$. A brief survey can be found in [24], where it has been shown that averaging can be efficient when used in the framework of multi-armed bandits, a statistical approach to model sequential dependencies (following ideas of [18]), and races[22]. Specifically, it is proved that an EDA using Bernstein races to choose the number of evaluations of a given point reaches an optimal convergence rate for certain noise models (see, for instance [25]).

When dealing with noisy optimization, it is important to distinguish cases in which the variance of the noise decreases to zero near the optimum-which we will refer to as the small noise assumption hereafter - and cases where it does not-large noise assumption (see Section 2 for more details on noisy settings). The small noise case, which is much easier and therefore more widely analyzed, has been tackled in [20] for a quite restricted noise model. [2] have then shown that in case of large noise, all usual step-size adaptation rules diverge or stop converging: the usual behavior of


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. To copy otherwise, to republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee.
    FOGA'11, January 5-9, 2011, A-6867 Schwarzenberg, Austria. Copyright 2011 ACM 978-1-4503-0633-1/11/01 ...\$10.00.

evolutionary algorithms for models with large noise is that they stop converging as they get too close to the optimum, and then keep a residual error, with a step-size which does not decrease to zero. The residual error remains large even w.r.t. computers' numerical accuracy of zero.

In [24] and [26] cases of large noise have been tackled, but only for fitness functions of the form $x \mapsto \lambda\left\|x-x^{*}\right\|+c$ excluding the quadratic (or higher-order polynomial) fitness functions. Furthermore, algorithms for noise handling such as Uncertainty Handling for Covariance Matrix Adaptation (UH-CMA), empirically quite efficient for small noise, are unfortunately not yet stable enough to deal with large noise cases. For the Scaled-Translated sphere (STS) model presented below, UH-CMA does not converge. Consistently with these results, [28] has shown that fast convergence involves a number of evaluations running to infinity with the number of iterations. This was further developed in [24, 26] with both lower bounds and algorithms reaching the bound in many cases. However, the natural case of fitnesses that are quadratic in the distance to the optimum was not covered. In the following, we show that:

- a version of Estimation of Distribution Algorithm dedicated to noisy optimization has been proposed in [26]; this version, termed R-EDA, is recalled in Algorithm 3, is based on a Race and has good theoretical guarantees, for both small noise and large noise scenarios;
- our R-EDA algorithm is not supposed to be a practical algorithm; we use it to derive complexity upper bounds, and to show that these complexity upper bounds can be reached by evolutionary algorithms based on races (races are discussed in section 2);
- R-EDA is empirically outperformed in large noise cases by surrogate models if $p=2$ (an example of such a surrogate model is Quadratic Logistic Regression (QLR) which fits a quadratic model using a Bayesian prior);
- R-EDA also converges at a controlled rate for polynomial functions of the distance to the optimum.

Note that R-EDA has first been used in [26], and has not been modified for this work. All positive properties of R-EDA are preserved, in particular its consistency in many difficult cases, e.g. for fitnesses $f(x)=c+\Theta\left(\left\|x-x^{*}\right\|\right)$, i.e. for functions that behave similarly to a translated sphere function in the neighborhood of the optimum $x^{*}$.

## 2. FRAMEWORK

The optimization framework is described in Algorithm 1. This is a black-box optimization framework: the algorithm can request the fitness values at any chosen point, and no other information on the fitness function is available. We consider a fitness function $f$ parameterized by the (unknown) location of its optimum, $t$. The noise is accounted for by a random variable $\theta \in[0,1]^{3}$; each coordinate $\theta_{i}$ for $i \in\{1,2, \ldots\}$ is uniformly distributed in $[0,1]$. The goal is to find the optimum $t$ of $f(., t)$, by observing noisy measurement of $f$ at $x_{i}$. Measurements are random variables $F_{t}\left(x_{i}\right)$ on the interval $[0,1]$. They satisfy $\mathbb{E}\left[F_{t}\left(x_{i}\right)\right]=f\left(x_{i}, t\right)$. For the proof of the lower bound, the law of random variable $F_{t}\left(x_{i}\right)$ is Bernouilli, with parameter $f\left(x_{i}, t\right)$ as shown in Algorithm 1. This fits applications based on highly noisy optimization, such as games: let $x$ be a parameter of a game

Algorithm 1 Noisy optimization framework. Opt is an optimization heuristic: it takes as input a sequence of visited points and their binary, noisy fitness values, and outputs a candidate optimum, that is a points of the domain such that $f(x, t)$ is as small as possible. This point is the point whose fitness is asked next. Opt is successful on target $f$ parameterized by $t$ and random noise $\theta$ if $\operatorname{Loss}(t, \theta, O p t)$ is small.

Parameters: $N$, number of fitness evaluations; $t$, unknown element of $X$.
$\theta$ : random state of the nature $\in[0,1]^{3}$; each coordinate $\theta_{i}$ for $i \in\{1,2, \ldots\}$ is uniformly distributed in $[0,1]$.
for $n \in[[0, N-1]]$ do
$x_{n+1}^{t, \theta}=\operatorname{Opt}\left(x_{1}^{t, \theta}, \ldots, x_{n}^{t, \theta}, y_{1}^{t, \theta}, \ldots, y_{n}^{t, \theta}\right)$
$/ /$ Return noisy fitness $\sim \mathcal{B}\left(f\left(x_{n+1}^{t, \theta}, t\right)\right)$
$y_{n+1}^{t, \theta}=\left(f\left(x_{n+1}^{t, \theta}, t\right)<\theta_{n+1}\right) ? 1: 0$
end for
$\operatorname{Loss}(t, \theta, O p t)=d\left(t, x_{N}^{t, \theta}\right)$
strategy, that we wish to set at its best value; a noisy observation is a game against a baseline, resulting either in a win or in a loss; the aim is to find the value of $x$ maximizing the probability of winning. Usual viability problems or binary control problems tackled by direct policy search also involve this kind of optimization.

We are interested in the number of requests needed for an optimization algorithm to find optimum $t$ with precision $\epsilon$ and confidence $1-\delta ; \epsilon=\left\|x_{n}-t\right\|$ is the Euclidian distance between $t$ and the output $x_{n}$ of the algorithm after $n$ fitness calls. The paper focuses on fitnesses of the form $(x, t) \mapsto c+\lambda\|x-t\|^{p}$, referred to as the Scaled-Translated sphere (STS) model. It is more general than the STS model of [26] which addresses only $p=1$. In the following, $t$ is not handled stochastically, i.e. the lower bounds are not computed in expectation w.r.t. all the possible fitness functions yielded by different values of $t$. Rather, we will consider the worst case on $t$. Therefore the only random variable in this framework is $\theta$, accounting for noise in fitness measurements, and all probability / expectation operators are w.r.t. $\theta$. For simplicity, we considered only deterministic optimization algorithms; the extension to stochastic algorithms is straightforward by including a random seed of the algorithm in $\theta$.

In the following, $\hat{O}$ means that logarithmic factors in $\epsilon$ are neglected. In all the paper, $[[a, b]]=\{a, a+1, a+2, \ldots, b\}$.

## Races

The algorithm used to prove upper bounds on convergence rates is based on Bernstein confidence bounds. It is a variation of the well-known Hoeffding bounds [19] (aimed at quantifying the discrepancy between an empirical mean and an expectation for bounded random variables), which takes variances into account $[9,5,6]$. It is therefore tighter in some settings. A detailed survey of Hoeffding, Chernoff and Bernstein bounds is beyond the scope of this paper; we will only present the Bernstein bound, within its application to races. A race between two or more random variables aims at distinguishing with high confidence random variables with better expectation from those with worse expectation. Algorithm 2 is a Bernstein race applied to distinct points $x_{i}$ of a domain $X$-the 3 random variables are $F_{t}\left(x_{i}\right)$, the goal

is to find a good point and a bad point such that we are confident that the good one is closer to the optimum than the bad one.

It is crucial in this situation to ensure that there exist $i, j$ such that $f\left(x_{i}, t\right) \neq f\left(x_{j}, t\right)$, otherwise the race will last very long, and the output will be meaningless. At the end of the race, $3 T$ evaluations have been performed, therefore $T$ is called the halting time. Intuitively, the closer the points $x_{i}$ are in terms of fitness value, the larger $T$ will be. This is formalized below.

Algorithm 2 Bernstein race between 3 points. Eq. 1 is Bernstein's inequality to compute the precision for empirical estimates (see e.g. [11, p124]); $\hat{\sigma}_{i}$ is the empirical estimate of the standard deviation of point $x_{i}$ 's associated random variable $F_{t}\left(x_{i}\right)$ (it is 0 in the first iteration, which does not alter the algorithm's correctness); $\hat{f}(x)$ is the average of the fitness measurements at $x$.

```
Bernstein \(\left(x_{1}, x_{2}, x_{3}, \delta^{\prime}\right)\)
\(T=0\)
repeat
    \(T \leftarrow T+1\)
    Evaluate the fitness of points \(x_{1}, x_{2}, x_{3}\) once, i.e. evaluate the noisy fitness at each of these points.
    Evaluate the precision:
```

$$
\epsilon_{(T)}=3 \log \left(\frac{3 \pi^{2} T^{2}}{6 \delta^{\prime}}\right) / T+\max _{i} \hat{\sigma}_{i} \sqrt{2 \log \left(\frac{3 \pi^{2} T^{2}}{6 \delta^{\prime}}\right) / T}
$$

until Two points (good, bad) satisfy $\hat{f}(b a d)-\hat{f}(g o o d) \geq 2 \epsilon$ - return (good, bad)

Let us define $\Delta=\sup \left\{\mathbb{E} F_{t}\left(x_{1}\right), \mathbb{E} F_{t}\left(x_{2}\right), \mathbb{E} F_{t}\left(x_{3}\right)\right\}-$ $\inf \left\{\mathbb{E} F_{t}\left(x_{1}\right), \mathbb{E} F_{t}\left(x_{2}\right), \mathbb{E} F_{t}\left(x_{3}\right)\right\}$. It is known [23] that if $\Delta>0$ and if we consider a fixed number of arms ${ }^{1}$ (in the context of multi-armed bandits),

- with probability $1-\delta^{\prime}$, the Bernstein race is consistent: $\mathbb{E} F_{t}(\operatorname{good})<\mathbb{E} F_{t}(b a d)$
- the Bernstein race halts almost surely, and with probability at least $1-\delta^{\prime}$, the halting time $T$

$$
T \leq K \log \left(\frac{1}{\delta^{\prime} \Delta}\right) / \Delta^{2}
$$

where $K$ is a universal constant;

- if, in addition,

$$
\Delta \geq C \sup \left\{\mathbb{E} F_{t}\left(x_{1}\right), \mathbb{E} F_{t}\left(x_{2}\right), \mathbb{E} F_{t}\left(x_{3}\right)\right\}
$$

then the Bernstein race halts almost surely, and with probability at least $1-\delta^{\prime}$, the halting time $T$

$$
T \leq K^{\prime} \log \left(\frac{1}{\delta^{\prime} \Delta}\right) / \Delta
$$

where $K^{\prime}$ depends on $C$ only.
The interested reader is referred to [23] and other references for more information.

[^0]
## 3. LOWER BOUND

This section describes a general lower bound derived in [24], and concludes with the application of this bound to the scaled-translated sphere model.

Let us consider a domain $X$, a function $f: X \times X \rightarrow \mathbb{R}$, and define

$$
d\left(t_{1}, t_{2}\right)=\sup _{x \in X}\left|f\left(x, t_{1}\right)-f\left(x, t_{2}\right)\right|
$$

for $t_{1}$ and $t_{2}$ in $X . B(n, p)$ denotes a binomial random variable (sum of $n$ independent Bernoulli variables of parameter p).

Theorem 1. For any optimization algorithm Opt, let $N \in \mathbb{N}^{*}$ (a number of points visited), $\epsilon_{0}>0,0<\epsilon<\epsilon_{0}$, $D \in \mathbb{N}^{*}, \delta \in] 0,1[$. We assume:

- $H\left(\epsilon_{0}, D\right): \forall \epsilon_{1}<\epsilon_{0} \exists\left(t_{1}, \ldots, t_{D}\right) \in X^{D}, \forall(i, j) \in$ $[[1, D]]^{2}, i \neq j \Rightarrow d\left(t_{i}, t_{j}\right)=\epsilon_{1}$ (generalized dimension)
- $H_{P A C}(\epsilon, N, \delta): \forall t, P\left(d\left(x_{N}^{t, \theta}, t\right)<\epsilon / 2\right) \geq 1-\delta$.

Then, if $\delta<1 / 2 D$,

$$
P\left(B(N, \epsilon) \geq\left\lceil\log _{2}(D)\right\rceil\right) \geq 1-D \delta
$$

The lower bound is related to a topological property of space $X$ : a number $D$ is taken such that for any distance $\epsilon<\epsilon_{0}, D$ equidistant points of $X$ can be found (assumption $H\left(\epsilon_{0}, D\right)$ ). This is closely related to the dimension of $X$ : for instance, in $\mathbb{R}^{d}$, the maximum number of such equidistant points is $d+1$.

The theorem states that if an optimization algorithm is able to find the optimum at precision $\epsilon$ with probability $1-\delta$ in $N$ fitness calls (i.e. the algorithm satisfies assumption $H_{P A C}(\epsilon, N, \delta)$ ), then $N$ is necessarily large; the theorem explicitly gives a lower bound on $N$. Indeed, Eq. 5 implies a clearer expression of the lower bound (using Chebyshev inequality):

$$
N=\Omega\left(\log _{2}(D) / \epsilon\right)
$$

for fixed $D$, where $N$ is the number of iterations required to reach precision $\epsilon$ with confidence $1-\delta$ for $\delta<1 / 2 D$. The theorem holds for any monotonic transformation of the sphere function. However, the distance $d$ is not the same for different classes of fitnesses. As mentioned earlier, we are interested in the Scaled-Translated sphere model $((x, t) \mapsto$ $c+\lambda\|x-t\|^{p}$ with optimum $t$ ).

Corollary 2. Under the conditions of Theorem 1, for any optimization algorithm learning a fitness of the STS model, if $\epsilon_{N}$ is the quantile $1-\delta$ of the Euclidean distance to the optimum after $N$ fitness calls and if $p \geq 1$, then $\epsilon_{N}=\Omega(\log (D) / N)$.

As stated in [24], the lower bound for $p=1$ is straightforward, since in this case it is clear that $d\left(t_{1}, t_{2}\right)=\left\|t_{1}-t_{2}\right\|$. Moreover, in the general STS model, we can show that for any $p \geq 2, d\left(t_{1}, t_{2}\right)=\Theta\left(\left\|t_{2}-t_{1}\right\|\right)$, which validates the above corollary. The lower bound of the corollary is tight for $p=1$ (see [24]). We will see that it is also tight if $p=2$ for $c=0$-in this case, both QLR and R-EDA reach this dependency.


[^0]:    ${ }^{1}$ We here consider 3 arms only, but more general cases can be handled with a logarithmic dependency (see e.g. [23]).

## 4. UPPER BOUNDS

Upper bounds on the convergence rate for the STS model will now be presented, using R-EDA (Algorithm 3 along with a Bernstein race). In the model restricted to $p=1$, upper bounds for small noise (i.e. $c=0$ ) have been derived in [24], and upper bounds for large noise (i.e. $c>0$ ) have been derived in [26]. In both cases, the bounds match the lower bound. This is why we focus on $p \geq 2$, which includes the case $p=2$ that often appears in practice. In this section, the optimum will be referred to as $x^{*}$, and $f\left(x, x^{*}\right)$ will be noted $f(x)$ for short.
R-EDA is a $(3,3)$ evolution strategy: the parent population consists of 3 points, and 3 points are generated from this population and act as the new population. The difference with respect to "standard" EDAs is as follows:

- the algorithm is derandomized: population $t$ is generated deterministically from population $t-1$;
- since $\mu=\lambda$, there is no need for actually ranking all the points (the algorithm still orders two points among the three as will be seen below).
The algorithm is comparison-based (since fitness values only matter by how they order the population), and fits the general description of an EDA.

Algorithm 3 R-EDA: algorithm for optimizing noisy fitness functions. Bernstein denotes a Bernstein race, as defined in Algorithm 2. The initial domain is $\left[x_{0}^{-}, x_{0}^{+}\right] \in \mathbb{R}^{D}$, $\delta$ is the confidence parameter.
$n \leftarrow 0$
while True do
$c_{n}=\arg \max _{i}\left(x_{n}^{+}\right)_{i}-\left(x_{n}^{-}\right)_{i} \quad / /$ Pick the coordinate with highest uncertainty
$\delta_{n}^{\max }=\left(x_{n}^{+}\right)_{c_{n}}-\left(x_{n}^{-}\right)_{c_{n}}$
for $i \in[[1,3]]$ do
$x_{n}^{\prime} \leftarrow \frac{1}{2}\left(x_{n}^{-}+x_{n}^{+}\right) \quad / /$ Consider the middle point $\left(x_{n}^{\prime \prime}\right)_{c_{n}} \leftarrow\left(x_{n}^{-}\right)_{c_{n}}+\frac{1}{2}\left(x_{n}^{+}-x_{n}^{-}\right)_{c_{n}} \quad / /$ The $c_{n}^{\text {th }}$ coordinate may take $3 \neq$ values
end for
$\left(\right.$ good $\left._{n}, b a d_{n}\right)=\operatorname{Bernstein}\left(x_{n}^{\prime 1}, x_{n}^{\prime 2}, x_{n}^{\prime 3}, \frac{b b}{\pi^{2}(n+1)^{2}}\right)$.
// A good and a bad point
Let $H_{n}$ be the halfspace
$\left\{x \in \mathbb{R}^{D} ;\left\|x-\right.\right.$ good $\left._{n} \| \leq\left\|x-b a d_{n}\right\|\right\}$
Split the domain: $\left[x_{n+1}^{-}, x_{n+1}^{+}\right]=H_{n} \cap\left[x_{n}^{-}, x_{n}^{+}\right]$
$n \leftarrow n+1$
end while
Sketch of R-EDA (Algorithm 3). We will use R-EDA (Algorithm 3) for showing the upper bounds. It proceeds by iteratively splitting the domain in two (not necessarily equal) halves, and retaining the one that most probably contains the optimum. At iteration $n$, from the $n_{t h}$ domain $\left[x_{n}^{-}, x_{n}^{-}\right]$, the $(n+1)_{t h}$ domain $\left[x_{n+1}^{-}, x_{n+1}^{+}\right]$is obtained by:

- Finding the coordinate $c_{n+1}$ such that $\delta_{n}^{\max }=$ $\left(x_{n}^{+}\right)_{c_{n}}-\left(x_{n}^{-}\right)_{c_{n}}$ is maximal;
- Selecting three regularly spaced points along this coordinate (see Figure 1);
- Repeatingly assessing those 3 points until we have confidence that the optimum is closer to one point $x_{n}^{\prime j}$ than to another $x_{n}^{\prime j}$ (by Bernstein race);
- Splitting the domain by the hyperplane in the middle of these points and normal to the line they define, and keeping only the side of the domain containing $x_{n}^{\prime j}$.

It is important to notice that three points selected at each iteration are necessarily distinct. A key element in proving upper bounds with this algorithm is that the fitness monotonic in the distance to the optimum ( $\left.\left\|a-x^{*}\right\|\right\rangle$ $\left.\left\|b-x^{*}\right\| \Rightarrow f(a)>f(b)\right)$, and it also has spherical symmetry $\left(\left\|a-x^{*}\right\|=\left\|b-x^{*}\right\| \Rightarrow f(a)=f(b)\right)$. Consequently, it is guaranteed that when choosing three points as in Algorithm 3, at least one of them will have an expected fitness that is different from two others. That is why the race will output a consistent result with high probability.

For simplicity, it is assumed that the initial domain is a hyperrectangle. Consequently, at any iteration $n$, the halfspace $H_{n}$ is a hyper-rectangle, whose largest axis' length $\delta_{n}^{\max }$ (defined in Algorithm 3) satisfies $\delta_{n}^{\max } \leq \frac{3 \cdot(n / D)}{4}$. The straightforward proof of this fact is given in [24], where R-EDA first appears.

The following lemma will be used for the upper bound. A similar lemma was published in [24], but it only applied to $p=1$. Notations are those introduced in Algorithm 3.

LEMMA 3. (The conditions of the Bernstein race are met) Assume that $x^{*} \in\left[x_{n}^{-}, x_{n}^{+}\right]$and $p \geq 2$. Then

$$
\max _{(i, j) \in[[1,3]]^{2}} f\left(x_{n}^{\prime j}\right)-f\left(x_{n}^{\prime i}\right) \geq 2\left(\frac{\delta_{\max }^{n}}{2}\right)^{p}
$$

Proof of Lemma 3. Let $\overrightarrow{x_{n}}$ be the projection of $x^{*}$ on the line on which $x_{n}^{\prime 1}, x_{n}^{\prime 2}, x_{n}^{\prime 3}$ lie. The result will now be proved for $\left(\overrightarrow{x_{n}}\right)_{c_{n}} \in\left[\left(x_{n}^{\prime 1}\right)_{c_{n}},\left(x_{n}^{\prime 2}\right)_{c_{n}}\right]$. The proof for the case $\left(\overrightarrow{x_{n}}\right)_{c_{n}} \in\left[\left(x_{n}^{\prime 2}\right)_{c_{n}},\left(x_{n}^{\prime 3}\right)_{c_{n}}\right]$ is symmetric (see Figure 1).
![img-0.jpeg](img-0.jpeg)

Figure 1: The large rectangle is the domain $\left[x_{n}^{-}, x_{n}^{+}\right]$, The three circles are arms $x_{n}^{\prime}, x_{n}^{\prime 2}, x_{n}^{\prime 3}$; the left arm is the "bad" arm, whereas the arm in the center is the "good" arm, i.e. the one which proved to be closer to the optimum than the left arm, with confidence $1-6 \delta /\left(\pi^{2} n^{2}\right)$; the point on the right is the third arm which is considered to be neither "good", nor "bad".

First of all, we have

$$
\Delta_{n} \doteq \max _{i, j \in[[1,3]]^{2}} f\left(x_{n}^{\prime i}\right)-f\left(x_{n}^{\prime j}\right) \geq f\left(x_{n}^{\prime 3}\right)-f\left(x_{n}^{\prime 2}\right)
$$

By Pythagora's theorem, $\forall i \in[[1,3]],\left\|x^{\prime}{ }^{\epsilon}-x^{*}\right\|^{2}=\left\|x_{n}^{\prime}{ }^{\epsilon}-\right.$ $\left.\left.x_{n}^{*}\right\|^{2}+\left\|x_{n}^{*}-x^{*}\right\|^{2}\right.$. Thus,

$$
\begin{aligned}
\Delta_{n} & \geq\left(\sqrt{\left\|x_{n}^{\prime 2}-x_{n}^{*}\right\|^{2}+\left\|x_{n}^{*}-x^{*}\right\|^{2}}\right)^{p} \\
& -\left(\sqrt{\left\|x_{n}^{\prime 2}-x_{n}^{*}\right\|^{2}+\left\|x_{n}^{*}-x^{*}\right\|^{2}}\right)^{p}
\end{aligned}
$$

Note that $\left\|x^{\prime 3}-x_{n}^{*}\right\|=\left\|x_{n}^{\prime 2}-x_{n}^{*}\right\|+\delta_{n}^{\max } / 2$. Define $d=\left\|x_{n}^{*}-x^{*}\right\|^{2}$ and $a=\left\|x^{\prime 3}-x_{n}^{*}\right\|$. Then, observing that $\delta_{n}^{\max } \geq a \geq \delta_{n}^{\max } / 2$, we have

$$
\begin{aligned}
\Delta_{n} & \geq\left(\sqrt{a^{2}+d}\right)^{p}-\left(\sqrt{\left(a-\delta_{n}^{\max } / 2\right)^{2}+d}\right)^{p} \\
& \geq a^{p}\left(\left(\sqrt{1+d / a^{2}}\right)^{p}-\left(\sqrt{\left(1-\frac{\delta_{n}^{\max }}{2 a}\right)^{2}}+\frac{d}{a^{2}}\right)^{p}\right) \\
& \geq\left(\frac{\delta_{n}^{\max }}{2}\right)^{p}\left(\left(\sqrt{1+d / a^{2}}\right)^{p}-\left(\sqrt{\frac{1}{4}+\frac{d}{a^{2}}}\right)^{p}\right)
\end{aligned}
$$

By setting $u=d / a^{2}$, it is clear that $\Delta_{n}$ is greater than the minimum of $u \mapsto(\sqrt{1+u})^{p}-(\sqrt{1 / 4+u})^{p}$ on the interval $[0, D]$ (since $\sqrt{d}=\left\|x_{n}^{*}-x^{*}\right\| \leq \sqrt{D} \delta_{n}^{\max } / 2$ ). This function is non-decreasing for $p \geq 2$, and therefore its minimum is its value in 0 , which is, for all $p \geq 2$, at least $\frac{1}{2}$; injecting in Equation 8 yields $\Delta_{n} \geq 2\left(\frac{\delta^{\max }}{2}\right)^{p}$, as stated by Eq. 7 .

Theorem 4. (Upper bounds for the STS model) Consider the STS model, and a fixed dimension D. The number of evaluations requested by R-EDA (Algorithm 3) to reach precision $\epsilon$ with probability at least $1-\delta$ is $\tilde{O}\left(\frac{\log (1 / \delta)}{\epsilon^{2 p}}\right)$.
Proof of Theorem 4. First, note that at iteration $n$, $\epsilon$ is upper bounded by $\left\|x_{n}^{-}-x_{n}^{*}\right\|$. Eq. 7 (shown in Lemma 3) ensures that $\Delta_{n}=\Omega\left(\left\|x_{n}^{+}-x_{n}^{-}\right\|^{p}\right)\left(\Delta_{n}\right.$ is defined by Eq. 3). Therefore, applying the concentration inequality, presented as Eq. 2, the number of evaluations in the $n^{\text {th }}$ iteration is at most

$$
\tilde{O}\left(\log \left(\frac{6 \delta}{\pi^{2}(n+1)^{2}}\right) /\left\|x_{n}^{-}-x_{n}^{+}\right\|^{2 p}\right)
$$

Now, let us consider the number $N(\epsilon)$ of iterations before a precision $\epsilon$ is reached. Eq. 4 shows that there is a constant $k<1$ such that $\epsilon \leq\left\|x_{n}^{+}-x_{n}^{-}\right\| \leq C k^{N(\epsilon)}$. Injecting this in Eq. 9 shows that the cost (the number of evaluations) in the last call to the Bernstein race is

$$
\operatorname{Bound}_{\text {last }}(\epsilon)=\tilde{O}\left(-\log \left(\frac{6 \delta}{\pi^{2}(N(\epsilon)+1)^{2}}\right) / \epsilon^{2 p}\right)
$$

Since $N(\epsilon)=O\left(\log (1 / \epsilon)\right), \quad$ Bound $_{\text {last }}=$ $O\left(\log (\log (1 / \epsilon) / \delta)) / \epsilon^{2 p} . \quad\right.$ For a fixed dimension $D$, the cost of the $(N(\epsilon)-i)^{t h}$ iteration is $O\left(\left(\right.\right.$ Bound $_{\text {last }} /\left.\left(k^{\prime}\right)^{\epsilon}\right)$ ) because the algorithm ensures that after $D$ iterations, $\left\|x_{n}^{+}-x_{n}^{-}\right\|$decreases by at least $3 / 4$ (see Eq. 4). The sum of the costs for $N(\epsilon)$ iterations is the sum of $O\left(\right.$ Bound $_{\text {last }} /\left(k^{\prime}\right)^{\epsilon}$ ) for $i \in\left[[0, N(\epsilon)-1]\right]$, that is $O\left(\right.$ Bound $_{\text {last }} /\left(\left.1-k^{\prime}\right)\right)=O\left(\right.$ Bound $_{\text {last }}$ ) (plus $O(N(\epsilon))$ for the rounding associated to the [...]). The overall cost is therefore $O\left(\right.$ Bound $_{\text {last }}+\log (1 / \epsilon)$ ), yielding the expected result.

Theorem 4 can be modified to use the small noise assumption, i.e. the case $c=0$. We then get a Bernstein's type rate, as follows:

Theorem 5. (Upper bounds for the STS model with small noise) Consider the STS model, and a fixed dimension D. Assume additionally that $c=0$, i.e. the scaled sphere model. The number of evaluations requested by R-EDA (Algorithm 3) to reach precision $\epsilon$ with probability at least $1-\delta$ is $\tilde{O}\left(\frac{\log (1 / \delta)}{\epsilon^{2}}\right)$.

Proof of Theorem 5. The variance of a Bernoulli random variable is always upper bounded by its expectation. The case $c=0$ implies that the expectation is upper bounded by the square of the distance to the optimum. Therefore, Eq. 3 holds. Thanks to Eq. 3, we can then use Eq. 4 instead of Eq. 2 in the proof of Theorem 4. This yields the expected result.

Note that this analysis is not limited to fitnesses that are exactly described by $f(x)=c+\left\|x-x^{*}\right\|^{p}$, but apply to any monotonic transformation of the sphere function that has a Taylor expansion of degree $p$ around its optimum.

## 5. EXPERIMENTS

We illustrate results of our experiments with an algorithm without surrogate models, UH-CMA, introduced in [17], and an algorithm with surrogate models, QLR (based on Quadratic Logistic Regression, i.e. it is assumed that the function is locally quadratic).

UH-CMA is an uncertainty handling approach based on a state-of-the-art CMA-ES. QLR, in comparison to many alternative methods, has only one mega-parameter to adjust (a Bayesian prior) and keeps information on all observed data.

### 5.1 Experimental results for UH-CMAoptimization without surrogate models

UH-CMA has been developed with intensive testing on the BBOB challenge [4], which includes mild models of noise. See [16] for the source code used in these experiments. The optimization domain is $\mathbb{R}^{2}$. Let $\mathcal{B}(q)$ denote a Bernoulli distribution of parameter $q, \mathcal{N}\left(\mu, \sigma^{2}\right)$ denote a Gaussian distribution centered on $\mu$ with variance $\sigma^{2}$, and $\mathcal{U}(I)$ denote a uniform distribution on interval $I$. UH-CMA ${ }^{2}$ was tested on four different noisy fitnesses: 1) $\|x\|^{2}(1+\mathcal{N}(0,0.1)) ; 2)$ $\|x\|^{2}+\mathcal{U}([0,1]) ; 3) \mathcal{B}\left(\|x\|^{2}\right) ; 4) \mathcal{B}\left(\|x\|^{2}+0.5\right)$.

The experiements with UH-CMA have been carried out using the following setting. The number of repeats equals 100, the population size $\lambda=4+\lfloor 3 \log N\rfloor$, where $N$ is the problem dimension, and the parent number $\mu=\lfloor\lambda / 2\rfloor$.

The initial values required by UH-CMA to start the search were sampled from $\mathcal{U}\left([0,1]^{2}\right)$. The convergence (and divergence) of UH-CMA-illustrated on Figure 2-is known to be log-linear.

For $\|x\|^{2}(1+\mathcal{N}(0,0.1))$, the algorithm converges efficiently: the precision decreases exponentially as the number of iterations increases. For $\|x\|^{2}+\mathcal{U}([0,1])$, the precision stops improving after a few hundred iterations. For $\mathcal{B}\left(\|x\|^{2}\right)$ and $\mathcal{B}\left(\|x\|^{2}+0.5\right)$ we observed divergence.

Let us point out that by adding some specific rules for averaging multiple fitness evaluations depending on the stepsize, specifically for each fitness function, it is possible to

[^0]
[^0]:    ${ }^{2}$ The version of UH-CMA used in our experiments is the one that was available at that time in http://www.lri. fr/ hansen/cmaesintro.html. The noise handling was activited and it was not modified in any manner.

obtain much better rates [15]. However, to the best of our knowledge, the rates remain worse than those reached by QLR.

### 5.2 Experiments with QLR—optimization with surrogate models

QLR is based on a Bayesian quadratic logistic regression. It samples regions of the search space with maximum variance of the posterior probability, i.e. regions with high variance conditionally to past observations. This is a key difference w.r.t. algorithms without surrogate models, which tend to sample points close to the optimum. QLR is fully described by $[12,8,21]$ (design of experiments for quadratic logistic model), [27] (active learning for logistic regression). See [10] for the code we used here, specifically tailored to binary noisy fitnesses.

QLR was tested on fitnesses of the form $B\left(\|x\|^{p}+c\right)$, for $p$ in $\{1,2\}$ and $c$ in $\{0,1 / 2\}$. The search space is $\mathbb{R}^{2}$. Figure 3 shows the experimental results:

Top left ( $\mathrm{p}=1, \mathrm{c}=0$ ): QLR converges on $x \mapsto B\left(\|x-\right.$ $\left.x^{*}\| \right)$, but with a suboptimal exponent $\frac{1}{2}$ (the slope of the curve is $-\frac{1}{2}$ in log-scale), i.e. $\mathbb{E} f\left(x_{n}\right)-\mathbb{E} f\left(x^{*}\right) \simeq \Theta(1 / \sqrt{n})$. R-EDA reaches a better $1 / n$ in this case;

Top right ( $\mathrm{p}=1, \mathrm{c}=1 / 2$ ): QLR converges with optimal exponent $1 / \sqrt{n}$ also reached by R-EDA;

Bottom left ( $\mathrm{p}=2, \mathrm{c}=0$ ): QLR reaches $\mathbb{E} f\left(x_{n}\right)-$ $\mathbb{E} f\left(x^{*}\right) \simeq \Theta(1 / n)$ as well as R-EDA;

Bottom right ( $\mathrm{p}=2, \mathrm{c}=1 / 2$ ): QLR still reaches $\mathbb{E} f\left(x_{n}\right)-$ $\mathbb{E} f\left(x^{*}\right) \simeq \Theta(1 / n)$ whereas R-EDA only reaches $1 / \sqrt{n}$.

## 6. CONCLUSION

The convergence rates for R-EDA (see [26]) and QLR are:

| fitness | $\left\|x_{n}-x^{*}\right\|$ <br> for R-EDA | Theoretical <br> lower-bound | $\left\|x_{n}-x^{*}\right\|$ for <br> QLR $(p=2)$ |
| :--: | :--: | :--: | :--: |
| $\lambda\left\|x-x^{*}\right\|$ | $\tilde{O}(1 / n)$ | $\Omega(1 / n)$ | $\simeq 1 / \sqrt{n}$ |
| $\lambda\left\|x-x^{*}\right\|+c$ | $\tilde{O}(1 / \sqrt{n})$ | $\Omega(1 / n)$ | $\simeq 1 / \sqrt{n}$ |
| $g\left(\left\|x-x^{*}\right\|\right)$ | $o(1)$ |  |  |
| $\lambda\left\|x-x^{*}\right\|^{p}+c$ | $\tilde{O}\left(1 / n^{1 / 2 p}\right)$ | $\Omega(1 / n)$ | $\simeq 1 / \sqrt{n}$ |
| $\lambda\left\|x-x^{*}\right\|^{p}$ | $\tilde{O}\left(1 / n^{1 / p}\right)$ | $\Omega(1 / n)$ | $\simeq 1 / \sqrt{n}$ |
| $\lambda\left\|x-x^{*}\right\|^{2}$ | $\tilde{O}(1 / \sqrt{n})$ | $\Omega(1 / n)$ | $\simeq 1 / \sqrt{n}$ |

Convergence rates are given for minimization; the fitness at point $x$ is the Bernoulli random variable $\mathcal{B}(f(x))$ with parameter $\min \left(1, \max (0, f(x))\right), x_{n}$ is the approximation of the optimum after $n$ fitness evaluations, $x^{*}$ is the optimum, $c>0$, and $g$ is some increasing mapping.

For the rightmost column, it is important to point out that we run experiments with QLR without knowledge of the parameter $p$, so that the comparison with other algorithms is fair. In particular, there is a single algorithm, R-EDA, which provably realizes the upper bounds above; a better algorithm should be better for all cases simultaneously without problem-specific parametrization.

The original results of our paper are presented by three last rows and the rightmost column; in particular we have shown:

- The upper and lower bounds for an exponent $p>1$;
- For $p=1$ and $c=0$, QLR is not optimal; R-EDA reaches (provably) $\tilde{O}(1 / n)$ whereas QLR has convergence $1 / \sqrt{n}$. By construction, it is probably difficult for QLR to do better than $1 / \sqrt{n}$;
- For $p=1$ and $c>0$, QLR and R-EDA perform equivalently $(1 / \sqrt{n})$; the lower bound does not match the upper bound. For R-EDA we have a mathematical proof and for QLR empirical evidence.
- For $p=2$ and $c=0$, QLR and R-EDA perform equivalently $(1 / \sqrt{n})$; the lower bound does not match the upper bound. For R-EDA we have a mathematical proof and for QLR empirical evidence.
- For $p=2$ and $c=0$, QLR (empirically) performs better than the proved upper bound and worse than the proved lower bound.

There is therefore still room for improvements.
Results for QLR and for UH-CMA are empirical, based on current versions of the algorithms. The available implementation of UH-CMA cope quite well with small noise situations, but as soon as the variance does not go to zero sufficiently fast it does not succeed.

R-EDA is efficient in many cases, yet its theoretical convergence rates are suboptimal in the case $B\left(c+\left\|x-x^{*}\right\|^{2}\right)$, more relevant from a practical point of view. However, R-EDA is not limited to Bernoulli-like fitness functions, whereas QLR is. This is why QLR is more efficient in the case $B\left(c+\left\|x-x^{*}\right\|^{2}\right)$ for $c>0$. UH-CMA does not converge in such cases, what demonstrates that algorithms tailored for small noise models do not easily extend to models with large noise. However, UH-CMA is the only algorithm with log-linear precision as a function of the number of iterations in the easy case $\left\|x-x^{*}\right\|^{2}(1+\mathcal{N})$.

R-EDA can be applied to any fitness of the form $x \mapsto$ $g\left(\left\|x-x^{*}\right\|\right)$ with $x^{*}$ the optimum and $g$ an increasing mapping, and will converge to the optimum. If, in addition, if $g$ is differentiable in 0 with non-zero derivative, then the convergence rate is guaranteed to meet the rates $p=1$ presented above. More generally, if $g$ is $p$ times differentiable in 0 , with the $p-1$ first derivatives null, then the convergence rate is the general rate presented above for a given $p$. A relevant further work would be to extend the algorithm to non-spherical models (i.e. no spherical symmetry around the optimum), in order to have more general convergence bounds.

Given the convergence rate table above, one can see that lower bounds for $p>1$ or $c>0$ are not tight. A relevant further work would be either to find out how to reach these bounds, or to prove lower bounds achieving tightnesswhich seems more likely, given that the current lower bounds are quite optimistic.

## 7. ACKNOWLEDGEMENTS

This work was supported by the IST Programme of the European Community, under the PASCAL2 Network of Excellence, IST-2007-216886; by Ministry of Higher Education and Research, Nord-Pas de Calais Regional Council and FEDER through the "CPER 2007-2013".
