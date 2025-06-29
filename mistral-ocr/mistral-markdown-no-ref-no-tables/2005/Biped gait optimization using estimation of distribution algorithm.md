# Biped Gait Optimization Using Estimation of Distribution Algorithm 

Lingyun $\mathrm{Hu}^{1,2}$, Changjiu Zhou ${ }^{2}$, Zengqi Sun ${ }^{1}$<br>${ }^{1}$ Department of Computer Science and Technology, Tsinghua University, Beijing, 100084, P.R. China<br>${ }^{2}$ School of Electrical and Electronic Engineering, Singapore Polytechnic, 500 Dover Road, 139651, Singapore<br>huly02@mails.tsinghua.edu.cn, ZhouCJ@sp.edu.sg, szq-dcs@mail.tsinghua.edu.cn


#### Abstract

This paper proposes a new biped gait optimization method based on Estimation of Distribution Algorithm (EDA). It is able to explicitly extract global statistical information from the selected solutions and build a posterior probability distribution model of promising solutions based on the extracted information. Biped gait for a nine-link robot is firstly formulated as a multiobjective optimization problem with consideration of multiconstraints including balance and torque. Optimization parameters are angles at transition poses. Instead of searching the joint space directly, EDA is applied to estimate the probability distribution of each joint degree. By this means, inherent mapping relationship between joint coordinates and cost function can be described in term of probability density. Compared to common intelligent learning method, the proposed optimization method can formulate a proper and feasible combination of impulses by tuning less parameters and visiting less states. The effectiveness of the proposed EDA based biped gait optimization method has been tested on a soccer-playing humanoid robot named Robo-Erectus. Experiment results demonstrate that the learned trajectory makes a good balance between stability and energy cost in short learning epochs.


Index Terms - Biped robot, gait optimization, Estimation Distribution Algorithm, probability distribution.

## I. INTRODUCTION

Current research on humanoid robots and biped locomotion is one of the most exciting topics in the filed of robotics. As a basic research topic, stable and intelligent biped trajectory generation attracts one's interests from the beginning. Since 1985, Kawarmura et al. had proposed a learning method to precisely follow the desired trajectory of each joint [1]. Later in 1992, Li et al. described an algorithm on using trunk motion to compensate the lower-limbs motion and to track the desired Zero Moment Point trajectory as close as possible [2]. Following this direction, many studies [3]-[5] employed such idea of deriving the hip motion to achieve the predefined desired ZMP trajectory. However, the actual walking stability of these methods depends greatly on the following three aspects: 1) Reasonability of the desired ZMP trajectory ; 2) Precision of the mathematical model; 3) Span and variation velocity of joint torques.

For a given robot, the third factor is mostly determined by hardware design. Recently, researchers have taken more attention to the first two directions [6]-[9]. A naturally good idea to solve these problems is to equip the robot controller
with some learning capabilities, which makes it possible for robots to follow the pre-designed trajectory. Various kinds of intelligent methods like neural networks, fuzzy logic, evolution algorithms and reinforcement learning have been introduced into trajectory learning. For example fuzzy logic is applied at the local control level for tuning local PID gains in [6]. The research showed that the aggregation-decomposition method for stability analysis of overall biped robot was applicable when local subsystems were stabilized with fuzzy regulator. Traditional feedforward neural network was developed as the controller by Juang [7]. Through learning, it could generate trajectory along a pre-defined path. A typical application of evolutionary algorithm in humanoid robotics was presented in [8], where Genetic Algorithm (GA) easily handled the constraints by using the penalty function vector and transformed a constrained problem into an unconstrained one. Zhou et al. formulated a reinforcement method for learning the parameters of rhythmic walking to generate a purposive motion [9].

However, the behaviour of these heuristic computation algorithms depends greatly on a large number of associated parameters. For the example of GAs, quality of evolution process is related to the parameters like operators and probabilities of crossing and mutation, population size, the number of generations and so on. Experiences are required to choose the suitable values for fast resolution. Furthermore, selection of best values for these parameters has been suggested to constitute an additional optimization problem. Moreover, sometimes the algorithms may behave worse than simpler search algorithms for sucking in local minima.

