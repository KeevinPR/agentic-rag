# The Experimental Study of Population-based Parameter Optimization Algorithms on Rule-based Ecological Modelling 

Hongqing Cao<br>School of Earth and<br>Environmental Sciences, University of Adelaide, 5005<br>Australia<br>hongqing.cao@adelaide.edu.au<br>Friedrich Recknagel<br>School of Earth and<br>Environmental Sciences, University of Adelaide, 5005<br>Australia<br>friedrich.recknagel@adelaide.edu au

Philip T. Orr<br>Seqwater, PO Box 16146, City East Qld, 4002<br>Australia<br>porr@seqwater.com.au


#### Abstract

This study investigates six population-based algorithms for the parameter optimization (PO) within the hybrid methodology developed for modelling algal abundance by rulebased models. These PO algorithms include: (1) Hill Climbing (2) Simulated Annealing (3) Genetic Algorithm (4) Differential Evolution (5) Covariance Matrix Adaptation Evolution Strategy and (6) Estimation of Distribution Algorithm. The effectiveness of algorithms is tested on the Cylindrospermopsis abundance data from Wivenhoe Reservoir in Queensland (Australia). We provide a systematic analysis and comparison of different parameter optimization algorithms as well as the resulting predictive rule models.


Keywords-evolutionary algorithm; genetic programming; parameter optimization; population-based algorithm; ecological modelling

## I. INTRODUCTION

Cyanobacterial blooms, perhaps of increasing intensity and extent, are a recurrent feature of Australian rivers, reservoirs and lakes [1], [2]. The cyanobacteria causing these blooms may produce toxins that may cause death if ingested in sufficient amounts by domestic animals and wildlife. They also pose significant health risks to humans using the water [3], [4]. Harmful algal blooms have caused massive economic cost to Australia annually [5]. There is an immediate need to develop an advanced modelling tool for cyanobacterial blooms to facilitate informed decision-making for water managers.

Traditionally models of phytoplankton dynamics are expressed as process-based mathematical models of eutrophication based on ordinary differential equations (ODEs) [6], [7] which allow simulations of food web dynamics and nutrient cycles over time. However these ODEs are typically calibrated and validated for one site only. With the rapid development of computing technology, extensive study of machine learning techniques has been conducted in ecological modelling. Artificial neural network [8]-[10] is one of the wellestablished technologies in machine learning and a mainstream technology for data-driven modelling. Despite its great advantage to approximate nonlinear multivariate functions with high accuracy, a major drawback of this approach is that it is difficult to extract and explain the knowledge about the
relationship between the model inputs and outputs. On the contrary, fuzzy logic models [11], [12] can make up for this to some extent. They can improve the model interpretability by introducing some fuzzy rules, but the acquisition of the fuzzy rules largely depends on expert empirical knowledge.

In recent years, the study of evolutionary algorithms (EAs) has gained interest of many researchers in a wide range of fields [13]. Since 2003, our group led by Dr Friedrich Recknagel have initiated pioneering work on modelling algal blooms by using EAs [14]-[16]. Recently we developed a hybrid evolutionary algorithm (HEA) to build an algal abundance model with a single IF-THEN-ELSE rule structure [14]. The most advantage of such rule models lies in its high interpretability. Meanwhile from our research, we surprisingly found that when developing predictive rule model for algal abundance, in many runs, the modelling algorithm can find the threshold values for some key water quality parameters, like water temperature, pH value etc. This gives us a hint that the calibration of the random constants in the rule is crucial work. Previously we used a genetic algorithm (GA) based on multiparent crossover [17] to optimise the model parameters contained in a rule and have not compared with other optimisation algorithms. In this study we extend previous work by systematically studying six population-based algorithms for the parameter optimization within the hybrid methodology which include: (1) Hill Climbing (HC) (2) Simulated Annealing (SA) (3) Genetic Algorithm (GA) (4) Differential Evolution (DE) (5) Covariance Matrix Adaptation Evolution Strategy (CMA-ES) and (6) Estimation of Distribution Algorithm (EDA). The effectiveness of all algorithms is tested on the Cylindrospermopsis (one of the Cyanobacterial populations) abundance data from Wivenhoe Reservoir in Queensland (Australia). We provide a systematic analysis and comparison of different parameter optimization algorithms as well as the resulting predictive rule models.

