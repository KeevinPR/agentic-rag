# Parameter Calibration of the Patch Growing Algorithm for Urban Land Change Simulations 

Rodrigo Lopez-Farias<br>CONACyT - Centro de Investigación en Ciencias de Información Geoespacial A.C. Queretaro, Mexico<br>rlopez@centrogeo.edu.mx

S. Ivvan Valdez<br>CONACyT - Centro de Investigación en Ciencias de Información<br>Geoespacial A.C. Queretaro, Mexico<br>svaldez@centrogeo.edu.mx

A. Garcia-Robledo<br>CONACyT - Centro de Investigación<br>en Ciencias de Información<br>Geoespacial A.C. Queretaro, Mexico<br>agarcia@centrogeo.edu.mx


#### Abstract

Urban growth modelling is a current trend in geocomputation due to its impact on the local living environment and the quality of life. The FUTure Urban-Regional Environment Simulation (FUTURES) model produces projections of landscape patterns by coupling land suitability, per-capita demand, and patch growing algorithm (PGA) sub-models. In particular, the PGA is the urban growing simulator component that takes into account the stochastic nature of urban development. It requires a set of parameters, namely compactness mean, compactness range, and discount factor to approximate the general characteristics of the urban development structure. The fitness of the parameters is measured by computing the difference between the area and compactness histograms of the observed and simulated urban growths. On the one hand, the authors find these parameters via an exhaustive grid search; nevertheless, this requires evaluating all the points in the grid, which implies a high computational cost because each point is associated with several PGA simulations. In addition, the approximation is limited to be one of the points in the grid. Thus, the better the precision is, the higher the required computational cost. On the other hand, evolutionary algorithms have been widely used for the automatic calibration of parameters but, in general, they are not designed to use a low number of evaluations, require expert tuning, and to define the stop criteria. Therefore, we propose an algorithm to find the adequate parameters, with minimum expert intervention, using an Estimation of Distribution Algorithm designed to use a low number of function evaluations (EDALNFE) when compared to the grid search. EDALNFE provides several assets: it delivers competitive results, it requires a low number of function evaluations, it does not require expert settings, and it is equipped with an automatic stop criterion. The proposed algorithm is compared to exhaustive grid search (the only method readily available in the FUTURES package) and differential evolution to demonstrate its superior performance.

Index Terms-Land Use Change, Estimation of Distribution Algorithm, Patch Growing Algorithm, Optimization


## I. INTRODUCTION

FUture Urban-Regional Environment Simulation (FUTURES) is a framework designed to produce consistent urban growth projections given a set of initial geographic conditions. It is one of the most accessible and used urban growth simulation models and it has been studied and compared against other popular models [1].

FUTURES is a modular model composed by three major modules: 1) the Land Use Suitability function, which produces
the initial probability of change from non-urban to urban land use; 2) the land demand per-capita, which estimates the quantity of land that should be allocated in the space; and 3) the Patch Growth Algorithm (PGA), which incorporates the stochastic nature of urban growth to simulate the allocation of the estimated urban land units.

Although the framework has the potential to give significant insights about the urbanization structure and spatial trends, the PGA parameters are not straight-forward to obtain for generating future urban scenarios. The available framework allows to select these parameters by expert experimentation which is, basically, a trial-error strategy.

Therefore we propose a competitive novel population-based meta-heuristic EDALNFE to automatically approximate global optimum parameters in an efficient way.

## II. RELATED WORK

The calibration of an urban growth model seeks to determine the parameter values that most accurately represent the observed land use [1] by searching for a combination of parameter values that minimizes the error between the simulated patch changes and the observed patch changes.

There are as many calibration algorithms as there are urban growth models since each model has different parameters to calibrate. Nonetheless, we can identify two rough classes of calibration strategies: brute-force-based calibration and optimization-based calibration. These two classes are discussed below.

## A. Brute-force Calibration

Brute-force calibration consists of testing all the possible combinations of sets of parameter values. In a worst-case scenario this is equivalent to a factorial experiment design.

In [2] the authors calibrate the widely-used SLEUTH urban growth model by following a brute-force approach. They test a set of combinations of the control parameters. Results are then sorted, and the parameters with the best results are used to begin the next calibration round.

In the case of FUTURES the plugin for GRASS includes the r.futures.calib module, which runs the PGA model (detailed in the next section) with different combinations

of parameters: compactness mean, compactness range, and discount factor. The structure of the simulated urban patches (land sub-regions composed by contiguous cells) of these runs are then compared against the observed patch changes in the ground truth to select the best set of parameters in terms of the measured error [3].

The brute-force approach is clearly highly computational intensive for a thorough parameter calibration. This approach usually requires the use of parallel computers. Also, often the search space of the continuous parameters is discretized. Hence, no values out of the discrete set are ever tested.

## B. Optimization-based Calibration

