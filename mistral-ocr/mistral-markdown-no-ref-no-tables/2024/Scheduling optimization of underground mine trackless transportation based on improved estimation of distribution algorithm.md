# Scheduling optimization of underground mine trackless transportation based on improved estimation of distribution algorithm 

Ning $\mathrm{Li}^{\mathrm{a}, \mathrm{b},{ }^{*}}$, Yahui $\mathrm{Wu}^{\mathrm{b}}$, Haiwang $\mathrm{Ye}^{\mathrm{a}, \mathrm{b}}$, Liguan Wang ${ }^{\mathrm{c}}$, Qizhou Wang ${ }^{\mathrm{a}, \mathrm{b}}$, Mingtao Jia ${ }^{\mathrm{c}}$<br>${ }^{a}$ Hubei Key Laboratory of Mineral Resources Processing and Environment, Wuhan University of Technology, Wuhan, Hubei 430070, China<br>${ }^{\mathrm{b}}$ School of Resource and Environment Engineering, Wuhan University of Technology, Wuhan, Hubei 430070, China<br>${ }^{c}$ School of Resource and Safety Engineering, Central South University, Changsha, Hunan 410083, China

## A R T I C L E I N F O

Keywords:
Underground mine
Trackless transportation
Estimation of distribution algorithm
O re blending scheme
Scheduling optimization

A B STR ACT

The trend in underground mine development is trackless transportation, and the scheduling optimization of underground mine trackless transportation is a current research hotspot. This paper proposes a truck scheduling optimization method for underground mine trackless transportation based on an improved estimation of distribution algorithm to address the truck scheduling problem in the underground mine trackless transportation process. The transportation process of transport trucks in underground mines is analyzed. The dispatching model of transport trucks in underground mines is constructed based on the requirements of reducing transportation costs and increasing transportation efficiencies, taking into account the truck meeting situation in the ramp section and minimizing the total shift transportation distance and the total waiting time of transport trucks as the objective functions. The improved estimation of distribution algorithm is used to solve the truck scheduling model, resulting in the optimal ore blending and scheduling schemes. The comparative analysis employs a genetic algorithm, particle swarm optimization algorithm, and immune algorithm. The results demonstrate that, compared to other algorithms, the improved estimation of distribution algorithm proposed in this paper has superior performance in terms of convergence speed and the search for the optimal solution. The total number of transportation tasks associated with the optimal ore allocation scheme is at least 82 , and the waiting time associated with the optimal scheduling scheme is reduced to 7.5 min . The operation time chart of transport trucks calculated by the optimal dispatching scheme can clearly depict the location of each transport truck at any time during a shift's working time, which has significant guiding significance for the actual truck transportation in the mine.

## 1. Introduction

With the continuous development and progress of human society, the demand for mineral resources continues to rise, causing the mining scale of underground mines to expand gradually and the number of mining equipment such as rock drilling, shoveling, and transportation to rise. Ore transportation, a key component of mine production, is responsible for the effective operation of underground ore and has a significant impact on the normal operation of mine mining, ore pass storage, surface dressing, and other processes. Currently, underground mine transportation mainly includes two modes, namely, electric locomotive transportation and trackless truck transportation. Due to its high efficiency, low cost, and high flexibility, trackless transportation is becoming increasingly popular in mines both domestically and
internationally (Zhao, Li, Li, Zhao, \& Liu, 2013). However, due to the mine's limited working space and discrete working area, improving the efficiency of the trackless equipment has become a significant issue for the current underground mine transportation operation. This has led to the development of a research hotspot for the underground mine trackless transportation operation system, namely the optimization of the truck scheduling. As a result, how reasonably planning the mine transportation operation path and optimizing the ore transportation scheduling plan is critical to ensuring the mine's green and efficient mining.

Currently, the mine's mining scale is expanding, and the increasing demand for ore transportation cannot be met solely by tramcar transportation. Increasing numbers of domestic and international mining companies are utilizing tramcars and trackless trucks for combined

[^0]
[^0]:    ${ }^{a}$ Corresponding author at: School of Resource and Environment Engineering, Wuhan University of Technology, Wuhan, Hubei 430070, China.
    E-mail addresses: 13875910191@163.com (N. Li), yehaiwang@sina.com (H. Ye), wqr@whut.edu.cn (Q. Wang).

![img-0.jpeg](img-0.jpeg)

Fig. 1. Underground mine trackless transportation system.
transportation. In the 1860s, the Kiruna Iron Mine in Sweden was the first to adopt trackless ramp development and the truck transportation system (Zong, 1976). Since then, several mines in Canada, the United States, and South Africa have adopted trackless transportation to increase the efficiency of mine transportation (Xia, 2011; Jiang \& Wang, 1997). After the 20th century, many domestic mines implemented ramp trackless transportation schemes to increase production capacity ( Li et al., 2021b; Sun, Wang, Hou, \& Zhang, 2020). Compared to tramcar transportation, trackless transportation has the advantages of flexibility, high speed, and high transportation efficiency. Additionally, its ore transportation through the ramp has lower excavation and transportation costs than the shaft, allowing mining enterprises to save investment and time. However, due to the unique transportation environment of underground mines, it remains challenging to maximize the transportation efficiency of trackless transportation. The ramp depicted in Fig. 1 of the underground mine trackless transportation system diagram is a turn-back ramp. Fig. 1 demonstrates that the transport truck must load ore at the pass of various mining sections, transport the ore to the surface ore storage bin for ore unloading through the same ramp, and then return to the pass from the ramp to continue loading ore. In this cyclical transportation procedure, all trucks must traverse the ramp, and the transportation operation points are scattered. The ramp of most mines is one-way, and the space for vehicle operation is restricted. The round-trip truck will meet at the ramp segment, disrupting the normal operation of the transport truck and decreasing the operational efficiency of the trackless transport truck. To maximize the benefits of underground mine transportation and improve the efficiency of truck transportation, it is necessary to optimize the scheduling scheme of the mine's trackless transportation system.

In light of the existing problems in the current mine trackless transportation system, this paper combines the actual working state of the transportation trucks in underground mines, considering the difference in the travel time of different trucks on different transportation sections and the meeting situation on the ramp section, introduced the truck travel time constraints, and built the transportation truck scheduling optimization model. In addition, the improved estimation of distribution algorithm is used to solve the model, providing a novel solution to the underground mine trackless transportation scheduling
problem.
The following sections are arranged as follows. Section 2 primarily introduces previous work in the field of mine transportation scheduling. The primary focus of Section 3 is the construction of an underground mine trackless transport scheduling model. Section 4 introduces the distributed estimation algorithm's principle and its enhancement. In Section 5, the efficiency and benefits of the distributed estimation model are discussed through specific cases. Section 6 concludes the paper.

## 2. Literature review

