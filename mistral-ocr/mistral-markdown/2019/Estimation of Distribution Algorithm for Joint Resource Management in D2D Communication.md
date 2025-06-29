# Estimation of Distribution Algorithm for Joint Resource Management in D2D Communication 

Mushtaq Ahmad ${ }^{2} \cdot$ Muhammad Naeem ${ }^{1,2} \cdot$ Muhammad Iqbal ${ }^{2}$<br>Published online: 7 May 2019<br>(c) Springer Science+Business Media, LLC, part of Springer Nature 2019


#### Abstract

Device to device (D2D) communication technique is one of the established means to enhance data rate in next generation wireless systems. Use of same resource of cellular users by D2D pairs creates interference problem among users. Simultaneous resource management and mode selection in emerging cellular networks having D2D capabilities can surely improve overall system throughput. This work addresses the problem of overall throughput maximization of emerging cellular networks while ensuring the power and interference constraints. The joint resource management problem is NP-Hard and is classified as mixed integer non-linear constraint optimization problem. Due to the fact that, the computational complexity of the system increases exponentially with the increase in users, it is almost impossible to find sub-optimal solution in polynomial time using greedy approach. Therefore, this paper applies evolutionary technique, like estimation of distribution algorithm which has the potential to address the complex problems having combinatorial nature such as joint resource management strategy in D2D. Near optimal solution convergence is achieved by the algorithm with minimal number of iterations. Simulation results show the effectiveness of the proposed approach as compared to other algorithms.


Keywords Device-to-device communication $\cdot$ Admission control $\cdot$ Mode selection $\cdot$ EDA

## 1 Introduction

World wide cellular operators are under tremendous competition and chief executive officers and financial advisors are in search of attractive venues to enhance the revenue base of their companies. Data intensive applications are gaining popularity as an alternative revenue generation sources among telecommunication companies including cellular operators. Examples include services using nearness of subscribers, multimedia applications, videos, gaming sources online, cloud computations and extensive file sharing among users. To meet the high end data rate requirements of subscribers, cellular operators have

[^0]
[^0]:    $\boxtimes$ Muhammad Iqbal miqbal1976@gmail.com
    1 WINCORE Laboratory in the Department of Electrical and Computer Engineering, Ryerson University, Toronto, ON, Canada
    2 COMSATS University Islamabad, Wah Campus, Wah, Pakistan

no choice but to upgrade their network with state of the art new technologies. Regulatory bodies around the globe are no exception. They have to develop new standards accordingly. In order to alleviate heavily congested cellular networks' traffic load, both academia and industry have classified Device to Device Communication (D2D) as a pivotal technology for next generation networks [1, 2]. Integration of D2D capability in the portfolio of services, service offering range is diversified and new financial opportunities like mobile commerce emerge for the rescue of cellular operators in this time of competition and financial crunch. D2D Communication technique is predominately becoming a standard feature of futuristic wireless network to get boost of data rates. D2D is defined as establishment of communication link directly between two cellular users without involvement of Base Station (BS)or eNB. D2D Communication can be classified into In-band and outband D2D Communications. In-band D2D Communication utilizes licensed spectrum of cellular operators. The same radio resources of cellular users are also used by D2D users to enhance the system throughput. On the other hand out-band D2D communication utilizes un-licensed spectrum [3]. The advantages of D2D Communication, inter-alia include: faster call setup time, ease in operation and maintenance of the system [4]. Rightly, realizing the importance of incorporation of newer technical features in next generation wireless networks, 3GPP has advocated to increase the bandwidth of International Mobile Telecommunications (IMT) advance systems upto $100 \mathrm{MHz}[1,5]$. The emerging wireless systems intend to facilitate the provision of enhanced data rates through spectral efficiency improvements [5, 6]. The reference [7], portrays various resource allocation methodologies used by the eNode-B. Non-orthogonal frequency sharing method maximizes spectral efficiency and is also termed as D2D underlay in in-band communication. D2D underlay has been active research area so far. Though popular and having associated advantages, underlay communication poses problem of interference management among cellular and D2D users because of usage of same resource pool by the users belonging from either of the types. To mitigate interference, some researchers earmark a part of cellular band for exclusive use of D2D communication. This type of communication is termed overlay in-band D2D Communication. There may be alternative means available in the market to cater for the needs of enhanced data rates namely, wireless local area networks (WLAN) and wireless personal area networks (WPAN) technologies including Blue tooth, Ultra Wide Band (UWB ) technologies but the major drawback in these technologies is lack of control over interference and requirement of manual peering in these technologies. D2D communication, on the other hand, works through controlled allocation of radio resources in the licensed band by the eNode-B. The problems of manual peering and interference management is alleviated to greater extant in D2D Communication.

The advantages of D2D communication comprise: Latency in the system is improved due to reduction of number of hops, closeness of users is exploited in terms of enhanced data rates, battery life of cell phones is prolonged due to minimum power consumption, more network capacity, increased coverage and improved quality of service [7]. With all added advantages, interference management task in D2D Communication underlay becomes quite challenging [8]. The proposed EDA based, joint resource allocation technique can help in achieving the target of faster data rates for emerging wireless networks.

# 1.1 Related Work 

D2D exploits the proximity gain and facilitates nearby users to directly communicate with each others, thereby, increasing spectral efficiency. In other words same resource blocks

