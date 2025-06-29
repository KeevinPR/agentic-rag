# Sharp Bounds for Genetic Drift in Estimation of Distribution Algorithms 

Benjamin Doerr and Weijie Zheng


#### Abstract

Estimation of distribution algorithms (EDAs) are a successful branch of evolutionary algorithms (EAs) that evolve a probabilistic model instead of a population. Analogous to genetic drift in EAs, EDAs also encounter the phenomenon that the random sampling in the model update can move the sampling frequencies to boundary values not justified by the fitness. This can result in a considerable performance loss. This article gives the first tight quantification of this effect for three EDAs and one ant colony optimizer, namely, for the univariate marginal distribution algorithm, the compact genetic algorithm, population-based incremental learning, and the max-min ant system with iteration-best update. Our results allow to choose the parameters of these algorithms in such a way that within a desired runtime, no sampling frequency approaches the boundary values without a clear indication from the objective function.


Index Terms-Estimation of distribution algorithms (EDAs), genetic drift, running time analysis, theory.

## I. INTRODUCTION

ESTIMATION of distribution algorithms (EDAs) are evolutionary algorithms (EAs) that evolve a probabilistic model instead of a population. An iteration of an EDA usually consists of three steps: 1) based on the current probabilistic model, a population of individuals is sampled; 2) the fitness of this population is determined; and 3) update of

[^0]the probabilistic model: based on the fitness of this population and the probabilistic model, a new probabilistic model is computed.

Different probabilistic models and update strategies form different specific algorithms in this framework. In multivariate EDAs, the probabilistic model contains dependencies among the variables. Examples for multivariate EDAs include mutual-information-maximization input clustering [2], bivariate marginal distribution algorithm [3], the factorized distribution algorithm [4], the extended compact genetic algorithm (cGA) [5], and many others.

For univariate EDAs, the bit positions of the probabilistic model are mutually independent. Univariate EDAs include population-based incremental learning (PBIL) [6], [7] with special cases univariate marginal distribution algorithm (UMDA) [8] and max-min Ant System with iteration-best update ( $\mathrm{MMAS}_{\text {ib }}$ ) [9], and the cGA [10]. Since the dependencies in multivariate EDAs bear significant difficulties for a mathematical analysis, almost all theoretical results for EDAs regard univariate models [11]. This article also deals exclusively with univariate EDAs.

In EAs, it is known that the frequencies of bit values in the population are not only influenced by the contribution of the bit to the fitness but also by random fluctuation stemming from other bits having a stronger influence on the fitness. These random fluctuations can even lead to certain bits converging to a single value different from the one in the optimal solution. This effect is called genetic drift [12], [13].

Genetic drift also happens in EDAs. González et al. [14] showed that for the 2-D OneMax function, the sampling frequency of PBIL can converge to any search point in the search space with probability near to 1 if the initial sampling frequency goes to that search point and the learning rate goes to 1 . Droste [15] noticed the possibility of the cGA getting stuck, but he only analyzed the runtime conditional on it being finite, and no analysis of genetic drift or stagnation times was given. Costa et al. [16] proved that a constant smoothing parameter for the cross entropy (CE) algorithm (which is equivalent to a constant learning rate $\rho$ for PBIL) results in that the probability mass function converges to a unit mass at some random candidate, but no convergence speed analysis was given. In summary, as Krejca and Witt said in [11], the genetic drift in EDAs is a general problem of martingales, that is, that a random process with zero expected change will eventually stop at the absorbing boundaries of the range. Witt [17] and Lengler et al. [18] recently showed that genetic drift can result in a considerable performance loss on the OneMax function.


[^0]:    Manuscript received November 4, 2019; revised February 23, 2020; accepted April 8, 2020. Date of publication April 13, 2020; date of current version December 1, 2020. This work was supported in part by the public grant as part of the Investissement d'Avenir Project, under Grant ANR-11-LABX-0056-LMH, LabEx LMH, in a joint call with Gaspard Monge Program for optimization, operations research and their interactions with data sciences, in part by the Program for Guangdong Introducing Innovative and Enterpreneurial Teams under Grant 2017ZT07X386, in part by the Guangdong Basic and Applied Basic Research Foundation under Grant 2019A1515110177, in part by the Shenzhen Peacock Plan under Grant KQTD2016112514355531, in part by the Program for University Key Laboratory of Guangdong Province under Grant 2017KSYS008, and in part by the Science and Technology Innovation Committee Foundation of Shenzhen under Grant JCYJ20190809121403553. (Benjamin Doerr and Weijie Zheng contributed equally to this work.) (Corresponding authors: Benjamin Doerr; Weijie Zheng.)

    Benjamin Doerr is with the Laboratoire d'Informatique, CNRS, École Polytechnique, Institut Polytechnique de Paris, 91120 Palaiseau, France (e-mail: doerr@lix.polytechnique.fr).

    Weijie Zheng was with the Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China, and also with the the Laboratoire d'Informatique, École Polytechnique, 91120 Palaiseau, France. He is now with the University Key Laboratory of Evolving Intelligent Systems of Guangdong Province, Department of Computer Science and Engineering, Southern University of Science and Technology, Shenzhen 518055, China, and also with the School of Computer Science and Technology, University of Science and Technology of China, Hefei 230027, China (e-mail: chengwj13@tsinghua.org.cn).

    Digital Object Identifier 10.1109/TEVC.2020.2987361

In this article, we shall quantify this effect asymptotically precisely for several EDAs and this via proven results. The few previous works in this direction have obtained the following results. Friedrich et al. [19] showed that for the cGA with hypothetical population size $K$, the frequency of a neutral bit position is arbitrary close to the borders 0 or 1 after expected $\omega\left(K^{2}\right)$ generations. Though not stated in [19], from its Corollary 9 , we can derive an upper bound of $O\left(K^{2}\right)$ for the expected time of leaving the interval $[(1 / 4),(3 / 4)]$, and $O\left(K^{2} \log K\right)$ for expected hitting time of a boundary value. For the UMDA selecting $\mu$ best individuals from $\lambda$ offspring, the situation is similar [19]. After $\omega(\mu)$ iterations, the frequencies are arbitrary close to the boundaries and the expected hitting time can be shown to be $O(\mu \log \mu)$ via similar arguments as above. Sudholt and Witt [20] mentioned that the boundary hitting time of the cGA is $\Theta\left(K^{2}\right)$, but without a complete proof (in particular, because they did not discuss what happens once the frequency leaves the interval $[(1 / 6),(5 / 6)])$. Although Krejca and Witt [21] focused on the lower bound of the runtime of the UMDA on OneMax, we can derive from it that the hitting time of the boundary 0 is at least $\Omega(\mu)$. This follows from the drift of $\phi$ in [21, Lemma 9] together with the additive drift theorem [22].

Our Results: While the results above give some indication on the degree of stability of PBIL and the cGA, a sharp proven result is still missing. This article overcomes this shortage and gives precise asymptotic hitting times for PBIL (including the UMDA and the $\mathrm{MMAS}_{\text {th }}$ ) and the cGA. With a simultaneous analysis of the UMDA and the cGA, we prove that for the UMDA selecting $\mu$ best individuals from $\lambda$ offspring on some $D$-dimensional problem, the expected number of iterations until the frequency of the neutral bit position is absorbed in 0 or 1 for the UMDA without margins or when the frequency hits the margins $\{1 / D, 1-1 / D\}$ for the UMDA with such margins is $\Theta(\mu)$, and the corresponding hitting time is $\Theta\left(K^{2}\right)$ for the cGA with hypothetical population size $K$. This article also gives a precise asymptotic analysis for PBIL selecting $\mu$ best individuals from $\lambda$ offspring and with a learning rate of $\rho$ : in expectation in $\Theta\left(\mu / \rho^{2}\right)$ generations the sampling frequency of a neutral bit position leaves the interval $[\Theta(\rho / \mu), 1-\Theta(\rho / \mu)]$ and then always the same value is sampled for this position.

For the lower bounds implicit in these estimates we prove an exponential tail bound in Theorem 2.

We also extend the lower bound results to bit positions that are neutral or have a preference for some bit value (Section VI). For example, we prove that for PBIL it takes an expected number of $\Omega\left(\mu / \rho^{2}\right)$ iterations until the sampling frequency of a position that is neutral or prefers a one (neutral or prefers a zero) reaches the interval $[0,(1 / 4)]$ $([(3 / 4), 1])$. The corresponding hitting time is $\Omega\left(K^{2}\right)$ for the cGA.

The remainder of this article is organized as follows. Section II briefly introduces PBIL and the cGA under the umbrella of the $n$-Bernoulli- $\lambda$-EDA framework proposed in [19]. Our notation for our results is fixed in Section III. Sections IV and V discuss how fast the frequency of a neutral bit position approaches the boundaries. Section VI extends the lower bound results of Section IV to bit positions that are neutral or have some preference. Finally, in Section VII

```
Algorithm 1 \(n\)-Bernoulli- \(\lambda\)-EDA Framework With Update
Scheme \(\varphi\) to Maximize a Function \(f:\{0,1\}^{D} \rightarrow \mathbb{R}\)
\(p^{0}=\left(\frac{1}{2}, \frac{1}{2}, \ldots, \frac{1}{2}\right) \in[0,1]^{D}\)
for \(t=1,2, \ldots\) do
        for \(i=1,2, \ldots, \lambda\) do
            \(\%\) \%Sampling of the \(i\)-th individual \(X_{i}^{t}=\left(X_{i, 1}^{t}, \ldots, X_{i, D}^{t}\right)\)
            for \(j=1,2, \ldots, D\) do
            \(X_{i, j}^{t} \leftarrow 1\) with probability \(p_{i}^{t-1}\) and
            \(X_{i, j}^{t} \leftarrow 0\) with probability \(1-p_{i}^{t-1}\);
        end for
        end for
            \%\%Update of the frequency vector
            \(p^{t} \leftarrow \varphi\left(p^{t-1},\left(X_{i}, f\left(X_{i}\right)\right)_{i=1, \ldots, \lambda}\right)\);
    end for
```

