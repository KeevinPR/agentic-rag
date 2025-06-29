# An insight to the performance of estimation of distribution algorithm for multiple line outage identification 

A. Ahmed ${ }^{\text {a }}$, Q. Khan ${ }^{\text {a }}$, M. Naeem ${ }^{\text {b, }^{*}}$, M. Iqbal ${ }^{\text {a }}$, A. Anpalagan ${ }^{\text {c }}$, M. Awais ${ }^{\text {a }}$<br>${ }^{a}$ COMSATS Institute of Information Technology (Wah Campus), Pakistan<br>${ }^{\text {b }}$ COMSATS Institute of Information Technology (Wah Campus), Pakistan and Ryerson University, Canada<br>${ }^{*}$ Ryerson University, Canada

## A R T I C L E I N F O

Keywords
Estimation of Distribution Algorithm
Multiple Line Outage Detection
Smart Grid

A B STR ACT

Realtime information relating to line outages has significant importance to pre-empt against the power system blackouts. Realtime information can be obtained by using phasor measurement units (PMUs) facilitating the realtime synchronized observations of voltage and current phasors at buses being monitored. Different optimization formulations including but not limited to linear, integer, stochastic, mixed integer and NP hard combinatorial optimization have been used to manipulate these phasor measurements for the detection of line outages. Single and double line outages can be addressed using combinatorial optimization but these are infeasible to apply for the detection of multiple line outages as the increased number of lines increases computational complexity. To alleviate the exponentially increased complexities of these combinatorial optimization problems, while investigating for multiple line outage, evolutionary, Estimation of Distribution Algorithm is used. This method gives near optimal solution in which computational complexity and time is reduced efficiently. In this paper we scrutinize the use of phasor angle measurements to detect multiple power line outages. The proposed EDA is compared with binary particle swarm optimization (BPSO) algorithm, adaptive BPSO and genetic algorithm (GA) in terms of line outage detection performance, fitness convergence w.r.t. iterations and time consumption. The simulation results depict that the proposed EDA outperforms the other state of the art algorithms.

## 1. Introduction

Power systems represent the networks of various electrical devices namely, power plants, transformers, transmission lines and distribution lines aimed to provide the electricity to the consumers. Utility companies are striving to provide interruption free and ample supply of electricity to their customers at the lowest possible rates [1]. When line outage occurs, the power flow in the system is changed, and some the of lines become overloaded which results in line failures. These line failures further cause cascaded failures, if not properly maintained in time. This situation can culminate the blackout of the whole power system, or some major part of the system.

It is critically important to have a mechanism of precise and swift observation of the system states to achieve power system stability and reliability [2]. Timely detection and restoration of line outage requires accurate identification of the fault location using realtime measurements of various transmission line parameters. This will enable the utilities to minimize the outage time, operational expenses and to increase the
customer satisfaction [3-5]. Phasor measurement units can be used to facilitate GPS-synchronized more precise, time correlated observations relating to voltage and current phasors [6]. PMUs have the capability to furnish various phasor quantities namely, magnitude and angles of the bus voltages along with the time of observation of each measurement. These measurements are time synchronized as each PMU uses common time source [7].

In order to realize a cost effective identification of power line outages, the first step relies on an optimal PMU placement. The objective of this step is to obtain a complete network observability with minimum number of PMUs. In the next step, the rich phasor data is exploited to identify the individual lines in outage. The literature proposes a number of solutions to both steps. Some remarkable works are discussed as follows. In [8], a Support Vector Machine (SVM) classification tool based on artificial intelligence has been suggested to find the health of the transmission line. A single line outage identification technique has been proposed in [9] employing PMUs phasor angle measurements and the other topological information relating to power system. The double line outage

[^0]
[^0]:    a Corresponding author.
    E-mail address: muhammadnaeem@gmail.com (M. Naeem).

