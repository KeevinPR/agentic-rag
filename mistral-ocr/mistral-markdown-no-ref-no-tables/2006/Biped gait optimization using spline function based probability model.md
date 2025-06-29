# Biped Gait Optimization Using Spline Function Based Probability Model 

Lingyun $\mathrm{Hu}^{1,2}$, Changjiu $\mathrm{Zhou}^{2}$, Zengqi Sun ${ }^{1}$<br>${ }^{1}$ Department of Computer Science and Technology, Tsinghua University, Beijing, 100084, P.R. China<br>${ }^{2}$ School of Electrical and Electronic Engineering, Singapore Polytechnic, 500 Dover Road, 139651, Singapore<br>Email: huly02@mails.tsinghua.edu.cn, ZhouCJ@sp.edu.sg, szq-dcs@mail.tsinghua.edu.cn


#### Abstract

A new Estimation of Distribution Algorithm (EDA) with spline kernel function (EDA_S) is proposed to optimize biped gait for a nine-link humanoid robot. Gait synthesis of the biped locomotion is firstly formulated as a multi-constraint optimization problem with consideration of two objectives, including zero-moment point (ZMP) for dynamically stable locomotion and driving torque for energy efficiency. The parameters to be optimized are joint coordinates at transition poses between three successive phases. Rather than searching in joint angle permutation space directly, the proposed method approximates the probability distribution by Catmull-Rom (CR) cubic spline function and updates them with gradient descent learning strategy. The effectiveness of EDA_S for biped gait optimization has been successfully tested on the simulated model of a humanoid soccer robot. It is shown that the flexible kernel with the updating rule is able to remarkably accelerate the learning speed with comparison to the traditional EDA.


Index Terms-Biped robot, gait optimization, probability distribution, EDA, spline function.

## I. INTRODUCTION

Researches related to humanoid robot have made notable progress in design, control and systemization of biped machine. However, gait generation and optimization still remains a challenge for such a high-order highly-coupled nonlinear dynamical system. To create valid biped walking, various criteria have been proposed such as stability and energy efficiency.

Zero Moment Point (ZMP) is one of the mostly used stability criteria for biped gaits. Recent humanoid robots using ZMP control strategies have demonstrated impressive biped walking [1, 2]. However, stability criterion is not good enough to guarantee the feasibility of biped gaits. Research of energy consumption in biped walking provides another useful criterion for gait optimization. In 1990, McGeer presented the possibility of passive dynamic walking [3]. Followed with him, several studies have explored energy efficient biped walking [4].

With consideration of the two criteria, many researches focus on intelligent paradigms including connectionist theory [5], fuzzy logic [6] and Genetic Algorithm (GA) [7] to optimize biped gaits. However, these heuristic computation algorithms depend greatly on a large number of associated parameters. Experiences are required to choose the suitable values for fast resolution.

To get the solution with less parameter, a new type of
population-based searching algorithm named Estimation of Distribution Algorithms (EDAs) is adopted in this paper [8]. EDAs try to predict the population movements in the search space as well as to avoid needing too many parameters. Being one type of EDAs for combinatorial optimization, $\mathrm{PBIL}_{\alpha}$, the extension of the Boolean PBIL (Population-Based Incremental Learning) to continuous space, performs successfully on numerous benchmark and real world problems with comparison to a variety of standard GAs and hill-climbing algorithms [9]. It is used in this paper to optimize the generated biped gaits under energy and stability criteria with the assumption that selected variables are independent.

However, Gaussian function is not able to precisely describe complex multi-peak distribution. So the proposed algorithm EDA_S updates traditional EDA with non-parametric technique, namely spline functions [10], to address the probability distribution of joint coordinates. The essence of spline-based probability model is to represent an arbitrary continuously probability function with a discrete sum of weighted and shifted Catmull-Rom (CR) basis functions. Sampling points are updated according to gradient descent method. In this paper, we demonstrated that CR spline function, as a kind of sub-optimization way of cubic spline, can approximate arbitrary continuous function with arbitrarily high quality too. This will speed up the modification of distribution density model and consequently accelerate the joint permutation searching. Also the quality of the proposed method is only affected by a few parameters. This has been tested by the application in biped gait optimization.

## II. Problem background

