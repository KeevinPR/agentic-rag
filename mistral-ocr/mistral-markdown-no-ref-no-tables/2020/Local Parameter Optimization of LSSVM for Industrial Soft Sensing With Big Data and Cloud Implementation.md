# Local Parameter Optimization of LSSVM for Industrial Soft Sensing With Big Data and Cloud Implementation 

Xinyu Zhang and Zhiqiang Ge ${ }^{\oplus}$, Senior Member, IEEE


#### Abstract

Due to the advantages of high prediction accuracy, least squares support vector machine (LSSVM) has been widely utilized for soft sensor developments in industrial processes. The hyper-parameters of LSSVM are often determined by minimizing the predicted error of validation set based on the intelligent optimization algorithm, which may lead to excessive optimization and model overfitting when validation set are selected improperly. Meanwhile, online parameters optimization is difficult to implement, which results in poor effect of local modeling. This paper proposes UMDA-LOS-LSSVM that is a LSSVM with parameters optimization in local objective set (LOS-LSSVM) by univariate marginal distribution algorithm (UMDA) based on the idea of local modeling. First, the local objective set is extracted in the candidate set based on the testing samples. Then, UMDA is utilized for minimize the predicted error of the objective set and provides the optimized parameters. Finally, training and testing of LSSVM are carried out based on the optimal parameters. In addition, this paper provides the distributed parallel form of the proposed method, which can be used for big data modeling and soft sensor development. The proposed method is applied in a $\mathrm{CO}^{2}$ absorbing column unit to estimate the residual $\mathrm{CO}^{2}$ content, which is implemented through an industrial big data distributed analytics platform. The results show a significant improvement of proposed method based soft sensor, compared to traditional methods.


Index Terms-Cloud computing, distributed parallel, estimation of distribution algorithm (EDA), local objective set, least squares support vector machine (LSSVM).

## I. INTRODUCTION

IN MODERN industrial processes, many key process variables and quality-related variables need to be measured accurately, which can improve the production process [1]. However, due to the limitation of actual measuring instruments,

[^0]many pivotal variables can hardly be obtained directly, such as the quality of product, the content of process gas, and some melt indices [2]. Therefore, data-driven soft sensors emerge as the times require and have been developed and implemented for several decades [3]. The principle of soft sensors can be roughly described that it utilizes an amount of historical data that contains the easy-to-measure variables and the information of the variables to be estimated for establishing the models which can output the variables to be estimated by inputting a set of new easy-to-measure variables [4], [5]. Therefore, soft-sensors play a key role in producing high quality products when hardware sensors are not available.

There are many soft sensor methods based on statistical and machine learning methods [6], such as Partial Least Squares Regression (PLS), Multivariate Linear Regression (MLR), Gaussian Process Regression (GPR), Support Vector Machine (SVM), etc., in which least squares support vector machine (LSSVM) with the advantages of fewer training samples and low difficulty in training stands out and has been widely used to predict key variables in the steel, chemical, and other industries [7]. It can transform the quadratic programming problem for solving the parameters in SVM into linear equations by constructing equation constraints, which reduces the difficulty of solving model [8].

However, the two types of parameters in LSSVM including the penalty factor and the parameter of kernel function which can affect the predicted accuracy of model need to be set artificially [9]. Due to the equation constraints, the higher penalty factor can result in a better performance in training set, which will affect the generalization of the model [10]. Then, the kernel function can map samples to high-dimensional space. The parameters of kernel function can control the relative position and separation degree of samples in high-dimensional space, therefore, the extreme parameters are prone to over-fitting [11].

In determination of those two parameters or called as hyperparameters, many scholars have done many relevant research works. In 1990s, Suykens has proposed the grid search and cross validation for searching hyper-parameters in LSSVM [12]. It is the earliest method of LSSVM hyper-parameter optimization. However, accuracy and efficiency of grid search are very low. Cross validation set will consume a lot of time. Then, based on the cross validation set, G Rubio derives the partial derivative of cross-validation error relative to hyper-parameters, which can


[^0]:    Manuscript received November 27, 2018; accepted February 13, 2019. Date of publication February 20, 2019; date of current version February 6, 2020. This work was supported in part by the National Natural Science Foundation of China (NSFC) (61833014, 61722310, 61673337), the Natural Science Foundation of Zhejiang Province (LR18F030001), and the Fundamental Research Funds for the Central Universities under grant 2018XZZX002-09. Paper no. TII-18-3153. (Corresponding author: Zhiqiang Ge.)
    The authors are with the Department of Control Science and Engineering, Zhejiang University, Hangzhou 310027, China (e-mail: zhangsinyu1995@126.com; gezhiqiang@zju.edu.cn).
    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
    Digital Object Identifier 10.1109/TII. 2019.2900479

be solved by the gradient descent method [13]. But gradient descent is easy to fall into local optimum so that it is difficult to converge to the optimal solution. Cross validation set has the same problem as the last method.

