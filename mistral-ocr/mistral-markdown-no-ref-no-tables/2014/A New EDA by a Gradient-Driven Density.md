# A New EDA by a Gradient-Driven Density 

Ignacio Segovia Domínguez, Arturo Hernández Aguirre, and S. Ivvan Valdez<br>Center for Research in Mathematics, Guanajuato, México<br>\{ijsegoviad,artha,ivvan\}@cimat.mx


#### Abstract

This paper introduces the Gradient-driven Density Function $\left(\nabla_{d} \mathrm{D}\right)$ approach, and its application to Estimation of Distribution Algorithms (EDAs). In order to compute the $\nabla_{d} \mathrm{D}$, we also introduce the Expected Gradient Estimate (EGE), which is an estimation of the gradient, based on information from other individuals. Whilst EGE delivers an estimation of the gradient vector at the position of any individual, the $\nabla_{d} \mathrm{D}$ delivers a statistical model (e.g. the normal distribution) that allows the sampling of new individuals around the direction of the estimated gradient. Hence, in the proposed EDA, the gradient information is inherited to the new population. The computation of the EGE vector does not need additional function evaluations. It is worth noting that this paper focuses in black-box optimization. The proposed EDA is tested with a benchmark of 10 problems. The statistical tests show a competitive performance of the proposal.


Keywords: Gradient estimation, Estimation of Distribution Algorithm.

## 1 Introduction

Several Evolutionary Algorithms search the global optimum by simulations from statistical models; e.g. EDAs, ES, etc. The evolutionary computation community has been making a large effort to add new information into statistical models in order to improve the search process. There are several approaches to add search directions into statistical models [3] [2]. In this context, some popular algorithms have demonstrated the feasibility of this idea (e.g. CMA-ES, NES, etc.). This paper introduces contributions in this trend by building density functions based on gradient estimates: Gradient-driven densities. The proposal developed here only use the function evaluations gathered from the population to build gradient estimates on fixed individuals. Hence, the algorithm does not require any extra evaluation of function. The first-order information is an important source of promising directions to improve any individual. For that reason, a Gradientdriven Density Function $\left(\nabla_{d} \mathrm{D}\right)$ is introduced. Any simulation from $\nabla_{d} \mathrm{D}$ might produce samples around the gradient estimation. Hence, the search process focuses in promising orientations. These novel ideas are merged to create a new EDA. As a consequence of the gradient estimation, the proposed EDA generates new individuals towards promising regions. The organization of the paper is as follows. Section 2 introduces the Expected Gradient Estimation method. Section 3 develops the Gradient-driven Density framework. Section 4 presents the

EDA based on Gradient-driven Density Functions. Section 5 is devoted to test the proposed EDA against others algorithms from the state of the art. Finally, Section 6 provides some concluding remarks.

# 2 The Gradient Estimation 

The gradient vector $\nabla \mathcal{F}(\boldsymbol{x})$ models the local greatest rate of increase by specifying a direction and magnitude at $\boldsymbol{x}$. Since the information about the problem comes from scattered samples on the search space, a neighborhood for an individual might be choosen. For that reason, this paper considers that any gradient estimate for individual $\boldsymbol{x}^{(i)}$ requires itself and its neighborhood, i.e. a set of individuals $\mathcal{N}_{\boldsymbol{x}^{(i)}}=\left\{\boldsymbol{x}^{\left(i_{1}\right)}, \boldsymbol{x}^{\left(i_{2}\right)}, \ldots, \boldsymbol{x}^{\left(i_{k}\right)}, \ldots, \boldsymbol{x}^{\left(i_{r-1}\right)}, \boldsymbol{x}^{\left(i_{r}\right)}\right\}$ from the population or gathered from previous generations, where $i \neq i_{1} \neq \ldots \neq i_{k} \neq \ldots \neq i_{r}$ and $r$ is the neighborhood size. Furthermore, any criterion to select the neighborhood can be used. Also, notice that this method permits to compute a gradient estimate for each individual only by using known information about the problem. The fitness values of $\left\{\boldsymbol{x}^{(i)}, \ldots, \boldsymbol{x}^{\left(i_{1}\right)}, \ldots, \boldsymbol{x}^{\left(i_{r}\right)}\right\}$ provide knowledge about the problem. Hence, that information can be used to estimate the gradient vector of $\boldsymbol{x}^{(i)}$. The common approach approximates the gradient by fitting a hyperplane in $d+1$ dimensions, where $d$ is the dimension size of $\boldsymbol{x}^{(i)}$. Therefore, the estimation of gradient might be tackled by the ordinary least square method [4]. Despite the fact that the previous technique creates an intuitive gradient approximation, in many contexts it might be inadequate (e.g. there are not enough samples to create the overdetermined system, etc). This section presents a new gradient estimation based on two mathematical concepts: the directional derivative and the statistical expectation.
Definition 1. Let $\mathcal{N}_{\boldsymbol{x}^{(i)}}=\left\{\boldsymbol{x}^{\left(i_{1}\right)}, \boldsymbol{x}^{\left(i_{2}\right)}, \ldots, \boldsymbol{x}^{\left(i_{k}\right)}, \ldots, \boldsymbol{x}^{\left(i_{r-1}\right)}, \boldsymbol{x}^{\left(i_{r}\right)}\right\}$ be the neighbors of individual $\boldsymbol{x}^{(i)}$, from the population. Then the Expected Gradient Estimate for $\boldsymbol{x}^{(i)}$ is defined by

