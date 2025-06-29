# An Estimation of Distribution Algorithm With Resampling and Local Improvement for an Operation Optimization Problem in Steelmaking Process 

Lixin Tang ${ }^{\oplus}$, Senior Member, IEEE, Chang Liu ${ }^{\ominus}$, Jiyin Liu ${ }^{\ominus}$, and Xianpeng Wang ${ }^{\ominus}$, Member, IEEE


#### Abstract

This article studies an operation optimization problem in a steelmaking process. Shortly before the tapping of molten steel from the basic oxygen furnace (BOF), end-point control measures are applied to achieve the required final molten steel quality. While it is difficult to build an exact mathematical model for this process, the control inputs and the corresponding outputs are available by collecting production data. We build a data-driven model for the process. To optimize the control parameters, an improved estimation of distribution algorithm (EDA) is developed using a probabilistic model comprising different distributions. A resampling mechanism is incorporated into the EDA to guide the new population to a broader and more promising area when the search becomes ineffective. To further enhance the solution quality, we add a local improvement to update the current best individual through simplified gravitational search and information learning. Experiments are conducted using real data from a BOF steelmaking process. The results show that the algorithm can help to achieve the specified molten steel quality. To evaluate the proposed algorithm as a general optimization algorithm, we test it on some complex benchmark functions. The results illustrate that it outperforms other state-of-the-art algorithms across a wide range of problems.


Index Terms-Data-driven model, estimation of distribution algorithm (EDA), local improvement, resampling, steelmaking process.

Manuscript received 8 October 2019; accepted 12 December 2019. Date of publication 26 September 2023; date of current version 16 February 2024. This work was supported in part by the Major International Joint Research Project of the National Natural Science Foundation of China under Grant 71520107004, in part by the Major Program of National Natural Science Foundation of China under Grant 71790614, in part by the Fund for Innovative Research Groups of the National Natural Science Foundation of China under Grant 71621061, in part by the 111 Project under Grant B16009, in part by the National Natural Science Foundation of China under Grant 61702077, and in part by the National Natural Science Foundation of China under Grant 61573086. This article was recommended by Associate Editor Q. Wei. (Corresponding author: Lixin Tang.)

Lixin Tang is with the Key Laboratory of Data Analytics and Optimization for Smart Industry (Northeastern University), Ministry of Education, Shenyang 110819, China (e-mail: lixintang@mail.neu.edu.cn).
Chang Liu is with the Liaoning Engineering Laboratory of Data Analytics and Optimization for Smart Industry, Northeastern University, Shenyang 110819, China (e-mail: lc1987328@126.com).
Jiyin Liu is with the School of Business and Economics, Loughborough University, Leicestershire LE11 3TU, U.K. (e-mail: j.y.liu@lboro.ac.uk).
Xianpeng Wang is with the Liaoning Key Laboratory of Manufacturing System and Logistics, Northeastern University, Shenyang 110004, China (e-mail: wangxianpeng@ise.neu.edu.cn).

Color versions of one or more of the figures in this article are available online at http://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TSMC. 2019.2962880

## I. INTRODUCTION

MANY complex industrial processes are difficult to model precisely. However, most such processes can be observed, and there are often large amounts of historical data from the system operations. These data make it possible to optimize or improve the systems using data-driven models [1]-[5]. This article studies one of such processes, the steelmaking process in the basic oxygen furnace (BOF). Steelmaking is one of the most important stages in the steel industry because the chemical contents of the steel are finalized at the end of steelmaking, while all the later stages can only change the physical shape and mechanical properties. A major step of steelmaking is performed in the BOF. Shortly before the production of a charge of molten steel completes, the temperature and the carbon content are detected. End-point control measures are then applied to achieve the required final temperature and molten steel compositions. This control operation can be considered as a black-box model and the control parameters can then be optimized.

There has been previous research on modeling the operation [6]-[9]. However, most of these models have focused on predicting the end-point temperature and carbon content using information obtained just before the end-point control and the given control parameters. Tian and Mao [6] developed an ensemble extreme learning machine (ELM) based on a modified AdaBoost. RT algorithm for the end-point temperature prediction problem in a ladle furnace (LF). Xu et al. [7] utilized the spectrum distribution of the flame with support vector machine (SVM) to predict the end-point carbon content in BOF steelmaking. Liu et al. [8] predicted the end-point temperature and molten steel quality in BOF steelmaking through computer vision and general regression neural network. Shao et al. [9] used flame spectral analysis and a multiclass classification algorithm to predict the end-point carbon content in BOF steelmaking. To solve the end-point phosphorus content prediction problem, He and Zhang [10] presented a data-driven model based on principal component analysis and back propagation neural network. Some physical models [11] and data-driven control strategies [12] have been proposed for the process control and end-point control problems in the steelmaking process. Liu et al. [12] proposed an improved estimation of distribution algorithm (EDA) for

![img-0.jpeg](img-0.jpeg)

Fig. 1. Description of black-box optimization problem.
solving end-point control problems in BOF steelmaking. The temperature and carbon content are considered in a blackbox optimization model, but other quality indicators are not applied.

For industrial productions [13]-[15], the main purpose of black-box optimization is to optimize control parameters in the model. The main basics of a black-box optimization model are control variables, objectives, and constraints (such as performance constraints of production equipment, capacity constraints of production equipment, and a variety of complex function relationships among control variables). The objectives may be to minimize cost, minimize energy consumption, or maximize benefit.

In black-box optimization problems, the black-box model [16] is the basis of optimization. It is difficult to build exact mathematical models, but some approximate models [17] frequently work well enough. Some data analytics methods [18]-[20] have been used to describe the internal structure of black-box models, and some global optimization algorithms based on statistical models have been used to solve some expensive problems [21]. As shown in Fig. 1, the structure of a black-box model is based on an input-output mapping relationship. If the desired output is known, then the black-box optimization may be considered as an adaptive feedback process.

To achieve ideal outputs, many researchers have utilized evolutionary algorithms (EAs) to solve black-box optimization problems with single or multiple objectives [22]-[29]. Among the various intelligent optimization algorithms, EDAs have the advantages on the specific modeling and sampling mechanisms. The sampling mechanism generates new solutions using probabilistic models that are based on known information from previous samples. The specific mechanism reinforces the candidature of EDAs as promising black-box optimization tools [30]. Thus, EDAs have increasingly been applied and improved to solve multiobjective optimization problems by capturing the relationship between variables and objectives [31]. For the multimodal problems, clustering-based niching tactics [32] and maintenance of multiple submodels [33] are skillfully applied to EDAs to explore promising areas. In dealing with high-dimension problems, restricted Boltzmann machine with clustering strategies [34] and model complexity control [35] have been added to EDAs to reduce their computational complexity. Kabán et al. [36] and Sanyang et al. [37] conducted various studies on the performance of EDAs for high-dimension blackbox optimization problems. Based on the aforementioned work
on EDAs, there has been growing interest in the model structures and the linkages among variables.

