# EDA-based optimized global control for PV inverters in distribution grids 

David Cañadillas ${ }^{1} \mid$ Hamed Valizadeh ${ }^{3} \mid$ Jan Kleissl ${ }^{3} \mid$ Benjamin González-Díaz ${ }^{2}$<br>Ricardo Guerrero-Lemus ${ }^{1}$

${ }^{1}$ Departamento de Física, Universidad de La Laguna, Avenida Astrofísico Francisco Sánchez, S/C de Tenerife, Spain<br>${ }^{2}$ Departamento de Ingeniería Industrial, Universidad de La Laguna, Avenida Astrofísico Francisco Sánchez, S/C de Tenerife, Spain<br>${ }^{3}$ Center for Energy Research, Department of Mechanical and Aerospace Engineering, University of California, San Diego, La Jolla, California, USA<br>Correspondence<br>David Cañadillas, Departamento de Física. Universidad de La Laguna. Avenida Astrofísico Francisco Sánchez, S/N, 38206, S/C de Tenerife, Spain. Email: deanadif@ufl.edu.es


#### Abstract

Operating distribution grids is increasingly challenging due to the increasing penetration of photovoltaic systems. To address these challenges, modern photovoltaic inverters include features for local control, which sometimes lead to suboptimal results. Improved communication infrastructure and photovoltaic inverters favour global control strategies, which receive information from all the systems in the grid. An estimation of distribution algorithm is used to optimize a global control strategy that minimizes active power curtailment and use of reactive power of the photovoltaic inverters, while maintaining voltage stability. Optimized global control outperforms every other local control evaluated in terms of apparent energy used for control ( $9.9 \%$ less usage compared to the second best alternative in all scenarios studied) and ranks second in terms of voltage stability (with a $0.14 \%$ of total time outside the voltage limits). Two new indicators to compare control strategies are proposed, and optimized global control strategy ranks best for both efficiency index (0.98) and average apparent power use $(0.48 \mathrm{kVA})$.


## 1 | INTRODUCTION

Photovoltaic (PV) systems connected to medium-voltage and low-voltage distribution grids pose several engineering challenges to distribution system operators (DSO) who ensure the quality of the electric supply. The most common problems are overvoltage at the end of the feeders and overloading of transformers or lines due to active power injection. Traditionally, these problems have been addressed by reinforcing the grid [1], which is a rather expensive solution.

Another effect of including distributed generation (DG) on distribution grids is a change in the traditional operational paradigm of power systems. The electric system has traditionally been operated in a radial way [2], where large generators supply the power to the loads in an unidirectional manner. With a large number of DG, power flow can be bidirectional and come from the demand-side depending on the load conditions. Active power injection in an electric grid increases the voltage especially in low and medium voltage distribution grids, due to their low $\mathrm{X} / \mathrm{R}$ ratio (the lines are more "resistive", meaning that
active power injections/absorptions has a larger effect on the voltage).

When the DG are PV systems, the variability of the solar resource caused by passing clouds becomes an important issue. Short-term solar forecasting has been identified as a key strategy for integration of PV systems in the grid, but high accuracy solar forecasts remain elusive. However, results may be difficult to obtain unless dedicated equipment such as sky-imagers are used [3]. The randomness of especially household loads is another source of uncertainty. The mismatch between high PV production and high demand periods exacerbates the issues in distribution grids [4].

Conventional voltage regulation elements on the distribution grid consist of on-load tap changers (OLTC) in the transformers and voltage regulators along the lines. All the above-mentioned issues make it difficult to find a fixed set of operational conditions that ensure the quality and stability of the electric supply. Without DG, these problems have been easily addressed using approaches such as transformer tap changes or voltage regulators in the middle of the distribution grids. However, the

[^0]
[^0]:    This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.
    (C) 2020 The Authors. IET Rewivable Power Generation published by John Wiley \& Sons Ltd on behalf of The Institution of Engineering and Technology

complexity resulting from adding DG at the distribution level requires different solutions.

Nowadays, solar inverters are capable of delivering PV power with a variable power factor (PF), which allows them to perform voltage control depending on different variables, such as voltage or power. The most common local control strategies supported by commercial PV inverters are reactive power compensation (operation with flexible PF) and curtailment of active power [1]. Increasingly countries are adopting new grid codes which require PV system inverters to participate in the regulation of the distribution grid [5]. It may be conceivable that solar inverters become the main source of voltage regulation in distribution grids.

Although, under some circumstances adequate voltage regulation can only be achieved by curtailing the active power injected to the grid, one of the objectives should be to curtail the least amount of clean energy. For that reason, reactive power compensation is a preferred strategy.

Voltage regulation through reactive power control is based on the reactance of the line, ignoring its resistance [6]. Hence, the effectiveness of reactive power compensation is determined by the $\mathrm{X} / \mathrm{R}$ ratio of the lines which differs depending on the voltage level of the grid, increasing as the voltage increases [7]. For that reason, it is expected that reactive power capabilities are less effective in low voltage circuits, since their lines are more resistive (lower X/R ratio) than in MV and HV networks.

The position of each PV system in the feeder is a critical factor in the behaviour of local controllers [8]. For instance, inverters located near the transformer are less likely to suffer from voltage problems, while those at the end of the line are more exposed to voltage problems. This fact may result in uneven and unequitable use of the solar inverters depending on their position on the feeder. A solution to uneven use includes different configurations for the local controllers (different set points on the curve) depending on the distance of the PV system to the substation [9].

Distribution systems are unbalanced systems. Although the DSO evenly distributes the capacity on each phase, shifts in the timing of loads by individual households can lead to imbalance especially as the size of the distribution grid diminishes. In unbalanced three-phase four-wire systems the power injections in one of the phases effects the other two, which is caused by neutral point shifting [10].

Due to the factors listed above typical local inverter control strategies can lead to solutions far from the optimum. Reactive power usage and active power curtailment may be managed suboptimally and control actions may be distributed suboptimally among the systems. Centralized control is expected to improve the control actions since the cost function takes into account all variables.

The evolution of the communication infrastructures and capabilities of PV systems promotes the introduction of global optimization methods. Global optimization methods can retrieve information from every system on the grid and analyze them and their operational conditions in real time to find optimal operating points for all the systems to maintain power quality [11]. The critical enabler of global optimized controls is
the increased communication of the devices in the power grid [12].

EC is a family of heuristics inspired by nature that tries to emulate natural selection, through the generation of a population of candidate solutions, which are evaluated with an objective function (also referred to as cost or fitness function). The best individuals are then selected to reproduce, "spreading their genes" or properties to the next generations of candidate solutions.

