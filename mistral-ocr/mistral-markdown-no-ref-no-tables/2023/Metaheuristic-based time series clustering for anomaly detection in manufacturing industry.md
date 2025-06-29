# Metaheuristic-based time series clustering for anomaly detection in manufacturing industry 

Woong Hyun Suh ${ }^{1} \cdot$ Sanghoun Oh ${ }^{2}$ (D) $\cdot$ Chang Wook Ahn ${ }^{1}$ (D)

Accepted: 26 March 2023 / Published online: 10 June 2023
(c) The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2023


#### Abstract

Nowadays time series clustering is of great importance in manufacturing industries. Meanwhile, it is considerably challenging to achieve explainable solution as well as significant performance due to computation complexity and variable diversity. To efficaciously handle the difficulty, this paper presents a novel metaheuristic-based time series clustering method which can improve the effectiveness and logicality of existing clustering approaches. The proposed method collects candidate cluster references from hierarchical and partitional clustering through shape-based distance measure as well as dynamic time warping (DTW) on manufacturing time series data. By applying metaheuristics highlighting estimation of distribution algorithms (EDA), such as extended compact genetic algorithm (ECGA), on the collected candidate clusters, advanced cluster centroid combinations with minimal distances can be achieved. ECGA employs the least complicated and the most closely related probabilistic model structure regarding population space during generation cycle. This feature strengthens the comprehension of clustering results in how such optimal solutions were achieved. The proposed method was tested on real-world time series data, open to the public, from manufacturing industry, and showed noticeable performances compared to well-established methods. Accordingly, this paper demonstrates that obtaining both comprehensible result as well as prominent performance is feasible by employing metaheuristic techniques to time series data clustering methods.


Keywords Metaheuristics $\cdot$ Time series clustering $\cdot$ Anomaly detection $\cdot$ Manufacturing industry $\cdot$ Evolutionary algorithm $\cdot$ Estimation of distribution algorithm $\cdot$ Extended compact genetic algorithm $\cdot$ Metaheuristic clustering $\cdot$ Explainable artificial intelligence

## 1 Introduction

Artificial intelligence and digital transformation are the megatrends shaping the future of the manufacturing industry. Rapid development of both information technology and operational technology are leading fast transition from traditional manufacturing process to future smart factory. Such

Corresponding authors are Sanghoun Oh and Chang Wook Ahn.
$\boxtimes$ Sanghoun Oh oosshoun@knou.ac.kr
$\boxtimes$ Chang Wook Ahn cwan@gist.ac.kr
1 AI Graduate School, Gwangju Institute of Science and Technology (GIST), Gwangju 61005, Korea
2 Department of Computer Science, Korea National Open University, Seoul 03087, Korea
transition shares the progress with technological improvements in system automation, sensor technology, cloud computing, big data processing and analysis [1, 2]. Ultimately, future smart factories will aim for remarkable advances in manufacturing productivity as well as production quality through comprehensive utilization of digital data and artificial intelligence techniques.

Especially, detecting anomalous cases in production, by analyzing massive data collected from smart sensors during the manufacturing process, is a fashionable area of research soaking up both academic and industrial interests. Recent technical advances in data processing and analysis enable detecting production losses that were unable to capture in the past. This progressive approach is where mass digital data and artificial intelligence methods converge effectively and improve the overall manufacturing productivity [3, 4]. These kinds of anomaly detectionmethods through artificial

intelligence techniques can be divided into supervised and unsupervised learning methods.

Data clustering techniques are representative unsupervised learning methods. It is specialized in grouping data that have similar features and patterns without any given data labels or tags. They have been utilized in various industries for the use of image classification, recommender systems, and anomaly detection. Deep learning, one of the representative supervised learning methods, is a pattern recognizing data analysis method that employs neural networks. Deep learning shows powerful performances in many real-world industrial domains specialized in image and video based data pattern recognitions. While neural network based methods show outstanding performances, they require a high amount of computing load and yield outcomes which have deficient analytical basis. This is because feature vectors and variables inside neural networks are tremendously huge that tracing analytical bases of the computation results is exceptionally challenging $[5,6]$.

This paper presents an effective time series clustering method highlighting estimation of distribution algorithm (EDA) for manufacturing time series data. The proposed method collects sub-clusters from both hierarchical and partitional clustering results through shape-based distance measure as well as dynamic time warping (DTW) on time series data. On the collected sub-cluster references, metaheuristic algorithms search for the most optimal cluster group. With the use of search algorithms derived from evolutionary computations, this paper proposes an explainable data clustering method for anomaly detection on manufacturing time series data with prominent performance.

This paper has three contributions. First, a novel metaheuristic-based time series clustering method for anomaly detection in manufacturing is suggested. Compared to existing time series clustering techniques, the proposed method shows noticeable performance on time series data clustering problems. Secondly, this paper elaborated the explainability of time series data clustering methods for anomaly detection. Grouping solutions with linkage information regarding the sub-cluster references are provided. Through metaheuristicbased clustering with the use of EDA, such as ECGA, the proposed algorithm derives dependent and explainable solutions which deliver logical relationships regarding how the collected clustering references have been achieved. Lastly, in order to demonstrate the applicability of the proposed method to real-world problems, this paper tested the proposed algorithm on real-world manufacturing time series data and showed the validity of its technique. This paper deems that the research in this paper can facilitate the reliable use of artificial intelligence technology as well as mass digital data in real-world industry settings.

