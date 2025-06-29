# Distributed Estimation of Distribution Algorithms for continuous optimization: How does the exchanged information influence their behavior? 

Santiago Muelas ${ }^{\mathrm{a}, \mathrm{v}}$, Alexander Mendiburu ${ }^{\mathrm{b}}$, Antonio LaTorre ${ }^{\mathrm{a}, \mathrm{c}}$, José-María Peña ${ }^{\mathrm{a}}$<br>${ }^{a}$ Dept. of Computer Systems Architecture and Technology, Universidad Politécnica de Madrid, Spain<br>${ }^{b}$ Intelligent Systems Group, Dept. of Computer Architecture and Technology, University of the Basque Country, Spain<br>${ }^{c}$ Instituto Cajal, Consejo Superior de Investigaciones Científicas, Madrid, Spain

## A R T I C L E I N F O

Article history:
Available online 24 October 2013

Keywords:
Evolutionary computation
Graphical model
Estimation of Distribution Algorithm
Island model
Continuous optimization

A B S T R A C T

One of the most promising areas in which probabilistic graphical models have shown an incipient activity is the field of heuristic optimization and, in particular, in Estimation of Distribution Algorithms. Due to their inherent parallelism, different research lines have been studied trying to improve Estimation of Distribution Algorithms from the point of view of execution time and/or accuracy. Among these proposals, we focus on the so-called distributed or island-based models. This approach defines several islands (algorithms instances) running independently and exchanging information with a given frequency. The information sent by the islands can be either a set of individuals or a probabilistic model. This paper presents a comparative study for a distributed univariate Estimation of Distribution Algorithm and a multivariate version, paying special attention to the comparison of two alternative methods for exchanging information, over a wide set of parameters and problems - the standard benchmark developed for the IEEE Workshop on Evolutionary Algorithms and other Metatheuristics for Continuous Optimization Problems of the ISDA 2009 Conference. Several analyses from different points of view have been conducted to analyze both the influence of the parameters and the relationships between them including a characterization of the configurations according to their behavior on the proposed benchmark.
(c) 2014 Published by Elsevier Inc.

## 1. Introduction

Estimation of Distribution Algorithms (EDAs) are a set of techniques that belong to the field of Evolutionary Computation. Since they were introduced in the 90s [32,43], the research community has put a lot of effort in their development, providing powerful algorithms which have been successfully applied to both artificial and real-world problems. In general terms, EDAs are similar to Genetic Algorithms (GAs), but their main characteristic is the use of probabilistic models to extract information from the most promising individuals of the current population (instead of using crossover or mutation operators) in order to create a new and presumably better population. The complexity of the different EDAs approaches is usually related to the probabilistic model used, and the ability of that model to identify and represent the (in) dependencies among the variables.

[^0]
[^0]:    * Corresponding author.

    E-mail addresses: smuelas@fi.upm.es (S. Muelas), alexander.mendiburu@ehu.es (A. Mendiburu), atorre@fi.upm.es (A. LaTorre), jmpena@fi.upm.es (J.-M. Peña).

Detailed information about the main characteristics of EDAs, as well as the different algorithms that belong to this family can be found in [25,27,35,36].

The main drawback of the most complex EDAs -those that try to consider all the possible (in) dependencies among the variables- is their high computational cost. Due to this, and thanks to the modularity of EDAs, several parallel approaches have been proposed. These proposals can be divided into two groups:

- Direct parallelization or parallel EDAs (pEDAs): Those whose behavior is exactly the same of the corresponding sequential version. Their main goal is the reduction of the execution time by the parallelization of the computation of the fitness function or the construction of the graphical models [27,29,38].
- Island-based approach or distributed EDAs (dEDAs): Those that create different subpopulations and exchange information among them, trying to improve the quality of the solutions of the sequential algorithm.

In this work, we pay attention to the second approach. In this scheme, an EDA instance is executed in each island, and some information is exchanged among the islands during the execution. This information can be made up of individuals (as done in other EAs), or probabilistic models (following the rationale that EDAs use them to extract and gather information about the population). Migration of individuals is a classic approach and has proven to obtain successful results in these and other Evolutionary Algorithms [2,4,9,28]. In addition, migration of models was explicitly developed for the distributed Estimation of Distribution Algorithms [1,11,12,19,20].

Until now, most of the previous work in dEDAs has been conducted in the discrete domain, and little research has been done in comparing both migration methods (individuals versus models). In particular, in continuous optimization, as far as the authors are aware, only two studies have been carried out [10,11]. Although these papers concluded that the migration of models obtains significantly better results than the migration of individuals, the experimental scenario was restricted to (a) a limited number of problems with small dimensions and (b) a small number of parameters. In this paper, a thorough study has been conducted to analyze the behavior of the distributed approaches in the context of EDAs. This study has demonstrated that the statement of the previous studies is not correct, at least not in the field of continuous optimization, using, for this task, a standard benchmark, formal methods for conducting the analysis of the influence of the parameters, and validating the results with formal statistical procedures. Briefly, the precise objectives pursued in this work are the following:

- Conduct an extensive study of different distributed EDAs configurations over several functions and dimensions.
- Identify the parameters that have a greater influence on the final behavior and the relationships between them.
- Analyze the relationship of the parameter values of both the best and the worst configurations.
- Compare the performance of the distributed configurations against their equivalent sequential configurations.
- Compare the performance of both methods for exchanging information: individuals vs models.
- Characterize the distributed configurations according to their behavior on the proposed benchmark.

