# Level-Based Analysis of Genetic Algorithms and Other Search Processes 

Dogan Corus, Duc-Cuong Dang, Anton V. Eremeev ${ }^{\oplus}$, and Per Kristian Lehre ${ }^{\ominus}$


#### Abstract

Understanding how the time complexity of evolutionary algorithms (EAs) depend on their parameter settings and characteristics of fitness landscapes is a fundamental problem in evolutionary computation. Most rigorous results were derived using a handful of key analytic techniques, including drift analysis. However, since few of these techniques apply effortlessly to population-based EAs, most time complexity results concern simple EAs, such as the (1+1) EA. We present the level-based theorem, a new technique tailored to population-based processes. It applies to any nonelitist process where offspring are sampled independently from a distribution depending only on the current population. Given conditions on this distribution, our technique provides upper bounds on the expected time until the process reaches a target state. The technique is demonstrated on pseudo-Boolean functions, the sorting problem, and approximation of optimal solutions in combinatorial optimization. The conditions of the theorem are often straightforward to verify, even for genetic algorithms and estimation of distribution algorithms which were considered highly nontrivial to analyze. The proofs for the example applications are available in the supplementary materials. Finally, we prove that the theorem is nearly optimal for the processes considered. Given the information the theorem requires about the process, a much tighter bound cannot be proved.


Index Terms-Approximation, estimation of distribution algorithm (EDA), genetic algorithm (GA), runtime analysis.

## I. INTRODUCTION

THE THEORETICAL understanding of evolutionary algorithms (EAs) has advanced significantly over the last decades. Significant progress in developing and understanding a formal model of canonical genetic algorithms (GAs) and their generalizations was made in the nineties using dynamical systems [53]. Notably, the behavior of the dynamical systems model is closely related to the local optima structure of the problem in the case of binary search spaces [54].

Manuscript received October 27, 2016; revised February 21, 2017 and June 13, 2017; accepted July 29, 2017. Date of publication September 18, 2017; date of current version September 28, 2018. This work was supported in part by the European Union Seventh Framework Programme (FP7/2007-2013, SAGE) under Grant 618091, and in part by the Russian Foundation for Basic Research under Grant 15-01-00785 and Grant 16-01-00740. (Corresponding author: Per Kristian Lehre.)
D. Corus was with the School of Computer Science, University of Nottingham, Nottingham NG8 1BB, U.K., and is now with the Department of Computer Science, University of Sheffield, Sheffield S1 4DP, U.K.
D.-C. Dang is an Independent Researcher.
A. V. Eremeev is with the Sobolev Institute of Mathematics SB RAS, Omsk 644099, Russia.
P. K. Lehre is with the School of Computer Science, University of Birmingham, Birmingham B15 2TT, U.K. (e-mail: p.k.lehre@cs.bham.ac.uk). This paper has supplementary downloadable multimedia material available at http://ieeexplore.ieee.org provided by the authors.
Digital Object Identifier 10.1109/TEVC.2017.2753538

However, most of these findings relate to the infinite population limit, from which it is difficult to derive statements about performance. Researchers from theoretical computer science argued in the early 2000s that EC theory had attempted to make either too general, or too precise statements [3]. Instead, one should develop techniques for deriving rigorous statements about worst-case optimization time, starting from the simplest possible settings. Much of the work assumed a population size of one and no crossover operator, e.g., the (1+1) EA [20].

Early analyses of EAs with larger population sizes often ignored the recombination operator. The family tree technique was introduced in [56] to analyze the $(\mu+1)$ EA. The performance of the $(\mu+\mu)$ EA for different settings of the population size was analyzed in [30], using Markov chains to model the search processes, and in [4], using a similar argument to fitness levels. The analysis of parallel EAs in [35] also made use of the fitness levels argument. The inefficiency of standard fitness proportionate selection without scaling was shown in [36] and [44], using drift analysis [28]. In the recently introduced switch analysis, the progress of the EA is analyzed relative to a reference process that is easier to understand [58].

Runtime analyses considering recombination often aimed at understanding how evolutionary search can benefit from sexual reproduction. For the OneMax problem, it is known that the simple genetic algorithm (SGA) [53] is inefficient, even when crossover is enabled [45]. For a variant of the $(\mu+1)$ EA, crossover can speed up by a factor of 2 compared to the (1+1) EA [51]. GAs with even higher (nonconstant) speedups on OneMax are known, but they rely on nonconventional reproduction mechanisms [16], [17]. The unrestricted blackbox complexity of OneMax is $\Omega(n / \log (n))$ [21], the speedup of any unrestricted black-box algorithm relative to the (1+1) EA is therefore at most $\mathcal{O}\left(\log (n)^{2}\right)$. More complex settings are required to show further speedups. So-called convex search algorithms, which include nonelitist GAs with gene pool recombination and no mutation, have been analyzed on quasi-concave fitness landscapes [41]. As a special case, convex search algorithm has expected runtime $\mathcal{O}(n \log n)$ on LEADINGONES, i.e., a speedup of $\Theta(n / \log (n))$ compared with the (1+1) EA. Prügel-Bennett et al. [47] considered nonelitist GAs, also without mutation, on noisy OneMax. The $(\mu+1)$ GA decreases the runtime on the JUMP problem, however this was first only shown for artificially small crossover probabilities [31], [32]. For realistic crossover probabilities, the $(\mu+1)$ GA decreases the runtime by an exponential factor on instances of an FSM testing problem, however, this result assumes a deterministic crowding diversity mechanism [39]. It was recently shown that

the standard $(\mu+1)$ GA has a speed up of $\Omega(n / \log (n))$ on JUMP compared to the mutation-only variant $(\mu+1)$ EA [10].

Estimation of distribution algorithms (EDAs), a relatively new type of EAs [34], build explicit probabilistic models in every generation from the fittest individuals, from which the next generation is sampled. The sequence of probability distributions should converge to a distribution concentrated on the optimal search points. Traditional EAs can be seen as special cases of EDAs, where the probability distributions are given implicitly via their genetic operators and selection mechanisms. Most theoretical studies of EDAs have considered convergence and scalability properties [27], [43], [46], [50], [59], and rigorous runtime analyses of EDAs are still rare. Droste's $\Theta(K n)$ bound on the expected runtime on linear functions for compact GA (cGA) with update parameter $K \geq n^{1+e}$, is an early rigorous result on the runtime of EDAs [19]. Recent runtime analyses have demonstrated the noise robustness of cGA [25], as well as the impact of its update parameter [52]. The runtime of univariate marginal distribution algorithm (UMDA), a more complex EDA [42], has been analyzed in a series of papers [5]-[8], [13], [37], [57]. Chen et al. [6] described easy and hard functions for the UMDA under the so-called "no-random-error" assumption and with a sufficiently large population. This assumption was lifted in [8], but the analysis still assumed an unrealistically large population size, leading to a high bound on the expected runtime. It is usually necessary to impose margins on the probability distribution of the UMDA [7], however, the only known setting where the UMDA outperforms the $(1+1)$ EA assumes the UMDA without margins [5]. An early variant of the level-based method provided the first upper bound of $\mathcal{O}(n \lambda \log \lambda)$ on the runtime of UMDA with realistic population size $\lambda=\Omega(\log n)$ on ONEMAX [13]. Recently, a more precise application of the level-based method tightened this bound to $\mathcal{O}(n \lambda)$ under the assumption that the parent population size is $\mu=\mathcal{O}(\sqrt{n})$ [37]. For offspring population sizes $\lambda=\mathcal{O}(\log n)$, this runtime bound is tight, because it matches the lower bound of $\Omega(\mu n+n \log n)$ shown via drift analysis [33]. A different argument than the level-based method yielded a similar upper bound [57] for the UMDA.

We show that all nonelitist EAs with or without crossover, and even EDAs, can be cast and analyzed in the same framework. An early version of this paper was published in [9]. This followed from work dating back to the introduction of a fitness level technique for nonelitist EAs with linear ranking selection [40], later on generalized to many selection mechanisms and unary variation operators [36], with a refined result in [14]. The original fitness level technique and its generalization to the level-based technique have already found several applications, including analysis of EAs in uncertain environments, such as partial information [14], noisy [12], and dynamic fitness functions [11]. It has also been used to analyze self-adaptive EAs [15], pointing out multimodal fitness landscapes where they outperform classical, elitist EAs.

This paper improves the main result of [9] in many aspects. A more careful analysis of the population dynamics leads to a much tighter expression of the runtime bound compared to [9], and close to optimal for the class of search processes the theorem applies to. This immediately implies improved results in the previously mentioned applications. In particular,

## Algorithm 1 Population-Based Algorithm

Require: A finite state space $\mathcal{X}$, and population size $\lambda \in \mathbb{N}$, a mapping $D$ from $\mathcal{X}^{\lambda}$ to the space of prob. dist. over $\mathcal{X}$, and an initial population $P_{0} \in \mathcal{X}^{\lambda}$.

1: for $t=0,1,2, \ldots$ until termination condition met do
2: $\quad$ Sample $P_{t+1}(i) \sim D\left(P_{t}\right)$ independently for all $i \in[\lambda]$.
the leading term in the runtime is improved by a factor of $\Omega\left(\delta^{-3}\right)$, where $\delta$ characterizes how fast good individuals can populate the population. This significantly improves the results of [12] and [14] concerning noisy optimization, for which $\delta$ is often very small (e.g., $1 / n$ ). We also recommend a stepwise guideline for how to apply the theorem to new settings. Example applications are given for the cases of GAs and UMDA in optimizing standard pseudo-Boolean functions, a simple combinatorial problem, and in searching for local optima of NP-hard problems.

In this paper, Section II describes the class of algorithms covered by the level-based theorem, showing that many GAs and EDAs are special cases. The section then states the main theorem and corollaries for special cases, followed by their proofs. Sections IV and V apply the level-based theorem to the simple genetic algorithm (SGA) and UMDA on example problems. Section VI proves that the level-based theorem is tight for the class of algorithms considered. Section VII concludes this paper. Some proofs have been omitted due to space restrictions, but are in the supplementary materials.

## II. Main Result

## A. Abstract Algorithmic Scheme

We consider population-based processes as stochastic processes $\left(P_{t}\right)_{t \in \mathbb{N}}$, where for each "generation" $t \in \mathbb{N}, P_{t}=$ $\left(x_{1}, \ldots, x_{\lambda}\right) \in \mathcal{X}^{\lambda}$ is a vector of $\lambda$ individuals, and where the set $\mathcal{X}$ represents the "search space" or "genospace." Our goal is to estimate the expected number of generations until the population contains at least one element in some given subset of $\mathcal{X}$. Our main assumption is that for every generation $t \in \mathbb{N}$, each individual in generation $P_{t+1}$ is obtained by independent sampling from a distribution $D\left(P_{t}\right)$. Intuitively, $D$ describes the randomized process determining how new individuals are produced, and may include fitness evaluations, selection, variation operators, external noise etc. Formally, $D$ is a mapping from the set of all possible populations $\mathcal{X}^{\lambda}$ into the space of probability distributions over $\mathcal{X}$. This scheme is summarized in Algorithm 1.

Algorithm 1 covers many nonelitist search heuristics, such as stochastic beam search [53], EDA, and GAs [26]. For example, the GA given by Algorithm 2 is a special case of Algorithm 1, where the operator $D$ corresponds to lines 3-5 in Algorithm 2. Here, the random operator select: $\mathcal{X}^{\lambda} \rightarrow[\lambda]$ represents a selection mechanism, which given a vector of $\lambda$ individuals, returns the index of the individual to be selected. The selection mechanism is typically defined relative to a fitness function $f: \mathcal{X} \rightarrow \mathbb{R}$. The GA uses the two variation operators mutate: $\mathcal{X} \rightarrow \mathcal{X}$, and crossover: $\mathcal{X} \times \mathcal{X} \rightarrow \mathcal{X}$.

