# Genetic \& Evolutionary Biometrics: Hybrid Feature Selection and Weighting for a MultiModal Biometric System 

Aniesha Alford, Crystal Steed, Marcus Jeffrey, Donovan Sweet, Joseph Shelton, Lasanio Small, Derrick Leflore, Gerry Dozier, and Kelvin Bryant<br>Center for Advanced Studies in Identity Sciences<br>North Carolina A \& T State University<br>Greensboro, NC, USA<br>aalford@ncat.edu, ccsteed@ncat.edu, mjeffrey_47@hotmail.com, DonoSweet@gmail.com, jashelt1@ncat.edu, lrsmall@ncat.edu, daleflor@ncat.edu, gvdozier@ncat.edu, ksbryant@ncat.edu

Tamirat Abegaz<br>Computer Science<br>Clemson University<br>Clemson, SC, USA<br>tamirat@programmer.net

John C. Kelly<br>Electrical and Computer Engineering<br>North Carolina A\&T State University<br>Greensboro, NC, USA<br>jck@ncat.edu

Karl Ricanek<br>Center for Advanced Studies in Identity Sciences<br>University of North Carolina at Wilmington<br>Wilmington, NC, USA<br>ricanekk@uncw.edu


#### Abstract

The Genetic \& Evolutionary Computation (GEC) research community is seeing the emergence of a new and exciting subarea, referred to as Genetic \& Evolutionary Biometrics (GEB), as GECs are increasingly being applied to a variety of biometric problems. In this paper, we present successful GEB techniques for multi-biometric fusion and multi-biometric feature selection and weighting. The first technique, known as GEF (Genetic \& Evolutionary Fusion), seeks to optimize weights for score-level fusion. The second technique is known as GEFeWS $_{\text {ML }}$ (Genetic \& Evolutionary Feature Weighting and Selection-Machine Learning). The goal of $\mathrm{GEFeWS}_{\mathrm{ML}}$ is to evolve feature masks (FMs) that achieve high recognition accuracy, use a low percentage of features, and generalize well to unseen subjects. GEFeWS $_{\text {ML }}$ differs from the other GEB techniques for feature selection and weighting in that it incorporates cross validation in an effort to evolve FMs that generalize well to unseen subjects.


Keywords- Biometrics, Cross Validation, Estimation of Distribution Algorithm, Feature Selection, Feature Weighting, Genetic \& Evolutionary Computation, Local Binary Pattern

## I. INTRODUCTION

Genetic \& Evolutionary Computation (GEC) [4, 14, 15, $21,22,35,36]$ is the field of study devoted to the design, development, and analysis of problem solvers based on natural selection [29]. GECs have been successfully used to solve a wide variety of complex, real-world, search, optimization, and machine learning problems for which conventional (and/or traditional) problem solvers yield
unsatisfactory results [4, 30, 31]. GECs have been successfully applied to problems in the areas of robotics (commonly referred to as Evolutionary Robotics) [23], design (commonly referred to as Evolutionary Design) [24], parameter optimization [25], scheduling (commonly referred to as Evolutionary Scheduling) [20], data-mining [42], bioinformatics [33] and cyber security [26], just to name a few.

Recently, the GEC research community has seen an increased interest in the application of GECs to problems within the area of biometrics $[1,2,3,5,6,16,41]$. This growing sub-area of GEC, which can be referred to as Genetic \& Evolutionary Biometrics (GEB), is devoted to the discovery, design, and analysis of evolution-based methods for solving traditional problems within the field of biometrics. To date, GEB techniques have been focused on three areas: feature extraction [16], feature weighting [41], and feature selection $[1,2,3,6]$.

In this paper, we extend the work presented in [6] by first analyzing the effect using the left and right periocular regions as separate biometric modalities has on the performance of Genetic \& Evolutionary Fusion (GEF). We also present a hybrid GEC for feature selection/weighting that dramatically reduces the number of features used while generalizing well to unseen instances. This hybrid GEC is called GEFeWS $_{\text {ML }}$ (Genetic \& Evolutionary Feature Weighting/Selection - Machine Learning). GEFeWS $_{\text {ML }}$ is