The optimization problem is an important branch of mathematics that arises from human labor production in real life. It mainly refers to the selection of a particular research scheme in order to attain the optimal goal under certain constraints. Many fundamental engineering issues in human society can be reduced to optimization problems, which encourages the study and development of optimization methods. With the continuous advancement of computer technology, more and more optimization algorithms have been proposed, allowing computers to solve increasingly complex optimization problems. In education (Precup, Hedrea, Roman, Petriu, Szedlak-Stinean, \& Bojan-Dragos, 2021), finance (Lin, 2022), and management (Tan, Ooi, Leong, \& Lin, 2014), among other fields, lead to optimization methods have been widely implemented. In addition, Singh (Singh \& Shukla, 2022) proposed an MMSE hybrid precoding algorithm that uses MMSE criteria to Manifold optimize MM wave massive MIMO communication signals, thereby enhancing signal spectral efficiency and energy efficiency. Bojan-Dragos (Bojan-Dragos, Precup, Preitl, Roman, Hedrea, \& Szedlak-Stinean, 2021) employed the grey Wolf optimization algorithm to design Takagi-Sugeno Type-1 and Type-2 fuzzy controllers, which improved the control performance of electromagnetic drive clutch systems affected by parameter uncertainty. Zamfirache (Zamfirache, Precup, Roman, \& Petriu, 2023) proposed a new reference tracking control method based on the Actor-Critic reinforcement learning framework and Grey Wolf optimization algorithm to optimize servo system control. With its powerful problem-solving ability, the intelligent optimization algorithm based on computer technology has been implemented in a variety of fields, including transportation truck scheduling optimization.

The truck scheduling issue is a variant of the job shop scheduling issue. As one of the earliest problems in production scheduling, job shop scheduling has been extensively studied and yielded abundant research results over the past decade (Gao, Suganthan, Chua, Chong, Cai, \& Pan, 2015). Shahzad (Shahzad \& Mebarki, 2012) proposed a prioritization scheduling method based on data mining that employs the tabu search algorithm to mine effective solutions provided by optimization modules in order to approximate the optimal scheduling scheme. Cheng (Cheng, Shiau, Huang, \& Lin, 2009) examined the dynamic interference in the field of job-shop scheduling and proposed a genetic algorithm-based dynamic real-time scheduling method to solve the problem of dynamic job-shop scheduling with resource and time constraints. Similar to how job shop scheduling is abstracted, transportation truck scheduling can be viewed as the solution of optimization problems with certain constraints. The essence of the transportation truck scheduling problem is to plan the optimal path between the origin and destination of the truck, subject to certain constraints, in order to achieve the objective of the lowest transportation cost or the highest transportation efficiency. The idea is to construct a scheduling model based on scheduling strategy, objective function, and constraints, and then to solve the scheduling model using an intelligent optimization algorithm in order to obtain the optimal scheduling scheme. Currently, most of the research on underground mine transportation scheduling focuses on all mobile equipment in all underground mine production links, and collaborative scheduling among mobile equipment has been resolved. The research scope is restricted to underground production sites.

Few studies have examined the scheduling of transportation equipment in the context of underground mine production scheduling. Gamache (Gamache, Grimard, \& Cohen, 2005) proposed the shortest path algorithm to solve the underground mine fleet management problem, taking into account underground traffic road constraints and vehicle operation constraints. Gamache (Gamache, 2006) proposed a dynamic programming-based enumeration algorithm to optimize the fleet management of underground mines, taking into account the bidirectional driving mode of underground mine transport trucks on the transport network. Nehring (Nehring, Topal, \& Knights, 2010) aimed at the short-term production scheduling and machine allocation of underground mines, introduced blasting blocks to control the ore grade constraint, proposed a solution method based on mixed integer programming, and accomplished the reasonable allocation of transport trucks and scrapers. Yardimci (Yardimci \& Karpuz, 2019) investigated the application of a genetic algorithm in determining the shortest path of an underground mine transportation road, providing a new scheme for the design of an underground mine transportation road. Similarly, Hou (Hou, Li, \& Hu, 2020) believe that the layout of underground mine roadways has a lasting effect on transportation and fuel costs. On this basis, a shortest path search algorithm to optimize roadway layout is proposed. An underground mine production scheduling optimization model is developed based on the optimized roadway network. Li (Li, Feng, Lei, Yu, Wang, Wang, \& Jia, 2022) established a transport equipment rescheduling model based on random simulation of equipment failure, considering that production equipment in underground mines frequently fails, and solved the model using an improved Wolf pack algorithm. Matamoros (Matamoros, \& Dimitrakopoulos, 2016) proposed a short-term mine production scheduling model based on stochastic integer programming. With total cost minimization as the objective function and production constraints and mining sequence constraints as constraints, the operation sequence of the fleet of underground mine transportation vehicles is optimized. Sun (Sun \& Lian, 2010) adopted an adaptive strategy to enhance the convergence rate of the ant colony algorithm in order to solve the transportation path optimization problem in underground mine production scheduling, and obtained satisfactory results by employing the improved ant colony algorithm.

Compared to previous research on optimizing the scheduling of a single underground mine transportation equipment, the current study
focuses more on the collaborative scheduling of all underground mine production mobile equipment. Max (Max, Mikael, \& Alessandro, 2018) proposed using constraint planning to schedule mobile devices in each link of underground mine production for the first time. Wang (Wang, Tenorio, Li, Hou, \& Hu, 2020) solved the scheduling optimization model built by a genetic algorithm to achieve the optimal working sequence of trackless equipment in the drilling, shoveling, and transportation processes. Max (Max, Mikael, \& Alessandro, 2020) proposed the underground mobile equipment scheduling based on constraint planning and large neighborhood search, considered the travel time of mobile equipment, and extended it to the constraints, resulting in a more comprehensive constraint model. Song (Song, Håkan, Mikael, \& John, 2015) designed a real-time schedule optimizer for mobile mining equipment in underground mines and implemented the optimal scheduling of mobile equipment using a grouping algorithm and a sorting algorithm to improve the efficiency of mining operations in underground mines. Hammami (Hammami, Jaoua, \& Layeb, 2021) evaluated the dependability of deterministic scheduling in a random environment by using the working time of the equipment as a random parameter in an equipment scheduling model. D O'Sullivan (D O'Sullivan \& Newman, 2015) developed a decomposition heuristic method based on optimization, which decomposes and simplifies the complex underground mine scheduling problem, and solves the optimal scheduling scheme with the goal of minimizing the amount of metal extracted within the mining range. Martinez (Martinez \& Newman, 2011) proposed a shortterm and short-term production scheduling optimization method based on mixed integer programming, developed a decomposition heuristic to decompose the long-term plan, and accelerated the solution speed of the Kiruna Mine's long-term production model. Fabián (Fabián, Javier, \& Nelson, 2020) considered the uncertainty in the production process of underground mines and proposed the use of a simulation optimization framework to generate short-term production scheduling and equipment scheduling schedules based on the scheduling plan, thereby enhancing the compliance of actual implementation to the scheduling plan. Huang (Huang, Li, Eugene, Bright, \& Hu, 2020) proposed incorporating the uncertainty of ore grade into the mine's production plan and developed an optimization model based on the stochastic mixed integer programming framework. Chen (Chen, Ding, Qin, \& Zhang, 2021) proposed an integrated genetic programming method based on super heuristics to solve the scheduling problem of random resource-constrained items. He constructed appropriate solution space through evolutionary priority rules. Li (Li et al., 2021a) first take the maximum total revenue as the objective function, solve the short-term production plan model of underground mines with the artificial bee colony algorithm, and then take the minimum total waiting time of equipment as the objective function, solve the equipment scheduling model with the non-dominant sorting genetic algorithm, and obtain the scheduling plan to guide the mine production operation.