Gait pattern of a nine-link biped robot is presented in this section to produce optimization parameters. Followed with it is the mathematic model for constraints definition.

## A. Biped gait pattern

Gait model of a $N_{i}$ links planar biped robot consisting of a torso, two hips and two identical legs with ankles and knees is analyzed. Biped walking is assumed to limit in sagittal plane and on a level surface, consisting the swing and double support phases as shown in Fig. 1.

- Swing Phase

The swing phase starts from the swing foot toeing off the ground and ends when the heel touches the ground. The swing foot reaches the highest point at $T_{s}$ and after $T_{s}$ lands on the

![img-0.jpeg](img-0.jpeg)

Fig. 1. Gait pattern of one cycle.
ground. The transition moment between swing phase and double support phase is labeled as $T_{n}+T_{s}$.

This phase is modeled as a continuous forward motion in which, the support leg plays as a pivot and the other leg swings forward. Let $q$ be the coordinate sets describing the link locomotion in joint space with respect to a world reference frame. $\dot{q}$ is the angular velocity of the mechanism. With above assumptions, the mechanism dynamic model of biped robots can be expressed by similar dynamic Newton-Euler equation like manipulators as Equation (1).

$$
\stackrel{\circ}{M}(q) \ddot{q}+\hat{C}(q, \dot{q})+\hat{G}(q)=\hat{\tau}
$$

Where $\stackrel{\circ}{M}(q)=\left\{p_{i j} \cos \left(q_{j}-q_{i}\right)\right\}_{N_{i}+N_{j}}$ is the square matrix describing full inertia, $\hat{C}(q)=\left\{-p_{i j} \sin \left(q_{j}-q_{i}\right)\right\}_{N_{i}+N_{j}} \dot{q}$ and $\hat{G}(q)=\operatorname{diag}\left\{-f_{i} \sin q_{i}\right\}_{N_{i}=1}$ are the vector of centrifugal, Coriolis and gravitational moments acting at $N_{i}$ mechanism joints respectively, $\hat{\tau}$ is the vector of driving moments at each joint. $J^{\hat{\tau}}(q, \dot{q})_{h=N_{i}}$ is the corresponding Jacobi matrix of the system. Parameters $r_{i j}, s_{i j}$ and $h_{i}$ are constants derived by Lagrange's equation. Inequality geometric constraints as shown in the next section are used to avoid collisions between ground and the swing foot.

- Double Support Phase

The double support phase begins at the moment that the front heel touching the ground and ends when the rear toeing sways off at $T_{n}+T_{s}+T_{c}$ (as shown in Fig. 1). End configuration of this phase initiates the swing phase of the next gait cycle.

Landing impact happens at the beginning of double support phase. The impulsive forces may cause an instantaneous velocity change in the generalized coordinates while the positions remain continuous. It can be described by Equation (2).

$$
\stackrel{\circ}{M}(q) \ddot{q}+\hat{C}(q, \dot{q})+\hat{G}(q)=\hat{\tau}+\hat{c} F_{e}
$$

Where $F_{e}$ is the integral of contact impulse at the impact instant. By supposing that the actuators are not impulsion, the velocity right after the impact $\dot{q}^{+}$can be represented as $\dot{q}^{+}=\Delta\left(\dot{q}^{-}\right)$, where $\dot{q}^{-}$is the velocity right before the impact and $\Delta$ is a continuous function with unique solution.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Mechanical model of the robot.
After the impact moment, the mechanical kinematic chain in double support phase can be considered as a manipulator with end position constraints. The dynamical model is given in Equation (3).

$$
\stackrel{\circ}{M}(q) \ddot{q}+\hat{C}(q, \dot{q})+\hat{G}(q)=\hat{\tau}+J^{\hat{\tau}}(q, \ddot{q}) F
$$

Where $F$ is the vector of external forces and moments acting at the landing foot of the robot.

It can be seen from Fig. 1, totally three key poses are chosen in one cycle. Phases between these key poses are approximated by third order spline functions. Such strategy guarantees the second order derivatives at every point, especially at connection points. Consequently, actuating torques is continuous at knots.

Ratio between swing and double support periods is a function of walking velocity [2]. To be mentioned in simulation as an example, swing phase is set to be twenty percent of one walking cycle according to [2].

## B. Mathematical model

