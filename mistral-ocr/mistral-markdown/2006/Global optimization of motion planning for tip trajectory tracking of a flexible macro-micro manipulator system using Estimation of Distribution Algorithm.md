# Global optimization of motion planning for a flexible macro-micro manipulator system using Estimation of Distribution Algorithm 

Lingzhi Luo, Yu Zhang, Zengqi Sun<br>Department of Computer Science and Technology<br>Tsinghua University<br>Beijing, 100084, China<br>luolingzhi@gmail.com, zhang-y-03@mails.tsinghua.edu.cn<br>szq-dcs@tsinghua.edu.cn

Tangwen Yang<br>School of Electrical, Electronic and Mechanical Eng<br>University College Dublin Belfield<br>Dublin 4, Ireland<br>tangwen.yang@ucd.ie


#### Abstract

This paper proposes a new method for motion planning global optimization of a macro-micro manipulator (3M) system based on Estimation of Distribution Algorithm (EDA). Due to the redundant character of a 3M system, its motion planning is formulated as a multi-objective optimization problem under the mechanical constraints. After a task space division, optimization parameters are transferred from joint angles to division points of macro and micro part of the system, which largely reduces the searching space. However, to avoid sucking local extremum, global optimization is too time-consuming to bear. Instead of searching the division point space directly, EDA is applied to estimate the probability model of the division space and thus extracts mapping information between the optimization function and division points. Simulation results on a planar 4 degree-of-freedom (DOF) macro-micro manipulator system are presented herein to show the effectiveness of the proposed methods.


Index Terms - macro-micro manipulator, motion planning, estimation of distribution algorithm, flexible manipulator, global optimization

## I. INTRODUCTION

With the development of space exploitation and exploration, a need has been developed for mature robot manipulation technology in space mission. Flexible manipulator has played crucial role in such applications for several decades due to large potential advantages such as large work range, high operation speed, and great ratio of payload to weight. Several flexible manipulator systems have been put into practice i.e. Canadian Mobile Servicing System (MSS) [1], which is mounted in the international space station. However, deformation and vibration of flexible links in high speed motion lead to complicated dynamics modeling, large motion errors of the endpoint and thus bring great difficulty to the controller design.

The flexible macro-micro manipulator system combines two type manipulators: the long and light flexible macro manipulator and the relatively short and rigid micro manipulator. Hogan et al. [2] examined the root locus and bode plot of force control and the results suggested that a
macro/micro manipulator is inherently more stable in regulating interface forces than a conventional robot system. A robust controller design based on physical equivalence and impedance matching is proposed. It is shown that interface force regulation at higher bandwidths can be achieved with only minimal knowledge of the structure. I Sharf et al. [3] used the reaction force from the micro manipulator to the macro manipulator as a control variable for damping the large flexible manipulator and simulation results in a 6-DOF rigid manipulator on a flexible mast demonstrate the feasibility of the approach. Yoshikawa et al. [4] used the concept of compensability of a flexible macro-micro manipulator system to generate the joint trajectories and proposed a quasi-static trajectory tracking controller to track a circle as the desired tip trajectory. However, the tracking errors may greatly increase once the motion acceleration of the system enlarges. Then a dynamic trajectory tracking controller was proposed to overcome such problem [5], which took the dynamics of the system into consideration. Motoyuki et al. [6] presented a Lyapunov-based positioning controller so-called PDS controller for a 2-DOF macro-micro manipulator system to suppress the bending vibration of the macro arm. Also fuzzy controller [7] and neural network controller [10] are introduced to improve the performance of controlling the motion of a macro-micro manipulator system. However, most of literature above neglected the role of motion planning in reducing tracking errors and enhancing the motion accuracy. Yoshikawa et al. [4] related to the path planning, and differential method is introduced in their reports to generate the joint trajectory and make compensability larger. However, the parameters' selection is not guided by definite theory or criteria and it is not certain that the solution is optimal for the compensability.

A population-based search algorithm EDA is adopted for joint trajectory generation and motion planning in this paper. EDA is able to build the probability distribution model of promising solutions from selected solutions. Compared to genetic algorithm employed in our work before [11], EDA avoids selection of too many parameters such as population

