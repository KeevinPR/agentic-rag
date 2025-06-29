# EDA-based Joint Power, Subcarrier Allocation and Relay Assignment Scheme for Multiuser Relaying in OFDMA-based Cognitive Radio Systems 

J.S.Oberoi, U.Pareek, M.Naeem, D.C.Lee, Senior Member, IEEE<br>School of Engineering Science<br>Simon Fraser University<br>Burnaby, Canada<br>(joberoi, upareek, mnaeem, dchlee)@sfu.ca


#### Abstract

In this paper, we present an interference and channel conditions aware multiple relay assignment and subcarrier allocation scheme for OFDMA based cognitive radio systems employing cooperative transmission using Decode and Forward (DF) technique. We focus on the problem of assigning the relays, the relay powers and allocating the subcarriers to the destination nodes using the sum capacity of the cognitive radio system as the objective function to be maximized under the constraint of maximum acceptable levels of interference for the primary users (PU). The computational complexity of this assignment using exhaustive search algorithm grows exponentially with the number of relays, subcarriers and receivers. Thus we propose Estimation of Distribution Algorithm (EDA) for this assignment problem. EDA is a probabilistic evolutionary algorithm which updates its population at each iteration on the basis of the probability densities obtained from the population of superior candidates evaluated and chosen at the previous iteration. EDA employed with our allocation scheme has low computational complexity and its performance is comparable to the Upper Bound of the solution as shown by various simulation results.


Keywords- Relay assignment, Subcarrier allocation, Cognitive Radio, OFDMA, Coooperative Communication

## I. INTRODUCTION

Recently, Cognitive Radio [1], [2], [3] has gained much attention of engineers and researchers as it suggests a solution to the problem of spectrum scarcity. The scheme allows the secondary users (SUs) to utilize [4], [5] frequency bands of the licensed primary users (PUs) [6] as long as the SUs avoid causing unacceptable interference to the PUs. In the system of the SUs, using relays is helpful for reducing the interference to the PUs because the secondary user nodes' transmission power can be reduced if their communication is assisted by the relays. Orthogonal Frequency Division Multiple Access (OFDMA) [7] has been developed as one of the most promising techniques for high performance transmission in cellular networks. In this paper, we consider the problem of efficiently allocating wireless resources in OFDMA-based cognitive radio systems.

We consider the downlink of a cognitive radio system comprising a single source, multiple relays employing decode and forward (DF) relaying [8] on multiple receivers. We focus on the method of jointly assigning transmission power and subcarriers to the relays and subcarriers to the receivers with the objective of maximizing the sum rate capacity for all receivers.

We consider the spectrum underlay approach [3], in which SUs are allowed to access PU's channels as long as the interference due to them is below a specified limit. The objective of our joint allocation is to maximize the sum capacity of the receivers under the constraints defined by the spectrum underlay approach. In a DF [8],[9],[10] relaying scheme, a relay receives the signal from the source, decodes it and forwards it to the destination. The performance of the system improves when we use multiple relays rather than a single relay. In the multiple relay scenario, one issue is how to assign the relays to the receivers and allocate relay powers in the best way to maximize the performance and satisfy the interference constraint on the PUs too. OFDMA separates signals carried by different subcarriers, so another issue is how to allocate subcarriers to different users and different relays. Regarding the previous related works, [11] provides a power allocation scheme for OFDM based Cognitive Radio Systems but doesn't take cooperative communication into consideration. Reference [10] provides assignment of relays and subcarriers but does not look into the Cognitive Radio technique. In [12], [13] an efficient scheme for multiple relay selection in Cognitive Radio Systems is introduced but it is not for OFDMA systems.

Exhaustive search algorithm could be considered for such relay assignment and subcarrier allocation for optimal solution but its complexity increases exponentially with the number of relays, subcarriers and SUs. In this paper we explore the idea of using Estimation-of-Distribution Algorithms (EDA) [14], which is categorized as a probabilistic evolutionary algorithm. Unlike the genetic algorithm, EDA produces a new population by evaluating probability density distribution rather than manipulating strings. In this paper, we experiment with the univariate marginal distribution algorithms (UMDAs) [14] due to its simplicity. The rest of the paper is organized in this way: Section 2 presents our system model, section 3 presents our

