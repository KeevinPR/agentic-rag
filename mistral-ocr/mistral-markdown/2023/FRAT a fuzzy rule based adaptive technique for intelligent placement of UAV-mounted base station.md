# FRAT: a fuzzy rule based adaptive technique for intelligent placement of UAV-mounted base station 

Dilip Mandloi ${ }^{1} \cdot$ Rajeev Arya ${ }^{1}$ (D)

Accepted: 30 January 2023 / Published online: 25 February 2023
(c) The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2023


#### Abstract

Unmanned Aerial Vehicle (UAV)-mounted base stations (UmBSs) are a potential approach for quick wireless service recovery in a scenario where the terrestrial network has collapsed or has not been installed. However, identifying the locations, where the minimum number of UmBSs can be deployed to serve the maximum number of Mobile Users (MUs) is one of the fundamental problems of base station deployment. In particular, we aim to reduce the number of UmBSs required and increase the number of MUs served by optimizing the deployment locations of UmBS. To this end, a threestep UmBS deployment approach is proposed. First, utilize K-means, a machine learning-based clustering technique, for the cluster initialization of the UmBSs deployment locations. Next, to ensure the required Quality of Service at MU, the service radius of each UmBS is estimated based on the minimum signal-to-interference plus noise ratio at each MU. Subsequently, a fuzzy rule-based adaptive genetic algorithm termed FRAT is proposed to reduce the number of UmBSs required and to increase the number of MU served. Finally, the effectiveness of the proposed approach is demonstrated using simulation results. Furthermore, the conventional Genetic Algorithm and Estimation of Distribution Algorithm are considered baseline techniques to present the comparative analysis.


Keywords UAV mounted base station (UmBS) $\cdot$ K-means technique $\cdot$ Fuzzy rule based adaptive genetic algorithm $\cdot$ SINR based MU-UmBS association $\cdot$ UmBS deployment

## 1 Introduction

Over the last decade, the number of people using networkconnected devices such as smartphones, smart home automation systems, wearable health monitors, smart cars, and so on has increased exponentially [1, 2]. The advantages of fifth-generation (5G) technology and smart cities can be ascribed to the fast proliferation of network-connected devices [3]. The operations of such devices highly rely on seamless network connectivity. However, these devices have experienced severe operational challenges in many instances [4]. Especially in areas with complex terrain structures where the deployment of terrestrial-based

[^0]network infrastructure is not feasible and in areas where existing network infrastructure has been demolished due to natural disasters [5]. In such instances, UmBS has been identified as a potential candidate to provide network connectivity with the required Quality of Service (QoS) due to the following benefits [6]:

- The ability to deploy quickly and on-demand, with minimal deployment cost and land area requirements compared to Terrestrial Base Station (TBS) deployment [3].
- The ability to produce more LoS connections to MUs via three dimensional (3D) mobility, resulting in highquality air-to-ground (A2G) links for network connectivity [7].
- The ability to deploy at different altitudes results in flexibility in service coverage modification based on Mobile User (MU) distribution [5].

Because of the aforementioned benefits, major telecom service providers are seeking commercial opportunities and


[^0]:    $\boxtimes$ Rajeev Arya
    rajeev.arya@nitp.ac.in
    Dilip Mandloi
    dilipm.phd19.ec@nitp.ac.in

    1 Department of ECE, National Institute of Technology Patna, Patna, Bihar 800005, India

working on UmBS deployment projects. AT\&T has recently tested its Unmanned Aerial Vehicle (UAV)mounted base stations (UmBSs) named "Flying COWs" in Louisiana City, USA, where the existing network infrastructure has been damaged due to hurricane lda [8]. Moreover, in collaboration with China Mobile Corporation, Huawei has also tested its first 5G UmBS in Xiong'an city recently [9]. In addition, large corporates like Facebook with project Aquila, Amazon with project Prime Air, Google with project Wing, and Nokia with project Nokia Drone Networks have also embraced this new wireless communication paradigm $[5,10,11]$.

Although the deployment of UmBS in emergency scenarios can provide network connectivity in no time, it faces some challenges also [6]. One major issue is the cost of UmBS deployment, which has a direct impact on the network service provider's revenue. In this paper, we investigate the deployment issues of multiple UmBSs in a scenario where conventional network infrastructure has been destroyed due to a natural catastrophe and Mobile Users (MUs) trapped in such a situation are seeking emergency network connectivity. From an overall investment perspective, we devised an optimization problem to reduce the number of UmBSs deployed while increasing the number of MUs served. The optimization problem has been solved under constraints such as the number of uncovered MUs should not be more than the predefined value, the minimum and maximum MUs to be served by each UmBS, and maintaining an SINR threshold at each MU.

### 1.1 Related work

In the literature, various studies have presented the potential of UmBS deployment in different scenarios, such as data collection in the Internet of Things (IoT) networks [2, 4, 12, 13], TBS coverage extension in remote areas [14, 15], offloading of an overloaded TBS [16, 17], quick wireless service recovery after natural disasters [11, 18, 19] and so on. The deployment of UmBS in such scenarios has been studied with different objectives such as maximizing the network capacity, minimizing the transmit power, reducing the number of UmBSs required, and so on.

### 1.1.1 Maximizing the network capacity

In the existing work, the authors have identified various parameters for optimization to achieve high throughput and maximum coverage. In [11], the authors jointly optimized the user association, the position of UmBS, and resource allocation to increase the network capacity. Similarly, a recursive approach is proposed in [15] to optimize UmBSs position, resource allocation, and user association that increases the user throughput. In [20], the authors designed an UmBSs placement algorithm aimed to improve the overall spectrum efficiency of the hotspot region. In their proposed algorithm, the UmBS placement problem was divided into two subproblems: MU association and UmBS deployment, which were solved recursively to obtain the optimal solution. In the sequel, a Weighted Expectation Maximization (WEM) and contract theory-based predictive method for the optimal UmBS deployment is proposed in [21]. In their work, WEM was utilized to anticipate user distribution and traffic demand, and contract theory was employed to guarantee the communication between UmBS and the TBS. In [22], the authors proposed a sweep and search algorithm to identify the user distribution for clustering and optimal placement of UmBSs. The authors of [23] focus on the optimal positioning of the UmBSs to enhance the capacity of an overloaded TBS. The authors presented a k-means-based approach for UmBS placement. Similarly, in [7], the position of the UmBS is optimized for coverage maximization. They proposed a convolutional neural network model-based deep learning approach for UmBS trajectory optimization in real-time. However, their study is limited to the deployment of a single UmBS. In [24], the height of the UmBS was optimized to reduce the symbol error rate and increase the coverage area in different environmental scenarios.

### 1.1.2 Minimizing the transmit power

Since UmBSs are limited-energy devices, the efficient use of the UmBS onboard energy is one of the biggest challenges. To this end, some authors focused their studies on the optimal positioning of UmBS to improve its energy efficiency. In [17], the authors proposed decoupling-based and successive convex approximation-based algorithms to investigate the optimal location of UmBS for equal transmit power and unequal transmit power scenarios, respectively. The authors of [18] jointly optimized the UmBS position, bandwidth allocation, and power of backhaul and access links to propose an energy-efficient UmBS deployment algorithm. Similarly, the authors of [25] investigated the 3D positioning and resource allocation issues of a UmBS with the goal of throughput maximization under the constraints of QoS requirements, backhaul capacity, channel bandwidth, and transmit power. In the sequel, to position UmBSs as relays for backhaul connectivity of ground base networks, a Genetic Algorithm (GA)based approach is proposed in [14]. In their proposed approach, available bandwidth, maximum power available, signal-to-interference plus noise ratio (SINR) threshold, the height of the UmBS, and data rate are considered constraints for the association of the UmBS and ground base network.

# 1.1.3 Reducing the number of UmBSs required 

