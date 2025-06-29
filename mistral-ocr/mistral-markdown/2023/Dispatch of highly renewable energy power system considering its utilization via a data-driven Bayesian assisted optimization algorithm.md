# Dispatch of highly renewable energy power system considering its utilization via a data-driven Bayesian assisted optimization algorithm ${ }^{\odot}$ 

Chaofan Yu ${ }^{\mathrm{a}, \mathrm{b}}$, Yuanzheng $\mathrm{Li}^{\mathrm{a}}$, Yun Liu ${ }^{\mathrm{c}, \mathrm{e}}$, Leijiao $\mathrm{Ge}^{\mathrm{d}}$, Hao Wang ${ }^{\mathrm{e}}$, Yunfeng Luo ${ }^{\mathrm{a}}$, Linqiang Pan ${ }^{\mathrm{a}}$<br>${ }^{a}$ Key Laboratory of Image Information Processing and Intelligent Control of Education Ministry of China, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430074, China<br>${ }^{b}$ China-EU Institute for Clean and Renewable Energy, Huazhong University of Science and Technology, Wuhan 430074, China<br>${ }^{c}$ School of Electric Power Engineering, South China University of Technology, Guangzhou 510641, China<br>${ }^{d}$ School of Electrical and Information Engineering, Tianjin University, Tianjin 300072, China<br>${ }^{e}$ Department of Data Science and Artificial Intelligence, Monash University, Melbourne, VIC 3800, Australia

## A R TICLE INFO

Keywords:
Renewable energy
Data-driven optimization algorithm
Power system dispatch
Bi-objective optimization
Uncertainty

## A B STR ACT

In recent years, renewable energy (RE) has been widely deployed, and the power system with high penetration RE is gradually formed. However, the high proportion of RE may threaten transmission security of power systems, which in turn limits its utilization. What is more, the interaction between RE penetration and power system transmission security has not been comprehensively investigated so far. To this end, we develop a bi-objective stochastic dispatch model to investigate the relationship between RE utilization and transmission security. It aims to solve the optimal power system dispatch (OPSD) problem with high penetration RE, in which the RE curtailment and the capacity margin of transmission lines are considered as two objectives of the dispatch problem and formulated in the probabilistic forms. With this, the proposed model is a complicated bi-objective stochastic optimization problem, which is difficult to be solved for traditional optimization algorithms. Therefore, we propose a data-driven Bayesian assisted optimization (DBAO) algorithm, based on Bayesian evolutionary optimization and estimation of distribution algorithm to improve the searching efficiency for the proposed model. Case studies on a modified Midwestern US power system verify the effectiveness of our proposed dispatch model and the optimization algorithm of DBAO.

## 1. Introduction

### 1.1. Background

In recent years, renewable energy (RE) has developed rapidly and drawn much attention [1,2]. For instance, the cumulative installed capacity of wind power in China reaches 188.4 GW in 2019, taking up about $37 \%$ of the global market, which is predicted to be 400 GW by 2030 [3]. Therefore, the high RE penetrated power system is gradually formed. However, with large-scale RE integrated into the power grid, its uncertain power output brings about serious challenges to the transmission security of the power system, e.g., the overload of transmission lines, which could lead to unavoidable RE curtailments [4]. In addition, in China, the RE curtailment is quite significant. For instance, in the first three quarters of 2019, the curtailed wind power has reached to about 12.83 billion kWh . The curtailment ratios in Xinjiang, Gansu, and Inner Mongolia of China are as high as $15.4 \%, 8.9 \%$, and $6.6 \%$, respectively [5].

To this end, we could draw a conclusion that the utilization of available RE is not sufficient. In order to support the sustainable development of RE, it is of critical importance to investigate the balance between RE utilization and transmission security in the optimal power system dispatch (OPSD).

### 1.2. Literature review

OPSD, aiming to guarantee high-efficient operations, calculates the optimal dispatch solution with respect to a specific objective, such as fuel cost, transmission loss, etc. When the RE is integrated into the power system, the uncertainties of RE shall be considered, which makes the dispatch problem becomes quite complicated. Currently, three main methodologies have been used to solve OPSD with RE integration, i.e., the fuzzy, robust, and stochastic optimization methods.

In the fuzzy optimization method, the uncertainty of RE is represented as a fuzzy variable, and the dispatch model is formulated

[^0]
[^0]:    ${ }^{\text {a) }}$ This work is supported by Science and Technology Project of State Grid Headquarters (1400-202099523A-0-0-00).

    * Corresponding author.

    E-mail address: liuyun19881026@gmail.com (Y. Liu).

using fuzzy memberships. Nevertheless, they are subjectively selected by dispatchers. Therefore, the obtained dispatch solution is confronted with strong subjectivity [6]. As for the robust optimization method, uncertain RE is presented as an interval variable. Due to the concise representation, this method becomes popular for solving the OPSD problem [7]. For instance, in Ref. [8], a robust optimization method is adopted to deal with uncertain wind power, and the robust dispatch solution of thermal generators is obtained to minimize the system cost under the worst wind scenario. Similarly, a robust energy management approach is adopted in Ref. [9], and the corresponding formulation is established to mitigate the influence of worst-case renewable power simulation. Furthermore, as the issue of RE absorption becomes important, Ref. [10] proposes a robust wind power optimization model in the OPSD problem, in which the penalty cost of possible wind curtailments is considered. However, the robust optimization method is regarded to be conservative since it always tends to find the worst-case scenario solution which often happens at a very low probability.

Although these two methods mentioned above have been extensively investigated by researchers, the stochastic optimization method is still the most widely used approach to solve the OPSD problem with RE integration. One of the main reasons is that by describing uncertainties via random variables using the probabilistic distribution information, it is convenient to use scenarios to quantify objective values of power systems with high RE penetration. For instance, a stochastic dispatch model is proposed in Ref. [11] to minimize power system operation costs, while wind power is presented as a random variable. The obtained results demonstrate that at least 6000 MW wind power can be utilized without significant curtailment, which is equivalent to about $34 \%$ of the total energy demand in Ireland. Note that with the increasing penetration of RE, more attention has been paid to enhance its utilization and reduce curtailment. For example, Ref. [12] proposes a stochastic dispatch method while employing the dynamic line rating scheme. It clearly demonstrates this method can reduce the expected operating cost and the RE curtailment. It is indicated in Ref. [13] that limited transmission capacity may lead to network congestion which renders RE curtailment. It then uses stochastic optimization to quantify the latent scheduling capacity of a power system with intermittent RE to mitigate the risk of network congestion. Furthermore, Ref. [14] presents a stochastic optimization dispatch model with secure constraints, and a scenario generation scheme is used to model uncertainties of RE power output.

### 1.3. Motivation and contribution

Existing researches clearly show that the stochastic optimization method can well solve the OPSD problem with RE integration. Especially, some work has attempted to reduce the power system operation cost in consideration of the security constraints. For example, Ref. [15] propose a security-constrained stochastic dispatch model to minimize the expected total dispatch cost while the limitation of transmission flow is taken into account. Simulation results indicate that the developed model can help to identify desired dispatching schemes and have a significant reduction on the wind power spillage and daily operation cost. A security constrained unit commitment model with extreme wind scenarios is developed in Ref. [16], in order to solve the operational risk caused by wind power uncertainty. Besides, Ref. [17] presents a novel voltage security constrained stochastic dispatch model for power system with battery, whose main objective is maximizing loading margin of battery. Numerical experiments verify the effectiveness of proposed model in achieving the desired maximal loading margin. However, these dispatch problems are usually established as optimization model with single objective while regarding the security as constraints. In this way, the optimal dispatch under secure operation is ensured but the interaction between power system economy and security is still unknown. Notably, the relationship between wind power curtailment and transmission security has not been comprehensively investigated
in the form of multi-objective optimization. To this end, it is worth investigating such a relationship in the bi-objective optimization manner with Pareto analysis, and well balancing the maximum wind power utilization and the transmission security under high RE penetration occasions.

