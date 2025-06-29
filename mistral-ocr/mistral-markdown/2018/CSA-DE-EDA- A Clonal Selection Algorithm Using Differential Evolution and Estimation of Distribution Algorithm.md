# CSA-DE/EDA: A Clonal Selection Algorithm Using Differential Evolution and Estimation of Distribution Algorithm 

Zhe $\mathrm{Li}^{1}$, Yong Xia ${ }^{1,2(\square)}$, and Hichem Sahli ${ }^{2,3,4}$<br>${ }^{1}$ Shaanxi Key Lab of Speech and Image Information Processing (SAIIP), School of Computer Science and Engineering, Northwestern Polytechnical<br>University, Xi'an 710072, China<br>yxia@nwpu.edu.cn<br>${ }^{2}$ Centre for Multidisciplinary Convergence Computing (CMCC), School of Computer Science and Engineering, Northwestern Polytechnical University, Xi'an 710072, China<br>${ }^{3}$ Audio Visual Signal Processing (AVSP), Department of Electronics and Informatics (ETRO), Vrije Universiteit Brussel (VUB), VUB-ETRO, Pleinlaan, 2, 1050 Brussels, Belgium<br>${ }^{4}$ Interuniversity Microelectronics Center, Kapeldreef 75, 3001 Leuven, Belgium


#### Abstract

The clonal selection algorithm (CSA), which describes the basic features of an immune response to an antigenic stimulus, has drawn a lot of research attention in the bio-inspired computing community, due to its highlyadaptive and easy-to-implement nature. However, despite many successful applications, this optimization technique still suffers from limited ability to explore the solution space. In this paper, we incorporate the differential evolution (DE) and estimation of distribution algorithm (EDA) into CSA, and thus propose a novel bio-inspired computing algorithm called CSA-DE/EDA. In this algorithm, the hypermutaion and receptor editing processes are implemented based on DE and EDA, which provide improved local and global search ability, respectively. We have applied this algorithm to brain image segmentation. Our comparative experimental results suggest that the proposed CSA-DE/EDA algorithm outperforms several bio-inspired computing techniques on the segmentation problem.


Keywords: Bio-inspired computing $\cdot$ Clonal selection algorithm (CSA) Differential evolution (DE) $\cdot$ Estimation of distribution algorithm (EDA) Image segmentation

## 1 Introduction

Optimization problems are commonly studied in almost every field of engineering for effective and efficient solutions [1]. Despite their wide-spread applications, traditional optimization algorithms, such as the gradient descent [2], pose many constraints on the objective function, including convexity, continuity, derivability and unimodality,

which, unfortunately, are not always satisfied in most real-life problems [1]. With the explosive growth of computational power, bio-inspired computing techniques, which are capable of imitating the key principles in nature, such as the natural selection and clonal selection, have been applied to several optimization problems. These techniques are highly-adaptive and easy-to-implement, and pose less constraints on the objective function [3].

There are two important categories of bio-inspired computing techniques: evolutionary algorithms and swarm intelligence [4]. As one of the most prevalent evolutionary algorithms, the genetic algorithm (GA) uses heuristics-guided search that simulates the process of natural selection and survival of the fittest, and generates the next population of solutions via performing a combination of genetic operators on the current population, including selection, crossover and mutation, which enable GA to adapt to the changing environments. Although GA has the potential to search the global optimal, it often falls into local optima due to the limited runtime [3].

To improve the performance of GA, many enhancements have been proposed. Among them, the differential evolution (DE) [3] and estimation of distribution algorithm (EDA) [5] are two of the most well-known algorithms. DE generates the trial individuals by perturbing existing individuals with the scaled difference between two randomly selected individuals [6]. It has proven itself in competitions and a variety of real applications by producing more accurate results than several other optimization methods including GA, simulated annealing and evolutionary programming [7]. EDA, also known as the probabilistic model-building genetic algorithm, replaces the crossover and mutation operators with learning and sampling from the solution distribution in generating new offspring [8]. The advantages of EDA include the expressiveness and transparency of the probabilistic model that guides the search process, the absence of multiple parameters to be tuned, compact representation and the ability to avoid premature convergence. EDA has been proven to be better suited to some applications than GAs, while achieving competitive and robust results in the majority of the tackled problems [9].