$$
\widehat{\nabla \mathcal{F}}\left(\boldsymbol{x}^{(i)}\right)=\frac{1}{r} \sum_{k=1}^{r} \frac{\mathcal{F}\left(\boldsymbol{x}^{\left(i_{k}\right)}\right)-\mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{\left\|\boldsymbol{x}^{\left(i_{k}\right)}-\boldsymbol{x}^{(i)}\right\|^{2}}\left(\boldsymbol{x}^{\left(i_{k}\right)}-\boldsymbol{x}^{(i)}\right)
$$

where $i \neq i_{1} \neq \ldots \neq i_{k} \neq \ldots \neq i_{r}, r$ is the neighborhood size and $\mathcal{F}(\cdot)$ computes the fitness value.

In order to justify equation (1), let us assume that $\boldsymbol{x}^{\left(i_{k}\right)}$ exists on the line defined by the true gradient $\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)$. This means

$$
\frac{\boldsymbol{x}^{\left(i_{k}\right)}-\boldsymbol{x}^{(i)}}{\left\|\boldsymbol{x}^{\left(i_{k}\right)}-\boldsymbol{x}^{(i)}\right\|}= \pm \frac{\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{\left\|\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)\right\|}
$$

Since the orientation depends on the sign, each case will be examined separately. Let $\boldsymbol{u}_{+}$and $\boldsymbol{u}_{-}$be two normalized vectors as follows

$$
\boldsymbol{u}_{+}=\frac{\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{h}, \quad \boldsymbol{u}_{-}=-\frac{\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{h}
$$

where $h=\left\|\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)\right\|$; please note $\boldsymbol{u}_{+}$has the same direction as the true gradient, opposite to $\boldsymbol{u}_{-}$. From the well-known directional derivative definition and its properties observe that

$$
\begin{aligned}
& \left(\lim _{h \rightarrow 0} \frac{\mathcal{F}\left(\boldsymbol{x}^{(i)}+h \boldsymbol{u}_{+}\right)-\mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{h}\right) \boldsymbol{u}_{+}=\left\|\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)\right\| \frac{\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{\left\|\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)\right\|}=\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right) \\
& \left(\lim _{h \rightarrow 0} \frac{\mathcal{F}\left(\boldsymbol{x}^{(i)}+h \boldsymbol{u}_{-}\right)-\mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{h}\right) \boldsymbol{u}_{-}=-\left\|\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)\right\| \frac{-\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{\left\|\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)\right\|}=\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)
\end{aligned}
$$

This is important because similar connections can be found just by considering two individuals, mainly due to the assumption in equation (2); for instance

$$
\begin{gathered}
\left(\lim _{l \rightarrow 0} \frac{\mathcal{F}\left(\boldsymbol{x}^{(i)}+l \cdot \boldsymbol{u}\right)-\mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{l}\right) \boldsymbol{u}=\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right) \\
\boldsymbol{u}=\frac{\boldsymbol{x}^{\left(i_{k}\right)}-\boldsymbol{x}^{(i)}}{\left\|\boldsymbol{x}^{\left(i_{k}\right)}-\boldsymbol{x}^{(i)}\right\|}, \quad l=\left\|\boldsymbol{x}^{\left(i_{k}\right)}-\boldsymbol{x}^{(i)}\right\|
\end{gathered}
$$