Optimization-based calibration is performed by metaheuristic algorithms which explore the space of parameter values by optimizing an objective function. A common class of meta-heuristics used for urban growth model calibration is population meta-heuristics such as Genetic Algorithms (GAs).

The disadvantage of optimization-based calibration is the need of adequately setting the meta-heuristic parameters, which can represent a non-trivial task. For example, in the case of GAs this involves designing an objective function, choosing a chromosome representation, generating an initial population, as well as defining the selection, crossover, and mutation operators.

The advantages include the reduction of number of parameters tests which often implies significantly lower calibration times when compared to the brute-force approach. Also, unlike brute-force algorithms, meta-heuristics can efficiently search parameter values in the continuous space. Following, we review the most iconic research in meta-heuristic algorithms for urban growth model calibration.

In [4] it is presented a memetic algorithm to calibrate a Dinamica-EGO-based LULC urban patch growth model. The memetic algorithm is used to heuristically search the parameter space by "extending a genetic algorithm with a local search function".

In [5] is presented a genetic algorithm to calibrate the transition rules of a cellular automata urban growth model based on the analysis of multi-temporal satellite imagery and population density.

In [6] a genetic algorithm is proposed to calibrate the SLEUTH growth algorithm on data for the Azadshahr, Gonbadekavoos, and Gorgan cities in Iran. The authors conclude that the GA prevents premature convergence to a local minimum, and favors the approximation to a global minimum.

In [7] it is proposed a cellular automata-based urban growth model that uses an Artificial Bee Colony optimization algorithm ( ABC ) to extract transition rules. The calibration is conducted through an Ant Colony Optimization algorithm (ACO) and compared against similar swarm-intelligence methods. Experiments were conducted on urban growth data from Urmia, Iran. Authors conclude that the ABC algorithms outperforms the ACO-based model "with fewer quantity and allocation errors".

In [8] authors optimize the parameters of a patch-based cellular automata model by using a GA that optimizes the size, shape, and compactness of the urban growth model. A surrogate model is used in the GA to reduce the number of the objective function evaluations.

In [9] authors propose a cellular automata model that uses irregular cells for simulating land-use change. They calibrate their model with a particle swarm algorithm that optimizes the agreement between the reference and simulation maps measured in their contingency matrix.

In [10] authors try two optimization algorithms for the calibration of the Fuzzy Cellular Urban Growth Model (FCUGM): a GA and parallel annealing. They conclude that the GA produces a better calibrated model.

In [11] authors calibrate an urban cellular automata model in two steps. First, they reduce the number of parameters to calibrate by determining the weights of the suitability evaluation factors with logistic regression. Then, they use a GA to calibrate the remaining parameters.

To the best of our knowledge, our work presents the first optimization-based calibration approach that specifically targets the FUTURES patch-growing algorithm.

## III. A Brief Overview of FUTURES Framework

FUTURES is a framework that simulates urban land change and urban growth using three modules: the potential module for computing land-use-change suitability, the one for the estimation of land demand, and the patch growing algorithm (PGA).
a) Land-use-change Suitability: It measures the likelihood of new land development based on the association of the socioeconomic, infrastructural, and environmental dimensions of a region. It is modeled with a logistic regression to associate geographic variables with urban change. It is described with Equation (1):

$$
s_{i}^{\prime}=a+\sum_{h=0}^{m} \beta_{h} \cdot x_{i h}
$$

where $s_{i}^{\prime}$ is the preliminary suitability score computed as the result of a linear combination of the $m$ map predictors coefficients $\beta_{i}$ indexed by $h$ that multiply each map variable $x_{h}$ at cell $i$ plus the intercept $a$.

The preliminary suitability score $s_{i}^{\prime}$ is mapped with the sigmoid function $s_{i}=e^{s_{i}^{\prime}} / 1+e^{s_{i}^{\prime}}$ to produce the suitability map. The suitability map is the most important map in the PGA to simulate realistic urban scenarios of the spatial urban growth and deserves an independent study.
b) Demand: It is a module that predicts the land demand per-capita given a population-size.
c) PGA: It is the module of main interest to this work. It simulates the urban growth dynamics given a suitability map of urban land change (Equation (1)), parameters $\Theta$, and land demand estimation, considering a stochastic process of urban land change. Every developed cell by PGA modifies

the suitability score in the neighborhood $s_{i}^{\prime}$ using Equation (2)

$$
s_{i}=s_{i}^{\prime} * d^{-\alpha}
$$

where $\alpha$ is a number from a uniform probability distribution that controls the attraction of the urban development around a given cell. The uniform probability distribution is defined by the compactness mean $\mu_{c}$, compactness range $\mu_{\sigma}$ parameters and the uniform random variable $r \in[0,1)$ :

