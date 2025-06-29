# Manufacturing rescheduling after crisis or disaster-caused supply chain disruption 

Hongguang Bo ${ }^{a, 1}$, Xiao Alison Chen ${ }^{b, c, 1}$, Qian Luo ${ }^{c, 1}$, Wenpeng Wang ${ }^{a, 1}$<br>${ }^{a}$ School of Economics and Management, Dalian University of Technology, 2 Lingqing Rd, Dalian, China<br>${ }^{b}$ Peter T Paul College of Business and Economics, University of New Hampshire, 10 Garrison Ave, Durham, NH, USA<br>${ }^{c}$ International Business School Suzhou, Xi'an Jiaotong-Liverpool University, 111 RenAi Rd, Suzhou, China

## A R TICLE INFO

Keywords:
Production rescheduling Supply chain disruption Two-stage genetic algorithm Estimation of distribution algorithm Productivity recovery

## A B STR ACT

In this paper, we study the problems a repair shop has with rescheduling after major supply disruptions. The repair shop provides repair and maintenance services to its customers. After a major disruption to production, the repair shop faces delays in production and order delivery due to shortages in materials and/or labor, which requires rescheduling of all the unfinished parts. We observe that the finished parts incur high holding costs until the entire order is completed, while any unfinished parts (in the form of raw material or work-in-progress) incur low holding costs until production starts. Moreover, the repair shop incurs a setup cost when switching between different types of parts. Considering these new features, we formulate the rescheduling problem for the repair shop under a coordinated supply chain as an integer program to minimize the total tardiness, setup cost, and holding cost. To solve the model, we propose an innovative two-stage genetic algorithm, which utilizes the estimation of distribution algorithm (EDA) to improve the search process of the optimal solution. We test the performance of this algorithm on a dataset generated from the order data of a heavy machinery maintenance provider. The numerical results show that our model generates solutions that outperform the initial schedule, which was obtained by minimizing holding and setup costs without disruption. In addition, using other closely-related genetic algorithms as benchmarks, we show that our algorithm outperforms the benchmarks without sacrificing the computational time. We also discuss an extension of the main model by considering the recovery of productivity in terms of processing time.

## 1. Introduction

Production scheduling has been heavily studied in supply chain and operations management because of its importance and complexity. It is a crucial part of many industries, including manufacturing, healthcare, and distribution (see, for example, Graves 1981, Portougal and Robb 2000, Guido et al. 2017, Sun et al. 2020, Helo et al. 2019). To achieve optimal operations performance, researchers have worked on different types of job scheduling or worker scheduling models. As technology and the industries evolve, scheduling problems incorporate more constraints and flexibility to model specific scenarios. In recent years, rescheduling models have become an emerging field of research. Rescheduling models study how to schedule jobs again when the initial production plan cannot be further continued as certain conditions or constraints no longer hold. Rescheduling is often necessary when there is a disruption in the supply and production system to reduce or avoid losses caused by the interruption; such interventions can save millions of dollars (Sheffi 2005, Kim et al. 2010).

An example of such a disruption is the recent COVID-19 pandemic. In the case of the COVID-19 pandemic, city lockdowns caused countless issues and sustained impacts on transportation, food processing, manufacturing, and the healthcare industry. The interruptions resulted in shortages in raw materials, consumer goods, and labor. Millions of people lost jobs, housing, and healthcare due to the COVID-19 pandemic, which has become a social and economic crisis for many countries with far-reaching and long-lasting effects.

During this crisis, many manufacturing plants have faced raw material shortages, labor shortages, shipping delays, and plant shutdowns, all of which call for production rescheduling (Marinova and Bitri 2021, Magableh 2021, Sheffi 2021). A particular problem we have observed in practice is the delay of production and order delivery due to the mandatory shutdown of a job shop that performs maintenance and repair services in Qingdao. This repair shop orders parts from a designated manufacturer in the same city. During regular operation, the repair shop uses a scheduling tool to generate an optimal production

[^0]
[^0]:    ${ }^{a}$ Corresponding author.

    E-mail addresses: hgbo@dlut.edu.cn (H. Bo), Alison.Chen@unh.edu (X.A. Chen), Qian.Luo@xjtlu.edu.cn (Q. Luo), wwpeng@mail.dlut.edu.cn (W. Wang).
    ${ }^{1}$ All authors contributed equally to the manuscript.

schedule based on the due dates, inventory holding cost, and setup costs. When everything goes according to plan, all orders can be produced and shipped by the due date. However, a mandatory lockdown in Qingdao disrupted the production schedule for weeks. Some parts had already been produced by the manufacturer while others had not. The repair shop had to wait for all parts to be produced before delivering the entire order. After the production resumes, many orders will be delayed if the repair shop continues to produce according to the initial production schedule. Orders past the due date will result in costly penalties. To reduce these costs, the repair shop must reschedule its jobs to minimize the total holding cost, setup cost, and penalty cost. Motivated by this real-life problem in the repair shop, we investigate and model a rescheduling problem under disruption.

In this paper, we consider a single-machine rescheduling problem for a repair shop and its manufacturing facility after a prolonged disruption to production. These two parties coordinate production schedules and make joint decisions. Throughout the paper, the two together are referred to as the service provider. The manufacturing facility produces parts for the repair shop, which provides maintenance and repair services to customers. The service provider minimizes tardiness and inventory costs. At the beginning of the disruption, some parts have already been produced. The finished parts incur high holding costs until the entire order is completed, while any unfinished parts (in the form of raw material) incur low holding costs until production starts. The service provider incurs a late penalty cost for orders past the due date. There is a setup cost during production if parts produced consecutively are not the same item type. The service provider's goal is to minimize the total cost, including holding costs, setup costs, and late penalty costs. We design a two-stage genetic algorithm that utilizes the estimation of distribution algorithm. Through numerical tests, we show that this algorithm outperforms a few other genetic algorithms that are designed for scheduling needs.

Note that the problem studied in this paper is more complex than a conventional single-machine scheduling problem that only considers tardiness. First, this paper considers two types of holding costs: the low holding cost of raw materials before production and the high holding cost of finished goods after production. By imposing these holding costs, the model will try to complete an order as fast as possible once the production of the order has started, even if there is plenty of time left until the due date. Second, when rescheduling after the disruption, the model needs to take into consideration those partially completed orders. Parts completed before the disruption incur high holding costs as long as the entire order is incomplete. Thus, at the time of rescheduling, the model must consider the parts produced prior to disruption. To incorporate this feature, we calculate the holding costs starting from the beginning of production after disruption to the time when all orders are completed. Lastly, our model considers the setup costs between different types of production job. When time is abundant, the model will group the same kind of parts together in the production. When time is limited, our model will balance the setup cost against the late penalty cost.

