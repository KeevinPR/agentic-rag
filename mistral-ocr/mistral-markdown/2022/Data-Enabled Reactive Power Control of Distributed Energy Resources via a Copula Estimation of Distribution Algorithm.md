# Data-Enabled Reactive Power Control of Distributed Energy Resources via a Copula Estimation of Distribution Algorithm 

Dennis van der Meer* (D)<br>MINES Paris - PSL University, Centre for<br>Processes, Renewable energies and Energy systems<br>Sophia Antipolis, France<br>Hamed Valizadeh Haghi (D),<br>Jan Kleissl (D)<br>Dept. of Mechanical and Aerospace<br>Engineering, University of California<br>San Diego, USA<br>Joakim Widén (D)<br>Dept. of Civil and Industrial<br>Engineering, Uppsala University<br>Uppsala, Sweden


#### Abstract

The increase in the number of distributed energy resources (DERs) in the low-voltage grid causes reverse active power flow, which induces voltage regulation issues across the feeder. We employ the parameter-free copula estimation of distribution algorithm (EDA) that optimally controls the reactive power of DERs to minimize voltage deviations. EDAs iteratively learn from data and sample an explicit probability distribution that models the dependencies between variables, allowing for a more effective exploration of the optimal solution space with fewer iterations. A copula offers additional flexibility, since the dependence structure between the decision variables and the marginal distributions can be modeled independently. The effectiveness of the proposed method is illustrated on a modified IEEE 123 node test feeder with 10 smart photovoltaic inverters. The results show that the proposed method achieves improved voltage profiles and offers many opportunities for further adaptability. Index Terms-Distributed generation, voltage/VAR control, distribution network, centralized optimization


## I. INTRODUCTION

The increase in the number of distributed energy resources (DERs) in distribution feeders induces variable and sometimes reverse active power flow. The associated voltage variability can be uneven across the feeder and poses a major challenge to distribution system operation [1]. Step down transformers with on-load tap changers (OLTCs) and switching capacitor banks may be unable to regulate voltage, despite attempts at optimal allocation [2] or optimal sizing [3], and they experience lower life expectancy due to an increased number of operations [4]. Other solutions include active power curtailment and grid reinforcement; however, these are economically less attractive.

Inverter-based DERs can contribute to voltage regulation through reactive power injection or absorption. Reactive power control in distribution grids reduces marginal costs of DER grid integration and increases the hosting capacity of distribution grids [5]. Reactive power control strategies can broadly

[^0]be divided into three approaches: (1) local control, (2) central control, and (3) a combination of local and central control.

## A. Local control

Local control typically relies on stand-alone control of DERs [6]-[8], or DER controllers that may exchange information with their nearest neighbors [9]. The disadvantage of local control is that decisions are based on incomplete information regarding the state of the distribution grid, while the advantages are fast response rates and the absence of a full communication system. Stand-alone reactive power control was applied by [7] by means of a droop control function, while [8] used an optimal $Q(P)$ (reactive power as a function of active power) curve and [6] proposed an adaptive local volt/var algorithm that switches between power loss minimization and voltage regulation depending on whether the voltage is close enough to the voltage at the substation.

## B. Central control

As opposed to local control, central control requires a system-wide two-way communication system. The state of the distribution grid is then known and the influence of DER control on the system can be assessed, allowing improved convergence of the optimization of DER control settings. The need for a communication system is simultaneously a disadvantage of central control because of the associated costs.

Evolutionary and population based methods are quite common in DER control optimization as few or no problem assumptions are required. For instance, [10] developed coordinated voltage support capable of online application based on evolutionary particle swarm optimization (PSO) and a neural network that maps the behavior of the distribution grid. To avoid local minima, researchers have employed evolutionary programming with dynamic mutation to minimize network losses, voltage deviation and compensation cost [11].

Convergence issues have led researchers to use more traditional optimization methods. For instance, [12] employed mixed integer nonlinear programming to minimize DER curtailment and compared it against mixed integer quadratically


