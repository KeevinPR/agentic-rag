# Modeling stochastic service time for complex on-demand food delivery 

Jie Zheng ${ }^{1}$ (D) $\cdot$ Ling Wang ${ }^{1}$ (D) $\cdot$ Shengyao Wang ${ }^{2} \cdot$ Jing-fang Chen ${ }^{1}$ (D) $\cdot$ Xing Wang ${ }^{1} \cdot$ Haining Duan ${ }^{2} \cdot$ Yile Liang ${ }^{2} \cdot$ Xuetao Ding ${ }^{2}$<br>Received: 6 October 2021 / Accepted: 5 March 2022 / Published online: 29 April 2022<br>(c) The Author(s) 2022


#### Abstract

Uncertainty is everywhere in the food delivery process, which significantly influences decision-making for complex ondemand food delivery problems, affecting delivery efficiency and customer satisfaction. Especially, the service time is an indispensable part of the delivery process impacted by various uncertain factors. Due to the simplicity and high accuracy requirement, we model the uncertain service time as a Gaussian mixture model (GMM). In detail, we transform the distribution estimation problem into a clustering problem by determining the probability of each data belonging to each component (each cluster as well). A hybrid estimation of distribution algorithm is proposed to intelligently solve the clustering problem with the criterion to optimize quality and simplicity simultaneously. First, to optimize the simplicity, problem-specific encoding and decoding methods are designed. Second, to generate initial solutions with good clustering results, a Chinese restaurant process-based initialization mechanism is presented. Third, a weighted-learning mechanism is proposed to effectively guide the update of the probability model. Fourth, a local intensification based on maximum likelihood is used to exploit better solutions. The effect of critical parameters on the performances of the proposed algorithm is investigated by the Taguchi design of the experimental method. To demonstrate the effectiveness of the proposed algorithm, we carry out extensive offline experiments on real-world historical data. Besides, we employ the GMMs obtained by our algorithm in a real-world on-demand food delivery platform, Meituan, to assist decision-making for order dispatching. The results of rigorous online A/B tests verify the practical value of introducing the uncertainty model into the real-life application.


Keywords Complex on-demand food delivery $\cdot$ Stochastic service time modeling $\cdot$ Gaussian mixture model $\cdot$ Hybrid estimation of distribution algorithm

## Introduction

Under the prosperous development tendency of e-commerce, on-demand food delivery (OFD) service has become a wave worldwide. In recent years, many OFD platforms have sprung up all over the world, such as Meituan (China), Grubhub (USA), Deliveroo (UK), and Swiggy (India). According to the Statista Digital Market Outlook, the global revenues of

```
\square \text { Ling Wang}
    wangling@mail.tsinghua.edu.cn
    Jie Zheng
    j-zheng18@mails.tsinghua.edu.cn
    Shengyao Wang
    wsy06@aliyun.com
    Jing-fang Chen
    cjl17@mails.tsinghua.edu.cn
    Xing Wang
    wang-x17@mails.tsinghua.edu.cn
```

the OFD service have increased from US\$91 million in 2018 to US $\$ 107$ million in 2019 [1]. Taking Meituan platform as an example, about 4 million riders, 6.5 million restaurants, and 400 million customers are active on the platform in 2020 [2]. Overall, OFD service has high user demands and abundant market opportunities.

```
Haining Duan
duanhaining@meituan.com
Yile Liang
liangyile@meituan.com
Xuetao Ding
dingxuetao@meituan.com
1 Department of Automation, Tsinghua University, Beijing
100084, China
2 Meituan, Beijing 100102, China
```

Figure 1 shows the entire complex process of OFD platforms to deliver an order, which can be described as two phases: system scheduling and order delivering. In the system scheduling phase, the computing systems of platforms will decide which rider each order should be assigned to as well as plan the best route for each rider based on the collected global information, such as the information of all orders, riders, customers, and restaurants, as shown in Fig. 2. To be specific, after customers order their favorite food, platforms will inform corresponding restaurants to confirm as well as prepare food. Afterward, platforms will simulate the real delivery process, plan routes by heuristics, and evaluate the objectives of assigning each new order to each rider based on the planned route. Finally, platforms will dispatch orders to appropriate riders (usually with minimum total time) and inform them to confirm the delivery tasks.

After systems make satisfactory decisions, it enters the actual order delivering phase, where riders will head to restaurants to pick up food and ride to the locations of customers. Usually, riding is prohibited in or around buildings. Therefore, riders need to stop riding if they are near the customers' buildings, walk to customers' homes or workplaces, and hand food to customers. The total time of delivering an order can be described as the time from when the rider confirms the order to when the rider hands the food to the customer. It consists of three parts: (1) Pickup time: the time from when riders arrive at restaurants to when they leave. (2) Travel time: the time that riders cost on the route. (3) Service time: the time from when riders stop riding and enter customers' building to when they leave the customers' building and start riding. If the three parts can be estimated precisely in the system scheduling phase, platforms can accurately assess the total time of order assignment and make optimal decisions.

Among the three parts, the service time is of special significance, because it is required for many decision-makings in OFD service. The most important application is to assess the total time for the system scheduling. In addition, based on the statistics of service time, platforms can also adjust riders' wages, modulate delivery priorities of orders, and judge whether and where to install self-help dining cabinets, etc. In general, the service time of an order is unknown until it has been finished, but most decisions need to be made before the order delivery phase.

