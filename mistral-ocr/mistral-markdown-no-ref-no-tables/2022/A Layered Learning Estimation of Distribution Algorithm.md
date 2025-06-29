# A Layered Learning Estimation of Distribution Algorithm 

Yong Li, Qiang Yang*, Xu-Dong Gao, Zhen-Yu Lu<br>School of Artificial Intelligence, Nanjing University of Information Science and Technology, Nanjing, China. Jun Zhang<br>Department of Electrical and Electronic Engineering, Hanyang University, Ansan, Korea.<br>Department of Computer Science and Information Engineering, Chaoyang University of Technology, Taichung, Taiwan.<br>*Corresponding author: Qiang Yang (mmmyq@126.com)


#### Abstract

Though estimation of distribution algorithms (EDAs) have witnessed success in problem optimization, most of them suffer from sharp shrink of covariance, which may lead to premature convergence. To alleviate this issue, this paper proposes a layered learning estimation of distribution algorithm (LLEDA) by maintaining multiple probability distribution models. Specifically, LLEDA first separates the population into several layers based on fitness. Then, the mean position of each layer is computed. Subsequently, we let the estimated mean position in each lower layer randomly learn from the one of a randomly selected higher layer, so that the mean positions of lower layers could be promoted to be close to promising areas found in the current population. At last, the covariance of each layer is estimated based on the generated new mean position and the individuals in this layer. By this means, multiple probability models with high quality are maintained and then are used to sample promising and diversified offspring separately. Comparative experiments conducted on a widely used benchmark problem set demonstrate that the proposed LLEDA achieves competitive or even much better performance than several state-of-the-art and representative EDAs.


## CCS CONCEPTS

- Mathematics of computing $\rightarrow$ Evolutionary algorithm; Bioinspired optimization;


## KEYWORDS

Estimation of Distribution Algorithms, Multivariate Gaussian Distribution, Layered Learning, Multiple Distribution Models, Global Numerical Optimization

## ACM Reference format:

Yong Li, Qiang Yang, Xu-Dong Gao, Zhen-Yu Lu and Jun Zhang. 2022. A Layered Learning Estimation of Distribution Algorithm. In Proceedings of Genetic and Evolutionary Computation Conference Companion (GECCO '22 Companion), July 9-13, 2022, Boston, MA, USA. ACM, New York, NY, USA, 4 pages.
https://doi.org/10.1145/3520304.3528904

[^0]
## 1 INTRODUCTION

Estimation of distribution algorithms (EDAs) [1-4] have been regarded as a special branch of evolutionary algorithms (EAs) since it was proposed in 2001 [5]. Different from traditional EAs, like particle swarm optimization (PSO) [6-8], which generate offspring based on individuals, EDAs generate new solutions via a specific probability distribution model, which is estimated based on highquality solutions in the current population. Due to the random sampling of offspring, EDAs generally preserve high search diversity and strong robustness [9].

In the literature, most EDAs use the Gaussian model to evaluate the probability distribution, and then sample new solutions based on the estimated Gaussian model [10]. These EDAs are usually called Gaussian estimation of distribution algorithms (GEDAs). Based on whether the correlation between variables is considered, existing GEDAs are mainly divided into two categories [9], namely univariate GEDAs (UGEDAs) [10] and multivariate GEDAs (MGEDAs) [11]. Compared with UGEDAs, MGEDAs generally achieve better performance especially on problems with many interacting variables [9].

However, when dealing with complex optimization problems, especially those with many wide and flat local basins [11], most MGEDAs suffer from premature convergence due to the rapid shrink of variances [9]. To alleviate this deficiency, researchers have focused their attention on designing novel techniques to promote the search diversity of EDAs. For instance, in [12], Grahl et al. proposed a correlation-triggered adaptive covariance scaling strategy to avoid premature convergence by adaptively multiplying a factor to the estimated variance based on the change of the global best solution. In [13], Bosman et al. designed an indicator, named standard-deviation ratio (SDR), to capture the improvements and then used this measure to scale the covariance when the captured improvements are far away from the mean vector. In [14], Cai et al. proposed a cross-entropy based adaptive covariance scaling method. In this approach, the covariance scaling factor is computed by minimizing the cross-entropy between the sampled population and the prediction of the probabilistic model. In [2], Liang et al. proposed a new GEDA variant, named EDA2, which utilized an archive to store historical information, and then estimated the distribution model through this archive to enlarge the covariance.

In addition, some researchers have also proposed some significant improvements in the mean vector estimation. For instance, Bosman et al. [15] designed an anticipated mean shift (AMS) scheme to shift the mean vector of the Gaussian distribution,


[^0]:    Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for thirdparty components of this work must be honored. For all other uses, contact the Owner/Author.
    GECCO '22 Companion, July 9-13, 2022, Boston, MA, USA
    (c) 2022 Copyright is held by the owner/author(s).

and then used the shifted mean vector along with the selected solutions to estimate the covariance matrix. In this way, the search direction could be corrected to a certain extent. In [16], Ren et al. proposed to utilize different mean vector shifts according to the difference between the mean vector estimated in the current generation and the one in the previous generation.

Even though a large number of significant EDA variants have been developed and achieved good performance in problem optimization, they all maintain only one distribution model during the evolution. Besides, the maintained distribution model is estimated only on a very small number of high-quality solutions with the others discarded. This will lead to serious loss of evolutionary information and heavy sacrifice of search diversity.

To alleviate this predicament, this paper devises a layered learning EDA (LLEDA). Different from existing MGEDAs with only one distribution model in the population, LLEDA maintains multiple probability distribution models for the population in each generation. To be specific, the current parent population is first sorted based on the fitness from the best to the worst, and then it is divided into several layers. Subsequently, each layer uses its own individuals to construct a distribution model. To improve the quality of sampled individuals, a learning method is introduced to let the mean vectors in the lower layers learn from the one randomly selected from higher layers. In this way, the distribution models in lower layers are expectedly promoted and thus the sampled offspring could be improved. With multiple distribution models, the search diversity of LLEDA is expectedly amplified largely, which is beneficial for EDA to escape from local basins.

To validate the effectiveness of LLEDA, we conduct experiments on the commonly used CEC 2014 benchmark set [17] by comparing LLEDA with several state-of-the-art EDA variants.

## 2 PROPOSED LLEDA

Given that $N P$ individuals are maintained in the population, the proposed LLEDA first sorts all individuals based on their fitness from the best to the worst. Then, the $N P$ individuals are divided into $N L$ layers equally with each layer containing $h_{i}=N P / N L(1 \leq i \leq N L)$ individuals (if $N P \% N L \neq 0$, the remaining $N P \% N L$ individuals are equally placed into the first $N P \% N L$ layers). For better

```
Algorithm 1: The overall procedure of LLEDA
Input: population size NP; Number of layers NL, Learning step \(P\);
    1: Initialize NP individuals randomly, evaluate their fitness, and \(F E s=N P\);
    2: Obtain the global best solution Gbest;
    3: While \((F E s<F E s_{\text {new }}\) )
    4: Divide the population into NL layers and calculate the mean vector of each
        layer based on Eq. (1);
    5: Except for the first layer, let each layer learn from a randomly selected higher
        layer based on Eq. (2);
    6: Estimate the covariance matrix \(\boldsymbol{C}_{\boldsymbol{i}}\) of each layer according to Eq. (3);
    7: Each layer separately samples \(h_{i}\) offspring randomly, calculates their fitness,
        and sets \(F E s=F E s+h_{i}\);
    8: Combine the offspring in the last generation and the ones in the current
        generation to select the NP best individuals to form the parent population;
    9: Update the global best solution Gbest;
    10: Execute the local search method 2 times on Gbest, and \(F E s=F E s+2\);
    11: End While
Output: the global best solution Gbest;
```

understanding, we denote each layer by $l_{i}(1 \leq i \leq N L)$ and the smaller the layer index is, the better the individuals in this layer are.

After the partition of the population, each layer first separately estimates its own probability distribution with respect to the mean vector of the Gaussian distribution as follows:

$$
\boldsymbol{\mu}_{i}=\frac{1}{h_{i}} \sum_{j=1}^{N} \boldsymbol{S}_{i}^{j} \quad(1 \leq i \leq N L)
$$

where $\boldsymbol{\mu}_{i}$ denotes the mean vector of the $i$ th layer, $\boldsymbol{S}_{i}$ represents the set of individuals in this layer, $\boldsymbol{S}_{i}^{j}$ is the $j$ th individual in the $i$ th layer, and $h_{i}$ is the number of individuals in this layer.

By means of the above manner, each layer has its own mean vector, and the higher the layer is, the closer to promising areas its mean vector expectedly is. Since the mean vectors of lower layers are slightly far away from the promising areas, we develop a layered learning strategy for lower layers to promote the quality of their distribution models, so that promising offspring could be sampled. Specifically, we let the mean vector of each lower layer learn from a randomly selected one of a higher layer in the following way:
$\boldsymbol{\mu}_{i, \text { new }}=\boldsymbol{\mu}_{i}+F^{*}\left(\boldsymbol{\mu}_{\text {rand }}-\boldsymbol{\mu}_{i}\right)(1 \leq i \leq N L, 1 \leq \operatorname{rand}<i)$
where $\boldsymbol{\mu}_{i}$ represents the mean vector of the $i$ th layer, while $\boldsymbol{\mu}_{\text {rand }}$ is the mean vector of a higher layer, which is randomly selected from those layers higher than the $i$ th layer. That is to say, rand is randomly sampled within $[1, i]$.

By means of Equation (2), the mean vector of each lower layer is expectedly closer to promising areas, and thus high-quality offspring are expectedly sampled. It should be mentioned that for the first layer, namley $l_{1}$, since there is no higher layer for it to learn from, we keep its mean vector unchanged.

After the learning of the mean vector of each layer, the covariance of each layer is then estimated by using the updated mean vector and the individuals in this layer in the follwing way:

$$
\boldsymbol{C}_{i}=\frac{1}{h_{i}-1}\left(\boldsymbol{S}_{i}-\boldsymbol{\mu}_{i, \text { new }}\right)\left(\boldsymbol{S}_{i}-\boldsymbol{\mu}_{i}\right)^{T} \quad(1 \leq i \leq N L)
$$

With the above manners, multiple high quality probability distribution models are maintained in the population. Therefore, with these distribution models, diversified offspring could be generated and hence high search diversity could be maintained during the evolution, which is beneficial for the population to escape from local areas.

To further enhance the balance between high search diversity and fast convergence speed, we further introduce a crossgeneration individual selection method to select individuals for the parent population. Specifically, we combine the offspring in the last generation and the ones in the current generation together and then select the $N P$ best individuals to form the parent population for the next generation. Subsequently, the parent population is divided into multiple layers and multiple distribution models are estimated.

Since EDAs preserve poor local exploitation ability, we further conduct the following local search method around the global best position (Gbest) to improve its accuracy:
Ind $=$ Gaussian $($ Gbest, $\left.1 \times 10^{-4}\right)$
In particular, we conduct the local search method in each

TABLE 1. Comparison between LLEDA and the compared state-of-the-art EDA variants on the 100-D CEC2014 benchmark functions.


In addition, to make fair and comprehensive comparisons, we execute each algorithm independently 30 times on each benchmark function, and then report the mean value and the standard deviation value over the 30 runs to evaluate the optimization performance of each algorithm. Besides, we also perform the Wilcoxon rank-sum test at the significance level of $\alpha=0.05$ to compare LLEDA with each compared EDA variant on each benchmark problem. Meanwhile, the Friedman test at the significance level of $\alpha=0.05$ |  |  |  |  |  |  |

is also carried out to obtain the overall optimization performance of each algorithm on the whole 100-D CEC 2014 benchmark set.

Table 1 shows the comparison results between LLEDA and the compared EDA variants. The symbols " + ", "-", and "=" above the mean values mean that LLEDA is significantly better than, significantly worse than and equivalent to the associated compared EDAs on the corresponding functions, which is determined by the Wilcoxon rank-sum test results. " $w / t / l$ " in the second to last row counts the numbers of " + ", "=", and "-", respectively. From this table, we obtain the following findings:

1) From the Friedman test results, it is observed that LLEDA achieves the lowest rank among all algorithms, and its rank value is much lower than the other algorithms except for EDA2. This proves that LLEDA obtains the best overall performance on the 100-D CEC 2014 benchmark set and it is significantly superior to all compared EDAs except for EDA2.
2) From the Wilcoxon rank sum test results, it is found that LLEDA is significantly superior to EDA/LS, EDA/LS-MS, and TRA-EDA on at least 24 functions, and shows inferiority to them on at most 5 functions. Compared with EDAvERS and BUMDA, LLEDA significantly outperforms them on 19 and 15 functions, respectively. In competition with EDA2, LLEDA achieve highly competitive performance on the 100$D$ CEC 2014 benchmark set.

