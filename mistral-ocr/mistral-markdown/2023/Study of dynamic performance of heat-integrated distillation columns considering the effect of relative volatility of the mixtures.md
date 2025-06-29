# Study of dynamic performance of heat-integrated distillation columns considering the effect of relative volatility of the mixtures 

R. Gutiérrez-Guerra ${ }^{\text {a, }}$, J.G. Segovia-Hernández ${ }^{\text {b }}$, S. Hernández ${ }^{\text {b }}$<br>${ }^{a}$ Universidad Tecnológica de León, Campus I, Área de Sustentabilidad para el Desarrollo, Blvd. Universidad Tecnológica 225, Col. San Carlos, 37670 León, Gto., Mexico<br>${ }^{\mathrm{b}}$ Universidad de Guanajuato, Campus Guanajuato, Departamento de Ingeniería Química, Noria Alta s/n, C.P., 36050 Guanajuato, Gto., Mexico

## A R T I C L E I N F O

Article history:
Received 12 August 2022
Received in revised form 17 January 2023
Accepted 18 January 2023
Available online 21 January 2023

## Keywords:

Dynamic performance
HIDiC configurations
Open-loop process analysis
Closed-loop process analysis
Temperature driving forces

A B STR ACT
In this paper the dynamic performance of Heat-Integrated Distillation Columns (HIDiC) is presented. The dynamic performance was determined for the optimal HIDiC designs optimized previously using a constrained Boltzmann-based estimation of distribution algorithm. Eight close-boiling mixtures, covering a range of relative volatility ( $\alpha$ ) from 1.12 to 2.4 , were used as case studies. The dynamic behavior was obtained under open and closed-loop process analysis. The results obtained showed that the HIDiC columns undergo worse dynamic performance than their equivalent traditional columns for all case studies. Furthermore, it was notorious that the difference in the dynamic behavior of both configurations kept a relatively uniform trend for most systems. However, a marked difference in the dynamic properties was determined for the mixture close to azeotropic behavior, which experienced a considerably larger control effort.

Thus, the novel findings disclosed in this paper show that, although the HIDiC sequences experienced worse dynamics than the conventional columns, the HIDiC configurations reached a stable dynamic behavior for all the range of $\alpha$ of the mixtures under study. Nevertheless, high control difficulties were particularly determined for the HIDiC configuration used to separate the mixture with $\alpha$ close to unity (mixture of xylenes), which in fact is the HIDiC sequence with the best energetic and economic benefits.

Hence, the energetic and economic potential of the HIDiC columns is not limited by the dynamic behavior for most case studies analyzed, at least in theoretical terms. However, such potential might be particularly reduced or unharnessed in the separation of the mixture with $\alpha$ near the azeotropic behavior due to the dynamics of the HIDiC column for this separation.

So, the findings presented in this paper allow to infer that sequential or simultaneous dynamic studies must be achieved along with the optimization of the HIDiC columns to determine the integral performance (energetic, economic and dynamic) of these configurations.
(c) 2023 Institution of Chemical Engineers. Published by Elsevier Ltd. All rights reserved.

[^0]
## 1. Introduction

Heat-Integrated Distillation Columns (HIDiC) are separation technologies that provide large energy savings and reduce


[^0]:    * Corresponding author.

    E-mail address:
    rogutierrez@ulieon.edu.mx (R. Gutiérrez-Guerra).
    https://doi.org/10.1016/j.cherd.2023.01.032
    0263-8762/© 2023 Institution of Chemical Engineers. Published by Elsevier Ltd. All rights reserved.

![img-0.jpeg](img-0.jpeg)

Fig. 1 - HIDiC configuration.
cooling water requirements and emissions of pollutants (such as carbon dioxide) into the atmosphere. This performance has been disclosed for optimal HIDiC sequences used to separate multiple close-boiling mixtures (Gutiérrez-Guerra et al., 2017).

The HIDiC configuration is shown in Fig. 1. In this configuration, the stripping section (SS) represents the low pressure column while RS represents the high pressure column. Thus, the temperature driving forces are produced between both columns and the heat transfer takes place from RS to SS. The high pressure of RS is kept by compressing the vapor stream withdrawn from the upper part of the SS using the compressor (C). Then, this stream is introduced in the bottoms of RS. Furthermore, SS is kept at low pressure by regulating the pressure of the stream 10 using the throttling valve (TV) and this stream is fed to the upper part of SS. In illustrative terms, Q1-Q5 represent the heat flows transferred from the rectifying section to the stripping section.

The main variables that determine the behavior of these distillation configurations are the compression ratio (CR), reflux ratio (RR) and total number of stages (TNS). From these variables, CR plays a critical role in the design of these configurations. In fact, this variable must be maintained at the minimum possible value to obtain a suitable cost-benefit of the HIDiC sequences. This is required due to that the compressor is commonly driven by electricity and each electricity unit used is equivalent to three thermal units (Qcomp= 3Qheat), Jana and Mali (2010). Thus, CR must be reduced as much as possible in order to minimize the energy consumption and total annual cost (TAC).

Powered by their large energy savings, $30-50 \%$, (Nakaiwa et al., 2003, Iwakabe et al., 2006) the potential of the HIDiC configurations has been continuously examined from different perspectives. For instance, the study of several structural arrangements, such as concentric columns and configurations supported with external heat transfer panels (Gadalla et al., 2007) has been performed. It allowed avoiding the limitation of heat transfer area of the annular space present in a concentric HIDiC. Besides, the distribution of the heat integration along the columns has been explored (Wang et al., 2020). So, it found that the heat integration is more suitable at both ends of the column. However, it has also been reported that other HIDiC configurations with nonuniform stages distribution between the stripping section
and rectifying section have led to energetic improvements over the known typical HIDiC configuration (Wakabayashi et al., 2019). Authors also suggest that good control properties are expected for these novel configurations due to the adequate heat exchange structure at limited points between both sections of the HIDiC column. Likewise, several levels of heat integration (internal and external heat integration) have been achieved, Schmal et al. (2006). Also, some sensitivity studies by manipulating CR, TNS and RR have been performed (e.g. Jana and Mali, 2010). Hence, energy savings of $44 \%$ and TAC reductions of $14 \%$ at optimal CR of about 1.5 were determined in the analysis of a debutanizer HIDiC. Thus, the major influence on the energy consumption and TAC was determined for CR, followed by the influence of RR and low influence of TNS. Notice also that rigorous optimization studies using stochastic algorithms, such as the Boltzmann-based estimation of distribution algorithm (Gutiérrez-Guerra et al., 2014), have been achieved. In this case, energy savings between $52 \%$ and $84 \%$ and TAC reductions from $2 \%$ to HIDiC configurations with TAC $35 \%$ larger than the conventional columns were obtained. In addition, TAC reductions of 6.60-9.75\% were determined by optimizing the HIDiC columns using Genetic algorithms (Shahandeh et al., 2014). Besides, the optimization of HIDiC sequences by using a constrained Boltzmann-based estimation of distribution algorithm (Gutiérrez-Guerra et al., 2016) and a MINLP algorithm (Harwardt et al., 2010) conducted to establish that the maximum potential (energy savings and TAC) of the HIDiC columns is obtained in the separation of mixtures with low $\alpha$. Similarly, the best energy savings and TAC were identified for the separation of non-equimolar systems, 0.75/ 0.25 , (Gutiérrez-Guerra et al., 2017), by optimizing HIDiC sequences using a constrained Boltzmann-based estimation of distribution algorithm. In this case, energy savings between $85 \%$ and $87 \%$ were computed. Similar reductions for the cooling water and carbon dioxide emissions were calculated. In addition, TAC reductions of $27 \%$ were obtained. Besides, it is important to underline that the energetic and economic performance of the HIDiC configurations have been mainly focused on the separation of binary mixtures and only few multicomponent mixtures have been considered.

On the other hand, although most research has been focused on design and optimization based on simulation and thermodynamics analysis, HIDiC technologies have been subject to experimental, industrial and commercial studies and good results have been obtained (Wakabayashi et al., 2019, Rix et al., 2019, Fang et al., 2019, Marin-Gallego et al., 2022). These examinations have demonstrated an adequate level of approximation to the theoretical predictions in terms of energy savings. Thus, HIDiC configurations are promissory intensified distillation schemes able to reduce the energy and cooling water consumption along with reductions of pollutants released into the environment through their industrial implementation. However, despite large energy savings and competitive TAC (in relation with the traditional column) and good industrial projections have been reported, the control properties of HIDiC sequences have not been completely explored, such as it has been observed in Fang et al. (2019). In fact, most studies recently reported in literature have been focused on the typical separation of benzene/toluene and only some cases on the other mixtures of hydrocarbons and air fractioning. In addition, in the studies reported has been claimed that HIDiC columns are controllable distillation configurations (Jana and Mali, 2010,

Nakaiwa et al., 1998). However, despite this fact, it has also been underlined (Bisgaard et al., 2017, Fang et al., 2019) that more elaborated models are required to predict the adequate control of these columns due to their complex dynamics. The control properties have been analyzed using several control schemes, such as internal model control (IMC) and proportional, integral, and derivative (PID) control with singular value decomposition (Yu and Liu, 2005). Moreover, the temperature control using the temperature difference between two stages as the controlled variable was able to deal with the continuous pressure changes in the rectifying section, leading to stable operation of the HIDiC around the steady state. In fact, this control scheme showed a better dynamic performance in comparison with a direct composition control scheme. (Huang et al., 2007). Also, the high-purity internal thermally coupled distillation column have been analyzed using the dynamic matrix control (DMC). The Servo and regulatory control implemented confirm the accuracy and validity of DMC for this distillation column (Cong et al., 2014). Besides, the development and implementation of an Extended Generic Model Control for High-Purity Heat Integrated Distillation Column Using Online Concentration Estimation was achieved (Cong et al., 2015). Results presented indicate that EGMC shows a superior performance in comparison with the Proportional Integral Derivative control (PID) and a model predictive control scheme (MPC). In addition, the implementation of an adaptive generic model control shows advantages on servo control and regulatory control when it is implemented on a high-purity heat integrated air separation column (Fu and Liu, 2015). Similarly, in comparison with the standard Extended Generic Model Control (EGMC) scheme and the PI controller, a Reduced Extended Generic Model Control (R-EGMC) scheme showed better performance to track the dynamic behavior of the HIDiC (Cong et al., 2019). Authors claim that R-EGMC concentrates its good performance on the top and bottom stages, where the product quality is important for the control system of the HIDiC.