The deployment of each UmBS increases the capital expenditure, which would impact the network's overall operational costs. To this end, various authors have formulated different mathematical models and proposed solutions to reduce the number of UmBSs deployed. The position of UmBS, user clustering, and resource allocation are parameters of optimization in [1], to reduce the number of UmBSs and enhance the coverage area. The authors of [3] proposed a hybrid approach for reducing the number of UmBSs required while optimizing their load balance. In [19], a Particle Swarm Optimization (PSO)-based approach is proposed to reduce the number of UmBSs deployed by jointly optimizing their position of deployment and transmit power while maintaining the SINR threshold. In [26], the authors aimed to obtain a minimum number of UmBSs and their locations to serve a maximum number of users with an acceptable data rate. The authors formulated an optimization model, which was solved under the constraints of coverage ratio, data rate, and onboard energy. To reduce the number of UmBSs required, the authors in [27] used a reinforcement learning-based technique to jointly optimize the UmBS position, transmit power, and user association. The trade-off between the number of UmBSs deployed and the number of users served was explored in [28]. The authors proposed a greedy heuristic that jointly optimizes the UmBS position and user association under practical network constraints. The proposed solution increases the number of users served while minimizing the number of UmBSs required. Similarly, an edge-prior algorithm is proposed in [29] to reduce the number of UmBSs required to serve users in a disaster area. Furthermore, the authors of [30] implemented In-band fullduplex technology for UmBS to enhance the network throughput and reduce the number of UmBSs required to facilitate ground users. In [31], the authors proposed a PSO-based heuristic algorithm. The proposed solution determined the minimum number of UmBSs and their locations to serve the maximum number of users spread across a geographical area with varying densities. The authors of [32] provided centralized and distributed placement algorithms to provide on-demand coverage while maintaining interconnection between the UmBSs. The authors of [33] proposed a spiral algorithm in which UmBSs are positioned in a spiral route to cover all ground users. The proposed algorithm reduces the number of UmBSs required to ensure network connectivity for the users. The comparison of the proposed and existing approaches for UmBS deployment is provided in Table 1.

### 1.2 Motivation and contibution

The deployment of each UmBS increases the capital expenditure, which would impact the network's overall operational costs. To this end, the position of UmBSs should be optimized to reduce the number of UmBSs required while maximizing the coverage ratio. Furthermore, to prevent underutilization of the UmBS, the number of MUs associated with each UmBS should not be less than a specified proportion of its total capacity. Different from the existing work and an overall investment perspective, we considered the constraint of the minimum MU association for optimization. We have formulated a mathematical model and solved the problem under the constraints, such as the maximum coverage radius, the percentage of uncovered MUs, the minimum and maximum MUs served by each UmBS and the SINR threshold at each MU.

The following are the key contributions to this work:

- We design a fuzzy rule-based adaptive genetic algorithm to optimize the number of UmBS required for wireless service recovery. In our proposed algorithm, we used the fitness value of an individual population as a diversity measure to update the parameters of the genetic algorithm such as $P_{c}, P_{m}$ and $N_{p}$ in an adaptive mannerTo reduce the computational complexity, we constrained MU association to the UmBS by a maximum service radius, which is estimated based on the minimum SINR required at each MU. In addition, a K-means clustering approach is utilized to intelligently identify the initial UmBS locations for the proposed algorithm. To evaluate the fitness of an individual population, we implement a penalty function approach that converts an optimization problem into an unconstrained one. In addition, we design a repair routine to ensure that the remaining infeasible solution is transformed into a feasible one.To demonstrate the effectiveness of our proposed algorithm, we conducted MATLAB simulations in different scenarios with Monte-Carlo runs. Additionally, the performance of the proposed algorithm is compared with two baseline techniques.


### 1.3 Organization

The rest of the paper is divided into six sections. In Sect. 2, a system model is introduced. Section 3 describes the problem formulated. In Sect. 4, a solution to the devised problem is presented. Section 5 presents simulation results. We conclude our work in Sect. 6. Additionally, a summary of the symbols used and their implications is provided in Table 2.

Table 1 Comparison of the proposed and existing approaches

| Ref. <br> no. | Objective | Maintained <br> $\mathfrak{I}$ threshold <br> at MU | Constraint of <br> the $\zeta$ is included | Constraint of <br> the $\phi$ is <br> included | Constraint of <br> the $\psi$ is <br> included | is <br> Reduced |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | Optimized user clustering and resource allocation to <br> reduce the number of UmBSs deployed | Y | N | N | Y | Y |
|  | Balancing of traffic load to reduce the number of <br> UmBSs deployed | Y | N | N | N | Y |
|  | Provide on demand network connectivity in hotspot <br> event | Y | N | N | N | N |
|  | Optimize UmBSs location and transmit power to <br> reduce the number of UmBSs to be deployed | Y | N | N | Y | Y |
|  | Reduce the number of UmBSs to be deployed under <br> the constraint of coverage area and data rate | Y | N | N | Y | Y |
|  | Increase the capacity of TBS by deploying multiple <br> UmBSs | Y | N | N | N | N |
|  | Demonstrate the impact of coverage and capacity on <br> the number of UmBSs deployed | N | Y | N | Y | N |
|  | Increase the network throughput with the <br> deployment of minimum number of UmBSs | Y | N | N | N | Y |
|  | Optimized 3D placement of UmBSs to reduce the <br> number of UmBSs deployed | Y | N | N | Y | Y |
|  | provide on-demand coverage with minimum number <br> of UmBSs deployment | Y | Y | N | Y | Y |
|  | Increase the coverage area with minimum number of <br> UmBSs using spiral algorithm | Y | Y | N | N | Y |
| This <br> paper | Increase the number of MUs serve with minimum <br> number of UmBSs while ensuring required QoS | Y | Y | Y | Y | Y |

Implication of $\mathfrak{I}, \zeta, \phi, \psi$, and is provided in Table 2, $Y$, yes, $N$ no

## 2 System model

This section presents an overview of the system model under consideration. We consider the scenario of a geographical area where the terrestrial network has collapsed due to a natural disaster. As shown in Fig. 1, multiple UmBSs are deployed to serve $K$ MUs. The ground MUs are randomly distributed in a geographical area of size $1000 * 1000 \mathrm{~m}^{2}$. Let $=\{1,2, \ldots . \mathrm{K}\}$ denote the set of ground MUs and $=\{1,2, \ldots . . N\}^{T}$ denotes the set of initial deployment locations of UmBSs. The fixed location of each MU $j \in$ is denoted by $\left(x_{j}, y_{j}\right)$ where $j=(1,2, \ldots K)$, while the location of each UmBS $i \in$ is denoted by $\left(x_{i}, y_{i}\right.$, $h_{i}$ ) where $\left(x_{i}, y_{i}\right)$ represents the ground projection of the UmBS and $h_{i}$ represents the height at which UmBSs are hovering. We have considered that all the UmBSs are hovering at an equal height. Also, as illustrated in Fig. 1, all the deployed UmBSs are associated with the core ground network via microwave backhaul links.

The connectivity between MU and UmBS may be obstructed by various surrounding obstacles, due to which the Non-Line of Sight (NLoS) path is also available along with the Line of Sight (LoS) path. So, the channel between
each MU and their serving UmBS is modeled using an A2G channel model that incorporates both the signal components i.e., LoS and NLoS. The pathloss between the ith UmBS and $j$ th MU is expressed as (in dB) [27]

$$
\begin{aligned}
\mathcal{L}_{i, j}(d B)= & 20 \log _{10}\left(\frac{4 \pi f_{c}}{c}\right)+20 \log _{10}\left(r_{i j}\right)+\rho_{L o S} \alpha_{L o s} \\
& +\rho_{N L o S} \alpha_{N L o S}
\end{aligned}
$$

where $f_{c}$ is the carrier frequency, $c$ is the speed of light. Furthermore, $\alpha_{L o s}$ and $\alpha_{N L o S}$ delineate the attenuation factors of the LoS and NLoS links respectively. $r_{i j}=$ $\sqrt{\left(x_{i}-x_{j}\right)^{2}+\left(y_{i}-y_{j}\right)^{2}+h_{i}^{2}}$ is the separation between MU and its serving UmBS. Let $\rho_{L o S}$ and $\rho_{N L o S}$ are the probability of LoS and NLoS connectivity of the MU to the UmBS. The $\rho_{L o S}$ and $\rho_{N L o S}$ is calculated using the Eqs. (2) and (3) respectively [27]
$\rho_{L o S}=\frac{1}{1+\mu \exp \left(-v\left(\theta_{i j}-\mu\right)\right)}$
$\rho_{N L o S}=1-\rho_{L o S}$
where $\mu$ and $v$ are the environment dependent constants

