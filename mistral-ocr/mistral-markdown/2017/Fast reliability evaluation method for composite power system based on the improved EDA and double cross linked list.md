# Fast reliability evaluation method for composite power system based on the improved EDA and double cross linked list 

Wenxia Liu ${ }^{1}$, Rui Cheng ${ }^{1 \text { (1) }}$, Yahui Xu ${ }^{1}$, Zongqi Liu ${ }^{1}$<br>${ }^{1}$ State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Changping District, Beijing, People's Republic of China<br>$\boxtimes$ E-mail: 619275404@gq.com


#### Abstract

To improve the computational efficiency of Monte Carlo simulation in composite power systems reliability evaluation, this study presents a method based on the improved estimation of distribution algorithm (EDA) and double cross linked list. Compared to traditional techniques, this method is comprehensively improved in the stage of both sampling and state evaluation. In the sampling stage, the population-based incremental learning algorithm is presented, where the probability vector is updated based on the distribution characteristics of excellent samples in population of previous generations. Meanwhile, setting a limit to the probabilities of elements in normal state and mutation strategy are introduced, which improves the excellent characteristics of the population. In the state evaluation stage, the state search and match process is speed up by utilising the intelligent storage technology based on the double across linked list. It avoids calling the optimal power flow for the same state repeatedly. Finally, the proposed method is tested in IEEE RTS 79. As the result shows, compared with other methods ever used in reliability evaluation, this method is not only more efficient in computation but also more accurate. Thus, the proposed method is proved to be reliable and effective.


## 1 Introduction

Power system reliability assessment plays a significant role to measure the ability of power system operating safely and stably. However, due to that the power system scale and complexity are increasing and large scale intermittent energy connects to the grid, the dimensionality and difficulty of reliability calculation increase dramatically. For this reason, it is of great importance for practical applications to conduct in-depth study of the composite power system reliability evaluation method, which can improve the computational efficiency.

At present, the available methods for reliability evaluation are generally categorised into analytical method and Monte Carlo simulation (MCS). When using analytical method, the computational complexity increases rapidly with the expansion of the system size. On the contrary, there is no close relationship between the MCS sampling frequency and the system size [1], so MCS is more applicable to the composite power system reliability evaluation. However, the disadvantage of MCS is that the time for convergence for large or complex systems with high reliability can become very long.

To effectively cope with the contradiction between computation time and precision in the process of MCS, efforts have been made to reduce the convergence time of MCS through a variety of techniques. One kind of improved technique is on the level of hardware and computer technology. For instance, a new method for reliability evaluation based on distributed computing is presented in [2], in which the reliability evaluation is decomposed into a number of sub-problems by utilising the distributed computing method. Then the sub-problems can be solved with small computation amount, and via parallel processing, the calculation efficiency can be improved. Compared to the improvement of distributed computing method, the improvements of MCS itself could be presented with more general applicability. The existing improvements in MCS are mostly focused on the sampling stage and state evaluation stage.

In the sampling stage, efforts have been made to reduce the variance and thus to speed up the convergence of MSC. Common methods of reducing the variance are stratified sampling method, importance sampling method and intelligent state space pruning
(ISSP). Stratified sampling method [3, 4] faces difficulties in determining the optimal proportion allocated to each layer, thus limiting the improvement of computational efficiency [5]. Importance sampling method aims at selecting a probability distribution (change of measure) through the sample learning which reduces or minimises the computational cost (simulation time), subject to a desired accuracy. It greatly increases the frequency of important events (i.e. loss of load) to be sampled, so as to achieve the purpose of reducing the variance. Based on optimal multiplier, the importance sampling method is applied in [6], and the size of optimal multiplier is revised repeatedly according to the element states in the loss of load states, until that the requirements of convergence is achieved. Then, the failure rate of all elements are multiplied by the optimal multiplier, thus the important distribution function is constructed. Moreover, the crossentropy method can also be applied to importance sampling to obtain the optimal distribution [7, 8]. In [9], a quasi-Monte Carlo reliability calculation model, in which the Sobol sequences are taken as the sampling points, is established and combined with importance sampling method, thus to achieve the convergence faster. In general, a series of improvements have been made in importance sampling method. Despite all this, it is still difficult to efficiently construct the optimal probability distribution of the system state because of the fact that a large number of training samples are needed and this process costs a lot of time. Hence, it is difficult to make further promotion for the method [10].