On the other hand, the control properties of the HIDiC sequences have been improved by adding a sensitive stage temperature control scheme with set-point correction. These results were determined through the implementation of this scheme on two PID temperature controllers and two Generic Model Control (GMC) schemes on a high-purity HIDiC column (Cong and Liu, 2020). In a more recent work (Markowski et al., 2022), the study of the control properties using novel model of heat and mass exchanger in a transient state implemented in the heat-integrated distillation columns was carried out. The results showed that the channel-type exchanger is dynamically stable under industrial constraints. In addition authors found that the distillate purity isn't strongly sensitive to the constraints related with the heat transfer surface or hold up of liquid inside the channel of exchanger. In fact, authors claim that distillate purity deteriorates approximately by $1 \%$. In addition, the study showed that the typical PID controller represents a good alternative to deal with industrial constraints through the proposed technology.

According to the background shown, the studies about control properties reported in literature have been directed to determine the dynamic behavior for a limited number of case studies. In fact, most studies have been focused on the separation of the mixture made of Benzene and Toluene and other few mixtures of hydrocarbons. So, generalized results about control properties have not been established for this
separation technology. Hence, in this work is presented the control properties of HIDiC columns implemented to separate eight close-boiling equimolar binary mixtures, exploring a range of $\alpha$ from 1.12 to 2.4 . This range was selected due to the large energetic and economic benefits obtained for these kinds of systems.

The mixtures under study are: Benzene-Toluene ( $\alpha=2.4$ ), Toluene-Ethylbenzene ( $\alpha=2.11$ ), Cyclohexane-n-Heptane ( $\alpha=1.68$ ), Isobutanol-n-Butanol ( $\alpha=1.44$ ), n-OctaneEthylbenzene ( $\alpha=1.248$ ), Ethylbenzene-o-Xylene ( $\alpha=1.23$ ), 111-Trichloroethane-Benzene ( $\alpha=1.20$ ), m-Xylene-o-Xylene ( $\alpha=1.12$ ). Product specifications (purity and recovery) around 0.995 were used for these mixtures.

Particularly, the goal of this work is to determine the performance of the HIDiC columns in comparison with their corresponding conventional sequences according to the $\alpha$ of the mixtures and the consequent implications of the control properties on the trends about design and optimization of the HIDiC sequences.

The control properties are determined using open-loop process analysis supported by the Singular Value Decomposition (SVD) technique and closed-loop process analysis supported by the minimization of the Integral Absolute Error (IAE). The study was supported by rigorous simulations carried out in Aspen Dynamics.

## 2. Control properties

Dynamic performance is an essential concern that must be addressed for all chemical processes in order to identify their behavior. This issue is related with the capability of the process to drive disturbances that modify the current steady state of the process. Thus, the response of the process is a key factor that will define the insurance (or not) of the production volume and the quality of the products processed, but also keep (or not) the safety conditions for the process itself and all resources around it.

In this work the control properties of HIDiC columns and conventional sequences are analyzed under a couple of approaches. The first one is the open-loop process analysis and the second one is the closed-loop process analysis. Notice that the simultaneous implementation of both approaches has not been achieved in previous dynamic studies of the HIDiC columns used in the separation of mixtures with variable $\alpha$. Hence, it addition to increase the confidence of the results obtained, the results will provide a background for dynamic studies of the HIDiC columns under both methods of analysis.

In this case, proportional integral controllers (PI) were used. These are common controllers used in the chemical processes due to their good performance and simplicity to be implemented (Luyben and Yu, 2008). It has been proved through their implementation to carry out the temperature control of multicomponent distillation columns (e.g. Baghmisheh et al., 2010).

### 2.1. Open-loop process analysis

Open-loop process analysis provides the natural response of the process when a disturbance acts on it. The open-loop dynamic properties of distillation columns are frequently obtained by evaluating the variation of the rich product composition of distillate and bottoms by disturbing the reboiler duty and reflux rate. The dynamic performance is

obtained by determining the singular values and condition number of the process. These parameters are found through the singular value decomposition (SVD) of the transfer function matrix (G), which is constituted by the transfer functions determined for each rich product obtained with the disturbances applied.

SVD of G is performed as follows: $G=V \Sigma W^{H}$, where $\Sigma=$ diag ( $\sigma 1 \ldots \mathrm{~m}$ ), $\mathrm{mi}=$ singular value of $\mathrm{G}=\lambda\left(\mathrm{V}^{2} \mathrm{GG}^{\mathrm{H}}\right), \mathrm{V}=(\mathrm{v} 1, \mathrm{v} 2, \ldots)$ is the matrix of left singular vectors and $\mathrm{W}=(\mathrm{w} 1, \mathrm{w} 2, \ldots)$ is the matrix of right singular vectors. In this work $\sigma$ - is used to represent the minimum singular value and $\sigma^{*}$ represents the maximum singular value. In addition, $\gamma=\sigma^{*} / \sigma$ - is defined as the condition number.

The minimum singular value is a measure of the invertibility of the system and represents a measure of the potential problems of the system under feedback control, while the condition number indicates the sensitivity of the system under uncertainties in process parameters and modeling errors.

Hence, the configurations with the largest minimum singular value and minimum condition number are expected to indicate the best dynamic properties of the process under feedback control (Gabor and Mizsey, 2008).

Notice that, although SVD is an approach to analyze the behavior of linear systems, it has been implemented in this work to obtain the control properties of HIDiC configurations, whose dynamic behavior is considered as nonlinear. However, we believe that this is an adequate approach to determine the control properties of these configurations because of the small disturbances ( $1 \%$ ) to be applied on the manipulated variables and the small variations expected in the product compositions. In other words, it is assumed that small disturbances will reduce the nonlinearity of distillation columns (Skogestad and Morari, 1988). In fact, this value of disturbance has been also applied on the manipulated variables in related studies (e.g. Bisgaard et al., 2017, Meyer et al., 2017). Besides, considering that the nonlinear behavior has a larger influence in separations with high purity products, the reduction of the purity was achieved with the disturbance applied. Thus, it is expected the nonlinear influence was also reduced using the direction of the disturbance proposed. Besides, as it was described before, a comparison of the control properties of the HIDiC columns and their respective conventional columns is achieved. Therefore, taking into account that both configurations will be examined using the same approach (SVD) and disturbance ( $1 \%$ ) on the manipulated variables, a fair comparison is expected.

Furthermore, the implementation of this control approach is achieved in this work because this technique has allowed predicting the control properties for different distillation sequences reported in previous studies (e.g. CabreraRuiz et al., 2017, Jana and Mali, 2010, Meyer et al., 2017, Murrieta-Dueñas et al., 2011).

In this work, SVD was carried out with the next frequency range: $\mathrm{w}=(0-1 \mathrm{E}+36)$. Although the upper limit represents a large frequency, the interest mainly concentrates on the frequencies near to the lower limit. That is, frequencies near the steady state ( $w=0$ ). However, the exploration of the upper limit was established to identify the trend of the control properties of the HIDiC configurations and their corresponding conventional sequences when large frequencies take place.

### 2.2. Closed-loop process analysis

This control strategy is based on the control action carried out by a controller installed on the process. This controller provides a response (control action) when the controlled variables are disturbed from their original value (initial steady state). In this case, the disturbance is handled by the controller through the control actions to take the process to the new steady state.

The closed-loop process analysis is performed using servo and load disturbance scenarios, employing Proportional Integral controllers (PI). The key factor to obtain the best performance of these controllers is the implementation of a right tuning process. This process consists of finding the adequate values for gain ( Kc ) and integral time ( $τ$ ) by means of an optimization process. The fitness function in this optimization process is the minimization of the Integral of the Absolute Error (IAE). The value for this criterion is computed through the generation of disturbances in the controlled variables and the behavior of these variables under control actions performed by the PI controller, taking as a reference the new setpoint. As before, the evaluation of the control properties under closed-loop analysis was carried out using small disturbances ( $1 \%$ ) on the purity of the rich products in the bottoms and distillate. The selection of this percentage of disturbance was made in order to preserve concordance with the open-loop process analysis and make a fair comparison between both control approaches. In addition, as before, this level of disturbance is used to reduce the impact of the nonlinear behavior on the control properties of these distillation columns. Although this level of disturbance is really small and a realistic operation could lead to larger perturbations, important results about the dynamic behavior of the HIDiC columns are expected by means of the implementation of this approach.

Likewise, the small offset errors expected between the product composition and the setpoint along the simulations (due to small disturbances applied), motivated the selection of the IAE index. IAE index is better than the ISE (integral of the square error) index because a small value (less than 1) raised to the power 2 becomes even smaller if ISE index is used. Besides, it is expected that offsets occur for short periods of time, so, ITAE (Integral of the Time-Weighted absolute error) was not considered convenient. This statement agrees with that established by Stephanopoulos (1984) and partially with Zhang et al. (2018). Hence, the configurations (either HIDiC or conventional columns) with lower IAE values are those with the best control properties.

Notice that IAE index has been implemented in multiples studies to disclose the control properties of distillation configurations (Alcocer-Garcia et al., 2020, Farias Neto et al., 2021, Meyer et al., 2017, Liang et al., 2021, Liu et al., 2022, Shan et al., 2021).

Through this approach PI controller manipulates the Reboiler Duty, when the disturbance is applied on the rich product of the bottoms, or the reflux rate, when the disturbance is applied on the rich product of the distillate. The selection of this relationship was supported on practical aspects related with distillation columns (Häggblom and Waller, 1992, Murrieta-Dueñas et al., 2011). That is, the purity of the distillate product is related with the manipulation of the reflux rate while the bottom product is associated with the manipulation of the reboiler duty.

