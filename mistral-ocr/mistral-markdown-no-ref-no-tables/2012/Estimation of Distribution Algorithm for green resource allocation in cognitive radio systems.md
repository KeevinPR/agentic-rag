# Estimation of Distribution Algorithm for Green Resource Allocation in Cognitive Radio Systems 

Muhammad Naeem<br>Department of Electrical and<br>Computer Engineering<br>Ryerson University<br>Toronto, ON, Canada<br>mnaeem@rnet.ryerson.ca

Saeed Ashrafinia<br>School of Engineering Science<br>Simon Fraser University<br>Burnaby, BC, Canada<br>saa62@sfu.ca

Daniel Lee<br>School of Engineering Science<br>Simon Fraser University<br>Burnaby, BC, Canada<br>dchlee@sfu.ca

Abstract- In this paper, we formulate a resource allocation optimization problem for a cooperative relay-assisted cognitive radio system, comprising a single source node, multiple relays and multiple destinations. Our formulation takes into account the effects of the resource allocation on $\mathrm{CO}_{2}$ emission, and we refer to it as a green resource allocation problem. The green resource allocation problem is formulated as a non-linear multi-objective optimization problem. We modify the objective function by applying the weighted sum method, which results in a non-convex mixed integer non-linear programming problem. We propose a hybrid evolutionary scheme that utilizes an enhanced version of Estimation of Distributions Algorithm to solve this optimization problem. Simulation results demonstrate the efficiency of our evolutionary algorithm approach in comparison to other schemes such as GA and EDA.

Index Terms- green communications, cognitive radio, resource allocation, evolutionary algorithms, multi objective optimization

## I. INTRODUCTION

The information and communication technology (ICT) has become one of the $21^{\text {st }}$ century's biggest industries and accordingly will have a huge carbon foot print. According to the Smart 2020 report, the ICT industry will emit 1.4 Giga tons $\left(10^{9}\right)$ of carbon dioxide $\left(\mathrm{CO}_{2}\right)$ emissions, or $2.8 \%$ of global emissions by 2020 [1], [2] [3]. This sector is responsible for approximately five per cent of the global electricity demand and $\mathrm{CO}_{2}$ emission [6] [7].

The ICT industry alone is estimated to produce $\mathrm{CO}_{2}$ emission that is equivalent to the carbon output of the entire aviation industry [2]. ICT emissions grow fastest among sectors in society: doubling about every $4-6$ years [5]. Currently ICT represent $8-9.4 \%$ of total US electricity consumption, and $8 \%$ of the global electricity consumption, and it is projected to grow to as much as $20 \%$ of all electrical consumption in the US [5]. Future Broadband Internet alone is expected to consume $5 \%$ of all electricity.

In the last few years, there have been increasing efforts towards green ICT to minimize the $\mathrm{CO}_{2}$ emissions. A comprehensive survey on green networking is presented in [4]. In [6], authors presented the concept of energy efficiency in telecommunication networks. A detailed discussion about ICTs footprint and its impact on the environment is presented in [8]
[9] and [10]. In [11], authors described a variable power/bandwidth efficient modulation strategy to save the battery life of the communication device. Major IT companies like Google and Microsoft have already started working towards green ICTs [21] [22].

In the context of green communication, cooperative communication can contribute to reducing the $\mathrm{CO}_{2}$ emissions. Cooperative communication is a powerful concept for extending coverage and improving system's efficiency [23]. Green communications can utilize cooperative paradigms in order to reduce energy consumption for signal transmission [24]. In this paper, we present a multi-objective optimization framework that jointly solves the problem of spectrum sharing and reducing $\mathrm{CO}_{2}$ emissions. In particular, we propose a green multi-objective optimization framework for joint relay assignment and power allocation in a cooperative cognitive radio system (CRS). Then, we present evolutionary algorithms to solve the green multi-objective optimization.

The organization of this paper is as follows: In Section II we discuss the multi-objective aspect of the optimization problem. The system model is described in Section III. The proposed low-complex evolutionary scheme is presented in section IV. Section V contains the simulation results, and the conclusion is given in Section VI.

## II. Multi-Objective Optimization

