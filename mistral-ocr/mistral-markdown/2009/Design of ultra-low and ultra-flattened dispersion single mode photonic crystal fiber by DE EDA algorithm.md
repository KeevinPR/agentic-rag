# Design of ultra-low and ultra-flattened dispersion single mode photonic crystal fiber by DE/EDA algorithm 

M. Pourmahayabadi* and S. Mohammad Nejad<br>Nanoptronics Research Laboratory, Department of Electrical Engineering, Iran University of Science and Technology, Tehran, Iran

(Received 17 March 2009; final version received 4 June 2009)


#### Abstract

This paper proposes a combination of differential evolution (DE) and estimation of distribution algorithm (EDA) to design photonic crystal fiber structures with desired properties over the C communication band. In order to determine the effective index of propagation of the mode and then, the other properties of structure, a finite difference frequency domain (FDFD) solver is applied. The results revealed that the proposed method is a powerful tool for solving this optimization problem. The optimized PCF exhibits a dispersion of $0.22 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ at $1.55 \mu \mathrm{~m}$ wavelength with a variance of $\pm 0.4 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ over the C communication band and a nearly zero dispersion slope.


Keywords: differential evolution/estimation of distribution algorithm; dispersion; dispersion slope; genetic algorithm; photonic crystal fiber

## 1. Introduction

Photonic crystals have attracted a great deal of attention in the optics community in recent years. One of the most promising applications of photonic crystals is the possibility of creating compact integrated optical devices with photons as the carriers of information, and then the speed and bandwidth of advanced communication systems can be increased dramatically [1,2]. Photonic crystal fibers (PCFs), a kind of two-dimensional photonic crystal, consisting of a central defect region surrounded by multiple air-holes that run along the fiber length have attracted much attention in recent years because of their unique properties which are not realized in conventional optical fibers [3-5]. PCFs are divided into two different kinds of fibers. The first one is the index-guiding PCF, guiding light by total internal reflection between a solid core and a cladding region with multiple air-holes. The second one uses a perfectly periodic structure exhibiting a photonic band-gap (PBG) effect at the operating wavelength to guide light in a low index core-region.

Index-guiding PCFs, also called holey fibers or microstructure optical fibers, possess especially an attractive property of great controllability in chromatic dispersion over a large wavelength range $[1,2,6]$. By varying different parameters of the photonic crystal fibers, such as the pitch $(\Lambda)$ of the periodic array, the air-hole diameter $(d)$, the number of air-hole rings $(N)$ and the refractive index $(n)$, one can engineer the
electromagnetic modes supported by the photonic crystal fibers and explore suitable properties for many practical applications.

The optimization of PCF design is often difficult due to the fact that the optical properties do not usually vary in a simple way with the fiber geometry parameters. The optimization problem of PCF gets more and more difficult as the numbers of variables $(\Lambda, n, d$ and $N)$ and the number of fiber properties that have to be considered, (chromatic dispersion, slope of this dispersion, confinement losses etc.) are increased. The design optimization is usually performed by trial and test approach. However, this is a time-consuming approach, both for the computer and the designer. In recent works, genetic algorithms (GAs) have been shown to offer a convenient platform for the solution of the optimization problems $[7-9]$.

The differential evolution (DE) is very successful in solving the global continuous optimization problem $[9,10]$. On the other hand, the estimation of distribution algorithm (EDA) offers another technique in which a probability model characterizes the distribution of excellent solutions [10-12]. This paper proposes a combination of DE and EDA (DE/EDA algorithm) to solve the optimization problem and to determine the PCF structure. Considering that the chromatic dispersion is a key parameter for many applications, this study is focused on the determination of the PCF structure that can lead to the minimum dispersion and nearly

[^0]
[^0]:    *Corresponding author. Email: pmahyabadi@iust.ac.ir

zero dispersion slope over the C communication band. Therefore, the two-dimensional finite difference frequency domain (2D-FDFD) method is applied to determine the effective index of propagation of mode which then enables one to ascertain the dispersion properties of PCF structures [13-16].

This paper is organized as follows. In the next section - Section 2 - the fiber geometry structures and problems associated with the optimizing fiber structure are stated. This is followed by Section 3, in which the theory of FDFD will be described. In the following section, the principles of DE/EDA algorithm will be explained. Section 5 will focus on the simulation results, analysing and making comparisons with similar works carried out in this field. The trend for future research works will be pointed out in Section 6 and finally the paper sets out its conclusion in the last section, Section 7.