Furthermore, as for the proposed stochastic dispatch model, traditional mathematical optimization algorithms cannot efficiently solve this non-convex multi-objective optimization problem [18]. Fortunately, the evolutionary algorithm is able to deal with this problem with strong robustness and adaptability [19-21]. For instance, various evolutionary algorithms are introduced to solve the multi-objective optimization problems, including commonly used PSO [22], NSGAIII [23] and differential evolution algorithm [24]. Although evolutionary algorithms could handle this problem to some extent, they still have weakness such as time-consuming and inefficient searching. Generally, a great number of objective evaluations is required for evolutionary algorithms to obtain the optimal solution, which easily leads to a timeconsuming computation especially when the optimization problem is high-dimensional and evaluation expensive. Also, the determination of proper parameter is very important since an unsuitable parameter might lead to inefficient searching and even local optimum. For that reason, the complicated multi-objective dispatch problem calls for a novel data-driven optimization algorithm to promote the searching ability and computational efficiency.

To this end, we conduct the following work, which are also the contributions of this paper.
(1) We propose a bi-objective stochastic dispatch model for OPSD with high RE penetration. The wind power utilization and the capacity margin of transmission lines are set as objectives, and the dispatch model aims to analyze their relationship. Therein, a gradual curtailment strategy is proposed in this paper to well formulate wind power curtailment objective functions under stochastic scenarios.
(2) To efficiently solve the proposed bi-objective stochastic dispatch problem, we propose a data-driven Bayesian assisted optimization algorithm based on Bayesian evolutionary optimization and estimation of distribution algorithm. A replacement strategy is developed to update the samples of Bayesian optimization for better prediction precision. Furthermore, an adaptive adjustment of key parameter is achieved based on estimation of the population distribution in this paper.
(3) We conduct case studies on a modified Midwestern US power system, to verify effectiveness of the proposed stochastic dispatch model and data-driven optimization algorithm. In addition, sensitivity analysis regarding our presented dispatch model and four important parameters is discussed, involving wind power penetration rate, sample distribution, consumption level of user loads and locations of wind farms.

These three aspects are the main contributions of our work. The rest of this paper is organized as follows. Section 2 introduces formulations of the proposed bi-objective stochastic dispatch model. In Section 3, the data-driven optimization algorithm is developed. Case studies based on a modified Midwestern US power system are presented in Section 4, and conclusions are drawn in Section 5.

## 2. Bi-objective stochastic dispatch model

### 2.1. Problem formulation

Indeed, the stochastic dispatch of power system is a high dimension nonlinear optimization problem with multiple constraints. The mathematical model of this problem can be formulated as follows:
$\min J=f(\boldsymbol{u}, \boldsymbol{x}, \boldsymbol{\Psi})$
s.t. $g(\boldsymbol{u}, \boldsymbol{x}, \boldsymbol{\Psi})=0$
$h(\boldsymbol{u}, \boldsymbol{x}, \boldsymbol{\Psi}) \leq 0$
where $J$ is the objective, $g$ and $h$ represent the equality and inequality constraints, respectively. $f(\boldsymbol{u}, \boldsymbol{x}, \boldsymbol{\Psi})$ is the objective function, where

![img-0.jpeg](img-0.jpeg)

Fig. 1. The evolution of absorption rate $\gamma$ with increasing scale $\alpha$.
decision variables $\boldsymbol{u}$ include power outputs of controllable generators $P_{G}$ excluding the slack generator $P_{G 1}$, generator terminal voltages $V_{G}$, transformer tap settings $T$, and outputs of reactive power compensation sources $Q_{C}$. State variables $\boldsymbol{x}$ consist of the active power of slack generator $P_{G 1}$, the voltage magnitude of load bus $V_{L}$, the reactive power of generators $Q_{G}$, and the apparent power flow in branch $S_{L} . \Psi=\left\{\psi_{1}, \psi_{2}, \ldots, \psi_{N_{W}}\right\}$ represents $N_{W}$ scenarios of wind power that are sampled by certain methods such as the point estimation approach [25].

### 2.2. Objectives

In order to investigate the relationship between wind power utilization and the security of power system, wind power curtailment and capacity margin of transmission lines are selected as objective functions of the dispatch model. A gradual curtailment strategy is proposed to well formulate the wind power curtailment objective function.

At first, the gradual curtailment strategy under deterministic scenario is presented in this section, as shown in Fig. 1. Initially, wind power absorption $\gamma$ ascends linearly with the increases in the integration scale $\alpha$, which implies that no wind power is curtailed. Afterwards, with a further increment in the integration scale $\alpha$, additional absorption $\gamma$ would lead to a violation of certain operational constraints in (2) or (3), and the curtailment has to be activated. It should be noted that the threshold is actually the maximal absorption at current integration scale, which is obtained by iterative computation rather than definition in advance. Taking $\alpha=45 \%$ as an example, absorption $\gamma$ will gradually decrease until all constraints are fulfilled by $W$ curtailments. The total curtailments are the summation of $W$ gradual curtailments, i.e., $C_{\text {total }}=$ $\sum_{i=1}^{W} C_{i}$, where $C_{i}$ represents the $i$ th wind power curtailment.

On the other hand, taking the uncertainty of wind power into account, wind curtailment is represented as a random variable. To better understand the gradual curtailment strategy in the stochastic dispatch model, the gradual curtailment procedure is shown in Fig. 2. Here, the circle in red represents power system operation constraints, the $j$ th fan-shaped area denotes the $j$ th scenario of wind power $\psi_{j}$ with the corresponding angle representing its possibility $P_{j}$ and radius denoting its output power. Fig. 2 indicates that when the output power of the $j$ th scenario exceeds the red line, constraints will be violated and curtailment has to be activated. Then, the wind power curtailment of this scenario can be calculated via the gradual curtailment strategy as $P_{c a r}^{j}=P_{j} \cdot \sum_{i=1}^{W} C_{j, i}$, where $C_{j, i}$ represents the $i$ th curtailment of the $j$ th scenario.

As there exists $N_{W}$ scenarios of wind power, the total wind power curtailment is the weighted sum of all $N_{W}$ scenarios.
$\min C(\boldsymbol{u}, \boldsymbol{x}, \boldsymbol{\Psi})=\sum_{j=1}^{N_{W}} P_{c a r}^{j}$
![img-1.jpeg](img-1.jpeg)

Fig. 2. Total wind curtailments regarding various scenarios.

The capacity margin of transmission lines is selected as the second objective, which is derived as follows. We first calculate and sort the margins between apparent power on all branches and the corresponding physical limitations in (5). Then, the minimum margin is to be maximized to enhance the transmission security of power systems, as shown in (6).
$\Delta S_{j}=\min \left\{S_{k}^{\max }-\left|S_{j, k}\right|\right\}, k=1,2, \ldots, N_{E}$
$\max C M(\boldsymbol{u}, \boldsymbol{x}, \Psi)=\sum_{j=1}^{N_{W}} \Delta S_{j} \cdot P_{j}$
where $\Delta S_{j}$ represents the minimum margin of the $j$ th scenario, $S_{k}^{\max }$ is the maximum transmitted power limitation in the $k$ th branch, $k=$ $1,2, \ldots, N_{E} . S_{j, k}$ is the output power in the $k$ th branch of the $j$ th scenario, and $N_{E}$ represents the total number of branches.

### 2.3. Constraints

(1) Equality Constraints

In power system operations, the active and reactive power shall be balanced between power sources and demand, which are shown as follows:
$P_{G_{i}}+P_{W . j}=P_{D i}+V_{i} \sum_{j=1}^{N_{i}} V_{j}\left(G_{i j} \cos \theta_{i j}+B_{i j} \sin \theta_{i j}\right)$
$Q_{G_{i}}+Q_{W . j}=Q_{D i}+V_{i} \sum_{j=1}^{N_{i}} V_{j}\left(G_{i j} \sin \theta_{i j}-B_{i j} \cos \theta_{i j}\right)$
where $P_{G i}$ and $Q_{G i}$ denote active and reactive power from traditional generators at bus $i . P_{W . j}$ and $Q_{W . j}$ represent active and reactive power outputs of wind farm at bus $i$. Besides, $P_{D i}$ and $Q_{D i}$ are the active and reactive power demand of buses $i . V_{i}$ and $V_{j}$ represent voltage magnitudes at bus $i$ and $j . \theta_{i j}$ denotes the voltage angle difference between buses $i$ and $j$. In addition, $G_{i j}$ and $B_{i j}$ are the transfer conductance and susceptance between buses $i$ and $j$, and $N_{i}$ represents the total number of buses adjacent to bus $i$.
(2) Inequality Constraints