$$
\alpha=\left(\mu_{c}-\mu_{\sigma}\right) \cdot 0.5+r \cdot \mu_{\sigma}
$$

The basic steps of PGA are:

1) Select randomly an undeveloped cell in the suitability map.
2) Set the selected cell as developed with a probability given by the suitability map.
3) If the cell is not set as developed, then repeat Step 1.
4) PGA explores the new urban land suitability of the neighbors. The cell is added to the growing patch depending on the composite suitability score $s_{i}$.
5) The composite scores of the neighboring cells are computed and sorted.
6) The PGA ranks the candidate cells according to their composite score $s_{i}$ to guide the patch growth through the neighborhood search. It stops when it meets a stop criterion, such as a maximum patch size.
The PGA requires the initial suitability map $S$, the initial urban map $M_{t}$, and the estimated land demand for the next time step $\Delta \hat{Q}_{t+1}$.

## A. Optimization Problem Definition

To define the optimization problem, it is important to consider the statistical representation of the urban land structure.

The land structure is represented by small land sub-regions composed by contiguous cells called patches. The set of all patches found in an urban map are characterized according to density estimations of patch shapes and sizes.

The density estimation of patch sizes $H_{s z}$ is calculated from the histogram of patch sizes. The patch size is the number of contiguous developed cells considering the 4-neighbor rule [12].

Similarly, the density estimation of patch shapes $H_{s h}$ is calculated from the histogram of shapes of the patches $s h$. The shape is the quotient of the perimeter of the observed patch $j$ of size $z$ and the perimeter of a circle of the same size, as described in Equation (4).

$$
\text { pshape }=\frac{\text { perimeter of patch } j \text { with size } z}{\text { perimeter of circle of size } z}
$$

Where if $s h>1$ means that the observed patch is not as compact as the circle.

The problem is to find the best PGA parameters, namely compactness mean $\mu_{c}$, compactness range $\sigma_{c}$, and discount factor $\varphi$ represented by $\Theta=\left\{\mu_{c}, \sigma_{c}, \varphi\right\}$ that produce a likely simulated increment of urban map $\Delta \hat{M}_{t+1}$. The parameters $\mu_{c}, \mu_{\sigma}$ are described in Equation (2), and $\varphi$ is a discount factor
that shrinks the initial patch sizes before calculating its density distribution, in order to compensate the smaller size of the new developed patches.

We want to produce the map $\Delta \hat{M}_{t+1}$ presenting similar size and patch shape density estimations to the urban map $M_{t}$, given an estimated land demand $\hat{Q}_{t+1}$, and initial urban and suitability maps $M_{t}$ and $S_{t}$, respectively. Equation (5), describes the stochastic dynamic process for simulating landuse change.

$$
\hat{M}_{t+1}=f_{P G A}\left(M_{t},\left\{S_{t}, \hat{Q}_{t+1}, \Theta\right\}\right)
$$

where $\hat{M}_{t+1}$ is the estimation of the urban growth map at time $t+1 . f_{P G A}$ is the dynamic process that receives the initial urban map $M_{t}$, suitability map $S_{t}$, and parameters $\Theta=$ $\left\{\mu_{c}, \mu_{r}\right\}$.

The urban land increment $\Delta \hat{M}_{t+1}$ is a map difference used in the objective function defined by:

$$
\Delta \hat{M}_{t+1}=\hat{M}_{t+1}-M_{t}
$$

In this regard, the minimization problem is given by:

$$
\underset{\Theta}{\arg \min } d_{s z}(\Theta)+d_{s h}(\Theta)
$$

where $d_{s z}(\Theta)$ and $d_{s h}(\Theta)$ are the density distribution distances for the size and shape defined by:

$$
\begin{aligned}
d_{s z}(\Theta) & =d\left(H_{s z}\left(p s i z e_{t}\right), H_{s z}\left(\varphi \cdot p s i z e_{t+1}\right)\right) \\
d_{s h}(\Theta) & =d\left(H_{s h}\left(p s h a p e_{t}\right), H_{s h}\left(p s h a p e_{t+1}\right)\right)
\end{aligned}
$$

where $\varphi$ is the discount factor, $p s i z e_{t}, p s i z e_{t+1}$ and $p s h a p e_{t}$, $p s h a p e_{t+1}$ are the lists of simulated and observed patch sizes and shapes in association with maps $M_{t}$ and $\Delta \hat{M}_{t+1}$. The density distribution distance is defined as:

$$
d(\mathbf{a}, \mathbf{b})=0.5 \cdot \sum_{i=1}^{\text {hits }} \frac{\left(a_{i}-b_{i}\right)^{2}}{a_{i}+b_{i}}
$$

where $a_{i}$ and $b_{i}$ are the bin values of two density distributions $H$ multiplied by 100 . The bins with no values are discarded to compute the distance.

## IV. Optimization Methods