The rest of this paper is organized as follows. Section 2 contains a brief overview and literature review on time series clustering methods as well as metaheuristic algorithms in order to demonstrate the subtle domain of metaheuristic time series clustering. Section 3 contains the proposed method of this paper which highlights the use of ECGA. Section 4 contains the experimental results and interpretations, and Section 5 includes conclusions and policy implications.

## 2 Background and related works

The scope of concepts that time series clustering as well as metaheuristics cover is extensive. In this Section, a succinct overview is provided regarding where the proposed method is placed among the two large techniques along with detailed descriptions on the methodologies that are used.

### 2.1 Time series clustering

Time series clustering techniques can be analyzed based on characteristics such as data representation, clustering techniques, evaluation criteria, and similarity measures. In respect to the huge scope that time series clustering covers, it can be classified as Fig. 1 [7, 8]. Representative time series clustering techniques, which this paper focuses on, can be divided into three methods: hierarchical clustering, partitional clustering, and model-based clustering. Being a domain of research with broad applicability, time series clustering is utilized in a large scope of academic and industrial domains, where the majority of applications are focused on time series classification as well as anomaly detection [7]. Diverse industries, which yield meaningful time series data, show active application of time series clustering, where those industries include astronomy, biology, finance, medicine, or robotics $[1-4]$.

Hierarchical clustering, for instance, assumes initial data points as individual clusters. It compares the distance between each data and successively merge or split clusters based on given distance measures. Hierarchical clustering is powerful when there is no prior knowledge about the data that it does not require a predefined number of clusters for training data. However, when time series data is large and complex, computational load increases sharply. In such cases, organized small-scale data is required in order to train within an estimable amount of computational capability [7]. Partitional clustering, on the other hand, shows rapid computation time compared to hierarchical clustering. It can be combined with fuzzy logic based algorithms for powerful performances as well. As partitional clustering requires a predefined number of clusters for data training, it lacks

Fig. 1 Time series clustering overview
![img-0.jpeg](img-0.jpeg)
analytical consistency and, similar to hierarchical clustering, requires sharp increase in computation time for analyzing huge data [7, 9]. Model-based clustering attempts to find the most optimal mathematical-fit on time series data. Modelbased clustering is a statistical, as well as neural network based, approach which operates with the rationale that there are finite mixture of underlying probability distribution that constructs the data [10]. It fundamentally assumes that time series data were previously generated by mathematical or probabilistic models.

Various research works approached to improve time series clustering techniques. Lai re-represented time series data into sub-sequences while preserving the fundamental characteristics of the data [11]. The overall sequence and sub-sequence
of time series data are considered in two different stages of time series clustering. The given algorithm used symbolic aggregate approximation to reduce data dimension, and used cluster affinity search technique for data clustering algorithm. For a similarity measure of given time series data, Lai used dynamic time warping when lengths of time series data are different and used Euclidean distance measure when the distances of time series data are identical. Munir, for instance, proposed a novel deep learning approach for shape-based time series data clustering [12]. The proposed method analyzes time series data through initially created networks as well as the closest neighboring network. Then, it creates a time series network based on Euclidean distance for similarity distance measure. Meanwhile, deep learning for time

Fig. 2 Metaheuristic overview
![img-1.jpeg](img-1.jpeg)
series classification is one of the most trending research in time series clustering. Fawaz divided deep learning methodologies for time series clustering into generative models and discriminative models; and conducted comprehensive comparison tests of deep learning models on time series data [13]. Those deep learning algorithms encompass models such as multi layer perceptrons (MLP), ResNet, Encoder, convolutional neural networks (CNN) and other prevalent algorithms. By testing such models on diverse real-world time series data - both univariate and multivariate - from devices, sensors, images, or motions; Fawaz demonstrates significant competitiveness of deep learning models in time series classification problems.

This paper employs univariate as well as raw data, which has different lengths of sequences, with shape-based distance and dynamic time warping distance measure. In order to collect candidate cluster references, partitional and hierarchical
clustering algorithms are used, which are long-standing and popular clustering algorithms not only in generic data clustering but also in time series clustering. Then, metaheuristics are utilized to search for optimal cluster centroids as well as a statistical approach to facilitate anomaly detection application. This paper compares the experiment results with other machine learning and deep learning classification methods, namely model-based clustering, to demonstrate the effectiveness of the proposed method.

### 2.2 Metaheuristics

Algorithms highly motivated by nature to solve complex realworld problems account for the substance of metaheuristrics. Many related algorithms support the large concept of metaheuristics such as evolutionary algorithms, bio-inspired algo-

Fig. 3 Simple genetic algorithm (GA) generation cycle and operators
![img-2.jpeg](img-2.jpeg)
rithms, swarm intelligence algorithms, and physics-based algorithms. As depicted in Fig. 2, the massive concept of metaheuristics can be divided into two categories: singlesolution based and population-based approaches [14, 15]. Single-solution based metaheuristic algorithms, such as tabu search (TS) or microcanonical annealing (MA), concentrate on improving single candidate solutions through local search. This relates to the main weakness of such algorithms that the best solution may be stuck in local optima. Population-based metaheuristic algorithms, on the other hand, utilize multiple candidate solutions in order to search for the most optimal solution. This feature makes population-based methods, such as genetic algorithm (GA) or particle swarm optimization (PSO), much more advantageous in searching for global optima compared to single-solution based approaches.