The output power of each generator shall be limited within a certain range.
$P_{G_{i}}^{\min } \leq P_{G_{i}} \leq P_{G_{i}}^{\max }$
$Q_{G_{i}}^{\min } \leq Q_{G_{i}} \leq Q_{G_{i}}^{\max }$
where $P_{G_{i}}^{\min }$ and $P_{G_{i}}^{\max }$ are the minimal and maximum active power of the $i$ th generator. $Q_{G_{i}}^{\min }$ and $Q_{G_{i}}^{\max }$ are the minimal and maximum reactive power of the $i$ th generator, $i=1,2, \ldots, N_{G}$, and $N_{G}$ denotes the total number of generators.

Similarly, the reactive power of shunt compensators is constrained by $Q_{C i}^{\min }$ and $Q_{C_{i}}^{\max }$, which represent the minimal and maximum reactive power of the $i$ th shunt compensator.
$Q_{C_{i}}^{\min } \leq Q_{C_{i}} \leq Q_{C_{i}}^{\max }, i=1,2, \ldots, N_{C}$

where $N_{C}$ is the total number of shunt compensators.
Besides, the tap position of transformer $k$ is limited to its minimal and maximum positions, i.e., $T_{k}^{\min }$ and $T_{k}^{\max }$.

$$
T_{k}^{\min } \leq T_{k} \leq T_{k}^{\max }, k=1,2, \ldots, N_{T}
$$

where $N_{T}$ represents the total number of transformers.
The magnitude of buses voltage shall satisfy the following constraint.
$V_{i}^{\min } \leq V_{i} \leq V_{i}^{\max }, i=1,2, \ldots, N_{B}$
where $V_{i}^{\min }$ and $V_{i}^{\max }$ are the minimal and maximum voltage magnitudes at bus $i$, and $N_{B}$ denotes the total number of buses.

Taking the transmission capacity of lines into account, the apparent power flow $S_{k}$ is constrained as follows:
$\left|S_{k}\right| \leq S_{k}^{\max }, k=1,2, \ldots, N_{E}$
To summarize, we propose a bi-objective stochastic dispatch model in (15) considering both wind power curtailment and capacity margin of transmission lines while satisfying various constraints. This would help power system operators to investigate their interaction, and to better utilize wind power and support transmission security for power systems with high RE penetration.
$\min \left[C(\boldsymbol{u}, \boldsymbol{x}, \boldsymbol{\Psi}),-C M(\boldsymbol{u}, \boldsymbol{x}, \boldsymbol{\Psi})\right]$
s.t. (6) - (14)

## 3. Data-driven Bayesian assisted optimization algorithm

As for the proposed stochastic dispatch model, traditional mathematical optimization algorithms cannot efficiently solve this nonconvex multi-objective optimization problem. Fortunately, the evolutionary algorithm is capable of handling this problem with strong adaptability and robustness. Recently, a newly invented evolutionary algorithm, named moth flame optimization (MFO), has drawn much attention for its simple structure and parameters [26]. However, just like other evolutionary algorithms, MFO still has weaknesses such as time-consuming computation and inefficient searching. Generally, a great number of objective evaluations is required for evolutionary algorithms to obtain the optimal solution, which easily leads to a timeconsuming computation especially when the optimization problem is high-dimensional and evaluation expensive. Also, the determination of proper parameter is very important since an unsuitable parameter might lead to inefficient searching and even local optimum. Therefore, we propose a data-driven Bayesian assisted optimization algorithm (DBAO), in which Bayesian optimization is introduced to assist evolutionary algorithms overcoming the drawback of time-consuming computation. Furthermore, taking the inefficiency of conventional evolutionary algorithms into consideration, a data-driven method called estimation of distribution algorithm is adopted to adaptively adjust the parameter and enhance the searching efficiency.

### 3.1. Moth flame optimization

As a recently proposed evolutionary algorithm, MFO has been utilized in many real-world optimization applications for its robustness [27]. It should be mentioned that the population in MFO is characterized by two types, i.e., moths and flames. Moths represent search agents of optimization problems that move around the search space, while flames denote the best solutions obtained by moths. That is to say, flames could be considered as pointers that guide moths to search the objective space. Hence, each flame will instruct a corresponding moth to search around itself, which is updated once the moth reaches a better position. The optimal solution would be finally obtained by updating positions of flames iteratively.

Another key feature of MFO is the spiral flying mechanism, which ensures moths search more spaces other than just the direct space between moths and flames. The formulation of logarithmic spiral function is expressed as follows:
$M_{i}=L S F\left(M_{i}, F_{j}\right)=D_{i} \cdot e^{M} \cdot \cos (2 \pi t)+F_{j}$
$D_{i}=\left|F_{j}-M_{i}\right|$
where $M_{i}$ represents the position of the $i$ th moth, and $L S F$ denotes the logarithmic spiral function. $F_{j}$ is the position of the $j$ th flame, and $D_{i}$ denotes the distance vector between the $j$ th flame and the $i$ th moth. Besides, $b$ is the key parameter of spiral function which affects the shape of spiral trajectory, and $t$ is a random number in $[-1,1]$.

### 3.2. Bayesian evolutionary optimization

In recent years, machine learning has made great strides and achieved success in engineering applications [28]. Among diverse machine learning approaches, Bayesian optimization is supposed to be one of the most advanced and promising methods in the probabilistic machine learning [29]. It is a powerful tool to solve complex optimization problems, especially the non-convex, multi-modal and evaluation-expensive one, like our proposed stochastic dispatch model. To this end, we utilize Bayesian optimization to assist MFO finding solutions of our computation expensive problem within a limited number of evaluations, which is named Bayesian evolutionary optimization (BEO). Summarily, the framework of BEO incorporates two parts, i.e., the probabilistic surrogate model and the acquisition function.

The probabilistic surrogate model is constructed to substitute the real objective evaluation, which is computational expensive for our problem. Indeed, there are series of researches focusing on probabilistic surrogate model, which could be divided into two categories based on the number of model parameters [30]. The first category is the parametric model including Beta-Bernoulli model, linear model and generalized linear model, in which the number of parameters is a constant. However, the applications of parametric model have so far been limited to relatively small-scale optimization tasks, whereas optimal power system dispatch problems tend to have a large number of variables.

Another category is the non-parametric model where the number of parameters is alterable, such as the random forests, radial basis function network and Kriging surrogate model. Unlike the parametric model, the number of parameters in the non-parametric model increases along with the amount of observation data. Consequently, Bayesian non-parametric model is regarded to be more flexible in comparison with the parametric one [31]. Among various non-parametric models, the Kriging surrogate model is easy to implement and has advantages in hyperparameter adaptively tuning and non-parametric flexibly inference. Indeed, Kriging surrogate model has achieved a wide variety of successful applications in high dimensional complicated optimization problems with strong generalization ability. To this end, Kriging surrogate model is applied in our manuscript to substitute the time-consuming real objective evaluation. Furthermore, the acquisition function is designed to denote the promising candidates for the next iteration based on predicted information. Several acquisition functions have been proposed such as probability of improvement, the upper confidence bound and the expected improvement (EI) [31].

In this paper, Kriging surrogate model is adopted as the probabilistic surrogate model since it can deliver the approximated value of the objective function as well as uncertain information, simultaneously [32]. EI is introduced as the acquisition function for it can well achieve a balance between global exploration and local exploitation [33]. Therefore, the rest of this section is organized to describe Kriging surrogate model and EI, respectively.

### 3.3. Kriging surrogate model

The Kriging surrogate model uses observed samples to create a response surface. It is used for estimating the fitness of objectives at unobserved locations [34]. In this paper, the Kriging surrogate model is combined with evolutionary algorithms. The positions of evaluated population are utilized as observed samples, which are denoted as $\boldsymbol{x}=\left\{x_{1}, \ldots, x_{t}, \ldots, x_{k}, \ldots, x_{N}\right\}$ with their objective fitness $\boldsymbol{y}=\left\{y_{1}, \ldots, y_{t}, \ldots, y_{k}, \ldots, y_{N}\right\}$. Then, an estimation model is constructed by these samples $\{\boldsymbol{x}, \boldsymbol{y}\}$ to obtain the estimated response surface and approximate the fitness of unobserved locations $\boldsymbol{x}^{*}$.

