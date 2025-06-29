# Reduction of carbon emissions and project makespan by a Pareto-based estimation of distribution algorithm 

Huan-yu Zheng, Ling Wang*<br>Tsinghua National Laboratory for Information Science and Technology (TNList), Department of Automation, Tsinghua University, Beijing 100084, China


#### Abstract

Article history: Received 28 March 2014 Accepted 6 December 2014 Available online 15 December 2014


Keywords:
Low-carbon production
Project scheduling
Estimation of distribution algorithm
Probability model
Multi-objective optimization

## A B STR A C T

Due to the increasing concerns about global warming, low-carbon production has been a hot topic around the world. In this paper, carbon emissions reduction and project makespan minimization are considered simultaneously. To formulate the problem, a multi-objective multi-mode resourceconstrained project scheduling model with makespan and carbon emissions criteria is given. To solve the problem, a Pareto-based estimation of distribution algorithm (PBEDA) is proposed. Specifically, an activity-mode list is used to encode the individual of the population; a hybrid probability model is built to describe the probability distribution of the solution space; and two Pareto archives are adopted to store the explored non-dominated solutions and the solutions for updating the probability model, respectively. New individuals are generated in the promising search areas by sampling and updating the hybrid probability model. Besides, Taguchi method of design of experiments is adopted to study the effect of parameter setting. Finally, numerical results and the comparisons to other algorithms are provided to show the effectiveness of the PBEDA in terms of quantity and quality of the obtained solutions. The Pareto set derived by the PBEDA can be helpful for project manager to recognize the relationship between carbon emissions and makespan so as to properly trade-off the two criteria according to certain preference.
(c) 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Currently, global climate change is one of the world's biggest public problems. As the concentration of $\mathrm{CO}_{2}$ in atmosphere is dangerously high, accompanied by more serious greenhouse effect, carbon emissions should be reduced. Although world carbon emission intensity has been reduced by $3 \%$ from 1980 to 2010, carbon emission rate has increased by $72 \%$ over the same time (Plambeck and Toktay, 2013). Facing the serious global climate change, several main economies are formulating stringent legislations or regulations on greenhouse gas emissions. Many companies are facing new constraints and trying to reduce carbon emissions while maximizing production profit.

As the largest energy-consuming industries, the industrial sector accounts for about half of world's total energy consumption (Fang et al., 2011), especially for some developing countries, e.g. more than $70 \%$ in China (Zhang and Wang, 2014). The current situation in China is "rich coal, less oil, gas shortage", i.e., coal is the main energy resource (Yu et al., 2014). Although the Chinese government and enterprises have taken great efforts, such as to shut down high energyconsumption firms, adoption of new energy-efficient technology, preference of renewable energy in the production process, carbon

[^0]emissions are still increasing rapidly as a result of economic growth. It was pointed out by Zhang and Wang (2014) that technology innovation alone is not sufficient to achieve the national carbon emission reduction target. According to Benjaafar et al. (2013), a more significant factor of carbon emissions are driven by business practices and operational policies rather than physical processes. Therefore, many measures should be taken to reduce carbon emissions by adopting advanced production, supply chain, and logistics methods.

In view of production economics, some methods to tackle carbon emissions can be considered at strategic, tactical and operational levels (Absi et al., 2013). At the strategic level, the design of supply chain or placement of factories and warehouses impacts carbon emissions (Sundarakani et al., 2010; Chaabane et al., 2012). At the tactical level, emissions are managed in production and distribution planning (Hua et al., 2011; Absi et al., 2013). At the operations level, emissions can be considered in production scheduling (Fang et al., 2011; Luo et al., 2013). At the operations level, the existing research work about lowcarbon production scheduling is very limited. Fang et al. (2011) presented a multi-objective mixed integer programming model of the flow shop scheduling problem considering the reduction of three objectives: peak power load, carbon emissions and the makespan. Luo et al. (2013) proposed a new ant colony optimization for a bi-objective hybrid flow shop scheduling problem reducing makespan and electric power cost with time-of-use electricity prices. Liu (2014) developed an $\varepsilon$-archived genetic algorithm (GA) for two batch scheduling problems


[^0]:    * Corresponding author. Tel.: +86 10 62783125; fax: +86 10 62786911.

    E-mail address: wangling@tsinghua.edu.cn (L. Wang).

to minimize $\mathrm{CO}_{2}$ emissions and total weighted tardiness, while Liu and Huang (2014) studied two cases using multi-objective GA. In most of the existing literature, peak power load is regarded as an objective, while it should be kept below certain engineering limit (Kobayashi et al., 2007). Therefore, it is important to model the problem of balancing production effectiveness and carbon emissions reasonably as well as to solve the problem with novel and effective approaches.

