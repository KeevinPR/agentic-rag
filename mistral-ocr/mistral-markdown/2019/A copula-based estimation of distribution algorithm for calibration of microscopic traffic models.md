# A copula-based estimation of distribution algorithm for calibration of microscopic traffic models 

Mehdi Rafati Fard, Afshin Shariat Mohaymany ${ }^{\circ}$

Traffic Research Laboratory, School of Civil Engineering, Iran University of Science and Technology, Narmak, Tehran, Iran

## A R T I C L E I N F O

Keywords:
Calibration
Estimation of distribution algorithms
Copula
Dependency structure
Static metrics

## A B S T R A C T

The importance of calibration of microscopic traffic models as the main core of traffic simulation software results from the need for more realistic traffic behaviors. The latent essence of several parameters in such models as well as the uncertainties resulting from the noise in the data, make the process of calibration much more complex. Usually, the calibration process is formulated as an optimization problem. Selecting the appropriate solution algorithm due to nonlinear and nonconvex nature of the problem is crucial. The importance of the issue is more significant when the matter of calibrating the medium or large-scale simulation model is considered. This is mainly due to the expensive cost that running the simulation models impose. Therefore, applying the current algorithms in which finding the appropriate solutions requires a large number of simulation runs is not deemed suitable. In this paper, an estimation of distribution algorithm based on copula theory has been suggested. In contrast with traditional solution algorithms, in the proposed algorithm complex interaction between parameters of a model has been considered by constructing and sampling from a copula-based probabilistic model. Copulas are functions that describe the dependence structure of a set of random variables and connect multivariate distribution functions to one-dimensional marginal distribution functions. The results indicate that applying an explicit probabilistic model based on copula helps the estimation of distribution algorithm to explore the search space more effectively and efficiently as well as provides the possibility of extracting the knowledge with regard to the structure of the calibration problem through analyzing the probabilistic models that are constructed during the evolution process. Furthermore, this new algorithm has been compared with the genetic algorithm and kernel-based cross-entropy method on synthetic and real trajectory data. The results confirm that the proposed algorithm is more efficient in terms of convergence rate, resource usage and more robust in terms of the probability of finding the global optimal solution.

## 1. Introduction

Nowadays, microscopic traffic simulation tools are widely employed to assess dynamic traffic management strategies, different applications of Intelligent Transportation Systems, and various options of geometric design. The capability of simulation software to model the complex processes and interactions in transportation systems on the one hand, and the inability of analytical tools to model and analyze such type of systems on the other, led to the ever-growing popularity and development of a wide range of microscopic traffic simulation software (Barceló, 2011). Among them, AIMSUN (TSS, 2015), VISSIM (PTV, 2015), Paramics (Quadstone, 2009),

[^0]
[^0]:    ${ }^{\circ}$ Corresponding author.
    E-mail address: shariat@iust.ac.ir (A. Shariat Mohaymany).

CORSIM (McTrans, 2014), and the open-source simulator SUMO (DLR, 2018) are the most well-known software. These software tools work based on a set of traffic microscopic models. Car following and lane changing models can be considered as the most important of such models and hence, attracted great interest of traffic researchers. To review these models we refer to Brackstone and McDonald (1999), Saifuzzaman and Zheng (2014) and Zheng (2014).

Car following models describe the longitudinal motion of a vehicle in a lane and its interaction with one or several vehicles ahead. According to applied basic logic, car following models are classified as follow: stimuli-response (Chandler et al., 1958; Gazis et al., 1961), desired measures (Helly, 1961; Treiber et al., 2000), collision avoidance or safety distance (Gipps, 1981; Kometani and Sasaki, 1959; Newell, 1961), optimal velocity (Bando et al., 1995; Helbing and Tilch, 1998), cellular automata (Krauß et al., 1996; Nagel and Schreckenberg, 1992), psychophysical or action point (Fritzsche, 1994; Wiedemann, 1974), discrete choice-based (Koutsopoulos and Farah, 2012; Toledo et al., 2007; Zheng et al., 2012), and data-driven models (Chakroborty and Kikuchi, 1999; Chong et al., 2013; Colombaroni and Fusco, 2014; Khodayari et al., 2014; Kikuchi and Chakraborty, 1992; Papathanasopoulou and Antoniou, 2015; Zheng et al., 2013). Each of the car following models includes a set of parameters. In fact, these parameters control the performance of the model and must be adjusted properly before using the model. The process of adjusting the parameters is called calibration. The purpose of calibration is to make the model outputs more consistent with corresponding field measurements and consequently, improve the model's ability to simulate the local characteristics of the traffic flow and driver behavior (Dowling et al., 2004). To provide an appropriate and efficient framework for calibration, several studies have been conducted in this field. However, calibration of microscopic traffic models is still an active area of research.

Considering the fact that several parameters of the car following models such as reaction time and desired variables (e.g. desired headway or speed) are latent and cannot be directly observed and calculated through field measurements, the complexity of the calibration process is highly increased. By the advancement of technology and increasing access to vehicle trajectory data, in recent years, simulation-based calibration of microscopic traffic model using trajectory data has become of great interest. In this approach, the calibration process is defined as a multivariate nonlinear optimization problem in the form of Eq. (1).

$$
\overrightarrow{\theta}^{*}=\arg \min f\left(Y^{\max }, Y^{\min } \mid \overrightarrow{\theta}\right)
$$

where $f$ is the objective function (Goodness of fit), $Y^{\min }$ and $Y^{\max }$ are simulated and corresponding field measurements (Measure of performance) respectively, $\overrightarrow{\theta}$ denotes the vector of model parameters for calibration, and $\overrightarrow{\theta}^{*}$ is the optimum value of parameters.

Punzo et al. (2012) mentioned the improper configuration of the calibration problem as one of the drawbacks related to calibration. Configuration of the calibration problem depends on how the goodness of fit (GOF), the measure of performance (MOP), and the optimization algorithm (OA) are chosen. The goodness of fit represents the difference between simulation outputs and corresponding real data. Different calibration methodologies have regarded different goodness of fit criteria. Root Mean Square Error (Hoogendoorn and Ossen, 2005; Punzo et al., 2012; Punzo and Simonelli, 2005; Vieira da Rocha et al., 2015), Theil's inequality coefficient U (Brockfeld et al., 2004; Jin et al., 2014; Kim and Mahmassani, 2011; Ossen and Hoogendoorn, 2008; Papathanasopoulou and Antoniou, 2015; Punzo et al., 2012; Zhong et al., 2016) and GEH statistic (Paz et al., 2015; Punzo et al., 2012) have been used more than others (for review of GOFs see Hollander and Liu (2008) and Ciuffo and Punzo (2010)). Investigating the effects of different calibration configurations, Ciuffo and Punzo (2014) pointed out the better performance of mean absolute error in comparison with other GOF criteria as well as restriction of normalized criteria such as NRMSE. Kesting and Treiber (2008) investigated the calibration of microscopic traffic models using trajectory data and pointed out that calibration results of car following models were dependent on the type of goodness of fit and such dependency can be considered as a criterion for the robustness of model calibration.

However, if any model could accurately reproduce the real system and on the other hand, there exists no difference between the outputs of the model and the observed values, it can be inferred that the type of objective function and measure of performance have no effect on the estimated values of parameters. Although, since the model is a summary of the reality, the model is more or less associated with errors. Hence, choosing different MOPs with the same GOF and even with the same optimal values of the objective function, could lead to different estimates of the model parameters (Punzo and Simonelli, 2005). In general, any time-varying quantity such as acceleration (Ranjitkar et al., 2005), speed (Brockfeld et al., 2004; Ossen and Hoogendoorn, 2009a; Ossen and Hoogendoorn, 2008; Punzo and Simonelli, 2005; Ranjitkar et al., 2004) and headway (Brockfeld et al., 2004; Kesting and Treiber, 2008; Ossen and Hoogendoorn, 2009a; Ossen and Hoogendoorn, 2008; Ranjitkar et al., 2004), or a combination of these criteria (Paz et al., 2015; Zhong et al., 2016) can be used as a measure of performance. Punzo and Simonelli (2005) investigated the effect of selected MOPs on the results of car following model calibration and pointed out that considering the inter-vehicle spacing as MOP leads to better results in the process of calibration. In another study, by using synthetic data, Punzo et al. (2012) examined different combinations of MOPs (headway and speed) and GOFs (RMSE, MAE, U and GEH) and announced that the combination of speed and headway as a measure of performance by using Theil inequality statistics leads to worse results than the application of these criteria separately. They also mentioned that employing the headway as MOP leads to acceptable results for speed, while the opposite direction of this relationship is not established. In a similar study, Kesting and Treiber (2008) confirmed the provided results by Punzo and Simonelli (2005) and announced that many of the calibration errors were linked to inter-driver variability in traffic flow.

Another source of uncertainty in the calibration of microscopic traffic models is due to errors of vehicle trajectory data. Ossen and Hoogendoorn (2009b) investigated the effect of measurement errors on the reliability of parameters estimated through calibration procedure and stated that this effect was much more tangible than to be negligible. In a similar study, Montanino and Punzo (2015) evaluated the performance of calibrated car following and lane changing models by using noise-contaminated and noise-free data separately and also when interacted with each other. Based on this research at the scale of individual models, effects of noise on the

distribution and correlation of parameters values of the lane changing model have been considerable, but its impact on calibrated parameters of the car following model is negligible. However, in the simulation scale, when the interaction between these two models is considered, calibrated model based on noise-free data could reproduce the macroscopic characteristics of the traffic flow and traffic congestion patterns more accurately.

Calibration approaches can be divided into the local and global approaches. In the local approaches, endogenous variables (MOPs) are independently compared with field data for each data point. While in the global approaches, the entire observed trajectory is compared with the simulated trajectory (Treiber and Kesting, 2013a). In other words, a local approach is entirely based on the model and no simulation is required. Whereas a global approach is based on the simulation and each calculation of the objective function requires one or more runs of the simulation. Treiber and Kesting (2013a) investigated the quality and quantity of data applied in the calibration of microscopic traffic models and expressed that car following models calibrated by using global methods are less affected by the noise than the local approaches. They also pointed out that applying gap data as MOP leads to better identification of model parameters.