For truck scheduling in underground mine trackless transportation, the primary objective is to solve the path optimization problem between the underground loading point and the surface unloading point of the truck in order to achieve the goal of completing the transportation task while minimizing the time and cost, which includes ore matching and grade requirements between the loading and unloading points. This kind of research on the optimization of transportation truck scheduling is relatively common in open-pit mines. Ahangaran (Ahangaran, Yasrebi, Wetherelt, \& Foster, 2012) realized that the transport fleet of most mines is composed of trucks with different transport capacities. On this basis, two methods of flow network and integer programming were utilized to develop a scheduling model suitable for trucks with varying capacities. Moradi-Afrapoli (Moradi-Afrapoli, Upadhyay, \& Askari-Nasab, 2021) incorporated the objectives of trucks, forklifts, and processing plants into the objective function and input parameter uncertainty into the solution program. They developed a model for truck scheduling using fuzzy linear programming. According to Alipour (Alipour, Khodaiari, Jafari, \& Tavakkolimoghaddam, 2022), the production scheduling of

![img-2.jpeg](img-2.jpeg)

Fig. 2. Schematic diagram of the underground trackless transportation route.
open-pit mines is significantly affected by price fluctuations of mineral products over time. They use stochastic differential equations to predict copper prices in different blocks of copper prices and guide production scheduling according to copper prices. Upadhyay (Upadhyay \& AskariNasab, 2016) proposed a mixed integer linear objective programming model to schedule trucks and shovels in open-pit mines based on the company's requirements for production cost, ore output, and ore grade. Samavati (Samavati, Essam, Micah, \& Sarker, 2018) proposed an adding cut technology to decompose the scheduling problem for large-scale open-pit mine production scheduling and used a local search heuristic to generate the optimal scheduling scheme. Moreno (Moreno, Rezakhah, Newman, \& Ferreira, 2017) considered spatial priority constraints and resource capacity constraints, took stock ore as part of the scheduling strategy, participated in the grade adjustment process for ore scheduling, and constructed an open-pit scheduling model based on linear integer programming. Mendes (Mendes, Flavio, Alves Maia, \& Rodrigues Veloso, 2016), He (He, Zhou, \& Nie, 2017), and Wang (Wang, Gong, Sun, \& Hu, 2022) all improved the genetic algorithm from different perspectives and then used the improved genetic algorithm to solve the optimization model of truck scheduling in open-pit mines. Khan (Khan \& Niemann-Delius, 2018) proposed a differential evolution-
based production scheduling method for open-pit mines under hierarchical uncertainty. They discussed the optimization performance of the differential evolution algorithm for open-pit mine production scheduling with and without uncertainty.

Most of the aforementioned studies on the scheduling of underground mining transportation equipment focus on all mobile equipment in all underground mining production links; this equipment primarily flows between underground stops and does not involve underground-tosurface operations. Most of the research on truck dispatching in open-pit mines employs mathematical programming, constructs the objective function and constraint conditions, and then solves the optimal dispatching scheme. This paper focuses on the link of underground mine trackless transport, the characteristics of transport trucks in underground mines, the similarities, and differences between their operation in underground mines and open pits, and the development of a scheduling optimization model appropriate for underground mine trackless transport trucks.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Schematic diagram of vehicle meeting on ramp section.

## Construction of truck transport model

### 3.1. Problem description

The transportation system for underground mines can be divided into rail transportation and trackless transportation. Trackless transportation is the cyclical process of loading ore in the underground pass, transporting it to the surface ore bin via the drift, ramp, and surface road, and then returning to the underground ore loading. The route diagram of the transportation truck between the pass and the ore bin is shown in Fig. 2. Generally, underground mines have multiple passes and ore bins. Due to the fact that mining companies have specific requirements for ore grade and output, the focus of current research and the purpose of developing an intelligent scheduling model is to determine how to complete transportation tasks at the lowest cost or in the shortest time while meeting the requirements for ore grade and output.

As shown in Fig. 2, the transport route of the transport truck in an underground mine is more restricted than that of an open-pit transport truck due to the constraints of the underground mine transport environment. In the underground mine, all transportation paths between the pass and the surface ore bin must utilize the same ramp segment. Since the underground ramp is a one-way line, when multiple trucks are operating concurrently, they will also meet at the slope section, and its traffic efficiency is significantly lower than the open pit mine. When two trucks meet at a slope road section, the mine must also establish meeting procedures. Underground mines are equipped with traffic signal devices to remind truck drivers on the slope road section that empty trucks must yield to loaded trucks and down trucks must yield to up trucks. At the sloped section of the road, a special stagger chamber is installed for downhill trucks to stop and avoid empty trucks. Fig. 3 is a schematic illustration of vehicles meeting at the slope road section. Complete the meeting in the order of (a) $\rightarrow(\mathrm{b}) \rightarrow(\mathrm{c}) \rightarrow(\mathrm{d})$.

Due to the existence of the truck meeting situation, as shown in Fig. 3, downward vehicles must wait for a certain time to pass during the meeting procedure. Compared with the waiting time during the loading and unloading process, the waiting time caused by the truck meeting situation is longer. In addition, the increase in the number of meeting times will have a negative impact on the overall efficiency of the trackless transport system, and a large amount of time will be lost in the process of meeting and waiting on the ramp section. Therefore, in the process of analyzing the trackless transport scheduling of underground mines, it is necessary to consider the meeting of transport trucks in the ramp section and reduce the waiting time caused by the meeting through a reasonable arrangement in order to improve the operation efficiency of transport trucks.

### 3.2. Dispatching mathematical model

To obtain the optimal solution to the scheduling problem, it is necessary to convert the complex actual scheduling problem into a mathematical model and then solve the mathematical model using the corresponding optimization algorithm. Generally, in order to successfully establish the mathematical model for scheduling, it is necessary to make the following assumptions about the problem:
(1) During shift hours, the transport truck operates continuously between the loading point and the unloading point, without any special circumstances.
(2) Ignore transport truck queues at loading and unloading points.
(3) The truck does not meet the level and surface sections, excluding the slope section.

