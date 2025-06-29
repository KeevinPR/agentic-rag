# Process optimization of microbial fermentation with parameter uncertainties via distributionally robust discrete control 

Juan Wang ${ }^{\mathrm{a}, *}$, Chihua Chen ${ }^{\mathrm{a}}$, Feiyan Zhao ${ }^{\mathrm{a}}$, Jichao Wang ${ }^{\mathrm{a}}$, An Li ${ }^{\mathrm{b}}$<br>${ }^{a}$ College of Science, China University of Petroleum, Qingdao 266580, Shandong, China<br>${ }^{\mathrm{b}}$ School of Mathematical Sciences, Xiamen University, Xiamen, 361005, Fujian, China

## ARTICLE INFO

Keywords
Distributionally robust control
Uncertainty
Estimation of distribution algorithms
Duality theory
Continuous fermentation

## ABSTRACT

There are some uncertain kinetic parameters in microbial fermentation system because of the unclear intracellular metabolic mechanisms. Considering the affection of these uncertain parameters on system performance, dynamic process optimization of the fermentation system can be modeled as a distributionally robust discrete control problem under moment uncertainty, which aims to maximize the mean productivity by optimizing the discrete-valued dilution rate function. Based on duality theory, the established min-max discrete optimal control problem is first transformed into a single level minimization problem, which is then discretized into a large-scale parameter optimization problem with semi-infinite constraint via time transformation and control parameterization. A new two-step estimation of distribution algorithm is developed to solve the obtained largescale optimization problem. Numerical results show the feasibility and effectiveness of the proposed solution approach together with the superiority of the obtained control strategy considering parameter uncertainties.

## 1. Introduction

Glycerol bioconversion to 1,3-propanediol (1,3-PD) by Klebsiella pneumoniae (K. pneumoniae) is of great significance to industry since 1,3-PD is an important chemical raw materials with a numerous applications in manufacture of polymers, cosmetics, food and lubricants [1]. Because of higher productivity of 1,3-PD, continuous fermentation is more popular than the other two widely used fermentation modes, i.e., batch fermentation and fed-batch fermentation [2]. In this bioconversion process, glycerol is added to the bio-reactor continuously, and the broth in bio-reactor pours out at the same rate. In 1995, Zeng et al. established an excess kinetic model for substrate consumption and product formation in continuous fermentation without considering the intracellular metabolism [3]. In 2008, Sun et al. set up a novel mathematical model to describe glycerol continuous and batch fermentations considering both extracellular and intracellular metabolism [4]. Based on this mathematical model, some scholars have made efforts in parameter identification (see $[5,6]$ ) and optimal control (see [7-9]).

In view of the high cost of diol recovery from aqueous solution, how to improve product concentration or productivity of glycerol bioconversion to 1,3-PD has attracted considerable research interest over the past years. Bao et al. presented an impulsive optimal control problem to maximize the concentration of 1,3-PD at the terminal time, taking the feeding volumes of glycerol and the feeding time points as decision variables [10]. Wang et al. took the input feeding rate
as control variable to design a trade-off strategy between final 1,3PD yield and switching cost [11]. Sattayasamitsathit et al. investigated two-phase pH -controlled strategy to improve yield and productivity of 1,3-PD in batch and fed-batch fermentation [12]. In continuous fermentation, optimizing dilution rate of the feed medium is one of the most effective methods to improve concentration or productivity. In $[13,14]$, dilution rate was taken as a time-independent parameter to optimize the continuous bioconversion process of glycerol. Considering the different demand of glycerol in different fermentation stage, some researchers took dilution rate in continuous fermentation as a timevarying continuous function [15-17]. However, it is undesirable and inoperable to continuously change dilution rate in practice. In fact, there are often several candidate operable modes to choose from. In this paper, considering the limitations of laboratory operating conditions, we shall take dilution rate as a time-varying discrete-valued function and formulate the process control of glycerol continuous bioconversion by a discrete optimal control problem.

Due to the lack of intracellular experimental data and the unclear intracellular metabolic mechanisms, there are some uncertain kinetic parameters in glycerol fermentation dynamic system. In view of the important affection of these uncertain parameters on system performance, it is of practical significance to consider parameter uncertainty in the determination of optimal control operation. Actually, many papers have

[^0]
[^0]:    * Corresponding author.

    E-mail address: wangj@upc.edu.cn (J. Wang).

![img-0.jpeg](img-0.jpeg)

Fig. 1. Diagram of simple fermentation device and main metabolism pathways of glycerol continuous fermentation.
taken this issue into account and a series of robust suboptimal control problems are proposed based on system sensitivity [9,18-20]. These papers focus on obtaining an optimal control strategy which can balance parameter sensitivity and system performance through multi-objective optimization. Unfortunately, there is great subjectivity and personal preference in the strategy obtained through multi-objective optimization. A more appropriate framework is robust optimization which has classically allowed to model this uncertainty within a decision-making framework [21]. Under this framework, He et al. presented a robust optimization approach considering power system key uncertainties and natural gas system dynamics [22]. Kumawat et al. proposed robust formulations to target the resource minimization constraints for continuous and batch processes under uncertainties related to internal resources [23]. However, the above studies attempt to overcome all the uncertainties, including the worst case, even though the possibility of such a situation in practice is very small. Even more unfortunately, such a conservative scheme may reduce performance without any return. However, distributionally robust optimization (DRO), which can overcome the shortcoming of robust optimization, has been widely studied in recent years [24,25]. The first paper to study DRO can be traced back to the work for the newsboy problem [26]. In recent years, many new advances have been made in the research of DRO, including stochastic linear optimization problem [27], two-stage problem [28] and moment uncertainty [29,30]. To make full use of the historical data, an ambiguity set is usually constructed in DRO models which is assumed to include the true distribution of uncertain data according to empirical estimates, such as, moment information [31] or empirical distribution [32,33]. Considering that it is also rarely the case that one is entirely confident in these estimates, Delage et al. constructed a wellknown ambiguity set under moment uncertainty [34], in which two constraints were used to represent this uncertainty. In [35], Gong et al. discussed distributionally robust optimization of glycerol batch fermentation to estimate the kinetic parameters of the metabolic system, in which the measured data are taken as stochastic variables. In this work, different from the work of Gong et al. we consider the bioprocess control of another fermentation (continuous fermentation) to optimize the dilution rate by solving a distributionally robust discrete control problem (DRDCP) under moment uncertainty, where the uncertain kinetic parameters are regarded as stochastic variables and only the existence interval of first-order moment is available for the uncertain parameters.

The main difficulty of solving the DRO problem lies in the infinitely many constraints. The numerical methods to solve the DRO problem vary greatly depending on the specific problem, and the existing papers do not provide us with much reference for solving our problem. More specifically, many papers are devoted to converting DRO problem to a tractable semidefinite programming problem which can be easily solved by many versatile numerical methods. For example, Zhao et al. reformulated the presented model as a tractable semidefinite programming problem and solved it by a constraint generation algorithm [36]. In [37], a knotty model is reformulated using the linear decision rule to obtain the tight and tractable problems, and the MAD-based ambiguity set combined with the approximation technique is used to reduce the solution time and to get high-quality solutions [37]. However, this equivalence transformation method is highly skilled and not applicable to all problems. Another common method is the cutting surface method. This method first considers only a portion of the constraint conditions to obtain the local optimal value, and then gradually adds constraints until the global optimal value is obtained [38,39]. However, this method may bring high computational costs, which is the reason why it is less used in actual production, even though it has been welldeveloped in the literature [40]. The most straightforward method is the discretization method, which makes the DRO problem become a solvable problem with finite constraints. In this paper, the proposed problem shall be firstly discretized by the Monte Carlo method and then solved by a new estimation of distribution algorithm.

The present paper studies the process optimization of glycerol continuous bioconversion to 1,3-PD where dilution rate of the feed medium taking values in a discrete set and the intracellular parameters are considered to be uncertain. This process optimization is formulated by a distributionally robust discrete control problem (DRDCP) with uncertain parameters as stochastic variables, which is essentially a bilevel min-max problem. The duality theory in probability spaces is applied to convert the min-max problem into a single level minimization problem with semi-infinite constraints. Then, using a time transformation proposed in [41] and discretization technique, the proposed DRDCP is transformed into a large-scale parameter optimization problem, which is finally solved by using a new two-step estimation of distribution algorithm (EDA). Numerical results show the effectiveness of the optimal strategy for industrial process with uncertain parameters and the feasibility of the numerical methods for solving DRDCP.

The main contributions of this paper can be summarized as follows:

- Considering the impact of parameter uncertainties on system performance, we propose a DRDCP under moment uncertainty to describe the bioprocess control of glycerol continuous fermentation with uncertain parameters, where the existence interval of the first-order moment of parameters is available. The obtained control strategy is verified to make the metabolism system more robust to parameter uncertainties than the general control strategy.
- A new two-step EDA is developed to solve the transformed largescale optimization problem with semi-infinite constraints. The proposed algorithm has been shown to have better performance in searching the best solution and better robustness in repeated execution than the basic EDA for our transformed problem.

This paper is organized as follows. A min-max DRDCP is proposed to describe the process optimization of glycerol continuous fermentation in Section 2. The transformation procedure, which includes duality theory, time transformation, and discretization is given in Section 3. Section 4 devotes to solving the transformed problem numerically by using a new two-step estimation of distribution algorithm, while Section 5 illustrates the numerical results. Section 6 concludes the paper.

## 2. Problem formulation

### 2.1. Dynamical system

In this work, we consider a continuous conversion process of glycerol to 1,3-PD by K. pneumoniae based on our previous work [42]. In Fig. 1, the diagram on the left describes the simple continuous fermentation device and the right one describes the main metabolism pathways of glycerol fermentation. As shown in the left diagram of Fig. 1, in continuous fermentation, glycerol solution with a concentration of $C_{0}$ is added to the reactor continuously through the inlet pipe, the broth in reactor pours out at the same rate through the outlet pipe and the volume of the fermentation broth keeps constant during the whole fermentation process. $x_{1}, x_{2}, x_{3}, x_{4}$ and $x_{5}$ are state variables representing the concentrations of biomass, glycerol, 1,3-PD, acetate and ethanol in the fermentation broth, respectively. Dilution rate $D$ of the feed medium is regarded as the control variable, and this work aims to design an optimal dilution rate function $D(t)$ to improve the productivity of target product 1,3-PD for this continuous fermentation with parameter uncertainty.

The fermentations of glycerol is a complex metabolism process covering both extracellular and intracellular environments. The two environments are linked by the transports of substrate and products across cell membrane. To describe this metabolism process as clearly as possible, we also draw a magnified figure of biomass cell in the right diagram of Fig. 1 to show the main metabolism pathways of glycerol fermentation according to [4]. Under anaerobic conditions, glycerol is dissimilated through coupled oxidative and reductive pathways and the latter generates the goal product 1,3-PD as shown in the right metabolism diagram of Fig. 1. Due to the complexity of the oxidative pathway and lack of experimental data, we considered the oxidative pathway as a 'black box' model, i.e., only the input and output in this pathway are considered but the details in the intermediate process are ignored. The reductive pathway will be emphasized in this work because 3-hydroxypropionaldehyde (3-HPA) is the key intermediate for 1,3-PD production.

According to the experiment process, we assume that
(H1) The concentrations of reactants are uniform in the reactor, time delay and nonuniform space distribution are ignored.
(H2) During the process of continuous culture, the substrate added to the reactor only includes glycerol.

Denote the intracellular concentrations of glycerol, 3-HPA and 1,3PD by $x_{6}, x_{7}$ and $x_{8}$, respectively. Let $\mathbf{x}(t):=\left(x_{1}(t), x_{2}(t), \ldots, x_{8}(t)\right)^{\top} \in$ $\mathbb{R}_{+}^{8}$ be the state vector. Under the assumptions (H1)-(H2), the continuous conversion process can be described as the following system on the fixed time interval $\left[0, t_{f}\right]$ :

$$
\dot{\mathbf{x}}(t)=\mathbf{F}(\mathbf{x}(t), D(t), \mathbf{p})
$$

with the given initial condition $\mathbf{x}(0)=\mathbf{x}^{0}$. In (2.1), $D(t)$ represents dilution rate of the feed medium, which is a key operational control in continuous culture. $\mathbf{p}=\left(p_{1}, \ldots, p_{17}\right)^{\top}$ is the vector of intracellular uncertain kinetic parameters. By the literature [42], the right hand side of system (2.1) is of the form $\mathbf{F}(\mathbf{x}(t), D(t), \mathbf{p})=\left(f_{1}(\mathbf{x}(t), D(t), \mathbf{p}), \ldots, f_{8}(\mathbf{x}(t), D(t), \mathbf{p})\right)^{\top}$ with the components defined as

