# Damage identification of single-layer cylindrical latticed shells based on the model updating technique 

Ying Xu ${ }^{1,2} \cdot$ Yongzhi Pan ${ }^{2} \cdot$ Ying Wang ${ }^{3,4} \cdot$ Dandan Deng ${ }^{2} \cdot$ Qinghua Han ${ }^{1,2}(D)$

Received: 13 May 2021 / Revised: 28 November 2021 / Accepted: 29 November 2021 / Published online: 22 January 2022
(c) Springer-Verlag GmbH Germany, part of Springer Nature 2021


#### Abstract

Large-span spatial structures have closely spaced frequencies and complex vibration modes. The traditional methods based on static responses or dynamic parameters are difficult to identify the multi-damage locations and severities in large-span spatial structures. Moreover, with a large number of structural members and a limited number of sensors, finite element (FE) model updating is especially challenging for spatial structures. In this work, a structural damage identification (SDI) framework based on the estimation of distribution algorithm (EDA) is proposed and applied to the damage identification of a single-layer cylindrical latticed shell. Numerical simulations and laboratory tests are performed. The results demonstrate the effectiveness of the proposed damage identification algorithm. Only four accelerometer locations from 38 available points are used to identify the damage of the test structure with 83 members. The average identification accuracy using FE data reaches $90 \%$ by considering multiple damage conditions and noise interference. Based on the laboratory data, the average identification accuracy is over $82 \%$ considering different damage levels of a single member. The results demonstrate that the EDA-based framework can effectively improve the optimization process in the parameter identification problem, which is applicable to the damage identification of large-span spatial structures.


Keywords Damage identification $\cdot$ Single-layer cylindrical latticed shell $\cdot$ Model updating $\cdot$ Estimation of distribution algorithm (EDA) $\cdot$ Modal assurance criterion (MAC)

## 1 Introduction

In recent years, the structural health monitoring (SHM) technique has become widely used in large-span spatial structures to preserve public infrastructures and reduce maintenance costs. Bao et al. carried out field tests on the National Aquatics Center in Beijing to validate the proposed approach of compressive sampling-based data loss recovery

[^0][1]. Zhang et al. proposed an interpolation method for missing stress data based on long-term monitoring data of the steel structure of the Hangzhou Olympic Center stadium [2]. It has been found that the SHM systems established in largespan spatial structures have become integrated, systematized and intellectualized.

As the most critical component of SHM, structural damage identification (SDI) is a systematic and automatic process of identifying the existence of damage and subsequently localizing and assessing its severity [3]. At present, SDI methods include static methods based on structural responses such as displacements and strains and dynamic methods based on vibration responses. Vibration-based methods are more common since they can cover comprehensive structural responses [4-6]. A comprehensive review of modal parameter-based damage identification methods for beam- or plate-type structures is presented by Fan et al. [7].

The SDI of large-span spatial structures is more difficult than that of 3D frame structures [8, 9] because of the large number of components, complex degrees of freedom, and serious mode localization and transitions. Moreover,


[^0]:    Qinghua Han qhhan@tju.edu.cn

    1 Key Laboratory of Coast Civil Structure Safety of China, Ministry of Education, Tianjin University, Tianjin 300350, China
    2 School of Civil Engineering, Tianjin University, Tianjin 300350, China
    3 School of Civil and Environmental Engineering, Harbin Institute of Technology (Shenzhen), Guangdong 518055, China
    4 Department of Civil and Environmental Engineering, University of Surrey, Guildford GU2 7XH, UK

large-span spatial structures may experience different types of damages during their entire life circles, such as cracking, loosening of bolts, corrosion, member flaws and fatigue. In recent years, many studies concentrated on the nondestructive evaluation of structures considering different damage types. Zhang et al. proposed a novel deep convolutional neural network, namely, SHMnet, for monitoring the conditions of bolted connections in steel structures [10]. Ozevin et al. proposed a new source localization methodology to identify the spatial locations of active flaws on spaced structures using the acoustic emission (AE) method [11]. Sodano et al. developed an automated eddy current sensor that can identify both corrosion and damage in the form of a small hole well outside the sensor's footprint [12]. The above SDI methods were demonstrated to be effective and automated. However, all these methods are concerned with a single damaged component with a specific damage form and thus are not applicable to large-span spatial structures since the joints or members must be individually monitored to obtain the global structural condition.

To solve the above problems, the combination of ambient vibration tests and model updating technique was proposed as a valuable tool for indirect non-invasive SDI of engineering structures [13]. The vibration signals mainly include the frequency-domain parameters and time-domain parameters. The combination of modal parameters in the frequency domain can be used to identify the severity and location of damage with good accuracy since the modal parameters contain both global and local information [14]. Li et al. [15] proposed a two-step damage detection method for large and complex structures based on model updating and modal flexibility curvature differences. Hao et al. [16] established three criteria, namely, frequency changes, modal shape changes and a combination of the two, to realize vibration-based damage detection in a cantilever beam and a frame. Masoumi et al. [17] proposed an objective function formed by modal parameters to solve the inverse problem of damage identification with the help of the imperialist competitive algorithm (ICA) optimization. Sun et al. [18] proposed a three-step damage identification method based on dynamic characteristics in which the frequency and difference of modal curvature (DMC) are used as damage indexes. Most of the above studies used the model updating technique to identify structural damage by minimizing the objective function by intelligent algorithms, namely the optimization process in SHM. Moreover, Rainieri et al. [13] proposed the model optimization method concerning the rational choices of updating parameters and objective functions for seismic assessment of heritage structures.