Evolutionary algorithms have been widely used for derivative-free and black-box optimization [13]. Parameter calibration of the PGA model is addressed with this kind of algorithms because of the complexity of the simulation algorithms that are, in this case, black boxes, and the characteristics of the objective functions that are distances in non-derivable measures. In this regard Differential Evolution (DE) [14] has been demonstrated competitive results for the calibration of water and rainfall models among others in recent research [15]. In the same regard, estimation of Distribution Algorithms (EDAs) have been used for model calibration and optimization [16]. Nevertheless, they have not been applied to the patch growing problem or to geography-related problems. EDAs use

a explicit probability distribution that could be equipped with mechanisms for improving the search or the convergence. In this case, we introduce a new EDA with two main advantages: it requires a low number of objective function evaluations and it presents fast convergence in contrast with the grid search and the DE. In contrast to other evolutionary algorithms, the EDA convergence can be measured and used as a stop criterion.

Additionally, the proposed EDA, named Estimation of Distribution Algorithm for a Low Number of Function Evaluations (EDALNFE), has a unique input parameter, hence it does not requires of expert settings.

In this section, we present: 1) a description of the grid search, that basically is an exhaustive search over a discretized search space; 2) the Differential Evolution, an evolutionary algorithm that reports competitive results for model calibration; and 3) the proposed EDALNFE, an Estimation of Distribution Algorithm specifically designed for this calibration task.

## A. Grid Search

The grid search works as follows. Each variable domain is partitioned into $N_{\rho c}, N_{\sigma c}$, and $N_{\text {parsa }}$ discrete points that are equally spaced nodes of the grid. Then, every node is a combination of parameters, so that the combination reporting the minimum objective function value is the best. On the one hand, this strategy presents the advantage of searching in representative solutions of the whole search space. On the other hand, it only looks at predefined configurations. Hence, very likely, the optimal parameters do not belong to the grid. Nevertheless, the grid search serves as the baseline result in computation cost and as objective function value. The aim of this research is to present a proposal that delivers a configuration with a lower objective function value than the grid search with a similar number of objective function evaluations, or a similar objective function value with a lower number of function evaluations.

The specific discrete points of the grid within the search limits are defined in Equation (11).

## B. Differential Evolution

Differential Evolution is a population based optimization algorithm that has been largely applied to a variety of optimization problems, for instance, the calibration of hydrological models [17] and calibration of climate projections based on [18]. The algorithm works generating an initial random population of $N p$ candidate solutions in $D$ dimensions inside defined bounds. In each iteration, the current population is replaced by a new one via a mutation operator. The DE is presented in Algorithm 1. Its inputs are the objective function $f()$, the population size $N p$, the search limits $\mathbf{b}_{\mathbf{U}}, \mathbf{b}_{\mathbf{L}}$, the number of dimensions $D$, and the number of maximum generations $g_{\text {max }}$. The mutation is defined in lines 8 to 15 , where a new candidate solution is partially formed by a combination of three other ones or inherits several variable values from a parent. In lines 16 to 18, the best individuals are preserved and the worst are replaced to generate the next population.

```
Algorithm \(1 \mathrm{DE} \text { (best/1/bin) }
    procedure \(\mathrm{DE}(f(\cdot), D, N p, \mathbf{b}_{\mathbf{U}}, \mathbf{b}_{\mathbf{L}}, g_{\max })\)
        for each \(i \in\{1 \ldots N p\}\) and \(j \in\{1 \ldots D\}\) do
            \(x_{j, i}=\operatorname{rand}_{j}\left(b_{j, U}-b_{j, L}\right)+b_{j, L}\)
        end for
        for each \(g \in\left\{1 \ldots g_{\max }\right\}\) do
            for each \(i \in\{1 \ldots N p\}\) do
                \(r 0, r 1, r 2=\) randomIndices \((1, N p)\)
                \(\mathbf{v}_{i}=\mathbf{x}_{r 0}+F\left(\mathbf{x}_{r 1}-\mathbf{x}_{r 2}\right)\)
            for each element vector \(j \in\{1 \ldots D\}\) do
                if rand \(_{j} \leq C r\) or \(j=j_{\text {rand }}\) then
                \(u_{j, i}=v_{i, j}\)
                else
                \(u_{j, i}=x_{j, i}\)
                end if
            end for
            if \(\left(f\left(\mathbf{u}_{i}\right) \leq f(\mathbf{x}_{i})\right)\) then
                \(\mathbf{x}_{i}=\mathbf{u}_{i}\)
                end if
            end for
        end for
    end procedure
```


## C. EDA for a Low Number of Function Evaluations

