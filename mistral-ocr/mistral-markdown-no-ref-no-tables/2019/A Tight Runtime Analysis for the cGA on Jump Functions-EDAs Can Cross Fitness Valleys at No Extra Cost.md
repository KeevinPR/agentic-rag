# A Tight Runtime Analysis for the cGA on Jump FunctionsEDAs Can Cross Fitness Valleys at No Extra Cost 

Benjamin Doerr<br>École Polytechnique, CNRS, Laboratoire d'Informatique (LIX)<br>Palaiseau, France


#### Abstract

We prove that the compact genetic algorithm (cGA) with hypothetical population size $\mu=\Omega(\sqrt{n} \log n) \cap \operatorname{poly}(n)$ with high probability finds the optimum of any $n$-dimensional jump function with jump size $k<\frac{1}{20} \ln n$ in $O(\mu \sqrt{n})$ iterations. Since it is known that the cGA with high probability needs at least $\Omega(\mu \sqrt{n}+n \log n)$ iterations to optimize the unimodal OneMax function, our result shows that the cGA in contrast to most classic evolutionary algorithms here is able to cross moderate-sized valleys of low fitness at no extra cost.

Our runtime guarantee improves over the recent upper bound $O\left(\mu n^{1.5} \log n\right)$ valid for $\mu=\Omega\left(n^{3.5+\varepsilon}\right)$ of Hasenöhrl and Sutton (GECCO 2018). For the best choice of the hypothetical population size, this result gives a runtime guarantee of $O\left(n^{5+\varepsilon}\right)$, whereas ours gives $O(n \log n)$.

We also provide a simple general method based on parallel runs that, under mild conditions, (i) overcomes the need to specify a suitable population size, but gives a performance close to the one stemming from the best-possible population size, and (ii) transforms EDAs with high-probability performance guarantees into EDAs with similar bounds on the expected runtime.


## CCS CONCEPTS

## - Theory of computation $\rightarrow$ Random search heuristics;

## KEYWORDS

Estimation-of-distribution algorithm; theory; runtime analysis

## ACM Reference Format:

Benjamin Doerr. 2019. A Tight Runtime Analysis for the cGA on Jump Functions- EDAs Can Cross Fitness Valleys at No Extra Cost. In Genetic and Evolutionary Computation Conference (GECCO '19), July 13-17, 2019, Prague, Czech Republic. ACM, New York, NY, USA, 9 pages. https://doi.org/ 10.1145/3321707.3321747

## 1 INTRODUCTION

While the mathematical analysis of evolutionary algorithms (EAs) has produced a plethora of insightful results in the last over 20 years, the rigorous understanding of estimation-of-distribution algorithms (EDAs) is much less developed [21]. Obviously, this is

[^0]due to the highly complex stochastic processes that describe the runs of such algorithms. In consequence, despite significant efforts and deep results [14, 23, 24], not even the runtime of the compact genetic algorithm (cGA) on the OneMax benchmark function is fully understood (here we would argue that the cGA is the most simple EDA and that the unimodal OneMax function, counting the number of ones in a bit string, is the most simple optimization problem with unique global optimum). It is therefore not surprising that many questions which are well-understood for EAs are only started being understood for EDAs. One such question is how EDAs optimize objective functions that are not unimodal.

In the first and so far only runtime analysis of an EDA on a nonunimodal objective function, Hasenöhrl and Sutton [17] regard the optimization time of the cGA on the jump function class, which are unimodal apart from having a valley of low fitness of scalable size $k$ around the global optimum. They show [17, Theorem 3.3] that, for a sufficiently large constant $C$ and any constant $\varepsilon>0$, the cGA with hypothetical population size at least $\mu \geq \max \left\{C n e^{4 k}, n^{3.5+\varepsilon}\right\}^{\frac{1}{2}}$ with probability $1-o(1)$ finds the optimum of any jump function with jump size at most $k=o(n)$ in $O\left(\mu n^{1.5} \log n+e^{4 k}\right)$ generations (which is also the number of fitness evaluations, since the cGA evaluates only two search points in each iteration).

This result is remarkable in that it shows that the cGA with the right choice of $\mu$ and for $k \geq 6$ is more efficient on jump functions than most evolutionary algorithms, who have a runtime of at least $\Omega\left(n^{k}\right)$, see Section 2.2.

There is one aspect in which the result of Hasenöhrl and Sutton is not yet perfect (and this is the motivation of this work). We note that even when choosing the smallest possible population size $\mu=n^{3.5+\varepsilon}$, the runtime guarantee becomes at least $\Omega\left(n^{5+\varepsilon}\right)$. While clearly a polynomial runtime, and thus efficient in the classic complexity theory view, this is a runtime that is not practical in many applications (and we recall here that the target of the mathematical analysis of evolutionary algorithms is not to understand jump functions, but to derive from the analysis on simple test problems insight that extend to practically relevant problems). Also, this runtime guarantee is weaker than the $O\left(n^{k}\right)$ bound for simple mutation-based EAs such as the $(1+1)$ EA when $k \leq 5$. Hence one could feel that the result of Hasenöhrl and Sutton shows the superiority of EDAs rather for problem instances for which both the runtime of typical EAs and the performance guarantee for the cGA are prohibitively large. In a similar vein, one has to question if a practitioner would run the cGA with a hypothetical population size of more than $n^{3.5}$ when solving a problem defined over bit strings of length $n$.

[^1]
[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
    GECCO '19, July 13-17, 2019, Prague, Czech Republic
    @ 2019 Copyright held by the owner/author(s). Publication rights licensed to the Association for Computing Machinery.
    ACM ISBN 978-1-4503-6111-8/19/07... $\$ 15.00$
    https://doi.org/10.1145/3321707.3321747

[^1]:    In the paper, this is stated as minimum of the two terms, but from the proofs it is clear that it should be the maximum.

Our main result is that these potential weaknesses of the cGA are not real and that the cGA performs in fact much better than what the previous work shows. We prove rigorously that the cGA with hypothetical population size $\mu \geq K \sqrt{n} \log n, K$ a sufficiently large constant, and $\mu$ polynomially bounded in $n$ with high probability optimizes any $n$-dimensional jump function with jump size $k<\frac{1}{20} \ln n$ in only $O(\mu \sqrt{n})$ iterations. For the smallest admissible populations size $\mu=\Theta(\sqrt{n} \log n)$, this gives a runtime guarantee of $O(n \log n)$, a result that both overcomes the large runtime and the large required hypothetical population size of the previous result.

From a broader perspective our result shows that the cGA (and we expect similar result to hold for other EDAs) does not suffer from moderate-size valleys of low fitness. We recall that Sudholt and Witt [24] have shown that the cGA with any hypothetical population size (polynomial in $n$ ) with high probability needs $\Omega(\mu \sqrt{n}+n \log n)$ iterations to optimize the OneMax function. Hence our result shows that adding a valley of low fitness to the OneMax function does not worsen the asymptotic performance of the cGA as long as the fitness valley is smaller than $\frac{1}{20} \ln n$.

We may add that our work also makes some arguments of [17] more rigorous. In particular, we observe that the progress of the cGA cannot be estimated by taking the progress one would have when no fitness valley was present and correcting this estimate by inverting the progress with the probability that a search point is sampled in the fitness valley. This argument ignores the stochastic dependencies between the absolute value of the progress and the event that a solution in the gap is sampled. These dependencies are real and have a negative impact as discussed in more detail before Lemma 6.

We note that the approach of intentionally ignoring some dependencies to make a mathematical analysis tractable, often called mean-field analysis, is common in some scientific areas, most notably statistical physics, and has also been used in evolutionary computation, e.g., [26]. This approach, however, needs an additional justification, e.g., via specific experiments, why the omission of the dependencies should not change the matter substantially. In any case, such mean-field approaches do not lead to results fully proven in the mathematical sense. In this sense, we hope that our work also provides methods that help in future analyses of EDAs on non-unimodal optimization problems.

As a side result, triggered by the fact that we "only" show a bound that holds with high probability, but not a bound on the expected runtime, we provide a general approach to transform an EDA using a population size parameter $\mu$ into an algorithm that does not require the specification of such a parameter, but has a performance similar to the one of the EDA with optimally chosen parameter. This performance guarantee also holds for the expected runtime, even if for the EDA only a with-high-probability runtime guarantee is known.

## 2 PRELIMINARIES

### 2.1 The Compact Genetic Algorithm

The compact genetic algorithm (cGA) is an estimation-of-distribution algorithm (EDA) proposed by Harik, Lobo, and Goldberg [16] for the maximization of pseudo-Boolean functions $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$. Being a univariate EDA, it develops a probabilistic model described
by a frequency vector $f \in[0,1]^{n}$. This frequency vector describes a probability distribution on the search space $\{0,1\}^{n}$. If $X=\left(X_{1}, \ldots, X_{n}\right) \in\{0,1\}^{n}$ is a search point sampled according to this distribution-we write

$$
X \sim \operatorname{Sample}(f)
$$

to indicate this-then we have $\operatorname{Pr}\left[X_{i}=1\right]=f_{i}$ independently for all $i \in[1 . . n]:=\{1, \ldots, n\}$. In other words, the probability that $X$ equals some fixed search point $y$ is

$$
\operatorname{Pr}[X=y]=\prod_{i: y_{i}=1} f_{i} \prod_{i: y_{i}=0}\left(1-f_{i}\right)
$$

In each iteration, the cGA updates this probabilistic model as follows. It samples two search points $x^{1}, x^{2} \sim \operatorname{Sample}(f)$, computes the fitness of both, and defines $\left(y^{1}, y^{2}\right)=\left(x^{1}, x^{2}\right)$ when $x^{1}$ is at least as fit as $x^{2}$ and $\left(y^{1}, y^{2}\right)=\left(x^{2}, x^{1}\right)$ otherwise. Consequently, $y^{1}$ is the rather better search point of the two. We then define a preliminary model by $f^{\prime}:=f+\frac{1}{\mu}\left(y^{1}-y^{2}\right)$. This definition ensures that, when $y^{1}$ and $y^{2}$ differ in some bit position $i$, the $i$-th preliminary frequency moves by a step of $\frac{1}{\mu}$ into the direction of $y_{i}^{\prime}$, which we hope to be the right direction since $y^{1}$ is the better of the two search points. The hypothetical populations size $\mu$ is used to control how strong this update is.

To avoid a premature convergence, we ensure that the new frequency vector is in $\left[\frac{1}{n}, 1-\frac{1}{n}\right]^{n}$ by capping too small or too large values at the corresponding boundaries. More precisely, for all $\ell \leq u$ and all $r \in \mathbb{R}$ we define

$$
\operatorname{minmax}(\ell, r, u):=\max \{\ell, \min \{r, u\}\}=\left\{\begin{array}{ll}
\ell & \text { if } r<\ell \\
r & \text { if } r \in[\ell, u] \\
u & \text { if } r>u
\end{array}\right.
$$

and we lift this notation to vectors by reading it component-wise. Now the new frequency vector is $\operatorname{minmax}\left(\frac{1}{n} \mathbf{1}_{n}, f^{\prime},\left(1-\frac{1}{n}\right) \mathbf{1}_{n}\right)$.

This iterative frequency development is pursued until some termination criterion is met. Since we aim at analyzing the time (number of iterations) it takes to sample the optimal solution (this is what we call the runtime of the cGA), we do not specify a termination criterion and pretend that the algorithm runs forever.

The pseudo-code for the cGA is given in Algorithm 1. We shall use the notation given there frequently in our proofs. For the frequency vector $f_{t}$ obtained at the end of iteration $t$, we denote its $i$-th component by $f_{i, t}$ or, when there is no risk of ambiguity, by $f_{i t}$.

Well-behaved frequency assumption: For the hypothetical population size $\mu$, we take the common assumption that any two frequencies that can occur in a run of the cGA differ by a multiple of $\frac{1}{\mu}$. We call this the well-behaved frequency assumption. This assumption was implicitly already made in [16] by using even $\mu$ in all experiments (note that the hypothetical population size is denoted by $n$ in [16]). This assumption was made explicit in [14] by requiring $\mu$ to be even. Both works do not use the frequencies boundaries $\frac{1}{n}$ and $1-\frac{1}{n}$, so an even value for $\mu$ ensures well-behaved frequencies.

For the case with frequency boundaries, the well-behaved frequency assumption is equivalent to $\left(1-\frac{2}{n}\right)$ being an even multiple of the update step size $\frac{1}{\mu}$. In this case, $n_{\mu}=\left(1-\frac{2}{n}\right) \mu \in 2 \mathbb{N}$ and the

Algorithm 1: The compact genetic algorithm (cGA) to maximize a function $\mathcal{F}:\{0,1\}^{n} \rightarrow \mathbb{R}$.
$t \leftarrow 0 ;$
$f_{t}=\left(\frac{1}{2}, \ldots, \frac{1}{2}\right) \in[0,1]^{n}$;
repeat
$x^{1} \leftarrow \operatorname{Sample}\left(f_{t}\right)$
$x^{2} \leftarrow \operatorname{Sample}\left(f_{t}\right)$
if $\mathcal{F}\left(x^{1}\right) \geq \mathcal{F}\left(x^{2}\right)$ then $\left(y^{1}, y^{2}\right) \leftarrow\left(x^{1}, x^{2}\right)$ else $\left(y^{1}, y^{2}\right) \leftarrow\left(x^{2}, x^{3}\right) ;$
$f_{t+1}^{t} \leftarrow f_{t}+\frac{1}{\rho}\left(y^{1}-y^{2}\right)$
$f_{t+1} \leftarrow \operatorname{minmax}\left(\frac{1}{n} 1_{n}, f_{t+1}^{t},\left(1-\frac{1}{n}\right) 1_{n}\right)$
$t \leftarrow t+1 ;$
until forever;
set of frequencies that can occur is

$$
F:=F_{\mu}:=\left\{\left.\frac{1}{n}+\frac{i}{\rho} \right\rvert\, i \in\left[0 . . n_{\mu}\right]\right\}
$$

This assumption was made, e.g., in the proof of Theorem 2 in [24] and in the paper [23] (see the paragraph following Lemma 2.1).

### 2.2 Related Work

In all results described in this section, we shall assume that the hypothetical population size is at most polynomial in the problem size $n$, that is, that there is a constant $c$ such that $\mu \leq n^{c}$.

The first to conduct a rigorous runtime analysis for the cGA was Droste in his seminal work [14]. He regarded the cGA without frequency boundaries, that is, he just took $f_{t+1}:=f_{t+1}^{t}$ in our notation. He showed that this algorithm with $\mu \geq n^{1 / 2+c}, c>0$ any positive constant, finds the optimum of the OneMax function defined by

$$
\operatorname{OneMax}(x)=\|x\|_{1}=\sum_{i=1}^{n} x_{i}
$$

for all $x \in\{0,1\}^{n}$ with probability at least $1 / 2$ in $O(\mu \sqrt{n})$ iterations [14, Theorem 8].

Droste also showed that this cGA for any objective function $\mathcal{F}$ with unique optimum has an expected runtime of $\Omega(\mu \sqrt{n})$ when conditioning on no premature convergence [14, Theorem 6]. It is easy to see that his proof of the lower bound can be extended to the cGA with frequency boundaries, that is, to Algorithm 1. For this, it suffices to deduce from his drift argument the result that the first time $T_{n / 4}$ that the frequency distance $D=\sum_{i=1}^{n}\left(1-f_{i t}\right)$ is less than $n / 4$ satisfies $E\left[T_{n / 4}\right] \geq \mu \sqrt{n} \frac{\sqrt{2}}{4}$. Since the probability to sample the optimum from a frequency distance of at least $n / 4$ is at most

$$
\begin{aligned}
\prod_{i=1}^{n} f_{i t} & =\prod_{i=1}^{n}\left(1-\left(1-f_{i t}\right)\right) \leq \prod_{i=1}^{n} \exp \left(-\left(1-f_{i t}\right)\right) \\
& =\exp \left(-\sum_{i=1}^{n}\left(1-f_{i t}\right)\right) \leq \exp (-n / 4)
\end{aligned}
$$

the algorithm with high probability does not find the optimum before time $T_{n / 4}$.

Ten years after Droste's work, Sudholt and Witt [24] showed that the $O(\mu \sqrt{n})$ upper bound also holds for the cGA with frequency boundaries. There (but the same should be true for the cGA without boundaries) a hypothetical population size of $\mu=\Omega(\sqrt{n} \log n)$ suffices (recall that Droste required $\mu=\Omega\left(n^{1 / 2+c}\right)$ ). The technically biggest progress with respect to upper bounds most likely lies in the fact that the analysis in [24] also holds for the expected optimization time, which means that it also includes the rare case that frequencies reach the lower boundary (see our discussion of the relation of expectations and tail bounds for runtimes of EDAs in Section 2.3). Sudholt and Witt also show that the cGA with frequency boundaries with high probability (and thus also in expectation) needs at least $\Omega(\mu \sqrt{n}+n \log n)$ iterations to optimize OneMax. While the $\mu \sqrt{n}$ lower bound could have been also obtained with methods similar to Droste's (in Lemma 5 we do something very similar), the innocentlooking $\Omega(n \log n)$ bound is surprisingly difficult to prove.

Not much is known for hypothetical population sizes below the order of $\sqrt{n}$. It is clear that then the frequencies will reach the lower boundary of the frequency range, so working with a non-trivial lower boundary like $\frac{1}{n}$ is necessary to prevent premature convergence. The recent lower bound $\Omega\left(\mu^{1 / 3} n\right)$ valid for $\mu=O\left(\frac{\sqrt{n}}{\log n \log \log n}\right)$ of [23] indicates that already a little below the $\sqrt{n}$ regime significantly larger runtimes occur, but with no upper bounds this regime remains largely not understood.

We refer the reader to the recent survey [21] for more results on the runtime of the cGA on classic unimodal test functions like LeAdinoOnes and BosVal. Interestingly, nothing was known for non-unimodal functions before the recent work of Hasenöhrl and Sutton [17] on jump functions, which we discussed already in the introduction.

To round off the picture, we briefly describe some typical runtimes of evolutionary algorithms on jump functions. We recall that the $n$-dimensional jump function with jump size $k \geq 1$ is defined by

$$
\operatorname{June}_{n k}(x)= \begin{cases}\|x\|_{1}+k & \text { if }\|x\|_{1} \in[0 . . n-k] \cup\{n\} \\ n-\|x\|_{1} & \text { if }\|x\|_{1} \in[n-k+1 . . n-1]\end{cases}
$$

Hence for $k=1$, we have a fitness landscape isomorphic to the one of OneMax, but for larger values of $k$ there is a fitness valley consisting of the $k-1$ highest sub-optimal fitness levels of the OneMax function. This valley is hard to cross for evolutionary algorithms using standard-bit mutation with mutation rate $\frac{1}{6}$ since with very high probability they need to generate the optimum from one of the local optima, which in a single application of the mutation operator happens only with probability less than $n^{-k}$. For this reason, e.g., the classic $(\mu+\lambda)$ and $(\mu, \lambda)$ EAs all have a runtime of at least $n^{k}$. This was proven formally for the $(1+1)$ EA in the classic paper [15], but the argument just given proves the $n^{k}$ lower bound equally well for all $(\mu+\lambda)$ and $(\mu, \lambda)$ EAs. By using larger mutation rates or a heavy-tailed mutation operator, a $k^{0(k)}$ runtime improvement can be obtained [13], but the runtime remains $\Omega\left(n^{k}\right)$ for $k$ constant.

Asymptotically better runtimes can be achieved when using crossover, though this is harder than expected. The first work in

this direction [20], among other results, could show that a simple $(\mu+1)$ genetic algorithm using uniform crossover with rate $p_{\mathrm{c}}=O(1 / k n)$ obtains an $O\left(\mu n^{2} k^{3}+2^{2 k} p_{\mathrm{c}}^{-1}\right)$ runtime when the population size is at least $\mu=\Omega(k \log n)$. A shortcoming of this result, already noted by the authors, is that it only applies to uncommonly small crossover rates. Using a different algorithm that first always applies crossover and then mutation, a runtime of $O\left(n^{k-1} \log n\right)$ was achieved by Dang et al. [6, Theorem 2]. For $k \geq 3$, the logarithmic factor in the runtime can be removed by using a higher mutation rate. With additional diversity mechanisms, the runtime can be further reduced up to $O\left(n \log n+4^{k}\right)$, see [5]. In the light of this last result, the insight stemming from the previous work [17] and ours is that the cGA apparently without further modifications supplies the necessary diversity to obtain a runtime of $O\left(n \log n+2^{O(k)}\right)$.

Finally, we note that runtimes of $O\left(n\left(\frac{n}{4}\right)\right)$ and $O\left(k \log (n)\left(\frac{n}{4}\right)\right)$ were shown for the $(1+1) \mathrm{IA}^{\text {hyp }}$ and the $(1+1)$ Fast-IA artificial immune systems, respectively $[3,4]$.

### 2.3 Expected Runtimes versus Guarantees with High Probability

We note that our main result as well as the previous one [17] for this problem give runtime bounds that hold with high probability, that is, with probability $1-o(1)$. However, we do not show a bound on the expected runtime. Let us quickly argue what the differences are, why we chose to prove a high-probability statement, and how to transform EDAs with high-probability guarantees into those with guarantees on the expected runtime. We note that Wegener [25, Section 3] with different arguments also suggests to prefer highprobability guarantees over expected runtimes.

For most evolutionary algorithms a high-probability guarantee can easily be turned into a bound on the expected runtime. If we know that a certain algorithm from any initial state finds the optimum in time $T$ with at least constant probability, then by splitting time into consecutive segments of length $T$ we see that after time $\gamma T$ the probability that the algorithm has not succeeded is at most $\exp (-\Omega(\gamma))$. Consequently, the runtime is stochastically dominated by $T$ times a geometric random variable with constant success rate, and consequently, the expected runtime is $O(T)$. The same argument gives a scalable tail bound of type "with probability at most $\exp (-\Omega(\gamma))$, the runtime is more than $\gamma T$."

For EDAs, it is usually much harder to show a good performance for any initial situation since there are some states which are particularly unfavorable (usually when all frequencies are close to the wrong boundary value). This does not rule out that the expected runtime and the time that is obtained with high probability are of the same order, but proving the bound on the expected runtime needs stronger arguments. The analysis of the expected runtime of the cGA on OneMax in [24] is an example for such a result.

This additional proof complexity raises the question if this effort is justified if the hardest part is dealing with states of the algorithm that are rarely reached (in [24] with probability $O\left(n^{-c}\right)$ only, where $c$ can be any positive constant). While we think that is was very valuable that the work [24] showed how to compute expected runtimes for EDAs, we feel that such results are not always needed, both because of the difficulty to obtain such results and because,
in some sense, they are a mildly unnatural remedy to the deeper problem.

As said, the main reason why guarantees for the expected runtime of an EDA can be difficult to show is that the EDA with small probability can reach a state from which the optimum is hard to reach. When in such a state, however, instead of spending much time to leave the unfavorable state, it would be more efficient and more natural to simply restart the algorithm and have a new good chance for a fast optimization process. While we cannot expect the algorithm to detect that it is in an unfavorable state (except in the case of premature convergence when no frequency boundaries are used), the following simple parallel-run strategy under mild assumptions can do this automatically. More precisely, via suitable parallel runs we obtain an expected runtime that is only a logarithmic factor above the runtime the EDA would have with high probability when using the optimal population size. Hence this approach both obtains expected runtimes and optimizes the value of the parameter $\mu$.

## Parallel EDA runs with exponentially growing population

size: Let $\mathcal{A}$ be an EDA with a parameter $\mu$ and let $\mathcal{P}$ be a problem we want to solve. We assume that there are unknown values $\hat{\mu}$ and $T$ such that $\mathcal{A}$ with any parameter value $\mu \geq \hat{\mu}$ solves $\mathcal{P}$ in time $\mu T$ with probability at least $\frac{4}{4}$.

We propose the following strategy to solve $\mathcal{P}$ via parallel runs of $\mathcal{A}$ with different parameter values. We start with no process running. In round $i=1,2, \ldots$ of our strategy, we let all running processes (which are process 1 to $i-1$ ) use a computational budget of $2^{i-1}$; further, we start process $i$ with parameter $\mu=\mu_{i}:=2^{i-1}$ and let it use a budget of $\sum_{j=0}^{i-1} 2^{j}$. We stop when any process has solved the problem.

We observe that at the end of round $i$, processes 1 to $i$ are running and have each spent a budget of $\sum_{j=0}^{i-1} 2^{j}$. Consequently, the total budget spent in the first $i$ rounds is less than $i 2^{i}$.

Note that after round $i_{0}=1+\left\lceil\log _{2} \hat{\mu}\right\rceil+\left\lfloor\log _{2} T\right\rfloor$, the process with parameter $\mu=2^{\left\lceil\log _{2} \hat{\mu}\right\rceil} \geq \hat{\mu}$ has started and has used a time budget of

$$
\sum_{j=0}^{i_{0}-1} 2^{j} \geq \sum_{j=\left\lceil\log _{2} \hat{\mu}\right\rceil}^{i_{0}-1} 2^{j}=\mu \sum_{j=0}^{\left\lfloor\log _{2} T\right\rfloor} 2^{j} \geq \mu T
$$

Consequently, with probability $3 / 4$ this process has found the optimum at that time. With the same type of computation, we see that in round $i_{0}+j$, the process with parameter $2^{j} \mu$ is finished with probability $3 / 4$. Consequently, the round in which we found the solution is dominated by $i_{0}-1$ plus a geometric distribution with success rate $3 / 4$. The expected time taken by this strategy to solve the problem thus is at most

$$
\sum_{j=i_{0}}^{\infty}\left(\frac{1}{4}\right)^{i-i_{0}}\left(\frac{3}{4}\right) i 2^{i}=\frac{3}{4} 2^{i_{0}} \sum_{j=0}^{\infty} 2^{-j}\left(j+i_{0}\right)=3 \cdot 2^{i_{0}-1}\left(i_{0}+1\right)
$$

using the well-known result $\sum_{j=0}^{\infty} j 2^{-j}=2$. We further estimate the expected runtime of our parallel-run strategy by
$3 \cdot 2^{i_{0}-1}\left(i_{0}+1\right) \leq 3 \mu T\left(\log _{2}(\mu T)+2\right) \leq 6 \hat{\mu} T\left(\log _{2}(\hat{\mu} T)+3\right) \asymp T_{\mathrm{par}}$.

We note that, again, analogous arguments give the scalable tail bound that with probability at most $\exp (-\Omega(\gamma))$, the runtime exceeds $\gamma T_{\text {par. }}$. We recall here that for EDAs such tail bounds are usually not shown, again due to the fact that the EDA may reach a situation from which is takes a long time to reach the optimum.

We note that if the values of $\tilde{\mu}$ and $T$ were known in advance, then restarting the EDA with $\mu=\tilde{\mu}$ and with a budget of $T$ until the problem is solved would immediately give an algorithm with expected runtime $T^{*} \leq \frac{4}{3} \tilde{\mu} T$. This is the best-possible expected runtime that can be deduced from our assumptions. Consequently, our parallel-run strategy with its $O\left(T^{*} \log T^{*}\right)$ expected runtime obtains the optimal expected runtime apart from a logarithmic factor.

We remark that a logarithmic factor usually is not a lot compared to what can be lost by choosing a wrong algorithm parameter, in particular, when the parameter is hard to guess. We note here that the recent work [23] suggests that already for the simple OneMax function, the hypothetical population size has a non-obvious influence on the runtime: Sufficiently small values give an $O(n \log n)$ runtime, in a middle regime the runtime increases to $\Omega\left(n^{7 / 6}\right)$ before dropping again to $O(n \log n)$ and then increasing linearly with $\mu$. In the light of such results, a logarithmic overhead for exploiting a near-optimal rate appears to be a good trade-off.

## 3 MAIN TECHNICAL ANALYSIS

We now conduct our runtime analysis of the cGA on jump functions. We start by giving a rough overview of the proof, then provide the necessary ingredients of the main proof, and finally state and prove our main result.

### 3.1 Proof Overview

We now give a brief overview of our runtime analysis and show how the different partial results work together. We leave it to the reader to read this section now or after the presentation of the partial results (or twice).

In our analysis, we roughly distinguish three phases of the optimization process. The first phase lasts until for the first time the frequency distance $D_{t}:=n-\left\|f_{t}\right\|_{1}$ is $O(\log n)$ with a large implicit constant. During this phase, by Lemma 1 and a union bound, with high probability we will never sample a solution in the gap. Consequently, we can pretend that we are optimizing the OneMax function and use our analysis of Lemma 5, which reuses arguments of the classic result by Droste [14] including Lemma 4. The second phase then lasts until we have a $D_{t}$ value of $O(k)$, again with large implicit constant. In this phase, we use the drift computed in Lemma 6. We profit from the fact that in this phase we only need to obtain a moderate decrease of $D_{t}$ and apply the additive drift theorem with the smallest drift that can occur in this phase, which is $\Omega(1 / \mu)$. Since this phase is so short, a simple Markov bound suffices to show that the phase ends with high probability in due time. Once we reach a $D_{t}$ value of $O(k)$, we have a reasonable chance to sample the optimum by Lemma 7. Since in this phase samples in the gap occur frequently, we have less control over $D_{t}$, in particular, we cannot exhibit an expected decrease of $D_{t}$. We therefore pessimistically estimate $D_{t}$ as if $D_{t}$ would always increase, which gives (apart from the boundary effects described in Lemma 2) an
increase of $\left\|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right\}$. Since $D_{t}$ is small, these increases are small as well, as again ensured by Lemma 1. With this observation, we can argue that we have a $D_{t}$ value of $O(k)$ for almost $\mu$ iterations, which suffices to sample the optimum with high probability.

All the arguments above need that the frequencies are bounded away from the lower boundary of $\frac{1}{6}$, more precisely, that they are $\Omega(1)$ at all times. In the first two phases, we ensure this via Lemma 3, our general result for random processes that are not Markov processes. To this aim, we estimate the probabilities of certain frequency changes by adjusting this data from the OneMax process (Lemma 8, taken from Sudholt and Witt [24]) via a pessimistic estimate of the negative influence of search points sampled in the gap. For the third phase, the fact that this phase only last $o(\mu)$ iterations implies that frequencies change by at most $o(1)$, hence the $\Omega(1)$ lower bound remains intact.

### 3.2 Technical Ingredients of the Main Proof

In this section, we collect the central arguments needed in the proof of our main result. Since we hope that some arguments are helpful for other runtime analyses of EDAs, we fix no general notation apart from the one defined in Algorithm 1 (at the price of occasionally restating a notion).

We frequently use the following estimate, which states that the OneMax fitness of a search point sampled from $\operatorname{Sample}(f)$ is close to the expected OneMax fitness $\|f\|_{1}$. Since we mostly need such results for frequency vectors close to $(1, \ldots, 1)$, we formulate this result in terms of distances to the maximum values. For reasons of space, the proof of this elementary result is omitted, but can be found in [10].

Lemma 1. Let $f \in[0,1]^{n}, D:=n-\|f\|_{1}, D^{-} \leq D \leq D^{+}$, $x \sim \operatorname{Sample}(f)$, and $d(x):=n-\|x\|_{1}$. Then for all $\delta \in[0,1]$, we have

$$
\begin{aligned}
& \operatorname{Pr}\left[d(x) \geq(1+\delta) D^{+}\right] \leq \exp \left(-\frac{1}{2} \delta^{2} D^{+}\right) \\
& \operatorname{Pr}\left[d(x) \leq(1-\delta) D^{-}\right] \leq \exp \left(-\frac{1}{2} \delta^{2} D^{-}\right)
\end{aligned}
$$

We need the lemma above in particular to argue that the probability to sample a search point in the gap region of the June function is small. For the June ${ }_{8 k}$ function, we observe that when $D:=n-\|f\|_{1}$ is at least $2 k$, then the probability that $x \sim \operatorname{Sample}(f)$ lies in the gap, that is, has $n-k<\|x\|_{1}<n$, is $e^{-\Omega(k)}$. We can also get low constant probabilities for sampling in the gap when $D \geq k+\Omega(\sqrt{k})$ with large implicit constant. In [17, Lemma 3.2], a gap probability of at most $1-1 / \sqrt{2} \leq 0.293$ is shown when $D \geq k+c$ for $c$ a sufficiently large constant and $k=o(n)$, but we are skeptical that this is true. Note that when $f=\frac{k-c}{n} \mathbf{1}_{n}$, then $X=n-\|x\|_{1}$ with $x \sim \operatorname{Sample}(f)$ follows a binomial distribution with parameters $n$ and $\frac{k+c}{n}$. Hence if $k$ is large compared to $c$, then $\operatorname{Pr}[X<k]=\operatorname{Pr}[X<E[X]-c] \approx \frac{1}{2}$.

When, in the notation of Algorithm 1, the current frequency vector $f_{t}$ is such that $f_{t t} \in\left\{\frac{1}{n}, 1-\frac{1}{n}\right\}$ for some $i \in[1 . . n]$, then it may happen that $f_{t+1}^{*} \notin\left[\frac{1}{n}, 1-\frac{1}{n}\right]$ and consequently $f_{t+1}$ does not satisfy the nice relation $f_{t+1}=f_{t}+\frac{1}{\mu}\left(y^{1}-y^{2}\right)$. The following lemma quantifies these discrepancies by showing that they are stochastically dominated (see, e.g., [7]) by $\frac{1}{\mu}$ times a binomial distributions with expectation 2. The proof is again omitted for reasons of space, but can be found in [10].

Lemma 2. Let $P=2 \frac{1}{n}\left(1-\frac{1}{n}\right)$. Let $t \geq 0$. Using the notation given in Algorithm 1, consider iteration $t+1$ of a run of the cGA started with a fixed frequency vector $f_{t} \in\left[\frac{1}{n}, 1-\frac{1}{n}\right]^{n}$.
(i) Let $L:=\left\{i \in[1 . . n] \mid f_{t t}=\frac{1}{n}\right\}, \ell=|L|$, and $M:=\left\{i \in L \mid\right.$ $\left.x_{i}^{1} \neq x_{i}^{2}\right\}$. Then $|M| \sim \operatorname{Bin}(\ell, P)$ and $\left\|f_{t+1}\right\|_{1}-\left\|f_{t+1}^{\prime}\right\|_{1} \leq$ $\left\|\left(f_{t+1}\right)_{|L}\right\|_{1}-\left\|\left(f_{t+1}^{\prime}\right)_{|L}\right\|_{1} \leq \frac{1}{\rho}|M| \leq \frac{1}{\rho} \operatorname{Bin}\left(n, \frac{2}{n}\right)$.
(ii) Let $L:=\left\{i \in[1 . . n] \mid f_{t t}=1-\frac{1}{n}\right\}, \ell=|L|$, and $M:=\left\{i \in\right.$ $\left.L \mid x_{i}^{1} \neq x_{i}^{2}\right\}$. Then $|M| \sim \operatorname{Bin}(\ell, P)$ and $\left\|f_{t+1}^{\prime}\right\|_{1}-\left\|f_{t+1}\right\|_{1} \leq$ $\left\|\left(f_{t+1}^{\prime}\right)_{|L}\right\|_{1}-\left\|\left(f_{t+1}\right)_{|L}\right\|_{1} \leq \frac{1}{\rho}|M| \leq \frac{1}{\rho} \operatorname{Bin}\left(n, \frac{2}{n}\right)$.

Since sampling the optimum is particularly unlikely when frequencies are close to the lower boundary, we shall argue that the frequencies in a run of the cGA on OneMax stay away from the lower boundary for a decent time.

A similar result was given in [17, Lemma 2.4], however, the proof appears to be not complete. It seems to us that the main technical prerequisite of this result, Lemma 2.2 in [17] with a proof of a little over one page in the condensed proceedings style, is not correct for two reasons. Since the proof of Lemma 2.2 never refers to the frequency boundaries, it is not clear if it is applicable for the cGA with these boundaries. Rather, a frequency vector having one entry $f_{t t}=\frac{1}{n}$ and another one $f_{j t}=1-\frac{1}{n}$ seems to be a counterexample (note that the frequency vector is called $p_{t}$ instead of $f_{t}$ in [17]). However, also for the case without boundaries counterexamples seem to exist for all value of $\mu$, e.g., the frequency vector $f_{t}=\left(\frac{1}{100}, \frac{1}{2}\right)$.

We did not see how to repair the otherwise elegant argument via the Azuma-Hoeffding inequality. For this reason, using a sequence of elementary reductions, we argue that the true random process of a frequency, which is not a Markov process when regarding one frequency in isolation, can be pessimistically replaced by a fair random walk on an unbounded frequency domain. For the analysis of the latter, classic Chernoff bounds can be used. This general approach was also taken in [14], however in the easier situation that there are no frequency boundaries and that the objective function is OneMax.

Lemma 3. Let $\mu$ be arbitrary except that it satisfies the wellbehaved frequency assumption. Let $\varepsilon>0$. Let $Z_{0}, Z_{1}, \ldots$ be any random process on $F_{\mu}$ such that (i) $Z_{0}=\frac{1}{2}$, (ii) for all $t=0,1, \ldots$ there are numbers $p_{t}, q_{t}, r_{t} \in[0,1]$, depending on $Z_{0}, Z_{1}, \ldots, Z_{t}$, such that $p_{t}+q_{t}+r_{t}=1$ and, conditional on $Z_{0}, \ldots, Z_{t}$,

$$
\begin{gathered}
\operatorname{Pr}\left[Z_{t+1}=Z_{t}\right]=p_{t} \\
\operatorname{Pr}\left[Z_{t+1}=Z_{t}+\frac{1}{\mu}\right]=q_{t} \\
\operatorname{Pr}\left[Z_{t+1}=Z_{t}-\frac{1}{\mu}\right]=r_{t}
\end{gathered}
$$

We further assume that $r_{t}=0$ when $Z_{t}=\frac{1}{n}$, that $q_{t}=0$ if $Z_{t}=1-\frac{1}{n}$, and that $q_{t} \geq r_{t}$ when $Z_{t} \neq 1-\frac{1}{n}$. Then for all $T \in \mathbb{N}$,

$$
\operatorname{Pr}\left[\exists t \in\left[0 . . T\right]: Z_{t}<\frac{1}{2}-\varepsilon\right] \leq 2 \exp \left(-\frac{2 \mu^{2} \varepsilon^{2}}{T}\right)
$$

Proof. We first observe that we can assume $p_{t}=0$ for all $t$. The event $Z_{t+1}=Z_{t}$ that the process does not move only slows down the process in the sense that it visits fewer states. Similarly, we can assume that $q_{t}=r_{t}$ except in the cases $Z_{t} \in\left(\frac{1}{n}, 1-\frac{1}{n}\right)$. For this
now uniquely defined process, which is an unbiased random walk with reflecting boundaries, we show

$$
\operatorname{Pr}\left[\exists t \in\left[0 . . T\right]: Z_{t} \notin\left[\frac{1}{2}-\varepsilon, \frac{1}{2}+\varepsilon\right]\right] \leq 2 \exp \left(-\frac{2 \mu^{2} \varepsilon^{2}}{T}\right)
$$

Being interested in the event that the process reaches a state outside $\left[\frac{1}{2}-\varepsilon, \frac{1}{2}+\varepsilon\right]$ at least once, we can also drop the boundary conditions and assume that we have $Z_{t+1} \in\left\{Z_{t}-\frac{1}{\mu}, Z_{t}+\frac{1}{\mu}\right\}$ uniformly at random at all times $t$. We can now rewrite the $Z_{t}$ as follows. Let $X_{1}, \ldots, X_{T}$ be independent random variables uniformly distributed on $\left(-\frac{1}{\mu}, \frac{1}{\mu}\right)$. Then for all $t, Z_{t}$ has the same distribution as $\frac{1}{2}+\sum_{t=1}^{T} X_{t}$. Consequently, by the additive Chernoff bound (in the sharper version working also for maxima, see (2.17) and Theorem 2 in [19] or, e.g., Theorem 10.31 together with Theorem 10.9 in [8]), we have

$$
\begin{aligned}
\operatorname{Pr}\left[\exists t \in\left[0 . . T\right]: Z_{t} \notin\left[\frac{1}{2}-\varepsilon, \frac{1}{2}+\varepsilon\right]\right] \\
& =\operatorname{Pr}\left[\exists t \in\left[0 . . T\right]: \mid Z_{t}-E\left[Z_{t}\right] \mid>\varepsilon\right] \\
& \leq 2 \exp \left(-\frac{2 \varepsilon^{2}}{T(1 / \mu)^{2}}\right)=2 \exp \left(-\frac{2 \mu^{2} \varepsilon^{2}}{T}\right)
\end{aligned}
$$

The following result is a weaker form of what was shown in the proof of Lemma 5 in [14].

Lemma 4. There is a constant $C>0$ such that the following holds. Let $n \in \mathbb{N}$ and $D \in \mathbb{N}$. Let $f \in\left[\frac{1}{3}, 1\right]^{n}$ such that $\|f\|_{1} \leq n-D$. Let $x^{1}, x^{2} \sim \operatorname{Sample}(f)$ independently. Then

$$
\operatorname{Pr}\left\{\left\|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right\| \geq \frac{1}{5} \sqrt{D}\right\} \geq C
$$

Since we shall use that the optimization process of the cGA on a jump function is identical to the one on the OneMax function as long as no search point in the gap region is sampled, we find the following analysis of the optimization process on OneMax useful. It differs from Droste's analysis of the cGA on OneMax [14] in that it regards the cGA with boundaries and in that it proves a high-probability statement for reaching a near-optimal frequency vector. We note that our analysis can easily be extended to also give a bound for the time to sample an optimal solution, but we do not need such a result (and in fact, such a result is implied by our main result). Also, a simplified version of our proof would apply to the cGA without boundaries.

Lemma 5. Consider a run of the cGA with $\mu \geq \log _{2} n$ on the OneMax benchmark function. Let $D_{t}:=n-\left\|f_{t}\right\|_{1}$ for all $t$. Let $K$ be a sufficiently large constant. Let $T$ be the first time that $D_{t} \leq K$ or that there is an $i \in[1 . . n]$ with $f_{t t}<\frac{1}{3}$. Then

$$
\operatorname{Pr}\left\{T \geq \frac{10(2+\sqrt{2})}{C} \mu \sqrt{n}\right\}=\exp (-\Omega(\mu))
$$

where $C$ is the constant from Lemma 4.
For reasons of space, the formal proof of this lemma is omitted in this extended abstract. It can be found in the preprint [10].

We now analyze the drift in $D_{t}$ when we are that close to the gap that we cannot assume anymore that we never sample a search point in the gap. To be precise, let us define the gap by $G:=G_{n k}:=$ $\left\{x \in\{0,1\}^{n} \mid n-k<\|x\|_{1}<n\right\}$. Let $G^{+}:=G \cup\{(1, \ldots, 1)\}$.

A difficulty here, which was not treated fully rigorously in [17, Lemma 3.1], is that the event $G_{t}$ that $x^{1}$ or $x^{2}$ lie in the gap and the random variable $\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|$ are not independent. Consequently, the estimate $E\left[D_{t}-D_{t+1} \mid D_{t}\right]=\frac{1}{\rho}\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|(1-2 \operatorname{Pr}\left[G_{t}\right])$ is not correct. In fact, the correlation is indeed not in our favor. When $\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|$ is large, the probability that a search point in the gap was sampled (and thus the frequency update is done in the unwanted direction) is higher.

Lemma 6. Let $\mu$ be arbitrary satisfying the well-behaved frequency assumption. Let $k \in\left[1, \frac{1}{2} n-1\right]$. Consider an iteration $t$ of the cGA optimizing $\operatorname{JUMP}_{n k}$ started with a frequency vector $f_{t}$ such that $D_{t}=$ $n-\left\|f_{t}\right\|_{1} \geq 2 k$ and such that $f_{t t} \geq \frac{1}{3}$ for all $i \in[1 . . n]$. Then

$$
E\left[\mu D_{t}-\mu D_{t+1}\right] \geq \frac{1}{5} C \sqrt{D_{t}}-6 D_{t} \exp \left(-\frac{1}{8} D_{t}\right)-2
$$

where $C$ is the constant from Lemma 4.
Proof. From the definition of the cGA, we note that when $x^{1}$ and $x^{2}$ are both not in $G^{+}$, then $D_{t+1}^{\prime}:=n-\left\|f_{t+1}^{\prime}\right\|_{1}$ satisfies $D_{t+1}^{\prime}=D_{t}-\frac{1}{\rho}\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|$. In all other cases, we have $D_{t+1}^{\prime} \leq$ $D_{t}+\frac{1}{\rho}\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|$. Consequently,

$$
\begin{aligned}
& E\left[\mu D_{t}-\mu D_{t+1}^{\prime}\right] \\
& \geq \operatorname{Pr}\left[x^{1}, x^{2} \notin G^{+}\right] E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \mid x^{1}, x^{2} \notin G^{+}\right] \\
& \quad-\operatorname{Pr}\left[\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right] E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \mid\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right] \\
& =E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|\right] \\
& \quad-2 \operatorname{Pr}\left[\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right] E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right| \mid\left\{x^{1}, x^{2}\right\} \cap G^{+} \neq \emptyset\right]
\end{aligned}
$$