we argue how our results allow to interpret existing research results and how they give hints on how to choose the parameters of these EDAs.

## II. $n$-BERNOULLI- $\lambda$-EDA FRAMEWORK

Since the $n$-Bernoulli- $\lambda$-EDA framework proposed in [19] covers many well-known EDAs, including PBIL and the cGA, we use it to make precise these two EDAs.

We note that often margins like $1 / D$ and $1-1 / D$ are used, that is, the frequencies are restricted to stay in the interval $[1 / D, 1-1 / D]$. This prevents the frequencies from reaching the absorbing states 0 and 1 . To ease the presentation, we regard the EDAs without such margins. We note that, trivially, the time to reach an absorbing state is not smaller than the time to reach a margin value. Hence, an upper bound on the hitting time of the absorbing states is also an upper bound for the time to reach or exceed the margin values. Our main result on lower bounds, Corollary 1 , shows a lower bound for the time to reach a frequency value in $[0,(1 / 4)] \cup[(3 / 4), 1]$. This again is a lower bound for the time to reach (or exceed) the margin values or the absorbing states.

The $n$-Bernoulli- $\lambda$-EDA framework for maximizing a function $f:\{0,1\}^{D} \rightarrow \mathbb{R}$ is shown in Algorithm 1. By suitably specifying the update scheme $\phi$, we derive PBIL and the cGA. The general idea of PBIL is to sample $\lambda$ individuals from the current distribution, select $\mu$ best of them, and use these (with a learning rate of $\rho$ ) and the current distribution to define the new distribution. Formally, the update scheme is

$$
\begin{aligned}
p_{j}^{t} & =\varphi\left(p^{t-1},\left(X_{i}, f\left(X_{i}\right)\right)_{i=1, \ldots, \lambda}\right)_{j} \\
& =(1-\rho) p_{j}^{t-1}+\frac{\rho}{\mu} \sum_{i=1}^{\mu} \tilde{X}_{i, j}^{t}
\end{aligned}
$$

where $\rho$ is the learning rate and $\tilde{X}_{1}^{t}, \ldots, \tilde{X}_{\mu}^{t}$ are the selected $\mu$ best individuals from the $\lambda$ offspring.

The CE algorithm has various definitions according to the problems to be solved. The basic CE algorithm for discrete optimization [16] samples $N$ individuals from the current distribution, selects $N_{b}$ best of them, and uses these (with a time-dependent smoothing rate of $\alpha_{t}$ ) and the current distribution to define the new distribution. The formal update scheme is (1) with $\mu, \lambda$, and $\rho$, respectively, replaced by $N_{b}, N$, and $\alpha_{t}$. The basic CE is equal to PBIL except that the learning rate is

fixed for PBIL, whereas CE utilizes time-dependent learning rates. When referring to the CE algorithm in this article, we mean this version from [16], but we denote its parameters by $\mu, \lambda$, and $\rho_{t}$ instead of $N_{b}, N$, and $\alpha_{t}$ to reflect the similarity with PBIL.

Two special cases of PBIL have been regarded in the literature. The UMDA only uses the samples of this current iteration to define the next probabilistic model, hence it is equivalent to PBIL with a learning rate of $\rho=1$. The $\lambda$-max-min ant system ( $\lambda$-MMAS) only selects the best-sampled individual and the current model to construct the new model, hence, it is the special case with $\mu=1$.

The cGA with hypothetical population size $K$, not necessarily an integer, samples two individuals and then changes the frequency of each bit position by an absolute value of $1 / K$ toward the bit value of the better individual (unless the two sampled individuals have identical values in this position). Formally, we have $\lambda=2$ in the $n$-Bernoulli- $\lambda$-EDA framework and the update scheme is

$$
\begin{aligned}
p_{j}^{t} & =\varphi\left(p^{t-1},\left(X_{i}, f\left(X_{i}\right)\right)_{i=1, \ldots, \lambda}\right)_{j} \\
& = \begin{cases}p_{j}^{t-1}+\frac{1}{K}, & \text { if } X_{(1), j}^{t}>X_{(2), j}^{t} \\
p_{j}^{t-1}-\frac{1}{K}, & \text { if } X_{(1), j}^{t}<X_{(2), j}^{t} \\
p_{j}^{t-1}, & \text { if } X_{(1), j}^{t}=X_{(2), j}^{t}\end{cases}
\end{aligned}
$$

where $\left\{X_{(1)}^{t}, X_{(2)}^{t}\right\}=\left\{X_{1}^{t}, X_{2}^{t}\right\}$ such that $f\left(X_{(1)}^{t}\right) \geq f\left(X_{(2)}^{t}\right)$. We shall always make the following well-behaved frequency assumption (first called so in [23], but made in many earlier works already): any two frequencies the cGA can reach differ by a multiple of $1 / K$. In the case of no margins, this means that the cGA can only use frequencies in $\{0,1 / K, 2 / K, \ldots, 1\}$. Note that $K$ needs to be even so that the initial frequency $1 / 2$ is also a multiple of $1 / K$. When using the margins $1 / D$ and $1-1 / D$, the set of reachable frequency boundaries is $\{1 / D, 1 / D+1 / K, 1 / D+2 / K, \ldots, 1-1 / D\}$. To have $1 / 2$ in this set, $1-2 / D$ needs to be an even multiple of $1 / K$.

## III. Notation Used in Our Analyses

Genetic drift is usually studied via the behavior of a neutral bit position. Let $f:\{0,1\}^{D} \rightarrow \mathbb{R}$ be an arbitrary fitness function with a neutral bit position. Without loss of generality, let the first bit position of the fitness function $f$ be neutral, that is, we have $f\left(0, X_{2}, \ldots, X_{D}\right)=f\left(1, X_{2}, \ldots, X_{D}\right)$ for all $X_{2}, \ldots, X_{D} \in\{0,1\}$. Then we can simply assume that $\tilde{X}_{i, 1}^{t}=$ $X_{i, 1}^{t}, i=1, \ldots, \mu$ in (1), and $X_{(1), 1}^{t}=X_{1,1}^{t}, X_{(2), 1}^{t}=X_{2,1}^{t}$ in (2). Let $p_{t}=p_{1}^{t}$ be the frequency of the neutral bit position after generation $t$. For PBIL, we have

$$
p_{t}= \begin{cases}\frac{1}{2}, & t=0 \\ (1-\rho) p_{t-1}+\frac{\rho}{\mu} \sum_{i=1}^{\mu} X_{i, 1}^{t}, & t \geq 1\end{cases}
$$

where the $X_{i, 1}^{t}$ are independent 0,1 random variables with $\operatorname{Pr}\left[X_{i, 1}^{t}=1\right]=p_{t-1}$.

For the cGA, we have

$$
p_{t}= \begin{cases}\frac{1}{2}, & t=0 \\ \left\{\begin{array}{l}
p_{t-1}+\frac{1}{K}, \quad \text { if } X_{1,1}^{t}>X_{2,1}^{t} \\
p_{t-1}-\frac{1}{K}, \quad \text { if } X_{1,1}^{t}<X_{2,1}^{t}, \\
p_{t-1}, \quad \text { if } X_{1,1}^{t}=X_{2,1}^{t}
\end{array}, \quad t \geq 1\right. \\ \hline
\end{cases}
$$

where $X_{1,1}^{t}$ and $X_{2,1}^{t}$ are independent 0,1 random variables with $\operatorname{Pr}\left[X_{1,1}^{t}=1\right]=\operatorname{Pr}\left[X_{2,1}^{t}=1\right]=p_{t-1}$.

We observe that this random process $\left(p_{t}\right)$ is independent of $f, D$, and, in the case of PBIL, $\lambda$. We also have

$$
E\left[p_{t} \mid p_{t-1}\right]=p_{t-1}
$$

that is, both PBIL and the cGA are balanced in the sense of [19].

Finally, let $T=\min \left\{t \mid p_{t} \in\{0,1\}\right\}$ be the hitting time of the absorbing states 0 and 1 .

We are now ready to prove our matching upper and lower bounds for the hitting time $T$. We start with lower bounds in Section IV as these are easier to prove and thus a good warm-up for the upper bound proofs in Section V.

## IV. LOWER BOUNDS ON THE BOUNDARY HitTING TIME

To prove our lower bounds, we use the following version of the Hoeffding-Azuma inequality for maxima, see [24, Th. 3.10 and (41)] and note that in (41) the absolute value should be inside the maximum, as can be seen from the proof in [24].

Theorem 1 [24]: Let $a_{1}, \ldots, a_{m} \in \mathbb{R}$, and $S_{1}, \ldots, S_{m}$ be a martingale difference sequence with $\left|S_{k}\right| \leq a_{k}$ for each $k$. Then for any $s \geq 0$

$$
\operatorname{Pr}\left[\max _{k=1, \ldots, m}\left|\sum_{i=1}^{k} S_{i}\right| \geq s\right] \leq 2 \exp \left(-\frac{s^{2}}{2 \sum_{i=1}^{m} a_{i}^{2}}\right)
$$

Now, we prove our lower bounds. We first derive tail bounds in Theorem 2, and use the tail bounds to further obtain our lower bounds on the expected hitting time of the absorbing states. The expectations of hitting times are asymptotically equal to (and necessarily not less than) the expected times of leaving the frequency range $(\{1 / 4\},[3 / 4])$, so we determine these in Corollary 1, which are also of independent interest.

Theorem 2: Consider using an $n$-Bernoulli- $\lambda$-EDA to optimize some function $f$ with a neutral bit position. Let $p_{t}, t=0,1,2, \ldots$, denote the frequency of the neutral bit position after iteration $t$.

1) If the EDA is PBIL with learning rate $\rho$ and selection size $\mu$, then for all $\gamma>0$ and $T \in \mathbb{N}$ we have