With a single probabilistic model (such as Gaussian distribution, Cauchy distribution, or others) [38], [39], most of the existing continuous EDAs have the disadvantages of inefficient local search ability or low convergence speed. Thus, alternatives with other single probabilistic models or with multiple probabilistic models [32], [40] have been employed to solve continuous optimization problems. A few of these have been very effective in solving some multimodal problems. A few hybrid optimization algorithms have also been incorporated into EDAs [41]-[43]. However, the approaches have still not taken full advantage of the varying search area in each generation and historical population information.

In this article, we build a data-driven operation optimization model in BOF steelmaking, based on input and output data, which is considered as a black-box optimization problem. An EDA with resampling and local improvement (EDA-RL) is developed to optimize the end-point control parameters. The contributions of this article to the literature in this field are as follows.

1) For the end-point control in BOF steelmaking, the temperature and quality indicators of molten steel are both considered as output objectives, and a data-driven operation optimization model is established using leastsquares SVM (LSSVM) with a hybrid kernel function.
2) To solve the black-box optimization problem, an EDA framework with different probabilistic models is considered. Sampling from different models increases the diversity of the population, while the resampling mechanism enlarges the sampled region and helps guide the search to more promising areas. The new framework enhances the exploration ability of EDA.
3) An idea of local improvement is proposed to improve the exploitation ability of EDA. The current best individual is evolved using information from some superior individuals in the population through simplified gravitational search and information learning.
The remainder of this article is organized as follows. Section II briefly describes the BOF steelmaking process and a data-driven optimization model. Section III presents our proposed algorithm in detail. In Section IV, the proposed algorithm is applied to a practical problem and is tested as a general optimization algorithm on some complex benchmark functions. Finally, the conclusions are drawn in Section V, and future research is discussed.

## II. BOF STEELMARING PROCESS AND DATA-DRIVEN OPERATION OPTIMIZATION MODEL

Because of the high temperature with fierce physical and chemical reactions in the BOF steelmaking process, it is difficult to establish a mechanism model and to control the temperature and the composition contents of molten steel. Consequently, the steelmaking process can be considered as a black-box optimization problem. In this article, we build a data-driven optimization model for the end-point control problem in BOF steelmaking.

![img-2.jpeg](img-2.jpeg)

Fig. 2. Structure of BOF.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Divided stages in the BOF steelmaking process.

## A. End-Point Control in BOF Steelmaking

Fig. 2 illustrates the structure of BOF. BOF steelmaking converts carbon-rich molten pig iron and steel scraps to molten steel through blowing oxygen. During the process, redundant carbon is burnt and released as gas. Other impurities are oxidized into slags on the surface, which can be separated. Auxiliary materials are also added to achieve the required content. After a series of physical and chemical reactions, the smelting process reaches the end-point at which the following requirements need to be satisfied: 1) the carbon content is within the end-point control range; 2) the phosphorus content and sulfur content in molten steel do not exceed their specified upper limits; and 3) the tapping temperature is appropriate for steel refining and casting.

The process can be seen as consisting of two main stages: 1) a static stage and 2) a dynamic stage, as shown in Fig. 3. Most of the smelting time is spent in the static stage, which continues until the first sublance detection, shortly before the end-point at which the second detection is conducted. Between the two detections is the dynamic stage, within which endpoint control is applied, based on the quality state obtained in the first detection and the final quality requirements.

The end-point control of BOF is very important in the late stage of steel smelting. Because of the complexity of desulphuration and dephosphorization, the removal of sulfur and phosphorus should be completed as soon as possible before the steelmaking process. To some extent, the carbon content and
temperature are crucial to end-point control in BOF steelmaking. End-point control in the dynamic stage is conducted to adjust the carbon content and temperature by adding coolants (scrap steel, iron ore, etc.) or further blowing oxygen.

## B. Data-Driven Operation Optimization Model

The input end-point control parameters include the rate of blowing oxygen, the amounts of auxiliary raw materials, and the rate of blowing inert gas at the bottom. The main output performance indicators are the temperature, the carbon content, and the contents of other elements. However, because of the complex physical and chemical reactions that occur in the furnace at high temperature, it is difficult to build exact mechanism models expressing the relationship between the inputs and outputs. Furnace state data can be sampled using multisource sensors, with the temperature being observed using a flame analyzer, some composition contents in the molten steel being detected using throwing probe and sublance sampling, and gas quantity being detected using a gas analyzer. In practice, operators usually control the levels of input parameters to attain the desired outputs, based on experience and knowledge collected from historical data.

In this article, a data-driven model is built to accurately control the end-point quality of the molten steel in BOF steelmaking. The modeling method is based mainly on LSSVMs, proposed by Suykens and Vandewalle [44]. LSSVMs have faster computation speed compared with SVMs. Because the analytical formulas can be solved using linear equations in LSSVMs, rather than by means of quadratic optimization in SVMs. To improve the generalization ability of LSSVMs, this article proposes an LSSVM method with a hybrid kernel function (HKLSSVM). The principle is introduced below.

Given a sample set of $N$ data points $\left\{\boldsymbol{x}_{i}, y_{i}\right\}, i=1,2, \ldots, N$, where $\boldsymbol{x}_{i} \in \mathfrak{R}^{d}$ is the $i$ th input data, $d$ is the number of features, and $y_{i} \in \Re$ is the corresponding $i$ th output data, the inputoutput relationship is expressed by the following equation:

$$
f\left(\boldsymbol{x}_{i}\right)=\boldsymbol{w}^{T} \cdot \varphi\left(\boldsymbol{x}_{i}\right)+b, \quad i=1,2, \ldots, N
$$

where $\varphi\left(\boldsymbol{x}_{i}\right)$ is a feature map, with which $\boldsymbol{x}_{i}$ can be mapped into a high-dimensional feature space. $\boldsymbol{w}^{T}$ and $b$ are the regression coefficients and the bias, respectively.

According to the principle of structural risk minimization, the LSSVM problem can be written as

$$
\begin{gathered}
\min _{\boldsymbol{w}, b, \boldsymbol{e}} J(\boldsymbol{w}, \boldsymbol{e})=\frac{1}{2}\|\boldsymbol{w}\|^{2}+\frac{\gamma}{2} \sum_{i=1}^{N} e_{i}^{2} \\
\text { s.t. } y_{i}=\boldsymbol{w}^{T} \cdot \varphi\left(\boldsymbol{x}_{i}\right)+b+e_{i} \\
\gamma \geq 0
\end{gathered}
$$

where $\gamma$ is a penalty coefficient, which is set to a value in the range of $[100,1000]$, and $e_{i}$ is a slack variable. Using the Lagrangian multiplier $\alpha_{i}$, the above LSSVM problem can be expressed as

$$
\operatorname{Lag}\left(\boldsymbol{w}, b, \boldsymbol{e}, \alpha_{i}\right)=J(\boldsymbol{w}, \boldsymbol{e})-\sum_{i=1}^{N} \alpha_{i}\left[\boldsymbol{w}^{T} \varphi\left(\boldsymbol{x}_{i}\right)+b+e_{i}-y_{i}\right]
$$

