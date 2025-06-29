# Global Optimal Selection of Web Composite Services Based on UMDA 

Shuping Cheng, Xiaoming Lu, and Xianzhong Zhou*<br>School of Management and Engineering, Nanjing University, Nanjing, China chensp70@163.com, zhouxz@nju.edu.cn


#### Abstract

QoS model of composite services and Web services selection based on QoS are currently the hot issues in the web service composition area. Services selection based on QoS, which is a global optimal selection issue, has been proved a NP-HARD problem. Takes engine into account, this paper builds the QoS model of service selection in the Web composite services, uses the estimation of distribution algorithm to solve the NP-HARD problem of services selection, and presents a Web services selection method based on the UMDA. Example analysis and experimental analysis based on the UMDA method are performed; it's proved that the method is effective in solving the NP-HARD problem of Web services selection.


Keywords: Qos, Web Composite Services, Service Selection, UMDA.

## 1 Preface

Researches on Web composite services are attracting more and more attention. The QoS for the composite services and the Web services selection method based on QoS are the hot issues presently.

The present QoS for the composite services only takes the QoS of the member services and the structures of the composite services into account, while the operation of the composite services depends on the engine, which will affect the efficiency of the QoS. The paper, taking the engine into account, rebuilds the QoS for the composite services.

QoS for the Web services depends on QoS of individual service in the combination and the logical structures of the services composited. The current studies show that there are four basic composite structures among the composite services: sequential structure, loop structure, parallel structure and case structure. Based on these four structures, with the known QoS data of the member services, the QoS aggregation method [1] [2] has been put forward. This method supports several common QoS attributes mentioned in the literature [3], such as service price, response time, reliability, and reputation degree. It is common for the academic circle to transform the optimal selection method of the global QoS into a combinatorial optimization problem to find the solutions. There are several optimization methods, such as linear

[^0]
[^0]:    * Corresponding author.

programming method[4][5], constrained optimization method ${ }^{[6]}$, heuristic method[7][8] and genetic algorithm[9][10][11].

Although, to some extent, the current genetic algorithms have solved the service selection problems, they haven't solved some special problems of the composite services. It is necessary to redesign the genetic algorithms of the Web services from the perspective of QoS. The design of the QoS of the composite services will affect the efficiency of the genetic algorithms deeply [12]. This paper builds the UMDA algorithm which supports the global optimal selection of Web composite services. Compared to the existing achievements, the method, based on the genetic algorithms, gives a more complete and effective QoS scheme of the composite services, which has a good adaptability.

# 2 QoS for the Composite Services 

### 2.1 Service Price

Due to the introduction of execution engine, the price of the composite services should be defined as the aggregate value of each member service's price adds the price of the engine:

$$
\operatorname{Pri}(c w s)=\operatorname{pri}(s)+\operatorname{pri}(e)
$$

$\operatorname{Pri}(c w s)$ means the price of the composite services(cws), $\operatorname{pri}(s)$ means the aggregation price of member services, $\operatorname{pri}(e)$ means price of the engine.

According to the mainstream toll mode of the Web services, the toll mode of the engine has two different modes: charging by time and charging by month. The charging by time mode happens when users use the engine, and the charging by month mode means that users can use the engine a certain number of times in a certain period after charged.

### 2.2 Response Time

Besides the aggregate value of the time of the member services, the response time should take the communication time and the treatment time of the engine into account:

$$
T(c w s)=t(s)+\operatorname{tran}(u, e)+\operatorname{pro}(e)
$$

$T(c w s)$ means the response time of the composite services, $t(s)$ means the aggregate value of the time of the member services, $\operatorname{tran}(u, e)$ means the communication time between the users and the engine, $\operatorname{pro}(e)$ means the treatment time of the engine. The estimation process of response time is as follow:

The first step is estimating the $t(s)$. Engine server suppliers should provide the current network parameters, the users should provide the access amount of every member service, and the member service suppliers provide the environment data when the member services are running.

The second step is estimating the $\operatorname{tran}(u, e)$. The $\operatorname{tran}(u, e)$ depends on the network environment between the users and the engine, and this data can be calculated by the network performance and the transmission amount caused by the composite services used by the users.

The third step is estimating the $\operatorname{pro}(e)$. The $\operatorname{pro}(e)$ depends on the complexity of the control logic of the composite services and the performance of the engine.