Table 1
Overview of state of the art for line outage identification problem.
identification was addressed by the authors using system topology information before and after the line outage in addition to the knowledge of the PMUs measurements. In [10], preventive integrated equipment maintenance scheduling problems in power systems are discussed. Teaching Learning Based Optimization (TLBO) has been used as a prime optimization tool, as it has been proven to be very effective optimization algorithm when applied to various practical optimization problems and its implementation is simple involving less computational effort. The model for unit commitment considering generator outages is formulated in [11], where the reliability requirement is incorporated into the spinning reserve constraint in the optimization design. An intelligent technique based on cascade neural network (CNN) is presented in [12] for identification of the overloaded transmission lines in a power system and for prediction of overloading amount in the identified overloaded lines. The task of security enhancement is formulated as a multi-objective optimization problem with minimization of fuel cost and minimization of FACTS device investment cost as objectives in [13].

A binary particle swarm optimization (BPSO) based methodology for the optimal placement of PMUs is proposed in [14], using a mixed measurement set. Another efficient technique to reduce the number of PMU placement, with full network observability, is presented in [15]. Cascaded effect in power grids are modeled and discussed in [16], where cascaded effects are the typical phenomenon of dependencies of components inside a system or among systems. For on-line voltage security assessment of power systems, a novel core vector machine (CVM)-based algorithm is proposed in [17]. An intelligent technique based on artificial intelligence for automatically detecting incidents on power distribution networks is presented in [18]. An investment decision model to determine the optimal placement of PMUs that guarantees the full observability of the power grid is presented in [19]. A problem-specific genetic algorithm is implemented to get the near optimal solution. An intelligent search-based approach for PMUs placement in the power system is proposed in [20], while maintaining complete observability. A new method for the optimal placement of PMUs is proposed in [21] using binary integer linear programming. Least possible number of PMUs are used, guaranteeing the full observability of the power system. In [22], the optimal placement for PMUs is investigated, along with PDCs (Phasor Data Concentrators) to maximize the reliability of data transmission. In [23], branch-and-bound algorithm, based on a linear programming and greedy heuristic relaxation, is proposed to find the globally optimal locations for PMUs.

To reduce exponentially increased complexities of these combinatorial optimization problems, while investigating for multiple line outage, an iterative probabilistic approach, namely Estimation of Distribution Algorithm (EDA), is proposed in this paper. EDA is basically stochastic optimization technique. It explores the space of potential solutions by building and sampling explicit probabilistic models of promising candidate solutions. EDA has the ability to speed up computation because it evaluates the candidate solutions simultaneously on parallel processors. It makes a population of some specific size. The population has some specific number of candidate solutions. Thus processing all of these solutions, inside the population based on some probability vector, in parallel reduces efficiently the computational burden and time. EDA is used to solve a variety of problems, like system-level synthesis problems [24], scheduling problems [25], estimation problems [26], [27], and much more. Therefore, in this paper the line outage problem is investigated using EDA. Table 1 shows an overview of the research work till now on the
topic of line outage detection and identification. It is quite clear that research work has already been carried out for the identification of single, double and multiple line outages, but the novelty in our proposed approach is the variable multiple line outage detection. In case of previous multiple line outage detection solutions, the algorithms were intended to detect static number of line outage, but in our proposed implementation the algorithm works well, independent of the number of outages. The proposed EDA is also compared with the state of the art binary particle swarm optimization algorithm (BPSO), adaptive BPSO (ABPSO) algorithm, using multiple transfer functions, and the genetic algorithm (GA). It is shown that the EDA outperforms the other competitors in terms of line outage detection performance and the consumed time by the algorithm.

The remaining part of the paper is organized as: the system model and problem formulation are discussed in section II, proposed algorithm is discussed in section III, results are discussed in section IV, whereas the conclusion is drawn in section V.

## 2. System model and problem formulation

