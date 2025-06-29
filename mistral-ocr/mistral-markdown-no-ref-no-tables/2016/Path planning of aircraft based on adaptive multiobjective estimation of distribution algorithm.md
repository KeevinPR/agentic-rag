# Path Planning of Aircraft Based on Adaptive Multiobjective Estimation of Distribution Algorithm 

Tao Lin<br>School of Astronautics, Harbin Institute of Technology<br>Harbin 150001, China<br>laestsea2005@163.com

Ke Zhang<br>Beijing Electro-mechanical Engineering Institute<br>Beijing 100074, China<br>zhangkehit6@yahoo.com

Naigang Cui<br>School of Astronautics, Harbin Institute of Technology<br>Harbin 150001, China<br>cui_naigang@163.com<br>Zhenbiao Tu and Hu Zhang<br>Beijing Electro-mechanical Engineering Institute<br>Beijing 100074, China<br>jxzhanghu@126.com


#### Abstract

Path planning is able to effectively improve the survival probability and operational efficiency of a combat aircraft. The essence of path planning of the aircraft is a multiobjective optimization problem. To deal with this problem efficiently, this paper proposes an adaptive multiobjective estimation of distribution algorithm named as AMEDA. In AMEDA, a novel clusteringbased multivariate Gaussian sampling strategy is designed. At each generation, a clustering analysis approach is utilized to discover the distribution structure of the population. Based on the distribution information, with a certain probability, a local or a global multivariate Gaussian model (MGM) is built for each solution to sample a new solution. A covariance sharing strategy is designed in AMEDA to reduce the complexity of building MGMs, and an adaptive update strategy of the probability that controls the contributions of the two types of MGMs is developed to dynamically balance exploration and exploitation. Experiments show that AMEDA is efficient to deal with the path planning model of the aircraft. Meanwhile, it is convenient to provide multiple flight paths with different characteristics for the decision makers.


## I. InTRODUCTION

The characteristic of modern warfare has been gradually changed from mass destruction to accurate and effective strike. For a combat aircraft, a good flight path is able to effectively improve its survival probability and operational efficiency. Therefore, path planning is very important for the aircrafts. Typical path planning approaches include [1]: A* search algorithm, dynamic programming algorithm, artificial potential filed algorithm and evolutionary algorithms (EAs), etc. Especially in recent years, with the rapid development of EAs and their wide applications in dealing with complicated engineering optimization problems, the scholars have carried out a lot of research works on path planning of aircrafts based on EAs [1], [2]. EA [3] is a type of nature inspired global searching algorithm, its solving operations include crossover, mutation and selection, etc. Since the operations do not depend on the properties of the problems to be solved, thus EA is quite suitable to be applied to deal with the complicated optimization problems which are hard for the traditional deterministic optimization approaches.

Since the path planning of aircrafts usually requires to take multiple conflicting objectives into consideration [1], such as, the shortest total length of flight path, the lowest flight altitude, and the successful avoidance of all the threats, etc., the essence
of aircrafts' path planning is a complicated multiobjective optimization problem (MOP). However, at present, most of the existing works usually use aggregation techniques to transform multiple objectives into a single objective for solving the problems [2], and typical aggregation techniques are weighted sum approach and constraint approach. Actually, the aggregation techniques have their own shortages: (a) the solutions of the MOPs obtained by the aggregation techniques greatly depend on the adopted aggregation parameters, such as the weights for each objective and the constraint parameters, etc.; (b) for an actual path planning model, the aggregation parameters are often hard to be set, especially when the mission information is unknown, the parameter settings are much harder; (c) a suite of aggregation parameters can only yield one flight path, but during decision making, the decision makers often hope to have more paths with different features for their decision. Therefore, to improve the shortages of aggregation techniques, it is necessary to study much more efficient path planning approaches of the aircrafts. Multiobjective evolutionary algorithm (MOEA) [4], [5], [6] is a type of EAs which can deal with MOPs efficiently. Since MOEA is able to obtain a set of solutions for a MOP through a single run, that is to say, it is able to yield multiple flight paths for a path planning model though a single run, consequently, more and more scholars start to perform path planning using the MOEAs [2], [7]. Similarly, this paper proposes to study path planning based a multiobjective estimation of distribution algorithm (MEDA) [8].

Estimation of distribution algorithm (EDA) [9] is a specialized paradigm in EAs. An EDA does not adopt the well-known traditional genetic operations (e.g. crossover and mutation). Instead, it explicitly extracts globally statistical information from the selected solutions, and builds a posterior probability distribution model of promising solutions based on the extracted statistical information. New solutions are sampled from the model thus built. In the genetic-based MOEAs, the genetic operations may disrupt the building of strong schemas of a population, and thus movement towards optimal is extremely difficult to predict. However, MEDAs are able to predict the locations or patterns of the PFs or to predict the favorable movements in the search spaces. By regulating the search to follow the discovered or predicted favorable movement

directions, promising solutions can be generated better [10]. A variety of MEDAs have been proposed and they yielded lots of encouraging results [8].

Although MEDAs have been studied by more and more scholars, they have not completely lived up to their a priori expectations until now. This can be attributed to a number of different causes, and three of them are the incorrect treatment of population outliers; the loss of population diversity, and too much computational effort being spent on finding an optimal population model [11]. To improve the effectiveness of path planning, this paper modifies the sampling strategy for generating new solutions, and proposes an adaptive multiobjective estimation of distribution algorithm (AMEDA) to address the path planning model. The features of AMEDA include:

- A novel clustering-based multivariate Gaussian sampling (CMGS) strategy is designed. In CMGS strategy, a clustering analysis approach is applied to cluster the population. To model the population more accurately and to enhance the searching ability of AMEDA, with a certain probability, a local multivariate Gaussian model (MGM) or a global MGM is built for each solution based on the clusters to sample a new solution. To reduce the modeling complexity, the solutions in the same cluster share the same covariance matrix to build MGMs.
- An adaptive update strategy of the probability that controls the contributions of local and global MGMs is developed. In the strategy, the control probability is adaptively updated at each generation according to the reproduction utility of the two types of MGMs over the last certain generations, so that the balance between exploration and exploitation can be dynamically maintained.
The rest of this paper is organized as follows. Section II introduces the path planning model. Section III describe the proposed AMEDA in detail. Section IV presents the experimental results of applying AMEDA to conduct path planning. The paper is concluded in Section V.


## II. Path Planning Model of Aircraft

Path planning model of an aircraft includes representations of terrain and threats, design of optimization objectives, constraint conditions and optimization variables.

## A. Representations of Terrain and Threats

1) Original Digital Terrain: Eq.(1) is used to simulated the original digital terrain.

$$
\begin{aligned}
z_{1}(x, y)= & \sin (y+a)+c \cos \left(d \sqrt{y^{2}+x^{2}}\right)+ \\
& b \sin (x)+e \sin \left(e \sqrt{y^{2}+x^{2}}\right)+f \cos (y)
\end{aligned}
$$

where $x$ and $y$ represent horizontal and vertical coordinates of a point in the horizontal plane, respectively, and $z_{1}$ represents terrain altitude corresponding to point $(x, y)$. Five constants, including $a, b, c, d, e, f$ are the terrain coefficients. Through adjusting the terrain coefficients, it is able to generate a variety of terrains with different features. The simulated terrains can be utilized as the explored terrain to provide basic data for the aircraft path planning.
2) Equivalent Terrains of Threats: During the flight, aircrafts usually encounter a variety of threats including peaks, enemy defense areas, etc. In order to conduct path planning conveniently, all the threats are transferred into peak terrains and contained in the path planning model of this paper. Eq. (2) are adopted to yield peak terrains.

$$
z_{2}(x, y)=\sum_{i=1}^{k} \mathcal{H}(i) \exp \left(-\frac{\left(x-\mathcal{X}_{c}(i)\right)^{2}}{\mathcal{X}_{t}(i)}-\frac{\left(y-\mathcal{Y}_{c}(i)\right)^{2}}{\mathcal{Y}_{t}(i)}\right)
$$

where $x$ and $y$ represent horizontal and vertical coordinates of a point in the horizontal plane, respectively, and $z_{2}$ represents terrain altitude corresponding to point $(x, y) . k$ is the number of peak terrains and $\mathcal{H}(i)$ is the height of peak $i . \mathcal{X}_{c}(i)$ and $\mathcal{Y}_{c}(i)$ are horizontal and vertical coordinates, respectively, corresponding to the center of peak $i . \mathcal{X}_{t}(i)$ and $\mathcal{Y}_{t}(i)$ represent profile parameters of peak $i$. Through changing the parameters in Eq. (2), it is able to simulate various equivalent terrains of threats with different number and shapes.
3) Equivalent Digital Terrain: Based on the principle of information fusion of digital terrains, the equivalent terrains of threats and the original digital terrain are fused to generate the equivalent digital terrain by Eq. (3):

$$
z(x, y)=\max \left(z_{1}(x, y), z_{2}(x, y)\right)
$$

In Eq. (3), through selecting much higher terrains, it is able to reflect the influence range of the threats more realistically. Digital terrain obtained by Eq. (3) is applied to conduct path planning directly.

## B. Optimization Objectives

Total length of flight path, flight altitude and turning angle are selected as the optimization objectives of the path planning.

1) Total Length of Flight Path: In order to save fuel and fight time, the total length of flight path of aircraft from the start point to the target point is required as short as possible. Supposing $\mathbf{p}^{0}, \mathbf{p}^{1}, \cdots, \mathbf{p}^{n}, \mathbf{p}^{n+1}$ are waypoints, thus $\mathbf{p}^{0}, \mathbf{p}^{n+1}$ represent start point and target point, respectively, $\mathbf{p}^{1}, \cdots, \mathbf{p}^{n}$ denote $n$ waypoints obtained by planning, and $\mathbf{p}^{i}=\left(x_{i}, y_{i}, z_{i}\right)^{\mathrm{T}}$ represents 3D coordinate of waypoint $i$. As a result, total length of the flight path can be expressed below:

$$
f_{1}=\sum_{i=1}^{n+1} d_{i, i-1}
$$

where $d_{i, i-1}=\left\|\mathbf{p}^{i}-\mathbf{p}^{i-1}\right\|$ represents distance between waypoints $i$ and $i-1$.
2) Flight Altitude: When the aircraft passes through enemy defense area, flying along the terrain can strengthen ground cover for it. Therefore, under the premise of satisfying required lowest flight altitude, the flight altitude of the aircraft is the lower the better. The optimization objective of the flight altitude is expressed as follows:

$$
f_{2}=\sum_{i=1}^{n} z_{i}
$$

where $z_{i}$ is the flight altitude of waypoint $i$.

3) Turning Angle: Due to the limited maneuverability of the aircraft, thus when flying, under the constraint of allowed maximum turning angle, the turning angle of the aircraft should be as small as possible. The optimization objective of the aircraft's turning angle is expressed as follows:

$$
f_{3}=\sum_{i=1}^{n}\left(1-\cos \left(\theta_{i}\right)\right)=\sum_{i=1}^{n}\left(1-\frac{\mathbf{a}_{i}^{\top} \mathbf{a}_{i+1}}{\left\|\mathbf{a}_{i}\right\| \bullet\left\|\mathbf{a}_{i+1}\right\|}\right)
$$

where $\mathbf{a}_{i}$ represents the projection of path segment $i$ on the horizontal plane, that is, $\mathbf{a}_{i}=\left(x_{i}-x_{i-1}, y_{i}-y_{i-1}\right)^{\top}$.

## C. Constraint Conditions

Due to the limitation of aircrafts design performance and according to the requirements of tactical use, aircraft is required to satisfy various constraints when flying. In this paper, constraints to be considered are as follows:

1) Allowed Highest Flight Altitude: In order to guarantee the flight safety, the aircraft must fly below a certain altitude. Supposing the allowed highest flight altitude of the aircraft is $H_{\max }$, and the flight altitude of path segment $i$ is $H_{i}$, so the constraint follows:

$$
H_{i} \leq H_{\max }, i=1, \cdots, n+1
$$

2) Required Lowest Flight Altitude: The optimization objective $f_{2}$ requires the flight altitude of aircraft to be as low as possible so as to improve penetration effect. Actually, the flight altitude is not the lower the better, since a quite low flight altitude will increase the probability of the aircraft's crash. The flight of the aircraft should be as low as possible under the condition of satisfying required lowest flight altitude. Supposing the required lowest flight altitude of the aircraft is $H_{\min }$, so the constraint follows:

$$
H_{i} \geq H_{\min }, i=1, \cdots, n+1
$$

3) Required Shortest Length of Path Segment: In general, in order to fulfill flight mission effectively, the aircraft is required to fly straightly for a certain distance before and after maneuvering. This distance is defined as the minimum step size $L_{\min }$, and the length of each path segment should be longer than or equal to $L_{\min }$, that is to say:

$$
d_{i, i-1} \geq L_{\min }, i=1, \cdots, n+1
$$

4) Allowed Maximum Turning Angle: The design performance of the aircraft determines that aircraft can only turn within the range of the predefined allowed maximum turning angle. Supposing the allowed maximum turning angle of the aircraft is $\phi$, and turning angle $i$ of the aircraft is $\theta_{i}$, thus the constraint of turning angle is as follows:

$$
\begin{aligned}
& \cos \left(\theta_{i}\right) \geq \cos (\phi), i=1, \cdots, n \\
& \cos \left(\theta_{i}\right)=\frac{\mathbf{a}_{i}^{\top} \mathbf{a}_{i+1}}{\left\|\mathbf{a}_{i}\right\| \bullet\left\|\mathbf{a}_{i+1}\right\|}
\end{aligned}
$$

5) Allowed Maximum Total Length of Flight Path: There exists a limit of allowed maximum flight distance for each type of aircraft. Supposing the maximum allowable flight distance of aircraft is expressed as $L_{\max }$. The constraint follows:

$$
\sum_{i=1}^{n+1} d_{i, i-1} \leq L_{\max }
$$

6) Allowed Maximum Climb Angle/Dive Angle: Since restricted by the restriction of longitudinal overload, the allowed maximum climb/dive ability of the aircraft is limited. The allowed maximum climb angle/ dive angle of the aircraft is supposed to be $\varphi$. The constraint follows:

$$
\frac{\left|z_{i}-z_{i-1}\right|}{\left\|\mathbf{a}_{i}\right\|} \leq \tan (\varphi), i=1, \cdots, n
$$

## D. Optimization Variables

In the path planning model of an aircraft, the variables that need to be optimized are the coordinates $(x, y, z)$ of all the waypoints. In this paper, the coordinates are directly employed to encode for the path planning. In the operations of AMEDA, each solution is represented by $\left(x_{1}, \cdots, x_{n}, y_{1}, \cdots, y_{n}, z_{1}, \cdots, z_{n}\right)^{\top}$, that is to say, each solution actually denotes a set of waypoints.

## III. PROPOSED AlGORITHMS

## A. Framework

The basic idea of AMEDA is that more MGMs are built by using a computationally cheap approach to describe the population more accurately; a number of different MGMs are employed to generate diverse new solutions, and the contributions of different types of MGMs are adaptively controlled to dynamically maintain the balance between exploration and exploitation. Algorithm 1 presents the framework of AMEDA.

## Algorithm 1 AMEDA