## 2. Problem statement: fiber design and optimization

At present, the design and optimization of photonic crystal fibers is still an area of active research. As shown in Figure 1, all the air-holes in a section of typical PCFs are arrayed according to triangle regularity with identical pitch $\Lambda$, spacing of the neighbouring air-holes. The scale of the air-holes is denoted by $d$, its diameter. The background is pure silica. Because the effective refractive index of the core region is higher than the cladding region, total internal reflective (TIR) can occur at the interface between the core and the cladding.

PCFs possess the attractive property of great controllability in chromatic dispersion. Controllability of dispersion in PCFs is a very important problem for practical applications to optical communication systems, dispersion compensation, and nonlinear optics. So far, various PCFs with remarkable dispersion properties have been investigated numerically.
![img-0.jpeg](img-0.jpeg)

Figure 1. Schematic representation of a typical PCF.

Generally, the total dispersion coefficient $D_{\mathrm{t}}$ should be expressed as the sum of the waveguide dispersion $D_{\mathrm{w}}$ and the material dispersion $D_{\mathrm{m}}$, and $D_{\mathrm{m}}$ can be calculated by applying the Sellmeier law. Because PCF is made of silica, the material dispersion is the same for PCFs with different parameters in their structures [14]. The waveguide dispersion $D_{\mathrm{w}}$ is a crucial factor for calculating the total dispersion coefficient, which can be expressed as

$$
D_{\mathrm{w}}=-\frac{\lambda}{c} \frac{\mathrm{~d}^{2} n_{\mathrm{eff}}}{\mathrm{~d} \lambda^{2}}
$$

where $c$ is the velocity of light in a vacuum. When the hole-diameter to pitch ratio is very small and the pitch is large, the dispersion curve is close to the material dispersion of pure silica. As the air-hole diameter is increased, the influence of waveguide dispersion becomes stronger $[17,18]$.

As mentioned in the previous section, the FDFD method combined with the DE/EDA algorithm is used to optimize the fiber's profile as well as to accurately determine its modal properties. The simulation study was carried out with the database consisting of 500 individuals. Every individual has four features which are fiber parameters including pitch $(\Lambda)$, number of air-hole rings $(N)$, refractive index $(n)$, and air-hole diameter $(d)$.

The logical constraints are considered in the optimization process. The refractive index range of silica is $1.44 \leq n \leq 1.46$. In the structure, the air-hole diameter changes between $0.25 \Lambda$ and $0.45 \Lambda$.

In fact, unlike conventional fibers, triangular PCFs can be designed to be endlessly single-mode (ESM) that is to support only the propagation of the fundamental mode whatever the wavelength and the pitch value. Previous analyses on PCF cutoff properties have demonstrated that the ESM region is defined by $d / \Lambda<0.406[19,20]$. Furthermore, the lattice constant or pitch might be set to any value (microns). The value of lattice constant limits the value of the radius of a particular air-hole. The radius should be lower than half the lattice constant as, mathematically, the diameter cannot be greater than the pitch and neither can it be equal to this value because the silica would cease to be continuous. Here, the pitch varies in the range of 1.5 to $3 \mu \mathrm{~m}$. Also the number of air-hole rings is selected between 5 and 9 .

The characteristics of the individual chosen here are dispersion $(D)$ and its slope $(S)$ in the wavelength range from 1.53 to $1.565 \mu \mathrm{~m}$ (C communication band). These characteristics are calculated using the set of chromosomes $\{\Lambda, r, N, n\}$. We are now going to consider the following optimization problem;

$$
\min f(x)
$$

where $f(x)$ is a real-value function which has to be minimized to find the best solution. To do that, we need to define our preferred cost function for the proposed algorithm. Here are two kinds of cost functions:

$$
\begin{aligned}
f_{1}(x) & =\sum_{\lambda}|D| \\
f_{2}(x) & =\sum_{\lambda}|D| \times \sum_{\lambda}|S|
\end{aligned}
$$

As can be seen in the first case, dispersion is minimized while in the second case both dispersion and dispersion slope are minimized simultaneously.

## 3. Analysis method

