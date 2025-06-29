# Genetic \& Evolutionary Biometrics: Feature Extraction from a Machine Learning Perspective 

Joseph Shelton, Aniesha Alford, Lasanio Small, Derrick Leflore, Jared Williams, Joshua Adams, Gerry Dozier, Kelvin Bryant<br>Center for Advanced Studies in Identity Sciences<br>NC A\&T<br>Greensboro, USA<br>jashelt1@ncat.edu,aalford@ncat.edu<br>,lrsmall@ncat.edu, daleflor@ncat.edu, jcwill24@gmail.com, jcadams2@ncat.edu, gvdozier@ncat.edu, ksbryant@ncat.edu


#### Abstract

Genetic \& Evolutionary Biometrics (GEB) is a newly emerging area of study devoted to the design, analysis, and application of genetic and evolutionary computing to the field of biometrics. In this paper, we present a GEB application called $\mathrm{GEFE}_{\mathrm{ML}}$ (Genetic and Evolutionary Feature Extraction Machine Learning). $\mathrm{GEFE}_{\mathrm{ML}}$ incorporates a machine learning technique, referred to as cross validation, in an effort to evolve a population of local binary pattern feature extractors (FEs) that generalize well to unseen subjects. $\mathrm{GEFE}_{\mathrm{ML}}$ was trained on a dataset taken from the FRGC database and generalized well on two test sets of unseen subjects taken from the FRGC and MORPH databases. $\mathrm{GEFE}_{\mathrm{ML}}$ evolved FEs that used fewer patches, had comparable accuracy, and were $\mathbf{5 4 \%}$ less expensive in terms of computational complexity.


Keywords- Biometrics, Cross Validation, Estimation of Distribution Algorithm, Feature Extraction, Genetic \& Evolutionary Computation, Local Binary Pattern

## I. INTRODUCTION

Genetic \& Evolutionary Biometrics (GEB) [8,21,22,23] is an emerging sub-area of Genetic \& Evolutionary Computation (GEC) $[10,12,13,16,19,20,24,27,28,29,30]$ that is devoted to the design, development, and application of Darwinian-style methods (those based on natural selection [25]) for solving problems within the area of biometrics. These methods (also referred to as GECs) discover optimal or near optimal solutions to problems as follows. Initially, a population of randomly generated candidate solutions (CSs) is created. Each CS is then evaluated and assigned a fitness based on a user-specified evaluation function, which is used to determine its relative 'goodness'. Next, parents are chosen from the population based on their fitness and are allowed to create offspring CSs.

Tamirat Abegaz<br>Computer Science<br>Clemson University<br>Clemson, SC, USA<br>tamirat@programmer.net

Karl Ricanek<br>Computer Science Department<br>UNC-W<br>Wilmington, USA<br>ricanekk@uncw.edu

The offspring are each assigned a fitness and typically replace weaker members of the previous population. This evolutionary process of selecting parents, allowing them to procreate, and replacing weaker members of the population with the newly formed offspring is repeated until a user-specified stopping condition is reached. Such stopping conditions would be a certain number of evaluations executing, populations converging onto a solution, or the GEC finding an optimal solution. Figure 1 provides a flowchart of a typical GEC.
![img-0.jpeg](img-0.jpeg)

Figure 1. Flowchart of a Typical GEC
In [4], Shelton et al. developed a GEC in the form of a genetic \& evolutionary feature extractor (GEFE). GEFE was used to evolve a population of Local Binary Pattern [1,2,3,5,6] (LBP)