A population-based search algorithm namely Estimation of Distribution Algorithms (EDAs) [10] is employed for biped gait generation and optimization in this paper. EDAs try to predict the population movements in the search space as well as to avoid needing too many parameters. The first explicit description of a solution process consisting with suitable updating on probability distributions was given by Muhlenbein and PaaB [11]. Though the study of EDAs is relatively new, there already exist lots of different types of EDAs like Population-Based Incremental Learning (PBIL) [12], Estimation of Multivariate Normal Algorithm (EMNA) [13], Mutual Information Maximization for Input Clustering (MIMIC) [11] and so on. Since PBIL performs successfully on numerous benchmark and real world problems when compared to a variety of standard GAs and hill-climbing

algorithms. It is adopted in this paper to optimize the generated gaits under energy and stability criteria.

The rest of the paper is organized as follows. In the following section, biped pattern and the mechanical models are briefly introduced. Constraints used in gait generation are presented in the section III. In section IV, gait optimization is abstracted as a multi-objective optimization problem with geometric and state constraints. The EDA used to solve the problem is then demonstrated in section V. This is followed by the algorithm simulation results demonstration in section VI. Section VII is concluding remarks.

## II. Problem DEFINITION

## A. Biped Gait Pattern

This section introduces the gait model of an $N_{P}$-link planar biped robot consisting of a torso, two hips and two identical legs with ankles and knees. Biped walking is assumed to limit in sagittal plane and on a level surface. The main phases of one walking cycle are assumed to be swing phase and double support phase as shown in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Gait pattern of one cycle.

## - Swing Phase

The swing phase starts from the swing foot toeing off the ground and ends when the heel touches the ground. The swing foot reaches the highest point at $T_{a}$ and after $T_{b}$ lands on the ground. The transition moment between swing phase and double support phase is labeled as $T_{a}+T_{b}$.

This phase is modeled as a continuous forward motion in which, the support leg plays as a pivot and the other leg swings forward. Ground friction is assumed to be large enough to ensure no slippage between the supporting foot and walking surface. The mechanism dynamic model of biped robots can be expressed by similar dynamic Newton-Euler equation like manipulators as (1).

$$
\ddot{M}(q) \ddot{q}+\hat{C}(q, \dot{q})+\hat{G}(q)=\hat{\tau}
$$

Where $\dot{M}(q)=\left\{p_{i j} \cos \left(q_{j}-q_{i}\right)\right\}_{N_{p}>N_{p}}$ is the square matrix describing full inertia, $\hat{C}(q)=\left\{-p_{i j} \sin \left(q_{j}-q_{i}\right)\right\}_{N_{p}>N_{p}} \dot{q}$ and $\hat{G}(q)=\operatorname{diag}\left[-f_{i} \sin q_{i}\right]_{N_{p}>N}$ are the vector of centrifugal, Coriolis and gravitational moments acting at $N_{l}$ mechanism
joints respectively, $\hat{\tau}$ is the vector of driving moments at each joint. $J^{T}(q, \ddot{q})_{n_{1} N_{1}}$ is the corresponding Jacobi matrix of the system. Parameters $r_{i j}, s_{i j}$ and $h_{i}$ are constants derived by Lagrange's equation. $q$ is the coordinate sets describing the link locomotion in joint space with respect to a world reference frame, $\dot{q}$ is angular velocities. Inequality geometric constraints as shown in the next section are used to avoid collisions between ground and the swing foot.

- Double Support Phase

The double support phase begins at the moment that the front heel touching the ground and ends when the rear toe sways off at $T_{a}+T_{b}+T_{c}$ (as shown in Fig. 1). End configuration of this phase initiates the swing phase of the next gait cycle.

Landing impact happens at the beginning of double support phase. Transition between the two phases is assumed to take place in an infinitesimal length of time. This assumption entails the use of a rigid model to describe the impact between the swing leg and the ground [14]. The impulsive forces may cause an instantaneous velocity change in the generalized coordinates while the positions remain continuous. It can be described as (2).