[^0]:    *Corresponding author: dennis.van_der_meer@minesparis.psl.eu Part of the present research was carried as part of the Smart4RES Project (European Union's Horizon 2020, No. 864337).

constrained programming. Sequential convex programming was used to minimize total reactive power injection of DERs [13]. To employ the most effective DERs, [14] considered a two-stage optimization scheme, where the first stage selected the DERs with the most impact on the voltage level and the second stage optimized their active and reactive power setting.

## C. Distributed control

To avoid a system-wide two-way communication system, researchers employed agent-based techniques that follow a top-down chain of command, but let the bottom layer (distribution grid) solve certain issues without intervention of top layers [15]. The disadvantage of this type of control is limited system awareness in case of a contingency. Local smart control was proposed by [16] through piece-wise linear functions, the parameters of which were regularly optimized centrally. A similar approach was proposed by [17], who used local control to provide fast response and a central controller to balance a multiple time-step problem.

## D. Contributions

A photovoltaic (PV) system is a DER that generates electricity from solar irradiance, which is a spatially and temporally correlated process that impacts the feeder unevenly due to the heterogeneity in cloud cover and infrastructure such as line ratings. Central control allows for exploitation of the spatiotemporal relationship, although none of the studies reviewed in Section I-B explicitly did, except for [14]. ${ }^{1}$ We employ a copula estimation of distribution algorithm (EDA) that explicitly accounts for-by means of a correlation matrixthe spatio-temporal variation in solar irradiance.

This paper presents the first application of a copula EDA in power systems which results in the following novelties in central reactive power control of distribution system voltages:

1) Copula EDAs enable explicit probabilistic parameterfree modeling of the intrinsic spatial relationship of reactive power control by distributed PV inverters.
2) Temporal association of the optimal reactive power settings allows warm starting the optimization at every time step, thus enhancing search space exploration.
The remainder of this paper is organized as follows. Section II presents reactive power control and the optimization problem. Section III describes the copula EDA in detail. Section IV presents the results of reactive power control using the copula EDA on a standard test feeder, while Section V provides the conclusions.

## II. Problem Formulation

A common feature of (weak) distribution feeders is the high line resistance compared to the line reactance, i.e., a high $R / X$ ratio. This exacerbates the voltage difference $\Delta V$ across the line, as can be deduced from the following approximation [5]:

$$
V_{1}-V_{2}=\Delta V \approx R \cdot P+X \cdot Q
$$

[^0]where $P$ and $Q$ are active and reactive power (in W and var), respectively. Equation (1) shows that variable active power injection via DERs increases voltage, but reactive power absorption can balance the voltage rise. Smart inverters can counteract voltage fluctuations using reactive power on the same timescale as solar irradiance fluctuations, as opposed to slow controllable devices such as OLTCs [17]. We formulate voltage stabilization to 1 p.u. as an optimization problem using smart inverter reactive power as decision variable as follows:

$$
\begin{aligned}
& \min _{Q_{j}} \sum_{j=1}^{M}\left|1-V_{j}\right| \\
& \text { s.t. } P_{i}=\left|V_{i}\right| \sum_{k=1}^{N}\left|V_{k}\right|\left(G_{i k} \cos \left(\theta_{i}-\theta_{k}\right)\right. \\
& +B_{i k} \sin \left(\theta_{i}-\theta_{k}\right)), \\
& \forall i, k \in \mathcal{I}, \\
& Q_{i}=\left|V_{i}\right| \sum_{k=1}^{N}\left|V_{k}\right|\left(G_{i k} \sin \left(\theta_{i}-\theta_{k}\right)\right. \\
& \left.+B_{i k} \cos \left(\theta_{i}-\theta_{k}\right)\right), \\
& \forall i, k \in \mathcal{I}, \\
& Q_{j} \leq Q_{j} \leq \bar{Q}_{j}, \\
& \forall j \in \mathcal{J}, \\
& \forall j \in \mathcal{J}, \\
& S_{j}^{2}=\bar{Q}_{j}^{2}+P_{j}^{2}, \\
& \forall j \in \mathcal{J} .
\end{aligned}
$$

