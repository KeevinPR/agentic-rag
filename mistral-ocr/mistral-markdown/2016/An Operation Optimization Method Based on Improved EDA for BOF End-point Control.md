# An Operation Optimization Method Based on Improved EDA for BOF End-point Control 

Chang Liu<br>Institute of Industrial Engineering\& Logistics Optimization<br>Northeastern University<br>Shenyang, China<br>lc1987328@126.com

Te Xu<br>Institute of Industrial Engineering\& Logistics Optimization<br>Northeastern University<br>Shenyang, China<br>xute@ise.neu.edu.cn


#### Abstract

Due to the large amounts of energy consumption in the converter steelmaking production process, the furnace state generates a fierce chemical reaction, and accompanies with high temperature. In this paper, in order to accurately control and optimize the converter steelmaking production process, and guarantee the quality of products, the data analytics method based on least square support vector machine (LSSVM) is used to establish the operation optimization model of converter steelmaking. Meanwhile, a kind of operation optimization method based on improved estimation of distribution algorithm (IEDA) is proposed, and Gaussian model is selected as the probabilistic model. In order to increase the diversity of population, the variable scale variance strategy is developed. In addition, aiming at the local search ability, the mutation mechanism of modified differential evolution algorithm is adopted in the search process. The experimental results illustrate that the proposed method can effectively solve the end-point control problems of temperature and carbon content in BOF steelmaking process.


Keywords-BOF end-point control; operation optimization; data analytics; UMDAc; differential evolution

## I. INTRODUCTION

In the present industrial production, especially the iron and steel smelting industry [1]-[3], the product quality and production often need some safe restrictions. In order to meet these indicators, internal structure models should be established more accurately. However, due to a large number of complex physical and chemical reactions in smelting process, it is difficult to identify mechanism models. Hence, to guide control operation in the reaction process preferably, so as to reduce the cost, and improve the quality of molten steel, the operation optimization problem is worth studying on the steel smelting production process.

Operation optimization aims at maximum production efficiency index or minimum energy consumption. In general, optimal operation setting parameters are obtained by the

Xiangman Song<br>Institute of Industrial Engineering\& Logistics Optimization<br>Northeastern University<br>Shenyang, China<br>xmsong@tli.neu.edu.cn<br>Lixin Tang<br>Institute of Industrial Engineering\& Logistics Optimization<br>Northeastern University<br>Shenyang, China<br>1xtang@tli.neu.edu.cn

intelligent optimization algorithms [4]-[5]. Operation optimization is an optimization problem based on mathematic models. Fig. 1 shows the relationship of operation optimization between control profile and expected output objective. $H_{p}$ is the operation interval range. Simultaneously, $y(k)$ can be regarded as the output value of actual profile $y(t)$ at the $k t h$ time point. We can attain the target setting profile $s(t)$ by adjusting the control parameters $u(t)$, then the estimated profile $\hat{y}(t \mid k)$ can approach to the expected output profile $r(t \mid k)$.

Basic oxygen furnace (BOF) is a key link of steel-making production, the main purpose of converter steel-making is to smelt molten steel (mainly refers to carbon content), which are conformed to the requirements of production. For the high temperature of converter steelmaking, and the quality information of furnace state cannot be detected continuously, it is difficult to establish mechanism model [6]-[7]. However, according to obtained actual data, analytical model can be established in the production process.

In the previous, many researchers focus on predicting the end-point carbon content and the end-point temperature of BOF steelmaking process. Sriram [8] develops the model based on adaptive neural fuzzy inference system (ANFIS), which has a more accurate prediction in contrast to those from BPNN model. Valyon [9] proposes a sparse robust model based on LSSVM for Linz-Donawitz converter, the used approach reduces the size of model, and strengthens noise immunity. Han [10] puts forward an input weighted support vector machine modeling method, and input variables selection technique is added to the proposed method, experimental results show that the prediction model is essential and effective. A novel RBF neural network is built to predict endpoint temperature and carbon content by Zhang [11], and a robust clustering method is used for data dispersion level, simulations indicate that the accuracy of endpoint prediction is improved.

On the basis of stable analytical model, optimized operation parameters can help the operators control better. To efficiently solve the operation optimization problem in the hotrolling production process, a hybrid self-adaptive genetic algorithm (HSaGA) is presented by Chen [12], computational results show that the proposed HSaGA can obtain better results than the empirical method. In addition, robust dynamic operation optimization is also applied to hot rolling production process by Chen [13]. Computational results show that the proposed RDOOP model and dynamic programming can enhance the level of shape control. In the [14], a dynamic control model based on adaptive network fuzzy inference system (ANFIS) and robust relevance vector machine (RRVM) is proposed for BOF steelmaking process. Simulations show that the proposed dynamic control model has good results on the oxygen and coolant calculation. In the [15], a combination model is proposed based on the reasoning and SVM for solving the control problems. Simulation results demonstrate that the proposed model is an effective way for solving the complex industrial problems.

According to the actual production data in process of converter steelmaking, this paper uses data analytics method based on LSSVM to establish operation optimization model, and RBF is selected as the kernel function of LSSVM. The parameters of operation optimization model are optimized by proposed operation optimization algorithm based on IEDA, which is regarded as univariate marginal distribution algorithm for continuous domains (UMDA ${ }_{\mathrm{C}}$ ) with the Gaussian probabilistic model. In order to increase the diversity of population, the variable scale variance strategy is developed in the whole search process. At the same time, for the sake of strengthening local search ability, IEDA absorbs some advantages from the mutation mechanism of modified differential evolution algorithm.

The rest of the paper is organized as follows. In Section II, the production process of BOF steelmaking is briefly described. Section III introduces data analytics method and operation optimization method based on improved EDA, respectively. In order to demonstrate the effectiveness of proposed algorithm, experimental analysis based on industrial actual data has been accomplished in Section IV. Finally, conclusions of the work and future work are presented in Section V.

