# Improving the estimation of distribution algorithm with a differential mutation for multilevel thresholding image segmentation 

Jorge Armando Ramos-Frutos ${ }^{1}$ - Israel Miguel-Andrés ${ }^{1}$, Diego Oliva ${ }^{2}$, Angel Casas-Ordaz ${ }^{2}$<br>Received: 24 October 2023 / Accepted: 16 March 2024<br>(c) The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2024


#### Abstract

Image segmentation consists of separating an image into regions that are entirely different from each other, and multilevel thresholding is a method used to perform this task. This article proposes an Estimation of Distribution Algorithms (EDA) combined with a Differential Evolution (DE) operator as a metaheuristic to solve the multilevel thresholding problem. The proposal is called the Differential Mutation Estimation of Distribution Algorithm (DMEDA), where the inclusion of the Differential Mutation increases the standard EDA's exploration capacity. The performance of the DMEDA for image segmentation is tested using Otsu's between-class variance and Kapur's entropy as objective functions applied separately over the Berkeley Segmentation Data Set 300 (BSDS300). Besides, a comparative study includes eight well-known algorithms in the literature. In this sense, statistical and non-parametric tests are performed to verify the efficiency of the DMEDA in solving the image segmentation problem from an optimization perspective. In terms of segmentation, different metrics are employed to verify the capabilities of the DMEDA to segment digital images properly. Regarding the two objective functions, the proposed DMEDA obtains better results in $97 \%$ of the experiments for Otsu's between-class variance and $85 \%$ for Kapur's entropy.


Keywords Image segmentation $\cdot$ Multilevel thresholding $\cdot$ Estimation of Distribution algorithm $\cdot$ Differential mutation

## 1 Introduction

Digital Image Processing (DIP) is a set of operations that can be applied to an image to obtain useful information or generate an image with better features [1, 2]. Based on the

[^0]characteristics found in the analysis of an image, decisions can be made, and developments can be carried out that allow the industry to improve its processes [3]. Image processing segmentation is a method for extracting desired information from an image [4]. Multilevel segmentation separates an image into more than two mutually exclusive regions. Some techniques can be mentioned to segment an image [5]: thresholding [6-8], edge-based methods [9, 10], regionbased methods [11], clustering [12], and artificial neural networks, [13-15]. In image segmentation by thresholding, the primary objective is to divide an image into classes that share characteristics or are very different from the other classes. The simplicity and efficiency of segmentation by multilevel thresholding generate interest from the scientific community, which generates further exploration and progress in this branch of digital image processing [16]. In multilevel image thresholding, $n$ regions of a digital image are obtained using $n-1$ thresholds located in the histogram corresponding to the image. The operations in multilevel thresholding are based on the gray-scale histogram to obtain different classes based on some criteria.


[^0]:    Jorge Armando Ramos-Frutos, Israel Miguel-Andrés, Diego Oliva and Angel Casas-Ordaz have contributed equally to this work.

    Diego Oliva
    diego.oliva@cucei.udg.mx
    Jorge Armando Ramos-Frutos
    jramos.estudiantepicyt@ciatec.mx
    Israel Miguel-Andrés
    imiguel@ciatec.mx
    Angel Casas-Ordaz
    angel.casas5699@alumnos.udg.mx
    1 Posgrados, Centro de Innovación Aplicada en Tecnologías Competitivas, Industrial Delta, 37545 León, Guanajuato, Mexico
    2 Depto. de Ingeniería Electro-Fotónica, Universidad de Guadalajara, CUCEI, 44430 Guadalajara, Jalisco, Mexico

There are different criteria for separating an image into regions using segmentation by multilevel thresholding. One of these criteria is Otsu; this criterion maximizes the between-class variance so that the regions obtained have the greatest possible difference [17, 18]. Otsu is a useful algorithm that is applied in threshold-based image segmentation algorithms [19]. Otsu algorithm is based on two-dimensional histograms, which consider gray-scale neighbor pixel information. Thus, it has much higher segmentation precision and robustness to low-contrast images [20]. Other methods are based on the entropy in each class or specific regions from the scene. Kapur [21] proposes his method for separating gray-scale images into different classes. Kapur's entropy tries to separate images into subdivisions by maximizing the entropy of the histogram of gray-scale intensities [22]. Another entropy used is minimum cross entropy; this type of entropy is minimized [23], while the other type of entropy is maximized. The minimum cross entropy is another alternative used as a separation criterion in the images. In addition to the ones already mentioned, other criteria are based on the histogram information used to divide images into regions. This article will use Otsu to maximize the variance between classes. The Otsu and Kapur methods are simple and have a stable affection. They are used because they are widely applied in image segmentation in practice [24], and it has precision and robustness to low-contrast images.

Metaheuristic algorithms have been used among academic researchers in various fields, such as science and engineering, in solving optimization problems [25-27]. The computational inefficiency of exhaustive search makes using metaheuristics attractive for solving problems with a vast search space [28-31]. Segmentation by multilevel thresholding can be performed using metaheuristics to optimize the objective function that maximizes the observed difference between classes in the histogram. Metaheuristic finds a combination of thresholds that maximizes the variance between classes (Otsu fitness) for separating the image into multiple regions. Some widely used metaheuristics for multilevel thresholding are Genetic Algorithms (GA) [32], Particle Swarm Optimization (PSO) [33], Artificial Bee Colonies (ABC) [34], Cuckoo Search (CS) [35], Gravitational Search Algorithm (GSA) [36], Runge Kutta Algorithm (RUN) [37], Differential Evolution (DE) [38], Battle Royal Optimizer (BRO) [39], African Vultures Optimization Algorithm (AVOA) [40], among others.

Evolutionary algorithms have been applied in multilevel thresholding using different algorithms in this field of artificial intelligence. Hammouche et al. in 2008 used GA with a wavelet transform to reduce the length of the original histogram. Based on this lower-resolution histogram version, the classification problem is solved using a GA that uses a new string representation of the chromosome [32]. Wang et al. used an Estimation of Distribution

Algorithm (EDA) to solve the segmentation problem, but they only programmed it for two thresholds. This EDA has the characteristic of converging rapidly [41]. Oliva et al. proposed a Bayesian Network-based EDA for multilevel image (BNMTH). The presented algorithm allows us to find the best combination that is obtained when using different thresholding techniques, exploring the inter-dependencies between the thresholds and the thresholding techniques [42]. EDAs are a variation of genetic algorithms. The EDA replaces the mutation and crossovers operators by the sampling operation to generate new individuals [43]. Instead, DE uses the mutation and recombination operators to obtain new individuals [44]. Several mutation operators can be applied to the DE algorithm. Each of them generates different results. As with other evolutionary approaches, EDA then fails into a sub-optimal solution[45].

Differential Evolution (DE) is an essential method widely used for solving complex optimization problems [44, 46]. Some authors use DE operators to improve their algorithms. Muangkote et al. in 2017 used to improve the search success rate in a DE an adaptation of the scale factor $s F$, repair of the crossover rate, and changed the direction of a randomly selected individual to a leader based on the classification. It successfully diversifies its population with the proposed operator [47]. In 2021, Liu et al. proposed a Modified Differential Evolution (MDE) Algorithm with a Slime Mould Foraging behavior. They proved that MDE has high convergence accuracy and exploration ability [48]. A variant of differential evolution named Transformed Differential Evolution (TDE) was presented by Ramadas \& Abraham in 2020; they propose an improved mutation strategy optimized to fewer function evaluations. The thresholding outcomes were improved for the TDE approach in judgment with traditional DE [49]. Soleimanian works with a binary multiobjective dynamic algorithm Harris Hawks Optimization (HHO) enhanced with mutation operator (MODHHO). They applied this algorithm in Botnet Detection in IoT, achieving good results to solve this problem [50]. Also, Shen et al. propose a variant of the Whale Optimization Algorithm (WOA) based on multi-population evolution (MEWOA) to make the original algorithm converge fast and not fall into local optima quickly. The algorithm was tested on CEC 2019 and engineering problems, testing its competitiveness [51]. Sun et al. use a DE/EDA; they use an EDA to avoid falling into local optima and reach global optima. They compare their improvement with the EDA using some minimization problems using up to 10 dimensions. The proposed algorithm obtains better results than EDA and DE in most cases. They hybridize the EDA using a DE mutation strategy at the start of the EDA; the mutated individuals become the probability model that will be used for sampling, and replacement is generated by elitism [52].

This paper joins concepts of two evolutionary algorithms, EDA and DE, to improve and obtain global optima, and it is called DMEDA. This proposal is made because there is no dominant algorithm in all areas of knowledge as established by the No Free Lunch Theorem [53]. The classic EDA is simple and does not use parameters to calibrate, but it is trapped in the local optimum at the time of optimization. An improvement in the EDA after sampling is proposed by adding the mutation operator to diversify the results and thus not fall into the local optimum. In sampling, the EDA works with individuals chosen by the tournament; the tournament winners are those with a better objective function. Therefore, the EDA has good exploitation by the sampling operation. While the mutation strategy helps the EDA with exploration, leaving the local optima and increasing the number of points visited from the sample space. Thus, it has an algorithm that can explore and exploit the sample space that does not have many parameters to configure. Several experimental studies indicate that estimating a distribution has positive effects on the exploration of the search space [54]. It has also been shown that the potential of EDA to discover the dependencies of the problem variables can make the search more effective, as in this case, in which the thresholds are dependent [55]. In recent years, this algorithm has achieved great success in combinatorial and continuous problems [56-58], generating attraction to use it to optimize complex objective functions. The research aims to solve the image segmentation problem optimizing the Otsu or Kapur objective functions using an EDA improved with a Differential Mutation Operator (DM) with the ability to obtain global optima in the search space of the Otsu and Kapur, independently. The main contributions of this paper are:

- The improvement that is generated in the EDA using the Differential Mutation Operator for the mutation after sampling to explore the search space better.
- The ability to get out of local optima when using the Differential Mutation operator in the EDA.
- It has been proved the proposed DMEDA solves the multilevel thresholding problem using two objective functions, Otsu and Kapur.
- A hybridization approach to EDA and not focusing on improving the probabilistic model used in the sampling phase.

The current article is divided into the following parts: Sect. 2 describes the problem and the concepts of the EDA and the DM. Section 3 shows the proposal to improve the EDA and the image thresholding problem. Section 4 describes the experimentation, its metrics, the images used to compare the algorithms, and experimental results and comparisons, including statistical and non-parametric tests, to generate
confidence in the research results. Finally, Sect. 5 discusses some conclusions and future works.

## 2 Background

Machine vision is a scientific discipline that consists of image acquisition, image preprocessing, image segmentation, feature extraction, and analysis [59]. Segmentation is used to obtain the interest regions of an image. Then, the interest regions of the image are obtained and analyzed with algorithms to extract features [28].

### 2.1 Problem definition

The segmentation problem consists of classifying the pixels of an image into a set of classes [60]. There are several techniques to segment an image; one of them is multilevel thresholding. Multilevel thresholding segmentation will find more than one region in an image [61]. Each threshold is a histogram value that separates the image in different regions. These regions may contain pixels that correspond to an object of interest, and using image segmentation with some other digital image processing operations, those regions can be extracted for analysis. Multilevel thresholding can be performed in one dimension, as in the case of gray-scale segmentation, or more than one dimension, as in the case of segmenting images on a color scale, such as RGB color space. To solve the gray-scale problem, it is possible to use Eq. 1 that defines the set of classes into which an image will be separated, taking into account the thresholds obtained from the histogram that represents the image.

$$
\begin{aligned}
& C_{0}=\left\{I_{i j} \in I(x, y) \mid 0 \leq I_{i j} \leq t h_{1}-1\right\} \\
& C_{1}=\left\{I_{i j} \in I(x, y) \mid t h_{1} \leq I_{i j} \leq t h_{2}-1\right\} \\
& \quad \vdots \\
& C_{k}=\left\{I_{i j} \in I(x, y) \mid t h_{k} \leq I_{i j} \leq t h_{L-1}\right\}
\end{aligned}
$$

From Eq. 1, $t h_{i}$ is the $i$ th threshold, $I(x, y)$ is the original image, $t h_{k}$ is the $k$ th threshold, $C_{k}$ is the $k$ th class or region of the segmented image, and $L$ is the maximum level in the gray-scale. The number of classes depends on the number of interested regions to detect in the image. It could be variable for each study case.

### 2.2 Otsu's between-class variance

The Otsu method is used as a fitness function. The discriminant criterion selects an optimal threshold to maximize the separability of the resultant classes in gray levels using the inter-class variance computed with the frequency histogram [17]. In the Otsu method, the bins displayed in a histogram show the number of pixels that are at an