$$
\operatorname{Pr}\left[\forall t \in\left[0 . . T\right]:\left|p_{t}-\frac{1}{2}\right|<\gamma\right] \geq 1-2 \exp \left(-\frac{\gamma^{2} \mu}{2 \rho^{2} T}\right)
$$

2) If the EDA is the cGA with hypothetical population size $K$, then for all $\gamma>0$ and $T \in \mathbb{N}$ we have

$$
\operatorname{Pr}\left[\forall t \in\left[0 . . T\right]:\left|p_{t}-\frac{1}{2}\right|<\gamma\right] \geq 1-2 \exp \left(-\frac{\gamma^{2} K^{2}}{2 T}\right)
$$

Proof: For PBIL, building on the notation introduced in Section III, we consider the random process

$$
Z_{t \mu+a}=(1-\rho) p_{t} \mu+\rho p_{t}(\mu-a)+\rho \sum_{i=1}^{a} X_{i, 1}^{t+1}
$$

where $t=0,1, \ldots$, and $a=0,1, \ldots, \mu-1$. For $a=0$, we obviously have $Z_{t \mu} / \mu=p_{t}$, that is, the $Z$-process contains the process $\left(p_{t}\right)$ we are interested in. Noting that $Z_{(t+1) \mu}$ can also

be written as $Z_{i \mu+\mu}=(1-\rho) p_{t} \mu+\rho p_{t}(\mu-\mu)+\rho \sum_{i=1}^{\mu} X_{i, 1}^{t+1}$, it is also not difficult to see that for all $k=0,1, \ldots$, we have

$$
\begin{aligned}
& \operatorname{Pr}\left[Z_{k+1}=Z_{k}+\rho-\rho p_{t} \mid Z_{1}, \ldots, Z_{k}\right]=p_{t} \\
& \operatorname{Pr}\left[Z_{k+1}=Z_{k}+0-\rho p_{t} \mid Z_{1}, \ldots, Z_{k}\right]=1-p_{t}
\end{aligned}
$$

where $t=\lfloor k / \mu\rfloor$. Consequently

$$
E\left[Z_{k+1} \mid Z_{1}, \ldots, Z_{k}\right]=Z_{k}
$$

and the sequence $Z_{0}, Z_{1}, Z_{2}, \ldots$, is a martingale. For $k=$ $1,2, \ldots$, let $R_{k}=Z_{k}-Z_{k-1}$ define the martingale difference sequence. By (4)

$$
\left|R_{k}\right| \leq \max \left\{\rho\left(1-p_{t}\right), \rho p_{t}\right\} \leq \rho
$$

By the Hoeffding-Azuma inequality (Theorem 1), we have

$$
\operatorname{Pr}\left[\max _{k=1, \ldots, t \mu}\left|\sum_{i=1}^{k} R_{i}\right| \geq M\right] \leq 2 \exp \left(-\frac{M^{2}}{2 t \mu \rho^{2}}\right)
$$

Recalling $Z_{0}=(\mu / 2)$ and $p_{t}=Z_{t \mu} / \mu$, we have

$$
\begin{aligned}
& \operatorname{Pr}\left[\max _{k=1, \ldots, t}\left|p_{k}-\frac{1}{2}\right| \geq M / \mu\right] \\
& \quad \leq \operatorname{Pr}\left[\max _{k=1, \ldots, t \mu}\left|\sum_{i=1}^{k} R_{i}\right| \geq M\right]
\end{aligned}
$$

Combining (5) and (6) with $M=\gamma \mu$, we obtain

$$
\operatorname{Pr}\left[\max _{k=1, \ldots, t}\left|p_{k}-\frac{1}{2}\right| \geq \gamma\right] \leq 2 \exp \left(-\frac{\gamma^{2}}{2 t \rho^{2}}\right)
$$

and thus we prove the result for PBIL.
For the cGA, we may simply regard the process $Z_{k}=p_{k}$. Since for all $k=0,1, \ldots$

$$
\begin{aligned}
\operatorname{Pr}\left[Z_{k+1}=Z_{k}+\frac{1}{K} \mid Z_{1}, \ldots, Z_{k}\right] & =p_{k}\left(1-p_{k}\right) \\
\operatorname{Pr}\left[Z_{k+1}=Z_{k}-\frac{1}{K} \mid Z_{1}, \ldots, Z_{k}\right] & =p_{k}\left(1-p_{k}\right) \\
\operatorname{Pr}\left[Z_{k+1}=Z_{k} \mid Z_{1}, \ldots, Z_{k}\right] & =1-2 p_{k}\left(1-p_{k}\right)
\end{aligned}
$$

we have $E\left[Z_{k+1} \mid Z_{1}, \ldots, Z_{k}\right]=Z_{k}$. The martingale difference sequence $R_{k}:=Z_{k}-Z_{k-1}$ satisfies $\left|R_{k}\right| \leq(1 / K)$. By the Hoeffding-Azuma inequality, we have

$$
\begin{aligned}
& \operatorname{Pr}\left[\max _{k=1, \ldots, t}\left|p_{k}-\frac{1}{2}\right| \geq M\right] \\
& \quad=\operatorname{Pr}\left[\max _{k=1, \ldots, t}\left|\sum_{i=1}^{k} R_{i}\right| \geq M\right] \leq 2 \exp \left(-\frac{M^{2} K^{2}}{2 t}\right)
\end{aligned}
$$

Taking $M=\gamma$ we prove our result for the cGA.
Let $T_{0}$ the first time the frequency of the neutral bit position is in $[0,(1 / 4)] \cup[(3 / 4), 1]$. Then we know $T_{0}=\min \left\{t \mid \mid p_{t}-\right.$ $(1 / 2) \mid \geq(1 / 4)\}$. Hence, via taking $T=\mu /\left(32 \rho^{2}\right)$ for PBIL and $T=K^{2} / 32$ for the cGA in Theorem 2, we could easily obtain the expected hitting time, as shown in Corollary 1.

Corollary 1: Consider using an $n$-Bernoulli- $\lambda$-EDA to optimize some function $f$ with a neutral bit position. Let $T_{0}$ denote the first time the frequency of the neutral bit position is in $[0,(1 / 4)] \cup[(3 / 4), 1]$. For PBIL, we have $E\left[T_{0}\right]=\Omega\left(\mu / \rho^{2}\right)$, in particular, $E\left[T_{0}\right]=\Omega(\mu)$ for the UMDA
and $E\left[T_{0}\right]=\Omega\left(1 / \rho^{2}\right)$ for the $\lambda$-MMAS. For the cGA, we have $E\left[T_{0}\right]=\Omega\left(K^{2}\right)$.

We note that the lower bound proof for PBIL can be extended to CE, either by simply replacing $\rho$ by the supremum $\rho_{\text {sup }}=\sup \left\{\rho_{t} \mid t \in \mathbb{N}\right\}$ and obtaining a lower bound of $\Omega\left(\mu / \rho_{\text {sup }}^{2}\right)$, or by replacing $t \rho^{2}$ in (5) by $\sum_{t=1}^{t} \rho_{t}^{2}$. With a suitable choice of $t$, this gives a bound taking into account the particular values of $\left(\rho_{t}\right)$. We omit the details.

## V. Upper Bounds on the Boundary Hitting Time

We now prove that, roughly speaking, the lower bounds shown in the previous section are asymptotically tight. To prove our upper bounds, we use the following two lemmas.

Lemma 1: For all $z \geq 0$ and $z_{0}>0$, we have

$$
\begin{aligned}
\sqrt{z} \leq & \sqrt{z_{0}}+\frac{1}{2} z_{0}^{-1 / 2}\left(z-z_{0}\right)-\frac{1}{8} z_{0}^{-3 / 2}\left(z-z_{0}\right)^{2} \\
& +\frac{1}{16} z_{0}^{-5 / 2}\left(z-z_{0}\right)^{3}
\end{aligned}
$$

Proof: For the convenience of the proof, let $x=\sqrt{z}$ and $a=\sqrt{z_{0}}$. We consider the function

$$
\begin{aligned}
g(x)= & x-a-\frac{1}{2} a^{-1}\left(x^{2}-a^{2}\right)+\frac{1}{8} a^{-3}\left(x^{2}-a^{2}\right)^{2} \\
& -\frac{1}{16} a^{-5}\left(x^{2}-a^{2}\right)^{3} \\
= & -\frac{1}{16} a^{-5} x^{6}+\frac{5}{16} a^{-3} x^{4}-\frac{15}{16} a^{-1} x^{2}+x-\frac{5}{16} a
\end{aligned}
$$

and show that $g(x) \leq 0$. Since

$$
g^{\prime}(x)=-\frac{3}{8} a^{-5} x^{5}+\frac{5}{4} a^{-3} x^{3}-\frac{15}{8} a^{-1} x+1
$$

and

$$
\begin{aligned}
g^{\prime \prime}(x) & =-\frac{15}{8} a^{-5} x^{4}+\frac{15}{4} a^{-3} x^{2}-\frac{15}{8} a^{-1} \\
& =-\frac{15}{8} a^{-5}\left(x^{4}-2 a^{2} x^{2}+a^{4}\right) \\
& =-\frac{15}{8} a^{-5}\left(x^{2}-a^{2}\right)^{2} \leq 0
\end{aligned}
$$

we know that $g^{\prime}(x)$ is monotonically decreasing. Since $g^{\prime}(0)=1$ and $g^{\prime}(a)=0$, we observe that $g(x)$ increases in $[0, a)$ and decreases in $[a, \infty)$. Therefore, $g(x) \leq g(a)=0$.

An easy calculation gives the following second-order and third-order central moments of the frequency of the neutral bit position in PBIL and the cGA.

Lemma 2: For PBIL, we have

$$
\begin{aligned}
& \operatorname{Var}\left[p_{t} \mid p_{t-1}\right]=\frac{\rho^{2}}{\mu} p_{t-1}\left(1-p_{t-1}\right) \\
& E\left[\left(p_{t}-E\left[p_{t} \mid p_{t-1}\right]\right)^{3} \mid p_{t-1}\right] \\
& =\frac{\rho^{3}}{\mu^{2}} p_{t-1}\left(1-p_{t-1}\right)\left(1-2 p_{t-1}\right)
\end{aligned}
$$