The formulation of this model can be expressed as
$\hat{\boldsymbol{y}}\left(\boldsymbol{x}^{*}\right)=\mu+c\left(\boldsymbol{x}^{*}\right)$
where $\hat{\boldsymbol{y}}\left(\boldsymbol{x}^{*}\right)$ represents the estimated fitness, $\mu$ denotes the mean value of Kriging, and $c\left(\boldsymbol{x}^{*}\right)$ is the Gaussian distributed error with the mean value 0 and variance $\sigma^{2}$. Particularly, the Kriging model assumes that the error of any two points is correlated.
$\operatorname{Corr}\left[c\left(x_{i}\right), c\left(x_{k}\right)\right]=\prod_{d=1}^{D} \exp \left(-\theta_{d}\left|x_{i d}-x_{k d}\right|^{p_{d}}\right)$
where $x_{i}$ and $x_{k}$ represent positions of the $i$ th and the $k$ th individual in population. $x_{i d}$ and $x_{k d}$ are the $d$ th dimensions of $x_{i}$ and $x_{k}$, respectively. $d=1, \ldots, D$, where $D$ is the number of dimensions of $x_{i}$. Besides, $\theta_{d}$ and $p_{d}$ are undetermined coefficients, where $\theta_{d}$ describes the descend speed of correlation from one point to another in the $d$ th dimension, while $p_{d}$ represents the smoothness of correlation function.

Key parameters of the Kriging surrogate model, such as $\mu, \sigma$, $\theta_{1}, \ldots, \theta_{D}, p_{1}, \ldots, p_{D}$ can be obtained by the maximum likelihood estimation [34]. Then, the estimated fitness of unobserved locations $\boldsymbol{x}^{*}$ is expressed as follows:
$\hat{\boldsymbol{y}}\left(\boldsymbol{x}^{*}\right)=\hat{\mu}+r^{T} \boldsymbol{R}^{-1}(\boldsymbol{y}-\mathbf{1} \hat{\mu})$
$\hat{\mu}=\frac{\mathbf{1}^{T} \boldsymbol{R}^{-1} \boldsymbol{y}}{\mathbf{1}^{T} \boldsymbol{R}^{-1} \mathbf{1}}$
$\hat{\sigma}^{2}=\frac{(\boldsymbol{y}-\mathbf{1} \hat{\mu})^{T} \boldsymbol{R}^{-1}(\boldsymbol{y}-\mathbf{1} \hat{\mu})}{n}$
where $\hat{\boldsymbol{y}}$ and $\hat{\mu}$ represent the estimated fitness and mean objective value regarding $\boldsymbol{x}^{*}$, respectively. $\boldsymbol{r}$ represents the $N \times 1$ correlation vector between unobserved $\boldsymbol{x}^{*}$ and observed $\boldsymbol{x}$, while its element $r_{i}=$ $\operatorname{Corr}\left[c\left(x_{i}^{*}\right), c(\boldsymbol{x})\right] . \boldsymbol{R}$ denotes the $N \times N$ dimensional matrix of correlation coefficient with its element $R_{i j}=\operatorname{Corr}\left[c\left(x_{i}\right), c\left(x_{j}\right)\right]$ representing the correlation between two points of $x_{i}$ and $x_{j}$, and $\mathbf{1}$ represents a $N \times 1$ dimensional unit vector.

Accordingly, the mean squared error of the Kriging model [35] at $\boldsymbol{x}^{*}$ is denoted as $s^{2}(\cdot)$.
$s^{2}\left(\boldsymbol{x}^{*}\right)=\hat{\sigma}^{2}\left[1-r^{T} \boldsymbol{R}^{-1} \boldsymbol{r}+\frac{\left(1-\mathbf{1}^{T} \boldsymbol{R}^{-1} \boldsymbol{r}\right)^{2}}{\mathbf{1}^{T} \boldsymbol{R}^{-1} \mathbf{1}}\right]$

### 3.4. Expected improvement criterion

It shall be mentioned that the traditional Kriging may lead to large estimation errors since the samples are not easy to be constructed and updated properly [35]. To this end, the acquisition function is proposed to assist in selecting potential individuals, which are evaluated by expensive objective function and update samples of surrogate model. In this paper, we introduce the EI criterion and a novel update strategy of Kriging samples [36]. Details about the EI rule are described as follows.

Firstly, the uncertainty $\boldsymbol{Y}\left(\boldsymbol{x}^{*}\right)$ about objective fitness at $\boldsymbol{x}^{*}$ is supposed to be a stochastic variable following the normal distribution with estimated mean value $\hat{\boldsymbol{y}}\left(\boldsymbol{x}^{*}\right)$ and variation $s^{2}\left(\boldsymbol{x}^{*}\right)$, i.e., $\boldsymbol{Y}\left(\boldsymbol{x}^{*}\right) \sim$ $N\left(\hat{\boldsymbol{y}}\left(x^{*}\right), s^{2}\left(\boldsymbol{x}^{*}\right)\right)$, since the real objective fitness of unobserved locations is unknown.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Samples update strategy of Kriging under EI criterion.

Therefore, the improvement of $\boldsymbol{x}^{*}$ to the current best individual with the objective fitness $y_{\min }$ is presented as follows:
$\boldsymbol{I}\left(\boldsymbol{x}^{*}\right)=\max \left\{\left(y_{\min } \cdot \mathbf{1}-\boldsymbol{Y}\left(\boldsymbol{x}^{*}\right)\right), 0\right\}$
As $\boldsymbol{Y}\left(\boldsymbol{x}^{*}\right)$ is a stochastic variable, we then adopt the corresponding expected improvement function $\boldsymbol{E} \boldsymbol{I}\left(\boldsymbol{x}^{*}\right)$, which is expressed in (25), and the unobserved location with the largest EI value is supposed to be the best candidate for next evaluation.
$\boldsymbol{E} \boldsymbol{I}\left(\boldsymbol{x}^{*}\right)=\left(y_{\min } \cdot \mathbf{1}-\hat{\boldsymbol{y}}\left(\boldsymbol{x}^{*}\right)\right) \boldsymbol{\Phi}(\boldsymbol{u})+s\left(\boldsymbol{x}^{*}\right) \boldsymbol{\phi}(\boldsymbol{u})$
where $\boldsymbol{\Phi}(\cdot)$ and $\boldsymbol{\phi}(\cdot)$ represent the cumulative distribution function and probability density function of the standard normal distribution, respectively. In addition, $\boldsymbol{u}$ is calculated as follows:
$\boldsymbol{u}=\frac{y_{\min } \cdot \mathbf{1}-\hat{\boldsymbol{y}}\left(\boldsymbol{x}^{*}\right)}{s\left(\boldsymbol{x}^{*}\right)}$
Usually, the individual with largest EI value will be added into observed samples iteratively to make updates [37]. However, this strategy might significantly increase the size of samples, which results in a heavy burden for calculating the correlation matrix in (20). To this end, we propose a replacement strategy to update samples of the surrogate model, as shown in Fig. 3. The circles marked with numbers represent sorted individuals in samples, while the best individual is marked with 1 and the last one is marked with $N$. The circles filled with lines represent different individuals of the population, while the best individual selected by the EI criterion is denoted with a star. The best individual will replace the first sample only if it is not worse than the first sample; Otherwise, it will replace the last sample. It is also noted that even if the fitness of the best individual is not better than the last sample, we still use this candidate selected by the EI rule to execute replacement, because it contains relevant information about the surrogate model.

### 3.5. Estimation of distribution algorithm

It should be mentioned that the unsuitable setting of parameters might result in the BEO algorithm falling into local optima. Therefore, a data-driven method, called EDA, is introduced to adaptively adjust parameters of BEO. EDA is a stochastic optimization algorithm based on probabilistic information that is driven by historical data [38]. It is able to learn from the distribution information of excellent individuals and construct a probabilistic model of population distribution, then a new population is generated by randomly sampling from this probabilistic model [39]. In order to improve the search efficiency of BEO algorithm, we adopt the EDA algorithm based on Gaussian distribution, which is beneficial to enhance its optimization ability. It shall be mentioned that $b$ is the key parameter in MFO, which impacts the shape of moth flying trajectory. Then, it will affect the searching efficiency of BEO algorithm. To this end, we combine EDA with BEO to adjust the parameter $b$ adaptively. The detailed procedure is presented as follows.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Flow chart of the data-driven Bayesian assisted optimization algorithm.

At first, we initialize the parameter $b$ of moth population with random numbers. Subsequently, better individuals of population are selected by objective function evaluations. Then, an estimated distribution information is constructed by calculating mean value $b_{\mu}$ and standard deviation $b_{\sigma}$ of such prior population as follows:
$b_{\mu}=\frac{1}{m} \sum_{i=1}^{m} b_{i}$
$b_{\sigma}=\sqrt{\frac{1}{m-1} \sum_{i=1}^{m}\left(b_{i}-b_{\mu}\right)^{2}}$
where $m$ is the number of excellent members and $b_{i}$ represents the value with respect to the $i$ th individual.

