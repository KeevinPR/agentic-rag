# Feature Selection for High-Dimensional Remote Sensing Data by Maximum Entropy Principle based Optimization 

Shixin Yu Paul Scheunders<br>Department of Physics, University of Antwerp<br>Antwerp, B-2020, Belgium


#### Abstract

For high-dimensional remote sensing data, the appropriate selection of features has a significant effect on the cost and accuracy of an automated classifier. In this paper, a method for feature selection by Estimation of Maximum Entropy Principle Algorithm, is presented. This method based on the EDA (Estimation of Distribution Algorithm) paradigm, avoids the use of crossover and mutation operators to evolve the populations, in contrast to Genetic Algorithms. It is combined with an approximate application of the Maximum Entropy Principle as the models for representing the probability distribution of a set of candidate solution in the feature selection problem, using the application of automatic learning methods to induce the right distribution model in each generation. Computational comparison is made between EDA in combination with Bayesian networks and EDA in combination with Maximum Entropy Principle. Experiments are performed on AVIRIS dataset.


## 1 Introduction

Advances in sensor technology for earth observation make it possible to collect large numbers of spectral bands. For example, the NASA/JPL Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) generates image data in more than 220 spectral bands simultaneously. For such high dimensionality, pattern recognition techniques suffer from the well-known curse-of-dimensionality phenomenon. This problem is resulting from the fact that the required number of labeled samples for supervised classification increases dramatically as a function of dimensionality [1].
In this paper, an approximate application of the Maximum Entropy Principle [3] is applied to feature selection problem for high dimentional remote sensing data. This method based on the EDA (Estimation of Distribution Algorithm) [4] paradigm, avoids the
use of crossover and mutation operators to evolve the populations, in contrast to Genetic Algorithms. It is combined with an approximate application of the Maximum Entropy Principle as the models for representing the probability distribution of a set of candidate solution in the feature selection problem, using the application of automatic learning methods to induce the right distribution model in each generation. This paper is organized as follows: Section 2 introduces the EDA paradigm, Bayesian networks and the EBNA search algorithm. Section 3 presents a new algorithm base on an approximate application of the maximum entropy principle. Section 4 summaries the primary results of comparasion.

## 2 EDA Paradigm and EBNA Algorithm

Genetic Algorithms(GAs) [2] are one of the well known optimization tools, based on population search with two operators: crossover and mutation. In contrast to GAs, the Estimation of Distribution Algorithm (EDA) [4] has neither crossover operator nor mutation operator. The scheme of EDA is as follows:
$D_{0} \leftarrow$ Generate $N$ individuals from the initial population randomly.
Repeat for $1=1,2, \ldots$, until a stop criterion is met.
$D_{l-1}^{s} \leftarrow$ Select $S \leq N$ individuals from
$D_{l-1}$ according to a method.
$p_{l}(X)=p\left(X \mid D_{l-1}^{s}\right) \leftarrow$ Estimate the joint probability distribution of an individual being among the selected individuals.
$D_{l} \leftarrow$ Sample N individuals from $p_{l}(X)$.
There are many methods proposed in the literature to estimate the distribution probability: Population Based Incremental Learning (PBIL) [5], Compact Genetic Algorithm (cGA) [6], Univariate Marginal Dis-

tribution Algorithm (UMDA) [7] and Bit-Based Simulated Crossover (BSC) [8] are four algorithms which assume independence among the features. Populationbased MIMIC algorithm using simple chain distribution [9], Dependece trees [10], and Bivariate Marginal Distribution Algorithm (BMDA) [11] are typical algorithms which cover pairwise interactions among the features. Most recently, Inza [12] proposed an algorithm called EBNA, which is based on EDA paradigam, using bayesian networks as the models for representing the probability distribution of a set of candidate solutions. We will compare our proposed algorithm with EDNA in the paper.

## 3 Maximum Entropy Principle based Optimization