based feature extractors (FEs). These FEs were of two types: (a) those that consisted of patches that were of non-uniform size and (b) those that consisted of patches that were of uniform size. The evolved FEs used a small number of patches (approximately 8) that covered only a small portion of an image (approximately $25 \%$ ) while outperforming the standard LBP approach.
In their paper, Shelton et al. worked with GEFEs that were instances of two well-known GECs: a steady-state genetic algorithm (SSGA) [15] and an estimation of distribution algorithm (EDA) [14]. Their results showed that the GEFE instances that evolved FEs composed of uniform sized patches were superior to those instances that evolved non-uniformed sized patches. Their results also showed that those GEFE instances that were EDAs outperformed their SSGA counterparts. All GEFE instances outperformed the standard LBP method in terms of recognition accuracy while using approximately $1 / 3$ the number of features.
Shelton et al.'s rationale for reducing the number features used for recognition was motivated by a two-stage hierarchical recognition system proposed by Gentile et al. [17]. This system reduced the overall number of feature checks needed for recognition by first comparing a probe, $p$, using a short-length biometric template (of the $n$ subjects within a dataset) consisting of a subset of $k$ features to obtain a set of $r$ subjects of the dataset that matched $p$ the closest. Next, $p$ is compared with the $r$ subjects using the full biometric template of $m$ features. The proposed system in [8] had a total computational complexity, with respect to feature checks, of $n k+r m$ which resulted in fewer feature checks of a conventional biometric recognition system which has a computational complexity of $n m$.
Since Shelton et al. were primarily focused on evolving short-lengthed biometric templates for a 'Gentile-style' recognition system, their GEFE instances trained on a subset of the images of all of the $n$ subjects of the dataset. In this paper, we extend the work of Shelton et al. to investigate how well the FEs evolved by GEFE generalize to unseen subjects by incorporating the machine learning concept of cross validation [31,32,33,34,35]. This GEB application will be referred to as Genetic and Evolutionary Feature Extraction - Machine Learning (GEFE ${ }_{\text {ML }}$ ).
The remainder of this paper is as follows: Section 2 provides an overview of LBP and an EDA. Section 3 provides a description of GEFE $_{\text {ML }}$, specifically, the representation of a FE, the function used to evaluate FEs via a training set, and evolving FEs using cross validation. Sections 4 and 5 present our experiments and our results. Section 6 provides a brief discussion. Our conclusions and future work are presented in Section 7.

## ILBACKGROUND

## A. LBP

LBP is a feature extraction technique that uses the textures of an image to create a feature vector for it. The common way to perform LBP is by first separating an entire image into even sized patches [6] as shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Standard LBP
Within each patch, a texture pattern can be extracted for each pixel, $C_{p}$ in the patch that has $t$ neighboring pixels surrounding it. The value of $t$ and the distance between neighboring pixels and $C_{p}$ are user specified. The pixel intensity values between $C_{p}$ and its neighboring pixels are compared and a texture pattern is produced. The pattern is represented as a binary string and is produced by taking the difference of each neighboring pixel and $C_{p}$. If the difference is negative, the texture pattern will have a zero bit in the position of the string relative to the position of the neighboring pixel with $C_{p}$; else the bit will have a one bit, meaning the length of the string will be equal to the number of neighboring pixels, $t$.
Each patch has a histogram associated with it, and the histogram keeps track of the frequencies of patterns within that patch. For a neighborhood size of $t$, there are $2^{t}$ possible patterns that can be extracted. To reduce the number of frequencies in histograms, the patterns are classified as uniform or non-uniform. A uniform pattern is a pattern where the bit changes two or less times when traversing it circularly and a non-uniform pattern would have more than two bit changes. This reduces the size of a histogram from $2^{t}$ to ( $t^{*}$ $(t-1))+2$; there are $t^{*}(t-1)$ patterns with exactly two changes and there are two patterns with no changes, specifically the patterns consisting of all zeros and all ones. The definition of uniform and non-uniform patterns is given more detail in [6].
The frequencies from the histograms of each patch are concatenated to form a feature vector for an image. The feature vector can be compared to other feature vectors of images using some distance measure, and the resulting measure with represent the similarity of vectors and, consequently, images.

## B. $E D A$

In [4], an EDA instance of GEFE outperformed the SSGA instance, which is the rationale for only using an EDA in this research. An EDA initially creates a population of candidate FEs, and these FEs are evaluated based on some fitness

evaluation. The top $50 \%$ of FEs from the population are selected and a probability density function (PDF) is built. Offspring are created from sampling the PDF, and they are then evaluated and assigned fitness. The offspring and an arbitrary number of best performing FEs, the elites, from the previous population make up a new population. The newer population undergoes the process of creating offspring and replacement until some terminating condition has been met.

## III. GEFEML

## A. Representation of Candidate FEs

