# Pilot Pattern Optimization for Sparse Channel Estimation in OFDM Systems 

Han Wang, Qing Guo, Member, IEEE, Gengxin Zhang, Guangxia Li, and Wei Xiang, Senior Member, IEEE


#### Abstract

Compressive sensing (CS) based sparse channel estimation requires optimal pilot patterns, whose corresponding sensing matrices should have small mutual coherences, so as to efficiently exploit the inherent channel sparsity. For the purpose of minimizing the mutual coherence of the sensing matrix, we introduce a new estimation of distribution algorithm (EDA) to optimize the pilot pattern so as to improve the channel estimation performance. The proposed scheme guides the optimization process by building and sampling the probability distribution model of the promising pilot indexes, and approaches the optimal pilot pattern iteratively. The algorithm is able to not only preserve the current best pilot indexes, but also introduce diversity by sampling new ones, and hence is unlikely to trap into local minima and more robust than other methods. Simulation results show that our proposed method can generate sensing matrices with smaller mutual coherences than existing methods, and the corresponding optimized pilot pattern performs well in terms of sparse channel estimation.


Index Terms-Compressive sensing (CS), estimation of distribution algorithm (EDA), pilot pattern optimization, sparse channel estimation.

## I. INTRODUCTION

CHANNEL estimation, which provides channel state information (CSI) for equalizing channel distortion and demodulating received signals, plays an important part in orthogonal frequency-division multiplexing (OFDM) systems. Comparing with conventional methods, compressive sensing (CS) based channel estimation is capable of exploiting the inherent sparse property of wireless channels, and providing the same CSI with much fewer pilots and high spectral efficiency [1].

In CS-based sparse channel estimation, sparse CSI can be recovered with a high probability, when pilot tones are randomly selected from all OFDM subcarriers. This kind of pilot patterns, corresponding to the partial Fourier sensing matrix

[^0]whose rows are randomly selected from the standard Fourier matrix, is difficult to implement in practical systems due to its randomness. One may design an optimal pilot pattern to improve the CSI recovery probability by constructing its corresponding sensing matrix that better satisfies the restricted isometry property (RIP). However, there are no known efficient methods to evaluate whether a given matrix satisfies the RIP in polynomial time. An alternative scheme is to evaluate the mutual coherence of the sensing matrix, which is more strict but practically feasible than the RIP [2]. The smaller the mutual coherence is, the better the sensing matrix satisfies the RIP. One can exhaustively search all possible pilot patterns to find the optimal sensing matrix. However, this is computationally intractable under the given numbers of subcarriers and pilots used in practical OFDM systems. Welch gave a lower bound of mutual coherence in [3]. We may utilize various mathematical theories, e.g., the cyclic different set theory [4], to construct optimal matrices with the Welch bound. However, optimal matrices only exist when their rows and columns satisfy specific conditions, which are not the common cases in OFDM systems. Therefore, efficient methods to search for a suboptimal pilot pattern are highly desirable, when both the total subcarrier number and the pilot number are given.

Towards this end, pilot pattern optimization schemes based on random search [5], discrete stochastic approximation [6], [7], and cross-entropy optimization (CEO) [8], [9] have been proposed. However, these approaches are randomized search methods whose convergence time cannot be guaranteed. Moreover, the genetic algorithm (GA), an evolutionary algorithm in artificial intelligence, is employed in [10], [11] to accelerate the search of suboptimal pilot patterns. However, this method is likely to trap into local minima and hence less robust.

In this letter, we propose a new pilot pattern optimization method based upon the estimation of distribution algorithm (EDA) [12] for sparse channel estimation in OFDM systems. The EDA is an evolutionary algorithm, which learns and samples the probability distribution of the best individuals of a population at each generation rather than operates the crossover and mutation in the GA. Hence, it can be regarded as a probability version of the GA. The EDA introduces the population diversity by sampling individuals from the probability distribution rather than producing one specific individual, and hence is unlikely to trap into local minima and more robust than the GA. Simulation results show that the pilot pattern optimized by EDA is more effective in exploiting channel sparsity than the ones obtained by random search, CEO and GA.

