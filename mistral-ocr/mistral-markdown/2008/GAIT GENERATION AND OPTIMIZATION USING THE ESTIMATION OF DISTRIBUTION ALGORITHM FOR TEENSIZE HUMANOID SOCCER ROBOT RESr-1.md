# GAIT GENERATION AND OPTIMIZATION USING THE ESTIMATION OF DISTRIBUTION ALGORITHM FOR TEENSIZE HUMANOID SOCCER ROBOT RESr-1 

LINGYUN HU and CHANGJIU ZHOU<br>Advanced Robotics and Intelligent Control Center (ARICC)<br>Singapore Polytechnic, 500 Dover Road, 139651, Singapore<br>http://www.robo-erectus.org<br>*ZhouCJ@sp.edu.sg<br>Received 30 July 2007<br>Accepted 30 January 2008


#### Abstract

This paper gives an overview of locomotion planning and control of a TeenSize humanoid soccer robot, Robo-Erectus Senior (RESr-1), which has been developed as an experimental platform for human-robot interaction and cooperative research in general and robotics soccer games in particular. The locomotion planning and control, along with an introduction of hierarchical control architecture, vision-based behavior and its application in the Humanoid TeenSize soccer challenge, are elaborated. The Estimation of Distribution Algorithm (EDA) is used in locomotion generation and optimization to achieves dynamically stable walk and a powerful kick. By setting different objective functions, smooth walking and powerful kicking can be generated quickly. RESr-1 made its debut at RoboCup 2007, and got fourth place in the Humanoid TeenSize penalty kick competition. In addition, some experimental results on RESr-1's walking, tracking and kicking are presented.


Keywords: Estimation of Distribution Algorithm; full-scale humanoid robot; walking and kicking gait generation and optimization; humanoid soccer robotics system.

## 1. Introduction

As humanoid robotics technology found its way into mainstream research in the past few decades, autonomous and safe locomotion systems aided by sensor information are becoming more important. The design of a full-size, general purpose and fully autonomous humanoid robots sets a new challenge area in humanoid robotics.

Typical humanoid experimental platforms, such as Asimo, ${ }^{3} \mathrm{H7},{ }^{13} \mathrm{HRP},{ }^{11} \mathrm{KHR},{ }^{8}$ PAL and so on, have been developed. Research topics on locomotion generation, sensor information integration, motivational and emotional control, human-robot interaction, etc. are being studied broadly with regard to these robots. Since humanoid robots are complicated, unstable and expensive by nature, it is difficult to construct

a human-like mechanical body, to integrate the sensor system, and to realize realtime motions.

To make the humanoid robot not only human-like outwardly but also easy for locomotion control, new ideas like automatic modular assembly and artificial muscle are being studied in the hardware design. The concept of modular actuators in physical structure construction is employed in the development of our humanoid robot Robo-Erectus Senior (RESr-1) as well. A modular humanoid platform consists of a set of independently designed standard modules, such as modular actuators, passive joints and rigid links (connectors), that can be rapidly assembled into different types of humanoid legged locomotion platforms with different kinematic and dynamic characteristics. As the actuators and joint modules can be interchangeable, and the connectors can be quickly fabricated, this modular design approach is able to reduce the complexity of the overall design problem to a manageable level. More importantly, the development cycle of the humanoid robot can be greatly shortened.

The objective of the RESr-1 project is to develop a modularly-based, configurable and reliable humanoid platform which can be used as a research platform for interaction and cooperative research in general and humanoid robotics soccer games in particular. However, as shown in Fig. 1, any increase in physical size will widen the locomotion range, and make locomotion planning and control algorithms complicated. This poses more challenges for humanoid research, particularly for the fullsize robots compared with KidSize ones. Computationally advanced and efficient algorithms are proposed for solving both the global navigation with obstacle avoidance and the local mechanics movement problems for TeenSize robots. Dynamical
![img-0.jpeg](img-0.jpeg)

Fig. 1. Contradictions exist in mechanical design of humanoid robots.

stability, energy cost, conformation similarity and other criteria are studied to quantify the locomotion quality precisely. In this paper, the zero moment point (ZMP) ${ }^{14}$ is used to estimate gait stability. Energy cost ${ }^{1}$ and kicking velocity are also considered in walking and kicking pattern generation.