Essentially, it is a multi-objective optimization problem considering production effectiveness and carbon emissions simultaneously. During recent years, meta-heuristics have been widely used to solve the production scheduling problems with multiple objectives, such as GA (Chang et al., 2002, 2007, 2008; Li and Wang, 2007; Chang and Chen, 2009), differential evolution (Pan et al., 2008; Qian et al., 2008, 2009), particle swarm optimization (Li et al., 2008), artificial bee colony (Wang et al., 2012b), and estimation of distribution algorithm (EDA) (L. Wang et al., 2013a, 2013b). Among them, EDA (Larrañaga and Lozano, 2002) is a population-based search framework by building a probability model for sampling new individuals among the promising areas, which is different from GA that generates new individuals by crossover and mutation operators. So far, the EDA-based algorithms have been successfully applied to a variety of optimization problems in both academic and industrial fields, such as feature selection (Armananzas et al., 2011), multi-dimensional knapsack problem (Wang et al., 2012a, 2012b), hybrid electric vehicle charging (Su and Chow, 2012), single machine scheduling (Chen et al., 2010), shop scheduling (S. Wang et al., 2013a, 2013b; Chang and Chen, 2014), and system-level synthesis (Wang et al., 2014).

For multi-objective scheduling problems (L. Wang et al., 2013a, 2013b), the EDAs have been proved to be more effective than other evolutionary algorithms. To the best of our knowledge, there is no work about EDA for solving the low-carbon production scheduling problem. In this paper, the reduction of carbon emissions and project makespan is formulated as a Multi-Objective Multi-mode ResourceConstrained Project Scheduling Problem with Makespan and Carbon emissions criteria (MOMRCPSP-Makespan-Carbon). A Pareto-based EDA (PBEDA) is proposed to construct a Pareto set for the problem effectively. To be specific, an activity-mode list (AML) is adopted to encode the individuals, and a modified serial schedule generation scheme (SSGS) is used to decode the AML. Moreover, a hybrid probability model is built for generating new individuals, which is updated by using the non-dominated solutions in each generation that are stored in an updating archive. Meanwhile, a Pareto archive is adopted to store all the non-dominated solutions explored during the whole search process. With the Pareto set, a proper plan can be made according to the project manager's preference. To show the effect of parameter setting, investigation by the Taguchi method of design-ofexperiment method is carried out. Numerical results and the comparisons to other algorithms are provided, which demonstrate the effectiveness of the proposed PBEDA.

The remaining contents are organized as follows. In Section 2, the project scheduling model is presented to formulate the lowcarbon production scheduling problem. Following the brief introduction to the original EDA in Section 3, the PBEDA to derive a Pareto set for the problem is proposed in Section 4. Numerical results and comparisons are provided in Section 5. Finally, we end the paper with some conclusions and future work in Section 6.

## 2. Project scheduling model for low-carbon production scheduling

### 2.1. Low-carbon production scheduling problem

In today's low-carbon manufacturing industry, production efficiency and carbon emissions should be considered simultaneously by project managers. The low-carbon production scheduling problem
considers a production project which consists of a series of working procedures. In each procedure, a particular amount of work should be done on machines. The goal is to reduce the project makespan and carbon emissions by reasonably choosing the processing speed and making a schedule of the procedures. Usually, it assumes that
(1) Intermediate storage between machines is unlimited.
(2) The actual processing speed of each machine can be chosen from a set of finite and discrete set of speeds. Under different speeds, the duration and the energy consumption of the procedure are different.
(3) The quantity of carbon emissions per unit of consumed electricity is a constant.
(4) A peak power load constraint should not be violated during the project execution, as mentioned in Section 1.

This work is inspired by the research and production activities in a metal-forming industry, which is an important link in manufacturing chain, supplying metal products to major manufacturing companies (Balakrishnan and Brown, 1996). Steel production includes several process phases, and is very intensive in energy consumption (Tang et al., 2002). It is a typical case of the general carbon-efficient scheduling project to make the cast iron with slots. Several activities are included in the project which can be processed in different cutting speeds, such as face milling to prepare the surface, and profile milling to cut the slots.

A typical power profile of an activity is illustrated in Fig. 1 (Fang et al., 2011). As we only consider the duration, energy assumption and peak power, the presentation of the activity can be simplified as Fig. 2. The duration of an activity $j$ in mode $m \in M_{\mathrm{j}}$ is divided into two parts: the first part is the cutting part, where the power $P_{p n 1}$ is the peak power of the activity, and $d_{p n 1}$ is the duration of cutting process; the second part describes the rest energy assumption of the activity, where $P_{p n 2}$ is the power, and $d_{p n 2}$ is the duration of the second part. The relationship between a simplified activity and the original one is as follows:
$P_{p n 1}=P_{\text {cutting }}+P_{\text {idle }}+P_{\text {basic }}$
$d_{p n 1}=t_{\text {cutting }}$
$P_{p n 1} d_{p n 1}+P_{p n 2} d_{p n 2}=P_{\text {basic }} t_{\text {basic }}+P_{\text {idle }} t_{\text {idle }}+P_{\text {cutting }} t_{\text {cutting }}$
$d_{p n 2}=t_{\text {basic }}-t_{\text {cutting }}$
where $t_{\text {basic }}, t_{\text {idle }}, t_{\text {cutting }}$ and $P_{\text {basic }}, P_{\text {idle }}, P_{\text {cutting }}$ denote the time and power in the basic, idle and cutting phases of an activity, respectively.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Power profile for an activity (Fang et al., 2011).

