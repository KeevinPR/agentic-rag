# Probabilistic distribution learning algorithm based transmit antenna selection and precoding for millimeter wave massive MIMO systems 

Salman Khalid ${ }^{1}$ (1) $\cdot$ Rashid Mehmood ${ }^{2} \cdot$ Waqas bin Abbas ${ }^{1} \cdot$ Farhan Khalid ${ }^{1} \cdot$ Muhammad Naeem ${ }^{2}$

Accepted: 24 September 2020
(c) Springer Science+Business Media, LLC, part of Springer Nature 2020


#### Abstract

In modern day communication systems, the massive MIMO architecture plays a pivotal role in enhancing the spatial multiplexing gain, but vice versa the system energy efficiency is compromised. Consequently, resource allocation in-terms of antenna selection becomes inevitable to increase energy efficiency without having any obvious effect or compromising the system spectral efficiency. Optimal antenna selection can be performed using exhaustive search. However, for a massive MIMO architecture, exhaustive search is not a feasible option due to the exponential growth in computational complexity with an increase in the number of antennas. We have proposed a computationally efficient and optimum algorithm based on the probability distribution learning for transmit antenna selection. An estimation of the distribution algorithm is a learning algorithm which learns from the probability distribution of best possible solutions. The proposed solution is computationally efficient and can obtain an optimum solution for the real time antenna selection problem. Since precoding and beamforming are also considered essential techniques to combat path loss incurred due to high frequency communications, so after antenna selection, successive interference cancellation algorithm is adopted for precoding with selected antennas. Simulation results verify that the proposed joint antenna selection and precoding solution is computationally efficient and near optimal in terms of spectral efficiency with respect to exhaustive search scheme. Furthermore, the energy efficiency of the system is also optimized by the proposed algorithm, resulting in performance enhancement of massive MIMO systems.


Keywords Millimeter wave propagation $\cdot$ Hybrid (analog and digital)precoding $\cdot$ Estimation of distribution algorithm $\cdot$ Spectral efficiency $\cdot$ Exhaustive search $\cdot$ Random search $\cdot$ Transmit antenna selection

## 1 Introduction

The unification of millimeter wave (mmW) frequency band with massive MIMO is considered effective to fulfill the modern day data requirements [1,2]. The utilization of mmW frequency band is attaining considerable attention, however, the main disadvantage of systems operating at higher frequencies is extensive path loss. Precoding and beamforming are considered essential in mmW regime for enhancing the array gain with the aim to mitigate the extensive path loss and establish acceptable signal to noise ratio (SNR) for reliable communication. With the aim to reap the maximum allowance of spatial multiplexing, fully digital precoding

[^0]systems incorporating an independent radio frequency (RF) chain for each antenna element are considered but practically they are not feasible due to complex structure and higher power consumption [3]. Analog precoding systems employing only a single RF chain can effectively manage the power consumption, but are not adopted due to lack of flexibility offered by digital systems. To effectively exploit the gain offered by digital processing techniques and achieve high energy efficiency, for a massive MIMO architecture, a hybrid precoding structure [4] realized by an analog and digital precoder has attained significant consideration. Researchers have generally considered two types of hybrid precoding architectures: (a) fully connected architecture, where every antenna element is connected to all RF chains and as a result the system can provide optimal spectral efficiency but comes with higher complexity and (b) partially sub connected architecture, where only a subgroup of antennas is connected to a corresponding RF chain resulting in a reduced spectral efficiency but higher computational efficiency. Researchers have


[^0]:    (1) Salman Khalid salmankhalid16@yahoo.com

    1 The National University of Computer and Emerging Sciences (NUCES), Islamabad, Pakistan

    2 COMSATS University, Wah Campus, Islamabad, Pakistan

proposed numerous precoding and beamforming techniques for both architectures. Precoder design for a fully connected architecture based on exploiting the sparsity of mmW channel using the orthogonal matching pursuit (OMP) algorithm is discussed in [5]. Alternating minimization techniques such as phase extraction (PE) and manifold optimization (MO), in which both the analog and digital precoder are alternatively optimized are presented in [6]. Both MO and OMP algorithms are implemented on a fully connected architecture and they approach the optimal theoretical limit of spectral efficiency, but both algorithms are computationally complex and are not suitable for practical systems. With the aim to optimize the computational complexity of the OMP algorithm based precoder, authors in [7] have proposed a bird swarm algorithm (BSA), which replaces the array response vector multiplied by residual inner product operation with an iterative search method. Researchers also have investigated the precoder design techniques for a partially connected architecture. One such technique is developed by incorporating successive interference cancellation (SIC) based algorithm [8]. Precoder designed using the SIC based algorithm is energy efficient and near optimum in terms of spectral efficiency. Precoder design using a particle swarm optimization (PSO) inspired by evolutionary algorithms is discussed in [9]. The analog precoder design by utilizing the signal to leakage noise ratio (SLNR) and digital precoder design by adopting the zero forcing (ZF) technique is discussed in [10]. In [11], authors have investigated the hybridly connected architecture and designed the precoder using a SIC based algorithm. In hybridly connected architecture the antennas are dynamically allocated to RF chains. Precoder based on singular value decomposition (SVD) is designed in [12]. Although the fully connected architecture is optimal in terms of spectral efficiency, the partially connected architecture is feasible for practical implementation owing to higer energy and computational efficiency.

Although the multiplexing gain can be achieved with higher dimensions of massive MIMO architecture, the consequences are also faced in terms of computational complexity. Antenna selection can be an effective way to overcome the complexity issues of massive MIMO architecture. Spectral efficiency increases significantly with the number of antennas. However, the gain gets almost constant beyond a certain limit, resulting in reduction of hardware efficiency and increase in power consumption of the system. Authors in [13] have demonstrated that a subset of available antennas can achieve $90 \%$ of ergodic rate achieved by full antennas. Ref. [14] demonstrates that in order to optimize the hardware, a selection procedure can be opted to choose the antennas experiencing good channel conditions. Authors proved that the advantage of multi-antenna diversity is not sacrificed using only the selected antennas, rather the system efficiency is increased. Exhaustive search (ES) algorithm is
the optimal way to choose the desired subset of available antennas. In ES scheme the algorithm iterates and evaluates all possible antenna combinations to select the desired combination that maximizes the spectral efficiency. However, such a scheme is computationally inefficient. An effective transmit antenna selection scheme is required to manage the frequently varying channel conditions for practical systems. Researchers have adopted minimum eigenvalue [15] and constrained cross entropy optimization (CCEO) [16] to choose the sub set of total available antennas. Inspired by the efficiency of evolutionary algorithms, authors in [17] and [18] have adopted binary version of particle swarm optimization (BPSO) algorithm for effective transmit and receive antenna selection. Reference [18] has applied the BPSO on user selection problem. For fully connected architecture, authors in [19] have performed joint antenna selection and precoding using sliding window index selection (SWIS) algorithm for antenna selection and adopting OMP algorithm for beamforming.