intensity level $i$ th on the gray-scale for the case of image segmentation on this scale. A histogram is a visual tool that helps choose the thresholds and calculate the variances needed to maximize the Otsu objective function. The probability distribution is computed in Eq. 2.
$p_{i}=\frac{n_{i}}{N}$
where:
$p_{i} \geq 0$
$\sum_{i=1}^{L} p_{i}=1$
where $n_{i}$ is the number of pixels inside of each class from 0 to $255, p_{i}$ is the probability of obtaining each intensity level in the frequency histogram, the number of the class is $k$, and it is necessary to obtain the thresholds. Each class denotes pixels into each threshold. Then, the probabilities of class occurrence and the class mean levels, respectively, are given by Eq. 3.
$\omega_{0}=P\left(C_{0}\right)=\sum_{i=1}^{i h_{1}-1} p_{i}$
$\omega_{1}=P\left(C_{1}\right)=\sum_{i=0}^{i h_{2}-1} p_{i}$
$\omega_{k}=P\left(C_{k}\right)=\sum_{i=0_{k}}^{L-1} p_{i}$
The probability to obtain a pixel in the $k$ th class is $\omega_{k}$. The mean of each class is denoted by Eq. 4.
$\mu_{0}=\sum_{i=0}^{i h_{1}-1} i P\left(i \mid C_{0}\right)=\frac{1}{\omega_{0}} \sum_{i=1}^{i h_{1}-1} i p_{i}$
$\mu_{1}=\sum_{i=0}^{i h_{1}-1} i P\left(i \mid C_{1}\right)=\frac{1}{\omega_{1}} \sum_{i=0}^{i h_{1}-1} i p_{i}$
$\mu_{k}=\sum_{i=0_{k}}^{L-1} i P\left(i \mid C_{k}\right)=\frac{1}{\omega_{k}} \sum_{i=0_{k}}^{L-1} i p_{i}$
The class variances are given by Eq. 5.
$\sigma_{0}^{2}=\sum_{i=0}^{i h_{1}-1}\left(i-\mu_{0}\right)^{2} P\left(i \mid C_{0}\right)=\frac{1}{\omega_{0}} \sum_{i=1}^{i h_{1}-1}\left(i-\mu_{0}\right)^{2} p_{i}$
$\sigma_{1}^{2}=\sum_{i=0}^{i h_{1}-1}\left(i-\mu_{0}\right)^{2} P\left(i \mid C_{1}\right)=\frac{1}{\omega_{2}} \sum_{i=0}^{i h_{2}-1}\left(i-\mu_{1}\right)^{2} p_{i}$
$\sigma_{k}^{2}=\sum_{i=0_{k}}^{L-1}\left(i-\mu_{0}\right)^{2} P\left(i \mid C_{k}\right)=\frac{1}{\omega_{k}} \sum_{i=0_{k}}^{L-1}\left(i-\mu_{k}\right)^{2} p_{i}$
Therefore, with the equations shown previously, it is possible to calculate the between-class variance with Eq. 6
$F_{\text {Otsu }}=\sum_{i=C_{0}}^{C_{1}} \sigma_{i}$
Here $\sigma_{i}$ is the variance corresponding to the $i$ th class. Then, the problem is reduced to an optimization problem to search for a threshold $k$ that maximizes the objective function Otsu given by the Eq. 7.
$t h_{1}^{*}, t h_{2}^{*}, \ldots, t h_{k}^{*}=\max _{i h_{1}^{*}, t h_{2}^{*}, \ldots, t h_{k}} F_{\text {Otsu }}\left(t h_{1}^{*}, t h_{2}^{*}, \cdots, t h_{k}^{*}\right)$
Where $t h_{1}^{*}, t h_{2}^{*}, \ldots, t h_{k}^{*}$ is the vector of thresholds that maximize Otsu fitness shown in Eq. 6.

### 2.3 Kapur's entropy

The Kapur's entropy is another popular criterion for obtaining thresholds [21]. The method finds the thresholds ( $t h$ ) that maximize the entropy, as shown in Eq. 8.
$t h_{1}^{*}, t h_{2}^{*}, \ldots, t h_{k}^{*}=\max _{i h_{1}^{*}, t h_{2}^{*}, \ldots, t h_{k}} F_{\text {Kapur }}\left(t h_{1}^{*}, t h_{2}^{*}, \ldots, t h_{k}^{*}\right)$
$t h_{1}^{*}, t h_{2}^{*}, \ldots, t h_{k}^{*}$ is the vector of thresholds that maximize Kapur fitness, and the objective function is constituted by the Eq. 9, which is the sum of a set of entropies.
$F_{\text {Kapur }}=\sum_{i=C_{0}}^{C_{1}} H_{i}$
From Eq. 9 each entropy is obtained with its respective threshold, for which Eq. 10, which allows it to be calculated.
$H_{0}=\sum_{i=0}^{i h_{1}-1} \frac{p_{i}}{\omega_{0}} \ln \left(\frac{p_{i}}{\omega_{0}}\right)$
$H_{1}=\sum_{i=0}^{i h_{1}-1} \frac{p_{i}}{\omega_{1}} \ln \left(\frac{p_{i}}{\omega_{1}}\right)$
$H_{k}=\sum_{i=0_{k}}^{L-1} \frac{p_{i}}{\omega_{k}} \ln \left(\frac{p_{i}}{\omega_{k}}\right)$
Here the probability occurrence $\omega_{i}$ of the $i$ th class are obtained with Eq. 3 and the probability distribution using Eq. 2.

### 2.4 Estimation of distribution algorithm

Estimation of Distribution Algorithm (EDA) was introduced by [62] in the area of evolutionary computation. EDA takes into account interacting variables to generate new populations. That approach is different from GA, which uses two operators: crossover and mutation. The EDA begins with a selection process on the initial population, just like the GA. The vectors that are selected from the initial population are analyzed to obtain a probability model that will be used to sample and generate new offspring [63, 64]. The EDA in each iteration improves its results by the sampling process, learning from the distributions that are generated and getting the optimal new individual. This case is used to solve a Multilevel Thresholding Problem. The operations carried out by the EDA are described in the following subsections (initial population generation, selection, sampling, and replacement) to optimize the objective function.

### 2.4.1 Generate initial population

The first step begins with the generation of the first population. The first population is generated randomly [41]. Each individual has a sorted discrete combination vector (th) defined as $\mathbf{t h} \in \mathbb{R}^{m} \mid 0 \leq t h_{i} \leq 255, i=1,2, \ldots, t n$. The value of $t n$ depends on the quantity of classes that want to be identified. Equation 11 is used to obtain each threshold to generate the initial population.
$t h_{i j}=L_{j}+\operatorname{rand}_{j} \times\left(U_{j}-L_{j}\right)$
Where $L_{j}$ and $U_{j}$ represent the lower and upper boundary of $t h_{i}$ in the $j$ th dimension, respectively. The $r a n d_{i} \in[0,1]$ is random number [65]. A set of $P_{i}$ conforms to the initial population. The initial population is described in the Eq. 12:
$\widetilde{P}_{i}^{[0]}=\left\{t h_{i 1}, t h_{i 2}, \ldots, t h_{i L-1}\right\}$
where $\widetilde{P}_{i}^{[0]}$ is the sorted discrete solution vector that corresponds to $i$ th inhabitant, and a superscript is placed to denote that it is the initial population. After generating the initial population, it is necessary to evaluate the fitness function to pass at the next operator.

### 2.4.2 Select operator

The select operator chooses the vectors with the conditions to be parents. A selection by the tournament is used in which two vectors compete, and the one with a higher value of the objective function (Otsu or Kapur) goes to the mating pool. Using a selection operator has less chance of convergence, making it the best choice for working in a large workspace [66].

### 2.4.3 Sampling

All selected parents must be sampled in this phase to generate new children. $t h_{i j}$ represents a random variable. Here, we use discrete variables $t h_{i j}$, and the mass probability for the variable is $p_{k}\left(t h_{i j}\right)$ [63]. For the probabilistic model, we use a Gaussian model in Eq. 13 to generate new children.
$p_{k}\left(t h_{i j}\right)=\prod_{i=1}^{k} N\left(t h_{i j} \mid \mu_{j}^{k}, \sigma_{j}^{k}\right)$
From Eq. 13, $N\left(t h_{i j} \mid \mu_{j}^{k}, \sigma_{j}^{k}\right)$ is defined by the Eq. 14.
$N\left(t h_{i j} \mid \mu_{j}^{k}, \sigma_{j}^{k}\right)=\frac{1}{\sqrt{2 \pi \sigma_{j}}} e^{\frac{\left(t h_{i j}-\mu_{j}\right)^{2}}{2 \sigma_{j}^{2}}}$
Where $t h_{i j}$ is the $j$ th threshold in the position $i$ th, $\mu_{j}^{k}$ is the average of the thresholds in the $j$ th level in the $k$ th iteration,
and $\sigma_{j}^{k}$ is the standard deviation of the thresholds in the $j$ th level in the $k$ th iteration.

The parameters used in the normal distribution are calculated using the corresponding statistics for each thresholding level. To calculate $\mu_{j}^{k}$ the Eq. 15 is used.
$\mu_{j}^{k}=\frac{1}{P} \sum_{i=1}^{P} t h_{i j}$
Where $\sigma_{j}^{k}$ is computed using Eq. 16.
$\sigma_{j}^{k}=\frac{1}{P-1} \sum_{i=1}^{P}\left(t h_{i j}-\mu_{j}^{k}\right)^{2}$
From Eq. 16, $P$ is the population size of the selected children. This sampling method ensures that new individuals converge when a local optimum is found. $99.7 \%$ of each threshold generated will be at $\mu_{j}^{k} \pm 3 \sigma_{j}^{k}$. As the number of iterations increases, the mean stabilizes, and the standard deviation is smaller because the populations tend to be similar. Therefore, the EDA is weak in finding global optima because it can get stuck in a local optimum.

### 2.4.4 Replacement

The replacement is generated by comparing the generation $k-1$ th with the generation that was generated in the current iteration $k$. Only children that improve parental fitness can be placed in generation $k$. With this replacement strategy, the quality of the populations is maintained because the optimums found by the EDA are exploited. The pseudocode used in the EDA is shown in the Algorithm 1.

```
Algorithm 1 Estimation of Distribution Algorithm (EDA)
Require: Gray-scale Image, Number of Thresholds, Population
Ensure: Thresholds, Segmented Image
for \(i=1: n\) do
    Generate Population
        Evaluate Population with Otsu
        Selection by tournament
        Sampling
    end for
    return thresholds and segmented image
```


### 2.5 Differential mutation operator

The Differential Mutation (DM) strategy is used after the sampling process in the EDA. The DM operator used in this article is taken from the Differential Evolution, and it is known as mutation DE/current-to-best/1 [67]. In DE, the mutation generates a mutant vector for each solution of the current population and it is called that because it is based

on the differences of individuals in the population or a set of vectors; this allows information to be transmitted between them [68]. The main benefit of using DM is that diversity in the population is maintained on a certain level [67]. The EDA is based on the mean of the set of individuals used, and there is a high probability of generating individuals close to the mean. Furthermore, the difference between the best and each individual converges to the global optimum. The DM used in the proposed approach is defined in Eq. 17.
$\widehat{m}_{i}=\widehat{\left|h_{i}+s F \times\left(\widehat{h}_{\text {best }}-\widehat{i h}_{i}+\widehat{i h}_{r 1}-\widehat{i h}_{r 2}\right)\right.}$
Here $\widehat{m}_{i}$ is the mutation as a candidate solution, $s F$ is the scaling factor and is the parameter of this mutation strategy that controls the magnitude in which the population will evolve, $\mathbf{t h}_{i}$ is the vector of thresholds located at the $i$ th position, $\mathbf{t h}_{\text {best }}$ is the threshold vector with the best fitness, $\mathbf{t h}_{r_{1}}$ and $\mathbf{t h}_{r_{2}}$ are two random thresholds vectors. With the use of this operator, the diversity is maintained, which is good because it allows exploration at the beginning of the process and exploitation at the end of the process. Here $\widehat{m}_{i}$ is the
mutation as a candidate solution, $s F$ is the scaling factor and is the parameter of this mutation strategy that controls the magnitude in which the population will evolve, $\mathbf{t h}_{i}$ is the vector of thresholds located at the $i$ th position, $\mathbf{t h}_{\text {best }}$ is the threshold vector with the best fitness, $\mathbf{t h}_{r_{1}}$ and $\mathbf{t h}_{r_{2}}$ are two random thresholds vectors.

## 3 Differential mutation estimation of distribution algorithm

This section describes how the EDA works with the Differential Mutation (DM) operator. This algorithm is named Differential Mutation Estimation of Distribution Algorithm (DMEDA). Figure 1 shows the improvement proposal to the EDA. Using the mutation strategy increases the capacity of the EDA to get out of the local optimum and increase the exploration capacity.

The pseudocode is collocated in the Algorithm 2. It can be seen that Eq. 17 is located after the sampling operation and before the replacement operation.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Flowchart of the proposed DMEDA

```
Algorithm 2 Differential Mutation Estimation of Distribution Algorithm (DMEDA)
Require: Gray-scale Image, Number of Thresholds, Population, of
Ensure: Thresholds, Segmented Image
for \(i=1: n\) do
    Generate Population
    Evaluate Population with Otsu
    Selection by tournament
    Sampling Eq. 13
    Differential Mutation (Improvement Eq. 17)
    replacement for elitism
end for
return thresholds and segmented image
```


### 3.1 Implementation of the DMEDA for image thresholding

To make the implementation of DMEDA easier to understand, Fig 2. Shows a flow chart of how the algorithm solves the maximization problem to obtain the thresholds that segment the image. It begins by reading the gray-scale image, and then the histogram of the read image is calculated. A population of vectors $\left(\mathbf{X}=\left[\mathbf{T h}_{1}, \mathbf{T h}_{2}, \ldots, \mathbf{T h}_{N}\right]\right)$ containing the thresholds ( $\mathbf{T h}_{i}=\left[t h_{1}, t h_{2}, \ldots, t h_{k}\right]^{T}$ ) that meet the constraints; thresholds are subject to $t h_{1}<t h_{2}<\cdots<t h_{k}<L$ where $L=255$, is generated. The objective functions are maximized; in this article, there are two: Otsu and Kapur. Finally, the set of thresholds that will output the segmented image is obtained.

