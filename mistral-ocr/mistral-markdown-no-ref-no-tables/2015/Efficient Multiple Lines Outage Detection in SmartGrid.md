# Efficient Multiple Lines Outage Detection in SmartGrid 

Ashfaq Ahmed*, Muhammad Awais*, Muhammad Naeem* ${ }^{\dagger}$, Muhammad Iqbal*, and Alagan Alpalagan ${ }^{\dagger}$<br>*COMSATS Institute of Information Technology, Wah Campus, Pakistan<br>$\dagger$ Ryerson University, Toronto, Canada<br>\{ashfaq.ahmed, muhammadawais\}@ciitwah.edu.pk, \{muhammadnaeem, miqbal1976\}@gmail.com, alagan@ee.ryerson.ca


#### Abstract

To avoid blackouts in the energy system, the knowledge of the state of the power lines has critical importance. To get the timely conscience, Phasor Measurement Units (PMUs) are used to provide real-time synchronized measurements of voltage and current phasors of the buses. The deployment of PMUs is done to first detect any single or multiple line outage, and further to identify the correct line in outage. But if these approaches are applied to more multiple line outages, the search space grows exponentially. To reduce the computational complexity in case of multiple line outage detection, stochastic optimization methods can be used. These methods give near optimal solution with an acceptable computational complexity. In this paper, the use of phasor angle measurements and optimal deployment of PMUs to identify multiple power line outages is investigated. An adaptive version of estimation of distribution algorithm (EDA) is proposed to detect and identify the lines in outage. In this adaptive EDA thresholding technique is introduced in order to get better solutions. It is shown that the proposed algorithm is achieving a better success rate than the other evolutionary techniques.


Index Terms-Estimation of distribution algorithm, smart grids, power systems, line outages.

## I. INTRODUCTION

Phasor measurement units (PMUs) are able to provide GPS-synchronized accurate, temporally correlated and much denser measurements of voltage and current phasors contrary to the traditional sensors [1]. PMUs provide the information related to phasors of the bus voltages and also the time of measurement. The measurement time is required because the PMUs are synchronized devices and usually they communicate to their respected base stations, or with the other PMUs, at the same time. For this particular reason, the PMUs use the common time source [2]. PMUs have already been installed and deployed in many commercial companies. PMU provides numerous applications, like protection, observations and control. Along with other commercial companies, PMUs are widely installed in the transmission grids of major power systems, which has made them more attractive to improve the reliability factors in the power transmission systems [3]. In smart grids, PMUs are installed on buses, who are responsible to take the difference between the phasors of the buses with on of the selected reference bus. Usually the initial phasors of the buses are known, also known as the normal condition. If any line outage occurs, the difference between the phasors indicates it. At this point, the PMUs provide an indication
to the base station of an expected line outage. Along with PMUs, supervisory control and data acquisition (SCADA) [4] is another technique for acquisition of data, and the processing of those data for use by the operator for control of remote devices. But PMUs have been proven as much more efficient solution towards the measurements in terms of resolution, observation state, area coverage etc. [5].

A lot of research work has already been done in the area of line outage detection. The optimal number of PMUs and the optimal placement of PMUs is being addresses in [6]. Various techniques and algorithms have been introduced in the literature for the optimal deployment of the PMUs and for effective detection of line outages. Ref. [7] proposes a support vector machine (SVM) classification tool based on artificial intelligence. SVM uses the output data of PMUs and determine the status of each line. Tate and Overbaye [8] proposed an approach for single line outage detection which is based on PMUs phasor angle measurements and the other parameters of the system topology. The proposed method also provides the power flow of outaged line before the outage has occurred. Later on Tate and Overbaye extended their investigation for double line outage detection in [9]. For double line outage detection, they used the topology information before and after the outage of line along with real time PMU measurements. Mathematically, the approaches used for single and double line outages are based on combinatorial optimization problem. Due to the discrete nature of these topologies, they require comprehensive information of all the topologies used in the power system. The above approaches cannot be used for multiple line outage detection (MLOD), because the search space increases exponentially with an increase in the number of lines. For multiple line outages detection, Zhu proposed an approach called Least Absolute Shrinkage and Selection Operator (LASSO) [10], which is based on compressed sensing technique. Use of LASSO requires information of some basic parameters related to line outage probability and perturbed noise.