By the Karush-Kuhn-Tucker condition, the following linear equations can be obtained:

$$
\left[\begin{array}{cc}
0 & \mathbf{1}^{T} \\
\mathbf{1} & \Omega+\gamma^{-1}
\end{array}\right]\left[\begin{array}{l}
b \\
\boldsymbol{\alpha}
\end{array}\right]=\left[\begin{array}{l}
0 \\
\boldsymbol{y}
\end{array}\right]
$$

where $\mathbf{1}=(1, \ldots, 1)^{T}, \boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{N}\right)^{T}, \boldsymbol{y}=$ $\left(y_{1}, \ldots, y_{N}\right)^{T}$, and $\Omega=\left\{\Omega_{i j} \mid i, j=1, \ldots, N\right\}=\varphi\left(\boldsymbol{x}_{i}\right)^{T} \varphi\left(\boldsymbol{x}_{j}\right)$ is a symmetric matrix of the kernel function. $K\left(\boldsymbol{x}_{i}, \boldsymbol{x}_{j}\right)$ is a Mercer kernel function that is defined as follows:

$$
K\left(\boldsymbol{x}_{i}, \boldsymbol{x}_{j}\right)=\varphi\left(\boldsymbol{x}_{i}\right)^{T} \cdot \varphi\left(\boldsymbol{x}_{j}\right), i, j=1,2, \ldots, N
$$

The LSSVM model can then be presented as

$$
f(\boldsymbol{x})=\sum_{i=1}^{N} \alpha_{i} K\left(\boldsymbol{x}, \boldsymbol{x}_{i}\right)+b
$$

To describe global and local performances by means of different kernel functions, a Gaussian kernel is combined with a polynomial kernel in this article to form a hybrid kernel function.

The Gaussian kernel function is defined as

$$
K_{1}\left(\boldsymbol{x}_{i}, \boldsymbol{x}_{j}\right)=\exp \left(-\frac{\left\|\boldsymbol{x}_{i}-\boldsymbol{x}_{j}\right\|^{2}}{2 \sigma^{2}}\right), i, j=1,2, \ldots, N
$$

where $\sigma$ is the width parameter of the kernel function, and the range of the parameter is set to $[1,100]$.

The polynomial kernel function is defined as

$$
K_{2}\left(\boldsymbol{x}_{i}, \boldsymbol{x}_{j}\right)=\left(\boldsymbol{x}_{i}^{T} \boldsymbol{x}_{j}+1\right)^{d_{\text {Ploy }}}, i, j=1,2, \ldots, N
$$

where $d_{\text {Ploy }}$ is the order of the polynomial kernel function and is an integer in the range of $[1,10]$. The hybrid kernel function can be expressed as

$$
K\left(\boldsymbol{x}, \boldsymbol{x}_{i}\right)=(1-\kappa) K_{1}\left(\boldsymbol{x}, \boldsymbol{x}_{i}\right)+\kappa K_{2}\left(\boldsymbol{x}, \boldsymbol{x}_{i}\right), i=1,2, \ldots, N
$$

where $\kappa$ represents a scale coefficient, and it takes a value in the range of $[0,0.005]$.

To obtain an accurate operation model, the values of the internal parameters $\left(\gamma, \sigma, d_{\text {Ploy }}\right.$, and $\left.\kappa\right)$ are determined by a simple optimization algorithm [17] based on differential evolution (DE) [45].

Using the above data-driven operation model, we build a data-driven operation optimization model. To determine the values of the control parameters that would achieve the required quality of the molten steel, the final model with weight coefficients is transformed into the following form:

$$
\begin{aligned}
\min & \hat{f}(\boldsymbol{x})=\omega_{1} \sqrt{\left(f_{1}(\boldsymbol{x})-y_{1}\right)^{2}}+\omega_{2} \sqrt{\left(f_{2}(\boldsymbol{x})-y_{2}\right)^{2}} \\
& +\left(1-\omega_{1}-\omega_{2}\right) \sum_{j=3}^{6} \sqrt{\left(f_{j}(\boldsymbol{x})-y_{j}\right)^{2}} \\
\text { s.t. } & \boldsymbol{x}_{\min } \leq \boldsymbol{x} \leq \boldsymbol{x}_{\max }
\end{aligned}
$$

where $\hat{f}(\boldsymbol{x})$ is the objective function, and $f_{1}(\boldsymbol{x}), f_{2}(\boldsymbol{x}), f_{3}(\boldsymbol{x})$, $f_{4}(\boldsymbol{x}), f_{5}(\boldsymbol{x})$, and $f_{6}(\boldsymbol{x})$ are operation models for temperature, carbon content, manganese content, silicon content, sulfur content, and phosphorus content, respectively. Given their importance to the molten steel quality, the temperature and carbon content have the greatest influences on molten steel. Thus, their weight coefficients ( $\omega_{1}$ and $\omega_{2}$ ) are also considered as input features. They are both set to vary within the range of $[0.35,0.5]$. Thus, the weight coefficient of the remaining component contents should be $1-\omega_{1}-\omega_{2}$. In (10), $y_{j}$ is the target value for the corresponding operation optimization objective, where $j=1,2, \ldots, 6$. The input control parameters $\boldsymbol{x}$ are within the range of $\left[\boldsymbol{x}_{\min }, \boldsymbol{x}_{\max }\right]$.

In actual applications, the optimized input control parameters include the rate of blowing oxygen on the surface of molten steel, the rate of blowing argon at the bottom, the rate of blowing nitrogen at the bottom, the amounts of added supplementary coolants, the height of the oxygen lance, and two weight coefficients of the optimized model. The output data are the temperature and the contents of carbon, manganese, silicon, sulfur, and phosphorus.

From the final operation optimization model, we can see that the objective function is complex: it is composed of six subfunctions and seven control parameters. Therefore, to optimize operation parameters, an effective operation optimization algorithm is necessary.

## III. IMPROVED EDA

In this section, this article focuses on an operation optimization algorithm in BOF steelmaking. We first present an EDA with a hybrid distribution model, and then elaborate on ideas of resampling (R) and local improvement (L) that are incorporated in the improved EDA framework. Finally, the overall structure of EDA-RL is presented.

## A. EDA With Hybrid Distribution Model

Estimation of distribution algorithms [46] are EAs that were originally developed to solve combinatorial optimization problems. Subsequently, EDAs [47] were extended to continuous optimization. Unlike other EAs, EDAs are a type of sampling algorithms based on probability distributions, and the individuals in the population are generated by sampling rather than crossover and mutation operations. The basic idea of an EDA is that a promising probabilistic model is constructed by extracting relevant distribution information from superior individuals in the population. The sampled individuals are then derived from the probabilistic models.