Inspired by Darwin's natural selection theory, genetic algorithm (GA) is one of the most well-known evolutionary algorithms which emulates Darwin's idea of survival of the fittest [16, 17]. GA functions with elements such as chromosome representation, fitness selection, and bio-inspired operators. The bio-inspired operators can be specified into gene (or chromosome) encoding, selection, crossover and
mutation, like the process of reproducing next generation offspring in nature. In GA, population is the search space, namely the set of candidate chromosomes, to find the most optimal solution. Here, GA, as well as other evolutionary algorithms, requires specific techniques in each component such as binary encoding, tournament selection, uniform crossover or displacement mutation; and predefined parameters such as fitness function, mutation and crossover rates. The overall cycle of simple genetic algorithms and operators is as described in Fig. 3 [18].

One of the representative swarm intelligence algorithms is particle swarm optimization (PSO) algorithm. Simulating the social behaviors of organisms such as birds or fishes, PSO aims to search for the most optimal solution by employing particles, similar to chromosomes in GA, on population space according to stochastic formulas on their position and velocity [19-21]. Each particle position is considered as a candidate solution for the target problem and the rate of change in position is treated as velocity. The position giving the best fitness value is stored as the best particle for the most optimal solution. Binary particle swarm optimization (BPSO) algorithm is PSO operating with binary variables,

Fig. 4 Extended compact genetic algorithm (ECGA) outline
![img-3.jpeg](img-3.jpeg)

namely binary encoding, on population space where individuals are represented by binary bits [22, 23]. PSO, as well as BPSO, has advantages of computational efficiency, robust control parameters, and easy computation [20, 24]. At the same time, PSO algorithms may have low convergence rate and may fall into local optima easily for high-dimensional problems.

Estimation of distribution algorithm (EDA) is a probabilistic optimization approach that searches for best solutions in population space through stochastic models [25]. The main characteristic of EDA that differs from other metaheuristics is that EDA attempts to build probabilistic models towards promising solutions based on trending distribution of selected solutions from previous generations. While EDA possesses high efficiency and applicability with trade-offs in computational complexities depending on the target problem that one aims to solve; as Hauschild and Pelikan suggested, EDA algorithms have strengths in not only solving difficult problems, but also in showing how such problems were solved [26]. This paper refers to the described aspects of EDAs to the artificial intelligence domain in order to enhance logical comprehension of data training outcomes.

Additionally, EDAs can be categorized into univariate models, which assume problem variables are independent of any other variables, and multivariate models, which capture correlated interactions among problem variables. Compact genetic algorithm (CGA) is an incremental univariate EDA which resembles population-based incremental learning (PBIL) [27-29]. Unlike other EDAs bequeath population space successively to the next generation, incremental EDAs replace population based on stochastic models derived from the previous generation. CGA and PBIL use probability vectors in order to represent the entire solutions in population space where fixed-length binary strings are used for encoding. While PBIL changes entire probability vectors in each generation, CGA changes probability vectors when only there exists a winning solution in each generation.

Extended compact genetic algorithm (ECGA), one of multivariate EDAs, was proposed by Harik with a key idea that choosing a good probability distribution over population space shall be equivalent to linkage learning in genetic algorithm (GA) [30-33]. Linkage learning in GA highlights building blocks of chromosomes that should be conserved under crossover operation for effective search of optimal solution. Here, quantifying the quality of a distribution is determined by minimum description length (MDL) models. When all things are equal, MDL models assume that simpler distributions are better than complex ones. Using MDL models, both inaccurate and complex models are penalized which results in an optimal probability distribution. This probability distribution is one of a class of marginal product models (MPM). MPMs in CGA and PBIL are measured as a prod-
uct of marginal distributions on singular gene partition; on the other hand, MPMs in ECGA represent the probability distributions for multiple genes simultaneously. The overall process of ECGA is depicted in Fig. 4, and simple pseudooutline of ECGA is as below [34]:

1. Initialization: create population randomly or use other initialization methods.
2. Fitness: evaluate fitness values of individuals in the population based on fitness function.
3. Selection: choose individual chromosomes through methods such as tournament selection or other selection procedures.
4. Build the probabilistic model: ECGA searches for both the structure and the parameters of probabilistic models. ECGA selects the model with lowest combined complexity and replaces it if there is a better one compared to previously selected model.
5. Create new individuals: produce new individuals by sampling probabilistic model on population.
6. Replace the parental population with the offspring population.
7. Repeat steps 2-6 until a convergence criteria is met.

In ECGA, marginal product models (MPMs) using minimum description length (MDL) models as well as creating new populations based on the probabilistic model are the core elements. This can be described as below.

Minimize: $\quad C_{m}+C_{p}$
Subject to: $\quad 2^{l_{b b, i}} \leq N_{p} \quad \forall i \in\left[1, N_{b b}\right]$
In equations from (1) to (4), $C_{m}$ represents model complexity, namely the cost of a complex model, and $C_{p}$ is the compressed population complexity, namely the cost of using a simple model compared to using a complex model [31].

$$
\begin{gathered}
C_{m}=\log _{2}\left(N_{p}+1\right) \sum_{i=1}^{N_{b b}}\left(2^{l_{b b, i}}-1\right) \\
C_{p}=\sum_{i=1}^{N_{b b}} \sum_{j=1}^{2^{l_{b b, i}}} N_{i j} \log _{2}\left(\frac{N_{p}}{N_{i j}}\right)
\end{gathered}
$$

$N_{p}$ is the size of population and $N_{b b}$ represents the number of building blocks. $l_{b b, i}$ is the length of building blocks, where $i \in\left[1, N_{b b}\right]$, and $N_{i j}$ is the number of chromosomes in the current population space possessing bit-sequence $j \in$ $\left[1,2^{l_{b b, i}}\right]$ for building block $i$. With optimal MPM calculated, a new population is filled with best individuals by size of $N_{p} *\left(1-P_{c}\right)$, where $P_{c}$ is the crossover probability. These