With increasing computing power and improvements in sensing technology in the last decade, machine learning (ML), especially deep learning (DL) algorithms, has become more feasible and extensively used in vibration-based structural damage detection [19]. A wavelet-domain response reconstruction technique was used for the damage identification of a substructure [20]. Guo et al. designed a new network architecture using a convolutional neural network (CNN) algorithm to extract damage features at different scales and reduce interference from noise-contaminated data [21]. Zhang et al. proposed a data-driven multilabel classification (MLC) method to locate multisite structural damage in frame structures [22].

In particular, the genetic algorithm (GA) is widely used in vibration signal-based SDI problems [16]. However, the shortcomings of the GA-based damage identification method include the following: (1) complex operations of selection, crossover and mutation of the genes, which lead to a slow convergence rate; (2) difficulty in determining the termination criteria; and (3) a poor local search ability. Therefore, a population evolutionary algorithm based on statistical learning theory is proposed to overcome these drawbacks: the estimation of distribution algorithm (EDA) [23]. In the EDA, new individuals are created by sampling from the probabilistic distribution instead of crossover and mutation operators. Due to the flexibility of choosing suitable probabilistic models, the probabilistic model used by the EDA can represent prior information about the structure of the problem, which enables a more efficient search for the optimal solution [24]. In addition, compared with other algorithms, EDA can provide not only the updated parameters but also the statistics of every objective and variable in each generation [25]. This can further provide the confidence level of the updated results, which becomes the unique advantage of EDA [26].

The target of this work is to identify the severity and locations of damage in the members of large-span spatial structures using the EDA-based model updating technique. The objective function is established based on the modal parameters, including the natural frequency and mode shape. Then, the EDA-based damage identification method is demonstrated by both numerical simulations and laboratory tests on a cylindrical latticed shell model. The tolerance of the proposed method is tested by considering multiple damage scenarios, include the damage location, damage severity, number of damaged members and noise interference.

## 2 EDA-based damage identification framework

### 2.1 EDA-based model updating

Large-span spatial structures have closely spaced frequencies and complex vibration modes. Thus, it is difficult for traditional damage identification methods based on static responses or dynamic parameters to identify the local

damage of structural members. Therefore, a model updating technique is adopted to identify the locations and severity of damage in the members of large-span spatial structures.

The model updating process includes three key components: updating parameters, objective functions and an optimization algorithm [23]. The model updating process can be summarized as updating the specified parameters to gradually approach their true values by maximizing or minimizing the value of the objective function, and the whole process is completed through the optimization algorithm.

In this study, an evolutionary optimization algorithm, the EDA, is adopted to realize the model updating in the Mateda-2.0 software [25]. The flowchart of the EDA-based model update is shown in Fig. 1.

The core of the EDA is to establish a probability model that describes the distribution of solutions in the learning and sampling process: estimate and learn the probability distribution of the good individuals in the previous generation, subsequently remove the ineffective individuals, generate the new individuals in the next generation based on the probability model, and repeat the evolutionary iteration until the optimal solution is found. In Mateda-2.0, the available probabilistic models include Bayesian networks, Gaussian networks and Markov networks [25], etc. In a Bayesian or Markov network, the variables are discretely distributed. In a Gaussian network, each variable is continuous and each local density function is the linear regression model. Therefore, the Gaussian network model is selected as the probability model in this study due to its adaptability in the damage severity identification problem [24, 26]. The EDA has a strong learning ability and evolutionary orientation and can
![img-0.jpeg](img-0.jpeg)

Fig. 1 Flowchart of the EDA-based model updating
effectively improve the global optimization ability compared with other intelligent algorithms.

### 2.2 EDA-based damage identification algorithm

In this study, the reduction rate (damage coefficient) of a member section area, $\alpha$, is introduced and defined as the updating parameter, which can reflect the damage severity of structural members. Moreover, three objective functions that can reflect the proximity between the updating model and the real model are derived from the damage-sensitive features:
$J_{1}=\frac{1}{\sum_{i=1}^{m}\left(\frac{f_{i a}-f_{a i}}{f_{a i}}\right)^{2}}$
$J_{2}=\frac{1}{\sum_{i=1}^{m} \sum_{j=1}^{m}\left(\frac{\Phi_{i j} \Phi_{j i}^{T}}{f_{a i}^{T}}-\frac{\Phi_{i j} \Phi_{j j}^{T}}{f_{a i}^{T}}\right)^{2}}$
$J_{3}=J_{1}+\frac{J_{2}}{w}$
where $f_{i}$ represents the $i$ th natural frequency; $\boldsymbol{\Phi}_{i}$ and $\boldsymbol{\Phi}_{j}$ represent the $i$ th and $j$ th mode shapes (displacement normalized), $m$ is the number of modes, and $a$ and $e$ are the analytical and experimental results, respectively.