The finite difference frequency domain (FDFD) is popular and appealing for numerical electromagnetic simulation due to its many merits. It has been one of the major tools for the analysis and understanding of PCFs.

The discretization scheme can be derived from the Helmholtz equations or Maxwell's equations directly. Now we use the direct discretization schemes first described for photonic crystal fibers by Zhu and Brown [12]. Yee's two-dimensional mesh is illustrated in Figure 2; note that the transverse fields are tangential to the unit cell boundaries, so the continuity conditions are automatically satisfied. After inserting the equivalent nonsplit-field anisotropic PML in the frequency domain, the curl Maxwell equations are expressed as

$$
\begin{aligned}
& \mathrm{i} k_{0} s \varepsilon_{\mathrm{r}} E=\nabla \times H, \quad-\mathrm{i} k_{0} s \mu_{\mathrm{r}} H=\nabla \times E, \\
& s=\left[\begin{array}{lll}
s_{y} / s_{x} & & \\
& s_{x} / s_{y} & \\
& & s_{x} s_{y}
\end{array}\right]
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. Unit cell in Yee's 2D-FDFD mesh. (The color version of this figure is included in the online version of the journal.)
where $\mu_{\mathrm{r}}$ and $\varepsilon_{\mathrm{r}}$ are the relative permittivity and permeability of the medium considered, $k_{0}=2 \pi / \lambda$ is the wave number in free space, $s_{x}=1-\sigma_{x} / \omega \varepsilon_{0}, s_{y}=$ $1-\sigma_{x} / \omega \varepsilon_{0}$ and $\sigma$ is the conductivity profile. Assuming that the PCFs are lossless and uniform and the propagation constant along the $z$ direction is $\beta$, the field variation along the propagation direction $z$ is of the form $(-\mathrm{i} \beta z)$. The $z$-derivatives, $\partial / \partial z$, can be replaced by $-\mathrm{i} \beta$ in Maxwell's equations and thus three-dimensional equations can be solved using only a two-dimensional mesh. Using the central difference scheme and zero boundary conditions outside of the anisotropic PML layers, the curl Equations (5) can be rewritten in a matrix form which includes six field components. In these numerical simulations, a ten layer PML is used. Then eliminating the longitudinal magnetic and electric fields, the eigenvalue matrix equation in terms of transverse magnetic fields and transverse electric fields can be obtained as

$$
\begin{aligned}
{\left[\begin{array}{ll}
Q_{x x} & Q_{x y} \\
Q_{y x} & Q_{y y}
\end{array}\right]\left[\begin{array}{l}
H_{x} \\
H_{y}
\end{array}\right] } & =\beta^{2}\left[\begin{array}{l}
H_{x} \\
H_{y}
\end{array}\right] \\
{\left[\begin{array}{ll}
P_{x x} & P_{x y} \\
P_{y x} & P_{y y}
\end{array}\right]\left[\begin{array}{l}
E_{x} \\
E_{y}
\end{array}\right] } & =\beta^{2}\left[\begin{array}{l}
E_{x} \\
E_{y}
\end{array}\right]
\end{aligned}
$$

where $Q$ and $P$ are highly sparse coefficient matrices. The order and the nonzero elements in them are reduced and effectively stored in sparse format, so the computation efficiency is improved greatly. The complex propagation constant $\beta$ and the transversal magnetic or electric field distribution can be solved out quickly and accurately by a sparse matrix solver [13,22].

Solving the eigenvalue Equations (7) or (8) using available numerical routines provides us with the effective modal index $n_{\text {eff }}=\beta / k_{0}$ and modal fields of the guided modes. The transversal field intensity distribution for the guiding modes of three different PCFs at $1.53,1.55$ and $1.565 \mu \mathrm{~m}$ wavelengths are shown in Figure 3. The modal field distributions exhibit the six-fold symmetry of the cladding region in these PCFs. The electromagnetic fields are confined efficiently in the core region of the PCFs at the shorter wavelength. This also implies that the PCFs will have better wave guide feature at a shorter wavelength than at a longer one for the same PCFs. As expected, on increasing the number of air-holes ring, the confinement loss is significantly reduced.

## 4. Design strategy

Genetic algorithms, applied to inverse PCF design, involve a stochastic search for a globally optimal PCF structure which provides the best performance of a PCF for a specific function. In this paper, an optimum

