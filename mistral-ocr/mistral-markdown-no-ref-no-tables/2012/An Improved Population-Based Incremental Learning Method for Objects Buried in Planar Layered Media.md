# An Improved Population-Based Incremental Learning Method for Objects Buried in Planar Layered Media 

Xiaoming Chen ${ }^{1}$, Gang Lei ${ }^{1,2}$, Guangyuan Yang ${ }^{1}$, K. R. Shao ${ }^{1}$, Youguang Guo ${ }^{2}$, Jianguo Zhu ${ }^{2}$, and J. D. Lavers ${ }^{3}$, Fellow, IEEE<br>${ }^{1}$ State Key Laboratory of Advanced Electromagnetic Engineering and Technology, Huazhong University of Science and Technology, Wuhan, 430074, China<br>${ }^{2}$ Faculty of Engineering and Information Technology, University of Technology, Sydney, N.S.W. 2007, Australia<br>${ }^{3}$ Department of Electrical and Computer Engineering, University of Toronto, Toronto, ON M5S 3G4, Canada

An evolutionary algorithm, the estimation of distribution algorithm (EDA), is used to reconstruct the objects that buried in planar layered media. It is essential that fast forward solvers be used to solve the forward scattering problem for the nonlinear inverse scattering methods, since it can avoid errors by approximation. The EDA is a predominant all-round optimizing method in the macroscopic simulation of evolution process species of nature. Recent studies have shown that the EDA provides better solution for nonlinear problems than the microscopic evolutionary algorithm, such as genetic algorithm (GA) in some cases. The EDA is simpler, both computationally and theoretically, than the GA. We discuss how this can be used to calculate the permittivity and conductivity of the targets. We show preliminary results indicating the potential of reconstruction for buried objects. Compared with other methods, the experiment result shows that the EDA algorithm reduces the number of iteration.

Index Terms-Buried objects, estimation of distribution algorithm, inverse scattering, layered media.

## I. INTRODUCTION

THE problem of reconstructing three-dimensional objects buried in layered media is an important research issue [1]. It is useful in geophysical exploration, target identification, environmental survey, microwave imaging and nondestructive testing. Previously, many methods have been applied to solve inverse problem, such as genetic algorithm (GA) [2], Born iteration method (BIM) [3], [4], and distorted Born iteration method (DBIM) [5].
Recent researches [6] have shown that the EDA outperforms a GA on large set of optimization problems in terms of both speed and accuracy in some cases, such as traveling salesman, job shop scheduling, knapsack, bin packing, neural network weight optimization, and numerical function optimization. EDAs are a class of novel stochastic optimization algorithms, which have recently become a hot topic in the field of optimization algorithms. Compared with GA, EDA does not need the process of inheritance and variation. As the problem of inverse scattering in layered media is a large scale problem, so we want to use the advantage and ability of EDA and apply it to this case.
In the present paper, we propose the application of a new inversion method, which is based on an estimation of distribution algorithm. The electromagnetic inverse problem is recast as a global optimization problem and discretized by using the moment method. It should be remarked that the applied stochastic optimization algorithm is potentially able to obtain the global minimum of the cost function resulting from the formulation of the inverse scattering problem.
In the following, the implementation procedure of the approach is presented. Moreover some obtained results are shown. The results have shown that in application of this method the

[^0]![img-0.jpeg](img-0.jpeg)

Fig. 1. Typical configuration of an inhomogeneous object in a planar layered medium.
cost and time of computation can also be reduced. This example allows a preliminary assessment of the capabilities of the approach.

## II. FORWARD MODEL

The geometry model of the problem is shown in Fig. 1, where the background medium has $M$ parallel layers with independent permittivity, conductivity, and permeability $\left(\varepsilon_{i}, \mu_{i}, \sigma_{i}, i=\right.$ $1, \ldots, M)$. The source is located in layer $p$, the target is completely buried in layer $i$, while the observation point is located in layer $m$; there is no restriction to $p, i$, or $m$. The electrical properties of the inhomogeneous objects are $\varepsilon_{r}, \sigma_{r}$, and $\mu_{i}$.

