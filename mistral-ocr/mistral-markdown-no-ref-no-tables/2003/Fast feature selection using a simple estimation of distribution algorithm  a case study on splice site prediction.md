# Fast feature selection using a simple estimation of distribution algorithm: a case study on splice site prediction 

Yvan Saeys ${ }^{1, *}$, Sven Degroeve ${ }^{1}$, Dirk Aeyels ${ }^{2}$, Yves Van de Peer ${ }^{1}$ and Pierre Rouzé ${ }^{3}$<br>${ }^{1}$ Department of Plant Systems Biology, Ghent University, Flanders Interuniversity Institute for Biotechnology (VIB), K.L. Ledeganckstraat 35, Ghent, 9000, Belgium, ${ }^{2}$ SYSTeMS Research Group, Ghent University, Technologiepark - Zwijnaarde 9, Zwijnaarde, 9052, Belgium and ${ }^{3}$ Laboratoire associé de l'INRA (France), Ghent University, K.L. Ledeganckstraat 35, Ghent, 9000, Belgium

Received on March 17, 2003; accepted on June 9, 2003


#### Abstract

Motivation: Feature subset selection is an important preprocessing step for classification. In biology, where structures or processes are described by a large number of features, the elimination of irrelevant and redundant information in a reasonable amount of time has a number of advantages. It enables the classification system to achieve good or even better solutions with a restricted subset of features, allows for a faster classification, and it helps the human expert focus on a relevant subset of features, hence providing useful biological knowledge. Results: We present a heuristic method based on Estimation of Distribution Algorithms to select relevant subsets of features for splice site prediction in Arabidopsis thaliana. We show that this method performs a fast detection of relevant feature subsets using the technique of constrained feature subsets. Compared to the traditional greedy methods the gain in speed can be up to one order of magnitude, with results being comparable or even better than the greedy methods. This makes it a very practical solution for classification tasks that can be solved using a relatively small amount of discriminative features (or feature dependencies), but where the initial set of potential discriminative features is rather large.


Keywords: Machine Learning, Feature Subset Selection, Estimation of Distribution Algorithms, Splice Site Prediction.
Contact: yvsae@gengenp.rug.ac.be

## INTRODUCTION

For many biological processes, it is still not clear which elements contribute to the observed behaviour. One example is the occurrence of splice sites in gene se-

[^0]quences, an important characteristic for gene finding in genome sequencing projects. The DNA sequences of most genes are coding for messenger RNA (mRNA) themselves encoding proteins. While in lower organisms (prokaryotes) the mRNA is a mere copy of a fragment of the DNA, in higher organisms (eukaryotes) the DNA contains non-coding segments in genes (introns) which should be precisely spliced out to produce the mRNA. The splice sites we refer to here are the border sides of such introns. The splice site in the upstream part of the intron is called the donor site, the other site is termed the acceptor site. Due to the completion of sequencing the genome from several eukaryotes, much data became available, allowing the use of supervised learning methods to automate the process of splice site prediction. Here we used sequence data from the model plant Arabidopsis thaliana, for which more than 12000 full length cDNAs are now available, providing a large dataset of genes with documented exon/intron structure. To complete this task these learning methods need information sources to enable them to distinguish between true and false sites. These information sources are termed features in machine learning. As it is not clear which features are relevant for an accurate splice site prediction these learning methods are usually provided with many features, assuming that this will increase the probability of including relevant information.

Since not all features are relevant to the classification task and others might be correlated, there is a need to search for a 'minimal' set of features with 'best' classification performance. Traditional Feature Subset Selection (FSS) methods are sequential and are based on a greedy heuristic (Kohavi and John, 1997). Sequential Forward Selection (SFS) starts with the empty feature set and iteratively adds features, while Sequential Backward


[^0]:    *To whom correspondence should be addressed.