Equation (4) presents a different manner to remake the gradient function. Notice that although the derivative is unavailable, an approximation by finite differences can be considered. It leads us to introduce a gradient estimate for $\boldsymbol{x}^{(i)}$, just given one neighbor, as follows

$$
\boldsymbol{g}^{\left(i_{k}\right)}=\left(\frac{\mathcal{F}\left(\boldsymbol{x}^{(i)}+l \boldsymbol{u}\right)-\mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{l}\right) \boldsymbol{u}=\frac{\mathcal{F}\left(\boldsymbol{x}^{\left(i_{k}\right)}\right)-\mathcal{F}\left(\boldsymbol{x}^{(i)}\right)}{\left\|\boldsymbol{x}^{\left(i_{k}\right)}-\boldsymbol{x}^{(i)}\right\|^{2}}\left(\boldsymbol{x}^{\left(i_{k}\right)}-\boldsymbol{x}^{(i)}\right)
$$

However, there is no chance to ensure that $\boldsymbol{x}^{\left(i_{k}\right)}$ is on the line defined by the true gradient, because the neighbors come from an unknown hidden random process. Hence, the difference between fitness values is also a random variable. Therefore, each estimate $\boldsymbol{g}^{\left(i_{k}\right)}$ arises from a random process. Please assume that $\mathcal{P}$ is the hidden uncertainty model which describes the behavior of outcomes $\boldsymbol{g}^{\left(i_{k}\right)}$. So, any instance of random variable $\boldsymbol{g}^{(i)} \sim \mathcal{P}$ is an outcome $\boldsymbol{g}^{\left(i_{k}\right)}$. A representative vector for the hidden model can be computed by the statistical expectation. Moreover, the $E\left(\boldsymbol{g}^{(i)}\right)$ can be approximated as follows

$$
E\left(\boldsymbol{g}^{(i)}\right)=\int_{\mathbb{R}^{d}} \boldsymbol{g}^{(i)} \mathcal{P} d \boldsymbol{g}^{(i)} \approx \frac{1}{r} \sum_{k=1}^{r} \boldsymbol{g}^{\left(i_{k}\right)}
$$

which is the Expected Gradient Estimate, equation (1).
To the best of our knowledge, the EGE developed above has not been addressed in literature. However, further theoretical study is necessary to verify its relationship with other approaches [1]. In order to empirically contrast the approximated orientations of EGE versus the usual approximation by hyperplane, a fixed population and a gradient estimation on each individual will be considered. An ideal population, at first generation, must cover the search domain

evenly; thus in this experiment the population is built by the Halton quasirandom sequence, from Matlab ${ }^{\circledR}$ with default options. Also, please consider the Sphere problem, the neighborhood size $r=d+1$ and the $r$ closer individuals to $\boldsymbol{x}^{(i)}$ (neighborhood, according to the Euclidean distance). Below there is an angle-comparison between $\widehat{\nabla \mathcal{F}}\left(\boldsymbol{x}^{(i)}\right)$ and $\nabla \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)$. So, the measurement vector of angles $\boldsymbol{\alpha}=\left\{\alpha^{(1)}, \ldots, \alpha^{(i)}, \ldots, \alpha^{(N)}\right\}$ includes an angle value for each individual, where $N$ is the population size. Figure 1 shows the histograms of orientation by
![img-0.jpeg](img-0.jpeg)

Fig. 1. Histograms of orientation in Sphere problem, Expected Gradient Estimation (EGE, solid line) versus hyperplane approach by ordinary least square (HLS, dashed line). (a) 10 dimensions: HLS has a median value of 1.30488 and EGE has a median value of 0.627966 . (b) 30 dimensions: HLS has a median value of 1.48743 and EGE has a median value of 0.617965 . EGE shows better performance.
setting $r=d+1, N=10 d$ and $x_{k} \in[-600,300]$; where $d$ is the dimension size. Notice that the EGE has more chances to compute better oriented vectors than the hyperplane approach for higher dimensions. In addition, the median values support the graphic observation. Here, the neighborhood size $r=d+1$ was chosen from literature [4]. In summary, the results suggest that the EGE might outperform previous gradient approximations used in evolutionary computation.

# 3 The Gradient-Driven Density 