Since the angular tracking error of RESr-1, as shown in the experimental result, is very small, a precise gait generation algorithm can be achieved. Moreover, the complicated mechanical structure of RESr-1 requires much computational power to collect feedback information and to synchronize whole body limbs.

Taking into consideration on precision and speed, the Estimation of Distribution Algorithm $(\mathrm{EDA})^{9}$ is employed in locomotion generation and optimization of RESr1. EDAs try to predict the population movements in the search space as well as to avoid involving too many parameters. By updating the probability function with selected individuals (with consideration of the objective function value), which is elitism in the available candidates, new samples can be generated from the modified probability model and thus feasible gaits can be achieved with the assumption that joint angles are independent variables.

This paper tests the traditional EDA to optimize the joint angle in biped walking and kicking with energy and stability criteria. First, a multilink biped robot is formulated as a nonlinear system with impulses to study the dynamic stability and energy cost of biped locomotion. Biped walking, formed by double support and swing phases, is represented by key poses extracted from one gait cycle. Then the probability distribution function of the generalized joint coordinates in these key poses is approximated by the Gaussian probability function. The EDA looks for preferable solutions indicated by the performance criterion, which is the sum of energy cost and ZMP displacement. Thereby, stable and low energy cost gaits can be found by forming probability distribution functions. Moreover, the EDA is applied to kicking pattern generation. Unlike biped walking, kicking power and torque is more critical in efficient kicking. By setting torque cost and kicking velocity as the objective function, the EDA is able to generate and optimize the kicking pattern with minimum torque.

As shown in the experimental results, the EDA converges quickly in both walking and kicking pattern optimization. In less than 100 iterations, it can achieve the dynamically stable and energy-efficient biped gaits. Similarly, stronger kicking can be found in less than 200 iterations. Smooth walking and impelling kicking are exhibited. By replacing probability functions and updating rules in the traditional EDA, EDA can hopefully be further improved for online gait generation and optimization. ${ }^{6}$

The rest of this paper is organized as follows. In the following section, an overview of RESr-1 including hardware design and software architecture is given. Section 3 presents the locomotion planning and optimization using the EDA. The experimental result of walking and kicking is shown in Sec. 4. Some conclusions and future work are presented in Sec. 5 .

# 2. Overview of TeenSize Humanoid Soccer Robot RESr-1 