![img-2.jpeg](img-2.jpeg)

Figure 3. Transversal field intensity distribution for the guiding modes of SMPCFs with the following parameters; (a) $\Lambda=3 \mu \mathrm{~m}$, $d / \Lambda=0.4$ and $N=5$, (b) $\Lambda=2.5 \mu \mathrm{~m}, d / \Lambda=0.4$ and $N=7$, (c) $\Lambda=2 \mu \mathrm{~m}, d / \Lambda=0.4$ and $N=9$ at (a) $1.53 \mu \mathrm{~m}$, (b) $1.55 \mu \mathrm{~m}$ and (c) $1.565 \mu \mathrm{~m}$ wavelengths. (The color version of this figure is included in the online version of the journal.)
design technique for PCF that utilizes an algorithm combining DE and EDA (DE/EDA) is proposed. Simulation results demonstrate that DE/EDA outperforms both the DE algorithm and the EDA in optimization design.

### 4.1. Differential evolution

In this section, we briefly review the DE algorithm. In fact, it is the best GA-like algorithm for the global
continuous optimization problem. The DE algorithm has several versions; we consider the best one [9]. This algorithm maintains a population of $N$ points in every generation, where each point is a potential solution. The algorithm evolves and improves the population iteratively. In each generation, a new population is generated based on the current population. To generate offsprings for the new population, the algorithm extracts distance and direction information from the current population members and adds random

deviation for diversity. If an offspring has a lower objective function value than a predetermined population member, it will replace this population member. This evolution process continues until a stopping criterion is met (e.g. the current best objective function value is smaller than a given value or the number of generations is equal to a given maximum value) $[9,10]$.

Due to its ability to maintain the diversity and to do local search, the DE algorithm performs better than some other GAs. But the DE algorithm has no mechanism to directly use the global information about the search space to guide the population towards promising areas.

### 4.2. Estimation of distribution algorithm

Estimation of the distribution algorithm (EDA) is a new class of GAs. EDA directly extracts the global statistical information about the search space from the search so far and builds a probability model of promising solutions. New solutions are sampled from the model thus built. Let $\operatorname{Pop}(t)$ be the population of solutions at generation $t$. EDAs work in the following iterative way:
Step 1: Selection. Select $M$ promising solutions from $\operatorname{Pop}(t)$ to form the parent set $Q(t)$ by a selection method.
Step 2: Modelling. Build a probabilistic model $p(x)$ based on the statistical information extracted from the solutions in $Q(t)$.
Step 3: Sampling. Sample new solutions according to the constructed probabilistic model $p(x)$.
Step 4: Replacement. Fully or partly replace solutions in $\operatorname{Pop}(t)$ by the sampled new solutions to form a new population $\operatorname{Pop}(t+1)$.
One of the major issues in EDAs is how to select parents. A widely-used selection method in EDA is the truncation selection. In the truncation selection, individuals are sorted according to their objective function values and only the best individuals are selected as parents. Another major issue in EDAs is how to build a probability distribution model $p(x)$. In EDAs for the global continuous optimization problem, the probabilistic model $p(x)$ can be a Gaussian distribution [10-12].

### 4.3. DEJEDA algorithm

The most important operation in the DE algorithm is to generate offspring. Each offspring is generated by crossing a solution from the current population and a solution obtained by the DE mutation. On the other hand, EDA tries to guide its search towards
a promising area by sampling new solutions from a probability model. The EDA mechanism is incorporated into the DE algorithm in order to create solutions which are more promising than solutions generated by the DE recombination (crossover and mutation), and consequently, to explore the search space more effectively [9]. The DE/EDA algorithm is given as follows:
Step 1: Randomly generate $N$ solutions $x_{1}^{0}, x_{2}^{0}, \ldots, x_{N}^{0}$ from the feasible search space to form an initial population, set $k=0$.
Step 2: Generate a new solution $x_{i}^{k}$ according to the DE/EDA offspring generation scheme described in the above section.
Step 3: If the given stopping criterion is not met, $k=k+1$, go to Step 2.
At generation $k$, the proposed DE/EDA offspring generation scheme works as follows:
Step 1: Select the best $M$ solutions from the current population, construct a probability model as;