To ensure the accuracy and timeliness of the scheduling scheme, the time range of the scheduling problem examined in this paper is the working time of an eight-hour shift, and the starting and ending points of the transportation truck are the ground surface. At the same time, to

Table 1
Variables used in the scheduling model.
Table 2
Parameters used by the scheduling model.
ensure that adjacent trucks maintain a safe distance during operation and to prevent congestion during shift handover. Before each truck begins working, the same interval is set, meaning that after the previous truck leaves, the next truck must leave at the same interval. In underground mining, transportation expenses account for a significant portion of total ore mining expenses. Therefore, when constructing the scheduling model, the cost of transportation operations should be considered first. Since the total transportation cost of a shift is related to the total transportation distance of a truck within a shift, the total transportation distance of a truck can reflect the total transportation cost of a shift. Second, in order to improve the traffic efficiency of transport trucks, the total waiting time of transport trucks must be minimized, i.e., the number of times that transport trucks meet on the ramp must be decreased. Therefore, this paper establishes two objective functions of the scheduling model: (1) minimize total shift transportation distance; (2) minimize total transport truck waiting time.

The scheduling model is solved in two steps. Firstly, the objective function is to minimize the total shift transportation distance, taking into account the constraints of the total shift transportation operation, the amount of ore at the loading point, the capacity of the unloading point, the grade requirement of the unloading point, the capacity of the transport truck, and other constraints. The ore allocation plan is solved, and the transportation task sequence of the transport truck, i.e., the number of times the transport truck must run on each path, is determined. Second, using the objective function of minimizing the total waiting time of transportation trucks and the constraints of shift working time, truck loading time, truck unloading time, truck travel time, etc., the transportation tasks are optimally sorted to obtain the optimal transportation task sequence, i.e., the final scheduling scheme. Table 1 displays the decision variables used in the scheduling model, while Table 2 displays the objective function and constraint parameters.

The first step in solving a scheduling model is to solve the scheduling plan for shift transportation and determine the transportation task sequence for the transportation truck. The objective function is to

![img-3.jpeg](img-3.jpeg)

Fig. 4. Comparison of the EDA algorithm and GA algorithm optimization process.
minimize the total distance traveled by all shifts, and its formula is as follows:
$n_{i j}=\left|\frac{x_{i j}}{C}\right|$
$\min f_{1}=\sum_{j=1}^{N S} \sum_{i=1}^{N S}\left(2 L_{i j} n_{i j}\right)$
where [.] is the upward rounding symbol; the decision variables are $x_{i j}$ and $n_{i j}$, and $n_{i j}$ is calculated using formula (1).

The constraints are:
$\sum_{j=1}^{N S} \sum_{i=1}^{N S} x_{i j} \geq D$
$\sum_{j=1}^{N S} x_{i j} \leq W L_{i}, i \in N L$
$\sum_{i=1}^{N S} x_{i j} \geq W S_{j}, j \in N S$
$P_{j}^{p c} \leq \frac{\sum_{j=1}^{N S}\left(p_{j} x_{i j}\right)}{\sum_{j=1}^{N S} k_{i j}} \leq P_{j}^{o p} . j \in N S$
Constraint (3) specifies that the total transport volume of the
transport truck cannot be less than the target ore volume of the shift transport, ensuring that the mine-specified transport task can be completed within the shift's working time. Constraint (4) ensures that the loading capacity of the transport truck at the loading point during shift working hours does not exceed the amount of ore stored at the loading point. Constraint (5) ensures that the amount of ore delivered to each unloading point during shift hours is within the target range. Constraint (6) controls the ore grade delivered to each unloading point within the required range and satisfies the ore processing plant's grade requirements.

The second step in solving the scheduling model is to determine the optimal transportation task sequence for the transportation truck by solving the scheduling scheme for the transportation truck. The objective function minimizes the total waiting time of transport trucks using the following formula:
$\min f_{2}=\sum_{i=1}^{K}\left(m_{k} T_{u}\right)$
where the decision variable $m_{k}$ represents the number of meets and waits for truck $k$ on the ramp section under the current transport task sequence, the value of which is affected by the sequence of trucking tasks. After determining the number of trucks, the no-load travel time of trucks, the heavy-load travel time, and the interval time between trucks.

On each transportation section, it is possible to calculate the operation time nodes of each transportation truck under the current transportation task sequence. MATLAB can be used to construct the transportation path simulation model, and the number of trucks meeting and waiting times for various transportation task sequences can be calculated. The total waiting time for the truck meeting can then be determined using a formula (7).
$\sum_{i=1}^{N S} \sum_{j=1}^{N S}\left(T_{i j} e_{i j}^{k}\right)+m_{k} T_{w}+(k-1) T_{f n} \leq T_{D}, k \in K$
$\sum_{k=1}^{K} e_{i j}^{k}=n_{i j}, i \in N L, J \in N S$
Constraint (8) ensures that the working time of each transport truck cannot exceed the working time of the shift. In the formula, the cycle transport time $T_{i j}$ of the transport truck between the loading point $i$ and the unloading point $j$ is calculated by the following formula:
$T_{i j}=T_{1}+T_{2}+T_{3}+T_{4}+T_{5}+T_{6}$
where $T_{1}$ represents the travel time of the drift section with loaded truck; $T_{2}$ indicates the travel time of the ramp section of the loaded truck; $T_{3}$ represents the travel time of the ground road section of the loaded truck; $T_{4}$ represents the travel time of the ground road section with empty truck; $T_{5}$ represents the travel time of the ramp section of the empty truck; $T_{6}$ represents the travel time of the drift section with empty truck. The travel time of the above six stages is predicted using a model based on the historical data of trucks (Li et al., 2023). This transportation truck travel time prediction model is one of the previous research works done by the author. Its main purpose is to provide basic data support for truck scheduling by predicting the travel time of transportation trucks on each transportation path.

Constraint (9) ensures that the number of transportation times between the unloading point and the loading point of the transport truck matches the result obtained in Step 1.

## 4. Method

### 4.1. Estimation of distribution algorithm

The Estimation of Distribution Algorithm (EDA) is a novel evolutionary algorithm developed on the basis of a probability model and genetic algorithm (Qu, Ji, Zhang, \& Wu, 2020). Its main idea is to combine a natural evolution algorithm with a constructive mathematical analysis method to guide the next search range of the algorithm by establishing a probability model for the currently found set of superior individuals, and calculating the probability distribution function of superior individuals. New individuals are sampled from the probability distribution function in order to generate a new population, reduce the search space for the optimal solution, and ultimately obtain the optimal solution (Zhang, Hu, \& Qian, 2021; Li \& Yang, 2021).