The rest of the paper is organized as follows: Section 2 presents an overview of the previous studies on EDAs and dEDAs. Section 3 describes the proposed experimental scenario. Section 4 presents and comments the results obtained and lists the most relevant facts extracted from this analysis. Finally, Section 5 contains the concluding remarks derived from this study.

# 2. Preliminaries 

In this section the main characteristics of EDAs and dEDAs are briefly reviewed.

### 2.1. Estimation of Distribution Algorithms: EDAs

EDAs are stochastic heuristic search strategies that are part of the Evolutionary Computation paradigm. In EDAs, multiple solutions or individuals are created at every generation, evolving successively until a satisfactory solution is achieved. In brief, the characteristic that clearly differentiates EDAs from other evolutionary search strategies, such as GAs, is that the evolution from one generation to the next is achieved by estimating the probability distribution of a set of individuals, sampling later the induced model. This avoids the use of crossing or mutation operators, and the number of parameters required by EDAs is considerably reduced. Based on the probabilistic model considered, three main groups of EDAs can be distinguished: univariate models, which assume that variables are marginally independent; bivariate models, which accept dependencies between pairs of variables; and multivariate models, in which there is no assumption about independences.

The univariate model is the simplest model, in which independence among variables is assumed. Therefore, the joint probability distribution is defined as the product of the marginal probability of each variable. The main advantage of this model is its low computational cost, although the assumption of independence among all the variables could lead to a very simplistic approach for some problems. Some representative algorithms of this model are: the Population-Based Incremental Learning algorithm (PBIL) [5], the compact Genetic Algorithm (cGA) [18] and the most extended heuristic within this model, the Univariate Marginal Distribution Algorithm UMDA [26,31] and its continuous version, the Univariate Marginal Distribution Algorithm for Gaussian Models $\left(\operatorname{UMDA}_{R}\right)[21,23]$.

A slightly more sophisticated approach than the previous model is to consider the dependencies existing between two variables (pairwise or bivariate dependencies). This implies a good trade-off in terms of complexity and efficiency as, at most, one variable may depend on another one. To construct such graphical models, greedy approaches which add arcs to an initially disconnected graph are normally used. Some of the most frequently used heuristics within this model are MIMIC [7], COMIT [6] and BMDA [34]. All these approaches are available in both discrete and continuous versions.

The multivariate models are more flexible models since they do not constrain the number of dependencies among the variables. Their main disadvantage is that the computational cost of learning and sampling such models can be considerably high. An additional drawback is that, in order to construct an accurate model, the required population size should be bigger than for simpler models. Some examples of heuristics in the discrete case are EBNA [22] and BOA [33]. In the continuous case, most representative heuristics are EMNA $_{\text {global }}$ and EGNA [25].

For this work we have focused on two of the EDAs that have been more extensively used on continuous optimization: the univariate $U M D A_{g}$ and the more complex multivariate EMNA $_{\text {global. }}$ No bivariate model has been included in this study since these two models have been the preferred choice in previous studies, the selected multivariate model can represent the same type of interactions than the bivariate approach and also with the aim of investing more effort in conducting a more extensive study in these two learning models instead of reducing the parameter values to include a third model.

# 2.2. $U M D A_{g}$ 

UMDA $_{g}$ assumes that the joint density function follows a $n$-dimensional normal distribution, which is factorized by a product of one-dimensional and independent normal densities. In every generation and for every variable, the UMDA $_{g}$ carries out some statistical tests in order to find the density function that best fits the sampling of that variable. UMDA $_{g}$ is a structure identification algorithm because the density components of the model to be learnt are identified via hypothesis tests. This estimation of parameters is carried out, after the densities are identified, by their maximum likelihood estimates. If all the univariate distributions are normal, then the two parameters to be estimated at each generation and for each variable are the mean, $\mu_{i}^{\prime}$, and the standard deviation, $\sigma_{i}^{\prime}$. It is well known that their respective maximum likelihood estimates are:

$$
\begin{aligned}
& \widehat{\mu}_{i}^{\prime}=\widehat{X}_{i}^{\prime}=\frac{1}{N} \sum_{t=1}^{N} x_{i, t}^{\prime} \\
& \widehat{\sigma}_{i}^{\prime}=\sqrt{\frac{1}{N} \sum_{t=1}^{N}\left(x_{i, t}^{\prime}-\bar{X}_{i}^{\prime}\right)^{2}}
\end{aligned}
$$

### 2.3. EMNA $_{\text {global }}$

The Estimation of Multivariate Normal Algorithm (EMNA) is an approach based on the estimation of a multivariate normal density function. At each generation, the vector of means $\mu=\left(\mu_{1}, \ldots, \mu_{n}\right)$ and the variance-covariance matrix $\Sigma$ whose elements are denoted by $\sigma_{i, j}^{2}$ with $i, j=1, \ldots, n$, are estimated. Therefore, it requires the estimation of $2 n+\binom{n-1}{2}$ parameters at each generation: $n$ means, $n$ variances and $\binom{n-1}{2}$ covariances. This can be done efficiently in a single pass through the population.