used to evolve multi-biometric feature masks via cross validation [37, 38, 39, 40]. The use of cross validation will ensure that overfitting does not occur, and hence, ensure that the evolved feature masks generalize well to unseen images.

The remainder of this paper is as follows. Section II provides an overview of GEB techniques for feature selection. Section III provides a brief overview of GECs, the Local Binary Patterns (LBP) method, and will also provide an introduction to GEF. An overview of how cross validation is used to generalize to unseen instances will be presented as well. Section IV describes $\mathrm{GEFeWS}_{\mathrm{ML}}$, Section V describes our experiments, and Section VI presents our results. Finally, Section VII presents our conclusions and future work.

## II. Related Work

Concerning GEB techniques for feature selection, Galbally et al. [2] developed binary-coded and integercoded Genetic Algorithms (GAs) for feature selection applied to the signature verification problem. The signatures of 330 subjects from the MCYT Signature database [17] were used. Two training sets were formed: one consisting of five signatures of each subject and the other consisting of 20 signatures of each subject. The remaining signatures were used as the test set. Their results showed that both schemes, when compared to the baseline method which used all of the features, were able to reduce the number of features used and improve the recognition accuracy of the system.

Ramadan and Abdel-Kader [1] compared the performances of Particle Swarm Optimization (PSO) [31] and a GA for feature selection for a facial recognition problem. They used the Cambridge ORL database [18], which consists of 10 images of 40 subjects, to evaluate the performances of the PSO and the GA. Four images of each subject were used to form the training set, and six images of each subject were used to form the test set. The Discrete Cosine Transform (DCT) and Discrete Wavelet Transform (DWT) methods were used to extract the original set of features. Their results showed that both GECs performed well in terms of recognition accuracies; however, the PSO used fewer features than the GA.

Kumar et al. [3] compared the performances of a Memetic Algorithm (MA) and a GA for feature selection for a face recognition system. The MA and GA were tested on two facial databases: the ORL database [18], and a subset of the YaleB [19] database (20 subjects). The original feature set was obtained by using the following feature extraction methods: Principal Component Analysis (PCA), Linear Discriminant Analysis, and Kernel PCA. After the original feature set was created, the MA and GA were applied in an effort to reduce the feature set size as well as to increase recognition accuracy.

For their experiments, Kumar et al. used two approaches for designing their training and test sets for each dataset. In the first approach, three random images of each subject were used to form the training set, and the remaining images were
used to form the test set. In the second approach, five random images of each subject were used to form the training set, and the remaining images were used to form the test set. Their results showed that in terms of accuracy and feature reduction, the MA as well as the GA outperformed the baseline methods, which used all of the extracted features. However, the MA proved to be superior to the GA.

In addition to the GEB techniques discussed above, the GEB community is witnessing the development of GEB techniques for multi-biometrics which can be referred to as Genetic \& Evolutionary Multi-Biometrics (GEMB). Genetic \& Evolutionary Fusion (GEF) [34] was developed by Alford et al. and was used to optimally fuse (weight) periocular and facial feature sets to improve recognition accuracy.

Genetic \& Evolutionary Feature Weighting/Selection (GEFeWS) [6], is a hybrid GEC that combines two other methods referred to as Genetic \& Evolutionary Feature Selection and Weighting (GEFeS and GEFeW) for multibiometric feature selection. In [6], instances of GEFeS, GEFeW, and GEFeWS (in the form of steady-state genetic algorithms (SSGAs) [14] and estimation of distribution algorithms (EDAs) [15]) were compared using face only, periocular only, and face + periocular feature templates. The objective of their research was to: (a) evolve feature masks that increase recognition accuracy and (b) test how well the feature masks generalized to unseen subjects.

Their results showed that GEFeWS outperformed both GEFeS and GEFeW and that the EDA instance of GEFeWS outperformed the SSGA instance. All GEFeS, GEFeW, and GEFeWS instances dramatically outperformed the baseline methods that were instances of the LBP and Eigenface methods. Their results also showed that the LBP instances outperformed the Eigenface instances. In addition, the performances of the methods using multiple biometric modalities were superior to those using only a single modality.

