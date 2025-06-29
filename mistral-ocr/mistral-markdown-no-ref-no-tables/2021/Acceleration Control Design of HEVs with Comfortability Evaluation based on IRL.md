# Acceleration Control Design of HEVs with Comfortability Evaluation based on IRL 

Shohei Narita* Jiangyan Zhang ${ }^{* *}$ Weidong Zhang ${ }^{* * *}$<br>Tielong Shen ${ }^{*}$<br>* Department of Engineering and Applied Sciences, Sophia University, Tokyo 102-8554 Japan (e-mail:s-narita-7wq@eagle.sophia.ac.jp).<br>** College of Mechanical and Electronic Engineering, Dalian Minzu<br>University, Dalian 116600, China (e-mail:<br>zhang-jiangyan@dlnu.edu.cn)<br>${ }^{* * *}$ Department of Automation, Shanghai Jiao Tong University, Shanghai 200240, China


#### Abstract

For passenger cars, comfortability is an important issue to consider in powertrain control. However, it is not easy to take comfortability into account when designing a powertrain control strategy because of its subjective nature and difficulty in being quantified. This paper presents a solution by using the inverse reinforcement learning (IRL) method. An acceleration scenario of a hybrid electric powertrain is considered to show this design approach. With a sample acceleration profile scored by an expert evaluating module, a reward function is obtained by training an extreme learning machine. Using the analytical representation of comfortability, an estimation of distribution algorithm (EDA) is used to seek the optimal acceleration reference. Given the reference acceleration signal, the control law for the electric motors that provide power assistance during the acceleration phase is obtained by solving a optimal tracking control problem. A numerical example is shown to evaluate the design approach.


Copyright (C) 2021 The Authors. This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0/)
Keywords: Hybrid electric vehicle, ride comfort, acceleration, inverse reinforcement learning, optimal control

## 1. INTRODUCTION

Comfortability, which is an important index for evaluating the performance of passenger cars, can be influenced strongly by dynamic control of the powertrain system. For hybrid electric vehicles (HEVs), controlling the powertrain to achieve desired comfortability is a challenging issue since different power sources such as the internal combustion engine and electric motors operate cooperatively to generate power. Especially during the acceleration and braking modes that are required in common maneuvers such as merging, passing, and deceleration, the electric motor and internal combustion engine generally require onoff control to switch between power production and energy regeneration. The energy management problem accounts for most of the literature in the field of HEV powertrain optimization, for instance, Lee (2020) and Hu (2019), which provide insight on effective energy management strategies for the cooperative operation of the internal combustion engine and electric motors.
Much of the existing literature focuses on finding the optimal control strategy for some given route. However, a strategy that is applicable in the real world must function without a priori knowledge of a vehicle's path. To this end, Jiang (2017) and Zhang (2021) propose a real-time adaptive optimal control scheme to minimize the energy

[^0]consumption of an automated HEV. While many papers discuss long-term optimization for HEV powertrains, only a few address the issue of short-term optimal control that is required in specific driving scenarios. For instance, a merging scenario is addressed by Xu (2021), in which the torque distribution problem is formulated as an optimal control problem with the cost function containing velocity and energy consumption terms, and consideration given to the dynamics of the vehicle. An acceleration scenario is addressed by Zhang (2020), in which the torques of the motor and combustion engine are controlled to minimize energy consumption while also tracking the vehicle's speed in real time. However, neither paper considers comfortability. Considering comfortability raises challenges, in that it is subject to an individual's senses, and it cannot easily be quantified. To this end, recent papers such as Shen (2020) and Zhu (2020) aim to increase comfortability by placing a limit on a vehicle's jerk signal. Although a correlation is seen between comfortability and jerk, giving an exact description of said relation poses additional challenges.
This paper addresses the powertrain control problem of HEVs while also considering comfortability. A major obstacle in optimizing comfortability via dynamic control lies in the need to explicitly define a cost function. In this paper, this challenge is overcome by employing an inverse reinforcement learning (IRL) technique. Suppose that a human's perception of comfortability is quantized by some score. Using this score as training data, the