The mathematical model of the biped locomotion proposed in [11] is modified in this paper. The spatial model defined in internal coordinate state space as shown in Fig. 2 will be used to synthesize the dynamic control of the biped mechanism and to verify the simulation research result. Definition of angular coordinates and disposition of the masses are also indicated in Fig. 2. The supporting ankle, noted as $l_{0}$ is adopted as the basic link of the mechanism. Since only symmetric gaits are considered, the same model can be used for different supporting leg by re-labeling coordinates.

## III. CONSTRAINTS

Natural principles for biped gait control criteria should include 1) anthropomorphic characteristics of a gait; 2) dynamic balance during the locomotion; 3) energy cost at robot joints; 4) impact between swing foot and the ground at the contact moment. Since dynamical model of the biped robot considers only the last criterion, other three one will be realized through constraints design.

Constraints are divided into two categories, namely geometric and state constraints in this section according to the

definition space.

## A. Geometric constraints

Geometric constraints (GCs) ensure the feasibility of biped gaits from the point of physical structure. Since one gait cycle can be regarded as a pose sequence that is generated by interpolating key poses, GCs will be constructed only at key poses. Two geometric constraints are designed as follows.

GC1) Positions limitations of knots as shown in Equation (4).

$$
A_{p} \leq p(\phi) \leq B_{g}
$$

Where $p=\left[p_{i}(t)\right]^{T}, A_{p}=\left[A_{p_{i}}(t)\right]^{T}, B_{p}=\left[B_{p_{i}}(t)\right]^{T}, p_{i}(t)=$ $\left[x_{i}(t), y_{i}(t), z_{i}(t)\right]$ denotes center position of the $i$ th link at $t$ moment, $i=1,2, \ldots, N_{i}, A_{p_{i}}(t)$ and $B_{p_{i}}(t)$ are lower limit and upper limit of $p_{i}(t)$.
GC2) Structure limitations of joint angles as shown in Equation (5).

$$
A_{q} \leq q(\phi) \leq B_{q}
$$

Where $q=\left[q_{i}(t)\right]^{T}$ stands for the joint angle at time $t$, $i=0,1, \ldots, N_{i}-1, A_{q}=\left[A_{q_{i}}(t)\right]^{T}, B_{q}=\left[B_{q_{i}}(t)\right]^{T}, A_{q_{i}}(t)$ and $B_{q_{i}}(t)$ are lower limit and upper limit of $q_{i}(t)$.

## B. State constraints

Three more kinds of state constraints include force, velocity and stability constraints are also taken into consideration.

- Force constraints

During double support phase, the leg force must satisfy the force constraint FC1 as

$$
\sum_{i=1}^{N_{i}} m_{i} \ddot{p}_{i}=f_{R}+f_{L}+\sum_{i=1}^{N_{i}} m_{i} g
$$

Where $f_{R}$ and $f_{L}$ are foot force at right and left legs respectively. $m_{i}, \ddot{p}_{i}$ are the mass and the acceleration of the $i$ th link. Since only the sum $f_{R}+f_{L}$ is known during the double support phase, another force constraint FC2 (as shown in Equation (9)) is taken into assumption as the internal force $f_{d}$ in the closed loop structure must be minimized.

$$
f_{d}=\min \left\{F\left(f_{R}, f_{L}\right)\right\}
$$

Where $F$ is the function to calculate the internal force.

- Velocity constraints

Velocity constraints (VC) are considered to guarantee motion smoothness with respect to mechanical limitations of the biped system. VC can be simply written as

$$
A_{q} \leq \dot{q}(\phi) \leq B_{q}
$$

Where $A_{q}=\left[A_{q_{i}}(t)\right]^{T}$ and $B_{q}=\left[B_{q_{i}}(t)\right]^{T}$ are lower and upper boundaries of the velocity $\dot{q}_{i}(t)$.

- Stability constraint

To achieve a dynamically stable gait, ZMP is usually used as a criterion [1, 2]. The ZMP is defined as the point on the ground at which the net moment of the inertial forces and the gravity forces has no component along the horizontal axes [12]. It can
be represented as Equations (11) and (12).