References [20] and [21] have performed joint transmit and receive antenna selection by adopting ant colony optimization and adaptive markov chain monte carlo algorithm respectively. [22] performs transmit antenna selection based on euclidean distance. In [23] survey article, the performance comparison of a transmit antenna selection system with different kinds of receiver architectures is discussed. Authors in [24] have investigated antenna selection methods for bidirectional full-duplex MIMO systems in which antennas at each node can be selected to either transmit or receive configuration. The user scheduling problem using the probabilistic model is discussed in [25]. In [26], for cooperative cognitive radio networks, authors have applied the cross entropy (CE) optimization for multiple relay assignment and power allocation. The resource management for D2D communication using the probabilistic algorithm is performed in [27]. In [28], for low resolution ADCs, authors have compared different beamforming (digital, analog and hybrid) architectures at receiver to study the spectral and energy efficiency tradeoff. This work extends the idea of the probabilistic model and applies the theory on the antenna selection problem aimed for partially connected massive MIMO architecture. Table 1 presents the summary of related work.

In order to efficiently operate the massive MIMO systems in mmW regime, joint application of antenna selection and precoding to achieve optimal energy efficiency and combat path-loss is essential. Also since the channel conditions change rapidly, the proposed algorithm should be computationally efficient to manage the rapid changes. However, most of the existing literature does not present the joint solution for antenna selection and precoding. So motivated by this fact, to improve the system efficiency of a massive MIMO partially connected architecture, we have developed a low complexity solution for joint antenna selection and precod-

Table 1 Literature review summary

| Paper | Structure Fully connected | Partially connected | Frequency Band <br> Microwave | mmWave | Antenna Selection | Algorithm |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| [5] | $\checkmark$ |  |  | $\checkmark$ |  | OMP |
| [6] | $\checkmark$ |  |  | $\checkmark$ |  | MO, PE |
| [7] | $\checkmark$ |  |  | $\checkmark$ |  | Heuristic |
| [8] |  | $\checkmark$ |  | $\checkmark$ |  | SIC |
| [9] |  | $\checkmark$ |  | $\checkmark$ |  | Heuristic |
| [10] |  | $\checkmark$ |  | $\checkmark$ |  | SLNR, ZF |
| [11] | $\checkmark$ | $\checkmark$ |  | $\checkmark$ |  | SIC |
| [12] | $\checkmark$ |  |  | $\checkmark$ |  | SVD |
| [14] | $\checkmark$ |  | $\checkmark$ |  | $\checkmark$ | CBM |
| [15] |  | $\checkmark$ | $\checkmark$ |  | $\checkmark$ | Minimum Eigen value |
| [16] | $\checkmark$ |  | $\checkmark$ |  | $\checkmark$ | CCEO |
| [17] |  | $\checkmark$ | $\checkmark$ |  | $\checkmark$ | Heuristic |
| [18] |  | $\checkmark$ | $\checkmark$ |  | $\checkmark$ | Heuristic |
| [19] | $\checkmark$ |  |  | $\checkmark$ | $\checkmark$ | Hybrid OMP |
| [20] |  | $\checkmark$ |  | $\checkmark$ | $\checkmark$ | Heuristic |
| [21] | $\checkmark$ |  |  | $\checkmark$ | $\checkmark$ | AMCMC |
| [25] | $\checkmark$ |  |  | $\checkmark$ | $\checkmark$ | Probability distribution |
| This paper |  | $\checkmark$ |  | $\checkmark$ | $\checkmark$ | Hybrid heuristic |

ing. Firstly, antenna selection scheme based on probabilistic distribution learning is applied for transmit antenna selection, and secondly, precoder for selected antennas based on SIC algorithm is designed to reduce signal attenuation and mitigate path loss. Summarized below are the main contributions of this work.

- For a partially connected hybrid massive MIMO architecture, a combination of novel learning based scheme i.e., Bayesian approach based estimation of distribution algorithm (EDA) for transmit antenna selection and SIC based precoding is proposed. The EDA is a learning algorithm, which learns the probability distribution of the best possible solution to update the samples. In EDA, the process of mutation and crossover is replaced by a Bayesian learning approach and a new population is generated on the basis of probability distributions learned from previous iterations. EDA can also evaluate the candidates simultaneously using parallel processing instead of sequential manipulations. The parallel processing capabilities can speed up the computations. Also, the tuning parameters are not required in EDA as compared to other evolutionary algorithms.
- In terms of computational complexity, hybrid learning based algorithms achieves optimal performance compared to exhaustive search without any performance hit in terms of spectral efficiency.
- The joint antenna selection and precoding based architecture optimizes the energy efficiency of the system.
- The proposed system can adapt to imperfect channel state information (CSI) and can achieve robustness in the presence of channel estimation errors.


## 2 System model

We have considered a partially connected sub array structure for a mmW massive MIMO system as depicted in Fig. 1, where the base station is equipped with $N_{S}$ number of data streams and $N_{R F}$ RF chains. $M_{T}$ antennas are connected to each RF chain, hence the total number of transmit antennas are $N_{T}=N_{R F} \times M_{T}$. The mmW channel for massive MIMO transmitter and receiver is represented by $\mathbf{H} \in C^{N_{R} \times N_{T}}$, where $N_{R}$ is the number of receive antennas. Based on this channel state information (CSI), the $M_{t}$ best antennas for each RF chain are selected. Hence, the system is reduced with a total of $N_{t}$ transmit antennas experiencing good channel conditions.

Since the propagation environment of mmW channel has a limited scatterers, channel matrix $\mathbf{H}$ at mmW frequencies does not follow the rich scattering model adopted for lower frequencies. Consequently, we have adopted the geometric Saleh-Valenzuela model to design the low rank mmW channel [29].

![img-0.jpeg](img-0.jpeg)

