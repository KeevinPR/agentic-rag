# Delineation of site-specific management zones using estimation of distribution algorithms 

Jonas Velasco ${ }^{\mathrm{a}}$, Salvador Vicencio ${ }^{\mathrm{b}}$, Jose A. Lozano ${ }^{\mathrm{c}}$ and Nestor M. Cid-Garcia ${ }^{\mathrm{d}, \mathrm{e}}$<br>${ }^{a}$ CONACYT-Centro de Investigación en Matemáticas (CIMAT), A.C., Fray Bartolomé de las Casas 314, Barrio de la Purísima, Aguascalientes 20259, Mexico<br>${ }^{\mathrm{b}}$ Centro de Investigación en Matemáticas (CIMAT), A.C., Fray Bartolomé de las Casas 314, Barrio de la Purísima, Aguascalientes 20259, Mexico<br>${ }^{c}$ Basque Center for Applied Mathematics (BCAM), University of the Basque Country UPV/EHU, Paseo Manuel<br>Lardizabal 1, Donostia-San Sebastián 20018, Spain<br>${ }^{d}$ Laboratorio Nacional de Gesichtelígencia, CONACYT-Centro de Investigación en Ciencias de Información Geoespacial, Circuito Tecnopolo Norte 107, Tecnopolo Pocitos II, Aguascalientes 20313, Mexico<br>E-mail: jvelasco@cimat.mx [Velasco]; salvador.vicencio@cimat.mx [Vicencio]; ja.lozano@ehu.es [Lozano]; ncid@centrogeo.edu.mx [Cid-Garcia]

Received 5 May 2020; received in revised form 18 December 2020; accepted 5 March 2021


#### Abstract

In this paper, we present a novel methodology to solve the problem of delineating homogeneous site-specific management zones (SSMZ) in agricultural fields. This problem consists of dividing the field into small regions for which a specific rate of inputs is required. The objective is to minimize the number of management zones, which must be homogeneous according to a specific soil property: physical or chemical. Furthermore, as opposed to oval zones, SSMZ with rectangular shapes are preferable since they are more practical for agricultural technologies. The methodology we propose is based on evolutionary computation, specifically on a class of the estimation of distribution algorithms (EDAs). One of the strongest contributions of this study is the representation used to model the management zones, which generates zones with orthogonal shapes, for example, L or T shapes, and minimizes the number of zones required to delineate the field. The experimental results show that our method is efficient to solve real field and randomly generated instances. The average improvement of our method consists in reducing the number of management zones in the agricultural fields concerning other operations research methods presented in the literature. The improvement depends on the size of the field and the level of homogeneity established for the resulting management zones.


Keywords: site-specific management zones; estimation of distribution algorithms; orthogonal shapes; evolutionary computation; combinatorial optimization

[^0]
[^0]:    *Corresponding author.
    (C) 2021 The Authors

    International Transactions in Operational Research (C) 2021 International Federation of Operational Research Societies Published by John Wiley \& Sons Ltd, 9600 Garsington Road, Oxford OX4 2DQ, UK and 350 Main St, Malden, MA02148, USA.

# 1. Introduction 

The problem of delineating site-specific management zones (SSMZ) in agricultural fields consists of generating subregions within a plot for which a specific rate of inputs is appropriate (Doerge, 1999; Moral et al., 2010). According to Plant (2001), Roudier et al. (2008), and Zhang et al. (2016), rectangular management zones are more practical for farmers by reducing the difficulties of adopting variable technologies and facilitating the use of agriculture machinery. Furthermore, the management zones with rectangular shapes are more applicable for farming in underdeveloped areas because farmers can easily apply these management zones to reduce fertilizer input, labor costs, and environmental waste without using advanced agriculture machinery.

The management zones must be homogeneous according to a specific soil property, physical or chemical, such as organic matter (OM), nitrogen (N), phosphorus (P), potential of hydrogen ( pH ), potassium ( K ), sodium ( Na ), and the sum of bases ( SB ), which is a mix of several properties. The delineation of management zones is a critical decision problem in agriculture since the soil characteristics have a strong impact on the crop yield. The chemical properties determine the application of inputs, for example, fertilizers and pesticides, while the water for irrigation depends on the physical properties.

The integration of some information technologies, called precision agriculture (PA), such as the global positioning systems, geographical information systems, and remote sensors, helps to improve crop productivity and makes farm management better. The idea of the PA is to face the variability of the soil properties and doing the right management practice at the right place and at the right time (Bongiovanni and Lowenberg-Deboer, 2004; Mulla, 2013; Janrao and Palivela, 2015). However, in some countries, farmers' attitudes and perceptions suggest that they are resistant to adopting unfamiliar technologies to improve agricultural management practices (Anastasiadis and Chukova, 2019; Watoo and Mugera, 2019).

In this context, the generation of SSMZ arises from the need of PA to deal with several factors, which are variable in space and time, that affect productivity and crop quality. Some of these factors, such as the heterogeneity of the physical and chemical soil properties, directly affect the water balance, the dynamics of nutrients, and the response to the application of inputs (Ortega and Santibáñez, 2007). The SSMZ helps to minimize the impact of spatial variability, allowing the sitespecific application of inputs and making more effective the agricultural planning (Betzek et al., 2018; Castrignanó et al., 2018).

An advantage of the SSMZ is the correct application of inputs in each region of the plot only where and when they are necessary according to the real requirements of the crop, its phenological stage, and the soil properties of the field, which allows a reduction of the environmental impact and a saving of resources and investment capital. These critical parameters and the crop prices must be considered to improve the decision-making process in agricultural fields (González et al., 2020; López et al., 2023). This contrasts with the conventional management agricultural practices, where the uniform applications of inputs are made throughout the whole production cycle considering, just in some cases, the phenological stage of the crop, which increases the production costs and the unnecessary waste of resources, especially water (Mulla, 2013; Janrao and Palivela, 2015). As in other water supply systems, the decision about the amount of water to be irrigated in each irrigation period directly impacts the total costs of farmers (Santos et al., 2022). The benefits of the SSMZ in vineyards and some crops have been demonstrated in Ortega and Santibáñez (2007).

![img-0.jpeg](img-0.jpeg)