Each generation has three different data sets: the individuals $\left\{\boldsymbol{x}^{(i)}\right\}$, the function evaluations $\left\{\mathcal{F}\left(\boldsymbol{x}^{(i)}\right)\right\}$ and the estimations of the gradient estimates $\left\{\widehat{\nabla \mathcal{F}}\left(\boldsymbol{x}^{(i)}\right)\right\}$. These provide distinct information about the function and the algorithms' behavior. Several stochastic optimization approaches (e.g. ES, EDA) aim to build a multivariate density function on optimum locations; or at least in better regions than the current ones. This section will begin with the same goal for a fixed individual from the population. Therefore, there might exist a multivariate density function $\mathrm{p}(\boldsymbol{x}, \boldsymbol{\theta})$ for $\boldsymbol{x}^{(i)}$ based on its gradient estimate $\widehat{\nabla} \mathcal{F}\left(\boldsymbol{x}^{(i)}\right)$, which is able to simulate better individuals than the present $\boldsymbol{x}^{(i)}$. Due to the fact that only two vectors will be used here, there is no chance to ensure that all simulations improve the current fitness value $\mathcal{F}\left(\boldsymbol{x}^{(i)}\right)$. However, the density modeling

can be modified to take advantage of the gradient estimate by developing a new estimation of parameters, updating the original parameters, improving the simulation, etc. For this reason, definition 2 introduces the $\nabla_{d} \mathrm{D}$ from the individual perspective.

Definition 2. Let $\boldsymbol{z}$ be an individual in the domain space and $G(\boldsymbol{z})$ a function which computes its gradient estimate. The density function $\mathrm{p}(\boldsymbol{x}, \boldsymbol{\theta})$ is a Gradient-driven Density $\left(\nabla_{d} D\right)$ for individual $\boldsymbol{z}$ if the following two conditions are satisfied:

1) The multivariate density $\mathrm{p}(\boldsymbol{x}, \boldsymbol{\theta})$ is a unimodal function,
2) $\frac{G(\boldsymbol{z})}{\|G(\boldsymbol{z})\|}=\frac{\nabla \mathrm{p}(\boldsymbol{z}, \boldsymbol{\theta})}{\|\nabla \mathrm{p}(\boldsymbol{z}, \boldsymbol{\theta})\|}$.

The conditions set up above allow a wide range of future proposals. The first condition permits a single mass of probability towards promising regions. The random search must be led by $G(\boldsymbol{z})$ because it is orienting towards promising regions. In fact, the second condition just allows density functions which $\nabla \mathrm{p}(\boldsymbol{z}, \boldsymbol{\theta})$ has the same direction as the gradient estimate $G(\boldsymbol{z})$. There are many ways to build a $\nabla_{d}$ Density. Below, a suitable technique based on multivariate calculus and the angular discrepancy are introduced .

Definition 3. Let $\mathrm{p}(\boldsymbol{x}, \boldsymbol{\theta})$ be a multivariate unimodal density. In order to ensure that $\mathrm{p}(\boldsymbol{x}, \boldsymbol{\theta})$ is a $\nabla_{d}$ Density, a parameter estimation on $\boldsymbol{\theta}$ must be performed. The minimum angle estimation solves this by,

$$
\widehat{\boldsymbol{\theta}}=\max _{\boldsymbol{\theta}} \frac{G(\boldsymbol{z})^{t} \nabla \mathrm{p}(\boldsymbol{z}, \boldsymbol{\theta})}{\|G(\boldsymbol{z})\|\|\nabla \mathrm{p}(\boldsymbol{z}, \boldsymbol{\theta})\|}
$$

Notice that the minimum angle estimation solves the parameter estimation of $\boldsymbol{\theta}$ by maximizing the dot product of two normalized vectors. It is a natural way because the angle between two vectors is related to the dot product. In addition, even if finding the solution of (8) is not possible, a good approximation can be discovered. The rest of this section uses the previous definition to build $\nabla_{d}$ densities. Please assume that $\mathrm{p}(\boldsymbol{x}, \boldsymbol{\theta})$ is a multivariate normal density and $\nabla \mathrm{p}(\boldsymbol{z}, \boldsymbol{\theta})$ its gradient function. Also, let

$$
\boldsymbol{z}_{G}=\frac{G(\boldsymbol{z})}{\|G(\boldsymbol{z})\|}
$$