## II. DESCRIPTION OF BOF STEELMAKING PROCESS

Basic oxygen steelmaking is a process which blows oxygen into hot metal for reducing carbon content, manganese, sulfur, phosphorus, etc. The reaction is an oxidation process for producing the molten steel. The molten iron can be transformed into the molten steel.

Converter steelmaking is a batch process, as is shown in Fig. 2. Main raw materials are the molten iron and the scrap steel. In BOF production process, scrap steel is put into the converter at first, and then molten iron is added. The height is lower than the height of top when oxygen lance begins blowing oxygen. Oxygen can rapidly begin reacting when oxygen flow is put into molten pool. Due to the oxidation reaction, and the content of $\mathrm{C}, \mathrm{Si}, \mathrm{Mn}, \mathrm{P}$ and S can reduce or remove continuously in the hot metal.
![img-0.jpeg](img-0.jpeg)

Fig. 1. The operation optimization sketch.
![img-1.jpeg](img-1.jpeg)

Fig. 2. The reaction process of BOF steelmaking.

## III. OPERATION Optimization Method

For the complex steelmaking process, LSSVM-based data analytics method is adopted for establishing the operation optimization model. In order to solve the model, an improved EDA with Gaussian probabilistic model is proposed. Taking the diversity of population into account, a variable scale variance strategy is added to IEDA in the whole evolution process. In addition, in order to strength the exploitation capability, a mutation idea based on DE is used as the local search.

## A. Data Analytics Method

Converter steelmaking is a complex industrial process, taking the lack of exact mechanism (physical-chemical) model into account, then, black-box model based on actual data is required. LSSVM can be regarded as a black-box model based on the input-output information. The history data can be used to establish the analytical model, which can completely identify the unknown internal model. On the basis of training models, expected objective values can be acquired by testing data.

LSSVM is an improved standard support vector machine (SVM) [16], which was developed by Suykens [17]. The most important distinction between SVM and LSSVM is that LSSVM uses a set of linear equations for solving, while the sub-problem of SVM is regarded as a quadratic programming.

In LSSVM, nonlinear estimation function can be transformed into the linear estimation function with high dimensional feature space as formula (1):

$$
f\left(\mathbf{x}_{i}\right)=\mathbf{w}^{T} \mathbf{x}_{i}+b, \quad i=1,2, \ldots, N
$$

where $\mathbf{x}_{i}$ is the $i$ th sample, given a sample of $N$ data points, $f\left(\mathbf{x}_{i}\right)$ is the output target, $\mathbf{w}$ is the regression coefficient, $b$ is the bias.

According to the structural risk minimization principle, the primal problem of LSSVM can be formulated as follows:

$$
\begin{gathered}
\min J\left(\mathbf{w}, \xi_{i}\right)=\frac{1}{2}\|\mathbf{w}\|^{2}+\gamma \sum_{i=1}^{N} \xi_{i} \\
\text { s.t. } y_{i}=\mathbf{w}^{T} \varphi\left(\mathbf{x}_{i}\right)+b+\xi_{i} \\
\gamma \geq 0
\end{gathered}
$$

In (2), $\gamma$ is the penalty coefficient, $\xi_{i}$ is the slack variable, $\mathbf{x}_{i}$ can be mapped to a high-dimensional feature space by $\varphi\left(\mathbf{x}_{i}\right)$. Matching Larranage function can be calculated by:

$$
L\left(\mathbf{w}, b, \xi_{i}, \alpha_{i}\right)=J\left(\mathbf{w}, \xi_{i}\right)-\sum_{i=1}^{N} \alpha_{i}\left\{y_{i}\left[\mathbf{w}^{T} \varphi\left(\mathbf{x}_{i}\right)+b\right]-1+\xi_{i}\right\}
$$

where $\alpha_{i}$ is the Larranage multiplier. Then its solution can be found by linear equations. Finally, the regression function of LSSVM is obtained by:

$$
f\left(\mathbf{x}_{i}\right)=\sum_{i=1}^{N} \alpha_{i} K\left(\mathbf{x}, \mathbf{x}_{i}\right)+b
$$

where the kernel function can be given by:

$$
K\left(\mathbf{x}_{i}, \mathbf{x}\right)=\exp \left(-\frac{\left\|\mathbf{x}_{i}-\mathbf{x}\right\|^{2}}{\sigma^{2}}\right), \sigma^{2}>0
$$

## B. $\quad U M D A_{C}$

EDAs [18]-[19] belong to the field of evolution computation. In continuous EDAs, the crossover and mutation operation of traditional GA [20] are not used for EDAs, instead, which generate new sample individuals by updated probabilistic model in each generation. Modeling distribution of promising solutions can be extracted from global statistic information of population. New individuals can be sampled by the probabilistic model. Hence, EDAs have been applied to a wide set of researches and actual optimization problems, and have achieved success in many scenarios [21]-[23].

UMDA [24] is one of the most basic EDA. The distribution model is based on the assumption of marginal independence among variables, which gives rise to the following factorization of the JPD:

$$
P\left(\mathbf{X}_{k}\right)=\prod_{i=1}^{n} P\left(\mathbf{x}_{i}\right)
$$

where each variable $\mathbf{X}_{k}(k=1, \ldots, N P)$ can take a finite number of states $\left\{\mathbf{x}_{1}, \mathbf{x}_{2}, \ldots, \mathbf{x}_{n}\right\}, n$ denotes the dimensions. Larrañage [25] extended UMDA to continuous domain (UMDAc), which adopts the univariate function with Gaussian distribution, and the maximum likelihood is used to estimate the parameters of

Gaussian distribution. The univariate density function of $\mathrm{UMDA}_{\mathrm{C}}$ can be described as follows:

$$
P\left(\mathbf{x}_{i}\right)=\frac{1}{\sqrt{2 \pi \sigma_{i}^{2}}} e^{\frac{1}{2 \sigma_{i}^{2}}\left(x_{i}-u_{i}\right)^{2}}
$$

where $u_{i}$ denotes the mean and $\sigma_{i}$ denotes the variance respectively. The formulas are defined by:

$$
\begin{gathered}
u_{i}=\frac{1}{n} \sum_{k=1}^{n} x_{i k} \\
\sigma_{i}=\sqrt{\frac{1}{n} \sum_{k=1}^{n}\left(x_{i k}-u_{i}\right)^{2}}
\end{gathered}
$$

The framework of UMDA $_{\mathrm{C}}$ is as follows:
Step1: Initialization. Within the search space, according to the uniform distribution, $N P$ points are randomly generated as the initial population, evolutional iteration $g$ denotes 1.
Step2: Evaluation. Calculate the fitness value of each individual in the current population at the $g$ th iteration.
Step3: Selection. According to the ordering of fitness values, $S$ advantage individuals are selected by truncation selection strategy.
Step4: Modeling. For the formula (7), the probability distribution model is established among advantage individuals.
Step5: Sampling. According to the probability distribution, the $L$ individuals are sampled as a part of new individuals.
Step6: Updating. The new individuals are composed of selected advantage individuals $S, L$ sampling individuals and $N P-S-L$ random individuals at the $g$ th iteration. Simultaneously, $g$ iteration is regarded as $g+1$ iteration.
Step7: Stopping. If the algorithm satisfies the terminal condition (Maximum iteration), the running is end. Otherwise, go to Step 2.

## C. Variable Scale Variance Strategy

Due to the lack relationship of UMDA $_{\mathrm{C}}$ between variables, and the marginal probability distributions of sampling individuals are considered as the joint probability distribution of the new population, thus the premature convergence of UMDA $_{\mathrm{C}}$ often appears in the search process, and leads to the poor search ability of global optimal solution, the population often obtains the local optimal solution. In order to enhance the diversity of population, many researchers [26]-[27] have studied intensively on the variance control based on Gaussian model.

Aiming at the above characteristic of variance, this paper develops the strategy based on the variable scale variance. According to the search way of UMDA $_{\mathrm{C}}$, the variable scale

variance can be divided into three stages. In the first stage, the scale variance has a wide range of searching, and the current estimated variance based on Gaussian model will be amplified. The smaller variance search is used for the second stage. To approach the global optimum rapidly, the third stage is designed with a tiny search variance. The formula of proposed strategy is introduced as follows:

$$
\sigma_{i}= \begin{cases}\operatorname{rand}(0.1,1) & \text { if }\left(\sigma_{i}<10^{-2}\right) \quad \text { First stage } \\ \operatorname{rand}(0.01,1) & \text { if }\left(\sigma_{i}<10^{-4}\right) \quad \text { Second stage } \\ \operatorname{rand}(0.001,1) & \text { if }\left(\sigma_{i}<10^{-6}\right) \quad \text { Third stage }\end{cases}
$$

For different search, the variable scale variance provides with randomness, so as to enhance the diversity of UMDAc.

## D. Local Search Algorithm

Due to the powerful search capability of differential evolution (DE) [4], this paper extracts the nutrition from the version of DE/rand/1 [28], so as to find the optimized parameters of LSSVM. Through crossover, mutation and selection between the individuals, the optimum approximate objective function value can be obtained, the sampling procedure can be converged fast.

The main steps of local search strategy based on DE are summarized as follows:

Step1: Mutation: To keep the diversity of population, two kinds of newly proposed mutation strategies based on DE/rand/1 are proposed for exploitation. These mutation strategies are used to encourage generating new individuals. In the $g$ th iteration of population, $x_{i, j}^{g}$ represents the $i$ th individual of the $j$ th dimension, $i=1, \ldots, N P . X_{\text {Best }}{ }^{g}{ }_{j}$ is the best individual of the $j$ th dimension. In addition, $F$ and $\zeta_{i, j}^{g}$ are the given mutation factor and the random number from the range $(0,1)$, respectively. $r 1, r 2$, and $r 3$ are different integers randomly selected from the range $[1, N P]$, and they are different from the base index $i$. On the basic of above, $v_{i, j}^{g}$ is regarded as the one of mutant individuals, $c_{i, j}^{g}$ is considered as the other one, they are presented as (11), (12), respectively.

$$
\begin{gathered}
v_{i, j}^{g}=x_{i 1, j}^{g}+F\left(x_{i, j}^{g}-\left(x_{i 2, j}^{g}+x_{i 3, j}^{g}\right) / 2\right) \\
c_{i, j}^{g}=\left(x_{i 1, j}^{g}+x_{i 2, j}^{g}\right) / 2+\zeta_{i, j}^{g}\left(x_{\text {best }, j}^{g}-x_{i 3, j}^{g}\right)
\end{gathered}
$$

Step2: Crossover: Generate a trial individual $u_{i, j}^{g}$ through the crossover operation as follows:

$$
u_{i, j}^{g}=\left\{\begin{array}{l}
v_{i, j}^{g} \quad \text { if }\left(\operatorname{rand}_{i, j}^{g} \leq C R\right) \\
c_{i, j}^{g} \quad \text { otherwise }
\end{array}\right.
$$

where $r a n d_{i, j}^{g}$ and $C R$ are the random number and the given crossover probability from the range $(0,1)$, respectively.

## Begin:

Set the iteration counter $g=0$

## // Initialization

1 Set the maximum iteration number $g_{\max }$, and initialize the values of parameters such as the size of population $N P$, the dimension $D$ of individuals, the selective rate $\theta$ of superior individuals, the random generated rate $\eta$, the mutation factor $F$ and the crossover probability $C R$.
2 Set the individuals as $\mathbf{P}^{g}=\left(\mathbf{x}_{1}^{g}, \mathbf{x}_{2}^{g}, \ldots, \mathbf{x}_{N P}^{g}\right), \mathbf{x}^{g}=\left(x_{2}^{g}, x_{i, 2}^{g}, \ldots, x_{N P}^{g}\right)$, $i=1, \ldots, N P$, and each individual is uniformly distributed in the range $[L, U]$.
3 Evaluate the objective function value of each individual $\mathbf{F}^{g}=\left(f\left(\mathbf{x}_{1}^{g}\right), f\left(\mathbf{x}_{2}^{g}\right), \ldots, f\left(\mathbf{x}_{N P}^{g}\right)\right)$.
// Selection
While ( $g_{\max }$ is not satisfied) do
Select $\theta \times N P$ promising individuals from $N P$.

## //Modeling

According to the promising individuals $M$, the means $u_{i}^{g}$ of the $j$ dimension and the variance $\sigma_{i}^{g}$ of the $j$-dimension can be computed by Gaussian probability distribution model, respectively.
// Variable Scale Variance
For $j=1$ to $D$
If $g<0.25 g_{\max }$
If $\sigma_{i}^{g}<10^{-2}$

$$
\sigma_{i}^{g}=\operatorname{rand}(0.1,1)
$$

End If
Else If $g>=0.25 g_{\max } \| g<=0.5 g_{\max }$
If $\sigma_{i}^{g}<10^{-4}$

$$
\sigma_{i}^{g}=\operatorname{rand}(0.01,1)
$$

End If
Else
If $\sigma_{i}^{g}<10^{-6}$

$$
\sigma_{i}^{g}=\operatorname{rand}(0.001,1)
$$

End If
End If
End For
// Sampling and Repairing
Utilize $u_{i}^{g}$ and $\sigma_{i}^{g}$ to generate new individuals. $y_{i, j}^{g}$ is the new individual vector, $P_{i}^{g}$ is the $j$-dimension probability.
For $i=1$ to $N P-P$
For $j=1$ to $D$

$$
\begin{aligned}
& y_{i, j}^{g}=\text { Gaussian }_{-} \text {Model }\left(P_{i}^{g}, u_{i}^{g}, \sigma_{i}^{g}\right) \\
& \text { If } y_{i, j}^{g}>U \| y_{i, j}^{g}<L \\
& y_{i, j}^{g}=L+\operatorname{rand}(0,1) \cdot(U-L)
\end{aligned}
$$

Else

$$
y_{i, j}^{g}=y_{i, j}^{g}
$$

End If
End For
End For
// Replacement
The offspring individuals are composed of $y_{i, j}^{g}$ and $M$. In addition, the random individuals are also added to the current offspring individuals. The size of random individuals is $\eta \times N P$. They are used to replace the poor fitness values of offspring individuals.
//Local Search
Randomly choose $t_{i+1}^{g}, t_{i+2}^{g}, t_{i+1}^{g}\left(t_{i, j}^{g} \neq t_{i+1}^{g} \neq t_{i+2}^{g} \neq t_{i+1}^{g}\right)$ from $N P$. By (11), (12) and (13), $\zeta_{i, j}^{g}$ is denoted as the random number. $o_{i, j}^{g}$ is

defined as the trial individual. $t_{n=1}^{k}$ is the best individual of $N P$.
For $i=1$ to $\mathrm{N} P$
For $j=1$ to $D$
If $\operatorname{rand}_{t_{j, j}}^{k}(0,1) \leq C R$

$$
o_{t, j}^{R}=t_{t, j, j}^{R}+F\left(t_{j, j}^{R}-\left(t_{t, j, j}^{R}+t_{t, j, j}^{R}\right) / 2\right)
$$

Else

$$
o_{t, j}^{R}=\left(t_{t, j, j}^{R}+t_{t, j, j}^{R}\right) / 2+\zeta_{t, j}^{R}\left(t_{n=1}^{k}-t_{t, j, j}^{R}\right)
$$

End If
If $f\left(o_{t, j}^{R}\right) \leq f\left(t_{t, j}^{R}\right)$

$$
t_{t, j}^{R}=o_{t, j}^{R}
$$

Else

$$
t_{t, j}^{R}=t_{t, j}^{R}
$$

End If
If $t_{t, j}^{R}>U \| t_{t, j}^{R}<L$

$$
t_{t, j}^{R}=L+\operatorname{rand}(0,1) \cdot(U-L)
$$

Else

$$
t_{t, j}^{R}=t_{t, j}^{R}
$$

End If

$$
x_{t, j}^{R}=t_{t, j}^{R}
$$

End For
End For
// Output results
Through calculating objective function values of current population, the final individuals with lower objective function values can be obtained. Set the iteration counter $g \sim g+1$.
End While
End
Fig. 3. Pseudo-code of IEDA scheme
Step3: Selection: To evaluate the trial individual, we compare the trial individual with the original individual. If the objective function is a minimum problem, then the minimum objective function value should be retained in the offspring population. The selective operation is described as:

$$
x_{t, j}^{R}=\left\{\begin{array}{l}
u_{t, j}^{R}, \text { if } f\left(u_{t, j}^{R}\right) \leq f\left(x_{t, j}^{R}\right) \\
x_{t, j}^{R}, \text { otherwise }
\end{array}\right.
$$

Step4: Repairing: To obtain the feasible individuals in the population, the regenerated individual need be checked, if the individual is beyond the boundary of search range, the individual will be replaced by the randomly generated individual among the feasible search range. The strategy guarantees that all the individuals are feasible in the local search procedure.

## E. The Proposed Algorithm

The detailed scheme is presented in Fig. 3.

## IV. EXPERIMENTS

To illustrate the effectiveness of the proposed method, industrial practical data are used to establish the operation optimization model. In order to achieve ideal temperature and
carbon content, IEDA has two effects, one is to optimize the parameters of analytical model, and the other is to optimize the model. In addition, the data analytics method and the operation optimization method are both coded in $\mathrm{C}++$, and the program run on a Core i5 with 3.30 GHz CPU and 3.46 GB memory using Windows 7 operating system (32-bit).

## A. Experimental Data

In this paper, experimental data are collected from the real iron and steel plant. Flame analyzer and off gas analyzer need to be installed on the steel converter. Flame temperature and composition of off gas are measured. The throwing probe is used to detect temperature and carbon content in the molten steel. The operator combines with the experience to judge the current reaction stage, and actual temperature of furnace is measured by the results of flame analyzer, the final data need to be integrated with the ones of off gas analyzer. In three months, a total of 1200 experiments are made, and the data are obtained from 380 furnaces. We have deleted some abnormal data from obtained data. However, in the process of production, a large number of data are missing. Therefore, we have complemented these data by interpolation method.

In the modeling process, the input data include: blowing oxygen content in the reaction process; height of the oxygen lance at the current moment; blowing nitrogen at bottom; blowing argon at bottom; extra seven kinds of supplementary materials. The output variables are current temperature and current carbon content. In Table I, the end-point testing values of temperature and carbon content are shown.

## B. Parameter Setup

The specific parameters of IEDA are given in Table II. The parameters are composed of $\mathrm{UMDA}_{C}$ and local search strategy. In order to ensure the fairness, we select the same evaluation number $(E N)$ as the terminal condition.

TABLE I. END-POINT TESTING DATA OF TEMPERATURE AND CARBON CONTENT

| Num | Temperature( $\mathrm{C})$ | Carbon content(\%) |
| :--: | :--: | :--: |
| 1 | 1615 | 0.035 |
| 2 | 1620 | 0.040 |
| 3 | 1625 | 0.045 |
| 4 | 1630 | 0.050 |
| 5 | 1635 | 0.055 |
| 6 | 1640 | 0.060 |
| 7 | 1645 | 0.065 |
| 8 | 1650 | 0.070 |
| 9 | 1655 | 0.075 |
| 10 | 1660 | 0.080 |

TABLE II. PARAMETERS OF THE IEDA

| Parameter | Value |
| :--: | :--: |
| $N P$ | 200 |
| $D$ | 17 |
| $\theta$ | 0.4 |
| $\eta$ | 0.2 |
| $F$ | 0.5 |
| $C R$ | 0.5 |
| $E N$ | 5000 |

## C. Evaluation Indicator

To evaluate the performance of models, maximum error (MAX), average relative error (ARE) and mean square root error (RMSE) are considered, which are defined by:

$$
\begin{gathered}
\mathrm{MAX}=\max \left(e_{i}\right), \quad i=1, \ldots, N \\
\mathrm{ARE}=\frac{1}{N} \sum_{i=1}^{N}\left(e_{i} / y_{i}\right) \\
\mathrm{RMSE}=\sqrt{\frac{1}{N} \sum_{i=1}^{N_{i}} e_{i}^{2}}
\end{gathered}
$$

where $e_{i}$ is the error, $\left|y^{\text {output }}-y^{\text {end }}\right|=e, y^{\text {output }}$ and $y^{\text {end }}$ are the output value and the end-point objective value respectively.
![img-2.jpeg](img-2.jpeg)

Fig. 4. The end-point temperature control graph by IEDA (a), EDA (b), DE (c) and PSO (d).

TABLE III. MINIMUM ERROR VALUE OF DIFFERENT OPERATIONAL OPTIMIZATION METHODS FOR TEMPERATURE

| Num | IEDA | EDA | DE | PSO |
| :--: | :--: | :--: | :--: | :--: |
| 1 | $\mathbf{0 . 0 E + 0 0}$ | $1.2 \mathrm{E}+01$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ |
|  | $+(9.8 \mathrm{E}-03)$ | $-(5.8 \mathrm{E}-01)$ | $-(4.9 \mathrm{E}-05)$ | $-(1.5 \mathrm{E}-01)$ |
| 2 | $\mathbf{0 . 0 E + 0 0}$ | $7.0 \mathrm{E}+00$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ |
|  | $+(4.6 \mathrm{E}-02)$ | $-(5.8 \mathrm{E}-01)$ | $-(1.1 \mathrm{E}-04)$ | $-(1.0 \mathrm{E}-02)$ |
| 3 | $\mathbf{0 . 0 E + 0 0}$ | $2.0 \mathrm{E}+00$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ |
|  | $+(1.3 \mathrm{E}-01)$ | $-(5.8 \mathrm{E}-01)$ | $-(2.0 \mathrm{E}-04)$ | $-(6.4 \mathrm{E}-03)$ |
| 4 | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ |
|  | $+(1.4 \mathrm{E}-01)$ | $-(3.0 \mathrm{E}-06)$ | $-(1.8 \mathrm{E}-04)$ | $-(2.5 \mathrm{E}-01)$ |
| 5 | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ |
|  | $-(2.7 \mathrm{E}-02)$ | $-(8.0 \mathrm{E}-07)$ | $-(8.3 \mathrm{E}-05)$ | $-(5.2 \mathrm{E}-03)$ |
| 6 | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ |
|  | $+(4.6 \mathrm{E}-02)$ | $-(2.0 \mathrm{E}-06)$ | $-(5.7 \mathrm{E}-06)$ | $-(1.8 \mathrm{E}-03)$ |
| 7 | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ |
|  | $+(1.1 \mathrm{E}-02)$ | $-(2.3 \mathrm{E}-07)$ | $-(1.1 \mathrm{E}-05)$ | $-(3.9 \mathrm{E}-03)$ |
| 8 | $\mathbf{0 . 0 E + 0 0}$ | $4.0 \mathrm{E}+00$ | $\mathbf{0 . 0 E + 0 0}$ | $\mathbf{0 . 0 E + 0 0}$ |
|  | $+(4.0 \mathrm{E}-03)$ | $-(6.8 \mathrm{E}-01)$ | $-(1.9 \mathrm{E}-04)$ | $-(1.9 \mathrm{E}-02)$ |
| 9 | $\mathbf{0 . 0 E + 0 0}$ | $9.0 \mathrm{E}+00$ | $1.0 \mathrm{E}+00$ | $\mathbf{0 . 0 E + 0 0}$ |
|  | $+(1.0 \mathrm{E}-02)$ | $-(6.9 \mathrm{E}-01)$ | $-(7.7 \mathrm{E}-02)$ | $-(8.3 \mathrm{E}-01)$ |
| 10 | $\mathbf{0 . 0 E + 0 0}$ | $1.4 \mathrm{E}+01$ | $6.0 \mathrm{E}+00$ | $5.0 \mathrm{E}+00$ |
|  | $-(2.2 \mathrm{E}-02)$ | $-(6.8 \mathrm{E}-01)$ | $-(7.7 \mathrm{E}-02)$ | $-(8.2 \mathrm{E}-01)$ |

## D. Experimental Results

1) End-point temperature control of BOF steelmaking: Due to the large range of end-point temperature, we select 10 end-point temperature values between $1615^{\circ} \mathrm{C}$ and $1660^{\circ} \mathrm{C}$. The feasible region is diffierent for each input varible. Blowing oxygen content in the reaction process belongs to [1.7,2.0]; height of the oxygen lance belongs to [200,400]; blowing nitrogen belongs to $[0,1]$; blowing argon belongs to $[0,20]$; extra seven kinds of supplementary materials belong to $[0,1]$. For the random characteristic of intelligent optimization, we run 30 times for each algorithm independently, their average value is regarded as the final result. Fig. 4 shows the end-point control results of IEDA, EDA, DE, PSO for temperature. The red point is the output control value of temperature, the blue point is the end-point objective value of temperature. We can find that the control effect of IEDA is better. EDA is unchanged among some end-point control values, which indicates that EDA occurs an overfit phenonmenon in the operation optimization model. The reason is that the probability model may be single, which has no diversity. DE and PSO have good effects. However, they do not control the last end-point values well. The reason is that they have no proper global search, and the local search capability is too strong. From the above experiments, we conclude that IEDA can obtain a higher control performance than other algorithms.

Table III presents the end-point control error results for different algorithms. The results are composed of the integer error and the decimal error. The integer error is equal to zero by IEDA, and the control precision can meet the actual demand. However, IEDA has some bias on the decimal part. Under the circumstance, these errors may be larger than other methods. To sum up, we can analyze that IEDA can control the end-point temperature on whole testing points more accurately. Meanwhile, experimental results show that IEDA has a powerful self-adaption capability.
2) End-point carbon content control of BOF steelmaking: End-point carbon content control setting is the same to temperature experiment. Nothing but the output is carbon content. We select 10 end-point carbon content values between $0.035 \%$ and $0.08 \%$. Fig. 5 shows the end-point carbon content control results. The red point is the output control value of carbon content, the blue point is the end-point objective value of carbon content. For the different comparable algorithms, we can discover that IEDA is closer to the objective testing point. EDA has a local coverage for the testing points of last stage, while DE has a premature for the testing points of first stage. In addition, PSO has a relative stable control accuracy, however, the last testing point has not been identified, the reason is similar to the anaylysis of temperature control experiment. Based on the above results, IEDA can control the end-point carbon content well.