## II. A HYBRID EVOLUTIONARY ALGORITHM FOR EVOLVING IF-THEN-ELSE RULES

We propose a hybrid evolutionary algorithm (HEA) to evolve the rule model for predicting the algal abundance. There are two layers in the HEA in which the first layer searches for

model structures using genetic programming (GP) [18], [19], whereas the inner layer searches for the optimal continuous parameters of the model by using some population-based optimization algorithms. Fig. 1 illustrates the conceptual diagram of the HEA based on water-quality input data and cyanobacteria output data. The details of the GP and the population-based algorithms are described in what follows.
![img-0.jpeg](img-0.jpeg)

Figure 1. The conceptual diagram of HEA for evolving the IF-THEN-ELSE rule models.

## A. Structure Optimization of Rule Models

## Model representation

We use GP as the main technique to evolve the rule model structure, which typically operates on parse trees instead of bit strings in traditional GA. In our case, the rule model with IF-THEN-ELSE structure is represented as a vector of multiple trees in GP with the form of (Tree1, Tree2, Tree3) where Tree1 denotes the IF condition branch, Tree2 and Tree3 denote the result branches of THEN branch and ELSE branch respectively. Fig. 2 shows an example of a rule model for predicting the abundance of Cylindrospermopsis. The chromosome representation (Tree1, Tree2, Tree3) in GP for this model is illustrated in Fig. 3.

$$
\begin{aligned}
& \text { IF }(((\mathrm{WT}>22.5) \text { AND }(\mathrm{pH}<10.8)) \text { OR }\left(\mathrm{TP}^{*} \mathrm{DO}>=523.5\right)) \longrightarrow \text { Tree } 1 \\
& \text { THEN Cylind. }=\mathrm{DO} * \exp (\mathrm{pH})+\mathrm{NTU} * \mathrm{SiO}_{2} * 34.5 \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots

methods, such as DE, CMA-ES and EDA, which are considered as the most competitive representatives of evolutionary computation, so far have not been applied to ecosystem models yet.

To make fair comparison, for each algorithm we define the stopping rule as when the total number of fitness evaluation evalnum reaches a maximum number $N_{\text {craf }}(=1000)$. The population size for all the algorithms is set as 50 . Below we give brief descriptions for each method as well as the settings of some key control parameters in the algorithm.

## $H C$

Hill climbing (HC) originally is a local search technique which starts with a random (potentially poor) solution, and iteratively makes small changes to the solution, each time improving it a little. When the algorithm cannot see any improvement anymore, it terminates. In this study we modify the simple HC by enabling to do hill-climbing iteratively, each time with an initial starting point from the best solution in last run. The pseudo-code of HC is shown as follows. The neighbourhood size $N_{\text {neighbors }}$ in the algorithm is set as 50 in this study.

## Pseudo-code of HC

## BEGIN

```
check all constants contained in current rule;
evalnum \leftarrow 0;
best rule \leftarrow current rule;
best fitness \leftarrow fitness of current rule;
while (evalnum < Nnval)
{
    n \leftarrow 0;
    current rule \leftarrow best rule;
    current fitness \leftarrow best fitness;
    while(n < Nneighbors)
    {
        produce a temporary rule by performing
        Gaussian mutations on the constants
            randomly chosen from Tree1,Tree2 and
            Tree3 respectively;
    calculate the fitness of the temporary rule;
    evalnum \leftarrow evalnum + 1;
    if(temporary fitness is better than best
        fitness)
    {
        best fitness \leftarrow temporary fitness;
        best rule \leftarrow current rule;
    }
    n \leftarrow n + 1;
    }
}
output the best rule and best fitness;
END
```


## $S A$

Simulated annealing (SA) is a random-search technique which exploits an analogy between the way in which a metal cools and freezes into a minimum energy crystalline structure (the annealing process) and the search for a minimum in a more general system. It forms the basis of an optimization technique for combinatorial and other problems. We set the three key control parameters in the algorithm as follows: initial
temperature $T_{0}=100$, the epoch length $L=100$ (the number of trials allowed at each temperature level), and the maximum allowable number of Markov chains $K=10000$. The pseudocode of SA is shown as follows:

## Pseudo-code of SA

## BEGIN