As shown in Eq. (3), $J_{3}$ is the combination of $J_{1}$ and $J_{2}$, while $w$ is a weighting parameter to match the magnitudes of $J_{1}$ and $J_{2}$. In this study, $J_{3}$ is selected as the final objective function since it can simultaneously consider the influences of the natural frequency and mode shape. The determination method of $w$ will be further described in the following numerical study cases. The termination condition of the model updating is set as $J_{3}$ reaching a maximum value (generally larger than $1 \times 10^{10}$ to achieve the accuracy requirements, which is set as $1 \times 10^{14}$ in this study), or the iterative process reaching the specified generation (should be large enough to guarantee the convergence of iterative results, which is taken as 150 in this study).

## 3 Numerical simulations of the single-layer cylindrical latticed shell

### 3.1 Numerical model

A single-layer cylindrical latticed shell is a typical grid form in spatial structures. Therefore, it was taken as the representative example to evaluate the practicability of the EDA-based model updating technique in the damage identification of large-span spatial structures. The FE model

Fig. 2 Numbers of members and nodes

![img-1.jpeg](img-1.jpeg)

Table 1 Geometric and material parameters of the members

| Member section $h \times b \times t$ (mm) | Density $\left(\mathrm{kg} / \mathrm{m}^{3}\right)$ | Elastic modulus (GPa) | Poisson's ratio | Yield strength (MPa) | Ultimate strength (MPa) |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $30 \times 50 \times 1.5$ | 7850 | 207.35 | 0.3 | 369.25 | 488.85 |

Table 2 Damage severity of members corresponding to multiple damage conditions

| Scenarios | Damaged <br> member | Damage coefficient $\alpha$ | Noise |
| :-- | :-- | :-- | :-- |
| MS-1 | 5 | 0.8 | - |
| MS-2 | 5 | 0.5 | - |
| MS-3 | 5,21 | $0.5(5), 0.8(21)$ | - |
| MS-4 | 5,21 | $0.5(5), 0.8(21)$ | $10 \%$ |

of a three-way single-layer cylindrical latticed shell was established in ANSYS, as shown in Fig. 2. The length of the shell model is 6 m , and the span is 4.5 m . The geometric parameters of the FE model and coordinates of the joints are consistent with the following test model for further comparison. The shell model is composed of 83 members and 38 nodes, which is supported on the longitudinal sides through fixed hinge supports. All the members were modelled by the beam element BEAM188. The joint system was assumed to be rigid for simplification. It is worth mentioning that, this assumption is only applicable for the numerical test case. However, for the physical test case, this assumption may lead to inconsistency between the FE model and physical model, since most fabricated joint systems in spatial structures are semi-rigid joints. In this condition, a pre-model updating is necessary to calibrate the initial FE model before damage identification. The bilinear constitutive model of the material was adopted in FEA according to the coupon test results shown in Table 1. The numbers of members and nodes are also shown in Fig. 2.

### 3.2 Introduction of multiple damage conditions

The single-layer cylindrical latticed shells are typical statically indeterminate structures. The temperature effect may have a great effect on the dynamic characteristics. To minimize the influence of temperature, a constant temperature environment was selected for both the numerical test case and physical test case. To simulate multiple damage conditions in practice, four damage scenarios were designed in the numerical simulations. The damaged members were randomly selected. As shown in Table 2, a single damaged member with different damage coefficients was considered in MS-1 and MS-2. Then, two members with different damage coefficients were considered in MS-3. In the last scenario MS-4, the model was updated based on noise-corrupted data: $10 \%$ uniformly distributed noise was introduced into the modal analysis results.

Modal analysis was first conducted on the intact FE model in ANSYS. Then, different damage conditions were introduced. The natural frequencies and mode shapes obtained by modal analysis were substituted into the objective function

as the true values. Thereafter, the damage coefficients of members were updated using the EDA. The effectiveness of the algorithm will be verified by comparing the updating results and real structural damage.

It is worth mentioning that, a trial calculation was conducted in advance to determine the weighting parameter $w$ based on the values of $J_{1}$ and $J_{2}$. The results are shown in Table 3. It is found that, $J_{2}$ is much larger than $J_{1}$ at the beginning of model updating. Then $J_{1}$ will gradually increase to the maximum value after 20 generations (different by scenarios) and far larger than $J_{2}$ after 80 generations. It is indicated that $J_{2}$ plays a dominant role at the first beginning of model updating. The value of $w$ in the first 10 generations will directly determine the convenience rate of the updating process. As shown in Table 3, the ratio of $J_{2}$ to $J_{1}$ is in the range of 40 to 95 in the first 10 generations. Therefore, the weighting parameter $w$ is set to be an average value of 60 in MS-1 to MS-4 to match the magnitudes of $J_{1}$ and $J_{2}$.

As described previously, the reduction rates of member section areas, $\alpha$, were defined as the updating parameters. In this study, each member is simulated by a beam element. Therefore, the number of updating parameters is equal to that of the members, which is 83 in total. The original values of $\alpha$ are set to be 1.0 for all the members. Thereafter, the selected parameters are updated using the EDA. According to the preliminary numerical simulation results, the displacement modes in the $X$ direction are much smaller than the displacement modes in the $Y$ and $Z$ directions. To improve the calculation efficiency, only the displacement modes in the $Y$ and $Z$ directions were used for model updating.