In Table IV, IEDA has a bias on the decimal part. However, the integer part is close to the setting objective value, and the error result can guarantee the industrial requirement. Through the performance analysis of different testing algorithms, experimental results demonstrate that IEDA has less errors for the end-point canbon content control.

Furthermore, IEDA has also a strong exploration and exploration search capability.
![img-3.jpeg](img-3.jpeg)

Fig. 5. The end-point carbon content control graph by IEDA (e), EDA (f), $\mathrm{DE}(\mathrm{g})$ and PSO (h).

TABLE IV. MINIMUM ERROR VALUE OF DIFFERENT OPERATIONAL OPTIMIZATION METHODS FOR CARBON CONTENT

| Num | IEDA | EDA | DE | PSO |
| :--: | :--: | :--: | :--: | :--: |
| 1 | 0.0E-02 | 0.0E-02 | $1.0 \mathrm{E}-02$ | 0.0E-02 |
|  | -(2.9E-05) | -(4.4E-03) | -(8.5E-03) | -(8.1E-05) |
| 2 | 0.0E-02 | 0.0E-02 | $1.0 \mathrm{E}-02$ | 0.0E-02 |
|  | -(1.2E-05) | -(3.3E-09) | -(3.5E-03) | -(1.2E-04) |
| 3 | 0.0E-02 | 0.0E-02 | 0.0E-02 | 0.0E-02 |
|  | -(1.7E-05) | -(3.3E-09) | -(8.5E-03) | -(3.7E-04) |
| 4 | 0.0E-02 | 0.0E-02 | 0.0E-02 | 0.0E-02 |
|  | -(1.6E-05) | -(3.3E-09) | -(3.5E-03) | -(1.2E-04) |
| 5 | 0.0E-02 | 0.0E-02 | 0.0E-02 | 0.0E-02 |
|  | -(1.2E-05) | -(6.7E-09) | -(5.3E-08) | -(6.3E-05) |
| 6 | 0.0E-02 | 0.0E-02 | 0.0E-02 | 0.0E-02 |
|  | -(2.0E-06) | -(1.0E-08) | -(1.4E-07) | -(1.1E-04) |
| 7 | 0.0E-02 | 0.0E-02 | 0.0E-02 | 0.0E-02 |
|  | -(1.9E-05) | -(3.3E-05) | -(5.3E-08) | -(4.7E-05) |
| 8 | 0.0E-02 | 0.0E-02 | 0.0E-02 | 0.0E-02 |
|  | -(9.3E-06) | -(5.0E-03) | -(3.7E-08) | -(1.6E-05) |
| 9 | 0.0E-02 | 1.0E-02 | 0.0E-02 | 0.0E-02 |
|  | -(2.6E-06) | -(1.0E-09) | -(1.0E-08) | -(2.0E-04) |
| 10 | 0.0E-02 | 1.0E-02 | 0.0E-02 | 0.0E-02 |
|  | -(8.5E-06) | -(5.0E-03) | -(3.3E-09) | -(3.5E-03) |

