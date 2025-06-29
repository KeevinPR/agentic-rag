# APPLIED RESEARCH 

## An Adaptive Evolutionary Multi-Objective Estimation of Distribution Algorithm and Its Application to Multi-UAV Path Planning

REN YUHANG ${ }^{\circledR}$ AND ZHANG LIANG ${ }^{\circledR}$<br>Department of Mathematics, School of Science, Wuhan University of Technology, Wuhan 430070, China<br>Corresponding author: Zhang Liang (zhangl@whut.edu.can)


#### Abstract

This paper concerns the multi-UAV cooperative path planning problem, which is solved by multi-objective optimization and by an adaptive evolutionary multi-objective estimation of distribution algorithm (AEMO-EDA). Since the traditional multi-objective optimization algorithms tend to fall into local optimum solutions when dealing with optimization problems in three dimensions, we suggest an advanced estimation of distribution algorithm. The main idea of this algorithm is to integrate the adaptive deflation of the selection rate, adaptive evolution of the covariance matrix, comprehensive evaluation of individual convergence and diversity, and reference point-based non-dominated ranking. A multi-UAV path planning model involving multi-objective optimization is established, and the designed algorithm is simulated and compared with other three high-dimensional multi-objective optimization algorithms. The results show that the AEMO-EDA proposed in this paper has stronger convergence and wider population distribution diversity in applying to the multi-UAV cooperative path planning model, as well as better global convergence. The algorithm can provide an stable path for each UAV and promote the intelligent operation of the UAV system.


#### Abstract

INDEX TERMS Multiple UAVs, collaborative path planning, multi-objective optimization, estimation of distribution algorithms, evolutionary algorithm.


## I. INTRODUCTION

In the past decade, unmanned aerial vehicles (UAVs) have been significant in applications due to the growing autonomous capabilities of UAV systems. These systems have been employed in various fields, including military, public, and civil applications [1], [2], [3], and have attracted various research interest. UAV path planning refers to the process of computerizing the construction of an optimal UAV path for a given scenario, considering factors such as path length, terrain environment, threat information, energy consumption, and other relevant factors. However, given the complexity of scenarios, a single UAV may no longer be sufficient to meet the requirements. Hence, there is an urgent need for collaborative multi-UAV path planning that considers not only the length and invisibility of UAV paths but also the synergy

[^0]between multiple UAVs to ensure the safty in completion of their tasks.

The UAV path planning problem is essentially an optimization problem with practical applications. In recent research, various optimization algorithms have been applied to this problem. For instance, Qu et al. proposed a hybrid algorithm that combined a simplified grey wolf optimizer with an improved symbiotic search to obtain feasible and efficient routes [4]. Genetic algorithms were used by the authors in [5] to optimize UAV path distances and path threat costs. Dasdemir et al. designed a preference-based multi-objective evolutionary algorithm that optimizes both the total distance of the planned path and the radar detection threat [6]. Yao et al. proposed a hybrid algorithm based on model predictive control and an improved grey wolf optimizer to plan optimal paths for multi-UAV target tracking in urban environments [7]. In [8], Peng Yang et al. modified the UAV path planning space by replacing the Cartesian coordinate system


[^0]:    The associate editor coordinating the review of this manuscript and approving it for publication was Wei Liu.

with a polar coordinate system and used an estimation of distribution algorithms (EDAs) to search for optimal paths.
Many works on UAV path planning has focused on single-objective optimal path planning problems, either by considering only a single objective or by integrating multiple objectives into a single objective using linear weighting [9], [10], [11]. However, this approach can be subjective as the decision maker sets the coefficients for the weighting of multiple objectives, which may dramtically affect the outcome of the optimization, while the most suitable paths that perform well on smaller targets may be missed. Some current research on multi-objective path planning considers two or three objectives, the UAV path planning problem is a practical optimization problem and the number of objectives to be optimized should not be limited to three. Therefore, it is necessary to establish high-dimensional multi-objective optimization algorithms for UAV path planning [12], [13].
The EDAs is a novel optimization algorithm based on machine learning theory [14]. As a gradient-free evolutionary algorithm, EDAs search the solution space primarily by maintaining the evolution of individuals within the population, with each individual representing a feasible solution. Unlike traditional evolutionary algorithms, EDAs do not employ genetic operators. Instead, they construct probabilistic models to characterize the distribution of the population and then sample these models to generate new individuals and populations [15]. Due to the random nature of offspring sampling, EDAs retain a high level of diversity and strong global search capability [16]. Numerous researchers have dedicated to developing effective EDAs, which have been widely applied to various optimization problems, such as multi-modal optimization problems [17], multiobjective optimization problems [18], and practical problems like multi-strategy insurance investment planning [19] and content-driven interactions generated by multiple sources of heterogeneous users [16]. EDAs also have numerous applications in the field of UAV path planning [20], [21], [22].
Although EDAs have been applied to numerous problems, research on UAV path planning using EDAs is limited. A basic Gaussian distribution EDA (GEDA) can solve the UAV path planning problem [8], but its convergence efficiency is suboptimal when the number of variables is large. To address the issue of dimensional explosion caused by multiple UAVs, this study proposes an improved multi-objective optimized GEDA for solving the multi-UAV collaborative path planning problem. The main contributions of this study are as follows:

- We establish a path planning model that constructs a high-dimensional multi-objective optimization model with path cost, spatial threat cost, terrain concealment index, and spatial synergy index as the optimization objectives. It is worth noting that this model treats multiple UAV paths as a whole, represented as individuals in a population, and optimizes multiple UAV paths simultaneously.
- We improve the GEDA algorithm by adaptively controlling the selection rate of mean and variance based on the number of iterations, enhancing the algorithm's global search ability and population diversity. Additionally, we add historical data to the estimation of covariance to prevent information loss.
- We use the comprehensive individual assessment method from [13] to select elite individuals, maintaining population diversity and improving population convergence. We also use a reference-point-based nondominated sorting method in environmental selection to address high-dimensional multi-objective optimization problems [23].

The paper is organized as follows. Section II presents the multi-UAV path planning model and formulates the four optimization objectives. Section III focuses on improving GEDAs to enhance their ability to deal with high-dimensional multiobjective optimization problems. In Section IV, we verify the effectiveness of our method through simulation analysis and comparative experiments. Finally, we present our conclusions in Section V.

