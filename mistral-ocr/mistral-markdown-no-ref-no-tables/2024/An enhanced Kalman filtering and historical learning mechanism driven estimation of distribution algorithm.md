# An enhanced Kalman filtering and historical learning mechanism driven estimation of distribution algorithm 

Ningning Zhu ${ }^{\mathrm{a}}$, Fuqing Zhao ${ }^{\mathrm{a}, *}$, Ling Wang ${ }^{\mathrm{b}}$, Chenxin Dong ${ }^{\mathrm{c}}$<br>${ }^{a}$ School of Computer and Communication Technology, Lanzhou University of Technology, Lanzhou 730050, China<br>${ }^{\mathrm{b}}$ Department of Automation, Tsinghua University, Beijing, 10084, China<br>${ }^{c}$ School of Mechanical and Automotive Engineering, Qingdao Hengxing University of Science and Technology, Qingdao 266100, China

## A R T I C L E I N F O

Keywords:
Estimation of distribution algorithm
Kalman filtering
Historical learning mechanism
Adaptive adjustment strategy
Elite strategy

## A B S T R A C T

As a representative evolutionary algorithm based on probabilistic models, the estimation of distribution algorithm (EDA) is widely applied in complex continuous optimization problems based on remarkable characteristics of modeling with macro-dominant information. However, the success of EDA depends on the quality of dominant solutions, modeling, sampling methods, and the efficiency of searching. An enhanced Kalman filtering and historical learning mechanism-driven EDA (KFHLEDA) is proposed to adjust the search direction and enlarge the search range of classical EDA in this paper. The enhanced Kalman filtering is designed in allusion to specific problems during the search through the prediction, observation, and the first and second revision stages. A historical archive is integrated into KFHLEDA to store the elite individuals with specific knowledge and diverse solutions from Kalman filtering. The elite strategy is embedded in the revision improvement matrix to revise modeling data, which is fed back to the probabilistic model through the historical learning mechanism with previous promising solutions to estimate the covariance matrix. The population adaptive adjustment strategy is introduced to reduce the number of invalid iterations. The effectiveness of the proposed KFHLEDA is proved through theoretical analysis. The evaluation results on benchmark functions of the CEC 2017 test suit validate that the KFHLEDA is efficient and competitive compared with fifteen classical metaheuristic algorithms and state-of-the-art EDA variants.

## 1. Introduction

Complex continuous optimization problems exist in practical industrial production and manufacturing systems with various optimal configurations aiming at minimizing objective functions [1]. However, it is extremely difficult to accurately establish mathematical models in several subsistent optimization scenarios, and the computational complexity increases exponentially with the dimension of the problem scale [2]. Moreover, branch and bound [3], linear programming [4], and traditional mathematical methods are unable to solve such problems efficiently due to non-separability, rotation invariance, non-linearity, and other characteristics of the variables, especially for the black-box optimization without analyzable objectives and gradient information $[5,6]$.

Meta-heuristic [7], a typical population-based intelligent optimization algorithm $[8,9]$, overcomes the defects of traditional mathematical methods and achieves remarkable success due to its strong versatility.

The optimization solutions for the optimization objectives are robust [10]. In 1996, H.Mühlenbein and G.Paa $\beta$ first proposed EDA as a typical meta-heuristic method based on estimation and sampling of the statistical probabilistic model [11]. In contrast to the other meta-heuristic methods, such as differential evolution (DE) $[12,13]$ and genetic algorithm (GA) $[14,15]$, that generate new solutions through crossover and mutation, the EDA combines GA and statistical learning approaches to select the high-quality individuals for modeling and estimating the distribution at the next generation to guide the population close to the potential region [16].

EDA establishes the mathematical model at the macro level of evolution, which provides a meaningful tool for complex optimization problems. Effective information is extracted and utilized in the evolutionary process based on specific structural characteristics. The relationship between variables is described through a probability model, which is valid for settling the high-dimensional, non-linear, and variable coupling optimization problems $[17,18]$. Diverse solution-generation

[^0]
[^0]:    a Corresponding author.

    E-mail addresses: 307516638@qq.com (N. Zhu), zhaofq@lut.edu.cn (F. Zhao), wangling@tsinghua.edu.cn (L. Wang), deyangxuanyi@hotmail.com (C. Dong).

approaches arise from the utilization of various probabilistic models. Common models include histogram models [19,20], Cauchy models [21], and Gaussian models [22]. Gaussian EDA (GEDA) is commonly applied in continuous optimization problems, and classified into three categories according to the complexity and variable dependency. The first category is the variable independent EDA [23], which includes the univariate marginal distribution algorithm (UMDAc) [24], and population-based incremental learning (PBIL) [25]. The second category is the bivariate correlated EDA represented by the bivariate marginal distribution algorithm (BMDA) [26,27]. The third category is the multivariate correlated EDA, which includes the estimation of multivariate normal algorithm (EMNA) [28] and the estimation of Gaussian networks algorithm (EGNA) [29].

Multivariate correlated EDA shows outstanding performance on most problems. Both EMNA and EGNA are based on single peaks [30]. The EMNA adopts maximum likelihood to estimate the mean and covariance matrix of multivariate Gaussian distribution at each generation in the process of evolution [31]. The EMNA instantly describes the distribution of high-quality solutions through the feedback of valuable information between variables and the utilization of problem characteristics. Therefore, the EMNA with immense potential for further improvement is employed in this paper. The EGNA is based on a Gaussian graph model where directed edges represent the relationship between variables. The EGNA reconstructs the Gaussian graph network according to the current population to represent the solution space and requires a long time to learn from the complex multi-peak and non-linear optimization problems [29]. The iterated density estimation algorithm (IDEA), proposed by Bosman [32], was employed to optimize problems with complex shapes. However, the relationship between variables is considered inadequate.

Despite exhibiting promising performance on a wide range of problems by capturing the characteristics of the optimization process, the EMNA still suffers from some limitations. First, the EMNA constantly estimates the distribution of the solutions for the next generation based on the high-quality solutions of the current generation. This approach results in selected solutions being located near the current mean, and population diversity is lost [33]. Therefore, designing an appropriate mechanism to learn from both historical and current information is indispensable to estimating the variance trend of new promising solutions. Furthermore, the main search direction of EMNA is perpendicular to the direction of fitness improvement, which affects its performance [34]. Several studies reveal that the search scope and direction affect the efficiency and accuracy of EMNA [35,36]. A large search scope contributes to producing plentiful promising solutions with high accuracy. The parallel direction of search and fitness improvement is conducive to search efficiency.

This paper proposes a novel approach to solve the above-mentioned problems simultaneously. Moreover, the study theoretically analyzes the improvement with the search scope and direction of EMNA by the proposed method. Kalman filtering, a digital processing technology in a communication system, is introduced. Based on the specific problem characteristics, the corresponding learning mechanisms and adjustment strategies combined with Kalman filtering are embedded in the framework of EMNA. An enhanced Kalman filtering and historical learning mechanism driven EDA (KFHLEDA) is proposed to improve search efficiency and solution accuracy while addressing the limitations of diversity loss, small search scope, and poor search direction. The effectiveness of the proposed KFHLEDA is verified through both theoretical analysis and experimental results. The main contributions are summarized as follows.

- A novel EMNA model is introduced based on an enhanced Kalman filtering mechanism designed for specific problem characteristics. The filtering process contains prediction, observation, and revision. The proposed KFHLEDA modifies the search center and improves the
search scope and direction. The revision stage is further divided into the first and second revisions to prevent population stagnation.
- The elite strategy is integrated into the revision improvement matrix to accelerate the process of evolution. The population adaptive adjustment strategy is employed to reduce the invalid search and achieve a good balance between exploration and exploitation.
- The KFHLEDA utilizes Kalman filtering to acquire enhanced information, which is fed back to the probabilistic model through the historical learning mechanism with previous promising solutions to estimate the covariance matrix, resulting in increased population diversity and further improvements in the quality of solutions.

The remainder of this paper is organized as follows. A literature review is presented in Section 2. The proposed KFHLEDA is described in Section 3. The experimental results of KFHLEDA and the comparison algorithms are presented in Section 4. The conclusions are drawn in Section 5 .

## 2. Literature review

As a classical probabilistic model for GEDA, the multivariate model considers the dependency of multiple variables [37]. Representative algorithms, such as EMNA [31], EGNA [29], IDEA [38], and Bayesian optimization algorithm (BOA) [39], have demonstrated superior optimal effects on most problems. However, there are some limitations, such as fast diversity loss, poor evolution direction, and small search scope, so the search efficiency and solution accuracy are affected [34, 35]. Several studies propose various variants to overcome the limitations and exploit potential multivariate models.

