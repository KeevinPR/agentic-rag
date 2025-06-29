# Traffic Signal Optimization with Estimation of Distribution Algorithms and VISSIM-MATLAB Integrated Simulation Platform 

Yongsheng Liang<br>School of Automation Science and Engineering<br>Xi'an Jiaotong University<br>Xi'an, China<br>liangyongsheng@stu.xjtu.edu.cn<br>Zhigang Ren*<br>School of Automation Science and Engineering<br>Xi'an Jiaotong University<br>Xi'an, China<br>renzg@xjtu.edu.cn<br>An Chen<br>School of Automation Science and Engineering<br>Xi'an Jiaotong University<br>Xi'an, China<br>chenan123@stu.xjtu.edu.cn<br>Daofu Guo<br>School of Automation Science and Engineering<br>Xi'an Jiaotong University<br>Xi'an, China<br>gdf19951205@stu.xjtu.edu.cn

Abstract-Traffic signal optimization plays a crucial role in improving the service ability of traffic networks in urban areas. With the traffic network getting more and more complex, there have been increasing research interests in employing intelligent algorithms to find proper settings for traffic signals. As a special type of evolutionary algorithms, estimation of distribution algorithms (EDAs) possess strong optimization ability but have seldom been used in traffic signal optimization. In this paper, two efficient variants of continuous EDAs, namely EDA with variance enlargement strategy (EDA $_{w}$ ) and EDA with variablewidth histogram model (EDA-VWH), are modified and adopted as optimizers to find proper traffic signal cycles in an actual urban area with multiple intersections. The performances of the two resultant algorithms, i.e. modified EDAve ( $\mathrm{mEDA}_{w}$ ) and modified EDA-VWH (mEDA-VWH), are comprehensively studied through a VISSIM-MATLAB integrated simulation platform, which could provide a convenient and close-to-reality simulation environment. The simulation results showed that $\mathrm{mEDA}_{w}$ and mEDA-VWH could effectively reduce the mean delay time of all vehicles under different traffic conditions. In comparison with four other algorithms, including genetic algorithm, particle swarm optimization, differential evolution and random search method, the two modified EDAs also achieved competitive results.

Keywords-urban traffic network, traffic signal optimization, estimation of distribution algorithms, VISSIM

## I. INTRODUCTION

With the rapid development of modern society, there are increasing number of vehicles in the urban areas around the world. Traffic congestion is occurring every day in most cities and becomes an important factor in limiting the growth of economy. A reasonable setting of traffic signals can be very helpful in improving the traffic flow and reducing the delay time of vehicles $[1,2]$.

[^0]As a vital part of the city infrastructure, traffic lights are installed in nearly every intersection and are operating round-the-clock to maintain the traffic order. It is generally not viable to frequently update the traffic lights due to multifaceted reasons, such as the economic and environmental issues. Therefore, many traffic agencies and researchers pay close attention to optimize the existing traffic lights to exploit their potential best service capability [3]. Over the past decades, considerable research efforts have been devoted in traffic signal optimization, which mainly focus on developing accurate traffic simulators [4-8] and finding suitable traffic signal programs with optimization algorithms [9-12].

Since it is impracticable to validate the effectiveness of a specific signal program in real traffic networks, the necessity of developing accurate traffic model for simulation is indubitable. Various representative traffic models have been proposed to describe the traffic flow from different point of views, such as the cellular automaton model [5], the gaskinetic model [6] and the continuous model [7]. Although these models have been successfully applied in different situations, they still have some limitations and cannot provide comprehensive information of the traffic flow. In addition to these mathematical models, some modern software developed by companies or universities was also widely adopted as powerful tools in simulating and analyzing a variety of traffic problems. VISSIM is famous software for traffic simulation and offers flexible analysis functions [8]. It provides a friendly graphical interface for users to design any type of traffic networks and set up the simulation environment. Moreover, it can communicate with other programming software like MATLAB through the component object model (COM) module, which is very convenient for users to develop and validate their traffic signal control strategies.

