# The Runtime of the Compact Genetic Algorithm on Jump Functions 

Benjamin Doerr ${ }^{1}$ (D)

Received: 19 August 2019 / Accepted: 24 October 2020 / Published online: 13 November 2020
(c) Springer Science+Business Media, LLC, part of Springer Nature 2020


#### Abstract

In the first and so far only mathematical runtime analysis of an estimation-of-distribution algorithm (EDA) on a multimodal problem, Hasenöhrl and Sutton (GECCO 2018) showed for any $k=o(n)$ that the compact genetic algorithm (cGA) with any hypothetical population size $\mu=\Omega\left(n e^{4 k}+n^{3.5+\epsilon}\right)$ with high probability finds the optimum of the $n$-dimensional jump function with jump size $k$ in time $O\left(\mu n^{1.5} \log n\right)$. We significantly improve this result for small jump sizes $k \leq \frac{1}{20} \ln n-1$. In this case, already for $\mu=\Omega(\sqrt{n} \log n) \cap$ poly $(n)$ the runtime of the cGA with high probability is only $O(\mu \sqrt{n})$. For the smallest admissible values of $\mu$, our result gives a runtime of $O(n \log n)$, whereas the previous one only shows $O\left(n^{5+\epsilon}\right)$. Since it is known that the cGA with high probability needs at least $\Omega(\mu \sqrt{n})$ iterations to optimize the unimodal ONEMAX function, our result shows that the cGA in contrast to most classic evolutionary algorithms here is able to cross moderate-sized valleys of low fitness at no extra cost. For large $k$, we show that the exponential (in $k$ ) runtime guarantee of Hasenöhrl and Sutton is tight and cannot be improved, also not by using a smaller hypothetical population size. We prove that any choice of the hypothetical population size leads to a runtime that, with high probability, is at least exponential in the jump size $k$. This result might be the first non-trivial exponential lower bound for EDAs that holds for arbitrary parameter settings. To complete the picture, we show that the cGA with hypothetical population size $\mu=\Omega(\log n)$ with high probability needs $\Omega(\mu \sqrt{n}+n \log n)$ iterations to optimize any $n$-dimensional jump function. This bound was known for OneMax, but, as we also show, the usual domination arguments do not allow to extend lower bounds on the performance of the cGA on OneMax to arbitrary functions with unique optimum. As a side result, we provide a simple general method based on parallel runs that, under mild conditions, (1) overcomes the need to specify a suitable population size and still gives a performance close to the one stemming from the best-possible population size, and (2) transforms EDAs with high-probability performance guarantees into EDAs with similar bounds on the expected runtime.


[^0]
[^0]:    Extended author information available on the last page of the article

Keywords Estimation-of-distribution algorithm $\cdot$ Runtime analysis $\cdot$ Combinatorial optimization $\cdot$ Local optima $\cdot$ Parallel runs

# 1 Introduction 

Estimation-of-distribution algorithms (EDAs) [52, 60] are a particular class of evolutionary algorithms. Whereas typical classic evolutionary algorithms evolve a population of (hopefully good) solutions, EDAs evolve a probabilistic model of the search space, that is, a probability distribution over the set of all solutions. The target is to obtain distributions that allow to easily sample good solutions for the optimization problem regarded.

While the mathematical analysis of classical evolutionary algorithms (EAs) has produced a plethora of insightful results, see, e.g., [2, 22, 45, 57], the rigorous understanding of EDAs is much less developed, see, e.g., the recent survey [49]. Obviously, this is due to the highly complex stochastic processes that describe the runs of such algorithms. In consequence, despite significant efforts and deep results [29, 55, 64], not even the runtime of the compact genetic algorithm (cGA) on the OneMax benchmark function is fully understood (here we would argue that the cGA is the simplest EDA and that the unimodal OneMax function, counting the number of ones in a bit string, is the easiest optimization problem with unique global optimum). It is therefore not surprising that many questions which are well-understood for EAs are only started to be understood for EDAs.

One such question is how EDAs optimize objective functions that are not unimodal. In the first and, prior to this work, only runtime analysis of an EDA on a multimodal problem, Hasenöhrl and Sutton [43] regard the optimization time of the cGA on the jump function class. These functions are unimodal apart from having a valley of low fitness of scalable size $k$ around the global optimum. For a sufficiently large constant $C$ and any constant $\varepsilon>0$, they show [43, Theorem 3.3] that the cGA with hypothetical population size $\mu \geq \max \left\{C n e^{4 k}, n^{3.5+\varepsilon}\right\}^{1}$ with probability $1-o(1)$ finds the optimum of any jump function with jump size $k=o(n)$ in $O\left(\mu n^{1.5} \log n\right)$ generations (which is also the number of fitness evaluations, since the cGA evaluates only two search points in each iteration).

This result is remarkable in that it shows that the cGA with the right choice of $\mu$ and for $k \geq 6$ is more efficient on jump functions than most evolutionary algorithms, which have a runtime of at least $\Omega\left(n^{k}\right)$; see Sect. 2.3.

### 1.1 An Improved Upper Bound for Small Jump Sizes

When the jump size $k$ is small, the runtime guarantee given by Hasenöhrl and Sutton [43] is still relatively large. We note that even when choosing the smallest possible

[^0]
[^0]:    ${ }^{1}$ In the paper, this is stated as minimum of the two terms, but from the proofs it is clear that it should be the maximum.

population size $\mu=n^{3.5+\epsilon}$, the runtime guarantee becomes at least $\Omega\left(n^{5+\epsilon}\right)$. While clearly a polynomial runtime, and thus efficient in the classic complexity theory view, this is a runtime that is not practical in many applications. Also, this runtime guarantee is weaker than the $O\left(n^{k}\right)$ bound for simple mutation-based EAs such as the $(1+1)$ EA when $k \leq 5$. Hence one could feel that the result of Hasenöhrl and Sutton shows the superiority of EDAs rather for problem instances for which both the runtime of typical EAs and the performance guarantee for the cGA are prohibitively large. In a similar vein, one has to question if a practitioner would run the cGA with a hypothetical population size of more than $n^{3.5}$ when solving a problem defined over bit strings of length $n$.

Our first main result is that these potential weaknesses of the cGA are not real and that the cGA performs in fact much better than what the previous work shows. We prove rigorously that the cGA with hypothetical population size $\mu \geq K \sqrt{n} \log n$, $K$ a sufficiently large constant, and $\mu$ polynomially bounded in $n$, with high probability ${ }^{2}$ optimizes any $n$-dimensional jump function with jump size $k \leq \frac{1}{20} \ln n-1$ in only $O(\mu \sqrt{n})$ iterations. Hence we both improve the runtime guarantee in terms of $n$ and we enlarge the range of admissible values for $\mu$. For the smallest admissible population size $\mu=\Theta(\sqrt{n} \log n)$, we obtain a runtime guarantee of $O(n \log n)$.

From a broader perspective our result yields that the cGA (and we expect similar results to hold for other EDAs) does not suffer from moderate-size valleys of low fitness. We recall that Sudholt and Witt [64] have shown that the cGA with any hypothetical population size (polynomial in $n$ ) with high probability needs $\Omega(\mu \sqrt{n})$ iterations to optimize the OneMax function. Hence our result shows that adding a valley of low fitness to the OneMax function does not worsen the asymptotic performance of the cGA as long as the fitness valley has a width of at most $\frac{1}{20} \ln n-1$.

On the technical side, our work makes some arguments of [43] more rigorous. In particular, we observe that the progress of the cGA cannot be estimated by taking the progress one would have when no fitness valley were present and correcting this estimate by inverting the progress with the probability that a search point is sampled in the fitness valley. This argument ignores the stochastic dependencies between the absolute value of the progress and the event that a solution in the fitness valley is sampled. These dependencies are real and have, in fact, a negative impact on the progress as discussed in more detail before Lemma 17.

We note that the approach of intentionally ignoring some dependencies to make a mathematical analysis tractable, often called mean-field analysis, is common in some scientific areas, most notably statistical physics, and has also been used in evolutionary computation, e.g., [33]. This approach, however, needs an additional justification, e.g., via specific experiments, why the omission of the dependencies should not change the matter substantially. In any case, such mean-field approaches do not lead to results fully proven with mathematical rigor. In this sense, we hope that our work also provides methods that help in future analyses of EDAs on multimodal optimization problems.

[^0]
[^0]:    ${ }^{2}$ That is, with probability $1-o(1)$, where the asymptotics is in $n$ for a fixed $k$ (which might be a function of $n$ )

# 1.2 An Exponential Lower Bound 

When $k$ is larger, say $k=\omega(\log n)$, then the runtime guarantee given in [43] is exponential in $k$, simply because $\mu$ has to be at least exponential in $k$ to fulfill the assumptions of the result. It is clear that with an exponential hypothetical population size, the runtime must be exponential as well (for the sake of completeness, we shall make this elementary argument precise in Lemma 1). What is not immediately clear is if by choosing a smaller hypothetical population size the cGA can optimize jump functions more efficiently.

Our second main result is a negative answer to this question. In Theorem 22 we show that, regardless of the hypothetical population size, the runtime of the cGA on a jump function with jump size $k$ with high probability is at least exponential in $k$. Interestingly, not only our result is a uniform lower bound independent of the hypothetical population size, but our proof is also "uniform" in the sense that it needs case distinctions neither w.r.t. the hypothetical population size nor w.r.t. the different reasons for the lower bound. Here we recall that the existing runtime analyses, see, e.g., again [29, 55, 64], find two reasons why an EDA can be inefficient. (i) The hypothetical population size is large and consequently it takes long to move the frequencies into the direction of the optimum. (ii) The hypothetical population size is small and thus, in the absence of a strong fitness signal, the random walk of the frequencies brings some frequencies close to the boundaries of the frequency spectrum (this effect is known as genetic drift, see [32] for a recent discussion and relatively precise quantification); from there they are hard to move back into the game.

We avoid such potentially tedious case distinctions via an elegant drift argument on the sum of the frequencies. Ignoring some technicalities here, we show that, regardless of the hypothetical population size, the frequency sum overshoots a value of $n-\frac{1}{3} k$ only after an expected number of $\exp (\Omega(k))$ iterations. However, in an iteration where the frequency sum is below $n-\frac{1}{4} k$, the optimum is sampled only with probability $\exp (-\Omega(k))$. These two arguments prove our lower bound of order $\exp (\Omega(k))$.

### 1.3 A Lower Bound for Small Jump Sizes

Since the exponential lower bound just discussed is not very strong for small jump sizes $k$, we also prove a lower bound of $\Omega(\mu \sqrt{n}+n \log n)$ for the performance of the cGA with hypothetical population size $\mu=\Omega(\log n)$ on any jump function. This lower bound was shown before for the OneMax function [64]. While it is not surprising that the cGA is not more efficient on jump functions than on OneMax, this is not trivial to show. As we also observe in Sect. 6, a result like "OneMax is an easiest function with a unique global optimum", which is true for many other evolutionary algorithms, cannot be proven with the usual arguments for the cGA. In fact, we currently have no indication that such a result is true for the cGA, nor do we have a counter-example.

# 1.4 Expected Runtimes of EDAs Versus Bounds with High Probability 

As a side result, triggered by the fact that we "only" show an upper bound that holds with high probability, but not a bound on the expected runtime, we provide in Sect. 2.4 a general approach to transform an EDA using a population size parameter $\mu$ into an algorithm that does not require the specification of such a parameter, but has a performance similar to the one of the EDA with optimally chosen parameter. This performance guarantee also holds for the expected runtime, even if for the EDA only a with-high-probability runtime guarantee is known.

## 2 Preliminaries

### 2.1 The Compact Genetic Algorithm

The compact genetic algorithm (cGA) is an estimation-of-distribution algorithm (EDA) proposed by Harik, Lobo, and Goldberg [41] for the maximization of pseudo-Boolean functions $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$. Being a univariate EDA, it develops a probabilistic model described by a frequency vector $f \in[0,1]^{n}$. This frequency vector describes a probability distribution on the search space $\{0,1\}^{n}$. If $X=\left(X_{1}, \ldots, X_{n}\right) \in\{0,1\}^{n}$ is a search point sampled according to this distribu-tion-we write

$$
X \sim \operatorname{Sample}(f)
$$

to indicate this-then we have $\operatorname{Pr}\left[X_{i}=1\right]=f_{i}$ independently for all $i \in[1 \ldots n]:=\{1, \ldots, n\}$. In other words, the probability that $X$ equals some fixed search point $y$ is

$$
\operatorname{Pr}[X=y]=\prod_{i: y_{i}=1} f_{i} \prod_{i: y_{i}=0}\left(1-f_{i}\right)
$$

In each iteration, the cGA updates this probabilistic model as follows. It samples two search points $x^{1}, x^{2} \sim \operatorname{Sample}(f)$, computes the fitness of both, and defines $\left(y^{1}, y^{2}\right)=\left(x^{1}, x^{2}\right)$ when $x^{1}$ is at least as fit as $x^{2}$ and $\left(y^{1}, y^{2}\right)=\left(x^{2}, x^{1}\right)$ otherwise. Consequently, $y^{1}$ is the better search point of the two (if not both have the same fitness). We then define a preliminary frequency vector by $f^{\prime}:=f+\frac{1}{\mu}\left(y^{1}-y^{2}\right)$, where $\mu$ is an algorithm parameter called hypothetical population size. This definition ensures that, when $y^{1}$ and $y^{2}$ differ in some bit position $i$, the $i$-th preliminary frequency moves by a step of $\frac{1}{\mu}$ into the direction of $y_{i}^{1}$, which we hope to be the right direction since $y^{1}$ is the better of the two search points. The hypothetical population size $\mu$ controls how strong this update is.

To avoid a premature convergence, we ensure that the new frequency vector is in $\left[\frac{1}{n}, 1-\frac{1}{\mu}\right]^{n}$ by capping too small or too large values at the corresponding boundaries. More precisely, for all $\ell \leq u$ and all $r \in \mathbb{R}$ we define

