# A self-adaptive estimation of distribution algorithm with differential evolution strategy for supermarket location problem 

Bing-Hai Zhou ${ }^{1} \cdot$ Fen Tan ${ }^{1}$<br>Received: 22 March 2018 / Accepted: 23 January 2019 / Published online: 8 March 2019<br>(c) Springer-Verlag London Ltd., part of Springer Nature 2019


#### Abstract

In modern production systems, an ever-rising product variety has imposed great challenges for in-plant part supply systems used to feed mixed-model assembly lines with required parts. In recent years, many automotive manufacturers have identified the supermarket concept as an efficient part feeding strategy to enable JIT (Just-in-time) deliveries at low costs. This paper studies a discrete supermarket location problem which considers the utilization rate and capacity constraint of the supermarkets simultaneously. Firstly, a mathematical model is developed with the objective of minimizing the total system cost consisting of operating cost and transportation cost. Then, a self-adaptive estimation of distribution algorithm with differential evolution strategy, named DE/AEDA, is proposed to solve the problem. Finally, computational experiments are carried out to analyze the performance of the proposed algorithm compared with the benchmark algorithm by using a non-parametric test method. The results indicate that the proposed algorithm is valid and efficient.


Keywords In-plant material delivery $\cdot$ Supermarket $\cdot$ Location $\cdot$ Estimation of distribution algorithm

## 1 Introduction

In the past few decades, in order to satisfy the personalized and diversified demand of customers, mixed-model assembly lines (MMALs) have been widely adopted in today's automobile industry [1, 2]. In this case, several models are to be assembled by the same assembly line. And thousands of diversified parts are obliged to be delivered to multiple stations timely and accurately. Thus, part delivery scheduling at these high-variant MMALs has been a crucial challenge due to the diversified demand and the limited line-side inventory capacity [3, 4].

In most of the past cases, parts are transported from centralized warehouse directly to stations. However, in recent decades, the supermarket concept has been adopted by more and more automobile manufacturers to enable a frequent and small-lot part delivery to ensure the smooth

[^0]flow of assembling production [5]. In this case, parts are intermediately stored in the supermarket, which is a decentralized logistics area near the assembly line where parts are consumed. And the parts in the supermarket are replenished by industrial trucks from the centralized warehouse. Then, based on the predefined schedule, parts required by production are transported to stations by means of tow train on the fixed route. Due to the increase in frequency of material delivery, it is easier and more flexible to re-plan when encountering unexpected situations. Moreover, the line-side inventory and transportation distance can also reduced effectively. In this case, the supermarket concept is increasingly prevalent in automobile production.

Four interrelated decision problems have to be settled when planning and controlling the material delivery process based on this concept [4].
(i) Supermarket location problem (SLP): determining the number and location of these decentralized supermarkets.
(ii) Tow train routing (TTR) problem: determining the number of required tow trains per supermarket and the route of each tow train. The route starts from


[^0]:    $\boxtimes$ Bing-Hai Zhou bhzhou@tongji.edu.cn
    Fen Tan tanfen007@tongji.edu.cn

    1 School of Mechanical Engineering, Tongji University, Shanghai 201804, People's Republic of China

the supermarket, visiting a sequence of stations, and eventually returns back to the supermarket.
(iii) Tow train scheduling (TTS) problem: determining the fixed delivery schedule per tow train, including the number of deliveries and the start time of each delivery.
(iv) Tow train loading (TTL) problem: determining the number of part bins to be loaded to corresponding stations per tour of the tow train.

It is assumed that supermarket system is employed in this paper. However, since the space on the shop floor is scarce and expensive [6], it is necessary to make a reasonable plan to decide on the location plan of supermarkets. In other words, decision (i) is the focus of this paper. The Supermarket location problem (SLP) is the most longterm problem after deciding to implement the supermarket concept concerned with location planning. In this context, the number of supermarkets to be installed on the shopfloor and their exact locations need to be determined. Furthermore, each supermarket is to be roughly assigned to the line segments it serves. Clearly, it has to be differentiated between initial location planning in a newly erected plant and a relocation problem. While in the former case some flexibility for finding a suited location per supermarket exists, in the latter case, typically, severe constraints with regard to the size and location need to be considered. In the objective function the fixed cost caused by any additional supermarket need to be weighed against the operational gains of the supermarket-concept. Clearly, an exact quantification of these gains requires an anticipation over the complete planning hierarchy. For instance, the reduction of the travel distances to the line for any additional supermarket should be exactly quantified.