Therefore, predicting or modeling service time plays an important and indispensable part in OFD service. However, in the current scheduling process of Meituan, the service time is assumed as a deterministic value, which leads to inaccurate estimation of objectives and wrong decisions. Besides, to the best of our knowledge, many research works focus on predicting or modeling travel time [3] and food preparation time [4], but few on service time. Most researchers assume that the service time is already known [5, 6]. To fill
up this gap, we intend to study the modeling and estimation of service time for OFD platforms. Usually, it is difficult to accurately estimate the service time of each order, because uncertainty is inevitable and pervasive throughout the service process. The service time will be prolonged if riders encounter various unexpected scenarios. For example, riders must stop riding and walk for a long distance in some villages that prohibit vehicles from entering. Besides, riders need to run up and down the stairs in some old residences without elevators. Even if there are elevators, riders sometimes must wait for a while to get on an elevator in office buildings with a high crowd flow. In addition, for serving the customers whose addresses are not clearly registered, it will take riders a lot of time to look for the particular position. These scenarios may happen all the time. However, it is hard to predict whether these scenarios will happen and how long it will take once any scenario happens for OFD platforms. Thus, predicting or modeling service time is a challenging task for OFD platforms.

There are many research works on the application of uncertain service time in scheduling problems. Some assumed that the service time distribution was known and simple, such as normal distribution, uniform distribution [7, 8], etc. However, service time distribution is much more complex and challenging to capture without priori knowledge in real life. Therefore, it usually cannot be assumed normally or uniformly distributed. Instead, some researchers employed fuzzy set theory to describe the uncertain service time [9], but this depiction is crude and cannot well highlight some tail features of actual situations. Therefore, it is necessary to build a precise model to reflect the fluctuation of service time. Besides, two additional requirements should also be satisfied. (1) The distribution should be in good form with analytical tractability. A suitable distribution form can effectively speed up the calculation process by countable additivity or mathematical analysis. (2) The distribution cannot occupy too much storage space. The storage resources of the OFD system are limited, because most of the resources are used to store necessary information on orders and riders. And it is also difficult for the system to transmit too much data in real time, especially during peak hours when the number of orders is enormous.

In this paper, we model the distribution of the uncertain service time as a Gaussian mixture model (GMM) and propose an intelligent estimation method to establish the model. This distribution estimation problem is then transformed into a clustering problem by regarding each cluster as a Gaussian component to determine the number of Gaussian components and other parameters of GMM. To solve the clustering problem, a hybrid estimation of distribution algorithm (HEDA) is presented to minimize distribution quality and simplicity. Solutions are generated by different sampling strategies. To be specific, in the initialization stage, the Chinese restaurant

![img-0.jpeg](img-0.jpeg)

Fig. 1 The process to finish an order delivery task
![img-1.jpeg](img-1.jpeg)

Fig. 2 Scheduling process of the OFD
process (CRP) is employed to sample the initial solutions with good quality; in the iterative stage, promising solutions are generated based on the sampling mechanism of the HEDA. By the design of the problem-specific probability matrix and cluster merging mechanism, the number of Gaussian components (or called clusters) can be learned dynamically during the searching process. Extensive offline experiments are conducted on real-world data and the results show the superiority of the proposed algorithm. In addition, to examine how the distribution model can help the decisionmaking for OFD platforms, we conduct an online A/B test on Meituan platform. The experimental results verify the practical value of the modeling and estimation of uncertain service time.

The remainder of the paper is organized as follows. Section "Literature review" gives the review of related literature. In Section "Problem description", the GMM estimation problem is described. Section "Algorithm" presents the HEDA in detail. Offline and online experimental
results and analysis are provided in section "Experimental results". Finally, we end the paper with some conclusions in section "Conclusions".

## Literature review

OFDP is an emerging field of research and related research works are lacking at present, let alone the uncertainty modeling and estimation in the OFDP. The research works on uncertain vehicle routing problem, which is one of the most related problems to OFDP, usually assumed the distribution of the service time was known with a simple form, such as a discrete probability distribution with finite support [10, 11], a uniform distribution [12, 13]. In addition, they did not quantify the actual benefits of introducing uncertainty into the problem for real-life application.

Bian et al. [14] presented a bus service time estimation model considering buses queueing for the curbside bus stop.

They employed the compound Poisson process to model the service time and calculated the probability of each scenario. However, it focuses on passengers' boarding and alighting process, as well as the buses queuing process at the stop area, whereas the scenario of OFD service is much more complex. As for the estimation of travel time, the major challenges are quite different from the service time, including the data sparsity of route segments, multiple combinations of route segments for a certain travel as well as the time limitation to answer users' queries [15]. The techniques of travel time estimation cannot be applied to service time estimation, although they are relatively mature. Therefore, it is necessary to propose an intelligent method to model the uncertain service time for OFD service.

According to [16], the class of mixture model densities can approximate any probability density function (PDF) if the number of mixture components of the model is taken to be sufficiently large. Thereinto, GMM, which is formed by multiple Gaussian components, is ubiquitously used for density estimation in many fields due to its analytical tractability and asymptotic properties [17]. The modeling of GMM can be divided into two types: first, the number of Gaussian components, denoted as $K$, is given or changeless; second, $K$ is unknown or can be changed dynamically. For the former type, Redner and Walker [18] proposed a traditional ExpectationMaximum (EM) method to estimate the parameters of GMMs (including means, variances, and weight). It starts from an initial set of mixture parameters and generates a sequence of mixture parameters with increasing log-likelihood. However, this method was easy to get trapped in a local maximum and strongly dependent on the initial setting of parameters. To overcome the defect, Biernacki et al. [19] improved the EM algorithm using different initial strategies to find a good starting point. Besides, some swarm intelligent algorithms, such as genetic algorithm (GA) [20], particle swarm optimization [21], and differential evolution (DE) [22], were also employed for solving the problem due to their global exploration ability.