EDA based algorithm, Upper Bound calculation is explained in section 4 and simulation results in section 5.

## II. SYSTEM MODEL

We consider an OFDMA-based two-hop cognitive radio wireless system with one transmitting node (source), $L$ relay nodes, $N$ subcarriers and $K$ receivers (SUs). We assume that the source, relays and receivers are equipped with a single antenna. Our system model also includes $M$ primary users (PUs), for which the transmission power of the cognitive radio nodes must be limited. $M$ primary users can also be seen as $M$ geographic locations or regions in which the strengths of the cognitive radio signals must be constrained. Fig. 1 shows a multiuser cognitive radio system.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Relay assisted multiuser cognitive radio system
We denote by $h_{r, l}^{n}$ the channel gain from the source to the $l$ th relay on the $n$th subcarrier, $h_{l, k}^{n}$ the channel from the $l$ th relay to the $k$ th SU on the $n$th subcarrier, $h_{l, m}^{n}$ the channel from the $l$ th relay to the $m$ th PU on the $n$th subcarrier and $h_{r, k}^{n}$ the channel from the source to the kth SU on the nth subcarrier. It is assumed that channel state information is known by the receivers and by the central controller that determines the relay and carrier assignment and the power allocation. It is also assumed that all the relays are perfectly synchronized as assumed in [8]. We denote by $p_{l}^{\max }$ the maximum allowable transmission power of the $l$ th relay, which is imposed by hardware. We denote by $P_{s}$ the transmission power of the source, and we assume in this paper that the source transmission power $P_{s}$ is fixed. We assume that the central controller has perfect knowledge of the channel gains: $h_{r, l}^{n}, h_{l, k}^{n}, h_{l, m}^{n}$ and $h_{r, k}^{n}$. For simulations, we will draw all these channel gains from the complex Gaussian distribution and assume that the channel gains are statistically independent. In our system, a central controller evaluates and decides which
relay is assigned to which SU and also the transmission powers of the relays. We define optimization variables $\varepsilon_{i, k}^{n}, l=1,2, \ldots, L$, $k=1,2, \ldots, K, n=1,2, \ldots, N$, where $\varepsilon_{i, k}^{n}$ is a binary assignment indicator such that,