Univariate marginal distribution algorithm (UMDA) [47] based on the univariate Gaussian model was first proposed in 1998. This algorithm is based on the assumption that the variables are independent, which makes computation fast. Based on the assumption of Gaussian distribution with continuous variables, an extension of UMDA (UMDA ${ }_{C}^{G}$ ) [47] was developed for many real-world continuous optimization problems. For the Gaussian model with a small number of parameters, UMDA ${ }_{C}^{G}$ is generally considered as a typical EDA. However, with the increasing number of generations, Gaussian

distribution gradually tends toward a small variance and an unchanged mean, leading to poor diversity of the population. In this article, to enhance the exploration ability of model sampling, Cauchy distribution is applied to the EDA, providing a wider sampling space than the Gaussian model and avoiding the problem of sampled individuals falling into local optima. Thus, the hybrid distribution model (univariate Gaussian distribution combined with Cauchy distribution) is considered as the probabilistic model of the EDA.

Details of the EDA are described as follows.

1) Initialization: The overall parameters of the EDA are set in the initial stage, with $N P$ denoting the number of individuals in the population, $D$ representing the dimension of individuals, $g_{\max }$ being the maximum generation number, and $g$ being the current generation, which is initialized to 0 . According to the search range of each individual, $L_{j}$ and $U_{j}$ denote the lower boundary and the upper boundary in the $j$ th dimension, respectively, where $j=1,2, \ldots, D$. The initial population is generated by sampling a uniform distribution. At each generation $g$, the $i$ th individual can be regarded as $\boldsymbol{z}_{i}^{g}$, $i=1,2, \ldots, N P$, and its corresponding objective function value can be expressed as $\hat{f}\left(\boldsymbol{z}_{i}^{g}\right)$. The parameter $\lambda$ represents the selection rate of superior individuals, and then the number of superior individuals $H(=\lambda N P)$ is obtained.
2) Selection: Based on the above initialization, the $I$ th most superior individual with $D$-dimension in the current generation $g$ is represented as $\boldsymbol{z}_{i}^{g}=\left(z_{i, 1}^{g}, z_{i, 2}^{g}, \ldots, z_{i, D}^{g}\right)$, $l=1,2, \ldots, H$, which is selected from the superior objective function values in the current population.
3) Modeling: Two different types of distributions are used to establish the probabilistic model of the EDA. Based on univariate marginal distribution, Gaussian probability density function is constructed with superior individuals according to

$$
p\left(z_{i, j}^{g}\right)=\frac{1}{\sqrt{2 \pi\left(\delta_{j}^{g}\right)^{2}}} \exp \left(-\frac{1}{2\left(\delta_{j}^{g}\right)^{2}}\left(z_{i, j}^{g}-u_{j}^{g}\right)^{2}\right)
$$

where $l=1,2, \ldots, H, j=1, \ldots, D, u_{j}^{g}$ and $\delta_{j}^{g}$ are the $j$ th dimension mean and the $j$ th dimension variance of superior individuals, respectively. In addition, Cauchy distribution is also applied to the modeling of the EDA, Cauchy probability density function is expressed as

$$
\begin{gathered}
p\left(z_{i, j}^{g}\right)=\frac{1}{\pi} \frac{\hat{b}}{\left(\hat{b}^{2}+\left(z_{i, j}^{g}-\hat{a}\right)^{2}\right)} \\
l=1, \ldots, H, j=1, \ldots, D
\end{gathered}
$$

where $\hat{a}(=0)$ is a location parameter and $\hat{b}(=1)$ is a scale parameter.
4) Sampling: To increase the diversity of the population, sampling strategies [32], [38] are used to generate new individuals. The sampling process is described as

Algorithm 1 EDA With a Hybrid Distribution Model
Input: the overall parameters of the EDA, and set the proportions of individuals to be sampled from different distributions in the probability model.
1: Randomly generate an initial population by uniform distribution, and compute the objective function values of the individuals. The current best individual is set as the overall best one so far.
2: While the stopping criteria is not satisfied do
3: Select superior individuals from the current population;
4: Build a hybrid distribution probabilistic model based on the selected individuals;
5: Sample new individuals using the hybrid distribution model;
6: Repair the new individuals if necessary. Compute the objective function values of the sampled individuals, and update the current best individual;
7: Combine the selected individuals with the sampled individuals to form the new population;
8: Increase the generation number;

## End while

Output: the overall best individual.
follows:

$$
\eta_{p}^{g} \leftarrow \begin{cases}\boldsymbol{u}^{g}+\mathrm{Ga}_{p}^{g} \boldsymbol{\delta}^{g}, & p=1, \ldots, \text { num } \\ \boldsymbol{u}^{g}+\mathrm{Ca}_{p}^{g} \boldsymbol{\delta}^{g}, & p=\text { num, } \ldots, N P-H\end{cases}
$$

where $\eta_{p}^{g}$ denotes a sampled individual. $\mathrm{Ga}_{p}^{g}$ and $\mathrm{Ca}_{p}^{g}$ are a standard normal random number and a standard Cauchy random number, respectively. The number of individuals sampled from Gaussian distribution num( $=$ $\rho(N P-H))$ is obtained by a sampling rate $\rho$, where $0<$ $\rho<1$. For the hybrid sampling mechanism, $\boldsymbol{u}^{g}$ and $\boldsymbol{\delta}^{g}$ are the mean vector and the variance vector of superior individuals in the $g$ th generation, respectively.
5) Repairing: If the sampled individual is beyond the search range, a repairing strategy is carried out. Infeasible individuals are regenerated randomly within the search range. The objective function values of sampled individuals are then calculated, and the current best individual is updated.
6) Replacement: The offspring population consists of the sampled individuals and the previous superior individuals.
7) Stopping Condition: If the algorithm satisfies the stopping criteria (the given maximum evaluation number $S$ or the maximum generation number $g_{\max }$ ), the algorithm is terminated, and the overall best individual is acquired. Otherwise, the algorithm continues to the next generation.
The main flow of the EDA with a hybrid distribution model is outlined in Algorithm 1.

## B. Resampling Strategy

In general, the objective functions behind complex blackbox optimization problems are multimodal, and so there exist a large number of local optima. The aforementioned approach

mainly emphases on the model structure. Although the hybrid distribution model can solve multimodal problems to a certain degree, it may take a long time to reach promising areas.

In this article, with the increasing number of generations, the sampled individuals will concentrate gradually. In order to enlarge its sampling region, as well as to improve the global search ability of the population, we introduce a resampling strategy that can help guide the population sampling. The resampling strategy is executed when the following two conditions are satisfied. One condition is that the best objective function value in the current population is unchanged for certain generations. The other one is that eva $<r_{-}$eva, where eva is the current evaluation number, and $r_{-} e v a$ is given by $\theta \times S$, where $\theta$ represents a resampling rate, and $S$ is a given maximum number of evaluations. The following shows the specific steps of resampling.

1) Enlarge the Sampling Region: Based on the current superior individuals' location information, the initial resampling region can be identified as follows:

$$
\tau_{j}=\max _{1 \leq l \leq H} z_{l, j}^{g}, v_{j}=\min _{1 \leq l \leq H} z_{l, j}^{g}, j=1, \ldots, D
$$