As discussed above, supply chain disruption caused by a social crisis, such as a pandemic, may affect the global supply chain. Another example of a major social crisis is the Russia and Ukraine war, which began in 2022. European countries and the United States imposed sanctions on Russia and suspended all business with the country. As a result, natural gas and crude oil supply have dropped significantly. Other commodities, such as wheat, barley, titanium, nickel, and palladium, have all experienced supply issues as a result of the war (Kilpatrick, 2022). The conflict has also disrupted day-to-day industrial activities in both countries. International logistics that used to travel through these two countries now take detours, resulting in shipment delays. All of these factors lead to disruptions in the global supply chain.

Our model is not exclusively for rescheduling in response to supply chain disruptions caused by social crises. Natural disaster is also a common cause of supply chain disruptions. In August 2005, Hurricane

Katrina struck the Gulf Coast, breaching levees and causing significant damage and thousands of deaths. Power outages and road closures along the Gulf Coast led to severe supply chain disruptions. Businesses had to reroute their supply chains to other areas and reschedule production in alternative plants. It took them months to recover from this disaster. Faced with such rescheduling problems, it is necessary to consider the holding costs of finished goods and unfinished (raw material or work-in-progress) products.

We note that supply chain disruptions caused by social crises and natural disasters may result in severe damage to manufacturing plants, which could delay the production and delivery of orders for weeks, sometimes even months. Nonetheless, in addition to social crises and natural disasters, our model can be applied to any scenario that involves long-term disruption, such as resource shortages. Resource shortages can cause supply and production delays and usually arise from disruptions to transportation. One example of an interruption to raw material transportation is the Suez Canal obstruction of March 2021. The container ship Ever Given was grounded in the world's busiest canal for six days, blocking over 369 ships that were waiting to pass through the canal. It is estimated that 9.6 billion worth of trade was stuck during these six days, causing a massive supply shortage worldwide. Another example of resource shortage is the Colonial Pipeline cyberattack of May 2021. The Colonial Pipeline suffered a ransomware cyberattack that affected its system. The company halted all of its operations to contain the attack, affecting fuel supply to the southeastern United States for many days. This was the largest cyberattack on oil infrastructure in the history of the United States. Similar supply chain disruption incidences can be seen daily, causing delays in the production schedule.

The above examples demonstrate the severe impact of supply chain disruptions and the need for rescheduling. Through proper scheduling and coordination, supply chain costs can be greatly reduced (Hall and Potts, 2003). As we discover from the literature in Section 2, there are various models and algorithms available for rescheduling. However, these existing models are not directly applicable to our context due to the idiosyncratic features we described above, and the algorithms currently available have relatively poor performance, underlining the significance and contribution of our work.

This paper is organized as follows. Section 2 reviews the related literature. In Section 3, we present the rescheduling model with a model extension. In Section 4, we introduce a two-stage genetic algorithm with the estimation of distribution algorithm (EDA) incorporated (we refer to it as EAGA throughout this paper). Section 5 contains the results of numerical tests showing the performance of our algorithm when applied to data from a heavy machinery maintenance service provider. We compare the total cost of the new schedule created using our model with those of the initial schedule. We also compare the performance of the proposed algorithm with five related genetic algorithms. Finally, Section 6 concludes the analysis and results. Future research directions are also suggested in this section.

## 2. Literature review

In this section, we review the related literature. Our work contributes to three areas: single-machine scheduling problems, rescheduling under disruption, and algorithms for scheduling problems.

First, our work is related to single-machine scheduling problems. Graves (1979) discusses two single-machine multi-product scheduling problems with deterministic demand and shows that these problems are identical to a one-warehouse, multiple-retailer inventory problem. Earlier work by Santos and Magazine (1985), Dobson et al. (1987), Naddef and Santos (1987), and Coffman et al. (1990) study singlemachine batch scheduling problems to minimize inventory holding cost. Dobson et al. (1987) and Naddef and Santos (1987) also propose heuristic solutions for their models. In addition to minimizing inventory holding costs, some work includes other costs in the objective function.

Table 1
Comparison between our paper and the reviewed rescheduling papers.

For example, Hall and Potts (2003) study the supply chain scheduling problem of minimizing inventory and delivery costs. Selvarajah and Steiner (2009) study a similar problem, whereby a delivery cost is associated with each batch. They propose approximation algorithms and prove that these algorithms have worst-case bounds.

The second, related area is rescheduling problems under disruption (we summarize and compare the main modeling features of our work and the rescheduling papers in Table 1). The study by Hall and Potts (2004) is one of the earliest papers on rescheduling problems. This work considers a rescheduling problem with a new set of job arrivals that creates a disruption. Liu and Ro (2014) study a rescheduling problem that minimizes a certain cost objective. The manufacturer needs to reschedule the jobs without excessively disrupting the original schedule.

Steiner and Zhang (2011) study a model that reschedules orders with a simultaneous assignment of revised due dates. Their objective is to minimize due date escalation and tardiness penalties for the supplier. Hoogeveen et al. (2012) discuss a model where new jobs arrive during production and the manufacturer needs to reschedule the original and new jobs. The objective is to minimize the makespan and total time deviation. Yin et al. (2016) study the rescheduling problem on parallel machines with multiple machine disruptions. Their objective is to minimize the total completion time and the total time deviation. Some recent papers consider real-time rescheduling, whereby new orders and disruptions constantly arrive, and the schedule needs to be adjusted accordingly. Gao et al. (2018) discuss the rescheduling problem that arises when a high-priority new job is inserted into the production plan. This model considers two objectives: instability and a time index. A heuristics named DJaya is introduced, and numerical tests are done to compare DJaya with other algorithms. Zhang et al. (2021) address the rescheduling problem of a dynamic, flexible job shop with disruptions incorporated. This model considers three objectives (makespan, maximum machine workload, and total tardiness) and a hybrid genetic algorithm is designed for this model. Our work contributes to this stream of literature by capturing the setup costs when switching between job types and the holding cost for partially finished orders.

Another area to which we contribute is algorithms for solving scheduling problems. The current literature contains three main streams of scheduling algorithms: exact algorithms, approximation algorithms, and heuristics (we summarize and compare the scheduling algorithms of our work with those of the reviewed papers in Table 2). Because the scheduling problems are integer-programming problems, most models are NP-hard. Three of the most classic exact algorithms are dynamic programming, branch-and-bound, and cutting-planes. Researchers design new algorithms based on these classic exact algorithms for specific scheduling problems. Bodur and Luedtke (2017) use a mixed-integer rounding technique in the branch-and-cut algorithm to solve stochastic
integer programming scheduling models. Drozdowski et al. (2017) propose branch-and-bound and local search algorithms to solve scheduling problem for a single machine with maintenance restrictions. Kowalczyk and Leus (2017) consider a parallel machine scheduling problem and introduce an exact algorithm based on branch and price that combines multiple algorithms. Emadikhiav et al. (2020) propose a branch-and-check and branch-and-price algorithm to solve a combined routing and scheduling problem. Gmys et al. (2020) introduce an efficient branch-and-bound algorithm that combines dynamic branching and lower bound refinement strategies.