The optimization structure and solution steps of the estimation of distribution algorithm and genetic algorithm are similar. The genetic algorithm simulates the evolution of organisms by implementing crossover, mutation, and other genetic operations on individuals in the population, whereas the estimation of distribution algorithm establishes the probability distribution function of the dominant population and generates new individuals by sampling the probability model, thereby eliminating the vulnerable population. The optimization process of the two algorithms is shown in Fig. 4. The fundamental solution steps of the algorithm for distribution estimation are as follows:

Step 1. Initial population generation: determine the initial solution dimension and population size according to the problem. Then, randomly generate the initial solution in the search space to form the initial population.

Step 2: Fitness solution: construct a fitness function based on the actual problem, and solve the fitness value of each individual in the
initial population while maintaining the optimal solution at this time.
Step 3. Select the dominant population: determine the selection strategy, select the superior individuals based on their individual fitness value, and eliminate the inferior population.

Step 4. Establish a probability model: estimate the probability distribution model of the dominant group.

Step 5. Random sampling: use a certain sampling mechanism to sample the probability model to generate new individuals and update the population.

Step 6. Determine the termination conditions: Determine whether the current population meets the termination criteria by establishing the termination conditions. If this is the case, the optimal member of the current population represents the optimal solution to the problem. If not, return to Step 2 to continue the iteration.

In the above steps of the EDA, the most important steps are the selection of the dominant population (Step 3) and the construction of the probability distribution model of the dominant population (Step 4).

Among them, the conventional EDA selects the dominant population as a truncation strategy. For instance, in view of the minimization problem, assuming the population size is $N$ and the dominant population size is set to $M(N=2 M$ in general), the fitness of $N$ individuals in the population is calculated, the fitness is sorted as $f^{1}<f^{2}<\cdots<f^{M}<\cdots<f^{N}$, and the corresponding population individuals are $x^{1}, x^{2}, \ldots, x^{M}, \ldots, x^{N}$.

The probability distribution model of the dominant population is a crucial factor affecting the direction of population evolution. The Gaussian probability model is the classical probability distribution model of EDA. It constructs the probability distribution model by solving the mean and variance of the dominant population, and then generates new individuals and new populations randomly based on the probability distribution model for iteration. The specific model is shown in Eqs. (11) to (13).
$\mu_{t}=\frac{1}{M} \sum_{i=1}^{M} x_{i}^{t}$
$\sigma_{t}=\sqrt{\frac{1}{M} \sum_{i=1}^{M}\left(x_{i}^{t}-\mu_{t}\right)^{2}}$
$P\left(x_{t}\right)=\frac{1}{\sqrt{2 \pi} \sigma_{t}} e^{-\frac{\left(x_{t}-\mu_{t}\right)^{2}}{2 \pi^{2}}}$
where $x_{i}^{t}$ represents the individual in the dominant population at the $t$ th iteration, $\mu_{t}$ is the mean value, which constrains the center of the sample, and $\sigma_{t}$ represents the variance, which controls the diversity of the sample.

With the evolution of the population, $\mu_{t}$ and $\sigma_{t}$ are constantly updated. $\mu_{t}$ gradually approaches the position of the global optimal solution, and $\sigma_{t}$ will become smaller and smaller, so that the population will gather near the global optimal solution.

### 4.2. Improved estimation of distribution algorithm

The traditional estimation of distribution algorithm will encounter difficulties when solving the multi-objective scheduling optimization problem. For instance, in the process of selecting the dominant population, the update of individuals is dependent on the probability model constructed by the dominant population, the mutation probability of individuals is difficult, and the diversity of the population is low, resulting in the algorithm's easy convergence to the local optimum and diminished global search capability. In light of the problems present in the aforementioned algorithm for distribution estimation, the selection strategy and population update method of the algorithm are improved, as are the population diversity and the algorithm's ability to escape local optimization based on considering the optimization speed.

The traditional estimation of distribution algorithm employs

![img-4.jpeg](img-4.jpeg)

Fig. 5. Optimization process of the improved estimation of distribution algorithm.
classical truncation selection in the process of selecting the dominant population, i.e., sorting the fitness of individuals in the population and selecting the individuals with superior fitness to form the dominant population according to a certain proportion. In the dominant population, the importance of every individual is equivalent, regardless of fitness. This method of value averaging is not easy to converge the algorithm. As a result, a reinforcement selection strategy is proposed to strengthen its role by increasing the proportion of superior individuals in accordance with their fitness.

The first $M$ superior individuals are selected to form the dominant population, and the individuals are expressed as $x_{k}^{1}, x_{k}^{2}, \ldots, x_{k}^{M}$; The fitness of individuals is ranked from the current optimum to the next, expressed as: $f_{k}^{1}, f_{k}^{2}, \ldots, f_{k}^{M}$, for the minimization problem, $f_{k}^{1}<f_{k}^{2}<\cdots<f_{k}^{M}$. According to the fitness value, increase the proportion of the superior individuals and expand the capacity of the dominant population. Let the scale of the expanded dominant population be $N$, and the number of each superior individual is allocated by the following formula:
$F_{S}=\sum_{m=1}^{M} f_{k}^{m}$
$x_{k}^{1}: \frac{\left(1-\frac{\hat{D}}{F_{S}}\right) N}{\sum_{m=1}^{M}\left(1-\frac{\hat{D}}{F_{S}}\right)} ; x_{k}^{2}: \frac{\left(1-\frac{\hat{D}}{F_{S}}\right) N}{\sum_{m=1}^{M}\left(1-\frac{\hat{D}}{F_{S}}\right)} ; \ldots ; x_{k}^{M}: \frac{\left(1-\frac{\hat{D}}{F_{S}}\right) N}{\sum_{m=1}^{M}\left(1-\frac{\hat{D}}{F_{S}}\right)}$
where $\|\cdot\|$ is the upward rounding symbol.
In the dominant population generated by the enhanced selection, the proportion of superior individuals varies according to fitness. In the optimization calculation, the better individuals occupy a larger proportion, and the algorithm has a faster convergence rate. At the same time, to enhance the ability of the algorithm to jump out of the local optimum, the annealing mechanism of the simulated annealing algorithm is introduced to increase the diversity of the population, as follows.

For the dominant population, after enhanced selection, each member of the population is perturbed according to the following formula:
$y_{i}=T_{k} \operatorname{sign}\left(R-\frac{1}{2}\right)\left[\left(1+\frac{1}{T_{k}}\right)^{\|R-1\|}-1\right]$
$\dot{x}=x+\left(x_{\max }-x_{\min }\right) y_{i}$
where $R$ represents the random number between $\{-1,1\}$, and $T_{k}$ is the temperature under the current iteration. The decision to accept the new

Table 3
Transportation distance between each pass and surface ore bin (unit: km).
Table 4
Ore volume and ore grade of each pass.