# 2.3 Reliability 

The reliability of the composite services is the probability of the right response of the services in a longest expected time. The present estimation methods of the Web services just take the aggregation of the reliabilities of the member services into account, while the engine controls the logic and the data flow of the composite services. If the engine fails, the whole operations of the composite services will fail, so the reliability of the engine should be more important than that of the member services. Here is the formula of the reliability of the composite services:

$$
\operatorname{Rel}(c w s)=\operatorname{rel}(s) \times \operatorname{rel}(e)
$$

$\operatorname{Rel}(c w s)$ means the reliability of the composite services, $\operatorname{rel}(s)$ means the aggregate value of the reliabilities of the member services, and $\operatorname{rel}(e)$ means the reliability of the engine. The reliability of the engine should be distributed by the engine suppliers after enough tests.

### 2.4 Reputation Degree

The reputation degree is the satisfaction of the composite services from users. In the problem of the member services selection, the whole reputation degree of the services after composited, as a constraint condition, should be taken into account in estimation of the reputation degree. The paper considers the reputation degree of the engine, besides the reputation degree of the member services. Here is the formula of the reputation degree:

$$
\operatorname{Rep}(c w s)=(1-\alpha) \times \operatorname{rep}(s)+\alpha \times \operatorname{rep}(e)
$$

$\operatorname{Rep}(c w s)$ means the reputation degree of services, $\operatorname{rep}(s)$ means the composite of the reputation degree of member services, and $\operatorname{rep}(e)$ means the reputation degree of the engine. $\alpha$ is a weight coefficient and $\alpha \in[0,1]$, and if $\alpha$ is

bigger, the reputation degree of the engine is more important. Because the engine is very important and irreplaceable in the solution of the selection of the Web services, the range of $\alpha$ should be $\alpha \in(0.5,1]$.

# 3 Selection Method of Web Services Based on UMDA 

### 3.1 Selection Method of Web Services Based on UMDA

The users consider the composite services as a whole and focus on satisfaction of the Qos of the whole under the global constraint condition, which is a global optimal selection problem.

Some assumptions are as follow: There are N tasks in the composite package, $\operatorname{tas} k_{i}(i=1 \sim N)$ means the NO. i task, $\operatorname{Set}_{i}$ means the candidate service set for $\operatorname{tas} k_{i}, M_{i}$ means the service amount in $\operatorname{Set}_{i}$, and $S_{i j}\left(j=1 \sim M_{i}\right)$ means it is NO. j service in the $\operatorname{Set}_{i}$. The global optimal selection problem based on the QoS is a multi-objective optimization problem, and a simple solution for this problem is to change the problem to a single-objective optimization problem. The mathematical description for the problem is as follow:

$$
\begin{gathered}
\operatorname{Max} F(c w s)=\sum_{k=1}^{l} \omega_{k} \times Q f_{k}(c w s) \\
\text { s.t. } Q f_{k}(c w s) \leq B_{k} \quad \text { Or } Q f_{k}(c w s) \geq B_{k} \\
c w s=\left(S_{1 j}, S_{2 j}, \cdots, S_{N j}\right) \\
S_{i j} \in \operatorname{Set}_{i}, i=1 \sim N, j=1 \sim M_{i} \\
\sum_{k=1}^{l} \omega_{k}=1
\end{gathered}
$$

$c w s$ means the composite of the services, $Q f_{k}(c w s)$ means the QoS value of the No.k service in the composite services package, $\omega_{k}$ means weight coefficient, $B_{k}$ means constraint condition of certain QoS.

In the Web service area, there are lots of researches on the traditional genetic algorithms and their improved versions, but there is little on the estimation of distribution algorithm. The paper discusses the solution of global optimal selection problem based on the QoS with the estimation of distribution algorithm.

### 3.2 Selection of the Web Services Based on UMDA

## (1) Narrowing Solution Space

The users hope the global QoS of the composite services is the best and the QoS of every service corresponding to the task is the best too. If there are too many candidate services, the local optimal selection algorithm can be used to calculate the QoS of

every candidate service, and all the services with a QoS value less than a certain threshold will be forsaken, to reduce the amount of the solutions. The threshold is given by the users. It is assumed that after the process above, the amount of the services in the candidate service set is still $\mathrm{M}_{\mathrm{i}}$.

# (2) Coding 