Elimination (SBE) starts with the full feature set and iteratively discards features. More advanced methods use heuristics to search the space of feature subsets, like e.g. genetic algorithms (Kudo and Sklansky, 2000; Siedelecky and Sklansky, 1988; Vafaie and De Jong, 1993). Recently, Estimation of Distribution Algorithms (EDAs) emerged as a more general framework of genetic algorithms (Mühlenbein and Paass, 1996). Instead of using the traditional crossover and mutation operators to create the new population, a more statistical approach is used to estimate the distribution of the parameters from a selected group of individuals. Creation of the new population is then performed by sampling individuals from the estimated distribution. EDAs have proven to outperform the standard genetic algorithms in many problems where multiple dependencies among parameters exist, and they usually need fewer fitness evaluations to obtain good solutions. In this paper we present an approach for feature subset selection for splice site prediction, using a simple EDA as a wrapper for feature subset selection. We will demonstrate the usefulness of EDAs when the number of features in the subset is constrained, resulting in a very practical algorithm being considerably faster than the sequential methods. The results of our experiments show that this approach is able to select feature subsets with equal or higher relevance than the traditional sequential methods, resulting in a better classification of the splice sites.

## METHODS

## Splice site data sets

The A.thaliana dataset was generated by aligning cognate mRNAs obtained from the public EMBL database with the BAC-sequences that were used for the Arabidopsis chromosome assembly. Redundant genes were excluded resulting in a dataset containing 1495 genes. From each gene only those introns confirming the GT-AG consensus were used to construct the set of positive instances. All GT dinucleotides at the upstream border of these introns are positive donor instances and all AG dinucleotides at the downstream border of these introns are positive acceptor instances. The negative donor instances are defined as, for all genes, all GT dinucleotides that are located between 300 nucleotide positions upstream of the first donor and 300 nucleotide positions downstream of the last acceptor in that gene and that are not donor sites. The negative acceptor instances are defined as all AG dinucleotides within the same range and that are not acceptor sites. Additional negative instances were extracted in the same range from the complementary DNA strand. These datasets and the way they were created (Degroeve et al., 2002) can be found on http://www.psb. rug.ac.be/gps\#eccb03.

Splice site prediction can be divided into two subtasks :

Table 1. Class distribution of the unbalanced datasets

prediction of donor sites and prediction of acceptor sites. Each of these subtasks can be formally stated as a twoclass classification task : \{donor site, non-donor site\} and \{acceptor site, non-acceptor site\}. The features describing the positive and negative instances were extracted from a local context around the splice site. In our experiments we used a fixed window of $p$ nucleotide positions to the left (upstream the splice site) and $q$ positions to the right (downstream the splice site) where $p=q=50$. This results in 100 position-dependent features, which were converted into binary format using sparse vector encoding yielding 400 binary features. Training sets with balanced class distribution were compiled by random selection of 1000 positive instances and 1000 negative instances (400AG.train. 2000 and 400GT.train.2000). For the test sets we extracted all candidate splice sites within the interval as defined above from 50 independant genes (400AG.test. 50 and 400GT.test.50). For feature subset selection, an independent dataset termed the holdout set is used to evaluate the subsets (see further). Two kinds of holdout sets for feature subset selection were created : balanced sets containing 1000 positive and 1000 negative instances not occurring in the training set (400AG.holdout. 2000 and 400GT.holdout.2000), and unbalanced sets containing instances from another 50 independant genes (400AG.holdout. 50 and 400GT.holdout.50). Table 1 summarizes the number of positive and negative instances in the unbalanced datasets.

## Estimation of Distribution Algorithms

During the last years, Estimation of Distribution Algorithms (EDAs) emerged as a more general framework for genetic algorithms. The main critics for standard genetic algorithms include the large number of parameters that have to be tuned, the difficult prediction of the movements of the populations in the search space and the fact that there is no mechanism for capturing the relations among the variables of the problem. EDAs try to overcome these difficulties by providing a more statistical analysis of the selected individuals, thereby explicitly modelling the relationships among the variables.

Figure 1 illustrates the main scheme of the EDA approach. After the generation of the initial population an iterative procedure is carried out until the termination

![img-0.jpeg](img-0.jpeg)

