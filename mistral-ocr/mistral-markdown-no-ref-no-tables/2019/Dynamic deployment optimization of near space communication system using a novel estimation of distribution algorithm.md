# Dynamic deployment optimization of near space communication system using a novel estimation of distribution algorithm 

Zhao Wang, Maoguo Gong *<br>Key Laboratory of Intelligent Perception and Image Understanding of Ministry of Education, International Research Center for Intelligent Perception and Computation, Xidian University, No. 2 South TaiBaiRoad, Xi'an 710071, China

## H I G H L I G H T S

- The conflict between selection mechanism and domination relationship is analyzed.
- The latest local information is included in a local incremental distribution model.
- A novel asymmetrical domination relationship is proposed to select robust solutions.
- Exploration and exploitation are balanced by tuning model compensation factors.


## ARTICLE INFO

Article history:
Received 17 June 2018
Received in revised form 21 February 2019
Accepted 27 February 2019
Available online 6 March 2019

Keywords:
Near space communication system
Estimation of distribution algorithm
Multiobjective optimization
Domination relationship

## A B S T R A C T

A robust deployment of the airship platforms is crucial to the performance of the Near Space Communication System (NSCS) in the dynamic environment. In this paper, a multiobjective NSCS deployment optimization model with multi-phased periodic user distribution is proposed. To optimize this model, we propose a local incremental estimation of distribution algorithm with an asymmetrical domination relationship within the multiobjective evolutionary algorithm based on decomposition framework. The conflict between the selection mechanism and the domination relationship is also analyzed theoretically for the first time. To obtain robust solutions under this conflict, the local distribution information of a certain subproblem within several generations is encompassed into a local incremental distribution model. As a generalized form of the existing domination relationship, an asymmetrical domination relationship (ADR), which treats the current and past objective values differently, is proposed to select robust solutions. The proposed algorithm is also tested on four designed problems compared with another four popular algorithms and proves its superiority. Some important parameters are also investigated in the experiments and some guidelines on tuning these parameters are given as well.
(c) 2019 Elsevier B.V. All rights reserved.

## 1. Introduction

The near space [1] has been widely exploited in many domains like earth observation [2], synthetic aperture radar [3,4], environment evaluation [5] and communication system [6,7]. Among these applications, the near space communication system (NSCS) attracts much attention. The deployment of the aircraft platforms is crucial in maximizing the performance of the NSCS [8]. Some studies have been carried out to optimize the NSCS deployment by considering its energy consumption [9,10], covered users [11], minimum delay [12], detection performances [13], network speed [14] and routing efficiency [8]. However, all the researches so far treat the deployment optimization as a static

[^0]problem. From the practical point of view, the users change their locations with an implicit manner [15] which includes two common phenomena. First, the change of the user distribution occurs in a relatively small time interval. The user distribution stays unchanged between two consecutive changes. Second, the change of the user distribution is periodic. Each period consists of several phases in each of which the user distribution follows a specific probability distribution model. An example is shown in Fig. 1. Besides, there could be more than two phases and the length of each period could be adjusted as required. From the analysis above, it can be concluded that the optimal solutions for different periods are similar but not the same. Thus, establishing the distribution model of the related solution set over a period of time is necessary to obtain robust solutions in the dynamic environment.


[^0]:    * Corresponding author.

    E-mail address: gong@ieee.org (M. Gong).

![img-0.jpeg](img-0.jpeg)

Fig. 1. Dynamic user distribution model.

In recent years, the evolutionary algorithm emerges as an effective method to solve complex real-world optimization problems [16]. The evolutionary algorithms have many advantages over traditional methods especially in dealing with the multiobjective optimization problems (MOP) [17]. In the optimization process, the variable distribution of the population determines how the population involves. To investigate and utilize the population distribution information, the estimation of distribution algorithm (EDA) is proposed and studied [18-21]. The basic idea of the EDA is to estimate the probability distribution model of the decision variables over a given solution set. With the capability of global estimation and variable linkage learning [22-24], the estimation of distribution algorithms have proven to perform well on many complex MOPs.

In this paper, we optimize the deployment of the NSCS as a maximization multiobjective optimization problem (MOP) regarding two conflicting representative performance indicators: the network speed and the coverage under the periodically changing user distribution. According to [8,25,26], this MOP is NP-hard. To solve this problem, we propose a local incremental estimation of distribution algorithm with an asymmetrical domination relationship (LI-EDA-ADR) within the multiobjective evolutionary algorithm based on decomposition (MOEA/D) framework [27]. The motivation and idea of this paper are two-fold. First, we notice that the conflict between the selection mechanism and domination relationship will cause the loss of population diversity which in turn deteriorates the completeness of the approximated Pareto front. To address this conflict, a local incremental distribution model (LIDM) is proposed to estimate the distribution of the neighboring solutions within a period of time. Second, it is difficult to evaluate a certain solution under the changing environment to select robust solutions. Thus, we propose an asymmetrical domination relationship (ADR) to expand the traditional domination relationship to dynamic environment. The ADR does not barricade the selection of the new solutions but helps distinguish the true inferior solutions in the external population (EP). Third, a compensation mechanism is introduced so that the LIDM is irreducible and ergodic [28]. The major contributions of this paper are concluded below.

- To our knowledge, the conflict between the selection mechanism and the traditional domination relationship is analyzed theoretically for the first time and a local incremental distribution model is proposed to address this conflict.
- An asymmetrical domination relationship is proposed to extend the traditional domination relationship to the dynamic domain.
- A dynamic NSCS deployment optimization model is proposed for the first time and solved using the LI-EDA-ADR.

This paper is organized as follows. In Section 2, we first describe the concept of the NSCS and its deployment optimization. And then we present the major development of the EDA and
conclude its advantages and disadvantages. The proposed LI-EDAADR is presented in Section 4. The experiments and analysis are carried out in Section 5. The conclusion and future work come at last in Section 6.

## 2. Background

### 2.1. Near space communication system and its deployment optimization

Compared with the other communication systems, the NSCS has many advantages such as low cost, easy maintenance, high network speed and low price [1,29,30]. An NSCS works as Fig. 2 shows. The users on the ground can connect to the airships using their mobile devices or through a special antenna. Considering the two phenomena mentioned in Section 1, the NSCS should provide a fast network speed while covering as large area as possible. These two representative objectives usually conflict with each other, and the effect of other performance indicators can be categorized into either of these two objectives. To optimize these two objectives with the dynamic users, the airships should adjust their positions to track the environment change, i.e., the user distribution change. However, due to the limited mobility of the airships, it can barely achieve the best position for each phase. Thus, a set of robust Pareto optimal solutions that maximize the overall performance of all the phases is required.

