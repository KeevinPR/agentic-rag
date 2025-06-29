# Mechanics Based Design of Structures and Machines 

An International Journal

## Structure-control design of a mechatronic system with parallelogram mechanism using an estimation of distribution algorithm

S. Ivvan Valdez, E. Chávez-Conde, Eusebio E. Hernandez \& M. Ceccarelli

To cite this article: S. Ivvan Valdez, E. Chávez-Conde, Eusebio E. Hernandez \& M. Ceccarelli (2016) Structure-control design of a mechatronic system with parallelogram mechanism using an estimation of distribution algorithm, Mechanics Based Design of Structures and Machines, 44:1-2, 58-71, DOI: 10.1080/15397734.2015.1035785

To link to this article: http://dx.doi.org/10.1080/15397734.2015.1035785

Published online: 06 Apr 2016.

Submit your article to this journal

Article views: 2

View related articles

View Crossmark data

Full Terms \& Conditions of access and use can be found at http://www.tandfonline.com/action/journallnformation?journalCode=Imbd20

# Structure-control design of a mechatronic system with parallelogram mechanism using an estimation of distribution algorithm 

S. Ivvan Valdez ${ }^{a}$, E. Chávez-Conde ${ }^{b}$, Eusebio E. Hernandez ${ }^{c}$, and M. Ceccarelli ${ }^{d}$<br>${ }^{a}$ Center for Research in Mathematics (CIMAT), Department of Computer Science, Guanajuato, Mexico; ${ }^{\text {b }}$ University of Papaloapan Campus Loma Bonita, Loma Bonita, Mexico; ${ }^{c}$ National Polytechnic Institute, ESIME-UPT, Section of Graduate Studies and Research, Mexico City, Mexico; ${ }^{d}$ Laboratory of Robotics and Mechatronics, University of Cassino and Southern Lazio, Cassino, Italy


#### Abstract

In this paper, a structure-control design methodology for simultaneously optimizing both mechanical structure and control of a parallelogram linkage robot is proposed. It takes into count the dynamical model and the mechanical parameters for the optimization process along with the controller. Thus, proportional-integral-derivative (PID) control and geometric variables are optimized in a simultaneously way. Through the concurrent procedure an optimal combination of the robot structure and controller gains is obtained. The global optimization problem is tackled by using an estimation of distribution algorithm (EDA) based on the Boltzmann distribution. The EDA seeks for the global optimum by estimating and sampling a probability distribution. The proposed methodology is verified through simulation experiments and applied to the design process of a parallelogram linkage system. The results obtained in experiments show the effectiveness of the proposal. This approach is generic and could be applied to other mechanisms in similar way when for concurrent process both kinematic and dynamic models are available along with the controller. In particular, the results are promising when the optimization parameters are uncorrelated, namely control and mechanical parameters.


## ARTICLE HISTORY

Received 26 March 2015 Accepted 26 March 2015

## KEYWORDS

Concurrent design; estimation of distribution algorithms; optimization; parallelogram linkage

## 1. Introduction

Products or systems dedicated for applications requiring high performance, require a multidisciplinary approach in their design process with an integrated approach. It can be considered that the mechatronic design is the integrated design of a mechanical system and its embedded control system (see, van Amerongen, 2003). In particular, the design process of robot manipulators can benefit greatly from the perspective of mechatronic design (see, Youcef-Toumi, 1996).

In recent years, parallel mechanisms have attracted increasing attention from research community and industry. It is well known that compared with traditional serial mechanisms, parallel mechanisms have potential advantages in accuracy, dynamic, and stiffness. Many architectures of robots using parallel mechanisms have been proposed and analyzed. However, the practical parallel structures show a significant difference between the expected and actual performance, due to passive joints that introduce geometric errors and deformations. In addition, most existing structures have limited workspace and singularities. This is a very demanding task for the design process of a parallel structure. Traditionally, the mechanism to be controlled is designed first and independently of the control scheme (see, for example

[^0]
[^0]:    CONTACT Eusebio E. Hernandez euhernandezm@ipn.mx National Polytechnic Institute, ESIME-UPT, Section of Graduate Studies and Research, Av. Ticomán, Col. San José Ticomán, Mexico City 07340, Mexico.
    Color versions of one or more of the figures in the article can be found online at www.tandfonline.com/Imbd. Communicated by Marco Ceccarelli.
    (c) 2016 Taylor \& Francis

Delchev and Zahariev, 2008 and Valles et al., 2012). In this case, a strategy similar to the fixed point method is used, it is to say, first we optimize about the lengths, once we get optimal lengths we intend to optimize control parameters. This kind of approaches, are not actually looking for a global optimum, but find the optimum in projections of the objective function with respect of a subset of variables, and then report the optimum in such projections as an approximation of the global optimum. In our case, we tackle the actual global optimization problem, without any assumption about independence of the control and length parameters.