Fig. 1 System model for joint antenna selection and precoding
$\mathbf{H}=\sqrt{\left(\frac{N_{T} N_{R}}{\epsilon L}\right)} \sum_{l=0}^{L} \eta_{l} \mathbf{a}_{R}\left(\mu_{l}\right) \mathbf{a}_{T}^{H}\left(\theta_{l}\right)$
where $\mathbf{H}$ represents the channel matrix, $L$ represents the number of effective channel paths linked with limited number of scatterers, $\epsilon$ is the path loss, $\eta_{l}$ is the complex gain associated with the $l$ th path, $\mathbf{a}_{R}$ and $\mathbf{a}_{T}$ represents the transmitter and receiver spatial signatures respectively, and $\mu_{l}$ and $\theta_{l}$ represent the angle of arrival (AoA) and the angle of departure (AoD) of the $\mu_{l}$ th path respectively. For a Uniform Linear Array (ULA) structure the spatial signatures of transmitter and receiver can be expressed as
$\mathbf{a}_{R}(\mu)=\frac{1}{\sqrt{N_{R}}}\left[1, \exp ^{i \frac{2 \pi}{N_{T}} d \sin (\mu)}, \ldots, \exp ^{j\left(N_{R}-1\right) \frac{2 \pi}{N_{T}} d \sin (\mu)}\right]^{T}$
$\mathbf{a}_{T}(\theta)=\frac{1}{\sqrt{N_{T}}}\left[1, \exp ^{i \frac{2 \pi}{N_{T}} d \sin (\theta)}, \ldots, \exp ^{j\left(N_{T}-1\right) \frac{2 \pi}{N_{T}} d \sin (\theta)}\right]^{T}$
where $\lambda$ is the wavelength of the signal and $d$ is the spacing between the antennas. Prior to antenna selection and precoding, the spectral efficiency of system is expressed as
$R=\log \left(\mathbf{I}_{N_{R}}+\frac{\rho}{N_{s}} \mathbf{H}(\mathbf{H})^{H}\right)$
$\boldsymbol{\Phi}=\binom{N_{T}}{N_{t}}$ denotes the collection of all possible combinations to select transmit antennas. A set of antennas selected from the parent set is denoted as $\boldsymbol{\Phi}$. As a result of antenna selection, the channel matrix is reduced as $\mathbf{H}^{\phi} \in C^{N_{R} \times N_{t}}$. The channel spectral efficiency after the antenna selection is expressed as
$R=\log \left(\mathbf{I}_{N_{R}}+\frac{\rho}{N_{s}} \mathbf{H}^{\phi}\left(\mathbf{H}^{\phi}\right)^{H}\right)$
Where $\rho$ is the average signal to noise ratio (SNR) of the channel and $\mathbf{I}_{N_{R}}$ is a $N_{R} \times N_{R}$ identity matrix. Selected transmitting are operating at same power. The transmit antenna selection is a optimization problem expressed as
$\arg \max _{\phi \in \Phi} \phi R=\arg \max _{\phi \in \Phi} \log \left(\mathbf{I}_{N_{R}}+\frac{\rho}{N_{s}} \mathbf{H}^{\phi}\left(\mathbf{H}^{\phi}\right)^{H}\right)$
A binary string can be used to represent each selection $\phi$. Let $q_{i}$ be the binary indicator for selection of $i^{\text {th }}$ transmit antenna out of total $N_{T}$ antennas. Then the binary string for $N_{T}$ antennas is given as
$Q=\left\{q_{1}, q_{2}, q_{3}, \ldots, q_{N_{T}}\right\}, q_{i} \in\{0,1\}, \forall i$
ES algorithms evaluates all combinations of $\boldsymbol{\Phi}$ set and selects the best on basis of spectral efficiency maximization. Since all the options are evaluated, ES is termed as optimal algorithm, but evaluating all combinations make ES computationally expensive. For real time massive MIMO systems, a computationally efficient algorithm for antenna selection is inevitable. After selecting the desired antennas, precoding only for reduced system is carried out. As preciously discussed, precoding is essential to combat path loss and provide spatial gain for systems operating in mmW regime. Both digital and analog precoding are not desired due to complexity and efficiency constraints, hence the hybrid precoding techniques are considered appropriate. The complete system flow chart presenting joint antenna selection and precoding is shown in Fig. 2.

## 3 Transmit antenna selection schemes

Now we discuss the antenna selection schemes based on proposed algorithm (EDA), Random Search (RS) and ES. The ES algorithm gauges all possible combinations of the transmit antenna connected to $N_{R F}$ RF Chains $\left(\boldsymbol{\Phi}=\binom{M_{T}}{M_{t}} \times N_{R F}\right)$ and to maximize the spectral efficiency selects the optimal combination $(\boldsymbol{\phi})$. First, all the possible combinations of antenna selection possibilities are generated and afterwards ES evaluates the combinations sequentially and selects optimal which gives highest spectral efficiency. But such evaluation is not desired for real time implementation due to complexity issues. The ES algorithm is presented in

![img-1.jpeg](img-1.jpeg)

Fig. 2 Flow chart of proposed algorithm

Algorithm 1. RS algorithm randomly generates an antenna combination for processing. Spectral efficiency is not optimal due to random nature of RS. In order to jointly optimize the computational complexity and spectral efficiency, an efficient selection algorithm is required.

```
Algorithm 1 Exhaustive Algorithm for Joint Transmit
Antenna Selection and Precoding
    (Step 1) Generate all possible combinations \(\boldsymbol{\Phi}\) applicable for selecting
    \(M_{l}\) transmit antennas out of total \(M_{T}\) antennas for \(N_{R F}\) RF chain. \(\Phi\)
    \(=\binom{\Phi_{T}}{\Phi_{T}} \times N_{R F}\)
    (Step 2) Apply SIC based precoding on every combination of selected
antennas. Where \(\mathbf{F}=\mathbf{A} \times \mathbf{D}\) is the precoding matrix with \(\mathbf{A}\) is the ana-
    log precoding matrix and \(\mathbf{D}\) being the digital or baseband precoding
    matrix \(\forall \phi \in \Phi\)
    \(R\left(H^{\phi}\right)=\log \left(\mathbf{I}_{N_{R}}+\frac{\rho}{N_{s}} \mathbf{H}^{\phi} \mathbf{F F}^{H}\left(\mathbf{H}^{\phi}\right)^{H}\right)\)
```

(Step 3) After applying joint antenna selection and precoding scheme, select the combination that maximizes the spectral efficiency.
$\arg \max _{\phi \in \Phi} R=\arg \max _{\phi \in \Phi} \log \left(\mathbf{I}_{N_{R}}+\frac{\rho}{N_{s}} \mathbf{H}^{\phi} \mathbf{F F}^{H}\left(\mathbf{H}^{\phi}\right)^{H}\right)$