However, as the number of PV system increases, so does the number of variables to be tracked and optimized, along with the complexity of the task of monitoring and control. Therefore, fast optimization algorithms are needed to find near optimal solutions in a reduced timeframe. There are multiple families of algorithms and heuristics, such as evolutionary computing (EC), that have started to emerge as useful tools to confront the computational problems derived from high complexity tasks.

Inside the EC family, there is a large set of algorithms and heuristics, and some are well known and commonly implemented in optimization problems in power systems [13-17]. One interesting family of algorithms that has not been widely applied to power systems is an estimation of distribution algorithms (EDAs) [18]. Unlike other EC algorithms, EDAs build a probabilistic model from the best individuals and sample the subsequent generations from it, instead of randomly generating mutations in the genes of the individuals, crossover, or reproducing them with some other arbitrary criteria. By using a probabilistic model, the search space of the algorithm narrows at each iteration, approaching the region with optimal solutions. The EDA will converge faster to the near-optimal solutions than other EC algorithms.

Several references in the literature evaluate the EDA performance against other algorithms, mainly genetic algorithms (GA) due to its similarities. In [19], EDA performance is contrasted with other metaheuristics in an electric vehicle charging problem. In that study, EDA performs best in terms of computational time and quality of the solution. In [20], a node allocation problem in a network is solved using GA and EDA. Again, EDA outperforms GA with these settings, especially as the population grows. Finally, in [21], an in-depth analysis of different metaheuristics is made for a series of NK landscapes. In this study, different strategies for EDA implementation are analyzed. UMDA and an advanced EDA (hierarchical Bayesian optimization algorithm, hBOA) are contrasted with GA. EDAs strategies prove to be better in terms of the number of evaluations.

EDAs have been used in various applications: as an optimizer for a controller for networked dc motor systems [22], systemlevel synthesis for chip designs [23], carbon emissions reduction and project makespan minimization [24], dynamic deployment of near space communication systems [25], energy-efficient scheduling of cloud computing services [26], or calibrating the parameters for microscopic traffic models [27]. To the best knowledge of the authors, there is only one paper on DG, where an EDA is used to intelligently charge electric vehicles [19] and there are no studies on distribution system optimization with PV using EDAs. EDAs are well suited for distribution system optimization as they can solve large-scale, complex, non-linear

![img-0.jpeg](img-0.jpeg)

FIGURE 1 Operational regions for the inverter depending on the type of control selected. $\mathrm{P}_{\mathrm{PV}}$ is the active power from the PV panels. (a) Fixed PF function, (b) VV function, (c) VW function and (d) Combined VV and VW
optimization problems and are immune to local minima. They converge faster to near-optimal solutions and their computational costs are lower compared to other EC alternatives [19].

In this paper, we implement an EDA-based optimization to obtain near-optimal solutions to the set of operational parameters of all PV inverters in a medium-voltage distribution grid to evaluate if they are capable of maintaining the voltage stability and the power quality by themselves. There are two main contributions of this paper. The first contribution is the implementation of an EDA-based optimization global control which optimizes the parameters (active power curtailment and reactive power support) of all the PV systems in a modified IEEE123 medium-voltage distribution grid. This kind of control could be easily deployed in actual grids with the technology currently available in commercial PV inverters. Second, to the authors' knowledge, for the first time, the viability of using solar inverters as the only voltage regulators in the distribution grid is examined.

## 2 | STANDARD LOCAL CONTROLS OF PV INVERTERS

Although smart inverters can provide a variety of additional functionalities for grid stability or responses to fault events [28], we will focus on voltage support. There are a variety of standard local control strategies that modern smart inverters have implemented. We compare our proposed EDA-based optimized global control (OptGC) to four of these local control methods: the fixed PF function, the Volt-var (VV) function, the Volt-Watt (VW) function, and a combination of VV and VW (VV+VW). The operational regions on the QP diagram for each of the local controls studied are depicted in Figure 1 and described further below.

### 2.1 | Fixed power factor

Modern PV inverters can operate at PFs different than the unity. Fixed PF control can be used to limit the injections of active power while providing a reactive power absorption or injection throughout the day. Reactive power output increases proportionally to the PF, as the PV active power increases [29]. Fixed PF control is usually suboptimal since it implies a continuous curtailment of active power and inefficient use of reactive power
irrespective of grid conditions, but it is easy to implement and its effects can be easily observed.

### 2.2 | Volt-var function

The VV function is a local controller that reacts to voltage measurements at the point of common coupling of the solar inverter with the feeder [9]. There are several VV configurations: different set points and slopes for the curves, the existence, or lack thereof, of a "deadband", the possibility of including hysteresis, etc. In this study, two different curves for VV control with and without deadband are used, which are shown in Figure 2. Without a deadband (top-left), reactive power compensation starts as soon as the voltage magnitude differs from unity. When the deadband is included, (top-right), the control does not absorb nor inject reactive power until the voltage approaches the set limits (in this case, at 0.97 p.u. and 1.03 p.u.), which in turn, should reduce reactive power usage.

### 2.3 | Volt-Watt function

The VW function is used to reduce the amount of active power delivered to the system (power curtailment) as a function of the voltage at the PCC of the solar inverter. An operation curve defining the voltage set point where the control should start to act is configured in the inverter [29]. The VW curve used for this study is shown in Figure 2 (bottom). VW is only useful in overvoltage conditions (that is, it does not respond to undervoltage situations) since it does not make use of reactive power.

### 2.4 | Simultaneous volt-var and volt-Watt function

Another strategy for local control is the combination of both VV+VW controls. As in the only VW control, this strategy is only useful when experiencing overvoltage situations, otherwise, it would behave as an only VV function. A priority of which function dominates over the other has to be defined [29]. If VW has priority, the inverter will first curtail active power before using reactive power compensation. If VV has priority, the inverter will first dispatch reactive power, and if the further reduction of voltage is required, active power will be curtailed. In general, the objective should be to curtail as little active power as possible. For that reason, in our simulations, the VV function has priority. That means that active power may be curtailed only if reactive power utilization it at its limit, allowing a larger share of the inverters apparent power to be used for reactive power compensation.

## 3 | OPTIMIZATION PROBLEM FORMULATION

The objective of the optimization problem is to find a set of near-optimal points of operation for each PV inverter in a distribution grid that maintains voltage within the limits, while minimizing the curtailment of active power and the use of reactive

![img-2.jpeg](img-2.jpeg)

FIGURE 2 Local control function curves. Top-left: VV curve without dead band. Top-right: VV curve with dead band (VVwD). Bottom: VW curve
![img-2.jpeg](img-2.jpeg)