Thus, the design and development of these kind of structures requires a multidisciplinary approach. The optimal design of these kind of structures, considered as mechatronic systems, can be stated as a traditional optimization problem. However, the optimization techniques to address these problems can be attracted by local minima, are sensitive to initial conditions or involve the computation of gradients of the objective function.

By instance, in Pil and Asada (1996), an integrated structure/control design method is proposed, based on an iterative algorithm, for the development of a robotic system. The mechanical structure is modified iteratively by using the structure reinforcement and rapid prototyping techniques, coupled with the adjustment of the control parameters according to the mechanical structure updated. This kind of approaches requires continuity and differentiability in all the configurations that are tested iteratively, it is quite possible that these characteristics are not accomplished, hence methods to circumvent numerical problems must be proposed. In Pil and Asada (1996) some methods to circumvent these problems are proposed, such as robust numerical estimations of jacobian matrices. Even though it is not sufficient to always adequately solve this problem, even if the problem of differentiability, continuity, and numerical singularities are solved, this kind of methods can converge to a local optimum. In Li (2006), an approach to the methodology of design for control is presented, applied to a five-bar mechanism. In the optimization process is considering the mass balancing in order to simplify as far as possible, the dynamic model, and so design a controller for tracking path, simultaneously.

Recently, with the aim to circumvent these problems, optimization techniques based on metaheuristic methods have been used in the design process of different mechatronic systems. In Ravichandran et al. (2006), optimization techniques based on a heuristic evolutionary algorithm are selected for optimizing both the design parameters and non-linear PD controller gains of a two-link planar manipulator. In Portilla-Flores et al. (2011), a method based on the differential evolution algorithm is implemented to address the optimization problem in the concurrent structure and control design of mechatronic systems.

Others works about structure-control design that have been presented in the last decade use genetic algorithm (see, Affi et al., 2007) or non-dominated sorting genetic algorithm (NSGA-II) for the optimization process (see, da Silva et al., 2009, EL-Kribi et al., 2013, and Liu et al., 2012). It is remarkable that until now all integrated design approaches are applied to simple mechanisms such as four-bar mechanisms (EL-Kribi et al., 2013; Affi et al., 2007), five-bar linkages (Villarreal-Cervantes et al., 2014, 2013), and for a Cartesian robot based on three linear motor motion system (see, da Silva et al., 2009).

Most of the above design optimization problems are solved by widely used stochastic methods, which have been successful in approaching the problem, but lack of a consistent interpretation of its way of working from a mathematical viewpoint. Actually they are consistent since the artificial evolution point of view, additionally neither apriori information nor a posteriori information can be introduced or obtained, respectively, from these algorithms.

We propose the use of Estimation of Distribution Algorithms (EDAs), (see, Mühlenbein and Paa $\beta$, 1996), for addressing the design optimization problem. The EDAs maintain the advantages of other evolutionary algorithms, it is to say, they approach the global optimum, and do not require gradients or continuity, while they have a more explainable way of working from the mathematical point of view. Additionally, the EDA proposed to be used in this work has proven statistically to require less evaluations than similar algorithms and to provide high quality of solutions, when the optimization parameters are considered uncorrelated. In this work we use an EDA based on the Boltzmann

distribution: the Boltzmann Univariate Marginal Distribution Algorithm (BUMDA), (see, Valdez et al., 2013). It has been proven that conceptual EDAs based on the Boltzmann selection, such as the Boltzmann EDA (BEDA), (see, Mühlenbein et al., 1999), converge to the optimum (see, Zhang and Mühlenbein, 2004). The BUMDA uses the Boltzmann distribution through a Gaussian model, fitted according to the Kullback-Leibler divergence. The BUMDA aim is to preserve the desired characteristics of the Boltzmann distribution, while maintaining a low computational cost in the estimation and sampling steps.