The number of thresholds or regions into which the image is divided is placed manually; the greater the number of regions, the details in the segmented images are perceptible with greater precision.

## 4 Experiments and results

This section presents the experiments and results obtained using the proposed DMEDA in the multilevel thresholding problem. The experimental conditions, the metrics used to evaluate the algorithm's performance from another
perspective, and the results obtained with the algorithm in comparison with other metaheuristics are presented.

### 4.1 Experimental setup

The experiments were carried out using the Matlab programming language. A computer with a 64-bit Windows 11 operating system, Intel Core i7-1165G7 processor, and 12 GB of RAM was used. All algorithms were implemented using the Berkeley Segmentation Data Set 300 (BSDS300) [69]. The algorithms used to compare the DMEDA are: Cuckoo Search Algorithm (CS) [35], Gravitational Search Algorithm (GSA) [36], Jellyfish Search Optimizer (JF) [70], Artificial Hummingbird Algorithm (AHA) [71], Osprey Optimization Algorithm (OOA) [72], Salp Swarm Algorithm (SSA) [73], Sine Cosine Algorithm (SCA) [74], and Estimation of Distributions (EDA) [43]. Table 1 describes the configuration of each algorithm's internal parameters. Notice that the values of such parameters were originally taken from the article. In the case of the EDA and DMEDA, the parameters were set based on the values commonly used in the related literature [45, 75].

All the algorithms use a maximum number of iterations set to 500 as a stop criterion. According to the related literature, the experiments were conducted using 2, 3, 4, and

Table 1 Algorithms parameter settings

| Algorithm | Parameters |
| :-- | :-- |
| DMEDA | $\mathrm{N}=100$, iters $=500$, scaling_factor $=0.2$ |
| EDA | $\mathrm{N}=100$, iters $=500$ |
| CS | $\mathrm{N}=100$, iters $=500$, ap $=0.25$, n_nest $=25$ |
| GSA | $\mathrm{N}=100$, iters $=500$, boundary_points $=[-\mathrm{pi}, \mathrm{pi}]$ |
| JF | $\mathrm{N}=100$, iters $=500$ |
| SCA | $\mathrm{N}=100$, iters $=500, \mathrm{a}=2$ |
| AHA | $\mathrm{N}=100$, iters $=500$ |
| OOA | $\mathrm{N}=100$, iters $=500$ |
| SSA | $\mathrm{N}=100$, iters $=500, \mathrm{st}=0.8$ |

Fig. 2 Flowchart of the implementation of DMEDA for image thresholding
![img-1.jpeg](img-1.jpeg)

5 thresholds [5, 76-79]. Finally, for statistical purposes, 30 independent experiments were performed by the algorithm over each image using a specific number of thresholds. The experiments are divided into three groups; in the first group, the DMEDA is tested and compared using Otsu's betweenclass variance as an objective function; in the second group, Kapur's is used as a criterion for image segmentation. Notice that the ten most representative images were chosen from the BSD300 for the first and second groups based on a classification within the same dataset described as the most complex to segment [69]. This is because such images help to graphically show the performance of the algorithms. The selected images with their histograms are presented in Fig. 3. In this sense, in the third group of experiments, the DMEDA is compared with the other optimization methodologies using all the images in the BSD300 dataset with both thresholding criteria, Otsu and Kapur. It is important to mention that different metrics are used to compare the performance of the optimization algorithms in terms of image segmentation (see Subsection 4.2). Also, statistical analysis and non-parametric tests complement the experimental study.

The evaluation of the metaheuristics is carried out using the mean and the standard deviation because all of them have stochastic behavior. Therefore, the results obtained in each replicate have variations, and it is necessary to measure how dispersed (stability) the results are and where they are located (accuracy) using these two statistics. When a metaheuristic is stable, the standard deviation tends to be zero because the results acquired from a set of individuals over the iterations tend to be the same. The precision of the metaheuristics can be observed by measuring the mean of the set of results obtained by the populations at the step of the iterations.

### 4.2 Metrics used for image segmentation

Image segmentation quality can be measured in seven ways [80-82]: Peak Signal to Noise Ratio (PSNR), Structure Similarity Index Measure (SSIM), Featured Similarity Index Measured (FSIM), Quality Index based on Local Variance (QILV), Haar wavelet-based Perceptual Similarity Index (HPSI), and Universal Image Quality Index (UIQI). The PSNR can be obtained with Eq. 18.
$P S N R=20 \log \left(\frac{255}{\text { RMSE }}\right)$
Where RMSE is the Root Mean Square Error calculated by Eq. 19
$R M S E=\sqrt{\frac{1}{M N} \sum_{i=1}^{M} \sum_{j=1}^{N}(I(i, j)-S(i, j))^{2}}$
$M, N$ are the size of image, $I(i, j)$ is the unsegmented image and $S(i, j)$ is the segmented image with a given thresholding level. When the PSNR is higher, the segmentation quality is lower because there is less difference between the original and processed images. The SSIM is calculated by Eq. 20:
$S S I M=\frac{\left(2 \mu_{I} \mu_{S}+c_{1}\right)\left(2 \sigma_{I S}+c_{2}\right)}{\left(\mu_{I}^{2}+\mu_{S}^{2}+c_{1}\right)\left(\sigma_{I}^{2}+\sigma_{S}^{2}+c_{2}\right)}$
where $I$ and $S$ designate the original and segmented images, respectively. $\mu_{I}$ and $\mu_{S}$ are the mean values of original and segmented images, respectively. $\sigma_{I}^{2}$ and $\sigma_{S}^{2}$ are the variances, $\sigma_{I S}$ the covariance. The constants $c_{1}=(0.01 \times 255)^{2}$ and $c_{2}=(0.03 \times 255)^{2}$ are employed in order to stabilize the division with weak denominator [83]. A SSIM near one indicates better results in segmentation.

Another metric is the Featured Similarity Index (FSIM). FSIM evaluates the importance of the local structure between the non-segmented image and segmented image [84]. The maximum FSIM value that can be attended is 1 . Equation 21 introduces the FSIM.
$F S I M=\frac{\sum_{I \in \Omega} S_{L}(I) P C_{m}(I)}{\sum_{I \in \Omega} P C_{m}(I)}$
where $\Omega$ represents the entire domain of the image, $S_{L}(I)$ is the product of the similarity measure of the Gradient Magnitude map and Phase Congruency map and is calculated with Eq. 22.
$S_{L}(I)=S_{P C(I)} S_{G(I)}$
In this Eq. $S_{P C(I)}$ and $S_{G(I)}$ are calculated with the next Eqs.
$S_{P C(I)}=\frac{2 P C_{1(I)} 2 P C_{2(I)}+T_{1}}{P C_{1(I)}^{2} P C_{2(I)}^{2}+T_{1}}$
To calculate $P C$ is necessary the Eq. 24.
$P C(I)=\frac{E(I)}{\varepsilon+\sum_{n} A_{n}(I)}$
where $A_{n}(I)$ is the local amplitude on scale $n$, and $E(I)$ is the magnitude of the response vector in $I$ over $n, \varepsilon$ is a small positive number. To continue with the description of Eq. 22, we define $S_{G(I)}$ as:
$S_{G(I)}=\frac{2 G_{1(I)} G_{2(I)}+T_{2}}{G_{1(I)}^{2} G_{2(I)}^{2}+T_{2}}$
Here $T_{1}$ and $T_{2}$ are constants with values 0.85 and 160 , respectively. $G$ is the magnitude of the gradient of a digital image and is calculated by Eq. 26.

![img-18.jpeg](img-18.jpeg)
(a) 12003 .
![img-19.jpeg](img-19.jpeg)
(d) 12003 histogram.
![img-18.jpeg](img-18.jpeg)
(g) 66075 .
![img-19.jpeg](img-19.jpeg)
(j) 66075 histogram.
![img-18.jpeg](img-18.jpeg)
(m) 108070.
![img-19.jpeg](img-19.jpeg)
(p) 108070 histogram.
![img-18.jpeg](img-18.jpeg)
(b) 37073 .
![img-19.jpeg](img-19.jpeg)
(e) 37073 histogram.
![img-18.jpeg](img-18.jpeg)
(h) 101087 .
![img-19.jpeg](img-19.jpeg)
(k) 101087 histogram.
![img-18.jpeg](img-18.jpeg)
(n) 160068 .
![img-19.jpeg](img-19.jpeg)
(q) 160068 histogram.
![img-18.jpeg](img-18.jpeg)
(c) 56028 .
![img-19.jpeg](img-19.jpeg)
(f) 56028 histogram.
![img-18.jpeg](img-18.jpeg)
(i) 210088 .
![img-19.jpeg](img-19.jpeg)
(l) 210088 histogram.
![img-18.jpeg](img-18.jpeg)
(o) 296059 .
![img-19.jpeg](img-19.jpeg)
(r) 296059 histogram.

Fig. 3 Selected images from the BSD300 and their histograms

$G=\sqrt{G_{x}^{2}+G_{y}^{2}}$
$G_{x}$ is the gradient in the $x$ direction and $G y$ is the gradient in the $y$ direction. To complete the description of Eq. $21 P C_{m}(I)$ is the maximum of the Phase Congruency map between segmented and non-segmented images.
$P C_{m}(I)=\max \left(P C_{1}(I), P C_{2}(I)\right.$
Metric QILV focuses on the image structure to appraise the changes in the non-stationarity behavior of images [85] and is computed by the Eq. 28.
$Q I L V=\frac{2 \mu_{V_{i}} \mu_{V_{x}}}{\mu_{V_{i}}^{2}+\mu_{V_{x}}^{2}} \cdot \frac{2 \sigma_{V_{i}} \sigma_{V_{x}}}{\sigma_{V_{i}}^{2}+\sigma_{V_{x}}^{2}} \cdot \frac{\sigma_{V_{i} V_{x}}}{\sigma_{V_{i}} \sigma_{V_{x}}}$
This Equation is constituted by the local variance of the image; the local variance is obtained with the Eq. 29.
$\operatorname{Var}(I(i, j))=\frac{\sum_{p \in \eta_{i j}} \omega_{p}\left(I_{p}-\bar{I}(i, j)\right)^{2}}{\sum_{p \in \eta_{i j}} \omega_{p}}$
Here $\eta_{i, j}$ is a neighborhood with defined size, $\omega_{p}$ are the weights with a Gaussian distribution given to the pixels under analysis $p$, and $\bar{I}(i, j)$ is the mean of the local variance computed by Eq. 30.
$\bar{I}(i, j)=\frac{\sum_{p \in \eta_{i j}} \omega_{p} I_{p}}{\sum_{p \in \eta_{i j}} \omega_{p}}$
The remaining variables (variables) of Eq. 28 can be estimated with Eqs. 31, 32, 33, respectively.
$\mu_{V_{i}}=\frac{1}{M N} \sum_{i=1}^{M} \sum_{j=1}^{N} \operatorname{Var}(I(i, j))$
$\sigma_{V_{i}}=\left(\frac{1}{M N} \sum_{i=1}^{M} \sum_{j=1}^{N}\left(\operatorname{Var}(I(i, j))-\mu_{V_{i}}\right)^{2}\right)^{1 / 2}$
And
$\sigma_{V_{i} V_{x}}=\frac{1}{M N-1} \sum_{i=1}^{M} \sum_{j=1}^{N}\left(\operatorname{Var}(I(i, j))-\mu_{V_{i}}\right)\left(\operatorname{Var}(S(i, j))-\mu_{V_{x}}\right)$
this can be extrapolated for the segmented image, and QILV can be calculated.

HPSI evaluates the perceptual similarity between a reference image and a segmented image [86].
$H P S I=l_{a}^{-1}\left(\frac{\sum_{x} \sum_{k=1}^{2} H S_{I, S}^{(k)}[x] \cdot W_{I, S}^{(k)}[x]}{\sum_{x} \sum_{k=1}^{2} W_{I, S}^{(k)}[x]}\right)$
The function $l_{a}^{-1}(\cdot)$ maps the weighted average from the interval $\left[1 / 2, I_{a}(1)\right]$. The local similarity measure $H S$ is based on the discrete Haar wavelet transform Eq. 35.
$H S_{I, S}^{(k)}[x]=l_{a}$
Here $I_{a}$ is given by
$l_{a}=\frac{1}{1+e^{-a x}}$
the parameter $a>0$, and $W_{I, S}^{(k)}[x]$ is obtained with
$W_{I, S}^{(k)}[x]=\max \left(W_{I}^{(k)}[x], W_{S}^{(k)}[x]\right)$
where $W_{I}^{(k)}[x]$ and $W_{S}^{(k)}[x]$ are a single low-frequency Haar wavelet filter for the original and the segmented images, respectively.

And UIQI measures image distortion as a combination of correlation loss, luminance distortion, and contrast distortion [87] is calculated using Eq. 38.
$U I Q I=\frac{4 \sigma_{x, y} \bar{x} \bar{y}}{\left(\sigma_{x}^{2}+\sigma_{y}^{2}\right)\left(\bar{x}^{2}+\bar{y}^{2}\right)}$
Where
$\bar{x}=\frac{1}{N} \sum_{i=1}^{N} x_{i}$
$\bar{y}=\frac{1}{N} \sum_{i=1}^{N} y_{i}$
are the means, and
$\sigma_{x}^{2}=\frac{1}{N-1} \sum_{i=1}^{N}\left(x_{i}-\bar{x}\right)^{2}$
$\sigma_{y}^{2}=\frac{1}{N-1} \sum_{i=1}^{N}\left(y_{i}-\bar{y}\right)^{2}$
are the standard deviations, and
$\sigma_{x, y}=\frac{1}{N-1} \sum_{i=1}^{N}\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right)$
is the covariance of the original and the segmented image signals, respectively. This metric is in the range $[-1,1]$.