As a well-known paradigm in swarm intelligence [4], the artificial immune system (AIS) [10] has drawn a lot of research attentions recently. Many AIS algorithms are designed to solve multimodal function optimization problems via mimicking the behavior of living organisms in protecting themselves against antigens. Inspired by the clonal selection principle of acquired immunity that explains how B and T lymphocytes improve their response to antigens over time [11], De Castro and Von Zuben [11] developed the clonal selection algorithm (CSA), which has shown superior performance compared to several other bionic algorithms and traditional optimizing mechanisms in a variety of applications [11, 12]. CSA is designed to simulate the affinity maturation process based on the clonal selection theory, which claims that only those cells that recognize the antigens will be selected to proliferate, and these cells will improve their affinity through an affinity maturation process [13].

Despite its success and prevalence, CSA can be further improved [14]. A good optimization algorithm should use both the local information around the current solutions and the global information about the search space [6]. The former is of great importance for exploitation, and the later can guide the search space for promising areas [6]. In CSA, antibodies are updated mainly via hypermutation and receptor

editing, which perform local and global search, respectively. Considering the superior performance of DE and EDA, we suggest using them to perform local and global search in CSA, and thus combining the strength of both evolutionary algorithms and swarm intelligence. Therefore, in this paper we use DE and EDA to perform hypermutation and receptor editing, respectively, and accordingly propose the CSADE/EDA algorithm for global optimization problems. Since brain magnetic resonance (MR) image segmentation of gray matter (GM), white matter (WM) and cerebrospinal fluid (CSF) is pivotal for quantitative brain analyses and can popularly be transformed into the optimization problem by some models such as hidden Markov random field (HMRF) [15], the proposed algorithm has been evaluated against state-of-the-art brain image segmentation approaches on clinical brain MR images.

# 2 CSA-DE/EDA Algorithms 

Similar to CSA, the proposed CSA-DE/EDA algorithm analogizes the clonal selection process to solve optimization problems

$$
x^{*}=\arg \max _{x \in R^{D}} f(x)
$$

Each admissible solution $x$ is encoded as an antibody $\boldsymbol{A} \boldsymbol{b}_{\boldsymbol{i}}^{k}=\left[A b_{i, 1}^{k}, A b_{i, 2}^{k}, \ldots\right.$, $\left.A b_{i, D}^{k}\right] \in R^{D}$, and the objective function $f(x)$ is defined as the adaptive immune response, namely the affinity, to the corresponding antigen. Solving this optimization problem is equivalent to searching the antibody that has the maximum affinity [11]. To this end, CSA-DE/EDA evolves (at $k$ th generation) a population of antibodies, denoted by $\boldsymbol{A} \boldsymbol{b}^{\boldsymbol{k}}=\left\{\boldsymbol{A} \boldsymbol{b}_{1}^{k}, \boldsymbol{A} \boldsymbol{b}_{2}^{k}, \ldots, \boldsymbol{A} \boldsymbol{b}_{N}^{k}\right\}$, where $N$ is the population size and $k$ gives the generation index. The population can be randomly initialized and updated on a generation-by-generation basis using five operators, including the selection, clone, DEbased hypermutation, reselection and EDA-based receptor editing [11], until a stopping criterion, such as a predefined maximum number of generations, is met. The diagram of CSA-DE/EDA is shown in Fig. 1.

### 2.1 Selection and Clone