For the cGA, we have

$$
\begin{aligned}
& \operatorname{Var}\left[p_{t} \mid p_{t-1}\right]=\frac{2}{K^{2}} p_{t-1}\left(1-p_{t-1}\right) \\
& E\left[\left(p_{t}-E\left[p_{t} \mid p_{t-1}\right]\right)^{3} \mid p_{t-1}\right]=0
\end{aligned}
$$

Proof: For PBIL, note that $\sum_{i=1}^{\mu} X_{i, 1}^{t} \sim \operatorname{Bin}\left(\mu, p_{t-1}\right)$. Thus we have

$$
\begin{aligned}
& \operatorname{Var}\left[\sum_{i=1}^{\mu} X_{i, 1}^{t} \mid p_{t-1}\right]=\mu p_{t-1}\left(1-p_{t-1}\right) \\
& E\left[\left(\sum_{i=1}^{\mu} X_{i, 1}^{t}-E\left[\sum_{i=1}^{\mu} X_{i, 1}^{t} \mid p_{t-1}\right]\right)^{3} \mid p_{t-1}\right] \\
& =\mu p_{t-1}\left(1-p_{t-1}\right)\left(1-2 p_{t-1}\right)
\end{aligned}
$$

Hence, recalling that $p_{t}=(1-\rho) p_{t-1}+(\rho / \mu) \sum_{i=1}^{\mu} X_{i, 1}^{t}$, and noting that centered moments are invariant to translations with constants and that constant scaling factors can be pulled out in the corresponding power, we have

$$
\begin{aligned}
\operatorname{Var}\left[p_{t} \mid p_{t-1}\right] & =\left(\frac{\rho}{\mu}\right)^{2} \operatorname{Var}\left[\sum_{i=1}^{\mu} X_{i, 1}^{t} \mid p_{t-1}\right] \\
& =\frac{\rho^{2}}{\mu} p_{t-1}\left(1-p_{t-1}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
& E\left[\left(p_{t}-E\left[p_{t} \mid p_{t-1}\right]\right)^{3} \mid p_{t-1}\right] \\
& \quad=\left(\frac{\rho}{\mu}\right)^{3} E\left[\left(\sum_{i=1}^{\mu} X_{i, 1}^{t}-E\left[\sum_{i=1}^{\mu} X_{i, 1}^{t} \mid p_{t-1}\right]\right)^{3} \mid p_{t-1}\right] \\
& \quad=\frac{\rho^{3}}{\mu^{2}} p_{t-1}\left(1-p_{t-1}\right)\left(1-2 p_{t-1}\right)
\end{aligned}
$$

For the cGA, we compute

$$
\begin{aligned}
\operatorname{Var}\left[p_{t} \mid p_{t-1}\right]= & E\left[\left(p_{t}-E\left[p_{t} \mid p_{t-1}\right]\right)^{2} \mid p_{t-1}\right] \\
= & p_{t-1}\left(1-p_{t-1}\right)\left(\frac{1}{K}\right)^{2} \\
& +p_{t-1}\left(1-p_{t-1}\right)\left(-\frac{1}{K}\right)^{2} \\
= & \frac{2}{K^{2}} p_{t-1}\left(1-p_{t-1}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
& E\left[\left(p_{t}-E\left[p_{t} \mid p_{t-1}\right]\right)^{3} \mid p_{t-1}\right] \\
& \quad=p_{t-1}\left(1-p_{t-1}\right)\left(\frac{1}{K}\right)^{3}+p_{t-1}\left(1-p_{t-1}\right)\left(-\frac{1}{K}\right)^{3}=0
\end{aligned}
$$

We are now ready to prove the following upper bounds for the hitting time of the absorbing states of the frequency of a neutral bit position. We consider EDAs without margins here, but since the time to reach an absorbing state is not smaller than the time to reach a margin value, we know that an upper bound on the hitting time of the absorbing states is also an upper bound for the time to hit a margin value when margins are used.

Theorem 3: Consider using an $n$-Bernoulli- $\lambda$-EDA to optimize some function $f$ with a neutral bit position.

1) If the EDA is PBIL with $\rho<1$, including the case of the $\lambda$-MMAS, then the following holds. Let $c \in$
$([1 / 2],[1 / \sqrt{2}])$. We say that the frequency $p_{t}$ of the neutral bit position runs away from time $t$ onward if:
a) $p_{t} \leq c(\rho / \mu)$ and in all iterations $t^{\prime}>t$ all samples have a zero in the neutral bit position;
b) $p_{t} \geq 1-c(\rho / \mu)$ and in all iterations $t^{\prime}>t$ all samples have a one in the neutral bit position.
For $\tilde{T}$ denoting the first $t$ such that $p_{t}$ runs away from time $t$ on, we have $E[\tilde{T}]=O\left(\mu / \rho^{2}\right)$.
2) If the EDA is the UMDA, that is, PBIL with $\rho=1$, then the first hitting time $T$ of the absorbing states $[0,1]$ satisfies $E[T]=O(\mu)$.
3) For the cGA, the expected first time to reach an absorbing state satisfies $E[T]=O\left(K^{2}\right)$.
Proof: Let $q_{t}=\min \left\{p_{t}, 1-p_{t}\right\}$ and $Y_{t}=\sqrt{q_{t}}$. Then $T=\min \left\{t \mid q_{t}=0\right\}$ and $\tilde{T}=\min \left\{t \mid q_{t} \leq c(\rho / \mu)\right\}$. Due to the symmetry, we just discuss the case when $q_{t-1}=p_{t-1}$. Obviously, $p_{t-1} \leq(1 / 2)$ in this case. Let us assume that $p_{t-1}>c(\rho / \mu)$. Using Lemma 1 with $z=p_{t}$ and $z_{0}=p_{t-1}$, we have

$$
\begin{aligned}
E\left[\sqrt{p_{t}} \mid p_{t-1}\right] \leq & E\left[Y_{t-1} \mid p_{t-1}\right]+\frac{1}{2} p_{t-1}^{-1 / 2} E\left[p_{t}-p_{t-1} \mid p_{t-1}\right] \\
& -\frac{1}{8} p_{t-1}^{-3 / 2} E\left[\left(p_{t}-p_{t-1}\right)^{2} \mid p_{t-1}\right] \\
& +\frac{1}{16} p_{t-1}^{-5 / 2} E\left[\left(p_{t}-p_{t-1}\right)^{3} \mid p_{t-1}\right]
\end{aligned}
$$

and thus

$$
\begin{aligned}
E\left[Y_{t-1}-\sqrt{p_{t}} \mid Y_{t-1}\right] \geq & -\frac{1}{2} p_{t-1}^{-1 / 2} E\left[p_{t}-p_{t-1} \mid p_{t-1}\right] \\
& +\frac{1}{8} p_{t-1}^{-3 / 2} E\left[\left(p_{t}-p_{t-1}\right)^{2} \mid p_{t-1}\right] \\
& -\frac{1}{16} p_{t-1}^{-5 / 2} E\left[\left(p_{t}-p_{t-1}\right)^{3} \mid p_{t-1}\right]
\end{aligned}
$$

We analyze PBIL first, which includes the UMDA. We start by showing that, regardless of $p_{0}$, the expected time to reach $p_{t} \in P:=[0, c \rho / \mu] \cup\left\{1-c \rho / \mu, 1\right\}$ is $O\left(\mu / \rho^{2}\right)$. Via Lemma 7, we have

$$
\begin{aligned}
E\left[Y_{t-1}-\sqrt{p_{t}} \mid Y_{t-1}\right] \geq & \frac{1}{8} p_{t-1}^{-3 / 2} \frac{\rho^{2}}{\mu} p_{t-1}\left(1-p_{t-1}\right) \\
& -\frac{1}{16} p_{t-1}^{-5 / 2} \frac{\rho^{3}}{\mu^{2}} p_{t-1}\left(1-p_{t-1}\right) \\
& \times\left(1-2 p_{t-1}\right) \\
= & \frac{\rho^{2}}{16 \mu} p_{t-1}^{-1 / 2}\left(1-p_{t-1}\right) \\
& \times\left(2-\frac{\rho}{\mu p_{t-1}}\left(1-2 p_{t-1}\right)\right) \\
\geq & \frac{\rho^{2}}{16 \mu} p_{t-1}^{-1 / 2}\left(1-p_{t-1}\right)\left(2-\frac{1}{c}\right)
\end{aligned}
$$

where the last estimate follows from $p_{t-1} \geq c \rho / \mu$ and from the fact that $0<p_{t-1} \leq(1 / 2)$ implies $0 \leq 1-2 p_{t-1}<1$. Since $p_{t-1} \leq(1 / 2)$, we have $p_{t-1}^{-1 / 2}\left(1-p_{t-1}\right) \geq(\sqrt{2} / 2)$. Hence, $E\left[Y_{t-1}-\sqrt{p_{t}} \mid Y_{t-1}\right] \geq c_{1} \rho^{2} / \mu$, where $c_{1}=$ $(\sqrt{2} / 32)(2-(1 / c))$. Using $q_{t}=\min \left\{p_{t}, 1-p_{t}\right\}$, we have

$$
E\left[Y_{t-1}-Y_{t} \mid Y_{t-1}\right] \geq E\left[Y_{t-1}-\sqrt{p_{t}} \mid Y_{t-1}\right] \geq c_{1} \rho^{2} / \mu
$$

By artificially modifying the process $\left(Y_{t}\right)$ once it goes below $c \rho / \mu$, e.g., by defining $\left(\tilde{Y}_{t}\right)$ via $\tilde{Y}_{t}=Y_{t}$ if $Y_{t} \geq c \rho / \mu$