$$
\min \max (\ell, r, u):=\max \{\ell, \min \{r, u\}\}=\left\{\begin{array}{ll}
\ell & \text { if } r<\ell \\
r & \text { if } r \in[\ell, u] \\
u & \text { if } r>u
\end{array}\right.
$$

and we lift this notation to vectors by reading it component-wise. Now the new frequency vector is $\min \max \left(\frac{1}{n} \mathbf{1}_{n}, f^{\prime},\left(1-\frac{1}{n}\right) \mathbf{1}_{n}\right)$.

This iterative frequency development is pursued until some termination criterion is met. Since we aim at analyzing the time (number of iterations) it takes to sample the optimal solution (this is what we call the runtime of the cGA), we do not specify a termination criterion and pretend that the algorithm runs forever.

The pseudo-code for the cGA is given in Algorithm 1. We shall use the notation given there frequently in our proofs. For the frequency vector $f_{i}$ obtained at the end of iteration $t$, we denote its $i$-th component by $f_{i, t}$ or, when there is no risk of ambiguity, by $f_{i t}$. We shall frequently argue with the sum of the frequencies, which can be written as $\left\|f_{t}\right\|_{1}:=\sum_{i=1}^{n}\left|f_{i t}\right|$ since the frequencies are non-negative. With a slight abuse of notation, we extend this common notation also to preliminary frequency vectors $f^{\prime}$ and thus write $\left\|f^{\prime}\right\|_{1}:=\sum_{i=1}^{n} f_{i t}^{\prime}$, when there is not danger of confusion. Where there could be a chance of a critical misunderstanding, we use the much less common notation $\sum[v]:=\sum_{i=1}^{n} v_{i}$ to denote the sum of the entries of an $n$-dimensional vector $v \in \mathbb{R}^{n}$.

Well-behaved frequency assumption: For the hypothetical population size $\mu$, we take the common assumption that any two frequencies that can occur in a run of the cGA differ by a multiple of $\frac{1}{\mu}$. We call this the well-behaved frequency assumption. This assumption was implicitly already made in [41] by using even $\mu$ in all experiments (note that the hypothetical population size is denoted by $n$ in [41]). This assumption was made explicit in [29] by requiring $\mu$ to be even. Both works do not use the frequencies boundaries $\frac{1}{n}$ and $1-\frac{1}{n}$, so an even value for $\mu$ ensures well-behaved frequencies.

```
Algorithm 1: The compact genetic algorithm (cGA) to maximize
a function \(\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}\).
    \(t \leftarrow 0\);
    \(f_{t}=\left(\frac{1}{2}, \ldots, \frac{1}{2}\right) \in[0,1]^{n}\);
    repeat
        \(x^{1} \leftarrow \operatorname{Sample}\left(f_{t}\right)\);
        \(x^{2} \leftarrow \operatorname{Sample}\left(f_{t}\right)\);
        if \(\mathcal{F}\left(x^{1}\right) \geq \mathcal{F}\left(x^{2}\right)\) then \(\left(y^{1}, y^{2}\right) \leftarrow\left(x^{1}, x^{2}\right)\) else
            \(\left(y^{1}, y^{2}\right) \leftarrow\left(x^{2}, x^{1}\right)\);
            \(f_{t+1}^{\prime} \leftarrow f_{t}+\frac{1}{\mu}\left(y^{1}-y^{2}\right)\);
            \(f_{t+1} \leftarrow \min \max \left(\frac{1}{n} \mathbf{1}_{n}, f_{t+1}^{\prime},\left(1-\frac{1}{n}\right) \mathbf{1}_{n}\right)\);
            \(t \leftarrow t+1\);
    until forever;
```

For the case with frequency boundaries, the well-behaved frequency assumption is equivalent to $\left(1-\frac{2}{n}\right)$ being an even multiple of the update step size $\frac{1}{\mu}$. In this case, $n_{\mu}=\left(1-\frac{2}{n}\right) \mu \in 2 \mathbb{N}$ and the set of frequencies that can occur is

$$
F:=F_{\mu}:=\left\{\left.\frac{1}{n}+\frac{i}{\mu} \right\rvert\, i \in\left[0 \ldots n_{\mu}\right]\right\}
$$

This assumption was made, e.g., in the papers [35] (see the last paragraph of Section II.C) and [55] (see the paragraph following Lemma 2.1) as well as in the proof of Theorem 2 in [64].

A trivial lower bound: We finish this subsection on the cGA with the following very elementary remark, which shows that the cGA with hypothetical population size $\mu$ with probability $1-\exp (-\Omega(n))$ has a runtime of at least $\min \left\{\frac{\mu}{4}, \exp (\Theta(n))\right\}$ on any $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$ with a unique global optimum (and also on all functions with a sufficiently small exponential number of optima). This shows, in particular, that the cGA with the parameter value $\mu=\exp (\Omega(k))$ used to optimize jump functions with gap size $k \in \omega(\log n) \cap o(n)$ in time $\exp (O(k))$ in [43] cannot have a runtime better than exponential in $k$.

Lemma 1 Let $\alpha, \beta \geq 0$ be constants such that $\alpha \beta<\frac{4}{3}$. Let $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$ have at most $\alpha^{n}$ optima. The probability that the cGA generates an optimum of $\mathcal{F}$ in $T=\min \left\{\frac{\mu}{4}, \beta^{n}\right\}$ iterations is at most $2\left(\alpha \beta \frac{3}{4}\right)^{n}=\exp (-\Omega(n))$.

Proof By the definition of the cGA, the frequency vector $f$ used in iteration $t=1,2,3, \ldots$ satisfies $f \in\left[\frac{1}{2}-\frac{t-1}{\mu}, \frac{1}{2}+\frac{t-1}{\mu}\right]^{n}$. Consequently, the probability that a fixed one of the two search points which are generated in this iteration is a fixed solution, is at most $\left(\frac{1}{2}+\frac{t-1}{\mu}\right)^{n}$. For $t \leq \frac{\mu}{4}$, this is at most $\left(\frac{3}{4}\right)^{n}$. Hence by a simple union bound (over time and the global optima), the probability that an optimum is generated in the first $T=\min \left\{\frac{\mu}{4}, \beta^{n}\right\}$ iterations, is at most $2 \alpha^{n} T\left(\frac{3}{4}\right)^{n} \leq 2\left(\alpha \beta \frac{3}{4}\right)^{n}=\exp (-\Omega(n))$.

# 2.2 Runtime Analysis for the cGA 

In this subsection, we briefly describe the relevant previous runtime analyses for the cGA. For simplicity, we shall always assume that the hypothetical population size is at most polynomial in the problem size $n$, that is, that there is a constant $c$ such that $\mu \leq n^{c}$. This is justified, among others, by Lemma 1, which shows that a super-polynomial hypothetical population size immediately leads to a super-polynomial runtime on any objective function with at most $\alpha^{n}$ optima, where $\alpha$ can be any constant less than $\frac{4}{3}$.

The first to conduct a rigorous runtime analysis for the cGA was Droste in his seminal work [29]. He regarded the cGA without frequency boundaries, that is, he just took $f_{t+1}:=f_{t+1}^{s}$ in our notation. He showed that this algorithm with $\mu \geq n^{1 / 2+\varepsilon}, \varepsilon>0$ any positive constant, finds the optimum of the ONEMAX function defined by

$$
\operatorname{ONEMAx}(x)=\|x\|_{1}=\sum_{i=1}^{n} x_{i}
$$

for all $x \in\{0,1\}^{n}$ with probability at least $\frac{1}{2}$ in $O(\mu \sqrt{n})$ iterations [29, Theorem 8].
Droste also showed that this cGA for any objective function $\mathcal{F}$ with unique optimum has an expected runtime of $\Omega(\mu \sqrt{n})$ when conditioning on no premature convergence [29, Theorem 6]. It is easy to see that his proof of the lower bound can be extended to the cGA with frequency boundaries, that is, to Algorithm 1. For this, it suffices to deduce from his drift argument the result that the first time $T_{n / 4}$ that the frequency distance $D=\sum_{i=1}^{n}\left(1-f_{0}\right)$ is less than $\frac{n}{4}$ satisfies $E\left[T_{n / 4}\right] \geq \frac{\sqrt{n}} \mu \sqrt{n}$. Since the probability to sample the optimum from a frequency distance of at least $\frac{n}{4}$ is at most $\exp \left(-\frac{n}{4}\right)$, see Lemma 9 , the algorithm with high probability does not find the optimum before time $T_{n / 4}$.

Around ten years after Droste's work, Sudholt and Witt [64] showed that the $O(\mu \sqrt{n})$ upper bound also holds for the cGA with frequency boundaries. There (but the same should be true for the cGA without boundaries) a hypothetical population size of $\mu=\Omega(\sqrt{n} \log n)$ suffices (recall that Droste required $\mu=\Omega\left(n^{1 / 2+\varepsilon}\right)$ ). The technically biggest progress with respect to upper bounds most likely lies in the fact that the analysis in [64] also holds for the expected optimization time, which means that it also includes the rare case that frequencies reach the lower boundary (see our discussion of the relation of expectations and tail bounds for runtimes of EDAs in Sect. 2.4). Sudholt and Witt also show that the cGA with frequency boundaries with high probability (and thus also in expectation) needs at least $\Omega(\mu \sqrt{n}+n \log n)$ iterations to optimize ONEMAX. While the $\Omega(\mu \sqrt{n})$ lower bound could have been also obtained with methods similar to Droste's (in Lemma 15 we do something very similar), the innocent-looking $\Omega(n \log n)$ bound is surprisingly difficult to prove.

Not much is known for hypothetical population sizes below the order of $\sqrt{n}$. It is clear that then the frequencies will reach the lower boundary of the frequency range, so working with a non-trivial lower boundary like $\frac{1}{n}$ is necessary to prevent premature convergence. The recent lower bound $\Omega\left(\mu^{1 / 3} n\right)$ valid for $\mu=O\left(\frac{\sqrt{n}}{\log n \log \log n}\right)$ of [55] indicates that already a little below the $\sqrt{n}$ regime significantly larger runtimes occur, but with no upper bounds this regime remains largely not understood.

We refer the reader to the recent survey [49] for more results on the runtime of the cGA on classic unimodal test functions like LeadingOnes and BinVal. Interestingly, nothing was known for multimodal functions before the recent work of Hasenöhrl and Sutton [43] on jump functions, which we discussed already in the introduction.

The general topic of lower bounds on runtimes of EDAs remains largely little understood. Apart from the lower bounds for the cGA on OneMax discussed above, the following is known. Krejca and Witt [50] prove a lower bound for the UMDA on OneMax, which is of a similar flavor as the lower bound for the cGA of Sudholt and Witt [64]: For $\lambda=(1+\beta) \mu$, where $\beta>0$ is a constant, and $\lambda$ polynomially bounded in $n$, the expected runtime of the UMDA on OneMax is $\Omega(\mu \sqrt{n}+n \log n)$. For the binary value function BinVal, Droste [29] and Witt [67] together give a lower bound of $\Omega\left(\min \left\{n^{2}, \mu n\right\}\right)$ for the runtime of the cGA. Apart from these sparse results, we are not aware of any lower bounds for EDAs. Of course, the black-box complexity of

the problem is a lower bound for any black-box algorithm, hence also for EDAs, but these bounds are often lower than the true complexity of a given algorithm. For example, the black-box complexities of OneMax, LeadingOnes, and jump functions with jump size $k \leq \frac{1}{2} n-n^{\varepsilon}, \varepsilon>0$ any constant, are $\Theta\left(\frac{n}{\log n}\right)$ [7, 17], $\Theta(n \log \log n)$ [1], and $\Theta\left(\frac{n}{\log n}\right)$ [8], respectively.

# 2.3 Runtime Results for Jump Functions 

To complete the picture, we briefly describe some typical runtimes of evolutionary algorithms on jump functions. We recall that the $n$-dimensional jump function with jump size $k \geq 1$ is defined by

$$
\operatorname{JUMP}_{n k}(x)= \begin{cases}\|x\|_{1}+k & \text { if }\|x\|_{1} \in[0 \ldots n-k] \cup\{n\} \\ n-\|x\|_{1} & \text { if }\|x\|_{1} \in[n-k+1 \ldots n-1]\end{cases}
$$

Hence for $k=1$, we have a fitness landscape identical to the one of OneMax apart from all fitness values being larger by one. For larger values of $k$, we still have a fitness landscape identical to OneMax apart from constant shifts when only regarding the lowest $n-k$ fitness levels of the OneMax function, however, now there is a fitness valley ("gap")

$$
G_{n k}:=\left\{x \in\{0,1\}^{n} \mid n-k<\|x\|_{1}<n\right\}
$$

consisting of the $k-1$ highest sub-optimal fitness levels of the OneMax function.
This valley is hard to cross via standard-bit mutation with mutation rate $\frac{1}{n}$. Consequently, as proven in the classic paper [16], the $(1+1)$ EA has an expected optimization time of at least $n^{k}$ on $\operatorname{JUMP}_{n k}(x)$. This lower bound also holds for the $(\mu+\lambda)$ EA for all values of $\mu$ and $\lambda$ as well as, more surprisingly, for the $(\mu, \lambda)$ EA for large ranges of the population sizes [26]. By using larger mutation rates or a heavy-tailed mutation operator, a $k^{\Theta(k)}$ runtime improvement for the runtime of the $(1+1)$ EA can be obtained [21], but the runtime remains $\Omega\left(n^{k}\right)$ for $k$ constant (and this is also true for the variation of the heavy-tailed mutation rate proposed in [36]). The runtime stemming from the optimal mutation rate can be automatically obtained (apart from constant factors) via a self-adjusting choice of the mutation rate [62].

Asymptotically better runtimes can be achieved when using crossover, though this is harder than expected. The first work in this direction [48], among other results, could show that a simple $(\mu+1)$ genetic algorithm using uniform crossover with rate $p_{c}=O\left(\frac{1}{k n}\right)$ obtains an $O\left(\mu n^{2} k^{3}+2^{2 k} p_{c}^{-1}\right)$ runtime when the population size is at least $\mu=\Omega(k \log n)$. A shortcoming of this result, already noted by the authors, is that it only applies to uncommonly small crossover rates. Using a different algorithm that first always applies crossover and then mutation, a runtime of $O\left(n^{k-1} \log n\right)$ was achieved by Dang et al. [13, Theorem 2]. For $k \geq 3$, the logarithmic factor in the runtime can be removed by using a higher mutation rate. With additional diversity mechanisms, the runtime can be further reduced up to $O\left(n \log n+4^{k}\right)$, see [12]. In the light of this last result, the insight stemming from the previous work [43] and

ours is that the cGA apparently without further modifications supplies the necessary diversity to obtain a runtime of $O\left(n \log n+2^{O(k)}\right)$.

With a three-parent majority vote crossover, among other results, a runtime of $O(n \log n)$ could be obtained via a suitable island model for all $k=O\left(n^{\frac{1}{2}-e}\right)$ [34]. Via a hybrid genetic algorithm using as variation operators only local search and a deterministic voting crossover, an $O(n)$ runtime for $m=O(\log n)$ was obtained in [69]. Via a different voting mechanism, an $O(n \log n)$ runtime was obtained even for $m$ as large as $O(n)$ [61]. With the right static or heavy-tailed parameters, the $(1+(\lambda, \lambda))$ GA optimizes jump functions in time roughly $n^{(k+O(1)) / 2}[4,5]$, however, when using the parameterization developed for OneMax [11], then several self-adjusting versions of the $(1+(\lambda, \lambda))$ GA cannot beat mutation-based EAs as shown in [37].

Finally, we note that runtimes of $O\left(n\binom{n}{k}\right)$ and $O\left(k \log (n)\binom{n}{k}\right)$ were shown for the $(1+1) \mathrm{IA}^{\text {hyp }}$ and the $(1+1)$ Fast-IA artificial immune systems, respectively $[9,10]$.

# 2.4 Expected Runtimes Versus Guarantees with High Probability 

We note that our main upper bound result as well as the previous one [43] for this problem give runtime bounds that hold with high probability, that is, with probability $1-o(1)$. However, we do not show a bound on the expected runtime. Let us quickly argue what the differences are, why we chose to prove a high-probability statement, and how to transform EDAs with high-probability guarantees into EDAs with guarantees on the expected runtime. We note that Wegener [65, Section 3] with different arguments also suggests to prefer high-probability guarantees over expected runtimes.

For most evolutionary algorithms a high-probability guarantee can easily be turned into a bound on the expected runtime. If we know that a certain algorithm from any initial state finds the optimum in time $T$ with at least constant probability, then by splitting time into consecutive segments of length $T$ we see that after time $\gamma T$ the probability that the algorithm has not succeeded is at most $\exp (-\Omega(\gamma))$. Consequently, the runtime is stochastically dominated (see Sect. 3.2 for the definition of this notation) by $T$ times a geometric random variable with constant success rate, and consequently, the expected runtime is $O(T)$. The same argument gives a scalable tail bound of type "for all $\gamma>1$, the probability that the runtime is more than $\gamma T$ is at most $\exp (-\Omega(\gamma))$. ."

For EDAs, it is usually much harder to show a good performance for any initial situation since there are some states which are particularly unfavorable (usually when all frequencies are close to the wrong boundary value). This does not rule out that the expected runtime and the time that is obtained with high probability are of the same order, but proving the bound on the expected runtime needs stronger arguments. The analysis of the expected runtime of the cGA on OneMax in [64] is an example for such a result.

This additional proof complexity raises the question if this effort is justified if the hardest part is dealing with states of the algorithm that are rarely reached (in

[64] with probability $O\left(n^{-c}\right)$ only, where $c$ can be any positive constant). While we think that it was very valuable that the work [64] showed how to compute expected runtimes for EDAs, we feel that such results are not always needed, both because of the difficulty to obtain such results and because, in some sense, they are a mildly unnatural remedy to the deeper problem.

As said, the main reason why guarantees for the expected runtime of an EDA can be difficult to show is that the EDA with small probability can end up in a state from which the optimum is hard to reach. When in such a state, however, instead of spending much time to leave the unfavorable state, it would be more efficient and more natural to simply restart the algorithm and have a new good chance for a fast optimization process. While we cannot expect the algorithm to detect that it is in an unfavorable state, the following simple parallel-run strategy under mild assumptions can do this automatically. More precisely, via suitable parallel runs we obtain an expected runtime that is only a logarithmic factor above the runtime the EDA would have with high probability when using the optimal population size. Hence this approach both obtains expected runtimes and optimizes the value of the parameter $\mu$. We note that the "noise-oblivious scheme" proposed in [35, Algorithm 4] can also be used to optimize the parameter $\mu$, however only under the much stronger assumption that the runtime (or an upper bound, which influences the runtime of the scheme) is known. In this case, a simple restart scheme with multiplicatively increasing $\mu$ values does the job.

We now proceed with detailing our parallel-run strategy. In the remainder, we shall assume the following.

General assumption: Let $\mathcal{A}$ be an EDA (or any other randomized search heuristic) with a parameter $\mu$ and let $\mathcal{P}$ be a problem instance we want to solve. We assume that there are unknown values $\tilde{\mu}$ and $T$ such that $\mathcal{A}$ with any parameter value $\mu \geq \tilde{\mu}$ solves $\mathcal{P}$ in time $\mu T$ with probability at least $\frac{3}{4}$.

For this situation, we proposed the following strategy.
Parallel EDA runs with exponentially growing population size: We propose the following strategy to solve $\mathcal{P}$ via parallel runs of $\mathcal{A}$ with different parameter values. We start with no process running. In round $i=1,2, \ldots$ of our strategy, we let all running processes (which are process 1 to $i-1$ ) use a computational budget of $2^{i-1}$; further, we start process $i$ with parameter $\mu=2^{i-1}$ and let it use a budget of $\sum_{j=0}^{i-1} 2^{j}$. These processes can be run in parallel or sequentially in any order. The pseudocode for this strategy is given in Algorithm 2.

```
Algorithm 2: The parallel-run cGA to maximize a function \(f\) :
\(\{0,1\}^{\alpha} \rightarrow \mathbb{R}\)
1 Initialize process 1 with population size \(\mu=1\) and run it for one
    generation;
2 for \(i=2,3, \ldots\) do
3 Run processes \(1, \ldots, i-1\) each for another \(2^{i-1}\) generations;
4 Initialize process \(i\) with population size \(\mu=2^{i-1}\) and run it for
    \(\sum_{j=0}^{i-1} 2^{j}\) generations;
```

Analysis: We observe that at the end of round $i$, processes 1 to $i$ are running and have each spent a budget of $\sum_{j=0}^{i-1} 2^{i}=2^{i}-1$ up to this point in time. Consequently, the total budget spent in the first $i$ rounds is less than $i 2^{i}$.

Note that after round $i_{0}:=1+\left\lceil\log _{2} \bar{\mu}\right\rceil+\left\lfloor\log _{2} T\right\rfloor$, the process started with parameter value $\mu=\mu_{0}:=2^{\left\lceil\log _{2} \bar{\mu}\right\rceil} \geq \bar{\mu}$ has started and has used a time budget of

$$
\sum_{j=0}^{i_{0}-1} 2^{j} \geq \sum_{j=\left\lceil\log _{2} \bar{\mu}\right\rceil}^{i_{0}-1} 2^{j}=\mu_{0} \sum_{j=0}^{\left\lceil\log _{2} T\right\rceil} 2^{j} \geq \mu_{0} T
$$

Consequently, with probability $\frac{3}{4}$ this process has found the optimum at that time. With the same type of computation, we see that after round $i_{0}+j$, the process with parameter value $\mu=2^{j} \mu_{0}$ is finished with probability $\frac{3}{4}$. Consequently, the round in which we find the solution is stochastically dominated (see Sect. 3.2) by $i_{0}-1$ plus a geometric distribution (on $1,2, \ldots$ ) with success rate $\frac{3}{4}$. The expected time taken by this strategy to solve $\mathcal{P}$ thus is at most

$$
\sum_{i=i_{0}}^{\infty}\left(\frac{1}{4}\right)^{i-i_{0}}\left(\frac{3}{4}\right) i 2^{i}=\frac{3}{4} 2^{i_{0}} \sum_{j=0}^{\infty} 2^{-j}\left(j+i_{0}\right)=3 \cdot 2^{i_{0}-1}\left(i_{0}+1\right)
$$

using the well-known equality $\sum_{j=0}^{\infty} j 2^{-j}=2$. We continue estimating the expected runtime of our parallel-run strategy by

$$
3 \cdot 2^{i_{0}-1}\left(i_{0}+1\right) \leq 6 \bar{\mu} T\left(\log _{2}(\bar{\mu} T)+3\right)=: T_{\mathrm{par}}
$$

We note that if the values of $\bar{\mu}$ and $T$ were known in advance, then restarting the EDA with $\mu=\bar{\mu}$ and with a budget of $T$ until the problem is solved would immediately give an algorithm with expected runtime at most $T^{*}=\frac{4}{3} \bar{\mu} T$. This is the bestpossible expected runtime that can be deduced from our assumptions. Consequently, our parallel-run strategy with its $O\left(T^{*} \log T^{*}\right)$ expected runtime obtains the optimal expected runtime apart from a logarithmic factor.

In summary, we have shown the following result.
Theorem 2 Under the general assumptions made above, with $i_{0}:=1+\left\lceil\log _{2} \bar{\mu}\right\rceil+\left\lfloor\log _{2} T\right\rfloor$, the parallel run strategy described above has the following performance.

- The expected time until $\mathcal{P}$ is solved is at most

$$
3 \cdot 2^{i_{0}-1}\left(i_{0}+1\right) \leq 6 \bar{\mu} T\left(\log _{2}(\bar{\mu} T)+3\right)=\frac{9}{2} T^{*}\left(\log _{2}\left(\frac{3}{4} T^{*}\right)+3\right)
$$

where $T^{*}=\frac{4}{3} \bar{\mu} T$ is the best expected runtime that can be achieved via restarts of $\mathcal{A}$ under the general assumptions.

- For all $j=0,1,2, \ldots$, the probability that a runtime of $2^{i_{0}+j}(i+j)$ does not suffice to solve $\mathcal{P}$, is at most $4^{-j-1}$.

We remark that a logarithmic factor performance loss over the optimal strategy (requiring the precise values of $\bar{\mu}$ and $T$ ) is not a lot compared to what can be lost by choosing a wrong algorithm parameter, in particular, when the parameter is hard to guess. We note here that the recent work [55] suggests that already for the simple OneMax function, the hypothetical population size has a non-obvious influence on the runtime: Sufficiently small values give an $O(n \log n)$ runtime, in a middle regime the runtime increases to $\widehat{\Omega}\left(n^{7 / 6}\right)$ before dropping again to $O(n \log n)$ and then increasing linearly with $\mu$. In the light of such results, a logarithmic overhead for automatically finding a near-optimal rate appears to be a good trade-off.

Finally, we remark without further proof that when our general assumption is fulfilled with some failure probability $p$ instead of $\frac{1}{4}$, then tail probabilities in the second item of Theorem 2 are of order $p^{i+1}$ instead of $\left(\frac{1}{4} \bar{\gamma}^{i+1}\right.$. This could potentially be interesting when the performance of $\mathcal{A}$ is strongly concentrated so that the general assumptions hold with some $p=o(1)$. We also note that our strategy could be adjusted to deal with smaller success probabilities than $\frac{3}{4}$, either by increasing the $\mu$ value by a smaller factor than 2 or by having several processes using the same $\mu$ value. We spare the details.

Finally, we note that recently a similar approach was proposed in [31]. The main difference to ours is that runs where stopped after a time that was based on a mathematical analysis of when genetic drift could become problematic. From the implementation point of view, in this approach the runs with different values of $\mu$ can be conducted one after the other. From the theoretical perspective, this approach has the advantage that with the right choice of the hyperparameters the $\Theta(\log (\bar{\mu} T))$ factor in the runtime bound of Theorem 2 can be saved. The experimental results in [31] suggest that their approach is superior when the hyperparameters are chosen suitably, which is however non-trivial. We note that here that there is a general agreement in the community that genetic drift leads to an undesired behavior of the EDA. Genetic drift can lead to catastrophic runtimes (compare the results of $[20,54]$ ), but not always does ( $[53,68]$ show that the UMDA already with a population size of $\Theta(\log n)$ and thus clearly in the genetic drift regime can optimize OneMax in the for this algorithm best known runtime $O(n \log n))$.

# 3 Technical Tools 

In this section, we collect a number of technical results that will be used in our main proofs. These include standard arguments like elementary estimates, Chernoff bounds, and drift theorems, as well as original arguments for the analysis of the cGA which might be of general interest such as a tool to quantify the effect of frequencies being capped at the boundaries (Lemma 8), an upper and a lower bound for the probability of sampling the optimum given the $\ell_{1}$-distance between the current frequency vector and the optimum (Lemma 9 and 10 ), an estimate for the time taken to sample a search point close to the current frequency vector, and a lower bound on the probability to sample two different search points in one iteration (Lemma 12).

# 3.1 Standard Tools 

The following estimate seems well-known (e.g., it was used in [46] without proof or reference). Gießen and Witt [40, Lemma 3] give a proof via estimates of binomial coefficients and the binomial identity. A more elementary proof can be found in [28, Lemma 1.10.37].

Lemma 3 Let $X \sim \operatorname{Bin}(n, p)$. Let $k \in[0 \ldots n]$. Then

$$
\operatorname{Pr}[X \geq k] \leq\binom{n}{k} p^{k}
$$

We regularly use the following well-known multiplicative Chernoff bounds, which can be derived from [42], see, e.g., Theorems 1.10.1 and 1.10.5 together with Section 1.10.1.8 in [28].

Theorem 4 Let $X_{1}, \ldots, X_{n}$ be independent random variables taking values in $[0,1]$. Let $X=\sum_{i=1}^{n} X_{i}$. Let $\mu^{+} \geq E[X]$ and $\mu^{-} \leq E[X]$. Let $\delta \geq 0$ and $\tilde{\delta} \in[0,1]$. Then

$$
\begin{aligned}
& \operatorname{Pr}\left[X \geq(1+\delta) \mu^{+}\right] \leq \exp \left(-\frac{\min \left\{\delta^{2}, \delta\right\} \mu^{+}}{3}\right) \\
& \operatorname{Pr}\left[X \leq(1-\tilde{\delta}) \mu^{-}\right] \leq \exp \left(-\frac{\tilde{\delta}^{2} \mu^{-}}{2}\right)
\end{aligned}
$$

A direct consequence of these Chernoff bounds are the following estimates, which state that the OneMax fitness of a search point sampled from $\operatorname{Sample}(f)$ is close to the expected OneMax fitness $\|f\|_{1}$. Since we mostly need such results for frequency vectors close to $(1, \ldots, 1)$, we formulate this result in terms of distances to the maximum value $n$.

Lemma 5 Let $f \in[0,1]^{n}, D:=n-\|f\|_{1}, D^{-} \leq D \leq D^{+}, x \sim \operatorname{Sample}(f)$, and $d(x):=n-\|x\|_{1}$. Then for all $\delta \geq 0$ and $\tilde{\delta} \in[0,1]$, we have

$$
\begin{aligned}
& \operatorname{Pr}\left[d(x) \geq(1+\delta) D^{+}\right] \leq \exp \left(-\frac{1}{3} \min \left\{\delta^{2}, \delta\right\} D^{+}\right) \\
& \operatorname{Pr}\left[d(x) \leq(1-\tilde{\delta}) D^{-}\right] \leq \exp \left(-\frac{1}{2} \tilde{\delta}^{2} D^{-}\right)
\end{aligned}
$$

Proof The random variable $n-\|x\|_{1}$ can be written as a sum $n-\|x\|_{1}=\sum_{i=1}^{n} Z_{i}=: Z$ of $n$ independent binary random variables $Z_{1}, \ldots, Z_{n}$ such that $\operatorname{Pr}\left[Z_{i}=1\right]=1-f_{i}$. By definition, $E[Z]=D$. The claims follow directly from Theorem 4.

We need the lemma above in particular to argue that the probability to sample a search point in the gap region of the JUMP function is small. For the JUMP ${ }_{n k}$ function, we observe that when $D:=n-\|f\|_{1}$ is at least $2 k$, then the probability that $x \sim \operatorname{Sample}(f)$ lies in the gap, that is, satisfies $n-k<\|x\|_{1}<n$, is $e^{-\Omega(k)}$. This result is sufficient for our purposes. We note that we could also obtain a

low constant probability for sampling in the gap when $D \geq k+\Omega(\sqrt{k})$ with large implicit constant. In [43, Lemma 3.2], a gap probability of at most $1-\frac{1}{\sqrt{2}} \leq 0.293$ is claimed already when $D \geq k+c$ for $c$ a sufficiently large constant and $k=o(n)$, but we are skeptical that this is true. Note that when $f=\frac{n-k-c}{n} \mathbf{1}_{n}$, then $X=n-\|x\|_{1}$ with $x \sim \operatorname{Sample}(f)$ follows a binomial distribution with parameters $n$ and $\frac{k+c}{n}$. Hence if $k$ is large compared to $c$, then we have $\operatorname{Pr}[X<k]=\operatorname{Pr}[X<E[X]-c] \approx \frac{1}{2}$.

At one point, in the proof of Lemma 19, we need an additive Chernoff bound not only for the sum of independent random variables, but also for all partial sums. Such bounds are less known despite the fact that many classical Chernoff bounds hold equally well in this more demanding fashion. The following result is from Hoeffding [42, Theorem 2 together with (2.17)]. It can also be found in [28], Theorems 1.10.9 and 1.10.31.

Theorem 6 Let $X_{1}, \ldots, X_{n}$ be independent random variables such that for all $i \in[1 \ldots n]$, the variable $X_{i}$ takes values in some interval $\left[a_{i}, b_{i}\right]$ and has expectation $E\left[X_{i}\right]=0$. Then for all $\lambda \geq 0$, we have

$$
\begin{aligned}
& \operatorname{Pr}\left[\exists j \in[1 \ldots n]: \sum_{i=1}^{j} X_{i} \geq \lambda\right] \leq \exp \left(-\frac{2 \lambda^{2}}{\sum_{i=1}^{n}\left(b_{i}-a_{i}\right)^{2}}\right) \\
& \operatorname{Pr}\left[\exists j \in[1 \ldots n]: \sum_{i=1}^{j} X_{i} \leq-\lambda\right] \leq \exp \left(-\frac{2 \lambda^{2}}{\sum_{i=1}^{n}\left(b_{i}-a_{i}\right)^{2}}\right)
\end{aligned}
$$

Finally, we state the additive drift theorem of He and Yao [44] (see also the recent survey [51]), which allows to translate an expected progress (or bounds on it) into bounds for expected hitting times.

Theorem 7 Let $S \subseteq \mathbb{R}_{\geq 0}$ be finite and $0 \in S$. Let $X_{0}, X_{1}, \ldots$ be a random process taking values in $S$. Let $\delta>0$. Let $T=\inf \left\{t \geq 0 \mid X_{t}=0\right\}$.
(i) If for all $t \geq 0$ and all $s \in S \backslash\{0\}$ we have $E\left[X_{t}-X_{t+1} \mid X_{t}=s\right] \geq \delta$, then $E[T] \leq \frac{E\left[X_{0}\right]}{\delta}$
(ii) If for all $t \geq 0$ and all $s \in S \backslash\{0\}$ we have $E\left[X_{t}-X_{t+1} \mid X_{t}=s\right] \leq \delta$, then $E[T] \geq \frac{E\left[X_{0}\right]}{\delta}$.

# 3.2 Tools for the Analysis of the cGA 

In this section, we prove a number of general arguments for the analysis of the cGA. Since we expect that they are helpful for other runtime analyses of EDAs, we fix no general notation apart from the one defined in Algorithm 1 (at the price of occasionally restating a notation).

We recall the notation of stochastic domination, which will be used several times in this work. For two random variables $X$ and $Y$, not necessarily defined

over the same probability space, we say that $Y$ stochastically dominates $X$, written as $X \preceq Y$, if for all $\lambda \in \mathbb{R}$ we have

$$
\operatorname{Pr}[X \geq \lambda] \leq \operatorname{Pr}[Y \geq \lambda]
$$

Stochastic domination is a strong way of saying that $Y$ is not smaller than $X$. It implies that $E[X] \leq E[Y]$. We refer to [23] for more details.

Boundary effects: When, in the notation of Algorithm 1, the current frequency vector $f_{t}$ is such that $f_{i t} \in\left\{\frac{1}{n}, 1-\frac{1}{n}\right\}$ for some $i \in[1 \ldots n]$, then it may happen that $f_{t+1}^{\prime} \notin\left[\frac{1}{n}, 1-\frac{1}{n}\right]$ and consequently $f_{t+1}$ does not satisfy the nice relation $f_{t+1}=f_{t}+\frac{1}{\mu}\left(y^{1}-y^{2}\right)$. The following lemma quantifies these discrepancies. We here recall the common definition that for an $n$-dimensional vector $x$ and a subset $L \subseteq[1 \ldots n]$ of its index set, $x_{i L}$ denotes the restriction of $x$ to $L$, that is, the vector $\left(x_{\ell}\right)_{\ell \in L}$.

Lemma 8 Let $P=2 \frac{1}{n}\left(1-\frac{1}{n}\right)$. Let $t \geq 0$. Using the notation given in Algorithm 1, consider iteration $t+1$ of a run of the cGA started with a fixed frequency vector $f_{t} \in\left[\frac{1}{n}, 1-\frac{1}{n}\right]^{n}$.
(i) Let $L=\left\{i \in[1 \ldots n] \mid f_{i t}=\frac{1}{n}\right\}, \ell=|L|$, and $M=\left\{i \in L \mid x_{i}^{1} \neq x_{i}^{2}\right\}$. Then $|M| \sim \operatorname{Bin}(\ell, P)$ and

$$
\left\|f_{t+1}\right\|_{1}-\left\|f_{t+1}^{\prime}\right\|_{1} \leq\left\|\left(f_{t+1}\right)_{|L}\right\|_{1}-\left\|\left(f_{t+1}^{\prime}\right)_{|L}\right\|_{1} \leq \frac{1}{\mu}|M| \leq \frac{1}{\mu} \operatorname{Bin}\left(n, \frac{2}{n}\right)
$$

(ii) Let $L=\left\{i \in[1 \ldots n] \mid f_{i t}=1-\frac{1}{n}\right\}, \ell=|L|$, and $M=\left\{i \in L \mid x_{i}^{1} \neq x_{i}^{2}\right\}$. Then $|M| \sim \operatorname{Bin}(\ell, P)$ and

$$
\left\|f_{t+1}^{\prime}\right\|_{1}-\left\|f_{t+1}\right\|_{1} \leq\left\|\left(f_{t+1}^{\prime}\right)_{|L}\right\|_{1}-\left\|\left(f_{t+1}\right)_{|L}\right\|_{1} \leq \frac{1}{\mu}|M| \leq \frac{1}{\mu} \operatorname{Bin}\left(n, \frac{2}{n}\right)
$$

Proof By symmetry, it suffices to prove the first part. For an $i \in L$, we have $\operatorname{Pr}\left[x_{i}^{1} \neq x_{i}^{2}\right]=2 \frac{1}{n}\left(1-\frac{1}{n}\right)=P$. Since the bits of $x^{1}$ and $x^{2}$ were sampled independently, we have $|M| \sim \operatorname{Bin}(\ell, P)$.

By the well-behaved frequency assumption and the fact that $f_{t+1}^{\prime}=f_{t}+\frac{1}{\mu}\left(y^{1}-y^{2}\right)$ for binary vectors $y^{1}$ and $y^{2}$, we can have $f_{i, t+1}^{\prime}<\frac{1}{n}$ and thus $f_{i, t+1}>f_{i, t+1}^{\prime}$ only when $f_{i t}=\frac{1}{\mu}$ and $x_{i}^{1} \neq x_{i}^{2}$, that is, when $i \in M$. This shows $\left\|f_{t+1}\right\|_{1}-\left\|f_{t+1}^{\prime}\right\|_{1} \leq\left\|\left(f_{t+1}\right)_{|L}\right\|_{1}-\left\|\left(f_{t+1}^{\prime}\right)_{|L}\right\|_{1}$.

Since $f_{i, t+1}>f_{i, t+1}^{\prime} \quad$ implies $\quad f_{i, t+1}=f_{i, t+1}^{\prime}+\frac{1}{\mu}, \quad$ we also have $\left\|\left(f_{t+1}\right)_{|L}\right\|_{1}-\left\|\left(f_{t+1}^{\prime}\right)_{|L}\right\|_{1} \leq \frac{1}{\mu}|M| \leq \frac{1}{\mu} \operatorname{Bin}\left(n, \frac{2}{n}\right)$.

Sampling a particular solution: The following two elementary estimates give an upper and a lower bound on the probability to sample a particular search point $x^{*}$. Note that the quantity $D=\left\|x^{*}-f\right\|_{1}$ is our usual distance measure $D=n-\|f\|_{1}$ when $x^{*}=(1, \ldots, 1)$.

Lemma 9 Let $x^{*} \in\{0,1\}^{n}$. Let $f \in[0,1]^{n}$ and $D=\left\|x^{*}-f\right\|_{1}$. Let $x \sim \operatorname{Sample}(f)$. Then $\operatorname{Pr}\left[x=x^{*}\right] \leq \exp (-D)$.

Proof The probability to sample $x^{*}$ is

$$
\begin{aligned}
& \prod_{i=1}^{n}\left(1-\left|x_{i}^{*}-f_{i i}\right|\right) \leq \prod_{i=1}^{n} \exp \left(-\left|x_{i}^{*}-f_{i i}\right|\right) \\
& \quad=\exp \left(-\sum_{i=1}^{n}\left|x_{i}^{*}-f_{i i}\right|\right)=\exp \left(-\left\|x^{*}-f\right\|_{1}\right)=\exp (-D)
\end{aligned}
$$

To ease reading, we formulate the following estimate only for $x^{*}=(1, \ldots, 1)$, but it is clear that by symmetry analoguous statements hold for arbitrary $x^{*}$ (when $\left.\left\|x^{*}-f\right\|_{\infty} \leq 1-c\right)$.

Lemma 10 Let $0<c<1, f \in[c, 1]^{n}$, and $D=n-\|f\|_{1}$. Let $x \sim \operatorname{Sample}(f)$. Then $\operatorname{Pr}[x=(1, \ldots, 1)] \geq c^{D /(1-c)}$.

Proof For $i \in[1 \ldots n]$, let $\alpha_{i}:=\frac{1-f_{i}}{1-c}$. Then $f_{i}=\alpha_{i} c+\left(1-\alpha_{i}\right) 1$ is the unique representation of $f_{i}$ as convex combination of $c$ and 1 . Since the logarithm is concave, we have

$$
\log f_{i}=\log \left(\alpha_{i} c+\left(1-\alpha_{i}\right) 1\right) \geq \alpha_{i} \log c+\left(1-\alpha_{i}\right) \log 1=\log \left(c^{\alpha_{i}}\right)
$$

Since the logarithm is monotonically increasing, this inequality implies $f_{i} \geq c^{\alpha_{i}}$. Consequently,

$$
\operatorname{Pr}[x=(1, \ldots, 1)]=\prod_{i=1}^{n} f_{i} \geq \prod_{i=1}^{n} c^{\alpha_{i}}=c^{\sum_{i=1}^{n} \alpha_{i}}=c^{\left(n-\|f\|_{1}\right) /(1-c)}
$$

Time to sample a search point when close: We use the above lower bound on the probability to sample $(1, \ldots, 1)$ to prove the following result. It shows that when $\mu$ is large enough and $D_{t}:=n-\left\|f_{i}\right\|_{1}$ is small enough, then regardless of the fitness function we sample the search point $(1, \ldots, 1)$ quickly with high probability. The main argument is that when $\mu$ is sufficiently large, then $D_{t}$ stays small sufficiently long.

Lemma 11 Let $\mu$ be at least $\sqrt{n}$, but polynomially bounded in $n$. Consider a run of the cGA with hypothetical population size $\mu$ on an arbitrary fitness function. Assume that at some time $t_{0}$, we have $D_{t_{0}}:=n-\left\|f_{t_{0}}\right\|_{1} \leq \frac{1}{10} \ln n$ and $f_{t_{0}} \in\left[\frac{1}{2}, 1\right]^{n}$. Then with probability at least $1-n^{-\omega(1)}$, the search point $(1, \ldots, 1)$ is sampled in the next $\frac{D_{t_{0}} \mu}{2 \ln (n)^{2}}$ iterations.

Proof We first argue that if at some time $t$ we have $D_{t} \leq \ln (n)^{2}$, then $\operatorname{Pr}\left[D_{t+1} \geq D_{t}+\frac{2}{\mu} \ln (n)^{2}\right] \leq n^{-v t(1)}$. By Lemma 5, we have

$$
\operatorname{Pr}\left[d\left(x^{i}\right) \geq 2 \ln (n)^{2}\right] \leq \exp \left(-\frac{1}{3} \ln (n)^{2}\right)=n^{-v t(1)}
$$

for $j=1,2$. Consequently, with probability $1-n^{-v t(1)}$, we have both $\left\|x^{1}\right\|_{1}>n-2 \ln (n)^{2}$ and $\left\|x^{2}\right\|_{1}>n-2 \ln (n)^{2}$. Now regardless of how $x^{1}$ and $x^{2}$ are sorted into $\left(y^{1}, y^{2}\right)$, less than $2 \ln (n)^{2}$ frequencies are decreased in the frequency update of this iteration. We conclude that $D_{t+1}<D_{t}+\frac{2}{\mu} \ln (n)^{2}$.

Let $L=\left\lfloor\frac{D_{t_{0}}}{(2 / \mu) \ln (n)^{2}}\right\rfloor$. By a union bound, with probability

$$
1-L n^{v t(1)} \geq 1-n^{v t(1)}
$$

we have $D_{t+1} \leq D_{t}+\frac{2}{\mu} \ln (n)^{2}$ in all iterations $t=t_{0}, \ldots, t_{0}+L-1$ that start with $D_{t} \leq 2 D_{t_{0}}$. Let us condition on this in the following. Then by induction, we have $D_{t} \leq D_{t_{0}}+\left(t-t_{0}\right) \frac{2}{\mu} \ln (n)^{2} \leq 2 D_{t_{0}}$ throughout these $L$ iterations.

Note that $L=O\left(\frac{\mu}{\log (n)}\right)$, hence throughout this period we also have $f_{i i} \geq \frac{1}{3}-\frac{1}{\mu} L \geq 0.32$ (assuming $n$ to be sufficiently large) for all $i \in[1 \ldots n]$. By Lemma 10, the probability that a fixed search point sampled in this period equals $(1, \ldots, 1)$, is at least

$$
\begin{aligned}
0.32^{2 D_{t_{0}} / 0.68} & \geq 0.32^{0.2 \ln (n) / 0.68} \\
& =\exp (0.2 \ln (n) \ln (0.32) / 0.68) \geq n^{0.2 \ln (0.32) / 0.68}=: q
\end{aligned}
$$

Since $0.2 \ln (0.32) / 0.68>-0.34$ and $L=\Omega\left(\frac{\mu}{\log (n)^{2}}\right)$, the probability that $(1, \ldots, 1)$ is not sampled in this period is at most

$$
(1-q)^{2 L} \leq \exp (-2 q L) \leq \exp \left(-n^{0.2 \ln (0.32) / 0.68} \cdot \Omega\left(\frac{\mu}{\ln (n)^{2}}\right)\right) \leq \exp \left(-\Omega\left(n^{0.16}\right)\right)
$$

Sampling search points with different 1-norm: To argue that the cGA makes at least some small progress, we shall use the following blunt estimate for the probability that two bit strings $x, y \sim \operatorname{Sample}(f)$ sampled from the same product distribution have a different distance from the all-ones string (and, by symmetry, from any other string, but this is a statement which we do not need here).

Lemma 12 Let $n \in \mathbb{N}, m \in\left[\frac{n}{2} \ldots n\right]$, and $f \in\left[\frac{1}{n}, 1-\frac{1}{n}\right]^{m}$. Let $x^{1}, x^{2} \sim \operatorname{Sample}(f)$ be independent. Then $\operatorname{Pr}\left[\left\|x^{1}\right\|_{1} \neq\left\|x^{2}\right\|_{1}\right] \geq \frac{1}{16}$.

Proof For all $v \in \mathbb{R}^{m}$ and $a, b \in[1 \ldots m]$ with $a \leq b$ we use the abbreviation $v_{[a \ldots b]}:=\sum_{i=a}^{b} v_{i}$. We first argue that by symmetry, we can assume that $f_{[1 \ldots m]} \leq \frac{m}{2}$. Indeed, let $f_{[1 \ldots m]}>\frac{m}{2}$ and assume the claim shown for the case that $f_{[1 \ldots m]} \leq \frac{m}{2}$. Let $\tilde{f}=\mathbf{1}_{m}-f$ and $\tilde{x}^{1}, \tilde{x}^{2} \sim \operatorname{Sample}(\tilde{f})$ independent. Then

$$
\begin{aligned}
\operatorname{Pr}\left[\left\|x^{1}\right\|_{1}=\left\|x^{2}\right\|_{1}\right] & =\sum_{i=0}^{m} \operatorname{Pr}\left[\left\|x^{1}\right\|_{1}=i=\left\|x^{2}\right\|_{1}\right] \\
& =\sum_{i=0}^{m} \operatorname{Pr}\left[\left\|x^{1}\right\|_{1}=i\right] \cdot \operatorname{Pr}\left[\left\|x^{2}\right\|_{1}=i\right] \\
& =\sum_{i=0}^{m} \operatorname{Pr}\left[\left\|\bar{x}^{1}\right\|_{1}=m-i\right] \cdot \operatorname{Pr}\left[\left\|\bar{x}^{2}\right\|_{1}=m-i\right] \\
& =\sum_{i=0}^{m} \operatorname{Pr}\left[\left\|\bar{x}^{1}\right\|_{1}=m-i=\left\|\bar{x}^{2}\right\|_{1}\right] \\
& =\operatorname{Pr}\left[\left\|\bar{x}^{1}\right\|_{1}=\left\|\bar{x}^{2}\right\|_{1}\right] \leq \frac{15}{16}
\end{aligned}
$$

where the last estimate follows from our assumption and the fact that $\bar{f}_{\{1 \ldots m\}} \leq \frac{m}{\delta}$. This shows the claim for $f$ and justifies that in the remainder, we assume $f_{\{1 \ldots m\}} \leq \frac{m}{\delta}$.

Without loss of generality, we may further assume that $f_{i} \leq f_{i+1}$ for all $i \in[1 \ldots m-1]$. We have $f_{\lfloor m / 4\rfloor} \leq \frac{2}{3}$ as otherwise

$$
f_{\{1 \ldots m\}} \geq f_{\{\lfloor m / 4\rfloor+1 \ldots m\}}>\frac{2}{3}\left(m-\left\lfloor\frac{m}{4}\right\rfloor\right) \geq \frac{2}{3} \cdot \frac{3}{4} m=\frac{m}{2}
$$

contradicting our assumption.
Let $\ell$ be minimal such that $f_{\{1 \ldots \ell\}} \geq \frac{1}{8}$. Since $\ell \leq \frac{n}{8} \leq \frac{m}{4}$, we have $f_{\ell} \leq \frac{2}{3}$ and thus $f_{\{1 \ldots \ell\}} \leq \frac{1}{8}+\frac{2}{3}=\frac{19}{24}$.

For $j \in\{0,1\}$ let $q_{j}=\operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1}=j\right]=\operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{2}=j\right]$. We compute