We consider a Linear DC power flow model. The power transmission network consists of $L$ transmission lines and $N$ number of buses. The transmission system is represented by a weighted graph $G=\{5, \mathscr{E}\}$, where $5=\{1.2 .3 \ldots . N\}$ is the set of buses and $\mathscr{E}=\{(m, n)\} \subseteq N \times N$ is the set of edges. We represent the set of transmission lines by $\mathcal{L}=\{1,2$, $3 \ldots . L\}$. For line $l \in \mathscr{L}$ that connects the buses $n$ and $m$, we denote the reactance along $(m, n)$ by $x_{l}$, as well as $x_{m n}=x_{n m}$, and we define the $i$ th element of its incidence vector $m_{i}$ as follows:
$m_{i}= \begin{cases}1 & ; \text { if } i=n \\ -1 & ; \text { if } i=m \\ 0 & ; \text { otherwise }\end{cases}$
To satisfy the conservation-of-flow constraint in the linear DC model, the amount of power injected into bus must be equal to the amount that flows out of it, i.e.,
$P_{n}=\sum_{m \in \mathbb{N}_{n}} P_{n m}$,
where, $P_{m n}$ is the power flow from bus $m$ to bus $n$ through line $l \in \mathcal{L}$ and it is represented as
$P_{n m}=\frac{1}{x_{n m}}\left(\theta_{n}-\theta_{m}\right)$,
where, $x_{m n}$ is the reactance along line $(m, n)$, as well as $x_{m n}=x_{n m}, \mathcal{N}_{m}$ is the set of neighboring buses connected to bus $n$. $\theta_{m}$ and $\theta_{n}$ are the voltage phasor angles of buses $m$ and $n$, respectively. The real power injections in $\mathbf{p} \in R^{N}$ and the voltage phases in $\theta \in R^{N}$ can be stacked into a matrix vector form as,
$\mathbf{p}=\mathbf{B} \theta$,
where $\mathbf{B} \in R^{N \times N}$ is a symmetric matrix and its ( $m, n$ )th entry is given by,
$B_{n m}= \begin{cases}-\frac{1}{x_{n m}^{-1}} & ; \text { if }(m, n) \in \mathscr{E} \\ \sum_{n \in \mathbb{N}_{n}} x_{n m}^{-1} & ; \text { if } m=n \\ 0 & ; \text { otherwise }\end{cases}$
Using $m_{l}$ of (1) an alternative representation of $\mathbf{B}$ can be expressed as [37],
$\mathbf{B}=\mathbf{M D}_{\mathbf{x}} \mathbf{M}=\sum_{l=1}^{L} L \frac{1}{x_{l}} m_{l} m_{l}^{T}$,
where, $x_{l}$ is the $l$ th diagonal entry and $\mathbf{D}_{\mathbf{x}}$ is the diagonal matrix. $\mathbf{M}$ is formed by columns $\left\{m_{l}\right\}_{l=1}^{L}$ of length $N$. The dimension of bus line

incidence matrix $\mathbf{M}$ is $N \times L$, with an $(n, l)$ th entry given as,
$M_{n l}= \begin{cases}1 & ; \text { if } l$ th line is from $n$th bus \\ -1 & ; \text { if } l$ th line is to $n$th bus \\ 0 & ; \text { otherwise }\end{cases}$
where the order of diagonal matrix $\mathbf{D}_{\mathbf{x}}$ is $N \times N$ and the order of matrix $\mathbf{B}$ is $N \times N$.

State of the interconnected grid before the line outage occurrence is termed as the pre-event state. At this state, the real power injections to the interconnected grid is given in (4). The state of the interconnected grid after any line outage event is termed as post-event state. An outage event corresponds to a loss of a subset of lines in $\mathbb{L}$. At this post-event state, the real power injections to the interconnected grid is,
$\mathbf{p}^{\prime}=p+\eta=B^{\prime} \theta^{\prime}$,
where $\mathbf{B}^{\prime}$ is post-event Laplacian matrix of weighted graph $G^{\prime}=\left\{\mathbb{N}, \mathscr{E}^{\prime}\right\}$, $\theta^{\prime}$ is the post-event phasor angle vector, and $\eta$ is the noise, and is the small difference between $\mathbf{p}^{\prime}$ and $\mathbf{p}$. It is usually modeled as Gaussian noise vector with zero mean and covariance matrix $\sigma_{n}^{2} \mathbf{L}$