Four model updates were conducted to identify the locations and severity of structural damage corresponding to MS-1 to MS-4. The natural frequencies of the FE model before and after model updating are compared in Table 4. Both the true values and the updating results of the natural frequencies decrease with the number of model updates, which show a decrease in structural rigidity. For MS-1 to MS-3, the error of the natural frequency is $0.3-4.0 \%$; when considering noise interference, the error of the natural frequency is $2.3-3.6 \%$. The true values fit well with the model updating results.

The modal assurance criterion (MAC) is commonly used to measure the similarity between two mode shapes. The off-diagonal elements of the MAC matrix represent the intersection angle of the corresponding modal vectors. Two mode shapes will be considered identical when the diagonal elements approach one while the off-diagonal elements of the MAC matrix approach zero. The MAC matrices for different damage scenarios are shown in Fig. 3. The diagonal elements are $0.98-1.00$ and the off-diagonal elements are all equal to zero. The mode shape obtained by modal analysis (considered the true value) is identical to the model updating result in most scenarios.

### 3.3 Discussion of the damage identification results

The damage identification results obtained from the EDAbased model update are shown in Fig. 4 and the members with lower damage coefficients were extracted in Table 5. In MS-1 and MS-2, Member 5 is the real damaged member.

Table 3 Values of $J_{1}$ and $J_{2}$ in 100 generations during model updating

| Number of generations | MS-1 |  | MS-2 |  | MS-3 |  | MS-4 |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $J_{1}$ | $J_{2}\left(\times 10^{3}\right)$ | $J_{1}$ | $J_{2}\left(\times 10^{3}\right)$ | $J_{1}$ | $J_{2}\left(\times 10^{3}\right)$ | $J_{1}$ | $J_{2}\left(\times 10^{3}\right)$ |
| 1 | 861.94 | 37.33 | 41.94 | 3.36 | 41.89 | 3.30 | 40.61 | 3.23 |
| 5 | $1.42 \times 10^{3}$ | 88.54 | 59.12 | 4.00 | 35.94 | 2.88 | 48.57 | 3.84 |
| 10 | $1.09 \times 10^{4}$ | 196.23 | $1.32 \times 10^{3}$ | 16.28 | 73.47 | 8.52 | 54.44 | 6.32 |
| 15 | $2.09 \times 10^{13}$ | 61.61 | $4.11 \times 10^{6}$ | 36.83 | 80.35 | 5.47 | 69.81 | 8.93 |
| 20 | $1.03 \times 10^{14}$ | 56.15 | $7.23 \times 10^{13}$ | 0.83 | 97.52 | 9.63 | 121.59 | 15.49 |
| 50 | $2.92 \times 10^{19}$ | 55.98 | $7.23 \times 10^{13}$ | 0.83 | $1.85 \times 10^{3}$ | 81.26 | $1.24 \times 10^{3}$ | 64.51 |
| 80 | $2.92 \times 10^{19}$ | 55.98 | $7.23 \times 10^{13}$ | 0.83 | $5.28 \times 10^{19}$ | 16.68 | $8.63 \times 10^{18}$ | 14.14 |
| 100 | $2.92 \times 10^{19}$ | 55.98 | $7.23 \times 10^{13}$ | 0.83 | $5.28 \times 10^{19}$ | 16.68 | $8.63 \times 10^{18}$ | 14.14 |

Table 4 Natural frequencies corresponding to multiple damage conditions (Hz)

| Order | Initial state | MS-1 |  | MS-2 |  | MS-3 |  | MS-4 |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  |  | True value | Updating result | True value | Updating result | True value | Updating result | True value | Updating result |
| 1st | 15.116 | 15.092 | 15.046 | 15.067 | 14.965 | 15.041 | 14.881 | 14.249 | 14.767 |
| 2nd | 29.026 | 28.968 | 28.557 | 28.888 | 27.733 | 28.806 | 28.088 | 28.584 | 27.800 |
| 3rd | 34.339 | 34.238 | 34.598 | 34.122 | 33.665 | 34.105 | 34.559 | 34.872 | 34.083 |

Fig. 3 MAC matrices between the true value and the updating result (numerical study)
![img-2.jpeg](img-2.jpeg)

As shown in Table 5, Member 5 was correctly identified as the damaged member with the lowest damage coefficient. The errors of the damage coefficient are $0.7 \%$ and $1.3 \%$ compared with the true values. In MS-1, the other identified members with low damage coefficients include adjacent Members 11 and 12 and support Members 43. In MS-2, the damage coefficient of Member 5 is correctly identified and much lower than those of the adjacent members and support members. The EDA-based damage identification framework shows good performance for single-damage cases. The variation in the updating factors during single-damage identification is shown in Fig. 5. The updating results stabilized after 25 generations. The updating process shows good reliability and stability (Fig. 5).

In MS-3 and MS-4, Members 5 and 21 are the real damaged members and have different damage severities. As shown in Table 5, both the location and the severity of damage in the two members were correctly identified, even with the noise-corrupted data. The errors of the damage coefficients of the two members are less than $7 \%$. The
other identified members with low damage coefficients are the members adjacent to the real damaged members and support members. Since Members 5, 67 and 68 are both diagonal members connected with Node 7, Members 67 and 68 were misidentified as the damaged members. The variation in the updating factors during the multi-damage identification scenarios is shown in Fig. 6. The updating results stabilized after 75 generations. MS-3 has a faster convergence rate than MS-4.