and $\bar{Y}_{t}=0$, otherwise, we can ensure that we have a drift of $E\left[\bar{Y}_{t-1}-Y_{t} \mid Y_{t-1}>0\right] \geq c_{1} \rho^{2} / \mu$ until we reach zero. Such an artificial extension of a process beyond the region of interest, to the best of our knowledge, was in the theory of EAs first used in [25]. With this artificial extension we can now use the additive drift theorem [22] with target $\bar{Y}_{t}=0$ and $\bar{Y}_{0}=\sqrt{(1 / 2)}$ and obtain that the expected time for the $\bar{Y}$-process to reach or go below $\sqrt{c \rho / \mu}$, equivalently to the $p_{t}$ process reaching $P$, is at most $\left[\left(\bar{Y}_{0} / c_{1} \rho^{2} / \mu\right)\right]=[16 /(2-1 / c)] \mu / \rho^{2}=O\left(\mu / \rho^{2}\right)$. We note here that for the UMDA, that is, PBIL with $\rho=1$, the $p_{t}$ process reaching $P$ hits the absorbing states $\{0,1\}$ since $c \rho / \mu=c / \mu<1 / \mu$ and the frequencies are well-behaved. Hence, we have $E[T]=O(\mu)$ for the UMDA.

Now, we continue to discuss the neutral frequency's behavior of PBIL once it has reached $P$. W.l.o.g. let $p_{t} \leq c \rho / \mu$. Then the probability that all of the next $\mu\lceil 1 / \rho\rceil$ samplings have a zero in the neutral bit position is at least

$$
\begin{aligned}
\left(1-p_{t}\right)^{\mu\lceil 1 / \rho\rceil} & \geq\left(1-\frac{c \rho}{\mu}\right)^{\mu\lceil 1 / \rho\rceil} \\
& \geq\left(1-\frac{c \rho}{\mu}\right)^{\mu \frac{2}{\rho}} \\
& =\left(1-\frac{c \rho}{\mu}\right)^{2 c\left(\frac{\rho}{c \rho}-1\right)}\left(1-\frac{c \rho}{\mu}\right)^{2 c} \\
& \geq \exp (-2 c)\left(1-2 c \frac{c \rho}{\mu}\right) \\
& \geq \exp (-2 c)\left(1-2 c^{2}\right)>0
\end{aligned}
$$

where the second inequality uses $\lceil 1 / \rho\rceil \leq 2 / \rho$ since $\rho \leq 1$, the antepenultimate inequality uses the Bernoulli's inequality, the penultimate inequality uses $\mu \geq 1$ and $\rho \leq 1$, and the last inequality uses $c<1 / \sqrt{2}$. In this case, the frequency after these $\lceil 1 / \rho\rceil$ iterations is

$$
p_{t+\lceil 1 / \rho\rceil}=(1-\rho)^{\lceil 1 / \rho\rceil} p_{t} \leq(1-\rho)^{1 / \rho} p_{t} \leq \frac{p_{t}}{e} \leq \frac{c}{e} \frac{\rho}{\mu}
$$

Therefore, with a similar calculation, it is easy to see that the probability that all of the next $\mu\lceil 1 / \rho\rceil$ samplings have a zero in the neutral bit position [from the $\left.\left(t+\lceil 1 / \rho\rceil+1\right)\right)$ th iteration to the $\left.\left(t+2\lceil 1 / \rho\rceil\right)\right)$ th iteration] is at least $\left(\exp (-2 c)\left(1-2 c^{2}\right)\right)^{1 / e}$, and $p_{t+2 / \rho} \leq\left(c / e^{2}\right)(\rho / \mu)$. A simple induction gives that the probability that all samplings have a zero in the neutral bit position from the $\left.\left(t+(n-1)\lceil 1 / \rho\rceil+1\right)\right)$ th iteration to the $\left.\left(t+n\lceil 1 / \rho\rceil\right)\right)$ th iteration is at least $\left(\exp (-2 c)\left(1-2 c^{2}\right)\right)^{1 / e^{n-1}}$. Therefore, the probability that only zeros are sampled in the neutral bit position is at least

$$
\begin{aligned}
\prod_{t=0}^{\infty}\left(\exp (-2 c)\left(1-2 c^{2}\right)\right)^{1 / e^{t}} & =\left(\exp (-2 c)\left(1-2 c^{2}\right)\right)^{\sum_{i=0}^{\infty} \frac{1}{e^{i}}} \\
& =\left(\exp (-2 c)\left(1-2 c^{2}\right)\right)^{1 /\left(1-e^{-1}\right)} \\
& >0
\end{aligned}
$$

where the last inequality uses $\exp (-2 c)\left(1-2 c^{2}\right)>0$.
Let us divide the run of the EDA into phases. The first phase starts with the first iteration, each subsequent phase starts with
the iteration following the end of the previous phase. A phase ends when for the first time after reaching in this phase a $p_{t^{-}}$ value in $P$ an unexpected value is sampled in the neutral bit position. That is, when a one is sampled if the first $p_{t}$-value in $P$ is in $[0, c(\rho / \mu)]$ or when a zero is sampled when the first $p_{t}$-value is at least $1-c(\rho / \mu)$. By the above, we know the following about these phases. We call a phase successful when it never samples the unexpected value, thus it will not end. From the above calculation, we know the success probability is at least $\left(\exp (-2 c)\left(1-2 c^{2}\right)\right)^{1 /\left(1-e^{-1}\right)}$, which is a positive constant. Consequently, there is an expected constant number of phases, one of which is successful (namely the last). In each phase, successful or not, it takes an expected time of $O\left(\mu / \rho^{2}\right)$ until the frequency of the neutral bit position reaches a value in $P$. In the successful phase, the frequency then runs away. For the unsuccessful phases, we now show that the phase ends after an expected number of additional $O(1 / \rho)$ iterations after reaching a frequency value in $P$.

Note that this means analyzing a run of the algorithm starting (in iteration $t+1$ ) with the neutral frequency $p_{t}$ in $P$, say w.l.o.g. in $[0, c(\rho / \mu)]$, conditional on the event that at some future time a one is sampled in this position.

Let $U$ be the event that the phase under investigation is unsuccessful. Let $X \in\{1,2, \ldots\}$ be minimal such that in iteration $t+X$ a one is sampled in the neutral bit position of a selected individual. Conditional on $U$, the random variable $X$ is well-defined (that is, finite). For $X=s$ to hold, in particular no one can be sampled in the iterations $t+1, \ldots, t+(s-1)$, and this implies not sampling a one in iteration $t+(s-1)$ when the current value of the frequency is $p_{t}(1-\rho)^{s-1}$. Consequently, the expected length (number of iterations) of an unsuccessful phase is

$$
\begin{aligned}
E[X \mid U] & =\sum_{s=1}^{\infty} s \operatorname{Pr}[X=s \mid U]=\frac{1}{\operatorname{Pr}[U]} \sum_{s=1}^{\infty} s \operatorname{Pr}[X=s] \\
& \leq \frac{1}{\operatorname{Pr}[U]} \sum_{s=1}^{\infty} s \mu p_{t}(1-\rho)^{(s-1)}
\end{aligned}
$$

using a union bound over the $\mu$ samples in iteration $t+(s-1)$.
To estimate this expectation, we first compute $\operatorname{Pr}[U]$. For any $k \in \mathbb{N}$, we have

$$
\begin{aligned}
\operatorname{Pr}[U] & \geq \operatorname{Pr}[X \leq k]=1-\operatorname{Pr}[X>k] \\
& =1-\prod_{i=1}^{k} \operatorname{Pr}[X>i \mid X>i-1] \\
& =1-\prod_{i=0}^{k-1}\left(1-p_{t}(1-\rho)^{i}\right)^{\mu} \\
& \geq 1-\exp \left(-\mu p_{t} \sum_{i=0}^{k-1}(1-\rho)^{i}\right) \\
& =1-\exp \left(-\mu p_{t} \frac{1-(1-\rho)^{k}}{1-(1-\rho)}\right) \\
& \geq 1-\left(1-\frac{1}{2} \mu p_{t} \frac{1-(1-\rho)^{k}}{\rho}\right)=\mu p_{t} \frac{1-(1-\rho)^{k}}{2 \rho}
\end{aligned}
$$

using the well-known estimates $1+x \leq \exp (x)$ valid for all $x \in \mathbb{R}$ and $\exp (-x) \leq 1-(x / 2)$ valid for all $0 \leq x \leq 1$. Taking the supremum over all $k \in \mathbb{N}$, we obtain $\operatorname{Pr}\{U\} \geq\left(\mu p_{t} / 2 \rho\right)$.

To estimate the infinite sum in (9), we first recall the elementary formula $\sum_{s=1}^{\infty} s x^{s}=\left[x /\left((1-x)^{2}\right)\right]$ for $0<x<1$, which follows from computing $A:=\sum_{s=1}^{\infty} s x^{s}=x \sum_{s=1}^{\infty}(s-$ 1) $x^{s-1}+\sum_{s=1}^{\infty} x^{s}=x A+[x /(1-x)]$ and solving for $A$. From this, we obtain

$$
\sum_{s=1}^{\infty} s \mu p_{t}(1-\rho)^{(s-1)}=\mu p_{t} \frac{1}{\rho^{2}}
$$

and finally

$$
E[X \mid U] \leq \frac{\mu p_{t} \frac{1}{\rho^{2}}}{\frac{\mu p_{t}}{2 \rho}}=\frac{2}{\rho}
$$

Consequently, an unsuccessful phase in total takes an expected number of $O\left(\mu / \rho^{2}\right)+O(1 / \rho)=O\left(\mu / \rho^{2}\right)$ iterations.

By Wald's equation, recalling that we have an expected constant number of unsuccessful iterations, we see that the total time until the frequency of the neutral bit position runs away is $O\left(\mu / \rho^{2}\right)$ iterations.

For the cGA, in a similar manner as in the first part of the analysis for PBIL, by Lemma 7, (7) becomes