Mitra and Singh [11-13] in 1996, put forward the state pruning method which is based on the state decoupling. Via state decoupling, the state space is decomposed into set A (acceptable) and set $U$ (unclassified). Then, after removing the set A, the sampling can be conducted in the space with high density of loss of load, greatly speeding up the convergence of variance [11-13]. To implement the state decoupling successfully, the system is ought to be coherent. However, when the DC or AC model is used in the power flow calculation, original coherence of the system will be damaged due to the line states having been changed [12].

As compared with the decomposition-based pruning, ISSP techniques are easy accommodation of any power flow model, non-coherency is avoided, and contingencies of all orders are sampled [14]. The intelligent algorithms are used in ISSP for state

![img-0.jpeg](img-0.jpeg)

Fig. 1 Diagram of state space pruning
space pruning. Rather than aiming to solve the optimal problems, the intelligent algorithm in ISSP focuses on the evolution of the population as a whole in the process of reproduction. By utilising intelligent search, more and more normal states can be obtained, and therefore, ISSP is easier to be realised, with more general applicability. Respectively, genetic algorithm and binary particle swarm optimisation are used in $[14,15]$ for the state space pruning, which improves the convergence performance of MCS. The performances of ISSP techniques under different heuristic algorithms are analysed and compared in [16], not only including the genetic algorithm and binary particle swarm as mentioned above, but also joining the mutually exclusive binary particle swarm and binary ant colony optimisation algorithms etc. In the process of state space pruning, traditional intelligent algorithms always achieve the search of excellent states via the random operation of crossover and mutation. With regard to the evolution process, the main idea is to take advantage of the information carried by excellent individuals (there is no loss of load) in a population, under the condition that the failure rates of elements keep constant. Owing to the fact that there is only a small quantity of fault elements in the state that there is no loss of load, the information carried is not enough, thus the evolution process becomes slower, which needs to be improved.

On the other hand, with regard to the state evaluation stage of MCS, some ways to achieve the improvement are via support vector machine [17-19] and neural networks [20-22] etc. These machine learning algorithms can take place of the optimal power flow calculation, so as to speed up the process of state evaluation. Nevertheless, there is a limitation in learning samples, thus the applicability of the model has an effect on reliability precision. In addition, intelligent storage is used in reliability evaluation in recent study, which can avoid the same state sequence being calculated repeatedly, so as to speed up the assessment.

To significantly improve the reliability computing efficiency, it is necessary to make comprehensive improvements considering both the sampling stage and state evaluation stage. This paper proposes a fast-reliability evaluation method for composite power system based on state space pruning. There are two main contributions in this method. One is to introduce the improved estimation of distribution algorithm (EDA) into ISSP, and in the evolution process, the failure characteristics of elements is revised on the basis of the probability statistics of excellent individuals' characteristics in the population. By this means, the coupling between a single element and every excellent individual can be reflected, thus to achieve fast search for the excellent states; the other is to adopt intelligent storage and search method based on double cross linked list in the stage of assessment. As a result, the state pruning as well as the state search is speed up, and meanwhile, the frequency of repeatedly calling the optimal power flow calculation is reduced due to the dynamic fault set.

## 2 Concept of state space pruning

The state space is defined as all possible combinations of generator configurations of a given test system. Each state will consist of a listing of all generators at all buses and all transmission lines along with their operating status: up or down. This generation capacity will then be compared with the total load of the test system in order to determine if there is or is not a loss of load. With vector $\boldsymbol{X}_{k}=\left(x_{1}\right.$, $\left.x_{2}, \ldots, x_{n}\right)$ to denote the state space, a binary encoding scheme is
used for the representation of the operating status of generators or transmission lines. 0 means the element is fault, and 1 means the element is normal, as well as that $n$ is the total number of elements in the system. Selection mechanisms allow removing a large proportion of normal states out of the original state space. Then the sampling is performed in the pruning space with high density of loss-of-load, thus greatly increasing the probability of loss of load event. The same convergence precision can be achieved, compared with the traditional MCS, with less sampling times and taking shorter time. Fig. 1 illustrates the process of state space pruning. The original state space can be divided into set A and set U , in which set A contains most of the normal states, while set U contains the loss-of-load states as well as a small proportion of normal states.

Assuming that the sampling size in the original state space is $N$ and the loss of load probability LOLP is $v$, the variance coefficient $\eta$ of LOLP can be expressed as:

$$
\eta=\frac{1}{v} \sqrt{\frac{v(1-v)}{N}}
$$

The proportion of set $U$ in the original state space is represented as $r$. If sampling is performed over the set $U$, then the probability of loss of load in set $U$ is presented as follows:

$$
v^{\prime}=\frac{v}{\varepsilon}
$$

The coefficient of variation $\eta^{\prime}$ is calculated by

$$
\eta^{\prime}=\frac{1}{r^{\prime}} \sqrt{\frac{v^{\prime}(1-v)^{\prime}}{N^{\prime}}}=\frac{\varepsilon}{v} \sqrt{\frac{(v / \varepsilon)(1-(v / \varepsilon))}{N^{\prime}}}
$$

where $N^{\prime}$ is the sampling size in the $U$ space. As the convergence of $\eta$ is the same as $\eta^{\prime}$, then

$$
\frac{N^{\prime}}{N}=\varepsilon \frac{1-(p / \varepsilon)}{1-p}
$$

Thus, under the same convergence precision, the sampling size $N^{\prime}$ required in reliability assessment in set $U$ is far less than the sampling size $N$ in the original state space.

## 3 Power system reliability evaluation based on the improved EDA and double cross linked list

### 3.1 Intelligent state space pruning based on the improved EDA

3.1.1 Improved EDA algorithms: EDAs are an emerging class of intelligent optimisation algorithms [23] based on the principles of statistics, which combines the genetic algorithm with statistical learning. An EDA typically work with the probability model and its update in order to describe the spatial distribution and overall evolution trend of population [23, 24]. The characteristic that most differentiates EDA from other evolutionary search strategies such as GA is that the evolution from a generation to the next one is conducted by estimating the probability distribution of the fittest individuals, and afterwards by sampling the induced probability model (Fig. 2).

According the differences between probability models, EDA can be divided into population-based incremental learning algorithm (PBIL), univariate marginal distribution algorithm, mutual information maximisation for input clustering and so on. Among these algorithms, PBIL is a recently developed technique that has drawn great concern. In the PBIL algorithm, the probability vector is updated on the basis of the distribution characteristics of the excellent individuals in last generation of population. The probability vector of the $l_{0}$, generation is represented by $\boldsymbol{P}_{i}(X)=\left(p\left(x_{1}\right), p\left(x_{2}\right), \ldots, p\left(x_{n}\right)\right)$, where $p\left(x_{i}\right)$ denotes the probability of element $i$ in normal state. The update process is as follows [24]:

![img-1.jpeg](img-1.jpeg)

Fig. 2 Basic procedures of EDA

$$
P_{l+1}(x)=\boldsymbol{P}_{l}(x)+a\left(\frac{1}{K} \sum_{k=1}^{K} X_{l}^{2}-\boldsymbol{P}_{l}(x)\right)
$$

where $X_{l}^{i}, X_{l}^{j}, \ldots, X_{l}^{K}$ are the state spaces of the best $K$ individuals sampled from the $l_{\mathrm{th}}$ generation. $a$ is the learning rate, which is between 0 and 1 .

However, due to the limitation of the population size in each generation as well as the randomness in the process of reproduction, the overall excellence of the population generated by PBIL algorithm cannot reach the optimal. Therefore, the update mode of PBIL algorithm needs to be improved. In this paper, PBIL algorithm is improved and the probability vector is updated based on the distribution characteristics of excellent samples in population of previous generations. By this way, the correlation between element state and system state is taken into consideration. The update process is as follows:

$$
P_{l+1}(x)=\boldsymbol{P}_{l}(x)+a\left(\frac{1}{K+1} \sum_{s=1}^{l}\left(\sum_{k=1}^{K} X_{l}^{s}\right)-\boldsymbol{P}_{l}(x)\right)
$$

Meanwhile, in order to avoid premature phenomena, some improvements are made in EDA as follows:
(i) Set the upper and lower value of $p\left(x_{i}\right)$, making $p\left(x_{i}\right)$ in the interval $\left[P_{\min }, P_{\max }\right]$. [only to avoid the occurrences of zeros or ones in vector $\boldsymbol{P}_{l}(X)$ ]
(ii) Introduce mutation strategy. Assume that the mutation rate is $p_{m}$, and generate a random value between 0 and 1 . If the random value is less than $p_{m}$, then randomly change the working state of a certain element, that is, ' 1 ' to ' 0 ' or ' 0 ' to ' 1 '.
3.1.2 Method of ISSP based on the improved EDA: When using the improved EDA for ISSP, there are two basic pieces that must be defined:
(i) A genetic representation of the solution domain.
(ii) A fitness function to evaluate the solution domain.