For the $k$ th generation of antibodies $\boldsymbol{A} \boldsymbol{b}^{\boldsymbol{k}}=\left\{\boldsymbol{A} \boldsymbol{b}_{1}^{k}, \boldsymbol{A} \boldsymbol{b}_{2}^{k}, \ldots, \boldsymbol{A} \boldsymbol{b}_{N}^{k}\right\}$, the corresponding affinities are evaluated and presented as $\boldsymbol{f}^{\boldsymbol{k}}=\left\{f\left(\boldsymbol{A} \boldsymbol{b}_{1}^{k}\right), f\left(\boldsymbol{A} \boldsymbol{b}_{2}^{k}\right), \ldots, f\left(\boldsymbol{A} \boldsymbol{b}_{N}^{k}\right)\right\}$. We select $n$ highest-affinity antibodies, denoted by $\left\{\boldsymbol{A} \boldsymbol{b}_{\{1\}}^{k}, \boldsymbol{A} \boldsymbol{b}_{\{2\}}^{k}, \ldots, \boldsymbol{A} \boldsymbol{b}_{\{\boldsymbol{n}\}}^{k}\right\}$, and clone each selected antibody $n_{i}$ times. Then the number of antibodies in the clone set $\boldsymbol{C}^{\boldsymbol{k}}$ is

$$
N_{c}=\sum_{i=1}^{n} n_{i}=\alpha * n
$$

where $\alpha$ is the clonal multiplying factor that takes a positive integer and controls the cloning number [11]. In this paper, $n_{i}$ is the same to all selected antibodies.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Diagram of the proposed CSA-DE/EDA algorithm.

# 2.2 Hypermutation 

The DE-based hypermutation is applied to each selected antibody $\boldsymbol{A} \boldsymbol{b}_{i}^{k}$ and its clones in $\boldsymbol{C}^{\boldsymbol{k}}$ in three steps. First, a temporary antibody is generated as follows

$$
Z=\frac{\left(A b_{d}^{k}+A b_{i}^{k}\right)}{2}+F \cdot\left[\left(A b_{d}^{k}-A b_{i}^{k}\right)+\left(A b_{b}^{k}-A b_{c}^{k}\right)\right]
$$

where $\boldsymbol{A} \boldsymbol{b}_{\boldsymbol{d}}^{\boldsymbol{k}}$ is randomly selected from $\boldsymbol{C}^{\boldsymbol{k}}$ such that $f\left(\boldsymbol{A} \boldsymbol{b}_{\boldsymbol{d}}^{\boldsymbol{k}}\right) \leq f\left(\boldsymbol{A} \boldsymbol{b}_{i}^{\boldsymbol{k}}\right), \boldsymbol{A} \boldsymbol{b}_{\boldsymbol{b}}^{\boldsymbol{k}}$ and $\boldsymbol{A} \boldsymbol{b}_{c}^{\boldsymbol{k}}$ are also randomly selected from $\boldsymbol{C}^{\boldsymbol{k}}$, and $F$ is a user specified scaling factor that controls the scaling of the difference vector. Second, the following crossover is applied to each temporary antibody $\boldsymbol{Z}$ and its parent $\boldsymbol{A} \boldsymbol{b}_{i}^{\boldsymbol{k}}$ to generate a trial antibody $\boldsymbol{A} \boldsymbol{b}_{i}^{\star k}$

$$
A b_{i, j}^{\star k}= \begin{cases}Z_{j} & \text { if }(\text { rand }<C R) \\ A b_{i, j}^{\star}, & \text { otherwise }\end{cases}, j=1, \cdots \cdots, D
$$

where rand is a uniform distributed random value within the range $[0,1]$ and $C R$ is the user specified crossover rate. At the combination step, the obtained trial antibody $\boldsymbol{A} \boldsymbol{b}_{i}^{\star k}$ replaces $\boldsymbol{A} \boldsymbol{b}_{i}^{\boldsymbol{k}}$ in $\boldsymbol{C}^{\boldsymbol{k}}$ if it has a higher affinity than the original antibody $\boldsymbol{A} \boldsymbol{b}_{i}^{\boldsymbol{k}}$; otherwise, $\boldsymbol{A} \boldsymbol{b}_{i}^{\boldsymbol{k}}$ is kept. After the hypermutation, $\boldsymbol{C}^{\boldsymbol{k}}$ is termed $\boldsymbol{C}^{\star \boldsymbol{k}}$. Since CSA-DE/EDA uses the arithmetic combination rather than randomly changing, it can capture the local information in the current population for more efficient exploitation [3].

### 2.3 Reselection