$$
\begin{aligned}
& \operatorname{Pr}\left[\left\|x^{1}\right\|_{1} \neq\left\|x^{2}\right\|_{1}\right] \\
& \geq \operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1}=x_{\{1 \ldots \ell\}}^{2} \wedge x_{\{\ell+1 \ldots n\}}^{1} \neq x_{\{\ell+1 \ldots n\}}^{2}\right] \\
& +\operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1} \neq x_{\{1 \ldots \ell\}}^{2} \wedge x_{\{\ell+1 \ldots n\}}^{1}=x_{\{\ell+1 \ldots n\}}^{2}\right] \\
& =\operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1}=x_{\{1 \ldots \ell\}}^{2}\right] \operatorname{Pr}\left[x_{\{\ell+1 \ldots n\}}^{1} \neq x_{\{\ell+1 \ldots n\}}^{2}\right] \\
& +\operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1} \neq x_{\{1 \ldots \ell\}}^{2}\right] \operatorname{Pr}\left[x_{\{\ell+1 \ldots n\}}^{1}=x_{\{\ell+1 \ldots n\}}^{2}\right] \\
& \geq \min \left\{\operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1}=x_{\{1 \ldots \ell\}}^{2}\right], \operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1} \neq x_{\{1 \ldots \ell\}}^{2}\right]\right\} \operatorname{Pr}\left[x_{\{\ell+1 \ldots n\}}^{1} \neq x_{\{\ell+1 \ldots n\}}^{2}\right] \\
& +\min \left\{\operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1}=x_{\{1 \ldots \ell\}}^{2}\right], \operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1} \neq x_{\{1 \ldots \ell\}}^{2}\right]\right\} \operatorname{Pr}\left[x_{\{\ell+1 \ldots n\}}^{1}=x_{\{\ell+1 \ldots n\}}^{2}\right] \\
& \geq \min \left\{\operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1}=x_{\{1 \ldots \ell\}}^{2}\right], \operatorname{Pr}\left[x_{\{1 \ldots \ell\}}^{1} \neq x_{\{1 \ldots \ell\}}^{2}\right]\right\} \\
& \geq \min \left\{q_{0}^{2}+q_{1}^{2}, 2 q_{0} q_{1}\right\}=2 q_{0} q_{1},
\end{aligned}
$$

the latter by the inequality of the arithmetic and geometric mean. Using Bernoulli's inequality, we estimate coarsely

$$
\begin{aligned}
& q_{0}=\prod_{i=1}^{\ell}\left(1-f_{i}\right) \geq 1-f_{\{1 \ldots \ell\}} \\
& q_{1}=\sum_{i=1}^{\ell} f_{i} \prod_{j \in\{1 \ldots \ell\} \backslash\{i\}}\left(1-f_{i}\right) \geq f_{\{1 \ldots \ell\}}\left(1-f_{\{1 \ldots \ell\}}\right)
\end{aligned}
$$

Since the function $z \mapsto z(1-z)^{2}$ is unimodal in $[0,1]$, the minimum in any subinterval of $[0,1]$ is necessarily found at a boundary of the interval. We thus obtain

$$
\begin{aligned}
2 q_{0} q_{1} & \geq 2 \min \left\{z(1-z)^{2} \mid z \in\left\{\frac{1}{8}, \frac{19}{24}\right\}\right\} \\
& =2 \min \left\{z(1-z)^{2} \mid z \in\left\{\frac{1}{8}, \frac{19}{24}\right\}\right\}=2 \frac{19}{24}\left(\frac{5}{25}\right)^{2} \geq \frac{1}{16}
\end{aligned}
$$

# 4 An Upper Bound for the Runtime of the cGA on Jump Functions 

In this section, we state precisely and prove our $O(\mu \sqrt{n})$ upper bound for the runtime of the cGA on jump functions with small jump size $k$. With the smallest admissable hypothetical populations size $\mu=\Theta(\sqrt{n} \log n)$, it gives a runtime guarantee of $O(n \log n)$. Our result includes the trivial case $k=1$, that is, the OneMax benchmark function, a result that was known before.

Our results are true not only for jump functions, but for the larger class of all functions that (apart from a uniform additive constant) agree with OneMax on $\{0,1\}^{n} \backslash G_{n k}$ and that have $(1, \ldots, 1)$ as an optimum (recall that $G_{n k}$ was defined to be the gap region of $\mathrm{JUMP}_{n k}$, see (2)). This observation is interesting in its own right, e.g., it yields that our result also holds for the plateau functions defined in [3]. It also helps us formulating the proofs in a more concise manner since we can now assume that $k$ is sufficiently large (since a jump function with small jump parameter $k^{\prime}$ is included in this larger class for all $k \geq k^{\prime}$ ).

To make things precise, for all $n \in \mathbb{N}$ and $k \geq 1$ we define the class of subjump functions with jump size $k$ as the class of all functions $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$ such that there is a $K \in \mathbb{N}$ such that