[^0]:    * This work is supported in part by National Natural Science Foundation (NNSF) of China under Grant 61973053.

relation between a vehicle's response and the cost function is approximated by an extreme learning machine (ELM). Using the result of IRL together with an estimation of distribution algorithm (EDA), the optimal acceleration profile is obtained. In turn, the optimal power assistance law for the electric motor is designed by solving an optimal control problem, assuming that the engine is operated at full throttle. Finally, the proposed design scheme is validated by numerical simulation.

## 2. BACKGROUND AND CONTROL ISSUE

Consider the powertrain shown in Fig. 1, composed of two electric motors MG1 and MG2, a battery package, an internal combustion engine with a turbocharger, a clutch, an automatic transmission (AT) system with a 10-speed gearbox, differential gears, and a distortion component. Suppose the vehicle is initially cruising in EV mode at a
![img-0.jpeg](img-0.jpeg)

Fig. 1. Configuration of HEV with two motors
constant speed $v_{0}$, with the driving torque provided solely by motor MG2. Thereafter, the vehicle enters acceleration mode targeting a final speed $v_{f}$. Due to the electric power constraint, the combustion engine is switched on with full throttle operation. While the vehicle is accelerating, the gear must be managed promptly. Achieving high comfortability by controlling the powertrain in this acceleration scenario raises the following issues:

1) Determining when to engage and release the clutch.
2) Managing the power generated by the electric motor to in turn control the total driving torque.
3) Evaluating comfortability using a cost function, according to the dynamical behavior of the powertrain during the acceleration mode.

Of these issues, the third can be solved provided the answers to the first two. That is, given the optimal controls resulting from 1) and 2), the speed and acceleration profiles may be obtained in accordance with the dynamics of the powertrain. However, solving issues 1) and 2) comes with multiple difficulties resulting from there being switching actions in the system, the power transformation having varying efficiency, and the power generation by the combustion engine with a turbocharger having strong nonlinearity. Above all, designing a control law via model-based optimization is difficult in the absence of an analytic formulation of comfortability. The only available knowledge regarding comfortability is the scores given by humans. Expert models are used in industry to evaluate comfortability.

Fig. 2 shows three acceleration responses under different power settings, where $v_{i}$ and $a_{i}(i=1,2,3)$ represent the
![img-1.jpeg](img-1.jpeg)

Fig. 2. Three examples of comfortability score
Table 1. Test conditions and comfortability scores from expert model
speed and corresponding acceleration signals, respectively. The power settings of the motors as well as the corresponding comfortability scores are shown in Table 1.
We begin with an analytic representation of the comfortability score to find the optimal acceleration profile. First, the inverse reinforcement learning technique is used to construct this analytic function. Then, using this function as a measure for optimality, the optimal acceleration signal is found via EDA. Finally, the optimal control law is sought by solving the optimal control problem regarding acceleration tracking.

## 3. DESIGN SCHEME

### 3.1 Inverse Reinforcement Learning

Since the comfortability score is based on human feeling which, in turn, is a dynamical response of the acceleration signal, we use an extreme learning machine (ELM) to approximate this score. To this end, the Distance Minimized Inverse Reinforcement Learning (DMIRL) approach proposed by Burchfiel (2016) is used with a set of training data.
Let $a_{k}^{i}\left(k=0,1, \cdots, M^{i} \leq M\right)$ denote a discreterized signal of acceleration, where $i=1,2, \cdots, S$ is the index of the acceleration data. The corresponding score of $a_{k}^{i}$ is represented by $J^{i}$. Suppose the unknown reward function $R$ on time step $k$ is given by

$$
R\left(x_{k}\right)=w^{\top} \phi\left(x_{k}\right)
$$

where $x_{k}=\left[\begin{array}{ll}a_{k} & k\end{array}\right]^{\top}$ is the state of the system, $\phi\left(x_{k}\right)=$ $\left[\phi_{1}\left(x_{k}\right) \phi_{2}\left(x_{k}\right) \cdots \phi_{N}\left(x_{k}\right)\right]^{\top}$ maps the state $x_{k}$ onto a $N$ dimensional feature vector, and $w \in \mathbb{R}^{N}$ is the vector of weighting coefficients, i.e.,