By its definition, the covariance matrix is always positive semi-definite but, because of the numerical errors caused by the finite precision of computers, sometimes the covariance matrix contains negative values. The problem with an ill-posed covariance matrix is that the sampling of new individuals becomes impossible. There are several solutions to repair the covariance matrix [13]. In this work, the most efficient method, the ECMR0 technique, has been selected for repairing the covariance matrix.

### 2.4. Distributed Estimation of Distribution Algorithms: dEDAs

In the distributed Evolutionary Algorithms (dEAs), ${ }^{1}$ the whole population is distributed over multiple subpopulations and occasionally allows the migration or exchange of some individuals among the different islands. Therefore, each node executes an independent algorithm on an independent population. An important aspect of the performance of dEAs is the migration strategy. This is configured through different parameters [8]:

- Migration frequency: How often (number of generations) is information sent?
- Migration rate: How many individuals migrate each time?
- Information selection: What kind of information is exchanged?

[^0]
[^0]:    ${ }^{1}$ Also known as coarse-grained, multiple-deme or island models.

- Acceptance policy: How are the incoming and the local information combined?
- Migration topology: Which island sends information to which other?

Close scrutiny of migration parameters [37] has proved that, even though EAs with small populations risk being trapped in a local optimum, an appropriate migration strategy can avoid a suboptimal solution from dominating all the populations. A correct configuration can help to obtain better results with fewer evaluations, but configuring these optimal parameters is not a simple issue [3,30,42]. This appropriate strategy must be adjusted between the limits of a low interaction (which would practically imply the execution of N independent algorithms) and an excessive interaction (that would lead to the predominance of only one solution).

Regarding the information exchanged among islands, two possible alternatives are available: (i) the straightforward approach of selecting a pull of individuals that will be later sent to the consignees and (ii) the alternative of using the main characteristic of EDAs: the probabilistic models. These probabilistic models will be (or should be) able to represent the (in) dependencies among the variables, and, therefore, comprise more information than a group of individuals. This second approach opens a new challenge: how should the different probabilistic models be combined? In general, the combination of the resident model with the immigrant one can be formalized by the following rule [19]:

$$
M_{R}^{\prime}=\beta M_{R} \circ(1-\beta) M_{I}
$$

where $\circ$ represents the combination operator of two probabilistic models and $\beta$ represents the influence of the immigrant model $M_{I}$ on the resident model $M_{R}$ and varies in the range $[0,1]$. An extended version of this formula for $n$ immigrant models would be:

$$
\begin{aligned}
& M_{R}^{\prime}=\beta_{10} M_{R} \circ \beta_{11} M_{11} \circ \beta_{12} M_{12} \circ \ldots \circ \beta_{1 n} M_{1 n} \\
& \sum_{i} \beta_{i i}=1
\end{aligned}
$$

A general approach for carrying out this combination is to apply a mixture model $M=\sum_{i} \beta_{i} M_{i}$ as a linear combination of simple distributions, where the $\beta_{i}$ 's satisfy that $\sum_{i} \beta_{i}=1$ [11]. In this case, the population from the mixture model is created by sampling the individuals from each of the involved models. The $\beta_{i}$ value defines the probability for selecting each model for the sampling of each new individual. This way, the models with higher $\beta$ values, would have a higher probability of producing more individuals of the new population and would have more influence on the next inferred model.

The previous approach has the advantage of not depending on the inner details of the model and, therefore, can be applied to probabilistic models of different nature. A different strategy is to use a specific operator that takes into account the structure of the models to combine them appropriately. This method has the disadvantage that, with complex models, the combination is not trivial and, in some cases, can be very inefficient [20]. In the simple $U M D A_{R}$ models, a straightforward and efficient approach that can be carried out, named $U M D A_{R}$ combination method, is to combine the means and variances vector, i.e.:

$$
\mu_{R}^{\prime}=\sum_{i=1}^{n} \beta_{i} \mu_{i}, \quad \sigma_{R}^{\prime}=\sqrt{\sum_{i=1}^{n} \beta_{i}^{2} \sigma_{i}^{2}}
$$

For this work we have introduced a new combination model called uniform combination for $U M D A_{R}$. In this method, instead of combining the models, each model component (mean and variance) is selected from a single model of the whole set of models. Each model has a probability $\beta_{i}$ of being selected for each of the components of the new model. Therefore, the best models would contribute to more components than the worst ones. This approach is similar to the mixture model in the sense that each model is selected according to the $\beta$ value. However, for this approach, the selected model is applied to a subset of dimensions for all the new individuals, whereas in the mixture case, the selected model was applied to all the dimensions of a single individual.

In order to compute the value of $\beta$, the strategy that has been followed in previous studies [10,20] is the so-called adaptative learning strategy. This method computes the $\beta$ values based on the quality of the population associated to each model.

For $n$ immigrants, the $\beta$ value is defined as:

$$
\beta_{R}=\frac{F_{R}}{F_{R}+\sum_{j}^{n} F_{I_{j}}}, \quad \beta_{I_{j}}=\frac{F_{I_{j}}}{F_{R}+\sum_{j}^{n} F_{I_{j}}}
$$

