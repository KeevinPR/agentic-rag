# Design optimization of a cable-based parallel tracking system by using evolutionary algorithms Eusebio E. Hernandez $\dagger$, S.-I. Valdez $\ddagger$, M. Ceccarelli $\S$, A. Hernandez $\ddagger$ and S. Botello $\ddagger$ 

$\dagger$ National Polytechnic Institute, ESIME-UPT, Section of Graduate Studies and Research, Mexico City, Mexico<br>$\ddagger$ Center for Research in Mathematics (CIMAT), Department of Computer Science, Guanajuato City, Mexico<br>§Laboratory of Robotics and Mechatronics, University of Cassino, Cassino (Fr), Italy

(Accepted February 2, 2014. First published online: March 5, 2014)

## SUMMARY

In this paper, an optimization design of a 6 DOF parallel measuring system is analyzed. First, a closed form direct kinematics formulation based on Cayley-Menger determinants is considered in the objective function, in order to measure the manipulator singularities, then an estimation of distribution algorithm is proposed to solve the optimization problem. It is shown that the evolutionary algorithm can find close to optimal solutions for minimum pose error estimation. Additionally, these global optimizers significantly reduce the computational burden in comparison with exhaustive search and other global optimization techniques. The sensitivity of the pose error estimation in the prescribed robots' workspace is analyzed and used to guide a designer in choosing the best structural configuration. Numerical examples are discussed to show the feasibility of the proposed optimization methodology.

KEYWORDS: Robotics; Parallel mechanism design; Tracking system; Optimization; Estimation of distribution algorithms.

## 1. Introduction

Calibration of robotic systems requires to measure the pose (position and orientation) of endeffectors for the purpose of compensating parameter errors and improving accuracy. Several measuring systems have been used to determine the pose of movable rigid bodies often by means of expensive measurement devices such as laser tracking systems, ${ }^{9}$ vision-based measure devices, ${ }^{22,23}$ or redundant systems. ${ }^{10}$ Nevertheless, often measuring systems cannot measure position and orientation simultaneously or have limited accuracy. ${ }^{7}$ The option of cable-based measuring systems is a feasible and cheap alternative for the identification of kinematic parameters on robotic systems. In fact, these systems can be a good compromise between expected accuracy and low cost. Some works have been focused on this type of architecture and parallel cable mechanisms have been presented for pose measuring purposes. ${ }^{14}$ At LARM (Laboratory of Robotics and Mechatronics) in Cassino, a cable-based measuring system has been studied and designed since late 90s. It is named as CaTraSys (Catrasys Tracking System) and has been used to evaluate the serial robot workspace. ${ }^{19}$ In addition, a characterization of singularities and error analysis have been presented for this system. ${ }^{8,17}$ Based on the design of CaTraSys, a measuring system has been developed at LARM for fine calibration. ${ }^{6,13}$ This system, shown in Fig. 1, has been named as Milli-CaTraSys. It is a cable-based tracking system capable of measuring displacements and orientation variations of complex movable multibody systems.

[^0]
[^0]:    * Corresponding author. E-mail: euhernandezm@ipn.mx

![img-0.jpeg](img-0.jpeg)

Fig. 1. A prototype built at LARM in Cassino.

Another advantage of using this measuring system consists in the possibility of applying a known wrench and measuring its effect on the end-effector of multibody robotic systems. One can simultaneously measure the linear and angular compliant displacements. Since known masses can be applied to the free ends of its cables, the system can be used for analyzing stiffness features as described in refs. [5, 13]. Thus, an experimental evaluation procedure of stiffness performance can consist in measuring the compliant displacements due to known external wrench. In addition, the measurement of a set of small angular compliant displacements can be very complex to achieve through commercially available sensors. Many applications in robotics, construction, and manufacturing require effective real-time measurement of Cartesian pose of end-effectors, tools, and materials. In this form, similar cable-based measuring systems have been used for identification of human walking characteristics ${ }^{15,18}$ or for assisting measurement in potential sculpture surfaces. ${ }^{30}$

