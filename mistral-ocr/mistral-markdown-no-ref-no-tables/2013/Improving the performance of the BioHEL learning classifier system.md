# Improving the performance of the BioHEL learning classifier system 

Xiao-Lei Xia ${ }^{\mathrm{a}, *}$, Huanlai Xing ${ }^{\mathrm{b}}$<br>${ }^{a}$ School of Mechanical and Electrical Engineering, Jiaxing University, Jiaxing 314001, PR China<br>${ }^{\mathrm{b}}$ School of Computer Science and IT, University of Nottingham, Nottingham NG8 1BB, UK

## A R T I C L E I N F O

Keywords:
Learning Classifier Systems
Bioinformatics-oriented Hierarchical Evolutionary Learning
Estimation of Distribution Algorithms

## A B S T R A C T

The identification of significant attributes is of major importance to the performance of a variety of Learning Classifier Systems including the newly-emerged Bioinformatics-oriented Hierarchical Evolutionary Learning (BioHEL) algorithm. However, the BioHEL fails to deliver on a set of synthetic datasets which are the checkerboard data mixed with Gaussian noises due to the fact the significant attributes were not successfully recognised. To address this issue, a univariate Estimation of Distribution Algorithm (EDA) technique is introduced to BioHEL which primarily builds a probabilistic model upon the outcome of the generalization and specialization operations. The probabilistic model which estimates the significance of each attribute provides guidance for the exploration of the problem space. Experiment evaluations showed that the proposed BioHEL systems achieved comparable performance to the conventional one on a number of real-world small-scale datasets. Research efforts were also made on finding the optimal parameter for the traditional and proposed BioHEL systems.
(c) 2013 Elsevier Ltd. All rights reserved.

## 1. Introduction

Recent decades have seen the successful application of Learning Classifier Systems (LCS) (Smith, 1980; Wilson, 1995) and GeneticBased Machine Learning to a number of real-life problems. The BioHEL (Bacardit, Burke, \& Krasnogor, 2009), an acronym for the Bioinformatics-oriented Hierarchical Evolutionary Learning, has been a very recent addition to the family of LCS algorithms. Its knowledge representation, which is preceded by an implicit feature selection procedure, is composed of only relevant attributes. It have been experimentally proven BioHEL's abilities to deliver maximally accurate, maximally general and compact rule sets for complex problems and its comparatively superior scalability to datasets of high dimensions.

In our recent studies, the BioHEL system was applied to 18 variants of checkerboard datasets in which a growing number of Gaussian noises were added. The BioHEL, with the default parameter setting had difficulties in maintaining satisfactory performance on datasets as the dimensions of noises grew to 7 and beyond. It was also discovered that multiple parameters for the knowledge representation, particularly the number of relevant attributes, have significant impact on the performance of the BioHEL.

[^0]An investigation was carried out to pinpoint the cause of the BioHEL's inability to cope with datasets contaminated by high dimensions of noises. It was observed that the significant attributes failed to prevail in terms of their occurrences in the population before the application of selection pressure. It was thus reduced the chances that the optimal attribute combination(s) and their respective optimal value range be identified.

It was conceived to introduce a mechanism to identify significant attributes for the BioHEL. Interestingly, other than the standard genetic algorithm operations which are selection, cross-over and mutation, the BioHEL also features two "special" operators: generalization and specialization. For each rule in the population, at each iteration by probability, generalization removes an attribute and specialization adds an extra attribute. These two types of operations, in fact, are explicit feature selection procedures. Nevertheless, the attribute is selected randomly, which, essentially, treats each attribute as equally significant. Consequently, this implicit feature selection procedure fails to benefit the BioHEL on the noisy variants of checkerboard datasets.

On the other hand, the fitness change resulting from the special operators is deemed informative about the significance of attributes. Intuitively, the loss of significant attributes, in general, worsens the fitness of associated rules across the population while the addition of significant attributes improves their fitness. Thus, this paper proposed to estimate the significance of attributes by constructing a probabilistic model based on the fitness change brought by the generalization or the specialization operator. A probability vector is built with each element gives the significance of each attribute. The vector is updated iteratively to reflect the


[^0]:    ${ }^{\text {a }}$ This document is a collaborative effort.

    * Corresponding author. TeL: +86 573 83647354.

    E-mail addresses: xxia01@qub.ac.uk (X.-L. Xia), pxxhs@nottingham.ac.uk (H. Xing).