Table 2 Summary of symbol used and their implications

| Symbol | Implications |
| :--: | :--: |
|  | Set of ground MUs |
| $\mathcal{N}$ | Set of initial deployment locations of UmBSs |
| $x_{j}, y_{j}$ | Position coordinates of $j$ th MU |
| $f_{c}$ | Carrier frequency |
| $\mathcal{L}_{i j}$ | Pathloss between the $i$ th UmBS and $j$ th MU |
| $\theta_{i j}$ | Elevation angle between $i$ th UmBS and $j$ th MU |
| $\mathfrak{T}$ | Signal to Interference plus Noise Ratio |
| $\mathcal{P}_{t, i}$ | Transmit power of $i$ th UmBS |
| $r_{i j}$ | Separation between $i$ th UmBS and $j$ th MU |
| $\mathcal{B}_{i}$ | Bandwidth of the $i$ th UmBS |
| $\Re_{i}$ | Attainable data rate from the ith UmBS |
| $\mathrm{x}_{\mathrm{i}}, \mathrm{y}_{\mathrm{i}}$ | Ground projection of $i$ th UmBS |
| $\mathrm{h}_{\mathrm{i}}$ | Height of $i$ th UmBS |
| $\mu, v$ | Environment dependent parameters |
| $\rho_{\text {LoS }}, \rho_{\text {NLoS }}$ | Probability of LoS and NLoS connectivity |
| $\Delta_{i j}$ | Horizontal distance between $i$ th UmBS and $j$ th MU |
| $\alpha_{\text {LoS }}, \alpha_{\text {NLoS }}$ | Attenuation factors of LoS and NLoS components |
| $\phi$ | Minimum number of MUs to be served by single UmBS |
| $\psi$ | Maximum number of MUs can be served by single UmBS |
| $\mathcal{M}_{i}$ | UmBS deployment status indicator |
| $\mathcal{T}_{i j}$ | indicator for MU and UmBS association |
| $\zeta$ | Maximum percentage of MUs to be unserved |
| $R_{i}$ | Data rate required by single MU |
| $P c$ | Crossover Probability |
| $P m$ | Mutation Probability |
| $N p$ | Random Permutation |
| $\mathcal{H}_{i j}$ | Channel power gain between the $i$ th UmBS and $j$ th MU |
| $\Omega$ | Per unit distance channel power gain |
| $\gamma$ | Path loss exponent |
| $\mathrm{C}_{\text {max }}$ | Maximum coverage radius |

parameters. Furthermore, $\theta_{i j}=\tan ^{-1}\left(h_{i} / \Delta_{i j}\right)$ is the measure of elevation angle between MU and UmBS, and $\Delta_{i j}=$ $\sqrt{\left(x_{i}-x_{j}\right)^{2}+\left(y_{i}-y_{j}\right)^{2}}$ is the horizontal distance of MU from the projection coordinates of its serving UmBS deployed at the height of $h_{i}(\mathrm{~m})$. Furthermore, we have denoted the transmitted power and bandwidth of $i$ th UmBS by $\mathcal{P}_{t, i}$ and $\mathcal{B}_{i}$ respectively. Based on the path loss model defined in Eq. (1), the SINR of the $j$ th MU served by the $i$ th UmBS is calculated as [11]
$\mathfrak{T}_{i j}=\frac{\mathcal{P}_{t, i} \mathcal{H}_{i j}}{\sigma^{2}}$
where $\sigma^{2}$ is the background noise power, $\mathcal{H}_{i j}$ is the measure of the channel power gain between the $i$ th UmBS and $j$ th MU and calculated as [11]
$\mathcal{H}_{i j}=\frac{\Omega}{\left(r_{i j}\right)^{\gamma}}$
where $\gamma$ denotes the path loss exponent and $\Omega$ is the measure of per unit distance channel power gain. The attainable data rate from an $i$ th UmBS located at $\left(x_{i}, y_{i}, h_{i}\right)$ is measured using Shannon's theorem as [30]
$\Re_{i}=\mathcal{B}_{i} \log _{2}(1+\mathfrak{T})$
Thus, to maintain the QoS requirement with the demanded data rate of each MU, the minimum SINR can be calculated as
$\mathfrak{T}_{\min }=2^{\frac{\%}{n_{t}}}-1$
Since the UmBS bandwidth is limited, to maintain the QoS requirement at MU, the maximum number of MUs that can be associated with a single UmBS is limited. The

Fig. 1 Illustration of the considered scenario for UmBS deployment
![img-0.jpeg](img-0.jpeg)
maximum number of MUs that can be associated with an UmBS is calculated as [31]
$\psi=\frac{\Re_{i}}{R_{i}}$

## 3 Problem formulation

In the event of a network outage, the deployment of UMBSs offers significant potential for quick wireless service recovery; nevertheless, the deployment procedure faces a number of major problems that must be resolved. First, how to select an association strategy for MUs and UmBS in order to maintain the QoS requirements at MU. Second, how to reduce the overall capital investment by limiting the number of UmBS required. In order to address these issues, the UmBS deployment procedure is constrained by the following limitations.

- To maintain the required QoS, the association of MU to any of the UmBS should be controlled by a minimum SINR received at MU.
- To limit the outage probability, the fraction of unserved MUs must be kept below a defined threshold.
- In view of the limited capacity of UmBS, the number of MU served by each UmBS must be in the range of lower and upper threshold values. Here, we denote the lower and upper thresholds by the variables
- $\phi$ and $\psi$ respectively.
- The horizontal distance between the MU and the UmBS should not exceed the coverage radius of the UmBS.
- To avoid redundancy, each MU should be served only by a single UmBS.

In this paper, we have formulated a mathematical model that aims to serve the maximum number of MUs with a minimum number of UmBSs while taking into account and incorporating the abovementioned constraints. We considered two binary matrices, first $\mathcal{M}=\left\{\mathcal{M}_{i}\right\}_{1 \times N}$ represents the deployment status of UmBS, second $\mathcal{T}=\left\{\mathcal{T}_{i j}\right\}_{K \times N}$ represents the association of the MUs with UmBS to formulate the mathematical model. The nonzero entries of the matrix $\mathcal{M}$ indicate the active status of the UmBS, while the nonzero entries of the matrix $\mathcal{T}$ indicate the association of the MUs with UmBSs. The optimization problem is formulated as follows
$\min \sum_{i=1}^{N}\left(\mathcal{M}_{i}+\frac{1}{\sum_{j=1}^{K} \mathcal{T}_{j i}}\right)$
s.t. $C_{1}: \mathcal{M}_{i}, \mathcal{T}_{i j} \in\{0,1\}, \quad \forall i \in \mathcal{N}, j \in \mathcal{K}$
$C_{2}: \sum_{i=1}^{N} \sum_{j=1}^{K} \mathcal{T}_{j i} \geq(1-\zeta) K$
$C_{3}: \sum_{j=1}^{K} \mathcal{T}_{i j} \leq 1, \quad \forall i \in \mathcal{N}$
$C_{4}: \mathfrak{I}_{i j} \geq \mathfrak{I}_{\text {min }}, \quad \forall i \in \mathcal{N}, j \in \mathcal{K}$
$C_{5}: \mathcal{T}_{i j} . \Delta_{i j} \leq \mathbb{C}_{\max }$
$C_{6}: \phi \geq \sum_{i=1}^{N} \mathcal{T}_{i j} \leq \psi \quad \forall j \in \mathcal{K}$
Constraint $\mathrm{C}_{1}$ depicts that the variables $\mathcal{M}_{i}$ and $\mathcal{T}_{i j}$ takes only binary values. Constraint $\mathrm{C}_{2}$ ensures that the percentage of unserved MUs does not exceed the predefined threshold value. Constraint $\mathrm{C}_{3}$ guarantees that a MU