Binary code system is used in UMDA, and every variable is represented by a binary code. If the binary code system is used in the problem of Web service selection, every candidate service will be represented by a binary code, which will cause a long coding, and this is not suitable to the algorithm processing. In this case, the better solution is using the integer array for coding. Please see the structure in figure 1, and the details are as follow:

The integer array is used for representing the entities of the population, and the length of the array, which is the amount of the gens, is equal to the task amount N in the composite package. $G_{i}(i=1 \sim N)$ means the NO. i gen, corresponding to the related $\operatorname{tas} k_{i}$ and $\operatorname{Set}_{i} . G_{i}$ is the number j candidate service in $\operatorname{Set}_{i}$, $j=\left\{1,2, \cdots, M_{i}\right\} ; G_{i}=j$ means the $\operatorname{tas} k_{i}$ will be implemented by the NO. j service in the candidate service set.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Entity Structure

## (3) Population Initialization

In the first step, the population size K should be determined. According to the research between the learning parameter and problem of the UMDA by Shapiro[14], only when the population size is huge enough, the UMDA algorithm can converge to the global optimal solution. The tests of the practical problems show that the population size should be the square root of the amount of the candidate solution. If there are total $\prod_{i=1}^{N} M_{i}$ candidate solutions of service selection, in order to make the

algorithm converge to the global optimal solution, K should be approximately equal the square root of it.

In the second step, the initial probability of every possible value of every gen $G_{i}$ should be determined. If users don't have any preference about certain service in the candidate $S e t_{i}$, the chance of every service is the same. In that case, if the service in $S e t_{i}$ is chosen, the chance of every possible value of $G_{i}$ is the same, and it will be showed as follow:

$$
P\left(G_{i}=j\right)=\frac{1}{M_{i}}, j=1 \sim M_{i}
$$

If the users have certain preference, and could give the probability of every candidate, the initial probability of every possible value comes from users. But in the practice, although the users have the preference about some services, the users can't give the exact probability of every candidate service, especially when the amount of the candidate services is huge. The local optimal selection algorithm is used to calculate the QoS of every candidate service and the sum of QoS of every candidate service, and the probability of every candidate service will be calculated by certain formula.

$$
P\left(G_{i}=j\right)=\frac{Q S_{i j}}{\sum_{j=1}^{M_{i}} Q S_{i j}}, j=1 \sim M_{i}
$$

In the third step, in every candidate service $S e t_{i}$, according to the probability of every candidate service, roulette algorithm is used K times for sampling to get the initial population.

# (4) Fitness Function 

It is applicable that the fitness function is the same with the object function, which means when the constraint conditions are satisfied, and the composite QoS of composite services influenced by the engine is taken into account, the formula is:

$$
f(c w s)=\sum_{k=1}^{t} \omega_{k} \times Q f_{k}(c w s)
$$

Because the amount of the composite schemes is too huge to calculate all the QoS of the possible composite services, $\omega_{k}$ is given directly by the users, not by the objective data, which is different from the method of the local optimal selection algorithm.

## (5) Selection Mechanism.

The selection mechanism is the foundation of the probability updating. Numbers of the distribution relations inherited from the old generation population by the new

generation population are called selection pressure, which depends on selection mechanism. In the case that the proper selection mechanism is chosen, the selection pressure will keep population diversity and increase the possibility of the global optimal converging. It can also guarantee the high amount of the optimal entities during the evolution, and the algorithm converges fast. Similar with the genetic algorithm, the selection mechanisms of the EDA include sorting algorithm, roulette algorithm, tournament selection algorithm, and random traversal sampling algorithm.

The paper uses the sorting algorithm. First, the QoS of the composite services of every entity of the population is calculated, and those unsatisfied with the constraint condition will be discarded. Then, after calculating the fitness values of the left entities by the fitness function, the fitness values will be sorted from maximum to minimum, and the excellent ones with high fitness value will be selected according to certain rate. In order to keep the population diversity, the rate should be around $50 \%$.

# (6) Probability Updating and Resample 

According to values of the gens of the selected optimal entities, the frequencies of the values of every gen are calculated. The probabilities of values of every gen are updated by the value calculated as the frequencies divided by total amount of the optimal entities. According to the new probabilities, every gen will be sampled K times by the roulette algorithm, and there will be K new entities then, which will form a new generation population.

## (7) Stopping Rule

