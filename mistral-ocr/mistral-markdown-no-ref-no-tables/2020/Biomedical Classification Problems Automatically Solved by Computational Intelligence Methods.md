# Biomedical Classification Problems Automatically Solved by Computational Intelligence Methods 

Luis Carlos Padierna ${ }^{1 \text { D }}$, Carlos Villaseñor-Mora ${ }^{1}$, Silvia Alejandra Lopez Juarez ${ }^{1}$<br>${ }^{1}$ Universidad de Guanajuato - División de Ciencias e Ingenierías, Campus León, Loma del Bosque 103, Lomas del Campestre, 37150 León, México<br>Corresponding author: Luis Carlos Padierna (e-mail: lc.padierna@ugto.mx).

This work was supported by the Universidad de Guanajuato, Campus León with the research project CIIC-232/2019; the Secretaría de Innovación, Ciencia y Educación Superior (SIECES) del Estado de Guanajuato with the project IJ-19-36 and the Consejo Nacional de Ciencia y Tecnología (CONACYT) with the project CB-2016-288605.


#### Abstract

Biomedical classification problems are of great interest to both medical practitioners and computer scientists. Due to the harmful consequences of a wrong decision in this ambit, computational methods must be carefully designed to provide a reliable tool for helping physicians to obtain accurate predictions on unseen cases. Computational Intelligence (CI) provides robust models to perform optimization, classification and regression tasks. These models have been previously designed, mainly based on the expertise of computer scientists, to solve a vast number of biomedical problems. As the number of both CI algorithms and biomedical problems continues to grow, selecting the right method to solve a given problem becomes more challenging. To deal with this complexity, a systematic methodology for selecting a suitable model for a given classification problem is required. In this work, we review the more promising classification and optimization algorithms and reformulate them into a synergic framework to automatically design and optimize pattern classifiers. Our proposal, including state-of-the-art evolutionary algorithms and support vector machines, is tested on a variety of biomedical problems. Experimental results on benchmark datasets allow us to conclude that the automatically designed classifiers reach higher or equal performance than those designed by computer specialists.


INDEX TERMS biomedical classification problems, estimation of distribution algorithm, evolutionary algorithms, genetic programming, orthogonal polynomial kernels, support vector machines

## I. INTRODUCTION

Biomedical engineering is a concept that bridges medicine and technology influencing fields of specialization such as: bioimaging, bioinstrumentation, biomolecular analysis, biomechanics and biomaterials [1]. Research conducted in these fields frequently faces classification problems, for instance when deciding: if a gene can be a candidate of risk to develop Autism [2], if a patient presents a Parkinson disease based on the information obtained by acoustic biomarkers [3], if a microscopic image of breast tumor tissue provides evidence that it is benign or malignant [4] or if thermal patterns can help on the diagnosis of diabetic foot [5].

Computational Intelligence has provided methods to solve biomedical classification problems for years. However, the task of selecting an appropriate set of algorithms for a given problem has been mainly delegated to an expert. Among classification methods, Support Vector Machines (SVMs) are one of the most successful approaches due to its generalization capability by conducting structural risk minimization, absence of local minima by solving a quadratic programming problem and representation based on few parameters [6] [7] [8].

The performance of SVMs is highly dependent on two of its components: kernel function and hyper-parameters [9]
[10]. Concerning the kernel functions, different scenarios have emerged through the years to ensure that the best kernel function is used for a classification task. These scenarios include kernel generation from primary operations [11] [12] [13], and multiple kernel combination from existing kernels [14] [15] [16] [17] [18] [19]. Out of these, the latter has proved to be more convenient, since it combines the flexibility of kernel generation with the effectiveness of pre-designed kernels. Regarding the hyper-parameter tuning, several optimization methods have been applied, from the simple Grid Search and Random Search [20], to the more sophisticated Evolutionary Strategies [21], Genetic Algorithms [22], Bioinspired Metaheuristics [23] [24] [25], and Estimation of Distribution Algorithms (EDAs) [26], among others. Recently, it has been shown that EDAs perform SVM hyperparameter tuning more efficiently than other methods when solving biomedical classification tasks [27].

Some studies have described strategies for simultaneous kernel selection (or kernel generation) and hyper-parameter optimization [12] [18]; however, it can be argued that they lack convergence efficiency, explore a limited search space, and are prone to overfitting. In this work, a novel method is formulated to solve the problems of previous studies by

combining the advantages of evolutionary programming with the guided exploration of the estimation of distribution algorithms. Our method, hereafter referred as Smart Evolution of Ensemble Kernel for Support Vector Machines (SEEKS), consists of a Genetic Programming (GP) mechanism [28] able to build new multiple kernels based on different kernel families (or to select the best single kernel) and an EDA [29] adapted to the GP mechanism and aimed to build probability models based on estimations of the hyper-parameter distributions. Thus, our method performs hyper-parameter tuning of kernels as these are being evolved without adding any significant overhead.

Through robust experimentation, it is shown that SEEKS automatically achieves simultaneous kernel design and hyperparameter tuning for SVM classifiers as successfully as previous methods designed by specialists, with higher computational efficiency.

The next section provides the background theory to understand the tasks of SVM-kernel design and hyperparameter tuning. In Sect. III, our SEEKS method is justified and described. Sect. IV presents the experimental methodology followed and the results obtained in terms of the performance of the generated SVMs. In Sect. V the effectiveness and efficiency of our proposal are analyzed. Conclusions and further directions are offered in Sect. VI.

## II. BACKGROUND