- $\mathcal{F}(x)=\|x\|_{1}+K$ if $\|x\|_{1} \in[0 \ldots n-k] \cup\{n\}$,
- $\mathcal{F}(x) \leq n+K$ if $\|x\|_{1} \in[n-k+1 \ldots n-1]$
for all $x \in\{0,1\}^{n}$. Here the prefix $s u b$ is to be understood in the sense that these functions are seen as at most as hard as the true jump function with jump size $k$ or that, if $\mathcal{F}$ is a jump function, its jump size is at most $k$. It is not to be understood in the sense that a subjump functions is pointwise less or equal to the corresponding jump function (which is not true).

As said before, subjump functions have an optimum at $(1, \ldots, 1)$, but there could be others in the gap region $G_{n k}$. We continue to call $G_{n k}$ the gap even though this is not for all subjump functions a fitness valley. We note that the class of subjump functions with jump size $k$ includes all subjump functions with jump size smaller than $k$, in particular, all jump functions with smaller jump size and thus also the OneMax function (to ensure this property, we needed the additional variable $K$ in the definition).

Without further details, we note that many previously proven upper bounds for runtimes on jump functions are also valid for subjump functions. However, this might not be true for results that heavily exploit the particular structure of the true jump functions, say the symmetry of the set of local optima, such as the results on crossover-based algorithms.

The main result of this section is the following runtime guarantee for subjump functions.

Theorem 13 Let $k \leq \frac{1}{20} \ln (n)-1$. For a sufficiently large constant $c_{\mu}$, let $\mu \geq c_{\mu} \sqrt{n} \ln (n)$, but polynomially bounded in $n$. Then the cGA with frequency boundaries (Algorithm 1) with hypothetical population size $\mu$ with probability $1-o(1)$ finds the optimum of any $n$-dimensional subjump function with jump size $k$ in time $O(\mu \sqrt{n})$. This time is $O(n \log n)$ when $\mu=\Theta(\sqrt{n} \ln (n))$.

We start by giving a rough overview of the proof in the following subsection and then state the formal proof in the two subsequent subsections.

# 4.1 Proof Overview 

We now give a brief overview of our runtime analysis and show how the different partial results work together. We leave it to the reader to read this section now or after the presentation of the partial results (or twice).

In our analysis, we roughly distinguish three phases of the optimization process. The first phase, analyzed in Lemma 16, lasts until for the first time the frequency distance $D_{t}:=n-\left\|f_{t}\right\|_{1}$ is $O(\log n)$ with a large implicit constant. During this phase, by Lemma 5 and a union bound, with high probability we will never sample a solution in the gap. Consequently, we can pretend that we are optimizing the OneMax function and use our analysis of Lemma 15, which reuses arguments of the classic result by Droste [29] including Lemma 14.

The second phase, analyzed in Lemma 18, then lasts until we have a $D_{t}$ value of less than $2 k$ (or less than some constant in the case of a very small $k$ ). In this phase, we use the drift computed in Lemma 17. We profit from the fact that in this phase we only need to obtain a moderate decrease of $D_{t}$ and apply the additive drift theorem (Theorem 7(i)) with the smallest drift that can occur in this phase, which is $\Omega\left(\frac{1}{\mu}\right)$. Since this phase is so short, a simple Markov bound suffices to show that the phase ends with high probability in due time.

Once we have reached a $D_{t}$ value of $O(k)$, we have a reasonable chance to sample the optimum as shown in Lemma 11. Since in this third phase samples in the

gap occur frequently, we have less control over $D_{t}$, in particular, we cannot exhibit an expected decrease of $D_{t}$. We therefore pessimistically estimate $D_{t}$ as if $D_{t}$ would always increase, which gives (apart from the boundary effects described in Lemma 8) an increase of $\left\|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right\|$. Since $D_{t}$ is small, these increases are small as well, as again ensured by Lemma 5. With this observation, we can argue that we have a $D_{t}$ value of $O(k)$ for almost $\mu$ iterations, which together with Lemma 10 shows that we sample the optimum with high probability.

All the arguments above need that the frequencies are bounded away from the lower boundary of $\frac{1}{n}$, more precisely, that they are $\Omega(1)$ at all times. In the first two phases, we ensure this via Lemma 19, our general result for random processes that are not Markov processes. To this aim, we estimate the probabilities of certain frequency changes by adjusting this data from the OneMax process (Lemma 20, taken from Sudholt and Witt [64]) via a pessimistic estimate of the negative influence of search points sampled in the gap. For the third phase, the fact that this phase only last $o(\mu)$ iterations implies that frequencies change by at most $o(1)$, hence the $\Omega(1)$ lower bound remains intact.

# 4.2 Proof Ingredients 

In this section, we prove separately the main arguments needed in our final proof. We also state some known results on how the cGA optimizes OneMax.

The following result is a weaker form of what was shown in the proof of Lemma 5 in [29]. The result of Lemma 5 in [29], bounding the expected progress instead of showing that a certain progress can be observed with constant probability, is not sufficient for our purposes, see the discussion below.

Lemma 14 [29] There is a constant $C>0$ such that the following holds. Let $n \in \mathbb{N}$ and $D \in \mathbb{N}$. Let $f \in\left[\frac{1}{3}, 1\right]^{n}$ such that $\|f\|_{1} \leq n-D$. Let $x^{1}, x^{2} \sim \operatorname{Sample}(f)$ independent. Then

$$
\operatorname{Pr}\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \geq \frac{1}{5} \sqrt{D}\right] \geq C
$$

We use this lemma to now conduct a (partial) runtime analysis of the cGA on OneMax. Such an analysis is helpful for our purposes since the optimization process of the cGA on a subjump function is identical to the one on the OneMax function as long as no search point in the gap region is sampled.

Our analysis on OneMax differs from Droste's analysis of the cGA on OneMax [29, Theorem 8] in several respects. First, we aim at a guarantee that holds with high probability. For this reason, we cannot use the approach via additive drift, and this is the reason why we need Lemma 14 instead of Lemma 5 from [29].

We note that Droste's drift argument is also not perfectly complete. In each of his $\Theta(n)$ relatively short phases, he uses additive drift to estimate from the expected progress the time to reach the phase target, but he ignores the fact that

his expected progress also takes into account progress beyond the phase target. This could lead to an overestimation of the progress. This problem does not occur in the additive drift theorem as stated in Theorem 7, since there the process lives in the non-negative numbers and the process target is zero. We have no doubt, though, that this technical gap can be fixed with additional arguments.

We regard the cGA with non-trivial boundaries, which requires additional arguments as the capping of the frequencies can change the drift of the frequency sum (albeit by not a lot, as our proof shows). We note that without these extra arguments, our proof also applies to the setting without boundaries.

We only regard the time needed to reach a frequency vector with constant distance to the all-ones vector. We note that our analysis can be extended to also give a bound for the time to sample an optimal solution, but we do not need such a result (and in fact, such a result is implied by our main result). Also, a simplified version of our proof would apply to the cGA without boundaries.

Lemma 15 Let $C$ be the constant from Lemma 14. Consider a run of the cGA with $\mu \geq \log _{2} n$ on the OneMax benchmark function. Let $D_{t}:=n-\left\|f_{i}\right\|_{1}$ for all $t$. Let $K$ be a sufficiently large constant. Let $T$ be the first time that $D_{t} \leq K$ or that there is an $i \in[1 \ldots n]$ with $f_{i t}<\frac{1}{3}$. Then

$$
\operatorname{Pr}\left[T \geq \frac{10(2+\sqrt{2})}{C} \mu \sqrt{n}\right]=\exp (-\Omega(\mu))
$$

We formulated the result above in the slightly cumbersome manner of giving a time guarantee for the event of reaching a near-optimal frequency vector or reaching a frequency below $\frac{1}{3}$. By Lemma 19 we will be able to rule out the latter event via a simple union bound over the failure probabilities. This approach is technically simpler than conditioning on the frequencies to not go below $\frac{1}{3}$ and then working in the conditional probability space.

Proof of Lemma 15 Define $D_{t}^{\prime}:=n-\left\|f_{t}^{\prime}\right\|_{1}$ for all $t \geq 1$. For $i=1,2, \ldots$ let $d_{i}=2^{-i} n$. Without loss of generality, we may assume that $K=2^{-\ell-1} n$ for some $\ell \in \mathbb{N}$. Note that $\ell \leq \log _{2} n$. We say that the optimization process enters Phase $i$ (and thus leaves its current phase) when for the first time $D_{t} \leq d_{i}$. Note that we stay in Phase $i$ even when after entering this phase $D_{i}$ increases beyond $d_{i}$. Note further that, by definition, the process starts in Phase 1. We also say that the current phase ends when a frequency reaches a value below $\frac{1}{3}$.

We analyze the time spend in each Phase $i \leq \ell$ (when assuming that all frequencies are at least $\frac{1}{2}$ at the start of the phase) and show that this time, with probability at least $1-\exp (-\Omega(\mu))$, is at most $T_{i}=\left\lceil 20 \frac{1}{C} \mu \sqrt{d_{i+1}}\right\rceil$. Let $t^{\prime}$ be the iteration in which the process enters Phase $i$. To ease the argument, we now consider exactly $T_{i}$ iterations. In case the phase ends earlier, we shall from that point on regard an artificial process, with a slight abuse of notation also denoted by $D_{t}$ and $D_{t}^{\prime}$, that satisfies the conditions

$$
\begin{aligned}
& \operatorname{Pr}\left[D_{t+1}^{\prime}=D_{t}-\frac{1}{5 \mu} \sqrt{d_{t+1}} \mid D_{t}\right]=C \\
& \operatorname{Pr}\left[D_{t+1}^{\prime}=D_{t} \mid D_{t}\right]=1-C \\
& \operatorname{Pr}\left[D_{t+1}=D_{t+1}^{\prime} \mid D_{t+1}^{\prime}\right]=1
\end{aligned}
$$

Such an artificial extension of a process was, to the best of our knowledge, in the theory of evolutionary algorithms first used in [14].

When all frequencies are at least $\frac{1}{3}$, by Lemma 14 we have $\operatorname{Pr}\left[\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1} \mid \geq \frac{1}{5} \sqrt{D_{t}}\right] \geq C$. Since we have $\left\|y^{1}\right\|_{1} \geq\left\|y^{2}\right\|_{1}$ when optimizing OneMax, we have that $D_{t+1}^{\prime}$ with probability at least $C$ satisfies $D_{t+1}^{\prime} \leq D_{t}-\frac{1}{5 \mu} \sqrt{D_{t}} \leq D_{t}-\frac{1}{5 \mu} \sqrt{d_{t+1}}$. We call this a success. Note that the probability for a success is at least $C$ regardless of what happened before in this phase. Consequently, in $T_{i}$ iterations, we not only have an expected number of at least $20 \mu \sqrt{d_{i+1}}$ successes, but, using the multiplicative Chernoff bounds (Theorem 4) and the fact that "sequential independence" suffices for Chernoff bounds to be admissible (Lemma 11 in [15] or Section 1.10.2.1 in [28]), we also have at least $10 \mu \sqrt{d_{i+1}}$ successes with probability at least $1-\exp \left(-\frac{5}{2} \mu \sqrt{d_{i+1}}\right)$. Note that with probability one we have $D_{t+1}^{\prime} \leq D_{t}$, again because $\left\|y^{1}\right\|_{1} \geq\left\|y^{2}\right\|_{1}$.

By Lemma 8 (ii), we have $D_{t+1} \leq D_{t+1}^{\prime}+\frac{1}{\mu} \operatorname{Bin}\left(n, \frac{2}{\mu}\right)$, again regardless of what happened in earlier iterations. Consequently, the total number of times we increase $D_{t}$ by $\frac{1}{\mu}$ due to reaching an upper frequency boundary can be estimated by a sum of $T_{i} n$ independent binary random variables with success probability $\frac{2}{\mu}$. Hence the expectation of this number is at most $2 T_{i} \leq 40 \frac{1}{C} \mu \sqrt{d_{i+1}}+2$ and, by Theorem 4, with probability at least $1-\exp \left(\frac{2 T_{i}}{3}\right) \geq 1-\exp \left(-\frac{40}{3} \frac{1}{C} \mu \sqrt{d_{i+1}}\right)$ this number is at most $4 T_{i}=80 \frac{1}{C} \mu \sqrt{d_{i+1}}+4$.

Taking these two observations together, we see that with probability

$$
1-\exp \left(-\frac{5}{2} \mu \sqrt{d_{i+1}}\right)-\exp \left(-\frac{40}{3} \frac{1}{C} \mu \sqrt{d_{i+1}}\right)=1-\exp (-\Omega(\mu))
$$

we have

$$
\begin{aligned}
D_{t^{\prime}+T_{i}} & \leq D_{t^{\prime}}-10 \mu \sqrt{d_{i+1}} \cdot \frac{1}{5 \mu} \sqrt{d_{i+1}}+\frac{1}{\mu}\left(80 \frac{1}{C} \mu \sqrt{d_{i+1}}+4\right) \\
& =D_{t^{\prime}}-2 d_{i+1}+\frac{80}{C} \sqrt{d_{i+1}}+\frac{4}{\mu}
\end{aligned}
$$

Since $K=2^{-\ell-1} n \leq d_{i+1}$ was chosen sufficiently large, we can assume that $-2 d_{i+1}+\frac{80}{C} \sqrt{d_{i+1}}+\frac{4}{\mu} \leq-d_{i+1}$ and thus $D_{t^{\prime}+T_{i}} \leq D_{t^{\prime}}-d_{i+1}$, that is, $D_{t^{\prime}+T_{i}}$ belongs to a later phase already. Consequently, we have that with probability at least $1-\exp (-\Omega(\mu))$, at most $T_{i}$ rounds are spend in Phase $i$.

We finally show our claim first by noting that there are only $O(\log n)$ phases, hence with probability at least $1-O(\log n) \exp (-\Omega(\mu))=1-\exp (-\Omega(\mu))$ no phase takes longer than the desired $T_{i}$ iterations, and second by computing

$$
\begin{aligned}
\sum_{i=1}^{\ell} T_{i} & \leq \ell+\sum_{i=1}^{\ell} 20 \frac{1}{C} \mu \sqrt{2^{-(i+1)} n} \leq \frac{10}{C} \mu \sqrt{n} \sum_{i=0}^{\infty}\left(2^{-1 / 2}\right)^{i} \\
& =\frac{10}{C} \mu \sqrt{n} \frac{1}{1-2^{-1 / 2}}=\frac{10(2+\sqrt{2})}{C} \mu \sqrt{n}
\end{aligned}
$$

Lemma 15 can be extended to give a time bound for subjump function as long as the target distance from the optimum is sufficiently large.

Lemma 16 Let $C$ be the constant from Lemma 14 and let $C_{\mu}$ be any constant. Consider a run of the cGA with $\mu=\omega(\log n)$ and $\mu \leq n^{C_{\mu}}$ on a subjump function $\mathcal{F}$ with jump size $k \leq \frac{1}{20} \ln n$. Let $D_{t}:=n-\left\|f_{t}\right\|_{1}$ for all $t$. Let $K=\left(8 C_{\mu}+12\right) \ln n$. Then with probability $1-O\left(\frac{1}{n}\right)$, there is a $t \leq T:=\frac{10(2+\sqrt{2})}{C} \mu \sqrt{n}$ such that $D_{t} \leq K$ or $f_{t t}<\frac{1}{3}$ for some $i \in[1 \ldots n]$.

Proof We regard the modified optimization process where we start with a run of the cGA on $\mathcal{F}$, but change the fitness function to OneMax when for the first time $D_{t} \leq K$. Clearly, this modified process satisfies our claim if and only if the original process on $\mathcal{F}$ does.

We now couple the modified process to the optimization process of the cGA with same $\mu$ value on the OneMax function. We construct this coupling as follows. For each $t=1,2, \ldots$ and each $j \in[1 \ldots 2]$ we let $r^{i j} \in[0,1]^{n}$ be a vector chosen uniformly at random. If $f_{t}$ is the frequency vector of the modified or the OneMax process, then the $j$-th sample $x^{i j} \in\{0,1\}^{n}$ in iteration $t$ of this process is defined by $x_{i}^{i j}=1$ if and only if $r_{i}^{i j} \leq f_{i i}$. Clearly, the two (marginal) processes defined this way are identically distributed to the two processes we wanted to couple. More interestingly, the two processes in the coupling are identical up to the point where the modified subjump process samples a search point in the gap region and thus before it changed the fitness to OneMax. If we denote the probability of this event happening within the first $T$ iterations by $p$, then by Lemma 15 and a union bound over the two failure probabilities, we have that with probability at least $1-(\exp (-\Omega(\mu))+p)$, within $T$ iterations the modified process has reached a $D_{t}$ value of at most $K$ or has reached a frequency below $\frac{1}{3}$.

Hence it remains to show that $p$ is sufficiently small. For this we note that by Lemma 5, the probability that in the modified subjump process before the switch to the OneMax fitness a particular search point $x^{i j}$ lies in the gap, is at most

$$
\operatorname{Pr}\left[d\left(x^{i j}\right) \leq k\right] \leq \operatorname{Pr}\left[d\left(x^{i j}\right) \leq \frac{1}{2} D_{t}\right] \leq \exp \left(-\frac{1}{8} D_{t}\right) \leq \exp \left(-\frac{1}{8} K\right) \leq n^{-C_{\mu}} n^{-1.5}
$$

where we wrote $d\left(x^{i j}\right):=n-\left\|x^{i j}\right\|$ as earlier in this work. By a union bound, $p \leq 2 T n^{-C_{\mu}} n^{-1.5}=O\left(\frac{1}{n}\right)$.

We now analyze the drift in $D_{t}$ when we are that close to the gap that we cannot assume anymore that we never sample a search point in the gap. We recall the definition of the gap by

$$
G:=G_{n k}:=\left\{x \in\{0,1\}^{n} \mid n-k<\|x\|_{1}<n\right\}
$$

and we further define $G^{+}:=G \cup\{(1, \ldots, 1)\}$.
A difficulty here, which was not treated fully rigorously in [43, Lemma 3.1], is that the event $G_{t}$ that $x^{1}$ or $x^{2}$ lie in the gap and the random variable $\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \quad$ are not independent. Consequently, the estimate $E\left[D_{t}-D_{t+1} \mid D_{t}\right]=\frac{1}{\mu}\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|\left(1-2 \operatorname{Pr}\left[G_{t}\right]\right)$ is not correct. In fact, the correlation is indeed not in our favor. When $\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|$ is large, the probability that a search point in the gap was sampled (and thus the frequency update is done in the unwanted direction) is higher. We solve this difficulty by computing an estimate for $\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|$ conditional on that at least one of the search points lies in the gap.

Lemma 17 Let $\mu$ be arbitrary (but, as always in this work, satisfying the wellbehaved frequency assumption). Let $k \in\left[1 \ldots \frac{1}{2} n-1\right]$. Consider an iteration $t$ of the cGA optimizing a subjump function with jump size $k$ started with a frequency vector $f_{t}$ such that $D_{t}:=n-\left\|f_{t}\right\|_{1} \geq 2 k$ and $f_{t} \in\left[\frac{1}{3}, 1-\frac{1}{n}\right]^{n}$. Then

$$
E\left[\mu D_{t}-\mu D_{t+1}\right] \geq \frac{1}{5} C \sqrt{D_{t}}-6 D_{t} \exp \left(-\frac{1}{8} D_{t}\right)-2
$$

where $C$ is the constant from Lemma 14.
Proof From the definition of the cGA, we note that when $x^{1}$ and $x^{2}$ are both not in $G^{+}$, then $D_{t+1}^{\prime}:=n-\left\|f_{t+1}^{\prime}\right\|_{1}$ satisfies $D_{t+1}^{\prime}=D_{t}-\frac{1}{\mu}\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|$ as if we were optimizing OneMax. In all other cases, we have $D_{t+1}^{\prime} \leq D_{t}+\frac{1}{\mu}\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|$. Consequently,

$$
\begin{aligned}
& E\left[\mu D_{t}-\mu D_{t+1}^{\prime}\right] \\
& \geq \operatorname{Pr}\left[x^{1}, x^{2} \notin G^{+}\right] E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \mid x^{1}, x^{2} \notin G^{+}\right] \\
& \quad-\operatorname{Pr}\left[\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right] E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \mid\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right] \\
& \quad=E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|\right] \\
& \quad-2 \operatorname{Pr}\left[\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right] E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \mid\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right] .
\end{aligned}
$$

When the frequencies are all at least $\frac{1}{3}$, we conclude from Lemma 14 that $E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|\right] \geq \frac{1}{5} C \sqrt{D_{t}}$.

For the contribution when search points are in $G^{+}$, we first note that the second bound of Lemma 5 (with $\delta=\frac{1}{2}$ and $D^{-}=D_{t}$ ) and $D_{t} \geq 2 k$ yield

$$
\operatorname{Pr}\left[x^{1} \in G^{+}\right] \leq \operatorname{Pr}\left[d\left(x^{1}\right) \leq \frac{1}{2} D_{t}\right] \leq \exp \left(-\frac{1}{8} D_{t}\right)
$$

Then, exploiting the symmetry between $x^{1}$ and $x^{2}$, counting the case $x^{1}, x^{2} \in G^{+}$ twice, and using again $\frac{1}{2} D_{t} \geq k$, we compute

$$
\begin{aligned}
& \operatorname{Pr}\left[\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right] E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \mid\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right] \\
& \quad \leq 2 \operatorname{Pr}\left[x^{1} \in G^{+}\right] E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \mid x^{1} \in G^{+}\right] \\
& \quad \leq 2 \operatorname{Pr}\left[x^{1} \in G^{+}\right]\left(E\left[\left|\left\|x^{1}\right\|_{1}-n\right| \mid x^{1} \in G^{+}\right]+E\left[\left|n-\left\|x^{2}\right\|_{1}\right|\right]\right) \\
& \quad \leq 2 \operatorname{Pr}\left[x^{1} \in G^{+}\right]\left(k+D_{t}\right) \\
& \quad \leq 2 \exp \left(-\frac{1}{8} D_{t}\right)\left(\frac{1}{2} D_{t}+D_{t}\right)=3 \exp \left(-\frac{1}{8} D_{t}\right) D_{t}
\end{aligned}
$$

In summary, we have

$$
E\left[\mu D_{t}-\mu D_{t+1}^{\prime}\right] \geq \frac{1}{5} C \sqrt{D_{t}}-6 D_{t} \exp \left(-\frac{1}{8} D_{t}\right)
$$

By Lemma 8, we further have $E\left[\mu D_{t+1}-\mu D_{t+1}^{\prime}\right] \leq 2$. Consequently, recalling that the linearity of expectation holds also for dependent random variables, we have