In this article, we propose a novel Estimation of Distribution Algorithm for a Low Number of Function Evaluations (EDALNFE), shown in Algorithm 2. The optimization variables are in the domain $[0,1]$. Notice that they can be scaled and translated in the evaluation. First, a random uniform population of size $N p=8 D+2$ is generated, where $D$ is the number of optimization variables. Then, they are evaluated by means of Equation (7). The selection operator uses the Empirical Selection Distribution [19] to assign a probability value to each individual according to its sorting by objective function value.

The selection algorithm assigns a probability value to each of the $N=|F|$ individuals. The best individual has a value of $N / Z$, the second best $(N-1) / Z$, and so on, where $Z$ is the normalization constant. The indexes of the sorted individuals are stored in ibest. The best individual is preserved in $X_{\text {elite }}$ and $F_{\text {elite }}$. The probability values are used to compute the weighted mean and the variance estimators, as shown in [19]. The algorithm resets when stagnation is detected, using a counter of the number of consecutive generations the elite individual does not improve above a threshold, this is from lines 13 to 19. Then, the $f_{\text {reset }}$ value is stored. It is the previous best objective value found before resetting, and it is used to test whether the $f_{\text {elite }}$ improves or not between two resets, to stop the algorithm in case of no improvement. The search uses two search distributions to generate candidate solutions. One of them is computed in all the dimensions of the search space via a normal multivariate distribution, where each dimension is considered independent to each other, thus, only the diagonal of the covariance matrix is computed, stored, and used. The second is a distribution over a projection vector in a promising search direction. This vector is randomly generated and modified by applying to it random perturbations. Each time a perturbation is applied, the algorithm tests whether the

current projection vector $U$ is better than the previous one by computing the Spearman correlation between the projection of the current population and their corresponding objective function values. The greater the correlation, the better the projection vector is. Notice that a perfect correlation means that the projection vector is in a perfect increasing/decreasing direction on the objective function. Hence, the proposal is sampling in all dimensions with the multivariate distribution, then, it shifts the samples over the direction of the projection vector. This sampling process is carried out according to Algorithm 3. For each generation the algorithm generates $D$ new candidate solutions, in this case, 3 new candidate solutions, requiring a low number of function evaluations. In addition, the covariance matrix and variance of the distribution on the projection direction are scaled as follows: if $f_{\text {elite }}$ improves, then the variance is increased, otherwise it is decreased. If it does not improve during a number of generations, according to line 19 in Algorithm 2, the population is reset by generating uniform solutions around the elite, preserving the best $C_{\text {resets }}$ solutions.

## V. EXPERIMENTS AND RESULTS

To test the approach, we optimized the PGA parameters $\Theta$ given two maps of years 2011 and 2016, respectively belonging to wake County U.S.A ${ }^{1}$. We organized the Wake County region in training and test sub-regions as described in Fig. 1, where each cell represents a squared area of $30 \mathrm{~m}^{2}$.

To produce the training and test sub-regions we proceeded as follows: first, we partitioned the map into 10 random Voronoi polygons. Then, seven Voronoi polygons were randomly selected and labeled as training regions. The remaining three polygons were labeled and used as test regions and used to produce PGA simulations to compare them with the ground truth.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Training region of Wake County U.S. in 2011. Yellow and dark color represents the developed and developable area respectively. The white region is the non developable region. The two white polygonal regions are reserved to test the PGA simulation

The training region from 2011 contains 436,314 urban cells with an increment of 21,020 in 2016. Similarly, the test region from 2011 contains 264,457 cells with an increment of 11,876

[^0]
## Algorithm 2 EDALNFE