where $F_{R}$ represents the mean fitness value of the resident subpopulation and $F_{I_{j}}$ represents the mean fitness value of the $i$ th immigrant subpopulation. A conservative policy is also followed and only those models with a population of better quality than the resident model are considered for the computation. Therefore, if all the immigrants models have worse quality than the resident model, no combination is carried out.

# 3. Experimentation 

For the experimentation, the benchmark from the workshop on Evolutionary Algorithms and other Metaheuristics for Continuous Optimization Problems - A Scalability Test held at the ISDA 2009 Conference has been considered. This benchmark defines 11 continuous optimization functions. The first 6 functions were originally proposed for the "Special Session and Competition on Large Scale Global Optimization" held at the CEC 2008 Congress [41]. The other 5 functions have been specially proposed for the Workshop of the ISDA 2009 Conference. These functions, presented in Table 1, have different degrees of difficulty and can scale to any dimension. Detailed information about the selected benchmark can be found at the web page of the organizers of the workshop. ${ }^{2}$

In order to analyze the effects of the migration strategies, several island configurations instances were compared against each other. The selection of the parameter values, such as the learning model, was based on the values used in previous studies with dEDAs [12,20] and was extended with additional values to obtain a wider view. Table 2 shows the different parameter values used throughout the experiments.

For the experimentation a full factorial design was chosen in order to conduct a complete study on the effect of each parameter on the response variable, as well as the effects of interactions between the parameters. Therefore, all possible combinations of the values across all the parameters were considered. This design has the disadvantage that it requires a higher number of runs but, in contrast, it can identify all the possible interactions between the parameters.

In order to make the results comparable with other algorithms, we have strictly followed the conditions imposed by the benchmark. Therefore, for each combination, 25 independent executions were carried out. The stopping criterion, as defined in the benchmark, was a fixed number of fitness evaluations ( 5000 times the dimension of the problem). The performance criterion (i.e. the response variable) is the distance (error) between the best individual found and the global optimum in terms of fitness value. Sequential versions of both the $U M D A_{g}$ and EMNA global algorithms were also executed with different population sizes ( $64,128,256,512,1024$ and 2048) in order to have a baseline comparison.

## 4. Analysis of the results

For accomplishing the objectives proposed at Section 1, several analyses have been conducted from different perspectives.

### 4.1. Overall analysis

In order to conduct this study, a standard global measure was obtained for each configuration. First, the configurations were ranked on each function according to the procedure defined in the Friedman test. This way, the results on each function are defined in the same scale and can be averaged for obtaining the global rank measure.

The first approach that was considered was to use the Analysis of Variance (ANOVA) technique for analyzing the interactions between the parameters. ANOVA was developed by R.A. Fisher and has been applied to a vast array of different domains for data analysis. However, despite its widespread use, some key assumptions must be checked before applying ANOVA to the experimentation data: (i) the distributions of the residuals must follow a normal distribution and (ii) the variance of data in groups should be the same (equality of variances or homoscedasticity). For checking the first assumption, the Anderson-Darling, Shapiro-Wilk and Kolmogorov-Smirnov tests were carried out for each dimension of the global results obtaining for all tests a $p$-value $<0.05$ and therefore rejecting the null hypothesis that the distributions of the residuals come from a normal distribution. The homocedasticity property was checked with both the Bartlett's and the Levene's tests obtaining a $p$-value less than $1 \mathrm{e}-4$ and therefore rejecting the assumption of homocedasticity on the results.

Due to these results, the Taguchi method [40] was selected as an alternative procedure for conducting the overall analysis. In this method, the concept of signal to noise ratio (SN ratio) is introduced for measuring the sensitivity of the quality characteristic being investigated in a controlled manner to those external influencing factors (noise factors) not under control. The aim of the experiment is to determine the highest possible SN ratio for the results since a high value of SN ratio implies that the signal is much higher than the random effects of the noise factors. From the quality point of view, there are three possible categories of quality characteristics: (i) smaller is better, (ii) nominal is best and (iii) bigger is better. The obtained results fall in the "smaller is better category" since the objective is to reduce the error between the best solution found and the global optimum. For this category, the SN ratio estimate is defined in Eq. (7) where $n$ denotes the total number of instances and $y_{1}, y_{2}, \ldots, y_{n}$ the target values (the error to the best solution in this case).

$$
S N=-10 \log \left(\frac{1}{n} \sum_{t=1}^{n} y_{t}^{2}\right)
$$

Figs. 1-3 display the main effects plot for the SN ratio results obtained for 50, 100 and 200 dimensions respectively. A main effect plot is a plot of the mean response values (the SN ratio for these graphs) at each level of a design parameter. This

[^0]
[^0]:    ${ }^{2}$ http://sci2s.ugr.es/programacion/workshop/Scalability.html.

Table 1
Benchmark functions.
Table 2
Parameters values.
Common parameter values
Problem size
50, 100 and 200
Population size
512, 1024 and 2048
Learning model
Selected inds. for learning
\#Islands
Topology
8 and 16
Migration period
Ring2 and all-to-all (a2a)
Acceptance policy
Migrate every 10, 20 and 40 generations
Best individuals from resident and
Immigrants populations
Particular parameter values
Inds. migration rate
Inds. emigrants selection
10\% and 20\%
Models combination
Best or random individuals
Mixture, UMDA combination and
UMDA uniform
![img-0.jpeg](img-0.jpeg)