[^0]
[^0]:    * Supported by the National Natural Science Foundation of China(No. 60305008 )

volume, number of genetic generations as well as parameters for the crossing and mutation operation.

This paper is organized as below. Section 2 briefly describes the kinematic and dynamic models of 3 M system as well as the motion planning problem. In Section 3 mechanical constraints which helps determine the division point space are introduced. Optimization criterion of joint trajectories is presented in section 4, which guarantees the optimization is global. In Section 5, EDA employed in this paper is demonstrated. This is continued by simulation results on a 4DOF macro-micro manipulator system.

## II. Problem Description

## A. Concept of a Flexible 3M System

To realize the tip trajectory tracking of flexible manipulators, a flexible 3 M system is proposed as shown in figure 1. The flexible macro part of this system can move widely but with low tip accuracy. The rigid micro part is attached to the tip of the macro one, which can move fast and precisely.
![img-0.jpeg](img-0.jpeg)

Fig. 1 A flexible 3M system
The flexible 3M system is generally redundant for tip trajectory tracking, with actuators whose number is more than the dimension of task space. So there exist infinite different solutions for joint variables which make the tip position locate exactly on the desired trajectory. Among all these possible solutions, better solutions are expected to be extracted. It is a problem of optimization to make compensation easy and improve the performance of tracking.

In general, both the macro and micro manipulator should have enough degree of freedom to complete the task of operation and compensation. A kind of special redundant macro-micro manipulator system is considered which consists of micro manipulator with the same DOF as that of the task coordinate system here. Although there exist redundant macro manipulator for the purpose of obstacle or singularity point avoidance, macro manipulator with the same DOF as that of the task coordinate system is studied here, representative for the research of trajectory is tracking.
B. Optimization in Division Point Space

Consider a robot system with an $M$-DOF macro manipulator and an $m$-DOF micro manipulator. Let
$\boldsymbol{\theta}_{M} \in \mathrm{R}^{M}$ and $\boldsymbol{\theta}_{m} \in \mathrm{R}^{m}$ be the vectors of the joint variables of the macro and micro manipulator, respectively, $\boldsymbol{\delta} \in \mathrm{R}^{r}$ be the flexural displacement vector and $\boldsymbol{p} \in \mathrm{R}^{n}$ be the tip vector in the n-dimensional task space. The endpoint vector $\boldsymbol{p}$ is a nonlinear function of $\boldsymbol{\theta}_{\boldsymbol{M}}, \boldsymbol{\theta}_{\boldsymbol{m}}$ and $\boldsymbol{\delta}$ :

$$
p=f\left(\theta_{M}, \theta_{m}, \delta\right)
$$

Define $\quad \boldsymbol{f}_{\delta=0}\left(\boldsymbol{\theta}_{M}, \boldsymbol{\theta}_{m}\right)=\boldsymbol{f}\left(\boldsymbol{\theta}_{M}, \boldsymbol{\theta}_{m}, \boldsymbol{\theta}\right)$
Optimization in the whole joint angle space will be timeconsuming and cannot guarantee that the tip positions locate exactly on the desired trajectory.

Here we transfer the search space from the joint variables to division point, the point where the micro manipulator connects to the macro one. Task space is divided to two parts: The macro manipulator carried the micro one to the neighbourhood of the task point, while the micro manipulator sets its joint variables to make the tip on the task point.

$$
p=p_{M}+p_{m}
$$

where $\boldsymbol{p}_{M}$ denotes the vector of the task division point, which is also the end-point of the macro manipulator and the base point of the micro one, $\boldsymbol{p}_{m}$ denotes the vector from the division point to the tip of the whole system.

The division point space is determined by the mechanical constraint from the 3M system:

$$
\begin{aligned}
& \left\|\boldsymbol{p}_{M}\right\| \leq \sum_{i=1}^{M} l_{i} \\
& \left\|\boldsymbol{p}_{m}\right\| \leq \sum_{i=M}^{M+m} l_{i}
\end{aligned}
$$

where $\|*\|$ denotes the Euclidean norm of vector *. Considering the real situation of task operation, it is assumed that macro manipulator is large enough to cover the space prescribed by inequation (5). So conditions (4) and (5) can be combined to (5). That is, the division point must be in the circle with task point as its centre and $\sum_{i=1}^{m} l_{M+i}$ as its radius.