Table 1 - Optimal HIDiC configurations.

|  | M1 |  |  | M2 |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | CONVENTIONAL |  | HIDiC | CONVENTIONAL |  | HIDiC |
| TNS | 28 |  | 28 | 28 |  | 28 |
| RR | 1.68 |  | 0.22 | 2.78 |  | 0.27 |
| CR | - |  | 2.15 | - |  | 1.99 |
| Recovery | 0.9949 |  | 0.9949 | 0.9952 |  | 0.9949 |
| Purity | 0.9949 |  | 0.9949 | 0.9952 |  | 0.9950 |
| TAC (USD/year) | 387607.33 |  | 531022.04 | 573709.34 |  | 768770.52 |
| QReb (kJ/h) | 4375889.30 |  | 1454545.06 | 6438085.61 |  | 1431414.88 |
| Qcomp (kJ/h) | - |  | 609019.98 | - |  | 984078.56 |
|  | M3 |  |  | M4 |  |  |
|  | CONVENTIONAL |  | HIDiC | CONVENTIONAL |  | HIDiC |
| TNS | 56 |  | 56 | 72 |  | 72 |
| RR | 3.06 |  | 0.38 | 5.27 |  | 0.084 |
| CR | - |  | 1.86 | - |  | 1.76 |
| Recovery | 0.9951 |  | 0.9949 | 0.9952 |  | 0.9952 |
| Purity | 0.9951 |  | 0.9949 | 0.9951 |  | 0.9950 |
| TAC (USD/year) | 609043.22 |  | 803937.05 | 1187928.65 |  | 1164170.08 |
| QReb (kJ/h) | 6126487.95 |  | 1534376.91 | 15815250.00 |  | 1043286.64 |
| Qcomp (kJ/h) | - |  | 738895.52 | - |  | 1153724.86 |
|  | M5 |  |  | M6 |  |  |
|  | CONVENTIONAL |  | HIDiC | CONVENTIONAL |  | HIDiC |
| TNS | 74 |  | 74 | 78 |  | 78 |
| RR | 23.56 |  | 9.63 | 13.20 |  | 2.55 |
| CR | - |  | 1.34 | - |  | 1.46 |
| Recovery | 0.9949 |  | 0.9951 | 0.9953 |  | 0.9947 |
| Purity | 0.9949 |  | 0.9952 | 0.9950 |  | 0.9953 |
| TAC (USD/year) | 3329422.20 |  | 2730126.20 | 2421000.00 |  | 2421000.00 |
| QReb (kJ/h) | 40513398.75 |  | 16941201.86 | 25448924.92 |  | 3984716.82 |
| Qcomp (kJ/h) | - |  | 1701190.44 | - |  | 2391899.12 |
|  | M7 |  |  | M8 |  |  |
|  | CONVENTIONAL |  | HIDiC | CONVENTIONAL |  | HIDiC |
| TNS | 82 |  | 82 | 138 |  | 138 |
| RR | 24 |  | 6.63 | 33.92 |  | 4.25 |
| CR | - |  | 1.35 | - |  | 1.56 |
| Recovery | 0.9948 |  | 0.9948 | 0.9953 |  | 0.9950 |
| Purity | 0.9948 |  | 0.9947 | 0.9953 |  | 0.9950 |
| TAC (USD/year) | 2214919.49 |  | 2613605.00 | 5306658.692 |  | 5678124.80 |
| QReb (kJ/h) | 27967688.10 |  | 9304639.36 | 72176583.60 |  | 1017917.75 |
| Qcomp (kJ/h) | - |  | 1999288.00 | - |  | 8575761.36 |

The components of each mixture are: M1: Benzene-Toluene ( $\alpha=2.4$ ), M2: Toluene-Ethylbenzene ( $\alpha=2.11$ ), M3: Cyclohexane-n-Heptane ( $\alpha=1.68$ ), M4: Isobutanol-n-Butanol ( $\alpha=1.44$ ), M5: n-Octane-Ehtylbenzene ( $\alpha=1.248$ ), M6: Ethylbenzene-o-Xylene ( $\alpha=1.23$ ), M7: 111-TrichloroethaneBenzene ( $\alpha=1.20$ ), M8: m-Xylene-o-Xylene ( $\alpha=1.12$ ).

Particularly, the correlation between manipulated variables and product composition was used as a first approximation to study the dynamic properties of the HIDiC sequences. Nevertheless, taking into account the structural characteristics of these sequences, it is suggested to examine their dynamics under alternative control schemes in a further study. For instance, considering CR as an additional manipulated variable. This examination will provide an additional comparison of the dynamic behavior of HIDiC columns in relation with the conventional sequences, but also the comparison of performance between both approaches (with or without the inclusion of CR) will be obtained. Thus, the results will also indicate the most convenient approach to obtain the control properties of HIDiC configurations.

## 3. Case study

The designs of the Heat-Integrated Distillation Columns described in Table 1 are used as case studies. These case studies are the optimal HIDiC configurations obtained in a
previous work (Gutiérrez-Guerra et al., 2016). In this case, the separation of eight equimolar binary mixtures whose $\alpha$ varies from 1.12 to 2.4 is carried out. The thermodynamic model of Chao-Seader was used as thermodynamic model to predict the behavior of the mixtures M1-M3 and M5. These mixtures are made up of hydrocarbons and they are separated in a relatively easy way (Seader and Henley, 2006). In addition, the mixture M6 and M8 were modeled by UNIQUAQ model. This election was made due to the fact that it adequately represents the thermodynamic properties of this mixture of isomers (Rodrigues et al. 2005). Whereas, NRTL model was used to estimate the thermodynamic properties for the mixtures M4 and M7 taking into account the general guidelines given by Seader and Henley (2006). These optimal HIDiC columns were obtained through an optimization process using a constrained Boltzmann-based estimation of distribution algorithm (Gutiérrez-Guerra et al., 2016). The TAC was used as fitness function while CR, TNS and RR were the decision variables of the optimization problem. These optimal configurations showed large energy savings (larger than $50 \%$ ) and competitive TAC for most cases in relation

with the traditional configuration. Besides, each HIDiC design is operated using $C R$ between 1.4 and 2.15 , which agrees with the values reported in other studies (Jana et al., 2010). Observe also that RR and TNS were determined under reasonable values in practical terms, considering the characteristics of the mixtures separated.

Notice that the optimal HIDiC configurations and their corresponding conventional columns were sized with the same TNS. Besides, the energy integration (from rectifying section to stripping section) was achieved in stages at the same height of the columns, that is, no crossed heat integration was performed.

On the other hand, a flow rate of $100 \mathrm{kmol} / \mathrm{h}$ of saturated liquid was introduced as feed on the first stage of the column 1 (SS) of the HIDiC, while recoveries and purities for the products were established in values around 0.995 . The same specifications were established for the corresponding conventional sequences.

The components of each mixture are: M1: BenzeneToluene $(\alpha=2.4)$, M2: Toluene-Ethylbenzene $(\alpha=2.11)$, M3: Cyclohexane-n-Heptane ( $\alpha=1.68$ ), M4: Isobutanol-n-Butanol $(\alpha=1.44)$, M5: n-Octane-Ethylbenzene $(\alpha=1.248)$, M6: Ethylbenzene-o-Xylene $(\alpha=1.23)$, M7: 111-TrichloroethaneBenzene $(\alpha=1.20)$, M8: m-Xylene-o-Xylene $(\alpha=1.12)$.

As it was described before, the potential of the HIDiC columns is given by the large energy savings achieved for these configurations in relation with the conventional sequences. This potential has been considerably increased by means of optimization processes. The optimization of the HIDiC columns used as case studies in this work was performed in a previous work. As it was described before, the optimization was carried out by manipulating CR, RR and TNS, having the total annual cost as the fitness function of the optimization problem. In this case, the TAC was computed using the procedure shown in Appendix A. In this optimization, product specifications (purity and recovery) of the mixtures were constrained to $0.995 \pm 0.0003$. In addition, the amount of internally heat integrated from stages of RS to stages of SS was achieved considering a minimum temperature driving $(1.67 \mathrm{~K})$ between both sections. Besides, the condenser duty (QT) was used as the amount of available heat to be transferred from the rectiputed section to the stripping section. The selection of the condenser duty was achieved considering the operational principles of the traditional distillation columns. That is, the heat used to fuel the reboiler in a conventional distillation column is released to the environment through the cooling water used in the condenser. This is the reason of the low thermodynamic efficiency of the conventional distillation columns. So, instead to reject this amount of energy to the environment, the energy quality (temperature) is increased by increasing the pressure of the rectifying section in the HIDiC column and then this higher quality energy is transferred from RS to SS. Particularly, the temperature driving forces were controlled by CR in the optimization process. So, the heat distribution was carried out along the column depending on such temperature driving forces between the stages of RS and SS. In this case, the heat transfer from the stages of the rectifying section to the stages of the stripping section was achieved using heat flows in Aspen Plus.

Furthermore, heat integration carried out in the HIDiC configurations under study was determined using the approach established by Suphanit (2010). In this approach, the heat distribution stage by stage was computed using Eq. (1) while the heat transfer area was determined using Eq. (2).
$\mathrm{Q}_{1}=\Delta \mathrm{T}_{\mathrm{RS} 1-\mathrm{SS}}\left(\frac{\mathrm{Q}_{\mathrm{T}}}{\sum_{\mathrm{i}=1}^{\mathrm{n}} \Delta \mathrm{T}_{\mathrm{RS} 1-\mathrm{SSi}}}\right)$
$A_{i}=\frac{Q_{i}}{U \Delta T_{\mathrm{RS} 1-\mathrm{SS}}}$
In this case, i represents the corresponding stage and n is the total number of stages of each column, either RS or SS. Notice that $\mathrm{n}_{\mathrm{RS}}=\mathrm{n}_{\mathrm{SS}}$. Hence, $\Delta \mathrm{T}_{\mathrm{RS} 1-\mathrm{SSI}}$ represents the difference of temperature between the stages of the rectifying section and the corresponding stages of the stripping section. QT and Qi represent the total internally heat integrated and the internally heat integrated at each stage, respectively. Moreover, the heat transfer takes place between stages at the same level of RS and SS. Likewise, the value for the overall heat transfer coefficient (U) used for sizing the heat transfer areas was of $4085.62 \mathrm{~kJ} / \mathrm{hm}^{2} \mathrm{~K}$ (Adapted from Turton et al., 2004).