## A. KERNEL FUNCTIONS FOR SUPPORT VECTOR MACHINES

Given a set of $m$ training data points $\left\{\mathbf{x}_{i}, y_{i}\right\}_{i=1}^{m}$, where $\mathbf{x}_{i} \in$ $R^{d}$ is the $i$-th input vector and $y_{i} \in\{+1,-1\}$ its corresponding class label; an SVM classifier in dual form can be formulated, introducing the Lagrange multipliers $\boldsymbol{\alpha}$ and following the Karush-Kuhn-Tucker conditions, as [30]:

$$
\begin{aligned}
& \operatorname{Max} L(\boldsymbol{\alpha})=\sum_{i=1}^{m} \alpha_{i}-\frac{1}{2} \sum_{i=1}^{m} \sum_{j=1}^{m} y_{i} y_{j} \alpha_{i} \alpha_{j} K\left(\mathbf{x}_{i}, \mathbf{z}_{j}\right) \\
& \text { s.t. } 0 \leq \alpha_{i} \leq C, \forall i=1, \ldots, m \quad \sum_{i=1}^{m} \alpha_{i} y_{i}=0
\end{aligned}
$$

where $C$ is called a penalty factor, $\mathbf{x}_{i}, \mathbf{z}_{j} \in R^{d}$ are the $i$-th and $j$-th input vector, respectively; and the function $K(\mathbf{x}, \mathbf{z})$ defined on $R^{d} \times R^{d}$ is called a kernel if there exists a map $\phi$ from the space $R^{d}$ to the Hilbert space, $\phi: R^{d} \rightarrow H$ such that $K(\mathbf{x}, \mathbf{z})=(\phi(\mathbf{x}), \phi(\mathbf{z}))$ [10]. The kernel function can take different forms, like those in TABLE I. Hyper-parameters are those parameters of a kernel plus the parameters of a specific SVM formulation (e.g. the penalty factor $C$ ). Choosing among different kernels is equivalent to choosing among different SVM models [9]. A deterministic way to select the most appropriate kernel for a given classification problem is still unknown. Moreover, kernel selection is becoming more challenging because the number of valid kernels continues to grow as new kernel families are proposed. These families include: wavelet kernels [31], non-parametric kernels [32], and orthogonal polynomial kernels [33] [34] [35] [36]. Kernels in TABLE I have proved to be valid kernels since they satisfy the necessary and sufficient conditions established in

Mercer's theorem [37]. Briefly stated, this theorem affirms that the series $\sum_{i=1}^{m} \lambda_{i} \phi_{i}(\mathbf{x}) \phi_{i}(\mathbf{z})$, in terms of eigenfunctions $\phi_{i} \in L_{2}\left(X \subseteq R^{d}\right)$ and positive associated eigenvalues $\lambda_{i}$, converges absolutely and uniformly to $K(\mathbf{x}, \mathbf{z})$ when the latter is symmetric and positive semidefinite. To be positive semidefinite a kernel function must comply with $\iint K(\mathbf{x}, \mathbf{z}) g(\mathbf{x}) g(\mathbf{z}) d \mathbf{x} d \mathbf{z} \geq 0$.

TABLE I
CLASSIC, WAVELET, NON-PARAMETRIC, AND ORTHOGONAL POLYNOMIAL KERNELS


A current research trend consists of combining two or more kernels to increase the accuracy rate and generalization capability of SVMs. A combination of Mercer kernels is also valid under the closures in TABLE II (for a formal proof of these closures, cf. [38]). This approach has been followed in several relevant works [14] [18] [19] [32] [34] [35] [36], and has introduced the concept of a Multiple Kernel, denoted: $K_{\eta}(\mathbf{x}, \mathbf{z})=f_{\eta}\left(\left\{K_{i}\left(\mathbf{x}^{i}, \mathbf{z}^{i}\right)\right\}_{i=1}^{p} \mid \eta\right)$ where $\mathbf{x}^{i}, \mathbf{z}^{i} \in R^{d_{i}}$; the kernel functions, $\left\{K_{i}: R^{d_{i}} \times R^{d_{i}} \rightarrow R\right\}_{i=1}^{p}$ take $P$ feature representations (not necessarily different) of data instances; and the combination function $f_{\eta}: R^{p} \rightarrow R$ can be linear or nonlinear. The parameter $\eta$ indicates that a certain set of predefined kernels is used (i.e., the kernels and their parameters are known before training) [39].

TABLE II
CLOSURES ALLOWING THE VALID COMBINATION OF KERNELS

## B. METAHEURISTIC ALGORITHMS

Metaheuristics refer to a family of approximate optimization techniques that provide acceptable solutions in a reasonable time for solving complex problems [40]. There exist several types of metaheuristics; however, only Genetic Programming and Estimation of Distribution algorithms will be considered in the implementation of SEEKS, since these are the more promising methods found in the literature related to kernel evolution [12] [18] [19] and hyper-parameter tuning of SVMs [23] [21] [20] [24] [25], respectively. The selection of an EDA among other metaheuristics is based on two reasons: first, its iterative mechanism naturally adapts to the GP algorithm; and second, it was proved to be the optimal hyper-parameter tuner of SVM classifiers when solving biomedical problems [27].

EDAs explore a solution space by iteratively building and sampling explicit probabilistic models of candidate solutions that guide the search [29]. The procedure is shown in LISTING 1.

## LISTING 1. General Estimation of Distribution Algorithm