Note that for simplicity we have assumed that the target has the same permeability as layer $i$ so that there is no contrast in $\mu_{i}$ and $\mu_{r}$. The complex permittivity is defined as $\tilde{\varepsilon}=\varepsilon+(\sigma / j \omega)$. Our objective in the forward model is to calculate the electromagnetic fields due to a source in such a complex medium.


[^0]:    Manuscript received June 24, 2011; revised October 11, 2011; accepted October 21, 2011. Date of current version January 25, 2012. Corresponding author: X. Chen (e-mail: xiaominghust@gmail.com).

    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

    Digital Object Identifier 10.1109/TMAG.2011.2173749

Similar to the scattering problem in a homogeneous background medium, the solution procedure of the volume integral equation method is to find the induced current density inside the object, then the scattered field everywhere can be obtained through the Green's function.

The total electric field $E^{m p}(r)$ in the $m$ th layer is the sum of the incident field $E_{\text {inc }}^{m p}(r)$ and the scattered field $E_{\mathrm{sc} t}^{m p}(r)$, or

$$
E^{m p}(r)=E_{\text {inc }}^{m p}(r)+E_{\mathrm{sc} t}^{m i}(r)
$$

where $r$ is the position vector of the observation point.
The scattered electric field $E_{\mathrm{sc} t}^{m i}(r)$ due to this induced source in the layered medium is given by

$$
E_{\mathrm{sc} t}^{m i}(r)=-j \omega\left[I+\frac{1}{k_{m}^{2}} \nabla \nabla \cdot\right] A_{\mathrm{sc} t}^{m i}(r)
$$

while the scattered magnetic vector potential is

$$
A_{\mathrm{sc} t}^{m i}(r)=j \omega \mu_{m} \int G^{m i}\left(r, r^{\prime}\right) \cdot \chi\left(r^{\prime}\right) D\left(r^{\prime}\right) d r^{\prime}
$$

where $D(r)=\tilde{\varepsilon} E(r)$ is the electric flux density inside the object (still an unknown at this point), and $\chi(r)=\left(\tilde{\varepsilon}(r)-\right.$ $\left.\tilde{\varepsilon}_{i}\right) / \tilde{\varepsilon}(r)$ is the contrast function of the object, and $G^{m i}\left(r, r^{\prime}\right)$ is the dyadic Green's function for magnetic vector potential in a layered background medium. In this paper, the $z$ component has been selected in addition to the $x$ component. The Green's function in this case takes the "traditional" form [7]

$$
G^{m i}\left(r, r^{\prime}\right)=(\hat{x} \hat{x}+\hat{y} \hat{y}) G_{x x}^{m i}+\hat{z} \hat{x} G_{z x}^{m i}+\hat{z} \hat{y} G_{x y}^{m i}+\hat{z} \hat{z} G_{z z}^{m i}
$$

in the spatial domain. The closed form of the Green's function in spectral domain is derived by using the equivalent transmission line network. The Green's function in spatial domain is obtained from its expression in spectral domain by the Sommerfeld integral evaluation.

The incident electric field $E_{\text {inc }}^{m p}(r)$ in the $m$ th layer is

$$
E_{\text {inc }}^{m p}(r)=-j \omega\left[I+\frac{1}{k_{m}^{2}} \nabla \nabla \cdot\right] A_{\text {inc }}^{m p}(r)
$$

while the incident magnetic vector potential is

$$
A_{\text {inc }}^{m p}(r)=j \omega \mu_{m} \int G^{m p}\left(r, r^{\prime}\right) \cdot \chi\left(r^{\prime}\right) D\left(r^{\prime}\right) d r^{\prime}
$$

