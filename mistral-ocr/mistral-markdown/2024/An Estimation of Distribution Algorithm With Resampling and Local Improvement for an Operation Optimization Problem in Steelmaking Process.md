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

| Parameter | $N P$ | $\lambda$ | $\rho$ | $\zeta$ | $\beta$ | $\theta$ | $\varepsilon$ | $G_{0}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Value | 100 | $30 \%$ | $90 \%$ | 10 | $20 \%$ | $60 \%$ | 10 | 100 |

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

| Model | Index | Different Kernel Functions |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  |  | Polynomial kernel | Gaussian kernel | Hybrid kernel |
| T | RMSE | $6.20 \mathrm{E}+00$ | $3.52 \mathrm{E}+00$ | 3.44E+00 |
|  | MAE $\left({ }^{\circ} \mathrm{C}\right)$ | $4.77 \mathrm{E}+00$ | $2.83 \mathrm{E}+00$ | 2.80E+00 |
|  | MAXAE $\left({ }^{\circ} \mathrm{C}\right)$ | $1.71 \mathrm{E}+01$ | $7.78 \mathrm{E}+00$ | 7.56E+00 |
| C | RMSE | $9.35 \mathrm{E}-03$ | $5.42 \mathrm{E}-03$ | 5.41E-03 |
|  | MAE (\%) | $6.63 \mathrm{E}-03$ | 4.34E-03 | 4.34E-03 |
|  | MAXAE (\%) | $2.36 \mathrm{E}-02$ | 1.52E-02 | 1.52E-02 |
| Mn | RMSE | $4.72 \mathrm{E}-02$ | 3.12E-02 | $3.14 \mathrm{E}-02$ |
|  | MAE (\%) | $3.92 \mathrm{E}-02$ | 2.56E-02 | $2.58 \mathrm{E}-02$ |
|  | MAXAE (\%) | $1.02 \mathrm{E}-01$ | $7.62 \mathrm{E}-02$ | 7.60E-02 |
| Si | RMSE | $4.00 \mathrm{E}-04$ | $3.75 \mathrm{E}-04$ | 3.72E-04 |
|  | MAE (\%) | $1.65 \mathrm{E}-04$ | $1.16 \mathrm{E}-04$ | 1.12E-04 |
|  | MAXAE (\%) | $2.06 \mathrm{E}-03$ | 2.05E-03 | 2.05E-03 |
| S | RMSE | $1.31 \mathrm{E}-02$ | 1.23E-02 | 1.23E-02 |
|  | MAE (\%) | $8.30 \mathrm{E}-03$ | 6.60E-03 | 6.60E-03 |
|  | MAXAE (\%) | $4.62 \mathrm{E}-02$ | 4.07E-02 | 4.07E-02 |
| P | RMSE | $2.61 \mathrm{E}-03$ | $1.90 \mathrm{E}-03$ | 1.85E-03 |
|  | MAE (\%) | $1.99 \mathrm{E}-03$ | $1.35 \mathrm{E}-03$ | 1.29E-03 |
|  | MAXAE (\%) | $6.54 \mathrm{E}-03$ | $5.85 \mathrm{E}-03$ | 5.77E-03 |
| No. of Best |  | 0 | 8 | 16 |

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

| Instance | $\theta=20 \%$ <br> Mean/Std. | $\theta=40 \%$ <br> Mean/Std. | $\theta=60 \%$ <br> Mean/Std. | $\theta=80 \%$ <br> Mean/Std. |
| :--: | :--: | :--: | :--: | :--: |
| 1 | $1.46 \mathrm{E}-01 \pm 4.61 \mathrm{E}-03$ | $1.45 \mathrm{E}-01 \pm 3.44 \mathrm{E}-03$ | $1.44 \mathrm{E}-01 \pm 2.32 \mathrm{E}-03$ | $1.43 \mathrm{E}-01 \pm 4.04 \mathrm{E}-03$ |
| 2 | $3.55 \mathrm{E}-01 \pm 1.98 \mathrm{E}-02$ | $3.59 \mathrm{E}-01 \pm 1.94 \mathrm{E}-02$ | $3.59 \mathrm{E}-01 \pm 1.45 \mathrm{E}-02$ | $3.59 \mathrm{E}-01 \pm 1.54 \mathrm{E}-02$ |
| 3 | $2.62 \mathrm{E}-01 \pm 2.63 \mathrm{E}-02$ | $2.64 \mathrm{E}-01 \pm 1.87 \mathrm{E}-02$ | $2.57 \mathrm{E}-01 \pm 1.63 \mathrm{E}-02$ | $2.58 \mathrm{E}-01 \pm 1.63 \mathrm{E}-02$ |
| 4 | $2.13 \mathrm{E}-02 \pm 7.59 \mathrm{E}-03$ | $2.15 \mathrm{E}-02 \pm 8.30 \mathrm{E}-03$ | $1.89 \mathrm{E}-02 \pm 5.66 \mathrm{E}-03$ | $2.40 \mathrm{E}-02 \pm 8.04 \mathrm{E}-03$ |
| 5 | $1.80 \mathrm{E}-02 \pm 8.58 \mathrm{E}-03$ | $2.09 \mathrm{E}-02 \pm 9.43 \mathrm{E}-03$ | $1.69 \mathrm{E}-02 \pm 8.06 \mathrm{E}-03$ | $1.75 \mathrm{E}-02 \pm 6.96 \mathrm{E}-03$ |
| 6 | $8.50 \mathrm{E}-02 \pm 3.22 \mathrm{E}-03$ | $8.34 \mathrm{E}-02 \pm 2.61 \mathrm{E}-03$ | $8.29 \mathrm{E}-02 \pm 2.18 \mathrm{E}-03$ | $8.32 \mathrm{E}-02 \pm 2.48 \mathrm{E}-03$ |
| 7 | $1.48 \mathrm{E}-01 \pm 1.96 \mathrm{E}-03$ | $1.48 \mathrm{E}-01 \pm 2.26 \mathrm{E}-03$ | $1.47 \mathrm{E}-01 \pm 1.43 \mathrm{E}-03$ | $1.48 \mathrm{E}-01 \pm 2.16 \mathrm{E}-03$ |
| 8 | $1.26 \mathrm{E}-01 \pm 7.80 \mathrm{E}-03$ | $1.25 \mathrm{E}-01 \pm 6.55 \mathrm{E}-03$ | $1.25 \mathrm{E}-01 \pm 7.77 \mathrm{E}-03$ | $1.28 \mathrm{E}-01 \pm 7.11 \mathrm{E}-03$ |
| 9 | $8.67 \mathrm{E}-02 \pm 2.00 \mathrm{E}-02$ | $7.54 \mathrm{E}-02 \pm 1.28 \mathrm{E}-02$ | $8.00 \mathrm{E}-02 \pm 1.41 \mathrm{E}-02$ | $7.55 \mathrm{E}-02 \pm 1.21 \mathrm{E}-02$ |
| 10 | $9.69 \mathrm{E}-03 \pm 4.61 \mathrm{E}-03$ | $9.43 \mathrm{E}-03 \pm 3.67 \mathrm{E}-03$ | $8.28 \mathrm{E}-03 \pm 2.93 \mathrm{E}-03$ | $8.77 \mathrm{E}-03 \pm 3.81 \mathrm{E}-03$ |
| 11 | $5.55 \mathrm{E}-02 \pm 4.36 \mathrm{E}-03$ | $5.37 \mathrm{E}-02 \pm 4.05 \mathrm{E}-03$ | $5.27 \mathrm{E}-02 \pm 3.65 \mathrm{E}-03$ | $5.22 \mathrm{E}-02 \pm 3.34 \mathrm{E}-03$ |
| 12 | $1.02 \mathrm{E}-01 \pm 2.09 \mathrm{E}-03$ | $1.01 \mathrm{E}-01 \pm 2.17 \mathrm{E}-03$ | $1.00 \mathrm{E}-01 \pm 1.96 \mathrm{E}-03$ | $1.00 \mathrm{E}-01 \pm 1.61 \mathrm{E}-03$ |
| 13 | $9.69 \mathrm{E}-02 \pm 3.06 \mathrm{E}-03$ | $9.59 \mathrm{E}-02 \pm 2.59 \mathrm{E}-03$ | $9.51 \mathrm{E}-02 \pm 1.97 \mathrm{E}-03$ | $9.53 \mathrm{E}-02 \pm 2.65 \mathrm{E}-03$ |
| 14 | $1.51 \mathrm{E}-02 \pm 3.87 \mathrm{E}-03$ | $1.49 \mathrm{E}-02 \pm 3.50 \mathrm{E}-03$ | $1.24 \mathrm{E}-02 \pm 2.09 \mathrm{E}-03$ | $1.33 \mathrm{E}-02 \pm 3.45 \mathrm{E}-03$ |
| 15 | $6.47 \mathrm{E}-02 \pm 7.06 \mathrm{E}-03$ | $6.17 \mathrm{E}-02 \pm 3.89 \mathrm{E}-03$ | $6.07 \mathrm{E}-02 \pm 2.92 \mathrm{E}-03$ | $6.01 \mathrm{E}-02 \pm 3.26 \mathrm{E}-03$ |
| 16 | $3.63 \mathrm{E}-02 \pm 9.78 \mathrm{E}-03$ | $3.23 \mathrm{E}-02 \pm 8.04 \mathrm{E}-03$ | $2.85 \mathrm{E}-02 \pm 7.47 \mathrm{E}-03$ | $2.92 \mathrm{E}-02 \pm 5.95 \mathrm{E}-03$ |
| 17 | $1.61 \mathrm{E}-01 \pm 1.09 \mathrm{E}-02$ | $1.54 \mathrm{E}-01 \pm 7.41 \mathrm{E}-03$ | $1.55 \mathrm{E}-01 \pm 8.81 \mathrm{E}-03$ | $1.52 \mathrm{E}-01 \pm 8.35 \mathrm{E}-03$ |
| 18 | $6.10 \mathrm{E}-02 \pm 4.02 \mathrm{E}-03$ | $5.89 \mathrm{E}-02 \pm 2.20 \mathrm{E}-03$ | $5.85 \mathrm{E}-02 \pm 2.19 \mathrm{E}-03$ | $5.88 \mathrm{E}-02 \pm 1.79 \mathrm{E}-03$ |
| 19 | $2.20 \mathrm{E}-01 \pm 1.47 \mathrm{E}-02$ | $2.14 \mathrm{E}-01 \pm 1.02 \mathrm{E}-02$ | $2.12 \mathrm{E}-01 \pm 1.03 \mathrm{E}-02$ | $2.14 \mathrm{E}-01 \pm 9.87 \mathrm{E}-03$ |
| 20 | $3.43 \mathrm{E}-01 \pm 6.81 \mathrm{E}-02$ | $3.45 \mathrm{E}-01 \pm 5.81 \mathrm{E}-02$ | $3.12 \mathrm{E}-01 \pm 9.11 \mathrm{E}-02$ | $2.94 \mathrm{E}-01 \pm 9.77 \mathrm{E}-02$ |
| No. of Best | 1 | 2 | 13 | 6 |