1 Generate an initial population of $N$ solutions: $S^{(0)}=$ $\left(\mathbf{s}_{i}\right)_{i=1}^{N}$ at iteration $t=0$, uniformly
2 while (stop criteria are not met)
3 Compute objective function of each solution $g\left(S^{(t)}\right)$
4 Select a subset of the best solutions, $S_{M}^{(t)}$ from $S^{(t)}$
5 Build a probabilistic model $\boldsymbol{P}^{(t)}$ based on $S_{M}^{(t)}$
6 Sample $\boldsymbol{P}^{(t)}$ to generate new solutions $S^{\prime(t)}$
7 Substitute / Incorporate $S^{\prime(t)}$ into $S^{(t)}$
8 Update $t=t+1$
9 end while
10 Output the best solution found, $\mathbf{s}^{*}$, as a result
By taking a specific probabilistic model, an EDA receives a certain name. Two of these particular cases of probabilistic models are considered in this work: the Univariate Marginal Distribution Algorithm (UMDA) [41], and the Boltzmann Univariate Marginal Distribution Algorithm (BUMDA) [42].
The UMDA builds a Gaussian model $\boldsymbol{P}$ from a set of solutions $S=\left\{\mathbf{s}_{i}\right\}_{i=1}^{M}$, with parameters given by:
$\mu_{\kappa}=\frac{1}{M} \sum_{i=1}^{M} s_{i, \kappa} \quad$ and $\quad \sigma_{\mathrm{k}}=\left(\frac{1}{M-1} \sum_{i=1}^{M}\left(s_{i, \kappa}-\mu_{\kappa}\right)^{2}\right)^{1 / 2}$
where $M$ is the number of solutions considered to compute these parameters and $s_{i, \kappa}$ represents the $\kappa$-th component of a solution $\mathbf{s}_{i}$, which is a $D$-dimensional vector in $\mathfrak{R}^{D}$.
The BUMDA modifies UMDA by employing a model based on the Boltzmann distribution and incorporating a truncation selection method to accelerate convergence, as well as to free the user from having to set the number of samples that are selected for parameter estimation. The parameters of the Gaussian distribution used by the BUMDA are:

$$
\mu_{\kappa}=\frac{1}{\beta} \sum_{i=1}^{M} s_{i, \kappa} g\left(\mathbf{s}_{i}\right) \quad \sigma_{\kappa}=\left(\frac{1}{\beta+1} \sum_{i=1}^{M}\left(s_{i, \kappa}-\mu_{\kappa}\right)^{2} g\left(\mathbf{s}_{i}\right)\right)^{\frac{1}{2}}
$$

where $M$ is adjusted by the automatic truncation method, $g\left(\mathbf{s}_{i}\right)$ is the objective function value of the $i$-th solution, and $\beta$ represents the sum of the objective function values over the $M$ selected solutions.
The GP algorithm arose as an extension of the conventional genetic algorithm, and it is useful for discovering computer programs using the expressiveness of symbolic representation. The search space for GP is the space of all possible expressions that can be recursively created by compositions of the available functions and variables for a given problem [28]. In the case of the kernel evolution problem, functions can be any operator in TABLE II, and variables can be any kernel as those in TABLE I. The major difference of GP, to other evolutionary algorithms, is that the solutions are stored in variable-sized structures, commonly in parse trees where the operations are internal nodes and the variables are leaves [43]. These tree-based structures are used to combine kernels in our proposal. The pseudocode of the GP method is shown in LISTING 2.


## III. SMART EVOLUTION OF KERNELS FOR SVMs

Previous works have constructed single and multiple kernels by using Evolutionary Algorithms [12] [13] [14] [18] [19]. The first attempt to evolve kernels appears to be [14], where genetic algorithms were employed to explore possible kernel combinations. Subsequent studies [12] [18] [19] utilized GP with tree data structures to encode multiple kernels. Those works using GP adopted two different approaches: the first one focuses on combining vector operators to discover new kernel functions; this strategy introduces several problems (from numerical errors to poor results), mainly because it is prone to generate invalid kernels. The second alternative approach combines predefined kernels under some of the closures in TABLE II. Although this latter strategy has shown to be more consistent and it is adopted as part of our proposed method, it presents three major limitations:
(i) The hyper-parameters of evolved kernels were assigned unsystematically, leaving the burden of this task to the guided search of the GP algorithm. This raises two problems: the search space is extended dramatically, and the GP method is

overloaded, since it should control the convergence of both hyper-parameters and kernel shape.
(ii) Evolved kernels obtained from the GP mechanism are prone to overfitting, since the search process is guided just by the accuracy index (without considering if datasets are unbalanced or the amount of data required to build the decision function).
(iii) The terminal set and consequently the basis of the GP search space was limited to combinations of classic kernels (Linear, Sigmoid, Polynomial, and RBF).

Our current proposal removes these limitations of previous works through the following improvements:
(i) The GP search space is reduced and the kernel shape convergence is increased, by delegating the hyper-parameter tuning task to a synergic EDA mechanism.
(ii) One advantage of SVMs, over other classifiers, is the property to estimate its generalization capability as a function of the Proportion of Support Vectors (PSV) that defines the SVM hyperplane, here $\mathrm{PSV}=S V / N$, where $S V$ is the number of essential support vectors and $N$ is the number of instances in the training dataset [9]. In our SEEKS method, the overfitting problem is considered by integrating the PSV as a complementary quality measure of evolved kernels.
(iii) Kernels recently developed have shown advantages when combined with classical kernels. In references [34], [35] and [44] the mixtures of classical, wavelet, and orthogonal polynomial kernels were shown to reach a better performance than classic kernels. As a natural next step, SEEKS enhances this expertise-based way of combining kernels by adapting a systematic tool for automatically exploring combinations of kernels from different families. To date, no single work has been found that reports the hyper-parameter tuning or the evolution of kernels based on different kernel families. Thus, another contribution is the potentially first analysis of these kernels in an evolutionary methodology.