Multi-objective optimization (MOO) is used in many complex engineering optimization problems [12] - [15]. In typical MOO problems, different objectives can conflict with each other. Optimization with respect to any particular objective can give unacceptable results with respect to other objectives [14]. For resource allocation in Green Cooperative Cognitive Radio Network (GCCRN), in this paper we consider two conflicting objectives: to maximize the sum-capacity and to minimize the $\mathrm{CO}_{2}$ emissions. Determining the optimal set of decision variables' values for a single objective $\left(\mathrm{CO}_{2}\right)$ emission minimization can result in a non-optimal solution with respect to other objectives, e.g. sum-capacity maximization.

Two widely used methods to solve multi-objective optimization, along with other methods, are the weighted sum method (WSM) and constraint objective methods [12] - [15]. In the WSM, a weighted sum of the multiple objective function is considered as the metric to minimize (maximize). In the

WSM, the weight of each objective is proportional to its importance placed for decision making. A general WSM multiobjective optimization problem is expressed as follows:
$\min f(x)=\sum_{i=1}^{Q} w_{i} f_{i}(x)$
subject to:
$g_{j}(x) \leq 0, j=1,2, \ldots, D$
$h_{j}(x)=0, j=1,2, \ldots, E$
where $Q$ is the number of objective functions, $D$ is the number of inequality constraints, $E$ is the number of equality constraints, and the weights are such that $\sum_{i=1}^{Q} w_{i}=1$. In the constraint objective method [14], each objective is transformed into a constraint. In our formulation, we will use the WSM.

In formulating the weighted sum MOO, we normalize each objective function $f_{j}(x)$ so that each one has the same range of values. The main reason for normalization is that the objective functions can have different dimensions (e.g., for the GCCRN problem, one is bits/Hz, and the other is power (Watts)), they become dimensionless after normalization, and this enables their addition in the weighted sum expression. Furthermore, in WSM for MOO [14], without normalization, one cannot specify the bias toward a particular objective with weights alone. For instance, if the value of one objective function is in the range of $[0,1]$, and the value of second objective is in the range $[0, \mathrm{x}]$ (where $1 \leq x \leq \infty$ ), then the second objective produces a bias in the weighted fitness function, even if we use equal weights $w_{1}=w_{2}=0.5$. In this work, all of the objective function values are normalized within the range close to $[0,1]$. In the case in which we do not have the exact maximal and minimal values of an individual objective function, we will normalize the objective function on the basis of its upper bound and lower bound. The GCCRN MOO is formulated so that the range of combined objective function is always within 0 and 1.

## III. GREEN RELAY ASSIGNMENT FOR GCCRN

We consider a two-hop wireless network with one transmitter (source), $K$ receivers or secondary users (SU), $L$ relays, and $M$ primary users (PUs). Each relay, transmitter, and receiver is equipped with a single antenna. We denote by $h_{s, l}$, the channel from the source to the $l^{\text {th }}$ relay, $h_{l, k}$ the channel from the $l^{\text {th }}$ relay to the $k^{\text {th }} \mathrm{SU}$, and $g_{l, m}$ the channel from the $l^{\text {th }}$ relay to the $m^{\text {th }} \mathrm{PU}$. We denote by $p_{l}$, the $l^{\text {th }}$ relay's transmission power. We consider a two-step amplify-andforward (AF) scheme [16]. We assumed in our cognitive radio network that data is received by each destination node on a separate frequency band and that each source-destination pair has been allocated equal bandwidth. We further assume that signals destined for different users do not interfere with one another. We also assume that each relay transmits its received signal at the same frequency band in which it received the signal. This models a low-cost relay that simply amplifies the signal and forwards it. We define $\varepsilon_{l, k}$ as a binary assignment indicator such that:

$$
\varepsilon_{l, k}= \begin{cases}1 & \text { if the } l^{\text {th }} \text { relay is assigned to the } k^{\text {th }} \text { receiver } \\ 0 & \text { otherwise }\end{cases}
$$