Fig. 1. Main effects plot for SN ratios on 50 dimensions.
plot can be used to compare the strength of the effects of the values of the parameter. From these results it can be observed that the most important parameter for characterizing the performance is the type of algorithm, having obtained the $U M D A_{g}$ model better SN values than the EMNA global approach. There are two main reasons that could explain this behavior: most of the functions ( 7 out of 11), although not linearly separable, can be easily optimized dimension by dimension, being the

![img-2.jpeg](img-2.jpeg)

Fig. 2. Main effects plot for SN ratios on 100 dimensions.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Main effects plot for SN ratios on 200 dimensions.

UMDA $_{8}$ algorithm more suitable for this kind of functions since it does not manage any kind of interaction in its model. Second, the EMNA global algorithm needs to have a considerable amount of individuals to be able to capture all the dependencies among the variables [13]. However, in this benchmark the maximum number of evaluations is fixed and larger population sizes mean less number of iterations which heavily penalizes the final results. It must be taken into account that this constraint was imposed in the original benchmark as an example of the limitations that metaheuristics must deal with when solving real-world problems (the balance between execution time and solution quality).

The remaining parameters are not as decisive as the type of algorithm although some important patterns must be mentioned. Regarding the population size, 2048 individuals has obtained the worst values. In general, the EDAs tend to improve their results with larger population sizes (more information to build the model). However, due again to the number of evaluations constraint, a bigger population size implies a smaller number of iterations which, at the end, can severely affect the final values. In general, 1024 individuals has offered a good trade-off between the number of solutions for building a quality model and the maximum number of allowed iterations, although with the 50 dimensional functions, 512 individuals has

obtained the best value. A similar trend has been observed with the number of islands. The smallest value, i.e., the one with the highest population size per island, has obtained the best signal to noise ratio values.

The next parameter that should be taken into account is the method for exchanging information. Regarding the two approaches for sending information, individuals or models, it can be mentioned that sending individuals has obtained better overall results being this difference bigger for the higher dimensional functions.

From the two remaining common parameters, it seems that there is no significant difference among the two topology values explored and that a more frequent exchange of information has been more beneficial for obtaining the best values. Concerning the particular parameter values for sending individuals, the best selection of emigrants has obtained a small improvement over the random selection and, apparently, both selection rate values have obtained similar results. For the analysis of the different methods for combining models, only the results from the $U M D A_{R}$ algorithms have been considered since for the $E M N A_{\text {global }}$ configurations only one method for combining models was proposed. From these results it is clear that the mixture model obtains the best results followed by the new proposed UMDA uniform model and having obtained the UMDA combination model the worst results among the three dimensions.

An analysis of the interactions between the parameters, measured with the SN ratio, was also conducted. Figs. 4-6 display the interactions plots between the parameters of the configurations based on sending individuals in 50, 100 and 200 dimensions, respectively. In the same way, Figs. 7-9 represent the interactions of the configurations based on sending models. An interaction plot is a powerful graphical tool which displays the mean response of two parameters (the SN ratio in this case) at all the possible combination of their values. For improving the clarity of the diagrams, only the parameters that have presented any interaction with any other parameter have been displayed in these graphs.

Several interactions have been identified in the configurations based on sending individuals. One of the most remarkable interactions is the relationship between the topology and the criterion for selecting the immigrants, where the worst results are obtained with the all-to-all topology and the selection of the best individuals. This seems logical since, in this combination, the diversity of the algorithm is quickly reduced in the first generations. A similar scenario arises between the population size and the topology parameters, where the performance of the all-to-all topology is heavily penalized when connected with the smallest population size, especially with the highest dimensional functions. Another interesting relationship is the one between the population size and the number of islands in the highest dimensional functions. With 512 individuals, the increment of the number of islands from 8 to 16 leaves a population of 32 individuals per island, which is clearly not enough for inducing a good model of the problem.

Several interactions have also arisen with the configurations that exchange models. As for the sending individuals configurations, the increment from 8 to 16 islands considerably reduces the performance of the configurations that use the smallest population size. Regarding the methods for combining the models, it seems that the UMDA combination method, in contrast to the other alternatives, obtains better results with the highest population sizes, lower migration frequencies and the lowest topology degree approach, i.e., characteristics that tend to increment the global diversity of the algorithm.

The previous studies have provided a broad view of the overall behavior of all the configurations. With the purpose of offering an alternative view of the relationships between the parameters and the algorithm performance, the best and worst
![img-3.jpeg](img-3.jpeg)

Fig. 4. Sending individuals interactions plot for SN ratios on 50 dimensions.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Sending individuals interactions plot for SN ratios on 100 dimensions.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Sending individuals interaction plot for SN ratios on 200 dimensions.
configurations have been analyzed independently from the remaining configurations. Moreover, the sequential algorithms have been included in this study in order to compare the performance of the distributed configurations. Tables 3-5, display a ranking of the configurations on 50, 100 and 200 dimensions, respectively, according to the global average rank. In these tables only the best and worst $5 \%$ of the configurations, as well as the sequential configurations, are displayed ${ }^{3}$.