Based on a traffic simulator, different methods can be employed to find suitable traffic signal programs for a given traffic network. Nonetheless, as the traffic network becomes more complex and the number of traffic lights grows, it is a challenging task to find the optimal setting of traffic signals due to the enormous number of combinations, which


[^0]:    * Corresponding author: Zhigang Ren (renzg@xjtu.edu.cn).

    Research supported in part by the National Natural Science Foundation of China under Grant 61873199, and in part by the Natural Science Basic Research Plan in Shaanxi Province of China under Grant 2020JM-059, and in part by the Fundamental Research Funds for the Central Universities under Grant xzy022019028.

motivated the use of intelligent algorithms in traffic signal optimization. As an active research branch of artificial intelligence, evolutionary algorithms (EAs) have been widely used to solve a broad array of optimization problems consisted in different domains. And there are increasing research interests in employing EAs to find high-quality solutions for traffic signal optimization problems in recent years [9-12]. For example, Sánchez-Medina et al. [3] suggested using a genetic algorithm (GA) to optimize the setting of traffic signals to reduce congestion in a set of different scenarios. Garcia-Nieto et al. [10] utilized a particle swarm optimizer (PSO) to find proper signal cycles with the aim of maximizing the number of vehicles that reach their destination and achieved satisfying optimization results in two large cities with different styles. Similarly, Hu et al. [11] attempted to reduce the total delay time and total parking number of vehicles with a quantumbehaved PSO. Recently, Gao et al. [12] employed a Jaya algorithm, a harmony search algorithm and a water cycle algorithm, respectively, to minimize the total delay time of all vehicles in a set of large scale traffic networks and showed that the three algorithms are helpful to improve the traffic efficiency. Besides the above algorithms, estimation of distribution algorithms (EDAs) [13-15] are also powerful algorithms with strong optimization ability, but have seldom been used in traffic signal optimization. To the best of our knowledge, only one related work was reported by Zhang et al. [16], who suggested adjusting the traffic signal cycle time of a single intersection with two basic EDAs. Their experimental results demonstrated that the two EDAs can effectively reduce the delay time of vehicles and perform better than a traditional GA. However, the optimization performance of EDAs in traffic networks with multiple intersections has neither been discussed nor tested.

The successful applications of many other EAs and the under-researched performance of EDAs in real traffic networks prompt us to introduce new and efficient EDAs into traffic signal optimization to provide new solutions for traffic systems. In this paper, two variants of continuous EDAs, namely EDA with variance enlargement strategy $\left(\mathrm{EDA}_{v e}\right)[14]$ and EDA with variable-width histogram model (EDA-VWH) [15], are adopted as optimizers to find proper traffic signal cycles in an actual urban area with multiple intersections. Since the two EDAs were originally designed for solving continuous optimization problems, we first modified them to make them suitable for solving traffic signal optimization problems and developed two modified algorithms, namely modified $\mathrm{EDA}_{v e}\left(\mathrm{mEDA}_{v e}\right)$ and modified EDA-VWH (mEDA-VWH). Then a VISSIM-MATLAB integrated simulation platform was realized to test the performance of the two modified EDAs. In this simulation platform, a regional traffic network with 11 intersections in Xi'an, China was realized in VISSIM, which works as a simulator to evaluate the solutions generated by the two modified EDAs implemented in MATLAB. The performances of $\mathrm{mEDA}_{v e}$ and mEDA-VWH were analyzed under different conditions of traffic volumes and the simulation results demonstrated that they could effectively reduce the total delay time of all vehicles. Comparison with several algorithms, including a GA [17], a PSO [18], a differential evolution (DE) [19] and a random search method [10], further verified the superiority of EDAs in traffic signal optimization.

The remainder of this paper is organized as follows. In Section II, the VISSM-MATLAB integrated simulation platform is introduced. In Section III, the modified $\mathrm{EDA}_{v e}$ and EDA-VWH are described in detail. Section IV presents the experimental setup and reports the simulation results along with some analyses. Conclusions and future work are given in Section V.