This study uses a binary encoding scheme for the genetic representation of the domain. This means that the possible state that a chromosome carries will be represented by a string of 1 and 0 s . In this way, each gene carried by a chromosome represents a single element, it can be represented as follows:

$$
x_{i}= \begin{cases}0 & \text { element } i \text { is down } \\ 1 & \text { element } i \text { is up }\end{cases}
$$

Considering the previous definitions, this fitness function $\operatorname{Fit}(k)$ is defined as follows in this paper [16]:

$$
F i t(k)=\operatorname{Copy}_{k} * P_{k} * E_{k}
$$

where $\operatorname{Copy}_{k}$ is the number of all possible permutations of the evaluated state $k$. Thus, $\operatorname{Copy}_{k}$ can be expressed by:

$$
\operatorname{Copy}_{k}=\binom{G_{1}}{O_{1}} \cdot\binom{G_{1}}{O_{j}} \cdot\binom{G_{m}}{O_{m}}
$$

Generators and transmission lines can be divided into $m$ groups according to different levels of rated capacity and voltage classes. Here $G_{j}$ is the total number of elements in group $j$ and $O_{j}$ is the number of elements that are normal in group $j$.
$P_{k}$ is the probability of state $k$ occurring, which can be computed by:

$$
P_{k}=\prod_{i=1}^{n} p_{i}
$$

$$
p_{i}= \begin{cases}1-\mathrm{FOR}_{i} & \text { element } i \text { is up } \\ \mathrm{FOR}_{i} & \text { element } i \text { is down }\end{cases}
$$

FOR $_{i}$ denotes the unavailability of element $i$, and $n$ is the number of elements.
$E_{k}$ denotes the total excess power supplied in state $k . C_{k}$ is the total generation capacity in state $k$ while $U_{k}$ is the actual amount of generation capacity used in state $k$ when the OPF is adopted. Then $E_{k}$ can be defined as follows:

$$
E_{k}= \begin{cases}C_{k}-U_{k} & \text { successful state } \\ U_{k}-C_{k} & \text { loss of load state }\end{cases}
$$

The fitness function used here is designed to encourage the total generation capacity and transmission capacity to increase, thus further search of the normal states can be achieve. As it is known, the actual goal of intelligent algorithm is to search more normal states - not to discover an optimum. Therefore, the stopping criterion of the state pruning process is supposed to be the number of generations rather than the variance.

The steps of the state space pruning based on the improved EDA can be described as follows:

Step 1: Generate the first generation of population according to the unavailability of elements. Set the population size as M.
Step 2: Identify each individual in the population and judge whether it is in the normal state. If it is, then store the individual into set A , and record its occurrence probability. $P_{k}$ is the original occurrence probability of individual $k$, which can be calculated by (10).

Step 3: Verify whether the stopping criterion is met, that is, whether the counter of generations reaches the setting number. If not, then go to step 4; otherwise, finish the process of ISSP.
Step 4: According to the fitness function $\operatorname{Fit}(k)$, select the $K$ best individuals from the population and store them into the collection of previous excellent samples.
Step 5: Update the probability vector via formula (6), which is based on the distribution characteristics of excellent samples in the population of previous generations. Thus, the probability model of the next generation of population is obtained, and make $p\left(x_{i}\right)$ is in the interval [Pmin, Pmax].
Step 6: Generate the next generation of population based on the updated probability model, then perform the mutation operation and go to step 2.

3.2 Intelligent storage and search method based on double cross linked list

To achieve fast-reliability evaluation, this paper proposes an intelligent storage and search method based on double cross linked list. The main idea of the double cross linked list is as follows: create two memory spaces in the form of cross linked list, which are, respectively, used to store set A and the state sequences that have been evaluated. The set which stores the state sequences that have been evaluated is defined as dynamic fault set. In the cross linked list, each storage node contains four domains: number, value, right pointer and down pointer. The cross linked list of set A or dynamic fault set is shown as Fig. 3.

In the cross linked list, the number domain is used to store the faults' order, that is, the number of elements which are in fault state. Right pointer and down pointer are used to store the column
![img-2.jpeg](img-2.jpeg)