Population diversity has a significant impact on the performance of EDA. Various studies demonstrate the effectiveness of variance adaptation and scaling methods to address diversity loss. Grahl and Bosman et al. presented a correlation-triggered adaptive variance scaling mechanism and incorporated it into IDEA to enlarge or shrink the variances based on the generated solutions [40]. Later, they proposed another approach named standard deviation ratio to deal with this structure [41]. Wagner et al. designed a novel EDA through the eigenspace and reconstructed the covariance matrix for the eigenvector with the smallest eigenvalue in the eigenspace [42]. In [43], an adaptive covariance scaling estimation of distribution algorithm (ACSEDA) was developed to compute the covariance based on various high-quality solutions, and an adaptive selection strategy and a covariance scaling method were established to estimate the mean and covariance, respectively. In [44], a random walk mutation was introduced into the collaborative frame of DE and EDA to settle the non-linear equations systems to retain the population diversity.

The archive technology is introduced to store a variety of promising information in optimization algorithms to maintain population diversity. The high-quality solutions in the archive have a high probability of being close to the global optimum. The historical learning mechanism utilizes effective historical and current information to influence the subsequent evolutionary process. The historical archive was employed by Zhang et al. [45], and a new differential evolution algorithm, called JADE, was proposed to implement a new mutation strategy with an optional external archive utilizing historical data to provide information for evolution direction. In [46], a multivariate $t$ distribution, archive, and mutation-based EDA was introduced to store the promising solutions for modeling. Liang et al. [36] incorporated a historical archive into EDA to guide the population to move toward promising regions. The number of individuals was reduced while the population diversity was maintained. In [47], a neighborhood-based EDA was proposed to encourage population diversity and search efficiency by using a neighborhood sampling strategy and diverse coverage schemes. Inspired by this, the historical learning mechanism is integrated into the proposed KFHLEDA.

Various studies reveal that the search direction and scope confine the

search efficiency and solution accuracy of GEDA. The main search direction becomes orthogonal to that of the fitness improvement. The rapid decline of variance generates a sharp decrease in search scope, and premature convergence occurs in the evolutionary process [34]. In [48], a novel approach was proposed to estimate probability density by adjusting the search behavior and implementing a reflecting sampling mechanism to further enhance the search efficiency. Hansen et al. [49] presented a rank- $\mu$-update operator for the covariance with the weighted dominant solutions to increase the variance along the gradient direction and explored a surrogate fitness model in the continuous optimization problems. Bosman et al. [50] proposed an anticipated mean shift strategy to shift several solutions along a certain direction, and the main search direction was altered. A novel algorithm, named AMaLGaM-IDEA, was developed by incorporating anticipated mean shift, adaptive variance scaling, and standard deviation ratio.

Various progressive mechanisms have been introduced to EDA models to improve solution accuracy. Doerr et al. [51] introduced a long history of samples into the EDA framework and updated the probabilistic model according to the information that it classified. The time cost was reduced and the accuracy was improved. In [52], an estimation of distribution algorithm based on an approximation of the Boltzmann distribution was proposed to balance the time cost and solution accuracy. Lin et al. [53] presented a new EDA that utilized the normalized mutual information in conjunction with an updated sampling mechanism, and opposition-based learning scheme to generate high-quality solutions. In [54], a co-evolutionary algorithm based on EDA and DE was incorporated with the random forest and fitness landscape to guide the search behavior and visualize the exact distribution of solutions in complex optimization problems.

The selection of population size is an important metric for EDA and other meta-heuristic algorithms [55-57]. Appropriate population size affects the exploration and exploitation of the algorithms and conduces to saving computing sources. A large population size is beneficial to exploration, but the convergence speed is slow, and considerable computing resources are occupied. A small population size accelerates the convergence speed, but it is easy to fall into the local optimum. Various population adjustment strategies have been applied in EDA, and good results have been obtained. Auger et al. [56] introduced a covariance matrix adaptive evolution strategy (CMA-ES) by increasing the population size to restart the population and improve the search characteristic. Tanabe et al. [57] addressed an adaptive DE utilizing the success-history-based parameter adaptation with linear population size reduction which makes the population size decline linearly over time. Bujok et al. [58] presented eigen crossover based on a cooperative algorithm with CMA-ES and three DE variants, and a linear population-size reduction mechanism was employed by the cooperative model to balance exploration and exploitation.

Diverse GEDA variants have achieved promising effects in multi-

## Algorithm 1

Kalman filtering

[^0]modal optimization problems. Wang et al. [59] proposed an adaptive estimation distribution distributed differential evolution (AEDDDE) algorithm, where every individual formed its niche to reach the global optimum, and multiple parameter-free niches coevolved with master-slave mechanisms to solve the distributed multi-modal problems. Yang er al. [60] designed a maintaining and processing sub-model method integrated with GEDA to explore the potential regions and accelerate the evolution process for multimodal problems. In [61], a new EDA that incorporated a dynamic cluster sizing strategy and utilized both Gaussian and Cauchy distributions was presented to balance exploration and exploitation. Moreover, an adaptive local search was adopted to improve the solution accuracy.

The EDA demonstrates splendid performance in solving continuous optimization problems due to its exceptional self-learning ability [62]. The EDA has also been applied to a variety of practical problems. Shao et al. [63] presented a Pareto-based EDA to solve the distributed no-wait flow shop scheduling problem with sequence-dependent setup time. In [64], a knowledge-based reinforcement learning and EDA for a flexible job shop scheduling problem that involved time-of-use electricity price constraints was presented. Ceberio et al. [65] proposed a distance-based ranking model EDA with the generalized Mallows model to explore the promising regions for the flow-shop scheduling problem. Zhang et al. [66] presented a three-dimensional matrix-cube-based EDA for the distributed assembly permutation flow-shop scheduling problem to minimize the maximum completion time.

To sum up, various studies have addressed the limitations of EDA by focusing on specific aspects such as learning mechanisms, adjustment strategies, or other meta-heuristics. This paper proposes a novel EDA that utilizes Kalman filtering and historical learning mechanisms to simultaneously improve the population diversity, enlarge the search range, and adjust the search direction of traditional EMNA in continuous optimization problems.

## 3. KPHLEDA

### 3.1. Kalman filtering

Kalman filtering [67] is an algorithm that utilizes the state equation to optimally estimate the state of a system through input and output observations. All past inputs and disturbances are represented by a set of minimal parameters. The state determines the entire behavior of the system along with future inputs and disturbances. Assuming proper statistical properties of the disturbance and observation error, the estimated value of the real state is acquired by processing the observed variables.

Gaussian distribution is adopted in this paper. When both the observation data and the state obey Gaussian distribution, the mean and covariance are calculated by Kalman recursive equations according to the properties of Kalman filtering. The updating process of conditional probability density is conducted by the minimum variance estimation. State estimation is a crucial part of Kalman filtering. Generally, quantitative inference based on the observed variables is regarded as an estimation problem. Especially, the estimation of dynamic behavior contributes to predicting the current state.

Kalman filtering is particularly well-suited for continuously changing dynamic systems [68]. It is due to its ability to track the real state to provide a reasonable prediction of the next direction for the system. The predicted and observed values are calculated according to Eqs. (1) and (2), respectively.
$x(k)=A x(k-1)+B \theta(k)+w(k)$
$y(k)=H x(k-1)+v(k)$
where $x(k-1)$ and $x(k)$ represent the predicted values at the previous and current time, respectively, $\theta(k)$ is a real number as the current input,


[^0]:    ## Algorithm 1

    1 Set the initial state variable and revision improvement matrix.
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    Perform prediction:
    Obtain the predicted status $x^{\text {pre }}$ and revision improvement matrix $v$.
    Perform observation:
    Obtain the observed status $x^{\text {obs }}$.
    Perform revision:
    Calculate the gain vector $g$.
    Update the revised status $x^{\text {rev }}$.
    Update revision improvement matrix $v$.
    $n f e s=m f e s+1$
    End while

## Algorithm 2

EMNA with the historical learning mechanism

where NEW_POP represents the generated new population, $\tau$ is the selection rate, and $N P$ is the population size.
$w(k)$ represents the prediction error matrix, $y(k)$ represents the observed value at the current time, $v(k)$ represents the noise component during observation, $A$ is the state transition matrix from the previous to the current state, $B$ is the observation coefficient matrix, and $H$ is the coefficient matrix of input variables.

Kalman filtering is well-suited for linear Gaussian systems and is applied to certain dynamic systems with uncertain information, including continuous systems. It can also be employed in complex nonlinear systems in virtue of non-linear mapping techniques [69]. In this paper, the difference in the function fitness is introduced in the gain coefficient and the non-linear relationship is simulated.

Kalman filtering with the operation of prediction, observation, and revision is introduced into the EMNA. The process of Kalman filtering is shown in Algorithm 1.

### 3.2. EMNA with historical learning mechanism