FIGURE 3 Example of the control curves output by the optimization algorithm and used by OptGC. These are the splines for one PV system resulting from one optimization step of the algorithm. The top and bottom figure shows results for a run with maximum and minimum load conditions, respectively. Positive values of reactive power correspond to inductive power and negative values are capacitive power
power. The optimization outputs are computed every 15 minutes and consist of the functions of optimal active power and reactive power output versus PV active power output capability (based on dc power output from solar irradiance) for every PV system and for 11 PV active power output levels from $0 \%$ to $100 \%$ (Figure 3). The optimization explores a linear space (or spline) [10] discretized in equal steps (in this case, 11 points
from $0 \%$ to $100 \%$ PV power output, both included). Each point of the spline is called knot. It has to be mentioned that, although the optimization is run for a discretized linear space, the control algorithm uses the whole spline to find the actual values i.e. it interpolates the values between the knots. This behaviour is better explained in Section 5.

The optimization ensures that all knots satisfy the constraints of the optimization problem. The constraints of the problem are handled via large penalty functions. Otherwise, every individual must be individually evaluated for constraint compliance before being included in the model, which will lead to additional computational costs for finding individuals that satisfy the constraints. The use of penalty functions means that if a constraint is not satisfied, a large penalty value is added to the objective function to rank the solution as suboptimal by the optimization algorithm. To drive the optimization algorithm to regions of the solution space closer to the true optima, the penalty for the constraint violation is obtained using distance functions. These distance functions are defined for each constraint and measure how far each solution is from the optimal region as explained further below.

The first constraint states that, for each PV inverter $p$, the total complex power output cannot exceed the rated apparent power $\left|N_{p}^{p}\right|$ of the PV inverter at each knot $k$ :

$$
\left(P_{p, k}^{\mathrm{PV}}-P_{p, k}^{\mathrm{corr}}\right)^{2}+\left(\varrho_{p, k}^{\mathrm{PV}}\right)^{2} \leq\left(\left|N_{p}^{p}\right|\right)^{2}
$$

where $P_{p, k}^{\mathrm{PV}}$ is the actual PV active power produced by the PV system; $P_{p, k}^{\text {corr }}$ is the curtailed active power; $\varrho_{p, k}^{\mathrm{PV}}$ is the reactive power absorption/injection.

Let $c_{p, k}^{1}$ be a distance function to the feasible region for each PV system $p$ at each power output level $k$. The distance function for this constraint is a summation of all the $c_{p, k}^{1}$ multiplied by a

penalty value, $p_{v}$, large enough to dominate over the rest of the elements of the objective function if the constraint is violated. If the constraint is satisfied by a particular knot, the distance value of that knot is removed from the scaled distance function $d_{V} \sigma(\tilde{x})$ using the max operator

$$
\begin{gathered}
c_{p, k}^{\tilde{x}}=\left(P_{p, k}^{\mathrm{PV}}-P_{p, k}^{e}\right)^{2}+\left(Q_{p, k}^{\mathrm{PV}}\right)^{2}-\left(\left|I_{p}^{\tilde{x}}\right|\right)^{2} \\
d_{V} \tilde{\tilde{x}}(\tilde{x})=p_{v} \cdot \sum_{p}^{\tilde{x}, \tilde{x}} \sum_{k}^{\tilde{x}, \tilde{x}} \max \left\{c_{p, k}^{\tilde{x}}, 0\right\}
\end{gathered}
$$

where $\tilde{x}$ is a vector representing one individual or solution generated by the EDA.

Another obvious constraint is that the curtailed active power of the PV system $p$ at each power output $k$ cannot exceed the actual produced PV power at the same $p$ and $k$

$$
P_{p, k}^{\mathrm{cur} 1} \leq P_{p, k}^{\mathrm{PV}}
$$

Again, the distance function is a summation of the linear function multiplied by a large penalty value

$$
d_{p \text { curt }}(\tilde{x})=p_{v} \cdot \sum_{k}^{\tilde{x}, \tilde{x}} \max \left\{\left(P_{p, k}^{\text {cur }}-P_{p, k}^{\mathrm{PV}}\right), 0\right\}
$$

The most important constraints (and the most difficult to satisfy) involve voltage limits. The voltage magnitude $\left|V_{h, k}\right|$ of each node $n$ of the circuit at every power output level $k$ has to remain within the normative limits $\left|V^{\min }\right|$ and $\left|V^{\max }\right|$ at all times. In this study, the voltage limits defined in the ANSI C84.1 norm $\left(\left|V^{\min }\right|=0.95\right.$ p.u. and $\left|V^{\max }\right|=1.05$ p.u.) are used

$$
\left|V^{\min }\right| \leq\left|V_{h, k}\right| \leq\left|V^{\max }\right|
$$

To evaluate the voltages that each solution generates, a power flow should be run. However, running $11 \times 1000$ (the number of candidate solutions generated by the EDA times the number of knots in the spline) power flows for each generation of the optimization routine would be computationally infeasible. Instead, a linearization of the power flow is used to estimate the voltage magnitude at every node, consistent with $[10,30,31]$

$$
\begin{aligned}
\left|V_{h, k}^{\prime}(\tilde{x})\right|= & \left|V_{i}^{\text {base }}\right|+\sum_{n=1}^{\tilde{x}_{n, \max }}\left(c_{v, n}^{p} \cdot\left(P_{p, k}^{\mathrm{PV}}-P_{p, k}^{\mathrm{cur}}\right)\right. \\
& \left.+c_{v, n}^{\tilde{x}}\left(Q_{p, k}^{\mathrm{PV}}\right)\right)
\end{aligned}
$$

In this formula, $\left|V_{h, k}^{\prime}(\tilde{x})\right|$ is the voltage magnitude in node $i$ at knot $k$ for the solution $\tilde{x} .\left|V_{i}^{\text {base }}\right|$ is the voltage magnitude of node $i$ excluding the effect of PV systems, and $c_{v, n}^{p}$ and $c_{v, n}^{x}$ are respectively the sensitivity of voltage magnitude at node $i$ to active and reactive power injections/absorptions at node $n$. Sensitivity matrices are obtained using the perturbation-observation
![img-3.jpeg](img-3.jpeg)

FIGURE 4 Histogram showing the distribution of voltage differences between the linearized power flow and the iterative Newton-Raphson method power flow returned by OpenDSS
method, by making a small change in network state and measuring the effect of that change [32].

A comparison between the linear power flow and the traditional iterative Newton-Raphson method shows that the linearization errors are small (Figure 4). Most of the voltages from the linearized power flow are within $10^{-4}$ p.u. compared to the power flow performed with the iterative method. All errors are less than $2 \times 10^{-3} \mathrm{p} . \mathrm{u}$.

The distance functions for the voltage constraints are the following slightly modified linear functions:

$$
\begin{aligned}
c_{k}^{V^{\prime} \min } & =V^{\prime \min }-\min \left(\left|\overline{V_{k}^{\prime}(x)}\right|\right) \\
d_{V^{\prime} \min }(\tilde{x}) & =p_{v} \cdot \sum_{k}^{\tilde{x}_{\min }} \max \left\{\left(c_{k}^{V^{\prime} \min }\right), 0\right\} \\
c_{k}^{V^{\prime} \max } & =\max \left(\left|\overline{V_{k}^{\prime}(x)}\right|\right)-V^{\prime \max } \\
d_{V^{\prime} \max }(\tilde{x}) & =p_{v} \cdot \sum_{k}^{\tilde{x}_{\max }} \max \left\{\left(c_{k}^{V^{\prime} \max }\right), 0\right\}
\end{aligned}
$$

The objective problem is finally given by

$$
\begin{aligned}
& \min _{\left(Q_{p, k}^{\mathrm{PV}}, P_{p, k}^{\mathrm{cur}}\right)} \sum_{k=1}^{\tilde{x}_{n, \max }}\left(w\left(Q_{p, k}^{\mathrm{PV}}\right)^{2}+(1-w) P_{p, k}^{\mathrm{cur}}\right) \\
& \text { s.t. }\left(P_{p, k}^{\mathrm{PV}}-P_{p, k}^{\mathrm{cur}}\right)^{2}+\left(Q_{p, k}^{\mathrm{PV}}\right)^{2} \leq\left(\left|I_{p}^{\text {Rated }}\right|\right)^{2} \\
& P_{p, k}^{\mathrm{cur}} \leq P_{p, k}^{\mathrm{PV}} \\
& \left|V^{\min }\right| \leq\left|V_{h, k}\right| \leq\left|V^{\max }\right|
\end{aligned}
$$

where $w$ is a weighting factor which has been set to 0.01 to favour the use of reactive power over active power curtailment.

The dimensionality of the problem increases with the number of nodes in the circuit ( $n_{\text {nodes }}$ ), the number of PV systems $\left(n_{\mathrm{PV}_{i}}\right)$ and the number of knots $\left(n_{\text {knots }}\right)$. All individuals in the population have $\left(2 \times n_{\text {knots }} \times n_{\mathrm{PV}_{i}}\right)$ variables, where the 2 comes from active and reactive power.

## 4 | ESTIMATION OF DISTRIBUTION ALGORITHM IMPLEMENTATION

Unlike other EC algorithms, EDA relies on the construction of a probabilistic model with the best individuals from the current generation to sample the population of the next generation. This is based on the reasonable assumption that good solutions for a determined problem should have a similar structure [19]. The general pseudo-code of an EDA is shown in Algorithm 1.

## Algorithm 1. General EDA pseudo-code

1 $\quad \boldsymbol{P}_{0} \leftarrow$ Generate a random initial population $P_{0}$, of $\lambda$ individuals $\bar{x}=\left(x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right)$, where $x$ is the number of variables. For $g=1,2,3 \ldots$ in number of generations:
$2 \quad P_{g-1}^{I x} \leftarrow$ Evaluate population and sort them according to their fitness value and select $S e$ best individuals
$3 \quad \boldsymbol{P}_{g}(x)=\boldsymbol{p}(\boldsymbol{x} \boldsymbol{P}_{g-1}^{I x}) \leftarrow$ Build the probabilistic model: estimate the probability distribution of an individual being among the selected individuals
$4 \quad \boldsymbol{P}_{g} \leftarrow$ Sample a new population from $p_{g}(x)$

EDAs are assumption-free approximators, allowing them to be directly implemented in a wide variety of problems without the complex tuning. EDAs provide flexibility in constructing the statistical distributions, which can be tuned to fit a specific problem. Unlike many other EC algorithms, EDAs have very few parameters that need to be adjusted, although the complexity of the model will always depend on the complexity of the problem being solved.

EDAs can be classified according to the relationships and interdependencies between their input variables. EDAs can have either independent variables or variables with multivariate dependencies [18]. It is reasonable to assume that in our optimization problem, the variables may have multivariate dependencies, since power injections or absorptions in one phase have an effect on the other phases. However, variables corresponding to different knots should be independent. It is worth mentioning that the probabilistic model is only used for searching the solutions of the optimization problem. The grid is modelled in a deterministic manner, where the load, the irradiance curves for the PV systems and the structure of the grid are predetermined. The only variables allowed to vary are those defined for the optimization problem: the active power curtailed and the reactive power injection/absorption of each PV system.

To determine whether univariate or multivariate algorithms are more suitable for the proposed problem, estimation of multivariate normal algorithm ( $\mathrm{EMNA}_{\text {global }}$ ) and univariate marginal distribution algorithm for continuous domains $\left(\mathrm{UMDA}_{c}\right)$ (both from [18]) were compared. An in-depth review and taxonomy showing the advantages and disadvantages of the different EDA strategies are presented in [33]. Generally, $\mathrm{UMDA}_{c}$ ignore feature dependencies and have worse performance for deceptive problems (a class of challenging problems which usually mislead the search to some local optima rather than the global optimum [34]). But on the other side,
they are the fastest among the other EDAs, they are well suited for high dimensionality problems and are easily scalable. When implementing $\mathrm{EMNA}_{\text {global }}$ to our problem, the construction of the covariance matrix was adapted to capture just the relationships between variables belonging to each knot. In other words, 11 different covariance matrices (one for each knot) are constructed. In $\mathrm{UMDA}_{c}$ variables are treated independently, so a different distribution is computed for each variable at each generation.

```
Algorithm 2. UMDA, for the optimization problem
\(\boldsymbol{P}_{0} \leftarrow\) Generate a random initial population \(P_{i}\) of individuals
    \(\bar{x}=\left(x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right)\), where \(s\) is the number of variables
    \(\left(s_{\text {Anot }} \times 2 s_{P V_{i}}\right)\), according to a multivariate normal distribution
    with mean \(\mu_{0}\) and covariance matrix \(\Sigma_{0}\) such as:
    \(X \sim \mathcal{N}\left(\mu_{0}, \Sigma_{0}\right), \mu_{0}=\mathbf{0}\)
    \(\Sigma_{0}=\left[\begin{array}{ccc}
\sigma_{0, i}^{2} & \cdots & 0 \\
1 & \ddots & \uparrow \\
0 & \cdots & \sigma_{0, i}^{2}
\end{array}\right]\)
    \(\sigma_{0}^{2}=\) large constant value
    For \(g=1,2,3 \ldots\) in number of generations:
    \(P_{g-1}^{I x} \leftarrow\) Evaluate population, sort them according to their fitness
    value and select Se best individuals
    \(P_{g}(x)=\boldsymbol{p}(\boldsymbol{x} \boldsymbol{P}_{g-1}^{I x})=\boldsymbol{\mathcal { N }}\left(\boldsymbol{\mu}_{g}, \boldsymbol{\Sigma}_{g}\right) \leftarrow\) Build the probabilistic
    model: estimate the probability distribution of an individual being
    among the selected individuals, where the mean and the covariance
    matrix are computed as follows:
    \(\mu_{g}=\bar{X}=\frac{1}{N} \sum_{i=1}^{N} x_{i, i} . \quad i=1, \ldots, s\)
    \(\Sigma_{g}=\left[\begin{array}{ccc}
\sigma_{g i}^{2} & \cdots & 0 \\
1 & \ddots & \uparrow \\
0 & \cdots & \sigma_{g i}^{2}
\end{array}\right]\)
    \(\sigma_{g i}^{2}=\frac{1}{N} \sum_{i=1}^{N}\left(x_{i, i}-\bar{X}_{i}\right)^{2} \quad i=1, \ldots, s\)
    \(P_{g} \leftarrow\) Sample a new population from \(p_{g}(x)\)
```