```
procedure EDALNFE \((f(\cdot), D)\)
    \(N p=8 D+2\)
    \(C_{\text {elite }}=0 ; C_{\text {resets }}=0\)
    \(X=\) initialize \((D, N p)\)
    \(F=\) evaluate \((X, f(\cdot)\)
    \([\) ibest, \(p_{S}]=\) selection \((F))\)
    \([X_{\text {elite }}, F_{\text {elite }}]=\left[X_{\text {ibest(1) }}, F_{\text {ibest(1) }}\right]\)
    \(f_{\text {reset }}=F_{\text {elite }(1)}\)
    \(U=\operatorname{rand}(D)\)
    while \(\operatorname{var}_{c}>\operatorname{var}_{\text {min }}\) do
        \([\dot{X}, U]=\) genNewInd \(\left(X, F, X_{\text {elite }}, p_{S}\right.\), ibest, \(\left.U\right)\)
        \(\bar{F}=\) evaluate \((X, f(\cdot))\)
        if \(\left|F_{\text {elite }}-F_{\text {ibest(1) }}\right|>\left|10^{-4} F_{1}\right|\) then
            \(C_{\text {elite }} \neq 0\)
            \(\left[F_{\text {elite }}, F_{\text {elite }}\right]=\left[X_{\text {ibest(1) }}, F_{\text {ibest(1) }}\right]\)
    else
        \(C_{\text {elite }}=C_{\text {elite }}+1\)
        end if
        if \(C_{\text {elite }}=\operatorname{integer}\left(15 C_{\text {resets }}+20\right)\) then
            \(C_{\text {resets }}=C_{\text {resets }}+1\)
            \(X_{\text {elite }}=X_{\text {best(1.. } C_{\text {resets }}}\)
            \(F_{\text {elite }}=F_{\text {best(1.. } C_{\text {resets }}}\)
            \(X=\) reinitialize \(\left(D, N p-1, C_{\text {resets }}, X_{\text {elite }}\right)\)
            \(F=\) evaluate \((X, f(\cdot))\)
            \([X, F]=\left[\left[X, X_{\text {elite }}\right],\left[F, F_{\text {elite }}\right]\right]\)
            \([\) ibest, \(p_{S}]=\) selection \((F)\)
            \(\left[X_{\text {elite }}, F_{\text {elite }}\right]=\left[X_{\text {ibest(1) }}, F_{\text {ibest(1) }}\right]\)
            \(U=\operatorname{rand}(D)\)
            \(C_{\text {elite }} \neq 0\)
            if \(F_{\text {elite(1) }}=f_{\text {reset }}\) or \(C_{\text {resets }}=N p / 2\) then
                break
            else
                \(f_{\text {reset }}=F_{\text {elite(1) }}\)
            end if
    end if
    \([X, F]=[X(i b e s t), F(i b e s t)]\)
    \([X, F]=[X(1 . . N p / 2), F(1 . . N p / 2)]\)
    \([X, F]=[[X, \dot{X}],[F, \dot{F}]]\)
    end while
    return \(\left[x_{\text {elite }}, f_{\text {elite }}\right]\)
    41: end procedure
```

urban cells in 2016. These developed cells were simulated with the best parameters found with the training regions.

We produced a suitability map by using the Logistic Regression model in Equation (1). The coefficients were estimated by using the lme 4 R package [20], to associate the urban land change produced in the 2011-2016 period given the information from 2011.

The urban land change is represented by using map algebra. The urban maps are binary where 1 means urban area, 0 means non-urban area, and null() means region not suitable for urbanization which includes protected and other excluded areas.

To produce two balanced classes for fitting the suitability function, we selected the $100 \%$ of cells presenting landuse change in the 2011-2016 period $(21,605)$, and a random sample with the same number of invariant non-urban from a total of 1,707,283 cells.

The coefficients of each variable associated with each map


[^0]:    ${ }^{1}$ These maps can be downloaded from: https://github.com/ ncsu-landscape-dynamics/GRASS_FUTURES/releases/tag/v2.0.0

Algorithm 3 Generate New Individuals

```
procedure \(\operatorname{GENNEWIND}\left(X, F, x_{\text {elite }}, p_{S}\right.\), ibest)
    if first-call=True then
        cnt \(=0 ; \sigma_{1}=-1 ; \sigma_{2}=-1 ; f_{\text {elite }}^{\text {local }}=1 e 100\)
    end if
        success=False
        if \(f_{\text {elite }}^{\text {local }}=F_{\text {ibest }(1)}\) and \(\sigma_{1}=-1\) then
            success=True
    end if
    \(f_{\text {elite }}^{\text {local }}=F_{\text {ibest }(1)}\)
    \(\mu_{X}=\) weightedColumnMean \((X, p)\)
    \(\sigma_{X}=\) weightedColumnsSD \(\left(\hat{X}, \mu_{X}, p\right)\)
    if success \(=\) False then
        cnt \(=\operatorname{cnt}+1\)
    end if
    increment=True
    if cnt \(\geq 6\) or cnt \(=0\) then
        \(\sigma_{X}=1.05 \sigma_{X}\)
        \(\operatorname{Scale}_{1}=\max \left(\sigma_{1} /\left|\sigma_{X}\right|, 1\right)\)
        if cnt \(=10\) then
            cnt \(=0\)
        end if
    else
        \(\sigma_{X}=0.6 \sigma_{X}\)
        \(\operatorname{Scale}_{1}=\min \left(\sigma_{1} /\left|\sigma_{X}\right|, 1\right)\)
        increment=False
    end if
    \(\sigma_{1}=\operatorname{Scale}_{1}\left|\sigma_{X}\right|\)
    \(U_{e}=U\)
    \(\operatorname{corr}_{\text {max }}=\operatorname{SpearmanCorr}\left(X U_{t}, F\right)\)
    for trial \(=1.2000\) do
        \(U_{t}=U_{e}+\operatorname{randn}(D) /(4 \sqrt{D})\)
        \(U_{t}=U_{t} /\left|U_{t}\right|\)
        \(\operatorname{corr}_{\text {trial }}=\operatorname{SpearmanCorr}\left(X U_{t}, F\right)\)
        if \(\left|\operatorname{corr}_{\text {trial }}\right|>\left|\operatorname{corr}_{\text {max }}\right|\) then
            \(\operatorname{corr}_{\text {max }}=\operatorname{sign}\left(\operatorname{corr}_{\text {trial }}\right) \operatorname{corr}_{\text {trial }}\)
            \(U_{e}=\operatorname{sign}\left(\operatorname{corr}_{\text {trial }}\right) U_{t}\)
        end if
    end for
    for \(i=1 \_D\) do
        \(\hat{X}_{i}=X_{\text {ibest }(1)}+\operatorname{Scale}_{1} \cdot \operatorname{randn}(D) \circ \sigma_{X}\)
    end for
        \(U=\left(0.05 U_{e}+0.95 U\right) /\left|0.05 U_{e}+0.95 U\right|\)
        \(\sigma_{t}=\operatorname{dot}\left(X_{\text {ibest }(1)}-X_{\text {ibest }\left(N p / 2\right)}, U_{e}\right)\)
    if increment=True then
        \(\operatorname{Scale}_{2}=\max \left(\sigma_{2} / \sigma_{t}, 1\right)\)
    else
        \(\operatorname{Scale}_{2}=\min \left(\sigma_{2} / \sigma_{t}, 1\right)\)
    end if
    \(\sigma_{2}=\operatorname{Scale}_{2} \sigma_{t}\)
    factor \(_{x}=0.6-2\left(\operatorname{corr}_{\text {max }}-1\right)^{2}\)
    for \(i=1 \_D\) do
        \(\hat{X}_{i}=\hat{X}_{i}+\left(\right.\) factor \(_{x}\) randn \(\left(\right)+\) factor \(_{x}\right) \sigma_{t} U\)
        boundToLimits \(\left(\hat{X}_{i}\right)\)
    end forreturn \([\hat{X}, U]\)
end procedure
```