In the work discussed in this section, the researchers were focused on optimization - feature set reduction. Many of these techniques also improved the recognition accuracy as well. However, none of the previously mentioned work used cross validation in an effort to prevent the common problem of overfitting [32].

## III. BACKGROUND

## A. Genetic \& Evolutionary Computation (GEC)

GECs are population-based problem solvers based on natural selection [4, 14, 15, 21, 22, 35, 36]. GECs typically work as follows. First, a population of candidate solutions is randomly generated and each candidate solution is assigned a fitness based on a user-defined evaluation function. Parents are then selected from the population, typically based on their fitness, and create offspring. Next, the offspring are assigned a fitness and usually replace the worst performing candidate solutions within the population. This evolutionary process is continued until a user-specified stopping condition is satisfied. Figure 1 shows a pseudocode version of a GEC.


Figure 1. Pseudocode Version of a GEC

## B. Local Binary Patterns (LBP) Method

The Local Binary Patterns (LBP) method is a texture classifying algorithm proposed by Ojala et al. [12] that has been used successfully to extract facial $[6,11,16,28]$ and periocular $[5,6,8,9,10]$ features. The LBP method works as follows. First, an image is segmented into a grid of $N$ evenly sized regions or patches. The intensity values of the internal pixels within each of the patches are compared to its $P$ neighboring pixels on a circle of radius $R$ using Equation 1 , where $i_{c}$ is the intensity value of the center pixel and $i_{p}$ is the intensity value of the $p^{\text {th }}$ neighboring pixel.

