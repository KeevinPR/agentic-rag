# A Comparison of GEC-Based Feature Selection and Weighting for Multimodal Biometric Recognition 

Aniesha Alford, Khary Popplewell, Gerry Dozier, Kelvin Bryant, John Kelly, Josh Adams, Tamirat

Abegaz, and Joseph Shelton
Center for Advanced Studies in Identity Sciences
North Carolina A \& T State University Greensboro, NC, USA
aalford@ncat.edu, ktpopple@ncat.edu, gvdozier@ncat.edu, ksbryant@ncat.edu, jck@ncat.edu, jcadams2@ncat.edu, tamirat@programmer.net, jashelt1@ncat.edu

Karl Ricanek<br>Center for Advanced Studies in Identity Sciences<br>University of North Carolina at Wilmington<br>Wilmington, NC, USA<br>ricanekk@uncw.edu

Damon L. Woodard<br>Center for Advanced Studies in Identity Sciences<br>Clemson University<br>Clemson, SC, USA<br>woodard@clemson.edu


#### Abstract

In this paper, we compare the performance of a Steady-State Genetic Algorithm (SSGA) and an Estimation of Distribution Algorithm (EDA) for multi-biometric feature selection and weighting. Our results show that when fusing face and periocular modalities, SSGA-based feature weighting (GEFeW $\mathbf{W}_{\text {SSGA }}$ ) produces higher average recognition accuracies, while EDA-based feature selection (GEFeS $\mathbf{S}_{\text {EDA }}$ ) performs better at reducing the number of features needed for recognition.


Keywords- Eigenface, Estimation of Distribution Algorithm, Feature Selection, Feature Weighting, Local Binary Pattern, Steady-State Genetic Algorithm

## I. INTRODUCTION

A biometric system is a pattern recognition system that operates by acquiring a biometric sample from an individual, extracting a feature set from the acquired sample, and comparing this feature set against the template sets in the biometric database [10]. Although researchers have shown that biometric systems that use only one biometric modality (unimodal biometric systems) can produce highly accurate results, there are a number of factors that can affect the system's performance including noise in the sensor data, biometric spoofing, and non-universality [8]. Multimodal biometric systems which fuse the evidence obtained from multiple modalities have addressed some of these issues and achieved higher recognition rates [12].

Researchers have also shown that feature selection and weighting can improve recognition accuracy $[1,2,3,7,8]$. Feature selection reduces the dimensionality of the data, keeping more discriminative features that contribute most to the recognition accuracy [12]. Feature weighting assigns are weight to each feature based on its discriminative ability [3].

Typically more weight is assigned to the more discriminating features.

Genetic and Evolutionary Computation (GEC) has also been used by the biometrics research community to optimize the recognition accuracy of biometric systems [2, 7]. The goal of GEC is to find the optimal or near optimal solution to a given problem. Typically, a GEC randomly generates a population of candidate solutions and assigns them a fitness. Members of the population are chosen, usually based on their fitness, to reproduce. The newly formed offspring are then assigned a fitness. A new population is formed using only a certain number of individuals from the newly formed offspring and the current population. Usually those with the best fitness survive and comprise the new population. This process is continued until the population converges or other conditions are met.

Two types of GECs were used in this research: a Steady State Genetic Algorithm (SSGA) and an Estimation of Distribution Algorithm (EDA). SSGAs typically create one offspring which replaces the worst individual within the current population [13]. The offspring is created by performing crossover and mutation on the selected parents. Unlike SSGAs, Estimation of Distribution Algorithms (EDAs) do not use crossover or mutation operators. Instead, an EDA randomly generates an initial population. After evaluating the population, a percentage of the top performing candidate solutions are used to form a probability density function (PDF) using the mean and standard deviation of each individual element. A certain percentage of the best members of the population, the elites, are allowed to survive to the next generation. The remaining members of the new population are then created by sampling the PDF using a Gaussian distribution $[14,15]$.

In [17], Popplewell et al. compared the performance of Genetic and Evolutionary Feature Selection (GEFeS) and Weighting (GEFeW) techniques based on a SSGA for multibiometric recognition. The techniques were tested on a subset of 105 subjects taken from the Face Recognition Grand Challenge (FRGC) dataset. Face and periocular biometric modalities were used. The Eigenface method $[9,16]$ was used to extract features from the face and the periocular features are extracted using Local Binary Patterns (LBP) [4, 11]. Their results showed that GEFeW outperformed GEFeS in terms of accuracy, while GEFeS performed better in reducing the percentage of features needed for recognition. In this paper, we extend their research, comparing the performance of EDAbased GEFeS and GEFeW.