## B. Level-Based Theorem

We now state the main result of this paper: a general technique for obtaining upper bounds on the expected runtime of

## Algorithm 2 GA

Require: A finite set $\mathcal{X}$, population size $\lambda \in \mathbb{N}$, recombination rate $p_{\varepsilon} \in(0,1]$, and initial pop. $P_{0} \in \operatorname{Unif}\left(\mathcal{X}^{\lambda}\right)$.
for $t=0,1,2, \ldots$ until termination condition met do
for $i=1$ to $\lambda$ do
$u:=P_{t}\left(\operatorname{select}\left(P_{t}\right)\right), v:=P_{t}\left(\operatorname{select}\left(P_{t}\right)\right)$.
With prob. $p_{\varepsilon}, x:=\operatorname{crossover}(u, v)$ else $x:=u$.
$P_{t+1}(i):=$ mutate $(x)$.
any process that can be described in the form of Algorithm 1. We use the following notation. The natural logarithm is denoted by $\ln (\cdot)$, and $[n]=\{1, \ldots, n\}$ denotes the first $n$ natural numbers. Suppose that for some $m$ there is an ordered partition of $\mathcal{X}$ into subsets $\left(A_{1}, \ldots, A_{m}\right)$ which we call levels. We define $A_{\geq j}:=\bigcup_{i=j}^{m} A_{i}$, i.e., the union of all levels above level $j$. The canonical partition of $\mathcal{X}$ with respect to a fitness function $f: \mathcal{X} \rightarrow \mathbb{R}$, is $x, y \in A_{j}$ if and only if $f(x)=f(y)$ (see [36]). The partition is called $f$-based if $f(x)<f(y)$ for all $x \in A_{j}, y \in A_{j+1}$ and all $j \in[m-1]$. As a result of the algorithmic abstraction, our main theorem is not limited to this particular type of partition. Let $P \in \mathcal{X}^{\lambda}$ be a population vector of a finite number $\lambda \in \mathbb{N}$ of individuals. Given any subset $A \subseteq \mathcal{X}$, we define $|P \cap A|:=\mid\{i \mid P(i) \in A\}|$, i.e., the number of individuals in $P$ that belong to $A$.

Theorem 1: Given a partition $\left(A_{1}, \ldots, A_{m}\right)$ of $\mathcal{X}$, define $T:=\min \left\{t \lambda \mid\left|P_{t} \cap A_{m}\right|>0\right\}$, where for all $t \in \mathbb{N}, P_{t} \in \mathcal{X}^{\lambda}$ is the population of Algorithm 1 in generation $t$. If there exist $z_{1}, \ldots, z_{m-1}, \delta \in(0,1]$, and $\gamma_{0} \in(0,1)$ such that for any population $P \in \mathcal{X}^{\lambda}$
(G1): for each level $j \in[m-1]$, if $\left|P \cap A_{\geq j}\right| \geq \gamma_{0} \lambda$; then

$$
\operatorname{Pr}_{y \sim D(P)}\left(y \in A_{\geq j+1}\right) \geq z_{j}
$$

(G2): for each level $j \in[m-2]$, and all $\gamma \in\left(0, \gamma_{0}\right]$ if $\left|P \cap A_{\geq j}\right| \geq \gamma_{0} \lambda$ and $\left|P \cap A_{\geq j+1}\right| \geq \gamma \lambda$, then

$$
\operatorname{Pr}_{y \sim D(P)}\left(y \in A_{\geq j+1}\right) \geq(1+\delta) \gamma
$$

(G3): and the population size $\lambda \in \mathbb{N}$ satisfies

$$
\lambda \geq\left(\frac{4}{\gamma_{0} \delta^{2}}\right) \ln \left(\frac{128 m}{z_{*} \delta^{2}}\right), \text { where } z_{*}:=\min _{j \in[m-1]}\left\{z_{j}\right\}
$$

then

$$
E[T] \leq\left(\frac{8}{\delta^{2}}\right) \sum_{j=1}^{m-1}\left(\lambda \ln \left(\frac{6 \delta \lambda}{4+z_{j} \delta \lambda}\right)+\frac{1}{z_{j}}\right)
$$

The level-based theorem gives an upper bound on the expected time until the algorithm discovers an element in the last level $A_{m}$, given that certain conditions on the operator $D$ and population size $\lambda$ are satisfied. Time is measured by the random variable $T$, which is defined as the number of individuals sampled in line 2 of Algorithm 1 until the end of the first generation having an individual in level $A_{m}$. This is an upper bound on the total number of sampled search points until a search point in $A_{m}$ is conceived for the first time.

Informally, the two first conditions require a relationship between the current population $P$ and the distribution $D(P)$ of the individuals in the next generation. Condition (G1) demands that the probability of creating an individual at level

Algorithm 3 Example Algorithm to Illustrate Theorem 1
: Sample an initial population $P_{0} \sim \operatorname{Unif}\left([m]^{\lambda}\right)$ u.a.r.
for $t=0,1,2, \ldots$ until termination condition met do
Sort $P_{t}=\left(x_{1}, \ldots, x_{k}\right)$ s.t. $x_{1} \geq x_{2} \geq \cdots \geq x_{k}$.
for $i=1$ to $\lambda$ do
$z:=x_{k}$, where $k \sim \operatorname{Unif}([\lambda / 2])$.
$y:=z+\operatorname{Unif}(\{-c, 0,1\})$ for any fixed $c \in[m]$
$P_{t+1}(i):=\max \{1, \min \{y, m\}\}$.
$j+1$ or higher is at least $z_{j}$ when some fixed portion $\gamma_{0}$ of the population has reached level $j$ or higher. Furthermore, if the number of individuals at level $j+1$ or higher is at least $\gamma \lambda>0$, condition (G2) requires that their number tends to increase further, by a multiplicative factor of $1+\delta$. Finally, (G3) requires a sufficiently large population. When all conditions are satisfied, an upper bound on the expected time for the algorithm to create an individual in $A_{m}$ is guaranteed.

We recommend these steps when applying the theorem.

1) Identify a partition of $\mathcal{X}$ reflecting the "typical" progress of the population to the target set $A_{m}$.
2) Find parameter settings of the algorithm and corresponding parameters $\gamma_{0}$ and $\delta$ which allow condition (G2) to be satisfied, possibly by adjusting the partition of $\mathcal{X}$.
3) For each level $j \in[m-1]$, estimate lower bounds $z_{j}$ such that condition (G1) holds.
4) Determine the lower bound on the population size $\lambda$ in (G3), using the parameters obtained in the previous steps.
5) Compute the upper bound on $E[T]$. The terms $\ln \left([(6 \delta \lambda) /\left(4+z_{j} \delta \lambda\right)\right])$ can be bounded by underestimating the denominator, either by 4 , or by $z_{j} \delta \lambda$, leading to the upper bounds $\ln (3 \lambda / 2)$, respectively, $\ln \left(6 / z_{j}\right)$.
We now illustrate this methodology on a simple example.
Corollary 1: Algorithm 3 with $\lambda \geq 72(\ln (m)+9)$ produces less than $216(m-1)(\lambda+1)$ individuals in expectation before it discovers $m$.

To illustrate Theorem 1, we estimate the time until the element $m$ is contained in the population of Algorithm 3. The search space $\mathcal{X}$ is the set of natural numbers between 1 and $m$. Following the scheme of Algorithm 1, the operator $D$ corresponds to lines 3-7. The new individual $y$ is obtained by first selecting uniformly at random one of the best $\lambda / 2$ individuals in the population (lines 3 and 5) and mutating this individual by adding 1 subtracting $c$ or doing nothing, with equal probabilities. We will see that the value of $c$ does not matter in our analysis.

We now carry out the steps described previously.
Step 1: We use the partition $A_{j}:=\{j\}$ for all $j \in[m]$.
Step 2: Assume that the current level is $j<m-1$. This means that in $P_{t}$, there are $\gamma_{0} \lambda$ individuals in $A_{\geq j}$, i.e., with fitness at least $j$, and at least $\gamma \lambda$ but less than $\gamma_{0} \lambda$ individuals in $A_{\geq j+1}$, i.e., with fitness at least $j+1$. We need to estimate $\operatorname{Pr}_{y \sim D\left(P_{t}\right)}\left(y \in A_{\geq j+1}\right)$, i.e., the probability of producing an individual with fitness at least $j+1$. We say that a selection event is "good" if in line 5, the algorithm selects an individual in $A_{\geq j+1}$, i.e., with fitness at least $j+1$. If $\gamma \leq 1 / 2$, then the

probability of a good selection event is at least $\gamma \lambda /(\lambda / 2)=2 \gamma$. We say that a mutation event is good if in line 6 , the algorithm does not subtract $c$ from the selected search point. The probability of a good mutation event is $2 / 3$. Selection and mutation are independent events, hence we have shown for all $\gamma \in(0,1 / 2]$ that $\operatorname{Pr}_{y \sim D\left(P_{y}\right)}\left(y \in A_{\geq j+1}\right) \geq$ $(2 \gamma)(2 / 3)=\gamma(1+(1 / 3))$. Condition (G2) is therefore satisfied with $\delta=1 / 3$ for any $\gamma_{0} \leq 1 / 2$. We will choose the parameter $\gamma_{0}$ later.
Step 3: Assume that population $P_{t}$ has at least $\gamma_{0} \lambda$ individuals in $A_{\geq j}$. The algorithm can then produce an individual in $A_{\geq j+1}$ by selecting an individual in $A_{\geq j}$, and mutate this individual into $A_{\geq j+1}$ by adding 1 in line 6 . We can conveniently fix $\gamma_{0}=$ $1 / 2$, so that the probability of selecting an individual in $A_{\geq j}$ becomes 1 . Furthermore, the probability of adding 1 to the selected individual is exactly $1 / 3$. Hence, we have $\operatorname{Pr}_{y \sim D\left(P_{y}\right)}\left(y \in A_{\geq j+1}\right) \geq 1(1 / 3)$, and we can satisfy condition (G1) by defining $z_{j}:=1 / 3$ for all $j \in[m-1]$.
Step 4: For the parameters we have chosen, it is easy to see by numerical calculation that the population size $\lambda \geq 72(\ln (m)+9)$ satisfies condition (G3).
Step 5: Using that $\ln ([(6 \delta \lambda) /\left(4+\delta \lambda z_{j}\right)])<\ln \left(6 / z_{j}\right)$, the expected time to discover the point $m$ is no more than

$$
\begin{aligned}
\frac{8}{(1 / 3)^{2}} & \sum_{j=1}^{m-1}\left(\lambda \ln \left(\frac{6}{1 / 3}\right)+\frac{1}{1 / 3}\right) \\
& <216(m-1)(\lambda+1)
\end{aligned}
$$

## C. Proof of the Level-Based Theorem

Theorem 1 will be proved using drift analysis [28], [29], a standard tool in theory of randomized search heuristics. We a variant of the additive drift theorem [29], which is proved in the supplementary materials. The lower bound statement will be used in Section VI to evaluate the tightness of the theorem. In what follows, " $\left(Z_{t+1}-Z_{t}+\varepsilon\right) ; t<T_{a}$ " denotes " $\left(Z_{t+1}-Z_{t}+\varepsilon\right) \cdot \mathbb{1}_{\left[t<T_{a}\right]}$ " (see [55, 6.3]).