Then, due to the faster search speed and the ability of searching global optimal solutions in most cases [14], intelligent optimization algorithms based on Biocomputing such as genetic algorithm (GA) [15], particle swarm optimization (PSO) [16], etc. have been widely used in hyper-parameters in LSSVM [17]. Although intelligent optimization algorithms compared with grid search and gradient descent owns the faster speed and the better search performance, the cross validation still owns the same problem [18]. In order to solve the time-consuming problem of cross validation, intelligent optimization combined with single validation set was proposed [19], [20], single validation set with similar distribution to the training data can be selected as the hyper-parameter optimization. Furthermore, intelligent optimization combined with all training set was proposed to simplify optimization process. Collecting validation set is sometimes cumbersome [21], therefore, it is often convenient to use all training samples as validation set for optimization, which mainly plays a fine-tuning role in hyper-parameters optimization. This method always requires a presetting for scope of hyper-parameters, then completes the fine-tuning. It is actually a common method in engineering [22].

Meanwhile, in actual industrial process, there are a lot of nonlinear, dynamic, and state shifting data. It is difficult for a single model to keep original performance on these data [23]. In order to make soft sensing more adaptable and local learning frameworks have been proposed by the means of a combination of local models based on the distance between training samples and testing samples [24]. About local modeling of LSSVM, as early as 2007, Liu et al. [25] have proposed the LSSVM with local modeling and applied it in batch processes. However, they only used grid search and cross validation to select hyper-parameters once, and used this parameters in subsequent local modeling. They also analyzed that only one-off parameter selection would lead to worse results in subsequent models. Then Igne et al. [26] applied local weighted LSSVM to the prediction of soil parameters. They utilized intelligent optimization and K-fold cross validation for selecting hyper-parameters, and supposed that the predictive results would be better if online parameters optimization can be implemented in local modeling.

Furthermore, in the modern industry, more and more process data have been collected, which leads to a big data problem [27]. In this case, the computation of kernel matrix of LSSVM, local modeling mechanism and parameter optimization will be quite time-consuming [28], which limits the application of LSSVM in industrial big data.

In this paper, aiming at the targets of hyper-parameters optimization and local modeling with online optimization in LSSVM, LOS-LSSVM has been proposed. It can select a "substitute" as local objective set or sample (LOS) from candidate set for each testing sample by the distance between samples. The parameters selected by local objective set can make LSSVM achieve the best performance when it predicts each testing sample, which can avoid the loss of predictive accuracy caused by the mismatch of parameters selected by cross or single
validation sets above with state-shifting testing samples, and implement local modeling by adjusting hyper-parameters while retaining the information of all training samples. Then, aiming at optimization algorithms, this paper utilizes UMDA as a kind of estimation of distribution algorithms [30] for optimizing local objective set. Empirically, the hyper-parameters with better performance should be concentrated and fixed in a certain range. Therefore, they can be considered as random variables subject to a certain probability distribution. Besides, this paper also proposes distributed parallel (dp) UMDA-LOS-LSSVM based on the MapReduce computing framework, which can significantly reduce the time of local optimization and modeling. In addition, the dp-UMDA-LOS-LSSVM are constructed for soft sensor applications of an industrial process based on industrial big data analytics cloud platform.

## II. LSSVM With Local Objective Set For Parameter Optimization BASED ON UMDA

## A. Least Square Support Vector Machine

In SVM, it usually utilizes quadratic programming method to determine the parameters, while LSSVM can use a set of linear equations for the same purpose [29]. Suppose the training dataset contains $N$ training samples with input variables $\mathbf{X} \in$ $R^{N \times m}$ and output variable $\mathbf{Y} \in R^{N \times r}$, where $m$ and $r$ are dimensions. The model structure of LSSVM can be given as follows:

$$
\hat{\mathbf{y}}_{i}=\mathbf{w}^{T} \Phi\left(\mathbf{x}_{i}\right)+b, i=1,2, \ldots, N
$$

where $\{\mathbf{w}, b\}$ are the parameters of the linear regression function. $\Phi(\cdot)$ is the nonlinear mapping function, which can map input samples to a high dimensional feature space. The parameters of the linear regression function can be obtained through solving the following constrained optimization problem [29]:

$$
\left\{\begin{array}{l}
\min _{\mathbf{w}, b, e} J(\mathbf{w}, e)=\frac{1}{2} \mathbf{w}^{T} \mathbf{w}+\frac{1}{2} \gamma \sum_{i=1}^{l} e_{i}^{2} \\
\text { s.t. } \quad \mathbf{y}_{\mathbf{i}}=\mathbf{w}^{T} \Phi\left(\mathbf{x}_{\mathbf{i}}\right)+b+e_{i}
\end{array}\right.
$$

where $J(\mathbf{w}, e)$ is the loss function, $\mathbf{w}$ is the weight vector, $b$ is the error variable, $e_{i}$ is the deviation variable, and $\gamma$ is the penalty coefficient. Lagrangian multiplier method can be applied in solving the problem (2), according to the KKT condition, the solution of (2) is equal to the solution of a set of following equations [29]:

$$
\left\{\begin{array}{l}
\partial L / \partial \mathbf{w}=0 \rightarrow \mathbf{w}=\sum_{i=1}^{l} \alpha_{i} \phi\left(\mathbf{x}_{\mathbf{i}}\right) \\
\partial L / \partial b=0 \rightarrow \sum_{i=1}^{l} \alpha_{i}=0 \\
\partial L / \partial e_{i}=0 \rightarrow \alpha_{i}=\gamma e_{i} \\
\partial L / \partial \alpha_{i}=0 \rightarrow \mathbf{w}^{T} \phi\left(\mathbf{x}_{\mathbf{i}}\right)+b+e_{i}=\mathbf{y}_{\mathbf{i}}
\end{array}\right.
$$

where $L$ is the Lagrangian multiplier, the model parameters $\left\{\alpha_{i}, b\right\}$ can be obtained by solving (3) and the LSSVM regression model can be represented as follow:

$$
\hat{\mathbf{y}}=\sum_{i=1}^{N} \alpha_{i} K\left(\mathbf{x}, \mathbf{x}_{\mathbf{i}}\right)+b
$$

In this paper, Radial Basis Function (RBF) is applied in LSSVM regression model, which can be formulated as

$$
K\left(\mathbf{x}, \mathbf{x}_{\mathbf{i}}\right)=\exp \left(-\frac{\left\|\mathbf{x}-\mathbf{x}_{\mathbf{i}}\right\|^{2}}{2 \sigma^{2}}\right)
$$

where $\sigma^{2}$ is the parameter of RBF [29].

## B. LSSVM Modeling With Local Objective Set

The parameters including the penalty coefficient and the parameter of RBF, which can affect the fitting performance and generalization of LSSVM need to be seriously determined [29]. As have been introduced, it is the most common practice to use an intelligent optimization algorithm to minimize the prediction error of the whole training set. However, it may lead to the extreme model parameters and overfitting problem. In this part, the local objective set is proposed to improve the traditional method. The LSSVM model can be formulated as follows, where $\mathbf{S}$ denotes the training data set, $\gamma, \sigma^{2}$ denote the penalty coefficient and the parameter of RBF

$$
\mathbf{Y}=\operatorname{LSSVM}_{\mathbf{s}}\left(\mathbf{X}, \gamma, \sigma^{2}\right)
$$

First, the data collected from the process can be divided into two parts: the training data set $\mathbf{S}$.std_train, the candidate data set $\mathbf{S}$.std_candidate, which are normalized. The numbers of them can be represented as $N, N_{c}$. Meanwhile, the testing samples normalized by the means and standard deviation of training set can be denoted by $\mathbf{S}$.std_test, of which the number can be 1 or $N_{t}\left(N_{t}>1\right)$. Then, by selecting the most similar samples in the candidate set with testing samples as the local objective set or samples S.obj. The similarity degree can be measured by Euclidean distance

$$
d_{i j}=\left\|\mathbf{S} \_\mathbf{s t d} \_\text {test }\left(x_{i}\right)-\mathbf{S} \_\mathbf{s t d} \_\text {candidate }\left(x_{j}\right)\right\|_{2}
$$

where $i=1 \ldots N_{t}, j=1 \ldots N_{c}$, apparently, the number of samples in the objective set are the same as the number of testing samples. Apparently, considering the flow data, when testing samples go into the model one by one, the size of $\mathbf{S}$.obj is one, then, testing samples enter the model in batch order, the size of $\mathbf{S}$.obj is $N_{t}$, meanwhile, $\mathbf{S}$.obj is the subset of S.std_candidate. According to (6), utilize S.std_train and S.obj for training LSSVM, which can be given as follows:

$$
\hat{\mathbf{Y}}_{\text {obj }}=\operatorname{LSSVM}_{\text {S.std_train }}(\mathbf{S} \_\mathbf{o b j}, \gamma, \sigma^{2})
$$

$\hat{\mathbf{Y}}_{\text {obj }}$ and $\mathbf{Y}_{\text {obj }}$ represent the predicted and the actual value of the objective set respectively. Therefore, the parameters optimization model of LSSVM can be constructed as follow. The range of hyper-parameters can be set broadly in advance, such as $0.001 \sim 1000$

$$
\begin{aligned}
& f=\min \left(\sum\left|\hat{\mathbf{Y}}_{\text {obj }}-\mathbf{Y}_{\text {obj }}\right|\right) \\
& \text { s.t. }\left\{\begin{array}{l}
\gamma_{\min } \leq \gamma \leq \gamma_{\max } \\
\sigma_{\min }^{2} \leq \sigma^{2} \leq \sigma_{\max }^{2}
\end{array}\right.
\end{aligned}
$$

The optimized parameters $\gamma_{\text {best }}^{\text {obj }}$ and $\sigma_{\text {best }}^{\text {obj }}$ can be obtained by solving (9). Finally, utilize the training set and the
optimized parameters for training LSSVM model again and complete the test

$$
\hat{\mathbf{Y}}=\operatorname{LSSVM}_{\text {S.std_train }}\left(\text { S.std_test }, \gamma_{\text {best }}^{\text {obj }}, \sigma_{\text {best }}^{\text {obj }}\right)
$$

The LSSVM with local objective set for optimization can be called LOS-LSSVM for short. In contrast, the LSSVM with K folds cross validation set, single validation set, and all training set for optimization can be called KCV-LSSVM, SV-LSSVM, and ATS-LSSVM for short respectively. Meanwhile, LOS-LSSVM is a model for online soft sensing. When the number of testing set is 1, LOS-LSSVM can be modeled for every testing sample sent in real time.

## C. Parameters Solution of LOS-LSSVM With UMDA

Estimation of Distribution Algorithm (EDA) is a kind of evolutionary algorithms developed by the genetic algorithm (GA). It first samples and extracts information from the master population with better fitness. Then, it utilizes the information for building the proper probability model. At last, it uses the probability model and individuals with better fitness to update the population. The way to select new solutions can keep the population diversity and speed up the convergence [30].

Univariate Marginal Distribution Algorithm (UMDA) as a kind of EDA algorithms can be used to deal with the problem of the independent continuous variables [31], which utilizes the N one-dimensional Gaussian distribution functions for calculating the probability vectors of N variables [32]. The function can be represented as follow:

$$
f\left(X_{i}=x_{i}\right)=\int_{-\infty}^{x_{i}} \frac{1}{\sqrt{2 \pi} \sigma_{i}} \exp \left\{-\frac{\left(x_{i}-\mu_{i}\right)^{2}}{2\left(\sigma_{i}\right)^{2}}\right\}
$$

where $i=1 \ldots N, X_{i}$ is the random variable, $x_{i}$ is the value of $X_{i}, f$ is the probability of $X_{i}, \mu_{i}$ and $\sigma_{i}$ are represented as the mean and standard deviation of variable $i$ in the population respectively, which can be updated by following formulas, where $M$ is the population size

$$
\begin{aligned}
\mu_{i} & =\frac{\sum_{j=1}^{M} x_{i}^{j}}{M}(i=1, \ldots, N) \\
\sigma_{i} & =\sqrt{\frac{\sum_{j=1}^{M}\left(x_{i}^{j}-\mu_{i}\right)^{2}}{M}}(i=0, \ldots, N)
\end{aligned}
$$

The master population can be selected by the truncation selection which is given as follows, where selectrate is the truncation selection rate, MS is the size of the master population, floor represents "round down"

$$
\mathrm{MS}=\text { floor }(\text { selectrate } \times M)
$$

The algorithm of minimization based on UMDA are shown in Algorithm I [32].

Procedures of utilizing UMDA to optimize LOS-LSSVM are displayed in the flowchart in Fig. 1.

Algorithm 1: The Algorithm of Minimization Based on UMDA.
Input: $n$ : number of optimal variables; $\mathbf{X}_{i}(i=1 \ldots n)$ : optimal variables; $\mathbf{X}_{i}^{\min }, \mathbf{X}_{i}^{\max }$ : range of optimal variables; pop: population; $m$ : population size; $t$ : times of iteration; $m s$ : number of master samples; max_iter: max number of iteration; rand: generate a random number between 0 and 1 ; calobj: the objective function; index: the index of individuals selected; sort: sort function; concate: concatenate function;
Output: the final optimization variables $\mathbf{X}_{\text {best }}$ and best fitness fit $_{\text {best }}$

## Main Process:

1: Generate $m \times n$ Initial population $\mathbf{p o p}^{t}=\mathbf{X}^{\min }+$ rand $*\left(\mathbf{X}^{\max }-\mathbf{X}^{\min }\right)$
2: For $t=1$ : max_iter

1) $\mathbf{f i t}=\operatorname{calobj}\left(\mathbf{p o p}^{t}\right)($ size : $m \times 1)$;
2) index $=$ sort $(\mathbf{f i t}, b y=$ ascending, sele $=m s)$ (size : $m s \times 1$ );
3) $\mathbf{X}_{\text {best }}^{\prime}=\mathbf{p o p}^{t}($ index $[0])$, fit $_{\text {best }}^{t}=\mathbf{f i t}($ index $[0])$;
4) $\mathbf{p o p}_{\text {master }}^{t}=\mathbf{p o p}^{t}($ index $)($ size : $m s \times n)$;
5) calculate $\mu^{t}$ and $\sigma^{t}$ of $\mathbf{p o p}_{\text {master }}^{t}$ by (12), (13) $\left(\mu^{t}, \sigma^{t}\right.$ are $\left.n \times 1\right)$;
6) utilize $\mu^{t}, \sigma^{t}$ to update (11);
7) generate $m-m s$ probability vector $\mathbf{p}^{t}($ size : $1 \times n)$;
8) put all $\mathbf{p}^{t}$ into updated (11), sample $m-m s$ individuals denoted by $\mathbf{p o p}_{\text {part }}^{t}($ size : $(m-m s) \times n)$;
9) $\mathbf{p o p}^{t+1}=$ concate $\left(\mathbf{p o p}_{\text {master }}^{t}, \mathbf{p o p}_{\text {part }}^{t}, b y=\right.$ rows $)($ size : $m \times n)$;
10: Let $t+1$;
11: End for;
12: Output $\mathbf{X}_{\text {best }}^{t}$ and fit $_{\text {best }}$.