TABLE 1
MAPS AND PARAMETERS FOR LOGISTIC REGRESSION
are presented in Table V.
The pressure map $p_{i}^{\prime}$ is computed with the following equation:

$$
p_{i}^{\prime}=\sum_{k=1}^{n_{i}} \frac{\text { STATE }}{d_{i k}^{n}}
$$

where STATE $\in\{1,0\}$, represents the developed or undeveloped state of cell $k$ in the neighborhood $i$. This equation models the assumption that cells near to the developed center are more likely to be developed and it is controlled with $\gamma$, which in this case is set to 0.5 . The suitability map is presented in Fig. 2.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Suitability map computed with the 21605 developed cells from 2011 to 2016 in the training region and 21605 random cells from the non developed cells

We compared the performance of the grid parameter identification approach implemented in the official FUTURES framework against both Differential Evolution (DE) and EDALNFE. The three approaches were limited to a maximum of 512 evaluations.

For the grid approach, every parameter was constrained to sets with 8 values evenly distributed from 0 to 1 , with the exception of the discount factor $\varphi$, since 0 means no patch histogram distributions. The discrete sets of parameters are presented in Equation (11).

$$
\begin{aligned}
\mu_{c} & =\{0.0,1 / 7,2 / 7,3 / 7,4 / 7,5 / 7,6 / 7,1\} \\
\sigma_{c} & =\{0.0,1 / 7,2 / 7,3 / 7,4 / 7,5 / 7,6 / 7,1\} \\
\varphi & =\{0.0001,1 / 7,2 / 7,3 / 7,4 / 7,5 / 7,6 / 7,1\}
\end{aligned}
$$

Therefore, we generated $512=\left|\mu_{c}\right| \times\left|\sigma_{c}\right| \times|\varphi|$ different combinations of parameters to evaluate.

For EDALNFE, the parameter search space was constrained by the intervals $0.01 \leq \mu_{c}, \sigma_{c} \leq 1$, and $0.0001 \leq \varphi \leq 1$.

For DE, the parameter search space was constrained by the intervals $0 \leq \mu_{c}, \sigma_{c} \leq 1$, and $0.0001 \leq \varphi \leq 1$.

The DE settings are those given by default in the scikitlearn implementation [21], but the population size was set to 16 with a maximum of 31 iterations to limit the optimization process to 512 evaluations with polish parameter to false to avoid the use of the L-BFGS-B optimization method after DE finishes.

We take as reference the Grid approach result where the best combined error found was 22.64 using 512 different evaluations. The number of evaluations are the $100 \%$ of the total time assigned to each optimization algoritm to optimize. The EDALNFE and DE were executed 5 independent times and the results are reported in Table II.

TABLE II
RESULTS OF 5 INDEPENDENT RUNS OF EDALNFE AND DE

For EDALNFE, we observed that for 4 out of 5 runs it obtained better results than Grid search with the lowest number of evaluations, but the first run with the worst result (combined error in bold) prematurely converged. The fifth execution presented the best combined error from all the executions. In the case of DE, 5 out of 5 runs obtained better results than the Grid search, stopping when 512 evaluations were reached.