The already proposed solutions for MLOD problem addresses only a fixed number of line outages, while in the this paper the proposed solution can be applied irrespective of the number of line outages. The proposed solution is analyzed with maximum of six line outages. To the best of our knowledge, this is the first solution which detects and identifies

a variable number of line outages. An estimation of distribution (EDA) algorithm [11] with thresholding technique is proposed to address MLOD problem. The results have shown that the proposed algorithm achieves the optimal solution in much less computational time than the other state-of-the-art solutions. Also the proposed solution is able to detect and identify much more line outages that the previous solutions. The proposed algorithm is tested with IEEE-14, 30 and 57 bus system network, with single line outage, 2-line outages, 3-line outages, 4-line outages, 5-line outage and 6-line outages. The EDA is susceptible to premature convergence. It can also be stuck at a local optimum solution. The proposed EDAbased algorithm overcomes these weaknesses. The effect of thresholding is investigated on the line outage detection and identification problem.

Notations: Lower- (upper-) case boldface letters denote matrices and vectors, respectively; calligraphic letters stand for sets; upper normal letters denote single values; $(\cdot)^{T}$ denotes transpose operation; $\left(x_{1}: x_{2}, y_{1}: y_{2}\right)$ denotes the rows from $x_{1}$ to $x_{2}$ and columns from $y_{1}$ to $y_{2} ;(.,$.$) denotes all rows$ and all columns; $[\cdot]$ denotes ceil function; random () denotes a uniformly distribution random function; $<$ and $>$ are less than and greater than operators, respectively, and produces a boolean results.

The remaining paper is organized as follows: In Section II, the system model, along with the actual problem statement is defined. In Section III, the EDA and the proposed solution are explained in detail. In Section IV, results are shown and discussed. Finally in Section V, the conclusion on the claims and the final results are drawn.

## II. System Model and Problem definition

## A. Linear DC Power Flow Model

In this section, the system model will be discussed in detail. We modeled a power transmission network with $N$ buses and $L$ transmission lines using a weighted graph $\mathcal{G}=\{\mathcal{N}, \mathcal{E}\}$, where $\mathcal{N}=\{1,2, \ldots, N\}$ and $\mathcal{E}=\{(m, n)\} \subseteq \mathcal{N} \times \mathcal{N}$ represent the set of buses and the set of edges, respectively. For mathematical convenience, we also denote the set of transmission lines by $\mathcal{L}=\{1,2, \ldots, L\}$. For line $l \in \mathcal{L}$ that connects the buses $n$ and $m$, we denote the reactance along $(m, n)$ by $x_{i}$, as well as $x_{m n}=x_{n m}$, and we define the $i$ th element of its incidence vector $\mathbf{m}_{l}$ as follows:

$$
\mathbf{m}_{l}=\left\{\begin{array}{cll}
1 & , & \text { if } i=n \\
-1 & , & \text { if } i=m \\
0 & , & \text { otherwise }
\end{array}\right.
$$

In this work, we consider the linear DC power flow model defined in [10]. According to conservation-of-flow constraint for power flow in the linear DC model, the injected power to a particular node $n$ must be equal to the total power going out of it. Mathematically it can be written as,

$$
P_{n}=\sum_{m \in \mathcal{N}(n)} P_{n m}=\frac{1}{x_{m n}}\left(\theta_{n}-\theta_{m}\right)
$$

where $\mathcal{N}(n)$ is the set of buses, connected to bus $n$, and $P_{n m}$ denotes the power flowing from buses $m$ to $n$ through their connecting transmission line. Here, $\theta_{n}$ and $\theta_{m}$ are the voltage phasor angles of buses $n$ and $m$, respectively. For ease in notation, the real power injection in $\mathbf{p} \in \mathbb{R}^{N \times 1}$, the voltage phases in $\theta \in \mathbb{R}^{N \times 1}$ and $\mathbf{B} \in \mathbb{R}^{N \times N}$ is a symmetric matrix can be stacked into a vector-matrix form as,

$$
\mathbf{p}=\mathbf{B}^{(k)} \theta^{(k)}, \text { where } k=1,2,3, \ldots, K
$$

where $K$ is the number of possible outage events. $K$ is equal to $2^{L}$, including the normal condition, i.e. the pre-outage can be expressed as [10],

$$
\mathbf{B}=\mathbf{M D}_{\mathbf{x}} \mathbf{M}^{\mathbf{T}}=\sum_{l=1}^{L}\left(\frac{1}{x_{l}} \cdot \mathbf{m}_{l} \cdot \mathbf{m}_{l}^{T}\right)
$$

where $\mathbf{D}_{\mathbf{x}}$ is a diagonal matrix with $1 / x_{l}$ as its $l$ th diagonal entry, and $\mathbf{M}$, formed by the columns $\left\{\mathbf{m}_{l}\right\}_{l=1}^{L}$ of length $N$, is the $N \times L$ bus-line incidence matrix with an $(n, l)$ th entry given by

$$
M_{n l}=\left\{\begin{array}{cl}
1 & \text {, if } l-\text { th line is from } n-\text { th bus } \\
-1 & \text {, if } l-\text { th line is to } n-\text { th bus } \\
0 & \text {, otherwise }
\end{array}\right.
$$

With these definitions, $\mathbf{B}$ can be viewed as the Laplacian matrix of the weighted graph $\mathcal{G}$. We are interested to detect if power line outage occurs, and to identify the outaged line/s in $\mathcal{L}$, where $\mathcal{L} \in L$.

## B. Unveiling Network Faults of Power Line Outage

Given the linear DC power flow model (3), the relationship between the injected power vector $\mathbf{p}$ and the pre-event phasor angle vector $\theta$ is dictated by the topology-dependent matrix B. When an outage occurs on the transmission lines, the interconnected grid is assumed to have reached a stable post-event state. In addition, the post-outage grid remains connected, and the post-event network is given by

$$
\mathbf{p}^{\prime}=\mathbf{p}+\eta=\mathbf{B}^{\prime} \theta^{\prime}
$$

where $\mathbf{B}^{\prime}$ and $\theta^{\prime}$ are the post-event Laplacian matrix of the weighted graph $\mathcal{G}^{\prime}=\{\mathcal{N}, \mathcal{E}\}$ and post-event phasor angle vectors, respectively, and $\eta$ denoted the noise introduced in the post-event DC power flow, which is usually modeled as a Gaussian noise vector with a zero mean and a covariance matrix $\sigma_{n}^{2} \mathbf{I}$ [12]. Substituting the pre-event power flow model (3) into the post-event one in (6) yields

$$
\mathbf{p}+\eta=\mathbf{B} \theta+\eta=\mathbf{B}^{\prime} \theta^{\prime}=(\mathbf{B}-\widehat{\mathbf{B}}) \theta^{\prime}
$$

where $\widehat{\mathbf{B}}$ is the difference between the pre-outage and postoutage Laplacian matrices, respectively, i.e. $\widehat{\mathbf{B}}:=\mathbf{B}-\mathbf{B}^{\prime}$ and can be expressed in terms of the reactances of lines and the indicies between the buses

$$
\overline{\mathbf{B}}=\sum_{l \in \mathcal{E}} \frac{1}{\forall l} \mathbf{m}_{l} \mathbf{m}_{l}^{T}
$$

After any line outage event $K$, the directed graph $\mathcal{G}=\{\mathcal{N}, \mathcal{E}\}$ will be changed to $\mathcal{G}=\left\{\mathcal{N}, \check{\mathcal{E}}\right\}$. Therefore, (8) will find the post-outage Laplacian matrix, where the set of new edges is $\check{\mathcal{E}}$ such that $|\check{\mathcal{E}}|<|\mathcal{E}|$. Therefore, $\overline{\mathbf{B}}$ can be rewritten as,

$$
\overline{\mathbf{B}}=\mathbf{M} \mathbf{D}_{\mathbf{x}} \operatorname{diag}\{\mathbf{b}\} \mathbf{M}^{T}
$$

Here, $\check{\mathcal{E}} \subset \mathcal{E}$ denotes the subset of the lines in outage, and $\mathbf{b}=\left\{b_{l}\right\}_{l=1}^{L}$ where $\mathrm{b} \in \mathbb{B}^{L \times 1}$ and can be given as,

$$
\mathbf{b}_{l}= \begin{cases}1 & , l \in \check{\mathcal{E}} \\ 0, \text { otherwise }\end{cases}
$$

With $\check{\theta}:=\theta^{\prime}-\theta$, the difference model in (7) can be written as,

$$
\mathbf{y} \stackrel{\text { def }}{=} \mathbf{B} \check{\theta}=\overline{\mathbf{B}} \check{\theta}+\eta
$$

Substituting (9) into (11) and applying $\operatorname{diag}\{\mathbf{b}\} \mathbf{M}^{T} \theta^{\prime}=$ $\operatorname{diag}\left\{\mathbf{M}^{T} \theta^{\prime}\right\} \mathbf{b}$ yields,

$$
\mathbf{y}=\mathbf{M} \mathbf{D}_{\mathbf{x}} \operatorname{diag}\left\{\mathbf{M}^{T} \theta^{\prime}\right\} \mathbf{b}+\eta
$$

where

$$
\Lambda_{\theta} \stackrel{\text { def }}{=} \mathbf{M} \mathbf{D}_{\mathbf{x}} \operatorname{diag}\left\{\mathbf{M}^{T} \theta^{\prime}\right\}
$$

which depicts the probability of $b$ given that $b$ vector shows the actual lines in outage. Given the measured $\mathbf{y}$ in (12), our goal is to identify the lines in $\check{\mathcal{E}}$. Mathematically, this power line outage identification problem can be formulated by the following optimization problem,

$$
\mathrm{P} 1: \quad \overline{\mathbf{b}}=\underset{\mathbf{b} \in(\mathbf{0}, \mathbf{1})^{\mathbf{L}}}{\arg \min }\left\|\mathbf{y}-\mathbf{\Lambda}_{\theta^{\prime}} \mathbf{b}\right\|_{\mathbf{2}}^{2}
$$

where (14) depicts the objective functions to be solved in the problem.

Problem in P1 is binary integer linear programming, which is known to be NP hard [13]. It is therefore computationally very complex to find the optimal solution using exhaustive search. If there are $L$ number of lines in a system, the maximum possible outage combination can be $2^{L}$, which means the order of complexity in case of exhaustive search would be $O\left(2^{L}\right)$. It is therefore proposed to find the optimal solution using evolutionary algorithms, which are computationally less complex than the exhaustive search.
![img-0.jpeg](img-0.jpeg)

Figure 1: EDA flow chart

## III. PROPOSED SOLUTION

## A. Proposed Algorithm

A conventional EDA is shown in Fig. 1. The EDA is susceptible to premature convergence. It can also be stuck at a less optimum solution, also known as local minima problem. The proposed algorithm is an updated version of EDA, in which a technique of thresholding is introduced. The proposed solution overcomes the problem of pre-mature convergence of the EDA. The effect of thresholding is investigated on the MLOD and identification problem.

In the proposed EDA Algorithm 1, the thresholding technique is adopted. The algorithm works in the same manner as the classic EDA, except that it monitors the probability distribution of the all features of the solutions. The probability of a particular feature is clipped to pre-defined value, if the probability of the feature exceeds a pre-defined upper or lower threshold.

Table I: Variables description of Algorithm 1
Algorithm 1 EDA Algorithm with Thresholding for MLOD Problem

## Initialize:

$1: L \leftarrow$ Number of lines in IEEE bus system, $\rho_{s}, P_{H T}$, $P_{L T}, P_{H}, P_{L}, N_{\text {thresh }}, P_{\text {val }}, B_{f}, B_{p}(1,1: L)$, $B_{c}(1: G, 1: L), N_{c}, N_{b p}, S_{p}, \operatorname{Pr}_{G}(1: G, 1: L), \operatorname{Pr}_{1}$, $\operatorname{Pop} \leftarrow \operatorname{random}\left(1: P_{s}, 1: L\right)<0.5$

## Execution:

1: while $(i \leq G)$ do
$\operatorname{Pr}_{G}(i,:) \leftarrow P r_{1}$
$\Lambda_{i} \leftarrow \mathcal{F}(\mathcal{P})$
$\left\lceil\Gamma_{f} \Gamma_{i}^{\uparrow}\right\rceil \leftarrow \mathcal{S}\left(\Lambda_{i}\right)$
if $\left(\Gamma_{f}(1)<B_{f}\right)$ then
$B_{f}=\Gamma_{f}(1)$
end if
$\Gamma_{i}^{\downarrow} \leftarrow \Gamma_{i}^{\uparrow}\left(1: N_{b p}\right)$
Pop $\leftarrow \operatorname{Pop}\left(1: \Gamma_{i}^{\downarrow}, 1: L\right)$
$\operatorname{Pr}_{1} \leftarrow \sum \frac{\sum P_{G B 1} ; N_{G 1}(: L)}{\sum N_{G}}$
11: Thresholding Routine : Algorithm 2
$12: \quad \operatorname{Pr}_{\text {mat }} \leftarrow \mathcal{R}\left(\operatorname{Pr}_{1}, 1: P_{s}, 1\right)$
$13: \quad \operatorname{Prob} \leftarrow \operatorname{random}(1: \mathrm{G}, 1: \mathrm{L}) \in[0,1]$
$14: \quad \operatorname{Pop}\left(1: P_{s}, 1: L\right) \leftarrow \operatorname{Prob}<\operatorname{Pr}_{\text {mat }} \in[0,1]$
15: end while

## Outputs:

## Algorithm Description

Most of the important variables used in the Algorithm 1 are shown in Tab. I. The proposed algorithm is analyzed with IEEE 14, 30 and 57 bus systems. The total population is $P_{s} \times L$, where $L$ is the number of transmission lines in the bus system and $P_{s}$ is the population size, i.e., the number of individual solutions. There is an input vector of the algorithm, which is binary in nature. Each ' 0 ' and ' 1 ' in the vector represents the line in normal condition and line in outage, respectively. Therefore, the population contains multiple of expected solutions, which converges to the optimal solution,

```
Algorithm 2 Thresholding Routine
    if \(\left(P_{\text {val }} \neq B_{f}\right)\) then
    \(P_{\text {val }} \leftarrow B_{f}\)
    \(N_{c} \leftarrow 0\)
else
    \(N_{c} \leftarrow N_{c}+1\)
    end if
    if \(\left(N_{c}>N_{\text {thresh }}\right)\) then
        \(N_{c} \leftarrow 0\)
        if \(\operatorname{Pr}_{1} \geq P_{H T}\) then
            \(\operatorname{Pr}_{1} \leftarrow P_{T}\)
        else if \(\operatorname{Pr}_{1} \leq P_{L T}\) then
            \(\operatorname{Pr} 1 \leftarrow P_{L}\)
        end if
    end if
```

i.e. the input solution. The probability of selection is set to 0.4 , which means that during each generation, $40 \%$ best individuals out of the whole population will be selected to produce the offspring. The fitness of the function is calculated using (14). The fitness of each individual is stored in $\Lambda_{i}$. Further, all the fitness are sorted in descending order and are stored in $\Gamma_{f}$ and the corresponding indexes in $\Gamma_{i}^{\uparrow}$. The best fitness of each generation is stored for analysis purpose. Therefore, it is checked in each generation, if the best fitness of the current generation is less than that of the next best fitness value. $B_{f}$ holds the value of the best fitness. The most healthy $N_{b p}$ individuals are selected from the original population. $N_{b p}$ is calculated by multiplying the selection probability with total population size. $N_{b p}$ must always be an integer number, therefore a ceil function [.] is applied after the multiplication. The probability distribution of the healthy solutions are then calculated adding all the features and dividing them by the total numbers of healthy solutions, i.e. $N_{b p}$. In this way, a vector of probabilities is obtained, whose dimension is $(1,1: L)$. The proposed thresholding technique is shown in Algorithm 2. It is checked if the value of the best fitness does not change consecutive $N_{\text {thresh }}$ times, and if the probability value exceeds $P_{H T}$ values, it is clipped to $P_{T}$ value. Similarly, if the best fitness value remains unchanged till $N_{\text {thresh }}$ times, and the probability values goes down below $P_{L T}$, it is clipped to $P_{L}$. In this way a probability distribution $\operatorname{Pr}_{1}$ of dimension $(1,1: L)$ is produced for the offspring production. A function $\mathcal{R}(x)$ is used to make $P_{s}$ number of copies of $\operatorname{Pr}_{1}$ vector. The copies of the probability distribution vector are cascaded in vertical order and this matrix is named as $\operatorname{Pr}_{\text {mat }}$. Finally, a new population is produced $\operatorname{Pr}_{\text {mat }}$.

## IV. ReSULTS \& DISCUSSION

As discussed before, the proposed algorithm is tested in IEEE 14 bus system. The problem is solved using five different evolutionary algorithms, i.e. EDA, Binary Particle Swarm Optimization (BPSO), Cross Entropy (CE), Genetic Algorithm (GA) and finally with the proposed EDA with thresholding. Maximum 6 -line outages are tested in the implementation. It is shown in the results that the proposed algorithm performs far better than all other competitors in detection and further

identification of the line(s) in outage. In order to get a fair conclusion from the algorithms which are random in nature, usually Monte Carlo simulation techniques [14] are adopted. In Monte Carlo simulations, the algorithms are run multiple times, typically thousands of times, and finally mean value of the performance metric is considered. During each Monte Carlo iteration, the algorithms completely run their generations and finally reach the optimal solution, which is in fact a binary vector of dimension $(1, L)$. As discussed in the previous sections, the binary solution contains ' 0 ' and ' 1 ', which indicates a line in normal condition and a line in outage, respectively. If the optimal solution found by the algorithm is equal to the input vector, it indicates a success. A success means the algorithm identifies the lines in outage. The algorithm will be considered unsuccessful even if it identifies a single wrong line in outage.
Success generation ratio (SGR) is an important metric derived for fair comparison of the algorithms. The SGR is given as,

$$
S G R=\frac{E_{x} / I T E R}{G_{x} / G}
$$

where $I T E R$ represents the total number of Monte Carlo iterations, $G_{x}$ represents the mean of best generations of algorithm $x, G$ represents the total number of algorithm generations. The target is to increase the SGR value, which means a larger numerator and smaller denominator is required. The numerator comprises the number of successes of algorithm $x$ during the whole Monte Carlo iterations. It is highly required to get this factor as large as possible. Similarly, in the denominator we have $G_{x}$ which represents the mean of best iterations, i.e., the iteration at which the algorithm has achieved the optimal solution. It is highly required to get this factor as small as possible, i.e. to get the optimal solution in less number of algorithm generations.

Similarly, Fig. 2 shows the SGR of all the five algorithms including the proposed algorithm. It is shown that the proposed algorithm outperforms the other algorithms in case of less $P_{s}$ and less $G$, whereas as soon as we increase the value of $P_{s}$ and $G$, the SGR of the proposed algorithm shows better results for less number of line outages, whereas, for a large number of line outages, the EDA performs betters than the proposed algorithm. The behavior is more likely due to the random nature of algorithm and can be modified by increasing the Monte Carlo iterations. In our case, we have taken the results with very few Monte Carlo iterations, i.e. 1000.

## V. CONCLUSION

In this paper, multiple line outage detection and identification problem is addressed. An efficient EDA algorithm is proposed for line outage detection and identification problem in smart grids. The algorithm uses the thresholding technique, in order to avoid the pre-mature convergence, which leads to overcome the local minima problem. From the simulated results, it is shown that the proposed algorithm gives much better results in terms of successes and improvements than the other evolutionary algorithms. The algorithm is also able to detect and identify multiple line outage. The proposed solution
![img-1.jpeg](img-1.jpeg)

Figure 2: Success Generation Ratio IEEE-14

is able to detect variable number of line outages, where up to six line outages are tested with the proposed solution. The algorithm has been tested on many IEEE bus systems to show that it outperforms on all the different IEEE bus systems.