## III. Distributed and Parallel UMDA-LOS-LSSVM in Distributed Data ANALYtics Platform

## A. Distributed and Parallel UMDA-LOS-LSSVM Based on MapReduce

When the number of training set is large, the modeling process for the LSSVM method becomes quite difficult. LSSVM in modeling needs to calculate kernel function matrix between samples and samples in training set. When the number of training samples is N , the time complexity of kernel function matrix is $\mathrm{O}\left(\mathrm{N}^{3}\right)$. Therefore, the scale of training samples is large, the calculation of kernel function matrix will be time-consuming. Meanwhile, UMDA-LOS-LSSVM needs to optimize hyper-parameters for each testing sample, and the selection of local objective set needs to calculate the distance between test samples and each training sample, of which the time complexity is still quadratic. Therefore, how to save the time of two steps above is the key to apply UMDA-LOS-LSSVM to large-scale data. Therefore, the idea of data parallelism training based on MapReduce can be proposed.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Flowchart of UMDA-LOS-LSSVM for modeling.

MapReduce is a programming platform for modeling and analyzing big data in a distributed cluster of computing nodes. In the Map stage, the data in chunks will be read line by line in parallel and mapped into "key value pairs." In the Reduce stage, the key value pairs with the same key will be reduced together and complete the follow-up operation in parallel [33], [34].