In this work, a kinematic design optimization of a 6 DOF cable-based parallel tracking system for minimum pose error estimation is analyzed. We intend to find the position on the base for six cables in order to reduce singularities, maintaining a large determinant (which is related with the volume of the tetrahedral shaped by the cables), additionally, we intend to maintain a similar volume during the whole trajectory, in order to perform a soft trajectory, it means without abrupt changes on the cables. Finally, our objective function also considers that the cables must be as farthest as possible from each other in the base platform.

The forward kinematics of the device in terms of Cayley-Menger determinants is used to measure singularities and subsequent pose errors of the end-effector. An estimation of distribution algorithm is developed and tested to solve the optimization problem. It is shown that the evolutionary algorithm can find close to optimal solutions with minimum pose error estimation.

In recent years, evolutionary algorithms have been considered for addressing optimization problems, as well as in robotics area. For example, genetic algorithms have been used to optimal planning of experiments for calibration problem in serial robots, ${ }^{33}$ or addressing an optimal control of parallel manipulators. ${ }^{16}$ In addition, a hybrid method based on a genetic algorithm has been implemented to solve the direct kinematics of the Stewart platform, by finding all real solutions. ${ }^{24}$ The optimized design of parallel mechanisms have been also studied by using differential evolution ${ }^{3}$ or neuro-genetic algorithms. ${ }^{1}$

The paper is organized as follows. Section 2 presents the system architecture and operation modes. In Section 3, the kinematics is analyzed in terms of Cayley-Menger determinants. The optimization problem is formulated in Section 4 and solved by using an Estimation of Distribution Algorithm (EDA) in Section 5. In Section 6, results and a sensitivity analysis are presented, and finally, conclusions are drawn in Section 7.

# 2. System Architecture 

Milli-CaTraSys can be considered as a Gough-Stewart parallel manipulator with 3-2-1 configuration. It consists of two rigid body platforms that are linked through six cables of variable lengths. Namely,

![img-1.jpeg](img-1.jpeg)

Fig. 2. A 3D scheme with reference frame.
the two rigid bodies are a base platform, and a moving platform that can be considered as endeffector, as shown in Figs. 1 and 2. By using Milli-CaTraSys, it is possible to evaluate the linear and angular compliant displacements occurring to a reference frame that is attached to the end-effector by measuring only linear distances of the cables. These linear distances are the lengths of cables that are measured by means of six LVDT transducers. Figure 2 shows the location of LVDT transducers on the fixed Milli-CaTraSys platform and the masses $m_{i}(i=1, \ldots, 6)$ that are applied on the free ends of the six cables, in order to guarantee that all cables are always pulling (in tension). Two types of LVDT sensors have been tested to be implemented on Milli-Catrasys prototype. The first type of LVDT sensors has a full scale measuring range of 200 mm and an accuracy of $0.25 \%$ of the full scale. The Milli-CaTraSys prototype can have an overall accuracy of 0.5 mm and $9.5 \mathrm{e}-3$ rad when equipped with this type of sensors. The second type of LVDT sensors has a full scale measuring range of 5 mm and an accuracy of $0.25 \%$ of the full scale. The system can have an overall accuracy of 0.01 mm and $1 \mathrm{e}-5 \mathrm{rad}$ when equipped with this type of sensors. It is worth noting that the measuring error can be considered as negligible when the distance from the base plane is large. The data acquisition and the signal conditioning for the six transducers are implemented through a NI DAQ Acquisition board PCI 6024, six LVDT transducers (with proper power supply and amplifiers) and a virtual instrument in LabVIEW environment. ${ }^{19}$ This virtual instrument has been developed to measure the data from the amplifiers of the LVDT transducers. In general, it consists of six channels to make the acquisition of analogical inputs and a filter stage for the six signals. Then, data are stored in a suitable data file. Applications of this measurement device include evaluation workspace and parameters identification of multibody robotic systems. Milli-CaTraSys has been already successfully used for evaluation of workspace. ${ }^{6}$ Moreover, Milli-CaTraSys can be used to apply a known wrench on the end-effector of a robotic system. Since known masses can be applied to the free ends of its cables, one can use Milli-CaTraSys for analyzing stiffness features of robotic systems too. ${ }^{5}$