TABLE V. MINIMUM FITNESS FUNCTION VALUE OF OPERATION OPTIMIZATION MODEL

| Type | IEDA-LS | EDA-LS | DE-LS | PSO-LS |
| :--: | :--: | :--: | :--: | :--: |
| Temperature | 2.5E-04 | 2.7E-04 | $1.6 \mathrm{E}-01$ | 4.7E-04 |
| Carbon content | 2.4E-04 | 4.3E-04 | $1.5 \mathrm{E}-01$ | 4.4E-04 |

TABLE VI. ANALYSIS OF PERFORMANCE INDICATORS FOR END-POINT TEMPERATURE CONTROL

| Index | IEDA | EDA | DE | PSO |
| :--: | :--: | :--: | :--: | :--: |
| RMSE | 6.6E-02 | 7.4E+00 | $2.2 \mathrm{E}+00$ | $1.9 \mathrm{E}+00$ |
| MAX( $\mathrm{C})$ | 1.4E-01 | $1.5 \mathrm{E}+01$ | $6.8 \mathrm{E}+00$ | $5.8 \mathrm{E}+00$ |
| ARE | 2.8E-05 | $3.2 \mathrm{E}-03$ | $5.1 \mathrm{E}-04$ | $4.3 \mathrm{E}-04$ |