When the frequencies are all at least $\frac{1}{3}$, we conclude from Lemma 4 that $E\left[\left|\left\|x^{1}\right\|_{1}-\left\|x^{2}\right\|_{1}\right|\right] \geq \frac{1}{5} C \sqrt{D_{t}}$.

For the contribution when search points are in $G^{+}$, we first note that the second bound of Lemma 1 (with $\delta=\frac{1}{5}$ and $D^{-}=D_{t}$ ) and $D_{t} \geq 2 k$ yield

$$
\operatorname{Pr}\left[x^{1} \in G^{+}\right] \leq \operatorname{Pr}\left[d\left(x^{1}\right) \leq \frac{1}{2} D_{t}\right] \leq \exp \left(-\frac{1}{8} D_{t}\right)
$$

Then, exploiting the symmetry between $x^{1}$ and $x^{2}$, counting the case $x^{1}, x^{2} \in G^{+}$twice, and using again $\frac{1}{2} D_{t} \geq k$, we compute

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

By Lemma 2, we further have $E\left[\mu D_{t+1}-\mu D_{t+1}^{\prime}\right] \leq 2$. Consequently, recalling that the linearity of expectation holds also for dependent random variables, we have $E\left[\mu D_{t}-\mu D_{t+1}\right]=E\left[\mu D_{t}-\right.$ $\left.\mu D_{t+1}^{\prime}\right]-E\left[\mu D_{t+1}-\mu D_{t+1}^{\prime}\right] \geq \frac{1}{5} C \sqrt{D_{t}}-6 D_{t} \exp \left(-\frac{1}{8} D_{t}\right)-2$.

