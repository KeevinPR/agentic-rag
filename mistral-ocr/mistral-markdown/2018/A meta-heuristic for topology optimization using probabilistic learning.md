# A meta-heuristic for topology optimization using probabilistic learning 

S. Ivvan Valdez ${ }^{1}$ () $\cdot$ José L. Marroquín ${ }^{2} \cdot$ Salvador Botello ${ }^{2} \cdot$ Noé Faurrieta ${ }^{2}$

(c) Springer Science+Business Media, LLC, part of Springer Nature 2018


#### Abstract

Topological shape optimization consists in finding the optimal shape of a mechanical structure by means of a process for removing or inserting new holes and structural elements, that is to say, using a process which produces topological changes. This article introduces a method for automated topological optimization via an Estimation of Distribution Algorithm (EDA), a global optimization meta-heuristic based on probabilistic learning, which requires of neither user initialization, nor a priori information or design bias in the algorithm. We propose a representation and solution mapping which favors feasible structures and requires a, relatively, low dimensionality (some hundreds), the probabilistic model learns from finite element evaluations to generate well-performed structures. The EDA for topology optimization (EDATOP) is compared with an algorithm, in the state of the art, specially designed to address this problem, demonstrating that our approach is useful for solving real-world problems, escapes from local optima, and delivers better solutions than the comparing algorithm which uses problem knowledge, with a payoff on the computational cost.


Keywords Topological optimization $\cdot$ Probabilistic learning $\cdot$ Global optimization $\cdot$ Estimation of distribution algorithm $\cdot$ Stress constraint

## 1 Introduction

The shape optimization problem is defined as to find the best shape of a structure for given design objectives [22].

For instance consider Fig. 1, an initial structure, a plate for 2-dimensional problems or a parallelepiped in 3 dimensions, is used to define boundary conditions, such as forces (loads) shown in red and fixed regions (supports) show with diagonal stripes. Thus, the goal of a topological shape optimization problem is to find another structure, in the given domain, which resists the same load conditions and performs the best in agreement with an objective

```
5 S. Ivvan Valdez
    ivvan@cimat.mx; si.valdez@ugto.mx
    José L. Marroquín
    jlm@cimat.mx
    Salvador Botello
    botello@cimat.mx
    Noé Faurrieta
    noe.faurrieta@cimat.mx
1 Division of Engineering, Universidad de Guanajuato,
    Salamanca, Guanajuato C.P. 36885, México
2 Center for Research in Mathematics, CIMAT, A.C. Jalisco
    S/N, Valenciana, Guanajuato, C.P. 36000 México
```

function. For the example in Fig. 1 the optimal shape is shown in blue. The objective functions are usually defined in two fashions: the first one is to maximize rigidity or stiffness at a given mass [27]. The second formulation consists in minimizing the mass, subject to stiffness (or stress) constraints [45], this is the one used in our proposal.

Topology optimization, is a kind of shape optimization problem, where the optimization algorithm must discover the number and shape of the holes and structural elements which compose the optimum design. In Fig. 1, if no initial holes are inserted in the structure, then the problem is a topology optimization problem. If the boundaries and initial holes are parameterized it is considered a shape optimization problem. If the structure does not change its shape and we are only looking for dimensions, the problem is considered a dimensional optimization problem.

We briefly review the state of the art methods for shape and topology optimization, with the purpose of contrasting the novelty of our proposal with existing ones. The methods can be grouped into five categories: homogenization or interpolation methods, level set methods, phase field methods, heuristics, and meta-heuristics.

Homogenization or interpolation methods [7, 13, 23, 24, 26, 48]. Assuming that the structures are evaluated using the

![img-0.jpeg](img-0.jpeg)

Fig. 1 Example of a topological shape optimization problem

Finite Element Method (FEM), homogenization methods are based on the idea that periodic micro-structures in a Finite Element (FE) $i$, can be described by a macroparameter $\psi_{i}$. It is supposed that any intermediate value of $\psi_{i}$ between $\psi_{\min }$ and $\psi_{\max }$ corresponds to some microstructure which occupies a proportion of the volume of the element, so the micro-structure is not as stiff as a solid element. The most popular homogenization method for topology optimization is the Solid Isotropic Material with Interpolation (SIMP) [6, 7, 42] and its variants. The governing model of the problem is rewritten using functions for the density $\rho\left(\psi_{i}\right)$ and the Young modulus $E\left(\psi_{i}\right)$ for each element $i$. Homogenization methods are commonly used to maximize the structure rigidity subject to a volume constraint, which requires a fraction of the original volume. A fixed point method is used to approximate the solution to the first optimality condition, that is to say, gradient is equal to 0 . Regularization, and morphological filters are used to improve the method [13]. The first intends to perform more robust approximations of properties such as gradient or density values, and the second intends to repair the checkerboard effect. Notice that a variable $\psi_{j}$ can be defined independently of the FEM mesh [42], for given points $j$, a smooth interpolation can be used for defining the density field.

Level set methods [1-4, 46, 47]. The most common level set methods work as follows: they compute a level set function $\gamma(x)$ where $x$ is defined over the physical domain where the structure is built. If $\gamma(y)<T$ then the structure has material at position $y$, otherwise the structure has no material in this place. The level set function must be initialized by the user. Then, it evolves in time using a Hamilton-Jacobi equation. This equation is connected with the gradient of the objective function with respect to the direction normal to boundary. Level set methods, have the advantages of being computationally efficient. They actually deliver material existence or void regions. Some proposals can generate holes [32], and are adequate for collapsing void regions $[3,4,49]$. In contrast, the local optimum, which the method converges, depends on the initialization. Often level set methods require reinitialization of the level set function to ensure convergence.

Phase field methods [9] are similar to level set methods, in the sense that a function describes the existence of material. A problem could be stated as a two-phase (void or non-void) or a multi-phase (multi-material) [8] problem. A phase field function describes the material properties (Young Modulus) in each region. Hence, it is used to rewrite the governing equations. The interface between regions is smoothly treated by the phase function. Hence, in the most simple scheme, we have a region with material, a region with void material and a smooth interface between the phases. The interface reduces numerical problems, in contrast with level set methods, and no reinitialization of the phase function is required. In addition, it naturally deals with body forces or design dependent loads [9]. Phase field methods are local optimization methods, which depend on user initialization.

Heuristics. Possibly the most popular heuristic for shape optimization is the Evolutionary Shape Optimization (ESO) [44] and its variants [29]. The idea is quite simple: given load conditions and a given initial domain, a FEM calculation is performed in order to measure a design variable or criterion, such as Von Mises stress or tensile stress. Then, the less efficient elements (less stressed elements) are removed according to a rejection criterion. Recent approaches have intended to provide mathematical formalization [17, 36]. An updated ESO method called bi-directional evolutionary optimization [25, 33], can aggregate and remove elements, and according to some authors [17], it is capable of avoiding ill-conditioned local solutions in contrast with ESO. In another heuristic, the bubble method [15], shape and topology optimization are combined in a single methodology, a sensitivity analysis is applied in order to determine where to insert a small hole (a bubble). Then, a shape optimization method (similar to a level set method) is executed to move the boundaries. Heuristics are efficient and simple, but, can present instability and convergence to undesired solutions. In addition, they cannot guarantee convergence to a global optimum, and the solutions depend on the initialization. When they do not find an adequate solution, they do not have any (automatic) procedure which considers a change on the rules or parameters.

Meta-heuristics $[5,10-12,19,20,30,31,34,41]$, are nondeterministic procedures that intend to automatically adapt the search according to the problem. The most common meta-heuristics in topology and shape optimization are evolutionary algorithms and other bioinspired algorithms. Usually, the algorithm starts with a randomly generated population of candidate solutions called individuals or particles (in the case of swarms). Then the population is evaluated, the best individuals are selected, variation operators are applied on the selected set in order to generate a new population, which is expected to be better than