At this point, the scattered field $E_{\mathrm{sc} t}^{m i}(r)$ still cannot be obtained because $D(r)$, thus $\chi\left(r^{\prime}\right) D\left(r^{\prime}\right)$ inside the integrand in (3), remains unknown. However, substituting (2) and (3) into (1), we can obtain yields

$$
\begin{aligned}
E_{\text {inc }}^{m p}(r)=\frac{D(r)}{\tilde{\varepsilon}_{m}}-\left(k_{m}^{2}\right. & \left.+\nabla \nabla \cdot\right) \frac{1}{\tilde{\varepsilon}_{m}} \\
& \times \int_{V} G^{m i}\left(r, r^{\prime}\right) \cdot \chi\left(r^{\prime}\right) D\left(r^{\prime}\right) d r^{\prime}
\end{aligned}
$$

Equation (7) is valid everywhere.
Solve this Sommerfeld integral equation, we can obtain the electric flux density $D(r) . D(r)$ can then be used to find the induced current density inside the scattering object according to

$$
J_{\mathrm{eq}}(r)=j w \chi(r) D(r)
$$

Once the induced current is known, the scattered electric field at any location can be easily obtained from (2) and (3). Then, we can obtain

$$
\begin{aligned}
E_{\mathrm{sc} t}^{m i}(r)=-j \omega\left[I+\frac{1}{k_{m}^{2}} \nabla \nabla \cdot\right] A_{\mathrm{sc} t}^{m i}(r) \int G^{m i} & \left(r, r^{\prime}\right) \\
& \cdot J_{\mathrm{eq}}\left(r^{\prime}\right) d r^{\prime}
\end{aligned}
$$

A relative error function with respect to the electromagnetic parameters is defined as

$$
\begin{aligned}
& G(g) \\
& =\frac{\sum_{u=1}^{n_{t}} \sum_{v=1}^{n_{r}} \sum_{w=1}^{n_{s}}\left|E^{\text {meas }}\left(t_{u}, r_{v}, s_{w}\right)-E^{\text {comp }}\left(t_{u}, r_{v}, s_{w} ; g\right)\right|^{2}}{\sum_{u=1}^{n_{t}} \sum_{v=1}^{n_{r}} \sum_{w=1}^{n_{s}}\left|E^{\text {meas }}\left(t_{u}, r_{v}, s_{w}\right)\right|^{2}}
\end{aligned}
$$

where $E^{\text {meas }}$ is the result of measured electric field intensity at the observation points, and $E^{\text {comp }}$ is the result of the hypothetical parameters $g$ computed by forward model. $t_{u}, r_{v}$, and $s_{w}$ are the incident element, receiver element, and sample point in the frequency domain respectively. $n_{t}, n_{r}$, and $n_{s}$ are the total number of incident, receivers and frequencies, respectively.

The relative error function gives a measurement on how close the inverted results approach the true profile. The inverse problem can therefore be cast into an optimization problem by minimizing the relative error function. In order to convert it into a maximization problem, a fitness function is defined as

$$
\begin{aligned}
& F(g) \\
& =1-\frac{\sum_{u=1}^{n_{t}} \sum_{v=1}^{n_{r}} \sum_{w=1}^{n_{s}}\left|E^{\text {meas }}\left(t_{u}, r_{v}, s_{w}\right)-E^{\text {comp }}\left(t_{u}, r_{v}, s_{w} ; g\right)\right|^{2}}{\sum_{u=1}^{n_{t}} \sum_{v=1}^{n_{r}} \sum_{w=1}^{n_{s}}\left|E^{\text {meas }}\left(t_{u}, r_{v}, s_{w}\right)\right|^{2}}
\end{aligned}
$$

## III. THE EDA-BASED CALCULATION

The estimation of distribution is a robust stochastic search and evolution procedure. Through using statistical learning tools from a macroscopic perspective to establish a probability model, the EDA describes the spatial distribution of candidate solutions by a probabilistic model. Then, according to probability model, generate a new random population sample, select best fitness individual, and repeat the procedure until the termination condition.