TABLE VII. ANALYSIS OF PERFORMANCE INDICATORS FOR END-POINT CARBON CONTENT CONTROL

| Index | IEDA | EDA | DE | PSO |
| :--: | :--: | :--: | :--: | :--: |
| RMSE | 1.5E-05 | $6.1 \mathrm{E}-03$ | 7.8E-03 | $1.1 \mathrm{E}-03$ |
| MAX( $\%$ ) | 2.9E-05 | $1.5 \mathrm{E}-02$ | $1.9 \mathrm{E}-02$ | $3.5 \mathrm{E}-03$ |
| ARE | 2.6E-04 | $5.2 \mathrm{E}-02$ | $1.1 \mathrm{E}-01$ | $6.6 \mathrm{E}-03$ |

3) Analysis of data analytics model: The operation optimization model is established by LSSVM based on optimized parameters. The parameters of operation optimization model is the key to the end-point control. If the parameters of operation optimization model are not exact, the model will be overfitting. In this paper, the proposed operation optimization algorithm is applied to the experiment twice, the first time is used to optimize the parameters of analytic model. The second time is used to optimize the whole operation optimization model. Table V shows the mimimum fitness function value of established operation optimization model after the whole experimental data are standardized. Among that, LS denotes LSSVM. The experimental results reflect that the analytic model has a good performance, and the errors of IEDA-LS are lower than that of other optimization algorithms.
4) Analysis of operation optimization algorithm: In order to verify the performance of operation optimization algorithm, Table VI and Table VII show different indicators of IEDA, EDA, DE and PSO for end-point temperature and end-point carbon content control experiments. From the above results, we can see that IEDA is superior to other optimization algorithms, as IEDA increases the diversity in the search process, and IEDA inherits the advantage of EDA and DE. On the basis of improved search strategies, end-point temperature and end-point carbon content are both accurately controlled by IEDA, which is successful for practical application in BOF steelmaking process.

## V. CONCLUSION

In this paper, an improved EDA is proposed for solving the operation optimization problems. The data analytic method based on LSSVM is used to establish the operation optimization model. Meanwhile, variable scale variance strategy is added to Gaussian-based IEDA, so as to strength the diversity of population. In addition, the local search method based on DE is adopted for the search process. Through the analysis of experimental results, we can adjust temperature and carbon content by adding supplementary material and adjusting oxygen rate at the ending moment. And the quality of molten steel can accurately be controlled in the BOF steelmaking process. The experimental results demonstrate the effectiveness of the proposed algorithm that can help production in the BOF steelmaking process. Moreover, there also exist operation optimization problems in some other key steelmaking processes, such as slab reheating furnace, hot rolling and cool rolling, which could also benefit from the proposed algorithm.

In the future, we will focus on the dynamic prediction problem and the dynamic operation optimization problem, in order to better monitor and control the whole state in the BOF steelmaking process. In addition, some other elements (such as

sulfur, phosphorus, manganese, silicon, etc.) will be considered in the BOF steelmaking process.

## ACKNOWLEDGMENT

This research is supported by the 111 Project (B16009), the National Natural Science Fund of China for Major International (Regional) Joint Research Project (Grant No. 71520107004), and the Fund for the National Natural Science Foundation of China (Grant No. 61374203).

## REFERENCES