A definition of a $\mathrm{FE}, \mathrm{fe}_{\mathrm{i}}$, can be found in [4]. The definition states that $\mathrm{fe}_{\mathrm{i}}$ can be represented as a six-tuple, $<\mathrm{X}_{\mathrm{i}}, \mathrm{Y}_{\mathrm{i}}, \mathrm{W}_{\mathrm{i}}, \mathrm{H}_{\mathrm{i}}, \mathrm{M}_{\mathrm{i}}, \mathrm{f}_{\mathrm{i}}>$. $\mathrm{X}_{\mathrm{i}}=\left\{\mathrm{x}_{\mathrm{i}, 0}, \mathrm{x}_{\mathrm{i}, 1}, \ldots, \mathrm{x}_{\mathrm{i}, \mathrm{n}-1}\right\}$ and $\mathrm{Y}_{\mathrm{i}}=\left\{\mathrm{y}_{\mathrm{i}, 0}\right.$, $\left.y_{i, 1}, \ldots, y_{i, n-1}\right\}$ represents the x-coordinates and the y-coordinates of the center of the $n$ possible patches. The widths and heights of the $n$ patches are represented by $\mathrm{W}_{\mathrm{i}}=$ $\left\{\mathrm{w}_{\mathrm{i}, 0}, \mathrm{w}_{\mathrm{i}, 1}, \ldots, \mathrm{w}_{\mathrm{i}, \mathrm{n}-1}\right\}$ and $\mathrm{H}_{\mathrm{i}}=\left\{\mathrm{h}_{\mathrm{i}, 0}, \mathrm{~h}_{\mathrm{i}, 1}, \ldots, \mathrm{~h}_{\mathrm{i}, \mathrm{n}-1}\right\}$. Because the patches are uniform, $\mathrm{W}_{\mathrm{k}}=\left\{\mathrm{w}_{\mathrm{k}, 0}, \mathrm{w}_{\mathrm{k}, 1}, \ldots, \mathrm{w}_{\mathrm{k}, \mathrm{n}-1}\right\}$ is equivalent to, $\mathrm{w}_{\mathrm{k}, 0}=\mathrm{w}_{\mathrm{k}, 1}, \ldots, \mathrm{w}_{\mathrm{k}, \mathrm{n}-2}=\mathrm{w}_{\mathrm{k}, \mathrm{n}-1}$, and $\mathrm{H}_{\mathrm{k}}=\left\{\mathrm{h}_{\mathrm{k}, 0}, \mathrm{~h}_{\mathrm{k}, 1}, \ldots, \mathrm{~h}_{\mathrm{k}, \mathrm{n}-1}\right\}$ is equivalent to, $\mathrm{h}_{\mathrm{k}, 0}=\mathrm{h}_{\mathrm{k}, 1}, \ldots, \mathrm{~h}_{\mathrm{k}, \mathrm{n}-2}=\mathrm{h}_{\mathrm{k}, \mathrm{n}-1}$. We use uniform sized patches due to results in [4]. $\mathrm{M}_{\mathrm{i}}=\left\{\mathrm{m}_{\mathrm{i}, 0}, \mathrm{~m}_{\mathrm{i}, 1}, \ldots, \mathrm{~m}_{\mathrm{i}, \mathrm{n}-1}\right\}$ represents the masking values for each patch and $\mathrm{f}_{\mathrm{i}}$ represents the fitness of $\mathrm{fe}_{\mathrm{i}}$. The masking value determines whether a patch is activated or deactivated.

## B. Evaluation function of a FE

To evaluate the fitness of a FE, we apply it to a dataset of subjects, $D$. Each subject has a series of snapshots, and one snapshot is assigned to a probe set, while the other snapshots are applied to a gallery set. A FE, $f e_{i}$, is applied to the probe set and gallery set to create FVs for all images. FVs from the probe set are matched to all FVs in the gallery set, and whichever two images are considered the closet and do not belong to the same subject is considered an error. The fitness, $f_{i}$, associated with a candidate $\mathrm{FE}, f e_{i}$, is equal to the number of incorrect matches, $c(D)$, multiplied by 10 plus the percentage of image space (measured in pixels) covered by $f e_{i}, \gamma\left(f e_{i}\right)$. Equation 1 provides an example of the evaluation function used by $\mathrm{GEFE}_{\mathrm{ML}}$ to assign fitnesses to candidate FEs.

$$
f_{i}=10 \varepsilon(D)+\gamma\left(f e_{i}\right)
$$