In the formulation above, the set of all buses $\mathcal{N}$ with index set $\mathcal{I}=\{1,2, \ldots, N\}$ is indexed by $i$ and $k$, i.e., $\left\{\mathcal{N}_{i, k}\right\}_{i, k \in \mathcal{I}}$. Similarly, the set of all buses with DERs installed is $\left\{\mathcal{M}_{j, l}\right\}_{j, l \in \mathcal{J}}$ with $\mathcal{J}=\{1,2, \ldots, M\}$ and $\mathcal{M} \subset \mathcal{N}$. Furthermore, $G_{i k}$ and $B_{i k}$ represent elements from the real and imaginary part of the admittance matrix, respectively, and $\theta$ the voltage phase angle. The transformer primary side voltage is assumed to be constant and 1 p.u., therefore $V_{j}$ in (2a) is expressed in p.u. The optimization problem in (2a)-(2e) differs from the classic optimal power flow (OPF) problem in that (2e) applies to the DERs in $\mathcal{M}$ rather than all buses in $\mathcal{N}$ and in that the voltage phase angle is not explicitly constrained [19]. The formulation in (2a)-(2e) disregards line limits because the voltage magnitude is often the most limiting factor when it concerns DER hosting capacity [20]. However, such a constraint could be included in future work and active power curtailment could be used to satisfy this constraint if necessary.

Equation (2f) determines the reactive power limit as a function of the inverter rated capacity $S$ (in VA). For the inverters, Watt priority is assumed, i.e., real power is not curtailed to enable more reactive power control and the reactive power limit $\bar{Q}_{i}$ therefore depends on the active power output and the inverter rated capacity. There are no further restrictions on reactive power output, so $Q_{j}$ can assume any value that satisfies (2f). Watt priority with undersized inverters would limit the ability for reactive power support during the times when it is most needed, i.e., when high solar PV generation leads to overvoltages. To enable voltage control at all times, inverters are oversized by $10 \%$ compared to the PV DC power capacity. Therefore, even for solar PV operating at rated DC


[^0]:    ${ }^{1}$ Note that population based methods such as PSO assume some dependence structure that is encoded by the control parameters [18].

power, $42 \%$ of the reactive power remains available for voltage control.

## III. Copula EDA-Based VAR CONTROL

An EDA is a probabilistic population-based optimization approach that iteratively learns and samples probability distributions of candidate solutions, while also modeling the dependencies between the decision variables by means of a multivariate probability distribution. A copula EDA offers more flexibility than an EDA because the marginal distributions, i.e., the distributions that describe the decision variables, and the multivariate distribution are fitted separately [21]. Consequently, the marginals can be nonparametric even if a multivariate Gaussian distribution is used.

Consider $M$ random variables $X_{1}, X_{2}, \ldots, X_{M}$ with realizations $x_{1}, x_{2}, \ldots, x_{M}$ and cumulative distribution functions (CDFs) $F_{X_{1}}, F_{X_{2}}, \ldots, F_{X_{M}}$. According to Sklar's theorem, these distributions can be coupled via a copula $C$ using a copula function [22]. In this study, we employ the Gaussian copula, which is defined as [22]:

$$
C_{\mathbf{K}}(\boldsymbol{u})=\Phi_{\mathbf{K}}\left(\Phi_{X_{1}}^{-1}\left(u_{1}\right), \ldots, \Phi_{X_{M}}^{-1}\left(u_{M}\right) \mid \mathbf{K}\right)
$$

where $\Phi$ the standard normal distribution, $F_{X_{j}}\left(x_{j}\right)=$ $u_{j}, \forall j \in \mathcal{J}$ is the probability integral transform, $\mathbf{K}$ is a symmetric positive semi-definite correlation matrix, and $u_{j}$ is a realization of the standard uniform random variable $U_{j}$. In other words, a copula is a multivariate CDF with standard uniform marginals. We fit the empirical marginal distributions with kernel density estimation (KDE) using a standard normal kernel and the rule-of-thumb bandwidth estimator. Since the marginals are non-normal, the correlation matrix $\mathbf{K}$ of the Gaussian copula can be estimated by inversion of Kendall's tau such that $K_{j l}=\sin \left(\pi / 2 \hat{\tau}_{j l}\right)$ for each pair of variables $j, l \in \mathcal{J}$ [22]. Other copulas may be more suitable for very large networks with many DERs. For instance, C-vines and D-vines copulas limit computations to bivariate copulas. We would like to leave that for future work.