The EMNA utilizes the dominant information in the solutions generated at the current generation to estimate the probabilistic models, which is crucial to the effectiveness of the algorithm. The introduction of a historical learning mechanism enables the Gaussian model to predict new solutions by utilizing historical information rather than by relying on the limited current information. The Gaussian probability density function is expressed as Eq. (3).
$G_{\langle e, C\rangle}(x)=\frac{(2 \pi)^{-d^{2}}}{(d e t C)^{1 / 2}} \exp \left(-(x-\mu)^{T}(C)^{-1}(x-\mu) / 2\right)$
where $x$ is an $n$-dimensional random vector, $\mu$ represents the mean, and $C$ is the covariance matrix.

The $\mu$ and $C$ contain $n$ and $0.5 *\left(n^{2}+n\right)$ estimated parameters, respectively, which are estimated according to the maximum likelihood estimation based on the selected solutions at the current generation, as shown in Eqs. (4)-(5).

The historical learning mechanism is further emphasized by introducing the archive technique to update the mean and covariance matrix. The information from the historical learning mechanism is employed to estimate the mean and covariance matrix to revise the modeling data, which further improves the solution accuracy.
$\mu(k)=\frac{1}{k} \sum_{i=1}^{n} x_{i}(k)$
$C(k)=\frac{1}{k} \sum_{i=1}^{k}\left(x_{i}(k)-\mu(k)\right)\left(x_{i}(k)-\mu(k)\right)^{T}$
where $x_{i}(k)$ represents the $i$ th solution in the history archive, $P O P=$ $\left\{x_{1}(k), x_{2}(k), \cdots, x_{s}(k)\right\}, P O P$ represents the population, and $s$ represents

## Algorithm 3

KPHLEDA


where $\tau$ represents the truncated selection rate of selected dominant individuals, $D$ is the dimension, $h$ represents the size of the historical archive, $P O P^{\text {rec }}, P O P^{\text {mod }}$, $P O P^{\text {obs }}$, and POP ${ }^{\text {rec }}$ represent the predicted, modeled, observed, and revised populations, $x$ represents the revision improvement matrix and $g$ is the gain coefficient of revision improvement.
the number of the selected solutions in the archive.
The historical archive is used to store the promising solutions from Kalman filtering, so the abundant hidden information is learned by the proposed algorithm. Algorithm 2 illustrates the operation of EMNA with the historical learning mechanism.

### 3.3. Population adaptive adjustment strategy

The EDA is a population-based algorithm, and the size of the population has a vital impact on its performance. A large search space avoids getting stuck in a local optimum, hence, exploration is crucial in the early evolution. The exploitation is emphasized at the later stage. A large population size is beneficial to population diversity and exploration, while a small one contributes to exploitation. The decrease in the population size accelerates the convergence speed and achieves the optimal solution appropriately. Compared to the conventional approach with a fixed population size, a population adaptive adjustment strategy makes a better trade-off between exploration and exploitation. The strategy utilizes the specific characteristics of the population at different stages to adaptively adjust the population size with the iteration process, which avoids the waste of computing resources. The adaptive adjustment strategy is shown in Eq. (6).
$N P(k+1)=\operatorname{round}\left(N P_{\max }-\frac{n f e s}{\max . n f e s}\left(N P_{\max }-N P_{\min }\right)\right)$
where $N P_{\max }$ and $N P_{\min }$ represent the maximum and the minimum numbers of the population, $N P(k+1)$ is the population size at the $(k+1)$ generation and round represents a function.

The population size is gradually decreased from the initial maximum

![img-0.jpeg](img-0.jpeg)

Fig. 1. The flow chart of KFHLEDA.
value to a minimum value by the linear reduction during the iteration process. The maximum and minimum of the population size are critical. An excessive value leads to slow convergence, which wastes computing resources, while a small one weakens exploration. With a view to the characteristics of EMNA, the covariance matrix contains $0.5 *\left(n^{2}+n\right)$ estimated parameters. $N P_{\min }$ is set as $0.5 *\left(n^{2}+n\right)$, and $N P_{\max }$ is obtained by parameter analysis in Section 4.2.

### 3.4. The proposed KFHLEDA

Kalman filtering has been employed in various communication systems. The optimization problem is abstracted as a system, and Kalman filtering is typically employed to solve the ideal state of the system. In this paper, the idea of the system is integrated with EMNA and specific problem characteristics. The Kalman filtering aims to predict the probabilistic model by promising solutions with diverse characteristics. The sampled solutions are applied to observation. Inspired by the filtering technique, the individuals are revised by prediction and observation, which in turn affects the modeling for the next generation. Transferring
it to the optimization problems is a new attempt.
The pseudocode of the proposed KFHLEDA is shown in Algorithm 3.
The probabilistic model of traditional EMNA does not utilize the previous information. The dominant solutions from the prediction, observation, and revision stages of Kalman filtering are placed into the historical archive to discover the potential regions in the search space. The enhanced information in the archive is fed back to the probabilistic model through the historical learning mechanism. Due to the positive impact of the elite strategy on solving various optimization problems [70,71], the elite strategy is integrated into the revision improvement matrix to accelerate the search speed during the whole process of Kalman filtering. The flow chart is summarized in Fig. 1, and the detailed steps are described in the following sections.

Kalman filtering and archive technology utilizes the state information of the previous generation to predict the current state. The revised solution is generated by the predicted and the observed values in the archive, which affects the solutions at the next generation by turns. Appropriate revisions lead the solutions to move to the search center with a high probability. The filtering aims to improve search efficiency

and solution accuracy by adjusting the search direction and scope.

### 3.4.1. Initialization

The concept of Kalman filtering requires the availability of prior information. In the proposed KFHLEDA, the solutions of the first generation are separately updated with the prior information.

The dominant individuals selected by the truncation selection are taken as $P O P^{\text {mod }}$, and the best individual $x_{\text {phest }}$ is found. The model is established as Eqs. (3)-(4). After modeling and sampling, $P O P^{\text {obs }}$ is obtained. NEW_POP at the first generation is constructed with $N E W . P O P_{[1]}$ $=\left(P O P^{\text {mod }}, P O P^{\text {obs }}\right)$. The revision improvement matrix at the first generation $x(1)$ is calculated according to Eq. (7) and added to the revision stage as an index of prediction accuracy.
$x(1)=\left[\begin{array}{c}x_{i}(1) \\ \vdots \\ x_{m}(1)\end{array}\right]=\left[\begin{array}{c}x_{\text {phest }}(1)-x_{i}^{\text {obs }}(1) \\ \vdots \\ x_{\text {phest }}(1)-x_{m}^{\text {obs }}(1)\end{array}\right]$
where $x_{i}^{\text {obs }}(1)=\left(x_{i}^{\text {obs }}(1), \cdots, x_{m}^{\text {obs }}(1)\right), i=1, \cdots m$ represents the selected individuals from the observed population at the first generation, $m=$ $\tau N P(k), \tau$ is obtained based on the parameter analysis in Section 4.2, and $N P(k)$ is the population size of the $k t h$ generation, which is calculated by the population adaptive adjustment strategy discussed in Section 3.3.

### 3.4.2. The prediction and observation stages

The predicted population, denoted as $P O P^{\text {pre }}(k)$, is generated by predicting the relevant information based on the previous population. The $x_{\text {phest }}$ is the best individual from the archive.

The prediction process is shown in Eq. (8).
$x_{i}^{\text {pre }}(k)=M x_{\text {phest }}(k-1)+N x_{i}(k-1)$
where $x_{i}^{\text {pre }}(k)$ is the $i$ th predicted individual of the $k t h$ generation, $x_{\text {phest }}(k-1)$ is the best individual of the $(k-1) t h$ generation, $N$ is a diagonal matrix with the diagonal elements randomly from the uniform distribution $U[0,1]$, and $x_{i}(k-1)$ is the revision improvement of the $i$ th individual at the $(k-1) t h$ generation. The revision improvement matrix $x(k)$ is calculated using Eq. (9).
$\boldsymbol{x}(k)=\left[\begin{array}{c}x_{i}(k) \\ \vdots \\ x_{m}(k)\end{array}\right]=\left[\begin{array}{c}x_{\text {phest }}(k)-x_{i}^{\text {obs }}(k) \\ \vdots \\ x_{\text {phest }}(k)-x_{m}^{\text {obs }}(k)\end{array}\right]$
In the proposed KFHLEDA, the dominant individuals from $P O P^{\text {pre }}(k)$ and $P O P^{\text {rec }}(k-1)$ are used for modeling. The model is established according to Eqs. (12)-(13) and the observed solutions for the observation phase are generated after sampling.

### 3.4.3. The revision procedure

In contrast to the conventional Kalman filtering, the proposed KFHLEDA divides the revision stage into two procedures, namely, the first revision and the second revision in allusion to the specific optimization problems.
(1) The first revision

The first revision is performed when at least one of the following two conditions is satisfied during the evolution process.

Condition 1. The covariance matrix is not positive definite.
Condition 2. The difference between the maximum and minimum fitness values is less than $10^{-4}$.

The specific revision method is described as follows. The dominant
![img-1.jpeg](img-1.jpeg)