Distributed modeling of UMDA-LOS-LSSVM can be designed by two MapReduce.

The first one is that split UMDA-LOS-LSSVM into distributed and parallel submodels based on the idea of bagging in ensemble learning [36], and train LSSVM models by divide and conquer, then fuse the results in each sub models. The split numbers can be calculated by the ratio $\alpha(\alpha>1)$ of the number of training samples in every data block to the number of testing samples, which can control the loss of predicted precision due to deblock. The formula is given as follows

$$
\text { Split.Num }=\text { floor }\left(n /\left(\alpha \cdot n_{t}\right)\right)
$$

The procedures are summarized as follows: First, determine the number of splitting blocks, in order to ensure the accuracy of model after divide and conquer, the number of blocks should not be excessive. We can control it by formula (15). Then sample with replacement from the training data stored in distributed

![img-1.jpeg](img-1.jpeg)

Fig. 2. Flowchart of distributed and parallel UMDA-LOS-LSSVM.
storage spaces equally and mark Split_Num (K1 in Fig. 2) kinds of keys for these samples equally in Map stage. Finally, the samples with the same key can be clustered in a Reduce chunk and complete sub models training and hyper-parameter optimization, and results fusion by taking the average. The whole process can be illustrated in the left of Fig. 2.

The second MapReduce is distributed and parallel extraction of local objective set for testing sample aiming at the section "Train UMDA-LOS-LSSVM in chunk i" in the first MapReduce.

The procedures are summarized as follows: Supposed that the number of parallel blocks is K2. First, samples from distributed candidate data chunks equally, calculate the Euclidean distance between each candidate sample and the test sample, and sort all distances ascending. These operators are executed in parallel in Map stage. Then, still in Map stage, split the sorted data in each map into K2 parts equally and mark the key of each sample with their part number respectively. The samples in each map marked as part 1 are closest to the test sample. Finally, in reduce stage, all samples marked as part 1 required can be gathered in a reduce process, and choose the first sample in this reducer block as the local objective set for the testing sample. After extracting local objective set, hyper-parameters can be optimized by UMDA and prediction result can be outputted. The whole process can be illustrated in the right of Fig. 2.

TABLE I
APPROXIMATE TIME COMPLEXITY ANALYSIS OF MAIN STEPS


Suppose that the number of splitting in obtaining submodels (Split_Num) is K1, and the splitting number of extracting local objective set $(\mathrm{K})$ is K 2 , the number of training and candidate samples are both N , the best sorting time complexity is $O(N)$. The approximate time complexity analysis of main steps for one testing sample in distributed model and nondistributed model is shown in Table I. From the approximate time complexity analysis, the value of K1 and K2 that we can control can adjust

![img-2.jpeg](img-2.jpeg)

Fig. 3. Implement and architecture of industrial big data distributed analytics cloud platform.
the training time of dp-UMDA-LOS-LSSVM. Generally, K1 is smaller, which needs to maintain the predictive accuracy of LSSVM.

## B. Practical Application of UMDA-LOS-LSSVM Based on Industrial Big Data Distributed Analytics Cloud Platform.