## II. COLLABORATIVE MULTI-UAV PATH PLANNING MODELING

## A. PROBLEM DESCRIPTION

In the multi-UAV collaborative path planning problem, multiple UAVs take off from the same starting point or different In the multi-UAV collaborative path planning problem, multiple UAVs take off from the same starting point or different starting points to travel to a target location and execute a mission. The UAVs fly in a complex mountainous area where radar warning areas and fire attack areas are deployed by the enemy. It is necessary to consider the constraints of the UAVs' capabilities and the synergy between multiple UAVs during the actual flight. This study simulates and analyzes the paths of multiple UAVs in a 3D planning space based on these characteristics. For the sake of arithmetic, the following assumptions are made: (1) the flight speed of the UAV remains constant during the mission; (2) the path of each UAV is divided into many path segments, and within each segment, the UAV flies in a straight line; (3) each UAV has the same capabilities.

## B. REPRESENTATION OF PLANNING SPACE AND PATH

In this paper, we use the rasterization method to represent the planning space. Rasterization is a discrete method that evenly distributes points on a regular square lattice, which can handle large planning spaces and is also suitable for 3D planning spaces. The planning space is rasterized by dividing the $x$ axis into $n^{\prime}$ sub-regions and the $y$ axis into $m^{\prime}$ sub-regions with a certain step, creating an $\left(n^{\prime}+1\right) \times\left(m^{\prime}+1\right)$ coordinate system for the $x$ and $y$ axis. The UAV path planning space can be

![img-0.jpeg](img-0.jpeg)

FIGURE 1. Representation of planning space and paths.
described as the following set:

$$
\Omega=\left\{\left(x_{i}, y_{i}\right) \mid i=1,2, \ldots, n^{\prime}+1, j=1,2, \ldots, m^{\prime}+1\right\}
$$

Similarly, the same operation can be performed for the three-dimensional planning space, so that the threedimensional planning space can be expressed as follows:

$$
\Omega=\left\{\left(x_{i}, y_{i}, z_{k}\right) \mid k=1,2, \ldots, l^{\prime}+1\right\}
$$

On the basis of the rasterised planning space, the UAV path can be discretized and represented as a series of coordinate points in the planning space, where the neighbouring points are directly connected by straight-line segments. This is shown in Figure 1 (in two dimensions).

Figure 1 shows a simple UAV path planning problem, where $U$ is the UAV platform, the UAV's departure location, $T$ is the mission target location, and $T_{1}, T_{2}$, and $T_{3}$ represent the threat area, then the path planning can be described as planning a suitable path for the UAV to travel from the UAV platform to the mission location for mission execution and avoiding the UAV from entering the threat area. For the sake of illustration, we use $r$ to denote the column of path points in the path planning space, and the discrete path can be expressed as:

$$
r=\left\{\left(x_{1}, y_{1}, z_{1}\right),\left(x_{2}, y_{2}, z_{2}\right), \ldots,\left(x_{n+1}, y_{n+1}, z_{n+1}\right)\right\}
$$

where $n$ is the number of path points, then $r_{i}$ can be referred to as one of the path segments in path $r$. A path should consist of $n$ path segments.

## C. OPTIMIZING THE DESIGN OF OBJECTIVE MODELS

In the context of the multi-UAV collaborative path planning problem, the optimization objectives encompass the path cost, spatial threat cost, terrain concealment index, and spatial synergy index. The goal of the multi-UAV collaborative path planning model is to facilitate the highest possible terrain
concealment and spatial coordination, with the lowest possible path cost and spatial threat cost for multiple UAVs. This constitutes a multi-objective optimization problem, whereby the objective function must be designed such that the smaller the value of the function, the better the objective. The model construction process for each optimization objective is given below.

## 1) PATH COST

The total path length refers to the overall spatial distance that a UAV must fly from its platform to the mission execution point, expressed as the path cost in this paper. The smaller the path cost, the more direct flight segments the UAV has along its path, which is more suitable for the UAV's manoeuvrability. Moreover, a smaller trajectory length cost results in a shorter flight time for the UAV, thereby increasing the efficiency of its operations. Assuming the existence of $m$ UAVs, with each UAV's path divided into $n$ segments, the path cost can be expressed as follows:

$$
f_{d}=\sum_{i=1}^{m} \sum_{j=1}^{n} l_{i j}
$$

where $l_{i j}$ is the distance cost of UAV $i$ on path segment $j$, which is calculated here using Euclidean distance.

## 2) SPATIAL THREAT COST

Assuming that there are $N_{\text {sila }}$ threat areas in the UAV mission area, which include radar, fire, and environmental threats. Each threat area has an absolute threat radius and a reachable threat radius, and if a UAV passes within the absolute threat radius, it will come under enemy fire. If it passes within the reachable threat radius, it is likely to receive enemy fire, and the probability of being attacked increases as it gets closer to the center of the threat. Let $d_{\min }$ and $d_{\max }$ denote the absolute and reachable threat radii, respectively. The spatial threat cost per UAV can be expressed as follows:

$$
\begin{aligned}
f_{t} & =\sum_{i=1}^{n} \sum_{j=1}^{N_{\text {sila }}} K_{j} t_{i j} \\
t_{i j} & =l_{i} \int_{l_{i}} f_{j}(X) d x
\end{aligned}
$$

where $K_{j}$ is a parameter reflecting the strength of threat $j$, and $t_{i j}$ is the overall threat index of path segment $i$ in the UAV's path route with respect to threat $j$. To reduce computational effort, the integral can be approximated by using the average of the threat indices for some points on the path segment [24]. $f_{j}(x)$ is the threat index of threat $j$ to point $X$, which is calculated as follows:

$$
f_{j}(x)= \begin{cases}N, & R_{j}<d_{\min } \\ N\left(\frac{d_{\max }-R_{j}}{d_{\max }-d_{\min }}\right)^{4}, & d_{\min }<R_{j}<d_{\max } \\ 0, & d_{\max }<R_{j}\end{cases}
$$

where $R_{j}$ is the distance of point $x$ from the center of threat $j$. In summary, the sum of the space threat cost of all UAVs is the total space threat cost, i.e., $f_{T}=\sum_{i=1}^{m} f_{i}{ }^{i}$.

## 3) TERRAIN CONCEALMENT INDEX