are shared both by cellular as well as D2D users. Coexistence of cellular and D2D users causes interference among the two types of users. In order to mitigate the interference, e-NodeB carefully assigns the resources to the D2D devices. Orthogonal Frequency Division Multiple Access (OFDMA) based resource management scheme for D2D communication is unique technique to allocate radio resources [9, 10]. The proposed technique is implemented in two steps: In first step, the radio resource is allocated to cellular downlink and uplink while ensuring the max-min fairness. In the second step, the scheme implements the D2D flows while ensuring the rate satisfaction constraints for cellular users. The reference [11] discusses mode selection technique without cognizance of distance related information of D2D pairs. In [12], the authors have highlighted modalities using graph theory. They illustrated that how we can use the same uplink channel for D2D and the cellular users to increase data rate. The methodology primarily focuses on interference level reduction and emphasizes that resource assignment and interference handling among D2D and cellular users requires extra care. Fractional frequency reuse (FFR) is a channel allocation technique which basically focusses on interference level management of cells using same channel. D2D and cellular users in outer cell regions experience interference in the tolerable limits [13]. In [14], the authors present contour of a greedy algorithm and successive interference cancelation (SIC) technique, allowing same channel option among different D2D communicating users and conventional cellular users. SIC simultaneously improves the quality of D2D links and reduces interference level experienced by cellular users. The authors have proposed a technique in [15] for improving the spectrum utilization by maximization of the weighted sum rate of D2D and cellular users. In [16] the authors highlight that D2D has the potential to enhance the efficiency of radio resource and improve system throughput by exploiting proximity of devices. In the refrence [17], the authors allocate resources in non-dense macrocell or femtocell networks by proposing an optimization formulation that tries to remove limitations in earlier research work namely, resources under utilization, absence of femtocells selection method. OFDMA is used as spectrum sharing techniques and problem is solved using GA to yield near optimal solution with reduced computation time. The approach maximizes system throughput by power and resource allocation and selection of appropriate base station. Performance is compared with Weighted Water Filling (WWF) algorithm.

In OFDMA based systems, [18] the condition of compliance of quality of service requirement makes it necessary for the scheme to allocate frequency resource while keeping the signal to interference noise ratio of cellular users with in the permissible limits. The scheme consists of two parts. First, sub-carriers are allocated among D2D multi cast groups complying with their minimum data rate requirements and second step involves quality of service of cellular users. For D2D design inclusion, 3GPP LTE system is a starter. Reference [19] is a treatise on a new spectrum sharing protocol. The protocol permits D2D users for two way communication among each other while at the same time also manages bidirectional communications between the BS and cellular users. In [20], the authors developed the mechanism for sharing multiple resource blocks among D2D pairs with the aim to enhance overall system through put. Evolutionary algorithm perform mode selection. In [21], the authors are in favour of distributed implementation. Game theory is used to maximize the overall sum-rate of D2D system. Reference [22] proposes how to handle interference control in DL mode and suggests to choose cellular users close to BS. This technique lowers the BS interference experienced by D2D users. Reference [23] explores resource sharing by considering distributive and cooperative context for the optimal performance of the system in D2D scenario. [24] discusses an interference management methodology which enhances the overall capacity of cellular network. A traditional approach is proposed

to mitigate the interference arising from D2D users. In [25], the authors have proposed an efficient technique to share the resources for the maximum utilization of the spectrum.

The reference [26], examines the problem of resource allocation within a cognitive cellular network with D2D communication capabilities. Secondary users form D2D group to transmit and receive data either in Cellular or D2D mode. Replicator dynamics of evolutionary game theory have been used to opt transmission mode by analysis of optimal power of secondary users. The authors in [27], use Genetic Algorithm (GA) with frequency hopping technique for optimal choice of frequency channels. Cluster based frequency hopping technique is used to mitigate interference effects in D2D Communication. GA searches for the best frequency resource under severe resource constraints and thereby enhances efficiency of D2D Communication. The reference [28] suggests modes selection and resource allocation by using a swarm based optimization technique. The authors suggest to maximize the system overall throughput by ensuring minimum required rate guarantee for D2D communication and is shown that their technique is superior to other schemes. A technique has been proposed in [29] to address the problem of the joint power control, mode selection and channel allocation in the D2D paradigm. Overall system throughput is optimized while observing the SINR of both cellular and D2D Communications. It is shown that the peculiar nature of the problem of joint mode selection and channel assignment make it NP hard. Decomposition technique is used to convert NP hard problem into manageable subproblems. Algorithms of low complexity are developed for different network scenarios. These algorithms can be utilized for obtaining different gains like the proximity gain, the reuse gain and hop gain in D2D communication.

An interference avoidance based resource allocation scheme using Particle Swarm Optimization (PSO) technique has been demonstrated in [30] in order to enhance overall spectral efficiency by allocating the same frequency resource of one Cellular user to more than one D2D pair. After mapping process of PSO, mode selection scheme is highlighted. Performance guarantees for cellular as well as D2D users can be ensured with the proposed scheme. Proposed scheme maximizes the spectral efficiency and minimizes the interference effects. In the past decade, a number of evolutionary algorithms have been proposed in the literature for efficiently solving the complex NP hard problems encountered in D2D resource allocation. One such reference [31] uses Genetic Algorithm based user matching scheme (GAM) which allocates power using multi dimensional optimization techniques. Simulation results testify that the GA based scheme can achieve much enhanced throughput as compared to traditional greedy search, and this gain is possible with minimal amount of complexity enhancement. In [32], authors use modified GA based technique for energy efficient resource allocation of multiple multiplexed resources. GA based scheme not only solves the NP Hard problem, but also significantly lowers the energy consumption. Liotou et al. [33] presents a D2D resource allocator based on Ant Colony Optimization(ACO) theory. ACO exploits identification of interference affected D2D links. Network is represented by weighted connected graph. Weights of the graph symbolise interference levels. Accordingly ACO, assigns more weights to less interference affected D2D links. ACO manages the computational complexity quite well as compared to other traditional resource allocators. The reference [34] presents algorithm which allocates multiplexed resources in mixed mode D2D communication. The authors use de-coupling technique and decompose the NP Hard problem into mixed mode and resource allocation sub-problems which are optimized separately. Sub problems reduce computational complexity. Lagrangian dual decomposition method is employed to solve both sub-problems. In [35], authors suggest GA based heuristic algorithm to improve secrecy of the D2D link. D2D communication inherently being weaker in protection against eavesdropping due to lack of control, realizing