$$
\begin{aligned}
p_{k}(x) & =\prod_{i=1}^{n} N\left(x_{i} ; \hat{\mu}_{i}^{k}, \hat{\sigma}_{i}^{k}\right) \\
\hat{\mu}_{i}^{k} & =\hat{X}_{i}^{k}=\frac{1}{M} \sum_{i=1}^{M} x_{i, i}^{k} \\
\hat{\sigma}_{i}^{k} & =\left[\frac{1}{M} \sum_{i=1}^{M}\left(x_{i, i}^{k}-\hat{X}_{i}^{k}\right)^{2}\right]^{1 / 2}
\end{aligned}
$$

Step 2: Generate a trial solution $u=\left(u_{1}, u_{2}, \ldots, u_{n}\right)$ as follows: for all $j=1,2, \ldots, n$ if $(\operatorname{rand}(.)<\delta)$
$u_{j}=\left[\left(x_{i}^{k}\right)_{j}+\left(x_{i i}\right)_{j}\right] / 2+F \times\left[\left(x_{i i}\right)_{j}-\left(x_{i}^{k}\right)_{j}+\left(x_{i i}\right)_{j}-\left(x_{i}\right)_{j}\right]$,
else $u_{j}$ is sampled according to $N\left(x_{i}^{k} ; \mu_{i}^{k}, \sigma_{i}^{k}\right)$; where $\operatorname{rand}()$ is an uniform random number in $(0,1)$, and $\delta(1 \leq \delta \leq N)$ is a parameter.
Step 3: If $f(u) \leq f\left(x_{i}^{k}\right)$ then $x_{i}^{k+1}=u$, otherwise, set $x_{i}^{k+1}=x_{i}^{k}$.
The above offspring generation scheme is similar to the DE crossover. Like the DE offspring generation scheme, one part of a trial solution generated comes from the DE mutation. But the other part of the trial solution is sampled in the search space from the constructed probability distribution model. Therefore, a trial solution generated by the DE/EDA offspring generation scheme is based on the differential information and global statistical information. $\delta$ is used to balance contributions of the global information and the differential information.

Parameters involved in the proposed algorithm are $N, \delta$ and $F$. The number of solutions selected in Step 1 of the DE/EDA offspring generation scheme $M=N / 2$. Compared with the DE algorithm, DE/EDA has only a small extra computational cost in constructing the probability model. On the other hand, DE/EDA has the ability to utilize the global statistical information collected from the previous search, and it also can use the differential information in the DE way.

## 5. Implementation of genetic algorithms; results and discussion

In this section the results of GA methods in order to optimize the dispersion characteristics of the PCFs are presented. At the first generation of each GA, a population of 'individuals' is randomly created, each individual being a possible solution to the problem. In the particular case of this paper, each individual corresponds to a particular design of PCF and is made of four 'chromosomes' $\{\Lambda, r, N$ and $n\}$ which constitute the variables of the problem.

The simulation study was carried out with the database consisting of 500 individuals. The following steps are performed 10 times.

First of all 100 individuals are selected randomly. Then all three GA algorithms, explained above are applied to this selected population. In order to calculate the cost function, we need to determine the dispersion characteristics over the C communication band. As mentioned in Section 2, the FDFD method is applied to analyze the dispersion property of the triangular PCF and it has been one of the major tools for the analysis and understanding of PCFs. This evolution process continues until the number of generations is equal to a given maximum value (it is 500 in our case). In the last step, the ten best individuals are selected and they are put in the pool as the new population.

Table 1. The solution (PCFs parameters) found by the three methods with the first cost function.

| Method | $N$ | $\Lambda(\mu \mathrm{~m})$ | $n$ | $d(\mu \mathrm{~m})$ |
| :-- | :--: | :--: | :--: | :--: |
| DE | 9 | 2.5 | 1.46 | 0.7472 |
| EDA | 9 | 2.077 | 1.449 | 0.9138 |
| DE/EDA | 5 | 2.276 | 1.457 | 0.8224 |

Table 2. Dispersion value at $1.55 \mu \mathrm{~m}$ wavelength and dispersion slope over the C band for the PCFs found by the three methods with the first cost function.

| Method | $D\left(\mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}\right)$ | $S\left(\mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}\right)$ |
| :-- | :--: | :--: |
| DE | -4.1 | 0.014285 |
| EDA | 0.35 | 0.114285 |
| DE/EDA | -0.55 | 0.085714 |