To speed up computation time, people have proposed approximation algorithms to solve for near-optimal solutions. Liu and Ro (2014) study a pseudopolynomial time optimal algorithm, an approximation algorithm, and a fully polynomial time approximation scheme. Levi et al. (2019) develop a class of scheduling models with explorationexploitation tradeoff and introduce approximation algorithms. Baardman et al. (2019) explore the scheduling of promotion vehicles and develop approximation algorithms that achieve a near-optimal result.

In recent years, heuristics have been widely used for scheduling problems. Based on the original genetic algorithm (GA) in Holland (1975), researchers have developed various modifications to GA to improve its solution quality and solving speed. Liu et al. (2016) propose adaptive genetic algorithms (AGA) to solve scheduling problems with due date changes and machine breakdowns. Yu et al. (2018) design a genetic algorithm with an updated decoding process (GAD) to solve a hybrid flow shop scheduling problem. Zhang et al. (2019) design a hybrid adaptive genetic algorithm (HAGA) to solve a task-scheduling problem with limited time and energy resources. Samarghandi (2019) develops a genetic algorithm (GANW) to handle large-scale job scheduling problems with no waiting time. Soares and Carvalho (2020) propose a parallel biased random-key genetic algorithm for a scheduling problem with identical parallel machines. Our paper differs from these papers by proposing an EDA-incorporated two-stage GA (denoted by EAGA), which aims to further improve the efficiency and efficacy in searching for the optimal solution.

Among all related research discussed, Selvarajah and Steiner (2009) is the most relevant to our work on model settings. This work is motivated by the need to reschedule due to production disruptions caused by resource shortages, natural disasters, or social crises. In this paper, we study the rescheduling problem that occurs when a manufacturer produces and supplies replacement parts to a service provider. The service provider processes repair jobs and delivers the finished jobs to the customers. After a major disruption to production, the service provider needs to reschedule its jobs to minimize tardiness and inventory costs. We further extend the model to incorporate cases with some processing time modifications. A two-stage genetic algorithm is then proposed to solve the rescheduling problem. Numerical experiments show that the proposed rescheduling model can effectively reduce tardiness and total

Table 2
Comparison of the algorithms used.
inventory costs. In addition, the proposed algorithm performs better than the five closely-related genetic algorithms in the literature.

## 3. Models

### 3.1. Notation and sequence of events

This model describes a scheduling problem under supply chain disruption. Consider a service provider (consisting of a repair shop and a manufacturing facility) who processes maintenance and repair jobs for its customers. At the beginning of the planning horizon, the service provider receives maintenance and repair orders from its customers. Each order consists of a few replacement parts. All parts are produced by the manufacturing facility and assembled by the repair shop. Since the parts are make-to-order, they cannot be produced before orders arrive. An order is considered complete only when all parts have been produced. In this centralized setting, the service provider needs to generate a production schedule to minimize the total cost (TC), which includes the holding costs and the setup cost. In our model, there are two types of holding cost: a low holding cost for storing raw material or unfinished parts, and a high holding cost for storing the finished products. This assumption is reasonable and common in the automotive and heavy machinery industry. Raw material, such as steel and gearwheels, is usually stored in covered outdoor spaces, whereas finished parts, such as suspension gears and passenger doors, are stored in monitored warehouses with advanced inventory management and security systems. The physical properties of the raw material and finished parts also affect the holding cost. For example, glassware has high holding cost while sand has low holding cost, and heat-treated ingots have a high holding cost while steel has low holding cost (Li et al., 2019). The setup cost is used to capture the price of extra labor and the operational costs for changeovers between job types. When production is initially scheduled, the service provider makes sure that no order will be late. In our model, the parts in each order do not have precedence relationships and parts in the same order do not need to be processed consecutively.

When supply chain disruption occurs, production is interrupted for a period. After production resumes, some orders will miss the due date, thus incurring a late penalty cost. If the service provider continues to follow the initial schedule, the late penalty cost from delayed orders could add up quickly. Thus, the service provider needs reschedule the unfinished orders to minimize the total cost, which now includes the holding cost, the setup cost, and the late penalty cost. To better describe the process, we list the sequence of events below.

1. Before the start of production and servicing, the service provider receives orders from its customers. Each order requires a few replacement parts.
2. Based on the production setup cost $S$, inventory holding cost $H$, and due dates $d$ of each order, the service provider generates a schedule to minimize holding and setup costs. We refer to this schedule as the initial schedule. Note here, the initial schedule does not consider disruption and the late penalty cost.
3. Production starts. Parts are produced one by one according to the initial schedule.
4. Disruption occurs and production is paused. Orders that have been completed before the disruption will be shipped before the disruption. Orders that have not yet been completed before the disruption will need further processing after it.
5. After a period of production downtime, operation resumes. Orders that cannot be completed by the due date will incur a late penalty cost. The service provider reschedules the production sequence to minimize the late penalty cost $P$, setup cost $S$, and inventory holding cost $H$. This is the rescheduling problem we focus on in this paper.
6. Once all required parts from an order have been produced, the service provider performs the maintenance service and ships the completed order to the customer.

Without loss of generality, we set the starting time after disruption as 0 . A negative time indicates that the parts have been produced before the disruption. See Fig. 1 for the timeline of the events. Next, we define the notation used in our model.

Let $M$ denote the number of orders received by the service provider. Order $i$ consists of $N_{i}$ parts. Throughout this paper, we use job to refer to the task of producing one of the parts in an order. Jobs are indexed by subscripts $i j$, where $i$ denotes the order number and $j$ denotes the parts in that order. The completion of job $i j$ only indicates the completion of the $j$ th job in order $i$. The machine cannot process in batches; therefore, an identical job from another order would need to be processed separately. Before disruption occurs, some jobs have already been completed. To simplify the notation, we assume, without loss of generality, that only $N$ jobs ${ }^{2}$ need to be rescheduled in each order. In practice, our model allows for any number of jobs to be rescheduled. One can simply replace $N$ with the exact number of jobs that need to be rescheduled in each order.

In the following, we define the parameters and variables in this model.

- $t_{i j}$ : the processing time of job $j$ in order $i, i=1, \ldots, M, j=$ $1, \ldots, N$.
- $c_{i j}$ : the completion time of job $j$ in order $i$ after rescheduling. For jobs completed before the disruption, we set $c_{i j}=0$.
- $\tilde{c}_{i}=\max \left\{c_{i j}\right\}$ : the completion time of the entire order $i$ after rescheduling.
- $d_{i}$ : the due date of order $i$.
- $\rho$ : the per unit per unit time late penalty cost incurred by the service provider if the firm fails to complete an order by the due date.
- $h_{j j}$ : the per unit per unit time holding cost of a job before processing. The holding cost of raw material is usually lower before processing.
- $h_{H}$ : the per unit per unit time holding cost of a job after processing. The holding cost of finished jobs is usually higher after processing.