In this paper, the design of a parallelogram linkage robot is carried out by this approach which integrates in a simultaneous way the structure design parameters of the robot and the PID controller gains, in order to optimize its mechanical design and to minimize the position error for a specific path. Thus, both the structure design and the controller design are simultaneously evaluated in order to obtain an appropriate system performance. The aim of this paper is to obtain the set of optimal mechanical and controller parameters in a concurrent way. The paper is organized as follows: Section 2 introduces the proposal of our concurrent design methodology. Section 3 describes the estimation of distribution algorithm-based approach. Section 4 presents the kinematic and dynamic models, and the motion controller for a Parallelogram Linkage System (PLS) as a case of study, while the optimization problem is depicted in Section 5. The results of experiments are showed and analyzed in Section 6. Finally, the conclusions are presented in Section 7.

# 2. Concurrent design methodology 

The concurrent design methodology proposed in this paper, considers the design process as a mapping from a requirement space to a structural space. In Li et al. (2001), is suggested dividing the requirement space into two subspaces: real-time behaviors (e.g., desired path, desired tracking speeds), and non-real-time behaviors (e.g., workspace, maximum payload). Following this division, the system parameters in the structural space can also be divided into two subspaces: real-time parameters (e.g., controller gains), and non-real-time parameters (e.g., kinematics and dynamics parameters). This viewpoint has been adapted for the optimal integrated design of a parallelogram linkage robot proposed in this paper, to optimize the structural parameters and the controller gains simultaneously, satisfying the restrictions set imposed, by using an estimation distribution algorithm. It is recommended to include constraints for mass and force balance, or constraints for dynamic model simplification.

The optimization process could consider the following criteria:

- Design objectives: (1) Minimizing position error $e_{i}(t)$ for a given path. Considering, $E=$ $\min \sum_{i=1}^{n}\left|e_{i}(t)\right|$ with $e_{i}(t)=q_{i}^{*}-q_{i}$, where $q_{i}^{*}$ and $q_{i}$ are the $i$-th generalized coordinates desired and actual, respectively, for $n$ generalized coordinates. (2) Maximizing a manipulability measure $w(\mathbf{q})$ (away from singularities). Considering, $S=\max w(\mathbf{q})$, with $w(\mathbf{q})=\sqrt{\operatorname{det}(J(\mathbf{q}) J^{T}(\mathbf{q}))}$, where $J(\mathbf{q})$ is the Jacobian matrix of robotic mechanism.
- Design constraints: (1) Inequalities design constraints (e.g., kinematic and dynamic parameters, actuator power, workspace). (2) Equality design constraints (e.g., dynamic model simplification, desired path).
- Design variables: Design parameters vector $\mathbf{X}$ (e.g., kinematic and dynamic parameters, controller gains), $\mathbf{X} \subset \mathbb{R}^{n}$.
The actual objective function depends on the particular problem. Thus, in the case of study we will provide the specific model for such application.

Figure 1 shows a flow diagram of the process performed by the estimation of distribution algorithm, used in this concurrent design methodology. Each of the blocks in the diagram are explained in more detail in the following sections.

![img-0.jpeg](img-0.jpeg)

Figure 1. Flow diagram of the automated design process using an Estimation of Distribution Algorithm (BUMDA).

# 3. The Boltzmann Univariate Marginal Distribution Algorithm (BUMDA) 

Estimation of Distribution Algorithms estimate and sample from a probability distribution. An EDA usually starts with an uniform initial sample, then it is evaluated, the best candidate solutions in the sample are selected, the selected set is used to re-estimate the probability distribution, and so on. The BUMDA (see, Valdez et al., 2013) is an EDA based on the Boltzmann distribution, the Boltzmann distribution is approximated by a Gaussian distribution because of its characteristics for estimating its parameters and sampling.

The BUMDA accomplishes two desired characteristics in any optimization algorithm:

- It maintains a non-decreasing sequence of the expected value of the objective function. In order to obtain better samples than the generation before.
- It converges to the best solution found. This allows to refine the solution, and to determine when the algorithm rarely will improve the best solution known.
The convergence is achieved by applying a truncation selection method which increases the mean of the objective value of the current sample, such as explained in Fig. 2. We ensure that it is always at least one element in the selected set by preserving the elite candidate solution.

The whole BUMDA is shown in Fig. 3. Notice that the BUMDA uses the truncation selection method to ensure a non-decreasing average (mean estimator) of the objective function of the sample. In addition, the objective function of the selected set is used to incorporate information about the fitness landscape into the Gaussian model. As can be seen it requires of two parameters: a sample size and a minimum variance, in comparison with other similar optimization algorithms the number of parameters is quite small. As suggested in Valdez et al. (2013), the sample size is chosen by setting an initial value, then increasing it until the algorithm performance does not change. The minimum variance allowed is of $5 \times 10^{-5}$ and is related with the maximum error allowed.

# Truncation Selection Method 

Consider a sample of decreasingly sorted candidate solutions (maximization case), such that $x_{1}$ are the decision variables of the candidate solution with the maximum objective function in the sample:

1. For the initial generation $t=0$, let be $g\left(x_{i}, 0\right)$ for $i=1 . . N$, the objective values of the initial sample. Define: $\theta_{0}=\min g\left(x_{i}, 0\right)$.
2. For $t>0$, set:
$\theta_{t}=\max \left(g\left(x_{N / 2}, t\right), \min \left(g\left(x_{i}, t\right) \mid g\left(x_{i}, t\right) \geq \theta_{t-1}\right)\right)$.
3. Truncate the sample such that $g\left(x_{s}, t\right) \geq \theta_{t}$. Where $x_{s}$ are all the candidate solutions whose objective values are equal or greater than $\theta_{t}$.

Figure 2. Truncation method to ensure convergence in the EDA.

## BUMDA

1. Give the parameter and stopping criterion:
nsample $\leftarrow$ Number of candidate solutions to be sample.
minvar $\leftarrow$ Minimum variance allowed.
2. Uniformly generate the initial sample $X_{0}$, set $t=0$.
3. While $v>$ minvar for all dimensions
(a) $t \leftarrow t+1$
(b) Evaluate and truncate the sample according to the algorithm in Fig. 2.
(c) Compute the approximation to $\mu$ and $v$ (for all dimensions) by using the selected set (of size nselec), as follows:
$\mu \approx \frac{\sum_{1}^{\text {nselec }} x_{i} \bar{g}\left(x_{i}\right)}{\sum_{1}^{\text {nselec }} \bar{g}\left(x_{i}\right)}, \quad v \approx \frac{\sum_{1}^{\text {nselec }} \bar{g}\left(x_{i}\right)\left(x_{i}-\mu\right)^{2}}{1+\sum_{1}^{\text {nselec }} \bar{g}\left(x_{i}\right)}$,
where $\bar{g}\left(x_{i}\right)=g(x)-g\left(x_{\text {nselec }}\right)+1$.
Note: the candidate solutions can be sorted to simplify the computation, and $g\left(x_{\text {nselec }}\right)$ is the minimum (for maximization case) objective value of the selected.
(d) Generate $n$ sample -1 candidate solutions from the new model $Q(x, t)=\operatorname{Normal}(\mu, v)$, and insert the elite candidate solution.
4. Return the elite candidate solution as the best approximation to the optimum.

Figure 3. Pseudo-code for BUMDA.

Some of the BUMDA advantages are the following:

- The BUMDA converges to the best approximation to the optimum.
- The variance tends to 0 for a large number of generations.
- The BUMDA only needs one parameter (sample size).
- The estimation of the search distribution parameters results in a fast automatic adaptation. The variance could be increased or decreased, according to the solutions in the selected set and their objective values, and the mean moves fast to the region where the best solutions are.


# 4. Case of study: A parallelogram linkage system 

The proposal is applied for the design process of a parallelogram linkage system, which can be considered as a parallel robot. Research on parallel robots have been increased recently due to their advantages in comparison with serial robots, such as high stiffness, elevate speed and accelerations, and a precise positioning capability. However, they show some disadvantages too, as singularities, friction losses or reduced workspace. Additionally, there is not a well developed standard method for analysis, synthesis, and control. The mechanism to be controlled is very often designed first and independently of the control scheme. Thus, the parallel robot design remains a challenge for optimizing both mechanical and control parameters in a concurrent way. Figure 4 shows a diagram of the parallelogram robot considered in this paper.