Theorem 2 (Additive Drift Theorem): Let $\left(Z_{t}\right)_{t \in \mathbb{N}}$ be a discrete-time stochastic process in $[0, \infty)$ adapted to any filtration $\left(\mathscr{F}_{t}\right)_{t \in \mathbb{N}}$. Define $T_{a}:=\min \left[t \in \mathbb{N} \mid Z_{t} \leq a\right]$ for any $a \geq 0$. For some $\varepsilon>0$ and constant $0<b<\infty$, define the conditions
1.1) $E\left[Z_{t+1}-Z_{t}+\varepsilon ; t<T_{a} \mid \mathscr{F}_{t}\right] \leq 0$ for all $t \in \mathbb{N}$;
1.2) $E\left[Z_{t+1}-Z_{t}+\varepsilon ; t<T_{a} \mid \mathscr{F}_{t}\right] \geq 0$ for all $t \in \mathbb{N}$;
2) $Z_{t}<b$ for all $t \in \mathbb{N}$;
3) $E\left[T_{a}\right]<\infty$.

If 1.1), 2), and 3) hold, then $E\left[T_{a} \mid \mathscr{F}_{0}\right] \leq Z_{0} / \varepsilon$.
If 1.2), 2), and 3) hold, then $E\left[T_{a} \mid \mathscr{F}_{0}\right] \geq\left(Z_{0}-a\right) / \varepsilon$.
In the proofs of Theorems 1 and 8 , it will be important that conditions 1.1) and 1.2) apply to the whole past-present (see [28]), unlike the usual additive drift statement [29] that is conditioned on the present state only.

When applying the additive drift theorem to a complex process, $Z_{t}$ is the result of a (measurable) mapping of the states of the process to a real number. Such a mapping is called the distance function, which measures the distance to some target state. Our distance function takes into account both the
current level of the population, as well as the distribution of the population around the current level. In particular, let the current level $Y_{t}$ be the highest level $j \in[m]$ such that there are at least $\gamma_{0} \lambda$ individuals at level $j$ or higher. Furthermore, for any level $j \in[m]$, let $X_{t}^{(j)}$ be the number of individuals at level $j$ or higher. Hence, we describe the dynamics of the population by $m+1$ stochastic processes $X_{t}^{(1)}, \ldots, X_{t}^{(m)}, Y_{t}$. Assuming that these processes are adapted to a filtration $\mathscr{F}_{t}$, we write $E_{t}[\mathrm{X}]:=E\left[X \mid \mathscr{F}_{t}\right]$ and $\operatorname{Pr}_{t}(\mathcal{E}):=E\left[\mathbb{1}_{\mathcal{E}} \mid \mathscr{F}_{t}\right]$. Our approach is to measure the distance of the population at time $t$ by a scalar $g\left(X_{t}^{(Y_{t}+1)}, Y_{t}\right)$, where $g$ is a function that satisfies the conditions in Definition 1.

Definition 1: A function $g:\left(\{0\} \cup\{\lambda\}\right) \times[m] \rightarrow \mathbb{R}$ is called a level function if the following three conditions hold:

1) $\forall x \in\{0\} \cup\{\lambda\}, \forall y \in[m-1]: g(x, y) \geq g(x, y+1)$;
2) $\forall x \in\{0\} \cup\{\lambda-1\}, \forall y \in[m]: g(x, y) \geq g(x+1, y)$;
3) $\forall y \in[m-1]: g(\lambda, y) \geq g(0, y+1)$.

Note that the sum of two level functions is also a level function. Furthermore, the conditions ensure that the distance $g\left(X_{t}^{(Y_{t}+1)}, Y_{t}\right)$ of the population decreases monotonically with the current level $Y_{t}$. Lemma 1 shows that this monotonicity allows an upper bound on the distance in the next generation which is partly independent of the change in current level.

Lemma 1: If $Y_{t+1} \geq Y_{t}$, then for any level function $g$

$$
g\left(X_{t+1}^{(Y_{t+1}+1)}, Y_{t+1}\right) \leq g\left(X_{t+1}^{(Y_{t}+1)}, Y_{t}\right)
$$

Proof: The statement is trivial when $Y_{t}=Y_{t+1}$. On the other hand, if $Y_{t+1}>Y_{t}$, then the conditions in Definition 1 imply

$$
\begin{aligned}
g\left(X_{t+1}^{(Y_{t+1}+1)}, Y_{t+1}\right) & \leq g\left(0, Y_{t+1}\right) \leq g\left(0, Y_{t}+1\right) \\
& \leq g\left(\lambda, Y_{t}\right) \leq g\left(X_{t+1}^{(Y_{t}+1)}, Y_{t}\right)
\end{aligned}
$$

Proof of Theorem 1: We apply Theorem 2 with respect to the parameter $a=0$ and the process $Z_{t}:=g\left(X_{t}^{(Y_{t}+1)}, Y_{t}\right)$, where $g$ is a level-function, and $\left(Y_{t}\right)_{t \in \mathbb{N}}$ and $\left(X_{t}^{(j)}\right)_{t \in \mathbb{N}}$ for $j \in[m]$ are stochastic processes, which will be defined later. $\left(\mathscr{F}_{t}\right)_{t \in \mathbb{N}}$ is the filtration induced by the populations $\left(P_{t}\right)_{t \in \mathbb{N}}$.

We will assume w.l.o.g. that condition (G2) is also satisfied for $j=m-1$, for the following reason. Given Algorithm 1 with a certain mapping $D$, consider Algorithm 1 with a different mapping $D^{\prime}(P)$ : if $\left|P \cap A_{m}\right|=0$, then $D^{\prime}(P)=D(P)$; otherwise $D^{\prime}(P)$ assigns probability mass 1 to some element $x$ of $P$ that is in $A_{m}$, e.g., to the first one among such elements. Note that $D^{\prime}$ meets conditions (G1) and (G2). Moreover, (G2) holds for $j=m-1$. For the sequence of populations $P_{0}^{\prime}, P_{1}^{\prime}, \ldots$ of Algorithm 1 with mapping $D^{\prime}$, we can put $T^{\prime}:=\lambda \cdot \min \left\{t \mid\left|P_{t}^{\prime} \cap A_{m}\right|>0\right\}$. Executions of the original algorithm and the modified one before generation $T^{\prime} / \lambda$ are identical. On generation $T^{\prime} / \lambda$ both algorithms place elements of $A_{m}$ into the population for the first time. Thus, $T^{\prime}$ and $T$ are equal in every realization and their expectations are equal.

For any level $j \in[m]$ and time $t \geq 0$, let the random variable $X_{t}^{(j)}:=\left|P_{t} \cap A_{\geq j}\right|$ denote the number of individuals in levels $A_{\geq j}$ at time $t$. Because $A_{\geq j}$ is partitioned into disjoint sets $A_{j}$ and $A_{\geq j+1}$, the definition implies

$$
\left|P_{t} \cap A_{j}\right|=X_{t}^{(j)}-X_{t}^{(j+1)}
$$

Algorithm 1 samples all individuals in generation $t+1$ independently from distribution $D\left(P_{t}\right)$. Therefore, given the current population $P_{t}, X_{t+1}^{(j)}$ is binomially distributed $X_{t+1}^{(j)} \sim$ $\operatorname{Bin}\left(\lambda, p_{t+1}^{(j)}\right)$, where $p_{t+1}^{(j)}:=\operatorname{Pr}_{t, \gamma \sim D\left(P_{t}\right)}\left(y \in A_{\geq j}\right)$ is the probability of sampling an individual in level $j$ or higher.

The current level $Y_{t}$ of the population at time $t$ is defined as $Y_{t}:=\max \left\{j \in[m] \mid X_{t}^{(j)} \geq \gamma_{0} \lambda\right\}$. Note that $\left(X_{t}^{(j)}\right)_{t \in \mathbb{N}}$ and $\left(Y_{t}\right)_{t \in \mathbb{N}}$ are adapted to the filtration $\left(\mathscr{F}_{t}\right)_{t \in \mathbb{N}}$ because they are defined in terms of the population process $\left(P_{t}\right)_{t \in \mathbb{N}}$.

When $Y_{t}<m$, there exists a unique $\gamma<\gamma_{0}$ such that

$$
\begin{aligned}
X_{t}^{\left(Y_{t}+1\right)} & =\left|P_{t} \cap A_{\geq Y_{t}+1}\right|=\gamma \lambda \\
X_{t}^{\left(Y_{t}\right)} & =\left|P_{t} \cap A_{\geq Y_{t}}\right| \geq \gamma_{0} \lambda \text { and } \\
X_{t}^{\left(Y_{t}-1\right)} & =\left|P_{t} \cap A_{\geq Y_{t}-1}\right| \geq \gamma_{0} \lambda
\end{aligned}
$$

In the case of $X_{t}^{\left(Y_{t}+1\right)}=0$, it follows from (1)-(3) that $\left|P \cap A_{j}\right|=X_{t}^{\left(Y_{t}\right)} \geq \gamma_{0} \lambda$. Condition (G1) for level $j=Y_{t}$ then gives

$$
p_{t+1}^{\left(Y_{t}+1\right)}=\operatorname{Pr}_{y \sim D\left(P_{t}\right)}\left(y \in A_{\geq Y_{t}+1}\right) \geq z_{Y_{t}}
$$

Otherwise if $X_{t}^{\left(Y_{t}+1\right)} \geq 1$, conditions (G1) and (G2) for level $j=Y_{t}$ with (2) and (3) imply

$$
\begin{aligned}
p_{t+1}^{\left(Y_{t}+1\right)} & =\operatorname{Pr}_{y \sim D\left(P_{t}\right)}\left(y \in A_{\geq Y_{t}+1}\right) \\
& \geq \max \left\{(1+\delta) \frac{X_{t}^{\left(Y_{t}+1\right)}}{\lambda}, z_{j}\right\}
\end{aligned}
$$

Condition (G2) for level $j=Y_{t}-1$ with (3) and (4) give

$$
p_{t+1}^{\left(Y_{t}\right)}=\operatorname{Pr}_{y \sim D\left(P_{t}\right)}\left(y \in A_{\geq Y_{t}}\right) \geq(1+\delta) \gamma_{0}
$$

We now define the process $\left(Z_{t}\right)_{t \in \mathbb{N}}$ as $Z_{t}:=0$ if $Y_{t}=m$, and otherwise, if $Y_{t}<m$, we let $Z_{t}:=g\left(X_{t}^{\left(Y_{t}+1\right)}, Y_{t}\right)$, where for all $k$, and for all $1 \leq j<m, g(k, j)=g_{1}(k, j)+g_{2}(k, j)$ and

$$
\begin{aligned}
g_{1}(k, j):= & \ln \left(\frac{1+(\delta / 2) \lambda}{1+(\delta / 2) \max \left\{k, z_{j} \lambda /(1+\delta)\right\}}\right) \\
& +\sum_{i=j+1}^{m-1} \ln \left(\frac{1+(\delta / 2) \lambda}{1+(\delta / 2) \lambda z_{i} /(1+\delta)}\right) \\
g_{2}(k, j):= & \frac{1}{q_{j}}\left(1-\frac{\delta^{2}}{7}\right)^{k}+\sum_{i=j+1}^{m-1} \frac{1}{q_{i}}
\end{aligned}
$$

where $q_{j}:=1-\left(1-z_{j}\right)^{\lambda}$.
It follows from Lemma 5 that $g(k, j)$ is a level function. Furthermore, $g(k, j) \geq 0$ for all $k \in[0] \cup[\lambda]$ and all $j \in[m]$. Due to properties 1 and 2 of level functions, and [14, Lemma 31], the distance is always bounded from above by

$$
\begin{aligned}
g(0,1) & \leq \sum_{i=1}^{m-1}\left(\ln \left(\frac{1+(\delta / 2) \lambda}{1+(\delta / 2) z_{i} \lambda /(1+\delta)}\right)+\frac{1}{q_{i}}\right) \\
& <\sum_{i=1}^{m-1}\left(\ln \left(\frac{4+2 \delta \lambda}{4+\delta z_{i} \lambda}\right)+1+\frac{1}{\lambda z_{i}}\right)
\end{aligned}
$$

Using that $z_{i} \leq 1$, this can be bounded further by