The statistics of the damage identification accuracies of all structural members in the last generation are listed in Table 6. The damage identification accuracy of a single member is defined as follows:

ACC $=\left|\frac{\alpha_{\mathrm{id}}}{\alpha_{\text {real }}}\right| \times 100 \%$
where $\alpha_{\mathrm{id}}$ is the identified damage coefficient and $\alpha_{\text {real }}$ is the real damage coefficient. The average identification accuracy is larger than $90 \%$, even considering multiple damage conditions and noise interference. The mean value

![img-3.jpeg](img-3.jpeg)

Fig. 4 The damage identification results obtained from the EDA-based model updating (numerical study)
of the identification accuracies decreased by approximately $1.9 \%$ when $10 \%$ noise was introduced.

The results also show that the identification accuracies decreased with both the number of damaged members and the damage severity. The main reason is that the objective function is highly related to the displacement modes of the shell model. An increase in the number of damaged
members or damage severity will significantly change the displacement modes of the adjacent nodes. As a result, more adjacent members will be misidentified with heavier member damages.

## 4 Physical tests on a single-layer cylindrical latticed shell

### 4.1 Test model

Physical tests on a single-layer cylindrical latticed shell were further conducted to evaluate the practicability of the EDA-based model updating technique. As shown in Fig. 7, the geometrical parameters of the test model are consistent with the FE model introduced in Sect. 3.1. All members are S235JR rectangular steel tubes, and the assembled hub joints were selected as the joint system [27]. The coordinates of joints were measured by a three-dimensional laser scanner before the test to reduce geometric errors between the test model and the numerical model.

### 4.2 Test procedure and equipment

The objective of the model test is to obtain the first three orders of the natural frequencies and mode shapes of the intact shell and damaged shell for further model updating. The above vibration responses were acquired by force hammer excitation.

The sensing system is composed of eight unidirectional ICP accelerometers, an intelligent data-collecting device (INV3062S3) and a matching hammer (INV9312), as shown in Fig. 8. The above sensing system is provided by the COINV company in China. The sampling frequency of the force hammer is 10 kHz , and the sampling frequency of the accelerators is 312.5 Hz .

Eight accelerometers (marked red in Fig. 2) were arranged at nodes $33,35,36$ and 38 in both the $Y$ and the $Z$ directions. This arrangement scheme of measuring points was determined based on the modal strain energy criterion [28, 29], which was realized by the EDA-based sensor optimization algorithm. Since the optimal sensor placement in a large-span spatial structure is beyond the scope of this article, the EDA-based sensor optimization algorithm will be introduced in our other works.

To obtain the complete mode shapes based on limited measuring points of accelerations, the impact hammer tests were conducted on each node of the latticed shell. In addition, the hammer tests were repeated three times at each node to obtain reliable vibration responses. Thereafter, both the acceleration and force signals were imported into the commercial software ARTeMIS Model for experimental modal analysis.

Table 5 Members with low damage coefficients during model updating

| MS-1 |  | MS-2 |  | MS-3 |  | MS-4 |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Member | $\alpha$ | Member | $\alpha$ | Member | $\alpha$ | Member | $\alpha$ |
| 5 | 0.7939 | 5 | 0.4937 | 5 | 0.4659 | 5 | 0.4891 |
| 51 | 0.8258 | 58 | 0.6202 | 67 | 0.6096 | 21 | 0.7174 |
| 12 | 0.8428 | 25 | 0.6992 | 68 | 0.6990 | 6 | 0.7371 |
| 11 | 0.8521 | 1 | 0.7095 | 60 | 0.7655 | 60 | 0.7869 |
| 43 | 0.8585 | 63 | 0.7514 | 21 | 0.8358 | 71 | 0.8557 |

![img-4.jpeg](img-4.jpeg)

Fig. 5 Variation in the updating factors during single-damage identification (numerical study)

The vibration test was first carried out on the intact shell model, which was denoted scenario MT-1. The time histories of the impact load and acceleration responses during the impact hammer test on Node 13 are shown in Fig. 9.
![img-5.jpeg](img-5.jpeg)

Fig. 6 Variation in the updating factors during multi-damage identification (numerical study)

Considering the subsequent use of the test model, only one damaged member was introduced in the test. Since it is a fabricated latticed shell, the damaged member can be replaced after the test. Three levels of damage severity were successively introduced at the mid-span of Member

Table 6 Statistics of the damage identification accuracies based on the FE data

| Scenarios | Maximum <br> value (\%) | Minimum <br> value (\%) | Mean value (\%) | Standard <br> deviation <br> $\left(\times 10^{-19}\right)$ |
| :-- | :--: | :--: | :--: | :--: |
| MS-1 | 100.00 | 82.58 | 95.37 | 6.64 |
| MS-2 | 99.79 | 62.02 | 92.51 | 5.33 |
| MS-3 | 99.65 | 60.96 | 92.43 | 1.27 |
| MS-4 | 99.10 | 73.71 | 90.54 | 3.13 |

![img-12.jpeg](img-12.jpeg)