# 3. Kinematics and Error in Pose Estimation 

Considering the scheme that is shown in Fig. 3, $B_{i}\left(B_{i x}, B_{i y}, 0\right)$ (with $i=1,6$ ) represent the vectors joining the origin with the points $B_{i}$, which are the sources of the cable lengths on the fixed base platform. The origin of the reference frame could be posed in any place on the base platform. In our calculations, we posed it in a corner as it is shown in Fig. 2. Similarly, $P i\left(P_{i x}, P_{i y}, P_{i z}\right)$ (with $i=1,2,3$ ) represent the vectors joining the origin with $P_{i}$ points, which are the attaching points of the cables on the end-effector. The centroid point on the Milli-CaTraSys end-effector is identified as $C(C x, C y, C z)$.

The inverse kinematic model expresses the relationship between the cable lengths and the pose. Indeed, when the pose of the end-effector is given, the solution of the inverse kinematic problem gives the cable lengths in the form:

$$
l_{i}=\operatorname{dist}\left(\mathbf{B}_{\mathbf{i}}, \mathbf{P}_{\mathbf{i}}\right), \quad \mathbf{i}=\mathbf{1}, \mathbf{2}, \mathbf{3}
$$

![img-2.jpeg](img-2.jpeg)

Fig. 3. A set of three trilateration operations for the direct kinematic model of the parallel tracking system. Given a set of six cable lengths, there are three tetrahedrons and two possible solutions for the location of $P_{1}$, $P_{2}$, and $P_{3}$ points.

Where $\operatorname{dist}(\cdot)$ is the distance. The problem of finding the Cartesian position and orientation of the movil platform associated with given cable lengths is discussed as follows. The position of $P_{1}$ on the robot end-effector can be defined as the position of the point at which three arcs intersect. These arcs are defined by three spheres equations.

The direct kinematics of the 3-2-1 configuration can be solved by three consecutive trilateration operations, as shown in Fig. 3. Using Eq. (1) the coordinates of $P_{1}$ can be obtained by referring to a tetrahedron with known edge lengths $l_{1}, l_{3}$, and $l_{5}$. Thus, the solution of Eq. (1) provides two mirror coordinates of $P_{i}$. However, the suitable solution can be chosen as the positive one. Then, the coordinates of $P_{2}$ can be obtained by referring to a second tetrahedron that is defined by referring the cable lengths $l_{4}, l_{2}$ and the known distance from $P_{1}$ to $P_{2}$. Finally, a third tetrahedron is defined by referring the cable length $l_{6}$ and the known distances $P_{1}$ to $P_{3}$ and $P_{2}$ to $P_{3}$. Once points $P_{1}, P_{2}$, and $P_{3}$ have been located, they can be used to compute the pose of the end-effector of Milli-CaTraSys as given by the coordinates of $C$ and, three orientation angles $\alpha, \beta$, and $\varphi$. Note that this completely solves the direct kinematics of the 3-2-1 configuration.

For Milli-CaTraSys, the above-mentioned direct kinematics procedure can be solved by implementing the formulation in ref. [27].

This formulation uses the concept of Cayley-Menger bideterminants and gives a closed-form solution to this problem. The performance of a 3-2-1 tracking system can be also analyzed in terms of these determinants.

The Cayley-Menger bideterminant $D$ of two sequences of points $\left[p 1, p 2, \ldots, p_{n}\right]$ and $\left[q_{1}, q_{2}, \ldots, q_{n}\right]$ is defined as ref. [26]:

$$
D\left(\bar{p}_{1}, \ldots, \bar{p}_{n} ; \bar{q}_{1}, \ldots, \bar{q}_{n}\right)=2\left(\frac{-1}{2}\right)^{n} \cdot\left|\begin{array}{cccc}
0 & 1 & 1 & 1 & 1 \\
1 & \hat{D}\left(\bar{p}_{1}, \bar{q}_{1}\right) & \hat{D}\left(\bar{p}_{1}, \bar{q}_{2}\right) & \cdots & \hat{D}\left(\bar{p}_{1}, \bar{q}_{n}\right) \\
1 & \hat{D}\left(\bar{p}_{2}, \bar{q}_{1}\right) & \hat{D}\left(\bar{p}_{2}, \bar{q}_{2}\right) & \cdots & \hat{D}\left(\bar{p}_{2}, \bar{q}_{n}\right) \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \hat{D}\left(\bar{p}_{n}, \bar{q}_{1}\right) & \hat{D}\left(\bar{p}_{n}, \bar{q}_{2}\right) & \cdots & \hat{D}\left(\bar{p}_{n}, \bar{q}_{n}\right)
\end{array}\right|
$$