be the normalized gradient estimate of individual $\boldsymbol{z}$. The estimation method must calculate the mean vector $\boldsymbol{\mu}$ and the covariance matrix $\boldsymbol{\Sigma}$ which satisfy definition 2. Then, the statistical parameters can be found by solving

$$
<\boldsymbol{\mu}^{n e w}, \boldsymbol{\Sigma}^{n e w}>=\max _{<\boldsymbol{\mu}, \boldsymbol{\Sigma}>} \frac{z_{G}^{t}\left[\mathcal{N}(\boldsymbol{z} ; \boldsymbol{\mu}, \boldsymbol{\Sigma}) \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z})\right]}{\left\|\mathcal{N}(\boldsymbol{z} ; \boldsymbol{\mu}, \boldsymbol{\Sigma}) \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z})\right\|}
$$

Let us address this problem separately for each parameter. By taking the derivative with respect to $\boldsymbol{\mu}$ and setting it equal to zero, we found the equation

$$
\left\|\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z})\right\|^{2} \boldsymbol{\Sigma}^{-t} \boldsymbol{z}_{G}-\boldsymbol{z}_{G}^{t} \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z}) \boldsymbol{\Sigma}^{-t} \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z})=0
$$

In a similar way, by taking the derivative with respect to $\boldsymbol{\Sigma}^{-1}$ and setting it equal to zero, we found the equation

$$
\left\|\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z})\right\|^{2} \boldsymbol{z}_{G}(\boldsymbol{\mu}-\boldsymbol{z})^{t}-\boldsymbol{z}_{G}^{t} \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z}) \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z})(\boldsymbol{\mu}-\boldsymbol{z})^{t}=0
$$

Notice that both are nonlinear matrix equations! In addition, the problem (12) is a constraint equation, since $\boldsymbol{\Sigma}$ needs to be a symmetric positive semidefinite matrix. So, it leads us to solve two more complex optimization problems than the original one. However, a few interesting facts arise by inspecting equations (10)-(12), when $\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z})=\boldsymbol{z}_{G}$ : Equation (10) reaches its maximum value, i.e. 1 ; and Equations (11) and (12) are fulfilled. Furthermore, notice that $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are closely related. In fact, there are an infinite number of symmetric semipositive definite matrices $\boldsymbol{\Sigma}$ able to fulfill $\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z})=\boldsymbol{z}_{G}$. This certainly means that the nonlinear system has an infinity number of solutions. However, straightforward solutions can be found by these observations. By assuming the matrix $\boldsymbol{\Sigma}$ is fixed and solving for the mean vector in $\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}-\boldsymbol{z})=\boldsymbol{z}_{G}$ a new formula is found:

$$
\boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}^{\text {new }}-\boldsymbol{z}\right)=\boldsymbol{z}_{G} \quad \therefore \quad \boldsymbol{\mu}^{\text {new }}=\boldsymbol{z}+\boldsymbol{\Sigma} \boldsymbol{z}_{G}
$$

Given a fixed covariance matrix, its related mean vector can be computed by (13). Furthermore, there is a unique mean vector for a given $\boldsymbol{\Sigma}$. On the contrary, given a fixed mean vector, there is a number of infinite possible covariance matrices. Definition 4 introduces a $\nabla_{d}$ Density based on the previous analysis.

Definition 4. Let $\boldsymbol{\Sigma}_{0}$ be a fixed covariance matrix. Then the $\nabla_{d}$ Normal $\left(\nabla_{d} \mathcal{N}\right)$ has parameters

$$
\boldsymbol{\mu}_{g}=\boldsymbol{z}+\boldsymbol{\Sigma}_{0} \boldsymbol{z}_{G} \quad \text { and } \quad \boldsymbol{\Sigma}_{g}=\boldsymbol{\Sigma}_{0}
$$

Notice that, simulations from the proposed densities will produce samples in a similar direction as the gradient vector (or gradient estimate). The next section applies the developed Gradient-driven densities in evolutionary computation.

# 4 The Gradient-Driven Density in EDAs 

The Estimation of Distribution Algorithm (EDA) aims to simulate new individuals on regions near optimum locations, preferably close to the global optimum. Interesting optimization methods might be developed by considering the $\nabla_{d} \mathrm{D}$ technique into EDAs. The EDA fits a target statistical model. A common one is the multivariate normal function [5]. This section introduces an EDA, based on