Fig. 3 Cross linked list of set $A$ or dynamic fault set
pointer and row pointer of matrix elements, respectively. For the value domain, it is different in the two levels of retrieval process. In the first level of retrieval, value domain stores the number of sampling records in accord with the faults' order. However, in the second level of retrieval, the value domain stores different information according to different cases. In the cross linked list of set A, the value domain stores the probability of state sequences occurring as well as the serial number of fault elements; in the cross linked list of dynamic fault set, the value domain stores the flag of loss-of-load as well as the serial number of fault elements. Based on the cross linked list, the state sequence can be quickly and accurately searched for match. The specific search and match process of the state sequences is shown in Fig. 4.

Via MCS, a new state sequence is randomly generated. First, call the cross linked list of set A, and judge whether there have been a same sequence in set A. If not, then continue to call the cross linked list of the dynamic fault set, and likewise, judge whether this sequence has been evaluated. If it has, the flag of loss of load can be obtained from the value domain, and it is unnecessary to call the OPF calculation again. If not, the state sequence would be evaluated by performing the OPF calculation and the calculated results under the node would be stored in the dynamic fault set.

### 3.3 Flow of reliability evaluation

Reliability evaluation based on the improved EDA and double cross linked list mainly consists of two parts: state space pruning using the improved EDA and MCS. The flow chart of reliability evaluation based on EDA and intelligent storage is shown in Fig. 5.

The $\mathrm{EPNS}_{\text {MCS }}$ and $\mathrm{LOLP}_{\text {MCS }}$ are, respectively, defined as the conditional expected demand not supplied and conditional loss of load probability calculated in the pruned state space. Therefore, once the state space has been pruned, to obtain the actual EPNS and LOLP in the original state space, the indices for the conditional state space must be restored by [14]:

$$
\mathrm{LOLP}=\mathrm{LOLP}_{\mathrm{MCS}} *\left(1-\sum P_{k}\right)
$$

$$
\mathrm{EPNS}=\mathrm{EPNS}_{\mathrm{MCS}} *\left(1-\sum P_{k}\right)
$$

![img-3.jpeg](img-3.jpeg)

Fig. 4 Searching and matching flow of state sequence

![img-4.jpeg](img-4.jpeg)

Fig. 5 Flow of reliability evaluation
where, $P_{k}$ is the occurring probability of the pruned state $k$, and $1-\sum P_{k}$ is the total probability of remaining states in the pruned state space.

## 4 Case study

In this section, the proposed method as well as computational algorithm is applied to IEEE-RTS 79 [25]. The test system consists of 24 buses, 38 transmission lines, 32 generating units and a compensator. The total peak load of the system is 2850 MW while total installed capacity is 3405 MW . Assuming that the population size M of each generation is $500, K$ is 350 , and the mutation rate $p_{\mathrm{m}}$ is 0.1 . The availability of elements in the modern power system is $>0.9$, and the availability of power lines is generally higher than that of generators. In view of this case, in order to avoid the occurrence that the probability of elements in normal state quickly reaches 1 (no fault occurs in each element), the learning rate of generators and power lines are set to be 0.1 and 0.01 , respectively. Set the probability of generator and line in normal state are in interval of $[0.90,0.99]$ and $[0.90,0.9995]$, respectively.

### 4.1 Impact of pruned states for iterations

In the process of ISSP, there are more and more normal individuals sampled in every generation under the guidance of the fitness function. Accordingly, the overall evolution of the population is realised. The number of pruned states in each generation varies with the number of generations, which is shown in Fig. 6.

As the red trend line shows in Fig. 6, the number of pruned states in each generation tends to increase, which means that the evolution of the population has been achieved successfully via EDA. When the generation number reached 65 , the number of pruned states stays around 490 with little fluctuation. This is
![img-5.jpeg](img-5.jpeg)

Fig. 6 Number of pruned states change along with the generation
mainly because the evolution of population has been realised basically in that time.

The number of MCS iterations is closely related to the number of pruned success states. With the number of generations taking 50, 60,70 and 80 , the variation trend of the iteration number is illustrated in Table 1. The LOLP calculated in different levels of pruning as well as the convergence process of the variance coefficient are shown in Fig. 7.