$$
\begin{aligned}
& <\sum_{i=1}^{m-1}\left(\ln \left(\frac{4+2 \delta \lambda}{z_{i}(4+\delta \lambda)}\right)+1+\frac{1}{\lambda z_{i}}\right) \\
& =\sum_{i=1}^{m-1}\left(\ln \left(\frac{1}{z_{i}}\left(1+\frac{\delta \lambda}{4+\delta \lambda}\right)\right)+1+\frac{1}{\lambda z_{i}}\right)
\end{aligned}
$$

We then exploit that $\ln (x) \leq x-1$ for all $x>0$ so

$$
<\sum_{i=1}^{m-1}\left(\frac{2}{z_{i}}+\frac{1}{\lambda z_{i}}\right)
$$

Finally, since $z_{i} \geq z_{*}$ and $\lambda \geq\lceil 4 \ln (128)\rceil=20$ by (G3)

$$
<\frac{m}{z_{*}}\left(2+\frac{1}{\lambda}\right) \leq \frac{41 m}{20 z_{*}}
$$

Hence, we have $0 \leq Z_{t}<g(0,1)<\infty$ for all $t \in \mathbb{N}$ which implies that condition 2 of the drift theorem is satisfied.

The drift of the process at time $t$ is $E_{t}\left[\Delta_{t+1}\right]$, where

$$
\Delta_{t+1}:=g\left(X_{t}^{\left(Y_{t}+1\right)}, Y_{t}\right)-g\left(X_{t+1}^{\left(Y_{t+1}+1\right)}, Y_{t+1}\right)
$$

We bound the drift by the law of total probability as

$$
\begin{aligned}
E_{t}\left[\Delta_{t+1}\right]= & \left(1-\operatorname{Pr}_{t}\left(Y_{t+1}<Y_{t}\right)\right) E_{t}\left[\Delta_{t+1} \mid Y_{t+1} \geq Y_{t}\right] \\
& +\operatorname{Pr}_{t}\left(Y_{t+1}<Y_{t}\right) E_{t}\left[\Delta_{t+1} \mid Y_{t+1}<Y_{t}\right]
\end{aligned}
$$

The event $Y_{t+1}<Y_{t}$ holds if and only if $X_{t+1}^{\left(Y_{t}\right)}<\gamma_{0} \lambda$. Due to (8), we obtain the following by a Chernoff bound

$$
\begin{aligned}
\operatorname{Pr}_{t}\left(Y_{t+1}<Y_{t}\right) & =\operatorname{Pr}_{t}\left(X_{t+1}^{\left(Y_{t}\right)}<\left(1-\frac{\delta}{1+\delta}\right)(1+\delta) \gamma_{0} \lambda\right) \\
& \leq \exp \left(-\frac{\delta^{2} \gamma_{0} \lambda}{2(1+\delta)}\right) \leq \frac{\delta^{2} z_{*}}{128 m}
\end{aligned}
$$

where the last inequality takes into account the population size required by condition (G3). Given the low probability of the event $Y_{t+1}<Y_{t}$, it suffices to use the pessimistic bound (11)

$$
E_{t}\left[\Delta_{t+1} \mid Y_{t+1}<Y_{t}\right] \geq-g(0,1) \geq-\frac{41 m}{20 z_{*}}
$$

If $Y_{t+1} \geq Y_{t}$, we can apply Lemma 1

$$
\begin{aligned}
& E_{t}\left[\Delta_{t+1} \mid Y_{t+1} \geq Y_{t}\right] \\
& \quad \geq E_{t}\left[g\left(X_{t}^{\left(Y_{t}+1\right)}, Y_{t}\right)-g\left(X_{t+1}^{\left(Y_{t}+1\right)}, Y_{t}\right) \mid Y_{t+1} \geq Y_{t}\right]
\end{aligned}
$$

Note that event $Y_{t+1} \geq Y_{t}$ is equivalent to having $X_{t+1}^{\left(Y_{t}\right)} \geq$ $\gamma_{0} \lambda$, then due to Lemma 7 , in the following we can skip the condition on the event when needed.

If $X_{t}^{\left(Y_{t}+1\right)}=0$, then $X_{t}^{\left(Y_{t}+1\right)} \leq X_{t+1}^{\left(Y_{t}+1\right)}$ and

$$
E_{t}\left[g_{1}\left(X_{t}^{\left(Y_{t}+1\right)}, Y_{t}\right)-g_{1}\left(X_{t+1}^{\left(Y_{t}+1\right)}, Y_{t}\right) \mid Y_{t+1} \geq Y_{t}\right] \geq 0
$$

because the function $g_{1}$ satisfies property 2 in Definition 1. Furthermore, we have the lower bound

$$
\begin{aligned}
& E_{t}\left[g_{2}\left(X_{t}^{\left(Y_{t}+1\right)}, Y_{t}\right)-g_{2}\left(X_{t+1}^{\left(Y_{t}+1\right)}, Y_{t}\right) \mid Y_{t+1} \geq Y_{t}\right] \\
& \quad>\operatorname{Pr}_{t}\left(X_{t+1}^{\left(Y_{t}+1\right)} \geq 1\right)\left(g_{2}\left(0, Y_{t}\right)-g_{2}\left(1, Y_{t}\right)\right) \geq \frac{\delta^{2}}{7}
\end{aligned}
$$

where the last inequality follows because of (5) and $\operatorname{Pr}_{t}\left(X_{t+1}^{(Y_{t+1})} \geq 1\right) \geq 1-\left(1-p_{t+1}^{(Y_{t+1})}\right)^{\lambda} \geq 1-\left(1-z_{Y_{t}}\right)^{\lambda}=q_{Y_{t}}$, and $g_{2}\left(0, Y_{t}\right)-g_{2}\left(1, Y_{t}\right)=\left(1 / q_{Y_{t}}\right)\left(\delta^{2} / 7\right)$.

In the other case, where $X_{t}^{\left(Y_{t+1}\right)} \geq 1$, we obtain

$$
\begin{aligned}
E_{t}[ & g_{1}\left(X_{t}^{\left(Y_{t+1}\right)}, Y_{t}\right)-g_{1}\left(X_{t+1}^{\left(Y_{t+1}\right)}, Y_{t}\right) \mid Y_{t+1} \geq Y_{t}] \\
& \geq E_{t}\left[\ln \left(\frac{1+\frac{\delta}{2} X_{t+1}^{\left(Y_{t+1}\right)}}{1+\frac{\delta}{2} \max \left\{X_{t}^{\left(Y_{t+1}\right)}, \frac{z_{Y_{t}} \lambda}{1+\delta}\right\}}\right)\right] \geq \frac{\delta^{2}}{7}
\end{aligned}
$$

where the last inequality follows from Lemma 6 for the parameters $X:=X_{t+1}^{(Y_{t+1})}$ and $p:=p_{t+1}^{\left(Y_{t+1}\right)}$ as given by (7). For the function $g_{2}$, we get

$$
\begin{aligned}
& E_{t}\left[g_{2}\left(X_{t}^{\left(Y_{t+1}\right)}, Y_{t}\right)-g_{2}\left(X_{t+1}^{\left(Y_{t+1}\right)}, Y_{t}\right) \mid Y_{t+1} \geq Y_{t}\right]= \\
& \quad \frac{1}{q_{Y_{t}}}\left(\left(1-\frac{\delta^{2}}{7}\right)^{X_{t}^{\left(Y_{t}\right)}}-E_{t}\left[\left(1-\frac{\delta^{2}}{7}\right)^{X_{t+1}^{\left(Y_{t+1}\right)}}\right]\right)>0
\end{aligned}
$$

where the last inequality is due to [14, Lemma 6] (see also the supplementary materials), applied to $X_{t+1}^{\left(Y_{t+1}\right)} \sim \operatorname{Bin}\left(\lambda, p_{t+1}^{\left(Y_{t+1}\right)}\right)$ with $p_{t+1}^{\left(Y_{t+1}\right)} \geq(1+\delta) X_{t}^{\left(Y_{t+1}\right)} / \lambda$ [see (7)] and the parameter $\kappa=-\ln \left(1-\delta^{2} / 7\right)<\delta$.

Taking into account all cases, we have

$$
E_{t}\left[\Delta_{t+1} \mid Y_{t+1} \geq Y_{t}\right] \geq \frac{\delta^{2}}{7}
$$

We now have bounds for all the quantities in (12) with (13)-(15), and we get

$$
\begin{aligned}
E_{t}\left[\Delta_{t+1}\right]= & \left(1-\operatorname{Pr}_{t}\left(Y_{t+1}<Y_{t}\right)\right) E_{t}\left[\Delta_{t+1} \mid Y_{t+1} \geq Y_{t}\right] \\
& +\operatorname{Pr}_{t}\left(Y_{t+1}<Y_{t}\right) E_{t}\left[\Delta_{t+1} \mid Y_{t+1}<Y_{t}\right] \\
\geq & \left(1-\frac{\delta^{2} z_{*}}{128 m}\right) \frac{\delta^{2}}{7}-\left(\frac{\delta^{2} z_{*}}{128 m}\right)\left(\frac{41 m}{20 z_{*}}\right)>\frac{\delta^{2}}{8}
\end{aligned}
$$

We now verify condition 3 of Theorem 2, i.e., that $T$ has finite expectation. Let $p_{*}:=\min \left\{(1+\delta) / \lambda, z_{*}\right\}$, and note by conditions (G1) and (G2) that the current level increases by at least one with probability $\operatorname{Pr}_{t}\left(Y_{t+1}>Y_{t}\right) \geq\left(p_{*}\right)^{\gamma_{0} \lambda}$. Due to the definition of the modified process $D^{\prime}$, if $Y_{t}=m$, then $Y_{t+1}=m$. Hence, the probability of reaching $Y_{t}=m$ is lower bounded by the probability of the event that the current level increases in all of at most $m$ consecutive generations, i.e., $\operatorname{Pr}_{t}\left(Y_{t+m}=m\right) \geq\left(p_{*}\right)^{\gamma_{0} \lambda m}>0$. It follows that $E[T]<\infty$.

By Theorem 2 and the upper bound on $g(0,1)$ in (9)

$$
E[T] \leq \lambda \cdot \frac{g(0,1)}{\delta^{2} / 8}<\left(\frac{8 \lambda}{\delta^{2}}\right) \sum_{i=1}^{m-1} \ln \left(\frac{4+2 \delta \lambda}{4+z_{i} \delta \lambda}\right)+1+\frac{1}{\lambda z_{i}}
$$

then using that $4 \leq \delta \lambda / 5$ from (G3) and $(1 / 5+2) e<6$

$$
<\left(\frac{8 \lambda}{\delta^{2}}\right) \sum_{i=1}^{m-1}\left(\ln \left(\frac{6 \delta \lambda}{4+z_{i} \delta \lambda}\right)+\frac{1}{\lambda z_{i}}\right)
$$

It can be seen from the proof of Theorem 1 that it easily extends to algorithms where the mapping $D$ is time-dependent, provided that (G1), (G2), and (G3) hold for any $t$ for some fixed (time independent) values $z_{1}, \ldots, z_{m-1}, \delta$, and $\gamma_{0}$.

## III. Tools for Analyzing Genetic Algorithms

We now derive two corollaries of Theorem 1 tailored to Algorithm 2 and give conditions on tunable parameters of selection mechanisms making the corollaries applicable.

A fitness function is not defined explicitly in Algorithm 2, so no assumptions on an $f$-based partition will be needed in the corollaries. Here, we generalize the cumulative selection probability of select, denoted $\beta(\gamma, P)$, which was defined relative to the fitness function $f$ in [14], to the one that is relative to the partition $\left(A_{1}, \ldots, A_{m}\right)$. To define $\beta(\gamma, P)$ of select with respect to $f$ for a population $P$ of $\lambda$ search points, we first assume $\left(f_{1}, \ldots, f_{\lambda}\right)$ to be the vector of sorted fitness values of $P$, i.e., $f_{i} \geq f_{i+1}$ for each $i \in[\lambda-1]$. Then