is served by a single UmBS. Constraint $\mathrm{C}_{4}$ checks for minimum SINR criteria for the establishment of a connection between ith UmBS and $j$ th MU. Constraint $\mathrm{C}_{5}$ is the coverage constraint, i.e., the horizontal distance between a MU and an UmBS must not exceed the coverage radius of the UmBS. Constraint $\mathrm{C}_{6}$ guarantees that the number of MUs served by each UmBS must be in the range of lower and upper threshold values.

## 4 Proposed solution

In this section, a solution to minimize the objective function in Eq. (9) is proposed. The objective function can be minimized in multiple ways, such as minimize $\mathcal{M}_{i}$ and fix $\mathcal{T}_{j i}$, fix $\mathcal{M}_{i}$ and maximize $\mathcal{T}_{j i}$, minimize $\mathcal{M}_{i}$ and maximize $\mathcal{T}_{j i}$. The proposed algorithm minimizes the objective function by minimizing $\mathcal{M}_{i}$ and maximizing $\mathcal{T}_{j i}$ i.e. serving the maximum number of MUs with a minimum number of UmBSs. We divide our proposed solution to the UmBS deployment problem into three steps. First, to reduce the computational complexity utilize K-means, a machine learning-based clustering technique, to initialize the UmBSs deployment locations. Next, to ensure the required QoS at MU, the service radius of each UmBS is estimated based on the minimum SINR at each MU. Subsequently, a Fuzzy rule-based adaptive genetic algorithm termed FRAT is proposed to reduce the number of UmBS required and to increase the number of MUs served. The pseudo code for the proposed algorithm is provided in Algorithm 1.

### 4.1 UMBS deployment locations initialization

In order to reduce the computational complexity of the proposed algorithm, the first step of our proposed algorithm is to divide the MUs into clusters and identify the centroid location of each cluster. The centroid location of each cluster is considered the initial deployment location of UmBS, i.e., a single UmBS is deployed in each cluster. We utilized K-means, a machine learning-based clustering algorithm, to tackle the clustering of the MUs. The clustering policy of the K-means algorithm depends on the specific feature. We considered the distance between the MUs and centroid location as the feature. Here, we considered that the initial value of K , which is the number of available UmBSs ready for deployment and the location of the MUs is provided by the network operator. The initial deployment locations of UmBSs is denoted by the set $=\{1,2, \ldots N\}^{\mathrm{T}}$.

### 4.2 MU-UmBS association

After the initialization of the UmBS deployment locations all the possible connections between the UmBSs and MUs are initialized in association step. To maintain the required QoS, the association of $j$ th MU to ith UmBS is coupled with the received SINR. The $j$ th MU can be associated with the ith UmBS only when the received SINR is more than the predefined threshold value $\left(\mathfrak{I}_{\min }\right)$. The value of $\left(\mathfrak{I}_{\min }\right)$ is computed using Eq. (7). The SINR of MUs is computed using Eq. (4), which depends on its distance from the serving UmBS. So, an upper bound on the distance between the UmBS and MU is derived to meet the SINR requirement. We define this upper bound on distance as the maximum coverage radius of UmBS. Then, the constraint $\left(\mathfrak{I}_{\min }\right)$ is transferred to the maximum coverage radius of UmBS, which can be calculated as
$\mathbb{C}_{\max }=\sqrt{\left(\frac{\Omega \mathcal{P}_{t, i}}{\mathfrak{I}_{\min } \sigma^{2}}\right)^{2 / 7}-h_{i}^{2}}$

### 4.3 Fuzzy rule based adaptive technique (FRAT)

Recently, GA is considered a promising technique to solve the optimization problem. However, getting a solution for an unconstrained optimization problem using GA is a simple task, whereas getting a solution to a constraint optimization problem has multiple issues [34]. The two main issues are balancing the exploration and exploitation relationship and handling the constraint while estimating the fitness value of the individual chromosome. When the exploration and exploitation relationship deteriorate, it leads to the problem of premature convergence, which degrades the performance of GA. The problem of premature convergence occurs due to fixing the algorithm parameters such as, $P_{c}, P_{m}$ and $N_{p}$ is at fix level during the execution of the GA. The problem of premature convergence is solved by dynamic adaptation of these parameters. We designed a single input and multiple output Mamdani FIS to vary $P_{c}, P_{m}$ and $N_{p}$ in an adaptive manner. Furthermore, we implement a penalty function approach to handle the constraint while estimating the fitness value of the individual chromosome. The penalty function technique appends constraint violations as a penalty term to the objective function and contributes to the selection of the next generation.

### 4.3.1 Initial population generation

The initial population is generated in a random manner and represented by a binary matrix $B$ with size $N_{p} * T_{v}$, where $N_{p}$ is the population size and $T_{v}$ is the number of variables.

```
Algorithm 1 Implementation of FRAT
    1 Input: \(\mathcal{K}, \mathcal{N}, \phi, \psi, \Delta, \zeta, \zeta_{\max }\)
    2 Output: \(\mathcal{M}, \mathcal{T}\)
    3 Perform clustering of MUs to identify the initial deployment location of UmBSs \((1,2 \ldots \ldots . \mathrm{N})\)
    Estimate the value of \(\mathbb{C}_{\max }\) using Eq. (16)
    for \(\mathrm{i}=1: \mathcal{K}\)
        for \(\mathrm{j}=1: \mathcal{N}\)
            Initialize the matrix \(\mathcal{T}=[n u l l]_{\mathcal{K} \times \mathcal{N}}\)
            Compute the value of \(\Delta_{i j}\)
            Compute \(\mathcal{T}_{i j}\) using the distance and \(\mathbb{C}_{\max }\).
        end for
        Generate the initial population as Inipop \(=(\) rand \()_{N_{p}}, \tau_{p}\)
    end for
    Calculate the number of crossovers \(C_{\mathrm{n}}\) and number of mutations \(M_{\mathrm{n}}\) (based on the \(P_{\mathrm{c}}, P_{\mathrm{m}}\) and \(N_{\mathrm{p}}\) )
    Calculate the number of elite parents \(E_{\mathrm{n}}\)
    Calculate the fitness value of each Inipop chromosomes using penalty function approach.
    Arrange Inipop chromosomes in ascending order
    for 1: number of generations
        Select \(E_{\mathrm{n}}\) elite parents from the current population
        Construct parents index vector based on the fitness proportionate selection from current population
        Initialize a crossover population matrix \(C_{\mathrm{p}}\)
        for \(\mathrm{i}=1: N_{\mathrm{p}}\)
            if rand \(>P_{\mathrm{c}}\) then
                Select parents \(P_{1}\) and \(P_{2}\) from current population
                Perform crossover operation using Eq. (18) and Eq. (19) and generate new offspring's \(P_{3}\) and \(P_{4}\)
                Add \(P_{3}\) and \(P_{4}\) to \(C_{\mathrm{p}}\)
                end if
            end for
    Initialize index vector \(I_{\mathrm{m}}\) based on the random permutation of \(N_{\mathrm{p}}\)
    Initialize a mutation population matrix \(C_{\mathrm{m}}\)
    for \(\mathrm{i}=1: N_{\mathrm{p}}\)
        if rand \(>P_{\mathrm{m}}\) then
                Select a chromosome with index value of \(I_{\mathrm{m}}\) from current population
                Perform mutation operation using Eq. (20) and generate new offspring \(P_{5}\)
                end if
                if index value exceeds the \(M_{\mathrm{n}}\) then break the loop
                end if
            end for
    Add \(P_{5}\) to the \(C_{\mathrm{m}}\)
    Update Inipop matrix based on \(E_{\mathrm{n}}, C_{\mathrm{p}}\) and \(C_{\mathrm{m}}\)
    Calculate the fitness value of each Inipop chromosomes using penalty function approach
    Arrange Inipop chromosomes in ascending order
    Estimate the mean variations in current population \(M_{\mathrm{e}}\)
    Develop a fuzzy system with INPUT: \(M_{\mathrm{e}}\) OUTPUT: \(\Delta P_{\mathrm{c}}, \Delta P_{\mathrm{m}}\)
    Update the value of crossover probability \(P_{\mathrm{c}}=P_{\mathrm{c}}+\Delta P_{\mathrm{c}}\)
    Update the value of mutation probability \(P_{\mathrm{m}}=P_{\mathrm{m}}+\Delta P_{\mathrm{m}}\)
    Update the value of \(C_{\mathrm{n}}\) and \(M_{\mathrm{n}}\) based on current population
    Increase the number of generations by unity
    end for
    Conduct repair operation to fix the constraint violations using Algorithm 2 and Algorithm 3
    Select chromosome of current population with best fitness value as \(\mathcal{M}, \mathcal{T}\)
```