## C. Cross Validation in $G E F E_{M L}$

We demonstrate how cross validation recorded the best generalizing FE during the evolutionary process in Figure 3. Initially, all candidate FEs are evaluated on the training set and the validation set. The best fit FE on the validation set is labelled FE*. After offspring FEs have been created, they are evaluated on thee training set and validation set. Any offspring FE that outperforms FE* becomes the new FE*. After a stopping condition is satisfied, two FEs are returned: the best performing FE on the training set, $\mathrm{FE}^{\mathrm{in}}$, and $\mathrm{FE}^{*}$.

## IV. EXPERIMENTS

In our two experiments, four datasets were taken from the Facial Recognition Grand Challenge (FRGC) [7] and the Craniofacial Longitudinal Morphological Face (MORPH) [26] databases. From the FRGC database, a total of 314 subjects were used to create three datasets: FRGC-100a, consisting 100 subjects, FRGC-109, consisting of 109 subjects, and FRGC-100b consisting of 100 subjects different from those inn FRGC-100a. MORPH-500, was formed by using 500 subjects taken from the MORPH database.
![img-2.jpeg](img-2.jpeg)

Figure 3. Flowchart of the Evolutionary Process of $\mathrm{GEFE}_{\mathrm{ML}}$ using Cross validation

In Experiment I, FRGC-100a was used as the training set, FRGC-109 as the validation set, and FRGC-100b was used as a test set. In Experiment II, MORPH-500 was used as a second test set. The datasets consisted of 3 images for each subject and were further divided into a probe set consisting of one image and a gallery set consisting of the other two images. Figure 4 provides an example of a subject from FRGC and MORPH. All images were pre-processed, aligned in a similar matter, and had the dimensions of $100 \times 127$ pixels.

In both experiments, the objective was twofold: to evolve FEs that generalize well to unseen subjects and to evolve FEs that are more efficient in terms of the amount of processing (associated computational complexity) needed to extract features from an image. In terms of computing the computational complexity of a FE, the fundamental unit of work used was the number of pixels that needed to be processed. The total amount of work, $w_{i}$, done by a candidate

FE, $f e_{i}$, can be expressed as follows where $x_{i}$ and $y_{i}$ represent the dimensions of each patch (in pixels) within $f e_{i}$ and where $n_{i}$ represents the number of patches within $f e_{i}$ : $w_{i}\left(n_{i} x_{n_{i}} y_{i}\right)=$ $n_{i}\left(x_{i}-2\right)\left(y_{i}-2\right)$.
![img-6.jpeg](img-6.jpeg)

Probe Image
![img-7.jpeg](img-7.jpeg)

Gallery Image Gallery Image
Figure 4a. Subject Snapshots from FRGC
![img-5.jpeg](img-5.jpeg)

Probe Image Gallery Image
![img-6.jpeg](img-6.jpeg)

Gallery Image Gallery Image
Figure 4b. Subject Snapshots from MORPH

## V. RESULTS

The results for both experiments were generated as follows. $\mathrm{GEFE}_{\mathrm{ML}}$ was run 30 times with maximum function evaluation limits of 1000, 2000, 3000 and 4000 (a total of 120 runs in all). On each run, $\mathrm{GEFE}_{\mathrm{ML}}$ returned the best performing FE on the training set $\left(\mathrm{FE}^{\mathrm{n}}\right)$, and the best performing FE with respect to the validation set (FE*). In addition, on each run, $\mathrm{GEFE}_{\mathrm{ML}}$ evolved a population of 20 candidate FEs and always allowed the best individual to remain in the population.

In both experiments, the standard LBP method was used as the baseline. This baseline method divided an image into a 6 by 4 set of nearly uniform sized patches. These patches were as follows: 15 patches were of $17 \times 32$ pixels, 5 patches were of $17 \times 31,3$ patches were of $15 \times 32$ pixels, and 1 patch was $15 \times 31$ pixels. No overlap occurred between patches. $\mathrm{GEFE}_{\mathrm{ML}}$ was allowed to evolve FEs consisting of a number of uniform sized patches ranging from [1..24] and the patches were allowed to overlap.

## A. Results: Experiment I