$$
\beta(\gamma, P):=\sum_{i=1}^{\lambda} p_{\mathrm{sel}}(i \mid P) \cdot\left[f(P(i)) \geq f_{\mid \gamma \lambda \uparrow}\right]
$$

for any $\gamma \in(0,1]$. Here and below, $[\cdot]$ is the Iverson bracket.
Similarly, given a partition $\left(A_{1}, \ldots, A_{m}\right)$, if we use $\left(\ell_{1}, \ldots, \ell_{\lambda}\right)$ to denote the sorted levels of search points in $P$, i.e., $\ell_{i} \geq \ell_{i+1}$ for each $i \in[\lambda-1]$, then the cumulative selection probability of select with respect to $\left(A_{1}, \ldots, A_{m}\right)$ is

$$
\zeta(\gamma, P):=\sum_{i=1}^{\lambda} p_{\mathrm{sel}}(i \mid P) \cdot\left[P(i) \in A_{\geq \ell_{\mid \gamma \lambda \uparrow}}\right]
$$

These definitions are related by the following lemma.
Lemma 2: For any $f$-based partition of $\mathcal{X}$ and $\lambda \in \mathbb{N}$

$$
\forall P \in \mathcal{X}^{\lambda}, \forall \gamma \in(0,1] \quad \zeta(\gamma, P) \geq \beta(\gamma, P)
$$

## A. Analysis of Nonpermanent Use of Crossover

We first derive from Theorem 1 a corollary that is adapted to Algorithm 2 with $p_{\mathrm{c}}<1$. This setting covers the case $p_{\mathrm{c}}=0$, i.e., only unary variation operators are used. This specific case is the main subject of [14]. As we will see later on, stronger and more general results can be claimed with the corollary.

Corollary 2: Given a partition $\left(A_{1}, \ldots, A_{m}\right)$ of $\mathcal{X}$, define $T:=\min \left\{t \lambda \mid\left|P \cap A_{m}\right|>0\right\}$ where for all $t \in \mathbb{N}, P_{t} \in \mathcal{X}^{\lambda}$ is the population of Algorithm 2 in generation $t$. If $p_{\mathrm{c}}<1$ and there exist $s_{1}, \ldots, s_{m-1}, s_{*}, p_{0}, \delta \in(0,1]$, and a constant $\gamma_{0} \in(0,1)$ such that for any population $P \in \mathcal{X}^{\lambda}$
(M1): for each level $j \in[m-1]$

$$
p_{\mathrm{mut}}\left(y \in A_{\geq j+1} \mid x \in A_{j}\right) \geq s_{j}
$$

(M2): for each level $j \in[m-1]$

$$
p_{\mathrm{mut}}\left(y \in A_{\geq j} \mid x \in A_{j}\right) \geq p_{0}
$$

(M3): for any population $P \in\left(\mathcal{X} \backslash A_{m}\right)^{\lambda}$ and $\gamma \in\left(0, \gamma_{0}\right]$

$$
\zeta(\gamma, P) \geq \frac{(1+\delta) \gamma}{p_{0}\left(1-p_{\mathrm{c}}\right)}
$$

(M4): the population size $\lambda$ satisfies

$$
\lambda \geq\left(\frac{4}{\gamma_{0} \delta^{2}}\right) \ln \left(\frac{128 m}{p_{0} s_{*} \delta^{2}}\right) \text { where } s_{*}:=\min _{j \in[m-1]}\left\{s_{j}\right\}
$$

then

$$
E[T]<\left(\frac{8}{\delta^{2}}\right) \sum_{j=1}^{m-1}\left(\lambda \ln \left(\frac{6 \delta \lambda}{4+\gamma_{0} s_{j} \delta \lambda}\right)+\frac{1}{\gamma_{0} s_{j}}\right)
$$

Proof: We apply Theorem 1 following the guidelines.
Step 1: It is skipped because we already have the partition.
Step 2: Assume that $\left|P \cap A_{\geq j}\right| \geq \gamma_{0} \lambda$ and $\left|P \cap A_{\geq j+1}\right| \geq$ $\gamma \lambda>0$ for some $\gamma \leq \gamma_{0}$. To create an individual in $A_{\geq j+1}$, it suffices to pick an $x \in\left|P \cap A_{k}\right|$ for any $k \geq j+1$ and mutate it to an individual in $A_{\geq k}$, the probability of such an event, according to (M2) and (M3), is at least $\left(1-p_{\mathrm{c}}\right) \zeta(\gamma, P) p_{0} \geq(1+\delta) \gamma$. So (G2) holds with $p_{0}, \delta$ and $\gamma_{0}$ from (M3).
Step 3: We are given $\left|P \cap A_{j}\right| \geq \gamma_{0} \lambda$. Thus, with probability $\zeta\left(\gamma_{0}, P\right)$, the selection mechanism chooses an individual $x$ in either $A_{j}$ or $A_{\geq j+1}$. If $x \in A_{j}$, then the mutation operator will by (M1) upgrade $x$ to $A_{\geq j+1}$ with probability $s_{j}$. If $x \in A_{\geq j+1}$, then by (M2), the mutation operator leaves the individual in $A_{\geq j+1}$ with probability $p_{0}$. Finally, no crossover occurs with probability $1-p_{c}$, so the probability of producing an individual in $A_{\geq j+1}$ is at least (1 $p_{\mathrm{c}} \zeta\left(\gamma_{0}, P\right) \min \left\{s_{j}, p_{0}\right\} \geq\left(1-p_{\mathrm{c}}\right) \zeta\left(\gamma_{0}, P\right) s_{j} p_{0}>$ $\gamma_{0} s_{j}$ and (G1) holds with $z_{j}=\gamma_{0} s_{j}, z_{*}=\gamma_{0} s_{*}$.
Step 4: Given $z_{*}=\gamma_{0} s_{*}$, condition (M4) yields (G3).
Step 5: Conditions (G1)-(G3) are satisfied and Theorem 1 gives

$$
\begin{aligned}
E[T] & \leq \frac{8 \lambda}{\delta^{2}} \sum_{j=1}^{m-1}\left(\ln \left(\frac{6 \delta \lambda}{4+z_{j} \delta \lambda}\right)+\frac{1}{z_{j} \lambda}\right) \\
& =\frac{8}{\delta^{2}} \sum_{j=1}^{m-1}\left(\lambda \ln \left(\frac{6 \delta \lambda}{4+\gamma_{0} s_{j} \delta \lambda}\right)+\frac{1}{\gamma_{0} s_{j}}\right)
\end{aligned}
$$

The proof implies that any operator can stand for crossover in line 4 of Algorithm 2, and the result will still hold.

## B. Analysis of Permanent Use of Crossover

We now adapt Theorem 1 to Algorithm 2 with $p_{\mathrm{c}}=1$.
Corollary 3: Given a partition $\left(A_{1}, \ldots, A_{m}\right)$ of $\mathcal{X}$, define $T:=\min \left\{t \lambda \mid \mid P_{t} \cap A_{m} \mid>0\right\}$, where for all $t \in \mathbb{N}, P_{t} \in \mathcal{X}^{\lambda}$ is the population of Algorithm 2. If $p_{\mathrm{c}}=1$ and there exist $s_{1}, \ldots, s_{m-1}, s_{*}, p_{0}, \varepsilon, \delta \in(0,1]$, and a constant $\gamma_{0} \in(0,1)$ such that
(C1): for each level $j \in[m-1]$

$$
p_{\mathrm{mut}}\left(y \in A_{\geq j+1} \mid x \in A_{j}\right) \geq s_{j}
$$

(C2): for each level $j \in[m]$

$$
p_{\mathrm{mut}}\left(y \in A_{\geq j} \mid x \in A_{j}\right) \geq p_{0}
$$

(C3): for each level $j \in[m-2]$

$$
p_{\mathrm{xor}}\left(x \in A_{\geq j+1} \mid u \in A_{\geq j}, v \in A_{\geq j+1}\right) \geq \varepsilon
$$

(C4): for any population $P \in\left(\mathcal{X} \backslash A_{m}\right)^{\lambda}$ and $\gamma \in\left(0, \gamma_{0}\right]$

$$
\zeta(\gamma, P) \geq \gamma \sqrt{\frac{1+\delta}{p_{0} \gamma_{0} \varepsilon}}
$$

(C5): the population size satisfies

$$
\lambda \geq\left(\frac{4}{\gamma_{0} \delta^{2}}\right) \ln \left(\frac{128 m}{\gamma_{0} \delta^{2} s_{*}}\right), \text { wheres } s_{*}:=\min _{j \in[m-1]}\left\{s_{j}\right\}
$$

then

$$
E[T]<\left(\frac{8}{\delta^{2}}\right) \sum_{j=1}^{m-1}\left(\lambda \ln \left(\frac{6 \delta \lambda}{4+\gamma_{0} s_{j} \delta \lambda}\right)+\frac{1}{\gamma_{0} s_{j}}\right)
$$

Proof: We apply Theorem 1 following the guidelines.
Step 1: It is skipped because the partition is already defined.
Step 2: We are given $\left|P \cap A_{\geq j}\right| \geq \gamma_{0} \lambda$ and $\left|P \cap A_{\geq j+1}\right| \geq$ $\gamma \lambda>0$. To create an individual in $A_{\geq j+1}$, it suffices to pick the individual $u$ in $A_{\geq j}$ and $v$ in $A_{\geq j+1}$, then to produce an individual in $A_{k}$ for any $k \geq j+1$ by crossover and not destroy the produced individual by mutation. The probability of such an event according to (C2), (C3), and (C4) is bounded from below by $\zeta\left(\gamma_{0}, P\right) \zeta(\gamma, P) \varepsilon p_{0} \geq(1+\delta) \gamma$. Condition (G2) is then satisfied with the same $\gamma_{0}$ and $\delta$ as in (C4).
Step 3: We assume $\left|P \cap A_{j}\right| \geq \gamma_{0} \lambda$. Note that condition (C3) written for level $j-1$ is $p_{\text {xor }}\left(x \in A_{\geq j} \mid u \in\right.$ $\left.A_{\geq j-1}, v \in A_{\geq j}\right) \geq \varepsilon$, and because $A_{\geq j} \subset A_{\geq j-1}$ then $p_{\text {xor }}\left(x \in A_{\geq j} \mid u \in A_{\geq j}, v \in A_{\geq j}\right) \geq \varepsilon$. To create an individual in levels $A_{\geq j+1}$, it then suffices to pick both parents $u$ and $v$ from levels $A_{\geq j}$ in line 3 , produce an intermediary offspring in $A_{k}$ for any $k \geq j$ via crossover, and from this an individual in $A_{\geq j+1}$ via mutation. If $k=j$, we need to improve the produced individual by mutation, relying on (C1). Otherwise if $k>j$ it suffices not to destroy the produced individual by mutation, relying on (C2). It follows from (C4) that the probability of producing an individual in $A_{\geq j+1}$ is at least $\zeta\left(\gamma_{0}, P\right)^{2} \varepsilon \min \left\{s_{j}, p_{0}\right\} \geq \zeta\left(\gamma_{0}, P\right)^{2} \varepsilon s_{j} p_{0}>\gamma_{0} s_{j}$. Condition (G1) then holds for $z_{j}=\gamma_{0} s_{j}$ and $z_{*}=\gamma_{0} s_{*}$.
Step 4: Given that $z_{*}=\gamma_{0} s_{*}$, (C5) implies (G3).
Step 5: Conditions (G1-3) are satisfied, so Theorem 1 gives

$$
E[T] \leq \frac{8}{\delta^{2}} \sum_{j=1}^{m-1}\left(\lambda \ln \left(\frac{6 \delta \lambda}{4+\gamma_{0} s_{j} \delta \lambda}\right)+\frac{1}{\gamma_{0} s_{j}}\right)
$$

Corollary 3 is similar to Corollary 2, except that condition (C2) has to additionally hold for level $A_{m}$, that (C3) is a new condition on the crossover operator, and that condition (C4) on the select operator differs from (M3).

## C. Analysis of Selection Mechanisms

We show how to parameterize the following selection mechanisms such that condition (M3) of Corollary 2 and (C4) of Corollary 3 are satisfied. In $k$-tournament selection, $k$ individuals are sampled uniformly at random with replacement from the population, and the fittest of these individuals is returned. In $(\mu, \lambda)$-selection, parents are sampled uniformly at random among the fittest $\mu$ individuals in the population. A function $\alpha: \mathbb{R} \rightarrow \mathbb{R}$ is a ranking function [26] if $\alpha(x) \geq 0$ for all $x \in[0,1]$, and $\int_{0}^{1} \alpha(x) d x=1$. In ranking selection with ranking function $\alpha$, the probability of selecting an individual among $\gamma \lambda$ best individuals is $\int_{0}^{1} \alpha(x) d x$.

In linear ranking selection, parameterized by $\eta \in(1,2]$, the ranking function is $\alpha(\gamma):=\eta(1-2 \gamma)+2 \gamma$. We define exponential ranking selection parameterized by $\eta>0$ with $\alpha(\gamma):=\eta e^{\eta(1-\gamma)} /\left(e^{\eta}-1\right)$.

Lemma 3: Assuming that $\left(A_{1}, \ldots, A_{m}\right)$ is a partition of $\mathcal{X}$ with $\left(A_{1}, \ldots, A_{m-1}\right)$ being an $f$-based partition of $\mathcal{X} \backslash A_{m}$, for any constants $\delta^{\prime}>0, p_{0} \in(0,1), \varepsilon \in(0,1)$, and for any non-negative parameter $p_{\mathrm{c}}=1-\Omega(1)$, there exists a constant $\gamma_{0} \in(0,1)$ such that all the following selection mechanisms:

1) $k$-tournament selection;
2) $(\mu, \lambda)$-selection;
3) linear ranking selection;
4) exponential ranking selection
with their parameters $k, \lambda / \mu$, and $\eta$ being set to no less than