the last one, and the best solution (called the elite) is preserved from one population to the next. The process is repeated from the evaluation step until the stopping criterion is met, and the elite solution is delivered as the best optimum approximation. The most common evolutionary algorithm in topology optimization is the Genetic Algorithm (GA). The most common solution representation in GAs is a binary vector, where each binary variable of the vector is associated with a finite element; if the variable takes the 0 value, then the element is void. Otherwise, it has material $[5,12,20,21]$. Hence, each individual in the population is a binary representation of a structure. The structures are evaluated. Then, some of them are selected for reproduction. Pairs of selected individuals, called parents, are recombined in order to produce children. Children are mutated, then they integrate the new population. A well known drawback of genetic algorithms is that they are not capable of managing a high number of variables (few hundreds) [18]. Hence the structures that can be built by this method are quite coarse. Different representations have been proposed to circumvent this problem, for instance in [16] and [40] a graph model which can be translated into a structure is proposed. Nevertheless, in these articles, the number of elements used in the numerical simulation is quite small. These methods can be extended to use an arbitrary number of finite elements and other conditions. The possible structures are limited in the number of parts or structural elements, and their sizes. Nevertheless GAs, usually, are not competitive with other approaches, such as homogenization, level set, etc., neither in objective value, esthetic quality of the results, nor in computational efficiency. The ant colony optimization [28, 30] has been modified for topology optimization, using the initial stress state to initialize the pheromone matrix, so that highly stressed elements are more probable to be visited. The particle swarm optimization [19] has been modified to deal with binary variables to perform topology optimization. A precursor of EDA used for topology optimization is the Population based Incremental Learning (PBIL) [10, 11]. It uses a probability distribution for sampling candidate solutions. Then, the best are selected and used to re-estimate the probability distribution using a weighted combination between the last distribution and the current frequencies (estimators of marginal probabilities). The process is repeated until a termination criterion is reached. Other proposals [31] combine stages of topology optimization with sizing optimization, so that once an adequate topology has found, it is converted to a set of trusses and refined to increase its performance.

In summary, the advantages of evolutionary and biosinpired algorithms (EAs) is their capacity to propose different topologies without user bias. They can tackle realistic optimization problem formulations. They consider existence and absence of material and no intermediate materials,
and they are global search methods. However, they usually only can handle a few optimization variables (tens). Many approaches handle as many finite elements as variables. Thus, the numerical simulations are rough. EAs, usually, do not refine solutions, so that these solutions, usually, are not as well performed as those delivered by local-search methods. In contrast, local-search methods cannot remove highly stressed or displaced elements. This is because they are formulated for removing the less stressed/displaced elements. However, there are cases of stress concentrations due to geometric abrupt changes, where removing stressed elements could be an adequate strategy. In other words, local-search methods could be trapped in a local minimum. While, meta-heuristics are less prone to converge to it.

Our approach tackles an objective function of weight or volume minimization considering body forces, subject to stress and displacements constraints. To the best of our knowledge there is no other approach which considers the same problem. The most common objective function is compliance minimization subject to volume constraints, using continuous variables for the material properties. There are some weight minimization approaches, but they only consider one of the two constraints: stress or displacements [43], and rarely consider body forces or design dependent loads. Notice that a stress constraint not only characterizes the structure functionality; in addition, a maximum stress characterizes the material elastic range. Hence, if stress constraints are not considered, the structure is physically unfeasible, and the usual numerical simulation is not adequate, because out of this range one must not use a linear-elastic model. In addition, even though our optimization model considers stress and displacement constraint, when unfulfilled, both constraints activate a displacement penalization, according to the authors experience and the most well performed methods displacement guides better the search [37]. In this article, we propose a meta-heuristic optimization algorithm, from the kind of evolutionary algorithms called Estimation of Distribution Algorithms (EDAs) for continuous domains. EDAs start by using a uniform distribution $Q_{X}^{0}$ to sample a random population of candidate solutions. Then they are evaluated, the best solutions are selected and used to re-estimate $Q_{X}^{i}$. In contrast with other metaheuristics, our optimization method actually delivers competitive structures with all the state of the art methods by working with structures evaluated with an arbitrary large number of finite elements. A key feature is to consider separately the optimization problem from the finite element evaluation using a similar idea to the one presented in [42]. In contrast with deterministic methods mentioned above, our proposal does not need initialization, and can perform a global search. During the optimization process our proposal works with two materials: the first one is stiff with high-density, and the second is weak with low density, but

the final solution is actually stiff material or void. We only use the weak material to avoid numerical singularities during the optimization process. A remarkable difference with existing methods is that our problem formulation and case studies guarantee that the final solution is made of a physically real material (steel), and that it is working in the elastic range. We test our proposal named EDA for topology optimization (EDATOP) on a benchmark [37] selected from more than one hundred articles in specialized literature. We use realistic material properties, in contrast with many proposals which use realistic dimensions but unrealistic Young and Poisson modulus and density [37]. In summary, our aim is to introduce a topology global optimization algorithm for solving a set of realistic test problems, considering the case of weight minimization subject to stress and displacement constraints.

The rest of the paper is organized as follows: in Section 2 we present our optimization problem formulation. Section 3 introduces the optimization method. Section 4 presents a set of case studies and results of our proposal, and Section 5 is the concluding remarks and future work.

## 2 Problem definition and representation

In order to define the elasto-mechanical problem boundary conditions and loads are set in an initial domain $\Omega$, as it is shown in Fig. 2a. This domain is discretized with a coarse mesh as in Fig. 2b. Each node is associated with a continuous variable $\phi_{i}$, as shown in Fig. 2c. The algorithm generates samples of each $\phi_{i}$, initially in the domain of $[0,1]$, and in subsequent iterations using a normal distribution which mean and variance are learned from the samples. In Fig. 2d, the $\phi$ values are interpolated in order to obtain a materialcontinuous function $\hat{\phi}$ (a level set function). In Fig. 2e, if the function value is above 0.5 , then the structure has material, otherwise it does not. Notice that this idea is applicable over two or three dimensions without any modification. Figure 2 f shows the evaluation of a candidate solution using the FEM, and finally, the best candidate solutions are selected to re-estimate the probability distribution as shown in Fig. 2g.

To obtain a continuous smooth function from a set of values in the nodes we apply an interpolation based on the minimization of a regularization functional in (1), as explained in Fig. 3.
$U(\phi)=\sum_{\mathbf{x}_{i} \in C M}\left(\phi\left(\mathbf{x}_{i}\right)-\hat{\phi}\left(\mathbf{x}_{i}\right)\right)^{2}+\lambda \int_{\Omega}|\nabla \phi(\mathbf{x})|^{2} d \mathbf{x}$
There are two meshes: the fine mesh and the coarse mesh $(C M)$, whose node positions are $\mathbf{x}_{i}=\left(x_{i}, y_{i}\right)$ for $i=1,2, . ., n_{\text {nodes }}$. On each node of the coarse mesh there is a value $\phi_{i}$, which is represented in the figure as a height with a square at the end; these values are filtered
and interpolated by minimizing the functional, resulting in $\hat{\phi}\left(\mathbf{x}_{i}\right)=\hat{\phi}_{i}$, which are represented in Fig. 3, as heights with a circle at the end. Notice that the minimization of the first term in (1) requires similar values for $\hat{\phi}_{i}$ and $\phi_{i}$. While, the second term requires similar values for $\hat{\phi}_{i}$ and its neighbors. The parameter $\lambda$ regulates the smoothness of the function. Hence, given a regular function defined by $\hat{\phi}_{i}$, shown as a shadowed surface in the figure, one can compute the value of the function at any point $(x, y)$ of the domain. For this proposal, it is of interest to compute $\hat{\phi}\left(x_{k}, y_{k}\right)$ at centroid positions $\left(x_{k}, y_{k}\right)$ of the fine mesh elements. If $\hat{\phi}\left(x_{k}, y_{k}\right) \geq 0.5$, then the $k-t h$ element has material, otherwise it does not. The functional is minimized by solving the associated Euler-Lagrange PDE using the Finite Element Method, which generates a linear system of equations; then, it is quite simple to obtain $\hat{\phi}_{i}$ as a unique solution for this system. The FEM-shape function can be used to interpolate the values at centroids of the fine mesh, in this case we use Lagrangian quadrilateral elements with four Gauss points.

