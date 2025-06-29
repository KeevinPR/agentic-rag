# Estimation of Distribution Algorithm for Scheduling in Uplink Multiuser Wireless Communication System 

M. Naeem and D. C. Lee, Senior Member, IEEE


#### Abstract

In this paper, we present a real-time low-complexity user scheduling scheme for uplink multiuser multiple input multiple output (MIMO) wireless communication systems. We apply Estimation of Distribution Algorithm (EDA) for user scheduling problem. The computational complexity of exhaustive search for user scheduling problem grows exponentially with the number of users. The proposed EDA has low computational complexity and can find a near-optimum solution in real time. In addition to applying the general EDA to user scheduling, we also present a specific improvement to EDA, which increases the likelihood of getting the optimum solution by generating cyclic shifted initial population.


Index Terms: Estimation of Distribution Algorithm, User Scheduling, MIMO, wireless communication

## I. INTRODUCTION

MULTIPLE-input-multiple-output (MIMO) wireless communication systems have significantly higher channel capacity than the single-input-single-output (SISO) system for the same total transmission power and bandwidth [1] [2]. In practical multiuser MIMO wireless communication systems, the selection diversity (user scheduling) plays a significant role in improving the system performance in terms of sum rate capacity. User scheduling scheme selects the best group of users at each time slot to maximize the sum rate capacity of multiuser MIMO wireless communication system [3].

A number of user scheduling schemes are in the literature, with the motivation to improve the system performance in terms of either sum rate capacity or bit error rate. The complexity of exhaustive search for user scheduling increases exponentially with the number of users. For example if $K_{s}$ is the maximum number of users that can be supported simultaneously by the multiuser MIMO system and $K$ is the total number of users, then the number of possible ways of user scheduling is $\sum_{i=1}^{K_{s}}\binom{K}{i}$. Exhaustive search algorithm (ESA) evaluates all possible ways of user scheduling. Enumerating over all possible combinations and finding the one that can give best performance is computationally inefficient. Due to the high computational complexity of the optimal selection (e.g., ESA), a number of suboptimal solutions were proposed [4]-[8]. The Norm Based (NB) algorithm is a low-complexity user scheduling method [4] [5]

[^0][6] but it is only suitable for low signal to noise ratio (SNR). Its performance is relatively poor at high SNR. An Adaptive Markov Chain Monte-Carlo (AMCMC) based user scheduling is presented in [4] and Sequential Monte Carlo Optimization (SMCO) is proposed for joint antenna and user selection in [5]. A Block Diagonalization (BD) based user selection algorithm with precoding is proposed in [6] and [7].

In this paper we introduce user scheduling that employs Estimation of Distribution Algorithms (EDAs) [11]. Unlike other population-based evolutionary algorithms, an EDA generates a new population from estimated probability distributions instead of string manipulation. One major advantage of EDAs is that they can use the interrelation among the variables explicitly. No significant parameter tuning is required for EDA as compared to other Evolutionary Algorithms (EAs). In applying EDAs to user scheduling, we present an improved scheme, which uses cyclic shifted initial population to achieve better algorithmic performance.

The rest of the paper is organized as the following. The system model is described in sections II. In section III, we present a new approach to user scheduling, which uses EDA. We also discuss how to tailor the conventional EDA for improving its convergence speed in applying to user scheduling. Simulation results are presented in section VI.

## II. SYSTEM MODEL

We consider an uplink Multiuser MIMO system with $K$ mobile users. Each user has $N_{S}$ transmit antennas, and the Base Station (BS) has $N_{B}$ receive antennas, as shown in Fig. 1. It is assumed that the receiver has the channel state information (CSI). The receiver (Base Station) will schedule the best subset of mobile users for transmission at each time block. Signals to be transmitted are generated in accordance with modulation schemes, such as M-PSK, M-FSK, M-QAM, etc., from the information messages to be sent. The mobile radio channel is assumed to be quasi-static, and the channel gain remains constant during each code block of data. We denote by vector $S_{k}=\left[\begin{array}{llllllllll}x_{k}^{1} & x_{k}^{2} & \cdots & x_{k}^{N_{c}}\end{array}\right]^{1 / 2} \in \mathbb{C}^{N_{c} \times 1}$ the symbols transmitted through $N_{c}$ transmit antennas simultaneously from the $k t h$ user in each channel use. The signal received at the receiver at each symbol duration can be expressed as [3]