$$
\left\{\begin{array}{l}
f_{1}(\mathbf{x}(t), D(t), \mathbf{p})=(\mu(t)-D(t)) x_{1}(t) \\
f_{2}(\mathbf{x}(t), D(t), \mathbf{p})=D(t)\left(C_{0}-x_{2}(t)\right)-r_{2}(t) x_{1}(t) \\
f_{i}(\mathbf{x}(t), D(t), \mathbf{p})=r_{i}(t) x_{1}(t)-D(t) x_{i}(t), i=3,4,5 \\
f_{6}(\mathbf{x}(t), D(t), \mathbf{p})=\frac{p_{1} x_{7}(t)}{x_{2}(t)+p_{2}}+p_{3}\left(x_{2}(t)-x_{6}(t)\right)-p_{4} r_{1}(t)-\mu(t) x_{6}(t) \\
f_{7}(\mathbf{x}(t), D(t), \mathbf{p})=\frac{p_{5} x_{6}(t)}{K_{m}^{G}\left(1+\frac{x_{7}(t)}{p_{6}}\right)+x_{6}(t)} \\
-\frac{p_{7} x_{7}(t)}{K_{m}^{P}+x_{7}\left(1+\frac{x_{7}(t)}{p_{8}}\right)}-\mu(t) x_{7}(t) \\
f_{8}(\mathbf{x}(t), D(t), \mathbf{p})=\frac{p_{7} x_{7}(t)}{K_{m}^{P}+x_{7}\left(t\right)\left(1+\frac{x_{7}(t)}{p_{8}}\right)} \\
-\frac{p_{9} x_{8}(t)}{x_{8}(t)+p_{10}}-p_{11}\left(x_{8}(t)-x_{3}(t)\right)-\mu(t) x_{8}(t)
\end{array}\right.
$$

where $C_{0}$ is the given initial glycerol concentration in the feed medium. According to [4], $K_{m}^{P}$ and $K_{m}^{G}$ are Michaelis-Menten constants, which are of $0.53 \mathrm{mmol} \mathrm{L}^{-1}$ and $0.14 \mathrm{mmol} \mathrm{L}^{-1}$, respectively. According to $[4,42]$, the specific growth rate of cells $\mu(t)$, specific consumption rate of substrate $r_{i}(t)(\dot{i}=1,2)$ and specific formation rate of products $r_{i}(t)(\dot{i}=3,4,5)$ are expressed by the following equations.

$$
\left\{\begin{array}{l}
\mu(t)=\mu_{m} \frac{x_{2}(t)}{x_{2}(t)+K_{s}} \prod_{i=1}^{3}\left(1-\frac{x_{i}(t)}{x_{i}^{*}}\right) \\
r_{1}(t)=P_{1}+\frac{\mu(t)}{P_{2}}+P_{1} \frac{x_{3}(t)}{x_{2}(t)+P_{4}} \\
r_{2}(t)=\frac{p_{12} x_{2}(t)}{x_{2}(t)+p_{13}}+p_{14}\left(x_{2}(t)-x_{6}(t)\right) \\
r_{3}(t)=\frac{p_{15} x_{8}(t)}{x_{8}(t)+p_{16}}+p_{17}\left(x_{8}(t)-x_{3}(t)\right) \\
r_{4}(t)=P_{5}+P_{6} \mu(t)+P_{7} \frac{x_{7}(t)}{x_{7}(t)+P_{8}} \\
r_{5}(t)=r_{2}(t) \frac{P_{9}}{P_{10}+D(t) x_{2}(t)}+\frac{P_{11}}{P_{12}+D(t) x_{3}(t)}
\end{array}\right.
$$

According to $[3,43]$, the maximum growth rate $\mu_{m}$ is $0.67 \mathrm{~h}^{-1}$ and Monod constant $K_{s}$ is 0.28 mmol L $^{-1}$ under anaerobic conditions at $37^{\circ} \mathrm{C}$ and pH 7.0 . The critical concentrations are $x_{1}^{*}=10 \mathrm{~g} \mathrm{~L}^{-1}$ for biomass, $x_{2}^{*}=x_{3}^{*}=2039 \mathrm{mmol} \mathrm{L}^{-1}$ for glycerol, $x_{3}^{*}=x_{4}^{*}=939.5 \mathrm{mmol}$ $\mathrm{L}^{-1}$ for 1,3-PD, $x_{4}^{*}=1026 \mathrm{mmol} \mathrm{L}^{-1}$ for acetate, $x_{5}^{*}=360.9 \mathrm{mmol} \mathrm{L}^{-1}$ for ethanol, and $x_{7}^{*}=30 \mathrm{mmol} \mathrm{L}^{-1}$ for 3-HPA. Extracellular kinetic parameters $P_{i}(i=1, \ldots, 12)$ and intracellular parameters $p_{i}(i=1, \ldots, 17)$ can be identified via biological robustness, and their values are given in Table 1 according to [42,44]. Here, we consider the identified intracellular parameters $p_{i}$ to be uncertain since the concentrations of intracellular substances are difficult to be accurately measured due to technical limitations and unclear intracellular metabolism.

Table 1
The values of parameters $P_{1}(i=1, \ldots, 12)$ and $p_{2}(i=1, \ldots, 17)$.

| $P_{1}$ | $P_{2}$ | $P_{3}$ | $P_{4}$ | $P_{5}$ | $P_{6}$ | $P_{7}$ | $P_{8}$ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 2.1854 | 0.0082 | 31.2328 | 11.43 | $-1.345$ | 30.8599 | 5.0099 | 85.71 |
| $P_{2}$ | $P_{10}$ | $P_{11}$ | $P_{12}$ | $p_{1}$ | $p_{2}$ | $p_{3}$ | $p_{4}$ |
| 0.0025 | 0.06 | 5.18 | 50.45 | 6.8135 | 2.3080 | 362.8623 | 0.1086 |
| $p_{3}$ | $p_{6}$ | $p_{7}$ | $p_{8}$ | $p_{9}$ | $p_{10}$ | $p_{11}$ | $p_{12}$ |
| 35.8174 | 268.7080 | 24.1471 | 1.4359 | 7.2118 | 30.2732 | 80.1388 | 67.5923 |
| $p_{13}$ | $p_{14}$ | $p_{15}$ | $p_{16}$ | $p_{11}$ |  |  |  |
| 1.6099 | 471.7370 | 16.0973 | 1.3844 | 23.7976 |  |  |  |

In practice, since it is undesirable and inoperable to continuously change dilution rate $D(t)$ over $t \in\left[0, t_{f}\right]$, we assume that there are several candidate operable modes to choose from. Let $M$ be the number of such levels and $D=\left\{d^{1}, d^{2}, \ldots, d^{M}\right\}$ be set of operable modes in which the components represent the certain operable dilution rates in the laboratory. Then, we define the admissible control set $D_{a d}$ as
$D_{a d}:=\{D(\cdot): D(t) \in D, \forall t \in\left[0, t_{f}\right]\}$.
Similarly, the admissible state set $X_{a d}$ is defined as
$X_{a d}:=\left\{\mathbf{x}(\cdot): \mathbf{x}(t) \in \prod_{i=1}^{8}\left[0, x_{i}^{*}\right], \forall t \in\left[0, t_{f}\right]\right\}$.
Based on the classical theory of differential equations, similarly to [42], it is easy to show that the following property holds.

Property 1. For a fixed $\mathbf{x}^{0} \in X_{a d}$ and given $\boldsymbol{p}, D(\cdot) \in D_{a d}$, there exists a unique solution to system (2.1), denoted by $\mathbf{x}(\cdot ; D(\cdot), \boldsymbol{p})$. Furthermore, $\mathbf{x}(\cdot ; D(\cdot), \boldsymbol{p})$ is continuous in $D(\cdot)$ on $D_{a d}$.

### 2.2. The proposed DRDCP

In order to improve productivity of product which is a major optimization objective in continuous culture, we define mean productivity of $1,3-\mathrm{PD}$ during the whole fermentation process as
$\frac{1}{t_{f}} \int_{0}^{t_{f}} D(t) x_{3}(t ; D(t), \mathbf{p}) d t$.
And, considering the influence of the uncertainty of intracellular parameter $\mathbf{p}:=\left(p_{1}, p_{2}, \ldots, p_{17}\right)^{\mathrm{T}}$ on system state $\mathbf{x}(t)$, our optimization object is to minimize an objective function $J(D, \mathbf{p})$ formulated as follows.
$\min _{D} J(D, \mathbf{p}):=-\frac{1}{t_{f}} \int_{0}^{t_{f}} D(t) x_{3}(t ; D(t), \mathbf{p}) d t$.
Due to the limitation of level of measurement in laboratory, some intracellular metabolism mechanisms of glycerol fermentation are still not clear and the experimental data of intracellular metabolites still lack, which make the exact value of intracellular parameter $\mathbf{p}$ cannot be determined. However, based on the results of a certain number of experiments given in [2], we can determine the variation range of the mean value of $\mathbf{p}$. In order to develop a less conservative control strategy, we abandon the conventional robust optimization framework and adopt a distributionally robust framework to describe the impact of the uncertainty of $\mathbf{p}$ on system performance.

Here, uncertain parameter $\mathbf{p}$ is regarded as a stochastic variable with its first-order moment given by
$\mathrm{E}_{\mathbb{P}}[\mathbf{p}]=\mu$
where $\mathrm{E}_{\mathbb{P}}$ represents the expectation under probability distribution of $\mathbb{P} ; \mu:=\left(\mu_{1}, \cdots, \mu_{17}\right)^{\mathrm{T}} \in \mathbb{R}_{+}^{\mathrm{T}}$. However, as mentioned above, the firstorder moment is a stochastic variable, and it is rarely the case that one is entirely confident in these estimates. Thus, we represent this uncertainty by
$\mathrm{E}_{\mathbb{P}}[\mathbf{p}] \in\left[\mu_{+}, \mu^{*}\right]$,
where $\mu_{+} \in \mathbb{R}_{+}^{\mathrm{T}}$ and $\mu^{*} \in \mathbb{R}_{+}^{\mathrm{T}}$ are given lower and upper bounds of $\mu$, respectively. Let $\Omega$ be the support set of $\mathbf{p}$ defined by
$\Omega:=\left\{\mathbf{p} \in \mathbb{R}_{+}^{\mathrm{T}}: \mathbf{p}_{+} \leq \mathbf{p} \leq \mathbf{p}^{*}\right\}$
where $\mathbf{p}_{+} \in \mathbb{R}_{+}^{\mathrm{T}}$ and $\mathbf{p}^{*} \in \mathbb{R}_{+}^{\mathrm{T}}$ are lower and upper bounds of $\mathbf{p}$, respectively. Let $F$ be the ambiguity set of probability measures of $\mathbf{p}$ defined by
$F:=\{\mathbb{P}: \mathbb{P} \mid \mathbf{p} \in \Omega\}=1, \mathrm{E}_{\mathbb{P}}[\mathbf{p}]=\mu\}$.
In view of the fact that we only know that the probability distribution $\mathbb{P}$ of the stochastic variable $\mathbf{p}$ is in the ambiguity set $F$. Thus, we define the worst-case scenario of $J(D, \mathbf{p})$ as
$\max _{\mathbb{P} \in F} \mathrm{E}_{\mathbb{P}}[J(D, \mathbf{p})]$,
and discuss the distributionally robust optimal control of glycerol continuous fermentation, which aims to minimize the worst-case scenario (2.12) by optimizing the discrete dilution rate $D(t)$. The corresponding optimization problem DRDCP under moment uncertainty is proposed as the following problem (P1).

Problem (P1). Given the controlled dynamic system (2.1), choose a control $D(\cdot) \in D_{a d}$ such that (2.12) is minimized subjected to state constraint $\mathbf{x}(\cdot) \in X_{a d}$.

Note that (P1) is a bilevel min-max dynamic optimization problem with discrete-valued control function which is difficult to be solved directly. Next, the duality theory in probability spaces shall be used to transform this problem into a min-min optimization problem with linear inner subproblem, which is further equivalently represented by a single-level minimization problem.

We start by considering the question of solving the inner maximization problem, and it can be explicitly expressed as
$(\mathbf{P}) \max _{\mathbb{P}} \mathrm{E}_{\mathbb{P}}[J(D, \mathbf{p})]$
s.t. $\mathrm{E}_{\mathbb{P}}[\mathbf{p}] \in\left[\mu_{+}, \mu^{*}\right]$,
$\mathbb{P}(\mathbf{p} \in \Omega)=1$
Assuming that $\mathbf{p}$ is the absolutely continuous stochastic variable, the expectation $\mathrm{E}_{\mathbb{P}}[J(D, \mathbf{p})]$ can be expressed by Lebesgue integral on $\Omega$. Thus, (IP) can be rewritten as
$(\mathbf{R IP}) \max _{\mathbb{P}} \int_{\Omega} J(D, \mathbf{p}) \mathrm{d} \mathbb{P}$
s.t. $\int_{\Omega} \mathbf{p} \mathrm{d} \mathbb{P} \in\left[\mu_{+}, \mu^{*}\right]$,
$\int_{\Omega} 1_{(\mathbf{p} \in \Omega)} \mathrm{d} \mathbb{P}=1$
Then, making use of duality theory, the inner maximization problem (RIP) becomes
$(\mathbf{D IP}) \min _{\lambda, \gamma} \mathbf{a}^{\mathrm{T}} \lambda+\gamma$
s.t. $J(D, \mathbf{p})+\mathbf{b}^{\mathrm{T}} \lambda-\gamma \leq 0, \lambda \geq 0, \forall \mathbf{p} \in \Omega$.
where $\lambda \in \mathbb{R}_{+}^{\mathrm{M}}$ and $\gamma \in \mathbb{R}$ are dual variables; $\mathbf{a}:=\left(-\mu_{\mathrm{T}}^{\mathrm{T}}, \mu^{* \mathrm{~T}}\right)^{\mathrm{T}}$; $\mathbf{b}:=\left(\mathbf{p}^{\mathrm{T}},-\mathbf{p}^{\mathrm{T}}\right)^{\mathrm{T}}$. Therefore, (P1) can be transformed into the following minimization problem (P2).

Problem (P2). Given the controlled dynamic system (2.1), choose a control $D(\cdot) \in D_{a d}$ and a pair $(\lambda, \gamma) \in \mathbb{R}_{+}^{\mathrm{M}} \times \mathbb{R}$ such that $\mathbf{a}^{\mathrm{T}} \lambda+$ $\gamma$ is minimized subjected to semi-infinite constraint (2.14) and state constraint $\mathbf{x}(\cdot) \in X_{a d}$.

Note that (P2) is actually a min-min problem while the inner problem with dual variables $\lambda$ and $\gamma$ is a linear problem for a given $D$. And it is essentially equivalent to a single level minimization problem involving control $D(\cdot)$ and parameter pair $(\lambda, \gamma)$ whose values need to be determined. Here, dynamic system (2.1) belongs to a discrete-valued control system with $D(t)$ taking values in the discrete set $\left\{d^{1}, \ldots, d^{M}\right\}$ at all times. To determine the control function $D(t)$, we need to specify the order in which different dilution rates are implemented (the switching sequence) and the times at which dilution rates are changed (the switching times). Note that the total number of switches of $D(t)$ is also regarded as unknown for describing the fermentation process more accurately.

## 3. Problem transformation

In this section, a time transformation proposed in [41] is used to deal with the variable switching times and unknown total number of switches of problem (P2). Then the transformed problem is discretized into a large-scale parameter optimization problem.

### 3.1. Time transformation

Denote $I:=\left\{0, t_{f}\right\}$, which is equally divided into $N$ major intervals $I_{j}:=\left(t_{j-1}, t_{j}\right), j=1, \ldots, N$ with $N$ partition points denoted by $t_{1}, \ldots, t_{N}$, and $0=t_{0}<t_{1}<\cdots<t_{N}=t_{f}$. Then, let each $I_{j}$ be partitioned into $n$ minor intervals $I_{j}^{i}:=\left(\tau_{j}^{i-1}, \tau_{j}^{i}\right), i=1, \ldots, n$ with $n$ partition points denoted by $\tau_{j}^{1}, \ldots, \tau_{j}^{n}$, and $t_{j-1}=\tau_{j}^{1}<\cdots<\tau_{j}^{n}=t_{j}$.

Denote $\mathscr{L}^{\infty}(I, D)$ be the space of all functions $g$ with $g: I \mapsto$ $D$ (Lebesgue-) measurable and essentially bounded, thus $\|g\|_{\infty}:=$ $e s s \sup _{t \in I}\|g(t)\|_{\infty}<\infty$. Define an integer-valued control function $v$ in $\mathscr{L}^{\infty}(I, D)$, which takes values in $\{1,2, \ldots, M\}$. Let $\mathcal{V}$ denote the class of all such admissible integer-valued controls. Let $D(t):=d^{x(t)}, t \in\left[0, t_{f}\right]$. Then system (2.1) becomes
$\left\{\begin{array}{l}\dot{\mathbf{x}}(t)=\mathbf{F}\left(\mathbf{x}(t), d^{x(t)}\right), t \in\left[0, t_{f}\right], \\ \mathbf{x}(0)=\mathbf{x}^{0}\end{array}\right.$
By replacing system (2.1) with system (3.1) and $J(D, \mathbf{p})$ with $J_{1}(v):=$ $J\left(d^{v}, \mathbf{p}\right)$, we can represent problem (P2) equivalently as a new problem referred as problem (P3), which is obviously an integer-valued OCP with only $v \in \mathcal{V}$ to be determined.

Further, define a piecewise constant function $\bar{v}$ in $\mathscr{L}^{\infty}(I, D)$, which is constant on each minor interval $I_{j}^{i}$. Let $\mathcal{V}_{N}$ denote the class of all such admissible integer-valued controls. Similar to [9,41], we give the definition of control consistency as follows.

Definition 1. A function $\bar{v} \in \mathcal{V}_{N}$ is consistent to an integer-valued control $v \in \mathcal{V}$, if for all $j \in\{1, \ldots, N\}$ and a.e. $\zeta_{1}, \zeta_{2} \in I_{j}$ with $\zeta_{1}<\zeta_{2}$, exist $\xi_{1}, \xi_{2} \in I_{j}$ with

$$
\begin{aligned}
& -\xi_{1}<\xi_{2} \\
& -\bar{v}_{N, n}\left(\xi_{1}\right)=v\left(\zeta_{1}\right), \bar{v}\left(\xi_{2}\right)=v\left(\zeta_{2}\right)
\end{aligned}
$$

The function $\bar{v}$ is called control consistent if it is consistent to each integer-valued control $v \in \mathcal{V}_{N}$, that has at most one switch per major interval $I_{j}$.

Let $\left(I_{j}^{i}\right)_{i=1 j=1}^{N, n}$ be an ordered partition in major and minor intervals with $n=2 M-1$, where $M$ is the total number of operable modes for dilute rate. According to [41], we can construct the integer control function $\bar{v}_{N, n}$ which is consistent to each $v: I \mapsto\{1, \ldots, M\}$ with $n=2 M-1$ as
$\bar{v}(t):= \begin{cases}t \Leftrightarrow t \in I_{j}^{i}, & \text { for } i \in\{1, \ldots, M\}, \\ n+1-i \Leftrightarrow t \in I_{j}^{i}, & \text { for } i \in\{M+1, \ldots, n\}\end{cases}$
Next, we define a time-scaling function $t_{\omega}: I \mapsto I$ as
$t_{\omega}(\tau)=\int_{0}^{\tau} \omega(s) d s$
where $\omega \in \mathscr{L}^{\infty}(I, \mathbb{R})$ fulfills the properties
$\omega(\tau) \geq 0, \int_{I_{j}} \omega(s) d s=\frac{t_{f}}{N}, \forall j$.
According to the fundamental theorem of calculus, the time transformation function $t_{\omega}$ is absolutely continuous with $\frac{\partial t_{\omega}}{\partial t}=\omega(\tau)$ almost everywhere on $I$.

Remark 1. Any switching sequence and switching times can be obtained by scaling the minor intervals $I_{j}^{i}$, and it is obviously that several minor intervals shall be scaled to zero.

Now, in new time horizon, we can rewrite the control function $D(t)$ as
$D\left(t_{\omega}(\tau)\right)=d^{\left(\delta t_{\omega}(\tau)\right)}$.
Let $\hat{\mathbf{x}}(\tau):=\mathbf{x}\left(t_{\omega}(\tau)\right)$ and
$\hat{J}(\omega):=J_{1}\left(\bar{v}\left(t_{\omega}(\tau)\right)\right)=-\int_{0}^{t_{f}} \omega(\tau) d^{\left(\delta t_{\omega}(\tau)\right)} \hat{x}_{3}(\tau) d \tau$,
then problem (P3) can be transformed into the following equivalent continuous OCP.
(P4) $\min _{\omega, \lambda, \gamma} \hat{\mathbf{a}}^{\mathrm{T}} \lambda+\gamma$

$$
\begin{aligned}
& \hat{\mathbf{x}}(\tau)=\omega(\tau) \mathbf{F}\left(\hat{\mathbf{x}}(\tau), d^{\left(\delta t_{\omega}(\tau)\right)}\right), \quad \tau \in\left[0, t_{f}\right] \\
& \hat{\mathbf{x}}(0)=\mathbf{x}^{0} \\
& \text { s.t. } \begin{cases}J(\omega)+\mathbf{b}^{\mathrm{T}} \lambda-\gamma \leq 0, \lambda \geq 0 \\
\int_{I_{j}} \omega(s) d s=\frac{t_{f}}{N}, j=1, \ldots, N \\
\hat{\mathbf{x}}(\tau) \in \mathcal{X}_{a d}, \omega(\tau) \geq 0, \tau \in\left[0, t_{f}\right]
\end{cases}
\end{aligned}
$$

### 3.2. Discretization

In this subsection, problem (P4) shall be approximated to a largescale parameter optimization problem through direct single shooting method which is a common method to solve the OCP [45]. Direct single shooting method can transfer the infinite dimensional problem into finite dimensional nonlinear programming problem by discretizing the control function on fixed grid. That is, first discretize, then optimize.

For problem (P4), based on the time grid $\left\{I_{j}^{i}\right\}$ adopted in above time transformation, we approximate the control $\omega(\cdot)$ by a piecewise constant function, i.e.,
$\omega(\tau) \approx \sum_{j=1}^{N} \sum_{i=1}^{n} \omega_{j}^{i} \chi_{\left\{r_{j}^{i-1}, r_{j}^{i}\right\}}(\tau), \tau \in\left[0, t_{f}\right]$.
where $\chi_{\left\{r_{j-1}, r_{j}\right\}}:=\mathbb{R} \mapsto\{0,1\}$ is the characteristic function defined as
$\chi_{\left\{r_{j}^{i-1}, r_{j}^{i}\right\}}(\tau) \approx \begin{cases}1, & \text { if } \tau \in\left[\tau_{j}^{i-1}, \tau_{j}^{i}\right), \\ 0, \text { otherwise. }\end{cases}$
Similar to (3.4), $\omega_{j}^{i}$ satisfies
$\omega_{j}^{i} \geq 0, \quad \sum_{i=1}^{n} \omega_{j}^{i}=n, \quad i=1, \ldots, n, j=1, \ldots, N$.
However, to facilitate practical operation, there is usually a minimum dwell time constraint. Taking this into account, for a given minimum dwell time $\delta$, we modify the constraint $\omega_{j}^{i} \geq 0$ to $\Delta I_{j}^{i} \omega_{j}^{i} \geq \delta$ where $\Delta I_{j}^{i}=\tau_{j}^{i}-\tau_{j}^{i-1}=\frac{t_{f}}{N \pi \pi}$.

On this basis, the time transformation (3.3) can be given explicitly as
$t_{\omega}(\tau)=t_{j-1}+\sum_{k=1}^{i-1} \Delta I_{j}^{k} \omega_{j}^{k}+\left(\tau-\tau_{j}^{i-1}\right) \omega_{j}^{i}, \forall \tau \in\left[\tau_{j}^{i-1}, \tau_{j}^{i}\right]$.
We can also give the discretized version of control function $\bar{v}(\cdot)$ as
$\bar{v}\left(t_{\omega}(\tau)\right)=\sum_{j=1}^{N} \sum_{i=1}^{n} I_{j}^{i} \chi_{\left\{r_{j}^{i-1}, r_{j}^{i}\right\}}(\tau), \tau \in\left[0, t_{f}\right]$,
where $I_{j}^{i}=\bar{v}\left(t_{\omega}(\tau)\right)$ for $\tau \in\left[\tau_{j}^{i-1}, \tau_{j}^{i}\right)$. Denote $\theta:=\left(\omega_{1}^{1}, \ldots, \omega_{1}^{n}, \ldots, \omega_{N}^{1}, \ldots, \omega_{N}^{n}\right)^{\mathrm{T}} \in \mathcal{R}^{N \times n}$ and
$\hat{J}(\theta):=-\int_{0}^{t_{f}} \sum_{j=1}^{N} \sum_{i=1}^{n} \omega_{j}^{i} \chi_{\left\{r_{j}^{i-1}, r_{j}^{i}\right\}}(\tau) d^{t_{f}^{i}} \hat{x}_{3}(\tau)$.
Then (P4) can be converted into the following tractable parameter optimization problem.
(P5) $\min _{\theta, \lambda, \gamma} \hat{\mathbf{a}}^{\mathrm{T}} \lambda+\gamma$

$$
\begin{aligned}
& \text { s.t. } \begin{cases}\hat{\mathbf{x}}(\tau)=\sum_{j=1}^{N} \sum_{i=1}^{n} \omega_{j}^{i} \chi_{[t]^{-1}, \tau_{j}^{i}}(\tau) \mathbf{F}(\hat{\mathbf{x}}(\tau), d^{i j}), \tau \in\left[0, t_{f}\right] \\
\hat{\mathbf{x}}(0)=\mathbf{x}^{0}
\end{cases} \\
& \text { s.t. } \begin{cases}\hat{J}(\theta)+\mathbf{b}^{\mathrm{T}} \lambda-\gamma \leq 0, \lambda \geq 0 \\
\Delta \hat{I}_{j}^{i} \omega_{j}^{i} \geq \delta, \sum_{i=1}^{n} \omega_{j}^{i}=n, i=1, \ldots, n, j=1, \ldots, N
\end{cases} \\
& \hat{\mathbf{x}}(\tau) \in A_{a d}, \tau \in\left\{0, t_{f}\right\}
\end{aligned}
$$

Problem (P5) is a large-scale parameter optimization problem containing $(N \times n+35)$ decision variables with combinatorial constraint, semi-infinite constraint and functional inequality constraint which make the problem hard to solve numerically. In next section, we shall propose a feasible evolution technique to handle these difficulties.

## 4. A two-step estimation of distribution algorithm

The main difficulty of solving Problem (P5) lies in its complex constraints. In this section, we will first utilize Monte Carlo to deal with semi-infinite constraint, and then construct a two-step estimation of distribution algorithm (TSEDA) to solve the transformed problem. Here "two-step" refers to a two-step process of establishing probabilistic model; first, for a given $\theta$, to obtain the exact solution $\lambda$ and $\gamma$ of (P5); and second, for a series of $\theta$, to obtain a series of fitness values and further establish the probabilistic model.

Estimation of distribution algorithm (EDA) was first introduced by Mühlenbein in 1996 and has become the frontier research content in the field of evolutionary computation [46]. Belonging to the field of evolutionary computation, EDAs are a set of stochastic algorithms based on learning and sampling of probability model [47]. Unlike the traditional genetic algorithms that simulate various operations of natural evolution at the individual level, EDAs describe the distribution of candidate solutions in space through a probability model, and then sample the probability model to generate a new population, which promotes the evolution of the population on a macro level. This modelbased approach to optimization has allowed EDAs to solve many large and complex problems [48]. In recent years, many variants of EDAs have been proposed to deal with some special problems [49-51].

The execution of basic EDA in [46] includes four steps as follows: generating the population according to the uniform distribution over all admissible solutions, sorting the population in descending order of fitness values to further determine the optimal individuals, constructing the probability distribution model of the selected set, and then generating a set of new offspring individuals according to the probabilistic mode. Update the population repeatedly until the global optimal solution is obtained. In the proposed TSEDA, there are three main improvements based on the basic EDA in [46]: one is the two-step strategy, another is the linear decreasing strategy of selected solutions, and the third is the sine and cosine wave sampling.

The reason why a two-step strategy is introduced into the TSEDA is to consider the particularity of the large-scale problem (P5), which embodies that, for a given set of $\theta$, the optimization about dual variables $\lambda$ and $\gamma$ is only a linear programming problem with semi-infinite constraint. Considering their large value ranges, dual variables $\lambda$ and $\gamma$ can be optimized by using linprog function of Matlab. Thus, the TSEDA shall firstly optimize the dual variables $\lambda$ and $\gamma$ which are carried out in fitness assessment before optimizing $\theta$. Here fitness function of $(\lambda, \gamma)$ is denoted by $F i t(\lambda, \gamma):=\mathbf{a}^{\mathrm{T}} \lambda+\gamma$. Algorithm 1 shows the framework of fitness assessment.

The proposed TSEDA uses statistical learning methods to establish a probability model that describes the distribution of solutions from a macro perspective of the population. In order to accurately represent the evolutionary trend of the population in the probability model, according to the sorted candidate solutions, several top best solutions are

Algorithm 1 The framework of fitness assessment.

```
for each candidate solution \(\theta^{j}\) do
    Monte Carlo sampling and convert the semi infinite constraint
    to \(s_{i}\) general inequality constraints.
    Solve (P5) with fixed \(\theta^{j}\) using linprog function of Matlab.
        Obtain the optimal solution \(\lambda^{j}, \gamma^{j}\) and the corresponding
        \(F i t(\lambda, \gamma)\).
        Update the complete candidate solution \(\left(\theta^{j}, \lambda^{j}, \gamma^{j}\right)\) of (P5).
    end for
    Sort all candidate solutions \(\left\{\left(\theta^{j}, \lambda^{j}, \gamma^{j}\right)\right\}\).
```

selected to build Gaussian probabilistic model whose mean, variance and probability density function can be expressed as

$$
\left\{\begin{array}{l}
\hat{\mu}_{i}=\frac{\sum_{i=1}^{m} \theta_{i}^{j}}{m}, \hat{\sigma}_{j}^{2}=\frac{\sum_{i=1}^{m}\left(\theta_{i}^{j}-\hat{\mu}_{i}\right)^{2}}{m-1}, i=1,2, \ldots, N \times n, j=1,2, \ldots, m \\
h(\theta)=\frac{1}{\sqrt{2 \pi}} e^{-\frac{\left(\theta_{i}-\hat{\mu}_{i}\right)^{2}}{2 \pi_{j}^{2}}}
\end{array}\right.
$$

where $m$ is the number of selected solutions and $\theta_{i}^{j}$ represents the position of $i$ th dimension of $j$ th individual. To enhance the exploitation ability of the algorithm, we make an improvement for the expression of $m$ by adopting a linear decreasing strategy whose formula is given by
$m=m_{0}+\left(m_{0}-m_{K}\right) \frac{k-K}{K}$,
where $m_{0}$ and $m_{K}$ are initial number and final number, respectively. $k$ is the number of current iterations, $K$ is the maximum number of iterations.

Rounding off the non-integer values, a new population of the same size is then constructed by sampling in the above Gaussian probabilistic model according to the following formula

$$
\left\{\begin{array}{l}
\theta_{i}^{j_{1}}=\hat{\mu}_{i}+\hat{\sigma}_{i}\left(-2 \ln c_{1}\right)^{1 / 2} \cos 2 \pi c_{2} \\
\theta_{i}^{j_{2}}=\hat{\mu}_{i}+\hat{\sigma}_{i}\left(-2 \ln c_{1}\right)^{1 / 2} \sin 2 \pi c_{2}
\end{array}\right.
$$

where $c_{1}, c_{2}$ are independent random numbers uniformly distributed on $(0,1)$. Due to the differences in periodicity between sine and cosine functions, the above sine and cosine wave sampling may result in different distribution characteristics of the generated samples, which can increase the diversity of generated population. Then the sine and cosine wave sampling given in (4.3) is one more improvement of the proposed TSEDA.

After obtaining the new population, repeat the above operations to update the population iteratively until the termination condition of the algorithm is reached. Algorithm 2 summaries the framework of the proposed TSEDA. And the flowing chart of the proposed TSEDA for solving problem (P5) is shown in Fig. 2.

Note that, in solving problem (P5) by the proposed TSEDA, the semi infinite constraint is discretized into several inequality constraints by Monte Carlo method. The disadvantage of this method is that when the number of these inequalities is not sufficient, the approximation error is often uncontrollable. However, as the iteration progresses, the negative effect of this method will become weaker and weaker. The reason is that in the later stage of iteration, the algorithm slowly converges to a certain point, and the semi-infinite constraint corresponding to this point will be discretized frequently. In other words, when the algorithm converges to the optimal solution, it will also more frequently check whether the solution satisfies the semi-infinite constraint.

Algorithm 2 Framework of TSEDA. $k$ is the generation number. $\theta_{i}^{j}(k)$ represents the position of the current solution in $i$ th dimension and $j$ th individual at $k$ th iteration. $\theta_{i s}$ and $\theta_{i}^{*}$ represent the lower and upper bound of the solution in $i$ th dimension. $\left(\theta^{*}, \lambda^{*}, \gamma^{*}\right)$ and $J^{*}$ represent the approximate optimal solution and corresponding objective function value, respectively.

```
1: Set the total population \(N_{\text {sizp }}\), the maximum number of iterations
    \(K\), the constants \(\sigma_{0}, \sigma_{K}, s_{1}\) and \(m\). Set \(k=1\).
2: for \(j \leq N_{\text {sizp }}\) do
        for \(i \leq N \times n\) do
            \(\theta_{i}^{j}(k)=\theta_{i s}+\left(\theta_{i}^{*}-\theta_{i s}\right) \times \operatorname{rand}()\).
            \(i=i+1\).
            \(j=j+1\).
        end for
    end for
    for \(k \leq K\) do
    10: Fitness assessment.
    11: Select \(m\) top best solutions.
    12: for \(i \leq N \times n\) do
            Calculate \(\hat{\mu}_{i}(k)\) and \(\hat{\sigma}_{i}(k)\) according to formula (4.1).
            for \(j \leq N_{\text {sizp }}\) do
                Sampling \(\theta_{i}^{j}(k+1)\) according to formula (4.3).
            end for
        end for
        \(k=k+1\).
    end for
    20: Fitness assessment.
    21: Select the best solution \(\left(\theta^{*}, \lambda^{*}, \gamma^{*}\right)\) and calculate \(J^{*}\).
    22: Output \(\left(\theta^{*}, \lambda^{*}, \gamma^{*}\right)\) and \(J^{*}\).
```


# 5. Numerical results 

In this Section, a continuous fermentation under anaerobic conditions at $37^{\circ} \mathrm{C}$ with initial state $\mathbf{x}^{0}=(0.1 \mathrm{~g} / \mathrm{L}, 400 \mathrm{mmol} / \mathrm{L}, 0,0,0,0,0,0)^{T}$ is considered. The total fermentation time $t_{f}$, initial glycerol concentration $C_{0}$ and the minimum dwell time are set to be $80 \mathrm{~h}, 675 \mathrm{mmol} / \mathrm{L}$ and 0.15 h , respectively. We consider seven candidate operable modes: $d^{1}=0.05, d^{2}=0.1, d^{3}=0.15, d^{4}=0.2, d^{5}=0.25, d^{6}=0.3, d^{7}=0.35$, which are determined by taking different values for the control function $D(t)$ in a reasonable range of $[0.05,0.35]$ according to the experiment operations in [2]. The lower bound $\mu_{\mathrm{s}}$ and upper bound $\mu^{*}$ of first moment of the uncertainty intracellular parameters are set to be $0.9 \cdot$ $\mathbf{p}^{0}$ and $1.1 \cdot \mathbf{p}^{0}$, respectively, where $\mathbf{p}^{0}$ is the nominal value of $\mathbf{p}$ listed in Table 1. To avoid inhibition of cell growth by excessive substrate, the continuous fermentation of glycerol discussed in this paper begins with batch fermentation where there is no substance is poured into or out of the bio-reactor. The batch fermentation process lasts for 4 h in this work. In the proposed TSEDA, we set $N_{s i z p}=120, K=40$, $m_{0}=60, m_{K}=5$ and $s_{1}=50$. The fourth-order Runge Kutta method is used to solve the control system equations. All the computations and simulations are performed in Matlab R2020b under 6 cores R5 computational environment with 3.30 GHz CPU.

By TSEDA, the approximate optimal solution of problem (P5) can be obtained, then the approximate optimal switching sequence and optimal switches times corresponding to the approximate optimal robust control $D^{*}(t)$ of problem (P1) can be constructed (Table 3 in the Appendix). The trajectory of the corresponding approximate optimal robust control $D^{*}$ is drawn in Fig. 3(a), and (b) shows the concentrations of biomass, glycerol and 1,3-PD during the fermentation process under $D^{*}$.

To illustrate the feasibility of the obtained approximate optimal control strategy $D^{*}$, we additionally consider a general process control of this fermentation by determining a dilution rate $\bar{D}$ in the discrete set $D_{\text {nd }}$ to improve the mean productivity in (2.6) without considering the
![img-1.jpeg](img-1.jpeg)

Fig. 2. The flowing chart of the proposed TSEDA.
parameter uncertainty, similar to the previous work [9,52]. To differentiate the two control strategies, we call $D^{*}$ and $\bar{D}$ the optimal robust control and the optimal general control, respectively. The optimal general control $\bar{D}$ is drawn in Fig. 4(a). Fig. 4(b) shows the corresponding concentrations of biomass, glycerol and 1,3-PD during the fermentation process under $\bar{D}$. It turns out that the mean productivity of 1,3-PD under $D^{*}$ is 58.0407 , while that under $\bar{D}$ is 63.4365 . When considering the parameter uncertainty, even though the mean productivity will decrease slightly, it can still remain at a high level.

To investigate the advantage of system performance under the optimal robust control $D^{*}$, we perturb the intracellular parameter $\mathbf{p} 25$ times in a small range by generating $\mathbf{p}^{i} \in\left[\mathbf{p}^{0}-0.15 \cdot \mathbf{p}^{0}, \mathbf{p}^{0}+0.15 \cdot \mathbf{p}^{0}\right]$, where $\mathbf{p}^{0}$ is the nominal value of $\mathbf{p}$ listed in Table 1. Fig. 5(a) and

![img-4.jpeg](img-4.jpeg)
(a) The obtained optimal robust control $D^{*}$.
![img-5.jpeg](img-5.jpeg)
(b) The concentration curves under $D^{*}$.

Fig. 3. The obtained optimal robust control $D^{*}$ considering parameter uncertainties and the corresponding concentrations curves under $D^{*}$.
![img-4.jpeg](img-4.jpeg)
(a) The optimal general control $\hat{D}$.
![img-5.jpeg](img-5.jpeg)
(b) The concentration curves under $\hat{D}$.

Fig. 4. The optimal general control $\hat{D}$ without considering parameter uncertainties and the corresponding concentration curves under $\hat{D}$.
(b) show the comparison of the state trajectories of $x_{3}$ (concentration of target product 1,3-PD) by perturbing the intracellular parameter $\mathbf{p}$ 25 times under two different controls $D^{*}$ and $\hat{D}$, respectively. Comparing Fig. 5(a) and (b), it is clear that adopting the obtained optimal robust control $D^{*}$ makes the system state more robust to parameter perturbations. In other words, the system under the optimal robust control $D^{*}$ is far superior to that under the optimal general control $\hat{D}$ in terms of system robustness to parameter uncertainty, which can verify the importance of considering parameter uncertainties in designing control system and the superiority of the obtained control strategy $D^{*}$. The study also suggests the proposed DRDCP is more suited to the bioprocess control design for the real problems with parameter uncertainties.

To investigate the performance of the proposed TSEDA, we compare its mean values (Mean), standard deviations (SD), and running time (Time) with the basic EDA proposed in [46] under 10 independent runs and three different $N_{s t 2 s}$, as listed in Table 2. We can see that the proposed TSEDA obtains a better objective function value and has a smaller standard deviation under 10 independent runs, which indicates that TSEDA has better performance in searching the best solution and better robustness in repeated execution. The excellent performance of the proposed algorithm comes at the cost of increasing computation time, but still within an acceptable range. In fact, considering the complexity of the large-scale problem (P5), which is characterized by high dimensions of variables ( 1023 variables, to be exact), semi-infinite constraint and strong nonlinearity of constraint system, the running times listed in Table 2 of two algorithms are both reasonable and acceptable.

Table 2
The statistical results of the proposed TSEDA and the basic EDA in [46].

| $N_{s t 2 s}$ | Algorithm | Mean | SD | Time (s) |
| :--: | :-- | :-- | :-- | :-- |
| 90 | EDA in [46] | -53.8536 | 0.6871 | 12589.5695 |
|  | TSEDA | -56.2519 | 0.6548 | 14183.2268 |
| 120 | EDA in [46] | -54.3649 | 0.7654 | 20649.5831 |
|  | TSEDA | -57.3833 | 0.4146 | 22312.3840 |
| 150 | EDA in [46] | -55.7819 | 0.6326 | 26179.8945 |
|  | TSEDA | -57.8661 | 0.3441 | 28237.3898 |

To further show the superiority of the proposed TSEDA, we also draw the change curves of the fitness value following the change of iterations of two algorithms under $N_{s t 2 s}=120$ in Fig. 6. It is obvious that both algorithms have good convergence, but the proposed TSEDA can search a better solution than the basic EDA in [46] through similar number of iterations.

## 6. Conclusions

This work provides an approach to designing a control strategy with good robustness to parameter uncertainties for glycerol continuous fermentation through solving a bilevel min-max discrete OCP using a modified two-step EDA algorithm. In view of the widespread existence of this control problem under consideration in real industrial process, and the difficulty to solve a large-scale DRO problem with semiinfinite constraint, this study has important theoretical significance and

![img-6.jpeg](img-6.jpeg)
(a) Trajectories under the robust control $D^{*}$.
![img-7.jpeg](img-7.jpeg)
(b) Trajectories under the general control $\hat{D}$.

Fig. 5. Comparison of the state trajectories of $s_{x}$ (concentration of 1,3-PD) with respect to 25 times perturbations of uncertain parameter $\boldsymbol{\rho}$ under two different control strategies: the obtained optimal robust control $D^{*}$ and the optimal general control $\hat{D}$.
![img-8.jpeg](img-8.jpeg)

Fig. 6. The convergence values of the proposed TSEDA and the basic EDA in [46].
practical application value. Numerical simulations demonstrate that the obtained approximate optimal dilution rate makes the fermentation system maintain a good performance even in the worst case, which can indicate the significance of considering parameter uncertainties in practical process control. Numerical comparisons also show that the modified algorithm is stable and efficient, and has potential to find a better solution for the large-scale DRO problem.

Our current work is carried out through engineering applied angle, and in future, we will further improve and perfect the two-step algorithm for large-scale benchmark DRO problem from the point of algorithm design, such as constructing the ambiguity set under Wasserstein metric. In addition, we are also interested in finding a better way to deal with semi infinite constraints and min-max problem, maybe bilevel optimization is a promising research direction.

## CRediT authorship contribution statement

Juan Wang: Conceptualization, Methodology, Reviewing and editing. Chihua Chen: Data curation, Methodology, Writing - original draft. Feiyan Zhao: Software, Data curation. Jichao Wang: Visualization, Investigation, Software. An Li: Supervision, Formal analysis, Reviewing and editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grant No. 42176011) and the Natural Science Foundation of Shandong Province of China (Grant No. ZR2020MD060).

## Appendix

See Table 3.

Table 3
The obtained approximate optimal switching sequence and switching times of $D^{1}(t)$.
(a) ${ }^{1}, a^{1}, a^{2}, a^{3}, a^{4}, a^{5}, a^{6}, a^{7}, a^{8}, a^{9}, a^{10}, a^{11}, a^{12}, a^{13}, a^{14}, a^{15}, a^{16}, a^{17}, a^{18}, a^{19}, a^{20}$,
$a^{2}, a^{2}, a^{3}, a^{4}, a^{5}, a^{6}, a^{7}, a^{8}, a^{9}, a^{10}, a^{11}, a^{12}, a^{13}, a^{14}, a^{15}, a^{16}, a^{17}, a^{18}$,
$a^{2}, a^{2}, a^{3}, a^{4}, a^{5}, a^{6}, a^{7}, a^{8}, a^{9}, a^{10}, a^{11}, a^{12}, a^{13}, a^{14}, a^{15}, a^{16}, a^{17}, a^{18}$,
$a^{2}, a^{2}, a^{3}, a^{4}, a^{5}, a^{6}, a^{7}, a^{8}, a^{9}, a^{10}, a^{11}, a^{12}$,
$(4.0000,4.6882,5.7892,6.6564,7.0400,7.6355,8.5600,9.5610,10.0800,11.3347$, $11.6000,12.0927,12.5553,12.8706,13.1200,13.9528,14.6400,15.1928,16.8959$, $17.6800,18.0132,18.2687,18.6898,19.2000,19.8619,20.7200,21.1584,22.2400$, $22.7400,23.7600,24.0527,24.6613,25.2800,26.2671,26.8000,27.3918,28.3200$, $29.1254,29.3283,29.8400,30.0756,30.3658,31.3600,32.4541,32.8800,34.4000$, $34.7418,35.1129,35.9200,37.1083,37.4400,37.7791,38.3149,38.7133,38.9600$, $39.6533,40.4800,40.7852,41.1794,41.5906,42.0000,42.9045,43.5200,44.4187$, $45.0400,45.5412,46.5600,47.0623,48.0800,48.8115,49.3143,49.6000,49.9541$, $51.1200,51.3792,52.6400,53.2853,53.5035,54.1600,54.7127,55.6800,56.8510$, $57.2000,57.7767,58.7200,59.4446,61.2486,61.7600,62.7026,63.2800,64.2990$, $64.8000,65.1981,65.6404,66.3200,67.3203,67.8400,68.2901,69.3600,70.4141$, $70.6243,70.8800,71.3989,72.4000,73.3535,73.9200,74.2728,74.5119,75.4400$, $76.0509,76.9600,77.5285,78.4800$ ).

## References

[1] M. Mccoy, Chemical makers try biotech paths, Chem. Eng. News 76 (1998) $13-19$
[2] K. Menzel, A.P. Zeng, W.D. Deckwer, High concentration and productivity of 1,3 propanediol from continuous fermentation of glycerol by Klebsiella pneumoniae, Enzyme Microb. Technol. 20 (1997) 82-86.
[3] A.P. Zeng, W.D. Deckwer, A kinetic model for substrate and energy consumption of microbial growth under substrate-sufficient conditions, Biotechnol. Prog. 11 (1995) 71-79.
[4] Y.Q. Sun, W.T. Qi, H. Teng, et al., Mathematical modeling of glycerol fermentation by Klebsiella pneumoniae: Concerning enzyme-catalytic reductive pathway and transport of glycerol and 1,3-propanediol across cell membrane, Biochem. Eng. J. 38 (2008) 22-32.
[5] J.G. Zhai, J.X. Ye, L. Wang, et al., Pathway identification using parallel optimization for a complex metabolic system in microbial continuous culture, Nonlinear Anal. RWA 12 (5) (2011) 2730-2741.
[6] J.L. Yuan, C.Z. Wu, J.X. Ye, et al., Robust identification of nonlinear statedependent impulsive switched system with switching duration constraints, Nonlinear Anal. Hybrid Syst. 36 (2020) 100879.
[7] H. Wang, N. Zhang, T. Qiu, et al., Optimization of a continuous fermentation process producing 1,3 -propanediol with hopf singularity and unstable operating points as constraints, Chem. Eng. Sci. 116 (2014) 668-681.
[8] H.Z. Wang, N. Zhang, T. Qiu, et al., Optimization of a continuous fermentation process producing 1,3 -propanediol with hopf singularity and unstable operating points as constraints, Chem. Eng. Sci. 116 (2014) 668-681.
[9] J. Wang, C.H. Chen, J.X. Ye, Multi-objective optimal control of bioconversion process considering system sensitivity and control variation, J. Process Control 119 (2022) 13-24.
[10] B. Ban, H.C. Yin, E.M. Feng, Computation of impulsive optimal control for 1,3-PD fed-batch culture, J. Process Control 34 (2015) 49-55.
[11] L. Wang, Q. Lin, R. Loxton, et al., Optimal 1, 3-propanediol production: Exploring the trade-off between process yield and feeding rate variation, J. Process Control 32 (2015) 1-9.
[12] S. Sattayasamitsathit, P. Methacanon, P. Prasertsan, Enhance 1, 3-propanediol production from crude glycerol in batch and fed-batch fermentation with two-phase pH-controlled strategy, Electron. J. Biotechnol. 14 (6) (2011) 4.
[13] R. Boenigk, S. Bowien, G. Gottschalk, Fermentation of glycerol to 1, 3propanediol in continuous cultures of citrobacter freundii, Appl. Microbiol. Biotechnol. 38 (1993) 453-457.
[14] X.H. Li, E.M. Feng, Z.L. Xiu, Stability and optimal control of microorganisms in continuous culture, J. Appl. Math. Comput. 22 (2006) 425-434.
[15] K. Cheng, Y. Sun, W. Liu, et al., Effect of feeding strategy on 1, 3-propanediol fermentation with Klebsiella pneumoniae, Food Ferment. Ind. (2004) 1-5.
[16] D.T. Pan, S.D. Wang, J.B. Wang, et al., Optimization and feedback control system of dilution rate for 1,3 -propanediol in two-stage fermentation: A theoretical study, Biotechnol. Prog. 38 (1) (2022) e3225.
[17] H.H. Bei, L. Wang, J. Sun, et al., A multistage feedback control strategy for producing 1,3 -propanediol in microbial continuous fermentation, Complexity 2019 (2019).
[18] R. Loxton, K.L. Teo, V. Rehbock, Robust suboptimal control of nonlinear systems, Appl. Math. Comput. 217 (14) (2011) 6566-6576.
[19] G.M. Cheng, L. Wang, B. Loxton, et al., Robust optimal control of a microbial batch culture process, J. Optim. Theory Appl. 167 (1) (2015) 342-362.
[20] C.Y. Liu, Z.H. Gong, H. Lee, et al., Robust bi-objective optimal control of 1 , 3-propanediol microbial batch production process, J. Process Control 78 (2019) $170-182$.
[21] H.G. Beyer, B. Sendhoff, Robust optimization - A comprehensive survey, Comput. Methods Appl. Mech. Engrg. 196 (33-34) (2007) 3190-3218.
[22] C. He, L. Wu, T.Q. Liu, et al., Robust co-optimization scheduling of electricity and natural gas systems via AIMM, IEEE Trans. Sustain. Energy 8 (2) (2017) $658-670$.
[23] P.K. Kumawat, N.D. Chaturvedi, Robust resource targeting in continuous and batch process, Clean Technol. Environ. Policy 24 (2022) 273-288.
[24] Z.Q. Chang, J.Y. Ding, S.J. Song, Distributionally robust scheduling on parallel machines under moment uncertainty, European J. Oper. Res. 000 (2018) 1-15.
[25] H. Rahimian, S. Mehrotra, Distributionally robust optimization: A review, 2019, arXiv preprint arXiv:1908.05659.
[26] H. Scarf, K. Arrow, S. Karlin, A min-max solution of an inventory problem, Stud. Math. Theory Inventory Prod. 10 (1958) 201-209.
[27] J. Goh, M. Sim, Distributionally robust optimization and its tractable approximations, Oper. Res. 58 (2010) 902-917.
[28] Y.W. Wang, Y.J. Yang, L. Tang, et al., A Wasserstein based two-stage distributionally robust optimization model for optimal operation of CCHP micro-grid under uncertainties, Electr. Power Energy Syst. 119 (2020) 105941.
[29] X. Yu, S.Q. Shen, Multistage distributionally robust mixed-integer programming with decision-dependent moment-based ambiguity sets, Math. Program. 196 (2022) 1025-1064.
[30] Q. Liu, J. Wu, X.T. Xiao, et al., A note on distributionally robust optimization under moment uncertainty, J. Numer. Math. 26 (2018) 141-150.
[31] S. Zymler, D. Kuhn, B. Rustem, Distributionally robust joint chance constraints with second-order moment information, Math. Program. 137 (2013) 167-198.
[32] P.M. Esfahani, D. Kuhn, Data-driven distributionally robust optimization using the Wasserstein metric: performance guarantees and tractable reformulations, Math. Program. 171 (2018) 115-166.
[33] W.J. Xie, On distributionally robust chance constrained programs with Wasserstein distance, Math. Program. 186 (2021) 115-155.
[34] E. Delage, Y.Y. Ye, Distributionally robust optimization under moment uncertainty with application to data-driven problems, Oper. Res. 58 (2010) $595-612$.
[35] Z.H. Gong, C.Y. Liu, K.L. Teo, et al., Distributionally robust parameter identification of a time-delay dynamical system with stochastic measurements, Appl. Math. Model. 69 (2019) 685-695.
[36] P.F. Zhao, C.H. Gu, D. Huo, Two-stage distributionally robust optimization for energy hub systems, IEEE Trans. Ind. Inform. 16 (5) (2020) 3460-3469.
[37] J.H. Zhang, Y.C. Li, G.D. Yu, Emergency relief network design under ambiguous demands: A distributionally robust optimization approach, Expert Syst. Appl. 208 (2022) 118139.
[38] H. Rahimian, G. Bayraksan, T. Homem-de Mello, Identifying effective scenarios in distributionally robust stochastic programs with total variation distance, Math. Program. 173 (2019) 393-430.
[39] F. Luo, S. Mehrotra, Decomposition algorithm for distributionally robust optimization using Wasserstein metric with an application to a class of regression models, European J. Oper. Res. 278 (2019) 20-35.
[40] F.M. Lin, X.L. Fang, Z.M. Gao, Distributionally robust optimization: A review on theory and applications, Control Optim. 12 (1) (2022) 159-212.
[41] M. Ringkamp, S. Ober-Blibaum, S. Leyendecker, On the time transformation of mixed integer optimal control problems using a consistent fixed integer control function, Math. Program. 161 (2017) 551-581.
[42] J. Wang, J.X. Ye, E.M. Feng, et al., Complex metabolic network of glycerol fermentation by Klebsiella pneumoniae and its system identification via biological robustness, Nonlinear Anal. Hybrid Syst. 5 (2011) 102-112.
[43] F. Barbirsto, J.P. Grivet, P. Soucaille, et al., 3-hydroxypropanaldehyde, an inhibitory metabolite of glycerol fermentation to 1,3 -propanediol by enterobacterial species, Appl. Environ. Microbiol. 62 (1996) 1448-1451.
[44] Z.L. Xiu, A.P. Zeng, L.J. An, Mathematical modeling of kinetics and research on multiplicity of glycerol bioconversion to 1,3 -propanediol, J. Dalian Univ. Technol. 40 (2000) 420-433.
[45] S. Sager, Numerical Methods for Mixed-Integer Optimal Control Problems, University Heidelberg, 2005.
[46] H. Mühlenbein, G. Paans, From recombination of genes to the estimation of distributions i. binary parameters, in: International Conference on Parallel Problem Solving from Nature, Springer, 1996, pp. 176-187.
[47] P. Larradaga, J.A. Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation, Vol. 2, Springer Science \& Business Media, 2001.
[48] M. Hauschild, M. Pelikan, A Survey of Estimation of Distribution Algorithms, MEDAI, Report 2011004, 2011.
[49] Z.S. Shao, D.C. Pi, W.S. Shao, Estimation of distribution algorithm with path relinking for the blocking flow-shop scheduling problem, Eng. Optim. 50 (5) (2018) 894-916.
[50] X.X. Duan, MCEDA: A novel many-objective optimization approach based on model and clustering, Appl. Soft Comput. 74 (2019) 274-290.
[51] S.J. Gao, C.W. Silva, Estimation distribution algorithms on constrained optimization problems, Appl. Math. Comput. 339 (2018) 323-345.
[52] J.C. Wang, X. Zhang, J.X. Ye, et al., Optimizing design for continuous conversion of glycerol to 1,3 -propanediol using discrete-valued optimal control, J. Process Control 104 (2021) 126-134.