solution is based on the Metropolis acceptance criterion, which involves calculating the difference $\Delta E$ between the fitness value of the new solution and the original solution. If $\Delta E \leq 0$, the new solution is accepted into the population. If $\Delta E>0$, the new solution is accepted with probability $P$, where $P=e^{-\Delta E / T}$.

Set the initial temperature as $T$, the temperature drop rate as $\lambda$, and the temperature drop formula is as follows:
$T=T \lambda$
According to the above formula, update the temperature to generate new species.

Based on the traditional estimation of distribution algorithm, the algorithm is updated using the reinforcement selection strategy and the annealing mechanism of the simulated annealing algorithm so that the algorithm can accept the worse solution with a certain probability, thereby increasing the population's diversity and size. The improved algorithm for distribution estimation not only takes into account the benefits of rapid convergence, but also greatly improves the algorithm's global optimization capability, making it more suitable for complex multi-objective optimization problems.

Write code according to the scheduling model built in section 3.2, and use the improved estimation of distribution algorithm to solve the model in two steps. The first step is to determine the optimal ore blending scheme with the objective function of minimizing the total distance of shift transportation. In step 2, based on the optimal ore blending scheme obtained in step 1, the optimal truck scheduling scheme is solved by minimizing the total truck waiting time as the objective function, and the optimal truck transportation task sequence is determined. Fig. 5 depicts the flow of the optimized scheduling model of the improved estimation of distribution algorithm.

## 5. Cases and discussions

### 5.1. Case analysis

The proposed scheduling model and solution algorithm are validated utilizing an underground mine as the engineering background. The annual ore mining volume of the mine is 2.16 million tons, and the ore is extracted by transport trucks, which are transported to the surface ore bin through the ramp through the underground ore drawing pass. The conversion reveals that the ore volume of the mine shift transportation task is 2400 tons and that the mine's transportation trucks have a load capacity of 30 tons. In the experimental section of the mine, there are two middle sections for truck-drawn ore transportation. Each section in the middle has two ore passes for ore extraction and two ore bins on the surface to receive ore transported by trucks. Additionally, the slope road section contains three stagger chambers, one of which is located between the two middle transportation sections. The transportation distance between each pass and the ore bin is shown in Table 3 in km.

Table 5
Target ore volume and target grade of surface ore bin.

Table 4 displays the ore quantity and ore grade for each pass. The target ore quantity and target grade of each surface ore bin are shown in Table 5.

### 5.2. Ore blending scheme

Step 1 of the scheduling model is to solve the ore allocation scheme, which is the ore transport allocation problem between the ore pass and the ore bin. Therefore, the individual in the initial population of the corresponding optimization algorithm is the ore amount allocated to each ore bin by each ore pass. However, during the generation of the initial population, it is necessary to test the randomly generated population members to determine if they satisfy the corresponding constraint conditions. Only when all individuals in the initial population satisfy the constraint conditions can the subsequent calculation step be performed. Similarly, an appeal test is required for new individuals generated by probabilistic models during the iterative process in order to guarantee that the optimal solution generated ultimately satisfies the constraint conditions.

Since the solution space of the ore allocation scheme optimization problem is continuous, a Gaussian distribution probability model is used to construct a probability distribution model by solving the mean and variance of the dominant population, and new individuals are generated at random to form a new population for iteration. The optimal solution is the ore quantity distributed between each ore pass and each ore bin, and the times of transportation between each ore pass and each ore bin can be calculated based on a single truck load.

Utilize MATLAB to compile the code based on the established mathematical model and the mine data listed above. Then, use the improved estimation of distribution algorithm proposed in this paper to solve step 1 of the scheduling model in order to obtain the optimal ore allocation plan for the mine during a shift, i.e., the number of times the transport truck must perform the transportation task between each pass and the surface ore bin. Secondly, use the genetic algorithm and particle swarm optimization algorithm to solve step 1 of the scheduling model. The results of the two algorithms and the improved estimation of distribution algorithm proposed in this paper are compared to demonstrate the scheduling optimization problem-solving advantages of the improved estimation of distribution algorithm.

The optimization parameters of the genetic algorithm, particle swarm optimization algorithm, and improved estimation of distribution algorithm are set as follows: the population number of the three algorithms is set to 20 , and the number of iterations is set to 100 ; the learning rate of the estimation of distribution algorithm is set to 0.1 ; the crossover probability and mutation probability of the genetic algorithm are set to 0.4 and 0.02 , respectively. Among the above parameters, the number of population iterations and the learning rate are obtained by performing a calculation check, and the above parameters are comprehensively selected based on their computational efficiency and convergence speed. The values of the genetic algorithm's cross probability and mutation probability have no obvious impact on the optimization procedure and can be appropriately changed. The steps of the scheduling model are solved by running the code of three algorithms in MATLAB software; the optimal ore blending scheme's data are displayed in Table 6, and the fitness curves of the three algorithms are displayed in Fig. 6. Table 7 shows the convergence degree of the three algorithms when they reach the optimal. The calculation method is the number of iterations at which each algorithm reaches the optimal divided by the total number of iterations, and is expressed in the form of percentage. Fig. 7.

Table 6
Optimal ore blending schemes calculated by the three algorithms.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Optimization fitness curve of three algorithms.

Table 7
The convergence degree of the three algorithms when they reach the optimal.


Fig. 7. Schematic diagram of the random ordering of transportation tasks.
Fig. 6 depicts the total distance traveled by trucks during a shift. In comparison to the improved estimation of distribution algorithm, the convergence speed of the genetic algorithm-based solution is faster and reaches the optimal level by the 14th iteration. As shown in Table 7, the
improved distribution estimation algorithm has a lower convergence rate than the genetic algorithm, which is $14 \%$. However, the optimal fitness of the genetic algorithm's solution is greater than that of the estimation of the distribution algorithm, indicating that the genetic algorithm reached only a local optimum and not a global optimum during the optimization process. In addition, the particle swarm optimization algorithm is relatively weak in terms of convergence speed and optimization performance, and its degree of convergence is $61 \%$, indicating that this method has disadvantages in solving the underground mine truck transportation scheduling problem. In contrast, the convergence speed of the improved estimation of the distribution algorithm proposed in this paper is slower than that of the genetic algorithm.

In order to verify the robustness and stability of the improved distribution estimation algorithm in the optimization process of ore allocation scheme, the improved distribution estimation algorithm was used to solve the ore allocation scheme for 5 times (including the results in Table 6), and the algorithm was statistically tested. The results of the 5 times of calculation were shown in Table 8. It can be seen from the data

Table 8
5 times calculation results of EDA.

Table 9
Optimal ore blending scheme (truck transportation times).
in the table that under the constraint conditions of ore quantity and grade, the results of the five calculations are very close, and the total transportation distance of the trucks is maintained at about 1370 km . Except for the result of the third, the total transportation times of the other results are 82 times. The above results show that the improved distribution estimation algorithm has strong robustness and stability, and can meet the requirements of mining enterprises for optimization results.