$$
\frac{1+\delta^{\prime}}{\left(1-p_{\mathrm{c}}\right) p_{0}}
$$

satisfy (M3), that is

$$
\zeta(\gamma, P) \geq \frac{\left(1+\delta^{\prime \prime}\right) \gamma}{p_{0}\left(1-p_{\mathrm{c}}\right)}
$$

for any $\gamma \in\left(0, \gamma_{0}\right]$, any $P \in\left(\mathcal{X} \backslash A_{m}\right)^{\lambda}$, and some constant $\delta^{\prime \prime}>0$.

Lemma 4: Given a partition $\left(A_{1}, \ldots, A_{m}\right)$ of $\mathcal{X}$ with $\left(A_{1}, \ldots, A_{m-1}\right)$ being an $f$-based partition of $\mathcal{X} \backslash A_{m}$, for any constants $\delta^{\prime}>0, p_{0} \in(0,1)$, and $\varepsilon \in(0,1)$, there exists a constant $\gamma_{0} \in(0,1)$ such that the following selection mechanisms:

1) $k$-tournament selection with $k \geq 4\left(1+\delta^{\prime}\right) /\left(\varepsilon p_{0}\right)$;
2) $(\mu, \lambda)$-selection with $\lambda / \mu \geq\left(1+\delta^{\prime}\right) /\left(\varepsilon p_{0}\right)$;
3) exponential ranking selection with $\eta \geq 4\left(1+\delta^{\prime}\right) /\left(\varepsilon p_{0}\right)$ satisfy (C4), that is

$$
\zeta(\gamma, P) \geq \gamma \sqrt{\frac{1+\delta^{\prime}}{p_{0} \varepsilon \gamma_{0}}}
$$

for any $\gamma \in\left(0, \gamma_{0}\right]$, and any $P \in\left(\mathcal{X} \backslash A_{m}\right)^{\lambda}$.
Lemmas 3 and 4 are proved in the supplementary materials.

## IV. APPLICATIONS TO GENETIC ALGORITHMS

We now apply the results from Section III. Proofs have been moved to the supplementary materials due to space limitations. Given a bitstring $x$ a bitwse mutation operator, returns a bitstring $y$, where for each $i \in[n]$, bit $y_{i}$, is set independently to $1-x_{i}$ with probability $p_{\mathrm{m}}$ and is otherwise kept equal to $x_{i}$. The parameter $p_{\mathrm{m}} \in[0,1]$ is called the mutation rate.

## A. Optimization of Pseudo-Boolean Functions

In this section, we consider the expected runtime of nonelitist GAs in Algorithm 2 on the following functions: ONEMAX $(x):=\sum_{i=1}^{n} x_{i}=\left|x\right|_{1}=\operatorname{OM}(x)$, LEADINGONES $(x):=\sum_{i=1}^{n} \prod_{j=1}^{i} x_{i}=\operatorname{LO}(x)$

$$
\operatorname{JUMP}_{r}(x):= \begin{cases}n+1 & \text { if }\left|x\right|_{1}=n \\ r+\left|x\right|_{1} & \text { if }\left|x\right|_{1} \leq n-r \\ n-\left|x\right|_{1} & \text { otherwise }\end{cases}
$$

$\operatorname{ROYALROAD}_{r}(x):=\sum_{i=0}^{n / r-1} \prod_{j=1}^{r} x_{i r+j}, \operatorname{Linear}(x):=$ $\sum_{i=1}^{n} c_{i} x_{i}$, where each $c_{i} \in \mathbb{R}$. For LINEAR, w.l.o.g. we can
assume $c_{1} \geq \cdots \geq c_{n}>0$ [14]. We also consider the class of $\ell$-UNIMODAL functions, where each function has exactly $\ell$ distinctive fitness values $f_{1}<\cdots<f_{\ell}$, and each bitstring $x$ of the search space is either optimal or it has a Hamming-neighbor $y$ with $f(y)>f(x)$.

Several results about the runtime of EAs with parent or offspring population size greater than one can be found in the literature. For the illustrative purpose, we cite just some of results. In [48], it is shown that $(1, \lambda)$ EA on ONEMAX has the runtime $\mathcal{O}(n \log n+n \lambda)$, provided that $\lambda \geq \log _{(e / e-1)} n$, and on the $\ell$-UNIMODAL functions this algorithm has the runtime $O(\ell n+\ell \lambda)$, given that $\lambda \geq \log _{(e / e-1)}(\ell n)$. A nonelitist GA using bitwise mutation and tournament selection with $k=\Omega(\lambda)$ and $\lambda=\Omega(n \log n)$ has runtime $\mathcal{O}(n \lambda)$ on LeAdingones [22]. The $(1+\lambda)$ EA on any linear function has runtime $O(n \log n+n \lambda)$, see [18]. A $(\mu+$ 1) GA where the uniform crossover is applied with probability $p_{c}=\mathcal{O}(1 /(n r))$ and $\mu$ is chosen appropriately is shown to have $\mathcal{O}\left(\mu n^{2} r^{3}+4^{r} / p_{c}\right)$ runtime on $\mathrm{JUMP}_{r}$ function [31]. The case of $p_{c}=1$ is treated in [10].

Our results presented below apply only to nonelitist GAs with bitwise mutation. For a moderate use of crossover, i.e., $p_{\mathrm{c}}=1-\Omega(1)$, Corollary 2 and Lemma 3 yield the following.

Theorem 3: The expected runtime of the GA in Algorithm 2, with $p_{\mathrm{c}}=1-\Omega(1)$, using any crossover operator, a bitwise mutation with mutation rate $\chi / n$ for any fixed constant $\chi>0$ and one of the selection mechanisms: $k$-tournament selection, $(\mu, \lambda)$-selection, linear or exponential ranking selection, with their parameters $k, \lambda / \mu$, and $\eta$ being set to no less than $(1+\delta) e^{\chi} /\left(1-p_{\mathrm{c}}\right)$, where $\delta \in(0,1]$ being any constant, is:

1) $\mathcal{O}(n \lambda)$ on ONEMAX if $\lambda \geq c \ln n$
2) $\mathcal{O}\left(n^{2}+n \lambda \ln \lambda\right)$ on LEADINGONES if $\lambda \geq c \ln n$;
3) $\mathcal{O}(n \ell+\ell \lambda \ln \lambda)$ on $\ell$-UNIMODAL if $\lambda \geq c \ln (\ell n)$;
4) $\mathcal{O}\left(n^{2}+n \lambda \ln \lambda\right)$ on LINEAR if $\lambda \geq c \ln n$;
5) $\mathcal{O}\left((n / \chi)^{r}+n \lambda+\lambda \ln \lambda\right)$ on $\mathrm{JUMP}_{r}$ if $\lambda \geq c r \ln n$;
6) $\mathcal{O}\left((n / \chi)^{r} \ln (n / r)+[(n \lambda \ln \lambda) / r]\right)$ on ROYALROAD $_{r \geq 2}$ if $\lambda \geq c r \ln n$
for some sufficiently large constant $c$.
The proof is in the supplementary materials.
In the case of regular use of crossover, i.e., $p_{\mathrm{c}}=1$, we limit our consideration to mask-based crossovers. Given two parent genotypes $u$ and $v$, such operator consists in first choosing (deterministically or randomly) a binary string $\tilde{m}=$ $\left(m_{1}, \ldots, m_{n}\right)$ to produce two offspring vectors $x^{\prime}, x^{\prime \prime}$ as

$$
x_{i}^{\prime}= \begin{cases}u_{i}, & \text { if } m_{i}=1 \\ v_{i}, & \text { otherwise, } x_{i}^{\prime \prime}= \begin{cases}v_{i}, & \text { if } m_{i}=1 \\ u_{i}, & \text { otherwise }\end{cases}
$$

Then one element of $\left\{x^{\prime}, x^{\prime \prime}\right\}$ chosen uniformly at random is returned. The well-known uniform crossover and $k$-point crossover are examples of mask-based crossover operators.

For a frequent use of crossover, i.e., $p_{\mathrm{c}}=1$, [9, Lemma 2], Corollary 3, and Lemma 4 yield the following.

Theorem 4: Assume that the GA in Algorithm 2 with $p_{\mathrm{c}}=$ 1 uses any mask-based crossover operator, a bitwise mutation with mutation rate $\chi / n$ for any fixed constant $\chi>0$, and one of the following selection mechanisms:

1) $k$-tournament selection with $k \geq 8(1+\delta) e^{\chi}$;
2) $(\mu, \lambda)$-selection with $\lambda / \mu \geq 2(1+\delta) e^{\chi}$;
3) exponential ranking selection with $\eta \geq 8(1+\delta) e^{\chi}$;

for any constant $\delta>0$. Then there exists a constant $c>0$, such that the expected runtime of the GA is:

1) $\mathcal{O}(n \lambda)$ on ONEMAX if $\lambda \geq c \ln n$
2) $\mathcal{O}\left(n^{2}+n \lambda \ln \lambda\right)$ on LEADINGONES if $\lambda \geq c \ln n$.

The proof can be found in the supplementary materials.
In the next sections, we further demonstrate the generality of Theorem 1 through Corollary 2 by deriving bounds on the expected runtime of GAs with $p_{\mathrm{c}}=1-\Omega(1)$ to optimize or to approximate the optimal solutions.

## B. Optimization on Permutation Space