Taking dependencies into account ( $\mathrm{EMNA}_{\text {global }}$ ), increased the computational expense of computing the covariance matrices, but did not reduce the cost function compared to $\mathrm{UMDA}_{c}$. One would expect that taking dependencies into account, while increasing computational expenses, would reduce the number of iterations of the optimizer, since the algorithm would build better distributions to sample from. But $\mathrm{EMNA}_{\text {global }}$ neither reduced the number of iterations nor improved the quality of the solution. Therefore, the $\mathrm{UMDA}_{c}$ algorithm was implemented to solve the optimization problem. The pseudo-code for our implementation of the $\mathrm{UMDA}_{c}$ is shown in Algorithm 2. When sampling the first generation, a large value for the variance of each variable $\sigma_{0}^{2}$ is set to favour the exploration of the solution space.

## 5 | SIMULATIONS

A modified version of the IEEE123 node test feeder was selected to perform the analysis. The IEEE123 node test feeder is a medium-size system with multiple voltage regulators and

![img-4.jpeg](img-4.jpeg)

FIGURE 5 Layout of the modified IEEE123 circuit used for this study. Nine PV systems were added to the circuit and all voltage regulators and shunt capacitors were disabled
shunt capacitors, and a nominal voltage of 4.16 kV . It is characterized by overhead and underground lines with different $\mathrm{X} / \mathrm{R}$ ratios, and considerable imbalance. IEEE123 is a well behavedcircuit with little convergence problems, and it was recommended for the evaluation of new control strategies [35].

The main modifications consist of disconnecting shunt capacitors (nodes 83, 88, 90 and 92) and voltage regulators (lines $9-14,25-26$ and $67-160$ ), and adding PV systems as shown in Figure 5. The modifications allow evaluating if the control provided by the PV inverters is sufficient to overcome voltage problems without the help of conventional equipment. The main effect of the proposed modifications is an overall decrease of the line voltages, especially pronounced in the last nodes of the feeder. This fact leads to uncommon large undervoltages in situations of maximum load. The $5 \%$ and $95 \%$ quantiles of the line voltages shift from 0.956 to 1.037 with shunt capacitors and voltage regulators to 0.929 to 0.990 without shunt capacitors and voltage regulators.

The 9 PV systems were evenly distributed among the three phases and located at the beginning, middle, and end of the line for each phase. The rated power of each system was selected at $1,000 \mathrm{kVA}$ for the total PV rated power be comparable to the total load of the feeder. To evaluate the proposed optimization heuristic in a realistic scenario where the active power injections are non-uniform among the phases (as a result of the control) and will affect the balance of the phases, the PV systems are modelled with single-phase inverters. The peak loads for phase 1,2 and 3 are respectively $1,420 \mathrm{~kW}, 915 \mathrm{~kW}$, and $1,155 \mathrm{~kW}$. The

PV penetration level is $225 \%$ given

$$
\mathrm{PV}_{\text {level }}=\frac{S_{\mathrm{PV}}}{S_{\text {load }}}
$$

where $S_{\mathrm{PV}}$ is the total rated apparent PV power and $S_{\text {load }}$ is the total peak apparent power of the loads.

The optimization problem is solved for 6 different scenarios designed to be representative of the range of situations the optimization algorithm may encounter during actual operation. These 6 scenarios are a combination of 3 irradiance curves (clear, partly cloudy and overcast conditions) and 2 load curves (high and low demand periods) as shown in Figure 6. Although the analysis ignores seasonal changes or week days versus weekend days, these 6 scenarios were considered to be enough to evaluate the performance and robustness of the algorithm.

For each scenario, a power flow is performed every minute for the whole day ( 1440 minutes, Figure 7). To reduce the computational cost, the optimization algorithm calculates the splines (Figure 3) only every 15 minutes. For the next 15 minutes, the operating points (active and reactive power output) are selected from the spline according to the actual PV power output of each PV system. Assuming that points lying between the calculated knots also satisfy the constraints, the actual operational points of the PV inverters are linearly interpolated between the knots and yield the actual power flow.

![img-5.jpeg](img-5.jpeg)

FIGURE 6 Normalized load and irradiance curves selected for each of the six proposed scenarios. Dashed lines represent load curves, and solid lines represent irradiance curves
![img-6.jpeg](img-6.jpeg)

FIGURE 7 Selection process of the operational points for each PV inverter at each time step the simulation is run

The power flows at each time step are solved using OpenDSS. Python scripts automate the process and the optimization routine. The proposed EDA was coded and implemented by the authors from scratch for reasons of flexibility and control over the different aspects of the algorithm

The results of the EDA-based OptGC are compared to six local control strategies: (i) without control (NC), (ii) fixed PF (PF0.98), (iii) VV function with the first curve in Figure 2 (VV), (iv) VV function with a dead band following the second curve in Figure 2, (VVwD), (v) VW function with the third curve in Figure 2, (VW) and (vi) a combined control of VVwD and VW (VVwD+VW).

## 6 | RESULTS

The main results of the simulations for all the scenarios are summarized in Figures 8-10 and Figures 11-13 for the minimum and maximum load, respectively. In the following sections, those results are analyzed in depth.

Clear day (1) Minimum load
![img-7.jpeg](img-7.jpeg)

FIGURE 8 Results for clear day at minimum load conditions

## Partly cloudy day (1) Minimum load

![img-8.jpeg](img-8.jpeg)

FIGURE 9 Results for partly cloudy day at minimum load conditions

## Overcast day (1) Minimum load

![img-9.jpeg](img-9.jpeg)

FIGURE 10 Results for overcast day at minimum load conditions