## A. PGA Simulations With the Best Experimental Result

Once we found the best PGA parameters, we proceeded to simulate the urban land change with those parameters. The best combined error of 18.22 was obtained with the fifth execution of EDALNFE $\varphi=0.2663, \mu_{c}=0.113$ and $\sigma_{c}=0.998$.

Since every PGA execution produced a different scenario, we ran 100 PGA independent simulations by using the test sub-region hoping to observe a consistent PGA pattern.

In Fig. 3 we present the map of a frequency histogram in the geographical space, where darkest green areas are those where PGA simulated urban development more times. The orange cells represent the actual development observed from 2011 to 2016. From all the independent runs, the maximum number of times that a cell was urbanized was 20 out of 100.

In order to appreciate with more detail the PGA performance in the test regions, we zoom-in an arbitrary small region in Fig. 4 to observe with more clarity the PGA pattern.

In this map, the white cells are excluded areas not suitable for urbanization (e.g. they were developed in 2011, represents a water shape, or a protected region). The light green cells are suitable for development and darkest green cells are the cells with more simulated urban development according to PGA. The darkest cells show that 20 simulations generated urban
![img-2.jpeg](img-2.jpeg)

Fig. 3. Test region of PGA in year 2016
![img-3.jpeg](img-3.jpeg)

Fig. 4. Heat map of 100 runs. The Darkest regions where urbanized more times than light regions
developing and the lightest green cells show no urban land change in any simulation.

The orange regions are the actual developed regions used as ground truth for comparison purposes.

When contrasting the green dark region with the ground truth, we observed that most of the developed regions included at least a dark green cell. In the map, dark green areas represent approximately the same probability of being urbanized. These probabilities do not pretend to indicate exactly where urbanization will occur, but the level of uncertainty of the urban development process.

## VI. CONCLUSIONS

We presented the formulation of PGA calibration as an optimization problem. To the best of our knowledge, it is the first time that PGA is automatically calibrated with an optimization algorithm and contrasted to grid search.

We introduce the Estimation of Distribution Algorithm for a Low Number of Function Evaluations (EDALNFE), that was designed for the calibration task.

EDALNFE is a competitive optimization algorithm that does not require expert settings and addresses the generalized problem in Evolutionary Algorithms (EAs) of defining a stopping criterion. Most of the EAs arbitrarily stop when a number of generations or function evaluations is reached. Other implementations additionally used some criteria based on a lack of improvement of the elite individual. The results of the EDALNFE show that it is competitive against the DE and the grid search for the PGA calibration, highlighting the low number of the evaluations used to find the best results.

Nevertheless, none of these criteria actually measures convergence. The EDALNFE converge in distribution. The stopping criterion uses the variance of the objective function. For a continuous function, the convergence in the image ensures the convergence in the search space, but measuring the convergence in the objective function space (or image), is computationally cheaper than measuring it in the search space.

The EDALNFE delivers competitive results for this calibration task, thus, likely it would be competitive in other similar problems.

Hence, future work contemplate the application of EDALNFE to other calibration tasks.

In addition, in this work we measure the performance of the prediction using distances between histograms. Nonetheless, they are used in this work since they are recommended by the FUTURES' authors and because introducing a particular objective function for a novel algorithm could lead to a biased conclusion about the performance. Therefore, it is fair to use a standard objective function with a novel algorithm to ensure an unbiased comparison. In this same regard, these measures do not quantify the actual prediction. Thus, future work also contemplates proposing a suitable performance measure that actually quantifies the prediction of the urban land, considering the urban structure of the geographic space accompanied with more experiments to analyze statistically the performance of the optimization algorithms.

According to the experimental conclusions, we found that the size and shape patch distribution distances are not enough for assessing the PGA. It is necessary to consider and study in a deeper way at least two additional aspects:

1) To design a better urban-structure characterization that does not depend on the circle shape, but considers the diversity of the patch shapes. As a consequence it would be necessary to adapt the PGA or to create a new urban simulation model that considers the complex characteristics of the urban structure to produce more realistic urban scenarios.
2) To consider a metric or a distance that takes into account the mismatch of the land use prediction directly in the geographic space.
The design of an urban simulation model should be accompanied with a calibration methodology that benefits the applicability of the model. We also think that the PGA distribution maps can be generated using conditional probabilistic models that produce similar results and could potentially substitute PGA simulations, reducing the computational cost.

## ACKNOWLEDGMENTS

S. Ivvan Valdez, Rodrigo Lopez-Farias, and Alberto GarciaRobledo are supported by Cátedra-CONACYT 7795, 7029 and 6245 respectively. The experiments were executed in the CentroGeo cloud computing project "Nimbus".