The goal of our research is to develop short length biometric templates that are able to achieve higher recognition accuracies and is inspired in part by the hierarchical two-stage system proposed by Gentile et al. for iris recognition [19]. Their system used short-length iris codes (SLICs) to reduce the number of feature checks required for an iris-based biometric recognition system. As explained by Alford et al. [20], for a conventional biometric recognition system, a probe, $p_{c}$ is compared to every template within the gallery. Therefore, the number of feature checks performed by a conventional biometric system, $f_{c}$, is:

$$
f_{c}=n m
$$

where $n$ is the number of individuals in the database and $m$ is the number of features extracted to represent those individuals. The hierarchical two-stage system reduces the number of feature checks performed. In the first stage, the reduced length biometric template consisting of $k$ features is used to create a shortlist of the $r$ closest matches to the probe $p$. The second stage compares the shortlist to the probe $p$ using all $m$ originally extracted features. The number of feature checks performed by the hierarchical system, $f_{h}$, is:

$$
f_{h}=n k+r m
$$

The savings gained by using the hierarchical biometric system, $f_{s}$, instead of the conventional biometric system is:

$$
f_{k}=\frac{f_{N}}{f_{K}}=\frac{n k+r m}{n m}=\frac{k}{m}+\frac{r}{n}
$$

The remainder of this paper is as follows. The next section provides an overview of the feature extractors used for our experiments. Section III describes how the GECs are used for feature selection and weighting. Section IV presents our experiments, and Section V presents the results. Finally, the conclusion and future work are presented in Section VI.

## II. Feature Extraction

In this paper we use face and periocular biometric modalities. The features used for the face are extracted using the Eigenface method $[9,16]$, while the periocular features are extracted using Local Binary Patterns (LBP) $[4,11]$.

Eigenface is a dimensionality reduction technique that uses the concept of Principal Component Analysis (PCA) for face recognition, reducing the image space into face space. The method captures the variation in the face images and uses this information to encode and compare images of individual faces $[16]$.

LBP is a mechanism for texture and pattern recognition and has been proven successful for the extraction of periocular features [11]. For our research, the image of an individual periocular region is segmented into a grid of 24 evenly sized patches. LBP is then used to measure the intensity change of $P$ pixels around a center pixel with a radius, $r$, within each patch, where $P$ is the neighborhood size. A neighborhood size, $P$, of 8 and a radius of 1 were used for our experiments, so that all interior pixels within a patch were used as center pixels. The concatenation of the sign of the result of subtracting the intensity value of the center pixel from each of the $P$ neighboring pixels represents the texture. If the resulting value is greater than or equal to 0 , it is represented by a 1 , otherwise a 0 . The texture is then used to update a histogram for the image, where each bin within the histogram represents the number of times a particular texture appears in a patch. Only uniform patterns (patterns with 2 or fewer bit changes when traversed circularly) are considered for efficiency reasons. Each of the possible uniform patterns is represented by a bin within the histogram. An additional bin is added for the non-uniform patterns. Thus, using a neighborhood size of 8 , our histograms contained 59 bins. The concatenation of the histogram for each patch is then used as the image's feature template.

## III. GEFeS AND GEFeW

Genetic and evolutionary feature selection (GEFeS) and weighting (GEFeW) are based on the eXploratory Toolset for the Optimization of Launch and Space Systems (X-TOOLSS) [5]. X-TOOLSS is an optimization software consisting of a suite of twelve GECs which interface with evaluation functions expressed as executables. The GECs used to generate the results presented in this paper are an instance of X-TOOLSS SSGA and EDA. Feature selection will be referred to as $\mathrm{GEFeS}_{\text {SSGA }}$ and $\mathrm{GEFeS}_{\text {EDA }}$, for SSGA and EDA respectively. Feature weighting will be referred to as $\mathrm{GEFeW}_{\text {SSGA }}$ and $\mathrm{GEFeW}_{\text {EDA }}$, for SSGA and EDA respectively.

As described in [17], GEFeS and GEFeW use a GEC to evolve a population of real-coded feature masks composed of values from 0.0 to 1.0 . The number of features within each candidate feature mask is equal to the number of features used to represent the individuals in the gallery.