As it is shown in Fig. 7, the convergence values of LOLP were $\sim 0.1$ when the generations were $50,60,70$, and 80 . It is proved that the new algorithm is stable and efficient. When the number of generations reached 80 , the convergence rate of LOLP became the fastest, which were followed by 70 and 60 , the slowest was 50 . As the number of pruned states in set A increases, the density of fault states in the pruned state space increases and the convergence criterion is met faster. Thus, the number of iterations needed for MCS convergence decreases as the increased number of pruned states. As it is shown in Table 1, when the generations reach 70 and 80 , the number of iterations and computational time needed for MCS convergence are significantly reduced. This could be due to that there are some normal state sequences with higher probability newly appearing in the generations ranging from 60 to 80 . At this time, the majority of normal states have been stored in set A, thus MCS will converge quickly.

### 4.2 Optimisation effect of intelligent storage for computational efficiency

For the state sequence randomly generated by MCS, if it is not in the set A, then the OPF calculation must be called for reliability evaluation. In the process of iterations, if the state is in the dynamic fault set, then read the data stored in the dynamic fault set, and it is unnecessary to call the OPF calculation again. The number of state sequences, the number of iterations and the frequency of calling the dynamic fault set are denoted by $T, S$ and $D$, respectively. $T, S$ and $D$ vary with the size of set A changing, which is shown in Table 2.

Table 2 shows that T decreases along with the increase of the size of set A, which means that the optimisation effect of searching normal states would get weakened as the frequency of calling the cross linked list of set A decreases. Set D/S as the frequency of calling the dynamic fault set in the process of iteration. When the size of set A reaches $9019,10,370,11,614$ and $12,845, \mathrm{D} / \mathrm{S}$ are $13.52,12.11,8.45$ and $5.68 \%$, respectively. With the size of set A increases, frequency of calling the dynamic fault set decreases, as a result of which, the optimisation role of dynamic fault set in state evaluation weakens. This is mainly because the size of set A grows bigger, then the probability of large-probability state sequences in dynamic fault set gets smaller. In the case of the number of iterations S decreases, the frequency of calling dynamic fault set decreases. When the number of generations reaches 50 and 60 , the value of D/S is slowly decreased. However, the value of D/S is significantly reduced as the number of generations reaches 70 and 80. When the number of generations reaches more than 70 , the number of iterations needed for MCS convergence is rapidly reduced. The dynamic fault set is constantly updated during the

![img-6.jpeg](img-6.jpeg)

Fig. 7 Convergence process of LOLP and $\beta$ under different pruned levels
Table 1 Iterations of MCS change along with the number of pruned states

| No. of generations | 50 | 60 | 70 | 80 |
| :-- | --: | --: | --: | --: |
| number of pruned states | 9019 | 10,370 | 11,614 | 12,845 |
| iterations | 7535 | 7121 | 4271 | 1637 |
| simulation time, s | 451.06 | 426.29 | 271.59 | 106.15 |

Table 2 Change of $T, S$ and $D$ along with the size of set A

| Size of set A | 9019 | 10,370 | 11,614 | 12,845 |
| :-- | --: | --: | --: | --: |
| $T$ | 21,702 | 19,667 | 12,857 | 4974 |
| $S$ | 7535 | 7121 | 4271 | 1637 |
| $D$ | 1019 | 862 | 361 | 93 |

process of simulation. Accordingly, the size of dynamic fault set is significantly reduced as the number of iterations needed for MCS convergence is significantly reduced. The probability of sampling the same fault state in the iteration process is greatly reduced with the fast decrease in the size of dynamic fault set. Hence the value of D/S is significantly reduced as the generations reach 70 and 80 .

### 4.3 Algorithm comparison

To verify the effect of the improved EDA algorithm and compare the computational performance of different methods, the reliability indices are evaluated for this system using the traditional nonsequential MCS (MCS), genetic algorithms-ISSP (GA-ISSP) [14] and the importance sampling method based on the cross entropy (CE) [8]. Set the variance coefficient $\beta$ of LOLP and EPNS as the convergence index ( $\beta$ is $<5 \%$ ). The algorithms are run using a population of 500 and the number of generations is 80 . The convergence processes of LOLP and EPNS are shown in Figs. 8 and 9. The comparison results are shown in Tables 3 and 4.