Jaynes [16] pioneered maximum entropy (ME) principle to do inference, cheeseman [17] proposed a clever technique to improve the compution efficiency of ME joint probability distribution, following work of Ku and Kullback [18], but no learning method was proposed. Most recently, Yan and Miller [3] proposed an approximate ME method, which encodes arbitrary low-order constraints but while retaining quite tractable learning. we here follow their discussion. For a feature vector $F=\left(F_{1}, F_{2}, \ldots, F_{n}\right)$ with $F_{i} \in$ $\mathcal{A}_{i}$, the ME joint probability consistent with pairwise probabilities is written as follows:

$$
P[f]=\frac{\exp \left(\sum_{m=1}^{N-1} \sum_{n>m}^{N} \gamma\left(f_{m}, f_{n}\right)\right)}{\sum_{f^{\prime} \in \mathcal{G}} \exp \left(\sum_{m=1}^{N-1} \sum_{n>m}^{N} \gamma\left(f_{m}^{\prime}, f_{n}^{\prime}\right)\right)}
$$

where $\mathcal{G}$ is the full feature space, $\gamma\left(f_{m}, f_{n}\right)$ is the Lagrange multiplier. If one uses the Lagrangian method to do direct optimization, the Lagrangian cost has the form $D-T H$, where $H$ is the joint entropy, $D$ is a cost function encoding the equality constraints on pairwise probabilities, and $T$ is a Lagrange multiplier. Then next minimize $D-T H$ over $\gamma\left(f_{m}, f_{n}\right)$, but as $H$ and $D$ are explicitly expressed as functions of the joint probability with the form of the above equation, so the optimization process is intractable. Yan and Miller [3] proposed to do a restriction on joint probability support in order to achieve tractable learning, i.e. $P[F]$ is restricted to $f \in \mathcal{G}_{s} \subset \mathcal{G}$. By a Lagangian reformulation, the quantities $H$ and $D$ have the


Table 1: Primary results and some papameters
following forms respectively [3]:

$$
\begin{aligned}
& H=\quad-\sum_{m=1}^{|\mathcal{G}_{j}|} P\left[f_{m}\right] \log P\left[f_{m}\right]- \\
& \frac{1}{N} \sum_{k=1}^{N} \sum_{m=1}^{|\mathcal{G}_{j}|} P\left[f_{m}\right] \sum_{i=1}^{|\mathcal{A}_{i}|} P\left[F_{k}=i \mid f_{m}^{-k}\right] \\
& \times \log P\left[F_{k}=i \mid f_{m}^{l}-k\right] \\
& D=\sum_{k=1}^{N} \sum_{l=1, l \neq k}^{N}\left(\sum_{i=1}^{|\mathcal{A}_{i}|} \sum_{j=1}^{|\mathcal{A}_{i}|} P\left[F_{k}=i, F_{l}=j\right]\right. \\
& \left.\times \log \frac{P\left[F_{k}=i, F_{l}=j\right]}{P_{M}^{(\mathcal{A})}\left[F_{k}=i, F_{l}=j\right]}\right)
\end{aligned}
$$

Given $D$ and $H$, the Lagrangian cost $D-T H$ can be formed, and the solution maximizes $H$ under the constraints $D=0$.
Once the joint probability is obtained, the ME model can be now used to do feature selection in combination with EDA schema.

## 4 Experiments and Discussion

Experiments were conducted on an AVIRIS dataset, containing 220 bands of $145 \times 145$ pixels, that is downloadable from [13], along with a groundtruth image, containing 16 classes. The primary experimental result is shown in Table 1 with some papameters. The $M L C$ software [19] was used to execute ID3 algorithm, and for random number generator, the GAlib [20]'s implementation was used.
we only did a primary experiment on 30 -band data with 2 classes. When the dimensionality increases, the computation time increases dramatically, so how to solve the computional complexity of ME model remains a topic. We are currently looking for methods, e.g.[21], [22], which might improve the computation efficiency of ME model.

## Acknowledgments

The authors wish to thank Dr. I. Inza of the department of computer science and artificial intelligence, University of Basque County, Spain, for the implementation of bayesian networks, and for his helpful suggestions.