Clear day (1) Maximum load
![img-10.jpeg](img-10.jpeg)

FIGURE 11 Results for clear day at maximum load conditions

## Partly cloudy day @ Maximum load

![img-11.jpeg](img-11.jpeg)

FIGURE 12 Results for partly cloudy day at maximum load conditions

## Overcast day @ Maximum load

![img-12.jpeg](img-12.jpeg)

FIGURE 13 Results for overcast day at maximum load conditions

### 6.1 | Minimum load scenarios

When studying solar power integration the most common problems are overvoltages during low load and high PV power injection [36]. As the controls in the substation have been disabledthe OLTC are set to operate at 1 p.u. voltages-the minimum load conditions are found to be less problematic. In a different set-up with the OLTC enabled, the minimum load scenarios would be more problematic. One of our objectives was to evaluate if the PV inverters were able to maintain the voltage within the acceptable limits without support from any other device in the grid, including capacitor banks or OLTC.

The results for the minimum load scenarios with clear, partly cloudy and overcast conditions are shown in Figures 8-10, respectively. In those figures, the top plot represents the distribution of voltage magnitudes throughout the day, where the whiskers of the violin plots include $100 \%$ of the values. Bottom left and bottom right plots represent active power curtailment and reactive power used for control, respectively. Different colours represent different phases (red is phase 1, blue is phase 2 and green is phase 3). Different tones of the colours represent different PV systems where darker colours represent PV systems located at a larger distance to the substation. The legend indicates the bus number and the phase number.

In general, OptGC reduces reactive power use and active power curtailment from the PV inverters compared to the local control strategies while maintaining the voltage within the limits most of the time. In minimal load conditions, OptGC operates outside the voltage limits $0.02 \%$ of the total time. These voltage violation events are caused by variations in load within the 15 minutes when the same spline is used in the controller. Since the control is designed to only consider changes in PV power output, it can handle solar variations across the full range of PV power output. But large changes in load may lead to situations not considered by the optimization algorithm, causing voltage violations.

Regarding active power curtailment, while the naïve PF0.98 curtails less active power than OptGC, it comes at the price of larger voltage deviations. Regarding reactive power compensation, the OptGC outperforms every other control strategy in terms of amount of reactive energy absorbed/injected, while the percentage of times outside the voltage limits remains similar. $\mathrm{VV}, \mathrm{VVwD}$, and PF 0.98 , all operate $0.01 \%$ of the time outside the limits, while VVwD+VW always operates within the limits; albeit VVwD+VW curtails 4.2 times more energy than OptGC ( $14,253 \mathrm{kWh}$ in total across the three solar scenarios).

Another interesting finding is that OptGC makes a slightly unbalanced use of power curtailment and reactive power compensation in comparison to local control methods. OptGC actuates control preferentially on phase 1 instead of spreading it equally among all the phases. This behaviour is a result of neutral point shifting, where the reactive power injections/absorptions in one phase affect the voltage in the other phases.

For all the controls, the PV systems at the end of the feeder are more active in regulation (darker colours or higher numbers in the legend in Figures 8-10). This is expected, since nodes

located at the end of the feeder are more prone to suffer voltage violations.

The non-zero values of power curtailment and reactive power use for OptGC in overcast condition are a consequence of the nature of the optimization algorithm which should be considered as an approximator. Near-optimal solutions may lead to small, but unnecessary control actions, such as power curtailment.

## 6.2 | Maximum load scenarios

Although high demand periods are less problematic in PV integration studies, due to the disconnection of the OLTC at the substation and the capacitors banks, the largest voltage violations in our study occur under maximum load conditions.

The results for the maximum load scenarios with clear, partly cloudy and overcast conditions are shown in Figures 11-13, respectively. The structure and colour code of the figures are the same as for minimum load results.

OptGC outperforms every other alternative in terms of reactive power use (except for the PF0.98 control on the overcast day) with a percentage of bad voltage values of $0.2 \%$. Since PF0.98 uses reactive power as a function of the actual PV power delivered, it is expected that on days with low irradiance, PF0.98 will use little reactive power. But PF0.98 fails to maintain the voltages within the allowed range; violations occur $21 \%$ of the time. VVwD+VW and VVwD are close in terms of reactive power usage and voltage stability, but inferior to OptGC. VVwD+VW and VVwD use $46 \%$ and $47 \%$ more reactive power than OptGC, respectively; while the percentages of time outside the voltage limits are $2 \%$ for both. For VV control, the amount of reactive power is 5.9 times higher than OptGC and voltages are violated $0.1 \%$ of the time. VV is the only control that achieves better voltage control than OptGC, but at the cost of a disproportionate amount of reactive power.

As expected, the curtailed energy in maximum load scenarios is considerably lower than in the minimum load scenarios (up to $10,433 \mathrm{kWh}$ ), with maximum values below $2,000 \mathrm{kWh}$. OptGC again outperforms all the methods that make use of power curtailment-except for PF0.98 on the overcast day. Again, there is a slight residual active power curtailment on the overcast day that can be explained by the algorithm as an approximator.

Practically all local control strategies violate the lower voltage limits as observed in the violin plots in Figures 11-13. The severe undervoltage situations experienced in maximum load scenarios are explained by the modifications made to the test feeder (explained in Section 5), primarily the removal of shunt capacitors. OptGC yields a high density of voltage magnitudes close to the lower limit. Since the objective function does not reward voltages being a safe distance away from the lower limit, small variations in the load can force voltage violations which occur $0.2 \%$ of the time. There is a tradeoff between minimizing power used for control and the proximity of voltages to the limit.

PV systems located at the end of the feeder use more reactive power compensation and power curtailment. For OptGC, the
![img-13.jpeg](img-13.jpeg)

FIGURE 14 Percentage of time with voltage violations (out of voltage limits) split by scenario (each colour represents one scenario). Red colours represent the high load scenarios, where most of the voltage violations take place
![img-14.jpeg](img-14.jpeg)

FIGURE 15 Total active power curtailment, reactive and apparent energy used for control in all scenarios
participation of PV systems in the control is unbalanced, with systems in phases 2 and 3 suffering more power curtailment, and systems in phases 1 and 3 using more reactive power compensation. This unbalanced nature of global controllers is due to their ability to inject or absorb reactive power in one phase to avoid voltage violations in the other phases.

### 6.3 | Summary metrics

Figure 14 summarizes the voltage violation results. VV results in the least voltage violations at $0.07 \%$ of the time (or 1,669 minutes). Although the amount of time of OptGC doubles with $0.14 \%$ of the time ( 3096 minutes) outside the voltage limits, both figures are far superior compared to the other strategies. The next controls in the ranking are the VVwD and the VVwD+VW, which are outside of the limits $1.04 \%$ of the time. The remaining strategies violate voltages $10 \%$ of the time.