$$
\ddot{M}(q) \ddot{q}+\hat{C}(q, \dot{q})+\hat{G}(q)=\hat{\tau}+\partial F_{e}
$$

Where $F_{e}$ is the integral of contact impulse at the impact instant. Since the stance leg is assumed to lift from the ground without interaction, only the external forces at the swing foot $F_{e}$ need to be considered. By supposing that the actuators are not impulsion, the velocity right after the impact $q$ can be represented as $\dot{q}^{\prime}=\Delta\left(\dot{q}^{\prime}\right)$, where $\dot{q}^{\prime}$ is the velocity right before the impact and $\Delta$ is a continuous function with unique solution.

After the landing impact moment, the mechanical kinematic chain in double support phase can be considered as a manipulator with end position constraints. The dynamical model is given in (3).

$$
\ddot{M}(q) \ddot{q}+\hat{C}(q, \dot{q})+\hat{G}(q)=\hat{\tau}+J^{T}(q, \ddot{q}) F
$$

Where $F$ is the vector of external forces and moments acting at the landing foot of the robot.

Totally three key poses are chosen in one cycle. Phases between these key poses are approximated by third order spline functions. A kind of these types of techniques has been implemented using splines of class $C^{2}$ in [15]. Such strategy guarantees the second order derivatives at every point, especially at connection points. Consequently, actuating torques is continuous at knots.

## B. Mathematical Model

The mathematical model of the biped locomotion proposed in [14] is modified in this paper. The spatial model defined in internal coordinate state space as shown in Fig. 2 will be used to synthesize the dynamic control of the biped mechanism and to verify the simulation research result. Definition of angular coordinates and disposition of the masses are also indicated in Fig. 2.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Mechanical model of the robot.

## III. CONSTRAINTS

Constraints are divided into two categories, namely geometric and state constraints in this section according to the definition space.
A. Geometric Constraints

Geometric constraints (GCs) ensure the feasibility of biped gaits from the point of physical structure. Since one gait can be regarded as a pose sequence that is generated by interpolating key poses, GCs will be constructed only at key poses. Two geometric constraints are taken into account.

GC1) Positions limitations of knots as (4).

$$
A_{p} \leqslant p \leqslant B_{p}
$$

Where $p=[p_{1}(t)]^{\mathrm{T}}, A_{p}=\left[A_{p_{1}}(t)\right]^{T}, B_{p}=\left[B_{p_{2}}(t)\right]^{T} \cdot p_{1}(t)=[x_{1}(t)$, $\left.y_{1}(t), z_{2}(t)\right]$ denotes center position of the $i^{\text {th }}$ link at $t$ moment. $i=1,2, \ldots, N_{t} . A_{p_{i}}(t)$ and $B_{p_{i}}(t)$ are lower limit and upper limit of $p_{1}(t)$. For the example of the position of the swing foot $p_{6}$ at $T_{a}, \quad A p_{6}\left(T_{a}\right)=\left[-\left(L_{6}+L_{1}+L_{2}\right), \quad-L_{6}, \quad L_{6}-a_{0}\right]$, $B p_{6}\left(T_{a}\right)=\left[L_{6}+L_{1}+L_{2}, 0, D_{6}\right] . L_{6}$ is the width of hip, $D_{6}$ is the max height of swing foot.

GC2) Structure limitations of joint angles as (5).

$$
A_{g} \leq q \leq B_{g}
$$

Where $q(t)=[q_{1}(t)]^{\mathrm{T}}$ stands for the joint angle at time t . $A_{g}=\left[A_{g_{1}}(t)\right]^{T}, B_{g}=\left[B_{g_{1}}(t)\right]^{T}, \mathrm{i}=0, \ldots, \mathrm{~N}_{t}=1 . A_{g_{i}}(t)$ and $B_{g_{i}}(t)$ are lower limit and upper limit of $q_{1}(t)$.
B. State Constraints

Three more kinds of state constraints including force, velocity and stability constraints are also taken into consideration in this paper. Details of each constraint are described as follows.

- Force constraints

During double support phase, the leg force must satisfy the
force constraint FC1 as shown in (6).