From these tables it is clear that the best results have been obtained with distributed configurations, being the sequential algorithms placed around positions near the middle of the table. To better analyze the influence of the parameters, Figs. 10-12 display the parallel coordinates graph of the distribution of the values of the parameters of the best configurations on 50, 100 and 200 dimensions respectively and Figs. 13-15 the equivalent graphs for the worst configurations. Parallel

[^0]
[^0]:    ${ }^{3}$ The complete 444 results can be accessed in the following URL http://cajalbbp.cesvima.upm.es/storage.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Sending models interactions plot for SN ratios on 50 dimensions.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Sending models interactions plot for SN ratios on 100 dimensions.
coordinates is a useful technique which has been successfully used to represent high dimensional data as polylines in two dimensions. More recently, it has been used to capture the underlying interactions between the parameters of a Particle Swarm Optimization algorithm [15]. In this paper, the first eight axes represent the parameters of the configurations, whereas the ninth one represents the Friedman average ranking mentioned before. Only the best and worst $20 \%$ of the solutions are displayed on these graphs. The best/worst $5 \%$ of the solutions have been highlighted with a variety of different colors while the remaining $15 \%$ has been marked in light gray. The global best and worst configurations have been depicted with a dashed line. A small deviation, similar to a jitter effect, has been applied to each configuration parameter value to distinguish better the configurations.

As happened in the first analysis, the $U M D A_{g}$ learning model has been the most decisive parameter: all the best results have been achieved with this learning model, whereas the EMNA global model has been the common value among the worst algorithms. Regarding the information exchange methods, it can be observed that sending individuals obtains the best

![img-8.jpeg](img-8.jpeg)

Fig. 9. Sending models interaction plot for SN ratios on 200 dimensions.
overall results and that this characteristic is present in almost all the best $5 \%$ of the configurations. However, the opposite is not true, since several configurations that send individuals are among the worst $5 \%$. This fact explains why the difference between these two approaches has not been very significant in the first study. Sending individuals has demonstrated to be the best choice for this benchmark but needs to be properly configured since, without the proper selection of the remaining parameters, this value would not determine the performance of the configuration. A similar situation happens with the topology parameter, where the ring topology has been selected by almost the whole set of the best configurations. For 100 and 200 dimensions the situation is quite similar, confirming the fact that the previous conclusions are stable and can be generalized to a higher number of dimensions.

# 4.2. Comparing the performance on each function 

For this study, it was planned to include the characteristics of the problems in the data set to see the impact of these characteristics in the solution quality. These characteristics were extracted from the literature and are represented in Table 6.

However, after conducting an analysis of the main effects and interaction graphs for each function, it was observed that the behavior of similar functions, according to this table, was completely different according to the graphs. For example, for functions $f 2$ and $f 8$, which both are unimodal, shifted and not separable, the corresponding main effects plots have little in common as it can be shown in Figs. 16 and 17 for 100 dimensions. Moreover, some functions that have opposite characteristics in Table 6, such as $f 1$ and $f 5$, have demonstrated to behave almost identically according to the main effects graphs as represented in Figs. 18 and 19. Therefore, this type of analysis could not be carried out.

By contrast, the analysis of the main effects graphs has identified two groups of functions with similar behaviors: one made up of functions $f 1$ and $f 5$ and a second one made up of functions $f 7, f 9, f 10$ and $f 11$. The remaining functions have presented a particular behavior, significantly different to be included in any other group.

Finally, it is worth mentioning that only in functions $f 4$ and $f 8$ the exchange of models obtained a better SN ratio than the exchange of individuals. In order to provide more insight about this behavior, a study for comparing both information exchange methods was carried out.

This study consisted in analyzing the performance on each function of the configurations based on sending individuals against the equivalent ones based on sending models. For this task, all the configurations were grouped according to their information exchange model: 4 groups for sending individuals and 3 for sending models with 61 configurations per group. Then, the average rank was obtained for each group ( 61 values per group). Tables 7-9 present the results in 50, 100 and 200 dimensions. For each function, the best average rank is highlighted on both tables.

From these results, it can be seen that, in 9 out of 11 functions, the groups based on sending individuals obtained a superior average rank than the ones based on sending models. Only on two functions, $f 4$ and $f 8$, the sending models configurations based on the $U M D A_{g}$ combination method obtained a better average rank than the sending individuals configurations. In order to explain this behavior, it is convenient to understand that the exchange and combination of models has the objective of improving the accuracy and reducing the noise of the current model by its combination with the models sent from the other islands. However, when exchanging models instead of individuals, the best solutions that

Table 3
Average rankings 50 dimensions.
the other islands have found are not available to the current island. As other studies have proven [24], the use of elitism is normally beneficial for the behavior of EDAs. For this reason, the combination of models offers a poorer performance on most of the functions.

Therefore, for the purpose of clarifying the behavior of the exchange of models in functions $f 4$ and $f 8$, the best sequential EDA was executed with and without elitism on the 50 dimensional functions. ${ }^{4}$ Table 10 displays the average error of the 25 executions and highlights if the differences between both versions (with and without elitism) are significant according to the Wilcoxon signed-rank test. In this table it is shown that the absence of elitism obtains significantly better results in functions $f 4, f 6$ and $f 8$. Furthermore, the results obtained in functions $f 4$ and $f 8$ by the sequential EDA

[^0]
[^0]:    ${ }^{4}$ Only in this dimension since the behavior is similar on the other dimensions.