Algorithm 1 describes the implementation of the copula EDA. It is a population-based optimization method where $M$ populations evolve over several generations, indexed by $g \in \mathcal{G}=\{1,2, \ldots, G\}$. The aim is to refine the population fitness, i.e., to minimize (2a), until one of the stopping criteria is met. For every time $t$, the first step is to compute $\bar{Q}_{j, t}$ and $\bar{Q}_{j, t}$ based on the active power production (2f) since we assume Watt priority. If $g=1$ and $t=1$, we uniformly sample $D$ population members $Q_{j, g, t} \forall j \in \mathcal{J}$ (line 6). Otherwise, if $t>1$ we sample $50 \%$ of the population members uniformly and take the fittest $50 \%$ of population members $Q_{j, g, t-1}$ (line 9). In words, we assume that the fittest population members at the previous time step can warm start the optimization at time $t$, which is reasonable because of the autocorrelation that is present. Each if-else statement is completed by evaluating the fitness of the population members using (2a).

In case both $g$ and $t$ are greater than 1 , we sample $50 \%$ of the population members uniformly and take the fittest

## Algorithm 1: Copula EDA

for $t=1: T$ do
Calculate $Q_{j, t}$ and $\bar{Q}_{j, t}$ using (2f) ;
$g \leftarrow 1$;
while stopping criteria not met do
if $g=1$ and $t=1$ then
Generate samples $Q_{j, g, t}$ uniformly such that $Q_{j, g, t} \leq Q_{j, g, t} \leq Q_{j, g, t}$;
Evaluate the fitness of samples $Q_{j, g, t}$;
else if $g=1$ and $t>1$ then
Combine the top $50 \%$ of $Q_{j, g, t-1}$ and randomly sample the remaining $50 \%$ to generate $Q_{j, g, t}$;
Evaluate the fitness of samples $Q_{j, g, t}$;
else
Select the top $50 \%$ from $Q_{j, g-1, t}$ and randomly sample the remaining $50 \%$;
Fit empirical marginal distributions using KDE ;
Transform the samples $Q_{j, g, t}$ to uniformly distributed samples in $[0,1]$;
Estimate the correlation matrix $\mathbf{K}$ of the Gaussian copula by inversion of Kendall's tau ; Generate uniformly distributed samples from the Gaussian copula with dependence structure determined by $\mathbf{K}$;
Transform the uniformly distributed samples back to $Q_{j, g, t}$ via the inverse CDF ;
If samples $Q_{j, g, t}$ do not satisfy the constraints, apply a local optimization method ;
Evaluate the fitness of samples $Q_{j, g, t}$;
end
$g=g+1$
end
end
$50 \%$ of population members $Q_{j, g-1, t}$ (line 12), which is referred to as "selection". Lines 13-15 estimate the marginal and multivariate probability distributions based on current population members $Q_{j, g, t}$. Using the multivariate probability distribution characterized by $\mathbf{K}$, we sample uniformly distributed population members (line 16) that are transformed back to reactive power population members via the inverse CDF (line 17). Before computing the fitness of the population members using (2a), we first verify that all population members satisfy constraints (2a)-(2e) and project members that violate the constraints back to the feasible set. The algorithm can be visualized as a multivariate probability distribution with decreasing variance (by re-estimation) as it moves (by selection) towards the optimal solution.

## IV. RESULTS AND DISCUSSION

## A. Test Feeder and PV Profiles

We illustrate the effectiveness of the copula EDA on the modified IEEE 123 node test feeder, see Fig. 1. Each node features the same load profile that is multiplied with the node's specific spot load that can be retrieved from [24]. Since the spot loads are relatively large, the PV systems have to be sized accordingly in order to induce voltage violations. The total nominal capacity of the 10 PV systems is therefore 10 MVA and these are placed randomly on the feeder, see Fig. 1.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The IEEE 123 node test feeder. Squares indicate placement of the PV systems on nodes $18,48,56,66,79,83,95,250,300$ and 450 with nominal capacities $588 \mathrm{kVA}, 1176 \mathrm{kVA}, 1681 \mathrm{kVA}, 420 \mathrm{kVA}, 756 \mathrm{kVA}, 1344 \mathrm{kVA}$, $1681 \mathrm{kVA}, 1176 \mathrm{kVA}, 504 \mathrm{kVA}$ and 672 kVA , respectively.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Top: Daily load and PV profiles. The solid lines are 10 spatially and temporally correlated PV power profiles, generated using the model introduced in [23]. The sunrise and sunset times for the clear sky profile differ from the partly cloudy day, because it is a different day. Bottom: Autocorrelation function (ACF) of the respective time series.