subsets are the groups identified by the MPM models and the rest individuals are generated randomly.

This paper highlights the use of EDA, especially ECGA, on time series clustering techniques. While application of metaheuristics on time series clustering is considered to be very few, evaluating time series clustering techniques based on the use of optimization methods has been concentrated on algorithms based on GA and PSO [8, 35]. The use of a probabilistic model, such as ECGA, in optimizing time series clustering techniques is considered to be unprecedented. This paper expects that the proposed method will enhance the understanding of data analysis results in the artificial intelligence domain regarding real-world problem solving.

### 2.3 Metaheuristic-based clustering

In this paragraph, the subtle domain of metaheuristic-based clustering techniques is briefly examined. Efficient search and effective optimization are the main aspects that data clustering methods adopt from metaheuristics, in order to overcome limitations such as inefficiency in distance measure or computational complexity [8]. Recent algorithms which advance the technical capacity of metaheuristics include red fox optimization algorithm, adopting the model of red fox habits, as well as polar bear algorithm, adopting polar bear's survival mechanism [48, 49]. There are various convergences betweenmetaheuristic algorithms and

Time series data
Image of random samples from raw and unlabeled time series data
![img-4.jpeg](img-4.jpeg)

New time series clustering results
![img-5.jpeg](img-5.jpeg)

Anomaly detection application
![img-6.jpeg](img-6.jpeg)

Fig. 5 Illustration of the proposed metaheuristic-based time series clustering method

clustering techniques. For instance, metaheuristics can be used to search for the most appropriate fixed-number of cluster centers by optimizing the initialization process, and to enhance the effectiveness of distance measures, or to reduce dimensions in time series data representation [36, 37]. Accordingly, deep learning methods, such as deep autoencoder networks, can be optimized with genetic algorithms for time series data clustering [38]. Recent relevant research includes short-term forecasting models with hybrid use of machine learning methods and support vector regression with grey catastrophe and random forest [50]. Real-world applications of metaheuristic clustering include distributed denial of service (DDoS) detection in order to protect network in cyber security, healthcare data collection in mobile wireless multimedia sensor networks, hybrid time series clustering based on evolutionary algorithms with pearson distance measure for manufacturing time series data, and evolutionary computation based manufacturing big data analysis [39-42]. The proposed method of this paper intends to expand both the theoretical utilization as well as the range of application of metaheuristics for time series clustering techniques.

## 3 Proposed method

The proposed framework can be divided into two steps: time series clustering stage and metaheuristic optimization stage. The main idea of the proposed method is to find the most optimal cluster combinations from the cluster candidate pool, with analytical bases, for the purpose of applying clustering results to anomaly detection. The overall process is depicted in Fig. 5 and the flowchart is described in Fig. 6. The algorithm aims to find optimal cluster centroids with shorter distances, namely advancing the existing clustering results, on time series data. Also, The proposed method derives how such a solution has been achieved, by highlighting ECGA, to deliver analytical substance for clustering results.

The initial stage of the proposed method begins with processing various types of time series clustering techniques on raw and unlabeled time series data. Primarily, it expands the pool of potentially best clusters by collecting time series clustering results. In the proposed framework, diverse time series clustering techniques as well as distance or similarity measures can be used to provide potential cluster references. In this paper, the mixture of long-standing and effective time series clustering techniques are used: k-means and hierarchical clustering with shape-based distance (SBD) and dynamic time warping (DTW).

One of the most popular distance measures in time series sequences shall be DTW [43, 44]. DTW can be thought of as an extended approach from Euclidean distance (ED). DTW is effective when time series sequences vary in time or speed.
![img-7.jpeg](img-7.jpeg)

Fig. 6 Flowchart of the proposed metaheuristic-based time series clustering algorithm

Through warping path $W=w_{1}, w_{2}, \ldots, w_{k}$, with $k>=m$, achieved from $m$ by $m$ matrix M with ED between any two points of two time series sequence vectors; DTW maps two sequence vectors in the case where lengths of two sequences differ. This path is evaluated through the following recurrent equation of evaluation, $\gamma(i, j)$, which can be computed through dynamic programming. In many cases, the model can be constrained to visit only a limited subset of the warping path on matrix M for practical computation.

$$
\begin{aligned}
& E D(\vec{x}, \vec{y})=\sqrt{\sum_{i=1}^{m}\left(x_{i}-y_{i}\right)^{2}} \\
& D T W(\vec{x}, \vec{y})=\min \sqrt{\sum_{i=1}^{k} w_{i}} \\
& \gamma(i, j)=E D(i, j)+\min \{\gamma(i-1, j-1), \gamma(i-1, j), \gamma(i, j-1)\}
\end{aligned}
$$

SBD is a distance measure based on normalized crosscorrelation proposed by Paparrizos and Gravano for time series clustering method called k -shape clustering algorithm [45]. SBD uses distance measure through cross-correlation which can be thought of as time lagged correlation. For time series sequences that differ in length, SBD adds zero paddings to match the length of sequences. Then, SBD calculates ED to find maximal similarity by crosscorrelation. In order to enhance the performance of SBD, employing z-normalization is a common case to match the scale of time series sequences. With time series sequence vectors $\vec{x}_{(s)}$, where $s \in[-m, m]$, SBD creates crosscorrelation $C C_{w}(\vec{x}, \vec{y})=\left(c_{1}, \ldots, c_{w}\right)$, which the length is $2 m-1$. The cross-correlation is defined as $C C_{w}(\vec{x}, \vec{y})=$ $R_{w-m}(\vec{x}, \vec{y}), w \in\{1,2, \ldots, 2 m-1\}$, where $R_{w-m}(\vec{x}, \vec{y})$ is computed as:

$$
R_{k}(\vec{x}, \vec{y})=\left\{\begin{array}{lr}
\sum_{i=1}^{m-k} x_{i+k} \cdot y_{i}, & k \geq 0 \\
R_{-k}(\vec{y}, \vec{x}), & k<0
\end{array}\right.
$$

Then, SBD can be derived as:

$$
S B D(\vec{x}, \vec{y})=1-\max _{w}\left(\frac{C C_{w}(\vec{x}, \vec{y})}{\sqrt{R_{0}(\vec{x}, \vec{x}) \cdot R_{0}(\vec{y}, \vec{y})}}\right)
$$

After computing clustering results, the proposed method finds the optimal number of clusters in each given clustering result using Silhouette analysis as cluster validity index [46]. Silhouette index is a method used for validating consistency within clusters of data. The silhouette value is a measure of
how similar an object is to its own cluster in comparison to other clusters. This can be achieved by calculating silhouette index for each sample, average silhouette index for each cluster, and overall average index for a dataset. The coefficient is calculated by utilizing mean intra-cluster distance (a) and the mean nearest-cluster distance $(b)$ for each sample.

Silhoutte index $=\frac{b(i)-a(i)}{\max \{a(i), b(i)\}}$
The silhouette index is defined as equation (10) which $a(i)$ is the average dissimilarity of $i^{t h}$ sample to all other samples in the same cluster and $b(i)$ is the average dissimilarity of $i^{t h}$ sample with all samples in the closest cluster. The index value lies between $[-1,1]$. If the value is close to 1 , the sample is well-clustered; if the value is close to 0 , the sample can be assigned to a different cluster; and if the value is close to -1 , the sample is in the wrong cluster. By using silhouette width as cluster validity index, the proposed method finds and collects cluster centroids in order to make candidate references for optimal clusters.

Based on the collected candidate cluster references, the proposed method searches for the most optimal cluster centroid combinations through metaheuristics. By considering given candidate centroids for the population pool, metaheuristic algorithms search for the best cluster combination through a binary encoded chromosome. In other words, the size of the population is $2^{n}$, where n is the length of cluster references that may differ based on previous clustering results. Accordingly, clusters represented as " 1 " are considered for fitness value calculation, and clusters represented as " 0 " are neglected for fitness value calculation. Both the length of the chromosome and the number of each clustering method in the chromosome vary according to the clustering results from the previous step.

For metaheuristic optimization, this paper employed GA, CGA, BPSO, and ECGA based on binary encoded chromosomes with tournament selection and average-max fitness function to find the most well-clustered centroid combinations. As mentioned in Section 2.2, many uses of metaheuristics in time series clustering techniques are focused on GA and PSO algorithms, and the use of EDAs such as CGA and ECGA in time series clustering is considered to be very few. Compared to other algorithms, ECGA holds a distinctive characteristic delivering how the algorithm has achieved such solutions by grouping population through probabilistic models which highlight trending as well as relevant candidates in population pool.

ECGA induces the search process in every generation cycle to find least complicated and most closely related probabilistic model structure on population space to partition

selected population and fit parameters. In other words, as the chromosome is considered to be the collected references of diverse time series clustering results, by searching optimal combinations and providing logical bases, enhancing performances and having explainable relationships among clusters are feasible simultaneously. This feature of EDA, concretely ECGA, draws logical solutions for data analysis.

Through metaheuristics, newly optimized time series clustering centroids derived from previously computed time series clustering methods are achieved. With given new time series clustering results, this paper applies them for anomaly detection. Each test data input is checked with the distance in respect to each cluster. If the distance is outside the threshold interval, it is considered as abnormal, and if the distance is within the threshold interval it is considered as normal. This paper refers to the statistical approach for building threshold intervals. More detailed descriptions on the overall framework can be found in Algorithms 1 and 2 as well as Section 4

This paragraph summarizes the main features of the proposed method. One of the main characteristics of the proposed research is that the input data for this framework is raw and unlabeled. Data does not need to be labelled to discern clusters among data, unlike supervised learning. Also, as long-standing clustering approaches require iterative experiments for optimal solutions or prior knowledge to set a predefined number of clusters, this paper proposes metaheuristic-based clustering method which collects clustering references to find the most optimal clusters. In addition, to the knowledge of this paper, there are no existing approaches that link or group candidate clusters by probabilistic models to find dependent and explainable solutions. These features enable analyzing time series data without prior knowledge as well as delivering explainable solutions, while maintaining outstanding performances.

## 4 Experimental results

### 4.1 Experiment setup

The proposed clustering framework is demonstrated on realworld collected time series data from the manufacturing process. The data, contributed by Olszewski, comprises a collection of in-line process-control measurements recorded from various sensors during etch processing of silicon wafers for semiconductor fabrication [47]. There are six data types, each set in the database contains measurements by one sensor during processing one wafer. Those sensors include radio frequency forward power sensor, radio frequency reflected power sensor, chamber pressure sensor, 405 nm emission sensor, 520 nm emission sensor, and direct current bias sensor. Each data is treated as signal one to six respectively in

Algorithm 1 Metaheuristic-based time series clustering framework

```
Require: maximum cluster range number \(K\), population rate \(r\),
fitness function \(f\), crossover rate \(c\), tournament size \(t\), selection
size \(s\)
```

Initialization: compute various types of time series clustering (optional) normalize time series data, if needed

1. partitional clustering $2: \mathrm{K}$ with DTW
2. hierarchical clustering $2: \mathrm{K}$ with DTW
3. partitional clustering $2: \mathrm{K}$ with SBD and DTW
4. hierarchical clustering $2: \mathrm{K}$ with SBD and DTW
find tentatively optimal clusters with Silhouette index
collect cluster centroids as candidate references
Optimization: metaheuristic search by ECGA population size $=\mathrm{r} *$ (cluster candidate length) max generation $=1.5 *$ sqrt(population) chromosome size $=$ length of candidate references tournament size $=\mathrm{t}$
selection size $=\mathrm{s}$
initialize population
set fitness value of population
calculate initial model with beginning population
while $i<$ max generation do
model = marginal_product_model(population, model)
$\triangleright$ Algorithm 2
new_model = link_group(model)
if new_model has converged then
break;
else
model $=$ new_model;
end
offspring = shuffle(population, model)
population_pool = tournament_selection( $\mathrm{t}, \mathrm{s}$, offspring)
evaluate $=$ fitness_function(population_pool)
$\mathrm{i}+=1$
end
Application: anomaly detection test
set threshold interval based on optimization results
interval = mean clustering result $+-2$ or 3 sigma values
if test data is within interval then
normal;
else
abnormal;
end

Algorithm 2 Marginal product model
Minimum Description Length (MDL): compute model and population complexity
$N_{P}=$ size of population
$L=$ list of building block lengths
$C_{m}=\log _{2}\left(N_{p}+1\right) * \operatorname{sum}\left(2^{L}-1\right)$
for $i$ in number of building blocks do
$l_{i}=$ length of building block $i$
for $j$ in $2^{L}$ do
$N_{l_{j}}=$ number of chromosomes in current population
where $j \in\left\{1,2^{L}\right\}$
$C_{p}=\operatorname{sum}\left(N_{l_{j}} * \log _{2}\left(N_{p} / N_{l_{j}}\right)\right)$
end
end
$\operatorname{mdl}=C_{m}+C_{p}$

this paper, and each wafer in the dataset has an assigned classification as normal or abnormal. The sample cluster shapes of six signal data can be found in Fig. 7. In order to investigate the validity of clustering results among time series clustering techniques, the proposed clustering method is demonstrated by using classified normal data only in each signals; and, for anomaly detection application, an undifferentiated whole time series data without distinction of signals is used.

The experiment environment is as follows. Computing power used in this paper is AMD Ryzen 55600G Radeon Graphics 3.90 GHz with 16.0 GB of RAMs. Main code language used in this paper is R, with Python assisting for partially efficient computations. One NVIDIA GeForce GTX 1070 Ti graphic card is used in computing other deep learning algorithms for anomaly detection result comparison. For metaheuristic algorithms, the proposed method had population size rate, $r$, population size, $p$, and max generation. Max generation as well as population size can be chosen with no limitation with the cost of computational time. In this paper, $r$ is $15, p$ is candidate length $* r$, and max generation is 1.5
$* \sqrt{p}$. Also, the proposed method utilizes tournament selection for selection strategy, mutation rate of 0.8 and crossover rate of 0.1 . Each type of data was sampled with both $75 \%$ and $25 \%$ random data sample rate and this paper verified that the method works properly regardless of data sampling bias. For clustering validity experiment, the data were normalized using $z$-score, which is $(x-\mu) / \sigma$, within given time series data set, when $\mu$ is mean and $\sigma$ is standard deviation. On the other hand, the whole data were not normalized for anomaly detection in order to compare with other time series classification methods.

### 4.2 Experimental results and interpretation

On univariate and raw time series data, four time series clustering techniques as well as four metaheuristic algorithms are used. First, as described in Section 3, hierarchical and partitional clustering with DTW, and two additional hybrid clustering approaches which include SBD prior to DTW are
![img-8.jpeg](img-8.jpeg)

Fig. 7 Cluster shape samples of six signals

obtained for experimental comparison. Four types of clustering techniques are abbreviated as H, P, HH and HP; which represent hierarchical (H), partitional (P), hybrid hierarchical $(\mathrm{HH})$ and hybrid partitional (HP). In order to propose a fundamental framework for metaheuristic-based time series clustering, this paper used K-means and hierarchical clustering techniques as referential time series clustering methods as they are one of the most common, basic, and efficient methods used widely. The time series clustering techniques in the proposed method can be altered freely to other techniques based on a researcher's preferences or insights. Maximum cluster number used in this experiment is 5 . Each clustering methods searches for clusters from 2 to 5 , and maximum cluster candidate length will be $4 * 5$, which is 20 . The proposed method assumes there is no previous knowledge regarding time series data so that max number of clusters can be adjusted freely and it does not have to be strictly determined before implementation. Four metaheuristics used in this paper include GA, BPSO, CGA and ECGA. The proposed method optimizes four types of clustering results by searching for better, or the best, cluster centroid combinations. In other words, the proposed framework performs various clustering techniques to expand the optimal cluster candidate pool then optimizes cluster centroid combinations using metaheuristics.

Tables 1, 2, 3, 4 and 5 show the experimental results. The experiment dataset is divided into two parts by data sample rate. In the beginning of each experiment iterations, the training data is divided into two subsets with random sample rate $25 \%$, and $75 \%$. This paper experimented the entire method 100 times for both sample rates, consequently a total of 200 iterations. Results are measured in the total average out of 100 iterations in each sample rate. The numerical values are DTW distances of each test data calculated with cluster
centroids in each method. The smaller values are the better ones. Signals 2 and 6 have spiking fluctuations, and this characteristic results in longer distances and less variation. In general, this paper demonstrates that four metaheuristic methods are capable of searching for optimal clusters. While there were subtle differences in performance among metaheuristic methods, CGA and BPSO tended to converge late resulting in slightly higher distance compared to GA and ECGA.

One of the weaknesses of the proposed approach, with ECGA, is the computational burden. In Table 1, the average of total computation time of each metaheuristics from 100 iterations is described. Although time measurement can differ by coding language or code syntax, there are distinct differences in runtime among metaheuristic methods. It can be said that the computational time is fastest in the order of CGA, BPSO, GA and ECGA. With respect to the results shown in Tables 4 and 5, while CGA is the fastest metaheuristic method, there are many cases where CGA fails to find optimal solutions compared to other methods. While ECGA is considered to be the slowest method for searching optimal solutions, this paper highlights ECGA due to its advantages of effective search capability as well as logical search techniques. Comparing the convergence rate of metaheuristics algorithms, this paper suggests that CGA showed deficiency in performance. Comparing the performance of metaheuristics may differ by the problem one aims to solve or by the characteristics of the data one attempts to use. Within the scope of optimizing the clustering result using time series data originated from the manufacturing process, GA, BPSO and ECGA showed near performance with negligible amount of difference. With strict comparison, the performance is better in the order of GA, ECGA and BPSO which can also be seen in Tables 4 and 5. While CGA, one of EDA, shows rapid computation time

Table 1 Metaheuristics computation time average (in seconds) of 100 iterations

Table 2 ECGA model samples
compared to the other three algorithms, this paper suggests that CGA holds a weakness that it requires more time to converge or may fail to find the most optimal solution compared to the metaheuristics used in this paper. In Figs. 8 and 9, this can be seen clearly. The figures show the initial 15 generation cycle to compare the converging performances. ECGA and GA tend to search for better initial fitness values compared to the other two.

Table 2 shows ECGA model examples sampled from the first five iterations of the experiment with data sample rate $25 \%$. The lengths of each chromosomes are different because optimal cluster candidates from the previous step vary based on the time series clustering results. The concept of proba-
bilistic model used in ECGA can be summarized as creating partitions in population space for selecting better chromosomes. For example, if a binary chromosome with length of 8 is partitioned as [1], [0,3], [2,4,6], [5,7]; there are 4 model blocks. The bits inside each block are considered to be jointly distributed, while the sole bit is considered to be independently distributed. In other words, cluster centroids located in the 0th and 3rd place in the binary chromosome are highly related and are jointly distributed in the population space. This probabilistic model is used for selecting a new population, namely chromosomes, for the next generation cycle for searching for better, or the best, gene that returns the highest fitness value.

Table 3 ECGA model dependency index

Table 4 Total average of 100 iterations with $25 \%$ sample rate

Table 5 Total average of 100 iterations with $75 \%$ sample rate

![img-9.jpeg](img-9.jpeg)

Fig. 8 Fitness function convergence graphs of initial 15 generations - $25 \%$ data sample rate
![img-10.jpeg](img-10.jpeg)

Fig. 9 Fitness function convergence graphs of initial 15 generations - $75 \%$ data sample rate

As mentioned above, signal 2 and 6 have traits of spiking fluctuations. This can also be inferred from the ECGA model results. Time series data with high variance means less cluster coherence. The length of chromosomes of signal 2 and 6 tends to be shorter than other signals, which means that there has been found less number of cluster candidates among time series clustering results. In addition, both signals show a relatively high number of model blocks compared to other signals. This is because, as there are fewer cluster candidates, there are comparably high number of similar (or jointly related) clusters within the chromosome. In other words, less cluster coherence with a smaller number of cluster candidates resulting into highly related clusters within limited candidate pools.

This logical reasoning can be numerically described as Table 3. Numerical values presented in the table are calculated by dividing the total sum of chromosome lengths with the total sum of number of model blocks in each signal data out of 100 iteration experiments. This paper describes this value as ECGA model dependency index. Higher values can be interpreted as there are relatively more dependent binary bits within chromosomes or, at the same time, shorter lengths of chromosomes have been created. As signal 2 and 6 are time series data which possess spiking traits compared to other signals, both of the signal data show a high number of model dependency index. Because signal 2 and 6 are comparably difficult to cluster the data, less number of promising clusters have been created as candidate clusters, and the cluster candidates show high dependency to each other due to less number of trending cluster centroids within chromosomes. Such numerical analysis as well as analytical reasoning are the unique characteristics of ECGA that differs from other algorithms. This feature of ECGA enhances the comprehension of data analysis results.

### 4.3 Anomaly detection investigation

Time series clustering, or time series classification, is highly correlated to anomaly detection. In the generic data analysis domain, including machine learning and deep learning, data clustering discovers the features and patterns from the train data. Hence, discerning anomalous cases among test data based on the clustering results is an inseparable twinlike mission to accomplish in data clustering. By inheriting the previous results from metaheuristic based time series clustering, the proposed method is employed to time series data anomaly detection through statistical tests for application purpose. Therefore, the proposed method is compared with other machine learning and deep learning techniques in detecting anomalous cases from time series data. The machine learning and deep learning methods used in this paper for comparison include - logistic regression (LR),

XGBoost (XGB), fully connected layer (FCN), multilayer perceptron (MLP), ResNet, and long-short term memory (LSTM). The data used for the anomaly detection comparison test are time series data from semiconductor and automotive industries named as wafer, FordA and FordB.

Data used for anomaly detection is - combined, raw, and whole time series data - identical for all methods. Rather than dividing the time series data by sensors as in the previous clustering experiment, all time series data is gathered as one whole data set with labels in each data row as normal or abnormal. The wafer data has 6,165 rows of train data and 1,000 rows of test data with sequence lengths of 152 . FordA has 3,601 rows of train data and 1320 rows of test data with sequence length of 500 ; and Ford B has 3,636 rows of train data and 810 rows of test data with sequence length of 500 . The wafer time series data is identical from the previous sections except they are gathered and labeled as a whole dataset. Unlike machine learning or deep learning methods, the proposed method does not use the labels for data training. The proposed method tests anomaly detection based on the labeled test data after discovering clusters out of raw whole data. This holds the same for FordA and FordB dataset, which the data was originally used in a competition in the IEEE World Congress on Computational Intelligence, 2008. All three datasets can be found on UCR/UEA time series data archive.

Table 6 is the result of anomaly detection comparison of machine learning, deep learning, and the proposed method. Accuracy is calculated as dividing the number of correct predictions - aggregation of true positives and true negatives - by the number of total predictions. The results are the average accuracy from 10 iterations. For anomaly detection, statistical confidence interval test is used in this paper. Based on the optimization results, confidence intervals are calculated based on the three-sigma rule (68-95-99.7 rule). This follows the statistical hypothesis that 68 percent of the data will lie within mean value plus and minus one standard deviation $(\sigma), 95$ percent of the data within mean value plus and minus two $\sigma$, and 99 percent of the data within mean value plus and minus three $\sigma$.

While the wafer dataset is relatively monotonous compared to the FordA and FordB dataset, both Ford dataset possess large amounts of noise in data. The overall average accuracy for the wafer dataset is the highest and the overall average accuracy for the FordB dataset is the lowest. The table shows that, compared to long-standing machine learning algorithms such as regressions or tree search algorithms, metaheuristic time series clustering methods show prominent performances. While the metaheuristic based time series clustering method shows deficient performance compared to prevailing deep learning techniques such as LSTM or ResNet; the proposed approach possesses a distinctive advantage of logical bases on understanding data analysis results

Table 6 Anomaly detection accuracy (\%) comparison

with significant level of performance compared to black-box based neural network models.

This paper shows that the proposed method shows noticeable performances compared to other time series techniques. With the combined use of long-standing time series clustering techniques, the metaheuristic based method surpassed $90 \%$ accuracy with a $3 \sigma$ confidence interval for wafer data. With meaningful figures of performance, the proposed approach possesses a significant advantage of logical bases on understanding data analysis results. This feature of the proposed method makes the difference compared to other artificial intelligence techniques which mainly adopt blackbox based neural network models as well as a considerable amount of complex variables.

## 5 Conclusion

This paper proposed a novel time series clustering framework employing metaheuristics, especially the estimation of distribution algorithm (EDA). Most data analysis techniques affiliated with the artificial intelligence domain include characteristics of deriving features and patterns among numerous amounts of data. Meanwhile, reasoning out logical substance from astronomical numbers of variables and parameters in artificial intelligence models is significantly challenging. Accordingly, the recent trend in artificial intelligence stresses about the importance of explainability regarding data analysis results.

With the combined use of time series clustering techniques as well as metaheuristic algorithms, this paper demonstrated logical outcomes from the data analysis results through employing extended compact genetic algorithm (ECGA). By expanding the cluster candidate pool with various types of time series clustering methods, the proposed method searched for the most optimal cluster centroids combination using evolutionary algorithms. Particularly, ECGA is specialized in providing how such a solution is derived based on proba-
bilistic models during the generation cycle. In other words, model blocks enable tracing back the cluster combination outcomes and interpreting the data analysis results as well.

Based on the optimized time series cluster centroid combinations, the proposed method applied them for effective use on anomaly detection in manufacturing time series data. The proposed approach showed meaningful performance compared to other machine learning and deep learning time series classification techniques. We reckon that our proposed research has advantages of not only an outstanding performance in anomaly detection application but also a logical background for data analysis results. In real-world use of data analysis in manufacturing industries, the analytical description as well as logical background regarding data training outcome is essential for robust utilization of mass data and artificial intelligence techniques.

Explainable relationship among clusters is what this paper mainly contributes in advancing the time series clustering techniques as well as extending the use of artificial intelligence methods in real-world settings. In future research, we expect to apply the advantage of metaheuristics, especially estimation of distribution algorithms (EDA), to other complex algorithm-based data analysis models such as reinforcement learning or graph neural networks. As they require a significant amount of computation complexity as well as variable diversity, there is recent research focusing on improving overall performance and efficiency of graph neural networks through various mathematical and statistical approaches [51, 52]. Furthermore, we plan to conduct future research on the proposed method for the performance change based on the change of maximum cluster number as well as the performance change based on the change of time series clustering techniques. We expect metaheuristics such as EDA will be effective not only in optimizing challenging problems but also delivering logical substances regarding causal comprehension on data analysis results.

Funding This work was supported by IITP grant funded by the Korea government (MSIT)(No. 2019-0-01842, Artificial Intelligence

Gradate School Program (GIST)), and the National Research Foundation of Korea(NRF) funded by the Ministry of Education (NRF2021R1A2C3013687)

## Declarations

Conflict of Interests The authors declare no conflict of interest
