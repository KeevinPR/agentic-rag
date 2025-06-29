# A continuous estimation of distribution algorithm for the online order-batching problem 

Ricardo Pérez-Rodríguez $\cdot$ Arturo Hernández-Aguirre $\cdot$ S. Jöns


#### Abstract

In manual order-picking systems such as picker-toparts, order pickers walk through a warehouse in order to pick up articles required by customers. Order batching consists of combining these customer orders into picking orders. In online batching, customer orders arrive throughout the scheduling. This paper considers an online order-batching problem in which the turnover time of all customer orders has to be minimized, i.e., the time period between the arrival time of the customer order and its completion time. A continuous estimation of distribution algorithm-based approach is proposed and developed to solve the problem and implement the solution. Using this approach, the warehouse performance can be noticeably improved with a substantial reduction in the average turnover time of a set of customer orders.


Keywords Estimation of distribution algorithm $\cdot$ Warehouse management $\cdot$ Order picking $\cdot$ Order batching $\cdot$ Online optimization

## 1 Introduction

Estimation of distribution algorithms (EDA), introduced by Mühlenbein and Paaß [20], have been successfully used to solve complex combinatorial optimization problems. Some papers such as Chen et al. [2], Liu et al. [19], Pan and Ruiz [22] are examples of combinatorial optimization problems.

[^0]Although the loss of diversity and insufficient use of location information of solutions are disadvantages of EDAs, these have been tackled successfully by incorporating other methods such as genetic algorithms (GA) or tabu search (TS) during the evolutionary process. Pérez et al. [23] use this approach. Several works have been done in order to capture the problem structure with more precision, Ganesan et al. [7] and Le Dinh et al. [17] work on this issue. Advanced probabilistic models, which solve combinatorial optimization problems through EDAs, have been proposed to an attempt to integrate higher order interactions to enhance the solution quality. Wang et al. [26] have contributed to research on it.

The order-picking problem is a combinatorial issue. It has been studied and solved through different approaches such as GAs. Öncan's research [21] is in this category. Although important results have been published on orderpicking problems using GAs, the individual's inadequate representation related to combinatorial problems contributes to random changes over the offspring that can disturb the solutions and does not have positive effects on the fitness. Facing that situation, an approach is to manipulate the individual's representation to prevent disorders among variables of the problem. Goldberg et al. [8], Kargupta [14], and Harik [10] offer good examples of this approach. The disadvantage of this approach is that it cannot determine the relationship or interaction between variables of the problem. Another approach consists of using EDAs. The motivation for their use is the identification and exploitation of the interaction among the variables involved in the problem in order to assist in the development of the algorithm. The idea is to learn and benefit from the interaction among variables by estimating the distribution of the population and sample from this distribution of the offspring. Although the interaction may or may not be present, generally, this is explicitly unknown even in simple order-picking warehouses.


[^0]:    R. Pérez-Rodríguez ( $\boxtimes$ ) $\cdot$ A. Hernández-Aguirre

    CIMAT, A. C., Callejón de Jalisco s/n, Mineral de Valenciana, C.P. 36240 Guanajuato, Guanajuato, México
    e-mail: ricardo.perez@cimat.mx
    S. Jöns

    CONACYT, Av. Insurgentes Sur 1582, Crédito Constructor, C.P. 03940 Benito Juárez, Distrito Federal, México

Henn [11] stated that, when different incoming articles are received and stored in unit loads such as pallets or racks and the customers require a few quantities of different articles, the order picking arises [5].