The following elementary estimate gives a lower bound for the probability to sample the optimum. For reasons of space, its proof can only be found in the preprint [10].

Lemma 7. Let $0<c<1$ and $f \in[c, 1]^{n}$. Let $x \sim \operatorname{Sample}(f)$. Then $\operatorname{Pr}[x=(1, \ldots, 1)] \geq c^{(n-\left\|f\right\|_{1}) /(1-c)}$.

We shall use the following estimate on the expected change of a frequency that is not affected by the boundaries. This result was proven in [24, Lemma 3].

Lemma 8. Let $\mu$ be arbitrary. Consider a run of the cGA optimizing OneMax. Consider an iteration starting with a frequency vector $f_{t}$. Let $i \in[1 . . n]$ be such that $\frac{1}{n}+\frac{1}{\mu} \leq f_{t t} \leq\left(1-\frac{1}{n}\right)-\frac{1}{\mu}$. Then

$$
E\left[f_{i, t+1}-f_{t t}\right] \geq \frac{2}{11} \frac{f_{i t}\left(1-f_{t t}\right)}{\mu}\left(\sum_{j \neq i} f_{j t}\left(1-f_{j t}\right)\right)^{-1 / 2}
$$

### 3.3 Main Result and Proof

We are now ready to state and prove our main result.
Theorem 9. Let $k \leq \frac{1}{20} \ln (n)-1$. Let $\mu \geq K \sqrt{n} \ln (n)$ for a sufficiently large constant $K$, but polynomially bounded in $n$. Then the cGA with frequency boundaries (Algorithm 1) with hypothetical population size $\mu$ with probability $1-o(1)$ finds the optimum of the Jump ${ }_{n k}$ function in time $O(n \log n)$.

