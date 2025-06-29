# Automated Dimensional Synthesis of a Portable Sky Scanner for Measuring Light Pollution 

Alejandra Rios<br>IPN ESIME-Ticomán<br>Ciudad de México, México<br>arioss1000@alumno.ipn.mx

Eusebio E. Hernández<br>IPN ESIME-Ticomán<br>Ciudad de México, México<br>euhernandezm@ipn.mx

Hector Lamphar<br>CONACYT-CENTROGEO AC<br>Querétaro, México<br>hsolano@centrogeo.edu.mx<br>S. Ivvan Valdez<br>CONACYT-CENTROGEO AC<br>Querétaro, México<br>svaldez@centrogeo.edu.mx


#### Abstract

Light pollution is often measured by a photometric sensor network distributed in the area of interest. However, photometric sensors usually have a narrow view angle, making difficult to perform measurements at low elevation angles. Furthermore, short-term variations are not significant; hence, a low-cost solution is to displace a portable device, able to scan the sky in a range of azimuth and zenith angles, to different locations of interest. The device should be designed with the aim of characterizing the emission function from ground based light sources, which is decreasing in intensity with respect to the zenith. In this manuscript, we propose to find the dimensions of a fourbar linkage mechanism that best fits the scanning task via an optimization problem, solved with an estimation of distribution algorithm. The optimization algorithm proposes configurations with different lengths and reference positions of four-bar linkage mechanisms; then, it measures the distance between points in the actual path and points in the desired path for each configuration. The objective function value is the sum of such distances; thus, the optimal design produces the minimum distance to the desired path. This proposal for automated design reduces the working time and experience requirements of a human designer, and trial-and-error design intends, by determining adequate dimensions for the mechatronic system. A CAD model and a simulation demonstrate the design feasibility and the high accuracy of the resulting device.


Index Terms-Dimensional synthesis, Optimization, BUMDA, Four-bar linkage mechanism, Automated design

## I. INTRODUCTION

As the energy efficiencies and artificial lighting systems have improved, lighting levels have risen, and therefore light at night. Light pollution is mostly located at the troposphere level, between 0 and 10 km above sea level. In this portion of the atmosphere, night-time artificial radiation interacts with suspended particles (specifically aerosols and water molecules), which are the main modulators of light pollution. The conditions of these particles can present extreme variations that make light pollution an overly complex phenomenon to study. Due to these variations, light pollution values show temporal changes that also occur at different measurement angles. Typically, measurements at the zenith never show the same values as measurements close to horizon. Light pollution is often measured with photometers located at astronomical observatories that offer only local measurements. Having not many portable instruments has limited the efforts of many scientists to obtain data covering larger areas. The magnitude
used in astronomy to quantify light pollution is the luminance of the night sky background [1] [2].

The measurement of light pollution must be carried out in night environments, where the amount of light is extremely low, and therefore, instruments with high sensitivity are required. There are some instruments photometrically calibrated consisted of CCD or CMOS sensors with different filters and fisheye lens, which provides the instrument with a 180-degree field of view in all directions. However, they are either expensive or complex. Therefore, the development of low-cost devices for measurements of angular daylight luminance distributions is increasing in interest. In [3], a low-cost prototype based on Light Dependent Resistors to measure angular daylight luminance distribution is developed. It has been proposed to predict indoor daylight distribution and optimizing the building's design. In [4], a High Dynamic Range image-based system was applied to capture luminance distributions of the sky, window view, and interior surfaces. In [5], a device for the measurement of diffuse solar irradiance on tilted surfaces pointing-to as well as fixed on the equatorial direction is proposed. Although most of these instruments fulfill the applications and they are inexpensive with low maintenance costs, they are adjusted by one single operator. Thus, the system's effects on the luminance measurement with a continuous and automatized operation could be investigated.

On the other hand, the generation of controlled movements through planar mechanisms has played an essential role in successful applications that range from industrial to health tasks into the robotic and mechatronic areas. Indeed, modifications of traditional planar mechanisms have still been proposed to achieve more flexibility, and high accuracy in function generation tasks [6]. Repeatability and automation of predefined tasks are the main advantages of these planar structures, which have been widely used in a diversity of applications. The continuous increase in computer power has permitted approaches for addressing demanding optimization problems, as is the synthesis of robotic mechanisms. Automated design of mechatronic systems has been addressed as an optimization problem, with the purpose of determining optimal dimensions [7], control gains, and other design specifications via a software application. In [8], the design optimization of the four-bar linkage for the reduction of the shaking force and moment by using natural coordinates and the use of