### 3.1 Bayesian approach based estimation of distribution algorithms

In this paper, we present the EDA based transmit antenna selection scheme for a partially connected massive MIMO hybrid architecture. The candidate or potential solutions to
a specific optimization problem are represented as samples. The value of an objective function implemented on a sample indicates the fitness of the individual. Unlike other popular evolutionary algorithms like genetic algorithm, the samples in EDA are generated without employing the crossover and mutation operations. Instead, in EDA a Bayesian approach is utilized to generate the new samples which is based on probability distribution estimated from the best performing samples of the previous iteration. EDA is characterized by the notations $\left(I_{s s}, F F, I_{l}, \alpha_{l}, p_{s}, \beta_{l}, N_{I t e r}\right)$, which are described as

- $I_{\text {ss }}$ represents the entire solution space.
- FF represents the fitness function also known as objective function.
- $I_{l}$ represents the samples at the $l_{t h}$ iteration.
- $\alpha_{l}$ represents the best solutions selected from set $I_{l}$ at the $l_{t h}$ iteration.
- $p_{s}$ represents the selection probability.
- $\beta_{l}$ represents the distribution which are estimated from $\alpha_{l}$ at the $l_{t h}$ iteration.
- $N_{\text {Iter }}$ represents the maximum number of iterations.

Each EDA sample is represented by a binary vector of dimension $N_{T}$. We denote a binary row vector $\mathbf{x}=$ $\left(x_{1}, x_{2}, \ldots, x_{N_{T}}\right), x_{i} \in(0,1)$ as an agent. Here, ' 0 ' and ' 1 ' represents whether a specific antenna is selected or not. The complete samples can be represented as a matrix specified below.

$$
\mathbf{x}=\left(\begin{array}{c}
\mathbf{x}^{\mathbf{1}} \\
\mathbf{x}^{\mathbf{2}} \\
\vdots \\
\vdots \\
\mathbf{x}^{\mathbf{h}}
\end{array}\right)=\left(\begin{array}{cccc}
x_{1}^{1} & x_{2}^{1} & \ldots & x_{N_{T}}^{1} \\
x_{1}^{2} & x_{2}^{2} & \ldots & x_{N_{T}}^{2} \\
\vdots & \vdots & \ddots & \vdots \\
x_{1}^{I_{l}} & x_{2}^{I_{l}} & \ldots & x_{N_{T}}^{I_{l}}
\end{array}\right)
$$

where the superscript $j \in\left(1,2, \ldots, I_{l}\right)$ in the row vector $\mathbf{x}^{\mathbf{j}}=\left(x_{1}^{j}, x_{2}^{j}, \ldots, x_{N_{T}}^{j}\right)$ indexes an individual in the sample. Each typical candidate solution to the antenna selection problem is represented by a binary row vector $\mathbf{x}=$ $\left(x_{1}, x_{2}, \ldots, x_{N_{T}}\right)$. The algorithm is summarized in Algorithm 2.

```
Algorithm 2 EDA for transmit antenna selection
    Initialize Number of samples, Iterations, Total Desired Antennas
    (Step 1) Generate the initial set of samples as per the dimensions of
    system \(I_{0}\). The initial samples are randomly generated according the
    uniform (equally likely) distribution.
\(p\left(\theta_{1}, \theta_{2}, \ldots, \theta_{N_{T}}\right)=\prod_{i=1}^{N_{T}} p_{i}\left(\theta_{i}\right)\),
\(p_{i}\left(\theta_{i}=1\right)=p_{i}\left(\theta_{i}=0\right)=0.5, i=1,2, \ldots, N_{T}\)
```

For iterations $l=1,2, \ldots$, follow Step 2 through Step 6:
(Step 2) Evaluate the current samples $I_{l-1}$ using the objective or fitness function $F F$ as given in Eq. (5). Sort the samples (solutions) in accordance with the value of the fitness function.
(Step 3) If the convergence criteria is satisfied or the iterations have reached the maximum limit $N_{I t e r}$, then terminate, otherwise perform Step 4
(Step 4) Select $\alpha_{l-1}$ best candidate solutions form the current samples $I_{l-1}$. This selection is done in accordance to the sorted candidate on the basis of fitness value.
(Step 5) Estimate the probability distribution $p\left(\theta_{1}, \theta_{2}, \ldots, \theta_{N_{T}}\right)$ on the basis of $\alpha_{l-1}$ best solutions and is denoted by
$\beta_{l-1}=P\left(\theta_{1}, \theta_{2}, \ldots, \theta_{N_{T}} \mid \alpha_{l-1}\right)$
(Step 6) Generate new $I_{l}-\alpha_{l-1}$ samples on the basis of estimated probability distribution $\beta_{l-1}$.
(Step 7) In randomly generating new individuals, if the number of 1's are more than the desired number of transmit antennas than randomly select the extra 1's and replace them with 0's so that the total number of selected antennas remains constant.
(Step 8) Combine the newly generated $I_{l}-\alpha_{l-1}$ with the members of $\alpha_{l-1}$ to form the new samples $I_{l}$.
(Step 9) Go to Step 1 and repeat the steps.

The fitness function for the antenna selection problem is the spectral efficiency expression as shown in Eq. (5). Using steps mentioned in Algorithm 2 and the fitness function we evaluate and determine the best subset of antennas out of the total available transmit antennas. In addition, we are able to further improve the performance of EDA by applying the
threshold on the probability distributions so that the algorithm does not get stuck in the local minimum or maximum.
(1) Threshold Method A typical EDA may be stuck in the local minimum or maximum due to premature convergence of probability distributions, or the solution can be slowed down due to non convergence. The issue is due to the fact that during the execution, some probabilities become 0 or very close to 0 in the early stage of the algorithm. In this situation, the algorithm is unable to completely explore the solution space. For example every individual in the row vector $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{N_{T}}\right)$ in the set happens to be 0 i.e $x_{i}=0$. As a result the probability distribution gives 0 probability of drawing a candidate with $x_{i}=1$ in sample $I_{l+1}$ and so there is no chance of drawing a candidate with $x_{i}=1$ in future generations. Hence, in this scenario the $i$ th component is stuck with the value 0 and so the solution with value 1 for the $i$ th component is never explored by the algorithm. We present the method of applying threshold as a solution to these type of problems. In order to cope with the premature convergence, the probabilities are adjusted after each iteration. At any iteration, if the probability value $P\left(\theta_{i}=1 \mid \alpha_{l-1}\right), \mathrm{i}=1,2, \ldots, \mathrm{n}$ is greater than $\gamma_{i}$, that value is set to $\gamma_{i}$, i.e. $P\left(\theta_{i}=1 \mid \alpha_{l-1}\right)=\gamma_{i}$. So the randomness is also not compromised. Similarly, the issue that a probability value prematurely converges to 0 can be sorted out in the same way by a applying lower threshold and adjusting the probability distributions.