### 2.1 Objective function

The optimization problem is defined as to find the topology and shape of a mechanical structure with minimum weight so that the maximum von Mises stress does not exceed a given yield stress, and maximum displacements in the loaded nodes do not exceed a given value. The goal as well as the constraints are handled by the objective function in (2).

$$
\begin{gathered}
\min F(\varphi)= \begin{cases}1+U(\varphi) & \text { if } V M(\varphi)>0 \text { or } U^{e x}(\varphi)>0 \\
\frac{W(\varphi)}{W_{\max }} & \text { otherwise. }\end{cases} \\
\text { S.t. } \\
K(\varphi) u=f(\varphi) . \\
\text { Where } \\
\varphi_{k}= \begin{cases}1 & \text { if } \hat{\phi}\left(x_{k}, y_{k}\right)>0.5 \\
0 & \text { ot herwise }\end{cases}
\end{gathered}
$$

In (2), $\varphi=\left\{\varphi_{k}\right\}$ for $k=1 \ldots n_{\text {elements }}$, is a vector of binary variables that represents whether an element in the fine FEM mesh, used for evaluating the elasto-mechanical problem, has material. The binary variable $\varphi_{k}$ is equal to 1 if the level set function $\hat{\phi}$, evaluated at the centroid $\left(x_{k}, y_{k}\right)$ of the $k-t h$ element of the fine FEM mesh, is greater than 0.5 , as it is explained in the previous section. The sum of displacements that exceed the maximum allowable value $U^{e x}(\varphi)$, the sum of displacements in the loaded nodes $U(\varphi)$, the sum of von Mises stresses that exceed the maximum allowable value $V M(\varphi)$, and the weight $W(\varphi)$ depend on $\varphi$. Equation (3) states the elastic constraint: $K(\varphi)$ is the stiffness matrix, $u$ are displacements, and $f$ are external forces, including self weight which depends on $\varphi$. This objective function

![img-1.jpeg](img-1.jpeg)

Fig. 2 Schematic representation of the proposed algorithm
computes the proportion of volume/weight of the current structure if it is feasible; accordingly, any feasible structure has an objective value less than 1 . Otherwise the objective function returns 1 plus the sum of the displacement norms in the loaded nodes. Thus, any unfeasible structure has an objective value greater than 1. In addition, for the case of unfeasible structures, if they exceed only the maximum von Mises stress, the smaller the displacements are, the smaller the objective function is. We have proposed this objective function after analyzing results among different functions that penalize stresses and/or displacements, and we have found that displacements are better for guiding the search. This is consistent with the fact that deterministic
methods that have good performance, such as SIMP [7], use a displacement guided search (compliance). These same methods apply interpolations or filtering of the objective gradient, for the sake of reducing numerical errors; these errors are often inherited to stresses, delivering an imprecise stress quantification. In consequence, objective functions based on stresses could be deceptive.

According to (2) the objective function is divided in two parts as follows: in the case that the displacements and stresses are below the given limits, the structure is feasible. Hence, the objective function is computed with the term in the second row, which measures the relative weight of the structure with respect to the full domain with material. If

![img-2.jpeg](img-2.jpeg)

Fig. 3 Representation of the process to obtain a smooth function $\hat{\phi}(x, y)$ from optimization variables $\phi_{i}$
the stresses or displacements are above the given limits, the objective value is 1 plus the sum of displacements in the loaded nodes. That goes to say, if the structure is unfeasible the objective function is always greater than that from a feasible structure, and the smaller the displacement is the better a unfeasible structure is. The purpose of this function is to use unfeasible structures for guiding the search to sampling more rigid structures, while the feasible ones guide the search to reducing the weight. Notice that the constraints given by the maximum von Mises stress and maximum displacement are managed by the first term of the objective function, and without regard to which one of them is violated, the objective function uses the displacements as penalization term. As mentioned the displacements are less prone to numerical errors, other advantage is that the penalizations are in the same scale independent of the constraint violated.

Equation (4) is used to compute the sum of exceeding von Mises stresses $V M(\varphi)$; the indicator function $\gamma_{\text {stress }}\left(\sigma_{k}\right)$ is 1 if the von Misses stress $\sigma_{k}$, at element $k$, is greater than the yield stress $\sigma_{\max }$.