Fig. 7 The single-layer cylindrical latticed shell model

Fig. 8 Composition of the sensing system
![img-7.jpeg](img-7.jpeg)
(a) ICP accelerometer
![img-8.jpeg](img-8.jpeg)
(b) Intelligent data-collecting device
![img-9.jpeg](img-9.jpeg)
(c) Hammer
![img-10.jpeg](img-10.jpeg)
(a) Impact load
![img-11.jpeg](img-11.jpeg)
(b) Accelerations in Y direction
![img-12.jpeg](img-12.jpeg)
(c) Accelerations in the Z direction

Fig. 9 The time histories of impact load and accelerations (MT-1)

Table 7 Damage severity of members in different test scenarios

| Scenarios | Damage level | Cutting depth/ <br> member height | Damage <br> coefficient <br> $\alpha$ |
| :-- | :-- | :-- | :-- |
| MT-1 | - | 0 | 1.00 |
| MT-2 | Slight | $1 / 4$ | 0.66 |
| MT-3 | Medium | $1 / 2$ | 0.50 |
| MT-4 | Heavy | $3 / 4$ | 0.34 |

### 4.4 Model updating based on the laboratory data

The above modal analysis results will be used for model updating as true values. The effectiveness of the algorithm will be verified by comparing the updating results with the real structural damage. Similar to the model updating process described in Sect. 3.2, the original FE model of the cylindrical latticed shell was established in ANSYS. The damage coefficients of 83 members were selected as the updating parameters, and the original values of the damage coefficient $\alpha$ were set to be 1.0 for all members. The determining method of $w$ is similar to the numerical study cases. Then, the selected parameters were updated using the EDA. The procedure and objective function of EDA were introduced in Sect. 2.

The model was updated four times. The first model updating process was performed to calibrate the initial FE model before damage identification, to eliminate the influence of the rigid-joint assumption. After the first model update, the error of the natural frequencies between the FE model and test model is reduced to only $2 \%$, which indicates that the dynamic characteristics of the calibrated model are consistent with those of the real test model. The second to fourth model updating processes were performed to identify the locations and severity of damage corresponding to MT-2 to MT-4. The natural frequencies of the analytical model before and after model updating are shown in Table 9.

As shown in Table 9, the natural frequencies of the FE model decline with the number of model updates, showing the decrease in structural rigidity. This observation is consistent with the test measurements in Table 8. The error of the natural frequencies obtained from the EDA-based model updating framework increases with the number of model updates. The maximum error is less than $15 \%$ compared with the test results. The errors of natural frequencies may
![img-13.jpeg](img-13.jpeg)

Fig. 10 The time histories of impact load and accelerations (MT-2)
![img-14.jpeg](img-14.jpeg)

Fig. 11 The time histories of impact load and accelerations (MT-3)

![img-15.jpeg](img-15.jpeg)

Fig. 12 The time histories of impact load and accelerations (MT-4)

Table 8 Natural frequencies of the shell model obtained by ARTeMIS Model

| Scenarios | Frequencies $(\mathrm{Hz})$ |  |  |
| :-- | :-- | :-- | :-- |
|  | 1st order | 2nd order | 3rd order |
| MT-1 | 10.946 | 20.535 | 22.300 |
| MT-2 | 10.946 | 20.535 | 22.300 |
| MT-3 | 10.944 | 20.536 | 22.301 |
| MT-4 | 10.876 | 20.486 | 22.227 |

result from several reasons, such as maximum number of iterations limited by computer hardware, efficiency of the objective function, number of updating parameters, limitation of the SDI method based on frequency-domain parameters, uncertainty assumption of the FE model and noise interference, etc.

The MAC matrices between the intact structure and different damage scenarios are shown in Fig. 16. The first model updating result was compared with the initial FE model, and the other model updating results were compared
![img-16.jpeg](img-16.jpeg)

Fig. 13 Mode shapes of MT-1
![img-17.jpeg](img-17.jpeg)

Fig. 14 Mode shapes of MT-3

![img-18.jpeg](img-18.jpeg)

Fig. 15 Mode shapes of MT-4

Table 9 Natural frequencies of the analytical model obtained by model updating $(\mathrm{Hz})$

| Scenarios | Frequencies (Hz) |  |  |
| :-- | :--: | :-- | :-- |
|  | 1st order | 2nd order | 3rd order |
| MT-1 | 10.638 | 20.559 | 24.450 |
| MT-2 | 10.200 | 19.735 | 23.205 |
| MT-3 | 9.941 | 18.792 | 24.076 |
| MT-4 | 9.304 | 18.238 | 21.658 |

with the corrected FE model. The MAC matrices based on the laboratory data are not as ideal as the MAC matrices shown in Fig. 3. For each damage scenario, the difference between the two mode shapes was the result of both the aggravation of cumulative damage and the difference in the model updating accuracy.

### 4.5 Discussion of the damage identification results

The damage identification results obtained from the EDAbased model updating technique are shown in Fig. 17. The updating results show that Member 2 and the adjacent members have relatively low damage coefficients.