## II. VISSIM-MATLAB INTEGRATED SIMULATION PLATFORM

Traffic simulators are widely used to model and analyze different traffic dynamics of real traffic networks. They are highly effective tools in assisting design of new traffic control strategies. In the traffic signal optimization process, every potential solution would be evaluated by a traffic simulator before it could be put into practical application.

VISSIM is a famous microscopic simulator and has always been a popular software in diverse research areas related to traffic. It consists of two main parts including the traffic simulator and the signal state generator. The task of the traffic simulator is to model the vehicle behavior, e.g. the code of conducts of running vehicles in a given traffic network. In order to achieve accurate simulation result, VISSIM employs a calibrated psycho-physical driver model [20] to assign specific behavior characteristics to every vehicle. The signal state generator works as a signal controller and determines the statuses of all signal lights for the next simulation step. Moreover, VISSIM also offers comprehensive evaluation functionalities, which could collect and evaluate many types of information, such as vehicle delay time and density, generated during the simulation. These data can be very helpful in reflecting the status of a given traffic network.

VISSIM provides a friendly graphical interface for users to design traffic network and set up the simulation environment, which is however sometimes still unsatisfying. For instance, it is inconvenient to automatically adjust the cycles of traffic signals in VISSIM and thus is less efficient in verifying the performances of multiple potential solutions. Fortunately, VISSIM integrates an additional COM module which allows users to access and manipulate VISSIM with external programming tools. Through the COM interface, the simulation configurations and the internal parameters originally defined by the graphical interface can be handily controlled by scripts written in MATLAB, JAVA, C++, etc. Among them, MATLAB is a popular tool to design intelligent algorithms and possesses flexible data processing ability. Based on the considerations above, a VISSIM-MATLAB integrated simulation platform is realized for traffic signal optimization, which can be described by Fig. 1. In this simulation platform, VISSIM is used to design the traffic network and configure the simulation environment. And then it receives new solutions, i.e. traffic signal cycles, generated by the algorithms implemented in MATLAB and produces the corresponding simulation results. These simulation results obtained in VISSIM, working as optimization criterion, will be transferred back to MATLAB to guide the optimization process.

By taking advantage of the VISSIM-MATLAB integrated simulation platform, on the one hand, we can achieve accurate simulation results in VISSIM and verify the effectiveness of a candidate solution in high efficiency. On the other hand, sorts

![img-0.jpeg](img-0.jpeg)

Fig. 1. VISSIM-MATLAB integrated simulation platform.
of optimization algorithms can be designed in MATLAB to explore better solutions for a traffic network. The integrated simulation platform has a wide range of applications in different traffic situations, and provides a convenient and economic tool for traffic signal optimization.

## III. APPROACHES

In this section, the details of our approaches for traffic signal optimization are presented. Firstly, the solution encoding and the optimization criterion are described. Then the modified $\mathrm{EDA}_{r e}$ and EDA-VWH are introduced for finding high-quality solutions for the traffic signal optimization problem.

## A. Solution Encoding

In many traffic networks, traffic lights are designated with fixed signal cycles over a period of time and they simultaneously perform their own cycles repeatedly to control the flow of all vehicles. The traffic lights located in the same intersection are harmoniously ruled by a common signal cycle. A signal cycle is a sequence of basic signal phases, where each phase has a separate duration time and indicates the color states of all signal lights allowing compatible vehicles to pass the intersection securely. Fig. 2 presents a signal cycle with four phases in an intersection, and we assume that each cycle has a fixed order of phases, i.e., phases are repeated based on the order " 1 ", " 2 ", " 3 " and " 4 ". This is an acceptable cycle program and is adopted by many cities like Xi'an. The main focus of this paper is to optimize the duration time of each phase with the aim of improving the service capability of a traffic network.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Four phases of a signal cycle.
Based on the above consideration, we can encode the signal cycles into a vector of integers, where each integer denotes the duration time of a phase of a given signal cycle. The reason of using integer value lies in that the duration times of real traffic lights are always integers. Table I presents a simple example to explain the solution encoding process.