Keep the LOLP and EPNS calculated by MCS as the reference. As is shown in Figs. 8 and 9, the convergence values of LOLP and EPNS calculated by above algorithms were close the values calculated by traditional MCS. It confirms the effectiveness and feasibility of the above algorithms. In addition, it is also shown that the coefficient of variation of both LOLP and EPNS converges faster by using the new algorithm compared to the others.

As shown in Tables 3 and 4, the new algorithm has a better accuracy. In terms of computational time and the number of
iterations, the new algorithm improves the efficiency, with less time and less iterations. Compared with GA-ISSP, the superiority is mainly because the correlation between the state of elements and systems is considered in the reproduction pattern of EDA, which achieves the improvement of population characteristic and diversity compared with GA. When the generation reaches 80 , the total probability of all state sequences stored in set A using EDA is $21.76 \%$ higher than with GA. Compared to CE, the computational efficiency is improved, mainly because the pretty high density of loss of load in the pruned state space, and the new algorithm is able to sample the loss of load events in the pruned state space with higher probability compared with CE, thus it converges more quickly. Compared to traditional EDA, on the one hand, the PBIL is improved, thus to avoid the bad effect of the population size in each generation as well as the randomness in the process of reproduction on the population characteristics. On the other hand, with truncation processing and mutation strategy introduced, premature convergence is avoided, improving the excellent characteristics and diversity of the population.

## 5 Conclusion

This paper proposes a new approach based on EDA and intelligent storage to evaluate the reliability of the power system, which is tested in a typical IEEE RTS-79 system. The conclusions are:
(i) Keeping the LOLP and EPNS calculated by MCS as the reference, the proposed algorithm is performed with higher

![img-7.jpeg](img-7.jpeg)

Fig. 8 Convergence process of LOLP and $\beta$ in different algorithms
![img-8.jpeg](img-8.jpeg)

Fig. 9 Convergence process of EPNS and $\beta$ in different algorithms
Table 3 Comparison of LOLP with different algorithms

|  | MCS | GA-ISSP | CE | EDA-ISSP | New algorithm |
| :-- | :--: | :--: | :--: | :--: | :--: |
| LOLP | 0.104 | 0.100 | 0.098 | 0.100 | 0.102 |
| Time, s | 1344.87 | 658.704 | 402.495 | 371.84 | 106.152 |
| Iterations | 21,562 | 10,190 | 6352 | 5734 | 1637 |

Table 4 Comparison of EPNS with different algorithms

|  | MCS | GA-ISSP | CE | EDA-ISSP | New algorithm |
| :-- | :--: | :--: | :--: | :--: | :--: |
| EPNS, MW | 18.156 | 17.526 | 17.628 | 17.643 | 17.663 |
| Time, s | 1991.32 | 1125.24 | 763.14 | 665.12 | 467.08 |
| Iterations | 30,409 | 15,721 | 11,854 | 10,272 | 7326 |

precision and computational efficiency compared with GA-ISSP, CE and EDA-ISSP.
(ii) The computational time for MCS decreases with the increase of the number of normal states pruned, while the computational time for state pruning increases. Thus, in the field of ISSP, the future

research will focus on how to reasonably choose the optimal level of state pruning and harmonise the contradiction between the pruning time and simulation time.
(iii) New energies, such as PV, have a strong dependence on the time sequence. However, the non-sequential MCS method is unable to be conducted with the consideration of the characteristics of time series.

When ISSP is combined with the sequential MCS method, how to reflect the chronological characteristics of system states stored in set A should be further investigated.

## 6 References