### 4.3 Otsu test with benchmark images discussion

For research, the most important thing is to obtain an improvement concerning the objective function. This aims to verify that the DMEDA is proposed to obtain better results in the Otsu objective function than the EDA. Table 2 shows the mean and standard deviation (std) fitness obtained by each algorithm in the ten images and in each threshold (running the algorithm thirty times in each case). Only in one case does the DMEDA not obtain the best average compared to the other eight algorithms ( $97.5 \%$ ).

Table 3 shows the best results obtained for each thresholding level in each image with each algorithm. A certain similarity is observed between the algorithms that obtain the best results in maximizing the objective function. Table 4 shows the mean and standard deviation (std) of the PSNR obtained by the nine algorithms presented in this research, including the proposed DMEDA. For the PSNR the EDA obtains first place. The EDA obtains the best PSNR average in $55 \%$ of the cases, the OOA in $25 \%$ of the cases, the SCA in $15 \%$ of the cases, and the JF in only $5 \%$ of the cases. These algorithms do not obtain the best results by optimizing the objective function, but the structure of the region obtained is similar to the original image.

On the other hand, Table 5 presents the mean and standard deviation for the SSIM. To this indicator, the EDA generates better results in $82.5 \%$ of the cases (behaves better at high threshold levels), the OOA and the SSA are better in two cases, the AHA, the JF and the SCA only in one case are better. It is desired that the standard deviation of the algorithms be much smaller because this metric indicates the ability of an algorithm to be consistent with its results each time it is run. The DMEDA is better when comparing its standard deviation in these two metrics.

Table 6, the results for the FSIM metric are obtained. In this table, the OOA is better in most cases because it has a higher value. Although it has a low standard deviation, it is no better than the standard deviation of the DMEDA. This corroborates that the proposed mutation operator into the EDA balances the exploration and exploitation of the algorithm, making it find a global optimum in a smaller number of iterations. According to the information shown, it is concluded that the DMEDA has better results optimizing the Otsu fitness function. In metrics such as PSNR, SSIM, and FSIM, leadership is not obtained due to the nature of the problem being solved. Although the segmented regions obtained with the DMEDA maximize the variance between the pixel classes of the ten images, they generate a more significant difference between the original image and the region chosen to generate the aforementioned metrics.

In Table 7 JF is the algorithm with the best results, compared to the others in most cases, SCA and OOA are
algorithms that also win but to a lesser extent. For Table 8 that represents the HPSI metric, JF remains the algorithm with the most won cases, while OOA takes second place. In Table 9 of the metric UIQI, it is observed that no algorithm is conclusive, but the DMEDA does not obtain the best results in most of the metrics. Although it remains close to the best and optimizes the objective function better than the other algorithms, it fails to outperform in these aspects.