The supermarket concept is a relatively new field of research. To date, there are few literatures explicitly tackling above decision problems. Vaidyanathan et al. [7] extended the classical vehicle routing problem into a new problem named Just-in-Time Capacitated Vehicle Routing Problem (JITCVRP), to deal with decision problem (ii). It was assumed that the route, once assigned to a tow train, must be served without breaks over the planning horizon, in which decision problem (iii) was not considered. In order to ensure that deliveries are carried out according to the just-in-time principle, the objective of JITCVRP was to minimize the total trip time along all routes. Then, two heuristics were proposed to solve it. Emde and Boysen [8] solved the routing problem (ii) and scheduling problem (iii) simultaneously by the proposed nested dynamic programming procedure, with the objective of minimizing all bins lying in stock over planning horizon and the number of tow trains applied, to make sure a reliable material delivery in line with JIT principle. On this foundation, Emde et al. [9]
further studied the tow train loading problem (iv) given station demands, specific routes and schedules to determine the number of bins to be loaded to corresponding stations per tour of a capacity-limited tow train. They developed an exact algorithm with polynomial time to simultaneously minimize the maximum and the sum inventories near the line. The joint routing (ii), scheduling (iii) and loading (iv) problem of tow train was firstly tackled by Golz et al. [10] in the case of a major German OEM given a set of possible routes to choose. A heuristic procedure was presented to minimize the number of vehicle operators while avoiding stockouts at the line. Fathi et al. [11-13] aimed at minimizing the number of tours and line-side inventories to deal with the scheduling (iii) and loading (iv) problem of tow train jointly with multi-objective delivery scheduling model. The difference among them is that different algorithm was presented based on different priority heuristic rules. As for the focus of this paper, little was published regarding on decision problem (i) in in-plant environment. Emde and Boysen [6] considered the problem of locating supermarkets on the shop floor by determining the optimal number and placements of supermarkets. A dynamic programming scheme was developed because it just assumed that the supermarkets could be established everywhere around the stations without consideration of some unavailable places and capacity limit of the supermarkets. Subsequently, Alnahhal and Noche [14] took into account the above two aspects. Therefore, the time complexity of SLP was improved and the problem was NP-complete. Then, a real genetic algorithm (RGA) was constructed to solve the problem.

To the best knowledge of the authors, the aforementioned papers are the only papers explicitly solving decision problem (i). SLP bears some similarities to the wellknown capacitated p-median problem (CPMP), one of the discrete facility location problems (FLP). The aim is to locate a given number of facilities from a set of sites to satisfy the demands of all customers, so that the sum of the weighted distances between facilities and assigned customers is minimized. There are two differences between CPMP and SLP. Firstly, customers served by one facility are consecutive in SLP. Secondly, unlike the CPMP, the number of facilities is not given, which means that it should be optimized to find the optimal number of supermarkets. Therefore, models and methods of CPMP are partially applicable to the SLP. As is known to all, the CPAM is an NP-hard problem and thus it is unpractical to solve it by exact algorithms [15]. Genetic algorithm (GA) [16-18], tabu search (TS) algorithm [19] and other evolutionary algorithms are most commonly used to solve CPMP [20, 21]. Correa et al. [22] proposed a modified GA with a new heuristic "hyper-mutation" operator to minimize the sum of the weighted distances. Herda [15] employed a

combined GA, combining hypermutation from G1 and dominant crossover from G2, for the CPMP. The results turned out that the authors built a high-performance parallel algorithm. As for TS, França et al. [23] developed a new adaptive tabu search approach to solve the problem. In addition, two local search heuristics, pairwise interchange and insertion, were added to generate neighborhood solution. Yaghini et al. [24] combined TS algorithm and a proposed cutting-plane neighborhood structure to construct an efficient hybrid metaheuristic algorithm. Landa-Torres [25] applied two different grouping-based algorithms to tackle the CPMP, including grouping genetic algorithm (GGA) and grouping harmony search approach (GHS). By computational experiments, the proposed grouping methods were proved to outperform other benchmark algorithms.

It has been known that the metaheuristics used in aforementioned literatures are mainly derived from GA, which generates new candidates by crossover and mutation operators. Some new metaheuristics have been developed last few decades, and it indicates that new metaheuristics ought to be explored to deal with the SLP. Estimation of distribution algorithm (EDA), originally introduced by Mühlenbein and Paass [26], is a new class of group evolutionary algorithms (EA) based on statistical learning theory [27]. Unlike other EAs, instead of generating new solutions by chromosome recombination, EDA describes the distribution information of candidate solutions in search space by establishing the probability model, based on which new solutions are sampled [28]. It avoids the blindness and randomness caused by chromosome recombination, thus the search efficiency is effectively improved. Due to its great search efficiency, EDA received much attention and has been applied to solve many engineering optimization problems, including flow shop scheduling [29], project scheduling [30, 31], nurse rostering [32] etc. To the best of authors' knowledge, there has not been published paper dealing with discrete SLP problem using EDA. In this paper, EDA is chosen as the main framework of our optimization algorithm.