## 4 Precoding using SIC based algorithm

For the sub-connected structure SIC based precoding is proved to be optimal for both computational and spectral efficiency [8]. For the system model presented in Fig. 1, the $N_{s}$ data streams which are input to the base station are precoded by an $N_{R F} \times N_{s}$ digital precoder $\mathbf{D}=\operatorname{diag}\left[d_{1}, d_{2}, \ldots\right.$, $\left.d_{N}\right]$, where $d_{n} \in R$, followed by an $M_{t} \times 1 \mathrm{RF}$ precoder $\mathbf{a}_{n}(\mathrm{n}=1, \ldots, \mathrm{~N}) \in \mathcal{C}^{M_{t} \times 1}$ before transmission. For sake of simplicity we have kept both $N_{s}$ and $N_{R F}$ equal to $N$. Phase shifters with unity amplitude and variable phases constitute the RF precoder. Finally, each data stream is transmitted over the selected $M_{t}$ antennas connected to the corresponding RF chain. The received $N_{R} \times 1$ signal vector $\mathbf{y}$ is denoted as
$\mathbf{y}=\sqrt{P_{a v}} \mathbf{H}^{\phi} \mathbf{A D} \mathbf{s}+\mathbf{z}$
where $P_{a v}$ is the average received power, $\mathbf{s}$ presents the input vector transmitted using the selected antennas. Hybrid precoding matrix at the transmitter is realized as $\mathbf{F}=\mathbf{A D}$, with $\mathbf{A}=\left[\mathbf{a}_{1}, \mathbf{a}_{2}, \ldots, \mathbf{a}_{N}\right]$, being the RF precoder satisfying condition of total power constraint $\|F\|_{F}^{2} \leq N_{s}$.

Here, $\mathbf{z}=\left[z_{1}, z_{2}, \ldots, z_{N}\right]^{T}$ is complex i.i.d Gaussian noise, $\mathcal{C N}\left(0, \sigma^{2}\right)$. Matrix $\mathbf{H}^{\phi}$ denotes the reduced channel matrix after transmit antenna selection. [8] presents the comprehensive details of SIC based precoder design. System spectral efficiency after performing joint antenna selection and precoding is
$R=\log \left(\mathbf{I}_{N_{R}}+\frac{\rho}{N_{s}} \mathbf{H}^{\phi} \mathbf{F F}^{H}\left(\mathbf{H}^{\phi}\right)^{H}\right)$
SIC decomposes the achievable rate $R$ into reduced capacity for all antenna arrays. The spectral efficiency after decomposing $\mathbf{F}$ as $\mathbf{F}=\left[\mathbf{f}_{1}, \mathbf{f}_{2}, \ldots, \mathbf{f}_{n}\right]$, where $\mathbf{f}_{n}$ is the $n$th column of $\mathbf{F}$ is given as
$R=\sum_{n=1}^{N} \log \left(1+\frac{\rho}{N_{s}} \mathbf{f}_{n}^{H}\left(\mathbf{H}^{\phi}\right)^{H} \mathbf{T}_{n-1}^{-1} \mathbf{H}^{\phi} \mathbf{f}_{n}\right)$
where $\mathbf{T}_{n}=\mathbf{I}_{n}+\frac{\rho}{N_{s}} \mathbf{H}^{\phi} \mathbf{F}_{n} \mathbf{F}_{n}^{H}\left(\mathbf{H}^{\phi}\right)^{H}$ and $\mathbf{T}_{0}=\mathbf{I}_{N}$. Here, for each antenna array, we have converted the total capacity optimization problem into a reduced capacity optimization problem. Finally the achievable capacity is optimized by employing SIC algorithm on each antenna arrays and updating matrix $\mathbf{T}_{1}$. Finally the hybrid precoder for the $n$th antenna sub-array $\mathbf{f}_{n}^{o p t}$ is expressed as
$\mathbf{f}_{n}^{o p t}=\log \left(1+\frac{\rho}{N_{s}} \mathbf{f}_{n}^{H} \mathbf{G}_{n-1} \mathbf{f}_{n}\right)$
where $\mathbf{G}_{n-1}=\left(\mathbf{H}^{\phi}\right)^{H} \mathbf{T}_{n-1}^{-1} \mathbf{H}^{\phi}$. It is worth mentioning that the $n$th precoding vector $\mathbf{f}_{n}$ has only got $M_{t}$ non zero elements from $\left(M_{t}(n-1)+1\right)$ th to $\left(M_{t} n\right)$ th. The matrix $\mathbf{G}_{n-1}$ of size $M_{t} \times M_{t}$ is obtained using $\mathbf{G}_{n-1}=\mathbf{R}\left(\mathbf{H}^{\phi}\right)^{H} \mathbf{T}_{n-1}^{-1} \mathbf{H}^{\phi} \mathbf{R}$. Where $\mathbf{R}$ is a operator matrix to select $\left(M_{t}(n-1)+1\right)$ th to $\left(M_{t} n\right)$ th rows and columns for $n$th sub array. The SIC algorithm is presented in Algorithm 3.

```
Algorithm 3 Algorithm for SIC based precoding
    (Step 1) SVD operation on \(\mathbf{G}_{n-1}\) to obtain \(\mathbf{v}_{1}\). Here \(\mathbf{v}_{1}\) is the first
    column of unitary matrix \(\mathbf{V}\).
    (Step 2) Let \(\mathbf{f}_{n}^{o p t}=\frac{1}{M_{t}} \| \mathbf{v}_{1} \|_{1}\) exp \(\left.\right|^{\text {jungle }(\mathbf{v}) \mathbf{v}_{1} \text { ) as solution to the } n \text { th sub- }
    array.
    (Step 3) Update the matrices \(\mathbf{G}_{n}=\mathbf{R}\left(\mathbf{H}^{\phi}\right)^{H} \mathbf{T}_{n}^{-1} \mathbf{H}^{\phi} \mathbf{R}\) and \(\mathbf{T}_{n}=\)
    \(\mathbf{I}_{n}+\frac{\rho}{N_{s}} \mathbf{H}^{\phi} \mathbf{F}_{n} \mathbf{F}_{n}^{H}\left(\mathbf{H}^{\phi}\right)^{H}\) for the next \((\mathrm{n}+1)\) sub-array.
```