TABLE IV
Parameter Comparisons for Local Improvement on the Practical Problem

| Instance | $\varepsilon=1$ <br> Mean/Std. | $\varepsilon=10$ <br> Mean/Std. | $\varepsilon=50$ <br> Mean/Std. | $\varepsilon=100$ <br> Mean/Std. |
| :--: | :--: | :--: | :--: | :--: |
| 1 | $1.43 \mathrm{E}-01 \pm 2.92 \mathrm{E}-03$ | $1.44 \mathrm{E}-01 \pm 2.32 \mathrm{E}-03$ | $1.44 \mathrm{E}-01 \pm 4.19 \mathrm{E}-03$ | $1.44 \mathrm{E}-01 \pm 3.46 \mathrm{E}-03$ |
| 2 | $3.58 \mathrm{E}-01 \pm 1.53 \mathrm{E}-02$ | $3.59 \mathrm{E}-01 \pm 1.45 \mathrm{E}-02$ | $3.59 \mathrm{E}-01 \pm 1.53 \mathrm{E}-02$ | $3.56 \mathrm{E}-01 \pm 1.75 \mathrm{E}-02$ |
| 3 | $2.54 \mathrm{E}-01 \pm 1.63 \mathrm{E}-02$ | $2.57 \mathrm{E}-01 \pm 1.63 \mathrm{E}-02$ | $2.58 \mathrm{E}-01 \pm 1.51 \mathrm{E}-02$ | $2.59 \mathrm{E}-01 \pm 1.98 \mathrm{E}-02$ |
| 4 | $2.11 \mathrm{E}-02 \pm 6.98 \mathrm{E}-03$ | $1.89 \mathrm{E}-02 \pm 5.66 \mathrm{E}-03$ | $1.91 \mathrm{E}-02 \pm 7.60 \mathrm{E}-03$ | $2.25 \mathrm{E}-02 \pm 8.31 \mathrm{E}-03$ |
| 5 | $1.75 \mathrm{E}-02 \pm 7.06 \mathrm{E}-03$ | $1.69 \mathrm{E}-02 \pm 8.06 \mathrm{E}-03$ | $1.69 \mathrm{E}-02 \pm 6.18 \mathrm{E}-03$ | $1.73 \mathrm{E}-02 \pm 7.00 \mathrm{E}-03$ |
| 6 | $8.28 \mathrm{E}-02 \pm 2.11 \mathrm{E}-03$ | $8.29 \mathrm{E}-02 \pm 2.18 \mathrm{E}-03$ | $8.27 \mathrm{E}-02 \pm 1.86 \mathrm{E}-03$ | $8.30 \mathrm{E}-02 \pm 2.44 \mathrm{E}-03$ |
| 7 | $1.48 \mathrm{E}-01 \pm 2.19 \mathrm{E}-03$ | $1.47 \mathrm{E}-01 \pm 1.43 \mathrm{E}-03$ | $1.47 \mathrm{E}-01 \pm 1.96 \mathrm{E}-03$ | $1.47 \mathrm{E}-01 \pm 2.30 \mathrm{E}-03$ |
| 8 | $1.27 \mathrm{E}-01 \pm 5.53 \mathrm{E}-03$ | $1.25 \mathrm{E}-01 \pm 7.77 \mathrm{E}-03$ | $1.29 \mathrm{E}-01 \pm 4.61 \mathrm{E}-03$ | $1.27 \mathrm{E}-01 \pm 6.65 \mathrm{E}-03$ |
| 9 | $7.31 \mathrm{E}-02 \pm 1.13 \mathrm{E}-02$ | $8.00 \mathrm{E}-02 \pm 1.41 \mathrm{E}-02$ | $7.66 \mathrm{E}-02 \pm 1.62 \mathrm{E}-02$ | $7.66 \mathrm{E}-02 \pm 1.30 \mathrm{E}-02$ |
| 10 | $8.50 \mathrm{E}-03 \pm 4.00 \mathrm{E}-03$ | $8.28 \mathrm{E}-03 \pm 2.93 \mathrm{E}-03$ | $7.55 \mathrm{E}-03 \pm 3.58 \mathrm{E}-03$ | $9.21 \mathrm{E}-03 \pm 3.07 \mathrm{E}-03$ |
| 11 | $5.18 \mathrm{E}-02 \pm 4.85 \mathrm{E}-03$ | $5.27 \mathrm{E}-02 \pm 3.65 \mathrm{E}-03$ | $5.16 \mathrm{E}-02 \pm 4.43 \mathrm{E}-03$ | $5.14 \mathrm{E}-02 \pm 4.43 \mathrm{E}-03$ |
| 12 | $1.01 \mathrm{E}-01 \pm 1.76 \mathrm{E}-03$ | $1.00 \mathrm{E}-01 \pm 1.96 \mathrm{E}-03$ | $1.01 \mathrm{E}-01 \pm 1.74 \mathrm{E}-03$ | $9.99 \mathrm{E}-02 \pm 1.74 \mathrm{E}-03$ |
| 13 | $9.55 \mathrm{E}-02 \pm 2.16 \mathrm{E}-03$ | $9.51 \mathrm{E}-02 \pm 1.97 \mathrm{E}-03$ | $9.57 \mathrm{E}-02 \pm 2.94 \mathrm{E}-03$ | $9.45 \mathrm{E}-02 \pm 1.71 \mathrm{E}-03$ |
| 14 | $1.27 \mathrm{E}-02 \pm 2.51 \mathrm{E}-03$ | $1.24 \mathrm{E}-02 \pm 2.09 \mathrm{E}-03$ | $1.28 \mathrm{E}-02 \pm 1.96 \mathrm{E}-03$ | $1.26 \mathrm{E}-02 \pm 2.11 \mathrm{E}-03$ |
| 15 | $6.14 \mathrm{E}-02 \pm 3.84 \mathrm{E}-03$ | $6.07 \mathrm{E}-02 \pm 2.92 \mathrm{E}-03$ | $6.33 \mathrm{E}-02 \pm 5.14 \mathrm{E}-03$ | $6.15 \mathrm{E}-02 \pm 5.60 \mathrm{E}-03$ |
| 16 | $2.93 \mathrm{E}-02 \pm 6.80 \mathrm{E}-03$ | $2.85 \mathrm{E}-02 \pm 7.47 \mathrm{E}-03$ | $3.16 \mathrm{E}-02 \pm 7.75 \mathrm{E}-03$ | $2.96 \mathrm{E}-02 \pm 7.01 \mathrm{E}-03$ |
| 17 | $1.57 \mathrm{E}-01 \pm 1.01 \mathrm{E}-02$ | $1.55 \mathrm{E}-01 \pm 8.81 \mathrm{E}-03$ | $1.56 \mathrm{E}-01 \pm 8.73 \mathrm{E}-03$ | $1.54 \mathrm{E}-01 \pm 8.52 \mathrm{E}-03$ |
| 18 | $5.93 \mathrm{E}-02 \pm 2.40 \mathrm{E}-03$ | $5.85 \mathrm{E}-02 \pm 2.19 \mathrm{E}-03$ | $5.86 \mathrm{E}-02 \pm 2.03 \mathrm{E}-03$ | $5.95 \mathrm{E}-02 \pm 2.42 \mathrm{E}-03$ |
| 19 | $2.13 \mathrm{E}-01 \pm 1.10 \mathrm{E}-02$ | $2.12 \mathrm{E}-01 \pm 1.03 \mathrm{E}-02$ | $2.12 \mathrm{E}-01 \pm 7.25 \mathrm{E}-03$ | $2.13 \mathrm{E}-01 \pm 1.07 \mathrm{E}-02$ |
| 20 | $3.14 \mathrm{E}-01 \pm 8.71 \mathrm{E}-02$ | $3.12 \mathrm{E}-01 \pm 9.11 \mathrm{E}-02$ | $3.31 \mathrm{E}-01 \pm 7.48 \mathrm{E}-02$ | $3.17 \mathrm{E}-01 \pm 8.20 \mathrm{E}-02$ |
| No. of Best | 3 | 10 | 5 | 6 |

Thus, the computational complexity of resampling is $O(D N P)$. For the local improvement, the evolutionary search based on superior individuals requires $O(D \beta N P)$, and the information learning requires $O\left(D^{2}\right)$. Because $0<\beta<1$, the overall computational complexity of local improvement is between $O\left(D^{2}\right)$ and $O(D C)$, where we note that $0<C<N P$. We conclude from the aforementioned comparisons and corresponding analysis that the increase in computation cost is not significant. It is obvious that EDA-RL solves the operation optimization problem in BOF steelmaking efficiently.

## C. Further Test of EDA-RL as General Optimization Algorithm

To further verify the performance of EDA-RL, we carry out some numerical experiments described in this section. Some
complex functions based on black-box optimization [49] are considered as benchmark problems. To ensure the fairness of comparisons, 51 independent runs are conducted for the blackbox optimization benchmark problems, and the MaxFEs is set to $10000 \times D$.

1) Benchmark Functions: The benchmark problems belong to the class of real-parameter single objective minimum optimization problems without knowledge of the exact equations. These problems consist of several basic functions, and their landscapes may have contained multiple nonseparable local optima. Furthermore, these black-box optimization functions have different properties as a result of variable shift and variable rotation operations (such as rotated high conditioned elliptic function, shifted and rotated Ackley's function, shifted and rotated Schwefel's function, etc.) As far as we know, a successful algorithm for the solution of these problems

TABLE V
Comparison Results of Minimum Objective Function Values