$$
Y=\sum_{k=1}^{K} H_{k} S_{k}+Z
$$

where $H_{k}$ is $N_{B} \times N_{S}$ channel matrix whose coefficients


[^0]:    The authors are with the School of Engineering Science at Simon Fraser University, Burnaby, BC V5A 1S6 Canada. (e-mail: mnaeem@sfu.ca; dchlee@sfu.ca).

represents the channel gains between $N_{K}$ receive antennas at the base station (BS) and $N_{t}$ transmit antennas of the kth user, $Y=\left[\begin{array}{llllllll}y_{1} & y_{2} & \ldots & y_{N_{K}}\end{array}\right]^{T} \in \mathbb{C}^{N_{K} \times 1}$ is the received signal vector and $Z=\left[\begin{array}{llllllll}z_{1} & z_{2} & \ldots & z_{N_{K}}\end{array}\right]^{T} \in \mathbb{C}^{N_{K} \times 1}$ is the complex additive white Gaussian noise with zero mean and unit variance .

If all $K$ users are to transmit together, the optimal sum rate capacity for the uplink multiuser MIMO system is [3] [4]

$$
\begin{aligned}
& C_{\max }\left(H_{1}, H_{2}, \ldots, H_{K}\right) \\
& =\left\{\text { s.t. } \sum_{k=1}^{K} \operatorname{Tr}\left(Q_{k}\right)=P\right\} \log \left|I+\sum_{k=1}^{K} H_{k}^{\dagger} Q_{k} H_{k}\right|
\end{aligned}
$$

where $H_{k}^{\dagger}$ denotes Hermitian (conjugate transpose) of channel matrix $H_{k}, P$ is the sum of average transmit power from all mobile users, $Q_{k}$ is the transmit covariance matrix of the $k t h$ mobile user and $I$ is the identity matrix. If channel state information (CSI) is not available at the transmitter, then a good approach is to distribute power equally for all transmit antennas [4]. For many channel conditions $\left(H_{1}, H_{2}, \ldots, H_{K}\right)$, disabling some users and allocating the total average power $P$ to transmitting users results in higher sum rate capacity. Let us denote by $\phi$ a particular selection of users; we define $\phi$ to be the set of mobile users selected for transmission in the time block. Then, the sum rate capacity of the selected users
$\left.C_{\text {sum }}\left(\phi, H_{1}, H_{2}, \ldots, H_{K}\right)=\left\{\right.\right.$ s.t. $\left.\sum_{k \in \phi}^{\max _{\{0\}, l \in \phi\}} \operatorname{Tr}\left(Q_{k}\right)=P\right\} \log \left|I+\sum_{k \in \phi} H_{k}^{\dagger} Q_{k} H_{k}\right|$
can be larger than (2). The main issue of this paper is how to determine selection $\phi$ so that the sum rate capacity is maximized for a given value of $\left(H_{1}, H_{2}, \ldots, H_{K}\right)$.

We denote by $\Phi$ the collection of all possible user selections. Then, the number of possible ways of selecting the users is $|\Phi|=\sum_{i=1}^{K}\binom{K}{i}$. We denote by $\phi$ a collection of selected users. We can model user scheduling problem as a combinatorial optimization problem

$$
\begin{aligned}
& \max _{\phi \in \Phi} C_{\max }\left(\phi, H_{1}, H_{2}, \ldots, H_{K}\right) \quad \text { or } \\
& \max _{\phi \in \Phi} \log \left|I+\sum_{k \in \phi} H_{k}^{\dagger} Q_{k} H_{k}\right|
\end{aligned}
$$