Fig. 1. Delineation of SSMZ for an agricultural field close to Santiago, Chile, using organic matter as chemical soil property. (a) The thematic map for the field before the delineation, (b) the delineation using an operations research technique, and (c) the delineation using clustering methods.

Delineating efficiently SSMZ is a big challenge for farmers and decision makers. The most typical methodology used to solve the problem is the clustering method, which uses soil samples in conjunction with procedures such as fuzzy k-means, fuzzy c-means, and k-means (Betzek et al., 2018; Monzon et al., 2018; Oldoni et al., 2019; Ohana-Levi et al., 2019). The information for these algorithms is obtained from different methods such as analysis of topographic maps, statistical information, remote sensing data, or semivariogram analysis (Hornung et al., 2006; Li et al., 2007; Molin and de Castro, 2008; Fu et al., 2010; Tagarakis et al., 2013; Haghverdi et al., 2015; Gili et al., 2017; Albornoz et al., 2018; Georgi et al., 2018; Gaviola et al., 2019; Ortuani et al., 2019). Although these methods obtain homogeneous management zones, in some cases, the solution can be harder to apply due to the structure of the generated regions, which are disjoint or with circular or irregular shapes.

Concerning operations research methods, the work of Cid-Garcia et al. (2013) presents one of the first mono-objective mathematical formulations of integer linear programming (MILP) to delineate rectangular and homogeneous management zones minimizing the total variance of the field for a specific soil property, physical or chemical. The complexity of this mathematical formulation is demonstrated using a reduction to the 2D-bin packing problem, which is NP-hard (Chung et al., 1982). Therefore, the computational time required to solve the problem can increase exponentially with the size of the instance.

In Albornoz et al. (2015), the previous work was improved, showing a biobjective mathematical formulation of integer linear programming (BILP), where (a) the number of management zones is minimized and (b) the homogeneity level within these zones is maximized. Some decomposition approaches to approximate a solution for the SSMZ problem are developed in Albornoz and Ñanco (2016) and Albornoz et al. (2019). In Saez and Albornoz (2016), the authors propose an approach to delineate SSMZ under uncertainty conditions. Other works that integrate the delineation of rectangular management zones and the crop planning problems are presented in Cid-Garcia and Ibarra-Rojas (2019), Albornoz et al. (2020), and Albornoz and Zamora (2020).

The operations research methods mentioned above are based on the work of Cid-Garcia et al. (2013) and only consider regions with rectangular or square shapes to generate SSMZ, avoiding zones with orthogonal shapes, for example, T or L shape, which can be used for partitioning the field. Figure 1 shows the delineation for an agricultural field using the OM as chemical soil property with 40 soil samples and around of 7.82 ha ( 256 m width and 305.6 m long) presented in the work of Cid-Garcia et al. (2013). Figure 1a is the thematic map obtained with specialized software such

as MapInfo, before the delineation, showing the variability of the field and the number of soil samples (black points). Green zones represent the ideal level of OM; red or blue zones denote upper or lower levels, respectively. Figure 1 b is the resulting delineation for the exact method proposed by Albornoz et al. (2015), and Fig. 1c is the resulting delineation using a clustering method with specialized software (MapInfo), which can be harder to adopt by farmers considering the resulting zones (disjoint and with irregular shapes).

The objective of this paper is to present a new methodology based on soil samples and an evolutionary algorithm, specifically on an estimation of distribution algorithm (EDA), to delineate agricultural fields, minimizing the number of management zones and satisfying a specific level of homogeneity for each zone (the details for the EDA are given in Section 2.2). We consider the computational complexity of the SSMZ problem and the possibility of obtaining management zones with orthogonal shapes, which can be harder to generate in the exact approaches mentioned above. Also, our algorithm generates the zones during its execution, instead of using a preprocessing stage to generate predefined management zones such as some previous approaches. Furthermore, the improvement of our method consists in reducing the number of management zones in the agricultural fields with respect to the operations research methods. This improvement depends on the size of the field (the number of soil samples) and the level of homogeneity established for the resulting management zones.

The selection of an EDA approach is due to their applicability to solve other complex combinatorial optimization problems, which include multiobjective knapsack, routing, scheduling, forest management, portfolio management, environmental monitoring network design, and bioinformatics (Larrañaga and Lozano, 2002; Armañanzas et al., 2008; Hauschild and Pelikan, 2011; Ceberio et al., 2013; Wang et al., 2015). With the EDA, we generate zones with an orthogonal shape that can be used in the delineation of management zones on the field. To the best of our knowledge, this is one of the first approaches with these characteristics.

The rest of this paper is organized as follows. Section 2 presents the materials and methods to solve the SSMZ problem. Section 3 shows the experimental results for our EDA, and compares them with some exact approaches of the literature to validate its efficiency. Finally, Section 4 gives some conclusions and recommendations.

# 2. Materials and methods 

In Fig. 2, we present an overview of the methodology used to solve the SSMZ problem. It is composed of two main steps: (a) collecting soil samples in the agricultural fields (see Section 2.1) and (b) designing and implementing a solution method based on an EDA algorithm (we call EDA-SSMZ) to obtain high-quality solutions in acceptable computational times (see Section 2.2).

### 2.1. Soil samples

The first step in the SSMZ problem consists of collecting soil samples from the agricultural field, which are represented by a grid where each soil sample is equidistant from each other. The sampling is made to obtain information about the soil according to a specific soil property, chemical or physical. The chemical properties are used to determine the seeds, fertilizers, and pesticides to

![img-3.jpeg](img-3.jpeg)

Fig. 2. Summary of our methodology.
(a)
![img-3.jpeg](img-3.jpeg)
(b)
![img-3.jpeg](img-3.jpeg)

Fig. 3. Generation of a grid for an agricultural field considering the organic matter (OM) as chemical soil property. (a) The thematic map for the field and (b) the resulting grid. The pink circles represent dummy samples.
supply to the crop. The physical properties impact the amount of water needed in the irrigation process. The number of soil samples for each field depends on the farmer's investment ${ }^{1}$ and not necessarily on the field size, that is, a plot with 10 ha can take the same number of soil samples as one with 30 ha. A way to visualize the soil variability of these properties is by generating thematic maps with specialized software, as in Fig. 3a, where it is possible to create a grid inside of the field