[^0]
[^0]:    ${ }^{2}$ Here, we index the jobs that need to be scheduled as jobs 1 to $N$. Since jobs do not have precedence relationships, this index system only simplifies the notation. It will not change the model itself.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Timeline of the events.

- $F$ : the setup cost when switching from one type of job to another. There is no setup cost if the manufacturing facility continues to produce the same type of jobs.
- $a_{i j, g}$ : an indicator parameter to denote if job $i j$ is of type $g$.
$a_{i j, g}= \begin{cases}1, & \text { if } i j \text { is of type } g ; \\ 0, & \text { otherwise. }\end{cases}$
- $G$ : the set of all job types.
- $O=\left\{O_{1}, \ldots, O_{k}, \ldots, O_{M \times N}\right\}$ : an ordered set that denotes the production sequence.
- $x_{i j, k}$ : a binary variable that denotes the position of job $i j$ in the ordered set $O$.
$x_{i j, k}= \begin{cases}1, & \text { if } i j \text { is assigned to the } k \text { th position; } \\ 0, & \text { otherwise. }\end{cases}$
- $C_{k}$ : a variable that defines the completion time of the job in the $k$ th position. $C_{0}=0$.
- $y_{k}$ : a binary variable that denotes if there is a setup after the $k$ th position.
$y_{k}= \begin{cases}1, & \text { if there is a setup after the } k \text { th position; } \\ 0, & \text { otherwise. }\end{cases}$
The service provider needs to determine the production sequence of jobs to minimize the total cost. The total cost consists of three parts, the late penalty cost, the holding cost, and the setup cost. The late penalty cost $P$ can be written as:
$P=\sum_{i=1}^{M} \rho \max \left\{0, \bar{c}_{i}-d_{i}\right\}$.
The inventory cost $H$ can be written as:
$H=\sum_{i=1}^{M} \sum_{j=1}^{N_{i}} h_{H}\left(\bar{c}_{i}-c_{i j}\right)+\sum_{i=1}^{M} \sum_{j=1}^{N} h_{L}\left(c_{i j}-t_{i j}\right)$.
The first part is the holding cost for the completed jobs. The finished goods require a better warehousing environment; thus, the per unit holding cost is higher. This high holding cost is calculated for the parts that are completed, both before and after the disruption, as long as the entire order is not completed. The second part is the low holding cost for the incomplete jobs (the per unit holding cost is low when the inventory is in the raw material stage). Note here, we only consider the holding costs incurred after the disruption. All costs incurred before the disruption are fixed; thus, this should not affect the rescheduling problem.

Lastly, the setup cost $S$ can be written as:
$S=F \sum_{k=1}^{M \times N} y_{k}$.
Again, the setup cost $S$ only includes the setup cost that is incurred after the disruption.

### 3.2. Service provider's rescheduling model

In this section, we formulate the service provider's rescheduling model.

$$
\begin{aligned}
& \min T C(O)=P+H+S \\
& \text { s.t. } \sum_{k=1}^{M \times N} x_{i j, k}=1, \quad \forall i \in\{1, \ldots, M\}, j \in\{1, \ldots, N\} \\
& \sum_{i=1}^{M} \sum_{j=1}^{N} x_{i j, k}=1, \quad \forall k \in\{1, \ldots, M \cdot N\} \\
& C_{k} \geq C_{k-1} \\
& +\left(x_{i j, k-1}+x_{p q, k}-1\right) y_{i j}, \\
& c_{i j} \geq C_{k}-\left(1-x_{i j, k}\right) M, \\
& \forall k \in\{1, \ldots, M \cdot N\}, \forall g \in G \\
& \bar{c}_{i}=\max \left\{c_{i j}\right\}, \\
& \forall i \in\{1, \ldots, M\} \\
& x_{i j, k} \in\{0,1\}, y_{k} \in\{0,1\}, \\
& c_{i j} \geq 0, C_{k} \geq 0 \\
& \forall i, j, k
\end{aligned}
$$

where

$$
\begin{aligned}
& P=\sum_{i=1}^{M} \rho \max \left\{0, \bar{c}_{i}-d_{i}\right\} \\
& H=\sum_{i=1}^{M} \sum_{j=1}^{N_{i}} h_{H}\left(\bar{c}_{i}-c_{i j}\right)+\sum_{i=1}^{M} \sum_{j=1}^{N} h_{L}\left(c_{i j}-t_{i j}\right) \\
& S=F \sum_{k=1}^{M \times N} y_{k}
\end{aligned}
$$

The objective is to minimize the total cost (TC) of a sequence of jobs, which is the sum of the penalty cost, holding costs, and setup cost. Constraint (1a) requires that each job must exist exactly once in the sequence. Constraint (1b) requires that each position in the sequence must correspond to exactly one job. Constraint (1c) calculates the completion time for the job at the $k$ th position. Constraint (1d) relates the completion time of job $i j$ with its assigned position. $M$ is the generic notation for a sufficiently large number, which could take on any value that is larger than the sum of processing times in our model. Constraint (1e) enforces $y_{k}=1$ if there is a setup operation between the $k$ th and the $(k+1)$ th position, and $y_{k}=0$ otherwise. Constraint (1f) defines the completion time of order $i$.

The service provider's model is a mixed integer linear programming problem (MILP) after some simple transformation. The decision variables $x_{i j, k}$ and $y_{i j}$ are constrained to be integers, while variables $c_{i j}$ and $C_{k}$ are continuous. The objective function and constraints are linear or can be written in linear forms. To linearize $P$, one can define new variables $r_{i}$ as a tardiness variable to replace $\max \left\{0, \bar{c}_{i}-d_{i}\right\}$ in $P$ and

add a group of linear inequality constraints:
$r_{i} \geq \bar{c}_{i}-d_{i}$,
$r_{i} \geq 0$.
Constraint (1f) can be replaced with a group of linear inequalities, $\bar{c}_{i} \geq c_{i j}, \forall j$.

Next, we briefly discuss the complexity of our model. We claim that a simplified version of our model is equivalent to a single machinescheduling problem that minimizes total weighted tardiness, denoted by $1 / / \bar{I}$, using the three-field classification of scheduling problems. By setting the holding costs and setup cost to 0 , the objective function becomes minimizing the total tardiness of the orders. As proved by Du and Leung (2017), minimizing the total tardiness on a single machine is NP-hard. With the additional constraints and cost objectives, our model is at least as hard as the $1 / / \bar{I}$ problem. Solving this problem on a large scale using an exact algorithm will be time-consuming.

### 3.3 Model extension