For each antibody $\boldsymbol{A} \boldsymbol{b}_{i}^{\boldsymbol{k}}$, there are $n_{i}$ cloned and hypermutated copies, which form a subset of antibodies. To keep the size of antibody population unchanged, we reselect the best antibody in each subset and thus form a trial population.

# 2.4 Receptor Editing 

Next, the EDA-based receptor editing is applied to the trial population. To explore the global information, we assume that the probabilistic distribution of the elite antibody is Gaussian and each component of the antibody is mutually independent. Thus, we have

$$
p\left(\boldsymbol{A} \boldsymbol{b}^{*}\right)=\prod_{d=1}^{D} p\left(A b_{d}^{*}\right)=\prod_{d=1}^{D} N\left(A b_{d}^{*} ; \mu_{d}, \sigma_{d}\right)
$$

where $\boldsymbol{A} \boldsymbol{b}^{*}=\left[A b_{1}^{*}, A b_{2}^{*}, \ldots, A b_{\Omega}^{*}\right]$ is the globally optimal antibody, and $N(\cdot ; \mu, \sigma)$ is a univariate Gaussian distribution with mean $\mu$ and standard deviation $\sigma$. To estimate the distribution $p\left(\boldsymbol{A} \boldsymbol{b}^{*}\right)$, we select $m$ highest-affinity antibodies from the current generation $\boldsymbol{A} \boldsymbol{b}^{\boldsymbol{k}}$ using the truncation selection [6] and apply the maximum likelihood estimation [6] to them, which results in the estimated Gaussian parameters $\left\{\mu_{d}^{k}, \sigma_{d}^{k} ; d=1,2, \cdots, D\right\}$. Then, we sample $r * N$ antibodies from the distribution $\prod_{d=1}^{D} N\left(A b_{d}^{*} ; \mu_{d}^{k}, \sigma_{d}^{k}\right)$ and use them to replace $r * N$ lowest-affinity antibodies in the trial population. Usually, the number of selected antibodies $m$, denoted by $\boldsymbol{A} \boldsymbol{b}_{\{\boldsymbol{M}\}}^{k}$, is set to $N / 2$ [6].

### 2.5 Summary

The major steps of the proposed CSA-DE/EDA algorithm are summarized in Table 1.

Table 1. The CSA-DE/EDA algorithm.

| Line | Pseudo code of CSA-DE/EDA |
| :-- | :-- |
| 1 | Initialization: Randomly generate N antibodies $\boldsymbol{A} \boldsymbol{b}^{\mathbf{0}}(k=0)$ |
| 2 | while the stopping criterion is not met |
| 3 | Evaluate the vector $\boldsymbol{f}^{\boldsymbol{k}}$ |
| 4 | Select $\boldsymbol{A} \boldsymbol{b}_{\{\boldsymbol{n}\}}^{k}$ |
| 5 | Select $\boldsymbol{A} \boldsymbol{b}_{\{\boldsymbol{M}\}}^{k}$ |
| 6 | Clone $\boldsymbol{A} \boldsymbol{b}_{\{\boldsymbol{n}\}}^{k} \rightarrow \boldsymbol{C}^{\boldsymbol{k}}$ |
| 7 | DE-based hypermutation $\boldsymbol{C}^{\boldsymbol{k}} \rightarrow \boldsymbol{C}^{* \boldsymbol{k}}$ |
| 8 | Reselect from $\boldsymbol{C}^{* \boldsymbol{k}}$ to obtain $\boldsymbol{A} \boldsymbol{b}^{\boldsymbol{k}+1}$ |
| 9 | EDA-based receptor editing to replace the $r * N$ lowest affinity anti- |
| 10 | bodies from $\boldsymbol{A} \boldsymbol{b}^{\boldsymbol{k}+1}$ |
|  | end |

## 3 Application to MR Image Segmentation

The proposed CSA-DE/EDA algorithm can be applied to many image segmentation problems, such as the segmentation of brain MR images that aims to delineate the gray matter (GM), white matter (WM) and cerebrospinal fluid (CSF) from the brain.