Order-picking systems involving operators are very common in industry. Henn [11] explained that "manual orderpicking systems can be divided into two categories [27]: parts-to-picker, where automated storage and retrieval systems deliver the articles to stationary pickers; picker-to-parts, where pickers normally walk through the warehouse and collect articles." Manual picking systems such as picker-to-parts where the activity of transformation of customer orders into batches (picking orders) is analyzed in this paper. If the number of arriving orders is too large for processing each customer order separately in an appropriate amount of time, customer orders must be combined into batches. It means that different customer orders can be simultaneously released for picking. If the customer orders are available at the beginning of the scheduling, the order batching is called off line batching, but if the customer orders arrive throughout the scheduling, the order batching is known online batching [29]. It means that customer orders become available dynamically over time. Therefore, the orders are not known in advance. At a specific point in time, it is only known if at least one order will arrive. However, no information regarding the number of orders or their characteristics is given. Thus, deciding which orders should be processed directly has to be done without access to information about those orders. In this paper, the online batching where the batches have to be formed based only on known orders is considered.

Although different algorithms have been proposed in order to solve the online order-batching problem successfully, these algorithms have been proposed without consideration for the relationship or interaction that can exist between different customer orders. For this reason and contrary to current research, the aim of this paper is to find a relationship or interaction between different customer orders known and available in order to build better batches for picking. The global idea is to estimate a relationship or interaction among different customer orders through an EDA. We propose the order batching-continuous estimation of distribution algorithm (OBCEDA) to guide the estimation mentioned above on the overall search process. To the best of our knowledge, this kind of algorithm has not been used to tackle the order-batching problem in order-picking warehouses.

## 2 Problem statement

Based on Henn [12], the online order-batching problem and an optimization model are explained below.

The picking process being analyzed here is described in the following way: The operators (pickers) start at a depot, and the
picker walks through the warehouse and picks up articles from different storage locations. Afterwards, the picker returns to the depot and hands over the picked articles. The route considered by the picker in order to find and collect articles in this research is the "S-Shape" route because it is easy to understand and has been widely used in industrial environments. Figure 1 shows an example of the "S-Shape" route for a set of articles to be picked. The black rectangles represent pick locations, i.e., the corresponding locations where articles have to be picked.

The order-picking process is usually done with the help of a picking device. Consequently, different orders can be combined until the capacity of the device is exhausted. The splitting of an order into two or more batches is prohibited, since it would result in additional unacceptable sorting efforts. If the picker has already started a tour, it is completed without interruption.

In this paper, a single order picker is considered, i.e., all batches must be processed one after another. Specifically, in the online batching, there is no information given about how many orders or their characteristics will arrive. The decision, which orders should be processed directly, has to be made without considering information about future incoming orders. The point in time when an order becomes available is called arrival time. The start time (release time) of a batch is the point in time when an order picker starts to process this batch. The start time of an order is identical to the start time of the batch the order is assigned to. The point in time when the order picker returns to the depot after collecting all articles is called completion time of a batch or of an order. The (customer order) waiting time can be determined as the length of the time between the arrival time and the start time of an order. The turnover time (response time) is the amount of time for which an order stays in the system, i.e., the time period between the completion and the start time of an order. This paper focuses on minimizing the average turnover time of all customer orders. All algorithms for the online order-batching problem, which are analyzed in the literature review section below, form and release batches without having complete information on the types and the arrival times of future orders. Therefore, when a set of unprocessed orders arrives and an order picker becomes available, those unprocessed orders can be grouped into one or more batches that should be released directly, or its start should be postponed to a later point in time.

Let $n$ be the number of customer orders known,
$m$ the number of batches to be processed,
$a_{i}$ the arrival time of order $i$ for all $i \in\{1, \ldots, n\}$,
$k_{i}$ the number of articles of order $i$,
$K$ the maximal number of articles that can be included in any batch (device capacity),
$S_{j}$ the start time of the batch $j$ for all $j \in\{1, \ldots, m\}$

Fig. 1 Example of "S-shape" route
![img-0.jpeg](img-0.jpeg)
$E_{j}$ the end time of the batch $j$ for all $j \in\{1, \ldots, m\}$ $x_{j i}=\{1$ if order $i$ is assigned to batch $j, 0$ otherwise $\}$