## III. PERFORMANCE CRITERION

To guarantee the accuracy of tip position by motion planning, two conditions (3) and (5) should be satisfied, which provides the search space boundary. One optimal solution can be selected by minimizing the fitness function which considers the compensability and the energy consumption in the process of trajectory tracking.
A. Compensability

The small displacements $\tilde{\boldsymbol{p}}$ of the tip vector can be expressed as

$$
\tilde{\boldsymbol{p}}=J_{\theta_{M}} \tilde{\boldsymbol{\theta}}_{M}+J_{\theta_{m}} \tilde{\boldsymbol{\theta}}_{m}+J_{\delta} \tilde{\boldsymbol{\delta}}
$$

where $\boldsymbol{J}_{\theta_{M}} \in \mathrm{R}^{n \times M}, \boldsymbol{J}_{\theta_{m}} \in \mathrm{R}^{n \times m}$ and $\boldsymbol{J}_{\delta} \in \mathrm{R}^{n \times e}$ are Jacobian matrices of $\boldsymbol{p}$ with respect to $\boldsymbol{\theta}_{\boldsymbol{M}}, \boldsymbol{\theta}_{\boldsymbol{m}}$ and $\boldsymbol{\delta}$, respectively, and $\tilde{\boldsymbol{\theta}}_{\boldsymbol{M}}, \tilde{\boldsymbol{\theta}}_{\boldsymbol{m}}$, and $\tilde{\boldsymbol{\delta}}$ denote small changes in $\boldsymbol{\theta}_{\boldsymbol{M}}, \boldsymbol{\theta}_{\boldsymbol{m}}$ and $\boldsymbol{\delta}$ respectively.

The deflection of flexible links $\tilde{\boldsymbol{\delta}}$ can be converted to $\tilde{\theta}_{\delta i}$, the errors of joint variables:

$$
\tilde{\theta}_{\delta i}=\left\{\begin{array}{c}
\varepsilon_{1} / l_{1}, i=1 \\
\alpha_{i-1}+\varepsilon_{i} / l_{i}, 2 \leq i \leq M \\
\alpha_{M}, i=M+1
\end{array}\right.
$$

So (6) can be rewritten to:

$$
\tilde{\boldsymbol{p}}=J_{\theta_{M}} \tilde{\boldsymbol{\theta}}_{M}^{\prime}+J_{\theta_{m}} \tilde{\boldsymbol{\theta}}_{m}^{\prime}
$$

where

$$
\tilde{\theta}_{i}^{\prime}=\left\{\begin{array}{l}
\tilde{\theta}_{i}+\tilde{\theta}_{\delta i}, 1 \leq i \leq M+1 \\
\tilde{\theta}_{i}, M+2 \leq i \leq M+m
\end{array}\right.
$$

Compared to the physical parameters of the manipulators, tip errors caused by the deformation of the flexible links are small. To compensate such errors, we need adjust the desired joint variables of the micro manipulator:

$$
\boldsymbol{f}_{\delta=\theta}\left(\boldsymbol{\theta}_{M}, \boldsymbol{\theta}_{m}^{\prime}\right)+\tilde{\boldsymbol{p}}=\boldsymbol{f}_{\delta=\theta}\left(\boldsymbol{\theta}_{M}, \boldsymbol{\theta}_{m}^{\prime}\right)
$$

where $\boldsymbol{\theta}_{m}{ }^{\prime}$ denotes the joint variables after adjustment and $\tilde{p}$ is substituted with

$$
\tilde{\theta}_{i}=0,1 \leq i \leq M+m
$$

Considering the adjustment is small for $\theta_{m}$, so the caused position change $\Delta f$ would be:

$$
\boldsymbol{f}_{\delta=\theta}\left(\boldsymbol{\theta}_{M}, \boldsymbol{\theta}_{m}^{\prime}\right)-\boldsymbol{f}_{\delta=\theta}\left(\boldsymbol{\theta}_{M}, \boldsymbol{\theta}_{m}\right)=J_{\theta_{m}}\left(\boldsymbol{\theta}_{m}^{\prime}-\boldsymbol{\theta}_{m}\right)
$$

Derived from (8), (9), (10), (11) and (12):

$$
\begin{aligned}
\boldsymbol{\theta}_{m}^{\prime} & =\boldsymbol{\theta}_{m}-\boldsymbol{J}_{\theta_{m}}{ }^{+}\left(\boldsymbol{J}_{\theta_{M}} \tilde{\boldsymbol{\theta}}_{M}^{\prime}+\boldsymbol{J}_{\theta_{m}} \tilde{\boldsymbol{\theta}}_{m}^{\prime}\right) \\
& =\left(\boldsymbol{\theta}_{m}-\tilde{\boldsymbol{\theta}}_{\delta_{m}}{ }^{\prime}\right)-\boldsymbol{J}_{\theta_{m}}{ }^{+} \boldsymbol{J}_{\theta_{M}} \tilde{\boldsymbol{\theta}}_{\delta_{M}}{ }^{\prime}
\end{aligned}
$$

where $\boldsymbol{J}_{\theta_{m}}{ }^{+}$denotes pseudo-inverse matrix of $\boldsymbol{J}_{\theta_{m}}$, $\tilde{\boldsymbol{\theta}}_{\delta_{M}}{ }^{\prime} \in \mathrm{R}^{M}$ and $\tilde{\boldsymbol{\theta}}_{\delta_{m}}{ }^{\prime} \in \mathrm{R}^{m}$ denote the equivalent joint variables alternation of the macro and micro manipulator, respectively, due to the deformation of flexible links of the macro manipulator, they are given as:

$$
\begin{aligned}
& \tilde{\boldsymbol{\theta}}_{\delta_{M}}{ }^{\prime}=\left[\tilde{\theta}_{\delta 1}^{\prime}, \tilde{\theta}_{\delta 2}^{\prime}, \cdots, \tilde{\theta}_{\delta M}^{\prime}\right]^{T} \\
& \tilde{\boldsymbol{\theta}}_{\delta_{m}}{ }^{\prime}=\left[\tilde{\theta}_{\delta(M+1)}^{\prime}, 0, \cdots, 0\right]^{T}
\end{aligned}
$$

Define

$$
\Delta \boldsymbol{\theta}_{m}=\boldsymbol{\theta}_{m}^{\prime}-\boldsymbol{\theta}_{m}
$$

According to (13), equality

$$
\Delta \boldsymbol{\theta}_{m}=\tilde{\boldsymbol{\theta}}_{\delta_{m}}{ }^{\prime}+\boldsymbol{J}_{\theta_{m}}{ }^{+} \boldsymbol{J}_{\theta_{M}} \tilde{\boldsymbol{\theta}}_{\delta_{M}}{ }^{\prime}
$$

is obtained. From (7) and (14), derived

$$
\tilde{\boldsymbol{\theta}}_{\delta_{M}}{ }^{\prime}=\boldsymbol{T}_{\varepsilon} \varepsilon+\boldsymbol{T}_{\alpha} \boldsymbol{\alpha}
$$

where $\boldsymbol{\varepsilon}=\left[\varepsilon_{1}, \cdots, \varepsilon_{M}\right]^{T}, \boldsymbol{\alpha}=\left[\alpha_{1}, \cdots, \alpha_{M}\right]^{T}, \boldsymbol{T}_{\varepsilon}$ and $\boldsymbol{T}_{\alpha}$ are given as:

$$
\begin{aligned}
& \boldsymbol{T}_{\varepsilon}=\frac{\partial \tilde{\boldsymbol{\theta}}_{\boldsymbol{\theta}_{M}}^{\prime}}{\partial \varepsilon}=\operatorname{diag}\left[l_{1}, l_{2}, \cdots l_{M}\right]^{-1} \\
& \boldsymbol{T}_{\alpha}=\frac{\partial \tilde{\boldsymbol{\theta}}_{\boldsymbol{\theta}_{M}}^{\prime}}{\partial \boldsymbol{\alpha}}=\left[\begin{array}{cccc}
0 & 0 & \cdots & 0 \\
1 & 0 & \ddots & \vdots \\
0 & \ddots & \ddots & 0 \\
0 & 0 & 1 & 0
\end{array}\right]
\end{aligned}
$$

Let $\operatorname{diag}[*]$ denote the diagonal matrix.
Substitute (18) to (17),

$$
\Delta \boldsymbol{\theta}_{m}=\boldsymbol{J}_{\varepsilon} \varepsilon+\boldsymbol{J}_{\alpha} \boldsymbol{\alpha}=\boldsymbol{J}_{\delta} \tilde{\boldsymbol{\delta}}
$$

is obtained, where $\boldsymbol{J}_{\delta}=\left[\begin{array}{ll}\boldsymbol{J}_{\varepsilon} & \boldsymbol{J}_{\alpha}\end{array}\right], \boldsymbol{J}_{\varepsilon}=\boldsymbol{J}_{\theta_{m}}{ }^{+} \boldsymbol{J}_{\theta_{M}} \boldsymbol{T}_{\varepsilon}$,

$$
\boldsymbol{J}_{\alpha}=\boldsymbol{J}_{\theta_{m}}{ }^{+} \boldsymbol{J}_{\theta_{M}} \boldsymbol{T}_{\alpha}+\left[\begin{array}{llll}
1 & 0 & \cdots & 0
\end{array}\right]^{T}, \tilde{\boldsymbol{\delta}}=\left[\begin{array}{ll}
\varepsilon & \boldsymbol{\alpha}
\end{array}\right]^{T}
$$

Deformation $\tilde{\boldsymbol{\delta}}$ is normalized to distinguish the weight of each element:

$$
\tilde{\boldsymbol{\delta}}_{\text {norm }}=\boldsymbol{T}_{\delta} \tilde{\boldsymbol{\delta}}
$$

where

$\boldsymbol{T}_{\boldsymbol{\delta}}=\operatorname{diag}\left[\varepsilon_{1 \max }, \cdots, \varepsilon_{M \max }, \alpha_{1 \max }, \cdots, \alpha_{M \max }\right]^{-1}$
Here $\varepsilon_{i \max }$ and $\alpha_{i \max }(i=1,2, \cdots, M)$ denotes weight
of each element of $\tilde{\boldsymbol{\delta}}$. Joint displacement of the micro manipulator $\Delta \boldsymbol{\theta}_{\boldsymbol{m}}$ for compensation is also normalized to take the cost of each micro manipulator joint into consideration:

$$
\Delta \tilde{\boldsymbol{\theta}}_{\boldsymbol{m}}=\boldsymbol{T}_{\boldsymbol{m}} \Delta \boldsymbol{\theta}_{\boldsymbol{m}}
$$

Where

$$
\boldsymbol{T}_{\boldsymbol{m}}=\operatorname{diag}\left[\theta_{\text {m} \mid \text { cost }}, \theta_{\text {m2cost }}, \cdots \theta_{\text {mncost }}\right]^{-1}
$$

Here $\theta_{\text {micost }}(i=1,2, \cdots, m)$ denotes the cost of each micro manipulator joint.

From (21), equality

$$
\Delta \tilde{\boldsymbol{\theta}}_{\boldsymbol{m}}=\tilde{\boldsymbol{J}}_{\delta} \tilde{\boldsymbol{\delta}}_{\text {norm }}
$$

is derived, where $\tilde{\boldsymbol{J}}_{\boldsymbol{\delta}}=\boldsymbol{T}_{\boldsymbol{m}} \boldsymbol{J}_{\boldsymbol{\delta}} \boldsymbol{T}_{\boldsymbol{\delta}}{ }^{-1}$. To minimize $\left\|\Delta \tilde{\boldsymbol{\theta}}_{\boldsymbol{m}}\right\|$
for any $\tilde{\boldsymbol{\delta}}_{\text {norm }}$ satisfying $\left\|\tilde{\boldsymbol{\delta}}_{\text {norm }}\right\| \leq 1$, compensability measured by:

$$
I_{c}=\frac{1}{\left\|\tilde{\boldsymbol{J}}_{\delta} \tilde{\boldsymbol{J}}_{\delta}^{\dagger}\right\|}
$$

should be as small as possible, which serves as the first factor for optimization.
B. Global Fitness Function

Define a fitness function

$$
g\left(\boldsymbol{\theta}_{M}, \boldsymbol{\theta}_{m}\right)=a_{1} I_{C}+a_{2} I_{e}
$$

where $a_{1}$ and $a_{2}$ denotes weight of $I_{C}$ and $I_{e}$ in the
optimization function respectively. Function $g\left(\boldsymbol{\theta}_{M}, \boldsymbol{\theta}_{m}\right)$
can be taken as the fitness function for optimization of each endpoint which locates on the desired tip trajectory. However, it is devoid of consideration for the whole tip trajectory.

According to the fitness function above, fitness values for subsequent tip points are determined by the selection of the start joint state. Discretize the continuous curve into $n$ individual points at appropriate interval, derive :

$$
f i t\left(\boldsymbol{\theta}_{\theta}\right)=\sum_{i=1}^{n} G\left(\boldsymbol{p}_{i}\right)
$$

where $\boldsymbol{\theta}_{\boldsymbol{\theta}}$ denotes the start joint variables, and $G(\boldsymbol{p})$ denotes the maximum of the fitness function $g\left(\boldsymbol{\theta}_{\boldsymbol{M}}, \boldsymbol{\theta}_{\boldsymbol{m}}\right)$ when the desired tip position is $\boldsymbol{p}$.

## IV. EDA-Optimization Algorithm

A new evolution algorithm EDA is adopted here to search for a series of joint variables, best solutions for the global fitness function. Different from the Genetic Algorithm (GA), EDA replace the crossing and mutation operation by utilizing probabilistic model for population generation and updating. New population is generated from updated probabilistic model by promising individuals selected from last generation.

Gaussian normal distribution is proposed for the probability model and there exist two parameters for the model, mean $\mu$ and standard deviation $\varphi, \mu \in R^{n}$ and $\varphi \in R^{n}, n$ is the dimension of the task space. No covariance is covered between different coordinates of the task space.

The proposed algorithm can be described as below:

1. Select a discrete tip point from the desired trajectory.
2. Give initial values of mean $\mu$ and standard deviation $\varphi$ for the model.
3. While termination condition is not satisfied
a) Sample $S$ individuals from the Gaussian model to generate population;
b) Calculate fitness values for individuals in the population;
c) Select $Q$ individuals from the population according to the fitness values;
d) Update the model parameters using the Q individuals;
Algorithm discussed above can be used for joint variables' optimization of every tip points. However, the optimization of each joint state derived by (29), as a whole, does not necessarily lead to the optimization of the whole fitness value calculated by (30). So another outer optimization loop is added by searching for the optimal start point for the whole fitness value.