Table I presents the results of Experiment I. The first column denotes the method used and the number of FE evaluations that were performed. The second column represents the results of applying the corresponding method to FRGC-100a. The third column represents the results of how well the $30 \mathrm{FE}^{\mathrm{n}} \mathrm{s}$ generalized on FRGC-100b, and the final column represents the results of how well the $30 \mathrm{FE} * \mathrm{~s}$ generalized on FRGC-100b. For these columns, the first number represents the average recognition accuracy and the second number represents the average computational complexity.

In terms of recognition accuracy and computational complexity, $\mathrm{GEFE}_{\mathrm{ML}}$ outperformed the baseline method for both FRGC-100a optimization and FRGC-100b Val-Gen. On FRGC-100a optimization, $\mathrm{GEFE}_{\mathrm{ML}}$ evolved $\mathrm{FE}^{\mathrm{n}} \mathrm{s}$ that had $100 \%$ recognition accuracy. The average computational complexities of the $\mathrm{FE}^{\mathrm{n}} \mathrm{s}$ were approximately $45 \%$ less than the baseline computational complexity. When the $\mathrm{GEFE}_{\mathrm{ML}}$ Opt-Gen performances were compared in terms of accuracy, there was no significant difference. Likewise, when the $\mathrm{GEFE}_{\mathrm{ML}}$ Val-Gen performances were compared in terms of accuracy, there was no significant difference. However, when the $\mathrm{GEFE}_{\mathrm{ML}}$ Opt-Gen performances were compared to the $\mathrm{GEFE}_{\mathrm{ML}}$ Val-Gen performances in terms of recognition accuracy, the Val-Gen performances were statistically better. These results were confirmed through the use of an ANOVA and t-tests.

For Experiment I, $\mathrm{GEFE}_{\mathrm{ML}}$ with 1000 evaluations achieved the highest recognition accuracy for Opt-Gen and Val-Gen. For this method, the baseline, $\mathrm{FE}^{\mathrm{n}}$ and $\mathrm{FE}^{*}$ are shown in Figure 5.

When comparing the images, the areas of the patches within $F E^{\mathrm{n}}$ and $F E^{*}$ are much smaller than the area of the baseline method. Additionally, one can observe that the patches within $F E^{\mathrm{n}}$ and $F E^{*}$ are clustered predominantly within the periocular region. This result supports the research of Miller et al. [5] that suggests that the periocular region can be a highly discriminating modality for recognition. Also, notice that $F E^{*}$ appears to extract more features from the periocular region than $F E^{\mathrm{n}}$. This observation suggests that in order to adequately generalize to unseen subjects a slight increase in the number of features may be required.
![img-7.jpeg](img-7.jpeg)

Figure 5. Baseline, $\mathrm{FE}^{\mathrm{n}}$ and $\mathrm{FE}^{*}$ on FRGC-100

## B. Results: Experiment II

Table II presents the results of Experiment II. As in Table I, the first column denotes the method used and the number of evaluations used. The second column represents the results of

how well the $30 \mathrm{FE}^{\text {ts }}$ generalized on MORPH-500 (the second test set), and the final column represents the results of how well the $30 \mathrm{FE} *$ s generalized on MORPH-500.

TABLE II: GENERALIZING ON MORPH DATASET

For Experiment II, $\mathrm{GEFE}_{\mathrm{ML}}$ achieved lower average recognition accuracies than the baseline method; however, the computational costs of the GEFEMI, methods were significantly lower than the baseline due to the reduction of the size and the number of patches. When the accuracies of the $\mathrm{GEFE}_{\mathrm{ML}}$ methods were compared to each other, for Opt-Gen and Val-GEN, the method with 2000 evaluations performed poorer than the other methods. When comparing the Opt-Gen accuracy to the Val-Gen accuracy, the performances of the $\mathrm{FE} * \mathrm{~s}$ (for 1000, 2000, 3000, and 4000 evaluations) outperformed their Opt-Gen counterparts. These results were, once again, confirmed using an ANOVA and a t-test. The $\mathrm{GEFE}_{\mathrm{ML}}$ that was allowed to use 4000 evaluations achieved the highest average recognition accuracy. Figure 6 shows the baseline, $\mathrm{FE}^{\mathrm{ts}}$, and $\mathrm{FE}^{*}$ on MORPH-500.
![img-8.jpeg](img-8.jpeg)