```
check all constants contained in current rule;
evalnum \leftarrow 0;
best rule \leftarrow current rule;
best fitness \leftarrow fitness of current rule;
T \leftarrow T0;
frozen \leftarrow false;
totaln \leftarrow 0;
while((!frozen || totaln < R) && evalnum < Nnval)
{
    cooling \leftarrow false;
    k \leftarrow 0;
    while( k < L)
    {
        produce a temporary rule by performing
        Gaussian mutations on the constants
        randomly chosen from Tree1, Tree2 and Tree3
        respectively;
    calculate the fitness of the temporary rule;
    evalnum \leftarrow evalnum + 1;
    \DeltaE \leftarrow temporary fitness - current fitness;
    if ( \DeltaE < 0)
    {
        cooling \leftarrow true;
        current rule \leftarrow temporary rule;
        current fitness \leftarrow temporary fitness;
        best fitness \leftarrow temporary fitness;
        best rule \leftarrow current rule;
    }
        L-IPSE
    else if (e e e e t random(0,1))
    {
        current rule \leftarrow temporary rule;
        current fitness \leftarrow temporary fitness;
    }
    k \leftarrow k + 1;
    totaln \leftarrow totaln + 1;
    }
    if (cooling)
    T \leftarrow 0.9 + T;
    else frozen \leftarrow true;
    }
    output the best rule and best fitness;
END
```


## $G A$

A genetic algorithm (GA) [24] is a search heuristic that mimics the process of biological evolution and the mechanisms of natural selection and genetic variation. Suitable encodings are used to represent possible solutions to a problem, and the search is guided by using some genetic operators (crossover, mutation etc.) and the principle of "survival of the fittest". Due to the merits of self-adaptation, self-organization, self-learning, intrinsic parallelism and generality, GAs have been applied successfully in a wide range of economic, engineering and scientific computations [25]. The GA we use in this study is a simple and general GA whose effectiveness has been demonstrated in our previous studies [17], [26]. The novelty of

the algorithm is the design of the multi-parent crossover. The pseudo-code of GA is shown as follows:

## Pseudo-code of GA

## BEGIN