Fig. 2. The composition of the solutions after Kalman filtering.
individuals in the archive are selected for modeling with the selection rate $\tau$, which affects the evolution of the next generation. When any condition occurs, $\tau$ changes with a fixed value, which is set to $10 \%$ according to [71]. The $\tau$ for the predicted population increases by $10 \%$ when $\tau$ for other population decreases by $10 \%$. Similarly, if no better solutions are generated for two consecutive generations, $\tau$ is adjusted in the same manner. If the new percentage exceeds $100 \%$, the algorithm subtracts $100 \%$ and retains the remaining percentage. When the percentage is less than $0,100 \%$ is added. For example, the proportion of the predicted population is $95 \%$, and the other is $5 \%$. When any condition of the first revision is satisfied, $\tau$ for the predicted population is calculated as $(95 \%+10 \%) \cdot 100 \%=5 \%$. For the other population, $\tau$ is $(5 \%-10 \%)+$ $100 \%=95 \%$.
(2) The second revision

Dominant individuals of $P O P^{\text {pre }}(k)$ and $P O P^{\text {rec }}(k-1)$ are selected from the historical archive. After the modeling and sampling are implemented, $P O P^{\text {obs }}(k)$ is acquired. NEW_POPis generated by combining $P O P^{\text {mod }}(k)$ and $P O P^{\text {obs }}(k)$. The best individual is found.

The search process of EMNA is typically non-linear. The gain coefficient and the revision improvement matrix are employed to perform the necessary non-linear transformation for Kalman filtering. The gain coefficient $g_{i}(k)$ is shown in Eq. (10).
$g_{i}(k)=\frac{\sum_{i=1}^{m} \pi_{i}(k-1)}{\sum_{i=1}^{n} \pi_{i}(k-1) \sum_{i=1}^{m}\left(f\left(x_{\text {phest }}(k-1)\right)-f\left(x_{i}^{\text {obs }}(k-1)\right)\right) \ni n}$
where $f\left(x_{\text {phest }}(k-1)\right)$, and $f\left(x_{i}^{\text {obs }}(k-1)\right)$ ) are the fitness values of the best individual and the $i$ th observed individual at the $(k-1) t h$ generation, respectively.

The $x_{i}(k-1)$ is introduced into $g_{i}(k)$. The fitness difference between the best and the observed individuals at the previous generation is taken as the weighted coefficient in the revised population, which is generated according to Eq. (11).
$x_{i}^{\text {rec }}(k)=x_{i}^{\text {rec }}(k)+g_{i}(k)\left(f\left(x_{\text {phest }}^{\text {rec }}(k)\right)-f\left(x_{i}^{\text {rec }}(k)\right)\right) x_{i}(k), i=1, \cdots, m$
where $f\left(x_{\text {phest }}^{\text {rec }}(k)\right)$ and $f\left(x_{i}^{\text {rec }}(k)\right)$ represent the best and the $i$ th individuals from the prediction population at the $k t h$ generation, respectively.

![img-2.jpeg](img-2.jpeg)

Fig. 3. The search behavior of the original EMNA.

The revision operations are executed in the direction of fitness improvement. The revised solutions are recycled for modeling at the next generation, which improves both population diversity and solution accuracy. Fig. 2 shows the composition of the solutions obtained through Kalman filtering. The red and black dots represent the optimal and the current solutions, while the blue triangles and the green squares are the predicted and the revised solutions, which are closer to the optimal solution than the ones before Kalman filtering.

The revised solutions are concentrated in the potential regions. The elite strategy guides the population to approach the direction of the optimal solution. The proposed KFHLEDA utilizes the specific knowledge embodied by the dominant and elite individuals. A faster search is achieved.