![img-0.jpeg](img-0.jpeg)

Fig. 1. The checkerboard datasets.
![img-1.jpeg](img-1.jpeg)

Fig. 2. The performance of the traditional BioHEL on the original checkerboard datasets.
most recent fitness change in associated rules. Meanwhile, the probability vector also provides guidelines for the special operations at the iteration that followed. Attributes whose addition or removal contributes to the improvement of fitness are given preference to more occurrence in candidate solutions, while the attributes that causes the fitness degradation are to occur less. This strategy can be categorized into the family of univariate Estimation of Distribution Algorithms (EDA) (Larranaga \& Lozano, 2002) which estimate a model of the problem structure, assuming that attributes are independent of each other.

Experiments were performed on various datasets to evaluate the performance of the BioHEL integrated with the novel EDA technique. It was shown that with appropriate configurations of the parameters, the performance of BioHEL using the EDA algorithm remained stably satisfactory over the noisy variants of checkerboard datasets. Its performance were proven competitive on a variety of real-life problems datasets, both small and large.

Research efforts have also made on analyzing influence of multiple parameters on the generalization performance of different BioHEL systems. The optimal parameter settings were identified

Table 1
Parameter configuration of BioHEL for the 2-dimensional checkerboard dataset.

Table 2
10-fold cross validation accuracies of LIBSVM, NaiveBayes (NB) and C4.5 on the checkerboard datasets.

for the conventional and the proposed BioHEL systems in order to achieve the best performance.

The paper is organized as follow. Section 2 reviews the related work, followed by a description of the BioHEL system in Section 3. Section 4 illustrates the performance of the standard BioHEL on the 2-dimensional checkerboard benchmark and the difficulties BioHEL encounters on variants of checkerboard datasets with a large amount of noisy disturbances. An investigation was carried out to pinpoint the root of the problem. Section 5 proposed the algorithms for constructing a probabilistic model which identifies significant attributes in order to make the generalization and the specialization operations better informed. It is followed by an analysis of parameter settings for different BioHEL systems. The conventional BioHEL and the proposed ones, each with their respective optimal parameter settings, are compared in terms of

![img-2.jpeg](img-2.jpeg)

Fig. 3. The performance of BioHEL degrades to the growth in the number of noise attributes.
their generalization performances on the variants of the checkerboard. Section 6 reports the experimental results of the new BioHEL systems embedded the EDA algorithm on a number of benchmark datasets and its performance was compared to that of the conventional BioHEL. Conclusions are given in Section 7 with an outlook on future work.

## 2. Related work

In the community of evolutionary learning, research efforts has continued unabated to unveil the structural information of a problem efficiently, which has prompted the emergence of various techniques. Among these techniques are the Estimation of Distribution Algorithms (EDA) (Larranaga \& Lozano, 2002) which are a class of evolutionary algorithms, identifying interactions between attributes. EDA techniques, in general, build a probabilistic model of candidate solutions from which offspring solutions are generated. For example, probabilistic models which contain the global structural information of the problem are built, respectively in the Compact Genetic Algorithm (cGA) (Harik, Lobo, \& Goldberg, 2002), the Extended Compact Genetic Algorithm (ECGA) (Butz,
![img-3.jpeg](img-3.jpeg)

Fig. 4. The number of occurrences of attributes for datasets with respectively 3, 5, 7 and 10 attributes.

2006; Harik, Lobo, \& Sastry, 2006) and the Bayesian Optimization Algorithm (BOA) (Pelikan, 2005).

The Learning Classifier Systems (LCS) has benefited greatly from these techniques which has made exploration of the problem space well-informed. The compact classifier system (CCS) (Llorà, Sastry, \& Goldberg, 2005) is a Pittsburgh LCS incorporated with Compact Genetic Algorithm (cGA) (Harik et al., 2002) which is a typical EDA method. cGA is run repeatedly in order to produce and evolve accurate and maximally general rules. Different rules are sampled from different probability distribution vectors which are different perturbations of the initial probability vector of cGA. Probability vectors are generated and removed adaptively to ensure a compact rule set containing accurate and maximally general rules. However, the number of function evaluations required grows exponentially to the size of multiplexer problem. The poor scalability of the CCS prompted the development of $\chi$-ary extended compact classifier system ( $\chi$ eCCS) (Llorà, Sastry, Goldberg, \& de la Ossa, 2006) in which: (1) the probabilistic model is built using the aforementioned ECGA which search for least complex and most accurate model; (2) efficient rule niching is realized using restricted tournament replacement scheme which makes possible maintenance and evolution of multiple rules in a single run. Experimental evaluations showed that the $\chi$ eCCs scales quadratically to the problem size for the multiplex applications.
![img-4.jpeg](img-4.jpeg)