In Scenario MT-2, the damage coefficients of Members 2,7 and 50 were identified as $0.7144,0.7046$, and 0.7051 , respectively. However, as introduced in the test setup, only Member 2 is the real damaged member, and the damage coefficient is equal to 0.66 . Moreover, Member 37 near the hinge support was also identified as a damaged member, which is incorrect. Overall, the model updating technique can identify generally damaged areas when slight damage occurs to a single member. However, additional inspection should be conducted to precisely locate the damage.

In Scenario MT-3, Members 2, 3 and 7 were identified as the damaged members with damage coefficients below 0.65. Member 2 has the lowest damage coefficient ( 0.4578 ), as shown in Fig. 17b. The error of the damage coefficients between the model updating result and the real value is $8.4 \%$.

In this scenario, the model updating technique successfully identified the damage location, and the identification error of the damage severity was acceptable.

In Scenario MT-4, the real damaged member was also identified with a damage coefficient of 0.4578 . By contrast, the damage coefficients of the adjacent members were $0.55-0.70$, which are much lower than those in Scenario MT-3.

In summary, the model updating technique can identify different levels of member damage based on the vibration responses of the test model. Although the error of the damage coefficients is not negligible, the updating results can correctly reflect the damage severity of the damaged member. The errors are mainly concentrated in the members near the real damaged member and the support members. The identification errors can result from several factors, such as limitation of the SDI method based on frequency-domain parameters, uncertainty assumption of the FE model and noise interference, etc.

The variations in the updating factors versus the number of generations for five selected members are shown in Fig. 18. Member 2 is the real damaged member, and Members $1,3,7,8$ are the surrounding diagonals. Dramatic fluctuation of the updating factors was observed at the beginning of model updating. Then, the updating factors gradually stabilized and converged after 80,100 and 110 generations for different levels of damage, which shows the stability of the updating results.

The damage identification accuracies of all 83 members in the last generation are listed in Table 10. The average identification accuracy is larger than $82 \%$ considering different damage levels of a single member. As shown in Table 10, the identification accuracies decrease with the severity of member damage since the objective function is highly related to the displacement modes of the shell model. As shown in Figs. 13, 14 and 15, the displacement modes are sensitive to the local damage of Member 2. Moreover, an increase in damage severity causes significant variation in the displacement modes of the adjacent nodes. As a result,

Fig. 16 MAC matrices between the intact structure and different damage scenarios (physical test)
![img-19.jpeg](img-19.jpeg)
more adjacent members will be misidentified as experiencing more severe member damage. It is worth pointing out that, the real damage of members in engineering practice is much less than the damage value introduced in the test. Therefore, the proposed method is promising to be applied to the SDI problem of large-span spatial structures.

## 5 Conclusions

In this study, the model updating technique is applied to identify the multiple locations and severities of damage in a single-layer cylindrical latticed shell. The EDA-based damage identification algorithm for large-span spatial structures is proposed. Then, the factors influencing the performance of the EDA, i.e., the number of damaged members, damage severities and level of noise interference, were studied through a numerical case study. Moreover, a fabricated latticed shell model was constructed, and impact hammer tests were conducted in the laboratory. Multiple damage scenarios were designed to test the performance of the algorithm. The results show that the EDA-based SDI framework has good
performance in parameter identification. The main conclusions are summarized as follows:

1. In the numerical study case, the damage identification algorithm shows good performance in damage location and severity assessment. The average identification accuracy can reach $90 \%$, even taking into account multiple damage conditions and noise interference.
2. The accuracies of the EDA-based damage identification algorithm will decrease with the severity of member damage. The average identification accuracy is larger than $82 \%$ based on the laboratory data considering different damage levels of a single member.
3. For medium and heavy damage levels, the model updating technique successfully identified different levels of member damage based on the vibration responses of the test model. For slight damage, the model updating technique can identify generally damaged areas. However, an additional inspection should be conducted to precisely locate the damage. The misidentified members are mainly located near the real damaged member and the support members since the displacement modes of

![img-20.jpeg](img-20.jpeg)

Fig. 17 The damage identification results obtained from the EDAbased model updating (physical test)
these points are more sensitive to the local damage of the members.

Further efforts can be focused on the following areas: (1) improving the objective function of damage identification to precisely locate the damage under complicated damage conditions; (2) considering multiple damage forms in addition to member weakening; and (3) testing the performance of the EDA-based model updating technique in real structures. It can be expected that the challenge of model updating technique in real-world applications include: (1) lack of knowledge of physical phenomena that are likely not simulated by the numerical model (i.e. noise level, boundary conditions, initial imperfections, damping ratio, etc.); (2) lack of basis for the selection of updating parameters; (3) convergence
![img-21.jpeg](img-21.jpeg)

Fig. 18 Variation in the updating factors versus the number of generations (physical test)

Table 10 Statistics of the damage identification accuracies based on the laboratory data

| Scenarios | Maximum <br> value (\%) | Minimum <br> value (\%) | Mean value (\%) | Standard <br> deviation |
| :-- | :-- | :-- | :-- | :-- |
| MT-2 | 99.85 | 70.44 | 89.59 | 0.0718 |
| MT-3 | 99.59 | 62.48 | 86.10 | 0.0697 |
| MT-4 | 98.57 | 55.62 | 82.26 | 0.1009 |

difficulties in multi-parameter updating problems, etc. To the author's knowledge, a combination of the physics-based and data-driven approaches is a possible way to solve the above problems.

