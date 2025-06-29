# Reliability evaluation of a composite power system in the presence of renewable generations 

Mohsen Firouzi, Abouzar Samimi *, Abolfazl Salami<br>Department of Electrical Engineering, Arak University of Technology, Arak, Iran

## A R T I C L E I N F O

Keywords:
Composite power system
Reliability
Uncertainty
Renewable energy resources
Non-sequential Monte Carlo simulation
Estimation of distribution algorithm

## A B S T R A C T

Power system reliability evaluation plays a vital role in the planning and operation studies by reflecting the system safety level. In this paper, a combination of a non-sequential Monte Carlo simulation (MCS)-based model and an improved Estimation of Distribution Algorithm (EDA) is exploited for evaluating the reliability of the composite power systems considering variability and uncertainty of wind farms (WFs) and Photovoltaic (PV) units. Variability of these resources is defined as the random fluctuation of wind speed and solar irradiation caused by changes in the atmosphere, while their uncertainty results from output power forecast errors. In the proposed model, the states of traditional generating units, transmission lines, WFs, and PV units are constructed using non-sequential MCS. These states can be achieved based on the component failure probability for dispatchable traditional generators and transmission lines along with the Probability Distribution Functions (PDFs) of renewable generations. To enhance the computational efficiency of the MCS in the sampling step, the improved EDA upgraded with the Population-Based Incremental Learning (PBIL) algorithm is employed. The proposed mathematical model for reliability evaluation of composite power system is applied to the IEEE RTS 24bus system, and numerical studies are performed under several case studies. The simulation results confirm the proficiency of the proposed method to improve the computational efficiency, while the high accuracy of reliability evaluation of the composite power system is attained.

## 1. Introduction

### 1.1. Background and concepts

Reliability evaluation plays a vital role in the planning and operation studies of the power system by reflecting the system safety level. Evaluating the generation and transmission systems' ability to meet sufficient electrical energy to the load demand points is defined as the reliability of a composite power system [1]. Mainly, assessing the reliability of a composite power system consists of three primary stages: constructing the power system modes or states, evaluating the consequences of the chosen modes, and computing the risk indices of the composite power system [2]. A system mode or state is a combination of all network component states. In order to evaluate Essentially, two situations of success or failure are supposed for conventional generators and transmission lines. Two main approaches can be employed to select the system modes that consist of analytical enumeration and Monte Carlo Simulation (MCS). Although the analytical enumeration technique can yield accurate reliability and risk indices by explicitly determining
all possible modes of the power system, it is rarely utilized by the power system operators and planners in evaluating the reliability of composite power systems specially with a more significant number of dispersed generations. Consequently, it is preferable to use MCS for reliability evaluation of large-scale composite power systems. The computational complexity grows significantly with the expansion of the power system scale and the presence of renewable generations [3]. As a result, the MCS is also utilized for reliability assessment of the composite power systems including renewable generations and considering existing uncertainties. There is no much dependency between the size of the power system and the MCS sampling technique. As one of various applications of the MCS method in bulk power systems, a flexible and robust tool based on the MCS is proposed in [3] to evaluate the spinning reserve requirements of generating systems considering the loss of load risk arising from failures in the generation and transmission network for bulk power systems. For this purpose, an unbiased estimator using importance sampling is employed and the set of optimal parameters is achieved based on a cross-entropy method.

The MCS tool is categorized into sequential and non-sequential simulations. The sequential technique creates the system modes based

[^0]
[^0]:    * Corresponding author.

    E-mail addresses: a.samimi@arakut.ac.ir, abouzarsamimi@iust.ac.ir (A. Samimi).

on the sequence of events. In contrast, in the non-sequential simulation framework, the composite power system modes are constructed in a random manner. To improve the MCS for evaluating power system reliability, significant works have been performed. The present improvement techniques in MCS are mainly directed towards sampling power system states and state evaluation.

### 1.2. Literature review

To implement the prominences of the computational efficiency of non-sequential MCS as well as the precision of sequential simulation technique, authors of Ref [4]. proposed a pseudo-sequential simulation based on the non-sequential MCS along with the chronological simulation of only the sub-sequences associated with failed states in order to compute total system interruption costs in composite power systems. In [5], a new methodology, namely pseudo-chronological simulation was presented to evaluate loss of load cost for composite generation and transmission systems considering time varying loads. The proposed method retains the computational efficiency of non-sequential MCS and the ability to model chronological load curves in the sequential simulation. Different types of variance reduction approach, such as importance sampling [6], subset simulation [7], Latin Hypercube Sampling (LHS) [8], and cross-entropy methods [9], have been employed to enhance the computational efficiency of MCS. These approaches can accelerate the computational process of choosing the power system states of the reliability assessment. In [10], an accelerating technique based on the non-sequential MCS, which avoids the contingency examination for the repetitive power system states, has been used to deal with the first stage of system reliability evaluation.

Reliability assessment of the power systems involves various issues, and many approaches have been introduced and employed, each of which analyses the power system reliability from a particular point of view. They can be categorized into two main clusters. In the first one, the power system is managed as a static system in which the adequacy index is taken into account as a criterion of the system reliability. While, in the second one, the power grid is considered as a dynamic system where the security issue is analyzed as a reliability index of the dynamic system [11]. In [12], the application of energy storage systems (ESS) in assessing reliability of power systems has been investigated based on the pseudo analytical sampling method. In [13], a contingency set partition-based impact transfer method consisting of two stages is proposed for the reliability assessment of composite generation and transmission systems. First, a contingency set partition approach is proposed
to combine the merits of the contingency enumeration method and the MCS method to obtain accurate reliability indices with higher efficiency. In the second stage, an impact transfer method is introduced to further improve the computational efficiency. The impact transfer reduces the impact variance of higher order contingencies and thus improves the sampling efficiency of the technique proposed in the first stage. In [14], a reliability analysis method using a multi-state decision diagram has been established for a multi-state non-repairable power generation system with warm standby considering the chronological characteristics of warm standby units before and after the activation. Based on the proposed method, the optimal activation sequence of the generating units is formulated in such a way that the maximal system reliability is achieved.