## V. Simulation Results

In order to test the effectiveness of the proposed trajectory planning scheme, a planar 4-DOF macro-micro

manipulator system has been considered. The flexible macro manipulator has 2-DOF and the rigid micro one has two other degrees of freedom. Geometric parameters of the macro-micro manipulator system are given in table 1.

TABLE I
The Geometric Parameters Of The 4-DOF Macro-Micro
MANIPULATOR SYSTEM

| Macro manipulator | $I_{1} / \mathrm{m}$ | $I_{2} / \mathrm{m}$ |
| :-- | :-- | :-- |
| length | 0.5 | 0.5 |
| Micro manipulator | $I_{3} / \mathrm{m}$ | $I_{4} / \mathrm{m}$ |
| length | 0.16 | 0.16 |

A desired circle tip trajectory is prescribed starting from the initial point $(1.1,0)$ with another point $(1.1,0.5)$ as its centre. Here $a_{1}=1, a_{2}=1$ and $\lambda$ is given as 2.5 .
A. Individual Optimization Result by EDA

Planned joint trajectory is shown in figure 2 as case (A). To show the effect of the proposed scheme, case (B) where $a_{1}=1$ and $a_{2}=0$ without considering energy consumption, case (C) where $a_{1}=0$ and $a_{2}=1$ without considering compensability are shown in the figure 2. Four joint values of each case are shown in figure 3, respectively. It is illustrated that the joint variables alter more rapidly if the energy consumption takes up a lower weight in the optimization function of (29) while the compensability is larger in case (B) than case (A) and case (C). The optimization results by EDA are almost the same as those derived from GA, but with much less time.
(A) Consider both compensability and energy consumption
![img-5.jpeg](img-5.jpeg)
(C)Only consider the energy consumptio
![img-5.jpeg](img-5.jpeg)