We consider single-phase connections and leave the study of voltage unbalance and neutral-point shifting for future work. However, we note that considering three-phase connections allows for load balancing, which has been shown to be effective in mitigating voltage violations [25].

Figure 2 (top) presents the daily active power load and irradiance profiles for the numerical analysis that have been normalized min-max scaling and then upscaled by multiplying with the spot loads and DER capacities presented in Fig. 1, respectively. These profiles form the basis of our case study: spatially and temporally correlated profiles are assigned to each PV system to emulate cloudy conditions with lower correlation. The irradiance profiles are generated by transforming points in time and space to points in a propagating cloud field, which allows for realistic spatially and temporally correlated irradiance profile generation based on cloud field velocity and hourly average clear-sky index trained on the pyranometer network in Oahu, Hawaii and applied to measurements at the

University of California, San Diego on 14 July 2011 [23], [26].
Figure 2 (bottom) presents the autocorrelation function (ACF) of the time series presented in the upper part of the figure. All time series contain significant autocorrelation, which is why it is reasonable to assume that carrying over samples between time steps could improve the performance of the copula EDA. We show the efficacy of carrying the samples forward in time in Section IV-D.

## B. Control Implementation and Settings

To model the copula EDA, we use copulaedas [21] in the statistical software R. The script that solves the AC power flow equations is written in Matlab. The scripts and data are publicly available on GitHub ${ }^{2}$.

The optimization contains two stopping criteria: (i) a function evaluation tolerance (the maximum allowable difference between the objective-zero voltage deviation-and the best solution in p.u.), and - in case (i) cannot be satisfied - (ii) the maximum number of iterations. In addition, the optimization requires setting the population size. While a small function evaluation tolerance or a large population size increases the model run time, a large function evaluation tolerance or a small population size can deteriorate the effectiveness of the control. To evaluate the sensitivity to the function evaluation tolerance and the population size, we test with population sizes of 75 and 100 and function evaluation tolerances of 0.1 p.u. and 0.01 p.u.

## C. Benchmarks

The copula EDA is compared to four benchmarks. (i) Unity power factor, i.e., no reactive power injection. (ii) Local volt/var control according to IEEE standards [27]. (iii) A copula that assumes independence between the decision variables. The algorithm is based on the univariate marginal distribution algorithm (UMDA) that uses the same marginals as the copula EDA and is implemented using copulaedas [21]. (iv) The OPF problem that includes line constraints. The script is developed by [28] and adapted to our case studies. The original script solves the OPF problem with PSO and is available online [29]. We set the population size and the maximum number of iterations identical to the setting of the copula EDA and the UMDA and leave the remaining parameters to their default setting.

## D. Numerical Analysis—Case study

As mentioned above, the case study considers PV power profiles during a cloudy day with considerable variability and subsequently lower spatial and temporal correlation (cf. Fig. 2). Figure 3 shows time series of the voltages across all buses in terms of the $99 \%$ probability interval, plotted for the four combinations of sample size ("POP") and function evaluation tolerance ("TOL"). Note that "001" and "01" are function evaluation tolerances of 0.01 p.u. and 0.1 p.u., respectively. Furthermore, the figure includes the unity power factor (PF1) and volt/var control strategies as well. PF1 increases the

[^0]
[^0]:    ${ }^{2}$ https://github.com/DWvanderMeer/Data-Enabled-Reactive-Power-Control

![img-2.jpeg](img-2.jpeg)

Fig. 3. 99\% probability interval of the voltage time series for the four combinations of sample size ("POP") and function evaluation tolerance ("TOL") for the second case study (cloudy sky). The different line colors represent the models.

TABLE I
LAST GENERATION RESULTS EXPRESSED AS MEAN AND STANDARD DEVIATION OVER ALL TIME STEPS. BOLD OBJECTIVE FUNCTION EVALUATIONS INDICATE UNSATISFIED TOLERANCE ON AVERAGE.