Afterwards, $b$ is updated as follows:
$b=b_{\mu}+b_{\sigma}\left(-2 \ln u_{1}\right)^{\frac{1}{2}} \cos \left(2 \pi \mu_{2}\right)$
where $\mu_{1}$ and $\mu_{2}$ are random numbers uniformly distributed in interval $[0,1]$, respectively.

Besides, to avoid the BEO population falling into local optimum, the random crossing is introduced to further renew $b$.
$b_{\text {new }}=a \cdot b_{\text {best }}+(1-a) \cdot b$
where $b_{\text {new }}$ denotes the updated parameter of $N \times p c$ moths using the random crossing, and $p c$ represents the random crossing probability. $a$ is a random number in interval $[0,1]$, and $b_{\text {best }}$ denotes the parameter value of the best individual.

Therefore, the flowchart of DBAO algorithm is presented in Fig. 4, which mainly includes two parts, i.e., BEO and EDA. To be specific,
the BEO is the fundamental of this algorithm which aims to improve the computational efficiency and the EDA is devoted to adaptively adjust the parameter of BEO and enhance the searching ability. At first, BEO is developed to assist evolutionary algorithms overcoming the drawback of time-consuming computation, which could solve our computation expensive problem within a limited number of evaluations. In detail, the data of power system is imported to initialize the population, which is also served as the initial observed samples. Then, the Kriging surrogate model is established on the basis of these samples. After that, BEO would calculate the EI value of population and update the Kriging samples through our proposed replacement strategy. Then, individuals with larger EI value are regarded as potential members, which are evaluated by real objective function. In this way, BEO achieves superior computational efficiency through reducing unnecessary evaluations and accelerating convergence.

Subsequently, EDA is introduced to adaptively adjust parameters of BEO by building probability distribution model of parameter and stochastically sampling from it. More specifically, an estimated distribution information is constructed by calculating mean value and standard deviation of such prior population. Afterwards, a probabilistic distribution model of parameter $b$ is established on the basis of this distribution information, then a new population is generated by randomly sampling from this probabilistic model. With the help of EDA, BEO is able to estimate the distribution of parameter $b$, which affects the searching efficiency of BEO. To summarize, the DBAO is executed by iterative repeating of the above procedure, in which BEO enhances the computational efficiency and EDA promotes the searching ability. Finally, the Pareto solutions are exported when the iteration loop is terminated.

## 4. Simulation studies

### 4.1. Simulation settings

In order to verify the effectiveness of the proposed bi-objective stochastic dispatch model and the optimization algorithm, a case study is conducted on a modified Midwestern US power system [40]. The network topology is shown in Fig. 5, and the rated power of transmission line is set as 200 MW . Five wind farms are installed at buses 2,7 , 10,16 , and 24 , respectively. We assume that forecast power outputs of these five wind farms are 36.2 MW, 100 MW, 24.1 MW, 41.7 MW, and 13.7 MW, respectively. In this way, the forecast wind power integrated into the power system is 215.7 MW , i.e., the penetrated ratio of wind power is about $43.14 \%$. Also, we set forecasting errors of wind power as $8 \%$ of their forecast values.

Firstly, we attempt to obtain corresponding Pareto solutions for testifying the effectiveness of proposed bi-objective dispatch model. Then, dispatching performances among these solutions are compared to verify the necessity of considering both wind power curtailments and the capacity margin of transmission lines simultaneously. In addition, to demonstrate the outperformance of DBAO algorithm, we adopt four other evolutionary algorithms for comparisons, i.e., multi-objective evolutionary algorithm based on decomposition (MOEA/D) [41], traditional moth flame optimization (MFO), non-dominated sorting genetic algorithm II (NSGA-II) [42] and Bayesian evolutionary optimization (BEO). To make a fair comparison, for all algorithms, the size of population members and the maximum number of iterations are set as 40 and 200, respectively. The size of potential individuals in BEO and DBAO population is set as 20 , which means 20 potential members are evaluated by real objective functions. The size of excellent members $m$ and random crossing probability $p c$ for the DBAO algorithm are set as 10 and 0.1 , regarding (27) and (30), respectively.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Topology of the modified Midwestern US power system.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Pareto fronts of OPSD obtained by BEO and DBAO in the modified Midwestern US power system.

### 4.2. Simulation results

### 4.2.1. The effectiveness of objective model

The best Pareto fronts obtained by BEO and DBAO in 30 independent runs are presented in Fig. 6, respectively. It could be observed that the capacity margin of transmission lines increases along with the wind power curtailment, which reflects wind power integration indeed impacts the secure operation of power system. On the one hand, wind power plants prefer to promote the utilization of RE in power system, in order to gain more revenue. However, additional RE absorption would result in a violation of certain secure constraints in power system operation, which further activates the curtailment mechanism. Actually, a higher level of wind power curtailment corresponds to a larger capacity margin of transmission lines, indicating that curtailment mechanism could relieve the security burden of transmission lines.

On the other hand, power system is inclined to increase the capacity margin of transmission lines, in order to ensure the secure transmission of power system. Consequently, more wind power curtailments might be occurred, which damages the interests of wind power plants in turn. Taking these two sides into account, it could be concluded that wind power curtailment and capacity margin of transmission lines are consistent to some extent, which means a higher level of wind power curtailment would bring about larger capacity margin of transmission lines.

Furthermore, from the perspective of Pareto analysis, it is illustrated that the Pareto front with respect to DBAO is better since it obtains more capacity margin of transmission lines than conventional BEO,

Table 1
Curtailments and capacity margin of selected solutions.

| Solutions | $\mathrm{WP}^{\mathrm{a} \text { a }}$ | Percentage/\% | $\mathrm{CM}^{\mathrm{b}}$ | Percentage/\% |
| :-- | :--: | :--: | :--: | :--: |
| A | 14.01 | 6.49 | 13.92 | 6.96 |
| $\mathrm{~A}_{1}$ | 14.01 | 6.49 | 2.67 | 1.34 |
| B | 24.79 | 11.49 | 81.25 | 40.63 |
| C | 52.86 | 24.51 | 96.17 | 48.08 |
| $\mathrm{C}_{1}$ | 52.86 | 24.51 | 95.47 | 47.73 |

a WPC represents the wind power curtailments (MW).
b CM denotes the capacity margin of transmission lines (MW).

Table 2
Candidate dispatch solutions obtained by preference ranking organization method.

| Solutions | $A$ | $A_{1}$ | $B$ | $C$ | $C_{1}$ |
| :-- | :--: | :--: | :--: | :--: | :--: |
| $P_{0}(\mathrm{MW})$ | 20.0351 | 20.2888 | 43.4932 | 51.3737 | 21.6761 |
| $P_{0}(\mathrm{MW})$ | 15.5439 | 16.2173 | 49.8639 | 49.9632 | 48.0007 |
| $P_{0}(\mathrm{MW})$ | 10.2308 | 10.6694 | 10.0415 | 31.0536 | 27.0529 |
| $P_{0}(\mathrm{MW})$ | 10.2679 | 10.0504 | 11.0773 | 23.0618 | 15.7010 |
| $P_{0}(\mathrm{MW})$ | 12.7349 | 12.4080 | 12.8873 | 14.6680 | 12.9902 |
| $V_{1}(\mathrm{p} . \mathrm{u})$ | 0.9840 | 0.9580 | 0.9850 | 1.0198 | 0.9774 |
| $V_{2}(\mathrm{p} . \mathrm{u})$ | 0.9689 | 0.9569 | 0.9793 | 1.0146 | 0.9731 |
| $V_{3}(\mathrm{p} . \mathrm{u})$ | 0.9659 | 0.9653 | 0.9663 | 0.9843 | 1.0279 |
| $V_{4}(\mathrm{p} . \mathrm{u})$ | 0.9501 | 1.0334 | 0.9828 | 0.9894 | 0.9507 |
| $V_{5}(\mathrm{p} . \mathrm{u})$ | 0.9802 | 1.0942 | 0.9703 | 0.9569 | 1.0093 |
| $V_{6}(\mathrm{p} . \mathrm{u})$ | 0.9959 | 0.9538 | 1.0445 | 0.9731 | 0.9843 |
| $T_{1}$ | 1.8838 | 13.2801 | 10.8010 | 12.4092 | 12.1196 |
| $T_{2}$ | 4.5138 | 6.9087 | 1.5486 | 16.6348 | 15.4368 |
| $T_{3}$ | 1.5340 | 16.1890 | 5.5112 | 6.4102 | 9.1508 |
| $T_{4}$ | 11.2867 | 4.8985 | 8.8561 | 8.7174 | 10.9234 |
| $Q_{0}(\mathrm{MVAx})$ | 3.6646 | 2.3736 | 2.4608 | 0.8563 | 4.9415 |
| $Q_{0}(\mathrm{MVAx})$ | 5.1817 | 2.5846 | 1.3209 | 4.6847 | 0.0744 |
| $Q_{2}(\mathrm{MVAx})$ | 4.2179 | 5.8800 | 5.8845 | 4.1437 | 4.8165 |
| $Q_{2}(\mathrm{MVAx})$ | 0.0046 | 2.5242 | 3.7887 | 2.7025 | 3.0460 |
| $Q_{0}(\mathrm{MVAx})$ | 0.8364 | 0.8726 | 4.4137 | 0.0180 | 2.8048 |
| $Q_{2}(\mathrm{MVAx})$ | 0.7168 | 4.2992 | 5.9734 | 3.5248 | 4.9468 |
| $Q_{3}(\mathrm{MVAx})$ | 5.7974 | 5.9533 | 5.1426 | 5.1189 | 1.2287 |
| $Q_{3}(\mathrm{MVAx})$ | 2.1067 | 4.2683 | 0.5310 | 4.6798 | 3.3519 |
| $Q_{0}(\mathrm{MVAx})$ | 5.9766 | 0.1113 | 5.4818 | 5.8448 | 4.1365 |