Fig. 1. Schematic overview of the EDA algorithm.
criteria are met (e.g. a fixed number of iterations). In each step of the iteration a number of individuals is selected from the population (e.g. the better half) and from these a probability distribution of the encoded variables is estimated.

The actual estimation of the underlying probability distribution represents the core of the EDA paradigm, and can be considered an optimization problem on its own. Depending on the domain (discrete or continuous), different estimation algorithms with varying complexity (modelling univariate, bivariate or multivariate dependencies) were designed. For an overview see Larrañaga and Lozano (2001). In the most complex case of multivariate dependencies, Bayesian Networks are frequently used. A greedy search algorithm is then used to find a suitable (and often constrained) network that is likely to generate the selected individuals.

In the following step, the estimated probability distribution is used to generate the next population. This is done by sampling the probability distribution, i.e. generating individuals according to this distribution. A simple estimation algorithm is the Univariate Marginal Distribution Algorithm (UMDA, Mühlenbein, 1998). The UMDA simplifies the estimation by assuming all variables are independent. For each iteration $l$ the probability model $p_{l}(x)$ is estimated as

$$
p_{l}(x)=\prod_{i=1}^{n} p_{l}\left(x_{i}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid D_{l-1}^{\mathrm{Se}}\right)
$$

where each $p_{l}\left(x_{i}\right)$ (the relative frequency) is estimated from the selected set of individuals of the previous generation $D_{l-1}^{\mathrm{Se}}$. Generation of a new individual is then achieved by sampling a value from the distribution $p_{l}\left(x_{i}\right)$ for each variable $x_{i}$.

## Classification models

As described above, our datasets contain positive and negative instances that are described by $q$ nucleotide positions downstream and $p$ nucleotide positions upstream the consensus. Formally, a data set $T$ contains $l$ instances $\mathbf{x}_{\mathbf{i}}$ $(i=1, \ldots, l)$ with each $\mathbf{x}_{\mathbf{i}}$ labelled as $y^{+}$or $y^{-}$(known as classes), indicating a positive or negative instance, respectively. Each index $x_{i j}(j=1, \ldots, n)$ in vector $\mathbf{x}_{\mathbf{i}}$ is a feature $F_{j}$.
Two methods for discriminating between positive and negative instances are described below : the Naive Bayes Method (NBM) and the Support Vector Machine (SVM). These are supervised classification methods that induce a decision function from the instances in $T$ which can then be used to classify a new instance $\mathbf{z}$ not seen in $T$.

Support Vector Machines The Support Vector Machine (Boser et al., 1992; Vapnik, 1995) is a data-driven method for solving two-class classification tasks. The Linear SVM (LSVM) separates the two classes in $T$ with a hyperplane in the feature space such that:
(a) the 'largest' possible fraction of instances of the same class is on the same side of the hyperplane, and
(b) the distance of either class from the hyperplane is maximal.

The prediction of a LSVM for an unseen instance $\mathbf{z}$ is 1 (classified as a positive instance) or -1 (classified as a negative instance), given by the decision function

$$
\operatorname{pred}(\mathbf{z})=\operatorname{sgn}(\mathbf{w} * \mathbf{z}+b)
$$

The hyperplane is computed by maximizing a vector of Lagrange multipliers $\alpha$ in

$$
\begin{aligned}
& W(\alpha)=\sum_{i=1}^{l} \alpha_{i}-\frac{1}{2} \sum_{i, j=1}^{l} \alpha_{i} \alpha_{j} y_{i} y_{j} K\left(\mathbf{x}_{\mathbf{i}}, \mathbf{x}_{\mathbf{j}}\right) \\
& \text { constrained to: } 0 \leq \alpha_{i} \leq C \text { and } \sum_{i=1}^{l} \alpha_{i} y_{i}=0
\end{aligned}
$$

where $C$ is a parameter set by the user to regulate the effect of outliers and noise, i.e. it defines the meaning of the word 'largest' in (a).
Function $K$ is a kernel function and maps the features in $T$, called the input space, into a feature space defined by $K$ in which then a linear class separation is performed. For the LSVM this mapping is a linear mapping:

$$
K\left(\mathbf{x}_{\mathbf{i}}, \mathbf{x}_{\mathbf{j}}\right)=\mathbf{x}_{\mathbf{i}} * \mathbf{x}_{\mathbf{j}}
$$

The non-linear mapping used in this paper is the Polynomial-SVM (PSVM):

$$
K\left(\mathbf{x}_{\mathbf{i}}, \mathbf{x}_{\mathbf{j}}\right)=\left(s \mathbf{x}_{\mathbf{i}} * \mathbf{x}_{\mathbf{j}}+r\right)^{d}
$$

The degree $d$ in the polynomial kernel describes the maximum order of feature interactions/dependencies. In the case of splice site prediction e.g. a kernel of degree 3 is able to model dependencies between up to 3 nucleotide positions (codon information). Similarly a kernel of degree 6 is able to extract dicodon (hexamer) information and a kernel of degree 9 can model tricodon (nonamer) information. Remark that these dependencies need not necessarily be between adjacent positions.

After calculating the $\alpha_{i}$ 's in (2), the decision function (1) becomes:

$$
\operatorname{pred}(\mathbf{z})=\operatorname{sgn}\left(\sum_{i=1}^{l} \alpha_{i} y_{i} K\left(\mathbf{x}_{\mathbf{i}}, \mathbf{z}\right)+b\right)
$$

For the LSVM this function reduces to (1) with

$$
\mathbf{w}=\sum_{i=1}^{l} \alpha_{i} \mathbf{x}_{\mathbf{i}} y_{i}
$$

In (5) each $\alpha_{i}$ is associated with $\mathbf{x}_{\mathbf{i}}$. After optimizing (2) many $\alpha_{i}$ 's will become zero and the corresponding $\mathbf{x}_{\mathbf{i}}$ will not be used in the decision function (5). All $\mathbf{x}_{\mathbf{i}}$ for which the $\alpha_{i}$ is not zero are called the support vectors. Typically the size of the set of support vectors is much smaller than $l$. The run-time complexity for training a Support Vector Machine is low order polynomial, usually approximately quadratic in the number of training samples (Hush and Scovel, 2000; Joachims, 1998).

Naive Bayes Method The Naive Bayes Method (Duda and Hart, 1973) follows the Bayes optimal decision rule, that tells us to assign a class $y^{c}$ (c in $\left[+,_{-}\right]$) to an unseen instance $\mathbf{z}$ with features $\left(F_{1}^{c}, F_{2}^{c}, \ldots, F_{n}^{c}\right)$ that maximizes $P\left(y^{c} \mid F_{1}^{c}, \ldots, F_{n}^{c}\right)$, or the probability of the class $y^{c}$ given the features $\left(F_{1}^{c}, F_{2}^{c}, \ldots, F_{n}^{c}\right)$. By using Bayes' rule we can write $\operatorname{pred}(\mathbf{z})=y^{c}$ as:

$$
y^{c}=\operatorname{argmax}_{c} \frac{P\left(F_{1}^{c}, \ldots, F_{n}^{c} \mid y^{c}\right) \times P\left(y^{c}\right)}{P\left(F_{1}^{c}, \ldots, F_{n}^{c}\right)}
$$

The NBM then simplifies the problem of estimating $P\left(F_{1}^{c} \ldots F_{n}^{c} \mid y^{c}\right)$ by making the arguable naive independence assumption that the probability of the features given the class is the product of the probabilities of the individual features given the class:

$$
P\left(F_{1}^{c}, \ldots, F_{n}^{c} \mid y^{c}\right)=\prod_{1 \leq j \leq n} P\left(F_{j}^{c} \mid y^{c}\right)
$$

The time complexity of the NBM is essentially linear in the number of training samples (McCallum et al., 1998).

It is known that the NBM can achieve considerably better results when feature subset selection is applied, yet also the SVM can benefit from feature selection, although it already performs an implicit feature weighting (Guyon et al., 2000).