The latter type is more common in many practical applications where $K$ is unknown and difficult to obtain at first. Biernacki and Govaert [23] assumed that $K$ belonged to a set of values $\mathcal{K}$, and then estimated the parameters of the GMM corresponding to each possible $K$ in $\mathcal{K}$. However, the method needs to be repeated card $(\mathcal{K})$ times to obtain the optimal solution which is too time-consuming, where card $(\cdot)$ means the number of elements in the set. Melnykov and Melnykov [24] presented a strategy based on the concentrations of neighbors to initialize mean vectors and determine $K$, and then used EM to estimate the final parameters. Nevertheless, due to the complexity of real-world data, the $K$ determined by this method may not be optimal. Pernkopf and Bouchaffra [25] combined the GA with the EM method and used the minimum

Table 1 The notations of the problem

description length criterion to select the number of components. In addition, Bayesian learning algorithms have also been developed to estimate the GMM with an unknown $K$ [26]. Bayesian-based approaches mainly include resampling methods [27] and variational inference [28]. The former is more accurate if given enough time but is too time-consuming in practical applications, whereas the latter is relatively quick but may lose some precision.

## Problem description

The notations of the problem are described in Table 1.

![img-2.jpeg](img-2.jpeg)

Fig. 3 An example of the GMM

A finite GMM $f(x ; \boldsymbol{\theta})$ can be defined by a weighted sum of $K$ components as follows:
$f(x ; \boldsymbol{\theta})=\sum_{k=1}^{K} w_{k} f_{k}\left(x ; \mu_{k}, \sigma_{k}^{2}\right)$,
where $w_{k}, \mu_{k}, \sigma_{k}^{2}$ are the weight, mean, and variance of the $k$ th component, respectively. $\sum_{k=1}^{K} w_{k}=1$. $\boldsymbol{\theta}=\left\{K, \boldsymbol{w}, \boldsymbol{\mu}, \boldsymbol{\sigma}^{2}\right\}$ is the vector of all the parameters. $f_{k}\left(x ; \mu_{k}, \sigma_{k}^{2}\right)$ is the following single Gaussian distribution function with parameter $\mu_{k}, \sigma_{k}^{2}$ :
$f_{k}\left(x ; \mu_{k}, \sigma_{k}^{2}\right)=\frac{1}{\sqrt{2 \pi \sigma_{k}^{2}}} \exp \left(-\frac{1}{2 \sigma_{k}^{2}}\left(x-\mu_{k}\right)^{2}\right)$.
Figure 3 shows an example of the GMM with three components: the blue dotted lines are the distributions of different components and the full black line is the distribution of the mixture model.