$t \leftarrow 0 ;$
evalnum $\leftarrow 0$;
randomly initialize a parameter population $P(0)$; calculate the fitness of the individuals in $P(0)$; evalnum $\leftarrow$ evalnum + 1 (for each calculation);
while(evalnum $<N_{\text {eval }}$ )
\{
sort population $P(t)$ in terms of fitness;
randomly choose $M$ individuals from $P(t)$ to do multi-parent crossover;
calculate the fitness of the new produced individual;
evalnum $\leftarrow$ evalnum +1 ;
if(new fitness is better than the worst fitness) replace the worst one with the new individual;
$P(t) \leftarrow P(t+1) ;$
$t \leftarrow t+1 ;$
output the best rule and best fitness;
END

## $D E$

Differential evolution (DE) is one of the most recent Evolutionary Algorithms (EAs) [27] for solving real-parameter optimization problems proposed by Price and Storn [28]. It is an effective, robust and simple global optimization algorithm which extracts the differential information (i.e., distance and direction information) from the current population of solutions to guide its further search. In this way no separate probability distribution has to be used which makes the scheme completely self-organizing. According to frequently reported comprehensive studies [29], [30], DE outperforms many other optimization methods in terms of convergence speed and robustness over common benchmark functions and real-world problems. The Pseudo-code of DE is shown as follows. The five DE schemes I used in the paper are DE-rand1, DE-rand2, DE-best1, DE-best2, and DE-randtobest1 (see [31] for more details).

## Pseudo-code of DE

## BEGIN

$t \leftarrow 0$;
evalnum $\leftarrow 0$;
randomly initialize a parameter population $P(0)$; calculate the fitness of the individuals in $P(0)$; evalnum $\leftarrow$ evalnum +1 (for each calculation); while(evalnum $<N_{\text {eval }}$ )
\{
sort population $P(t)$ and get the best individual bestp(t);
for(i $=0$; i<Popsize; i++)
produce a new offspring $p_{i}^{*}(t)$ for individual $p_{i}(t)$ by randomly choosing one of the five alternative DE schemes;
calculate the fitness of $p_{i}^{*}(t)$;
evalnum $\leftarrow$ evalnum +1 ;
if (fitness $\left(p_{i}^{*}(t)\right)$ is better than fitness $\left(p_{i}(t)\right)$
$p_{i}(t+1) \leftarrow p_{i}^{*}(t)$;
else $p_{i}(t+1) \leftarrow p_{i}(t)$;

## \}

$t \leftarrow t+1 ;$
output the best rule and best fitness;
END

## CMA-ES

The covariance matrix adaptation evolution strategy (CMAES) is one of the most powerful evolutionary algorithms for real-valued optimization [32], [33] with many successful applications (for an overview see [34]). The main advantages of the CMA-ES lie in its invariance properties, which are achieved by carefully designed variation and selection operators, and in its efficient (self-) adaptation of the mutation distribution. The general scheme of CMA-ES approach is shown as follows:

## Main scheme of the CMA-ES approach

set $x_{i} / /$ number of samples per iteration, at least two, generally $>4$
initialize $m, \sigma, C=1, p_{\sigma}=0, p_{\sigma}=0$;
// imbalize state variables
while not terminate // iterate
for $\downarrow$ in $\{1 \ldots \lambda\} / /$ sample $\lambda$ new solutions and evaluate them
$x_{i}=$ sample_multivariate_normal
(mean $=m_{0}$ covariance_matrix $=\sigma^{2} C$ );
$f_{i}=$ fitness $\left(x_{i}\right)$;
$x_{1 \ldots \lambda} \leftarrow x_{s(1) \ldots s(1)}$ with $s(\lambda)=$ argsort $\left(f_{1 \ldots \lambda}, \lambda\right)$; // sort solutions
$m^{\prime}=m ; \quad / /$ we need later $m-m^{\prime}$ and $x_{i}-m^{\prime}$
$m \leftarrow$ update_m $\left(x_{1}, \ldots, x_{k}\right) ; / /$ move mean to better solutions
$p_{\sigma} \leftarrow$ update_ps $\left(p_{\sigma}, \sigma^{\prime} C^{\prime}\left(x^{\prime \prime}\left(m-m^{\prime}\right)\right)\right)$
$/ /$ update isotropic evolution path
$p_{\sigma} \leftarrow$ update_pc $\left(p_{\sigma}, \sigma^{\prime \prime}\left(m-m^{\prime}\right),\left(\left(p_{\sigma}\right)\right)\right)$
$/ /$ update anisotropic evolution path
$C \leftarrow$ update_C $\left(C, p_{\sigma},\left(x_{1}-m^{\prime}\right) / \sigma, \ldots,\left(x_{k}-m^{\prime}\right) / \sigma\right) ;$ // update covariance matrix
$\sigma \leftarrow$ update_sigma $\left(\sigma,\left(\left(p_{\sigma}\right)\right)\right)$;
// update step-size using isotropic path length
return $m$ or $x_{1}$.
$E D A$
Estimation of distribution algorithm (EDA) [35], [36] is a relatively new branch of EAs. Unlike other EAs, EDAs do not use crossover or mutation. Instead, they explicitly extract global statistical information from the selected solutions and build a probability model of promising solutions based on the extracted information. New solutions are sampled from the model thus built and fully or in part replace solutions in the current population. The general scheme of the EDA approach for continuous domains is shown as follows:

## Main scheme of the EDA approach

$D_{i} \leftarrow$ Generate $M$ individuals (the initial population) randomly;
$1 \leftarrow 1 ;$
do
\{
$D^{D_{i-1}} \leftarrow$ Select $N \leq M$ individuals from $D_{i-1}$
according to a selection method;
$p_{i}(x)=p\left(x \mid D^{D_{i-1}}\right) \leftarrow$ Estimate the probability distribution of an individual being among the selected individuals;
$D_{i} \leftarrow$ Sample $M$ individuals (the new population) from $p_{i}(x)$;
$1 \leftarrow 1+1 ;$

Different continuous EDAs have been proposed for the global continuous optimization problem [37]-[40]. In this study we use an improved IDEA (Iterated Density Evolutionary Algorithm) [40] called AMal,GaM-IDEA (Iterated Density Evolutionary Algorithm with Adapted Maximum-Likelihood Gaussian Models) [41] which uses the combination of SDR (Standard-Deviation Ratio), AVS (Adaptive Variance Scaling), and AMS (Anticipated Mean Shift) to adaptively change both the covariance and the mean-shift to prevent inefficient sampling. In addition the truncation selection, rejection sampling and elitist replacement are used in the algorithm.

## Parameter set encoding and fitness evaluation

For all above six parameter optimization (PO) algorithms, the encoding of the parameter set is the same. Regarding a specific rule model, we first check all the constants contained in the Tree1, Tree2 and Tree3, including counting the number of constants $l$ and recording their positions. Each individual in the parameter population can then be represented as an $l$ dimensional row vector $\left(c_{1}, c_{2}, \ldots, c_{l}\right)$ where each component $c_{i}$ for $i=1,2, \ldots, l$ is encoded as a floating number and generated randomly ranging from 0 to a predefined maximum integer during the initialization of the parameter population.

Before the fitness evaluation of an individual in the parameter population, we first return to the original rule model and replace all constants with the corresponding components of the row vector (i.e. the individual) and then follow the same procedure as in Section II (A) to calculate the fitness.

## III. EXPERIMENTS

## A. Study Data

In this study we use the Cylindrospermopsis abundance data from Wivenhoe Reservoir in Queensland (Australia) to test and compare the performance of different parameter optimization algorithms based on hybrid evolutionary modelling framework. A number of limnological variables have been collected over an 11-year period (1998-2009) as shown in Table I. A simple linear interpolation has been used to fill missing values to produce a complete daily time series for this period. In order to develop 7-days-ahead predictive models for Cylindrospermopsis abundance by using our modelling algorithm, we shift the interpolated daily data for 7 days and use as input data.

TABLE I. PARAMETERS USED AS INPUT AND OUTPUT
VARIABLES IN THE EVOLUTIONARY MODELLING WITH HEA

## B. Parameter Settings and Measures

All the experiments were performed on a Hydra supercomputer (IBM eServer 1350 Linux) provided by eResearch SA with a peak speed of 1.2 TFlops by using the programming language $\mathrm{C}++$. The GP parameter settings of HEA for structure optimization are: Popsize $=100$, maximum tree depth $=4$, maximum number of generations $=80$. Besides total RMSE, we also calculate the total $\mathrm{R}^{2}$ value between the predicted and measured values on whole data set to measure the algorithm performance.

## C. Results and Discussions

Table II shows the statistical results of six PO algorithms in 100 runs. In terms of the RMSE and $\mathrm{R}^{2}$ values, the rank of the average performance of those six algorithms is: HC, SA, DE, GA, EDA, and CMA-ES. In terms of computational efforts, HC and CMA-ES are the two most time-consuming algorithms, whereas the average running time for other four algorithms are very close.

TABLE II. THE STATISTICAL RESULTS OF SIX PO ALGORITHMS IN 100 RUNS


Table III shows the best rule models obtained by six PO algorithms in 100 runs. It is interesting to notice that all those rule models clearly indicate the threshold values of some water quality parameters (i.e. WT, TP, NTU, $\mathrm{SiO}_{2}, \mathrm{DO}, \mathrm{EC}$ ) or their ratios (i.e. $\mathrm{SiO}_{2} / \mathrm{pH}$ ) in the IF condition branch favoured by the growth of Cylindrospermopsis. This demonstrates that the HEA has the most advantage of automatically discovering the understandable IF-THEN-ELSE rules hidden in the measured data and can be regarded as a powerful intelligent data mining tool for ecological data.

Among the six best models found by different PO algorithms, the HC and SA models are significantly superior to other models in terms of their much lower RMSE and higher $\mathrm{R}^{2}$ value ( $>0.65$ ). The secondary are the DE, EDA and GA models and their RMSE and $\mathrm{R}^{2}$ values are very close. It seems that the CMA-ES model is the worst one with the largest RMSE ( $>15000$ ) and the lowest $\mathrm{R}^{2}$ value ( $=0.46$ ).

TABLE III. THE BEST MODELS OBTAINED BY SIX PO ALGORITHMS IN 100 RUNS


The modelling results of the six best models validated on the whole data are illustrated in Fig. 4. One feature of the Cylindrospermopsis measured data is that there are regular summer peaks annually during the years from 1998 to 2009. Among those peaks, the most prominent ones are the six experiencing in the years of 2000, 2001, 2002, 2003, 2006 and 2009 respectively. It is encouraging result that for all the six models, the predicted timings of these prominent peaks correspond very well with the measured data, which coincides with our aim of giving early warning of cyanobacterial blooms by developing these models. Desirably both the HC and SA models can forecast the magnitudes of the summer peaks in successive four years from 2000 to 2003 very well, whose predicted values almost overlap with the measured data. In contrast, other models under-estimate these peaks in most cases. Due to the fact that all the six models fail to predict their magnitudes reasonably, it seems challenging work to predict the summer peaks in 2006 and 2009.
![img-2.jpeg](img-2.jpeg)
(a)
![img-2.jpeg](img-2.jpeg)
(b)

Figure 4. The validation results on whole data for the best models in 100 runs using six PO algorithms. (a) HC, SA, GA; (b) DE, CMA-ES, EDA.

Finally the results of the experiments are analysed using a one-way ANOVA test combined with Tukey's HSD Post Hoc Test for multiple comparisons using a $95 \%$ confidence level as suggested by [42]. The data we use for statistical analysis are the total RMSE values in 100 runs for six PO algorithms. The calculated F-value is 337.4 which is significant compared with the threshold value 2.2899 . The statistical results for Tukey's HSD Post Hoc Test are shown in Table IV. From the table, we conclude the dominance order of six PO algorithms performed on the Cylindrospermopsis data is:

$$
\mathrm{HC} \rightarrow \mathrm{SA} \rightarrow \mathrm{DE} \rightarrow \mathrm{GA} \rightarrow \mathrm{EDA} \rightarrow \mathrm{CMA}-\mathrm{ES}
$$

## IV. CONCLUSIONS AND FUTURE WORK

This paper proposes a new methodology in freshwater ecosystem modelling. It mainly includes the following three main features:
(1) The explainable single rules with IF-THEN-ELSE structure are developed to model the abundance of Cylindrospermopsis;

(2) A hybrid evolutionary algorithm (HEA) is designed to perform structural and parameter optimization of rule models simultaneously;
(3) Six population-based algorithms are applied to perform the parameter optimization (PO) task within the hybrid methodology including HC, SA, GA, DE, CMA-ES, and EDA.

The effectiveness of the methodology is tested on the Cylindrospermopsis abundance data from Wivenhoe Reservoir in Queensland (Australia). Six different parameter optimization (PO) methods are applied to each test data set and their results are compared and analysed. Based on the experimental results, we draw some conclusions as follows:
(a) Whatever which PO method is applied in the hybrid EA, our modelling algorithm can always find multiple IF-THENELSE rules, which not only clearly indicate various environmental conditions favoured by Cylindrospermopsis but also are capable of forecasting their abundances reasonably. More interestingly, our algorithm is able to propose a variety of alternative rule models with distinctive IF condition branches. This result is very encouraging as it could help ecologists to design new experiments in the lab to testify the competing hypothesis (models) which the human brains can hardly imagine.
(b) Both the experiments and their statistical analysis suggest that when comparing different PO methods, HC and SA always perform the best. The secondary is DE, GA and EDA, which are three comparable methods, whereas CMA-ES performs the worst. This result looks somewhat surprising. We surmise that this is mainly caused by the high complexity and uncertainty of model parameters contained in a rule model. Unlike some benchmark functions, the number of the random constants in a rule is arbitrary and their value ranges can be largely different. Hence it is hard for some sophisticated methods with complex mathematical computation (i.e. CMAES) to capture the data relativity and find the global optima with small population size. We observed that the default population size $\lambda$ in CMA-ES is less than 10 in most cases of our study. On the contrary, some classical optimization techniques, like HC and SA, have the advantage to explore the irregular search space by multiple starting points and iterative random search. They seem to work better when optimizing the random constants with arbitrary number for these rule models which are evolved based on the real-world ecological data.

In order to further improve the predictive accuracy of rule models we consider two possibilities to extend the single rule model structure in our future work. One is to use an ensemble of multiple single rules to model the algal abundance. Another is to design a more complicated rule set model with multi-level embedded IF-THEN-ELSE structures. It will be interesting to compare the advantages and disadvantage of these three different model structures: a single rule, an ensemble of multiple single rules, and a rule set with embedded single rules, when performing on ecological data from real-world freshwater ecosystems.