### 4.1. Kinematic model of PLS

The direct kinematic is given as,

$$
\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{l}
L_{1} \cos \varphi_{1}-L_{4} \cos \varphi_{2} \\
L_{1} \sin \varphi_{1}-L_{4} \sin \varphi_{2}
\end{array}\right]
$$

The solution of the inverse kinematic problem can be computed as,

$$
\begin{aligned}
& \varphi_{1}=\tan ^{-1}\left(\frac{y}{x}\right)-\tan ^{-1}\left(\frac{L_{4} \sin \gamma}{L_{1}+L_{4} \cos \gamma}\right), \quad \gamma=\tan ^{-1}\left(\frac{-\sqrt{1-d^{2}}}{d}\right) \\
& \varphi_{2}=\varphi_{1}+(\gamma+\pi), \quad d=\cos \gamma=\frac{x^{2}+y^{2}-L_{1}^{2}-L_{4}^{2}}{2 L_{1} L_{4}}
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Figure 4. A schematic diagram of the parallelogram linkage system.

where $L_{1}, L_{2}, L_{3}, L_{2}+L_{4}$ are the link lengths, $l_{c 1}, l_{c 2}, l_{c 3}, l_{c 4}$ are the locations of the mass centers for each link, $\varphi_{1}$ and $\varphi_{2}$ are the angular positions for the link 1 and link 2, respectively. In the same form, the differential kinematics can be computed as,

$$
\dot{\mathbf{x}}=J(\mathbf{q}) \dot{\mathbf{q}}
$$

where, $\dot{\mathbf{x}}=[\dot{x} \dot{y}]^{T}$ is the vector of Cartesian velocities in the end-effector, $\dot{\mathbf{q}}=\left[\dot{\varphi}_{1} \dot{\varphi}_{2}\right]^{T}$ is the vector of angular velocities of the link 1 and link 2, and the Jacobian matrix is given by,

$$
J(\mathbf{q})=\left[\begin{array}{cc}
-L_{1} \sin \varphi_{1} & L_{4} \sin \varphi_{2} \\
L_{1} \cos \varphi_{1} & -L_{4} \cos \varphi_{2}
\end{array}\right]
$$

# 4.2. Dynamic model of PLS and its controller 

The dynamic model of the PLS without friction parameters has been reported in Rivin (1987), Spong and Vidyasagar (2008), Sciavicco and Siciliano (2000), which can be written as,

$$
\begin{aligned}
& d_{11} \ddot{\varphi}_{1}+d_{12} \ddot{\varphi}_{2}+\left(m_{3} L_{2} l_{c 3}-m_{4} L_{1} l_{c 4}\right) \sin \left(\varphi_{2}-\varphi_{1}\right) \dot{\varphi}_{2}^{2}+\phi_{1}\left(\varphi_{1}\right)=\tau_{1} \\
& d_{21} \ddot{\varphi}_{1}+d_{22} \ddot{\varphi}_{2}-\left(m_{3} L_{2} l_{c 3}-m_{4} L_{1} l_{c 4}\right) \sin \left(\varphi_{2}-\varphi_{1}\right) \dot{\varphi}_{1}^{2}+\phi_{2}\left(\varphi_{2}\right)=\tau_{2}
\end{aligned}
$$

with,

$$
\begin{aligned}
d_{11} & =m_{1} l_{c 1}^{2}+m_{3} l_{c 3}^{2}+m_{4} L_{1}^{2}+I_{1}+I_{3} \\
d_{12} & =d_{21}=\left(m_{3} L_{2} l_{c 3}-m_{4} L_{1} l_{c 4}\right) \cos \left(\varphi_{2}-\varphi_{1}\right) \\
d_{22} & =m_{2} l_{c 2}^{2}+m_{3} L_{2}^{2}+m_{4} l_{c 4}^{2}+I_{2}+I_{4} \\
\phi_{1}\left(\varphi_{1}\right) & =g \cos \varphi_{1}\left(m_{1} l_{c 1}+m_{3} l_{c 3}+m_{4} L_{1}\right) \\
\phi_{2}\left(\varphi_{2}\right) & =g \cos \varphi_{2}\left(m_{2} l_{c 2}+m_{3} L_{2}+m_{4} l_{c 4}\right)
\end{aligned}
$$