The eXtended classifier system (XCS) which is a well-known LCS, has also used strategy of constructing probabilistic models (Wilson, 1995). The model, in effect, presents the XCS with well-informed recombination operators without require explicit global knowledge of the specific problem at hand. As a result,, the need for the conventional crossover operation is eliminated. More lately, a novel model was proposed which contains the structural information contained in the population of XCS system (Park \& Oh, 2009). Using this model, different weights were assigned to the action that different inputs recommended for the prediction of a testing instance. The model is suggested to be capable of improving the performance of the traditional XCS by $10 \%$ for large-scale speaker identification problems.

Another important research avenue regarding the performance enhancement of LCSs is the application of Memetic Algorithms (Krasnogor \& Smith, 2005), inspired by models of adaption in natural systems which hybridizes evolutionary adaptation of a population with individual learning procedures for local refinement. Recent research efforts include the LCS proposed in Wyatt and Bull (2005) where the memetic learning techniques were introduced to LCS to address continuous-valued problems. It is demonstrated that memetic technique can make the learning of LCS more accurate and more robust. Also in this category is the XCS which was incorporated with the gradient descent methods for multi-step problems (Butz, Goldberg, \& Lanzi, 2005). Its superi-
![img-5.jpeg](img-5.jpeg)

Fig. 5. The mean accuracy for datasets with respectively 3, 5, 7 and 10 attributes.

![img-6.jpeg](img-6.jpeg)

Fig. 6. The mean coverage for datasets with respectively 3, 5, 7 and 10 attributes.
ority to the standard XCS is experimentally confirmed. Within the domain of multistep applications, the SAMUEL system (Grefenstette, 1991) is another LCS in which various learning operators, inspired by memetic learning mechanisms, are defined.

More recently, a smart crossover operator was proposed within the framework of Pittsburgh LCS (Bacardit \& Krasnogor, 2006). The operator recombines rules from multiple parents and heuristically identify rule set which is maximally accurate and compact. In the extension of this LCS (Bacardit \& Krasnogor, 2009), multiple new operators are defined to reinforce the specificity/generalization pressure for individual rules. Experiments showed that the Pittsburgh LCS reinforced a proper combination of these operators can achieve comparable performance to that XCS/BOA and $z e C C S$.

## 3. Bioinformatics-oriented Hierarchical Evolutionary Learning System

The Bioinformatics-oriented Hierarchical Evolutionary Learning System (BioHEL) is a Pittsburgh LCS which employes Iterative Rule Learning (IRL) paradigm (Venturini, 1993). The system employs genetic algorithm to evolve a population of candidate rules iteratively. At each iteration, a rule is learnt and appended to the rule set which is initially empty. Meanwhile, the instances that are covered by the rule are removed from the training set. The resultant
rule set, with the rule elements in chronological order, forms the solution to the problem.

Each rule in BioHEL takes the general form of IF < condition> THEN < class > . For continuous attributes, the rule specifies the eligible value range by specifying a lower upper and an upper bound. For discrete attributes, the rule uses binary representation where each optional value is assigned a bit. The disjunctive of the bits which is assigned a value of " 1 " is the set of all the optional values for a single attribute. Different attributes are combined by logical conjunction into the condition part. Each rule is identified by the following parameters: (1) an integer specifying the number of attributes selected into the rule; (2) a vector containing the indexes of the attributes; (3) a vector specifying the feasible value range for each attribute; (4) the class label. For large-scale datasets, only a subset of attributes are selected randomly into each rule during initialization, which is, in effect, an explicit feature selection process for each rule.

Exploration operators defined for this rule representation include the traditional crossover operator and the mutation operator. The crossover operator selects a random cut point within each parent rule and recombines into two offsprings. The mutation operator selects an attribute of a rule randomly and alters its value interval or its value options. It is worth attention that, in a single rule, the mutation operator "virtually" removes an attribute when the interval for an attribute is expanded to its feasible or all the op-

![img-7.jpeg](img-7.jpeg)