An optimization model can be formulated as follows.
The main idea is to minimize the average turnover time that can be defined by
$\frac{\sum_{j=1}^{m} E_{j}-S_{j}}{m}$

Equation (2) ensures the assignment of each order to exactly one batch. It is possible by means
$\sum_{j=1}^{m} x_{j i}=1, \forall i \in\{1, \ldots, n\}$

Inequalities (3) guarantee that the capacity of the picking device is not violated with
$\sum_{i=1}^{n} k_{i} x_{j i} \leq K, \forall j \in\{1, \ldots, m\}$

The conditions (4) indicate that a batch is started after all customer orders assigned to that batch are known using
$S_{j} \geq \max \left\{a_{i} \cdot x_{j i}\right\}, \forall i \in\{1, \ldots, n\}, \forall j \in\{1, \ldots, m\}$

From Eq. (5) follows that a batch is started after the previous one is completed by means
$S_{j} \geq E_{j-1} \forall j \in\{2, \ldots, m\}$

Finally,
$S_{j} \geq 0$
$x_{j i} \in\{0,1\}$

## 3 Literature review

Henn [11] detailed a discussion about the most current research on the order-batching process. A part of that discussion is outlined below.

Kamin [13] analyzed a practical batching problem where greeting cards are retrieved from a warehouse. Pickers use automated-guided vehicles on a fixed course collecting the items according to given customer orders. Those orders arrive throughout the study horizon, and this research focuses on the minimization of average turnover times.

Chew and Tang [3] focus on the optimal number of customer orders that should be assigned to a batch such that the average turnover time is minimized. They employ a queuing network with two queues. In the first queue, customer orders arrive according to a Poisson process and batches are generated by means of the first come first serve (FCFS) rule. If a

particular number of customer orders are in the first queue, those orders are assigned to a batch and move onto the second queue. Those orders are released according to the availability of pickers.

A study of the average turnover time of a random customer order for a two-block layout is carried out by Le-Duc and de Koster [18]. A corresponding model for all customer orders arriving during a particular time interval are assigned to batches in a two-block layout is presented by van Nieuwenhuyse and de Koster [25].

Yu and de Koster [29] explain an order-picking area that is divided into several zones of identical size. The articles of each batch are picked up sequentially by zones. For this picking process, the researchers give an estimation of the average turnover times and observe that an optimal batch size exists.

Henn [12] describes an online order-batching problem in a walk-and-pick warehouse in which the completion times of all (dynamically arriving) customer orders (or the makespan) are to be minimized. The author also shows modifications of solution approaches for offline order batching in order to deal with the online situation.

Öncan [21] introduces a GA for the order-batching problem considering traversal and return routing policies. The proposed GA is tested on randomly generated instances and compared with the well-known savings algorithm. According to the author's extensive computational experiments, we can say that the proposed GA yields promising solutions in acceptable computation times.

The main characteristic in all this current research is the common representation of the solution. The authors employ discrete vectors where the number of elements equals the total number of orders to pick up and where each element contains an integer value that represents the batch to be assigned. In addition, the traditional evolutionary operators used in current research do not try to learn about the relationship between variables. These were not built for that purpose.

Although different algorithms have been proposed in order to solve the online order-batching problem successfully, EDAs have not been considered in this perspective. To the best of our knowledge, this kind of algorithm has not been used to tackle the order-batching problem in order-picking warehouses.

## 4 OBCEDA—for the online batching problem

EDA is a relatively new paradigm in the field of evolutionary computation. Compared with other evolutionary algorithms, the EDA reproduces new population implicitly instead of using traditional evolutionary operators. In the EDA, a probability model of the most promising area is built by statistical information based on the search experience, and then the probability model is used for sampling to generate new
individuals. The EDA makes use of the probability model to describe the distribution of the solution space. The updating process reflects the evolutionary trend of the population [16].

The OBCEDA is proposed and explained to solve the online order-batching problem in this section. We introduce the solution representation, population initialization, a weakness approach of the probability model, and the probability model proposed.

