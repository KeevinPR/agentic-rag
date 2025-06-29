# Hybrid EDA-based Optimal Attitude Control for a Spacecraft in a Class of Control Task 

Xiong Luo<br>School of Information Engineering<br>University of Science and Technology Beijing<br>Beijing 100083, China<br>robertxiongluo@gmail.com<br>Zengqi Sun<br>Department of Computer<br>Science and Technology<br>Tsinghua University<br>Beijing 100084, China<br>National Laboratory of Space<br>Intelligent Control<br>Beijing 100080, China<br>szq-dcs@mail.tsinghua.edu.cn<br>Xiang Zhang<br>Yangtze University, Jingzhou, Hubei 434023,China<br>Laihong Hu<br>Department of Computer Science and Technology<br>Tsinghua University<br>Beijing 100084, China<br>Chao Wang<br>School of Information Engineering<br>University of Science and<br>Technology Beijing<br>Beijing 100083, China


#### Abstract

In the practical situation, if failure of one of the actuators occurs, there exists the attitude control task of a rigid spacecraft using only two control torques supplied by momentum wheel actuators. Here, this class of control task for a rigid spacecraft is discussed. This nonlinear control problem can be converted to the nonholonomic motion planning optimization problem of a driftfree system. In order to improve the search efficiency of current optimization algorithms, the hybrid estimation of distribution algorithm (EDA) is presented by combing the idea of differential evolution strategy (DES). Then, the optimal attitude control task for the spacecraft using two momentum wheel actuators is achieved. By comparing the proposed algorithm with existing genetic algorithm and evolutionary programming, the simulation results show the accuracy and efficiency of hybrid EDA.


## Categories and Subject Descriptors

1.2.8 [Artificial Intelligent]: Problem Solving, Control Methods, and Search - control theory, heuristic methods.

## General Terms

Algorithms, Design.

## Keywords

Estimation of distribution, differential evolution, spacecraft, control, optimization

## 1. INTRODUCTION

A rigid spacecraft can be controlled via three actuators, either gas jets or momentum wheels. Here, a class of control task problem in an actuator failure mode is discussed especially. Namely, in the practical situation, if failure of one of the actuators occurs, one is left with only two actuators. Then, there exists the optimal attitude control problem of a rigid spacecraft using only two

Copyright is held by the author/owner(s). GEC'09, June 12-14, 2009, Shanghai, China.
ACM 978-1-60558-326-6/09/06.
control torques supplied by momentum wheel actuators. It occupies an increasingly conspicuous position. Since the work of Crouch [1], there has been a great deal of research activity in this special control task problem [2]-[6].
In [2], the authors considered the attitude stabilization problem of a rigid spacecraft using control torques supplied by two momentum wheel actuators and constructed the discontinuous feedback control strategies that stabilize the spacecraft to any equilibrium attitude in finite time. In [3], the authors discussed the nonholonomic motion planning (NMP) for the same object using Ritz Approximation Theory and Gauss-Newton iteration method. But, the method used to search for the optimal solution was a local search one and its results strongly depended on the initial conditions. Recently in [4] and [5], for the same problem, the authors respectively proposed genetic algorithm (GA) and evolutionary programming (EP) to steer a rigid spacecraft with two momentum wheels. Unfortunately, the method used in [5] was too simple, which was only a traditional GA. Because of the essential characters of EP, the method used in [5] could not improve the search efficiency for the solution significantly.
In order to improve the computational accuracy, we will focus our discussion on how to find a solution for this class of control task using estimation of distribution algorithm (EDA). EDA is a new paradigm for evolutionary computation. It generalizes genetic algorithms by replacing the crossover and mutation operators by learning and sampling the probability distribution of the best individuals of the population at each iteration of the algorithm [6]. Currently, there is considerable enthusiasm for the research and application of EDA. In this paper, a hybrid EDA is proposed by combing EDA and differential evolution strategy (DES).

## 2. PROBLEM DESCRIPTION AND OPTIMIZATION MODEL

The rotational dynamic equations of a rigid spacecraft controlled by two momentum wheels, can be deduced by using the conservation theory of angular momentum. Thus, this control problem can be converted to the nonholonomic motion planning (NMP) problem of a drift-free system. Suppose the spacecraft