One of the main challenges in the calibration of microscopic traffic models is choosing the appropriate optimization algorithm to find approximate solutions to Eq. (1). Applied optimization algorithms in solving the calibration problem are divided into two categories, namely deterministic and probabilistic algorithms. Due to the complex structure of calibration problem and different combinations of parameters, the deterministic algorithms, which are mainly based on the gradient, lead to a large number of local optima and the application of these types of algorithms does not provide appropriate results when the objective function is highly complex (a jagged objective function). Instead, random search algorithms have been widely used (Zhong et al., 2016). Meanwhile, genetic algorithm (GA) has undoubtedly been used more than any other for such purposes (Hamdar et al., 2015; Jin et al., 2014; Kesting and Treiber, 2008; Monteil et al., 2014; Ranjitkar et al., 2005; Schultz and Rilett, 2004). Other methods such as nonlinear constrained simplex (Ossen and Hoogendoorn, 2009a; Ossen and Hoogendoorn, 2008), downhill simplex (Brockfeld et al., 2004; Kim and Mahmassani, 2011), OptQuest Multistart (Ciuffo and Punzo, 2010; Punzo et al., 2012; Punzo and Simonelli, 2005), and crossentropy method (Zhong et al., 2016) have been used in the literature to determine optimal value of model parameters. To evaluate the efficiency of algorithms in solving the calibration problem, Punzo et al. (2012) applied some indicators to determine the robustness and accuracy of OptQuest, downhill simplex, and the genetic algorithm in finding a known global solution. It was found that the performance of the applied algorithms is quite different. Both genetic and OptQuest algorithms would be able to find the true value of parameters with high frequency. However, the random nature of genetic algorithm mostly influenced the reproducibility of the best solution. While OptQuest algorithm shows less dependence on initial condition and in most cases converges to the same global solution. In another study, Ciuffo and Punzo (2014) indicated the best performance of the genetic algorithm and OptQuest Multistart to the simultaneous perturbation stochastic approximation and simulated annealing in terms of convergence rate and quality of solutions. Paz et al. (2015) investigated the performance of the memetic algorithm, which is a combination of genetic and simulated annealing algorithms, and pointed out that simulated annealing could allow better refinement of produced solutions by genetic algorithm and as a result, provide the global optimal solution by spending fewer resources. Recently, Zhong et al. (2016) represented a framework for calibrating car following models through using cross-entropy and probabilistic sensitivity analysis. Cross-entropy was used in order to find solutions close to the global optimal solution and the probabilistic sensitivity analysis to reveal the probabilistic behavior of the model's response with respect to its parameter uncertainties.

Although mentioned algorithms have a proper performance in solving the calibration problem, nevertheless, algorithms with more satisfactory results from the point of view of accuracy, in terms of finding a global or near-global solution, and efficiency, in terms of consuming resources (e.g. computational cost) are required. The recent case is more evident when the mentioned algorithms are used in computationally expensive simulations such as medium and large-scale microscopic traffic simulations (Balakrishna et al., 2007; Hale et al., 2015). These types of simulations due to the spatial and temporal extent of the model can be prohibitively expensive, requiring anywhere from minutes to hours of simulation time for each evaluation of candidate solution. Therefore, more efficient algorithms are required. In addition, the performance of these algorithms depends largely on fine-tuning of their various parameters (Armañanzas et al., 2008). For example, in the genetic algorithm, the type of operators, the probability of recombination and mutation, the mutation rate, population size and the number of generations could be mentioned. The values of these parameters are usually determined empirically and therefore, the analyst requires sufficient experience in using this algorithm to solve various problems. In some algorithms such as genetic algorithm which is broadly used in calibration, another issue is the disrupting effects of its operators in problems with complex interactions between the parameters (Larranaga and Lozano, 2002).

To solve these knots in the calibration of microscopic traffic simulation models, we were motivated to use an estimated distribution algorithm (EDA) based on copula theory (named hereafter copula-based EDA). The EDA family (Larranaga and Lozano, 2002; Mühlenbein and Paaß, 1996; Pelikan, 2005), which has recently been of great interest, is a population-based evolutionary algorithm that differs from conventional genetic algorithms in generating new solutions and propagation between generations. The main advantages of the estimated distribution algorithm include the lack of need to adjust the algorithm parameters. This is conducted through applying an explicit probabilistic model to guide the search process and achieve better and more robust results than other algorithms across a broad spectrum of optimization problems (Armañanzas et al., 2008). Additionally, analyzing the probabilistic model that has been learned through evolution can be useful to capture previously unknown information about the structure of black box optimization problems and also provide important knowledge about the characteristics of the problem. So, the EDAs can be used not only as an optimization algorithm but also as a simulation tool to produce information about the problem domain. Estimated distribution algorithms are used in a wide range of fields such as engineering (Liu et al., 2015; Wang et al., 2015) and Bioinformatics (Armañanzas et al., 2008). As far as the authors know, this study is the first case in applying the copula-based EDA for calibration of microscopic traffic simulation models.

To better present our findings, this paper is organized into 7 sections. Following this introduction, the next section explains the formulation of the intelligent driver model. Then, a short introduction of the estimated distribution algorithms and copula theory are presented in Sections 3 and 4 respectively. In Section 5, different experiments that are designed to compare the performance of the proposed algorithm with genetic algorithm (GA) and Cross-Entropy Method (CEM) are explained. It includes the applied trajectory data, how to configure the calibration problem, proposed performance indicators, and the configuration parameters of each algorithm. The results of applying the proposed algorithm and its comparison with results of applying GA and CEM are presented in Section 6. Finally, in Section 7 conclusions and future studies are presented.

# 2. Intelligent driver model 

In this study, the Intelligent Driver Model (IDM) (Treiber et al., 2000) due to the relatively large number of parameters to be adjusted is used for performance assessment of the copula-based EDA in the calibration of microscopic traffic models. IDM belongs to desired measures type of car following models. Most of the variables (e.g., desired headway or speed) in desired measures models are latent and could not be easily calculated from the field data. Therefore, estimation of parameters and calibration of these models is quite challenging. In the IDM, desired gap and speed are considered simultaneously and therefore, can be used for both the free and bounded traffic flow. Using an equation for both free and bounded flow enables smooth transitions between these two traffic flow conditions. Eq. (2) shows the functional form of the IDM. Accordingly, when two cars are far away, the third part of the model (ratio of the desired gap to the current gap) is insignificant. Therefore, the model acts as a free flow model in which the desired speed of the driver controls driver's accelerating behavior. In terms of traffic congestion, in which the driver's behavior is heavily influenced by its environment, the second part of the model (the ratio of current speed to the desired speed) is negligible due to the low speed. In such circumstances, the driver's behavior is controlled by the third part of Eq. (2).

$$
a_{n}(t)=a_{\max }^{n}\left[1-\left(\frac{V_{n}(t)}{V_{n}^{*}}\right)^{2}-\left(\frac{S_{n}^{*}(t)}{S_{n}(t)}\right)^{2}\right]
$$

where $a_{\max }^{\mathrm{n}}$ is the maximum acceleration/deceleration of subject vehicle $n, V_{n}^{*}$ is the desired speed, $S_{n}(t)$ denotes the current gap (bumper to bumper distance between the subject vehicle and the leading vehicle), $S_{n}^{*}(t)$ is the desired gap at time $t$, and $\delta$ controls the free acceleration near the desired speed. Desired gap (following distance) in this model depends on several factors that include speed $\left(V_{n}(t)\right)$, speed difference or approaching rate $\left(\Delta V_{n}(t)=V_{n}-V_{n-1}\right)$, the maximum acceleration $\left(a_{\max }^{\mathrm{n}}\right)$, the comfortable deceleration $\left(b_{\text {comf }}^{\mathrm{n}}\right)$, the minimum distance at the standstill situation $\left(S_{\text {sim }}^{\mathrm{n}}\right)$, and the desired time gap $\left(T_{n}^{*}\right)$. Eq. (3) shows the mathematical form of the desired gap in the IDM.

$$
s_{n}^{*}(t)=s_{\text {sim }}^{\mathrm{n}}+V_{n}(t) T_{n}^{*}+\frac{V_{n}(t) \Delta V_{n}(t)}{2 \sqrt{a_{\max }^{\mathrm{n}} b_{\text {comf }}^{\mathrm{n}}}}
$$

## 3. Principles of the estimated distribution algorithms

Evolutionary Algorithms (EAs) are stochastic search techniques which are designed to solve difficult optimization and adaptive problems. Estimated distribution algorithms are known as a new family of algorithms and in fact, are an alternative to the traditional EAs. This class of algorithms was introduced by Mühlenbein and Paaß (1996) as the development of genetic algorithms. EDAs apply a combination of genetic and evolutionary computation, machine learning and statistics in the optimization process. The main difference in EDAs compared to GAs is the lack of variation operators. There is no recombination nor mutation operator in EDAs. The mentioned operators have been replaced with building a probabilistic model of promising candidate solutions and sampling new solutions by use of the constructed model. The probabilistic models which are embedded in the EDAs, capture the features of promising individuals in order to increase the probability of generating global optimum (Larranaga and Lozano, 2002). Moreover, in traditional evolutionary computation, the mutual connections between the variables (the building blocks that represent individuals) are implicitly considered. While in the EDAs these mutual connections are explicitly considered through a joint probability distribution of selected solutions in each generation.

Fig. 1 shows the general process of EDAs. Similar to other population-based algorithms, firstly, the initial population of solutions, usually by assuming that each variable has uniform distribution, is generated and next, each solution is evaluated by its corresponding objective function value. After entering the iterative loop to explore the search space, a certain number of individuals (promising solutions) are selected by using a selection method. These promising solutions will be used to construct the probabilistic model in the next step. There are several methods to select individuals. Lima et al. (2007) investigated the influence of selection methods in EDAs and showed the more appropriate performance of the truncation selection method at keeping the interactions between decision variables. In this method, solutions are ordered according to the objective function values and some of the best individuals are selected based on truncation coefficient.

In the third step, induction of the $n$-dimensional probabilistic model among the individuals of the previous step that best reflects the interdependencies between decision variables is carried out. This step is known as the learning step. Proper display of interdependencies between variables is necessary for better evolution toward fitter solutions. EDAs are different based on applied probabilistic models. These include simple models like bivariate Gaussian to more complex models like Bayesian networks or copula models. After constructing the probabilistic model, in the next step, new individuals are generated by sampling from the probabilistic

![img-0.jpeg](img-0.jpeg)

Fig. 1. The general process of the estimated distribution algorithms (EDAs).
model. Notably, the learning and sampling are the most crucial steps in EDAs and will be discussed in detail in the following sections.
After sampling the new individuals, the new population is generated by using a replacement method. Replacement methods increase the diversity in the population by incorporating new individuals that are obtained in the current generation with the individuals of previous generation. Investigating the effect of replacement methods in EDAs, Lima et al. (2007) indicated the better performance of elitist replacement method when the truncation method is used to select promising solutions. In this method, individuals are ordered according to their fitness values and some of the worst individuals are replaced with the new individuals that are sampled from the probabilistic model. Finally, the mentioned process is repeated until a certain stopping criterion is verified. Similar to other optimization algorithms, several stopping criteria such as reaching a predetermined number of generations or number of objective function evaluations, uniformity of generated population can be used separately or combined.

As mentioned earlier the fundamental difference between EDAs and traditional algorithms lies in constructing (learning step) and sampling from a probabilistic model. In practice, decision variables of optimization problems are dependent. Some algorithms such as Mutual Information Maximization of Input Clustering (MIMIC) (De Bonet et al., 1997), Combining Optimizers with Mutual Information Trees (COMIT) (Baluja and Davies, 1997) and Binary Marginal Distribution Algorithms (BMDA) (Pelikan and Mühlenbein, 1998) consider the linear relationship of variables. In the last decade, many EDAs considering the multivariate dependence, such as Extended Compact Genetic Algorithm (ECGA) (Harik, 1999), Factorized Distribution algorithms (FDA) (Muhlenbein and Mahnig, 1999), Bayesian Optimization Algorithm (BOA) (Pelikan et al., 1999), Stochastic Hill Climbing with Learning by Vector of Normal Distribution (SHCLVND) (Rudlof and Köppen, 1997), Estimation of Multivariate Normal Algorithm (EMNA) (Larranaga et al., 2001) and Estimation of Gaussian Networks Algorithm (EGNA) (Larrañaga et al., 2000), are proposed. In practice, normal distribution has been commonly used to model the search distribution in EDAs due to its tractable properties (Bosman and Thierens, 2006).