Table 4
Average rankings 100 dimensions.
are better than the obtained by the best distributed algorithm as it will be shown in the following study. It seems that, for these functions, it is better to improve the general diversity of the population (and therefore, the exploratory ability of the algorithm) in order to reach better regions of the search space. In $f 6$, where both versions have almost converged to the final optimum, it seems that the greater diversity of the distributed model (against the sequential version) is enough for dealing with this characteristic and the non-elitist sequential EDA does not improve the results of the distributed versions.

Within the individuals configurations, sending the best $10 \%$ individuals achieves the best overall performance in most of the functions for both $U M D A_{R}$ and $E M N A_{\text {global }}$ models. On the other hand, sending a $20 \%$ of randomly chosen individuals obtained the worst results. Regarding the different methods for combining the models, it must be taken into account that

Table 5
Average rankings 200 dimensions.
within the $U M D A_{g}$ configurations, the mixture model obtains the best results in most of the functions followed by the proposed uniform approach, being both models better than the combination method.

# 4.3. Comparing the best configurations 

A comparison of the best configurations for both type of algorithms and the different methods for exchanging information was conducted. The best sequential configuration for each algorithm was also included in this study along with the IPOP-CMA-ES algorithm, a metaheuristic that follows a strategy similar to that of the EMNA $_{\text {global }}$ since it learns a covariance matrix and uses it (along with more information) to sample the individuals of the new population. This algorithm was the winner of the Special Session on Real-Parameter Optimization of the IEEE CEC 2005

![img-9.jpeg](img-9.jpeg)

Fig. 10. Parameter values of the best configurations on 50 dimensions.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Parameter values of the best configurations on 100 dimensions.
![img-11.jpeg](img-11.jpeg)

Fig. 12. Parameter values of the best configurations on 200 dimensions.

![img-12.jpeg](img-12.jpeg)

Fig. 13. Parameter values of the worst configurations on 50 dimensions.
![img-13.jpeg](img-13.jpeg)

Fig. 14. Parameter values of the worst configurations on 100 dimensions.
![img-14.jpeg](img-14.jpeg)

Fig. 15. Parameter values of the worst configurations on 200 dimensions.

Table 6
Properties of the functions of the benchmark.
![img-15.jpeg](img-15.jpeg)

Fig. 16. Main effects plot for $S N$ ratios on 100 dimensions for the $f 2$ function.
![img-16.jpeg](img-16.jpeg)

Fig. 17. Main effects plot for SN ratios on 100 dimensions for the $f 8$ function.
conference [39] and was proposed by the organizers of the benchmark as a reference algorithm for comparing the results.

Table 11 displays the average error of the 25 executions on each function. As shown in the table, the best results on most of the functions are obtained by the distributed configuration that uses the $U M D A_{g}$ algorithm and exchanges individuals.

![img-17.jpeg](img-17.jpeg)

Fig. 18. Main effects plot for SN ratios on 100 dimensions for the $f 1$ function.
![img-18.jpeg](img-18.jpeg)

Fig. 19. Main effects plot for SN ratios on 100 dimensions for the $f 5$ function.

Similarly to what happened in the previous analysis, the performance of the EMNA $_{\text {global }}$ configurations is significantly worse than the $U M D A_{g}$ ones. However, with the $f 8$ function, both the sequential and the distributed exchanging models configuration obtain better results than the $U M D A_{g}$ ones. As shown on its function definition (Eq. (8)), the first components of the solution have more influence in the fitness function than the remaining components. With an appropriate population size, the EMNA $_{\text {global }}$ algorithm is able to detect this dependency between the variables and focus the search on the first dimensions of the solutions.
$f 8(x)=\sum_{i=1}^{n}\left(\sum_{j=1}^{i} z_{i}\right)^{2}, \quad z=x-0$
$o$ represents the global optimum
An interesting pattern that can be seen in this table is that, for the configurations that exchange models, the population size is larger for those based on sending individuals and the selected topology in both cases is the all-2-all method. It seems that, for most of the functions, it is better to have a larger population size for improving the quality of the induced model and share it with the rest of the islands to accelerate the diffusion of good patterns.

The performance of the sequential configurations is, in general terms, worse than their equivalent distributed configurations. However, in some functions ( $f 9$ and $f 11$ for $U M D A_{g}$ and $f 8$ for the EMNA $_{\text {global }}$ ) the concentration of the individuals helps to improve the results.

In order to provide a proper statistical validation of the results, the procedure described in [16,17] was followed, where the distribution of the results was first compared with the Friedman test in order to detect significant differences.

Table 7
Average ranking per function on 50 dimensions functions.

Table 8
Average ranking per function on 100 dimensions functions.

A value of 103.59 was obtained for the chi-squared statistic, which corresponds with a $p$-value of $4.45 \mathrm{E}-20$, confirming the existence of significant differences between the results. Then, two post hoc methods (Holm and Hochberg) were used to obtain the adjusted $p$-values for each comparison between the control algorithm (the distributed $U M D A_{g}$ based on sending individuals).

The results of these tests are reported in Table 12, and show, for all of them, that there is statistical evidence to state that the dEDA algorithm based on sending individuals is significantly better than any of the EDA algorithms considered in the

Table 9
Average ranking per function on 200 dimensions functions.