| Instance | EDA <br> Mean/std. | EDA-R <br> Mean/std. | EDA-RL <br> Mean/std. |
| :--: | :--: | :--: | :--: |
| 1 | $1.47 \mathrm{E}-01 \pm 4.66 \mathrm{E}-03$ | $1.45 \mathrm{E}-01 \pm 3.95 \mathrm{E}-03$ | $\mathbf{1 . 4 4 E - 0 1 \pm 2 . 3 2 E - 0 3}$ |
| 2 | $3.69 \mathrm{E}-01 \pm 1.99 \mathrm{E}-02$ | $\mathbf{3 . 5 5 E - 0 1 \pm 1 . 8 2 E - 0 2}$ | $3.59 \mathrm{E}-01 \pm 1.45 \mathrm{E}-02$ |
| 3 | $2.62 \mathrm{E}-01 \pm 2.16 \mathrm{E}-02$ | $2.60 \mathrm{E}-01 \pm 1.57 \mathrm{E}-02$ | $\mathbf{2 . 5 7 E - 0 1 \pm 1 . 6 3 E - 0 2}$ |
| 4 | $2.79 \mathrm{E}-02 \pm 8.99 \mathrm{E}-03$ | $2.59 \mathrm{E}-02 \pm 9.56 \mathrm{E}-03$ | $\mathbf{1 . 8 9 E - 0 2 \pm 5 . 6 6 E - 0 3}$ |
| 5 | $2.58 \mathrm{E}-02 \pm 1.26 \mathrm{E}-02$ | $1.92 \mathrm{E}-02 \pm 7.99 \mathrm{E}-03$ | $\mathbf{1 . 6 9 E - 0 2 \pm 8 . 0 6 E - 0 3}$ |
| 6 | $8.61 \mathrm{E}-02 \pm 3.53 \mathrm{E}-03$ | $8.46 \mathrm{E}-02 \pm 2.65 \mathrm{E}-03$ | $\mathbf{8 . 2 9 E - 0 2 \pm 2 . 1 8 E - 0 3}$ |
| 7 | $1.50 \mathrm{E}-01 \pm 2.81 \mathrm{E}-03$ | $1.49 \mathrm{E}-01 \pm 2.97 \mathrm{E}-03$ | $\mathbf{1 . 4 7 E - 0 1 \pm 1 . 4 3 E - 0 3}$ |
| 8 | $\mathbf{1 . 2 1 E - 0 1 \pm 8 . 5 1 E - 0 3}$ | $1.24 \mathrm{E}-01 \pm 7.94 \mathrm{E}-03$ | $1.25 \mathrm{E}-01 \pm 7.77 \mathrm{E}-03$ |
| 9 | $8.09 \mathrm{E}-02 \pm 2.00 \mathrm{E}-02$ | $8.22 \mathrm{E}-02 \pm 1.49 \mathrm{E}-02$ | $\mathbf{8 . 0 0 E - 0 2 \pm 1 . 4 1 E - 0 2}$ |
| 10 | $1.11 \mathrm{E}-02 \pm 4.17 \mathrm{E}-03$ | $8.76 \mathrm{E}-03 \pm 3.33 \mathrm{E}-03$ | $\mathbf{8 . 2 8 E - 0 3 \pm 2 . 9 3 E - 0 3}$ |
| 11 | $5.34 \mathrm{E}-02 \pm 5.36 \mathrm{E}-03$ | $5.48 \mathrm{E}-02 \pm 3.53 \mathrm{E}-03$ | $\mathbf{5 . 2 7 E - 0 2 \pm 3 . 6 5 E - 0 3}$ |
| 12 | $1.03 \mathrm{E}-01 \pm 3.64 \mathrm{E}-03$ | $1.02 \mathrm{E}-01 \pm 2.07 \mathrm{E}-03$ | $\mathbf{1 . 0 0 E - 0 1 \pm 1 . 9 6 E - 0 3}$ |
| 13 | $9.57 \mathrm{E}-02 \pm 2.20 \mathrm{E}-03$ | $\mathbf{9 . 4 9 E - 0 2 \pm 2 . 0 9 E - 0 3}$ | $9.51 \mathrm{E}-02 \pm 1.97 \mathrm{E}-03$ |
| 14 | $1.53 \mathrm{E}-02 \pm 3.80 \mathrm{E}-03$ | $1.32 \mathrm{E}-02 \pm 2.07 \mathrm{E}-03$ | $\mathbf{1 . 2 4 E - 0 2 \pm 2 . 0 9 E - 0 3}$ |
| 15 | $6.54 \mathrm{E}-02 \pm 7.01 \mathrm{E}-03$ | $6.19 \mathrm{E}-02 \pm 3.34 \mathrm{E}-03$ | $\mathbf{6 . 0 7 E - 0 2 \pm 2 . 9 2 E - 0 3}$ |
| 16 | $3.52 \mathrm{E}-02 \pm 1.08 \mathrm{E}-02$ | $3.03 \mathrm{E}-02 \pm 6.37 \mathrm{E}-03$ | $\mathbf{2 . 8 5 E - 0 2 \pm 7 . 4 7 E - 0 3}$ |
| 17 | $1.62 \mathrm{E}-01 \pm 1.31 \mathrm{E}-02$ | $1.60 \mathrm{E}-01 \pm 9.79 \mathrm{E}-03$ | $\mathbf{1 . 5 5 E - 0 1 \pm 8 . 8 1 E - 0 3}$ |
| 18 | $6.02 \mathrm{E}-02 \pm 2.79 \mathrm{E}-03$ | $5.88 \mathrm{E}-02 \pm 2.42 \mathrm{E}-03$ | $\mathbf{5 . 8 5 E - 0 2 \pm 2 . 1 9 E - 0 3}$ |
| 19 | $2.20 \mathrm{E}-01 \pm 9.84 \mathrm{E}-03$ | $2.13 \mathrm{E}-01 \pm 9.65 \mathrm{E}-03$ | $\mathbf{2 . 1 2 E - 0 1 \pm 1 . 0 3 E - 0 2}$ |
| 20 | $3.51 \mathrm{E}-01 \pm 6.52 \mathrm{E}-02$ | $3.46 \mathrm{E}-01 \pm 5.76 \mathrm{E}-02$ | $\mathbf{3 . 1 2 E - 0 1 \pm 9 . 1 1 E - 0 2}$ |
| No. of Best | 1 | 2 | 17 |

TABLE VI
Performance Comparisons of EDA, EDA-R, and EDA-RL

| Algorithm | Average Minimum Objective Function Value |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  | MAXAE | MINAE | MAE | STD |
| EDA | $3.69 \mathrm{E}-01$ | $1.11 \mathrm{E}-02$ | $1.22 \mathrm{E}-01$ | $1.05 \mathrm{E}-01$ |
| EDA-R | $\mathbf{3 . 5 5 E - 0 1}$ | $8.76 \mathrm{E}-03$ | $1.19 \mathrm{E}-01$ | $1.03 \mathrm{E}-01$ |
| EDA-RL | $3.59 \mathrm{E}-01$ | $\mathbf{8 . 2 8 E - 0 3}$ | $\mathbf{1 . 1 6 E - 0 1}$ | $\mathbf{1 . 0 1 E - 0 1}$ |

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

| Instance | T $\left({ }^{\circ} \mathrm{C}\right)$ |  |  | C (\%) |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Expectation <br> Value | Absolute Error |  | Expectation <br> Value | Absolute Error |  |
|  |  | EK | EDA-RL |  | EK | EDA-RL |
| 1 | $1.644 \mathrm{E}+03$ | $1.50 \mathrm{E}+01$ | 2.73E+00 | $2.30 \mathrm{E}-02$ | $6.00 \mathrm{E}-03$ | 4.40E-05 |
| 2 | $1.641 \mathrm{E}+03$ | $7.00 \mathrm{E}+00$ | 4.11E+00 | $3.50 \mathrm{E}-02$ | $1.60 \mathrm{E}-02$ | 5.44E-03 |
| 3 | $1.650 \mathrm{E}+03$ | $1.00 \mathrm{E}+01$ | 3.41E-01 | $3.30 \mathrm{E}-02$ | $1.20 \mathrm{E}-02$ | 8.58E-03 |
| 4 | $1.645 \mathrm{E}+03$ | $7.00 \mathrm{E}+00$ | 2.54E-01 | $2.90 \mathrm{E}-02$ | $5.00 \mathrm{E}-03$ | 1.80E-05 |
| 5 | $1.648 \mathrm{E}+03$ | $1.10 \mathrm{E}+01$ | 4.87E-02 | $2.50 \mathrm{E}-02$ | $2.00 \mathrm{E}-03$ | 6.90E-05 |
| 6 | $1.651 \mathrm{E}+03$ | $9.00 \mathrm{E}+00$ | 2.40E-01 | $2.80 \mathrm{E}-02$ | $4.00 \mathrm{E}-03$ | 3.14E-03 |
| 7 | $1.655 \mathrm{E}+03$ | $2.70 \mathrm{E}+01$ | 2.23E-02 | $2.10 \mathrm{E}-02$ | $9.00 \mathrm{E}-03$ | 6.02E-03 |
| 8 | $1.658 \mathrm{E}+03$ | $6.00 \mathrm{E}+00$ | 1.96E+00 | $2.70 \mathrm{E}-02$ | $5.00 \mathrm{E}-03$ | 1.53E-03 |
| 9 | $1.656 \mathrm{E}+03$ | $1.80 \mathrm{E}+01$ | 1.02E-01 | $3.10 \mathrm{E}-02$ | $1.00 \mathrm{E}-02$ | 2.53E-03 |
| 10 | $1.653 \mathrm{E}+03$ | $1.90 \mathrm{E}+01$ | 6.22E-03 | $2.60 \mathrm{E}-02$ | $6.00 \mathrm{E}-03$ | 6.50E-05 |
| 11 | $1.655 \mathrm{E}+03$ | $1.00 \mathrm{E}+01$ | 5.97E-01 | $2.50 \mathrm{E}-02$ | $2.00 \mathrm{E}-03$ | 1.71E-03 |
| 12 | $1.654 \mathrm{E}+03$ | $1.00 \mathrm{E}+00$ | 1.18E-02 | $3.10 \mathrm{E}-02$ | $8.00 \mathrm{E}-03$ | 3.86E-03 |
| 13 | $1.662 \mathrm{E}+03$ | $1.20 \mathrm{E}+01$ | 1.83E+00 | $2.60 \mathrm{E}-02$ | $2.00 \mathrm{E}-03$ | 3.00E-05 |
| 14 | $1.664 \mathrm{E}+03$ | $3.00 \mathrm{E}+00$ | 1.65E-01 | $2.60 \mathrm{E}-02$ | $8.00 \mathrm{E}-03$ | 2.70E-05 |
| 15 | $1.665 \mathrm{E}+03$ | $1.40 \mathrm{E}+01$ | 1.09E+00 | $2.70 \mathrm{E}-02$ | $6.00 \mathrm{E}-03$ | 4.00E-06 |
| 16 | $1.664 \mathrm{E}+03$ | $1.90 \mathrm{E}+01$ | 3.55E-01 | $2.30 \mathrm{E}-02$ | $5.00 \mathrm{E}-03$ | 2.12E-04 |
| 17 | $1.662 \mathrm{E}+03$ | $6.00 \mathrm{E}+00$ | 1.98E+00 | $3.00 \mathrm{E}-02$ | $7.00 \mathrm{E}-03$ | 2.07E-03 |
| 18 | $1.665 \mathrm{E}+03$ | $1.20 \mathrm{E}+01$ | 1.09E+00 | $2.70 \mathrm{E}-02$ | $1.00 \mathrm{E}-03$ | 1.50E-05 |
| 19 | $1.676 \mathrm{E}+03$ | $8.00 \mathrm{E}+00$ | 8.80E-01 | $3.20 \mathrm{E}-02$ | $7.00 \mathrm{E}-03$ | 3.79E-03 |
| 20 | $1.671 \mathrm{E}+03$ | $2.40 \mathrm{E}+01$ | 3.22E+00 | $2.30 \mathrm{E}-02$ | $5.00 \mathrm{E}-03$ | 2.95E-03 |

