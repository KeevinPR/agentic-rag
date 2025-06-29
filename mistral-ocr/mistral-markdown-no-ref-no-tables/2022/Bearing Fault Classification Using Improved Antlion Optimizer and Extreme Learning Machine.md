# Research Article 

## Bearing Fault Classification Using Improved Antlion Optimizer and Extreme Learning Machine

Zhuanzhe Zhao ${ }^{\circledR}$, ${ }^{1,2}$ Yu Zhang, ${ }^{1}$ Qiang Ma, ${ }^{1}$ Yujian Rui ${ }^{\circledR}$, ${ }^{1}$ Guowen Ye, ${ }^{1}$ Mengxian Wang, ${ }^{1}$ Yongming Liu ${ }^{\circledR}$, ${ }^{1,3}$ Zhen Zhang, ${ }^{1,2}$ Neng Wei, ${ }^{2}$ and Zhijian $\mathrm{Tu}^{2}$<br>${ }^{1}$ School of Mechanical Engineering, Anhui Polytechnic University, Wuhu, Anhui 241000, China<br>${ }^{2}$ Wuhu Ceprei Robotics Industry Technology Research Institute Co. Ltd., Wuhu, Anhui 241003, China<br>${ }^{3}$ Anhui New R\&D Institutions of Human-machine Interaction and Collaboration, Wuhu, Anhui 241000, China

Correspondence should be addressed to Yongming Liu; liuyongming1015@163.com
Received 4 June 2021; Revised 12 April 2022; Accepted 21 April 2022; Published 18 May 2022
Academic Editor: Aniello Riccio
Copyright © 2022 Zhuanzhe Zhao et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

Bearing is an important part of rotating machinery, and its early fault diagnosis and accurate classification have always been difficult in engineering application. At present, the models based on the fusion of various optimization algorithms and neural networks have become one of the emerging techniques for accurate fault identification. Firstly, an improved antlion optimizer (ALO) algorithm based on estimation of distribution algorithm (EDA) and variable-step Lévy flight strategy, abbreviated as ELALO, is proposed as a new bionic intelligence. During the initialization of population, the individuals with poor fitness are redistributed by the Gaussian probability model. In view of the stagnation of iteration, Lévy flight strategy is introduced and the adaptive change of disturbance step length is controlled. Experimental results on 4 benchmark functions show that the novel ELALO can effectively improve the solution accuracy and convergence speed, compared with the original ALO. Secondly, in order to solve the disadvantage that extreme learning machine (ELM) network is easy to fall into local optimization, this ELALO algorithm is used to initialize the weights and thresholds of its network and to form the new pattern recognition model, ELALOELM. Finally, the bearing data of 8 patterns from Western Reserve University are decomposed by local mean decomposition (LMD), and then the symbolic entropy (SE) of the first three product function (PF) components signals is extracted and used as the input eigenvectors. Compared with the standard ELM and ALO-ELM models, the ELALO-ELM model has better generalization and stronger robustness and it can effectively improve the efficiency of network training and the accuracy of early fault pattern classification in bearing fault diagnosis. The new ELALO-ELM model can also be used for other difficult classification problems.

## 1. Introduction

Bearing is one of the most widespread and important parts in mechanical equipment. The classification of early faults of bearings is a very important issue in practical applications, which has attracted the attention of many scholars and engineers. Due to the complex structure of most mechanical equipment, there is a nonlinear coupling relationship between components. And the weak non-stationary bearing fault signal is often submerged in the environmental noise. All these have caused some difficulties for the accurate
classification of early faults of bearings. At present, there are three main types of fault diagnosis and classification methods for bearing: model-based methods, knowledgebased reasoning methods, and data-driven methods. The model-based method explored the operating laws of bearings by constructing accurate mathematical models and obtained the related information of normal and abnormal operation by studying the internal relationship between dynamic parameters and response signs under fault conditions. In the literature [1], a dynamic model considering the time-varying deflection excitation (TDE) and the time-

varying contact stiffness excitation (TCSE) is introduced to investigate vibration responses of a lubricated rolling bearing with a uniform and a non-uniform surface waviness on its races. To investigate the vibration mechanism of cylindrical roller bearings with localized defects, Cao et al. [2] developed the dynamic models with gyroscopic moment, centrifugal force, and lubrication traction/slip between roller/raceway, roller/cage, and cage/raceway. However, with the increasing complexity of mechanical systems and more coupling factors, the accurate mathematical models are becoming more and more difficult to establish. The method based on knowledge reasoning does not require the accurate mathematical model of the system, but carries out computational reasoning and classification, such as fault treebased reasoning [3], DS theory [4], and expert system [5]. These methods usually require a large amount of domain expert knowledge, knowledge expression, and reasoning mechanism. Therefore, it is difficult for its large-scale application in case of incomplete or lack of domain knowledge. The data-driven diagnosis method, such as machine learning, does not need to understand the physical structure and the precise mathematical model, nor does it require a large amount of accumulation of expert knowledge. It only uses measurable condition monitoring signals or historical data to analyze and extract characteristic information, so as to realize the fault diagnosis, classification, and performance evaluation of bearings. A condition monitoring index of bearings was developed based on self-organizing map (SOM) and improved hidden Markov model so as to detect incipient bearing faults quickly [6]. In the literature [7], a three-stage semisupervised learning approach using data augmentation and metric learning is proposed for an intelligent bearing fault diagnosis under limited labeled data. Wen et al. [8] proposed a novel method that integrates graph theory and singular value decomposition (SVD) with the purpose of inspection of dynamic rolling element bearings health conditions. The data-driven method has attracted the great attention of researchers, and its application in the intelligent fault diagnosis has become more and more extensive.

In recent years, various pattern recognition models emerge in an endless stream, such as the support vector machine (SVM) [9], variable prediction model [10], neural network [11], and deep learning [12, 13]. Ravikumar et al. [14] proposed a fault diagnosis model that includes a multiscale deep residual learning with a stacked long short-term memory (MDRL-SLSTM) to cope with sequence data in a gearbox health prediction process in an internal combustion engine. A novel learning rate scheduler based on the reinforcement learning (RL) for convolutional neural network (RL-CNN) [15] is presented and applied in fault classification of three bearing datasets. As a single hidden layer feedforward neural network, extreme learning machine (ELM) has also been widely used by researchers. But it also has some disadvantages. For example, the input weights and thresholds of the ELM network are randomly generated, and some almost worthless nodes will inevitably be generated, which will cause the solution accuracy of ELM model to decrease seriously, or even fall into local convergence [16].