Substituting the pre-event power flow model (4) into the post-event one in (8) yields,
$\mathbf{B} \theta+\eta=\mathbf{B} \theta^{\prime}-\widetilde{B} \theta^{\prime}=\mathbf{B}^{\prime} \theta^{\prime}$.
In the matrix form we can write,
$\widetilde{\mathbf{B}}=\mathbf{M} \mathbf{D}_{\mathbf{x}} \operatorname{diag}[\mathbf{b})] \mathbf{M}^{\mathrm{T}}$.
where $\mathbf{b}=\left\{b_{l}\right\}_{l=1}^{L}$ is a $L \times 1$ binary vector defined as,
$b_{l}= \begin{cases}1 & ; \text { if line } l \text { is in outage } \\ 0 & ; \text { if line } l \text { is not in outage }\end{cases}$
therefore, $b_{l}=1$ if the $l$ th bus belongs to subset of lines in outage denoted by $\mathscr{E}$, where $\mathscr{E} \subset \mathscr{E}$, and $b_{l}=0$ if the $l$ th bus does not belong to $\mathscr{E}$. If $\theta=$ $\theta^{\prime}-\theta$, or other way around $\theta^{\prime}=\theta+\theta$, (9) will become,
$\mathbf{y}=\mathbf{B}^{\theta^{\prime}} \mathbf{B} \theta^{\prime}=\widetilde{\mathbf{B}} \theta^{\prime}+\eta$,
further we get,
$\mathbf{y}=\mathbf{B}^{\theta^{\prime}} \mathbf{A}_{\theta^{\prime}} \mathbf{b}+\eta$,
where $\mathbf{A}_{\theta^{\prime}}=\operatorname{diag}\left\{\mathbf{M T} \theta^{\prime}\right\}$. Therefore, the objective is to find lines in $\mathscr{E}^{\prime}$. Mathematically, objective function can be defined as,
$P 1: \quad \tilde{b}=\underset{\mathbf{b} \in[0,1)^{2}}{\operatorname{argmin}}\left\|\mathbf{y}-\mathbf{A}_{\theta^{\prime}} \mathbf{b}\right\|_{2}^{2}$

## Example

As an example, the power flow model of an interconnected system is shown, where $N=7$ and $L=10$. The incidence matrix of the power flow model can be shown as,
$\mathbf{M}=\left[\begin{array}{cccccccccc}1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & -1 & 1 & -1 & 0 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 & -1 & 0 & 1 & 0 & -1 & 0 \\ 0 & 0 & -1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & -1 & -1 & 0 & -1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1\end{array}\right]$
The diagonal matrix given in (6) will be,
$\mathbf{D}_{\mathbf{x}}=\operatorname{diag}(\mathbf{a})$
where $\mathbf{D}_{\mathbf{a}}$ is a diagonal matrix, with $\mathbf{a}=\left[\begin{array}{llllllll}1 & \frac{1}{a} & \frac{1}{b} & \frac{1}{c} & \frac{1}{d} & \frac{1}{e} & \frac{1}{f} & \frac{1}{g} & \frac{1}{h} & \frac{1}{i} & \frac{1}{j} \end{array}\right]$ are the diagonal elements.