In this part, we discuss an extension of the model to incorporate changes in processing time. In the base model, we assume that the processing time $t_{i j}$ remains the same after a disruption. However, this may not always be the case. After a disruption, it usually takes a while for factories to recover to full production capacity. Thus, the processing time during that transition period could be longer than normal. One example we saw during the COVID-19 pandemic is that factories' productivity dramatically decreases due to insufficient labor resources. Factories are unable to return to their full capacity for productivity until workers are released from quarantine or social-distancing rules are lifted. When production lines have been destroyed in a natural disaster or social crisis, factories have to operate under low levels of productivity while rebuilding new production lines. This reduction in productivity will lead to extended processing times, which could impact the completion time of the orders, thus affecting the total cost. When rescheduling the production sequence under such scenarios, factories need to consider the changes in capacity or productivity.

Consider a case where a factory's productivity is affected following a disruption. In the first $T_{r}$ periods, the factory produces with only a subset of its requisite workers and equipment. Thus, the processing time $t_{i j}^{\prime}$ in the first $T_{r}$ periods becomes $i$ times the original processing time, or $t_{i j}^{\prime}=I t_{i j}$, where $i$ could be any number greater than 1 . Starting from period $T_{r}+1$, the factory is back to its full capacity. The processing time returns to the original processing time, $t_{i j}^{\prime}=t_{i j}$. If a job is scheduled to be processed during the first $T$ periods after disruption, its processing time will be $i$ times the original processing time. However, if the job is scheduled to be processed after period $T_{r}$, its processing time will be normal. Therefore, we introduce a new variable $\left(z_{i j}\right)$ to this model to denote whether or not job $i j$ is scheduled to be completed before time $T_{r}$.
$z_{i j}= \begin{cases}1, & \text { if } c_{i j} \leq T_{r} \\ 0, & \text { otherwise }\end{cases}$
The new processing time for job $i j$ now becomes:
$t_{i j}^{\prime}=I t_{i j} z_{i j}+t_{i j}\left(1-z_{i j}\right)$.
The rest of the notation is kept the same as in Section 3.1.
The rescheduling model for this extension shares the same objective function and constraints with the main model after replacing $t_{i j}$ with $t_{i j}^{\prime}$. The new constraints for this extension are as follows:

$$
\begin{array}{ll}
t_{i j}^{\prime}=I t_{i j} z_{i j}+t_{i j}\left(1-z_{i j}\right), & \forall i, j \\
c_{i j}-T_{r} \leq M\left(1-z_{i j}\right), & \forall i, j \\
T_{r}-c_{i j} \leq M z_{i j}, & \forall i, j \\
z_{i j} \in\{0,1\}, & \forall i, j
\end{array}
$$

$M$ is the generic notation for a sufficiently large number. Constraints (2b) and (2c) guarantee that when $c_{i j} \leq T_{r}, z_{i j}=1$ and when $c_{i j} \geq$ $T_{r}, z_{i j}=0$. Note that since the processing time is no longer a parameter, this model becomes a nonlinear mixed-integer problem. In Section 5, we test our algorithm on this model and present the results.

## 4. Two-stage genetic algorithm

A genetic algorithm, or GA, is a search algorithm inspired by the theory of natural evolution. A GA simulates the process of natural selection, where the best individuals are selected to produce offspring. GA is widely used in optimization and search problems due to its efficiency and has a higher chance of finding the global optimum than other algorithms. However, GA still has shortcomings. There is still some possibility of being trapped into the local optimum and having premature convergence. To overcome this issue, the estimation of distribution algorithms (EDA) is used to guide the search for the optimum employing an explicit probability distribution.

In this section, we propose the EAGA, a two-stage hybrid AGA that combines EDA with an adaptive local search operator. The EAGA works with a set of encoded individuals called a population. Each individual is represented by a string of genes called chromosome. The objective function value used to evaluate an individual is called fitness. The current population generates offsprings through the process of the EAGA. In the first stage of the EAGA, we use the AGA proposed by Liu et al. (2016). The dominant population obtained from the first stage is used as the initial population for the second stage. In the second stage of the EAGA, we use an EDA with an adaptive local search operator to explore the fitness of offspring and update the population until an optimal or near-optimal individual is obtained, or the maximum iteration is reached. The framework of the EAGA is shown in Fig. 2.

The EAGA is designed to greatly reduce the likelihood of the GA converging to a local optimum while still maintaining fast convergence. Specifically, the EDA in the second stage utilizes the global statistical information to ensure the diversity of the population in each generation. The adoption of the adaptive local search operator used in this algorithm guarantees the best individuals are retained in the next generation. We also note that the quality of the initial population heavily impacts the efficiency of the EDA. Thus, to ensure the rate of convergence of the algorithm, we use an AGA in the first stage to generate a high-quality initial population rather than to just randomly generate a population. Therefore, our two-stage algorithm aims to improve the efficiency and efficacy in searching for the optimal solution in contrast to the existing genetic algorithms. In the following parts, we explain the algorithm in detail.

### 4.1. Encoding and initializing the population

Before the EAGA starts the search for the optimal solution, the initial population should be generated. Many papers in job scheduling use a single-layer chromosome-encoding scheme. This approach encodes an individual using one chromosome to represent its job permutation. This encoding scheme works well for problems with simple job sequencing. However, in our model, jobs belong to different types, and we consider the setup cost incurred when switching production between types. The classic, single-layer chromosome-encoding approach is no longer suitable. Thus, we adopt a two-layer chromosome-encoding scheme to represent an individual. Before the upper layer is coded, all jobs (i.e., $\sum N_{i}$ ) from customers are indexed in increasing order. The upper layer represents job permutations, and the lower layer represents the job types (see Fig. 3). In our work, only individuals with a lower total cost after rescheduling will be retained in the initial population to ensure its quality.

![img-1.jpeg](img-1.jpeg)

Fig. 2. The framework of EAGA.

Upper layer


Lower layer


Fig. 3. The two-layer chromosome-encoding scheme.

### 4.2. The first stage of EAGA

The purpose of the first stage is to obtain a high-quality population as the initial population for the second stage. The steps of the first stage are as follows:

1. Define parameters:

- population size, $P s$;
- maximum iteration, iter $_{\max }$;
- the minimum crossover probability, $P c_{\text {min }}$;
- the maximum crossover probability, $P c_{\max }$;
- the minimum mutation probability, $P m_{\min }$;
- the maximum mutation probability, $P m_{\max }$.
Set starting time $T=0$. Encode and initialize population.

2. Calculate the fitness of the individuals within in the population. Use the roulette-wheel selection method to select the parents. The selection probability of the $y$ th individual, $P_{y}$, is calculated using the following function:
$P_{y}=\frac{f_{y}}{\sum_{j=1}^{N} f_{y}}$,
where $f_{y}$ denotes the fitness of the $y$ th individual.
3. Conduct the adaptive crossover operation based on the following crossover probability: $P c$.