## A. THE SEEKS ALGORITHM

SEEKS is formulated to take advantage of the GP and EDA mechanisms so that, on each iteration, kernel evolution and hyper-parameter tuning are performed simultaneous and independently. The algorithm is overviewed in LISTING 3, its time complexity is presented in APPENDIX A, and the sequence of steps is detailed below.

1. In the first step, $N$ kernel combinations are codified as binary trees, randomly populated from the lists of kernels and operators described in TABLE I and TABLE II, respectively. Hyper-parameters vectors are all of cardinality $\kappa=6$, since $\mathbf{h}=(C, \gamma, a, b, n, \alpha)^{T}$. R proRe $t$ illustrates two possible initial kernel trees with corresponding hyper-parameter vectors.
2. In step two, each pair of kernel tree $\mathbf{k}$ and hyper-parameter vector $\mathbf{h}$ is evaluated as an SVM classifier on the same $k$-fold cross-validation for a given dataset. The objective function $g(\mathbf{k}, \mathbf{h})$ is the $k$-fold classification average performance. Then, the kernel population is sorted by this average.
3. Common stop criteria include: The max number of iterations reached, the tolerance between the best solution and possible objective function value was achieved, it has
achieved a small deviation on the population performance, etc. If criteria are not satisfied, then, at iteration $t$ perform steps 4 to 7 .

LISTING 3. Pseudocode of the SEEKS Algorithm
Initialize a population of kernel trees $K^{(0)}=\left\{\mathbf{k}_{i}\right\}_{i=1}^{N}$ and a set 1 of hyper-parameter vectors $H^{(0)}=\left\{\mathbf{h}_{i}\right\}_{i=1}^{N}$ following a uniform distribution. Set iteration $t=0$
2 Compute objective function $g\left(K^{(0)}, H^{(0)}\right)$ for each kernel with its corresponding parameters on the same validation data.
3 while (stop criteria are not met)
Select the best $M$ parameter vectors to update a probability
4 model $\boldsymbol{P}^{(t)}$ by using (11) or (12). Also select kernel trees for reproduction $K_{r}^{(t)} \subset K^{(t)}$ with a crossover method.
5 Apply variation operators to $K_{r}^{(t)}$ and keep the offspring $K_{o}^{(t)}$ Sample new hyper-parameter vectors from $\boldsymbol{P}^{(t)}$ and compute $g\left(K_{o}^{(t)}, H^{(t)}\right)$ for each new kernel tree.
7 Integrate candidates $K_{o}^{(t)}$ to a new population according to replacement operators and update $t=t+1$
8 end while
9 Output the best solution found, $\left(\mathbf{k}^{*}, \mathbf{h}^{*}\right)$, as a result.
4. The indexes of the best $M$ kernel trees are used to update $\boldsymbol{P}^{(t)}$ for all continuous parameters. In the case of the discrete parameter $n$, a multinomial model is estimated based on the distribution of the $M$ best degrees. After this, kernel trees are again selected from the population $K^{(t)}$ by a method such as tournament, reward-based or binary selection, etc.
5. Crossover and one-point mutation are used as variation operators. To avoid uncontrolled growth a bloat-control method, such as Tarpeian or others [45] is recommended.
6. Sample the value of the required hyper-parameters for the new individuals from the current probability model $\boldsymbol{P}^{(t)}$ and train the SVMs corresponding to the new individuals. Again, following the same $k$-fold cross-validation scheme using the partition obtained in step 2.
7. Update the population $K^{(t)}$ by replacing the worstperforming individuals with the top-performing new individuals from $K_{o}^{(t)}$. Increment the iteration counter and go to step 2 .
![img-0.jpeg](img-0.jpeg)

FIGURE 1. Kernel tree decoding. a) Kernel selection is possible when the root node is a kernel, irrelevant hyper-parameters are ignored. b) Kernel construction combining four basic kernels, hyper-parameters are shared.

# IV. EXPERIMENTAL DESIGN 

## A. BIOMEDICAL PROBLEMS

Fifteen benchmark biomedical classification problems were selected from related works to test the SEEKS method. Datasets (and short labels) corresponding to these problems are: breast cancer prediction (breast), chronic kidney disease prediction (chronic), vertebral column orthopedic normality (column_2C), wart treatment results by using cryotherapy (cryotherapy), type 2 diabetes diagnosis (diabetes), identification of altered sperm concentration (fertility), survival prediction after surgery of breast cancer (haberman), determination of heart disease (heart), wart treatment results by using immunotherapy (immuno), liver disorders caused by alcohol (liver), discrimination of benign and malignant mammographic masses (mammo), Parkinson prediction based on voice measurements (parkinsons), post-operative life expectancy in lung cancer patients after thoracic surgery (thoracic), prediction on the donation of blood (transfusion) and prognostic on breast cancer (wphc).
All datasets are publicly available at the UCI Machine Learning Repository [46]. Their characteristics and results of previous studies are summarized in TABLE III. The bestreported rates, in classification accuracy by using the RBF kernel or Multiple kernels, are also included as a basereference for comparison. All datasets were scaled to the range $[-1,1]$ to prevent the influence of attributes with dominating values and to preserve the conditions required by orthogonal kernels. For the sake of reproducibility, our pre-processed data can be found in the datasets folder of the public repository in [47] or [48].