Many studies on the deployment optimization of the near space platforms are carried out in recent years. In [12], Wang et al. constructed a preliminary NSCS model and optimized the development with a modified genetic algorithm. In [13], the authors proposed a genetic algorithm with adaptive crossover and mutation to optimize the deployment of the NSCS. The deployment of the NSCS is also optimized as an MOP in [14]. In this paper, a comprehensive NSCS model with two conflict objectives is proposed for the first time. An MOEA/D with a local search strategy is proposed to solve this problem. In [8], a similaritybased MOEA/D is proposed to solve the deployment optimization problem of the NSCS. In this paper, the authors achieve the airship redeployment among different regions while an elaborate local search is performed inside each implicit region. However, all the studies so far focus only on the static user distribution, while the ever changing user distribution has not been considered yet.

### 2.2. Estimation of distribution algorithm

In discrete optimization domain, the univariate marginal distribution algorithm [31,32] maintains an independent univariate model for the discrete variables and the offspring are generated with their corresponding probabilities. In continuous optimization domain [33,34], an adaptive discretization method is proposed in [35]. If the number of the search points within a certain interval exceeds a threshold, this method splits this interval randomly. In [20], the Gaussian and the Cauchy distribution are

![img-1.jpeg](img-1.jpeg)

Fig. 2. Near space communication system.
mixed and estimated to preserve the diversity. Other Gaussianbased models can be found in [36,37]. In [38], highly related jobs are combined based on a bi-variate model. With the blocks as the new manipulated genes, the complexity of the schedule optimization problem is reduced. To handle MOPs, Zhang et al. studied the regularity property of the MOPs and proposed a regularity-based multiobjective EDA which combines the approxmated Pareto set and a noise vector into one model. Another multiobjective EDA is proposed in [39] in which a cheap and an expensive local search methods are introduced into the EDA. For dynamic cases, there are two popular strategies to deal with the environment change. The first one is to maintain the population diversity of the estimated model [40,41]. The second one is to maintain an external population which is inserted into the main population when the environment change is detected [42,43]. However, these two strategies are faced with the challenges of high computation cost and the difficulty of selecting a suitable model respectively.

## 3. Near space communication system modeling in dynamic environment

### 3.1. Dynamic user modeling

Due to the complexity of the dynamic user, two major characteristics of the user change that are worth notice are described in Section 2.1 and shown in Fig. 1. Assume the probability distribution in phase $i$ is $P_{i}(x, y), i=1, \ldots, I$ and $(x, y)$ is the user coordinate, the transition between various phases can be considered as a Markov chain of which the transition probability matrix is $T$. Consider the change period, the user distribution $U_{t}$ at iteration $t$ can be described as follows:

$$
\begin{aligned}
U_{t}= & \left(u_{t}^{i_{1}}, \ldots, u_{t}^{i_{t}}\right)(1-\operatorname{sgn}(t \bmod N)) \\
& +\left(u_{t-1}^{i_{1}}, \ldots, u_{t-1}^{i_{t}}\right) \operatorname{sgn}(t \bmod N) \\
\operatorname{sgn}(x)= & \left\{\begin{array}{ll}
1, & x \neq 0 \\
0, & \text { otherwise }
\end{array}\right. \\
u_{t}^{i_{k}} \sim P_{i_{k}}(x, y)
\end{aligned}
$$

where $u_{t}^{i_{k}}$ is the user distribution. $N$ is the interval between two changes. Given the initial user probability distribution $P_{i_{0}}(x, y)$ at the very beginning, the probability $P_{i}^{j}\left(i_{k}\right)$ that $P_{i_{k}}(x, y)$ is chosen as
the probability distribution of phase $j$ at iteration $t$ is calculated as follows:
$P_{i}^{j}\left(i_{k}\right)=\left[T^{\left|\frac{i-i i}{N}\right| \cdot i} \cdot T^{j}\right]_{i_{0} \cdot i_{k}}$
In this paper, the transition probability between any two consecutive statuses is set as 1 .

### 3.2. Near space communication system modeling

From the practical point of view, the aim of the deployment optimization is to maximize the performance with limited airship resource [11]. According to the analysis in Section 2.1, to provide fast connection, the airships should be deployed around the hotspots so that the network capacity can be most utilized. To cover large area, the airships should be evenly deployed. In this paper, we focus on a limited area and the deployment optimization of a large network can be achieved by integrating the proposed LI-EDA-ADR into a distributed continuous-time multiagent system [44]. The aim of this paper is to provide a set of robust Pareto optimal solutions for the decision maker to choose from. By applying the proposed LI-EDA-ADR, a complete set consisting of trade-off robust solutions optimizing these two objectives is provided. However, not all of the obtained Pareto optimal solutions are preferred by the decision maker. Some popular methods of selecting preferred solutions can be found in [45].

### 3.2.1. The first objective

High network speed relies heavily on stable and high transmission rate. The transmission rate is affected by many factors like power supply, whether condition, processing capability and so on. Among all these factors, the power supply and processing capability are highly related with the transmission performance [46]. The transmission distance and process capability are the radical controllable factors. With the increase of the transmission distance, a better power supply is required. And higher process capability can serve more users with smaller delay. Thus, for general purposes, the transmission rate can be simulated by the Friis equation [47,48] considering the power supply, transmission distance and process capability:
$P_{r}=P_{t} G_{t} G_{r}\left(\frac{\lambda_{c}}{4 \pi d}\right)^{2}$
where $P_{t}$ is the signal power received by the users. $P_{t}$ is the original signal power. $\lambda_{c}$ is the wavelength. $G_{t}$ is the antenna transmission gain. $G_{r}$ is the antenna receiving gain. $d$ is the

transmission distance. To gain high network speed, the users could connect to multiple airships [29]. From the user experience's point of view, the network speed obtained by a user can be simulated as follows. In this paper, we refer to the overall network resource that a user obtains as the network capacity. Given $N$ users on the ground, $M$ airships and $L$ phases in each period, the positions of user $i$ and airship $j$ in phase $l$ are $U P_{0}=$ $\left(x_{0}^{U}, y_{0}^{U}, 0\right)$ and $A P_{0}=\left(x_{0}^{A}, y_{0}^{A}, z_{0}^{A}\right)$, respectively. The maximum transmission distance between a user and an airship is $D T$. The maximum network capacity of each airship is $C M$.

The network capacity $U C_{0}$ obtained by user $i$ in phase $l$ is calculated as follows:
$U C_{0}=\sum_{j=1}^{M} S C_{0 j} \cdot C S_{0 j} \cdot\left(1-F D \cdot D A_{0 j}\right)^{2}$
where $F D$ is the transmission factor. $D A_{0 j}$ is the transmission distance between user $i$ and airship $j$ in phase $l$ :
$D A_{0 j}=\sqrt{\left(x_{0}^{U}-x_{0}^{A}\right)^{2}+\left(y_{0}^{U}-y_{0}^{A}\right)^{2}+\left(z_{0}^{A}\right)^{2}}$
$S C_{0 j}$ is the sign function:
$S C_{0 j}= \begin{cases}1, & D A_{0 j} \leq D T \\ 0, & \text { otherwise }\end{cases}$
An airship assigns equal network capacity $C S_{0}$ to each user that connects to it:
$C S_{0}=\frac{C M}{\sum_{i=1}^{N} S C_{0 j}}$
By optimizing the airship positions in all the phases: $A P_{0}=$ $\left(x_{0}^{A}, y_{0}^{A}, z_{0}^{A}\right), j \in\{1, \ldots, M\}$, the first objective is the total capacity $C A$ obtained by all the users in one period, which is shown as:
$C A=\sum_{i=1}^{L} \sum_{i=1}^{N} U C_{0}$

### 3.2.2. The second objective

By optimizing the airship positions in all the phases: $A P_{0}=$ $\left(x_{0}^{A}, y_{0}^{A}, z_{0}^{A}\right), j \in\{1, \ldots, M\}$, the second objective is the total coverage of the NSCS in an entire period. Assume that the coverage in phase $l$ is $S_{l}$, and then the second objective $S T$ is calculated as follows:
$S T=\sum_{l=1}^{L} S_{l}$

### 3.2.3. Airship mobility

Due to the limited power supply, the airships adjust their positions by ascending or descending to different atmosphere layers to utilize the airflow of different directions. This limits the mobility of the airships and thus, the airships are able to move for a limited distance within a certain period of time. This constraint is described for airship $j$ as follows:

$$
\left\{\begin{array}{l}
D C_{l_{1} l_{2} j} \leq D M \\
\left|I_{1}-I_{2}\right|=1 I_{1}, I_{2}=1, \ldots, L
\end{array}\right.
$$

where $D C_{l_{1} l_{2} j}$ is the distance between the positions of airship $j$ in phase $I_{1}$ and $I_{2}$. DM is the maximum mobility distance. For the solutions that do not satisfy Eq. (12), a phase at which an airship is too far from its position in the next phase is randomly selected, and the position of this airship at this phase is adjusted toward its position in the next phase till the mobility constraint is satisfied for these two phases. This process starts at the earliest phase and repeats until Eq. (12) is fully satisfied for all the phases.

Based on the above analysis, the deployment optimization of the NSCS in the dynamic environment is a dynamic multiobjective optimization problem as follows:
$\left\{\begin{array}{l}\text { maximize } C A \\ \text { maximize } S T \\ \text { subject to (12) }\end{array}\right.$

## 4. Local incremental estimation of distribution algorithm with asymmetrical domination relationship

The MOEA/D has proven to be effective in solving complex MOPs. The success of the MOEA/D comes from the fact that it decomposes the original difficult MOP into a set of simple subproblems [49].

Considering the solution distribution in the evolutionary process, three issues are discussed in [8]. First, two solutions with similar objective values may have quite different solution structures which implicitly represent their own perceptions of the search space. Second, there exists common latent regions in the decision variable space by comparing any two neighboring solutions. Third, these two phenomena above also exist in the optimization process of many other MOPs and can be utilized in improving the algorithm effectiveness. Considering the MOP described in Eq. (13), the changing users make the common perception between two neighboring solutions more uncertain. In addition, with multiple evaluations in the changing environment, solutions that have both similar objective values and different variable distributions can be selected by a certain subproblem within several iterations. This leads to an incomplete exploration of the search space. Thus, considering the utilization of the neighboring subproblems and dramatically changing variable distribution, an estimated distribution model is proposed and discussed below.

### 4.1. Local incremental distribution model

The local incremental distribution model is proposed based on three factors.

### 4.1.1. The first factor

Many decomposition approaches are discussed in [50]. The selection mechanism based on the decomposed objective value decides whether a parent should be replaced by its offspring. At the meantime, a complete Pareto front and fast convergence are desired [51]. The conflict between the decomposition based selection mechanism and Pareto optimality usually deteriorates the selection pressure in the early stage and the population diversity in the late stage of the iteration. A deep survey on the population diversity and niching methods can be found in [52] in which the dynamic case is addressed particularly. Before investigating some popular decomposition approaches, an important theorem is provided.

Theorem 1. With a greedy selection mechanism, the feasible hypercube of a new replacing solutions is a subset of that of the replaced solution.

Proof. Consider a minimization decomposition function $F_{d}\left(F_{1}\right)$ and two solutions to a certain subproblem: $F_{1}$ and $F_{2}$. Assume $F_{2}$ is able to replace $F_{1}$, which means:
$F_{d}\left(F_{1}\right)>F_{d}\left(F_{2}\right)$
Consider the feasible hypercubes defined by $F_{1}$ and $F_{2}$ are $H_{1}$ and $H_{2}$, respectively and assume $\exists F_{3} \in H_{2} \backslash H_{1}$, and thus we have:
$F_{d}\left(F_{1}\right)<F_{d}\left(F_{3}\right)$
$F_{d}\left(F_{2}\right) \geqslant F_{d}\left(F_{3}\right)$

From Eqs. (15) and (16), we have:
$F_{d}\left(F_{1}\right)<F_{d}\left(F_{2}\right)$
which contradicts Eq. (14). The proof is completed.
Given a reference point $Z=\left(z_{1}, \ldots, z_{N}\right)$, the current and its equivalent solution to a certain subproblem are $F_{1}=\left(f_{11}, \ldots, f_{1 N}\right)$ and $F_{2}=\left(f_{21}, \ldots, f_{2 N}\right)$, respectively and $N$ is the number of objectives. The projection of $F_{2}$ on vector $\overrightarrow{F_{1} Z}$ is $F_{3}=\left(f_{31}, \ldots, f_{3 N}\right)$. The PBI decomposition with penalty factor $\theta$ can be described as follows:
$\theta\left|\overrightarrow{F_{2} F_{3}}\right|+\left|\overrightarrow{F_{3} Z}\right|=\left|\overrightarrow{F_{1} Z}\right|$
Then the angle between $\overrightarrow{F_{1} Z}$ and $\overrightarrow{F_{1} F_{2}}$ is:
$\left(\overrightarrow{F_{1} Z}, \overrightarrow{F_{1} F_{2}}\right)=\arctan \frac{1}{\theta}$
Given the unit vector $X_{i}=(0, \ldots, 1, \ldots, 0)$ along axis $i$, we have:
$\left\langle X_{i}, \overrightarrow{F_{1} Z}\right\rangle=\arccos \frac{f_{1 i}-z_{i}}{\sqrt{\sum_{j=1}^{N}\left(f_{1 j}-z_{j}\right)^{2}}}=\arccos \frac{w_{1 i}}{\sqrt{\sum_{j=1}^{N}\left(w_{1 j}\right)^{2}}}$
To investigate the selection pressure of the $i$ th objective, the following equation is solved:
$\arctan \frac{1}{\theta}=\arccos \frac{w_{1 i}}{\sqrt{\sum_{j=1}^{N}\left(w_{1 j}\right)^{2}}}$
And we have:

$$
\left\{\begin{array}{l}
\theta=\frac{w_{1 i}}{\sqrt{\sum_{1, j, j e i}^{N}\left(w_{1 j}^{2}\right)}}>\frac{w_{1 i}^{\prime}}{\sqrt{\sum_{1, j, j e i}^{N}\left(w_{1 j}^{2}\right)}} \\
w_{1 i}^{\prime}=\epsilon w_{1 i}, \epsilon \sim(0,1), i \neq j \\
w_{1 j}^{\prime}=w_{1 j}, 3 k \in\{1, \ldots, N\}, k \neq j \neq i, w_{1 k}^{\prime}=w_{1 k}+(1-\epsilon) w_{1 i}
\end{array}\right.
$$

where $W_{h}=\left(w_{h 1}, \ldots, w_{h N}\right)$ is the weight vector of subproblem $h$. According to Eq. (22), the selection pressure differs from different objectives. The subproblems with evenly distributed weights maintain a relatively large selection pressure and an inferior diversity, and it is the opposite for those with unevenly distributed weights. An example is to adjust the $i$ th weight of $W_{1}$ as Eq. (22) shows to obtain a new weight vector $W_{1}^{\prime}$ which intends to maintain a better diversity of objective $i$ and a better convergence pressure of objective $k$. With more objectives, it can be noticed that:
$\lim _{N \rightarrow \infty}\left\langle X_{i}, \overrightarrow{F_{1} Z}\right\rangle=0$
That is, the solutions grow more vertical to each axis while the angle $\left(\overrightarrow{F_{1} Z}, \overrightarrow{F_{1} F_{2}}\right)$ stays unchanged. This implies that the lost nondominated hypercube becomes larger with more objectives. Since $\theta$ should be big enough to keep a reasonable selection pressure, the lost non-dominated hypercube is inevitable.

For the weighted sum decomposition approach, the hyperplane on which the solution $F_{2}$ have the same decomposed objective value as $F_{1}$ does is:
$\sum_{i=1}^{N} f_{2 i} w_{1 i}=\sum_{i=1}^{N} f_{1 i} w_{1 i}$
Considering a solution $F_{3}$ :
$\left\{\begin{array}{l}F_{3}=\left(f_{31}, \ldots, f_{3 i}, \ldots, f_{3 k}, \ldots, f_{3 j}, \ldots, f_{3 N}\right) \\ f_{3 i}=\xi f_{1 i} \\ f_{3 j}=\zeta\left(\frac{\left(1-\xi f_{1 i}\right.}{w_{2}}+f_{1 j}\right) \\ f_{3 k}=f_{1 k}, k \in\{1, \ldots, N\} \backslash\{i, j\}\end{array}\right.$
where $\xi, \zeta \sim(0,1), F_{3}$ and $F_{1}$ are non-dominated while $F_{3}$ is unable to replace $F_{1}$. Therefore, there still exists less explored area when applying the weighted sum approach. The normal of the hyperplane defined by Eq. (24) is $W_{1}=\left(w_{11}, \ldots, w_{1 N}\right)$. The distribution of the weight over all the objectives has the same effect as the PBI approach does. However, since:
$\arctan \frac{1}{\theta}<\frac{\pi}{2}$
The selection pressure of the weight vector approach is smaller than that of the PBI approach whereas the diversity is better.

With the Tchebycheff decomposition approach, a solution $F_{4}$ that can replace $F_{1}$ can be described as:

$$
\left\{\begin{array}{l}
i=\max _{k}\left\{\left|\left(z_{k}-f_{1 k}\right) w_{k}\right|\right\}, k \in\{1, \ldots, N\}\} \\
j=\max _{k}\left\{\left|\left(z_{k}-f_{4 k}\right) w_{k}\right|\right\}, k \in\{1, \ldots, N\}\} \\
\left|\left(z_{j}-f_{4 j}\right) w_{j}\right|<\left|\left(z_{i}-f_{1 i}\right) w_{i}\right|
\end{array}\right.
$$

Given a certain solution $F_{3}$ that satisfies:

$$
\left\{\begin{array}{l}
\left|\left(z_{i}-f_{3 i}\right) w_{i}\right|>\left|\left(z_{i}-f_{1 i}\right) w_{i}\right| \\
3 k \in 1, \ldots, N,\left|\left(z_{k}-f_{3 k}\right) w_{k}\right|<\left|\left(z_{k}-f_{1 k}\right) w_{k}\right|
\end{array}\right.
$$

we can notice that $F_{1}$ does not dominate $F_{3}$ which is yet unable to replace $F_{1}$. Therefore, the entire Pareto front cannot be explored with equal resource. The possible hypercube to be explored determined by $F_{1}$ can be obtained by solving Eq. (27) for $\forall k \in$ $\{1, \ldots, N\}$ and we have:
$f_{4 k}>z_{k}-\left(z_{i}-f_{1 i}\right) \frac{w_{i}}{w_{k}}$
With $N$ objectives, $F_{1}$ divides the entire objective space into $N^{2}$ hypercubes including one dominating hypercube, one dominated hypercube and $N^{2}-2$ non-dominated hypercubes. The number of non-dominated hypercubes that can be explored under $F_{1}$ is $\frac{N^{2}}{2}-1$. Therefore, almost half of the Pareto front lacks exploration. However, the Tchebycheff approach is not affected by the number of objectives. An example is shown in Fig. 3 in which the contours of different decomposed objective values are presented using the penalty-based boundary intersection (PBI) approach [53]. In Fig. 3, the solutions that can replace individual 4 is in the cone area of which the boundary is defined by individual 4. The solutions to be returned to the decision maker are selected according to the domination relationship. If individual 4 is in the current population, the individuals in region $C$ should also be selected which nevertheless are outside the constrained area. The constrained area becomes smaller as the individuals of this subproblem evolve from individual 1 to individual 9. Considering Theorem 1 at the same time, we can conclude that the conflict is inevitable no matter how many subproblems are generated.

Based on the analysis above, we are inspired by the EDA that a more complete approximation of the Pareto set can be obtained by memorizing the individuals of some neighboring subproblems within several latest generations in a histogram model. With the information of the latest individuals 5, 6, 7, 8 and 9, especially individual 6, promising individuals like individual 10 can also be explored with fair probability.

### 4.1.2. The second factor

Along with time, the users' positions are not the same in different periods. It cannot be guaranteed that the current population obtained based on the previous user distribution is optimal under a new environment no matter whether the population converges or not. Therefore, it is not possible to determine whether a solution should be selected into the next generation or not. Based on the analysis above, including the variable distribution of several latest generations into a local incremental distribution model (LIDM) can improve the robustness of the solutions. With

![img-2.jpeg](img-2.jpeg)

Fig. 3. Conflict between the selection mechanism and domination relationship. (a) Evolutionary process of a certain subproblem in the constrained areas formed by its decomposition function using the PBL. (b) Simulation of the conflict between the selection mechanism and the domination relationship using PBL.
the LIDM, all the promising solutions over a period of time can contribute to the next generation and the fluctuation of the population because the abnormal user positions can be counteracted as well.

### 4.1.3. The third factor

According to [28], the optimization process of the EDA as a Markov chain should satisfy two necessary conditions to be an effective algorithm. The first one is that the algorithm should be able to search the whole parameter space. The second one is that, with local flat objective subspaces, the algorithm should be able to search the whole parameter space with equal likelihood. To address the first condition, a compensation mechanism is introduced into the LIDM as Eq. (32) shows. The compensation mechanism makes sure that there is no degenerated region in the LIDM parameter space, which guarantees that the iteration process is irreducible and ergodic. Regarding the second necessary condition, on the one hand, it is less likely that a local objective subspace stays flat under dynamic environment with more than one objective. On the other hand, the existence of the absorbing area in the parameter space relies on the degenerated possibility parameters like 0 or 1 , which are totally eliminated by the compensation mechanism. In conclusion, the proposed LIDM with the compensation mechanism is irreducible and ergodic throughout the entire optimization process.

The details of the proposed LIDM are described as follows. The size of the area where the NSCS is deployed is $B U \times B L$. The population size is $N$. Each period includes $L$ phases. The position of airship $j, j=1, \ldots, M$, in phase $l$ of individual $i$ is $A P_{l i j}=$ $\left(x_{l i j}, y_{l i j}\right), A P_{l j j} \in \Omega=\{(x, y) \mid x \in[0, B U], y \in[0, B L]\}$. The airship height is fixed so the last coordinate is omitted for simplicity. The individual $i$ is encoded as: $Q_{i}=\left\{A P_{l i j} \mid i \in\{1, \ldots, L\}, j \in\right.$ $\{1, \ldots, M\}\}$. The search space $\Omega$ is divided into $U \times V$ cells. The $K$ neighboring individuals of individual $i$ is $i_{1}, \ldots, i_{K}$. At generation $t$, the local distribution model $P_{U \times V}^{i t}$ of individual $i$ in phase $l$ is calculated as follows:
$P_{U \times V}^{i t}(u, v)=\frac{\sum_{k=1}^{K} C_{U \times V}^{i t_{k}}(u, v)}{\sum_{v=1}^{U} \sum_{v=1}^{V} \sum_{k=1}^{K} C_{U \times V}^{i t_{k}}(u, v)}$
where $C_{U \times V}^{i t}(u, v)$ is the number of airships that are deployed in cell $(u, v)$. The latest $H$ local distribution models of individual $i$ are memorized in:
$S P_{U \times V}^{h t 0}(u, v)=P_{U \times V}^{i t}(u, v)$
where $h=(t \bmod H)+\left\lfloor\frac{t}{H}\right\rfloor$. The compensation value $C P_{U \times V}^{i t}(u, v)$ of cell $(u, v)$ is calculated as:
$C P_{U \times V}^{i t}(u, v)=\frac{1}{\sum_{v=1}^{H} Z^{i t}(u, v)}$
where $Z^{i t}(u, v)$ is calculated as follows:
$Z^{i t}(u, v)= \begin{cases}1, & \sum_{h=1}^{H} S P_{U \times V}^{h t 0}(u, v)=0 \\ 0, & \text { otherwise }\end{cases}$
With the compensation mechanism, the LIDM $T P_{U \times V}^{i t}(u, v)$ of individual $i$ is constructed as:
$T P_{U \times V}^{i t}(u, v)=\frac{1}{H+C F}\left(\sum_{h=1}^{H} S P_{U \times V}^{h t 0}(u, v)+C F \cdot C P_{U \times V}^{i t}(u, v)\right)$

Based on Eq. (34) and similar to the optimality analysis in [54], we can prove the irreducible and ergodic characteristics of the LI-EDA-ADR as follows.

Theorem 2. The Markov chain of the set of the LIDM as its status space is irreducible and ergodic if $C F>0$.

Proof. The lower bound of Eq. (34) for any $(u, v), u \in\{1, \ldots, U\}$, $v \in\{1, \ldots, V\}$ can be obtained by considering an extreme case where all the airships of the neighbor solutions of a certain subproblem are deployed in one block $\left(u_{0}, v_{0}\right)$. And thus the lower bound of $T P_{U \times V}^{i t}(u, v)$ at $t-1$ is:

$$
\left\{\begin{array}{l}
T P_{U \times V}^{(t-1) 0}(u, v)=\frac{1}{H+C F}\left(C F \cdot \frac{1}{H t-1}\right) \\
u \in\{1, \ldots, U\}, v \in\{1, \ldots, V\}, u \neq u_{0}, v \neq v_{0}
\end{array}\right.
$$

Given the finite and countable status space of population $\Omega=$ $\left\{\lambda^{1}, \ldots, \lambda^{L}\right\}$, the probability transition matrix of $\Omega$ is $T_{L \times L}(i, j)=$ $P\left(\lambda^{1} \mid \lambda^{j}\right)$. Therefore, the probability of the population transiting from time $t-1$ to $t$ can be calculated as:
$P\left(\lambda_{t}^{i} \mid \lambda_{t-1}^{j}\right)=T_{L \times L}(i, j)=\sum_{k=1}^{K} P\left(D_{k} \mid \lambda_{t-1}^{j}\right) \cdot P\left(\lambda_{t}^{i} \mid O, D_{k}\right)$
where $D_{k} \in \Psi$ and $\Psi$ is the set of the candidate populations and $K$ is the size of $\Psi . O$ is a deterministic selection mechanism, and therefore, we have:

$$
\left\{\begin{array}{l}
P\left(\lambda_{t}^{i} \mid O, D_{k}\right)=1 \\
P\left(\lambda_{t}^{i} \mid \lambda_{t-1}^{j}\right)=\sum_{k=1}^{K} P\left(D_{k} \mid \lambda_{t-1}^{j}\right)
\end{array}\right.
$$

Since the generation and selection of the offspring are independent for each subproblem, we have:

$$
\left\{\begin{array}{l}
P\left(D_{k} \mid \lambda_{t-1}^{i}\right)=\prod_{i=1}^{N} P\left(S_{k}(n) \mid \lambda_{t-1}^{i}\right) \\
P\left(S_{k}(n) \mid \lambda_{t-1}^{i}\right)=\prod_{r=1}^{R}\binom{m_{r}}{M}\left(T P_{U=V}^{(t-1) n}\left(u_{r}, v_{r}\right)\right)^{m_{r}} \\
\sum_{r=1}^{R} m_{r}=M
\end{array}\right.
$$

where $S_{k}(n)$ is the offspring of subproblem $n$ in $D_{k} . N$ and $R$ are the neighborhood size and the number of blocks where the airships are deployed respectively. $M$ is the number of airships. Considering Eqs. (35)-(38), we have:
$P\left(\lambda_{t}^{i} \mid \lambda_{t-1}^{j}\right) \geqslant \sum_{k=1}^{K} \prod_{n=1}^{N} \prod_{r=1}^{R}\binom{m_{r}}{M}\left(\frac{1}{H+C F}\left(C F \cdot \frac{1}{U V-1}\right)\right)^{m_{r}}$
Since $C F>0$, we have:
$P\left(\lambda_{t}^{i} \mid \lambda_{t-1}^{j}\right)>0$
And the proof is completed.

## Algorithm 1 The Asymmetrical Domination Relationship

1: Input: external population $E P$; the size of $E P: P$; the set of all the objective value sets: $\left\{\left\{F C_{i}, F P_{i}\right\} \mid i=1, \ldots, P\right\}$; the new individual: indiv; the number of the objectives: $K$.
2: Initialization: insert $=1$, remove $(i)=0, i=1, \ldots, P$.
3: if the environment change is detected then
4: for $i=1$ to $P$ do
5: Calculate the objective value of $E P(i)$ in the new environment, and store the objective value vector $\left(f_{1}(E P(i)), \ldots, f_{K}(E P(i))\right)$ in $F C_{i}$.
6: Insert $\left(f_{1}(E P(i)), \ldots, f_{K}(E P(i))\right)$ into $F P_{i}$.
7: Remove all the dominated objective value vectors in $\left\{F C_{i}\right\} \cap F P_{i}, i=1, \ldots, P$.
8: end for
9: for $i=1$ to $P$ do
10: for $j=1$ to $P, j \neq i$ do
11: if $\forall F P_{i}\left(m_{i}\right), \exists F P_{j}\left(m_{j}\right), F P_{i}\left(m_{i}\right)$ is dominated by $F P_{j}\left(m_{j}\right)$ then
12: remove $(i)=1$.
13: end if
14: end for
15: end for
16: end if
17: for $i=1$ to $P$ do
18: if remove $(i)=1$ then
19: Remove $E P(i)$ from $E P$ and $P=P-1, i=i-1$.
20: end if
21: end for
22: for $i=1$ to $P$ do
23: if $\left(f_{1}\right.$ (indiv), $\ldots, f_{K}$ (indiv)) is dominated by $F C_{i}$ then
24: insert $=0$.
25: Break.
26: end if
27: end for'
28: if insert $=1$ then
29: Insert the new individual indiv into $E P$.
30: end if
31: Output: EP

### 4.2. Asymmetrical domination relationship

With multiple evaluations of each external individual under different environments, the traditional domination relationship is
not sufficient to select robust individuals. Apparently, for each external individual, the past and current objective values play different roles in the evaluation of an individual. In addition, the past objective values should not barricade the new individuals being selected into the external population but help assess the overall quality of the current external population. Therefore, an asymmetrical domination relationship (ADR) is proposed as Algorithm 1 shows. With $K$ objectives, a set for each external individual $E P(i)$ is maintained as: $\left\{F C_{i}, F P_{i}\right\}$ :
$F C_{i}=\left\{\left(f_{1}^{c}(E P(i)), \ldots, f_{K}^{c}(E P(i))\right)\right\}$
$F P_{i}=\left\{\left(f_{1}^{p m_{i}}(E P(i)), \ldots, f_{K}^{p m_{i}}(E P(i))\right) \mid m_{i}=1, \ldots, M\right\}$
where $F C_{i}$ is the set of the objective value vector obtained by individual $E P(i)$ in the current environment. $F P_{i}$ is the set of $M$ non-dominated objective value vectors obtained by individual $E P(i)$ in all the past environment. $F P_{i}\left(m_{i}\right)$ is the $m_{i}$ th objective value vector in $F P_{i}$. The algorithm of the ADR is shown in Algorithm 1. An example is shown in Fig. 4. A new individual $A$ is included in the external population if its objective value vector is not dominated by the objective value vectors of all the external individuals calculated in the current environment. An external individual, for example, individual $C$, is removed from the EP iff. there exists another individual $B$ and each of the objective value vectors of individual $C$ is dominated by a certain objective value vector of individual $B$.

The advantages of the ADR are described as follows.

- The ADR is a generalized form of the traditional domination relationship and can be applied in the existing algorithms without modification.
- With non-dominated objective value vectors in different environments, it is more accurate to select the external population.
- The robust external population is protected, and the difficulty that a new individual enters the EP does not change.

The local incremental estimation of distribution algorithm with the asymmetrical domination relationship is shown in Algorithm 2. The entropy based termination criterion [55] is applied in this paper.

### 4.3. Computational complexity analysis

In Algorithm 2, the generation of the subproblems and the initial population requires $O(M N+N \log N)$ computations, where $M$ and $N$ are the numbers of airships and population size, respectively. It consumes $O(L U M)$ computations to calculate the objective values, where $L$ is the number of phases in one period and $U$ is the number of users. The initialization of the external population requires maximum $O\left(N^{2}\right)$ comparisons. The estimation of the subproblem $n$ in step 5 requires $L(K M+H)$ computations, where $K$ is neighborhood size. $H$ is the number of the included historical population distributions in the LIDM. Step 6 requires $O\left(L M P^{2}\right)$ computations, $P$ is the number of the divided cells used to count the number of deployed airships in it. The replacement operation from step 11 to 17 needs $O(K)$ computations. According to Algorithm 1, the update of EP consumes maximum $O\left(E^{2} C^{2}\right)$ computations, where $E$ is the size of EP and $C$ is the total number of periods so far. And then the computations required from step 4 to 19 is $O\left(N L\left(K M+M P^{2}+H\right)+N E^{2} C^{2}\right)$. To sum up, the overall upper bound of the computational complexity is $O\left(N L\left(U M+M P^{2}+H\right)+N^{3} C^{2}\right)$.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Asymmetrical domination relationship with two objectives.
Table 1
Details of the four test problems.

${ }^{a}$ Each hotspot follows Gaussian distribution.
${ }^{\mathrm{b}}$ The number of the urban users of each hotspot in the first phase.
${ }^{\mathrm{c}}$ The number of the suburban users of each hotspot in the second phase.

## 5. Experiments and discussion

In this section, the proposed local incremental estimation of distribution algorithm with the asymmetrical domination relationship is tested on four designed NSCS deployment optimization problems in the dynamic environment. The deployment area is $100 \times 100$. The details of these four problems are described in Table 1.

### 5.1. Comparison of local incremental EDA with ADR against four competitive algorithms

Considering the complexity of the problems and to eliminate the algorithm bias on the search space, we test the proposed algorithm together with another four general algorithms under the same MOEA/D framework. These four algorithms are the MOEA/D with the simulated binary crossover (SBX) and the polynomial mutation (SBX-PN) [56], the MOEA/D with the differential evolution (DE) and the polynomial mutation (DE-PN) [57], the MOEA/D with the blend crossover (BLX) and the non-uniform mutation (BLX-NU) [58] and the MOEA/D with the geometrical crossover and the non-uniform mutation (GC-NU) [59]. The crossover probability is 0.8 and the mutation probability is 0.1 . The $F$ parameter of the DE is 0.5 . The parameters of the SBX and BLX are 1 and 0.5 , respectively. The penalty factor of the PBI is 1 . The length of the estimated generations of the LI-EDA-ADR is 10. The compensation factor is 0.3 . The population size is 100 and the neighborhood size is 10 . The capacity and height of each airship are 100 and 30, respectively. Each airship covers a circle area of radius 30. The mobility of each airship is 10. Each period contains 10 generations. All the four problems are solved with $4,5,6$ and 8 airships. Each instance is repeated for 10 times.

The airship deployments of 10 repeated tests of problem 1 are shown in Fig. 5. From this figure, it can be noticed that all the five
algorithms succeed in locating the hotspots of these two phases. Despite the uniformly distributed users, there are some promising regions that are more suitable for the deployment. The detection and evaluation of the promising regions imply the algorithm performance. Regarding the SBX-PN and BLX-NU, we can notice that these two algorithms perform well in several conjunction regions between two promising regions. This is due to the fact that these two algorithms both generate new offspring along the line that crosses two parents and the conjunction regions are more likely to be explored. This helps these two algorithms generate a smoother transmission among the promising regions. In contrast, the promising regions obtained by the proposed algorithm are much larger due to the combination of the global and local search based on the LIDM. In addition, we can notice that all the four algorithms despite the LI-EDA-ADR have difficulty in exploiting some parts of the vicinity of the hotspots. This is because the other four algorithms generates the offspring based on the locations of the parents. With relatively nearer parents, the offspring of high quality can be generated. However, as the geometrical distance between the selected parents getting bigger, the subspace to be searched gets larger so that the newly generated offspring spread out more. Compared with the offspring generated by the nearer parents, these offspring are inferior in fitness and suppressed by those offspring generated by the nearer parents. This phenomenon gets even worse as the deployment area getting larger, which in turn causes the intermediate regions to be less explored. Therefore, the loss of some promising areas is inevitable for the geometry-based algorithms. Compared with the other four algorithms, the proposed algorithm obviously provides more promising deployment locations. As mentioned above, the LI-EDA-ADR is not limited by the geometrical location of the parents, thus the whole search area can be explored more efficiently. Therefore, the high-quality offspring can be generated more easily. In conclusion, the experimental results and analysis

![img-4.jpeg](img-4.jpeg)

Fig. 5. Deployments of 8 airships of 10 repeated tests of the test problem 1. The color changes from blue to red as the subproblems focusing from on coverage to network speed. The airship deployment of each subgraph is obtained by (a) SBX-PN, (b) DE-PN, (c) BLX-NU, (d) GC-NU and (e) LI-EDA-ADR.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Synthetic Pareto fronts of 8 airships of 10 repeated tests of the four test problems with the newly generated user distribution. The Pareto front of each subgraph is obtained from (a) Test problem 1, (b) Test problem 2, (c) Test problem 3 and (d) Test problem 4.
in Section 4 indicate that the LI-EDA-ADR has a theoretical potential to fully explore the whole search space especially in the dynamic environment.

The synthetic Pareto fronts obtained with the newly generated user distribution are shown in Fig. 6. Except the LI-EDA-ADR, it can be noticed that all the four algorithms are unable to obtain the complete Pareto front. This includes two reasons. First, a robust individual is difficult to distinguish in the dynamic environment and cannot be preserved properly. However, the LI-EDA-ADR can evaluate these individuals more fairly thus succeed in preserving these superior individuals. Second, we can notice that all the four algorithms lose some parts of the Pareto front where the first objective is emphasized. This is because the search space for a larger coverage is relatively bigger than that of a fast network speed. Thus, it is easier to achieve a high value of the second objective. In contrast, the LI-EDA-ADR assesses the whole search space based on the LIDM which is more comprehensive. And the local information provided by the neighboring subproblems is utilized more efficiently by the LI-EDA-ADR. In this figure, it can also be noticed that the other four algorithms outperform the LI-EDA-ADR as the coverage is more emphasized. The first
reason is that more computation resource is allocated to the coverage optimization due to the premature population. The second reason is that the compensation factor is small in this experiment. A larger compensation factor will improve the performance of LI-EDA-ADR on the coverage while deteriorating the performance on the network speed. The effect of the compensation factor is demonstrated in Section 5.4.

To investigate the overall performance of these five algorithms from the statistic point of view, the hypervolume of each algorithm is compared with that of the LI-EDA-ADR shown in Table 2. From this table, we can notice that the LI-EDA-ADR outperforms the other four algorithms significantly with 4 and 5 airships. In some cases with more airships, like 6 and 8 airships, the hypervolume obtained by the LI-EDA-ADR is not better or worse than those of the other four algorithms. Regarding the results in Fig. 6, the more balanced computation resource allocation makes the LI-EDA-ADR not fully converge with more airships. However, the proposed LI-EDA-ADR can obtain more complete Pareto fronts than the other algorithms do. Consider the analysis above, we can conclude that the LI-EDA-ADR outperforms the other algorithms in obtaining more complete Pareto fronts and qualified solutions in the dynamic environment.

Table 2
$t$ test results and the comparison of LI-EDA-ADR with four competitive algorithms.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Box-plot of the hypervolume obtained by solving test problem 1 with 4 airships with different estimated generations.

### 5.2. Experimental results on the length of the estimated generations

The length of the estimated generations plays an important role in the performance of the LI-EDA-ADR. To investigate its effect, the test problem 1 with 4 airships is solved with different
estimated generations. The result is shown in Fig. 7. From this figure, we can notice that the LI-EDA-ADR performs better with an estimated generation length from 7 to 20. The algorithm with 2 estimated generations does not perform well due to a less robust LIDM in the dynamic environment. With 3 or more generations, the performance is improved significantly. The algorithm can obtain more qualified solutions with 7 to 20 estimated generations than in the other cases. However, the algorithm performance becomes less stable with more estimated generations. As for the cases with too many estimated generations, like 30 estimated generations in this figure, the LIDM estimates both many good and bad individuals which undermine the performance. Thus, the performance varies dramatically in the case of 30 estimated generations. However, the best length of the estimated generations depends on the specific problem, and thus the proposed algorithm performs the best with a fine tuned length of estimated generations on different problems.

### 5.3. Experimental results on environment change frequency

As we have pointed out in Section 5.2, the performance of the LI-EDA-ADR is also affected by the difficulty of specific problems. The environment change frequency plays a key role in the difficulty of the deployment optimization of the NSCS. To investigate the effect of the environment change frequency on the problem difficulty, the problem 1 with 4 airships is solved with environment changing every $5,10,15$ and 20 generations. The result is shown in Fig. 8. From this figure, we can notice that the best hypervolume achieved decreases as the environment change frequency decreases. This is because the internal

## Algorithm 2 The Local Incremental EDA with the ADR

1: Input: population size: $N$; neighborhood size: $K$; the parameters of the NSCS; the parameters of the LIDM; the parameters of the ADR.
2: Initialization:

- Generate $N$ subproblems and the initial population randomly.
- Calculate the objective value and the decomposed objective value of the population.
- Initialize an empty external population (EP).

3: while the termination criterion is not satisfied do
4: for $n=1$ to $N$ do
5: Estimation: for the subproblem $n$, estimate the LIDM as Eq. (34).
6: Sampling: sample a new individual $n^{\prime}$ from the estimated LIDM.
7: Repair: repair the new individual $n^{\prime}$ as described in Section 4.2.
8: if environment changes at $t$ then
9: $\quad$ Generate the new user distribution according to Eq. (4) and update the decomposed objective value of each internal individual.
10: end if
11: Replacement:
12: for $k=1$ to $K$ do
13: $\quad$ Calculate the decomposed objective value $f_{d}\left(n^{\prime} \mid w_{k}\right)$ with the weight vector $w_{k}$ of the neighbor individual $k$ of the individual $n$.
14: if $f_{d}\left(n^{\prime} \mid w_{k}\right)<f_{d}\left(k \mid w_{k}\right)$ then
15: Replace the individual $k$ with the individual $n^{\prime}$.
16: end if
17: end for
18: $\quad$ Update EP: update EP according to Algorithm 1.
19: end for
20: end while
21: Output: EP
![img-7.jpeg](img-7.jpeg)

Fig. 8. Box-plot of the hypervolume obtained by solving the test problem 1 with 4 airships under different environment change frequencies.
population changes less severely with low environment change frequency which deteriorates the exploration capability of the
![img-8.jpeg](img-8.jpeg)

Fig. 9. Hypervolume obtained by solving the test problem 1 with 5 airships and different compensation factors.
present internal population. With bigger environment change frequency like 5 and 10 generations, the quality of the best solutions increases. As we have discussed in Section 4.1.3, the new fitness evaluation in the new environment helps assess the robustness of the internal and external population. With more fitness evaluations in different environments, it is easier to refine the promising solutions. However, by comparing the results for 5 and 10 generations cases, a big change frequency also deteriorates the averaged quality of the population. Considering the result obtained with a newly generated user distribution in Fig. 8, we can conclude that multiple evaluations in different environments are important in obtaining solutions of high quality both for dynamic and static optimization problems.

### 5.4. Experimental results on compensation factor

The compensation factor balances the convergence and divergence of the LI-EDA-ADR. To investigate to what extent the compensation factor affects the performance of the LI-EDA-ADR, we solve the test problem 1 with 5 airships using different compensation factors, and the result is shown in Fig. 9.

From this figure, we can notice that there are two opposite trends. As the compensation factor increases, the averaged hypervolume increases while the best hypervolume decreases. The reason is, with a small compensation factor, the LI-EDAADR explores the promising area with more effort which helps generate more qualified solutions like the case of 0.005 as shown in Fig. 9. However, due to the relatively poor diversity, it is easy for some inferior solutions to survive in the less competitive population. Thus, the averaged hypervolume is relatively low. With a bigger compensation factor, the diversity of the LIDM is alleviated. More qualified individuals are estimated by the LIDM, thus, the averaged hypervolume increases. However, the limited computation resource is assigned to more individuals. The improvement of the promising individuals is deteriorated. Therefore, the cases like $0.5,0.6$ and 0.7 have better averaged hypervolumes but fewer solutions of high quality. Based on the analysis above, we can conclude that the compensation factor balances the computation resource allocation between the exploration and exploitation. With a small compensation factor, the proposed algorithm is able to obtain solutions of high quality, while the averaged fitness of the solutions is relatively poor. A

larger compensation factor prompts the algorithm to improve the fitness of the whole population, while less computation resource is used to improve the fitness of the best solutions.

## 6. Concluding remarks

In this paper, we propose a local incremental estimation of distribution algorithm with an asymmetrical domination relationship to solve the deployment optimization problem of the near space communication system in the dynamic environment. We first conclude the features of the dynamic user distribution and propose a dynamic user distribution model. And then the deployment optimization in the dynamic environment is proposed as a multiobjective optimization problem based on two major concerns of the NSCS. Based on the features of the target MOP and similar problems, we summarize the development and advantages of the EDA. Three major issues of the EDA are theoretically analyzed in the dynamic environment: dynamic environment's effect, the conflict between the selection mechanism of the external and internal population and the exploration ability in the probability model space. Based on the analysis of these three issues, the LI-EDA-ADR is proposed. We test the proposed algorithm compared with the other four popular algorithms. The result demonstrates that the proposed LI-EDA-ADR is an effective algorithm and outperforms the other four algorithms significantly. Important parameters like the length of the estimated generations, the compensation factor and environment change frequency are investigated in the experiments. Some guidelines for tuning these parameters are given as well.

There are also many interesting problems that are worth notice. The first one is that an adaptive mechanism for the compensation factor can help the algorithm perform well. The second one is that it might be helpful to add a noise to the objective functions of a static MOP or dynamic MOP to improve the solution quality. These two problems will be investigated in our future work.

## Acknowledgments

This work was supported by the National key research and development program of China (Grant no. 2017YFB0802200), the National Natural Science Foundation of China (Grant nos. 61772393), and the Key research and development program of Shaanxi Province (Grant no. 2018ZDXM-GY-045).