For GEFeS, a masking threshold of 0.5 is used to form a binary-coded feature mask. Features within the evolved realcoded feature masks that are less than the masking threshold, are set equal to 0 . Otherwise, the feature is set equal to 1 . The resulting binary-coded feature masks are then used to mask out features within the biometric templates during comparisons.

For GEFeW the evolved real-coded feature masks are used to weight the features within the biometric templates. Each

feature within the biometric template is multiplied by its corresponding feature mask value.

Associated with each candidate feature mask, $i$, there were two weights, $w_{i f}$ and $w_{i p}$, which are weights for the face and periocular features to allow for score-based fusion [18]. The weights ranged from 0.0 to 1.0 and were co-evolved with the before-mentioned feature masks.

Recognition was performed by computing the Manhattan distance between the probe template and the templates in the gallery set after applying the evolved feature masks. The subject of the template within the gallery set with the smallest Manhattan distance was considered a match.

The following function was used to evaluate each of the evolved candidate feature masks:

$$
f i t=10 \varepsilon+\frac{k}{m}
$$

where $\varepsilon$ is the number of errors generated when the candidate feature mask is applied, $k$ is the number of features used by the feature masks, and $m$ is the number of originally extracted features.

## IV. EXPERIMENT

Our experiments were performed using a subset of the Face Recognition Grand Challenge (FRGC) dataset [21]. This subset consisted of three images of the first 105 subjects. The images used were unoccluded frontal views of the subjects with neutral facial expressions. One image of each subject was used to form the probe set, and the other two images were used to form the gallery set.

For each of the images used to form the probe and gallery set, the Eigenface method was used to extract 210 face features, and 2832 ( 2 periocular regions $\times 24$ patches $\times 59$ bins) periocular features were extracted using the LBP method.

The tested biometric modalities for the comparisons were face, periocular, and face plus periocular. For each of the three biometric modalities, SSGA and EDA based feature selection
(GEFeS) and feature weighting (GEFeW) were used. The biometric modalities were also tested using all of the originally extracted features without the use of GECs. This served as a control/baseline for our experiments. When the face and periocular modalities were fused, they were weighted evenly.

## V. RESULTS

For our experiments, the SSGA instances had a population size of 20, a crossover and mutation rate of 1.0 , and a Gaussian mutation range of 0.2 . The EDA instances had a population size of 20 and 5 elites ( $25 \%$ of the population). Each instance was run 30 times, performing a maximum of 1000 function evaluations each run.

In Table I, the average performance of the three experiments is shown. The first column represents the modalities tested. The second column represents the type of algorithm used. The third column represents the average number of features used and the final column represents the average accuracy of the 30 runs.

For the Face-Only experiment, in terms of accuracy, the GEFeW instances performed the best. These results were confirmed using ANOVA and t-tests. The GEFeS instances were in the second equivalence class. In terms of the percentage of features used, $\mathrm{GEFeS}_{\text {EDA }}$ had the best performance using only $42.86 \%$ of the features. $\mathrm{GEFeS}_{\text {SSGA }}$, $\mathrm{GEFeW}_{\text {SSGA }}$, and $\mathrm{GEFeW}_{\text {EDA }}$ were in the second, third, and fourth equivalence classes respectively.

For the Periocular-Only experiment, $\mathrm{GEFeS}_{\text {EDA }}$ performed the best in terms of accuracy and in reducing the percentage of features used. These results were also confirmed using ANOVA and t-tests. There was no statistical significance between the performances of the SSGA based algorithms in terms of accuracy. In terms of the percentage of features used, there was a statistically significant difference between the performances of all of the algorithms. $\mathrm{GEFeS}_{\text {SSGA }}$, $\mathrm{GEFeW}_{\text {SSGA }}$ and $\mathrm{GEFeW}_{\text {EDA }}$ were in the second, third, and fourth equivalence classes respectively.

TABLE I
COMPARISING BETWEEN SSGA AND EDA BASED GEFeS AND GEFeW FOR UNE-MERAL AND MULTIMENAL BENEFINE SYSTEMS