this density function, by computing the expectation and variance of a multivariate Gaussian mixture model. Please consider a mixture of two models: the empirical normal density and a Gradient-driven Density. The first one promotes the exploitation whilst the second one allows predictive samples on possible promising regions (exploration). In order to build a simpler model, the mixture of densities is approximated by a unique Multivariate Gaussian model 6. The target density for the proposed EDA is built by $\mathcal{N}\left(\boldsymbol{\mu}^{\text {new }}, \boldsymbol{\Sigma}^{\text {new }}\right)$, where:

$$
\begin{aligned}
\boldsymbol{\mu}^{\text {new }} & =E(E(\boldsymbol{X} \mid \vartheta))=(1-\beta) \widehat{\boldsymbol{\mu}}+\beta \boldsymbol{\mu}_{g} \\
\boldsymbol{\Sigma}^{\text {new }} & =\operatorname{Var}(E(\boldsymbol{X} \mid \vartheta))+E(\operatorname{Var}(\boldsymbol{X} \mid \vartheta))=(1-\beta) \widehat{\boldsymbol{\Sigma}}+\beta \boldsymbol{\Sigma}_{g} \\
& +(1-\beta)\left(\widehat{\boldsymbol{\mu}}-\boldsymbol{\mu}^{\text {new }}\right)\left(\widehat{\boldsymbol{\mu}}-\boldsymbol{\mu}^{\text {new }}\right)^{t}+\beta\left(\boldsymbol{\mu}_{g}-\boldsymbol{\mu}^{\text {new }}\right)\left(\boldsymbol{\mu}_{g}-\boldsymbol{\mu}^{\text {new }}\right)^{t}
\end{aligned}
$$

and $\beta \in[0,1]$ is the associated weight to the $\nabla_{d} \mathrm{D}$. Also, $\beta$ controls the amount of credibility on each model. Please note that $\beta=0$ produces the empirical density and $\beta=1$ yields the other one. In addition, since the simulation method might build samples outside the search domain, a re-insertion technique is added, line 10 of algorithm 2. Let $\gamma_{k}=l_{k}^{\text {upper }}-l_{k}^{\text {lower }}$ be the domain length in dimension $k$, where $l_{k}^{\text {upper }}$ and $l_{k}^{\text {lower }}$ are the upper bound and lower bound in dimension $k$. For each dimension, the new sample $\boldsymbol{y}^{(i)}=\left(y_{1}^{(i)}, \cdots, y_{k}^{(i)}, \cdots, y_{D}^{(i)}\right)$ is tested/replaced by

- if $y_{k}^{(i)}>l_{k}^{\text {upper }}$ then $a=\left(y_{k}^{(i)}-l_{k}^{\text {upper }}\right) / \gamma_{k}$ and $y_{k}^{(i)}=l_{k}^{\text {upper }}-\gamma_{k}(a-\lfloor a\rfloor)$
- if $y_{k}^{(i)}<l_{k}^{\text {lower }}$ then $a=\left(l_{k}^{\text {lower }}-y_{k}^{(i)}\right) / \gamma_{k}$ and $y_{k}^{(i)}=l_{k}^{\text {lower }}+\gamma_{k}(a-\lfloor a\rfloor)$
which ensure any new individual is inside the domain. The algorithm 2 describes the proposed EDA led by a Gradient-driven Density (EDA-LGD). Because of the importance of the gradient estimate for the $\nabla_{d} \mathrm{D}$, this proposal just computes the gradient of the best individual using the historical best individuals from previous generations. So, if at generation (t) a new best individual $\boldsymbol{x}^{\text {best }}$ is found, then $\boldsymbol{x}^{\text {best }}$ replaces the worst individual in $P_{\text {best }}$ and the next gradient estimate is over $\boldsymbol{x}^{\text {best }}$ with the neighborhood $\left\{P_{\text {best }}\left\backslash \boldsymbol{x}^{\text {best }}\right\}\right.$. Then two populations are saved: the usual population $P o b_{t}$ at each generation $(t)$ and the historically best individuals $P_{\text {best }}$; in algorithm 2 the first one has $N$ individuals meanwhile the second one has $d+2$ individuals.


# 5 Experiment 