$$
\sum_{i=1}^{N_{t}} m_{i} p_{i}=f_{R}+f_{L}+\sum_{i=1}^{N_{t}} m_{i} g
$$

Where $f_{R}$ and $f_{L}$ are foot force at right and left legs respectively. $m_{i}, p_{i}$ are the mass and the acceleration of the $i^{\text {th }}$ link. Since only the sum $f_{R}+f_{L}$ is known during the double support phase, another force constraint FC2 is taken into assumption as the internal force $f_{d}$ in the closed loop structure must be minimized. It can be expressed as (7).

$$
f_{d}=\min \left\{F\left(f_{R}, f_{L}\right)\right\}
$$

Where $F$ is the function to calculate the internal force.

- Velocity constraints

Velocity constraints (VC) are considered to guarantee motion smoothness with respect to mechanical limitations of the biped system. VC can be simply written as:

$$
A_{g v} \leqslant \dot{q} \leqslant B_{g v}
$$

where $\dot{q}=\left[\dot{q}_{1}(t)\right]^{\mathrm{T}}, \dot{q}_{1}(t)$ denotes velocity of the $i^{\text {th }}$ actuated joint, $A_{g v}=\left[A_{g v_{1}}(t)\right]^{T}$ and $B_{g v}=\left[B_{g v_{1}}(t)\right]^{T}$ are lower and upper boundaries of the velocity $\dot{q}_{1}(t)$.

- Stability constraint

To achieve a dynamically stable gait, ZMP is usually used as a criterion [1-5]. The ZMP is defined as the point on the ground at which the net moment of the inertial forces and the gravity forces has no component along the horizontal axes [16]. It can be represented as (9) and (10).