Recently, RESs such as wind and photovoltaic (PV) units have been developed as emission-free and efficient options in power systems. However, the intermittent nature of RESs and stochastic output powers of these resources have prevented the high integration rate of these resources into power systems. Consequently, they create challenges for the power system reliability assessment [15]. Therefore, to assess the impact of RES generations on power system reliability is gaining more importance. Moreover, employing the analytical models of wind farms (WF) and PV generation units considering their output power correlation has many obstacles. In power system studies, there are three common uncertainty handling methods as follows: probabilistic methods, fuzzy methods, and combined methods which are a combination of probabilistic and fuzzy approaches. In [16], a probabilistic interval prediction model has been outlined for reliability assessment of power systems considering wind power uncertainty. The wind power interval prediction is modeled using an autoregressive integrated moving average (ARIMA) combined with the Markov Chain Monte Carlo (MCMC)-based Bayesian estimation method. To better forecast the energy production of onshore WFs, a comprehensive investigation has been conducted in [17] using a hybrid-based approach combining the Jensen wake theory and a fault tree model of stochastic dependability. As reported in this reference, the Jensen wake theory can yield a precise prediction of the weekly energy generation of a WT. By contrast, the fault tree model of a WT is able to capture the availability of the wind generators. Authors of Ref [18]. have presented a modeling technique based on both the deterministic and the stochastic nature of PV power plant using the Stochastic Hybrid Fault Tree Automaton (SHyFTA) aiming at providing the knowledge-base to design a dynamic reliability model of a renewable power plant. The SHyFTA is able to provide a more accurate system modeling by integrating traditional deterministic approaches and a stochastic model of the system including the randomness of the primary resource and the fault and performance degradation states [18]. In [19], the effects of PV resources has been analyzed on the system reliability based on a probabilistic model with transmission system contingencies and possible cascading failures. Authors of Ref [20]. have used the machine learning methods to evaluate the reliability of power systems using the MCS. In [21], a multi-state decision diagram technique have been proposed for the reliability evaluation of power systems with multi-state units and transmission lines. In [22], a procedure-based DC power flow model is presented for the efficient assessment of component importance and network reliability in power transmission grids with wind hazards. Authors of Ref [23]. investigate comprehensive models for wind and compressed air energy storage operating strategies in a wind integrated power network to quantify the potential benefits of compressed air energy storages in terms of their contributions to system reliability, efficiency, and environmental objectives. In [24], a wind generation-based power system consisting of two wind farms is modeled and analyzed from the reliability viewpoint considering the dependence between wind speeds at two sites. To efficiently assess the reliability of the composite power systems with wind energy integrated, an improved two stage cross entropy-based importance sampling is proposed in [25]. Particularly, the used method in this reference takes the correlation between wind speed and load into account and models multi-state

![img-0.jpeg](img-0.jpeg)

Fig. 1. Discretized wind speed PDF.
random variables with multinomial distribution. In [26], a MCS-based decision support system framework is implemented to enable fast calculation of loss of load expectation (LOLE) as a risk measure in a power system consisting various sources of renewable and conventional power. In order to enable wind energy to be distributed to consumers, dynamic thermal rating (DTR) system is utilized to alleviate the congestion of power system. In line with purpose, the authors of Ref [27]. have presented the reliability modeling of battery energy storage system along with the DTR technologies for the first time. The authors of [28] have presented the conception of a framework for the modeling and the simulation of the SHyFTA which is able to combine dynamic fault tree with the deterministic model of the system process. The proposed framework in this reference is realized based on a hybrid Discrete Event-Time Driven iteration engine at the base of the MCS.

A large amount of uncertainty entered into power systems may affect the system vulnerability to cascading failures. To cascade a failure simulation model, authors of Ref [29]. have outlined a coupled extreme frame weather event. Then, a common sequential MCS framework has been utilized to compute extreme weather events affecting energy transmission. Nevertheless, many works in the literature have addressed the effects of wind power generations on power system reliability, and few researches have explored the variability and uncertainty of wind power generation [30].

With the development of smart grid infrastructure, a hierarchical model comprising a layered fault tree and continuous-time Markov chains is introduced in [31] to model a smart grid system aiming to find the weak parts of the system and to improve the system design. In [32], the effect of small-size energy storage operating along with the local PV-based microgrids in smart grids has been examined to improve reliability performance and attain financial benefits for the system operator and their owners.

### 1.3. Novelty and contributions of this paper

While advantages of using RES can be readily seen, their actual impact on power system reliability is not yet precisely investigated. Therefore, we develop a new method to quantify the effect of adding PV units and WFs on the composite power system reliability. In this paper, integration of the non-sequential MCS-based model and the improved Estimation of Distribution Algorithm (EDA) is exploited for evaluating the reliability of the composite power systems with WFs and PV units. In the proposed model, first, the states of traditional generators, transmission lines, WFs, and PV cells are composed using non-sequential MCS. These states can be achieved based on the component failure probability for conventional generators and transmission lines besides
the PDFs of wind speed and solar irradiation for WFs and PV units, respectively. Furthermore, the uncertainty sets have been exploited to estimate the PDF parameters that account for the uncertainty and variability of renewables. The improved EDA based on the populationbased incremental learning (PBIL) algorithm is implemented to improve the computational efficiency of the MCS in the sampling step. To accelerate the process of states' evaluation, the technique of integrating similar states is utilized. By storing the same states and avoiding recalculating them, the number of states that should be examined reduces significantly. Moreover, the required load curtailment in the reliability evaluation stage has been calculated based on the virtual generator concept to reduce computational process time.