TABLE III
SUMMARY OF BIOMEDICAL CLASSIFICATION PROBLEMS

${ }^{1}$ Fts is the number of attributes (features) that model a case.
${ }^{2}$ Variations on accuracy are due to either the SVM solver algorithm applied or the validation scheme followed on each study (dataset pre-processing and partition, hyper-parameter tuning strategy, etc.)

## B. KERNEL EVOLUTION SETTINGS

For training SVMs with kernel trees, the LIBSVM [56] solver was selected to achieve a direct comparison against previous works. Training a standard SVM has an algorithmic complexity between $O\left(N^{2}\right)$ and $O\left(N^{3}\right)$, with $N$ the number of input vectors [57]. Furthermore, the associated Gram matrix of size $N \times N$ must be allocated. Thus, the computational cost of evolving SVMs is high for each evaluation of the fitness function (classification accuracy obtained by 5 -fold crossvalidation). Taking into account this cost and the fact that only small improvements of candidate solutions have been observed after the 15th generation [18], in our experiments the number of generations was set to 15 as a stop criterion.

The performance index that guides the search of SEEKS is the rate in classification accuracy. However, high classification rates may hide overfitting to the training data. One way to observe this case is through an estimation of the generalization capability of an SVM, such as the PSV. Therefore, producing a good solution with the minimum PSV is a desirable goal when evolving kernels.

For the sake of a direct comparison against previous works: the PSV is not used to guide the evolution of SVMs, but it is adopted as a complementary performance measure; parameters including tree depth, mutation, and crossover rates, as well as methods for initialization, selection, variation, and replacement were set to the values used in [18]. The function set was defined so that results could be directly compared with those reported in [34] and [35]. The terminal set includes the identifiers of kernels presented in TABLE I. This configuration is provided in TABLE IV.

TABLE IV
CONFIGURATION OF SEEKS FOR KERNEL EVOLUTION

[^0]
[^0]:    ${ }^{1}$ As GE does not use a tree structure, a max depth tree is not required. Instead, the max size of expression is indicated.
    ${ }^{2}$ Instead of generations, Koch et al used 2500 kernel tree evaluations.
    ${ }^{3}$ Values marked with "---" were not reported by the authors of that experiment.

## C. PARAMETER SETTING AND EXPERIMENTAL GOALS

The standard C-SVM considers few hyper-parameters, namely: the penalty factor $C$, and the kernel parameters, such as the decaying parameter $\gamma$, the degree $n$, and the dilation factor $a$ for the RBF, orthogonal and Wavelet kernels, respectively. The work of Sun et al. [51] is the only one that we have identified that addresses the hyper-parameter tuning of orthogonal kernels (through Grid Search). No studies have been found about the influence of the Wavelet kernel parameters, so the values of the dilation parameter $a$ are taken from the original work [31]. The non-parametric and Linear kernels do not possess parameters. From the analysis of these works, the hyper-parameter setting used to perform tuning is summarized in TABLE V.

Two experiments were performed with the settings described in TABLES III-V. The objective of the first experiment is to analyze the effect (in terms of effectiveness and efficiency) of reformulating an EDA to synchronize with the GP mechanism, which is the main idea of the SEEKS algorithm. Both EDAs detailed in Sect. II, UMDA and BUMDA, were implemented so that three different kernel evolutionary algorithms were compared. These algorithms are referred to as GP, GP-U, and GP-B as short names for the standard Genetic Programming with totally random hyperparameter setting, GP coupled with UMDA and GP coupled with BUMDA, respectively.
The second experiment is aimed to observe if there exist improvements in classification performance when varying the terminal set of kernels being evolved. Three different terminal sets were employed: the set of classic kernels (clas $=$ $\{L, R, P\}$ ), the set of modern kernels (mod $=$ $\left\{K_{-} 11, K_{-} 13, H, E, W, G\right\}$ ), and the set of all kernels (all $=$ $\left\{L, R, P, K_{-} 11, K_{-} 13, H, E, W, G\right\})$.

Both experiments were carried out on the same framework, following the methodology described in LISTING 4. Also, they were performed on an Intel ${ }^{\circledR}$ Core $^{\text {TM }}$ i9-9980XE CPU (18 cores) running at 3.0 GHz and with 16 GB of RAM. The algorithms were implemented in the Java programming language using multithreading, where each thread execute an independent call of the SEEKS algorithm. Experimental results were analyzed with the Python programming language and are reported in the following section. Java and Python codes will be updated in the codes folder in [47].

## LISTING 4. Experimental Methodology

INPUT: User-defined parameters for kernel evolution, hyperparameter ranges, number of trials, performance metrics, etc.
OUTPUT: Performance Indexes (PI: Accuracy, PSV, G-mean, etc)
![img-1.jpeg](img-1.jpeg)

## V. EXPERIMENTAL RESULTS AND DISCUSSION

## A. EFFECTIVENESS AND EFFICIENCY OF THE SEEKS