In this section, we utilize self-developed industrial big data distributed analytics cloud platform with multifunctional subclusters in process industry (MCBDA) for implementing dp-UMDA-LOS-LSSVM so that complete the follow-up simulation experiments and actual industrial application. The architecture of MCBDA including "sub clusters and load balancer in clouds," "industrial scene terminal," "monitoring terminal," and "clients terminal" have been shown in Fig. 3.

The process of modeling has been shown in "Clients" section of Fig. 3. First, users need to select the "UMDA-LOS-LSSVM" basis model and some data input-output modules in model generator so that MCBDA matches these modules and will automatically turn into "dp-UMDA-LOS-LSSVM Modeling" interface. Then, users can upload training set and off-line testing set, and the parameters of model have been predefined.

In the testing stage, the predictive results of off-line testing has been shown at the bottom right of Fig. 3. In the dynamic testing stage, users need to communicate with actual industrial object remotely. If the communication is successful, the online
soft sensing can be started. The online predictive results can be shown at the bottom left of Fig. 3. Meanwhile, if predictive results are abnormal and exceed a certain limit, the system will sent messages to the mobile phone and trig an alarm in time. The platform MCBDA can help dp-UMDA-LOS-LSSVM to be widely used in simulation experiments and actual industries.

## IV. CASE STUDY

## A. Introduction of $\mathrm{CO}^{2}$ Absorbing Column Unit

The principle of $\mathrm{CO}^{2}$ absorption can be described by the following chemical reaction equation:

$$
\mathrm{CO}_{2}+K_{2} \mathrm{CO}_{3}+H_{2} \mathrm{O} \longleftrightarrow 2 \mathrm{KHCO}_{3}+Q
$$

The $\mathrm{CO}^{2}$ absorption process is shown by Fig. 4. After the initial cooling of the process gas from the previous unit, the process gas is cooled again in the process condensing tank 05F003 and enter the absorption column 05C001. Next, the process gas after the absorption column is sent into the mist removal separation tank 06F001, meanwhile, the residual $\mathrm{CO}^{2}$ content is recorded by AR06001. Absorption fluid after absorbing $\mathrm{CO}^{2}$ in 05C001 can be transformed from poor liquid and semi poor liquid to rich liquid which can be reabsorbed in the follow-up process.

In this process, the objective variable for soft sensor development is residual $\mathrm{CO}^{2}$ content in the process gas. Inputs include 11 process variables that can be illustrated in Table II.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Process chart of $\mathrm{CO}^{2}$ absorption column and recovery unit.

TABLE II
DESCRIPTIONS OF THE 11 PROCESS VARIABLES

TABLE III
PARAMETERS SETTING OF UMDA

## B. Prediction of Residual $\mathrm{CO}^{2}$ Content Based on UMDA-LOS-LSSVM

In this part, 3000 samples have been collected from the process, 1500 of them are utilized for training, 500 of them are regarded as the testing samples, and 1000 of them are used to construct the candidate set.

The parameters setting of UMDA is shown in Table III, the optimization range of $\gamma$ is $0.001 \sim 1000$ and the range of
![img-4.jpeg](img-4.jpeg)

Fig. 5. Predicted curves in testing samples by UMDA-LOS-LSSVM.
$\sigma^{2}$ is $0.001 \sim 50$. The predictive curve in testing samples has been shown in Fig. 5. The red points represent real value of testing samples, and the blue line represents predictive results of UMDA-LOS-LSSVM. Testing RMSE is 0.00072347 , and maximum error is 0.0047 .

Section IV-C-G will compare common methods to illustrate the advantages of UMDA-LOS-LSSVM in various aspects.

## C. Advantages of Hyper-Parameters Optimization in Local Objective Set About UMDA-LOS-LSSVM

In this section, the popular hyper-parameters of LSSVM selection methods include five folds cross validation from training set, single validation set with the same distribution as training set and all training set as validation. The three methods need to utilize UMDA to select one-off hyper-parameters. Their prediction and error curves compared with UMDA-LOS-LSSVM have been shown in following figures, and red points and blue line are the same as shown in Fig. 5. The green line represents the predictive results of these popular methods. The predictive

TABLE IV
EVALUATION INDICATORS OF EXPERIMENTS


![img-10.jpeg](img-10.jpeg)

Fig. 6. Compared curves of UMDA-LOS/5CV-LSSVM.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Compared error of UMDA-LOS/5CV-LSSVM.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Compared curves of UMDA-LOS/SV-LSSVM.
evaluation indicators have been shown in Table IV (Only a set of parameters optimized for a testing sample is shown in UMDA-LOS-LSSVM).

From the results of UMDA-5CV-LSSVM shown in Figs. 6 and 7, although cross validation can select parameters many times by splitting training set, there is still a gap between validation set and actual testing samples. However, optimization of local objective set is more effective for each testing sample. Therefore, the proposed model owns better performance. From the results of UMDA-SV-LSSVM shown in Figs. 8 and 9, single validation set only selects parameters once, and the effect of selection is related to the selection of validation set. Therefore, it is usually worse than cross validation set. Meanwhile, Fig. 10 has shown
![img-8.jpeg](img-8.jpeg)