$$
\begin{aligned}
& x_{\text {zmp }}=\frac{\sum_{i=1}^{N_{i}}\left[m_{i}(\ddot{z}_{i}+g) x_{i}-m_{i} \ddot{x}_{i} z_{i}-\left(I_{i} \ddot{\theta}_{i}\right)_{x_{i}}\right]}{\sum_{i=1}^{N_{i}}\left(\ddot{z}_{i}+g\right)} \\
& y_{\text {zmp }}=\frac{\sum_{i=1}^{N_{i}}\left\{m_{i}(\ddot{z}_{i}+g) y_{i}-m_{i} \ddot{y}_{i} z_{i}+\left(I_{i} \ddot{\theta}_{i}\right)_{y_{i}}\right\}}{\sum_{i=1}^{N_{i}}\left(\ddot{z}_{i}+g\right)}
\end{aligned}
$$

To achieve dynamically stable gait, the ZMP constraints $(\boldsymbol{Z C})$ should satisfy

$$
p_{\text {zmp }}(\phi) \in S_{\text {zmp }}\left(A_{\text {zmp }}, B_{\text {zmp }}\right)
$$

Where $p_{\text {zmp }}=\left(x_{\text {zmp }}, y_{\text {zmp }}, 0\right)^{T}, S_{\text {zmp }}$ is the support polygon defined by $A_{\text {zmp }}$ and $B_{\text {zmp }}$, which are lower and upper boundaries of the stable region respectively.

## IV. PROBLEM FORMULATION

The proposed constrained dynamical model with geometric and state constraints provides the searching space boundary. Based on the proposed framework, an optimization procedure will be developed to select a continuous feasible solution by minimizing an appropriate cost function. Since analytical property of the performance criterion affects the optimal searching in terms of either dynamics or stabilities. ZMP displacement $Y_{1}$ and energy cost $Y_{2}$ are chosen to form the cost function. Performance criterion is defined as:

## Minimize $\quad Y=Y_{1}+Y_{2}$

## Subject to

GC1 $\quad A_{p} \leq p(\phi) \leq B_{g}$
GC2 $\quad A_{q} \leq q(\phi) \leq B_{q}$
$\boldsymbol{F C 1} \quad \sum_{i=1}^{N_{i}} m_{i} p_{i}=f_{R}+f_{L}+\sum_{i=1}^{N_{i}} m_{i} g$
$\boldsymbol{F C 2} \quad f_{d}=\min \left\{F\left(f_{R}, f_{L}\right)\right\}$
$\boldsymbol{V C} \quad A_{q} \leq \dot{q}(\phi) \leq B_{q}$
$\boldsymbol{Z C} \quad p_{\text {zmp }}(\phi) \in S_{\text {zmp }}\left(A_{\text {zmp }}, B_{\text {zmp }}\right)$
Where $Y_{1}=\int_{t=0}^{T_{R}+T_{L}+T_{T}}\left\|p_{\text {zmp }}(t)-p_{\text {zmp }}^{d}(t)\right\|^{2} d t \quad$ estimates the Euclidean distance between the actual ZMP trajectory $p_{\text {zmp }}$ and the desired one $p_{\text {zmp }}^{d} . Y_{2}=\int_{t=0}^{T_{R}+T_{L}+T_{T}} \tau(t) d t$ represents the dynamic load during one gait cycle $\left[0, T_{a}+T_{b}+T_{c}\right]$.

Let $N_{p}$ be the total number of discrete sample poses in one cycle. Thus the cost function can be defined as Equation (14).