In Ref [10]. which is investigated the reliability assessment of composite power system, only wind farms (WFs) are considered in the power system and the effects of PVs are not evaluated in the reliability studies. Moreover, the EDA technique is not implemented in the proposed model. Another striking point is that in this reference, the uncertainty sets have not been exploited to estimate the PDF parameters that account for the uncertainty and variability of renewables. In fact, the uncertainty of wind generations is modeled based on a multistate probability table.

In [33], in which the computational efficiency of traditional Monte Carlo simulation (MCS) in the composite power system reliability evaluation is improved based on the improved EDA and double cross-linked list, only conventional generators are considered in the power system and the renewable generations, which play a vital role in the modern power systems, are disregarded. Moreover, the techniques of integrating similar states and the virtual generator concept are not utilized.

The main contributions of this paper are organized as follows.
(i). In this study, a new method for evaluating the reliability of composite power systems is presented using a combination of a nonsequential MCS-based model and an improved EDA.
(ii). The virtual generator concept is employed to determine the required load curtailment in the evaluation stage.
(iii). Variability and uncertainty of WFs and PV sources are accurately modeled based on uncertainty sets.
(iv). The rank correlation coefficient method is used to generate random numbers for WFs and PV systems.

### 1.4. Paper organization

The remaining parts of the paper are organized as follows:
In Section 2, the probabilistic model of renewable energy resources is explained Section 3. describes the proposed model for reliability

![img-2.jpeg](img-2.jpeg)

Fig. 2. The PDF for solar irradiation.
evaluation of the composite power system. Simulation results and their analysis are presented in Section 4. Finally, the paper is concluded in Section 5.

## 2. Probabilistic modeling for renewable energy resources

### 2.1. Wind generation

The output power of the wind generating unit depends on wind speed. As reported in the literature [34], the wind speed characteristic at a particular location follows the Weibull PDF. Therefore, the PDF of the wind speed based on the Weibull distribution is given as follows:
$f(v)=(k / c)(v / c)^{|k-1|} e^{-(v / c)^{k}}, 0<v<\infty$
Where, $v, k$, and $c$ are wind speed, shape factor, and scale factor, respectively. For simplicity, the wind speed distribution is normalized by the average speed in the Weibull distribution. The PDF of wind speed can be divided into some specific intervals depending on the desired accuracy. The probability of each interval is determined by the numerical integral method. In this paper, wind speed distribution is divided into five equal intervals, as exhibited in Fig. 1.

According to the wind speed, the output power of a wind generating
unit is computed using the speed-to-power conversion function as follows [35]:

$$
\begin{aligned}
& 0, \text { for } v\left(v_{i} \text { and } v\right) v_{o} \\
& \omega_{v}, \text { for } v_{v} \leq v \leq v_{o}
\end{aligned}
$$

Where, $P_{W}, P_{v}, v_{o}, v_{v}$ and $v_{o}$ are WT output power, nominal power, cutin speed, rated speed, and cut-out speed, respectively.

### 2.2. PV system

With ever-increasing PV technology, more large-scale PV units are being integrated into power systems where low-cost land and abundant solar energy are readily available. The output power of PV units is a function of uncertain parameters including ambient temperature and solar irradiance. Due to extreme variations of ambient temperature and solar irradiance throughout the day, the active power of PV panels has intense fluctuations in spite of many advances in the maximum power point tracing (MPPT) techniques. As reported in the literature [36,37], at a particular location, the distribution of hourly irradiance is generally in accordance with a bimodal distribution, which can be expressed as a linear combination of two unimodal distribution functions. A Beta PDF
![img-2.jpeg](img-2.jpeg)

Fig. 3. Variations of average wind speed and its standard deviation based on the measurements [30].

![img-3.jpeg](img-3.jpeg)

Fig. 4. The relationship between the amount of uncertainty and the average wind speed.
has been applied for each unimodal. Accordingly, in this paper, the double Weibull PDF has been implemented to model the uncertainty of the solar irradiance as follows [38]:
$\sigma=0.231+0.197 \mu$
To clarify this issue, the relationship between the amount of uncer-

$$
\begin{aligned}
& f(g)=\omega\left(k_{1} / c_{1}\right)\left(g / c_{1}\right)^{(k_{1}-1)} e^{-\left(g / c_{1}\right)^{2} t}+(1-\omega)\left(k_{2} / c_{2}\right)\left(g / c_{2}\right)^{(k_{2}-1)} e^{-\left(g / c_{2}\right)^{2} t}, 0<g<\infty \\
& \text { Where, } \mathrm{g} \text { represents the solar irradiance in } \mathrm{kWh} / \mathrm{m}^{2}, \omega \text { is the } \\
& \text { weighting factor, } k_{1} \text { and } k_{2} \text { are the shape factors and } c_{1} \text { and } c_{2} \text { indicate } \\
& \text { the scale factors. In a similar way, the solar irradiation PDF can also be } \\
& \text { discretized. As depicted in Fig. 2, a 5-discrete interval irradiation PDF is } \\
& \text { considered in this study [39]. Therefore, once the considered PDF is } \\
& \text { generated for a specific period, the produced power of a PV unit during } \\
& \text { the different intervals is given by the following equation [38]: } \\
& P_{p r}=\eta^{P V} S^{P V} g
\end{aligned}
$$