where, $\mathbf{q}=\left[\varphi_{1} \varphi_{2}\right]^{T}$ is the vector of generalized coordinates, $\tau_{1}$ and $\tau_{2}$ are the input torques, $m_{1}, m_{2}$, $m_{3}, m_{4}$ are the masses of each of the links of the mechanism, $I_{1}, I_{2}, I_{3}, I_{4}$ are the moments of inertia at the center of mass of each of the links, and $g$ is the acceleration of gravity. And the other parameters have been described above.

If the next terms of mathematical model,

$$
m_{3} L_{2} l_{c 3}=m_{4} L_{1} l_{c 4}
$$

the inertial matrix is diagonal and constant. If this condition is satisfied, the dynamic model of the manipulator can be simplified and this is given by a set of decoupled equations without centrifugal terms as the next form,

$$
\begin{aligned}
d_{11} \ddot{\varphi}_{1}+\phi_{1}\left(\varphi_{1}\right) & =\tau_{1} \\
d_{22} \ddot{\varphi}_{2}+\phi_{2}\left(\varphi_{2}\right) & =\tau_{2}
\end{aligned}
$$

Due to these considerations, the parallelogram linkage system has been adopted by industrial robots and can be considered very popular in this context. In fact, the angles $\varphi_{1} y \varphi_{2}$ can be adjusted in independent form. Considering that the gravity terms of the dynamic model have been eliminated in mechanical way by means of a force-balancing, it is possible to use a proportional-derivative (PD) controller, considering not exist applied loads to mechanism and it is friction free. On the other hand, if the gravity terms are not eliminated, a PID controller can be considered which can be implemented for minimizing the steady state error that is generated by these terms.

In this case study is considered a classic PID controller for each input torque, for the motion control of mechanism, given by,

$$
\begin{aligned}
u_{i}(t) & =k_{i}^{p} e_{i}(t)+k_{i}^{I} \int_{0}^{t} e_{i}(\tau) d \tau+k_{i}^{D} \dot{e}_{i}(t) ; \quad i=1,2 \\
e_{i}(t) & =\varphi_{i}^{*}-\varphi_{i}
\end{aligned}
$$

where, $u_{i}(t)$ with $i=1,2$, are the input torque, $\tau_{1}$ and $\tau_{2}$, respectively; $e_{i}(t)$ and $\dot{e}_{i}(t)$ with $i=1,2$, are the position and velocity errors of the link 1 and link 2 (desired $\varphi_{i}^{*}$ and actual $\varphi_{i}$ ); $k_{i}^{p}, k_{i}^{I}$ and $k_{i}^{D}$, are the controller gains, proportional, integral, and derivative, respectively. In Qu and Dorsey (1991), Cervantes and Alvarez-Ramirez (2001) can see proof of stability of PID controllers for trajectory tracking of robot manipulators, and have been widely applied in industrial robots.

# 5. Optimization problem 

As it has been mentioned before, the design process for both the geometric and controller parameters ought to be performed in a simultaneously way. Thus, the design process can be expressed as an optimization problem as follows:

### 5.1. Problem definition

The design variables vector $\mathbf{X} \in \mathbb{R}^{22}$ is given by,

$$
\mathbf{X}=\left[m_{i}, L_{i}, l_{i i}, I_{i}, k_{1}^{p}, k_{2}^{p}, k_{1}^{I}, k_{2}^{I}, k_{1}^{D}, k_{2}^{D}\right]^{T} ; \quad i=1,2,3,4
$$

This variables are kinematic and dynamic parameters of the parallelogram linkage, and the controller gains. Table 1 shown the values of the parameters of the parallelogram linkage that were employed by practical issues of academic type.

The following constraints are considered:

$$
\begin{aligned}
L_{i, \min } & \leq L_{i} \leq L_{i, \max } \\
L_{1} & =L_{3} \\
m_{3} L_{2} l_{c 3} & =m_{4} L_{1} l_{c 4}
\end{aligned}
$$

The first three are the search limits, hence we only draw random values inside such limits. The last one is a model simplification considered in the simulation.