$$
w=\left[\begin{array}{llll}
w_{1} & w_{2} & \cdots & w_{N}
\end{array}\right]^{\top}
$$

Following the standard notation of extremal learning machines (ELMs), the neuron function $\phi_{j}\left(x_{k}\right)$ is defined as follows:

$$
\phi_{j}\left(x_{k}\right)=\tanh \left(p_{j} a_{k}+h_{j} k+q_{j}\right)
$$

The values of the weighting factors $p_{j}, h_{j}, q_{j}(j=$ $1,2, \cdots, N)$ are assigned randomly. The structure of the ELM is shown in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Fig. 3. ELM-based model structure
Given the output of the ELM, the cost function for representing the comfortability score is constructed by

$$
J_{E}^{i}\left(a_{k}^{i}\right)=\sum_{k=1}^{M_{i}} R\left(x_{k}\right)
$$

Note that $J_{E}^{i}$ is linear in the weighting coefficient $w$, that is,

$$
\begin{aligned}
J_{E}^{i}\left(a_{k}\right) & =\sum_{k=1}^{M_{i}} R\left(x_{k}\right) \\
& =w^{\top} \sum_{k=1}^{M_{i}} \phi\left(x_{k}\right) \\
& =w^{\top}\left[\begin{array}{c}
\sum_{k=1}^{M_{i}} \tanh \left(p_{1} a_{k}^{i}+h_{1} k^{i}+q_{1}\right) \\
\sum_{k=1}^{M_{i}} \tanh \left(p_{2} a_{k}^{i}+h_{2} k^{i}+q_{2}\right) \\
\vdots \\
\sum_{k=1}^{M_{i}} \tanh \left(p_{N} a_{k}^{i}+h_{N} k^{i}+q_{N}\right)
\end{array}\right]
\end{aligned}
$$

Benefiting from this linearity, we are able to determine the optimal coefficient $w$ by minimizing the the following cost function:

$$
\min _{w} \sum_{i=1}^{S}\left\|J\left(a_{k}^{i}\right)-J_{E}^{i}\left(a_{k}^{i}\right)\right\|^{2}
$$

### 3.2 Seeking Optimal Acceleration profile

An advantage of the ELM representation of the comfortability score is that it enables us to seek the extremal acceleration signal by constructing an analytic algorithm, i.e., by finding an acceleration signal $a_{k}^{i}, k=1,2, ., M$ that maximizes the cost function $J_{E}\left(a_{k}\right)$. In this section, we discuss the EDA to reach this goal.
To simplify the problem of seeking the optimal acceleration profile, we represent the acceleration signal with four parameters, $a_{1}, a_{2}, t_{1}$, and $t_{2}$, which capture the fundamental
characteristics of the signal as shown in Fig. 4. Using this representation, the extremum seeking problem can be formulated as follows. Note that the optimization problem is discretized with time step $\Delta t$.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Shape of the acceleration

$$
\max _{u} \sum_{k=1}^{M} R(a, t)
$$

subject to