However, in the application of multivariate normal distribution, all margins are assumed to have normal density and only linear correlation between the variables can be considered. These properties could lead to the construction of incorrect models of search space. For instance, the fitness landscape of multimodal objective functions cannot be properly presented by the multivariate normal distribution (Gonzalez-Fernandez and Soto, 2014).

Recently, Copula Theory (Sklar, 1959) is introduced into the framework of EDAs to tackle this problem. By using copulas, a multivariate joint distribution is decomposed into univariate margins and a function called copula that determines the dependence structure between the variables. EDAs based on copulas inherit these properties, and consequently, can build more flexible search distributions and overcome the limitations of a multivariate normal probabilistic model. In the copula-based EDA, which is proposed in this context, only the margins are estimated and the next generation is sampled from a copula and the inverse function of margins. The basic theorem and properties of copulas are briefly introduced in the following sections.

# 4. A brief introduction to copula theory 

Each random variable is fully described by its cumulative distribution function (CDF). However, CDFs do not provide information on the correlation structure between random variables. Copulas that are suitable tools for modeling this kind of dependency were first introduced by Sklar (1959) in the statistics and their applications have grown over the last years. Copulas are functions that describe the dependence structure of a set of random variables and connect multivariate distribution functions to their one-dimensional marginal distribution functions (Nelsen, 2006).

One of the main reasons for using copula functions is their possibility to define the structure of dependency between variables

independent of the selected marginal distribution functions. Hence, a large number of copulas have been introduced to capture different patterns of dependency among the random variables. Another reason is the possibility of studying scale-free measures of dependence between variables. In other words, the superiority of copulas for modeling dependence is because of their greater flexibility to the correlation coefficient approach. The linear correlation coefficient has a major flaw that is invariant under nonlinear transformation. However, the dependence criteria that are derived from copulas are able to overcome this problem. These features are suitable for modeling dependencies between variables in the car following models that often do not show a clear dependency between variables. With this brief overview in mind, it is now appropriate to give the definition of a copula function.

Definition.. an n-dimensional copula is a function $\mathrm{C}: \mathrm{I}^{\mathrm{n}} \rightarrow \mathrm{I}$ with the following properties (Jaworski et al., 2010).
(1) For every $u \in I^{n}$,

$$
C(u)=0 \text { if only one coordinate of } u \text { is } 0
$$

(2) For every $u \in I^{n}$

If all coordinates of $\mathbf{u}$ are 1 except $u_{k}$, then $C(u)=u_{k}$
(3) For every $u, v \in I^{n}$ with $u_{i} \leqslant v_{i}$

$$
\sum_{\left(u_{1}, \ldots, u_{n}\right) \in \mathcal{U}_{i=1}^{k}\left[u_{i}, v_{i}\right]}(-1)^{|i| u_{i}=u_{i} \mid} C\left(w_{1}, \ldots, w_{d}\right) \geqslant 0
$$

A function that satisfies the first condition is said to be grounded. Moreover, the third condition is the $n$-dimensional counterpart of a nondecreasing one-dimensional function.

The primitive Theorem of Sklar (1959) is the building block of copula theory. In a nutshell, it states that any multivariate probability distribution can be divided into its univariate margins and a copula. Conversely, connecting the margins and a given copula is equivalent to building a multivariate distribution. Accordingly, for each $n$-dimensional distribution of $\boldsymbol{F}$ with marginal distributions $F_{i}\left(x_{i}\right), \ldots, F_{n}\left(x_{n}\right)$ exists an $n$-dimensional copula $C$ such that for all $x=\left(x_{1}, \ldots, x_{n}\right)^{T} \in[-\infty, \infty]^{n}$ :

$$
\begin{aligned}
\boldsymbol{F}\left(x_{1}, \ldots, x_{n}\right) & =p\left(X_{1} \leqslant x_{1}, \ldots, X_{n} \leqslant x_{n}\right) \\
=\boldsymbol{C}\left(p\left(X_{1} \leqslant x_{1}\right), \ldots, p\left(X_{n} \leqslant x_{n}\right)\right) \\
& =\boldsymbol{C}\left(F_{1}\left(x_{1}\right), \ldots, F_{n}\left(x_{n}\right)\right)
\end{aligned}
$$

Concisely, one can derive a copula for any $n$-variable distribution by using Eq. (7). Especially when $F_{i}\left(x_{i}\right)$ is continuous for each $i=1, \ldots n$. In this case, the copula $C$ is unique and for any $u=\left(u_{1}, \ldots, u_{n}\right)^{T} \in[0,1]^{n}$ can be easily calculated using the inverse method as follows (Nelsen, 2006):

$$
\begin{aligned}
& \boldsymbol{C}\left(u_{1}, \ldots, u_{n}\right)=p\left(U_{1} \leqslant u_{1}, \ldots, U_{n} \leqslant u_{n}\right) \\
& =p\left(X_{1} \leqslant F_{1}^{-1}\left(u_{1}\right), \ldots, F_{n}^{-1}\left(u_{n}\right)\right) \\
& =\boldsymbol{F}\left(F_{1}^{-1}\left(u_{1}\right), \ldots, F_{n}^{-1}\left(u_{n}\right)\right)
\end{aligned}
$$

where $F_{i}^{-1}$ is the inverse function of $F$ and is determined as $F_{i}^{-1}\left(u_{i}\right)=\sup \left\{x \mid F_{i}(x) \leqslant u_{i}\right\}$. Therefore, copulas are essentially a way to convert $\left(X_{1}, \ldots, X_{n}\right)$ random vector to another random vector $\left(U_{1}, \ldots, U_{n}\right)=\left(F_{1}\left(X_{1}\right), \ldots, F_{n}\left(X_{n}\right)\right)$ having the uniform margins on $\mathrm{I}=[0,1]$ and preserving dependencies between components (Jaworski et al., 2010). It is worthy to note, by using Eq. (7) each copula can be combined with different univariate distribution functions in order to obtain the multivariate distribution function. This is actually one of the main advantages of the copula idea. Therefore, copulas can be used for modeling situations in which a different distribution function is necessary for each margin and it is a credible alternative to the classic multivariate distribution functions such as Gaussian, Gamma, and Pareto.

From the above definition, it can be derived that the conditions of the copula are very easy to satisfy. Hence, many functions can be considered as copulas. A rich set of copula types such as the elliptical and Archimedean class of copula, the Copula-GARCH, and the vine copula have been generated in the literature. However, in this paper, only a parametric family of copulas called elliptical copulas are discussed. Detailed surveys of families of copulas can be found in Nelsen (2006).

# 4.1. The elliptical family of copulas 

Elliptical copulas are one of the famous classes of copulas. These copulas are a rich source of multivariate distributions and have many properties of the multivariate normal distribution. Furthermore, they provide the possibility of modeling multivariate extremes distribution and other forms of non-normal dependency. Elliptical distributions are distributions whose density function (if it exists) has the general form of Eq. (9) (Nelsen, 2006).

$$
f(\mathbf{x})=|\Sigma|^{-\frac{1}{2}} g\left[(\mathbf{x}-\mu)^{T} \Sigma^{-1}(\mathbf{x}-\mu)\right], \quad x \in \mathrm{R}^{n}
$$

where $\mathbf{X}$ is an $n$-dimensional vector of random variables, $\sum$ is a symmetric non-negative definite matrix (dispersion), $\mu \in \mathrm{R}^{n}$ is location parameter, and $g$ is a $[0, \infty) \rightarrow[0, \infty)$ function (density generator).

![img-1.jpeg](img-1.jpeg)

Fig. 2. Scatterplot of samples from bivariate Gaussian copula functions with (a) strong positive dependence $\tilde{v}=0.90$, (b) very weak positive dependence $\tilde{v}=0.10$, (c) very weak negative dependence $\tilde{v}=-0.10$, (d) strong negative dependence $\tilde{v}=-0.90$.

If $g(\mathbf{x})=\frac{1}{2 \pi} \exp \left(-\frac{\mathbf{x}}{2}\right)$ is considered as the generator in Eq. (9), the multivariate Gaussian distribution is obtained and the relevant copula has the following functional form.

$$
\begin{aligned}
& \boldsymbol{C}_{\Sigma}\left(u_{1}, u_{2}, \ldots, u_{n}\right)=\Phi_{\Sigma}\left[\Phi^{-1}\left(u_{1}\right), \Phi^{-1}\left(u_{2}\right), \ldots, \Phi^{-1}\left(u_{n}\right)\right] \\
& =\boldsymbol{f}_{-\infty}^{\Phi^{-1}\left(u_{1}\right)} \boldsymbol{f}_{-\infty}^{\Phi^{-1}\left(u_{2}\right)}-\boldsymbol{f}_{-\infty}^{\Phi^{-1}\left(u_{n}\right)} \frac{1}{(2 \pi)^{n / 2} / \Sigma^{(1 / 2)}} \exp \left(-\frac{1}{2} \mathbf{W}^{T} \sum^{-1} \mathbf{W}\right) d \mathbf{W}
\end{aligned}
$$

where $\Phi_{\Sigma}$ is the multivariate standard normal distribution with zero mean and a positive semidefinite correlation matrix $\sum$, $\Phi(u)=\int_{-\infty}^{u} \frac{1}{x / 2 z} e^{-\frac{z^{2}}{2}} d t$ is the CDF of the standard normal distribution, $\Phi^{-1}(u)$ is the inverse of the univariate standard normal distribution function, and $\mathrm{W}=\left(w_{1}, w_{2}, \ldots, w_{n}\right)$. The Gaussian copula is a comprehensive copula which means it captures the full range of dependence between random variables. Considering two random variables the bivariate Gaussian copula $\mathrm{C}_{\tilde{v}}$ is defined as Eq. (11).

$$
C_{\tilde{v}}(u, v)=\Phi_{\Sigma}\left[\Phi^{-1}(u), \Phi^{-1}(v)\right]=\int_{-\infty}^{\Phi^{-1}(u)} \int_{-\infty}^{\Phi^{-1}(v)} \frac{1}{2 \pi \sqrt{1-\tilde{v}}} \exp \left(-\frac{s^{2}-2 \tilde{v} s t+t^{2}}{2\left(1-\tilde{v}^{2}\right)}\right) d s d t
$$

where $\Sigma=\left(\begin{array}{cc}1 & \tilde{v} \\ \tilde{v} & 1\end{array}\right)$ is the correlation matrix with $\tilde{v} \in[-1,1]$. Examples of bivariate Gaussian copula function with different correlation matrices can be seen in Fig. 2.

By considering $g(\mathbf{x})=\left(1+\frac{\mathbf{x}}{2}\right)^{-2+\nu}$ as a generator in Eq. (9), the multivariate t-Student distribution with degrees of freedom $v$ is obtained and the related copula is defined as Eq. (12).

$$
\begin{aligned}
& \boldsymbol{C}^{\prime}\left(u_{1}, u_{2}, \ldots, u_{n}\right)=t_{\Sigma, v}\left[t_{v}^{-1}\left(u_{1}\right), t_{v}^{-1}\left(u_{2}\right), \ldots, t_{v}^{-1}\left(u_{n}\right)\right] \\
& \quad=\boldsymbol{f}_{-\infty}^{\mathrm{v}_{v}^{-1}\left(u_{1}\right)} \boldsymbol{f}_{-\infty}^{\mathrm{v}_{v}^{-1}\left(u_{2}\right)} \ldots \boldsymbol{f}_{-\infty}^{\mathrm{v}_{v}^{-1}\left(u_{n}\right)} \frac{\Gamma\left(\frac{v+q}{2}\right)}{\Gamma\left(\frac{v}{2}\right) \sqrt{v v^{2} / 2 \pi}}\left(1+\frac{\mathbf{w}^{T} \Sigma^{-1} \mathbf{W}}{v}\right) d \mathbf{W}
\end{aligned}
$$