Figure 15 shows the total amount of reactive power and active power curtailed for each strategy for all scenarios, as well as the total apparent power. Since some strategies only use reactive power compensation, some rely only on active power curtailment, and some use both, ranking the different controls is

![img-15.jpeg](img-15.jpeg)

FIGURE 16 Performance indicators for each control, sorted from best (top) to worst (bottom). Left: EI. Right: average apparent power $\left(S_{\text {avg }}\right)$
difficult. We proposed two new metrics to comprehensively evaluate the performance of the controls by linking the total energy used for control (both curtailed active power and reactive power) with the resulting voltages over all scenarios.

The first indicator, $\dot{S}_{\text {avg }}$, estimates the average apparent power needed for successful voltage regulation

$$
\dot{S}_{\text {avg }}=\frac{S_{\text {control }}}{t_{1 / \text { good }}}
$$

where $S_{\text {control }}$ is the total amount of apparent power used by each control in kVAh and $t_{1 / \text { good }}$ is the number of hours with voltages within the accepted range achieved with that same control. $S_{\text {control }}$ includes the curtailed active power $\left(P_{\text {curs }}\right)$ and the reactive power $(Q)$ in all scenarios as:

$$
S_{\text {control }}=\sqrt{P_{\text {curs }}{ }^{2}+|Q|^{2}}
$$

$\dot{S}_{\text {avg }}$ has units of kVA and evaluates the apparent power expended to achieve an hour of voltages in the permitted range. A smaller $S_{\text {avg }}$ indicates a better performance.

The second indicator, the effectiveness index (EI), quantifies both how effective the control is relative to the usage of apparent power, and its success in voltage regulation. EI is defined as

$$
E I=\left(1-\frac{S_{\text {control }}}{S_{\mathrm{PV}}}\right)\left(\frac{t_{1 / \text { good }}}{t_{\text {total }}}\right)
$$

where $S_{\mathrm{PV}}$ is the total available apparent power (i.e. the sum of the inverter rated powers), and $t_{\text {total }}$ is the total number of hours evaluated ( 6 scenarios x 24 hours). The EI ranges from 0 to 1 and a value of 1 indicates maximum effectiveness.

Figure 16 shows the EI and the average apparent power for each strategy. OptGC scores the best for both indicators. Therefore, (i) OptGC makes the most efficient use of apparent power to obtain voltages within the allowable limits; (ii) OptGC is the most effective control method in terms of how voltage viola-
tions are avoided through judicious use of reactive and active power.

## 6.4 | Benchmarking

In this section, we compare the performance of EDA to two well-known metaheuristics commonly used in optimization problems: GA and particle swarm optimization (PSO).

GA mimics the natural selection by selecting the best individuals in a population for reproduction, generating variance at each generation through crossover and mutation operations. Common GA hyper parameters that need to be tuned are the mutation probability, the crossover probability, the type of crossover, the population size and number of generations. We implemented a GA using Python programming language. Hyper parameters selected were: a mutation probability of 0.5 , a crossover probability of 1 (there is always crossover between all selected candidates), a population size of 1,000 (same as EDA) and a number of generations of 150 without any additional stopping criterion nor tolerance. Regarding the type of crossover, as the individuals or vectors representing the solutions are structured in a very specific manner for our problem (i.e. each vector encodes the curtailed power and reactive power for each knot in a defined order), the crossover operation must preserve this order to avoid the exploration of useless areas in the solution space and hence satisfy the constraints. For that reason, a position-based crossover operation [37] is preferred instead of the classic k-point crossover which splits the individuals at some k arbitrary points.

PSO differs in that there is an initial population (swarm) of individuals (particles), but they are not selected for reproduction. Instead, the particles move through the solution space and their position is evaluated at each iteration (iteration is the equivalent of "generation" in EDA and GA). The movement of the particles is initialized randomly. As the solution evolves, the movement for every iteration is based on each particle's best position reached (cognitive coefficient $c_{1}$ ) and global best of all particles reached (social coefficient $c_{2}$ ). The main hyper parameters that need to be tuned for PSO are those related to the movement, and can be observed in Equations (17) and (18)

$$
\begin{gathered}
x_{i}^{f+1}=x_{i}^{f}+v_{i}^{f+1} \\
v_{i}^{f+1}=\omega \cdot v_{i}+c_{1} \cdot u_{1} \cdot\left(x_{i}^{\text {best }}-x_{i}^{f}\right) \\
+c_{2} \cdot u_{2} \cdot\left(x_{2}^{\text {best }}-x_{i}^{f}\right)
\end{gathered}
$$

where $x_{i}^{f}$ is the current particle position, $v_{i}^{f+1}$ is the particle's movement, $\omega$ is the inertia of the particle, $v_{i}$ is the initial velocity of the particle, $u_{1}$ and $u_{2}$ are uniformly distributed random variables within $[0,1], x_{i}^{\text {best }}$ is the best position attained by the particle, and $x_{2}^{\text {best }}$ is the global best position attained by all particles. We implemented a generic PSO algorithm using Python, with $\omega=0.01, c_{1}=0.7$, and $c_{2}=0.5$. These hyper parameters were selected empirically by testing a different set of values and evaluating compliance with the problem constraints.

![img-16.jpeg](img-16.jpeg)

FIGURE 17 Convergence plot for all the metaheuristics implemented for all optimization runs in the clear day scenario under minimum load conditions. Each line represents one optimization run. There are 96 runs (every 15 minutes for 24 hours) during the day

As the main analysis identified that two scenarios are particularly interesting to study, we benchmarked EDA against GA and PSO for minimum load with clear sky conditions and maximum load with overcast conditions. To allow for a fair comparison between the methods, the same number of generations/iterations (150) was defined for each method.

Figure 17 shows the convergences of the three methods for the clear sky day with minimum load. EDA converges rapidly over the first generations, reaching a plateau after generation 100, and it achieves a smaller fitness value than PSO and GA.

GA has a more stable decay without reaching a plateau, indicating that more generations may be needed to improve the fitness. This stable, but slow decrease of the fitness value is consistent with how new individuals are generated in the GA, which is characterized by randomness in its operation. In contrast, EDA effectively reduces the variance by sampling from a normal distribution constructed by the best individuals, actively searching for the best distribution possible.

PSO converges quickly to a local minimum in the first generations, but it is a factor of 20 larger than the minimum attained by EDA. A closer look at the convergence plot (Figure 17, c, right) reveals sudden steps down in some runs in the last iterations for a few runs. This could mean an insufficient number of iterations.