In summary, the above experiments demonstrate the great superiority of LLEDA to the compared state-of-the-art EDA variants on the 100-D CEC 2014 benchmark set. Such superiority of LLEDA mainly benefits from the proposed layered learning method and the cross-generation individual selection strategy. With the layered learning strategy, LLEDA maintains multiple highquality probability distribution models. In this way, the evolutionary information of the population is fully made use of to sampled diversified individuals. With the help of the corssgeneration individual selection scheme, LLEDA selects highquality but diversified individuals for the parent population. By means of the cohesive cooperation between the two mechanisms, LLEDA expectedly compromises search intensification and diversification well to find high-quality solutions.

## 4 CONCLUSION

In this paper, we have proposed a layered learning estimation of distribution algorithm (LLEDA) to improve the optimization performance of EDA in solving complicated optimization problems. By means of dividing the population into multiple layers and separately estimating the probability distribution model of each layer, LLEDA maintains multiple distribution models to fully utilize the evolutionary information of the whole population. To improve the quality of the estimated distribution models, LLEDA lets the mean vector of each lower layer learn from the one of a randomly selected higher layer. In this way, it is expected that multiple high-quality distribution models can be maintained to sample high-quality and diversified offspring to seek promising solutions. In addition, a cross-generation individual selection strategy and a local search mechanism have further introduced into LLEDA to enhance the search diversity and promote the local exploitation, so that high-quality solutions can be found.

Comparative experiments have been conducted on the 100-D

CEC 2014 benchmark set by comparing LLEDA with several state-of-the-art EDA variants. Experimental results have demonstrated the great superiority of LLEDA to the compared EDA variants in solving optimization problems.

## ACKNOWLEDGEMENTS

This work was supported in part by the National Natural Science Foundation of China under Grant 62006124 and U20B2061, in part by the Natural Science Foundation of Jiangsu Province under Project BK20200811, in part by the Natural Science Foundation of the Jiangsu Higher Education Institutions of China under Grant 20KJB520006, and in part by in part by the National Research Foundation of Korea (NRF-2021H1D3A2A01082705).
