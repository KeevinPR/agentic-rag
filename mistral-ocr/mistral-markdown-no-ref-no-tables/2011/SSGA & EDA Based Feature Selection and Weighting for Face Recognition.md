# SSGA \& EDA Based Feature Selection and Weighting for Face Recognition 

Tamirat Abegaz ${ }^{\oplus}$, Gerry Dozier ${ }^{\oplus}$, Kelvin Bryant ${ }^{\oplus}$, Joshua Adams ${ }^{\oplus}$, Joseph Shelton ${ }^{\oplus}$, Karl Ricanek ${ }^{\text {a }}$, Damon L. Woodard*<br>Center for Advanced Studies in Identity Sciences<br>$\#$ North Carolina A\&T State University<br>${ }^{\text {a }}$ The University of North Carolina at Wilmington<br>*Clemson University


#### Abstract

In this paper, we compare genetic and evolutionary feature selection (GEFeS) and weighting (GEFeW) using a number of biometric datasets. GEFeS and GEFeW have been implemented as instances of Steady-State Genetic and Estimation of Distribution Algorithms. Our results show that GEFeS and GEFeW dramatically improve recognition accuracy as well as reduce the number of features needed for facial recognition. Our results also show that the Estimation of Distribution Algorithm implementation of GEFeW has the best overall performance.


Keywords-Face Recognition, Steady State Genetic Algorithm, Estimation of Distribution Algorithm, Eigenface, Feature Selection.

## I. INTRODUCTION

The human face is an extremely complex visual stimulus that articulates identity, emotion, ethnicity, age, and gender of individuals [1,2]. The human brain, by its nature, is highly adapted for compensating for changes that occur due to various physiological (for example facial expression due to emotion, aging), and environmental factors (such as illumination, pose) and performs face recognition efficiently and accurately [3]. Automated Facial Recognition (FR) has been a difficult task since it requires datasets that represent realistic scenarios in terms of changes such as illumination, aging, and facial expression. On the other hand, automating FR is useful for several applications such as passport verification, entrance control, criminal investigation, and surveillance, to name a few [3].

The Eigenface method [3] is one of the most widely used feature extraction techniques. It is capable of efficient and accurate feature extraction in a constrained environment where pose, illumination, and expression are similar between the training and the test sets. Since all faces have similar structure such as two eyes, a nose between the eyes, a mouth, etc, training and test set images can be grouped or concentrated at a specific location on a high dimensional data space. This method allows one to successfully extract those dimensions required for efficient representation of the face and ignore those that contribute less.

The Eigenface method uses Principal Component Analysis (PCA) for feature extraction. In statistical terminology, PCA [4] is a transform that chooses a new coordinate system for the dataset such that the greatest variance by any projection of the
dataset comes to lie on the first axis (the first principal component), the second axis corresponds to the maximal remaining variation (the second principal component) in the dimension orthogonal to the first axis, and so on. The fundamental idea behind PCA is that if there are a series of multidimensional data vectors representing objects within a space (image space for our case) which have similarities, it is possible to use a transformation matrix to create a reduced space (i.e., face space) that accurately describes the original multidimensional vectors. Kirby and Sirovich [5] proposed the use of PCA for the analysis and representation of images, Turk and Pentland [6] used the PCA for face recognition systems.

This work is an extension of the research performed by Abegaz et. al [7]. In their work, Abegaz et al. used Genetic and Evolutionary Feature Selection (GEFeS) and Weighting (GEFeW) along with the Eigenface method. First, they implemented the Eigenface method to extract features from a subset of the Face Recognition Grand Challenge (FRGC) dataset [8]. In their dataset, they used 280 subjects, each subject having a total of 3 associated images (resulting in a total of 840 images). Abegaz et. al indicate that 560 features were extracted for each image (for both the gallery set, which is the pre-enrolled images, and the probe set, which is the newly acquired images). They created Eigen-GEFeS and Eigen-GEFeW that were instances of Steady State Genetic Algorithms (SSGAs). In their work, Abegaz et. al. reported that Eigen-GEFeS and Eigen-GEFeW enhanced the overall performance of the Eigenface method while reducing the number of features needed. Comparing Eigen-GEFeS with Eigen-GEFeW, their results showed that Eigen-GEFeW performed better in terms of accuracy even though it used a significantly larger number of features as compared to EigenGEFeS.

In this paper, we extend the work of Abegaz et. al and focus on two additional aspects: First, we used an Estimation of Distribution Algorithm (EDA) implementation of GEFeS and GEFeW in addition to the SSGA implementations of GEFeS and GEFeW performed in [17]. Second, we investigate the performance of GEFeS and GEFeW across multiple datasets which include FRGC [8, 9], Face Recognition Technology (FERET) [10], Yale [11], and Essex [12]. The GEFeS and GEFeW implementations for our work