$$
\begin{aligned}
E\left[Y_{t-1}-\sqrt{p_{t}} \mid Y_{t-1}\right] & \geq \frac{1}{8} p_{t-1}^{-3 / 2} \frac{2}{K^{2}} p_{t-1}\left(1-p_{t-1}\right) \\
& =\frac{1}{4} p_{t-1}^{-1 / 2} \frac{1-p_{t-1}}{K^{2}} \geq \frac{1}{4} \frac{\sqrt{2}}{2} \frac{1}{K^{2}} \\
& =\frac{\sqrt{2}}{8} \frac{1}{K^{2}}
\end{aligned}
$$

Hence,

$$
E\left[Y_{t-1}-Y_{t} \mid Y_{t-1}\right] \geq E\left[Y_{t-1}-\sqrt{p_{t}} \mid Y_{t-1}\right] \geq \frac{\sqrt{2}}{8} / K^{2}
$$

Via the Additive Drift Theorem [22] and $Y_{0}=\sqrt{(1 / 2)}$, we know that the expected time for the $Y$-process to reach zero is at most $\left.Y_{0} /\left[\sqrt{2} /\left(8 K^{2}\right)\right]=4 K^{2}\right.$.

We now briefly show that the upper bound proof can, under suitable assumptions, also be applied to CE with small modifications. Assume that the learning rate sequence $\left(\rho_{t}\right)$ has both supremum and infimum, and let $\rho_{\text {sup }}=\sup \left\{\rho_{t} \mid t \in \mathbb{N}\right\}$ and $\rho_{\text {inf }}=\inf \left\{\rho_{t} \mid t \in \mathbb{N}\right\}$. Consider the first generation when the frequency reaches $\bar{P}:=\left[0, c \rho_{\text {sup }} / \mu\right] \cup\left[1-c \rho_{\text {sup }} / \mu, 1\right]$. Following similar arguments as above, we can obtain that the corresponding value in the right side of (8) becomes $c_{1} \rho_{\text {inf }}^{2} / \mu$, and hence the expected reaching time is $O\left(\mu / \rho_{\text {inf }}^{2}\right)$.

For the neutral frequency's behavior once it has reached $P$, we discuss the case when there exists a positive constant $c^{\prime}<2$ so that $\rho_{\text {sup }} / \rho_{\text {inf }} \leq c^{\prime}$. In this case, we refine $c \in$ $\left(1 / 2, \sqrt{1 /\left(2 c^{\prime}\right)}\right)$. Then we can obtain that the probability that all samplings have a zero in the neutral bit position from the $\left(t+i\left\lceil 1 / \rho_{\text {inf }}\right\rceil+1\right)$ th iteration to the $\left(t+(i+1)\left\lceil 1 / \rho_{\text {inf }}\right\rceil\right)$ th iteration is at least

$$
\begin{aligned}
& \left(\exp \left(-\frac{2 c \rho_{\text {sup }}}{\rho_{\text {inf }}}\right)\left(1-\frac{2 c^{2} \rho_{\text {sup }}^{2}}{\rho_{\text {inf }}}\right)\right)^{1 / e^{i}} \\
& \geq\left(\exp \left(-2 c c^{\prime}\right)\left(1-2 c^{2} c^{\prime}\right)\right)^{1 / e^{i}}>0
\end{aligned}
$$

for $i=0,1, \ldots$, and the frequency after these $\left\lceil 1 / \rho_{\text {inf }}\right\rceil$ iterations is at most $c \rho_{\text {sup }} /\left(e^{i+1} \mu\right)$. Hence, the probability that only zeros are sampled in the neutral bit position is at least

$$
\left(\exp \left(-2 c c^{\prime}\right)\left(1-2 c^{2} c^{\prime}\right)\right)^{1 /\left(1-e^{-1}\right)}>0
$$

Similarly, we could calculate that an unsuccessful phase ends after an expected number of additional $O\left(\rho_{\text {sup }} / \rho_{\text {inf }}^{2}\right)$ iterations after reaching a frequency value in $\bar{P}$. Hence, for CE, the total time until the frequency of the neutral bit position runs away is $O\left(\mu / \rho_{\text {inf }}^{2}\right)$ iterations.

We note that Corollary 1 and Theorem 3 give sharp bounds for several hitting times. For the UMDA without margins, the expected first time when the frequency of the neutral bit position is absorbed in 0 or 1 is $\Theta(\mu)$, and the corresponding hitting time is $\Theta\left(K^{2}\right)$ for the cGA. For PBIL without margins and any $c \in(1 / 2,1 / \sqrt{2})$, the expected first time that the frequency of the neutral bit position hits $c \rho / \mu$ or $1-c \rho / \mu$ is $\Theta\left(\mu / \rho^{2}\right)$. As discussed in the second paragraph in Section II, these results also hold for the hitting time of the margins $\{1 / D, 1-1 / D\}$ when running EDAs with such margins.

## VI. Extending the Lower Bounds to Bit Positions With Preference: Domination Results

In the previous Sections IV and V, we discussed how fast neutral bit positions approach the boundaries of the frequency range. In many situations, e.g., for the benchmark functions OnEMAX or LEAdingONES, bit positions are not neutral, but are neutral or have a preference of one bit-value (here the value one). Precisely, we say some bit position, w.l.o.g., the first bit position, of the fitness function $f$ is neutral or prefers a one (we also say weakly prefers a one) if and only if

$$
f\left(0, X_{2}, \ldots, X_{D}\right) \leq f\left(1, X_{2}, \ldots, X_{D}\right)
$$

for all $X_{2}, \ldots, X_{D} \in\{0,1\}$. We say that the bit position weakly prefers a zero if $f\left(0, X_{2}, \ldots, X_{D}\right) \geq f\left(1, X_{2}, \ldots, X_{D}\right)$ for all $X_{2}, \ldots, X_{D} \in\{0,1\}$.

If seems natural that for a bit that weakly prefers a one, the time for its frequency to reach or go below a certain value satisfies the same lower bounds as proven for neutral bit positions, and an analogous statement should be true for bits that weakly prefer a zero. This is what we show in this section.

To prove this result, we first establish the following dominance result, which we expect to be useful also beyond this article. It, in particular, shows that when comparing two runs of an EDA, the first one starting with a higher frequency in a neutral bit position than the second, then in the next generation the frequency in the first run stochastically dominates the one in the second run. This statement remains true if the position in the first run is not neutral, but weakly prefers ones. A simple induction extends this statement to all generations. While not important for this article, we add that we believe that the lemma below does not remain true when both functions can be such that the first bit weakly prefers a one, since other bits' contributions to the fitness should be considered as well. Also, simple examples show that our claim is false for the cGA without well-behaved frequencies.

Lemma 3: Consider using an $n$-Bernoulli- $\lambda$-EDA to optimize: 1) some function $f$ such that the first bit weakly prefers a one and 2) some function $g$ with the first bit being neutral. Assume that the first process is started with a frequency vector $u^{0}$ and the second with a frequency vector $v^{0}$ such that $u_{i}^{0}=v_{i}^{0}$ for $i=2, \ldots, D$, and $u_{1}^{0} \geq v_{1}^{0}$. Assume that in the case of the cGA, the well-behaved frequency assumption holds.

Let $u^{t}$ and $v^{t}$ be the corresponding frequency vectors generated in the $t$-th generation. Then $u_{1}^{t} \succeq v_{1}^{t}$ for all $t \in \mathbb{N}$.

Analogously, if $f$ is such that the first bit weakly prefers a zero and we start with $u_{1}^{0} \leq v_{1}^{0}$, then $u_{1}^{t} \preceq v_{1}^{t}$ for all $t \in \mathbb{N}$.

Proof: We only show the result for the weak preference of a one as the other statement can be shown in an analogous fashion or by regarding $(-f,-g, 1-u, 1-v)$ instead of $(f, g, u, v)$.

We first show the claim for the first iteration and later argue that an easy induction shows it for any time $t$.

For PBIL (or CE), we recall from Section III that in the second process in an iteration $t$ started with a frequency $v_{1}^{t-1}$ of the neutral first bit of $g$, the next frequency of this neutral position is distributed as

$$
(1-\rho) v_{1}^{t-1}+\rho \frac{1}{\mu} Y
$$

where $Y \sim \operatorname{Bin}\left(\mu, v_{1}^{t-1}\right)$. In the first process, a closer inspection of the update rule (1) shows the frequency of the position weakly preferring a one changes from $u_{1}^{t-1}$ to

$$
u_{1}^{t} \sim(1-\rho) u_{1}^{t-1}+\rho \frac{1}{\mu} X
$$

where $X \succeq \operatorname{Bin}\left(\mu, v_{1}^{t-1}\right)$.
If $u_{1}^{0} \geq v_{1}^{0}$, then $\operatorname{Bin}\left(\mu, u_{1}^{0}\right)$ stochastically dominates $\operatorname{Bin}\left(\mu, v_{1}^{0}\right)$, and hence $u_{1}^{t} \succeq v_{1}^{t}$ by (10) and (11).

For the cGA with the well-behaved frequency assumption, we note that $u_{1}^{0} \geq v_{1}^{0}$ implies $u_{1}^{0}=v_{1}^{0}$ or $u_{1}^{0} \geq v_{1}^{0}+1 / K$. We only regard the latter, more interesting case. We show $u_{1}^{1} \succeq v_{1}^{1}$ using the definition of domination, that is, that $\operatorname{Pr}\left[u_{1}^{1} \leq \lambda\right] \leq \operatorname{Pr}\left[v_{1}^{1} \leq \lambda\right]$ holds for all $\lambda \in \mathbb{R}$. We discuss differently the following three cases.