## 5 Simulations and results

Simulation results are presented in this section. First EDA is applied for transmit antenna selection, afterwards the hybrid precoder is designed using SIC algorithm. EDA iterations $\left(N_{\text {iter }}\right)$ is set to 50 and sample size $\left(N_{\text {prop }}\right)$ is set to 20 . System
![img-2.jpeg](img-2.jpeg)

Fig. $3 N_{T}=64, N_{R}=8, N_{R F}=4, M_{t}=8$
parameters for results shown in Fig. 3 are as follows, the transmit antennas are set as $N_{T}=64$, the receive antennas are set as $N_{R}=8$, the system is equipped with $N_{R F}=4$ RF chains, the paths are set as $L=3$, the antennas per RF chain are $M_{T}=16$, the desired antennas per RF chain are $M_{t}=8$ and finally the total selected antennas become $N_{t}=32$. Secondly, we perform analysis with $N_{T}=144$ and $N_{T}=256$ as shown in Figs. 4 and 5 respectively. The number of RF chains in both cases is set as $N_{R F}=12$. Note that the number of selected antennas is kept as half of the total available antennas to ensure greater than $90 \%$ spectral efficiency.

Figure 3 shows the results for $N_{T}=64$. Joint solution of exhaustive search and SIC based hybrid precoder gives the optimal results. EDA is outperforming conventional evolutionary algorithm in terms of spectral efficiency. The proposed EDA can offer a better solution by increasing the number of iterations or samples, but at the cost of computational complexity. Hence, a tradeoff between optimal performance and computational complexity exists which can be exploited to configure the algorithm in accordance with the available hardware.

Figures 4 and 5 show the results when $N_{T}$ is set as 144 and 256 representing the massive MIMO architecture. Half of the total available antennas are selected and it can be seen that the EDA based algorithm is outperforming the evolutionary algorithm in terms of spectral efficiency.

Figure 6 shows the comparison between EDA and evolutionary algorithm based antenna selection algorithms in terms of spectral efficiency vs. number of iterations. Clearly, the EDA based approach is outperforming the evolutionary

![img-6.jpeg](img-6.jpeg)

Fig. $4 \quad N_{T}=144, N_{R}=16, N_{R F}=12, M_{t}=4$
![img-4.jpeg](img-4.jpeg)

Fig. $5 \quad N_{T}=256, N_{R}=16, N_{R F}=12, M_{t}=8$
algorithm based approach. For EDA, the lower threshold is set to 0.2 and upper threshold is set to 0.8 , also the probability distribution is calculated by sorting the samples from the previous iteration and using the best half for calculations. Similarly, the new samples for next iteration are composed of half best from previous iteration and half newly generated based on probability distribution. Also, if the sorting is not performed and the probability distribution is calculated using all the samples of previous iteration to constitute a completely new population, results in lower performance than what is achieved by sorting the samples and calculating
![img-5.jpeg](img-5.jpeg)

Fig. $6 \quad N_{T}=64, N_{R}=8, N_{R F}=4, M_{t}=8, N_{p o p}=20$
![img-6.jpeg](img-6.jpeg)

Fig. $7 \quad N_{T}=144, N_{R}=16, N_{R F}=8, M_{t}=9, N_{p o p}=20$
probability distribution on the basis of learning from elite samples.

The comparison of EDA based approach, CE based approach and evolutionary algorithm (Genetic Algorithm) is shown in Fig. 7. It is clearly seen that the EDA based antenna selection with SIC algorithm for precoding outclasses other algorithms in terms of spectral efficiency.

Figure 8 shows the $95 \%$ confidence interval plot for EDA iterations. The confidence interval is plotted for 1000 iterations and the plot verifies the robustness of the algorithm.

![img-7.jpeg](img-7.jpeg)

Fig. $895 \%$ confidence interval for EDA

### 5.1 Performance analysis with imperfect CSI

The effect of uncertainty on channel model and subsequently the performance of proposed algorithm is evaluated in this section. In the presence of imperfect CSI, the estimated channel matrix $\widehat{\mathbf{H}}$ is given as [8]
$\widehat{\mathbf{H}}=\xi \mathbf{H}+\sqrt{1-\xi^{2}} \mathbf{E}$
Where the actual Saleh-Valenzuela channel model is $\mathbf{H}$. $\xi \in[0,1]$ is the precision number for CSI and the error matrix with distribution i.i.d $\mathbb{C N}(0,1)$ is denoted as $\mathbf{E}$. Figure 9 presents the imperfect CSI analysis for a mmW massive MIMO system having $N_{T}=64, N_{R}=8, N_{R F}=4$ and $M_{t}=8$. It can be seen that the proposed system is robust to channel imperfectness.

### 5.2 Energy efficiency analysis

The energy efficiency of the proposed system is also analyzed. Adopting the energy consumption model [8], the energy efficiency $\eta$ is defined as
$\eta=\frac{R}{P_{\text {total }}}=\frac{R}{P_{t}+N_{R F} P_{R F}+N_{P S} P_{P S}}$
where $P_{\text {total }}=P_{t}+N_{R F} P_{R F}+N_{P S} P_{P S}$ is the total power consumption of the massive MIMO hybrid precoder. The system parameters are explained and set as follows. Power consumed by each RF chain, phase shifter and total transmit power is assumed as $P_{R F}=250 \mathrm{~mW}, P_{P S}=1 \mathrm{~mW}$ and $P_{t}=1 \mathrm{~W}$ [8]. $N_{R F}$ and $N_{P S}$ represents the RF chains
![img-8.jpeg](img-8.jpeg)

Fig. 9 Impact of imperfect CSI
![img-9.jpeg](img-9.jpeg)

Fig. 10 Energy efficiency analysis
and phase shifters, respectively. Figure 10 depicts the energy efficiency analysis against RF chains with selected antennas as $N_{t}=32$ and 64 out of total available $N_{T}=64$ and 128 antennas, respectively. The system adopting the antenna selection achieves better energy efficiency than the legacy system without any selection. Hence the proposed system is proved to be energy efficient and enhances the performance of massive MIMO architecture.

### 5.3 Complexity analysis