Table 10
Average error of the best sequential EDA configurations with and without elitism on the 50 dimensional functions.
${ }^{\text {a }}$ Means that there are statistical differences, according to the Wilcoxon test, with significance level $\alpha=0.05$.
comparison. Furthermore, this configuration obtains significant results against the IPOP-CMA-ES algorithm on two of the three statistical procedures.

# 4.4. Characterization of the configurations 

Finally, an unsupervised learning algorithm was applied to all the configurations to extract the groups of configurations that have a similar performance. For each configuration, a vector of all the ranks among all the functions on all the dimensions was collected and used as a representative value for the configurations. Therefore, two configurations with similar ranks among all the functions would be considered similar configurations. Then, a density-based clustering algorithm that has obtained successful results in the literature, the DBScan algorithm [14], was applied to the ranks vector of each configuration. In order to obtain an explanation of the results, the C4.5 machine learning algorithm was applied to the configurations to describe the assigned clusters, generating the induction tree depicted in Fig. 20, which represents the relevant characteristics that belong to each cluster. For determining the quality of each cluster, the average rank of the configurations belonging to the same cluster was computed, obtaining the values: $124.21,201.97,329.96,329.15$, 349.52 for clusters 1 to 5 , respectively.

These results have confirmed the conclusions from the previous studies, being the type of algorithm the parameter that most differentiates the configurations. As previously shown, the performance of the EMNA $_{\text {global }}$ configurations is con-

Table 11
Average error of the best configurations.

Table 12
Statistical validation (UMDA_inds is the control algorithm).

${ }^{a}$ Means that there are statistical differences with significance level $\alpha=0.05$.
siderably lower than the equivalent $U M D A_{g}$ configurations having all the $U M D A_{g}$ clusters (1 and 2) a superior cluster average rank that the EMNA $_{\text {global }}$ clusters (3, 4 and 5). For the $U M D A_{g}$ configurations, the second most important attribute is the information exchange method, being all the configurations based on sending individuals grouped in the same cluster plus some of the configurations based on sending models (the ones with the best results). For the EMNA $_{\text {global }}$ configurations, it seems that the population size per island determines better the performance of the configuration than the information exchange method.

![img-19.jpeg](img-19.jpeg)

Fig. 20. C4.5 Induction tree from the DBScan cluster. Each leaf node contains the cluster name and, in parentheses, the number of instances classified by the branch. The average ranks of the configurations included in each cluster are: cluster1: 124.21, cluster2: 201.97, cluster3: 329.96, cluster4: 329.15 and cluster5: 349.52 .

# 5. Conclusions 

This paper presents an extensive comparison of several configurations of dEDAs and sequential EDAs over a standard benchmark of continuous functions in both 50, 100 and 200 dimensions. Several analyses from different points of view have been carried out and non-parametric tests have been applied for contrasting the achieved results. From these studies, it has been observed than the learning model of the algorithms has been the most decisive factor. It seems that, for the proposed benchmark, the $U M D A_{g}$ has obtained the best results. However, it must be taken into account that the EMNA $_{\text {global }}$ algorithm needs a considerable amount of individuals to induce the dependencies among the variables and, with the benchmark constraint on the number of evaluations, this has implied a considerable reduction on the number of iterations which has heavily penalized the final results. Therefore, a future work would be to extend this analysis with a higher number of evaluations and also with the more complex EGNA models which also require larger population sizes.

A special attention has been paid to determine which method for exchanging information between dEDAs, the migration of individuals or the migration of probabilistic models, is the best approach for a researcher who would like to apply the $U M D A_{g}$ or EMNA $_{\text {global }}$ dEDAs in a continuous domain. From this perspective, the results from this study clearly express that, for most of the functions, the exchange of individuals obtains significantly better results than the alternative approach of sending models, although the remaining parameters must be properly tuned to obtain the best results. However, it was also discovered that, for the functions where the absence of elitism improves the results, the exchange of individuals (which implies a degree of elitism) obtains worse results.

From the remaining parameters of the distributed configurations some interesting relationships have arisen such as the interaction between the topology and the criterion for selecting the immigrants, the relationship between the topology and the population size, and between the population size, migration period and topology with the selected method for conducting the combination of the models.

The question of whether the dEDAs configurations obtain better results than their equivalent sequential versions has been also addressed: the study shows that the best dEDAs configurations outperform the best results of the sequential counterparts.

Finally, taking advantage of all the configurations analyzed through this experiment, a characterization of the behavior of the configurations has also been presented. The clustering analysis of all these configurations shows that the type of algorithm $\left(\mathrm{UMDA}_{\mathrm{g}}\right.$ and $\left.E M N A_{\text {global }}\right)$, the information exchange method for the $U M D A_{g}$ configurations and the population size per island for the $E M N A_{\text {global }}$ configurations are the most determinant characteristics for characterizing the behavior of the configurations.

# Acknowledgments 

This work was financed by the Spanish Ministry of Science TIN2010-21289-C02-02 and supported by the Cajal Blue Brain Project. The authors thankfully acknowledge the computer resources, technical expertise and assistance provided by the Centro de Supercomputación y Visualización de Madrid (CeSViMa) and the Spanish Supercomputing Network. The authors would also like to thank Nelis Franken for his help with his Fluxviz tool.