## Feature subset selection methods

To select an optimal subset of features from $\left\{F_{1}, \ldots, F_{n}\right\}$, given the instances in $T$, one needs to define what is meant by 'optimal subset of features' (referred to as the selection criterion), and define a search algorithm to search for this optimal subset of features in the space of feature subset candidates. As this is an optimization problem on its own, the evaluation of some subset needs to be calculated on a dataset. This dataset should be independent of both the training and test set and is termed the holdout set. As mentioned before we created two versions of the holdout set : balanced and unbalanced. The feature subset selection procedure then uses the training set to create a model, based on a particular subset of features. During the whole search process, only the holdout set is used for evaluation, and when the search has finished, a final evaluation on the test set is performed. We used a wrapper approach (Kohavi and John, 1997) for feature selection, embedding the classification methods within a greedy or heuristic framework.

Selection criterion The selection criterion used in most classification tasks is the accuracy ratio, defined as

$$
\mathrm{ac}=\frac{\mathrm{TP}+\mathrm{TN}}{\mathrm{TP}+\mathrm{TN}+\mathrm{FP}+\mathrm{FN}}
$$

where TP and TN denote the number of true positives/negatives, and FP and FN denote the number of false positives/negatives. However, the unbalanced class distribution of splice sites (the number of pseudo sites in a sequence is a number of magnitudes higher than the number of actual sites) makes things more complicated. Let $Z$ be a set of instances where $98 \%$ of the instances are labelled as pseudo site. Then a simple classifier that always outputs the class 'pseudo' would have an accuracy ratio of 0.98 . This would be hard to beat by a classifier that tries to capture the actual dependencies between features. Although current evaluation criteria such as sensitivity and specificity introduced by Snyder and Stormo (1995), or the correlation coefficient do not seem to suffer so drastically from this problem, they are still correlated to the class distribution of $Z$. A recent proposal, the $q 9$ statistic (Zhang and Zhang, 2002), incorporates content-balancing, which means the measure is independent of the class distribution in $Z$.