TABLE VIII
Performance Comparisons Between EK and EDA-RL

| Objective | EK |  |  |  | EDA-RL |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | MAXAE $\left({ }^{\circ} \mathrm{C} \%\right)$ | MINAE $\left({ }^{\circ} \mathrm{C} \%\right)$ | MAE | STD | MAXAE $\left({ }^{\circ} \mathrm{C} \%\right)$ | MINAE $\left({ }^{\circ} \mathrm{C} \%\right)$ | MAE | STD |
| T | $2.70 \mathrm{E}+01$ | $1.00 \mathrm{E}+00$ | $1.19 \mathrm{E}+01$ | $6.70 \mathrm{E}+00$ | 4.11E+00 | 6.22E-03 | 1.05E+00 | 1.21E+00 |
| C | $1.60 \mathrm{E}-02$ | $1.00 \mathrm{E}-03$ | $6.30 \mathrm{E}-03$ | $3.63 \mathrm{E}-03$ | 8.58E-03 | 4.00E-06 | 2.10E-03 | 2.46E-03 |

![img-8.jpeg](img-8.jpeg)

Fig. 9. Number of best results between EDA-RL and state-of-the-art algorithms.

EDA converges faster than EDA-R in a few unimodal blackbox optimization problems, the latter performs better in terms of its exploration ability for multimodal problems. Moreover, with the L strategy, EDA-RL selects the superior individuals to yield the best individual in the current population, and employs operators with information learning. Thus, EDA-RL can take full advantage of population information in the later stage of the process to enhance the exploitation ability of the algorithm and can yield some better solutions than EDA and EDA-R.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Convergence curves of EDA, EDA-R, and EDA-RL on four 10-D problems: (a) Fun2, (b) Fun3, (c) Fun4, and (d) Fun6.

4) Comparisons With State-of-the-Art Algorithms: To further demonstrate the competitiveness of our proposed algorithm, we compare EDA-RL to some state-of-the-art

TABLE IX
Parameter Comparisons for Resampling on Benchmark Problems

| Fun. | $D$ | $\theta=20 \%$ <br> Mean/std. | $\theta=40 \%$ <br> Mean/std. | $\theta=60 \%$ <br> Mean/std. | $\theta=80 \%$ <br> Mean/std. |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Fun2 | 10 | $4.10 \mathrm{E}+01 \pm 3.69 \mathrm{E}+01$ | $3.85 \mathrm{E}+01 \pm 4.58 \mathrm{E}+01$ | 2.23E+01 $\pm 1.91 \mathrm{E}+01$ | $2.70 \mathrm{E}+01 \pm 2.51 \mathrm{E}+01$ |
|  | 30 | $2.52 \mathrm{E}+02 \pm 1.16 \mathrm{E}+02$ | $2.49 \mathrm{E}+02 \pm 1.08 \mathrm{E}+02$ | 2.16E+02 $\pm 5.63 \mathrm{E}+01$ | $2.50 \mathrm{E}+02 \pm 9.29 \mathrm{E}+01$ |
|  | 50 | $4.09 \mathrm{E}+02 \pm 2.32 \mathrm{E}+02$ | $3.99 \mathrm{E}+02 \pm 2.57 \mathrm{E}+02$ | 3.67E+02 $\pm 1.96 \mathrm{E}+02$ | $4.17 \mathrm{E}+02 \pm 1.95 \mathrm{E}+02$ |
| Fun3 | 10 | $3.42 \mathrm{E}+02 \pm 2.36 \mathrm{E}+02$ | 2.34E+02 $\pm 2.13 \mathrm{E}+02$ | 2.34E+02 $\pm 1.86 \mathrm{E}+02$ | $2.49 \mathrm{E}+02 \pm 1.85 \mathrm{E}+02$ |
|  | 30 | $3.70 \mathrm{E}+03 \pm 7.12 \mathrm{E}+02$ | $3.32 \mathrm{E}+03 \pm 6.12 \mathrm{E}+02$ | $3.06 \mathrm{E}+03 \pm 5.06 \mathrm{E}+02$ | 2.93E+03 $\pm 4.04 \mathrm{E}+02$ |
|  | 50 | $7.65 \mathrm{E}+03 \pm 9.64 \mathrm{E}+02$ | $6.98 \mathrm{E}+03 \pm 8.73 \mathrm{E}+02$ | 6.37E+03 $\pm 6.43 \mathrm{E}+02$ | $6.58 \mathrm{E}+03 \pm 6.92 \mathrm{E}+02$ |
| Fun8 | 10 | $3.06 \mathrm{E}+02 \pm 8.78 \mathrm{E}+01$ | $3.46 \mathrm{E}+02 \pm 1.28 \mathrm{E}+02$ | 2.45E+02 $\pm 9.01 \mathrm{E}+01$ | $3.23 \mathrm{E}+02 \pm 8.80 \mathrm{E}+01$ |
|  | 30 | $2.96 \mathrm{E}+02 \pm 2.80 \mathrm{E}+01$ | $3.42 \mathrm{E}+02 \pm 2.10 \mathrm{E}+02$ | 2.84E+02 $\pm 5.43 \mathrm{E}+01$ | $3.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ |
|  | 50 | $4.60 \mathrm{E}+02 \pm 4.25 \mathrm{E}+02$ | $5.19 \mathrm{E}+02 \pm 5.95 \mathrm{E}+02$ | 4.00E+02 $\pm 0.00 \mathrm{E}+00$ | $5.19 \mathrm{E}+02 \pm 5.95 \mathrm{E}+02$ |
| No. of Best |  | 0 | 1 | 8 | 1 |

TABLE X
Parameter Comparisons for Local Improvement on Benchmark Problems

| Fun. | $D$ | $\begin{gathered} c=1 \\ \text { Mean/std. } \end{gathered}$ | $\begin{gathered} c=10 \\ \text { Mean/std. } \end{gathered}$ | $\begin{gathered} c=50 \\ \text { Mean/std. } \end{gathered}$ | $\begin{gathered} c=100 \\ \text { Mean/std. } \end{gathered}$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Fun2 | 10 | $3.52 \mathrm{E}+01 \pm 3.95 \mathrm{E}+01$ | 2.23E+01 $\pm 1.91 \mathrm{E}+01$ | $5.37 \mathrm{E}+01 \pm 5.54 \mathrm{E}+01$ | $4.65 \mathrm{E}+01 \pm 5.18 \mathrm{E}+01$ |
|  | 30 | $2.48 \mathrm{E}+02 \pm 9.76 \mathrm{E}+01$ | 2.16E+02 $\pm 5.63 \mathrm{E}+01$ | $2.90 \mathrm{E}+02 \pm 1.02 \mathrm{E}+02$ | $3.18 \mathrm{E}+02 \pm 1.33 \mathrm{E}+02$ |
|  | 50 | 3.07E+02 $\pm 1.85 \mathrm{E}+02$ | $3.67 \mathrm{E}+02 \pm 1.96 \mathrm{E}+02$ | $5.87 \mathrm{E}+02 \pm 2.58 \mathrm{E}+02$ | $6.24 \mathrm{E}+02 \pm 3.21 \mathrm{E}+02$ |
| Fun3 | 10 | $2.47 \mathrm{E}+02 \pm 2.04 \mathrm{E}+02$ | 2.34E+02 $\pm 1.86 \mathrm{E}+02$ | $4.03 \mathrm{E}+02 \pm 2.44 \mathrm{E}+02$ | $4.39 \mathrm{E}+02 \pm 2.56 \mathrm{E}+02$ |
|  | 30 | 2.81E+03 $\pm 8.07 \mathrm{E}+02$ | $3.06 \mathrm{E}+03 \pm 5.06 \mathrm{E}+02$ | $3.36 \mathrm{E}+03 \pm 1.03 \mathrm{E}+03$ | $3.08 \mathrm{E}+03 \pm 1.15 \mathrm{E}+03$ |
|  | 50 | $6.48 \mathrm{E}+03 \pm 7.09 \mathrm{E}+02$ | 6.37E+03 $\pm 6.43 \mathrm{E}+02$ | $8.03 \mathrm{E}+03 \pm 9.56 \mathrm{E}+02$ | $8.85 \mathrm{E}+03 \pm 1.23 \mathrm{E}+03$ |
| Fun8 | 10 | $3.52 \mathrm{E}+02 \pm 1.24 \mathrm{E}+02$ | 2.45E+02 $\pm 9.01 \mathrm{E}+01$ | $3.61 \mathrm{E}+02 \pm 1.38 \mathrm{E}+02$ | $3.78 \mathrm{E}+02 \pm 1.50 \mathrm{E}+02$ |
|  | 30 | $5.70 \mathrm{E}+02 \pm 6.56 \mathrm{E}+02$ | 2.84E+02 $\pm 5.43 \mathrm{E}+01$ | $6.11 \mathrm{E}+02 \pm 7.66 \mathrm{E}+02$ | $8.19 \mathrm{E}+02 \pm 8.21 \mathrm{E}+02$ |
|  | 50 | $6.96 \mathrm{E}+02 \pm 9.07 \mathrm{E}+02$ | 4.00E+02 $\pm 0.00 \mathrm{E}+00$ | $5.21 \mathrm{E}+02 \pm 6.03 \mathrm{E}+02$ | $5.81 \mathrm{E}+02 \pm 7.30 \mathrm{E}+02$ |
| No. of Best |  | 2 | 7 | 0 | 0 |

TABLE XI
EXPERIMENTAL RESULTS OF SYRATEGY COMPARISONS ON 10-D BENCHMARK PROBLEMS