The results of all the algorithms evaluated are summarized in TABLE VI. Concerning the first experiment, on TABLE VI it is possible to observe that, in almost all cases, both versions of the SEEKS algorithm (GP-U and GP-B) reached higher accuracies than the GP with a random hyper-parameter search. This is an important finding, because it means that the effect of an EDA coupled to the GP mechanism improves the performance on the classification rate of evolved SVMs.
To draw stronger conclusions regarding this finding, three statistical tests were applied: Friedman, Aligned Friedman, and Quade. These tests differ in the way of ranking each algorithm. In Friedman test, differences between the accuracy index values are equally weighted without considering their magnitude; in Aligned Friedman test, the biomedical problems are equally weighted independently of their difficulty, thus evaluating a general behavior of all datasets as a group; and in Quade test, rankings are weighted based on the difficulty of each dataset [58]. The three tests are helpful to determine if there exist differences in at least one of the algorithms under comparison. Once a difference is found, post hoc tests (such as Bonferroni-Dunn, Holm, Holland, Rom or Finner) are used to conclude which algorithms are statistically different from a pre-selected control method [59]. A significance level of 0.05 was used for all statistical tests. The average ranks and $p$-values of these tests are reported in TABLES VII-IX.

TABLE VI
AVERAGE ACCURACIES AND STANDARD DEVIATIONS OF NINE PAIRS (ALGORITHM, TERMINAL SET). STATISTICS WERE COMPUTED FROM AROUND 2500 KERNELS FOR EACH PAIR (100 KERNELS EVOLVED DURING THE LAST FIVE GENERATIONS OF FIVE INDEPENDENT RUNS).

TABLE VII
AVERAGE RANKS AND P-VALUES OF STATISTICAL TESTS ON THE NINE ALGORITHMS FOR KERNEL EVOLUTION

Results in TABLE VII indicate that the nine algorithms are not statistically equivalent under the Friedman and Quade tests. In both cases, the SEEKS version GP-B_mod is suggested as the control method for post hoc tests. In TABLE VIII and TABLE IX the hypothesis of equal performance to the control method is rejected with a $p$-value smaller or equal to that reported in the last row. Rejections are highlighted in boldface. From TABLE VIII it can be concluded that GP-B_mod is statistically better in finding higher accuracies than the other methods, except for GP-U_all, GP-B_all, and GP-U_mod. Thus, indicating that the introduction of both the new set of kernel functions and the EDA mechanism helps to improve the performance of the previous GP-clas scheme.

TABLE VIII
POST HOC TEST FOR THE CONTROL METHOD (GP-B_mod) SUGGESTED BY THE FRIEDMAN TEST. ALGORITHMS ARE SORTED p-VALUE

TABLE IX
POST HOC TEST FOR THE CONTROL METHOD (GP-B_mod) SUGGESTED BY THE QUADE TEST. ALGORITHMS ARE SORTED p-VALUE

![img-2.jpeg](img-2.jpeg)

FIGURE 2. Comparison among methods for kernel evolution. Groups of methods that are not significantly different are connected. CD is the critical difference that determines the cutoff range of each group.

From TABLE IX it can be observed that the GP-B_mod method is not statistically better to the rest of algorithms, with exception to the state-of-the-art GP-clas. Since Quade test weights rank based on the difficulty of each dataset, its results indicate that the GP-B_mod is the only SEEKS version that can reach a statistically better performance than GP-clas for kernel evolution when solving biomedical classification problems.
The critical difference diagram, described in FIGURE 2, is based on the Friedman and post hoc Nemenyi tests [60], it helps to visualize and further understand the conclusions provided by the Friedman and Quade tests, since it presents how the kernel evolution methods are grouped.
![img-3.jpeg](img-3.jpeg)

FIGURE 3. Density estimations based on the distribution of all SVMs with kernel trees evaluated during the last 5 generations (around 2500 SVMs minus duplicates for each dataset). The terminal set of all kernels was used. Densities illustrate convergence to the best performance on accuracy (x-axis). Higher peaks to the right indicate better kernels were found.

The information presented in TABLES VI-IX is useful to determine improvements in performance; however, it is not enough to verify if there exists any gain in efficiency, and it is insufficient to understand why the three evolutionary methods (GP, GP-U, and GP-B) differ. To understand how the efficiency of the kernel evolution process was performed, a density estimation [61], based on the distribution of all kernel trees (without duplicates) evaluated during the last five generations of the SEEKS algorithm and the baseline GP, is presented for each dataset in FIGURE 3. For the three algorithms shown in this figure, the terminal set with all kernels was used. Due to space restrictions, Figures showing densities corresponding to classic and modern sets of kernels are not presented but are available in the figures folders in [47] [48].

As can be observed from FIGURE 3, most densities for the GP algorithm (red curves) present a large area to the left side, thus indicating that most of the evaluated kernels reached lower performance than those generated by GP-U (blue curves) or GP-B (green curves). An interesting case is the mammographic dataset, which obtained similar average accuracy on the nine algorithms reported in TABLE VI. For the mammographic dataset, it could be hard to determine which algorithm is preferable, but after revealing the notable skewness of the GP method, it is possible to justify that the SEEKS algorithm is a preferable option because it found a larger amount of kernels with higher accuracy rate. FIGURE 3 also helps to estimate how hard is to solve a given dataset. For instance, datasets like breast, chronic or cryotherapy are easily solvable, whereas diabetes, haberman or liver do not. Also, it is worth noting that although the three methods can find the kernel with higher accuracy, the GP reaches it due to randomness more than by a proper convergence.

## B. EVALUATING DIFFERENT TERMINAL SETS