Where, $P_{p r}$ is the output power of PV, $\eta^{P V}$ and $\mathrm{S}^{\mathrm{PV}}$ indicate, respectively, efficiency and the total area of PV panels.

### 2.3. Improvement of uncertainty modeling of renewable resources using uncertainty sets

Wind power generation creates variability and uncertainty in the operation of the power system. Variability of wind generation is defined as the random fluctuation of wind speed caused by changes in the atmosphere, while its uncertainty results from wind forecast errors. Here, the uncertainty sets have been extracted to estimate PDF parameters that account for wind power generation uncertainty and variability. To represent the uncertainties of wind sources, the standard deviation ( $\sigma$ ) and to demonstrate the forecasted value of the wind production, which implies the variability of wind generation, $(\mu)$ have been used. The relationship between $\sigma$ and $\mu$ can be attained based on the measurement and experimental studies as displayed in Fig. 3 for wind speed [30]. Generally, these experiments are performed by predicting the hourly average wind speed for a one-year period. It can be seen in Fig. 3 that increasing the mean value of wind speed also leads to an increase in standard deviation $\sigma$. Whenever, the mean value of wind is high, the amount of uncertainty is also high, and unlike most previous studies, fixed standard deviation values for wind generation should not be adopted. Therefore, in the MCS method to generate wind power scenarios, more scenarios are needed to be generated during the hours with high mean values for RES units due to the high uncertainty. On the other hand, for hours with the small mean values, the uncertainties of wind speed can be modeled with fewer scenarios. The linear relationship between $\sigma$ and $\mu$ for wind is considered as given in Eq. (5). Accurate modeling of wind power generations in the states of the composite power systems will lead to more precise reliability assessment results.

$$
\sigma=0.231+0.197 \mu
$$

To clarify this issue, the relationship between the amount of uncer-

$$
\begin{aligned}
& f(g)=\omega\left(k_{1} / c_{1}\right)\left(g / c_{1}\right)^{(k_{1}-1)} e^{-\left(g / c_{1}\right)^{2} t}+(1-\omega)\left(k_{2} / c_{2}\right)\left(g / c_{2}\right)^{(k_{2}-1)} e^{-\left(g / c_{2}\right)^{2} t}, 0<g<\infty
\end{aligned}
$$

tainty and the average wind speed is shown in Fig. 4. Based on the explanations provided for wind resources, a similar relationship between the amount of uncertainty and the average solar irradiation can be extracted to model the uncertainty of PV resources accurately. In this way, the PDF curves are examined separately for each hour of a day and become sharper or broader depending on the high or low forecast average output. A broader pdf means more inaccurate forecasted output power and accordingly, more uncertainty. In contrast, a sharper pdf indicates a more accurate production forecast and less uncertainty.

## 3. Proposed model for composite power system reliability evaluation

In this section, a reliability evaluation model for composite power systems in the presence of WFs and PV units will be performed. Generally, one or two reliability indices have been calculated in the relevant references. However, in this paper, four important indices which consist of (i) Loss of Load Expectation (LOLE), (ii) Expected Energy Not Supplied (EENS), iii) Average Energy Not Supplied (AENS), and iv) Probability of Load Curtailment (PLC) are computed based on the proposed model.

In the following, the details of the proposed model are provided.

### 3.1. Generating states of composite power systems

The states of a composite power system are extracted from all component states using the non-sequential MCS technique. Essentially, two situations of success or failure are supposed for conventional generators and transmission lines, and there is no relationship between their failures. In this way, each component situation of generators and lines can be represented by creating a set of distributed uniformly random numbers between [0 and 1]. Thus, the state of component ith, i.e., $\mathrm{S}_{\mathrm{i}}$, is expressed based on the failure probability of component $\mathrm{FP}_{\mathrm{i}}$ and the generated random number $U_{i}$ using the following equation:
$S_{i}=1 \begin{aligned} & 0 \text { (Failure), } 0 \leq U_{i}<F P_{i} \\ & 1 \text { (Success), } F P_{i} \leq U_{i} \leq 1\end{aligned}$
To be consistent with the non-sequential method, the WF and PV are taken into consideration as generation systems with multi-state output power. However, in the reliability assessment, there are two issues have to be addressed. First, owing to the integration of renewable generations into the power system at different buses, instead of the probability table of produced power of all RESs, the multi-state probability table of each

![img-4.jpeg](img-4.jpeg)

Fig. 5. Flowchart of generating, transforming, and integrating system states based on the non-sequential MCS.

RES has to be employed for composite power system reliability. Fortunately, this issue is solved by implementing an apportioning technique to the output power series of each renewable [40]. Second, it is worth mentioning that there is a correlation between the output power of the WFs (and PVs) in close regions [41]. Accordingly, the state sampling of each RES cannot be achieved using only independent random numbers. The two main criterions to determine the dependence among random numbers in power system applications are Pearson correlation and rank
correlation coefficients [42]. In this paper, the rank correlation coefficient method is used to generate random numbers of WFs and PV systems. The detailed process of this method has been given in [10]. Assuming that $X_{i}$ is a random number between [ 0 and 1], that is created by specified linear correlation coefficient-based Copula method, the output power state of the RES $i$ th can be determined as follows:

![img-5.jpeg](img-5.jpeg)

Fig. 6. Dividing the state space into two clusters [33].