Acknowledgements This research was financially supported by the National Natural Science Foundation of China (nos. 51525803; 51978458).

## References

1. Bao Y, Li H, Sun X et al (2012) Compressive sampling-based data loss recovery for wireless sensor networks used in civil structural health monitoring. Struct Health Monit 12(1):78-95
2. Zhang Z, Luo Y (2017) Restoring method for missing data of spatial structural stress monitoring based on correlation. Mech Syst Signal Process 91:266-277
3. Farrar CR, Doebling SW, Nix DA (2001) Vibration-based structural damage identification. Philos Trans R Soc A 359:131-149
4. Magalhães F, Cunha A, Caetano E (2012) Vibration based structural health monitoring of an arch bridge: from automated OMA to damage detection. Mech Syst Signal Process 28:212-228
5. Fugate ML, Sohn H, Farrar CR (2001) Vibration-based damage detection using statistical process control. Mech Syst Signal Process 15(4):707-721
6. Shadan F, Khoshnoudian F, Esfandiari A (2016) A frequency response-based structural damage identification using model updating method. Struct Control Health Monit 23(2):286-302
7. Fan W, Qiao P (2010) Vibration-based damage identification methods: a review and comparative study. Struct Health Monit 10(1):83-111
8. Nair KK, Kiremidjian AS, Law KH (2006) Time series-based damage detection and localization algorithm with application to the ASCE benchmark structure. J Sound Vib 291(1-2):349-368
9. Grande E, Imbimbo M (2012) A data-driven approach for damage detection: An application to the ASCE steel benchmark structure. J Civ Struct Heal Monit 2(2):73-85
10. Zhang T, Biswal S, Wang Y (2019) SHMnet: condition assessment of bolted connection with beyond human-level performance. Struct Health Monit 19(4):1188-1201
11. Ozevin D (2010) Geometry-based spatial acoustic source location for spaced structures. Struct Health Monit 10(5):503-510
12. Sodano HA (2007) Development of an automated eddy current structural health monitoring technique with an extended sensing region for corrosion detection. Struct Health Monit 6(2):111-119
13. Rainieri C, Fabbrocino G, Verderame GM (2013) Non-destructive characterization and dynamic identification of a modern heritage building for serviceability seismic analyses. NDT\&E Int 60:17-31
14. Ying W, Hong H (2013) Damage identification of slab-girder structures: experimental studies. J Civ Struct Health Monit 3(2):93-103
15. Li Y, Ma L, Li S et al (2016) Two-step damage detection method for large and complex structures. In: International conference in communications, signal processing, and systems 2016, vol 423, pp 419-429
16. Hao H, Xia Y (2002) Vibration-based damage detection of structures by genetic algorithm. J Comput Civ Eng 16(3):222-229
17. Masoumi M, Jamshidi E (2015) Damage diagnosis in steel structures with different noise levels via optimization algorithms. Int J Steel Struct 15(3):557-565
18. Sun G, Liu C, Zhang S et al (2014) Three-step damage identification method based on dynamic characteristics. Trans Tianjin Univ 20(5):379-384
19. Avci O, Abdeljaber O, Kiranyaz S et al (2021) A review of vibra-tion-based damage detection in civil structures: from traditional methods to machine learning and deep learning applications. Mech Syst Signal Process 147:107077
20. Li J, Hao H (2014) Substructure damage identification based on wavelet-domain response reconstruction. Struct Health Monit 13(4):389-405
21. Guo T, Wu L, Wang C et al (2019) Damage detection in a novel deep-learning framework: a robust method for feature extraction. Struct Health Monit 19(2):424-442
22. Zhang Z, Sun C (2020) Multi-site structural damage identification using a multi-label classification scheme of machine learning. Measurement 154:107473
23. Larranga P, Lozano JA (2001) Estimation of distribution algorithms: a new tool for evolutionary computation. Kluwer Academic Publishers, New York
24. Wang Y, Zhang T (2013) Finite element model updating using estimation of distribution algorithm. In: SHMII-6 2013: Proceedings of the 6th international conference on structural health monitoring of intelligent infrastructure, Hong Kong Polytechnic University, Hong Kong, pp 1-8
25. Santana R, Bielza C, Larranaga P et al (2010) Mateda-2.0: estimation of distribution algorithms in MATLAB. J Stat Softw 35(7):1-30
26. Xu Y, Nikitas G, Zhang T et al (2019) Support condition monitoring of offshore wind turbines using model updating techniques. Struct Health Monit 19(4):1017-1031
27. Han Q, Wang C, Xu Y et al (2020) Mechanical performance of AH joints and influence on the stability behaviour of single-layer cylindrical shells. Thin Walled Struct 146:217-232
28. Doebling SW, Hemez FM, Peterson LD et al (1997) Improved damage location accuracy using strain energy based on mode selection criteria. AIAA J 35(4):693-699
29. Brehm M, Zabel V, Bucher C (2010) An automatic mode pairing strategy using an enhanced modal assurance criterion based on modal strain energies. J Sound Vib 329(25):5375-5392
30. Selesnick IW, Burrus CS (1998) Generalized digital Butterworth filter design. IEEE Trans Signal Process 46(6):1688-1694

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.