| Run | Model | Objective function (p.u.) | Number of <br> iterations ( $t$ ) | SD (p.u.) |
| :-- | :--: | :--: | :--: | :--: |
| POP100TOL001 | EDA | $8.9 \times 10^{-3} \pm 2.0 \times 10^{-3}$ | $5.9 \pm 3.8$ | $1.2 \times 10^{-3}$ |
| POP100TOL01 | EDA | $4.3 \times 10^{-2} \pm 2.4 \times 10^{-2}$ | $1.0 \pm 0.1$ | $4.9 \times 10^{-3}$ |
| POP75TOL001 | EDA | $9.1 \times 10^{-3} \pm 2.0 \times 10^{-3}$ | $6.2 \pm 4.1$ | $1.2 \times 10^{-3}$ |
| POP75TOL01 | EDA | $4.0 \times 10^{-2} \pm 2.2 \times 10^{-2}$ | $1.0 \pm 0.3$ | $4.6 \times 10^{-3}$ |
| POP100TOL001 | PSO | $\mathbf{1 . 1} \times \mathbf{1 0}^{-2} \pm 3.0 \times 10^{-3}$ | $11.7 \pm 3.7$ | $1.8 \times 10^{-3}$ |
| POP100TOL01 | PSO | $5.4 \times 10^{-2} \pm 1.2 \times 10^{-2}$ | $1.0 \pm 0.1$ | $6.9 \times 10^{-3}$ |
| POP75TOL001 | PSO | $\mathbf{1 . 3} \times \mathbf{1 0}^{-2} \pm 4.0 \times 10^{-3}$ | $13.2 \pm 3.0$ | $2.1 \times 10^{-3}$ |
| POP75TOL01 | PSO | $6.0 \times 10^{-2} \pm 1.4 \times 10^{-2}$ | $1.0 \pm 0.0$ | $7.8 \times 10^{-3}$ |
| POP100TOL001 | UMDA | $\mathbf{3 . 2} \times \mathbf{1 0}^{-2} \pm 2.2 \times 10^{-2}$ | $11.1 \pm 4.8$ | $4.0 \times 10^{-3}$ |
| POP100TOL01 | UMDA | $6.5 \times 10^{-2} \pm 2.4 \times 10^{-2}$ | $1.4 \pm 0.6$ | $6.7 \times 10^{-3}$ |
| POP75TOL001 | UMDA | $\mathbf{3 . 5} \times \mathbf{1 0}^{-2} \pm 2.4 \times 10^{-2}$ | $11.3 \pm 4.6$ | $4.3 \times 10^{-3}$ |
| POP75TOL01 | UMDA | $6.6 \times 10^{-2} \pm 2.6 \times 10^{-2}$ | $1.5 \pm 0.6$ | $7.0 \times 10^{-3}$ |

voltage well above above the upper ANSI limit for voltage deviation while the local volt/var control strategy exactly respects the upper ANSI limit. The optimization strategies maintain the voltage well within the ANSI limits. While a lower function evaluation tolerance smooths the voltage profile and maintains it closer to 1 p.u., this comes at the cost of computational efficiency as indicated by the increased number of required iterations (cf. Table I). The smoothness of the voltage profile in Fig. 3 is summarized by the standard deviation (SD) in Table I, which shows that a function evaluation tolerance of 0.01 p.u. results in a much smoother voltage profile compared to a function evaluation tolerance of 0.1 p.u. and that the copula EDA control actions result in the lowest voltage variability.

Table I presents the average and the standard deviation of the objective function achieved by each model over all time steps. The copula EDA satisfies the function evaluation tolerance, regardless of the population size. Conversely, PSO and UMDA are not, on average, able to satisfy the 0.01 p.u. function evaluation tolerance within the 15 iterations. Although it could be argued that the function evaluation tolerance of 0.01 p.u. is too stringent, it is clear that the copula EDA outperforms the benchmarks. In contrast, the function evaluation tolerance of 0.1 p.u. appears trivial to achieve, as all models require fewer than 2 iterations on average. We did not encounter excessive line loading in our results.

## E. Relative contribution of DERs

We present the distribution of reactive power control settings for each solar PV system during high voltages around noon in Fig. 4. The UMDA does not favor any particular inverter for reactive power control as shown by the elongated box plots. This behavior is caused by the independence assumption; each inverter appears to be randomly employed because the initial population is randomly sampled and the independence assumption prevents convergence of the multivariate distribution. PSO frequently employs inverter 250, 83 and 95 and occasionally employs the others as well. The copula EDA favors inverters 56, 250 and 66, which are located closer to the transformer than the inverters employed by PSO and more evenly spread out over the feeder.