Let an observed brain MR image be an instance of the image random field $\boldsymbol{Y}$, and the corresponding segmentation result be an instance of the label random field $\boldsymbol{X}$.

According to the HMRF model, this segmentation task can be converted into the following optimization problem.

$$
\begin{aligned}
\boldsymbol{X}^{*} & =\arg \max _{\boldsymbol{X}} p\left(\boldsymbol{X} \mid \boldsymbol{Y}, \boldsymbol{b}, \boldsymbol{\theta}^{*}\right) \\
\boldsymbol{\theta}^{*} & =\arg \max _{\boldsymbol{\theta}} p\left(\boldsymbol{\theta} \mid \boldsymbol{Y}, \boldsymbol{b}, \boldsymbol{X}^{*}\right)
\end{aligned}
$$

where $\boldsymbol{b}$ is the bias field, $\boldsymbol{\theta}=\left\{\theta_{k} \mid k=1,2, \cdots, K\right\}$ the ensemble of model parameters, $K$ the number of classes, and

$$
p\left(\boldsymbol{\theta} \mid \boldsymbol{Y}, \boldsymbol{b}, \boldsymbol{X}^{*}\right) \propto p\left(\boldsymbol{Y} \mid \boldsymbol{X}^{*}, \boldsymbol{b}, \boldsymbol{\theta}\right) p(\boldsymbol{\theta})=\prod_{j} \sum_{k}\left[N\left(Y_{j}-b_{j} \mid X_{j}=k ; \theta_{k}\right) p\left(\theta_{k}\right)\right]
$$

with $N\left(x ; \theta_{k}\right)$ a Gaussian distribution with parameter $\theta_{k}=\left(u_{k}, \sigma_{k}\right)$. This problem can be solved using a three-step iterative process, which starts from a random initialization and iteratively (1) using the method in [16] to update the bias filed $\boldsymbol{b}$, (2) using the CSA-DE/EDA algorithm to solve the sub-problem given in Eq. (7) and update the model parameters (i.e. $\boldsymbol{\theta}$ being the antibody), and (3) using the iterated conditional mode (ICM) approach [17] to update the segmentation result.

Since the region-based HMRF method [18] is more robust to noise and artifacts than pixel-based HMRF but may offer a too smooth and relatively holistic view of the image to be segmented, we jointly used both region- and pixel-based HMRF methods. We first adopted the super pixel algorithm-TurboPixel [19] to over-segment a brain MR image into small regions $\boldsymbol{R}=\left\{R_{i} \mid i=1,2, \ldots, m\right\}$, where $m$ is the number of regions. Then the region adjacency graph (RAG) can be defined on $\boldsymbol{R}$, where each region $R_{i}$ corresponds to a node of the graph. The intensity of each node is the average intensity of all pixels in this region. So, we perform region-based segmentation to generate a coarse result. Next, we estimate the ranges of model parameters based on the coarse result and perform pixel-based segmentation to produce the final result. This process is summarized in Algorithm 2.

```
Algorithm 2: HMRF-CSA/DE/EDA MR segmentation algorithm
    Input: observed brain MR image \(\boldsymbol{Y}\)
    Output: optimal voxel class labels \(\boldsymbol{X}\) and model parameters \(\boldsymbol{\theta}\).
        Initialization: segmentation by k-means, random model parameters and initial bias
        field \(\boldsymbol{b}\)
        while the stopping criterion is not met (region-based)
            Evaluate the vector \(\boldsymbol{f}^{\boldsymbol{k}}\) through Eq. (8)
            Select \(\boldsymbol{A} \boldsymbol{b}_{(\boldsymbol{n})}^{\boldsymbol{k}}\)
            Select \(\boldsymbol{A} \boldsymbol{b}_{(\boldsymbol{M})}^{\boldsymbol{k}}\)
            Clone \(\boldsymbol{A} \boldsymbol{b}_{(\boldsymbol{n})}^{\boldsymbol{k}} \rightarrow \boldsymbol{C}^{\boldsymbol{k}}\)
            Hypermutation using DE \(\boldsymbol{C}^{\boldsymbol{k}} \rightarrow \boldsymbol{C}^{\boldsymbol{- k}}\)
            Reselect from \(\boldsymbol{C}^{\boldsymbol{- k}}\) to partly replace \(\boldsymbol{A} \boldsymbol{b}^{\boldsymbol{k}}\)
            EDA-based receptor editing
            Update class labels in Eq. (6) by ICM
            Update the bias field using the method in [16]
        end
    Execute step 2 to 12 again with the ranges of \(\boldsymbol{\theta}\) (pixel-based)
```