are instances of SSGAs and EDAs within eXploratory Toolset for the Optimization Of Launch and Space Systems (XTOOLSS) [13].

Our work is partly motivated by the research of Gentile et. al [14, 15]. Gentile et. al proposed a hierarchical two-stage process to reduce the number of iris feature checks required for recognition iris recognition system.

The remainder of this paper is as follows. In Section II, we provide an overview of GEFeS and GEFeW, and in Section III we present our experiments. In Section IV, we present our results. Finally, our conclusions and future work are presented in Section V.

## II. GEFeS AND GEFeW

GEFeS and GEFeW [16, 17, 18, 19, 20,21] were designed for the purpose of selecting and weighting high discriminating features used for biometric identification. In identification [22], the objective is to rank the gallery (the pre-enrolled images and their associated feature vectors) by similarity to the probe (the newly acquired images and their feature vectors) by comparing the probe features with each of the gallery features. Such ranking is computationally expensive particularly for real world applications that involve large number of images in a dataset. GEFeS and GEFeW are targeted to reduce the number of features by keeping only those features that have high discriminatory power and mask out those which have less contribution for FR. Consider the matrix shown in Figure 1 as a feature set.

Figure 1: Sample feature set given as matrix
Consider also the matrix shown in Figure 2 as a candidate real-coded feature mask.

Figure 2: Real-Coded Feature Mask
For GEFeS, in order to mask features, a masking threshold value of 0.5 is used as follows. If the value of a real-coded feature mask is less than 0.5 , then the value corresponding to the real-coded feature mask is set to 0 (otherwise it is set to 1 ).

Figure 3 shows candidate binary-coded feature mask obtained from the real coded feature mask generated in Figure 2. In other words, the binary-coded value is a mapping of realcoded value into zeros and ones based on user specified threshold.

When comparing a binary-coded candidate feature mask with the feature set, if a position corresponding to the feature set value in the candidate feature mask is 0 then that feature value is masked. Figure 4 shows the result of GEFeS when applied to the features matrix given in Figure 1.

Figure 4: The Resulting feature set after feature masking
For GEFeW, the real-coded candidate feature mask is used to weight features. The value in Figure 5 is obtained by multiplying the real-coded feature mask with the feature matrix. In other words, when the real-coded value is multiplied by each feature value, it provides a weighted feature matrix (see Figure 5). Whenever the weighted feature value is 0 (or approximately equal to 0 ), it is considered as masked. Figure 5 shows the weighted feature set.

$$
\left[\begin{array}{cccccc}
0.56 & 31.2 & 68.53 & 51.3 & 17 \\
40.95 & 10.2 & 0.24 & 0 & 60.8 \\
9.92 & 11.5 & 20.25 & 22.75 & 106.8 \\
16.72 & 19.35 & 3.52 & 25.23 & 17.6
\end{array}\right]
$$

Figure 5: Weighted Feature Set
The computation of the fitness value for GEFeS and GEFeW is shown in Equation 1. The objective of the evaluation function is to minimize the number of recognition errors (increasing accuracy) while reducing the number of features needed. As shown in Equation 1, the fitness returned by the evaluation function is the number of recognition errors encountered after applying the feature mask multiplied by 10 plus the percentage of features used.

$$
\text { Fitness }=(\text { number of errors })^{*} 10+\% \text { Features Used }
$$

## III. EXPERIMENT

Four publicly available facial datasets were used for the multi-dataset GEFeS and GEFeW experiments. These datasets include FRGC, Face Recognition Technology (FERET), Essex, and Yale. For these experiments, a subset of each dataset with frontal images were used. The FRGC dataset used for this experiment was is composed of 840 images taken from 280 subjects. The FERET dataset is composed of 787 images taken for 239 subjects. The Essex dataset consists of

435 images taken from 145 subjects. The Yale dataset consists of 114 images taken from 36 subjects.

Figure 6 shows five sample test images for each dataset used in the experiment. The first, second, third, and fourth rows shows sample test set images from the FRGC, FERET, Essex, and Yale datasets respectively.

Each image has been through the pre-processing stages such as eye rotation alignment, histogram equalization, resizing ( $225 \times 195$ pixels) and conversion of the images into greyscale. For all the datasets used, the gallery contains two snapshots and the probe contains one snapshot per subject.

The objective of GEFeS and GEFeW is to evolve feature masks and feature weights in an effort to improve accuracy while reducing the number of features needed for recognition purposes.
![img-0.jpeg](img-0.jpeg)

Figure 6: Sample images for datasets used in this experiment

## IV. RESULTS