$$
\begin{aligned}
V M(\varphi) & =\sum_{i=1}^{n_{\text {elements }}} \varphi_{k} \gamma_{k}\left(\sigma_{k}\right) \\
\gamma_{\text {stress }}\left(\sigma_{k}\right) & =\left\{\begin{array}{l}
1 \text { if } \sigma_{k}>\sigma_{\max } \\
0 \text { otherwise }
\end{array}\right.
\end{aligned}
$$

Equation (5) below is used to compute the sum of the displacements exceeding the maximum displacement constraint $U^{e x}(\varphi)$ at the loaded nodes. $n_{\text {loaded }}$ is the number of loaded nodes, $\left|\delta_{l}\right|$ is the displacement norm at the $l-t h$ node. $\gamma_{\text {disp }}$ indicates whether there exists a node that exceeds the maximum allowed displacement.

The maximum allowed displacement $\delta_{\max }$ is a user-given parameter.

$$
U^{e x}(\varphi)=\gamma_{\text {disp }}(\delta) \cdot \sum_{l=1}^{n_{\text {loaded }}}\left|\delta_{l}\right|
$$

$\gamma_{\text {disp }}(\delta)=\left\{\begin{array}{l}1 \text { if any } \delta_{l}>\delta_{\max }, l=1 . . n_{\text {loaded }} \\ 0 \text { otherwise }\end{array}\right.$

## 3 Optimization algorithm

We address the problem via an Estimation of Distribution Algorithm for global optimization (EDA), which we call EDA for topology optimization (EDATOP). EDAs are stochastic optimization methods which perform global search by building and sampling from probabilistic models. The optimization variables are denoted as $\phi \in \mathbb{R}^{n_{\text {var }}}, n_{\text {var }}=$ $n_{\text {nodes }}-n_{\text {cond }}$, where $n_{\text {nodes }}$ are the number of nodes in the coarse mesh, while $n_{\text {cond }}$ are the nodes with forces or fixed-displacement conditions. EDAs are population based algorithms; thus, they sample a population of candidate solutions often called individuals. In this case, an individual is a real-valued vector $\phi_{i}$ of values at the nodes of the coarse mesh, which are translated into a structure by applying the process described in Section 2 and Fig. 3. A fitness value must be computed for each individual by means of (2). In summary, the workflow for evaluating an individual is as follows: given an individual $\phi$, apply the process described in in Section 2 and Fig. 3 to obtain regularized values $\hat{\phi}_{i}$; using $\hat{\phi}_{j}$ and the shape-FEM functions one can interpolate values $\hat{\phi}\left(x_{k}, y_{k}\right)$ for the centroids of the elements of the fine mesh. Then, using (3), $\hat{\phi}\left(x_{k}, y_{k}\right)$ is binarized resulting in a value $\psi_{k}$ which, if it equals 1 , indicates the existence of material in the $k-t h$ element of the fine mesh. This is used in conjunction with the FEM method to compute stresses and displacements. The EDA for continuous variables, introduced here, uses weighted estimators for the mean and variance of independent Gaussian probability functions, similar to [38] and [39]. The general work-flow is described in Algorithm 1. Line 1 initializes a generation counter used as superindex to indicate variable updating and used as stopping criterion. Line 2 initializes the probability model with a uniform distribution in the range $[0,1]$ for all variables. In line 3, we simulate the initial sample of $2 n_{\text {pop }}$ candidate solutions which are called a population. Note that only the initial population is of size $2 n_{\text {pop }}$; the subsequent ones are of size $n_{\text {pop }}$. A candidate solution, in this case, is a vector of real values of size $n_{\text {var }}$, which in turn can be translated into a structure. In line 4 , the initial population $\Phi^{0}$ is evaluated by means of the FEM, i.e., it is used to solve the elastic problem, determining displacements and stresses to compute the objective function in (2). In line

5, we compute two sets: the so called, selected set $S^{0}$ used to update the probability distribution, and an elite set $\Phi_{\text {Best }}^{t}$ used to maintain a history of the best solutions found. For any $t, S^{t}$ is at most of size $n_{\text {pop }} / 2$ while $\Phi_{\text {Best }}^{t}$ is of size $n_{\text {pop }}$. The main loop of the algorithm starts in line 6. In line 8, the probability model is updated by means of computing $n_{\text {var }}$ independent Gaussian probability functions with parameters given by a vector of standard deviations $\Sigma$ and a mean vector $\mu$. The detailed computation of these parameters is revised in the next subsection. In line $9, n_{\text {pop }}-1$ candidate solutions are generated using the updated probability model $Q^{t}$, and they are evaluated in line 10. In line 11, the best individual, $\phi_{\text {Best }}^{t}$, is reinserted in the population. Finally, in line 12, the last elite set $\Phi_{\text {Best }}^{t-1}$ is added to the current population $\Phi^{t}$, and a set of the best $n_{\text {sel }}$ individuals are selected. The selection method, described below, guarantees that the best solution found $\Phi_{\text {best }}^{t}$ is stored and preserved through all generations. The process is repeated from line 7 until the stopping criterion is reached. The main differences of our algorithm with similar ones is given by the selection method, the computation of the parameters of the probability model and, the stopping criteria. These topics are discussed in the next subsections.

```
Algorithm 1: EDA for topology optimization
    (EDATOP)
    Input: \(n_{\text {pop }}=\) Population size.
    \(n_{\text {gen }}=\) Maximum number of generations.
    Data: \(n_{\text {var }}=\) Number of variables ( \(\phi\) size).
    Result: \(\phi_{\text {Best }}^{t}=\) Best optimum approximation
    \(t=0\);
    \(Q^{0}(x)=\) Initial_probability_model();
    \(\Phi^{0}=\) Generate_a_random_population* \(\left(Q^{0}\right)\);
    \(F^{0}=\) Evaluation \(\left(\Phi^{0}\right)\);
    \(\left[S^{0}, F_{S}^{0}, \Phi_{\text {Best }}^{0}, F_{\text {Best }}^{0}\right]=\) Selection* \(\left(F^{0}, \Phi^{0}\right)\);
    while stopping criterion is not met do
        \(\mathrm{t}=\mathrm{t}+1\);
        \(Q^{t}(\Sigma, \mu, \phi)=\operatorname{Compute} \_\)probability_model \(\left(S^{t-1}\right)\);
        \(\hat{\Phi}^{t}=\) Generate_a_random_population \(\left(Q^{t}\right)\);
        \(\hat{F}^{t}=\operatorname{Evaluation}\left(\hat{\Phi}^{t}\right)\);
        \(\left[\Phi^{t}, F^{t}\right]=\left[\hat{\Phi}^{t} \cup\left\{\phi_{\text {Best }}^{t}\right\}, \hat{F}^{t} \cup\left\{f_{\text {Best }}^{t}\right\}\right]\);
        \(\left[S^{t}, F_{S}^{t}, \Phi_{\text {Best }}^{t}, F_{\text {Best }}^{t}\right]=\) Selection \(\left(\Phi^{t}, F^{t}, \Phi_{\text {Best }}^{t-1}\right.\)
        \(\left.F_{\text {Best }}^{t-1}\right)\);
```


### 3.1 Selection method

In the selection step, lines 5 and 12 of Algorithm 1, we compute two sets: $S^{t}$ and $\Phi_{\text {Best }}^{t} . S^{t}$ is used for updating the probability distribution parameters; as mentioned, it is a set of variable size between $\left[1, n_{\text {pop }} / 2\right]$, which contains the
individuals with best performance. This set inserts the bias in the probability distribution to sample more intensively the most promising regions. The second set $\Phi_{\text {Best }}^{t}$ is of fixed size $n_{\text {pop }}$; it stores the best individuals found up to the current generation $t$. Note that $S^{t}$, which is always a subset of $\Phi^{t}$, is used to estimate the probability distribution and to bias the search. $\Phi^{t}$ is a history of size $n_{\text {pop }}$ of the best solutions found whether they are used to update the probability model or not. The initial $\Phi_{\text {Best }}^{0}$ consists of the best $n_{\text {pop }}$ individuals in the initial population $\Phi^{0}$. For the remaining generations $\Phi_{\text {Best }}^{t}$ is computed as the best $n_{\text {pop }}$ individuals in $\Phi^{t} \cup \Phi_{\text {Best }}^{t-1}$. For the sake of computing the selected set $S^{t}$, a truncation method similar to the one introduced in [38] is used. Consider the $n_{\text {pop }} / 2$ best individuals in $\Phi_{\text {Best }}^{t}, S^{t}$ consists of those individuals whose objective values are less or equal than a threshold $\hat{\theta}^{t}=\theta^{t}-$ $10^{-5}$. The initial $\theta^{0}$ is set to infinity (or a very large positive
![img-3.jpeg](img-3.jpeg)

Fig. 4 Cantilever problems, loaded at top (CLT), center (CLC) and bottom (CLB)

number). Consequently, the first selected set $S^{0}$ consists of the $n_{\text {pop }} / 2$ individuals in $\Phi_{\text {Best }}^{t}$ with the minimum (best) objective function value. For the remaining iterations, $\theta^{t}=$ $\min \left(\theta^{t-1}, F\left(\Phi_{\text {Best }}^{t}\right)_{\pi_{n_{\text {pop } / 2}}}\right)$, where $\pi$ are the indexes of the increasingly sorted objective values of $\Phi_{\text {Best }}^{t}$; therefore $\pi_{n_{\text {pop }} / 2}$ is the $\left(n_{\text {pop }} / 2\right)^{t h}$ position and $F\left(\Phi_{\text {Best }}^{t}\right)_{\pi_{n_{\text {pop }} / 2}}$ is the corresponding objective function value. Notice that the threshold for computing $S^{t}$ is, actually, $\hat{\theta}^{t}$, not $\theta^{t}$; in consequence we can guarantee that the worst individual in $S^{t}$ is always improving with $t$ (it is an increasing sequence). This ensures convergence to the best solution found. In summary, we select the solutions above a threshold $\theta^{t}$ (or above or equal to $\hat{\theta}^{t}$ ), which initially is the worts objective function in the population, and then it is the best between the threshold from the last iteration or the individual in the position $n_{\text {pop }} / 2$, hence the size of the selected set, denoted by $n_{\text {select }}$ is variable, because the selection method requires that the worst individual in the current selected set must be better than the worst individual in the last one.

### 3.2 Computing the probability model

The probability model is a set of independent Gaussian probability distributions $Q=\left(Q_{1}, \ldots Q_{n_{\text {corr }}}\right)$ associated with each variable $\phi_{m}$ at node $x_{m}, y_{m}$ of the coarse grid. The Gaussian distribution $Q_{m}\left(\phi_{m}, \mu_{m}, \sigma_{m}\right)$ for the $m-$ th variable is defined in the range of $[-\infty, \infty]$ given the parameters of mean $\mu_{m}$ and variance $\sigma_{m}^{2}$. Consider a selected set $S^{t}$ of size $n_{\text {select }}$ sorted according the objective function value in ascending order. A ranking function for each element in $S^{t}$ is defined as in (6).
$g\left(\pi_{i}\right)=n_{\text {select }}-i+1$
The best solution, in the first position, that is to say $\pi_{1}$, gets the value $g\left(\pi_{1}\right)=n_{\text {select }}$, the second best gets the value $g\left(\pi_{2}\right)=n_{\text {select }}-1$, and so on. Using $g(\cdot)$ we compute weighted estimators for the mean and variance. The mean parameter of the $m-t h$ variable is computed with (7) and

Table 1 Cantilever results

| Cantilever loaded at top |  |  |  |
| :-- | :-- | :-- | :-- |
| Data | SIMPSC | EDATOP | GA |
| Iterations |  | 445 | 540 |
| Final Vol. | 0.9257 | $\mathbf{0 . 4 5 6 8 7 4}$ | 1.659374 |
| Final Vol. frac. | 0.46289 | $\mathbf{0 . 2 2 8 4 3 7}$ | 0.829687 |
| \|Displacement $\mid$ | $\mathbf{2 . 3 1 1 7 E - 3}$ | $5.892646 \mathrm{E}-5$ | 0.016967 |
| SF | 0.968896 | 0.9909091 | 0.9417818 |
| Avg(VM/YS) | 0.27649 | $\mathbf{0 . 5 3 3 2 5 4 6}$ | 0.1241781 |
| SD(VM/YS) | 0.056441 | 0.2232552 | 0.116405 |
| Max VonMises | 2.193157 e 8 | 2.1797 e 8 | 2.07192 e 8 |
| Cantilever loaded at center |  |  |  |
| Iterations |  | 538 | 540 |
| Final Vol. | 1.271483 | $\mathbf{0 . 5 6 4 6 8 8}$ | 1.900624 |
| Final Vol. frac. | 0.6357417 | $\mathbf{0 . 2 8 2 3 4 4}$ | 0.950312 |
| \|Displacement $\mid$ | $\mathbf{2 . 1 4 0 0 7 E - 3}$ | $5.176993 \mathrm{E}-3$ | $1.92579 \mathrm{e}-3$ |
| SF | 0.9996258 | 0.9898682 | 0.9543818 |
| Avg(VM/YS) | 0.22621 | $\mathbf{0 . 5 2 3 0 5 2 2}$ | 0.1576364 |
| SD(VM/YS) | 0.069561 | 0.22111 | 0.1083356 |
| Max VonMises | 2.199177 e 8 | 2.17771 e 8 | 2.09964 e 8 |
| Cantilever loaded at bottom |  |  |  |
| Iterations |  | 454 | 540 |
| Final Vol. | 0.9257 | $\mathbf{0 . 4 4 5 9 3 8}$ | 1.682032 |
| Final Vol. frac. | 0.46289 | $\mathbf{0 . 2 2 2 9 6 9}$ | 0.841016 |
| \|Displacement $\mid$ | 2.3117E-3 | $5.647418 \mathrm{E}-3$ | $2.34258 \mathrm{e}-3$ |
| SF | 0.9968896 | 0.9899091 | 0.945073 |
| Avg(VM/YS) | 0.27649 | $\mathbf{0 . 5 3 3 5 6 9 4}$ | 0.1297626 |
| SD(VM/YS) | 0.056441 | 0.2131123 | 0.1165115 |
| Max VonMises | 2.193157 e 8 | 2.1778 e 8 | 2.07916 e 8 |

variance with (8). $\phi_{i, m}^{S^{t}}$ is the $m-t h$ element of the $i-t h$ individual in $S^{t}$,
$\mu_{m}^{t}=\frac{1}{\sum_{i}^{\mu_{\text {select }}} g(i)} \sum_{\phi_{i}^{S^{t}} \in S^{t}} \phi_{i, m}^{S^{t}} g(i)$
$\sigma_{m}^{2}=\frac{1}{\sum_{i}^{\mu_{\text {select }}} g(i)} \sum_{\phi_{i}^{S^{t}} \in S^{t}}\left(\phi_{i, m}-\mu_{m}\right)^{2} g(i)$.
As $S^{t}$ could be of variable size, these formulae are only applied if the size is greater than 1 , otherwise $\sigma^{t}$ is 0 and $\mu^{t}$ is the value of such unique individual.

### 3.3 Stopping criteria

We use two stopping criteria: a maximum number of generations and a minimum value of the standards deviation norm, $\|\Sigma\|<0.01 n_{\text {nodes }}$. The algorithm stops if one of them is reached. In all the case studies reported here the second one is always applied.

### 3.4 Numerical considerations

The final solution only considers material or void, which can be interpreted as two Young moduli: $E_{1}$ which is the actual material property, and $E_{0}=0$. During the optimization process however, we consider $E_{0}=10^{-5} E_{1}$, in order to evaluate disconnected or singular structures. For the purpose of compensating the consideration above, we multiply the yield stress and maximum displacement by 0.99 . Hence during the optimization process the stress and displacement constraints are more conservative, expecting that at the end, when using void material, they are fulfilled. The algorithm, in all cases, has converged to feasibleconnected structures, whose displacements and stresses, computed during the optimization process, are practically equal to the final ones (i.e., those with $E_{0}=0$ ). The reported figures and quantitative results correspond to those that consider only presence and absence of material. The elements with boundary conditions, that is to say elements with forces or fixed nodes (supports) have probability 1 of having solid material.

Fig. 5 Results for CLT
![img-4.jpeg](img-4.jpeg)

## 4 Case studies

We present 8 case studies widely used in specialized literature; they were selected from an analysis of more than 100 articles [37]. The quantitative results are compared with a version of the SIMP [35] for volume minimization subject to a stress constraint (SIMPSC) [37] and with a genetic algorithm (GA) which uses the same operators and way of working than the Omnioptimizer [14], crossover probability of 0.9 and mutation probability of $1 / n_{\text {var }}$, the representation for the GA is the same than that of the EDATOP, as well as the population size, the number of generations is similar to that of the EDATOP and is reported for each case study.

The SIMP [35] is a deterministic method which delivers competitive results for the compliance minimization problem, subject to a volume constraint. The compliance is measured as $u^{T} K u$, where $u$ are nodal displacements and $K$ is the stiffness matrix in a FEM problem. The constraint states that the final structure volume must be a fraction of the initial one. To use SIMP for volume minimization, SIMPSC [37] sets an initial volume fraction as constraint, usually as 0.5 , and then SIMP is applied in order to minimize compliance
at such volume; if the resulting structure violates the yield stress, SIMPSC increases the volume fraction, and otherwise it decreases it. The volume fraction is increased or decreased using a bisection method until convergence.

For these case studies we perform a quantitative comparison of our results with those delivered by the SIMPSC and the GA, using the following measures:

- Final volume. It is the volume of the optimum structure approximation in square meters. The smallest is the best.
- Final volume fraction. It is the final volume proportion with respect to the whole domain. The smallest is the best.
- Average of the norm of displacements. We compute the norm of the $x$ and $y$ displacements in the loaded nodes, then we compute the average. In our proposal the displacements are a constraint; for all cases the maximum allowable displacement is set to 0.1 m . The smaller the displacement, the more stiff is the structure; note however that in our proposal, this value only has effect if it exceeds the maximum allowed value.

Fig. 6 Results for CLC
![img-5.jpeg](img-5.jpeg)

Fig. 7 Results for CLB
![img-6.jpeg](img-6.jpeg)

Fig. 8 Short cantilever problems, loaded at top (SCLT), center (SCLC) and bottom (SCLB)
![img-7.jpeg](img-7.jpeg)
1.0 (L)
![img-8.jpeg](img-8.jpeg)
1.0 (M)
1.0 (M)
1.0 (L)
![img-9.jpeg](img-9.jpeg)
1.0 (M)
1.0 (M)
1.0 (L)

- Security factor (SF). The security factor is defined as the maximum elemental von Mises stress in the structure divided by the yield stress. The security factor intends to measure whether the structure is prone to fail, the security factor must be less or equal than 1 .
- Average of von Mises stress divided by the yield stress (Avg(VM/YS)). This value gives a rough idea
of the structure efficiency; we take every elemental von Mises stress divided by the yield stress, and call this the elemental efficiency; then we compute the average. The closest to one this value is, the most efficient is the structure, meaning that every element in the final shape is working close to its maximum capacity.

Fig. 9 Results for SCLT
![img-10.jpeg](img-10.jpeg)

- Standard deviation of VM/YS. This value gives an idea of the uniformity of the von Mises stresses over all elements.
- Maximum von Mises stress. The maximum elemental von Mises stress is reported in order to show that the delivered structure is feasible.

For the optimization problem the yield stress is set to $2.2 E 8 N$ and the maximum displacement to 0.1 m . As mentioned before, the smoothing factor in (1) is set to $\lambda=0.4$ for all cases. We recommend this value as a constant for any problem; hence the only parameter for the algorithm is the population size; we use a population size of 3600 for all cases.

Fig. 10 Results for SCLC
![img-11.jpeg](img-11.jpeg)

The coarse as well as the fine mesh use quadrilateral elements.

### 4.1 Cantilever

In this subsection we present 3 variations of the Cantilever problem: with a load at top (CLT), center (CLC) and bottom
(CLB). Figure 4 shows the external forces and conditions. The loads are $6.2 E 4,8.6 E 4$ and $6.2 E 4 N$ for CLT, CLC and CLB respectively. The loads are distributed in 0.1 m of the right side. The left side has 0 fixed displacement. The results of this case study are summarized in Table 1.

Figure 5 presents visual results of the optimal approximation. The figure labeled as "probability at iteration

Fig. 11 Results for SCLB
![img-12.jpeg](img-12.jpeg)

Table 2 Short cantilever results

| Short cantilever loaded at top |  |  |  |
| :-- | :-- | :-- | :-- |
| Data | SIMPSC | EDATOP | GA |
| Iterations |  | 324 | 370 |
| Final Vol. | 0.26367 | $\mathbf{0 . 1 3 0 9}$ | 0.7424 |
| Final Vol. frac. | 0.26367 | $\mathbf{0 . 1 3 0 9}$ | 0.7424 |
| \|Displacement $\mid$ | $\mathbf{1 . 0 4 2 7 E - 3}$ | $2.17423 \mathrm{E}-3$ | $9.75 \mathrm{E}-04$ |
| SF | 0.99795 | $\mathbf{0 . 9 8 6 3 9 0 9}$ | 0.9412636 |
| Avg(VM/YS) | 0.37014 | $\mathbf{0 . 5 8 5 5 4 9 8}$ | 0.09823871 |
| SD(VM/YS) | 0.043981 | 0.237214 | 0.1093163 |
| Max VonMises | 2.195505 e 8 | 2.17006 e 8 | 2.07078 e 8 |
| Short cantilever loaded at center |  |  |  |
| Iterations |  | 362 | 370 |
| Final Vol. | 0.43945 | $\mathbf{0 . 1 8 0 4}$ | 0.7447 |
| Final Vol. frac. | 0.43945 | $\mathbf{0 . 1 8 0 4}$ | 0.7447 |
| \|Displacement $\mid$ | $\mathbf{6 . 9 8 2 1 E - 4}$ | 0.001867846 | $8.20 \mathrm{E}-04$ |
| SF | 0.99822 | $\mathbf{0 . 9 8 9 6 0 9 1}$ | 0.9666364 |
| Avg(VM/YS) | 0.27610 | 0.5900248 | 0.1249533 |
| SD(VM/YS) | 0.05435 | 0.2390476 | 0.1296907 |
| Max VonMises | 2.196099 e 8 | 217714000 | 2.1266 e 8 |
| Short cantilever loaded at bottom |  |  |  |
| Iterations |  | 282 | 370 |
| Final Vol. | 0.263672 | $\mathbf{0 . 2 5 7 8}$ | 0.7071 |
| Final Vol. frac. | 0.263672 | $\mathbf{0 . 2 5 7 8}$ | 0.7071 |
| \|Displacement $\mid$ | $\mathbf{1 . 0 4 2 9 E - 3}$ | 0.09608119 | $9.43 \mathrm{E}-02$ |
| SF | 0.99849 | $\mathbf{0 . 9 0 4 5 6 8 2}$ | 0.8795682 |
| Avg(VM/YS) | 0.37022 | $\mathbf{0 . 2 8 9 0 6 8 8}$ | 0.09283329 |
| SD(VM/YS) | 0.044009 | 0.09028993 | 0.1165829 |
| Max VonMises | 2.196685 e 8 | 1.99005 e 8 | 1.93505 e 8 |

60 " presents the frequency of elements with material at such generation, which gives an idea of the probability of material existence at that point. The red regions in this figure show that smooth curved-shaped structures are sampled, and the green regions at center indicate that different
connections to reinforce the structure are randomly tested. Although it seems that some curved structures are tested, the final structure shows that EDATOP is capable of refining such intermediate solutions, reducing the volume and obtaining more efficient structures. The final-probability

Fig. 12 L-beam problems, loaded at top (LT) and center (LC)
![img-13.jpeg](img-13.jpeg)

Fig. 13 Results for LT
![img-14.jpeg](img-14.jpeg)
figure shows the convergence of the probability distribution; the red regions have a probability of 1 for being sampled and the blue regions have probability of 0 . Note that there are only a few elements with intermediate values in the contour where the last changes are explored. The von Mises stress
figure shows that the stresses are well distributed in the structure, having regions with high stress in different locations. Note that the most efficient structure must be red in the whole domain to indicate that all the structure is working at the maximum capacity of the material.

Fig. 14 Results for LC
![img-15.jpeg](img-15.jpeg)

EDATOP ability for finding efficient structures is also observed in Table 1, the volume delivered by EDATOP is less than half of that delivered by SIMPSC. Note that even when neither SIMPSC nor EDATOP are close to the constraint limit, SIMPSC delivers a smaller norm
displacement, which is expected because it uses more material. Possibly, the most interesting measurement is the average of the von Mises stress divided by the yield stress; the value of 0.5332546 obtained by EDATOP shows that on average the structure is working at more than $50 \%$ percent of

its capacity; notice that SIMPSC delivers structures which work around at $28 \%$ of their capacity; in addition, in the case of EDATOP the standard deviation of VM/YS is quite small, which means that most of the elements actually are working around that value.

Figures 6 and 7 show the results for the CLC and CLB cases. The results present similar characteristics than the CLT case; in both cases the final volume for EDATOP is less than half of that delivered by SIMPSC, and the average VM/YS is more than 0.5 for EDATOP. For all cantilever cases the problem was successfully solved. Note that the consideration of reducing the yield stress and maximum allowable displacement by a factor of 0.99 is sufficient to ensure feasible structures when considering actually void regions.

### 4.2 Short cantilever

The second set of case studies are short catilevers. The boundary conditions are defined as in Fig. 8 (see [37] for details). The loads magnitudes are $6.2 E 4 N, 8.6 E 4$ and $6.2 E 4$ for the top (SCLT), center (SCLC)) and bottom (SCLB) case respectively. Figures 9, 10 and 11 show visual results of this test and Table 2 presents quantitative results. In all cases, volumes found by EDATOP are smaller than those delivered by the SIMPSC. For the SCLT and SCLC, volumes of the EDATOP solutions are less than the half of those delivered by the SIMPSC. For the SCLB case both volumes are similar but EDATOP delivers a structure with a less average of VM/YS with a slightly smaller volume.

In this case, during the search, the active constraint, most of the time, is the displacement, while for SCLT and SCLC is the von Mises constraint. This is a remarkable case which demonstrates that the method is capable of finding structures with a desired rigidity, fulfilling both Von Mises and displacement constraints.

### 4.3 L-beam

The last two cases are: L-beam with a load at top of the right side (LLT), and L-beam with a load at the center of the right side (LLC), Fig. 12. They are also defined in [37]. The loads in both cases are of $1.5 E 4 N$. Visual results are in Figs. 13 and 14, and quantitative results are in Table 3.

In addition to outperforming SIMPSC in volume reduction, the L-beam problems show an important characteristic of the proposal: note from Figs. 13 and 14, that at the interior corner there is a stress concentration because of the abrupt change in geometry. In this case, our method explores topologies with smooth curved interior corners. This can be seen in the probability map at iteration 60 , as the curved shape diminishes the stress concentration. Notice that other methods such as SIMPSC, ESO and BESO [17], usually cannot deal with this kind of issues, since they do not remove material in highly stressed regions. The final shape presents a smooth geometry at this corner, consequently, the stress concentration is reduced.

Finally, for the sake of comparison with other metaheuristic that is not specially suited for topology optimization we present the graphical results of the GA in Fig. 15.

Table 3 L-beam results

| L-beam loaded at top |  |  |  |
| :-- | :-- | :-- | :-- |
| Data | SIMPSC | EDATOP | GA |
| Iterations |  | 480 | 490 |
| Final Vol. | 0.27246 | $\mathbf{0 . 1 0 8 0 8 9}$ | 0.5238221 |
| Final Vol. frac. | 0.425724 | $\mathbf{0 . 1 6 8 8 0 9}$ | 0.818472 |
| $\mid$ Displacement | $\mathbf{1 . 6 9 9 2 E - 3}$ | $5.264389 \mathrm{E}-3$ | $1.86 \mathrm{E}-03$ |
| SF | 0.99995 | 0.9892682 | 0.8243909 |
| Avg(VM/YS) | 0.23528 | $\mathbf{0 . 5 2 1 0 1 2 8}$ | 0.09660504 |
| SD(VM/YS) | 0.041240 | 0.2039309 | 0.09709171 |
| Max VonMises | 2.19989 e 8 | 2.17639 e 8 | 1.81366 e 8 |
| L-beam loaded at center |  |  |  |
| Iterations |  | 484 | 490 |
| Final Vol. | 0.291253 | $\mathbf{0 . 1 0 7 5 5 5 8}$ | 0.5066669 |
| Final Vol. frac. | 0.45508 | $\mathbf{0 . 1 6 8 0 5 6}$ | 0.791667 |
| $\mid$ Displacement | $\mathbf{1 . 6 4 5 9 E - 3}$ | 0.005307147 | $1.98 \mathrm{E}-03$ |
| SF | 0.9980207 | $\mathbf{0 . 9 8 9 7 3 1 8}$ | 0.96465 |
| Avg(VM/YS) | 0.21641 | $\mathbf{0 . 5 0 3 5 4 8 5}$ | 0.09357818 |
| SD(VM/YS) | 0.042650 | 0.2069733 | 0.09823741 |
| Max VonMises | 2.19564 e 8 | 2.17741 e 8 | 2.12223 e 8 |

![img-16.jpeg](img-16.jpeg)

Fig. 15 Graphical results from the Genetic Algorithm which uses exactly the same representation than EDATOP but it is not adapted for topology optimization

## 5 Conclusions

In this paper we introduce a global search method for topology optimization, from the family of estimation of distribution algorithms, which we call EDATOP. It explores the search space by means of estimating and sampling from a probability distribution, in order to randomly generate candidate solutions. The proposed method is quite simple
to program, and in practice, it only requires one parameter: the population size, which can be easily set, by proposing an initial value and then increasing it until no improvement is noticed. We address the topology optimization problem as volume minimization subject to a stress constraint; our method is compared with a version of SIMP called SIMPSC [35, 37]. In all cases, EDATOP delivers a smaller volume. Thus, it is clear that the global search provides

better results than the local search method for the widely used case studies presented. In contrast with local search strategies, our method explores solutions that are not proposed by these methods; for instance, in the L-beam case, EDATOP removes material in a region with high stress concentration in order to make a smooth corner. EDATOP can deal with stress as well as displacement constraints as it is shown in the short cantilever cases. The stress constraint ensures that the elastic model used as well as the simulation are realistic. Thus, the importance of the research on global search methods is not only that they could get better objective function values, but also that they provide qualitatively different designs. In contrast with other global search methods, EDATOP deals with real-world problem settings, for instance, in the best of our knowledge, there is no other global search strategy capable of dealing with meshes of more than ten thousand elements, considering self weight, using real world material and loads, and delivering results which are competitive with methods such as SIMPSC. On the other hand, when EDATOP is compared with a GA, it performs better because the probabilistic learning is better suited for topology optimization than the crossover and mutation operators, EDATOP explores at the beginning, of the search and refines the solutions at the end of the search process, while the GA performs the very same operations through the optimization process.

One of the main advantages in EDATOP is the decoupling of the optimization problem and the evaluation strategy, which produces a much smaller number of optimization variables than the number of finite elements used to evaluate candidate solutions. This is achieved as a consequence of the main contributions of this work: 1) the use of a smooth function to define material existence which is defined by few nodal values on a coarse mesh, which makes tractable the optimization problem and generates candidate structures with smooth contours and avoids the checkerboard effect. 2) A global optimization method which proposes solutions usually unexplored by localsearch methods and is capable of both: exploring many different topologies and refining the best solution in order to improve its efficiency.