Terrain concealment is primarily related to the altitude at which the UAV flies during actual flight. In this study, it is assumed that the safe flight altitude of the UAV is denoted as $h_{\text {safe }}$, the maximum flight altitude is $h_{\text {max }}$, and the terrain concealment index $f_{\text {hide }}$ can be expressed as follows:

$$
f_{\text {hide }}=\left\{\begin{array}{lc}
\sum_{i=1}^{m} \sum_{j=1}^{n}\left(h_{\text {safe }}+h_{\max }\right) l_{i j}, & z_{i j}^{\prime}<h_{\text {safe }} \\
\sum_{i=1}^{m} \sum_{j=1}^{n}\left(2 h_{\text {safe }}+h_{\max }-z_{i j}^{\prime}\right) l_{i j}, & z_{i j}^{\prime} \geq h_{\text {safe }}
\end{array}\right.
$$

where $z^{\prime} i j=z i j-z_{D E M}, z_{i j}$ represents the altitude of a given path segment, and $z_{D E M}$ is the height value of the corresponding path segment in the digital map of the planning space. Furthermore, $l_{i j}$ denotes the distance cost of UAV $i$ on path segment $j$.

## 4) SPATIAL SYNERGY INDEX

When multiple UAVs are involved in a mission, they need to be at an appropriate, safe distance from each other to prevent collisions and to avoid exposing each other's positions. This enhances the safety of the UAVs working together on a mission. The spatial synergy performance of multiple UAVs can be expressed as the sum of the minimum distances between multiple UAV path points within $n$ path segments [25]. The spatial synergy index $f_{\text {space }}$ can be expressed as follows:

$$
\begin{aligned}
f_{\text {space }} & =\sum_{j=1}^{n} \sum_{i=1}^{m^{\prime}} f_{i j} \\
f_{i j} & = \begin{cases}0, & \min d_{j}\left(i, i_{\text {nei }}\right)>d_{\text {safe }} \\
\left(\frac{d_{\text {safe }}}{\min d_{j}\left(i, i_{\text {nei }}\right)}\right)^{4}, & \min d_{j}\left(i, i_{\text {nei }}\right) \leq d_{\text {safe }}\end{cases}
\end{aligned}
$$

where $\min d_{j}\left(i, i_{\text {nei }}\right)$ is the Euclidean distance between UAV $i$ and its closest untraversed UAV $i_{\text {nei }}$ on path segment $j, m$ is the number of UAVs passing through path segment $j$, and $d$ is the minimum safe distance between two UAVs. As per Eq. 10, the lower the value of the spatial synergy index, the higher the spatial synergy between the UAVs.

## D. CONSTRAINTS AND MULTI-OBJECTIVE OPTIMIZATION MODELS

In actual flight, UAVs are often subject to many constraints due to their own airframe performance. Specifically, during flight the UAV is mainly limited by the minimum straight flight distance $l_{\max }$, the maximum turn angle $\theta$, the maximum climb height $Z_{\max }$ and the maximum total path length $L_{\max }$. Therefore, combining the four optimization objectives proposed in the previous section, and taking the path $r$ as a variable, a multi-objective optimization model can be proposed
as follows:

$$
\begin{aligned}
& \operatorname{minimize} F(x)=\left(f_{d}(r), f_{i}(r), f_{\text {hide }}(r), f_{\text {space }}(r)\right)^{T} \\
& \text { s.t. }\left\{\begin{array}{l}
l_{i j} \leq l_{\max } \\
\left\|z_{i j}-z_{i(j+1)}\right\| \leq Z_{\max } \\
\arccos \frac{\alpha_{i} \cdot \alpha_{i-1}^{T}}{\left\|\alpha_{i}\right\| \cdot\left\|\alpha_{i-1}\right\|} \leq \theta \\
\sum_{j=1}^{n}\left|l_{i j}\right| \leq L_{\max }
\end{array}\right.
\end{aligned}
$$

Assuming that the UAV path is composed of a series of path nodes,i.e. $r=\left\{X_{i} \mid i=1,2, \ldots, n+1\right\}$, then $\alpha_{i}$ in the above equation is the vector composed of the path nodes $X_{i}$ and $X_{i+1}$.

## III. ADAPTIVE EVOLUTIONARY MULTI-OBJECTIVE ESTIMATION OF DISTRIBUTION ALGORITHMS

## A. A SIMPLE ESTIMATION OF DISTRIBUTION ALGORITHM

The Estimation of Distribution Algorithm (EDA) is a technique that utilizes statistical methods to create a probability model from which new offspring are sampled to generate new solutions. It is a method that characterizes the distribution of solutions from a macroscopic perspective of the population. One of the probability models that can be used is the Gaussian distribution model, which has good applicability.

Assuming that the population size is $P S$, with individuals $x \in R^{n}$, and the selection rate of elite individuals is $s r$, i.e., $[P S \cdot s r]$ promising individuals are selected per generation to form the elite set, the simple Gaussian Estimation of Distribution Algorithm (GEDA) can be summarized in

## Algorithm 1 The Procedure of GEDA

Input: population size $P S$, selection ratio $s r$;
1: Initialize the number of iterations $t=0$, initialize the population $P^{(t)}$;
2: Record the global optimal solution Gbest;
3: repeat
4: Select $[P S \cdot s r]$ promising individuals from population $P^{(t)}$ to form the elite set $D_{\text {elite }}^{(t)}$;
5: Update the mean $\mu^{(t)}$ and covariance matrix $C^{(t)}$ of the population distribution based on the elite set $D_{\text {elite }}^{(t)}$ according to Eq.12, Eq.13;
6: Randomly generate a new population whose population size is $P S$ by sampling from Gaussian distributions according to Eq.14;
7: Update the global best solution Gbest;
8: $t=t+1$;
9: until the stopping criterion is met;
Output: the global best solution Gbest.

Algorithm 1.

$$
\begin{aligned}
\mu^{(t)} & =\operatorname{avg}\left(D_{\text {elite }}^{(t)}\right)=\frac{1}{\lambda} \sum_{i=1}^{\lambda} s_{i}^{(t)} \\
C^{(t)} & =\operatorname{var}\left(D_{\text {elite }}^{(t)}\right)=\frac{1}{\lambda-1} \sum_{i=1}^{\lambda}\left(s_{i}^{(t)}-\mu^{(t)}\right)^{2} \\
P^{(t+1)} & =\left\{x_{i}^{(t+1)} \mid x_{i}^{(t+1)} \sim \mathcal{N}\left(s \mid \mu^{(t)}, C^{(t)}\right)\right\}
\end{aligned}
$$

## B. ADAPTIVE EVOLUTIONARY ESTIMATION OF DISTRIBUTION ALGORITHMS

A key problem encountered with most existing GEDA during optimization is the rapid reduction in variance (covariance), which can result in a loss of search diversity and premature convergence to a local optimum solution. To address this issue, this paper proposes an adaptive GEDA that adjusts the covariance matrix according to the number of iterations. This approach not only allows the covariance to be scaled in different directions but also enables the algorithm to better capture the optimization problem's structure.

## 1) ADAPTIVE SELECTION RATE

In the basic GEDA, the mean and covariance of the next generation are derived from the elite set, and the covariance matrix of the next generation is estimated by introducing more promising individuals to improve the sampling range of the probability distribution. Specifically, considering a population size $P S$, the mean vector of the probability distribution is estimated by selecting $\lambda=[s r-P S]$ promising individuals from the population, where $s r$ is the selection rate used to estimate the mean vector; the covariance of the probability distribution is estimated by selecting $\lambda^{\prime}=[c s-P S]$ promising individuals from the population, where $c s$ is the selection rate used to estimate the covariance and is usually greater than $s r$. In this manner, it is possible to expand the covariance by selecting more promising individuals to be involved in the covariance estimation.

As illustrated in Figure 2, the populations are sorted from the highest to lowest adaptation value and $\lambda$ promising individuals are selected to form $D_{\text {elite }}^{(t)}$, while the mean vector is estimated according to Eq.12. Unlike most existing GEDAs, the proposed selection rate scaling method selects $\lambda^{\prime}$ best individuals to form the promising individual set $D_{\text {elite }}^{(t)}$, and uses it to estimate the covariance according to Eq.13. Due to the involvement of more promising individuals in covariance estimation, a larger sampling range of the distribution model is obtained. On one hand, the availability of a more diverse sampling offspring is highly beneficial for the population to avoid falling into local areas. On the other hand, it may also increase the probability of producing sampled offspring in better areas; thus, convergence can be enhanced to a certain degree.

In the proposed selection rate scaling method, the study has found that the choice of the $(c s, s r)$ parameter of the selection rate is crucial, and using a too large or too small value may
not yield satisfactory results. A too large $c s$ may result in oversampling of the probability distribution, particularly in the late stages of evolution, which can make the population too diverse. Conversely, a too small $c s$ may result in too much concentration of the sampling, leading to slow evolution in the early stages of evolution. Similarly, $s r$ as the selection rate of the mean vector also has a significant impact on the convergence speed of the algorithm. An excessively large $s r$ may result in too many promising individuals when estimating the mean vector, which may move the estimated mean vector further away from the optimal value. Conversely, a too small $s r$ may cause the algorithm to lack search diversity and be prone to premature convergence. Therefore, it is essential to dynamically adjust $c s$ and $s r$ during the evolutionary process, making the algorithm more diverse in the early stages of evolution and more convergent in the later stages of evolution. Based on the above analysis, an adaptively adjusted selection rate is designed in this paper as follows:

$$
\begin{aligned}
& c s=1-\left(1-s r_{\min }\right)\left(\frac{t}{t_{\max }}\right)^{2} \\
& s r=s r_{\max }-\left(s r_{\max }-s r_{\min }\right)\left(\frac{t}{t_{\max }}\right)^{0.1}
\end{aligned}
$$

where $s r_{\text {max }}$ and $s r_{\text {min }}$ are the maximum and minimum selection rates of the mean vector, $t_{\max }$ is the maximum number of iterations of the algorithm, and $t$ is the current number of iterations.

As indicated by Eq. 15 and Eq. 16, both $c s$ and $s r$ decrease as the number of iterations increases. Specifically, $c s$ decreases from 0.1 to $s r_{\min }$, which implies that early in the iteration, most individuals in the population are involved in the estimation of covariance, expanding the search space of the algorithm. Including a large number of promising individuals early in the iteration is also helpful for capturing the precise structure of the optimization problem. In the later stages of the iteration, $c s$ decreases to $s r_{\min }$, indicating that the sampling of offspring will be more focused in the vicinity of the mean. This improves the quality of the population's search area, thus increasing the accuracy of the solution. Overall, the adaptive selection rate scaling scheme achieves a balance between population diversity and convergence, meeting the algorithm's design expectations.

## 2) ADAPTIVE EVOLUTION OF THE COVARIANCE MATRIX

In the basic GEDAs, the covariance matrix of the elite set needs to be computed for each generation to update the next generation of populations. For now, we assume that the aggregate contains enough information to reliably estimate the covariance matrix of the aggregate. This study can re-estimate the original covariance matrix $C^{(t)}$ using the totality of the elite set $D_{\text {elite }}^{(t)}$.

$$
C_{\text {emp }}^{(t)}=\frac{1}{\lambda-1} \sum_{i=1}^{\lambda}\left(s_{i}^{(t)}-\frac{1}{\lambda} \sum_{j=1}^{\lambda} s_{j}^{(t)}\right)\left(s_{i}^{(t)}-\frac{1}{\lambda} \sum_{j=1}^{\lambda} s_{j}^{(t)}\right)^{T}
$$

![img-1.jpeg](img-1.jpeg)

FIGURE 2. The visual structure of selection rate scaling strategy.
where $x_{i}^{(t)} \in D_{\text {elite }}^{(t)}(i=1, \ldots, \lambda)$, and the empirical covariance matrix $C_{\text {emp }}^{(t)}$ is an unbiased estimate of $C^{(t)}$. We can obtain $E\left(C_{\text {emp }}^{(t)}\right)=C^{(t)}$ only when the individuals within the elite set $D_{\text {elite }}^{(t)}$ are all random variables (not true samples). Considering this, to obtain a more accurate original covariance matrix $C^{(t)}$, we need to maximize the number of individuals sampled $\lambda$. However, this can significantly reduce the search speed of the algorithm. As a remedy, we add information from previous generations for correction when estimating the original covariance matrix $C^{(t)}$. A simple example is as follows: after a sufficient number of generations, a reliable estimate of the current covariance matrix is replaced by the average of the empirical covariance matrix estimated over all generations; refer to Eq. 18 .

$$
C^{(t+1)}=\frac{1}{t+1} \sum_{i=0}^{t} C_{e m p}^{(i+1)}
$$

where $C_{\text {emp }}^{(i+1)}$ denotes the empirical covariance matrix for generation $i+1$; refer to Eq.18. It denotes the mean estimate of all covariance matrices for the previous $t$ generations, but with the same weights for each generation. To assign higher weights to the most recent generations, this paper introduces the Polyak averaging method for exponential smoothing. Choosing $C^{(0)}=I$ as the unit matrix and setting the learning rate to $0<c_{\lambda} \leq 1, C^{(t+1)}$ can be expressed as

$$
C^{(t+1)}=\left(1-c_{\lambda}\right) C^{(t)}+c_{\lambda} C_{\text {emp }}^{(t+1)}
$$

where $c_{\lambda} \leq 1$ is used to update the learning rate of the covariance matrix. For $c_{\lambda}=1$, no prior information is retained and $C^{(t+1)}=C_{\text {emp }}^{(t+1)}$; for $c_{\lambda}=0$, no learning occurs and the covariance is kept constant $C^{(t+1)}=C^{(0)}$. The selection of $c_{\lambda}$ is crucial; too small a value leads to a slow learning rate and too large a value leads to learning failure due to degradation of the covariance matrix [26]. However, the setting of $c_{\lambda}$ also depends on the optimization objective function, and a good
choice is that $c_{\lambda}$ should be approximated to first order by $\lambda / n^{2}$ so that $c_{\lambda} \approx \min \left(1, \lambda / n^{2}\right)$ is a suitable choice.

## C. MULTI-OBJECTIVE GEDA

The optimization model constructed in Section II is a multi-objective optimization model, in which the optimization objectives are composed of four optimization functions. In general, objectives in high-dimensional multi-objective optimization problems are often conflicting or not directly related, requiring the decision maker to focus on the required solution from the Pareto solution set obtained from the algorithm optimization according to the actual requirements. A Pareto solution set is a set of high-performance solutions that are not dominated by each other and that contain solutions with outstanding performance on each objective, as well as solutions with excellent overall performance on multiple objectives. A high-dimensional multi-objective optimization problem with $n(n>3)$ objectives can be formulated as follows:

$$
\operatorname{minimize} F(x)=\left(f_{1}(x), f_{2}(x), \ldots, f_{n}(x)\right)^{T}
$$

where $x=\left(x_{1}, x_{2}, \ldots, x_{m}\right) \in X$ is referred to as the decision variable; $f_{1}(x), f_{2}(x), \ldots, f_{n}(x)$ is the $n$ objective function; $X$ is the decision space, and $m$ is the dimensionality of the decision variable.

Compared to the GEDA with a single optimization objective, the largest difference lies in the selection of the elite set $D_{\text {elite }}$ and the selection of the offspring population. The selection of the elite set is based on the number of population generations to select more suitable individuals. It is expected that the members of the elite set will be more convergent in the early iterations and more diverse in the later iterations. In contrast, the selection of the offspring population is no longer based solely on the merits of a single optimization objective. Environmental selection must also consider multiple objectives to select more diverse populations in the non-dominated solution set. This article proposes the following strategy for both parts of the process.

## 1) ELITE SELECTION STRATEGIES BASED ON COMPREHENSIVE INDIVIDUAL EVALUATION

In high-dimensional multi-objective optimization algorithms, the diversity and convergence of individuals are significant indicators of individual merit. In the proposed elite selection strategy, the convergence and diversity of each individual are first comprehensively evaluated, and then the elite individuals are selected by ranking according to their comprehensive evaluation value. Assuming that the population size $P$ is $N$, i.e., $P=\left\{p_{1}, p_{2}, \ldots, p_{N}\right\}$, the comprehensive evaluation indicators of convergence and diversity for the individuals $p_{i}$ in population $P$ are:

$$
\begin{aligned}
F_{\text {cad }}\left(p_{i}\right)= & {\left[1+\operatorname{rand}(0.8,1) \cdot M \cdot\left(\frac{t}{t_{\max }}\right)^{\theta} \cdot F_{d}\left(p_{i}\right)\right] } \\
& \cdot\left(1-F_{c}\left(p_{i}\right)\right)
\end{aligned}
$$

The functions $F_{d}$ and $F_{c}$ denote the diversity and convergence of the individual $p_{i}$, the formula of which is referred to in [13]; $M$ denotes the number of optimization objectives; $t$ and $t_{\max }$ denote the number of iterations of the current run of the algorithm and the maximum number of iterations of the algorithm; $\theta$ is the equilibrium influence parameter of the number of iterations. To prevent overfitting, a random number rand $(0.8,1)$ is added to the individual evaluation process.

Referring to Eq. 21, in the early stages of the algorithm, when $t$ is small, the diversity index has less influence on individuals, and the convergence index has more influence on evaluating the merit of individuals, which results in the individuals in the early populations of the algorithm converging quickly. Conversely, in the later stages of the algorithm, as $t$ becomes increasingly large, the diversity index takes on more weight in evaluating individuals, and the algorithm tends to select individuals with better diversity.

## 2) NONDOMINATED SORTING ALGORITHMS BASED ON REFERENCE POINTS

As the number of objectives increases, common multiobjective optimization algorithms such as NSGA-II [27] tend to generate a large number of nondominated solutions during the optimization process. This results in insufficient selection pressure to guide the individuals towards the desired point. To address this issue, Deb et al. proposed the nondominated sorting genetic algorithm, the third version (NSGA-III) [23]. Unlike the NSGA-II algorithm, the NSGA-III algorithm uses a reference point strategy instead of a congestion calculation strategy to solve the problem of complicated congestion calculation among a large number of nondominated solutions in a high-dimensional space.

The reference point-based nondominated sorting algorithm begins with a nondominated sort. When selecting the next generation of populations, priority is given to the first level of the nondominated solution set, followed by the second level of the undominated set, and so on until the number of offspring populations is filled. If the individuals in a particular nondominated layer do not need to be selected in their
![img-2.jpeg](img-2.jpeg)

FIGURE 3. Diagram of reference points.
entirety, this layer is marked as a critical layer. This algorithm uses a reference point-based approach to intercept individuals in the critical layer. The main components in the selection process include adaptive population normalization, mapping relationships between population individuals and reference points, and small habitat conservation operations.

As shown in Figure 3, the reference points are a set of points uniformly distributed in the decision space. The connection between these points and the ideal points partitions the decision space uniformly, and the similar population individuals in the decision space are then corresponded to one by one. Finally, based on the idea of small habitat preservation, the points whose reference points correspond to less are selected as the basis for the selection of population individuals in the critical layer. This algorithm achieves population diversity and effectively mitigates the issue of quick convergence leading to a local optimum solution.

## D. ALGORITHM PROCESS

The proposed adaptive evolutionary multi-objective estimation of distribution algorithm (AEMO-EDA) is outlined in Algorithm 2, combining the three schemes described above. Initially, the UAV information, environmental parameters, the number of track segments, and other algorithm parameters are determined and initialized. These parameters include the maximum and minimum selection rates of the mean vector $s r_{\max }, s r_{\min }$, the algorithm's maximum number of iterations $t_{\max }$, the learning rate parameter $c_{\lambda}$ for updating the covariance matrix, and the balance impact parameter $\theta$ for the number of iterations of the individual comprehensive evaluation. Furthermore, the number of iterations is initialized as $t=0$, and the drone population $P^{(t)}$ is initialized. The global best solution Gbest is obtained (lines 1-3). Subsequently, the algorithm enters the main iterative loop for evolution (lines 512). In this loop, the optimal set of solutions is recorded for each generation, and the optimal set of solutions is updated. Finally, the global optimal solution set is output at the end of the loop (line 13).

## Algorithm 2 The Procedure of AEMO-EDA

Input: UAV information, environmental parameters, population size $P S$;
1: Initialize the number of iterations $t=0$;
2: Initialize the population $P^{(t)}$ randomly and evaluate their fitness;
3: Obtain the global best solution Gbest and store the current population;
4: while $t<t_{\max }$ do
5: Calculate the mean vector selection rate $s r$ according to Eq.15; calculate the covariance matrix selection rate $c s$ according to Eq.16;
6: Sorting of individual comprehensive evaluation indicators for the population $P^{(t)}$ according to Eq.21;
7: Select $[P S \cdot s r]$ outstanding individuals from the population according to the ranking and calculate the mean vector $\mu^{(t)}$ according to Eq.12;
8: Select $[P S \cdot c s]$ outstanding individuals from the population according to the ranking and calculate the covariance matrix $C^{(t)}$ according to Eq.19;
9: Randomly sample $P S$ new individuals based on the estimated multivariate Gaussian model, evaluate their fitness, and store them;
10: Select $P S$ better individuals by nondominated sorting algorithms based on reference points to form the parent population $P^{t+1}$ for the next generation;
11: Update the global best solution Gbest;
12: $t=t+1, P^{t}=P^{t+1}$;
13: end while
Output: the global best solution Gbest.

In Algorithm 2, a cross-generational individual selection strategy is employed for the parent population to improve the quality of the sampled progeny. Specifically, sampled offspring from the previous generation are combined with sampled offspring from the current generation, and the best $P S$ individuals are selected as the parent population for the next generation to estimate the probability distribution model. This strategy enables the construction of the probability distribution model using historical information from the previous generation [28], [29], [30]. The size of the global best solution set Gbest is set to around $P S / 2$, and if the number of nondominated sorted first levels is greater than $P S / 2$, then all individuals in the first level are used as the global best solution set Gbest.

## E. BENCHMARK PROBLEM TEST

To test the effectiveness of AEMO-EDA, the DTLZ and WFG benchmark problems were used. For each problem, the number of optimization targets was chosen to be $3,6,8,10$, and 15 . In the DTLZ problem, the number of variables was set to $(M+k-1)$, where $M$ is the number of optimization targets, and the parameter $k$ was set to 5 for DTLZ1 and 10 for DTLZ2, DTLZ3, and DTLZ4. For the WFG prob-
lem, the location parameter $k$ was set to $2 \times(M-1)$, and the distance parameter was set to 20 . The evaluation metric used in this study was the inverse generation distance (IGD) metric, and the performance of AEMO-EDA was compared with NSGA-III [23], reference vector guided evolutionary algorithm (RVEA) [31], and generation-based fitness evaluation in NSGA-III (NSGAIII-GBFE) [13]. The final results are shown in Table 1.

Table 1 presents the results of four algorithms on seven benchmark problems with different numbers of objectives. DTLZ1 evaluates the ability of the multi-objective algorithm to converge to the PF plane, DTLZ2 to DTLZ3 test the ability of the algorithm to handle problems with different shapes and distributions, and the three benchmark functions of WFG test the ability of the algorithm to handle problems with higher variable fusion. The cells in bold indicate that the IGD value of the algorithm is the smallest among the four algorithms, indicating that the algorithm produces the best solutions. Based on the results of the experiments, the following conclusions can be drawn:
(1) AEMO-EDA has a significant advantage in handling 5 and 8 dimensional problems. It outperforms other algorithms for the 5 dimensional problems and achieves optimal results for four sets of benchmark problems in the 8 -dimensional problems, demonstrating its better performance in handling multi-objective optimization problems in 5 and 8 dimensions.
(2) AEMO-EDA also demonstrates good performance in the other three dimensions. By comparing the solutions obtained by this algorithm with those obtained by other algorithms, it can be seen that the algorithm consistently produces optimal or near-optimal results for each problem, making it highly competitive among several multi-objective optimization algorithms. Therefore, AEMO-EDA can effectively solve high-dimensional multi-objective optimization problems.

## IV. SIMULATION AND RESULTS ANALYSIS

## A. INDIVIDUAL CODING

The AEMO-EDA is a heuristic evaluation algorithm that requires the design of variables and their coding to form populations based on the actual problem, before solving the optimization problem.

Let us assume that the multi-UAV path planning problem involves $T$ UAVs, and that the path route of each UAV is divided into $H$ path segments, where each UAV's path is composed of $H+1$ sequential path points. Therefore, the sum of all UAVs' paths constitutes the independent variable of the problem, which represents an individual in the population. The population can be represented by the matrix $X=\left[X_{1}, X_{2}, \ldots, X_{N}\right]^{T}$, where $N$ is the population size, and the individuals $X_{i}$ in the population are encoded as shown in Figure 4.

The paths of $T$ UAVs, denoted by $r_{1}, r_{2}, \ldots r_{T}$, are encoded in the same way as $r_{1}$, and are composed of a

TABLE 1. Comparison results of AEMO-EDA with three multi-objective optimization algorithms.

![img-3.jpeg](img-3.jpeg)

FIGURE 4. Schematic diagram of individual encoding.
sequence of coordinates in the $x, y, z$ directions of the $H+$ 1 path points. The individual $X_{i}$ is a vector of size $T \times(H+1)$, consisting of the $T$ paths $r_{1}, r_{2}, \ldots r_{T}$. When an individual $X_{i}$ does not satisfy the constraints, it is marked as ineligible to enter the next environmental selection operation.

## B. SIMULATION EXPERIMENT

In order to verify the effectiveness of the multi-UAV path planning model and the efficiency of the proposed algorithm, this paper conducted simulation experiments by setting up scenarios, models, and algorithm data. All the experiments
were performed on a system with an Intel(R) Core(TM) i510400F CPU@2.90GHz, 16GB memory, running Windows 10 operating system, and using Matlab R2017a as the simulation tool.

The UAV flight environment was simulated using a randomly generated digital elevation map with dimensions of $10 \mathrm{~km} \times 10 \mathrm{~km} \times 0.4 \mathrm{~km}$. The scenario consists of two UAVs executing a mission simultaneously, with their initial positions set to $[0,0,0.05] \mathrm{km}$ and $[0,0.12,0.05] \mathrm{km}$, respectively. The mission execution position is $[10,10,0.05] \mathrm{km}$. There are also three enemy threat areas in addition to the terrain constraints. The 3D view of the mission execution area is shown in Figure 5.

Multi-UAV path planning model parameters are set as shown in Table 2 and Table 3.

Furthermore, in order to verify the effectiveness of the AEMO-EDA for the multi-UAV path planning problem, the population size is set to 500 and the maximum number of iterations is set to 350 for 2 UAVs, and to 1000 and 700 for 4 UAVs. The related parameters are shown in Table 4.

![img-4.jpeg](img-4.jpeg)

FIGURE 5. A 3D view of the UAV flight environment.

TABLE 3. UAV parameter setting.

TABLE 3. Environmental threat parameter setting.

TABLE 4. AEMO-EDA related parameter settings.


After the simulation, the results of the multi-UAV path planning model using AEMO-EDA are shown in Figure 6. It should be noted that the model is a multi-objective optimization problem with four optimization objectives, and the amount of non-dominated solutions in the optimal set can be very large. Therefore, Figure 6 shows the simulation results with 25 solutions randomly selected from the optimal set, from which the mission operator selects the appropriate path. Subplots (a) and (c) show the simulation results for two UAVs, while subplots (b) and (d) show the simulation results for four UAVs. Sub-plots (a) and (b) are views in the 3D planning space, which allows visualization of the UAV path, while subplots (c) and (d) are views in the planning space from an overhead perspective, which allows the junction of the path route with mountain obstacles and
threat areas to be clearly discerned. The results in Figure 6 demonstrate that the AEMO-EDA is effective in solving the multi-UAV cooperative path planning problem, and is able to plan multiple paths for each UAV that satisfy the target requirements.

## C. SENSITIVITY ANALYSIS OF ALGORITHM PARAMETERS

The AEMO-EDA proposed in this paper employs a selection rate that is adaptable through an estimation of distribution method. The selection rate of each generation is influenced by the maximum and minimum selection rates of the mean. In this section, we perform parameter sensitivity analysis experiments for the two UAV cases by choosing different values of $s_{r_{\text {min }}}$ and $s_{r_{\text {max }}}$. The other relevant parameter settings remain the same as in the previous section. Table 5 presents the results for different maximum-minimum selection rates. The values are calculated based on the IGD metric, which assesses the convergence and diversity of the optimal solution set under this parameter. It should be noted that to ensure the evolution of the population, the table only investigates the case where the minimum selection rate of the mean is within 0.6 , where the selection rate of the mean and variance of the algorithm will always be equal when $s_{r_{\text {min }}}=s_{r_{\text {max }}}$, i.e., the optimization strategy is not used.

According to Table 5, the following conclusions can be drawn.
(1) Moderate settings of the parameter $s_{r_{\text {max }}}$ result in better performance. The results of AEMO-EDA are not better with either a larger or a smaller $s_{r_{\text {max }}}$. When $s_{r_{\text {min }}}$ is small, $s_{r_{\text {max }}}$ is best at values equal to 0.45 and 0.6 , much higher than when $s_{r_{\text {max }}}$ is 0.15 and 0.9 . The larger the covariance, the more dispersed the probability distribution for population sampling, and the greater the diversity of the population evolution. A large value of $s_{r_{\text {max }}}$ $\left(s_{r_{\text {max }}}=0.9\right)$ leads to low population convergence and failure to converge to the optimal solution. These experimental results verify the analysis of the algorithm in Chapter III.
(2) The selection rate scaling strategy is effective. Comparing all values of $s_{r_{\text {max }}}$, the IGD values when $s_{r_{\text {min }}}=$ $s_{r_{\text {max }}}$, i.e., without the selection rate scaling strategy, are higher than those when $s_{r_{\text {min }}}<s_{r_{\text {max }}}$, indicating that the selection rate with increasing variance is beneficial for the algorithm to find the optimal solution set. It is worth noting that as the value of $s_{r_{\text {min }}}$ gradually increases, the improvement of the result by increasing $s_{r_{\text {max }}}$ also gradually decreases. It can be seen that a too large $s_{r_{\text {min }}}$ will lead to a high selection rate of the mean value, making the population search direction too large to converge to the optimal solution.
In summary, the proposed AEMO-EDA algorithm performs best when $s r_{\min }=0.15$ and $s r_{\max }=0.45$. Furthermore, the experimental results suggest that the higher the value of the parameter $s r_{\max }$ is when $s r_{\min }$ is fixed, the better the algorithm performance.

![img-5.jpeg](img-5.jpeg)
(c) Top view of two UAVs
![img-6.jpeg](img-6.jpeg)
(d) Top view of four UAVs

FIGURE 6. UAV path simulation results.

TABLE 5. The IGD values for different mean selection rate parameter settings.


## D. ALGORITHM ABLATION EXPERIMENT

In this paper, the proposed AEMO-EDA algorithm not only utilizes an adaptive deflation rate strategy, but also incorporates an adaptive evolutionary covariance matrix and an integrated individual evaluation strategy. The effectiveness of the adaptive deflation rate approach has been demonstrated in the previous section through parameter analysis experiments. In this section, ablation experiments will be conducted for the other two strategies, with two UAVs. The algorithm will be experimentally explored for the removal of these two strategies separately, while all parameters of the algorithm are set as in the above experiments. The IGD metric will be used
as the criterion for the algorithm, and the experimental results of the ablation experiment are shown in Figures 7.

Figure 7 shows the comparison results of the ablation experiments. Based on the figure, the following conclusions can be drawn:
(1) The covariance matrix adaptive evolution strategy is effective in enhancing the convergence of the algorithm. The algorithm without this strategy shows a rapid decrease in convergence rate when the number of iterations exceeds 50. As discussed in Chapter III, the covariance matrix adaptive evolution strategy increases

![img-7.jpeg](img-7.jpeg)

FIGURE 7. Comparison results of ablation experiments.
the historical information of the covariance matrix, improves the accuracy of the covariance matrix, determines the optimal search direction, and thus improves the convergence performance of the algorithm.
(2) The individual comprehensive evaluation strategy is effective in accelerating the convergence of the algorithm. As shown in Figures 7, the convergence speed of AEMO-EDA is significantly higher than that of the algorithm that does not use this strategy. This is because the individual comprehensive evaluation strategy increases the convergence of the algorithm in the each iteration and speeds up the convergence of the algorithm.

## E. ALGORITHM COMPARISON ANALYSIS

To demonstrate the applicability and superiority of the AEMO-EDA proposed in this paper in solving the multi-UAV collaborative path planning problem, we compared the path planning results with the NSGAIII-GBFE [13], the standard NSGA-III [23], and the RVEA [31]. We used the same experimental environment settings for each algorithm as in the previous experiments, including the number of targets, population size, and several algorithm iterations. After the simulation, we obtained box plots of the final optimal solution sets obtained by the four algorithms under each objective, as shown in Figure 8.

As most of the optimized multi-UAV cooperative paths have 0 threat cost, we did not present box plots for this objective. Moreover, AEMO-EDA, RVEA, NSGA-III, and NSGAIII-GBFE optimized paths with zero spatial threat cost accounted for $88.61 \%, 79.11 \%, 74.27 \%$, and $82.33 \%$ of their total paths, respectively. These results show that AEMO-EDA is significantly better than the other three algorithms in avoiding enemy threats. Additionally, the box plots of the four algorithms in Figure 8 reveal that the median value of the optimization results of AEMO-EDA is significantly better than the other three algorithms in terms of both path cost and

TABLE 6. Performance evaluation indicators comparison results.


terrain concealment index when dealing with the multi-UAV collaborative path planning problem, and the optimal and inferior values of its optimization results are also better than those of the other three algorithms.

As the AEMO-EDA algorithm proposed in this paper focuses more on the convergence of solutions in the early stage of the algorithm and more on the diversity of solutions in the later stage of the algorithm, the length of the box plot can reflect the diversity of the optimization results to some extent. From the figure 8, it can be seen that in terms of terrain concealment and spatial synergy, the algorithm in this paper produces a better diversity of results compared to the other three algorithms. When comparing the optimal values and median values produced by the algorithm, we can see that the convergence of the algorithm in this paper is better for the four objectives. Since the solutions generated by the high-dimensional multi-objective optimization algorithm are Pareto sets, it is unlikely that the solutions generated will perform optimally on all objectives simultaneously. Therefore, the decision maker may choose the appropriate solution according to the actual requirements.

The algorithms were evaluated using the hypervolume evaluation index (HV) [32] and the IGD evaluation index [33], as shown in Table 6. These evaluation metrics reflect the convergence and population distribution of the algorithms, as well as the average running time of the algorithms $\left(\right.$ time $\left._{\text {avg }}\right)$.

HV strictly adheres to the Pareto dominance principle and has the strongest monotonicity and a good evaluation effect among many evaluation metrics. A larger value of HV indicates better convergence and distribution of the algorithm. IGD indicates the average of all distances between the nondominated solution set $P F_{\text {known }}$ obtained by the algorithm and the true optimal Pareto front $P F_{\text {true }}$. A smaller value of IGD indicates better performance of the algorithm.

Among the four algorithms for solving the multi-UAV collaborative path planning problem, all metrics of the AEMO-EDA are optimal, except for the average running time, which is slightly inferior to that of the RVEA. This shows that the algorithm has a significant advantage in the convergence and distribution of the population. In summary, this multi-UAV collaborative path planning model based on high-dimensional multi-objective optimization can provide effective path planning, while the improved AEMO-EDA algorithm has better convergence and versatility in solving this model.

![img-8.jpeg](img-8.jpeg)

FIGURE 8. Comparison of multi-algorithm simulation results.

## V. CONCLUSION

This paper presents a model for the path planning problem of multiple UAVs in complex mountainous areas under adversarial conditions between the enemy and the agent. Four main optimization objectives are considered, namely the UAV path cost, spatial concealment, spatial threat cost, and spatial synergy performance, which are essential in line with the tactical conditions and context when UAVs are employed.

A multi-objective evolutionary algorithm based on a distribution estimation algorithm is proposed for the multi-objective optimization problem of multi-UAV collaborative path planning. The algorithm adjusts the selection rates of the mean and covariance adaptively according to the number of iterations to improve the performance of the solution distribution. It also adds historical information to increase the global search capability of the solution during covariance matrix sampling and an individual comprehensive evaluation method to improve the convergence and diversity of the algorithm, allowing the algorithm to obtain good performance in all aspects.

The AEMO-EDA is applied to the multi-UAV collaborative path planning problem, and the results show that it has certain advantages in terms of convergence and population distribution and achieves better results in the solution of UAV path planning problems, indicating wide applicability and extension potential. After simulation, the UAV successfully avoids the enemy threat within a shorter path, while also maintaining certain spatial collaborative performance to obtain a better planning route.

Future work will focus on improving the model for the temporal synergy of multi-UAV paths and simulating multi-UAV collaborative path planning for more complex mission spaces to bring the model closer to real-world scenarios. Additionally, the AEMO-EDA algorithm will be analyzed further to explore whether further improvements can be made in terms of population diversity maintenance and whether better results can be achieved in high-dimensional optimization problems.