where $t_{\Sigma, v}$ is the multivariate standard t-student distribution parametrized by the correlation matrix $\Sigma$ and degrees of freedom $v, \Gamma$ is Gamma function, $\mathbf{W}=\left(w_{1}, w_{2}, \ldots, w_{n}\right)$. By considering bivariate distribution, the bivariate $t$ copula can be written in the form of Eq. (13).

$$
C_{\tilde{v}}(u, v)=t_{\Sigma}\left[t_{v}^{-1}(u), t_{v}^{-1}(v)\right]=\int_{-\infty}^{\mathrm{v}_{v}^{-1}(u)} \int_{-\infty}^{\mathrm{v}_{v}^{-1}(v)} \frac{1}{2 \pi \sqrt{1-\tilde{v}^{2}}}\left(1+\frac{s^{2}-2 \tilde{v} s t+t^{2}}{v\left(1-\tilde{v}^{2}\right)}\right)^{-s+2} d s d t
$$

In order to better understand the relationship between variables in t-Student and Gaussian copulas, heat map of the bivariate density function for each of them is shown in Fig. 3. In this order, marginal distribution functions are considered as normal and values initially have been calculated for a 100 in 100 network by using the mentioned copulas with a specific value of $\tilde{v}$, then these random values convert to normal random values by using integral transform.

It is worth noting that, a large variety of copulas with different dependence structures are formulated in literature in order to tie random variables. However, seeking simplicity, in this context a Gaussian copula has been applied. A comprehensive review of the copulas can be found in Nelsen (2006).

# 4.2. Estimation of copula probabilistic model and sampling new individuals (random variate generation) 

Similar to the EDAs, the two key steps in the copula-based EDA are the identification of the probabilistic model and a mechanism for sampling new candidate solutions from it. Given the copula C and random variables, the first step is to select appropriate marginal distribution for each random variable and transform the data onto the copula scale using probability integral transform. The next step is to estimate copula parameter $\tilde{v}$. Depending upon the marginal specifications, different parametric and nonparametric methods have been introduced in the literature. Generally, there are three methods which include full maximum likelihood method, sequential two-step maximum likelihood method, and the generalized method of moments to estimate a multivariate Gaussian copula. Assuming a non-parametric marginal distribution, namely an empirical distribution, there are no marginal parameters which need to be

![img-2.jpeg](img-2.jpeg)

Fig. 3. Bivariate elliptical copulas (a) Gaussian copula with $\tilde{v}=0.90$, (b) t-Student copula with $\tilde{v}=0.50, v=1$.
estimated. In such a configuration, rank-based estimators that are somehow a nonparametric adaptation of the method of moments are appropriate to estimate a Gaussian copula (Genest and Favre, 2007). A straightforward rank-based estimator is based on Spearman correlation coefficient. It is a nonparametric version of the Pearson product-moment correlation and measures the strength and direction of the association between two ranked variables. For a multivariate Gaussian copula, correlation matrix $\Sigma$ and the Spearman correlation coefficient have the relationship as follow (Genest and Favre, 2007):

$$
\rho_{\tilde{v}}=2 \sin \left(\frac{\pi}{6} \rho_{X_{i}, X_{j}}^{2}\right)
$$

where $\rho_{i, j}$ denote the element in the $i$ th row and $j$ th column of $\Sigma$, and $\rho_{X_{i}, X_{j}}^{2}$ is the Spearman correlation coefficient and for two variable instances $X_{i}=\left\{x_{i}^{(1)}, x_{i}^{(2)}, \ldots, x_{i}^{(n)}\right\}, X_{j}=\left\{x_{j}^{(1)}, x_{j}^{(2)}, \ldots, x_{j}^{(n)}\right\}$ is calculated by Eq. (15).

$$
\rho_{X_{i}, X_{j}}^{2}=1-\frac{6 \sum_{k=1}^{n} d_{k}^{2}}{n\left(n^{2}-1\right)}
$$

where $d_{k}=r_{x_{i}^{(k)}}-r_{x_{j}^{(k)}}$ is the difference between the two ranks of each observation, and $n$ is the number of observations. An attractive property of Eq. (16) is its invariance through monotonic transformation. In the Gaussian copula, since $\Phi(.)$, $F_{i}^{-1}($.$) are both monotonic, the rank vector of X_{i}$ is the same as the rank vector of $U_{i}$. This implies that the Spearman correlation coefficients are also similar (i.e. $\rho_{X_{i}, X_{j}}^{2}=\rho_{U_{i}, U_{j}}^{2}$ ). Accordingly, at each generation, the copula parameter $\Sigma$ can be computed simply and directly from selected individuals.

After constructing the copula model, the next task is sampling from this probabilistic model in order to generate new individuals. The following algorithm is used to draw $m$ samples from the Gaussian copula with the parameter $\Sigma$ and the marginal $F_{i}$ (Mai and Scherer, 2012):
(1) Compute the Cholesky decomposition of $\sum$, i.e. compute the matrix $A \in \mathbb{R}^{n \times n}$ with $A A^{T}=\sum$, where $A$ is a lower triangular matrix. Alternatively, one can compute $\sum^{1 / 2}$, where $\sum^{1 / 2} \sum^{1 / 2}=\sum$, and use it instead of $A$.
(2) Generate a vector of independent random variables from a uniform distribution. i.e. $\tilde{\mathbf{u}}=\left(\tilde{u}_{1}, \ldots, \tilde{u}_{n}\right), \tilde{u}_{i} \sim U(0,1)$
(3) Compute vector $\tilde{\mathbf{z}}$ by applying the inverse CDF of the standard normal distribution to each element of the vector $\tilde{\mathbf{u}}$. i.e. $\tilde{\mathbf{z}}=\left(\Phi^{-1}\left(\tilde{u}_{2}\right), \ldots, \Phi^{-1}\left(\tilde{u}_{n}\right)\right)$
(4) Compute $\tilde{\mathbf{z}}^{T}=\tilde{\mathbf{z}} \cdot A^{T}$. The result is a vector with normally correlated elements.
(5) Apply the CDF of the standard normal distribution to each element of the vector $\tilde{\mathbf{z}}^{T}$. i.e. $\tilde{\mathbf{z}}=\left(\Phi\left(\tilde{z}_{1}^{T}\right), \ldots, \Phi\left(\tilde{z}_{n}^{T}\right)\right)$
(6) Compute vector $\tilde{\mathbf{x}}$ by applying the transform of $F_{i}^{-1}($.$) to each element of the vector \tilde{\mathbf{v}}$ to obtain desired random sample. i.e. $\tilde{\mathbf{x}}=\left(F_{1}^{-1}\left(\tilde{v}_{1}\right), \ldots, F_{n}^{-1}\left(\tilde{v}_{n}\right)\right)$
(7) Repeat Steps 2 to 6 until m new samples are produced

# 5. Experiments setup 

Several experiments have been designed to evaluate the performance of the GA, CEM and the copula-based EDA. In this section, the applied trajectory data, the mechanism of generating noise-free and noise-contaminated data, how the calibration problem is configured, proposed performance indicators, and the configuration parameters of each algorithm have been explained.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Position (a), speed (b) and acceleration (c) profiles of the leader (vehicle ID 692) from NGSIM-US101 and the created synthetic follower by simulating IDM.

# 5.1. The data 

In this paper, high resolution trajectory data from the southern section of the US101 highway in Los Angeles, which is provided by the Cambridge Systematic in cooperation with Federal Highway Administration (FHWA, 2004) are used. Extracted Data through image processing include location, speed, acceleration, and type of vehicles in the period of 7:50 to 8:35 with a resolution of 0.1 s . Traffic flow was 8077 vehicles per hour with a combination of $97.0 \%$ car, $2.2 \%$ heavy vehicle, and $0.7 \%$ motorcycle.

Since extraction of vehicle trajectory is associated with errors and the noise domain is amplified in the calculation of speed and acceleration (Montanino and Punzo, 2015; Rafati Fard et al., 2017), in order to mitigate the disruptive effects of errors, the trajectory of vehicles has been modified by using two-step procedure proposed by Rafati Fard et al. (2017).

### 5.1.1. Generation of a synthetic trajectory

To investigate the performance of an algorithm in identifying the true value of parameters, knowing the ground truth of the parameters is crucial and as mentioned in the literature, using synthetic data is the only way to perform such assessment (Ciuffo and Punzo, 2014; Ossen and Hoogendoorn, 2008; Punzo et al., 2012).

Therefore, in this context, a synthetic trajectory data by simulating the IDM with values $[2,1.5,5,1.3,30,4]$ for $\left[a_{\max }, b_{\text {sens }}, c_{\text {sens }}, T^{*}, V^{*}, \delta\right]$ is generated. It should be noted that, in order to ensure that the synthetic trajectory is as similar to real trajectory as possible, the trajectory of leading vehicle is derived from the US101 dataset. Fig. 4 represents the position, speed, and acceleration profiles of the leader and follower. In addition, the considered search range of IDM parameters in the calibration process is presented in Table 1.

### 5.1.2. Generation of a noise-contaminated trajectory (optimization under uncertainty)

The presence of errors in the data is one of the sources of uncertainty in the calibration of microscopic traffic models. To evaluate the robustness of the calibration process to data errors when using copula-based EDA, the calibration process is repeated for a noisecontaminated trajectory. This trajectory is generated by considering additive noise to the positional locations of the follower. Usually, additive noise is assumed Gaussian with zero mean and $\sigma$ variance (Yaochu and Branke, 2005). However, analysis of residuals obtained from vehicle trajectory reconstruction is far from being normally distributed (Montanino and Punzo, 2015; Rafati Fard et al., 2017). Therefore, in order to preserve structure and domain of generated noise with the structure and domain of noise in NGSIM database, noise values are produced through sampling the empirical distribution of residuals (by using Monte Carlo sampling method) and added to the noise-free synthetic positional data. This empirical distribution is obtained in the process of trajectory reconstruction. Fig. 5 shows position, speed and acceleration of the original and noise-contaminated trajectory. It is necessary to mention that sampling from the empirical distribution leads to structure and domain of generated noise in the synthetic trajectory with the structure and domain of noise in NGSIM database being largely consistent.

### 5.1.3. Actual trajectory data

In order to investigate the ability of the copula-based EDA method in reproducing actual trajectories by identifying the parameters of IDM, we randomly select 685 leader-follower trajectory pairs from the US101 dataset and solve the calibration problem for each pair. These trajectories are selected so that they are affected at least by one shockwave and their travel times are longer than 60 s .

It should be pointed out, in the case of real trajectory data, the upper bound of parameters search range indicated in Table 1 are changed for $a_{\max }, b_{\max }, V^{*}$ and $\delta$ parameters to $10,10,70$ and 8 respectively, in order to not exclude possible solutions.

Table 1
The searching range of each parameter of IDM.