$$
\begin{aligned}
E\left[\mu D_{t}-\mu D_{t+1}\right] & =E\left[\mu D_{t}-\mu D_{t+1}^{\prime}\right]-E\left[\mu D_{t+1}-\mu D_{t+1}^{\prime}\right] \\
& \geq \frac{1}{5} C \sqrt{D_{t}}-6 D_{t} \exp \left(-\frac{1}{8} D_{t}\right)-2
\end{aligned}
$$

From Lemma 17, we obtain the following coarse estimate for the time to reach a frequency distance $D_{t}$ below $2 k$ (or at least below some constant).

Lemma 18 Let $k \in\left[1 \ldots \frac{n}{2}-1\right]$. Consider a run of the cGA with arbitrary hypothetical population size $\mu$ (satisfying the well-behaved frequency assumption) and started with a fixed frequency vector $f_{0}$ instead of the usual initialization $f_{0}=\left(\frac{1}{2}, \ldots, \frac{1}{2}\right)$. For all $t \geq 0$, let $D_{t}:=n-\left\|f_{t}\right\|_{1}$. Let $D^{\prime \prime} \geq 2 k$ and at least some sufficiently large constant (depending on the constant $C$ from Lemma 14). Let $T$ be the first time $t$ that this run reaches a frequency vector $f_{t}$ with $D_{t}<D^{\prime \prime}$ or that there is a frequency $f_{0}$ that is less than $\frac{1}{3}$. Then

$$
E[T] \leq \mu D_{0}
$$

Proof Based on the run of the cGA, we define a random process $\bar{D}_{t}$ as follows. If for some $s \in[0 \ldots t]$ we have $D_{s}<D^{\prime \prime}$ or there is an $i \in[1 \ldots n]$ with $f_{i s}<\frac{1}{3}$, then $\bar{D}_{t}=0$. Otherwise, we let $\bar{D}_{t}=D_{t}$. In other words, the process $\left(\bar{D}_{t}\right)$ agrees with $\left(D_{t}\right)$ while $\left(D_{t}\right)$ is at least $D^{\prime \prime}$ and there is no frequency below $\frac{1}{3}$, and then is constant zero.

By Lemma 17 and using our assumption that $D^{\prime \prime}$ is a large absolute constant, we have $E\left[\bar{D}_{t}-\bar{D}_{t+1}\right] \geq \frac{1}{\mu}$ whenever $D_{t} \geq D^{\prime \prime}$ and $f_{t} \in\left[\frac{1}{3}, 1\right]^{n}$, that is, we have $E\left[\bar{D}_{t}-\bar{D}_{t+1} \mid \bar{D}_{t}>0\right] \geq \frac{1}{\mu}$ for all $t \geq 0$.

Since $T=\inf \left\{t \geq 0 \mid \bar{D}_{t}=0\right\}$, the additive drift theorem (Theorem 7(i)) yields $E[T] \leq \frac{D_{0}}{1 / \mu}$.

We end this section of preliminary results with an argument showing that the frequencies stay away from the lower boundary for a decent amount of time. On the formal level, this argument will be used to argue that at the times $T$ estimated

on Lemmas 16 and 18, we have the desired small $D_{t}$ value and not the case that a frequency went below $\frac{1}{3}$. On the intuitive level, this argument is necessary for two reasons. On the one hand, as can be seen from the proof or via simple counterexamples, a lower bound for the probability of sampling the optimum such as Lemma 10 is not anymore true if arbitrarily small frequencies are allowed. On the other hand, small frequencies support that the two offspring sampled in one iteration agree in the corresponding bit. In this case, no change of the frequency is possible, which slows down the progress and rules out progress guarantees such as Lemma 17.

A guarantee that all frequencies stay away from the lower boundary in a run of the cGA on jump functions was also given in [43, Lemma 2.4]. Unfortunately, the proof appears not complete to us. It seems to us that the main technical prerequisite of this result, Lemma 2.2 in [43] with a proof of a little over one page in the condensed proceedings style, is not correct for two reasons. Since the proof of Lemma 2.2 never refers to the frequency boundaries, it is not clear if it is applicable for the cGA with these boundaries. Rather, a frequency vector having one entry $f_{i t}=\frac{1}{n}$ and another one $f_{j t}=1-\frac{1}{n}$ seems to be a counter-example (note that the frequency vector is called $p_{t}$ instead of $f_{t}$ in [43]). However, also for the case without boundaries counter-examples seem to exist for all values of $\mu$, e.g., the frequency vector $f_{t}=\left(\frac{1}{100}, \frac{1}{2}\right)$.

We did not see how to repair the otherwise elegant argument via the AzumaHoeffding inequality. For this reason, using a sequence of elementary reductions, we argue that the true random process of a frequency, which is not a Markov process when regarding one frequency in isolation, can be pessimistically replaced by a fair random walk on an unbounded frequency domain. For the analysis of the latter, classic Chernoff bounds can be used. This general approach was also taken in [29], however in the easier situation that there are no frequency boundaries (apart from the trivial boundaries, which are absorbing). For this reason, some additional arguments are necessary in our situation.

Lemma 19 Let $\mu$ be arbitrary (except that it satisfies the well-behaved frequency assumption). Let $\varepsilon>0$. Let $Z_{0}, Z_{1}, \ldots$ be any random process on $F_{\mu}$ (defined in (1)) such that
(i) $Z_{0}=\frac{1}{2}$,
(ii) for all $t=0,1, \ldots$ such that $Z_{t} \geq \frac{1}{2}-\varepsilon$ there are numbers $p_{t}, q_{t}, r_{t} \in[0,1]$, depending on $Z_{0}, Z_{1}, \ldots, Z_{t}$, such that $p_{t}+q_{t}+r_{t}=1$ and

$$
\begin{gathered}
\operatorname{Pr}\left[Z_{t+1}=Z_{t} \mid Z_{0}, \ldots, Z_{t}\right]=p_{t} \\
\operatorname{Pr}\left[Z_{t+1}=Z_{t}+\frac{1}{\mu} \mid Z_{0}, \ldots, Z_{t}\right]=q_{t} \\
\operatorname{Pr}\left[Z_{t+1}=Z_{t}-\frac{1}{\mu} \mid Z_{0}, \ldots, Z_{t}\right]=r_{t}
\end{gathered}
$$

We further assume that $q_{t} \geq r_{t}$ when $Z_{t} \neq 1-\frac{1}{n}$.
Then for all $T \in \mathbb{N}$,

$$
\operatorname{Pr}\left[\exists t \in\left[0 \ldots T\right]: Z_{t}<\frac{1}{2}-\varepsilon\right] \leq 2 \exp \left(-\frac{\mu^{2} \varepsilon^{2}}{2 T}\right)
$$

Proof For the ease of the argument, we can without loss of generality assume that condition (ii) also holds when $Z_{t}<\frac{1}{2}-\varepsilon$. We conduct a sequence of reductions to a fair unbiased random walk on an infinite line. We first observe that we can assume $p_{t}=0$ for all $t$. The event $Z_{t+1}=Z_{t}$ that the process does not move only slows down the process in the sense that it visits fewer states, and thus is less likely to approach the lower boundary.

We now argue that w.l.o.g. we can assume that $q_{t}=r_{t}=\frac{1}{2}$ for all $t \in[0 \ldots T-1]$ except in the cases $Z_{t} \in\left\{\frac{1}{n}, 1-\frac{1}{n}\right\}$. To make this argument formal, we inductively modify $q_{t}$ and $r_{t}$ in the time interval $t \in[0 \ldots T-1]$. The modified process will be denoted by $\left(\tilde{Z}_{t}\right)_{t=0, \ldots, T}$ and described via $\tilde{q}_{t}$ and $\tilde{r}_{t}, t \in[0 \ldots T-1]$, which again are functions of $\tilde{Z}_{0}, \ldots, \tilde{Z}_{t}$. We start with $\left(\tilde{Z}_{t}\right)$ being a copy of $\left(Z_{t}\right)$. We denote by

$$
\begin{aligned}
& P_{i t}:=\operatorname{Pr}\left[\exists s \in\left[t \ldots T\right]: Z_{s}<\frac{1}{2}-\varepsilon \mid Z_{t}=i\right] \\
& \tilde{P}_{i t}:=\operatorname{Pr}\left[\exists s \in\left[t \ldots T\right]: \tilde{Z}_{s}<\frac{1}{2}-\varepsilon \mid \tilde{Z}_{t}=i\right]
\end{aligned}
$$

the "failure probabilities" of both processes given a particular starting point and time.

Assume that $\left(\tilde{Z}_{t}\right)$ is such that for some $t_{0} \in[1 \ldots T]$ we have that for all $s \in\left[t_{0} \ldots T-1\right]$
(i) $\tilde{q}_{s}=\tilde{r}_{s}=\frac{1}{2}$ regardless of $\tilde{Z}_{0}, \ldots, \tilde{Z}_{s}$ (except in the boundary cases $\left.\tilde{Z}_{s} \in\left\{\frac{1}{n}, 1-\frac{1}{n}\right\}\right)$;
(ii) $P_{i s} \leq \tilde{P}_{i s}$ for all $i \in F_{\mu}$.

Note that our initial copy $\left(\tilde{Z}_{t}\right)$ satisfies these conditions for $t_{0}=T$. We now modify $\left(\tilde{Z}_{t}\right)$ so that the new process satisfies these conditions already for $t_{0}-1$. To this end, let $\left(Z_{t}^{\prime}, q_{t}^{\prime}, r_{t}^{\prime}\right)$ be a copy of $\left(\tilde{Z}_{t}, \tilde{q}_{t}, \tilde{r}_{t}\right)$ expect that we define $q_{t_{0}-1}^{\prime}=r_{t_{0}-1}^{\prime}=\frac{1}{2}$ (except in the boundary cases $Z_{t_{0}-1}^{\prime} \in\left\{\frac{1}{n}, 1-\frac{1}{n}\right\}$ ). Since from time $t_{0}$ on $\left(Z_{t}^{\prime}\right)$ equals $\left(\tilde{Z}_{t}\right)$, we have $P_{i s}^{\prime}=\tilde{P}_{i s} \geq P_{i s}$ for all $i \in F_{\mu}$. Since further from time $t_{0}$ on $\left(Z_{t}^{\prime}\right)$ and $\left(\tilde{Z}_{t}\right)$ are a fair random walks with reflecting boundaries, a simple coupling argument shows $P_{i-1 / \mu, t_{0}}^{\prime} \geq P_{i+1 / \mu, t_{0}}^{\prime}$ for all $i \in F_{\mu} \backslash\left\{\frac{1}{n}, 1-\frac{1}{n}\right\}$. From this, $\tilde{r}_{t_{0}-1} \leq \tilde{q}_{t_{0}-1}$, and $\tilde{r}_{t_{0}-1}+\tilde{q}_{t_{0}-1}=1$, we obtain for all $i \in F_{\mu} \backslash\left\{\frac{1}{n}, 1-\frac{1}{n}\right\}$ that

$$
\begin{aligned}
P_{i, t_{0}-1}^{\prime} & =\frac{1}{2} P_{i-1 / \mu, t_{0}}^{\prime}+\frac{1}{2} P_{i+1 / \mu, t_{0}}^{\prime} \\
& \geq \tilde{r}_{t_{0}-1} P_{i-1 / \mu, t_{0}}^{\prime}+\tilde{q}_{t_{0}-1} P_{i+1 / \mu, t_{0}}^{\prime}=\tilde{P}_{i, t_{0}-1} \geq P_{i, t_{0}}
\end{aligned}
$$

In the boundary cases, we trivially have $P_{1 / n, t_{0}-1}^{\prime}=1=P_{1 / n, t_{0}-1}$ and $P_{1-1 / n, t_{0}-1}^{\prime}=P_{1-1 / n-1 / \mu, t_{0}}^{\prime}=\tilde{P}_{1-1 / n-1 / \mu, t_{0}} \geq P_{1-1 / n-1 / \mu, t_{0}}=P_{1-1 / n, t_{0}-1}$. This proves our claim. An elementary induction gives a process $\left(\tilde{Z}_{t}\right)$ that satisfies (i), (ii) above from $t_{0}=0$ on. This process, then, is a simple unbiased random walk with reflecting

boundaries. From (ii) we see that such an unbiased random walk is not better than the original process $\left(Z_{t}\right)$ in terms of avoiding to go below $\frac{1}{2}-\varepsilon$.

Hence we can now assume that $\left(Z_{t}\right)$ is an unbiased random walk on $F_{\mu}$ with reflecting boundaries. We shall show that

$$
\operatorname{Pr}\left[\exists t \in\left[0 \ldots T\right]: Z_{t} \notin\left[\frac{1}{2}-\varepsilon, \frac{1}{2}+\varepsilon\right]\right] \leq 2 \exp \left(-\frac{\mu^{2} \varepsilon^{2}}{2 T}\right)
$$

Being interested in the event that the process reaches a state outside $\left[\frac{1}{2}-\varepsilon, \frac{1}{2}+\varepsilon\right]$ at least once, we can also drop the boundary conditions and assume that we have $Z_{t+1} \in\left\{Z_{t}-\frac{1}{\mu}, Z_{t}+\frac{1}{\mu}\right\}$ uniformly at random at all times $t$. We can now rewrite the $Z_{t}$ as follows. Let $X_{1}, \ldots, X_{T}$ be independent random variables uniformly distributed on $\left\{-\frac{1}{\mu}, \frac{1}{\mu}\right\}$. Define $Z_{t}^{\prime \prime}:=\frac{1}{2}+\sum_{i=1}^{t} X_{t}$ for all $t \in[0 \ldots T]$. Then $\left(Z_{0}, \ldots, Z_{T}\right)$ and $\left(Z_{0}^{\prime \prime}, \ldots, Z_{T}^{\prime \prime}\right)$ are identically distributed. Consequently, we can apply to $\left(Z_{t}\right)$ and $\left(Z_{t}^{\prime \prime}\right)$ the additive Chernoff bound in the sharper version working also for partial sums, Theorem 6, and obtain

$$
\begin{aligned}
& \operatorname{Pr}\left[\exists t \in\left[0 \ldots T\right]: Z_{t} \notin\left[\frac{1}{2}-\varepsilon, \frac{1}{2}+\varepsilon\right]\right] \\
& \quad=\operatorname{Pr}\left[\exists t \in\left[0 \ldots T\right]:\left|Z_{t}-E\left[Z_{t}\right]\right|>\varepsilon\right] \\
& \quad \leq 2 \exp \left(-\frac{2 \varepsilon^{2}}{T\left(\frac{2}{\mu}\right)^{2}}\right)=2 \exp \left(-\frac{\mu^{2} \varepsilon^{2}}{2 T}\right)
\end{aligned}
$$

To apply Lemma 19, we need a deeper understanding of the random process describing a single frequency. For this, we build on the following estimate of the expected change of a frequency that is not affected by the boundaries in the OneMax process. This result was proven in [64, Lemma 3].

Lemma 20 Let $\mu$ be arbitrary (but satisfying the well-behaved frequency assumption). Consider a run of the cGA optimizing OneMax. Consider an iteration starting with a frequency vector $f_{i}$. Let $i \in[1 \ldots n]$ be such that $\frac{1}{n}+\frac{1}{\mu} \leq f_{i i} \leq\left(1-\frac{1}{n}\right)-\frac{1}{\mu}$. Then

$$
E\left[f_{i, t+1}-f_{i t}\right] \geq \frac{2}{11} \frac{f_{i t}\left(1-f_{i t}\right)}{\mu}\left(\sum_{j \neq i} f_{j i}\left(1-f_{j t}\right)\right)^{-1 / 2}
$$

From Lemmas 19 and 20, we now obtain the following lower bound guarantee for the frequencies in the optimization process on subjump functions. Regarding the restriction $k \geq 17$, we recall that a subjump function with jump size smaller than 17 also is a subjump function with jump size 17. The lemma thus applies also to these (in a suitable manner). We could have alternatively formulated the lemma for all $k$ and defined $D^{\prime \prime}=\max \{2 k+1,35\}$.

Lemma 21 Let $k \in[1 \ldots n]$ be arbitrary. Consider the run of the cGA with hypothetical population size $\mu$ on a subjump function with jump size $k \geq 17$. Let $D_{t}=n-\left\|f_{t}\right\|_{1}$ for all $t$. Let $D^{\prime \prime}=2 k+1$ and $T^{\prime \prime}=\inf \left\{t \geq 0 \mid D_{t} \leq D^{\prime \prime}\right\}$. Then for all $T \in \mathbb{N}$, with $T^{\prime \prime \prime}:=\min \left\{T^{\prime \prime}, T\right\}$, we have

$$
\operatorname{Pr}\left[\exists i \in[1 \ldots n] \exists t \in\left[0 \ldots T^{\prime \prime \prime}\right]: f_{i t}<\frac{1}{3}\right] \leq 2 n \exp \left(-\frac{\mu^{2}}{72 T}\right)
$$

Proof Consider some time $t$ such that $f_{t} \in\left[\frac{1}{3}, 1\right]^{n}$ and $D_{t} \geq D^{\prime \prime}$. Consider a fixed bit $i \in[1 \ldots n]$ such that $f_{i t} \neq 1-\frac{1}{n}$. If we were optimizing the OneMax function, then by Lemma 20,

$$
\begin{aligned}
& \operatorname{Pr}\left[f_{i, t+1}=f_{i t}+\frac{1}{\mu}\right]-\operatorname{Pr}\left[f_{i, t+1}=f_{i t}-\frac{1}{\mu}\right] \\
& \quad=\mu E\left[f_{i, t+1}-f_{i t}\right] \\
& \quad \geq \frac{2}{11} f_{i t}\left(1-f_{i t}\right)\left(\sum_{j \neq i} f_{j t}\left(1-f_{j t}\right)\right)^{-1 / 2} \\
& \quad \geq \frac{2}{11} f_{i t}\left(1-f_{i t}\right)\left(D_{t}\right)^{-1 / 2}
\end{aligned}
$$

Regardless of whether we optimize OneMax or a subjump function, the events $f_{i, t+1}=f_{i t}+\frac{1}{\mu}$ and $f_{i, t+1}=f_{i t}-\frac{1}{\mu}$ can only occur when the two search points sampled in this iteration satisfy $x_{i}^{1} \neq x_{i}^{2}$. The definition of $f_{i, t+1}$ in the subjump case differs from the OneMax case at most when at least one of $x^{1}$ and $x^{2}$ lie in the gap $G_{n k}$. Hence the following coarse correction of the above estimate is valid for the optimization of subjump functions of jump size $k$.

$$
\begin{aligned}
& \operatorname{Pr}\left[f_{i, t+1}=f_{i t}+\frac{1}{\mu}\right]-\operatorname{Pr}\left[f_{i, t+1}=f_{i t}-\frac{1}{\mu}\right] \\
& \quad \geq \frac{2}{11} f_{i t}\left(1-f_{i t}\right)\left(D_{t}\right)^{-1 / 2}-\operatorname{Pr}\left[\left(x_{i}^{1} \neq x_{i}^{2}\right) \wedge\left(\left\{x^{1}, x^{2}\right\} \cap G_{n k} \neq \emptyset\right)\right]
\end{aligned}
$$

We now estimate this correction term. We note that

$$
\begin{aligned}
& \operatorname{Pr}\left\{\left(x_{i}^{1} \neq x_{i}^{2}\right) \wedge\left(\left\{x^{1}, x^{2}\right\} \cap G_{n k} \neq \emptyset\right)\right] \\
& \quad=\operatorname{Pr}\left[x_{i}^{1} \neq x_{i}^{2}\right] \cdot \operatorname{Pr}\left[\left\{x^{1}, x^{2}\right\} \cap G_{n k} \neq \emptyset \mid x_{i}^{1} \neq x_{i}^{2}\right]
\end{aligned}
$$

By symmetry and the union bound, we have

$$
\operatorname{Pr}\left[\left\{x^{1}, x^{2}\right\} \cap G_{n k} \neq \emptyset \mid x_{i}^{1} \neq x_{i}^{2}\right] \leq 2 \operatorname{Pr}\left[x^{1} \in G_{n k} \mid x_{i}^{1} \neq x_{i}^{2}\right]
$$

Conditional on $x_{i}^{1} \neq x_{i}^{2}$, the bit string $x^{1}$ is sampled from Sample $\left(f_{t}\right)$, however, conditional on the $i$-th bit being zero or one. In either case, to have $x^{1} \in G_{n k}$, we need that $\bar{D}=\sum_{j \neq i}\left(1-x_{j}^{1}\right)$ is at most $k \leq \frac{1}{2}\left(D_{t}-1\right)$, where we recall that $D_{t} \geq D^{\prime \prime}=2 k+1$. Since $E[\bar{D}]=D_{t}-\left(1-f_{i t}\right) \geq D_{t}-1$, by Lemma 5 with $\delta=\frac{1}{2}$ this event happens with probability at most $\exp \left(-\frac{1}{8}\left(D_{t}-1\right)\right)$. Together with $\operatorname{Pr}\left[x_{i}^{T} \neq x_{i}^{2}\right]=2 f_{i t}\left(1-f_{i t}\right)$, we obtain

$$
\begin{aligned}
& \operatorname{Pr}\left[f_{i, t+1}=f_{i t}+\frac{1}{\mu}\right]-\operatorname{Pr}\left[f_{i, t+1}=f_{i t}-\frac{1}{\mu}\right] \\
& \quad \geq \frac{2}{11} f_{i t}\left(1-f_{i t}\right)\left(D_{t}\right)^{-1 / 2}-2 f_{i t}\left(1-f_{i t}\right) \exp \left(-\frac{1}{8}\left(D_{t}-1\right)\right)
\end{aligned}
$$

which is non-negative since $D_{t} \geq D^{\prime \prime}=2 k+1 \geq 35$.
Consequently, the process $\left(f_{i t}\right)$, satisfies the assumptions of Lemma 19 up to time $T^{\prime \prime}$. If $T^{\prime \prime}<T$, we artificially extend the process (for the following argument only) by setting $f_{i t}=f_{i T^{\prime \prime}}$ for all $t \in\left[T^{\prime \prime}+1 \ldots T\right]$. We apply Lemma 19 to this extended process and obtain that up to time $T$, the $i$-th frequency is always at least $\frac{1}{3}$ with probability $1-2 \exp \left(-\frac{\mu^{2}}{22 T}\right)$. With a union bound over the $n$ frequencies, we have $f_{i} \in\left[\frac{1}{3}, 1\right]^{n}$ up to time $T$ with probability at least $1-2 n \exp \left(-\frac{\mu^{2}}{72 T}\right)$ in the extended process, and up to time $T^{\prime \prime \prime}$ in the true process.

# 4.3 Proof of Theorem 13 

We are now ready to formulate the full proof of our main upper bound result.
Proof of Theorem 13 To allow the reader to easily check that all implicit constants can be chosen in a way that they give the claimed result, we make these constants explicit in the following proof, but note that for most of them it just suffices to choose them sufficiently large.

