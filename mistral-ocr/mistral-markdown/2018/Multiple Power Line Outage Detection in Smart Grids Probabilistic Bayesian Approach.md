# Multiple Power Line Outage Detection in Smart Grids: Probabilistic Bayesian Approach 

ASHFAQ AHMED ${ }^{1}$, MUHAMMAD AWAIS ${ }^{1}$, MUHAMMAD NAEEM ${ }^{1,2}$, (Senior Member, IEEE), MUHAMMAD IQBAL ${ }^{1}$, WALEED EIAZ ${ }^{2}$, (Senior Member, IEEE), ALAGAN ANPALAGAN ${ }^{2}$, and HONGSEOK KIM ${ }^{3}$, (Senior Member, IEEE)<br>${ }^{1}$ COMSATS Institute of Information Technology, Islamabad 47040, Pakistan<br>${ }^{2}$ Department of Electrical and Computer Engineering, Ryerson University, Toronto, ON M5B 2K3, Canada<br>${ }^{3}$ Department of Electronics Engineering, Sogang University, Seoul 04107, South Korea

Corresponding author: Hongseok Kim (hongseok@sogang.ac.kr)
This work was in part by the Korea Electric Power Corporation of the South Korea under Grant CX72166553-R16DA17.


#### Abstract

Efficient power line outage identification is an important step which ensures reliable and smooth operation of smart grids. The problem of multiple line outage detection (MLOD) is formulated as a combinatorial optimization problem and known to be NP-hard. Such a problem is optimally solvable with the help of an exhaustive evaluation of all possible combinations of lines in outage. However, the size of search space is exponential with the number of power lines in the grid, which makes exhaustive search infeasible for practical sized smart grids. A number of published works on MLOD are limited to identify a small, constant number of lines outages, usually known to the algorithm in advanced. This paper applies the Bayesian approach to solve the MLOD problem in linear time. In particular, this paper proposes a low complexity estimation of outage detection algorithm, based on the classical estimation of distribution algorithm. Thanks to an efficient thresholding routine, the proposed solution avoids the premature convergence and is able to identify any arbitrary number (combination) of line outages. The proposed solution is validated against the IEEE-14 and 57 bus systems with several random line outage combinations. Two performance metrics, namely, success generation ratio and percentage improvement have been introduced in this paper, which quantify the accuracy as well as convergence speed of proposed solution. The comparison results demonstrate that the proposed solution is computationally efficient and outperforms a number of classical meta-heuristics.


#### Abstract

INDEX TERMS Line outage identification, smart grids, estimation of distribution algorithm, power networks.


## I. INTRODUCTION

Phasor measurement units (PMUs) are devices which provide synchronized, real time, dense and highly accurate measurements of current and voltage phasors [1]. PMUs are widely used for automation and state information collection of widearea measurement systems [2], [3]. They have been installed by a large number of utility companies across the globe and help to perform key system tasks including protection, observation and control of power networks [4]. The overview of security and privacy related issues in smart grid are discussed in [5].

## A. MOTIVATION

PMUs play a vital role in the identification of line outages of geographically large power grids. They are installed on a number of power system buses. One of the PMUs is taken as
a reference and the phasor measurements of other PMUs are relative to it. When a single or multiple power lines undergo an outage, the relative phase angles are changed and hence the system's power flow is disturbed. Due to overloading, the cascaded tripping of power lines leads to a complete system blackout [6].

Another smart grid automation technique is supervisory control and data acquisition (SCADA) [7]. However, PMUs have demonstrated a significant advantage over SCADA in a number of ways including measurement resolution, state observation capability and coverage area [8]. Some key differences between SCADA and PMU technologies are highlighted in Table 1. In addition to power system protection, PMUs are also used for implementing a load shedding method that consists of simultaneous reactive and active power to address the frequency and voltage stability issues respectively [9]. Moreover, PMUs increase the power service

TABLE 1. SCADA vs. PMU [8].

| Parameters | SCADA | PMU |
| :-- | :-- | :-- |
| Measurement | Analog | Digital |
| Resolution | 2-4 samples per <br> cycle | Up to 60 samples <br> per cycle |
| Observability | Steady state | Dynamic/Transient <br> state |
| Monitoring | Local-area | Wide-area |
| Phase Angle <br> Measurement | No | Yes |

quality by precise analysis, automated correction and disturbance recording of sources of system degradation [10].

## B. RELATED WORK

The state-of-the-art protection techniques for power grids can be classified into two broad categories. Firstly, it includes strategies which determine the optimal location and number of PMUs to achieve a grid-wide observability. Secondly, the techniques which exploit rich PMU data for efficient identification of power lines in outage. Some important works are discussed as follows. The work in [11] proposes a two step PMU placement technique. At first, linear programming is used to obtain an optimum upper bound on the number of PMUs. Then, a branch and bound algorithm is used to obtain a near optimal placement solution. An integer linear programming based PMU placement is also considered in [12]. Moreover, the work also studies the effect of a single PMU loss or a single line outage on optimal PMUs placement. The work in [13] proposes a probabilistic approach for PMU placement. Two main objectives are achieved. At first, system observability is ensured with minimum number of PMUs. Secondly, the multi-objective problem is solved with the help of an augmented epsilon constraint method to achieve Pareto optimal points. In [14], an artificial intelligence approach based on support vector machines (SVM) is proposed. Using the PMU data, the work trains all candidate network topologies under several loading conditions in order to detect single line outages. In [15], PMU's phasors and other system topology parameters are used for optimal detection of single line outages. This work is extended in [16], in which the pre- and post-event information of the topology is used to solve the double line outage identification problem.

Mathematically, the approaches used in [15] and [16] are combinatorial in nature. Multiple line outage detection (MLOD) problem is also a kind of combinatorial optimization problem, which requires comprehensive information of all possible network topologies. Therefore, due to drastic increase in the search space, the approaches proposed in [15] and [16] cannot be used. In [17], a solution is proposed which adopts a compressed sensing technique. The solution named as least absolute shrinkage and selection operator (LASSO) is capable to detect outage
over multiple lines. However, the accuracy of solution is highly affected by a parameter which depends on a-priori information about perturbed noise and outage probability. Rubinstein and Kroese in [18] propose a cross entropy optimization (CEO), a stochastic search method for detection of multiple line outages. CEO demonstrates better detection capability as compared to LASSO. Banerjee et al. [19] suggested an approach named quickest change detection. The authors adopted a linearized model of power system and proposed a statistical method for detection and isolation of line outages. Emami and Abur [20] propose a method which uses internal system measurements in order to track the external network changes. Further, integer linear programming is used for the detection of minor and major network changes.

Bijwe et al. [21] proposed a method which uses voltage deviation and overload performance metrics in order to rank line outage contingencies in AC-DC systems. The work uses Jacobian matrix to calculate current compensations for line outages and uses a coupled AC-DC flow model. IEEE 14-bus system is used to test the proposed model and compare it with rigorous AC-DC load flow methods. Hao et al. [22] proposed a method based on compressive sensing to identify multiple line outages and sudden impedance changes in power system.