The Robo-Erectus humanoid project was initiated in the Advanced Robotics and Intelligent Control Centre (ARICC) at Singapore Polytechnic in 2002 (http://www. robo-erectus.org). It has gone through many stages of improvements in the mechanical structure, electronics system and control algorithm design. At RoboCup 2007, held in Atlanta, USA, RESr-1 participated in the Humanoid TeenSize League. The robot demonstrated smooth walking, precise tracking and powerful kicking, and got fourth place in the Penalty Kick competition. Some of the current Robo-Erectus family members are shown in Fig. 2.

### 2.1. Mechanical design

Off-the-shell modular intelligent mechatronic devices - PowerCube - are selected as actuator modules for rapid deployment. PowerCubes are compact rotary units consisting of electrical motors and play-free harmonic drive gears, with the entire electronics (control and drive) integrated. They have a cubic or double-cube design with multiple connecting sockets so that two actuator modules can be connected in many different orientations. To facilitate the forward kinematic analysis, an angular displacement sensor is built into each of the modules.

Besides modular actuators, a set of rigid links with various geometrical shapes and dimensions has been customized to connect different joint modules. The left leg's three joints, which are assembled by six such modules, are shown in Fig. 3. The joint controller, motor drive, battery, sensors and main controller (PC) are designed to be installed in the robot itself.

The system configuration and specification of RESr-1 are shown in Table 1.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Humanoid robots from the Robo-Erectus family (RESr-1 and REJr).

![img-2.jpeg](img-2.jpeg)

Fig. 3. Reconfigurable structure of the left leg of RESr-1.

Table 1. Physical specifications of RESr-1.

1. Physical Specifications

|  | Dimensions |  |  | Speed |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Weight | Height | Width | Depth | Walking | Running |
| 42 kg | 150 cm | 27 cm | 20 cm | $6 \mathrm{~m} / \mathrm{min}$ | - |
| 2. Degrees of Freedom |  |  |  |  |  |
| Joint | Roll | Pitch | Yaw |  |  |
| Head |  |  | $\checkmark$ |  |  |
| Shoulder | $\checkmark$ | $\checkmark$ |  |  |  |
| Elbow |  | $\checkmark$ |  |  |  |
| Hip | $\checkmark$ | $\checkmark$ | $\checkmark$ |  |  |
| Knee |  | $\checkmark$ |  |  |  |
| Ankle | $\checkmark$ | $\checkmark$ |  |  |  |
| 3. Sensors |  |  |  |  |  |
| Sensor |  | Details |  |  |  |
| Camera | $320 \times 240$ resolution 30 fps |  |  |  |  |
| Compass | $1^{\circ}$ heading accuracy |  |  |  |  |
| Tilt | Two dimensions |  |  |  |  |
| Sonar | Distance range $5-250 \mathrm{~cm}$ |  |  |  |  |

4. Specifications

| Features | Main processor | Vision | Sensor/Actuator |
| :--: | :--: | :--: | :--: |
| Processor | Intel Celeron | Intel Core Solo | Dual PIC18F8720 |
| Speed | 800 Mhz | 1.33 GHz | 25 Mhz |
| Memory | 1 GB | 1 GB | 8 KB |
| Storage | 30 GB | 16 GB | 256 KB |
| Interface | CAN-bus, USB, WIFI | USB, WIFI | RS232, RS485 |

![img-3.jpeg](img-3.jpeg)

Fig. 4. Control structure of RESr-1.

# 2.2. Control system 

As demonstrated in Fig. 4, RESr-1 is powered by two Sony VAIO ultraportable computers, namely a Vision PC for image processing of both global and local cameras, and an AI PC for motion planning, navigation and motion control. Because the modular actuators are self-contained mechatronic units, the control loop of the robot is closed at the joint level. Each actuator module has its own individual motion controller. The intermodule communication is achieved through the CAN-bus Protocol. Based on the hierarchical control concept, low-level trajectory generation and control are developed. Once the robot is fully constructed, configured and initialized, the AI PC is able to identify the configuration of the robot, generate the necessary models and coordinate the motion control of the robot. In order to easily develop and debug the perception-action control loop, all sensor data, such as actuator encoder values, gyro outputs, force/torque values and camera images, are directly available to the AI PC. Control commands are sent from the AI PC to the modular actuators directly via CAN-bus.

### 2.3. Vision system

RESr-1 is equipped with two cameras, the top one for global vision and the bottom one for local vision (see Fig. 5). Figures 6 and 7 show the raw image and the resultant image with desired objects segmented after applying the developed algorithm.

## 3. Locomotion Planning and Optimization Using the EDA

This section formulates the generation and optimization problem of humanoid walking and kicking as a multiconstraint optimization problem. With the hierarchical locomotion planning and control architecture, the EDA can represent preferable angular solutions in terms of probability functions for biped walking and kicking.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Vision system of RESr-1.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Images from the global camera.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Images from the local camera.

# 3.1. Hierarchical locomotion planning and control architecture 

A hierarchical motion planning, optimization and control architecture is used to manage system components and provides a framework for high-level autonomous locomotion behaviors. The overall design of the walking planning and optimization architecture is illustrated in Fig. 8, in which the basic architecture for online locomotion control and sensor feedback is also shown.

![img-7.jpeg](img-7.jpeg)

Fig. 8. Overview of the locomotion planning and control architecture for RESr-1.

# 3.2. EDA-based biped gait generation and optimization 

### 3.2.1. Estimation of the distribution algorithm

The control-principle-based method can generate gaits by either exploiting the intrinsic dynamics of biped structure or the parametric optimization technique. The parametric optimization technique provides the possibility of coping with multi-DOF structure that varies in locomotion. State parameters, designed in either task space or joint space, can be approximated by different methods along the motion time. Besides polynomials or spline functions, ${ }^{7}$ heuristic computation methods like neural networks, ${ }^{4}$ fuzzy logic ${ }^{10}$ and genetic algorithms ${ }^{2}$ are the most-used strategies.

Since the behavior of these heuristic computation algorithms depends on many parameters and becomes computational intensive for high-dimensional optimization, this paper focuses on a new kind of population-based searching algorithm the EDA. EDAs were introduced into the field of evolutionary computation by Muhlenbein. ${ }^{12}$ Following his idea, different types of EDAs have been proposed. Among them, Population-Based Incremental Learning (PBIL) performs successfully on numerous benchmark and real world problems when compared to a variety of standard genetic algorithms and hill-climbing algorithms. ${ }^{15}$

It converges quickly with several parameters on the probability function and updating rule. It is employed to approximate the probability distribution of the joint coordinates at transition phases. Such methods provide a new way to reflect the relationship between cost function and input variables in terms of probability distribution. The structure of the general EDA is outlined as follows:
(1) Initiate the multivariate distribution model $M(k), k=1$.
(2) While the termination condition is not met:
(a) Generate a population of $N_{s}$ individuals $O_{s}(k)$ from the probability model $M(k)$.

(b) Select $N_{b}$ best individuals $O_{b}(k)$ from $O_{s}(k)$ according to the objective function value $f\left(O_{s}(k)\right)$.
(c) Modify $M(k+1)$ with $O_{b}(k)$ according to the updating rule and set $k=$ $k+1$.

It can be found from the structure that the probability model and its corresponding updating rule are two main factors for EDAs; we have looked at how to improve the learning quality of EDAs through ameliorating both factors. ${ }^{5,6}$ In this paper, only the traditional EDA with the Gaussian function and partial replacing updating rule is tested on biped walking and kicking gaits. The EDA generates a population according to

$$
\operatorname{Prob}_{i, j}(k)=G\left(\mu_{i, j}(k), \sigma_{i, j}(k)\right)
$$

and updates the probability function by

$$
\begin{aligned}
& \mu_{i, j}(k+1)=(1-\alpha) \mu_{i, j}(k)+\alpha\left(\mu_{i, j, b}(k)+\mu_{i, j, 2 b}(k)-\mu_{i, j, w}(k)\right) \\
& \sigma_{i, j}(k+1)=(1-\alpha) \sigma_{i, j}(k)+\alpha \sqrt{\frac{1}{N_{b}} \sum_{m=1}^{N_{b}}\left(\mu_{i, j, m}(k)-\hat{\mu}_{i, j, m}(k)\right)^{2}}
\end{aligned}
$$

where $\operatorname{Prob}_{i, j}(k)$ is the probability distribution of $q_{i, j}$ at the $k$ th iteration. $\mu_{i, j}(k)$ and $\sigma_{i, j}(k)$ are the means and covariance of Gaussian function $G . \mu_{i, j, b}(k), \mu_{i, j, 2 b}(k)$ and $\mu_{i, j, w}(k)$ are the values of the best, second-best and worst individuals (with respect to the objective function $f_{w}(q)$ ) for variable $q_{i, j}$ at iteration $k . \mu_{i, j, m}$ are the $N_{b}$ best individuals and $\hat{\mu}_{i, j, m}$ is their average value. $\alpha \in[0,1]$ is the learning rate and $m=1,2, \ldots, N_{b}$.

# 3.2.2. Biped gait pattern definition 

The main phases of one gait cycle are supposed to be the swing phase and the double support phase, as shown in Fig. 9. The swing phase of the $n$th gait cycle starts from the swing foot toeing off the ground and ends when the heel touches the ground. The swing foot reaches the highest point at $n T+T_{a}$, and after $T_{b}$ it touches the ground. $T=T_{a}+T_{b}+T_{c}$ is the time period for one gait cycle, with $T_{c}$ representing the time for the double support phase. $n=0,1, \ldots$ records the number of steps. The double support phase begins at the moment that the front heel touches the ground and ends when the rear toe sways off at $(n+1) T$. The end configuration of this phase initiates the swing phase of the next gait cycle. Landing impact occurs at the beginning of the double support phase. The transition between the two phases is assumed to take place in an infinitesimal length of time.

### 3.2.3. Problem formulation

It can be found from Fig. 9 that in total four key poses are chosen in one complete gait cycle. Phases between these key poses are approximated by third order spline

![img-8.jpeg](img-8.jpeg)

Fig. 9. Biped gait pattern and key poses in the left leg support phase. The three key poses are defined as: key pose 1 - the moment the swing (right) toe touches the ground; key pose 2 - when the swing foot reaches the highest point; key pose 3 - when the swing heel touches the ground. Similar key poses can be selected during the right leg support phase. For symmetric gaits, the key poses in the right support phase are the corresponding ones in the left support phase.
functions in joint space. Such a strategy guarantees that the second order derivatives at every point, especially at connection points, are continuous and the actuating torques is continuous at knots. The robot trajectories are parametrized as cubic splines $S(q, t)$ as a function of the parameters $q \in R^{N_{q}}$.

Therefore, the problem can be reduced to a general problem of nonlinear parametric optimization with equality and inequality constraints as

$$
\begin{array}{ll}
\text { Minimize } & f_{w}(q)=\beta_{1} f_{1}(q)+\beta_{2} f_{2}(q) \\
\text { Subject to } & g_{i}(q) \leq 0 \\
& q \in \Omega
\end{array}
$$

where $f_{w}(q)$ represents the optimization goal of achieving the dynamically stable and low energy cost biped gaits. $f_{1}(q)=\int_{t=k T}^{(k+1) T} \| p_{\mathrm{ZMP}}(t)-p_{\mathrm{DZMP}}(t) \| d t$ is the integral of ZMP displacement during the $k$ th gait cycle. $p_{\mathrm{ZMP}}(t)$ and $p_{\mathrm{DZMP}}(t)$ are real and desired ZMP trajectories respectively, and $\|\cdot\|$ is the second order norm. For the concept definition and position calculation of ZMP using the complete robot link model, the reader can refer to Ref. 16. $f_{2}(q)=\int_{t=n T}^{(n+1) T} \tau(t) d t$ estimates the dynamical load during one gait cycle $[n T,(n+1) T]$.

By sampling $N_{s}$ poses in the $k$ th gait cycle, we can get the discrete $f_{1}(q)$ and $f_{2}(q)$, as Eqs. (2) and (3) shown.

$$
\begin{aligned}
& f_{1}(q)=R\left(\sum_{i=1}^{N_{s}} f_{1}^{i}(\cdot)\right) \\
& f_{2}(q)=R\left(\sum_{i=1}^{N_{s}} f_{2}^{i}(\cdot)\right)
\end{aligned}
$$

where $f_{1}^{i}=\left\|p_{\mathrm{ZMP}, \mathrm{i}}-p_{\mathrm{DZMP}, i}\right\|$ calculates the Euclidean distance between the actual ZMP trajectory $p_{\mathrm{ZMP}}$ and the desired ZMP trajectory $p_{\mathrm{DZMP}}$ at the $i$ th sample index. $f_{2}^{i}=\sum_{j=1}^{N_{q}} \tau_{i j}$ summarizes the torque of all actuated joints at the $i$ th sample index. Torque at these key moments is calculated by a simple link model. ${ }^{6} R$ is the normalization operator for making the two targets comparable.
$\beta_{1}$ and $\beta_{2}$ are weights satisfying $\beta_{1}+\beta_{2}=1$ to note the desired character of generated gaits. The combination of $\beta_{1}$ and $\beta_{2}$ can be adjusted according to practical requirements. Larger $\beta_{1}$ would lead searching to gaits with a smaller ZMP displacement, because the improvement in stability has a more significant impact on the objective function. A heuristic algorithm like fuzzy logic can be embedded to tune the two parameters properly, which will not be emphasized in this paper.
$\Omega$ denotes the domain defined by $g_{i}(q)$, which is a set of inequality constraints arising from the geometric and state requirement to guarantee the feasibility of the generated gaits. The definition of constraints is presented in Ref. 6.

The EDA is then used to search the preferable combination of joint angles which has a small objective function value.

# 3.3. Kicking pattern generation and optimization 

### 3.3.1. Definition of kicking phases

The quality of kicking is mostly determined by the velocity at the kicking moment. Since momentum $I$ is the product of mass $m$ and velocity $v$, the larger the velocity, the bigger the momentum. Based on conservation of momentum and collisions, a bigger momentum leads to further rolling of the ball for $t=I / f$, and sequentially better kicking, where $f$ is the friction.

In observing instep driving of human kicking, the steps to follow include:
(1) Approach the ball from directly behind or from a slight angle; square hips and shoulders to the line of the kick.
(2) With the balance foot behind the ball and the balance knee slightly flexed, kick hard at the center of the ball with the instep.
(3) Follow through in the direction of the target.

Accordingly, kicking is divided into three phases: speed-up, kicking and speeddown (see Fig. 10). The kicking leg accelerates to the maximum velocity, $q_{\max }$ in

![img-9.jpeg](img-9.jpeg)

Fig. 10. Plan kicking in angle space.
the first phase, dribbles up the ball and kicks it away during the kicking phase, and finally it decelerates to zero velocity at the end of the speed-down phase.

According to the $x$ coordinate of the swing foot, $x_{f}=l_{t} \times \sin \left(q_{h}\right)+l_{c} \times \sin \left(q_{k}\right)$ ( $l_{t}$ and $l_{c}$ are the length of the thigh and crus; $q_{h}$ and $q_{k}$ are the hip and knee joint angles), we define the range of $\left[x\left(t_{1}\right), x\left(t_{2}\right)\right]$ as the "most efficient kicking range" because of the large velocity during this period, and define $[x(0), x(T)]$ as the "possible kicking range."

# 3.3.2. Problem formulation 

Since kicking is finished by fixing the supporting leg on the floor, vibration is brought mainly by the kicking leg, and stability is not the crucial problem in kicking. On the other hand, the farther the ball goes, the more powerful the kicking is. However, it is not easy to measure the rolling distance of the ball.

To find the kicking with a large velocity and a small torque, let the objective function of kicking be

$$
f_{k}(q)=\frac{f_{3}(q)}{f_{4}(q)}
$$

where

$$
f_{3}(q)=R\left(\sum_{i=1}^{N_{s}} f_{2}^{i}(\cdot)\right) \quad \text { and } \quad f_{4}(q)=R\left(\sum_{i=1}^{N_{s}} \sum_{j=1}^{N_{q}} \dot{q}_{i j}\right)
$$

As in walking, joint angles can be optimized by the traditional EDA, and the following section shows the experimental results of walking and kicking using the EDA.

# 3.3.3. Analysis of the EDA for biped gait optimization 

Due to the probability model being updated by selected samples, the EDA can formulate solutions better than random searching methods. ${ }^{12}$ Different probability models and updating rules for different application cases are studied in Ref. 6.

By setting the stride length and period, the EDA can find the desired gait defined by the objective function off-line first. The quality of the optimized gait is ensured by objective functions.

## 4. Experimental Results

### 4.1. Walking

Let $N_{s}=16, N_{b}=4, T_{a}=4, T_{b}=4, T=10, \alpha=0.05$ and $\beta_{1}=\beta_{2}=0.5$. The EDA stops optimization when $f_{w}(q)<0.1$ or $k>100$.

The objective function value $f_{w}(k)$ in biped gait optimization is exhibited in Fig. 11. It keeps falling down from more than 0.34 to about 0.26 in 200 optimization iterations. The subobjective function value of $f_{1}(q)$, as given in Fig. 12, comes down as well during optimization. However, no obvious reduction is observed in the optimization of $f_{2}(q)$. That is to say, optimization comes mainly from dynamical stability.

Correspondingly, joint angles in the sagittal plane optimized by the EDA are shown in Fig. 13. For indexes of joint angles, see Ref. 6.

By getting feedback from the modular actuators via CAN-bus (20 sampling points per walking cycle), the tracking errors of the hip, knee and ankle joints are given in Fig. 14. It can be seen that the modular actuator module is able to
![img-10.jpeg](img-10.jpeg)

Fig. 11. Objective function value $f_{w}(q)$ in 100 optimization iterations for walking.

![img-11.jpeg](img-11.jpeg)

Fig. 12. $f_{1}(q)$ (left) and $f_{2}(q)$ (right) in 100 optimization iterations for walking.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Trajectory of each joint in the sagittal plane for walking.
precisely track the given trajectory for each joint. However, landing impact needs to be tackled to further reduce the tracking errors. We are currently developing a virtual spring-damper system for hip and ankle joints so that the vertical shock at the landing moment can be absorbed through rapid modification of the hip joint height.

Figure 15 shows snapshots of RESr-1 tracking and following a ball target at RoboCup 2007, held in Atlanta.

# 4.2. Kicking 

The EDA is also applied to kicking locomotion optimization. Similarly, let $N_{s}=$ $16, N_{b}=4, T_{1}=4, T_{2}=6, T=10$ and $\alpha=0.1$. The EDA stops optimization when $f_{k}(q)<0.05$ or $k>200$.

![img-13.jpeg](img-13.jpeg)

Fig. 14. Error in servomotor control.
![img-14.jpeg](img-14.jpeg)

Fig. 15. Snapshots of RESr-1 tracking and following a ball target at RoboCup 2007.

The objective function value $f_{k}(q)$ vibrates during the first 20 optimization epochs, as shown in Fig. 16. It decreases from about 0.36 to 0.22 and finally converges to around 0.21 . It is mainly because of the increase existing in velocity searching (see the right one in Fig. 17). From the vibration of torque and velocity functions, it can be seen that velocity plays an important role in kicking optimization. Increase in velocity causes increase in torque during the initial optimization process and finally converges to a good balance between these two criteria.

A full kicking process is shown in Fig. 19. In the experiment, if the target is outside the viewing area, the robot will either make use of the most recently detected position or enter the searching mode (using both global and local cameras) to locate the target. To implement a more efficient goal tracking behavior control, we

![img-15.jpeg](img-15.jpeg)

Fig. 16. Objective function value $f_{k}(q)$ in 100 optimization iterations.
![img-16.jpeg](img-16.jpeg)

Fig. 17. $f_{3}(q)$ (left) and $f_{3}(q)$ (right) in 500 optimization iterations for kicking.
are currently developing a stereovision processing system for target detection and three-dimensional position estimation in camera coordinates.

In both experiments, the EDA converges quickly and keeps constant during the later optimization process. For the general off-line optimization problem, the traditional EDA is enough in terms of speed and precision but not fitting for online application. By studying the probability function and the updating rule, it is found that convergence precision and speed can be improved with a different combination of these two factors. This will be studied in future work.

![img-17.jpeg](img-17.jpeg)

Fig. 18. Trajectory of swing joints in the sagittal plane for kicking.
![img-18.jpeg](img-18.jpeg)

Fig. 19. Snapshots of RESr-1 kicking a ball at RoboCup 2007.

# 5. Conclusion 

The RESr project aims to develop a platform for interactive cooperation between humans and robots in the general environment and specially for TeenSize humanoid soccer games. It is constructed from a set of independently designed standard modules. Thereby, modular actuators, rigid connectors and passive joints can be assembled into different types of humanoid legged locomotion platforms with different kinematic and dynamic characteristics.

As part of the research on the full-size humanoid robot, a locomotion planning and control system for navigation and location is described in this paper. Gaits

are decomposed into key poses, which are connected by a third-order interpolation function. Joint angles at these key poses are generated by the EDA optimization method. As shown in the experimental results, by setting ZMP displacement and energy cost as the objective function in the EDA, dynamically stable and energyefficient gaits can be found with few variables. Besides that, a powerful kicking pattern can be achieved using the EDA with energy cost and kicking velocity as the objective function.

With the help of the hierarchical control architecture, vision-based behavior system, RESr-1 demonstrated smooth walking, precise tracking and powerful kicking, and finally got fourth place in the Humanoid TeenSize Penalty Kick competition of RoboCup 2007.

As indicated in Sec. 4 about the experimental result, the tracking error brought by land impact greatly affects the locomotion quality. To overcome the unstable factor, a virtual spring damper system is under investigation and development now. Moreover, a stereovision processing system is being developed to cope with the 3D position location problem.

# Acknowledgments 

This research is supported by the Singapore TB Model Project (11-27801-36-M096 and 11-30012-36-M096). We would like to thank staff and students at the Advanced Robotics and Intelligent Control Center (ARICC) of Singapore Polytechnic for their support in the development of RESr-1. In particular, we are grateful to Bi Wu, Hendra, Pik Kong Yue, Carlos Antonio Acosta Calderon, Rajesh Elara Mohan, Nguyen The Loan, Chin Keong Ang, Weiming Yuan, Edric Lee Lai Fatt, Guohua Yu, Weijie Ye, Aung Aung Kyaw and Karta Sutanto for their contributions to this project.

## References

1. F. Asano, M. Yamakita, N. Kamamichi and Z.-W. Luo, A novel gait generation for biped walking robots based on mechanical energy constraint, IEEE Trans. Robot. Automat. 20(3) (2004) 565-573.
2. G. Capi, S. Kaneko, K. Mitobe, L. Barolli and Y. Nasu, Optimal trajectory generation for a prismatic joint biped robot using genetic algorithms, Robot. Autonom. Syst. 38(2) (2002) $119-128$.
3. K. Hirai, Current and future perspective of Honda humanoid robot, in Proc. IEEE Int. Conf. Intelligent Robots and Systems (1997), pp. 500-508.
4. J. Hu, J. Pratt and G. Pratt, Stable adaptive control of a bipedal walking robot with CMAC neural networks, in Proc. IEEE Int. Conf. Robotics and Automation (1999), pp. 1950-1956.
5. L. Hu, C. Zhou and Z. Sun, Estimating probability distribution with Q-learning for biped gait generation and optimization, in Proc. IEEE Int. Conf. Intelligent Robots and Systems (2006), pp. 362-368.
6. L. Hu, C. Zhou and Z. Sun, Estimating biped gait using spline-based probability distribution function with Q-learning, IEEE Trans. Ind. Elec. 55(3) (2008) 14441452 .

7. Q. Huang, K. Yokoi, S. Kajita, K. Kaneko, H. Arai, N. Koyachi and K. Tanie, Planning walking patterns for a biped robot, IEEE Trans. Robot. Automat. 17(3) (2001) 280290.
8. J. Y. Kim, I. W. Park and J. H. Oh, Walknig control algorithm of biped humanoid robot on uneven and inclined floor, J. Intell. Robot. Syst. 48(4) (2007) 457-484.
9. P. Larranaga and J. A. Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation (Kluwer, 2001).
10. Z. Liu and C. Li, Fuzzy neural network quadratic stabilization output feedback control for biped robots via $h_{\infty}$ approach, IEEE Trans. Fuzzy Syst. 33(1) (2003) 67-84.
11. M. Morisawa, S. Kajita, K. Kaneko, K. Harada, F. Kanehiro, K. Fujiwara and H. Hirukawa, Pattern generation of biped walking constrained on parametric surface, in Proc. IEEE Int. Conf. Robotics and Automation (2005), pp. 2405-2410.
12. H. Muhlenbein and R. Hons, The estimation of distributions and the minimum relative entropy principle, Evolution. Comput. 13(1) (2005) 1-27.
13. K. Nishiwaki, J. Kuffner, S. Kagami, M. Inaba and H. Inoue, The experimental humanoid robot h7: A research platform for autonomous behaviour, Philos. Trans. Roy. Soc. 365 (2007) 79-107.
14. M. Vukobratovic and B. Borovac, Zero moment point - Thirty five years of its life, Int. J. Human. Robot. 1(1) (2004) 157-173.
15. S. Yang and X. Yao, Experimental study on population-based incremental learning algorithms for dynamic optimization problem, Soft Comput. 9(11) (2005) 815-834.
![img-19.jpeg](img-19.jpeg)

Lingyun Hu received her M.S. and Ph.D. degrees in Computer Science from Tsinghua University, China, in 2003 and 2007, respectively. From 2005 to 2006, she was a Research Associate in the School of Electrical and Electronic Engineering at Singapore Polytechnic. She has been a Research Scientist at the Advanced Robotics and Intelligent Control Center (ARICC), a Technology and Innovation Center (TIC) at Singapore Polytechnic, since 2007.
Dr. Hu is a member of organizing committee of the Humanoid League at RoboCup 2008. She has over 20 research publications. Her research interests include humanoid robotics, intelligent control and learning, evolutionary computation and soft computing.
![img-20.jpeg](img-20.jpeg)

Changjiu Zhou received his B.Eng. and M.Eng. degrees in Electrical Engineering from Jilin University (formerly Jilin University of Technology), China, in 1985 and 1988, respectively, and his Ph.D. degree in Control Engineering from Dalian Maritime University, China, in 1997.

He is currently Centre Director of the Advanced Robotics and Intelligence Control Centre (ARICC), a Technology and Innovation Centre (TIC) at Singapore Polytechnic. Before joining Singapore Polytechnic in 1996, he was an Associate Professor in the Department of

Computer Science at Dalian Jiaotong University, China. He has been a guest professor at Dalian Maritime University since 2001. He is also an adjunct professor at Jilin University. He was a visiting scholar as the Computational Learning and Motor Control Laboratory, University of Southern California, from November 2003 to March 2004, and the Polytechnic University of Madrid in June and December 2001 and September 2002.

Dr. Zhou has been a member of the RoboCup Executive Committee since 2003; he was Chair of the Humanoid League in 2003, 2004 and 2008. He is the founding chairman of the RoboCup Singapore National Committee, and a member of the International Robotic Olympia Committee (IROC). He is an associate editor of International Journal of Humanoid Robotics and IES Journal B: Intelligent Devices and Systems. He also served as guest editor for several international journal special issues, e.g. "Fuzzy Sets and Systems". His current research interests include humanoid robotics, edutainment and service robots, computational intelligence, machine learning, and bioinspired robotic systems. He has published over 150 journal and conference papers, and 3 edited books by Springer.