There are two intersections and each of them has its own cycle with fixed order of phases. Each phase is assigned with a separate duration time specified in seconds. In this way, a candidate solution can be easily obtained and its length will be four times of the intersection number.

TABLE I. Solution Encoding of Two Intersections

## B. Optimization Criterion

To identify high-quality solutions, each candidate solution is evaluated by simulating it in the traffic networks implemented in VISSIM. The information obtained from the simulation can be employed as optimization criterion, i.e. fitness value. There are many useful information can be extracted from VISSIM through its evaluation module, such as the global mean speed of vehicles, mean travel time and mean delay time. The main objective of this study is to minimize the mean delay time of all vehicles traveling in a traffic network. The delay time of a vehicle is the time difference between its real travel time and the ideal travel time (no other vehicles, no signal control). By minimizing the mean delay time of all vehicles, the drivers can travel through a local area as soon as possible and thus get higher degree of satisfaction.

## C. Optimization Methods

$\mathrm{EDA}_{r e}[14]$ and EDA-VWH [15] are two efficient variants of estimation of distribution algorithms for solving continuous optimization problems. They will be introduced and modified to tackle the traffic signal optimization problem in this subsection.

## (1) Modified EDA $_{r e}$

$\mathrm{EDA}_{r e}$ is a recently developed Gaussian EDA (GEDA), it employs a univariate Gaussian model and enhances the search ability of traditional GEDA by improving the estimation method for the Gaussian model. Concretely, $\mathrm{EDA}_{r e}$ first estimates the weighted average of selected high-quality solutions as follows:

$$
\tilde{\boldsymbol{\mu}}^{i}=\frac{\sum_{j=1}^{|S|^{2}}\left[\log \left(\left|\boldsymbol{S}^{i}\right|+1\right)-\log i\right] \boldsymbol{S}_{i \mid \boldsymbol{S}^{i}}^{i}}{\sum_{j=1}^{|S|^{2}}\left[\log \left(\left|\boldsymbol{S}^{i}\right|+1\right)-\log j\right]}
$$

where $\boldsymbol{S}_{i \mid \boldsymbol{S}^{i}}^{i}$ represents the $i$ th best solution in the selected set $\boldsymbol{S}^{i}$. To obtain a more promising search center, $\mathrm{EDA}_{r e}$ further shifts $\tilde{\boldsymbol{\mu}}^{i}$ according to the following equations:

$$
\begin{gathered}
\Delta \hat{\boldsymbol{\mu}}^{\prime}=\hat{\boldsymbol{\mu}}^{\prime}-\hat{\boldsymbol{\mu}}^{t-1} \\
\hat{\boldsymbol{\mu}}^{\prime}=\left\{\begin{array}{ll}
\hat{\boldsymbol{\mu}}^{\prime}+2 \Delta \hat{\boldsymbol{\mu}}^{\prime}, & \text { if } f\left(\hat{\boldsymbol{\mu}}^{\prime}+2 \Delta \hat{\boldsymbol{\mu}}^{\prime}\right)<f\left(\hat{\boldsymbol{\mu}}^{\prime}\right)<f\left(\hat{\boldsymbol{\mu}}^{t-1}\right) \\
\hat{\boldsymbol{\mu}}^{\prime}-0.5 \Delta \hat{\boldsymbol{\mu}}^{\prime}, & \text { if } f\left(\hat{\boldsymbol{\mu}}^{\prime}\right)>\max \left\{f\left(\hat{\boldsymbol{\mu}}^{t-1}\right), f\left(\hat{\boldsymbol{\mu}}^{\prime}-0.5 \Delta \hat{\boldsymbol{\mu}}^{\prime}\right)\right\} \\
\hat{\boldsymbol{\mu}}^{\prime}, & \text { otherwise }
\end{array}\right.
\end{gathered}
$$

where $\hat{\boldsymbol{\mu}}^{\prime}$ is the shifted mean and $f(\cdot)$ is the objective function to be minimized. It has been shown that $\hat{\boldsymbol{\mu}}^{\prime}$ generally works better than $\hat{\boldsymbol{\mu}}^{\prime}$ and could guide $\mathrm{EDA}_{\text {ve }}$ to search more promising solution regions. Moreover, $\mathrm{EDA}_{\text {ve }}$ improves the variance estimator based on $\hat{\boldsymbol{\mu}}^{\prime}$ :

$$
\hat{\boldsymbol{\Delta}}^{\prime}=\frac{1}{\left|\boldsymbol{S}^{t}\right|} \sum_{t=1}^{\boldsymbol{S}^{t-1}}\left(\boldsymbol{S}_{t}^{t}-\hat{\boldsymbol{\mu}}^{\prime}\right) \circ\left(\boldsymbol{S}_{t}^{t}-\hat{\boldsymbol{\mu}}^{\prime}\right)
$$

where the symbol $\circ$ denotes dot product, and $\hat{\boldsymbol{\Delta}}^{\prime}$ stores the estimated variable variances.

After estimating $\hat{\boldsymbol{\mu}}^{\prime}$ and $\hat{\boldsymbol{\Delta}}^{\prime}$, a univariate Gaussian model could be built to produce new solutions. However, the solutions directly sampled from the model are composed of real numbers rather than integers, which are not feasible for the above signal optimization problem. To address this issue, we utilize a simple rounding function to make these solutions feasible. The rounding function will round the elements of a solution to the nearest integers so that it could be used to represent the duration times of traffic phases. The detailed steps of the modified $\mathrm{EDA}_{\text {ve }}\left(\mathrm{mEDA}_{\text {ve }}\right)$ are shown in Algorithm 1, where two points need to be noted. First, $\mathrm{mEDA}_{\text {ve }}$ adopts the truncation selection rule to select good solutions in step 4. Second, $\mathrm{mEDA}_{\text {ve }}$ maintains the current best solution and the mean $\hat{\boldsymbol{\mu}}^{\prime}$ to the next generation, so it only generates $(p-2)$ new solutions in step 7 .


## (2) Modified EDA-VWH

Different from $\mathrm{EDA}_{\text {ve }}, \mathrm{EDA}-\mathrm{VWH}$ is a Histogram EDA and adopts a univariate variable-width histogram model as the basic model. In order to balance the exploration and exploitation, the VWH model not only focuses on promising regions, but also assigns other regions with relatively low probabilities to alleviate premature convergence.

To build the marginal distribution model $H_{t}\left(x_{i}\right)$ for the $i$ th variable $x_{i}$, the search space $\left[a_{i}, b_{i}\right]$ is first divided in to $M$ bins, $\left[a_{i, m}, a_{i, m+1}\right), m=0,1, \ldots, M-2$ and $\left[a_{i, M-1}, a_{i, M}\right]$, where $a_{i, b}=a_{i}$ and $a_{i, M}=b_{i}$. Then the VWH model compute $a_{i, 1}$ and $a_{i, M-1}$ as:

$$
\begin{aligned}
& a_{i, 1}=\max \left\{x_{i, \min }^{1}-0.5\left(x_{i, \min }^{2}-x_{i, \min }^{1}\right), a_{i}\right\} \\
& a_{i, M-1}=\min \left\{x_{i, \max }^{1}+0.5\left(x_{i, \max }^{1}-x_{i, \max }^{2}\right), b_{i}\right\}
\end{aligned}
$$

in which $x_{i, \min }^{1}$ and $x_{i, \min }^{2}$ are the first and second minimum values, respectively, and $x_{i, \max }^{1}$ and $x_{i, \max }^{2}$ are the first and second maximum values, respectively, of the $i$ th elements of all the solutions in the current population.

The second to $(M-1)$ th bin in VWH model are set to have the same width:

$$
a_{i, m}-a_{i, m-1}=\frac{1}{M}\left(a_{i, M-1}, a_{i, 1}\right), m=2, \ldots, M-1
$$

It is obvious that the number of solutions in the first and the last bins are all zero, and it is also likely that some bins in the middle may contain no solutions. To guarantee that each bin has a probability to be searched, VWH model adjusts the count of solutions in each bin according to the following equation:

$$
C_{i, m}= \begin{cases}C_{i, m}+1, & \text { if } 1<m<M \\ 0.1, & \text { if } m=1, M \text { and } a_{i, m}>a_{i, m-1} \\ 0, & \text { if } m=1, M \text { and } a_{i, m}=a_{i, m-1}\end{cases}
$$

where $C_{i, m}$ is the count of solutions in the $m$ th bin. In this way, the promising solution regions could have higher probability to be searched, and the other regions could also have a chance to be explored. Based on $C_{i, m}$, the probability of variable $x_{i}$ in the $m$ th bin $H_{i, m}$ could be estimated as:

$$
H_{i, m}=\frac{C_{i, m}}{\sum_{j=1}^{M} C_{i, j}}
$$

Combing the rounding function as introduced above, a modified version of EDA-VWH could be obtained to solve

the traffic signal optimization problem, as shown in Algorithm 2. Different from $\mathrm{mEDA}_{v e}, \mathrm{mEDA}-\mathrm{VWH}$ forms the new population by selecting the best $p$ solutions from the current population and the produced population in step 7.

## IV. EXPERIMENTAL STUDIES

In this section, the experimental setup is first introduced, including an urban traffic network instance and the parameter settings. Then the performances of $\mathrm{mEDA}_{v e}$ and mEDAVWH are assessed and compared with several other algorithms. Analyses and discussions are made based on the experimental results.

## A. Experimental Setup

To test the performance of the two modified EDAs in a close-to-reality environment, the traffic network in an urban area of Xi'an, China was realized in VISSM by extracting real information from the digital map. Fig. 3 shows the map view of this area and the corresponding traffic network realized in VISSIM. This traffic network contains 11 intersections, so there are 44 decision variables need to be optimized with each of them denoting a phase duration time. We assume that the values of all phase duration times are all within the interval $[20,60] \in \mathbf{Z}^{\prime}$. This instance covers an area of approximately $2.2 * 2.5 \mathrm{~km}^{2}$, and there are 13 entrances and exits, respectively. For each entrance, the traffic volume was set to 500 vehicles per hour or 1000 vehicles per hour. Each vehicle travels through the network by following its own route with a maximum speed of $50 \mathrm{~km} / \mathrm{h}$ and leaves from an exit. The travel routes were randomly generated with the aim of covering as uniform as possible all networks.

The simulation time for each candidate solution was set to 500 s and the mean delay time of all vehicles traveling through the network was collected as the fitness value at the end of the simulation. To make a fair comparison, 10 independent runs were carried out for each algorithm with a maximum number of simulations of 10,000 for each run.

In the following experiments, the population sizes of $\mathrm{mEDA}_{v e}$ and mEDA-VWH were both set to 200. The truncation selection ratio of $\mathrm{mEDA}_{v e}$ was set as $\tau=0.5$, the bin number of mEDA-VWH was set as $M=15$. In addition to the
![img-2.jpeg](img-2.jpeg)
two EDAs, four other algorithms were also included in this experiment as competitors, including a GA [17], a PSO [18], a DE/current-to-best/1/bin algorithm [19] and a random search method [10]. The population sizes for the first three competitors were all set to 50 , their other parameters were set as the default values in their original papers. Besides, they also adopted the same rounding function to make their solutions suitable for the traffic signal optimization problem.

## B. Simulation Results and Discussions

Figs. 4(a) and (b) present the final optimization results obtained by the involved six algorithms in terms of mean delay time when the traffic volumes were set to 500 and 1000 vehicles per hour, respectively. The best, average and worst results of each algorithm are all reported for comparison. Observing the results in Figs. 4(a) and (b), we can give the following comments:

1) $\mathrm{mEDA}_{v e}$ achieves the best performance among the six algorithms. The best, average and worst results obtained by $\mathrm{mEDA}_{v e}$ are all smaller than the corresponding results obtained by other algorithms, respectively, which demonstrates the strong optimization ability of $\mathrm{mEDA}_{v e}$ in reducing the delay time of vehicles.
2) mEDA-VWH performs similar to DE and PSO, but is more stable. As we can see from Figs. 4(a) and (b) that the average results obtained by mEDA-VWH, DE and PSO are close to each other. The best results of mEDA-VWH are generally worse than that of DE and PSO, while the worst results of mEDA-VWH are better than that of DE and PSO. Therefore we can say that mEDA-VWH performs more stable than them.
3) $\mathrm{mEDA}_{v e}$ and mEDA-VWH adapt well to different traffic volumes. When the traffic volume increases from 500 vehicles per hour to 1000 vehicles per hour, the mean delay times obtained by different algorithms would generally grow. It is easy to understand since traffic congestion is more likely to occur with more vehicles. Nevertheless, the two EDAs could successfully find proper solutions and effectively reduce the mean delay time.
4) GA and the random search method perform relatively weak on this instance.
![img-3.jpeg](img-3.jpeg)