where $\hat{D}\left(\bar{p}_{i}, \bar{q}_{j}\right)$ denotes the squared distance between the points $\bar{p}_{i}, \bar{q}_{j}$. When the sequences of points are the same, it is to say $D\left(\bar{p}_{1}, \ldots, \bar{p}_{n} ; \bar{p}_{1}, \ldots, \bar{p}_{n}\right)$, we use the notation $D\left(\bar{p}_{1}, \ldots, \bar{p}_{n}\right)$. It can be shown that $D\left(\bar{p}_{1}, 3, \bar{p}_{n}\right)$ is $((n-1)!)^{2}$ times the squared hypervolume of the simplex spanned by the points $\bar{p}_{1}, \ldots, \bar{p}_{n}$.

Thus, given three points in space, $\bar{p}_{1}, \bar{p}_{2}$, and $\bar{p}_{3}$, the trilateration problem can be solved by finding the location of another point, $\bar{p}_{4}$, where the distance from it to these points is known. According to this formulation, ${ }^{27,28}$ the point $\bar{p}_{4}$ can be expressed as

$$
\bar{p}_{4}=\bar{p}_{1}+C_{1}\left(-C_{2} \bar{v}_{1}+C_{3} \bar{v}_{2} \pm \sqrt{C_{4}}\left(\bar{v}_{1} \times \bar{v}_{2}\right)\right)
$$

where $\bar{v}_{1}=\bar{p}_{2}-\bar{p}_{1}$ and $\bar{v}_{2}=\bar{p}_{3}-\bar{p}_{1}$, the $\pm$ sign gives two mirror symmetric coordinates for $\bar{p}_{4}$ point, and

$$
\begin{gathered}
C_{1}=\frac{1}{D\left(\bar{p}_{1}, \bar{p}_{2}, \bar{p}_{3}\right)}=\frac{1}{\left\|\bar{v}_{1}-\bar{v}_{2}\right\|} \\
C_{2}=D\left(\bar{p}_{1}, \bar{p}_{2}, \bar{p}_{3} ; \bar{p}_{1}, \bar{p}_{3}, \bar{p}_{4}\right)=\left[\left(\bar{p}_{1}-\bar{p}_{3}\right) \times\left(\bar{p}_{2}-\bar{p}_{3}\right)\right] \cdot\left[\left(\bar{p}_{1}-\bar{p}_{4}\right) \times\left(\bar{p}_{3}-\bar{p}_{4}\right)\right] \\
C_{3}=D\left(\bar{p}_{1}, \bar{p}_{2}, \bar{p}_{3} ; \bar{p}_{1}, \bar{p}_{2}, \bar{p}_{4}\right)=\left[\left(\bar{p}_{1}-\bar{p}_{3}\right) \times\left(\bar{p}_{2}-\bar{p}_{3}\right)\right] \cdot\left[\left(\bar{p}_{1}-\bar{p}_{2}\right) \times\left(\bar{p}_{2}-\bar{p}_{4}\right)\right] \\
C_{4}=D\left(\bar{p}_{1}, \bar{p}_{2}, \bar{p}_{4}\right)
\end{gathered}
$$

The formulation is not expressed according to a specific coordinate frame and it is coordinate-free. Moreover, the main advantage of this formulation is that all the involved terms are determinants with geometric meaning, representing side areas or volumes of tetrahedrons. In this form, effects caused by error pose estimation and singularities can be investigated in a straight way. It has been reported ${ }^{26}$ that there are certain singular sets of cable lengths in which the number of solutions are not two, for at least one of the three trilateration operations. In fact, the moving platform is in a singular configuration in which at least one of the following equations is satisfied:

$$
D\left(B_{1}, B_{3}, B_{5}, P_{1}\right)=0, D\left(B_{2}, B_{4}, P_{1}, P_{2}\right)=0, \text { or } D\left(B_{6}, P_{1}, P_{2}, P_{3}\right)=0
$$

These conditions characterize all singularities for the three trilateration operations in Fig. 3. During normal operation, it is desirable that the tracking system works in a region without singularities. Indeed, near a singularity, small errors in the cable lengths induce important errors in the pose estimations, i.e., noise amplification occurs near a singularity not only for their variances but also in their biases. In addition, the bias error becomes relevant as the moving platform approaches the base plane. ${ }^{13,27}$

Thus, the forward kinematics of the tracking system can be performed in terms of CayleyMenger determinants to measure singularities and subsequent pose errors of the end-effector. With this formulation, a design optimization problem can be proposed to find a set of device parameters for a given path, that satisfy user requirements and returns adequate coordinates for the base. The optimization procedure is explained in the next section.

# 4. Optimization 

The optimization problem of the system can be defined as: to find the position of the cables sources in the base which maximizes the determinant of the system during the complete trajectory (a given path), and avoiding as possible cable intersections.

In order to tackle the problem as stated above, we use an Estimation of Distribution Algorithm, ${ }^{32}$ this kind of algorithm intends to find an optimum by estimating and sampling from a probability distribution. They are used when the objective function is not explicitly defined, is not derivable, or have multiple maxima/minima. Any or all of the characteristics mentioned above is a reason to use a population-based optimizer. In the particular case of highly correlated variables, there is evidence about the effectiveness of Estimation of Distribution Algorithms. ${ }^{20,21}$ In this case, we expect that the variables be highly correlated, because they are the positions of the cables, then all together impact in the system precision.

### 4.1. Objective function

The objective function is stated as follows:

$$
\max f\left(d e t, D_{\min }\right)=\left(\frac{\mu_{d e t}}{s d_{d e t}+1}\right)\left(\prod_{j=1}^{6} D_{\min , j}\right)-\sum_{i=1}^{n_{d e t}} I_{i} \exp \left(\frac{1}{0.001+d e t_{i}}\right)
$$

where $d e t_{i}$ is the determinant in the $i$ position, and $D_{\min , j}$ is the distance of the $j$ point in the base to the closest point different than itself. By maintaining a separation as greater as possible among the cables we intend to avoid cable intersections, this is the purpose of $D_{\min , j}$ product. $\mu_{d e t}$ is the average of the determinant considering all the positions, and $s d_{d e t}$ the standard deviation. $I_{i}$ is an indicator function it is 1 if $d e t_{i}<1$ and 0 otherwise.

Note how the different components of the function consider the optimization goal, first the average, in the first term of the equation is maximized, as it is divided by the standard deviation, then we are asking for points that are not collapsed in the based. The product in the second parenthesis considers the distances among each point and its closest neighbor, if a point is very close to another, then this product reduces the function value. This is another criterion, together with the standard deviation, which is used to maintain sparse points in the base. The second term is only used when a determinant in any position is too small, then it is penalized exponentially.

The pure condition ${ }^{12}$ measures the singularities as well as our objective function, both are related with the volume of the tetrahedral formed by a set of points. An advantage of our objective function is that it measures the singularities in the first term, additionally intends to maximize the determinants during the whole trajectory by maximizing the mean, and maintaining a similar determinant for each point in the trajectory, hence we do not expect abrupt changes of the cable positions during the trajectory. Finally, our objective function penalizes determinants smaller than 1 , which means that we do not allow negative or near to 0 determinants, a negative determinant implies that a plane of the tetrahedral passes through another (a possible intersection of cables), and a determinant close to 0 is a singularity as mentioned. We could use the pure condition as objective function, we consider that the pure condition does not contribute with additional information and lacks of the extra information that is already in our objective function.

## 5. Estimation of Distribution Algorithm-based Approach