### 4.1 Solution representation

In this paper, a solution to the online batching problem previously mentioned is expressed by the assignment of customer orders to batches, i.e., an order assignment vector represents a solution where the number of elements equals the total number of orders to pick up, where each element contains a random value $U[0,1]$, an important difference between our approach and others. This representation is shown in Fig. 2 with 10 orders. This continuous vector does not have a real meaning on the solution that it represents.

### 4.2 Generation of the population

Initial population members are generated randomly in order to enable a wide range of solutions [9].

### 4.3 A weakness approach of the probability model

A primary approach for the probability model is to design a probability matrix, i.e., a batch probability matrix. The element $p_{j i}$ of the probability matrix would represent the probability that batch $j$ were used for the $i$ customer order. For all $j(j=1, \ldots, m)$ and for all $i(i=1, \ldots, n)$. The value of $p_{j i}$ would indicate the opportunity of a customer order on a certain batch. Via sampling according to the probability matrix, new individuals could be generated. For every position $i$, batch $j$ would be selected with the probability $p_{j i}$. If batch $j$ has already been filled according to the device capacity, it would mean the assignment of batch $j$ has been finished. Then, the whole column $p_{j 1}, p_{j 2}, \ldots, p_{j i}$ of the probability matrix would be set as zero. This updating mechanism would consider the previous assignments. Although in this approach, the probabilistic model would be updated each time an order is assigned in a batch and this updating would eliminate the possibility of choosing a previous batch, a modification in the sampling process has to be carried out if we would set as zero the whole column of probability matrix mentioned above. In addition, this approach does not consider if exists a relationship between the previous position result and the current position result.

To demonstrate the weakness of the approach above, different trials were carried out assuming that there is no relationship between customer orders. The performance obtained was


compared with the continuous approach proposed in this research, and these are shown in Section 5. The continuous approach proposed is explained below.

### 4.4 Probability model proposed

In order to avoid modifying the sampling process mentioned above and to demonstrate that there is a relationship between customer orders, we adopted a continuous optimization procedure instead of a discrete one to solve the online batching problem. This is an important difference between this approach and the current research. The advantage of this representation for each individual, through continuous values, is that they do not have direct meaning to the solution they represent. There is no problem if each individual does not explicitly shows its information on the sequence of batches to be processed. It is not necessary that the probabilistic model be updated each time an order is assigned in the batch sequence, and it is not necessary to make any modification in the sampling process. Rudolph [24] and Bean and Norman [1] can be consulted about continuous optimization procedures. We used the MIMIC ${ }_{C}^{G}$ algorithm to build the probabilistic model introduced by Larrañaga et al. [15]. It is an adaptation of the MIMIC algorithm presented by De Bonet et al. [4] to continuous domains. The MIMIC ${ }_{C}^{G}$ algorithm uses a chain structured probabilistic model where the probability distribution of all the variables except the head node is conditioned on the value of the variable preceding them in the chain. It means
a marginal univariate function and $n-1$ pairs of conditional density functions to build the probabilistic model. Thus, the current position result for any customer order is conditioned to the previous position result.

Once the individuals have been generated from the algorithm MIMIC ${ }_{C}^{G}$, they must be decoded to be represented as a valid batch sequence. Hence, we need a method to decode these real vectors into discrete vectors. Figure 3 details an example of a real vector and its decoding.

The major procedure of the OBCEDA is listed as follows:
Step 1. Set the generation index $g=0$. Initialize an initial population $S(0)$ of size $M$.
Step 2. Select a subset $D$ from $S(g)$ of size $N$, where $N \leq$ $M$.
Step 3. Establish a probabilistic model $P$ according to $\mathrm{MIMIC}_{C}^{G}$, which describes the distribution characteristics of $D$.
Step 4. Generate a set $K$ of new individuals by sampling $P$.

