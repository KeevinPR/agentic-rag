# USV Course Controller Optimization Based on Elitism Estimation of Distribution Algorithm* 

Qingyang Xu


#### Abstract

PID controller is used in most of the course-keeping closed-loop control of Unmanned Surface Vehicle (USV). However, the parameters of PID are difficult to tuning. In this paper, we adopt an elitism estimation of distribution algorithm (EEDA) to optimize the PID, which makes use of the probabilistic model to estimate the optimal solution distribution. It has a better global searching ability. A linear Nomoto model is adopted to simulate the USV, and the PID controller is used to control the course of the USV. The simulation results exhibit the validity of the EEDA.

Key words - Estimation of distribution algorithm. USV. PID. Global optimization. Nomoto.


## I. INTRODUCTION

In the last two decades of research and development, a large number of Unmanned Surface Vehicle (USV) have been developed to achieve a military, commercial or civilian mission [1]. USV are now heavily relied upon for surveillance, intelligence, search and rescue [2]. USV is always used for a riverine environment, where the waterways may be narrow and nonuniform [3]. But, the USV must can navigate autonomously in the dynamic and uncertain environment. Ideally, the USV need to operate without any human intervention. In many instances, USV are remotely operated to perform a specific mission [4]. This means that the vessel's on-board control system must be self-reliant and able to provide a rapid assessment, the perception and maneuvering algorithms must execute quickly and reliably. Therefore, the performance of controller is an important for the control of USV.

The ship response on the sea is typically considered as six degrees of freedom rigid body motion. However, three degrees of freedom planar motion is enough for ship maneuvering study [1]. Whereas, USV is a high speed vessel, the roll motion can not be negligible. Four degrees of freedom motion includes surge, sway, yaw and roll motions are considered [2, 3]. The Nomoto model is always used in ship steering autopilot design due to its simplicity. For simplifications, the second order and the first order Nomoto model are considered in this paper.

The PID controller is still the popular one in course-keeping. The proportional, integral and derivative actions are provided in the controller, which has the characteristics of simple structure, good stability, and high reliability [5].

Although the number of parameters to adjust in a PID is very small, there are many tuning rules [1]. It has been

[^0]experimentally checked that more than $30 \%$ of controllers are operating in manual mode and $65 \%$ of the loops operating in automatic mode are poorly tuned because of the inappropriate parameters [6].

Tuning of the PID controller is not a straightforward problem especially when the plants to be controlled are nonlinear and unstable. It can be considered as a parameter optimization process to achieve a good system response, such as a minimum rise time, overshoot, regulating time, etc. Thus, the tuning process of the controller has multiple objectives to be achieved, and it is conflicting with each other in most cases. Over the years, many methods have been proposed for the tuning of the PID controller, both in the deterministic or stochastic frameworks[7].

In this paper, we adopt an elitism estimation of distribution algorithm to optimize the parameters of PID. The Nomoto model is used to simulate the USV.

## II. MATHEMATICAL MDEL OF USV

Most modern manoeuvring mathematical models used in various simulators are built according to the MMG separation model, which include submodels for the hull, propeller, rudder, engine and steering gear. Every sub-model usually describes the components of forces and moments. It is flexible to reflect the intrinsic characteristics of different models but at the same time reduces their computational speed.

Different from MMG separation model, Nomoto model is an integral model of ship. The first-order Nomoto model is especially suitable for collision-avoidance system design, and can also be used to adaptive auto-pilots design.

For small rudder angles, the transfer function between the rudder angle $\delta$ and the yawing rate r of a surface ship can be described by the linear models of Nomoto. Nomoto's 2nd order model is written as:

$$
\frac{r(s)}{\delta(s)}=\frac{K\left(1+T_{1} s\right)}{\left(1+T_{1} s\right)\left(1+T_{2} s\right)}
$$

where K is a gain constant and Ti are the time constants.
For simplification, the time constant are grouped as $\mathrm{T}=\mathrm{T} 1+\mathrm{T} 2-\mathrm{T} 3$. Hence,

$$
\frac{r(s)}{\delta(s)}=\frac{K}{1+T s}
$$

The yaw angle $\varphi(t)$ is related to the yaw rate $r(t)$ as

$$
r(t)=\varphi^{\prime}(t)
$$


[^0]:    *Qingyang Xu is with the School of Mechanical, Electrical \& Information Engineering, Shandong University (Weihai), Weihai, 264209 China ( 86-0631-5688066-315; fax: 86-0631-5688338; e-mail: xuqy1981@ 163. com).

## III. Estimation of Distribution Algorithm

Estimation of Distribution Algorithm (EDA) was proposed by Miuhlenbein and Paaß [8], and emerged as a generalization of EAs, for overcoming the shortcoming of traditional EAs, such as building blocks broken and ingnoring the distribution of solutions modeling. It is the main advantages of EDA that the explanatory and transparency of the probabilistic model guides the search process $[9,10]$. The algorithm is mainly based on the following two steps: (1) Statistics the excellent individuals' information and establish the probability model. (2) Generate new population according to the probability model. An elitism strategy is adopted to improve the performance of standard EDA,. Figure 1 is the flowchart of EEDA.
![img-0.jpeg](img-0.jpeg)

Figure 1. Flowchart of EEDA

The steps of the FEGEDA is as follows:
Step 1. Initialization: Set the parameters, like population size N , excellent individuals No. BN for probability model establishment.

Step 2. Population Evaluation: Evaluate the N individuals $\mathrm{x} 1, \mathrm{x} 2, \ldots \mathrm{xN}$ according to fitness function $\mathrm{f}(\mathrm{x})$.

Step 3. Statistical information obtaining: According to the fitness value select BN individuals, and calculate the mean $\mu$ and standard deviation $\sigma$ of the individuals.