In view of some unavailable places on the assembly shop, this paper proposes the discrete SLP problem considering the utilization rate and capacity limit of the supermarkets simultaneously with the objective of minimizing the total system cost consisting of operating and transportation cost. Then, the authors choose EDA as the main framework of our optimization algorithm. EDA is good at global searching, but lacks the ability for refined search. Therefore, differential evolution (DE) strategy and adaptive learning rate mechanism are integrated into EDA to enhance the performance of algorithm. In this paper, the proposed algorithm is named the self-adaptive estimation
of distribution algorithm with differential evolution strategy (DE/AEDA).

The remainder of this paper is organized as follows. Section 2 describes the problem formulations of the discrete SLP problem. Section 3 is used to present the proposed DE/AEDA algorithm in detail. Computational experiments are carried out to evaluate and validate the performance of the algorithm in Sect. 4. Finally, Sect. 5 draws some conclusions.

## 2 Problem statement

### 2.1 Problem description and assumptions

In this paper, the supermarket is a decentralized logistics area near the assembly line where parts are consumed and it is replenished by industrial trucks from the centralized warehouse. Parts are intermediately stored in the supermarket, and then transported to stations by tow trains on fixed routes based on the predefined schedule. There are $|S|$ stations along the mixed-model assembly lines. Due to the limited space in the assembly shop, the shop needs to be properly planned to determine the best supermarket layout.

In order to obtain a proper mathematical model, premises and assumptions are made as follows:

1. Cycle time is selected as the basic unit time for the system.
2. Supermarket serves consecutive stations, that is to say, the supply area of supermarket is no-overlapping.
3. Materials are stored by bins of uniform size, thus, stations' demand and the capacity of the supermarket are consequently represented by the number of bins.
4. As the planning of supermarkets is a long-term decision-making issue, the demand at each station is a pre-estimate.

### 2.2 Notations and model formulation

In this subsection, a mathematical model is established based on aforementioned assumptions. For the convenience of description, the notations and explanations are listed in Table 1.

Concerning the goal of SLP, the classic objective of minimizing the total cost including average operating cost per shift and transportation cost of tow trains is certainly applicable, which is also widely applied in many other literatures [6, 14]. Since the capacity of tow trains is rather limited, how many and which stations can be supplied in one tour is restrained. Not too many high-demand stations can be served in one tour, or else the tow trains will be overloaded. In this paper, it is also supposed that the

Table 1 Notations and explanation
capacity of the supermarket is sufficient to fulfill the total demand of its responsible supply area, because overworked supermarkets will have to make use of additional vehicles, routes and safety stock, all leading to higher operating cost. According to the above assumptions and notation definitions, the SLP problem is now formulated as follows:Objective function:

Minimize $m \cdot \Gamma+u \cdot e_{g} \cdot \sum_{g=1}^{m} \sum_{s=o_{g-1}+1}^{o_{g}} d_{s}$
Subject to
$o_{0}=1$
$o_{g-1}+1 \leq o_{g} \quad \forall g \in G$
$o_{m}=|S|$
$\sum_{s=o_{g-1}+1}^{o_{g}} d_{s} / C \geq \eta \quad \forall g \in G$
$\sum_{s=o_{g-1}+1}^{o_{g}} d_{s} \leq C \quad \forall g \in G$
where

$$
\begin{aligned}
e_{g}= & \left(\left|x_{o_{g}}-x_{o_{g-1}+1}\right|+\left|y_{o_{g}}-y_{o_{g-1}+1}\right|\right) \\
& +\left(\left|x_{o_{g}}-a_{g}\right|+\left|y_{o_{g}}-b_{g}\right|\right) \\
& +\left(\left|a_{g}-x_{o_{g-1}+1}\right|+\left|b_{g}-y_{o_{g-1}+1}\right|\right) \\
& \forall g \in G
\end{aligned}
$$

Objective function (1) is to minimize the total cost, including average operating cost per shift and transportation cost of tow trains. Constraints from (2) to (4) indicate each supermarket is responsible for at least one station, and the supply area is no-overlapping. Constraint (5) ensures
that the utilization rate per supermarket is not lower than the expected utilization rate. Constraint (6) makes sure that the capacity of the supermarket is sufficient to meet the total demand of its responsible supply area. Considering driving lanes in assembly workshops are generally straight lines, the driving distance of tow train is calculated according to (7) by the Manhattan metric.

Since the SLP problem is an NP-complete problem, it is almost impossible to solve real-world scale problems by exact approach. Therefore, metaheuristic algorithms are needed to deal with the SLP problem.

## 3 DE/AEDA