| $10-D$ | EDA <br> Mean/std. | EDA-R <br> Mean/std. | EDA-RL <br> Mean/std. |
| :--: | :--: | :--: | :--: |
| Fun1 | $4.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ | $4.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ | 3.88E+02 $\pm 4.32 \mathrm{E}+01$ |
| Fun2 | $5.46 \mathrm{E}+02 \pm 3.08 \mathrm{E}+02$ | $4.74 \mathrm{E}+02 \pm 3.31 \mathrm{E}+02$ | 2.00E+01 $\pm 1.47 \mathrm{E}+01$ |
| Fun3 | $6.51 \mathrm{E}+02 \pm 3.42 \mathrm{E}+02$ | $5.29 \mathrm{E}+02 \pm 2.89 \mathrm{E}+02$ | 1.28E+02 $\pm 1.17 \mathrm{E}+02$ |
| Fun4 | $2.06 \mathrm{E}+02 \pm 4.49 \mathrm{E}+00$ | $2.00 \mathrm{E}+02 \pm 4.42 \mathrm{E}-02$ | 1.98E+02 $\pm 9.09 \mathrm{E}+00$ |
| Fun5 | $2.01 \mathrm{E}+02 \pm 1.98 \mathrm{E}+00$ | $2.00 \mathrm{E}+02 \pm 1.59 \mathrm{E}-01$ | 1.98E+02 $\pm 9.92 \mathrm{E}+00$ |
| Fun6 | $1.32 \mathrm{E}+02 \pm 3.26 \mathrm{E}+01$ | $1.47 \mathrm{E}+02 \pm 3.72 \mathrm{E}+01$ | 1.08E+02 $\pm 1.24 \mathrm{E}+01$ |
| Fun7 | $3.02 \mathrm{E}+02 \pm 4.31 \mathrm{E}+00$ | 3.00E+02 $\pm 2.31 \mathrm{E}-01$ | 3.00E+02 $\pm 6.09 \mathrm{E}-01$ |
| Fun8 | $3.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ | $3.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ | 2.45E+02 $\pm 9.01 \mathrm{E}+01$ |
| No. of Best | 0 | 1 | 8 |

TABLE XII
EXPERIMENTAL RESULTS OF SYRATEGY COMPARISONS ON 30-D BENCHMARK PROBLEMS

| $30-D$ | EDA <br> Mean/std. | EDA-R <br> Mean/std. | EDA-RL <br> Mean/std. |
| :--: | :--: | :--: | :--: |
| Fun1 | $3.45 \mathrm{E}+02 \pm 7.73 \mathrm{E}+01$ | $3.30 \mathrm{E}+02 \pm 7.67 \mathrm{E}+01$ | 2.52E+02 $\pm 6.04 \mathrm{E}+01$ |
| Fun2 | $5.37 \mathrm{E}+03 \pm 1.41 \mathrm{E}+03$ | $4.95 \mathrm{E}+03 \pm 1.75 \mathrm{E}+03$ | 2.01E+02 $\pm 6.06 \mathrm{E}+01$ |
| Fun3 | $6.59 \mathrm{E}+03 \pm 3.59 \mathrm{E}+02$ | $6.25 \mathrm{E}+03 \pm 1.21 \mathrm{E}+03$ | 2.55E+03 $\pm 8.10 \mathrm{E}+02$ |
| Fun4 | $2.18 \mathrm{E}+02 \pm 5.92 \mathrm{E}+00$ | 2.05E+02 $\pm 3.23 \mathrm{E}+00$ | $2.10 \mathrm{E}+02 \pm 4.47 \mathrm{E}+00$ |
| Fun5 | $2.65 \mathrm{E}+02 \pm 7.83 \mathrm{E}+00$ | $2.44 \mathrm{E}+02 \pm 1.86 \mathrm{E}+01$ | 2.10E+02 $\pm 1.65 \mathrm{E}+01$ |
| Fun6 | 2.00E+02 $\pm 8.27 \mathrm{E}-05$ | 2.00E+02 $\pm 1.47 \mathrm{E}-04$ | 2.00E+02 $\pm 1.79 \mathrm{E}-04$ |
| Fun7 | $4.50 \mathrm{E}+02 \pm 5.98 \mathrm{E}+01$ | 3.40E+02 $\pm 1.83 \mathrm{E}+01$ | $3.91 \mathrm{E}+02 \pm 4.79 \mathrm{E}+01$ |
| Fun8 | $3.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ | $3.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ | 2.88E+02 $\pm 4.75 \mathrm{E}+01$ |
| No. of Best | 1 | 3 | 6 |

algorithms, using their reported results, such as DE with an individual-dependent (IDE) [22], comprehensive learning particle swarm optimizer (CLPSO) [50], DE with an adaptive
strategy (SaDE) [51], and restart covariance matrix adaptation evolution strategy with increasing population size (IPOP-CMA-ES) [52]. These state-of-the-art algorithms have been

TABLE XIII
Experimental Results of Strategy Comparisons on 50-D Benchmark Problems

| $50-D$ | EDA <br> Mean/std. | EDA-R <br> Mean/std. | EDA-RL <br> Mean/std. |
| :--: | :--: | :--: | :--: |
| Fun1 | $8.26 \mathrm{E}+02 \pm 3.86 \mathrm{E}+02$ | $7.34 \mathrm{E}+02 \pm 4.27 \mathrm{E}+02$ | $4.97 \mathrm{E}+02 \pm 4.14 \mathrm{E}+02$ |
| Fun2 | $6.78 \mathrm{E}+03 \pm 5.09 \mathrm{E}+03$ | $6.21 \mathrm{E}+03 \pm 5.28 \mathrm{E}+03$ | $2.87 \mathrm{E}+02 \pm 1.50 \mathrm{E}+02$ |
| Fun3 | $1.29 \mathrm{E}+04 \pm 4.58 \mathrm{E}+02$ | $1.25 \mathrm{E}+04 \pm 1.59 \mathrm{E}+03$ | $6.41 \mathrm{E}+03 \pm 6.96 \mathrm{E}+02$ |
| Fun4 | $2.47 \mathrm{E}+02 \pm 9.71 \mathrm{E}+00$ | $2.12 \mathrm{E}+02 \pm 4.42 \mathrm{E}+00$ | $2.20 \mathrm{E}+02 \pm 6.67 \mathrm{E}+00$ |
| Fun5 | $3.26 \mathrm{E}+02 \pm 9.00 \mathrm{E}+00$ | $2.99 \mathrm{E}+02 \pm 7.78 \mathrm{E}+00$ | $3.02 \mathrm{E}+02 \pm 7.99 \mathrm{E}+00$ |
| Fun6 | $2.00 \mathrm{E}+02 \pm 1.82 \mathrm{E}-04$ | $2.00 \mathrm{E}+02 \pm 1.71 \mathrm{E}-04$ | $2.00 \mathrm{E}+02 \pm 2.66 \mathrm{E}-05$ |
| Fun7 | $8.92 \mathrm{E}+02 \pm 1.20 \mathrm{E}+02$ | $4.13 \mathrm{E}+02 \pm 4.94 \mathrm{E}+01$ | $5.47 \mathrm{E}+02 \pm 1.14 \mathrm{E}+02$ |
| Fun8 | $4.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ | $4.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ | $4.00 \mathrm{E}+02 \pm 0.00 \mathrm{E}+00$ |
| No. of Best | 2 | 5 | 5 |

TABLE XIV
Comparison Results Between EDA-RL and State-of-the-Art Algorithms on 10-D Benchmark Problems

| $10-D$ | IDE <br> Mean/std. |  | CLPSO <br> Mean/std. |  | IPOP-CMA-ES <br> Mean/std. |  | SaDE <br> Mean/std. |  | EDA-RL <br> Mean/std. |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Fun1 | $\begin{aligned} & 3.96 \mathrm{E}+02 \\ & \pm 2.80 \mathrm{E}+01 \end{aligned}$ | $\approx$ | $\begin{aligned} & 2.88 \mathrm{E}+02 \\ & \pm 1.21 \mathrm{E}+02 \end{aligned}$ | $+$ | $\begin{aligned} & 3.75 \mathrm{E}+02 \\ & \pm 7.17 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 4.00 \mathrm{E}+02 \\ & \pm 0.00 \mathrm{E}+00 \end{aligned}$ | $=$ | $\begin{aligned} & 3.88 \mathrm{E}+02 \\ & \pm 4.32 \mathrm{E}+01 \end{aligned}$ |
| Fun2 | $\begin{aligned} & 9.15 \mathrm{E}+00 \\ & \pm 5.82 \mathrm{E}+00 \end{aligned}$ | $\approx$ | $\begin{aligned} & 4.46 \mathrm{E}+01 \\ & \pm 5.04 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 7.33 \mathrm{E}+01 \\ & \pm 4.94 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.65 \mathrm{E}+01 \\ & \pm 2.63 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 2.00 \mathrm{E}+01 \\ & \pm 1.47 \mathrm{E}+01 \end{aligned}$ |
| Fun3 | $\begin{aligned} & 4.03 \mathrm{E}+02 \\ & \pm 1.87 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 7.42 \mathrm{E}+02 \\ & \pm 1.94 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 8.62 \mathrm{E}+01 \\ & \pm 6.61 \mathrm{E}+01 \end{aligned}$ | $+$ | $\begin{aligned} & 6.74 \mathrm{E}+02 \\ & \pm 3.19 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 1.28 \mathrm{E}+02 \\ & \pm 1.17 \mathrm{E}+02 \end{aligned}$ |
| Fun4 | $\begin{aligned} & 1.98 \mathrm{E}+02 \\ & \pm 1.34 \mathrm{E}+01 \end{aligned}$ | $\approx$ | $\begin{aligned} & 1.42 \mathrm{E}+02 \\ & \pm 3.46 \mathrm{E}+01 \end{aligned}$ | $+$ | $\begin{aligned} & 2.09 \mathrm{E}+02 \\ & \pm 7.02 \mathrm{E}+00 \end{aligned}$ | - | $\begin{aligned} & 1.94 \mathrm{E}+02 \\ & \pm 2.17 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 1.98 \mathrm{E}+02 \\ & \pm 9.09 \mathrm{E}+00 \end{aligned}$ |
| Fun5 | $\begin{aligned} & 2.00 \mathrm{E}+02 \\ & \pm 2.02 \mathrm{E}-05 \end{aligned}$ | $\approx$ | $\begin{aligned} & 1.92 \mathrm{E}+02 \\ & \pm 3.19 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 2.06 \mathrm{E}+02 \\ & \pm 6.71 \mathrm{E}+00 \end{aligned}$ | - | $\begin{aligned} & 1.99 \mathrm{E}+02 \\ & \pm 1.12 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 1.98 \mathrm{E}+02 \\ & \pm 9.92 \mathrm{E}+00 \end{aligned}$ |
| Fun6 | $\begin{aligned} & 1.20 \mathrm{E}+02 \\ & \pm 3.48 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 1.22 \mathrm{E}+02 \\ & \pm 2.16 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.04 \mathrm{E}+02 \\ & \pm 1.51 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 1.11 \mathrm{E}+02 \\ & \pm 1.93 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 1.08 \mathrm{E}+02 \\ & \pm 1.24 \mathrm{E}+01 \end{aligned}$ |
| Fun7 | $\begin{aligned} & 3.02 \mathrm{E}+02 \\ & \pm 1.40 \mathrm{E}+01 \end{aligned}$ | $\approx$ | $\begin{aligned} & 3.25 \mathrm{E}+02 \\ & \pm 3.53 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 4.55 \mathrm{E}+02 \\ & \pm 7.92 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 3.04 \mathrm{E}+02 \\ & \pm 1.96 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 3.00 \mathrm{E}+02 \\ & \pm 6.09 \mathrm{E}-01 \end{aligned}$ |
| Fun8 | $\begin{aligned} & 2.88 \mathrm{E}+02 \\ & \pm 4.75 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.50 \mathrm{E}+02 \\ & \pm 8.60 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 3.00 \mathrm{E}+02 \\ & \pm 0.00 \mathrm{E}+00 \end{aligned}$ | - | $\begin{aligned} & 2.92 \mathrm{E}+02 \\ & \pm 3.92 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.45 \mathrm{E}+02 \\ & \pm 9.01 \mathrm{E}+01 \end{aligned}$ |
| No. of Best | 1 |  | 3 |  | 1 |  | 0 |  | 3 |
| - |  | 3 |  | 4 |  | 6 |  | 2 |  |
| $=$ |  | 5 |  | 2 |  | 1 |  | 6 |  |
| $+$ |  | 0 |  | 2 |  | 1 |  | 0 |  |