Figure 4 show the convergence curves of the objective function (Otsu's between-class variance) of the algorithms used to solve the multilevel thresholding problem. There is a clear difference between the proposed algorithm and the EDA in the four cases observed; this does not vary when the thresholding level is changed. Also, it is observed how the algorithm converges to the highest point compared to the other algorithms; in some cases, such as SCA, this algorithm does not converge. Although the SCA does not converge, it can be seen in some metrics how it wins in some cases. In another case, as in the AHA, it can be seen that there is a result that is much lower in the curves shown.

Figures 5, 6, 7, and 8 show the thresholds at which the DMEDA maximizes the objective function. Three images are shown in Fig. 5, namely, 12,003, 37,073, and 56,028, with the four thresholding levels, the respective frequency histograms, and the processed images. The images are thresholded using the Otsu criterion, and groups of pixels are generated in regions with maximum inter-class variance. Each region that is obtained by the algorithm takes on a different shade of gray. Thresholded images take on a shade of gray according to the regions or thresholds that you define. If there are three thresholds, the thresholded image will take four shades of gray to represent the pixel classes. Figure 6 shows three other images (108,070, 160,068, and 296,059) segmented using four thresholding levels. All three segmented images contain animals. Image 108,070 shows a tiger covered by the shadows of some object, and the pixels corresponding to the tiger have two different intensities; the thresholding results using DMEDA are better by increasing the thresholds. The thresholded images with a larger number of thresholds show the pixel regions; it is possible to locate the tiger's body in these regions. A similar problem occurs in image 160,068 because the cat shown in that image has similar colors to the trunk on which it rests. It is possible to distinguish the regions more clearly by increasing the thresholds. The third image shows two elephants, one of which obstructs the correct identification of the other. Still, the regions shown in the segmented image successfully identify the pixels corresponding to the animals. In the Figs. 5 and 6 some images have a rectangular shape in which the width $(i)$ is greater than the length $(j)$.

Figures 7, and 8 have thresholded images with a different shape than the first two already described. Figure 7 shows

![img-20.jpeg](img-20.jpeg)

two images using from 3 to 6 regions. Image 66,075 is an animal that is not obstructed by any object, and its segmentation should be simple; from a low level of thresholding, the region belonging to the bird in the image is not lost. In image 101,087, a person is drawn on a raft, and by thresholding it into three regions, it is possible to identify the sky of the other regions. Increasing the number of regions presents a greater amount of detail with similar intensities. In this way, it is possible to distinguish the pixels corresponding to the sky and those corresponding to other regions of interest.

Figure 8 also contains two images. These images are more complex because you have an animal whose vision is obstructed by a plant and a person dressed in clothing with similar tones as the image's background. In these two images, the good work of the multilevel thresholding method can also be observed, finding regions corresponding to the person's clothing and the background. Post-processing tasks are facilitated by having a greater number of regions and ensuring that these regions contain the object of interest. Furthermore, by increasing the number of regions, it is possible to detect a greater amount of detail in the man's face and clothing.

### 4.4 Kapur test with benchmark images discussion

As already mentioned, the goal is to obtain an algorithm for optimizing the objective function (in this case, Kapur's entropy) with better results. This subsection presents the results obtained with DMEDA using Kapur's entropy. As with Otsu, DMEDA obtains good results in maximizing the Kapur objective function, as shown in Table 10. In $85 \%$ of the total cases, DMEDA is superior to the other algorithms. For the remaining $15 \%$, the OOA is the winner. In this objective function, it wins a smaller number of times with the ten images used to construct the results of this Section.

The thresholds shown in Table 11 differ from those obtained with Otsu. For this reason, the result in the metrics is different. However, DMEDA performs better when Kapur's criterion is used to segment the images. By changing the positions of the thresholds, the perception of the images changes, and the results shown in Figs. 10, 11, 12, and 13 .

Table 12 shows the mean and standard deviation of the PSNR in which DMEDA is better for high thresholding levels in most cases. The other algorithm with good results is SSA, but as will be seen later in the convergence curves, this algorithm does not converge. Therefore, consistent results on the objective function and the metric are not expected. In $35 \%$ of the cases, the DMEDA is the one that expires; another $35 \%$ is distributed in the SSA, and the remaining $30 \%$ is divided into the OOA, AHA, CS, GSA, and JF. This shows how there is no conclusive algorithm for this metric.

For the SSIM at almost $50 \%$ of the thresholding levels for each image, the DMEDA is the best. And secondly, the SSA is maintained with $40 \%$ of the victories. CS and SCA algorithms won twice each. OOA and GSA won only once each. Table 13 shows how DMEDA continues to win in the high dimensions for this metric. Unlike the SSIM results obtained in Otsu, DMEDA performs better for Kapur.

In $52.5 \%$ of the cases of the FSIM shown in Table 14, the DMEDA obtains better results than the other algorithms, in six cases ( $15 \%$ ), the OOA is victorious, and in five of them the SSA. In less than three cases, the algorithms with good results were JF, CS, GSA, and AHA, tying JF and AHA with three moments and CS with GSA in one case.

QILV metric presented in Table 15 shows that the DMEDA wins eleven times ( $27.5 \%$ ). In this metric, OOA beats DMEDA on one occasion, accumulating 12 wins. GSA obtain five victories, while JF and GSA get 4 each. And CS win in one case. In nineteen of the forty cases reported in Table 16, corresponding to the HPSI metric, the DMEDA wins, while the OOA and the AHA win five times, and the SSA and JF wins four times. In Table 17, DMEDA only expires in $25 \%$ of the cases. The majority of victories are obtained by the SSA in this metric. Until now, there is no dominant algorithm for all the proposed metrics. The DMEDA is an algorithm that won in the majority of the evaluations corresponding to the two objective functions (Otsu and Kapur). Still, the dominance of the metrics is divided into the proposed algorithms. It is important to mention that the DMEDA has better metrics with Kapur than with Otsu.

Based on the convergence curves shown in Fig. 9 show that the proposed algorithm performs better on the Kapur objective function compared to the others. The algorithm, as in Otsu, converges and is superior to EDA. The impact that the mutation operator has on the EDA results is significant for the two objective functions of the multilevel thresholding problem. Being a minor modification, improvements are obtained in the results of the original EDA. In both metrics, the algorithm shows fast convergence and to a better optimum than EDA. Therefore, we have an algorithm with better characteristics than EDA only by applying the current to best Differential Mutation operator.

Figs. 10, 11, 12, and 13 contain the segmented images at the different thresholding levels. For this case, the images were thresholded using Kapur's entropy criterion. As with Otsu, increasing the number of thresholds brings out the details in the images. Images 12,003, 37,073, and 56,028 are shown in Fig. 10. In image 12,003, it is observed that the background details are not perceptible for two thresholds, but for five thresholds, these details can be found. In images 37,073 and 56,028 , when using two thresholds, the details of the concrete and the wall are not perceived. In image 37,073,

![img-21.jpeg](img-21.jpeg)

![img-22.jpeg](img-22.jpeg)

![img-23.jpeg](img-23.jpeg)

![img-24.jpeg](img-24.jpeg)

![img-25.jpeg](img-25.jpeg)

![img-26.jpeg](img-26.jpeg)

![img-27.jpeg](img-27.jpeg)

![img-28.jpeg](img-28.jpeg)

![img-29.jpeg](img-29.jpeg)

![img-30.jpeg](img-30.jpeg)

![img-31.jpeg](img-31.jpeg)

![img-32.jpeg](img-32.jpeg)

![img-33.jpeg](img-33.jpeg)

![img-34.jpeg](img-34.jpeg)

![img-35.jpeg](img-35.jpeg)

![img-36.jpeg](img-36.jpeg)

![img-37.jpeg](img-37.jpeg)

![img-38.jpeg](img-38.jpeg)

Fig. 4 Convergence curves using Otsu's between-class variance as an objective function
the man who walks does not appear when segmented with two thresholds.

Figure 11 shows three images of animals (108,070, $160,068,296,059)$. In image 108,070 you can see a tiger camouflaged with the shadow of some trees, with thresholding by Kapur using two thresholds. The tiger is imperceptible, but it can be detected more easily with five. Image 160,068 is another spotted feline on a trunk. The details of the spots and the trunk can be observed from three thresholds. Finally, the superimposed elephants presented in image 296,059 can be seen in greater detail from four thresholds. The environment can be better appreciated when you have a threshold level greater than three.

In Figs. 12 and 13, four images are shown with different sizes than the previous ones. The images presented are $66,075,101,087,210,088$, and 302008 . The first of them is an ostrich that does not have great complexity for its segmentation. With two thresholds, it is possible to perceive the bird's position. In image 101,087, which shows a boatman, the details of the environment can be better appreciated by increasing the number of thresholds. The fish shown in image 210,088 with five thresholds can be easily detected;
having smaller thresholds decreases the amount of detail. Finally, the person wearing dark clothing loses detail when thresholded in three regions; with a level of five thresholds, the details of the shirt and face can be perceived. In some real cases, it is necessary to extract small regions from the images that are segmented to be analyzed; therefore, a higher level of detail is necessary and, using segmentation by thresholding, it is possible to define the number of necessary regions, this gives flexibility in image processing.

### 4.5 Analysis on the entire BSDS300 dataset using Otsu and Kapur as objective functions

This section shows a general analysis of the behavior of the algorithms over the 300 images of the BSDS300 dataset using Otsu and Kapur as objective functions. First, the results using Otsu's between-class variance will be discussed, and an analysis will be carried out by thresholding level in which it is observed how the DMEDA has better results over the objective function at all thresholding levels. Table 18 shows the general results for two thresholds. In this case, it can be seen that DMEDA is better for

![img-39.jpeg](img-39.jpeg)

Fig. 5 Images and the different thresholds obtained using the Otsu's between-class variance

Otsu, but the JF and SCA algorithms perform better in the metrics.

Tables 19, 20, and 21 show that the DMEDA is better in the objective function and the SSIM metric as the number of thresholds increases. For the three and five thresholds, the OOA generates better general results in the metrics; in the four thresholds, the JF is the winner. The performance of the JF for two and four thresholds, in terms of the objective function, is similar to the performance of the DMEDA. The distance of DMEDA on the metrics concerning the algorithms with the best results is small. Notably, when comparing DMEDA with EDA, a considerable difference is observed between the two algorithms when the number of
thresholds increases. Therefore, it can be said that the mutation operator positively impacts increasing dimensionality.

To review the behavior of the data on the different indicators that have already been discussed, the use of the boxplot graph is proposed in Fig. 14. As an example, the boxplots are generated with the result obtained using 2 thresholds. With this type of graph, it is possible to compare a set of algorithms visually, and together with the tables, you can reach a better conclusion about what is observed. In the different metrics, the values must be high, indicating that the algorithm obtained good results. As mentioned, the algorithms that obtain good results in the previous Tables appear to be at the same level graphically

![img-40.jpeg](img-40.jpeg)

Fig. 6 Images and the different thresholds obtained using the Otsu's between-class variance
on the objective function and the seven metrics described in Subsection 4.2. In some algorithms, such as CS, the difference with the others is evident due to their low performance.

On the other hand, an analysis similar to the previous one is done, but now with the Kapur objective function. In this case, DMEDA improves its results by increasing the number of thresholds, but unlike Otsu, it is done globally. The Table 22 shows that DMEDA is outperformed by OOA over two thresholds on a set of meaningful metrics. However, the Tables show how DMEDA is significantly superior to the other algorithms, optimizing with better results in Kapur and obtaining better metrics than with Otsu. Therefore, the optimization with Kapur and DMEDA provides better solutions
on the metrics than using Otsu and DMEDA, although the objective function in both cases was optimized with better results with the algorithm in question (Tables 23, 24, 25).

A graphical analysis was also carried out on the results obtained with Kapur. In this case, a slight visual difference can be noticed between DMEDA and the other algorithms. The worst algorithm is now the SCA. Using the previous tables and this boxplot, you can see the superiority of DMEDA compared to the other algorithms. As with Otsu, an example of the boxplots is placed using two thresholds (Fig. 15).

DMEDA optimizes the two objective functions with better results than the other algorithms, and by increasing the number of thresholds, it increases its superiority in both

![img-41.jpeg](img-41.jpeg)

Fig. 7 Images and the different thresholds obtained using the Otsu's between-class variance
cases. Using Kapur achieves better overall performance than using Otsu. Therefore, this algorithm performs better using Kapur.

### 4.6 Statistical analysis using paired Wilcoxon test

To use a parametric test, it is necessary to comply with normality, homogeneity, and independence assumptions. When any of these assumptions are not met, it is necessary to use a non-parametric test such as Wilcoxon to pair data [88]. In this case, the Wilcoxon test is used because some of the residuals or populations do not meet the normality assumption when using some parametric tests. A comparison of
each algorithm was performed on each image and each thresholding level. The test was performed by comparing the data obtained in thirty replicates of each algorithm for each threshold.

The Table 26 shows a summary of all the possible combinations of the algorithms and the $p$-values and the $h$-values. The $p$-value shows the area under the curve of the statistic used in the Wilcoxon test, and it is known that if the $p$-value is less than 0.05 , the null hypothesis of the test is not accepted. The null hypothesis that is posed is that the distributions of the two algorithms that are compared at the time are equal. Therefore, if the $p$-value is less than 0.05 , it is said that the data distributions obtained by the two compared algorithms are significantly different. The h-value is a

![img-42.jpeg](img-42.jpeg)

Fig. 8 Images and the different thresholds obtained using the Otsu's between-class variance
dummy variable that returns $T$ if there is a significant difference between the algorithms and $F$ if there is not.

The comparison of the DMEDA in Otsu with most of the algorithms shows significant differences, except with two. The first of these is CS, with which there is no significant difference in three cases, which coincide at a threshold level of 5 . The second is the OOA, with which there are no significant differences in $72.5 \%$ of the cases. Using the information obtained by the Wilcoxon test and the information in Table 2, it can be said that the DMEDA has better overall results on fitness function.

To complement what was observed in the Otsu objective function, the same analysis is done on Kapur (Table 27). For Kapur, all the results obtained with the different algorithms have a significant difference. Taking Table 10 that shows the algorithm's results on the objective function and this statistical analysis, we also conclude that DMEDA is superior to the other algorithms in the majority of this set of ten images of this dataset.

![img-43.jpeg](img-43.jpeg)

![img-44.jpeg](img-44.jpeg)

![img-45.jpeg](img-45.jpeg)

![img-46.jpeg](img-46.jpeg)

![img-47.jpeg](img-47.jpeg)

![img-48.jpeg](img-48.jpeg)

![img-49.jpeg](img-49.jpeg)

![img-50.jpeg](img-50.jpeg)

![img-51.jpeg](img-51.jpeg)

![img-52.jpeg](img-52.jpeg)

![img-53.jpeg](img-53.jpeg)

![img-54.jpeg](img-54.jpeg)

![img-55.jpeg](img-55.jpeg)

![img-56.jpeg](img-56.jpeg)

![img-57.jpeg](img-57.jpeg)

![img-58.jpeg](img-58.jpeg)

![img-59.jpeg](img-59.jpeg)

![img-60.jpeg](img-60.jpeg)

![img-61.jpeg](img-61.jpeg)

Fig. 9 Convergence curves using Kapur's entropy as an objective function

## 5 Conclusions and future works

In this paper, a hybrid EDA algorithm is proposed that improves its exploratory capacity by adding a simple Differential Mutation operator. It tested how the algorithm can give better results than EDA and a set of metaheuristic algorithms on the Otsu and Kapur objective functions. A different approach is shown in the proposal of probabilistic models for the sampling process through hybridization of the algorithm, providing significant improvements in the results. With the DMEDA, better results are obtained on the objective function. The EDA is improved in exploring the search space using the Differential Mutation operator, and its results are consistent at each iteration. After the sampling phase, the DM operator is proposed so that the new population of individuals to be sampled can better explore the search space and leave possible local optimums. Therefore, the DMEDA optimizes the objective
function with better results, balancing the exploration and exploitation of its individuals in the search for local optima in the Otsu objective function maximization problem and Kapur objective function maximization problem for image segmentation by multilevel thresholding. Also, the DMEDA has greater exploitation capacity than the EDA because the results have less variation at each iteration.

In this research, images of an established dataset were studied. Metrics such as processing PSNR, SSIM, FSIM, QILV, HPSI, and UIQI were analyzed to evaluate the algorithms concerning the original image. It is observed that other algorithms generate results that favor the structures that result from the segmentation process. Still, the DMEDA is always consistent with its results and achieves better results in the standard deviation of all metrics and in some cases with Kapur, it is better. The PSNR, SSIM, FSIM, QILV, HPSI, and UIQI metrics are smaller when

![img-62.jpeg](img-62.jpeg)

Fig. 10 Images and the different thresholds obtained using Kapur's entropy
the number of thresholds increases; this is generated because the regions are smaller and the similarity of the region of interest with the original image is lower, and these three metrics provide a measure of similarity based on different criteria.

The EDA has the advantage of using few hyper-parameters for its operation; only the size of the population must be configured. This helps because you don't have to solve the problem of optimizing the hyper-parameters based on the algorithm's results. It is known that increasing the size of the population will have better results because it is based on the construction of a probabilistic model that works based on the observed probability distribution. The disadvantage
of EDA is that it gets stuck in local optima, and the stability is not what it is. Therefore, an operation that improves the stability of the results without affecting the advantage that the EDA is used adds only one hyperparameter to the metaheuristics and sacrifices a bit of simplicity. In addition, precision is obtained in the results with higher means of the fitness function.

The proposed algorithm for segmentation obtains better metrics using Kapur than with Otsu, but both objective functions are attacked well by DMEDA. Although, there are some limitations of the proposed algorithm, which are listed below:

![img-63.jpeg](img-63.jpeg)

Fig. 11 Images and the different thresholds obtained using Kapur's entropy

- In low dimensions (fewer number of thresholds), the algorithm is unstable and imprecise.
- It cannot be used in real-time applications, and the number of thresholds must be set manually.
- The method was exclusively designed for image segmentation by multilevel thresholding.

As future work, the proposed DMEDA can be implemented in multilevel thresholding color image segmentation
problems using different objective functions as criteria. In the multilevel thresholding color image segmentation, the objective function is optimized in the three color channels in which the image is located to obtain the different regions of the image. The DMEDA should be compared with state-of-the-art algorithms already applied in image color segmentation. Besides, another branch of future work is the use of the DMEDA as a preprocessing step for a machine learning classifier using medical images.

![img-64.jpeg](img-64.jpeg)

Fig. 12 Images and the different thresholds obtained using Kapur's entropy

![img-65.jpeg](img-65.jpeg)

Fig. 13 Images and the different thresholds obtained using Kapur's entropy

Table 18 Comparison of using Otsu's between-class variance over the BSD300 for two thresholds

| Metric | Algorithm |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | DMEDA | EDA | CS | GSA | JF | SCA | AHA | OOA | SSA |
| Otsu | $\mathbf{2 . 0 4 E + 0 3}$ | $2.04 \mathrm{E}+03$ | $2.04 \mathrm{E}+03$ | $2.02 \mathrm{E}+03$ | $\mathbf{2 . 0 4 E + 0 3}$ | $2.04 \mathrm{E}+03$ | $2.03 \mathrm{E}+03$ | $2.04 \mathrm{E}+03$ | $2.04 \mathrm{E}+03$ |
| PSNR | $1.54 \mathrm{E}+01$ | $1.53 \mathrm{E}+01$ | $1.20 \mathrm{E}+01$ | $1.52 \mathrm{E}+01$ | $\mathbf{1 . 5 5 E + 0 1}$ | $1.54 \mathrm{E}+01$ | $1.51 \mathrm{E}+01$ | $1.55 \mathrm{E}+01$ | $1.50 \mathrm{E}+01$ |
| SSIM | $5.98 \mathrm{E}-01$ | $5.92 \mathrm{E}-01$ | $4.80 \mathrm{E}-01$ | $5.87 \mathrm{E}-01$ | $\mathbf{5 . 9 9 E - 0 1}$ | $5.97 \mathrm{E}-01$ | $5.83 \mathrm{E}-01$ | $5.97 \mathrm{E}-01$ | $5.78 \mathrm{E}-01$ |
| FSIM | $7.15 \mathrm{E}-01$ | $7.09 \mathrm{E}-01$ | $5.93 \mathrm{E}-01$ | $7.04 \mathrm{E}-01$ | $7.19 \mathrm{E}-01$ | $\mathbf{7 . 1 9 E - 0 1}$ | $7.00 \mathrm{E}-01$ | $7.17 \mathrm{E}-01$ | $7.00 \mathrm{E}-01$ |
| QILV | $7.98 \mathrm{E}-01$ | $7.80 \mathrm{E}-01$ | $1.98 \mathrm{E}-01$ | $7.67 \mathrm{E}-01$ | $8.10 \mathrm{E}-01$ | $\mathbf{8 . 1 0 E - 0 1}$ | $7.48 \mathrm{E}-01$ | $8.01 \mathrm{E}-01$ | $7.34 \mathrm{E}-01$ |
| HPSI | $4.21 \mathrm{E}-01$ | $4.11 \mathrm{E}-01$ | $2.45 \mathrm{E}-01$ | $4.05 \mathrm{E}-01$ | $4.23 \mathrm{E}-01$ | $\mathbf{4 . 2 3 E - 0 1}$ | $3.99 \mathrm{E}-01$ | $4.22 \mathrm{E}-01$ | $3.93 \mathrm{E}-01$ |
| UIQI | $8.92 \mathrm{E}-01$ | $8.85 \mathrm{E}-01$ | $6.68 \mathrm{E}-01$ | $8.77 \mathrm{E}-01$ | $\mathbf{8 . 9 8 E - 0 1}$ | $8.95 \mathrm{E}-01$ | $8.68 \mathrm{E}-01$ | $8.95 \mathrm{E}-01$ | $8.49 \mathrm{E}-01$ |

Bold means the best value provided by each algorithm

Table 19 Comparison of using Otsu's between-class variance over the BSD300 for three thresholds

| Metric | Algorithm |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | DMEDA | EDA | CS | GSA | JF | SCA | AHA | OOA | SSA |
| Otsu | $\mathbf{2 . 2 0 E + 0 3}$ | $2.18 \mathrm{E}+03$ | $2.19 \mathrm{E}+03$ | $2.16 \mathrm{E}+03$ | $2.20 \mathrm{E}+03$ | $2.19 \mathrm{E}+03$ | $2.17 \mathrm{E}+03$ | $2.20 \mathrm{E}+03$ | $2.19 \mathrm{E}+03$ |
| PSNR | $1.80 \mathrm{E}+01$ | $1.75 \mathrm{E}+01$ | $1.49 \mathrm{E}+01$ | $1.73 \mathrm{E}+01$ | $1.80 \mathrm{E}+01$ | $1.79 \mathrm{E}+01$ | $1.71 \mathrm{E}+01$ | $\mathbf{1 . 8 0 E + 0 1}$ | $1.70 \mathrm{E}+01$ |
| SSIM | $7.06 \mathrm{E}-01$ | $6.93 \mathrm{E}-01$ | $6.40 \mathrm{E}-01$ | $6.87 \mathrm{E}-01$ | $7.05 \mathrm{E}-01$ | $7.04 \mathrm{E}-01$ | $6.80 \mathrm{E}-01$ | $\mathbf{7 . 0 6 E - 0 1}$ | $6.76 \mathrm{E}-01$ |
| FSIM | $7.73 \mathrm{E}-01$ | $7.61 \mathrm{E}-01$ | $6.87 \mathrm{E}-01$ | $7.54 \mathrm{E}-01$ | $7.74 \mathrm{E}-01$ | $7.74 \mathrm{E}-01$ | $7.48 \mathrm{E}-01$ | $\mathbf{7 . 7 5 E - 0 1}$ | $7.49 \mathrm{E}-01$ |
| QILV | $8.81 \mathrm{E}-01$ | $8.58 \mathrm{E}-01$ | $5.05 \mathrm{E}-01$ | $8.47 \mathrm{E}-01$ | $8.85 \mathrm{E}-01$ | $\mathbf{8 . 8 6 E - 0 1}$ | $8.30 \mathrm{E}-01$ | $8.85 \mathrm{E}-01$ | $8.22 \mathrm{E}-01$ |
| HPSI | $5.21 \mathrm{E}-01$ | $5.00 \mathrm{E}-01$ | $3.74 \mathrm{E}-01$ | $4.91 \mathrm{E}-01$ | $5.23 \mathrm{E}-01$ | $\mathbf{5 . 2 3 E - 0 1}$ | $4.79 \mathrm{E}-01$ | $5.23 \mathrm{E}-01$ | $4.80 \mathrm{E}-01$ |
| UIQI | $9.42 \mathrm{E}-01$ | $9.34 \mathrm{E}-01$ | $8.70 \mathrm{E}-01$ | $9.29 \mathrm{E}-01$ | $9.44 \mathrm{E}-01$ | $9.43 \mathrm{E}-01$ | $9.18 \mathrm{E}-01$ | $\mathbf{9 . 4 4 E - 0 1}$ | $9.05 \mathrm{E}-01$ |

Bold means the best value provided by each algorithm

Table 20 Comparison of using Otsu's between-class variance over the BSD300 for four thresholds

| Metric | Algorithm |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | DMEDA | EDA | CS | GSA | JF | SCA | AHA | OOA | SSA |
| Otsu | $\mathbf{2 . 2 6 E + 0 3}$ | $2.24 \mathrm{E}+03$ | $2.25 \mathrm{E}+03$ | $2.23 \mathrm{E}+03$ | $2.26 \mathrm{E}+03$ | $2.25 \mathrm{E}+03$ | $2.23 \mathrm{E}+03$ | $2.26 \mathrm{E}+03$ | $2.26 \mathrm{E}+03$ |
| PSNR | $1.96 \mathrm{E}+01$ | $1.90 \mathrm{E}+01$ | $1.70 \mathrm{E}+01$ | $1.87 \mathrm{E}+01$ | $\mathbf{1 . 9 7 E + 0 1}$ | $1.96 \mathrm{E}+01$ | $1.85 \mathrm{E}+01$ | $1.97 \mathrm{E}+01$ | $1.85 \mathrm{E}+01$ |
| SSIM | $\mathbf{7 . 8 1 E - 0 1}$ | $7.56 \mathrm{E}-01$ | $7.26 \mathrm{E}-01$ | $7.48 \mathrm{E}-01$ | $7.81 \mathrm{E}-01$ | $7.72 \mathrm{E}-01$ | $7.38 \mathrm{E}-01$ | $7.79 \mathrm{E}-01$ | $7.38 \mathrm{E}-01$ |
| FSIM | $8.13 \mathrm{E}-01$ | $7.94 \mathrm{E}-01$ | $7.48 \mathrm{E}-01$ | $7.87 \mathrm{E}-01$ | $8.16 \mathrm{E}-01$ | $8.12 \mathrm{E}-01$ | $7.82 \mathrm{E}-01$ | $\mathbf{8 . 1 7 E - 0 1}$ | $7.84 \mathrm{E}-01$ |
| QILV | $9.23 \mathrm{E}-01$ | $9.00 \mathrm{E}-01$ | $6.96 \mathrm{E}-01$ | $8.91 \mathrm{E}-01$ | $\mathbf{9 . 2 7 E - 0 1}$ | $9.25 \mathrm{E}-01$ | $8.75 \mathrm{E}-01$ | $9.26 \mathrm{E}-01$ | $8.62 \mathrm{E}-01$ |
| HPSI | $6.03 \mathrm{E}-01$ | $5.62 \mathrm{E}-01$ | $4.68 \mathrm{E}-01$ | $5.50 \mathrm{E}-01$ | $\mathbf{6 . 0 5 E - 0 1}$ | $5.95 \mathrm{E}-01$ | $5.37 \mathrm{E}-01$ | $6.03 \mathrm{E}-01$ | $5.40 \mathrm{E}-01$ |
| UIQI | $9.65 \mathrm{E}-01$ | $9.56 \mathrm{E}-01$ | $9.32 \mathrm{E}-01$ | $9.50 \mathrm{E}-01$ | $\mathbf{9 . 6 5 E - 0 1}$ | $9.63 \mathrm{E}-01$ | $9.44 \mathrm{E}-01$ | $9.65 \mathrm{E}-01$ | $9.33 \mathrm{E}-01$ |

Bold means the best value provided by each algorithm

Table 21 Comparison of using Otsu's between-class variance over the BSD300 for five thresholds

| Metric | Algorithm |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | DMEDA | EDA | CS | GSA | JF | SCA | AHA | OOA | SSA |
| Otsu | $\mathbf{2 . 3 0 E + 0 3}$ | $2.27 \mathrm{E}+03$ | $2.28 \mathrm{E}+03$ | $2.26 \mathrm{E}+03$ | $\mathbf{2 . 3 0 E + 0 3}$ | $2.29 \mathrm{E}+03$ | $2.27 \mathrm{E}+03$ | $2.29 \mathrm{E}+03$ | $2.28 \mathrm{E}+03$ |
| PSNR | $2.13 \mathrm{E}+01$ | $2.04 \mathrm{E}+01$ | $1.86 \mathrm{E}+01$ | $1.99 \mathrm{E}+01$ | $\mathbf{2 . 1 3 E + 0 1}$ | $2.11 \mathrm{E}+01$ | $1.98 \mathrm{E}+01$ | $2.13 \mathrm{E}+01$ | $1.98 \mathrm{E}+01$ |
| SSIM | $\mathbf{8 . 2 8 E - 0 1}$ | $8.00 \mathrm{E}-01$ | $7.80 \mathrm{E}-01$ | $7.90 \mathrm{E}-01$ | $8.27 \mathrm{E}-01$ | $8.16 \mathrm{E}-01$ | $7.81 \mathrm{E}-01$ | $8.23 \mathrm{E}-01$ | $7.80 \mathrm{E}-01$ |
| FSIM | $8.44 \mathrm{E}-01$ | $8.20 \mathrm{E}-01$ | $7.86 \mathrm{E}-01$ | $8.11 \mathrm{E}-01$ | $8.45 \mathrm{E}-01$ | $8.40 \mathrm{E}-01$ | $8.06 \mathrm{E}-01$ | $\mathbf{8 . 4 5 E - 0 1}$ | $8.10 \mathrm{E}-01$ |
| QILV | $9.45 \mathrm{E}-01$ | $9.24 \mathrm{E}-01$ | $7.94 \mathrm{E}-01$ | $9.16 \mathrm{E}-01$ | $9.48 \mathrm{E}-01$ | $9.46 \mathrm{E}-01$ | $9.02 \mathrm{E}-01$ | $\mathbf{9 . 4 8 E - 0 1}$ | $8.92 \mathrm{E}-01$ |
| HPSI | $6.61 \mathrm{E}-01$ | $6.09 \mathrm{E}-01$ | $5.36 \mathrm{E}-01$ | $5.96 \mathrm{E}-01$ | $6.63 \mathrm{E}-01$ | $6.52 \mathrm{E}-01$ | $5.87 \mathrm{E}-01$ | $\mathbf{6 . 6 4 E - 0 1}$ | $5.88 \mathrm{E}-01$ |
| UIQI | $9.76 \mathrm{E}-01$ | $9.69 \mathrm{E}-01$ | $9.56 \mathrm{E}-01$ | $9.64 \mathrm{E}-01$ | $9.76 \mathrm{E}-01$ | $9.75 \mathrm{E}-01$ | $9.59 \mathrm{E}-01$ | $\mathbf{9 . 7 7 E - 0 1}$ | $9.51 \mathrm{E}-01$ |

Bold means the best value provided by each algorithm

![img-66.jpeg](img-66.jpeg)
(a) Otsu's between-class variance.
(b) FSNR.
![img-67.jpeg](img-67.jpeg)
(c) SSIM
![img-68.jpeg](img-68.jpeg)
(e) QIIV.
![img-69.jpeg](img-69.jpeg)
(g) UIQI.

Fig. 14 Boxplot representation for two thresholds general results with Otsu's between-class variance

Table 22 Comparison of using Kapur's entropy over the BSD300 for two thresholds

| Metric | Algorithm |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | DMEDA | EDA | CS | GSA | JF | SCA | AHA | OOA | SSA |
| Kapur | $1.29 \mathrm{E}+01$ | $1.28 \mathrm{E}+01$ | $1.29 \mathrm{E}+01$ | $1.28 \mathrm{E}+01$ | $1.27 \mathrm{E}+01$ | $5.54 \mathrm{E}+00$ | $1.28 \mathrm{E}+01$ | $\mathbf{1 . 2 9 E + 0 1}$ | $1.27 \mathrm{E}+01$ |
| PSNR | $1.07 \mathrm{E}+01$ | $1.08 \mathrm{E}+01$ | $1.03 \mathrm{E}+01$ | $1.10 \mathrm{E}+01$ | $1.10 \mathrm{E}+01$ | $8.53 \mathrm{E}+00$ | $1.10 \mathrm{E}+01$ | $1.06 \mathrm{E}+01$ | $\mathbf{1 . 1 6 E + 0 1}$ |
| SSIM | $3.14 \mathrm{E}-01$ | $3.18 \mathrm{E}-01$ | $3.02 \mathrm{E}-01$ | $3.31 \mathrm{E}-01$ | $3.35 \mathrm{E}-01$ | $2.65 \mathrm{E}-01$ | $3.35 \mathrm{E}-01$ | $2.99 \mathrm{E}-01$ | $\mathbf{4 . 3 7 E - 0 1}$ |
| FSIM | $5.79 \mathrm{E}-01$ | $5.83 \mathrm{E}-01$ | $5.75 \mathrm{E}-01$ | $5.86 \mathrm{E}-01$ | $\mathbf{5 . 8 7 E - 0 1}$ | $4.62 \mathrm{E}-01$ | $5.71 \mathrm{E}-01$ | $5.62 \mathrm{E}-01$ | $5.73 \mathrm{E}-01$ |
| QILV | $3.49 \mathrm{E}-01$ | $3.69 \mathrm{E}-01$ | $2.80 \mathrm{E}-01$ | $\mathbf{3 . 9 2 E - 0 1}$ | $3.92 \mathrm{E}-01$ | $5.76 \mathrm{E}-02$ | $3.81 \mathrm{E}-01$ | $3.45 \mathrm{E}-01$ | $3.55 \mathrm{E}-01$ |
| HPSI | $2.18 \mathrm{E}-01$ | $2.22 \mathrm{E}-01$ | $2.09 \mathrm{E}-01$ | $2.28 \mathrm{E}-01$ | $2.30 \mathrm{E}-01$ | $1.02 \mathrm{E}-01$ | $2.27 \mathrm{E}-01$ | $2.13 \mathrm{E}-01$ | $\mathbf{2 . 3 4 E - 0 1}$ |
| UIQI | $2.49 \mathrm{E}-01$ | $-1.88 \mathrm{E}-01$ | $\mathbf{7 . 5 6 E - 0 1}$ | $2.61 \mathrm{E}-01$ | $-1.23 \mathrm{E}-01$ | $2.16 \mathrm{E}-01$ | $2.21 \mathrm{E}-01$ | $8.39 \mathrm{E}-02$ | $2.42 \mathrm{E}-01$ |

Bold means the best value provided by each algorithm

Table 23 Comparison of using Kapur's entropy over the BSD300 for three thresholds

| Metric | Algorithm |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | DMEDA | EDA | CS | GSA | JF | SCA | AHA | OOA | SSA |
| Kapur | $\mathbf{1 . 8 0 E + 0 1}$ | $1.77 \mathrm{E}+01$ | $1.79 \mathrm{E}+01$ | $1.76 \mathrm{E}+01$ | $1.76 \mathrm{E}+01$ | $8.08 \mathrm{E}+00$ | $1.76 \mathrm{E}+01$ | $1.79 \mathrm{E}+01$ | $1.75 \mathrm{E}+01$ |
| PSNR | $\mathbf{1 . 4 0 E + 0 1}$ | $1.38 \mathrm{E}+01$ | $1.35 \mathrm{E}+01$ | $1.39 \mathrm{E}+01$ | $1.39 \mathrm{E}+01$ | $9.38 \mathrm{E}+00$ | $1.38 \mathrm{E}+01$ | $1.36 \mathrm{E}+01$ | $1.33 \mathrm{E}+01$ |
| SSIM | $5.23 \mathrm{E}-01$ | $5.14 \mathrm{E}-01$ | $5.09 \mathrm{E}-01$ | $5.20 \mathrm{E}-01$ | $5.19 \mathrm{E}-01$ | $3.36 \mathrm{E}-01$ | $5.18 \mathrm{E}-01$ | $4.91 \mathrm{E}-01$ | $\mathbf{5 . 3 7 E - 0 1}$ |
| FSIM | $\mathbf{6 . 6 7 E - 0 1}$ | $6.65 \mathrm{E}-01$ | $6.60 \mathrm{E}-01$ | $6.67 \mathrm{E}-01$ | $6.66 \mathrm{E}-01$ | $4.94 \mathrm{E}-01$ | $6.61 \mathrm{E}-01$ | $6.59 \mathrm{E}-01$ | $6.39 \mathrm{E}-01$ |
| QILV | $6.29 \mathrm{E}-01$ | $6.27 \mathrm{E}-01$ | $5.71 \mathrm{E}-01$ | $\mathbf{6 . 3 2 E - 0 1}$ | $6.29 \mathrm{E}-01$ | $9.66 \mathrm{E}-02$ | $6.15 \mathrm{E}-01$ | $6.28 \mathrm{E}-01$ | $4.96 \mathrm{E}-01$ |
| HPSI | $\mathbf{3 . 4 8 E - 0 1}$ | $3.44 \mathrm{E}-01$ | $3.35 \mathrm{E}-01$ | $3.45 \mathrm{E}-01$ | $3.43 \mathrm{E}-01$ | $1.30 \mathrm{E}-01$ | $3.39 \mathrm{E}-01$ | $3.37 \mathrm{E}-01$ | $3.01 \mathrm{E}-01$ |
| UIQI | $7.24 \mathrm{E}-01$ | $6.29 \mathrm{E}-01$ | $-8.53 \mathrm{E}-02$ | $5.65 \mathrm{E}-01$ | $8.26 \mathrm{E}-01$ | $3.20 \mathrm{E}-01$ | $\mathbf{9 . 1 1 E - 0 1}$ | $6.88 \mathrm{E}-01$ | $6.60 \mathrm{E}-01$ |

Bold means the best value provided by each algorithm

Table 24 Comparison of using Kapur's entropy over the BSD300 for four thresholds

| Metric | Algorithm |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | DMEDA | EDA | CS | GSA | JF | SCA | AHA | OOA | SSA |
| Kapur | $\mathbf{2 . 2 6 E + 0 1}$ | $2.21 \mathrm{E}+01$ | $2.24 \mathrm{E}+01$ | $2.19 \mathrm{E}+01$ | $2.19 \mathrm{E}+01$ | $1.04 \mathrm{E}+01$ | $2.20 \mathrm{E}+01$ | $2.25 \mathrm{E}+01$ | $2.18 \mathrm{E}+01$ |
| PSNR | $\mathbf{1 . 6 7 E + 0 1}$ | $1.61 \mathrm{E}+01$ | $1.59 \mathrm{E}+01$ | $1.59 \mathrm{E}+01$ | $1.60 \mathrm{E}+01$ | $1.00 \mathrm{E}+01$ | $1.59 \mathrm{E}+01$ | $1.61 \mathrm{E}+01$ | $1.48 \mathrm{E}+01$ |
| SSIM | $\mathbf{6 . 5 8 E - 0 1}$ | $6.36 \mathrm{E}-01$ | $6.37 \mathrm{E}-01$ | $6.30 \mathrm{E}-01$ | $6.31 \mathrm{E}-01$ | $3.83 \mathrm{E}-01$ | $6.29 \mathrm{E}-01$ | $6.17 \mathrm{E}-01$ | $6.13 \mathrm{E}-01$ |
| FSIM | $\mathbf{7 . 3 3 E - 0 1}$ | $7.21 \mathrm{E}-01$ | $7.20 \mathrm{E}-01$ | $7.18 \mathrm{E}-01$ | $7.19 \mathrm{E}-01$ | $5.14 \mathrm{E}-01$ | $7.15 \mathrm{E}-01$ | $7.25 \mathrm{E}-01$ | $6.78 \mathrm{E}-01$ |
| QILV | $\mathbf{7 . 8 3 E - 0 1}$ | $7.58 \mathrm{E}-01$ | $7.28 \mathrm{E}-01$ | $7.50 \mathrm{E}-01$ | $7.52 \mathrm{E}-01$ | $1.30 \mathrm{E}-01$ | $7.37 \mathrm{E}-01$ | $7.82 \mathrm{E}-01$ | $5.96 \mathrm{E}-01$ |
| HPSI | $\mathbf{4 . 5 5 E - 0 1}$ | $4.33 \mathrm{E}-01$ | $4.30 \mathrm{E}-01$ | $4.26 \mathrm{E}-01$ | $4.27 \mathrm{E}-01$ | $1.51 \mathrm{E}-01$ | $4.22 \mathrm{E}-01$ | $4.38 \mathrm{E}-01$ | $3.58 \mathrm{E}-01$ |
| UIQI | $8.60 \mathrm{E}-01$ | $8.81 \mathrm{E}-01$ | $\mathbf{1 . 0 2 E + 0 0}$ | $8.61 \mathrm{E}-01$ | $8.47 \mathrm{E}-01$ | $3.97 \mathrm{E}-01$ | $8.54 \mathrm{E}-01$ | $8.36 \mathrm{E}-01$ | $8.07 \mathrm{E}-01$ |

Bold means the best value provided by each algorithm
Table 25 Comparison of using Kapur's entropy over the BSD300 for five thresholds

| Metric | Algorithm |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | DMEDA | EDA | CS | GSA | JF | SCA | AHA | OOA | SSA |
| Kapur | $\mathbf{2 . 6 9 E + 0 1}$ | $2.61 \mathrm{E}+01$ | $2.65 \mathrm{E}+01$ | $2.58 \mathrm{E}+01$ | $2.58 \mathrm{E}+01$ | $1.23 \mathrm{E}+01$ | $2.60 \mathrm{E}+01$ | $2.68 \mathrm{E}+01$ | $2.57 \mathrm{E}+01$ |
| PSNR | $\mathbf{1 . 8 7 E + 0 1}$ | $1.77 \mathrm{E}+01$ | $1.77 \mathrm{E}+01$ | $1.75 \mathrm{E}+01$ | $1.75 \mathrm{E}+01$ | $1.05 \mathrm{E}+01$ | $1.75 \mathrm{E}+01$ | $1.80 \mathrm{E}+01$ | $1.59 \mathrm{E}+01$ |
| SSIM | $\mathbf{7 . 4 1 E - 0 1}$ | $7.08 \mathrm{E}-01$ | $7.14 \mathrm{E}-01$ | $7.00 \mathrm{E}-01$ | $7.01 \mathrm{E}-01$ | $4.16 \mathrm{E}-01$ | $7.01 \mathrm{E}-01$ | $7.01 \mathrm{E}-01$ | $6.60 \mathrm{E}-01$ |
| FSIM | $\mathbf{7 . 8 3 E - 0 1}$ | $7.61 \mathrm{E}-01$ | $7.63 \mathrm{E}-01$ | $7.55 \mathrm{E}-01$ | $7.55 \mathrm{E}-01$ | $5.31 \mathrm{E}-01$ | $7.53 \mathrm{E}-01$ | $7.73 \mathrm{E}-01$ | $7.04 \mathrm{E}-01$ |
| QILV | $\mathbf{8 . 6 1 E - 0 1}$ | $8.29 \mathrm{E}-01$ | $8.14 \mathrm{E}-01$ | $8.19 \mathrm{E}-01$ | $8.20 \mathrm{E}-01$ | $1.59 \mathrm{E}-01$ | $8.09 \mathrm{E}-01$ | $8.60 \mathrm{E}-01$ | $6.64 \mathrm{E}-01$ |
| HPSI | $\mathbf{5 . 4 0 E - 0 1}$ | $5.00 \mathrm{E}-01$ | $5.04 \mathrm{E}-01$ | $4.89 \mathrm{E}-01$ | $4.89 \mathrm{E}-01$ | $1.70 \mathrm{E}-01$ | $4.85 \mathrm{E}-01$ | $5.19 \mathrm{E}-01$ | $3.99 \mathrm{E}-01$ |
| UIQI | $9.07 \mathrm{E}-01$ | $9.44 \mathrm{E}-01$ | $9.03 \mathrm{E}-01$ | $8.84 \mathrm{E}-01$ | $9.42 \mathrm{E}-01$ | $6.02 \mathrm{E}-02$ | $\mathbf{1 . 2 1 E + 0 0}$ | $1.20 \mathrm{E}+00$ | $8.31 \mathrm{E}-01$ |

Bold means the best value provided by each algorithm

![img-70.jpeg](img-70.jpeg)
(a) Kapur's entropy.
(b) PSNR.
![img-71.jpeg](img-71.jpeg)
(c) SSIM.
![img-72.jpeg](img-72.jpeg)
(e) QILV.
![img-73.jpeg](img-73.jpeg)
(g) UIQI.

Fig. 15 Boxplot representation for two thresholds general results with Kapur's entropy

![img-74.jpeg](img-74.jpeg)

![img-75.jpeg](img-75.jpeg)

![img-76.jpeg](img-76.jpeg)

![img-77.jpeg](img-77.jpeg)

Author Contributions All authors contributed equally to the study conception and design.

Data Availability The data used to support the findings are cited within the article. Also, the datasets generated during and/or analyzed during the current study are available from the corresponding author upon reasonable request.

## Declarations

Ethical approval This article does not contain any studies with human participants or animals performed by any of the authors.

Funding The authors declare that no funds, grants, or other support were received during the preparation of this manuscript.

Conflict of interest All the authors declare that there is no Conflict of interest.

Informed consent Informed consent was obtained from all individual participants included in the study.

## References

1. Abd Elaziz M, Ewees AA, Oliva D (2020) Hyper-heuristic method for multilevel thresholding image segmentation. Expert Syst Appl 146:113201
2. Teoh TT, Rong Z (2022) Python for data analysis. In: Artificial Intelligence with Python, pp 107-122. Springer
3. Özbay E, Özbay FA, Gharehchopogh FS (2023) Peripheral blood smear images classification for acute lymphoblastic leukemia diagnosis with an improved convolutional neural network. J Bionic Eng 1-17
4. Chauhan R, Joshi R (2021) Comparative evaluation of image segmentation techniques with application to mri segmentation. In: Proceedings of International Conference on Machine Intelligence and Data Science Applications, pp 521-537, Springer
5. Oliva D, Abd Elaziz M, Hinojosa S (2019) Metaheuristic algorithms for image segmentation: theory and applications. Springer, New York
6. Abd El Aziz M, Ewees AA, Hassanien AE (2017) Whale optimization algorithm and moth-flame optimization for multilevel thresholding image segmentation. Expert Syst Appl 83:242-256 (2017)
7. Houssein EH, Helmy BE-D, Oliva D, Elngar AA, Shaban H (2021) A novel black widow optimization algorithm for multilevel thresholding image segmentation. Exp Syst Appl 167:114159
8. Jiang Z, Zou F, Chen D, Kang J (2021) An improved teaching-learning-based optimization for multilevel thresholding image segmentation. Arab J Sci Eng 46(9):8371-8396
9. Liu C, Liu W, Xing W (2019) A weighted edge-based level set method based on multi-local statistical information for noisy image segmentation. J Vis Commun Image Represent 59:89-107
10. Prathusha, P., Jyothi, S.: A novel edge detection algorithm for fast and efficient image segmentation. In: Data Engineering and Intelligent Computing, pp. 283-291 (2018). Springer
11. Bakkay MC, Chambon S, Rashwan HA, Lubat C, Barsotti S (2018) Automatic detection of individual and touching moths from trap images by combining contour-based and region-based segmentation. IET Comput Vision 12(2):138-145
12. Huang H, Meng F, Zhou S, Jiang F, Manogaran G (2019) Brain image segmentation based on fcm clustering algorithm and rough set. IEEE Access 7:12386-12396
13. Hao S, Zhou Y, Guo Y (2020) A brief survey on semantic segmentation with deep learning. Neurocomputing 406:302-321
14. Asgari Taghanaki S, Abhishek K, Cohen JP, Cohen-Adad J, Hamarneh G (2021) Deep semantic segmentation of natural and medical images: a review. Artif Intell Rev 54(1):137-178
15. Milioto, A., Vizzo, I., Behley, J., Stachniss, C.: Rangenet++: Fast and accurate lidar semantic segmentation. In: 2019 IEEE/ RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 4213-4220 (2019). IEEE
16. Upadhyay P, Chhabra JK (2021) Multilevel thresholding based image segmentation using new multistage hybrid optimization algorithm. J Ambient Intell Humaniz Comput 12:1081-1098
17. Otsu N (1979) A threshold selection method from gray-level histograms. IEEE Trans Syst Man Cybern 9(1):62-66
18. Merzban MH, Elbayoumi M (2019) Efficient solution of otsu multilevel image thresholding: A comparative study. Expert Syst Appl 116:299-309
19. Zhang, Z., Zhou, N.: A novel image segmentation method combined otsu and improved pso. In: 2012 IEEE Fifth International Conference on Advanced Computational Intelligence (ICACI), pp. 583-586 (2012). IEEE
20. Fengjie, S., He, W., Jieqing, F.: 2d otsu segmentation algorithm based on simulated annealing genetic algorithm for iced-cable images. In: 2009 International Forum on Information Technology and Applications, vol. 2, pp. 600-602 (2009). IEEE
21. Kapur JN, Sahoo PK, Wong AK (1985) A new method for gray-level picture thresholding using the entropy of the histogram. Computer vision, graphics, and image processing 29(3):273-285
22. Manic KS, Priya RK, Rajinikanth V (2016) Image multithresholding based on kapur/sallis entropy and firefly algorithm. Indian J Sci Technol 9(12):89949
23. Li CH, Lee C (1993) Minimum cross entropy thresholding. Pattern Recogn 26(4):617-625
24. Huang, M., Yu, W., Zhu, D.: An improved image segmentation algorithm based on the otsu method. In: 2012 13th ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, pp. 135-139 (2012). IEEE
25. Gharehchopogh FS, Ucan A, Ibrikci T, Arasteh B, Isik G (2023) Slime mould algorithm: A comprehensive survey of its variants and applications. Archives of Computational Methods in Engineering 30(4):2683-2723
26. Piri J, Mohapatra P, Acharya B, Gharehchopogh FS, Gerogiannis VC, Kanavos A, Manika S (2022) Feature selection using artificial gorilla troop optimization for biomedical data: A case analysis with covid-19 data. Mathematics 10(15):2742
27. Gharehchopogh FS, Khargoush AA (2023) A chaotic-based interactive autodidactic school algorithm for data clustering problems and its application on covid-19 disease detection. Symmetry 15(4):894
28. Abd Elaziz M, Lu S, He S (2021) A multi-leader whale optimization algorithm for global optimization and image segmentation. Expert Syst Appl 175:114841
29. Brajevic, I., Taba, M.: Cuckoo search and firefly algorithm applied to multilevel image thresholding. Cuckoo Search and Firefly Algorithm: Theory and Applications, 115-139 (2014)
30. Wong, W., Ming, C.I.: A review on metaheuristic algorithms: recent trends, benchmarking and applications. In: 2019 7th International Conference on Smart Computing \& Communications (ICSCC), pp. 1-5 (2019). IEEE
31. Ólafsson S (2006) Metaheuristics. Handbooks Oper Res Management Sci 13:633-654

32. Hammouche K, Diaf M, Siarry P (2008) A multilevel automatic thresholding method based on a genetic algorithm for a fast image segmentation. Comput Vis Image Underst 109(2):163-175
33. Kennedy, J., Eberhart, R.: Particle swarm optimization. In: Proceedings of ICNN'95-international Conference on Neural Networks, vol. 4, pp. 1942-1948 (1995). IEEE
34. Karaboga D (2010) Artificial bee colony algorithm. scholarpedia 5(3):6915
35. Yang, X.-S., Deb, S.: Cuckoo search via lévy flights. In: 2009 World Congress on Nature \& Biologically Inspired Computing (NaBIC), pp. 210-214 (2009). Ieee
36. Rashedi E, Nezamabadi-Pour H, Saryazdi S (2009) Gsa: a gravitational search algorithm. Inf Sci 179(13):2232-2248
37. Ahmadianfar I, Heidari AA, Gandomi AH, Chu X, Chen H (2021) Run beyond the metaphor: An efficient optimization algorithm based on runge kutta method. Expert Syst Appl 181:115079
38. Sarkar, S., Patra, G.R., Das, S.: A differential evolution based approach for multilevel image segmentation using minimum cross entropy thresholding. In: Swarm, Evolutionary, and Memetic Computing: Second International Conference, SEMCCO 2011, Visakhapatnam, Andhra Pradesh, India, December 19-21, 2011, Proceedings, Part I 2, pp. 51-58 (2011). Springer
39. Rahkar Farshi T (2021) Battle royale optimization algorithm. Neural Comput Appl 33(4):1139-1157
40. Gharehchopogh, F.S., Ibrikci, T.: An improved african vultures optimization algorithm using different fitness functions for multilevel thresholding image segmentation. Multimedia Tools and Applications, 1-47 (2023)
41. Wang, W., Duan, L., Wang, Y.: Fast image segmentation using two-dimensional otsu based on estimation of distribution algorithm. Journal of Electrical and Computer Engineering 2017 (2017)
42. Oliva D, Martins MS, Osuna-Enciso V, Morais EF (2020) Combining information from thresholding techniques through an evolutionary bayesian network algorithm. Appl Soft Comput 80:106147
43. Larrañaga, P., Lozano, J.A.: Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation vol. 2, (2001). Springer Science \& Business Media
44. Storn R, Price K (1997) Differential evolution-a simple and efficient heuristic for global optimization over continuous spaces. J Global Optim 11(4):341
45. Ceberio, J., Mendiburu, A., Lozano, J.A.: A roadmap for solving optimization problems with estimation of distribution algorithms. Natural Computing, 1-15 (2022)
46. Das S, Suganthan PN (2010) Differential evolution: A survey of the state-of-the-art. IEEE Trans Evol Comput 15(1):4-31
47. Muangkote N, Sunat K, Chiewchanwattana S (2017) Rr-crijade: An efficient differential evolution algorithm for multilevel image thresholding. Expert Syst Appl 90:272-289
48. Liu L, Zhao D, Yu F, Heidari AA, Ru J, Chen H, Mafarja M, Turabieh H, Pan Z (2021) Performance optimization of differential evolution with slime mould algorithm for multilevel breast cancer image segmentation. Comput Biol Med 138:104910
49. Ramadas M, Abraham A (2020) Detecting tumours by segmenting mri images using transformed differential evolution algorithm with kapur's thresholding. Neural Comput Appl 32:6139-6149
50. Gharehchopogh FS, Abdollahzadeh B, Barshandeh S, Arasteh B (2023) A multi-objective mutation-based dynamic harris hawks optimization for botnet detection in iot. Internet of Things 24:100952
51. Shen Y, Zhang C, Gharehchopogh FS, Mirjalili S (2023) An improved whale optimization algorithm based on multi-population evolution for global optimization and engineering design problems. Expert Syst Appl 215:119269
52. Sun J, Zhang Q, Tsang EP (2005) De/eda: A new evolutionary algorithm for global optimization. Inf Sci 169(3-4):249-262
53. Wolpert DH, Macready WG (1997) No free lunch theorems for optimization. IEEE Trans Evol Comput 1(1):67-82
54. Chen, T., Lehre, P.K., Tang, K., Yao, X.: When is an estimation of distribution algorithm better than an evolutionary algorithm? In: 2009 IEEE Congress on Evolutionary Computation, pp. 14701477 (2009). IEEE
55. Pelikan M, Sastry K, Goldberg DE (2002) Scalability of the bayesian optimization algorithm. Int J Approximate Reasoning 31(3):221-258
56. Li Y, Han T, Tang S, Huang C, Zhou H, Wang Y (2023) An improved differential evolution by hybridizing with estimation-of-distribution algorithm. Inf Sci 619:439-456
57. Zhou A, Sun J, Zhang Q (2015) An estimation of distribution algorithm with cheap and expensive local search methods. IEEE Trans Evol Comput 19(6):807-822
58. Pang S, Li W, He H, Shan Z, Wang X (2019) An eda-ga hybrid algorithm for multi-objective task scheduling in cloud computing. IEEE Access 7:146379-146389
59. Ren Z, Fang F, Yan N, Wu Y (2022) State of the art in defect detection based on machine vision. International Journal of Precision Engineering and Manufacturing-Green Technology 9(2):661-691
60. Rahaman J, Sing M (2021) An efficient multilevel thresholding based satellite image segmentation approach using a new adaptive cuckoo search algorithm. Expert Syst Appl 174:114633
61. Suresh S, Lal S (2016) An efficient cuckoo search algorithm based multilevel thresholding for segmentation of satellite images using different objective functions. Expert Syst Appl 58:184-209
62. Mühlenbein, H., Paass, G.: From recombination of genes to the estimation of distributions i. binary parameters. In: Parallel Problem Solving from Nature-PPSN IV: International Conference on Evolutionary Computation-The 4th International Conference on Parallel Problem Solving from Nature Berlin, Germany, September 22-26, 1996 Proceedings 4, pp. 178-187 (1996). Springer
63. Larranaga, P.: A review on estimation of distribution algorithms. Estimation of distribution algorithms, 57-100 (2002)
64. Pérez-Rodríguez R (2021) A hybrid estimation of distribution algorithm for the quay crane scheduling problem. Mathematical and Computational Applications 26(3):64
65. Abd Elaziz M, Bhattacharyya S, Lu S (2019) Swarm selection method for multilevel thresholding image segmentation. Expert Syst Appl 138:112818
66. Sharma K, Singh S, Doriya R (2021) Optimized cuckoo search algorithm using tournament selection function for robot path planning. Int J Adv Rob Syst 18(3):1729881421996136
67. Gao S, Wang K, Tao S, Jin T, Dai H, Cheng J (2021) A state-of-the-art differential evolution algorithm for parameter estimation of solar photovoltaic models. Energy Convers Manage 230:113784
68. Kumar A, Biswas PP, Suganthan PN (2022) Differential evolution with orthogonal array-based initialization and a novel selection strategy. Swarm Evol Comput 68:101010
69. Martin, D., Fowlkes, C., Tal, D., Malik, J.: A database of human segmented natural images and its application to evaluating segmentation algorithms and measuring ecological statistics. In: Proceedings Eighth IEEE International Conference on Computer Vision. ICCV 2001, vol. 2, pp. 416-423 (2001). IEEE
70. Chou J-S, Truong D-N (2021) A novel metaheuristic optimizer inspired by behavior of jellyfish in ocean. Appl Math Comput 389:125535
71. Zhao W, Wang L, Mirjalili S (2022) Artificial hummingbird algorithm: A new bio-inspired optimizer with its engineering applications. Comput Methods Appl Mech Eng 388:114194

72. Dehghani M, Trojovský P (2023) Osprey optimization algorithm: A new bio-inspired metaheuristic algorithm for solving engineering optimization problems. Frontiers in Mechanical Engineering 8:1126450
73. Mirjalili S, Gandomi AH, Mirjalili SZ, Saremi S, Faris H, Mirjalili SM (2017) Salp swarm algorithm: A bio-inspired optimizer for engineering design problems. Adv Eng Softw 114:163-191
74. Mirjalili S (2016) Sca: a sine cosine algorithm for solving optimization problems. Knowl-Based Syst 96:120-133
75. Ahmad MF, Isa NAM, Lim WH, Ang KM (2022) Differential evolution: A recent review based on state-of-the-art works. Alex Eng J 61(5):3831-3872
76. Jena, B., Naik, M.K., Wunnava, A., Panda, R.: A comparative study on multilevel thresholding using meta-heuristic algorithm. In: 2019 International Conference on Applied Machine Learning (ICAML), pp. 57-62 (2019). IEEE
77. Hussein WA, Sahran S, Abdullah SNHS (2016) A fast scheme for multilevel thresholding based on a modified bees algorithm. Knowl-Based Syst 101:114-134
78. Al-Rahlawee ATH, Rahebi J (2021) Multilevel thresholding of images with improved otsu thresholding by black widow optimization algorithm. Multimedia Tools and Applications 80(18):28217-28243
79. Alsahafi YS, Elshora DS, Mohamed ER, Hosny KM (2023) Multilevel threshold segmentation of skin lesions in color images using coronavirus optimization algorithm. Diagnostics 13(18):2958
80. Agrawal S, Panda R, Bhuyan S, Panigrahi BK (2013) Tsallis entropy based optimal multilevel thresholding using cuckoo search algorithm. Swarm Evol Comput 11:16-30
81. Hilali-Jaghdam I, Ishak AB, Abdel-Khalek S, Jamal A (2020) Quantum and classical genetic algorithms for multilevel segmentation of medical images: A comparative study. Comput Commun $162: 83-93$
82. Aranguren I, Valdivia A, Morales-Castañeda B, Oliva D, Abd Elaziz M, Perez-Cisneros M (2021) Improving the segmentation of magnetic resonance brain images using the lshade optimization algorithm. Biomed Signal Process Control 64:102259
83. Wang Z, Bovik AC, Sheikh HR, Simoncelli EP (2004) Image quality assessment: from error visibility to structural similarity. IEEE Trans Image Process 13(4):600-612
84. Zhang L, Zhang L, Mou X, Zhang D (2011) Fsim: A feature similarity index for image quality assessment. IEEE Trans Image Process 20(8):2378-2386
85. Aja-Fernandez, S., Estepar, R.S.J., Alberola-Lopez, C., Westin, C.-F.: Image quality assessment based on local variance. In: 2006 International Conference of the Ieee Engineering in Medicine and Biology Society, pp. 4815-4818 (2006). IEEE
86. Reisenhofer R, Bosse S, Kutyniok G, Wiegand T (2018) A haar wavelet-based perceptual similarity index for image quality assessment. Signal Processing: Image Communication 61:33-43
87. Wang Z, Bovik AC (2002) A universal image quality index. IEEE Signal Process Lett 9(3):81-84
88. Zimmerman DW (1996) An efficient alternative to the wilcoxon signed-ranks test for paired nonnormal data. J Gen Psychol 123(1):29-40

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.