counterweights have been presented. The automated synthesis of a four-bar mechanism to positioning a portable sky scanner is proposed in this contribution. An optimization problem is formulated by considering the workspace that must cover the task device, which has been intended for measuring luminescence pollution. This formulation is implemented and solved with an estimation of distribution algorithm that delivers a set of design variables required for CAD modeling of the resulting optimized design.

## II. BACKGROUND

The four-bar linkage has been widely used as a case study for optimal synthesis of mechanisms and mechatronic systems [9], [10], [11] due to its flexibility to reach a wide variety of cyclic paths, and its simplicity. It has a single actuated element, and the end-effector can be posed in non-intuitive positions by manipulating the mechanism's lengths and reference positions. Finally, its inverse kinematics presents two solutions that are solved with a minimum computational effort. All these features make it excellent as a base design for automated synthesis. In the same regard, the portable sky scanner requires a mechanism that can repeat cyclic paths, hence the design task makes a perfect match with the proposed four-bar linkage base design. This section discusses the kinematics of the four-bar linkage. It is a pure algebraic model that must be solved per each candidate solution proposed by the optimization algorithm. Solving the model is, actually, to numerically simulate a position of the end effector given an angle in the actuated element.

## A. Inverse Kinematics

The four-bar linkage mechanism is shown in Figure 1. The inverse kinematics is used for computing the position of the end effector $C$ given the actuated angular position $\theta_{2}$.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Schematic diagram of the mechanism
The position of the end-effector $C$ in terms of the relative coordinates $X_{0}, Y_{0}$ is defined in vector notation in Equation (1).

$$
C_{0}=r_{2}+r_{c x}+r_{c y}
$$

Decomposing Equation (1) along $X_{0}$ and $Y_{0}$ we obtain Equation (2) as follows.

$$
\begin{aligned}
& C_{0 x}=r_{2} \cos \theta_{2}+r_{c x} \cos \theta_{3}-r_{c y} \sin \theta_{3} \\
& C_{0 y}=r_{2} \sin \theta_{2}+r_{c x} \sin \theta_{3}+r_{c y} \cos \theta_{3}
\end{aligned}
$$

Now, in order to determine $\theta_{3}$, let us establish the closedloop of the mechanism, that is to say, Equation (3).

$$
r_{2}+r_{3}-r_{4}-r_{1}=0
$$

The expression in Equation (3) is outlined in terms of its components around the relative coordinates, in Equation (4).

$$
\begin{gathered}
r_{2} \cos \theta_{2}+r_{3} \cos \theta_{3}-r_{4} \cos \theta_{4}-r_{1}=0 \\
r_{2} \sin \theta_{2}+r_{3} \sin \theta_{3}-r_{4} \sin \theta_{4}=0
\end{gathered}
$$

Equations (3) to (4) are employed to eliminate $\theta_{0}$, yielding a simple homogeneous formulation defined as follows in Equation (5), thus,

$$
k_{1} \cos \theta_{3}+k_{2} \cos \theta_{2}+k_{3}=\cos \left(\theta_{2}-\theta_{3}\right)
$$

In this manner, $\theta_{3}$ is computed as shown in Equation (6),

$$
\theta_{3}=2 \arctan \left(\frac{-b \pm \sqrt{b^{2}-4 a c}}{2 a}\right)
$$

with

$$
\begin{gathered}
a=\cos \left(\theta_{2}\right)-k_{1}+k_{2} \cos \left(\theta_{2}\right)+k_{3} \\
b=-2 \sin \left(\theta_{2}\right) \\
c=k_{1}+\left(k_{2}-1\right) \cos \left(\theta_{2}\right)+k_{3} \\
k_{1}=r_{1} / r_{2} \\
k_{2}=r_{1} / r_{3} \\
k_{3}=\left(r_{4}^{2}-r_{1}^{2}-r_{2}^{2}-r_{3}^{2}\right) /\left(2 r_{2} r_{3}\right)
\end{gathered}
$$

Finally, the position of the end effector, defined in terms of the general coordinates is in Equations (8) and (9). These equations are used to compute the objective function, in order to determine the quality of a given configuration. Notice that Equation (6) has three kinds of solutions, two of them real, and the others are complex. The real solutions, are two valid configurations, named as crossed and open configurations, but the complex is not valid. In addition, it is possible to have real and complex solutions for the very same lengths and reference positions, that means that for some values of $\theta_{2}$ the configuration is valid, but for others it is not.