Fig. 7. The mean generality for datasets with respectively 3, 5, 7 and 10 attributes.
tional values for the attribute are allowed. Two special operators are also defined which are respectively generalization operator and specialization operator. The generalization operator removes an attribute from a rule and specialization operator adds an extra attribute to a rule. These two operators, in actual fact, perform feature selection on a rule and ensure that attribute combinations as many as possible are evaluated.

The fitness function of the BioHEL follows the principle of Minimum Description Length (MDL) (Rissanen, 1978). The MDL principle seeks the optimal trade-off between the complexity and the accuracy of a rule. BioHEL searches for the rule with the minimal fitness value. The fitness function is formulated as:

Fitness $=$ TL $\cdot \mathrm{W}+\mathrm{EL}$
where TL, the acronym for theory length, is indicative of the complexity of a rule while EL, the acronym for exception length, is indictive of the accuracy of the rule. W is the parameter which adjusts the tradeoff between the two terms.

For a rule denoted as $R$, its TL is calculated as:
$\operatorname{TL}(R)=\frac{\sum_{i=1}^{n \text { Atr }}\left(1-\operatorname{Size}\left(R_{i}\right)\right) / \operatorname{Size}\left(D_{i}\right)}{\# A t t r}$
where \#Attr is the number of the relevant attributes, Size $\left(R_{i}\right)$ is the width of the interval for ith attribute in the rule $R$ and Size $\left(D_{i}\right)$ is the width of the feasible range for ith attribute.

EL, on the other hand, is formulated as:
$\operatorname{EL}(R)=2-\operatorname{ACC}(R)-\operatorname{COV}(R)$
where $\operatorname{ACC}(R)$ represents the accuracy of the rule $R$, defined as the number of examples correctly classified among all the examples that are covered by the rule. And COV $(R)$ stands for the coverage of the rule $R$ defined as the number of examples matched by the rule divided by the current number of total training examples. The tradeoff between $\operatorname{ACC}(R)$ and $\operatorname{COV}(R)$ is controlled by a parameter called the Coverage Ratio (CR). Meanwhile, the coverage term is a function of the number of examples that are matched by the rule $R$, matched $(R)$. COV $(R)$ grows linearly to matched $(R)$ until it reaches a threshold which is parameterized by a threshold termed as the Coverage Breakpoint (CB). After reaching the CB, COV (R) grows at a slower rate.

Techniques which are introduced to improve the performance of the BioHEL system also include: (1) incremental learning with alternating strata (ILAS) windowing scheme in which a portion of, rather than all, training examples are used to evaluate the fitness of each rule. (2) ensemble learning scheme in which the BioHEL run multiple times with different random seeds. Each run cast a vote on the membership of an example which is eventually

![img-8.jpeg](img-8.jpeg)

Fig. 8. The pearson correlation coeffiecent between accuracy and coverage for each attribute of datasets with respectively 3, 5, 7 and 10 attributes.
assigned the label of the class winning the majority of votes. (3) default class policy which allows examples to be grouped into a certain class in order to make the ultimate rule set more compact.

## 4. Experiments on checkerboard datasets

### 4.1. Performance of various algorithms on the checkerboard datasets

The checkerboard dataset contains 992 data points from two classes on $X-Y$ plane, with 496 for each class, as shown by Fig. 1. Fig. 2 displays the checkerboard pattern successfully recognized by the BioHEL using the parameter setting in Table 1. The BioHEL achieved a 10 -fold cross-validation accuracy of $97.17 \%$.

In order to examine BioHEL's ability of identifying signification attributes, the checkerboard datasets were added, incrementally, 1 to 18 dimensions of Gaussian noises, resulting in 18 synthetic datasets. Each noisy attribute, as well as the original two, has roughly the same mean of 1.50 . The standard deviations of the noises are also at the same level of around 0.14 , while they are around 0.28 for the original two attributes.

Ten-fold cross validation accuracies of LIBSVM (Chang \& Lin, 2001), NaiveBayes (NB) and C4.5 on the checkerboard datasets were reported in Table 2 and depicted by Fig. 3. For LIBSVM, the following Gaussian Radial Basis Function (RBF) was used:
$K\left(\mathbf{X}_{i}, \mathbf{X}_{j}\right)=\mathrm{e}^{-c_{i}\left(\mathbf{X}_{i}-\mathbf{X}_{j}\right)^{2}}$
From Fig. 3, it can be seen that both NaiveBayes and C4.5 were unable to perform well while the performance of both the BioHEL and LIBSVM degraded as the number of noises grows.

### 4.2. Investigation into BioHEL's performance degradation

In order to investigate the cause of BioHEL's performance degradation, different variables in the system and their relations were analyzed in detail. First analyzed was the average change of different variables through the 100 iterations to generate the first rule. Figs. 4-7 depicts respectively the number of occurrences, the mean accuracy, the mean coverage and the mean generality for each attribute across rules, on datasets with 3, 5, 7 and 10 attributes. For each graph, variables depicted are, in a direction of clockwise, the number of occurrences, accuracies, generality and coverage of different attributes across the entire population. The value of these variables averaged over 25 runs on different random seeds. The blue and the green curves represented the two significant attributes while the rest in different shades of cyan are all noises.

It can be seen that the number of occurrence and the coverage of different attributes both can help distinguish the significant attributes from the noises on datasets of 3 attributes. However,

![img-9.jpeg](img-9.jpeg)

Fig. 9. The pearson correlation coeffiecent between accuracy and generality for each attribute of datasets with respectively 3, 5, 7 and 10 attributes.
![img-10.jpeg](img-10.jpeg)

Fig. 10. The pearson correlation coeffiecent between coverage and generality for each attribute of datasets with respectively 3, 5, 7 and 10 attributes.

![img-11.jpeg](img-11.jpeg)

Fig. 11. the average fitness improvement of the original BioHEL and the non-alternate system on the checkerboard datasets with respectively 3 and 9 attributes.
as the number of attributes grows, for both variables, curves of significant attributes tend to merge with those of the noise attributes, particularly on datasets of 15 and 20 attributes.

Also analyzed was the pearson correlation coefficient between each pair of different variables, as illustrated by Figs. 8-10. It is demonstrated that the expected correlation between coverage and generality can be detected for all attributes. For datasets of 3 attributes, the correlation is relatively constant while for datasets with large amounts of noises, these correlation coefficients show significant fluctuation. It is noted that, as the number of noises grow, the correlation coefficients between different variables for significant attributes become more and more indistinguishable from those for noise attributes.

## 5. BioHEL integrated with EDA techniques

The above various analysis exposed the BioHEL's inability of identifying significant attributes for noisy datasets. This fact necessitates the development of a mechanism which can help identify significant attributes. Although there have been a number of Esti-
mation of Distribution Algorithms (EDA) existing in the literature which exploits the structure of the problem space to find the useful attributes or attribute combinations, they were unable to be directly applied to the BioHEL. Nonetheless, it is observed that the fitness change brought by the special operation, which include the generalization and the specialization operators, can be informative about the relevance of the attributes. Fig. 11 (a) and (c), for the checkerboard datasets with 3 and 9 attributes respectively, plot the average fitness improvement versus the number of total occurrences for each attribute at each iteration. In the figures, the blue and the green lines indicates the original two attributes and the cyan the noise one(s). For the specialization operator, the fitness improvement refers to only the positive change in the value of a rule's fitness after the addition of a attribute. For the generalization operator, the fitness improvement refers to that the negative change in fitness upon the removal of the attribute. The fitness improvement for a specific attribute is summed and then averaged over the total occurrence of special operations, which results in the average fitness improvement for the attribute.

From Fig. 11(a) and (c), it can be observed that the average fitness improvement of both significant attributes is much higher

Table 3
Special operators incorporated with the EDA technique: non-alternate style.
(1) Initialize the probability vector for $i:=1$ to $/ d o$
$p[i]=1 / i$
(2) Initialize the sum of fitness improvement and the occurrence count of special operations for each attribute
for $i:=1$ to $/ d o$
$s[i]=0 ; c[i]=0$
(3) Apply the specialization or the generalization operator to each individual by probability.
for $i:=1$ to $n$ do
generate a random number represented by $p_{i} \in[0,1]$
if $p_{i}$ is greater than probability of specialization, then
\{
generate a random number between $[0,1]$
for $j:=1$ to $/ d o$
if $\sum_{i=1}^{n} p[i]$ is greater than the random number
then break;
add the $j$ th attribute to the $i$-th rule;
$c[j]=c[j]+1$;
if the fitness of the rule after specialization is increased by
$\Delta F>0$ then
$s[j]=s[j]+\Delta F$
\}
elseif $p_{i}$ is greater than greater than probability of generalization,
then
\{
generate a random number between $[0,1]$
for $j:=1$ to $/ d o$
if $\sum_{i=1}^{n}\left(2-p[i]\right)$ is greater than the random number
then break;
remove the $j$ th attribute from the $i$ th rule;
$c[j]=c[j]+1$;
if the fitness of the rule after generalization is reduced by
$\Delta F>0$ then
$s[j]=s[j]+\Delta F$
\}
(4) Update the probability vector
for $i:=1$ to $/ d o$
$p[i]=s[i] ; \sum_{i=1}^{n} s[i]$
(5) Go to step 2 and repeat
$i$ : the number of attributes
$n$ : the number of individuals in the population
than that of noises, which successfully separate the two types of attributes. This observation is in consistent with the intuition that, the loss of significant attributes, in general, worsens the fitness of associated rules across the population while the addition of significant attributes improves their fitness.

Fig. 11(c) shows that, for the checkerboard with 9 dimensions of noise, the average fitness improvement still manages to set the significant attributes apart from the noise attributes to a certain extent. However, by comparing Fig. 11(c) to (a), it can be inferred that as the amount of noises grows larger, the curves of average fitness improvement between significant attributes and noises one become harder to separate.

Thus, it is proposed in this paper: (1) to estimate the significance of attributes by constructing a probabilistic model based on the fitness improvement resulting from the application of special operators; (2) to use the probabilistic model, in turn, as guidance for the exploration of the search space by the special operators. Table 3 lists the pseudocode for the updated special operators at a single iteration.

It is worth attention the algorithm in Table 3 disallows the generalization and the specialization both to be performed at one iteration. Consequently, if the probability of specialization is set to be $a \in[0,1]$, the probability of generalization can not exceed $1-a$. To address this issue, a second algorithm is proposed which performs generalization and specialization alternately between

Table 4
Special operators incorporated with the EDA technique: alternate style.
(1) xmllabelp0245 Initialize the probability vector
for $i:=1$ to $/ d o$
$p[i]=1 / i$
(2) Initialize the sum of fitness improvement and the occurrence count of special operations for each attribute
for $i:=1$ to $/ d o$
$s[i]=0 ; c[i]=0$
(3) Depending on the count of iterations, apply the specialization or the generalization operator
to each individual by probability.
if the current iteration count is an odd number then
for $i:=1$ to $n$ do
generate a random number represented by $p_{i} \in[0,1]$
if $p_{i}$ is greater than probability of specialization, then
\{
generate a random number between $[0,1]$
for $j:=1$ to $/ d o$
if $\sum_{i=1}^{n} p[i]$ is greater than the random number
then break;
add the $j$ th attribute to the $i$ th rule;
$c[j]=c[j]+1$
if the fitness of the rule after specialization is increased
by $\Delta F>0$ then
$s[j]=s[j]+\Delta F$
\}
if the current iteration count is an even number then
\{
generate a random number between $[0,1]$
for $j:=1$ to $/ d o$
if $\sum_{i=1}^{n}\left(2-p[i]\right)$ is greater than the random number
then break;
remove the $j$ th attribute from the $i$ th rule;
$c[j]=c[j]+1$;
if the fitness of the rule after generalization is reduced by $\Delta F>0$
then
$s[j]=s[j]+\Delta F$
\}
(4) Update the probability vector
for $i:=1$ to $/ d o$
$p[i]=s[i] ; \sum_{i=1}^{n} s[i]$
(5) Go to step 2 and repeat
$i$ : the number of attributes
$n$ : the number of individuals in the population
iterations. Table 4 gives the pseudocode for the algorithm of alternate style. The two algorithms are referred to, respectively, as the non-alternate and the alternate algorithms in this paper.

Fig. 11(b) and (d) depict, for checkerboard with respectively 3 and 9 attributes, the fitness improvement in the non-alternate system brought by different attributes. From Fig. 11(b), it can be observed that the non-alternate systems identified the significant attributes for the dataset with 3 attributes. Also can be seen is that less overlapping were displayed in Fig. 11(d) than in Fig. 11(c), which suggests that the non-alternate system set the attributes and the noise further apart than the traditional BioHEL.

### 5.1. Parameter tuning of different BioHEL systems

The parameter setting, on the other hand, have a major impact on the performance of the BioHEL algorithm. In an effort to find the optimal parameter setting for the BioHEL, the non-alternate and the alternate algorithms, the following three parameters are tested.
(1) number expressed attributes at initialization: $5,10,15,20$,
(2) the interval of the initial population: [0,0.1], $[0,0.25],[0.25,0.50],[0.25,0.75]$,
(3) probability of generalization/specialization: $0.1,0.3,0.6$.

Table 5
The rank of different parameter settings for the BioHEL on checkerboard datasets.

The resultant 48 combinations are listed in order in Table 5, where "\#Attr" refers to number of relevant attributes, "prob" probability of generalization and specialization, and "interval" the value interval for the initial population. For each setting, the BioHEL system which performed the best is identified in the last column.

Empirically, for both the BioHEL and the alternate algorithms, the optimal parameter setting is proved to be $10,[0.25,0.75], 0.6$ for the three parameters. For the non-alternate method, it is $10,[0.25,0.75], 0.3$. From Tables 5-7, it can be seen that, with respect to the interval parameter, the 3 BioHEL learning systems favored a more general setting as $[0.25,0.75]$ while the setting of $[0,0.1]$ resulted in poorer performance. The different systems showed a certain level of flexibility on the parameter of \#Attr since the four optional settings achieved comparable performance to each other. The top ranking settings for different systems also suggest a bias towards higher probability for the generalization and the specialization operations in order to combat the large number of noises.

After performing friedman test on the three algorithms each with their respective optimal parameter setting, the average rank

Table 6
The rank of different parameter settings for the non-alternate system on checkerboard datasets.

for BioHEL, non-alternate and alternate are respectively 2.28 , 2.17 and 1.56 with $p$-value $=0.06573$. It indicated that the alternate method performed better than the original BioHEL and the non-alternate algorithms.

## 6. Experiments on small-scale real-world problems

Experiments were further performed on 30 datasets from UCI repository (Blake \& Merz, 1998), whose detailed information is given in Table 8, with the 48 value combinations for the 3 parameters discussed previously. The setting on the rest of the parameters was given in Table 9.

The rank of the 48 value combinations for the different BioHELs were given in Tables 10-12. The optimal parameter setting for both the BioHEL, the non-alternate and the alternate can be read respectively as $20,[0.25,0.5], 0.1,15,[0,0.25], 0.1$ and $15,[0.25,0.75], 0.1$. The different BioHEL systems exhibited insensitivity, to some extent, to the value setting of the "interval" parameter. And in general, they favored low probability value for generalization and specialization

Table 7
The rank of different parameter settings for the alternate system on checkerboard datasets.

Table 8
summary of datasets.
Table 8 (continued)
Table 9
Base configuration of different BioHEL systems.
Table 10
The rank of different parameter settings for the conventional BioHEL on real-life problems.
Table 10 (continued)
Table 11
The rank of different parameter settings for the non-alternate system on real-life problems.

Table 12
The rank of different parameter settings for the alternate system on real-life problems.

and a higher setting on "\#Attr". It can be justified by the fact that, comparatively, these datasets contain much smaller amount of irrelevant attributes than the noisy checkerboard datasets. As a result, it did not depend on the generalization and specialization operations as heavily to identify significant attributes.

The BioHEL, the non-alternate and the alternate learning machines, each using their respective optimal parameter setting, were then applied to the 30 classification problems. Friedman tests were performed on the three algorithms, and the average rank for the BioHEL, the non-alternate and the alternate are respectively 2.0, 2.08 and 1.92 with $p$-value $=0.8$. The alternate method is proven to be the best method among the three.

## 7. Conclusions

In order to improve the performance of the newly-emerged BioHEL learning systems, the paper proposed to build a probabilistic model which identifies the significant attributes according to the fitness improvement upon the application of generalization and

specialization operators. Experiments on synthetic checkerboard datasets showed that, the introduction of the probabilistic model lead to the successful recognition of the checkerboard pattern even the original benchmark was added with 18 dimensions of Gaussian noises. In contrast, the conventional BioHEL system can only maintain satisfactory performances up to 7 extra attributes of noises. Experiments on small-scale datasets further confirmed the superiority, in terms of the classification accuracies, of the proposed BioHEL systems over the traditional one. It was also analyzed the impact of different parameter settings on the generalization of BioHEL systems. Future work will focus on the application of proposed BioHEL systems to large-scale problems.

## Acknowledgement

This work was supported by grants from the project of Zhejiang Provincial Natural Science Foundation of China (Project LQ13F030011).