## V. Conclusions and Future Work

We presented a copula estimation of distribution algorithm (EDA) applied to centralized optimal reactive power control. The objective of the copula EDA was to minimize the voltage fluctuation from 1 p.u. caused by significant active power injection by distributed solar photovoltaic (PV). Tests on the modified IEEE 123 node test feeder showed that the copula EDA significantly reduced the voltage fluctuations. Key advantages of the copula EDA are that (i) it allows separate modeling of the dependence structure between the decision variables and the marginal distributions, enabling it to accurately learn the spatial relationship between the voltage control points by means of a copula while the marginal distributions can be estimated empirically; (ii) copula EDA takes advantage of the temporal correlation by moving some of the best performing population members forward in time; (iii) copula EDA is parameter-free unlike other heuristic optimization algorithms such as PSO; and (iv) copula EDA is interpretable due to its statistical foundation. We showed that the copula EDA satisfies the most stringent function evaluation tolerance ( 0.01 p.u.) on average, whereas the benchmarks did not. Moreover, the copula EDA required fewer iterations on average compared to the benchmarks. Regarding inverter contribution, the copula EDA consistently favored a limited number of inverters that were evenly spread out over the feeder, unlike the benchmarks that

![img-3.jpeg](img-3.jpeg)

Fig. 4. The distribution of reactive power control settings for each solar PV system for 10 time steps around noon. The reactive power is normalized by the inverter nominal capacity. The inverters are organized by increasing distance from the substation.
either employed inverters randomly or the inverters located on the edges of the feeder.
In future work, we will test various types of copulas, e.g., Cvines and D-vines, that allow for greater flexibility in modeling the dependence structure since they are based on bivariate probability distributions. Another improvement is to create a local version of the copula EDA by considering information from neighboring solar PV systems and joining them in a tree structure, similar to vine copulas. Such an approach could improve computational performance, while the tree structure would retain the spatial information of the network. Finally, further research is required to include neutral-point shifting in unbalanced networks.

## REFERENCES