### 2.2. Resource-constrained project scheduling model

The resource-constrained project scheduling problem (RCPSP) is one of the most important problems in scheduling field, where scarce resources are allocated to dependent activities over time (Brucker et al., 1999). During the past few decades, the RCPSP and its extended problems have been widely studied (Agarwal et al., 2007; Shukla et al., 2008; Fang and Wang, 2012; Wang and Fang, 2012). A majority of realistic problems have also been formulated as RCPSP, such as shop scheduling problem (Voß and Witt, 2007), service centers management (Quintanilla et al., 2012), system-level synthesis problem (Wang et al., 2014), and software project management (Alba and Francisco Chicano, 2007; Chen and Zhang, 2013).

According to the characteristics of the low-carbon production scheduling problem, it can be modeled as MOMRCPSP-MakespanCarbon: A project contains $J$ activities, and each activity $j=1,2, \ldots, J$ can be executed in $M_{J}$ modes, corresponding to different processing speeds. Before activity $j$ starts, a set of activities should be completed, which are denoted as the precedence activity set $\boldsymbol{P S}_{\boldsymbol{J}}$. The only renewable resource constraint is the peak power load limit $P_{\max }$.

The start and the end of a project are presented by dummy activities 0 and $J+1$, respectively. The power consumption and durations of dummy activities are zero. The extended activity set $(0,1, \ldots, J+1)$ is denoted as $\boldsymbol{J}^{+}$. The objective of the MOMRCPSP-Makespan-Carbon is to minimize both the makespan and the carbon emissions. Thus, the mathematical model of the MOMRCPSP-Makespan-Carbon can be formulated as follows:

Minimize[Makespan, Carbon]
Subject to Makespan $=\frac{\left\{F T_{j+1}\right.}{t+\frac{1}{E F T_{j+1}}} t \cdot x_{j+1,1, t}$
$E=\sum_{j=1}^{J} \sum_{m=1}^{M_{j}}\left(P_{j m 1} \cdot d_{j m 1}+P_{j m 2} \cdot d_{j m 2}\right) \cdot \sum_{t=E F_{j}}^{t_{E}}\sum_{x_{j m t}}$
![img-2.jpeg](img-2.jpeg)

Fig. 2. A simplified activity.
![img-2.jpeg](img-2.jpeg)

Fig. 3. An example of the MOMRCPSP-Makespan-Carbon.

Carbon $=\varepsilon \cdot E$
$\sum_{m=1}^{M_{j}} \sum_{t=E F_{j}}^{t_{E}} x_{j m t}=1, \quad j \in \boldsymbol{J}^{+}$
$\sum_{m=1}^{M_{j}} \sum_{t=E F_{j}}^{t_{E}} t \cdot x_{i m t} \leq \sum_{m=1}^{M_{j}} \sum_{t=E F_{j}}^{t_{E}}\left(t-d_{j m 1}-d_{j m 2}\right) \cdot x_{j m t}, \quad j \in \boldsymbol{J}^{+}, \quad i \in \boldsymbol{P S}_{\boldsymbol{J}}$

$$
\begin{aligned}
& \sum_{j=1}^{J} \sum_{m=1}^{M_{j}} P_{j m 1} \sum_{\substack{\text { min } \left(t+d_{j m t}+d_{j m 2}-1, L F_{j}\right) \\
t=\max _{j=1}^{E F_{j}} \sum_{m=1}^{M_{j}} P_{j m 2}} \sum_{\substack{\sum_{t=\max (t+1, E F_{j}) \\
t=1,2, \ldots, T}} x_{j m t} \leq P_{\max }, \quad t=1,2, \ldots, T \\
& x_{j m t}= \begin{cases}1 & \text { if activity } j \text { is performed in mode } m \text { and finished at time } t \\
0 & \text { otherwise }\end{cases}
\end{aligned}
$$

where $x_{j m t}$ is a decision variable that represents whether activity $j$ is executed in mode $m$ and finishes at time $t$, as shown in Eq. (12). Eq. (5) defines the goal is to minimize the makespan and carbon emissions; Eqs. (6) and (7) are used to calculate the makespan and the project electric energy consumption $E$, respectively; Eq. (8) describes the relationship between carbon emissions and the electric energy consumption, in which $\varepsilon$ is the quantity of carbon emissions per unit of electric energy consumption; Eq. (9) guarantees that each activity is executed only once; Eq. (10) shows the precedence constraints of the project; Eq. (11) confirms that the peak power load limit should not be exceeded; $L F T_{j}$ and $E F T_{j}$ are the latest finish time and the earliest finish time of activity $j$, respectively; $T$ is an upper bound for the project makespan.

Let $x=\left\{x_{j m t}, j \in \boldsymbol{J}^{+}, m=1,2, \ldots, M_{j}, t=1,2, \ldots, T\right\}$ be a solution and $\chi$ be the set of all solutions. Consider two solutions $x_{1}, x_{2} \in \chi$, $x_{1}$ dominates $x_{2}\left(x_{1}>x_{2}\right)$ if
$M S\left(x_{1}\right) \leq M S\left(x_{2}\right) \quad$ and $\quad \operatorname{Carbon}\left(x_{1}\right) \leq \operatorname{Carbon}\left(x_{2}\right)$
where at least one of the inequalities is strict. A solution $x$ is called a Pareto optimal solution or a non-dominated solution iff there does not exist another solution $x^{\prime} \in \chi$ that dominates $x$. The Pareto set is constituted by all Pareto optimal solutions.

A simple example of the MOMRCPSP-Makespan-Carbon with four activities is shown in Fig. 3, in which activity 0 and activity 3 are dummy activities. An activity-on-node network is used to represent the project, where activities are denoted as nodes and precedent restraints between activities are denoted as arcs. Each non-dummy activity has two modes. The power requirements and corresponding durations are shown in Table 1. The peak power load limit is 16 , i.e., $P_{\max }=16$, and the quantity of carbon emissions per unit of electric energy consumption is 1 , i.e., $\varepsilon=1$. The Pareto set is presented in Fig. 4.

## 3. Estimation of distribution algorithm

As a relatively new paradigm in the field of evolutionary computation, EDA (Larrañaga and Lozano, 2002; Lozano et al., 2006) is a general framework of statistical learning based optimization algorithm. With statistical analysis tool, the EDA makes the population movement track the promising search areas based on the available experience. For a minimization problem, the procedure of the EDA is shown below.

Step 1: Initialize the population and the probability model.
Step 2: Sample the probability model to generate a new population.

Step 3: Construct the elite population and update the probability model.
Step 4: Go to Step 2 unless a stopping criterion is met.

The critical step of the EDA procedure is to estimate the probability distribution. According to the characteristics of different problems, different probability models should be established to estimate the reasonable promising probability distribution. In the next section, a specially designed EDA with a probability model and an updating mechanism will be presented to obtain a Pareto set for the low-carbon production scheduling problem.

## 4. The Pareto based EDA

In this section, the encoding and decoding schemes, initialization, hybrid probability model, sampling mechanism, and updating mechanism will be presented sequentially. Then, the framework of the PBEDA will be given and the computational complexity will be analyzed.

Table 1
Power requirements and corresponding durations of the example in Fig. 3.
![img-3.jpeg](img-3.jpeg)

### 4.1. Encoding and decoding schemes

Experimental evaluation by Hartmann and Kolisch (2000) showed that metaheuristics using the activity list perform generally better than those adopting other representations. As the MOMRCPSP-Makespan-Carbon is a generalization of the RCPSP, the AML based encoding scheme is adopted in the PBEDA expecting to get good results. That is, $\mathrm{AML}=[\pi, \lambda]$, where $\pi=\left[\pi_{1}, \pi_{2}, \ldots, \pi_{j}\right]$ is the activity list, denoting the priority of activities; and $\lambda=\left[\lambda_{1}, \lambda_{2}, \ldots, \lambda_{j}\right]$ is the mode list, where $\lambda_{j} \in\left\{1,2, \ldots, M_{j}\right\}$, representing the execution mode of each activity.

Note that activities in this paper are different from the original form (see Section 2). The serial schedule generation scheme (Kolisch, 1996) (see Fig. A1 for pseudo code) is modified to build a schedule (a solution to an individual) according to activities in this paper. When an AML is given, the activities are scheduled in the activity list order as early as possible, satisfying the precedence constraints and peak power load limit. The pseudo code of the scheme is illustrated in Fig. 5, where $n$ is the iteration; $\boldsymbol{S}_{\boldsymbol{n}}$ denotes the set of scheduled activities; $\boldsymbol{D}_{\boldsymbol{n}}$ is the decision set, containing all schedulable activities; $\pi P_{t}$ denotes the deviation from the peak power load limit at time $t ; \boldsymbol{A}_{\boldsymbol{1 t}}$ and $\boldsymbol{A}_{\boldsymbol{2 t}}$ represent sets of activity's first and second part active at the schedule time, respectively.

### 4.2. Initialization

The population of PBEDA is initialized by generating Popsize individuals (decoded as AML). To be specific, an AML is generated as follows.

First, for each non-dummy activity, a possible mode is uniformly and randomly chosen to generate a mode list. Then, an iterative procedure is followed to generate the activity list. After the $l$ th iteration, the set of selected activities are denoted as $\boldsymbol{S A}_{\boldsymbol{l}}$. If

![img-4.jpeg](img-4.jpeg)

Fig. 4. Pareto set for the example in Fig. 3.

## Modified SSGS

$$
\begin{aligned}
& n=1, S_{n}=\varnothing \\
& \text { While }\left|S_{n}\right| \leq J \\
& \quad D_{n}=\left\{j \mid j \in S_{n}, P S_{j} \subseteq S_{n}\right\} \\
& \quad \sigma_{1}^{n}=P_{\text {

## Archive Updating

$\boldsymbol{U A}=\varnothing$;
For $i=1$ to Popsize
flag $=$ true;
For $j=1$ to $|\boldsymbol{P A}|$
If $S P_{j}>S N_{i}$ or $S P_{j}=S N_{i}$
flag $=$ false;
break;
End if

## End for

If flag $==$ true
For $j=1$ to $|\boldsymbol{P A}|$
If $S N_{i}>S P_{j}$
Remove $S P_{j}$ from $\boldsymbol{P A}$;
End if
End for
Add $S N_{i}$ to $\boldsymbol{P A}$ and $\boldsymbol{U A}$;

## End if

## End for

Fig. 6. Pseudo code of the archive updating procedure.
$R_{j k}^{k}= \begin{cases}1 & \text { if activity } j \text { is executed in mode } i \\ 0 & \text { else }\end{cases}$
### 4.7. Procedure of the proposed PBEDA

The procedure of the proposed PBEDA is summarized as follows. First, the population and the probability matrix $\boldsymbol{P M A c t}$ $(0)$ and $\boldsymbol{P M M o d}(0)$ are initialized. Then, a new population is generated by sampling the probability model with the designed sampling mechanism. After all the individuals are evaluated by the modified SSGS, the Pareto archive PA is updated, and solutions improving PA are selected into UA. With UA, the probability matrix $\boldsymbol{P M A c t}(\mathrm{g})$ and $\boldsymbol{P M M o d}(\mathrm{g})$ are updated. The procedure is repeated until a stopping criterion is met. The flowchart of the procedure is illustrated in Fig. 7.

### 4.8. Computational complexity analysis

For each generation of the PBEDA, its computational complexity is analyzed as follows.

For the sampling process, every position of activity list is generated by randomly sampling $\boldsymbol{P M A c t}$, the construction of the activity list is with the complexity $O\left(J^{2}\right)$; every execution mode of the mode list is sampled with the PMMod, the computational complexity of generating a mode list is $O(M J)$. Note that the size of population is Popsize, a population can be generated with the complexity $O\left(J \cdot\right.$ Popsize $\left.\cdot(J+M)\right]$.

For the decoding process, Ballestín (2007) pointed out that the complexity of the original SSGS to generate a schedule is $O\left(K \cdot J^{2}\right)$, in which $K$ is number of renewable resources. As the peak power load limit is the only resource constraint, i.e., $K=1$, then the modified SSGS to generate a schedule is with the complexity of $O\left(J^{2}\right)$. Thus, the complexity of generating schedules for a population is $O\left(\right.$ Popsize $\left.\cdot J^{2}\right)$.

For the updating process, to update $\boldsymbol{P A}$ and construct $\boldsymbol{U A}$, the solutions to newly generated individuals are compared to solutions
![img-5.jpeg](img-5.jpeg)

Fig. 7. The flowchart of the PBEDA.
in $\boldsymbol{P A}$, with the complexity of $O\left(\right.$ Popsize $\cdot(\boldsymbol{P A})$. Usually, $|\boldsymbol{P A}|$ is similar to or less than $J$. Thus, the complexity of updating process can be roughly estimated as $O\left(\right.$ Popsize $\left.\cdot J\right)$. To update all $J^{2}$ elements of $\boldsymbol{P M A c t}$ and $M \cdot J$ elements of PMMod, it is with the complexity of $O\left(J^{2}+M J\right)$. So, the complexity of the updating process is $O\left(J \cdot\right.$ Popsize $\left.\left.+J+M\right)\right]$.

Thus, the computational complexity of each generation of the PBEDA is $O\left[J \cdot\right.$ Popsize $\left.\cdot(J+M)\right]+O\left(\right.$ Popsize $\left.\cdot J^{2}\right)+O\left[J \cdot\right.$ Popsize $\left.+J+\right.$ $M)]$, which can be simplified as $O\left[\right.$ Popsize $\left.\cdot J \cdot(2 J+M)\right]$. Taking the number of generation $g$ into account, the total computational complexity of the PBEDA is $O\left[g \cdot\right.$ Popsize $\left.\cdot J \cdot(2 J+M)\right]$. It can be seen that the complexity of the proposed PBEDA does not increase greatly compared to solution space as the size of problem increases.

## 5. Numerical results and comparisons

To test the performance of the proposed PBEDA, numerical simulations are carried out and comparisons to random search algorithm (RAND) and the well-known non-dominated sorting genetic algorithm II (NSGA2) (Deb et al., 2002) are performed. All the experiments are implemented on a PC with 2.83 GHz processor/4.00 GB RAM in Windows 7. The algorithm is coded in C++ using Microsoft Visual Studio 2008.

### 5.1. Test data description

To evaluate the performance of different algorithms, test data is needed for different situations in accordance with problem size and structure. Due to the difficulty in accessing real data from industry, a set of test data is generated randomly as follows.

First, the number of activities and the precedence relationship between activities of projects are the same as the standard multimode RCPSP test data sets from the well-known PSPLIB (Kolisch and Sprecher, 1996) j10, j20 and j30, which contain 536, 554, 552 projects, respectively. Then, the levels and ranges of other factors are shown in Table 2. Note that each non-dummy activity in a project is assigned three modes, corresponding to different cutting speeds. In addition, factors $P_{\text {cutting }}$ and $t_{\text {cutting }}$ of an activity are calculated as Eqs. (27) and (28). The quantity of carbon emissions

Table 2
Factors and their levels.

Table 3
Combinations of parameter values.

per unit of electric energy consumption is set to 1 , i.e., $\varepsilon=1$.
$P_{\text {cutting }}=\delta V_{\text {cutting }}^{2}$
$t_{\text {cutting }}=U / V_{\text {cutting }}$

### 5.2. Parameters setting

The PBEDA contains three key parameters: the population size of each generation (Popsize) and the learning rates of PMAct and PMMod ( $\theta_{1}$ and $\theta_{2}$ ). The Taguchi method of design of experiment (DOE) (Montgomery, 2005) is used to investigate the effect of parameter setting on the PBEDA. Combinations of different values for these parameters are listed in Table 3. The data set with moderate scale j20 is chosen to carry out the DOE test. The stopping criterion is set to a maximum 50,000 number of schedules for each project.

According to the number of parameters and the number of factor levels, we choose the orthogonal array $L_{10}\left(\boldsymbol{s}^{3}\right)$. That is, the total number of treatments is 16 , the number of parameters is three and the number of factor levels is four. For the ith parameter combination, $i=1,2, \ldots, 16$, the PBEDA is run to obtain a set of nondominated solutions $\boldsymbol{P A}_{i}^{1}$ for project $j$ of j20. The non-dominated solutions among all $\boldsymbol{P A}_{i}^{1}$ for project $j$ are collected as the reference set $\boldsymbol{R S}_{j}$. Clearly, the more solutions in $\boldsymbol{R S}_{j}$ obtained by one parameter combination, the better the combination is. The average response variable (ARV) is the average percentage of nondominated solutions for each combination of $\boldsymbol{R S}_{j}$, which can be calculated as Eq. (29). The orthogonal array and the obtained ARV values are shown in Table B1.
$\operatorname{ARV}(i)=\frac{1}{554} \sum_{j=1}^{554} \frac{\left|\boldsymbol{R S}_{j} \cap \boldsymbol{P A}_{j}^{1}\right|}{R S_{j}} \times 100 \%$
The trend of each factor level is shown Fig. 8. Then, the response value of each parameter is figured out and the significance rank of each parameter is analyzed in Table 4.

From Table 4, it can be seen that learning rate of PMMod $\theta_{2}$ is the most significant parameter among the three factors. As the carbon emissions are only decided by mode list, while the makespan is decided by both activity list and mode list, the adjustment of mode list is more crucial to the performance of PBEDA. Thus, $\theta_{2}$ is a more significant parameter than learning rate of PMAct $\theta_{1}$. From Fig. 8, it can be seen that $\theta_{2}$ should neither be too small nor too large, as a large $\theta_{2}$ makes the algorithm easily be trapped in local minima, while a small $\theta_{2}$ leads to a slow convergence. The parameter $\theta_{1}$ ranks second among the three. Similar to $\theta_{2}$, a large value of $\theta_{1}$ leads to premature convergence, but it is indicated that a small $\theta_{1}$ is helpful to maintain population diversity. Although the population size Popsize has the least significance to the algorithm, a suitable one can still yield a good performance. According to the analysis above, an appropriate combination of parameters is suggested as Popsize $=80, \theta_{1}=0.01$ and $\theta_{2}=0.05$.

### 5.3. Pareto sets with different computing budget

In this section, the Pareto sets with different computing budget are investigated using the instance j3010_9. The stopping criteria are set to 1000, 5000 and 50,000 schedules.

The Pareto sets of the instance j3010_9 with different stopping criteria are shown in Fig. 9. It can be seen that as more schedules are generated, the solutions in the approximate Pareto set become better and the size of approximate Pareto set becomes larger. This implies that the PBEDA can keep on finding better and more solutions with the increase of computational budget.

### 5.4. Comparison of different algorithms

Next, the PBEDA is compared with RAND and the well-known multi-objective optimization algorithm NSGA2 (Deb et al., 2002), which adopt the same encoding and decoding procedure as PBEDA. In addition, for NSGA2, some widely used genetic operators for the RCPSP are adopted: two-point crossover (Hartmann, 1998) and permutation-based local search (PBLS) (Fang and Wang, 2012). To compare the performance of different algorithms, the following performance metrics are adopted:
(1) The size of approximate Pareto set. An approximate Pareto set is better, if it contains more solutions. It means more choices can be provided to the project manager.
(2) The coverage of the approximate Pareto sets (Zitzler and Thiele, 1999). Suppose two approximate Pareto sets $\boldsymbol{P A}_{1}$ and $\boldsymbol{P A}_{2}$ obtained by two algorithms. The coverage of $\boldsymbol{P A}_{1}$ and $\boldsymbol{P A}_{2}$, denoted as $C\left(\boldsymbol{P A}_{1}, \boldsymbol{P A}_{2}\right) \in[0,1]$, which is also called $C$ values between $\boldsymbol{P A}_{1}$ and $\boldsymbol{P A}_{2}$, is defined as follows:
$C\left(\boldsymbol{P A}_{1}, \boldsymbol{P A}_{2}\right)=\left\{\left(x_{2} \mid x_{2} \in \boldsymbol{P A}_{2}, \quad \exists x_{1} \in \boldsymbol{P A}_{1}: x_{1}>x_{2}\right.\right.$ or $\left.\left.x_{1}=x_{2}\right\}\right\}\left(\mid \boldsymbol{P A}_{2}\right)$

The larger value of $C\left(\boldsymbol{P A}_{1}, \boldsymbol{P A}_{2}\right)$, the more solutions that in $\boldsymbol{P A}_{2}$ are dominated by or equal to solutions in $\boldsymbol{P A}_{1}$. If $C\left(\boldsymbol{P A}_{1}, \boldsymbol{P A}_{2}\right)$ is larger than $C\left(\boldsymbol{P A}_{2}, \boldsymbol{P A}_{1}\right)$, then $\boldsymbol{P A}_{1}$ is better than $\boldsymbol{P A}_{2}$ in sense of the Pareto dominance. That is, the algorithm obtaining $\boldsymbol{P A}_{1}$ is better than that obtaining $\boldsymbol{P A}_{2}$.

In our experiments, the population size of NSGA2 is set to 100, and the probability of exchanging two consecutive activities by PBLS is set to 0.2 . The stopping criteria are set to 1000, 5000 and 50,000 schedules for each project. The average sizes of the approximate Pareto sets for j10, j20 and j30 are listed in Tables 5, 6 and 7, respectively.

It can be seen from the tables that the PBEDA can provide more solutions in the approximate Pareto set than RAND and NSGA2 on

![img-6.jpeg](img-6.jpeg)

Fig. 8. Factor level trend of the PBEDA.

Table 4
Response value and significance rank.

![img-7.jpeg](img-7.jpeg)

Fig. 9. Pareto front with different computing budget.

Table 5
Average size of the approximate Pareto set for j10.
Note: the bold values mean the best results.
all cases, especially for middle to large scale problems. This implies that the PBEDA is superior to RAND and NSGA2 in terms of population diversity.

In terms of $C$ values, the box plot is used to show the distributions intuitively. For each project in j10, j20 and j30, RAND, PBEDA and NSGA2 are compared to each other in pairs to calculate $C$ values. The

Table 6
Average size of the approximate Pareto set for j20.
Note: the bold values mean the best results.

Table 7
Average size of the approximate Pareto set for j30.
Note: the bold values mean the best results.
box plots with different stopping criteria for j10, j20 and j30 are shown in Figs. 10, 11 and 12, respectively. Each subfigure contains three box plots representing the distributions of $C$ values for pairs of algorithms when stopping criterion is set to 1000, 5000, and 50,000 schedules, respectively. The median is indicated by a line inside the box. The lower quartile $q_{1}$ and upper quartile $q_{3}$ are indicated by the lower and upper ends of the box (called inner fences). The lower and upper ends of whiskers indicate the outer fences of the box, which are $4.5 q_{1}-1.5 q_{3}$ and $4.5 q_{3}-1.5 q_{1}$. Outliers plotted in dots indicate data that are not between the outer fences.

From Figs. 10 to 12, it can be seen that the PBEDA is superior to the NSGA2 and the RAND on all data sets with all the three stopping criteria. Taking j30 with 1000 schedules as an example, it can be seen from Fig. 12 that the median value of $C$ (PBEDA, NSGA2) is 0.6 , and the median value of $C$ (NSGA2, PBEDA) is 0.2 . Also, it can be seen from Figs. 10 to 12 that with 5000 or 50,000 generated schedules, all median values of $C$ (PBEDA, NSGA2) and $C$ (PBEDA, RAND) equal to 1 . That is, the PBEDA is better than the other two algorithms on coverage of the approximate Pareto set especially when computational budget is medium to large.

In addition, the average CPU times spent by PBEDA, NSGA2 and RAND for each instance in j10, j20 and j30, are shown in Table 8, with maximum 50,000 schedules as the stopping criterion.

From Table 8, it can be seen that in each problem set, CPU time spent by the PBEDA is slightly more than that of the RAND and the NSGA2. The reason is that the RAND and the NSGA2 perform search on the solution space directly, while the PBEDA needs to update and sample the probability distribution to perform search process. Fortunately, the average CPU time of the PBEDA is at the same level of the RAND and the NSGA2. Above all, the Pareto set found by the PBEDA has much better quality than

![img-8.jpeg](img-8.jpeg)
those by the RAND and the NSGA2. Therefore, the PBEDA is more effective than both the NSGA2 and the RAND considering two performance metrics in terms of quantity and quality of the obtained solutions.

The effectiveness of the PBEDA owes two main reasons. First, probability model of the PBEDA can predict the movements of population in the search space and estimate the potential probability distribution of the encoded representation, so as to generate new

![img-9.jpeg](img-9.jpeg)

Fig. 12. Box plots of $C$ values for $\mathrm{j} 30$.

Table 8
Average CPU times (s).
individuals according to the promising search areas. Second, by using updating archive, the probability model is updated by excellent individuals, which improves the convergence rate of the probability model. The hybrid probability model of the PBEDA can provide the manager information about the distribution of project activities and modes. Then activities can be put on proper positions with proper modes. Since the PBEDA optimizes carbon reduction and project makespan at the same time, it helps the manager to understand the relationship between these two objectives. Because the PBEDA can find a better Pareto set than the RAND and the NSGA2 in both quantity and quality, more and better choices for project manager can be chosen to make a flexible decision according to certain preference between reduction of carbon emissions and production effectiveness.

## 6. Conclusions

In this paper, the low-carbon production scheduling problem was modeled as a multi-objective multi-mode resource-constrained project scheduling problem concerning both the makespan and carbon emissions criteria. Then, a Pareto-based estimation of distribution algorithm was proposed to solve the problem. Numerical results and comparisons showed the effectiveness of the algorithm in solving the low-carbon production scheduling problem. This work is the first to formulate the low-carbon production
scheduling problem as a project scheduling model, and it is also the first work to solve the problem by developing a multi-objective estimation of distribution algorithm. As the majority of the project scheduling approaches have focused on production effectiveness but ignored environmental objectives, this work is an important addition to the literature. And, this work can be useful for project manager in production industry to balance production effectiveness and carbon emissions under peak power load constraint. Future work could focus on further studying the low-carbon production issues, such as exploring problem-specific methodologies. It is also interesting to develop other novel evolutionary algorithms for the problems and to extend research on low-carbon scheduling in distributed production environments.

## Acknowledgments

This research is partially supported by the National Key Basic Research and Development Program of China (2013CB329503), the National Natural Science Foundation of China (61174189, 61025018), and the Doctoral Program Foundation of Institutions of Higher Education of China (20130002110057).

## Appendix A

See Fig. A1, where $J, T$ and $\boldsymbol{P S}_{\boldsymbol{j}}$ are consistent with the notations in Section 2; $n, \boldsymbol{S}_{\boldsymbol{n}}, \boldsymbol{D}_{\boldsymbol{n}}$ and $\pi$ are consistent with the notations in Section 4.1; $K$ represents the number of renewable resources in the project; $\pi K_{r t}$ denotes the left over amount of renewable resource $r$ at time period $t$; for each period, there are $K_{r}$ units of renewable resource $r$; activity $j$ requires $k_{j r}$ units of renewable resource $r$ during its duration.

## Original SSGS

$$
\begin{aligned}
& n=1, S_{n}=\varnothing \\
& \text { While }\left|S_{n}\right| \leq J \\
& \qquad D_{n}=\left\{j \mid j \notin S_{n}, P S_{j} \subseteq S_{n}\right\} \\
& \qquad \pi K_{i t}=K_{y}=\sum_{j \in A_{i}} k_{j r}, t=1,2, \ldots, T, r=1,2, \ldots, K \\
& \qquad j^{*}=\min _{j \in D_{n}}\left\{j \mid \pi_{j}=\inf _{i \in D_{n}} \pi_{j}\right\} \\
& E F T_{j^{*}}=\max \left\{F T_{i} \mid i \in P S_{j^{*}}\right\}+d_{j^{*}} \\
& F T_{j^{*}}=\min \{t \mid E F T_{j^{*}} \leq t \leq L F T_{j^{*}}, \\
& k_{j^{*}, \tau} \leq \pi K_{c \tau}, \tau=t-d_{j^{*}}+1, \ldots, t, r \in R\} \\
& S_{n+1}=S_{n} \cup\left\{j^{*}\right\} \\
& n=n+1
\end{aligned}
$$

## End while

Fig. A1. Pseudo code of the original SSGS (Kolisch, 1996).

## Appendix B

See Table B1.
Table B1
Orthogonal array and ARV values.