Finally, in our future work we are planning to introduce apriori information in the probability distribution, such as stresses or distortion energy (von Mises stress), in order to reduce the number of evaluations. In addition, the probability distribution can be seen as design expertise which has been discovered during the optimization process, and it could be of interest for engineers and decision makers.

## References

1. Allaire G, Dapogny C, Frey P (2014) Shape optimization with a level set based mesh evolution method. Comput Methods Appl Mech Eng 282:22-53. https://doi.org/10.1016/j.cma.2014.08.028
2. Allaire G, Jouve F (2005) A level-set method for vibration and multiple loads structural optimization. Comput Methods Appl Mech Eng 194:3269-3290. https://doi.org/10.1016/j.cma.2004. 12.018
3. Allaire G, Jouve F, Toader AM (2002) A level-set method for shape optimization. C R Math 334:1125-1130
4. Allaire G, Jouve F, Toader AM (2004) Structural optimization using sensitivity analysis and a level-set method. J Comput Phys 194:363-393. https://doi.org/10.1016/j.jcp.2003.09.032
5. Balamurugan R, Ramakrishnan C, Singh N (2008) Performance evaluation of a two stage adaptive genetic algorithm (tsaga) in structural topology optimization. Appl Soft Comput 8:1607-1624
6. Bendsøe M (1989) Optimal shape design as a material distribution problem. Struct Optim 1(4):193-202. https://doi.org/10.1007/ BF01650949
7. Bendsoe MP, Sigmund O (1999) Material interpolation schemes in topology optimization. Arch Appl Mech 69:635-654
8. Blank L, Farshbaf-Shaker MH, Garcke H, Rupprecht C, Styles V (2014) Multi-material phase field approach to structural topology optimization. In: Trends in PDE constrained optimization. Springer, pp 231-246
9. Bourdin B, Chambolle A (2003) Design-dependent loads in topology optimization. ESAIM: Control. Optim Calc Var 9:19-48
10. Bureerat S, Limtragool J (2006) Performance enhancement of evolutionary search for structural topology optimisation. Finite Elem Anal Des 42:547-566
11. Bureerat S, Limtragool J (2008) Structural topology optimisation using simulated annealing with multiresolution design variables. Finite Elem Anal Des 44:738-747. https://doi.org/10.1016/j.finel. 2008.04.002
12. Chen T, Chiou Y (2013) Structural topology optimization using genetic algorithms. In: Proceedings of the world congress on engineering, vol 3, pp 3-5
13. Deaton JD, Grandhi RV (2014) A survey of structural and multidisciplinary continuum topology optimization: post 2000. Struct Multidiscip Optim 49:1-38. https://doi.org/10.1007/s00158-0130956-z
14. Deb K, Tiwari S (2005) Omni-optimizer: a procedure for single and multi-objective optimization. In: Coello Coello CA, Hernández Aguirre A, Zitzler E (eds) Evolutionary multi-criterion optimization. Springer Berlin Heidelberg, Berlin, pp 47-61
15. Eschenauer HA, Kobelev VV, Schumacher A (1994) Bubble method for topology and shape optimization of structures. Struct Optim 8:42-51
16. Garcia-Lopez NP, Sanchez-Silva M, Medaglia AL, Chateauneuf A (2013) An improved robust topology optimization approach using multiobjective evolutionary algorithms. Comput Struct 125:1-10. https://doi.org/10.1016/j.compstruc.2013.04.025
17. Ghabraie K (2015) The eso method revisited. Struct Multidiscip Optim 51(6):1211-1222. https://doi.org/10.1007/s00158-014-1208-6
18. Goldberg DE, Holland JH (1988) Genetic algorithms and machine learning. Mach Learn 3(2):95-99
19. Guan-Chun L, Chun-Yi L, Yu-Shu L (2011) A binary particle swarm optimization for continuum structural topology optimization. Appl Soft Comput 11(2):2833-2844