$$
q 9=\left\{\begin{array}{l}
\frac{\mathrm{TN}-\mathrm{FP}}{\mathrm{TN}+\mathrm{FP}} \text { if } \mathrm{TP}+\mathrm{FN}=0 \\
\frac{\mathrm{TP}-\mathrm{FN}}{\mathrm{TP}+\mathrm{FN}} \text { if } \mathrm{TN}+\mathrm{FP}=0 \\
1-\sqrt{2}\left(\left(\frac{\mathrm{FN}}{\mathrm{TP}+\mathrm{FN}}\right)^{2}+\left(\frac{\mathrm{FP}}{\mathrm{TN}+\mathrm{FP}}\right)^{2}\right. \\
\text { if } \mathrm{TP}+\mathrm{FN} \neq 0 \text { and } \mathrm{TN}+\mathrm{FP} \neq 0
\end{array}\right.
$$

This yields a number between -1 and +1 , which can then be rescaled to a number between 0 and 1 by applying $q 9=\frac{1+q 9}{2}$. As the class distribution between our test set and holdout sets differs considerably, we adopted the $q 9$ statistic as the selection criterion to guide the search for good feature subsets.

Search algorithms A review of different search algorithms can be found in Kohavi and John (1997) and Boz (2002), and techniques to combine feature subset selection and naive Bayes have been discussed in the literature (Hall, 1999; Langley et al., 1994). As the number of feature subsets increases exponentially with increasing $n$ (number of features) and $n$ is relatively large, two techniques are justified : greedy search and heuristics. In this paper we will compare greedy search and heuristic search with the EDA-approach. Both techniques were combined with the Support Vector Machine and the Naive Bayes Method.

SVM and NBM are known to perform well in highdimensional input spaces because they implicitly avoid overfitting. This allows us to start the greedy search algorithm with the full feature set. The candidate space is explored with just one operator which eliminates a feature from the current subset. This bottom-up search procedure is called a sequential backward elimination (SBE) procedure. Another possibility would be to start with an empty feature set and iteratively add features. Such a method is termed a sequential forward selection (SFS) procedure. The strength of using backward feature elimination in comparison to forward selection is that correlated features are better discovered using SBE than with SFS.

We tested the SBE procedure both in combination with the SVM and the NBM. This was done as follows : at iteration $l$ the feature set consists of $n_{l}$ features and $n_{l}$ models have to be trained, leaving out each feature once in each model. At iteration $l+1$ the feature set for the model with the best predictive performance (i.e. the best $q 9$ statistic on the holdout set) is then chosen as the new feature subset.

For the heuristic approach we combined Estimation of Distribution Algorithms both with the Support Vector Machine and the Naive Bayes Method. The individuals in the population are represented as binary feature vectors, a 0 indicating an irrelevant/redundant feature, a 1 indicating a relevant feature. The goal of the EDA is then to look for the best subset with respect to some optimization criterion. As the number of features for splice site prediction is quite large, we need to use rather large populations (up to 500 individuals) to allow a good estimation. Furthermore, a considerable amount of time is spent in analysing the fitness of each individual. For each individual a new model has to be trained, and this model
has to be evaluated on the holdout set. Therefore, a fast classification algorithm and a fast estimation algorithm is preferred. In our experiments we used the NBM and SVM as the classification system, and the Univariate Marginal Distribution Algorithm (UMDA; Mühlenbein (1998)) as the estimation algorithm. It has to be noted that NBM and linear SVM are fast algorithms, the higher order polynomial SVMs are rather slow. Although using the naive assumption that parameters are independent both NBM and UMDA have shown to perform well in several fields such as text and image classification. As an adaptation to the standard UMDA we slightly modified the algorithm by replacing zero/one probabilities by very small/large probabilities.

Constraining feature subsets An important characteristic of using a string representation like in EDAs is the fact that we can easily constrain the size $S$ of the feature subset (i.e. the number of features in the subset, so the number of 1's in the string) by adding or removing features. This can be used to explicitly search for the best feature subset given a number of features. To achieve a subset of the same size $S$ using SBE, the algorithm starts with the full feature set, and iteratively discards features until $S$ features are retained. If we denote the total number of features by $N$, then the SBE procedure needs

$$
\text { Numeval }_{\mathrm{SBE}}=\frac{N *(N+1)-S *(S+1)}{2}
$$

model evaluations to complete this task. Each model evaluation involves the training of the model on the training set, and an evaluation on the holdout set. The average number of features over all model evaluations can then be calculated as

$$
\frac{\sum_{i=S+1}^{N} i^{2}}{\text { Numeval }_{\mathrm{SBE}}}
$$

For an EDA with a population size of $P$, running for $I$ iterations and using an elitist approach of $E$ elitists (the best $E$ individuals survive) the number of model evaluations can be calculated as

$$
\text { Numeval }_{\mathrm{EDA}}=P+(I-1) *(P-E)
$$

Whereas the number of evaluations needed for SBE only depends on the total number of features and the size $S$ of the subset, the number of evaluations for the EDA depends on $P, I$ and $E$, but not directly on $N$ and $S$. The average number of features over all model evaluations using the EDA-approach is fixed $(S)$.

## Implementation

The wrapper methods for feature selection were all implemented in C++, making use of the $\mathrm{SVM}^{\text {light }}$ implementation for Support Vector Machines (Joachims, 1998). Both

![img-2.jpeg](img-2.jpeg)

Fig. 2. Acceptor prediction : FSS on a balanced holdout set (400AG.holdout.2000).

SBE and EDA are suitable candidates for parallellizing, providing a linear speedup of the selection process. This was done making use of the MPI libraries, available at http://www-unix.mcs.anl.gov/mpi/mpich. All experiments were run on a cluster of 5 dual-processor (1.2 Ghz) Linux machines running RedHat Linux 7.2.

## RESULTS

All methods (NBM, LSVM and PSVM) were trained on a balanced dataset (400AG.train. 2000 and 400GT.train.2000) and evaluated on an unbalanced test set (400AG.test. 50 and 400GT.test.50). The experiments for feature subset selection were run on two holdout sets : a balanced data set (400AG.holdout. 2000 and 400GT.holdout.50) and an unbalanced data set (400AG.holdout. 50 and 400GT.holdout.50). For the polynomial SVM we used a ninth degree polynomial kernel function ( $\mathrm{d}=9$ in (4)), a linear coefficient of $0.01(\mathrm{~s}=0.01)$ and a constant of 1 $(\mathrm{r}=1)$. For both the LSVM and PSVM we used a value of 0.05 for the c-parameter. These parameter values were determined experimentally using a cross-validation procedure.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Acceptor prediction : FSS on an unbalanced holdout set (400AG.holdout.50).

## Feature subset selection

To compare greedy and heuristic feature selection for splice site prediction we evaluated both techniques with NBM, LSVM and PSVM. The greedy algorithm starts with the full feature set and iteratively removes features, the heuristic algorithm finds an optimal subset of features with regard to the $q 9$ ratio on the holdout set. Afterwards a greedy algorithm is applied to the solution found by the EDA, iteratively discarding features. For NBM and LSVM the population size $P$ was set to 500 , the number of elitists $E$ to 50 and the number of iterations $I$ to 150 . As a standard practice we used the best half of the population to estimate the underlying probability distribution. For the PSVM the procedures for EDA-based and greedy FSS had to be adapted, as otherwise computations would take too long. Whereas in the greedy versions of NBM and LSVM only one feature was eliminated during each iteration, we eliminated five features at the time for each iteration in the case of PSVM. For the EDA approach $P$ was changed to 100 and $E$ to 10 . Figure 2 compares the $q 9$ ratios for NBM, LSVM and PSVM with a SBE and EDA method

Table 2. Acceptor prediction : evaluation of FSS on a balanced holdout set (400AG.holdout.2000)

in the case of acceptor prediction and FSS on a balanced holdout set. On the x -axis the number of features that is eliminated so far is shown, starting at the origin with the full feature set. Figure 3 shows the $q 9$ ratios in the case of acceptor prediction and FSS on an unbalanced holdout set. It is clearly observed that for each of the three classification methods, the EDA approach outperforms the SBE, being able to select more relevant features, yielding a better classification. Both greedy and heuristic feature selection achieve better results on the unbalanced holdout set. Similar trends were seen for donor prediction. The results and analysis for these sites are available online at http://www.psb.rug.ac.be/gps\#eccb03.

## Constraining the number of features

As already mentioned before, using the EDA-approach, the size $S$ of the feature subset can be constrained by adapting the binary feature vectors. We compared the greedy and heuristic approach for three fixed values of $S: 150,80$ and 40 features. The parameters we used were the same as described in the previous experiment,

Table 3. Acceptor prediction : evaluation of FSS on an unbalanced holdout set (400AG.holdout.50)

again adapting the parameters in the case of PSVM to enable computational feasibility. Table 2 summarizes the results for acceptor prediction with FSS on a balanced holdout set. The first column in the table describes the combination of the classification algorithm and the feature selection algorithm. In the second column the number of features that was used is displayed. It contains the evaluation values for fixed subsets of 150,80 and 40 features. An additional value Max was added for SBE; this value indicates the best $q 9$ ratio over all iterations. For the EDA the field Unconstrained indicates the value in the case the size of the feature subset is not constrained. This value is equal to the starting point of the EDA curves in Figures 2 and 3. The last two columns show the correlation coefficient $(C C)$ and the $q 9$ ratio. As the EDAapproach is a heuristic, we repeated these experiments in five independent runs. The results in the table show the mean and the standard deviation (Mean $\pm$ Stddev).

Similar results for FSS on an unbalanced holdout set are shown in Table 3. In the case where the size of the subset is constrained it is observed that the constrained EDA-

Table 4. Comparisons of the running times for constrained subsets on a Linux cluster (5 dual-processors at 1.2 Ghz)

The first two columns indicate the algorithm and the size of the constrained subset. The third column shows the number of model evaluations that is needed, calculated using formulas 10 and 12 . The average number of features that has to be evaluated is shown in the fourth column and can be calculated with formula 11. The last two columns show the running time (in hours and minutes) that is needed for a balanced holdout set (400AG.holdout.2000) and an unbalanced holdout set (400AG.holdout.50)
approach performs comparable to the greedy method. A McNnemar statistical test with $\mathrm{p}=0.05$ did not reveal any significant difference to prefer one method over the other on the basis of their q9 values. Furthermore the results of the EDA-approach can be obtained in much less time, showing the advantage of a simple EDA method like the UMDA.

To compare the running time (speed) of the greedy and heuristic algorithm, two aspects need to be considered : the number of model evaluations and the average number of features for a model evaluation. The number of model evaluations needed for both methods can be calculated using formulas 10 and 12. For the greedy algorithm the average number of features that has to be evaluated is calculated with formula 11, the heuristic algorithm with a constrained subset size has a fixed number of features. Table 4 shows the results of the time comparisons for constrained subsets. Clearly the EDA-approach needs considerably less model evaluations as the size of the feature subsets decreases, resulting in a faster feature selection algorithm. Furthermore, all models in the EDAapproach have a fixed number $S$ of features to be trained on, whereas the greedy approach starts with the full feature
set and gradually decreases the number of features until a set of $S$ features remains. For both holdout sets it is observed that the EDA-approach provides a considerable speedup. The increase in speed depends on a number of things like e.g. complexity of the algorithm, size of the constrained subset and the holdout set. Whereas the increase in speed is not so much in the case of NBM on an unbalanced holdout set and a subset of 150 features, the speedup for the PSVM on the unbalanced holdout set for a fixed number of 40 features is about a factor 10 .

These results support the view that the use of EDAs for feature selection provides a very practical approach when feature sets get larger or when very time-demanding algorithms (like e.g. PSVM) are used. In these cases the use of SBE becomes computationally infeasible and by tuning the EDA-parameters $P, E$ and $I$, a relevant subset of $S$ features can be discovered.

## RELATED WORK

Genetic Algorithms (GAs) have been frequently used for feature subset selection in small scale (less than 100 features) domains (Kudo and Sklansky, 2000; Siedelecky and Sklansky, 1988; Vafaie and De Jong, 1993). The use of

EDA's for feature subset selection was pioneered by Inza et al. (1999) and the use of EDA's for FSS in large scale domains was reported to yield good results (Larrañaga and Lozano, 2001). Cantú-Paz (2002) compared several EDA's with the simple GA for small scale domains (at most 35 features) using a Naive Bayes classifier, and concluded that the complicated dependency learning EDA's are not significantly better than the simple compact GA. It has to be pointed out that the EDA-UMDA approach is very similar to the compact GA (Harik et al., 1998) or to a GA with uniform crossover.
Recently, the technique of feature distributional clustering was combined with Support Vector Machines for text categorization (Bekkerman et al., 2001). This method performs feature selection by distributional clustering of words via the information bottleneck method (Tishby et al., 1999) and can be considered a sophisticated filter method.
An extensive overview of splice site recognition, including new methods like Support Vector Machines can be found in Sonnenburg (2002), while a more general overview and a comparison of gene and splice site prediction is discussed in Mathé et al. (2002) and Zhang (2002).

## CONCLUSIONS AND FUTURE WORK

The results displayed in this paper are showing that feature subset selection by estimation of distribution algorithms is able to select highly relevant features for splice site prediction. We presented a method that is scalable to larger feature sets and, when applied with a constraint on the size of the feature subset, provides a considerable gain in speed. This was obtained at no expense on efficiency, on the contrary. The method can be used for any optimisation problem where the feature set is sufficiently large, like e.g. gene selection in microarray datasets. Future research on splice site prediction will include position-independent information, possibly also structural information to achieve better results. Other future directions we would like to explore are the combination of EDAs with other classification systems, and the development of faster estimation algorithms for multiple dependencies.