Regarding the second experiment, TABLE VI shows that, independently of the evolutionary mechanism employed, algorithms taking the modern or full set of kernels reach higher performance than those using the classic set. To ease the comparison of terminal sets, FIGURE 4 illustrates the max, average, and min performance over each dataset. In this figure it can be observed for which datasets, the terminal set of modern (blue dots) or all (green dots) kernels obtained better or equal performance than the classic (solid red line) set of kernels. Statistical tests of Friedman, Aligned Friedman, and Quade were applied to the results presented in TABLE VI. The results of these tests, summarized in TABLE X, indicate that there are differences among the three terminal sets for each one of the evolutionary algorithms. GP_all, GP-U_all, and GP-B_mod were suggested as control methods by the tests of Friedman, Aligned Friedman, and Quade, respectively. To determine which algorithms present statistical differences, the Bonferroni-Dunn post hoc test was applied to the control methods and their results are summarized in TABLE XI

TABLE X
RANKS AND $p$-VALUES OF STATISTICAL TESTS APPLIED TO THE ALGORITHMS FOR KERNEL EVOLUTION


![img-4.jpeg](img-4.jpeg)

FIGURE 4. Performance of all algorithms sorted by average accuracy and grouped by terminal set. The red solid line represents the GP with random hyper-parameter search. Shadowed areas are limited with the max and min values. The same data that in Fig. 2 and Table VI were used

TABLE XI
BONFERRONI-DUNN POST HOC TESTS TO DETERMINE WHICH TERMINAL SETS OF KERNELS ARE STATISTICALLY DIFFERENT.

${ }^{*}$ No difference was found; therefore, post hoc test was not applied. The GP_all, GP-U_all, and GP-B_mod were taken as the control methods

The conclusion from post hoc tests is that, with statistical significance, GP_all is better than GP_clas, but not than GP_mod; GP-U_all is better than GP-U_clas, but not than GP$\mathrm{U} \_$mod, and GP-B_mod is better than GP-B_clas, but not than GP-B_all. Therefore, the introduction of the modern set of kernels (either as an independent terminal set or as in combination with the classic kernels) improves the performance of the evolutionary algorithms that use only the classic set of kernels functions.

## C. SELECTING THE BEST EVOLVED KERNEL

For each of the 15 biomedical problems considered in this work, different evolved kernels were found to reach the highest performance in terms of accuracy. This is an important finding because it means that there are several single kernels or kernel combinations that can effectively solve a given dataset. At the same time, it raises the problem of determining which kernel should be selected since, due to the nondeterministic nature of the evolutionary algorithms, the final form of the best kernel found can be different from one run of the algorithm to another. Furthermore, as evolutionary algorithms are targeted to find the best possible accuracy without considering other aspects such as the PSV, the kernel complexity, the training time, the balance of the dataset, etc.; it is necessary to verify that the selected kernel is not overfitted. TABLE XII illustrates both cases, the existence of different kernels with equal performance and kernels that tend to overfit (highlighted in boldface). For the sake of brevity, only the information of the first three independent runs is provided, the rest of evolved kernels and all experimental results given in section V are available in the results folder of [47] or [48]. From TABLE XII it may be noted that overfitted kernels were found for the fertility and wpbc datasets, and in contrast, for the chronic dataset desirable kernels were obtained.

To alleviate the overfitting problem and being able to select the most convenient kernel for each dataset, we propose to consider the PSV as a complementary quality index,
because it measures the amount of data required to build the decision function of SVMs. A PSV value equals to 1 indicates that all training data points were used, so the model is overfitted. Thus, kernels with similar accuracy and lower PSV should be preferred since they are expected to have better generalization on unseen cases. In order to conduct a systematic evaluation of SVMs by measuring the accuracy and PSV at the same time, the following combined index, previously reported in [27], is used. The results of applying this selection strategy are provided in TABLE XIII

$$
\operatorname{cmbld} x=\exp \left(\frac{-0.1\left(100 \times P S V+(100-A c c)^{2}\right)}{200-100 \times P S V-A c c+.001}\right)
$$

TABLE XII
BEST KERNELS FOUND ON DIFFERENT RUNS OF THE EVOLUTIONARY METHODS REPORTED IN TABLE VI (HIGHLIGHTED IN GRAY). KERNEL EXPRESSIONS ARE FACTORED WHEN POSSIBLE

TABLE XIII
EVOLVED KERNEL SELECTION BY THE HIGHEST COMBINED INDEX OF ACCURACY AND PSV


Other aspects of the evolved kernels such as the kernel complexity, the training time or the bias to an unbalanced class, can be evaluated based on the user's requirements. For instance, a third criterion can be suggested by following the Occam's razor principle, so that evolved kernels with similar accuracy and PSV, but with smaller tree-depth are selected since they are simpler to implement and cheaper to evaluate. The integration of these ideas into an evolutionary method like SEEKS will conduct to a multi-objective optimization scheme, which is beyond the scope of the present work. However, in order to provide a baseline for future comparisons of the SEEKS method, TABLE XIII presents the accuracy, PSV, cmbldx, and G-mean indexes [62] and also the training time and associated hyper-parameters for the evolved kernels with the highest cmbldx during the first three runs reported in TABLE XII. The same information that in TABLE XIII is available for all the evolved kernels and can be consulted in the results directory of [47] or [48]. The accuracy and PSV obtained by the base techniques of SEEKS and by other methods are also presented in TABLE XIII for reference.

## VI. CONCLUSIONS

The main conclusion of the present work is that the proposed SEEKS method was able to automatically design an effective SVM classifier for each of the considered biomedical classification problems. Effectiveness was evaluated by comparing the performance of SVMs designed by our method against the SVMs produced by the state-of-the-art GP_clas algorithm. Experimental results indicate that the GP-U_mod version of SEEKS was statistically better than GP_clas, under the Friedman and Quade tests, and that GP_clas was inefficient and sensible to randomness. Results from FIGURE 2 allow us to conclude that the introduction of both EDAs and new kernel functions to the previous evolutionary scheme is
beneficial. As per the results recorded in TABLES VI and X, The improvements in effectiveness were found to be caused by the introduction of new families of kernel functions.