$$
\begin{aligned}
& x_{\text {smp }}=\frac{\sum_{i}\left\{m_{i}(\ddot{z}_{i}+g) x_{i}-m_{i} \ddot{x}_{i} z_{i}-(I_{i} \dot{H})_{i, \dot{j}}}{\sum_{i} m_{i}(\ddot{z}_{i}+g)} \\
& y_{\text {smp }}=\frac{\sum_{i} m_{i}(\ddot{z}_{i}+g) y_{i}-m_{i} \ddot{y}_{i} z_{i}+(I_{i} \dot{H})_{i, \dot{j}}}{\sum_{i} m_{i}(\ddot{z}_{i}+g)}
\end{aligned}
$$

So the ZMP constraints $(\boldsymbol{Z C})$ should satisfy:

$$
A_{\text {smp }} \leqslant P_{\text {smp }} \leqslant B_{\text {smp }}
$$

Where $p_{\text {smp }}=\left[p_{\text {smp }}^{\prime}(t)\right]^{\mathrm{T}}, p_{\text {smp }}^{\prime}(t)=\left(x_{\text {smp }}^{\prime}(t), y_{\text {smp }}^{\prime}(t), 0\right)$ is position of the $i^{\text {th }} \mathrm{ZMP}, A_{\text {smp }}=\left[A_{\text {smp }_{1}}(t)\right]^{T}$ and $B_{\text {smp }}=\left[B_{\text {smp }_{2}}(t)\right]^{T}$ are lower and upper boundaries of the stable region respectively.

## IV. PERFORMANCE CRITERION

The proposed constrained dynamical model with geometric and state constraints provides the searching space boundary. Based on the proposed framework, an optimization procedure will be developed to select a continuous feasible solution by minimizing an appropriate cost function. Since analytical property of the performance criterion affects the optimal searching in terms of either dynamics or stabilities. ZMP displacement $\Upsilon_{1}$ and Energy cost $\Upsilon_{2}$ are chosen to form the cost function. Performance criterion is defined as:

$$
\begin{array}{ll}
\text { Minimize } & \Upsilon=\Upsilon_{1}+\Upsilon_{2} \\
\text { Subject to } & \\
\text { GC1 } & A_{p} \leq P \leq B_{p} \\
\text { GC2 } & A_{q} \leq q \leq B_{q}
\end{array}
$$

$$
\begin{array}{ll}
F C 1 & \sum_{i=1}^{N_{c}} m_{i} p_{i}=f_{R}+f_{L}+\sum_{i=1}^{N_{c}} m_{i} g \\
F C 2 & f_{R}=\min \left\{F\left(f_{R}, f_{L}\right)\right\} \\
V C & A_{q i} \leq q \leq B_{q i} \\
Z C & A_{\text {emp }} \leq P_{\text {emp }} \leq B_{\text {emp }}
\end{array}
$$

Where $Y_{1}=\int_{t=0}^{t_{0}+T_{0}+T_{1}}\left\|p_{\text {emp }}(t)-p_{\text {emp }}^{d}(t)\right\|^{2} d t$ estimates the Euclidean distance between the actual ZMP trajectory $p_{\text {emp }}$ and the desired one $p_{\text {emp }}{ }^{d} . \quad Y_{2}=\int_{-t=0}^{t_{0}+T_{0}+T_{1}} \tau(t) d t$ represents the dynamic load during one gait cycle $\left[0, T_{0}+T_{0}+T_{1}\right]$.

Let $s_{0}$ be the total number of discrete sample poses in one gait. Thus the cost function can be defined as (12).

$$
C(\bullet)=\beta_{f} f(\bullet)+\beta_{g} g(\bullet)=\sum_{i=1}^{N_{c}}\left(\beta_{f} \mathbb{N}\left(f_{i}(\bullet)\right)+\beta_{g} \mathbb{N}\left(g_{i}(\bullet)\right)\right)
$$

Where $f_{i}(\bullet)=\frac{1}{2}\left\|p_{\text {emp }}^{i}-p_{\text {emp }}^{d}\right\|^{2}$ calculates the Euclidean distance between the actual ZMP and the desired ZMP at the $i^{\text {th }}$ sample index. $g_{i}(\bullet)=\sum_{j=1}^{N_{c}} \tau_{i j}$ summarizes the torque of all actuated joints at the $i^{\text {th }}$ sample index. $\beta_{f}$ and $\beta_{g}$ are weights satisfying $\beta_{f}+\beta_{g}=1$ to balance between stability and energy cost. $\mathbb{N}$ is the normalization operator.

Appendix 1 proves that ZMP trajectory will satisfy third order spline interpolation function if joint trajectories are generated by the same function. That is, $f_{j=k_{0}}(\bullet)$ and $f_{j=k_{0,1}}(\bullet)$ makes a difference with $f_{k_{0}<j<k_{0,1}}(\bullet)$. So the proposed algorithm improves only key states to minimize the desired cost function.

## V. EDA

The proposed algorithm adopts a new evolutionary algorithm EDA [10]. It is based on the probabilistic model where selection and recombination of building blocks of GAs are replaced by generating new solutions through sampling the probability distribution which is calculated from the selected promising solutions. The probabilistic model is in an explicit model of promising regions of the searching space.

As the input coordinates $q_{i}\left(i=1, \ldots, N_{i}\right)$ of the $N_{i}$ links in joint space are considered to satisfy multivariate normal distribution $\Pi_{i=1}^{N_{i}} p_{i}\left(q_{i}\right)$, which is the product of $N_{i}$ independent univariate normal distributions $p_{i}\left(q_{i}\right)$, the population of solution is replaced by two vectors. One is the mean values of Gaussian normal distribution $\mu_{i}$ and the other is the standard deviation $\sigma_{i}$ for each optimized variable $q_{i}$. No interactions among the variables are covered. After generating a number of new solutions, the mean values $\mu_{i}$ are shifted towards the best of the generated solutions and the standard deviation $\sigma_{i}$ is
reduced to make future exploration of the search space narrower.

The algorithm can be summarized as follows.

1. Give a multivariate Gaussian distribution of mean $\mu_{i}$ and standard deviation $\sigma_{i}$.
2. While termination condition is not met:
a) Generate a population of $P$ individuals.
b) Select the best $Q$ individuals from parent generation $k$ 's population.
c) Update the multivariate Gaussian distribution using the $Q$ selected individuals. The mean and standard deviation of each univariate distribution are updated in the following ways as (13) and (14).