$$
\varepsilon_{i, k}^{n}=\left\{\begin{array}{lr}
1 & \text { if the } l \text { th relay transmits to the } k \text { th user on } n \text { th subcarrier } \\
0 & \text { otherwise }
\end{array}\right.
$$

We also define optimization variable $p_{l}^{n}$ as the transmission power of the $l$ th relay on $n$th subcarrier. We consider the system with the spectrum underlay approach, in which the secondary users (SUs) can utilize the whole spectrum being used by the primary users (PUs) as long as the strength of their signals do not exceed a particular threshold at the primary users. We assume that the bandwidth of each subcarrier is $B$. In the underlay approach, the strength of the interference caused by all the $L$ relays at the primary users must not exceed the interference limit set by the regulatory authority. The cumulative interference caused by transmission of all the $L$ relays on primary users in $l$ th relay's band can be written as,

$$
\sum_{i=1}^{L} \sum_{n=1}^{N}\left|h_{m}^{n}\right|^{2} p_{l}^{n} \int_{f_{n}}^{f_{c}} \phi^{n}(f) d f \leq I_{m}^{\max } \quad \forall m
$$

where, $p_{l}^{n} \phi_{l}^{n}(f)$ is the power spectral density of the $l$ th relay on the $n$th subcarrier [16], where

$$
\phi_{l}^{n}(f)=T_{c}\left(\frac{\sin \pi\left(f-\frac{(2 n-1) B}{2}\right) T_{c}}{\pi\left(f-\frac{(2 n-1) B}{2}\right) T_{c}}\right)^{2}
$$

In (2), $T_{c}$ is the symbol duration, $f_{L}$ and $f_{U}$ represent lower and upper limit of the frequency band licensed to the primary user (which is also shared by the secondary users) and $I_{m}^{\max }$ is the interference limit defined by the regulatory body at each primary user [11].

We now formulate our optimization problem for the case of two-step decode-and-forward (DF) scheme [8] [9] [10]. In such a system, conveyance of each symbol from the source to destination takes place in two time slots. In the first time slot, the source transmits its data symbol for each receiver on the subcarriers assigned to the receiver and its associated relays, and all the relays can receive the signal carrying the symbol. In the second time slot relays will transmit the decoded signal to the receivers using the subcarriers assigned to them. Since the relays transmit the data for each receiver (SU) on a separate subcarrier, their transmissions destined for different receivers are orthogonal to one in accordance with the OFDMA [7] principles. The throughput of reliable information that the $k$ th receiver can receive through the $l$ th relay on $n$th subcarrier and directly from the source can be written [10] as,

$$
C(k, l, n, \boldsymbol{\varepsilon}, \boldsymbol{p})=\frac{\varepsilon_{i, k}^{n}}{2} \log \left(1+\min \left\{P_{r}^{n}\left|h_{r l}^{n}\right|^{2}, P_{r}^{n}\left|h_{r k}^{n}\right|^{2}+p_{l}^{n}\left|h_{m}^{n}\right|^{2}\right\}\right)
$$

Thus we define our optimization problem as given in (4). Constraint C1 ensures that the transmission power of each relay over each subcarrier is non-negative. C2 defines that the sum of all the transmission powers of a particular relay on different subcarriers can't be greater than the maximum allowed limit for that particular relay. C3 makes sure that if a relay doesn't transmit on a subcarrier then its power should be zero. This constraint eliminates some solutions that waste transmission power. C4 ensures the cumulative interference from all relays and through all subcarriers on a particular PU should not be greater than the interference limit set. C5 and C6 ensure that in the second time slot, in which relays can transmit, a particular subcarrier can be used either by one pair of relay and SU or not used at all. This constraint precludes the possibility of multiple relays simultaneously transmitting at the same subcarrier; that is, we consider the system in which a receiver does not have diversity combining capability.
$\max \sum_{k=1}^{K} \sum_{n=1}^{N} \sum_{l=1}^{L} C(n, k, l, \boldsymbol{\varepsilon}, \boldsymbol{p})$
$C 1: p_{i}^{*} \geq 0 \quad \forall(l, n)$
$C 2: \sum_{n=1}^{N} p_{i}^{*} \leq p_{i}^{m \times 1} \quad \forall l$
$C 3: p_{i}^{*} \leq \sum_{k=1}^{K} \varepsilon_{i, k}^{*} p_{i}^{m \times 1} \quad \forall(l, n), l \neq 0$
$C 4: \sum_{l=1}^{L} \sum_{n=1}^{N}\left|h_{l n}^{*}\right|^{2} p_{i}^{*} \int_{l_{n}^{*}}^{l_{n}^{*}} \phi_{i}^{*}(f) d f \leq I_{m}^{m \times 1} \quad \forall m$
$C 5: \sum_{k=1}^{K} \sum_{l=0}^{L} \varepsilon_{i, k}^{*} \leq 1, \quad \forall n$
$C 6: \varepsilon_{i, k}^{*} \in\{0,1\} \quad \forall(l, k, n)$

## III. EDA BASED AlGORITHM

In this section, we present our use of the Estimation-ofDistribution Algorithm (EDA), which belongs to the class of the Evolutionary Algorithms (EAs), for solving optimization problem (4). EAs are inspired by the biological evolution theory and in it the candidate solutions of an optimization problem are represented as individuals of the population. The fitness of each individual (a particular candidate solution) in the population is evaluated in the first phase of each iteration. In the selection phase, the individuals with higher fitness values are chosen as the parents of the individuals for the next population. In EDA the probability distribution is estimated from the selected individuals of the previous population rather than mutation or cross over, as done in other evolutionary algorithms [14]. Then, a new population of individuals is randomly generated from the probability distribution estimated from the previous iteration.

In general, EDA is characterized and described by the parameters $\left(I_{s}, F, \Delta_{l}, \eta_{l}, \beta_{l}, p_{s}, \Gamma, I_{T e r}\right)[13]$, where

1. $I_{s}$ is the space of all potential solutions (entire search space of individuals).
2. $F$ denotes the fitness function.
3. $\Delta_{l}$ is the population (the set of individuals) at the $l_{\text {th }}$ iteration and $\left|\Delta_{l}\right|$ denotes its cardinality.
4. $\eta_{l}$ is the set of best candidate solutions selected from the set $\Delta_{l}$ at the $l_{\text {th }}$ iteration.
5. We denote $\beta_{l} \equiv \Delta_{l}-\eta_{l} \equiv \Delta_{l} \cap{ }^{c} \eta_{l}$ where ${ }^{c} \eta_{l}$ denotes the complement of $\eta_{l}$.
6. $p_{s}$ is the selection probability. The EDA algorithm selects $p_{s}\left|\Delta_{l}\right|$ individuals from the set $\Delta_{l}$ to make up the set $\eta_{l}$.
7. We denote by $\Gamma$ the distribution estimated from $\eta_{l}$ (the set of selected candidate solutions) at each iteration.
8. $I_{T e r}$ is the maximum number of iterations.

For EDA each individual can be represented by a binary string of a fixed length. Let us denote by $z$ the length of the binary string. The binary string can be also viewed as a $z$ dimensional binary vector. For example, an individual can be denoted by a binary row vector $\mathbf{X}=\left(x_{1}, x_{2}, \cdots, x_{z}\right), x_{i} \in\{0,1\}$. In our optimization problem, we represent the decision variable $\varepsilon_{i, k}^{*}$ as a binary array. For our EDA implementation we can represent array $\varepsilon_{i, k}^{*}$ as a binary vector of length $N L K \equiv z$ For each iteration $l$, the EDA maintains a population of individuals, and we denote by $\Delta_{l}$ the population at iteration (generation) $l$. Population, $\Delta_{l}$ can be specified by the following matrix,

$$
A=\left(\begin{array}{c}
X^{1} \\
X^{2} \\
\vdots \\
X^{\left[k_{1}\right]}
\end{array}\right)=\left(\begin{array}{cccc}
x_{1}^{1} & x_{2}^{1} & \vdots & x_{z}^{1} \\
x_{1}^{2} & x_{2}^{2} & \vdots & x_{z}^{2} \\
\cdots & \cdots & \cdots & \cdots \\
x_{1}^{\left[k_{1}\right]} & x_{2}^{\left[k_{2}\right]} & \vdots & x_{z}^{\left[k_{z}\right]}
\end{array}\right)
$$

where the superscript indexes and individual and the subscript indexes the component of the binary vector representing an individual. The EDA scheme can be described as the following:

Step 1: Generate initial population $\Delta_{0}$. This is done by random sampling according to the uniform distribution, i.e. probability of getting 1 and 0 on any bit position in an individual being equal to 0.5 which means,

$$
p_{i}\left(x_{i}=1\right)=p_{i}\left(x_{i}=0\right)=0.5, i=1,2, \ldots, n
$$

The resultant generated population is passed through various defined constraints and if they are not satisfied the population is modified to do so.

For iterations $1=1,2, \ldots, I_{T e r}$ steps 2-7 are followed:
Step 2: Rate the individuals of the current population $\Delta_{l . l}$ by evaluating the fitness function at each particular individual.

Step 3: If $I_{T e r}$ number of iterations have been processed then terminate, else proceed.

Step 4: Select the best $p_{s} \Delta_{l . l}$ individuals.
Step 5: Estimate the probability density distribution on the basis of $\eta_{l . l}$ best individuals which is, (7)

$$
\Gamma_{l}=P\left(x_{1}, x_{2}, \cdots, x_{n} \mid \eta_{l-1}\right)
$$

Step 6: Generate new $\left|\Delta_{l}\right|$ individuals on the basis of the new probability distribution (7) and again pass it through all

the mentioned constraints to get modified individuals which satisfy all constraints.

Step 7: Go to step 2 and repeat.
The easiest way to calculate an estimate of the required probability distribution is to treat all the variables of the binary vector as if they were statistically independent from each other. Then, the joint probability distribution becomes the product of the marginal distributions. This particular method in EDA is called UMDA (univariate marginal distribution algorithm) [8]. EDA creates new candidate solutions by building and sampling a probabilistic model in the form of the probability vector instead of using crossover and mutation. After selection, the probability vector is updated and it stores the proportion of 1 s in each position of the selected population. Then, each bit of a new candidate solution is set to 1 with the probability equal to the proportion of 1 s in that particular position; otherwise, the bit is set to 0 . Consequently, the variation operator of UMDA preserves the proportions of 1 s in each position while decorrelating different string positions. Our problem falls under the same category as one relay allocation doesn't depend on the other relay or subcarrier allocation and vice versa. Thus $\Gamma_{l}$ is estimated by taking the product of individually estimated univariate marginal distributions (UMDA) which is mathematically expressed as,

$$
\Gamma_{l-1}=p\left(x_{1}, x_{2}, \cdots, x_{n} \mid \eta_{l-1}\right)-\prod_{i=1}^{n}\left(\frac{\sum_{j=1}^{|n_{i}|} \delta\left(X_{i}^{j}=x_{i} \mid \eta_{l-1}\right)}{\left|\eta_{l-1}\right|}\right)
$$

Where, $\delta$ is an indicator function for the individual indexed by $j$ in the set $\eta_{l-1}$

$$
\delta\left(X_{i}^{j}=x_{i} \mid \eta_{l-1}\right)=\left\{\begin{array}{cc}
1 & \text { if } X_{i}^{j}=x_{i} \\
0 & \text { otherwise }
\end{array}\right.
$$

The fitness function for our EDA is, $\sum_{k=1}^{n} \sum_{i=1}^{n} \sum_{k=1}^{n} C(n, k, l, \varepsilon, p)$ as given in (3).

As suggested in [13], thresholds are applied to the EDA process to stop it from converging prematurely and thus getting stuck in a local optimum. The same method is followed and fixed thresholds are set for higher and lower limits of probability distribution. As a result probability distribution densities are not allowed to converge to 1 or 0 prematurely.

Now we present our subroutine, Channel and Interference Aware Power Allocation (CIAPA), Table 1 to show how power is assigned and subcarriers allocated to different selected relays. Loop (A) of CIAPA makes sure that either just one pair of SU and relay or none is served through a subcarrier by restricting number of active $\varepsilon_{l, k}^{n}$ in a row to maximum of one. Then channel conditions between relays and the SUs are taken into account for different possible subcarriers. Loop (B) divides the power amongst different subcarriers of a relay according to the channel condition weights, thus giving more power to the subcarrier having better channel condition with a SU than other possible pairs. Finally, Loop (C) satisfies the maximum allowed interference constraint on the PUs through following steps. First, the relay subcarrier pair producing
maximum interference is identified. The transmitting power of the relay on that subcarrier is reduced to a level at which the interference constraint can be satisfied. If it still violates the maximum level then that pair is assigned zero power level and next highest interference producing pair is picked to repeat this loop (C) procedure.

Table 1: CIAPA

| For $\mathbf{n}=1$ to $\mathbf{N}$ (A) | Flops |
| :--: | :--: |
| 1: if $\sum_{k=1}^{n} \sum_{l=1}^{n} \varepsilon_{l, k}^{n}>1$ |  |
| 2: $x=$ rand permof find $\left(\varepsilon_{l, k}^{n}=1\right)$ | $1: \mathrm{LK}+1$ |
| 3: $\varepsilon_{l, k}^{n}=0 \forall l, k$ | 2: LK |
| 4: $\varepsilon_{u(1)}^{n}=1$ | 3: LK |
| 5: End | 4: 1 |
| 6: channel $\_$epsilon $_{l, k}^{n}=H_{l, k}^{n} * \varepsilon_{l, k}^{n} \forall l, k$ | 6: LK |
| 7: epsilon $_{l}^{n}=$ find $\left(\right.$ channel $\left._{-} \epsilon_{l, k}^{n} \neq 0\right) \forall l$ | 7: L |
| End |  |
| For $1=1$ to L (B) |  |
| 1: factor $=\sum_{n=1}^{1} \epsilon_{l, k}^{n} \epsilon_{n} p_{l}^{n}$ |  |
| 2: $p_{l}^{n}=\left(\right.$ epsilon $\left._{l}^{n} / \right.$ factor $)^{*} p_{l}^{n \times n} \forall n$ | 1: N |
|  | 2: 2 N |
| End |  |
| For $\mathrm{m}=1$ to M (C) |  |
| $1: \Psi_{l}^{n}=\left|\hat{n}_{m}^{n}\right|^{2} \int_{l}^{1} \phi_{l}^{n}(f) d f \forall l, n$ |  |
| 2: $I_{n}^{\text {min }}=\sum_{l=1}^{1} \sum_{n=1}^{n} \Psi_{l}^{n}$ |  |
| 3: While $I_{n}^{\text {min }}>I_{m}^{\text {max }}$ | 1: LN |
|  | 2: LN |
| 4: $I_{m}^{\text {ref }}=\max \left(\Psi_{l}^{n}\right)$ | 3: 1 |
| 5: $\left(I^{n}, n^{n}\right)=\arg \max \left(\Psi_{l}^{n}\right)$ | 4: LN |
| 6: $I_{m}^{\text {min }}=I_{m}^{\text {max }}-I_{m}^{\text {ref }}$ | 5: 2 |
| 7: if $I_{m}^{\text {min }}<I_{m}^{\text {max }}$ | 6: 1 |
| 8: $p_{l^{n}}^{n^{r}}=p_{l^{n}}^{n^{r}} *\left(I_{m}^{\max }-I_{m}^{\text {rem }}\right) / I_{m}^{\text {ref }}$ | 7: 1 |
| 9: break | 8: 3 |
| 10: end | 11: 2 |
| 11: $\Psi_{l^{n}}^{n^{r}}=0, p_{l^{n}}^{n^{r}}=0$ | 12: K |
| 12: $\varepsilon_{l^{n}, k}^{n^{r}}=0 \forall k$ | 13: $I_{m}^{\text {max }}=\sum_{l=l}^{k} \sum_{n=l}^{m} \Psi_{l}^{n}$ |
| 13: $I_{m}^{\text {max }}=\sum_{l=l}^{k} \sum_{n=l}^{m} \Psi_{l}^{n}$ |  |
| 14 : End |  |
| End |  |
| Return: $p_{l}^{n}$ |  |

We present the complexity of our subroutine in terms of flops. A flop is defined as a real floating point operation. A real addition, multiplication and division is considered as a

single flop each. Logical and assignment operator takes one flop too. For our subroutine, total flops are $N(4 L K+L+2)+$ $L(3 N)+M(4 L N+K+10)$. The UMDA procedure uses $|\eta|(L K N)$ + LKN flops and $|\Delta|(6 L N K)$ flops are consumed by the objective function evaluation. The complexity order obtained is $\approx \mathrm{O}(L K N+L M N+K M)$ which is polynomial time and less than that of exhaustive search.

## IV. UPPER BOUND CALCULATION

In order to evaluate the quality of solutions produced by our EDA algorithm, we need some benchmarks. However, the exact optimal solution to problem (4) is difficult to achieve for large values of $K, L$, and $N$. In this section we derive an upper bound of $\sum_{k=1}^{\infty} \sum_{n=1}^{\infty} \sum_{k=1}^{\infty} C(n, k, l, \varepsilon, p)$ in optimization problem (4). In the next section, we will compare the quality of our EDA solutions against this upper bound. Integer constraint C6 of problem (4) immediately poses a challenge. We can first relax this constraint to $0 \leq \varepsilon_{l, k}^{*} \leq 1, \forall l, n, k$ in order to remove the integer constraint and obtain an upper bound. However, even with this relaxation, the optimization problem is not convex. Thus, we take the following approach. Throughput given in (3) can be written as,
$C(k, l, n, \varepsilon, p)=\min \left\{\frac{\varepsilon_{l, 1}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}\right), \frac{\varepsilon_{l, 2}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}+p_{l}^{n}\left|h_{n}^{*}\right|^{2}\right)\right\}$
For $\varepsilon_{l, k}^{*} \in\{0,1\}$, the following relation holds:
$\frac{\varepsilon_{l, 2}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}+p_{l}^{n}\left|h_{n}^{*}\right|^{2}\right)=\frac{\varepsilon_{l, 1}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}+\frac{p_{l}^{n}\left|h_{n}^{*}\right|^{2}}{\varepsilon_{l, k}^{*}}\right)$
if we interpret the value of $\frac{\varepsilon_{l, 1}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}+\frac{p_{l}^{n}\left|h_{n}^{*}\right|^{2}}{\varepsilon_{l, k}^{*}}\right)$ at
$\varepsilon_{l, 1}^{*}=0$ as $\lim _{0 \leq k \rightarrow 0} \frac{\varepsilon_{l, 2}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}+\frac{p_{l}^{n}\left|h_{n}^{*}\right|^{2}}{\varepsilon_{l, k}^{*}}\right)=0$.
Thus we can transform (10) into,
$C(k, l, n, \varepsilon, p)=\min \left\{\frac{\varepsilon_{l, 1}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}\right), \frac{\varepsilon_{l, 2}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}+\frac{p_{l}^{n}\left|h_{n}^{*}\right|^{2}}{\varepsilon_{l, k}^{*}}\right\}\right.$
Now we introduce a slack variable, $P_{l, k}^{*}$ and reform our optimization problem as follows (13):
$\max \sum_{k=1}^{N} \sum_{n=1}^{N} \sum_{l=1}^{L} r_{l, k}^{*}$
$D 1: r_{l, k}^{*} \leq \frac{\varepsilon_{l, k}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}\right) \quad \forall(l, k, n)$
$D 2: r_{l, k}^{*} \leq \frac{\varepsilon_{l, 1}^{*}}{2} \log \left(1+P_{l}^{n}\left|h_{n}^{*}\right|^{2}+\frac{p_{l}^{n}\left|h_{n}^{*}\right|^{2}}{\varepsilon_{l, k}^{*}}\right) \forall(l, k, n)$
$D 3: p_{l}^{*} \geq 0 \quad \forall(l, n)$
$D 4: \sum_{k=1}^{N} p_{l}^{*} \leq p_{l}^{n+1} \quad \forall l$
$D 5: p_{l}^{*} \leq \sum_{k=1}^{N} \varepsilon_{l, k}^{*} p_{l}^{n+1} \quad \forall(l, n), l \neq 0$
$D 6: \sum_{k=1}^{N} \sum_{n=1}^{N}\left|h_{n *}^{*}\right|^{2} p_{l}^{*} \int_{l_{1}}^{l_{2}} \phi_{l}^{*}(f) d f \leq l_{n}^{n+1} \quad \forall m$
$D 7: \sum_{k=1}^{N} \sum_{l=1}^{L} \varepsilon_{l, k}^{*} \leq 1, \quad \forall n$
$D 8: \varepsilon_{l, k}^{*} \in(0,1) \quad \forall(l, k, n)$
This optimization problem can be solved by convex solver as D2 is a convex constraint [17]. We relaxed the constraint on $\varepsilon_{l, k}^{*}$ in D8 to allow it to take any real value between 0 and 1. The solution of (13) gives us the upper bound of our original problem.