According to the definition of mean in Eq. (4), the improved mean value after revision, denoted by $\tilde{\mu}(k)$, is calculated as Eq. (12). The proposed KFHLEDA incorporates the weighted fitness of the elite individuals in the archive to modify the mean to enhance the influence of the dominant information.
$\tilde{\mu}(k)=\frac{1}{s} \sum_{i=1}^{s}\left(x_{i}(k)+g_{i}(k)\left(f\left(x_{\text {phval }}(k)-f\left(x_{i}(k)\right)\right) \pi_{i}(k)\right)\right.$
shown in Eq. (14).
$\Delta(k)=\tilde{\mu}(k)-\mu(k)$
After the operations of enhanced Kalman filtering, the new mean is adjusted to explore more potential solution spaces, which leads to a more prospective search direction and enables KFHLEDA to achieve promising solutions along the direction of fitness improvement. The revision is guided by elite solutions, which speed up the search and reduce the time consumption caused by random searches.

In Figs. 3-4, the red and black dots represent the optimal and current solutions, the green squares are the revision solutions, FID represents the direction of fitness improvement, and ED represents the evolution direction, which is the direction of the principal axis of the probability density ellipse. In the traditional EMNA, ED is perpendicular to FID and the search scope is small, as shown in Fig. 3. In the process of Kalman filtering, the prediction, observation, and revision operations guided by the elite strategy are embedded into the EMNA framework. ED becomes parallel to FID and the search scope turns extensive, as shown in Fig. 4. The adjustments made through the Kalman filtering enable KFHLEDA to modify the search direction and scope. The search efficiency and solution accuracy are improved. Section 3.5 conducts a detailed theoretical analysis to prove the above conclusions.

Moreover, a historical archive is integrated into KFHLEDA to make full use of the promising information from various types of individuals, which promotes population diversity. To address the specific search problem, the Kalman filtering revision procedure is divided into the first and the second revisions, which improves the accuracy of the algorithm.

### 3.5. Theoretical analysis

The covariance matrix determines the search scope and direction [35]. Fig. 3 indicates that the individuals generated by the traditional EMNA evolve in an unfavorable direction that is perpendicular to the direction of fitness improvement. After applying the enhanced Kalman filtering, more potential revision solutions are achieved. The revised mean and covariance matrix results in the principal axis of a probability density ellipsoid being oriented towards the direction of $\Delta(k)=\tilde{\mu}(k)-$ $\mu(k)$, which is the direction of fitness improvement.

$$
\begin{aligned}
\tilde{C}(k) & =\frac{1}{s} \sum_{i=1}^{s}\left(x_{i}(k)-\tilde{\mu}(k)\right)=\frac{1}{s} \sum_{i=1}^{s}\left(x_{i}(k)-\mu(k)-\Delta(k)\right)\left(x_{i}(k)-\mu(k)-\Delta(k)\right)^{T} \\
& =\frac{1}{s} \sum_{i=1}^{s}\left(x_{i}(k)-\mu(k)\right)\left(x_{i}(k)-\mu(k)\right)^{T}-\frac{1}{s} \sum_{i=1}^{s}\left(x_{i}(k)-\mu(k)\right)(\Delta(k))^{T} \\
& -\frac{1}{s} \sum_{i=1}^{s} \Delta(k)\left(x_{i}(k)-\mu(k)\right)^{T}+\Delta(k)(\Delta(k))^{T}=\frac{1}{s} \sum_{i=1}^{s}\left(x_{i}(k)-\mu(k)\right)\left(x_{i}(k)-\mu(k)\right)^{T} \\
& -\frac{1}{s} \sum_{i=1}^{s} x_{i}(k)(\Delta(k))^{T}+\mu(k)(\Delta(k))^{T}-\frac{1}{s} \sum_{i=1}^{s} \Delta(k)\left(x_{i}(k)\right)^{T}+\Delta(k)(\mu(k))^{T}+\Delta(k)(\Delta(k))^{T} \\
& =C(k)+\Delta(k)(\Delta(k))^{T}
\end{aligned}
$$

The mean after revision explores more potential solution spaces than that without revision. The improved covariance matrix, denoted by $\tilde{C}(k)$, is obtained as shown in Eq. (13).
$\tilde{C}(k)=\frac{1}{s} \sum_{i=1}^{s}\left(x_{i}(k)-\tilde{\mu}(k)\right)\left(x_{i}(k)-\tilde{\mu}(k)\right)^{T}$
The revision improvement of the mean, represented by $\Delta(k)$, is

Eq. (15) illustrates that the covariance matrix $\tilde{C}(k)$ improved by enhanced Kalman filtering is the rank-one correction of the original covariance matrix $C(k)$.

The analysis of the following two mathematical lemmas illustrates that the estimation method of the enhanced Kalman filtering extends the search range and adjusts the search direction adaptively.
Lemma 1. If the selected set of samples yields $\tilde{\mu}(k) \neq \mu(k)$, the

![img-3.jpeg](img-3.jpeg)

Fig. 4. The search behavior after Kalman filtering.
probability density ellipsoid bound by the covariance matrix after Kalman filtering provides coverage that is greater than or equal to that without Kalman filtering.

Proof. In the Gaussian distribution, the principal axis direction of the probability density ellipsoid corresponds to the eigenvector of the covariance matrix, and the length of the half-axis is equal to the square root of the eigenvalue [72]. As the length of the principal axis increases, the coverage of the probability density ellipsoid expands accordingly. The eigenvalues of $\tilde{C}(k)$ and $C(k)$ are defined as $\tilde{\lambda}_{i}$ and $\lambda_{i}$, respectively, where $i=1,2, \cdots, m$. According to Eq. (5), it is easy to prove that the covariance matrix is positive semi-definite. Therefore, $C(k)$ is decomposed into $C(k)=\psi(k) \Lambda(k) \psi(k)^{\mathrm{T}}$, where $\Lambda(k)$ is a diagonal matrix with the eigenvalues as the diagonal elements, and $\psi(k)$ is an orthogonal matrix. From Eq. (14), $\Delta(k)=\tilde{\mu}(k)-\mu(k)$. When $\varphi(k)=\psi(k)^{\mathrm{T}} \Delta(k)$, the following conclusion holds.

$$
\begin{aligned}
& \psi(k)^{\mathrm{T}} \tilde{C}(k) \psi(k)=\psi(k)^{\mathrm{T}}\left(C(k)+\Delta(k) \Delta(k)^{\mathrm{T}}\right) \psi(k) \\
& =\psi(k)^{\mathrm{T}} C(k) \psi(k)+\psi(k)^{\mathrm{T}} \Delta(k) \Delta(k)^{\mathrm{T}} \psi(k) \\
& =\psi(k)^{\mathrm{T}} C(k) \psi(k)+\left(\psi(k)^{\mathrm{T}} \Delta(k)\right)\left(\psi(k)^{\mathrm{T}} \Delta(k)\right)^{\mathrm{T}} \\
& \quad=\Lambda(k)+\varphi(k) \varphi(k)^{\mathrm{T}}
\end{aligned}
$$

Based on the conclusion of Lemma 1.4 in [73], the eigen polynomial of $\Lambda(k)+\varphi(k) \varphi(k)^{\mathrm{T}}$ is equal to that of $\tilde{C}(k)$.

$$
\begin{aligned}
p(\lambda) & =\prod_{i=1}^{m}\left(\lambda-\lambda_{i}\right)=\operatorname{det}\left(\lambda E-\Lambda(k)-\varphi(k) \varphi(k)^{\mathrm{T}}\right) \\
=\operatorname{det}(\lambda E & -\Lambda(k)) \operatorname{det}\left(E-(\lambda E-\Lambda(k))^{-1} \varphi(k) \varphi(k)^{\mathrm{T}}\right) \\
& =\prod_{i=1}^{m}\left(\lambda-\lambda_{i}\right)\left(1-\sum_{j=1}^{m} \frac{\varphi_{j}^{2}}{\lambda-\lambda_{j}}\right) \\
& =\prod_{i=1}^{m}\left(\lambda-\lambda_{i}\right)-\sum_{j=1}^{m}\left(\varphi_{j}^{2} \prod_{i=1, j \in i j}^{m}\left(\lambda-\lambda_{i}\right)\right)
\end{aligned}
$$

where $E$ represents an identity matrix. When $\lambda=0$, Eq. (17) is written as follows.

$$
\prod_{i=1}^{m} \tilde{\lambda}_{i}=\sum_{i=1}^{m} \lambda_{i}+\sum_{j=1}^{m}\left(\varphi_{j}^{2} \prod_{i=1, j \in i j}^{m} \lambda_{i}\right)>\prod_{i=1}^{m} \lambda_{i}
$$

Lemma 1 is proved.
According to [72], the length of the half-axis equals the square root of $\lambda_{i}$. Combined with the analysis of Lemma 1, the proposed KFHLEDA expands the coverage of the probability density ellipsoid compared to
the traditional EMNA, hence, the search scope of EMNA is expanded.
Lemma 2. For a selected set of samples, when $\tilde{\mu}(k) \neq \mu(k)$, the angle between $\Delta(k)$ and the major axis of the probability density ellipsoid revised by Kalman filtering is less than or equal to that without Kalman filtering.

Proof. The eigenvectors corresponding to the maximum eigenvalues $\tilde{\lambda}_{m}$ and $\lambda_{m}$ of $\Lambda(k)+\varphi(k) \varphi(k)^{\mathrm{T}}$ and $\Lambda(k)$ are defined as $\tilde{\chi}(k)$ and $\chi(k)$, respectively. Based on Eq. (16) in Lemma $1, \Lambda(k)+\varphi(k) \varphi(k)^{\mathrm{T}}$ and $\Lambda(k)$ are orthogonal transformations of $\tilde{C}(k)$ and $C(k)$, respectively. Thus, Lemma 2 is equivalent to certify that $\angle(\varphi(k), \tilde{\chi}(k)) \leq \angle(\varphi(k), \chi(k))$.

An acute angle is employed to represent the angle between the two vectors. Evidently, $\varphi(k)^{\mathrm{T}} \tilde{\chi}(k) \geq 0, \varphi(k)^{\mathrm{T}} \chi(k) \geq 0$.
Case 1. $\varphi(k)^{\mathrm{T}} \chi(k)=0, \angle(\varphi(k), \chi(k))=90^{\circ}, \angle(\varphi(k), \tilde{\chi}(k)) \leq 90^{\circ}, \angle(\varphi(k)$, $\tilde{\chi}(k)) \leq$

$$
\angle(\varphi(k), \chi(k)) . \text { Lemma } 2 \text { is proven. }
$$

Case 2. If $\varphi(k)^{\mathrm{T}} \chi(k) \neq 0, \tilde{\lambda}_{m}>\lambda_{m}$ is valid based on Eq. (18). According to the definition of eigenvalues, Eq. (19) is established.

$$
\left(\Lambda(k)+\varphi(k) \varphi(k)^{\mathrm{T}}\right) \tilde{\chi}(k)=\tilde{\lambda}_{m} \tilde{\chi}(k)
$$

If $\varphi(k)^{\mathrm{T}} \tilde{\chi}(k)=0$ in Eq. (19), $\Lambda(k) \tilde{\chi}(k)=\tilde{\lambda}_{m} \tilde{\chi}(k), \tilde{\lambda}_{m}$ is the eigenvalue of $\Lambda(k)$, which is a contrary conclusion. $\varphi(k)^{\mathrm{T}} \tilde{\chi}(k) \neq 0$. Eq. (19) is converted to Eq. (20).
$\tilde{\chi}(k)=\left(\tilde{\lambda}_{m} E-\Lambda(k)\right)^{-1} \varphi(k) \varphi(k)^{\mathrm{T}} \tilde{\chi}(k)$
The $\lambda$ in Eq. (17) is replaced with $\tilde{\lambda}_{m}$ as shown in Eq. (21).
$p\left(\tilde{\lambda}_{m}\right)=\left(1-\sum_{i=1}^{m} \frac{\varphi_{i}^{2}}{\tilde{\lambda}_{m}-\lambda_{i}}\right) \prod_{i=1}^{m}\left(\tilde{\lambda}_{m}-\lambda_{i}\right)=0$
Eq. (21) is transformed into Eq. (22).
$\sum_{i=1}^{m} \frac{\varphi_{i}^{2}}{\tilde{\lambda}_{m}-\lambda_{i}}=1$
Eq. (20) is obtained based on Eq. (18).
$1 \geq \frac{\varphi_{m}^{2}}{\tilde{\lambda}_{m}-\lambda_{m}}>0$
$\cos \angle(\varphi(k), \tilde{\chi}(k))=\frac{\varphi(k)^{\mathrm{T}} \tilde{\chi}(k)}{\|\varphi(k)\|\|\tilde{\chi}(k)\|}$
$=\frac{\varphi(k)^{\mathrm{T}} \tilde{\chi}(k)}{\|\varphi(k)\|\left\|\left(\tilde{\lambda}_{m} E-\Lambda(k)\right)^{-1} \varphi(k)\right\| \varphi(k)^{\mathrm{T}} \tilde{\chi}(k)}$
$=\frac{1}{\|\varphi(k)\| \sqrt{\sum_{i=1}^{m}\left(\frac{\varphi_{i}^{2}}{\left(\lambda_{m}-\lambda_{i}\right)^{2}}\right.}}$
$\geq \frac{1}{\|\varphi(k)\| \sqrt{\sum_{i=1}^{m}\left(\frac{\varphi_{i}^{2}}{\left(\lambda_{m}-\lambda_{i}\right)^{2}}\right.}} \sqrt{\frac{\varphi_{m}^{2}(k)}{\left(\lambda_{m}-\lambda_{m}\right)}}$
$=\frac{\left|\varphi_{m}(k)\right|}{\|\varphi(k)\| \sqrt{\left(\tilde{\lambda}_{m}-\lambda_{m}\right) \sum_{i=1}^{m}\left(\frac{\varphi_{i}^{2}}{\left(\lambda_{m}-\lambda_{i}\right)^{2}}\right.}}$
$\geq \frac{\left|\varphi_{m}(k)\right|}{\|\varphi(k)\| \sqrt{\left(\tilde{\lambda}_{m}-\lambda_{m}\right) \sum_{i=1}^{m}\left(\frac{\varphi_{i}^{2}}{\left(\lambda_{m}-\lambda_{m}\right)\right)\left(\lambda_{m}-\lambda_{i}\right)}}$

Table 1
MANOVA results for parameter settings of KFHLEDA.

$$
\begin{aligned}
& =\frac{\left|\varphi_{w}(k)\right|}{\|\varphi(k)\| \sqrt{\sum_{i=1}^{m} \frac{\varphi_{i}^{2}}{\left(\sigma_{w}-k_{i}\right)}}}} \\
& =\frac{\left|\varphi_{w}(k)\right|}{\|\varphi(k)\| \times 1} \\
& =\frac{\varphi(k)^{2} \chi(k)}{\|\varphi(k)\|\|\chi(k)\|} \\
& =\cos \angle(\varphi(k), \chi(k)) \\
& \angle(\varphi(k), \bar{\chi}(k)) \leq \angle(\varphi(k), \chi(k))
\end{aligned}
$$

Based on the detailed analysis presented above, the conclusion in Eq. (25) confirms that the angle between $\Delta(k)$ and the major axis of the probability density ellipsoid revised by Kalman filtering is less than or equal to that without Kalman filtering. This conclusion indicates that the direction of fitness improvement aligns with the evolutionary direction after the filtering.

## 4. Experimental results and analysis

### 4.1. Test suites

The KFHLEDA is tested in the IEEE CEC 2017 test suite to demonstrate and evaluate the effectiveness [74]. The algorithm is run on 29 benchmark test functions. The 29 functions in the test suite include two unimodal functions $f_{1}, f_{3}$, seven simple multimodal functions $f_{4}-f_{10}$, ten hybrid functions $f_{11}-f_{20}$, and ten composition functions $f_{21}-f_{30}$. It is difficult to obtain the optimal solution due to the complex structural characteristics and multiple local optima of most functions.

The performance of the proposed KFHLEDA and comparison algorithms is evaluated by the experiments on $10,30,50$, and 100 di-
mensions, denoted as 10D, 30D, 50D, and 100D, respectively. Each function is independently run 51 times. max. nfes $=10000 D$, which is taken as the experimental termination condition for each run. The function error (the difference between the best solution and the known global optimal of the function by each run) is taken as an evaluation criterion. When the error is less than $10^{-8}$, it is set to 0 . All the algorithms in this study are evaluated under the same experimental conditions and environments. The experiments are performed by MATLAB on a PC with a 3.4 GHz Intel(R) Core (TM) i7-6700 CPU, and 8 GB of RAM. The source code and material data can be downloaded at https://github. com/Znnalgorithms/KFHLEDA.git.

### 4.2. Parameters analysis

The parameter setting affects the performance of the algorithms. The proposed KFHLEDA includes three parameters, which are the initial size of the population $N P_{\max }$, the selection rate $\tau$, and the size of the historical archive $h$.

Selecting a suitable $N P_{\max }$ is crucial. A too-large value leads to slow convergence and wastes computing resources. While a too-small value reduces population diversity, exploration is weak. The $\tau$ affects the selection of the dominant solutions and directly determines the quality of solutions at each generation. If $\tau$ is small, the influence of the dominant population on subsequent iterations is weakened. It is easy to fall into the local optimum, which affects the solution accuracy. When $\tau$ is too colossal, the useless solutions are introduced except for the superior ones.

The historical archive $h$ determines the amount of historical information that is retained by the algorithm. The degree of learning the dominant solutions makes the acquisition depend on both the current and the historical information. If $h$ is oversized, the search space contains superabundant inferior information. The convergence speed is retarded. Similarly, if $h$ is undersize, the dominant information in the archive is hard to learn adequately. Therefore, selecting an appropriate value of $h$ is critical for achieving high search efficiency.

Various combinations of the three parameters result in diverse performances. The differences are analyzed through the results in the Design of the Experiments (DOE) and Multifactor Analysis of Variance (MANOVA) to achieve a promising performance [75]. The values are set as $N P_{\max }=\{1000.2000 .3000 .4000\} . \tau=\{0.15 .0 .25 .0 .35 .0 .45\}$. and $h=\{100.200 .300 .400\}$ The total number of the parameter combinations is $4 \times 4 \times 4=64$. Each combination is run on 29 functions until the termination condition is met. There are three basic assumptions in MANOVA including normality, variance homogeneity, and sample independence. The hypotheses are satisfied through the experiments. The number of samples in the experiments is large, and the
![img-4.jpeg](img-4.jpeg)

Fig. 5. Main effects plot and interaction plot of three parameters.

Table 2
The experimental results of KFHLEDA and other comparison algorithms (50D).
Table 3
The experimental results of KFHLEDA and other comparison algorithms (100D).
![img-5.jpeg](img-5.jpeg)

Fig. 6. Box plots of four typical functions (50D).
normality is guaranteed according to the central limit theorem. The individuals are randomly generated and the null hypothesis is rejected based on the Leneve test of SPSS. The validity of variance homogeneity is confirmed.

Table 1 shows that the p -value of $N P_{\max }$ is less than 0.05 , and the corresponding F-ratio is the largest. It indicates that $N P_{\max }$ has an important influence within the $95 \%$ confidence interval. The $\tau$ and $h$ are greater than 0.05 , which means there is an interaction between them. The main effects plot and interaction plot in Fig. 5 show that the best and the worst results are obtained when $N P_{\max }=3000$ and $N P_{\max }=1000$. The smaller $N P_{\max }$ is, the worse the exploration is. A large $N P_{\max }$ wastes computing resources. When $\tau=0.35$. the minimum error value is achieved. Hence, the optimal combination of the three parameters is $N P_{\max }$ $=3000 . \tau=0.35 . h=200$. The analysis above is consistent with the results shown in Fig. 5.

### 4.3. Comparison with the state-of-the-art algorithms

In this study, the KFHLEDA is compared with fifteen classical and state-of-the-art algorithms. The classical model-based evolutionary strategies include APBIL [25], CMA-ES [49], EGNA [29], and EMNA [28]. The novel DE variants include LSHADE [57], jSO [76], PID-DE [77], LSHADE-cnEpSin [78], and NL-SHADE-RSP [55]. The state-of-the-art cooperative algorithms with DE and CMA-ES are EA4eig [58], and LSHADE-SPACMA [79]. The typical EMNA variants include EDA2 [36], ACSEDA [43], EMSM [80], and AEDDDE [59]. The corresponding parameters in comparison algorithms are set to be consistent with those in the original literature and are detailed in Table S1.

Tables S2-S3 (supplementary material) and Tables 2-3 compare the overall performance of KFHLEDA and comparison algorithms through the mean, standard deviation, and computing time on 10D, 30D, 50D, and 100D for 29 functions. The numbers in bold in each line indicate that the value on the corresponding function is minimal. The smaller these values are, the better the performance is. When the mean of two algorithms is the same, the standard deviation reflects the performance.

For the unimodal functions $f_{1}$ and $f_{5}$, KFHLEDA, jSO, LSHADESPACMA, LSHADE-cnEpSin, and CMA-ES find the optimal solution on 10D, 30D, 50D, and 100D.

For the simple multimodal functions $f_{4}-f_{10}$, KFHLEDA shows the obvious advantages. When the dimension is 10D, several algorithms are slightly better than the proposed KFHLEDA on $f_{4}$. The KFHLEDA ach-
ieves promising performance on $f_{6}-f_{10}$ compared with most algorithms. Several algorithms obtain similar results, such as LSHADESPACMA, LSHADE-cnEpSin, NL-SHADE-RSP, EA4eig, EGNA, ACSEDA, and AEDDDE on $f_{7}$. The EGNA is the best on $f_{5}$, followed by the NL-SHADE-RSP, AEDDDE, and KFHLEDA. When the dimension is 30D, CMA-ES performs best on $f_{4}$. The KFHLEDA obtains excellent results on $f_{6} . f_{7}$. and $f_{9}$. The LSHADE, jSO, LSHADE-SPACMA, EDA2, and ACSEDA also reach the optimal solution on $f_{6}$ and $f_{9}$. The AEDDDE is superior to the comparison algorithms on $f_{5}$ and $f_{6}$. When the dimension is 50D, LSHADE-SPACMA, NL-SHADE-RSP, and ACSEDA outperform other algorithms on $f_{6}$, followed by LSHADE-cnEpSin, EA4eig, KFHLEDA and APBIL. The proposed KFHLEDA is better than other algorithms on $f_{7} . f_{8}$, and $f_{9}$, while the LSHADE-SPACMA, LSHADE-cnEpSin, LSHADE, EGNA, and ACSEDA also achieve performance similar to the KFHLEDA. When the dimension is 100D, NL-SHADE-RSP is the best on $f_{4}$. and $f_{6}$, LSHADE-SPACMA is the best, followed by the KFHLEDA, which is superior to other algorithms on $f_{5}$. and $f_{10}$.

For the hybrid functions $f_{11}-f_{20}$, when the dimension is 10D, KFHLEDA achieves the best results compared with other algorithms on $f_{11}$. and $f_{10}$, and is preferable on $f_{14} . f_{15}$. and $f_{18}$. Some other algorithms also obtain similar results. For example, the performance of jSO, LSHADE-SPACMA, LSHADE-cnEpSin, EA4eig, ACSEDA, and AEDDDE on $f_{11}$ is equal to that of the proposed KFHLEDA. While EA4eig achieves the optimal solution on $f_{11} . f_{14} . f_{19}$. and $f_{20}$, the NL-SHADE-RSP also performs excellently on $f_{14} . f_{19}$, and $f_{20}$. When the dimension is 30D, the jSO is superior to others on $f_{11}$. The proposed KFHLEDA obtains superior performance on $f_{13} . f_{15} . f_{16} . f_{17}$. and $f_{19}$. While the NL-SHADE-RSP performs best on $f_{18}$, the LSHADE-cnEpSin, LSHADE, jSO, EA4eig, EMSM, EDA2, ACSEDA, and AEDDDE also achieve similar advantageous results on $f_{18}$. The EDA2 is the best on $f_{14}$ and $f_{20}$ compared with other algorithms. When the dimension is 50D, the KFHLEDA is superior to others on $f_{11} . f_{13} . f_{14} . f_{16} . f_{18} . f_{19}$. and $f_{20}$. However, the ACSEDA achieves equivalent results on $f_{12}$ and $f_{19}$. The EDA2 performs best on $f_{17}$. When the dimension is 100D, the proposed KFHLEDA has more advantages over other algorithms on $f_{11} . f_{12} . f_{14} . f_{15} . f_{16} . f_{18}$ and $f_{19}$. While the AEDDDE, ACSEDA, and EDA2 also achieve better performance on $f_{18} . f_{19}$. and $f_{20}$ than other algorithms.

For the composition functions $f_{21}-f_{30}$, most algorithms obtain similar results. However, the proposed KFHLEDA exhibits splendid performance on the whole. When the dimension is 10D, the KFHLEDA shows the best performance on $f_{23} . f_{25} . f_{27}$. and $f_{28}$. The PID-DE and NL-
![img-6.jpeg](img-6.jpeg)

Fig. 7. Box plots of four typical functions (100D).

![img-7.jpeg](img-7.jpeg)

Fig. 8. Convergence curves of four typical functions (30D).
![img-8.jpeg](img-8.jpeg)

Fig. 9. Convergence curves of four typical functions (50D).
![img-9.jpeg](img-9.jpeg)

Fig. 10. Convergence curves of four typical functions (100D).
SHADE-RSP are superior to other algorithms on $f_{22}$. and $f_{27}$, respectively. The LSHADE-cnEpSin is the best on $f_{21}$. and $f_{29}$. When the dimension is 30D, the NL-SHADE-RSP achieves the optimal solution on $f_{22}$, and also shows outstanding performance on $f_{24}, f_{26}$. and $f_{29}$. In addition, KFHLEDA also performs better than the other algorithms on $f_{21}, f_{23}$. and $f_{24}$. The CMA-ES is superior to the other algorithms on $f_{29}$. When the dimension is 50D, the proposed KFHLEDA also demonstrates advantages on $f_{22}, f_{23}, f_{24}$, and $f_{29}$ compared with the other algorithms. EA4eig achieves the best results on $f_{27}$. and $f_{28}$. When the dimension is 100D, the KFHLEDA outperforms other algorithms on $f_{21}$.
$f_{22}, f_{23}, f_{24}, f_{26}$, and $f_{29}$
The computing time of the sixteen algorithms is considered. The average computing time in milliseconds on 10D, 30D, 50D, and 100D is shown in Tables S2-S3 and Tables 2-3. According to the experimental results, the computing time of KFHLEDA is shorter than most algorithms. Especially, the computing time of ENGA is overlong because of the construction of the complex probability graph model through the finite sample set in the coupling relation of continuous variable space. The results verify that the learning of EGNA is of higher cost as the problem scale becomes larger.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Rankings obtained through the Friedman test.

Table 4
The mean rank of the algorithms (100 D).
The stability of the proposed algorithm is demonstrated through box plots on all 29 functions. The experimental results are listed in Figs. S1S6 (supplementary material) and Figs. 6-7 where the horizontal axis represents all the sixteen algorithms, and the vertical axis is the standard variance of the error values between the candidate and the optimal solutions. In Figs. S3-S4 and Figs. 6-7, one function is selected to represent each of the four function types, namely $f_{1}, f_{4}, f_{15}$, and $f_{23}$. Compared with other algorithms, the standard variance of KFHLEDA is less than that of most comparison algorithms. Therefore, the proposed KFHLEDA has the best overall stability and reveals the robustness in continuous real-valued optimization problems.

The convergence curves declare the convergence degree of all sixteen algorithms in Figs. S7-S11 (supplementary material) and Figs. 8-10, where the horizontal axis is the number of function evaluations, and the vertical axis is the logarithm of the error value. The red line represents the proposed KFHLEDA with the best convergence precision on most functions. The CEC 2017 test suit specifies that a convergence curve is drawn with specified 14 points. The results reveal that some algorithms converge quickly but with lower accuracy. The reason is that these algorithms fail to find the global optimal solution due to the limitation of the algorithm performance design. From the experimental data, some algorithms have stalled prematurely in the later iteration. The overall performance of the KFHLEDA is outstanding in most cases. While the proposed algorithm performs well on most functions, it shows poor performance on some others.

### 4.4. The Friedman, Friedman Aligned rank, and Quade tests

The Friedman Test is a rank sum test between multiple samples that compares algorithms for significant differences. The test is employed to evaluate the performance of sixteen algorithms to obtain a statistical conclusion in this section. The critical difference $(C D)$ as a crucial indicator is calculated by $C D=q_{a} \sqrt{\frac{k(k-1)}{h}} \frac{1}{f u}$ where $k$ is the total number of algorithms, $f u$ is the number of functions, and $q_{a}$ is the critical value. The effects of all algorithms are indicated in Fig. S12 (supplementary material) and Fig. 11 where the horizontal axis represents all algorithms, and the vertical axis represents an average rank. The solid and dotted lines are the CDs in the $90 \%$ and $95 \%$ confidence intervals, respectively. The bar of the proposed KFHLEDA is highlighted.

The ranking results of different dimensions reveal that KFHLEDA has the best ranking. The average rank of KFHLEDA is under the critical differences. There are significant differences between KFHLEDA and most algorithms except for jSO, LSHADE-SPACMA, LSHADE-cnEpSin, NL-SHADE-RSP, EA4eig, and LSHADE on 10D, EDA2, and AEDDDE on 30D, ACSEDA and AEDDDE on 50D, LSHADE-SPACMA and LSHADEcnEpSin on 100D in $90 \%$ and $95 \%$ confidence intervals.

Friedman Aligned ranks test and Quade test are employed to further demonstrate the performance of algorithms. These two tests are methods of performing multiple comparisons. The experimental results between the proposed KFHLEDA and other comparison algorithms on 10D, 30D, 50D, and 100D are displayed in Tables S6-S8 (supplementary material) and Table 4. The results of the Friedman, Friedman Aligned, and Quade tests illustrate that the proposed KFHLEDA has a rank of 5.00, 193.24, and 5.62 on 10D, 3.22, 176.88, and 3.41 on 30D, 2.64, 176.22, 2.85 on 50D, 13.83, 305.21, 13.71 on 100D, respectively. From the experimental results, a significant difference exists between the KFHLEDA and most algorithms. The KFHLEDA is a superior algorithm.

### 4.5. Post-hoc test

The statistical results of the Friedman test show whether there are significant differences among $k$ algorithms. If differences exist, a posthoc test is performed further, which reveals statistically detailed differences between algorithms. Common post-hoc test approaches include Nemenyi, Bonferroni-Dunn, Holm, Hochberg, Hommel, Holland, and Rom tests. The test principle is to compare the difference in average ranking between algorithms with $C D$ to determine the significant difference.

The Bonferroni-Dunn, Holm, Hochberg, Hommel, Holland, and Rom methods are introduced to calculate a set of adjusted $p$-values for the experimental hypotheses. The KFHLEDA is taken as the control algorithm and compared with the remaining $k-1$ algorithms. The $p$-value is acquired from the Friedman test. When the values are less than $10^{-6}$,

Table 5
Results of post-hoc test with KFHLEDA as control algorithm (100 D).
Table 6
Results of 16 vs 16 comparisons on the benchmark (50D).

Table 6 (continued)
they are set as 0 . The test results are listed in Tables S9-S11 (supplementary material) and Table 5. The $p$-values and the adjusted $p$-values present differences between the comparison algorithms on 10D, 30D, 50D, and 100D in most situations.

The Nemenyi test compares the performance of $k$ algorithms one-toone to further statistically analyze the test results. All the comparison pairs are performed without a control algorithm. A $16 \times 16$ comparison at 10D, 30D, 50D, and 100D are displayed in Tables S4-S5 (supplementary material) and Tables 6-7, respectively. The proposed KFHLEDA is superior to most comparison algorithms, which further shows its effectiveness.

These results demonstrate that the KFHLEDA outperforms most algorithms, which verifies that the enhanced Kalman filtering mechanism, history learning mechanism, and population adaptive adjustment strategy effectively improve the performance of the proposed algorithm. Kalman filtering feeds the enhanced information back to the EDA model through the history learning mechanism. The population adaptive adjustment strategy improves the quality of solutions and effectively balances exploration and exploitation. According to the No Free Lunch Theory [81], there is no single algorithm with optimal performance on all problems.

Compared to these classical and state-of-the-art algorithms, the proposed KFHLEDA demonstrates competitive performance due to its improved design based on problem characteristics, which include the enhanced Kalman filtering operation, history learning mechanism, and population adaptive adjustment strategy. The following experiments verify this point by components availability analysis in Section 4.6.

### 4.6. Component availability analysis

The proposed KFHLEDA covers three important strategies: the Kalman filtering, the history learning mechanism, and the population adaptive adjustment strategy. This section evaluates the effectiveness of the three strategies.

Three variants of the KFHLEDA are adopted and tested against it on the CEC 2017 test suit to demonstrate the effectiveness of each strategy. The three variants are denoted as KFHLEDA1, KFHLEDA2, and KFHLEDA3, each representing KFHLEDA without the enhanced Kalman filtering, KFHLEDA without the history learning mechanism, and KFHLEDA without the population adaptive adjustment strategy, respectively. The three variants are detailed below.
(1) KFHLEDA1: It excludes the application of enhanced Kalman filtering while preserving other operations of the KFHLEDA. Comparison with this variant demonstrates the effect of the enhanced Kalman filtering. The mean and variance of the probabilistic model are updated according to Eqs. (4)-(5), instead of Eqs. (12)-(13) based on the filtering operation, that is, the mean and variance are guided by the dominant information in the historical archive.
(2) KFHLEDA2: This variant omits the history learning mechanism while retaining the other operations of the proposed KFHLEDA. It implies that the modification of the individuals by the enhanced Kalman filtering operation is based on the information obtained in the last operation rather than on the historical archive.
(3) KFHLEDA3: This variant removes the population adaptive adjustment strategy while retaining the other operations of the KFHLEDA. Therefore, the population size is no longer updated
adaptively with each iteration but instead, set to a fixed value of 3000 .

Table 8 shows that the overall performance of the proposed KFHLEDA is optimal compared with the three variants. The KFHLEDA1 obtains worse results than KFHLEDA2 and KFHLEDA3, all of which are worse than the KFHLEDA. Among the three variants, the KFHLEDA1 performs the worst due to the absence of the Kalman filtering mechanism, while the KFHLEDA3 achieves the best results by utilizing Kalman filtering and the historical learning mechanism. These experimental results show the effectiveness and significance of the selected strategies for KFHLEDA. The mean values in Table 8 are visualized in Fig. 12.

The population adaptive adjustment strategy contributes to exploration of the proposed KFHLEDA in the early stage to avoid premature convergence, and exploitation in the late stage to avoid ineffective searches and accelerate the evolution process. The historical learning mechanism helps the population explore the hidden information in the archive during the evolutionary process, and make it evolve towards the potential region. In the stages of the prediction, observation, and two revision operations during the enhanced Kalman filtering, the elite strategy is employed to guide the population to jump out of the local optimum.

### 4.7. Analysis of the fitness landscape

The fitness landscape reproduces the evolution of the population in the search space and intuitively responds to the specific phenomena with the progress of iteration [82]. The fitness landscape is highly effective in analyzing the optimization effect of the algorithms on the functions in the test suit, especially for the complex, diverse, multi-modal, funnel-shaped features. The distribution of solutions is visualized. In view of the hybrid functions without a two-dimensional definition, the fitness landscape of seventeen functions is listed in Figs. 13-15 and Figs. S13-S15 (Supplementary materials), where the red dots represent the individuals involved in the evolution. In the unimodal functions $f_{1}$ and $f_{3}$, the optimal position is found at express speed. $f_{4}-$ $f_{10}$ are the multimodal functions with the rugged landscape and many local optimal solutions. The global optimal position is difficult to be discovered, particularly for composition functions $f_{21}-f_{28}$ with varying basin shapes, making them difficult to optimize.

Fig. 13 shows that the proposed KFHLEDA evolves rapidly on $f_{3}$, and finds the optimal solution, attributed to the rich population diversity and outstanding local search ability. While the CMA-ES performs poorly on asymmetrical function $f_{9}$ with a huge number of local optima, the proposed KFHLEDA finds the optimal solution quickly as shown in Fig. 14. For the composition functions, such as $f_{21}, f_{24}$, and $f_{26}$ with many peaks and valleys in Fig. 15, the proposed KFHLEDA performs well due to its splendid exploration and exploitation.

## 5. Conclusion and future work

In this paper, a novel EDA named KFHLEDA that incorporates an enhanced Kalman filtering and historical learning mechanism and population adaptive adjustment strategy is proposed to solve continuous optimization problems. The proposed KFHLEDA enhances the conventional Kalman filtering operation. The prediction, observation, first revision, and second revision operations for the enhanced Kalman filtering are embedded into the EDA framework to address problem-

Table 7
Results of 16 vs 16 comparisons on the benchmark (100D).
(continued on next page)

Table 7 (continued)

Table 8
Comparison of results on 29 functions.
![img-11.jpeg](img-11.jpeg)

Fig. 12. The comparison results of KFHLEDA and the three variants on 29 functions.

![img-12.jpeg](img-12.jpeg)

Fig. 13. The fitness landscape of KFHLEDA on unimodal functions.
![img-13.jpeg](img-13.jpeg)

Fig. 15. The fitness landscape of KFHLEDA on composition functions.

specific characteristics during the optimization process. The filtering mechanism is based on the elite strategy, which modifies the system gain to strengthen the filtering effect. The theoretical analysis and experiments demonstrate that the modified probabilistic model with enhanced Kalman filtering takes the revised mean as a new search center, and improves the direction of population evolution and the quality of solutions. These operations effectively improve the search efficiency of the algorithm.

The historical archive in the KFHLEDA incorporates the dominant information from the iterative process to guide population evolution, rather than solely relying on the current information. The premature convergence is avoided. Learning the information from dominant individuals modifies the mean and covariance matrix, and reduces the invalid evolutionary iterations. Moreover, the population adaptive adjustment strategy adjusts the population size to further balance exploration and exploitation during the evolution and ameliorates the overall efficiency of the KFHLEDA. The non-parametric tests show significant differences between the proposed KFHLEDA and most comparison algorithms. Furthermore, the fitness landscape completely reemerges the evolution process and the distribution of the entire population, which has guiding significance for the design of the algorithm in this study. The search behavior is visualized to show the effectiveness of the designed algorithm. The experimental results show that the KFHLEDA has superior robustness and stability on 29 functions in the CEC 2017 test suit with 10D, 30D, 50D, and 100D.

As the proposed algorithm achieves the desired results, future work will involve integrating the proposed KFHLEDA with other evolutionary algorithms and learning mechanisms for solving the constrained multiobjective continuous optimization problems. Moreover, the KFHLEDA will also be applied to solve practical problems in conjunction with hyper-heuristic algorithms, such as distributed no-wait flow shop scheduling problems with energy consumption constraints.

## Credit authorship contribution statement

Ningning Zhu: Investigation, Software, Original draft, Experiments of the algorithms. Fuqing Zhan: Funding acquisition, Investigation, Supervision. Ling Wang: Methodology, Resources, Conceptualization. Chenxin Dong: Formal analysis, Review \& editing, Visualization.

## CRediT authorship contribution statement

Ningning Zhu: Writing - original draft, Software, Investigation, Data curation. Fuqing Zhao: Supervision, Investigation, Funding acquisition. Ling Wang: Resources, Methodology, Conceptualization. Chenxin Dong: Writing - review \& editing, Visualization, Formal analysis.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

I have shared the link to my code at my manuscript.

## Acknowledgments

This work was financially supported by the Excellent Postgraduate Innovation Star Project of Gansu Provincial Education Department (2023CXXX-476). It was also supported by the National Natural Science Foundation of China under grant 62063021, the Key Program of National Natural Science Foundation of Gansu Province under Grant

23JRRA784, the High-level Foreign Experts Project of Gansu Province under grant 22JR10KA007, the Key Research Programs of Science and Technology Commission Foundation of Gansu Province (21YF5WA086), and Lanzhou Science Bureau project (2018-rc-98), respectively.

## Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.swevo.2024.101502.