$$
\begin{gathered}
\bar{\mu}_{i}(k)=\frac{1}{N} \sum_{n=1}^{B N} x_{i}^{n}(k) \\
\sigma_{i}^{2}(k)=\frac{1}{N} \sum_{n=1}^{B N}\left(x_{i}^{n}(k)-\bar{\mu}_{i}(k)\right)\left(x_{i}^{n}(k)-\bar{\mu}_{i}(k)\right)^{T}
\end{gathered}
$$

$\bar{\mu}_{i}(k)$ is the $i$-th variable mean value of $k$-th iteration, BN is the excellent individuals No. $\sigma_{i}^{2}(k)$ is the $i$-th variable covariance of $k$-th iteration.

Step 4. Probability model $\mathrm{P}(\mathrm{x} 1, \mathrm{x} 2, \ldots, \mathrm{xm})$ establishment: Using the fast learning rule, and build the Gaussian normal distribution by the u of means and a covariance $\sigma$.

$$
P\left(x_{1}, x_{2}, \cdots x_{m}\right)=\prod_{i=1}^{m} \frac{1}{\sigma_{i} \sqrt{2 \pi}} e^{-\frac{\left(x_{i}-\bar{\mu}_{i}\right)^{2}}{2 \sigma_{i}^{2}}}
$$

Step 5. Generate new population Pop(k): Sampling the probability model to generate a new population.

Step 6. Finally, the termination criteria method determines the stopping conditions for EDA evolution. These criteria can be a fixed number of generations or a statistical analysis of the population. If the stopping criteria isn't adequate, return step2.

## IV. PID Controller

The continuous PID with input $e$ and output $u$ can be described as follows:

$$
u(t)=K_{p} e(t)+K_{i} \int e(t)+K_{d} \dot{e}(t)
$$

where $\mathrm{Kp}, \mathrm{Ki}$ and Kd are the proportional, the integral and the derivative gains.

Two types of discrete PID are used in industry. The position-type PID is as following

$$
u(k)=K_{p} e(k)+K_{i} \sum_{j=0}^{k} e(k)+K_{d}(e(k)-e(k-1))
$$

where $u(\mathrm{k})$ is the output of controller, $\mathrm{e}(\mathrm{k})$ is the system error. In practical system, the integral part is not flexible for position-type PID. Therefore, the velocity-type PID is always used as following
$\Delta u(k)=K_{p} \Delta e(k)+K_{i} e(k)+K_{d}(\Delta e(k)-\Delta e(k-1))$
and $\Delta e(k)=e(k)-e(k-1)$
where Ts is the sample time. For velocity-type PID, the integral part doesn't need calculate, and the controller output is the increment of PID. Therefore, it is easy for realization.

Tuning of the PID controller is not a straightforward problem to achieve a good system response, such as a minimum rise time, overshoot, regulating time, etc.

![img-3.jpeg](img-3.jpeg)

Figure 2. The diagram of PID controller optimization system

Aggregation function is a conventional method to convert a multi-objective problem to a single-objective problem.

$$
\text { fitness }=\sum_{i=1}^{n} w_{i} f_{i}
$$

where fitness is the summation of fitness, $w_{i}$ is the weight of $i$-th objective, and $f_{i}$ is the fitness value of $i$-th objective.

In order to evaluate the performance of PID, the fitness function is written as

$$
\begin{aligned}
f_{1} & =\int_{1}^{c}|e(t)| d t \\
f_{2} & =\int_{1}^{c} u^{2}(t) d t \\
f_{3} & =t_{r}
\end{aligned}
$$

where $e(t)$ is the system error, $u(t)$ is the controller output, and $t_{r}$ is the rising time of system response.

In order to avoid overshoot, a penalty part is used to guide the search process. Once overshoot occurs, the penalty value is added to the fitness function. Therefore, the fitness function can be described as

$$
f_{4}= \begin{cases}\int_{1}^{c}(y(t)-y(t-1)) d t & \text { if } e(t)<0 \\ 0 & \text { if } e(t) \geq 0\end{cases}
$$

where $y(t)$ is the USV response.
Therefore, the fitness function is constructed as follow.

$$
f=w_{1} f_{1}+w_{2} f_{2}+w_{3} f_{3}+w_{4} f_{4}
$$

where w1, w2, w3 and w4 are the weight coefficients, and w4»w1.

## V. SIMULATION

We take a water-jet-propelled USV for example. The parameters of a specific water-jet-propelled USV are estimated by spiral test according to literature of Wu\#. The parameters of linear Nomoto's 1st order model are that $K$ is $-2.364, T$ is 3.384 . The algorithm is used to optimize the
parameters of PID, and compares against the standard GA. In this paper, we pay attention to the overshoot and rising time. Therefore, $w 1$ is $1, w 2$ is $0.1, w 3$ is 2 and $w 4$ is 200 . The variable domain of $K_{p}$ is $[0,10], K_{i}$ and $K_{d}$ are $[0,5]$. By the optimization of EEDA, we get the PID parameters ( $K_{p}, K_{i}$, $\left.K_{d}\right)=0.110 .0000001,1.95$ ). The response curves of USV is shown in fig. 3 and error is shown if fig. 4. From fig. 3 and fig. 4 we can see, the optimal result of EEDA is better than the SGA output.
![img-3.jpeg](img-3.jpeg)

Figure 3. The response of system
Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 5. The error of system

## VI. CONCLUSION

PID is a popular controller in industry. Although, there are only few parameters, the parameters are difficult to determine due to the uncertain model of industry. EEDA provides a means to find an optimal solution of determining the parameters. In this paper, we use a EEDA to optimize the $K_{p}, K_{i}$ and $K_{d}$ of USV course controller. We can have optimal parameters by EEDA according to our optimal guideline.