[1] L. X. Tang, G. S. Wang, and Z. L. Chen, "Integrated charge batching and casting width selection at Baosteel," Oper Res., vol. 62, no. 4, pp. 772-787, Jul-Aug. 2014.
[2] L. X. Tang, Y. Zhao, and J. Y. Liu, "An improved differential evolution algorithm for practical dynamic scheduling in steelmaking-continuous casting production," IEEE Trans. Evol. Comput., vol. 18, no. 2, pp. 209225, Apr. 2014.
[3] L. X. Tang, G. S. Wang, J. Y. Liu, J. Y. Liu, "A combination of Lagrangian relaxation and column generation for order batching in steelmaking and continuous-casting production," Naval Rese. Logi., vol. 58, no. 4, pp. 370-388, Jan. 2011.
[4] L. X. Tang, Y. Dong, and J. Y. Liu, "Differential evolution with an individual -dependent mechanism," IEEE Trans. Evol. Comput., vol. 19, no. 4, pp. 560-574, Aug. 2015.
[5] L. X. Tang and X. P. Wang, "A hybrid multiobjective evolutionary algorithm for multiobjective optimization problems," IEEE Trans. Evol. Comput., vol. 17, no. 1, pp. 20-45, Feb. 2013.
[6] T. H. Su, H. J. Yang, Y. H. Shau, E. Takazawa and Y. C. Lee, "CO2 sequestration utilizing basic-oxygen furnace slag: Controlling factors, reaction mechanisms and V-Cr concerns," Env. Sci., in Press, Sep. 2015.
[7] J. Zhang, F. Y. Jia and L. X. Tang, "An improved quantum-behaved PSO algorithm for a new process optimization problem based on mechanism model of LBE converter," in Proc 4th Int. Sym. Advan. Cont. of Indus. Pro., May. 2011, pp. 23-26.
[8] M. V. V. N. Sriram, N. K. Singh and G. Rajaraman, "Neuro fuzzy modelling of basic oxygen furnace and its comparison with neural network and GRNN models," IEEE Int. Con. Comput. Intel. and Comput. Res. (ICCIC), Dec. 2010, pp. 1-8.
[9] J. Valyon and G. Horváth, "A sparse robust model for a Linz-Donawitz steel converter," IEEE Trans instr. and measu., vol. 58, no. 8, pp. 1-6, Aug. 2009.
[10] X. Z. Wang, M. Han and J. Wang, "Applying input variables selection technique on input weighted support vector machine modeling for BOF endpoint prediction," Eng. App. Arti. Int., vol. 23, no. 6, pp. 1012-1018, Sep. 2010.
[11] Y. X. Zhang, T. Liu and J. H. Wang, "A novel RBF neural network based on data dispersion level and its application in BOF endpoint
prediction," in Proc 25th Conf. Cont. Dec. Conf. (CCDC), May. 2013, pp. 1900-1903.
[12] L. Chen, X. P. Wang and L. X. Tang, "Operation optimization in the hot-rolling production process," Ind. Eng. Chem. Res., vol. 53, no. 28, pp. 11393-11410, Jun. 2014.
[13] L. Chen, Y. Yang and I, Yang, "Robust dynamic operation optimization in hot rolling production process," in Proc. 11th Wor. Con. Int. Con. Auto., Jun-Jul. 2014, pp. 2751-2755.
[14] M. Han, Y. Li and Z. J. Cao, "Hybrid intelligent control of BOF oxygen volume and coolant addition," Neur., vol. 123, no. 10, pp. 415-423, Jan. 2014.
[15] M. Han and Y. Zhao, "Dynamic control model of BOF steelmaking process based on ANFIS and robust relevance vector machine," Exp. Sys. App., vol. 38, no. 12, pp. 14786-14798, Nov-Dec. 2011.
[16] V.N. Vapnik, The nature of statistical learning theory, Springer Verlag, New York, 1995.
[17] J.A.K. Suykens and J. Vandewalle, "Least squares support vector machine classifiers," Neur. Proc. Lett, vol. 9, no. 3, pp. 293-300, 1999.
[18] P. Larrañaga and J. Lozano, "Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation," Kluwer Academic Publishers, 2002.
[19] H. Mühlenbein and G. Paaß, "From recombination of genes to the estimation of distributions I. Binary parameters," in 4th Inter. Conf. Para. Prob. Solv. Nature (PPSN), Springer-Verlag, Berlin, 1996, vol. 1141, pp. 178-187.
[20] D. E. Goldberg, "Genetic Algorithms in Search, Optimization, and Machine Learning," Addison/Wesley, Reading MA, 1989.
[21] A. M. Zhou, J. Y. Sun, and Q. F. Zhang, "An estimation of distribution algorithm with cheap and expensive local search methods," IEEE Trans. Evol. Comput., vol. 19, no. 6, pp. 807 - 822, Dec. 2015.
[22] W. S. Dong, T. S. Chen, P. Tiño and X. Yao, "Scaling up estimation of distribution algorithms for continuous optimization," IEEE Trans. Evol. Comput., vol. 17, no. 6, pp. 797 - 822, Dec. 2013.
[23] Q. F. Zhang, A. M. Zhou, and Y. C. Jin, "RM-MEDA: A regularity model-based multiobjective estimation of distribution algorithm," IEEE Trans. Evol. Comput., vol. 12, no. 1, pp. 41-63, Feb. 2008.
[24] H. Muhlenbein, "The equation for response to selection and its use for prediction," IEEE Trans. Evol. Comput., vol. 5, no. 3, pp. 303-346, Sep. 1997.
[25] P. Larrañaga, R. Etxeberria, J.A. Lozano and J.M. Peña, "Optimization in continuous domain by learning and simulation of Gaussian networks," in Proc Gene. Evol. Comput., 2000, pp. 201-204.
[26] J. Ocenasek, S. kern, N Hansen and P. Koumoutsakos, "A mixed bayesian optimization algorithm with variance adaptation," in 8th Inter. Conf. Para. Prob. Solv. Nature, Heidelberg: Springer Berlin, 2004, pp. 352-361.
[27] W. S. Dong and X. Yao, "NichingEDA: Utilizing the diversity inside a population of EDAs for continuous optimization," IEEE Con. Evol. Comput. (CEC), Jun. 2008, pp. 1260-1267.
[28] R. Storm and K. Price, Differential Evolution-A simple and efficient adaptive scheme for global optimization over continuous spaces, Berkeley: University of California, 2006.