Therefore, substituting (15) and (16) in (6) we get,
$\mathbf{B}=\left[\begin{array}{cccccccccc}X_{1} & 0 & -\frac{1}{a} & -\frac{1}{b} & 0 & 0 & 0 \\ 0 & X_{2} & -\frac{1}{d} & 0 & -\frac{1}{c} & 0 & 0 \\ -\frac{1}{a} & -\frac{1}{d} & X_{3} & -\frac{1}{e} & 0 & -\frac{1}{f} & 0 \\ -\frac{1}{b} & 0 & -\frac{1}{e} & X_{4} & 0 & -\frac{1}{g} & -\frac{1}{i} \\ 0 & -\frac{1}{c} & 0 & 0 & X_{5} & -\frac{1}{h} & 0 \\ 0 & 0 & -\frac{1}{f} & -\frac{1}{g} & -\frac{1}{h} & X_{6} & -\frac{1}{j} \\ 0 & 0 & 0 & -\frac{1}{i} & 0 & -\frac{1}{j} & X_{7}\end{array}\right]$ where
$X_{i}=\left\{\begin{array}{ccc}\frac{1}{a}+\frac{1}{b} & ; & \text { for } s=1 \\ \frac{1}{c}+\frac{1}{d} & ; & \text { for } s=2 \\ \frac{1}{a}+\frac{1}{d}+\frac{1}{e}+\frac{1}{f} & ; & \text { for } s=3 \\ \frac{1}{b}+\frac{1}{e}+\frac{1}{g}+\frac{1}{i} & ; & \text { for } s=4 \\ \frac{1}{c}+\frac{1}{h} & ; & \text { for } s=5 \\ \frac{1}{f}+\frac{1}{g}+\frac{1}{h}+\frac{1}{i} & ; & \text { for } s=6 \\ \frac{1}{i}+\frac{1}{j} & ; & \text { for } s=7\end{array}\right.$
Each entry in (17) satisfies the conditions shown in (5). Let us assume, $\mathbf{b}=\left[\begin{array}{lllllllll}1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\end{array}\right]^{\mathrm{T}}$ leads to, $\mathbf{C}=\operatorname{diag}\{\mathbf{b}\}$, where $\mathbf{C}$ is a diagonal matrix with $\mathbf{b}$ in its diagonal. The post-event phasor vector can be written as $\theta^{\prime}=\left[\begin{array}{lllllllll}\theta_{0}^{\prime} & \theta_{1}^{\prime} & \theta_{2}^{\prime} & \theta_{3}^{\prime} & \theta_{4}^{\prime} & \theta_{5}^{\prime} & \theta_{6}^{\prime}\end{array}\right]$ and the vector for small perturbation between $\mathbf{p}$ and $\mathbf{p}^{\prime}$ can be written as $\eta^{\prime}=\left[\begin{array}{llllllllll}\eta_{0}^{\prime} & \eta_{1}^{\prime} & \eta_{2}^{\prime} & \eta_{3}^{\prime} & \eta_{4}^{\prime} & \eta_{5}^{\prime} & \eta_{6}^{\prime}\end{array}\right]$.

Substituting values of $\mathbf{M}, \mathbf{b}, \mathbf{D}_{\mathbf{x}}$ and $\theta^{\prime}$ in (13) yields,
$\mathbf{y}=\left[\begin{array}{c}-\frac{1}{a}\left(\theta_{0}^{\prime}-\theta_{2}^{\prime}\right)+\eta_{0} \\ \eta_{1} \\ -\frac{1}{a}\left(\theta_{0}^{\prime}-\theta_{2}^{\prime}\right)+\eta_{2} \\ \eta_{3} \\ \eta_{4} \\ -\frac{1}{j}\left(\theta_{6}^{\prime}-\theta_{5}^{\prime}\right)+\eta_{3} \\ -\frac{1}{j}\left(\theta_{6}^{\prime}-\theta_{5}^{\prime}\right)+\eta_{6}\end{array}\right]$
where (18) indicates the noisy version of phasor differences. The objective is then to find the vector $\mathbf{b}$ for which the norm in (14) gets minimum results. The problem mentioned in (13) is an integer programming, as the decision variable $\mathbf{b}$ contains either a ' 0 ' or a ' 1 ' in any particular entry. The computational complexity of the problem increases exponentially with the increase of number of power lines. Therefore, to get an optimal solution in less computations, a meta-heuristic approach is used.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Power flow model.

## 3. Estimation of distribution algorithm

EDA is one of the types stochastic optimization algorithms, where it optimizes a function by keeping track of the statistics of the population. EDA follows iterative probabilistic approach to find the sub-optimal solution. This is the reason that in each iteration the new population is generated, instead of keeping the former population alive. In each generation, the population with strong statistics is selected, so that the new population is more healthier. EDA has three main steps of the algorithm, i.e., 1) how to select the healthier candidate solutions from the total population, 2) what statistics are to be calculated from the selected solutions, and 3) how to use the calculated statistics to produce the new population. Keeping in mind the above discussion, EDA performs following steps to find the solution:

1. Generate initial population. The initial population is obtained by sampling according to the uniform distribution. As the line outage detection problem is a binary problem, the population will be binary in nature, where each ' 1 ' will represent if that particular line is in outage and every ' 0 ' will represent the line in normal condition.
2. According to the fitness function, evaluate the current population. For the said problem, the fitness function is shown in (14).
3. Sort the individuals according to the fitness inside the current population.
4. If the best candidate solutions (the one with least fitness in the line outage problem) satisfy the convergence criterion then terminate the simulation. There are some other termination criterion as well, e.g.,

Table 2
IEEE bus systems' details.

the number of generations. In the case of number of generations, the simulation run for a fix number of iterations.
5. Select the best candidate solutions (individuals) from current population. As the fitness function in (14) is a minimization function, the candidate solutions with minimum fitness will be selected, according to selection probability. The selection probability is an input to the function. In our case, we have set the selection probability equal to 0.5 , i.e., $50 \%$ of the best individuals will be selected.
6. On the basis of best candidate solutions, estimate the probability distribution of each feature, i.e., the probability distribution of ' 1 's and ' 0 's in each column of the selected population.
7. If the fitness does not change for $L$ many generations, apply thresholding, i.e., truncate the probability of a feature $j$ to 0.75 if it exceeds 0.85. Similarly, wrap the probability of a feature $j$ to 0.25 if it goes below 0.15 . In this way, the pre-mature convergence can be avoided, which eventually leads to local minima or maxima problems.
![img-1.jpeg](img-1.jpeg)

Fig. 3. Success generation ratio for IEEE 14-bus system.
![img-2.jpeg](img-2.jpeg)

Table 3
Time consumed (in seconds) by different algorithms for IEEE-14 bus system.
8. Generate new candidate solutions (individuals) on the basis of new probability vector obtained from the selected candidate solutions in the current population. Replace the bad candidate solutions with newly generated candidate solutions and generate a new population having better candidate solutions as compared to the previous population.
9. Go to step 2 and repeat all the steps from 2 to 6 Fig. 1.

The flow diagram of EDA is shown in Fig. 2.

## 4. Results and discussion

We have tested the algorithm on IEEE 14-bus system, 30-bus system, 39-bus system and 118-bus system. The details of the considered IEEE benchmark bus systems are shown in Table 2. For a fair comparison of the proposed algorithm with other state-of-the-art algorithms, success generation ratio (SGR) metric is derived. The SGR is given as,
$S G R=\frac{E_{s} / \Omega}{\widetilde{G}_{s} / G}$,
where $\Omega$ represents the total number of Monte Carlo iterations, $\widetilde{G}_{s}$ represents the mean of best generations of algorithm $x, G$ represents the total number of algorithm generations. It is clear that a larger SGR value is desirable, which means a larger numerator and smaller denominator. Larger numerator can be achieved if the algorithm successfully identifies the lines in outage during the Monte Carlo simulations. For example, the best case could be when $E_{s}=\Omega$ and $\widetilde{G}_{s}=1$, which would mean that the algorithm $x$ correctly identifies the lines in outage in a single algorithm generation, during all Monte Carlo iteration. To make the SGR more understandable, lets take an example where an algorithm ' $x$ ' correctly identifies the lines in outage 700 times out of total 1000 Monte Carlo iterations, and on average the algorithm ' $x$ ' takes 30 algorithm generations, out of total 50 algorithm generations, to find the best solution. It means $\Omega=1000 . E_{s}=700 . \widetilde{G}_{s}=30$ and $\widetilde{G}=50$, results in an SGR value of $\frac{900,1000}{30,50}=\frac{0.5}{0.6}=1.667$. The proposed algorithm is compared with ABPSO [53], BPSO and GA. Both the ABPSO and BPSO are further simulated with different ' S ' type transfer functions, given in [54]. ${ }^{1}$ In Fig. 3, the SGR results are shown.