| Modality | Algorithm | Average \% of Features Used | Average Accuracy |
| :--: | :--: | :--: | :--: |
| Face Only | Eigenface | $100.00 \%$ | $64.76 \%$ |
|  | $\mathrm{GEFeS}_{\text {SSGA }}+$ Eigenface | $50.30 \%$ | $86.13 \%$ |
|  | $\mathrm{GEFeS}_{\text {EDA }}+$ Eigenface | $42.86 \%$ | $85.59 \%$ |
|  | $\mathrm{GEFeW}_{\text {SSGA }}+$ Eigenface | $87.16 \%$ | $87.56 \%$ |
|  | $\mathrm{GEFeW}_{\text {EDA }}+$ Eigenface | $96.54 \%$ | $87.81 \%$ |
| Periocular Only | LBP | $100.00 \%$ | $94.29 \%$ |
|  | $\mathrm{GEFeS}_{\text {SSGA }}+$ LBP | $48.03 \%$ | $95.14 \%$ |
|  | $\mathrm{GEFeS}_{\text {EDA }}+$ LBP | $41.03 \%$ | $95.87 \%$ |
|  | $\mathrm{GEFeW}_{\text {SSGA }}+$ LBP | $86.22 \%$ | $95.46 \%$ |
|  | $\mathrm{GEFeW}_{\text {EDA }}+$ LBP | $95.78 \%$ | $94.67 \%$ |
| Face + Periocular | Eigenface + LBP [evenly fused] | $100.00 \%$ | $90.77 \%$ |
|  | $\mathrm{GEFeS}_{\text {SSGA }}+$ Eigenface + LBP | $48.18 \%$ | $97.40 \%$ |
|  | $\mathrm{GEFeS}_{\text {EDA }}+$ Eigenface + LBP | $45.24 \%$ | $96.70 \%$ |
|  | $\mathrm{GEFeW}_{\text {SSGA }}+$ Eigenface + LBP | $87.59 \%$ | $98.98 \%$ |
|  | $\mathrm{GEFeW}_{\text {EDA }}+$ Eigenface + LBP | $97.40 \%$ | $96.64 \%$ |

For the multimodal experiment, Face + Periocular, $\mathrm{GEFeW}_{\text {SSGA }}$ had the highest average accuracy. According to the ANOVA and t-test, $\mathrm{GEFeS}_{\text {SSGA }}$ belonged to the second equivalence class. There was not a statistically significant difference between performances of the EDAbased algorithms. In terms of the percentage of features used, $\mathrm{GEFeS}_{\text {EDA }}$ had the best performance once again, followed by $\mathrm{GEFeS}_{\text {SSGA }}, \mathrm{GEFeW}_{\text {SSGA }}$, and $\mathrm{GEFeW}_{\text {EDA }}$.

The Face + Periocular experiment performed the best in terms of accuracy for all the algorithms used, followed by the Periocular-Only experiment, and the Face-Only experiment. The highest average accuracy, $98.98 \%$, was achieved by the Face + Periocular experiment for the $\mathrm{GEFeW}_{\text {SSGA }}$ instance.

For the percentage of features used, the $\mathrm{GEFeS}_{\text {EDA }}$ instances used the least amount of features, while the $\mathrm{GEFeW}_{\text {EDA }}$ instances used the highest percentage of features for each experiment performed.

## VI. CONCLUSION

Our results show that SSGA-based feature weighting $\left(\mathrm{GEFeW}_{\text {SSGA }}\right)$ produces the best recognition accuracy for biometric identification when both the face and periocular modalities are used. In general, the multimodal (Face + Periocular) experiment performs better in terms of accuracy when compared to the uni-modal (Face-Only and Periocular-Only) experiments. EDA-based feature selection $\left(\mathrm{GEFeS}_{\text {EDA }}\right)$ performed better at reducing the number of features necessary for recognition for all of our experiments. Our future work will include investigating the usage of different optimization techniques to further improve the performance of multi-biometric identification.

## ACKNOWLEDGMENT

This research was funded by the Office of the Director of National Intelligence (ODNI), Center for Academic Excellence (CAE) for the multi-university Center for Advanced Studies in Identity Sciences (CASIS) and by the National Science Foundation (NSF) Science \& Technology Center: Bio/computational Evolution in Action CONsortium (BEACON). The authors would like to thank the ODNI and the NSF for their support of this research.

## REFERENCES