The objective function is the following:

$$
\begin{aligned}
\max f\left(m, L, l_{c}, I, k\right)= & W-\left[\lambda\left(E\left(\left|\tau_{1}, k\right|\right)+E\left(\left|\tau_{2}, k\right|\right)\right)\right. \\
& \left.+E\left(\left|\int e_{1}(t) d t\right|\right)+E\left(\left|\int e_{2}(t) d t\right|\right)\right]
\end{aligned}
$$

where $E(x)=1 / T \cdot \int_{0}^{T} x d t$. And $\lambda=1 / 10$ is a scaling factor. $W=50$ is a translation parameter. Notice that the BUMDA is a maximization algorithm, hence the function to minimize is multiplied by -1 and translated in order to a turn it into a maximization problem with an objective function that only returns positive values.

### 5.2. Discussion about the optimization process

The kind of algorithm used in this paper is also known as blackbox optimization. This kind of algorithms do not require information about a mathematical expression of the objective function. They only used an evaluator (or blackbox) from which they obtain evaluations of candidate solutions. The advantages are that a simulator, or numerical solver can be an evaluator (also a physical experimental test). Blackbox

Table 1. Kinematic and dynamic parameters of the parallelogram linkage system.
optimization algorithms do not assume convexity or derivability of the objective function. Notice that proving convexity of such function is not straight forward Eq. (15), numerically the objective function seems not to be convex neither derivable in the whole domain, for example, consider a mechanism with unconnected elements, such candidate solutions could be sampled by the BUMDA, such mechanism represents a discontinuity of the objective function. In such case, we assign a very low value to the objective function. Hence, classical optimization algorithms such as gradient based ones, can not be applied in this case. Equation (15) minimizes the power $\left(\tau_{1}\right.$ and $\left.\tau_{2}\right)$ used for manipulating the mechanism (which is related with the proportional, integral, and derivative errors), as well as the integral of the error in the simulation interval.

The $\lambda$ value is set to scale the $\tau$ term with the integral error term. It was set after revising numerical experiments. Notice that the objective function is basically composed of two terms: the $\tau_{i}$ term and the error term. As $\lambda$ is introduced to scale the terms. Notice that only one scaling factor is needed, for example, consider the maximization problem as: $\max C_{0}-\left(C_{1}(\tau \text { term })+C_{2}(\text { error term })\right)$, it has the same maximum than $\max C_{0} / C_{2}-\left(C_{1} / C_{2}(\tau \text { term })+(\text { error term })\right)$. In our problem $C_{0} / C_{2}=50$ and $C_{1} / C_{2}=\lambda$.

When a mechanism presents any singularity, or the system of equations can not be numerically solved, it is set to 0 (a low value), such solutions are automatically disregarded by the truncation procedure of the BUMDA.

# 6. Results 

In this section we test three different paths in order to show the robustness of the algorithm. The paths are listed in Table 2. The simulation time in the optimization process is of 20 sec and the step size for the

Table 2. Paths considered for testing the proposal.
![img-2.jpeg](img-2.jpeg)

Figure 5. Circle path: Desired $\varphi_{i d}$ versus computed $\varphi_{i}$, angular error $\varphi_{i d}-\varphi_{i}$, torque $\tau_{1}, \tau_{2}$.

![img-3.jpeg](img-3.jpeg)

Figure 6. Circle path: Desired versus computed path, end effector.
![img-4.jpeg](img-4.jpeg)

Figure 7. Path of a three petal flower: Desired $\varphi_{i d}$ versus computed $\varphi_{i}$, angular error $\varphi_{i d}-\varphi_{i}$, torque $\tau_{1}, \tau_{2}$.

Runge-Kutta method is of 0.001 sec . The optimization algorithm uses a sample size of 73 . The stopping criterion is when the sum of the standard deviations of all variables reaches a value less than $1.0 \times E^{-4}$. In the optimization process all the variables were considered in the interval $[0,1]$, then the values are mapped to the corresponding intervals simply by scaling and translating them. The execution of the algorithm is about $1 \mathrm{~min} 56 \mathrm{sec}$. In a personal computer with Intel $i 7$ processor and 8 GB of RAM, using OpenSuse Linux and GNU compiler (GCC) and C program. The number of evaluations of the objective function in a typical program execution is about 6745 .