Proof. To allow the reader to easily check that all implicit constants can be chosen in a way that they give the claimed results, we make these constants explicit in the following proof, but note that for most of them it just suffices to choose them sufficiently large.

Let $k \leq C_{k} \ln (n)-1, C_{k}=\frac{10}{20}$. Let $\mu \geq c_{\mu} \sqrt{n} \ln (n)$ and $\mu \leq n^{C_{\mu}}$ for a constant $c_{\mu}$ to be defined in a moment and, say, $C_{\mu} \geq 1$. Consider a run of the cGA on the objective function $\operatorname{Jump}_{n k}$.

Let $\tilde{T}^{\prime}$ be the first time that $D_{t}:=n-\left\|f_{t}\right\|_{1}$ satisfies $D_{t} \leq D^{\prime}:=$ $C_{D^{\prime}} \ln n$, where $C_{D^{\prime}} \geq 8 C_{\mu}+12$ is a constant. Let $\tilde{T}^{\prime \prime}$ be the first time that $D_{t} \leq D^{\prime \prime}:=\max \left\{2 k+1, C_{D^{\prime \prime}}\right\}$, where $C_{D^{\prime \prime}}$ is a sufficiently large constant (independent also of all other constants).

Let $T^{\prime}=\min \left\{\tilde{T}^{\prime},\left\lfloor C_{T^{\prime}} \mu \sqrt{n}\right\rfloor\right\}$ with $C_{T^{\prime}}=\frac{10(2 \times \sqrt{2})}{k}$, where $C$ is the constant from Lemma 4. Let $T^{\prime \prime}=\min \left\{\tilde{T}^{\prime \prime},\left\lfloor C_{T^{\prime \prime}} \mu \sqrt{n}\right\rfloor\right\}$ with $C_{T^{\prime \prime}}=C_{T^{\prime}}+1$. Let now $c_{\mu} \geq 36 C_{T^{\prime \prime}}$.