| Parameters | $a_{\max }\left(m / s^{2}\right)$ | $b_{\text {sens }}(m / s^{2})$ | $S_{\text {sens }}(m)$ | $T^{*}(s)$ | $V^{*}(m / s)$ | $\delta$ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Range | $[0.1,5]$ | $[0.1,7]$ | $[0.1,8]$ | $[0.1,3]$ | $[1,35]$ | $[0,6]$ |

![img-4.jpeg](img-4.jpeg)

Fig. 5. Position (a), speed (b) and acceleration (c) profiles of the original and noise-contaminated data.

# 5.2. Measure of performance and objective function 

On the one hand, car following models are not able to accurately reproduce driving behavior and on the other hand, field data to some extent include noises; therefore, the types of measure of performance and objective function can affect the calibration results. In this research, besides the investigation of copula-based EDA performance on the calibration problem, the effect of MOPs and GOFs in identifying the true values of parameters has been examined. Therefore, the speed and gap criteria as MOPs and three metrics, root mean square error (RMSE), mean absolute error (MAE) and Thiel's inequality (U) with the following functional form have been applied as GOFs in various configurations of the calibration problem:

$$
\begin{aligned}
& R M S E=\sqrt{\frac{1}{T} \sum_{i=1}^{T}\left(Y_{i}^{\text {meas }}-Y_{i}^{\text {sim }}\right)^{2}} \\
& M A E=\frac{1}{T} \sum_{i=1}^{T}\left|Y_{i}^{\text {meas }}-Y_{i}^{\text {sim }}\right| \\
& U=\frac{\sqrt{\frac{1}{T} \sum_{i=1}^{T}\left(Y_{i}^{\text {meas }}-Y_{i}^{\text {sim }}\right)^{2}}}{\sqrt{\frac{1}{T} \sum_{i=1}^{T}\left(Y_{i}^{\text {meas }}\right)^{2}}+\sqrt{\frac{1}{T} \sum_{i=1}^{T}\left(Y_{i}^{\text {sim }}\right)^{2}}}
\end{aligned}
$$

### 5.3. Algorithms setting

As mentioned earlier, for the purpose of comparison, performance of the copula-based EDA along with the benchmark genetic algorithm (GA) and the recently proposed algorithm named cross-entropy method (CEM) have been investigated, The CEM is a probabilistic optimization method and is originated by an adaptive variance minimization algorithm for estimating the probabilities of rare events (Beruvides et al., 2016). Without going into further details, in this context, the GA algorithm and the CEM have been implemented according to (Goldberg, 1989) and Zhong et al. (2016) respectively. The configuration parameters of each algorithm have been set as follow.

- For Copula-based EDA, population size is 30, maximum number of generations is 200, and the truncation coefficient is set to 0.5 .
- For GA, population size is 200, maximum number of generations is 500, recombination and mutation percentage are 0.75 and 0.25 respectively, the mutation rate is 0.05 , and the selection mechanism is stochastic universal sampling with a generation gap equal to 0.5 .
- For CEM, the number of samples generated in each iteration is set to 100, maximum number of iterations is set to 300, the smoothing parameter is only applied to the variance and is set to 0.35 , and the percentage of elite samples is set to 0.15 .

The performance of algorithms is highly dependent on the values of their parameters. These parameters are inherently dependent on the nature of the optimization problem and could have positive effect on the overall solution quality if chosen properly. In this paper, to obtain the best performance of applied algorithms in the calibration problem, parameters of algorithms have been determined by using the method of Grefenstette (1986). In this method, a genetic algorithm is applied to tune various parameters of optimization algorithms for efficiency.

### 5.4. Proposed performance indicators

In order to evaluate and compare the performance of the GA, CEM, and copula-based EDA in the calibration of microscopic traffic models, calibration process for each combination of MOP and GOF is done using synthetic noise-free and noise-contaminated trajectories. Since the applied algorithms are stochastic search methods, every run of them produces different results. Therefore, each

calibration experiment has been repeated 50 times by using different random seeds (a total of $3(\mathrm{GOF}) \times 2(\mathrm{MOP}) \times 3(\mathrm{Alg}) \times 2($ Clean \& Noisy data $) \times 50($ Replication $)=1800)$. This approach allows the performance of algorithms in dealing with local optima and uncertainty in finding the global solution to be evaluated (Punzo et al., 2012).

The mean values and standard deviation of the objective function (Eq. (19) and Eq. (20) respectively) and the average error of calibrated parameters (Eq. (21)) are considered to compare the accuracy of different configurations of the calibration problem to identify the true value of model parameters.

$$
\begin{aligned}
& \bar{f}\left(f^{G O F, M O P, A l g, T r j}\right)=\frac{1}{N} \sum_{t=1}^{N} f_{t}^{G O F, M O P, A l g, T r j} \\
& \sigma\left(f^{G O F, M O P, A l g, T r j}\right)=\sqrt{\frac{1}{N-1} \sum_{t=1}^{N}\left(f_{t}^{G O F, M O P, A l g, T r j}-f^{G O F, M O P, A l g, T r j}\right)^{2}} \\
& \Delta\left(\hat{\sigma}_{r o l}^{G O F, M O P, A l g, T r j}, \hat{\sigma}_{r o u l}\right)=\frac{1}{N} \sum_{t=1}^{N}\left(\left|\frac{\hat{\sigma}_{r o l}^{G O F, M O P, A l g, T r j}-\hat{\sigma}_{r o u l}}{\hat{\sigma}_{r o u l}}\right| \times 100\right)
\end{aligned}
$$

where $\bar{f}(.), \sigma(),, \Delta($.$) are respectively mean, standard deviation of fitness value, and mean percentage error by considering$ $G O F \in[R M S E, M A E, U]$ as an objective function, $M o P \in[$ Speed, Gap $]$ as a measure of performance, $A \lg \in[G A, C E M, C o p u l a-E D A]$ as a solution algorithm, $\operatorname{Trj} \in[$ Clean, Noisy $]$ as a trajectory, $\hat{\sigma}_{r o t}$ as the estimated value of model parameters, and $\hat{\sigma}_{r o u l}$ as the original value of model parameters (considered to produce the synthetic trajectory).

The indicators above show to some extent the ability of GA, CEM, and copula-based EDA algorithms to solve the calibration problem. However, the frequency of finding the original values of each parameter with error of $\pm 1 \%$ is considered as an indicator to analyze the reliability and the ability of the algorithms to identify solutions in the close neighborhood of the global solution, as well as the ability to rediscover the original values in various iterations with different random seeds.

Another problem in the calibration process is associated with the efficiency of the applied algorithms. Efficiency refers to the usage rate of resources in finding appropriate solutions, which is very important in problems with expensive evaluation of the objective function. In the calibration of microscopic traffic models, since each simulation procedure consumes a certain time cost which is vastly in excess of that required to organize the search, an algorithm is more efficient, if it searches fewer solution on average (i.e. fewer number of function evaluations) to find the global optimal solution than all of its competitors. Therefore, in this context number of objective function evaluations (NFE) is intended as an indicator to evaluate the efficiency.

It should be noted that, when using real trajectory data, the global optimal solution is unknown. In this case, the cumulative distribution function (CDF) of GOF values (MAE) after a certain number of objective function evaluations has been used as an indicator to compare the efficiency of algorithms.

# 6. Results 

Table 2 indicates the results of GA, CEM and copula-based EDA application in different calibration configurations of the IDM. As can be seen, using all three algorithms leads to acceptable results. However, applying the copula-based EDA algorithm compared with genetic algorithm and cross-entropy method has led to significant improvement in the calibration results in terms of accuracy in identifying the true values of parameters and recognition of these values in different iterations. For example, mean percentage error as an indicator to assess the accuracy of the different configurations of calibration, when the copula-based EDA algorithm is applied, varies between 0 and 0.67 percent. While the range of the mentioned indicator by using GA and CEM is between 0.01 and 11.67 and 0 and 7.51 percent respectively. In addition, when using the GA and CEM as optimization algorithms, the calibration results are more sensitive to the selected measure of performance and objective function. Various combinations of MOPs and GOFs to some extent lead to different results. For instance, when RMSE is considered as GOF, only by changing MOP from speed to the gap, the mean percentage error in identification of the true value of the parameter $V^{\prime}$ increased from $3.67 \%$ to $10.55 \%$ and from $4.66 \%$ to $11.81 \%$ for GA and CEM respectively.

Using the copula-based EDA algorithm, calibration results for different combinations of MOPs and GOFs, to a large extent, are similar to each other. This means that the calibration process of microscopic traffic models by using the copula-based EDA as solution algorithm is more robust to the type of measure of performance and goodness of fit criteria.

Evolutionary algorithms are affected by random numbers from creation of the first generation to application of their operators for creating the new populations. This randomization is used inclusively in evolutionary algorithms. One interpretation of the robustness of an algorithm relates to the performance variation of it over different runs - with different random seeds- in the same instance (Talbi, 2009). High frequency in identifying the original values of parameters with error of $\pm 1 \%$ by using the copula-based EDA in various configurations of calibration shows its independence to different random seeds and its robustness in finding the optimal solution. The original values of parameters for any combination of MOPs and GOFs in EDA have been identified in 94-100 percent of iterations. However, these values are between 4 and 100 and 6 and 100 percent of iterations for GA and CEM, respectively.

As shown in Table 2, regardless of the type of intended calibration configuration, frequency of identifying the original value of parameters and the mean percentage error between the estimated and original values for the $V^{\prime}$ and $\delta$ parameters compared to other parameters of IDM are clearly different. When using GA and CEM, this difference is more pronounced. One reason is that in this study, the parameter $\delta$ is intended as one of the necessary parameters for calibration in contrast to previous similar studies (Zhong et al.,

![img-5.jpeg](img-5.jpeg)

2016). On the one hand, this leads to increase in the dimensionality of the search space and on the other hand, leads to a complex interaction between $\delta$ and the desired speed $\left(V^{*}\right)$ and, consequently, makes it more difficult to search for the optimal solution. Another reason could be related to insufficient information in synthetic data to determine the true values of these parameters which are considered as incompleteness (Treiber and Kesting, 2013a). However, since both of the optimization algorithms use the same data, the latest cause is not important and the main problem is the dependency among parameters. If there is a correlation between parameters, small changes and even in some cases, big changes in the values of these parameters could lead to obtaining the same values of the objective function. In other words, this dependency may lead to the creation of several global optima. In GA and CEM, these interactions between parameters are not explicitly considered and operators of GA may have disruptive effects on these interactions. However, in the copula-based EDA, learning and sampling from a copula function of the best individuals of the population in each generation, dependency between variables, especially $V^{*}$ and $\delta$, are explicitly and effectively captured and exploited (Larranaga and Lozano, 2002).

Calibration of microscopic traffic models is usually done by using trajectory data. Regardless of the collection method, trajectory data is more or less associated with errors. These errors may severely affect the results of calibration (Montanino and Punzo, 2015; Ossen and Hoogendoorn, 2008). Filtering and reconstructing the trajectory data are appropriate ways to reduce the adverse effects of errors in identifying parameters of models (Monteil et al., 2014; Treiber and Kesting, 2013a). Another alternative as mentioned by Treiber and Kesting (2013a) is to use global calibration approaches instead of local approaches in the calibration of microscopic traffic models. The use of optimization algorithms that are less sensitive to noise is another approach that is rarely mentioned in the literature.

