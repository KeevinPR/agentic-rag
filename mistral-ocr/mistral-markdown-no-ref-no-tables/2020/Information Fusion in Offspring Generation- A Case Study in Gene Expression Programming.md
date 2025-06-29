# Information Fusion in Offspring Generation: A Case Study in Gene Expression Programming 

TONGLIN LIU ${ }^{1}$, HENGZHE ZHANG ${ }^{\otimes 2}$, HU ZHANG ${ }^{\otimes 1}$,<br>AND AIMIN ZHOU ${ }^{\otimes 2}$, (Senior Member, IEEE)<br>${ }^{1}$ Science and Technology on Complex System Control and Intelligent Agent Cooperation Laboratory, Beijing Electro-Mechanical Engineering Institute, Beijing 100074, China<br>${ }^{2}$ Shanghai Key Laboratory of Multidimensional Information Processing, School of Computer Science and Technology, East China Normal University, Shanghai 200062, China<br>Corresponding author: Hu Zhang (jxzhanghu@126.com)


#### Abstract

This work was supported in part by the National Natural Science Foundation of China under Grant 61703382, Grant 51875053, and Grant 61673180, in part by the China Ministry of Science and Technology Key Research and Development Program under Grant 2018YFC1903101, in part by the Science Foundation of Science and Technology on Complex System Control and Intelligent Agent Cooperative Laboratory under Grant 181601, and in part by the Science and Technology Commission of Shanghai Municipality under Grant 19511120600.


#### Abstract

Gene expression programming (GEP), which is a variant of genetic programming (GP) with a fixed-length linear model, has been applied in many domains. Typically, GEP uses genetic operators to generate offspring. In recent years, the estimation of distribution algorithm (EDA) has also been proven to be efficient for offspring generation. Genetic operators such as crossover and mutation generate offspring from an implicit model by using the individual information. By contrast, EDA operators generate offspring from an explicit model by using the population distribution information. Since both the individual and population distribution information are useful in offspring generation, it is natural to hybrid EDA and genetic operators to improve the search efficiency. To this end, we propose a hybrid offspring generation strategy for GEP by using a univariate categorical distribution based EDA operator and its original genetic operators. To evaluate the performance of the new hybrid algorithm, we apply the algorithm to ten regression tasks using various parameters and strategies. The experimental results demonstrate that the new algorithm is a promising approach for solving regression problems efficiently. The GEP with hybrid operators outperforms the original GEP that uses genetic operators on eight out of ten benchmark datasets.


#### Abstract

INDEX TERMS Genetic programming, gene expression programming, estimation of distribution algorithm, offspring generation.


## I. INTRODUCTION

Gene expression programming (GEP) [1] is an evolutionbased algorithm for solving symbolic regression problems. Comparing with traditional machine learning algorithms, such as the neural network, GEP evolves interpretable symbolic expressions without calculating gradients. Although lack of pervasive theoretical performance studies, the distinct features of GEP also draw extensive attention from multiple disciplines to build an explainable model, such as in energy management [2], economic modeling [3], and power distribution [4] domains. GEP is similar to the tree-based genetic programming algorithm (GP) [5], which both generate a symbolic expression under the framework of evolutionary algo-

The associate editor coordinating the review of this manuscript and approving it for publication was Li Zhang ${ }^{\circledR}$.
rithms (EAs). However, in contrast with GP, GEP has a fixedlength gene sequence and an unconstrained search space through a genotype-phenotype mapping mechanism [6]. This advantage enables GEP to produce more satisfactory results in diverse domains. For example, in the water resources management domain, substantial improvement has founded by replacing GP with GEP [7]. In other domains, such as in rock mechanics [8] and data mining [9] domains, similar results have also been obtained.

GEP uses a linear representation to represent a variety of programs. The linear gene in GEP is composed of a head and a tail. The head contains function primitives and terminal primitives, and the tail only contains terminal primitives. Fig. 1 presents an example of the GEP expression.

In GEP, computer program functions are usually considered as function primitives, which can accept several

![img-0.jpeg](img-0.jpeg)

FIGURE 1. An example of a gene expression in GEP.
![img-1.jpeg](img-1.jpeg)