![img-3.jpeg](img-3.jpeg)

Figure 4. Dispersion characteristics as a function of wavelength for the PCFs found by three methods with the first cost function.
![img-4.jpeg](img-4.jpeg)

Figure 5. Transversal field intensity distribution for the guiding mode of a SMPCF found by DE/EDA algorithm with $\Lambda=2.276 \mu \mathrm{~m}, d=0.8224 \mu \mathrm{~m}$ and $N=5, n=1.457$ at (a) $1.53 \mu \mathrm{~m}$, (b) $1.55 \mu \mathrm{~m}$ and (c) $1.565 \mu \mathrm{~m}$ wavelengths. (The color version of this figure is included in the online version of the journal.)

Finally, a new population is created with 100 individuals. Again the GA algorithms are performed with this population and the best individual with the minimum cost function is selected as the solution. In this phase, the number of generations is made equal to 1000 . In order to make a fair comparison, we repeat the process several times for each cost function of these algorithms.

### 5.1. Cost function with dispersion

The first cost function is the summation of absolute dispersion over all $\lambda$ (wavelength) in the specified wavelength range of optimization ( C band). The results of the optimization are summarized in Tables 1 and 2. Table 1 shows the best individuals achieved by the algorithms and the dispersion characteristics are depicted in Table 2 and also in Figure 4. As can be seen, the minimum value of dispersion at $1.55 \mu \mathrm{~m}$ wavelength is for the PCF (best solution) achieved by the EDA method whereas the best PCF found by the DE algorithm has the minimum dispersion slope. However, it is seen that overall the hybrid method, DE/EDA performs better than these two algorithms. The transversal field intensity distribution for the guiding mode of the PCF found by the DE/EDA algorithm, at $1.53,1.55$ and $1.565 \mu \mathrm{~m}$ wavelengths is shown in Figure 5. As can be seen, the light is guided inside the core of the structure. Also, the effective index profile and the dispersion characteristics of the PCF found by this method are shown in Figure 6.

### 5.2. Cost function with dispersion and dispersion slope

The second cost function is the summation of the absolute dispersions over all $\lambda$ multiplied by the summation of absolute dispersion slope over all $\lambda$ in the specified range of optimization. Tables 3 and 4 summarize the results of the optimization. Table 3 shows the best individuals achieved by the algorithms. The dispersion characteristics are depicted in Table 4 and also in Figure 7.

It is obvious that the DE/EDA performs better than these two algorithms although the solution found by DE has dispersion slope characteristics slightly superior than that of DE/EDA. The transversal field intensity distribution for the guiding mode of the PCF found by the DE/EDA algorithm, at $1.53,1.55$ and $1.565 \mu \mathrm{~m}$ wavelengths is shown in Figure 8. The results show that the light is confined inside the core of the structure. The effective index profile and the dispersion characteristics of the fiber achieved by the DE/EDA method are also depicted in Figure 9.

### 5.3. Discussion

To summarize, we have shown that for this specific optimization problem, the DE/EDA algorithm performs better than both the DE and the EDA algorithms. Although, there are some reports on the
![img-5.jpeg](img-5.jpeg)

Figure 6. (a) Refractive index profile and (b) dispersion characteristics as a function of wavelength for the PCF found by the DE/EDA algorithm with $\Lambda=2.276 \mu \mathrm{~m}, d=0.8224 \mu \mathrm{~m}$ and $N=5, n=1.457$. (The color version of this figure is included in the online version of the journal.)

Table 3. The solution (PCFs parameters) found by the three methods with the second cost function.

| Method | $N$ | $\Lambda(\mu \mathrm{~m})$ | $n$ | $d(\mu \mathrm{~m})$ |
| :-- | :-- | :-- | :-- | :-- |
| DE | 9 | 2.5 | 1.44 | 0.7482 |
| EDA | 6 | 2.733 | 1.442 | 0.8894 |
| DE/EDA | 7 | 2.713 | 1.44 | 0.7596 |

design of ultra low and ultra flattened dispersion photonic crystal fibers, these fibers will not provide single mode operation over the C communication band [23-26]. A related work that has used the simple GA was performed by Kerrinckx et al. [7], in which, each individual has two chromosomes $[\Lambda, r]$. The best solution they demonstrated, was a nine ring structure

