# An EDA-based method for solving electric vehicle charging scheduling problem under limited power and maximum imbalance constraints 

Hadi Shahmoradi ${ }^{\mathrm{a}}$, Majid Esmaelian ${ }^{\mathrm{a}, *}$, Hossein Karshenas ${ }^{\mathrm{b}}$<br>${ }^{a}$ Department of Management, University of Isfahan, Hesarjerib St., Asadi Square, Isfahan, Iran<br>${ }^{\mathrm{b}}$ Department of Artificial Intelligence, Faculty of Computer Engineering, University of Isfahan, Hesarjerib St., Asadi Square, Isfahan, Iran

## A R T I C L E I N F O

Keywords:
Electric Vehicle Charging Scheduling Problem (EVCSP)
Balance constraint
Estimation Distribution Algorithm (EDA)
Markov Network-based EDA
Mallows Model-based EDA
Constraint Programming (CP)


#### Abstract

Electronic vehicles (EVs) are receiving increasing attention to addressing global warming challenges since fossil fuel is replaced with fuel cell technology. Hence, new challenges arise as demands have increased for using EVs. One of these challenges is the long waiting time of charging EVs spent in queues, especially during peak hours. So, in this study, we aim to propose an efficient method for the electric vehicle charging scheduling problem (EVCSP), which an actual charging station inspires. The most important constraint in this problem is balancing power consumption between charging lines, leading to a limited number of devices that can be charged simultaneously. Also, in this problem, EVs may have interrelationships with each other during the scheduling procedure. So, the estimation of distribution algorithm (EDA) as a competent method in handling the possible relations among decision variables is applied in our proposed hybrid EDA-based solving method. Our proposed method comprises two EDAs, a Markov network-based EDA and a Mallows model-based EDA. It achieves an appropriate schedule and charging line assignment simultaneously while minimizing the total tardiness considering problem constraints. We compared our method with a constraint programming (CP) model and the state-of-art meta-heuristic methods in terms of the objective function value by simulation on a benchmark dataset. Results from the experimental study show significant improvement in solving the introduced EVCSPs.


## 1. Introduction

Releasing greenhouse gas (GHG) into the atmosphere by burning fossil fuels, especially in the transportation sector, is one of the main contributors to global warming and climate change (Acar \& Dincer, 2020; Zhou et al., 2020). To address the global warming challenges, non-fossil fuels (such as hydrogen in fuel cell technology) are receiving increasing attention (Chen et al., 2019; Wilberforce et al., 2017). Fuel cell technology in the automotive industry as one of the successful efforts results in emerging electric vehicles (EVs) in the market (Chung et al., 2018). Although EVs bring several advantages to transportation, they require frequent and long-time charging. Hence, with increasing demand for EVs (Jian et al., 2017), they should spend long queuing hours, especially during peak hours (Zhu et al., 2014). Therefore, an efficient method is required for the electric vehicle charging scheduling problem (EVCSP) (Al-Ogaili et al., 2019).

The EVCSP addressed in this study is inspired by an actual charging station first raised in (Hernández Arauzo et al., 2013). This problem includes an EV station with multiple charging points in three different
lines of a three-phase feeder. The assignment of EVs to the charging points is pre-defined. The critical constraint for charging scheduling in this station is to impose an upper bound on the number of EVs connected to each line at any given time.

Various studies have been proposed so far to address the aforementioned problem while minimizing the charging delays of all EVs such as (Hernández-Arauzo et al., 2015), (García-Álvarez et al., 2015), (Mencía et al., 2017), (García-Álvarez et al., 2018), (Mavrovouniotis et al., 2019). In this study, we also aim to achieve an effective schedule for this EVCSP. Moreover, we consider a more generalized form of this problem in which EVs are not pre-assigned to charging lines. So, we also aim to address this generalized problem requiring the assignment of EVs to charging lines to be handled by the proposed algorithm.

We propose a hybrid estimation of distribution algorithm (EDA) as our solving method for the outlined problem. Since these problems are NP-hard, EDAs as metaheuristic algorithms are proper for obtaining good results in a reasonable computational time (García-Álvarez et al., 2018). In addition, there are possible interactions between EVs during the scheduling procedure while considering the problem constraints,

[^0]
[^0]:    a Corresponding author.

    E-mail addresses: ha.shahmoradi@ase.ui.ac.ir (H. Shahmoradi), m.esmaelian@ase.ui.ac.ir (M. Esmaelian), h.karshenas@eng.ui.ac.ir (H. Karshenas).

![img-0.jpeg](img-0.jpeg)

Fig. 1. A general structure of an EV charging station with multiple charging points in three charging lines (García-Álvarez et al., 2018).
and EDAs are competent in handling the possible relations among decision variables (Kacprzyk \& Pedrycz, 2015).

The strength of EDAs is in their search mechanism that can learn and adapt itself according to the problem. They are rooted in evolutionary computing and machine learning. From the evolutionary perspective, they have adopted using a population of promising solutions that evolve iteratively by performing selection and variation steps. They also adopted the idea of data-driven modeling from machine learning in which a probabilistic model is learned based on a population of previously visited reasonable solutions, and the resulting model is used to infer where other reasonable solutions might be (Kacprzyk \& Pedrycz, 2015).

Our EDA-based proposed approach comprises two EDAs: a Markov network-based EDA (MN-EDA) and a Mallows model-based EDA (MMEDA) algorithms. We called our proposed method "HMM-EDA" after the Hybrid Markov network and Mallows model-based EDA. The reason for this hybridization is that we model the EVCSP with two types of decision variables; (1) assignment of each EV to a charging line and (2) sequence of all EVs charging. Markov network is a suitable model for dealing with the interaction among variables (Shakya et al., 2012). Due to the shared power supply in our considered EVCSP, EVs interact with each other once they seize a power line. So, MN-EDA is proposed to handle charging line assignment while considering these interactions. In addition, by considering EV sequence as a permutation problem, we offered MM-EDA since the Mallows model is a suitable approach for permutation modeling (Zangari et al., 2017). It is worth mentioning that permutation problems are defined as ordering specific symbols where two symbols cannot have the same position, and two positions cannot belong to the same symbol (Ceberio et al., 2012).

The proposed method is evaluated using the benchmark introduced in (García-Álvarez et al., 2018). This benchmark is obtained from a sample station with three lines where each line has 60 charging points ( 180 charging points in total). It includes arrival times and due times corresponding to the expected behavior of real users in different situations. Even though the charging line assignment is pre-determined in this benchmark, we have also considered this assignment as a decision variable due to specific features of our generalized problem.