Step 5. Select the best individuals from $K \cup S(g)$ and assign them to the next generation $S(g+1)$.
Step 6. Let $g=g+1$. If $g<\mathrm{GN}$, where GN is the maximum number of generations return to step 2. Otherwise, output the best solution in $S(g)$.

Figure 4 details the overall OBCEDA process, and Fig. 5 depicts a flowchart about the algorithm process.

Fig. 3 Representation of an individual to a valid batch sequence


Step 1. Find the minimum value. Assign to batch


Step 2. Find the next minimum value. Assign to batch if the capacity device is available. If not, assign to another batch


Step 3. Return step 2 until all customer orders have been assigned to


![img-1.jpeg](img-1.jpeg)

Fig. 4 The OBCEDA algorithm

## 5 Results and comparison

A GA is proposed as a benchmark for comparison with the OBCEDA scheme. GA works with tournament selection. The "edge recombination operator" is used as a cross operator based on Whitley et al. [28], and a mutation operator changes batches among different positions.

A TS based on Henn [11] is utilized as a benchmark for comparison with the OBCEDA scheme, too. For the local search phase, we implemented the operator "swap move," meaning the interchanging of two customer orders from different batches. A tabu list is built on 10 neighbors at most.

We used a Dell ${ }^{\circledR}$ Vostro $^{\circledR} 3500$ computer, Intel ${ }^{\circledR}$ Core $^{\mathrm{TM}} \mathrm{i} 3$ processor, 2.6 GHZ, 4 GB of RAM, Windows ${ }^{\circledR} 7$ for 64 bits to run each algorithm. The algorithms have been encoded in DevC++ ${ }^{\circledR}$.

To account for the stochastic nature of the order-picking warehouse, we ran 50 trials for the algorithms where 75 individuals belong to each generation. Each trial contains a stop criterion. It means that any trial returns the optimal vector when the difference between the average fitness of the trial and the best is $<5 \%$.

We established a workload to evaluate and find the best average turnover time. The workload mentioned contains different customer orders, due dates, and differing types of articles required in a workday, replicating the order-picking process conditions. Each corresponding customer order includes different numbers of articles. The arrival times of the customer orders are indeterminable. Our experiments were
based on a single-block warehouse with two cross aisles. It is assumed that there is one in the front and one in the back of the picking area. This layout was used by Henn [11]. As the author explains, the picking area consists of 900 storage locations, where a different article has been assigned to each storage location. The storage locations are arranged into 10 aisles with 90 storage locations each. The aisles are numbered from 1 to 10 ; aisle 1 is the leftmost aisle and aisle 10 the rightmost one. The depot is in the lefthand corner of the warehouse. We further assume that an order picker walks through 10 storage locations in 30 s , and they need 10 s to search and collect an article from a storage location. For the capacity of the picking device $K_{c}$ we assume two different values, namely, 45 and 75 articles. For the routing strategy, the "S-Shape" route was used. For an order, we choose the quantity of articles uniformly distributed in $\{5, \ldots, 25\}$, resulting in three or five orders per batch on average, in accordance with the aforementioned capacities of the picking device. For the total number of orders $n_{c}$ we consider 30 and 60. The orders should arrive within a planning period of 8 h . The inter-arrival times, i.e., the time between the arrival of order $i$ and order $i+1$, are exponentially distributed with a parameter $\lambda$ called arrival rate. Let $X(t)$ be the number of incoming orders in the time interval $[0, t]$. In the case of exponentially distributed inter-arrival times $E[X(t)]=\lambda t$ holds. In our numerical experiments, we choose $\lambda$ in a way that the expectation $E[X(t)]$ is equal to $n$ for $t=8[h]$. In summary, we use the following values for $\lambda$ : for $n=30$, $\lambda=0.08625$; for $n=60, \lambda=0.125$.

![img-2.jpeg](img-2.jpeg)

MAX - Number of generations
Fig. 5 The algorithm process