Table 4. Dispersion value at $1.55 \mu \mathrm{~m}$ wavelength and dispersion slope over C band for the PCFs found by the three methods with the second cost function.

| Method | $D\left(\mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}\right)$ | $S\left(\mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}\right)$ |
| :-- | :--: | :--: |
| DE | -4.58 | 0.015714 |
| EDA | 0.4 | 0.057142 |
| DE/EDA | 0.22 | 0.025114 |

![img-6.jpeg](img-6.jpeg)

Figure 7. Dispersion characteristics as a function of wavelength for the PCFs found by the three methods with the second cost function.
of PCF with the pitch $\Lambda=2.35 \mu \mathrm{~m}$ and the diameter $r=0.66 \mu \mathrm{~m}$. The dispersion and dispersion slope of this PCF are $2.5 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ at $1.55 \mu \mathrm{~m}$ wavelength and $0.03575 \mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}$, respectively. In another similar work the chromatic dispersion of $0.8 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ at $1.55 \mu \mathrm{~m}$ wavelength was obtained for a nine ring structure with the following parameters: $\Lambda=2.59 \mu \mathrm{~m}$ and $r=0.29 \mu \mathrm{~m}[27]$.

In this case, a PCF with the dispersion of $0.22 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ at $1.55 \mu \mathrm{~m}$ wavelength and dispersion slope of $0.025114 \mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}$ over the C communication band has been designed. So, it is revealed that the DE/EDA method is a powerful tool for optimum design of PCFs.

## 6. Future work

In further work, we are going to combine EDA with the hill climbing (HC) algorithm for tackling this optimization problem. Also we will try to present the cost function using a combination of dispersion and loss characteristics in order to design an optimum photonic crystal fiber. Furthermore, we will attempt to demonstrate that the number of the individuals' chromosomes (PCF parameters) can be increased to achieve the PCF structure with better dispersion characteristics.

## 7. Conclusion

In this paper we have applied a novel design technique using DE/EDA to achieve a PCF with desirable properties. The simulation results demonstrate that DE/EDA outperforms the DE algorithm and the EDA methods in the optimization problem of the
![img-7.jpeg](img-7.jpeg)

Figure 8. Transversal field intensity distribution for the guiding mode of a SMPCF found by the DE/EDA algorithm with $\Lambda=2.713 \mu \mathrm{~m}, d=0.7596 \mu \mathrm{~m}$ and $N=7, n=1.44$ at (a) $1.53 \mu \mathrm{~m}$, (b) $1.55 \mu \mathrm{~m}$ and (c) $1.565 \mu \mathrm{~m}$ wavelengths. (The color version of this figure is included in the online version of the journal.)

![img-8.jpeg](img-8.jpeg)

Figure 9. (a) Refractive index profile and (b) dispersion characteristics as a function of wavelength for the PCF found by the DE/ EDA algorithm with $\Lambda=2.713 \mu \mathrm{~m}, d=0.7596 \mu \mathrm{~m}$ and $N=7, n=1.44$. (The color version of this figure is included in the online version of the journal.)

PCF structure. In order to determine the dispersion properties of the structure and consequently the cost function, the FDFD solver is applied. The optimized PCF exhibits a dispersion of $0.22 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ at $1.55 \mu \mathrm{~m}$ wavelength with a variance of $\pm 0.4 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ over the C communication band and nearly zero dispersion slope. With further optimization of the structure and increasing the number of individual's chromosomes in the DE/EDA method, dispersion characteristics can be improved still further.

## References