FIGURE 2. A valid expression tree converted by a gene expression.
parameters and return a result after operation. Variables and constants are regarded as terminal primitives. Hence, all function primitives are located at non-leaf nodes in the gene expression tree, and all terminal primitives are located at leaf nodes in the gene expression tree.

In GEP, two parameters, the head length and the tail length, are used to determine the size of a gene expression. The head length can be set to any natural number $h \in \mathbb{N}$. However, the tail length $t$ can not be set freely because it is calculated from the head length as (1):

$$
t=h *(a-1)+1
$$

where $t$ represents the tail length, $h$ represents the head length, and $a$ represents the maximum arity of the function primitives. In Fig. 1, the maximum arity functions are binary operators " + " and " - ". Hence, under this circumstance, the maximum arity is 2 .

By this mechanism, each symbolic expression tree can be converted to a linear gene expression, and each linear gene expression can be converted to a valid symbolic expression tree. For example, the gene expression in Fig. 1 can be converted to an expression tree as illustrated in Fig.2.

One of the main contributions of GEP is its representation, which uses a fixed-length gene expression to represent a variety of symbolic expressions. This representation directly leads to an advantage in the offspring generation. As representation with a fixed-length gene expression, many offspring generation operators can be applied. Basically, there are two kinds of operators that have widely used in GEP.

The first one is genetic operators, such as crossover and mutation operators. These kinds of operators choose one or two parent individuals, exchange the gene components between parent individuals or vary the gene components in a single parent individual. In traditional GEPs [10], various mutation operators and crossover operators are proposed for generating offspring. These operators increase the diversity of the population. A random numerical constant (RNC) array has also been proposed for improving the constant fitting efficiency. However, genetic operators are fixed during the
evolution process. In real practice, an adaptive operator to accommodate specific problems is more desired to achieve better performance than traditional genetic operators. EDA operator is suitable for this requirement [11].

Therefore, the second one is the EDA operator. This kind of operator builds a probabilistic model to extract the population distribution information from the population, and sample new offspring solutions from the probabilistic model. In the community of GP, EDA has been widely used. Probabilistic incremental program evolution (PIPE) [12] is the first algorithm that uses a probabilistic model to generate solutions. Subsequently, extended compact genetic programming (ECGP) [13] was proposed, which incorporates the strategy of extended compact genetic algorithm (ECGA) [14] into GP. The Bayesian network [15] has also been used to integrate with the traditional genetic algorithm in the GP algorithm. The experimental results proved that using the integrated approach outperforms using both algorithms separately [16]. However, it needs much effort to construct a Bayesian network, especially when the structure of the Bayesian network is needed to learn from data. Therefore, in the EDA domain, traditional statistical models are still widely used [17], [18]. Recently, scholars have tried to apply EDA to GEP to realize improved performance. Probabilistic developmental program evolution (PDPE) [19] has been proposed, which uses a probabilistic model to generate offspring. However, [19] only explores the effects of a probabilistic model based GEP offspring generation algorithm, and the effects of the hybrid algorithm based on the genetic algorithm (GA) and the estimation of distribution algorithm (EDA) has not been discussed. Although the EDA operator reveals many impressive results, some drawbacks have been founded in real practice. A significant shortcoming of the EDA algorithm is that it tends to be trapped in a local minimum [20]. Another problem that might be encountered in EDA-GP is the stochastic sampling drift problem, which impedes the algorithm to achieve superior performance due to the loss of the population diversity [21].

Both genetic operators and EDA operators show their advantages and disadvantages in GEP offspring generation. Therefore, it is natural to combine both of these two kinds of operators in GEP. By integrating the EDA operator and genetic operators, the genetic algorithm will generate diverse solutions [20], and EDA can fully leverage the information in the evolutionary process to intensification the evolution process. These characteristics of the hybrid algorithm are important for the optimization process in the genetic programming domain, due to the multimodal landscape property of genetic programming.

As discussed in our previous work [17], the key issue is how to hybrid the two different kinds of offspring generation operators. There are three ways to do so, i.e., hybrid on the population level, the individual level, or the chromosome level. In this paper, we propose a hybrid offspring generation strategy on the individual level to give full play to the advantages of those two kinds of operators. In the new

