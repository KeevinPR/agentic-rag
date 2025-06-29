# Identifying DNA Methylation Modules Associated with a Cancer by Probabilistic Evolutionary Learning 

![img-0.jpeg](img-0.jpeg)

## Je-Keun Rhee

Cancer Research Institute, College of Medicine, Catholic University of Korea, Seoul, KOREA

## Soo-Jin Kim

Research Institute of Agriculture and Life Sciences, College of Agriculture and Life Sciences, Seoul National University, Seoul, KOREA

## Byoung-Tak Zhang

School of Computer Science \& Engineering, Seoul National University, Seoul, KOREA

Abstract-DNA methylation leads to inhibition of downstream gene expression. Recently, considerable studies have been made to determine the effects of DNA methylation on complex disease. However, further studies are necessary to find the multiple interactions of many DNA methylation sites and their association with cancer. Here, to assess DNA methylation modules potentially relevant to disease, we use an Estimation of Distribution Algorithm (EDA) to identify high-order interaction of DNA methylated sites (or modules) that are potentially relevant to disease. The method builds a probabilistic dependency model to produce a solution that is a set of discriminative methylation sites. The algorithm is applied to array- and sequencing-based high-throughput DNA methylation profiling datasets. The experimental results show that it is able to identify DNA methylation modules for cancer.

## I. Introduction

Genomic studies mainly aim to find genetic markers that are associated with a phenotype. Based on DNA sequences, researchers have searched for causal effects on biological processes including gene regulatory mechanisms and diseases. Although several risk factors have been identified by the association studies, the genetic variants do not fully explain the abnormal regulation because the biological regulatory mechanism can be affected by many other factors, as well as DNA sequence modification [1]-[4].

Epigenomics refers to the study of regulation of various genomic functions that are controlled by another partially stable modification, but not DNA sequence variants [5]. Among these, DNA methylation, which typically occurs at CpG dinucleotides catalyzed by DNA methyltransferase, is a crucial epigenetic regulatory mechanism in cellular processes. DNA methylation of CpG sites mostly causes silencing of the downstream gene. The enrichment of the differentially methylated DNA fractions can contribute to specific abnormalities, including complex diseases [6]-[8]. In particular, with the advent of array and next generation sequencing (NGS) technology, many researchers have carried out genome-wide DNA methylation profiling studies [9]-[11], and the genome-wide studies have reported that many genomic regions are differentially methylated in normal and abnormal cells [12]-[14].

However, a complex disease is caused by a combination of dysegulatory effects of multiple genes [15]-[17]. That is, errors of biological processes are not caused by the alteration of an individual methylation level. Recently, Easwaran et al. hypothesized that DNA hypermethylation modules preferentially target important developmental regulators in embryonic stem cells [18]. They found a set of genes whose DNA methylation contributed to the stem-like state of cancer. Horvath et al. studied aging effects of DNA methylation and identified co-methylated modules related to aging in the human brain and blood tissue [19]. Zhang and Huang investigated the DNA co-methylation patterns frequently observed in cancer [20].

Here, we identify combinatorial modules of DNA methylation sites associated with human diseases using an evolutionary learning approach (Figure 1). Evolutionary algorithms can approximate solutions well for a variety of problems [21]-[25]. They generate a new population through iterative updates and selection using a guided search process in a feature space. We utilized an Estimation of Distribution Algorithm (EDA)-based learning approach to identify combinations of cancer-related DNA methylation sites. In the EDA, the population is evolved according to the probabilistic distribution in selected individuals without conventional genetic operators such as crossover and mutation. As a result, the EDA can provide answers in combinatorial optimization problems [26]-[29]. The EDA-based methods have been previously applied in several biological studies, and it has offered promising results for
complex problems where other methods failed to find a good solution [30]-[32].

We investigated DNA methylation modules relevant to cancer, using the DNA methylation profiling datasets produced by array- and sequencing-based approaches. The experimental results showed that our method could identify DNA methylation modules related to cancer.