There are three common types of terminal conditions: the generation of evolution achieves the set value; the fitness value of the entity achieves the set value; and there is less likely a big change in the next generation. Normally, the generation of evolution of the population is large enough; the evolution should converge to certain optimal entity; or the evolution stops at the set value accepted by the users.

As the other evolutionary algorithms, the solution of the EDA depends on the related parameters and methods, and the solution may be not the optimal one. For the problem of the selection of the Web services, if there are too many composite schemes, the suboptimal solution calculated by the EDA is acceptable.

## 4 Simulation and Comparison

Some tests with the simulation data will be used in this part to verify that EDA is efficiency to solve the selection of the Web services based on QoS under the big solution space. Both the efficiency of the EDA and the efficiency of the genetic algorithm will be analyzed in this part.

There are 4 types of the QoS attributes, the values of the attributes are randomly generated, and the weight is $\omega=(0.4,0.2,0.2,0.1,0.1)$. The related data of the engine here is the same as that in the real example. There are N tasks in the composite services, the amount M of the candidate services of every task is the same, the generation size is

K, and the generation of the evolution is P . Different Ns and Ms are used in different experiments, and the algorithm will run 50 times in every experiment. If the convergence fails even the operation of the algorithm is over, the maximal fitness value of the entity in the last generation is used as the statistical data.

# 4.1 Simulation Result 

The related data is as follow:
(1) N is $5, \mathrm{~K}$ is 100 , the value of M is changing, and the stopping rule is that P is 200 or convergence finishes in advance.
(2) N is $5, \mathrm{~K}$ is 100 , the value of M is changing, and the stopping rule is that the maximal fitness value achieve the set value or convergence finishes in advance.
(3) M is $10, \mathrm{~K}$ is 100 , the value of N is changing, and the stopping rule is that P is 200 or convergence finishes in advance.
(4) M is $10, \mathrm{~K}$ is 100 , the value of N is changing, and the stopping rule is that the maximal fitness value achieve the set value or convergence finishes in advance.
![img-3.jpeg](img-3.jpeg)

Fig. 2. Comparison of the average optimal fitness value
![img-3.jpeg](img-3.jpeg)

Fig. 3. Comparison of the average evolution generation
![img-3.jpeg](img-3.jpeg)

Fig. 4. Comparison of the average optimal fitness value

Fig. 5. Comparison of the average evolution generation

# 4.2 The Efficiency of EDA 

From the comparison:
(1) When the stopping rule is the evolution generation, if the N is fixed, the fluctuation of the convergence evolution generation is small when M increases; if the M is fixed, the convergence evolution generation increases when N increases; and the EDA converges very fast to a good fitness value.
(2) If the stopping rule is a maximal fitness value, N is fixed, and the fluctuation of the evolution generation of EDA when the maximal fitness value achieves is small when M increases; M is fixed, and the evolution generation of EDA when the maximal fitness value achieves increases when N increases; and the maximal fitness value of EDA achieves fast under a small evolution generation, and it sometimes happens that the algorithm converges fast to the value less than the maximal fitness.

It shows that the satisfied suboptimal solution can be steadily achieved in a small evolution generation, and the better composite scheme can be found for the selection of the Web services with EDA.

### 4.3 Comparison

It shows that EDA is more efficiency than the traditional genetic algorithm in literature[11] in the selection of the Web services:

The convergence speed of EDA is fast than that of GA. If the generation size and the stopping rules (the evolution generation) are the same, the optimal fitness value of EDA is better than that of GA. If the generation size and the stopping rules (the optimal fitness value) are the same, the evolution generation of EDA is much less than that of GA.

Additionally, this experiment just proves that the EDA in this paper is better than the traditional genetic algorithm in literature[11] in the selection of the Web services, which doesn't mean the EDA is better than the traditional genetic algorithm. The operations of the two algorithms depend on the coding, evolution and the parameters.

## 5 Conclusion

The paper discusses the selection of the web services based on QoS, introduces the EDA which is a global optimal selection scheme to solve the NP-HARD problem. The paper introduces the solution of the selection of the Web services based on the UMDA, designs the algorithm, performs example analysis and experimental analysis, and verifies that the UMDA is efficient to solve the problem.

Acknowledgement. This research was supported by: (i) the National Planning Office of Philosophy and Social Science under Grant 11\&ZD169; (ii) the NSFC under Grant 70971061 and 71171107.