An Estimation of Distribution Algorithm is an optimization method based on estimating and sampling a probability distribution. Usually, it starts with a random population sampled from a uniform distribution defined on a search space, then a subset of the best solutions is selected in order to be used for estimating a new probability distribution. The new distribution is sampled, and the sample replaces the old population, and so on. Usually a subset of the best solutions is preserved from one generation to the next one, in order to ensure convergence and to get a better bias. The aim is that the EDA, eventually, samples the optimum.

The EDAs have shown an excellent capacity for finding and using correlations among variables, ${ }^{20,21}$ which is a desirable property when the optimization process involves interconnected elements of a system. On the other hand, various studies suggest that EDAs suffer from premature convergence, it

Table I. Normal multivariate EDA based on the potential selection.

# Problem parameters: 

1
$x_{\text {inf }}, x_{\text {sup }}$ vectors of inferior and superior limits respectively.
2
$\epsilon_{\text {tol }}$ Minimum covariance matrix norm, for stopping criterion.
3
$n_{\text {var }}$ Number of variables
User given parameters:
$4 \quad N$ Population size
$5 \quad X \leftarrow \operatorname{uniform}\left(N, x_{\text {inf }}, x_{\text {sup }}\right)$
$6 \quad F \leftarrow$ evaluation $(X)$
Truncation selection according Algorithm 5.
$7 \quad I^{S} \leftarrow$ selection $(F)$
Potential of the selected set, Eq. (10).
$8 \quad p\left[I^{S}\right] \leftarrow$ potential $\left(F\left[I^{S}\right]\right)$
$9 \quad \mu \leftarrow x_{\text {best }}$
Covariance matrix computation
10 For $i=1 . n_{\text {var }}$
$11 \quad$ For $j=1 . n_{\text {var }}$

$$
\Sigma_{i, j}=\frac{\sum_{k \in I^{s}}\left(x_{k, i}-\mu_{i}\right)\left(x_{k, j}-\mu_{j}\right) p_{k}}{\sum_{k \in I^{s}} p_{k}}
$$

13 While $|\Sigma|>\epsilon_{\text {tol }}$
$14 \quad X \leftarrow \operatorname{Normal}\left(N, \Sigma, \mu, x_{\text {inf }}, x_{\text {sup }}\right)$
$15 \quad F \leftarrow$ evaluation $(X)$
$16 \quad I^{S} \leftarrow$ selection $(F)$
17 Potential of the selected set, Eq. 10.
$18 \quad p\left[I^{S}\right] \leftarrow$ potential $\left(F\left[I^{S}\right]\right)$
$19 \quad \mu \leftarrow x_{\text {best }}$
20 For $i=1 . n_{\text {var }}$
21 For $j=1 . n_{\text {var }}$

$$
\Sigma_{i, j}=\frac{\sum_{k \in I^{s}}\left(x_{k, i}-\mu_{i}\right)\left(x_{k, j}-\mu_{j}\right) p_{k}}{\sum_{k \in I^{s}} p_{k}}
$$

Output
23
$x_{\text {best }}$ Best optimum approximation.
is to say that the population collapses in a single point before the search space has been adequately explored. ${ }^{2,4,25,31}$ In this approach, we use an EDA based in a Gaussian distribution as most of the EDAs for continuous spaces. ${ }^{11}$ The EDA uses the so-called Potential Selection, a kind of selection and weighting method that improves the exploration of the search space, preventing from premature convergence. The algorithm was proposed as a general optimization method ${ }^{29}$ and is presented in the algorithm of Table I.

In Table I, line 1 is the set of search limits, in this case the base platform limits. $\epsilon_{\text {tol }}$, in line 2, is an stopping criterion when the norm of the covariance matrix of the normal distribution used for searching is too small, it means that the algorithm is not searching anymore, hence it is stopped. The $\epsilon_{\text {tol }}$ must be always smaller than the physical error desired. Line 3 is the number of parameters (12 in this case, for 6 positions in $x$ and $y$ coordinates). Line 4 is the unique user given parameter: the population size, usually the greater the population is the better the performance of the algorithm, but also the greater the computational effort needed to solve the problem. In step 5, the initial population is uniformly and randomly sampled in the search space, hence $X$ is a matrix of candidate solutions. In step 6, the candidate solutions are evaluated by means of Eq. (9). In step 7, a subset of the best solutions are selected by using the algorithm in Table II. In step 8, the potential value for each candidate solution in the selected set is computed by using Eq. (10). In step 9, the mean of the search distribution (the distribution used for sampling new candidate solutions) is computed. Steps 10-12 are the computation of the covariance matrix of the search distribution. Line 13 is the beginning of the main loop. The steps just mentioned are repeated, with the difference that the new candidate solutions $X$ are sampled from a Normal distribution instead of the uniform.