[1] Russell, P.S.J. J. Light Wave Technol. 2006, 24, 4729-4749.
[2] Calo, G.; D'Orazio, A.; De Sario, M.; Mescia, L.; Petruzzelli, V.; Prudenzano, F. Presented at the 7th International Conference on Transport Optical Networks, Barcelona, July 3-7, 2005.
[3] Zhou, J.; Tajima, K.; Nakajima, K.; Kurokawa, K.; Fukai, C.; Matsui, T.; Sankawa, I. Opt. Fiber Technol. 2005, 11, 101-110.
[4] Pourmahyabadi, M.; Mohammad Nejad, S. Optimal Confinement Loss Reduction in Photonic Crystal Fiber with Ultra-Flattened Dispersion. Symposium on High Capacity Optical Networks \& Enabling Technologies, HONET 08, Penang, Malaysia, November 18-20, 2008.
[5] Hoo, Y.L.; Jin, W.; Ju, J.; Ho, H.L.; Wang, D.N. Opt. Commun. 2004, 242, 327-332.
[6] Chen, M.Y. Opt. Commun. 2006, 266, 151-158.
[7] Kerrinckx, E.; Bigot, L.; Douay, M.; Quiquempois, Y. Opt. Express 2004, 12, 1990-1995.
[8] Poletti, F.; Finazzi, V.; Monro, T.M.; Broderick, N.G.R.; Tse, V.; Richardson, D.J. Opt. Express 2005, 13, 3728-3736.
[9] Shahoei, H.; GhafooriFard, H.; Rostami, A.; Shahoei, W. Design of Flattened-Low Dispersion MII Type Optical Fiber by using DE Algorithm. Tarbiat Modares University, Tehran, Iran, May 2008.
[10] Sun, J.; Zhang, Q.; Tsang, E.P.K. Informat. Sci. 2005, 169, 249-262.
[11] Tsutsui, S.; Pelikan, M.; Goldberg, D.E. Evolutionary Algorithm Using Marginal Histogram Models in Continuous Domain. Proceedings of the 2001 Genetic and Evolutionary Computation Conference Workshop, San Francisco, CA, 2001.
[12] Rudlof, S.; Koppen, M. Stochastic Hill-Climbing with Learning by Vectors of Normal Distributions, Berlin, December 1997.
[13] Zhu, Z.; Brown, T.G. Opt. Express 2002, 10, 853-864.
[14] Shuqin, L.; Zhi, W.; Guobin, R.; Shuisheng, J. Opt. Fiber Technol. 2005, 11, 34-45.
[15] Ping Yu, C.; Chun Chang, H. Opt. Quantum Electron. 2004, 36, 145-163.
[16] Yu, C.P.; Chang, H.C. Opt. Express 2004, 12, 2795-2809.
[17] Pourmahyabadi, M.; Mohammad Nejad, S. Numerical Investigation and Optimization of a Photonic Crystal Fiber with Ultra-Low Confinement Loss and Ultra-Flattened Dispersion. The 6th International Symposium on Communication Systems, Networks and Digital Signal Processing, CSNDSP, Graz, Austria, July 2008.
[18] Pourmahyabadi, M.; Mohammad Nejad, S. Numerical Analysis of Dispersion Properties of

Heterostructured Photonic Crystal Fibers. 4th IEEE UZ Regional Chapter International Conference in Central Asia on Internet, The Next Generation of Mobile, Wireless and Optical Communications Networks, Uzbekistan, September 2008.
[19] Selleri, S.; Cucinotta, A.; Foroni, M.; Poli, F.; Bottacini, M. Proc. SPIE 2005, 5950, 59500U.
[20] Pourmahyabadi, M.; Mohammad Nejad, S. Design of Single Mode Photonic Crystal Fibers with Low-Loss and Flattened Dispersion at $1.55 \mu \mathrm{~m}$ Wavelength. 4th International Symposium on High Capacity Optical Networks and Enabling Technologies, Dubai, UAE, November 18-20, 2007.
[21] Zhu, Z.; Brown, T.G. Opt. Express 2002, 10, 853-864.
[22] Guo, S.; Wu, F.; Albin, S. Opt. Express 2004, 12, 1741-1746.
[23] Wu, T.L.; Chao, C.H. IEEE Photon. Technol. Lett. 2005, 17, 67-69.
[24] Poli, F.; Cucinotta, A.; Selleri, S.; Bouk, A.H. IEEE Photon. Technol. Lett. 2004, 16, 1065-1067.
[25] Ferrando, A.; Silvestre, E.; Andres, P. Opt. Express 2001, 9, 687-697.
[26] Liu, Z.L.; Liu, X.D.; Li, S.G.; Li, G.Y.; Wang, W.; Hou, L.T. Opt. Commun. 2007, 272, 92-96.
[27] Reeves, W.H.; Knight, J.C.; Russell, P.St.J. Opt. Express 2002, 10, 609-613.