[1] J.E. Gentile, N. Ratha, and J. Connell, "SLIC: Short-length iris codes," IEEE 3rd International Conference on Biometrics: Theory, Applications, and Systems, pp.1-5, 28-30 Sept. 2009.
[2] G. Dozier, K. Frederiksen, R. Meeks, M. Savvides, K. Bryant, D. Hopes, T. Munemoto, "Minimizing the number of hits needed for iris recognition via Bit Inconsistency and GRIT," IEEE Workshop on Computational Intelligence in Biometrics: Theory, Algorithms, and Applications, pp.30-37, March 30 2009-April 22009.
[3] R. Kohavi, P. Langley, and Y. Yun. "The utility of feature weighting in nearest-neighbor algorithms," In Proceedings of the European Conference on Machine Learning (ECML-97), 1997.
[4] Z.N. Sun, T.N. Tan, X.C. Qiu, "Graph Matching Iris Image Blocks with Local Binary Pattern," In: Zhang, D., Jain, A.K. (eds.) Advances in Biometrics. LNCS, vol. 3832, pp. 366-372. Springer, Heidelberg (2005).
[5] M. L. Tinker, G. Dozier, and A. Garrett, "The exploratory toolset for the optimization of launch and space systems (X-TOOLSS)," http://nxt.ncat.edu/, 2010.
[6] D.B. Fogel, "An introduction to simulated evolutionary optimization," IEEE Trans. Neural Networks, vol. 5, pp. 3-14, Jan. 1994.
[7] J. Adams, D. L. Woodard, G. V. Dozier, P. E. Miller, K. Bryant, and G. Glenn, "Genetic-based type II feature extraction for periocular biometric recognition: less is more," International Conference on Pattern Recognition - ICPR , pp. 205-208, 2010.
[8] A.K. Jain, K. Nandakumar, and A. Ross, "Score normalization in multimodal biometric systems," Pattern Recognition., vol. 38, no. 12, pp. 2270-2285, Dec. 2005.
[9] M. Turk and A. Pentland, "Eigenfaces for recognition," Journal of Cognitive Neuroscience, vol. 3 no. 1 pp. 76-81, Winter 1991.
[10] A. K. Jain, A. Ross, S. Prabhakear. "An introduction to biometric recognition". IEEE Transactions on Circuits and Systems for Video Technology, Vol. 14, No. 1, January 2004.
[11] P.E. Miller, A.W. Rawls, S.J. Pundlik, D.L. Woodard. "Personal identification using periocular skin texture". SAC 2010: Proceedings of the 2010 ACM symposium on Applied Computing. New York, NY, USA: ACM, 2010.
[12] A. Kumar and D.Zhang. "Biometric recognition using feature selection and combination." In Proc. AVBPA, New York, Jul. 2005, pp. 813-822.
[13] F. Vavak, T.C. Fogarty. "Comparison of steady state and generational genetic algorithm for use in nonstationary environments".
[14] J.M. Peña, V. Robles, P. Larrañaga, V. Herves, F. Rosales, and M.S. Pérez. "GA-EDA: Hybrid evolutionary algorithm using genetic and estimation of distribution algorithms". IEA/AIE 2004, LNAI 3029, pp. 361-371, 2004.
[15] P. Larrañaga and J.A. Lozano. "Estimation of distribution algorithms: A new tool for evolutionary computation". Springer, 2002.
[16] Y.V. Lata, C.K.B Tungathurthi, H.R.M. Rao, A. Govardhan, L.P. Reddy. "Facial recognition using eigenfaces by PCA". International Journal of Recent Trends in Engineering, Vol. 1, No. 1, May 2009.
[17] K. Popplewell, A. Alford, G. Dozier, K. Bryant, J. Kelly, J. Adams, T. Abegaz, K. Purrington, and J. Shelton, "A comparison of genetic feature selection and weighting techniques for multi-biometric recognition," In Proceedings of ACM Southeast Conference (ACMSE), Kennesaw, GA, USA, Mar 24-26, 2011.
[18] A. Alford C. Hansen, G. Dozier, K. Bryant, J. Kelly, T. Abegaz, K. Ricanek, and D. Woodard. "GEC-based multi-biometric fusion", IEEE Congress on Evolutionary Computation (CEC), 2011.
[19] J.E. Gentile, N. Ratha, and J. Connell, "An efficient, two-stage iris recognition system", In Proc. 3rd International Conference on Biometrics: Theory, Applications, and Systems (BTAS), 2009.
[20] A. Alford, K. Popplewell, G. Dozier, K. Bryant, J. Kelly, J. Adams, T. Abegaz, and J. Shelton. "GEFeWS: A hybrid genetic-based feature weighting and selection algorithm for multi-biometric recognition", Midwest Artificial Intelligence and Cognitive Science Conference (MAICS), 2011.
[21] P.J. Phillips, P.J. Flynn, T. Scruggs, K.W. Bowyer, J. Chang, K. Hoffman, J. Marques, J. Min, and W. Worek, "Overview of face recognition grand challenge," in Proc. IEEE Conference on Computer Vision and Pattern Recognition, 2005.