As mentioned above, the EDA has been chosen as the main framework of the proposed optimization algorithm. The EDA is a novel type of group evolutionary algorithm and has been applied to solve many engineering optimization problems successfully in many fields. Unlike other meta heuristic algorithms, instead of generating new solutions by chromosome recombination, EDA describes the distribution information of candidate solutions in search space by establishing the probability model, based on which new solutions are sampled. It avoids the blindness and randomness caused by chromosome recombination, thus the search efficiency is effectively improved.

However, although EDA is good at global searching, it lacks the ability for refined search. Therefore, differential evolution (DE) strategy and adaptive learning rate mechanism are integrated into EDA to enhance the local search performance of algorithm, which is called the self-adaptive estimation of distribution algorithm with differential evolution strategy (DE/AEDA). The combination of EDA

algorithm and DE strategy can effectively promote the search ability of the algorithm. And the detailed descriptions of the proposed algorithm are presented as follows.

### 3.1 Encoding schemes

Encoding is the key step for EDA as it directly determines whether the probability model is appropriate or not. For the SLP problem studied in this paper, there are two encoding schemes as shown in Fig. 1.

Encoding scheme (a) is more applicable to algorithms that generate new individuals with crossover and mutation operators. It contains two sections-the first section (shaded) represents the last station served by each supermarket and the second section indicates the corresponding supermarket.

However, taking the characteristics of EDA algorithm into account, this paper applies (b) as the encoding scheme, under which the length of encoding stands for the total number of stations and each number here represents the supermarket which is in charge of the located station.

For example, as depicted in Fig. 1, there are 12 stations in total. Both schemes imply that stations $1-5$ are served by supermarket 1 . Stations 6-9 are served by supermarket 3 , and the rest are in the charge of supermarket 4.