$$
Y(\bullet)=\beta_{f} f(\bullet)+\beta_{g} g(\bullet)=\sum_{i=1}^{N_{p}}\left(\beta_{f} \mathbb{N}\left(f_{i}(\bullet)\right)+\beta_{g} \mathbb{N}\left(g_{i}(\bullet)\right)\right.
$$

Where $f_{i}(\bullet)=\frac{1}{2}\left\|p_{\text {zmp }}^{i}-p_{\text {zmp }}^{d}\right\|^{2}$ calculates the Euclidean distance between the actual ZMP and the desired ZMP at the $i$ th sampling index. $g_{i}(\bullet)=\sum_{j=1}^{N_{i}} \tau_{i j}$ summarizes the torque of all actuated joints at the $i$ th sample index. Where $N_{i}$ is the number

of driving torques. $\beta_{f}$ and $\beta_{g}$ are weights satisfying $\beta_{f}+\beta_{g}=1 . \mathbb{N}$ is the normalization operator.
It is proved that ZMP trajectory will satisfy third order spline interpolation function if joint trajectories are generated by the same function [13]. So the proposed algorithm improves only key states to minimize the desired cost function.

## V. Spline FUNCTION BASED EDA

A new evolutionary algorithm named EDAs is adopted to solve the biped gait optimization problem. EDA is based on the probability distribution function where selection and recombination of building blocks in GAs are replaced by selection from probability models and modification of probability models [8].
As the input coordinates $q_{i}(i=1,2, \ldots, N_{i})$ of the $N_{i}$ links in joint space are considered independent, their probability distribution functions satisfy $\Pi_{i=1}^{N_{i}} \operatorname{Pro}_{i}\left(q_{i}\right)$, which is the product of $N_{i}$ univariate distribution $\operatorname{Pro}_{i}\left(q_{i}\right)$. To describe the multi-model distribution function for each joint coordinate exactly, one non-parametric model, spline function, is used with cubic CR basis in the proposed method EDA_S. The kernels will be updated with gradient descent method. By this means, EDA_S can characterize more complex distribution functions since every continuous function on a closed interval can be approximated uniformly to any prescribed accuracy by a polynomial [14].

## A. Spline function based probability model

Different from traditional probability model, the proposed algorithm employs piecewise polynomial spline interpolation schemes, which is local adaptive and has continuous first order derivative. For given points $\left\{W_{1} \ldots W_{N w}\right\}, W_{i}=\left[w_{x_{i}}, w_{y_{i}}\right]^{T}$, a general spline can be described by Equation (15).

$$
F(u)=\bigcup_{i=1}^{N_{i}} F_{i}(u)
$$

Where $\bigcup$ is the concatenation operator on local spline basis functions. $N_{w}$ is the number of points and

$$
F_{y_{i}}(u)=\sum_{j=0}^{3} C_{y}(u) w_{y_{i+j}}
$$

$F_{y_{i}}(u)(0 \leqslant u \leqslant 1)$ is the $r$ th curve span function controlled by four points $\left[W_{i}, W_{r+1}, W_{r+2}, W_{r+3}\right]^{T}$ and $C_{y}(u)$ is the CR cubic spline basis, which is a sub-optimal and adaptive realization of the cubic spline function with the kernel $\left|x^{3}\right|$. We use CR spline, as shown in Equation (17), due to its low computation load and local characteristic to avoid the oscillatory in global adaptation. Cubic polynomials are chosen to achieve a better balance between the computational complexities and to guarantee both continuity and the existence of its derivatives.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Structure of spline functions.

$$
C(u)=\left[\begin{array}{c}
C_{x}(u) \\
C_{y}(u) \\
C_{z}(u) \\
C_{x}(u)
\end{array}\right]=\left[\begin{array}{ccc}
u^{3} \\
u^{2} \\
u \\
1
\end{array}\right]=\left[\begin{array}{ccc}
-1 & 3 & -3 & 1 \\
2 & -5 & 4 & -1 \\
-1 & 0 & 1 & 0 \\
0 & 2 & 0 & 0
\end{array}\right]
$$

For input $W=\left[w_{x}, w_{y}\right]^{T}$, proper local parameters of $u$ and $r$ can be obtained by $W_{x}=F_{x_{x}}(u)$. To accelerate the computation of local parameters and to reduce free parameters, we uniformly sample the x -axis with fixed step length $\Delta w=w_{x_{i+1}}-w_{x_{i}}$. This turns $F_{x_{x}}(u)$ to a first degree polynomial as

$$
F_{x_{x}}(u)=u \Delta w+w_{x_{x}}
$$

It has been proved that function smoothness can be tuned by $\triangle w$, which is insensitive to generalization error in a suitable range [15]. So the proposed method sets it by manual tuning.

Supposing $q_{j}^{i}$ is the input angle of joint $j$ at the $i$ th key pose in one gait cycle. Output of this model $\operatorname{Pro}_{j}^{i}$ can be calculated by Equations (19) to (21) (see Fig. 3). Where $i=1,2, \ldots, N_{k p}$, $j=1,2, \ldots, N_{i}$.

$$
\begin{gathered}
r_{j}^{i}=\left\{\frac{q_{j}^{i}}{\Delta w}+\frac{N_{k p}}{2}\right\} \\
u_{j}^{i}=\frac{q_{j}^{i}}{\Delta w}+\frac{N_{k p}}{2}-r_{j}^{i} \\
\operatorname{Pro}_{j}^{i}=F_{j, y_{i}}^{i}(\cdot)=\sum_{m=0}^{3} w_{j, y_{i+1}}^{i} C_{j, m}^{i}\left(u_{j}^{i}\right)
\end{gathered}
$$

Equations (19) and (20) implement local parameter computation. $\square$ is the floor operator and the second term in Equation (19) is designed to guarantee $u_{j}^{i}$ be always nonnegative.

The CR spline approximation error is a function of the sampling step $\triangle w$ and approximation order $L$. Since CR spline is a sub-optimal of the cubic spline function, it can also be understood as a subclass of Moms functions, which stands apart as the best achievable compromise between approximation quality and speed [16].

## B. Gradient descent updating rule

Supposing that $D_{j}^{i}(t)$ is the desired output. Consider a representation of the cost function $C(q)$ using a Boltzmann distribution as

$$
D_{j}^{i}(x)=\frac{1}{Z} e^{-\frac{Z t(q)}{T}}=\frac{1}{Z} e^{\frac{1}{T c(q)}}
$$

Where $\bar{c}(q)=1 / c(q)$, then

$$
E_{d}(k)=\frac{1}{2}\left(D_{j}^{i}(k)-\operatorname{Pro}_{j}^{i}(k)\right)^{2}
$$

Equation (23) is the squared output error related to the $k$ th iteration. According to gradient descent algorithm, the control points are updated with anti-gradient of error surface as

$$
q_{j, c_{1}^{(j,+m)}}^{i}(k+1)=q_{j, c_{1}^{(j,+m)}}^{i}(k)-\mu_{k} \frac{\partial E_{d}(k)}{\partial q_{j, c_{1}^{(j,+m)}}^{i}(k)}
$$

Where $\mu_{k}$ is learning rates for control points. $m=0, \ldots, 3$, $i=1,2, \ldots, N_{k p}, j=1,2, \ldots, N_{l}$. By substituting (23) to (24), we have

$$
q_{j, c_{1}^{(j,+m)}}^{i}(k+1)=q_{j, c_{1}^{(j,+m)}}^{i}(k)+\mu_{k}\left(D_{j}^{i}(k)-\operatorname{Pro}_{j}^{i}(k)\right) C_{c, m}^{i}\left(n_{j}^{i}(k)\right)
$$

## C. $E D A \_S$

The proposed algorithm EDA_S can be outlined as follows.

1. Give a multivariate distribution model $\operatorname{Pro}_{j}^{i}(1)$ represented by $N_{m}$ random sample points $q_{j, 1}^{j}$, $l=1,2, \ldots, N_{m}, i=1,2, \ldots, N_{k p}, j=1,2, \ldots, N_{l}$.
2. Generate a population of $N_{n}$ individuals.
3. While termination condition is not met:
a) Select the best $N_{n}$ individuals from parent generation $k$ 's population according to cost function value $\Upsilon$.
b) Update $q_{j, j}^{i}(k)$ and $\operatorname{Pro}_{j}^{i}(k)$ with the $N_{b}$ individuals according to Equations (24) and (21).