## II. Methods

## A. Evolutionary Learning Procedure to Identify a Set of DNA Methylation Sites Associated with a Disease

EDAs evolve a population to find the optimal solution probabilistically. The initial population is constructed by randomly selecting individuals. The individuals represent higher order interactions of the methylated sites. The population size $m$ is decided empirically and the initial weight $w_{j}$ of the individual $j(0<j<m)$ is randomly assigned with a small value $(-1<w_{j}<1)$.

In the evolutionary process, each individual is evaluated for how discriminative the interaction is for the datasets. Better individuals are then selected and a dependency tree is built by fitting to the selected individuals. New individuals of the next generation are generated using the probability distribution within the tree structure, and replace the previous individuals. The overall procedure is as follows:
Step 1) Set $g \leftarrow 0$
Step 2) Initialize population $X(g)$ by random generation
Step 3) Evaluate individuals in $X(g)$
Step 4) Select a set of individuals by tournament selection from $X(g)$
Step 5) Construct a dependency tree $G(g)$ by measuring Kull-back-Leibler divergence between variables
Step 6) Learn parameters using a probability distribution of the set of selected at step 4
Step 7) Generate new individuals by sampling with joint distribution from the $G(g)$, and create a new population $X(g+1)$
Step 8) Set $g \leftarrow g+1$
Step 9) If the termination criterion is not met, go to Step 3
Further details for steps 3 and 5 are explained in following sections.

## B. Learning Dependency Tree

The dependency tree is built from the selected individuals by searching conditional dependencies between random variables. The model is then optimized by a series of incremental updates [33], [34], as follows:

Suppose that $X$ is a population and $X=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ represents a vector of variables with $n$ features, i.e., DNA methylation sites. The probability distribution is denoted by a joint probability $P\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ as to:

[^0]
[^0]:    [^1]:    [^1]:    Corresponding Author: Byoung-Tak Zhang (Email: btsftung@bi.snu.ac.kr)

![img-1.jpeg](img-1.jpeg)

FIGURE 1 Schematic overview for probabilistic evolutionary learning to identify DNA methylation modules.

$$
\begin{aligned}
P(X) & =P\left(X_{1}, X_{2}, \ldots, X_{n}\right) \\
& =P\left(X_{1} \mid X_{2}, \ldots, X_{n}\right) P\left(X_{2} \mid X_{3}, \ldots, X_{n}\right) \ldots . P\left(X_{n-1} \mid X_{n}\right) P\left(X_{n}\right)
\end{aligned}
$$

However, it is hard to measure all the joint probabilities exactly when $n$, the number of variables, is large. Thus it is necessary to approximate the probability distribution. In this study, we used a dependency tree, and the distribution is approximated as follows:

$$
P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=P\left(X_{i}\right) \prod_{i \neq r} P\left(X_{i} \mid X_{p r(i)}\right)
$$

where $X_{1}, X_{2}, \ldots, X_{n}$ are random variables, $r$ is an index of a root node, and $p a(i)$ denotes the index of the parent node of $X_{i}$. The tree structure is built by searching based on KullbackLeibler divergence between two random variables. The dependency graph is constructed optimally in a direction to maximize total mutual information as follows:

$$
\operatorname{argmax}_{c, p r} \prod_{c \neq r} I\left(X_{i} ; X_{p r(i)}\right)
$$

$$
\begin{aligned}
& I\left(X_{i} ; X_{p r(i)}\right)= \\
& \sum_{x} \sum_{y} P\left(X_{i}=x, X_{p r(i)}=\gamma\right) \log \frac{P\left(X_{i}=x, X_{p r(i)}=\gamma\right)}{P\left(X_{i}=x\right) P\left(X_{p r(i)}=\gamma\right)}
\end{aligned}
$$

The complete graph $G$ searches the maximum spanning tree, and then the best dependency tree is constructed.