The key point of EDA is the probability model of the problem. The basic procedure of the EDA can be seen in Fig. 2. Compared to GA, the EDA excuses the process of inheritance and variation. Because of the inheritance and variation procedure in GA is very complicated and increases the difficulty of implementation. After reducing these two steps, the EDA is relatively easy to implement.

In order to compare the efficiency, most of the studies have used the ideal data. The reconstruction object in layered media can been seen Fig. 3. The dielectric con-

![img-3.jpeg](img-3.jpeg)

Fig. 2. The basic procedure of EDA.
![img-3.jpeg](img-3.jpeg)

Fig. 3. Two cubical anomalies to be imaged. The centers of the two cubes are $(2.5,2.5,5) \mathrm{cm}$ and $(7.5,7.5,7.5) \mathrm{cm}$ respectively, with the center of domain D located at $(5,5,5) \mathrm{cm}$.
stant and conductivity of the three layers studied here are $(\varepsilon, \sigma)=(1.0,0.0 \mathrm{~S} / \mathrm{m}),(3.5,0.02 \mathrm{~S} / \mathrm{m})$, and $(5.0,0.03 \mathrm{~S} / \mathrm{m})$, respectively. The dielectric constant and conductivity of the two objects are $\left(\varepsilon_{r}, \sigma_{r}\right)=(10.0,0.3 \mathrm{~S} / \mathrm{m})$. The second-layer thickness is 3 cm . The size of the $D$ domain containing the object is $10 \times 10 \times 10 \mathrm{~cm}^{3}$.

In this validation experiment, we use Gaussian pulse

$$
E^{\text {loc }}=\hat{x} \exp \left(-\left[\frac{4}{T}\left(t-\frac{r \cdot k}{c}\right)\right]^{2}\right)
$$

to reconstruct the objects buried in layered media. We cannot get the measurement data in real condition, so most of studies have add the Gaussian noise to the ideal data and this method is
![img-3.jpeg](img-3.jpeg)

Fig. 4. The structure of an individual.
commonly used in the inverse problems. In this paper, our objective is to calculate the electromagnetic parameters of the target. We discrete the $D$ domain into $4096=16 \times 16 \times 16$ uniform cells, with the size of each cell $0.625 \times 0.625 \times 0.625 \mathrm{~cm}^{3}$. This accuracy (less than 1 cm ) can meet the demand of engineering application. Then, a candidate solution can be written as

$$
g=g\left(\varepsilon_{1}, \sigma_{1}, \varepsilon_{2}, \sigma_{2}, \ldots, \varepsilon_{4096}, \sigma_{4096}\right)
$$

where $\varepsilon_{i}, \sigma_{i}(i=1,2, \ldots, 4096)$ are the dielectric constant and conductivity of the $i$ th cell, respectively. We can get the domain of every parameter according to our prior knowledge. The solution precision can be written as $P_{\beta}$, where $\beta$ denotes permittivity $\varepsilon$ or conductivity $\sigma$. Then, the length of every parameter is $L_{\beta}=\left(\beta_{\max }-\beta_{\min }\right) / P_{\beta}, \beta_{\max }$ and $\beta_{\min }$ can be obtained by prior knowledge.

We had better choose a low precision $P_{\beta}$ in the beginning. If we choose a high precision at first, the total length of individual will be too large to figure out. In order to reduce the computational burden, we first use small dimensions to ensure the range of solution roughly, and then use more dimensions to refine the precision gradually. The solution steps as follows:

First, we generate the initial population according to our probability vector. In order to be fair, generally this probability vector can be set as

$$
P_{i}^{0}=0,5, \quad i=1, \ldots, l
$$

where $l$ is the length of each individual, and $P_{i}^{0}$ is the probability of getting value " 1 " in the $i$ th place of the first generation. Now, every individual has a fitness that can be calculated by the objective function $F(g)$ in Section II. We can arrange the individual order according to its fitness and choose the relatively high fitness individual.