[1] R. A. Shayani and M. A. G. de Oliveira, "Photovoltaic generation penetration limits in radial distribution systems," IEEE Trans. Power Syst., vol. 26, no. 3, pp. 1625-1631, Aug 2011.
[2] B. A. de Souza and A. M. F. de Almeida, "Multiobjective optimization and fuzzy logic applied to planning of the volt/var problem in distributions systems," IEEE Trans. Power Syst., vol. 25, no. 3, pp. 1274-1281, Aug 2010.
[3] S. X. Chen, Y. S. Foo. Eddy, H. B. Gooi, M. Q. Wang, and S. F. Lu, "A centralized reactive power compensation system for lv distribution networks," IEEE Trans. Power Syst., vol. 30, no. 1, pp. 274-284, Jan 2015.
[4] F. Katiraei and J. R. Aguero, "Solar pv integration challenges," IEEE Power Energy Mag., vol. 9, no. 3, pp. 62-71, May 2011.
[5] P. N. Vovos, A. E. Kiprakis, A. R. Wallace, and G. P. Harrison, "Centralized and distributed voltage control: Impact on distributed generation penetration," IEEE Trans. Power Syst., vol. 22, no. 1, pp. 476-483, Feb 2007.
[6] H. Yeh, D. F. Gayme, and S. H. Low, "Adaptive var control for distribution circuits with photovoltaic generators," IEEE Trans. Power Syst., vol. 27, no. 3, pp. 1656-1663, Aug 2012.
[7] P. Jahangiri and D. C. Aliprantis, "Distributed volt/var control by pv inverters," IEEE Trans. Power Syst., vol. 28, no. 3, pp. 3429-3439, Aug 2013.
[8] S. Weckx and J. Driesen, "Optimal local reactive power control by pv inverters," IEEE Trans. Sustain. Energy, vol. 7, no. 4, pp. 1624-1633, Oct 2016.
[9] Z. Tang, D. J. Hill, and T. Liu, "Fast distributed reactive power control for voltage regulation in distribution networks," IEEE Trans. Power Syst., vol. 34, no. 1, pp. 802-805, Jan 2019.
[10] A. G. Madureira and J. A. Pecas Lopes, "Coordinated voltage support in distribution networks with distributed generation and microgrids," IET Renewable Power Gener., vol. 3, no. 4, pp. 439-454, December 2009.
[11] C. Jiang and C. Wang, "Improved evolutionary programming with dynamic mutation and metropolis criteria for multi-objective reactive power optimisation," IEE Proceedings - Gener., Transmiss. Distrib., vol. 152, no. 2, pp. 291-294, March 2005.
[12] F. Capitanescu, I. Bilibin, and E. Romero Ramos, "A comprehensive centralized approach for voltage constraints management in active distribution grid," IEEE Trans. Power Syst., vol. 29, no. 2, pp. 933-942, March 2014.
[13] S. Deshmukh, B. Natarajan, and A. Pahwa, "Voltage/var control in distribution networks via reactive power injection through distributed generators," IEEE Trans. Smart Grid, vol. 3, no. 3, pp. 1226-1234, Sep. 2012.
[14] T. Ding, C. Li, Y. Yang, J. Jiang, Z. Bie, and F. Blaabjerg, "A two-stage robust optimization for centralized-optimal dispatch of photovoltaic inverters in active distribution networks," IEEE Trans. Sustain. Energy, vol. 8, no. 2, pp. 744-754, April 2017.
[15] A. A. Aquino-Lugo, R. Klump, and T. J. Overbye, "A control framework for the smart grid for voltage support using agent-based technologies," IEEE Trans. Smart Grid, vol. 2, no. 1, pp. 173-180, March 2011.
[16] S. Weckx, C. Gonzalez, and J. Driesen, "Combined central and local active and reactive power control of pv inverters," IEEE Trans. Sustain. Energy, vol. 5, no. 3, pp. 776-784, July 2014.
[17] H. S. Bidgoli and T. Van Cutsem, "Combined local and centralized voltage control in active distribution networks," IEEE Trans. Power Syst., vol. 33, no. 2, pp. 1374-1384, March 2018.
[18] P. Cortez, Modern Optimization with R. Springer International Publishing, 2014.
[19] S. Frank and S. Rebennack, "An introduction to optimal power flow: Theory, formulation, and examples," IIE Transactions, vol. 48, no. 12, pp. 1172-1197, 2016.
[20] R. C. Dugan, M. F. McGranaghan, S. Santoso, and H. W. Beaty, Electrical Power Systems Quality, Third Edition. McGraw-Hill Professional, 2012.
[21] Y. Gonzalez-Fernandez and M. Soto, "copulaedas: An r package for estimation of distribution algorithms based on copulas," J. Stat. Softw., vol. 58, no. 9, pp. 1-34, 2014.
[22] R. B. Nelsen, An Introduction to Copulas (Springer Series in Statistics). Berlin, Heidelberg: Springer-Verlag, 2006.
[23] J. Widén and J. Munkhammar, "Spatio-temporal downscaling of hourly solar irradiance data using gaussian copulas," in 2019 IEEE 46th Photovoltaic Specialist Conference (PVSC), June 2019.
[24] "The IEEE 123 node test feeder, 1992," https://cmte.ieee.org/ pes-testfeeders/resources/, accessed: 2021-06-09.
[25] S. Weckx and J. Driesen, "Load balancing with ev chargers and pv inverters in unbalanced distribution grids," IEEE Trans. Sustain. Energy, vol. 6, no. 2, pp. 635-643, 2015.
[26] M. Sengupta and A. Andreas, "Oahu solar measurement grid (1-year archive): 1-second solar irradiance; oahu, hawaii (data)," 2010, data retrieved from: https://midcdmx.nrel.gov/oahu_archive/.
[27] Interconnection and Interoperability of Distributed Energy Resources with Associated Electric Power Systems Interfaces, IEEE, New York, NY, 2018.
[28] H. Bouchekara, "Optimal power flow using black-hole-based optimization approach," Appl. Soft Comput., vol. 24, pp. 879 - 888, 2014.
[29] "Optimal power flow version 1," https: /ise.mathworks.com/matlabcentral/fileexchange/ 72293-optimal-power-flow-opf-problem-version-1, accessed: 2021-0510 .