The remainder of this letter is organized as follows. In Section II, the sparse channel estimation model and the pilot pattern optimization problem are formulated mathematically. Then, the EDA-based pilot pattern optimization method is proposed in Section III. Finally, simulation results are presented in Section IV for evaluating the performance of the proposed approach.


[^0]:    Manuscript received December 12, 2014; accepted May 2, 2015. Date of publication May 5, 2015; date of current version July 8, 2015. This work was supported in part by the National Natural Science Foundation of China under Grants 91338201 and 91438109, by a Smart Futures Fellowship funded by the Queensland Government of Australia, and by the Key Laboratory of Universal Wireless Communications (Beijing University of Posts and Telecommunications), Ministry of Education, P. R. China. The associate editor coordinating the review of this paper and approving it for publication was K. J. Kim.
    H. Wang is with the School of Electronics and Information Engineering, Harbin Institute of Technology, Harbin 150080, China, and also with the Institute of Communications Engineering, PLA University of Science and Technology, Nanjing 210007, China (e-mail: wanghan_email@163.com).
    Q. Guo is with the School of Electronics and Information Engineering, Harbin Institute of Technology, Harbin 150080, China (e-mail: qguo@hit. edu.cn).
    G. Zhang and G. Li are with the Institute of Communications Engineering, PLA University of Science and Technology, Nanjing 210007, China (e-mail: gengxin_zhang@126.com; guangxia@tom.com).
    W. Xiang is with the School of Mechanical and Electrical Engineering, University of Southern Queensland, Toowoomba, QLD 4350, Australia (e-mail: wei.xiang@usq.edu.au).

## II. System Model and Problem Formulation

We assume that an OFDM system has $N$ subcarriers, among which $P(P \leq N)$ subcarriers indexed by $\mathcal{K}=\left\{k_{1}, \ldots, k_{P}\right\}(0 \leq$ $k_{1}<\cdots<k_{P} \leq N-1$ ) are selected as pilot tones. The relationship between the transmitted and received pilot tones can be expressed as

$$
\mathbf{Y}=\mathbf{X H}+\mathbf{V}=\mathbf{X} \mathbf{W} \mathbf{h}+\mathbf{V}
$$

where $\mathbf{Y}=\left[Y\left(k_{1}\right), \ldots, Y\left(k_{P}\right)\right]^{T}$ is the received pilot tone vector, $\mathbf{X}=\operatorname{diag}\left(X\left(k_{1}\right), \ldots, X\left(k_{P}\right)\right)$ is a diagonal matrix composed of the corresponding transmitted pilot tones, $\mathbf{H}=\left[H\left(k_{1}\right), \ldots\right.$, $\left.H\left(k_{P}\right)\right]^{T}$ is the channel frequency response (CFR) vector, $\mathbf{h}=$ $[h(1), \ldots, h(N)]^{T}$ is the $N$-length channel impulse response (CIR) vector whose first $L$ elements contain most of the multipath energy, $\mathbf{W}$ is a $P \times N$ partial Fourier matrix consisting of $P$ rows indexed by $\mathcal{K}$ of the standard $N \times N$ Fourier matrix, and $\mathbf{V}=\left[V\left(k_{1}\right), \ldots, V\left(k_{P}\right)\right]^{T}$ is the additive white Gaussian noise term.

Equation (1) shows that, when the transmitted pilots $\mathbf{X}$ are known at the receiver, the CSI (i.e., CFR vector $\mathbf{H}$ or CIR vector $\mathbf{h})$ is attainable from the received pilots $\mathbf{Y}$. Conventional channel estimation methods work in the frequency domain, requiring that the pilot tone number $P=N$ so as to cover channel variation adequately. In this case, the CFR vector $\mathbf{H}$ can be estimated by the least squares (LS) method. However, recent studies have revealed that the wireless channel is inherently sparse [13], meaning that most elements of the $N$-length CIR vector $\mathbf{h}$ are either zero or nearly zero. As a result, the CS technique can be used to extract the $N$-length sparse CIR vector $\mathbf{h}$ from only a few $P(L<P<N)$ pilot tones, reducing the pilot overhead as well as improving spectral efficiency.