under the same value of wind power curtailment. Also, we select five solutions (i.e., $\mathrm{A}, \mathrm{A}_{1}, \mathrm{~B}, \mathrm{C}, \mathrm{C}_{1}$ ) to analyze the quality of obtained Pareto fronts, the objective values of which are listed in Table 1. The detailed decision variables of these candidate solutions are also listed and shown in Table 2 and Fig. 7, respectively. Note that solutions A and C are extreme solutions regarding DBAO, since they correspond to the minimum wind power curtailment and the maximum capacity margin of transmission lines, respectively, while solutions $\mathrm{A}_{1}$ and $\mathrm{C}_{1}$ correspond to the BEO. As for solution B, it is determined by a decisionmaking method from various Pareto solutions, i.e., preference ranking organization method [43] for enrichment evaluations.

For solution $\mathrm{A}_{1}$, the value of wind power curtailment is as low as 14.01 MW. As the forecasted wind power integration is 215.7 MW , the curtailment percentage is $14.01 / 215.7=6.49 \%$. However, the capacity margin of transmission lines is only 2.67 MW , as compared to the rated power of 200 MW . That is, the corresponding percentage is $2.67 / 200=1.34 \%$, which is only accounted to $38.36 \%(2.67 / 6.96)$ of DBAO. More importantly, the capacity margin of such a low level would threaten the power system transmission security. As for solution $\mathrm{C}_{1}$, it curtails the similar quantity of wind power but the corresponding capacity margin of transmission lines is less than that of solution C. This means that solution C performs better, which also verifies that the Pareto front obtained by DBAO outperforms that of BEO, to certain extent. Without generality, Pareto fronts obtained by other optimization algorithms can also be analyzed in the same way.

It is noted that for solutions obtained by DBAO, both solution A and C are not preferred for power system operations, as they put more efforts into optimizing single one objective. Indeed, solution B is actually the balanced solution between wind power curtailment and capacity margin. On the one hand, from the aspect of renewable

![img-6.jpeg](img-6.jpeg)

Fig. 7. Final solutions obtained by preference ranking organization method.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Wind power curtailments and capacity margin of transmission lines samples for solution A, B and C.
energy utilization, the wind power curtailment of solution B is only accounted for $46.89 \%(24.79 / 52.86)$ of solution C, but it archives $84.49 \%$ $(81.25 / 96.17)$ capacity margin of transmission lines compared with solution C. On the other hand, from the perspective of power system transmission security, solution B obtains $33.67 \%$ (40.63-6.96) more capacity margin, at the cost of just curtailing $5.00 \%$ ( $11.49 \%-6.49 \%$ ) more wind power than solution A. Taking these two aspects into consideration, solution B would be a better solution than both A and C.

To well verify the effectiveness of solution A, B and C, the value of wind power curtailments and capacity margin of transmission lines with respect to 10 samples are calculated and shown in Fig. 8. It should be mentioned that these 10 samples are actually the scenarios of wind power sampled by point estimation approach as mentioned before. It is observed from Fig. 8 that solution B is the balanced solution that considers wind power curtailment and capacity margin of transmission lines in 10 different scenarios, which is coincident with our foregoing analysis. To this end, we could make a conclusion that it is necessary to consider both wind power curtailment and capacity margin of transmission lines simultaneously.

### 4.2.2. The effectiveness of optimization algorithm

Furthermore, from the aspect of optimization algorithms, a comprehensively quantitative comparison between DBAO and other four algorithms is conducted. Here, two performance indices, including Hypervolume (HV) [44] and elapsed computing time (ECT), are adopted in this paper to evaluate the quality of obtained Pareto fronts and algorithm, respectively. The HV is calculated by summing the hypervolume between all solutions and reference point (set as $[215.7,0.0]$ in this paper), and this index can measure the quality of the obtained Pareto front. More specifically, a higher value of HV index corresponds

Table 3
Metric comparisons between Pareto fronts obtained by MOEA/D, MFO, NSGA-II, BEO and DBAO.

| ALGO | MOEA/D | MFO | NSGA-II | BEO | DBAO |
| :-- | :-- | :-- | :-- | :-- | :-- |
| ECT | 772.64 | $954.82 \mathrm{~s}$ | $1922.59 \mathrm{~s}$ | $544.89 \mathrm{~s}$ | $\mathbf{5 1 4 . 1 2} \mathrm{s}$ |
| HV | 45341.24 | 45507.36 | 45311.03 | 45446.95 | $\mathbf{4 5 5 0 7 . 3 6}$ |

![img-8.jpeg](img-8.jpeg)

Fig. 9. Comparison of the HV index between MOEA/D, MFO, NSGA-II, BEO and DBAO.
to a better quality of Pareto front. In addition, the ECT denotes elapsed time of the algorithm while solving the optimization problem.

These two indices with respect to different algorithms are listed in Table 3. We could observe that the value of ECT obtained by DBAO is 514.12 s , which is significantly less than those of other algorithms. It is also shown that HV obtained by DBAO is equal to MFO, which is larger than those of MOEA/D, NSGA-II and BEO. Larger value of HV denotes that the Pareto solutions obtained by DBAO are of higher quality. Taking these two aspects into account, we cloud make a conclusion that the convergence speed of DBAO is much faster than conventional evolutionary algorithms, since EDA has the ability to adaptively adjust parameter which contributes to better convergent performance. In summary, DBAO outperforms MFO, NSGA-II, MOEA/D, and BEO in computational time and searching efficiency.

It shall be mentioned that all these indicators are usually calculated based on the finally obtained Pareto front. Thus, it is not easy to observe the whole optimization process of algorithms. In order to further present a detailed comparison intuitively, HV index is also adopted to illustrate the performance of the proposed algorithm. A large value of HV denotes a better quality of Pareto fronts. Therefore, the variation process of HV values along iterations is shown in Fig. 9(a). It is observed that MFO and DBAO obtain the largest value of HV among these optimization algorithms, which means the Pareto fronts obtained by MFO and DBAO are better than that of other algorithms. However, it is not easy to judge which one is better between MFO and DBAO since they converge to the same HV value finally.

Fortunately, note that reducing unnecessary evaluations and accelerating convergence are the prominent features of DBAO. Taking this issue into consideration, unlike Fig. 9(a), a comparison of HV index regarding solving time rather than iterations among MOEA/D, MFO, NSGA-II and BEO is presented in Fig. 9(b). Since the horizontal ordinate is time, this figure could indicate the convergent speed of algorithms. It is shown that convergent speed of DBAO is obviously faster than the other four algorithms. More importantly, the HV index of DBAO is still larger than others when DBAO is terminated at 514.12 s , which means DBAO has a superior performance with less evaluations and solving time.