Fig. 2 Planned joint trajectories
(A)
![img-5.jpeg](img-5.jpeg)
(B)
![img-5.jpeg](img-5.jpeg)
(C)
![img-5.jpeg](img-5.jpeg)

Fig. 3 Planned joint angle
B. Global Optimization Result

To test the effect of initial state's selection, disturbance is introduced to make the initial state deviate from the optimal state. Different fitness values such as the whole fitness values, fitness for compensability, and fitness for energy consumption are shown in figure 4, figure 5, and figure 6, respectively. Figure 4 illustrates that selecting the best solutions for the

initial state does not lead to the advantage in the whole trajectory. Since the initial state of the whole running procedure is optimal for compensability, the consequent points would be searched in the neighborhood of the state according to the proposed EDA frame and the little distance between adjacent tip points leads to the adjacency of optimal joint states. It is observed that individual optimization can guarantee the compensability of the 3 M system in the cost of energy consumption from figure 5 and figure 6.
![img-6.jpeg](img-6.jpeg)

Fig. 4 Fitness values for each discrete tip points
![img-7.jpeg](img-7.jpeg)

Fig. 5 Fitness values of compensability for each discrete tip points
![img-8.jpeg](img-8.jpeg)

Fig. 6 Fitness values of energy consumption for each discrete tip points