Denote the sensing matrix $\mathbf{A} \triangleq \mathbf{X W}$ for simplicity, i.e.
$\mathbf{A} \triangleq \mathbf{X W}=\frac{1}{\sqrt{N}}\left[\begin{array}{ccc}X\left(k_{1}\right) \omega^{k_{1} 0} & \cdots & X\left(k_{1}\right) \omega^{k_{1}(N-1)} \\ \vdots & \ddots & \vdots \\ X\left(k_{P}\right) \omega^{k_{P} 0} & \cdots & X\left(k_{P}\right) \omega^{k_{P}(N-1)}\end{array}\right]$,
where $\omega=e^{-j 2 \pi / N}$. The mutual coherence of the sensing matrix $\mathbf{A}$ is defined as

$$
\mu(\mathbf{A})=\max _{\substack{0 \leq m, n \leq N-1 \\ \text { onpin }}} \frac{\left|\left\langle\mathbf{a}_{m}, \mathbf{a}_{n}\right\rangle\right|}{\left\|\mathbf{a}_{m}\right\|_{2}\left\|\mathbf{a}_{n}\right\|_{2}}
$$

where $\mathbf{a}_{m}$ is the $m$-th column of $\mathbf{A}$, and $\langle\cdot, \cdot\rangle$ denotes the inner product of two columns. Substituting (2) into (3) gives rise to

$$
\mu(\mathbf{A})=\max _{\substack{0 \leq m, n \leq N-1 \\ \text { onpin }}} \frac{\left|\sum_{i=1}^{P}\left|X\left(k_{i}\right)\right|^{2} \omega^{k_{i}(n-m)}\right|}{\sum_{i=1}^{P}\left|X\left(k_{i}\right)\right|^{2}}
$$

Since commonly used OFDM pilot sequences have the property of "constant amplitude zero auto-correlation", we take $\left|X\left(k_{1}\right)\right|=\cdots=\left|X\left(k_{P}\right)\right|=1$. By defining $d=n-m$ and $\mathcal{D}=$ $\{1, \ldots, N-1\},(4)$ can be simplified into

$$
\mu(\mathbf{A})=\max _{d \in \mathcal{D}} \frac{1}{P}\left|\sum_{i=1}^{P} \omega^{k_{i} d}\right|
$$

which shows that $\mu(\mathbf{A})$ is merely determined by the pilot index set $\mathcal{K}=\left\{k_{1}, \ldots, k_{P}\right\}$ when the total subcarrier number $N$ is given. As a result, we use $\mu(\mathbf{A}(\mathcal{K}))$ instead of $\mu(\mathbf{A})$ for clarity. In view of the periodicity of base $\omega, \mathcal{K}$ can be regarded as a "base pilot pattern" whose flipped and/or circularly shifted versions would produce the same mutual coherence of $\mathbf{A}$ [11], and hence should have the same effect in exploiting channel sparsity. This property will be used for matching pilot patterns in Section III.

As mentioned in Section I, we aim to minimize the mutual coherence of the sensing matrix $\mathbf{A}$ in searching for the optimal pilot pattern to ensure that the CIR vector $\mathbf{h}$ can be recovered with a high probability. Towards this end, the pilot pattern optimization problem can be formulated as

$$
Q_{0}: \quad \min _{\mathcal{K} \in \mathcal{S}} \mu(\mathbf{A}(\mathcal{K}))
$$

where $\mathcal{S}$ is a set composed of all the candidate pilot patterns when $(N, P)$ is given, and hence the cardinality of $\mathcal{S}$ is $\binom{N}{P}$. It is intractable to exhaustively search all $\binom{N}{P}$ possible pilot patterns due to its overwhelming computational complexity. Consequently, we propose a new method to obtain an efficient suboptimal solution $\mathcal{K}_{\text {opt }}$ to the combinatorial optimization problem $Q_{0}$ in (6).