Notice that the HIDiC columns designed and optimized were assembled using the same TNS in both sections of the column (rectifying section and stripping section). In fact, the original optimization study was conducted based on this criterion (Gutiérrez-Guerra et al., 2016). So, the HIDiC columns subject to optimization were built by dividing the conventional column into two sections with the same number of stages. Therefore, the feed stream was introduced in the first stage of the stripping section of the HIDiC column. Hence, the feed stage was not considered as an optimization variable. In fact, the design and optimization strategy stablished in such optimization study was well supported by the large energy savings and competitive TAC obtained, in comparison with the conventional columns. Thus, these results encouraged the analysis of the control properties of the optimal HIDiC columns performed in this work.

## 4. Problem statement

The control properties of HIDiC and traditional configurations for mixtures under study were determined using the open-loop process analysis supported by the singular values decomposition (SVD) technique and the closed-loop process analysis supported by the minimization of the Integral of the Absolute Error (IAE).

### 4.1. Open-loop process analysis

### 4.1.1. Stage I

Step 1. Export HIDiC design from Aspen Plus to Aspen Dynamics.

Step 2. Compute the new reboiler duty $\left(\mathrm{QReb}_{\text {new }}\right)$ and reflux rate (RRnew) values by applying $1 \%$ of disturbance on the current values. Hence, $\mathrm{QReb}_{\text {new }}=0.99^{*}$ (QReb) and RRnew $=0.99^{*}$ RR. Notice that CR for the HIDiC columns was kept constant in the rigorous simulations performed in Aspen Dynamics.

Step 3. Apply the disturbance on the reboiler duty of the HIDiC column and run the simulation. In this case, the perturbation is applied in SS. In this step, the composition of the bottoms and distillate changes along the time until stabilizes. Hence once the stabilization is achieved, the simulation is stopped.

Step 4. Obtain and plot (in Excel) the composition profiles (as a function of time) of the distillate product $\left(\mathrm{X}_{\mathrm{D}}\right)$ and bottoms product $\left(\mathrm{X}_{\mathrm{B}}\right)$ of the HIDiC column.

Step 5. Adjust each composition profile ( $\mathrm{X}_{\mathrm{B}}$ and $\mathrm{X}_{\mathrm{D}}$ ) to a known transfer function (TF), such as first order, second order, with or without time delay (dead time) and so on. The fitting parameters [Gain (Kc), Integral time ( $\tau$ ), time delay, and so on] of the transfer functions are defined by the user. The selected parameters used to fit the transfer functions must minimize the error between the composition profile given by the simulation and the adjustment achieved by the transfer function proposed by the user. The fitting process may be described as follows: Initially, user introduces the values for the gain, integral time, time delay, and so on, to the model of the transfer function, depending on the order of it. Then, the deviation grade (error) between the original composition profile (obtained from Aspen Dynamics) and the approximation using the transfer function is computed with the current setting parameters (gain, integral time, time delay, and so on). Hereafter, an optimization process is achieved, having as fitness function the minimization of the error between the original composition profile and the approximation using the transfer function, by evaluating several values of the parameters of the transfer function described before. It is important to mention that the tool called Goal Seek of Excel was used to carry out the minimization of the Error.

In this case, two transfer functions (TF1 and TF2) are obtained, one for the rich product of the bottoms (B) and one for rich product of the distillate (D).

Step 6. Repeat steps 3-5 using the new reflux rate (RRnew) instead the Rebolier duty in the HIDiC column. In this case, the perturbation is applied on RS. As a result, two additional transfer functions are obtained (TF3, TF4).

In overall terms, steps 1-6 can be summarized in Fig. 2.

### 4.1.2. Stage 2

Step 7. Assemble the transfer function matrix. The form of the transfer function matrix is given in Eq. (3).

$$
G=\begin{array}{cc}
Q \operatorname{Re} b & R R \\
X_{D}\left(\begin{array}{cc}
T F 11 & T F 12 \\
T F 21 & T F 22
\end{array}\right) \\
\hline
\end{array}
$$

Step 8. Perform SVD of G in Matlab.
Step 9. Repeat the previous loop (step 1 to step 8) for the conventional configurations.

Step 10. Plot the minimum singular values of the HIDiC columns on the same graphic as the minimum singular values of the conventional sequence. Similarly, the condition numbers for the HIDiC are plotted on the same figure as the condition number obtained for the traditional column.

Step 11. Perform the comparison of the control properties of both configurations (HIDiC and conventional sequences) and determine the configuration with the largest minimum singular value and lowest condition number. The best
![img-2.jpeg](img-2.jpeg)

Fig. 2 - Flowsheet to obtain the open-loop process responses of HIDiC sequences and conventional columns.
dynamic performance is expected for the configuration with such values.

### 4.2. Closed-loop process analysis

4.2.1. Stage 1

Step 1. Export HIDiC design from Aspen Plus to Aspen Dynamics.

Step 2. Add PI controller and IAE module to the bottoms (PI-B, IAE-B) and distillate (PI-D, IAE-D) of the HIDiC column. See Fig. 3.
![img-2.jpeg](img-2.jpeg)

Fig. 3 - HIDiC configuration used for closed-loop process analysis.

Step 3. Determine the new composition of the rich product of the bottoms ( $\mathrm{X}_{\text {Bnew }}$ ) and the new composition of the rich product of the distillate ( $\mathrm{X}_{\text {Dnew }}$ ) of the HIDiC column by applying a disturbance of $1 \%$. That is, $\mathrm{X}_{\text {Bnew }}=0.99^{\circ} \mathrm{X}_{\mathrm{B}}$ and $\mathrm{X}_{\text {Dnew }}=0.99^{\circ} \mathrm{X}_{\mathrm{B}}$. Thus, $\mathrm{X}_{\text {Bnew }}$ and $\mathrm{X}_{\text {Dnew }}$ represents the new setpoint to be reached in the process through the control action performed by the PI controller. The reboiler duty (QReb) and reflux rate (RR) are the manipulated variables to drive the rich product composition of bottoms and the rich composition of distillate, respectively.

Step 4. Configure the PI-B controller and IAE module. The PI-B controller is configured when user introduces the gain $(\mathrm{Kc})$ and integral time $(\tau)$ values while IAE-B module is configured using $\mathrm{X}_{\text {Bnew }}$ value.

Step 5. Run the simulation and obtain the value of IAE-B when the composition of the bottoms equals to the setpoint, through the automatic manipulation of the reboiler duty achieved by the controller. As before, CR for the HIDiC columns was kept constant in the rigorous simulations performed in Aspen Dynamics.

Step 6. Repeat the steps 4-5, updating Kc and $\tau$, until the minimization of the IAE value is achieved. Again, user introduces each pair of parameters and performs the simulation in Aspen dynamics.

Step 7. Repeat steps 4-6 for PI-D and IAE-D instead PI-B and IAE-B, respectively, by manipulating the reflux rate instead reboiler duty. Notice that when PI-B is closed, PI-D is open and vice versa. This tuning strategy is supported due to the fact that the influence among the control loops is reduced considering the simultaneous reduction of the nonlinearity of the process under the small disturbances (1\%) applied on it. This consideration is made taking into account the analysis of the control properties of distillation columns conducted by Skogestad and Morari (1988). They decoupled the flows dynamics from the composition dynamics for small variations in the product compositions and found low effect of the non-linearity on the control properties of the distillation columns under this assumption.

Step 8. Perform steps 1-7 for the conventional sequence.
In this case, steps 1-8 can be summarized in Fig. 4.
Notice that the first step to perform the tuning of the PI controllers was the exploration of the search space for identifying the region where the pairs ( Kc and $\tau$ ) provide lower values of IAE. To make this exploration, firstly was delimited the search space. It was conducted by establishing a rectangle formed by four pairs of gain and integral time and determining the respective IAE values, see Fig. 5 The first pair $(\mathrm{Kc} 1, \tau 1)$ was formed by small values of gain and integral time, while the second pair ( $\mathrm{Kc} 1, \tau 2$ ) was assembled using a small value of the gain but a large value of the integral time. The third pair ( $\mathrm{Kc} 2, \tau 1$ ) was formed by a large value of the gain but a small value of the integral time. Whereas, the fourth pair ( $\mathrm{Kc} 2, \tau 2$ ) was made with large values of the gain and integral time. Notice that the initial values of the gain and integral time were randomly established. Once the initial exploration was achieved, the search was conducted in the direction of the region where lower IAE values were determined. Of course, the search space was reconfigured when the trend of the best search zone was out of the original search space established. In general terms, the search space was continuously limited by evaluating several pairs of gain and integral time until to segregate the best search space where the optimal values of IAE were obtained. The search is
![img-3.jpeg](img-3.jpeg)

Fig. 4 - Flowsheet to obtain the closed-loop process responses of HIDiC and conventional columns.

| $\mathrm{Kc} 1, \tau 1$, IAE1 | $\mathrm{Kc} 1, \tau 2$, IAE2 |
| :-- | :-- |
| $\mathrm{Kc} 2, \tau 1$, IAE3 | $\mathrm{Kc} 2, \tau 2$, IAE4 |

Fig. 5 - Delimitation of the search space.
finalized when the IAE values was unchangeable or when they experienced relatively low variations.

### 4.2.2. Stage 2

Step 9. Perform the comparison of the IAE values of the HIDiC column and IAE values of the corresponding conventional sequence, for the respective rich component of the bottoms and distillate obtained in steps 1-8.

Step 10. Determine the configuration with the best control properties through the comparison achieved in step 9. In this case, the configuration with the best dynamic properties will be the column with lower IAE values.

## 5. Results and discussion

In the first part of this section are presented the results for the open-loop process analysis. The discussion concentrates on the comparison of the minimum singular values and condition numbers obtained through the SVD technique. In