## V. SIMULATION RESULTS

In this section, we present simulation results. In order to evaluate the quality of each solution obtained by our EDA heuristic algorithm, we compare its associated objective function value (sum capacity) with an upper bound of the function value. For simplicity they have been labeled as EDA and UB, respectively. We have evaluated our algorithm for different parameters of the system model such as the number of relays, SUs, PUs, subcarriers and interference level. In Fig. 2 we plot the performance of our proposed algorithm against different numbers of relays. We see the performance of our EDA heuristic is fairly close to the upper bound. We see that the sum capacity increases as the number of relays increases. Fig. 3 plots the sum capacity of our EDA solution against the number of subcarriers, $N$. Again, the EDA solution has performance fairly close to the performance upper bound derived. The sum capacity increases with the number o subcarriers, as it should because each subcarrier has a fixed bandwidth attached to it. Fig. 4 shows that the sum capacity decreases if the number of PUs increases. As the number of PUs increase, interference constraints are to be satisfied by the relay and subcarrier assignment and thus the feasible set of the optimization problem shrinks.
![img-1.jpeg](img-1.jpeg)

Fig. 2 Capacity vs. Number of Relays

![img-4.jpeg](img-4.jpeg)

Fig. 3 Capacity vs. Number of Subcarriers
![img-5.jpeg](img-5.jpeg)