Fig. 9. Compared error of UMDA-LOS/SV-LSSVM.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Compared curves of UMDA-LOS/5CV/SV-LSSVM.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Compared curves of UMDA-LOS/ATS-LSSVM.
the error curves of UMDA-LOS-LSSVM and validation set methods including UMDA-5CV/SV-LSSVM, which can show more intuitively that optimization based on local objective set is superior to the methods based on validation set and one-time optimization. From the results of UMDA-ATSLSSVM shown in Fig. 11, because it is an empirical method for fine-tuning, when the range of hyper-parameters is too large, such as the range of parameters set in this experiment, the optimized parameters will lead to serious over-fitting, and the parameters optimized are extreme. Therefore, from Fig. 11, it is obvious that the performance of proposed method is better.

![img-11.jpeg](img-11.jpeg)

Fig. 12. Predicted curves in local objective set by UMDA-LOS-LSSVM.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Predicted curves in all training set by UMDA-ATS-LSSVM.

## TABLE V

EVALUATION INDICATORS OF EXPERIMENTS

## D. Explanation of Advantages of Local Objective Set From the Point of Degree of Convergence to Testing Samples

In this section, compared with UMDA-ATS-LSSVM, it is more obvious that the optimization of local objective set is helpful to the fitting of testing samples. Fig. 12 has shown the predictive curves of local objective samples in UMDA-LOSLSSVM. Fig. 13 showed the predictive curves of all training set in UMDA-ATS-LSSVM. The predictive evaluation indicators of local objective set and all training set have been shown in Table V. From Figs. 5 and 12 and their RMSE, the prediction result in testing set of UMDA-LOS-LSSVM is similar to the result in local objective set, which means that the local objective sample can serve as the "substitutes" of testing sample. However, from Figs. 11 and 13, due to the large optimization range of hyper parameters and all training set as optimization target, UMDA-ATS-LSSVM has been over-fitted, which make the prediction results of all training set are wonderful, but the result in testing samples are bad.

Figs. 14 and 15 show the RMSE drop curves (yellow line) in testing samples and convergence curves (blue line) of UMDA-LOS/ATS-LSSVM. Fig. 14 belongs to LOS, which means that each iteration of UMDA reduces the fitness error once, the RMSE corresponding to LSSVM with the parameters will decrease synchronously, which shows optimization of each step based on LOS is effective. However, Fig. 15 has shown
![img-13.jpeg](img-13.jpeg)

Fig. 14. RMSE drop and convergence curves by UMDA-LOS-LSSVM.
![img-14.jpeg](img-14.jpeg)

Fig. 15. RMSE drop and convergence curves by UMDA-ATS-LSSVM.
![img-15.jpeg](img-15.jpeg)

Fig. 16. Convergence process in testing set of the UMDA-LOS LSSVM.
![img-16.jpeg](img-16.jpeg)

Fig. 17. Convergence process in testing set of the UMDA-ATS LSSVM.
that the optimization process and RMSE drop are not synchronized, which shows optimization of each step based on ATS is ineffective.

Figs. 16 and 17 have shown that mapping all prediction results into a slant line. The more concentrated projection points mean the better predictive effect. The optimization times of UMDA is 10 , we map prediction results corresponding to the first, fifth, and last optimized parameters into the slant line and draw enveloping lines of each predicted results. Fig. 16 belongs to LOS where the three enveloping lines are contractive, which means that the effect of optimization is uniformly valid. However, Fig. 17

![img-17.jpeg](img-17.jpeg)

Fig. 18. Convergent curves of UMDA and PSO.
![img-18.jpeg](img-18.jpeg)

Fig. 19. Convergence process in testing set of UMDA and PSO.
![img-19.jpeg](img-19.jpeg)

Fig. 20. Variety of Gauss distributions for hyper-parameters in UMDA.
belongs to ATS where the three enveloping lines are outspread, which means that the effect of optimization is irregular.

From the experiments above, UMDA-LOS-LSSVM can implement the most effective hyper-parameters optimization aiming at each testing sample.

## E. Advantages of Optimization Algorithm UMDA for UMDA-LOS-LSSVM

In this section, the standard particle swarm optimization (PSO) is utilized for comparing with UMDA under the same conditions which is shown in Table III. The two algorithms used to optimize LOS-LSSVM are run eighty times and the results with the lowest final fitness are extracted for contrast respectively. Fig. 18 shows the convergent curves of UMDA and PSO, which indicates that the optimization performances of UMDA and PSO are similar, however, the final fitness of UMDA is lower. Fig. 19 illustrates convergent process in testing set of UMDA and PSO which shows that predicted circles of UMDA are smaller than the circles of PSO and are closer to the actual value. Meanwhile, in UMDA optimization process, the variation of Gaussian distributions that hyper-parameters obey has been shown in Fig. 20. Right to left denotes the first, fifth, and last iterations, respectively. The peak of Gaussian distribution be-
![img-20.jpeg](img-20.jpeg)