shown to be successful in solving black-box optimization problems, and have yielded better test results for some benchmark functions than some basic optimization algorithms, such as DE, PSO, and CMA-ES.

Fig. 9 shows the number of best results obtained with EDARL and the state-of-the-art algorithms. Statistical results concerning significant differences are shown in Tables XIV-XVI. In comparing statistically significant differences, the twosided Wilcoxon rank sum test [22] is conducted to evaluate performance differences at the 0.05 significance level. The symbol " + " indicates that the compared algorithm performs better than EDA-RL, the symbol "-" indicates that EDA-RL performs better, and the symbol " $=$ " indicates no significant difference between the performance of EDA-RL and the compared algorithm.

As is evident from the aforementioned comparison results, it is notable that for 10/30/50-dimension problems, in most functions, EDA-RL is able to find solutions of the same or better quality, because R can identify multimodal and different local optima for multiple variables effectively, and L can improve the local search ability to make convergence faster in the later
search process. This implies that EDA-RL can address larger complex functions with a large number of local optima more effectively. On the other hand, EDA-RL fails to perform the best for Fun2, Fun3, and Fun4, but it still remains competitive with other state-of-the-art algorithms. Therefore, as the results show, our proposed algorithm can effectively solve some complex black-box optimization problems and exhibit a powerful generalization ability.
5) Analysis of Performance: In order to investigate the convergence and stability of EDA-RL, we present the convergence curves for EDA, EDA-R, and EDA-RL for four 10-dimension problems in Fig. 10. The figures show that EDARL requires fewer evaluations to reach a steady state than the other strategies. As with the previous comparison results, EDA-RL obtains better objective function values than EDA and EDA-R.

## V. CONCLUSION

This article has studied a control parameter optimization problem in the steelmaking process. Based on historical data,

TABLE XV
Comparison Results Between EDA-RL and State-of-the-Art Algorithms on 30-D Benchmark Problems

| $30-D$ | IDE <br> Mean/std. | CLPSO <br> Mean/std. |  | 1POP-CMA-ES <br> Mean/std. |  | SaDE <br> Mean/std. |  | EDA-RL <br> Mean/std. |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Fun1 | $\begin{aligned} & 3.17 \mathrm{E}+02 \\ & \pm 6.01 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.87 \mathrm{E}+02 \\ & \pm 2.78 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.55 \mathrm{E}+02 \\ & \pm 5.03 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 3.26 \mathrm{E}+02 \\ & \pm 8.06 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.52 \mathrm{E}+02 \\ & \pm 6.04 \mathrm{E}+01 \end{aligned}$ |
| Fun2 | $\begin{aligned} & 1.21 \mathrm{E}+02 \\ & \pm 4.39 \mathrm{E}+00 \end{aligned}$ | $+$ | $\begin{aligned} & 1.43 \mathrm{E}+02 \\ & \pm 2.69 \mathrm{E}+01 \end{aligned}$ | $+$ | $\begin{aligned} & 5.02 \mathrm{E}+02 \\ & \pm 3.09 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 1.14 \mathrm{E}+02 \\ & \pm 1.42 \mathrm{E}+01 \end{aligned}$ | $+$ | $\begin{aligned} & 2.01 \mathrm{E}+02 \\ & \pm 6.06 \mathrm{E}+01 \end{aligned}$ |
| Fun3 | $\begin{aligned} & 3.28 \mathrm{E}+03 \\ & \pm 3.80 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 5.44 \mathrm{E}+03 \\ & \pm 4.14 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 5.76 \mathrm{E}+02 \\ & \pm 3.50 \mathrm{E}+02 \end{aligned}$ | $+$ | $\begin{aligned} & 5.03 \mathrm{E}+03 \\ & \pm 9.93 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 2.55 \mathrm{E}+03 \\ & \pm 8.10 \mathrm{E}+02 \end{aligned}$ |
| Fun4 | $\begin{aligned} & 2.00 \mathrm{E}+02 \\ & \pm 3.60 \mathrm{E}-01 \end{aligned}$ | $+$ | $\begin{aligned} & 2.72 \mathrm{E}+02 \\ & \pm 6.57 \mathrm{E}+00 \end{aligned}$ | - | $\begin{aligned} & 2.86 \mathrm{E}+02 \\ & \pm 3.02 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.26 \mathrm{E}+02 \\ & \pm 7.25 \mathrm{E}+00 \end{aligned}$ | - | $\begin{aligned} & 2.10 \mathrm{E}+02 \\ & \pm 4.47 \mathrm{E}+00 \end{aligned}$ |
| Fun5 | $\begin{aligned} & 2.14 \mathrm{E}+02 \\ & \pm 2.09 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.96 \mathrm{E}+02 \\ & \pm 5.43 \mathrm{E}+00 \end{aligned}$ | - | $\begin{aligned} & 2.87 \mathrm{E}+02 \\ & \pm 2.85 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.66 \mathrm{E}+02 \\ & \pm 1.23 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.10 \mathrm{E}+02 \\ & \pm 1.65 \mathrm{E}+01 \end{aligned}$ |
| Fun6 | $\begin{aligned} & 2.00 \mathrm{E}+02 \\ & \pm 6.39 \mathrm{E}-03 \end{aligned}$ | $=$ | $\begin{aligned} & 2.02 \mathrm{E}+02 \\ & \pm 6.19 \mathrm{E}-01 \end{aligned}$ | - | $\begin{aligned} & 3.15 \mathrm{E}+02 \\ & \pm 8.14 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.00 \mathrm{E}+02 \\ & \pm 8.77 \mathrm{E}-03 \end{aligned}$ | - | $\begin{aligned} & 2.00 \mathrm{E}+02 \\ & \pm 1.79 \mathrm{E}-04 \end{aligned}$ |
| Fun7 | $\begin{aligned} & 3.06 \mathrm{E}+02 \\ & \pm 5.37 \mathrm{E}+00 \end{aligned}$ | $+$ | $\begin{aligned} & 7.77 \mathrm{E}+02 \\ & \pm 3.14 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 1.14 \mathrm{E}+03 \\ & \pm 2.90 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 6.18 \mathrm{E}+02 \\ & \pm 7.16 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 3.91 \mathrm{E}+02 \\ & \pm 4.79 \mathrm{E}+01 \end{aligned}$ |
| Fun8 | $\begin{aligned} & 3.00 \mathrm{E}+02 \\ & \pm 0.00 \mathrm{E}+00 \end{aligned}$ | $=$ | $\begin{aligned} & 3.00 \mathrm{E}+02 \\ & \pm 3.10 \mathrm{E}-05 \end{aligned}$ | $=$ | $\begin{aligned} & 3.00 \mathrm{E}+02 \\ & \pm 0.00 \mathrm{E}+00 \end{aligned}$ | $=$ | $\begin{aligned} & 3.00 \mathrm{E}+02 \\ & \pm 0.00 \mathrm{E}+00 \end{aligned}$ | $=$ | $\begin{aligned} & 2.88 \mathrm{E}+02 \\ & \pm 4.75 \mathrm{E}+01 \end{aligned}$ |
| No. of Best | 3 |  | 0 |  | 1 |  | 2 |  | 4 |
| - |  | 3 |  | 6 |  | 5 |  | 6 |  |
| $=$ |  | 2 |  | 1 |  | 2 |  | 1 |  |
| $+$ |  | 3 |  | 1 |  | 1 |  | 1 |  |

TABLE XVI
Comparison Results Between EDA-RL and State-of-the-Art Algorithms on 50-D Benchmark Problems