In the ABPSO, the inertia weight is linearly reduced during the BPSO iterations. According to [55] the linearly reduction of inertia weights w.r.t. to the time (generations) enhances the computational efficiency. The reduction of the inertia weight is carried out as,

[^0]where $w_{i}$ and $w_{j}$ are initial and final weights, respectively, $G$ is maximum algorithm iterations, $i$ is the current iteration. Along with the time varying inertia weight, the time varying acceleration coefficients are also introduced in [56]. The acceleration coefficients control the movement of the particles, either according to local decision or according to the global decision. If both the acceleration coefficients are of same weight, then movement of the particles is influenced equally from social and local behaviours. The time varying acceleration coefficients efficiently controls the search process and the convergence to the global solution. The time varying acceleration coefficients restrict the movement of particles around the search space during the early generations, whereas in the later generations they force the particles to follow the trend of social behavior, which eventually reduces the affect of pre-mature convergence in BPSO. The time varying acceleration coefficients are shown as,
$c_{1}=\left(c_{1 i}-c_{1 j}\right)\left(\frac{i}{G}\right)+c_{1 i}$,
$c_{2}=\left(c_{2 i}-c_{2 j}\right)\left(\frac{i}{G}\right)+c_{2 i}$
where $c_{1 f}<c_{1 i}$ and $c_{2 f}<c_{2 j}$ are constants. From (21) it is observed that the value of acceleration coefficients vary from $c_{i}$ to $\left(2 c_{i}-c_{f}\right) . G$ is the maximum algorithm iterations, and $i$ is current iteration. In (20) and (21), the inertia weight and acceleration coefficients are adaptively changing with a view of enhancing the computational efficiency, improving the search capabilities and obtaining the global optimal solution.

Transformation function is an important factor, which eventually affects the performance of a BPSO algorithm. The simulations are carried out using different ' S ' type transfer functions for BPSO and ABPSO. In the detection performance and time consumption results, the BPSO(Sx) term means the BPSO result with ' Sx ' transfer function. Similarly, ABPSO(Sx) means the ABPSO result with ' Sx ' transfer function. Following S-functions are used in this work,
$S_{1}=\frac{1}{1+e^{-2 x}}, \quad, \quad S_{2}=\frac{1}{1+e^{-2}}$
$S_{3}=\frac{1}{1+e^{2 f}}, \quad, \quad S_{4}=\frac{1}{1+e^{2 f}}$
It is evident from Fig. 3 that for all considered number of line outages, the proposed algorithm gives a better success in terms of line outage detection and identification in fewer algorithm generations w.r.t. to other state of the art algorithms. In this peculiar case, we have obtained the results using Monte Carlo simulations. Similarly, the timing comparison of the proposed EDA is also shown in Tables 3 and 4 for IEEE-14 and -30 bus systems, respectively. In the tables, $\Delta$ denotes the population size,


[^0]:    ${ }^{1}$ The simulation are also carried out for BPSO and ABPSO with various 'V' type transfer functions, but the results are very poor. Therefore, adding the poor ' V ' types transfer functions curves clutter the figures.