$$
\begin{aligned}
C_{x}=X_{0}+r_{2} \cos \left(\theta_{0}+\theta_{2}\right)+r_{c x} & \cos \left(\theta_{0}+\theta_{3}\right) \\
& -r_{c y} \sin \left(\theta_{0}+\theta_{3}\right) \\
C_{y}=Y_{0}+r_{2} \sin \left(\theta_{0}+\theta_{2}\right)+r_{c x} & \sin \left(\theta_{0}+\theta_{3}\right) \\
& +r_{c y} \cos \left(\theta_{0}+\theta_{3}\right)
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. The sky scanner must cover a kind of discretized semi-sphere. This is achieved via two movements: the mechanism covers the angle parallel to the precision points, while the base is moved in a perpendicular direction.

## III. AUTOMATED SYNTHESIS PROBLEM

The portable sky scanner must cover a kind of half sphere. Figure 2 shows a quarter of such sphere, to show a cut, this cut defines a path for the four-bar linkage mechanism. Actually, covering the surface is not as important as covering the zenith and azimuth angles. The first is achieved via the four-bar linkage mechanism, while the second is covered by a moving base.

The optimization problem is to find the mechanism that reaches with minimum error a set of points named precision points. Hence, the optimization model is in Equation (10). The objective function sums the square difference between the $N$ precision points, labeled as $\left[C_{x, i}^{P}, C_{y, i}^{P}\right]$, and their closest points in the mechanism's path $\left[C_{x, i}^{M}, C_{y, i}^{M}\right]$.

$$
\begin{gathered}
\min f\left(\theta_{0}, r_{1}, r_{2}, r_{3}, r_{4}, r_{c x}, r_{c y}, X_{0}, Y_{0}\right)= \\
\sum_{i=1}^{N}\left(C_{x, i}^{P}-C_{x, i}^{M}\right)^{2}+\left(C_{x, i}^{P}-C_{y, i}^{M}\right)^{2} \\
0 \leq \theta_{0} \leq 2 \pi \\
0.1 \leq r_{1}, r_{2}, r_{3}, r_{4}, r_{c x}, r_{c y} \leq 0.5 \\
0 \leq X_{0}, Y_{0} \leq 1
\end{gathered}
$$

## A. Evaluation of a candidate configuration

The optimization algorithm proposes a set of candidate solutions, each of them consist of an array of 9 elements $\left[\theta_{0}, r_{1}, r_{2}, r_{3}, r_{4}, r_{c x}, r_{c y}, X_{0}, Y_{0}\right]$, and it must be evaluated in the objective function in (10). For this purpose, the angular positions of $\theta_{2}$ (see Figure 1), are discretized in the range $[0,2 \pi]$, with intervals of $\pi / 18000$, that is to say, the end effector position is computed for different positions of $\theta_{2}$, in its complete working range, displacing 0.01 degrees the angle between consecutive computations. We associate an error array of size $N$ to the set of $N$ precision points. It is initialized with a large value before starting the simulation. For each
value of $\theta_{2}$ we verify whether the current position of the end effector has a lower distance to any of the precision points. All the precision points with a lower distance to the current endeffector position, require to update the corresponding positions in the error array.

Notice the following:

- Some configurations can not be simulated, because the dimensions of the elements can not build a working mechanism. In this case, the error array remains with a set of large values, thus their sum, that is larger, is returned.
- If a single value of $\theta_{2}$ delivers a real value of the endeffector's position, all the values in the error array are modified.
- If a subset of values of $\theta_{2}$ deliver real values of the end-effector's position, this is sufficient to compute the objective function, and possible, to deliver a competitive configuration. Hence, it is not necessary that the optimum configuration delivers a real solution to all the $\theta_{2}$ values, neither in the optimization process, nor in the physical mechanism.


## B. Optimization method

The optimization method is the Boltzmann Univariate Marginal Distribution Algorithm (BUMDA) [12], [13], [7], [14]. It is an Estimation of Distribution Algorithm based on the Boltzmann distribution approximated by a normal distribution. The BUMDA generates an initial population, with a uniform distribution within the search limits defined in Equation (10). Then, each candidate solution is evaluated. The best solutions are selected and weighted proportional to a translation of their objective function value, for computing weighted estimators of the mean and variance of the normal distribution. Then, new samples are generated from the normal distribution and they are used to replace the current population except the elite individual, the process is repeated until convergence is reached. The convergence is measured using the standard deviation of the objective function values of the population. The BUMDA, presents several advantages, for instance, it do not require of an arbitrary stopping criterion, as other populationbased algorithms, and it requires a single parameter, that is the population size, and is set to $10 n_{\text {var }}=90$, the minimum standard deviation used as stopping criterion is $10^{-20}$.