To compare the performance of the HMM-EDA with other solving methods, we proposed a constraint programming (CP) model since it provides an optimal solution for our problem. Moreover, we solved our problem with state-of-art meta-heuristic methods, including simulated
annealing (SA), discrete particle swarm optimization (PSO), and artificial bee colony (ABC). Results are compared in terms of the gap from the best solution with respect to the objective, showing the superiority of the proposed HMM-EDA.

The contributions of this study are as follows:

1. According to the literature, it is assumed that the assignment of each EV to the charging lines is known. However, in this study, new decision variables are added to the problem formulation for handling EV assignment, which is very important for real-world applications. It is worth mentioning that solving the more generalized form of this EVCSP has not been addressed in the literature yet.
2. To the best of our knowledge, the EDA-based method has not been used to solve EVCSPs. In this study, we developed and proposed a hybrid Markov network and Mallows model EDA (HMM EDA) method to solve this scheduling problem, including problem constraints, to minimize the total tardiness. To enhance the performance of the proposed EDAs, we proposed an initial population generation algorithm, a diversity control mechanism, and a heuristic local search method.
3. In this study, a constraint programming (CP) model of the general proposed form of EVCSP is proposed.

The rest of this paper is organized in the following way. In the next section, we explained the problem formulation. Then in section 3, we briefly reviewed the related studies in EVCSP. We describe our proposed method in section 4, which is followed by the discussion and results section. In the end, the conclusion is presented in section 6.

## 2. Problem formulation

This study's EV charging scheduling problem (EVCSP) is motivated by (Hernández Arauzo et al., 2013). It includes an EV station with 60 charging points in each of the three lines ( 180 charging points total) of a three-phase feeder (Fig. 1). As it is shown in Fig. 1, there is an aggregator which is responsible for scheduling the charging of EVs while considering the following constraints:

1. Active charging points upper bound- restricts the maximum number of EVs that can be connected to each line at any given time.

Table 1
Problem parameters and variables in the static EVCSP variant.

2. Power imbalance constraint- controls power imbalance among lines due to economic and electro-technical reasons.
3. Non-preemptive charging- refers to a no-interruption charging process once the charging of each EV starts.

In real-life EV stations, the arrival time, charging time, and due time (expected time of leaving the station) of each EV is unknown before an EV arrives in a station. This problem is dynamic. However, for solving and evaluation purposes, a static variant of the problem is mainly considered in studies where the behavior of each EV, including arrival, charging, and due times is known in advance (García-Álvarez et al., 2018). In this study, we considered both the static and the dynamic variant of the problem. The problem formulations of these variants are described in the following.

In the formulation of the static variant of EVCSP, it is assumed that arrival times, charging times, and due times of all EVs are known in advance. The problem parameters and variables are tabulated in Table 1.

The mathematical formulation of the static problem is aimed to minimize the total tardiness of all EVs according to Eq. (1) concerning the problem constraints, which are described in Eq. (2)-(5).

$$
\begin{aligned}
& \sum_{i=1}^{s} \sum_{j=1}^{M} \max \left(0, e_{i j}-d_{j}\right) \\
& s_{i j} \geq a_{j}, \quad \forall 1 \leq i \leq 3,1 \leq j \leq M \\
& e_{i j}=s_{i j}+c_{j}, \quad \forall 1 \leq i \leq 3,1 \leq j \leq M \\
& N_{i}(t) \leq N, \quad \forall 1 \leq i \leq 3 \\
& \frac{\left|N_{i}(t)-N_{i}(t)\right|}{N} \leq \Delta, \quad \forall 1 \leq i, j \leq 3
\end{aligned}
$$

The constraint defined in Eq. (2) restricts each EV from starting the charging process before its arrival time. According to the constraint in Eq. (3), EVs are charged in a non-preemptive process. So, they must not be disconnected from their charging point until their charging process is finished. Eq. (4) assures that the number of active EVs at any given time and any given line should not exceed $N$. At last, Eq. (5) imposes an upper bound on the imbalance between every-two lines.

The dynamic variant of the problem is modeled as a sequence of $n$ static problem instances $\left(P_{1}, P_{2} \cdots, P_{n}\right)$. Each instance includes EVs that are already arrived in the station in which some of the EVs are in the middle of their charging process, and others are pending to start their charging process. Consequently, EVs' charging time $c_{j}$ and due time $d_{j}$ of each instance is known. At each time interval, the aggregator checks for new EV arrivals. For the sake of server workload in the case of arriving many EVs simultaneously and efficient use of resources, the time

Table 2
Review of recent centralized EVCSP studies from an operations research perspective.

interval is usually set at two minutes (Garcia Alvarez et al., 2018). Accordingly, the scheduling problem is defined as determining the starting time $s_{0}$ of each pending EV in each time interval with respect to all constraints described in the static variant of the problem while minimizing the total tardiness. Notice that the $s_{0}$ may be modified in further $P_{n}$ instances as long as the corresponding EV does not start charging.

## 3. Literature review

A comprehensive review of scheduling, clustering and forecasting strategies for controlling EV charging can be found in (Al-Ogaili et al., 2019). From Al-Ogalia's perspective, there are two main EV charging scheduling strategies: centralized and decentralized. In the centralized approach, EVs are connected to an EV aggregator. The EV aggregator collects charging data from EVs and electrical grids to solve the optimization problem for the sake of its stakeholders, operators of charging stations, and EV owners (Jin et al., 2013). In the decentralized strategy, each EV owner has the authority to operate strategically to minimize their charging costs. Although this strategy offers more flexibility to EV owners, it does not guarantee optimality (Ma et al., 2011). Our study is focused on the centralized strategy.

As far as we know, EVCSPs are not reviewed from the operation research (OR) perspective. So, we reviewed EVCSP from their problem

Table 3
Review of recent EDA-based method in solving the scheduling problem.
constraints, objective function, and solving method points of view. Table 2 summarizes our findings of the recent literature dealing with centralized EVCSPs from the OR perspective.

According to Table 2, from the objective function, our study lies in minimizing total tardiness. From a constraints point of view, we consider the power and balance constraints in our research. Moreover, from our optimization and solving method perspective, we proposed an EDA-based method that has not been addressed in the EVCSP literature to the best of the authors' knowledge. In the following, we reviewed, EDA-based approach in scheduling literature.

### 3.1. EDA-based method in the scheduling problem

Considering that the EVCSPs lie in scheduling problems, we reviewed the EDA-based method in solving scheduling problems (Table 3). According to the following Table, EDAs are applicable in scheduling problems; nevertheless, it does not use in the EVCSPs yet. It should be pointed out here that most of the EDA-based solving methods in the studied scheduling problem applied the order statistics approach as the EDA probabilistic model. In this approach, EDA probabilistic model is a matrix of probabilities of symbol $i$ in position $j$.

## 4. Proposed method