$$
P c=\left\{\begin{array}{ll}
P c_{\max }-\frac{\left(P c_{\max }-P c_{\min } \forall f-f_{\text {avg. }}\right)}{f_{\max }-f_{\text {avg. }}}, & f \geq f_{\text {avg. }} \\
P c_{\max }, & \text { otherwise }
\end{array}\right.
$$

where $f, f_{\max }, f_{\text {avg. }}$ denote the larger fitness of the two individuals being crossovered, the maximum fitness of the entire population, and the average fitness of the entire population, respectively.
4. Conduct the adaptive mutation operation based on the following mutation probability $P m$.

$$
P m= \begin{cases}P m_{\max }-\frac{\left(P m_{\max }-P m_{\min } \times f-f_{\text {avg. }}\right)}{f_{\max }-f_{\text {avg. }}}, & f \geq f_{\text {avg. }} \\ P m_{\max }, & \text { otherwise }\end{cases}
$$

5. Update $t=t+1$. If $t<\operatorname{iter}_{\max }$, return to Step 2; otherwise, exit first stage.

In Step 3, the adaptive crossover probability is defined to accelerate evolution speed and increase individual diversities. This approach is adopted from Wang and Tang (2011). After the two chromosomes performed a crossover operation, if the larger fitness is greater than or equal to the population's average fitness (indicating a worse individual), its crossover probability decreases; otherwise, it remains unchanged.

### 4.3. The second stage of EAGA

In the second stage of the proposed algorithm, we search to discover whether better individuals exist. The final population from the first stage is used as the initial population for the second stage. In this section, we first introduce the algorithms used in the process; we then summarize the second stage at the end of this section.

### 4.3.1. Probability model and updating mechanism

Unlike GA, EDA generates offspring by sampling according to a probability model instead of crossover and mutation operators. Thus, the probability model in EDA has a great impact on the performance of the algorithm. In this stage, the probability is modeled by an $n \times n$ probability matrix, as follows:
$P(t)=\left[\begin{array}{llll}p_{11}(t) & p_{12}(t) & \ldots & p_{1 n}(t) \\ \ldots & & \\ p_{n 1}(t) & p_{n 2}(t) & \ldots & p_{n n}(t)\end{array}\right]$
where $p_{j k}(t)$ denotes the probability that job $j$ is processed in the $k$ th position of the sequence in generation $t$. At the beginning of this stage $(t=0)$, we set all $p_{j k}(0)=1 / n$.

In generation $t$, we produce new individuals by sampling from the population using the probability matrix $P(t)$. To ensure that each job is assigned to one and only one position, a parameter $r$ is randomly generated within the range of $(0,1)$. For the $k$ th position, we assign the first job $j$ that satisfies the condition $r \leq \sum_{i=1}^{t} p_{i k}(t)$. To avoid a job $j$ being assigned to other positions after it is already in position $y$, all other $p_{j k}(t)$ is are set to 0 . At the same time, the probabilities of assigning other jobs to position $y$ are also set to 0 . After generating a new individual, its fitness is evaluated. If the fitness after rescheduling is smaller than before rescheduling, the new individual will be retained in the population; otherwise, a new individual will be generated.

Next, we discuss how to update the probability matrix $P(t)$. In the updating mechanism, we select the top $\eta \cdot P s$ individuals from the population as samples to update the probability matrix. Here, $\eta$ is predefined and denotes the proportion of the top individuals in a population and $P s$ denotes the population size. In this paper, an incremental learning method is used to update the probability matrix. Define $\alpha \in(0,1)$ as the learning rate. We update the probability matrix using the following equation:
$p_{j k}(t+1)=(1-\alpha) p_{j k}(t)+\frac{\alpha}{\eta P s} \sum_{i=1}^{n P s} I_{j k}^{i}(t), \quad \forall j, k$
where $I_{j k}^{i}(t)$ is the indicator function of the $i$ th top individual in generation $t$. It is defined as:
$I_{j k}^{i}(t)= \begin{cases}1, & \text { if job } j \text { is assigned to position } k \\ 0, & \text { otherwise }\end{cases}$

### 4.3.2. Adaptive local search operator

An effective local search can dramatically improve the performance of evolutionary algorithms (Wang et al., 2013). The EDA makes effective use of global statistical information rather than local information about individuals during the evolution process (Zhou et al., 2016). An efficient algorithm should find a balance between global information and local information. Therefore, we propose an adaptive local search operator to improve the local search performance of EDA. We mainly consider four local search structures: swap-based structure, insert-based structure, invert-based structure, and double swap-based structure. See Fig. 4 for an illustration of each of the structures. In each structure, the chromosome on the top is original sequence and the chromosome on the bottom is the new sequence after the local search operator.

Compared with the traditional local search, we propose a twostep adaptive local search operator. In the first step, we generate new individuals using the four local search structures and initialize the probability distribution, $Q(0)$, for the local search structure selection in the second step. The process to generate a new individual is as follows:

1. Randomly select a search structure and generate a new individual based on the structure.
2. Compare the fitness of the new individual with the original individual.
3. If the new individual is better, stop. If the old individual is better, randomly select another search structure from the rest of the structures.
4. Repeat 1, 2, and 3 until a better individual is found or all four structures have been tried. If no new individual is found after all four search structures, stop and discard the new individual. Move on to the next individual in the population.

In this process, an individual is only updated if the algorithm finds a new individual that is better than the original one. During the process, we record the number of successful updates of each local search structure $\left(N_{i}, i=1, \ldots, 4\right)$. After all individuals are updated, we define $\hat{q}_{i}(0)$ as follows:
$\hat{q}_{i}(0)=\frac{N_{i}}{\sum_{g=1}^{4} N_{g}}+\delta, \quad \forall i=1, \ldots, 4$.
Here, we manually set $\delta=0.05$ to avoid the probability of any local search structure being initialized to 0 . Then, we normalize $\hat{q}_{i}(0)$ so that the sum of all four probabilities equals 1 . The probability after normalization, $Q(0)=\left\{q_{i}(0)\right\}$, is used to select the local search structures in the next step.

In the second step, we use $Q(0)$ as the starting probability to select a local search structure. This probability is updated during the process using the number of successful individual updates. At the beginning of the second stage, we reset all $N_{i} \mathrm{~S}$ to 0 . The probability of selecting search structure $i$ in generation $t$ is denoted as $q_{i}(t)$. In each generation, $q_{i}(t)$ is updated using the following equation:
$q_{i}(t)=(1-\beta) q_{i}(t-1)+\beta \frac{N_{i}}{\sum_{g=1}^{4} N_{g}}$,
where $\beta \in(0,1)$ is the predefined learning rate. Once we iterate through all the individuals in the population, we stop and exit the algorithm.

### 4.3.3. Process of the second stage

1. Reset $\mathrm{t}=0$. Define the learning rates $\alpha$ and $\beta$ for $P(t)$ and $Q(t)$. Define the top percentage of the population, $\eta$. Initialize probability matrix $P(0)$.

![img-2.jpeg](img-2.jpeg)

Fig. 4. Local search structures.
2. Generate a new population based on $P(0)$ and combine the new and old generation into a temporary population of size $2 P s$.
3. Calculate the fitness of each individual in the temporary population and sort individuals from the best to the worst.
4. Keep the first $P s$ individuals in the temporary population. Apply the two-step adaptive local search operator.
5. Update $t=t+1$. If $t<\operatorname{iter}_{\text {max }}$, return to Step 2. Otherwise, stop and exit the algorithm.

Once the first and second stages have been executed, the EAGA will return a production sequence and its fitness. In the next section, we show the performance of the EAGA and compare it with a few other algorithms from the models presented in Section 3.

## 5. Numerical results

To test the performance of the proposed model and the algorithm, we apply our model to a heavy-machinery service factory in Qingdao, China. In this section, we will discuss the result of the algorithm and compare the performance with a few recent and closely related algorithms used in scheduling and/or rescheduling.

This service factory provides maintenance and repair services to various forms of heavy machinery and automobiles, such as locomotives, cranes, and wheel loaders. Its customers are located in different regions of China. When the heavy machinery or automobiles are due for maintenance or need repair, they are sent to the service factory. The machinery first undergoes a thorough inspection by technicians at the factory, then services are scheduled, and orders for replacement parts are placed. The service factory has a contract manufacturer who produces all the replacement parts. The manufacturer receives orders from the service factory and sends parts to the service factory once production is done. When all parts are installed, and all services are completed, the machinery is sent back to the customer.

We obtain the service request data and production data from this factory. Based on the dataset, we generate some instances as test data. For each instance, we execute ten runs and collect the best fitness, the average fitness, and the worst fitness. The algorithm is coded in $\mathcal{C}^{K}$ and executed on an Intel(R)-i5, 1.6 GHz computer with 4 GB of RAM.

Now, we introduce the parameters used in the numerical experiments. The parameters are approximated from the data gathered from the heavy-machinery service factory where the research project was conducted. In the numerical experiments, we set the parameters as follows:

- Penalty cost $\rho=16$
- Low inventory cost per unit $h_{L}=4$
- High inventory cost per unit $h_{H}=6$;
- Setup cost, $F=6000$
- Minimum mutation probability, $P m_{\max }=0.01$;
- Maximum mutation probability, $P m_{\max }=0.1$;
- Minimum crossover probability, $P c_{\max }=0.6$;
- Maximum crossover probability, $P c_{\max }=0.9$;
- Population size, $P s=50$;
- Percent of top individuals, $\eta=0.1$;
- Learning rate in the probability matrix in the EDA, $\alpha=0.2$;
- Learning rate in the adaptive local search operator, $\beta=0.2$;
- Number of job types, $G=5$.

To show the necessity of using an approximation algorithm, we run our model for a real-life-size problem using CPLEX MILP solver. We compare the efficiency of the EAGA and the exact algorithm from the mixed-integer optimizer. We test our algorithm for order count $M=20$, 50 , and total job count of $\sum N_{i}=1000,1500$. For each instance, we generate five sets of order data. For each set of data, we calculate the percent of improvement from the exact algorithm to the EAGA. At the current problem scale, optimal solutions based on CPLEX are not obtainable within a reasonable amount of time. Thus, we set a fixed computation time of one hour for both algorithms and compare the solution quality. In the numerical experiments, it turns out that EAGA only takes 70 s to 210 s for the cases we tested, while CPLEX reaches the maximum time limit. We use Reduction Percentage (RP) to measure the cost reduction of EAGA when comparing with the exact scheduling algorithms based on CPLEX. Define RP as follows:
$\mathrm{RP}=\frac{\bar{C}-C}{\bar{C}} \times 100 \%$
where $\bar{C}$ is the cost applying the CPLEX-based exact algorithm and $C$ is the cost using our proposed rescheduling algorithm. A negative $R P$ indicates an increase in the cost. The results are listed in Table 3.

Results show that, our algorithm greatly improves the solution quality compared with the exact algorithm in CPLEX. As illustrated in Table 3, the improvement can be up to $20.65 \%$ (that is, EAGA can reduce the cost by $20.65 \%$ ). The overall average improvement is calculated as $12.13 \%$. Thus, when applying this model to a practical scenario, exact algorithms tend to be time-consuming and a suboptimal solution from the exact algorithm could diverge significantly from the actual optimum. In this regard, using an approximation algorithm such as EAGA to solve the focal problem in this paper is necessary.

In the following subsections, we test our models and algorithm under various combinations of order counts and total job counts and compare the results with the initial schedule and various genetic algorithms. Due to the large number of test runs we need to conduct in the numerical experiments, running large datasets will be time-consuming. Thus, the scale of the problem has been reduced in the numerical experiments to gain efficiency.

Table 3
Total cost comparisons between EAGA and CPLEX-based exact algorithm.

### 5.1. Model comparison with the initial schedule

In the numerical experiments, we test 21 combinations of order counts $(M)$ and the total job counts $\left(\sum N_{i}\right)$. The number of jobs in each order is evenly distributed or as close to an even distribution as possible. In each table, the first column is the total number of jobs. The second column is the number of customer orders. We first compare the cost of the rescheduled production sequence with the initial schedule. The initial schedule is calculated at the beginning of the planning horizon (before disruption occurs) by minimizing the total holding cost and setup cost. The penalty cost, holding cost, fixed cost, and RP are shown in Table 4. In this part, when calculating RP, $\bar{C}$ represents the cost of applying the initial schedule to the problem with disruption. The first five columns are the total cost $(T C)$, the total low holding cost $\left(H_{L}\right)$, the total high holding cost $\left(H_{H}\right)$, the total setup cost $(S)$, and the penalty cost $(P)$ of the initial schedule. The next few columns are the costs after rescheduling and the corresponding RP.

From Table 4, we can see that in all cases, the total cost after rescheduling is less than the initial schedule. In most cases, the RP of the total cost after rescheduling is over $20 \%$. When there are more jobs, RP tends to be higher. From the next few columns, we observe that the main contribution of cost reduction is from high holding cost $H_{H}$ and penalty cost $P$. At the same time, $H_{L}$ and $S$ are increasing, indicating that orders with an approaching deadline have higher priorities after rescheduling. Similar jobs that were scheduled consecutively in the initial schedule have to be broken into multiple setup rounds to avoid delays. Jobs from the same order are more likely to be produced in clusters, and the entire order takes less time to finish. Thus, the high holding cost of the finished parts is lower, and the total low holding cost of the raw material is higher.

We also run the same instances for the extension model with the reduced productivity, with $l=2$. The results are shown in Table 5. Again, the first five columns show the costs from the initial schedule. The costs are higher than those in Table 4 because of the longer processing times following the supply chain disruption. The next few columns show the cost after rescheduling. From the table, we can see that rescheduling becomes crucial when processing capacity is limited for a period of time. In most cases, the RP of the total cost after rescheduling is over $25 \%$, and some can go as high as $47 \%$. Under this model, the low holding cost $H_{L}$ and setup cost $S$ increase after rescheduling. The main drivers of the total cost reduction are the high holding cost $H_{H}$ and penalty cost $P$.

### 5.2. EAGA performance comparison with other algorithms

Next, we compare the performance of the EAGA with five closelyrelated genetic algorithms. We apply the following five genetic algorithms to the same scheduling model.

1. the original genetic algorithm (GA) (Holland, 1975)
2. the adjusted genetic algorithm (AGA) (Liu et al., 2016)
3. the hybrid adaptive genetic algorithm (HAGA) (Zhang et al., 2019)
4. the genetic algorithm with updated decoding process (GAD) (Yu et al., 2018)
5. a genetic algorithm for no-waiting scheduling (GANW) (Samarghandi, 2019).

To ensure the performance of each algorithm, we set the algorithmspecific parameters to the suggested values in their original work. Cost parameters are consistent with those used in our EAGA algorithm. Using these five algorithms, we calculate the same rescheduling problem and obtain the best fitness, the average fitness, and the worst fitness for each setting. We use the Improvement Rate (IR) to measure the percent improvement of the EAGA in contrast to other GAs. Here, we calculate the cost reduction of an algorithm by taking the difference between the initial schedule $T C$ and the solution generated by this algorithm $T C_{a l g}$ :
$\operatorname{cost}$ reduction $_{a l g_{i}}=T C-T C_{a l g_{i}}$
Using cost reduction, we define IR as follows:
IR $=\frac{\text { cost reduction }_{E A G A}-\text { cost reduction }_{a l g_{i}}}{\text { cost reduction }_{E A G A}} \times 100 \%$
$=\frac{T C_{a l g_{i}}-T C_{E A G A}}{\text { cost reduction }_{E A G A}} \times 100 \%$.
A positive IR indicates that the EAGA's reschedule solution has a lower cost than the benchmark algorithm. The larger the IR, the better the solution from EAGA in contrast to each specific algorithm.

For each algorithm, we execute ten runs and collect the best fitness, the average fitness, and the worst fitness to undertake the comparison. In Tables 6, 7, and 8, we show the total cost after rescheduling using each algorithm and the Improvement Rate $(I R)$, as defined at the beginning of Section 5. From Table 6, we can see that when the number of jobs is small (below 20), most algorithms converge to the same solution in the best scenario. However, as the number of jobs increases, the advantage of the EAGA begins to show. The EAGA always has a lower total cost than the other five algorithms. As the number of jobs becomes larger, the IR of the EAGA tends to become larger. Even in the best scenario where we only compare the lowest total cost from the ten runs, the IR still ranges from $2 \%-45 \%$. Comparing the five selected algorithms, the classic GA is the worst performer.

A similar pattern was observed in both Tables 7 and 8 . When $N$ is small, most algorithms converge to the same solution. As $N$ becomes larger, the EAGA's cost reduction advantage becomes more evident in all instances. From Table 7 we can see that, on average, the EAGA has the highest improvement when the benchmark is the classic GA, which ranges between $4 \%$ and $49 \%$, depending on the number of total jobs, with the majority falling between $10 \%$ and $40 \%$. The other four algorithms perform better than the classic GA but are still below the EAGA, with the majority of $I R$ falling between $5 \%$ and $18 \%$.

In summary, the rescheduling models proposed in this work will greatly reduce the total cost when disruptions occur in the supply chain. The EAGA substantially outperforms the five closely-related genetic algorithms in all best, average, and worst scenarios. In addition, as the number of jobs becomes larger, the benefit of using the EAGA

Table 4
Total cost breakdown and cost reduction percentage of the main model.

Table 5
Total cost breakdown and cost reduction percentage of the extension model with reduced productivity.

becomes more evident. We compare the computational time of each algorithm under different cases in Fig. 5. The results show that the GANW algorithm has a longer computational time than the others and the classic GA has the shortest computational time. The computational time of our algorithm (the black line) is also sufficiently short and does not increase dramatically along with the number of jobs. The results in Fig. 5, together with our results described above, further demonstrate that the proposed algorithm (i.e., the EAGA) can greatly improve the quality of the solution without sacrificing the computational time.

## 6. Conclusion and future work

In this paper, we focus on a rescheduling problem that arises from supply chain disruption. Supply chain disruptions can occur for various reasons, such as resource shortages, natural disasters, or social crises.

The recent COVID-19 pandemic caused major supply chain disruptions all around the world. Cities were under quarantine for weeks. People were unable to go to work. Factories, including the one we obtained production data from, could not produce at their regular capacities. Because of the supply disruption of raw materials, many industries have suffered from production delays. When production is disrupted at factories, it is crucial to reconsider the production schedule based on customers' order requests and to reschedule production when necessary.

We study a single-machine rescheduling problem where a service provider (consists of a repair shop and a manufacturing facility) produces parts and provides maintenance services to customers in the presence of disruption. When regular production and services are disrupted, the service provider needs to optimally reschedule the jobs to minimize the total cost, including production setup costs, inventory holding costs (high and low, depending on whether production

Table 6
Comparison of the best values between the EAGA and other algorithms.

Table 7
Comparison of the average values between the EAGA and other algorithms.

is completed), and penalty costs for delayed deliveries. We formulate the rescheduling problem using a mixed integer linear program (MILP) model. An extension model with reduced productivity during the disruption recovery stage is also discussed. We design a two-stage genetic algorithm (EAGA), which combines the genetic algorithm with an adaptive local search operator to solve the model and efficiently search for the optimal solution. Our results show that our model greatly reduces the total cost and the EAGA algorithm outperforms a few related genetic algorithms for scheduling.

There are some limitations to our research, which give rise to a number of interesting areas for future work. First, this paper considers a single-machine rescheduling problem, while multiple-machine manufacturing is also common in practice. Our model can be extended to
multiple-machine contexts to solve the rescheduling problems. Second, in this work, we focus on a deterministic model; however, uncertainties that could affect the rescheduling may arise from different parts of the system (for example, raw material and/or labor supply uncertainties during disruptions). In future studies, we could extend our model to capture these uncertainties. For example, to incorporate the stochastic processing time into our model, we could use a probability distribution to model processing times for the same types of jobs. Third, the system we analyzed is a static system where new job arrivals are not considered. In practice, new job arrivals could occur. Depending on the arrival of new jobs (deterministic or stochastic), future research could incorporate corresponding features into the model and make it a dynamic system. For all the proposed model extensions and variations

Table 8
Comparison of the worst values between the EAGA and other algorithms.

![img-3.jpeg](img-3.jpeg)

Fig. 5. Computational time of each algorithm under difference total job counts.
mentioned above, we could explore the performance of the EAGA applied to large-scale datasets.

## Data availability

Test data are randomly-generated using a set of rules defined in the manuscript.

## Acknowledgments

This work was supported by the National Social Science Fund of China [grant number 21AGL015].