1) Assume $\lambda<v_{1}^{0}$. Since $u_{1}^{0}-1 / K \geq v_{1}^{0}>\lambda$ from our assumption, we have $\operatorname{Pr}\left[u_{1}^{1} \leq \lambda\right]=0 \leq \operatorname{Pr}\left[v_{1}^{1} \leq \lambda\right]$.
2) Assume $v_{1}^{0} \leq \lambda<u_{1}^{0}$. In this case, $\operatorname{Pr}\left[u_{1}^{1} \leq \lambda\right] \leq u_{1}^{0}(1-$ $\left.u_{1}^{0}\right) \leq(1 / 4)$ and $\operatorname{Pr}\left[v_{1}^{1} \leq \lambda\right]=1-v_{1}^{0}\left(1-v_{1}^{0}\right) \geq 1-(1 / 4)$, which gives the claim.
3) Assume $\lambda \geq u_{1}^{0}$. Since $v_{1}^{0}+1 / K \leq u_{1}^{0} \leq \lambda$ from our assumption, we have $\operatorname{Pr}\left[v_{1}^{1} \leq \lambda\right]=1 \geq \operatorname{Pr}\left[u_{1}^{1} \leq \lambda\right]$.
Hence, we have $u_{1}^{t} \succeq v_{1}^{t}$.
To extend our proof to arbitrary generation $t$, we note that if we have $u_{1}^{t-1} \succeq v_{1}^{t-1}$, then (see e.g., [26, Th. 12]) we can find a coupling of the two probability spaces describing the states of the two algorithms at the start of iteration $t$ in such a way that for any point $\omega$ in the coupling probability space we have $u_{1}^{t-1} \geq v_{1}^{t-1}$. Conditional on this $\omega$, we can use the above argument for one iteration and obtain $u_{1}^{t} \succeq v_{1}^{t}$. This implies that we also have $u_{1}^{t} \succeq v_{1}^{t}$ without conditioning on an $\omega$.

From Lemma 3, we now easily derive that our lower bounds shown in Section IV, suitably adjusted, also hold for bits that
weakly prefer one value. Theorem 4 discusses the case when a bit weakly prefers a one.

Theorem 4: Consider using an $n$-Bernoulli- $\lambda$-EDA to optimize some function $f$ with a bit weakly preferring a one. Let $p_{t}, t=0,1,2, \ldots$, denote the frequency of this position after iteration $t$. Let $T_{0}=\min \left\{t \mid p_{t} \leq(1 / 4)\right\}$ denote the first time this frequency is in $[0,(1 / 4)]$.

1) Let the EDA be PBIL with learning rate $\rho$ and selection size $\mu$. Then $E\left[T_{0}\right]=\Omega\left(\mu / \rho^{2}\right)$, in particular, $E\left[T_{0}\right]=$ $\Omega(\mu)$ for the UMDA and $E\left[T_{0}\right]=\Omega\left(1 / \rho^{2}\right)$ for the $\lambda$ MMAS. Again for PBIL, for all $\gamma>0$ and $T \in \mathbb{N}$ we have

$$
\operatorname{Pr}\left[\forall t \in\left[0 . . T\right]: p_{t}>\frac{1}{2}-\gamma\right] \geq 1-2 \exp \left(-\frac{\gamma^{2} \mu}{2 \rho^{2} T}\right)
$$

2) Let the EDA be the cGA with hypothetical population size $K$. Then $E\left[T_{0}\right]=\Omega\left(K^{2}\right)$ and for all $\gamma>0$ and $T \in \mathbb{N}$ we have

$$
\operatorname{Pr}\left[\forall t \in\left[0 . . T\right]: p_{t}>\frac{1}{2}-\gamma\right] \geq 1-2 \exp \left(-\frac{\gamma^{2} K^{2}}{2 T}\right)
$$

Proof: Let $g$ be some function with first bit position truly neutral, let $\tilde{p}_{t}, t=0,1,2, \ldots$, denote the frequency of this position after iteration $t$, and let $\tilde{T}_{0}=\min \left\{t \mid \tilde{p}_{t} \leq \frac{1}{4}\right\}$ denote the first time this frequency is in $[(0,(1 / 4)]$. Noting that $\tilde{p}_{0}=$ $p_{0}=(1 / 2)$, we apply Lemma 3 and observe that $p_{t} \succeq \tilde{p}_{t}$ for all $t$. This together with Theorem 2 shows the tail bounds.

From $p_{t} \succeq \tilde{p}_{t}$ for all $t$, we also deduce $T_{0} \succeq \tilde{T}_{0} \succeq \min \left\{t \mid\right.$ $\left.p_{t} \in[0,(1 / 4)] \cup[(3 / 4), 1]\right]=: T_{0}$ and thus $E\left[T_{0}\right] \geq E\left[T_{0}^{\prime}\right]$. By Corollary 1, $T_{0}^{\prime}$ satisfies the lower bounds we claim for the expectation of $T_{0}$, and so does $T_{0}$ itself.

In an analogous fashion, we obtain Corollary 2 the corresponding result for bits weakly preferring a zero.

Corollary 2: Consider using an $n$-Bernoulli- $\lambda$-EDA to optimize some function $f$ with a bit weakly preferring a zero. Let $p_{t}, t=0,1,2, \ldots$, denote the frequency of this position after iteration $t$. Let $T_{0}=\min \left\{t \mid p_{t} \geq(3 / 4)\right\}$ denote the first time this frequency is in $[(3 / 4), 1]$.

1) Let the EDA be PBIL with learning rate $\rho$ and selection size $\mu$. Then $E\left[T_{0}\right]=\Omega\left(\mu / \rho^{2}\right)$, in particular, $E\left[T_{0}\right]=$ $\Omega(\mu)$ for the UMDA and $E\left[T_{0}\right]=\Omega\left(1 / \rho^{2}\right)$ for the $\lambda$-MMAS. Again for PBIL, for all $\gamma>0$ and $T \in \mathbb{N}$ we have

$$
\operatorname{Pr}\left[\forall t \in\left[0 . . T\right]: p_{t}<\frac{1}{2}+\gamma\right] \geq 1-2 \exp \left(-\frac{\gamma^{2} \mu}{2 \rho^{2} T}\right)
$$

2) Let the EDA be the cGA with hypothetical population size $K$. Then $E\left[T_{0}\right]=\Omega\left(K^{2}\right)$ and for all $\gamma>0$ and $T \in \mathbb{N}$ we have

$$
\operatorname{Pr}\left[\forall t \in\left[0 . . T\right]: p_{t}<\frac{1}{2}+\gamma\right] \geq 1-2 \exp \left(-\frac{\gamma^{2} K^{2}}{2 T}\right)
$$

We have just extended our previous lower bounds to the case of bit positions preferring a particular value. One may ask whether similar results can be obtained for upper bounds as well. Let us comment on this question. Let us, as in Theorem 4 and its proof, denote by $p_{t}$ the frequencies of a position preferring a one and by $T_{0}$ the first time this frequency has reached or exceeded a particular value [e.g., $(3 / 4)$ or the upper boundary

of the frequency range]. Let us denote by $\tilde{p}_{t}$ and $\tilde{T}_{0}$ the corresponding random variables for a neutral bit position. Then again $p_{t} \succeq \tilde{p}_{t}$ implies $T_{0} \preceq \tilde{T}_{0}$, so (informally speaking or made precise via a coupling argument) $p_{t}$ reaches the target not later than $\tilde{p}_{t}$.
However, we do not have any good upper bounds on $\tilde{T}_{0}$, neither on its expectation nor in the domination sense. On the technical side, the reason is that we regarded the symmetric process $q_{t}=\min \left\{p_{t}, 1-p_{t}\right\}$ in Section V. The true reason is that also the process itself (when regarding a neutral bit position) is symmetric: with probability $(1 / 2)$ each, the first visit to a boundary is to $(1 / D)$ and to $1-(1 / D)$. However, if the first visit is to $(1 / D)$, then it takes quite some time to reach $1-(1 / D)$. Consequently, the distribution of the first hitting time of $1-(1 / D)$ is not well concentrated, and consequently, its expectation might be significantly larger than the first hitting time of $\{(1 / D), 1-(1 / D)\}$. For this reason, we currently do not see how our domination arguments allow to deduce from our results on neutral bit positions reasonable upper bounds on hitting times of frequencies of positions with weak preferences. However, we expect that in most situations where bits with weak preferences occur, one would rather try to exploit the preference to show stronger upper bounds than in the neutral case. For this reason, trying to retrieve information from the neutral case might not be too interesting anyway.

## VII. DisCUSSION

Just like classic EAs, EDAs are subject to genetic drift and this can, even when using margins for the frequency range, lead to a suboptimal performance.
For several classical EDAs, this article proved the first sharp estimates of the expected time the sampling frequency of a neutral bit position takes to leave the middle range $[(1 / 3),(3 / 4)]$ or to reach the boundaries. These times, roughly speaking, are $\Theta\left(K^{2}\right)$ iterations for the cGA and $\Theta\left(\mu / \rho^{2}\right)$ iterations for PBIL [and consequently $\Theta(\mu)$ for its special case UMDA].
These results are useful both to interpret existing performance results and to set the parameters right in future applications of EDAs. As an example of the former, we note that the recent work [27] shows that the UMDA with $c \log D \leq \mu=o(D), c$ a sufficiently large constant, with $\lambda \leq 71 \mu$, and with the margins $1 / D$ and $1-1 / D$, has a weak performance of $\exp (\Omega(\mu))$ on the $D$-dimensional DeceptiveLeadingBlocks benchmark function. This runtime is at least some unspecified, but most likely large polynomial in $D$; it is super-polynomial as soon as $\mu$ is chosen super-logarithmic. For this article, we know that the expected time for the frequency of a neutral bit position to reach the boundaries is only $O(\mu)$ iterations. Since the DeceptiveLeadingBlocks function, similar to the classic LeadingOnes function, has many bit positions that for a long time behave like neutral, a value of $\mu=o(D)$ results in that a constant fraction of these currently neutral bit positions will have reached the boundaries at least once within the first $D$ iterations. Hence also without looking at the proof of the result in [27], which indeed exploits the fact that frequencies
reach the margins to show the weak performance, our results already indicate that the weak performance might be caused by the use of parameter values leading to strong genetic drift.