The hyper cube $\left[v_{j}, \tau_{j}\right], j=1,2, \ldots, D$, contains all current superior individuals and represents the current sampling region. In order to avoid falling into the local optima, the sampling region needs to be enlarged. The region for resampling is determined by the following.

If $\delta_{j}^{g}>\zeta$

$$
U_{j}^{*}=\tau_{j}, L_{j}^{*}=v_{j}, j=1, \ldots, D
$$

Otherwise

$$
\begin{aligned}
U_{j}^{*} & =\tau_{j}+\operatorname{rand}(0,1)\left(U_{j}-\tau_{j}\right), j=1, \ldots, D \\
L_{j}^{*} & =v_{j}-\operatorname{rand}(0,1)\left(v_{j}-L_{j}\right), j=1, \ldots, D
\end{aligned}
$$

where $\zeta$ is a threshold value of variance, $U_{j}^{*}$ and $L_{j}^{*}$ are the upper and lower boundaries of the resampling region, respectively. rand $(0,1)$ denotes a random number from 0 to 1 .
2) Resampling: $W(=2 N P)$ individuals are generated from uniform distribution over the resampling region. The $j$ th dimension of the $o$ th resampled individual, $\hat{z}_{o, j}$, $o=1,2, \ldots, W, j=1, \ldots, D$, is obtained as follows:

$$
\hat{z}_{o, j}=L_{j}^{*}+\operatorname{rand}(0,1)\left(U_{j}^{*}-L_{j}^{*}\right)
$$

The Euclidean distance $s_{0}$ between each of the resampled individuals $\hat{z}_{o}$ and the overall best individual $z_{\text {best }}$ is calculated as

$$
s_{o}=\left\|\hat{z}_{o}-z_{\text {best }}\right\|_{2}, o=1,2, \ldots, W
$$

After that, $N P$ smallest distances are selected. The corresponding individuals are used to replace the current population and their objective function values are calculated. Superior individuals from this population are then selected, and used to recalculate $\boldsymbol{u}^{g}$ and $\boldsymbol{\delta}^{g}$.

To retain the overall best objective function value and the overall best individual, the current best individual $z_{c \text { best }}$ and the current best objective function value are stored to an external archive before each resampling. The main flow of the resampling strategy is shown in Algorithm 2.

## Algorithm 2 Resampling Strategy

Input: the initialization parameters of resampling.
1: Enlarge the sampling region:
For $j=1: D$

$$
\tau_{j}=\max _{1 \leq l \leq L} z_{l, j}^{g}, v_{j}=\min _{1 \leq l \leq L} z_{l, j}^{g}
$$

If $\delta_{j}^{g}>\zeta$

$$
U_{j}^{*}=\tau_{j}, L_{j}^{*}=v_{j}
$$

Else

$$
\begin{aligned}
U_{j}^{*} & =\tau_{j}+\operatorname{rand}(0,1)\left(U_{j}-\tau_{j}\right) \\
L_{j}^{*} & =v_{j}-\operatorname{rand}(0,1)\left(v_{j}-L_{j}\right)
\end{aligned}
$$

End if
End for
2: Resampling:
For $o=1: 2 N P$
For $j=1: D$

$$
\hat{z}_{o, j}=L_{j}^{*}+\operatorname{rand}(0,1)\left(U_{j}^{*}-L_{j}^{*}\right)
$$

End for

$$
s_{o}=\left\|\hat{z}_{o}-z_{\text {best }}\right\|_{2}
$$

## End for

3: Select $N P$ resampled individuals with the smallest $s_{o}$ to form a population. Evaluate the individuals in the population and select superior individuals from this population, and recalculate $\boldsymbol{u}^{g}$ and $\boldsymbol{\delta}^{g}$ based on this set of superior individuals.
Output: the resampled population.

Note that resampling may be performed only when eva $<r_{-}$eva. For the first generation after eva $=r_{-} e v a$ (and only for this one generation), the overall best individual in the external archive is used to replace the current best individual.

## C. Local Improvement

Because the distinctive sampling mechanism of the EDA lacks the local search ability, in order to make full use of superior information between sampled individuals, a local improvement step based on the simplified gravitational search [48] and information learning is introduced. In this step, the current best individual $z_{c \text { best }}$ is updated by simplified gravitational search, evolving with information from some superior individuals in the current population. Moreover, $z_{c \text { best }}$ learns from the current best-sampled individual, as well as the evolved best individuals. This local improvement enhances the local search ability of the algorithm. It applies only to the recorded $z_{c \text { best }}$ and so does not affect the current sampling.

1) Evolution With Superior Individuals: In the evolution, simplified gravitational search is applied to $z_{c \text { best }}$ using information from some superior individuals in the current population. First, the $n p(=\beta N P)$ individuals in the current population are selected and sequenced, here $\beta$ is a proportion

of superior individuals. These are denoted as $\boldsymbol{\vartheta}_{1}^{g}, \boldsymbol{\vartheta}_{2}^{g}, \ldots, \boldsymbol{\vartheta}_{n p}^{g}$ in ascending order of their objective function values.
Using each of the selected individuals $\boldsymbol{\vartheta}_{k}^{g}, k=$ $1,2, \ldots, n p-1$, an acceleration $\boldsymbol{a}_{k}$ is computed and applied to $z_{\text {cbest }}$. To do so, the gravitational mass $M_{k}$, Euclidean distance to another individual $R_{k, k_{1}}$ and the gravitational force $\boldsymbol{F}_{k}$ are first calculated in the following steps.

Gravitational mass is defined by

$$
M_{k}=\frac{m_{k}}{\sum_{t=1}^{n p-1} m_{t}}, k=1,2, \ldots, n p-1
$$

where

$$
m_{k}=\frac{\hat{f}\left(\boldsymbol{\vartheta}_{k}^{g}\right)-\hat{f}\left(\boldsymbol{\vartheta}_{n p}^{g}\right)}{\hat{f}\left(z_{\text {cbest }}\right)-\hat{f}\left(\boldsymbol{\vartheta}_{n p}^{g}\right)}, k=1,2, \ldots, n p-1
$$

$\boldsymbol{\vartheta}_{n p}^{g}$ is the worst individual among the selected superior individuals.

Euclidean distance is defined by

$$
R_{k, k_{1}}=\left\|\boldsymbol{\vartheta}_{k}^{g}-\boldsymbol{\vartheta}_{k_{1}}^{g}\right\|_{2}, k=1,2, \ldots, n p-1
$$

where $k_{1}$ is an integer number randomly chosen from $1, \ldots, n p-1$, and $\boldsymbol{\vartheta}_{k}^{g} \neq \boldsymbol{\vartheta}_{k_{1}}^{g}$.

Gravitational force is defined by

$$
\boldsymbol{F}_{k}=G \frac{M_{k} \times M_{k_{1}}}{R_{k, k_{1}}}\left(\boldsymbol{\vartheta}_{k}^{g}-\boldsymbol{\vartheta}_{k_{1}}^{g}\right), k=1,2, \ldots, n p-1
$$