20. Hansel W, Treptow A, Becker W, Freisleben B (2002) A heuristic and a genetic topology optimization algorithm for weight-minimal laminate structures. Compos Struct 58:287-294
21. Hansel W, Treptow A, Becker W, Freisleben B (2002) A heuristic and a genetic topology optimization algorithm for weight-minimal laminate structures. Compos Struct 58(2):287-294
22. Haslinger J et al (2003) Introduction to shape optimization: theory, approximation, and computation, vol 7. SIAM
23. Hassani B, Hinton E (1998) A review of homogenization and topology opimization II-analytical and numerical solution of homogenization equations. Comput Struct 69(6):719-738
24. Hassani B, Hinton E (1998) A review of homogenization and topology optimization I-homogenization theory for media with periodic structure. Comput Struct 69(6):707-717
25. Huang X, Xie Y (2010) Evolutionary topology optimization of continuum structures: methods and applications. Wiley, Hoboken
26. Jeong SH, Choi DH, Yoon GH (2014) Separable stress interpolation scheme for stress-based topology optimization with multiple homogenous materials. Finite Elem Anal Des 82:16-31. https://doi.org/10.1016/j.finel.2013.12.003
27. Jeong SH, Park SH, Choi DH, Yoon GH (2013) Toward a stressbased topology optimization procedure with indirect calculation of internal finite element information. Comput Math Appl 66(6):1065-1081
28. Kaveh A, Hassani B, Shojaee S, Tavakkoli S (2008) Structural topology optimization using ant colony methodology. Eng Struct 30(9):2559-2565
29. Kutuk MA, Gov I (2013) A finite element removal method for 3d topology optimization. Advances in Mechanical Engineering 2013(413463). https://doi.org/10.1155/2013/413463
30. Luh GC, Lin CY (2009) Structural topology optimization using ant colony optimization algorithm. Appl Soft Comput 9(4):13431353
31. Noëlublao N, Bureerat S (2013) Simultaneous topology, shape, and sizing optimisation of plane trusses with adaptive ground finite elements using MOEAs. Math Probl Eng 2013(2013):10. https://doi.org/10.1155/2013/838102
32. Osher S, Fedkiw R (2006) Level set methods and dynamic implicit surfaces, vol 153. Springer Science \& Business Media
33. Radman A (2013) Bi-directional evolutionary structural optimization (beso) for topology optimization of material's microstructure. Ph.D. thesis, RMIT University
34. Shin H, Todoroki A, Hirano Y (2013) Elite-initial population for efficient topology optimization using multi-objective genetic algorithms. Int J Aeronaut Space Sci 14(4):324-333
35. Sigmund O (2001) A 99 line topology optimization code written in matlab. Struct Multidiscip Optim 21:120-127
36. Tanskanen P (2002) The evolutionary structural optimization method: theoretical aspects. Comput Methods Appl Mech