Table II. Truncation method to ensure increasing mean of the objective function and convergence to the elite individual. Maximization case.

# Input: 

$1 \quad F$ vector of objective function values of size $N$.
$2 \quad \theta^{i}$ a threshold.
$3 \quad \hat{I}^{S} \leftarrow \operatorname{sort}(F$, decreasing,return_index $)$.
$4 \quad \hat{I}^{S} \leftarrow \hat{I}_{1 /(N / 2)}^{S}$.
$5 \quad I^{S} \leftarrow \hat{I}_{i}^{S}$ for all $i \in \hat{I}^{S}$ such that $F_{I_{i}^{S}} \geq \theta^{i}$.
$6 \quad M \leftarrow \operatorname{sizeof}\left(I^{S}\right)$.
$7 \quad \theta^{i+1} \leftarrow I_{M}^{S}$.

## Output

$I^{S}$ vector of indexes of selected individuals of size $M$. $\theta^{i+1}$ threshold for the next selection.

The truncation method presented in Table 2 receives as input a vector of the objective function values $F$ a truncation threshold $\theta_{t}$, the threshold $\theta_{0}$ for the first call of the method is the worst objective value known, from the second to the last call it is returned by the same method. In step 3, the objective values are sorted and the indices of the sorting are stored, then the indices are truncated to the half in step 4 , from this last vector of indices we verify that all of them be greater or equal than the current threshold, if any of them is below the threshold then it is truncated from the vector. Then, we obtain the number $M$ of solutions which remain in the selected set, and update the threshold to the last individual (the worst) in the selected set. The selected set then is used in the algorithm in Table 1 for updating the search distribution. This method ensures convergence of the method and pushes the population to the best regions in the search space.

The potential equation is presented in Eq. (10), which is used in algorithm 1 in order to weight the most diverse solutions and to maintain an adequate exploration. It assigns a large weight to the most promising solution as well as to the most diverse solution, or solutions that are in the subset of the best ones but are the farthest from the best solution known.

$$
p\left(x_{i}\right)=\frac{\hat{p}\left(x_{i}\right)}{\sum_{i} \hat{p}\left(x_{i}\right)}, \quad \text { for } i \text { in the selected set. }
$$

Where:

$$
\begin{aligned}
& \hat{p}\left(x_{i}\right)=\max \left(p_{d}\left(x_{i}\right), p_{f}\left(x_{i}\right)\right), \quad p_{d}\left(x_{i}\right)=\frac{\hat{p}_{d}\left(x_{i}\right)-\min \left(\hat{p}_{d}\left(x_{i}\right)\right))}{\max \left(\hat{p}_{d}\left(x_{i}\right)\right)-\min \left(\hat{p}_{d}\left(x_{i}\right)\right)}, \\
& p_{f}\left(x_{i}\right)=\frac{f\left(x_{i}\right)-\min \left(f\left(x_{i}\right)\right)}{\max \left(f\left(x_{i}\right)\right)-\min \left(f\left(x_{i}\right)\right)}, \text { and } \hat{p}_{d}\left(x_{i}\right)=\sqrt{\sum_{j=1}^{n}\left(x_{i, j}-x_{\text {best }, j}\right)^{2}} .
\end{aligned}
$$