system is composed of the spacecraft $B_{0}$, and two momentum wheels $B_{1}, B_{2}$. The demonstration can be found in Fig. 1 [2].

Let $m_{i}(i=0,1,2)$ be the mass of the spacecraft $B_{0}$, and two wheels $B_{1}, B_{2}$, respectively. Let $\mathbf{I}_{i}(i=0,1,2)$ be the inertial tensors of $B_{0}, B_{1}$, and $B_{2}$, respectively. Let $\mathbf{p}_{i}(i=0,1,2)$ be the position vectors of the center of mass of $B_{0}, B_{1}$, and $B_{2}$, respectively, with respect to the center of mass of the whole system. Consider an inertial $X Y Z$ coordinate frame, let $x y z$ be a coordinate frame aligned with principal axes of the spacecraft with origin at the center of mass of the spacecraft. If the two frames are initially coincident, a series of three rotations about the body axes performed in the proper sequence is sufficient to allow the spacecraft to reach any orientation [2]. Assume two wheels $B_{1}$ and $B_{2}$ spinning about axes defined by unit vectors $\mathbf{b}_{1}, \mathbf{b}_{2}$ fixed in the spacecraft. Further $\mathbf{b}_{1}$ and $\mathbf{b}_{2}$ span a two-dimensional plane that is orthogonal to a principal axis of the spacecraft. Without loss of generality, $\mathbf{b}_{i}(i=l, 2)$ can be expressed as: $\mathbf{b}_{i}=\left(b_{i 0}, b_{i 1}, 0\right)^{T}$. Meanwhile, according to the location of the wheels, the position vectors can be described as: $\mathbf{p}_{i}=\left(\rho_{i 1}, \rho_{i 1}, 0\right)^{T}(i=0,1,2)$.

Let $\theta_{i}(i=1,2)$ be the angles of rotation of wheels $B_{1}$ and $B_{2}$ about the axis defined by $\mathbf{b}_{1}$ and $\mathbf{b}_{2}$. Let the attitude angles $\mathbf{q}=(\theta, \psi, \phi)^{T}$ be the state variable $(\theta, \psi$ and $\phi$ are Carden angles). Let the angles velocity $\dot{\theta}_{i}(i=1,2)$ be the control input variable. Define $\mathbf{u}=\left(u_{1}, u_{2}\right)^{T}=\left(\dot{\theta}_{1}, \dot{\theta}_{2}\right)^{T}$. Then, under the hypothesis that the angular momentum vector of system is zero, we can obtain the state equation of the controlled system [4]:

$$
\left\{\begin{array}{l}
\dot{\mathbf{q}}=B(\mathbf{q}) \mathbf{u} \\
B(\mathbf{q})=\left(-\mathbf{L}^{-1}\left(\sum_{i=0}^{2}\left(\mathbf{I}_{i}+\overline{\mathbf{I}}_{i}\right)\right)^{-1}\right) \cdot\left[\underline{\mathbf{1}}_{1} \mathbf{b}_{1} \quad \underline{\mathbf{1}}_{2} \mathbf{b}_{2}\right]
\end{array}\right.
$$

where
![img-0.jpeg](img-0.jpeg)

Figure 1. The demonstration of the spacecraft system.

$$
\left[\begin{array}{c}
\mathbf{I}_{i}=\left[\begin{array}{ccc}
\cos \psi \cos \phi & \sin \phi & 0 \\
-\cos \psi \sin \phi & \cos \phi & 0 \\
\sin \psi & 0 & 1
\end{array}\right] \\
\mathbf{J}=\mathbf{I}_{0}+\sum_{i=0}^{2} \overline{\mathbf{I}}_{i}+\sum_{i=1}^{2}\left(\mathbf{I}_{i}-\underline{\mathbf{I}}_{i}\right) \\
\overline{\mathbf{I}}_{i}=m_{i}\left[\begin{array}{ccc}
\rho_{i 0}^{2} & -\rho_{i 1} \rho_{i 2} & 0 \\
-\rho_{i 1} \rho_{i 2} & \rho_{i 2}^{2} & 0 \\
0 & 0 & \rho_{i 2}^{2}+\rho_{i 2}^{2}
\end{array}\right] \quad(i=0,1,2) \\
\mathbf{I}_{j}=\mathbf{b}_{j} \mathbf{b}_{j}^{T} j_{j}=\left[\begin{array}{ccc}
b_{i 1}^{2} & b_{i 1} b_{i 2} & 0 \\
b_{i 2} b_{i 2} & b_{i 2}^{2} & 0 \\
0 & 0 & 0
\end{array}\right] \cdot j_{i} \quad(i=1,2)
$$

Here, $\mathbf{J}$ is the inertial matrix, $j_{j}(i=1,2)$ are the moments of inertia of wheels $B_{1}$ and $B_{2}$ about the axis defined by $\mathbf{b}_{1}$ and $\mathbf{b}_{2}$.
The Eq. (1) is nonintegrable. Thus, the discussed control problem in this paper has nonholonomic constraints. In deed, it is a NMP problem. Given the initial and final configurations $\mathbf{q}_{0}$ and $\mathbf{q}_{f}$ of spacecraft system, it is requested to find a set of optimal control inputs $\mathbf{u}(t) \in \mathbb{R}^{2}(t \in[0, T])$ to steer system (1) from $\mathbf{q}_{0}$ to $\mathbf{q}_{f}$ [4].
Based on the principle of minimum energy control, the optimal control object of system is to minimize the rotation dissipated energy of the momentum wheels. Let $\left\{e_{i}\right\}_{i=1}^{N}$ be an orthonormal basis for $L_{2}([0, T])\left(L_{2}([0, T])\right.$ denotes the Hilbert space composed of measurable vector-valued functions). Based on the idea of Ritz Approximation Theory, the cost function can be described as [4]:

$$
\mathbf{Y}(\mathbf{a})=\sum_{i=1}^{N} \alpha_{i}^{2}+\sum_{j=1}^{3} \gamma_{j} \cdot\left(\hat{q}^{(j)}-q_{f}^{(j)}\right)^{2}
$$

where $\mathbf{q}_{f}=\left(q_{f}^{(1)}, q_{f}^{(2)}, q_{f}^{(3)}\right)^{T}, \mathbf{a}=\left\{\alpha_{i}\right\}_{i=1}^{N} \in \mathbb{R}^{N}$ are the projects of $\mathbf{u}$ on $\left\{e_{i}\right\}_{i=1}^{N},\left\{\gamma_{j}\right\}_{j=1}^{3}$ is a penalty coefficient vector, $\left\{\hat{q}^{(j)}\right\}_{j=1}^{3}$ is the solution of the Eq. (1) at $t=T$.

Our problem is to find $\mathbf{a} \in \mathbb{R}^{N}$ such that the objective function in Eq. (3) is minimized. As mentioned in Section 1, there are some methods used to find $\boldsymbol{\alpha}$ [3-5]. However, because of the essential limitations of the proposed algorithms, it is restricted to use in a larger range in some degree. In this paper, in order to improve the computational accuracy, we use hybrid EDA to solve optimization problem (3).

## 3. HYBRID EDA BASED OPTIMAL ATTITUDE CONTROL APPROACH

Estimation of Distribution Algorithm (EDA) is a family of evolutionary algorithms. Its appealing features over other evolutionary algorithms are a simple structure and an intuitive dynamics of the population which facilitate choosing the values of

the control parameters [6]. Here, we design advanced EDA based on differential evolution strategy (DES). DES is a relatively new evolutionary optimization algorithm [7]. There exists some work concerning the algorithm design by combining these two issues [8]. But, the hybrid algorithm is too complex to apply easily. So, we propose a hybrid EDA that is with the simple form and easy to increase the diversity of population.

The framework of hybrid EDA can be found in Fig. 2. The main steps of hybrid EDA are shown as following.

## (1) Generation of initial population

To improve calculate precision, real numbers are chosen as the coding style. According to the objective function (3), we can directly define the individuals as: $\mathbf{a}=\left\{\alpha_{i}\right\}_{i=1}^{N} \in \mathbb{R}^{N}$. The initial population is sampled random from the subset of parameter space.

## (2) Calculation of the fitness of every individual

The fitness must show the closeness of each individual to the best solution and needs to be easy to be calculated. Here, the fitness function can be defined as: $F(\mathbf{a})=1.0 / \mathbf{Y}(\mathbf{a})$

## (3) Selection of individuals with high fitness

According to the fitness which calculated in Step (2), individuals with high fitness are chosen to generate new population.

## (4) Generation of new population

Gaussian model is chosen for its low computation load. Mean and variance of the chosen individuals are calculated. Then, in the $t$-th generation, new population $\mathbf{P}(t)$ generated via Gauss sampling based on the calculated mean and variance.
(5) Population modification based on differential evolution strategy

Define $\mathbf{P}(t)=\left\{\boldsymbol{\alpha}_{j}(t)\right\}_{j=1}^{S}$. Here, $S$ be the size of a population and $\boldsymbol{\alpha}_{j}(t)=\left\{\alpha_{j}^{(i)}(t)\right\}_{j=1}^{N}$.

For every individual $\boldsymbol{\alpha}_{j}(t)$, a new individual is generated according to:
![img-1.jpeg](img-1.jpeg)

Figure 2. The framework of hybrid EDA

$$
\begin{aligned}
& \alpha_{j}^{(i)^{T}}(t)=\left\{\begin{array}{lc}
\alpha_{j}^{(i 1)}(t)+\ell \cdot\left(\alpha_{j}^{(i 2)}(t)-\alpha_{j}^{(i 3)}(t)\right), \\
\text { if } \operatorname{rand}[0,1]<P_{c} \text { or } j=j_{\text {rand }} \\
\alpha_{j}^{(i)}(t), & \text { otherwise }
\end{array}\right. \\
& \ell=\bar{a}+\bar{c} \cdot \operatorname{rand},[0,1] \\
& \boldsymbol{\alpha}_{j}(t+1)=\left\{\begin{array}{l}
\boldsymbol{\alpha}_{i}{ }^{\prime}(t)=\left(\alpha_{j}^{(i)^{T}}(t)\right)_{j=1}^{N} \text {, if } F\left(\boldsymbol{\alpha}_{i}{ }^{\prime}(t)\right)>F\left(\boldsymbol{\alpha}_{i}(t)\right) \\
\boldsymbol{\alpha}_{i}(t), \quad \text { otherwise }
\end{array}\right.
\end{aligned}
$$

where random indexes $r 1, r 2$, and $r 3$ are integers $(r 1, r 2, r 3 \in\{1,2, \cdots, S\})$, mutually different, and also chosen to be different from the running index $i . P_{c}$ is the parameter which is a real-valued crossover factor in range $[0,1]$. Random index $j_{\text {rand }} \in\{1,2, \cdots, N\}$. $\bar{\ell}$ is strongly problem-dependent and the user can choose $\bar{\ell}$ after some trial and error tests. In the Eq. (5), $\bar{\ell}$ is varied randomly within specified range. Here, $\bar{a}$ and $\bar{c}$ are positive and real-valued constant, and the sum of $\bar{a}$ and $\bar{c}$ is less than 1 .

Then, $\mathbf{P}(t+1)=\left\{\boldsymbol{\alpha}_{j}(t+1)\right\}_{i=1}^{S}$ is the modified new population.
(6) Repeat Step (2)-(5) until current population satisfy the terminal condition, and choose the best individual.

## 4. SIMULATION RESULTS

Matlab has been used to implement the hybrid EDA. We consider an example appeared in [2]. There is a rigid spacecraft with no control torque about the third principal axis and two control torques, generated by momentum wheel actuators, are applied about the other two principal axes. Thus, the vectors $\mathbf{b}_{1}$ and $\mathbf{b}_{2}$ are defined as $(1,0,0)^{T}$ and $(0,1,0)^{T}$. Moreover,

Then, the inertial matrix $\mathbf{J}$ appeared in Eq. (2) is:

$$
\mathbf{J}=\operatorname{diag}(86.663039,85.518039,114.461078) \mathrm{kg} \cdot \mathrm{~m}^{2}
$$

The initial and final configurations of spacecraft system described by Carden angle are: $\mathbf{q}_{0}=(0,0,0)^{T}$ and $\mathbf{q}_{f}=(0,0, \pi / 6)^{T}$. Namely, the final configuration is a rotation from the initial configuration about the third axis without a wheel [8]. Let $N$ be 10 . Select 10 terms of the orthonormal Fourier basis for $L_{2}([0, T])$, where $T=5 \mathrm{~s}$. The first 5 basis elements are:

$$
\begin{aligned}
& e_{1}=(0.5,0)^{T} e_{2}=(\sin t, 0)^{T} e_{3}=(\cos t, 0)^{T} \\
& e_{4}=(\sin 2 t, 0)^{T} e_{5}=(\cos 2 t, 0)^{T}
\end{aligned}
$$

The remaining 5 terms can be obtained by permuting rows of the above elements.

For this example, we use Newton iteration method mentioned in [3], GA mentioned in [4], EP mentioned in [5], and the proposed algorithm to find the optimal solution, respectively. In the hybrid EDA, we assume the population size is 100 , the upper limit value of evolutionary generation is 500 . The simulation results can be found in Table 1.

By checking the Table 1, we find the optimal solution obtained by using hybrid EDA is better than the existing results obtained by using the other three algorithms. In addition, the convergence rate of hybrid EDA is better than that of EP and GA.

In order to confirm the validity of optimal solution, we also give the relation curves of optimal solutions. Fig. 3 shows the optimal control inputs ( $u_{1}$ and $u_{2}$ ) for the angles velocity of rotation of two wheels about the principal axes.

## 5. CONCLUSION

A class of control task for spacecraft is analyzed in this paper. That is, the optimal attitude control of a rigid spacecraft using only two control torques supplied by momentum wheel actuators. Under the restriction that the total angular momentum vector of the spacecraft system is zero, the dynamic system is controllable. Then, this nonlinear control problem can be converted to the nonholonomic motion planning problem of a drift-free system. The hybrid EDA is presented by combing the idea of DES to achieve optimal attitude control task for the spacecraft using two momentum wheel actuators. By comparing the proposed algorithm with existing Newton iteration method, GA, and EP, the simulation results show that the accuracy and efficiency of the hybrid EDA.

## 6. ACKNOWLEDGMENTS

This work was jointly supported by National Natural Science Foundation of China under Grant 60604010, 90716021, 60736023, and 60773073 and Foundation of National Laboratory of Space Intelligent Control of China under Grant SIC07010202.

## 7. REFERENCES

[1] Crouch, P. E. 1984. Spacecraft attitude control and stabilization: application of geometric control theory to rigid body models. IEEE Transactions on Automatic Control, 29, 4(Aug. 1984), 87-95.
[2] Krishnan, H., McClamroch, N. H., and Reyhanoglu, M. 1995. Attitude stabilization of a rigid spacecraft using two momentum wheel actuators. Journal of Guidance, Control and Dynamics, 18, 2(Apr. 1995), 256-263.
[3] Ge, X. S., Chen, L. Q., and Liu, Y. A. 2004. Nonholonomic motion planning for the attitude of rigid spacecraft with two momentum wheel actuators. Control Theory and Applications, 21, 5(Oct. 2004), 781-784.

Table 1. Comparison of four methods applied to the example

| Algorithm | The optimal solution $\sqrt{\sum \alpha_{i}^{2}}$ |
| :--: | :--: |
| Newton iteration [3] | 45.1200 |
| GA [4] | 37.9752 |
| EP [5] | 37.0845 |
| Hybrid EDA | 36.8848 |

![img-2.jpeg](img-2.jpeg)
(b)

Figure 3. The optimal control inputs of two momentum wheels
[4] Ge, X. S. and Chen, L. Q. 2004. Attitude control of a rigid spacecraft with two momentum wheel actuators using genetic algorithm. Acta Astronautica, 55, 1(Jan. 2004), 3-8.
[5] Luo, X. and Sun, Z. Q. 2006. Optimal attitude control for a spacecraft using two momentum wheel actuators based on intensified evolutionary programming. Dynamics of Continuous, Discrete and Impulsive Systems, Series A: Mathematical Analysis, 13, Suppl. 5(Dec. 2006), 733-737.
[6] Larranaga, P. and Lozano, J. A. (Eds.) 2001. Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Dordrecht: Kluwer Academic Publishers, 2001.
[7] Price, K. V., Storn, R. M., and Lampinen, J. A. 2005. Differential Evolution: A Practical Approach to Global Optimization. London: Springer-Verlag, 2005.
[8] Cho, D. Y. and Zhang, B. T. 2004. Evolutionary continuous optimization by distribution estimation with variational Bayesian independent component analyzers mixture model. Lecture Notes in Computer Science, 3242(Apr. 2004), 212221.