This section comprises three sub-sections. This study's preliminary concepts, including introductory concepts of EDAs, Markov networkbased EDA, Mallows Model-based EDA, and the CP paradigm, are briefly described in the first part. Next, our proposed HMM-EDA model is illustrated for solving EVCSP. In the final section, CP as an optimal solving approach for EVCSP is explained.

### 4.1. Preliminaries

EDAs are random optimization methods investigating the potential solutions space by modeling the possible promising solutions (Hauschild \& Pelikan, 2011). The resulting model helps recognize relationships among variables that provide valuable and understandable insights into the real-world problem structure. In addition, determining a potential distribution could increase the probability of finding an estimated area, including the promising solutions in the entire problem-solving space. Also, this distribution could reduce the number of function evaluations (NFE) for approaching the optimum solution (Larrañaga \& Lozano, 2001). The repetitive steps in an EDA are:

1. Selection- selecting a set of promising solutions from the population;
2. Model Learning- learning a probability model from the promising solutions; and
3. Sampling- producing a sample from the probability model (Larrañaga \& Lozano, 2001).

We described two EDA versions based on the Mallows model and the Markov network in the first two parts. Besides, a CP model is briefly explained in part three, and the optimal solution obtained from the CP model is considered as a baseline for comparison purposes.

### 4.1.1. Mallows models based EDA (MM-EDA)

In MM-EDA, a Mallows model is learned based on the current population. Then, the learned Mallows model is used to find other promising solutions for the next population generation. This process is repeated until the termination condition for MMEDA is met. In the following, we first describe the Mallows model and its learning procedure, then explain the sampling method for generating the next population.
(a) Mallows Model

The Mallows Model (MM) is an exponential family of probability models for permutation problems based on the distance between two permutations. The probability value of every permutation $(\psi(\delta))$ is defined by two parameters: (1) spread parameter $(\theta)$; and (2) a central permutation $\left(\delta_{0}\right)$. So, the MM is expressed as follows (Arrieta, 2014):
$p_{\delta \delta_{0}}(\delta)=\frac{\exp \left(-\theta d\left(\delta, \delta_{0}\right)\right)}{\psi(\theta)} \quad$ where $\psi(\theta)=\sum_{\delta} \exp \left(-\theta d\left(\delta, \delta_{0}\right)\right)$
Where $\psi(\theta)$ denotes the normalization constant. Also, $\delta_{0}$ refers to the central permutation. When $\theta=0$, the probability distribution is uniform. When $\theta>0, \delta_{0}$ is the permutation with the highest probability value (distribution mode), otherwise in the case that $\theta<0, \delta_{0}$ is the antimode, i.e., the permutation with the lowest probability. Also, $d\left(\delta, \delta_{0}\right)$ denotes the distance metric, which can be defined in several ways such as Kendall's- $\tau$, Spearman's- $\rho$, Spearman's footrule, Cayley, Hamming, and Ulam (Diaconis, 1988).

Due to the dynamic and NP-hard nature of EVCSP and the importance of required time by the problem-solving method, we choose Kendall's- $\tau$ distance metric (Arrieta, 2014). Given two permutations $\delta_{1}$ and $\delta_{2}$, the Kendall- $\tau$ distance is defined by the total number of pairwise disagreements between two permutations. In other words, it counts the minimum number of adjacent swaps to convert $\delta_{1}$ into $\delta_{2}$. Formally, it can be written as follows (Ceberio et al., 2011):