For our experiment, we will be comparing two instances of GEFeS (implemented using an SSGA and an EDA), and two instances of GEFeW (again, implemented using a SSGA and an EDA). The instances are as follows: Eigen-GEFeS ${ }_{\text {SSGA }}$, Eigen- $\mathrm{GEFeS}_{\mathrm{EDA}}$, Eigen- $\mathrm{GEFeW}_{\text {SSGA }}$, and Eigen- $\mathrm{GEFeW}_{\text {EDA }}$. The SSGA instances all have a population size of 20 , Gaussian mutation rate of 1 and mutation range of 0.2 . The EDA instances also had a population size of 20 individuals with elites size of $5(25 \%$ of the population). Furthermore, they were each run a total of 30 times with a maximum of 1000 function evaluations. Our results are shown from Tables I to IV. In each table four instances are compared with the Eigenface method denoted as Eigenface ${ }_{\text {Baseline }}$.
The second column denotes the percentage of the average number of features used. The third and fourth columns represent the average and the best accuracy obtained, respectively. ANOVA and t-Tests were used to divide Eigen$\mathrm{GEFeS}_{\text {SSGA }}$, Eigen- $\mathrm{GEFeS}_{\text {EDA }}$, Eigen- $\mathrm{GEFeW}_{\text {SSGA }}$, Eigen-

GEFeW $_{\text {EDA }}$, and the baseline algorithm into equivalence classes.

Table I shows the performance comparison of the five methods on our subset of the FRGC dataset. For FRGC dataset, the results show that Eigen- $\mathrm{GEFeW}_{\text {SSGA }}$ and Eigen$\mathrm{GEFeW}_{\text {EDA }}$ significantly outperform the baseline method in terms of accuracy. Eigen- $\mathrm{GEFeW}_{\text {EDA }}$ provides the best result in terms of accuracy though it uses almost the entire feature set. While Eigen- $\mathrm{GEFeS}_{\text {EDA }}$ used only $49.58 \%$ of the features, Eigenface ${ }_{\text {Baseline, }}$, Eigen- $\mathrm{GEFeS}_{\text {SSGA, }}$ and Eigen- $\mathrm{GEFeS}_{\text {EDA }}$ fall in the same equivalent class with respect to accuracy. In general, the results indicate that EDA-based feature selection and weighting performs better than the corresponding SSGA.

TABLE I
EXPERIMENTAL RESULTS FOR EIGENFACE, EIGEN-GEFES AND EIGENGEFEW FRGC DATASET

Table II shows the performance comparison of the five methods on our subset of the FERET dataset. The results indicate that Eigen- $\mathrm{GEFeS}_{\text {SSGA }}$ and Eigen- $\mathrm{GEFeS}_{\text {EDA }}$ instances fall into the same equivalence class in terms of accuracy. The percentage of features used for Eigen$\mathrm{GEFeS}_{\text {SSGA }}$ and Eigen- $\mathrm{GEFeS}_{\text {EDA }}$ is $51.79 \%$ and $44.88 \%$, respectively. The overall results of the four instances shown in Table II indicate that EDA-based feature selection and weighting performs better than the corresponding SSGA.

TABLE II
EXPERIMENTAL RESULTS FOR EIGENFACE, EIGEN-GEFES AND EIGENGEFEW FERET DATASET

Table III shows the performance comparison of the five methods on our subset of the ESSEX dataset. Once again Eigen- $\mathrm{GEFeS}_{\text {EDA }}$ performs better than Eigen- $\mathrm{GEFeS}_{\text {SSGA }}$ in terms of accuracy. However, the feature reduction of Eigen$\mathrm{GEFeS}_{\text {SSGA }}$ is significantly lower than Eigen- $\mathrm{GEFeS}_{\text {EDA }}$. Eigen- $\mathrm{GEFeS}_{\text {SSGA }}$ used only $36.21 \%$ features. It reduces the features needed by approximately two thirds while obtaining better accuracy than the corresponding baseline method. Similar to the results reported for FRGC and FERET datasets, Eigen- $\mathrm{GEFeW}_{\text {EDA }}$ provides the best result in terms of accuracy. In general, the results indicate that EDA-based feature selection and weighting performs better than the corresponding SSGA.

TABLE III
EXPERIMENTAL RESULTS FOR EIGENFACE, EIGEN-GEFES AND EIGENGEFEW ESSEX DATASET

Table IV shows the performance comparison of the five methods on our subset of the YALE dataset. The baseline accuracy result is $100 \%$. The aim of this experiment is to discover the percentage of features that are needed to produce the same accuracy as the baseline method (since the performance of the baseline method is $100 \%$ ). The results indicate that Eigen- $\mathrm{GEFeS}_{\text {SSGA }}$ and Eigen- $\mathrm{GEFeS}_{\text {EDA }}$ provide a dramatic reduction in the percentage of feature usage. Both the Eigen- $\mathrm{GEFeS}_{\text {SSGA }}$ and Eigen- $\mathrm{GEFeS}_{\text {EDA }}$ reduce the features needed by more than 90 percent. Eigen-GEFeW also reduces the features needed considerably as compared to the FRGC, FERET, and ESSEX datasets.