# 4 Experiments and Results 

The proposed CSA-DE/EDA algorithm has been applied to the segmentation of clinical brain MR images obtained from the internet brain segmentation repository (IBSR). The segmentation experiment was performed on 18 T1-weighted clinical brain MR images with expert segmentations (IBSR_V2.0) [20]. Each image was first spatially normalized into the Talairach orientation, and then resliced into a dimension of $256 * 256 * 128$ voxels with a voxel size of $1.0 * 1.0 * 1.5 \mathrm{~mm}^{3}$. The parameters used in this algorithm were empirically set as follows: population size $N=50$, scaling factor $F=0.9$, crossover rate $C R=0.1$, clonal multiplying factor $\alpha=2$, replacement ratio $r=0.1$ and the maximum iterations is 15 , including 5 iterations for region-based segmentation and 10 iterations for pixel-based segmentation. The accuracy of delineating gray matter and white matter was assessed quantitatively by using the Dice similarity coefficient (DSC).

$$
D\left(V_{s}(k), V_{g}(k)\right)=2 * \frac{\left|V_{s}(k) \cap V_{g}(k)\right|}{\left|V_{s}(k)\right|+\left|V_{g}(k)\right|}
$$

where $V_{s}(k)$ is the volume of brain tissue class k in the segmentation result, $V_{g}(k)$ is the corresponding volume in the ground truth, and $|V|$ represents the number of voxels in volume $V$. DSC takes a value from the range $[0,1]$, and a higher value represents more accurate brain tissue delineation. The accuracy of segmenting the entire brain volume is measured by the percentage of correctly classified voxels.

Figure 2 shows the 68th coronal slice of the study "IBSR_09", the intermediate segmentation result and final result of the proposed algorithm, and the ground truth brain tissue map. It reveals that the final result after the region- and pixel-based segmentation processes is more similar to the ground truth than the result obtained by using only the region-based segmentation.
![img-1.jpeg](img-1.jpeg)

Fig. 2. An example coronal slice from the Brain MRI study "IBSR_09" (left), and the corresponding result of region-based segmentation (middle left), result of region- and pixel-based segmentation (middle right) and ground truth (right).

Next, the proposed algorithm was quantitatively compared to the GMM-based unified registration-segmentation routine in SPM [21], the classic HMRF-EM algorithm of the FSL packages [22], the GA-GMM algorithm of the GAMixute package [23], the D-C algorithm [24] and the HMRF-CSA [25]. The accuracy of these six algorithms in the segmentation of gray matter, white matter and overall brain volume

on each image is depicted in Fig. 3, and the average segmentation accuracies of these algorithms are compared in Table 2. As it can be noticed, the proposed HMRFCSA/DE/EDA algorithm can produce more accurate segmentation of gray matter and overall brain volume than the other five algorithms on the IBSR_V2.0 dataset.

We conducted the ablation experiment with HMRF-CSA/DE/EDA and HMRFCSA/DE/EDA without region-based part (PHMRF-CSA/DE/EDA). The average accuracy and time cost of the two algorithms on one 3D MR image of IBSR_V2.0 are shown in Table 3 (Intel Core i7-4710HQ CPU, 16 GB memory and Matlab R2015a). It shows that HMRF-CSA/DE/EDA outperforms PHMRF-CSA/DE/EDA, which means that the region-based HMRF can indeed improve the pixel-based HMRF as an auxiliary. However, HMRF-CSA/DE/EDA still has a relatively high computational complexity due to the time-consuming nature of bio-inspired algorithms.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Accuracy of six algorithms in the segmentation of gray matter (bottom left), white matter (bottom right) and overall brain volume (top) on each image in the IBSR_V2.0 dataset.