Table 4
Time consumed (in seconds) by different algorithms for IEEE-30 bus system.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Fitness function vs. algorithm iterations for IEEE-14 bus system.
whereas $G$ denotes the number of algorithm iterations. All the simulations are carried out on a single machine with Intel core I7-4790 CPU @ 3.60 GHz clock frequency and 8 GB RAM installed on it. The tables show the results in terms of the mean, median, mode and standard deviation. All the metrics are calculated using the results of time taken by each algorithm in each Monte Carlo iteration. Three different population sizes and algorithmic iterations are considered for the timing comparison. It is again very clear that the proposed EDA takes much lesser time than its other competitors.

Finally, the performance of the proposed algorithm is verified w.r.t.
the fitness function's value versus the algorithm iterations. Fig. 4 shows the decaying trend of the fitness function for EDA and other algorithms. It is quite clear from the figure that the proposed EDA attains the best solution in fewer number of iterations than the other algorithms. The fitness trend is shown for different scenarios, where scenario 1 shows the fitness vs. iterations graph when there is one line in outage. Similarly, scenario 2 depicts the simulation results when there are two lines in outage, and so on.

After validating the EDA against its other competitors, the insight of EDA is shown. Figs. 5 and 6 show the simulation results of IEEE 14-bus

![img-4.jpeg](img-4.jpeg)

Fig. 5. IEEE 14 bus system with single line outages.
![img-5.jpeg](img-5.jpeg)

Fig. 6. IEEE 14 bus System with Seven Line Outages.
system with single LOD and seven LODs, respectively. Fig. 5 shows the trend of a conventional EDA. It is shown that the population is converging towards the required solution after few generations. Each figure shows two graphs, where the stem graph depicts the line states (whether in outage or healthy) and the plot graph shows the probability distribution against each line status. The IEEE 14-bus system, with two, four and seven line outages, is considered, as shown in Figs. 5 and 6. During the early generations, the convergence rate is very fast, but after some generations, the convergence becomes slow. The identification process determines the actual number of lines in outage and also their respective position. Slowly and gradually the probability of the lines, in outage, moves towards ' 1 ' and the probability of other lines moves towards ' 0 '. Accordingly, the line status also changed either from ' 0 ' to ' 1 '
or from ' 1 ' to ' 0 '.
The similar trend is depicted in Figs. 7 and 8, where the simulation results for IEEE 39-bus system, with two and five line outages are shown. The trend remains the same, as in the case of IEEE 14-bus system, but in this case, as the number of lines are 46 , the number of generations to reach the sub-optimal solution is greater. Figs. 9 and 10 show the simulation results for IEEE 118-bus system, with a single and seven line outage. In this case, the total number of lines are 186. Therefore, EDA takes a little more generations to identify the lines in outages.

## 5. Conclusion

Line outages may cause a disaster in the smart grid systems. It has
![img-6.jpeg](img-6.jpeg)

Fig. 7. IEEE 39 bus system with two line outages.

![img-7.jpeg](img-7.jpeg)

Fig. 8. IEEE 39 bus system with five line outages.
![img-8.jpeg](img-8.jpeg)

Fig. 9. IEEE 118 bus system with single line outages.
![img-9.jpeg](img-9.jpeg)

Fig. 10. IEEE 118 bus system with seven line outages.
already been investigated in the literature that a single line outage may extend to double and further to multiple line outages. Therefore, it is required to detect and identify the lines in outage as soon as possible, in order to avoid complete or partial blackouts. In this paper, the behavior of Estimation of Distribution (EDA) algorithm is investigated to identify multiple line outages problem. The multiple line outage identification in the smart systems is taken as a case study. The actual behavior of the EDA is shown in the simulations, where the probability distributions are converging in favor of the objective function for the considered case. The proposed algorithm is also compared with some other state of the art algorithms, i.e. binary particle swarm optimization (BPSO) algorithm, adaptive BPSO and genetic algorithm (GA). The proposed EDA outperforms in terms of line outage detection performance and time consumption.