Figures 7 through 10 show the percentage of Eigenface usage for the best accuracy of Eigen- $\mathrm{GEFeS}_{\text {SSGA }}$ and Eigen$\mathrm{GEFeS}_{\text {EDA }}$. The natural expectation for Eigenface based systems is that the first few principal components (eigenfaces) with greater eigenvalues contain the most discriminatory features. However, as can be observed from the results presented in Figures 7 to 10, the histogram result is roughly
uniform across the components histogram result of the distribution of feature selection experiment

TABLE IV
EXPERIMENTAL RESULTS FOR EIGENFACE, EIGEN-GEFES AND EIGENGEFEW Yale DATASET

The experimental results show that Eigen- $\mathrm{GEFeS}_{\text {SSGA }}$ and Eigen- $\mathrm{GEFeS}_{\text {EDA }}$ does not necessary select those Eigenfaces with greater Eigenvalues. Notice that the some Eigenfaces with smaller Eigenvalues can have a better feature contribution than some of the components with higher Eigenvalues. This indicates that being a principal component with higher Eigenvalues does not necessary lead to better performance since some Eigenfaces might capture unwanted information for recognition.. In other words, being a principal component with higher Eigenvalues doesn't necessarily make the eigenvector as a candidate component for feature selection. Instead of relying on the Eigenvalues, GEFeS selects those components that have higher discriminatory power. This result supports the work of Liu and Wechsler [23]. Liu and Wechsler showed that PCA identifies the Most Expressive Feature, which are not necessarily the most discriminatory features.

The overall result of comparing the SSGA and EDA instances of GEFeS and GEFeW implementations indicates that EDA performs well in both reducing the number of features required and providing improved accuracy. In most of the results obtained, Eigen- $\mathrm{GEFeS}_{\text {SSGA }}$ and Eigen- $\mathrm{GEFeS}_{\text {EDA }}$ reduced the features needed approximately by half. However, both Eigen- $\mathrm{GEFeW}_{\text {SSGA }}$ and Eigen- $\mathrm{GEFeW}_{\text {EDA }}$ improve the accuracy significantly while using more features than their respective Eigen- $\mathrm{GEFeS}_{\text {SSGA }}$ and EigenGEFeS $_{\text {EDA }}$. In general, the FRGC, FERET, Essex, and Yale dataset based experimental results indicate that EDA instances of GEFeS and GEFeW perform better than the corresponding SSGA instances.

![img-2.jpeg](img-2.jpeg)

Figure 7: Percentage usage of Eigenfaces in decreasing order of the eigenvalues Eigen-GEFES $_{\text {SSGA }}$ and Eigen-GEFES $_{\text {EDA }}$ for FRGC dataset
![img-2.jpeg](img-2.jpeg)

Figure 8: Percentage usage of Eigenfaces in decreasing order of the eigenvalues Eigen-GEFES $_{\text {SSGA }}$ and Eigen-GEFES $_{\text {EDA }}$ for FERET dataset

![img-3.jpeg](img-3.jpeg)

Figure 9: Percentage usage of Eigenfaces in decreasing order of the eigenvalues Eigen-GEFES $_{\text {SSGA }}$ and Eigen-GEFES $_{\text {EDA }}$ for ESSEX dataset
![img-4.jpeg](img-4.jpeg)

Figure 10: Percentage usage of Eigenfaces in decreasing order of the eigenvalues Eigen-GEFES $_{\text {SSGA }}$ and Eigen-GEFES $_{\text {EDA }}$ for YALE dataset

## V. CONCLUSION AND FUTURE WORK

Our results using GEFeS and GEFeW suggest that hybrid Genetic and Evolutionary Computation for feature selection/weighting enhances the overall performance of the Eigenface methods while reducing the number of features needed. When comparing the SSGA based instances with EDA instances, the EDA instances of GEFeS and GEFeW performed better accuracy. Our future work will be devoted towards investigating the usage of GEFeS and GEFeW for other feature extraction algorithms such as LDA and EBGM.

## ACKNOWLEDGMENT

This research was funded by the Office of the Director of National Intelligence (ODNI), Center for Academic Excellence (CAE) for the multi-university Center for Advanced Studies in Identity Sciences (CASIS) and by the National Science Foundation (NSF) Science \& Technology Center: Bio/computational Evolution in Action CONsortium (BEACON). The authors would like to thank the ODNI and the NSF for their support of this research