## VI. DISCUSSION

In Experiment I, $\mathrm{GEFE}_{\mathrm{ML}}$ performed better than the baseline method in terms of average recognition accuracy and average computational complexity. In Experiment II, the average performance of $\mathrm{GEFE}_{\mathrm{ML}}$ did not outperform the baseline method in regards to accuracy; however $\mathrm{GEFE}_{\mathrm{ML}}$ had approximately a $40 \%$ reduction in computational complexity.

The Cumulative Match Characteristic (CMC) curves and the Receiver Operator Characteristic (ROC) curves provide further analysis of the performance of $\mathrm{GEFE}_{\mathrm{ML}}$. The ROC curves were created using the normalized Manhattan Distance formula, $N M D[8]$, shown in Equation 2, where $h_{i}$ and $h_{j}$ represent the two feature vectors being compared, $l$ represents the length of the feature vectors, and $z$ represents the $z^{\text {th }}$ feature in a feature vector.

$$
N M D\left(h_{i}, h_{j}\right)=\sum_{i=0}^{j-1} \frac{\left|h_{i, z}-h_{j, z}\right|}{\max \left(h_{i, z}-h_{j, z}\right)}
$$

The generalizing performance of the best $\mathrm{FE}^{*}$ and the best $\mathrm{FE}^{\text {ts }}$ were measured on FRGC-100 and MORPH-500 using CMC and ROC curves. We chose $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ from the $\mathrm{GEFE}_{\mathrm{ML}}$ that used a maximum of 1000 FE evaluations because it had the best average performance on FRGC-100 with respect to the $\mathrm{GEFE}_{\mathrm{ML}}$ instances.

Figure 7a shows the CMC curves of the baseline method, $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ (which appears as 'FEts') based on their performances on the first test set, FRGC-100. One can see that at Rank 1 and Rank 2, $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ outperform the baseline method. At Rank 3, all three methods perform equally; however, the performances of $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ are computationally less expensive.

In Figure 7b, one can see that the ROC curves of the three methods are similar; however, the curve of $\mathrm{FE}^{*}$ has a slight separation from the other two methods. Of the three methods, with respect to Figure 7b, $\mathrm{FE}^{*}$ has the best performance.

Figure 8a provides the CMC curves of the performances of the three methods with respect to the second test set, MORPH-500. The baseline method outperforms $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ at each rank with a maximum accuracy of $64 \%$ at Rank 10. The Rank 10 accuracies for $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ were $58.2 \%$ and $55.8 \%$. These results are encouraging when one considers that $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ were trained on only 100 subjects from a different database. This is also the case with the ROC curves shown in Figure 8b. The performances of the three methods are somewhat similar; however, the performances of $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ come at a fraction of the cost of the baseline method.
![img-9.jpeg](img-9.jpeg)

Figure 7a. CMC curve of Baseline, $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ on FRGC-100
![img-10.jpeg](img-10.jpeg)

Figure 7b. ROC curve of Baseline, $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {ts }}$ on FRGC-100

![img-11.jpeg](img-11.jpeg)

Figure 8a. CMC curve of Baseline, $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {N }}$ on MORPH-500
![img-12.jpeg](img-12.jpeg)

Figure 8b. ROC curve of Baseline, $\mathrm{FE}^{*}$ and $\mathrm{FE}^{\text {N }}$ on MORPH-500

## VII. CONCLUSION AND FUTURE WORK

In this paper, a GEB application, $\mathrm{GEFE}_{\mathrm{ML}}$, was presented which was used to evolve FEs that were able to generalize well to unseen subjects taken from two different databases. The evolved FEs were not only comparable in terms of accuracy with the baseline LBP method but used approximately $45 \%$ less processing time (in terms of computational complexity). Our future work will include the development of training, validation, and test sets composed of images from a variety of databases.

## ACKNOWLEDGMENT

This research was funded by the Office of the Director of National Intelligence (ODNI), Center for Academic Excellence (CAE) for the multi-university Center for Advanced Studies in Identity Sciences (CASIS), NSF SSTEM, Lockheed Martin and the National Science Foundation (NSF) Science \& Technology Center: Bio/computational Evolution in Action CONsortium (BEACON). The authors would like to thank the ODNI, the NSF, and Lockheed Martin for their support of this research.