We also denote $\phi^{*}=\underset{\phi \in \Phi}{\arg \max } C_{\text {sum }}\left(\phi, H_{1}, H_{2}, \ldots, H_{K}\right)$ where $\phi^{*}$ is the optimum of the objective function $C_{\max }\left(\phi, H_{1}, H_{2}, \ldots, H_{K}\right)$. We represent each selection $\phi$ by binary a string

$$
\Upsilon=\left[\varepsilon_{i}, \varepsilon_{2}, \ldots, \varepsilon_{K}\right], \varepsilon_{i} \in\{0,1\}
$$

where $\varepsilon_{i}$ is a binary indicator of whether user $i$ is selected or not from the $K$ users. For example, let us consider a case with $K=9$. Suppose that the first, third, fifth, sixth and ninth
![img-0.jpeg](img-0.jpeg)

Fig. 1: Block diagram of multiuser MIMO communication system.
![img-1.jpeg](img-1.jpeg)

Fig. 2: The basic initialization of EDA (cyclic shifted operation on adjacent users)
users are selected from these $K=9$ users. Then $\phi$ representing this selection will be $[1,0,1,0,1,1,0,0,1]$. In this paper, we will consider imposing another restriction to $\Phi$. We will consider the case that the system cannot schedule more than $K_{s}$ users to transmit together, possibly due to the limitation of real-time signal processing capability at the base station for multiuser detection.

Exhaustive Search Algorithm (ESA) evaluates all possible $|\Phi|$ selections. Enumerating over all possible combinations and finding the one that achieves maximization (3) is computationally inefficient. Computational complexity increases exponentially with the number of users. A computationally efficient (polynomial-time) algorithm is not known. High-speed communications demand user scheduling scheme with lower complexity. In the next section we will describe the EDA based user scheduling scheme.

## III. ESTIMATION OF DISTRIBUTION ALGORITHM (EDA) FOR USER SELECTION

In this section we present a user-scheduling scheme that utilizes Estimation of Distribution Algorithm (EDA) [11]. In general, conventional EDAs can be characterized by parameters and notations $\left(I_{s}, F, \Delta_{i}, \eta_{i}, \beta_{i}, p_{i}, D_{i s}, I_{t s s}\right)$, where

1. $I_{s}$ is the space of all potential solutions (entire search space of individuals).
2. $F$ denotes a fitness function.
3. $\Delta_{i}$ is the set of individuals (population) at the $l_{\text {th }}$ iteration.
4. $\eta_{i}$ is the set of best candidate solutions selected from

set $\Delta_{i}$ at the $l_{\text {th }}$ iteration.
5. We denote $\beta_{i} \equiv \Delta_{i}-\eta_{i} \equiv \Delta_{i} \cap \eta_{i}^{\prime}$, where $\eta_{i}^{\prime}$ is the complement of $\eta_{i}$.
6. $p_{i}=\left|\eta_{i}\right| j\left|\Delta_{i}\right|$ is called selection probability.
7. $D_{i n}$ is the distribution estimated from $\eta_{i}$ (the set of selected candidate solutions) at each iteration.
8. $I_{f, n}$ are the maximum number of iteration

In conventional EDA each individual is designated by a binary string of length $n$ ( $n$-dimensional binary vector). We denote by a binary row vector $X=\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right\}, x_{i} \in\{0,1\}$ as an individual. In each iteration, an EDA maintains a population of $\left|\Delta_{i}\right|$ individuals. Population $\Delta_{i}$ can be specified by the following matrix

$$
X=\left(\begin{array}{c}
X^{1} \\
X^{2} \\
\vdots \\
X^{\left|\Delta_{i}\right|}
\end{array}\right)=\left(\begin{array}{cccc}
x_{1}^{1} & x_{2}^{1} & \vdots & x_{n}^{1} \\
x_{1}^{2} & x_{2}^{2} & \vdots & x_{n}^{2} \\
\cdots & \cdots & \cdots & \cdots \\
x_{1}^{\left|\Delta_{i}\right|} & x_{2}^{\left|\Delta_{i}\right|} & \vdots & x_{n}^{\left|\Delta_{i}\right|}
\end{array}\right)
$$