As a response variable for the experiment, we measure the relative percentage increase (RPI)
$\operatorname{RPI}\left(c_{i}\right)=\left(c_{i}-c^{*}\right) / c^{*} \times 100$
where $c_{i}$ is the average turnover time obtained in the $i$ th replication by a given algorithm configuration, and $c^{*}$ is the best objective value found by any of the algorithm configurations. Note that, for this problem, there are no known effective exact techniques and comparing against an optimum solution is not possible.

Table 1 details the average obtained for each trial when the total number of orders is 30 and the $K$ capacity is 45 articles. We analyze the performance between averages of GA and OBCEDA algorithms.

As we can see in Table 1, there is a significant difference between the averages of both algorithms. The performance of OBCEDA was superior in 28 of the 50 trials.

Table 2 shows the variance obtained for each trial. We analyze whether there is a statistically significant difference between variances of both algorithms.

According to Table 2, there is no statistically significant difference between variances of both algorithms. The performance was the same in 50 of the 50 trials with $\alpha=0.01$ of significance level. We consider that the stability of both algorithms is practically the same ( $100 \%$ of the time).

Table 3 details the average obtained for each trial when the total number of orders is 30 and the $K$ capacity is 75 articles. We analyze the performance between averages of GA and OBCEDA algorithms.

On Table 3, there is a significant difference between the averages of both algorithms. The performance of OBCEDA was superior in 46 of the 50 trials.

Table 4 shows the variance obtained for each trial. We analyze whether there is a statistically significant difference between variances of both algorithms.

As we can see in Table 4, there is no statistically significant difference between variances of both algorithms. The performance was the same in 50 of the 50 trials with $\alpha=0.01$ of significance level. We consider that the stability of both algorithms is practically the same ( $100 \%$ of the time).

Table 5 details the average obtained for each trial when the total number of orders is 60 and the $K$ capacity is 45 articles. We analyze the performance between averages of GA and OBCEDA algorithms.

Based on Table 5, there is a significant difference between the averages of both algorithms. The performance of OBCEDA was superior in 29 of the 50 trials.

Table 6 shows the variance obtained for each trial. We analyze whether there is a statistically significant difference between variances of both algorithms.

Table 1 Comparison of results for each average with $n=30, K=45$

Table 2 Comparison of results for each variance with $n=30, K=45$

*There is no statistically significant difference between samples

Table 3 Comparison of results for each average with $n=30, K=75$

Table 4 Comparison of results for each variance with $n=30, K=75$

*There is no statistically significant difference between samples

Table 5 Comparison of results for each average with $n=60, K=45$
Table 6 Comparison of results for each variance with $n=60, K=45$

*There is no statistically significant difference between samples

According to Table 6, there is no statistically significant difference between variances of both algorithms. The performance was the same in 50 of the 50 trials with $\alpha=0.01$ of significance level. We consider that the stability of both algorithms is practically the same ( $100 \%$ of the time).

Table 7 details the average obtained for each trial when the total number of orders is 60 and the $K$ capacity is 75 articles. We analyze the performance between averages of GA and OBCEDA algorithms.

On Table 7, there is a significant difference between the averages of both algorithms. The performance of OBCEDA was superior in 37 of the 50 trials.

Table 8 shows the variance obtained for each trial. We analyze whether there is a statistically significant difference between variances of both algorithms.

Based on Table 8, there is no statistically significant difference between variances of both algorithms. The performance was the same in 50 of the 50 trials with $\alpha=0.01$ of significance level. We consider that the stability of both algorithms is practically the same ( $100 \%$ of the time).

The same GA is used for comparison with the primary approach, i.e., batch probability matrix in the same stochastic nature of the order-picking warehouse.

Table 9 details the average obtained for each trial when the total number of orders is 30 and the $K$ capacity is 45 articles. We analyze the performance between averages of both algorithms.

As we can see in Table 9, there is no a significant difference between the averages of both algorithms.