For parameter learning, the most likely values are calculated from the frequencies in the selected individuals. That is, the model parameters are represented as marginal probabilities in a root node and conditional probabilities in the other nodes. The marginal probabilities in the root nodes and the conditional probabilities in the child nodes are calculated by Eqs. (5) and (6), respectively, as follows:

$$
\begin{gathered}
P\left(X_{r}=x\right)=\frac{c\left(X_{r}=x\right)}{N} \\
P\left(X_{i}=x \mid X_{p r(i)}=\gamma\right)=\frac{c\left(X_{i}=x, X_{p r(i)}=\gamma\right)}{c\left(X_{p r(i)}=\gamma\right)}
\end{gathered}
$$

where $c$ is the count of a variable $X$ with a specific value and $N$ is the total number of individuals.

## C. Fitness Evaluation in a Population

The fitness function represents how informative the chromosome is to classify the samples. That is, the fitness for an individual is evaluated by measuring the classification accuracy for interaction of the features. To determine and update the fitness for each individual, we introduce a gradient descendant rule for training data $\mathbf{D}$ as follows:

$$
w_{i}=w_{i}+\eta\left(t_{j}-f\left(\mathbf{D}_{j}\right)\right) v_{j i}
$$

where $w_{i}$ is the weight value for $i$-th feature and $t_{j}$ is the target class in the $j$-th training instance $\mathbf{D}_{j}, \eta$ is the learning rate and $v_{j i}$ is the value of the $i$-th attribute in the $j$-th instance. $f\left(\mathbf{D}_{j}\right)$ is the predicted output value of the $j$-th training instance by our model and determined as follows:

$$
f\left(\mathbf{D}_{j}\right)=\left\{\begin{array}{l}
1, \quad \text { if } \sum_{i=0}^{n} w_{i} \cdot v_{j i}>0 \\
-1, \text { otherwise }
\end{array}\right.
$$

The difference between the predictions and the target values specified in the training sequence is used to represent the error of the current weight vector. The target function is optimized to minimize the classification error. The weight values are evaluated against a sequence of training samples and are updated to improve the classification accuracy. The weight update processes are repeated until they converge after a number of epochs.

Using the learning scheme, we identify the most informative individuals for classification, where the absolute values of their weights are large. In addition, it is better to find the DNA methylation module, whose number of features is small. Finally, the fitness function for the $k$-th individual $X^{k}$, Fitness $\left(X^{k}\right)$ is defined as follows:

$$
\text { Fitness }\left(X^{k}\right)=A \alpha\left(X^{k}\right)-\operatorname{Order}\left(X^{k}\right)
$$

where $A \alpha\left(X^{k}\right)$ is the classification accuracy for training datasets and $\operatorname{Order}\left(X^{k}\right)$ denotes the number of methylation sites which are selected in the individual $X^{k}$.

## D. Dataset

The high-throughput DNA methylation profiles of large genomic regions can be produced by both array and NGS technologies. We applied our approach to these two types of datasets. The array data were generated by the Illumina Infinium 27 k Human DNA methylation BeadChip, for surveying genome-wide DNA methylation profiles in breast cancer and normal samples [35]. We downloaded the dataset from Gene Expression Omnibus accession number GSE32393, and removed the samples with missing values. Sequence-based datasets were produced by MethylCap-seq in matched normal and colorectal cancer samples and collected at GSE39068 [36]. Normalization and preprocessing were carried out using the approaches detailed by Simmer et al. [36].

The DNA methylation levels of the two datasets were represented as beta-values, which were bounded between 0 (unmethylated) and 1 (totally methlyated).

## III. Results

## A. DNA Methylation Module Associated with Breast Cancer

This analysis was carried out based on DNA methylation profiling datasets that experimentally measured the methylation statuses using DNA Methylation BeadChip [35]. We extracted data for DNA methylation profiles on chromosome 17 from breast cancer and normal samples. Then, the data used at our experiment consist of total 99 samples with 82 cancer and 17 normal samples with 1,587 features. Figure 2 shows the learning curves in the evolutionary process. The fitness value was improved when the number of generations increased. We introduced a term, in the fitness function, for the number of the methylation sites to find an individual with a shorter length;
![img-2.jpeg](img-2.jpeg)

FIGURE 2 Learning curve using breast cancer datasets. The $x$-axis is the number of generations and the $y$-axis shows (a) fitness values and (b) the number of methylation sites.

therefore, the order decreased with the learning process (Figure 2(b)). After convergence, six sites were selected for the discrimination. These six sites were related to genes, KIAA1267, CD79B, ALOX12, TMEM98, KRT19 and FOXJ1 (Table 1).

ALOX12 has a role in the growth of breast cancer and its inhibition may be a strategy for inhibiting tumor growth [37]. The gene can be used as a serum marker for breast cancer [38].


TABLE 2 Classification Performance by Splitting Training and Test Data.


In addition, it has been reported that hypermethylation of ALOX12 is associated with cancer [39]-[42]. Indeed, the ALOX12 gene is closely related to apoptosis, and alterations in its expression caused by DNA methylation can cause a malfunction in cell death [43]-[45]. Therefore, it is reasonable to hypothesize that a change of methylation in the gene is linked to cancer, including breast tumors. KRT19 is a well-known marker for breast cancer [46], [47], and the KRT19 promoter can be aberrantly methylated in cancer cell lines [48]. The CD79B gene has also been shown to be related to breast cancer in several studies [49], [50]. FOXJ1, a member of the forkhead box (FOX) family, may function as a tumor suppressor gene in breast cancer [51]. FOXJ1 is hypermethylated and silenced in breast cancer cell lines [52]. TMEM98 is a transmembrane protein. Recently, Grimm et al. investigated transmembrane proteins specific for cancer cells, and showed that the transmembrane proteins can be targets for antibodies and may form biomarkers for tumor diagnosis, prognosis, and treatment [53]. The function of KIAA1267 is unclear yet, but this gene encodes KAT8 regulatory NSL complex subunit 1, and KAT8 regulates p53, a tumor suppressor gene [54], [55]. Our results suggest that KIAA1267 also can have a role in breast cancer.

To verify that our method produced good classification performance generally, we calculated the classification performance by randomly separating the original dataset into training and test datasets. Table 2 shows the average accuracy, sensitivity and specificity for 20 times repetition of random

TABLE 3 Classification Performance Using the Selected Sites and Randomly Selected Sites.


[^0]
[^0]:    *At the column Feature, $f$ is the number of randomly selected sites, and selected means the selected sites by our method.

![img-3.jpeg](img-3.jpeg)

FIGURE 3 Learning curve using colorectal cancer datasets. The $x$-axis is the number of generations and the $y$-axis is fitness values.
splitting, measured by conventional classification algorithms. Our algorithm showed good classification results even at the independent test set. For further verification, we randomly extracted the methylation sites with 100 times repetition, then measured the classification performance in each dataset by 10 -fold cross-validation. Table 3 shows that our method produced better results than the others, regardless of the number of the randomly selected sites. In particular, it was noted that the specificity using the selected sites by our method was much better than the others, even though the original data was highly imbalanced.

## B. Modules Associated with Colorectal Cancer using High-Throughput Sequencing Data

Recently, high-throughput sequencing technologies have been used to determine DNA methylation profiles. We applied our method to the sequencing-based methylation profile datasets produced by Simmer et al. [36].

The experiments were carried out using 25 cancer and 25 normal samples with 10,393 genomic regions on chromosome 17. Figure 3 depicts the improvement of the fitness in iterative learning procedures using these datasets, and finally 348 regions were selected to discriminate colorectal cancer and normal samples after convergence. Table 4 shows the average classification performance by 10 -fold cross-validation using the selected sites.

We annotated the 348 selected regions using GPAT [56] and investigated which genes were located close to the selected regions. We determined which genes were enriched within the KEGG pathway using the genes whose transcription start sites are located within 5,000 bp from the selected genomic regions [57], [58]. Table 5 summarizes the significantly enriched pathways with low $p$-values and shows that most of these are closely associated with cancer-related networks. Note that the enriched signaling pathways were related to colorectal cancer. In colorectal

TABLE 4 Classification Performance Using Only the Selected Sites in Colorectal Cancer.




cancer, the roles of the wnt signaling pathway and MAPK signaling pathway have been studied intensively [59]-[62]. Genetic mutations affecting the pathway components and the alteration of their expression can enhance tumorigenicity in cancer cells. In addition, the neurotrophin signaling pathway could be related to growth of colorectal cancer cells [63] and the chemokine signaling pathway suppresses colorectal cancer metastasis [64], [65].

The phosphatidylinositol signaling pathway plays an important role in the growth, survival and metabolism of cancer cells, and targeting this pathway has the potential to lead to treatments for colorectal cancer [66], [67].VEGF and ErbB may be valid therapeutic targets for patients with colorectal cancer [68]-[71].

## IV. Discussion and Conclusion

DNA methylation may be associated significantly with complex diseases and many genomic regions are differentially methylated in various cancers, comparing to normal samples. In this study, we presented a method to identify combinatorial effects of DNA methylation at multiple sites. From a systematic perspective, the relationship between DNA methylation regions and a specific disease is learned by the presented probabilistic evolutionary learning method. The fitness value of a DNA methylation module measures the level of its responses to the cancer. In a computational view, our method can solve a large number of feature problems by identifying modules with both compactness and high coverage of cancer-related genes. Applying our method to breast cancer and colorectal cancer data produced by high-throughput technologies, we detected cancer-related modules that were confirmed by the literature and functional enrichment analysis. Interestingly, we observed that the selected regions were located around genes that are significantly enriched in cancer-related gene set categories, which provided evidence that the identified modules in our study are biologically meaningful.

Moreover, from the result for the array-based dataset, we could obtain a good accuracy with a very small number of random features. However, the specificity was very low in the experiments with random features. The result suggested that our method could generate well-balanced classification performance even with a highly imbalanced dataset, although conventional classifiers would not work well with imbalanced circumstances. Also in the second experiment using the NGS-based dataset with large number of features and small sample size, our method could find the informative DNA methylation sites with good classification performances, even though the decision tree, necessary to be discretized in each value, showed relatively lower results.

Studies on DNA methylation could reveal the process of tumorigenesis as well as identify biomarkers. Our approach, which identifies multiple DNA methylation sites that might be epigenetically regulated, could provide a useful strategy to detect the epigenetic association related to cancer. By applying our method to array- and NGS-based data, we showed that it is applicable to a variety of data types and various disease contexts. Moreover, recent studies suggest a complex relationship between genetic variation and DNA methylation. Systems genetics and epigenetics approaches are required to examine these relationships. Although our framework is based on DNA methylation profile datasets, it could be used to identify the combinatorial association of various factors, including gene expression levels, microRNAs, copy number variations, genetic variations, and environmental factors. The integration of a variety of data would provide the basis for new hypotheses and experimental
approaches in the model of a complex disease. Moreover, the systematic identification of causal factors and modules would provide insights into mechanisms underlying complex diseases and help to develop efficient therapies or effective drugs.

In summary, we presented a method for searching the higherorder interaction of DNA methylation sites using a probabilistic evolutionary learning method. We also examined the potential for the combined effects of various sites on the genome. The results suggested that the alteration of DNA methylations at multiple sites affects cancer. Similar to genome-wide association studies, our approach provided an opportunity to capture the complex and multifactorial relationships among DNA methylation sites and to find new factors for future study. Therefore, our approach would facilitate a comprehensive analysis of genomewide DNA methylation datasets and help the interpretation for the effects of DNA methylation on multiple sites.

## Acknowledgment

This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Ministry of Science and ICT, Republic of Korea (grant no. NRF-2015R1C1A1A01053824, NRF-2018R1C1B6005304, NRF-2016R1D1A1B03935676, and NRF-2018R1D1A1B07050393).