$$
\begin{aligned}
d\left(\delta_{1}, \delta_{2}\right) & =|\{(x, y): x<y,\left(\delta_{1}(x)<\delta_{1}(y) \wedge \delta_{2}(x)>\delta_{2}(y)\right) \vee\left(\delta_{2}(x)\right. \\
& \left.\left.<\delta_{2}(y) \wedge \delta_{1}(x)>\delta_{1}(y)\right)\right\|
\end{aligned}
$$

Which can also be written as:

$d\left(\delta_{1}, \delta_{2}\right)=\sum_{j=1}^{M-1} V_{j}\left(\delta_{1}, \delta_{2}\right)$
Where $\mathrm{V}_{j}\left(\delta_{1}, \delta_{2}\right)$ is the minimum number of adjacent swaps to set in the $f^{\text {th }}$ position of $\delta_{1}, \delta_{1}(\mathrm{j})$, to the value in $\delta_{2}(\mathrm{j})$. Also, $M$ represents the permutation length.

The MM (Eq. (6)) under Kendall's- $\tau$ distance can be rewritten as follows (Ceberio et al., 2013):
$p(\delta)=\frac{\exp \left(\sum_{j=1}^{M-1}-\theta V_{j}\left(\delta, \delta_{0}\right)\right)}{\psi(\theta)}$
So, the probability distribution of the random variables $\mathrm{V}_{j}\left(\delta, \delta_{0}\right)$ can be written as (Ceberio et al., 2013):
$p\left(V_{j}\left(\delta, \delta_{0}\right)=r_{j}\right)=\frac{\exp (-i \theta r_{j})}{\psi_{j}(\theta)} r_{j} \in(0, \cdots, M-j)$.
(b) Learning

The exact estimation of the MM parameters can be computationally intractable. By experimental evaluation, Arrieta showed that the approximate learning process and the Kendall's- $\tau$ distance metric find accurate estimators in polynomial time for MM (Arrieta, 2014).

Like any other EDAs, in MM-EDA, a probability model is learned in each step from a set of promising solutions. For this purpose, $\delta_{0}$ and $\theta$ parameters are estimated given a dataset of permutations $\left\{\delta_{1}, \cdots, \delta_{Q}\right\}$ using the maximum likelihood estimation (MLE) method. The loglikelihood function can be written as follows (Ceberio et al., 2011):

$$
\begin{aligned}
\log \mathscr{L}\left(\left\{\delta_{1}, \cdots, \delta_{Q}\right\} \mid \delta_{0}, \theta\right) & =\sum_{k=1}^{K} \log p\left(\delta_{k} \mid \delta_{0}, \theta\right)=\sum_{k=1}^{K} \log \frac{\exp \left(-\theta V_{j}\left(\delta_{k}, \delta_{0}\right)\right)}{\psi_{j}(\theta)} \\
& =\sum_{k=1}^{K}\left(-\theta V_{j}\left(\delta_{k}, \delta_{0}\right)+\log \psi_{j}(\theta)\right) \\
& =-K\left(\theta \bar{V}_{j}\right)-K\left(\log \psi_{j}(\theta)\right)
\end{aligned}
$$

Where $\bar{V}_{j}=\sum_{\mathrm{k}=1}^{\mathrm{K}} \mathrm{V}_{j}\left(\delta_{\mathrm{k}}, \delta_{0}\right) / \mathrm{Q}$ which means $\overline{\mathrm{V}}_{j}$ is the observed mean for $V_{j}$.

Due to the independence calculation of $\delta_{0}$ and maximization of Eq. (11) with respect to $\theta$, MLE can be divided into two steps: first, $\delta_{0}$ is obtained, and then $\theta$ is computed for the given $\overline{\delta}_{0}$. The problem of calculating $\delta_{0}$ is called rank aggregation. The permutation $\delta_{0}$ that maximize the log-likelihood can be expressed as follows (Arrieta, 2014):
$\overline{\delta}_{0}=\arg \max _{\delta_{0}} \sum_{k=1}^{K}-V_{j}\left(\delta_{k}, \delta_{0}\right)=\arg \min _{\delta_{0}} \sum_{k=1}^{K} V_{j}\left(\delta_{k}, \delta_{0}\right)$
In other words, Eq.(12) denotes that the MLE for $\delta_{0}$ is given by the permutation that minimizes the sum of the Kendall's- $\tau$ distances to the samples in the dataset. This problem is known to be NP-hard (Bartholdi et al., 1989). Hence, we use the heuristic method introduced by Ceberio et al. as our solving method(Ceberio et al., 2011).

Once $\delta_{0}$ is known, the MLE for estimation of $\theta$ is achieved by differentiating Eq. (12) with respect to $\theta$ and equaling to zero. Hence, $\theta$ is estimated to satisfy the following expression (Arrieta, 2014):
$\frac{M-1}{e^{\theta}-1}=\sum_{j=1}^{M} \frac{M e^{-\theta j}}{1-e^{-\theta j}}=\bar{d}$
Eq. (13) has no closed-form solution. So, we solved it with the Netwon-Rapshon algorithm (Arrieta, 2014).
(c) Sampling

To sample a new solution from the learned model (Eq. (9)), a method described by Ceberio et al. is applied (Ceberio et al., 2013). In this sampling method, vectors $\mathrm{V}_{j}\left(\delta_{\mathrm{k}}, \delta_{0}\right), 1 \leq \mathrm{k} \leq \mathrm{K}-1$ with the distribution according to Eq. (10) is generated(9). Then, the new permutations are calculated using an algorithm proposed by Meila et al., as illustrated in Algorithm 1 (Meila et al., 2012). Finally, each permutation is obtained by inverting and composing with the central permutation.
Algorithm 1. Conversion from $\mathrm{V}(\mathrm{x})$ to $\pi^{-1}$
1 Input: A vector $V(x)$
2 Create an empty list $x^{-1}$
3 Insert $n$ in position 0
4 for $j=M-1: 1$ in decreasing order
5 Insert $j$ in position $V_{j}$ of $x^{-1}$
6 output: $x^{-1}$

### 4.1.2. Markov network-based EDA (MN-EDA)

In Markov network-based EDA (MN-DEA), a Markov network is learned based on the current population. The other procedure in this variant of EDA is the same as other EDAs. To elucidate MN-EDA, first, we describe Markov networks and their learning procedure, then explain the sampling method for generating the next population.

## (a) Markov Network Model

A Markov network (MN) model is represented by an undirected graph, $G$, and a set of parameters $\varphi$. In this graph, each node denotes a decision/random variable, $X_{i}$, and the edges, $E_{g}$, represent the relationships between the variables $X_{i}$ and $X_{j}$ through their affinity potentials. Consequently, the relationship between two nodes is seen as a neighborhood relationship in which the neighborhood $H_{i}$ of node $X_{i}$ includes all nodes connecting to the node $X_{i}$ by an edge. The neighborhood relationship can be written in terms of probability as follows (Shakya et al., 2012):
$p\left(x_{i} \mid x-\left\{x_{i}\right\}\right)=p\left(x_{i} \mid H_{i}\right)$
In addition, an MN is described in terms of cliques, $\varsigma_{c}$, a fully connected subset of nodes. Thus, the joint probability distribution can be written as follows (Shakya et al., 2012):
$p(x)=\frac{1}{Z^{p}} \cdot \sum_{i=1}^{Q} \frac{\left(x_{i} \mid \zeta_{i}\right) / T}{Z}$
Where, $Q$ is the number of cliques in the undirected graph structure $G$ and $Z$ is the normalization term called partition function. Also, $u_{i}\left(\zeta_{i}\right)$ is a potential function on clique $\zeta_{i}$ which can have many different functional forms. The parameters of this function that completely defines the joint probability are estimated from the data. $T$ is a normalization constant.

## (b) Learning

Several different approaches can be applied for estimating an undirected structure. We use the Mutual Information (MI) index to determine the graph structure to reduce the complexity. So, the matrix of mutual information is created in which the cross-entropy of each pair of variables is estimated. Using Eq. (16), the MI value between two random variables $X_{i}$ and $X_{j}$ is calculated as (Shakya et al., 2012):
$M I\left(X_{i}, X_{j}\right)=\sum_{x_{i} \in X_{i} \mid x_{j} \in X_{j}} \sum_{i=1}^{m} p\left(x_{i}, x_{j} \mid D\right) \times \log \left(\frac{p\left(x_{i}, x_{j} \mid D\right)}{p\left(x_{i} \mid D p\left(x_{j} \mid D\right)}\right)\right.$
Where $p\left(x_{i} \mid D\right)$ and $p\left(x_{j} \mid D\right)$ are the marginal probabilities of the decision variables $X_{i}$ and $X_{j}$, respectively, on a set of promising solutions, $D$. Also, $p\left(x_{i}, x_{j} \mid D\right)$ is the joint probability of $X_{i}$ and $X_{j}$ and the summation represents all possible combinations of values for random variables $X_{i}$ and $X_{j}$. If the MI value of two variables is higher than a threshold value, we consider them as neighbors and draw an edge between them. This

threshold could be given as a fixed value or can be updated based on MI values as follows:
threshold $=\alpha \times \operatorname{avg}(M I)$
The value of $\alpha$ controls the density of the edges in the MN network. A larger value $\alpha$ implies fewer edges and, therefore, a sparser structure requiring less computational time. In addition, if the number of neighbors to a decision variable is higher than the maximum number, MN only keeps the neighbors with the highest MI.

The structure learning results in a graph with neighborhood relationships that estimate variables' conditional probabilities.

## (c) Sampling

Unlike Bayesian networks, the MN model does not assume any ancestral ordering between variables to allow forward sampling techniques (Shakya et al., 2012). Thus, a Gibbs sampler is used as one of the Markov chain Monte Carlo (MCMC) methods for sampling. It is a randomized algorithm that allows obtaining samples from an approximation of the distribution of interest. Several different versions of the Gibbs sampler can be implemented for this purpose (Shakya et al., 2012). Algorithm 2 describes a version that is used for this work.
Algorithm 2. Gibbs sampler Algorithm in MN-based EDA.
1 Input: Neighborhood relationships
2 Generate a random solution $x=\left(x_{1},-x_{R}\right)$
3 for each iteration
4 Randomly choose a variable $x_{i}$ from $x$
5 Compute conditional probabilities $p\left(x_{i} \mid \hat{x}_{i}\right)$ according to Eq. (14), and the neighborhood relationship
6 Sample $p\left(x_{i} \mid \hat{x}_{i}\right)$ to get new $x_{i}$.
7 output: new sampled $x_{i}$

According to Algorithm 2, a single solution is created after terminating the Gibbs sampler algorithm. Hence, multiple executions should be done to generate the population.

### 4.1.3. Constraint programming (CP)

Constraint programming is a problem-solving approach that distinguishes between problem constraints and search algorithms. This approach is used to solve combinatorial problems requiring searching in a potentially exponential space to find an optimal solution, and it is often made possible by constraint propagation algorithms (Dincbas, 1988). Compared to other optimization models, CP models take advantage of the following key characteristics that make it a good method for optimization problems: (1) Rich modeling language suitable for representing complex real-world problems with discrete variables (Koltai et al., 2021), (2) Supporting a different variety of constraints including equality and inequality constraints, logic constraints, non-linear constraints, and almost any possible expression; (3) Prune the search space which contains infeasible solutions using constraint propagation mechanism which results in tackling several large problems. So unlike MIP problems, increasing the number of constraints may indeed be beneficial as it helps propagation (4) Ability to directly model with global constraints (handling relationships among large sets of decision variables), that implement efficient propagators (Oliveira \& Carravilla, 2017). Although there are specific well-performing global constraints that have been designed and tested for scheduling problems (Bukchin \& Raviv, 2018). Hence, CP models have attracted the attention of many researchers, particularly for scheduling problems (Esmaelian et al., 2021). It should be mentioned that our problem which is rooted in a complex real-world situation, is categorized as a scheduling problem. So it can benefit from some global constraints and non-linear constraints that CP offers.

In general, CP models can be divided into two groups: the constraint satisfaction problems; and the constraint optimization problems. In constraint satisfaction problems, the search procedure for finding a

Fig. 2. The encoding of decision variables for proposed modeling of the EVCSP.
solution includes assigning values to variables from each variable's domain, satisfying all the problem constraints. While in constraint optimization problems, the search procedures satisfy the problem constraints and find the best solution.

### 4.2. Proposed model

A competent EDA is designed using an efficient initial population, a suitable probabilistic model, a proper diversity control mechanism, and a hybrid local search method. An efficient initial population includes either diverse or high-quality solutions rather than random solutions. A suitable probabilistic model results in sampling more promising solutions. A diversity control mechanism provides an effective search that helps the algorithm prevent early trapping in local minima. Furthermore, a hybrid local search method enhances the algorithm's ability to explore the search space locally and provides an appropriate balance between the search method's exploitation and exploration abilities. Accordingly, in this study, we developed our EDA-based method while considering all these remarks. In the following, each remark is explained in more detail.

### 4.2.1. Efficient initial population

To achieve a suitable balance between the quality and diversity of solutions in the initial population, we use two stochastic dispatching rules, including the due time and the latest start time rules based on previous studies (Garcia Alvarez et al., 2018). The latest start time is defined as $L S T_{j}=d_{j}-c_{j}$ where $d_{j}$ is due time and $c_{j}$ is the charging time of $f^{\text {th }} \mathrm{EV}$. Hence, in this study, the initial population is generated according to Algorithm 3.

Algorithm 3. Initial Population Generation Algorithm.
1 Input: EVs due times and charging times
2 for each population member
3 Sort accordingly the due time vector
4 Sort ascendingly the latest start time $\left(L S T_{j}=d_{j}-c_{j}\right)$ vector
5 Generate an empty vector $R$ with length $M$
6 for $i=1: n$
7 Select a rule randomly from the rule list \{due time, latest start time, random \}
8 if random rule
9 Append an EV to position $i$ that is randomly selected from the list of nonselected EVs
10 if due time rule
11 Append an EV to position $i$ that is after previously appended EV in due time vector and not
12 yet selected in R
13 If no EV is found, then select EV using random rule
14 if latest start time rule
15 Append an EV to position $i$ that is after previously appended EV in latest start time
16 vector and not yet selected in R
17 If no EV is found, then select EV using random rule
18 output: initial population

### 4.2.2. Probabilistic model

Considering the objective function in our EVCSP, minimizing the total tardiness, we modeled our problem using two decision variables, encoding as Fig. 2.

1. $R$ - a vector representing a sequence of all EVs with length $M$;

![img-2.jpeg](img-2.jpeg)

Fig. 3. An example of a feasible solution according to the decision variables.
2. $L$ - a vector representing an assignment of each EV to charging line with length $M\left(1 \leq L_{i} \leq 3\right)$.

According to these decision variables, the start time of each EV $\left(s_{i j}\right)$ is not considered as a decision variable. Indeed, $s_{i j}$ is the earliest time that satisfies all problem constraints considering EV position in $R$ sequence and its value in $L$ vector $\left(l_{i}\right)$. To shed light on this method, consider a hypothetical example including 7 EVs with the same charging time ( 3 minutes) and arrival times $\{1,2,1,2,2,1,2\}$. One feasible solution includes $R=\{3,7,1,2,6,5,4\}$ and $L=\{2,2,1,1,1,3,3\}$. Also, in this example, $N=2, \Delta=0.2$. Fig. 3 shows the corresponding feasible solution. Compared to models in which start time is considered as a decision variable, our model complexity is reduced due to domain reduction.

To find a solution for these decision variables, we use the Mallows model and Markov network for encoding the distributions of $R$ and $L$ vectors, respectively.

The EV sequence $(R)$ is defined in a permutation space which makes the Mallows model a suitable choice for variable modeling. So, the probability distribution of permutation $R$ is estimated according to Eq. (10). Then, promising solutions (EV sequences) are generated through learning and sampling steps described in section 4.1.1.

Due to the shared power supply, EVs interact with each other once they seize a line. So, assigning a charging line to each EV $\left(1 \leq l_{i} \leq 3\right)$ depends on other EV's assignments. We use the Markov network to deal
with this behavior, a proper candidate for dealing with variable interactions. Here, each node of the Markov network represents $l_{i}$ and edges indicate the interaction among EVs. Once the Markov network is constructed, each EV is assigned to a charging line based on the status of its neighboring nodes.

### 4.2.3. Diversity control mechanism

Generally, elitism selection is used as the selection strategy in EDAs, giving preference to higher-quality solutions (Pelikan et al., 2015). By sampling from these elite populations over generations, population diversity diminishes, and the population becomes very similar (Dehnad, 2012). To control the diversity and avoid being trapped in local optima, we generate a random population with the same length as the current population. When the value of the objective function does not improve in 20 consecutive generations, the random population is added to the current population. Then the new promising solutions are selected based on the elitist strategy.

### 4.2.4. Heuristic local search method

Here, we present a local search method to improve each sampled solution considering their corresponding $R$ and $L$. The method moves backward from the current start time to the latest time for each randomly selected EV where the problem constraints are still satisfied. This procedure is repeated until all EVs are chosen.

To shed light on this method, consider the aforementioned
![img-2.jpeg](img-2.jpeg)

Fig. 4. An example of improving a feasible solution through the heuristic local search method.

![img-3.jpeg](img-3.jpeg)

Fig. 5. A feasible scheduling of EVs on three charging lines with minimum tardiness obtained from the proposed HMM-EDA Algorithm.
hypothetical example in 4.2.2. Fig. 4(a) and (b) show one of the corresponding feasible solutions and an improved solution obtained by the local search method, respectively.

### 4.2.5. The proposed HMM-EDA

Algorithm 4 presents our proposed HMM algorithm to solve the generalized EVCSP while minimizing the total tardiness according to previously introduced concepts and algorithms.

## Algorithm 4. HMM-EDA Algorithm for EVCSP.

1 Inputs:
2 Parameters of Mallows-based EDA method: Parameters in learning, sampling, and selection methods
3 Parameters of Markov Network-based EDA Method: Parameters in learning, sampling, and selection methods
4 Parameters of Algorithm: Population parameters, iteration, and termination conditions

## 5 Individual encoding:

$6 \quad R$ : a sequence of numbers $(1 \leq r_{i} \leq M)$ with length $M$ representing EV sequence
$7 \quad L$ : a vector $(1 \leq l_{i} \leq 3)$ with length $M$ representing each EV's line assignment 5 Algorithm:
9 Initialize variable $R$ of the population using Algorithm 3 and randomly initialize variable $L$.
10 For each population member, schedule each EV such that the earliest possible starting time is selected
11 while all constraints are satisfied.
12 Calculate the total tardiness for each population member and select promising solutions using elitism.
13 Initialize Mallows probability model for variable $R$
14 Initialize Markov network probability model for variable $L$
15 While termination criteria not met:
16 Sample solution using Algorithm 1 for variable $R$
17 Sample solution using Algorithm 2 for variable $L$
18 Schedule EVs through finding the possible earliest starting time for each EV in sampled $R$ and $L$.
19 Improve each schedule using the heuristic local search method described in section 4.2.4.
20 Select promising solutions using the diversity control mechanism introduced in section 4.2.3.
21 Update probability models of Mallows and Markov modeling using selected promising solutions

22 Output: A feasible sequence of EVs on charging lines with minimum tardiness

In the static variant, the algorithm is applied once to solve the problem for all EVs. However, in the dynamic variant, the algorithm is used for each problem instance $\left(P_{n}\right)$ in which the scheduling is applied for the pending EVs.

Fig. 5 shows feasible scheduling with minimum tardiness of an example obtained by Algorithm 4. This example includes a station with three charging lines with 100 EVs and $N=9 . \Delta=0.25$. The X -axis and the Y-axis corresponds to the problem time horizon and the number of active EVs in each time point, respectively. Light gray rectangles represent EVs that are charged before their due times. While the rest two-colored rectangles are EVs facing delays, the black part represents a portion of the charging time exceeding its due time. The step chart at the bottom of Fig. 5 shows the maximum imbalance between the lines in each time point, which meets the maximum imbalance constraint.

### 4.3. Proposed constraint programming (CP) model

We compare the performance of our proposed HMM-EDA with state-of-art meta-heuristic methods. We proposed a CP model to provide a baseline solving approach since it provides an optimal solution for our problem. It is worth mentioning that the mathematical programming method is too time-consuming when we have a large-scale problem size (Peng et al., 2014). So MP is impractical for large-scale EVCSP.

The CP model is written in OPL (Optimization Programming Language) and solves problems using "IBM ILOG CP optimizer". The usual way for solving a CP model is to run an automatic search. In this study, we use "Restart" as our search type method in which a depth-first search is applied, which is restarted from time to time, guiding toward an optimal solution (Laborie et al., 2018). The rest of this section discusses the variable definition and problem formulation in the CP model.

### 4.3.1. Variable definition

In our EVCSP, each EV has a start time and a charging time according to its scheduling behavior. In the CP optimizer, such time intervals are presented by "interval variables" characterized by a starting and ending. Integer expressions "startOf" and "endOf" provide access to the start time and end time for the corresponding interval variable, the scheduled EV (Laborie et al., 2018).

Optionality in interval variables is essential in scheduling problems presented by a Boolean presence status (presenceOf) (Laborie et al.,

2018). In our EVCSP, optionality means that each EV can be left unperformed in charging lines. We define $x_{i j}$ as an optional interval variable representing the $j^{\text {th }} \mathrm{EV}$ in the $i^{\text {th }}$ charging line. Also, the charging time of an EV $\left(c_{j}\right)$ is considered as the size of $x_{i j}$.

Allocation of scarce resources to time intervals is also another critical characteristic of scheduling. The evolution of a resource (power supply) over time in our EVCSP is modeled by a cumulative resource in which the CP optimizer provides "cumul function expression" for this aim. This expression is used to constrain the temporal evolution of resource usage (Laborie et al., 2018). In our model, the charging task related to each EV increases the usage level of charging lines by one unit. Similarly, once the charging task of the corresponding EV is ended, the usage level of charging lines is decreased by one unit. So, we consider $U_{i}$ as a cumulative function which represents the usage of $i^{\text {th }}$ charging line at any given time:
$U_{i}=\sum_{j=1}^{N} \operatorname{pulse}\left(x_{i j}, 1\right)$
Where pulse $\left(x_{i j}, 1\right)$ is the usage of $i^{\text {th }}$ charging line such that $x_{i j}$ increases the power supply usage by 1 unit at its start time of charging process and decreases usage by 1 unit when it releases the resource at its end charging time.

Also, dependent variables are implemented as OPL variable expressions (dexpr) defined through equality constraints. To count the number of active EVs at any given time, we define $\operatorname{count}_{i t}$ as a dependent variable which is described as follows:
$\operatorname{count}_{i t}=\sum_{j=1}^{N}\left(\operatorname{startOf}\left(x_{i j}\right) \geq t\right) \times\left(\operatorname{endOf}\left(x_{i j}\right)<t+1\right)$,
$\forall 1 \leq i \leq 3,1 \leq j \leq M, t \in$ time horizon

### 4.3.2. CP problem formulation

The proposed CP formulation for our EVCSP is described as follows:
$\min \sum_{i=1}^{3} \sum_{j=1}^{M} \operatorname{presenceOf}\left(x_{i j}\right) \times\left(\operatorname{endOf}\left(x_{i j}\right)-d_{j}\right)$
$\sum_{i=1}^{3} \operatorname{presenceOf}\left(x_{i j}\right)=1$
$\operatorname{presenceOf}\left(x_{i j} \times \operatorname{startOf}\left(x_{i j}\right) \geq a_{j}\right.$,
$\forall 1 \leq i \leq 3,1 \leq j \leq M$
$U_{i} \leq N, \quad \forall 1 \leq i \leq 3$
$\frac{\operatorname{count}_{i t}}{N} \leq \Delta, \quad \forall 1 \leq i, j \leq 3, t \in$ time horizon
The objective function (Eq. (20)) aims to minimize the total tardiness of all interval variables considering their end charging time and their due times with respect to problem constraints which are described in Eq. (21)-(24). The constraint defined in Eq. (21) ensures that an EV appears only in one charging line. Eq. (22) prohibits each EV from starting the charging process before its arrival time. According to constraint in Eq. (23), the number of active EVs at any given time in any given line should not exceed $N$. At last, Eq. (24) imposes an upper bound on the imbalance between two lines.

## 5. Experimental study

This section presents our experimental results regarding solving the EV charging scheduling problem using our proposed HMM-EDA method. To do that, we first described the benchmark dataset. Then, the parameters setting of the proposed method is presented. Then, in the last section, we evaluated our proposed HMM-EDA method and compared it

Table 4
Parameter setting of meta-heuristics based on the previous studies parameter settings.
with the proposed CP model and other state-of-art meta-heuristic methods, including simulated annealing (SA), discrete particle swarm optimization (PSO), and ant artificial bee colony (ABC).

### 5.1. Benchmark description

The introduced benchmark in this study (García-Álvarez et al., 2018) is used for evolution purposes. This benchmark data is aggregated from a sample station with three charging lines where each line has 60 charging points ( 180 charging points in total). This benchmark is classified into 72 sets. In each set, EVs' arrival and due times corresponding to the expected behavior of real EV owners in 30 different situations are given. So, there are 2160 samples (problems) in this benchmark. The benchmark is openly available on the web. ${ }^{1}$

Each set is represented by a tuple \{scenario.type. N. $\Delta$ \}. There are three different scenarios; In scenario 1 , the EV that arrived in the station are distributed such that there are two peak demands in the time horizon. In scenario 2 and 3, most EVs came to the station in a short time interval. However, in scenario 3 a more intensive due time is considered compared to scenario 2. Type value determines the distribution of EVs in charging lines wherein type 1, all EVs are distributed uniformly in all charging lines (e.g., one-third of EVs enter each line). In type $2,60 \%$ of EVs enter line $1,30 \%$ enter line 2 , and $10 \%$ enter line 3 . $N$ is the maximum number of active EVs that can be charged at any time in each line and it can be one of the values 20,30 or $40 . \Delta$ is the maximum imbalance parameter with values of $0.2,0.4,0.6$, or 0.8 .

We should note that in the introduced benchmark, line allocation is pre-determined. However, in this study, line assignment is also considered as a decision variable. Hence, type value in the set tuple is no longer meaningful in our considered problems which result in reducing the number of sets to 36 .

### 5.2. Parameters setting

Fine-tuning of parameters is required for most of the algorithms to obtain desired solutions. In this study, besides our proposed HMM-EDA method, we also apply the state-of-art meta-heuristic methods including SA, PSO, and ABC for solving the studied EVCSP. We set some of these meta-heuristic parameters according to these algorithms' settings in previous studies (Table 4).

To tune the rest of the parameters, both for meta-heuristics and our proposed HMM-EDA method, we use the Taguchi method, a powerful tool for parameter design (Dehnad, 2012). It identifies the best parameters and improves the performance characteristic with orthogonal

[^0]
[^0]:    ${ }^{1}$ Repository section in https://www.di.uniovi.es/iscop.

Table 5
The level of factors used for the L27 orthogonal designing method and the best level.
array technique and signal-to-noise (SN) ratios. In this study, the L27 orthogonal designing method is applied, and values for each parameter in each level of factors are tabulated in Table 5. The best level is also shown in bold-face and underlined for each parameter.

### 5.3. Performance comparison

Since our study is the pioneer in solving this generalized EVCSP problem, there aren't any other methods to compare. Hence, we solved the EVCSP with state-of-the-art metaheuristic methods for comparison purposes, including SA, PSO, and ABC. Also, for achieving an optimal solution, we proposed a CP model. Eventually, we compared our proposed HMM-EDA method with the performance of these methods in
terms of the gap from the best solution with respect to the objective. Notice that the CP model does not meet the optimal solution within each interval (two minutes). Hence, the CP model performance is not considered in the performance comparison of the dynamic variant.

All implementations are run on a laptop with an Intel ${ }^{\circledR}$ Core ${ }^{\mathrm{TM}}$ ( $7 \cdot 3$ GHz CPU, 32 GB of DDR4-3200 RAM, NVMe PCIe ${ }^{\circledR}$ SSD 1 TB, and Windows 10 PRO. Also, the proposed model was coded using MATLAB R2018a and the CP model was modeled and solved using IBM-ILOG-CPLEX-Optimisation Studio version 12.6. Due to the stochastic nature of the meta-heuristic algorithms, ten independent runs were executed for each instance (problem). Also, considering the dynamic nature of the problem (e.g., in/out EV flows in the station), it is necessary to reschedule EVs every couple of minutes (Garcia Alvarez et al., 2018). Hence, this study considers two-minute ( 120 s ) execution time as the termination condition in our proposed HMM-EDA and meta-heuristic methods. Nevertheless, in the CP model, no termination condition is set to achieve an optimal solution. It should be mentioned that the definition of decision variables and initial population in HMM-EDA and meta-heuristic methods are all the same.

As mentioned earlier, in the introduced benchmark, there are 36 sets comprising 30 instances in which each set is distinguished with its scenarios, and $N$ and $\Delta$ values. We solved all 30 EVCSPs in each set in which the total value of the object function (total tardiness) is calculated over all instances. Table 6, Table 7, and Table 8 reported the average value of the computed objective function in each set over ten independent runs. Also, the total objective function value of the CP model is reported in each set as the $\mathrm{Obj}^{*}$ in the static problems. The best value for the objective function among all meta-heuristic and HMM-EDA methods is bold-faced and underlined in each table.

According to Table 6-8, our proposed HMM-EDA outperforms all other meta-heuristics, including ABC, PSO, and SA, in every single set in

Table 6
The total objective function values in scenario 1 with corresponding N and $\Delta$ values.
Obj* refers to the best solution with respect to the objective.

Table 7
The total objective function values in scenario 2 with corresponding N and $\Delta$ values.
Table 8
The total objective function values in scenario 3 with corresponding N and $\Delta$ values.
Table 9
Total gap values from the best solution with respect to the objective (CP results) in the static variant.
terms of total tardiness in both dynamic and static problems.
In addition, in Table 9, total gap values from the best solution with respect to the objective (CP results) are reported in the static variant. Results show the superiority of our proposed HMM-EDA algorithm.

In Fig. 6, the performance of the proposed HMM-EDA method is compared with the CP and the meta-heuristics in all different sets of statice problems. Each set is distinguished with a tuple (Scenario, N, $\Delta$ ).

According to Fig. 6, the solution of scenario 3 is those with higher total tardiness compared to the rest. This results from existing peak demands in the time horizon and intensive due time for EVs. Moreover, with increasing the N and $\Delta$ values in each scenario, the total tardiness is decreased due to the constraint on the active charging points' upper bound and power imbalance constraint. From the performance comparison point of view, our proposed HMM-EDA outperforms the metaheuristics, especially in more complex problems (e.g., scenario 3 with the lowest $N$ and $\Delta$ value).

### 5.4. Performance comparison based on previous studies

To compare the performance of EDA-based methods in solving the EVCSP, which is introduced in (García Alvarez et al., 2018), we proposed a simpler version of our method. According to the specific problem setting in which EV's line assignment is pre-defined, we used MMEDA as our solving method since we have only one type of decision variable, i.e., the sequence of EVs.

We compared the MM-EDA with other methods proposed in previous studies (García Alvarez et al., 2018), including a Memetic Algorithm (MA), Artificial Bee Colony (ABC), a Hybrid Artificial Bee Colony (hABC), and EVS (Hernández-Arauzo et al., 2015). So, in Table 10-12, we reported the total value of the objective function in these methods compared to our (MM-EDA) corresponding to each scenario. Since line assignments are pre-defined in these samples, each set is characterized with a tuple (scenario, N. $\Delta$, type) in which type determines the distribution of EVs in power lines. The best value for the objective function is shown in bold-face and underlined in each table. Also, the number in parenthesis for each value represents the rank in ascending order of all compared method performances.

Based on the results tabulated in Table 10-12, the proposed EDAbased method (MM-EDA) ranked first in most samples.

In Table 13, methods are compared in terms of ranking from their objective function values. Notice that EVS and ABC method's results are not reported for all instances. Also, Their performance in the reported instances is not among the best; hence, we discarded them in the rank
![img-4.jpeg](img-4.jpeg)

Fig. 6. Performance comparison of the proposed HMM-EDA method with CP and the meta-heuristics in all different sets in the static problems.

Table 10
The total objective function values in scenario 1 with the corresponding type, N , and $\Delta$ values (based on the EVCSP introduced in (Garcia Alvarez et al., 2018)). Value in parenthesis represents the rank of its corresponding method.
Table 11
The total objective function values in scenario 2 with the corresponding type, N , and $\Delta$ values (based on the EVCSP introduced in (Garcia Alvarez et al., 2018)). Value in parenthesis represents the rank of its corresponding method.
comparison reported in Table 13.
As shown in Table 13, MM-EDA outperforms the other techniques and shows the superiority of EDA-based methods in solving EVCSPs.

To show the superiority of the proposed MM-EDA over other methods, the objective function values obtained from each method are subtracted from the best answer in each set. The sum of the total gap from the best values on all data is reported in the third row of Table 13.

Best values are underlined and bold-faced in Table 10-12. Notice that the smaller this metric is, the better the corresponding method performance is. Hence, considering the problem's objective (minimizing the total tardiness) and real-world problem conditions, the proposed MM-EDA shows significant improvement in solving the introduced EVCSP.

Table 12
The total objective function values in scenario 3 with the corresponding type, N , and $\Delta$ values (based on the EVCSP introduced in (Garcia Alvarez et al., 2018)). Value in parenthesis represents the rank of its corresponding method.
Table 13
Method comparison in terms of ranking from their objective function perspective in solving the introduced EVCSP in (Garcia Alvarez et al., 2018).

## 6. Conclusion

This study aims to solve an EVCSP inspired by an actual charging station while minimizing all EVs' charging delays (tardiness). The most important constraint in this problem is balancing power consumption between charging lines, limiting simultaneous charging EVs. Usually, line allocation is pre-determined in EVCSPs. However, in this study, line assignment is also considered as a decision variable. Therefore, considering the objective function in our EVCSP, minimizing the total tardiness, we modeled our problem using two decision variables: a vector representing a sequence of all EVs; and a vector representing an assignment of each EV to a charging line.

Several methods have been proposed so far for solving this problem. Deterministic optimization models such as CP or linear programming (LP) usually suffer from the curse of dimensionality (De Farias, 2002). Thus, these models require a long processing time to find the optimal solution in EVCSP due to the high dimensions of decision variables in real-world situations (the introduced benchmark, which includes 180 EVs). Accordingly, metaheuristic algorithms are proper choices to obtain good results in a reasonable computational time. We proposed a method based on EDAs. This is because of existing possible interrelationships among EVs during scheduling procedures and the competency of EDAs in handling these relations among decision variables. Our proposed method is a hybrid EDA in which a Markov network and a Mallows model are simultaneously used, called "HMM-EDA". Markov network is a suitable approach for dealing with interaction among variables. So, it is proposed to handle charging line assignment
while considering these interactions. In addition, we proposed a Mallows-based-EDA since the Mallows model is suitable for permutation problems by considering EV sequence as a permutation problem.

Our method is evaluated by simulation on a benchmark dataset comprising several examples with different characteristics. We compared our method with a constraint programming (CP) model and the state-of-art meta-heuristic methods in terms of the objective function value. Results show the superiority of our proposed method in terms of the gap from the best solution with respect to the objective compared to other meta-heuristics.

It remains for future work to investigate the performance of our proposed HMM-EDA method while considering other constraints such as EV state-of-charge and slow/fast charging EVs (introduced in Table 2) in the EVCSP formulation. In addition, other objective functions such as charging price (Savari et al., 2019) combined with total tardiness could also be considered in future studies to examine our proposed HMM-EDA method in multi-objective optimization.

## CRediT authorship contribution statement

Hadi Shahmoradi: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data curation, Writing - original draft, Writing - review \& editing, Visualization. Majid Esmaelian: Conceptualization, Methodology, Validation, Formal analysis, Investigation, Resources, Data curation, Writing - original draft, Writing - review \& editing, Visualization, Supervision, Project administration. Hossein Karshenas: Conceptualization, Methodology, Validation, Formal analysis, Investigation, Writing - original draft, Writing review \& editing.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