## III. EDA-Based Pilot Pattern Optimization

We first map some evolutionary concepts (such as individual, population, etc.) in the EDA to the problem $Q_{0}$. Define a binary vector, termed individual, $\mathbf{f}=[f(0), \ldots, f(N-1)]^{T}$ whose elements $f\left(k_{1}\right)=\cdots=f\left(k_{P}\right)=1$ and others are 0 . Hence, individual $\mathbf{f}$ encodes the pilot pattern $\mathcal{K}$, and the problem $Q_{0}$ becomes equivalent to

$$
Q_{1}: \min _{\mathbf{f} \in \mathcal{S}} \mu(\mathbf{A}(\mathbf{f})) \quad \text { s.t. } \quad \sum_{n=0}^{N-1} f(n)=P
$$

where $\mathbf{A}(\mathbf{f})$ is the sensing matrix $\mathbf{A}$ determined by the pilot pattern $\mathbf{f}, \mu(\mathbf{A}(\mathbf{f}))$ is the corresponding mutual coherence called fitness, and $\mathcal{S}$ is the search space composed of all the $\binom{N}{P}$ candidate individuals. Exhaustive search of every individual $\mathbf{f}$ in the search space $\mathcal{S}$ is intractable, and the EDA introduces a population $\mathcal{F}$, composed of $M$ individuals, to tackle this issue.

The essential idea behind the EDA is to evolve the current population $\mathcal{F}^{(i)}$ towards the next one $\mathcal{F}^{(i+1)}$ under the guidance of an explicit probability distribution $\mathbb{P}^{(i)}$, which is constructed from selected individuals in $\mathcal{F}^{(i)}$ with best fitness. The new population $\mathcal{F}^{(i+1)}$ is sampled from the promising distribution $\mathbb{P}^{(i)}$, and thus would have better fitness as a whole. As the algorithm evolves, the distribution $\mathbb{P}^{(i)}$ is learned from good individuals and sampled to create new ones for the next generation. And the population $\mathcal{F}^{(i)}$ evolves towards the more promising area of the search space $\mathcal{S}$. Finally, $\mathbb{P}^{(i)}$ converges to a stable distribution $\mathbb{P}_{\text {opt }}$ which the optimal population $\mathcal{F}_{\text {opt }}$ follows, and the optimal individual $\mathbf{f}_{\text {opt }}$ can be found in $\mathcal{F}_{\text {opt }}$. The EDA-based pilot pattern optimization algorithm is summarized in Fig. 1, and detailed as follows.

```
1: Initialize the generation counter \(s=0\), and generate \(M\) individuals randomly as
        the initial population: \(\mathcal{F}^{(0)}=\left[\mathbf{f}_{1}^{(0)}, \ldots, \mathbf{f}_{M}^{(0)}\right]\).
    repeat
        For the current population \(\mathcal{F}^{(1)\), evaluate the fitness of \(\mathbf{f}_{1}^{(1)}, \ldots, \mathbf{f}_{M}^{(1)}\) by (5),
        and sort them by their fitness in ascending order.
        Select the first \(T\) individuals with better fitness: \(\left\{\tilde{\mathbf{f}}_{1}^{(1)}, \ldots, \tilde{\mathbf{f}}_{T}^{(1)}\right\}\) let the
        best one \(\tilde{\mathbf{f}}_{1}^{(1)}=\tilde{\mathbf{f}}_{1}^{(1)}\) and match \(\tilde{\mathbf{f}}_{2}^{(1)}, \ldots, \tilde{\mathbf{f}}_{T}^{(1)}\) with \(\tilde{\mathbf{f}}_{1}^{(1)}\) as follows:
        for \(t=2\) to \(T\) do
            Calculate two circular convolutions \(\mathbf{g}_{t}^{(1)}\) and \(\mathbf{g}_{t, \text { flip }}^{(1)}\) by (17).
            Find the maximum matching index \(N_{0}\) by (16), the matched individual
                \(\tilde{\mathbf{f}}_{t}^{(1)}\) is obtained by circularly shifting \(N_{0}\) bits of \(\tilde{\mathbf{f}}_{t, \text { flip }}^{(1)}\) or \(\tilde{\mathbf{f}}_{t}^{(1)}\).
        for
            Generate the promising population: \(\tilde{\mathcal{F}}^{(1)}=\left[\tilde{\mathbf{f}}_{1}^{(1)}, \ldots, \tilde{\mathbf{f}}_{T}^{(1)}\right]\).
        Calculate the pilot tone occurrence probability vector \(\mathbf{p}^{(i)}\) by (10), and
        formulate the promising probability distribution \(\mathbb{P}^{(1)}\) as in (12).
        Preserve \(\tilde{\mathbf{f}}_{t}^{(1)} \neq \mathbf{f}_{t}^{(i+1)}\), sample new individuals from \(\mathbb{P}^{(1)}\) as in (13), and
        build the new population: \(\mathcal{F}^{(i+1)}=\left[\mathbf{f}_{1}^{(i+1)}, \ldots, \mathbf{f}_{M}^{(i+1)}\right]\).
    until The pilot tone occurrence probability vector \(\mathbf{p}^{(i)}\) satisfies that \(p^{(i)}\left(k_{1}\right)=\)
        \(\cdots=p^{(i)}\left(k_{T}\right)=1\), and others are 0 .
    return The optimal pilot index set \(\mathcal{K}_{\text {opt }}=\left\{k_{1}, \ldots, k_{T}\right\}\).
```