The results of each heuristic in terms of voltage violations, active power curtailed and usage of reactive power, for the clear day with minimum load conditions are shown in Figure 18. The indicators described in the previous section ( $E I$ and $\hat{S}_{\text {avg }}$ ) for each method are depicted in Figure 19. It can be seen that, although the other methods obtain better results in terms of voltage violations, this comes at the cost of a 10 times more curtailed active power and 37 times more reactive power usage.
![img-17.jpeg](img-17.jpeg)

FIGURE 18 Benchmarking results for clear day at minimum load conditions

Clear day @ Minimum load conditions
![img-18.jpeg](img-18.jpeg)

FIGURE 19 Performance indicators for the benchmarking analysis of the clear day at minimum load conditions scenario

The small improvement for GA and PSO in the voltages violations (less than a $0.1 \%$ ) does not justify the excessive increase of curtailed power and reactive power usage as shown by the indicators in Figure 19, especially the average consumption of apparent power.

The results are similar for the overcast day with maximum load conditions. The voltage and power results are shown in Figure 20 and the indicators are shown in Figure 21. As it can be seen in Figure 20, again the voltage violations are improved for GA and PSO, but this comes at the expense of an increase in reactive power used by over a factor 7 . Once again, EDA scores the best in both indicators, showing that it makes better use of reactive power and power curtailment.

## 7 | DISCUSSION

The proposed EDA-based optimization has been proven to be an excellent approximator for optimizing voltage regulation

Overcast day @ Maximum load conditions
![img-19.jpeg](img-19.jpeg)

FIGURE 20 Benchmarking results for overcast day at maximum load conditions

Overcast day @ Maximum load conditions
![img-20.jpeg](img-20.jpeg)

FIGURE 21 Performance indicators for the benchmarking analysis of the overcast day at maximum load conditions scenario
with PV inverters, yielding suitable solutions in a reasonable time. Although, the EDA leads to some suboptimal solutions (cases where there are residual values of $P_{r}$ and $Q$ even if they are not needed), the reduction in use of power dedicated to voltage regulation compared with other local control strategies is significant.

For the IEEE123 circuit and the specific setup of PV inverters, PV inverters were able to accomplish all the voltage regulation. Although there is a minimal amount of time where the voltage is outside the ANSI limits, these situations may be overcome with different configurations of the optimization algorithm (for example, setting more restrictive voltage limits) or if the Watt-Watt and Watt-var control curves were updated at every time step (instead of updating them every 15 minutes).

Voltage violations mostly result from solar or load variability within the 15 -minute updates of the control curves. Solar variability can be significant over time scales of a few minutes. The control curves prescribe changes in the PV Watt and var
output as a function of PV active power. Therefore, solar variability directly affects the control curves and does so at every control time step ( 1 minute). But the coordination of the control curves across inverters will no longer be optimal given that solar variability causes changes in the state of the grid since the most recent 15 -minute control curve time step. Therefore, voltage violations-or more generally suboptimal voltage controlmay result from solar variability.

Some voltage violations in the OptGC strategy are caused by the inability of the optimization problem to take into account the load variability. Again, running the optimization algorithm every minute would solve most of these voltage violations. But short-term uncontrolled voltage variability is common in electric distribution systems; load tap changers, which are common voltage control devices, are not capable of handling rapid voltage fluctuations either. Load tap changers only act after the voltage has exceeded the threshold for a certain amount of time, typically 10 s of seconds to a minute. The control delay associated with load tap changers suggests that fast load fluctuations are not that common or important in distribution grid operations.

Other findings are aligned with the results expected from the literature. First, there is a clear positive correlation between the distance to the substation and the amount of power used for control purposes [8]. This is an expected behaviour because voltages at the end of the feeder differ more from the substation voltage. Second, in three-phase four-wire configurations, the actuations on one phase affects the voltage of other phases, due to the shifting of the neutral point [30]. OptGC takes advantage of neutral point shifting by optimizing the control to act more on some phases instead of even control among all the phases. Third, the EDA performs well in this problem despite the large number of variables. Since EDAs extract global statistical information from the populations they are immune to potential local minimal, making them good candidates to solve power systems optimization problems [19].

The EDA performance was benchmarked against other state-of-art metaheuristics (GA and PSO). EDA outperformed both methods, in terms of the quality of the solutions. This matches other results in the literature [19], [20], where the more active search strategy of EDAs led to better solutions in less iterations.

This study could be extended as follows:
(i) Using different strategies in the EDA algorithm (e.g. efficiently building a model with multivariate dependencies). Although the EDA-based strategy still needs to be evaluated with a larger number of PV systems in the grid, based on our preliminary analysis we expect a similar performance if the same strategy without variable interdependencies (UMNA) is used.
(ii) Extending the optimization problem to consider variations in load. The solutions input to the global control would then have an extra dimension (that is, they would be planes instead of splines) to represent load variation.
(iii) Adding more PV systems on the grid; or targeting runs for specific load and solar PV value based on probabilistic forecasts; and reducing the computational cost, e.g. by varying

the number of generations being created at each optimization run.
(iv) Unrelated to EDA one could optimize the VV control curves, since it performs quite well in most scenarios.

## 8 | CONCLUSION

In this study, an EDA-based optimized global voltage control for PV systems in a three-phase four-wire distribution grid was evaluated. The objective was to find out if PV inverters were able to maintain voltages within ANSI limits without any other regulation device on the grid while minimizing the amount of active power curtailed and the use of reactive power. To evaluate the performance of the optimization algorithm, six scenarios with different load and irradiance conditions were analyzed, and the results were compared to other standard local controls.

The OptGC outperformed every other alternative in terms of apparent energy dedicated to control, averaging 0.48 kVAh per hour of good voltage values. In terms of voltage quality, only the VV local control (VV) performs slightly better (with voltage violations $0.07 \%$ of the time versus $0.14 \%$ for the OptGC), but with a less efficient use of the energy based on the EIs.

The viability of using PV inverters as the only source of voltage regulation has been demonstrated, at least for the IEEE123 test feeder. The main limitations encountered by the strategy are related to the formulation of the optimization problem, which does not take into account variations in load conditions, which lead to some undervoltages.

The suitability of using EDA as approximators in power system related optimization problems with a high number of variables was demonstrated. EDA provides quality solutions in a reasonable time.

## ACKNOWLEDGEMENTS

This work was funded by the Spanish Ministerio de Ciencia, Innovación y Universidades (RTI2018-095563-B-I00), the "Agencia Canaria de Investigación, Innovación y Sociedad de la Información (ACIISI) de la Consejería de Economía, Industria, Comercio y Conocimiento" and the European Social Funds (ESF). The authors also thank the Fostering Grads program and the "Cabildo de Tenerife", for the funds received to make the research visit to the University of California, San Diego, from which this work is derived.