where superscript $j$ in the row vector $X^{j}=\left(x_{i}^{j}, x_{2}^{j}, x_{3}^{j}, \ldots, x_{n}^{j}\right)$ indexes an individual in the population. A typical EDA is described in the following steps:

Step 0: Generate initial population $\Delta_{n}$. (Note: later in this section we will present different methods to generate initial population). The initial population ( $\left|\Delta_{n}\right|$ individuals) is typically obtained by sampling according the uniform distribution [11]:

$$
\begin{aligned}
p\left(X^{j}\right)= & \prod_{i=1}^{n} p\left(x_{i}^{j}\right) \quad \forall j=\left\{1,2, \ldots,\left|\Delta_{n}\right|\right\}, \\
& \text { and } p\left(x_{i}=1\right)=p\left(x_{i}=0\right)=0.5, \\
& i=1,2, \ldots, n
\end{aligned}
$$

For iterations $l=1,2, \ldots$ follow steps 1 through 6
Step 1: Evaluate the current population $\Delta_{i}$, according to the fitness function F. Sort the candidate solutions (individuals in the current population) according to their fitness orders. Keep the track of the best individual.

Step 2: If the best candidate solution satisfies the convergence criterion or the number of iterations exceeds its limit then terminate; else go to step 3.

Step 3: Select the best $\left|\eta_{i-1}\right|$ candidate solutions (individuals) from current $\left|\Delta_{i-1}\right|$ populations. This selection is accomplished according to the sorted solutions.

Step 4: Estimate the probability distribution $P\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ on the basis of $\left|\eta_{i-1}\right|$ best candidate solutions. We denote this estimation by

$$
D_{i n}=P\left(x_{1}, x_{2}, \ldots, x_{n} \mid \eta_{i-1}\right)
$$

Step 5: Generate new $\left|\Delta_{i-1}\right|-\left|\eta_{i-1}\right|$ individuals on the basis of
this new estimated probability distribution $D_{i n}$. Replace the bad $\left|\beta_{i-1}\right|$ individuals with newly generated $\left|\Delta_{i-1}\right|-\left|\eta_{i-1}\right|$ individuals.

Step 6: Go to step 1 and repeat the steps
For user-scheduling problem, the fitness function required by EDA is the function to be maximized in (3). We followed all the steps as discussed above for an EDA implementation for user-scheduling problem. In our experimentation, for estimation (7), we used a simple heuristic scheme of estimating the marginal distribution $P\left(x_{i} \mid \eta_{i-1}\right)$ of individual random variables $x_{i}, i=1,2, \ldots, n$, separately and using product form $D_{i n}=P\left(x_{1}, x_{2}, \ldots, x_{n} \mid \eta_{i-1}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid \eta_{i-1}\right)$. $P\left(x_{i}=1 \mid \eta_{i-1}\right)$ is estimated by simply counting the number of individuals with $x_{i}=1$ from the set of $\eta_{i-1}$ selected individuals and dividing it by the size of this set $\left|\eta_{i-1}\right|$. The simulation results show that the performance of EDA is better than previously proposed algorithms. We also propose an improved algorithm, and the next subsection presents the improved EDA algorithm.

In this paper we also propose three modifications in conventional EDAs to improve the efficiency of the proposed user scheduling. The modifications are 1) A predefined initial feed 2) Cyclic shifted initial population and 3) Weighted Estimation of Distribution. In conventional EDAs initial population is generated randomly from the uniform distribution. We present a scheme of selecting an initial population to make the average convergence time shorter than the randomly generated initial population. The idea is to contrive the initial population by utilizing domain knowledge of the Multiuser MIMO system and the dynamics of the EDAs evolution. The main theme of this idea is to use a promising initial selection of users (initial feed), which is represented by a binary string $X^{0}$, and then to use cyclic shifts of this binary string $X^{0}$ as initial population. In the user scheduling problem, we set the length of binary string $X^{0}$ (dimension of vector $X^{0}$ ) to be the total number of users. Exemplary methods of choosing the initial feed include 1) adjacent user method and 2) Norm Based (NB) method.