## VI. EXPERIMENT RESULTS

To show the effectiveness of the proposed algorithm, we apply it on the simulation model of the humanoid robot named Robo-Erectus (RE) as shown in Fig. 4 [17]. Totally 23 Degree of Freedoms (DOFs) are designed in RE as 6 per leg, 4 per arm and 1 for head, 2 for waist. They are driven by servo motor with maximum torque as $30 \mathrm{~kg} \times \mathrm{cm}$. One notebook with window XP operation system is set on RE for online control. (www.robo-erectus.org)

Based on the robot, a simplified model as shown in Fig. 2 is
![img-3.jpeg](img-3.jpeg)

Fig. 4. Physical model of robot Robo-Erectus. (60cm, 4.6kg, 23 DOFs) constructed for simulation experiment. Basic structure parameters of the model are $N_{l}=9, N_{k p}=3, N_{p}=10$, $L_{h}=10 \mathrm{~cm}, L_{0}=4 \mathrm{~cm}, L_{1}=L_{2}=8 \mathrm{~cm}, L_{3}=20 \mathrm{~cm}, D_{c}=20 \mathrm{~cm}$, $M_{b}=0.1 \mathrm{~kg}, M_{1}=M_{2}=0.2 \mathrm{~kg}, M_{3}=1 \mathrm{~kg}$. Desired ZMP is set as the middle line in the stable region.