approach, new offspring are partly sampled from a categorical distribution and partly generated via genetic operators. The new approach has been applied to ten PMLB regression datasets, and the experimental results demonstrate that the new approach outperforms the traditional GEP algorithm.
The main contributions of this paper are as follows:

- We hybrid EDA and GA offspring generation operators to enhance the performance of GEP. Our experiments demonstrate that the hybrid algorithm outperforms both EDA and GA based GEP algorithms.
- We design two sampling strategies and a standardization strategy for the EDA operator. By conducting experiments on ten benchmark datasets, these strategies exhibit different characteristics, and the best policy outperforms GA-GEP on eight out of ten datasets.
The remainder of this paper is organized as follows: Section II introduces the algorithm framework and the details of the individual evaluation, the probabilistic model, and the offspring generation. Section III presents some experiments on ten datasets for evaluating the performance of our proposed approach. We also discuss the impacts of the parameters on algorithm performance. Section IV summarizes the paper and discusses future works.


## II. ALGORITHM

In this section, we introduce the main algorithm, which involves two offspring generation strategies. The main components, including the individual evaluation, model definition, model initialization, model updating, and model sampling, are presented in detail.

## A. ALGORITHMIC FRAMEWORK

In this section, we propose a hybrid GEP algorithm $\left(G E P_{H}\right)$, which fuses information at the individual level. In other words, in each generation, some offspring are sampled from the probabilistic model, and the others are generated by applying genetic operators to some selected individuals. The pseudo-code of the $G E P_{H}$ algorithm is presented in Algorithm 1, and the flowchart is shown in Fig.3.

- Population initialization: In line 1, the population $X$ is randomly initialized by randomly sampling in the search space.
- Model initialization: In line 2, the probabilistic model $P$ is initialized as a uniform distribution.
- Individual evaluation: In line 3 and 21, the individual fitness $f_{x}$ is evaluated in terms of the mean squared error.
- Model updating: In line 5, each value $p$ in the EDA model $P$ is updated according to the fitness values.
- EDA offspring generation: In line 7-10, EDA offspring $X_{e}$ are generated by sampling from the probabilistic model $P$. $\left|X_{e}\right|$ represents the number of individuals generated by the EDA model.
- Parent selection: In line 11, GA uses the tournament selection operator [22] to select promising individuals for generating the population of the next generation.
$\left|X_{g}\right|$ represents the number of individuals generated by genetic operators.
- GA offspring generation: In line 12-19, offspring $X_{g}$ are generated by applying crossover and mutation operators to the selected promising individuals.
- Offspring merge: In line 20, EDA offspring and GA offspring are merged to generate a new population $X$.

```
Algorithm 1 Hybrid GEP Algorithm
    \(X \leftarrow\) population_initialization()
    \(P \leftarrow\) categorical_distribution initialization()
    \(\left\{f_{x} \mid x \in X\right\} \leftarrow\) evaluation(X)
    while iteration \(<\max\) _iteration do
        \(P \leftarrow\) updating \(\left(P,\left\{f_{x} \mid x \in X\right\}\right) \quad \triangleright\) Model updating
        \(X_{e}=\emptyset\)
        for \(i=1, \cdots,\left|X_{e}\right|\) do \(\triangleright\) EDA generation
            \(x \leftarrow \operatorname{sampling}(P)\)
            \(X_{e} \leftarrow X_{e} \cup\{x\}\)
        end for
        \(X_{g} \leftarrow \operatorname{selection}\left(X,\left|X_{g}\right|\right) \quad \triangleright\) Parent selection
        for \(i=1, \cdots,\left|X_{g}\right|\) do \(\triangleright\) GA generation
            if \(i \% 2==0 \& \operatorname{rand}()<p m\) then
                \(X_{g}^{i+1}, X_{g}^{i} \leftarrow \operatorname{crossover}\left(X_{g}^{i}, X_{g}^{i+1}\right)\)
            end if
            if \(\operatorname{rand}()<p c\) then
                \(X_{g}^{i} \leftarrow\) mutation \(\left(X_{g}^{i}\right)\)
            end if
        end for
        \(X \leftarrow X_{e} \cup X_{g}\)
        \(\left\{f_{x} \mid x \in X\right\} \leftarrow\) evaluation(X)
    end while
    return X
```