In Figs. 5, 6, 7, 8, 9, and 10 shows the error of $\varphi_{1}$ and $\varphi_{2}$, the $\tau_{1}$ and $\tau_{2}$ values, and desired path versus the delivered by the BUMDA, for a circle path, a three petal flower and snail Pascal, respectively.

# 6.1. Improvement of the initial design 

In Fig. 11(a) we can observe the evolution of the best and worst solution as well as the mean of the objective value per iteration of the BUMDA. Hence, it shows the improvement of the solutions thought

![img-5.jpeg](img-5.jpeg)

Figure 8. Path of a three petal flower: Desired versus computed path, end effector.
![img-6.jpeg](img-6.jpeg)

Figure 9. Snail Pascal path: Desired $\varphi_{i d}$ versus computed $\varphi_{i}$, angular error $\varphi_{i d}-\varphi_{i}$, torque $\tau_{1}, \tau_{2}$.
the iterations. In Fig. 11(b) we can observe the improvement for the last iterations. We divide in this two phases the algorithm behavior, because in the first iterations BUMDA finds an approximation of the global solutions, it is to say, it explores the whole search space, in the second phase the solutions is almost the final design but it refines the design, even though the improvement can be consider marginal, it shows the capacity of the algorithm to evolve solutions with a high precision, the figures were computed using Circle Path, but a similar behavior is presented by the other.

Table 3 shows the best solutions known at the first iteration of the BUMDA, and at the end of the optimization process, notice that nevertheless the objective function is not quite different, the initial and final design is completely different.

![img-7.jpeg](img-7.jpeg)

Figure 10. Snail Pascal path: Desired versus computed path, end effector.
![img-8.jpeg](img-8.jpeg)

Figure 11. (a) Evolution of the design in the first 20 iterations. Notice that a significant improvement is achieved in this phase. (b) Improvement of the design for the last iterations. Notice that the design can be refined with a high precision.

Table 3. Initial and final designs for a typical run, for each of the paths. The values are taken as the best solution known in the first generation and the best solution at the end of the optimization process.

# 7. Conclusion 

In this proposal, a structure-control design for a parallelogram linkage robot with trajectory tracking is presented. This is formulated as a concurrent process where both the kinematic and the dynamic models of the mechanical structure and the controller gains are considered for optimizing in a simultaneously way. An estimation of distribution algorithm was adopted for solving the optimization problem. This

algorithm successfully found well performed solutions. One of the most remarkable characteristics of this algorithm is that practically it uses a unique parameter: the sample size, because the stopping criterion is set according to the maximum allowed numerical error, which is a problem parameter. The sample size is quite small for this kind of algorithms.

The BUMDA performs quite well and we expect to tackle similar problems with this algorithm. The BUMDA samples the whole search space using an approximation of the Boltzmann distribution, in such distribution the probability of sampling the global optimum is the maximum. Hence, we look for the global optimum, and it is quite possible that we find a near approximation, and on the other hand, when the algorithm converges, this approximation is refined by locally sampling in a small neighborhood. Notice that the BUMDA uses a Gaussian model, which is a soft distribution, when this Gaussian model has a standard deviation less than $\epsilon$, most of the samples from it will be in a radius of $3 \epsilon$ from the mean, hence if $\epsilon$ is a small number the Gaussian distribution provides a way of looking for solutions in a close neighborhood, even this is not a prove of local optimality, it is a strong argument about our procedure, which samples intensively the neighborhood of the best solution when the algorithm converges. In consequence we have a strong argument to say that very possibly the solutions delivered by the BUMDA are local optima. On the other hand, when the algorithm is not in the convergence phase (when it has a large variance) it is performing a global exploration. Then it is possible that BUMDA finds the global optimum, but it is highly possible that at least it provides a local optimum.

The experiments are developed using different kinds of paths of the parallelogram linkage robot, in all cases the algorithm is capable of solving satisfactorily all the cases. It can be observed that structural and controller parameters of the mechanism fulfill desired motions. In a subsequent work, other parallel mechanisms will be studied, even those with more complex architecture where optimization parameters are uncorrelated, in order to test the performance of the concurrent optimization methodology.