In this section, we compare the computational complexity of the proposed EDA algorithm with that of the exhaustive search. We have considered the number of complex multiplications and additions as a measure of computational complexity. A determinant can be computed with complexity $O\left(n^{3}\right)$ and for a $n \times n$ matrix each determinant requires $(1 / 3) \times n^{3}$ complex operations. To calculate the term inside determinant $\left(\mathbf{I}_{N_{R}}+\frac{\rho}{N_{t}} \mathbf{H}^{\phi}\left(\mathbf{H}^{\phi}\right)^{H}\right)$ approximately $\left(N_{R}^{2} N_{t}\right)$ complex operations are required. The term $\operatorname{det}\left(\mathbf{I}_{N_{R}}+\frac{\rho}{N_{t}} \mathbf{H}^{\phi}\left(\mathbf{H}^{\phi}\right)^{H}\right)$ needs $\left(N_{R}^{3} / 3\right)+\left(N_{R}^{2} N_{t}\right)$ determinants [18]. The exhaustive search algorithm needs to compute $\binom{N_{T}}{N_{t}}$ complex determinants so the total number of complex multiplications and additions becomes $\binom{N_{T}}{N_{t}} \times$ $\left(N_{R}^{3} / 3\right)+\left(N_{R}^{2} N_{t}\right)$. As a result for Massive MIMO systems with large number of antennas, the computational complexity increases exponentially with the number of antennas. In comparison with exhaustive search schemes, EDA only needs to compute $I_{l} \times N_{I t e r}$ determinants. So EDA only requires $I_{l} \times N_{I t e r} \times\left(N_{R}^{3} / 3\right)+\left(N_{R}^{2} N_{t}\right)$ complex operations, which marks the efficiency of EDA based approach. Similarly the computational complexity of SIC and OMP based schemes is $O\left(2 M_{t} N_{s}\left(N_{t}^{2}\left(K+N_{s} M_{t}\right)\right)\right)$ and $O\left(2 M_{t}^{3}\left(M_{t}^{4} N_{t}+M_{t}^{2} L^{2}+\right.\right.$ $\left.\left.M_{t}^{2} N_{t}^{2} L\right)\right)$, respectively [30].

We have considered the total number of flops required by algorithm as an index to calculate the computational complexity. We have not considered the time complexities due to the reason that the time complexities are dependent on machine type and coding style. Complexity in terms of number of flops gives a more specific representation of computations required by any algorithm.

## 6 Conclusions

In this paper, we have jointly optimized the antenna selection and precoding problem for a massive MIMO system. The proposed algorithm comprising of the learning based EDA for antenna selection and SIC based approach for precoding is computationally optimal and energy efficient with high spectral efficiency. Energy efficiency is improved as a result of hardware reduction by adopting the antennas experiencing the good channel conditions. Hybrid precoder design using SIC algorithm is optimal in combating the path loss incurred by mmW frequencies. Our future work will explore the multi user massive MIMO scenario and its efficiency improvement by adopting the antenna selection with precoding.

## References

1. Rangan, S., Rappaport, T. S., \& Erkip, E. (2014) Millimeter-wave cellular wireless networks: Potentials and challenges. In Proceedings of the IEEE (pp. 366-385).
2. Akdeniz, M. R., Liu, Y., Samimi, M. K., et al. (2014). Millimeter wave channel modeling and cellular capacity evaluation. The IEEE Journal on Selected Areas in Communications, 32(6), 1164-1179.
3. Heath, R. W., González-Prelcic, N., Rangan, S., et al. (2016). An overview of signal processing techniques for millimeter wave MIMO systems. IEEE Journal of Selected Topics in Signal Processing (JSTSP), 10(3), 436-453.
4. Han, S., Chih-Lin, I., Xu, Z., et al. (2015). Large-scale antenna systems with hybrid analog and digital beamforming for millimeter wave 5G. The IEEE Communications Magazine, 53(1), 186-194.
5. El Ayach, O., Rajagopal, S., Abu-Surra, S., Pi, Z., \& Heath, R. (2014). Spatially sparse precoding in millimeter wave MIMO systems. IEEE Transactions on Wireless Communications, 13(3), $1499-1513$.
6. Yu, X., Shen, J., Zhang, J., \& Letaief, K. B. (2016). Alternating minimization algorithms for hybrid precoding in millimeter wave MIMO systems. IEEE Journal of Selected Topics in Signal Processing, 10(3), 485-500.
7. Khan, I., et al. (2019). An efficient precoding algorithm for mmWave massive MIMO systems. Symmetry, 11(9), 1099.
8. Gao, X., et al. (2016). Energy-efficient hybrid analog and digital precoding for mmWave MIMO systems with large antenna arrays. IEEE Journal on Selected Areas in Communications, 34(4), 9981009 .
9. Alluhaibi, O., Ahmed, Q. Z., Wang, J. \& Zhu, H. (2017). Hybrid digital-to-analog precoding design for mm-wave systems. In IEEE International Conference on Communications (ICC), Paris (pp. 16).
10. Yi, X., Bo, L., Zhongjiang, Y., Jiancun, F., \& Mao, Y. (2019). A general hybrid precoding method for mmWave massive MIMO systems. Radio Engineering, 29(2), 1.
11. Zhang, D., Wang, Y., Li, X., \& Xiang, W. (2017). Hybridly connected structure for hybrid beamforming in mmWave massive MIMO systems. IEEE Transactions on Communications, 66(2), 662674.
12. Liu, X., et al. (2019). Hybrid Precoding for Massive mmWave MIMO Systems. IEEE Access, 7, 3357733586.
13. Asaad, S., Rabiei, A. M., \& Mller, R. R. (2018). Massive MIMO with antenna selection: Fundamental limits and applications. IEEE Transactions on Wireless Communications, 17(12), 8502-8516.
14. Molisch, A., et al. (2005). Capacity of MIMO systems with antenna selection. IEEE Transaction on Wireless Communication, 4(4), $1759-1772$.
15. Uchida, D., Arai, H., Inoue, Y., \& Cho, K. (2010). Antenna selection based on minimum Eigenvalue in dual-polarized directional MIMO antenna. In Proceedings of the IEEE Vehicular Technology Conference (VTC2010-Spring) IEEE (Vol.71, pp. 1-5).
16. Yangyang, Z., Gan, Z., Chunlin, J., Kai-Kit, W., Edwards, D. J., \& Tiejun, C. (2010). Near-optimal joint antenna selection for amplify-and-forward relay networks. IEEE Transactions on Wireless Communications, 9(8), 2401-2407.
17. Naeem, M., \& Lee, D. C. (2011). Low-complexity joint transmit and receive antenna selection for MIMO systems. Engineering Applications of Artificial Intelligence, 24, 1046-1051.
18. Naeem, M., \& Lee, D. C. (2014). A joint antenna and user selection scheme for multiuser MIMO system. Applied Soft Computing, 23, 366-374.
19. Hsu, K. N., Wang, C. H., Lee, Y. Y., \& Huang, Y. H. (2015). Low complexity hybrid beamforming and precoding for 2D pla-