The work in [23] simulates the power system state after the event of a sudden outage of an element. The authors adopted the AC power flow model and proposed a simple method to determine the important parameters of the formulated problem. In [24], $N-1$ criterion is investigated for an evolving power grid along with its impact on cascaded line outages. In [25], the measurement errors in DC power flow are identified by exploiting the singularity of the impedance matrix and sparsity of the error vector. The proposed sparsitybased decomposition-DC power flow approach is able to compute the measurement errors accurately, when the method is verified on the IEEE 118-bus and 300-bus systems. In [26], the work exploits the historical weather data from NCDC, along with the historical interruption information, and predicts the power system interruptions. A minimum variance unbiased estimators (MVUEs) is derived in [27] for active power based on the voltage phase at each node of the power system. It is concluded that power system operations can be more accurately estimated if there is lower correlation between the noise vector elements. In [28], a power loss minimization scheme is presented. The proposed scheme is based on oblivious network design, and is therefore termed as oblivious routing-based power flow method. The approach can be applied for the large scale power loss minimization.

An oblivious routing economic dispatch (ORED) algorithm is presented in [29], for congestion in smart power systems. It is claimed that the proposed method works independent of the network topology, and is therefore suitable for large scale economic dispatch problems. The ORED algorithm outperforms the other state-of-the-art economic dispatch algorithms in terms of congestion management and power loss minimization. In [30], fuzzy models are built of overhead power line outages. In [31], Galton-Watson

TABLE 2. Summary of some published works on power line outage detection.

| Ref. | Single line outage | Multiple Fixed line <br> outages | Multiple Variable <br> line outages |
| :--: | :--: | :--: | :--: |
| [Proposed] |  |  | $\checkmark$ |
| [14] | $\checkmark$ |  |  |
| [15] | $\checkmark$ |  |  |
| [16] |  | $\checkmark$ |  |
| [17] |  | $\checkmark$ |  |
| [19] | $\checkmark$ |  |  |
| [20] | $\checkmark$ |  |  |
| [21] | $\checkmark$ |  |  |
| [22] |  | $\checkmark$ |  |
| [23] |  | $\checkmark$ |  |
| [24] |  | $\checkmark$ |  |
| [30] |  | $\checkmark$ |  |
| [31] |  | $\checkmark$ |  |
| [32] |  | $\checkmark$ |  |

branching process model is proposed in order to estimate the load shed propagation in cascaded line outages. In [32], PMU data is exploited in order to identify the line outage locations within a specified geographical area of the power system. The proposed approach assumes PMUs to be placed within and at the boundary of the area. The proposed approach is unable to identify the line outages outside the boundary of the area.

Table 2 presents a summary of published solutions for line outage detection (LOD). Broadly, the published solutions are categorized on the basis of line outage detection flexibility. In the first column, there are solutions which are limited to detect only single line outage. In the second column, there are solutions with multiple line outage detection (MLOD) capability. However, they are named as fixed MLOD solutions as they are limited to identify only a fixed (usually small) number of line outages. Almost all published works on outage detection fall in to the first two categories.

## C. CONTRIBUTIONS

In this work, we have proposed a solution based on a probabilistic Bayesian approach which solves the MLOD problem in linear time. The proposed solution is named as estimation of outage detection (EOD) and based on estimation of distribution algorithm (EDA). The main contribution of this work are:

- The proposed EOD solution has capability to detect and identify any combination and number of lines in outage.
- An efficient thresholding routine is applied to update the probability distribution of candidate solutions. This helps to avoid the local optima. The EOD algorithm with thresholding is thus named as EOD-Threshold.
- The proposed algorithm is simulated for several IEEE bus systems with random line outage combinations.
![img-0.jpeg](img-0.jpeg)

FIGURE 1. Schematic overview of the paper.
The comparison results show that the proposed EOD solution outperforms a number of other meta-heuristics in terms of success and convergence rates.

## D. PAPER ORGANIZATION

In Fig. 1, the schematic overview of the paper is shown. The rest of this paper is organized as follows. In Section II, system model is described with MLOD problem formulation. Section III discusses the basics of EDA along with the proposed EOD and EOD-Threshold algorithms. Section IV discusses the simulation results and comparisons. Finally, the conclusions are drawn in Section V.

## II. SYSTEM MODEL AND PROBLEM DEFINITION

## A. LINEAR DC POWER FLOW MODEL

Consider a power network consisting of $L$ transmission lines and $N$ buses. This network can be modelled in the form of a directed graph $\mathcal{G}=\{\mathcal{N}, \mathcal{E}\}$, where $\mathcal{N}=\{1,2, \ldots, N\}$ is the

![img-1.jpeg](img-1.jpeg)

FIGURE 2. Transmission line network (a) interconnect grid system and (b) power flow model.
set of nodes (buses) and $\mathcal{E}=\{(m, n)\} \subseteq \mathcal{N} \times \mathcal{N}\}$ denotes the set of possible edges. The incident matrix of $\mathcal{G}$ is a matrix $\mathbf{M}$ of size $N \times L$. An entry at row $n \in\{1,2, \cdots, N\}$ and column $l \in\{1,2, \cdots, L\}$ of $\mathbf{M}$ is given by:

$$
M_{n l}=\left\{\begin{array}{ll}
1, & \text { if line } l \text { originates from bus } n \\
-1, & \text { if line } l \text { terminates at bus } n \\
0, & \text { otherwise }
\end{array}\right.
$$

Fig. 2(a) shows an example of a network with $L=5$ lines and $N=4$ buses. For this network, the matrix $\mathbf{M}$ is obtained as:

$$
\mathbf{M}=\left[\begin{array}{cccc}
1 & 0 & 0 & -1 & 1 \\
-1 & 1 & 0 & 0 & 0 \\
0 & -1 & 1 & 0 & -1 \\
0 & 0 & -1 & 1 & 0
\end{array}\right]
$$

This work adopts a linear DC power flow model [17]. The conservation of power must be satisfied i.e. for each bus, the total power inflow must be equal to the sum of all power outflows. Mathematically,

$$
P_{n}=\sum_{m \in \mathcal{N}(n)} P_{n m}
$$

where $P_{n}$ denotes the power flowing in to bus $n, P_{n m}$ is the power flowing out from bus $n$ to bus $m$ and $\mathcal{N}(n)$ denotes the set of all buses which have direct connection with bus $n$. Moreover,

$$
P_{n m}=\frac{1}{x_{m n}}\left(\theta_{n}-\theta_{m}\right)
$$

where, $x_{m n}=x_{m n}$ is the reactance of line between buses $n$ and $m$ and $\theta_{n}$ and $\theta_{m}$ are their respective voltage phasor angles. With real power injections $\mathbf{p}=\left[p_{1}, \cdots, p_{N}\right]^{T} \in \mathbb{R}^{N}$ and voltage phasor angles $\boldsymbol{\theta} \in\left[\theta_{1}, \cdots, \theta_{N}\right]^{T} \in \mathbb{R}^{N}$, the above equations can be stacked in vector notation as

$$
\mathbf{p}=\mathbf{B} \boldsymbol{\theta}
$$

where $\mathbf{B}=\left\{B_{n m}\right\} \in \mathbb{R}^{N}$ is an $N \times N$ matrix with entry at $m$-th row and $n$-th column given by,

$$
B_{m n}=\left\{\begin{array}{ll}
-x_{m n}^{-1}, & \text { if }(m, n) \in \mathcal{E} \\
\sum_{n \in \mathcal{N}(m)} x_{m n}^{-1}, & \text { if } m=n \\
0, & \text { otherwise }
\end{array}\right.
$$

The above equation shows that $\mathbf{B}$ is dependent upon the network topology as well as line reactance values $x_{m n}$. The topological changes in network as a result of line outages affect the voltage phasor angle vector $\boldsymbol{\theta}$ in (5). This topological effect can be modelled by expressing $\mathbf{B}$ as a Laplacian matrix of weighted graph $\mathcal{G}$ and representing it as [17]

$$
\mathbf{B}=\mathbf{M D}_{\mathbf{x}} \mathbf{M}^{\mathbf{T}}=\sum_{l=1}^{L}\left(\frac{1}{x_{l}} \mathbf{m}_{l} \mathbf{m}_{l}^{T}\right)
$$

where the diagonal matrix $\mathbf{D}_{\mathbf{x}}$ has line reactance $x_{l}^{-1}$ as its $l$-th diagonal entry. For the power network for Fig. 2 (a), the power flow graph is represented in Fig. 2 (b) The matrix B takes the form
where real numbers $a, b, \cdots, e$ denote respectively, the reactance of the lines 1 to 5 .

Table 3 lists all notations used in this section.

TABLE 3. Description of main notations used in the system model.

| Symbol | Details |
| :-- | :-- |
| $L$ | Number of power lines in the network |
| $N$ | Number of power buses in the network |
| $\mathcal{G}$ | Weighted graph of network |
| $\mathcal{E}$ | Set of edges in $\mathcal{G}$ |
| $\mathcal{L}$ | Set of lines in the network |
| $\mathcal{N}$ | Set of buses in the nework |
| $\mathbf{M}$ | Bus line incidence matrix of $\mathcal{G}$ |
| $\mathbf{p}$ | Real vector of length $N$ of power injections |
| $\mathbf{D}_{\mathbf{x}}$ | $L \times L$ diagonal matrix with line reactances as |
| $\boldsymbol{\eta}$ | $\quad$ diagonal entries |
| $\boldsymbol{b}$ | Noise perturbation vector |
| $\mathbf{A} 1 \times L$ binary vector. A bit 0 denotes a normal |  |
|  | line whereas, 1 denotes an outaged line |
| $x_{l}$ | Reactance of line $l$ that belongs to set $\mathcal{L}$ or $\mathcal{E}$ |
| $P_{n}$ | Total power flowing into bus $n$ |
| $P_{n m}$ | Power flowing out from bus $n$ to $m$ |
| $\theta_{n}$ | Pre-outage voltage phasor angle measured at bus |
| $\theta_{n}$ | $n$ |
| $\theta_{n}$ | Laplacian matrix of pre-outage event |
| $\theta_{n}$ | Post event phasor angle measured at bus $n$ |
| $\mathbf{B}$ | Laplacian matrix of post-outage |
| $\mathbf{m}_{l}$ | Incidence vector of single line $l$ |
| $\hat{\mathbf{B}}$ | $\mathbf{B}^{\prime}-\mathbf{B}$ |
| $B_{m n}$ | Single reactance between bus $m$ and $n$ |

## B. LINE OUTAGE MODEL

Given a linear model of DC power flow (5), vector $\mathbf{p}$ of real power injections and vector $\boldsymbol{\theta}$ of pre-event phase angles are related to each other by the topology dependent susceptance matrix B. As a result of network topological changes caused by an outage over one or multiple lines, the pre-outage directed graph $\mathcal{G}=\{\mathcal{N}, \mathcal{E}\}$ is transformed into a post-outage directed graph $\mathcal{G}^{\prime}=\left\{\mathcal{N}, \mathcal{E}^{\prime}\right\}$, where $\mathcal{E}^{\prime}=\mathcal{E} \backslash \mathcal{E}$ is the set of lines in outage. The post outage directed graph remains connected and grid is assumed to be in quasi-stable state. The DC power flow following the outage event is expressed as

$$
\mathbf{p}^{\prime}=\mathbf{B}^{\prime} \boldsymbol{\theta}^{\prime}=\mathbf{p}+\boldsymbol{\eta}
$$

where $\mathbf{B}^{\prime}$ is the post outage susceptance matrix, $\boldsymbol{\theta}^{\prime}$ is the post outage phasor vector and $\boldsymbol{\eta}$ is the noise vector which contains perturbations between $\mathbf{p}$ and $\mathbf{p}^{\prime}$. The value $\boldsymbol{\eta}$ contains the DC approximation errors and is usually modeled a vector of Gaussian distribution with covariance matrix $\sigma_{\eta}^{2} \mathbf{I}$ and zero mean [33]. Substituting (5) in (9) yields

$$
\mathbf{B} \boldsymbol{\theta}+\boldsymbol{\eta}=\mathbf{B}^{\prime} \boldsymbol{\theta}^{\prime}=\mathbf{B} \boldsymbol{\theta}^{\prime}-\overline{\mathbf{B}} \boldsymbol{\theta}^{\prime}
$$

where $\overline{\mathbf{B}}=\mathbf{B}-\mathbf{B}^{\prime}$, is the weighted Laplacian of outaged lines in $\mathcal{E}$ and expressed as,

$$
\overline{\mathbf{B}}=\sum_{l \in \mathcal{E}} \frac{1}{k_{l}} \mathbf{m}_{l} \mathbf{m}_{l}^{T}=\mathbf{M} \mathbf{D}_{\mathbf{x}}\{\mathbf{b}\} \mathbf{M}^{T}
$$

where $\mathbf{b}$ is an $L$-dimensional binary vector whose element $b_{l}$ can be written as:

$$
\mathbf{b}_{l}= \begin{cases}1, & l \in \tilde{\mathcal{E}} \\ 0, & \text { otherwise }\end{cases}
$$

Considering the phase angle change vector $\tilde{\boldsymbol{\theta}} \triangleq \boldsymbol{\theta}^{\prime}-\boldsymbol{\theta}$ and substituting in difference model (9) yields

$$
\mathbf{y} \triangleq \mathbf{B} \tilde{\boldsymbol{\theta}}=\overline{\mathbf{B}} \boldsymbol{\theta}+\boldsymbol{\eta}
$$

Substituting (11) into (13) and applying the equality $\{\mathbf{b}\} \mathbf{M}^{T} \boldsymbol{\theta}^{\prime}=\left\{\mathbf{M}^{T} \boldsymbol{\theta}^{\prime}\right\} \mathbf{b}$ yields

$$
\mathbf{y}=\mathbf{M} \mathbf{D}_{\mathbf{x}} \operatorname{diag}\left\{\mathbf{M}^{T} \theta^{\prime}\right\} \mathbf{b}+\boldsymbol{\eta}
$$

Defining the notation

$$
\mathbf{A}_{\theta^{\prime}} \triangleq \mathbf{M} \mathbf{D}_{\mathbf{x}} \operatorname{diag}\left\{\mathbf{M}^{T} \theta^{\prime}\right\}
$$

yields the following equation.

$$
y=\mathbf{A}_{\theta^{\prime}} \mathbf{b}+\boldsymbol{\eta}
$$

where the matrix $\mathbf{A}_{\theta^{\prime}} \in \mathbb{R}^{N \times L}$ depends on $\theta^{\prime}$. It turns out that, if the pre-event network topology (i.e. $\mathbf{M}$ and $\mathbf{D}_{\mathbf{x}}$ ) and the post-event phasor angle vector $\boldsymbol{\theta}^{\prime}$ are given, then $\mathbf{A}_{\theta^{\prime}}$ can be computed via (15).

## C. LINE OUTAGE IDENTIFICATION PROBLEM

Given the noisy observation $\mathbf{y}$ in (14), the objective of optimization problem is to obtain the vector $\mathbf{b}$ i.e. identify the lines that belong to $\tilde{\mathcal{E}}$. Formally, the optimization problem for power line outage identification can be formulated as,

$$
\text { P1: } \tilde{\mathbf{b}}=\underset{\mathbf{b} \in\{0,1\}^{L}}{\arg \min } \mathcal{F}_{1}\left(\mathbf{b} ; y, \mathbf{A}_{\theta^{\prime}}\right)
$$

where $\mathcal{F}_{1}$ is the objective function of $\mathbf{b}$ in the model (16) which is defined as

$$
\text { P1: } \tilde{\mathbf{b}}=\underset{\mathbf{b} \in\{0,1\}^{L}}{\arg \min }\left\|\mathbf{y}-\mathbf{A}_{\theta^{\prime}} \mathbf{b}\right\|_{2}^{2}
$$

The above objective function is evaluated on the basis of $1_{2}$ norm of least square criterion. For a network consisting of $L$ lines, the number of possible combinations of line outages is $2^{L}$. Hence, exhaustive enumeration of all possible line outages is not feasible for practical sized networks. In order to solve this problem in linear time, this work considers the probabilistic Bayesian evolutionary approach which is metaheuristic in nature and computationally efficient as compared to exhaustive search.

## III. PROPOSED ESTIMATION OF OUTAGE DETECTION (EOD) AND EOD-THRESHOLD ALGORITHMS

In order to provide a better insight into the proposed solution, this section begins by discussing the main features of classical EDA. The discussion is extended later to the proposed EOD and EOD-Threshold algorithms for MLOD problem.

![img-2.jpeg](img-2.jpeg)

FIGURE 3. Overview of estimation of distribution algorithm.

## A. EDA Bayesian ALGORITHM

Estimation of distribution algorithms (EDAs) are the iterative, population based stochastic optimization methods. They are based on probabilistic modelling of candidate solutions to the problem. Unlike the classical evolutionary algorithms e.g. genetic algorithm, mutation or crossover operations are not used to generate the new population. Instead, the individuals of new population are generated based on sampling of probability distribution of best selected candidates of previous population. Moreover, while in other evolutionary algorithms, the new candidates are generated by an implicit distribution defined by variation variables, in EDAs the interrelations between the candidates are expressed through an explicit probability distribution encoded by a multivariate normal distribution, Bayesian network or another model class. The binary EDA is formally outlined by the following steps.

## 1) GENERATION OF INITIAL POPULATION

The EDA begins with a generation of an initial population, a matrix of dimensions $P_{x} \times L$, where $P_{x}$ denotes the number of candidate solutions, i.e., the population size and $L$ denotes the size of each individual candidate. Each candidate individual is represented by a row vector $X=\left(x_{1}, x_{2}, x_{3}, \ldots, x_{L}\right)$, where $x_{i} \in\{0,1\}$. The initial population is represented as,

$$
\Lambda_{0}=\left(\begin{array}{c}
X^{1} \\
X^{2} \\
\vdots \\
X^{P_{x}}
\end{array}\right)=\left(\begin{array}{cccc}
x_{1}^{1} & x_{2}^{1} & \cdots & x_{L}^{1} \\
x_{1}^{2} & x_{2}^{2} & \cdots & x_{L}^{2} \\
\vdots & \vdots & \vdots & \vdots \\
x_{1}^{P_{x}} & x_{2}^{P_{x}} & \cdots & x_{L}^{P_{x}}
\end{array}\right)
$$

The initial population is typically obtained by sampling over an initialization model that represents uniform (equally likely) distribution over admissible solutions.

## 2) FITNESS EVALUATION

After generating the initial population, the iterative process begins until some termination criterion is not met. During each iteration, all individuals of current population are first evaluated for a given objective/fitness function $\mathcal{F}$. In our MLOD problem, the fitness function is given in (18). In the next step, the candidates of current population are sorted in terms of their fitness values.

## 3) SELECTION OF HEALTHY CANDIDATES

At this step, the best $N_{b p}=\rho_{s} \times P_{s}$ individuals are selected from the sorted current population, where $\rho_{s}$ is the probability of selection given as an input to the algorithm.

## 4) PROBABILITY MODEL ESTIMATION FOR NEXT GENERATION

Estimate the probability distribution $P\left(\theta_{1}, \theta_{2}, \ldots, \theta_{L}\right)$ on the basis of $N_{b p}$ best candidate solutions. The probability distribution denotes the probability of ' 1 ' in each column. We denote this estimation by:

$$
P r_{1}=P\left(\theta_{1}, \theta_{2}, \ldots, \theta_{L} \mid N_{b p}\right)
$$

## 5) GENERATION OF NEW POPULATION

New $\left(P_{s}-N_{b p}\right)$ individuals are generated using the probability distribution $P r_{1}$. These individuals are combined with the previous best individuals to generate a new population for next generation (iteration).

## B. ESTIMATION OF DETECTION (EOD) ALGORITHM

This section discusses in detail, the proposed solution to MLOD problem of Section II. The proposed EOD algorithm is derived from the classical EDA discussed above.

The computational steps of proposed EOD solution are shown in Algorithm 1 and its important variables and functions are listed in Table 4. A graphical overview of EOD (Algorithm 1) is shown in Fig. 3.

```
Algorithm 1 Estimation of Detection (EOD) Algorithm for
MLOD Problem
    1: Initialize Parameters:
2: \(L \leftarrow\) Number of Lines in Power System,
3: \(\rho_{s} \leftarrow 0.4, P_{h t} \leftarrow 0.85, P_{l t} \leftarrow 0.15\),
4: \(P_{h} \leftarrow 0.75, P_{l} \leftarrow 0.25, N_{t h} \leftarrow 5\),
5: \(P_{\text {val }} \leftarrow 0, \Omega_{g} \leftarrow \infty, \Omega_{p} \leftarrow \infty, B_{p}(1,1: L) \leftarrow 0\),
6: \(B_{G}(1,1: L) \leftarrow 0, N_{c} \leftarrow 0\)
7: \(N_{b} \leftarrow\left\lceil\rho_{s} \cdot P_{s}\right\rceil\)
8: \(\operatorname{Pr}_{G}(1: G, 1: L) \leftarrow 0.5\)
9: \(\operatorname{Pr}_{b s}(1,1: L) \leftarrow 0\)
10: Pop \(\leftarrow\) random \(\left(1: P_{s}, 1: L\right)<0.5\)
11: \(g \leftarrow 1\)
12: \(f_{t h} \in\{0,1\}\)
13: Execution:
14: while \(g \leq G\) do
15: \(\Lambda_{g} \leftarrow \mathcal{F}(P o p)\)
16: \(\left[\Gamma_{f} \Gamma_{g}^{\uparrow}\right] \leftarrow \mathcal{S}\left(\Lambda_{g}\right)\)
17: \(\Omega_{p} \leftarrow \Gamma_{f}(1)\)
18: \(\quad B_{p} \leftarrow \operatorname{Pop}\left(\Gamma_{g}^{\uparrow}(1), 1: L\right)\)
19: if \(\Omega_{p}<\Omega_{g}\) then
20: \(\Omega_{g} \leftarrow \Omega_{p}\)
21: \(\quad B_{G} \leftarrow B_{P}\)
22: end if
23: \(\Gamma_{g}^{s} \leftarrow \Gamma_{g}^{\uparrow}\left(1: N_{b}\right)\)
24: \(\operatorname{Pop}\left(1: N_{b}, 1: L\right) \leftarrow \operatorname{Pop}\left(\Gamma_{g}^{s}, 1: L\right)\)
25: \(\operatorname{Pop}\left(N_{b}+1: P_{s}, 1: L\right) \leftarrow 0\)
26: \(\operatorname{Pr}_{b s}(1, l) \leftarrow \frac{\sum \operatorname{Pop}\left(1: N_{b}, l\right)}{N_{b}} \forall l=1: L\)
27: if flag then
28: $\quad \operatorname{Pr}_{b s} \leftarrow \operatorname{Threshold}\left(P_{\text {val }}, \Omega_{g}, N_{c}, N_{t h}, \operatorname{Pr}_{b s}, P_{h t}, P_{l t}\right)$
29: end if
30: \(\operatorname{Pr}_{\text {pop }} \leftarrow \operatorname{Rep}\left(P_{s}, \operatorname{Pr}_{b s}, 1\right)\)
31: \(P_{\text {temp }} \leftarrow\) random \(\left(1: P_{s}, 1: L\right) \in[0,1]\)
32: \(\operatorname{Pop}\left(1: P_{s}, 1: L\right) \leftarrow\left(P_{\text {temp }}<\operatorname{Pr}_{\text {pop }}\right) \in[0,1]\)
33: \(\operatorname{Pr}_{G}(g,:) \leftarrow \operatorname{Pr}_{b s}\)
34: \(\quad g \leftarrow g+1\)
35: end while
36: \(\hat{b} \leftarrow B_{G}\)
37: Outputs: \(\hat{b}, \Omega_{g}\)
```

The algorithm takes as input, the binary vector $b=$ $\left\{b_{1}, \cdots, b_{L}\right\}$, which represents a possible line outage combination and noise corrupted observation vector $y$. A zero at bit position $b_{i}$ of $b$ indicates a normal line whereas, a one indicates an outaged line. The optimization goal is to minimize the fitness function (18). During the initialization phase, the main parameters of the algorithm are initialized which include number of lines $L$ in the system, population size $P_{s}$, number of algorithm generations $G$ and the best selection probability $\rho_{s}$ etc. The random binary population

TABLE 4. Variables description of algorithms 1 and 2.

| Variable | Detail |
| :--: | :--: |
| $G$ | Number of generations of algorithm |
| $L$ | Number of transmission lines in the power grid |
| $P_{s}$ | Size of population |
| $\rho_{s}$ | Probability of selection of best candidates |
| $P_{h t}, P_{l t}$ | Upper and lower threshold limits respectively of probability |
| $P_{h}$ | Upper probability value |
| $P_{l}$ | Lower probability value |
| $N_{t h}$ | No. of generations after which thresholding is applied |
| $P_{\text {val }}$ | temporary variable for holding population best probability |
| $\Omega_{g}$ | Global best fitness value |
| $\Omega_{p}$ | Local (population) best fitness value |
| $B_{p}$ | Population best individual |
| $B_{G}$ | Global best individual |
| $\hat{b}$ | Output of algorithm, the estimated line outage vector |
| $N_{b}$ | Number of best selected candidates |
| $\operatorname{Pr}_{h s}$ | The vector of size $P_{s} \times L$ containing joint probability distribution for best selected candidates |
| $\operatorname{Pr}_{G}$ | The matrix containing generation wise $\operatorname{Pr}_{h s}$ vectors |
| Pop | The population matrix |
| $f_{t h}$ | binary flag to control the threshold function on $\operatorname{Pr}_{h s}$ |
| $\mathcal{S}(x)$ | Sorting function: sorts the vector $x$ in ascending order |
| $\operatorname{Rep}(a, b, 1)$ | Matrix replication function. Produces a matrix which consists of $a$ copies of vector $b$ concatenated in vertical order |
| $\lceil$. | Ceil function |
| $\Lambda_{g}$ | Column vector of size $P_{s}$ stores the fitness values of all individuals of Pop |
| $\Gamma_{g}^{\uparrow}$ | Indexes of sorted values of $\Lambda_{g}$ |
| $\Gamma_{f}$ | Actual values of $\Lambda_{g}$ after sorting |
| $\Gamma_{g}^{s}$ | Indexes of best selected solutions |
| $\mathcal{F}$ | objective function (18) |
| $X(1: r, 1: c)$ | rows from 1 to $r$ and columns from 1 to $c$ of matrix $X$ |

matrix Pop of size $P_{s} \times L$ is generated similar to the one represented in (19). The population is generated by sampling the uniform distribution i.e. the probability $\operatorname{Pr}\left(b_{i j}=0\right)=$ $\operatorname{Pr}\left(b_{i j}=1\right)=0.5$, where $b_{i j}$ represents a bit at row $i$ and column $j$ of Pop.

The second phase is the execution phase which runs for $G$ iterations. During each iteration, all individuals of Pop are evaluated by applying the objective function $\mathcal{F}$ of (18) and corresponding fitness values are saved in vector $\Lambda_{g}$. In the next step, the function $\mathcal{S}$ sorts the fitness values of $\Lambda_{g}$ in

ascending order and the resulting sorted values are stored in vector $\Gamma_{f}$ along with their indexes in vector $\Gamma_{g}^{\uparrow}$. Since, the optimization goal is minimization of objective function $\mathcal{F}$ therefore, the first value of $\Gamma_{f}$ is the minimum fitness value of current population. This value is named as the population best and denoted by $\Omega_{p}$. During each iteration, the population best fitness $\Omega_{p}$ is compared with the global best fitness $\Omega_{g}$, if $\Omega_{g}$ is greater than $\Omega_{p}$, it is replaced by $\Omega_{p}$. Next step is the selection of $N_{b}=\left\lceil\rho_{s} \times P_{s}\right\rceil$ best individuals of Pop. To do so, the individuals of Pop whose indexes are stored in the first $N_{b}$ entries of $\Gamma_{g}^{\uparrow}$ are selected and stored back at first $N_{b}$ rows of Pop whereas, the remaining individuals of Pop are discarded (i.e. set to zero). In the next step, the joint probability of best selected candidates is obtained. For this purpose, the vector $P r_{b s}$ of length $L$ is computed such that the value at index $l=\{1, \cdots, L\}$ of $P r_{b s}$ is obtained by taking the sum of binary values in the $l$-th column of Pop and dividing the sum by the number $N_{b}$.

In order to avoid the premature convergence of proposed solution, an efficient thresholding is applied to $\operatorname{Pr}_{b s}$ vector and the EOD algorithm is thus named as EOD-Threshold. The threshold function routine is given in Algorithm 2 and is enabled by the $f_{t h}$ flag. The global best fitness value $\Omega_{g}$ is monitored and if it remains same for a pre-defined number of iterations $N_{t h}$, then the probability values of $\operatorname{Pr}_{b s}$ are investigated. If the probabilities exceed $P_{b t}$, they are clipped to $P_{b}$ value. Similarly, if they go below $P_{l t}$, they are clipped to $P_{l}$. The thresholds values are obtained through extensive simulations and are presented in the initialization phase of Algorithm 1. After applying the threshold, the probability matrix for the whole population is generated by applying the replication operator Rep which generates $P_{s}$ copies of $P r_{b s}$ vector and cascades them in vertical order. Finally, the next population Pop is obtained for the next generation. The output of the algorithm are the global best individual $\hat{b}$ and its fitness value $\Omega_{g}$.

## IV. PERFORMANCE EVALUATION

The proposed solution is implemented in Matlab. The simulations are performed for IEEE-14 and 57 bus systems. The MatPower [34] simulation tool is used to extract the topology information and other necessary parameters for these systems. To compare with the proposed EOD solution, a number of other meta-heuristics are also implemented namely; the genetic algorithm (GA), binary particle swarm optimization (BPSO) and cross entropy optimization (CEO). Simulation results are shown for up to five outages; however, the EOD solution is capable to blindly identify any combination and number of line outages. The simulation results are the average of a number of Monte Carlo runs of the above mentioned algorithms. In each Monte Carlo iteration, the algorithm executes its $G$ generations and outputs its global best solution $\hat{b}$, an estimated line outage vector.

In order to quantify the results and comparison, two performance metrics have been adopted in this work. The first one is named as percentage improvement (PI). The PI of proposed

```
Algorithm 2 Threshold Function Routine
    Inputs : \(P_{\text {val }}, \Omega_{g}, N_{c}, N_{t h}, P r_{b s}, P_{b t}, P_{l t}\)
    if \(P_{\text {val }} \neq \Omega_{g}\) then
        \(P_{\text {val }} \leftarrow \Omega_{g}\)
        \(N_{c} \leftarrow 0\)
    else
        \(N_{c} \leftarrow N_{c}+1\)
    end if
    if \(N_{c}>N_{t h}\) then
        \(N_{c} \leftarrow 0\)
        for \(l=1: L\) do
            if \(P r_{b s}(l) \geq P_{H T}\) then
                \(P r_{b s}(l) \leftarrow P_{H}\)
            else if \(P r_{b s}(l) \leq P_{L T}\) then
                \(P r_{b s}(l) \leftarrow P_{L}\)
            end if
        end for
    end if
    Outputs: \(P r_{b s}\)
```

algorithm over another algorithm $X$ is defined as

$$
P I=\frac{S_{E O D}-S_{X}}{S_{X}} \times 100
$$

where $S_{E O D}$ and $S_{X}$ denote respectively the number of successes of proposed EOD solution and another solution $X$. An algorithm success occurs when the input line outage vector $b$ is exactly equal to the estimated line outage vector $B_{G}$. A failure occurs when these vectors differ by at least one bit. The positive value of PI indicates that the proposed solution achieves a greater number of successes as compared to the other solution. PI provides a good picture of algorithm's overall performance. However, it may be possible that an algorithm achieves a high success rate but at the cost of large number of generations. To account for this factor, another metric is adopted and named as success generation ratio (SGR). The SGR of a solution $X$ is defined as:

$$
S G R_{X}=\frac{S_{X} / I_{X}}{G_{X} / G}
$$

where $I_{X}$ denotes the total number of Monte Carlo runs of algorithm $X, G$ denotes the generations per Monte Carlo iteration and $G_{X}$ denotes the mean of best generations. $G_{X}$ is defined as

$$
\bar{G}_{X}=\frac{\sum_{i \in\left\{1, \cdots, I_{X}\right\}} g_{b}(i)}{I_{X}}
$$

For each Monte Carlo iteration $i \in\left\{1, \cdots, I_{X}\right\}$, the best generation value $g_{b} \in\{1, \cdots, G\}$ is noted which corresponds to the generation number beyond which the algorithm no more converges. The mean best generation $\bar{G}_{X}$ is obtained by adding the $g_{b}$ values for all Monte Carlo iterations dividing the sum by $I_{X}$. The numerator of (22) corresponds to the success rate of algorithm whereas, the denominator corresponds to the convergence rate of algorithm. Smaller value

![img-6.jpeg](img-6.jpeg)
(b) $P_{s}=50, G=100$
![img-4.jpeg](img-4.jpeg)
(c) $P_{s}=100, G=200$

FIGURE 4. PI of the proposed EOD-Threshold v.s. other algorithms for IEEE-14 bus system. (a) $P_{s}=20, G=50$. (b) $P_{s}=50, G=100$. (c) $P_{s}=100, G=200$.
of denominator means a fast convergence rate. A high value of SGR means a high success rate with fast convergence rate.

In Figs. 4 and 5, the results are plotted for IEEE-14 bus system for $P_{s}$ ranging from 20 to 100 and $G$ ranging from 50 to 200. First, Fig. 4 plots the PI of EOD-Threshold
![img-5.jpeg](img-5.jpeg)
(b) $P_{s}=50, G=100$
![img-6.jpeg](img-6.jpeg)

FIGURE 5. Success Generation Ratio (SGR) results for IEEE-14 bus system. (a) $P_{s}=20, G=50$. (b) $P_{s}=50, G=100$. (c) $P_{s}=100, G=200$.
over other algorithms including the EOD without thresholding. For a scenario consisting of small values of $P_{s}=20$ and $G=50$, Fig. 4 (a) demonstrates that the EOD-Threshold achieves a very large PI over other algorithms. This is due to the fact that EOD-Threshold achieves a very high number

![img-7.jpeg](img-7.jpeg)

FIGURE 6. Percentage improvement of the proposed EOD-Threshold for IEEE-57 with $P_{s}=500, G=200$.
![img-8.jpeg](img-8.jpeg)

FIGURE 7. Success Generation IEEE-57 with $P_{s}=500, G=200$.
of successes thanks to the efficient thresholding technique, while other algorithms get stuck in local optima. Furthermore, the plots of Figs. 4 (b) and (c) reveal that although the PI of EOD-Threshold decreases with increase in $P_{s}$ and $G$ values, still the PI is fairly large and positive. Moreover, the EOD-Threshold achieves a maximum PI over CEO. Overall, the results of Fig. 4 demonstrate the advantage in terms of accuracy of the proposed EOD-Threshold solution. The SGR results for same scenarios are reported in Fig. 5. For $P_{s}=20$ and $G=50$, Fig. 5 (a) reveals that maximum SGR is obtained by EOD-Threshold. This trend changes in Figs. 5 (b) and (c) where the SGR performance is dominated by simple EOD algorithm, as the aim of thresholding is to increase the accuracy (PI) of solution at the cost of a greater number of generations. It is worth to mention here that, by adjusting the values of thresholds $P_{H T}$ and $P_{L T}$, one can trade between accuracy and convergence rate of solution. If accuracy (PI) is the prime objective, one can apply the EOD with thresholding. Otherwise, simple EOD algorithm can be applied to achieve a high SGR. As a matter of fact, setting the values of $P_{H T}=1$ and $P_{L T}=0$, the EOD-Threshold algorithm becomes the simple EOD algorithm.

For a considerably larger network such as IEEE-57 bus system, the simulation results are demonstrated in Figs. 6 and 7. Here, considerably large $P_{s}$ and $G$ values have been selected and PI plot of Fig. 6 demonstrates the accuracy of EODThreshold with respect to other algorithm. For all values of lines in outage, the EOD-Threshold achieves a positive, fairly large PI value and hence shows a better success rate as compared to other solutions. The plot of Fig. 7 demonstrates that the SGR performance is dominated by the simple EOD solution. However, the EOD-Threshold also achieves an SGR fairly larger than other solutions and comparable to simple EOD algorithm. Therefore, for such case, the EOD-Threshold solution is a good option in terms of accuracy and convergence rate.

## V. CONCLUSIONS

To avoid the grid-wide blackouts, an accurate and prompt line outage identification method is required. For a system consisting of $L$ lines, the complexity of exhaustive search is $2^{L}$, which is clearly infeasible for practical sized smart grids. The published works on line outage identification are limited to identify only a fixed (usually small) number of lines in outage. As a key contribution, this work applies the Bayesian probability theory to solve the MLOD problem in linear time. The proposed solution named as estimation of outage detection (EOD) is accurate to identify any arbitrary number and combination of line outages. Moreover, the solution avoids the local optima, thanks to an efficient thresholding routine applied to update the probabilities of candidate solutions. The simulations of proposed solution are carried out for IEEE-14 and -57 bus systems. The results are compared with a number of meta-heuristics. To have an unbiased comparison, two performance metrics have been introduced in the paper namely the success generation ratio (SGR) and performance improvement (PI). These metrics quantify respectively the convergence rate and accuracy of solution. For a number of random line outage scenarios, the simulation results demonstrate that the proposed solution achieves a better PI and SGR as compared to other meta-heuristics. This confirms the validity of proposed approach as well as its applicability to practical smart grids.

## REFERENCES

[1] A. G. Phadke, "Synchronized phasor measurements in power systems," IEEE Comput. Appl. Power, vol. 6, no. 2, pp. 10-15, Apr. 1993.
[2] D. Ghosh, T. Ghose, and D. K. Mohanta, "Communication feasibility analysis for smart grid with phasor measurement units," IEEE Trans Ind. Informat., vol. 9, no. 3, pp. 1486-1496, Aug. 2013.
[3] A. Moreno-Munoz, V. Pallares-Lopez, J. J. G. de la Rosa, R. Real-Calvo, M. Gonzalez-Redondo, and I. M. Moreno-García, "Embedding synchronized measurement technology for smart grid development," IEEE Trans. Ind. Informat., vol. 9, no. 1, pp. 52-61, Feb. 2013.
[4] H. Morais, P. Vancraeyveld, A. H. B. Pedersen, M. Lind, H. Jóhannsson, and J. Østergaard, "SOSPO-SP: Secure operation of sustainable power systems simulation platform for real-time system state evaluation and control," IEEE Trans. Ind. Informat., vol. 10, no. 4, pp. 2318-2329, Nov. 2014.
[5] K. G. Borosjeni, M. H. Amini, and S. S. Iyengar, "Overview of the security and privacy issues in smart grids," in Smart Grids: Security and Privacy Issues. Cham, Switzerland: Springer, 2017, pp. 1-16.

[6] K. Yamashita, S.-K. Joo, J. Li, P. Zhang, and C.-C. Liu, "Analysis, control, and economic impact assessment of major blackout events," Int. Trans. Elect. Energy Syst., vol. 18, no. 8, pp. 854-871, 2008.
[7] D. J. Gaushell and H. T. Darlington, "Supervisory control and data acquisition," Proc. IEEE, vol. 75, no. 12, pp. 1645-1658, Dec. 1987.
[8] B. Singh, N. K. Sharma, A. N. Tiwari, K. S. Verma, and S. N. Singh, "Applications of phasor measurement units (PMUs) in electric power system networks incorporated with FACTS controllers," Int. J. Eng., Sci. Technol., vol. 3, no. 3, pp. 64-82, 2011.
[9] J. Tang, J. Liu, F. Ponci, and A. Monti, "Adaptive load shedding based on combined frequency and voltage stability assessment using synchrophasor measurements," IEEE Trans. Power Syst., vol. 28, no. 2, pp. 2035-2047, May 2013.
[10] R. O. Burnett, Jr., M. M. Butts, and P. S. Sterlina, "Power system applications for phasor measurement units," IEEE Comput. Appl. Power, vol. 7, no. 1, pp. 8-13, Jan. 1994.
[11] H. Zhu and Y. Shi, "Phasor measurement unit placement for identifying power line outages in wide-area transmission system monitoring," in Proc. HICSS, Jan. 2014, pp. 2483-2492.
[12] A. Enshaee, R. A. Hooshmand, and F. H. Fesharaki, "A new method for optimal placement of phasor measurement units to maintain full network observability under various contingencies," Electr. Power Syst. Res., vol. 89, pp. 1-10, Aug. 2012.
[13] J. Aghaei, A. Baharvandi, A. Rabiee, and M. A. Akbari, "Probabilistic PMU placement in electric power networks: An MILP-based multiobjective model," IEEE Trans Ind. Informat., vol. 11, no. 2, pp. 332-341, Apr. 2015.
[14] A. Y. Abdelaziz, S. F. Mekhamer, M. Ezzat, and E. F. El-Saadany, "Line outage detection using support vector machine (SVM) based on the phasor measurement units (PMUs) technology," in Proc. IEEE Power Energy Soc. General Meeting, San Diego, CA, USA, Jul. 2012, pp. 1-8.
[15] J. E. Tate and T. J. Overbye, "Line outage detection using phasor angle measurements," IEEE Trans. Power Syst., vol. 23, no. 4, pp. 1644-1652, Nov. 2008.
[16] J. E. Tate and T. J. Overbye, "Double line outage detection using phasor angle measurements," in Proc. IEEE Power Energy Soc. General Meeting, Calgary, AB, Canada, Jul. 2009, pp. 1-5.
[17] H. Zhu and G. B. Giannakis, "Sparse overcomplete representations for efficient identification of power line outages," IEEE Trans. Power Syst., vol. 27, no. 4, pp. 2215-2224, Nov. 2012.
[18] R. Y. Rubinstein and D. P. Kroese, The Cross-Entropy Method: A Unified Approach to Combinatorial Optimization, Monte-Carlo Simulation and Machine Learning. New York, NY, USA: Springer, 2013.
[19] T. Banerjee, Y. C. Chen, A. D. Dominguez-Garcia, and V. V. Veeravalli, "Power system line outage detection and identificationA quickest change detection approach," in Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP), Florence, Italy, May 2014, pp. 3450-3454.
[20] R. Emami and A. Abur, "Tracking changes in the external network model," in Proc. IEEE North Amer. Power Symp. (NAPS), Arlington, TX, USA, Sep. 2010, pp. 1-6.
[21] P. R. Bijwe, J. Nanda, and K. L. Puttabuddhi, "Ranking of line outages in an AC-DC system causing overload and voltage problems," IEE Proc. C-Generat., Transmiss. Distrib., vol. 138, no. 3, pp. 207-211, May 1991.
[22] J. Hao, R. J. Piechocki, D. Kaleshi, W. H. Ching, and Z. Fan, "Smart grid health monitoring via dynamic compressive sensing," in Proc. IEEE PES Innov. Smart Grid Technol. Eur. (ISGT EUROPE), Kongens Lyngby, Denmark, Oct. 2013, pp. 1-5.
[23] M. M. M. El-Arini, S. A. Soliman, and A. M. Al-Kandari, "A fast technique for outage studies in power system planning and operation," Electr. Power Syst. Res., vol. 32, no. 3, pp. 203-211, Mar. 1995.
[24] H. Ren, I. Dobson, and B. A. Carreras, "Long-term effect of the n-1 criterion on cascading line outages in an evolving power transmission grid," IEEE Trans. Power Syst., vol. 23, no. 3, pp. 1217-1225, Aug. 2008.
[25] M. H. Amini, M. Rahmani, K. G. Borvojeni, G. Atia, S. S. Iyengar, and O. Karabasoglu, "Sparsity-based error detection in DC power flow state estimation," in Proc. IEEE Int. Conf. Electro Inf. Technol. (EIT), May 2016, pp. 0263-0268.
[26] A. I. Sarwat, M. Amini, A. Domijan, Jr., A. Damnjanovic, and F. Kaleem, "Weather-based interruption prediction in the smart grid utilizing chronological data," J. Modern Power Syst. Clean Energy, vol. 4, no. 2, pp. 308-315, 2016.
[27] M. Amini, A. I. Sarwat, S. S. Iyengar, and I. Guvenc, "Determination of the minimum-variance unbiased estimator for DC power-flow estimation," in Proc. 40th Annu. Conf. IEEE Ind. Electron. Soc. (IECON), Oct. 2014, pp. 114-118.
[28] K. G. Borvojeni, M. H. Amini, and S. S. Iyengar, "An oblivious routingbased power flow calculation method for loss minimization of smart power networks: A theoretical perspective," in Proc. 15th IEEE Int. Conf. Mach. Learn. Appl. (ICMLA), Dec. 2016, pp. 641-645.
[29] K. G. Borvojeni, M. H. Amini, S. S. Iyengar, M. Rahmani, and P. M. Pardalos, "An economic dispatch algorithm for congestion management of smart power networks," Energy Syst., pp. 1-25, Oct. 2016.
[30] W. Li, J. Zhou, and X. Xiong, "Fuzzy models of overhead power line weather-related outages," IEEE Trans. Power Syst., vol. 23, no. 3, pp. 1529-1531, Aug. 2008.
[31] J. Kim and I. Dobson, "Propagation of load shed in cascading line outages simulated by OPA," in Proc. IEEE Complex. Eng. (COMPENG), Rome, Italy, Feb. 2010, pp. 1-6.
[32] H. Sehwail and I. Dobson, "Locating line outages in a specific area of a power system with synchrophasors," in Proc. IEEE North Amer. Power Symp. (NAPS), Champaign, IL, USA, Sep. 2012, pp. 1-6.
[33] A. Schellenberg, W. Rosehart, and J. Aguado, "Cumulant-based probabilistic optimal power flow (P-OPF) with Gaussian and gamma distributions," IEEE Trans. Power Syst., vol. 20, no. 2, pp. 773-781, May 2005.
[34] R. D. Zimmerman, C. E. Murillo-Sánchez, and R. J. Thomas, "MATPOWER: Steady-state operations, planning, and analysis tools for power systems research and education," IEEE Trans. Power Syst., vol. 26, no. 1, pp. 12-19, Feb. 2011.

ASHFAQ AHMED is currently an Assistant Professor with the Department of Electrical Engineering, COMSATS Institute of Information Technology, Islamabad, Pakistan.

MUHAMMAD AWAIS, photograph and biography not available at the time of publication.

MUHAMMAD NAEEM (SM'16) received the B.S. and M.S. degrees in electrical engineering from the University of Engineering and Technology at Taxila, Taxila, Pakistan, and the Ph.D. degree from Simon Fraser University, BC, Canada, in 2011. From 2012 to 2013, he was a Post-Doctoral Research Associate with the WINCORE Laboratory, Ryerson University, Toronto, ON, Canada. Since 2013, he has been an Assistant Professor with the Department of Electrical Engineering, COMSATS Institute of Information Technology, Islamabad, Pakistan, and a Research Associate with the WINCORE Laboratory, Ryerson University. From 2000 to 2005, he was a Senior Design Engineer with Concept (pvt) Ltd. At the design department of Concept (pvt) Ltd., he participated in the design and development of smart card-based GSM and CDMA pay phones. He is also a Microsoft Certified Solution Developer. His research interests include the optimization of wireless communication systems, non-convex optimization, resource allocation in cognitive radio networks, and approximation algorithms for mixed integer programming in communication systems. He has been a recipient of the NSERC CGS Scholarship.

MUHAMMAD IQRAL is currently an Assistant Professor with the Department of Electrical Engineering, COMSATS Institute of Information Technology, Islamabad, Pakistan.

WALEED EJAZ ( $\mathrm{S}^{\prime} 12-\mathrm{M}^{\prime} 14-\mathrm{SM}^{\prime} 16$ ) received the M.Sc. degree in computer engineering from the National University of Sciences and Technology, Islamabad, Pakistan, the B.Sc. degree in computer engineering from the the University of Engineering and Technology at Taxila, Taxila, Pakistan, and the Ph.D. degree in information and communication engineering from Sejong University, South Korea, in 2014. He also completed certificate courses on Teaching and Learning in Higher Education from the Chang School, Ryerson University, Toronto, Canada. He was a Post-Doctoral Fellow with Queen's University, Kingston, Canada. He was involved in top engineering universities in Pakistan and Saudi Arabia as a Faculty Member. He is currently a Senior Research Associate with the Department of Electrical and Computer Engineering, Ryerson University. His current research interests include Internet of Things, energy harvesting, 5G cellular networks, and mobile cloud computing. He is currently an Associate Editor of the Canadian Journal of Electrical and Computer Engineering and the IEEE Access. In addition, he is handling the special issues in the IET Communications, the IEEE Access, and the Journal of Internet Technology.

ALAGAN ANPALAGAN received the B.A.Sc., M.A.Sc., and Ph.D. degrees in electrical engineering from the University of Toronto, Canada. He joined the Department of Electrical and Computer Engineering, Ryerson University, in 2001 and was promoted to Full Professor in 2010. He served the Department of Electrical and Computer Engineering, Ryerson University, as the Graduate Program Director from 2004 to 2009, and the Interim Electrical Engineering Program Director from 2009 to 2010. During his sabbatical from 2010 to 2011, he was a Visiting Professor with the Asian Institute of Technology and a Visiting Researcher with Kyoto University. He also completed a course on Project Management for Scientist and Engineers with the University of Oxford CPD Center. He currently directs a research group involving in radio resource management and radio access \& networking areas, the WINCORE Laboratory. He is a registered Professional Engineer with the province of Ontario, Canada. He is a Co-Author/Editor of the books Small Cell Networks (Cambridge Press, 2014), Handbook of Green Information and Communication Systems (Academic Press, 2012), and Routing in Opportunistic Networks (Springer-Verlag, 2013). His current research interests include cognitive radio resource allocation and management, wireless cross layer design and optimization, collaborative communication, green communications technologies, machine-to-machine communication, and small cell networks. He has authored over 200 technical papers in his research areas. He was a recipient of the Dean's Teaching Award in 2011, the Faculty Scholastic, Research and Creativity Award in 2010, and the Faculty Service Award from Ryerson University in 2010. He has been as an Associate Editor of the IEEE Communications Society \& Tutoralls since 2012, and the Springer Wireless Personal Communications since 2009. He was an Associate Editor of the IEEE Communications Letters from 2010 to 2013 and the past Editor of the EURASIP Journal of Wireless Communications and Networking from 2004 to 2009. He also served as a Guest Editor for special issues in the ACM/Springer MONET Green Cognitive and Cooperative Communication and Networking in 2012, the EURASIP Radio Resource Management in 3G+ Systems in 2006, and the EURASIP Fairness in Radio Resource Management for Wireless Networks in 2008. He held various positions within the IEEE Canada, including the Chair, the IEEE Central Canada, the Chair (2013-), the IEEE Canada Professional Activities Committee from 2009 to 2011, the IEEE Toronto Section Chair from 2006 to 2007, and the ComSoc Toronto Chapter Chair from 2004 to 2005.

HONGSEOK KIM (S'06-M'10-SM'16) received the B.S. and M.S. degrees in electrical engineering from Seoul National University in 1998 and 2000, respectively, and the Ph.D. degree in electrical and computer engineering from The University of Texas at Austin in 2009. He was a member of Technical Staff with Korea Telecom Labs from 2000 to 2005. He was a PostDoctoral Research Associate with the Department of Electrical Engineering, Princeton University, from 2009 to 2010. He was a member of Technical Staff with Bell Labs, USA, from 2010 to 2011. He is currently an Associate Professor with the Department of Electronic Engineering, Sogang University, South Korea. His research interests include network resource allocation and optimization, including the cross layer design of wireless communication systems, HetSNet, green wireless, MIMO and OFDMA, network economics, Smart Grid and energy ICT. He was a recipient of the Korea Government Overseas Scholarship from 2005 to 2008. He serves as an Editor of the Journal of Communication Networks.