where $G$ is a function with the initial value $G_{0}$, we define it as

$$
G=G_{0} \exp \left(-\varepsilon\left(\frac{\text { eva }}{S}\right)^{2}\right)
$$

where eva is the current number of evaluations in the algorithm, $S$ is the total number of evaluations, and $\varepsilon$ is a decreasing coefficient.

The acceleration $\boldsymbol{a}_{k}$ can then be calculated

$$
\boldsymbol{a}_{k}=\frac{\boldsymbol{F}_{k}}{M_{k}}, k=1,2, \ldots, n p-1
$$

Adding $\boldsymbol{a}_{k}$ to $z_{\text {cbest }}$, an evolved individual is obtained by

$$
\begin{aligned}
\boldsymbol{q}_{k} & =z_{\text {cbest }}+\boldsymbol{a}_{k} \\
& =z_{\text {cbest }}+G \frac{M_{k_{1}}}{R_{k, k_{1}}}\left(\boldsymbol{\vartheta}_{k}^{g}-\boldsymbol{\vartheta}_{k_{1}}^{g}\right), k=1,2, \ldots, n p-1
\end{aligned}
$$

For each $k=1,2, \ldots, n p-1$, there is an evolved individual $\boldsymbol{q}_{k}$. Let $\boldsymbol{q}_{\text {best }}$ be the best among them. If $\boldsymbol{q}_{\text {best }}$ is better than $z_{\text {cbest }}, z_{\text {cbest }}$ is updated.

As can be seen from the above description, this gravitational search is much simplified from its original version in [48]. It applies the gravitational forces individually to only $z_{\text {cbest }}$, rather than using their combination to every solution. Moreover, as the best individual in the current population, $z_{\text {cbest }}$ is assumed not to change unless being improved. Therefore, each evolved solution is obtained by changing $z_{\text {cbest }}$ with the acceleration for the current generation only, and the velocity is assumed always gets back to 0 then. This is why velocity variables are not used.

If the differences between the superior individuals are very small, the resulting acceleration would not cause any obvious evolution. Therefore, the evolutionary strategy based on superior individuals will not be executed when the variance of the samples is below a certain value.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Sketch of information learning.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Overall structure of the proposed algorithm.
2) Information Learning: Sometimes the quality of $z_{\text {cbest }}$ may be impaired because of the information in a few dimensions while the information in the corresponding dimensions of other individuals may be better. To make use of the potentially useful information of the superior individuals, we perform a learning operation for each dimension of $z_{\text {cbest }}$. If the resulting individual is better, $z_{\text {cbest }}$ is updated. As shown in Fig. 4, information of $z_{\text {cbest }}$ learns from that of the current bestsampled individual $z_{\text {cbest }}$ and $\boldsymbol{q}_{\text {best }}$. The corresponding learning operation is skipped if $z_{\text {cbest }}$ is the same to any of $z_{\text {cbest }}$ and $\boldsymbol{q}_{\text {best }}$.

The main flow of local improvement is shown in Algorithm 3. In later generations, it is expected that the search has reached the most promising region and the focus should be mainly on exploitation. Therefore, for the generations after eva $=r_{-}$eva, if $\hat{f}\left(z_{\text {cbest }}\right)>\hat{f}\left(z_{\text {best }}\right)$, then $z_{\text {best }}$ will be used as $z_{\text {cbest }}$ in the local improvement.

## D. Proposed EDA-RL

This article makes full use of the sampled information, incorporating a resampling (R) strategy and a local improvement (L) strategy into the EDA. The overall structure of the proposed algorithm (EDA-RL) is described in Fig. 5. The hybrid distribution function in modeling can help strengthen the diversity of the population. The resampling strategy enlarges the search scale of the EDA, which

## Algorithm 3 Local Improvement

Input: the initialization parameters of local improvement.
1: Evolution with superior individuals: Apply an evolutionary strategy to $\boldsymbol{z}_{\text {chest }}$ using information of randomly chosen superior individuals from the current population. Update $\boldsymbol{z}_{\text {chest }}$ if $\boldsymbol{q}_{\text {best }}$ is better than $\boldsymbol{z}_{\text {chest }}$.
2: Information learning: For each dimension of $\boldsymbol{z}_{\text {chest }}$, replace it with that of another solution if this leads to improvement. Update $\boldsymbol{z}_{\text {chest }}$ if the result is better. This learning operation may be performed for two rounds using $\boldsymbol{z}_{\text {chest }}$ and $\boldsymbol{q}_{\text {best }}$ as "another solution." If any of them is the same as $\boldsymbol{z}_{\text {chest }}$, that round is skipped.
Output: the current best individual and its function value.

TABLE I
Setting of Main Parameters for EDA-RL

enhances the exploration ability of EDA-RL. Furthermore, the local improvement based on simplified gravitational search and information learning is added to improve the exploitation search ability of EDA-RL.

## IV. EXPERIMENTS

The effectiveness of EDA-RL is verified in this section by its application to a practical end-point control problem in BOF steelmaking. To further demonstrate the generalization ability of our proposed algorithm, we compare it with other state-of-the-art black-box optimization algorithms through experiments on some complex benchmark problems.

## A. Experimental Setting

1) Experimental Platform: The experiments are conducted on a personal computer with an Intel Core i7-6700 3.40-GHz CPU, 16-GB RAM, and a 64-bit Windows 7 system. The algorithms are implemented in C++ on the Microsoft Visual Studio 2008 platform.
2) Parameter Setup: The main parameters of EDA-RL are listed in Table I. The population size is set based on the problem dimension $D$. The selection rate $\lambda$ is set to $30 \%$ so that the number of selected individuals is sufficient for modeling. In general, the resampling rate $\theta$ should be set larger for problems with a larger number of local optima. For our problem, the effects of $\theta$ and the decreasing coefficient $\varepsilon$ are analyzed in the next section. To reduce the effect of randomness on the experimental results, 30 independent runs are conducted for the practical application problem. The stopping criterion is set to $1000 \times D$ maximum function evaluations (MaxFEs).

## B. Results and Discussion

To verify the practicability of EDA-RL, we test it on an actual application problem. Based on real-world data from a Chinese steel plant, we solve the operation optimization problem in BOF steelmaking. The end-point control problem is
formulated using the data-driven operation model that is based on one month of historical data. The problem is then solved with EDA-RL. The performance is analyzed by comparing the results of different strategies.