| $50-D$ | IDE <br> Mean/std. | CLPSO <br> Mean/std. |  | 1POP-CMA-ES <br> Mean/std. |  | SaDE <br> Mean/std. |  | EDA-RL <br> Mean/std. |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Fun1 | $\begin{aligned} & 7.32 \mathrm{E}+03 \\ & \pm 3.82 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 5.31 \mathrm{E}+02 \\ & \pm 2.39 \mathrm{e}+02 \end{aligned}$ | $=$ | $\begin{aligned} & 5.17 \mathrm{E}+02 \\ & \pm 4.08 \mathrm{E}+02 \end{aligned}$ | $=$ | $\begin{aligned} & 9.18 \mathrm{E}+02 \\ & \pm 2.96 \mathrm{E}+02 \end{aligned}$ | $-$ | $\begin{aligned} & 4.97 \mathrm{E}+02 \\ & \pm 4.14 \mathrm{E}+02 \end{aligned}$ |
| Fun2 | $\begin{aligned} & 6.88 \mathrm{E}+01 \\ & \pm 2.03 \mathrm{E}+01 \end{aligned}$ | $+$ | $\begin{aligned} & 3.68 \mathrm{E}+02 \\ & \pm 1.58 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 1.83 \mathrm{E}+03 \\ & \pm 2.86 \mathrm{E}+03 \end{aligned}$ | - | $\begin{aligned} & 2.21 \mathrm{E}+01 \\ & \pm 4.87 \mathrm{E}+00 \end{aligned}$ | $+$ | $\begin{aligned} & 2.87 \mathrm{E}+02 \\ & \pm 1.50 \mathrm{E}+02 \end{aligned}$ |
| Fun3 | $\begin{aligned} & 7.32 \mathrm{E}+03 \\ & \pm 6.92 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 1.21 \mathrm{E}+04 \\ & \pm 6.60 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 2.99 \mathrm{E}+03 \\ & \pm 4.19 \mathrm{E}+03 \end{aligned}$ | $+$ | $\begin{aligned} & 8.75 \mathrm{E}+03 \\ & \pm 2.15 \mathrm{E}+03 \end{aligned}$ | - | $\begin{aligned} & 6.41 \mathrm{E}+03 \\ & \pm 6.96 \mathrm{E}+02 \end{aligned}$ |
| Fun4 | $\begin{aligned} & 2.02 \mathrm{E}+02 \\ & \pm 1.14 \mathrm{E}+00 \end{aligned}$ | $+$ | $\begin{aligned} & 3.51 \mathrm{E}+02 \\ & \pm 7.23 \mathrm{E}+00 \end{aligned}$ | - | $\begin{aligned} & 3.75 \mathrm{E}+02 \\ & \pm 3.34 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.78 \mathrm{E}+02 \\ & \pm 9.38 \mathrm{E}+00 \end{aligned}$ | - | $\begin{aligned} & 2.20 \mathrm{E}+02 \\ & \pm 6.67 \mathrm{E}+00 \end{aligned}$ |
| Fun5 | $\begin{aligned} & 3.03 \mathrm{E}+02 \\ & \pm 1.09 \mathrm{E}+01 \end{aligned}$ | $=$ | $\begin{aligned} & 3.92 \mathrm{E}+02 \\ & \pm 6.74 \mathrm{E}+00 \end{aligned}$ | - | $\begin{aligned} & 3.74 \mathrm{E}+02 \\ & \pm 3.35 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 3.44 \mathrm{E}+02 \\ & \pm 1.13 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 3.02 \mathrm{E}+02 \\ & \pm 7.99 \mathrm{E}+00 \end{aligned}$ |
| Fun6 | $\begin{aligned} & 2.23 \mathrm{E}+02 \\ & \pm 4.46 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.06 \mathrm{E}+02 \\ & \pm 9.17 \mathrm{E}-01 \end{aligned}$ | - | $\begin{aligned} & 3.82 \mathrm{E}+02 \\ & \pm 1.29 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 2.61 \mathrm{E}+02 \\ & \pm 8.73 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 2.00 \mathrm{E}+02 \\ & \pm 2.66 \mathrm{E}-05 \end{aligned}$ |
| Fun7 | $\begin{aligned} & 3.58 \mathrm{E}+02 \\ & \pm 3.30 \mathrm{E}+01 \end{aligned}$ | $+$ | $\begin{aligned} & 1.50 \mathrm{E}+03 \\ & \pm 5.59 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 1.94 \mathrm{E}+03 \\ & \pm 4.55 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 1.17 \mathrm{E}+03 \\ & \pm 9.89 \mathrm{E}+01 \end{aligned}$ | - | $\begin{aligned} & 5.47 \mathrm{E}+02 \\ & \pm 1.14 \mathrm{E}+02 \end{aligned}$ |
| Fun8 | $\begin{aligned} & 4.00 \mathrm{E}+02 \\ & \pm 0.00 \mathrm{E}+00 \end{aligned}$ | $=$ | $\begin{aligned} & 4.00 \mathrm{E}+02 \\ & \pm 1.63 \mathrm{E}-02 \end{aligned}$ | - | $\begin{aligned} & 1.03 \mathrm{E}+03 \\ & \pm 1.22 \mathrm{E}+03 \end{aligned}$ | - | $\begin{aligned} & 5.35 \mathrm{E}+02 \\ & \pm 6.75 \mathrm{E}+02 \end{aligned}$ | - | $\begin{aligned} & 4.00 \mathrm{E}+02 \\ & \pm 0.00 \mathrm{E}+00 \end{aligned}$ |
| No. of Best | 3 |  | 1 |  | 1 |  | 1 |  | 4 |
| - |  | 3 |  | 7 |  | 6 |  | 7 |  |
| $=$ |  | 2 |  | 1 |  | 1 |  | 0 |  |
| $+$ |  | 3 |  | 0 |  | 1 |  | 1 |  |

a black-box model was built to describe the end-point control operation of the steelmaking process. This model was then used to formulate an optimization problem to set the control parameters for the required temperature and molten steel quality. To solve the problem, a new framework based on EDA with a resampling strategy and a local improvement (EDA-RL) was developed. In the EDA, we designed a hybrid distribution model to strengthen the diversity of the population. A resampling strategy was proposed to enlarge the sampling region and to guide the new population to a more promising area. This new sampling model with resampling has good exploration ability. To enhance its exploitation ability, we incorporated local improvement, based on simplified
gravitational search and information learning, to identify the current best individual. The EDA-RL was tested on practical operation data. The results illustrate that our proposed approach can optimize the control parameters of the steelmaking process to obtain the specified output accurately. To further test the performance of EDA-RL as a general optimization algorithm, an experiment was conducted on some complex black-box optimization benchmark problems. The results indicate that EDA-RL outperforms other state-of-the-art algorithms across a wide range of problems.

In process industries, there are problems that involve optimizing the dynamic processes of operations instead of the final outputs. These problems can be considered as dynamic

operation optimization problems. In further research, we will apply our proposed algorithm to solve dynamic operation optimization problems in practice.

## REFERENCES

[1] J. L. Ding, H. Modares, T. Y. Chai, and F. L. Lewis, "Databased multiobjective plant-wide performance optimization of industrial processes under dynamic environments," IEEE Trans. Ind. Informat., vol. 12, no. 2, pp. 454-465, Apr. 2016.
[2] Y. Zhang, Y. Yang, S. X. Ding, and L. Li, "Data-driven design and optimization of feedback control systems for industrial applications," IEEE Trans. Ind. Electron., vol. 61, no. 11, pp. 6409-6417, Nov. 2014.
[3] R. H. Chi, Z. S. Hou, S. T. Jin, and B. Huang, "An improved data-driven point-to-point ILC using additional on-line control inputs with experimental verification," IEEE Trans. Syst., Man, Cybern., Syst., vol. 49, no. 4, pp. 687-696, Apr. 2019.
[4] T.-H. S. Li, M.-C. Kao, and P.-H. Kuo, "Recognition system for home-service-related sign language using entropy-based $k$-means algorithm and ABC-based HMM," IEEE Trans. Syst., Man, Cybern., Syst., vol. 46, no. 1, pp. 150-162, Jan. 2016.
[5] X. Qin, S. Lysecky, and J. Sprinkle, "A data-driven linear approximation of HVAC utilization for predictive control and optimization," IEEE Trans. Control Syst. Technol., vol. 23, no. 2, pp. 778-786, Mar. 2015.
[6] H.-X. Tian and Z.-Z. Mao, "An ensemble ELM based on modified AdaBoost.RT algorithm for predicting the temperature of molten steel in ladle furnace," IEEE Trans. Autom. Sci. Eng., vol. 7, no. 1, pp. 73-80, Jan. 2010.
[7] L.-F. Xu, W. Li, M. Zhang, S.-X. Xu, and J. Li, "A model of basic oxygen furnace (BOF) end-point prediction based on spectrum information of the furnace flame with support vector machine (SVM)," Optik, vol. 122, no. 7, pp. 594-598, Apr. 2011.
[8] H. Liu, B. Wang, and X. Xiong, "Basic oxygen furnace steelmaking end-point prediction based on computer vision and general regression neural network," Optik, vol. 125, no. 18, pp. 5241-5248, Sep. 2014.
[9] Y. Shao, Q. Zhao, Y. R. Chen, Q. B. Zhang, and K. Wang, "Applying flame spectral analysis and multi-class classification algorithm on the BOS endpoint carbon content prediction," Optik, vol. 126, no. 23, pp. 4539-4543, Dec. 2015.
[10] F. He and L. Y. Zhang, "Prediction model of end-point phosphorus content in BOF steelmaking process based on PCA and BP neural network," J. Process Control, vol. 66, pp. 51-58, Jun. 2018.
[11] W. Birk, I. Arvanitidis, P. G. Jonsson, and A. Medvedev, "Physical modeling and control of dynamic foaming in an LD-converter process," IEEE Trans. Ind. Appl., vol. 37, no. 4, pp. 1067-1073, Jul/Aug. 2001.
[12] C. Liu, X. Song, T. Xu, and L. Tang, "An operation optimization method based on improved EDA for BOF end-point control," in Proc. IEEE World Congr. Comput. Intell. (WCCI), Vancouver, BC, Canada, Jul. 2016, pp. 1077-1084.
[13] B. Brunaud, I. E. Grossmann, "Perspectives in multilevel decisionmaking in the process industry," Front. Eng. Manag., vol. 4, no. 3, pp. 256-270, Jul. 2017.
[14] S. L. Jiang, M. Liu, and J. H. Hao, "A two-phase soft optimization method for the uncertain scheduling problem in the steelmaking industry," IEEE Trans. Syst., Man, Cybern., Syst., vol. 47, no. 3, pp. 416-431, Mar. 2017.
[15] S. P. Yu, T. Y. Chai, and Y. Tang, "An effective heuristic rescheduling method for steelmaking and continuous casting production process with multirefining modes," IEEE Trans. Syst., Man, Cybern., Syst., vol. 46, no. 12, pp. 1675-1688, Dec. 2016.
[16] H. Stafford and G. Leitmann, "On representing a black box as a dynamical system," J. Math. Anal. Appl., vol. 38, no. 2, pp. 348-364, May 1972.
[17] C. Liu, L. X. Tang, J. Y. Liu, and Z. H. Tang, "A dynamic analytics method based on multistage modeling for a BOF steelmaking process," IEEE Trans. Autom. Sci. Eng., vol. 16, no. 3, pp. 1097-1109, Jul. 2019.
[18] C. L. P. Chen and Z. L. Liu, "Broad learning system: An effective and efficient incremental learning system without the need for deep architecture," IEEE Trans. Neural Netw. Learn. Syst., vol. 29, no. 1, pp. 10-24, Jan. 2018.
[19] C. L. P. Chen, "A rapid supervised learning neural network for function interpolation and approximation," IEEE Trans. Neural Netw., vol. 7, no. 5, pp. 1220-1230, Sep. 1996.
[20] C. Liu, L. X. Tang, and J. Y. Liu, "Least squares support vector machine with self-organizing multiple kernel learning and sparsity," Neurocomputing, vol. 331, pp. 493-504, Feb. 2019.
[21] A. Žilinskas and J. Calvin, "Bi-objective decision making in global optimization based on statistical models," J. Glob. Optim., vol. 74, pp. 599-609, Feb. 2018.
[22] L. X. Tang, Y. Dong, and J. Y. Liu, "Differential evolution with an individual-dependent mechanism," IEEE Trans. Evol. Comput., vol. 19, no. 4, pp. 560-574, Aug. 2015.
[23] W. Ewert, R. J. Marks, B. B. Thompson, and A. Yu, "Evolutionary inversion of swarm emergence using disjunctive combs control," IEEE Trans. Syst., Man, Cybern., Syst., vol. 43, no. 5, pp. 1063-1076, Sep. 2013.
[24] A. Che, P. Wu, F. Chu, and M. C. Zhou, "Improved quantuminspired evolutionary algorithm for large-size lane reservation," IEEE Trans. Syst., Man, Cybern., Syst., vol. 45, no. 12, pp. 1535-1548, Dec. 2015.
[25] X. P. Wang, Z. M. Dong, and L. X. Tang, "Multiobjective differential evolution with personal archive and biased self-adaptive mutation selection," IEEE Trans. Syst., Man, Cybern., Syst., to be published, doi: $10.1109 / \mathrm{TSMC} .2018 .2873043$.
[26] D. W. Gong, B. Xu, Y. Zhang, Y. N. Guo, and S. X. Yang, "A similaritybased cooperative co-evolutionary algorithm for dynamic interval multiobjective optimization problems," IEEE Trans. Evol. Comput., to be published, doi: $10.1109 / \mathrm{TEVC} .2019 .2912204$.
[27] D. W. Gong, J. Sun, and Z. Miao, "A set-based genetic algorithm for interval many-objective optimization problems," IEEE Trans. Evol. Comput., vol. 22, no. 1, pp. 47-60, Feb. 2018.
[28] D. W. Gong, Y. P. Liu, and G. G. Yen, "A meta-objective approach for many-objective evolutionary optimization," Evol. Comput., to be published, doi: $10.1162 /$ evcc_s_00243.
[29] D. W. Gong, J. Sun, and X. F. Ji, "Evolutionary algorithms with preference polyhedron for interval multi-objective optimization problems," Inf. Sci., vol. 233, pp. 141-161, Jan. 2013.
[30] C. Echegoyen, A. Mendiburu, R. Santana, and J. A. Lozano, "Toward understanding EDAs based on Bayesian networks through a quantitative analysis," IEEE Trans. Evol. Comput., vol. 16, no. 2, pp. 173-189, Apr. 2012.
[31] A. Zhou, Q. Zhang, and Y. Jin, "Approximating the set of Pareto-optimal solutions in both the decision and objective spaces by an estimation of distribution algorithm," IEEE Trans. Evol. Comput., vol. 13, no. 5, pp. 1167-1189, Oct. 2009.
[32] Q. Yang, W.-N. Chen, Y. Li, C. L. P. Chen, X.-M. Xu, and J. Zhang, "Multimodal estimation of distribution algorithms," IEEE Trans. Cybern., vol. 47, no. 3, pp. 636-650, Mar. 2017.
[33] P. Yang, K. Tang, and X. Lu, "Improving estimation of distribution algorithm on multimodal problems by detecting promising areas," IEEE Trans. Cybern., vol. 45, no. 8, pp. 1438-1449, Aug. 2015.
[34] V. A. Shim, K. C. Tan, C. Y. Cheong, and J. Y. Chia, "Enhancing the scalability of multi-objective optimization via restricted Boltzmann machine-based estimation of distribution algorithm," Inf. Sci., vol. 248, pp. 191-213, Nov. 2013.
[35] W. Dong, T. Chen, P. Tiño, and X. Yao, "Scaling up estimation of distribution algorithms for continuous optimization," IEEE Trans. Evol. Comput., vol. 17, no. 6, pp. 797-822, Dec. 2013.
[36] A. Kabán, J. Bootkrajang, and R. J. Durrant, "Towards large scale continuous EDA: A random matrix theory perspective," in Proc. Genet. Evol. Comput. (GECCO), Jul. 2013, pp. 383-390.
[37] M. L. Sanyang, R. J. Durrant, A. Kabán, "How effective is CauchyEDA in high dimensions?" in Proc. IEEE World Congr. Comput. Intell., Vancouver, BC, Canada, Jul. 2016, pp. 3409-3416.
[38] X. Yao and Y. Liu, "Fast evolution strategies," in International Conference on Evolutionary Programming. Berlin, Germany: Springer, 1997, pp. 151-161.
[39] P. Pošík, "Comparison of cauchy EDA and BIPOP-CMA-ES algorithms on the BBOB noiseless testbed," in Proc. Genet. Evol. Comput. (GECCO), Jul. 2010, pp. 1697-1702.
[40] J. Zhong, J. Zhang, and Z. Fan, "MP-EDA: A robust estimation of distribution algorithm with multiple probabilistic models for global continuous optimization," in Asia-Pacific Conference on Simulated Evolution and Learning. Berlin, Germany: Springer, 2010, pp. 85-94.
[41] A. Zhou, J. Sun, and Q. Zhang, "An estimation of distribution algorithm with cheap and expensive local search methods," IEEE Trans. Evol. Comput., vol. 19, no. 6, pp. 807-822, Dec. 2015.