$$
\begin{aligned}
& \mu_{i}(k+1)=(1-\alpha) \mu_{i}(k)+\alpha\left(\mu_{i, \text { best }}(k)+\mu_{i, 2, \text { subsec }}(k)-\mu_{i, \text { swav }}(k)\right) \\
& \sigma_{i}(k+1)=(1-\alpha) \sigma_{i}(k)+\alpha \sqrt{\frac{1}{Q} \sum_{i=1}^{Q}\left(\mu_{i}^{j}(k)-\hat{\mu}_{i}^{j}(k)\right)^{2}}
\end{aligned}
$$

Where $\mu_{i, \text { best }}(k), \mu_{i, 2, \text { subsec }}(k)$ and $\mu_{i, \text { swav }}(k)$ are the values of the best, second best and worst individual (with respect to the cost function) of the $i$ th variable at iteration $k . \mu_{i}^{j} j=1, \ldots, Q$ are the $Q$ best individuals for the $i$ th variable and $\hat{\mu}_{i}^{j}$ is their mean. $\alpha$ is the learning rate.

## VI. SimULATION RESULTS

To show the effectiveness of the proposed algorithm, we apply it on the digital robot model of humanoid robot named Robo-Erectus (RE) as shown in Fig. 3 [17]. Height and weight of RE are 600 mm and 4.6 kg respectively. Totally 23 DOFs are designed in RE as 6 per leg, 4 per arm and 1 for head, 2 for waist. They are driven by servo motor with maximum torque as $30 \mathrm{~kg} \times \mathrm{cm}$. One notebook powered with window XP operation system is set on RE for online control. It is one of the foremost leading soccer-playing humanoid robots, in the RoboCup Humanoid League. (www.roboerectus.org)
![img-2.jpeg](img-2.jpeg)

Fig. 3 Humanoid robot Robo-Erectus.

Based on the robot, a simplified model as shown in Fig. 2 is constructed for simulation experiment. Basic structure parameters of the model are $N_{l}=7, N_{k p}=4, s_{n}=10, L_{h}=10 \mathrm{~cm}$, $L_{0}=4 \mathrm{~cm}, L_{l}=L_{2}=8 \mathrm{~cm}, L_{3}=20 \mathrm{~cm}, M_{0}=0.1 \mathrm{~kg}, M_{l}=M_{2}=0.2 \mathrm{~kg}$, $M_{l}=1 \mathrm{~kg}$. Desired ZMP is set as the middle line in the stable region. Other parameters used in EDA are designed as $Q=40$, $P=20, \alpha=0.01$. EDA stops learning after 200 iterations.

Fig. 4 exhibits the probability distribution $\operatorname{Pro}\left(q_{1}\right)$ of $q_{1}$ in the ten looping times. Probability distribution functions $\operatorname{Pro}\left(q_{i}\right)$ of other coordinate parameters $q_{i}$ converge similarly like $\operatorname{Pro}\left(q_{1}\right) . i=1, \ldots, N_{l}$. Variation of torque and ZMP in the learning procedure are shown in Fig. 5 and Fig. 6 respectively, from which it can be found that both of them converge to reasonable values after EDA learning.
![img-3.jpeg](img-3.jpeg)

Fig. 4 Probability model of $q(1)$.
![img-4.jpeg](img-4.jpeg)

Fig. 5 Torque of learned gait in one cycle.
![img-5.jpeg](img-5.jpeg)

Fig. 6 ZMP trajectory of learned gait in one cycle.

## VI. CONCLUSIONS

We propose a general biped gait optimization algorithm based on EDA in this paper. Gait synthesis of the biped locomotion is formulated as a multi-objective optimization problem. By supposing that the probability distribution of each joint degree satisfies Gaussian distribution function, EDA is applied to find the stable and low energy cost joint degree permutation. To the best of our knowledge, the proposed algorithm is the first biped gait optimization method using EDA. It can be easily extended on more joints for more complex robot structure, which will be discussed in the future. We will also look at how to use computational learning approaches, e.g. fuzzy reinforcement learning [19] to further optimize biped gaits.

## APPENDIX I