Adjacent feed technique is illustrated in figure 2. The following example uses $K=7, K_{S}=3$ as the initial parameters to illustrate the idea of adjacent feed technique. In adjacent user feed, for user scheduling $K_{S}=3$ bits are set to one and placed adjacent to each other in the vector; e.g., vector ( $1,1,1$, $0,0,0,0)$ in the case of $K=7, K_{S}=3$ has three consecutive 1 's. In the next stage of initialization a cyclic shift is applied on these initial feeds as shown in figure 2. This cyclic shift process is used to generate the initial population from these initial feeds. The cyclically shifted initial population ensures that each user is selected the same number of times in the entire population of particles initially. This will also ensure unbiased user selection at the initialization. In Norm based feed, first the users with best channel conditions are selected as initial feed. In the next step of initialization a cyclic shift is applied to this to get initial population.

To obtain an acceptable solution (a near-optimum solution) in an efficient way, we also propose an idea of adding some skew in estimating the probability distribution from a population, which is a modification to (7). This skew can be added by giving more weights to the individuals in $\eta_{i-1}$ that have better fitness in estimating the probability distribution $P\left(x_{1}, x_{2}, \ldots, x_{n}\right)$. We now provide a brief overview of this idea. Note that estimation (7) is often implemented in the following simple way: $D_{i n}=\prod_{k=1}^{n} P\left(x_{i} \mid \Omega_{i}^{-1}\right)$, where $\Omega_{i}^{-1}=$ $\left(x_{i}^{2} \quad x_{i}^{2} \quad \cdots \quad x_{i}^{\left\|\eta_{i}\right\|}\right)^{T}$ is the $i_{\text {th }}$ column vector from matrix $X$ and $P\left(x_{i} \mid \Omega_{i}^{-1}\right)$ is the estimated probability from the selected $\left|\eta_{i-1}\right|$ individuals in the $(l-I)_{t h}$ iteration. The skewed estimation $\hat{D}_{i n}$ is

$$
\hat{D}_{i n}=\prod_{i=1}^{n} P\left(x_{i} \mid \hat{\Omega}_{i}^{-1}\right)
$$

where $\hat{\Omega}_{i}^{-1}$ is the biased column vector determined through point by point multiplication of weight vector $\omega=$ $\left[\begin{array}{lll}\omega_{1} & \omega_{2} & \cdots & \omega_{\left\|\eta_{i}\right\|}\end{array}\right]^{T}$ and $\Omega_{i}^{-1}$ i.e, $\quad \hat{\Omega}_{i}^{-1}=\left(\begin{array}{lllll}\omega_{1} & x_{1}^{1} & \omega_{2} & x_{2}^{2} & \cdots & \omega_{\left\|\eta_{i}\right\|} x_{i}^{\left\|\eta_{i}\right\|}\end{array}\right)^{T}$. These weights are applied in accordance with the fitness order of the selected population at the $(l-I)_{t h}$ iteration. The weights are normalized and calculated to satisfy the condition that $\omega_{\left\|\eta_{i}\right\|}>\ldots \omega_{2}>\omega_{1}$, and $\sum_{i=1}^{n} \omega_{i}=1$. The following equations give idea about weight calculation

$$
\begin{gathered}
\omega_{1}=\frac{\log \left(\left|\eta_{i}\right|\right)-\log (i)}{\sum_{i=1}^{n}\left[\log \left(\left|\eta_{i}\right|\right)-\log (i)\right]}, i=1,2, \ldots, \mid \eta_{i} \mid \\
\omega_{2}=\frac{\left|\eta_{i}\right|-i}{\sum_{i=1}^{n}\left[\left|\eta_{i}\right|-i\right]}, i=1,2, \ldots, \mid \eta_{i}
\end{gathered}
$$