We consider the optimization of a subjump function $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$ with jump size $k \leq \frac{1}{20} \ln (n)-1$. Without loss of generality, we can assume that $k \geq 17 .{ }^{3}$

Let $\mu \geq c_{\mu} \sqrt{n} \ln (n)$ for a constant $c_{\mu}$ to be defined in a moment. Assume further that for some constant $C_{\mu}$ we have $\mu \leq n^{C_{\mu}}$. Without loss of generality, we assume that $C_{\mu} \geq 1$.

Consider a run of the cGA with hypothetical population size $\mu$ on $\mathcal{F}$. Let $D_{t}:=n-\left\|f_{i}\right\|_{1}$ for all $t \geq 0$.

Let $D^{\prime}:=C_{D^{\prime}} \ln n$, where $C_{D^{\prime}} \geq 8 C_{\mu}+12$ is a constant. Let $T^{\prime}$ be the first time that $D_{t} \leq D^{\prime}$ or that there is a frequency $f_{i t}$ that is less than $\frac{1}{3}$. By Lemma 16, with probability at least $1-O\left(\frac{1}{n}\right)$ we have $T^{\prime} \leq \frac{10(2+\sqrt{2})}{C} \mu \sqrt{n}$, where $C$ is the constant from Lemma 14.

Let $D^{\prime \prime}:=\max \left\{2 k+1, C_{D^{\prime \prime}}\right\}$, where $C_{D^{\prime \prime}}$ is a sufficiently large constant (that depends only on the constant $C$ from Lemma 14). Let $T^{\prime \prime}$ be the first time that $D_{t}<D^{\prime \prime}$ or that there is a frequency $f_{i t}$ that is less than $\frac{1}{3}$. By Lemma 18, we have $E\left[T^{\prime \prime}-T^{\prime}\right]=O(\mu \log n)$. Hence a simple Markov bound gives $T^{\prime \prime} \leq T^{\prime}+\mu n^{0.4} \ln n$ with probability $1-O\left(n^{-0.4}\right)$.

Finally, let $c_{T}:=\frac{10(2+\sqrt{2})}{C}+1$ and assume that $c_{\mu} \geq 144 c_{T}$. Using our assumption that $k \geq 17$, we first invoke Lemma 21 with $T=c_{T} \mu \sqrt{n}$ and obtain that up to time $T^{\prime \prime \prime}=\min \left\{T^{\prime \prime}, T\right\}$, all frequencies are at least $\frac{1}{3}$ with probability

[^0]
[^0]:    ${ }^{3}$ In fact, we could just assume that $k=\left\lfloor\frac{1}{20} \ln (n)\right\rfloor-1$, but we find it more insightful to present the proof in a way that the arguments are adjusted to the true value of $k$ (assuming it to be at least 17 ).

$1-2 n \exp \left(-\frac{\mu^{2}}{72 T}\right) \geq 1-2 n \exp \left(-\frac{\mu}{72 c_{T} \sqrt{n}}\right) \geq 1-2 n \exp \left(-\frac{c_{p}}{72 c_{T}} \ln n\right)=1-O\left(\frac{1}{n}\right)$ by choice of $c_{\mu}$.

Putting these three arguments together, we see that with probability $1-O\left(\frac{1}{n}\right)-O\left(n^{-0.4}\right)-O\left(\frac{1}{n}\right)=1-O\left(n^{-0.4}\right)$, there is a time $t=O(\mu \sqrt{n})$ such that $D_{t} \leq D^{\prime \prime} \leq \frac{1}{10} \ln (n)$ and $\tilde{f}_{t} \in\left[\frac{1}{3}, 1\right]^{n}$. By Lemma 11, we now find the optimum in $O\left(\frac{\mu}{\log \frac{n}{n}}\right)$ iterations with probability $1-n^{-o(1)}$. This shows that the total runtime is $O(\mu \sqrt{n})$ with probability $1-O\left(n^{-0.4}\right)-n^{-o(1)}=1-O\left(n^{-0.4}\right)$.

Let us remark that we did not try to optimize the implicit constants, nor did we try to find the largest constant $C_{k}$ such that the $O(n \log n)$ runtime guarantee holds for all $k \leq C_{k} \ln (n)-1$. We further note that all but one argument in the above proof, by choosing the constants right, would give a success probability of $1-n^{-c}$, where $c$ can be any constant. This is not true for the Markov bound argument in the analysis of the time to reach a $D_{t}$ value of at most $D^{\prime \prime}$. Without further details, we note that also for this phase an arbitrary inverse-polynomial failure probability could be obtained with stronger methods.

Finally, we note that by taking $k=1$, our result also applies to the OneMax function.

# 4.4 General Insights From This Proof 

Our result that the cGA can cross small fitness valleys at no extra cost, whereas many EAs pay an $\Omega\left(n^{k}\right)$ price for this, raises the question why these algorithms differ that significantly. From our proof, we obtain the following insight.

To ease the presentation, we take as point of comparison the simple $(1+1)$ EA, but as discussed earlier, similar behaviors are observed for many other muta-tion-based EAs. Again, when talking about the cGA, we measure the progress via the frequency distance $D_{t}=n-\left\|f_{t}\right\|$, which is the expected fitness distance of a sample. For the $(1+1)$ EA, naturally, we regard the Hamming distance $d\left(x_{t}\right)=n-\operatorname{ONEMAX}\left(x_{t}\right)$ of the current solution $x_{t}$ from the optimum.

We observe that both algorithms easily reach a distance of $O(k)$. For the cGA this is "only" $O(k)$ and for the $(1+1)$ EA this is exactly $k$, but this difference is not important. The important difference is that from such a state, the $(1+1)$ EA samples the optimum only with probability $O\left(n^{-k}\right)$, whereas the cGA does so with probability $\exp (-\Omega(k))$, at least when $f_{t} \in\left[\frac{1}{3}, 1\right]^{n}$.

A first observation is that the cGA samples solutions with higher variance. This is easiest visible from Lemma 14, which implies that with constant probability the distance $d(y)$ of a sample $y$ is $\Omega\left(\sqrt{D_{t}}\right)$ away from the expected distance $E[d(y)]=D_{t}$.

For the $(1+1)$ EA, the sampling variance is much smaller. Since the number of bits that are flipped in a mution follows a binomial distribution with parameters $n$ and $\frac{1}{n}$, which is asymptotically a Poisson distribution with parameter $\lambda=1$, we see that larger fitness changes can only occur with relatively small probability (e.g., a super-constant fitness change happens only with probability $o(1)$, a fitness change of $\delta$ happens with probability at most $\left.\delta^{-\Omega(\delta)}\right)$.

The reason for this low sampling variance of the $(1+1)$ EA, obviously, is the small mutation rate of $\frac{1}{n}$ usually employed. However, raising the mutation rate does not solve the problem and, in fact, creates new problems. When using a larger mutation rate, then the expected OneMax fitness of the offspring gets worse. If $x$ is a search point with distance $d(x)=k=O(\log n)$ and $y$ is obtained from $x$ via standardbit mutation with mutation rate $p$, then the expected distance of $y$ from the optimum is $E[d(y)]=d(x)+p n(1-2 d(x) / n)$.

Clearly, worsening the expected quality of the offspring can only make sense if there is a clear gain from this. Unfortunately, there is no such gain. Indeed, when using a larger mutation rate $p$, then the expected distance $d(y)$ has a larger variance. However, this variance mostly works into the wrong direction. When not only looking at the first or second moment, but at the precise distribution, then we see that the distance gain or loss is distributed as $d(x)-d(y) \sim-X_{n-k, p}+X_{k, p}$, where $X_{n-k, p}$ and $X_{k, p}$ are independent random variables following binomial laws with parameters $(n-k, p)$ and $(k, p)$, respectively. Consequently, a positive gain can only stem from the $X_{k, p}$ part, which (unless $p$ is ridiculously large) again has a small variance since $k$ is small.

In summary, we see that regardless of how we set the mutation rate, the $(1+1)$ EA only with relatively small probability reduces the distance by a larger amount. This is caused by a generally small sampling variance when $p$ is small, say $p=\frac{1}{n}$, or by the fact that the distribution of the distance change is highly asymmetric in the way that true distance reductions are unlikely (when $p$ is larger).

For the cGA, things are different. Assuming for simplicity a frequency vector $f_{t}=\left(1-\frac{2 k}{n}\right) \mathbf{1}_{n}$, then the fitness gain of a sample $y$ over the expectation is distributed like $D_{t}-\bar{d}(y) \sim X_{n, \frac{2 k}{n}}$, where again $X_{n, \frac{2 k}{n}}$ denotes a random variable following a binomial law with parameters $n$ and $\frac{2 k}{n}$. While this distribution is not perfectly symmetric, it is not too strongly concentrated in both directions and thus allows larger improvements with reasonable probability, in particular, sampling the optimum with probability $\exp (-O(k))$. This substantially different way how solutions are sampled seems to be the key to the significantly better performance of the cGA on jump functions.

# 5 An Exponential Lower Bound 

We now prove that the cGA, regardless of the value of the parameter $\mu$, optimizes jump functions in a time that is at least exponential in the jump size $k$.

As for our upper bound result, also this lower bound is valid for a broader class of functions. We say that a function $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$ is a superjump function with jump size $k$ if it has a unique global maximum $x^{*}$ and for all $r \in[1 \ldots k-1]$ and $x, y \in\{0,1\}^{n}$ with $H\left(x, x^{*}\right)=r$ and $H\left(y, x^{*}\right)=r+1$ we have $\mathcal{F}(x)<\mathcal{F}(y)$; here we recall the definition

$$
H(x, y):=\left\{i \in[1 \ldots n] \mid x_{i} \neq y_{i}\right\}
$$

of the Hamming distance between the bit strings $x$ and $y$ of length $n$. In other words, $\mathcal{F}$ has a unique global maximum and is fully deceptive in a ball of radius $k$ around this optimum: search points closer to the optimum have a lower fitness. Clearly, all jump functions with jump size $k$ or larger are superjump functions with jump size $k$. Also, by arbitrarily modifying a jump function outside the gap region and in a way that the global optimum remains the unique global optimum, we obtain superjump functions.

We now show the following result.
Theorem 22 There are constants $\alpha_{1}, \alpha_{2}>0$ such that for any $n$ sufficiently large and any $k \in[1 \ldots n]$, regardless of the hypothetical population size $\mu$, the runtime of the cGA on any superjump function with jump size $k$ with probability $1-\exp \left(-\alpha_{1} k\right)$ is at least $\exp \left(\alpha_{2} k\right)$. In particular, the expected runtime is exponential in $k$.

We note that we intentionally prove a runtime bound that holds with high probability. The reason is that, as discussed in Sect. 2.4, EDAs may with small probability reach states from which they find it very hard to reach the optimum. Such a situation could lead to a very high expected runtime even when the EDA with high probability is very efficient. For that reason, lower bounds that hold with high probability are particularly desirable for EDAs. Needless to say, a lower bound that holds with high probability immediately implies an asymptotically identical lower bound on the expected runtime.

We also note that the cGA is treating all bit-positions and the two bit values zero and one in a symmetric fashion (this property was called unbiased in [56]). Consequently, in any runtime analysis of the cGA on a pseudo-Boolean function we can assume that $(1, \ldots, 1)$ is an optimum. Since further the actions of the cGA do not depend on absolute fitness values, but only on relative ones (this property was called ranking-based in [30]), its performance is invariant under monotonic rescalings of the fitness function. For this reason, it suffices to regard superjump functions that agree with the jump function of jump size $k$ on all search points $x$ with $\|x\|_{1} \geq n-k$ (and thus also have $(1, \ldots, 1)$ as unique global optimum). To ease the presentation, we shall take this assumption in the remainder without further notice. This also allows us to continue to use the definition

$$
G_{n k}:=\left\{x \in\{0,1\}^{n} \mid n-k<\|x\|_{1}<n\right\}
$$

of the gap.
Before stating the formal proof, we briefly describe the main proof arguments on a more intuitive level. As in the previous section, we will regard the stochastic process $D_{t}:=n-\left\|f_{t}\right\|_{1}$, that is, the distance between the sum of the frequencies and its ideal value $n$. Our general argument is that this process with probability $1-\exp (-\Omega(k))$ stays above $\frac{1}{4} k$ for $\exp (\Omega(k))$ iterations. In each iteration with $D_{t} \geq \frac{1}{4} k$, the probability that the optimum is sampled is only $\exp (-\Omega(k))$, see Lemma 9. Hence there is a $T=\exp (\Omega(k))$ such that with probability $1-\exp (-\Omega(k))$, the optimum is not sampled in the first $T$ iterations.

The heart of the proof is an analysis of the process $\left(D_{t}\right)$. It is intuitively clear that once the process is below $k$, then often the two search points sampled in one iteration both lie in the gap region, which gives $D_{t}$ a positive drift (that is, a decrease of the average frequency). To turn this drift away from the target (a small $D_{t}$ value) into an exponential lower bound on the runtime, we consider the process

$$
Y_{t}=\exp \left(c \min \left\{\frac{1}{2} k-D_{t}, \frac{1}{4} k\right\}\right)
$$

that is, an exponential rescaling of $D_{t}$. Such a rescaling has recently also been used in [6]. We note that the usual way to prove exponential lower bounds is the negative drift theorem of Oliveto and Witt [59]. We did not immediately see how to use it for our purposes, though, since in our process we do not have very strong bounds on the one-step differences. E.g., when $D_{t}=\frac{1}{2} k$, then the underlying frequency vector may be such that $D_{t+1} \geq D_{t}+\sqrt{k}$ happens with constant probability. We also note that after the submission of this work, a negative multiplicative drift theorem was proposed [27], which would be applicable to our setting as well. It would, however, not greatly simplify the proof as the main work, estimating the drift of the process $\left(Y_{t}\right)$, would still be needed.

We shall show that the process $Y_{t}$ has at most a constant point-wise drift, more precisely, that

$$
E\left[Y_{t+1}-Y_{t} \mid Y_{t}=y\right] \leq 2
$$

holds for all $y<Y_{\max }:=\exp \left(\frac{c}{4} k\right)$. From this statement, the lower bound version of the additive drift theorem (Theorem 7(ii)) would immediately show that the expected time to reach a $D_{t}$ value of $\frac{k}{4}$ or less is at least exponential in $k$. However, since we aim at a runtime bound that holds with high probability, we take a different (and, in fact, more elementary) route. We regard the process $\left(\tilde{Y}_{t}\right)$ which is identical to $Y$ until $Y$ first reaches $Y_{\max }$ and then stays constant at $Y_{\max }$. This process satisfies $E\left[\tilde{Y}_{t+1}-\tilde{Y}_{t}\right] \leq 2$ for all times $t$. From this and $\tilde{Y}_{0}=Y_{0}<1$ we obtain $E\left[\tilde{Y}_{t}\right] \leq 1+2 t$. Hence for $T=\exp (\Omega(k))$ sufficiently small, we have

$$
\frac{E\left[\tilde{Y}_{T}\right]}{Y_{\max }}=\exp (-\Omega(k))
$$

and a simple Markov bound argument is enough to show that $\operatorname{Pr}\left[\tilde{Y}_{T}=Y_{\max }\right]=\exp (-\Omega(k))$. Note that $\tilde{Y}_{T}<Y_{\max }$ is equivalent to $Y_{t}<Y_{\max }$ for all $t \in[0 \ldots T]$.

The main work in the following proof is showing (3). The difficulty here is hidden in a small detail. When $D_{t} \in\left[\frac{1}{4} k, \frac{3}{4} k\right]$, and this is the most interesting case (case 2 in the formal proof), then we have $\left\|f_{t+1}^{\prime}\right\|_{1} \leq\left\|f_{t}\right\|$ whenever the two search points sampled lie in the gap region, and hence with probability $1-\exp (-\Omega(k))$; from Lemma 12 we obtain, in addition, a true decrease, that is, $\left\|f_{t+1}^{\prime}\right\|_{1} \leq\left\|f_{t}\right\|-\frac{1}{\mu}$, with constant probability. This progress of $f_{t+1}^{\prime}$ over $f_{t}$ would be perfectly fine for our purposes. Hence the true difficulty arises from the capping of the frequencies into the interval $\left[\frac{1}{n}, 1-\frac{1}{n}\right]$, that is, from the fact that the new frequency vector is $f_{t+1}:=\operatorname{minmax}\left(\frac{\pi}{n} \mathbf{1}_{n}, f_{t+1}^{\prime}\right),\left(1-\frac{1}{n}\right) \mathbf{1}_{n}$ ). This appears to be a minor problem, among

others, because only a capping at the lower bound $\frac{1}{n}$ can have an adverse effect on our process, and there are at most $O(k)$ frequencies sufficiently close to the lower boundary. Things become difficult due to the exponential scaling, which can let rare events still have a significant influence on the expected change of the process.

We now make these arguments precise and prove Theorem 22. We recall that, while the theorem refers to arbitrary superjump functions with jump size $k$, we can always assume that we regard a fitness function that agrees with the classic jump function with parameter $k$ on all search points $x$ with $\|x\|_{1} \geq n-k$, including the unique global optimum $(1, \ldots, 1)$.

Proof Since we are aiming at an asymptotic statement, we can assume in the following that $n$ is sufficiently large.

To ease the presentation of the main part of the proof, let us first give a basic argument for the case of small $k$ and then assume that $k \geq w(n)$ for some function $w: \mathbb{N} \rightarrow \mathbb{N}$ with $\lim _{n \rightarrow \infty} w(n)=\infty$.

We first note that with probability $f_{i t}^{2}+\left(1-f_{i t}\right)^{2} \geq \frac{1}{2}$, the two search points $x^{1}$ and $x^{2}$ generated in the $t$-th iteration agree in the $i$-th bit, which in particular implies that $f_{i, t+1}=f_{i t}$. Hence with probability at least $2^{-T}$, this happens for the first $T$ iterations, and thus $f_{i t}=\frac{1}{2}$ for all $t \in[0 \ldots T]$. Let us call such a bit position $i$ idle.

Note that the events of being idle are independent for all $i \in[1 \ldots n]$. Hence, taking $T=\left\lfloor\frac{1}{2} \log _{2} n\right\rfloor$, we see that the number $X$ of idle positions has an expectation of $E[X] \geq n 2^{-T} \geq \sqrt{n}$, and by a simple Chernoff bound (Theorem 4), we have $\operatorname{Pr}\left[X \geq \frac{1}{2} \sqrt{n}\right] \geq 1-\exp (-\Omega(\sqrt{n}))$.

Conditional on having at least $\frac{1}{2} \sqrt{n}$ idle bit positions, the probability that a particular search point sampled in the first $T$ iterations is the optimum is at most $2^{-\frac{1}{2} \sqrt{n}}$. By a simple union bound argument, the probability that at least one of the search points generated in the first $T$ iterations is the optimum is at most $2 T 2^{-\frac{1}{2} \sqrt{n}}=\exp (-\Omega(\sqrt{n}))$. In summary, we have that with probability at least $1-\exp (-\Omega(\sqrt{n}))$, the runtime of the cGA on any function with unique optimum (and in particular any superjump function) is greater than $T=\frac{1}{2} \log _{2} n$. This implies the claim of this theorem for any $k \leq C \log \log n$, where $C$ is a sufficiently small constant, and, as discussed above, $n$ is sufficiently large.

With this, we can now safely assume that $k=\omega(1)$. Since $k \leq n$ and our result is invariant under constant-factor changes of $k$, we can assume that $k \leq \frac{n}{320}$.

Let $D_{t}:=n-\left\|f_{t}\right\|_{1}=n-\sum_{i=1}^{n} f_{i t}$ be the distance of the sum of the frequencies from the ideal value $n$.

Our intuition (which will be made precise) is that the process $\left(D_{t}\right)$ finds it hard to go significantly below $k$ because there we will typically sample individuals in the gap, which leads to a decrease of the sum of frequencies (when the two individuals have different distances from the optimum). To obtain an exponential lower bound on the runtime, we suitably rescale the process by defining, for a sufficiently small constant $c$,

$$
Y_{t}=\min \left\{\exp \left(c\left(\frac{1}{2} k-D_{t}\right)\right), \exp \left(\frac{1}{4} c k\right)\right\}=\exp \left(c \min \left\{\frac{1}{2} k-D_{t}, \frac{1}{4} k\right\}\right)
$$

Observe that $Y_{t}$ attains its maximal value $Y_{\max }=\exp \left(\frac{1}{4} c k\right)$ precisely when $D_{t} \leq \frac{1}{4} k$. Also, $Y_{t} \leq 1$ for $D_{t} \geq \frac{1}{2} k$.

To argue that we have $D_{t}>\frac{1}{4} k$ for a long time, we now show that for all $y<Y_{\max }$ the drift $E\left[Y_{t+1}-Y_{t} \mid Y_{t}=y\right]$ is at most constant. To this aim, we condition on a fixed value of $f_{t}$, which also determines $D_{t}$. We treat separately the two cases that $D_{t} \geq \frac{3}{4} k$ and that $\frac{3}{4} k>D_{t}>\frac{1}{4} k$.

Case 1: Assume first that $D_{t} \geq \frac{3}{4} k$. By Lemma 5, with probability $1-\exp \left(-\Omega\left(D_{t}\right)\right) \geq 1-\exp (-\Omega(k))$, the two search points $x^{1}, x^{2}$ sampled in iteration $t+1$ both satisfy

$$
\left|\left\|x^{i}\right\|_{1}-\left\|f_{t}\right\|_{1}\right|=\left|d\left(x^{i}\right)-D_{t}\right|<\frac{1}{18} D_{t} \leq \frac{1}{6}\left(D_{t}-\frac{1}{2} k\right)
$$

Here and in the following, when writing $\Omega(k)$ we mean that there is a positive constant $C$, independent of $n, k$, and $c$, such that the expression is at least $C k$. Let us call $A$ the event described in (4). In this case, we argue as follows. We recall the notation $\sum[v]:=\sum_{i=1}^{n} v_{i}$ to denote the sum of the elements of an $n$-dimensional vector $v$ and we recall further that, with a slight abuse of notation, we defined $\left\|f^{\prime}\right\|_{1}:=\sum\left[f^{\prime}\right]$ for intermediate frequency vectors $f^{\prime}$. Let $\left\{y^{1}, y^{2}\right\}=\left\{x^{1}, x^{2}\right\}$ such that $\mathcal{F}\left(y^{1}\right) \geq \mathcal{F}\left(y^{2}\right)$. Then