1) Data Processing: Practical production data for one month are collected from the steelmaking process. Each charge of steel production has an end-point control problem and generates a set of operation data. A total of more than 300 data sets are collected in the month. Some of the data sets are abnormal. They are identified by means of clustering and then are removed. Some incomplete data sets are complemented using standard statistical method. After the preprocessing, 218 valid data sets are obtained and used in the experiment, 198 for building the black-box operation model and 20 for testing the operation optimization algorithm. In the optimization problem, the values of control variables vary within the following ranges. The rate of blowing oxygen in the reaction process varies from 0 to $1500 \mathrm{~m}^{3} / \mathrm{min}$, the height of the oxygen lance varies from 8 to 20 m , the rate of blowing nitrogen varies from 0 to $50 \mathrm{~m}^{3} / \mathrm{min}$, the rate of blowing argon at the bottom varies from 0 to $50 \mathrm{~m}^{3} / \mathrm{min}$, the range of supplementary coolants varies from 0 to 1 ton, and two weight coefficients of operation optimization model vary between 0.35 and 0.5 . Considering the large differences in the values of different variables, they are normalized in the operation optimization model.
2) Comparisons With Different Kernel Functions: To verify the effectiveness of operation models (such as temperature [T], carbon content [C], manganese content [Mn], silicon content [Si], sulfur content [S], and phosphorus content [P]), the data-driven operation models are tested using different kernel functions. Three performance indices, including the root mean square error (RMSE), mean absolute error (MAE), and maximum absolute error (MAXAE), are used to evaluate the performance of operation models. The results are listed in Table II. We can find that the hybrid kernel function obtains 16 best results and yields better results than the Gaussian kernel function and polynomial kernel function. It follows that the hybrid kernel function can be used to build accurate operation optimization model.
3) Parameter Analysis: The parameters selection may sometimes have a great influence on the performance of the algorithm. We analyze this by considering two key parameters: 1) the resampling rate $\theta$ and 2 ) the decreasing coefficient $\varepsilon$, as shown in Tables III and IV. When $\theta$ is set to $60 \%$, EDA-RL yields better results than others. For the local improvement, EDA-RL with $\varepsilon=10$ is better than EDA-RL with other parameter settings. Based on these results, we infer that if the resampling rate $\theta$ is too small, the individuals in the current population will concentrate fast, and the diversity will also be reduced. Conversely, if $\theta$ is too large, EDA-RL will have a powerful exploration ability but poor exploitation ability. We also infer that, to a certain extent, a smaller $\varepsilon$ yields better performance than a large $\varepsilon$. However, if the $\varepsilon$ is too small, the speed will decrease more rapidly, and the search scope will be trapped into a local optimum solution. These findings illustrate why appropriate parameter values can maintain a balance between the global search and local search of the algorithm.

TABLE II
Comparisons With Different Kernel Functions in Models


![img-5.jpeg](img-5.jpeg)

Fig. 6. Convergence curves of EDA, EDA-R, and EDA-RL for four practical problems. (a) Instance 4. (b) Instance 6. (c) Instance 10. (d) Instance 20.
4) Comparison Results: The results of 20 real-time test instances obtained after normalizing are listed in Table V. The mean error and the corresponding standard deviation are the main evaluation indices, and the best results are shown in bold font. If the results are smaller than 1.0E-08, we regard them as zero (all results in the subsequent tables are interpreted in the same way). Standard deviations are indicated using the symbol " $\pm$." Clearly, EDA-RL yields the best results for 17 of the 20 instances, outperforming the other comparison strategies tested.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Control graphs by EK and EDA-RL: (a) T and (b) C.

The average performance index values for the 20 realtime test instances are shown in Table VI, where MINAE and STD denote the minimum absolute error and standard deviation, respectively. We can see that EDA-RL yields better performance according to MAE. The results illustrate that EDA-RL can provide better solutions for various production furnaces. In addition, EDA-RL also generates ideal outputs for the temperature and contents of molten steel components and provides a reliable control scheme for operators. For the four practical instances listed in Table V, the convergence curves of EDA, EDA-R, and EDA-RL are shown in Fig. 6. The diagrams show that EDA-RL not only has a faster convergence than EDA-R and EDA but also obtains better solutions than the other strategies.
5) Practicability Comparisons: Under normal operating environment conditions, operators can adjust control parameters by combining their expert knowledge (EK) and experience with the mechanism model. However, smart industries often need reliable controls for quality and safety, and if the furnace state exhibits abnormal fluctuations, EK controls may lead to unreasonable or inaccurate operation results. The results obtained with EDA-RL and EK are presented in Table VII and in Fig. 7, where the expectation value is the given objective value. From these results, we can observe that EDA-RL obtains smaller absolute error values than EK and that the practical outputs of temperature and carbon content are also closer to the expectation values.

Table VIII shows the results of performance comparisons between EK and EDA-RL. From the comparison results, we can see that EDA-RL performs better than EK and that the calculated error results are consistent with the practical production requirements.
6) Computational Complexity Analysis of EDA-RL: Based on [35], some analysis of modeling, sampling, and improvement strategies are conducted in this article. In UMDA ${ }_{C}^{G}$, the computational complexity of modeling is $O(D A)$ in each generation, where $A=\lambda N P, 0<\lambda<1$. The sampling process requires $O(D Q)$, where $Q=N P-A$. In EDA with a hybrid distribution model, the overall computational complexity requires $O(D A)$ in the modeling. The overall computational complexity of sampling requires $O\left(D Y_{1}+D Y_{2}\right)$, where we note that $Y_{1}=\rho(N P-A), Y_{2}=(1-\rho)(N P-A)$, and $0<\rho<1$. Thus, the overall complexity of the sampling strategy has the same computational complexity as UMDA ${ }_{C}^{G}$. For the resampling strategy, the modeling requires $O(D A)$, and the resampling requires $O(D W)$, where $A=\lambda N P, 0<\lambda<1$, and $W=2 N P$.

TABLE III
Parameter Comparisons for Resampling on the Practical Problem

TABLE IV
Parameter Comparisons for Local Improvement on the Practical Problem

Thus, the computational complexity of resampling is $O(D N P)$. For the local improvement, the evolutionary search based on superior individuals requires $O(D \beta N P)$, and the information learning requires $O\left(D^{2}\right)$. Because $0<\beta<1$, the overall computational complexity of local improvement is between $O\left(D^{2}\right)$ and $O(D C)$, where we note that $0<C<N P$. We conclude from the aforementioned comparisons and corresponding analysis that the increase in computation cost is not significant. It is obvious that EDA-RL solves the operation optimization problem in BOF steelmaking efficiently.

## C. Further Test of EDA-RL as General Optimization Algorithm

To further verify the performance of EDA-RL, we carry out some numerical experiments described in this section. Some
complex functions based on black-box optimization [49] are considered as benchmark problems. To ensure the fairness of comparisons, 51 independent runs are conducted for the blackbox optimization benchmark problems, and the MaxFEs is set to $10000 \times D$.

1) Benchmark Functions: The benchmark problems belong to the class of real-parameter single objective minimum optimization problems without knowledge of the exact equations. These problems consist of several basic functions, and their landscapes may have contained multiple nonseparable local optima. Furthermore, these black-box optimization functions have different properties as a result of variable shift and variable rotation operations (such as rotated high conditioned elliptic function, shifted and rotated Ackley's function, shifted and rotated Schwefel's function, etc.) As far as we know, a successful algorithm for the solution of these problems

TABLE V
Comparison Results of Minimum Objective Function Values

TABLE VI
Performance Comparisons of EDA, EDA-R, and EDA-RL