$$
s\left(i_{c}, i_{p}\right)=\left\{\begin{array}{l}
1, i f i_{p} \geq i_{c} \\
0, i f i_{p}<i_{c}
\end{array}\right.
$$

A binary pattern, or texture, is then formed by concatenating the resulting values as shown in Equation 2.

$$
T=\left\{s\left(i_{c}, i_{0}\right), s\left(i_{c}, i_{1}\right) \ldots, s\left(i_{c}, i_{P-1}\right)\right\}
$$

Next, the set of all $T$ textures derived for a given patch, are encoded into a histogram where each bin represents the number of times a particular texture pattern is formed. For this research, only uniform patterns, texture patterns with at most two bit changes when traversed circularly, are distinguished within the histograms [8, 13, 28]. Therefore, each histogram consists of $P(P-1)+3$ bins, where $P(P-1)$ bins are for the uniform patterns with exactly two bit changes, two bins are for the uniform patterns with zero bit changes (i.e. all zeros, and all ones), and an additional bin is for all of the non-uniform patterns.

The histograms formed for each of the $N$ patches are concatenated together to form the feature template for an image which consists of $N \times[P(P-1)+3]$ features. In this paper, we use a neighborhood size, $P$, of 8 , and a radius, $R$, of 1 . Therefore our histograms consisted of 59 bins, and the feature templates consisted of $N \times 59$ features.

## C. Genetic \& Evolutionary Fusion (GEF)

Genetic \& Evolutionary Fusion (GEF) [34] was proposed by Alford et al. as an approach for optimizing the weights assigned to biometric modalities for score-level fusion. GEF works as follows. For a multi-biometric system that uses $b$ biometric modalities, GEF evolves a weight, $w_{i}$, within the range $[0 . .1]$ for each biometric modality. The weights are evolved so that the number of recognition errors for the multi-biometric system is minimized. The evolved weights are then normalized so that their sum equals 1 using the following formula:

$$
w_{i}^{\prime}=\frac{w_{i}}{\sum_{j=1}^{b} w_{j}}
$$

where $w_{i}{ }^{\prime}$ is the normalized weight for biometric modality $i$.
The weighted sum rule [27] is then used to fuse the normalized scores returned for the biometric modalities. Using the weighted sum rule, the fused match score, $S$, returned by the multi-biometric system is:

$$
S=\sum_{i=1}^{b} w_{i}^{\prime} s_{i}
$$

where $s_{i}$ is the normalized scores for the $i^{\text {th }}$ biometric.

## D. Machine Learning: Generalization to Unseen Instances via Cross Validation

The goal of any machine learning technique is to develop an artifact (in the form of a neural network, classifier, decision tree, neuro-fuzzy inference system, etc.) that generalizes well to unseen instances [37, 38, 39, 40]. Most machine learning techniques, including GECs [32, 42], will tend to overfit the set of training instances - those instances that are 'seen' by the machine learning technique as it attempts to develop a high performance artifact for classification or regression. This means that the best performing artifact, with respect to the training set, will perform well on these 'seen' instances but will perform relatively poorly on the 'unseen' instances of a test set.

The concept of cross validation [32, 37, 38, 39, 40] was developed in an effort to prevent overfitting. In cross validation, the total set of available instances is broken up into three sets: a training set, a validation set, and a test set. The training set contains instances that are 'seen' by the machine learning technique while the validation and test sets contain instances that are 'unseen' by the learning technique.

As a machine learning technique attempts to develop artifacts that reduce the classification/regression error on the training set, periodically, artifacts are checked with the validation set. An artifact's performance on the validation set is kept 'hidden' from the machine learning technique. After a user-specified number of artifacts have been developed without reducing the overall best error on the validation set, the learning technique is halted and the artifact with the best performance on the validation set is extracted and applied to the test set and future unseen instances.

As long as a machine learning technique interacts with a training set, the corresponding error rates of successive artifacts will typically move towards zero. The validation set is used to approximate the actual error associated with an artifact if it were to be applied to a test set of unseen instances [32].

## IV. $\mathrm{GEFeWS}_{\mathrm{ML}}$

Genetic \& Evolutionary Feature Weighting and Selection (GEFeWS) [6], is a hybrid GEC proposed by Alford et al. that combines Genetic \& Evolutionary Feature Selection (GEFeS) and Weighting (GEFeW). GEFeWS evolves a population of real-valued candidate feature masks (FMs). Each candidate $\mathrm{FM}, f m_{i}$, can be viewed as a tuple $\left(\mathrm{M}_{i}, f i t_{i}\right)$ where $\mathrm{M}_{i}=\left\{\mu_{i, 0}, \mu_{i, 1}, \ldots, \mu_{i, n-1}\right\}$ and where $\mu_{i, j}$ is the $j^{\text {th }}$ mask value for $f m_{i}$. The value $f i t_{i}$ represents the fitness of $f m_{i}$. The mask values are initially within the range [0..1]. For GEFeWS, values within a FM that are less than 0.5 are set to 0 and the corresponding biometric feature is not used during matching; otherwise, the value is used to weight the corresponding biometric feature.

For GEFeWS, the following weighted Manhattan distance is used to compare two feature templates, $h_{j}$ and $h_{i}$ :

$$
\begin{aligned}
w M D_{W S}\left(h_{j}, h_{i}, f m_{i}\right) & =\sum_{k=0}^{n-1}\left|h_{j, k}-h_{i, k}\right| f_{W S}\left(\mu_{i, k}\right) \\
f_{W S}\left(\mu_{i, k}\right) & =\left\{\begin{array}{l}
1, i f \mu_{i, k} \geq 0.5 \\
0, \text { otherwise }
\end{array}\right.
\end{aligned}
$$

where $n$ is the original number of features, $\mu_{i, k}$ is a FM value, $k$ is the $k^{\text {th }}$ feature, and the function $f_{W S}$ represents the process of feature weighting/selection as performed by GEFeWS. The subject associated with the template within the gallery set with the smallest weighted Manhattan distance when compared to the probe was considered the match.

Each candidate FM is assigned a fitness using the following evaluation function:

$$
f i t_{i}=10 \varepsilon+\frac{m}{n}
$$

where $c$ is the number of recognition errors that occurred when the candidate FM was applied to the probe and gallery templates, where $m$ is the number of features used by the candidate FM, and where $n$ is the original number of features in the biometric templates. In addition, for each candidate FM, the weights for the biometric feature templates were co-evolved for score-level fusion as in GEF [34].

GEFeWS $_{\text {ML }}$ is similar to GEFeWS with the exception that the machine learning concept of cross validation is incorporated. Alford et al. [6] showed that the EDA instance of GEFeWS outperformed the SSGA instance. Therefore, in this paper GEFeWS $_{\text {ML }}$ is an instance of an EDA [15].

GEFeWS $_{\text {ML }}$ works as follows. First, an initial population of $Q$ candidate FMs is randomly generated. Each candidate FM is evaluated, using Equation 5, based on its performance on the training set. The candidate FMs are also applied to the validation set, and the best performing candidate FM on the validation set, which will be referred to as $F M^{*}$, is retained. Next, the top $50 \%$ of the candidate FMs in the initial population are used to form a probability density function (PDF). The PDF is then sampled to create $(1-\alpha) Q$ offspring FMs, where $\alpha$ is a user-defined percentage. The
offspring are then evaluated based on the training set. The offspring are also evaluated based on the validation set and their performances are then compared to the performance of $F M^{*}$. If an offspring's performance is better than $F M^{*}$, the offspring will become the new $F M^{*}$. A new population is then formed using $\alpha Q$ of the best performing candidate FMs in the current population, known as the elites [22], and the $(1-\alpha) Q$ offspring. This process continues until a userspecified stopping condition is satisfied. When the stopping condition is satisfied, the best performing FM on the training set, which is referred to as $F M^{o}$, as well as $F M^{*}$ are returned. Figure 2 provides a flow chart of the GEFeWS $_{\text {ML }}$ learning process.
![img-0.jpeg](img-0.jpeg)

Figure 2. Flowchart of the GEFeWS $_{\text {ML }}$ Learning Process

## V. EXPERIMENTS

Two experiments were performed: one to evaluate the effectiveness of GEF and another to evaluate the effectiveness of GEFeWS $_{\text {ML }}$.

The datasets used for our experiments were extracted from the Face Recognition Grand Challenge (FRGC) database [7]. From FRGC, a total of 309 subjects were selected. The training set consisted of images of 105 subjects and will be referred to as FRGC-105. The validation set consisted of images of an additional 105 subjects and will be referred to as FRGC-105b. The testing set consisted of the images of the remaining 99 subjects and will be referred to as FRGC-99. For each dataset, three frontal images of each subject were selected. One image of each subject was used to form the probe set and an additional two images of each subject were used to form the gallery set. These images were used for extraction of both the facial and periocular features.

The facial images were pre-processed as follows. The selected images were first cropped to include only the face

region (i.e. no background and little hair). The images were then resized to $100 \times 127$ pixels, converted to grayscale, and histogram equalization was performed. The LBP method was then used to extract 2124 ( 36 patches $\times 59$ bins) facial features from each image.

The periocular images were pre-processed as follows. First, the left and right periocular regions were cropped individually from each image. The extracted periocular regions were then converted to grayscale and histogram equalization was performed. In addition, the centers of the periocular images were masked to eliminate the effect of texture and color in the iris and sclera area, as was done in [10]. The LBP method was then used to extract 1416 (24 patches $\times 59$ bins) periocular features from each region. In this research, there were two schemes for the periocular templates: (1) using the periocular region as one biometric modality, and (2) using the periocular regions as two distinct biometric modalities. For the first scheme, the feature templates for the left and right periocular regions were concatenated together to form a feature template consisting of 2832 ( 1416 features per periocular region) periocular features. For the second scheme, the left and right periocular regions were considered separately, each represented by a feature template consisting of 1416 features.

For our experiments, GEF and GEFeWS $_{\text {ML }}$ were implemented using the eXploration Toolset for the Optimization of Launch and Space Systems (X-TOOLSS) [43, 44]. For our first experiment, GEF was used to evolve weights for the FRGC-105 facial and periocular templates. For our second experiment, $\mathrm{GEFeWS}_{\mathrm{ML}}$ was used to evolve FMs for the FRGC-105 face, periocular, and face + periocular templates. This will be referred to as FRGC-105 Optimization because we are attempting to minimize the number of features necessary for recognition while increasing the recognition accuracy. The best performing FMs on the training set, $F M^{*} s$, were then applied to the test set in order to evaluate how well they generalized to unseen subjects. This will be referred to as FRGC-99 Opt-Gen. In addition, the best performing FMs on the validation set, $F M^{*} \mathrm{~s}$, were applied to the test set in order to evaluate how well they generalized to unseen subjects within the test set. This will be referred to as FRGC-99 Val-Gen.

## VI. RESULTS

## A. Experiment 1: GEF

For our first experiment, GEF, which was an instance of an EDA, was used to evolve weights for (a) the facial + combined periocular (denoted as Periocular ${ }_{c}$ ) features and (b) the facial + left periocular + right periocular (denoted as Periocular ${ }_{L R}$ ) features. The EDA evolved a population of 20 candidate weight sets and kept the $5(\alpha=25 \%)$ best performing candidate weight sets, known as elites. GEF was run 30 times with a maximum of 1000 function evaluations allowed during each run.

Table 1 shows the results of our experiment. The first column represents the biometric modalities. The second column represents the methods, where the subscripts denote
the average normalized weight assigned to the facial and periocular features respectively. The final columns represent the average recognition accuracy.

Both methods resulted in $100 \%$ recognition accuracy. In addition, both methods placed more emphasis on the facial features, assigning them the highest weight. In addition, the method for the Face + Periocular ${ }_{\mathrm{LR}}$ features assigned lower weights to the left periocular features. This could be due to illumination variation within the two periocular regions as well as the fact the face isn't symmetric.

TABLE I. GENETIC \& EVOLUTIONARY FUSION RESULTS


## B. Experiment 2: GEFeWS $_{M L}$

For our second experiment, the EDA instance of $\mathrm{GEFeWS}_{\mathrm{ML}}$ evolved a population of 20 candidate FMs and kept $5(\alpha=25 \%)$ elites. $\mathrm{GEFeWS}_{\mathrm{ML}}$ was run 30 times, with a maximum of 1000,2000 , and 4000 function evaluations allowed. At the end of each run, the best performing FM on the training set, $F M^{*}$, and the best performing FM on the validation set, $F M^{*}$, were returned. These FMs were then applied to the test set, FRGC-99.

The optimization and generalization performances are presented in Table 2. Because using 4000 function evaluations performed best, only those results are presented. The first column represents the biometric modality and the second column represents the methods that were compared. For the methods, the feature templates that were used by the $\mathrm{GEFeWS}_{\mathrm{ML}}$ instances are denoted in parentheses. Face $_{\mathrm{L}}$ refers to the facial LBP features, Periocular ${ }_{C}$ refers to the combination of the left and right periocular LBP features, and Periocular ${ }_{\mathrm{LR}}$ refers to using the left and right periocular regions independently. The third column represents the FRGC-105 Optimization performance, the fourth column represents the FRGC-99 Opt-Gen performance, and the final column represents the FRGC-99 Val-Gen performance. For the last three columns, the first number denotes the average recognition accuracy achieved by the 30 FMs and the number in parentheses denotes the average percentage of features used by the 30 FMs . In addition, the baselines for the test set are shown under the Val-Gen column and are denoted by an asterisk.

The results of our experiments were separated into equivalence classes based on accuracy and the percentage of features used by performing ANOVA and t-tests.

## 1) Face-Only

With respect to the Face-Only FRGC-105 Optimization results, $\mathrm{GEFeWS}_{\mathrm{ML}}$ outperformed the baseline method, achieving a $99.6 \%$ average recognition accuracy, while using an average of $34.4 \%$ of the features.

When the FM's were applied to the test set, the average recognition rate was $97.5 \%$. In comparison, when the FM's

TABLE II. GEFeWS ${ }_{\text {ML }}$ Optimization and GENERALIZATION ReSults

were applied to the test set, they outperformed the FM's in terms of accuracy, achieving an average recognition rate of $98.5 \%$. This result shows that cross validation improves the performance when generalizing to unseen instances. In terms of the percentage of features used, the Val-Gen performances used more features than the Opt-Gen performances. This is most likely due to the fact that more features may be needed for adequate generalization.

In addition, although the generalization performances were lower than the performance of the baseline method, it's important to note that for the baseline method, LBP was applied directly to the test set.

## 2) Periocular-Only

With respect to the Periocular-Only FRGC-105 Optimization results, both GEFeWS $_{\text {ML }}$ methods outperformed the baseline method in terms of accuracy and the percentage of features used. When the performances of the two GEFeWS $_{\text {ML }}$ methods were compared, Periocular $_{\text {LR }}$ performed best in terms of accuracy while Periocular ${ }_{\mathrm{C}}$ performed best in terms of feature reduction.

With respect to the Opt-Gen performances, Periocular ${ }_{\mathrm{C}}$ performed best in terms of accuracy and the percentage of features used. With respect to the Val-Gen performances, Periocular ${ }_{\mathrm{C}}$ also achieved higher recognition accuracies and used a fewer percentage of features; however, there was not a statistically significant difference in the performances.

When the Opt-Gen and Val-Gen performances were compared, the Val-Gen performances were better in terms of accuracy, but used significantly more features than the Opt-Gen performances. Again, this may be an indication that more features are necessary for generalization.

In summary, combining the left and right periocular feature templates (Periocular ${ }_{\mathrm{C}}$ ) would be the best method to use for periocular recognition. The evolved FMs and the best performing FMs on the validation set generalized better than the FMs formed via Periocular ${ }_{\text {LR }}$.

## 3) Face + Periocular

With respect to the Face + Periocular FRGC-105 Optimization results, GEFeWS $_{\text {ML }}$ achieved $100 \%$ recognition accuracy for both schemes. However, the Face

+ Periocular ${ }_{\mathrm{C}}$ templates performed best in terms of feature usage.

With respect to the FRGC-99 Opt-Gen results, the FM ${ }^{\mathrm{ts}}$ for both schemes generalized well to the test set, outperforming the baseline method by achieving higher recognition accuracies while using significantly fewer features. There was not a statistically significant difference between the performances of the two GEFeWS $_{\text {ML }}$ methods in terms of accuracy, however when GEFeWS $_{\text {ML }}$ was applied to the Face + Periocular ${ }_{\mathrm{C}}$ templates, it resulted in the use of the fewest percentage of features.

With respect to the FRGC-99 Val-Gen results, the FM's generalized well to the test set. Both schemes achieved an average recognition rate of $99.4 \%$, outperforming the baseline method. However, the Face + Periocular ${ }_{\mathrm{C}}$ templates used the least percentage of features.

In summary, combining the periocular regions would also be the best method to use for face + periocular recognition. Using the Periocular ${ }_{\mathrm{C}}$ features resulted in practically the same recognition accuracies as using Periocular ${ }_{\mathrm{LR}}$ while using statistically fewer features.

## VII. CONCLUSION AND FUTURE WORK

In this paper, we explored the use of two periocular recognition schemes for GEF and also introduced GEFeWS $_{\text {ML }}$, a hybrid GEC for feature selection/weighting that incorporated cross validation to evolve feature masks that generalize well to unseen subjects extracted from the FRGC database.

Our results showed that it is efficient to use the left and right periocular regions as one biometric modality instead of two. In addition, GEFeWS $_{\text {ML }}$ was able to achieve high recognition rates while using less than $50 \%$ of the features. Our results also showed that the feature masks evolved via the validation set performed better than those evolved via the training set for the face-only and periocular-only templates.

Our future work will be devoted towards further improvement in the generalization performance of GEFeWS $_{\text {ML }}$ and will include the development of diverse training, validation, and test sets taken from a variety of databases.

## ACKNOWLEDGMENT

This research was funded by the Office of the Director of National Intelligence (ODNI), Center for Academic Excellence (CAE) for the multi-university Center for Advanced Studies in Identity Sciences (CASIS), NSF SSTEM, Lockheed Martin and the National Science Foundation (NSF) Science \& Technology Center: Bio/computational Evolution in Action CONsortium (BEACON). The authors would like to thank the ODNI, the NSF, and Lockheed Martin for their support of this research.