Fig. 4 Capacity vs. Number of Primary users
![img-4.jpeg](img-4.jpeg)

Fig. 5 Capacity vs. Interference Limit
![img-5.jpeg](img-5.jpeg)

Fig. 6 Capacity vs. Number of Secondary users
In Fig. 5 we see that the capacity of the system increases with the maximum allowed level of interference on PU's increases. Fig. 6 shows that the sum capacity increases for increase in number of SUs. In all the above figures, we have provided the percentage value of EDA vs. UB on the x -axis. The results show that on an average our EDA result is in the bracket of (99-99.5\%) of the UB. Overall our results are consistent with our system model and also show that our EDAbased approach gives results close in capacity to the upper bound of the solution.

## VI. CONCLUSION

In this paper we presented an EDA-based Power, Subcarrier Joint Allocation and Relay Assignment scheme for OFDMAbased Multiuser Cognitive Radio Systems. It performed very well and gave results close to a performance upper bound. Thus, the scheme presented in this paper is a good candidate for solving complex resource allocation problems in real-time in practical communication system scenarios.

## REFERENCES

[1] L. E. Doyle, Essentials of Cognitive Radio, Cambridge University Press, 2009.
[2] L. Berlemann and S. Mangold, Cognitive radio and Dynamic Spectrum access, Wiley, 2009.
[3] S.Haykin, "Cognitive radio: brain-empowered wireless communications," IEEE Journal on Selected Areas in Communications, vol.23, no.2, pp.201-220, February 2005.
[4] Ian F. Akyildiz, Won-Yeol Lee, Mehmet C. Vuran, Shantidev Mohanty, NeXt generation/dynamic spectrum access/cognitive radio wireless networks: A survey, Computer Networks, volume 50, Issue 13, 15 September 2006, Pages 2127-2159, ISSN 1389-1286.
[5] Federal Communications Commission, Spectrum Policy Task Force Report, FCC 02-135, 2002.
[6] J. Mitola III and G. Q. Maguire, Jr., Cognitive radio: making software radios more personal, IEEE Personal Communications Magazine, Vol. 6, nr. 4, pp. 13-18, Aug. 1999.
[7] Samuel C. Yang, OFDMA System Analysis and Design, Artech House, 2010.
[8] Y. Jing and H. Jafarkhani, "Single and multiple relay selection schemes and their achievable diversity orders," IEEE Transactions on Wireless Communications, vol. 8, no. 3, pp. 1414 - 1423, Mar. 2009.