Fig. 21. Compared curves of UMDA-LOS/LM-LSSVM.
![img-21.jpeg](img-21.jpeg)

Fig. 22. Compared error of UMDA-LOS/LM-LSSVM.

TABLE VI
EVALUATION INDICATORS OF EXPERIMENTS


comes "thin" gradually, which indicates the optimal parameters are more concentrated.

## F. Advantages of Local Modeling Compared With local LSSVM in UMDA-LOS-LSSVM

In this part, the implement process of local modeling LSSVM (LM-LSSVM) can be described as follows. First, utilize UMDA and five-folds cross validation to select hyper-parameters in LSSVM. Then, aiming at each testing sample, we select 120 samples closest to the testing sample (Euclidean Distance Metric) from training set. Finally, utilize the samples selected for training a local LSSVM model and complete prediction of the testing sample [25]. The prediction curves and prediction error of two methods have been shown in Figs. 21 and 22. The evaluation indicators are shown in Table VI. Due to all samples for training and on-line local hyper-parameters adjustment for each testing sample, performance of proposed method is better than local modeling.

## G. Advantages of Fitting Ability Compared With Strong Regression Model GBDT in UMDA-LOS-LSSVM

Gradient Boosting Decision Tree (GBDT) which is one of the most effective algorithms for classification and regression applications [35]. In this experiment, the number of boost trees is 200 , the learning rate is 0.3 , and the max depth of boost tree is 30 . Prediction curves and prediction error of two methods have been shown in Figs. 23 and 24. Evaluation indicators are

![img-22.jpeg](img-22.jpeg)

Fig. 23. Compared curves of UMDA-LOS-LSSVM/GBDT.
![img-23.jpeg](img-23.jpeg)

Fig. 24. Compared error of UMDA-LOS-LSSVM/GBDT.
TABLE VII
EVALUATION INDICATORS OF EXPERIMENTS


![img-24.jpeg](img-24.jpeg)

Fig. 25. Predicted result in testing set by dp-algorithm.
shown in Table VII. From results, the proposed method owns the advantages of local modeling, which can obtain better prediction effect at spikes. Parameters optimization in the proposed method can adjust nonlinear unit of model. It owns stronger nonlinear processing ability.

## H. Prediction of Residual $\mathrm{CO}^{2}$ Content Based on Distributed and Parallel UMDA-LOS-LSSVM

In this part, 10000 samples have been collected from the process, 5000 of them are utilized for training models, 100 of them are regarded as the testing samples and 4900 of them are used to construct the candidate set. Meanwhile, the number ratio $\alpha$ is set as 20 . The distributed parameters in the Section III-A can be set: K 1 is 2 , and K 2 is 3 . The whole experiment can be completed in the platform in the Section III-B.

The predicted results of (distributed and parallel) dp-UMDA-LOS-LSSVM and it without distribution have been shown in Fig. 25, and evaluation indicators has been shown in Table VIII

TABLE VIII
EVALUATION INDICATORS OF EXPERIMENTS

in this paper. From the predicted results, dp and non-dp methods are similar as a whole. However, the number of training samples in submodels is less than non-dp model, which will reduce the accuracy of model more or less. It will be reflected in prediction of spikes, which has been marked by blue frameworks shown in Fig. 25. But from RMSE in Table VIII, the predictive loss of dp-model is small, and it is acceptable completely. More importantly, the small predictive loss can obtain large improvement in modeling time. Compared with non-dp model, the time of dp-modeling is almost $1 / 8$ of non-dp modeling, which means that distributed and parallel UMDA-LOS-LSSVM proposed can be applied to large scale data under the condition of less precision loss.

The proposed model has been put into practical application in industrial big data distributed analytics cloud platform introduced in the Section III-B, and the effects of off-line and on line modeling have been shown in Fig. 3.

## V. CONCLUSION

In the present paper, the idea of local modeling was utilized for constructing the objective set of LSSVM parameter optimization, which extracts the samples similar to testing samples from the candidate set and forms the objective set. Meanwhile, the UMDA as a kind of estimation of distribution algorithms (EDA) with better convergence effect has been utilized for solving the problem of optimization, which improve the prediction accuracy. In experiments, UMDA-LOS-LSSVM can achieve better performance than common parameter optimization methods, local modeling and strong model. Then, the distributed and parallel UMDA-LOS-LSSVM was proposed based on the data parallel strategy, which can greatly reduce the time cost of model training in case of less prediction precision loss. Finally, all the proposed algorithms were implemented on the industrial big data distributed analytics cloud platform. The real industrial $\mathrm{CO}^{2}$ absorbing column unit has demonstrated the effectiveness and superiority of the proposed algorithms for soft sensor modeling and application.