nar antenna array mmWave systems. In IEEE Workshop on Signal Processing Systems (SiPS) (p. 16).
20. Naeem, M., \& Lee, D. C. (2009). Near-optimal joint selection of transmit and receive antennas for MIMO systems. 9th International Symposium on Communications and Information Technology (p. 572577). Icheon: South Korea.
21. Maimaiti, S., Chuai, G., Gao, W. et al. (2019). A low-complexity algorithm for the joint antenna selection and user scheduling in multi-cell multi-user downlink massive MIMO systems. Journal Wireless Communication Network
22. Rajashekar, R., et al. (2019). Transmit antenna subset selection in generalized spatial modulation systems. IEEE Transactions on Vehicular Technology, 68(2), 1979-1983.
23. Tan, B. S., Li, K. H., \& Teh, K. C. (2013). Transmit antenna selection systems: A performance comparison of different types of receiver schemes. IEEE Vehicular Technology Magazine, 8(3), $104-112$.
24. Jang, S., Ahn, M., Lee, H., \& Lee, I. (2016). Antenna selection schemes in bidirectional full-duplex MIMO systems. IEEE Transactions on Vehicular Technology, 65(12), 10097-10100.
25. Naeem, M., \& Lee, D. C. (2013). EDA-based scheduling of users in the MIMO multiple access channel. Wireless Personal Communications, 71, 467-490.
26. Naeem, M., Khwaja, A. S., Anpalagan, A., \& Jaseemuddin, M. (2014). Cross entropy optimization for constrained green cooperative cognitive radio network. In IEEE 79th Vehicular Technology Conference (VTC Spring) (pp. 1-5). Seoul.
27. Ahmad, M., Naeem, M., \& Iqbal, M. (2019). Estimation of distribution algorithm for joint resource management in D2D communication. Wireless Personal Communication, 1, 1113-1129.
28. Abbas, W. B., Gomez-Cuba, F., \& Zorzi, M. (2017). Millimeter wave receiver efficiency: A comprehensive comparison of beamforming schemes with low resolution ADCs. IEEE Transactions on Wireless Communications, 16(12), 8131-8146.
29. Alkhateeb, A., et al. (2014). Channel estimation and hybrid precoding for millimeter wave cellular systems. IEEE Journal of Selected Topics in Signal Processing, 8(5), 831-846.
30. Huang, H., et al. (2019). Deep-learning-based millimeter-wave massive MIMO for hybrid precoding. IEEE Transactions on Vehicular Technology, 68(3), 3027-3032.

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
![img-10.jpeg](img-10.jpeg)

Salman Khalid received the bachelor's degree from the University of Engineering and Technology (UET), Taxila, Pakistan in 2008, master's degree from the Center of Advanced Studies in Engineering (CASE), Islamabad, Pakistan, in 2014, and currently pursuing the Ph.D. degree in electrical engineering from the National University of Computer and Emerging Sciences (NUCES), Islamabad, Pakistan. During master's degree, his research was focused on wireless communication, compressed sensing and digital signal processing, while during Ph.D. degree, his research is mostly focused on hybrid precoder design, resource allocation in MIMO communication networks and
energy efficiency in wireless networks. His current research interests include energy efficiency in 5G millimeter-wave cellular networks, MIMO communication, and millimeter-wave hybrid beamforming.
![img-11.jpeg](img-11.jpeg)

Rashid Meh mood received his BE degree in Avionics Engineering from NUST College of Aeronautical Engineering, Risalpur, Pakistan in 2010. He is currently pursuing his MS degree in Electrical Engineering from COMSATS University Islamabad, Wah Campus, Pakistan. His current research focuses on optimization of millimeter wave Massive MIMO systems.
![img-12.jpeg](img-12.jpeg)

Waqas Bin Abbas received the Bachelors and the Masters degree from National University of Computer and Emerging Sciences (NUCES), Islamabad, Pakistan in 2008 and 2012, respectively, and the Ph.D. in Information Engineering in 2017 from the University of Padova, Italy. Currently, he is working as an Assistant Professor at NUCES, Islamabad, Pakistan. During Masters, his research was focused in underwater wireless communication, while during Ph.D., his research was mostly focused on energy efficiency in wireless networks. His current research interests include energy efficiency in 5G millimeter wave cellular networks, MIMO communication and multi-hop wireless networks.
![img-13.jpeg](img-13.jpeg)

Farhan Khalid received the B.S. degree in electronic engineering from Ghulam Ishaq Khan Institute of Engineering Sciences \& Technology, Topi, Pakistan, in 1999, the M.Sc. degree in electrical engineering from Blekinge Institute of Technology, Karlskrona, Sweden, in 2005, and the Dr.Ing. (Ph.D.) degree in electrical engineering from the University of Stuttgart, Stuttgart, Germany, in 2012. Additionally, he holds a master's degree in telecommunication management awarded by
the Institut National des Telecommunications, France, in 2001. He started his professional career as an engineer, working for various organizations in the telecom sector. Since 2006, he has been involved with academia and research in the domains of digital communications and signal processing. His current research interests lie in the area of wireless communications, with particular focus on transceiver design and optimization for multiuser MIMO, massive MIMO and millimeter wave systems.

![img-14.jpeg](img-14.jpeg)

Muhammad Naeem received the BS (2000) and MS (2005) degrees in Electrical Engineering from the University of Engineering and Technology, Taxila, Pakistan. He received his PhD degree (2011) from Simon Fraser University, BC, Canada. From 2012 to 2013, he was a Postdoctoral Research Associate with WINCORE Lab. at Ryerson University, Toronto, ON, Canada. He is currently associate professor with the Department of Electrical and computer Engineering, COMSATS University Islamabad, Wah Campus, Pakistan. From 2000 to 2005, he was a senior design engineer at Comcept (pvt) Ltd. At the design department of Comcept (pvt) Ltd, he participated in the design and development of smart card based GSM and CDMA pay phones. He is also a Microsoft Certified Solution Developer (MCSD). His research interests include optimization of wireless communication systems, non-convex optimization, resource allocation in cognitive radio networks and approximation algorithms for mixed integer programming in communication systems. He has been the recipient of NSERC CGS scholarship.