![img-4.jpeg](img-4.jpeg)

Fig. 6 - Open-loop process analysis/Minimum Singular Values.
this case, the analysis is carried out considering a range of frequency between $1 \mathrm{E}-04-1 \mathrm{E}+02$ for the minimum singular values and $1 \mathrm{E}-04-1 \mathrm{E}+04$ for the condition number. In a complementary analysis, the comparison of the closed-loop process analysis is shown in the second part. In this case, the analysis focuses on the IAE values. In both dynamic properties analysis, the comparison between the control properties of the HIDiC configuration and the control properties of the conventional sequence is performed. In the third part, the results analysis and their implications on the HIDiC are discussed.

### 5.1. Open-loop process analysis

In Fig. 6 the minimum singular values for the HIDiC sequences and their corresponding conventional columns are presented. As it can be observed, the minimum singular values tend to decrease as frequency increases. This behavior is experienced for all cases. However, it is observed that the minimum singular values continuously decrease with relatively small reductions (from $1 \mathrm{E}-01-7 \mathrm{E}+01$ ) at low frequencies. In contrast, the minimum singular values undergo large reductions as the frequency increases.

The trend of the dynamic behavior depicted in Fig. 6 shows that the largest minimum singular values of the HIDiC are lower than the minimum singular values of their corresponding conventional sequence for all mixtures. Besides, notice that the major difference between the minimum singular values ( 0.4 for the HIDiC and 60 for the conventional) was found in the steady state ( $w<1$ ) for the system M8, whose $\alpha$ is 1.12 .

The behavior of the condition numbers shown in Fig. 7 describes a non-uniform trend at low frequencies (1E-04-1E +02). In fact, the condition number values experience a variation from 1 to 604 in this range of frequency considering all mixtures analyzed. In addition, Fig. 7 depicts lower condition numbers for the conventional sequences than for the HIDiC sequences for most case studies. However, there exists one system (M7) whose condition number is larger than the HIDiC column at frequencies lower than 1, but this trend is inverted at larger frequencies. So, a competence for the best control properties is identified for this mixture in terms of
![img-5.jpeg](img-5.jpeg)

Fig. 7 - Open-loop process analysis/condition numbers.
this parameter. Besides, although the condition number for the mixture M1 becomes slightly lower for the HIDiC than the conventional column for frequencies larger than 5 , the condition number for the conventional column is considerably lower at frequencies lower than 5 .

Since other point of view, the trend of the condition number shown in Fig. 7 indicates that at large frequencies the plant is less influenced by disturbances in the process. Thus, it is expected that the PI controller handles the disturbances effectively because of the uniform trend (linear trend) experienced for this criteria (CN) at large frequencies. Nonetheless, notice there exists a large influence of the disturbances in the operation conditions as the system approximates to steady state. In fact, there exists a range of frequencies ( $1 \mathrm{E}-02<\mathrm{w}<1 \mathrm{E}+02$ ) at which the system experiences a transition state where the marked nonlinear behavior takes place. This behavior denotes that a larger control effort must be made by the PI controller around the steady state of the process. However, the steady state is reached by conventional and HIDiC configurations at frequencies lower than 1E-02. Therefore, the similar behavior observed for HIDiC columns and conventional sequences enables us to say that this trend could be mainly produced by the characteristics of the mixtures, i.e., close-boiling mixtures with low $\alpha$ and high purity products.

Therefore, the best control properties for this system are attributed to the conventional sequence in terms of the condition number. On the other hand, notice that the system with lowest $\alpha$ (M8) undergoes the major difference of the condition number between both configurations. In fact, the largest condition number for the HIDiC configuration was about 604 while the largest value for the conventional sequence was about 31. In addition, the minimum condition number for the HIDiC sequences was 18.21 while the minimum condition number for the conventional column was of 1.9. Therefore, based on this parameter, the control properties for the conventional column are predominantly better than the HIDiC for this mixture.

A complementary representation of the minimum singular values and condition numbers is shown in Table 2. Particularly, these parameters represent the steady state ( $\mathrm{w}=0$ ) of HIDiC configurations and conventional sequences. Here, SV-ratio is given by the minimum singular value of the HIDiC column divided by the minimum singular value of the conventional sequence. Similarly, CN-ratio represents the

Table 2 - Minimum singular value and condition number at steady state.

|  | Minimum Singular Values |  |  | Condition Numbers |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| Mixture | HIDiC | CONV | SV-ratio | HIDiC | CONV | CN-ratio |
| M1 | 0.12 | 4.71 | 0.0259 | 14.46 | 1.72 | 8.41 |
| M2 | 0.19 | 6.18 | 0.0303 | 9.24 | 1.77 | 5.21 |
| M3 | 0.35 | 13.79 | 0.0251 | 7.44 | 1.19 | 6.25 |
| M4 | 0.14 | 25.50 | 0.0053 | 11.22 | 1.85 | 6.06 |
| M5 | 23.82 | 44.89 | 0.5306 | 1.61 | 1.90 | 0.85 |
| M6 | 5.82 | 32.49 | 0.1790 | 1.46 | 1.54 | 0.95 |
| M7 | 5.96 | 7.41 | 0.8043 | 3.00 | 7.94 | 0.38 |
| M8 | 0.40 | 60.15 | 0.0066 | 32.87 | 1.89 | 17.39 |

condition number of the HIDiC column divided by the condition number of the traditional sequence. As it is depicted in Table 2, the minimum singular values of the HIDiC columns were less than the corresponding values of the conventional sequences. In fact, SV-ratio was considerably less $(<<1)$ for most cases. Furthermore, the condition numbers of the HIDiC columns were larger than the condition numbers for the conventional sequences for most case studies. Thus, CNratio $>1$ was determined for most case studies. As before, the steady state results confirm the better dynamic performance of the traditional sequences in comparison with the HIDiC sequences.

Thus, the open-loop analysis reveals that the conventional columns have better control properties than the HIDiC configurations. This statement is applicable even to the mixture M7 due to that despite it undergoes competence in terms of condition number, the minimum singular values are larger for the conventional columns than for the HIDiC sequences. On the other hand, it is evident that the conventional column showed considerably better control properties than the HIDiC sequence for the mixture M8, which allows to infer major control difficulties for this mixture in relation with the other systems with larger $\alpha$. Finally, with the aim to provide a more detailed visualization of the trends for the minimum singular values and condition numbers, the individual comparison (HIDiC versus conventional sequence) for each mixture along the range of frequency established, is presented in Appendix B.

In addition, in order to justify the dynamic performance of the HIDiC configurations and traditional columns, a set of data has been collected in Table 3. As an illustrative case, these data were obtained for the response of the rich component of the distillate of the HIDiC columns.

The analysis of Table 3 shows that the inputs and outputs of the HIDiC configurations and also those of the conventional columns are modeled by first order and second order transfer functions, such as it was described before. Besides, the value of the gains for the HIDiC configurations is lower than the values of the gains for the conventional sequences. Similarly, the integral time values were larger for the HIDiC configurations in comparison with the traditional columns. Moreover, due to the relatively small values of the gain for most HIDiC configurations, it is expected that the PI controller becomes less sensitive when disturbances take place and, consequently, less effective control actions are performed and larger stabilization times are required. This fact supports the better dynamic behavior determined for the conventional columns.

As illustrative cases, the transfer function matrices for the HIDiC sequence and conventional column (for mixture M2)
are shown in Eq. (4) and eq. (5), respectively.