The number of variables is the sum of $\mathcal{N}$ and $\mathcal{N} *$. After the generation of initial population, the fitness of each chromosome of $B$ is estimated using penalty function approach and the initial association matrix of MUs and UmBS
created using maximum service radius. As our aim is to serve the maximum number of MUs with minimum number of UmBSs and minimize the estimated fitness value of the individual chromosomes.

### 4.3.2 Crossover and mutation

Getting an optimal solution of an optimization problem using GA is strongly dependent on the setting of its genetic parameters such as selection (select chromosome from current population for next generations), $P_{c}$ (It determines whether perform or not to perform the crossover operation), and $P_{m}$ (It determines whether perform or not to perform the mutation operation). In the proposed approach, the parent population to perform crossover operation is selected using fitness proportionate selection. The fitness proportionate selection scheme associates the selection probability of each chromosome with their fitness value and can be estimated as
$p_{i}=\frac{C_{i}}{\sum_{i=1}^{N_{p}} C_{i}}$
where $C_{i}$ denote the fitness value of the individual chromosome. So, higher the value of fitness value means higher the chance of getting selected. The indexes of the selected parents are stored in the index vector denoted as $I$. Next to perform the crossover operation two parent chromosomes, $\mathrm{P}_{1}$ with index value $I_{2 n}$ and $\mathrm{P}_{2}$ with index value $I_{2 n-1}$, where $\mathrm{n}=\left\{1,2 \ldots N_{p} / 2\right\}$ are selected from the initial population. The crossover operation generates two new offspring i.e., $\mathrm{P}_{3}$ and $\mathrm{P}_{4}$ in following manner
$P_{3}=(1+\alpha) P_{1}+(1-\alpha) P_{2}$
$P_{4}=(1-\alpha) P_{1}+(1+\alpha) P_{2}$
where $\alpha$ is a user defined variable and its value ranges in [0, 1]. After the crossover operation we conducted the mutation operation which update the single or multiple components of individual chromosome. The mutation operation of $j$ th chromosome, selected from the random permutation vector of $N_{p_{i}}$ is performed in the following manner
$P_{5}=\left\{\begin{array}{c}N_{p}(j)+\left(U-N_{p}(j)\right) *(1-r)^{\frac{1}{1+r}} r>0.5 \\ N_{p}(j)-\left(N_{p}(j)-L\right)(1-r)^{\frac{1}{1+r}} r \leq 0.5\end{array}\right.$
where [L U] is the range of mutation, r is a random number with range [0 1], and $v$ is user defined parameter.

Table 3 Rule base for FIS
If $M_{v}$ is low then $\Delta P_{c}$ is positive $\Delta P_{m}$ is negative (1)
If $M_{v}$ is medium then $\Delta P_{c}$ is neutral $\Delta P_{m}$ is neutral (1)
If $M_{v}$ is high then $\Delta P_{c}$ is negative $\Delta P_{m}$ is positive (1)

### 4.3.3 Fuzzy inference system (FIS) for parameter adaptation

In this subsection, we proposed the design of FIS for dynamic adaption of the GA parameters such as $P_{c}, P_{m}$ and $N_{p}$. Here, to measure the level of diversity in the population, the mean variation in the current population $M_{v}$ is considered as an input for the FIS system. The range of values for the input variable $M_{v}$ is [0 1]. Furthermore, the output variables of the FIS are denoted as, $\Delta P_{c_{i}}$ and $\Delta P_{m}$. These variables vary in the range of $[-0.2,0.2]$ and $[\mathrm{0} .1,0.1]$ respectively. The values of $\Delta P_{c}$ and $\Delta P_{m}$ is the measure of the amount to which the current values of the $P_{c}$ and $P_{m}$ varies. As the algorithm progresses, the values of $P_{c}$ and $P_{m}$ are dynamically updated for the next iteration by adding the output variable of FIS to it. Subsequently, the values of $P_{c}$ and $P_{m}$ updated $N_{p}$ for each iteration. The linguistic variables associated with the input is diversity having three Membership Functions (MFs): Low, medium and high. The linguistic variables associated with the two output variables are differential crossover probability and differential mutation probability. The MFs of the output variables is: negative, neutral and positive. Three rules are defined to describe the input-output relationship. The rules are defined such that exploration takes precedence over exploitation in the initial iteration of the GA execution, and exploitation takes precedence over exploration in the final iterations. The Table 3 summarizes the rule base for dynamic parameter modification.

The input and output variables of the proposed FIS is having trapezoidal MFs and these trapezoidal MFs are defined in terms of four parameters r, s, t and u. Table 4 summarised the MFs of input and output variables.

### 4.3.4 Repair operation to fix constraints violation

In the proposed algorithm, we utilized the penalty function technique to solve the optimization problem defined in Eq. (9). The penalty function technique appends constraints as a penalty term to the objective function for constraint handling. However, besides having multiple advantages, the penalty function technique has drawbacks too. The main drawback of the penalty function technique is that it does not guarantee the solution's feasibility. Therefore, we combine repair operations with a penalty function technique to fix constraint violations. We conduct a repair operation on the output of algorithm $1 . C_{3}$ ensures that each MU is associated with a single UmBS only. The association of a single MU with multiple UmBSs is detected and removed. Algorithm 2 describes in detail how to delete multiple associations for each MU. Meanwhile, after the execution of Algorithm 2, the number of MUs

![img-1.jpeg](img-1.jpeg)

```
Algorithm 2 Repair operation to fix the violation of \(C_{3}\)
    find the association of each MU with the UmBSs and record it in set B
    while (the maximum value in B greater than 1) do
        find the MUs associated with each UmBS and record it in set D
        find the index of UmBS with the maximum MU association and let \(i\)
        find the MUs that are associated with \(i^{th}\) UmBS and record it in set E
        find the distance between \(i^{th}\) UmBS and each MU associated with it
        if (the distance between \(i^{th}\) UmBS and the associated MU> \(\mathbb{C}_{\text {max }}\) ) then
            remove the association between \(i^{th}\) UmBS and the associated MU
            update set E
        end if
        if (length of \(\mathrm{E}>\psi\) ) then
            find the MU with the maximum association in set E say \(j\)
            remove the association between \(i^{th}\) UmBS and \(j^{th}\) MU
            update set E
        end if
        remove the MU association that remained in D to other UmBS
        update \(\mathrm{B}, \mathcal{T}\)
    end while
    calculate \(\mathcal{M}\) based on \(\mathcal{T}\)
```

associated with ith UmBS may be outside of the lower and upper bounds i.e., a violation of $C_{6}$. Therefore, we conducted a repair operation to fix the violation and the same is described in Algorithm 3 in details. Furthermore, we collaborated $C_{5}$ with the repair operation of $C_{3} \alpha n d C_{6}$ to ensure that it was not violated

## 5 Simulation results

In this section, simulation results and their analysis are presented. The performance of the proposed algorithm is evaluated through MATLAB simulations and averaged through Monte-Carlo runs. For simulations, we have considered a scenario where a network provider has 12 ready-to-deploy UmBSs and wants to achieve quick wireless recovery in a network outage by deploying a minimum number of UmBSs under the constraints mentioned in Sect. 3. Additionally, we assume that the network provider has position coordinates for MUs that are randomly distributed in an area of size $1000^{*} 1000 \mathrm{~m}^{2}$. The transmit power of all the UmBSs is assumed to be equal and fixed. Here the value of $\phi$ is fixed at $30 \%$ of $\psi$ while the value of $\psi$ is estimated using Eq. (8). Furthermore, other simulation parameters are specified in Table 5. We have conducted different experiments to evaluate the performance of the proposed algorithm in terms of the number of UmBSs required, the number of MUs served, and the average SINR received at each MU, with different transmission bandwidths of UmBSs, varying numbers of MUs seeking wireless service, different hovering heights of the UmBSs, and varying percentages of MUs allowed to remain in
outages. Finally, the performance of the proposed algorithm is compared with two baseline techniques.

## 6 Effect of UmBS transmission bandwidth

Here, is the effect of UmBS bandwidth available for a single UmBS $\left(\mathcal{B}_{i}\right)$ while fixing the $R_{i}=5 \mathrm{Mbps}$, $\mathcal{P}_{r, i}=30 \mathrm{dBW}$, and $\mathfrak{T}_{\min }=12 \mathrm{~dB}$. As shown in Eq. (6), the change in the value of $\mathcal{B}_{i}$ affects the $\Re_{i}$ subsequently $\Re_{i}$ affected the value of $\phi$ and $\psi$ which can be estimated using Eq. (8). We consider a set available UmBS bandwidth

Table 5 Simulation parameters

| Parameter name | Parameter value |
| :-- | :-- |
| Service area | $1000 * 1000 \mathrm{~m}^{2}$ |
| Per unit distance channel power gain $(\Omega)$ | 1 [11] |
| Attainable data rate from the ith UmBS $\left(\left(\Re_{i}\right)\right.$ | 100 Mbps |
| Bandwidth of the ith UmBSs $\left(\mathcal{B}_{i}\right)$ | $25,50,75 \mathrm{MHz}$ |
| Path loss exponent $(\gamma)$ | 2 [6] |
| SINR threshold $\left(\mathfrak{T}_{\min }\right)$ | 12 dB |
| Background noise power $\left(\sigma^{2}\right)$ | -30 dB |
| Transmit power of the ith UmBS $\left(\mathcal{P}_{r, i}\right)$ | $30 \mathrm{dBW}[1]$ |
| Total Number of MUs | $40-200$ |
| Data rate required by single MU $R_{i}$ | 5 Mbps |
| Height of UmBSs $\left(h_{i}\right)$ | $40-200 \mathrm{~m}$ |
| Distance measure for proximity | Euclidian distance |

```
Algorithm 3 Repair operation to fix the violation of \(C_{0}\)
    find the total MU associated with each UmBS and record it in set U
    find the UmBS with less than \(\phi\) MU association and record it in set V
    for \(\mathrm{i}=1\) : length (V) do
        find the index of MUs associated with \(i^{t h}\) UmBS and let \(j\)
        find the association of \(j^{\text {th }} \mathrm{MU}\) with other UmBS and record it in set W
        for each \(k \in \mathrm{~W}\) do
            if \(\left(C_{3}, C_{5}, C_{6}\right.\) hold simultaneously for k ) then
                associate the \(j^{\text {th }} \mathrm{MU}\) with \(k^{\text {th }} \mathrm{UmBS}\)
            update \(\mathcal{M}, \mathcal{T}\)
        end if
        end for
    end for
    find the UmBS with greater than \(\psi\) MU association and record it in set X
    for \(\mathrm{i}=1\) : length(X) do
        find the total MUs associated with \(i^{\text {th }} \mathrm{UmBS}\) and record in set Y
        find the excess number of associations with \(i^{\text {th }} \mathrm{UmBS}\) to the \(\psi\) and record in set Z
        initialize a null set to record shifting of MUs i.e., R
        for \(\mathrm{j}=1\) : length \((\mathrm{Y})\) do
            if \((\mathrm{R} \in \mathrm{Z})\) then
                find the association of \(j^{\text {th }} \mathrm{MU}\) with other UmBS and record in set S
                for each \(k \in \mathrm{~S}\) do
                    if \(\left(C_{3}, C_{5}, C_{6}\right.\) hold simultaneously for \(k)\) then
                        associate the \(j^{\text {th }} \mathrm{MU}\) with \(k^{\text {th }} \mathrm{UmBS}\)
                        update \(\mathcal{M}, \mathcal{T}\)
                        increase R by 1 for each reassociation of MU
                end if
            end for
        end if
        end for
    end for
```

$\mathcal{B}_{i}=\{25,50,75\}$ where values are in Mbps. Figure 2 illustrates how the number of UmBSs required and the percentage of MUs served get affected when the number of MUs seeking network service varies from 40 to 200 with each set of bandwidth. Here, we fix the value of $h_{i}=120 \mathrm{~m}$ and $\zeta=20$. As shown in Fig. 2, the number of UmBSs required to serve different sets of MUs decreases with the increase in the UmBS bandwidth. However, it can also be noticed that there is a significant reduction in the percentage of MUs served. The reason behind this is that the transmission bandwidth of the UmBS is directly related to the $\Re_{i}$ so an increase in the bandwidth increases the value of $\Re_{i}$ thus increasing the value of $\phi$ and $\psi$ too. Due to the random distribution of MUs in the service area, there aren't many places where UmBSs can be deployed to meet the higher values of $\phi$. However, it is important to notice that when the service area becomes crowded, the difference between the percentage of MUs covered by UmBS with low transmission bandwidth and those covered by high transmission bandwidth becomes smaller. Figure 3 illustrates the number of UmBSs with different bandwidths required to serve 120 MUs when the $h_{i}$ varies from 40 to

200 m . As shown in Fig. 3, with the deployment of UmBS at lower altitudes, we can serve a greater percentage of MUs with a smaller number of UmBSs with all values of bandwidth. This is because the lower height of the UmBS
![img-2.jpeg](img-2.jpeg)

Fig. 2 Analysis of required UmBSs and percentage of MU serve as a function of bandwidth with varying number of MUs with $\zeta=20, h_{i}=120 m$

![img-3.jpeg](img-3.jpeg)

Fig. 3 Analysis of required UmBSs and percentage of MU serve as a function of bandwidth with varying height of UmBS with $\zeta=20, \mathcal{K}=120$
leads to higher values of received SINR at MU. Figure 4 plots the number of UmBS required and the percentage of MUs served when the $\phi$ varies from 10 to $90 \%$. From Fig. 4, it can be seen that the deployment of UmBSs with larger bandwidth is beneficial in terms of the number of UmBSs required, but it is detrimental in terms of the percentage of MUs served. A large portion of MUs remains unserved. The percentage of MU served does not meet the predefined threshold of MUs served. Meanwhile, from Fig. 4, it is also important to note that, even though the use of UmBS with less bandwidth means more UmBSs are needed, it is good in terms of MUs served.
![img-4.jpeg](img-4.jpeg)

Fig. 4 Analysis of required UmBSs and percentage of MU serve as a function of bandwidth with varying minimum MU coverage with $h_{i}=120 \mathrm{~m}, \mathcal{K}=120$
![img-5.jpeg](img-5.jpeg)

Fig. 5 Number of UmBSs required and percentage of MU serve with varying number of MUs with $\zeta=20, h_{i}=120 m, B_{i}=25 M H z$

### 6.1 Performance evaluation of the FRAT

In this subsection, the performance of the proposed algorithm, termed FRAT, is evaluated with three performance metrics, such as the number of UmBSs required, percentage of MUs served, and SINR received. We analyze the effects of the number of MUs seeking wireless services, the height of UmBS and the UMBS coverage ratio on the performance metrics. Meanwhile, two evolutionary algorithms such as the conventional GA and the Estimation of Distribution Algorithm (EDA) are considered the baseline approach for comparative analysis. In the first base line approach, i.e., conventional GA, the solution to the optimization problem is based on the selection and recombination process by setting its genetic parameters such as $P_{e}, P_{m}$, and $N_{p}$ at a fixed level for all the generations, while in the second base line approach, i.e., EDA, the solution to the optimization problem is based on the probabilistic model of the chromosome with the best fitness value. Figure 5 plots the performance of the proposed approach and two baseline approaches in terms of the number of UmBSs required and percentage of MU served as the number of MUs varies from 40 to 200. As shown in Fig. 5, for the same set of MUs the proposed algorithm serves a greater percentage of MUs with the deployment of a smaller number of UmBSs as compared to both baseline approaches. The reason behind this is that, in the execution of baseline approaches, genetic parameters are set at a fixed level for all the generations, which leads to the problem of premature convergence, while in the proposed approach, genetic parameters are dynamically adapted, which creates better population diversity for next generations. Since a single deployment of extra UmBS affects the capital expenditure of a network provider, the proposed approach is a cost-effective approach because it minimizes the

![img-6.jpeg](img-6.jpeg)

Fig. 6 Number of UmBSs required and percentage of MU serve with varying height of UmBS with $\zeta=20, \mathcal{K}=120, \mathrm{~B}_{i}=25 \mathrm{MHz}$
number of UmBSs required and maximizes the percentage of MUs served.

Figure 6 shows the number of UmBSs required along with the percentage of MU served when the height of the UmBSs varies from 40 to 200 m . When the UmBSs are deployed at a lower height, as plotted in Fig. 6, a higher percentage of MU are served by a lower number of UmBSs with all three approaches. Meanwhile, as the height of the UmBSs increases, the required number of UmBSs increases while the percentage of MUs served is reduced. This is because the association between MUs and UmBSs is constrained by a minimum SINR threshold and it is obvious that as the height of UmBSs increases, its separation from the ground MUs increases as well, lowering the value of the received SINR at MUs. Thus, to maintain the SINR threshold at each MU, the maximum coverage radius of each UmBS gets smaller as its height increases. As the
![img-7.jpeg](img-7.jpeg)

Fig. 7 Number of UmBSs required and percentage of MU serve with varying minimum MU coverage with $h_{i}=120, \mathcal{K}=120, B_{i}=25 M H z$
![img-8.jpeg](img-8.jpeg)

Fig. 8 Effect of number of MUs on the average received SINR at each MU when $\zeta=20, h_{i}=120 m, B_{i}=25 M H z$
height of the UmBSs increases, the number of MUs falling within its coverage radius decreases, so a greater number of UmBSs are required to cover all the MUs. However, the proposed approach outperforms. In the event that a network provider lacks a sufficient number of UmBSs to deploy, instead of serving all MUs, a predetermined fraction of the total MUs is served. Figure 7 shows the number of UmBSs required to serve a predefined fraction of the total MU. As shown in Fig. 7, for a higher outage percentage of MU, the performance of the three techniques is similar. However, as the outage percentage of MU decreases, the performance of the proposed method gets better and better.

The effect of the number of MUs, UmBS deployment height, and outage percentage of MUs on the SINR performance is depicted in Figs. 8, 9 and 10. For all the simulations, the available bandwidth for each UmBS is fixed at 25 MHz , hence the values of $\psi$ and $\phi$ are 20 and 6 , respectively. The other simulation parameters are mentioned in Table 5. Figure 8 plots a comparison of the proposed approach with benchmark approaches when the number of MUs varies from 40 to 200. One can observe that the average received SINR decreases when the number of MUs increases in all three approaches. This is because as the number of MUs increases, the number of UmBSs deployed also increases. This has been plotted in Fig. 5. However, the proposed approach provides a constant gain of almost 1 dB compared to the benchmark schemes. The received SINR is highly coupled with the height of the UmBSs, and the same is demonstrated in Fig. 9. It can be observed that received SINR decreases when the height of the UmBSs increases. However, the proposed approach provides a significant gain in terms of SINR compared to benchmark approaches. The effect of the MU outage on the received SINR was also investigated, and the same is

![img-9.jpeg](img-9.jpeg)

Fig. 9 Effect of deployment height of UmBSs on the average received SINR at each MU when $\zeta=20, \mathcal{K}=120, \mathrm{~B}_{\mathrm{i}}=25 \mathrm{MHz}$
illustrated in Fig. 10. It can be observed that with a small MU outage, better SINR performance can be achieved. This is because when the MU outage decreases, more UmBSs need to be deployed to serve MUs.

## 7 Conclusion

In this article, we have formulated an objective to serve the maximum number of MUs with the deployment of a minimum number of UmBSs. To achieve this objective with constraints such as minimum SINR threshold to maintain the QoS, permissible outage percentage of MUs, and minimum and maximum MU association to each UmBS, we proposed a fuzzy rule-based adaptive GA termed FRAT. Meanwhile, two evolutionary algorithms, such as the conventional GA and EDA, are considered the baseline approaches for comparative analysis. The proposed algorithm is divided into three interrelated steps. First, to reduce the computational complexity and to estimate the initial deployment locations of UmBSs, MUs are divided into clusters using the K-means technique. Next, association of MUs to the UmBSs has been fixed based on the received SINR. Then the FRAT was executed to reduce the number of UmBSs required and to increase the number of MU served. Based on the simulation results, we can conclude that our proposed algorithm outperforms when compared to two baseline approaches for the required number of UmBSs, percentage of MUs served, and received SINR.

Author contributions The authors confirm contribution to the paper as follows: Study conception and design: DM; Analysis and

![img-10.jpeg](img-10.jpeg)

Fig. 10 Effect of MUs coverage on the average received SINR at each MU when $h_{\mathrm{i}}=120, \mathcal{K}=120, B_{\mathrm{i}}=25 \mathrm{MHz}$
interpretation of results: DM; Draft manuscript preparation: DM; Supervision and draft editing: RA. All authors reviewed the results and approved the final version of the manuscript.

Funding No funding was received for conducting this study.
Availability of data and materials The author maintains the information used for analysis and simulation, but these files are not available to the public.

## Declarations

Conflict of interest The author declares that no conflict of interest exists.

Ethical approval Not applicable.

## References

1. Zhang, C., Zhang, L., Zhu, L., Zhang, T., Xiao, Z., \& Xia, X. G. (2021). 3D deployment of multiple UAV-mounted base stations for UAV communications. IEEE Transactions on Communications, 69(4), 2473-2488. https://doi.org/10.1109/TCOMM.2021. 3049387
2. Guo, J., Huang, G., Li, Q., Xiong, N. N., Zhang, S., \& Wang, T. (2021). STMTO: A smart and trust multi-UAV task offloading system. Information Sciences, 573, 519-540. https://doi.org/10. 1016/j.ins.2021.05.020
3. Wang, H., Zhao, H., Wu, W., Xiong, J., Ma, D., \& Wei, J. (2019). Deployment algorithms of flying base stations: 5G and beyond with UAVs. IEEE Internet of Things Journal, 6(6), 10009-10027. https://doi.org/10.1109/JIOT.2019.2935105
4. Liao, Z., Ma, Y., Huang, J., Wang, J., \& Wang, J. (2021). HOTSPOT: A UAV-assisted dynamic mobility-aware offloading for mobile-edge computing in 3-D space. IEEE Internet of Things Journal, 8(13), 10940-10952. https://doi.org/10.1109/JIOT.2021. 3051214

5. Kimura, T., \& Ogura, M. (2021). Distributed 3D deployment of aerial base stations for on-demand communication. IEEE Transactions on Wireless Communications, 1276(c), 1-15. https://doi.org/10.1109/TWC.2021.3086815
6. Liu, X., Liu, Y., \& Chen, Y. (2019). Reinforcement learning in multiple-UAV networks: Deployment and movement design. IEEE Transactions on Vehicular Technology, 68(8), 8036-8049. https://doi.org/10.1109/TVT.2019.2922849
7. Demirtas, A. M., Seyfioglu, M. S., Bor-Yaliniz, I., Tavli, B., \& Yanikomeroglu, H. (2021). Autonomous UAV base stations for next generation wireless networks: A deep learning approach. (pp. 1-7, online). Preprint retrieved from http://arxiv.org/abs/ 2107.13869.
8. Rains, T. (2021). Take a look at AT\&T's 'flying COWs'—drones that returned cell service to Hurricane Ida-hit Louisiana. https:// www.businessinsider.in/tech/news/take-a-look-at-atamptapossapostlying-cowsapos-drones-that-returned-cell-service-to-hurri cane-ida-hit-louisiana/slidelist/85925842.cms\#slideid=85926104.
9. Zhang, P. (2020). Huawei tests world's first 5G base station on drones. https://cntechpost.com/2020/01/02/huawei-tests-worlds- first-5g-base-station-on-drones/.
10. Fotouhi, A., Member, S., Qiang, H., Member, S., Ding, M., \& Member, S. (2019). Survey on UAV cellular communications: Practical aspects, standardization advancements, regulation, and security challenges. IEEE Communications Surveys \& Tutorials, 21, 3417-3442. https://doi.org/10.1109/COMST.2019.2906228
11. Yin, S., Li, L., \& Yu, F. R. (2020). Resource allocation and basestation placement in downlink cellular networks assisted by multiple wireless powered UAVs. IEEE Transactions on Vehicular Technology, 69(2), 2171-2184. https://doi.org/10.1109/TVT. 2019.2960765
12. Kuo, Y. C., Chiu, J. H., Sheu, J. P., \& Hong, Y. W. P. (2021). UAV deployment and IoT device association for energy-efficient data-gathering in fixed-wing multi-UAV networks. IEEE Transactions on Green Communications and Networking. https://doi. org/10.1109/TGCN.2021.3093453
13. Kuo, Y. C., Chiu, J. H., Sheu, J. P. \& Hong, Y. W. P. (2020). Energy-efficient UAV deployment and IoT device association in fixed-wing multi-UAV networks, in GLOBECOM 2020—2020 IEEE global communications conference (pp. 1-6). https://doi. org/10.1109/GLOBECOM42002.2020.9322292.
14. Shehzad, M. K., Ahmad, A., Hassan, S. A., \& Jung, H. (2021). Backhaul-aware intelligent positioning of UAVs and association of terrestrial base stations for Fronthaul connectivity. IEEE Transactions on Network Science and Engineering, 4697, 1-14. https://doi.org/10.1109/TNSE.2021.3077314
15. Qiu, C., Wei, Z., \& Yuan, X. (2020). Multiple UAV-mounted base station placement and user association with joint Fronthaul and Backhaul optimization. IEEE Transactions on Communications, 68(9), 5864-5877. https://doi.org/10.1109/TCOMM.2020. 3001136
16. Aydin, Y., Kurt, G. K., \& Member, S. (2021). Group handover for drone-mounted base stations. IEEE Internet of Things Journal, 8(18), 13876-13887. https://doi.org/10.1109/JIOT.2021. 3068297
17. Wang, L., Hu, B., \& Chen, S. (2020). Energy efficient placement of a drone base station for minimum required transmit power. IEEE Wireless Communications Letters, 9(12), 2010-2014. https://doi.org/10.1109/LWC.2018.2808957
18. Youssef, M. J., Nour, C. A., Farah, J., \& Douillard, C. (2019). Backhaul-constrained resource allocation and 3D placement for UAV-enabled networks, in IEEE 90th vehicular technology conference (VTC2019-Fall) (pp. 1-7). https://doi.org/10.1109/ VTCFall.2019.8891385.
19. Liu, W., Niu, G., Cao, Q., Pun, M. O., \& Chen, J. (2019). 3-D placement of UAVs based on SIR-measured PSO algorithm. https://doi.org/10.1109/GCWkshps45667.2019.9024696.
20. Sun, X., Ansari, N., \& Fierro, R. (2020). Jointly optimized 3D drone mounted base station deployment and user association in drone. IEEE Transactions on Vehicular Technology, 69(2), 2195-2203. https://doi.org/10.1109/TVT.2019.2961086
21. Zhang, Q., Saad, W., Bennis, M., \& Member, S. (2021). Predictive deployment of UAV base stations in wireless networks: Machine learning meets contract theory. IEEE Transactions on Wireless Communications, 20(1), 637-652. https://doi.org/10. 1109/TWC.2020.3027624
22. Li, X. (2018). Deployment of drone base stations for cellular communication without apriori user distribution information, in 37th Chinese control conference (pp. 7274-7281). https://doi.org/ 10.23919/ChCC.2018.8482797.
23. Ozturk, M., Nadas, J. P. B., Klaine, P. H. V., Hussain, S., \& Imran, M. A. (2020). Clustering based UAV base station positioning for enhanced network capacity, in 2019 international conference on advances in the emerging computing technologies, AECT 2019 (pp. 3-8). https://doi.org/10.1109/AECT47998.2020.9194188.
24. Sharma, N., Kumar, A., Pervaiz, H., Magarini, M., Musavian, L., Alam, M. M., Jindal, A., \& Imran, M. A. (2021). Aerial base station assisted cellular communication: Performance and tradeoff. IEEE Transactions on Network Science and Engineering, 8(4), 2765-2779. https://doi.org/10.1109/TNSE.2021.3052984
25. Zhang, S., \& Ansari, N. (2020). 3D drone base station placement and resource allocation with FSO-based Backhaul in hotspots. IEEE Transactions on Vehicular Technology, 69(3), 3322-3329. https://doi.org/10.1109/TVT.2020.2965920
26. Huang, H., Huang, C., \& Ma, D. (2020). A method for deploying the minimal number of UAV base stations in cellular networks. IEEE/CAA Journal of Automatica Sinica, 7(2), 559-567. https:// doi.org/10.1109/JAS.2019.1911813
27. Dai, H., Zhang, H., Wang, B., \& Yang, L. (2019). The multiobjective deployment optimization of UAV-mounted cache-enabled base stations. Physical Communication, 34, 114-120. https://doi.org/10.1016/j.phycom.2019.03.007
28. Ahmed, A., Awais, M., Akram, T., Kulac, S., Alhussein, M., \& Aurangzeb, K. (2019). Joint placement and device association of UAV base stations in IoT networks. Sensors (Switzerland), 19(9), 1-16. https://doi.org/10.3390/s19092157
29. Qin, J., Wei, Z., Qiu, C., \& Feng, Z. (2019). Edge-prior placement algorithm for UAV-mounted base stations. https://doi.org/ 10.1109/WCNC.2019.8885992.
30. Zhang, L., \& Ansari, N. (2019). On the number and 3-D placement of in-band full-duplex enabled drone-mounted base-stations. IEEE Wireless Communications Letters, 8(1), 221-224. https://doi.org/10.1109/LWC.2018.2867501
31. Kalantari, E., Yanikomeroglu, H., \& Yongacoglu, A. (2016). On the number and 3D placement of drone base stations in wireless cellular networks. https://doi.org/10.1109/VTCFall.2016.7881122.
32. Zhao, H., Wang, H., Wu, W., \& Wei, J. (2018). Deployment algorithms for UAV airborne networks toward on-demand coverage. IEEE Journal on Selected Areas in Communications, 36(9), 2015-2031. https://doi.org/10.1109/JSAC.2018.2864376
33. Lyu, J., Zeng, Y., Zhang, R., \& Lim, T. J. (2017). Placement optimization of UAV-mounted mobile base stations. IEEE Communications Letters, 21(3), 604-607. https://doi.org/10.1109/ LCOMM.2016.2633248
34. Bidabadi, N. (2018). Using a repair genetic algorithm for solving constrained nonlinear optimization problems. Journal of Information and Optimization Sciences. https://doi.org/10.1080/ 02522667.2017.1395146

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightisholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.
![img-11.jpeg](img-11.jpeg)
algorithms, UAV communication.

Dilip Mandloi received his M.E. degree in Electronics and Communication Engineering from the Rajiv Gandhi Prosidyogiki Vishwavidyalaya, Bhopal, in 2012. From 2019 he is pursuing his Ph.D. from Electronics and Communication Engineering Department of National Institute of Technology, Patna, Bihar, India. He is currently working on the application of unmanned aerial vehicles in wireless communication. His research interest includes Path planning
![img-12.jpeg](img-12.jpeg)

Rajeev Arya received the Engineering Degree in Electronics and Communication Engineering from Government Engineering College, Ujjain, (RGPV University, Bhopal) India and the Master of Technology in Electronics and Communication Engineering from Indian Institute of Technology (ISM), Dhanbad, India. He received the Ph.D. degree in Communication Engineering from Indian Institute of Technology (IIT Roorkee), Roorkee, India. He has received Ministry of Human Resource Development Scholarship (MHRD India) during M.Tech. and Ph.D. He is currently an Assistant Professor with the Department of Electronics \& Communication Engineering at National Institute of Technology, Patna, India. His current research interests are Communication Systems and Wireless Communication.