Table 3 demonstrates the calibration results of IDM by using GA, CEM and the proposed algorithm in the presence of noise. As expected, the presence of noise in data affects all performance criteria, which were intended for comparison purposes. Different configurations exhibit different performance for identification of parameters in the presence of noise. In general, the minimum distance at the standstill situation $\left(\bar{\tau}_{\text {min }}^{*}\right)$ and the desired time gap $\left(T_{n}^{*}\right)$ were better identified in comparison with other parameters.

One reason for decreasing efficiency of algorithms in identifying the original values of parameters, as mentioned by Ossen and Hoogendoorn (2008), is the presence of noise in data which decreases the sensitivity of the objective function to variation in the values of parameters. Therefore finding true values becomes more difficult. Fig. 6 shows this sensitivity reduction of the objective function. In this figure, contour plots of RMSE as an objective function from the sensitivity analysis with parameters maximum acceleration and comfortable deceleration (values of other parameters were considered as the original value), when the gap is considered as MOP, for noise-free and noise-contaminated data are drawn. It demonstrates how errors in trajectory data affect the value of the objective function and change the structure of search space. Consequently, a wide range of solutions could lead to the same value of the objective function. It should be noted that the effect of the errors to identify the original values of the parameters for additional trajectories is also investigated but is not mentioned to meet briefness. However, investigations demonstrate that the impact of measurement errors on the calibration results is greater when the driving behavior of the leader is too soft. In such cases, small amounts of noise might bring about incorrect identification of parameters in all of the three algorithms. This finding is in agreement with the previous study reported by Monteil et al. (2014).

One of the findings in this study is the better performance of Mean Absolute Error (MAE) as the goodness of fit over the other GOFs in noisy data. Specifically, when copula-based EDA and gap are considered as MOP and solution algorithm. In this case, as can be seen, the probability of finding the true value of parameters by using copula-based EDA is higher in comparison to GA and CEM. This could be accidental and true only for this noisy trajectory. Hence, in order to have a more accurate investigation, 50 other synthetic noisy trajectories have been made by the mentioned method and IDM's parameters were calibrated using these trajectories. In almost all cases, using this configuration (MAE, gap and Copula-based EDA as GOF, MOP, and solution algorithm respectively) leads to having better results compared with the other calibration configurations.

One reason for the better performance of MAE criterion over the RMSE could be the basic assumption used in the RMSE criterion. In this error metric, it is expected that distribution of errors is Gaussian. In this study, unlike previous research (Ciuffo and Punzo, 2014; Ossen and Hoogendoorn, 2008) that errors were created by the assumption of being normal, noisy trajectory data have been created using empirical distribution of residues that was obtained from the process of trajectory reconstruction. However, the analysis of the residuals demonstrates the non-normality distribution of errors. One more reason is the less sensitivity of MAE to large errors compared to RMSE. The criteria that are based on the square error exert more weight to large errors. When calibration is performed using noise-free data, assigning greater penalties for larger errors seems appropriate. Whereas when using the noise-contaminated data, the occurrence of occasionally big errors could be due to the existing noise in data and thus, giving more weight to these errors could lead the algorithms to produce incorrect value of decision variables in order to reduce the amount of mentioned errors. In other words, MAE leads to better robustness since it is less sensitive to outliers.

Regardless of the type of goodness of fit and the solution algorithm, the calibration configurations with the gap as MOP shows better performance in comparison with the speed in the process of identifying model parameters by using noise-contaminated data. The main reason is the increasing noise domain in the trajectory data, which is caused by numerical differentiation and thus the sensitivity of the objective function to the original values of the parameters is further reduced.

The efficiency of algorithms is of importance because solving some optimization problems is considerably expensive. It can be due to the high cost of evaluating the objective function (for example, every run of microsimulation of medium or large-scale networks may take several hours) or the very high dimensionality of the problem (for example, a large number of local and global parameters in traffic microsimulation software). In this case, algorithms that conduct better solutions by using fewer numbers of simulation runs are more desirable. To evaluate the efficiency of the optimization algorithms used for solving the calibration problem in terms of utilization of resources, the average changes of the best value of objective function in different iterations (iterations with different

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

Fig. 6. Contour plots showing details of the objective function (around the minimum RMSE values) from the sensitivity analysis with parameters maximum acceleration $\left(a_{\max }\right)$ and comfortable deceleration $\left(b_{\text {comf }}\right)$. (a) noise-free data. (b) noise-contaminated data.
random seeds) versus the number of objective function evaluations (the number of performed simulations) have been shown in Fig. 7.
Evidently, besides the accuracy, the main advantage of copula-based EDA to GA and CEM is faster convergence rate which leads to lowering the number of simulation runs required to identify the original values of the model parameters. For example, for a 1000 evaluation of the objective function, the values of the RMSE for GA, CEM and copula-based EDA are in the order of $10^{-1}, 10^{-1}$ and $10^{-2}$ respectively. In addition, the final amount of RMSE when using a genetic algorithm after about one hundred thousand simulation runs is of the order of $10^{-3}$, whereas when using copula-based EDA, the final amount has the order of $10^{-5}$ and this amount is obtained using only about 6000 simulations. As can be seen in Fig. 7b, when using a noise-contaminated data in the calibration of IDM, all algorithms converge to the same value of the objective function. However, the convergence rate when using copula-based EDA is much higher. Note that the difference in the starting and final point of the diagrams is due to the existing differences in the population size and maximum number of generations of the solution algorithms.

In order to have a better assessment of calibration results, the convergence of model parameters for the noise-free data and noisecontaminated ones have been depicted in Figs. 8 and 9 respectively. The charts with respect to MAE as the objective function and gap as a measure of performance are plotted. Most of the parameters in all three algorithms (except the $\delta$ and $V^{\prime}$ parameters when using the GA and CEM) converge to the original values.

Apparently, the rate of convergence to the original values of the parameters when using Copula-based EDA as the solution algorithm is much higher than the others. By means of CEM and GA, $a_{\max }, b_{\text {comf }}, S_{\text {jam }}$ and $T^{*}$ parameters approach the original values after about three to twenty thousand objective function evaluations. While using the proposed algorithm, the original values of
![img-8.jpeg](img-8.jpeg)

Fig. 7. The convergence rates of GA, CEM and copula-based EDA in solving the calibration problem with respect to RMSE as the objective function, when the gap is considered as the measure of performance. (a) noise-free, (b) noise-contaminated data. NFE indicates the number of objective function evaluations.

![img-9.jpeg](img-9.jpeg)

Fig. 8. The convergence rates of the GA, CEM and copula-based EDA with respect to model parameters when MAE and gap are considered as GOF and MOP respectively, using noise-free data.
![img-10.jpeg](img-10.jpeg)

Fig. 9. The convergence rates of the GA, CEM and copula-based EDA with respect to model parameters when MAE and gap are considered as GOF and MOP, respectively, using noise-contaminated data.
parameters are identified by running the simulation only about 1000 times.
Notwithstanding, identifying the $\delta$ and $V^{*}$ parameters in all three algorithms is slightly different and the convergence rate of these parameters when using copula-based EDA is about one-second to one-third of the others. While using GA and CEM, the mentioned parameters converge to the false values. Low sensitivity of the objective function to the changes of these parameters is the main reason behind the difficulty of the algorithms in identifying the original values of these parameters. In the generated synthetic trajectory, the subject vehicle has been in the state of car following and then, the second term in Eq. (2) is negligible. In other words, with regard to the values intended for $\delta$ and parameters $V^{*}(\delta=4$ and $V^{*}=30)$, the effective domain of this term on the anticipated acceleration, would vary between 0 and 0.02 of maximum acceleration of the vehicle $\left(a_{\max }\right)$ which is very low. On the other hand, the interaction between these two parameters also makes the searching conditions more difficult.

![img-11.jpeg](img-11.jpeg)

Fig. 10. Contour plots showing details of the objective function (around the minimum RMSE values) from the sensitivity analysis with parameters $\delta$ and $V^{*}$, (a) noise-free data, (b) noise-contaminated data.

Fig. 10 demonstrates the variations of RMSE as an objective function with respect to $\delta$ and $V^{*}$. Obviously, the existing noise in data has a strong influence on the sensitivity of the objective function to variations of these two parameters. In all evaluated calibration configurations except the configuration in which MAE is used as the objective function, gap as MOP, and copula-based EDA as the solution algorithm, the two mentioned parameters converge to false values when the noise-contaminated data are used. It is important to highlight that in applying noise-contaminated data in the calibration process, averaging the estimated values of parameters in different replications of solution algorithm to some extent, can reduce the disruptive effects of noise and improve the quality of estimated parameters.

Fig. 11 shows the variation of the objective function in different replications of all three algorithms with different random seeds (blue lines) along with their average variations (red line). In the use of copula-based EDA, all runs had appropriate performance leading to the identification of the original values of the parameters. Evidently, a limited number of runs (three cases) have somewhat different performances over the others. These runs have the highest impact on the average values. However, as can be seen, the final values of the objective function (MAE) in different replications, for GA and CEM mostly are in the order of $10^{-3}$ and $10^{-4}$ respectively, whereas in the use of copula-based EDA, the final values of MAE in most runs are in the order of $10^{-7}$. This indicates that the proposed algorithm is more accurate than the other ones.

While using synthetic data makes sense from the perspective of having the ground truth, it is necessary to investigate the performance of the proposed algorithm in calibration with real trajectory data. Accordingly, 685 leader-follower pairs are chosen from US101 dataset to assess the performance of GA, CEM, and copula-based EDA in real traffic conditions. Fig. 12 indicates the cumulative distribution function of MOP values (MAE) after a specific number of function evaluations (NFE) with the two-sample Kol-mogorov-Smirnov test results and p-values presented at the top of each plot. the Kolmogorov-Smirnov has been used to verify the difference between CDFs. As can be seen in Fig. 12f, eventually after a large number of NFE especially for GA and CEM, all of three algorithms reach to similar values of MAE. It is not surprising because these algorithms have been proven to be global in the literature. However, as it is obvious in Fig. 12a-e, for a similar NFE, the performance of the proposed algorithm is more appropriate than others. When applying copula-based EDA, the related CDF of MAE values is always on the left side of CDFs obtained by GA and CEM. In other words, the proposed algorithm can find the global optimum with lower cost (fewer NFE) in calibration problem
![img-12.jpeg](img-12.jpeg)

Fig. 11. The variations of MAE as an objective function (run with different random seeds) along with their average when considering gap as MOP, (a) GA, (b) CEM, (c) copula-based EDA.

![img-13.jpeg](img-13.jpeg)

Fig. 12. The cumulative distribution function of MAE after a specific number of function evaluations (NFE).
compared with other ones.
Fig. 13 demonstrates the distribution of calibrated parameters. Three algorithms give comparable results. As can be perceived, regardless of the type of solution algorithm, in some cases the estimated parameters hit the specified boundaries. This may be due to the fact that use of single vehicle trajectory is not sufficient for estimating all parameters. For instance, some trajectory data are related to congestion condition and do not contain free flow traffic regime which is required to estimate the desired speed. In some others, there are not sufficient data from approaching regime to calibrate the desired deceleration. This lack of information in trajectory data is regarded as data incompleteness in the literature and have negative effects on the reliability of estimated parameters (Ossen and Hoogendoorn, 2009a; Treiber and Kesting, 2013b). In order to address such problem, as shown by Hoogendoorn and Hoogendoorn (2010) using multiple trajectory data simultaneously can improve the calibration results. Another method is to restrict the calibration to parameters that are relevant to the dataset (Treiber and Kesting, 2013a).