$f\left(x_{i}\right)$ is the objective function of the individual $x_{i}$, and $n$ the number of variables. The potential function in Eq. (10) returns the greatest value for the elite as well as for the farthest individual to the elite.
$\hat{p}_{d}\left(x_{i}\right)$ basically is the distance between the $i$ candidate solution to the best solution known, hence $p_{d}\left(x_{i}\right)$ is a normalized distance. $p_{f}\left(x_{i}\right)$ is a normalized difference of the objective function of the candidate solution $i$ to the worst solution in the selected set. Thus, $\hat{p}\left(x_{i}\right)$ is the maximum between this two distances, and $p\left(x_{i}\right)$ has the same meaning but is also a probability, hence the farthest individuals to the best as well as the best individual have the maximum probability.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Results of the 30 best executions with the modified-final ranges. We plot the density of the best positions found, the greater the density the higher the number of solutions we found in that region. As explained in the text we reduce the search space in order to refine the optimum position approximation. These are plots are obtained from the final search in the reduced intervals mentioned in the text. The red rectangles are the regions in which most probably the actual optimum position is at the end of the search process.

# 6. Results 

The EDA used in this approach only needs two parameters: the population size, and an stopping criterion which can be a minimum norm of the variance in the search distribution or a number of generations. We perform 150 executions of the algorithm with the following parameters: 300 of population size, and 600 generations or a minimum variance norm of $1.0 e-22$.

Using this parameters we obtain the positions in Fig. 4. We plot the results of the best 30 executions, the color represents the approximate density of the best solutions, it is to say the greater value in the color bar the greater number of solutions are in such region. The red rectangles enclose the region where the best solutions are with the greatest probability, to compute these rectangles we apply the following procedure: we use the Boostrap methodology to compute confidence intervals for the best parameters at $99 \%$ of confidence. Then, we increase the interval by $20 \%$, if some value is out of the search interval we make it equal to the bound of the interval. Using this region where the best solution is, we execute 150 executions with the limits of the search space updated. The process is repeated until there is not a reduction in (all) the limits, that is three times in our calculations, then we found the regions where most probably is the adequate position, as it is shown in Fig. 4. The black asterisk in Fig. 4 represents the best solution found, which coordinates are

![img-4.jpeg](img-4.jpeg)

Fig. 5. Best solutions for a given path of the parallel tracking system (red) and original base coordinates (blue).

# Determinant for 100 points in a path 

![img-5.jpeg](img-5.jpeg)

Fig. 6. Determinant for the best solution found.
the following: $X=\{370.87979,258.65610,87.23333,499.96070,204.42310,131.88560\}$, and $Y=$ $\{-149.32958,-65.48691,-374.13420,-148.40912,-427.06850,-87.14045\}$. This solution is shown in Fig. 5, blue points on the base represent the original base coordinates of the parallel tracking system, meanwhile red points represent the best solution given by the optimization process. The objective function value for these coordinates is: 525434179749 . We have not found any singularity in the determinant computation for these coordinates.

Figure 6 shows the determinant measured for 100 points in a linear path, as can be seen in the figure, the differences between the average value (red line in the middle of the plot), and the other values is really small between $[-0.07452393,0.06140137]$ around the average. It means that actually our

optimization process is successful, because we found position coordinates with a high determinant for the whole path, additionally the determinant is almost the same for each point in the path.

# 7. Conclusions 

In this paper, the kinematic design of a cable-based parallel tracking system for minimum pose error estimation is analyzed. An evolutionary algorithm from the family of estimation of distribution algorithms is utilized to solve an optimization problem. In particular, an EDA formulation is developed and tested, by considering a formulation based on Cayley-Menger determinants for characterizing singularities. The EDA converged to close to optimal solutions that are characterized by multiple sets of optimal kinematic parameters. Moreover, the EDA provides a representative solution set of the parameters. The performance obtained shows that it is possible to find a set of coordinates for a given path that fulfills the designer criteria and returns adequate coordinates for the base, with high, uniform, and non-singular determinants.

Since an optimization algorithm draws several optimal solutions, a sensitivity analysis (computing confidence intervals) is performed in order to guide the robot designer to select the best structural configuration, the analysis reveals that some architectures might be preferred. The approach can be easily generalized and used in other global optimization problems.

## Acknowledgments

The authors would like to thank CONACYT and SIP-IPN for supporting part of this work through the research project grants CB-2011-01-169132, SIP20121377, and SIP20131372.