Second, we can update the probability vector according to the selected population:

$$
P_{i}^{k+1}=(1-\lambda) P_{i}^{k}+\lambda \frac{\sum_{j=1}^{R} x_{j i}^{k}}{R}, \quad i=1,2, \ldots, l
$$

The structure of an individual can be seen in Fig. 4. The EDA varies many different methods in this step, different update probability vector methods create different efficiency.

Third, we can generate new population according the update probability, and repeat the step 1 until the termination condition. An implementation pseudo code in $\mathrm{C}++$ is presented in Fig. 5. In this implementation, alpha is the learning rate. $M I N$ or $M A X$ is the minimum or maximum of the electromagnetic parameters, respectively. It also can be a vector. ERROR is the tolerance error in the result. NP is the number of problem. P0 is the initial

```
Generate population according to P0;
for( int i=1; i<NP; i++)
    Binary \(\rightarrow\) Decimal; Fitness;
    Sort Fitness; Old_Best>The best of fitness;
    P1=(1-alpha)*P0+alpha*(Best1+Best2+BEST3)/3;
Generate new population according to P1;
for( int i=1; i<NP; i++)
    Binary \(\rightarrow\) Decimal; Fitness;
    Sort Fitness; New_Best=The new best of fitness;
    ProfId=P2;
    While ([New_Best-Old_Best]=ERROR)
    Old_Best=New_Best;
    Pro_New= (1-alpha)*Pro_Old+ alpha*(Best1+Best2+BEST3)/3;
    Generate new population according to Pro_New;
    for( int i=1; i<NP; i++)
    Binary \(\rightarrow\) Decimal; Fitness;
    Sort Fitness; New_Best=The new best of fitness;
```

Fig. 5. The implementation pseudocode of the EDA in C++.
![img-4.jpeg](img-4.jpeg)

Fig. 6. The left is the GA reconstruction result and The right is the EDA reconstruction result. Dielectric constant $\varepsilon$ and conductivity $\sigma$ are in the top and bottom, respectively.

TABLE I
Performance Comparison of Defferent
METHODS ON THE RECONSTRUCTION


probability, generally $\mathrm{P} 0=(0.5,0.5, \ldots, 0.5)$. Each individual fitness can be obtained according to the objective function $F(g)$ in the Section II.

As is shown in Fig. 6, the EDA is relatively better than the GA in this condition. To explain this comparison difference, the key point may be that the global optimizing ability of EDA is better than GA. However, the reconstruction result is not very
ideal and has noise in results; this may be caused by the lack of sample points.

In order to compare the performance of different algorithms, we compare the number of iterations in BIM (DBIM) [8] with generation of EDA (GA) in Table I. Compared with other methods, we can see that EDA can reduce the computation in different accuracy. Generally, the accuracy of $5 \%$ can meet the demand of engineering application, so we choose this accuracy as a comparison standard.

## IV. CONCLUSION

Previous empirical work showed that EDA generally outperformed GA, BIM, and DBIM on this inverse scattering problem. As the EDA is a biological evolution algorithm modeling in "macro" level, it has very good performance advantage and its ability that handles nonlinear and large scale problems is better than the "micro" level mathematics iterative method. Compared with the numerical iterative method commonly, it can use the a priori information; for example, people know that dielectric constant and conductivity have a scope, so we can use this prior information to improve the efficiency of iteration.

Perhaps the most important contribution from this paper is an EDA way of thinking about reconstruction of objects in layered media using electromagnetic waves. Therefore, the present work provides an attractive alternative to deal with reconstruction of buried objects in layered media. This method is potentially very useful for the inverse-scattering problem in the detection of buried objects.

## ACKNOWLEDGMENT

This work was supported by the National Natural Science Foundation of China (NSFC) under Grant 51177054.