Fig. 1. EDA-based pilot pattern optimization.

The algorithm begins with a population $\mathcal{F}^{(0)}$ which contains $M$ randomly generated individuals, and the population of the $i$-th generation can be denoted by

$$
\mathcal{F}^{(i)}=\left[\mathbf{f}_{1}^{(i)}, \ldots, \mathbf{f}_{M}^{(i)}\right]
$$

which is an $N \times M$ binary matrix. We first evaluate the fitness of each individual in $\mathcal{F}^{(i)}$ by (5), and sort them by their fitness in ascending order. By selecting the first $T(T<M)$ individuals with better fitness (smaller mutual coherence), we generate the following promising population

$$
\tilde{\mathcal{F}}^{(i)}=\left[\tilde{\mathcal{f}}_{1}^{(i)}, \ldots, \tilde{\mathcal{f}}_{T}^{(i)}\right]
$$

The average of the $n$-th row of the binary matrix $\tilde{\mathcal{F}}^{(i)}$ describes the probability of the pilot tone located in the $n$-th subcarrier as follows

$$
p^{(i)}(n)=\frac{1}{T} \sum_{t=1}^{T} \tilde{f}_{t}^{(i)}(n) \quad(n=0, \ldots, N-1)
$$

where $\tilde{f}_{t}^{(i)}(n)$ is the $n$-th element of the $t$-th individual $\tilde{\mathcal{f}}_{t}^{(i)}$ in $\tilde{\mathcal{F}}^{(i)}$. Hence, the promising individual element $\tilde{f}^{(i)}(n)$ satisfies

$$
\tilde{f}^{(i)}(n) \sim \operatorname{Ber}\left(p^{(i)}(n)\right)
$$

where $\operatorname{Ber}(\cdot)$ denotes the Bernoulli distribution, and the promising probability distribution $\mathbb{P}^{(i)}$ can be formulated as

$$
\mathbb{P}^{(i)}: \quad \tilde{\mathcal{f}}^{(i)} \sim \operatorname{Ber}\left(\mathbf{p}^{(i)}\right)
$$

where $\mathbf{p}^{(i)}=\left[p^{(i)}(0), \ldots, p^{(i)}(N-1)\right]^{T}$ is the pilot tone occurrence probability vector. Then we take $\mathbf{f}_{1}^{(i+1)}=\mathbf{f}_{1}^{(i)}$ to preserve the current best individual, and sample new individuals from $\mathbb{P}^{(i)}$ as