## B. INDIVIDUAL EVALUATION

1) INDIVIDUAL EVALUATION

This section introduces the individual evaluation process. This evaluation process is the same as the traditional evaluation process. For a k-dimensional input and a onedimensional output dataset $D=\left(z, y ; z \in R^{k}, y \in R\right)$, the basic evaluation function of an individual $x$ is defined as:

$$
f_{x}=-\operatorname{Loss}(E(z), Y)
$$

This function is similar to the traditional machine learning evaluation function. We use a negative sign before the loss value because our target is to maximize the fitness value. $E$ represents the symbolic expression of $x$, and $E(z)$ output a scalar value presents the predicted value of the specific task. Loss represents the loss function. For the regression problem, the mean absolute error (MAE) or the mean square error (MSE) can be used as a reasonable loss function [23].

In the remaining paragraphs, MSE is used as the evaluation metric. MSE is defined as follow:

$$
M S E(E(z), Y)=(E(z)-Y)^{2}
$$

![img-2.jpeg](img-2.jpeg)

FIGURE 3. The flowchart of the hybrid GEP algorithm.

## 2) FITNESS STANDARDIZATION

Since the value of the loss function depends on the training data, the magnitude of the training data will influence the fitness value. This will cause the updating scale of the probabilistic model becomes uncontrollable. Therefore, a fitness value standardization function can be applied to the fitness value. The standardization function is defined as below:

$$
f_{x}:= \begin{cases}\frac{f_{x}-p_{f}}{\sigma_{f}} & \text { if } \sigma_{f}>0 \\ 0 & \text { if } \sigma_{f}==0\end{cases}
$$

where $\mu_{f}$ represents the mean value of fitness values, i.e., $\mu_{f}=\frac{\sum_{i \in \mathcal{K}} f_{x}}{|\chi|} \cdot \sigma_{f}$ represents the variance value of fitness values, i.e., $\sigma_{f}=\frac{\sum_{i \in \mathcal{K}}\left(f_{x}-\mu_{f}\right)^{2}}{|\chi|}$.
When the standard deviation of fitness values is zero, the fitness values will not be standardized again. All fitness values should be set as zero in this scenario to avoid updating the probabilistic model. After the standardization, the standardized fitness values satisfy a Gaussian distribution fitness $\sim \mathcal{N}(0,1)$.

Fitness standardization is not an essential part of the model update process. The effects of fitness standardization are empirically studied in the following section.

## C. PROBABILISTIC MODEL

1) MODEL DEFINITION

The algorithm uses a group of univariate categorical distributions as the distribution model of programs. The group of


FIGURE 4. An illustration of gene points sampled from a categorical distribution in GEP $P_{N}$.
categorical distributions is defined as $\operatorname{Cat}(P)$, and $P$ is the probability matrix, which represents the likelihood of primitives on gene points. In the probability matrix $P, p_{i j}$ represents the likelihood to realize excellent performance when applying the j-th primitive at the i-th point.

Applying the univariate categorical distribution as the probabilistic model means that we do not consider the dependency between gene points. Due to each gene expression has several gene points, we use a group of univariate categorical distributions as the distribution model. For example, the categorical distribution can be represented as Fig.4. Each gene point is sampled from a categorical distribution, and multiple categorical distributions constitute an estimate of the distribution model.

## 2) MODEL INITIALIZATION

The categorical distribution is initialized as a uniform distribution since we have no prior knowledge of the target problems. For example, if the number of primitives is 5 , then we can initialize the categorical distribution as in Fig.5.

The initialization of the probability distribution can be expressed as:

$$
p_{i j}=\frac{1}{\text { primitive_amount }}
$$

where primitive_amount represents the number of primitives.

## 3) MODEL UPDATING

In the model updating process, the probability distribution is updated according to the fitness values. The update process is described as the below formula:

$$
p_{i j}:=p_{i j}+\sum_{i=1}^{n} \eta * f_{x}
$$