This section contrasts the proposed EDA against two known Evolutionary Algorithms based on multivariate densities: CMA-ES [3] and xNES [2]. Each algorithm runs in 10 benchmark problems, see Table 1 In order to make a fair comparison, the code was downloaded from authors homepage and 50 runs were performed. Also, the initial center of densities was chosen randomly in the search domain with an initial variance according to the domain ( $1 / 3$ of this). The three algorithms only have two stopping conditions: maximum number of evaluations of function is reached $\left(10^{4} \times d\right)$, or target error smaller than $10^{-8}$,

1: $t \leftarrow 0, \beta \leftarrow 0.5, N \leftarrow\left\lceil 4+\left(1+d^{0.7}\right)\right], M \leftarrow 2 *\lfloor\log (d)\rfloor+1, r \leftarrow d+1$
2: $\operatorname{POb}_{t} \leftarrow \mathcal{U}$ (Domain), compute $\mathcal{F}\left(\boldsymbol{x}^{(i)}\right)$, find the $\boldsymbol{x}^{\text {best }} \quad \triangleright$ First population
3: $P_{\text {best }} \leftarrow$ Best $r+2$ individuals from $\operatorname{POb}_{t} \quad \triangleright$ Historical best population
4: while (Stop condition is not reached) do
5: $\quad$ Gradient estimate $G\left(\boldsymbol{x}^{\text {best }}\right)=\widehat{\nabla \mathcal{F}}\left(\boldsymbol{x}^{\text {best }}\right)$ with neighborhood $\left\{P_{\text {best }} \backslash \boldsymbol{x}^{\text {best }}\right\}$
6: $\quad$ Normalized vector $\boldsymbol{x}_{G}^{\text {best }}$ by (9) or negative for minimization
7: $\quad$ Empirical estimation of $\widehat{\boldsymbol{\mu}}$ and $\widehat{\boldsymbol{\Sigma}}$. Initial covariance $\boldsymbol{\Sigma}_{0}=\operatorname{diag}(\operatorname{diag}(\widehat{\boldsymbol{\Sigma}}))$
8: $\quad$ Parameters $\boldsymbol{\mu}_{g}$ and $\boldsymbol{\Sigma}_{g}$ by definition 4. Parameters $\boldsymbol{\mu}^{\text {new }}$ and $\boldsymbol{\Sigma}^{\text {new }}$ by (15)
9: $\quad \circ \mathcal{S} \leftarrow$ Simulate $M$ individuals from $\mathcal{N}\left(\boldsymbol{x} ; \boldsymbol{\mu}^{\text {new }}, \boldsymbol{\Sigma}^{\text {new }}\right)$
10: $\quad \circ \mathcal{S} \leftarrow \operatorname{Reinsertion}(\mathcal{S}) \quad \triangleright$ if-outside-domain
11: $\quad$ Fitness values $\mathcal{F}(\mathcal{S})$
12: $\quad \circ \operatorname{POb}_{t+1} \leftarrow$ Best individuals among $\left\{\operatorname{POb}_{t}, \mathcal{S}\right\}$
13: $\quad$ Find the $\boldsymbol{x}_{t+1}^{\text {best }}$ of $\operatorname{POb}_{t+1}$
14: if $\boldsymbol{x}_{t+1}^{\text {best }}$ has better fitness value than $\boldsymbol{x}^{\text {best }}$ then
15: $\quad \boldsymbol{x}^{\text {best }} \leftarrow \boldsymbol{x}_{t+1}^{\text {best }}$ and $\boldsymbol{x}_{t+1}^{\text {best }}$ replaces the worst individual in $P_{\text {best }}$
16: end if
17: $\quad \circ M_{\text {sur }} \leftarrow$ Number of survivors from $\mathcal{S}$ into $\operatorname{POb}_{t+1}$
18: if $\frac{M_{\text {sur }}}{M}>1 / 2$ then
19: $\quad \beta \leftarrow \beta+0.05$; if $\beta>1$ then $\beta=1 \quad \triangleright$ Exploration
20: else
21: $\quad \beta \leftarrow \beta-0.05$; if $\beta<0$ then $\beta=0 \quad \triangleright$ Exploitation
22: end if
23: $\quad t \leftarrow t+1$
24: end while
Fig. 2. Pseudocode of the EDA led by a Gradient-driven Density (EDA-LGD)
Table 1. Benchmark problems [2] [5]. The minimum fitness value of all problems is 0 , except for $\mathcal{F}_{4}, \mathcal{F}_{6}$ and $\mathcal{F}_{10}$ where $\mathcal{F}_{4}^{*}=2, \mathcal{F}_{6}^{*}=-10$ and $\mathcal{F}_{10}^{*}=-0.1 d$.
i.e. $\left(\mathcal{F}-\mathcal{F}^{*}\right)<10^{-8}$. Figure 3 contrasts the error $\mathcal{F}-\mathcal{F}^{*}$ reached for each algorithm. Also, this Figure shows a comparison between two algorithms in the second and third columns. For each problem there are three measures: 1) the first row is the percentage of success rate, 2) the second row is the mean and standard deviation of reached fitness values, 3) the third row is the mean and standard deviation of needed evaluations of function. The mean values highlighted with boldface, i.e. the winner algorithm, are supported by a statistical test. The last column presents the results of two nonparametric bootstrap tests. Here, the hypotheses are based on the mean value $\mu$. The hypotheses $\left(H_{0}: \mu_{1} \geq \mu_{2}, H_{1}\right.$ : $\mu_{1}<\mu_{2}$ ) yields the p-value $\rho_{1}$ and $\left(H_{0}: \mu_{2} \geq \mu_{1}, H_{1}: \mu_{2}<\mu_{1}\right)$ produces