$$
\begin{aligned}
\left\|f_{t+1}^{\prime}\right\|_{1} & =\sum\left[f_{t}+\frac{1}{\mu}\left(y^{1}-y^{2}\right)\right] \\
& =\sum\left[f_{t}+\frac{1}{\mu}\left(y^{1}-f_{t}\right)-\frac{1}{\mu}\left(y^{2}-f_{t}\right)\right] \\
& \leq \sum\left[f_{t}\right]+\frac{1}{\mu}\left|\sum\left[y^{1}-f_{t}\right]\right|+\frac{1}{\mu}\left|\sum\left[y^{2}-f_{t}\right]\right| \\
& =\left\|f_{t}\right\|_{1}+\frac{1}{\mu}\left|\left\|x^{1}\right\|_{1}-\left\|f_{t}\right\|_{1}\right|+\frac{1}{\mu}\left|\left\|x^{2}\right\|-\left\|f_{t}\right\|_{1}\right| \\
& \leq n-D_{t}+2 \frac{1}{\mu} \frac{1}{6}\left(D_{t}-\frac{1}{2} k\right) \\
& \leq n-D_{t}+2 \frac{1}{6}\left(D_{t}-\frac{1}{2} k\right) \\
& =n-\frac{2}{3} D_{t}-\frac{1}{6} k \leq n-\frac{2}{3} \cdot \frac{3}{4} k-\frac{1}{6} k \leq n-\frac{2}{3} k
\end{aligned}
$$

We still need to consider the possibility that $f_{i, t+1}>f_{i, t+1}^{\prime}$ for some $i \in[1 \ldots n]$. By Lemma 8, not conditioning on $A$, we have that $\left\|f_{t+1}\right\|_{1}-\left\|f_{t+1}^{\prime}\right\|_{1} \leq \frac{1}{\mu} \operatorname{Bin}(\mathscr{E}, P) \leq \operatorname{Bin}(\mathscr{E}, P) \quad$ for some $\mathscr{E} \in[1 \ldots n]$ and $P=2 \frac{1}{n}\left(1-\frac{1}{n}\right)$.

Let us call $B$ the event that $\left\|f_{t+1}\right\|_{1}-\left\|f_{t+1}^{\prime}\right\|_{1}<\frac{1}{6} k$. Note that $A \cap B$ implies $\left\|f_{t+1}\right\|_{1}<n-\frac{1}{2} k$ and thus $Y_{t+1} \leq 1$. By Lemma 3 and the estimate $\binom{a}{b} \leq\left(\frac{\omega}{b}\right)^{b}$, we have

$$
\operatorname{Pr}[\neg B] \leq\binom{\mathscr{E}}{\frac{1}{6} k} P^{k / 6} \leq\left(\frac{12 e \mathscr{E}}{k n}\right)^{k / 6} \leq k^{-\Omega(k)}
$$

We conclude that the event $A \cap B$ holds with probability $1-\exp (-\Omega(k))$; in this case $Y_{t} \leq 1$ and $Y_{t+1} \leq 1$. In all other cases, we bluntly estimate $Y_{t+1}-Y_{t} \leq Y_{\max }$. This gives

$$
E\left[Y_{t+1}-Y_{t}\right] \leq(1-\exp (-\Omega(k))) \cdot 1+\exp (-\Omega(k)) Y_{\max }
$$

By choosing the constant $c$ in the definition of $\left(Y_{t}\right)$ sufficiently small and taking $n$ sufficiently large, we have $E\left[Y_{t+1}-Y_{t}\right] \leq 2$.

Case 2: Assume now that $\frac{2}{4} k>D_{t}>\frac{1}{4} k$. Let $x^{1}, x^{2}$ be the two search points sampled in iteration $t+1$ and let $y^{1}, y^{2}$ be such that $\left\{y^{1}, y^{2}\right\}=\left\{x^{1}, x^{2}\right\}$ and $\mathcal{F}\left(y^{1}\right) \geq \mathcal{F}\left(y^{2}\right)$. By Lemma 5 again, we have $k>n-\left\|x^{i}\right\|_{1}>0$ with probability $1-\exp (-\Omega(k))$ for both $i \in\{1,2\}$. Let us call this event $A$. Note that if $A$ holds, then both offspring lie in the gap region. Consequently, $\left\|y^{1}\right\|_{1} \leq\left\|y^{2}\right\|_{1}$ and thus $\left\|f_{t+1}^{\prime}\right\|_{1} \leq\left\|f_{t}\right\|_{1}$.

Let $L=\left\{i \in\{1 \ldots n\} \mid f_{\mu}=\frac{1}{n}\right\}, \ell=|L|$, and $M=\left\{i \in L \mid x_{i}^{1} \neq x_{i}^{2}\right\}$ as in Lemma 8. Note that by definition, $D_{t} \geq\left(1-\frac{1}{n}\right) \ell$, hence from $D_{t}<\frac{2}{4} k$ and $n \geq 4$ we obtain $\ell<k$.

Let $B_{0}$ be the event that $|M|=0$, that is, $x_{|L}^{1}=x_{|L}^{2}$. Note that in this case, we have $f_{t+1} \leq f_{t+1}^{\prime}$ (component-wise) and thus

$$
\left\|f_{t+1}\right\|_{1} \leq\left\|f_{t+1}^{\prime}\right\|_{1}=\left\|f_{t}+\frac{1}{\mu}\left(y^{1}-y^{2}\right)\right\|_{1}=\left\|f_{t}\right\|_{1}+\frac{1}{\mu}\left(\left\|y^{1}\right\|_{1}-\left\|y^{2}\right\|_{1}\right)
$$

By Lemma 8, Bernoulli's inequality, and $\ell \leq k$, we have

$$
\operatorname{Pr}\left[B_{0}\right]=\left(1-2 \frac{1}{n}\left(1-\frac{1}{n}\right)\right)^{\ell} \geq 1-\frac{2 \ell}{n} \geq 1-\frac{2 k}{n}
$$

Since $\ell<k \leq \frac{n}{320}<\frac{n}{2}$, by Lemma 12, we have $\left\|x_{|\{n\}| L}^{1}\right\|_{1} \neq\left\|x_{|\{n\}| L}^{2}\right\|_{1}$ with probability at least $\frac{1}{16}$. This event, called $C$ in the following, is independent of $B_{0}$. We have

$$
\operatorname{Pr}\left[A \cap B_{0} \cap C\right] \geq \operatorname{Pr}\left[B_{0} \cap C\right]-\operatorname{Pr}[\widetilde{A}] \geq\left(1-\frac{2 k}{n}\right) \frac{1}{16}-\exp (-\Omega(k))
$$

If $A \cap B_{0} \cap C$ holds, then $\left\|f_{t+1}\right\|_{1} \leq\left\|f_{t+1}^{\prime}\right\|_{1} \leq\left\|f_{t}\right\|_{1}-\frac{1}{\mu}$. If $A \cap B_{0} \cap \bar{C}$ holds, then we still have $\left\|f_{t+1}\right\|_{1} \leq\left\|f_{t+1}^{\prime}\right\|_{1} \leq\left\|f_{t}\right\|_{1}$.

Let us now, for $j \in[1 \ldots \ell]$, denote by $B_{j}$ the event that $|M|=j$, that is, that $x_{|L}^{1}$ and $x_{|L}^{2}$ differ in exactly $j$ bits. By Lemma 8 again, we have $\operatorname{Pr}\left[B_{j}\right]=\operatorname{Pr}[\operatorname{Bin}(\ell, P)=j]$.

The event $A \cap B_{j}$ implies $\left\|f_{t+1}\right\|_{1} \leq\left\|f_{t+1}^{\prime}\right\|_{1}+\frac{j}{\mu} \leq\left\|f_{t}\right\|_{1}+\frac{j}{\mu}$ and occurs with probability $\operatorname{Pr}\left[A \cap B_{j}\right] \leq \operatorname{Pr}\left[B_{j}\right]=\operatorname{Pr}[\operatorname{Bin}(\ell, P)=j]$.

Taking these observations together, we compute

$$
\begin{aligned}
E\left[Y_{t+1}\right]= & \operatorname{Pr}[\bar{A}] E\left[Y_{t+1} \mid \bar{A}\right] \\
& +\sum_{j=1}^{\ell} \operatorname{Pr}\left[A \cap B_{j}\right] E\left[Y_{t+1} \mid A \cap B_{j}\right] \\
& +\operatorname{Pr}\left[A \cap B_{0} \cap \bar{C}\right] E\left[Y_{t+1} \mid A \cap B_{0} \cap \bar{C}\right] \\
& +\operatorname{Pr}\left[A \cap B_{0} \cap C\right] E\left[Y_{t+1} \mid A \cap B_{0} \cap C\right] \\
\leq & \exp (-\Omega(k)) Y_{\max } \\
& +\sum_{j=1}^{\ell} \operatorname{Pr}\left[\operatorname{Bin}(\ell, P)=j\right] Y_{t} \exp \left(\frac{c j}{\mu}\right) \\
& +\operatorname{Pr}[\operatorname{Bin}(\ell, P)=0] Y_{t} \\
& -\left(\frac{1}{16}\left(1-\frac{2 k}{\pi}\right)-\exp (-\Omega(k))\right) Y_{t}\left(1-\exp \left(-\frac{c}{\mu}\right)\right)
\end{aligned}
$$

We note that the second and third term amount to $Y_{t} E\left[\exp \left(\frac{c Z}{\mu}\right)\right]$, where $Z \sim \operatorname{Bin}(\ell, P)$. Writing $Z=\sum_{i=1}^{\ell} Z_{i}$ as a sum of $\ell$ independent binary random variables with $\operatorname{Pr}\left[Z_{i}=1\right]=P$, we obtain

$$
E\left[\exp \left(\frac{c Z}{\mu}\right)\right]=\prod_{i=1}^{\ell} E\left[\exp \left(\frac{c Z}{\mu}\right)\right]=\left(1-P+P \exp \left(\frac{c}{\mu}\right)\right)^{\ell}
$$

By assuming $c \leq 1$ and using the elementary estimate $e^{x} \leq 1+2 x$ valid for $x \in[0,1]$, see, e.g., Lemma 1.4.2(b) in [28], we have

$$
1-P+P \exp \left(\frac{c}{\mu}\right) \leq 1+2 P\left(\frac{c}{\mu}\right)
$$

Hence with $P \leq \frac{2}{n}, \mu \geq 1$, and $\ell \leq \frac{n}{320}$, we obtain

$$
E\left[\exp \left(\frac{c Z}{\mu}\right)\right] \leq\left(1+2 P\left(\frac{c}{\mu}\right)\right)^{\ell} \leq \exp \left(2 P\left(\frac{c}{\mu}\right) \ell\right) \leq \exp \left(\frac{4 c}{320 \mu}\right) \leq 1+\frac{c}{40 \mu}
$$

again by using $e^{x} \leq 1+2 x$. The second and third term of (5) thus add up to at most $\left(1+\frac{c}{40}\right) Y_{t}$.

In the first term of (5), we again assume that $c$ is sufficiently small to ensure that $\exp (-\Omega(k)) Y_{\max }=\exp (-\Omega(k)) \exp \left(\frac{1}{4} c k\right) \leq 1$. Recalling that $k \leq \frac{n}{320}$ and assuming $k$ sufficiently large (since $k=\omega(1)$ and $n$ is large), we finally estimate in the last term $\frac{1}{16}\left(1-\frac{2 k}{\pi}\right)-\exp (-\Omega(k)) \geq \frac{1}{20}$ and, more interestingly, $1-\exp \left(-\frac{c}{\mu}\right) \geq \frac{c}{\mu}\left(1-\frac{1}{e}\right)$ using the estimate $e^{-x} \leq 1-x\left(1-\frac{1}{e}\right)$ valid for all $x \in[0,1]$, which stems simply from the convexity of the exponential function.

With these estimates we obtain

$$
E\left[Y_{t+1}\right] \leq 1+\left(1+\frac{c}{40 \mu}\right) Y_{t}-\frac{1}{20}\left(1-\frac{1}{e}\right) \frac{c}{\mu} Y_{t} \leq 1+Y_{t}
$$

and thus $E\left[Y_{t+1}-Y_{t}\right] \leq 1$.
In summary, we have now shown that for all $y<Y_{\max }$ and at all times $t$ the process $\left(Y_{t}\right)$ satisfies $E\left[Y_{t+1}-Y_{t} \mid Y_{t}=y\right] \leq 2$. We note that $Y_{0} \leq 1$ with probability one.

For the sake of the argument, let us artificially modify the process from the point on when it has reached a state of at least $Y_{\max }$. So we define $\left(\tilde{Y}_{t}\right)$ by setting $\tilde{Y}_{t}=Y_{t}$, if $Y_{t}<Y_{\max }$ or if $Y_{t} \geq Y_{\max }$ and $Y_{t-1}<Y_{\max }$, and $\tilde{Y}_{t}=\tilde{Y}_{t-1}$ otherwise. In other words, $\left(\tilde{Y}_{t}\right)$ is a copy of $\left(Y_{t}\right)$ until it reaches a state of at least $Y_{\max }$ and then does not move anymore. With this trick, we have $E\left[\tilde{Y}_{t+1}-\tilde{Y}_{t}\right] \leq 2$ for all $t$.

A simple induction and the initial condition $\tilde{Y}_{0} \leq 1$ shows that $E\left[\tilde{Y}_{t}\right] \leq 2 t+1$ for all $t$. In particular, for $T=\frac{1}{2} \exp \left(\frac{1}{8} c k\right)-1$, we have $E\left[Y_{T}\right] \leq \exp \left(\frac{1}{8} c k\right)$ and, by Markov's inequality,

$$
\operatorname{Pr}\left[\tilde{Y}_{T} \geq Y_{\max }\right] \leq \frac{\exp \left(\frac{1}{8} c k\right)}{Y_{\max }}=\exp \left(-\frac{1}{8} c k\right)
$$

Hence with probability $1-\exp \left(-\frac{1}{8} c k\right)$, we have $\tilde{Y}_{T}<Y_{\max }$. We now condition on this event. By construction of $\left(\tilde{Y}_{t}\right)$, we have $Y_{t}<Y_{\max }$, equivalently $D_{t}>\frac{1}{4} k$, for all $t \in[0 \ldots T]$. If $D_{t}>\frac{1}{4} k$, then by Lemma 9 the probability that a sample generated in this iteration is the optimum, is at most $\exp \left(-\frac{1}{4} k\right)$. Assuming $c \leq 1$ again, we see that the probability that the optimum is generated in one of the first $T$ iterations, is at most $2 T \exp \left(-\frac{1}{4} k\right) \leq \exp \left(\frac{1}{8} c k\right) \exp \left(-\frac{1}{4} k\right)=\exp \left(-\frac{1}{8} k\right)$. This shows the claim.

# 6 An $\Omega(n \log n)$ Lower Bound 

With the exponential lower bound proven in the previous section, the runtime of the cGA on jump functions is well understood, except that the innocent looking lower bound $\Omega(n \log n)$, matching the corresponding upper bound for $k \leq \frac{1}{20} \ln n-1$ and optimal choice of $\mu$, is still missing. Since Sudholt and Witt [64] have proven an $\Omega(n \log n)$ lower bound for the simple unimodal function ONEMAX, which for many EAs is known to be one of the easiest functions with unique global optimum [18, $23,63,66]$, it would be very surprising if this lower bound would not hold for jump functions as well.

In this section, we first argue why, unlike for many other algorithms, it is hard to show that a lower bound on the runtime of the cGA on OneMax extends to a lower bound for any other function with unique optimum. We then analyze in detail the proof of the $\Omega(n \log n)$ lower bound for OneMax [64] and argue that the same arguments can be applied in the case of jump functions (but not superjump functions).

### 6.1 Domination Arguments Fail

The true reason why OneMax is the easiest optimization problem for many evolutionary algorithms $\mathcal{A}$, implicit in all such proofs and explicit in [23], is that when comparing a run of $\mathcal{A}$ on OneMax and on some other function $\mathcal{F}$ with unique global optimum, then at all times the Hamming distance between the current-best solution and the optimum in the OneMax process is stochastically dominated by the same

quantity in the other process. This follows by induction and a coupling argument from the following key insight (here formulated for the $(1+1)$ EA only).

Lemma 23 Let $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$ be some function with unique global optimum $x^{*}$ and let OneMax be the n-dimensional OneMax function with unique global optimum $y^{*}=(1, \ldots, 1)$. Let $x, y \in\{0,1\}^{n}$ such that $H\left(x, x^{*}\right) \geq H\left(y, y^{*}\right)$, where $H(\cdot, \cdot)$ denotes the Hamming distance. Consider one iteration of the $(1+1)$ EA optimizing $\mathcal{F}$, started with $x$ as parent individual, and denote by $x^{\prime}$ the parent in the next iteration. Define $y^{\prime}$ analogously for OneMax and $y$. Then $H\left(x^{\prime}, x^{*}\right) \geq H\left(y^{\prime}, y^{*}\right)$.

As a side remark, note that the lemma applied in the special case $\mathcal{F}=$ ONEMAX shows that the intuitive rule "the closer a search point is to the optimum, the shorter is the optimization time when starting from this search point" holds for optimizing OneMax via the $(1+1)$ EA.

We now show that a statement like Lemma 23 is not true for the cGA. Since the states of a run of the cGA are the frequency vectors $f$, the natural extension of the Hamming distance quality measure above is the $\ell_{1}$-distance $d\left(f, x^{*}\right)=\left\|f-x^{*}\right\|_{1}=\sum_{i=1}^{n}\left|f_{i}-x_{i}^{*}\right|$. Note that for $x^{*}=(1, \ldots, 1)$, we have $d\left(f, x^{*}\right)=n-\|f\|_{1}$, the distance measure regarded in many of the other proofs in this work.

Lemma 24 Let $n$ be even. We consider running the cGA with hypothetical population size $\mu=n$. Then there are a fitness function $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$ with unique global optimum $x^{*}=(1, \ldots, 1)$ and frequency vectors $f, g \in\left(F_{\mu}\right)^{n}$ such that the following holds. Let $\tilde{f}$ be the frequency vector obtained after one iteration of optimizing $\mathcal{F}$ via the cGA started with frequency vector $f$. Let $\tilde{g}$ be the frequency vector obtained after one iteration running the cGA on OneMax (with unique global optimum $y^{*}:=x^{*}$ ) started with $g$. Then $d\left(f, x^{*}\right) \geq d\left(g, y^{*}\right)$, but $d\left(\tilde{f}, x^{*}\right) \not \geq d\left(\tilde{g}, y^{*}\right)$.

Proof Let $\mathcal{F}$ be any subjump function with jump size $k \leq \frac{n}{2}$. Let $f=\frac{1}{2} \mathbf{1}_{n}$. Let $g \in[0,1]^{n}$ be such that half the entries of $g$ are equal to $\frac{1}{n}+\frac{1}{\mu}=\frac{2}{n}$ and the other half are equal to $1-\frac{1}{n}-\frac{1}{\mu}=1-\frac{2}{n}$.

We obviously have $d\left(f, x^{*}\right) \geq d\left(g, y^{*}\right)$, since both numbers are equal to $\frac{n}{2}$. Since with probability $1-\exp (-\Omega(n))$, both search points sampled in the jump process have between $\frac{n}{4}$ and $\frac{3}{4 n}$ ones, their jump fitnesses equal their OneMax fitnesses. Consequently, we may apply Lemma 5 from [29] (or, with one more argument, Lemma 14) and see that $E\left[d\left(\tilde{f}, x^{*}\right)\right] \leq \frac{n}{2}-\Omega\left(\frac{1}{n} \sqrt{n}\right)$. For the OneMax process started in $g$, however, denoting the two search points generated in this iteration by $x^{1}$ and $x^{2}$, we have

$$
E\left[\left\|g-\tilde{g}\right\|_{1}\right]=\sum_{i=1}^{n} \frac{1}{\mu} \operatorname{Pr}\left[x_{i}^{1} \neq x_{i}^{2}\right]=n \cdot \frac{1}{\mu} \cdot 2 \cdot \frac{2}{n}\left(1-\frac{2}{n}\right) \leq \frac{4}{n}
$$

From this and $d\left(\tilde{g}, y^{*}\right)=\left\|\tilde{g}-y^{*}\right\|_{1}=\left\|\tilde{g}-g+g-y^{*}\right\|_{1} \geq\left\|g-y^{*}\right\|_{1}-\|\tilde{g}-g\|_{1}$, we obtain

$$
E\left[d\left(\tilde{g}, y^{*}\right)\right] \geq d\left(g, y^{*}\right)-\frac{4}{\mu}=\frac{n}{2}-O\left(\frac{1}{\mu}\right)
$$

Since thus $E\left[d\left(\tilde{f}, x^{*}\right)\right] \leq E\left[d\left(\tilde{g}, y^{*}\right)\right]$, we cannot have $d\left(\tilde{f}, x^{*}\right) \geq d\left(\tilde{g}, y^{*}\right)$.

We note that a second imaginable domination result is also not true, namely that, roughly speaking, the frequency vector arising from one iteration started with a better initial frequency vector dominates the result of starting with a worse initial frequency vector. More precisely, we have the following.

Lemma 25 Let $\mu$ be an arbitrary hypothetical population size for all cGAs considered here. There are frequency vectors $f, g \in\left(F_{\mu}\right)^{n}$ with $f \leq g$ (componentwise) such that the following holds. Let $\mathcal{F}$ be any subjump function with jump size at most $\frac{n}{2}$ (including the OneMax function). Let $\tilde{f}$ be the frequency vector resulting from optimizing $\mathcal{F}$ for one iteration with the cGA started with frequency vector $f$. Let $\tilde{g}$ be the frequency vector resulting from optimizing ONEMAX for one iteration with the cGA started with frequency vector $g$. Then we do not have $\tilde{f}_{i} \preceq \tilde{g}_{i}$ for all $i \in[1 \ldots n]$.

Proof Let $f=\left(\frac{1}{2}, \frac{1}{n}, \ldots, \frac{1}{n}\right)$ and $g=\frac{1}{2} \mathbf{1}_{n}$. Clearly, $f \leq g$.
When performing one iteration of the cGA on $\mathcal{F}$ started with $f$, and denoting the two samples by $x^{1}$ and $x^{2}$ and their quality difference in all but the first bit by $\Delta=\left\|x_{\mid[2 \ldots n]}^{1}\right\|_{1}-\left\|x_{\mid[2 \ldots n]}^{2}\right\|_{1}$, then the argument that with probability $1-\exp (-\Omega(n))$ this iteration equals an iteration with OneMax as objective function shows that the resulting frequency vector $\tilde{f}$ satisfies

$$
\begin{aligned}
& \operatorname{Pr}\left[\tilde{f}_{1}=\frac{1}{2}+\frac{1}{\mu}\right] \\
& \quad \geq \operatorname{Pr}\left[x_{1}^{1} \neq x_{1}^{2}\right]\left(\frac{1}{2} \operatorname{Pr}\{\Delta \notin\{-1,0\}\}+\operatorname{Pr}\{\Delta \in\{-1,0\}\}\right)-\exp (-\Omega(n)) \\
& \quad=\operatorname{Pr}\left[x_{1}^{1} \neq x_{1}^{2}\right]\left(\frac{1}{2}+\frac{1}{2} \operatorname{Pr}\{\Delta \in\{-1,0\}\}\right)-\exp (-\Omega(n))
\end{aligned}
$$