In this section, we will prove that if joint trajectory $\left(x_{i}^{j}\right.$, $\left.y_{i}^{j}, z_{i}^{j}\right)$ is generated by third order spline interpolation functions $\left(S x_{i}^{3}, S y_{i}^{3}, S z_{i}^{3}\right)$, the corresponding ZMP trajectory $\left(x_{i, \text { imp }}^{i}, y_{i, \text { imp }}^{i}\right)$ also satisfies third order spline interpolation functions $\left(S x_{i, \text { imp }}^{i}, S y_{i, \text { imp }}^{i}\right)$.

Proof: Take the example of $x_{i, \text { imp }}^{i}$.

$$
\begin{aligned}
& \text { Since } z_{i}^{i}(t)=S_{z_{i}^{i}}(t)=A_{z_{i}^{i}} t^{3}+B_{z_{i}^{i}} t^{2}+C_{z_{i}^{i}} t+D_{z_{i}^{i}} \\
& x_{i}^{j}(t)=S_{x_{i}^{j}}(t)=A_{x_{i}^{j}} t^{3}+B_{x_{i}^{j}} t^{2}+C_{x_{i}^{j}} t+D_{x_{i}^{j}}
\end{aligned}
$$

Then $\ddot{z}_{i}^{i}(t)=\ddot{S}_{z_{i}^{i}}(t)=6 A_{z_{i}^{i}} t+2 B_{z_{i}^{i}}$

$$
\ddot{x}_{i}^{j}(t)=\ddot{S}_{x_{i}^{j}}(t)=6 A_{x_{i}^{j}} t+2 B_{x_{i}^{j}}
$$

$A_{z_{i}^{i}} \cdot B_{z_{i}^{i}} \cdot C_{z_{i}^{j}} \cdot D_{z_{i}^{i}} \cdot A_{z_{i}^{j}} \cdot B_{z_{i}^{i}} \cdot C_{z_{i}^{j}} \cdot D_{z_{i}^{j}}$ are parameters produced by the key states and predetermined gait parameters like gait length and gait height. It leads to

$$
\begin{aligned}
x_{\text {emp }}^{j}= & \sum_{i=1}^{n} m_{i}\left(\ddot{z}_{j}^{i}+g\right) x_{j}^{i}-\sum_{i=1}^{n} m_{i} \ddot{x}_{j}^{i} z_{j}^{i} \\
& \sum_{i=1}^{n} m_{i}\left(\ddot{z}_{j}^{i}+g\right) \\
= & \sum_{i=1}^{n} m_{i}\left(\ddot{S}_{z_{j}}(t)+g\right)\left(S_{z_{j}^{i}}(t)\right)-\sum_{i=1}^{n} m_{i} \ddot{S}_{z_{j}^{i}}(t)\left(S_{z_{j}^{i}}(t)\right) \\
& \sum_{i=1}^{n} m_{i}\left(\ddot{S}_{z_{j}^{i}}(t)+g\right) \\
= & \sum_{i=1}^{n} m_{i}\left(6 A_{z_{j}^{i}} t+2 B_{z_{j}^{i}}+g\right)\left(A_{z_{j}^{i}} t^{3}+B_{z_{j}^{i}} t^{2}+C_{z_{j}^{i}} t+D_{z_{j}^{i}}\right) \\
& \sum_{i=1}^{n} m_{i}\left(6 A_{z_{j}^{i}} t+2 B_{z_{j}^{i}}+g\right) \\
= & A_{z_{\text {emp }}} t^{3}+B_{z_{\text {emp }}} t^{2}+C_{z_{\text {emp }}} t+D_{z_{\text {emp }}} \\
= & S_{z_{\text {emp }}^{i}}(t)
\end{aligned}
$$

The same deduction can be carried on $y^{i}{ }_{\text {emp }}$.

## ACKNOWLEDGMENTS

We would like to thank staff and students at the Advanced Robotics and Intelligent Control Center (ARICC) of Singapore Polytechnic for their support in the development of humanoid robots named Robo-Erectus. The research described in this paper was made possible by the jointly support of the Singapore Tote Fund and the Singapore Polytechnic R\&D Fund.