Given $n$ distinct elements from a totally ordered set, we consider the problem of ordering them so that some measure of sortedness is maximized. In [49], the (1+1) EA was analyzed on several measures of sortedness, including $\operatorname{Inv}(\pi)$ which is defined to be the number of pairs $(i, j)$ such that $1 \leq i<j \leq n$, $\pi(i)<\pi(j)$ (i.e., pairs in correct order). We show that with the method introduced in this paper, analyzing GAs on Sorting problem with InV measure, denoted by $\operatorname{SORTING}_{\text {Inv }}$, is not much harder than analyzing the (1+1) EA.

For the mutation, we use the Exchange( $\pi$ ) operator [49], which consecutively applies $N$ pairwise exchanges between uniformly selected pairs of indices, where $N$ is a random number drawn from a Poisson distribution with parameter 1.

Theorem 5: If the GA in Algorithm 2 with $p_{\mathrm{c}}=1-\Omega(1)$ uses any crossover operator, the Exchange mutation operator, one of the selection mechanisms $k$-tournament selection, $(\mu, \lambda)$-selection, and linear or exponential ranking selection, with their parameters $k, \lambda / \mu$ and $\eta$ being set to no less than $(1+\delta) e /\left(1-p_{c}\right)$, then there exists a constant $c>0$ such that if the population size is $\lambda \geq c \ln n$, the expected time to obtain the optimum of $\operatorname{SORTING}_{\text {Inv }}$ is $\mathcal{O}\left(n^{2} \lambda\right)$.

The proof can be found in the supplementary materials.

## C. Search for Local Optima

A great interest in the area of combinatorial optimization is to find approximate solutions to NP-hard problems, because exact solutions for such problems are unlikely be computable in polynomial time under the so-called $\mathrm{P} \neq \mathrm{NP}$ hypothesis. In the case of maximization problems, a feasible solution is called a $\rho$-approximate solution if its objective function value is at least $\rho$ times the optimum for some $\rho \in(0,1]$. Local search is one method among others to approximate solutions for combinatorial optimization problems through finding local optima (a formal definition is given below). For a number of well-known problems, it was shown [1] that any local optimum is guaranteed to be a $\rho$-approximate solution with a constant $\rho$.

Suppose that a neighborhood $\mathcal{N}(x) \subseteq \mathcal{X}$ is defined for every $x \in \mathcal{X}$. The mapping $\mathcal{N}: \mathcal{X} \rightarrow 2^{\mathcal{X}}$ is called the neighborhood mapping and all elements of $\mathcal{N}(x)$ are called neighbors of $x$. For example, a frequently used neighborhood mapping in the case of binary search space $\mathcal{X}=\{0,1\}^{n}$ is defined by the Hamming distance $H(\cdot, \cdot)$ and a radius $r$ as $\mathcal{N}(x)=\{y \mid H(x, y) \leq r\}$. If $f(y) \leq f(x)$ holds for all neighbors $y$ of $x \in \mathcal{X}$, then $x$ is called a local optimum with respect to $\mathcal{N}$. The set of all local optima is denoted by $\mathcal{L O}$ (note that global optima also belong to $\mathcal{L O}$ ).

A local search method starts from some initial solution $y_{0}$. Each iteration of the algorithm consists of moving from the current solution $x$ to a new solution in its neighborhood, so
that the value of the fitness function is increased. The algorithm continues until a local optimum is reached. Let $m$ be the number of different fitness values attained by solutions from $\mathcal{X} \backslash \mathcal{L O}$ plus 1 . Then starting from any point, the local search method finds a local optimum within at most $m-1$ steps, each step requiring at most $\mathcal{N}(x)$ fitness evaluations.

The following result provides sufficient conditions that ensure the GA finds (at least) a local optimum with a runtime not much greater than that of the local search.

Corollary 4: Given some positive constants $p_{0}, \varepsilon_{0}$, and $\delta$, define the following conditions:
(X1) $p_{\text {mut }}(y \mid x) \geq s$ for any $x \in \mathcal{X}, y \in \mathcal{N}(x)$;
(X2) $p_{\text {mut }}(x \mid x) \geq p_{0}$ for all $x \in \mathcal{X}$;
(X3) $p_{\text {xor }}(f(x) \geq \max \{f(u), f(v)\} \mid u, v) \geq \varepsilon_{0}$ for any $u, v \in \mathcal{X}$;
(X4.1) The nonelitist GA in Algorithm 2 is set with $p_{\mathrm{c}}=1$, and it uses one of the following selection mechanisms:

1) $k$-tournament selection with $k \geq([4(1+\delta)] /\left[\varepsilon_{0} p_{0}\right])$
2) $(\mu, \lambda)$-selection with $(\lambda / \mu) \geq([1+\delta] /\left[\varepsilon_{0} p_{0}\right])$;
3) exponential ranking selection with $\eta \geq$ $\left[(4(1+\delta)) /\left(\varepsilon_{0} p_{0}\right)\right]$
(X4.2) The nonelitist GA is set with $p_{\mathrm{c}}=1-\Omega(1)$, and it uses one of the following selection mechanisms: $k$-tournament selection, $(\mu, \lambda)$-selection, linear or exponential ranking selection, with their parameters $k, \lambda / \mu$, and $\eta$ being set to no less than $\left([1+\delta] /\left[\left(1-p_{\mathrm{c}}\right) p_{0}\right]\right)$.
If (X1)-(X3) and (X4.1) hold, or exclusively (X1), (X2) and (X4.2) hold, then there exists a constant $c$, such that for $\lambda \geq c \ln (m / s)$, a local optimum is reached for the first time after $\mathcal{O}(m \lambda \ln \lambda+(m / s))$ fitness evaluations in expectation.

Condition (X4.1) or (X4.2) characterizes the setting of selection mechanisms, while (X1)-(X3) bear the properties of the variation operators over the neighborhood structure $\mathcal{N}$. Particularly, (X1) assumes a lower bound $s$ on the probability that the mutation operator transforms an input solution into a specific neighbor. Note that in most of the local search algorithms, the neighborhood $\mathcal{N}(x)$ may be enumerated in polynomial time of the problem input size. For such neighborhood mappings, a mutation operator that generates the uniform distribution over $\mathcal{N}(x)$ will satisfy (X1) with $1 / s$ polynomially bounded in the problem input size.

If crossover is frequently used, i.e., $p_{\mathrm{c}}=1$, we also need to satisfy condition (X3) on the crossover operator. It requires that the fitness of solution $x$ on the output of crossover is not less than the fitness of parents with probability at least $\varepsilon_{0}$. Note that such a requirement is satisfied with $\varepsilon_{0}=1$ for the optimized crossover operators, where the offspring is computed as a solution to the optimal recombination problem (see [23]). This supplementary problem is known to be polynomially solvable for maximum clique, set packing, set partition and some other NP-hard problems (see [23]).

The proof of Corollary 4 directly follows from Corollaries 3 and 2 of Theorem 1, see supplementary materials.

Consider the binary search space $\{0,1\}^{n}$ with Hamming neighborhood of a constant radius $r$, a fitness function $f$ such that $m \in \operatorname{poly}(n)$, and assume that the GA uses the bitwise mutation operator and $p_{c}=1-\Omega(1)$. This operator

outputs a string $y$, given a string $x$, with probability $p_{\mathrm{m}}^{H(x, y)}(1-$ $p_{\mathrm{m}})^{n-H(x, y)}$. Note that probability $p_{\mathrm{m}}^{i}\left(1-p_{\mathrm{m}}\right)^{n-j}$, as a function of $p_{\mathrm{m}}$ attains its maximum at $p_{\mathrm{m}}=j / n$. It is easy to show (see [22]) that for any $x \in \mathcal{X}$ and $y \in \mathcal{N}(x)$, the bitwise mutation operator with $p_{\mathrm{m}}=r / n$ satisfies the condition $p_{\text {mut }}(y \mid x)=\mathcal{O}\left(1 / n^{r}\right)$. For a sufficiently large $n$ and any $x \in \mathcal{X}$ holds $p_{\text {mut }}(x \mid x) \geq e^{-r} / 2=\Omega(1)$. By Corollary 4, a GA with the above mentioned operators, given appropriate $\lambda, p_{\mathrm{m}}$ and $p_{c}$, first visits a local optimum with respect to a constant radius Hamming neighborhood after a polynomially bounded number of fitness evaluations in expectation.

Consider the following two unconstrained (and unweighted) problems.

1) MAX-SAT: Given a CNF formula in $n$ logical variables which is represented by $m^{\prime}$ clauses $\mathbf{c}_{1}, \ldots, \mathbf{c}_{m^{\prime}}$ and each clause is a disjunction of logical variables or their negations, it is required to find an assignment of the variables so that the number of satisfied clauses is maximized.
2) MAX-CUT: Given an undirected graph $G=(V, E)$, it is required to find a partition of $V$ into two sets $(S, V \backslash S)$, so that $\delta(S):=\left|\{(u, v) \mid(u, v) \in E, u \in S, v \notin S\}\right|$, is maximized.
Both problems are NP-hard, and their solutions can be naturally represented by bitstrings. Particularly, any local optimum with respect to the neighborhood defined by Hamming distance 1 has at least half the optimal fitness [1].

Theorem 6: Suppose the GA in Algorithm 2 is applied to MAX-SAT or to MAX-CUT using a bitwise mutation with $p_{\mathrm{m}}=\chi / n$, where $\chi>0$ is a constant, a crossover with $p_{c}=1-\Omega(1)$ and one of the selection mechanisms: $k$-tournament selection, $(\mu, \lambda)$-selection, linear or exponential ranking selection, with their parameters $k, \lambda / \mu$ and $\eta$ being set to no less than $\left(\left[(1+\delta) e^{\chi}\right] /\left[1-p_{c}\right]\right)$, where $\delta>0$ is any constant. Then there exists a constant $c$, such that for $\lambda \geq c \ln \left(n m^{\prime}\right)$, a $1 / 2$-approximate solution is reached for the first time after $\mathcal{O}\left(m^{\prime} \lambda \ln \lambda+n m^{\prime}\right)$ fitness evaluations in expectation for MAX-SAT, and after $\mathcal{O}(|E| \lambda \ln \lambda+|V||E|)$ for MAX-CUT.

The proof is analogous to the analysis of $\ell$-UNIMODAL function in Theorem 3, combined with Corollary 4, where $m \leq m^{\prime}+1$ for MAX-SAT and $m \leq|E|+1$ for MAX-CUT.

## V. ESTIMATION OF DISTRIBUTION ALGORITHMS

There are few rigorous runtime results for UMDA and other EDAs. The techniques used in previous analyses of EDAs were often complex, e.g., relying on Markov chains theory. Surprisingly, even apparently simple problems, such as the expected runtime of UMDA on ONEMAX, were open until recently. Indeed, much more is known about classical EAs, e.g., the (1+1) EA solves ONEMAX in expected time $\Theta(n \ln n)$, and this is optimal for the class of unary unbiased black-box algorithms [38].

Algorithm 1 matches closely the typical behavior of EDAs: given a current distribution over the search space, sample a finite number of search points, and update the probability distribution. We demonstrate the ease at which the expected runtime of UMDA with margins and truncation selection on the OneMax function can be obtained using the level-based theorem without making any simplifying assumptions about the optimization process.

## Algorithm 4 UMDA

## Require:

A pseudo-Boolean function $f:\{0,1\}^{n} \rightarrow \mathbb{R}$, and "margins" $m^{\prime} \in[0, \mu / 2)$.
1: Initialise the vector $p_{0}:=(1 / 2, \ldots, 1 / 2)$.
2: for $t=1,2,3, \ldots$ do
3: for $x=1$ to $\lambda$ do
4: $\quad$ Sample the $x$-th individual $P_{t}(x, \cdot)$ according to

$$
P_{t}(x, i) \sim \operatorname{Bernoulli}\left(p_{t-1}(i)\right) \text { for all } i \in[n]
$$