Since $\operatorname{Pr}\{\Delta \in\{-1,0\}\} \geq \operatorname{Pr}\left\{\left\|x_{\mid[2 \ldots n]}^{1}\right\|_{1}=\left\|x_{\mid[2 \ldots n]}^{2}\right\|_{1}=0\right\}=\left(1-\frac{1}{n}\right)^{2(n-1)} \geq \frac{1}{e^{2}}$, we have $\operatorname{Pr}\left[\tilde{f}_{1}=\frac{1}{2}+\frac{1}{\mu}\right] \geq \frac{1}{4}+\frac{1}{4 e^{2}}-\exp (-\Omega(n))$.

When starting the iteration with $g$, the resulting frequency vector $\tilde{g}$ satisfies an equation analogous to (6), but now $\Delta$ is the difference of two binomial distributions with parameters $n-1$ and $\frac{1}{2}$. Hence, we have $\operatorname{Pr}\{\Delta \in\{-1,0\}\}=O\left(n^{-1 / 2}\right)$, see, e.g., [28, Lemma 1.4.13] for this elementary estimate, and thus $\operatorname{Pr}\left\{\tilde{g}_{1}=\frac{1}{2}+\frac{1}{\mu}\right\}=\frac{1}{4}+o(1)$, disproving that $\tilde{f}_{1} \preceq \tilde{g}_{1}$.

In summary, the richer mechanism of building a probabilistic model of the search space in the cGA (as opposed to using a population in EAs) makes is hard to argue that OneMax is the easiest function for the cGA. This, in particular, has the consequence that lower bounds for the runtime of the cGA on OneMax cannot be easily extended to other functions with a unique global optimum.

# 6.2 Imitating the OneMax Proof 

Above, we have seen that a simple, general argument why a lower bound for the runtime of the cGA on OneMax should extend to jump functions appears hard to find. For this reason, we now analyze the proof of the lower bound given in [64] and observe, fortunately, that its main arguments apply equally well to jump functions. Since the full proof in [64] is relatively long, namely more than twelve pages, we apologize to the reader that we cannot give a self-contained version of the proof, but that instead we only argue why the arguments given in [64] remain valid in our case.

We show the following result, which is independent from the jump size $k$. This result, in particular, shows that our upper bound of Theorem 13 is asymptotically tight. We note that this result is proven only for jump functions, but not also for superjump functions. This is due to the fact that the lower bound in [64] is only proven for OneMax and not for all functions with unique global optimum.

Theorem 26 Let $c>0$ be an arbitrary constant. Let $C$ be a constant that is sufficiently large compared to $c$. Let $\mu \geq C \log n$ and $\mu \leq n^{c}$. Then with probability $1-o(1)$, the runtime of the cGA with hypothetical population size $\mu$ on any n-dimensional jump function is at least $\Omega(\mu \sqrt{n}+n \log n)$.

Proof When $k$ is $\Omega(n)$, then Theorem 22 gives a lower bound of $\exp (\Omega(n))$ with high probability. For this reason, we can now conveniently assume that $k \leq \kappa n$ for an arbitrarily small constant $\kappa>0$.

As announced, we argue that the main arguments of the proof of the corresponding result in [64], Theorem 8, remain valid. The proof of this Theorem 8 mostly consists of Lemma 10 to 15 (in [64]). There is nothing to show for Lemma 10 as it refers only to iterations in which a fixed bit is performing a random-walk step (in which the fitness function is irrelevant). Lemma 11 is a statement on sums of independent random variables and does not refer to the cGA at all. In Lemma 12, a lower bound on the probability of a non-random-walk step is given. Informally speaking, a non-random-walk step for a particular bit means that in this iteration, the particular bit has an influence on how the two offspring are sorted before the frequency update. Since two search points have the same OneMax value if and only if they have the same objective value w.r.t. some jump function, this probability for a non-random-walk step is the same for OneMax and the jump function. Lemma 13, while formulated in the language of the cGA, is a statement on independent parallel unbiased random walks. The basic argument in the proof of Lemma 14 is that when $n^{k}$ frequencies have reached the lower boundary, then with high probability at least one of them will not move for $\Omega(n \log n)$ iterations, simply because the two offspring generated in each iteration always agree in this bit. The claim of Lemma 15 includes that $\Omega(n)$ frequencies stay in the interval $\left[\frac{1}{6}, \frac{2}{6}\right]$ for a given time frame $T$. To sample a search point in the gap, since $k$ is sufficiently small, at least a constant fraction of these bits have to be sampled as one. By a simple Chernoff bound (Theorem 4), this happens only with probability $\exp (-\Omega(n))$ in one iteration. Since Lemma 15 gives a statement with probability $1-\operatorname{poly}(n) 2^{-\Omega(\min \{p, n\})}$ only, the probabilities of sampling a search point in the gap do not affect the failure probability of

poly $(n) 2^{-\Omega(\min [\mu, n])}$. The main proof of Theorem 8 consists mostly of applications of these intermediate results. Only the last two paragraphs discuss what happens after the time frame $T$, which was analyzed in Lemma 15. These two paragraphs, however, again only use general properties of the cGA that are independent of the particular fitness function. ${ }^{4}$ In summary, all arguments given in the proof of Theorem 8 in [64] are equally valid for the optimization of a jump function with $k \leq \kappa n$ instead of the OneMax function. This proves our claim.

We note that the proof above (and thus our result) applies not only to jump functions, but to all functions where Theorem 22 can be employed and, more interestingly, to all functions that agree with OneMax on all search point $x$ with $\frac{n}{6} \leq\|x\|_{1} \leq \frac{3 n}{6}$. This restriction is necessary to use the arguments of [64]. Overcoming this restriction is most likely non-trivial. It would most likely immediately imply a general lower bound of $\Omega(n \log n)$ for the runtime of the cGA on any function with unique global optimum, which is a major open problem in the field.

# 7 Conclusion 

This study (including the preliminary versions [24, 25]) is, to the best of our knowledge, after [43] only the second mathematical analysis of an EDA on a multimodal optimization problem. Our two main results are
(i) that the cGA can optimize jump functions with logarithmic jump sizes in asymptotically the same efficiency as the simple OneMax function; it thus does not suffer from the fitness valleys present in these objective functions;
(ii) an $\exp (\Omega(k))$ lower bound for the runtime of the cGA on jump functions with jump size $k$, regardless of the hypothetical population size $\mu$. This result shows, in particular, that the corresponding upper bound by Hasenöhrl and Sutton [43] cannot be improved by running the cGA with a hypothetical population size that is sub-exponential in $k$.

The obvious question arising from this work is whether similar results hold for other EDAs and other optimization problems, or whether this result is a particularity of the cGA and jump functions. Natural candidates for other EDAs could be the UMDA, for which several rigorous runtime results exist, see [49], and the signifi-cance-based cGA [19], which might profit from using only the three frequencies $\frac{1}{n}$, $\frac{1}{2}$, and $1-\frac{1}{n}$. Candidates for optimization problems leading to a multimodal fitness landscape include the maximum matching problem [38, 39] or the minimum vertex cover problem $[47,58]$.

[^0]
[^0]:    ${ }^{4}$ To be very precise, the argument that a frequency at the lower boundary leaves this boundary only with probability $O\left(n^{-3 / 2}\right)$ in one iteration is not correct, but the authors of [64] convinced us that also with the correct estimate of $O\left(\frac{1}{n}\right)$ and setting the implicit constants right, at least $\sqrt{n}$ frequencies remain at the lower boundary at the end of the first $T$ iterations. This is enough to apply Lemma 14.

We also proved an $\Omega(n \log n)$ lower bound for jump functions in Sect. 6, and did so by arguing that this lower bound is witnessed in the OneMax process at a time up to which the cGA most likely has not sampled a search point that lies in the gap of a jump function. For this reason, the proof of [64] extends to jump functions as well. This argument was sufficient for our purposes, but left the real (and most likely very difficult) question untouched, namely if $\Omega(n \log n)$ is a lower bound for the cGA optimizing any function with unique global optimum. We do not dare to speculate what is the answer.

Acknowledgements Extended version of results that appeared at GECCO 2019 [25] and FOGA 2019 [24]. It contains as new result the $\Omega(\mu \sqrt{n}+n \log n)$ lower bound. All other results have been significantly rewritten, both to polish the arguments and to give a more unified treatment of the two previous works. In this process, the GECCO 2019 results were extended to subjump functions, the FOGA 2019 results were extended to superjump functions-two natural extensions of the jump functions class. This work was supported by a public grant as part of the Investissement d'avenir project, reference ANR-11-LABX-0056LMH, LabEx LMH, in a joint call with Gaspard Monge Program for optimization, operations research and their interactions with data sciences.

# References 

1. Afshani, P., Agrawal, M., Doerr, B., Doerr, C., Larsen, K.G., Mehlhorn, K.: The query complexity of a permutation-based variant of Mastermind. Discrete Appl. Math. 260, 28-50 (2019)
2. Auger, A., Doerr, B. (eds.): Theory of Randomized Search Heuristics. World Scientific Publishing, Singapore (2011)
3. Antipov, D., Doerr, B.: Precise runtime analysis for plateaus. In: Parallel Problem Solving From Nature, PPSN 2018, Part II, pp. 117-128. Springer, Berlin (2018)
4. Antipov, D., Doerr, B.: Runtime analysis of a heavy-tailed $(1+(\lambda, \lambda))$ genetic algorithm on jump functions. In: Parallel Problem Solving From Nature, PPSN 2020. Springer, Berlin (2020) (to appear)
5. Antipov, D., Doerr, B., Karavaev, V.: The $(1+(\lambda, \lambda))$ GA is even faster on multimodal problems. In: Genetic and Evolutionary Computation Conference, GECCO 2020, pp. 1259-1267. ACM (2020)
6. Antipov, D., Doerr, B., Yang, Q.: The efficiency threshold for the offspring population size of the $(\mu, \lambda)$ EA. In: Genetic and Evolutionary Computation Conference, GECCO 2019, pp. 1461-1469. ACM (2019)
7. Anil, G., Wiegand, R.P.: Black-box search by elimination of fitness functions. In: Foundations of Genetic Algorithms, FOGA 2009, pp. 67-78. ACM (2009)
8. Buzdalov, M., Doerr, B., Kever, M.: The unrestricted black-box complexity of jump functions. Evolut. Comput. 24, 719-744 (2016)
9. Corus, D., Oliveto, P.S., Yazdani, D.: On the runtime analysis of the Opt-IA artificial immune system. In: Genetic and Evolutionary Computation Conference, GECCO 2017, pp. 83-90. ACM (2017)
10. Corus, D., Oliveto, P.S., Yazdani, D.: Fast artificial immune systems. In: Parallel Problem Solving from Nature, PPSN 2018, Part II, pp. 67-78. Springer, Berlin (2018)
11. Doerr, B., Doerr, C., Ebel, F.: From black-box complexity to designing new genetic algorithms. Theor. Comput. Sci. 567, 87-104 (2015)
12. Dang, D.-C., Friedrich, T., Kötzing, T., Krejca, M.S., Lehre, P.K., Oliveto, P.S., Sudholt, D., Sutton, A.M.: Escaping local optima with diversity mechanisms and crossover. In: Genetic and Evolutionary Computation Conference, GECCO 2016, pp. 645-652. ACM (2016)
13. Dang, D.-C., Friedrich, T., Kötzing, T., Krejca, M.S., Lehre, P.K., Oliveto, P.S., Sudholt, D., Sutton, A.M.: Escaping local optima using crossover with emergent diversity. IEEE Trans. Evolut. Comput. 22, 484-497 (2018)
14. Doerr, B., Happ, E., Klein, C.: Tight analysis of the (1+1)-EA for the single source shortest path problem. Evolut. Comput. 19, 673-691 (2011)

15. Doerr, B., Johannsen, D.: Edge-based representation beats vertex-based representation in shortest path problems. In: Genetic and Evolutionary Computation Conference, GECCO 2010, pp. 759-766. ACM (2010)
16. Droste, S., Jansen, T., Wegener, I.: On the analysis of the (1+1) evolutionary algorithm. Theor. Comput. Sci. 276, 51-81 (2002)
17. Droste, S., Jansen, T., Wegener, I.: Upper and lower bounds for randomized search heuristics in black-box optimization. Theory Comput. Syst. 39, 525-544 (2006)
18. Doerr, B., Johannsen, D., Winzen, C.: Multiplicative drift analysis. Algorithmica 64, 673-697 (2012)
19. Doerr, B., Krejca, M.S.: Significance-based estimation-of-distribution algorithms. IEEE Trans. Evolut. Comput. (2020). https://doi.org/10.1109/TEVC.2019.2956633
20. Doerr, B., Krejca, M.S.: The univariate marginal distribution algorithm copes well with deception and epistasis. In: Evolutionary Computation in Combinatorial Optimization, EvoCOP 2020, pp. 51-66. Springer, Berlin (2020)
21. Doerr, B., Le, H.P., Makhmara, R., Nguyen, T.D.: Fast genetic algorithms. In: Genetic and Evolutionary Computation Conference, GECCO 2017, pp. 777-784. ACM (2017)
22. Doerr, B., Neumann, F. (eds.): Theory of Evolutionary Computation-Recent Developments in Discrete Optimization. Springer, Berlin (2020)
23. Doerr, B.: Analyzing randomized search heuristics via stochastic domination. Theor. Comput. Sci. 773, 115-137 (2019)
24. Doerr, B.: An exponential lower bound for the runtime of the compact genetic algorithm on jump functions. In: Foundations of Genetic Algorithms, FOGA 2019, pp. 25-33. ACM (2019)
25. Doerr, B.: A tight runtime analysis for the cGA on jump functions: EDAs can cross fitness valleys at no extra cost. In: Genetic and Evolutionary Computation Conference, GECCO 2019, pp. 14881496. ACM (2019)
26. Doerr, B.: Does comma selection help to cope with local optima? In: Genetic and Evolutionary Computation Conference, GECCO 2020, pp. 1304-1313. ACM (2020)
27. Doerr, B.: Lower bounds for non-elitist evolutionary algorithms via negative multiplicative drift. In: Parallel Problem Solving From Nature, PPSN 2020. Springer, Berlin (2020) (to appear)
28. Doerr, B.: Probabilistic tools for the analysis of randomized optimization heuristics. In: Doerr, B., Neumann, F. (eds.) Theory of Evolutionary Computation: Recent Developments in Discrete Optimization, pp. 1-87. Springer, Berlin (2020). arXiv:1801.06733
29. Droste, S.: A rigorous analysis of the compact genetic algorithm for linear functions. Nat. Comput. 5, 257-283 (2006)
30. Doerr, B., Winzen, C.: Ranking-based black-box complexity. Algorithmica 68, 571-609 (2014)
31. Doerr, B., Zheng, W.: A parameter-less compact genetic algorithm. In: Genetic and Evolutionary Computation Conference, GECCO 2020, pp. 805-813. ACM (2020)
32. Doerr, B., Zheng, W.: Sharp bounds for genetic drift in estimation-of-distribution algorithms. IEEE Trans. Evolut. Comput. (2020). https://doi.org/10.1109/TEVC.2020.2987361
33. Doerr, B., Zheng, W.: Working principles of binary differential evolution. Theor. Comput. Sci. 801, $110-142(2020)$
34. Friedrich, T., Kötzing, T., Krejca, M.S., Nallaperuma, S., Neumann, F., Schirneck, M.: Fast building block assembly by majority vote crossover. In: Genetic and Evolutionary Computation Conference, GECCO 2016, pp. 661-668. ACM (2016)
35. Friedrich, T., Kötzing, T., Krejca, M.S., Sutton, A.M.: The compact genetic algorithm is efficient under extreme Gaussian noise. IEEE Trans. Evolut. Comput. 21, 477-490 (2017)
36. Friedrich, T., Quinzan, F., Wagner, M.: Escaping large deceptive basins of attraction with heavytailed mutation operators. In: Genetic and Evolutionary Computation Conference, GECCO 2018, pp. 293-300. ACM (2018)
37. Fajardo, M.A.H., Sudholt, D.: On the choice of the parameter control mechanism in the $(1+(\lambda, \lambda))$ genetic algorithm. In: Genetic and Evolutionary Computation Conference, GECCO 2020, pp. 832840. ACM (2020)
38. Giel, O., Wegener, I.: Evolutionary algorithms and the maximum matching problem. In: Symposium on Theoretical Aspects of Computer Science, STACS 2003, pp. 415-426. Springer, Berlin (2003)
39. Giel, O., Wegener, I.: Searching randomly for maximum matchings. Electronic Colloquium on Computational Complexity (ECCC), (076) (2004)

40. Gießen, C., Witt, C.: The interplay of population size and mutation probability in the $(1+\lambda)$ EA on OneMax. Algorithmica 78, 587-609 (2017)
41. Harik, G.R., Lobo, F.G., Goldberg, D.E.: The compact genetic algorithm. IEEE Trans. Evolut. Comput. 3, 287-297 (1999)
42. Hoeffding, W.: Probability inequalities for sums of bounded random variables. J. Am. Stat. Assoc. 58, 13-30 (1963)
43. Hasenöhrl, V., Sutton, A.M.: On the runtime dynamics of the compact genetic algorithm on jump functions. In: Genetic and Evolutionary Computation Conference, GECCO 2018, pp. 967-974. ACM (2018)
44. He, J., Yao, X.: Drift analysis and average time complexity of evolutionary algorithms. Artif. Intell. 127, 51-81 (2001)
45. Jansen, T.: Analyzing Evolutionary Algorithms-The Computer Science Perspective. Springer, Berlin (2013)
46. Jansen, T., De Jong, K.A., Wegener, I.: On the choice of the offspring population size in evolutionary algorithms. Evolut. Comput. 13, 413-440 (2005)
47. Jansen, T., Oliveto, P.S., Zarges, C.: Approximating vertex cover using edge-based representations. In: Foundations of Genetic Algorithms, FOGA 2013, pp. 87-96. ACM (2013)
48. Jansen, T., Wegener, I.: The analysis of evolutionary algorithms-a proof that crossover really can help. Algorithmica 34, 47-66 (2002)
49. Krejca, M., Witt, C.: Theory of estimation-of-distribution algorithms. In: Doerr, B., Neumann, F. (eds.) Theory of Evolutionary Computation: Recent Developments in Discrete Optimization, pp. 405-442. Springer, Berlin (2020). arXiv:1806.05392
50. Krejca, M.S., Witt, C.: Lower bounds on the run time of the Univariate Marginal Distribution Algorithm on OneMax. Theor. Comput. Sci. 832, 143-165 (2020)
51. Lengler, J.: Drift analysis. In: Doerr, B., Neumann, F. (eds.) Theory of Evolutionary Computation: Recent Developments in Discrete Optimization, pp. 89-131. Springer, Berlin (2020). arXiv :1712.00964
52. Larrañaga, P., Lozano, J.A. (eds.): Estimation of Distribution Algorithms. Genetic Algorithms and Evolutionary Computation. Springer, Berlin (2002)
53. Lehre, P.K., Nguyen, P.T.H.: Improved runtime bounds for the univariate marginal distribution algorithm via anti-concentration. In: Genetic and Evolutionary Computation Conference, GECCO 2017, pp. 1383-1390. ACM (2017)
54. Lehre, P.K., Nguyen, P.T.H.: On the limitations of the univariate marginal distribution algorithm to deception and where bivariate EDAs might help. In: Foundations of Genetic Algorithms, FOGA 2019, pp. 154-168. ACM (2019)
55. Lengler, J., Sudholt, D., Witt, C.: Medium step sizes are harmful for the compact genetic algorithm. In: Genetic and Evolutionary Computation Conference, GECCO 2018, pp. 1499-1506. ACM (2018)
56. Lehre, P.K., Witt, C.: Black-box search by unbiased variation. Algorithmica 64, 623-642 (2012)
57. Neumann, F., Witt, C.: Bioinspired Computation in Combinatorial Optimization-Algorithms and Their Computational Complexity. Springer, Berlin (2010)
58. Oliveto, P.S., He, J., Yao, X.: Analysis of the (1+1)-EA for finding approximate solutions to vertex cover problems. IEEE Trans. Evolut. Comput. 13, 1006-1029 (2009)
59. Oliveto, P.S., Witt, C.: Erratum: Simplified drift analysis for proving lower bounds in evolutionary computation. CoRR arXiv:1211.7184 (2012)
60. Pelikan, M., Hauschild, M., Lobo, F.G.: Estimation of distribution algorithms. In: Kacprzyk, J., Pedrycz, W. (eds.) Springer Handbook of Computational Intelligence, pp. 899-928. Springer, Berlin (2015)
61. Rowe, J.E., Aishwaryaprajna.: The benefits and limitations of voting mechanisms in evolutionary optimisation. In: Foundations of Genetic Algorithms, FOGA 2019, pp. 34-42. ACM (2019)
62. Rajabi, A., Witt, C.: Self-adjusting evolutionary algorithms for multimodal optimization. In: Genetic and Evolutionary Computation Conference, GECCO 2020, pp. 1314-1322. ACM (2020)
63. Sudholt, D.: A new method for lower bounds on the running time of evolutionary algorithms. IEEE Trans. Evolut. Comput. 17, 418-435 (2013)
64. Sudholt, D., Witt, C.: On the choice of the update strength in estimation-of-distribution algorithms and ant colony optimization. Algorithmica 81, 1450-1489 (2019)
65. Wegener, I.: Simulated annealing beats Metropolis in combinatorial optimization. In: Automata, Languages and Programming, ICALP 2005, pp. 589-601. Springer, Berlin (2005)

66. Witt, C.: Tight bounds on the optimization time of a randomized search heuristic on linear functions. Comb. Probab. Comput. 22, 294-318 (2013)
67. Witt, C.: Domino convergence: why one should hill-climb on linear functions. In: Genetic and Evolutionary Computation Conference, GECCO 2018, pp. 1539-1546. ACM (2018)
68. Witt, C.: Upper bounds on the running time of the univariate marginal distribution algorithm on OneMax. Algorithmica 81, 632-667 (2019)
69. Whitley, D., Varadarajan, S., Hirsch, R., Mukhopadhyay, A.: Exploration and exploitation without mutation: solving the jump function in $\Theta(n)$ time. In: Parallel Problem Solving from Nature, PPSN 2018, Part II, pp. 55-66. Springer, Berlin (2018)

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

# Affiliations 

## Benjamin Doerr ${ }^{1}$

Benjamin Doerr
doerr@lix.polytechnique.fr
1 Laboratoire d'Informatique (LIX), CNRS, École Polytechnique, Institut Polytechnique de Paris, Palaiseau, France