Eng 191(47-48):5485-5498. https://doi.org/10.1016/S0045-7825 (02)00464-4
37. Valdez SI, Botello S, Ochoa MA, Marroquín JL, Cardoso V (2017) Topology optimization benchmarks in 2d: Results for minimum compliance and minimum volume in planar stress problems. Arch Comput Methods Eng 24(4):803-839. https://doi.org/10.1007/s11831-016-9190-3
38. Valdez SI, Hernández A, Botello S (2013) A boltzmann based estimation of distribution algorithm. Inform Sci 236:126-137. https://doi.org/10.1016/j.ins.2013.02.040
39. Valdez-Peña SI, Hernández-Aguirre A, Botello-Rionda S (2009) Approximating the search distribution to the selection distribution in edas. In: Proceedings of the 11th annual conference on genetic and evolutionary computation, GECCO '09. ACM, New York, pp 461-468. https://doi.org/10.1145/1569901.1569965
40. Wang S, Tai K (2004) Graph representation for structural topology optimization using genetic algorithms. Comput Struct 82(20):1609-1622
41. Wang SY, Wang MY (2006) An enhanced genetic algorithm for structural topology optimization. Int J Numer Methods Eng 65:18-44. https://doi.org/10.1002/nme. 1435
42. Wang Y, Kang Z, He Q (2014) Adaptive topology optimization with independent error control for separated displacement and density fields. Comput Struct 135:50-61. https://doi.org/10.1016/ j.compstruc.2014.01.008
43. Wang Y, Kang Z, He Q (2014) Adaptive topology optimization with independent error control for separated displacement and density fields. Comput Struct 135:50-61
44. Xie Y, Steven GP (1993) A simple evolutionary procedure for structural optimization. Comput Struct 49(5):885-896
45. Xu H, Guan L, Chen X, Wang L (2013) Guide-weight method for topology optimization of continuum structures including body forces. Finite Elem Anal Des 75:38-49
46. Yamada T, Izui K, Nishiwaki S, Takezawa A (2010) A topology optimization method based on the level set method incorporating a fictitious interface energy. Comput Methods Appl Mech Eng 199:2876-2891. https://doi.org/10.1016/j.cma.2010.05.013
47. Yamasaki S, Kawamoto A, Nomura T, Fujita K (2015) A consistent grayscale-free topology optimization method using the levelset method and zero-level boundary tracking mesh. Int J Numer Methods Eng 101:744-773. https://doi.org/10.1002/nme. 4826
48. Zhao J, Wang C (2014) Robust topology optimization under loading uncertainty based on linear elastic theory and orthogonal diagonalization of symmetric matrices. Comput Methods Appl Mech Eng 272:204-218. https://doi.org/10.1016/j.cma.2014.01.018
49. Zhu B, Zhang X, Fatikow S (2015) Structural topology and shape optimization using a level set method with distance-suppression scheme. Comput Methods Appl Mech Eng 283:1214-1239. https://doi.org/10.1016/j.cma.2014.08.017