However, the final fitness value is lower, and it can be seen from Table 6 that under the assumption of meeting the shift transportation task volume and the ore grade goal, the improved estimation of distribution algorithm solves the ore blending scheme with a shorter total transportation distance and shorter transportation times. The result of the improved estimation of distribution algorithm is therefore selected as the optimal ore blending scheme. The number of times the transport truck must perform transport tasks between each pass and the surface ore bin is depicted in Table 9.

### 5.3. Truck dispatching scheme

The optimal ore allocation scheme determined in Section 5.2 is the number of transport tasks between each ore pass and surface ore bin that transport trucks must complete during a shift. The next step is to identify the transport task sequence that requires the shortest total time, i.e., the transport task sequence that corresponds to the fewest number of truck meetings on the slope road section during a shift. Table 6 shows that the total number of transportations corresponding to the optimal ore allocation scheme is 82 . According to the calculation of the total transportation time of trucks, a minimum of ten trucks are required to complete 82 transportation tasks.

The optimal scheduling scheme, consisting of the classification of 82 transportation tasks, has been resolved. The scheduling scheme that results in the fewest number of trucks meeting on a sloped road segment is the optimal one. Therefore, the initial population individual corresponding to the optimization algorithm is the sorting of transportation tasks, and the 82 transportation tasks are sorted at random as follows:

Where $Q_{i}$ denotes the transport task number placed at the $i$ th position in the solution sequence. Then, the sorted task is assigned to ten trucks in the following way:
![img-6.jpeg](img-6.jpeg)

In the process of generating new individuals, it is necessary to ensure that the time required by each transport truck to complete the transportation task does not exceed the shift working time ( 8 h ); if it does, the generation of new individuals is repeated until all individuals in the initial population satisfy the shift working time constraint.

Objective function calculation: determine the time node for each
![img-7.jpeg](img-7.jpeg)

Fig. 8. Relationship between the total number of meetings and interval time.
truck to complete each transportation task according to the assigned transportation task, as well as the time period of each truck on the ramp and down the ramp during the shift time. Then, the total number of meeting vehicles can be determined by counting the number of times each truck overlapped during the ramp time period. If the time period of truck 1 going down the ramp coincides once with the time period of truck 2 going down the ramp, then the total number of meeting vehicles on the ramp road section can be calculated.

Since the scheduling scheme is intended to solve the sorting optimization problem in the discrete solution space, the probability distribution model of the dominant population is constructed by constructing the probability matrix. Let $P(t)$ be the probability matrix of $n \times n(n=$ 82), as follows:
$P(t)=\left[\begin{array}{cccc}\rho_{11}(t) & \rho_{12}(t) \cdots & \rho_{1 n}(t) \\ \rho_{21}(t) & \rho_{22}(t) \cdots & \rho_{2 n}(t) \\ \vdots & \vdots & \vdots \\ \rho_{n t}(t) & \rho_{n 2}(t) \cdots & \rho_{n n}(t)\end{array}\right]$
where element $\rho_{i j}(t)$ represents the probability that the transport task $j$ appears on the $i$ bit of the solution sequence in the $t$ iteration, and this value represents the priority of the transport task being executed. At the initial stage, to ensure uniform sampling of the solution space, the probability of elements in the probability matrix is uniformly distributed, i.e., the probability values of all elements are $1 / n$.

### 5.3.1. Impact of interval time on the number of train meetings

In step 2 of the scheduling model, the objective function is to minimize the total waiting time of transport trucks during a shift, which is the product of the number of times all transport trucks meet during a shift and the waiting time of a single truck meeting. Therefore, the total number of meeting times of transport trucks can represent the total waiting time of trucks. The total number of meeting times is selected as an indicator for analyzing the effects of varying truck departure intervals on the total waiting time of transport trucks. The total number of meeting times of transport trucks has a great relationship with the traffic density of the entire transport path. The greater the traffic density, the greater the likelihood of transport trucks meeting on a sloped road segment. The corresponding number of meeting times and waiting times will also increase, as will the decrease in transport efficiency. The road's traffic density is related to the number and interval time between trucks. The number of trucks is determined by the number of transportation tasks. In the case presented in Section 5.1, there are at least ten trucks. Increasing the number of trucks will increase costs, which is contrary to the purpose of this paper, which is to reduce transportation costs. Consequently, the number of trucks is essentially fixed, while the interval time between trucks is variable. By varying the interval time between trucks, the effect of interval time on the total number of truck meeting times corresponding to the optimal scheme is analyzed. The

![img-8.jpeg](img-8.jpeg)

Fig. 9. No-load and heavy-load travel time of each truck on the path.
method proposed by Li et al. (Li, Wu, Wang, Ye, Wang, Jia, \& Zhao, 2023) is used to predict the no-load and heavy-load travel times of ten trucks, and the corresponding truck travel times are shown in Fig. 8. The interval time is adjusted from one minute to 15 min , and the intermediate adjustment interval is one minute. Fig. 8 depicts the results of calculating the total number of meetings corresponding to the optimal scheduling scheme using the estimation of distribution algorithm.

In general, the relationship between the total number of meetings corresponding to the optimal scheme and the interval time decreases and then increases, as shown in Fig. 8. A lengthy interval time will also reduce the efficiency of transport. However, too short an interval time will result in inadequate safety distance between vehicles and increase the likelihood that transport trucks will need to queue at the pass and ore bin. As shown in Fig. 8, set the interval to three minutes and employ the estimation of distribution algorithm to determine the optimal scheduling scheme's minimum number of meeting times. Therefore, three
minutes is the optimal interval time for the transportation truck to begin running.

### 5.3.2. Truck travel time prediction

The optimal ore blending scheme determined in Section 5.2 is the number of transportation tasks the transport trucks must complete between each pass and the surface ore bin during a shift. The next step is to identify the transportation task sequence that requires the least total waiting time, which corresponds to the fewest number of times that all transport trucks meet in the ramp section during a shift. The optimal transportation task sequence is solved based on the objective function and constraint conditions shown in step 2 of the scheduling model in section 3.2. According to the accounting, at least ten trucks can operate concurrently in a single shift of the mine in order to complete the transportation task for the shift. The no-load and heavy-load travel time of trucks required in the process of solving the dispatching scheme

![img-9.jpeg](img-9.jpeg)

Fig. 9. (continued).
![img-10.jpeg](img-10.jpeg)

Fig. 10. Fitness curves of four algorithms.
presented in this paper is predicted by the method provided in another paper (Li et al., 2023), by the same author, and the details are shown in this paper. The travel time prediction method of transport trucks in this paper is utilized to predict the unloaded and loaded travel time of ten trucks. The no-load travel time and heavy-load travel time of transport trucks between the pass and the surface ore bin are shown in Fig. 9. Both the loading and unloading times for the transport truck have been set to one minute. According to the calculation results in Section 5.3, the interval between trucks to start running is set to three minutes. The
waiting time for the downhill trucks to meet is set to 2.5 min .