For a practical use of EDAs, our tail bounds of Theorem 2 can be helpful. As a quick example, assume one wants to optimize some function via the cGA and one is willing to spend a computational budget of $F$ fitness evaluations. Since the cGA performs two fitness evaluations per iteration, this is equivalent to saying that we have a budget of $T=$ $F / 2$ iterations. From Theorem 2(b), with $\gamma=1 / 4$, and a simple union bound over the $D$ bit positions, we see that the probability that one of the (temporarily) neutral bit positions leaves the middle range $[(1 / 4),(3 / 4)]$ is at most $D \cdot 2 \exp \left(-\left[\left(\gamma^{2} K^{2}\right) / 2 T\right]\right)$. Consequently, by using a parameter value of $K \geq(1 / \gamma) \sqrt{F \ln (20 D)}$, we obtain that with probability at least $90 \%$ no neutral position leaves the middle range (and, with the results of Section VI, no position that weakly prefers one-bit value leaves the middle range into the opposite direction). Phrased differently, this means that within this time frame, only those positions approach the boundaries for which there is a sufficiently strong signal from the objective function. While this consideration cannot determine optimal parameters for each EDA and each objective function, it can at least prevent the user from taking parameters that are likely to give an inferior performance due to genetic drift. Since genetic drift has been shown to lead to a poor performance in the past, we strongly recommend to choose the parameters $K$ and $\mu$ large enough so that estimates based on Theorem 2 guarantee that positions without a fitness signal stay in the middle range.

## ACKNOWLEDGMENT

This work was supported by a public grant as part of the Investissement d'avenir project, reference ANR-11-LABX-0056-LMH, LabEx LMH, in a joint call with Gaspard Monge Program for optimization, operations research and their interactions with data sciences. The authors thank Guangwen Yang, Haohuan Fu, and Xin Yao for their valuable support of this article. A small subset of results presented in this work were already stated, without proof or proof idea, in the conference paper [1, Th. 4.5], namely that the expected time the frequency of a neutral bit position takes to hit the absorbing states 0 or 1 is $\Theta\left(K^{2}\right)$ for the cGA and $\Theta(\mu)$ for the UMDA. This article now extends the UMDA result to PBIL, strengthens all lower bounds by regarding the event of leaving the middle range $[1 / 4,3 / 4]$ of the frequency range, adds tail bounds for lower bounds, and adds domination arguments allowing to extend the lower bounds to positions that are neutral or prefer a particular value. Also, complete proofs are given for all results.

## REFERENCES

[1] W. Zheng, G. Yang, and B. Doerr, "Working principles of binary differential evolution," in Proc. Genet. Evol. Comput. Conf. (GECCO), 2018, pp. 1103-1110.
[2] J. S. De Bonet, C. L. Isbell Jr., and P. A. Viola, "Mimic: Finding optima by estimating probability densities," in Advances in Neural Information Processing Systems. Cambridge, MA, USA: MIT Press, 1996, pp. 424-430.

[3] M. Pelikan and H. Mühlenbein, "The bivariate marginal distribution algorithm," in Advances in Soft Computing, London, U.K.: Springer, 1999, pp. 521-535.
[4] H. Mühlenbein and T. Mahnig, "FDA - a scalable evolutionary algorithm for the optimization of additively decomposed functions," Evol. Comput., vol. 7, no. 4, pp. 353-376, Dec. 1999.
[5] G. R. Harik, F. G. Lobo, and K. Sastry, "Linkage learning via probabilistic modeling in the extended compact genetic algorithm (ECGA)," in Scalable Optimization via Probabilistic Modeling, Heidelberg, Germany: Springer, 2006, pp. 39-61. [Online]. Available: https://link.springer.com/ chapter/10.1007\%2F978-3-540-34954-9_3
[6] S. Baluja, "Population-based incremental learning: A method for integrating genetic search based function optimization and competitive learning," Dept. Comput. Sci., Carnegie Mellon Univ., Pittsburgh, PA, USA, Rep. CMU-CS-94-163, Jun. 1994.
[7] S. Baluja and R. Caruana, "Removing the genetics from the standard genetic algorithm," in Proc. Int. Conf. Mach. Learn. (ICML), 1995, pp. 38-46.
[8] H. Mühlenbein and G. Paass, "From recombination of genes to the estimation of distributions I. Binary parameters," in Proc. Int. Conf. Parallel Problem Solving Nat. (PPSN), 1996, pp. 178-187.
[9] F. Neumann, D. Sudholt, and C. Witt, "A few ants are enough: ACO with iteration-best update," in Proc. Annu. Genet. Evol. Comput. Conf. (GECCO), 2010, pp. 63-70.
[10] G. R. Harik, F. G. Lobo, and D. E. Goldberg, "The compact genetic algorithm," in Proc. IEEE Int. Conf. Evol. Comput. (ICEC), Anchorage, AK, USA, 1998, pp. 523-528.
[11] M. Krejca and C. Witt, "Theory of estimation-of-distribution algorithms," in Theory of Evolutionary Computation: Recent Developments in Discrete Optimization, B. Doerr and F. Neumann, Eds. Cham, Switzerland: Springer, 2020, pp. 405-442.
[12] K. Motoo, "Diffusion models in population genetics," J. Appl. Probab., vol. 1, no. 2, pp. 177-232, 1964.
[13] H. Asoh and H. Mühlenbein, "On the mean convergence time of evolutionary algorithms without selection and mutation," in Proc. Int. Conf. Parallel Problem Solving Nat. (PPSN), 1994, pp. 88-97.
[14] C. González, J. A. Lozano, and P. Larrahaga, "The convergence behavior of the PBIL algorithm: A preliminary approach," in Proc. Int. Conf. Artif. Neural Nets Genet. Algorithms (ICANNGA), 2001, pp. 228-231.
[15] S. Droste, "A rigorous analysis of the compact genetic algorithm for linear functions," Nat. Comput., vol. 5, pp. 257-283, Aug. 2006.
[16] A. Costa, O. D. Jones, and D. Kroese, "Convergence properties of the cross-entropy method for discrete optimization," Oper. Res. Lett., vol. 35, no. 5, pp. 573-580, 2007.
[17] C. Witt, "Upper bounds on the running time of the univariate marginal distribution algorithm on OneMax," Algorithmica, vol. 81, pp. 632-667, Feb. 2019.
[18] J. Lengler, D. Sudholt, and C. Witt, "Medium step sizes are harmful for the compact genetic algorithm," in Proc. Genet. Evol. Comput. Conf. (GECCO), 2018, pp. 1499-1506.
[19] T. Friedrich, T. Kötzing, and M. S. Krejca, "EDAs cannot be balanced and stable," in Proc. Genet. Evol. Comput. Conf. (GECCO), 2016, pp. 1139-1146.
[20] D. Sudholt and C. Witt, "On the choice of the update strength in estimation-of-distribution algorithms and ant colony optimization," Algorithmica, vol. 81, no. 4, pp. 1450-1489, 2019.
[21] M. S. Krejca and C. Witt, "Lower bounds on the run time of the univariate marginal distribution algorithm on OneMax," Theor. Comput. Sci., to be published, 2020.
[22] J. He and X. Yao, "Drift analysis and average time complexity of evolutionary algorithms," Artif. Intell., vol. 127, pp. 51-81, Mar. 2001.
[23] B. Doerr, "A tight runtime analysis for the cGA on jump functions: EDAs can cross fitness valleys at no extra cost," in Proc. Genet. Evol. Comput. Conf. (GECCO), 2019, pp. 1488-1496.
[24] C. McDiarmid, "Concentration," in Probabilistic Methods for Algorithmic Discrete Mathematics. Heidelberg, Germany: Springer, 1998, pp. 195-248. [Online]. Available: https://link.springer.com/ chapter/10.1007/978-3-662-12788-9_6
[25] B. Doerr, E. Happ, and C. Klein, "Tight analysis of the $(1+1)$-EA for the single source shortest path problem," Evol. Comput., vol. 19, no. 4, pp. 673-691, Dec. 2011.
[26] B. Doerr, "Analyzing randomized search heuristics via stochastic domination," Theor. Comput. Sci., vol. 773, pp. 115-137, Jun. 2019.
[27] P. K. Lehre and P. T. H. Nguyen, "On the limitations of the univariate marginal distribution algorithm to deception and where bivariate EDAs might help," in Proc. ACM/SIGEVO Found. Genet. Algorithms (FOGA), 2019, pp. 154-168.
![img-0.jpeg](img-0.jpeg)

Benjamin Doerr received the Diploma, Ph.D., and the Habilitation degrees in mathematics from the Christian-Albrechts-Universität zu Kiel, Kiel, Germany, in 1998, 2000, and 2005, respectively.

He is a Full Professor (professeur de classe exceptionnelle) with the École Polytechnique, Palaiseau, France. From 2005 to 2013, he was a Senior Researcher (tenured) with the Max Planck Institute for Informatics, Saarbrücken, Germany, and an Adjunct Professor with Saarland University, Saarbrücken. His research interests include mathematical analyses of problem-specific algorithms and randomized search heuristics as well as the development of new algorithms based on such analyses.

Prof. Doerr is a member of the editorial boards of several scientific journals, among them, artificial intelligence, evolutionary computation, and natural computing.
![img-1.jpeg](img-1.jpeg)

Weijie Zheng received the bachelor's degree in mathematics and applied mathematics from the Harbin Institute of Technology, Harbin, China, in July 2013, and the Doctoral degree in computer science and technology from Tsinghua University, Beijing, China, in October 2018.

He is currently a Postdoctoral Researcher with the Department of Computer Science and Engineering, Southern University of Science and Technology, Shenzhen, China, and the School of Computer Science and Technology, University of Science and Technology of China, Hefei, China. His current research majorly focuses on the theoretical analysis and design of evolutionary algorithms, especially, binary differential evolution and estimation-of-distribution algorithms.