1: Initialize population $\mathcal{P}=\left\{\mathbf{x}^{1}, \cdots, \mathbf{x}^{N}\right\}$, control probability $\beta$.
for $t=1$ to $T$ do
Set an auxiliary archive $\mathcal{A}=\emptyset$.
Partition the population into local clusters, $\left\{\mathcal{L C}^{1}, \cdots, \mathcal{L C}^{k}\right\}=$ $\operatorname{AHC}(\mathcal{P}, K)$.
Construct a global cluster $\mathcal{G C}$.
Calculate covariances of $\mathcal{L C}^{k}$ and $\mathcal{G C}$ as $\boldsymbol{\Sigma}_{\mathrm{LC}^{k}}$ and $\boldsymbol{\Sigma}_{\mathrm{GC}}$, respectively, $k=1, \cdots, K$.
for each $\mathbf{x}^{i} \in \mathcal{P}, i=1, \cdots, N$ do
Decide a covariance matrix $\boldsymbol{\Sigma}^{i}$ for $\mathbf{x}^{i}, \boldsymbol{\Sigma}^{i}=$ $\left\{\begin{array}{ll}\boldsymbol{\Sigma}_{\mathrm{LC}^{k}} & \text { if } \operatorname{rund}()<\beta \\ \boldsymbol{\Sigma}_{\mathrm{GC}} & \text { otherwise }\end{array}\right.$
Generate a new solution $\mathbf{y}^{i}=\operatorname{SolGen}\left(\boldsymbol{\Sigma}^{i}, \mathbf{x}^{i}\right)$.
Store the new solution $\mathcal{A}=\mathcal{A} \cup\left\{\mathbf{y}^{i}\right\}$.
end for
Update the population $\mathcal{P}=\operatorname{EnvSel}(\mathcal{A} \cup \mathcal{P})$.
Update $\beta$ based on reproduction utility.
end for
return final population $\mathcal{P}$.

In Algorithm 1, $N$ is the population size. $K$ is the maximum number of clusters defined in agglomerative hierarchical clustering (AHC) [12] approach. $T$ is the maximum evolutionary

generations. $\mathcal{G C}$ and $\mathcal{L C}^{k}$ denote the global cluster and the $k$-th local cluster, respectively. $\boldsymbol{\Sigma}_{\mathrm{LC}^{k}}^{i}$ is the covariance matrix of the $k$-th local cluster that $\mathbf{x}^{i}$ locates in. $\beta$ is a probability to control which covariance matrix is decided for $\mathbf{x}^{i}$. rand() generates a uniformly distributed random number in $[0,1]$.
At each generation of AMEDA, the population is firstly partitioned into $K$ local clusters by a AHC approach (line 4), and a solution is randomly selected from each local cluster to construct a global cluster (line 5). Afterwards, the covariance matrix of the global cluster and all the covariance matrices of the local clusters are estimated as $\boldsymbol{\Sigma}_{\mathrm{GC}}$ and $\boldsymbol{\Sigma}_{\mathrm{LC}^{k}}(k=$ $1, \cdots, K)$ (line 6). Next, for each solution $\mathbf{x}^{i}$, a covariance matrix $\boldsymbol{\Sigma}^{i}$ is set using $\boldsymbol{\Sigma}_{\mathrm{LC}^{k}}^{i}$ or $\boldsymbol{\Sigma}_{\mathrm{GC}}$ with probability $\beta$ and $1-\beta$, respectively (line 8), a new solution $\mathbf{y}^{i}$ is sampled from the MGM built by $\mathbf{x}^{i}$ and $\boldsymbol{\Sigma}^{i}$ (line 9), and $\mathbf{y}^{i}$ is preserved in an auxiliary archive $\mathcal{A}$ (line 10). After completing solution generation, an environmental selection operation is conducted to update the population (line 12). Finally, a reproduction utility-based update strategy is applied on $\beta$ to get a new probability of building different types of MGMs for the next generation (line 13). With respect to the AMEDA framework, there are following comments should be noted.

- A general agglomerative AHC approach [12] is employed to proceed clustering. The group average linkage algorithm is used in the AHC of AMEDA to define the distance between two clusters. Detailed descriptions of the agglomerative AHC refer to [12].
- The MGM built based on a local or a global cluster is called a local or a global MGM. Sampling from the local MGMs emphasizes on exploitation, and sampling solutions from the global MGM is beneficial to exploration. The local and global MGMs work together to maintain the balance between exploitation and exploration.
- The covariance matrix of $\mathcal{G C}$ is a $n \times n$ matrix, i.e., $\boldsymbol{\Sigma}_{\mathrm{GC}}=$ $\left[\operatorname{Cov}\left(x_{s}, x_{t}\right)\right], s, t=1, \cdots, n . \operatorname{Cov}\left(x_{s}, x_{t}\right)$ denotes the covariance between the elements $x_{s}$ and $x_{t}$ of a solution x. $\boldsymbol{\Sigma}_{\mathrm{GC}}$ is estimated by the equation below.

$$
\operatorname{Cov}\left(x_{s}, x_{t}\right)=\frac{1}{|\mathcal{G C}|-1} \sum_{\mathbf{x} \in \mathcal{G C}}\left(x_{s}-x_{t}\right)^{2}
$$

for $s, t=1, \cdots, n$. The covariance matrix $\boldsymbol{\Sigma}_{\mathrm{LC}^{k}}(k=$ $1, \cdots, K)$ can also be estimated by the approach for estimating $\boldsymbol{\Sigma}_{\mathrm{GC}}$.

- If any one of the local clusters includes only one solution, the global covariance matrix will be used for the solution to build a MGM.


## B. Solution Generation

SolGen operator in line 9 of Algorithm 1 aims to produce new solutions, which is implemented by MGMs sampling and polynomial mutation [13] approaches shown in Algorithm 2. When producing an offspring, a MGM is firstly built to sample a new trial solution (lines 1-3). Afterwards, a repair operation is performed to make the solution feasible (line 4). Next, the trial solution is mutated by a polynomial mutation operator
(line 5). Finally, the mutated solution is repaired again to ensure its feasibility (line 6).

## Algorithm 2 $\operatorname{SolGen}\left(\boldsymbol{\Sigma}^{k}, \mathbf{x}^{k}\right)$

1: Take the Cholesky method to decompose the covariance matrix $\boldsymbol{\Sigma}^{k}$ to obtain a lower triangular matrix $\boldsymbol{\Lambda}$, and $\boldsymbol{\Sigma}^{k}=\boldsymbol{\Lambda} \boldsymbol{\Lambda}^{\boldsymbol{\top}}$.
2: Generate a vector $\mathbf{v}=\left(v_{1}, \cdots, v_{n}\right)^{\boldsymbol{\top}}$, where $v_{i} \sim N(0,1), i=$ $1, \cdots, n$, obey the unit Gaussian distribution.
3: Produce a trial solution $\mathbf{y}^{\prime}=\mathbf{x}^{k}+\boldsymbol{\Lambda} \mathbf{v}, \mathbf{y}^{\prime}=\left(y_{1}^{\prime}, \cdots, y_{n}^{\prime}\right)^{\top}$.
4: Repair the solution

$$
y_{i}^{\prime \prime}= \begin{cases}x_{i}^{k}-\operatorname{rand}()\left(x_{i}^{k}-a_{i}\right) & \text { if } y_{i}^{\prime}<a_{i} \\ x_{i}^{k}+\operatorname{rand}()\left(b_{i}-x_{i}^{k}\right) & \text { else if } y_{i}^{\prime}>b_{i} \\ y_{i}^{\prime} & \text { otherwise }\end{cases}
$$

for $i=1,2, \cdots, n$.
5: Mutate the solution

$$
y_{i}^{\prime \prime \prime}= \begin{cases}y_{i}^{\prime \prime}+\delta_{i} \times\left(b_{i}-a_{i}\right) & \text { if } \operatorname{rand}()<p_{m} \\ y_{i}^{\prime \prime} & \text { otherwise }\end{cases}
$$

with
$\delta_{i}= \begin{cases}{[2 r+(1-2 r)\left(\frac{b_{i}-y_{i}^{\prime \prime}}{b_{i}-a_{i}}\right)^{\eta_{m}+1}]^{\frac{1}{\eta_{m}+1}}-1} & \text { if } r<0.5 \\ 1-[2-2 r+\left(2 r-1\right)\left(\frac{y_{i}^{\prime \prime}-a_{i}}{b_{i}-a_{i}}\right)^{\eta_{m}+1}]^{\frac{1}{\eta_{m}+1}} & \text { otherwise }\end{cases}$,
where $a_{i}$ and $b_{i}$ denote the lower and upper boundaries of the $i$-th variable, respectively, $i=1, \cdots, n ; p_{m}$ is the mutation probability, and $\eta_{m}$ denotes the distribution index of mutation; $r=\operatorname{rand}()$.
6: Repair the solution

$$
y_{i}^{k}= \begin{cases}a_{i} & \text { if } y_{i}^{\prime \prime \prime}<a_{i} \\ b_{i} & \text { else if } y_{i}^{\prime \prime \prime}>b_{i} \\ y_{i}^{\prime \prime \prime} & \text { otherwise }\end{cases}
$$

7: return the new solution $\mathbf{y}^{k}=\left(y_{1}^{k}, \cdots, y_{n}^{k}\right)^{\boldsymbol{\top}}$.

Different from the traditional MEDA [14] that only one MGM is built for a cluster, in AMEDA, each solution $\mathbf{x}^{i}$ is assumed to be from a different MGM which adopts $\mathbf{x}^{i}$ as the mean vector, i.e., $\mathbf{x}^{i} \sim N\left(\mathbf{x}^{i}, \boldsymbol{\Sigma}\right)$. With a probability $\beta$, a local MGM is built for $\mathbf{x}^{i}$ to sample a solution, and the covariance matrix of the local cluster that $\mathbf{x}^{i}$ locates in is used to build the local MGM. Otherwise, with a probability $1-\beta$, a global MGM is built for $\mathbf{x}^{i}$ to sample a solution, and the covariance matrix of the global cluster is employed to build the global MGM. We have the following comments on the solution generation in AMEDA.

- The distribution structure of solutions in a population is usually strongly nonlinear. In AMEDA through building a MGM for each solution, the MGMs can work together to capture the population structure more accurately.
- In AMEDA, a different MGM is build for each solution to sample only one offspring. By this way, more diverse solutions can be produced, and the searching ability for the variable space can be enhanced greatly.
- AMEDA samples offsprings based on each solution considers outliers enough, which is also helpful for strengthening the searching ability of the algorithm.
- The solutions in the same cluster are set to share a same covariance matrix to build MGMs for themselves, the

modeling cost can be saved.

## C. Environmental Selection

The $\operatorname{EnvSel}(\mathcal{A} \cup \mathcal{P})$ operator in line 12 of Algorithm 1 is to preserve the promising solutions in $\mathcal{A} \cup \mathcal{P}$ survive into the next generation. A hypervolume metric-based environmental selection approach modified from the environmental selection in SMS-EMOA [15] is used in AMEDA. Algorithm 3 presents the details of the environmental selection in AMEDA.

```
Algorithm 3 \(\operatorname{EnvSel}(\mathcal{A} \cup \mathcal{P})\)
    Partition \(\mathcal{A} \cup \mathcal{P}\) into \(L\) fronts by fast nondominated sorting
    approach
        \(\left\{\mathcal{B}_{1}, \cdots, \mathcal{B}_{L}\right\}=\) FastNondominatedSorting \((\mathcal{A} \cup \mathcal{P})\).
    Copy better solutions,
        \(\mathcal{P}^{\prime}=\left\{\mathbf{x}^{l} \mid \mathbf{x}^{t} \in \bigcup_{j=1}^{l} \mathcal{B}_{j}, \bigcup_{j=1}^{l-1} \mathcal{B}_{j}<N \wedge \bigcup_{j=1}^{l} \mathcal{B}_{j} \geq N, l<L\right\} .\)
    if \(l>1\) then
        while \(\|\mathcal{P}\|^{\prime}>N\) do
            \(\mathbf{x}^{*}=\arg \max _{\mathbf{x} \in \mathcal{P}^{\prime}} d\left(\mathbf{x}, \mathcal{P}^{\prime}\right)\).
            Set \(\mathcal{P}^{\prime}=\overline{\mathcal{P}^{\prime}} \backslash\left\{\mathbf{x}^{*}\right\}\).
        end while
    else
        while \(\|\mathcal{P}\|^{\prime}>N\) do
            \(\mathbf{x}^{*}=\arg \min _{\mathbf{x} \in \mathcal{P}^{\prime}} \Delta_{\varphi}\left(\mathbf{x}, \mathcal{P}^{\prime}\right)\).
            Set \(\mathcal{P}^{\prime}=\overline{\mathcal{P}^{\prime}} \backslash\left\{\mathbf{x}^{*}\right\}\).
        end while
    end if
    Set \(\mathcal{P}=\mathcal{P}^{\prime}\).
    return \(\mathcal{P}\).
```

At first, a large population $\mathcal{A} \cup \mathcal{P}$ is constructed by combining the current population $\mathcal{P}$ and the auxiliary archive $\mathcal{A}$ consisted of new solutions, and the fast nondominated sorting approach proposed in NSGA-II [16] is used to partition $\mathcal{A} \cup \mathcal{P}$ into $L$ different nondominated fronts $\left\{\mathcal{B}_{1}, \cdots, \mathcal{B}_{L}\right\}$, where $\mathcal{B}_{1}$ and $\mathcal{B}_{L}$ represent the best and the worst fronts, respectively. Afterwards, all the solutions in $\mathcal{B}_{j}, j=1, \cdots, l, l<L$ are copied into a transitional archive $\mathcal{P}^{\prime}$ until $\left|\mathcal{P}^{\prime}\right| \geq N$. if $l>1$, i.e., the solutions in more than one front are put into $\mathcal{P}^{\prime}$, the solutions with the maximum $d\left(\mathbf{x}, \mathcal{P}^{\prime}\right)$ are removed one by one until $\left|\mathcal{P}^{\prime}\right|=N$, where $d\left(\mathbf{x}, \mathcal{P}^{\prime}\right)$ is the number of solutions in $\mathcal{P}^{\prime}$ that dominate $\mathbf{x}$. Otherwise, the solutions with the minimum hypervolume contribution $\Delta_{\varphi}\left(\mathbf{x}, \mathcal{P}^{\prime}\right)$ are deleted one by one until the size of $\mathcal{P}^{\prime}$ equals to $N$, where $\Delta_{\varphi}$ is calculated by the approach in [15]. After $\left|\mathcal{P}^{\prime}\right|=N, \mathcal{P}^{\prime}$ is transferred to $\mathcal{P}$ as the population of next generation.

## D. Adaptive Probability Update Strategy

In AMEDA, local and global MGMs are used to sample new solutions for emphasizing on exploitation and exploration, respectively. To balance the exploitation and exploration, a probability $\beta$ is applied to control the contributions of the different types of MGMs. In practice, different $\beta$ values need to be given for different MOPs. Even at different evolutionary
stages, $\beta$ may also require different values. Thus setting an adaptive $\beta$ is necessary for AMEDA. A reproduction utilitybased approach is proposed to adaptively adjust the $\beta$ value at each generation (line 13 of Algorithm 1), which is shown in Algorithm 4.

```
Algorithm 4 Probability Update
    Estimate the reproduction utility of the MGMs built based on
    local clusters or the global cluster at the \(t\)-th generation:
```

$$
u_{t}^{\mathrm{LC}(\mathrm{GC})}=\left\{\begin{array}{ll}
\frac{\sum_{k=1}^{L} S_{k}^{\mathrm{LC}(\mathrm{GC})}}{\sum_{k=1}^{L} Q_{k}^{\mathrm{LC}(\mathrm{GC})}} & \text { if } t<H L \\
\frac{\sum_{k=1}^{L} S_{k}^{\mathrm{LC}(\mathrm{GC})}}{\sum_{k=1}^{L} B_{L+1} Q_{k}^{\mathrm{LC}(\mathrm{GC})}} & \text { otherwise }
\end{array}\right.
$$

where $u_{t}^{\mathrm{LC}(\mathrm{GC})}$ is the reproduction utility of local MGMs (the global MGM) over the previous $H L$ generations. $Q_{k}^{\mathrm{LC}(\mathrm{GC})}$ represents the number of new solutions sampled from the local MGMs (the global MGM) at the $k$-th generation. $S_{k}^{\mathrm{LC}(\mathrm{GC})}$ is the number of successful solutions sampled from the local MGMs (the global MGM) at the $k$-th generation, where successful solutions indicate the solutions that enter the next generation successfully.
2: Calculate the mating restriction probability for the $(t+1)$-th generation:

$$
\beta_{t+1}=\frac{u_{t}^{\mathrm{GC}}+\varepsilon}{u_{t}^{\mathrm{GC}}+u_{t}^{\mathrm{LF}}+\varepsilon}
$$

where $\varepsilon=10^{-10}$ is employed to ensure the legality of the calculation.
3: return $\beta_{t+1}$.

It should be noted that, at each generation five solutions are forced to be sampled from local and global MGMs, respectively, so that there always exist more than five new solutions generated from each different type of MGMs, which is with the purpose of keeping the update of $\beta$ to be available all the time.

## IV. EXPERIMENTAL STUDIES

## A. Performance Metric

It is well-known that a MOP has a set of Pareto optimal solutions called Pareto set (PS). The set of objective points of Pareto optimal solutions is named as Pareto front (PF). A MOEA is able to obtain an approximated solution set of a MOP through a single run. In general, it is hoped that the corresponding front of approximated solution set (approximated front for short) approaches to the PF as close as possible (convergence), the objective points spread along the PF as widely as possible (diversity) and distribute along the PF as uniformly as possible (uniformity).

A commonly used quality indicator called hypervolume (HV) [17] is employed to quantitatively measure the quality of approximated front obtained by the algorithms. Suppose $\mathcal{P}$ is an approximated front. The HV metric is defined as follows:

$$
\operatorname{HV}(\mathcal{P}, \mathbf{z})=\operatorname{VOL}\left(\bigcup_{\mathbf{x} \in \mathcal{P}}\left[f_{1}(\mathbf{x}), z_{1}\right] \times \cdots\left[f_{m}(\mathbf{x}), z_{m}\right]\right)
$$

where $\mathbf{z}=\left(z_{1}, \cdots, z_{m}\right)^{\boldsymbol{\top}}$ is a reference point in the objective space dominated by any objective points in $\mathcal{P}$, and $\operatorname{VOL}(\cdot)$ is the Lebesgue measure. HV metric measures the size of the objective space dominated by the objective points in $\mathcal{P}$ and bounded by $\mathbf{z}$. When calculating the HV metric values of the obtained approximated front of path planning model, the reference point is set as $\mathbf{z}=(500,5,15)^{\top}$.

HV metric can measure the convergence, diversity and uniformity of the obtained approximated fronts. If approximated front $\mathcal{P}$ does not miss any parts of PF, and the objective points approach to PF as close as possible and distribute along the PF as evenly as possible, $\mathcal{P}$ will have a larger HV metric value.

## B. Algorithm Parameters

To examine the performance of AMEDA for the path planning model, five state of the art MOEAs, i.e., MOEA/DDE [18], TMOEA/D [19], RM-MEDA [20], NSGA-II [16] and SMS-EMOA [15] are selected to conduct comparison experiments. The simulated binary crossover operator in original NSGA-II and SMS-EMOA are replaced by the differential evolution (DE) operator to take part in the comparison experiments. The parameters of all the MOEAs are tuned through the preliminary experiments and the best parameter combinations are adopted in the comparison studies. All the parameter settings are as follows:

- Public parameters:
- population size $N: N=105$ for all the algorithms;
- variable dimension: $n=30$ (i.e., 10 waypoints);
- maximum evolutionary generations: $T=500$.
- AMEDA Parameters:
- initial control probability: $\beta_{0}=0.9$;
- history length: $H=10$;
- maximum number of clusters: $K=4$;
- polynomial mutation: $p_{m}=1 / n, \eta_{m}=20$.
- MOEA/D-DE Parameters:
- neighborhood size: $N S=5$;
- probability of neighborhood search: 0.7 ;
- maximal number of solution replacement: $n_{r}=2$;
- differential evolution: $F=0.5, C R=0.6$;
- polynomial mutation: $p_{m}=1 / n, \eta_{m}=20$.
- TMOEA/D Parameters:
- neighborhood size: $N S=30$;
- first searching phase: $T 1=T / 10$;
- second searching phase: $T 2=\alpha T, \alpha=\{0.01,0.02$, $\cdots, 0.1,0.1,0.1,0.15\}$
- differential evolution: $F=0.9, C R=1$;
- RM-MEDA Parameters:
- number of clusters in local PCA: 7;
- maximal iteration number for local PCA: 50;
- extension rate of sampling: 0.25 .
- NSGA-II and SMS-EMOA Parameters:

Two algorithms have the same parameter settings.

- differential evolution: $F=0.3, C R=0.8$;
- polynomial mutation: $p_{m}=1 / n, \eta_{m}=20$;

To get statistically sound experimental conclusions, each algorithm runs 30 times independently for the path planning model, and the comparisons are performed based on the statistical metric values, i.e., mean values and standard deviations.

## C. Model Parameters

In this paper, suppose that an aircraft flies across a combat area with size $200 \times 200 \mathrm{~km}^{2}$, and there are six threats in the area. According to Eq.(1), Eq.(13) is used to generate the original digital terrain shown in Fig.1(a).

$$
\begin{aligned}
z_{1}(x, y)= & \sin (y / 90+3 \pi / 2)+\sin (x / 15) / 10+ \\
& 9 \cos \left(\sqrt{(y / 18)^{2}+(x / 15)^{2}} / 2\right) / 10+ \\
& \sin \left(\sqrt{(y / 18)^{2}+(x / 15)^{2}} / 2\right) / 2+ \\
& 3 \cos (y / 18) / 10
\end{aligned}
$$

Parameters of the five peak terrains of threats are set as: heights $\mathcal{H}=\{0.7,2.5,3.2,2.34,1.77\}$; horizontal coordinates of the centers $\mathcal{X}_{c}=\{50,100,100,130,160\}, \mathcal{Y}_{c}=$ $\{60,160,100,20,100\}$; parameters of the terrain profiles $\mathcal{X}_{t}=$ $\{140,280,150,160,170\}, \mathcal{Y}_{t}=\{20,220,280,190,230\}$. Based on the parameters, the yielded equivalent terrains of threats are presented in Fig.1(b).

Through fusing the original digital terrain and the equivalent terrains of threats, the generated equivalent digital terrain is shown in Fig.1(c). The path planning in this paper is conducted based on the digital terrain in Fig.1(c). The start and target points of flight are $[0,0,0.25]$ and $[200,200,0]$, respectively.
![img-0.jpeg](img-0.jpeg)
(a)
![img-1.jpeg](img-1.jpeg)
(c)

Fig. 1. (a) Original digital terrain; (b) Equivalent terrain of threats; (c) Equivalent digital terrain.

In addition, in the path planning model, the allowed highest altitude, lowest flight altitudes, maximum turning angle, maximum total length of flight path and maximum climb/dive angle are set as $H_{\max }=1.5 \mathrm{~km}, H_{\min }=0.05 \mathrm{~km}, \phi=60^{\circ}$, $L_{\max }=500 \mathrm{~km}$ and $\varphi=45^{\circ}$, respectively; the required

shortest length of path segment is set as $L_{\min }=2 \mathrm{~km}$. The penalty method is used to handle the constraints when the path planning model is optimized.

## D. Comparison Experiments

The error bars of HV metric values obtained by MOEA/DDE, TMOEA/D, RM-MEDA, NSGA-II, SMS-EMOA and AMEA, respectively, over 30 independent runs on the path planning model are given in Fig.2. It can be seen from the figure that AMEDA obtains the maximum mean HV metric value and the minimum standard deviation value, which denotes that AMEDA is able to stably and effectively find the approximated front with good diversity and excellent convergence for the path planning model.
![img-4.jpeg](img-4.jpeg)

Fig. 2. The error bars of HV metric values obtained by MOEA/D-DE, TMOEA/D, RM-MEDA, NSGA-II, SMS-EMOA and AMEA, respectively, over 30 independent runs on the path planning model.

The evolution of mean values and standard deviations of HV metric values versus generations is plotted in Fig.3. Fig. 3 shows that during evolution for 300 generations, AMEDA reaches the maximum mean HV metric values using the least evolutionary generations, and AMEDA always has small standard deviations of HV metric values when evolving. The figure indicates that during evolutions, AMEDA always maintains a population with better convergence, diversity and uniformity.
![img-3.jpeg](img-3.jpeg)

Fig. 3. Evolution of mean values and standard deviations of HV metric values versus generations.

Fig. 4 plots the approximated fronts obtained by SMSEMOA and AMEDA. All the 30 approximated fronts yielded by SMS-EMOA and AMEDA, respectively, are plotted in Fig.4(a). The approximated front with median HV metric value (called representative front) obtained by SMS-EMOA and AMEDA, respectively, over 30 independent runs are plotted in Fig. 4(b). Fig.4(a) shows that compared with SMSEMOA, all the approximated fronts obtained by AMEDA all stably converge to the region of objective space with smaller objective values, and the distribution of the approximated fronts is much more widely. Part of the approximated fronts achieved by SMS-EMOA have not reached the region with smaller objective values, and the objective points in these fronts are much more concentrated. According to Fig.4(b), it is easy to observe that the representative approximated front obtained by AMEDA spreads much more widely than those yielded by SMS-EMOA.
![img-4.jpeg](img-4.jpeg)

Fig. 4. Approximated fronts obtained by SMS-EMOA and AMEDA.
In the final population with median HV metric value, the corresponding flight paths with the shortest total length, the lowest flight altitude and the smallest turning angle are presented in Fig.5. Fig.5(a) shows that the flight path with the shortest total length almost straightly traverses the combat area. However, the flight altitude is relatively high, which implies a higher risk of being discovered and attacked. Fig.5(b) presents that the flight path with the lowest altitude is quite close to the ground, which is helpful for concealment and penetration. However, the path length is much longer, which will increase fight time. Fig.5(c) shows that the path with the smallest turning angle is very smooth, the turning angles during flight are all very small. Fig. 5 illustrates that AMEDA is able to yield multiple flight paths with different characteristics for the decision makers to help their decision making through a single run. This type of path planning approach is quite meaningful and efficient.

The comparisons in Fig.2, Fig. 3 and Fig. 4 indicate that AMEDA has excellent performance to deal with the path

![img-5.jpeg](img-5.jpeg)

Fig. 5. (a) Path with the shortest total length; (b) Path with the lowest flight altitude; (c) Path with the smallest turning angle.
planning model of this paper. The visualization in Fig. 5 illustrates AMEDA is very helpful for the decision makers on planning the paths of the aircraft.

## V. CONCLUSION

This paper has proposed a novel adaptive multiobjective estimation of distribution algorithm named as AMEDA to deal with the path planning of aircraft. The characteristic of AMEDA is that a clustering-based multivariate Gaussian sampling strategy is designed. At each generation, AMEDA firstly employs an agglomerative hierarchical clustering approach to partition the population into a number of local clusters, and constructs a global cluster by randomly selecting a solution from each local cluster. Afterwards, for each solution, with a probability a local multivariate Gaussian model (MGM) is built based on the local cluster that the solution locates in to sample an offspring, which is beneficial to exploitation; otherwise, a global MGM is built for the solution based on the global cluster to generate an offspring, which is helpful for exploration. To reduce the modeling complexity, a covariance sharing strategy is also designed for the solutions within the same cluster to build MGMs. To balance the exploration and exploitation better, the probability that controls the contributions of the local and global MGMs is updated at each generation, according to the reproduction utility of the two types of MGMs over the last certain generations.

AMEDA has been compared with five representative MOEAs (i.e., MOEA/D-DE, TMOEA/D, RM-MEDA, NSGAII, and SMS-EMOA) on the path planning model. The experimental results have shown that AMEDA dramatically outperforms the comparison algorithms on planning the flight path of the aircraft. AMEDA is very meaningful and efficient for the decision makers on planning the paths of the aircraft.