We first argue that with high probability we have no frequencies below $\frac{1}{3}$ up to time $T^{\prime \prime}$. For this, consider some time $t$ such that $f_{t} \in\left[\frac{1}{3}, 1\right]^{n}$ and $D_{t} \geq D^{\prime \prime}$. Consider a fixed bit $i \in[1 . . n]$ such that $f_{i t} \neq 1-\frac{1}{n}$. If we were optimizing the OneMax function, then by Lemma 8,

$$
\begin{aligned}
& \operatorname{Pr}\left[f_{i, t+1}=f_{i t}+\frac{1}{\mu}\right]-\operatorname{Pr}\left[f_{i, t+1}=f_{i t}-\frac{1}{\mu}\right] \\
& \quad=\mu E\left[f_{i, t+1}-f_{i t}\right] \\
& \quad \geq \frac{2}{11} f_{i t}\left(1-f_{i t}\right)\left(\sum_{j \neq i} f_{j t}\left(1-f_{j t}\right)\right)^{-1 / 2} \\
& \quad \geq \frac{2}{11} f_{i t}\left(1-f_{i t}\right)\left(D_{t}\right)^{-1 / 2}
\end{aligned}
$$

Regardless of whether we optimize OneMax or Jump ${ }_{n k}$, the events $f_{i, t+1}=f_{i t}+\frac{1}{\mu}$ and $f_{i, t+1}=f_{i t}-\frac{1}{\mu}$ can only occur when the two search points sampled in this iteration satisfy $x_{i}^{1} \neq x_{i}^{2}$. Further, the definition of $f_{i, t+1}$ differs from the OneMax case at most when at least one of $x^{1}$ and $x^{2}$ lie in the gap $G_{n k}$. Hence the following coarse correction of the above estimate is valid for the