where $\eta$ represents the learning rate of the updating process, and $f_{x}$ is the standardized fitness value.

After updating the probabilistic model, some of the probability values might be less than zero. This will cause trouble in


FIGURE 5. An illustration of initialization of the categorical distribution in $\mathrm{GEP}_{\mathrm{H}}$.
the offspring generation process. Therefore, repair is applied to ensure that the probability is larger than zero.

$$
p_{i j}:=p_{i j}-\min _{j=1}^{m} p_{i j}
$$

In the following sections, $p_{i j}$ represents the repaired fitness value. After this step, each fitness value is guaranteed to be greater than zero.

## D. OFFSPRING GENERATION

After model initialization and model updating, offspring can be generated by applying the genetic operators and the EDA operators.

## 1) GA OFFSPRING GENERATION

In the genetic algorithm, crossover and mutation operators are used to generate offspring. Suppose there are two gene expressions $x^{1}=\left(x_{1}^{1}, x_{2}^{1}, x_{3}^{1} \ldots x_{n}^{1}\right)$ and $x^{2}=\left(x_{1}^{2}, x_{2}^{2}, x_{3}^{2} \ldots x_{n}^{2}\right)$, and a random integer $r \in[1, n]$ represents the crossover or the mutation point location. A typical crossover operation used in GEP is the single point crossover. By applying this operator, the gene points before the location $r$ are exchanged, and the result is $x^{1}=\left(x_{1}^{2}, x_{2}^{2}, x_{3}^{2} \ldots x_{r}^{2}, x_{r+1}^{1} \ldots x_{n}^{1}\right) x^{2}=$ $\left(x_{1}^{1}, x_{2}^{1}, x_{3}^{1} \ldots x_{r}^{1}, x_{r+1}^{2} \ldots x_{n}^{2}\right)$. A typical mutation operation used in GEP is the single point mutation. By applying this operator, the gene point at the location $r$ is mutated to a new value $x^{r_{j}^{1}}$. Then, the new gene expression is $x^{1}=\left(x_{1}^{1}, x_{2}^{1}, x_{3}^{1} \ldots x^{r_{j}^{1}} \ldots x_{n}^{1}\right)$. The crossover process of the single point crossover operator and the mutation process of the single point mutation operator are illustrated in Fig. 6 and Fig.7.

## 2) EDA OFFSPRING GENERATION

Since the new gene expression is composed of multiple primitives, generating a new offspring is equivalent to sampling new primitives from the categorical distributions.

Suppose a primitive $s_{i}$ is sampled from a categorical distribution $s_{i} \sim p_{i}$. Then, this primitive should be placed at location $i$ in the gene expression. For example, suppose the categorical distribution at the first point is plotted as Fig.4.
![img-3.jpeg](img-3.jpeg)

FIGURE 6. An illustration of single point crossover used in GEP.


FIGURE 7. An illustration of single point muation used in GEP.

Then, the primitive " + " may be sampled from this distribution and become the first gene point of this linear model.

Two strategies can be applied in the sampling process:

1) Probabilistic sampling strategy $\left(\mathrm{GEP}_{\text {HP }}\right)$ : sampling a primitive from the categorical distribution.
2) Max sampling strategy $\left(\mathrm{GEP}_{H M}\right)$ : choosing the primitive that corresponds to the maximum probability.
When using the probabilistic sampling strategy, one must ensure that $\sum_{j=1}^{n} p_{i j}^{k}=1$ is satisfied. Hence, a normalization process should be applied. The normalization process is described as the following formula:

$$
p_{i j}^{k}=\frac{p_{i j}^{k}}{\sum_{j=1}^{m} p_{i j}^{k}}
$$

The algorithm 2 shows the process of EDA offspring generation.

```
Algorithm 2 EDA Offspring Generation
for \(i=1, \cdots, n\) do
    for \(j=1, \cdots, m\) do
        \(p_{i j} \leftarrow \frac{p_{i j}}{\sum_{j=1}^{m} p_{i j}} \quad \Delta\) Normalization
        end for
        if strategy \(==\mathrm{GEP}_{\text {HP }}\) then
            \(x_{i} \leftarrow \operatorname{sample}\left(p_{i}\right)\)
        else if strategy \(==\mathrm{GEP}_{M P}\) then
            \(x_{i} \leftarrow \arg \max _{i} p_{i}\)
        end if
    end for
    return \(x\)
```