To illustrate biased estimation of distribution idea in detail, assume that $\left|\Delta_{1}\right|=10$ and $\left|\eta_{i}\right|=5$ are defined as initial parameters. Generate initial population as describe in step and apply other steps of EDA. To calculate normalized weight we need the number of best population i.e., $\eta_{i}$. Use (9) to calculate $\left|\eta_{i}\right|=5$ normalized weights, we will get $\omega=$ $\left\{\begin{array}{lllll}0.0437 & 0.0972 & 0.1662 & 0.2634 & 0.4293\end{array}\right\}^{T}$, similarly for (10) the weights are $\omega=$ $\left\{\begin{array}{lllll}0.0667 & 0.1333 & 0.2000 & 0.2667 & 0.3333\end{array}\right\}^{T}$. It is observed from the above data that logarithmic weights from (9) produce more bias as compared to (10). Equation (9) and (10) satisfied the conditions $\omega_{\left\|\eta_{i}\right\|}>\ldots \omega_{2}>\omega_{1}$ and $\sum_{i=1}^{n} \omega_{i}=1$.The weights are used such that the largest weight will be used for best solution and smallest weight will be used for worst solution. Numerical results show that this biased weighted estimation of distribution algorithm is better in performance than other proposed EDAs.

## IV. SIMULATION RESULTS

For performance comparison, we present the simulation
results of the proposed EDA-based user scheduling. The channel is assumed to be quasi-static, and different channels in MIMO are assumed independent. The parameters used for simulations are selected such that the performance of EDA is evaluated for different search space sizes and signal to noise ratios.

Figure 3 shows the performance Optimal ESA, Random, best norm based, and EDA with different initialization schemes. The sum rate channel capacity is a random variable because it is a function of random channel condition $\left(H_{1}, H_{2}, \ldots, H_{K}\right)$. It is meaningful to consider the sum rate capacity's statistical properties. We consider its statistical behavior called outage capacity. We now briefly interpret the concept of outage capacity [14]. Sum-rate channel capacity in (3) is the tightest upper bound on the total of the bit rates at which the selected mobile users can convey information to the base station reliably (asymptotically error-free) under the assumption that channel gain $\left(H_{1}, H_{2}, \ldots, H_{K}\right)$ is fixed. For a given channel condition $\left(H_{1}, H_{2}, \ldots, H_{K}\right)$, as long as the sum rate $R$ is less than the sum-rate capacity $C_{\text {sum }}\left(\phi, H_{1}, H_{2}, \ldots, H_{K}\right)$, there exists a set of data rates $\left\{R_{i} \mid i \in \phi^{*}, \sum_{k \in \phi^{*}} R_{k}=R\right\}$ that the base station can allocate to the selected mobile users $i \in \phi^{*}$ in such a way that each mobile $i \in \phi^{*}$ can send information to the base station at rate $R_{i}$ reliably. That is, the transmitter of each user can asymptotically achieve error-free communication through implementing error correction codes theoretically (according to information theory). On the other hand, if the sum rate $\sum_{k \in \phi^{*}} R_{k}$ is larger than sum-rate capacity $C_{\text {sum }}\left(\phi, H_{1}, H_{2}, \ldots, H_{K}\right)$, then there is no way that error-free communication can take place. Let us note that channel condition $H \equiv\left(H_{1}, H_{2}, \ldots, H_{K}\right)$ is randomly time-varying from code block to code block. Suppose that the transmitters are configured to always send information at total rate $R$ user bits per channel use and $R>C(H)$, then information theory also tells us that the block of user bits sent in that time interval will contain some bit error at some time due to randomness of $H$. The event $R>C(H)$ is referred to as an outage and $P[R>C(H)]$ is called outage probability. The $\alpha$-outage capacity $C_{\alpha}$ is defined as the maximal $R$ that keeps the outage probability under $\alpha$. That is, $C_{\alpha} \equiv \max \{R[P[R>C(H)] \leq \alpha\}$ $C_{\alpha} \equiv \max \{R[P[R>C(H)] \leq \alpha\}$.