## IV. Optimization results

Table I shows a typical output of the BUMDA. It shows the dimensions of the mechanism and the reference positions and angle. The $f$ value is the objective function value, that also is an accumulated distance from the desired discretized path to the actual path. These two paths are shown in Figure 5, the actual path, with red lines, is quite close to the precision points (with blue crosses). Hence these results demonstrate that the method actually design a feasible mechanism.

Finally, Figure 6 shows a 3D CAD model of the final design, the mechanism is shown in white, the end effector is modeled as a light-weight element, with the optical sensor mounted as

a cylinder with a cable, the cable varies the orientation of the sensor, to take measurements in a normal angle to the semicircular path described by the four-bar linkage mechanism. The base in blue is equipped with an actuator to rotate the mechanism. Due to the simplicity of the resulting mechanism and the light weight of the moving sensor, the material of the elements is proposed to be of rigid polymer, which favors the energy saving in the task of conducting the light sensor. Besides, ball bearings are employed to reduce the friction between the rotating links. This mechanism can be actuated in both directions with step DC motors.

TABE I
OPTIMIZATION RESULTS

## V. CONCLUSIONS

This article presents an application to automated design of a portable sky scanner. Nevertheless, several proposals have approached similar problems, in this research we take advantage of the body of knowledge in the state of the art of different problems, for instance, automated design, a bioinspired algorithm that has shown excellent performance in similar problems, simulation and modelling of a mechatronic system, and the proposal of using a portable sky scanner, that has been designed ad hoc for the task of replacing a network of sensors.

The accumulated error to the desired path is $6.21 e-5$, but notice that is the sum of the squares of the error, hence, the error for each point is less than 0.001 , even more, this error can be reduced in several manners, for instance, increasing the number of precision points, increasing the size of the discretization of $\theta_{2}$, and reducing the standard deviation of the objective function values, used as the stopping criterion of the BUMDA. Although, for this particular application the error is sufficient.

Finally, this research does not consider the comparison between different bio-inspired algorithms for automated design or a general procedure. It is possible that all of the comparing algorithms deliver noncompliant designs, out of specification, and this is not important when the purpose of the investigation is to compare the algorithms. In our case, if another algorithm performs better than the BUMDA is not relevant because the error delivered at this stage by the BUMDA is so small that it is less than the required in a physical application, in addition, assuming that other algorithm reports a lower error, lengths or dimensions with more decimals below the tenththousands, these are not physically noticeable for building a physical prototype. In summary, the comparison is not
![img-4.jpeg](img-4.jpeg)
![img-3.jpeg](img-3.jpeg)
![img-4.jpeg](img-4.jpeg)

Fig. 3. Different positions of the optimized mechatronic system for scanning in the zenith angle.

![img-5.jpeg](img-5.jpeg)

Fig. 4. Different positions of the optimized mechatronic system for scanning in the azimuth angle.
![img-6.jpeg](img-6.jpeg)

Fig. 5. Approximation of the desired trajectory through the optimization
![img-7.jpeg](img-7.jpeg)

Fig. 6. Close-up to the sensor mounting, notice the cable that keeps the sensor perpendicular to the path in Figure 5.
performed since from the real-world application problem, it does not substantially contribute to improving the prototype. Our research problem models a real-world problem as an optimization problem that is solved by an algorithm. The future work, in this sense, is to improve the optimization model to consider more design specifications or an integral design, for instance to include dexterity, rigidity, or other kinds of constraints, that is the direction of our approach. From the point of view of automated design via an optimization model, we can improve the design by improving the optimization model, hence, the future work contemplate to include dexterity constraints, and the design of the control of the mechatronic system.

## ACKNOWLEDGMENT

S. Ivvan Valdez is supported by Cátedra-CONACYT 7795. Authors are also grateful to SIP-IPN for supporting part of this work through project SIP-20210243. H. Lamphar is supported by Cátedras Conacyt and by the Slovak Research and Development Agency under Project No. APVV-18-0014.