We give our modeling of uncertain service time based on GMM as follows. Assume the input data are denoted as $\boldsymbol{t}=\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$, where $n$ is the size of the dataset, and $t_{i}(i=1, \ldots, n)$ is the $i$ th service time. Then, the real distribution of historical service time, denoted as $f_{\mathrm{s}}$, can be approximated as the frequency function of the data
$f_{\mathrm{s}}\left(t_{i}\right)=\sum_{j=1}^{n} I_{t_{i}=t_{j}} / n$,
where $I_{a=b}$ is the following characteristic function:
$I_{a=b}=\left\{\begin{array}{l}1, \text { if } a=b \\ 0, \text { else }\end{array}\right.$.

Besides, the GMM obtained from historical service time, denoted as $f_{\mathrm{d}}$, can be represented as follows:
$f_{\mathrm{d}}\left(t_{i} ; \boldsymbol{\theta}\right)=\sum_{k=1}^{K} w_{k} f_{k}\left(t_{i} ; \mu_{k}, \sigma_{k}^{2}\right)$.
Our goal is to determine the parameter vector $\boldsymbol{\theta}$ of $f_{\mathrm{d}}$ with the minimization of distribution quality and simplicity synchronously, where the distribution quality means the similarity between the estimated GMM and the real distribution of historical data, and the simplicity means the number of the GMM parameters. Kullback-Leibler divergence is commonly used in the previous works [29] to measure the similarity of two distributions. However, it has obvious weaknesses, such as asymmetry and unboundedness [30]. Instead, Wasserstein distance, presented by [31], not only has none of these disadvantages but also can measure the minimum average distance required to move the data from one distribution to another. Therefore, Wasserstein distance is employed in this paper to construct the objective function $\varepsilon$, which is calculated as follows:
$\min _{\boldsymbol{\theta}} \varepsilon=W_{\mathrm{d}}\left(f_{\mathrm{s}}(\boldsymbol{t}), f_{\mathrm{d}}(\boldsymbol{t} ; \boldsymbol{\theta})\right)+\lambda K$
$W_{\mathrm{d}}\left(f_{\mathrm{s}}(\boldsymbol{t}), f_{\mathrm{d}}(\boldsymbol{t} ; \boldsymbol{\theta})\right)=\sum_{x=\min \boldsymbol{t}}^{\max \boldsymbol{t}}\left|f_{\mathrm{s}}(x)-f_{\mathrm{d}}(x ; \boldsymbol{\theta})\right|$,
where $\lambda$ is a given weight coefficient, $W_{\mathrm{d}}\left(f_{\mathrm{s}}, f_{\mathrm{d}}\right)$ is the Wasserstein distance between $f_{\mathrm{s}}$ and $f_{\mathrm{d}}$ under L1-norm, and $\lambda K$ is a penalty to guarantee the simplicity.

This minimization problem has infinite solution space and is hard to obtain the analytical solution in a short time. Although several methods have been proposed to estimate the GMM with an unknown $K$, they are either poor in quality [23] or too time-consuming for Meituan platform due to the huge amount of data [27]. To well solve the problem, we transform it into a clustering problem. Each data can be assigned to a certain cluster, where a cluster represents a component of the GMM. Based on the clustering results $\boldsymbol{z}=\left\{z_{1}, z_{2}, \ldots, z_{n}\right\}$ where $z_{i}=k$ means that the $i$ th data are assigned to cluster $k, K$ can be determined by the number of clusters, and the parameters $\boldsymbol{w}, \boldsymbol{\mu}, \boldsymbol{\sigma}^{2}$ can be easily derived by calculating the maximum-likelihood estimation for each cluster as follows:
$K=\max \left(z_{1}, z_{2}, \ldots, z_{n}\right)$
$\mu_{k}=\sum_{j=1}^{n} I_{z_{i}=k} t_{i} / \sum_{i}^{n} I_{z_{i}=k}, k=1, \ldots, K$
$\sigma_{k}^{2}=\sum_{i=1}^{n} I_{z_{i}=k}\left(t_{i}-\mu_{k}\right)^{2} / \sum_{i}^{n} I_{z_{i}=k}, k=1,2, \ldots, K$.

![img-3.jpeg](img-3.jpeg)

Fig. 4 The framework of the HEDA

In a word, the decision variables are transformed as $z$ after defining the clustering problem. Then, the objective function will be transformed into
$\min _{z} \varepsilon=W_{\mathrm{d}}\left(f_{\mathrm{s}}(\boldsymbol{t}), f_{\mathrm{d}}(\boldsymbol{t} ; \boldsymbol{z})\right)+\lambda K$,
where $f_{\mathrm{d}}(\boldsymbol{t} ; \boldsymbol{z})$ can be calculated by Eq. (5) and Eqs. (8)-(10).

## Algorithm

Estimation of the distribution algorithm (EDA) is a swarm intelligent algorithm of good global exploration capacity [32, 33]. It is a statistical learning method that explores potential search space by building and sampling an explicit probability model of promising elite individuals. It has been employed in many fields, such as factory production scheduling [34], financial decision-making [35], green energy technology [36], and so on. In this paper, we design a HEDA to build the GMM by the cooperation of the EDA and the EM method. Besides, to obtain the initial solutions with a certain quality, the Chinese restaurant process (CRP) [37], one typical model of the Dirichlet process [38], is employed for initial clustering. The overall framework is shown in Fig. 4. We will present the algorithm with data pre-processing, encoding and decoding methods, initialization, cluster merging, local
intensification, elite solutions selection, probability model updating, and new population sampling.

## Encoding and decoding

The HEDA is proposed as a clustering method where the encoding represents the clustering results of each data, and the decoding is to calculate the distribution parameters according to maximum-likelihood estimation. To be specific, solutions can be represented by the clustering vector $z$ of the length $n$. However, since the amount of input data is huge, this method will occupy too much space. Instead, only the clustering results of unique data are stored to save space, because there is a lot of duplication in data. To be specific, a matrix PM of size $K_{\max } \times n_{\mathrm{d}}$ is used to represent solutions, where $K_{\max }$ is the given maximum number of components due to the storage limitation, and $n_{\mathrm{d}}$ is the number of unduplicated data. Each element $\mathrm{PM}_{k i}$ of PM is defined as the count that the $i$ th number is classified into cluster $k$ as follows. Besides, $\boldsymbol{C}=\left\{c_{1}, c_{2}, \ldots, c_{n_{d}}\right\}$ is the count vector of the number of each unique value in the data, where $\sum_{k=1}^{K_{\max }} p_{i k}=c_{i}$ must be satisfied
$\mathrm{PM}=\left[\begin{array}{cccc}p_{11} & p_{12} & \ldots & p_{1 n_{d}} \\ p_{21} & p_{22} & \ldots & p_{2 n_{d}} \\ \vdots & \vdots & \ddots & \vdots \\ p_{K_{\max } 1} & p_{K_{\max } 2} & \ldots & p_{K_{\max } n_{d}}\end{array}\right]$.
Decoding is to obtain $\boldsymbol{\theta}$ via encoding, which is adjusted on the basis of Eqs. (8)-(10). Before calculating $\boldsymbol{\theta}$, there may be some same or related rows in the PM, which can be merged to reduce the number of components (clusters). The most basic idea is to do elementary row transformation to find a normal form of PM, and set the rank of the transformed PM as $K$. This method can minimize $K$ of a certain PM, but is too timeconsuming for large matrixes. Therefore, we only operate some simple row transformations to merge identical rows and turn the PM into $\left[\mathrm{PM}^{\prime}, 0\right]^{T}$. Then, $\boldsymbol{\theta}$ can be calculated as follows:
$K=N_{r}\left(\mathrm{PM}^{\prime}\right)$
$\mu_{k}=\sum_{i=1}^{n_{d}}\left(t_{i}^{u} \times \mathrm{PM}_{i k}^{\prime}\right) / \sum_{i=1}^{n_{d}} \mathrm{PM}_{i k}^{\prime}, k=1,2, \ldots, K$
$\sigma_{k}^{2}=\sum_{i=1}^{n_{d}}\left(t_{i}^{u}-\mu_{k}\right)^{2} \times \mathrm{PM}_{i k}^{\prime} / \sum_{i=1}^{n_{d}} \mathrm{PM}_{i k}^{\prime}, \quad k=1,2, \ldots, K$
$w_{k}=\sum_{i=1}^{n_{d}} \mathrm{PM}_{i k}^{\prime} / n, \quad k=1,2, \ldots, K$,

where $N_{r}\left(\mathrm{PM}^{\prime}\right)$ is the number of rows of $\mathrm{PM}^{\prime}$.
For example, given the input service time as $\boldsymbol{t}=$ $\{2,3,5,3,2,6,2,6\}$ and $K_{\max }$ as 3 , then the unique data set $\boldsymbol{t}^{\boldsymbol{n}}$ is $\{2,3,5,6\}$ with $n_{\mathrm{d}}=4$ and $\boldsymbol{C}=\{3,2,1,2\}$, and a possible realization of PM can be
$\mathrm{PM}=\left[\begin{array}{llll}1 & 1 & 0 & 1 \\ 1 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0\end{array}\right]$
It can be transformed to $\left[\mathrm{PM}^{\prime}, 0\right]^{T}$ as follows, where $\mathrm{PM}^{\prime}=\left[\begin{array}{llll}2 & 2 & 0 & 2 \\ 1 & 0 & 1 & 0\end{array}\right]$

CRP has good clustering properties, and can be employed to sample initial solutions for our problem. To ensure the diversity of the population, a shuffled index vector will be used to access service time for each solution, denoted as $\boldsymbol{S}=\left\{s_{1}, s_{2}, \ldots, s_{n}\right\}$, where $1 \leq s_{1}, s_{2}, \ldots, s_{n} \leq n_{d}$, and the constraint that the number of elements in $\boldsymbol{S}$ that are equal to $i$ is $c_{i}$, for $i=1,2, \ldots, n_{d}$ should also be satisfied. Similarly, $t_{s 1}$ belongs to the first cluster, denoted as $z_{s_{i}}=$ 1 , and $\mathrm{pm}_{s_{1}, 1}=1$. For the $i$ th subsequent data, since the number of components should not be larger than $K_{\max }$, the distribution is transformed as follows:

$$
p\left(z_{s_{i}}=k \mid z_{s_{1}}, z_{s_{2}}, \ldots, z_{s_{i-1}}, K<K_{\max }\right)=\frac{\sum_{i=1}^{n_{d}} \mathrm{PM}_{i k}^{\prime}}{\gamma+i-1}
$$

Then, the parameters can be calculated as $K=2, \mu_{1}=$ $2 \times(2+3+6) / 6 \approx 3.6667, \mu_{2}=(2+5) / 2=3.5, \sigma_{1}^{2}=$ $2 \times\left[(2-3.6667)^{2}+(3-3.6667)^{2}+(6-3.6667)^{2}\right] / 6 \approx$ $2.8889, \sigma_{2}^{2}=\left[(2-3.5)^{2}+(5-3.5)^{2}\right] / 2=2.25, w_{1}=$ $6 / 8=0.75, w_{2}=2 / 8=0.25$. Therefore, $\boldsymbol{\mu}=$ $\{3.6667,3.5\}, \boldsymbol{\sigma}^{2}=\{2.8889,2.25\}, \boldsymbol{w}=\{0.75,0.25\}$, $\boldsymbol{\theta}=\{2,0.75,0.25,3.6667,3.5,2.8889,2.25\}$.

In general, our encoding can use a small storage space to represent the entire solution space, and our decoding method can quickly obtain $\boldsymbol{\theta}$ as well as reduce $K$.

## Initialization

The CRP is a typical discrete-time stochastic process in probability theory, and has been widely employed to represent uncertainty over the number of components in a mixture model [37]. It builds a distribution on partitions of integers to describe the process where $n$ customers sit down in a Chinese restaurant with an infinite number of tables. Definitely, the first customer sits at the first table. For the $i$ th subsequent customer, the tendency to choose the table obeys the following distribution:
$p\left(T_{i}=k \mid T_{1}, T_{2}, \ldots, T_{i-1}\right)=\frac{n_{k}}{\gamma+i-1}$
$p\left(T_{i}=K+1 \mid T_{1}, T_{2}, \ldots, T_{i-1}\right)=\frac{\gamma}{\gamma+i-1}$,
where $n_{k}$ is the number of previous customers sitting at table $k, T_{i}$ is the chosen table of customer $i, K$ is the number of occupied tables, and $\gamma$ is a given parameter that describes the dispersion degree of the distribution.

$$
\begin{aligned}
& p\left(z_{s_{i}}=K+1 \mid z_{s_{1}}, z_{s_{2}}, \ldots, z_{s_{i-1}}, K<K_{\max }\right)=\frac{\gamma}{\gamma+i-1} \\
& p\left(z_{s_{i}}=k \mid z_{s_{1}}, z_{s_{2}}, \ldots, z_{s_{i-1}}, K=K_{\max }\right) \\
& \quad=\frac{\sum_{i=1}^{n_{d}} \mathrm{PM}_{i k}^{\prime}}{\sum_{k=1}^{K} \sum_{i=1}^{n_{d}} \mathrm{PM}_{i k}^{\prime}}
\end{aligned}
$$

By sampling the distribution, we can divide the $i$ th data into a specific cluster $k^{*}$, and then, $\mathrm{pm}_{s_{i}, k^{*}}^{\prime}=\mathrm{pm}_{s_{i}, k^{*}}^{\prime}+1$. If it is assigned to a new cluster, then $K=K+1$. Repeat the above sampling process and we will obtain the initial population which is consisted of $P n$ individuals.

In addition to the initial population, the probability matrix should also be initialized. It is the core of the EDA, which affects the whole evolution and updating process of the population. Denote $Q$ as the probability matrix of size $K_{\max } \times n_{d}$. Each element $q_{k i} \in Q$ represents the probability that $t_{i}^{\alpha}$ belongs to cluster $k$. In this part, $Q$ is initialized uniformly to guarantee sufficient randomness for population diversity. That is, $q_{k i}=1 / K_{\max }$.

## Cluster merging

To further reduce the number of Gaussian components, a cluster merging strategy is designed. To be specific, some clusters with very few elements may be generated during the sampling process of the CRP or HEDA. These clusters are with small weights and have little effect on the overall distribution. Therefore, to reduce the length of $\boldsymbol{\theta}$, we discard these clusters and redistribute the elements to other clusters with large weights. The pseudo-code of the cluster merging is given as Algorithm 1. The threshold of the smallest number thres of elements is $n / 2 K_{\max }$.

```
Algorithm 1: Cluster merging
    \(K^{r m v} \leftarrow \emptyset\) : the index set of the removed cluster
        For \(k=1\) to \(K\)
        If \(\sum_{i=1}^{n_{d}} p m_{k i}<\) thres
            \(K^{r m v}=K^{r m v} \cup k\)
        End if
        End for
        For \(k\) in \(K^{r m v}\)
        For \(i=1\) to \(n_{d}\)
        For \(j=1\) to \(p m_{k i} \times c_{i}\)
            Assign data \(t_{j}\) to a randomly selected \(k_{\text {new }}, 1 \leq k_{\text {new }} \leq K\) and \(k_{\text {new }} \notin K^{r m v}\)
            \(p m_{k i}=p m_{k i}-1\)
            \(p m_{k_{\text {new }} i}=p m_{k_{\text {new }} i}+1\)
        End for
        End for
        End for
        Repair \(P M\) by row transformations
        Return \(P M\).
```


## Local intensification

The EDA has a strong global search capacity, but a relatively weak local searchability, while the EM algorithm is on the contrary. Therefore, we employ the EM algorithm as the local intensification operator to balance the exploration and exploitation of the HEDA.

The parameter vector of the best solution obtained during the current iteration is set as the initial solution of the EM algorithm. Then, by alternating E-step and M-step, the parameter vector will be improved until a certain search depth $l s$ is reached. The E-step and M-step are defined as follows.

E-step: Given the parameter vector from the previous iteration of the EM algorithm, the posterior probability can be computed as

$$
\begin{aligned}
\mathrm{PM}_{k, i}^{g}= & c_{i} w_{k, g} f_{k}\left(t_{i}^{u} \mid \mu_{k, g}, \sigma_{k, g}^{2}\right) / \sum_{l=1}^{K} w_{k, g} f_{l} \\
& \times\left(t_{i}^{u} \mid \mu_{l, g-1}, \sigma_{l, g-1}^{2}\right)
\end{aligned}
$$

where $w_{k, g}, \mu_{k, g}$ and $\sigma_{k, g}^{2}$ denotes the weight, mean, and variance parameters of $k$ th Gaussian component in $g$ th iteration.

M-step: Given the posterior probabilities $\mathrm{PM}_{k, i}$ obtained in the E-step, the parameters $w_{k, g}, \mu_{k, g}$, and $\sigma_{k, g}^{2}$ can be calculated according to Eqs. (14)-(16).

## Updating probability model

The probability model is updated by elite solutions, which is defined as the first $e_{n}$ solutions with minimal objective value. To better learn about the probability information, a sequencedependent weight strategy is designed. To be specific, we will sort the elite solutions by their objective, denoted as Elite $=$ $\left\{E_{(1)}, \ldots, E_{\left(e_{n}\right)}\right\}$, and the better ones will be assigned with a higher weight. The weight $w_{(\varepsilon)}^{\prime}$ of $E_{(\varepsilon)}$ is set as
$w_{(\varepsilon)}^{\prime}=\frac{e_{n}+1-e}{\sum_{j=1}^{e_{n}} j}$.
Then $Q$ is updated as follows:
$q_{k i}=(1-\alpha) q_{k i}+\alpha p_{k i}($ Elite $)$
$p_{k i}($ Elite $)=\sum_{\varepsilon=1}^{e_{n}} w_{(\varepsilon)}^{\prime} p_{E_{(\varepsilon)}}(i, k) / c_{i}$,
where $\alpha \in(0,1)$ is the learning rate. Besides, $Q$ should be normalized by column to ensure feasibility.

## Sampling mechanism

For each iteration, new individuals are sampled from the probability model $Q$. To ensure the population diversity, a

Fig. 5 The distribution of the instances on AOI types
![img-4.jpeg](img-4.jpeg)
temporary probability matrix $Q^{\prime}$ is generated by adding disturbances to $Q$, and is normalized by column to guarantee the feasibility. To ensure the quality of the solution, we narrow the range of disturbance, which is set as the maximum probability of a certain column as follows:
$q_{k i}^{\prime}=q_{k i}+\delta p, \forall i, k$,
where $\delta p$ is a random number between 0 and $\max \left(q_{i 1}, \ldots, q_{i K}\right)$
$\operatorname{PM}_{k i}=q_{k i}^{\prime} \times c_{i} / \sum_{k=1}^{K} q_{k i}^{\prime}, \forall i, k$.

## Experimental results

In this section, extensive offline and online tests are conducted. The offline experiments are carried out by comparing the HEDA with several existing algorithms on real-world datasets from the Meituan platform to validate the estimation effectiveness of GMM. The online A/B tests are implemented by employing the GMM obtained by the HEDA on the real-world scheduling system to validate the efficacy of the utilization of stochastic models. The details of the experiments are elaborated as follows.

## Offline experiment

## Experimental settings

Instance generation In this part, we will introduce the instance generation of the offline experiment. The instances of the offline experiment are the data set of service time $\boldsymbol{t}=\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$ in different areas and time periods. Service time differs greatly in space and time. Specifically,
![img-5.jpeg](img-5.jpeg)

Fig. 6 The distribution of the instances on periods
because residential areas usually have a more complex building environment and may not allow riders to pass, the service time in residential areas maybe be longer than that of office buildings. Besides, due to factors such as the passenger flow of elevators or other passing facilities, the service time during the peak hours is regularly longer than idle hours. Therefore, we distinguish the distribution of uncertain service time under different areas of interest (AOI) (each residence, office, school, mall, hospital, and so on) and periods (peak hours and idle hours). Each city can be divided into many AOIs. For example, in Beijing, there are more than 3000 schools alone. That is, tens of thousands of GMMs need to be constructed for cities throughout the whole country, which forces us to construct accurate GMMs with parameters vectors as short as possible. By collocating 1 month's historical data from multiple cities, a total of 29,028 instances are obtained. The distributions of the instances divided by AOI types and periods are shown in Figs. 5 and 6, respectively.

Due to the possibility of extremely abnormal situations, some data may deviate far from the majority in the collected dataset of different AOI and periods. The analysis and statistics of the abnormal data are of little significance, so we need to clean the data first to ensure the validity of the input. After

![img-6.jpeg](img-6.jpeg)

Fig. 7 The distribution of the instances on the amount of data

Table 2 Combinations of parameter values
removing the null values and singularities, we will retain the $95 \%$ confidence data as the input. Besides, in light of the amount of data in each instance which infects the computational complexity of building the GMMs, we also divide these instances into ten groups as shown in Fig. 7, where the ranges of the data amount of each group are marked around the pie.

Parameters The HEDA contains three key parameters: the population size Pn , the learning rate $\alpha$ of $Q$, and the number of elite solutions $e_{n}$. To investigate the effect of these parameters on the performance of the algorithm, we implement the Taguchi method of design of the experiment using a moderate scale instance in group 7. Four levels of each parameter are set as shown in Table 2. According to the number of parameters and levels, an orthogonal table $\mathrm{L} 16\left(4^{3}\right)$ is generated with 16 combinations of parameter values in total. For each combination, we run the HEDA 20 times independently to obtain the average $\varepsilon$, which is set as the response value (RV). The smaller the RV, the better the performance of the parameter combination. The orthogonal array and RVs are listed in Table 3. The significant rank of each parameter is listed in Table 4. Besides, the trend of each factor is shown in Fig. 8. It can be seen that $\alpha$ is the most significant parameter. A large value of $\alpha$ may lead to premature convergence, while a small

Table 3 Orthogonal array and RV values

Table 4 Response value and rank of each parameter

value of $\alpha$ may lead to slow convergence. Besides, $e_{n}$ ranks the second. A proper $e_{n}$ can help the algorithm update the probability model reasonably. As for Pn , it ranks third. If Pn is too large, it will be too time-consuming for one iteration and lead to slow convergence. However, if Pn is too small, the solution space cannot be sampled sufficiently. According to the above analysis, the parameters of the HEDA are suggested as $\mathrm{Pn}=50, e_{n}=10$, and $\alpha=0.6$, which will be used in the following experiments. Besides, $\lambda$ is empirically set as 0.1 .

Comparison algorithms We compare our HEDA with the following three other methods.

- Nested-EM [39], which was proposed recently to build GMMs with an unknown $K$.

Fig. 8 Factor level trend

Table 5 Results of RPD and $p$ value
![img-7.jpeg](img-7.jpeg)

- Differential evolution (DE) algorithm [22], which is proposed to solve the GMM with a priori number of components. For a fair comparison, we set the priori number of components as $K_{\max }$ and adapt the cluster merging operator to the algorithm to reduce $K$.
- The K-means algorithm [40], which is a typical and most known clustering method. We also compare our proposed HEDA to this well-known clustering method, since we transmit our distribution estimating problem into a clustering problem.

Besides, to demonstrate the effectiveness of the local intensification, we compare the HEDA with HEDA_nls (HEDA without local intensification). The termination criterion for each algorithm is the same evaluation times. All the algorithms are coded in Java and run on the servers of Meituan.

Evaluation metric In this paper, relative percentage deviation (RPD) and proportion of best times (PBT) are employed to evaluate the performance
$\operatorname{RPD}\left(\operatorname{alg}_{i}\right)=\frac{\operatorname{alg}_{i}-\mathrm{bst}_{i}}{\mathrm{bst}_{i}} \times 100$
$\operatorname{PBT}\left(\operatorname{alg}_{i}\right)=\sum_{i=1}^{N} I_{\mathrm{alg}_{i}=\mathrm{bst}_{i}} / N \times 100$,
where $\mathrm{alg}_{i}$ is the objective value of a certain algorithm and $\mathrm{bst}_{i}$ is the best objective value obtained by all the compared algorithms for the $i$ th instance. A smaller RPD indicates a better performance. PBT represents the proportion of the times that an algorithm obtains the best solutions in the group with $N$ instances. A larger PBT indicates a better performance.

![img-8.jpeg](img-8.jpeg)

Fig. 9 The PBT on different AOI types
![img-9.jpeg](img-9.jpeg)

Fig. 10 The PBT on different periods

## Experimental results

The results of the RPD on different groups are listed in Table 5. It can be seen that the HEDA is better than other algorithms in all groups of instances, which indicates the superiority of the HEDA. And the difference between the RPDs of HEDA and other algorithms, especially the nested EM in Group 1 is significantly smaller than in other groups. It may be because the instances of Group 1 are with the smallest problem scale and are easier to be solved. Besides, by comparing the HEDA and HEDA_nls, it can be concluded that the local intensification can effectively improve the performance of the algorithm. In addition, the nonparametric tests (Kruskal-Wallis tests) with 95\% confidence interval are carried out for each pair of RPDs.

Besides, the results of PBT on different AOI types are shown in Fig. 9. It can be seen that the proposed HEDA is the best on most AOI types, especially on the residence, which occupies $66.37 \%$ of all the instances.

From Fig. 10, it can be seen that the PBT of HEDA is close to $80 \%$ at any period. Therefore, we can conclude that the HEDA is superior on different AOI types and periods to other compared algorithms.

## Online A/B test

## Experiment settings

Settings of policy and the A/B test To quantify the benefits of introducing the uncertainty of service time into the OFDP for real-life application, we compare the deterministic policy and stochastic policy to dispatch orders on Meituan platform. The two policies are shown in Fig. 11. And the specific details of route planning and order dispatching algorithms can be found in reference [41]

- Deterministic policy, Fig. 11a. It is the current scheduling policy of Meituan, where the service time is assumed as a deterministic value and is obtained according to the average value of historical service time, leading to deterministic objective values for order dispatching.
- Stochastic policy, Fig. 11b. We employ the GMMs of stochastic service time generated by the HEDA. For utilization, multiple scenarios are sampled from the GMMs via the Monte Carlo sampling method to calculate the objective values of solutions. And the expected objective will be employed to guide the order dispatching.

Then, online A/B test is employed to compare these two policies. The A/B test is conducted in Zhuhai, Guangdong Province, China. Similar to the test settings by Chen et al. [42], we divide the areas in this city into two similar regions:

![img-10.jpeg](img-10.jpeg)

Fig. 11 The framework of scheduling process in Meituan
an experimental region (E-region) and a control region (Cregion). And the input of the online experiment includes the whole information of riders, orders, restaurants, as well as the distributions or deterministic values of service time. For a fair comparison, we guarantee that there are no significant differences between the two regions before the test. The observation metrics of the E-region and C-region are as close as possible during a period (denoted as comparison dates) when dividing areas. Afterward, we employ the deterministic method in the C-region and the stochastic method in the E-region to dispatch orders relatively. These methods are run for a period of time (denoted as experimental dates), which lasts for the same duration as the comparison dates.

Observation metric For the online test, several observation metrics are adopted to evaluate customer satisfaction and delivery efficiency as follows.
(a) Customer satisfaction-based metric.

- 5-Min punctual rate $\left(\mathrm{PR}_{5}\right)$ :

$$
\mathrm{PR}_{5}=\frac{\left|\hat{O}_{5^{-}}\right|}{|O|} \times 100 \%
$$

- 15-Min overtime rate $\left(\mathrm{OR}_{15}\right)$ :

$$
\mathrm{OR}_{15}=\frac{\left|\hat{O}_{15^{*}}\right|}{|O|} \times 100 \%
$$

- Proportion of orders delivered over $55 \mathrm{~min}\left(\mathrm{PP}_{55}\right)$ :

$$
\mathrm{PP}_{55}=\frac{\left|\hat{O}_{55^{*}}\right|}{|O|} \times 100 \%
$$

(b) Delivery efficiency-based metric.

- Average online delivery time (AODT) (unit: minute):

$$
\mathrm{AODT}=\frac{1}{|O|} \sum_{o(i) \in O}\left(\widehat{\mathrm{OT}}_{i}-\mathrm{RT}_{i}\right)
$$

- Area time efficiency (ATE):

$$
\mathrm{ATE}=\frac{|O|}{\hat{t}_{\mathrm{del}}}
$$

where $O$ is the set of all delivered orders during a day in a certain area, $\hat{O}_{5^{-}}$is the set of orders that are delivered without delay or delayed within $5 \mathrm{~min}, O_{15^{*}}$ is the set of orders that are delayed for more than $15 \mathrm{~min}, \widehat{\mathrm{OT}}_{i}$ is the time when $o_{i}$ is delivered to the customer, $\mathrm{RT}_{i}$ is the time when $o_{i}$ is accepted by the platform, and $\hat{t}_{\text {del }}$ is the total time spent by all the riders to deliver orders. The units of AODT and $\hat{t}_{\text {del }}$ are both minutes. The notation with a " " means that it is observed online. The $\mathrm{PR}_{5}, \mathrm{PP}_{55}$, ATE are the bigger the better, and the $\mathrm{OR}_{15}, \mathrm{AODT}$ are the smaller the better.

## Experiment results

Although the ideal situation is that the observation metrics of the E-region and C-region are exactly the same before the test, it is difficult to achieve this situation. Therefore, to mitigate the effect caused by the deviation, the following true difference $\Delta_{\text {trn }}$ is introduced as the comparison metric.

We believe that the difference of each metric between the E-region and C-region during the comparison dates, denoted as inherent deviation $\left(\Delta_{\text {inh }}\right)$, can represent the essential difference between the two regions. Besides, the difference during the experiment dates, denoted as the experimental difference

Table 6 The results of the online A/B test

$\left(\Delta_{\text {exp }}\right)$, should include this inherent deviation and the influence caused by different methods. Then, $\Delta_{\text {tru }}=\Delta_{\text {exp }}-\Delta_{\text {inh }}$ can be regarded as the true difference of different methods by excluding the influence of inherent deviation.

The results of the online A/B test are shown in Table 6, where the bold value of $\Delta_{\text {tru }}$ means that the corresponding metric is improved by employing the stochastic service time model in the dispatching system. It can be seen that our new GMM-based policy can improve all the metrics compared to the current policy. Roughly speaking, if we extend this policy to the whole country, we can reduce about 30,000 severely-overtime orders a day which can greatly improve the customers' satisfaction. Besides, about 50 s can be saved on average for delivering an order, which indicates an improvement in rider efficiency. Therefore, we can conclude that accurate description and application of uncertain service time can effectively improve customer satisfaction and delivery efficiency for OFD applications.

## Conclusions

This paper focused on the modeling of uncertain stochastic time in OFD applications. An HEDA was presented to build GMMs with an unknown component number of each AOI under different scenarios. Extensiveoffline numerical tests of real-world data showed the effectiveness of the proposed algorithm. In addition, we also employed the GMMs in a particular OFD application, and the results of the online A/B test indicated the practical value of introducing a stochastic model for decision-making. This method can be extended to the modeling of distributions on other uncertain data. In future work, we will employ the current state and finegrained features to build a predictive model, which can guide decision-making more accurately.

Acknowledgements This research is supported by the National Science Fund for Distinguished Young Scholars of China [No. 61525304], the National Natural Science Foundation of China [No. 61873328], and Tsinghua University-Meituan Joint Institute for Digital Life.

## Declarations

Conflict of interest On behalf of all authors, the corresponding author states that there is no conflict of interest.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecomm ons.org/licenses/by/4.0/.