For the SLP problem of $|S|$ stations and $|G|$ candidate supermarkets, if the individual is encoded as $\pi=\left(\pi_{1}, \pi_{2}, \ldots, \pi_{|S|}\right)$, then it has following properties:
$\left\{\begin{array}{ll}\pi_{s} \in G, & \forall s \in S \\ \pi_{s+1} \geq \pi_{s}, & \forall s=1,2, \ldots,|S|-1\end{array}\right.$

### 3.2 Population initialization

The quality of the initial population is crucial for the convergence of algorithms and the quality of solutions. If each individual gene is randomly selected from $1,2, \ldots,|G|$, then there may be illegal individuals. Consequently, according to the characteristic formula (8) of individual encoding scheme and given population size $N$, the following population initialization algorithm is designed:


(a) Encoding scheme for traditional EAs


(b) Encoding scheme for the EDA

Fig. 1 Encoding schemes for individuals

Step 1: Define station optional supermarket matrix as $\boldsymbol{\Omega}=\left(\omega_{i j}\right)_{|G| \times|S|}$, a $0-1$ matrix, where $\omega_{i j}=1$ indicates that the station $j$ can be assigned to the supermarket $i$.

Step 2: Let $k=1$.
Step 3: Make non-zero rows in the matrix $\boldsymbol{\Omega}$ as $\left(r_{1}, \ldots, r_{b}, \ldots, r_{B}\right)$, and let the first value which meets $\pi_{i}=$ $r_{1}$ be denoted as $i_{0}$, while the $k-\mathrm{th}$ gene of an individual is marked as row ${ }_{k}$. If $\sum_{s=i_{0}}^{k-1} d_{s}<\eta \cdot C$, that is, the supermarket utilization constraint has not been met, then row $_{k}=r_{1}$. While if $\sum_{s=i_{0}}^{k} d_{s}>C$, that is, capacities of supermarkets will be exceeded choosing $r_{1}$, then row $_{k}$ is a non-zero row randomly selected from $\left(r_{2}, \ldots, r_{B}\right)$; otherwise, row $_{k}$ is a non-zero row randomly selected from $\left(r_{1}, \ldots, r_{b}, \ldots, r_{B}\right)$.

Step 4: Set elements in row $\left(\right.$ row $\left._{k}-1\right)$ and column $k$ to zero.

Step 5: $k \leftarrow k+1$.
Step 6: Repeat Step 3-Step 5 until $\boldsymbol{\Omega}$ comes to be a zero matrix.

Repeat Step 2-Step 6 above for $N$ times to generate the initial population.

### 3.3 Probability model

The process of establishing the probability model plays a decisive role in designing the EDA. In this paper, $\mathbf{P}(\mathbf{g e n})$, a $|G| \times|S|$-dimensional probability matrix, is applied to demonstrate the probability model for distribution of the solution space:
$\mathbf{P}(\mathbf{g e n})=\left(\begin{array}{cccc}p_{11} & p_{12} & \cdots & p_{1|S|} \\ p_{21} & p_{22} & \cdots & p_{2|S|} \\ \cdots & \cdots & \cdots & \cdots \\ p_{|G| 1} & p_{|G| 2} & \cdots & p_{|G||S|}\end{array}\right)$
where $\mathbf{P}(\mathbf{g e n})$ is the probability matrix of the gen - th generation and $\left(p_{i j}\right)_{|G| \times|S|}$ stands for the probability that station $j$ is assigned to the supermarket $i$.

For the initial probability matrix $\mathbf{P}(\mathbf{0})$, the following uniform distribution is adopted to achieve the uniform sampling of the solution space:
$p_{i j}=\frac{1}{|G|}, \quad i \in G, j \in S$
In this paper, truncation selection method is used to select superior individuals. Select a number of SP individuals with smaller fitness values from the population, which is called SP population, where $\mathrm{SP}=\lfloor\gamma \cdot N\rfloor$ and $\gamma \in$ $(0,1)$ is the selection rate.

Then, calculate the frequency matrix $\mathbf{F}=\left(f_{i j}\right)_{|G| \times|S|}$ of SP population, where $f_{i j}$ represents the frequency that station $j$ is assigned to the supermarket $i$ in the SP population. Moreover, the average fitness values of $\overline{Z_{1}}$ and $\overline{Z_{2}}$ of the

current population and SP population are calculated. Finally, based on the current probability matrix $\mathbf{P}(\mathbf{g e n})$ and the frequency matrix $\mathbf{F}$, the probability matrix is updated, in each generation.

### 3.4 Self-adaptive updating mechanism of probability matrix

After $N$ new individuals are generated by sampling, a number of SP individuals are selected according to the fitness values to construct the dominant population. Then, the probability matrix is updated through the Hebb rule in machine learning incorporated with the adaptive strategy:
$\mathbf{P}(\mathbf{g e n}+\mathbf{1})=(1-\alpha) \cdot \mathbf{P}(\mathbf{g e n})+\alpha \cdot \mathbf{F}$
$\alpha=\alpha_{0} \cdot e^{\frac{-\alpha-\lambda}{m_{0} \cdot \beta_{1}}}$
The updating process is essentially an incremental learning process, where $\alpha$ is the incremental learning rate, $0<\alpha_{0}<1$ and $\alpha \leq \alpha_{\max }$, and $\alpha \cdot \mathbf{F}$ denotes the learning information obtained from the superior population. The updating formula of the probability matrix can adaptively adjust the learning rate in accordance with the fitness values in the population.

### 3.5 Sampling algorithm

If $\mathbf{P}(\mathbf{g e n})=\left(p_{i j}\right)_{|G| \times|S|}$ is the current probability matrix, based on Monte Carlo method, combined with the characteristics of the individual encoding in this paper, the sampling algorithm is constructed to obtain a new individual as follows:

Step 1: Let $\mathbf{W}=\mathbf{P}$. Then, select the $k$ - th column of matrix $\mathbf{W}$, and let $k=1$.

Step 2: A number of $|G|$ probability values of the $k$ - th column of the matrix $\mathbf{W}$ are accumulated in turn, and a number of $|G|$ cumulative probability values are thus obtained.

Step 3: $\kappa(0<\kappa \leq 1)$ is randomly generated, and if the $\lambda_{k}$ - th cumulative probability values is the one which is the smallest greater than $\kappa$, then the value of the $k$ - th gene is $\lambda_{k}$.

Step 4: Let the elements of matrix $\mathbf{W}$ be $w_{\lambda_{k}, k}=0$ and $w_{i j}=0\left(i<\lambda_{k}\right.$ and $\left.j>k\right)$. And then the original probability is proportionally compensated for other sampling elements so as to ensure the sum of probabilities of optional supermarkets in matrix $\mathbf{W}$ to be 1 during subsequent sampling process.

Step 5: $k \leftarrow k+1$.
Step 6: If $k \leq|S|$, then go to Step 2, otherwise the algorithm ends and a new individual is gained through sampling.

### 3.6 A novel discrete DE strategy

If the optimal solution to the population is not updated for $L$ consecutive generations in the AEDA algorithm, a novel discrete differential evolution strategy will be constructed for the sub-population with the fitness values ranking $\beta_{1} \sim \beta_{2}$ in the current population to avoid falling into local optimum.

The discrete DE operator specifically includes three types of operators: separation, combination and mutation. Given specific differential control parameters $0<\varphi_{1}<\varphi_{2}<1$, the discrete DE strategy is operated as follows:

Step 1: Random number $\kappa(0<\kappa \leq 1)$ is randomly generated.

Step 2: If $0<\kappa \leq \varphi_{1}$, separation operator is performed as shown in Fig. 2a; if $\varphi_{1}<\kappa \leq \varphi_{2}$, combination operator is conducted as shown in Fig. 2b; otherwise mutation operator is carried out as shown in Fig. 2c.
(a) Before separation
![img-0.jpeg](img-0.jpeg)

After separation
![img-1.jpeg](img-1.jpeg)

After combination
![img-2.jpeg](img-2.jpeg)
(c) Before mutation
![img-3.jpeg](img-3.jpeg)

After mutation
![img-4.jpeg](img-4.jpeg)

Fig. 2 Illustration of the novel discrete DE operators

Step 3: Metropolis acceptance criteria is applied to select individuals after carrying out the discrete DE strategy.

Step 4: End.

### 3.7 Overall procedure of DE/AEDA algorithm

Based on detailed descriptions in Sects. 3.1-3.6, the overall procedure of DE/AEDA algorithm proposed to solve the SLP is illustrated in Fig. 3.

## 4 Simulation and results

In this section, in order to analyze the performance of the proposed DE/AEDA, simulation experiments are carried out. All the algorithms are run on a personal PC with an Intel(R) Core(TM) i5-4200M CPU clocked at 2.50 GHz with 4 GB RAM. The codes are run on Matlab (2014a) platform.

### 4.1 Datasets

In order to verify the effectiveness of the DE/AEDA algorithm, the test examples $(|S|, \Gamma)$ are constructed as follows referring to Refs. [6, 14].
$|S| \in\{20,40,60,100,150,200\}$, the number of stations, in each case corresponds to 6 different supermarket configurations, and the average operating cost per shift in the supermarket is $\Gamma \in\{50,100,150,300,500\}$. Consequently, 24 test cases are constructed in total. The $y$-coordinates of each station and each candidate are set to $y_{s}=1, b_{g}=5$ respectively. While the supermarkets are randomly distributed among the stations, that is, $a_{g}=\operatorname{rand}(1,6 \cdot(|S|-1))$. And the distance between two consecutive stations is set to 6 , namely $x_{s+1}-x_{s}=6$, which guarantees the length of a car. The estimated demand for station $s$ per shift follows a uniform distribution $U(40,100)$.

### 4.2 Parameters setting

The main parameters of the proposed DE/AEDA algorithm include the population size $N$, the selection rate of SP population $r$ and the initial learning rate $\alpha_{0}$. A mediumscale test case $(60,150)$, is selected to implement design of experiments (DOE) to explore the influence of these parameters on the performance of the DE/AEDA algorithm.

Since each factor consists of four levels, the orthogonal array $L_{16}\left(4^{3}\right)$ is employed. The detailed configuration of these parameters and the orthogonal array are listed in

Tables 2 and 3 respectively. For each test case, the DE/ AEDA runs 20 times independently. The average result obtained by the DE/AEDA is selected as response variable, denoted as RV. The results are shown in Table 4. In addition, Fig. 4 depicts the trend of the parameters with different levels.

As shown in Table 3, the range of initial learning rate $\alpha_{0}$ ranks first, which indicates that $\alpha_{0}$ is the most significant parameter to the performance of the DE/AEDA, followed by the selection rate of SP population $r$, the last is population size $N$. It can be known from Fig. 4 that each parameter ought to be set reasonably. If $\alpha_{0}$ is too small, the updating of probability matrix is slowly, resulting in weakening global searching ability of the algorithm. On the contrary, if $\alpha_{0}$ is too big, the updating process will be rather rapid, leading to the lack of refined search process. As for the selection rate of SP population $r$, small $r$ will lead to premature convergence of the population, while the large one will make the population have a slow convergence. Although the population size $N$ has a minimal effect on the algorithm performance, it is still necessary to find a suitable value to achieve the optimal performance of the algorithm.

In summary, the configuration of parameters is set to $N=150, r=0.2$ and $\alpha_{0}=0.10$, which is a good choice to the proposed DE/AEDA.

### 4.3 Comparison experiment and analysis

Traditional evolutionary algorithms generate new candidates by chromosome recombination, including crossover and mutation operators. However, in the EDA algorithm, new solutions are sampled from the constructed probability model. In order to verify the performance of the proposed DE/AEDA, a benchmark algorithm named RGA (Real Genetic Algorithm) from Ref. [14] has been involved.

For each test case, each algorithm $a\left(a \in\{\mathrm{DE} / \mathrm{AEDA}, \mathrm{RGA}\}\right)$ will run 10 times independently. Then, statistical analysis is conducted to the results. The best value, the worst value and the calculated average value obtained in these runs by algorithm $a$ are denoted respectively as $T Z_{\mathrm{b}}(a), T Z_{\mathrm{w}}(a), T Z_{\mathrm{av}}(a)$. On this basis, the following variables are constructed:
$R T Z_{\mathrm{b}}(a)=T Z_{\mathrm{b}}(a) / T Z_{\mathrm{b}}(\mathrm{DE} / \mathrm{AEDA})$
$R T Z_{\mathrm{w}}(a)=T Z_{\mathrm{w}}(a) / T Z_{\mathrm{w}}(\mathrm{DE} / \mathrm{AEDA})$
$R T Z_{\mathrm{av}}(a)=T Z_{\mathrm{av}}(a) / T Z_{\mathrm{av}}(\mathrm{DE} / \mathrm{AEDA})$
which stands for the relative ratio of the result obtained by the algorithm $a$ to the best value of the DE/AEDA algorithm [33]. Since the results don't necessarily obey the normal distribution, then the Wilcoxon rank-sum test, which has been increasingly applied for the intelligent

![img-5.jpeg](img-5.jpeg)

Fig. 3 Flowchart of the DE/AEDA algorithm
computing research [34], is conducted to verify whether the performance of DE/AEDA algorithm is significantly superior to other algorithms.

Rank values $R$ are divided into positive values $R^{+}$and negative values $R^{-}$. Let $T^{+}$be the sum of ranks for positive values and $T^{-}$the sum of ranks for the opposite, namely $T^{+}=\sum R^{+}, \quad T^{-}=\sum R^{-}$. Then, $W=\min \left(T^{+}, T^{-}\right)$, the smaller of the sums is calculated, defined as the ranks-
related variable. The null hypothesis is that there is no statistical difference between DE/AEDA and RGA. Due to 10 independent runs for each algorithm, then $n=10$. When the null hypothesis can be rejected at the 0.05 level, the critical value under two-tailed test is $U=8$. Therefore, if $W<U$, it indicates that the performance of DE/AEDA is significantly superior to the other one. The difference between the worst value and the best value obtained in each

Table 2 Configuration of parameter values

Table 3 Orthogonal table and $R V$ values
Table 4 Statistical analysis of experimental results

test case denoted as $\Delta_{\mathrm{wb}}$, which is calculated by $\Delta_{\mathrm{wb}}=T Z_{\mathrm{w}}-T Z_{\mathrm{b}}$, can be regarded as an indicator to measure the stability of the algorithm.
![img-6.jpeg](img-6.jpeg)

Fig. 4 Factor level trend of the parameters
According to the statistical analysis results in Table 5, among the 24 test cases, there are 21 cases which demonstrate that the results obtained by the DE/AEDA are significantly better than those of RGA. Besides, it can be observed from Fig. 5 that the $\Delta_{\mathrm{wb}}$ values of DE/AEDA are mainly distributed within the interval $(6 \%, 10 \%)$, while the $\Delta_{\mathrm{wb}}$ values of RGA are mainly distributed within the interval $(7 \%, 17 \%)$. Therefore, it can be concluded that the DE/AEDA algorithm is more stable and robust than the RGA algorithm.

Consequently, the experimental results show that the performance of DE/AEDA algorithm is superior to that of RGA, resulting in solving SLP problem more effectively. The superiority of DE/AEDA algorithm mainly originates from two aspects: one is the application of the probability model which avoids the randomness and blindness caused by chromosome recombination, including crossover and mutation. The other is the random searching ability of the probability model and local optimization ability from the hybrid of the discrete DE operators.

### 4.4 Cost function and parameter analysis

Apart from the comparison experiments which are carried out in Sect. 4.3, the proposed DE/AEDA is compared with RGA by the objective function of SLP in this part. Table 6 shows the detailed results for all station counts, averaged over all 30 runs per station count S. All instances were tested with four different fixed cost values $\Gamma$, hence giving

Table 5 Comparison between DE/AEDA and RGA
![img-7.jpeg](img-7.jpeg)

Fig. 5 Stability comparison between DE/AEDA and RGA
monetary value to the basic trade-off of fixed cost and transportation cost. " $m$ " denotes the number of supermarkets in the resulting solution for the given station count and fixed cost, averaged over the 30 instances. " $F$ " denotes the total transportation cost, as calculated by the latter item in the objective function [Eq. (1)]. " $F$ " stands for the optimal SLP objective value, which exactly equals the total operation cost. And "CPU time" is the average time in seconds taken by the algorithm per instance.

Expectedly, the lower the fixed cost $\Gamma$ per supermarket, the more supermarkets are installed and the lower the corresponding SLP objective value $F$. This is, however, not true when fixed costs are very low and hence many supermarkets erected. This can be explained by the fact that every supermarket needs at least one vehicle stationed at it, which also entails fixed cost. At some point, the cost of adding another supermarket to an already large supermarket set is too high to be offset by the only marginally more transportation cost reduction it enables. This leads to a conclusion that even a small number of supermarkets is very efficient in supplying an assembly line, while too many logistics areas can quickly become counterproductive.

On a performance note, the propose DE/AEDA algorithm appears to run quite fast and seems adequate for problems of realistic size, as it could solve all instances in acceptable CPU time. Also, DE/AEDA has achieved a better performance on the objective function of SLP. In Table 6, optimal solutions are bolded and it can be seen that the propose DE/AEDA algorithm outperforms RGA in most cases (18 of 24 cases). Therefore, it can be concluded

Table 6 Cost function comparison between DE/AEDA and RGA
$\|S\|$ : number of stations; $\Gamma$ : average operating cost per shift; $m$ : number of supermarkets; $F^{*}$ : total transportation cost; $F$ : total cost (Objective function); CPU: average CPU time
that DE/AEDA is superior to RGA in obtaining better results.

### 4.5 Validation of the operators

In order to verify the validity of self-adaptive learning rate and DE operators, based on the control variable method, DE/ADEA is compared to AEDA and DE/EDA respectively. For each test case, each algorithm $a(a \in\{\mathrm{DE} / \mathrm{AEDA}, \mathrm{DE} / \mathrm{EDA}, \mathrm{AEDA}\})$ runs 10 times independently. The average computation time for obtaining the optimal solution is selected as setting time. In the end, the results are statistically analysed. The aforementioned non-parametric test method is also applied to analyze the results of each test case. Table 7 shows the statistical analysis values of the DE/EDA algorithm and the AEDA algorithm. It is obvious that among the 24 test cases, there are 22 cases showing that the results obtained by the DE/ AEDA are significantly better than that of DE/EDA. And for the AEDA algorithm, there are 21 cases in total. Thus, it illustrates the impact of self-adaptive learning rate and

DE operators on the performance of the algorithm and its effectiveness respectively.

From Figs. 6, 7 and 8, the distribution of the statistical results of 24 test cases in different metrics can be illustrated directly. As depicted in Fig. 6, the corresponding $R T Z_{0}$ value of the AEDA algorithm is larger than that of the other two algorithms, which indicates that DE operator has a stronger influence on refined search ability of the algorithm. Figure 7 depicts that the impact of self-adaptive learning rate is even greater in terms of the average performance. As can be seen from Fig. 8, there is no significant difference in the stability of the 3 algorithms, which can be referred to probability model of the EDA algorithm for statistical learning. As a result, self-adaptive learning rate and DE operators can help improve the performance of the EDA algorithm in different aspects.

Table 7 Statistical analysis of comparison among DE/EDA, AEDA and DE/AEDA algorithms
"\#" means "whether is significantly"
![img-8.jpeg](img-8.jpeg)

Fig. 6 Box plots of 24 test cases in $R T Z_{b}$ metric

## 5 Conclusions

In this paper, a novel EDA algorithm, named self-adaptive estimation of distribution algorithm with differential evolution strategy (DE/AEDA) is proposed to solve the discrete SLP problem with the consideration of the utilization rate and capacity constraint of the supermarkets
![img-9.jpeg](img-9.jpeg)

Fig. 7 Box plots of 24 test cases in $R T Z_{a v}$ metric
simultaneously. Unlike traditional evolutionary algorithms, instead of generating new solutions by chromosome recombination, in the EDA algorithm, new solutions are sampled from the constructed probability model, so EDA is good at global searching. Considering EDA lacks the ability for refined search, the DE strategy and adaptive learning rate mechanism are integrated into EDA. The

![img-10.jpeg](img-10.jpeg)

Fig. 8 Box plots of 24 test cases in $\Delta_{\mathrm{xb}}$ metric
Wilcoxon rank-sum test method is carried out to verify the performance of the proposed algorithm. From the comparisons of the results, it can be concluded that the performance of DE/AEDA is superior to that of other algorithms, resulting in solving SLP problem more effectively.

Finally, the supermarket location problem is of great practical significance and deserves deeper investigation in the future. First, it is supposed in this paper that supermarkets can be located anywhere on the assembly floor. However, if only very specific areas on the shop floor are available for construction of a supermarket, then discrete location planning approaches should be involved to solve the problem. Second, other objectives can be considered and factors to be optimized in multi-objective scenarios are to be studied in the location decision problem. For example, the effect of number of supermarkets on the safety stock can be useful in many lean manufacturing situations. Moreover, it is also of great managerial significance to involve the total weighted distance of the routes applied by respective supermarkets through all the stations and back. In case the same parts are used at multiple stations, it may be efficient to have these stations served by one supermarket. Considering their interdependencies with other corporate objectives, SLP problems will remain a fruitful field of research in the foreseeable future.

Acknowledgements This work was supported by the National Natural Science Foundation of China under Grant No. 71471135.

Funding The authors appreciate the supports to this research from the National Natural Science Foundation of China under Grant No. 71471135 .

## Compliance with ethical standards

Conflict of interest No potential conflict of interest was reported by the authors.