5: Sort the population $P_{t}$ according to $f$.
6: For all $i \in[n]$, with $X_{i}:=\sum_{k=1}^{i n} P_{t}(k, i)$, define

$$
p_{t}(i):=\max \left\{\min \left\{\frac{X_{i}}{\mu} ; 1-\frac{m^{\prime}}{\mu}\right\} ; \frac{m^{\prime}}{\mu}\right\}
$$

To start, we give a formal description of UMDA. If $P \in \mathcal{X}^{k}$ is a population of $\lambda$ solutions, let $P(k, i)$ denote the value in the $i$ th bit position of the $k$ th solution in $P$. The UMDA with $(\mu, \lambda)$-truncation selection is defined in Algorithm 4.

The algorithm has three parameters, the parent population size $\mu$, the offspring population size $\lambda$, and a parameter $m^{\prime}<$ $\mu$ controlling the size of the margins. It is necessary to set $m^{\prime}>0$ to prevent a premature convergence, e.g., without this margin, $p_{t}(i)$ can go to a nonoptimal fixation, this prevents further exploration and causes an infinite runtime. Based on insights about optimal mutation rates in the (1+1) EA, we will use the parameter setting $m^{\prime}=\mu / n$ in the rest of this section.

It is immediately clear that the UMDA in Algorithm 4 is a special case of Algorithm 1. The probability distribution $D\left(P_{t}\right)$ of $y$ is computed in step 7 , and is $\operatorname{Pr}(y=x)=\prod_{j=1}^{n} p_{t}(j)^{x_{j}}(1-$ $\left.p_{t}(j)\right)^{1-x_{j}}$ for any bitstring $x \in\{0,1\}^{n}$.

In some other randomized search heuristics, such as ant colony optimization and cGA, the sampling distribution $D_{t}$ does not only depend on the current population but also on additional information, such as pheromone values. The levelbased theorem does not apply to such algorithms.

Theorem 7: Given any positive constants $\delta \in(0,1)$, and $\gamma_{0} \leq[1 /((1+\delta) 13 e)]$, the UMDA with offspring population size $\lambda$ with $b \ln (n) \leq \lambda \leq n / \gamma_{0}$ for some constant $b>0$, parent population size $\mu=\gamma_{0} \lambda$, and margins $m^{\prime}=\mu / n$, has expected optimization time $\mathcal{O}(n \lambda \ln \lambda)$ on OneMax.

The proof which is available in our supplementary materials follows our guidelines of level-based analysis, a preliminary version of it appeared in [13]. To obtain lower bounds on the tail of the level distribution, we make use of the Feige inequality [24] (or see [13, Corollary 3]).

A similar analysis for LEADINGONES [13] yields a runtime bound $\mathcal{O}\left(n \lambda \ln \lambda+n^{2}\right)$ with offspring population size $\lambda \geq b \ln (n)$ for some constant $b>0$ without use of Feige's inequality. The previous result [8] on LEADINGONES requires a larger population size and gives a longer runtime bound.

Table I summarizes the runtime bounds for the example applications of the tools presented in this paper and the above mentioned result for UMDA on LEADINGONES.

TABLE I
Summary of Results for the GA [Algorithm 2, $p_{\mathrm{c}}=1-\Omega(1)$ ], GA1 (Algorithm 2, $p_{\mathrm{c}}=1$ ) and UMDA (Algorithm 4, $m^{\prime}=\mu / n$ )



On $\{0,1\}^{n}$, GA and GA1 use bitwise mutation operator with rate $\chi / n$, where $\chi$ is any constant. On permutation search space, i.e., Sorting, GA uses Exchange mutation and its setting assumes $\chi=1$. In the case of MAX-SAT, $n$ is the number of logical variables and $m^{\prime}$ is the number of clauses. Parameter $\delta$ is any positive constant, and $c$ is some constant.

## VI. LeVel-Based Theorem Is Almost Tight

How accurate are the time bounds provided by the levelbased theorem? To answer this question, we first interpret the theorem as a universally quantified statement over the operators $D$ satisfying the conditions of the theorem. More formally, given a choice of level-partition and set of parameters $z_{1}, \ldots, z_{m-1}, \delta, \gamma_{0}$, which we collectively denote by $\Theta$, the theorem can be expressed in the form of $\forall D \in \mathcal{D}_{\Theta}: E\left[T_{D}\right] \leq$ $t_{\Theta}$, where $\mathcal{D}_{\Theta}$ is the set of operators $D$ in Algorithm 1 that satisfy the conditions of the level-based theorem with parameterizations $\Theta, E\left[T_{D}\right]$ is the expected runtime of Algorithm 1 with a given operator $D$, and $t_{\Theta}$ is the upper time bound provided by the level-based theorem which depends on $\Theta$.

In order to obtain an accurate bound for a specific operator $D$, e.g., the $(\mu, \lambda)$ EA applied to the OneMax function, it is necessary to choose a parametrization $\Theta$ that reflects this process as tightly as possible. If the bounds on the upgrade probabilities $z_{j}$ for the $(\mu, \lambda)$ EA are too small, then the class $\mathcal{D}_{\Theta}$ includes other processes which are slower than the $(\mu$, $\lambda$ ) EA, and the corresponding bound $t_{\Theta}$ cannot be accurate. Hence, the theorem is limited by the accuracy at which one can describe the process by some class $\mathcal{D}_{\Theta}$.

Assuming a fixed parameterizations $\Theta$, it is possible to make a precise statement about the tightness of the upper bound $t_{\Theta}$. Theorem 8 below is an existential statement on the form $\exists D \in \mathcal{D}_{\Theta}: E\left[T_{D}\right] \geq t_{\Theta}^{\prime}$, where the lower bound $t_{\Theta}^{\prime}$ is close to the upper bound $t_{\Theta}$. Hence, given the information the theorem has about the process through $\Theta$, the runtime bound is close to optimal. More information about the process would be required to obtain a more accurate runtime bound.

In some concrete cases, one can prove that the level-based theorem is close to optimal, using parallel black-box complexity theory [2]. From Corollary 2 with $p_{\mathrm{c}}=0$, which specializes the level-based theorem to algorithms with unary mutation operators, one can obtain the bounds $\mathcal{O}(n \lambda+n \ln n)$ for OneMax, and $\mathcal{O}\left(n \lambda \ln \lambda+n^{2}\right)$ for LeAdingONES for appropriately parameterized EAs. These bounds are within a $\mathcal{O}(\ln \lambda)$-factor of the lower bounds that hold for any parallel unbiased black-box algorithm [2]. For population sizes $\lambda=\mathcal{O}(n / \ln n)$ and $\lambda=\Omega(\ln n)$, the resulting $\mathcal{O}\left(n^{2}\right)$ bound on LEADINGONES is asymptotically tight, because it matches
the lower bound that holds for all black-box algorithms with unary unbiased variation operators [38].

Theorem 8: Given any partition of $\mathcal{X}$ into $m$ nonempty subsets $\left(A_{1}, \ldots, A_{m}\right)$, for any $z_{1}, \ldots, z_{m-1}, \delta, \gamma_{0} \in(0,1)$, where $z_{j} \in(0, \gamma_{0})$ for all $j \in[m-1]$, and $\lambda \in \mathbb{N}$, there exists a mapping $D$ which satisfies conditions (G1), (G2), and (G3) of Theorem 1, such that Algorithm 1 with mapping $D$ has expected hitting time

$$
E[T] \geq\left(\frac{2}{3 \delta} \sum_{j=1}^{m-2} \lambda \ln \left(\frac{\gamma_{0} \lambda}{1+2 \lambda z_{j}+1 / \delta^{2}}\right)\right)+\sum_{j=1}^{m-1} \frac{1}{z_{j}}
$$

where $T:=\min \left\{\lambda t \in \mathbb{N} \mid\left|P_{t} \cap A_{m}\right|>0\right\}$.

The proof can be found in the supplementary materials.

## VII. CONCLUSION

This paper introduces a new technique, the so-called levelbased analysis, that easily yields upper bounds on the expected runtime of complex, nonelitist search processes. The technique was first illustrated on GAs. We have shown that GAs efficiently optimize standard benchmark functions and some combinatorial optimization problems. As long as the population size is not overly large, the population does not incur an asymptotic slowdown on these functions compared to standard EAs that do not use populations. So, speedups can be achieved by parallelizing fitness evaluations. Furthermore, previous work using a weaker form of the level-based analysis indicates that nonelitist, population-based EAs have an advantage on more complex problems, including those with noisy [12], dynamic [11], and peaked [15] fitness landscapes. To demonstrate the generality of the theorem, we also provided runtime results for the UMDA algorithm, an estimation of distribution algorithm, for which few theoretical results exist. Finally, we have shown via lower bounds on the runtime of a concrete process that, given the information the theorem requires about the process, the upper bounds are close to tight.

The conditions of the level-based theorem yield settings for algorithmic parameters, such as population size, mutation and crossover rates, selection pressure etc., that are sufficient to guarantee a time complexity bound. This opens up the possibility of theory-led design of EAs with guaranteed runtimes,

where the algorithm is designed to satisfy the conditions of the level-based theorem. This paper also opens several new directions for future work. An important open problem is to develop techniques for proving lower bounds on the runtime of Algorithm 1. Rowe and Sudholt [48] showed that the nonelitist $(1, \lambda)$ EA becomes inefficient when the population size is too small. While condition (G3) in this paper gives a sufficient condition for the population size, it would be interesting to determine a necessary condition on the population size to efficiently reach the last level $A_{m}$.

## APPENDIX

We state the lemmas used in the proof of Theorem 1. Their proofs are provided in the supplementary materials.
Lemma 5: The functions $g_{1}$ and $g_{2}$ defined below are level functions for any $c>0, \kappa \in(0,1), x \in[\lambda], y \in[m]$ and $y_{j}, q_{j} \in(0,1]$ for each $j \in[m-1]$

$$
\begin{aligned}
g_{1}(x, y) & :=\ln \left(\frac{1+c \lambda}{1+c \max \left\{x, y_{y} \lambda\right\}}\right)+\sum_{i=y+1}^{m-1} \ln \left(\frac{1+c \lambda}{1+c y_{i} \lambda}\right) \\
g_{2}(x, y) & :=\frac{(1-\kappa)^{x}}{q_{y}}+\sum_{i=y+1}^{m-1} \frac{1}{q_{i}}
\end{aligned}
$$

for all $y \in[m-1]$, and $g_{1}(x, y):=g_{2}(x, y):=0$ for $y=m$.
Lemma 6 (Improved Version of [14, Lemma 5]: If $X \sim$ $\operatorname{Bin}(\lambda, p)$ with $p \geq(i / \lambda)(1+\delta)$ and $i \geq 1$ for some $\delta \in(0,1]$, then

$$
E\left[\ln \left(\frac{1+\delta X / 2}{1+\delta i / 2}\right)\right] \geq \frac{\delta^{2}}{7}
$$

Lemma 7: Let $\left\{X_{i}\right\}_{i \in[\lambda]}$ be independent identically distributed random variables, define $Y(j):=\sum_{i=1}^{\lambda} \mathbb{1}_{\left\{X_{i} \geq j\right\}}$ for any $j \in \mathbb{R}$. It holds for any $a, b, c, j \in \mathbb{R}$ with $c \geq 0$ and $b \leq \lambda$ that
(i) $\operatorname{Pr}(Y(j+c) \geq a \mid Y(j) \geq b) \geq \operatorname{Pr}(Y(j+c) \geq a)$
and for any nondecreasing function $f$

$$
\text { (ii) } E[f(Y(j+c)) \mid Y(j) \geq b] \geq E[f(Y(j+c))]
$$

provided that both expectations are well-defined.

## ACKNOWLEDGMENT

Early ideas were discussed at Dagstuhl Seminars 13271 and 15211 "Theory of Evolutionary Algorithms."