[42] J. Sun, Q. Zhang, and E. P. K. Tsang, "DE/EDA: A new evolutionary algorithm for global optimization," Inf. Sci., vol. 169, nos. 3-4, pp. 249-262, Feb. 2005.
[43] C. W. Ahn, J. An, and J.-C. Yoo, "Estimation of particle swarm distribution algorithms: Combining the benefits of PSO and EDAs," Inf. Sci., vol. 192, pp. 109-119, Jun. 2012.
[44] J. A. K. Suykens and J. Vandewalle, "Least squares support vector machine classifiers," Neural Process. Lett., vol. 9, no. 3, pp. 293-300, Jun. 1999.
[45] R. Storn and K. V. Price, "Differential evolution: A simple and efficient adaptive scheme for global optimization over continuous spaces," Int. Comput. Sci. Inst., Berkeley, CA, USA, Rep. TR-95-012, 1995.
[46] H. M'uhlenbein and G. Paaß, "From recombination of genes to the estimation of distributions. I. Binary parameters," in Proc. Int. Conf. Parallel Problem Solving Nat. Sep. 1996, pp. 178-187.
[47] P. Larrañaga and J. Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Norwell, MA, USA: Kluwer, 2001.
[48] E. Rashedi, H. Nezamabadi-Pour, and S. Saryazdi, "GSA: A gravitational search algorithm," Inf. Sci., vol. 179, no. 13, pp. 2232-2248, Jun. 2009.
[49] J. J. Liang, B. Y. Qu, P. N. Suganthan, and A. G. Hernández-Díaz, "Problem definitions and evaluation criteria for the CEC 2013 special session on real-parameter optimization," Comput. Intell. Lab., Zhengzhou Univ., Zhengzhou, China, and Nanyang Technol. Univ., Singapore, Rep. 201212, Jan. 2013. [Online]. Available: http://www.ntu.edu.sg/home/ epnsugan/
[50] J. J. Liang, A. K. Qin, P. N. Suganthan, and S. Baskar, "Comprehensive learning particle swarm optimizer for global optimization of multimodal functions," IEEE Trans. Evol. Comput., vol. 10, no. 3, pp. 281-295, Jun. 2006.
[51] A. K. Qin, V. L. Huang, and P. N. Suganthan, "Differential evolution algorithm with strategy adaptation for global numerical optimization," IEEE Trans. Evol. Comput., vol. 13, no. 2, pp. 398-417, Apr. 2009.
[52] I. Loshchilov, "CMA-ES with restarts for solving CEC 2013 benchmark problems," in Proc. IEEE Congr. Evol. Comput. (CEC), Cancún, Mexico, Jun. 2013, pp. 369-376.
![img-10.jpeg](img-10.jpeg)

Lixin Tang (Senior Member, IEEE) received the B.E. degree in industrial automation, the M.E. degree in systems engineering, and the Ph.D. degree in control theory and application from Northeastern University, Shenyang, China, in 1988, 1991, and 1996, respectively.

He is currently a fellow of Chinese Academy of Engineering, a Chair Professor of the Institute of Industrial and Systems Engineering, Northeastern University; the Director of Key Laboratory of Data Analytics and Optimization for Smart Industry (Northeastern University). Ministry of Education, China; and the Head of Centre for Artificial Intelligence and Data Science. He has published papers in journals, such as Operations Research, IIE Transactions, Naval Research Logistics, the European Journal of Operational Research, the IEEE Transactions on Evolutionary Computation, IEEE Transactions on Power Systems, and IEEE Transactions on Control, Systems Technology. His research interests include industrial big data science, data analytics and machine learning, reinforcement learning and dynamic optimization, computational intelligent optimization, plant-wide production and logistics planning, production and logistics batching and scheduling and engineering applications in manufacturing (steel, petroleumchemical, nonferrous), energy, resources industry, and logistics systems.

Dr. Tang serves as an Associate Editor for IISE Transactions, the IEEE Transactions on Evolutionary Computation, IEEE Transactions on Cybernetics, Journal of Scheduling, International Journal of Production Research, and Journal of the Operational Research Society, in editorial board for the Annals of Operations Research, and an Area Editor for the Asia-Pacific Journal of Operational Research.
![img-11.jpeg](img-11.jpeg)

Chang Liu is currently pursuing the Ph.D. degree in systems engineering with the Institute of Industrial and Systems Engineering, Northeastern University, Shenyang, China.
He has published several papers in journals, such as the IEEE Transactions on Automation SCIENCE AND ENGINEERING and Neurocomputing. His research interests include data analytics and optimization for smart industry, model predictive control, machine learning, computational intelligent optimization, and engineering applications in various industrial processes.
![img-12.jpeg](img-12.jpeg)

Jiyin Liu received the B.E. degree in industrial automation and the M.E. degree in systems engineering from Northeastern University, Shenyang, China, in 1982 and 1985, respectively, and the Ph.D. degree in manufacturing engineering and operations management from the University of Nottingham, Nottingham, U.K., in 1993.
He is currently a Professor of Operations Management with the School of Business and Economics, Loughborough University, Leicestershire, U.K. He is also a Cheung Kong Scholars Visiting Chair Professor with the Institute of Industrial and Systems Engineering, Northeastern University. He has published papers in journals, such as the European Journal of Operational Research, the IEEE Transactions, IIE Transactions, International Journal of Production Research, Naval Research Logistics, Operations Research, and Transportation Research. His research interests include operations planning and scheduling problems in production, logistics and supply chains, and mathematical modeling, optimization, and heuristic methods.
![img-13.jpeg](img-13.jpeg)

Xianpeng Wang (Member, IEEE) received the B.S. degree in materials and control engineering from Shenyang University, Shenyang, China, in 2002, and the Ph.D. degree in systems engineering from Northeastern University, Shenyang, in 2007.
He is currently a Professor with the Liaoning Engineering Laboratory of Data Analytics and Optimization for Smart Industry, and the State Key Laboratory of Synthetical Automation for Process Industries, Northeastern University. He has published more than 20 papers in international journals, such as the IEEE Transactions on Evolutionary Computation, IEEE Transactions on Control, Systems Technology, European Journal of Operational Research, Applied Soft Computing, Computers and Operations Research, IEEE Transactions on Automation Science and Engineering, Information Sciences, and Journal of the Operational Research Society. His research interests include multiobjective optimization, machine learning, production scheduling, modeling and optimization in process industries based on data analytics, decision support systems, and process operation optimization.