Another reason to explain why some of the estimated parameters reach to their specified boundaries may also be related to the limits of the predictive power of IDM. That means while IDM best reproduce actual trajectories for some individuals, it is partially able to reproduce driving style (actual trajectory) for others. In other words, individual drivers have different driving style, which is regarded as inter-driver differences in the literature, and satisfactory modeling of them requires various car following models (Ossen et al., 2006; Treiber and Kesting, 2013b).

It is worthy to note that, when the objective function of calibration problem is smooth and unimodal, simpler deterministic approaches such as the method of gradient descent or Levenberg-Marquardt algorithm have satisfying performance. However, when the complexity of the objective function is high (e.g. calibration with multiple vehicle trajectories, calibration of stochastic models) and there is a jagged objective function landscape with many local optima, any deterministic method is bound to get stuck in local optima. Therefore, it is necessary to use stochastic optimization techniques such as the one proposed in this paper to increase the probability of escaping from local optima and locate a good near-global optimum.

# 7. Conclusion and future study 

Calibration is one of the most important steps in the development of the microscopic traffic models. Different configurations of the calibration problem lead to different results. In this study, the major focus is on solution algorithm of the calibration problem. However, the effect of different objective functions and measure of performances is also evaluated. The results show that the performance of the GA and CEM are not satisfying. One of the limitations of these algorithms is the lack of considering the interactions between variables. This leads to increasing the cost (a large number of simulations) in identifying the original values of the model parameters. The importance of this issue is more obvious when the evaluation cost of the objective function (for example, medium and large-scale microsimulation models) is high. As an alternative, in this study, the copula-based EDA is used to solve the calibration problem. The most important difference between copula-based EDA and GA is the lack of recombination and mutation operators. In

![img-14.jpeg](img-14.jpeg)

Fig. 13. Distribution of IDM parameters.

the proposed algorithm, these operators are replaced with constructing and sampling from a copula-based probabilistic model of promising candidate solutions. This probabilistic model provides the possibility of considering the interaction between different variables.

In order to evaluate the performance of the proposed algorithm, calibration is carried out with different configurations by using synthetic and real trajectory data. The calibration results show more accuracy of the proposed algorithm to identify the original values of parameters, and its robustness to the type of objective function, type of measure of performance and different random seeds in comparison with GA and CEM. The main advantage of copula-based EDA over GA and CEM is less resource consumption in order to identify the true values of parameters. Considering the number of simulation runs (number of objective function evaluations) as a measure of resource usage, shows that convergence rate of the proposed algorithm to the true values of parameters is far greater than GA and CEM. These findings are also true when the real trajectory data are put to use. Another finding is the better performance of mean absolute error as the goodness of fit compared with the root mean square error and $U$ inequality in the presence of noise in data.

In this article, we just tried to explore implications of the copula-based EDA algorithm for calibrating microscopic traffic model. However, it is interesting to use more sophisticated copula models such as copula Vine for calibration of medium to large-scale microscopic simulation models, where a large number of highly interacted parameters require adjustment, and mining probabilistic models that are learned by copula-based EDA to reveal new information about the calibration problem structure. Furthermore, it can be applied in the parameter sampling of microscopic traffic simulation models to preserve structural dependency between parameters.

# Acknowledgments 

The authors would like to thank Traffic Research Laboratory of Iran University of Science and Technology (IUST-TRL) for hardware and software support.

## References

Armañanzas, R., Inza, I., Santana, R., Saeys, Y., Flores, J.L., Lozano, J.A., Peer, Y.V.d., Blanco, R., Robles, V., Bielza, C., Larrañaga, P., 2008. A review of estimation of distribution algorithms in bioinformatics. BioData Min. 1 (1), 1-12. https://doi.org/10.1186/1756-0381-1-6.
Balakrishna, R., Antoniou, C., Ben-Akiva, M., Koutsopoulos, H., Wen, Y., 2007. Calibration of microscopic traffic simulation models: methods and application. Transport. Res. Re.: J. Transport. Res. Board (1999) 198-207.
Baluja, S., Davies, S., 1997. Using Optimal Dependency-Trees for Combinatorial Optimization: Learning the Structure of the Search Space. DTIC Document.
Bando, M., Hasebe, K., Nakayama, A., Shibata, A., Sugiyama, Y., 1995. Dynamical model of traffic congestion and numerical simulation. Phys. Rev. E 51 (2), 1035-1042. https://doi.org/10.1103/PhysRevE.51.1035.
Barceló, J., 2011. Fundamentals of Traffic Simulation. Springer.
Beruvides, G., Quizá, R., Haber, R.E., 2016. Multi-objective optimization based on an improved cross-entropy method. A case study of a micro-scale manufacturing process. Inf. Sci. 334-335, 161-173. https://doi.org/10.1016/j.ins.2015.11.040.
Bosman, P.A.N., Thierens, D., 2006. Numerical Optimization with Real-Valued Estimation-of-Distribution Algorithms. In: Pelikan, M., Sastry, K., CantúPaz, E. (Eds.), Scalable Optimization via Probabilistic Modeling. Springer, Berlin Heidelberg, Berlin, Heidelberg, pp. 91-120.
Brackstone, M., McDonald, M., 1999. Car-following: a historical review. Transport. Res. F: Traffic Psychol. Behav. 2 (4), 181-196. https://doi.org/10.1016/s1369-8478(00)00005-x.
Brockfeld, E., Kühne, R., Wagner, P., 2004. Calibration and validation of microscopic traffic flow models. Transport. Res. Rec.: J. Transport. Res. Board 1876, 62-70. https://doi.org/10.3141/1876-07.
Chakroborty, P., Kikuchi, S., 1999. Evaluation of the general motors based car-following models and a proposed fuzzy inference model. Transport. Res. C: Emerg. Technol. 7 (4), 209-235. https://doi.org/10.1016/S0968-090X(99)00020-0.
Chandler, R.E., Herman, R., Montroll, E.W., 1958. Traffic dynamics: studies in car following. Oper. Res. 6 (2), 165-184. https://doi.org/10.1287/opre.6.2.165.
Chong, L., Abbas, M.M., Flintsch, A.M., Higgs, B., 2013. A rule-based neural network approach to model driver naturalistic behavior in traffic. Transport. Res. C: Emerg. Technol. 32, 207-223. https://doi.org/10.1016/j.trc.2012.09.011.
Ciuffo, B., Punzo, V., 2014. 'No Free Lunch' theorems applied to the calibration of traffic simulation models. IEEE Trans. Intell. Transp. Syst. 15 (2), 553-562. https:// doi.org/10.1109/itis.2013.2287720.
Ciuffo, B.F., Punzo, V., 2010. Verification of traffic micro-simulation model calibration procedures: analysis of goodness-of-fit measures. Transport. Res. Board 89th Ann. Meet.
Colombaroni, C., Fusco, G., 2014. Artificial neural network models for car following: experimental analysis and calibration issues. J. Intel. Transport. Syst. 18 (1), 5-16. https://doi.org/10.1080/15472450.2013.801717.
De Bonet, J.S., Isbell, C.L., Viola, P., 1997. MIMIC: Finding optima by estimating probability densities. Adv. Neural Inform. Process. Syst. 424-430.
DLR, 2018. SUMO 0.32.0 user manual. Germany.
Dowling, R., Skabardonis, A., Alexiadis, V., 2004. Traffic analysis toolbox volume III: guidelines for applying traffic microsimulation modeling software.
FHWA, 2004. NGSIM—Next Generation SIMulation.
Fritzsche, H.-T., 1994. A model for traffic simulation. Traffic Eng. Control 35 (5), 317-321.
Gazis, D.C., Herman, R., Rothery, R.W., 1961. Nonlinear follow-the-leader models of traffic flow. Oper. Res. 9 (4), 545-567. https://doi.org/10.1287/opre.9.4.545.
Genest, C., Favre, A.-C., 2007. Everything you always wanted to know about copula modeling but were afraid to ask. J. Hydrol. Eng. 12 (4), 347-368.
Gipps, P.G., 1981. A behavioural car-following model for computer simulation. Transport. Res. B: Methodol. 15 (2), 105-111. https://doi.org/10.1016/0191-2615(81) 90037-0.

Goldberg, D., 1989. Genetic Algorithms in Search, Optimization and Machinn Learning. Addison-Wesley Longman Publishing Co., Inc.
Gonzalez-Fernandez, Y., Soto, M., 2014. Copulaedae: An R package for estimation of distribution algorithms based on copulair. J. Stat. Softw. 58 (699).
Grefenstette, J., 1986. Optimization of control parameters for genetic algorithms. IEEE Trans. Syst. Man Cybernet. 16 (1), 122-128. https://doi.org/10.1109/tsmc. 1986.289288.

Hale, D.K., Antoniou, C., Brackstone, M., Michalaka, D., Moreno, A.T., Parikh, R., 2015. Optimization-based assisted calibration of traffic simulation models. Transport. Res. C: Emerg. Technol. 55, 100-115.
Hamdar, S.H., Mahmassani, H.S., Treiber, M., 2015. From behavioral psychology to acceleration modeling: calibration, validation, and exploration of drivers' cognitive and safety parameters in a risk-taking environment. Transport. Res. B: Methodol. 78, 32-53. https://doi.org/10.1016/j.trb.2015.03.011.
Harik, G., 1999. Linkage learning via probabilistic modeling in the ECGA. Urbana 51 (61), 801.
Helbing, D., Tilch, B., 1998. Generalized force model of traffic dynamics. Phys. Rev. E 58 (1), 133-138. https://doi.org/10.1103/PhysRevE.58.133.

Helly, W., 1961. Simulation of bottlenecks in single-lane traffic flow. In: Proceedings of the Symposium on Theory of Traffic Flow.
Hollander, Y., Liu, R., 2008. The principles of calibrating traffic microsimulation models. Transportation 35 (3), 347-362. https://doi.org/10.1007/s11116-007-9156-2.
Hoogendoorn, S., Hoogendoorn, R., 2010. Genetic calibration framework for joint estimation of car-following models by using microscopic data. Transport. Res. Rec: J. Transport. Res. Board 2188, 37-45. https://doi.org/10.3141/2188-05.

Hoogendoorn, S.P., Ossen, S., 2005. Parameter estimation and analysis of car-following models. Transportation and Traffic Theory. Flow, Dynamics and Human Interaction. 16th International Symposium on Transportation and Traffic Theory.
Jaworski, P., Durante, F., Härdle, W.K., Rychlik, T., 2010. Copula theory and its applications: proceedings of the workshop held in Warsaw, 25-26 September 2009. Springer Science \& Business Media.
Jin, P.J., Yang, D., Ran, B., 2014. Reducing the error accumulation in car-following models calibrated with vehicle trajectory data. IEEE Trans. Intell. Transp. Syst. 15 (1), 148-157. https://doi.org/10.1109/itis.2013.2273872.
Kesting, A., Treiber, M., 2008. Calibrating car-following models by using trajectory data: methodological study. Transport. Res. Rec.: J. Transport. Res. Board 2088, $148-156$. https://doi.org/10.3141/2088-16.
Khodayari, A., Ghaffari, A., Braunstingl, R., Alimardani, F., Kazemi, R., 2014. Improved adaptive neuro fuzzy inference system car-following behaviour model based on the driver-vehicle delay. IET Intel. Transport Syst. 8 (4), 323-332. https://doi.org/10.1049/irt-its.2012.0111.
Kikuchi, S., Chakraborty, P., 1992. Car-following model based on fuzzy inference system. Transport. Res. Rec.: J. Transport. Res. Board 1365.
Kim, J., Mahmassani, H., 2011. Correlated parameters in driving behavior models. Transport. Res. Rec.: J. Transport. Res. Board 2249, 62-77. https://doi.org/10. $3141 / 2249-09$.
Kometani, E., Sasaki, T., 1959. A safety index for traffic with linear spacing. Oper. Res. 7 (6), 704-720. https://doi.org/10.1287/oper.7.6.704.
Koutsopoulos, H.N., Farah, H., 2012. Latent class model for car following behavior. Transport. Res. B: Methodol. 46 (5), 563-578. https://doi.org/10.1016/j.trb.2012. 01.001.