## VI. Conclusions

We propose a global optimization algorithm using EDA for the motion planning in the problem of trajectory tracking. Compared to genetic algorithm, EDA is fit to the identity of this problem and thus largely reduce the calculation time. Also global optimization is conducted here to compare with individual optimization. Individual optimization can find better solutions for the compensability of the 3 M system, while global optimization lead to better solutions from the whole fitness values especially reducing the energy consumption. It is practical to search for solutions with compensability as high as possible with tolerable energy consumption. Such conclusions are demonstrated in the simulation above and we expect to test the work on the experiment equipment in the near future.

## REFERENCES

[1] C. Sallaberger. Robotics and control R\&D in the Canadian space station program. In: Proc. of Canadian Conf. on Electrical and Computer Engineering. Calgary, Canada, 1996: 482-485.
[2] N. Hogan, A. Sharon and E D. Hardt. High bandwidth force regulation and inertia reduction using a macro/micro manipulator system. In: Proc. of IEEE Conf. on Robotics and Automation. Phila., PA, USA, 1988: 126-132.
[3] I. Sharf. Active Damping of a Large Flexible Manipulator with a Short-Reach Robot. ASME Journal of Dynamic Systems Measurement and Control, 1996, 118:704-713.
[4] T. Yoshikawa, K. Hosoda, T. Doi and H. Murakami. Quasi-static trajectory tracking control of flexible manipulator by macromicro manipulator system. In: Proceedings of IEEE International Conf. on Robotics and Automation. Atlanta, USA, 1993: 210215.
[5] T. Yoshikawa, K. Hosoda, T. Doi and H. Murakami. Dynamic trajectory tracking control of flexible manipulator by macromicro manipulator system. In: Proceedings of IEEE International Conf. on Robotics and Automation. San Diego, USA, 1994: 1804-1809.
[6] K. Motoyuki, M. Yoshifumi et al. PDS Control of Macro-Micro Arm. In: Proceedings of the $8^{\text {th }}$ IEEE Int. Workshop on Advanced Motion Control. Kawasaki, Japan, 2004: 123-128.
[7] A. Mannami and H. A. Talebi. A Fuzzy Lyapunov-based Control Strategy for a Macro-micro Manipulator. In: Proceedings of IEEE Conf. on Control Applications. Istanbul, Turkey, 2003: 368-373.
[8] X. P. Cheng and R. V. Patel. Neural network based tracking control of a flexible macro-micro manipulator system. Neural Networks, 2003, 16: 271-186.
[9] T. W. Yang, W. L. Xu and S. K. Tso. Dynamic modeling based on real-time deflection measurement and compensation control for flexible multi-link manipulators. Dynamics and Control, 2001, 11: 5-24.