$$
\left\{\begin{array}{l}
u=\left[\begin{array}{lll}
a_{1} & a_{2} & t_{1} & t_{2}
\end{array}\right] \\
a(t)=\frac{a_{1}}{t_{1}} t \quad\left[t \leq t_{1}\right] \\
a(t)=\frac{a_{2}-a_{1}}{t_{2}-t_{1}}\left(t-t_{1}\right)+a_{1} \quad\left[t_{1}<t \leq t_{2}\right] \\
a_{\min } \leq a(t) \leq a_{\max } \\
0 \leq t_{1} \leq t_{2} \leq 6 \\
0 \leq t \leq t_{2} \\
M=\frac{t_{2}}{\Delta t}
\end{array}\right.
$$

An estimation of distribution algorithm, which is a stochastic optimization method, is used to solve this optimization problem. It searches for the optimum by building and sampling explicit probabilistic models of promising candidate solutions. Simply put, EDA is an extension of the genetic algorithm (GA). The difference between EDA and other meta-heuristic optimization methods is that it builds a probabilistic model that captures the probability distribution from the population of good candidate solutions. The flowchart of EDA is shown in Fig. 5.
The algorithm begins with an initial population of randomly generated individuals given a range of parameters. Then, the performance of each individual in the initial population is evaluated. Based on these evaluations, the top individuals are selected from the population. A probabilistic model is estimated based on these selected individuals. The next generation of individuals is generated by sampling the estimated probability model. The better the evaluation value, the higher the chance an individual makes its way into the next generation. Finally, the each individual in the next generation is evaluated. This process is repeated until the optimal solution is reached.

### 3.3 Powertrain Control Law

The acceleration of a vehicle is generated by control of the powertrain dynamics. As is shown in Fig. 6, the powertrain system considered in this paper has a combustion engine

![img-4.jpeg](img-4.jpeg)

Fig. 5. Flowchart of EDA
and two electric motors which generate power. As mentioned in the Section 2, the combustion engine is assumed to be operating at full throttle. Therefore, the only way to control the total propulsion power of the powertrain is to control the motor torques. In what follows, a dynamic control law for tuning the motor torque is designed by solving an optimal acceleration tracking problem.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Block diagram of the HEV driveline system
First, we summarize the model of the powertrain dynamics. Since the engine with a turbocharger is operating at full throttle, the torque generated by the engine is given by

$$
\dot{\tau}_{e}(t)=f_{\tau_{e}}\left(\omega_{e}(t)\right)
$$

where $\omega_{e}$ denotes the engine speed and $f_{\tau_{e}}(\cdot)$ is a nonlinear function that represents the torque raising rate with respect to engine speed. Note that the maximum torque during this engine starting period is constrained by a precalibrated bounding line $\tau_{e}^{\max }\left(\omega_{e}\right)$. The dynamics of the motor are modeled by

$$
\dot{\tau}_{m_{i}}(t)=\frac{1}{c_{m_{i}}}\left(u_{m_{i}}(t)-\tau_{m_{i}}(t)\right), \quad(i=1,2)
$$

where $u_{m_{i}}$ represents the torque commands and $c_{m_{i}}$ represents time constants. The maximum torque limits $\tau_{m_{1}}^{\max }$ and $\tau_{m_{2}}^{\max }$ of MG1 and MG2, respectively, are also given by their respective rotational speeds $\omega_{m_{1}}$ and $\omega_{m_{2}}$.
With consideration of the power transmission efficiency denoted by $\eta_{t}$, the total torque $\tau_{t}$ acting on the differential gear is given by

$$
\tau_{t}(t)=\eta_{t} i_{g}(t)\left(\tau_{e}(t)+\tau_{m_{1}}(t)\right)
$$

where $i_{g}$ denotes the gear ratio, including efficiency-loss. Taking efficiency-loss into account, the gear ratio during the transient period of gear changing is represented by

$$
i_{g}(t)=f_{g}\left(t, i_{g}\left(t^{*}\right), i_{g}^{f}\right), \quad t \in\left[t^{*}, t^{*}+0.7\right]
$$

where $t^{*}$ denotes the timing of gear shifting. Combining these two models, the transmission efficiency is given by

$$
\eta_{t}(t)=f_{\eta}\left(t, \eta_{t}\left(t^{*}\right), \eta_{t}^{f}\right), \quad t \in\left[t^{*}, t^{*}+0.7\right]
$$

where $f_{\eta}$ is a nonlinear continuous function and $\eta_{t}^{f}$ is the efficiency at the desired gear position after shifting gears. Moreover, during the gear shifting process, the gear ratio variation is approximated using a time-varying parameter $t$, where $f_{g}$ is a linear continuous function of time $t$ and $i_{g}^{f}$ denotes the ratio of the desired gear position.
Furthermore, when the clutch is engaged, considering the relation (8), the inertia dynamics of the powertrain system can be represented as

$$
\begin{aligned}
\dot{v} & =f_{v}\left(t, \tau_{e}, \tau_{m_{1}}, \tau_{m_{2}}, v\right) \\
& =\frac{1}{I_{1}+I_{2} \rho(t)}\left[C_{2} \eta_{t} i_{g}\left(\tau_{e}+\tau_{m_{1}}\right)+C_{1} \tau_{m_{2}}-F(v)\right]
\end{aligned}
$$

In Equation (11), $v$ represents vehicle speed, $I_{1}$ and $I_{2}$ represent the equivalent moment of inertia from the MG2 shaft to the vehicle driving shaft and the equivalent moment of inertia from the engine shaft to the wheel of the vehicle, respectively, $F(v)$ represents the road load that is a nonlinear function of vehicle speed, and $C_{1}=$ $\eta_{f} G_{m} G_{f} / R_{w}$ and $C_{2}=\eta_{f} G_{f} / R_{w} . \eta_{f}$ represents the final transmission efficiency, $R_{w}$ represents the radius of the vehicle wheel, and $G_{m}$ and $G_{f}$ represent the reduction ratio of the differential gears I and II, respectively.
Moreover, the $\omega_{m_{2}}$ is related to the vehicle speed by

$$
\omega_{m_{2}}=\frac{G_{m} G_{f}}{R_{w}} v
$$

Note that when the clutch is released, the vehicle operates in EV mode driven by MG2 while MG1 operates to start the engine. In summary, the engine speed has the following relations

$$
\left\{\begin{array}{l}
\left(I_{e}+I_{m_{1}}\right) \dot{\omega}_{e}=\tau_{e}+\tau_{m_{1}}, \text { clutch released } \\
\omega_{e}=\omega_{m_{1}}=\frac{i_{g}(t) G_{f}}{R_{w}} v, \quad \text { clutch engaged }
\end{array}\right.
$$

where $I_{e}$ and $I_{m_{1}}$ denote the inertias of the engine shaft and the MG1 shaft, respectively.
Thus, for a given optimal acceleration profile $a^{*}$ that is synthesized with the extremum seeking result $u^{*}$ given in Section 3.2, the optimal torque assistant control law can be found by solving the following optimal acceleration tracking problem subject to the system dynamics constraint.

$$
\begin{aligned}
& \min _{u} J(u)=\min _{u} \int_{t_{0}}^{t_{f}}\left(a^{*}(t)-a(t)\right)^{2} d t \\
& \text { subject to } \\
& \left\{\begin{array}{l}
\dot{v}(t)=f_{v}\left(t, \tau_{e}, \tau_{m_{1}}, \tau_{m_{2}}, v\right) \\
\dot{\tau}_{e}(t)=f_{\tau_{e}}\left(\omega_{e}(t)\right) \\
\dot{\tau}_{m_{i}}(t)=\frac{1}{c_{m_{i}}}\left(u_{m_{i}}(t)-\tau_{m_{i}}(t)\right) \\
0 \leq \tau_{e} \leq \tau_{e}^{\max }\left(\omega_{e}\right) \\
\tau_{m_{i}}^{\min }\left(\omega_{m_{i}}\right) \leq \tau_{m_{i}} \leq \tau_{m_{i}}^{\max }\left(\omega_{m_{i}}\right) \\
v_{\min } \leq v \leq v_{\max }
\end{array}\right.
\end{aligned}
$$

The control signal includes the torque command for both electric motors, that is, $u=\left[u_{m_{1}} u_{m_{2}}\right], t_{0}$ is the starting time of the acceleration mode, and $\left[t_{0}, t_{f}\right]$ denotes the acceleration period.

## 4. SIMULATION VALIDATION

In summary, a control design approach was proposed to achieve better comfortability as evaluated by an ELMbased cost function obtained via inverse reinforcement learning. The first step is to formulate a method for comfortability evaluation using inverse reinforcement learning. Using the result of IRL, an ELM-based cost function is constructed, and EDA is used to determine an optimal acceleration profile. This profile is used as a reference signal for the powertrain control, which is realized by solving an optimal acceleration tracking problem subject to the powertrain dynamics and other physical constraints. This proposed design approach is validated using numerical simulation.

300 acceleration data are used as training data for inverse reinforcement learning. The training data is generated by randomly varying the characteristic parameters (see Fig. 7 ), where the corresponding scores are $79.9,66.8$ and 58.0 , respectively. To evaluate the ELM-based cost function, the cost function was tested using a set of 90 data points. The root mean square error (RMSE) for this set was found to be 3.71 .
![img-6.jpeg](img-6.jpeg)

Fig. 7. Three samples of the training data
![img-7.jpeg](img-7.jpeg)

Fig. 8. The obtained reward function by IRL
The result of IRL is shown in Fig. 8, where the value of $R(a, k)$ is sketched. Observe that the performance during

Table 2. Physical parameter of powertrain

the initial raising period is mostly focused on evaluating the score. However, it should be noted that this reward function is nothing but an approximate representation with ELM of the evaluation score, hence, has no physical meaning. This implies that searching for the most comfortable acceleration profile $a^{*}(t)$ using this reward function or directly using this reward function as a cost function in optimizing the torque commands with the powertrain dynamics might not equate to the highest score. Moreover, there is no guarantee of the convexity of the extremum seeking or optimal control problem. Indeed, at the second step, the score of the obtained optimal acceleration profile is 71.4 , with the parameters given by

$$
a_{1}=a_{2}=2.60, t_{1}=2.5, t_{2}=4.5
$$

An interpolation curve of the signal is shown in Fig. 4. Using this signal as the desired acceleration reference $a^{*}(t)$, the optimal control input $u$ of the powertrain, i.e., the torque command for the electric motors, is obtained by solving the optimal problem formulated in Section 3.3 using a dynamic programming algorithm. The physical parameters of the powertrain are shown in Table 2, and the constraint conditions are defined as follows:

$$
v_{\min }=70(\mathrm{~km} / \mathrm{h}), \quad v_{\max }=100(\mathrm{~km} / \mathrm{h})
$$

Also, the clutch is engaged at $t_{0}=0.47[\mathrm{sec}]$ with $v\left(t_{0}\right)=70.76(\mathrm{~km} / \mathrm{h}), \tau_{c}\left(t_{0}\right)=302.1(\mathrm{Nm})$, and $\tau_{m 2}\left(t_{0}\right)=$ $44.03(\mathrm{Nm})$. The optimal control problem is solved for the period with $t_{f}=4.5(\mathrm{sec})$. Fig. 9 shows the optimal torque commands. It is seen that motor MG1 initially provides motoring torque to start the engine and MG2 provides assistant torque since the engine is not yet switched on. However, once the engine torque acts on the shaft, MG2 turns to reject the total torque by regenerative breaking. The actual acceleration response is as shown in Fig. 10, where an overshoot appears when the engine and the motors are switched on or off. The response of the optimized control is reasonable and the score calculated with the sum of the reward function is 72.4 . The score given by the expert model is 69.3 . The gap between these scores is caused by learning error.

## 5. CONCLUSION

For HEVs, especially in acceleration mode, the torque of the motor and the timing of gear shifting should be managed with consideration given to comfortability. When the combustion engine is operated at full throttle, if the vehicle begins accelerating in EV mode, the desired acceleration torque is too large. In this paper, a control design approach that gives rise to a motor assistant control law achieving comfortable acceleration behavior is proposed. The key contribution of this design approach is the use of inverse reinforcement learning for evaluating comfortability. It is shown that using IRL enables us to design a control law by optimizing an analytically formulated cost function.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Optimal torque commands
![img-9.jpeg](img-9.jpeg)

Fig. 10. Outputs of acceleration and vehicle speed

It should be noted that evaluation of comfortability is not an easy task. This is why the subject is challengeable when the comfortability is taken into power control account. Most existing approach such as shown in Shen (2020) the comfortability is described as a specification of the acceleration profile which enables us to directly apply the dynamical control method. This paper focuses on the human feeling which is eliminated as a non-analytic module. An inverse reinforcement learning approach is exploited to translate the comfortability feeling to an acceleration profile, then dynamical optimal control design is followed to obtain a comfortable acceleration profile.