- In line 3, the probability value is normalized to make sure the sum of probability values is equal to one.
- In line 5-9, a new gene point $x_{i}$ is sampled from the categorical distribution $p_{i}$.

TABLE 1. Parameter settings.

TABLE 3. Operators.


## III. EXPERIMENTS

## A. EXPERIMENT ENVIRONMENT

1) PARAMETER SETTINGS

Unless otherwise stated, the experiments are conducted using the parameters in TABLE 1.

- The population size is 20 , and all algorithms stop after 200 iterations.
- Each chromosome has only one gene expression. The head length $h$ is set as 50 , and RNC length is set as 15 . The RNC range is set as $[-25,25]$. The learning rate and the EDA individual ratio are determined by experiments in the following section.
- The function operators that are used in GEP are introduced in TABLE 2. The max arity $a$ corresponds to these operators is 3 . The tournament selection algorithm [22] is adopted with a tournament size of 5 .
- The fitness standardized version of $G E P_{H}$ with the probabilistic sampling strategy $\left(G E P_{H S P}\right)$ is used as the default $G E P_{H}$ algorithm.
- Every experiment is conducted on each dataset with 50 distinct random seeds. To ensure reproducibility, we set the random seed of the pseudo-random generator of Numpy [24] with a range from 0 to 49.


## 2) EXPERIMENTAL DATASET

In order to evaluate the universality of the algorithm, ten datasets from the PMLB dataset [25] were used to evaluate the performance of our algorithm. In order to reveal the general applicability of the proposed algorithm, the size of benchmark datasets is ranged from 60 to 8192 , and the number of features is spanned from 4 to 22 . Detailed information of these datasets is presented in TABLE 3.

TABLE 3. Experimental datasets.


In the hyper-parameter study part, we use "195_auto_price" and "197_cpu_act" to study the impacts of various hyperparameter values.

## B. CONTROL PARAMETER SENSITIVITY

When introducing the EDA algorithm into GEP, two parameters are also introduced: the learning rate $\eta$ and the EDA offspring ratio, i.e., $\frac{X_{c}}{\left(X_{c}+X_{g}\right)}$. Like many other machine-learning hyperparameters, it is hard to give a proper value beforehand. The most suitable value must be determined based on data.

In industrial applications, algorithms that are insensitive to the hyperparameter or for which the hyperparameter is easy to determine based on simple principles are popular because these algorithms require low computation resources to yield a satisfactory result. Therefore, the influence of various hyperparameters is the focus of this section.

## 1) LEARNING RATE

The learning rate can control the convergence speed of the EDA probabilistic model. If a low learning rate is chosen, the probabilistic model will cost much time to converge to the optimal distribution. If a high learning rate is chosen, the probabilistic model will converge quickly. However, a high learning rate may also impede the model converge to the optimal model due to it can not fine-tune the probability distribution. Therefore, the selection of an appropriate learning rate is challenging many machine learning engineers. An algorithm that can easy to choose a reasonable learning rate is more likely to be applied in industrial scenarios.

The current experiment focuses on identifying the relationship between algorithm performance and the learning rate. The "195_auto_price" dataset has been chosen with a learning rate from 0.1 to 1 with a step interval of 0.1 .

Fig. 8 and Fig. 9 present the experiment results of the "195_auto_price" dataset. The "Baseline" presents the performance of GEP without EDA. The experimental results reveal that the learning rate of 0.3 is the most suitable learning rate. Although results are unstable with different learning rates, they universally outperform the GA-GEP algorithm. However, a careful choice of the learning rate will yield a much better result.

![img-4.jpeg](img-4.jpeg)

FIGURE 8. MSE versus learning rate on "195_auto_price".
![img-5.jpeg](img-5.jpeg)

FIGURE 9. MSE versus learning rate on "195_auto_price".