should not be influenced by shifting the position of the optimum and slightly changing the rotation matrix.

The selected benchmark problems are based on complex composition functions described in [49], which consist of unimodal functions, simple multimodal functions, and hybrid functions. These functions can match many data-driven operation optimization models in practical application problems. Fun1-Fun8 represent the composition functions from No. 21 to No. 28, respectively, in [49]. The search ranges of all the functions are set to $[-100,100]$.
2) Parameter Analysis: To further confirm the sensitivity of EDA-RL, parameter comparisons for some representative functions on 10/30/50-dimension problems are conducted. The results are shown in Tables IX and X. The final results are consistent with those obtained previously for the practical problem. The best results are also obtained at $\theta=60 \%$ and $\varepsilon=10$. This suggests that the current parameter settings for EDA-RL are effective for solving different black-box optimization problems.
3) Strategy Comparisons: The results obtained for different strategies are listed in Tables XI-XIII, respectively, where
![img-7.jpeg](img-7.jpeg)

Fig. 8. Number of best results on comparison strategies.

EDA-RL is compared to EDA and EDA-R on 10/30/50dimension problems. To test the accuracy of each strategy, its solution for each instance is compared to the known optimal solution. Based on the calculated values of the mean error and standard deviation, the best results are shown in bold font. We can see from the results that the performance of EDA-RL is superior to that of EDA and EDA-R for most of the problems. The number of best results for each strategy is plotted in Fig. 8, which shows that EDA-RL has a prominent effect on 10/30-dimension problems.

To investigate the interaction between " $R$ " and " $L$ " in terms of the performance of EDA-RL for different problems, we conduct the analysis of different strategies. Based on the above results, we find that the R strategy is increasingly effective when the dimension increases. In dealing with low dimension problems, EDA-R exhibits no obvious effect. Although

TABLE VII
Comparison Results on the Practical Problem


TABLE VIII
Performance Comparisons Between EK and EDA-RL

![img-8.jpeg](img-8.jpeg)

Fig. 9. Number of best results between EDA-RL and state-of-the-art algorithms.

EDA converges faster than EDA-R in a few unimodal blackbox optimization problems, the latter performs better in terms of its exploration ability for multimodal problems. Moreover, with the L strategy, EDA-RL selects the superior individuals to yield the best individual in the current population, and employs operators with information learning. Thus, EDA-RL can take full advantage of population information in the later stage of the process to enhance the exploitation ability of the algorithm and can yield some better solutions than EDA and EDA-R.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Convergence curves of EDA, EDA-R, and EDA-RL on four 10-D problems: (a) Fun2, (b) Fun3, (c) Fun4, and (d) Fun6.

4) Comparisons With State-of-the-Art Algorithms: To further demonstrate the competitiveness of our proposed algorithm, we compare EDA-RL to some state-of-the-art

TABLE IX
Parameter Comparisons for Resampling on Benchmark Problems


TABLE X
Parameter Comparisons for Local Improvement on Benchmark Problems


TABLE XI
EXPERIMENTAL RESULTS OF SYRATEGY COMPARISONS ON 10-D BENCHMARK PROBLEMS

TABLE XII
EXPERIMENTAL RESULTS OF SYRATEGY COMPARISONS ON 30-D BENCHMARK PROBLEMS

algorithms, using their reported results, such as DE with an individual-dependent (IDE) [22], comprehensive learning particle swarm optimizer (CLPSO) [50], DE with an adaptive
strategy (SaDE) [51], and restart covariance matrix adaptation evolution strategy with increasing population size (IPOP-CMA-ES) [52]. These state-of-the-art algorithms have been

TABLE XIII
Experimental Results of Strategy Comparisons on 50-D Benchmark Problems

TABLE XIV
Comparison Results Between EDA-RL and State-of-the-Art Algorithms on 10-D Benchmark Problems


shown to be successful in solving black-box optimization problems, and have yielded better test results for some benchmark functions than some basic optimization algorithms, such as DE, PSO, and CMA-ES.

Fig. 9 shows the number of best results obtained with EDARL and the state-of-the-art algorithms. Statistical results concerning significant differences are shown in Tables XIV-XVI. In comparing statistically significant differences, the twosided Wilcoxon rank sum test [22] is conducted to evaluate performance differences at the 0.05 significance level. The symbol " + " indicates that the compared algorithm performs better than EDA-RL, the symbol "-" indicates that EDA-RL performs better, and the symbol " $=$ " indicates no significant difference between the performance of EDA-RL and the compared algorithm.

As is evident from the aforementioned comparison results, it is notable that for 10/30/50-dimension problems, in most functions, EDA-RL is able to find solutions of the same or better quality, because R can identify multimodal and different local optima for multiple variables effectively, and L can improve the local search ability to make convergence faster in the later
search process. This implies that EDA-RL can address larger complex functions with a large number of local optima more effectively. On the other hand, EDA-RL fails to perform the best for Fun2, Fun3, and Fun4, but it still remains competitive with other state-of-the-art algorithms. Therefore, as the results show, our proposed algorithm can effectively solve some complex black-box optimization problems and exhibit a powerful generalization ability.
5) Analysis of Performance: In order to investigate the convergence and stability of EDA-RL, we present the convergence curves for EDA, EDA-R, and EDA-RL for four 10-dimension problems in Fig. 10. The figures show that EDARL requires fewer evaluations to reach a steady state than the other strategies. As with the previous comparison results, EDA-RL obtains better objective function values than EDA and EDA-R.

## V. CONCLUSION

This article has studied a control parameter optimization problem in the steelmaking process. Based on historical data,

TABLE XV
Comparison Results Between EDA-RL and State-of-the-Art Algorithms on 30-D Benchmark Problems


TABLE XVI
Comparison Results Between EDA-RL and State-of-the-Art Algorithms on 50-D Benchmark Problems


a black-box model was built to describe the end-point control operation of the steelmaking process. This model was then used to formulate an optimization problem to set the control parameters for the required temperature and molten steel quality. To solve the problem, a new framework based on EDA with a resampling strategy and a local improvement (EDA-RL) was developed. In the EDA, we designed a hybrid distribution model to strengthen the diversity of the population. A resampling strategy was proposed to enlarge the sampling region and to guide the new population to a more promising area. This new sampling model with resampling has good exploration ability. To enhance its exploitation ability, we incorporated local improvement, based on simplified
gravitational search and information learning, to identify the current best individual. The EDA-RL was tested on practical operation data. The results illustrate that our proposed approach can optimize the control parameters of the steelmaking process to obtain the specified output accurately. To further test the performance of EDA-RL as a general optimization algorithm, an experiment was conducted on some complex black-box optimization benchmark problems. The results indicate that EDA-RL outperforms other state-of-the-art algorithms across a wide range of problems.

In process industries, there are problems that involve optimizing the dynamic processes of operations instead of the final outputs. These problems can be considered as dynamic

operation optimization problems. In further research, we will apply our proposed algorithm to solve dynamic operation optimization problems in practice.