Fig. 3. Percentage of success rate, reached fitness values and needed number of evaluations (mean and standard deviation) for each algorithm in dimension 20. The last column shows two nonparametric bootstrap tests. If $\rho_{1}$ is boldface the winner is EDALGD, if $\rho_{2}$ is boldface the winner is either CMA-ES or xNES, otherwise there is no winner.
the p-value $\rho_{2}$. So, if $\rho_{1}$ is boldface the winner is EDA-LGD, if $\rho_{2}$ is boldface the winner is either CMA-ES or xNES, otherwise there is no winner. The null hypothesis is rejected with significance level $\alpha=0.05$ Comments (CMAES): The problems $\mathcal{F}_{1}, \mathcal{F}_{2}, \mathcal{F}_{3}, \mathcal{F}_{5}$ and $\mathcal{F}_{6}$ do not seem difficult for EDA-LGD nor CMA-ES, since both algorithms reach the perfect success rate. On the contrary, the rest of the problems have a more difficult landscape. According to the bootstrap test, there is statistical evidence to conclude that in 5 out of 10 problems the proposed EDA requires fewer function evaluations than the CMA-ES. Comments (xNES): According to the bootstrap test, there is statistical evidence to conclude that in 5 out of 10 problems the proposed EDA requires fewer function evaluations than the xNES. Also, there appears to be a pattern related to the landscape. For instance, note xNES has better results for problems $\mathcal{F}_{7}-\mathcal{F}_{10}$, but EDA-LGD has better results for problems $\mathcal{F}_{2}-\mathcal{F}_{6}$. This kind of pattern must be further studied in future work.

# 6 Conclusion 

This paper presents a new EDA based on the Gradient-driven densities $\left(\nabla_{d} \mathrm{D}\right)$. In order to build the proposed EDA (EDA-LGD) two main contributions were developed: the Expected Gradient Estimate (EGE) and the $\nabla_{d} \mathrm{D}$. Also, a technique has been proposed to compute a gradient estimate for any individual only by using the actual knowledge about the problem. Hence, the estimation of the gradient does not need extra evaluations of function. The $\nabla_{d} \mathrm{D}$ are statistical models built by taking into account a gradient estimate. This new framework can create a density function for any individual. Consequently, any simulation from those densities has a random gradient component. Here, Gradient-driven densities based on the Multivariate Normal have been constructed. However, the developed framework allows for the assumption of other statistical models. The ideas discussed above motivated a new EDA: EDA-LGD. It is based on the Gradient-driven Independent Normal, the EGE and the hierarchical latent variable model. Moreover, it was tested in 10 benchmark problems; where the EDA-LGD shows competitive performance against CMA-ES and xNES. In summary, the EDA-LGD is an interesting approach because of the performance of the algorithm and its mathematical foundation. Since the $\nabla_{d} \mathrm{D}$ will produce samples in a similar direction as the gradient estimation, this density can be regarded as a predictive model. Thus, the Gradient-Driven density allows for exploration of the search domain whilst the empirical density intends fast convergence (exploitation). Finally, notice that the main contributions developed here can be extended to other evolutionary algorithms.