optimization of $\mathrm{J} \mathrm{u} \mathrm{\alpha p}_{n k}$ -

$$
\begin{aligned}
& \operatorname{Pr}\left[f_{i, t+1}=f_{i t}+\frac{1}{\mu}\right]-\operatorname{Pr}\left[f_{i, t+1}=f_{i t}-\frac{1}{\mu}\right] \\
& \geq \frac{2}{11} f_{i t}\left(1-f_{i t}\right)\left(D_{t}\right)^{-1 / 2}-\operatorname{Pr}\left\{\left(x_{i}^{1} \neq x_{i}^{2}\right) \wedge\left(\left\{x^{1}, x^{2}\right\} \cap G_{n k} \neq \emptyset\right)\right\}
\end{aligned}
$$

We now estimate this correction term, first by noting that $\operatorname{Pr}\left\{\left(x_{i}^{1} \neq\right.\right.$ $\left.x_{i}^{2}\right) \wedge\left(\left\{x^{1}, x^{2}\right\} \cap G_{n k} \neq \emptyset\right\}\right]=\operatorname{Pr}\left[x_{i}^{1} \neq x_{i}^{2}\right] \cdot \operatorname{Pr}\left\{\left\{x^{1}, x^{2}\right\} \cap G_{n k} \neq\right.$ $\emptyset\left|x_{i}^{1} \neq x_{i}^{2}\right|$, then by using the union bound estimate $\operatorname{Pr}\left\{\left\{x^{1}, x^{2}\right\} \cap\right.$ $\left.G_{n k} \neq \emptyset\left|x_{i}^{1} \neq x_{i}^{2}\right| \leq 2 \operatorname{Pr}\left[x^{1} \in G_{n k} \mid x_{i}^{1} \neq x_{i}^{2}\right] .\right.$ Conditional on $x_{i}^{1} \neq x_{i}^{2}$, the bit string $x^{1}$ is sampled from $\operatorname{Sample}\left(f_{t}\right)$, however, conditional on the $i$-th bit being zero or one. In either case, to have $x^{1} \in G_{n k}$, we need that $\hat{D}=\sum_{j \neq i}\left(1-x_{i}^{1}\right)$ is at most $k \leq \frac{1}{2}\left(D_{t}-1\right)$, where we recall that $D_{t} \geq D^{\prime \prime} \geq 2 k+1$. Since $E[\hat{D}]=D_{t}-\left(1-f_{i t}\right) \geq$ $D_{t}-1$, by Lemma 1 with $\delta=\frac{1}{2}$ this event happens with probability at most $\exp \left(-\frac{1}{8}\left(D_{t}-1\right)\right)$. Together with $\operatorname{Pr}\left[x_{i}^{1} \neq x_{i}^{2}\right]=2 f_{i t}\left(1-f_{i t}\right)$, we obtain

$$
\begin{aligned}
& \operatorname{Pr}\left[f_{i, t+1}=f_{i t}+\frac{1}{\mu}\right]-\operatorname{Pr}\left[f_{i, t+1}=f_{i t}-\frac{1}{\mu}\right] \\
& \quad \geq \frac{2}{11} f_{i t}\left(1-f_{i t}\right)\left(D_{t}\right)^{-1 / 2}-2 f_{i t}\left(1-f_{i t}\right) \exp \left(-\frac{1}{8}\left(D_{t}-1\right)\right)
\end{aligned}
$$

which is non-negative since $D_{t} \geq D^{\prime \prime} \geq C_{D^{\prime \prime}}$, which was chosen sufficiently large.

Consequently, the process $\left(f_{i t}\right)_{t}$ satisfies the assumptions of Lemma 3 up to time $T^{\prime \prime}$. If $T^{\prime \prime}<C_{T^{\prime \prime}} \mu \sqrt{n}$, we artificially extend the process (for the following argument only) by setting $f_{i t}=f_{i T^{\prime \prime}}$ for all $t \in\left[T^{\prime \prime}+1 . . C_{T^{\prime \prime}} \mu \sqrt{n}\right]$. By Lemma 3 we thus obtain that up to time $T=\left\lfloor C_{T^{\prime \prime}} \mu \sqrt{n}\right\rfloor$, the $i$-th frequency is always at least $\frac{1}{3}$ with probability $1-2 \exp \left(-\frac{\mu^{2}}{18 T}\right) \geq 1-2 \exp \left(-\frac{\mu}{18 C_{T^{\prime \prime}} \sqrt{n}}\right) \geq$ $1-2 \exp \left(-\frac{C_{T^{\prime \prime}}}{18 C_{T^{\prime \prime}}} \ln n\right)$. With a union bound over the $n$ frequencies, we have $f_{t} \in\left[\frac{1}{3}, 1\right]^{n}$ in this time interval with probability at least $1-2 n \exp \left(-\frac{C_{T^{\prime \prime}}}{18 C_{T^{\prime \prime}}} \ln n\right)=1-O(1 / n)$ by choice of $c_{\mu}$ and $C_{T^{\prime \prime}}$.

Since $D^{\prime}=C_{D^{\prime}} \ln n$ with $C_{D^{\prime}} \geq 12$ and $k \leq C_{k} \ln n \leq \frac{C_{D^{\prime \prime}}}{\ln n}$, by Lemma 1 and a union bound the probability that within the first $T^{\prime} \leq C_{T^{\prime}} \mu \sqrt{n}$ iterations a search point in the gap region is sampled, is at most $2 C_{T^{\prime}} \mu \sqrt{n} \exp \left(-\frac{C_{D^{\prime \prime}}}{8} \ln n\right) \leq 2 C_{T^{\prime}} n^{C_{\mu}+0.5-C_{D^{\prime \prime}} / 8}=O(1 / n)$. Consequently, by Lemma 5, after at most $C_{T^{\prime}} \mu \sqrt{n}$ iterations with probability $1-O(1 / n)$ we have $D_{t} \leq D^{\prime}$.

We now estimate the additional time it takes to reach $D_{t} \leq D^{\prime \prime}$. Let $t_{0}$ be the first time such that $D_{t} \leq D^{\prime}$. By Lemma 6 and using our assumption that $C_{D^{\prime \prime}}$ is a large absolute constant, we have $E\left[D_{t}-D_{t+1} \mid D_{t}\right] \geq \frac{1}{\mu}$ when $D_{t} \geq D^{\prime \prime} \geq C_{D^{\prime \prime}}$. We define a random process $\hat{D}_{t}$ as follows. Let $t \geq t_{0}$. If $D_{s}<D^{\prime \prime}$ for some $s \in\left[t_{0} . . t\right]$, then $\hat{D}_{t-t_{0}}=0$. Otherwise, $\hat{D}_{t-t_{0}}=D_{t}$. By the above observation, we have $E\left[\hat{D}_{t}-\hat{D}_{t+1} \mid \hat{D}_{t}>0\right] \geq \frac{1}{\mu}$. By the additive drift theorem [18], also to be found in the recent survey [22], $T:=\$ $\min \left\{t \mid \hat{D}_{t}=0\right\}$ satisfies $E[T] \leq \frac{D^{\prime}}{1 / \mu}=O(\mu \log n)$. By Markov's inequality, we have $T=O\left(\mu n^{0.4} \log n\right)$ with probability $1-n^{-0.4}$.

Let now $t_{0}$ be such that $D_{t_{0}} \leq D^{\prime \prime}$ and all frequencies are at least $\frac{1}{3}$. We first argue that if $D_{t} \leq \ln (n)^{2}$, then $\operatorname{Pr}\left[D_{t+1} \geq D_{t}+\right.$ $\left.\frac{4}{\mu} \ln (n)^{2}\right] \leq n^{o(1)}$. By Lemma 1, we have $\operatorname{Pr}\left\{d\left(x^{j}\right) \geq 2 \ln (n)^{2}\right\} \leq$ $\exp \left(-\ln (n)^{2} / 3\right)=n^{o(1)}$ for $j=1,2$. Consequently, with probability $1-n^{o(1)}$, we have both $\left\|x^{1}\right\|_{1} \geq n-2 \ln (n)^{2}$ and $\left\|x^{2}\right\|_{1} \geq n-$ $2 \ln (n)^{2}$. In this case, the Hamming distance between $x^{1}$ and $x^{2}$ satisfies $H\left(x^{1}, x^{2}\right) \leq 4 \ln (n)^{2}$, which implies that $\left|D_{t}-D_{t+1}\right| \leq$
$\left\|f_{t}-f_{t+1}\right\|_{1} \leq \frac{4}{\mu} \ln (n)^{2}$ and thus $D_{t+1} \leq D_{t}+\frac{4}{\mu} \ln (n)^{2}$. By a union bound, with probability $1-n^{o(1)}$, this happens in all iterations $t_{0}, \ldots, t_{0}+\left\lfloor\frac{D^{\prime \prime}}{\left(4 / \mu\right) \ln (n)^{2}}\right\rfloor-1$ and consequently, throughout these $L=\left\lfloor\frac{D^{\prime \prime}}{14 / \mu(\ln (n)^{2})}\right\rfloor$ iterations we have $D_{t} \leq 2 D^{\prime \prime}$. Note that $L=$ $O(\mu / \log (n))$, hence throughout this period we also have $f_{i t} \geq \frac{1}{2}-$ $\frac{1}{\mu} L \geq 0.32$ (assuming $n$ to be sufficiently large). By Lemma 7 , the probability that a fixed search point sampled in this period is the optimum, is at least $0.32^{2 D^{\prime \prime} / 0.68} \geq 0.32^{4 C_{k}} \ln (n) / 0.68 \geq n^{-6.71 C_{k}} \geq$ $n^{-0.34}$ by choice of $C_{k}$. Hence the probability that the optimum is not sampled in this period is at most $\left(1-n^{-0.34}\right)^{2 L} \leq \exp \left(-n^{-0.34}\right.$. $\left.\mu / \ln (n)^{2}\right\} \leq \exp \left(-\Omega\left(n^{0.16} / \log (n)\right)\right)$.

Let us remark that we did not try to optimize the implicit constants, nor did we try to find the largest constant $C_{k}$ such that the $O(n \log n)$ runtime guarantee holds for all $k \leq C_{k} \ln (n)-1$. We further note that all but one argument in the above proof, by choosing the constants right, would give a success probability of $1-n^{-c}$, where $c$ can be any constant. This is not true for the Markov bound argument in the analysis of the time to reach a $D_{t}$ value of at most $D^{\prime \prime}$. Without further details, we note that also for this phase an arbitrary inverse-polynomial failure probability could be obtained with stronger methods. Finally, we note that by taking $k=1$, our result also applies to the OneMax function.

## 4 CONCLUSION

This is, to the best of our knowledge, only the second mathematical analysis of an EDA on a multi-modal optimization problem. Our main result shows that the cGA can optimize jump functions with logarithmic jump sizes in asymptotically the same efficiency as the simple OneMax function. It thus does not suffer from the fitness valleys present in these objective function.

The obvious question arising from this work is to what extent such or similar results hold for other EDAs. Natural candidates could be the UMDA, for which several rigorous runtime results exist, see [21], and the significance-based cGA [12], which might profit from using only the three frequencies $\frac{1}{6}, \frac{1}{2}$, and $1-\frac{1}{n}$. Equally interesting would be results for other optimization problems. We would speculate that our result easily extends to the plateau function defined in [1], so more interesting would be combinatorial optimization problems with significant local optima or plateaus.

On the more speculative side, given that the black-box complexity of jump functions is low even for large jump sizes [2, 11], one could also try to challenge the upper bound $\exp (O(k))$ given in [17] for larger values of $k$. Since [9] shows a matching lower bound of $\exp (\Omega(k))$, the only way to improve the exponential dependence on $k$ would be via a modification of the cGA. We have no idea to what extent this is possible, but given that [17] and this work show that EDAs can be more powerful on multi-modal functions, this is an interesting direction for future research.

## ACKNOWLEDGMENTS

This work was supported by a public grant as part of the Investissement d'avenir project, reference ANR-11-LABX-0056-LMH, LabEx LMH, in a joint call with the Gaspard Monge Program for optimization, operations research and their interactions with data sciences.