Fig. 10 and Fig. 11 present another experiment on the "197_cpu_act" dataset with a 0.1 EDA individual ratio. The results demonstrate that a learning rate of 1.0 yields the best result.

From the above two experiments, we conclude that: $G E P_{H}$ can not find a clear rule for determining the best learning rate. However, even though a worse learning rate has been chosen, it also achieves better results than the $G E P_{G}$ algorithm.

## 2) EDA OFFSPRING RATIO

In Section II, we proposed a hybrid EDA and GP algorithm that integrates the advantages of these two algorithms. However, this algorithm introduces a new parameter, the EDA offspring ratio, which must be specified based on the specific task.

Therefore, an experiment is conducted to investigate the effects of various values of the EDA offspring ratio. Our experiment considers offspring ratios from 0 to 1 , with a step interval of 0.1 . If the ratio is 0 , it is equivalent to the GA-GEP algorithm. If the ratio is 1 , it is equivalent to the EDA-GEP algorithm.
![img-6.jpeg](img-6.jpeg)

FIGURE 10. MSE versus learning rate on "197_cpu_act".
![img-7.jpeg](img-7.jpeg)

FIGURE 11. MSE versus learning rate on "197_cpu_act".

Fig. 12 plots MSEs with various offspring ratios of the "195_auto_price" dataset. This figure demonstrates that the best performance of the hybrid algorithm achieves when the EDA individual ratio equals to 0.1 . In this experiment, the hybrid algorithm reveals better performance than the GA-GEP algorithm and the EDA-GEP algorithm. Moreover, although the hybrid algorithm performs much better with the EDA offspring ratio increases, after reaching a specific threshold, the performance of the hybrid algorithm is decreased with the EDA offspring ratio increases. This phenomenon proves the necessity of the hybrid algorithm.

Fig. 13 presents another experiment on the "197_cpu_act" dataset, which is based on a learning rate of 0.4 . The result is similar to the experimental result that is presented above, too high or too low of the ratio will cause the final result to deteriorate, and the EDA individual ratio of 0.2 achieves the best result.

Considering both the above two experiment results, we can conclude that: a reasonable offspring ratio is close to 0.1 . The more precisely value must be determined based on the specific task.

TABLE 4. Experimental results obtained by four comparison algorithms.


![img-8.jpeg](img-8.jpeg)

FIGURE 13. MSE versus EDA offspring ratio on "195 auto price".

## C. A COMPARISON STUDY ON THE PMLB DATASET

## 1) EXPERIMENT CONFIGURATION

In order to have a fair comparison of GA-GEP $\left(G E P_{G}\right)$, max sampling strategy $G E P_{H}\left(G E P_{H M}\right)$, and probabilistic sampling strategy $G E P_{H}\left(G E P_{H P}\right)$, experiments are conducted with the same parameters. Details on the parameters are presented in TABLE 1. We also conduct an experiment with standardized fitness values based $G E P_{H P}$ algorithm $\left(G E P_{H S P}\right)$ for comparison with the unstandardized version of the algorithm.

For the sake of reproducibility, the pseudo-random generator is used again. The learning rate and the EDA generation individual ratio are only applied to the hybrid algorithm.

## 2) EXPERIMENTAL RESULTS

Fig. 14 uses a box plot to present the experimental results, and TABLE 4 gives the median values of 50 experiment results with various random seeds. The final results demonstrate that $G E P_{H S P}$ exhibits satisfactory performance on these datasets.

Experimental results show that $G E P_{H S P}$ outperforms $G E P_{G}$ on eight tasks. $G E P_{H M}$ and $G E P_{H P}$ are the secondbest ones because they outperform $G E P_{G}$ on seven tasks. $G E P_{H S P}$ and $G E P_{H M}$ both perform poorly on the " 527 analcatdata_election2000" and " 561 cpu " datasets. On the contrary, $G E P_{H P}$ performs well on these datasets. Therefore, it is reasonable to consider $G E P_{H P}$ as a complementary strategy, which can be applied when $G E P_{H S P}$ does not perform well.
![img-9.jpeg](img-9.jpeg)

FIGURE 13. MSE versus EDA offspring ratio on "197 cpu act".