[1] Bie, Z., Wang, X.: ‘The application of Monte Carlo method to reliability of power system', Autom. Electr. Power Syst., 1997, (6), pp. 68-75 (in Chinese)
[2] Yang, F., Shi, Y.: 'Research of algorithm for operational reliability of power grid based on distributed computing', Ind. Mine Autom., 2014, 40, (8), pp. $22-25$ (in Chinese)
[3] Huang, J., Guo, R., Zhao, F., et al.: ‘Stratified uniform sampling method for power system evaluation', Autom. Electr. Power Syst., 2012, 36, (20), pp. 1924 (in Chinese)
[4] Song, Y., Guo, Y., Cheng, L.: ‘Monte-Carlo simulation adequacy evaluation for lage-scale power generation and transmission system', Power Syst. Technol., 2003, 27, (8), pp. 24-28 (in Chinese)
[5] Melo, A.C.G., Oliveira, G.C., Morozowski, M., et al.: 'A hybrid algorithm for Monte Carlo/enumeration based composite reliability evaluation', Int. Conf. on Probabilistic Methods Applied To Electric Power Systems, 1991, pp. 7074
[6] Wang, B., Zhao, Y., Liu, W., et al.: 'Power system reliability assessment using importance sampling method with splitting optimal multiplier', Autom. Electr. Power Syst., 2008, 32, (19), pp. 30-34 (in Chinese)
[7] Ridder, A.: 'Importance sampling simulations of Markovian annals of operations research', Ann. Oper. Res., 2005, 134, (1), pp. 119-136
[8] González-Fernend, R.A., da Silva, A.M.L., Resende, L.C., et al.: 'Composite systems reliability evaluation based on Monte Carlo simulation and crossentropy methods', IEEE Trans. Power Syst., 2013, 28, (4), pp. 4598-4606
[9] Hou, Y., Wang, X., Liu, J., et al.: 'A Quasi-Monte Carlo method based power system reliability evaluation', Power Syst. Technol., 2015, 39, (3), pp. 744750 (in Chinese)
[10] Mazundar, M., Gaver, D.P.: 'A comparison of algorithms for computing power generating system reliability indices', IEEE Trans. Power Appar. Syst., 1984, PAS-103, (1), pp. 92-99
[11] Mitra, J., Singh, C.: 'Incorporating the DC load flow model in the decomposition-simulation method of multi-area reliability evaluation', IEEE Trans. Power Syst., 1996, 11, (3), pp. 1245-1254
[12] Singh, C., Mitra, J.: 'Composite system reliability evaluation using state space pruning', IEEE Trans. Power Syst., 1997, 12, (1), pp. 471-479
[13] Mitra, J., Singh, C.: 'Pruning and simulation for determination of frequency and duration indices of composite power systems', IEEE Trans. Power Syst., 1999, 14, (3), pp. 899-905
[14] Green, R.C., Wang, L., Singh, C.: 'State space pruning for power system reliability evaluation using genetic algorithms'. IEEE Power and Energy Society General Meeting., 2010, pp. 1-6
[15] Green, R.C., Wang, L., Alam, M., et al.: 'State space pruning for reliability evaluation using binary particle swarm optimization'. Power Systems Conf. and Exposition (PSCE), 2011 IEEE/PES, 2011, pp. 1-7
[16] Green, R.C., Wang, L., Wang, Z., et al.: 'Power system reliability assessment using intelligent state space pruning techniques: A comparative study'. IEEE 2010 Int. Conf. on. Power System Technology (POWERCON), 2010, pp. 1-8
[17] Cortes, C., Vapnik, V.: 'Support-vector networks', Mach. Learn., 1995, 20, (3), pp. 273-297
[18] Sameverino, C.M.R., Moreno, J.A.: 'Reliability evaluation using Monte Carlo simulation and support vector machine'. Lecture Notes in Computer Science, 2001, vol. 2329, pp. 147-155
[19] Rocco, C.M., Moreno, J.A.: 'System reliability evaluation using Monte Carlo \& support vector machine'. Reliability and Maintainability Symp., 2003, pp. $482-486$
[20] Amjady, N., Elisan, M.: 'Evaluation of power systems reliability by an artificial neural network', IEEE Trans. Power Syst., 1999, 14, (1), pp. 287292
[21] Amjady, N.: 'A framework of reliability assessment with consideration effect of transient and voltage stabilities', IEEE Trans. Power Syst., 2004, 19, (2), pp. 1005-1014
[22] Song, Y., Bu, G., Zhang, R.: 'A fast method for probabilistic reliability assessment of bulk power system using FSOM neural network as system states filters'. IEEE/PES Transmission and Distribution Conf. and Exposition: Asia and Pacific, 2005, pp. 1-6
[23] Wang, S., Wang, L., Fang, C., et al.: 'Advances in estimation of distribution algorithms', Control Decis., 2012, 27, (7), pp. 961-966 (in Chinese)
[24] Zhou, S., Sun, Z.: 'A survey on estimation of distribution algorithms', Acta Autom. Sin., 2012, 27, (7), pp. 961-966 (in Chinese)
[25] Grigg, C., Wong, P., Albrecht, P., et al.: 'The IEEE reliability test system 1996: a report prepared by the reliability test system task force of the application of probability methods subcommittee', IEEE Trans. Power Syst., 1999, 14, (3), pp. 1010-1020