Some optimization algorithms have been tried in the literature to improve the performance of ELM networks. For example, Zeng et al. [17] combined ELM with an improved particle swarm optimization (PSO) algorithm that added a delay factor to short-term load forecasting of power systems, to avoid the addition of unnecessary hidden layer nodes and overtraining, and to improve the generalization of ELM networks. Jiang et al. [18] proposed an ELM model combined with a compound differential evolution algorithm and applied it to the prediction of the silicon content of molten iron in a blast furnace. Kadri et al. [19] applied an ant colony (ACO) algorithm with ELM in the fault detection and identification of cement rotary kilns. Wang et al. [20] introduced a fault diagnosis scheme based on multi-scale diversity entropy (MDE) and ELM, which was verified by simulated signals and two experimental data from the bearing and the dual-rotator of the aeroengine test in gears.

Swarm optimization algorithm, such as the PSO and ACO , is a kind of algorithm inspired by the intelligent cooperation of biological groups. It has the advantages of easy implementation, good parallelism, and strong adaptability. Recently, new meta-heuristics optimization algorithms based on bionics have sprung up one after another, such as slap swarm algorithm (SSA) [21], the monarch butterfly optimization (MBO) [22], slime mould algorithm (SMA) [23], moth search algorithm (MSA) [24], hunger games search (HGS) [25], colony predation algorithm (CPA) [26], marine predator algorithm (MPA) [27], Harris hawks optimization (HHO) [28], mayfly algorithm (MA) [29], reptile search algorithm(RSA) [30], and honey badger algorithm (HBA) [31]. As a bionic intelligence algorithm, the antlion optimizer (ALO) simulates the predation mechanism of the antlions in the natural environment [32]. Due to few parameters and high convergence accuracy, it has been used in motor control [33, 34], path planning [35], multiobjective optimization [36], scheduling optimization [37, 38], and other fields [39, 40]. According to the no free lunch theorem [41], there is no optimization algorithm that can be universally used in all engineering fields, and the performance of all optimization algorithms on all possible function sets is equivalent. When ALO is used to solve actual complex engineering problems, there are several shortcomings, such as easy precocity of populations. Therefore, some variants of ALO have been proposed in different applications. For example, Yue and Zhang [42] employed a new inertial weight strategy and integrated invasive weed optimization algorithm (IWOA) and bat algorithm (BA) to further improve the performance of the original ALO. Kilic et al. [43] proposed an improved random walk model for the long time-consuming process of ALO, which uses the tournament selection method instead of roulette to improve the global search efficiency of ALO. An improved ALO based on spiral complex path searching pattern is proposed to improve the diversity of the population and the ability of the algorithm to balance exploration and exploitation [44]. Tharwat and Hassanien [45] proposed a new ALO algorithm based on chaos theory and applied it to optimize the initial parameters of SVM model. The classical Lévy flight is also used to improve the ALO [46-48]. The Lévy flight random

walk was suggested as a permutation for performing a local search in Ref. [46], and it is utilized to replace the random walk as the motion of ants in Ref. [47]. But in Ref. [48], it is essentially the fusion of the group search optimization (GSO) algorithm and ALO; that is, the better solutions are selected from the initial random solutions, and they are updated using GSO, whereas the remaining initial solutions are updated using ALO. In the above 3 literatures, the step size control factor $w$ of Lévy distribution is constant and is simply used. The deep fusion with the Lévy strategy is not carried out according to the actual situation.

Therefore, in order to accurately classify the early faults of rolling bearings, a new pattern recognition model based on the improved ALO algorithm and ELM network is proposed in this paper. Firstly, the estimation of distribution algorithm (EDA) and a variable-step Lévy flight strategy are introduced into the initial ALO, called ELALO. To avoid the problem of local optimum and instability during ELM training process, the new ELALO is used to optimize the initial parameters of ELM network and the new pattern recognition is formed, denoted as ELALO-ELM. The experimental results show that the recognition rate of ELALOELM model is improved significantly through the case of rolling bearing early fault classification.

The remainder of this paper is organized as follows. The proposed ELALO algorithm is dictated in Section 2, where the superiority of ELALO over conventional ALO is demonstrated by a comparative study. Section 3 introduces the ELALO-ELM network model and its structure, and then applies the hybrid model to the early fault classification of rolling bearings in the area. Section 4 introduces the experimental comparative study using ELM and ELALO-ELM network models. Section 5 summarizes this article.

## 2. Improved Antlion Optimizer

2.1. Antlion Optimizer. ALO is a meta-heuristic intelligent algorithm that mimics the hunting mechanism of antlions in nature [32]. Five hunting steps are extracted on the predation process, that is, the random walk of ants, trap mining of antlion, ants falling into the trap, antlion preying on ants, and trap reconstruction. According to the above steps, a mathematical model of antlion hunting and ALO algorithm is established. The interactions between ants and antlions in the above steps are all reflected in vectors in multi-dimensional space. In order to expound the meaning of the formula, all the following models are constructed based on dimension $D=1$.
(1) The ants walk randomly in the solution space, and the walk step formula can be described as follows:

$$
\begin{gathered}
r w(1)=\left\{\begin{array}{cc}
1, & \text { rand }<0.5 \\
-1, & \text { rand } \geq 0.5
\end{array}\right. \\
r w(t+1)=\sum_{i=1}^{T} r w(t)
\end{gathered}
$$

In Equations (1) and (2), $r w(1)$ represents the initial step value of the first generation of ants to walk. $T$
![img-0.jpeg](img-0.jpeg)

Figure 1: A schematic diagram of a random walk around the trap of ALO.
represents the maximum number of iterations, and $t$ is the number of current iterations. $r w(t)$ is the walking step length of the ant from the starting point in $(t+1)^{\text {th }}$ and the step length value is equal to the cumulative sum of all previous generation steps. The rand takes a random number between 0 and 1.
(2) Antlion digs traps with itself as the center. The process maps to a multi-dimensional space equivalent to constructing a super-sphere trap model near the antlion. The two-dimensional form of the model is shown in Figure 1. Equations (3) and (4) can be used to transform the initial boundary range of the algorithm into a trap enclosure centered on the antlion as follows:

$$
\begin{aligned}
& c_{r}(t)=a l_{x}(t)+c(t) \\
& d_{r}(t)=a l_{x}(t)+d(t)
\end{aligned}
$$

In Equations (3) and (4), $c(t)$ and $d(t)$, respectively, represent the upper and lower bounds of the generation $t$ trap. $a l_{x}(t)$ represents the antlion individual, which is selected as $X_{r s}$ by the roulette strategy or $X_{e}$ by the elite strategy in the generation $t$ trap. $c_{r}(t)$ and $d_{r}(t)$, respectively, represent the upper and lower bounds of the coordinate of the generation $t$ trap relative to the coordinates of the antlion $a l_{x}(t)$.
(3) To prevent ants from randomly walking beyond the boundary, the standardization of the walking range is carried out by the following:
$R_{s, d}(t)=\frac{(r w(t)-a(T)) \cdot\left(b(T)-c_{r}(t)\right)}{d_{r}(t)-a(t)}+c_{r}(t)$,
where $R_{s d}(t)$ represents the standardized random walking step length of the $t^{\text {th }}$ generation. $a(T)$ and $b(T)$, respectively, represent the maximum and minimum of the walking step length of the ant after reaching $T$ times of walking around the antlion.
(4) The random walk of each ant in the range of $X_{r s}$ and $X_{e}$ can be expressed as

$$
\operatorname{ant}(t+1)=\frac{R_{r x}(t)+R_{e}(t)}{2}
$$

![img-1.jpeg](img-1.jpeg)

Figure 2: Flow chart of EDA.
where ant $(t+1)$ represents the updated ant individual of the generation $t+1$. When the center antlion, which is surrounded by ants, is determined by the $X_{v o}, R_{s d}(t)$ can be recorded as $R_{v s}(t)$. Similarly, when the center antlion, which is surrounded by ants, is the elite antlion $X_{e}, R_{e d}(t)$ can be recorded as $\operatorname{Re}(t)$.
(5) The antlion pulls the ant inside sand and consumes its body. This process occurs under the condition that the fitness value of the ant is better than that of the antlion, and the antlion will replace the ant's position. If the minimum fitness value is optimal, the process can be described as
$a l(t+1)=\left\{\begin{array}{l}\operatorname{ant}(t+1) \quad \text { if } f(\operatorname{ant}(t+1))<f(a l(t)) \\ a l(t) \quad \text { otherwise }\end{array}\right.$
(6) When the grain reserves are exhausted, the antlion will repair the traps to wait for the next hunting. For this behavior, ALO algorithm is assumed that the scope of the trap will be adaptively reduced with the iterative process to improve the ability of local
optimization. Mathematical models are shown in Equations (8) and (9):

$$
\begin{aligned}
& c(t)=\frac{c(t-1)}{I(t)} \\
& d(t)=\frac{d(t-1)}{I(t)}
\end{aligned}
$$

where $I(t)=10 w t / T$, and $w$ is given different constant values in different iterative stages of the algorithm.

### 2.2. Improved Antlion Optimizer

2.2.1. Introduction of an Estimation of Distribution Algorithm. The EDA [49] is an algorithm like genetic algorithm that uses the strategy of establishing a probability model to replace the population optimization change of the genetic operator. According to the different learning and sampling forms of probabilistic models, EDA has developed many different forms of algorithms, which are widely used in multi-objective optimization [50], path planning [51], machine learning [52], hierarchical cluster analysis [53, 54], and other fields.

According to the differences of the variable forms constructed by the probability model, EDA can be divided into the discrete type and the continuous type. This article mainly deals with the usage of the continuous EDA. The algorithm flow chart is shown in Figure 2.

Based on the probability model calculated by each generation, EDA generates new individuals based on the probability model calculated by each generation, which breaks through the range limitation of ALO random walk and makes it easier to achieve the global optimum. Since each generation of EDA is generated based on a probabilistic model, it is not only effective in solving nonlinear coupling problems, but also can directly describe the evolutionary trend of the population from a macro level. On this basis, the EDA probability model is introduced into the initial ALO model to realize the idea of population generation. The ALO algorithm in the population generation stage includes the initial population stage and the stage where the antlion and ant populations are mixed to form the next generation population at the end of each generation. In these newly generated populations, individuals with a certain fitness value are selected (the selection rate in this paper is $50 \%$ ). And the average and variance of each individual dimension are calculated and used to build a Gaussian probability model. Individuals randomly generated by the probability model replace some of the individuals in the population that are lagging in fitness. Given that $z$ dominant individuals are selected to construct the model, the set of positions of the $i^{\text {th }}$ dimension $z$ individual positions is $U^{i}=\left(u_{1}^{i}, u_{2}^{i},, u_{z}^{i}\right)$.

$$
A^{i}=\operatorname{gauss}\left(\tilde{u}^{i}, \varepsilon^{i}\right)
$$

where gauss () indicates that a new population $A^{i}$ that meets the requirements of mean $\tilde{u}^{i}$ and variance $\varepsilon^{i}$ is generated within the scope of the $i^{\text {th }}$ dimensional solution space.

![img-2.jpeg](img-2.jpeg)

Figure 3: Lévy flight trajectory of the generation 100.
2.2.2. Introduction of Variable Step Size Lévy Flight Strategy. The Lévy flight is an optimization strategy obeying the Lévy probability distribution [55]. The principle of Brownian motion in physics can correspond to this search strategy well. In the cuckoo algorithm [56], the bird renewal formula is based on this model. Lévy flight can quickly change the orientation in the solution space, so when applied to the optimization field, it can guide the algorithm to quickly jump out of the local optimum and improve the performance of the algorithm. The position updating formula of Lévy flight is as follows [57]:

$$
p_{i}^{t+1}=p_{i}^{t}+\omega \oplus s, \quad i=1,2, \ldots, A
$$

where $p_{i}$ represents the $i^{\text {th }}$ individual position in the population and the superscript indicates the current generation of the individual. The product $\oplus$ means entry-wise multiplications and $\omega$ represents the step adjustment factor which should be related to the scales of the problem of interest. $A$ is the population size and $s$ represents a random step. As the implementation of the Lévy distribution mathematical model is relatively complicated, the Mantegna algorithm is commonly used in practical applications to simulate the Lévy distribution. The algorithm model is as follows.

The random step length $s$ is calculated as

$$
s=\frac{\mu}{|v|^{1 / \zeta}}
$$

where $\mu$ and $v$ are Gaussian distributions and satisfy Equations (13) and (14):

$$
\begin{aligned}
& \mu \sim N\left(0, \sigma_{\mu}^{2}\right) \\
& v \sim N\left(0, \sigma_{v}^{2}\right)
\end{aligned}
$$

where $\sigma_{v}=1$ and $\sigma_{\mu}$ is expressed as follows:

$$
\sigma_{\mu}=\left[\frac{\Gamma(1+\zeta)^{*}}{\Gamma\left[(1+\zeta) / 2\right] \zeta^{*} 2^{(\zeta-1) / 2}}\right]^{1 / \zeta}
$$

In (15), the value of symbol $\zeta$ is generally1.5.
Taking the coordinate origin $(0,0)$ as the initial point, the Lévy flight trajectory of the generation 100 is shown in Figure 3.

Figure 3 verifies the characteristics of the combination of long and short jump distances of Lévy flight, and it is very helpful to fully explore the solution space. After the Gaussian probability model of EDA is added to ALO, the search accuracy of ALO is improved, but the number of iterations is limited in practical application, and it is particularly important to accelerate the speed of jumping out of the local optimum. According to the Lévy perturbation method made by the PSO algorithm in [58], the new strategy, which integrated the step shrinkage factor and the particle swarm inertia weight parameter with similar function characteristics (which should follow the previous step to strengthen the global convergence ability and the feature of strengthening the local optimization ability in the later stage), is proposed and applied to ALO. Specific steps are as follows.

Step 1. After each iteration of ALO, it is judged whether the fitness value of the elite individual changes within 3 generations. If there is no change, enter Step 2. Otherwise, enter the next iteration.

Step 2. Take the elite individual as the parent and perform $g$ Lévy flights to generate a candidate point set containing $g$ points. Elite individuals follow (16)-(18) for Lévy disturbance. One can see that

$$
\begin{aligned}
& P_{t}=\left\{p_{t}^{1}, p_{t}^{2}, \cdots, p_{t}^{g}\right\} \\
& p_{t}^{i}=e_{t}+\omega_{t} \oplus s, \quad i=1,2, \cdots, g \\
& \omega_{t}=\omega_{\max }-\left(\omega_{\max }-\omega_{\min }\right) \frac{t}{T}
\end{aligned}
$$

where $P_{t}$ is the candidate set of the $g$ elements of the $t^{\text {th }}$ generation and $P_{t}^{i}$ represents the $i^{\text {th }}$ element in $P_{t} . e_{t}$ represents the elite individuals obtained by the generation $t$ fused with EDA and the symbol $\omega t$ represents a linearly decreasing random step adjustment factor, where its maximum and minimum values are $\omega \max =0.8$ and $\omega \min =0.1$, respectively.

Step 3. Judge whether the candidate point set is superior to the elite individual of the current generation. And if so, replace the elite individual of the current generation with the elite individual of the next generation. Otherwise, elite individuals of this generation are retained. One can see that

$$
\left\{\begin{array}{l}
e_{t+1}=\min \left(f\left(P_{t}\right)\right) \quad \text { if } \min \left(f\left(P_{t}\right)\right)<f\left(e_{t}\right) \\
e_{t+1}=e_{t} \quad \text { otherwise }
\end{array}\right.
$$

The new improved algorithm based the above two strategies is called as ELALO. To summarize, the process of ELALO algorithm is shown in Figure 4.

![img-3.jpeg](img-3.jpeg)

Figure 4: Flow chart of ELALO algorithm.
2.3. Verification with Simulation Studies. In order to test the optimize performance of ELALO, sphere function $\left(F_{1}\right)$, Ackley function $\left(F_{2}\right)$, Lévy function $\left(F_{3}\right)$, and Rosenbrock's valley function $\left(F_{4}\right)$ are used in this simulation experiment. The specific expressions are shown in reference [59].

The sphere function is a typical nonlinear symmetric benchmark function and is mainly used to test the solution accuracy and speed of the algorithm in practical applications. The Ackley function is a multimodal function with particularly dense peaks and troughs. Lévy function is a complex multimodal function, where many algorithms will fall into the premature state and cannot get the global optimal solution. Multimodal functions are mainly used to test the algorithm's ability to jump out of local optimum. The Rosenbrock's valley function is a typically ill-conditioned, non-convex, and uni-modal function which is difficult to minimize, and there is an obvious correlation between variables. The mesh graphic of 4 benchmark functions $(D=2)$ is shown in Figure 5.

According to the recommended values in references [32, 55-57], the basic parameters of the four algorithms are
the same, such as the population size $A=500$, and the maximum number of iterations $T=2000$. And in Lévy flight process, the time $g$ is set to 100 . Other parameters of PSO and GA are set according to Ref. [17, 21], as shown in Table 1.

Each algorithm runs 50 times independently. The dimension of the four benchmark functions is $D=15$. The mean is used as the accuracy index, the best is used as the global optimization performance index, and the variance is as the stability index. The $p$-values mean the result of the Wilcoxon rank-sum test over benchmark functions. The statistical results are shown in Table 2.

It can be seen from Table 2 that the mean value of ELALO algorithm in function $F_{2}$ is $4.76 \mathrm{E}-15$. Compared with 1.79E-01 corresponding to initial ALO, ELALO algorithm has 14 orders of magnitude advantages and has similar performance in functions $F_{1}, F_{2}$, and $F_{4}$, which fully indicates that the convergence accuracy of the improved algorithm has been significantly improved. In the test function $F_{2}$, the optimal value of ELALO algorithm is 2.95E-13. Compared with 1.30E-06 corresponding to initial ALO, its global optimization performance is improved. And there are similar

![img-4.jpeg](img-4.jpeg)

Figure 5: Mesh graphic of four benchmark functions $(D=2)$ :(a) Sphere function $\left(F_{1}\right)$. (b) Ackley function $\left(F_{2}\right)$. (c) Lévy function $\left(F_{3}\right)$. (d) Rosenbrock's valley function $\left(F_{4}\right)$.

Table 1: Other parameters setting of GA and PSO.

conclusions on functions $F_{1}, F_{3}$, and $F_{4}$. The variance of ELALO algorithm in function $F_{3}$ is 3.21E-25. Compared with the corresponding variance of ALO algorithm $(4.73 \mathrm{E}+04)$, it has an advantage of nearly 29 orders of magnitude, which strongly proves the stability of ELALO and has similar conclusions on functions $F_{1}, F_{2}$, and $F_{4}$. Compared with PSO, ELALO algorithm is better than PSO except the $F_{3}$ function. When solving the multimodal function $F_{3}$, the average accuracy of the solution is the same order of magnitude, but its variance is less than PSO, indicating that the stability of ELALO algorithm is better than PSO. Compared with GA, there is a similar situation, except for solving $F_{4}$. When solving the ill-conditioned uni-modal function $F_{4}$, the stability of GA is better than ELALO. Overall, the performance of ELALO algorithm has been significantly improved.

The Wilcoxon rank-sum test is a famous nonparametric test in statistics theory that can be applied to determine if two sets of solutions (population) are different statistically
significant or not. In this way, each set of pairs in both populations is compared to calculate and analyze their numerical differences. It also tests the null hypothesis as to whether both populations are of the same distribution. In short, the Wilcoxon rank-sum test returns a numerical result called $p$-value. A $p$-value determines the significance level of two algorithms. In this work an algorithm is statistically significant if and only if it results in a $p$-value less than $5 \%$. The $p$ values in Table 2 also show that this superiority is statistically significant since all $p$-values are much less than $5 \%$, which further reflect the robustness of ELALO algorithm.

In order to intuitively distinguish the performance characteristics of the two algorithms, the convergence curves of the two algorithms in each test function are shown in Figure 6. In particular, the value on the convergence curve is the average after 50 independent operations of the two algorithms.

In Figure 6, the abscissa is the number of iterations of the algorithm, and the maximum number of iterations is 2000 generations. In order to make a clear distinction between the algorithm iteration curves, the logarithm of the fitness value with base 10 is taken as the ordinate. The optimization accuracy of ELALO has been significantly improved. When the algorithm reaches the same accuracy in the early stage,

Table 2: Comparison results in four benchmark functions.

![img-5.jpeg](img-5.jpeg)

Figure 6: Comparison of convergence curve. (a) Curve comparison on $F_{1}$, (b) curve comparison on $F_{2}$, (c) curve comparison on $F_{3}$, and (d) curve comparison on $F_{4}$.

the convergence speed of the ELALO is also higher than the initial ALO. Hence, one can see that the proposed ELALO algorithm has a good convergence.
2.4. Time Complexity Analysis. Time complexity is the key factor of algorithm performance and reflects the operation efficiency of the algorithm. In ALO, the population size is $A$, the individual dimension is $D$, and the maximum number of iterations is $T$. Suppose that the time to generate the random number and calculate the position of randomly distributed ants in each dimension is $\delta_{1}$, the time to calculate the fitness value of the objective function according to the ant position is $f(D)$, and the time to sort according to the ant fitness and select the optimal solution is $\delta_{2}$. Because the initial position of the ant and antlion is the same, the initial position of the elite antlion is the optimal solution selected from ant population. Therefore, the time complexity of population initialization stage is $O\left(A\left(D \delta_{1}+f(D)+\delta_{2}\right)\right)=O(D+f(D))$. After entering the iterative process, the time when the antlion is selected is $\delta_{3}$, the time when the ants generate the position and judge the walking direction around an antlion is $\delta_{4}$ and $\delta_{5}$, respectively, the time for the ant to change the boundary in the process of walking is $\delta_{6}$, and the time when the ant obtains the new position after walking is $\delta_{7}$. The time to calculate the fitness value according to the ant position is $f$ $(D)$ and the time of fitness value comparison and position replacement between ant and antlion is set to $\delta_{8}$. So, the time complexity of this stage is $O\left(T\left(A\left(\delta_{4}+\delta_{5}+\delta_{7}+f(D)+\delta_{8}\right)+\right.\right.$ $\left.\left.\delta_{3}+\delta_{6}\right)\right)=O(f(D))$. Therefore, the maximum time complexity of ALO algorithm is $O(D+f(D))+O(f(D))=O(D+f$ (D)) $[60]$.

The population size, dimension, maximum number of iterations, and the time to solve the value of objective or fitness function of ELALO algorithm are the same as those of ALO. Therefore, the time complexity of population initialization stage is the same as that of ALO; that is, $O\left(A(D\right.$ $\left.\delta_{1}+f(D)+\delta_{2}\right)\right)=O(D+f(D))$. After entering the iteration, suppose that the time to construct the Gaussian distribution probability model with EDA is $\tau_{1}$, the time to eliminate the individuals with poor fitness value is $\tau_{2}$, the time to generate new individuals according to EDA is $\tau_{3}$, the time to generate elite individuals by Lévy flight is $\tau_{4}$, the time to compare the fitness values of the old and new elite individuals is $\tau_{5}$, and the time to judge whether to replace is $\tau_{6}$. Other calculation times are the same as those in ALO algorithm. So, the time complexity of this stage is $O\left(T\left(A\left(\delta_{4}+\delta_{5}+\delta_{7}+2 f(D)+\delta_{8}\right)+\right.\right.$ $\left.3 \tau_{1}+3 \tau_{2}+3 \tau_{3}+\tau_{4}+\tau_{5}+\tau_{6}+\delta_{3}+\delta_{6}\right)\right)=O(f(D))$. Therefore, the total time complexity of ELALO algorithm is also $O(D+f$ (D) $)+O(f(D))=O(D+f(D))$.

It can be seen from the above analysis that compared with the initial ALO, the time complexity of ELALO algorithm does not change, nor does it reduce the operation efficiency of the original algorithm.

## 3. ELALO-ELM Network Model

In this section, the mentioned ELALO algorithm is merged with the ELM network to develop a new ELALO-ELM network model for pattern classification.
3.1. ELM Network Fundamentals. The ELM is a new artificial neural network model for single-hidden layer feedforward neural networks (SLFNs), which randomly chooses hidden nodes and analytically determines the output weights of SLFNs [61]. In theory, ELM tends to provide good generalization performance at extremely fast learning speed.

Suppose the set of $N$ training samples is $\{X, Y\}=$ $\left\{x_{i}, y_{i}\right\}_{i=1}^{N}$, where $x_{i}=\left\{x_{i 1}, x_{i 2}, \ldots, x_{i D}\right\} \varepsilon R^{D}, y_{i}=\left\{y_{i 1}, y_{i 2}, \ldots\right.$, $\left.y_{i m}\right\}^{T} \varepsilon R^{m}, D$ is the feature dimension contained in the sample set, and $m$ is the total number of categories in the sample set. Supposing the number of hidden layer nodes is $L$ and the excitation function is $g(x)$, then the network output expression is shown as follows:

$$
\begin{aligned}
f_{L}(x)= & \sum_{i=1}^{L} \xi_{i} g\left(a_{i} \cdot x_{i}+b_{i}\right), \quad x_{i} \in R^{D}, a_{i} \in R^{D} \\
& \xi_{i} \in R^{m}, i=1,2, \ldots, L
\end{aligned}
$$

where $a_{i}=\left[a_{i 1}, a_{i 2},,, a_{i n}\right]^{T}$ represents the weight matrix from the input layer to the $i^{\text {th }}$ hidden layer node, $b_{i}$ is the threshold of the $i^{\text {th }}$ hidden layer node, and $\xi_{i}=\left[\xi_{i 1}, \xi_{i 2},,, \xi_{i m}\right]^{T}$ is the output weight of the $i^{\text {th }}$ hidden layer node.

If the network can accurately approximate $N$ samples, there is $a_{i}, b_{i}$ and $\xi_{i}$ satisfying

$$
f_{L}(x)=\sum_{i=1}^{I} \xi_{i} g\left(a_{i} \cdot x_{i}+b_{i}\right)=y_{i}, \quad i=1,2, \ldots, L
$$

Then, (21) can be simplified as follows:

$$
H \xi=Y
$$

$H$ represents the output matrix of the hidden layer of the network. In operation, the initial weight and threshold matrix are randomly assigned by the program, so that the training of the ELM model is completely transformed into the least squares solution problem in the mathematical sense. By (22), the least square solution form of the output weight matrix can be expressed as

$$
\bar{\xi}=H^{*} Y
$$

where $H^{*}$ represents the Moore-Penrose generalized inverse of matrix $H$.
3.2. ELALO-ELM Network Model. The steps to construct the ELALO-ELM model are as follows:
(1) Determine the number $k$ of ELM hidden layer nodes and the number of input layer features $d$.
(2) Set the ELALO individual dimension $D=k(d+1)$ and initialize the parameters of ELALO, and then any individual $\theta$ in the algorithm can be expressed as

$$
\theta=\left[\rho_{1}, \rho_{2}, \ldots, \rho_{k(d+1)}\right]
$$

(3) Note that the initial weight matrix of ELM is $W$ and the threshold matrix is $B_{i}$, input the individual $\theta$ into ELM, and calculate the fitness value of $\theta$ by selecting

![img-6.jpeg](img-6.jpeg)

Figure 7: Flow chart of ELALO-ELM.
the appropriate fitness function. Then, $W$ and $B_{i}$ can be expressed as

$$
\begin{aligned}
W & =\left[\begin{array}{cccc}
\rho_{1} & \rho_{2} & \cdots & \rho_{k} \\
\rho_{k+1} & \rho_{k+2} & \cdots & \rho_{2 k} \\
\vdots & \vdots & \cdots & \vdots \\
\rho_{(d-1) k+1} & \rho_{(d-1) k+2} & \cdots & \rho_{d k}
\end{array}\right] \\
B i & =\left[\rho_{d k+1} \rho_{d k+2} \cdots \rho_{k(d+1)}\right]
\end{aligned}
$$

(4) Repeat step 3 for each generation of ELALO population individuals to find the weight and threshold corresponding to the optimal fitness value.
(5) Assign the optimal weights and thresholds calculated by ELALO to ELM, complete the establishment of the ELALO-ELM model, and input the test set into the model to evaluate the performance of the model.
Based on the above steps, the realization process of the ELALO-ELM model is shown in Figure 7.

## 4. Using ELALO-ELM Network for Early Fault Diagnosis of Roller Bearings

This section uses the fault data from the drive end of the rolling bearing fault platform of Case Western Reserve University in the United States [62]. The experiment uses electric spark technology to cause damage to different parts
of the bearing in different sizes to simulate the early fault of the roller bearing. The acceleration vibration sensor is used to collect bearing signal, and sampling frequency is 12 kHz [63].

The damage degree of the rolling bearing fault is distinguished by the diameter of the fault. 8 types of rolling bearing states of different sizes are extracted, rolling ball faults, outer ring faults, and normal bearings to form a fault set, which are denoted as $\mathrm{FM}=\left\{\mathrm{fm}_{1}, \mathrm{fm}_{2}, \mathrm{fm}_{3}, \mathrm{fm}_{4}, \mathrm{fm}_{5}, \mathrm{fm}_{6}\right.$, $\mathrm{fm}_{7}, \mathrm{fm}_{8}$ ]. The $\mathrm{fm}_{1}, \mathrm{fm}_{2}, \mathrm{fm}_{3}$, and $\mathrm{fm}_{4}$, respectively, represent the faults of the rolling ball with diameters of 0.1778 mm , $0.3556 \mathrm{~mm}, 0.5334 \mathrm{~mm}$, and 0.7112 mm , and $\mathrm{fm}_{5}, \mathrm{fm}_{6}$, and $\mathrm{fm}_{7}$ represent the faults of the outer ring with diameters of $0.1778 \mathrm{~mm}, 0.3556 \mathrm{~mm}$, and 0.5334 mm , respectively. $\mathrm{fm}_{8}$ means normal bearing. Using data of different fault categories as the input samples of the ELALO-ELM model can make more accurate performance evaluation of the model. According to literature [64], the sampling points of each group of data to the original data are 2048. The time-domain waveforms of the 8 bearing states are shown in Figure 8.

### 4.1. Fault Feature Extraction Based on LMD and Sample Entropy

4.1.1. Introduction of Estimation of Distribution Algorithm. Local mean decomposition (LMD) [65] is a feature extraction method for adaptive time-frequency analysis of non-stationary signal. The vibration signals of early failures

![img-7.jpeg](img-7.jpeg)

Figure 8: Bearing waveforms on time-domain.
of rolling bearings are not easy to find obvious features, but they have the characteristics of non-linearity and non-stationarity. LMD can efficiently extract early fault characteristics of rolling bearings, and thus improve the effectiveness and correlation of candidate feature sets. The LMD generally decomposes the original signal $x(t)$ through (26) and decomposes it into several $\operatorname{PF}(t)$ components that conform to the essential law of characteristics and a residual component $\mu_{k}(t)$ with weak characteristic performance. This component can describe the signal characteristics in more details. The detailed steps of this method can be found in the literature [65], which will not be repeated here

$$
x(t)=\sum_{p=1}^{k} \mathrm{PF}_{p}(t)+\mu_{k}(t)
$$

4.1.2. Symbolic Entropy Theory. Symbol entropy [66] is a signal complexity measurement method based on information entropy, which is simple and efficient. A random sequence $\left\{a_{n}\right\}$ is provided, and the sequence is symbolized by

$$
s_{n}= \begin{cases}1 & a_{n}>\bar{m} \\ 0 & a_{n}<\bar{m}\end{cases}
$$

where $\bar{m}$ is the mean value of sequence $\left\{a_{n}\right\}$. After converting $\left\{a_{n}\right\}$ into symbol sequence $\left\{s_{n}\right\}$, which is composed of 0 and 1 , it needs to be decomposed into multiple short symbol sequences by

$$
\bar{S}(i)=s(i), s(i+1), \ldots, s(i+(L-1)) \quad i=1,2, \ldots, B-L+1
$$

$L$ represents the length of each symbol sequence after decomposition, and $B$ represents the total length of the original sequence $\left\{s_{n}\right\}$. Convert all sequences $\bar{S}(i)$ into decimal sequences and the code sequence can be obtained [67]. For example, the original symbol sequence $\left\{s_{n}\right\}$ is $\{100101001\}$, when $L=3$, it can be decomposed into a short sequence of $\{100,001,010,101,010,100,001\}$ and converted into a decimal coding sequence as $\{4,1,2,5,2,4,1\}$.

Then, the entropy of the above symbol sequences is calculated according to

$$
H_{s}(L)=\frac{1}{\log M} \sum P_{m, L} \log \left(P_{m, L}\right)
$$

where $H_{s}(L)$ represents the symbol entropy value, $P_{m, L}$ is the relative overall occupancy rate of each digital code in the decimal code sequence, and $M$ represents the number of $0 \sim 9$ digital categories in the sequence.

Figures 9(a)-9(h) show the LMD exploded view of 8 different states of the rolling bearing, respectively.

It can be seen from Figure 9 that the bearing signal is mainly concentrated in the first 3 PF component signals after LMD. Therefore, the symbol entropy of the PF component is calculated separately and used as the feature quantity of the input classifier. And 50 sets of samples are taken for each state of the bearing, and the PF symbol entropy is calculated as shown in Table 3.

It can be seen from Table 3 that the difference between the PF symbol entropy features based on LMD is obvious, and the distribution is stable and the aggregation degree is

![img-8.jpeg](img-8.jpeg)

Figure 9: Continued.

![img-9.jpeg](img-9.jpeg)

Figure 9: FF1-PF6 signal of the 8 bearing states: (a) PF1-PF6 signal of LMD on $\mathrm{fm}_{1}$. (b) PF1-PF6 signal of LMD on $\mathrm{fm}_{2}$. (c) PF1-PF6 signal of LMD on $\mathrm{fm}_{3}$. (d) PF1-PF6 signal of LMD on $\mathrm{fm}_{4}$. (e) PF1-PF6 signal of LMD on $\mathrm{fm}_{5}$. (f) PF1-PF6 signal of LMD on $\mathrm{fm}_{6}$. (g) PF1-PF6 signal of LMD on $\mathrm{fm}_{7}$. (h) PF1-PF6 signal of LMD on $\mathrm{fm}_{8}$.

Table 3: The first 3 PF symbol entropy of 8 states of bearings.

high. Using it as the input feature of the classifier can significantly reduce the learning difficulty of the classifier (Table 4).
4.2. Experimental Results. Since the content of this section mainly uses the bearing data set to evaluate the performance of the ELALO-ELM model, the performance evaluation index can be measured by the mean value of the failure recognition rate. So, the fitness function is constructed as

$$
\max f(x)=\frac{1}{\text { count }} \sum_{i=1}^{\text {count }} \text { accuracy }_{i}
$$

where the count represents the bearing state category and accuracy $i$ represents the data recognition rate percentage of the $i$ th category.

Table 4: Feature input and ideal output.
![img-10.jpeg](img-10.jpeg)

Figure 10: The average recognition rate curve.

Because the number of hidden layer nodes of ELM has a great influence on the results of the model. According to the literature [68], the number of hidden layer nodes of ELM is selected in order from 1 to 80 . And taking (26) as the evaluation index, the curve of the average recognition rate with hidden layer nodes is obtained. As shown in Figure 10, the peak value of the curve shows that the best number of hidden layer nodes is 56 .

Table 5: Actual output comparison of ELM and ELALO-ELM.

Note. The bold characters represent the classification results of the network, in which italics and underline indicate misclassification.

Table 6: Recognition rates comparison of 3 networks.

The ELM, ALO-ELM, and ELALO-ELM network models are used to conduct comparative experiments. Set population size $A=500$, Lévy flight times $g=100, T=300$. The three PF symbol entropy features are input to the classifier, so the input node is 3 . And the number of bearing status labels is 8 . So, the output node is also 8 . Since the hidden layer node is set to 56 , the method ELALO-ELM model establishment according to Section 3.3 is as follows: $D=56 *(3+1)=224$.

The actual output results of the standard ELM and ELALO-ELM networks are shown in Table 5. The actual output of the ELM network is far from the ideal value, and classification-errors occur in faults $\mathrm{fm}_{2}$ and $\mathrm{fm}_{3}$. The actual output of the ELALO-ELM network is more consistent with the ideal output, indicating that the network model of the fusion improved algorithm ELALO has excellent performance and can more accurately distinguish the different fault characteristics of rolling bearings.

The comparison results of the recognition rates of the three networks solved 20 times are shown in Table 6. The recognition rate of ELM is the lowest when the bearing status are $\mathrm{fm}_{2}$ and $\mathrm{fm}_{3}$, reaching $23.33 \%$ and $44.03 \%$, respectively. However, the overall recognition rate of new ELM models after parameter optimization is no less than $62.78 \%$, and the recognition rate of each bearing status is significantly improved. When the fault type is $\mathrm{fm}_{7}$, the recognition rate reaches $98.41 \%$, which is $7.46 \%$ higher than the original ELM network. It shows that the ALO algorithm fused in ELM parameter optimization can significantly improve the classification performance. Among them, ELALO-ELM has the
best network recognition rate, with an average recognition rate of $88.00 \%$ and has even a recognition rate of $100 \%$ for $\mathrm{fm}_{7}$, which is $16.26 \%$ and $2.09 \%$ higher than ELM and ALOELM respectively. It verifies the effectiveness and superiority of the new ELALO-ELM to improve accuracy of classification model on the bearing early fault.

The broken lines of the recognition rates obtained by using the three networks model for 20 times are shown in Figure 11. The abscissa represents the experiment number, and the ordinate is the bearing status recognition rate calculated by the 3 networks model in each experiment. The fault recognition rate obtained by using only the ELM network reached a peak of $79.65 \%$ at the experimental number 12, and the worst value of the ELM fault recognition rate based on the ALO algorithm was $80.94 \%$ at the experimental number 17 , which shows that the recognition rate of ELM has been significantly improved after the ALO parameter optimization. And most points in the broken line corresponding to ELALO-ELM network model are higher than ALO-ELM, which shows that the overall classification accuracy on bearing early fault of ELALO-ELM is better than that of ALO-ELM.

In order to reflect the advantages of the ELALO-ELM network more intuitively, in this paper, the average of the 20 experimental iteration curves of the two ALO network fusion is shown in Figure 12. It can be seen from Figure 11 that the two kinds of network iteration curves stabilized and converged before 50 generations. Finally, the average recognition rate of ALO-ELM stabilized at $85.91 \%$, and the average recognition rate of ELALO-ELM stabilized at

![img-11.jpeg](img-11.jpeg)

Figure 11: The recognition rate results of the three types of networks 20 times.
![img-12.jpeg](img-12.jpeg)

Figure 12: Comparison of two network iteration curves.
88.00\%. When the number of iteration steps is the same, the iteration curve corresponding to ELALO-ELM is always higher than that of ALO-ELM, indicating that the convergence accuracy of ELALO-ELM is always higher than that of ALO-ELM. When the two network models reach the same recognition rate in the early stage of iteration, the number of iteration steps required by ELALO-ELM is less than that of ALO-ELM, indicating that ELALO-ELM has higher convergence efficiency and faster convergence speed.

## 5. Conclusions

(1) This work proposes an improved ALO algorithm, called ELALO, integrates the EDA and the variablestep Lévy flight strategy. The test results on 4 benchmark functions and theoretical analysis show that the ELALO is the same as the original ALO in
terms of computational complexity, but is not easy to fall into the local optimum and superior to ALO algorithm in terms of solution accuracy and convergence speed.
(2) Aiming at the highly nonlinear and strong coupling characteristics of early fault data of rolling bearing, a method combining LMD and symbolic entropy is proposed to extract the most effective features as the input features of classifier model, which effectively reduces the difficulty of classifier pattern recognition.
(3) Aiming at the defect of random initialization of initial weight and threshold in the calculation process of ELM network, ELALO is used to optimize its initial parameters to form a new pattern recognition model called ELALO-ELM. The experimental results show that new model can effectively overcome the inherent defect of falling into local optimization caused by random initialization of ELM network, resulting in high accuracy of early fault classification of rolling bearing. The ELALO-ELM model can also be used for other weak fault classification problems.
(4) In our future work, we will focus on more complex and weaker fault pattern classification and recognition, which is challenging to the global convergence performance of ELALO algorithm and the classification ability of ELALO-ELM model.

## Appendix

## A

Pseudo-code of ELALO algorithm
$\{$
//ELALO args initialization
Init all args of ELALO: static GAUSS_POP, ALO_POP, EDA_POP, . .
//Interface implementation
function void __ALO_INIT(void)
do
Initialize ALO_POP
done
function EDA_POP __GAUSS_RND(ALO_POP)
do
EDA_POP = Initialize GAUSS_POP and Replace ALO_POP
done
function void __EDA_INIT(void)
do
EDA_POP = __ GAUSS_RND(ALO_POP)
done
function void __ELALO_INIT(void)
do

```
        _ALO_INIT()
        __EDA_INIT()
done
function ELITE_POP __ALO_SEARCH(ELALO_
TEMP_POP)
do
    According to ALO walk
done
function FVAL __FITNESS_VALUE(POP)
do
    Calculate the fitness of POP
done
function CANDIDATE_SET __LEVY_FLIGHT
(ELITE_POP)
do
    According to formula (11)
done
function BEST_POP __ELALO_SEARCH(void)
do
    ELALO_TEMP_POP = EDA_POP
    while ( }t<\mathrm{ max_iterations)
    do
        ELITE_POP = __ALO_SEARCH(ELALO_
        TEMP_POP)
            FVAL = __FITNESS_VALUE(ELITE_POP)
        if (FVAL get trapped in continuous 3 generation)
        do
            CANDIDATE_SET = __LEVY_
            FLIGHT(ELITE_POP);
            if (__FITNESS_VALUE(CANDIDATE_SET) is
good than __FITNESS_VALUE(ELITE_POP))
        do
            Replace CANDIDATE_SET to ELITE_POP
            Update ELITE_POP
        done
        else
        do
            Reserve ELITE_POP
        done
    done
    Update ELALO_TEMP_POP
    done
    end while
    BEST_POP = ELALO_TEMP_POP
    return BEST_POP
done
//Main function implementation
void main
```

do
$\qquad$ ELALO_INIT()
BEST_POP = _ELALO_SEARCH()
done
\}

## Data Availability

The data used to support the findings of this study are included within the article.

## Conflicts of Interest

The authors declare that there are no conflicts of interest regarding the publication of this article.

## Acknowledgments

This work was supported in part by the Anhui Province Natural Science Foundation under Grant No. 1808085ME127, the Overseas Visiting and Research Project for Outstanding Young Backbone Talents in Universities of Anhui Province under Grant No. gxgwfx2019041, the Innovation Project for Returned Overseas Students in Anhui Province under Grant No. 2020LCX013, the Key Research and Development Projects of Anhui Province under Grant No. 202004b11020006, the Scientific Research Foundation of Anhui Polytechnic University under Grant No. 2020YQQ010, the Anhui Polytechnic University Research Initiation Fund for Introducing Talents under Grant No. 2019YQQ004, the Anhui Polytechnic University Research Project under Grant no. Xjky019201905, the Industrial Collaborative Innovation Fund of Anhui Polytechnic University and Jiujiang District under Grant No. 2021cyrtb9, the Open Project of Anhui Provincial Engineering Laboratory on Information Fusion and Control of Intelligent Robot under Grant No. IFCIR2020001, the Science and Technology Planning Project of Anhui Market Supervision and Administration Bureau under Grant no. 2021MK005, and the Open Project of Key Laboratory of Industrial Equipment Quality Big Data Ministry of Industry and Information Technology under Grant No. 2021-IEQBD-05.