The reason why DBAO outperforms the other four algorithms is that it hybridizes BEO and EDA. With the help of EDA, DBAO is able to estimate the distribution of parameter $b$, which affects the searching efficiency of BEO. The variation process of mean value $b_{\mu}$ and standard deviation $b_{\sigma}$ of parameter $b$ is presented in Fig. 10. We can observe that the standard deviation of parameter $b$ is large at the initial iterations, indicating that the flight trajectories of moth population are diverse. By using EDA to draw lessons from distribution information of excellent individuals, it will enter a dynamic adjustment stage where the mean

![img-9.jpeg](img-9.jpeg)

Fig. 10. Variation of parameter in DBAO driven by EDA.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Pareto fronts obtained by DBAO in the modified Midwestern US power system with various wind power penetration.
value of spiral paths fluctuates up and down until it stabilizes to a certain value after about the 171th iteration. Also, it is indicated that the standard deviation gradually decreases to zero after about 90th iteration, which demonstrates posterior moths draw on the experience of excellent individuals and obtain convergence finally.

In summary, on the basis of the analysis in this section, we could make a conclusion that DBAO has advantages in searching efficiency and solving the problem of time-consuming, compared with aforementioned optimization algorithms.

### 4.2.3. Sensitivity analysis

As mentioned before, the penetration rate of wind power is very important for power system economic and secure operation. For that reason, a sensitivity analysis of wind power utilization has been executed to investigate the relationship between the ratio of wind power integration and power system operation in this paper.

Firstly, we preset the penetration ratio of wind power linearly as $23.14 \%, 33.14 \%, 43.14 \%$ and $53.14 \%$ for different simulation scenarios. After that, case studies under different rates of wind power penetration are conducted on the modified Midwestern US power system, respectively. The best Pareto fronts obtained by DBAO under these different penetration rates of wind power in 30 independent runs are presented in Fig. 11. It could be observed that the wind power integration indeed impacts the operation of power system. On the view of transmission security, with the increase rate of wind power integration, the capacity margin of transmission lines is decreasing. This phenomenon reflects that excessive uncertain wind power integrating into power system cloud threaten the secure operation of power system certainly. On the view of renewable energy utilization, more wind power is curtailed with the increasing of wind power penetration rate, which means improper dispatch of wind power might result in massive economic losses.
![img-11.jpeg](img-11.jpeg)

Fig. 12. HV index obtained by DBAO in the modified Midwestern US power system with various wind power penetration.

Similarly, the HV index is also adopted to illustrate the performance of Pareto fronts obtained by DBAO under different penetration rates of wind power. The variation process of HV values with regard to the iterations and time are shown in Fig. 12, respectively. It is clearly illustrated from Fig. 12(a) that the HV value of lower penetration is larger than the value of higher one, which reflects the Pareto front obtained under low wind penetration is better that the higher one. Also, it could be observed from Fig. 12(b) that the solving time of power system under lower penetration is less than the higher one, which denotes that the power system is becoming complex with the penetration ratio raising.

In addition, our proposed dispatch model is considered to be sensitive to other three parameters, i.e., sample distribution, consumption level of user loads and locations of wind farms. Firstly, it should be mentioned that our dispatch model is based on the stochastic optimization, which depicts uncertainty via random variables using the probabilistic distribution information. More specifically, stochastic dispatch model usually assumes that the renewable power follows an exact probability distribution, according to the history data. Afterwards, massive scenarios could be obtained by iteratively sampling from this probability distribution, which corresponds to various probabilities. Therefore, this sample distribution is quite important for our dispatch model, which describes the uncertainty of RE. In other words, different probabilistic distributions will generate distinct random samples with respective probability masses, which further leads to different dispatch results of power system.

Secondly, the consumption level of user loads is significant for optimal power system dispatch as well. This is due to the fact that the amount of wind power transmitted by power lines is relative to the consumption level of user loads. In detail, the output power of wind farms is firstly supplied to the local loads while the residual part is delivered by transmission lines. That is to say, if the consumption level of user loads is high enough, the curtailment problems in power system would be alleviated, to a considerable extent. Thirdly, the proposed dispatch model is also sensitive to the locations of wind farms, which strongly impacts the distribution of power flows. It should be note that the capacity margin of transmission lines in our article is dependent on the transmission capacity of lines as well as the current power flow. Hence, wind farms integrating to power system at different locations would correspond to a distinct distribution of power flows, which results in the calculation of capacity margin of transmission lines different at last.

To summarize, we verify the effectiveness of developed bi-objective stochastic dispatch model could successfully obtain feasible solutions and Pareto front. On this basis, the trade-off relationship between wind power utilization and capacity margin of transmission lines is revealed. Afterwards, the outperformance of proposed DBAO algorithm regarding solving time and searching efficiency is testified, compared to other four optimization algorithms. Finally, sensitivity analysis in terms of our presented dispatch model and four important parameters is discussed in this section, including wind power penetration rate, sample distribution, consumption level of user loads and locations of wind farms.

## 5. Conclusion

In this paper, a bi-objective stochastic dispatch model for OPSD with high RE penetration is proposed to investigate the relationship between wind power curtailment and capacity margin of transmission lines. Especially, this proposed model simulates wind power uncertainties as random variables, and uses scenarios to analyze objective values. Then, an optimization algorithm DBAO, based on BEO and EDA, is proposed to solve the bi-objective stochastic dispatch problem.

Case studies based on the modified Midwestern US power system have been conducted to verify the effectiveness of the proposed stochastic dispatch model and data-driven optimization algorithm DBAO. The results indicate that a higher wind power curtailment corresponds to a larger capacity margin of transmission lines. In addition, the analysis of algorithm performance reveals the advantages of DBAO over several benchmark optimization algorithms in terms of searching ability and computational efficiency.

Although the proposed DBAO optimization algorithm has achieved satisfying results for the optimal power system dispatch problems, some aspects should still be concentrated on for further researches. Firstly, the maximal iteration number of optimization algorithm could be increased to further study the performance of DBAO. In our case, this maximum is set as 200 since the OPSD problem is regarded computational expensive, especially taking the uncertainty of renewable energy into account. Secondly, our framework is based on the moth flame optimization algorithm, which could also be combined with other heuristic algorithms. The effects of different evolutionary algorithms on the final optimization results are worth investigating. Thirdly, some parameters of DBAO are adaptively adjusted while the parameters of surrogate model are predefined. Consequently, developing an adaptive tuning method for updating surrogates will also be our future research work.

## CRediT authorship contribution statement

Chaofan Yu: Data curation, Writing - original draft, Software, Writing - review \& editing. Yuanzheng Li: Conceptualization, Methodology,Writing - review \& editing, Supervision. Yun Liu: Visualization, Investigation, Conceptualization. Leijiao Ge: Validation. Hao Wang: Supervision. Yunfeng Luo: Supervision. Linqiang Pan: Supervision.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## References