The channel capacity of the $k^{\text {th }}$ user for amplify and forward relaying is [16] [17]:
$C_{K}(\boldsymbol{\varepsilon}, \boldsymbol{p})=\frac{1}{2} \log \left[1+\frac{P_{c}^{K}}{N} \frac{\left(\sum_{l=1}^{L} \varepsilon_{l, k} \mid h_{s, l} h_{l, k}\left|\beta_{l} \sqrt{p_{l}}\right|^{2}\right.}{1+\sum_{l=1}^{L}\left(\beta_{l}\left|h_{l, k}\right| \sqrt{p_{l}}\right)^{2}}\right]$
where $\beta_{l}=\left(\sqrt{P_{c}^{k}\left|h_{s, l}\right|^{2}+N}\right)^{-1}, \boldsymbol{\varepsilon}=\left[\varepsilon_{l, k}\right]_{L \times K}$ is an $L \times K$ binary matrix indicating relay to secondary users connectivity, and $\boldsymbol{p}=\left[p_{l}\right]_{1 \times L}$ is an $L$-dimensional vector comprising $L$ relays' power levels. Our first objective is to maximize the sum-rate capacity $\sum_{k=1}^{K} C_{k}$. As mentioned in section II, the division of the sum-rate capacity with $\sum_{k=1}^{K} C_{k}^{\max }$ normalizes the first objective between 0 and 1 , where $C_{k}^{\max }$ is an upper bound on the capacity of the $k^{\text {th }}$ secondary user. The following upper bound can be obtained from Schwartz inequality:
$\log \left[1+\frac{P_{c}^{K}}{N} \frac{\left(\sum_{l=1}^{L}\left|h_{s, l} h_{l, k}\right| \beta_{l} \sqrt{p_{l}}\right]^{2}}{1+\sum_{l=1}^{L}\left(\beta_{l}\left|h_{l, k}\right| \sqrt{p_{l}}\right)^{2}}\right] \leq$
$\log \left[1+\frac{P_{c}^{K}}{N} \frac{\left(\sum_{l=1}^{L}\left(\left|h_{s, l}\right|\right)^{2}\right)\left(\sum_{l=1}^{L}\left(\left|h_{l, k}\right| \beta_{l}\right)^{2} p_{l}\right)}{1+\sum_{l=1}^{L}\left(\beta_{l}\left|h_{l, k}\right| \sqrt{p_{l}}\right)^{2}}\right] \triangleq C_{k}^{\max }$
Note that if the term $\left(\sum_{l=1}^{L}\left(\left|h_{l, k}\right| \beta_{l}\right)^{2} p_{l}^{\max }\right)$ is canceled out from the numerator and denominator of the latter expression, the resulted upper bound is even looser than the current $C_{k}^{\max }$. Thus the objective of the sum-rate capacity can be written as:

$$
\bar{f}_{c}(\boldsymbol{\varepsilon}, \boldsymbol{p})=\frac{\sum_{k=1}^{K} C_{k}(\boldsymbol{\varepsilon}, \boldsymbol{p})}{\sum_{k=1}^{K} C_{k}^{\max }}
$$

The second objective is to reduce the $\mathrm{CO}_{2}$ emissions. The $\mathrm{CO}_{2}$ emissions are measured in grams. If $P$ is the transmission power and $X$ is a constant in grams/KWh, then the product, $P X$, of $P$ and $X$ represents the $\mathrm{CO}_{2}$ emissions in grams/hour. The value of $X$ is different for different types of material (fuel) used in electricity generation. There are three major sources of fuel for electricity generation: oil, gas, and coal. The value of $X$ for lignite/brown coal, natural gas, crude oil and diesel oil is 940 , 370,640 , and 670 grams/KWh , respectively [6] - [8]. The $\mathrm{CO}_{2}$ emissions due to the $l^{\text {th }}$ relay would be $E_{l}^{\mathrm{CO}_{2}}\left(p_{l}\right)=X p_{l}$. Therefore, the objective of $\mathrm{CO}_{2}$ emissions can be written as:

$$
f_{\mathrm{CO}_{2}}(\boldsymbol{p})=\frac{\sum_{l=1}^{L} E_{l}^{\mathrm{CO}_{2}}(\boldsymbol{p})}{\sum_{l=1}^{L} E_{l \max }^{\mathrm{CO}_{2}}}
$$

where $E_{l \max }^{\mathrm{CO}_{2}}=\sum_{l=1}^{L} X p_{l}^{\max }$. To define a single objective, the maximization objective $\bar{f}_{c}$ is transformed into minimization using the relation $f_{c}=1-\bar{f}_{c}$. Mathematically, the MOO for GCCRN can be expressed as:
$O P 1: \min _{\boldsymbol{\varepsilon}, \boldsymbol{p}}\left\{w_{1} f_{c}(\boldsymbol{\varepsilon}, \boldsymbol{p})+w_{2} f_{\mathrm{CO}_{2}}(\boldsymbol{p})\right\}$ subject to
$C 1: \sum_{k=1}^{K} \varepsilon_{l, k} \leq 1, \forall l$
$C 2: \sum_{l=1}^{L} \varepsilon_{l, k} p_{l}\left|g_{l, m}\right|^{2} \leq l_{m}^{\max }, \quad \forall(m, k)$
$C 3: \quad 0 \leq p_{l} \leq \sum_{k=1}^{K} \varepsilon_{l, k} p_{l}^{\max }, \quad \forall l$
$C 4: \varepsilon_{l, k} \in\{0,1\}$

The formulation in (4) is a multi-objective non-convex mixed integer non-linear programming problem. The objective function in (4) is bounded by zero and one. In this equation, the constraint $C 1$ assures that a relay can only be assigned to one secondary user, $C 2$ is the interference constraint, the constraints $C 3$ and $C 4$ jointly ensure that if the $l^{\text {th }}$ relay is not assigned to any secondary user, then the transmission power of the $l^{\text {th }}$ relay should be zero. In the next section, we present a low-complexity hybrid Estimation-of-Distribution Algorithm (EDA) for GCCRN MOO problem.

## IV. HYBRID EDA FOR GCCRN MOO PROBLEM

In this section, we present a hybrid scheme for GCCRN multi-objective problem, as a combination of an evolutionary EDA for power allocation, plus an iterative greedy algorithm for relay assignment. Evolutionary Algorithms (EAs) in general have been often used to solve multi-objective optimization problems. EAs are inspired by the theory of biological evolution. Candidate solutions to a multi-objective optimization problem are represented as individuals in the population. In EAs, the objective function value of a candidate solution indicates the fitness of the individual, which is associated with the concept of natural selection [18]. Unlike other EAs such as the genetic algorithm, in EDA, the individuals are generated without the crossover and mutation operators. Instead, in EDA, a new population is generated based on a probability distribution, which is estimated from the best-selected individuals of the previous iterations [19]. In general, EDA is used for discrete optimization problems; however, we introduce EDA for continuous domain to allocate power to the relays. Table I illustrates the parameters and notations used in continuous EDA (CEDA).

TABLE I. PARAMETERS AND NOTATIONS OF CEDA


In CEDA, each individual can be designated by an $n$-dimensional real-valued vector. For GCCRN MOO problem, $n$ is equal to the number of relays $L$. In our CEDA implementation, each individual represents the relays transmission power. We denote by a row vector $\boldsymbol{P}=$ $\left[p_{1}, p_{2}, \ldots, p_{n}\right]$ as an individual where $p_{i}$ is the transmission power of the $l^{\text {th }}$ relay. The transmission power of the $l^{\text {th }}$ relay is bounded by $W_{L}$ and $H$, where $W_{L}$ and $W_{H}$ are the lower and the upper limit of an EDA search window. In each iteration, the CEDA maintains a population of individuals. The population is denoted by set $\Delta_{i}$. We denote by $\left|\Delta_{i}\right|$ the number of individuals
in the population. Population $\Delta_{i}$ can be specified by the following matrix:

$$
\Delta_{C E D A}=\left[\begin{array}{c}
\boldsymbol{P}^{1} \\
\boldsymbol{P}^{2} \\
\vdots \\
\boldsymbol{P}\left|\Delta_{i}\right|
\end{array}\right]=\left[\begin{array}{ccc}
p_{1}^{1} & \cdots & p_{n}^{1} \\
\vdots & \ddots & \vdots \\
p_{1}^{\left|\Delta_{i}\right|} & \cdots & p_{n}^{\left|\Delta_{i}\right|}
\end{array}\right]
$$

where superscript $j$ in the row vector $\boldsymbol{P}^{j}=\left[p_{1}^{j}, p_{2}^{j}, \ldots, p_{n}^{j}\right]$ indexes an individual in the population. A flow diagram of EDA algorithm is shown in Figure 1. The CEDA applied to the GCCRN MOO problem can be described in the following steps:

Step 0: Generate an initial population $\Delta_{0}$. Each element of matrix $\Delta_{\text {CEDA }}$ is obtained from the following formula:

$$
\begin{aligned}
p_{i}^{j}= & W_{L}+\left(W_{H}-W_{L}\right) \times \text { rand } \\
& \forall i=1,2, \ldots, n ; \forall j=1, \ldots,\left|\Delta_{i}\right|
\end{aligned}
$$

where $W_{L}=0, W_{H}=p_{i}^{\max }$ and " $r$ and" returns a uniform random number between 0 and 1 . For iterations $i=1,2, \ldots, G$, follow Steps 1 through 7:

Step 1: Evaluate the individuals in the current population $\Delta_{i-1}$ according to the fitness function $F$. Sort the candidate solutions (individuals in the current population) according to their fitness orders.

Step 2: In this step, the algorithm determines the assignment variable $\varepsilon=\left[\varepsilon_{1,1}, \varepsilon_{1,2}, \ldots, \varepsilon_{1, K}, \ldots, \varepsilon_{1, k}, \ldots, \varepsilon_{1, K}\right]$ for each individual heuristically. We propose an iterative relay assignment algorithm that generates a feasible $\varepsilon=$ $\left[\varepsilon_{1,1}, \varepsilon_{1,2}, \ldots, \varepsilon_{1, K}, \ldots, \varepsilon_{1, k}, \ldots, \varepsilon_{1, K}\right]$ and repairs each individual such that constraints C 2 and C 3 are satisfied. The algorithm is described in section IV.B. At the end of this step, the algorithm has a population comprises of individuals with feasible relays' power levels and the associated assignment variables $\varepsilon=$ $\left[\varepsilon_{1,1}, \varepsilon_{1,2}, \ldots, \varepsilon_{1, K}, \ldots, \varepsilon_{1, k}, \ldots, \varepsilon_{1, K}\right]$.

Step 3: In this step, the algorithm evaluates the cost function to determine the fitness values for each individual in the population, and the individuals are sorted according to their fitness values. If the convergence criteria (e.g. number of iterations) is satisfied, then the algorithm terminates; otherwise, continue to step 4.

Step 4: Select the best $p_{\text {set }}\left|\Delta_{i-1}\right|=\left|\eta_{i-1}\right|$ candidate solutions (individuals) from the current population $\Delta_{i-1}$. This selected population is used to compute the mean and standard deviation.

Step 5: Determine the mean $m$ and standard deviation $\sigma$. Based on the estimations of $m$ and $\sigma$, update the search window bounds $W_{L}$ and $W_{H}$ to $W_{L}=m-\sigma$ and $W_{H}=m+\sigma$.

Step 6: Generate new $\left|\Delta_{i}\right|-\left|\eta_{i-1}\right|$ individuals on the basis of this new estimated $W_{L}$ and $W_{H}$ using (6). Combine these $\left|\Delta_{i}\right|-\left|\eta_{i-1}\right|$ newly generated individuals with members of $\eta_{i-1}$ to form a new population $\Delta_{i}$.

Step 7: Go to step one and repeat the steps.
The simulation results demonstrate good performance for CEDA with the simple procedure described above. In addition, we were able to modify this basic EDA algorithm and improve the algorithm's performance even further. The modification includes the introduction of thresholds in CEDA to avoid premature convergence. We call this algorithm the Modified EDA (MEDA), which is described in the next section.

## A. Modified EDA

During the execution of CEDA, the difference between the search window bounds $W_{L}$ and $W_{H}$ may diminishes as the iterations proceeds. This may cause the CEDA to stocked in a search space and result in a premature convergence. The premature convergence may occur if the difference between $W_{L}$ and $W_{H}$ diminishes to an extremely small value. In that case, during the rest of iteration, the algorithm will generate nearly same power levels. We suggest restoring the $W_{L}$ and $W_{H}$ to their initial values $W_{L}=0$ and $W_{H}=p_{l}^{\max }, l=1,2, \ldots, l$ when the difference between $W_{L}$ and $W_{H}$ is less than a pre-specified threshold $\gamma$, i.e.:
if $W_{L}-W_{H} \leq \gamma$

$$
\begin{aligned}
& W_{L}=0 \\
& W_{H}=p_{l}^{\max }
\end{aligned}
$$

end if
In Section V we present some experimental results, which show the effect of threshold on the performance of EDA. In the next subsection, we describe the iterative greedy algorithm for relay assignment.

## B. Iterative Greedy Algorithm

In this section, we present an Iterative Greedy Algorithm to repair each EA individual such that constraints $C 2$ and $C 3$ are satisfied, and also to generate a feasible assignment variable $\boldsymbol{\varepsilon}$ for each individual heuristically that satisfies all constraints in (4). At the end of this procedure, the algorithm's output is an individual with feasible relays' power levels and the associated assignment variables $\boldsymbol{\varepsilon}$, which it is ready to be passed on to the fitness function evaluation process. This procedure has to be run for $N$ times (number of individuals in the EA's population) to determine the relay assignment variable and ensure that all individuals satisfy the constraints.

Table II shows the pseudo-code of the iterative greedy algorithm. The algorithm runs the procedure in Table II for every individual $\boldsymbol{P}^{j}$ of the population in every EA iteration. This algorithm consists of two steps. In the first step, the algorithm greedily assigns relays to the secondary users based on the channel conditions. However, the assigned relays in this step may not satisfy all the constraints. In the second step, the algorithm verifies the assigned relays with the constraints and finalizes the power allocation to ensure that the interference constraint at the PUs is satisfied.

## 1) Step 1: Partial Relay Assignment

For describing the basic idea behind the proposed suboptimal algorithm, we view $\left|h_{\varepsilon, l}\right|^{2}\left|h_{l, k}\right|^{2}$ (the product of the channel gain from the source to the $l^{\text {th }}$ relay and the channel gain from the $l^{\text {th }}$ relay to the $k^{\text {th }}$ secondary user) as the profit from investing (assigning) the $l^{\text {th }}$ relay to the $k^{\text {th }}$ secondary user (because of the channel gain's positive effect on the throughput). Step 1 of the algorithm temporarily assigns each relay to the secondary users that return the maximum profit. Note that according to $C 1$ in problem (4), each relay can be assigned only to one secondary user. Mathematically, for each relay $l$, the algorithm temporarily assigns secondary users as follows:

$$
\begin{aligned}
S(l) & =\arg \max _{k=1, \ldots, K}\left|h_{\varepsilon, l}\right|^{2}\left|h_{l, k}\right|^{2} \\
& =\arg \max _{k=1, \ldots, K}\left|h_{l, k}\right|^{2}
\end{aligned}
$$

where $S$ is an $L$-dimensional vector that stores this temporary assignment. At the end of Step 1, every relay is assigned to one secondary user. However, the relay powers, along with the temporarily relay assignment variables from (7), still need to satisfy the interference constraint at the PUs. In Step 2 of the algorithm, based on temporary relay assignment in Step 1, the algorithm performs a joint relay assignment and power allocation such that the constraints are satisfied at all PUs.

TABLE II. ITERATIVE GREEDY RELAY ASSEGMENT FOR EACH EA INDIVIDUAL

## Initialization:

1. $S(l)=0, \forall l$,
2. $C(k)=0, \forall k$,

## Step 1:

3. for $l=1, \ldots, L$,
4. $S(l)=\arg \max _{k=1, \ldots, K}\left|h_{l, k}\right|^{2}$,
5. end for,

## Step 2:

6. for $l=1, \ldots, L$
7. $p_{l}^{j}=\min \left\{\frac{\left|l^{\max }\right|}{\left|g_{l, 1}\right|^{2}}, \ldots, \frac{\left|l^{\max }\right|}{\left|g_{l, M}\right|^{2}}, p_{l}^{j}\right\}, \forall l$ (power of the $l^{\text {th }}$ relay of the $j^{\text {th }}$ individual),
8. end for,
9. for $k=1, \ldots, K$
10. $\mathcal{L}_{k}=\{l \mid S(l)=k\}$
11. if $\mathcal{L}_{k} \neq \emptyset$ then,
12. $f l g=0$,
13. while $f l g=0$,
14. if $\{$ constraint $C 2$ is not satisfied with $\mathcal{L}_{k}\}$ then,
15. $\tilde{l} \leftarrow$ find the relay that causes the highest interference,
16. $\mathcal{L}_{k}=\mathcal{L}_{k} \backslash\{\tilde{l}\}$,
17. else
18. $f l g=1$,
19. $C(k) \leftarrow$ calculate the capacity from equation (1) using $\mathcal{L}_{k}$,
20. end if,
21. end while
22. end if,
23. end for,

2) Step 2: Final Relay Assignment / Interference Constraint

In the second step, the algorithm performs a final assignment to ensure that the interference constraints at the PUs are all satisfied. Note that the relays' power levels randomly generated by the EA can violate the constraint of the limited interference to the PUs, which is to be taken care of by Step 2 of the iterative greedy algorithm.

At the beginning of the second step, the algorithm repairs the power of any relay that violates the interference constraint. For this purpose, first it examines whether the transmission power of each relay $l$ violates any interference constraint. We denote by $p_{l}^{I}$ the power of the $l^{\text {th }}$ relay in the $j^{\text {th }}$ individual of the population. If $p_{l}^{I}$ violates any of the interference constraint, then the algorithm performs the following adjustment: Note that the relays' power levels randomly generated by the EDA algorithm can violate the constraint of the limited interference to the primary users. At the start of the second step, the algorithm starts repairing the relays' power levels if they violate an interference constraint. First, the algorithm examines each relay $l$ whether its transmission power would violate any interference constraint even if all other relays' power levels were set to zero. We denote by $p_{l}^{I}$ the power of the $l^{\text {th }}$ relay in the $j^{\text {th }}$ individual of the population. If $p_{l}^{I}$ violates any of the interference constraint $I_{m}^{\max }$, even under the assumption that other relays' transmission power levels are all set to 0 , then the algorithm first makes the following adjustment:

$$
p_{l}^{I}=\min \left\{\frac{I_{1}^{\max }}{\left\|g_{l, 1}\right\|^{2}}, \frac{I_{2}^{\max }}{\left\|g_{l, 2}\right\|^{2}}, \ldots, \frac{I_{M}^{\max }}{\left\|g_{l, M}\right\|^{2}}, p_{l}^{I}\right\}, \quad \forall l
$$

The algorithm then continues to iterate over all of the secondary users to complete the final assignment of the relays. During every iteration over secondary users, the algorithm collects the set of relays that has been temporarily assigned to the $k^{\text {th }}$ secondary user during Step 1 in the variable $\mathcal{L}_{k}$. Then it checks whether the relays in the set $\mathcal{L}_{k}$ satisfy the interference constraint. If the relays set $\mathcal{L}_{k}$ violate the interference constraint at any PU, the algorithm greedily removes the relay from the set $\mathcal{L}_{k}$ that causes the maximum interference to the PUs. This removal process continues until $\mathcal{L}_{k}$ satisfies the interference constraint. The whole algorithm in Step 2 then continues to run until relays are assigned to all secondary users.

## V. SIMULATION RESULTS

In this section we present the simulation results of EAs applied to a GCCRN MOO problem. In all simulations, the channel gains between source, relays and destinations have been generated from independent complex Gaussian distribution. Each result is an average of two thousand independent simulation runs. We compare the results of Hybrid EDA and MEDA with the standard continuous genetic algorithm [20]. Table III describes the notations used in the simulation results. Figures 1, 2 and 3 present the trade-off plots of sum-capacity and power. The trade-off is calculated between the green communication and without green communication. Trade-off is presented as percentage decrease in sum-capacity (DSC) and percentage decrease in power consumption (DP). To get the result without green communication, we set $w_{1}=1$ and $w_{2}=0$. Figures 1 and 2 show the effect of green communication, by changing the values of weights $w_{1}$ and $w_{2}$.

The results show that when $w_{2}$ is more than $w_{1}$ there is more reduction in $\mathrm{CO}_{2}$ emissions (percentage decrease in power). This reduction comes at the cost of throughput drop. From the results, we can observe that $\mathrm{CO}_{2}$ emissions will decrease by $50 \%$ to $70 \%$ at the cost of $10 \%$ to $30 \%$ loss of throughput when $w_{2} \geq w_{1}$. The different weights settings are suitable for different geographical conditions and regulatory policies. The results also show EDA outperforms GA. Fig. 3 illustrates the trade-off plots of sum-capacity and power for different $L, K$ and $I_{m}^{\max }$, and it shows that there is less decrease in power at $I_{m}^{\max }=$ $10 \mathrm{~m} W$ as compared with $1 W$, and is due to the fact that lower interference threshold makes the CR as a green communication device and there is no room for further improvement.

Figures 4 and 5 present the iterations vs. fitness for different number of relays and users for $\left(M, p_{l}^{\max }, I_{m}^{\max }, w 1, w 2\right)$ $=\left(1,10 \mathrm{~W}, 10 \mathrm{~mW}, 0.5,0.5\right)$ and $\left(1,10 \mathrm{~W}, 1 \mathrm{~W}, 0.5,0.5\right)$. These figures demonstrate that performance of MEDA is better than EDA and GA. A simple EDA and GA can get stuck in local optimum after few iterations. Also note that the fitness values with large relays and less number of users (e.g., $L=20, K=10$ ) is better than fitness values with less relays and large number of users (e.g., $L=10, K=20$ ). The reason is with a large number of relays and less number of secondary users there is more freedom in assigning the relays to the secondary users.

Figures 6 presents the comparison performance results between EDA, MEDA and GA on each objective function for $\left(M, p_{l}^{\max }, I_{m}^{\max }, K, w_{1}, w_{2}\right)=\left(1,10 \mathrm{~W}, 10 \mathrm{~mW}, 10,0.5,0.5\right)$. The results show performance of both EDA and MEDA outperform GA on the fitness function and the two objective functions.

TABLE III. Abbreviations used in SIMULATION RESULTS


![img-0.jpeg](img-0.jpeg)

Fig. 1. Power and sum-capacity trade-off plot with $K=10, L=10, I_{m}^{\max }=$ $10 W$

![img-5.jpeg](img-5.jpeg)

Fig. 2. Power and sum-capacity trade-off plot with $K=20, L=10, I_{\mathrm{m}}^{\max }=$ 10 W
![img-5.jpeg](img-5.jpeg)

Fig. 3. Power and sum-capacity trade-off plot with $\left(K, L, I_{\mathrm{m}}^{\max }\right)=$ $(10 / 20,10 / 20,10 \mathrm{~mW} / 1 \mathrm{~mW})$
![img-5.jpeg](img-5.jpeg)

Fig. 4. Iterations vs. Fitness plot for different ( $L, K)$ configuration. The parameters are $\left(\mathrm{M}, p_{1}^{\max }, I_{\mathrm{m}}^{\max }, w_{1}, w_{2}\right)=(1,10 \mathrm{~W}, 10 \mathrm{~mW}, 0.5,0.5)$
![img-5.jpeg](img-5.jpeg)

Fig. 5. Iterations vs. Fitness plot for different $(L, K)$ configuration. The parameters are $\left(\mathrm{M}, p_{1}^{\max }, I_{\mathrm{m}}^{\max }, w_{1}, w_{2}\right)=(1,10 \mathrm{~W}, 1 \mathrm{~W}, 0.5,0.5)$
![img-5.jpeg](img-5.jpeg)

Fig. 6. Iterations vs. Fitness plot for different number of relays. The parameters are $\left(\mathrm{M}, p_{1}^{\max }, I_{\mathrm{m}}^{\max }, \mathrm{K}, w_{1}, w_{2}\right)=(1,10 \mathrm{~W}, 1 \mathrm{~W}, 20,0.50 .5)$

## VI. CONCLUSION

In this paper, we presented a multi-objective framework for green resource allocation in the multiuser cognitive radio network. We present the constrained optimization formulation of the relay assisted cognitive radio system. Our formulation includes effect transmission power on $\mathrm{CO}_{2}$ emission and is a multi-objective optimization in nature. We approached this problem by applying the weighted sum method, which results in a non-convex mixed integer non-linear programming problem. We proposed a hybrid continuous evolutionary scheme comprising an enhanced version of EDA and a greedy algorithm to solve this optimization problem. The results demonstrate that in all combinations of system parameters and weight values the proposed algorithm outperforms other wellknown evolutionary algorithms. The simple underlying concept and ease of implementation of our proposed algorithm make it a suitable candidate for green resource allocation.

This paper presented a simple optimization problem that takes into account the effects of communication resource allocation on the environment. We believe that the more system optimization models that take into account the system's effect on the environment will be developed and enhanced. The results of this paper indicate that our evolutionary algorithms proposed in this paper may be useful for various optimization problems for green communication.

## ACKNOWLEDGMENT

This work was supported in part by a Discovery Grant from the National Science and Engineering Research Council (NSERC) of Canada.