$$
\mathbf{f}_{m}^{(i+1)} \sim \operatorname{Ber}\left(\mathbf{p}^{(i)}\right) \quad \text { s.t. } \quad \sum_{n=0}^{N-1} f_{m}^{(i+1)}(n)=P
$$

where $m=2, \ldots, M$. The sampling operation is performed by a two-dimensional Gibbs sampler [14], whose marginal distributions are $\operatorname{Ber}\left(\mathbf{p}^{(i)}\right)$ and $U\{1, M\}$ respectively, and only the samples satisfying the weight constraint of (13) are selected as the candidate individuals. Thus, the population of the $(i+1)$-th generation can be formulated as

$$
\mathcal{F}^{(i+1)}=\left[\mathbf{f}_{1}^{(i+1)}, \ldots, \mathbf{f}_{M}^{(i+1)}\right]
$$

which would have better fitness as a whole. As the algorithm iterates, $\mathbb{P}^{(i)}$ would converge to a stable distribution $\mathbb{P}_{\text {opt }}$, in which $\mathbf{p}^{(i)}$ satisfies that $p^{(i)}\left(k_{1}\right)=\cdots=p^{(i)}\left(k_{P}\right)=1$ and others are 0 . Therefore, the optimal pilot index set can be obtained as $\mathcal{K}_{\text {opt }}=\left\{k_{1}, \ldots, k_{P}\right\}$. The algorithm not only preserves the current best individual, but also introduces diversity by sampling new individuals, and hence is less likely to trap into local minima and more robust than the conventional GA.

It is noted that, the individuals $\tilde{\mathcal{f}}_{t}^{(i)}(t=2, \ldots, T)$ in the promising population $\tilde{\mathcal{F}}^{(i)}$ of (9) are "matched" with the best one $\tilde{\mathcal{f}}_{1}^{(i)}$ so that the promising pilot tones overlap most. Specifically, let $\left\{\tilde{\mathcal{f}}_{1}^{(i)}, \ldots, \tilde{\mathcal{f}}_{T}^{(i)}\right\}$ be the $T$ promising individuals which are selected from $\mathcal{F}^{(i)}$. The first one $\tilde{\mathcal{f}}_{1}^{(i)}$ has the best fitness, and is denoted by $\tilde{\mathcal{f}}_{1}^{(i)}$, i.e., $\tilde{\mathcal{f}}_{1}^{(i)}=\tilde{\mathcal{f}}_{1}^{(i)}$. For $t=2, \ldots, T$, in view of the "flip and/or circular shift constant" property of pilot patterns discussed in Section II, we calculate two $N$-point circular convolutions $\mathbf{g}_{t}=\tilde{\mathcal{f}}_{1} \circledast \tilde{\mathcal{f}}_{t}$ and $\mathbf{g}_{t, \text { flip }}=\tilde{\mathcal{f}}_{1} \circledast \tilde{\mathcal{f}}_{t}$, flip as follows:

$$
\left\{\begin{array}{l}
g_{t}(n)=\sum_{m=0}^{N-1} \tilde{f}_{1}(m) \tilde{f}_{t}((n-m) \bmod N) \\
g_{t, \text { flip }}(n)=\sum_{m=0}^{N-1} \tilde{f}_{1}(m) \tilde{f}_{t}((n+m) \bmod N)
\end{array}\right.
$$

and find the maximum matching index as

$$
N_{0}=\arg \max _{n=0, \ldots, N-1}\left\{g_{t}(n), g_{t, \text { flip }}(n)\right\}
$$

By circularly shifting $N_{0}$ bits of $\tilde{\mathcal{f}}_{t, \text { flip }}$ or $\tilde{\mathcal{f}}_{t}$, we obtain the matched individual $\tilde{\mathcal{f}}_{t}$, and thus the pilot tones in $\tilde{\mathcal{f}}_{t}$ will overlap most with those in the best one $\tilde{\mathcal{f}}_{1}$. As for computing the circular convolution, it can be fast implemented by the FFT/IFFT as

$$
\mathbf{g}_{t}=\tilde{\mathcal{f}}_{1} \circledast \hat{\boldsymbol{f}}_{t}=\operatorname{IFFT}\left(\operatorname{FFT}\left(\tilde{\mathcal{f}}_{1}\right) \circ \operatorname{FFT}\left(\tilde{\mathcal{f}}_{t}\right)\right)
$$

where $\circ$ denotes the Hadamard product of two vectors.

## IV. Simulation Results

In this section, we assume that the OFDM system under consideration has $N=128$ subcarriers, among which $P=32$ are pilot tones. The Extended Vehicular A (EVA) model [15] is employed to evaluate the channel estimation performances with different pilot patterns obtained by various methods. According to [15], we choose the Doppler shift $f_{\mathrm{d}}=5 \mathrm{~Hz}$. In order to directly compare the effectiveness of these patterns in exploiting channel sparsity, no channel coding is considered. The OFDM signal's format follows the Frame Structure type 1 for LTE FDD [16], and the modulation scheme is QPSK. Our experiments were carried out in MATLAB R2014b using an Intel Pentium E6700 3.20 GHz processor with 2 GB memory.

![img-0.jpeg](img-0.jpeg)

Fig. 2. EDA-based pilot pattern optimization process.

TABLE I
Pilot Patterns Optimized by Random
SEARCH, CEO, GA, AND EDA

| Scheme | $\mu(\mathbf{A})$ | $\mathcal{K}_{\text {opt }}$ |
| :--: | :--: | :--: |
| Random | 0.4032 | 611142228313334364045495053556063 |
| Random | 0.4032 | 64707172757882889092100102110114124 |
| CEO | 0.3623 | 413161921242528303133353637434651 |
|  |  | 56586065697783929499109111121123126 |
| GA | 0.2869 | 6815182326334243444547565860636569 |
|  |  | 727376858891949798108116122123128 |
| EDA | 0.2104 | 41314171819202529323538444648525663 |
|  |  | 647177829299101110112119122123124125 |

![img-1.jpeg](img-1.jpeg)

Fig. 3. Channel estimation M.S.E and system BER performance in different pilot patterns.

The iterative process of our proposed EDA-based pilot pattern optimization method is illustrated in Fig. 2. $M=1000$ individuals are randomly generated as the initial population $\mathcal{F}^{(0)}$, and thus the initial pilot tones are uniformly distributed. Then, by selecting and matching $T=500$ better individuals as the promising population $\overline{\mathcal{F}}^{(0)}$, the pilot tone occurrence probability $\mathbf{p}^{(0)}$ focuses on some specific indexes, which show the potential to produce a smaller mutual coherence. As the algorithm iterates, the distribution vector $\mathbf{p}^{(i)}$ is gradually updated by best individuals $\overline{\mathcal{F}}^{(i)}$, which helps generate more promising ones $\mathcal{F}^{(i+1)}$. After 16 iterations, the indexes become stable, and the corresponding distribution $\mathbf{p}^{(i)}$ converges within 73.26 s at the 28 -th generation. Table I compares the obtained pilot pattern with the ones optimized by random search [5], CEO [9] and GA [11]. These algorithms are performed within the same time, and produce various pilot patterns among which the one optimized by the EDA has the smallest mutual coherence.

The channel estimation performances, exploiting the sparse channel with the above different pilot patterns and extracting the CIR with the same T-SLO algorithm [17], are evaluated in Fig. 3. Simulation results suggest that the pilot pattern with smaller mutual coherence produces better channel estimation in terms of the mean square error (MSE), resulting in better
bit error rates (BER) of the system. Hence, the pilot pattern optimized by the EDA is more efficient than its comparative counterparts in exploiting channel sparsity.

## V. CONCLUSION

Optimal pilot patterns, corresponding to the sensing matrices with smaller mutual coherence, are more efficient in exploiting channel sparsity. In this letter, we propose an EDA-based method to minimize the mutual coherence of the sensing matrix for the purpose of optimizing the pilot patterns for sparse channel estimation. The algorithm builds a probability distribution model of the current promising pilot indexes, samples new ones guided by the model, and thus converges towards the optimal pilot pattern iteratively. Simulation results show that our proposed method can produce a sensing matrix with smaller mutual coherence than existing methods. The resulting optimized pilot pattern performs better in terms of sparse channel estimation.

## REFERENCES

[1] F. Yu, D. Li, Q. Guo, Z. Wang, and W. Xiang, "Block-FFT based OMP algorithm for compressed channel estimation in underwater acoustic communications," IEEE Commun. Lett., to be published, DOI: 10.1109/LCOMM.2015.2427806.
[2] J. Tropp, "Greed is good: Algorithmic results for sparse approximation," IEEE Trans. Inf. Theory, vol. 50, no. 10, pp. 2231-2242, Oct. 2004.
[3] L. Welch, "Lower bounds on the maximum cross correlation of signals," IEEE Trans. Inf. Theory, vol. 20, no. 3, pp. 397-399, May 1974.
[4] P. Xia, S. Zhou, and G. Giannakis, "Achieving the welch bound with difference sets," IEEE Trans. Inf. Theory, vol. 51, no. 5, pp. 1900-1907, May 2005.
[5] X. He and R. Song, "Pilot pattern optimization for compressed sensing based sparse channel estimation in OFDM systems," in Proc. IEEE Int. Conf. Wireless Commun. Signal Process., Suzhou, China, Oct. 2010, pp. 1-5.
[6] C. Qi and L. Wu, "Optimized pilot placement for sparse channel estimation in OFDM systems," IEEE Signal Process. Lett., vol. 18, no. 12, pp. 749-752, Dec. 2011.
[7] C. Qi and L. Wu, "A study of deterministic pilot allocation for sparse channel estimation in OFDM systems," IEEE Commun. Lett., vol. 16, no. 5, pp. 742-744, May 2012.
[8] J. C. Chen, C. K. Wen, and P. Ting, "An efficient pilot design scheme for sparse channel estimation in OFDM systems," IEEE Commun. Lett., vol. 17, no. 7, pp. 1352-1355, Jul. 2013.
[9] C. Qi, G. Yue, L. Wu, and A. Nallanathan, "Pilot design for sparse channel estimation in OFDM-based cognitive radio systems," IEEE Trans. Veh. Technol., vol. 63, no. 2, pp. 982-987, Feb. 2014.
[10] L. Najjar, "Pilot allocation by genetic algorithms for sparse channel estimation in OFDM systems," in Proc. 21st EUSIPCO, Sep. 2013, pp. 1-5.
[11] X. He, R. Song, and W. P. Zhu, "Pilot allocation for sparse channel estimation in MIMO-OFDM systems," IEEE Trans. Circuits Syst. II, Esp. Briefs, vol. 60, no. 9, pp. 612-616, Sep. 2013.
[12] P. Larrañaga and J. A. Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. New York, NY, USA: Springer-Verlag, 2002.
[13] W. Bajwa, J. Haupt, A. Sayeed, and R. Nowak, "Compressed channel sensing: A new approach to estimating sparse multipath channels," Proc. IEEE, vol. 98, no. 6, pp. 1058-1076, Jun. 2010.
[14] S. Geman and D. Geman, "Stochastic relaxation, gibbs distributions, and the bayesian restoration of images," IEEE Trans. Pattern Anal. Mach. Intell., vol. PAMI-6, no. 6, pp. 721-741, Nov. 1984.
[15] Evolved universal terrestrial radio access (E-UTRA); user equipment (UE) radio transmission and reception, 3rd Generation Partnership Project, Sophia Antipolis Cedex, France, 3GPP TS 36.101, 2014.
[16] Evolved universal terrestrial radio access (E-UTRA); physical channels and modulation, 3rd Generation Partnership Project, Sophia Antipolis Cedex, France, 3GPP TS 36.211, 2015.
[17] H. Wang, Q. Guo, G. Zhang, G. Li, and W. Xiang, "Thresholded smoothed $\ell_{0}$ norm for accelerated sparse recovery," IEEE Commun. Lett., to be published, DOI: 10.1109/LCOMM.2015.2416711.