$$
\begin{aligned}
& Q \operatorname{Re} b \quad R R \\
& G(s)=\begin{array}{c}
X_{D}\left(\frac{0.584}{1+2.3 S} \quad \frac{-0.3568}{1+4 S}\right. \\
X_{B}\left(\frac{-1.5492}{1+4 S} \quad \frac{0.3928}{1+4.5 S}\right) \\
Q \operatorname{Re} b \quad R R
\end{array} \\
& G(s)=\begin{array}{c}
X_{D}\left(\frac{0.8744}{1+2 \mathrm{~S}} \quad \frac{-6.6324}{1+2.2 \mathrm{~S}}\right. \\
X_{B}\left(\frac{-10.47}{2.25 \mathrm{~S}^{2}+3 \mathrm{~S}+1} \quad \frac{1.9804}{1+2 \mathrm{~S}}\right)
\end{array}
\end{aligned}
$$

Similarly, the transfer function matrices for the mixture M8 (Xylenes mixture) are shown through Eq. (6) and eq. (7) for the HIDiC configuration and conventional column, respectively.
![img-6.jpeg](img-6.jpeg)

The transfer function matrices (Eqs. 4-7) show the form through which the inputs and outputs of the HIDiC configurations and also those of the conventional columns are related by means of first order and second order transfer functions. As it was described before, larger gains and lower integral times were determined for the transfer functions of the conventional sequences compared with the parameters of the HIDiC columns.

In addition to the previous analysis, Table 4 shows the heat distribution in the stripping and rectifying sections of the HIDiC columns. The aim of Table 4 is to present the fraction of the energy supplied in the reboiler and removed in the condenser of the HIDiC configurations. Here, Qint. represents the amount of internally heat integrated from

Table 3 - Tuning parameters for PI controller of HIDiC and conventional columns.

| HIDiC configuration |  |  |  |  | Conventional column |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Mixture | Order of the transfer function | Kc | $\tau(h)$ |  | Order of the transfer function | Kc | $\tau(h)$ |
| M1 | First order | $-0.2996$ | 2.3 |  | First order | $-5.0152$ | 5.0 |
| M2 | First order | $-0.3568$ | 4.0 |  | First order | $-6.6324$ | 2.2 |
| M3 | First order | $-0.5040$ | 8.0 |  | Second order | $-15.6332$ | 4.0 |
| M4 | First order | $-0.2884$ | 13.0 |  | Second order | $-47.0820$ | 2.5 |
| M5 | Second order | $-23.8900$ | 18.0 |  | Second order | $-44.9180$ | 8.0 |
| M6 | Second order | $-7.2424$ | 20.0 |  | Second order | $-32.6340$ | 3.2 |
| M7 | Second order | $-6.1892$ | 9.0 |  | Second order | $-7.4632$ | 2.0 |
| M8 | Second order | $-12.9000$ | 238.0 |  | Second order | $-60.2188$ | 20.0 |

rectifying section to stripping section. In this case, Qint. $=$ Qint. ${ }_{S S}=$ Qint. ${ }_{R S}$, which indicates that the heat released in the rectifying section is taken by the stripping section. Besides, QReb and $\mathrm{Q}_{\text {Cond. }}$ represent the reboiler duty and condenser duty, respectively. Thus, Qratio ${ }_{S S}$ and Qratio ${ }_{R S}$ are given by Eq. (8) and eq. (9):
$\mathrm{Q}_{\text {ratio }_{S S}}=\frac{\mathrm{Q}_{\text {Reb. }}}{\mathrm{Q}_{\text {Reb. }}+\mathrm{Q}_{\text {Int.SS }}}$
$\mathrm{Q}_{\text {ratio }_{R S}}=\frac{\mathrm{Q}_{\text {Cond. }}}{\mathrm{Q}_{\text {Cond }}+\mathrm{Q}_{\text {Int. }_{R S}}}$
As it can be observed, the internal heat integration provides more than $80 \%$ of the energy required to perform the separation of most mixtures. In fact, the separation of some mixtures is performed taking even more than $90 \%$ of the energy by means of the internal heat integration. Notice also that more than $75 \%$ of the energy was removed from the process by means of the internal heat integration for most mixtures. As before, there exists even one mixture whose condenser removes less than $10 \%$ of the heat released in the process. Thus, the heat supplied by the reboiler and the heat removed by the condenser represents less than $20 \%$ and $25 \%$, respectively, of the total energy involved in the separation of most mixtures.

So, it can be assumed that the dynamic behavior for the HIDiC columns is mostly influenced by the liquid and vapor internal flows generated with the internally heat integrated in comparison with the effect of the external flows. Hence, it would be interesting to explore the implementation of an additional control loop by involving CR as an additional manipulated variable in order to improve the performance of the PI controller to deal with the disturbances of the HIDiC configurations.

### 5.2. Closed-loop process analysis

The results of the closed-loop process analysis for the HIDiC and conventional columns are shown in Table 5. In this case, there are two IAE values reported. One IAE value corresponds to the IAE obtained from the PI controller of the rich component of the distillate while the other value corresponds to the IAE value determined for the PI controller of the rich component of the bottoms. As it is illustratively shown in Appendix C, for the case of HIDiC configurations, these results were obtained by evaluating several pairs of gain and integral time for the HIDiC configurations.

As it can be observed in Table 5, the values of the IAE for
the HIDiC sequences are larger than the IAE values for the conventional sequences for the Distillate product when this product is disturbed. In fact, the IAE of the HIDiC columns for some mixtures (M1, M2, M3 and M6) is one order of magnitude larger than the IAE values of the conventional sequences. In addition, the IAE value for the HIDiC (mixture M4) is two orders of magnitude larger than the conventional sequence. On the other side, notice that the IAE values for the HIDiC columns (mixtures M5 and M7) were larger but with equal order of magnitude as IAE values for the conventional columns. However, notice that IAE values for the conventional sequence (mixture M8) were three orders of magnitude lower than the IAE values for the HIDiC.

Moreover, the IAE values for the bottoms product (disturbed product) were larger for the HIDiC columns than the IAE values for the conventional columns. For instance, the IAE values for the HIDiC (M2 and M5) were larger but with the same order of magnitude as the conventional sequences, for their respective values of IAE. Likewise, the IAE values for the conventional sequences (mixtures M3, M4 and M6) were one order of magnitude lower than the IAE values for the HIDiC columns. However, IAE values with equal order of magnitude but slightly larger were determined for the conventional sequences (M1 and M7) compared with the IAE values for the HIDiC columns. It is important to note that the IAE value for the conventional sequence (mixture M8) was three orders of magnitude lower than the IAE values for the HIDiC, such as it was observed when the disturbance was applied on the Distillate product.

According to the results described under IAE criterion, the conventional sequences showed better dynamic performance than the HIDiC sequences for all case studies. This condition is also applied to the mixtures M1 and M7 due to that the respective total values of IAE (IAE of bottoms plus IAE of distillate) of the conventional configurations are lower than the respective total values of IAE of the HIDiC configurations.

Again, notice that the control properties of the conventional columns are considerably better than the HIDiC for the system with the lowest $\alpha$, M8 (mixture of xylenes).

On the other hand, Fig. 8 illustrates the typical behavior of the composition for the HIDiC configurations and their counterpart conventional columns for the mixtures M2 and M8. Notice that the conventional columns require less time to get the stabilization on the new setpoint produced with the disturbance. At the same time, the overshoots are less pronounced in the conventional sequences than in the HIDiC

Table 4 - Distribution of heat duty in the HIDiC columns.

|  |  | Stripping section |  | Rectifying section |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Mixture | QReb (kJ/h) | Qint. ${ }_{50}$ (kJ/h) | Qratio $_{50}$ | QCond. (kJ/h) | Qratio $_{85}$ |
| M1 | 1,454,545.06 | 3,776,723.96 | 0.278 | 1,798,572.10 | 0.323 |
| M2 | 1,431,414.88 | 8,059,422.56 | 0.151 | 2,018,985.00 | 0.200 |
| M3 | 1,534,376.91 | 7,074,605.05 | 0.180 | 1,978,934.10 | 0.219 |
| M4 | 1,043,286.64 | 15,026,765.10 | 0.065 | 2,165,327.10 | 0.126 |
| M5 | 16,941,201.86 | 22,464,730.30 | 0.430 | 18,525,041.00 | 0.452 |
| M6 | 3,984,716.82 | 38,770,314.10 | 0.093 | 6,185,164.00 | 0.138 |
| M7 | 9,304,639.36 | 37,761,710.40 | 0.198 | 11,210,541.00 | 0.229 |
| M8 | 1,017,917.75 | 129,315,322.00 | 0.008 | 9,339,536.50 | 0.067 |

Notice that Qratio $_{85}$ was computed considering that Qint. ${ }_{300}$ Qint. ${ }_{55}$

Table 5 - IAE values for HIDiC and conventional configurations.

|  |  | HIDiC | CONV |
| :--: | :--: | :--: | :--: |
| Mixture | Component | IAE |  |
| M1 | Benzene | 1.16E-03 | 2.65E-04 |
|  | Toluene | 1.62E-03 | 1.97E-03 |
| M2 | Toluene | 1.77E-03 | 1.77E-04 |
|  | Ethylbenzene | 1.47E-03 | 1.04 E-03 |
| M3 | Cyclohexane | 2.00E-03 | 2.07E-04 |
|  | n-Heptane | 1.06E-02 | 1.08E-03 |
| M4 | Isobutanol | 1.12E-02 | 1.64E-04 |
|  | n-Butanol | 2.31E-03 | 4.80E-04 |
| M5 | n-Octane | 6.49E-04 | 3.16E-04 |
|  | Ethylbenzene | 5.74E-04 | 3.05E-04 |
| M6 | Ethylbenzene | 1.69E-03 | 2.08E-04 |
|  | o-Xylene | 2.05E-03 | 7.16E-04 |
| M7 | 111-Trichloroethane | 8.14E-04 | 2.10E-04 |
|  | Benzene | 7.25E-04 | 8.81E-04 |
| M8 | m-Xylene | 1.42E-01 | 4.45E-04 |
|  | o-Xylene | 1.10E-01 | 7.58E-04 |

configurations, which lead them to lower IAE values. Observe also that the HIDiC sequence used to separate the mixture M8 ( $\alpha$ of 1.12) stabilizes on time values between 70 h and 100 h while the corresponding conventional columns require less than 1.5 h . Appendix D shows the behavior of composition and manipulated variables of the HIDiC and conventional columns for the other mixtures analyzed.

The behavior experienced by the manipulated variables is related with the effort made by the PI controller for settling the current composition over the setpoint generated by the disturbance applied. Therefore, the size of the changes experienced by the manipulated variables depends on the offset along the settling process. As it is expected, the largest offsets are observed at the beginning of the settling process, which continuously decrease as the process advances, until the settling is achieved and the setpoint is overlapped by the composition profile. However, it is noticed that there exist large changes of the manipulated variables at the beginning of the process. This phenomenon is identified in most HIDiC sequences and conventional configurations. This behavior reflects the relatively high difficulties experienced by the PI controller to track the behavior of the composition at the beginning of the settling process. Due to the fact that this behavior is experienced by both kinds of configurations, it is assumed that this phenomenon is the result of using high initial purities of the products and also, of course, due to the low $\alpha$ of the mixtures under study. Regarding this point, it is
important to underline that the separation of these kinds of mixtures with high purities of the products, by means of conventional sequences, is related with large reflux rates and large heat duties. Therefore, the initial actions of the PI controller tend to make abrupt changes trying to reach the setpoint since the first approximations. Nevertheless, as the settling proceeds, the feedback provided by the control loop reduces the variation of the manipulated variables. Moreover, although HIDiC configurations require both relatively low external reflux rates and heat duties in the optimized designs under steady state, the internal heat integration indirectly influences the size of the changes of the manipulated variable. That is, due to the fact that the PI controller does not have knowledge nor direct control on the internal liquid and vapor flows (produced by the internal heat integration), which implicitly contributes to the dynamics of the process, the single option for the PI controller is to produce large external reflux rates and heat duties pretending to reduce the offset. However, as the settling process advances, the PI controller modulates the changes of the manipulated variable through the feedback of the control loop until steady state is reached.

### 5.3. Analysis of results and their implications on the HIDiC

As it was described before, the best control properties were determined for the conventional columns. These results were consistent in both control analysis approaches (SVD and IAE). That is, the largest minimum singular values and lowest condition numbers and the minimum values of IAE were obtained for the conventional sequences for the mixtures along the range of $\alpha$ analyzed. Therefore, the concordance of these results supports the application of both approaches for determining the control properties of HIDiC and conventional configurations.

According with the results presented before, the largest minimum singular values and the lowest condition numbers were determined for the relative volatilities from 1.2 to 1.248 (mixtures M5-M7). The medium values for these parameters were obtained for the relative volatilities larger than 1.4 (mixtures M1-M4). However, in comparison with before cases, notice that considerably lower minimum singular values and considerably larger condition numbers were computed for $\alpha$ of 1.12 (mixture of xylenes, M8). Thus, the trend found under these criteria (condition numbers and minimum singular values) disclose that the best performance of the HIDiC configurations is obtained for the mixtures with $\alpha$ within an intermediate value of the range analyzed. As

![img-7.jpeg](img-7.jpeg)

Fig. 8 - Trend of the composition under closed-loop process analysis (IAE)-Case M2 and M8.
before, it is established due to that the HIDiC configurations with the best performance are those with the largest minimum singular values and lowest condition numbers. At the same time, the trend also disclose that worse control properties are found for the lowest $\alpha$ analyzed (1.12), mixture M8. It means that, in relation with the medium relative volatilities, as $\alpha$ is increased, the control difficulties are also
increased. This behavior is also observed for reductions in $\alpha$, however, the control difficulties are severely increased in this direction, which was shown for the system (M8) with $\alpha$ near to unity. Thus, in general terms, this behavior indicates that the largest control effort (if control is possible) must be directed to the separation of mixtures near the azeotropic behavior.

On the other hand, a similar analysis was performed for the IAE values along the $\alpha$ under study. In this case, a total IAE (IAE of the light component plus IAE of the heavy component) value was computed for each HIDiC column. As before, this analysis shows also that the best dynamic performance was determined for relative volatilities between 1.2 and 1.248. Besides, having this range as a reference, it is evidenced that worse control properties were determined for the mixtures with relative volatilities larger than 1.4. Notice also that the worst control properties were again obtained for $\alpha$ of 1.12 (mixture of xylenes). Interestingly, this analysis also revealed that the control properties for $\alpha$ of 1.23 were worse in comparison with the mixtures with $\alpha$ of 1.20 and the mixture with $\alpha$ of 1.248 . This trend is attributed to the interaction of the components of the mixture, which is also a mixture of isomers as the mixture M8. Although of course, in comparison with the mixture M8, the dynamic performance for the mixture M6 was better due to its larger $\alpha$.

These results reveal the sensitivity of the HIDiC column derived from its structural configuration and operative characteristics. This statement is established due to that the HIDiC columns are designed based on the CR between the stripping section and rectifying section, RR and TNS. From these variables, CR provides the major influence on the process. Thus, according to this CR, the temperature profiles are produced and the corresponding temperature driving forces between both sections are generated. At the same time, depending on the temperature driving forces, the amount of heat transferred from the rectifying section to the striping section is performed.

Hence, larger control difficulties and major control effort is expected for HIDiC configurations in comparison with the conventional columns. At the same time, it is assumed that when a disturbance takes place on these configurations, the temperature profiles of the columns (RS and SS) and the temperature driving forces between them become unstable and the heat transfer from RS to SS is disturbed.

In fact, depending on the size of the disturbance, temperature driving forces could be reduced considerably, causing a reduction in the heat transfer. So, the instability of the process is produced. In addition, although a new steadystate being reached under a disturbance, the results showed that the stabilization of the HIDiC configuration is more difficult than the stabilization for the conventional sequences.

Similarly, as it has been described in the background, the heat transfer can be distributed along the stages of the columns but there are some regions where the most favorable operation is obtained. Nonetheless, the perturbation on the columns could trigger changes in this condition and the most efficient operation condition could be lost.

On the other side, a more complicated operational condition could take place when the temperature driving force is inverted (negative temperature driving force). That is, the temperature of the rectifying section could be lower than the temperature of the stripping section, and a severe destabilization will be experienced. This situation could take place considering that the design and optimization of these configurations are based on the maximum heat transfer practically possible, such a way that only some Kelvin degrees are defined as the temperature driving forces to perform the heat transfer from the stages of RS to stages of SS. Therefore, the disturbances on highly sensitive stages could undergo this operative condition and the heat transfer will be inverted. Based on the operational principles of the HIDiC columns, this
behavior would be mainly influenced by CR. In fact, the major problem would be expected for configurations with too low CR.

At the same time, depending on the level of disturbance, the sizing of the heat transfer areas is affected due to that these heat transfer surfaces are computed using the temperature driving forces established in the process.

Thus, this study shows that the energetic efficiency of the HIDiC configurations must be complemented with the respective analysis of their control properties in order to determine the operative boundaries where large energetic efficiency and good dynamic performance are preserved. Hence, a robust control scheme must be assembled with control loops able to drive disturbances by adjusting the internal heat integration in an efficient way, keeping the compression requirements, water steam fed to the reboiler and cooling water fed to the condenser as low as possible.

In fact, according to the results obtained and considering the operational principles of HIDiC columns, it is suggested the analysis of an alternative control scheme in order to deal more directly with the influence of the internally produced vapor and liquid flows by the internal heat integration. The exploration of other control schemes is proposed due to the fact that the dynamic performance of HIDiC columns may be predominantly promoted by the heat transfer between stages of RS and stages of SS instead of the reboiler duty and condenser duty. So, the control actions performed by manipulating the reboiler duty and flow rate could not have enough effect on the controlled variables. Therefore, the control properties might be improved by the dynamic manipulating of CR as an additional process variable for driving disturbances.

Consequently, it is recommended to carry out the design and optimization of the HIDiC configurations considering simultaneously the dynamic behavior of the temperature profiles and the temperature driving forces in order to determine suitable operative ranges under the presence of disturbances.

In addition, it is important to underline that special attention must be directed to the systems with $\alpha$ near to 1.12 due to the dynamic performance determined in this work.

## 6. Conclusions

In this paper is presented the dynamic performance of the Heat-Integrated Distillation Columns (HIDiC) considering the effect of relative volatility of the mixtures. The dynamic performance was determined for the optimal HIDiC designs optimized in an earlier study using a constrained Boltzmannbased estimation of distribution algorithm. A set of equimolar binary mixtures whose $\alpha$ varies from 1.12 to 2.4 were used as case studies. The study was carried out using open and closed-loop process analysis.

The comparative analysis showed that the HIDiC columns experience worse control properties than the conventional configurations. In addition, it was also determined that the worst control properties were obtained for the HIDiC used to separate the mixture of xylenes, whose $\alpha$ is 1.12 .

At the same time, the novel findings disclosed in this paper show that despite the HIDiC sequences have worse dynamics than the conventional columns, these configurations were able to drive the disturbances and reach a stable dynamic behavior for all the range of $\alpha$ analyzed. Nevertheless, a high control effort was particularly found for the HIDiC configuration used to separate the mixture with $\alpha$

close to the azeotropic behavior (mixture of xylenes), which in fact, provides the largest energetic and economic benefits. Hence, at least in theoretical terms under the disturbances applied, the high energetic and economic potential of the HIDiC columns is not limited by the dynamic behavior for most case studies analyzed. However, such potential might be particularly reduced or unharnessed in the separation of the mixture with $\alpha$ near the azeotropic behavior due to the dynamics of the HIDiC column for this separation.

So, the main concern around the HIDiC configurations is to find an effective way to deal the disturbances and keep temperature feasible and stable driving forces to perform the heat transfer from RS to SS. In this sense, it is suggested that the implementation of a control scheme that uses CR as an additional manipulated dynamic variable could improve the dynamics of the HIDiC configurations. Through this control scheme the effect of the internal liquid and vapor flows on the control properties of the HIDiC columns would be considered, due to their relation with the internally integrated heat in this configuration.

At the same time, the results presented in this paper allow to infer that sequential or simultaneous dynamic studies must be performed along with the optimization of the HIDiC columns with the aim to determine the integral performance (energetic, economic and dynamic) of these configurations.

Finally, although this analysis was carried out using binary mixtures as case studies, the study of a considerable number of them has been achieved and some important mixtures of isomers were considered. Hence, the findings obtained provide some important remarks for guiding the searching for HIDiC designs with a dynamic behavior that allows to harness the large energetic and economic benefits for more complex HIDiC configurations, e.g. the separation of multicomponent mixtures.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Appendix A. Supporting information

Supplementary data associated with this article can be found in the online version at doi:10.1016/j.cherd.2023.01.032.

## References

Alcocer-García, H., Segovia-Hernández, J.G., Prado-Rubio, O.A., Sánchez-Ramírez, E., Quiroz-Ramírez, J.J., 2020. Multi-objective optimization of intensified processes for the purification of levulinic acid involving economic and environmental objectives. Part II: a comparative study of dynamic properties. Chem. Eng. Proc. 147, 107745. https://doi.org/10.1016/j.cep. 2019.107745

Baghmisheh, G., Shahrokhi, M., Bozorgmehri, R., 2010. Comparison of dynamic and static performances of a quaternary distillation sequence. Ind. Eng. Chem. Res. 49, 6135-6143. https://doi.org/10.1021/ie100169p
Bisgaard, T., Skogestad, S., Abildskov, J., Huusom, J.K., 2017. Optimal operation and stabilising control of the concentric heat-integrated distillation column (HIDiC. Comput. Chem. Eng. 96, 196-211. https://doi.org/10.1016/j.compchemeng. 2016. 09.020

Cabrera-Ruiz, J., Santaella, M.A., Alcántara-Ávila, J.R., SegoviaHernández, J.G., Hernández, S., 2017. Open-loop based controllability criterion applied to stochastic global optimization for intensified distillation sequences. Chem. Eng. Res. Des. 123, 165-179. https://doi.org/10.1016/j.cherd.2017.05.006
Cong, L., Chang, L., Liu, X., 2015. Development of extended generic model control for high-purity heat integrated distillation column using online concentration estimation. Ind. Eng. Chem. Res. 54 (51), 12897-12907. https://doi.org/10.1021/acs. iecr.5b03300
Cong, L., Liu, X., 2020. Temperature profile movement investigation and application to a control scheme with corrected set-point for a heat integrated distillation column. Chem. Eng. Proc. 147 (107710), 1-14. https://doi.org/10.1016/j. cep.2019.107710
Cong, L., Liu, X., Deng, X., Chen, H., 2019. Development of a partially accurate model and application to a reduced order control scheme for heat integrated distillation column. Sep. Pur. Tech. 229, 115809. https://doi.org/10.1016/j.seppur.2019. 115809
Cong, L., Liu, X.G., Wang, C.Y., 2014. Dynamic matrix control of a high-purity internal thermally coupled distillation column. Can. J. Chem. Eng. 92 (4), 696-702. https://doi.org/10.1002/cjce. 21867
Fang, J., Cheng, X., Li, Z., Li, C., 2019. A review of internally heat integrated distillation column. Chin. Chem. Eng. 27, 1272-1281. https://doi.org/10.1016/j.cjche.2018.08.021
Farias Neto, G.W., Carneiro, L.O., Vasconcelos, L.G.S., Brito, K.D., Brito, R., 2021. Pressure control of fully heat-integrated pres-sure-swing distillation system using hot-vapor bypass. Sep. Pur. Tech. 275, 119168. https://doi.org/10.1016/j.seppur.2021. 119168
Fu, Y., Liu, X., 2015. Nonlinear dynamic behaviors and control based on simulation of high-purity heat integrated air separation column. ISA Trans. 55, 145-153. https://doi.org/10. 1016/j.isatra.2014.11.006
Gabor, M., Mizsey, P., 2008. A Methodology to determine controllability indices in the frequency domain. Ind. Eng. Chem. Res. 47, 4807-4816. https://doi.org/10.1021/ie070952e
Gadalla, M., Jiménez, L., Olujić, Z., Jansens, P.J., 2007. A thermohydraulic approach to conceptual design of an internally heatintegrated distillation column (iHIDiC). Comput. Chem. Eng. 31, 1346-1354. https://doi.org/10.1016/j.compchemeng.2006. 11.006
Gutiérrez-Guerra, R., Cortez-González, J., Murrieta-Dueñas, R., Segovia-Hernández, J.G., Hernández, S., Hernández-Aguirre, A., 2014. Design and optimization of heat-integrated distillation column schemes through a new robust methodology coupled with a Boltzmann-based estimation of distribution algorithm. Ind. Eng. Chem. Res. 53, 11061-11073. https://doi. org/10.1021/ie500084w
Gutiérrez-Guerra, R., Murrieta-Duenas, R., Cortez-González, J., Segovia-Hernández, J.G., Hernández, S., Hernández-Aguirre, A., 2016. Design and optimization of HIDiC columns using a constrained Boltzmann-based estimation of distribution al-gorithm-evaluating the effect of relative volatility. Chem. Eng. Proc. 104, 29-42. https://doi.org/10.1016/j.cep.2016.02.004
Gutiérrez-Guerra, R., Murrieta-Duenas, R., Cortez-González, J., Segovia-Hernández, J.G., Hernández, S., Hernández-Aguirre, A., 2017. Design and optimization of heat-integrated distillation configurations with variable feed composition by using a Boltzmann-based estimation of distribution algorithm as optimizer. Chem. Eng. Res. Des. 12 4, 46-57. https://doi.org/10. 1016/j.cherd.2017.05.025
Häggblom, K.E., Waller, K.V., 1992. Control structures, consistency, and transformations. In: Luyben, W.L. (Ed.), Practical Distillation Control. Van Nostrand Reinhold, NY.
Harwardt, A., Kraemer, K., Marquardt, W., 2010. Identifying optimal mixture properties for HIDiC application. Distill. Absorpt. 2010, 55-60.
Huang, K.J., Wang, S.J., Iwakabe, K., Shan, L., Zhu, Q., 2007. Temperature control of an ideal heat-integrated distillation

column (HIDiC). Chem. Eng. Sci. 62 (22), 6486-6491. https://doi. org/10.1016/j.ces.2007.05.015
Iwakabe, K., Nakaiwa, M., Huang, K., Nakanishi, T., Resjorde, A., Ohmori, T., 2006. Performance of an internally heat-integrated distillation column (HIDiC) in separation of ternary mixtures. Chem. Eng. Jpn. 39, 417-425. https://doi.org/10.1252/jeej.39.417
Iana, A.K., Mali, S.V., 2010. Analysis and control of a partially heat integrated refinery debutanizer. Comput. Chem. Eng. 34, 1296-1305. https://doi.org/10.1016/j.compchemeng.2010.03. 002

Liang, J., Zhou, H., Li, J., Kong, W., Ma, Z., Sun, L., 2021. Comparison of dynamic performances for heat integrated reactive distillation considering safety. Chem. Eng. Proc. 160, 108294. https://doi.org/10.1016/j.cep.2020.108294

Liu, J., Liu, X., Li, J., Ren, J., Wang, J., Sun, L., 2022. Design and control of side-stream extractive distillation to separate acetic acid and cyclohexanone from wastewater by varying pressure. Proc. Saf. Environ. Prote 159, 1127-1149. https://doi.org/ 10.1016/j.psep.2022.01.064

Luyben, W.L., Yu, C.-C., 2008. Reactive Distillation Design and Control. John Wiley \& Sons, Inc, USA.
Marin-Gallego, M., Mizzi, B., Rouzineau, D., Gourdon, C., Meyer, M., 2022. Concentric heat integrated distillation column (HIDiC): a new specific packing design, characterization and pre-industrial pilot unit validation. Chem. Eng. Proc. 171, 108643. https://doi.org/10.1016/j.cep.2021.108643

Markowski, M., Trafczynski, M., Kisielewski, P., 2022. The dynamic model of a rectification heat exchanger using the concept of heat-integrated distillation column. Energy 256, 124622. https://doi.org/10.1016/j.energy.2022.124622

Meyer, K., Risgaard, T., Hunsom, J.K., Abildskov, J., 2017. Supervisory model predictive control of the heat integrated distillation column. IFAC-Pap. 50, 7375-7380. https://doi.org/ 10.1016/j.ifacol.2017.08.1506

Murrieta-Dueñas, R., Gutiérrez-Guerra, R., Segovia-Hernández, J.G., Hernández, S., 2011. Analysis of control properties of intensified distillation sequences: Reactive and extractive cases. Chem. Eng. Res. Des. 8 (9), 2215-2227. https://doi.org/10.1016/j. cherd.2011.02.021
Nakaiwa, M., Huang, K., Endo, A., Ohmori, T., Akiya, T., Takamatsu, T., 2003. Internally heat-integrated distillation columns: a review. Trans. IChemE 81, 162-177. https://doi.org/ 10.1205/026387603321158320

Nakaiwa, M., Huang, K., Owa, M., Akiya, T., Nakane, T., Takamatsu, T., 1998. Operating an ideal heat integrated distillation column with different control algorithms. Comput. Chem. Eng. 22, 5389-5393. https://doi.org/10.1016/S0098-1354(98)00079-9

Rix, A., Hecht, C., Paul, N., Schallenberg, J., 2019. Design of heatintegrated columns: Industrial practice. Chem. Eng. Res. Des. 147 (2019), 83-89. https://doi.org/10.1016/j.cherd.2019.05.009
Rodrigues, W.L., Mattedi, S., Abreu, J.C.N., 2005. Experimental vapor-liquid equilibria data for binary mixtures of xylene isomers. Chem. Eng. Braz. 22 (03), 453-462. https://doi.org/10. 1590/50104-66322005000300013
Schmal, J.P., De Rijke, A., Oluijic', Z., Jansens, P.J., 2006. Internal versus external heat integration operational and economic analysis. Chem. Eng. Res. Des. 84, 374-380. https://doi.org/10. 1205/cherd05041
Seader, J.D., Henley, E., 2006. Separation Process Principles. John Wiley and Sons.
Shahandeh, H., Ivakpour, J., Kasiri, N., 2014. Internal and external HIDiCs (heat integrated distillation columns) optimization by genetic algorithm. Energy 64, 875-886. https://doi.org/10.1016/ j.energy.2013.10.042

Shan, B., Niu, C., Meng, D., Zhao, Q., Ma, Y., Wang, Y., Zhang, F., Zhu, Z., 2021. Control of the azeotropic distillation process for separation of acetonitrile and water with and without heat integration. Chem. Eng. Proc. 165, 108451. https://doi.org/10. 1016/j.cep.2021.108451
Skogestad, S., Morari, M., 1988. Understanding the dynamic behavior of distillation columns. Ind. Eng. Chem. Res. 27, 1848-1862.
Stephanopoulos, G., 1984. Chemical Process Control: An Introduction to Theory and Practice. Prentice-Hall.
Suphanit, B., 2010. Design of internally heat-integrated distillation column (HIDiC): uniform heat transfer area versus uniform heat distribution. Energy 35, 1505-1514.
Turton, R., Bailie, R.C., Whiting, W.B., Shaeiwitz, J.A., 2004. Analysis Synthesis and Design of Chemical Process, second ed. Prentice Hall, USA.
Wakabayashi, T., Yoshitani, K., Takahashi, H., Hasebe, S., 2019. Verification of energy conservation for discretely heat integrated distillation column through commercial operation. Chem. Eng. Res. Des. 142, 1-12. https://doi.org/10.1016/j.cherd. 2018.11.031

Wang, Z., Qin, W., Yang, C., Wang, W., Xu, S., Gui, W., Sun, Y., Xie, D., Wang, Y., Lu, J., Chen, Q., Liu, X., 2020. Heat-transfer distribution optimization for the heat-integrated air separation column. Sep. Pur. Tech. 248, 117048. https://doi.org/10.1016/j. seppur.2020.117048
Yu, Z., Liu, X.G., 2005. Dynamics and control of high purity heat integrated distillation columns. Ind. Eng. Chem. Res. 44 (23), 8806-8814. https://doi.org/10.1021/ie050141f
Zhang, Q., Liu, M., Li, C., Zeng, A., 2018. Design and control of extractive distillation process for separation of the minimumboiling azeotrope ethyl-acetate and ethanol. Chem. Eng. Res. Des. 136, 57-70. https://doi.org/10.1016/j.cherd.2018.04.043