Fig. 3. The map view (left) and the traffic network (right) of an area in Xi'an.

![img-4.jpeg](img-4.jpeg)

Fig. 4. The optimization results of six algorithms with different traffic volumes: (a) 500 vehicles per hour, (b) 1000 vehicles per hour.
![img-5.jpeg](img-5.jpeg)

Fig. 5. The variation of the average results of the six algorithms with different traffic volumes: (a) 500 vehicles per hour, (b) 1000 vehicles per hour.
To delve into the performances of the six algorithms, the simulation results of them obtained during the optimization process are illustrated in Fig. 5. Figs. 5(a) and (b) show the variation of the average results of them when the traffic volumes were set to 500 and 1000 vehicles per hour, respectively. It can be seen that $\mathrm{mEDA}_{v e}$ keeps desirable improvement tendency and obtains the best final results. The convergence rate of mEDA-VWH is relatively low and it is finally ranked third in Fig. 5(a) and second in Fig. 5(b).

Based on the above simulation results, we can conclude that $\mathrm{mEDA}_{v e}$ and mEDA-VWH are both effective tools for solving traffic signal optimization problems and can significantly reduce the delay time of vehicles.

# V. Conclusions and Future Work 

In this paper, two modified estimation of distribution algorithms, i.e. $\mathrm{mEDA}_{v e}$ and mEDA-VWH, were proposed and employed to optimize the traffic signal cycles in an actual urban area. Since the two EDAs were originally developed for solving continuous optimization problems, we first modified them by combing them with a simple rounding function such that the resultant algorithms could adapt to the traffic signal
optimization problem. To assess the efficiencies of the two modified EDAs, a VISSIM-MATLAB integrated simulation platform was realized, in which the former works as a traffic simulator for evaluating candidate solutions and the latter is responsible for the implementation of algorithms. Through this simulation platform, the performances of the two modified EDAs were tested in a regional traffic network with 11 intersections located at Xi'an with the objective of reducing the mean delay time of vehicles. Simulation results on this traffic network with different traffic volumes demonstrated that the two modified EDAs were very robust and could effectively reduce the mean delay time of all vehicles. In comparison with four other algorithms, $\mathrm{mEDA}_{v e}$ achieved the best overall performance in different traffic conditions, which verified the advantage and potential of EDAs in solving traffic signal optimization problems.

In future work, we plan to test the performances of EDAs using different objectives besides the delay time. We are also interested in designing new simulation environment containing large-scale traffic networks as close as possible to real scenarios.