Table 10 shows the average obtained for each trial when the total number of orders is 30 and the $K$ capacity is 75 articles. We analyze the performance between averages of both algorithms.

On Table 10, there is no a significant difference between the averages of both algorithms.

Table 11 details the average obtained for each trial when the total number of orders is 60 and the $K$ capacity is 45 articles. We analyze the performance between averages of both algorithms.

According to Table 11, there is no a significant difference between the averages of both algorithms.

Table 12 shows the average obtained for each trial when the total number of orders is 60 and the $K$ capacity is 75 articles. We analyze the performance between averages of both algorithms.

Based on Table 12, there is no a significant difference between the averages of both algorithms.

Table 13 details the average obtained for each trial when the total number of orders is 30 and the $K$ capacity is 45 articles. We analyze the performance between averages of TS and OBCEDA algorithms.

As we can see in Table 13, there is no a significant difference between the averages of both algorithms. The performance of OBCEDA was almost equal to the TS performance.

Table 7 Comparison of results for each average with $n=60, K=75$
Table 8 Comparison of results for each variance with $n=60, K=75$

*There is no statistically significant difference between samples

Table 9 Comparison of results for each average

Table 10 Comparison of results for each average
Table 11 Comparison of results for each average
Table 12 Comparison of results for each average
Table 13 Comparison of results for each average with $\mathrm{n}=30, \mathrm{~K}=45$
Table 14 shows the variance obtained for each trial. We analyze whether there is a statistically significant difference between variances of both algorithms.

According to Table 14, there is no statistically significant difference between variances of both algorithms. The performance was the same in 50 of the 50 trials with $\alpha=0.01$ of significance level. We consider that the stability of both algorithms is practically the same ( $100 \%$ of the time).

Table 15 details the average obtained for each trial when the total number of orders is 30 and the $K$ capacity is 75 articles. We analyze the performance between averages of TS and OBCEDA algorithms.

In Table 15, there is no a significant difference between the averages of both algorithms. The performance of TS was almost equal to the OBCEDA performance.

Table 16 shows the variance obtained for each trial. We analyze whether there is a statistically significant difference between variances of both algorithms.

As we can see in Table 16, there is no statistically significant difference between variances of both algorithms. The performance was the same in 50 of the 50 trials with $\alpha=0.01$ of significance level. We consider that the stability of both algorithms is practically the same ( $100 \%$ of the time).

Table 17 details the average obtained for each trial when the total number of orders is 60 and the $K$ capacity is 45 articles. We analyze the performance between averages of TS and OBCEDA algorithms.

Based on Table 17, there is no a significant difference between the averages of both algorithms. The performance of OBCEDA was equal to the TS performance.

Table 18 shows the variance obtained for each trial. We analyze whether there is a statistically significant difference between variances of both algorithms.

According to Table 18, there is no statistically significant difference between variances of both algorithms. The performance was the same in 50 of the 50 trials with $\alpha=0.01$ of significance level. We consider that the stability of both algorithms is practically the same ( $100 \%$ of the time).

Table 19 details the average obtained for each trial when the total number of orders is 60 and the $K$ capacity is 55 articles. We analyze the performance between averages of TS and OBCEDA algorithms.

In Table 19, there is no a significant difference between the averages of both algorithms. The performance of TS was equal to the OBCEDA performance.

Table 20 shows the variance obtained for each trial. We analyze whether there is a statistically significant difference between variances of both algorithms.

Based on Table 20, there is no statistically significant difference between variances of both algorithms. The performance was the same in 50 of the 50 trials with $\alpha=0.01$ of significance level. We consider that the stability of both algorithms is practically the same ( $100 \%$ of the time).

Table 14 Comparison of results for each variance with $n=30, K=45$

*There is no statistically significant difference between samples

Table 15 Comparison of results for each average with $n=30, K=75$
Table 16 Comparison of results for each variance with $n=30, K=75$

*There is no statistically significant difference between samples