Fig. 1 Comparison of different resource allocation techniques
![img-0.jpeg](img-0.jpeg)
the need of secrecy,the authors have presented joint optimization of power allocation and jammer selection scheme. The work considers the worst case outcast scenario posed as eavesdropper and selection of jammer exploits jammer's inherent social trust property. NP Hard, D2D Secrecy rate maximization problem is simplified to some extent by considering upper bound and lower bound approximation of original D2D Secrecy rate maximization problem. The article [13], highlights that if physical distance among D2D users is large enough, it is possible for D2D pairs to share the same sub-carriers and resultantly have tolerable, weaker co-channel interference. The work proposes joint mode selection and flexible resource reusing method based on evolutionary algorithm techniques to mitigate extra interference introduced because of use of same resource by multiple users.

# 1.2 Contributions 

The literature review unveils that there is no evolutionary algorithm related research work which attempts to maximize the overall system throughput in cellular network having D2D features and simultaneously controls the admission of the users, assigns modes (to be in cellular or D2D mode) and allocates power complying with QoS and interference constraints. As can be seen from Fig. 1, the existing research work deals with individual aspects. This work fills the missing link and attempts to enhance the throughput of the Cellular System having D2D capabilities using EDA with thresholds (statistical based evolutionary algorithm) while jointly considering features of access control, selection of mode and power allocation of users. The main contribution of this article are enumerated as under:

1) A constrained optimization problem of Joint Resource Management (JRM) has been proposed that maximizes the overall system throughput of next generation cellular net-

![img-1.jpeg](img-1.jpeg)

Fig. 2 System model showing D2D and cellular modes
works while jointly managing multifarious tasks like admission of the users, assignment of modes and power control constraints of the cellular users as well as base stations.
2) The JRM belongs to mixed integer non-linear constraint optimization problems class and is NP-Hard. JRM have integer variables. As the number of D2D user pairs increase in the cellular network, the comprehensive search of integer variables which yield optimal solution becomes impossible task and computational complexity increases exponentially. In this paper, we apply statistically based EDA Algorithm which provides near optimal solution for such kind of computationally complex (NP-Hard) problems.
3) Finally, the simulation results are interpreted to explain the near optimal solution .

Paper sections stand organized as per following: Sect. 2 builds the system model and narrates problem statement. In Sect. 3, we delineate JRM technique using EDA with thresholds algorithm. The simulation results are presented in Sect. 4 and last but not the least, paper is concluded in Sect. 5.

# 2 System Model and Problem Formulation 

Schematic diagram of Cellular network with D2D functionality is depicted in Fig. 2. Modes of communication can be classified as, (1) cellular mode and (2) D2D mode. D2D users share frequency resources in nonorthogonal frequency sharing mode. Frequency reuse is deployed to enhance spectral efficiency. Let us assume that $\mathcal{K}$ pairs are desirous of communication. Various powers are denoted by $p_{k}^{a l}, p_{k}^{a l}$ and $p_{k}^{d}$, to represent the uplink power of $k$ th user in cellular mode, the downlink power of the $k$ th user and power of the $k$ th user in D2D mode respectively. $g_{k}$ symbolises the gain of the channel occupied by the $k$ th user pair. The symbols $h_{k}$ and

$f_{k}$ are being used to represent the gain of the channel between sending user-eNB link (uplink) and eNB- recipient (downlink) respectively. Log normal shadowing is represented by $\xi 10^{\frac{\bar{h}_{0}}{10}}$ whereas antenna gain is $G_{o}$ and $\bar{\xi}_{o}$ represents the zero mean Gaussian random variable having standard deviation $\sigma$. The channel $h_{k}$ can be written as [36]:

$$
h_{k}=\bar{h}_{k} \xi G_{o}\left(\frac{d_{o}}{d}\right)^{\alpha}
$$

The symbols used in above equation represent different parameters as per following: Far field reference antenna distance is denoted by $d_{o}$ whereas and $d$ represents the distance between the receiver and transmitter. The path loss constant is represented by $\alpha$ and Rayleigh random variable is denoted by $\bar{h} . C_{k}=\log \left(1+\frac{p_{k}^{a} h_{0}}{N_{0}}\right)$ represents the channel capacity of the $k$ th user in cellular mode while channel capacity of D2D users will $C_{k}=\log \left(1+\frac{p_{k}^{a} g_{k}}{N_{0}}\right)$.

In cellular mode, eNB acts like a relay and two time slots are required for communication; one for uplink and the other one for down link. The $k$ th user rate in cellular mode is given by $C_{k}^{c}=\frac{1}{2} \min \left(C_{k}^{u l}, C_{k}^{d l}\right)$. The possible rate for $k$ th pair in D2D is $C_{k}^{d}=\log \left(1+\frac{p_{k}^{d} g_{k}}{N_{0}}\right)$. Let us define binary mode selection and user admission indicators as per following:

$$
\begin{aligned}
& x_{k}=\left\{\begin{array}{l}
1, \text { Cellular mode } \\
0, \text { D2D mode }
\end{array}\right. \\
& y_{k}=\left\{\begin{array}{l}
1, \text { User admitted } \\
0, \text { User not admitted }
\end{array}\right.
\end{aligned}
$$

QoS Constraint dictates that the user pair under consideration must meet their minimum rate $C_{k}^{\min }$. For a given power related constraint, wireless network is unable to meet every user's rate requirement. This failure is due to many reasons including but not limited to bad channel conditions, weaker battery and higher interference level. Resultantly, some of the users have to be dropped due to their stringent rate requirements. Generally, admission control schemes allow only those users that can enhance aggregate throughput of the system. This paper devises a technique for joint access control and selection of mode in order to maximize the overall throughput of the system and the number of admitted users complying with the power and minimum rate constraint requirements. Users are granted permission to communicate in either of the D2D or cellular mode.

Due to either mode selection (Cellular or D2D), respective rate contribution term in $x_{k} C_{k}^{c}+\left(1-x_{k}\right) C_{k}^{d}$ becomes active (1) and other term becomes non active (0) due to non mode selection. If cellular mode is allocated to any admitted user, then the rate terms related cellular mode $\left(C_{k}^{c}\right)$ contributes and rate contribution from D2D mode ( $C_{k}^{d}$ )becomes zero and vice versa. The constrained optimization mathematical model of JRM becomes as per following:

$$
\max _{Y, X, P} \sum \frac{y_{k}}{K}\left(\sum_{k=1}^{K} x_{k} C_{k}^{c}+\left(1-x_{k}\right) C_{k}^{d}\right)
$$

subject to

$$
\begin{aligned}
& C 1: x_{k} C_{k}^{c}+\left(1-x_{k}\right) C_{k}^{d} \geq y_{k} R_{k}, \forall k \\
& C 2: p_{k}^{d} \leq y_{k}\left(1-x_{k}\right) R^{d} P_{d, k}^{m i n}, \forall k \\
& C 3: p_{k}^{u l} \leq y_{k} x_{k} P_{c, k}^{m u x}, \forall k \\
& C 4: \sum_{k} x_{k} p_{k}^{d l} \leq P_{e N B}^{m u x}, \forall k \\
& C 5: p_{k}^{d l} \leq y_{k} P_{e N B}^{m u x}, \forall k \\
& C 6: x_{k} \in\{0,1\}, y_{k} \in\{0,1\} \forall k \\
& C 7: p_{k}^{d} \geq 0, p_{k}^{u l} \geq 0, p_{k}^{d l} \geq 0, \forall k
\end{aligned}
$$

The problem in (2) is a max-min problem. Let us translate it into equivalent maximization problem by introduction of a new variable $t_{k}, k \in \mathcal{K}$,

$$
\max _{t, Y, X, P} \sum_{k=1}^{K} \frac{y_{k}}{K}\left(\sum_{k=1}^{K} x_{k} t_{k}+\left(1-x_{k}\right) C_{k}^{d}\right)
$$

subject to

$$
\begin{aligned}
& \text { C1-C7 of (2) } \\
& C 8: C_{k}^{u l} \geq x_{k} t_{k}, \forall k \\
& C 9: C_{k}^{d l} \geq x_{k} t_{k}, \forall k
\end{aligned}
$$

The above problem jointly maximizes the users admitted and overall throughput. The constraint $C 1$ ensures compliance of threshold of minimum rate for each admitted user. Users in violations of constraint $C 1$ are not allowed to transmit. Power constraints $C 2, C 3$ and $C 4$, limit the transmit powers for D2D, cellular uplink and cellular down link modes respectively. While in D2D mode, Constraint $C 2$ ensures that out side $R$, the power level of any other D2D user or cellular user would remain lower than $P_{d, k}^{\text {min }}$. Constraint $C 3$ bounds uplink power while $C 4$ limits overall down link power. Constraints, $C 5$ sets threshold on downlink transmit power for admitted users in cellular mode and in any down link transmit power should not exceede the base station maximum power $P_{e N B}^{m u x} . C 6$ allocates binary mode selection and user admission variables. Constraints $C 7$ ensures that if a user is not selected, its respective power becomes zero. Constraints, $C 8$ and $C 9$ ensure quality of uplink and down link data rates of cellular users.

The problem in (3) is a non-convex mixed integer non-linear programming problem and is NP Hard. Optimal solution determination in polynomial time is very difficult for such kind of problems. Computational load exponentially increases as the number of integer variables/users increase. In the next section we shall use EDA for solution of Problem in (3) to yield near optimal solution.

```
Algorithm 1.1 Generic EDA algorithm
    Randomly generate initial population
    while termination criteria meets do
        Find fitness using objective function
        Sort the population based on fitness
        Select the best population
        Compute the probabilities of the selected population
        Apply threshold algorithm if necessary (optional)
        Use the calculated probabilities to generate new popu-
        lation
    end while
```


# 3 Proposed Approach to a Solution 

An EDA optimizes an objective function based on the statistics of the candidate solutions of population. Usually, probability distribution of population is used as statistics [37]. This algorithm has advantage in the sense that storage of candidate solutions are not required rather statistical characteristics are preserved while proceeding ahead in iterations. EDA being iterative algorithm, calculates population using probability of previous generation. The best fit solution, along with iteration counter and fitness value are stored in each iteration. EDA is population based algorithm which discards some of the population and discarded population is exchanged with newly generated population. As we move ahead in iterations, the solution converges to the best population. In EDA with a threshold algorithm, the probability of the typical candidate is shaved off in case the probability of that candidate exceeds the already defined uper or lower limit. In other words, probability is maintained within defined range. Algorithm 1.1 describes pseudo code for implementation of generic EDA.

```
Algorithm 1.2 EDA Algorithm with Thresholding for EDA
based JRM D2D Communication Problem
    Initialization: \(P_{s} \leftarrow 0.5, P_{U T L} \leftarrow 0.75, P_{L T L} \leftarrow 0.25\),
        \(P_{H C} \leftarrow 0.7, P_{L C} \leftarrow 0.3, C_{\text {thresh }} \leftarrow 4, F_{p b v} \leftarrow 0\),
        \(F_{c b v} \leftarrow \infty\), Count \(\leftarrow 0\)
    \(C_{b p} \leftarrow\left\lceil P_{s} \cdot P_{\text {size }}\right\rceil\)
    \(\operatorname{Pr}_{\text {gen }}(1: G E N, 1: N) \leftarrow 0.5\)
    \(\operatorname{Pr}_{\text {temp }} \leftarrow \operatorname{Pr}_{\text {gen }}(1,1: N)\)
    Pop \(\leftarrow \operatorname{random}\left(1: P_{\text {size }}, 1: N\right)<0.5\)
    \(i \leftarrow 1\)
    Execution:
    while \(i \leq G E N\) do
        \(F_{i} \leftarrow \mathcal{O} \mathcal{F}(\mathcal{P})\)
        \(\left\lceil\Lambda_{f} \Lambda_{i}^{\uparrow}\right\rceil \leftarrow \mathcal{S O R T}\left(F_{i}\right)\)
        if \(\Lambda_{f}(1)<F_{c b v}\) then
            \(F_{c b v}=\Lambda_{f}(1)\)
            end if
            \(\Lambda_{i}^{*} \leftarrow \Lambda_{i}^{\uparrow}\left(1: C_{b p}\right)\)
            Pop \(\leftarrow \operatorname{Pop}\left(1: \Lambda_{i}^{*}, 1: N\right)\)
            \(\operatorname{Pr}_{\text {temp }} \leftarrow \frac{\sum \operatorname{Pop}\left(1: C_{b p}, 1: N\right)}{C_{b v}}\)
        Thresholding Implementation Routine : Algorithm
        1.3
        \(\operatorname{Pr}_{\text {repmat }} \leftarrow \mathcal{R E P}\left(\operatorname{Pr}_{\text {temp }}, 1: P_{\text {size }}, 1\right)\)
        SampProb \(\leftarrow \operatorname{random}\left(1: P_{\text {size }}, 1: N\right) \in[0,1]\)
        \(\operatorname{Pop}\left(1: P_{\text {size }}, 1: N\right) \leftarrow \operatorname{SampProb}<\operatorname{Pr}_{\text {repmat }} \in\)
        \(\{0,1\}\)
    end while
Algorithm 1.3 Thresholding Routine
    if \(F_{p b v} \neq F_{c b v}\) then
        \(F_{p b v} \leftarrow F_{c b v}\)
        Count \(\leftarrow 0\)
    else
        Count \(\leftarrow\) Count +1
    end if
    if Count \(>C_{\text {thresh }}\) then
        Count \(\leftarrow 0\)
        if \(\operatorname{Pr}_{\text {temp }} \geq P_{U T L}\) then
            \(\operatorname{Pr}_{\text {temp }} \leftarrow P_{H C}\)
            else if \(\operatorname{Pr}_{\text {temp }} \leq P_{L T L}\) then
            \(\operatorname{Pr}_{\text {temp }} \leftarrow P_{L C}\)
            end if
    end if
```


# 3.1 Algorithm Description 

Table 1 elaborates different variables being used in Algorithm 1.2. The total population is $P_{\text {size }} \times N$, where $N$ is the dimension of the population and $P_{s}$ is the population size, i.e.,

Table 1 Table for algorithm notations 1.2

| Variable | Description |
| :-- | :-- |
| $N$ | Population dimesion |
| $G E N$ | No. of generations |
| $P_{s}$ | Selection probability |
| $P_{s l|s}$ | Size of population |
| $P_{U T L}$ | Upper threshold limit |
| $P_{L T L}$ | Lower threshold limit |
| $P_{H C}$ | Upper clipped value |
| $P_{L C}$ | Lower clipped value |
| $R \mathcal{E} \mathcal{P}$ | Matrix replication function |
| $[\cdot]$ | Ceiling function |
| $S \mathcal{O} R \mathcal{T}$ | Sorting function |
| $P o p$ | Original population |
| $F_{i}$ | Fitness vector |
| $\Lambda_{i}^{1}$ | Indexes of fitness vector post sorting |
| $F_{f}$ | Actual fitness vector post sorting |
| $\Lambda_{i}^{s}$ | Indexes of best solutions |
| $F_{c b v}$ | Current generation best fitness |
| $F_{p b v}$ | Previous generation best fitness |
| $C_{b p}$ | No. of best selected population |
| $P r_{g e n}$ | Generation best probability distribution |
| $\mathcal{O} \mathcal{F}$ | JRM objective function ((3)) |
| $(1: x, 1: y)$ | Represents rows number 1 to $x$ and |
|  | columns from 1 to |
| $C_{\text {thresh }}$ | Count threshold |

the number of individual solutions. The population of candidate solution contains number of expected solutions, which converge to the optimal solution as the algorithm proceeds. We have used value of probability of selection as 0.4 , meaning thereby that each generation retains $40 \%$ of the best individuals out of the whole population lot to produce children. The fitness of the function is calculated using (3). $F_{i}$ contains fitness vector. Fitness are sorted in descending order and stored in $F_{f}$ and relevant indices in $\Lambda_{i}^{1}$. The best value of fitness function per generation is also stored. Best fitness of the current generation is compared with that of previous best value. $F_{p b v}$ retains the value of the best fitness of previous generations. Based on fitness values, $C_{b p}$ best individuals are chosen from the initial population. Probability of selection is multiplied with population size to yield $C_{b p}$. To make $C_{b p}$ an integer value, ceiling function [.] is used post multiplication. The probability distribution of the healthy population are found by summing all the features and dividing them by the total numbers of healthy population, i.e. $C_{b p}$. Thus, a vector containing probability distribution is obtained having dimension( $1,1: N)$. Algorithm 1.3 depicts the thresholding technique used in this article. Check is applied to see if the value of the best fitness does not alter during consecutive $C_{\text {thresh }}$ times, and if the probability value exceeds upper threshold limit $P_{U T L}$ values, it is assigned value of $P_{H C}$ value. Similarly, if the best fitness value remains unaltered for $C_{\text {thresh }}$ iterations, and the probability values dips down below the lower threshold limit $P_{L T L}$, it is assigned value of $P_{L C}$. Thus, probability distribution $P r_{\text {temp }}$ having dimension $(1,1: N)$ is generated for the offspring population. Replicate function

Fig. 3 Comparison of iteration versus utility values with $K=8$, $P_{e N B}=2 \mathrm{~W}, P_{k}^{\max }=0.5 \mathrm{~W}$ and $C_{k}^{\min }=100 \mathrm{kbps}$
![img-2.jpeg](img-2.jpeg)
$R \mathcal{E} \mathcal{P}$ is used to generate multiple $P_{\text {size }}$ copies of $P r_{\text {temp }}$ vector. The multiple copies of the probability distribution vector are cascaded in vertical order to generate $P r_{\text {repmat }}$. Finally, probability matrix $P r_{\text {repmat }}$ is compared with randomly generated matrix to generate new population.

# 4 Simulation Results 

In this section, we show simulation results to demonstrate that the performance of the proposed EDA with thresholds is superior as compared to classic EDA and GA. Following parameters have been considered for simulation purpose: (1) The $P_{e N B}$ assumes values of 2 W. (2) $P_{k}^{\max }$ has been assigned value of 0.5 W . (3) $P_{d}^{\min }$ is set to 100 mW . (4) $C_{k}^{\min }$ is set to 100 kbps . (5) $d_{o}$ is assigned 20 m . (6) eNB coverage ranges up to 1 km . (7) $d$ is a uniformly distributed distance. (8) $\xi_{o}$ is 10 dB , and (9) $G_{o}$ is 50 . Figures 3 and 4 show performance comparison (in terms of utility value vs number of iterations) of three algorithms i.e. EDA with threshold, EDA with classic and GA. Results show that EDA with threshold performs better than the other two algorithm. EDA with threshold provides better utility values and convergence to the best utility value is attained with less number of iterations. As EDA attains the best utility value with less number of iteration proving the fact that this algorithm is computationally more efficient compared to classic EDA and GA. Figure 4 confirms that EDA with threshold performs well in spite of the situation where number of users are increased. Figure 5 compares performance with different number of users. As the number of users are increased, EDA with Threshold provides better utility value(better performance)compared to the other two considered algorithms. Figure 6 reveals that EDA with threshold is superior in terms of selection of users compared to EDA classic and GA Algorithms. More number of users are selected with EDA with threshold. Figure 7 is testimony to the fact that EDA with threshold is spectrally more efficient. Spectral efficiency is measured in terms of aggregate system throughput per hertz (bits/s/Hz). Spectral efficiency affects can be seen more prominently as the number of users become more larger The simulation results confirm that EDA with threshold provides better utility values hence

Fig. 4 Comparison of iteration versus utility values with $K=20$, $P_{u N R}=2 \mathrm{~W}, P_{k}^{m a x}=0.5 \mathrm{~W}$ and $C_{k}^{\text {min }}=100 \mathrm{kbps}$
![img-3.jpeg](img-3.jpeg)
an excellent means to jointly control admission of users and selection of modes with more spectral efficiency.

# 5 Conclusion 

A convergent solution to address the problem of joint admission control, mode selection and power allocation has been proposed in this paper. We used EDA algorithm with threshold to solve the problem and compared the performance with classic EDA and GA. Results confirm the superiority of EDA with threshold over the other two considered algorithm in terms of yielding better utility values, computationally more efficient, spectrally more efficient and more efficient in terms of selection of users.

Fig. 6 Performance comparison(in terms of number of selected users) of EDA with threshold versus GA having parameters of $P_{u N B}=2 \mathrm{~W}, P_{k}^{\max }=0.5 \mathrm{~W}$ and $C_{k}^{\min }=100 \mathrm{kbps}$
![img-4.jpeg](img-4.jpeg)

Fig. 7 Performance comparison (in terms of spectral efficiency (bits/sec/Hz)) of EDA with threshold versus GA having parameters of $P_{u N B}=2 \mathrm{~W}, P_{k}^{\max }=0.5 \mathrm{~W}$ and $C_{k}^{\min }=100 \mathrm{kbps}$ with different numbers of users
![img-5.jpeg](img-5.jpeg)

# References 

1. Astely, D., Dahlman, E., Fodor, G., Parkvall, S., \& Sachs, J. (2013). LTE release 12 and beyond [accepted from open call]. Communications Magazine, IEEE, 51(7), 154-160.
2. Panwar, N., Sharma, S., \& Singh, A. K. (2016). A survey on 5G: The next generation of mobile communication. Physical Communication, 18, 64-84.
3. Dan, N., Li, B., Lan, B., \& JunRen, C. (2013). Resource allocation over cooperation for cross-cell D2D communication underlaying LTE network. In TENCON 2013-2013 IEEE region 10 conference (31194) (pp. 1-4). IEEE.
4. Pahlevani, P., Hundebøll, M., Pedersen, M. V., Lucani, D. E., Charaf, H., Fitzek, F. H., et al. (2014). Novel concepts for device-to-device communication using network coding. Communications Magazine, IEEE, 52(4), 32-39.

5. Doppler, K., Rinne, M., Wijting, C., Ribeiro, C. B., \& Hugl, K. (2009). Device-to-device communication as an underlay to LTE-advanced networks. Communications Magazine, IEEE, 47(12), 42-49.
6. Asadi, A., Wang, Q., \& Mancuso, V. (2014). A survey on device-to-device communication in cellular networks. Communications Surveys \& Tutorials, IEEE, 16(4), 1801-1819.
7. Akkarajitsakul, K., Phunchongharn, P., Hossain, E., \& Bhargava, V. K. (2012). Mode selection for energy-efficient D2D communications in LTE-advanced networks: A coalitional game approach. In 2012 IEEE international conference on communication systems (ICCS) (pp. 488-492). IEEE.
8. Tran, H., Kaddoum, G., \& Gagnon, F. (2016). Power allocation for cognitive underlay networks with spectrum band selection. Physical Communication, 21, 41-48.
9. Peng, B., Hu, C., Peng, T., \& Wang, W. (2012). Optimal resource allocation for multi-D2D links underlying ofdma-based communications. In 2012 8th International conference on wireless communications, networking and mobile computing (WiCOM) (pp. 1-4). IEEE.
10. Le, L. B. (2012). Fair resource allocation for device-to-device communications in wireless cellular networks. In Global communications conference (GLOBECOM), 2012 IEEE (pp. 5451-5456). IEEE.
11. Gao, J., Liao, X., Deng, J., \& Ren, P. (2013). A mode shifting resource allocation scheme for device-to-device underlaying cellular network. AASRI Procedia, 5, 40-47.
12. Zhang, H., Wang, T., Song, L., \& Han, Z. (2013). Graph-based resource allocation for D2D communications underlaying cellular networks. In 2013 IEEE/CIC international conference on communications in China-workshops (CIC/ICCC) (pp. 187-192). IEEE.
13. Wang, B., Chen, L., Chen, X., Zhang, X., \& Yang, D. (2011). Resource allocation optimization for device-to-device communication underlaying cellular networks. In Vehicular technology conference (VTC Spring), 2011 IEEE 73rd (pp. 1-6). IEEE.
14. Tao, Y., Sun, J., \& Shao, S. (2013). Radio resource allocation based on greedy algorithm and successive interference cancellation in device-to-device (D2D) communication. In Proceedings of IETICT (pp. 452-458).
15. Wang, J., Zhu, D., Zhang, H., Zhao, C., Li, J. C., \& Lei, M. (2014). Resource optimization for cellular network assisted multichannel D2D communication. Signal Processing, 100, 23-31.
16. Wu, W., Xiang, W., Zhang, Y., Zheng, K., \& Wang, W. (2015). Performance analysis of device-todevice communications underlaying cellular networks. Telecommunication Systems, 60(1), 29-41. https://doi.org/10.1007/s11235-014-9919-y. [Online].
17. Marshoud, H., O trok, H., Barada, H., Estrada, R., J array, A., \& Dziong, Z. (2015). Realistic framework for resource allocation in macrofemtocell networks based on genetic algorithm. Telecommunication Systems [Online],. https://doi.org/10.1007/s11235-015-9976-x. [Online].
18. Peng, B., Hu, C., Peng, T., Yang, Y., \& Wang, W. (2013). A resource allocation scheme for D2D multicast with QoS protection in OFDMA-based systems. In 2013 IEEE 24th international symposium on personal indoor and mobile radio communications (PIMRC) (pp. 12383-2387). IEEE.
19. Pei, Y., \& Liang, Y.-C. (2013). Resource allocation for device-to-device communications overlaying two-way cellular networks. IEEE Transactions on Wireless Communications, 12(7), 3611-3621.
20. Pang, H., Wang, P., Wang, X., Liu, F., \& Van, N. N. (2013). Joint mode selection and resource allocation using evolutionary algorithm for device-to-device communication underlaying cellular networks. Journal of Communications, 8(11), 751-757.
21. Wen, S., Zhu, X., Lin, Z., Zhang, X., \& Yang, D. (2013). Distributed resource management for device-to-device (D2D) communication underlay cellular networks. In 2013 IEEE 24th international symposium on personal indoor and mobile radio communications (PIMRC) (pp. 1624-1628). IEEE.
22. Chen, R., Liao, X., Zhu, S., \& Liang, Z. (2012). Capacity analysis of device-to-device resource reusing modes for cellular networks. In 2012 IEEE international conference on communication, networks and satellite (ComNetSat) (pp. 64-68). IEEE.
23. Zhang, R., Song, L., Han, Z., Cheng, X., \& Jiao, B. (2013). Distributed resource allocation for device-to-device communications underlaying cellular networks. In 2013 IEEE international conference on communications (ICC) (pp. 1889-1893). IEEE.
24. Min, H., Lee, J., Park, S., \& Hong, D. (2011). Capacity enhancement using an interference limited area for device-to-device uplink underlaying cellular networks. IEEE Transactions on Wireless Communications, 10(12), 3995-4000.
25. Wang, J., Zhu, D., Zhao, C., Li, J. C., \& Lei, M. (2013). Resource sharing of underlaying device-todevice and uplink cellular communications. Communications Letters, IEEE, 17(6), 1148-1151.

26. Cheng, P., Deng, L., Yu, H., Xu, Y., Wang, H. (2012). Resource allocation for cognitive networks with D2D communication: An evolutionary approach. In Wireless communications and networking conference (WCNC), 2012 IEEE (pp. 2671-2676). IEEE.
27. Lee, Y.-H., Tseng, H.-W., Lo, C.-Y., Jan, Y.-G., Chin, L.-P., Song, T.-C., \& Hsu, H.-I. (2012). Using genetic algorithm with frequency hopping in device to device communication (D2DC) interference mitigation. In 2012 International symposium on intelligent signal processing and communications systems (ISPACS) (pp. 201-206). IEEE.
28. Su, L., Ji, Y., Wang, P., \& Liu, F. (2013). Resource allocation using particle swarm optimization for D2D communication underlay of cellular networks. In Wireless communications and networking conference (WCNC), 2013 IEEE (pp. 129-133). IEEE.
29. Yu, G., Xu, L., Feng, D., Yin, R., Li, G. Y., \& Jiang, Y. (2014). Joint mode selection and resource allocation for device-to-device communications. IEEE Transactions on Communications, 62(11), $3814-3824$.
30. Sun, S., \& Shin, Y. (2014). Resource allocation for D2D communication using particle swarm optimization in LTE networks. In 2014 International conference on information and communication technology convergence (ICTC) (pp. 371-376). IEEE.
31. Yang, C., Xu, X., Han, J., Rehman, W. U., \& Tao, X. (2014). Ga based optimal resource allocation and user matching in device to device underlaying network. In Wireless communications and networking conference workshops (WCNCW), 2014 IEEE (pp. 242-247). IEEE.
32. Yang, C., Xu, X., Han, J., \& Tao, X. (2015). Energy efficiency-based device-to-device uplink resource allocation with multiple resource reusing. Electronics Letters, 51(3), 293-294.
33. Liotou, E., Tsolkas, D., Passas, N., \& Merakos, L. (2014). Ant colony optimization for resource sharing among D2D communications. In 2014 IEEE 19th international workshop on computer aided modeling and design of communication links and networks (CAMAD) (pp. 360-364). IEEE.
34. Tang, H., \& Ding, Z. (2016). Mixed mode transmission and resource allocation for D2D communication. IEEE Transactions on Wireless Communications, 15(1), 162-175.
35. Wang, L., Wu, H., Liu, L., Song, M., \& Cheng, Y. (2015). Secrecy-oriented partner selection based on social trust in device-to-device communications. In 2015 IEEE international conference on communications (ICC) (pp. 7275-7279). IEEE.
36. Goldsmith, A. (2005). Wireless communications. Cambridge: Cambridge University Press.
37. González, C., Lozano, J., \& Larranaga, P. (2002). Mathematical modeling of discrete estimation of distribution algorithms (pp. 147-163). Berlin: Springer.

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
![img-6.jpeg](img-6.jpeg)

Mushtaq Ahmad received the B.Sc. degree in electrical engineering from the University of Engineering and Technology, Lahore, Pakistan, in 1990; the M.S. degree in electrical engineering from the University of Michigan, Ann Arbor, MI, USA, in 1994; and the Masters of Telecommunication Management degree from the Institut National Des Telecom France, Evry, France, in 1999. He has served as an Incumbent Operator with Pakistan Telecommunication Company Limited; as a Regulator with the Pakistan Telecommunication Authority; as a Member (Telecom) with the Ministry of Information Technology and Communication, Pakistan; and as the Chief Executive Officer of reputable public and private institutions. He is currently a Principal Engineer with COMSATS Institute of Information Technology, Pakistan. His main research interests include resource allocation in next-generation networks.

![img-7.jpeg](img-7.jpeg)
ent of NSERC CGS scholarship.
![img-8.jpeg](img-8.jpeg)

Muhammad Naeem received the BS (2000) and MS (2005) degrees in Electrical Engineering from the University of Engineering and Technology, Taxila, Pakistan. He received his PhD degree (2011) from Simon Fraser University, BC, Canada. From 2012 to 2013, he was a Postdoctoral Research Associate with WINCORE Lab. at Ryerson University, Toronto, ON, Canada. Since August 2013, he is working as faculty member in the Department of Electrical Engineering, COMSATS Institute of IT, Wah Campus, Pakistan and Research Associate with WINCORE Lab. at Ryerson University. From 2000 to 2005, he was a senior design engineer at Comcept (pvt) Ltd. At the design department of Comcept (pvt) Ltd, Dr. Naeem participated in the design and development of smart card based GSM and CDMA pay phones. Dr. Naeem is also a Microsoft Certified Solution Developer (MCSD). His research interests include optimization of wireless communication systems, non-convex optimization, resource allocation in cognitive radio networks and approximation algorithms for mixed integer programming in communication systems. Dr. Naeem has been the recipi-

Muhammad Iqbal received B.Sc. Electrical Engineering degree in 1999 from University of Engineering and Technology, Lahore. After completing B.Sc. Electrical Engineering, he served in the state owned telecommunication company for more than seven years. In 2007 he completed his MS Telecommunication Engineering from the University of Engineering and Technology, Peshawar. After completing PhD by July, 2011 from Beijing University of Posts and Telecommunications, P.R. China, he rejoined COMSATS and till this date working as faculty member, Electrical Engineering Department, CIIT, Wah Campus. His research interests include signal and information processing, wireless communication, smart grid and applied optimization.