Table 2. Average segmentation accuracy of six algorithms on the IBSR_V2.0 dataset.

| Accuracy | FSL | D-C | SPM | GA-EM | HMRF-CSA | HMRF-CSA/DE/EDA |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Overall | $75.06 \%$ | $75.02 \%$ | $81.02 \%$ | $74.97 \%$ | $82.95 \%$ | $\mathbf{8 9 . 9 0 \%}$ |
| GM | $77.35 \%$ | $73.80 \%$ | $84.42 \%$ | $77.90 \%$ | $84.92 \%$ | $\mathbf{9 2 . 0 2 \%}$ |
| WM | $87.08 \%$ | $\mathbf{8 8 . 4 1 \%}$ | $87.38 \%$ | $87.23 \%$ | $83.88 \%$ | $87.52 \%$ |

Table 3. Average accuracy and time cost of PHMRF-CSA/DE/EDA and HMRF-CSA/DE/EDA

|  | Accuracy | GM | WM | Time |
| :-- | :-- | :-- | :-- | :-- |
| HMRF-CSA/DE/EDA | $\mathbf{8 9 . 9 0 \%}$ | $\mathbf{9 2 . 0 2 \%}$ | $\mathbf{8 7 . 5 2 \%}$ | $\mathbf{1 5 1 0} \mathbf{~ s}$ |
| PHMRF-CSA/DE/EDA | $85.09 \%$ | $86.85 \%$ | $86.66 \%$ | 2164 s |

# 5 Conclusion 

In this paper, we proposed the CSA-DE/EDA algorithm for optimization problems. This algorithm incorporates DE and EDA into the CSA process, and thus generates offspring solutions by jointly using both local and global information from the current generation. Our experimental results indicated that the proposed algorithm outperforms the GA-GMM, HMRF-CSA, D-C algorithms and the brain image segmentation routine in the commonly used SPM and FSL packages for brain MR image segmentation. In future work we will mainly focus on reducing the computation time of the algorithm by using parallel computing techniques and designing adaptive parameters to further improve the robustness of CSA-DE/EDA [26, 27].

## References

1. Zhang, A., Sun, G., Ren, J., Li, X., Wang, Z., Jia, X.: A dynamic neighborhood learningbased gravitational search algorithm. IEEE Trans. Cybern. 48(1), 436-447 (2016)
2. Ji, L., Zhou. T.: On gradient descent algorithm for generalized phase retrieval problem. In: International Conference on Signal Processing, ICSP, pp. 320-325 (2016)
3. Binitha, S., Sathya, S.S.: A survey of bio inspired optimization algorithms. Int. J. Soft Comput. Eng. 2(2), 137-151 (2012)
4. Timmis, J., Andrews, P., Hart, E.: On artificial immune systems and swarm intelligence. Swarm Intell. 4(4), 247-273 (2010)
5. Peña, J.M., Robles, V., Larrañaga, P., Herves, V., Rosales, F., Pérez, M.S.: GA-EDA: hybrid evolutionary algorithm using genetic and estimation of distribution algorithms. In: Orchard, B., Yang, C., Ali, M. (eds.) IEA/AIE 2004. LNCS, vol. 3029, pp. 361-371. Springer, Heidelberg (2004). https://doi.org/10.1007/978-3-540-24677-0_38
6. Sun, J., Zhang, Q., Tsang, E.P.K.: DE/EDA: a new evolutionary algorithm for global optimization. Inf. Sci. 169(3-4), 249-262 (2005)
7. Onwubolu, G.C., Babu, B.V.: New Optimization Techniques in Engineering. Springer, Berlin (2004). https://doi.org/10.1007/978-3-540-39930-8
8. Huda, S., Yearwood, J., Togneri, R.: A constraint-based evolutionary learning approach to the expectation maximization for optimal estimation of the hidden Markov model for speech signal modeling. IEEE Trans. Syst. Man Cybern. Part B Cybern. 39(1), 182-197 (2009). A Publication of the IEEE Systems Man \& Cybernetics Society
9. Armañanzas, R., Inza, I., Santana, R., Saeys, Y., Flores, J.L., Lozano, J.A., et al.: A review of estimation of distribution algorithms in bioinformatics. Biodata Min. 1(1), 6 (2008)
10. Vidal, J.M., Orozco, A.L.S., Villalba, L.J.G.: Adaptive artificial immune networks for mitigating DoS flooding attacks. Swarm Evolut. Comput. 38, 94-108 (2018)
11. Castro, L.N.D., Zuben, F.J.V.: Learning and optimization using the clonal selection principle. IEEE Trans. Evol. Comput. 6(3), 239-251 (2002)