Table 17 Comparison of results for each average with $n=60, K=45$
Table 18 Comparison of results for each variance with $n=60, K=45$

*There is no statistically significant difference between samples

Table 19 Comparison of results for each average with $n=60, K=75$
Table 20 Comparison of results for each variance with $n=60, K=75$

*There is no statistically significant difference between samples

## 6 Discussion

On robustness, the algorithms utilized in this research are not able to handle invalid or unexpected inputs. These have not been encoded for specific users. This topic has not been considered in this research because it is not the main objective. However, the OBCEDA algorithm proposed can be modified in order to get a useful module for specific users in industry.

On convergence and diversity, the algorithms used in this research keep diversity to incorporate specific operators such as the mutation operator in GA and TS in the evolutionary progress. Those operators are useful on permutation-based problems. In addition, any trial returns the optimal vector until the difference between the average fitness of the trial and the best is $<5 \%$.

On stopping criteria, we changed the stopping criterion used previously where a number of generations had to be reached because the disadvantage is that the number of function evaluations necessary for convergence is unknown a priori. Therefore, we used the difference between the average fitness of the trial and the best as a stopping criterion.

On computational time and cost, these were not considered in this research because the algorithm proposed is currently in the prototype phase. Future research work would consider a module for users, and it should include computational time and cost aspects.

On advantages and disadvantages of the proposed method, we can consider that it takes into account the relationship or interactions among variables of the problem as an advantage. For each generation, we know the probability that batch $j$ was used for the $i$ customer order. However, the probabilistic model used could be basic; it may be a disadvantage if we need to model higher interactions.

On global optimum, note that for this problem, there are no known effective precise techniques and a comparison with an optimum solution is not possible. It is a characteristic of the online optimization topic.

On computational complexity, the online order-batching problem is as $N P$ hard as the offline problem type based on Gademann and van de Velde [6], if the number of orders per batch is greater than two.

On feasibility and flexibility, on the one hand, all the algorithms used in this research were able to produce feasible solutions according to different constraints detailed in the problem statement section of this paper. It was not necessary to repair the solutions as other algorithms used for permutation-based problems. The proposed method considers the previous results in order to avoid unfeasible solutions. On the other hand, the algorithms utilized in this research are not flexible to handle new and unexpected customer orders. The proposed method is currently in the prototype phase for users.

On efficiency and effectiveness, in this research, the amount of resources used by all the algorithms was not
considered, e.g., the requirement for high speed or for minimum memory usage were of no interest.

On reliability and user friendliness, all the algorithms were tested in order to get reliability according to the online orderbatching characteristics. However, these are not industryready yet.

On exploitative and exploration capability, all the algorithms used in this research keep exploitative and exploration capability to incorporate specific operators such as cross and mutation operator in GA and TS in the evolutionary progress.

## 7 Conclusions

Based on the experimental results shown, we confirmed that an appropriate modeling of the most important variables that affect the performance of the picking process should be considered in the proposed solution. We reach the conclusion that the order-picking performance can be improved if we take into account the relationship or interaction among variables of the problem. Using a continuous EDA was not necessary to make any modifications in the sampling process in the processing sequence of customer orders on the batches, as is generally required by other algorithms. It allowed for better trust in the data against the GA. The OBCEDA considers the previous assignments like an updating mechanism to detect the relationship between customer orders and was able to tackle the individual's inadequate representation related to combinatorial problems used in GAs. We conclude that the OBCEDA can be an efficient mechanism to handle different order-picking conditions where there are diverse variable interactions such as the online batching problem.

Although the difference between the TS and OBCEDA performances was not statistically significant, future research work will use higher probabilistic models in order to model higher interactions or relations between variables of the orderpicking performance. Finally, this research contributes using an EDA as an optimization method for any order-picking process.

Acknowledgments We would like to express our gratitude to Elizabeth O'Shaughnessy for reviewing the manuscript.