### 5.3.3. Optimal truck scheduling scheme

Use MATLAB to write the code for step 2 of the scheduling model, solve the model with the improved estimation of distribution algorithm proposed in this paper, and determine the optimal scheduling scheme. At the same time, genetic algorithm (GA), particle swarm optimization (PSO), and artificial immune algorithm (IA) are selected for comparative verification. Due to the complexity of the scheduling scheme and the

Table 10
The number of meeting times corresponding to the optimal solution of each algorithm.
Table 11
The convergence degree of the three algorithms when they reach the optimal.

Table 12
The truck transportation task sequence corresponding to the optimal plan.

discreteness of the solution space, finding the optimal solution in the solution space requires a larger population size and iteration times. Experimentally, the population size of the four algorithms is set to 50, and the number of iterations is set to 1000 . Refer to Step 1 to set other algorithm parameters and adjust them accordingly. Fig. 10 depicts the fitness curves calculated by the final four algorithms. Table 10 displays the number of meeting times calculated by the four algorithms for the
optimal ore blending scheme. Like the ore blending scheme calculated in Section 5.2, the convergence of the four algorithms, when they reach the optimum, is shown in Table 11.

Fig. 10 demonstrates that by using an optimization algorithm to arrange the transportation task sequence in a reasonable manner, the waiting time of the transportation trucks during the entire shift working time is drastically reduced due to truck meetings, indicating that the transportation task sequence has a significant impact on the final truck meeting times. In addition, the improved estimation of distribution algorithm proposed in this paper has the smallest final fitness in the process of solving the scheduling scheme. Nevertheless, genetic algorithm (GA), particle swarm optimization (PSO), and immune algorithm (IA) are susceptible to local optimum and fail to converge to a global optimum. Although the convergence degree of the improved estimation of the distribution algorithm shown in Table 11 is relatively high, the optimization problem focuses on the ability to seek optimal solutions. On the basis of preserving the optimization capability, accelerating the convergence rate of the algorithm is also a direction for future improvement. The improved estimation of distribution algorithm shown in Table 10 has a minimum number of times of trucks meeting, and the total waiting time for trucks meeting within a shift working time is 7.5 min . Table 12 depicts the sequence of transportation tasks for each truck in the optimal scheduling scheme.

Note: Each transportation task of the truck in the table (such as 1-1, $1-2$, etc.) represents the round-trip process of the truck from the surface empty truck to the ore pass loading and then to the surface ore bin unloading.

According to the truck transportation task sequence shown in Table 12, as well as the no-load and heavy-load travel time between the transportation routes, the loading and unloading time of the transport trucks, the interval time between the trucks, and the waiting time for the
![img-11.jpeg](img-11.jpeg)

Fig. 11. Truck 1 travel schedule under the optimal dispatching scheme.

![img-12.jpeg](img-12.jpeg)

Fig. 12. Travel schedule of each truck under the optimal dispatching scheme.
meeting, we can calculate the travel time diagram of each transport truck during the working time of a shift, with the ground surface as the starting point for each truck. Taking a shift from 8:00 to 16:00 as an example, the calculated travel time diagram of No. 1 transport truck is shown in Fig. 11.

As shown in Fig. 11, the partially enlarged view on the right depicts the unloading time of the first truck during the transportation task. The waiting time at the ramp section of the road and the loading time from top to bottom. Fig. 11 illustrates that during the third transportation task, truck 1 met the empty car on the downhill road segment and waited 2.5 min in the stagger chamber. The precise time range was 10:03:54 to 10:06:24. Similarly, the travel time diagram of other trucks is calculated according to the transportation task sequence of each truck, as shown in Fig. 12.

According to Figs. 11 and 12, truck 1, truck 6, and truck 8 must avoid waiting in the stagger chamber under the optimal dispatching scheme. By optimizing the scheduling scheme of transport trucks, the number of truck meeting events in the entire transport fleet has been significantly reduced, and the transport efficiency of trucks has been substantially
improved. At the same time, based on Figs. 11 and 12, the position of each transport truck during any time period can be determined, as well as the time period during which the transport trucks will meet according to this scheduling scheme. It is crucial for the preparation of mine transportation plans and the direction of actual mine production.

## 6. Conclusion

An intelligent underground mine dispatching system is an essential component of intelligent mine construction. This paper proposes an optimized method of underground mine trackless transportation truck scheduling based on an improved estimation of distribution algorithm in an attempt to solve the problem of truck dispatching in underground mine trackless transportation. The main conclusions are as follows:
(1) Considering the meeting situation of the truck in the ramp stage, with the objective of minimizing the total transport distance of a shift and the total waiting time of the transport truck, and considering the ore quantity constraints, ore grade constraints,

![img-13.jpeg](img-13.jpeg)
(g) Truck 8
(h) Truck 9
![img-14.jpeg](img-14.jpeg)
(i) Truck 10

Fig. 12. (continued).
and truck travel time constraints, a mathematical model of the transport truck scheduling in an underground mine is developed.
(2) The improved estimation of distribution algorithm is used to solve the truck scheduling model step by step. Firstly, the optimal ore blending scheme is determined based on the objective function of minimizing the shift's total transportation distance. Secondly, in accordance with the optimal ore blending scheme, the optimal scheduling scheme, i.e., the optimal truck transportation task sequence, is obtained by minimizing the total truck waiting time as the objective function. In comparison to other algorithms, the improved estimation of distribution algorithm yields the best result, with a waiting time of 7.5 min corresponding to the scheduling scheme it generates. It demonstrates that the implementation of this scheduling scheme can prevent traffic meetings on the ramp segment and significantly improve the efficiency of truck transportation.
(3) The travel time diagram for each transport truck can be calculated based on the optimal scheduling scheme obtained by the improved estimation of distribution algorithm. According to the diagram, the position of each transport truck at any given time can be determined, which has significant guiding significance for the mine's actual truck transportation.

# CRediT authorship contribution statement 

Ning Li: Funding acquisition, Conceptualization, Methodology, Software, Data curation, Visualization, Writing - original draft. Yahui Wu: Formal analysis, Validation, Writing - review \& editing. Haiwang Ye: Resources, Writing - review \& editing. Liguan Wang: Funding acquisition, Methodology. Qizhou Wang: Data curation, Resources. Mingtao Jia: Funding acquisition, Investigation.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This research was supported by the National Natural Science Foundation of China (Grant No. 42271296), Major Scientific and Technological Innovation Plan of Hubei Province (Grant No. 2023BEB040), and National Key Research and Development Program of China (Grant No. 2019YFC0605304).