Regarding efficiency, the SEEKS method found more kernels with the highest accuracy than GP for most datasets. As both methods used the same computational resources, initial population and terminal sets, the improvement in efficiency can only be explained by the introduction of the EDA mechanisms. From this result, it can be concluded that delegating the hyper-parameter tuning of evolved kernels to EDAs leads to an increase in the convergence of the GP evolutionary algorithms for SVMs.

In addition to the accuracy index, the quality of the best kernels found by the evolutionary algorithms was measure through the PSV, which resulted to be useful for detecting classifiers prone to overfitting. Also, the G-mean index, the kernel-tree depth, and other valuable information can be obtained from the evolutionary process. Thus, a major direction to future improvements of this work consists in reformulating the SVM kernel evolution as a multi-objective optimization problem, in order to reduce the PSV or the kernel complexity while maintaining the optimal accuracy or Gmean indexes.

It is important to mention that evolving kernels during 15 generations, with a maximum depth of 2 levels in the treebased chromosome, was enough to find multiple kernels with high performance. Further these thresholds, kernels presented numerical problems and the evolution was time-consuming. This increment in computational time as a function of the kernel-tree depth is a limitation that may be overcome with the introduction of more efficient and manageable evolutionary algorithms, such as grammatical evolution. Genetic operators and GP hyper-parameters values were fixed to those reported

in TABLE IV, a deeper analysis on this configuration is required to further improve the SEEKS evolutionary process. Another restriction is the maximum size of the datasets (around 2000 instances) that can be handled by SEEKS. In order to deal with larger datasets, an SVM solver different to the LIBSVM may be implemented, as long as it allows the introduction of kernel functions. Due to the stochastic nature of SEEKS, different runs of the algorithm can produce different kernel-trees; thus, a systematic strategy to identify which kernel-tree is the best for a given dataset is required.

Finally, since the SEEKS strategy is independent of the problem domain, applications to domains other than classification (such as regression or density estimation) can be easily conducted in future work.

## APPENDIX

## A. TIME COMPLEXITY OF SEEKS

The SEEKS algorithm integrates two metaheuristics into a single mechanism, namely EDAs (LISTING 1) and GP (LISTING 2). The time complexity of both EDAs, UMDA and BUMDA, was reported for the SVM hyper-parameter optimization problem to be $O\left(p N^{3}\right)$ [27]. Where $p$ and $N$ stand for the population size and the number of training samples, respectively. The evaluation of the fitness function (training an SVM with the LIBSVM solver) is the most expensive step that dominates the processing time with a complexity of $O\left(N^{3}\right)$ [57]. The GP time complexity has not been reported by previous studies on kernel evolution [12, 18, 19]; hence, an analysis of its mechanism is now provided.
The GP time complexity can be bounded only after some assumptions are made on the genetic operators of selection, crossover, and mutation; and also after hyper-parameters such as the population size $(p)$, maximum number of generations $(G)$, and max tree depth $\left(T_{\max }\right)$ are fixed. Changing these genetic operators and/or hyper-parameters directly impacts on the GP processing time, e.g., the time complexity of selection by tournament is $O(p)$, and by roulette wheel with binary search is $O(p \log p)$ [63]. If onepoint crossover and one-point mutation operators are used with $>$ constant probabilities $p_{c}>0$, and $p_{m}>0$, respectively; then, the overall complexity of the genetic reproduction step is $O(p n G)$, where $n<2^{T_{\max }+1}$ is the total number of nodes [64]. Regarding the GP hyper-parameters, the complexity of depth-first traversals of binary trees (such as the kernel tree used by SEEKS) is in $O(n)$; and the sorting algorithm required to rank the evolved SVMs is $O(p \log (p))$ [65]. Therefore, the bound of the GP time complexity is given by the sum of the following steps: evaluation of the initial population (A), ranking and selection (B), reproduction and mutation (C), population updating (D).
The SEEKS algorithm takes advantage of the similarities between the GP and EDA mechanisms, so that the more expensive steps (A and D) are used for updating the probability model of EDAs and the kernel-tree population of GP at the same time. The only computational cost that SEEKS adds to GP is on the computation required to obtain
the parameters of either the BUMDA or the UMDA probabilistic model, which is linear $O(d p)$ with $d$ the number of SVM hyper-parameters [42]. Let be $G, T_{\text {max }}$, and $p, p_{c}>0, p_{m}>0$ constant values and assume tournament selection, one-point crossover and one-point mutation are the genetic operators employed; the time complexities of SEEKS and its base techniques is bounded as reported in TABLE XIV.

TABLE XIV
TIME COMPLEXITY OF SEEKS AND ITS BASE TECHNIQUES


## B. SUPPLEMENTARY MATERIAL

All datasets, files with performance indexes, evolved kernel trees, complementary figures, and codes are available at: https://github.com/padiernacarlos/SEEKS. Or at IEEE Dataport: http://dx.doi.org/10.21227/32ab-9884. For copyright reasons, the source code will be available once this paper is published.

## ACKNOWLEDGMENT

The authors want to acknowledge the support provided by the División de Ciencias e Ingenierías, Universidad de Guanajuato, Campus León during the research and preparation of the manuscript. Luis Carlos Padierna also wants to thank to Dr. Arturo González-Vega for his valuable comments about experimental results.