12. Batista, L., Guimaraes, F.G., Ramirez, J.A.: A distributed clonal selection algorithm for optimization in electromagnetics. IEEE Trans. Magn. 45(3), 1598-1601 (2009)
13. Castro, L.N.D., Zuben, F.J.V.: Clonal selection algorithm with engineering applications. In: GECCO 2002—Workshop Proceedings, pp. 36-37 (2002)
14. Zhang, L., Gong, M., Jiao, L., Yang, J.: Optimal approximation of linear systems by an improved Clonal Selection Algorithm. In: IEEE Congress on Evolutionary Computation, pp. 527-534 (2008)
15. Zhang, Y., Brady, M., Smith, S.: Segmentation of brain MR images through a hidden Markov random field model and the expectation-maximization algorithm. IEEE Trans. Med. Imag. 20(1), 45-57 (2001)
16. Li, C., Gatenby, C., Wang, L., Gore, J.C.: A robust parametric method for bias field estimation and segmentation of MR images. In: IEEE Conference on Computer Vision and Pattern Recognition, pp. 218-223 (2009)
17. Besag, J.: On the statistical analysis of dirty pictures. J. Roy. Stat. Soc. Ser. B (Methodol.) 48 (3), 259-302 (1986)
18. Zheng, C., Yijun, H., Leiguang, W., Qianqing, Q.: Region-based MRF model with optimized initial regions for image segmentation. In: International Conference on Remote Sensing, Environment and Transportation Engineering, RSETE, pp. 3354-3357 (2011)
19. Levinshtein, A., Stere, A., Kutulakos, K.N., Fleet, D.J., Dickinson, S.J., Siddiqi, K.: TurboPixels: fast superpixels using geometric flows. IEEE Trans. Pattern Anal. Mach. Intell. 31(12), 2290-2297 (2009)
20. Rohlfing, T.: Image similarity and tissue overlaps as surrogates for image registration accuracy: widely used but unreliable. IEEE Trans. Med. Imag. 31(2), 153-163 (2012)
21. Flandin, G., Friston, K.J.: Statistical parametric mapping (SPM). Scholarpedia 3(4), 6232 (2008)
22. FMRIB Software Library, in http://fsl.fmrib.ox.ac.uk/fsl/
23. Tohka, J., Krestyannikov, E., Dinov, I.D., Graham, M.K., Shattuck, D.W., Ruotsalainen, U., et al.: Genetic algorithms for finite mixture model based voxel classification in neuroimaging. IEEE Trans. Med. Imag. 26(5), 696-711 (2007)
24. Zhang, T., Xia, Y., Feng, D.D.: A deformable cosegmentation algorithm for brain MR images. In: Engineering in Medicine and Biology Society, EMBC, pp. 3215-3218 (2012)
25. Zhang, T., Xia, Y., Feng, D.D.: Hidden Markov random field model based brain MR image segmentation using clonal selection algorithm and Markov chain Monte Carlo method. Biomed. Signal Process. Control 12(1), 10-18 (2014)
26. Sun, G., Ma, P., Ren, J., Zhang, A., Jia, X.: A stability constrained adaptive alpha for gravitational search algorithm. Knowl. Based Syst. 139, 200-213 (2018)
27. Wei, F., Wenjiang, H., Jinchang, R.: Class imbalance ensemble learning based on the margin theory. Appl. Sci. 8(5), 815 (2018)