[^0]
[^0]:    ${ }^{1}$ In Mexico, the costs per soil sample are around $\$ 50$ (INIFAP), which determines the number of samples in the fields of the farmer.

with the resulting soil samples (see Fig. 3b). In this sense, each soil sample represents the center of each square in the grid.

When the fields are no initially with a rectangular or square shape, that is, when the soil sampling does not generate a perfect grid, then the methodology adds dummy soil samples to complete the grid and enforces each soil sample as the center of each square. A perfect grid facilitates and improves the performance of the EDA-SSMZ algorithm. The number of dummy samples depends on the original soil sampling and the shape of the field. The EDA-SSMZ algorithm uses the variability in the soil samples to delineate the management zones considering a specific chemical or physical property. Therefore, to avoid using dummy soil samples as a new management zone in the final delineation, the value for each one is established by the decision maker considering the same concentration as a specific neighbor (a spatial correlation among the soil samples can be considered). The procedures of the EDA-SSMZ ensure that a management zone cannot group only dummy soil samples. With this, the use of dummy samples is not a disadvantage for the method. Figure 3b shows two dummy soil samples (pink circles) in the agricultural field (more details can be found in Cid-Garcia et al., 2013).

The relative variance (RV) constitutes an excellent criterion to prove the efficiency of a zoning method (Ortega and Santibáñez, 2007). Suppose that a set $M$ of management zones in the field, then the $R V$ is defined as

$$
\mathrm{RV}(M)=1-\frac{\sum_{m \in M}\left(n_{m}-1\right) \sigma_{m}^{2}}{\sigma_{T}^{2}[N-|M|]}
$$

where $\sigma_{T}^{2}$ is the total variance of the field, $N$ is the total number of soil samples, $|M|$ is the number of management zones used to delineate the field, $n_{m}$ the number of soil samples in zone $m$, and $\sigma_{m}^{2}$ is the variance within the management zone $m$. In this sense, $\sigma_{T}^{2}$ and $\sigma_{m}^{2}$ are calculated considering the formula of sample variance. According to the experts, to guarantee a homogeneous behavior of the zoning method, the RV must be greater than or equal to 0.5 (an alpha parameter ( $\alpha$ )). The highest values for $\alpha$ mean the highest levels of homogeneity in the management zones. Note that the range of values for $\alpha$ is $[0,1]$ :

$$
1-\frac{\sum_{m \in M}\left(n_{m}-1\right) \sigma_{m}^{2}}{\sigma_{T}^{2}[N-|M|]} \geq \alpha
$$

# 2.2. Estimation of distribution algorithms 

An EDA is a class of population-based optimization algorithm that extracts statistical information from the population of solutions, to generate new ones. The algorithm starts by generating a population of candidate solutions. These solutions are evaluated using an objective function. Based on this evaluation, a subset of solutions is selected using a selection method, and the population of the selected individuals is used to estimate a probability distribution. Finally, a new set of solutions is sampled from the estimated distribution, generating a new population of solutions, and the algorithm iterates again. The procedure ends when a stopping criterion, previously established, is reached. In our algorithm, the best solution represents the solution with the minimum number

of management zones that satisfy the homogeneity level $(\alpha)$ established by the decision maker, and the stopping criterion is fixed with a maximum number of iterations. For further reference about EDAs, the reader can consult (Larrañaga and Lozano, 2002).