[9] I. Maric and R. D. Yates, "Bandwidth and Power Allocation for Cooperative Strategies in Gaussian Relay Networks," IEEE Trans. Inform. Theory, vol. 56, no. 4, pp. 1880-1889, Apr. 2010.
[10] Danhua Zhang; Youzheng Wang; Jianhua Lu; , "QoS Aware Resource Allocation in Cooperative OFDMA Systems with Service Differentiation," Communications (ICC), 2010 IEEE International Conference on, vol., no., pp.1-5, 23-27 May 2010.
[11] Gaurav Bansal, Md. Jahangir Hossain, Vijay K. Bhargava, "Optimal and Suboptimal Power Allocation Schemes for OFDM-based Cognitive Radio Systems," IEEE Transactions on Wireless Communications, vol 7, no 11, pp 4710-4718 (2008)
[12] M. Naeem, D. C. Lee, U. Pareek, "An Efficient Multiple Relay Selection Scheme for Cognitive Radio Systems," Communications Workshops (ICC), 2010 IEEE International Conference on, vol., no., pp.1-5, 23-27 May 2010.
[13] U. Pareek, M. Naeem and D.C. Lee, "EDA-Based Relay Assignment Scheme for Multiuser Cognitive Radio Systems," The IASTED International Conference on Wireless Communications, Banff, Alberta Canada, 2010.
[14] P. Larranaga and J. A Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation (Kluwer Academic Publishers, 2001).
[15] J. Ocenasek, J. Schwarz, M. Pelikan, Design of Multithreaded Estimation of Distribution Algorithms, ACM Genetic and Evolutionary Computation Conference - GECCO pp. 1247 - 1258, 2003.
[16] T. Weiss, A. Krohn, J. Hillenbrand, F. Jondral, "Mutual Interference in OFDM-based Spectrum Pooling Systems," in Proc. IEEE Vehicular Technol. Conf. (VTC '04), vol. 4, pp. 1873-1877, May 20.
[17] W. Yu and J. M. Cioffi, "FDMA Capacity of Gaussian Multiple-Access Channels with ISI, " IEEE Transactions on Communications, vol. 50, no. 1, pp. 102-111, Jan. 2002.