# UAV path optimization with an integrated cost assessment model considering third-party risks in metropolitan environments 

Bizhao Pang ${ }^{\text {a }}$, Xinting $\mathrm{Hu}^{\mathrm{a}}$, Wei Dai ${ }^{\mathrm{a}, \mathrm{b}}$, Kin Huat Low ${ }^{\mathrm{a}, *}$<br>${ }^{a}$ School of Mechanical and Aerospace Engineering, Nanyang Technological University, Singapore 639798, Singapore<br>${ }^{\mathrm{b}}$ Air Traffic Management Research Institute, Nanyang Technological University, Singapore 637460, Singapore

## A R TICLE INFO

Keywords:
Unmanned aircraft system
Third party risk
Flight path optimization
Hybrid algorithm
Reliability analysis

A B STR A C T

Various applications of unmanned aerial vehicles (UAVs) in urban environments facilitate our daily life and public services. However, UAV operations bring third party risk (TPR) issues, as UAV may crash to pedestrians and vehicles on the ground. It may also cause property damages to critical infrastructures and noise impacts to the public. Path planning is an effective method to mitigate these risks and impacts by avoiding high-risk areas before flight. However, most of the existing path planning methods focus on minimizing flight distance or energy cost, rarely considered risk cost. This paper develops a novel flight path optimization method that considers an integrated cost assessment model. The assessment model incorporates fatality risk, property damage risk, and noise impact, which is an extension of current TPR indicators at modeling and assessment levels. To solve the proposed integrated cost-based path optimization problem, a hybrid estimation of distribution algorithm (EDA) and CostA* (named as EDA-CostA*) algorithm is proposed, which provides both global and local heuristic information for path searching in cost-based environments. A downtown area in Singapore is selected for the case study. Simulation results demonstrate the effectiveness of the developed cost-based path optimization model in reducing the risk cost. The statistical analysis for 100 sampled environments also shows the reliability of the proposed method, which reduced the cost by [42.64\%, 44.15\%] at $95 \%$ confidence level.

## 1. Introduction

Applications of advanced air mobility [1] have been extensively seen in urban areas for various cases such as traffic monitoring, aerial photography, delivery, etc. Projection also shows that drone operations in metropolitan areas will continue to rise [2]. To handle large-scale UAV operations with different tasks, the autonomous flying capability is crucial. As one of the key enablers of autonomous flying, path planning problems have been widely investigated with purposes of minimizing flight distance and operational cost [3], energy consumption [4], or maximizing coverage rate for surveillance missions [5]. However, third-party risk issues are essential for UAVs operating in metropolitan areas, as UAVs may crash due to loss of control or navigation [6]. A crashed UAV may cause fatalities to people [7] and damages to properties [8]. UAV operating in low-altitude airspace also brings societal issues like noise impact to the public [9], which needs to be mitigated in the path planning phase [10]. In this paper, we investigate the questions of how to quantitively assess various UAV operational risks, and how to effectively mitigate these risks by using a cost-based path optimization
method.
Existing studies have investigated the risk assessment problems of UAV operation, and they focused on impact probability and severity models to people and vehicles on the ground. The authors [11] presented main mathematic models for conflict and collision probability estimation, which provide insights for collision risk assessment of AAM. Pioneer works studied the probability of fatalities and the fatality rates associated with a ground impact on pedestrians, and analysis results showed that the risk of fatality to humans is low in the condition of light UAV operates in areas with low population density [8]. The probability model of UAV to road traffic was also established. The authors [12] defined the possible ground impact area of falling UAV and developed the collision probability model, which helps for the identification of main risky areas of the road network. Follow-up works studied the impact severity of UAV on people and they subsequently proposed the weight threshold of falling UAV impact ground people based on the injury scale and criterion [7][13]. Based on the UAV impact probability and severity studies, the researcher proposed a risk-based approach for small UAV operations [14] and generated the probabilistic map using

[^0]
[^0]:    * Corresponding author.

    E-mail address: mkhlow@ntu.edu.sg (K.H. Low).

Monte Carlo simulation for more accurate ground impact risk analysis [15].

Recent studies paid attention to third-party risk modeling and analysis for UAS operations. The third-party risk was defined as risks on human life and property damage that are not onboard the UAV [13,16, 17]. In subsequent studies, a third-party risk framework was proposed to analyze the UAV ground impact risk [16]. Third-party risk indicators and their utilization in safety regulations were proposed [18] and the authors further extended the indicators with societal and individual risks [17]. By using these proposed frameworks, some practical studies have been conducted to model the third-party risk in urban environments [19,20], and the level of risk for UAV system was also proposed to identify critical areas and actions [21]. The analysis and modeling of these risks facilitate the generation of the risk-aware map, which can be used for risk-based path planning to achieve safer UAV operations in metropolitan environments.

UAV path planning problems have also been studied with different models and optimization objectives. There were exact methods like the Dijkstra algorithm [22], heuristic algorithms like A* [23], and swarm-based heuristic methods [24]. These methods have various optimization objectives like minimizing travel distance and cost, maximizing flight duration. These methods always consider obstacle avoidance but ignore risks underneath the UAV flying path. Extended from conventional distance-based path planning problems, the risk-based one has relied on a risk map used for path planning [25]. Various methods and algorithms were developed to generate the risk map and to solve the risk-based path planning problems. The A*-based algorithms, for instance, were developed together with Dubins Curves for risk-based path planning and smoothing [26]). In the follow-up study, the authors [27] developed a RiskA* algorithm to minimize the risk of the produced path, and a conflict-free A* [28] was proposed to handle flight conflicts and mitigate delays. Genetic algorithm and Dijkstra methods are also popular in addressing this type of problems [29,30]. Other methods like the Markov decision process were used with a hierarchical method to maximize efficiency and minimize risks [31]. A rapidly exploring random tree was proposed to minimize the third-party risk of UAV takeoff trajectories [32]. The Tabu search algorithm was employed to optimize the UAV route to minimize the cost of damaged cargo [33]. What is more, the authors [34] also developed a risk-aware graph search algorithm to select paths that have a lower risk cost. On the other hand, the UAV operational environments have also been covered from the factory-like area [31] to inhabited areas [35] and urban environments [36]. In different areas, the risk types are various. For instance, in factory areas, the main risk sources are critical infrastructure and property damages. While in the inhabited area and urban areas, population and vehicle density, high-rise buildings are more important for risk-based path planning.

Overall, existing studies have investigated the probability and severity models of UAV ground impact on pedestrians and vehicles. However, these models always consider population density as an average value, which may fail to capture the population density distribution that is a primary contributor in risk modeling. There are also less studies have worked on the property damage risk and noise impact issues at modeling and assessment levels, which are two important societal factors when UAVs operate in metropolitan areas. What is more, existing methods rarely consider an integrated cost assessment to cope with various risk costs for UAV flight path optimization, and even fewer studies have investigated the cost-based heuristic algorithm to improve the performance and reliability of the path searching result.

In this paper, we develop a novel UAV flight path optimization method that considers an integrated cost assessment model. A hybrid algorithm is developed to solve the path optimization problem in costbased environments. The performance of the developed method is demonstrated by a set of case studies and simulations. The main contributions of this paper are summarized as follows:
(1) We extend the third-party risk with two societal indicators of property damage risk and noise impact at modeling and assessment levels. The correlation between property damage risk and building height is established as a log-normal distribution model. The introduced noise impact model enables noise mitigation in UAV flight path optimization.
(2) We propose a novel path optimization method that considers an integrated cost assessment model. The integrated model incorporates fatality risk, property damage risk, and noise impact where a gravity model is introduced to estimate the population density distribution in a finer scale.
(3) We develop a hybrid algorithm integrating estimation of distribution algorithm and the proposed CostA* algorithm (named as EDA-CostA*) to solve the cost-based path optimization problems. The outer loop of EDA-CostA* algorithm is to solve a 0-1 optimization problem, which aims for optimizing the feasible region and estimating the heuristic value. The estimated heuristic value is ingested in the inner loop where the CostA* algorithm is used to generate the cost-effective flight path.

The rest of the paper is structured as follows: Section 2 discusses the societal indicators of third-party risk in urban environments with illustrations of risk cost-based path planning. The risk cost modeling and assessment are presented in Section 3. Section 4 proposes the UAV flight path optimization model with an integrated cost assessment model and also develops the solution algorithm. This is followed by case studies and simulations in Section 5. Section 6 concludes the research findings of this paper.

## 2. Problem background

### 2.1. Risk and impact factors in urban environments

In metropolitan environments, there are dense populations, high-rise buildings, critical infrastructure, etc. UAVs operating in such lowaltitude airspace will encounter various risk issues [37]. In this paper, the scope of operation altitude is below 400 feet above ground level [38]. Recent studies investigated various risks in urban environments, and most of their attentions are on the risks of the impact on ground people and vehicles [13,39], midair collision with small UAVs and manned aircraft [40-42], noise impact [9], as well as UAV operational cost and efficiency [3]. We conclude the primary risk and impact factors, as illustrated in Fig. 1.
(1) Fatality risk: Crashed UAV impacts pedestrians and vehicles on the ground, causing fatalities on people.
(2) Property damage risk: Crashed UAV hits critical infrastructures or collides with high-rise buildings, causing property loss.
(3) Noise impact: Noise impact to the public is a big concern for the acceptance of UAV operations in urban environments, which will be assessed and mitigated.