Figure 3 shows the $10 \%$ outage capacity versus the signal to noise ratio (SNR) for $K=18, K_{S}=5, N_{T}=2$ and $N_{R}=2$. The population size of EDA is 18 and number of iterations is 10 . The figure shows that capacity achieved by the proposed algorithm is close to the optimal (ESA) and is better than other algorithms for all values of signal to noise ratio.

![img-4.jpeg](img-4.jpeg)

Fig. 3. Performance of Estimation of Distribution Algorithm for user-scheduling. The parameters are $K=18, K_{s}=5, N_{f}=2$ and $N_{R}=2$
![img-5.jpeg](img-5.jpeg)

Fig. 4. Performance of Estimation of Distribution Algorithm for userscheduling. The parameters are $K=24, K_{s}=4, N_{f}=2$ and $N_{R}=2$.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Sum rate Outage Capacity versus number of selected users.
Figure 4 also shows the $10 \%$ outage capacity versus the signal to noise ratio (SNR) for $K=24, \quad K_{s}=4, \quad N_{f}=2$ and $N_{R}=2$. The population size of EDA is 24 and number of iterations is 10 . The figure shows that capacity achieved by the
proposed algorithm (EDA) is close to the optimal (ESA) and is better than other algorithms for all values of signal to noise ratio. One interesting result in both figures is that the performance of the proposed algorithm becomes more significant at high SNR.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Sum rate Capacity versus iterations of various EDA Algorithms.

Figure 5 shows the performance EDA and other algorithms for different number of selected users. The figure shows the $10 \%$ outage capacity versus $K_{s}$ for fixed $S N R=20 d B$, $K=18, N_{f}=2$ and $N_{R}=2$. The population size of EDA is 18 and number of iterations is 10 .The figure shows that capacity achieved by the proposed algorithm is close to the optimal (ESA) and is better than other algorithms for all values selected users.

Figure 6 shows the performance of different EDA algorithms with $S N R=20 d B, K=16, K_{s}=5 N_{f}=2$ and $N_{R}=2$. The figure shows that capacity achieved by the proposed weighted EDA is better than adjacent-feed and randomly initialize EDA.

In this paper we consider the number of complex multiplications and additions as a measure of computational complexity. The exhaustive search algorithm needs to compute $\sum_{i=1}^{K}\binom{K}{i}$ complex determinants and each determinant require (1/3) $\cdot n^{3}$ complex multiplications and additions [9]. The Norm$\cdot$ based method require $2 K N_{R} N_{f}$ complex multiplications and additions. EDA needs to compute $\left(\Delta I_{r o}\right)$ determinants therefore it requires $N_{R}^{3} / 3\left(\Delta I_{r o}\right)$ complex multiplications and addictions. BD based scheduling require approximately $K\left(48 N_{R}^{3} N_{f}+24 N_{R} N_{f}^{3}+54 N_{R}^{3}+2 N_{R}^{3}+8 N_{R}\right)$ complex multiplications and additions [7].In modern communication and signal processing systems, dedicated DSP processors are used for complex multiplications and additions. For testing feasibility for practical implementation, in table 1 we present the time required by each algorithms for different parameter settings (i.e., different search space size).

TABLE 1
Computation complexity of user scheduling with TI DSP processor C67xx series having a capability of 500 millions multiplications and additions per second (MMACS)

| Parameters <br> $\left[K, K_{s}, N_{s}, N_{d}, \Delta, t\right]$ | Exhaustive <br> Search Algorithm | Norm | BD | EDA |
| :--: | :--: | :--: | :--: | :--: |
| $[18,5,2,2,18,10]$ | 67 us | 0.28 us | 37 us | 0.96 us |
| $[24,4,2,2,24,10]$ | 69 us | 0.38 us | 49.5 us | 1.28 us |
| $[20,10,2,2,20,10]$ | 3.3 ms | 0.32 us | 41.28 us | 1.068 us |
| $[25,8,3,2,25,10]$ | 9.6 ms | 60.0 us | 0.366 ms | 1.33 us |
| $[30,10,3,2,30,10]$ | 0.2827 s | 72.0 us | 0.4423 ms | 1.6 us |