Other parameters used in EDA are designed as $N_{v}=16$, $N_{h}=4, \beta_{f}=\beta_{g}=0.5$. Number of sample points $N_{w}=20$ is chosen empirically [15]. Terminal condition to stop learning is $\Upsilon(k)<3$ for five continuous iterations or $k>100$.

To verify the effectiveness of EDA_S, an analytical experiment is taken on it with comparison to traditional EDA with Gaussian distribution kernel $G\left(\mu_{i}, \sigma_{i}\right)$ (EDA_G). Same number of candidate solutions is generated in EDA_G to select the best, the second best and the worst samples for the modification on the means $\mu_{i}$ and covariance $\sigma_{i}$ [13]. Details of these two learning methods are given in Table I. Where $\alpha$ is the learning rate and $\hat{\mu}_{i}^{c}$ is the average value of $\mu_{i}^{c} \cdot \Upsilon^{c}(k)$ records the cost function value at the $k$ th iteration in the $i$ th experiment.

Fig 5. gives the value variation of the cost function by these two algorithms. It can be found that EDA_S stands out notably in term of convergent speed. Its cost function value reduces third of the initial value in less than 50 epoches while the cost function value of EDA_G does not show obvious descent tendency with the same learning rate. The avearage of ten times experiment results of EDA_S is also better than that of EDA_G (see Table I). The corresponding ZMP trajectory and joint torques of the learned gait is illustrated in Fig. 6 and Fig 7 with comparison to the one before learning. They regress to proper value in logical region as the learning goes on. To represent it more clearly, value variation of the two critera before normalization along the learning epoches is also exhibited.

It can be concluded that
TABLE I

![img-4.jpeg](img-4.jpeg)

Fig. 5. Cost function value in the first 100 loops.
1) Spline functions characterize the probability distribution in a more previous way.
2) Gradient descent updating rule plays an important role in acelerating the final learning. It makes EDA_S learning continuely even the best one in the current population is not significantly greater than the rest individuals.

## VII. CONCLUSION AND FUTURE WORK

This paper proposes a new biped gait optimization method EDA_S to achieve a dynamically stable and low energy cost walking by using EDA with spline kernel and gradient descent updating rule. A nine-link biped robot is firstly formulated as a nonlinear system with impulse effects, evolving in a subset of $R^{3}$. In this framework, the biped gait optimization can be modeled as a multi-object optimization problem with multi-constraints. By modeling the probability distribution of joint angles with the non-parametric kernel, EDA_S transfers the searching in infinite dimensional joint space to probability distribution space constructed by CR cubic spline functions. The effectiveness of EDA_S for biped gait optimization has been successfully tested on a humanoid soccer robot named Robo-Erectus [17], which has won several awards in RoboCup competitions. It is shown that the EDA_S is able to speed up
![img-5.jpeg](img-5.jpeg)

Fig. 6. Left figure shows ZMP trajectories before and after learning. Right figure is sum of distances between the real ZMP and Middle line of the stable region at sample points.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Left figure is joint torques before and after learning. Right figure is sum of torque at actuated joints at sample points.
learning by interpolating distribution function with gradient descent learning algorithm.

For the proposed spline-based EDAs for biped gait optimization, the basic assumption is that the joint angles are independent variables, which may not be valid for some more general applications. To find out more meaningful mapping between object function and state variables for biped gait generation and optimization, our next research will focus on the variable interrelationship in EDA's probability model for biped gait transition. We will also look at how to use computational learning approaches, e.g. fuzzy reinforcement learning to further optimize biped gaits [6].

## ACKNOWLEDGMENT

The research described in this paper is jointly supported by the Singapore Tote Fund and the Singapore Polytechnic R\&D Fund. It is also partially supported by the National Key Project for Basic Research of China (Grant No: 2002CB312205).