There exist many different EDAs that differ one with each other by the probabilistic models used and their construction. In this work, we are going to consider the univariate marginal distribution algorithm (UMDA), which is the most basic EDA and was introduced by Mühlenbein and Paaß (1996) and Mühlenbein (1997) for binary optimization problems in the late 1990s. Mathematically, a univariate model decomposes the probability of a candidate solution $\boldsymbol{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ into the product of probabilities of individual variables as

$$
p(\boldsymbol{x})=p\left(x_{1}, x_{2}, \ldots, x_{n}\right)=p\left(x_{1}\right) p\left(x_{2}\right) \cdots p\left(x_{n}\right)
$$

where $p\left(x_{i}\right)$ is the probability of variable $x_{i}$, and $p\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is the probability of the candidate solution $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$. In the case of binary problems, we can define the probability of $x_{i}$ as $p\left(x_{i}=1\right)=r_{i}$ and $p\left(x_{i}=0\right)=1-r_{i}$, each $x_{i}$ following a Bernouilli distribution with a parameter value equal to $r_{i}$. On the other hand, we use $D$, to represent the population of $N$ individuals with $n$ binary variables. In (3), we present a short example with a population size set of $N=10$ and $n=6$ binary variables per solution. Assuming that the initial population is obtained at random by sampling the following probability function $p\left(x_{i}=1\right)=0.5$ for $i=1, \ldots, 6$, then a possible $D$ is

$$
\begin{array}{llll}
\boldsymbol{x}_{1}=(0,1,1,1,1,0) & f\left(\boldsymbol{x}_{1}\right)=2, & \boldsymbol{x}_{2}=(0,1,1,1,1,1) & f\left(\boldsymbol{x}_{2}\right)=3, \\
\boldsymbol{x}_{3}=(1,0,0,1,1,0) & f\left(\boldsymbol{x}_{3}\right)=1, & \boldsymbol{x}_{4}=(1,1,1,0,1,0) & f\left(\boldsymbol{x}_{4}\right)=1, \\
\boldsymbol{x}_{5}=(0,1,0,0,0,1) & f\left(\boldsymbol{x}_{5}\right)=2, & \boldsymbol{x}_{6}=(0,1,0,0,1,0) & f\left(\boldsymbol{x}_{6}\right)=4, \\
\boldsymbol{x}_{7}=(0,0,1,1,1,0) & f\left(\boldsymbol{x}_{7}\right)=4, & \boldsymbol{x}_{8}=(1,0,1,0,1,0) & f\left(\boldsymbol{x}_{8}\right)=5, \\
\boldsymbol{x}_{9}=(0,1,0,0,0,0) & f\left(\boldsymbol{x}_{9}\right)=5, & \boldsymbol{x}_{10}=(0,1,1,1,1,1) & f\left(\boldsymbol{x}_{10}\right)=3,
\end{array}
$$

where $f$ is a fitness function, and $f(\boldsymbol{x})$ is the fitness value of each individual, $\boldsymbol{x}$. Similarly, we use $D^{S e}$, to represent the population of the selected $S e$ individuals from $D$, where $S e<N$. This can be done using one of the standard selection methods that are common in evolutionary computation, and which use information from the fitness function. Hence, individuals with better fitness values have a bigger chance of being selected. Let us assume that our selection method is truncation and that we select half of the population, that is, $S e=5$. The population of selected individuals $D^{S e}$ is represented by (4):

$$
\begin{aligned}
\boldsymbol{x}_{1} & =(0,1,1,1,1,0) \\
\boldsymbol{x}_{2} & =(0,1,1,1,1,1) \\
\boldsymbol{x}_{3} & =(1,0,0,1,1,0) \\
\boldsymbol{x}_{4} & =(1,1,1,0,1,0) \\
\boldsymbol{x}_{5} & =(0,1,0,0,0,1)
\end{aligned}
$$

In UMDA, the interest is to estimate $p\left(\boldsymbol{x} \mid D^{S e}\right)$, that is, the joint probability distribution over one individual $\boldsymbol{x}$ being among the selected individuals $D^{S e}$. Therefore, $p\left(x_{i} \mid D^{S e}\right)$ with $i=1, \ldots, 6$ is estimated from $D^{S e}$ using its corresponding relative frequency, $p\left(x_{i}=1 \mid D^{S e}\right)$. Thus, using the information from (4), the univariate marginal frequencies are as follows:

$$
\begin{array}{ll}
p\left(x_{1}=1 \mid D^{S e}\right)=2 / 5, & p\left(x_{2}=1 \mid D^{S e}\right)=4 / 5 \\
p\left(x_{3}=1 \mid D^{S e}\right)=3 / 5, & p\left(x_{4}=1 \mid D^{S e}\right)=3 / 5 \\
p\left(x_{5}=1 \mid D^{S e}\right)=4 / 5, & p\left(x_{6}=1 \mid D^{S e}\right)=2 / 5
\end{array}
$$

Consequently, with the learned model and the values of (5), we can generate the next population $D$, where the first binary variable for each new candidate solution has a probability of 0.4 of being 1 , and a 0.6 chance of being a 0 . The second one has a 0.8 chance of being 1 , and 0.2 of being a 0 , and so on. Finally, we repeat the selection, estimation, and sampling steps, until a stopping criterion is reached, for example, a maximum number of generations Tmax. The general form of the UMDA is as follows:

- STEP 0 (Initialization): Set $t \leftarrow 1 . D_{0} \leftarrow$ Generate $N>0$ individuals randomly.
- STEP 1 (Selection): $D_{t-1}^{S e} \leftarrow$ Select $S e<N$ individuals for $D_{t-1}$ according to a selection method.
- STEP 2 (Estimation): $p_{t}\left(x_{i} \mid D_{t-1}^{S e}\right) \leftarrow$ Compute the univariate marginal frequencies of the selected set.
- STEP 3 (Sampling): $D_{t} \leftarrow$ Generate $N$ new individuals according to the distribution $p_{t}(\boldsymbol{x})=$ $\prod_{i=1}^{n} p_{t}\left(x_{i} \mid D_{t-1}^{S e}\right)$. Set $t \leftarrow t+1$.
- STEP 4: If termination criteria are not met, go to STEP 1.


# 2.2.1. EDA for the SSMZ problem 

In this section, we define the methodology to solve the SSMZ problem using the population-based method of UMDA along with the objective function to evaluate the fitness for each candidate solution, which we call as EDA-SSMZ algorithm.

## Individual representation

Designing any iterative metaheuristic needs a representation of a solution. The individual representation plays a major role in the efficiency and effectiveness of any metaheuristic, and constitutes an essential step in designing a metaheuristic. A solution for the EDA-SSMZ problem represents a partition of the field using a specific number of management zones. We implement an indirect encoding (representation) for the SSMZ problem. First, each possible edge inside of the grid is enumerated and labeled to create the representation of solutions for the SSMZ problem. Then, the candidate solution is generated with a vector of 1 s or 0 s represented by $\boldsymbol{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ where $x_{i}$ indicates if the $i$ th edge inside of the grid (binary variable) appears in the solution or not. The size of the search space is determined by $2^{\left[n_{c}\left(n_{c}-1\right)+n_{c}\left(n_{c}-1\right)\right]}$ possible candidate solutions, where $n_{c}$ and $n_{c}$ represent the number of rows and columns inside of the grid, respectively.

Figure 4 shows the representation (binary encoding) for a plot with 16 soil samples, $4 \times 4$, where Fig. 4a shows the sequence of the 16 soil samples numbered by $m_{1}, m_{2}, \ldots, m_{16}$, and the total edges

![img-4.jpeg](img-4.jpeg)

Fig. 4. Individual representation for the SSMZ problem. (a) The binary encoding, (b) a candidate solution, and (c) a partition of the field with six management zones.
![img-5.jpeg](img-5.jpeg)

Fig. 5. Four candidate solutions representing a similar delineation as Fig. 4b.
inside of the grid (binary variables) numbered by $1,2, \ldots, 24$. Figure 4 b illustrates a candidate solution for the SSMZ problem given by

$$
\boldsymbol{x}=\left(0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0\right)
$$

where it is possible to determine which edges inside of the grid are activated, and therefore, which soil samples correspond to which management zone. Figure 4c illustrates a partition of the field with six management zones where $q_{1}$ contains $m_{1}$ and $m_{2} ; q_{2}$ contains $m_{3}, m_{4}, m_{6}, m_{7}, m_{8}, m_{10}$, and $m_{14} ; q_{3}$ contains $m_{5} ; q_{4}$ contains $m_{9}$ and $m_{13} ; q_{5}$ contains $m_{11} ;$ and $q_{6}$ contains $m_{12}, m_{15}$, and $m_{16}$. Note that $q_{i} \subseteq S$, where $S=\left\{m_{1}, m_{2} \ldots, m_{M}\right\}$ denotes the set of soil samples on the grid, and $q_{i}$ represents a subset of the soil samples in the management zone $i$. We represent the set of management zones $Q$ as a collection of subsets (partitions) of the soil samples $\left\{q_{1}, q_{2}, \ldots, q_{k}\right\}$, and $|Q|$ as the total number of management zones.

Our indirect encoding can generate candidate solutions that represent the same delineation of the field, for example, Fig. 5a and d shows four candidate solutions that produce a similar result as Fig. 4b. In this particular case, these candidate solutions show a delineation of the field that corresponds to the same solution illustrated in Fig. 4c with six management zones. Note that, in

the candidate solutions of Fig. 5a and d, not all activated edges separate two zones, that is, some edges are isolated, which does not generate infeasibility. An isolated edge does not split a region of the plot into two different zones. For example, Fig. 5a and d shows the isolated edges for the four candidate solutions, which correspond to the edges labeled with the numbers $3,6,7$, and 10 , respectively. Moreover, the procedures of the EDA-SSMZ ignore these isolated edges to avoid them in the final delineation.

The EDAs build and maintain a probability distribution of the current population over the search space, from which the next generation of individuals is sampled. The fact that our algorithm obtains similar solutions tells us that it has converged, and therefore an edges pattern on the grid is learned. The above means that the probability of variable $x_{i}$ could remain fixed at either zero or one, obstructing some search space regions in the next generation. On the other hand, the chance that some edges are active or not on the grid depends on whether their marginal frequencies are different from zero or one.

# Fitness function 

The objective of the fitness function is to have the means to evaluate each one of the possible individuals so that the search algorithm can compare the different solutions and act in consequence to find the best solution. It is important to define it appropriately to assess the search for the SSMZ problem. For our EDA-SSMZ, the best solution represents the solution with the minimum number of management zones.

First, let us define our SSMZ problem as a combinatorial optimization problem, which can be described as finding a $k$-partition of the field using a candidate solution, $\boldsymbol{x}$. The objective is minimizing the number of management zones (partitions) given by $f(\boldsymbol{x})=\left|\left(q_{1}, \ldots, q_{k}\right)\right|$, subject to some constraints in the shape of these partitions and on the homogeneity level of the soil samples inside each partition $i \in K$, where $K \in\{1, \ldots, k\}$. The mathematical model for the SSMZ problem is expressed as follows:

$$
\begin{aligned}
& \text { Minimize } f(\boldsymbol{x})=\left|\left(q_{1}, \ldots, q_{k}\right)\right| \\
& \text { subject to } q_{i} \neq \emptyset, \quad i \in K \\
& \bigcup_{i \in K} q_{i}=S \\
& q_{i_{1}} \cap q_{i_{2}}=\emptyset, \quad i_{1}, i_{2} \in K \\
& \delta\left(q_{i}\right) \text { is connected, } \quad i \in K \\
& h(Q, S) \geq \alpha
\end{aligned}
$$

where (6) is the fitness function that minimizes the number of management zones. Constraints (7)(9) define the $k$-partition: with no-empty zones, all soil samples are covered by the zones generated, and there is no intersection of soil samples between zones, respectively. Constraints (10) represent the contiguity of the soil samples, where $\delta\left(q_{i}\right)$ represents the set of soil samples that are adjacent

to at least one soil sample of $q_{i}$. Constraint (11) guarantees the homogeneity of the management zones $Q=\left\{q_{1}, \ldots, q_{k}\right\}$. Note that constraints (7)-(10) can be easily handled by the representation proposed in the previous section. For constraint (11), it is necessary to introduce a special constraint handling strategy. In this work, we use a simple penalizing mechanism where infeasible solutions are considered during the search process.

The penalty function modifies the original fitness function $f(\boldsymbol{x})$ applied to a candidate solution $\boldsymbol{x}$ such that $f^{\prime}(\boldsymbol{x})=f(\boldsymbol{x})+\tilde{P}(\boldsymbol{x})$, where $\tilde{P}(\boldsymbol{x})$ is a distance metric from the infeasible point to the feasible region $\mathcal{F}$ (this might be simply a count of the number of constraints violated). The penalty function $\tilde{P}$ is zero for feasible solutions, and it increases with distance from the feasible region (for minimization problems). Equation (12) shows that one simple strategy is to calculate the homogeneity of the management zones (based on Equation (2)):

$$
h(Q, S)=\left(1-\frac{\sum_{i \in K}\left[s\left(q_{i}\right)-1\right] \sigma^{2}\left(q_{i}\right)}{\sigma_{T}^{2}(S)[|S|-|Q|]}
$$

and then we use the penalty function

$$
\tilde{P}(\boldsymbol{x})= \begin{cases}0, & \text { if } \quad h(Q, S) \geq \alpha \\ \tilde{M}-h(Q, S), & \text { if } \quad h(Q, S)<\alpha\end{cases}
$$

where $\alpha$ is a given homogeneity parameter, and the fixed number $\tilde{M}$ is large enough that feasible solutions are preferred; $s\left(q_{i}\right)$ represents the number of soil samples in the management zone $q_{i}$; $\sigma_{i}^{2}\left(q_{i}\right)$ represents the variance in $q_{i}$, and finally, $\sigma_{T}^{2}(S)$ represents the total variance about the set of soil samples $S$ in the field. The $\tilde{M}$ value is setting as $\tilde{M}=|S| \cdot 10$, where $|S|$ is the number of soil samples. With this, we ensure that $\tilde{M}$ is large enough for this purpose. Therefore, in the case of some infeasible solution, $\tilde{P}(\boldsymbol{x})$ is one order of magnitude more than $f(\boldsymbol{x})$. If the value of $\tilde{M}$ is large enough, then infeasible points near the constraint boundary will be discarded, which may delay, or even prevent, the exploration of this region. On the other hand, if $\tilde{M}$ is not large enough, then solutions in infeasible regions may dominate the feasible regions.

The fitness evaluation process requires a search process over an adjacency list to find connected soil samples for each management zone. In the worst case, the search process is $O(n \cdot|S|)$, where $|S|$ is the number of soil samples, and $n$ is the number of edges inside of the grid. Finally, the algorithm determines which soil samples belong to which management zones and computes their homogeneity level.

# EDA-SSMZ algorithm 

The most representative steps for the proposed EDA-SSMZ are presented by the Algorithm 1 that takes as inputs the population size $(N)$, the initial probability vector $\left(p_{0}(\boldsymbol{x})\right)$, the selection size $\left(S_{e}\right)$, the homogeneity parameter $(\alpha)$, and the maximum number of iterations (Tmax). With the procedure InitializePopulation $\left(N, p_{0}(\boldsymbol{x})\right.$ ), an initial population of $N$ individuals is generated at random by sampling several Bernouilli distributions using the initial probability vector $p_{0}(\boldsymbol{x})$. Then, with EvaluatePopulation $(D, \alpha)$, a fitness function $f^{\prime}(\boldsymbol{x})$ is evaluated, which weighs the infeasibilities using the objective (6) and the constraint (11). In this step, we evaluate each individual of the

# Algorithm 1. EDA-SSMZ 

Input:
$\alpha:=$ homogeneity parameter
$S_{c}:=$ selection size
$N:=$ population size
$p_{0}(\boldsymbol{x}):=$ initial probability vector
Tmax :=maximum number of iterations
Output: $Q^{\text {best }}$ : A feasible solution, $k$-partition of $S$ (soil samples)
$1: \quad t \leftarrow 1$
2: $\quad D_{0} \leftarrow$ InitializePopulation $\left(N, p_{0}(\boldsymbol{x})\right)$
3: EvaluatePopulation $\left(D_{0}, \alpha\right)$
4: $Q^{\text {best }} \leftarrow$ GetBestSolution $\left(D_{0}\right)$
5: for $t=1,2, \ldots$, Tmax do
6: $\quad D_{t-1}^{S e} \leftarrow$ SelectBestSolutions $\left(D_{t-1}, S e\right)$
$7: \quad p_{t}(\boldsymbol{x}) \leftarrow$ CalculateMarginalFrequency $\left(D_{t-1}^{S e}\right)$
8: $\quad D_{t} \leftarrow$ GeneratePopulation $\left(N, p_{t}(\boldsymbol{x})\right)$
9: EvaluatePopulation $\left(D_{t}, \alpha\right)$
10: Best $\leftarrow$ GetBestSolution $\left(D_{t}\right)$
11: $\quad Q^{\text {best }} \leftarrow$ UpdateBestSolution $\left(Q^{\text {best }}\right.$, Best $)$
12: $\quad t \leftarrow t+1$
13: end for
14: return $Q^{\text {best }}$
population $D$ using the parameter of homogeneity $\alpha$, and store the best individual in $Q^{\text {best }}$ obtained with GetBestSolution $(D)$. Procedure SelectBestSolutions $\left(D_{t-1}, S e\right)$ selects the best $S e$ individuals from population $D_{t-1}$, according to the fitness function. Then the joint probability distribution $p_{t}(\boldsymbol{x})$ is estimated with CalculateMarginalFrequency $\left(D_{t-1}^{S e}\right)$, using the population of the selected individuals, $D_{t-1}^{S e}$. Procedure GeneratePopulation $\left(N, p_{t}(\boldsymbol{x})\right)$ generates the new population of solutions using the estimated probability model $p_{t}(\boldsymbol{x})$. The algorithm evaluates the new individuals with EvaluatePopulation $(D, \alpha)$, gets the best individual of the population with GetBestSolution $(D)$, and stores it in Best. Finally, the algorithm updates the best solution, comparing the best current solution with the solution obtained in the previous iteration (UpdateBestSolution $\left(Q^{\text {best }}\right.$, Best $)$ ). The above step preserves the best solution (or incumbent for short) to the current iteration. The EDASSMZ algorithm iterates until the maximum of iterations Tmax has been reached and returns the best solution found, $Q^{\text {best }}$.

## 3. Experimental results

In this section, we present the experimental results to validate the performance of our EDA-SSMZ algorithm. In Section 3.1, we describe two exact approaches used to compare our methodology. In Section 3.2, we show the set of instances used to test our algorithm. In Section 3.3, we present the calibration of the critical parameters for the EDA. Finally, Sections 3.4 and 3.5 show the experimentation and some graphical visualizations of the results, respectively.

Table 1
Characteristics for each instance group of the random instances
# 3.1. Benchmark algorithms 

We compare the EDA-SSMZ algorithm with the exact approaches of Cid-Garcia et al. (2013) and Albornoz et al. (2015) that proposed an MILP and a BILP, respectively. To the best of our knowledge, these approaches are the first in the literature to generate rectangular and homogeneous management zones using operations research techniques.

### 3.2. Test problem instances

### 3.2.1. Real-field instances

To evaluate the performance of the algorithm, we used the real-field instances proposed by CidGarcia et al. (2013) and adapted in the work of Albornoz et al. (2015). These instances show an agricultural field with 40 soil samples, which extract information about the following soil properties: OM, pH , phosphorous, and sum of bases. For these instances, two dummy soil samples were considered to complete a perfect grid (the pink circles of Fig. 3b), and their values were fixed considering the neighbor of the left.

### 3.2.2. Randomly generated instances

Another set of instances was generated at random to evaluate the scalability of the algorithm. We use the data information for OM of the real-instances because this property showed more variability than the rest. To generate a random value for each soil sample, we consider a uniform distribution with the maximum and minimum value obtained from the $O M$ property. These random values were generated using the Mersenne Twister, a strong pseudo-random number generator (PRNG). In nonrigorous terms, a strong PRNG has a long period and statistically uniform distribution of values (Shema, 2012).

The instances were grouped into five classes according to the number of soil samples in the field, with a minimum of 42 and a maximum of 400 soil samples. Each class contains ten different instances considering alpha values of $0.5,0.7$, and 0.9 for the homogeneity level ( 30 instances per class). Recall that alpha values $(\alpha)$ greater than or equal to 0.5 are desirable to guarantee a homogeneity management zone delineation. For this set of instances, we assume the plots have a rectangular or square shape. Therefore, it is not necessary to add dummy soil samples.

Table 1 presents the characteristics for each class of the random instances. The first column represents the class of the instance. Columns 2 and 3 show the width and height of the plot regarding the

number of soil samples, respectively. The fourth column represents the total number of soil samples. The last column is the total number of potential management zones computed for each plot according to the algorithm presented in Cid-Garcia et al. (2013), which is pseudo-polynomial. This set of potential management zones contains only zones with a rectangular or square shape, which depends on the size of the field (soil samples in the width and height of the plot), and the size of the zone with the minimum number of soil samples in the width and height. In real-life scenarios, the number of soil samples in the plots commonly corresponds to instances of class 1 or 2 (the set of random instances can be downloaded from https://github.com/NxtrCd/Instances-EDA-SSMZ.git).

# 3.3. Calibration of the EDA-SSMZ algorithm 

Calibration of algorithms is one of the most important steps in order to obtain good results. To set the appropriate parameters for the EDA-SSMZ algorithm, we used the iterated racing procedure. This procedure focuses on the sampling parameter configurations according to a particular distribution, evaluating them using either Friedman's test or the $t$-test, and refining the sampling distribution to bias the sampling toward the best configurations. To calibrate the parameters, we used Friedman's test and the irace ver. 3.1.2112M, a software package that implements the iterated racing procedure for metaheuristic parameter tuning (López-Ibáñez et al., 2016). For each class, the tuning procedure was performed using a budget of 5000 experiments with the following ranges for the parameter sampling: $p_{0}(\boldsymbol{x}) \in[0.95,0.99], N \in[1000,25000], S e \in[15,1500]$, and $T \max \in[50,100]$. For each iteration, the irace package determines elite parameter configurations and selects the best of them. The tuning procedure is conducted several times, and favorable parameter settings are selected. For the real-field instances the parameters obtained were $p_{0}(x)=(0.95, \ldots, 0.95), N=9902, S e=669$, and $T \max =32$. For the generated instances the parameters were $p_{0}(x)=(0.99, \ldots, 0.99), N=9902, S e=669$, and $T \max =32$, except for Class 5 where $T \max =60$, and when $\alpha=0.9$ then $N=24535$, and $S e=200$.

### 3.4. Computational results

The computational experiments were carried out on a server with four Intel Xeon E5-2620 v2 Six-Core Processor @2.10 GHz, running the Linux operating system with Ubuntu Server release 18.04.2 LTS, and 128 GB of RAM. The EDA-SSMZ algorithm was implemented in C/C++ and replicated 50 times with the tuned parameter settings. The MILP and BILP approaches of Section 3.1 were executed in the same computer to compare the EDA-SSMZ algorithm.

### 3.4.1. Results for real-field instances

In this section, we evaluate the EDA-SSMZ algorithm using the real-field instances described in Section 3.2. Table 2 shows the experimental results comparing the BILP and MILP approaches with the EDA-SSMZ algorithm. Numbers in bold are the best solutions. The first column presents the chemical soil property (OM, pH, P, and SB). The second column determines the homogeneity level of the management zones ( $\alpha$-parameter). Columns 3-6 present the results for the EDA-SSMZ

Table 2
Experimental results for the real-field instances

showing the minimum, average, maximum, and average time (in seconds) over 50 independent runs of the algorithm. Columns $7-10$ are the results for the BILP and MILP, showing the number of zones $\left(Z^{*}\right)$ and the execution time (in seconds) for each approach. The last column represents the improvement (in $\%$ ) of the EDA-SSMZ (considering its best solution) in comparison with the other approaches. The percentage is computed as $\left|\operatorname{Min}-Z^{*}\right| / \operatorname{Min} \times 100$. The last row shows the total number of management zones obtained by each approach.

The EDA-SSMZ algorithm obtains the best solutions in all the real-field instances. However, for 10 instances, the MILP and BILP approaches reach similar solutions in comparison with our method. For OM and SB, the results of the EDA-SSMZ and the exact approaches, in almost all cases, are very different (high percentages of improvement). On the contrary, the results for pH and P are relatively similar (low percentages of improvement). That is because the data information for OM and SB exhibits more variability than the rest of the soil properties, and delineating the field with management zones that use orthogonal shapes allows using a minor number of management zones than that with regions with rectangular or square shapes.

It is also noteworthy that the percentage of improvement for the EDA-SSMZ algorithm is up to $200 \%$ higher compared to the other exact approaches, and the computational time for solving the instances is higher for the EDA-SSMZ than the exact methodologies, for example, on average, around 23 seconds against less than 1 second. This behavior is expected because the solution space for the EDA-SSMZ is bigger. However, the execution time does not represent a disadvantage for the algorithm.

# 3.4.2. Results for random instances 

In this section, we test the performance of the EDA-SSMZ using the random instances explained in Section 3.2. The experimental results for each class of instances (Classes 1-5) are presented in Tables 3-7, which have similar format as Table 2, except for the first two columns that show the homogeneity level ( $\alpha$ value) in the first column, and the number of instance in the second column.

For all the random instances, the EDA-SSMZ can provide better solutions than the ones provided by the exact approaches. To highlight this behavior, we mark in boldface the best solution obtained for each instance. An important characteristic of the EDA-SSMZ is that even the worst solutions outperform the best ones obtained by the exact approaches. However, the computational time for the EDA-SSMZ increases considerably with the instance size and the homogeneity level in comparison with the exact approaches, for example, for Class 5, with the alpha parameter equal to 0.9 , in the worst case our algorithm takes around 3.5 hours in solving the instance, against the 45 seconds of the MILP approach. As in the real-field instances, this behavior is expected because the solution space for the EDA-SSMZ algorithm is bigger.

Currently, it seems a long time for large instances, but, in practice, it is reasonable since the agricultural production cycle is every year or, in some cases, every six months. Furthermore, we highlight that the number of soil samples in real fields corresponds, generally, to small instances (Class 1 or 2 ) that can be efficiently solved by our EDA-SSMZ in less than two minutes, as can be seen in Tables 3 and 4. Note that, for large instances (Table 7), the homogeneity level ( $\alpha$-parameter) plays an important role in the execution of the algorithm, that is, when the alpha value tends to 1 , our algorithm requires more computational time. With this, we have detected a future research line

Table 3
Experimental results for the random instances: Class 1

where it is possible to apply the parallelization of the EDA-SSMZ to decrease the computational time for large instances.

Table 8 shows a summary of the experimental results for the random instances. The first and the second columns present the class and field sizes (the total number of soil samples on the width and height). The third column is the homogeneity level ( $\alpha$-parameter ). Columns 4-6 show the results for the EDA-SSMZ algorithm (the minimum, the average, and the maximum of management zones). Columns 7 and 8 are the results for the BILP and MILP approaches, respectively. The last column shows the percentage of improvement obtained by the EDA-SSMZ algorithm. Finally, the last row presents the total of management zones obtained by each approach for all the classes.

Table 4
Experimental results for the random instances: Class 2

For each class, we observe when the homogeneity level decreases ( $\alpha$ tends to 0.5 ), then the average relative improvement of the EDA-SSMZ increases, and when the homogeneity level increases ( $\alpha$ tends to 1 ), then the average relative improvement decreases. This behavior is not surprising since when a high level of homogeneity is imposed, and there is variability in the information of the soil sample, the EDA-SSMZ tends to assign each soil sample within an individual zone. Therefore, the number of possibilities for delineation is reduced, and the percentage of improvement decreases too. Furthermore, the percentage of improvement increases with the size of the instance, that is, larger instances show better improvements than short ones. For example, instances of Class 5 show an average percentage of improvement up to $277 \%$ for $\alpha=0.5,159 \%$ for $\alpha=0.7$, and $24 \%$ for $\alpha=0.9$. In contrast with the $89 \%$ for $\alpha=0.5,70 \%$ for $\alpha=0.7$, and $19 \%$ for $\alpha=0.9$ on the instances of Class 1.

Table 5
Experimental results for the random instances: Class 3

Figure 6 shows a summary for each class of the random instances presented in Tables 3-8. The $X$-axis represents the instance with its corresponding alpha-value, and the $Y$-axis the number of partitions used in the final delineation. Note for all the instances, our EDA-SSMZ algorithm (black lines) improves the BILP and MILP approaches (red lines).

# 3.5. Visualization 

In Figs. 7-9, we show some configurations obtained by the EDA-SSMZ algorithm compared with the $B I L P$ approach, considering the OM as chemical soil property and fixing the homogeneity

# Class 1 

![img-6.jpeg](img-6.jpeg)

Class 3
![img-7.jpeg](img-7.jpeg)

Class 5
![img-8.jpeg](img-8.jpeg)

Class 2
![img-9.jpeg](img-9.jpeg)

Class 4
![img-10.jpeg](img-10.jpeg)

## Summary

![img-11.jpeg](img-11.jpeg)

Fig. 6. EDA-SSMZ vs. BILP/MILP: a summary for each class of randomly generated instances.

Table 6
Experimental results for the random instances: Class 4

level ( $\alpha$-parameter) to $0.5,0.7$, and 0.9 , respectively. Figures $7 \mathrm{a}, 8 \mathrm{a}$, and 9 a represent the solution obtained by the EDA-SSMZ algorithm, and Figs. 7b, 8b, and 9b show the solution of the BILP. We can observe that our approach selects figures with orthogonal shapes to partitioning the field, which minimizes the number of management zones in the final delineation.

# 4. Conclusions 

In this paper, we introduce a new methodology to solve the problem of delineating homogeneous SSMZ in agricultural fields based on an EDA. This problem consists of partitioning the field in

Table 7
Experimental results for the random instances: Class 5

small regions considering a specific soil property, chemical or physical, such that the generated zones satisfy a determined level of homogeneity. To the best of our knowledge, this is the first approach that generates management zones with orthogonal shape, for example, L or T, which minimizes the number of regions required in the final delineation of the field.

Our methodology was tested on a set of real-life instances, and it was compared with other operations research methodologies presented in the literature. Furthermore, a set of instances was generated at random to analyze the scalability of the method. The experimental results show that our method is efficient and robust (the average/deviation behavior of the algorithm over different runs of the algorithm) to solve instances with different size for the SSMZ problem by improving the solutions presented by the other operations research approaches. According to the size of the

Table 8
Experimental results for the random instances: a summary
(a)
![img-12.jpeg](img-12.jpeg)

Fig. 7. Management zones for organic matter when $\alpha=0.5$. (a) The results for the EDA-SSMZ algorithm (five zones) and (b) the results for the BILP approach (nine zones).
instances, the EDA-SSMZ algorithm can find an average relative improvement is up to $277 \%$ when $\alpha=0.5$, between $70 \%$ and $160 \%$ when $\alpha=0.7$, and, at most, $40 \%$ when $\alpha=0.9$.

The EDA-SSMZ represents the agricultural field with a grid composed of edges and soil samples, from which and adjacency list is created. The execution time for the EDA-SSMZ increases considerably for large instances because our fitness evaluation process requires a search process (like depth-first search) over the adjacency list to find which soil samples belong to which management zone. Moreover, the fitness evaluation process is applied in a sequential way in each generation and for each individual of the population. Therefore, this is an important issue to improve. In particular, a parallel evolutionary approach can effectively reduce the computational time of the

![img-13.jpeg](img-13.jpeg)

Fig. 8. Management zones for organic matter when $\alpha=0.7$. (a) The results for the EDA-SSMZ algorithm ( 9 zones) and (b) the results for the BILP approach ( 14 zones).
![img-14.jpeg](img-14.jpeg)

Fig. 9. Management zones for organic matter when $\alpha=0.9$. (a) The results for the EDA-SSMZ algorithm (17 zones) and (b) the results for the BILP approach ( 20 zones).

EDA-SSMZ and lead to an increased exploration and better diversity, compared to a sequential approach. In future research, our attention will concentrate on two main parallel approaches: the evolution of parallel populations and the parallelization of the fitness evaluation process. Additionally, we consider formulating our combinatorial optimization problem as a mixed-integer program model (MIP) to obtain optimal solutions for the SSMZ problem or develop new methods for generating acceptable lower bounds. The main difficulty for both strategies is the procedure of finding connected components to calculate the evaluation of the management zone.

# Acknowledgments 

This study was partially supported by the Chairs Program of the National Council of Science and Technology (CONACYT) projects 843 and 2193. Salvador V. wishes to acknowledge graduate scholarship from CONACYT. Jose A. Lozano is partially supported by the Basque Government through the BERC 2018-2021 program, IT1244-19 and ELKARTEK program (3KIA KK-2020/00049) by the Spanish Ministry of Science, Innovation and Universities: BCAM Severo Ochoa accreditation SEV-2017-0718, TIN2016-78365-R, and PID2019-104966GB-I00.