[1] R. Ren, M. Tang, H. Liao, Managing minority opinions in micro-grid planning by a social network analysis-based large scale group decision making method with hesitant fuzzy linguistic information, Knowl.-Based Syst. 189 (2020) 105060.
[2] Y. He, W. Zhang, Probability density forecasting of wind power based on multicore parallel quantile regression neural network, Knowl.-Based Syst. 209 (2020) 106431.
[3] F. Liu, F. Sun, W. Liu, T. Wang, H. Wang, X. Wang, W.H. Lim, On wind speed pattern and energy potential in China, Appl. Energy 236 (2019) 867-876.
[4] S. Robak, J. Machowski, K. Gryzapanowicz, Automatic alleviation of overloads in transmission network by generation curtailment, IEEE Trans. Power Syst. 33 (4) (2017) 4424-4432.
[5] National Energy Administration, Integrated wind power operation in the first three quarters of 2019 in China, 2019, http://www.nea.gov.cn/2019-11/04/c_ 138527392.htm.
[6] G. Piperagkas, A. Anastasiadis, N. Hatziargyriou, Stochastic PSO-based heat and power dispatch under environmental constraints incorporating CHP and wind power units, Electr. Power Syst. Res. 81 (1) (2011) 209-218.
[7] Y. Chi, Y. Xu, R. Zhang, Many-objective robust optimization for dynamic VAR planning to enhance voltage stability of a wind-energy power system, IEEE Trans. Power Deliv. 36 (1) (2021) 30-42.
[8] R. Jiang, J. Wang, Y. Guan, Robust unit commitment with wind power and pumped storage hydro, IEEE Trans. Power Syst. 27 (2) (2012) 800-810.
[9] Y. Zhang, N. Gatsis, G.R. Giannakis, Robust energy management for microgrids with high-penetration renewables, IEEE Trans. Sustain. Energy 4 (4) (2013) 944-953.
[10] W. Wu, J. Chen, B. Zhang, H. Sun, A robust wind power optimization method for look-ahead power dispatch, IEEE Trans. Sustain. Energy 5 (2) (2014) 507-515.
[11] P. Meibom, R. Barth, B. Hasche, H. Brand, C. Weber, M. O'Malley, Stochastic optimization model to study the operational impacts of high wind penetrations in Ireland, IEEE Trans. Power Syst. 26 (3) (2011) 1367-1379.
[12] H. Park, Y.G. Jin, J. Park, Stochastic security-constrained unit commitment with wind power generation based on dynamic line rating, Int. J. Electr. Power Energy Syst. 102 (2018) 211-222.
[13] B. Banerjee, D. Jayaweera, S. Islam, Risk constrained short-term scheduling with dynamic line ratings for increased penetration of wind power, Renew. Energy 83 (2015) 1139-1146.
[14] H. Sharifzadeh, N. Amjady, H. Zareipour, Multi-period stochastic securityconstrained OPF considering the uncertainty sources of wind power, load demand and equipment unavailability, Electr. Power Syst. Res. 146 (2017) 33-42.
[15] M.A. Mirzaei, A.S. Yazdankhah, B. Mohammadi-Ivarloo, Stochastic securityconstrained operation of wind and hydrogen energy storage systems integrated with price-based demand response, Int. J. Hydrogen Energy 44 (27) (2019) $14217-14227$.
[16] X. Zhu, Z. Yu, X. Liu, Security constrained unit commitment with extreme wind scenarios, J. Mod. Power Syst. Clean Energy 8 (3) (2020) 464-472.
[17] S.M. Mohami Bouah, I. Kamwa, A. Moeini, A. Rabiee, Voltage security constrained stochastic programming model for day-ahead BESS schedule in co-optimization of 7\&D systems, IEEE Trans. Sustain. Energy 11 (1) (2019) 391-404.
[18] Y. Li, G. Hao, Y. Liu, Y. Yu, Z. Ni, Y. Zhao, Many-objective distribution network reconfiguration via deep reinforcement learning assisted optimization algorithm, IEEE Trans. Power Deliv. 37 (3) (2022) 2230-2244.
[19] N.O. Aljehane, R.F. Mansour, Optimal allocation of renewable energy source and charging station for PHEVs, Sustain. Energy Technol. Assess. 49 (2022) 101669.
[20] F. Abokhodair, W. Alsaggal, A.T. Jamal, S. Abdel Khalek, R.F. Mansour, An intelligent metadeuristic binary pigeon optimization-based feature selection and big data classification in a MapReduce environment, Mathematics 9 (20) (2021) 2627.
[21] A. Althobaiti, A.A. Alotaibi, S. Abdel-Khalek, E.M. Abdelrahim, R.F. Mansour, D. Gupta, S. Kumar, Intelligent data science enabled reactive power optimization of a distribution system, Sustain. Comput.: Inform. Syst. (2022) 100765.
[22] T. Zhong, H.T. Zhang, Y. Li, L. Liu, R. Lu, Bayesian learning-based multiobjective distribution power network reconfiguration, IEEE Trans. Smart Grid 12 (2) (2020) 1174-1184.
[23] Y. Li, Y. Cai, T. Zhao, Y. Liu, J. Wang, L. Wu, Y. Zhao, Multi-objective optimal operation of centralized battery swap charging system with photovoltaic, J. Mod. Power Syst. Clean Energy 10 (1) (2021) 149-162.
[24] Y. Li, Z. Ni, T. Zhao, M. Yu, Y. Liu, L. Wu, Y. Zhao, Coordinated scheduling for improving uncertain wind power adsorption in electric vehicles-Wind integrated power systems by multiobjective optimization approach, IEEE Trans. Ind. Appl. 56 (3) (2020) 2238-2250.
[25] M. Albazmi, P. Dehghanian, S. Wang, B. Shinde, Power grid optimal topology control considering correlations of system uncertainties, IEEE Trans. Ind. Appl. 55 (6) (2019) 5594-5604.
[26] S. Mirjalili, Moth-flame optimization algorithm: A novel nature-inspired heuristic paradigm, Knowl.-Based Syst. 89 (2015) 228-249.
[27] Y. Xu, H. Chen, J. Luo, Q. Zhang, S. Jiao, X. Zhang, Enhanced Moth-flame optimizer with mutation strategy for global optimization, Inform. Sci. 492 (2019) 181-203.
[28] Z. Li, Y. Li, Y. Liu, P. Wang, R. Lu, H.B. Gooi, Deep learning based densely connected network for load forecasting, IEEE Trans. Power Syst. 36 (4) (2021) 2829-2840.
[29] Z. Ghahramani, Probabilistic machine learning and artificial intelligence, Nature 521 (7553) (2015) 452-459.
[30] B. Shahriari, K. Swersky, Z. Wang, R.P. Adams, N. de Freitas, Taking the human out of the loop: A review of Bayesian optimization, Proc. IEEE 104 (1) (2016) $148-175$.
[31] S. Greenhill, S. Rana, S. Gupta, P. Vellanki, S. Venkatesh, Bayesian optimization for adaptive experimental design: A review, IEEE Access 8 (2020) 13937-13948.
[32] S. Qin, C. Sun, Y. Jin, G. Zhang, Bayesian approaches to surrogate-assisted evolutionary multi-objective optimization: A comparative study, in: 2019 IEEE Symposium Series on Computational Intelligence, SSCI, 2019, pp. 2074-2080.
[33] D. Zhan, Y. Cheng, J. Liu, Expected improvement matrix-based infill criteria for expensive multiobjective optimization, IEEE Trans. Evol. Comput. 21 (6) (2017) 956-975.
[34] J. Sacks, W.J. Welch, T.J. Mitchell, H.P. Wynn, Design and analysis of computer experiments, Statist. Sci. 4 (1989) 409-423.
[35] S. Xiao, G. Liu, K. Zhang, Y. Jing, J. Duan, P. Di Barba, J. Sykulski, Multiobjective puesto optimization of electromagnetic devices exploiting Kriging with lipschitzian optimized expected improvement, IEEE Trans. Magn. 54 (3) (2018) $1-4$.

[36] Z. Deng, M.D. Rotaru, J.K. Sykulski, Kriging assisted surrogate evolutionary computation to solve optimal power flow problems, IEEE Trans. Power Syst. 35 (2) (2019) 831-839.
[37] N. Namura, K. Shimoyama, S. Obayashi, Expected improvement of penalty-based boundary intersection for expensive multiobjective optimization, IEEE Trans. Evol. Comput. 21 (6) (2017) 898-913.
[38] Q. Yang, W. Chen, Y. Li, C.P. Chen, X. Xu, J. Zhang, Multimodal estimation of distribution algorithms, IEEE Trans. Cybern. 47 (3) (2016) 636-650.
[39] X. Liang, H. Chen, J.A. Lozano, A Boltzmann-based estimation of distribution algorithm for a general resource scheduling model, IEEE Trans. Evol. Comput. 19 (6) (2015) 793-806.
[40] R. Christie, Power systems test case archive, 2015, http://labs.ece.uw.edu/pstca/ $\mathrm{pC} 01 / \mathrm{pg} \_$tca30bus.htm.
[41] Q. Zhang, H. Li, MOEA/D: A multiobjective evolutionary algorithm based on decomposition, IEEE Trans. Evol. Comput. 11 (6) (2007) 712-731.
[42] K. Deb, A. Pratap, S. Agarwal, T. Meyarivan, A fast and elitist multiobjective genetic algorithm: NSGA-II, IEEE Trans. Evol. Comput. 6 (2) (2002) 182-197.
[43] J.P. Brans, P. Virecke, B. Mareschal, How to select and how to rank projects: The PROMETHEE method, European J. Oper. Res. 24 (2) (1986) 228-238.
[44] Y. Li, J. Huang, Y. Liu, Z. Ni, Y. Shen, W. Hu, L. Wu, Economic dispatch with high penetration of wind power using extreme learning machine assisted group search optimizer with multiple producers considering upside potential and downside risk, J. Mod. Power Syst. Clean Energy 10 (6) (2022) 1459-1471.