Although $G E P_{H M}$ performs poorly on three datasets and does not remedy the shortcomings of $G E P_{H S P}$, the algorithm can still have a place in some scenarios. For example, $G E P_{H S P}$ realizes the best performance on the " 666 rmftsa_ladata" dataset. Therefore, we can consider $G E P_{H M}$ as an alternative strategy to pursue superior performance.

In essence, $G E P_{H P}$ and $G E P_{H S P}$ are equivalent in a way because we can regard the scale of loss value in $G E P_{H P}$ as the scale of the learning rate. Section III shows that there is no universal principle for selecting an appropriate learning rate. Therefore, it is difficult to explain the different characteristics between $G E P_{H S P}$ and $G E P_{H P}$. However, due to the substantial differences and complementary property of different learning rate strategies, an adaptive learning rate algorithm that can combine the benefits of $G E P_{H P}$ and $G E P_{H S P}$ may effectively improve the performance of $G E P_{H}$ algorithms, and it deserves further investigation in further works.

Fig. 15 presents the training processes of ten datasets. This figure supports our conclusion that the hybrid strategy can generate a better model than the traditional strategy. From the training curves, we find that $G E P_{H M}$ can speed up the training process on some datasets, such as on the " 666 _rmftsa_ladata" dataset. In the training process of " 666 _rmftsa_ladata", $G E P_{H M}$ may find some inherent patterns which lead it performs much better than other

![img-10.jpeg](img-10.jpeg)

FIGURE 14. Experimental results obtained by four algorithms on ten benchmark datasets.
![img-11.jpeg](img-11.jpeg)

FIGURE 15. Training curves obtained by four algorithms on ten benchmark datasets.
strategies. Finally, $G E P_{H M}$ achieves the lowest training loss on " 666 _rmftsa_ladata", and also achieves the best generalization performance among other strategies as shown in TABLE 4. Although $G E P_{H M}$ performs much better than other strategies on " 666 _rmftsa_ladata", it should be pointed out
that $G E P_{H M}$ performs much inferior to other strategies on the " 227 _cpu_small" dataset. Therefore, $G E P_{H M}$ should be used cautiously in real practice. By contrast, $G E P_{H S P}$ reveals superior performance on "557_analcatdata_apnea1" and "227_cpu_small" datasets comparing with other strategies,

TABLE 5. List of abbreviations.

and also with competent performance on other datasets, which confirms that $G E P_{H S P}$ is a relatively good strategy among other strategies.

## IV. CONCLUSION AND FUTURE WORK

In this paper, we considered utilizing both genetic and EDA operators for the offspring generation. To this end, a hybrid offspring generation algorithm was proposed for GEP in which some of the solutions are generated by genetic operators, and some of the solutions are generated by EDA operators. The EDA operator constructs a univariate categorical distribution and then samples the offspring randomly from that categorical distribution. In this way, the individual information and the population information are combined. The disadvantages faced by genetic operators and EDA operators are thus solved.

The new algorithm was applied to ten datasets, and the experimental results demonstrate that this new hybrid algorithm can outperform the GA algorithm for symbolic regression problems. The effects of two offspring generation strategies and the fitness standardization strategy were empirically studied via experiments. The experimental results demonstrate that the standardized probabilistic sample strategy $G E P_{H}\left(G E P_{H S P}\right)$ algorithm is the most suitable algorithm for most regression tasks. The effect of hyperparameters, such as the effect of different EDA learning rates, and the effect of different EDA individual ratios, had also been empirically studied. The results from these experiments demonstrate that the worse learning rate can also perform better than the GA based algorithm $\left(G E P_{G}\right)$, and an appropriate EDA individual ratio is approximately 0.1 .

The work reported in this paper is preliminary. Several issues should be considered in the future. For example, although the hybrid model can achieve substantial improvements, a carefully selected learning rate is also important to achieve superior performance. Therefore, an adaptive learning rate method merits future investigation. Moreover, designing a more fine-grained hybrid algorithm is also a
promising direction to further improve the performance of the hybrid GEP algorithm.

## LIST OF ABBREVIATIONS

A list of abbreviations used in this paper is given in TABLE 5.