The risk factor of midair collision between UAV and manned aircraft in urban airspace [43] is not considered in this work, as the aerodrome control zone is treated as a restricted area where the UAV is strictly not allowed to enter. Risks of UAVs intruding military-related bases and facilities are also out of the scope of this study.

The risk factors of population density, vehicle density, and buildings are discretely distributed in metropolitan environments. Subdivision of airspace into smaller units enables a more flexible managing [44,45]. To quantitatively assess these risks, urban low-altitude airspace is divided into discrete three-dimension air block units [6] and the centroid of the unit is denoted as the vertex $v_{g g g}$ (Fig. 2(a)). UAV has 26 possible choices to move from one vertex to another, and it follows the centroid point to maintain safe separation with other UAVs in adjacent air blocks. Risk cost assessment of each airspace unit is conducted based on its

![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of fatality risk, property damage risk, and noise impact of UAV operations in metropolitan environments.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Illustrations of risk-based airspace and flight path planning.
pertaining environments such as population density and vehicle density underneath. The risk is represented as colored air blocks (Fig. 2(b)), and the 3D cost-based flight path is illustrated in Fig. 2(c). UAVs operate in complex 3D risk map to avoid high-risk areas (presented as red color) and to minimize total operational risk cost.

### 2.2. Definition of equation terms used in this paper

This paper studies the UAV path optimization problem considering an integrated risk cost assessment model. In the development of the problem and model, multiple equation terms and notations are used and can be classified into three aspects: (1) third party risk modeling and assessment, (2) formulation of UAV path optimization, (3) solution algorithm development. All the equation terms and notations used in these developments are defined and explained in Table 1.

## 3. Risk modeling and assessment

The integrated cost assessment model includes three parts: fatality risk cost model, property damage risk cost model, and noise impact cost model. We develop the corresponding models for the cost assessment.

### 3.1. Fatality risk cost model

Fatality risk cost is defined as the cost that UAV crashes to pedestrians and persons in ground vehicles, and the unit is the number of fatalities per flight hour. The fatality risk cost is denoted as $c_{s, f}$, and it
consists of the fatality risk cost to pedestrians $c_{s, p}$ and to the person in the vehicle $c_{s, v}$.
$c_{s, f}=c_{s, p}+c_{s, v}$

### 3.1.1. Fatality risk to pedestrians

UAVs may lose control and crash to pedestrians on the ground (see Fig. 1). To evaluate the fatality risk cost to pedestrians, there are three processes [17,25] need to be considered: (1) system failure of UAV; (2) UAV crashes to pedestrians; and (3) fatal damages caused to the pedestrians. That falling UAV hits people on the ground causing fatalities is a sequential action, which associates with the three processes mentioned above. The risk cost of UAV crashes to pedestrians $c_{s, p}$ is defined as the number of fatalities per flight hour, denoted as
$c_{s, p}=P_{\text {crash }} N_{\text {lin }}^{p} R_{f}^{p}$
where $c_{s, p}$ is the risk cost associated with the fatality of pedestrians, and $P_{\text {crash }}$ is the probability of UAV system failure. Note that $N_{\text {lin }}^{p}$ is the number of pedestrians hit by crashed UAV (correlated with population density), and $R_{f}^{p}$ is the fatality rate that people killed in UAV accidents.

The $P_{\text {crash }}$ is primarily determined by the reliability of the UAV system itself, including hardware and software reliabilities. The $R_{f}^{p}$ is correlated with the weight and falling height of the UAV. The uncertain variable in Eq. (2) is $N_{\text {lin }}^{p}$, which is associated with the population density, defined as

Table 1
Definition of equation terms used in this paper.
$N_{b h}^{0}=S_{\text {,hit }} \sigma_{g}$
where $S_{\text {,hit }}$ is the size of UAV crash impact area, and $\sigma_{g}$ is the population density in the administrative unit.

The fatality rate $R_{f}^{0}$ associated with two main factors: impact kinetic energy and sheltering effects. The kinetic energy $E_{\text {imp }}$ of falling UAV primarily determines the severity of impact, while the sheltering coefficient $S_{e}$ affects the degree of impact on the people and vehicle, as the buffering effects of buildings and trees will soften the impact. The sheltering coefficient $S_{e}$ is introduced as the absolute real number $S_{e}=$ $(0,1]$ [46], and the fatality rate is presented as
$R_{f}^{0}=\frac{1}{1+\sqrt{\beta}\left(\frac{\rho}{c_{\text {out }}}\right)^{\frac{1}{16}}}$
where $\alpha$ is the impact energy that might cause $50 \%$ fatality with $S_{e}=$ 0.5 , while $\beta$ is the impact energy threshold required to cause fatality as $S_{e}$ approaching zero (see Fig. 2 in [8]). Based on that, we take $\alpha=10^{6} \mathrm{~J}$ and $\beta=100 \mathrm{~J}$.

The impact kinetic energy $E_{\text {imp }}$ of the falling UAV is known as
$E_{\text {imp }}=\frac{1}{2} m v^{2}$
where $m(\mathrm{~kg})$ is the mass of the falling UAV, and $v$ is the velocity when the UAV hits the ground. The processes to compute $v$ will be presented next.

The vertical drag force $F_{d}$ of falling UAV is related to its size and materials, as well as the density of air, etc., denoted by [7]
$F_{d}=\frac{1}{2} R_{f} S_{\text {,hit }} \rho_{A} v_{\text {TAS }}^{2}$
where $R_{f}$ is the drag coefficient that is related to the UAV type, and $\rho_{A}$ is the density of air ( $1.225 \mathrm{~kg} / \mathrm{m}^{3}$ at sea level), and $\nu_{\text {TAS }}$ is the true airspeed of the falling UAV.

The acceleration of UAV can be then presented as
$a=\frac{F_{g}-F_{d}}{m}=g-\frac{R_{f} S_{\text {,hit }} \rho_{A} v_{\text {TAS }}^{2}}{2 m}$
where $F_{g}$ is the gravitational force, $F_{g}=m g\left(g=9.8 \mathrm{~m} / \mathrm{s}^{2}\right)$.
Thus, the velocity $v$ of UAV hits the ground at moment $t$ can be obtained as
$v=\int_{0}^{t}\left(g-\frac{R_{f} S_{\text {,hit }} \rho_{A} v_{\text {TAS }}^{2}}{2 m}\right) d t=\sqrt{\frac{2 m g}{R_{f} S_{\text {,hit }} \rho_{A}}\left(1-e^{-\frac{m v^{2}-v^{2} \rho_{A} v^{2}}{2 m}}\right)}$
where $h$ is the falling height of the UAV above ground level.

### 3.1.2. Fatality risk to persons in the vehicle

Fatality risk cost to persons in the vehicle is modelled and there are also three components of a crash UAV accident on vehicles [12]: (1) UAV system failure; (2) falling UAV hits a vehicle; (3) the crash accident causes a direct fatality to people or causes a traffic accident which subsequently kills persons in the vehicle.

Fatality risk cost that UAV crashes to persons in the vehicles is defined as the number of fatalities per flight hour, denoted as
$c_{v, v}=P_{\text {crash }} N_{\text {hit }}^{v} R_{f}^{v}$

where $N_{\text {int }}^{c}$ is the number of vehicles hit by the crashed UAV, and $R_{t}^{c}$ is the average fatality rate that persons in vehicles are killed in accidents, which can be obtained by: (annual total fatalities caused by car accidents) / (annual total number of car accidents).

The average number of vehicles that might be hit by crashed UAV can be defined as the ratio of the total projected area of all vehicles and the total road area, denoted as
$N_{\text {int }}^{c}=S_{\text {_hit }} \sigma_{v}$
in which $S_{\text {_hit }}$ is the size of UAV crash impact area, and $\sigma_{v}$ is the vehicle density in a road network.

### 3.1.3. Estimation of population density and traffic density

The population density and traffic density distributions in metropolitan environments are essential variables that directly influence the UAV operational risk costs as discussed in Eqs. (3) and (10). Based on the previous studies, these density distributions are correlated with the consumption amenities [47], which attracts people and vehicles. To quantitively assess this correlation between urban amenity and population density, the gravity model is used [48]. Inspired by the gravity model [49] and the population mapping method [50], we have the following formulas to estimate the population density in urban environments.

The estimated population density of a given area unit $\sigma_{p}$ is defined as
$\sigma_{p}=e^{\left(1-r^{2}\right)} \sigma_{\mathrm{v}, \text { avg }}$
where $\sigma_{\mathrm{p}, \text { avg }}$ is the average population density in the whole given area. Note that $r$ is the radius of the gravity influence area induced by the amenity, which is given as 1 km in this work. As shown in Fig. 3, the population density decreases in an inverted exponential pattern with the increase of the radius $r$. In the first 0.3 km of $r$, the population density index remains high, which captures the high population density distribution in the vicinity of amenities. While in the range of 0.3 km to 1.0 km , the index drops linearly, presenting an even decreasing trend of population density.

Similarly, the estimated road vehicle density in a given area unit can be denoted as
$\sigma_{v}=e^{\left(1-r^{2}\right)} \sigma_{\mathrm{v}, \text { avg }}$
where $\sigma_{\mathrm{v}, \text { avg }}$ is the average traffic density in the given area.

### 3.2. Property damage risk cost model

Dense high-rise building in urban environments is another challenge
![img-2.jpeg](img-2.jpeg)

Fig. 3. Illustration of population density index changes with influence radius $r$.
for UAV operations. Potential collisions with buildings pose property damage risks, and densely distributed high-rise buildings also limit the speed of traffic flow, resulting in the inefficiency of the UAS system [51]. The property damage risk cost model also integrates the operational efficiency cost, which is accounted for planning and optimization of airspace and traffic flow.

The flight altitude is a primary variable of the property damage risk model. As Fig. 4(a) depicted, in the low-altitude layer (Layer 1, for instance), the density of the building is high. UAV operating in Layer-1type airspace needs to frequently perform deconfliction to avoid obstacles, increasing risks and efficiency loss. In the high-altitude layer (i. e., Layer 4), in contrast, there are few buildings to affect UAV operations, so that the operational safety and efficiency can be significantly improved. Here, we assume that the operation will be affected if the flight distance of a drone from buildings is smaller than the separation minima. The building density distribution in different heights plays a key role in property damage risk modeling, which is correlated with the collision probability of UAVs with buildings. The building height distribution is not fit with standard normal distribution but log-normal distribution [52,53], as building height is the nonnegative value and its distribution is not symmetrical. Based on these characteristics, the correlation between building height and property damage risk cost $c_{v, p, d}$ is established as
$\psi(h ; \mu, \sigma)=\frac{1}{h \sigma \sqrt{2 \pi}} e^{-\frac{(\sigma-\mu)^{2}}{2 \sigma^{2}}}$
$c_{v, p, d}=\left\{\begin{array}{c}\psi\left(e^{\mu}\right), 0<h \leq e^{\mu} \\ \psi(h), h>e^{\mu}\end{array}\right.$
where $h$ is the building height, $\mu$ and $\sigma$ are the mean and standard deviation of the logarithmic variable. Note that $c_{v, p, d}$ is the risk cost of property damage upon drone operation. For buildings with a height smaller than the threshold of $e^{\mu}$, the risk cost equals the one which the height $e^{\mu}$ has (as Eq. (14) defines). This could be due to the fact that the buildings below that height $\left(h=e^{\mu}\right)$ are dense and the risks are high. The biggest risk cost value is therefore taken as the one with height $h=$ $e^{\mu}$. In this study, the building density and height data are obtained from a downtown area (size: $6 \mathrm{~km} \times 6 \mathrm{~km}$ ) in Singapore. A total number of 3366 buildings are included in the selected area. By computing statistical features, the mean value for the log-normal distribution is obtained as $\mu=3.0467$. While for buildings with a height greater than $e^{\mu}$, the operational risk cost is computed as the log-normal distribution presents in Eq. (13). Meaning that with the increase of building height $\left(h>e^{\mu}\right)$, the property damage risk cost decreases, as in higher layers there are fewer building obstacles to influence safe operations of UAV. Note that the property damage risk factor is to facilitate the determination of optimal flight layer in particular areas.

### 3.3. Noise impact cost model

Noise impact is another important societal issue and needs to be mitigated when UAVs operate in low-altitude urban environments [9]. That should be therefore considered as a cost when conducting UAV flight planning. The impact of noise on the public is in effect when UAVs operate close to people, especially at nighttime. While with the increase of flying altitude, the impact will decrease to the threshold which will not have effects for people on the ground. The correlation of noise impact cost and its flying height is illustrated in Fig. 5. As we can see from the figure, the key factor of noise impact cost is UAV flying height, as the sound propagation is correlated with the height and distance of UAV away from the people.

An approximation of sound propagation is the spherical spreading, which can be presented as
$I(s i)=\frac{1}{h^{2}+d^{2}}$

![img-3.jpeg](img-3.jpeg)

Fig. 4. Building obstacles impact on UAV safe and efficient operations in urban areas. In (a), the building height data is selected from a particular area (size: $6 \mathrm{~km} \times$ 6 km ) in Singapore, where 100 building clusters have been selected to illustrate the building height distribution. In (b), the statistical features of building height distribution are analyzed using log-normal distribution. Here, the height frequency presents the number of buildings at a certain height.
![img-4.jpeg](img-4.jpeg)
(a) Illustration of noise impact on people
![img-5.jpeg](img-5.jpeg)
(b) Log-normal distribution of building height

Fig. 5. UAV noise impacts on people.
where $I(s l)$ is the sound intensity at height $h$ and distance $d$ from the point directly under the UAV. Here $d$ is taken as 30 feet [54]. The sound intensity is further converted as sound level,
$L(s l)=\omega \mathrm{L}_{h} I(s i)$
in which $L(s l)$ is the sound level (dB); $\omega$ is the conversion factor from sound intensity to sound level; $\mathrm{L}_{h}$ is the reference noise produced by drone, taken as $\mathrm{L}_{h}=55 \mathrm{~dB}[55]$.

Cost of noise impact upon UAV operations is correlated with sound level (dB), denoted as
$c_{\text {noise }}=L(s l)=\omega \mathrm{L}_{h} \frac{1}{h^{2}+d^{2}}$
where $c_{\text {noise }}$ is the cost of noise impact upon drone operation in the given airspace unit. Noise impact will not be considered as a cost for UAV operation if flying height exceeds the threshold. Based on previous studies [56,57], we take the height threshold as the one that corresponds to the noise level of 40 dB , illustrated as Fig. 5(b).

## 4. Cost-based UAV flight path optimization

In this Section, the cost-based path planning is modelled, and the solution algorithm is also developed. First, we propose an integrated cost model for the optimization of the UAV flight path considering fatality risk, property damage risk, and noise impact. Based on the integrated cost model, we formulate the cost-based path planning as a minimum cost flow problem in an undirected graph. To solve the formulated problem, we propose a hybrid algorithm that incorporates estimation of distribution algorithm (EDA) and CostA* algorithm.

### 4.1. Integrated cost model

The total operational cost integrates fatality risk cost, property damage risk cost, and noise impact cost. As the weightage of these three types of cost might be different due to their significance or user's preferences, the contribution of each type of cost will also be various. For instance, aviation regulators may take safety as the top priority, requiring a very low fatality risk cost of UAV operation. In this regard,

the weight of fatality cost should be increased. By doing so, areas with dense populations and vehicles will be identified as high-risk areas by the proposed model, and the path planning will subsequently avoid these areas. To quantify the significance and preferences of UAS stakeholders on different risk types, the weight factor $\alpha_{t}$ is introduced. As the three risk cost factors are exclusive and are normalized into the range of $(0,1]$, the integrated cost assessment model is developed as an additive linear model

$$
c_{t}=\sum_{i=1}^{3} \alpha_{t} \omega_{t} c_{t}
$$

where $c_{t}$ is the integrated cost of a vertex. Here $\alpha_{t}$ is weight factor, $\omega_{t}$ is normalization factor and $c_{t}$ is the cost value. Note that $\tau=\{1,2,3\}$ corresponds to fatality risk, property damage risk, and noise impact, respectively. Here $\left\{\alpha_{t}: \alpha_{1}, \alpha_{2}, \alpha_{3}\right\} \in[0,1]$, and $\alpha_{1}+\alpha_{2}+\alpha_{3}=1$. Note that $\left\{\omega_{t}: \omega_{1}=\omega_{t, 1}, \omega_{2}=\omega_{t, p, 4}, \omega_{3}=\omega_{\min }\right\}$, and $\left\{c_{t}: c_{1}=c_{t, 1}, c_{2}=\right.$ $\left.c_{t, p, 4}, c_{3}=c_{\max }\right\}$.

The normalization factor $\omega_{t}$ is used to eliminate the magnitude effect among different risk types [58]. The cost $c_{t}$ is divided by the maximum cost value $c_{t, \max }$. Here $c_{t, \max }$ is defined as the maximum cost value among all vertices in a given environment. For example, the given environment has meshed into standard airspace units that have 100 vertices. The fatality risk is computed for all vertices and the maximum cost value is ten, for instance. Then, the fatality risk value of all 100 vertices will be divided by ten, and all the cost values will fall in the range of $(0,1]$. The correlation between the normalization factor and the maximum cost value is denoted as
$\omega_{t}=\frac{1}{c_{t, \max }}$

### 4.2. Problem formulation of cost-based path planning

To facilitate the cost assessment, airspace is divided into uniform three-dimensional units. These units consist of vertices and edges and can be represented as a graph. The cost-based path planning problem is a special case of the minimum cost flow problem, which is to find a path in the graph from origin to destination with minimum cost. We modelled the problem as follows:

Let $G=(V, E, C)$ be an undirected, connected and weighted graph for which

- $V=\left\{v_{1}\left(x_{1}, y_{1}, z_{1}\right), v_{2}\left(x_{2}, y_{2}, z_{2}\right), \ldots, v_{n}\left(x_{n}, y_{n}, z_{n}\right)\right\}, n \in \mathbb{N}$ presents the finite set of graph vertices of the divided airspace.
- $E \subset V \times V$ denotes the finite set of edges connecting the vertices in the graph.
- $C: E \rightarrow \mathbb{R}_{\mathrm{ij}}^{+}$presents the weight function of edge.

In this paper, the weight represents the cost of the edge. The cost of an edge $e_{t}\left(v_{t}, v_{t+1}\right)$ can be denoted as $c_{e_{t}}$. The integrated cost is given to the vertex of the airspace unit centroid. To align with that, the cost of the edge $c_{e_{t}}$ is represented by the cost of the vertex on the edge, denoted as $c_{e_{t}}$. The weight function of the edge is equivalent to the cost function of the vertex as shown in Eq. (18). Let $s$ and $t$ be distinct vertices of $G$. A path $P$ from $s$ to $t$ in $G$ is called the most cost-effective path if $C_{P}$ is minimum among all paths from $s$ to $t$ in $G$.

The objective of this work is to optimize the integrated cost of the planned path, denoted as
$\min : C_{P}=\sum_{v_{i} \in V_{P}} c_{v_{i}}$
where $C_{P}$ is the total cost of path $P$, and $c_{v_{i}}$ is the cost of vertex $v_{i}$. Note that $V_{P}$ is the set of vertices on path $P$.

As Fig. 2(a) shows, 26 available vertices can be chosen as the next point to move. Specifically, six vertices are straightly connected with the
current vertex, while 12 vertices are connected as planar diagonal and eight vertices are connected as cubical diagonal. To ensure the planned flight path is operationally valid in the sense that a complete sequence of waypoints is provided for autonomous navigation, the constraint of waypoint selection is presented as

$$
\left\{\begin{array}{c}
x_{i+1}=x_{i}+\delta_{i}^{\prime} \\
y_{i+1}=y_{i}+\delta_{i}^{\prime} \\
z_{i+1}=z_{i}+\delta_{i}^{\prime} \\
\delta_{i}^{\prime}, \delta_{i}^{\prime}, \delta_{i}^{\prime} \in\{-\lambda, 0, \lambda\}
\end{array}\right.
$$

where $\left(x_{i+1}, y_{i+1}, z_{i+1}\right)$ is the next path point $v_{i+1}$ choosing to move, and $\left(x_{i}, y_{i}, z_{i}\right)$ is the current position $v_{i}$. Note that $\delta_{i}^{\prime}, \delta_{i}^{\prime}$, and $\delta_{i}^{\prime}$ are the movements corresponding to $x$-axis, $y$-axis, and $z$-axis, respectively. The step size of the movements is $\lambda$.

Another constraint is to ensure the planned flight does not collide with buildings. The path of UAV flight should not enter the airspace units that are occupied by buildings
$u_{t} \in U_{O b e}, k \geq 0$
in which $u_{k}$ is the building-occupied airspace unit, and $U_{O b e}$ is the set of all the building-occupied units. The motivation of making Eq. (22) as a constraint is to improve the computational efficiency. The buildingoccupied airspace blocks will be disabled during the path searching process, and it will not be evaluated by the fitness function that is the most time-consuming part in the algorithm.

### 4.3. Solution algorithm for cost-based path planning

This section develops a hybrid algorithm to solve the cost-based path optimization problem. The algorithm incorporates the estimation of distribution algorithm (EDA) and the $\mathrm{A}^{*}$ algorithm. To improve the computational efficiency, the $k$-means method is introduced to identify low-cost clusters that are used as local heuristic guidance for path searching. Detailed developments of the algorithm are presented in the following sections.

### 4.3.1. EDA-A* algorithm for cost-based path planning

To solve the developed cost-based path optimization problem, there are several types of algorithms we can choose. The exact method, like the Dijkstra, is one of the classic and effective methods for graph-based path-searching. However, Dijkstra is a computational inefficiency method, especially in dealing with large-scale problems like the one in this paper. To improve the efficiency, an extension of the Dijkstra method was made with heuristic information, and a new algorithm called the $\mathrm{A}^{*}$ algorithm was developed [23]. The computational efficiency of the $\mathrm{A}^{*}$ algorithm is significantly higher than the Dijkstra method. While the $\mathrm{A}^{*}$ algorithm can still be an exact method if an appropriate heuristic value can be obtained. In the distance-based environment (Fig. 6(a)), the heuristic value can be surely obtained either as Manhattan distance or Euclidean distance. However, in the cost-based environment (Fig. 6(b)), an appropriate heuristic value is difficult to be obtained because the distribution of cost values is uneven and unpredictable in different airspace units.

If the heuristic value is taken too big, it may exceed the lower bound and that reduces the heuristic effectiveness. In contrast, if the heuristic value is too small, although it might be within the lower bound, the computational efficiency will be significantly reduced. Finding a proper heuristic value can make a good compromise between solution quality and computational efficiency. That motivates this paper to propose a global optimization method to assist the estimation of the exact lower bound. What is more, as the scale of the problem gets larger, it becomes more difficult for the heuristic methods that are initiated with only one solution to search for the outstanding solutions from the feasible region.

![img-6.jpeg](img-6.jpeg)

Fig. 6. Illustration of heuristic value in the distance-based environment and the cost-based environment. Note that (a) shows that in the distance-based environment the conventional $\mathrm{A}^{*}$ algorithm has two options to choose its heuristic value: Manhattan distance and Euclidean distance. For (b) in the cost-based environment, the heuristic information may not be effective, as the risk cost distribution is uneven and unpredictable from the current node $\left(x_{i}, y_{i}\right)$ to the target node $\left(x_{\text {end }}, y_{\text {end }}\right)$. For (c), the global heuristic distance path is directly from the current node to the destination. While the local heuristic direction is generated by connecting the cluster centroids. The heuristic value is approximate to the exact lower bound by incorporating both the global and local heuristic information.

Swarm-based methods initiate with a number of solutions and are suitable to solve the above-proposed problem. Estimation of distribution algorithm (EDA) [59,60] is one of the typical swarm-based algorithms for solving both discrete and continuous optimization problems. EDA algorithm is a stochastic method, and it performs well in terms of global searching. That makes it a suitable method to optimize the searching region and estimate the lower bound of the heuristic value in cost-based environments. Besides, the EDA method also has no limitation for the number of variables in the optimization process. That aligns with the requirement for the optimization variable of this paper. As in this paper, the optimization variables of the cost-based path planning problem are coordinates of path points, and the number of the points may not be the same for different flight paths.

The core of EDA is to generate and sample explicit probabilistic models of the promising solutions to guide the search for the optimum. The optimization process can be seen as a series of incremental updates of the probabilistic model to achieve the global optimal solution. To reduce the complexity of the optimization process, authors [61] proposed a method by using a binary integer to avoid exploring irrelevant areas. Inspired by their works, this paper develops a hybrid algorithm called EDA-A*, which integrates EDA and A* algorithms. The outer loop of the EDA-A* algorithm is to solve a binary $0-1$ optimization problem, which aims for optimizing the feasible region for path searching. The optimized feasible region will be fed into the inner loop, where A* algorithm is used, to generate the cost-effective path. The workflow and pseudocode of the EDA-A* algorithm are presented in Fig. 7 and Algorithm 1.

The main loop of the EDA-A* algorithm is from Line 6 to Line 23 as shown in Algorithm 1. In this algorithm, the species include a number of populations. One population refers to a complete path searching region based on the selected environment. The EDA method is used to optimize the searching region by selecting the low-cost airspace units along with the reference path from origin to destination. The A* algorithm is used to produce the cost-effective path using the optimized searching region. The essential part of the EDA-A* algorithm is the probability update function (Line 22), which is used to balance the exploitation and exploration of the searching process. By selecting the dominant populations from the species, the function is updated towards that individuals belonging to the dominant populations will have increasing probabilities to be selected as optimal points.

As defined in Eq. (23), the probability array $\boldsymbol{p}_{i+1}$ of being selected for next candidate solutions consists of two parts. The first part is to exploit
![img-7.jpeg](img-7.jpeg)

Fig. 7. Framework of EDA-A* algorithm.
the current best solution by using the currently obtained probability array $\boldsymbol{p}_{i}$. The second part is to explore the searching space for better solutions. Each candidate solution point in the array $\boldsymbol{D}_{\mathrm{s}}$ is divided by the total number of dominant species $\mathrm{N}_{\mathrm{s}}$. The more times a candidate point is selected (based on fitness value), the higher probability it will have in $\boldsymbol{p}_{i+1}$, and eventually it has higher probability to be selected as a solution point. The balance of the exploitation and exploration is adjusted by the learning rate $l_{\text {rate }}$. Specifically, there will be no exploitation process if $l_{\text {rate }}=1$, as the current best probability has no contribution to the next status. In contrast, there will be no exploration process if $l_{\text {rate }}=0$, as the next status is completely contributed by the current best probability. The update function is denoted as
$\boldsymbol{p}_{i+1}=\left(1-l_{\text {rate }}\right) \boldsymbol{p}_{i}+l_{\text {rate }} \frac{\boldsymbol{D}_{s}}{\mathrm{~N}_{\mathrm{s}}}$
As EDA is a stochastic method based on a probabilistic model, during the iteration, path planning in some populations (feasible regions) might be

## Algorithm 1

Hybrid EDA-A* algorithm for cost-based path planning.

```
input: cost value of each airspace unit (Cost), origin and destination (OD) of
    UAV flight, obstacle information
    output: generated path (path), total cost of the path (TotalCost)
    path \(=\mathrm{null}\)
    TotalCost \(=0\)
    initialize the probability matrix \(p\) of EDA
    for \(i=1: n_{\text {ime }}\) Do\% outer loop, \(n_{\text {ime }}\) is the number of iterations
        while \(j<=n_{\text {opt }}\) Do\% \(n_{\text {opt }}\) is the number of populations in the species
            \(r=\) rand(size Cost \() \)
    each airspace unit
            species \((j, 1)=1 \cdot *(r(j, 1)-p,(j, 1)): \%\) select path searching space by
    comparing \(r\) and \(p\)
        \(j=j+1 ;\)
        end while
        save species\% selected path searching spaces
        for \(k=1: n_{\text {opt }}\) Do\% inner loop
            path \(=\mathrm{A}^{*}(\) OD, species, obstacle \() ; \%\) generate path using \(\mathrm{A}^{*}\) algorithm
            TotalCost \(=\) FitnessValue (path);
            T_cost \(=\) [T_cost;TotalCost];
        end for
        T_cost \((C, n p, 1=\) max(T_cost);\% eliminate populations that have no feasible
        path found
        FitnessValue \(=\) T_cost;
    [Fitness, index] = sort(FitnessValue);
    Do \((), 1\) = species (index(), 1);\% select dominant populations
        \(p_{i-1}=\left(1-\mathrm{I}_{\text {max }}\right)^{n} p_{i+1} \mathrm{I}_{\text {min }} * D s / N c \%\) probability update function: Eq. (23)
    end for
```

trapped by obstacles and may not be able to find a feasible path from origin to destination. The total cost $C_{\text {_np }}$ for these populations will be replaced by the maximum cost among the whole species (Line 18). In subsequent iterations, these populations will be eliminated, and the selected dominant population is guaranteed to find a feasible path.

### 4.3.2. An improvement of EDA-A* with fast computation: EDA-CostA*

In EDA-A* algorithm, the EDA is used to select the feasible region for path planning, and $\mathrm{A}^{*}$ is used to produce the path based on the selected region. With heuristic information, $\mathrm{A}^{*}$ algorithm conducts very fast compared with Dijkstra method. However, $\mathrm{A}^{*}$ algorithm is called for every population of the species at every iteration (a For loop from Line 13 to Line 17 in Algorithm 1). That makes the overall EDA-A* algorithm taking more computational time as the problem scale gets larger. To cope with this problem, we further improve the EDA-A* algorithm by introducing the $k$-means method to provide both global and local heuristic information for path searching (see Fig. 6(c)). The improved hybrid algorithm is named as EDA-CostA*, and its workflow is presented in Fig. 8.

The EDA-CostA* algorithm has three main functions. The first function is the EDA algorithm, which is used to globally optimize the feasible region that has low costs among all searching space. The second function is the $k$-means algorithm, which is used to cluster the low-cost regions and to identify the global heuristic distance and local heuristic direction. The identified heuristic information will be used to estimate the lower bound of the heuristic value that will be ingested into the third function $\left(\operatorname{CostA}^{*}\right)$ to generate the cost-effective path.

The global heuristic distance $h_{\text {Dist }}$ is improved from Euclidean distance to estimate the total cost from current node to the destination, which is presented as
$\left\{\begin{array}{l}h_{\text {Dist }}=h_{\text {heuDist }} \sqrt{\left(x_{D}-x_{i}\right)^{2}+\left(y_{D}-y_{i}\right)^{2}+\left(z_{D}-z_{i}\right)^{2}} \\ h_{\text {heuDist }}=\min \left\{\left(\frac{1}{N_{V_{\text {opm }}} \sum_{v, v_{o p m}} c_{v_{i}}}\right),\left(\frac{1}{N_{V_{\text {opm }}} \sum_{v, v_{o p m}} c_{v_{i}}}\right)\right\}\end{array}\right\}$
in which $\left(x_{D}, y_{i}, z_{i}\right)$ is the coordination of the current point and $\left(x_{D}, y_{D}\right.$. $\left.z_{D}\right)$ is the destination point, which are used to compute the Euclidean distance. Note that $h_{\text {heuDist }}$ is the heuristic distance factor, which takes
![img-8.jpeg](img-8.jpeg)

Fig. 8. Workflow of EDA-CostA* algorithm.
the minimum value among the mean cost of all open vertices $\mathrm{V}_{\text {open }}$ and the mean cost of cluster centroid vertices $\mathrm{V}_{\text {Cirs }}$. Taking the minimum value is because a smaller value is more likely to fall within the lower bound and that leads to a better quality of solution for CostA* algorithm [23]. When the heuristic value is down to zero, the CostA* will then be equivalent to the Dijkstra method. The determination of the heuristic value for the algorithm is to make a trade-off between the quality of solution and computational efficiency.

The local heuristic direction $h_{\text {Dcrit }}$ is defined as the distance from the current point $\left(x_{i}, y_{i}, z_{i}\right)$ to its nearest cluster centroid $\left(x_{\text {cen... } . .}, y_{\text {cen... } .}\right.$, $\left.z_{\text {cen... } .}\right)$ as illustrated in Fig. 6(c), which is denoted as
$h_{\text {Dcrit }}=\sqrt{\left(x_{\text {cen... } .},-x_{i}\right)^{2}+\left(y_{\text {cen... }},-y_{i}\right)^{2}+\left(z_{\text {cen... }},-z_{i}\right)^{2}}$
The detailed pseudocode of the EDA-CostA* algorithm is presented as Algorithm 2.

The identified heuristic information above will be ingested into the third function (CostA*) to generate the cost-effective path. In CostA* algorithm, the solution point is evaluated by the cost function $f(c)$, which is defined as the sum of costs from two parts, as denoted in Eq. (26). The first part is the integral of the cost from origin point to current point, presented as $g(c)$. The second part is the heuristic value $h(c)$, which is determined by both of the global heuristic information $h_{\text {Dist }}$ and local heuristic information $h_{\text {Dcrit }}$.

As Fig. 6(c) illustrates, the heuristic distance path provides the global heuristic information $h_{\text {Dist }}$, which is directly from the current node to the destination. While the heuristic direction path provides local heuristic information $h_{\text {Dcrit }}$, which connects the cluster centroids. To avoid the local path search deviating too far from the global path, the deviation between the local path and the global path is evaluated and constrained. The deviation is defined as the difference between $h_{\text {Dcrit }}$ and $h_{\text {Dist_cen }}$ over $h_{\text {Dist_cen }}$. Here $h_{\text {Dist_cen }}$ is the heuristic distance from the current point to the point that is projected from cluster centroid on the global track. If the deviation does not exceed the threshold $c$, which means the local cluster centroid is not far from the global track. The $h_{\text {Dcrit }}$ will be

## Algorithm 2

EDA-CostA* algorithm for fast cost-based path planning.

```
input: cost value of each airspace unit (Cost), origin and destination (OD) of
    UAV flight, obstacle information
    output: generated path (path), total cost of the path (TotalCost)
    path=null
    TotalCost=0;
    \(\mathrm{P}_{\text {final }}=\) EDA(Cost) \(; \%\\) obtain the best population \(\mathrm{P}_{\text {best }}\)
    if sum \(\left(P_{\text {total }}\left(\mathrm{i}, j, k\right)\right)=1\) Do\% obtain open points for path searching
        \(\mathrm{P}_{\text {indiv }}=\left[\mathrm{i}, j, k\right] ; \%\) get the position of individual open point
        \(\mathrm{P}_{\text {all }}=\left[\mathrm{P}_{\text {all }}\right] \cdot \mathrm{P}_{\text {indiv }}\|; \%\) obtain the positions of all open points
    end if
    \(\mathrm{P}_{\text {contrast }}=k\)-means(Posts);\% obtain the positions of cluster centroids
    \(\left(h_{\text {Dist }}, h_{\text {Decto }}\right)=f\left(F_{\text {contrast }}\right) \%\) obtain heuristic information by Eq. (24) and Eq.
    (25)
    (path, TotalCost) \(=\operatorname{CostA}^{*}(\) OD, obstacle, \(h_{\text {Dist }}, h_{\text {Decto }}\);
```

used as the heuristic information for the current point. In contrast, the $h_{\text {Dist }}$ will be used. Here the $\varepsilon$ is taken as 0.2 , which presents the deviation between global path and local path. The cost function is denoted as

$$
\begin{aligned}
& f(c)=g(c)+h(c)=\int_{c_{i}}^{\infty} c_{i} d v+h(c) \\
& \left\{\begin{array}{l}
h(c)=h_{\text {Distn. }} \text { if } \frac{\left(h_{\text {Distn. }}-h_{\text {Dist. } \text { con }}\right)}{h_{\text {Dist. con }}}<\varepsilon \\
h(c)=h_{\text {Dist. }} \text { if } \frac{\left(h_{\text {Distn }}-h_{\text {Dist. con }}\right)}{h_{\text {Dist. con }}} \geq \varepsilon
\end{array}\right.
\end{aligned}
$$

The pseudocode of the CostA* algorithm is presented as Algorithm 3.

To summarize, there are two similarities between the EDA-A* and EDA-CostA* algorithms. They use the same cost data as input, and they both employ EDA to generate the initial solution of feasible regions. The difference between the two algorithms is the computational efficiency. In EDA-A*, the A* algorithm is called for every single iteration to produce the path for all populations, which consumes significant computational time. While for EDA-CostA*, the CostA* is only called once to generate the cost-effective path based on the optimized feasible region by EDA, which significantly reduces the computational time.

## Algorithm 3

$\operatorname{CostA}^{*}$ algorithm.

```
input: cost value of each airspace unit (Cost), origin and destination (OD) of
    UAV flight, obstacle information
    output: generated path (path)
    for( \(=1: 26\) Do\% possible choices of next path point
        next \(=[x(i), y(i), z(i), \operatorname{Cost}(x(i), y(i), z(i)] ; \%\) coordinates of the next point
        and its cost value
        Motion=[Motion; next];
        end for
        MotionMode() \(=\) Motion; \(\%\\) store the cost value matrix for every open point
        \(g(c)=f(\operatorname{MotionMode}(c)) ; \%\) the integral of the cost from origin point to current
        point
    Obtained the global heuristic information \(h_{\text {Dist }}\) by Eq. (24) and local heuristic
        information \(h_{\text {Distn. }}\}\) by Eq. (25)
    if \(\left(h_{\text {Distn. }}-h_{\text {Dist. con }}\right) / h_{\text {Dist. con }}\left(\leq x\right.\) Do\% approximate heuristic value by Eq. (26)
        \(h(c)=h_{\text {Distn. }} \%\) deviation is acceptable, path searching direction follows local
        low-cost cluster
        else
        \(h(c)=h_{\text {Dist. }} \%\) deviation is unacceptable, path searching direction follows
        global track
    end if
    \(f(c)=g(c)+h(c) ; \%\) overall cost function
    if \(f(c)<\operatorname{open}(f(c))\) Do\% distance from current point to destination less than
        that of the points in open list
        Putting current point as father point, and it will be included in the path
    end if
```


## 5. Simulation results

To demonstrate the integrated cost assessment model and the developed cost-based path planning algorithms, we perform simulations and case studies in a representative metropolitan area. First, the cost assessment model is implemented in a real-world environment to generate the cost-based airspace map. Based on the map, the proposed algorithms are used to produce the cost-effective path. Simulations and statistical analysis are conducted to test how well the proposed cost assessment model and algorithms can be generalized to other urban patterns.

### 5.1. Case study of the integrated cost assessment model

A typical metropolitan area ( $6 \mathrm{~km} \times 6 \mathrm{~km}$ ) in Singapore is selected for the modeling of risk-based airspace, and the allowable altitude in this study is chosen as 120 m ( 400 feet) above the ground. The size of each air block is $100 \mathrm{~m} \times 100 \mathrm{~m} \times 30 \mathrm{~m}$. The selected metropolitan area has dense high-rise buildings, shopping centers, city squares, residential areas with dense populations, parks, etc., which are representative of modern megacities. A total number of 3366 buildings are included in the selected area. The selected environment has two administrative districts, and the average population densities are $8.358 \times 10^{3}$ and $7.219 \times 10^{3}$ (people $/ \mathrm{km}^{2}$ ) [62]. The average traffic density in the road of the given area is obtained as $7.12 \times 10^{3}$ (vehicle $/ \mathrm{km}^{2}$ ) [63]. Based on the average population and vehicle densities, we estimate the population density distribution using Eq. (11) and traffic density distribution using Eq. (12). Obtained population and traffic distribution results are illustrated in Fig. 9.

In this case study, the UAV is selected as one of the most commonly used drones (DJI Phantom 4). The weight of the drone is 1.38 kg and in urban environments the crash probability $P_{\text {crash }}$ is $3.42 \times 10^{-4}$ per flight hour [16]. The size of the UAV crash impact area is $S_{\text {_hit }}=0.0188 \mathrm{~m}^{2}$ and the drag coefficient is $R_{f}=0.3$ [7]. The number of casualties caused by average traffic accident is $R_{f}^{\prime}=0.27$ [64]. For the integrated cost model, the weight factors of fatality risk, property damage risk and noise impact are given as $\alpha_{1}=0.5, \alpha_{2}=0.25$, and $\alpha_{3}=0.25$, respectively. The fatality risk cost is given a high weightage of 0.5 , while the property damage cost and noise impact cost are given the same weight as 0.25 in this study. Based on the obtained data, the total integrated cost of each flight layer is computed and illustrated in Fig. 10.

In Fig. 10(a), the average cost of flight Layer 1 is the highest. The locations with high fatality risks are identified on the map. For instance, the location $(20,55)$ on the map has the highest risk cost, as there are shopping streets, highway intersections, and dense populations in realworld environments. Thus, the fatality risk and property damage risk in there are high, making the total cost high. In Layer 2 (Fig. 10(b)), with the increase of flight altitude, the costs are significantly reduced for property damage and noise impact, whereas the fatality risk cost increases by $7.7 \%$ compared with the one in Layer 1. In the third and fourth flight layers as shown in Fig. 10(c) and Fig. 10(d), the flight altitude increases to 90 and 120 m . The high-risk areas in these two layers are still clearly identified while the total cost has not changed much from Layer 3 to Layer 4 because of two reasons. For one thing, the fatality risk only slightly increases by $4.09 \%$ from Layer 2 to Layer 3 and $2.66 \%$ from Layer 3 to Layer 4 after the altitude over 60 m . That is because UAV impact over such height is mostly causing fatalities. For another, the influence of the noise impact exceeds the height threshold (Eq. (17) and Fig. 5(b)) and contributes nothing to the integrated cost, while the property damage cost is significantly small. The integrated costs in Layer 3 and Layer 4 are therefore significantly small while the high-cost areas are clearly identified.

![img-9.jpeg](img-9.jpeg)

Fig. 9. Distribution of population density and traffic density in the selected urban environment.
![img-10.jpeg](img-10.jpeg)

Fig. 10. Integrated risk cost mapping for different flight layers.

# 5.2. Cost-based flight path planning 

Based on the obtained cost-based map, we conduct the cost-based path planning with algorithm comparisons in terms of solution quality and computational time. The heuristic effectiveness of our proposed EDA-based method is also demonstrated by simulation results. Lastly, the influence of different risk types on the cost-based path planning results is investigated.

### 5.2.1. Cost-based path planning in a real-world environment

The flight paths optimized by our proposed hybrid algorithm can avoid obstacles and high-cost areas identified by our proposed cost
assessment model. The results of the 3D view with risk map, top view, and 3D view without risk map are presented in Fig. 11(a), Fig. 11(b), and Fig. 11(c). Observed from 3D view, the drone flight height for most of the time is 120 m , which is the top layer of the modelled environments. Flying at such height significantly reduced the property damage risk and noise impact cost, and the fatality cost can also be reduced by avoiding high population density and vehicle density areas such as locations (10, $12),(40,40)$ and $(42,39)$ shown in the top view Fig. 11(b). In a realworld environment, these identified high risk cost locations are shopping streets, hospitals, schools, or highway conjunctions, where the population density and vehicle density are significantly higher than the rest of the areas. Being able to quantitively identify high risk areas using
![img-11.jpeg](img-11.jpeg)

Fig. 11. Cost-based paths generated in a real-world environment.

our proposed model can facilitate the risk management of low-altitude urban airspace and cost-based path optimization. Which subsequently enables safe UAV operations in metropolitan environments.

In the simulations, five algorithms are used to generate the costbased flight path. They are Dijkstra, RiskA*, ACO, EDA-A* and EDACostA* algorithms. Dijkstra algorithm, as an exact method, is used to generate the optimal solutions as a basis for comparison. The other two main types of cost-based path planning algorithms are the heuristic A*based (RiskA*) method [27] and evolutionary ACO (Ant Colony Optimization: ACO)-based method [25,65]. In this study, the heuristic value of the RiskA* algorithm is taken as the average cost of all cells in the map. The same cost-based map is used for all five algorithms for path planning.

The path planning results of five algorithms are obtained and presented in Table 2. Compared with the Dijkstra algorithm, the flight path produced by EDA-CostA* has $2.06 \%$ shorter while it uses a mere $3.05 \%$ computational time, whereas the risk cost of the path is $4.58 \%$ greater than the Dijkstra one. For the path produced by ACO algorithm, it has $1.51 \%$ more risk cost and $1.22 \%$ longer distance. However, its computational time is significantly greater than all of the other algorithms, with $785.98 \%$ greater than Dijkstra method. For EDA-A* algorithm, its performance makes a good trade-off among the risk cost, flight distance, and computational time. As to RiskA* algorithm, it consumes only $0.16 \%$ of time and the path is $90.65 \%$ long compared with the path produced by Dijkstra. However, it has the highest cost index, with $28.8 \%$ higher than the basis generated by Dijkstra. As it fails to avoid some high-cost areas like locations $(11,12)$ and $(43,45)$ as shown in Fig. 11 (b). Furthermore, the heuristic value of RiskA* is also hard to obtain and it plays a key role in optimization performance, as analysis shown in Table 1 of reference [27]. Determination of a proper heuristic value for RiskA* is unsolved, especially when the environment changes. That is the key motivation for our proposed hybrid EDA-A* and EDA-CostA* algorithms to solve the cost-based path planning problems in various environments. Simulations and analyses are conducted next to demonstrate the performance of our proposed algorithms.

### 5.2.2. Heuristic effectiveness of using EDA to estimate the lower bound

As we discussed in Section 4.3, it is difficult to obtain the exact heuristic lower bound in a cost-based environment, as the cost values are distributed unevenly and unpredictably. That motivates this paper to propose an EDA-based method to better estimate the exact lower bound of heuristic value. As EDA is a stochastic method, the estimated heuristic value may not be a global optimal but suboptimal. We conduct simulations to demonstrate the performance of our proposed EDA-based method in estimating the exact lower bound. The exact lower bound is defined as the exact cost from the current point to the destination, which is the baseline in this study. The baseline value for each path point is obtained by the cost-based Dijkstra method. The estimated lower bound is defined as the approximate cost from the current point to the destination, which is computed by our proposed EDA-based method.

In the simulation, the environment is as same as the one used in Section 5.2.1. A path is generated, and it has 73 path points. Both the exact heuristic value and the estimated heuristic value of each path point are obtained and presented in Fig. 12(a). The absolute error and the relative error between the estimated values and the exact values are also computed, shown in Fig. 12(b).

The results in Fig. 12(a) show that the estimated heuristic value is
approximate to the exact heuristic value, while the estimated values are higher than the exact values except for the values in point 63 and point 71. That enables the high computational efficiency for EDA-CostA* in the path searching process, whereas it may sacrifice the optimality of results as discussed in Table 2. The absolute error between the estimated value and exact value shows a decreasing trend (Fig. 12(b)), from 93.92 in origin point to zero in the destination. The relative error shows a stable trend with around $5 \%$ error in the first half of the points. The trend intensifies as the points approach the destination. That is because the exact heuristic value (denominator in the computation of relative error) becomes smaller when approaching the destination. A small change of the difference (numerator in the computation of relative error) between the estimated value and the exact value will lead to a significant relative error. Overall, the obtained results demonstrate the high heuristic effectiveness of proposed EDA-based methods compared with the baseline, with an average estimation error of $5.65 \%$.

### 5.2.3. Influence of different risk cost types on cost-based path planning

To demonstrate the influence of different risk cost types on safe UAV operations, we conduct four groups of path planning simulations: (1) Path1: without considering any risk cost; (2) Path2: only consider fatality risk cost; (3) Path3: consider fatality risk cost and property damage risk cost; (4) Path4: consider all three costs. The environment of the four simulations is the same, which is generated in Section 5.1. As the EDACostA* algorithm performs well among the other methods in terms of computational efficiency and effectiveness, it is applied for each of the four simulations to generate the flight path. Obtained results are shown in Fig. 13 and Table 3.

Path1 goes from the origin $(1,1,1)$ to the destination $(60,60,4)$ with almost a straight line. This path avoids obstacles in locations like (30, 32) and $(40,40)$ shown in Fig. 13. However, it does not avoid high-cost areas where population density and vehicle density are high, resulting in the total cost of Path1 being the highest among all paths, with a risk cost index of 1698.25 (see Table 3). Whereas the distance of the path is the shortest as it goes almost straightly to the destination. For Path2 the fatality risk is taken into account. This path successfully avoids the high population density areas (10, 12), (40, 45), (42, 15) shown in Fig. 9(a) and high vehicle density areas $(8,20),(45,10)$, and $(55,40)$ shown in Fig. 9(b). As the fatality risk cost has a high proportion in the integrated cost model, avoiding that makes a significant reduction ( $23.68 \%$ ) of cost for Path2, compared with Path1. For Path3 the fatality risk and property damage risk are both considered. The produced path3 not only avoids the high fatality risk areas but avoids dense high-rise building areas like $(20,20)$ and $(30,30)$ shown in Fig. 4(a), which Path1 and Path2 fail to do so. By adding property damage risk into the model, Path3 can avoid dense building areas, thus the cost of its path further drops by $5.94 \%$ compared with Path2. For Path4, it considers all three cost types, the integrated cost of Path4 has a further reduction of $2.48 \%$ compared with Path3.

Overall, the fatality risk cost is the primary factor in the integrated cost assessment model, followed by property damage risk cost and noise impact cost. With more risk types getting considered, a more accurate cost-based map will be generated to produce a lower-cost path for safe UAV operations. While the distance of the produced path will be longer as the UAV may need to travel a longer distance to avoid obstacles and high-risk areas. Analysis of the trade-off between the integrated cost and flight distance is performed in the following subsection.

Table 2
Comparison results of the four cost-based path planning algorithms.

![img-12.jpeg](img-12.jpeg)

Fig. 12. Heuristic effectiveness of our proposed EDA-based methods.
![img-13.jpeg](img-13.jpeg)

Fig. 13. Top view of the generated paths considering different risk cost types.

### 5.3. External validity of the integrated cost assessment model

Above, the integrated cost assessment model is used in a specific urban pattern, which is a downtown area selected in Singapore. To demonstrate how well the proposed model can be generalized to other urban patterns, we conduct external validities in this section. Here, external validity refers to how well the outcome of a study can be expected to apply to other settings. In our case, two groups of urban environments are generated for the validity. One group has the same size environments, and the other has different size environments. The detailed parameter settings of the environments are given in the following subsections.

### 5.3.1. External validity in environments with the same size

The environmental parameters are randomly generated in the simulations to eliminate the selection bias. Population density is taken from the range of $[5,25] \times 10^{3}\left(\right.$ people $/ \mathrm{km}^{2}$ ), which covers the most densely populated cities worldwide [66]. The average traffic density is given as same as above in Section 5.1. The building height distribution of all generated patterns follows a log-normal distribution. The size of the environment is $6 \mathrm{~km} \times 6 \mathrm{~km} \times 120 \mathrm{~m}$ (Length, Width, Height). The integrated cost assessment model is used to compute the cost value of each airspace unit in 100 independent simulation environments, and the distance-based Dijkstra and cost-based Dijkstra are used to generate the flight path. The distance-based Dijkstra algorithm is performed in a distance-based map without considering the integrated cost (Eq. (20)). While the cost-based Dijkstra is conducted in the cost-based map to minimize the integrated cost. Comparison is made between these two algorithms to see how much percentage of integrated cost can be reduced by using the cost-based algorithm. The simulation starts from the origin $(1,1,1)$ to the destination $(60,60,4)$ in the generated environments.

In the 100 sample environments, the total cost is significantly reduced by using cost-based Dijkstra. While the flight distance shows an opposite trend. The flight distance of the paths produced by cost-based Dijkstra is greater than that of the distance-based Dijkstra algorithm. To further present the quantitative relationship of the cost and distance, we computed the differences of total cost and total flight distance generated by the above two algorithms for all 100 simulations. The differences are defined as the results obtained by cost-based Dijkstra compared with the results obtained by distance-based Dijkstra. The differences of total cost and flight distance are presented in Fig. 14.

To test the reliability of the model for the population (all urban patterns), we conduct statistical analysis to find a $95 \%$ confidence interval for the cost reduction and flight distance increase. In this case, we have two sets for testing. One is the integrated cost and the other is the flight distance. Each of the testings has two sample groups, and they are the integrated cost of path produced by cost-based Dijkstra (Group 1) and by distance-based Dijkstra (Group 2). Each group has 100 samples. As the sample sizes are large $\left(n_{1}>30\right.$ and $\left.n_{2}>30\right)$, we use normal distribution to compute the confidence interval. The sample means $\left(\bar{x}_{1}\right.$ and $\left.\bar{x}_{2}\right)$ and sample variances $\left(x_{1}^{2}\right.$ and $\left.x_{2}^{2}\right)$ of the two groups are computed

Table 3
Results of the four paths considering different risk cost types.
![img-14.jpeg](img-14.jpeg)

Fig. 14. Differences of total cost and total flight distance for the generated path in same size environments ( $6 \mathrm{~km} \times 6 \mathrm{~km} \times 120 \mathrm{~m}$ ). The baseline is the cost and distance of the path produced by the distance-based Dijkstra algorithm. The percentage differences of total cost and total flight distance can be obtained by $\left(C_{\text {cost }, \text { Dijkstra }}-C_{\text {distance }, \text { Dijkstra }}\right) / C_{\text {distance }, \text { Dijkstra }}$ and $\left(D_{\text {cost }}, \text { Dijkstra }-D_{\text {distance }, \text { Dijkstra }}\right) / D_{\text {distance }, \text { Dijkstra }}$, respectively.
and presented in Table 4. The population means of Group 1 and Group 2 are presented as $\mu_{1}$ and $\mu_{2}$. The confidence interval of cost reduction effect can be then described as $\left(\mu_{2}-\mu_{1}\right) / \bar{x}_{2}$, where the interval of $\mu_{2}-\mu_{1}$ can be computed by $\left(\bar{x}_{2}-\bar{x}_{1}\right) \pm Z_{\alpha / 2} \sqrt{s_{1}^{2} / n_{1}+s_{2}^{2} / n_{2}}$. The obtained result shows that a $95 \%$ confidence interval for cost reduction is $\left(\mu_{2}-\right.$ $\left.\mu_{1}\right) / \bar{x}_{2} \in[0.4264,0.4415]$. Which means that our proposed integrated cost assessment model is effective for various types of urban patterns, and the average total cost is reduced by [42.64\%, 44.15\%] at $95 \%$ confidence level. Similarly, we obtained the testing results for flight distance. The average flight distance increases by [17.36\%, 19.23\%] at $95 \%$ confidence level by using the cost-based Dijkstra algorithm. That is because UAV needs to travel longer distance to avoid high-cost areas.

### 5.3.2. External validity in environments with different sizes

Simulations are conducted to further test the reliability of the proposed cost assessment model in environments of different sizes. The simulations include 30 randomly generated environments with the size of $1 \mathrm{~km} \times 1 \mathrm{~km}, 2 \mathrm{~km} \times 2 \mathrm{~km}, \ldots, 30 \mathrm{~km} \times 30 \mathrm{~km}$. The height of the environment is 120 m with four flight layers. The integrated cost assessment model is used to produce the cost-based map, and the costbased Dijkstra and distance-based Dijkstra algorithms are used to generate the path. The total cost and total distance of the generated path are obtained for both algorithms. The differences of the total cost and total distance by using cost-based Dijkstra, compared with distancebased Dijkstra, are presented in Fig. 15.

By using the proposed cost-based path planning method, the average total cost for the 30 environments is reduced by $42.35 \%$, with a variance of $1.54 \%$. Whereas the flight distance increases by $12.03 \%$, with a variance of $0.15 \%$. The results demonstrate that the integrated cost assessment model and cost-based path planning methods are also effective in environments of different sizes. Compared with the results obtained in the same-size ( $6 \mathrm{~km} \times 6 \mathrm{~km}$ ) environment, the average total cost increases by $[0.29 \%, 1.80 \%]$ while the average total flight distance reduces by $[5.33 \%, 7.23 \%]$ in 30 different size environments. With the increase of environment size, the difference of total cost has no significant change while the difference of total flight distance slightly decreases. The difference of total cost has no significant change is because
the flight path without considering cost will always go through the highcost areas that the cost-based path will always avoid (as shown in Section 5.2.2). The increase of environment size only changes the value of total cost but not the percentage of the difference. For the total flight distance, the search space becomes larger for a flight path with the increase of environment size, which provides more alternatives for the path to avoid high-cost areas. The path can choose the shortest one among the alternatives, which therefore reduces the flight distance.

### 5.4. Reliability analysis of the proposed algorithms

Above we demonstrated that the proposed integrated cost assessment model is effective to generate the cost-based map in various types of urban patterns. With that map, the cost-based algorithm can produce a cost-effective flight path. To test the reliability of proposed cost-based algorithms in different urban environments, we perform the simulations based on the urban environments with same size used in Section 5.3. The cost-based Dijkstra algorithm is used to generate the optimal solution as a basis for comparisons with EDA-A* and EDA-CostA* algorithms. Three indicators of the total cost, total flight distance, and computational time are obtained and presented in Fig. 16 and Table 5.

In the overall 100 simulations, the cost-based Dijkstra algorithm performs the best in terms of the total cost reduction, followed by EDAA* and EDA-CostA* with an average performance rate of $102.76 \%$ and $105.47 \%$, respectively. It means that the average total cost of the path produced by EDA-A* and EDA-CostA* algorithms are $2.76 \%$ and $5.47 \%$ greater than that of the Dijkstra method. On the other hand, the EDACostA* algorithm provides the best performance in terms of average total distance and average computational time, with 0.4\% shorter in total distance and a mere $2.07 \%$ in computational time. Followed by EDA-A* algorithm, it saves $0.17 \%$ travel distance while spending $24.12 \%$ computational time compared with the Dijkstra method. Analysis results show that the proposed EDA-A* and EDA-CostA* algorithms have good robustness, with a mere $1.29 \%$ and $2.54 \%$ standard deviations in total cost, while $2.18 \%$ and $4.29 \%$ for total distance (see Table 5).

In summary, the EDA-CostA* is the fastest algorithm in terms of

Table 4
Statistical analysis for cost reduction and flight distance increase.

![img-15.jpeg](img-15.jpeg)

Fig. 15. Differences of total cost and total flight distance of the generated path in different sizes of environments. The baseline is the cost and distance of the path produced by the distance-based Dijkstra algorithm. The percentage differences can be computed as shown in the caption of Fig. 14.
![img-16.jpeg](img-16.jpeg)

Fig. 16. Reliability analysis results of the proposed cost-based path planning algorithms.

Table 5
Reliability analysis results of the proposed algorithms with 100 independent simulations.

computation and it is much faster than the other two algorithms. While it also has a good performance in the quality of solutions. Its performance is made possible by the heuristic information scheme and the algorithm's structure (see Algorithm 3) without the need to call the A* algorithm in every loop. The EDA-CostA ${ }^{\mathrm{e}}$ algorithm can be used for large-scale and time-sensitive cost-based path planning applications. The EDA-A ${ }^{\mathrm{e}}$ algorithm performs well in both solution quality and computational efficiency, and it can be applied to the trade-off case.

Cost-based Dijkstra can be employed to produce the minimum cost path if computational time is not sensitive.

## 6. Conclusions

Risk mitigation for UAV operation is a key enabler for the opening up of airspace to entice investment and promote innovations in this field. By conducting risk cost based path planning, the UAV operational risks

and impacts on populations in urban areas can be significantly reduced before flight. In this paper, the UAV flight path optimization problem has been studied with consideration of an integrated cost assessment model that incorporates fatality risk, property damage risk, and noise impact for safe UAV operations in metropolitan environments.
(1) The developed UAV flight path optimization method is effective and reliable in minimizing the risk cost of the flight path. The method has been both applied to a downtown area in Singapore and to 100 sample environments to optimize flight paths. The total integrated costs of the optimized paths have an average reduction by [42.64\%, 44.15\%] at $95 \%$ confidence level, compared with the costs of the paths produced by the distancebased Dijkstra algorithm. Whereas the average flight distance of the path increased by [17.36\%, 19.23\%]. That indicates a tradeoff exists between the risk cost and flight distance. Because UAVs may need to travel a longer distance to avoid not only obstacles but high risk cost areas [34].
(2) The proposed integrated cost assessment model can capture comprehensive risk types in urban environments including fatality risk, property damage risk, and noise impact. Instead of taking the average population density into the fatality risk cost model, this paper introduced a gravity model to estimate population density distribution in a finer scale. Which enables the opening of more airspace, as only the high population density areas will be identified.
(3) The extension of third-party risk in societal indicators (property damage risk and noise impact) is conducive for UAV flight path optimization in cost-based environments. The flight path will tend to fly at a lower altitude if only considers fatality risk, as the fatality risk is smaller in lower flight altitude due to the kinetic energy being lower. However, UAVs flying at lower altitude encounters more risks of property damage, operational efficiency loss, and noise impact. Because in lower altitude airspace the buildings are denser, which increases the collision probability of UAV with buildings. That also limits the flight speed and increases the intensity of flight maneuvers, resulting in loss of operational efficiency [51]. Noise impact also matters, and it can be solved by flying at a higher altitude.
(4) The developed cost-based path planning algorithm provides a novel scheme to determine the heuristic information for path searching methods in cost-based environments. The simulation results show the effectiveness and reliability of the developed algorithm in solving cost-based path optimization problems. The proposed hybrid EDA-CostA ${ }^{\circledR}$ algorithm performs best in computational time consuming only $2.07 \%$ of the time compared with the Dijkstra method, while it can reach an average of $94 \%$ optimality of solution quality.

The scope of this paper is in low altitude urban environments, and the integrated cost assessment model does not consider the risk cost of collision of UAV with general aviation and commercial aircraft. The risk assessment models for air traffic conflict and collision [11] for a mixed type of aircraft require further developments. As a key parameter in the fatality risk assessment model, the population density is better estimated using the gravity model with the data of shopping street and central business district (CBD) locations. Follow-up work can be on a more accurate estimation model for population density with multisource data [50]. What is more, the total flight duration of a path also matters, as the longer flight duration of UAV over people or vehicles, the higher risk cost (fatality, property damage, and noise impact) will be. For a given flight path, a faster flight speed yields a shorter flight duration. However, as the scope of this paper is on 3D flight path optimization, the flight speed and flight time are not considered. It could be follow-up research on cost-based motion planning or 4D flight path optimization. Where the flight duration should be considered, and the cost of a
path will also be correlated with flight speed. Another valuable research aspect is to incorporate the dynamic risk cost assessment into the real-time cost-based path planning. This enables us to tackle dynamically changing objects in the cost-assessment model, which will be critical for the real-life implementation of UAV operations in metropolitan areas.

## Author statement

Bizhao Pang: Conceptualization; Ideas; Writing, Methodology; Resource;Softwareprogramming&development;Validation
Xinting Hu: Investigation; Software programming; Resources
Wei Dai: Investigation; Resources
Kin Huat Low:Framework conceptualization; Ideas;Supervision; Resource; Editing; Validation;Review

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This research is supported by the National Research Foundation, Singapore, and the Civil Aviation Authority of Singapore, under the Aviation Transformation Programme on "Integration of Unmanned Aircraft Systems (UAS) into the Airspace." Any opinions, findings and conclusions or recommendations expressed in this material are those of the authors and do not reflect the views of National Research Foundation, Singapore and the Civil Aviation Authority of Singapore. Research Student Scholarship (RSS) provided by the NTU to the first author is acknowledged. The authors would like to thank Dr. Yu Wu and Dr. C.H. John Wang for their suggestions on the risk modeling and algorithm design. The collaborative efforts, on the risk modelling and assessment in urban-like enviroments, with both teams supported separately by the NTU's ATMRI UAS Programme and the Ministry of Education (MOE, Singapore) Tier-1 project research grant (Project ID: 2018-T1-002-124) are appreciated. The authors also wish to express their gratitude to the anonymous reviewers for their valuable suggestions and comments, which have significantly improved the quality of the final version of this article.