$$
\begin{gathered}
00 \leq X_{i}<p_{R E S(1)} \\
1, p_{R E S(1)} \leq X_{i}<\left(p_{R E S(1)}+p_{R E S(2)}\right) \\
s_{i}=\left\{\begin{array}{c}
k, \sum_{j=1}^{k} p_{R E S(j)} \leq X_{i}<\sum_{j=1}^{k+1} p_{R E S(j)} \\
n_{v q}-1, \sum_{j=1}^{k+1} p_{R E S(j)} \leq X_{i} \leq 1
\end{array}\right.
\end{gathered}
$$

Where, $s_{i}$ indicates the state number of RES $i$ th, $n_{v q}$ is the total number of equivalent states of a RES. $p_{\text {RES }(j)}$ indicates the probability of interval $j$ th of RES $i$ th.

### 3.2. Construction of system states based on a binary array

To calculate the reliability indices, it is necessary to analyze each of the considered states of the power system, including the states of the conventional generators, transmission lines, WFs, and PV systems, along with obtaining the amount of load curtailment for each state. As mentioned, conventional generators and lines are represented as a twostate model (success and failure), and renewable sources are introduced as multi-state generation units. Therefore, system states can be extracted by applying a combination of all system component states. Here, a binary array is employed to represent the operation status of the system. This binary array arrangement can be created as follows: For two-state components, one array comprising 0 or 1 is applied to determine their operation states, in which 0 indicates "out of service," and 1 means that the component is "in service." For a RES which is demonstrated by a multi-state model, several array elements, including 0 and 1 , are provided to demonstrate its output power for each state. A RES unit is introduced as a generation unit with $n_{v q}$ states represented by the $n_{r}$ array elements. The value of $n_{r}$ is given as follows:
$n_{r}=\operatorname{ceil}\left(\log _{2} n_{v q}\right)$
Where, the function "ceil" rounds up a variable to the nearest greater integer.

To generate a system state array, the two-state arrays of conventional units and lines, should be integrated with the binary string arrays of the RES. Assuming $n_{l}$ lines, $n_{g}$ traditional generators, and $n_{\text {RES }}$ WF and PV systems as RES units, the binary arrays of the system states consist of the following elements:
(1). The first $n_{l}$ cells in the state array signify the states of the lines, in which " 1 " indicates the corresponding line is "in service", while " 0 " denotes it is "out of service".
(2). The next $n_{g}$ cells characterize the state of the conventional generators, in which " 1 " indicates the corresponding generator is "in service", while " 0 " denotes it is "out of service".
(3). Assuming that each output power state of WF and PV system is expressed by $n_{r}$ binary numbers. Therefore, the last $n_{r} \times n_{\text {RES }}$ cells in the
state array arrangement of the system demonstrate the output power states of $n_{\text {RES }}$ RES units. The value of $n_{r}$ is determined based on the equivalent number $\left(n_{v q}\right)$ of the RES states.

### 3.3. Transforming and integrating similar states of the system

After generating required system states by the non-sequential MCS as the binary arrays, they are compared and identified based on an encoding conversion method. In line with this purpose, each sampled binary array representing the power system's state is transformed to its comparable decimal number to demonstrate a special system status. Accordingly, the two power system states are effortlessly compared using their equivalent decimal numbers instead of examining their corresponding large binary arrays. To reduce the number of states considerably, the identical decimal numbers determining one special system status should be incorporated and declared as an identical system state. As a result, for each specific system state, the corresponding binary array, the equivalent decimal number, and its number of occurrence times need to be saved [10] Fig. 5. describes the flowchart of generating and transforming system states along with integrating the identical states.

### 3.4. Trimming down the state space based on the EDA

To achieve a higher computational efficiency of MCS in the sampling step, the improved EDA based on the PBIL algorithm is applied [33]. This algorithm aims to accelerate the sampling stage executed by the non-sequential MCS method. The probabilities vector of the state space will be updated based on the distribution characteristics of the best samples in the last generation of the population.

To increase the computational efficiency of the reliability evaluation stage, the state space should be pruned. In each system state, the generation capacity based on the created array will be compared with the total load demand. If for a particular state, loss of load occurs, this state enters the evaluation list. As a result, many normal states are excluded from the calculations. They will be counted only for obtaining the states' probability. For a better understanding, Fig. 6 shows this separation.

As depicted in Fig. 6, the original state space is separated into two clusters of N-St and U-St, in which cluster N-St includes most of the normal states, while cluster U-St consists of most of the loss-of-load states along with a small part of normal states.

It is supposed that the number of samples in the primary set is N and the Loss of Load Probability (LOLP) is defined as $v$, the LOLP variance coefficient $\eta$ is obtained as follows:
$\eta=\frac{1}{v} \sqrt{\frac{\ln (1-v)}{N}}$
If the percentage of cluster U-St in the primary state space is defined by $\varepsilon$ and the sampling procedure is accomplished in cluster U-St, the LOLP in this cluster can be computed as follows:

![img-6.jpeg](img-6.jpeg)

Fig. 7. Flowchart of calculating reliability indices.
$\bar{u}^{\prime}=\frac{u}{\varepsilon}$
According to Eq. (9), variance coefficient $\bar{u}^{\prime}$ related to the LOLP in cluster U-St is given as:
$\bar{\eta}^{\prime}=\frac{1}{\bar{u}^{\prime}} \sqrt{\frac{\bar{u}^{\prime}\left(1-\bar{u}^{\prime}\right)}{N^{\prime}}}$
Where, $N^{\prime}$ represents the sampling size in the U-St cluster. Since the convergence of variance coefficients $\eta$ and $\bar{\eta}^{\prime}$ is identical, then:
$\frac{N^{\prime}}{N}=\varepsilon \frac{1-(p / \varepsilon)}{1-p}$
As a result, with the same convergence accuracy, the sampling size
$N^{\prime}$ required for evaluating of the reliability in the U-St cluster is far less than the number of samples in the primary set N [33]. Details of the improved EDA along with the steps of trimming down the state space are given in Section 3.1.2 in [33].

# 3.5. Calculation of reliability indices 

Probability of load curtailments (PLC), loss of load expectation (LOLE), expected energy not supplied (EENS), and average energy not supplied (AENS) have been calculated as four commonly reliability indices, and they are formulated as follows:
$P L C=\sum_{i=1}^{N_{m}}\left(I_{i} \times \frac{\alpha_{i} \cdot}{N 3}\right)$

![img-7.jpeg](img-7.jpeg)

Fig. 8. The overall framework for the proposed model.
$I_{i}=\left\{\begin{array}{l}0, \\ 1, \\ C S_{i} \neq 0\end{array}\right.$
Where, $N S$ and $N_{m}$ denote the total number of initial states of the power system and the number of decreased states after integrating similar states and utilizing EDA, respectively. $n s_{i}$ is the number of occurrence times of state $i$ th. $I_{i}$ is a binary variable representing the load curtailment of system state $i$ th based on the value of load curtailment $C S_{i}$ in MW.
$E E N S=\sum_{i=1}^{N_{m}} C S_{i} \times \frac{n s_{i}}{N S} \times D u_{i}$
Where, $\boldsymbol{D} \boldsymbol{u}_{i}$ is the time duration of the load curtailment of system state $i$ th
$L O L E=\sum_{i=1}^{N_{m}} C S_{i} \times \frac{n s_{i}}{N S}$
$A E N S=\sum_{i=1}^{N_{m}}\left(C S_{i} \times \frac{n s_{i}}{N S} \times D u_{i}\right) / N$
Where, $\boldsymbol{N}$ is the total number of consumers.
To calculate the required load curtailment in the reliability evaluation stage, the virtual generator concept is applied to improve computational efficiency. For this purpose, a generator with a high operational cost is considered at each bus with a capacity equivalent to the load connected to that bus. This idea leads to operating this virtual unit if the power system needs to load curtailment in a particular state. The produced power of this virtual generator is equivalent to its bus load curtailment. This method significantly increases the computational
speed of required load shedding in each state of the system. Because, existing software solves the problem of optimal power flow (OPF) very quickly, while load shedding is an optimization problem that requires modeling and solving based on the optimization techniques Fig. 7. shows the flowchart for calculating reliability indices. The overall framework for the reliability evaluation based on the proposed method presented in Sections 2 and 3, is shown in Fig. 8.

## 4. Simulation results

The proposed mathematical model for reliability evaluation of the composite power system is applied to the modified IEEE RTS 24-bus system [10] and numerical studies are performed under several case studies. The EDA technique is applied to the state space for pruning the state space generated by non-sequential MCS. Accordingly, the reliability evaluation method is performed with a smaller number of samples. The WF and PV systems are connected to the network and the reliability indices are evaluated according to the proposed model. Each WF includes 100 wind turbines (WTs) with a capacity of 2 MW and each PV farm consists of 200,000 panels model with a capacity of $1 \mathrm{~kW} / \mathrm{m}^{2}$ [43]. The FOR of each WT and PV is $5 \%$ [10].

The IEEE RTS 24-bus system has 38 lines and 31 conventional generators. Therefore, a 69-bit binary array is needed to determine the status of the entire system, and consequently, there are $2^{69}$ possible states for this system. It is almost impossible to investigate and evaluate all of these states. However, if fewer random states are generated and analyzed, a high approximation may occur in the evaluations. Fortunately, system states with more than two simultaneous failures are very improbable. Accordingly, by considering single and maximum couple failure modes in transmission lines and conventional generators, an

Table 1
A binary array of a system state.

Table 2
SRCC for wind speed (solar irradiation) and the corresponding output powers.
Table 3
State probability values of output powers of dependent WFs (PVs) 1 and 2 [10].
extensive state space pruning of the possible states can be covered. In other words, the total number of states that sufficiently tackle the state space pruning is $1+\binom{69}{1}+\binom{69}{2}=2416$ states. However, it is still almost impossible to investigate all of these states and compute the reliability indices.

Based on Eqs. (6)-(8), a binary array representing a state of the test system with two WFs and two PVs is shown in Table 1. Combination the non-sequential MCS and the EDA provides the reliability assessment of the composite power system in an acceptable time by selecting states that cover most of the high probability system states. To further accelerate the simulation, encoding and integrating the similar system states are performed by transforming the binary arrays of generated random states to their equivalent decimal numbers.

To adapt the uncertainties of wind and solar generations with the proposed MCS model, Spearman's Rank Correlation Coefficient (SRCC) is used. The SRCCs of the wind speed and solar irradiation, along with their corresponding SRCCs for output powers of two WFs and two PVs have been reported in Table 2.

The probabilities of the multi-state generation capacity of the RES units based on three different SRCCs $0.2,0.5$, and 0.9 are reported in Table 3.

SRCCs have been implemented to model the correlation between renewable generations. Due to the linear relationship in power conversion functions for both WF and PV units, the correlation coefficients between the output powers of these resources are the same as the corresponding correlation coefficients of wind speeds and solar irradiation, respectively.

Here, five case studies are defined and analyzed as follows:
Case 1: Two WFs are located at buses 1 and 2 of the RTS 24-bus system.

Table 4
Comparison of computational efficiency of two scenarios in Case 1.

Table 5
Reliability indices in Case 1.

Case 2: A WF with a PV farm are considered in both buses 1 and 2 of the network, simultaneously.
Case 3: Renewable resources modeling based on the uncertainty sets is applied to Case 2.
Case 4: In this case study, the EDA is applied to Case 3 to improve computational efficiency.
Case 5: Two PV systems are located at buses 1 and 2 of the RTS 24bus system, and the EDA and the uncertainty modeling of renewable resources are utilized.

Case 1: The wind speed correlation coefficient for two WFs in this study is considered as 0.5 . Also, the criterion for stopping non-sequential MCS in the sampling stage is the variance of reliability indices. In this way, if the variance value reaches an acceptable convergence, further sampling will not be required. In [10], it has been proved that the variance coefficient of the EENS index has the lowest convergence rate among the other risk indices. Thus, the variance coefficient for the EENS index can be taken as the convergence criterion, which is considered $2 \%$ in this study. By performing the simulation procedure, the number of samples examined for the convergence criterion becomes 93,359. To evaluate the computation time of the proposed method, two scenarios are employed as follows:

Scenario 1: By utilizing transforming the binary array to its equivalent decimal number without integrating similar states.

Scenario 2: By utilizing transforming the binary array to its equivalent decimal number and considering integrating similar states.

The computational efficiency of these scenarios in Case 1 has been reported in Table 4.

By applying the state integration method, only $28.5 \%$ of the total states should be examined to achieve the desired accuracy of the algorithm. Thus, the computational time in this scenario is less than the time required in the first scenario. Also, due to the use of the concept of the virtual generator described in Section 3 in load flow analysis, the computation time compared to the Ref [10]. has been considerably reduced from 693 to 72 s in the first scenario and from 316 to 43 s in the second scenario, respectively. Moreover, the number of optimal load flow iterations in the first scenario is 100 times, and in the second scenario is 35 times. The values of the four reliability indices are reported in Table 5.

Given that the integrating states technique in Scenario 2 significantly

Table 6
Results of the reliability evaluation in Case 2.

reduces the computational burden, Scenario 1 will not be developed in subsequent case studies.

Case 2: A WF and a PV are connected to bus 1, and other WF and PV are also connected to bus 2, simultaneously. In this case study, all four reliability indices have been computed and the obtained results are shown in Table 6. It is worth mentioning that the integrating states technique and the idea of the virtual generator have been considered in this case and subsequent case studies. The number of optimal load flow iterations in the second case study is 90 times.

In this case, the convergence criterion is obtained by sampling 76,839 states of the system. In fact, with the presence of PV sources along with WFs, the number of samples has decreased, which indicates that the uncertainty of PV sources is less than wind sources. In the subsequent case studies, the effect of the uncertainty of RES on the composite power system reliability has been accurately investigated.

Case 3: In this case study, the uncertainty modeling presented in Section 2 for RES are applied to Case 2, and the reliability indices have been computed. Here, the effect of the accurate uncertainties modeling of RES on the reliability has been appropriately investigated. The number of generated scenarios for wind and PV units depends on the uncertainty related to their production estimations. Also, the duration curves of the average wind speed and solar irradiation values have been utilized for reliability assessment. Depending on the values of the average wind speed and solar irradiation, stochastic scenarios and their capacity probability tables are created to extract standard deviation $\sigma$ based on Eq. (5). As indicated in Fig. 9, these curves are divided into ten sections according to the percentage of the output power of renewables and the percentage of days in a year, in which the amount of load, wind and PV generations in each section is constant. According to ten sections for wind and PV generations, we have 100 reliability evaluation modes. Then, the proposed method is applied to each section separately and the obtained results are combined. The results of Case 3 are shown in Table 8. This procedure aims to increase the accuracy of the reliability evaluation in the presence of renewable sources by developing a relationship between the uncertainties of production estimation and the accuracy of wind speed and solar irradiation predictions. Similar to the
previous case studies, the load is fixed throughout the year and is considered as the peak load.

The results in Table 7 show that the actual value of the reliability indices is slightly higher than the values calculated in Case 2. In other words, assessing reliability without considering the relationship between the amount of output power uncertainty and the range of renewable sources' accuracy leads to inaccurate results. If the average values of renewables uncertainty are more significant than the actual values and are considered the same for all times, the calculated reliability indices will be worse than reality. On the contrary, the values of the calculated reliability indices are less than the actual values and incorrectly indicate better reliability (Case 2). In Case 3, by sampling 7,982,662 samples, the convergence criterion has been achieved. Since, for each 100 modes of the renewable based-system, a particular problem has been evaluated; the total samples of 100 modes are equal to $7,982,662$. Also, the number of optimal power flow iterations in this study is 31,086 times. As can be seen, by improving the accuracy of uncertainty modeling, the computation time and the number of samples have significantly increased. Accordingly, the EDA should be implemented along with the other methods used in the previous cases, including the virtual generator concept and integrating similar states method, as reported in the following coupled case studies.

Case 4: In this case, along with the integrating states and applying the precise uncertainty modeling for RES, the EDA algorithm has been adopted and applies to Case 3. Since the number of system modes in Case 3 was 100 and also the states of system equipment must be included, the number of required samples and the evaluation time will be unreasonable. In Case 3, the number of samples was 10 million and the time needed to evaluate the reliability was 5560 s . Here, the EDA algorithm has been used to assess the reliability indices. In this algorithm, before assessing the system states, many states with low failure modes that will not lead to loss of load are eliminated. Therefore, the remaining sample size will be significantly reduced. After this reduction, fewer samples can estimate the total probabilistic space of the problem.

If the load duration curve were considered instead of the fixed load
Table 7
Results of the reliability evaluation in Case 3.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Duration curve of wind and photovoltaic production.

Table 8
Results of the reliability evaluation in Case 4.

Table 9
Results of the reliability evaluation in Case 5.

(peak load), a large number of states would be omitted from the evaluation cycle. In other words, if in an interval of the load duration curve where the total load is much less than the installed capacity without renewable sources, the evaluation of the 100 modes of renewables will not be required. However, in this paper, the reliability assessment has been performed by considering the peak load for the whole year.

Moreover, at intervals where wind and photovoltaic output power levels are high, many possible network states are excluded from the reliability assessment because the load will be supplied. Therefore, in this case, $6,872,362$ samples are first removed from the samples' space of Case 3, and as a result, the remaining samples often lead to load interruption. The convergence of the EENS value with 898,763 samples has been obtained. In fact, the percentage of evaluated samples to the total number of available samples is about $13 \%$, which has significantly reduced the time in comparison with the previous case. The number of optimal power flow iterations, in this case, is 3500 times. The simulation results of Case 4 are provided in Table 8.

The results of Table 8 indicate the high computational efficiency of Case 4, while the reliability indices are not much different from the results of Case 3. Thus, the high efficiency of the EDA algorithm for improving computational efficiency with high accuracy is confirmed.

Case 5: In this case study, two WFs are removed from the test system, and only the PV units are considered as renewable resources. The integrating states and applying the precise uncertainty modeling for RES, the idea of the virtual generators and the EDA algorithm have been implemented for the reliability evaluation. Before evaluating the system states, a large number of states with the low possibility of failure, which certainly does not lead to loss of load, are eliminated and therefore, the samples size is significantly reduced. The reliability indices and computation time of this case are presented in Table 9.

The results of Table 9 demonstrate that the reliability of PV units is higher than wind resources. Hence, the contribution of generation failure events in the reliability indices has decreased by $15 \%$ compared to the previous case. Here, similar to Case $4,6,872,362$ samples in which total load is supplied, are initially removed from the probabilistic space.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Comparison of PLC index in five case studies.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Comparison of EENS index in five case studies.

![img-11.jpeg](img-11.jpeg)

Fig. 12. Comparison of LOLE index in five case studies.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Comparison of AENS index in five case studies.

The number of samples required to obtain convergence conditions is 577,776 , which shows that only $9 \%$ of the total samples have been evaluated. The required iterations for the optimal power flow program in the reliability assessment are 2250 times. As can be seen, in Case 5, there is a compromise between the reliability indices, computation efficiency and accuracy.

As can be seen from Figs. 10-13, the most important part of power system outages which leads to the load curtailment is pertaining to the generation level, where about $90 \%$ of failures occur, and only about $10 \%$ of failures are related to the transmission network. In Cases 3-5, due to the accurate modeling of the RES's uncertainty, more precise and reliable results are obtained from two other case studies. According to the proposed method, Case 5 has the best results regarding the values of reliability indices and computational efficiency.

## 5. Conclusion

In this paper, the reliability evaluation of the composite system, including renewable resources, has been performed by the nonsequential Monte Carlo method. The uncertainty sets have been used to estimate the PDF parameters that account for the uncertainty and variability of wind and PV power generation. The output powers of dependent RES units are determined by combining the multi-state probability table based on SRCC. To generate a system state array, the two-state arrays of conventional units, as well as transmission lines, are integrated with the binary string arrays of the WFs and PV units. Then, the system state array is transformed to its equivalent decimal number to
facilitate the integration of the entire system states. Thus, similar states in the sampling stage were simply extracted by this technique, and in the stage of calculating the reliability indices, only the probability of the relevant states was considered to avoid executing the OPF program. Moreover, the EDA according to the PBIL algorithm has been adopted for improving the computational efficiency of the MCS in the sampling step. In the reliability evaluation stage, the virtual generator concept has been introduced to significantly increase the computational speed of required load curtailment in each system state. The proposed mathematical model for reliability evaluation of composite power system is applied to the IEEE RTS 24-bus system, and numerical studies are performed under five case studied. The simulation results verify the proficiency of the proposed method to improve the computational efficiency, while the high accuracy of reliability evaluation of a composite power system is attained. The simulation results briefly show that:

If the reliability of the system equipment is higher, more similar states are obtained, and consequently, by integrating similar states, the number of OPF iterations to assess reliability is significantly reduced.

Generally, in the composite power systems, the most important part of power system outages which leads to the load curtailment is pertaining to the generation level, where about $90 \%$ of failures occur, and only about $10 \%$ of failures are related to the transmission network.

Assessing reliability without considering the relationship between the amount of output power uncertainty and the range of renewable sources' accuracy, using uncertainty sets, leads to inaccurate results. If the average values of renewables uncertainty are more significant than the actual values and are considered the same for all times, the

calculated reliability indices will be worse than reality. On the contrary, the values of the calculated reliability indices are less than the actual values and incorrectly indicate better reliability.

Improvement of uncertainty modeling of renewable resources using uncertainty sets yields the accurate reliability indices for renewablebased composite power systems with high computational time. Deficiency of high computational time is improved by implementing the EDA algorithm.

## CRediT authorship contribution statement

Mohsen Firouzi: Investigation, Methodology, Data curation, Software. Abouzar Samimi: Conceptualization, Writing - original draft, Supervision, Validation. Abolfazl Salami: Resources, Visualization, Writing - review \& editing, Validation.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