The time is calculated for Texas Instruments DSP processor C67XX series with the capability of 500 millions multiplications and additions per second (MMACS). It is clear from the time comparison that EDA requires less time that ESA and BD algorithm. The least time is required by norm base method but its performance is poor at high SNR.

## V. CONCLUSION

In this paper, we have presented EDA for user-scheduling problem in multiuser MIMO system. The EDA for the userscheduling problem requires very low computation and its performance is close to that of the exhaustive search. The simple model, low implementation complexity, resistance to trap in local minima and convergence to a nearly optimal solution with a small number of iterations all make EDA a suitable candidate for solving complex communication problems like the user scheduling.

## REFERENCES

[1] G. J. Foschini and M. J. Gans, "On limits of wireless communications in a fading environment when using multiple antennas," Wireless Personal Communications, vol. 6, pp. 311-335, 1998.
[2] E. Telatar, "Capacity of Multi-antenna Gaussian Channels," European Trans. on Telecomm. vol. 10, pp 569-709, Nov. 1999.
[3] S. Vishwanath, N. Jindal, and A. Goldsmith, "Duality, achievable rates, and sum-rate capacity of Gaussian MIMO broadcast channels," IEEE Trans. Inform. Theory, vol. 49, pp. 2658-2668, Oct. 2003.
[4] Y. Zhang, C. Ji, Y. Liu, W. Q. Malik, D. C. O'Brien, and D. J. Edwards, "A low complexity user scheduling algorithm for uplink multiuser MIMO systems," IEEE Transactions on Wireless Communications, vol. 7, no. 7, pp. 2486-2491, Jul. 2008.
[5] Y. Zhang, C. Ji, W. Q. Malik, Y. Liu, D. C. O'Brien, and D. J. Edwards, "Joint antenna and user selection algorithm for uplink multiuser MIMO systems using sequential Monte Carlo optimization," IEEE Statistical Sig. Proc. Workshop (SSP). WI. USA, pp. 493-496, Aug. 2007.
[6] Z. Shen, J. G. Andrews, R. W. Heath, Jr., and B. L. Evans, "Low Complexity User Selection Algorithms for Multiuser MIMO Systems with Block Diagonalization, " IEEE Trans. on Signal Processing, vol. 54, no. 9, pp. 3658-3663, Sep. 2006.
[7] Zukang Shen, Runhua Chen, Jeffrey G. Andrews, Robert W. Heath, Jr., and Brian L. Evans, "Sum capacity of multiuser MIMO broadcast channel with block Diagonalization ," IEEE Transactions on Wireless Communications, vol. 6 no. 6, June 2007.
[8] C. Anton-Haro,P. Svedman, M. Bengtsson,A. Alexiou and A. Gameiro, "Cross-layer scheduling for multi-user MIMO systems," IEEE Communications Magazine, vol. 44, issue 9, pp. 39-45, Sept. 2006.
[9] G.H.Golub and C.F. VanLoan, Matrix Computations, The Johns Hopkins Univ. Press, 1983.
[10] A.E. Eiben and J.E. Smith, Introduction to Evolutionary Computing, Springer Verlag, 2003.
[11] P. Larrañaga and J. A Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Kluwer Academic Publishers, 2001.
[12] E. A. Yfantis, "Random number generator for electronic applications," U.S. Patent 5871400, Feb 16, 1999.
[13] Q. Zhang and H. Muehlenbein, "On the Convergence of a Class of Estimation of Distribution Algorithms," IEEE Trans. on Evolutionary Computation, vol. 8, no. 2, 2004.
[14] E. G. Larsson and P. Stoica, Space-Time Block Coding for Wireless Communications. Cambridge University Press, May 2003.