Krauß, S., Wagner, P., Gawron, C., 1996. Continuous limit of the Nagel-Schreckenberg model. Phys. Rev. E 54 (4), 3707. https://doi.org/10.1103/PhysRevE.54.3707. Larrafaga, P., Etxeberria, R., Lozano, J.A., Peña, J.M., 2000. Optimization in continuous domains by learning and simulation of Gaussian networks.
Larranaga, P., Lozano, J., Bengoetxea, E., 2001. Estimation of distribution algorithms based on multivariate normal and Gaussian networks. Technical Report EHU-KZAA-JK-1.
Larranaga, P., Lozano, J.A., 2002. Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Springer Science \& Business Media.
Lima, C.F., Pelikan, M., Goldberg, D.E., Lobo, F.G., Sastry, K., Hauschild, M., 2007. Influence of selection and replacement strategies on linkage learning in BOA. In: 2007 IEEE Congress on Evolutionary Computation, pp. 1083-1090.
Liu, B., Fan, Y., Liu, Y., 2015. A fast estimation of distribution algorithm for dynamic fuzzy flexible job-shop scheduling problem. Comput. Ind. Eng. 87, 193-201. https://doi.org/10.1016/j.cie.2015.04.029.
Mai, J.-F., Scherer, M., 2012. Simulating Copulas: Stochastic Models, Sampling Algorithms, and Applications. Imperial College Press.
McTrans, 2014. TSIS-CORSIM Overview.
Montanino, M., Punzo, V., 2015. Trajectory data reconstruction and simulation-based validation against macroscopic traffic patterns. Transport. Res. B: Methodol. 80, 82-106. https://doi.org/10.1016/j.trb.2015.06.010.
Monteil, J., Billot, R., Sau, J., Buisson, C., El Faouzi, N.-E., 2014. Calibration, estimation, and sampling issues of car-following parameters. Transport. Res. Rec.: J. Transport. Res. Board 2422, 131-140. https://doi.org/10.3141/2422-15.
Mühlenbein, H., Malung, T., 1999. Convergence theory and applications of the factorized distribution algorithm. CIT. J. Comput. Inform. Technol. 7 (1), 19-32.
Mühlenbein, H., Paaß, G., 1996. From recombination of genes to the estimation of distributions I. Binary parameters. International Conference on Parallel Problem Solving from Nature. Springer Berlin Heidelberg, Berlin, Heidelberg, pp. 178-187.
Nagel, K., Schreckenberg, M., 1992. A cellular automaton model for freeway traffic. J. Phys. I 2 (12), 2221-2229. https://doi.org/10.1051/jp1:1992277.
Nelsen, B.B., 2006. An Introduction to Copulas. Springer Science \& Business Media.
Newell, G.F., 1961. Nonlinear effects in the dynamics of car following. Oper. Res. 9 (2), 209-229. https://doi.org/10.1287/opre.9.2.209.
Ossen, S., Hoogendoorn, S., 2009a. Reliability of parameter values estimated using trajectory observations. Transport. Res. Rec.: J. Transport. Res. Board 2124, 36-44. https://doi.org/10.3141/2124-04.
Ossen, S., Hoogendoorn, S., Gorte, B., 2006. Interdriver differences in car-following: a vehicle trajectory-based study. Transport. Res. Record: J. Transport. Res. Board 1965, 121-129. https://doi.org/10.3141/1965-13.
Ossen, S., Hoogendoorn, S.P., 2008. Validity of trajectory-based calibration approach of car-following models in presence of measurement errors. Transport. Res. Re.: J. Transport. Res. Board 2088, 117-125. https://doi.org/doi:10.3141/2088-13.

Ossen, S., Hoogendoorn, S.P., 2009b. Validity of trajectory-based calibration approach of car-following models in presence of measurement errors. Transport. Res. Record: J. Transport. Res. Board 2088, 117-125. https://doi.org/10.3141/2088-13.
Papathanasopoulou, V., Antoniou, C., 2015. Towards data-driven car-following models. Transport. Res. C: Emerg. Technol. 55, 496-509. https://doi.org/10.1016/j. trc.2015.02.016.
Paz, A., Molano, V., Martinez, E., Gaviria, C., Arteaga, C., 2015. Calibration of traffic flow models using a memetic algorithm. Transport. Res. C: Emerg. Technol. 55, 432-443. https://doi.org/10.1016/j.trc.2015.03.001.
Pelikan, M., 2005. Hierarchical Bayesian Optimization Algorithm: Toward a New Generation of Evolutionary Algorithms. Springer.
Pelikan, M., Goldberg, D.E., Cambi-Paz, E., 1999. BOA: The Bayesian optimization algorithm. In: Proceedings of the 1st Annual Conference on Genetic and Evolutionary Computation. Morgan Kaufmann Publishers Inc., pp. S25-S32.
Pelikan, M., Mühlenbein, H., 1998. Marginal distributions in evolutionary algorithms. In: Proceedings of the International Conference on Genetic Algorithms Mendel, pp. $90-95$.
PTV, A., 2015. VISSIM 8.0 user manual. Karlsruhe, Germany.
Punzo, V., Ciuffo, B., Montanino, M., 2012. Can results of car-following model calibration based on trajectory data be trusted? Transport. Res. Rec.: J. Transport. Res. Board 2315, 11-24. https://doi.org/10.3141/2315-02.
Punzo, V., Simonelli, F., 2005. Analysis and comparison of microscopic traffic flow models with real traffic microscopic data. Transport. Res. Record: J. Transport. Res. Board 1934, 53-63. https://doi.org/10.3141/1934-06.
Quadstone, 2009. The paramics manuals, version 6.6. 1. Quastone Paramics LTD, Edinburgh, Scotland, UK.
Rafati Fard, M., Shariat Mohaymasry, A., Shahri, M., 2017. A new methodology for vehicle trajectory reconstruction based on wavelet analysis. Transport. Res. C: Emerg. Technol. 74, 150-167.
Ranjitkar, P., Nakatsiji, T., Asano, M., 2004. Performance evaluation of microscopic traffic flow models with test track data. Transport. Res. Rec.: J. Transport. Res. Board 1876, 90-100. https://doi.org/10.3141/1876-10.
Ranjitkar, P., Nakatsoji, T., Kawamura, A., 2005. Experimental analysis of car-following dynamics and traffic stability. Transport. Res. Rec.: J. Transport. Res. Board 1934, 22-32. https://doi.org/10.3141/1934-03.
Rudlof, S., Köppen, M., 1997. Stochastic hill climbing with learning by vectors of normal distributions.
Saifuzzaman, M., Zheng, Z., 2014. Incorporating human-factors in car-following models: a review of recent developments and research needs. Transport. Res. C: Emerg. Technol. 48, 379-403. https://doi.org/10.1016/j.trc.2014.09.008.
Schultz, G., Rilett, L., 2004. Analysis of distribution and calibration of car-following sensitivity parameters in microscopic traffic simulation models. Transport. Res. Rec.: J. Transport. Res. Board 1876, 41-51. https://doi.org/10.3141/1876-05.
Sklar, M., 1959. Fonctions de répartition à n dimensions et leurs marges. de l'Institut de Statistique de L'Universite de Paris.
Talbi, E.G., 2009. Metahearistice. From Design to Implementation. Wiley.
Toledo, T., Koutsopoulos, H.N., Ben-Akiva, M., 2007. Integrated driving behavior modeling. Transport. Res. C: Emerg. Technol. 15 (2), 96-112. https://doi.org/10.

1016/j.trc. 2007.02.002.
Treiber, M., Hennecke, A., Helbing, D., 2000. Congested traffic states in empirical observations and microscopic simulations. Phys. Rev. E: Stat. Phys. Plasmas Fluids Relat. Interdiscip. Top. 62 (2 Pt A), 1805-1824. https://doi.org/10.1103/PhysRevE.62.1805.
Treiber, M., Kesting, A., 2013a. Microscopic calibration and validation of car-following models - a systematic approach. Procedia - Soc. Behav. Sci. 80, 922-939. https://doi.org/10.1016/j.sbapra.2013.05.050.
Treiber, M., Kesting, A., 2013b. Traffic flow dynamics. Traffic Flow Dynamics: Data, Models and Simulation, Springer-Verlag Berlin Heidelberg.
TSS, 2015. aimsun 8.1 User's Manual, Barcellona, Spain.
Vieira da Rocha, T., Leclercq, L., Montanino, M., Parzani, C., Punzo, V., Ciuffo, B., Villegas, D., 2015. Does traffic-related calibration of car-following models provide accurate estimations of vehicle emissions? Transport. Res. D: Transp. Environ. 34, 267-280. https://doi.org/10.1016/j.trd.2014.11.006.
Wang, K., Choi, S.H., Lu, H., 2015. A hybrid estimation of distribution algorithm for simulation-based scheduling in a stochastic permutation flowshop. Comput. Ind. Eng. 90, 186-196. https://doi.org/10.1016/j.cie.2015.09.007.
Wiedemann, R., 1974. Simulation des Straßenverkehrsflusses. In: Proceedings of the Schriftenreihe des tnstituts fir Verkehrswesen der Universitit Karlsruhe, Karlsruhe, Germany.
Yaschu, J., Branke, J., 2005. Evolutionary optimization in uncertain environments - a survey. IEEE Trans. Evol. Comput. 9 (3), 303-317. https://doi.org/10.1109/ TEVC.2005.846356.
Zheng, J., Suzuki, K., Fujita, M., 2012. A car-following model based on discrete choice theory. J. Transport. Syst. Eng. Inform. Technol. 12 (5), 31-38. https://doi.org/ $10.1016 /$ t1579-6672(11)60221-3.
Zheng, J., Suzuki, K., Fujita, M., 2013. Car-following behavior with instantaneous driver-vehicle reaction delay: a neural-network-based methodology. Transport. Res. C: Emerg. Technol. 36, 339-351. https://doi.org/0.1016/j.trc.2013.09.010.

Zheng, Z., 2014. Recent developments and research needs in modeling lane changing. Transport. Res. B: Methodol. 60, 16-32. https://doi.org/10.1016/j.trb.2013.11. 009 .
Zhong, R.X., Fu, K.Y., Sumalee, A., Ngoduy, D., Lam, W.H.K., 2016. A cross-entropy method and probabilistic sensitivity analysis framework for calibrating microscopic traffic models. Transport. Res. C: Emerg. Technol. 63, 147-169. https://doi.org/10.1016/j.trc.2015.12.006.