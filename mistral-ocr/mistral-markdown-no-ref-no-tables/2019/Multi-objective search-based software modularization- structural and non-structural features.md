# Multi-objective search-based software modularization: structural and non-structural features 

Nafiseh Sadat Jalali ${ }^{1} \cdot$ Habib Izadkhah ${ }^{1}$ (1) $\cdot$ Shahriar Lotfi ${ }^{1}$<br>Published online: 29 November 2018<br>(c) Springer-Verlag GmbH Germany, part of Springer Nature 2018


#### Abstract

Software modularization techniques are employed to understand a software system. The purpose of modularization is to decompose a software system from a source code into meaningful and understandable subsystems (modules). Since modularization of a software system is an NP-hard problem, the modularization quality obtained using evolutionary algorithms is more reasonable than greedy algorithms. All evolutionary algorithms presented for software modularization only consider structural features that are dependent on the syntax of programming languages. For most programming languages, does not exist a tool to extract structural features, so it is not possible to modularize them. To overcome this problem, this paper presents a new multi-objective fitness function, named MOF, which exploits the structural (such as calling dependency and inheritance dependency) and non-structural features (such as semantic contained in the code comments and identifier names), aiming to automatically guide optimization algorithms to find a good decomposition of software systems. To evaluate the performance of this objective function, three optimization strategies, namely globalbased search, combining global and local search, and Estimation of Distribution (EoD), are adapted to optimize it. The results on Mozilla Firefox indicate that the proposed algorithm which is based on EoD along with the new MOF function outperforms the algorithms that use structural-based objective functions in guiding the optimization process, in finding more understandable modules.


Keywords Evolutionary algorithms $\cdot$ Modularization $\cdot$ Clustering $\cdot$ Estimation of distribution algorithm $\cdot$ Reverse Engineering

## 1 Introduction

Today, all large organizations are dependent on software systems. Adapting to the new requirements is one of the basic principles of these organizations. Therefore, to handle these requirements, it is necessary to keep the related software system up-to-date. During the maintenance process, to rejuvenate the application for newer needs, the

[^0]software architecture deviates from its original architecture, while these modifications are not well documented. Without up-to-date documentation, in the process of software maintenance, software engineers spend considerable time to understand the code of the software system, which indicates the importance of the program's understanding. For example, a study (see Pfleeger 2001; Pigoski 1996) reports that from 40 to $60 \%$ of the maintenance activity is spent on studying the program to understand it. Understanding a program is possible from design features, such as software architecture. The architecture of a software system represents the components and connections between them. Software modularization techniques are used to extract the software architecture from the source code, aiming to understand and maintenance of the software. Modularization has been used in two different areas in software engineering in the literature: software architecture recovery and refactoring. The purpose of the software architecture recovery is to use modularization


[^0]:    Communicated by V. Loia.
    Habib Izadkhah
    izadkhah@tabrizu.ac.ir
    Nafiseh Sadat Jalali
    nafisejalali1989@yahoo.com
    Shahriar Lotfi
    shahriar_lotfi@tabrizu.ac.ir
    1 Department of Computer Science, Faculty of Mathematical Sciences, University of Tabriz, Tabriz, Iran

techniques to partition a software system from the source code into meaningful and understandable subsystems. This helps to understand the software in the process of reverse engineering software. Refactoring also utilizes modularization, but with different goals. Refactoring approaches support big-bang re-modularization (meaning those taking a system as an input and providing it as output, as a completely new system with a new modularization). Some papers that use modularization to refactor the source code are (Bavota et al. 2012; Candela et al. 2016; Mkaouer et al. 2015). This paper aims to present modularization approaches to support software architecture recovery, not software refactoring.

Artifact Dependency Graph (ADG) is the input of modularization algorithms. In a software, depending on the type of software, any component such as class, method, function, or file can be considered as an artifact. Also, calling dependency or similarity between comments and etc. can be used as a dependency between artifacts.

To be a reasonable structure of software systems, artifacts placed within the same module should have the maximum connection/similarity to each other and artifacts in different modules should have the minimum relationship. Hence, most modularization methods use cohesion and coupling criteria to modularize a software system. Cohesion indicates the coherence of a module and coupling is the degree of interaction between modules. Candela et al. (2016) in an excellent paper named "Using Cohesion and Coupling for Software re-modularization: Is It Enough?". It was concluded that these criteria alone are not enough and other criteria are needed. Note that, they did not argue about what criteria are needed. In this paper, we aim at answering the following research questions:
(1) Which features in the source code can lead to modularization which is closer to the modularization created by the domain expert?
(2) Does a multi-objective fitness function that takes into account structural and non-structural features can improve modularization quality?
(3) Is the estimation of distribution-based algorithm able to produce higher-quality modularization compared with other search-based modularization algorithms?

In the most modularization algorithms, structural features such as cohesion and coupling are exploited for modularization. In this paper, in addition to the cohesion and coupling, we will examine the impact of inheritance relationships and non-structural features, e.g., identifier names and comments, on the modularization quality of a software system. Then, considering these structural and non-structural features, we propose a number of objectives and present a relationship which considers these objectives for modularization. Due to the NP-hardness of software
modularization problem, the use of search-based and evolutionary approaches such as genetic algorithm to be more efficient than other approaches (Isazadeh et al. 2017). The searching procedure in search-based algorithms can be performed in two ways: global search and local search. Global search-based methods usually consider the whole search space to find a good solution. These methods have an operator to explore new regions in search space. The genetic algorithm is one of the main search methods that uses the global search strategy. Local search algorithms utilize exploitation ability to improve the quality of the already existing solutions. These algorithms start from an initial solution and then iteratively move from the current solution to a neighbor solution (to be defined) in the search space by applying local changes. Hill climbing is one of the main search methods that uses the local strategy for search. To optimize the proposed multi-objective function, in this paper, we apply the genetic algorithm alone and also with two different combinations with the hill climbing algorithm, aiming to use the advantage of these two search algorithms.

Mutation and crossover operators and their probability have a great influence on the efficiency of the genetic algorithm. The main problem with a genetic algorithm is the lack of keep of building blocks and important patterns obtained during the evolutionary process. The building blocks may be destroyed after applying the crossover and mutation operators. This will slow down the process of the optimal solution finding. Estimation of Distribution (EoD)based algorithms are used to maintain the building blocks. To solve a problem, the EoD-based algorithms generate an initial population and construct a probabilistic model from it. The next generation is created based on the constructed probabilistic model, aiming to maintain valuable building blocks. Determining the mutation and crossover rates is one of the problems of genetic algorithms. EoD-based algorithms do not use concepts like mutations and crossovers to create a new population. In this way, eliminating the good solutions in the answers will be avoided as far as possible.

This paper proposes a new multi-objective fitness function which considers structural features (such as calling dependency and inheritance dependency) and latent semantic contained in non-structural features (such as identifier names and comments) for software modularization. We used the machine learning techniques for extracting latent semantic contained in non-structural features. To evaluate the performance of this objective function, three optimization strategies, namely global-based search, combining global and local search, and estimation of distribution, are adapted to optimize it. Each of these algorithms has unique features. The results on Mozilla Firefox, as a large-scale application, demonstrate that

modularization which is based on structural features outperforms those which are based on non-structural features. Moreover, combining the structural and non-structural features (i.e., the proposed multi-objective function) outperforms the structural-based objective functions in guiding the optimization algorithms to find more understandable modules. Furthermore, the results indicate that the algorithm which is based on the estimation of distribution strategy is better than the rest of the strategies in software system modularization.

The contributions of this paper are summarized as below:

1. Proposing a new objective function which considers structural and non-structural features;
2. The proposed multi-objective function is the first objective function that can use the latent semantic contained in non-structural features for software modularization;
3. Identifying non-structural features in the source code that can replace structural features. Most modularization algorithms utilize structural features such as Call Dependency for modularizing a software system. In a multi-lingual program, due to the different syntactic structure used in programming languages, it is not possible to extract calling dependency among programming languages. In this case, it is not possible to modularize it. Furthermore, for most programming languages, does not exist a tool to extract structural features, so it is not possible to modularize them. Therefore, in this study, we investigate the effect of non-structural features on modularization quality. The results demonstrate that identifier names, as a nonstructural feature, can be used instead of calling dependency with acceptable reliability.
4. Applying three search strategies for software modularization. These strategies are: (1) using global search, (2) combining global and local search, and (3) a proposed algorithm which is based on the estimation of distribution. These algorithms have not been studied by any researcher, to solve the software modularization problem, taking into account structural and nonstructural features simultaneously.

The structure of this paper is organized as follows: Sect. 2 addresses and evaluates the related works. Section 3 presents the proposed multi-objective functions and a number of evolutionary algorithms to optimize it. Section 4 evaluates the proposed algorithms, and Sect. 5 concludes the paper.

## 2 Related works

In the literature, clustering techniques can be categorized into data clustering techniques and graph clustering techniques. Some examples of data clustering techniques are (Abualigah et al. 2017a, b, 2018; Alswaitti et al. 2018; Liu et al. 2017). Graph-based clustering techniques can be applied to different areas such as social network, protein complex identification, image segmentation, and software clustering. Some examples of graph clustering techniques are (Chang et al. 2017; Wen et al. 2017).

Software modularization (or software clustering) algorithms can be classified into hierarchical and non-hierarchical (including search-based methods and greedy algorithms) categories.

Most presented hierarchical methods for software modularization are agglomerative. The overall process of modularization in these methods is that, initially, all artifacts are individually placed in separate modules. During an iterative process, based on certain criterion, e.g., Jaccard similarity criterion or Euclidean distance criterion, the similarity or dissimilarity is calculated between all artifacts, and artifacts with the highest similarity or least dissimilarity are merged together. Hierarchical methods tend to have the following issues:
(1) A well-defined criterion does not exist to determine where the modularization operation should end;
(2) Arbitrary decisions are one of the main issues in the hierarchical modularization methods. These decisions have a great impact on the final modularization;
(3) It is not possible to go back and correct the wrong choices;
(4) These algorithms cannot search the problem space well.

In the following, a number of hierarchical modularization methods are discussed.

Saeed et al. (2003) proposed a modularization algorithm named combined algorithm. This algorithm uses a binary data table to show relationships between artifacts and features. The Jaccard similarity measure is used in this algorithm to calculate the similarity between artifacts, and OR operator is employed to calculate the new feature vector from two previous feature vectors. Two major drawbacks of this algorithm are: it does not handle the arbitrary decision problem and does not take into account the number of artifacts that have access to a feature. To overcome this drawback, Maqbool and Babri (2004) proposed a modularization algorithm named weighted combined algorithm. This algorithm uses a weighted version of Jaccard, named Ellenberg similarity measure, to calculate

the similarity between artifacts. Andritsos and Tzerpos (2005) presented an entropy-based hierarchical clustering algorithm which uses structural and non-structural features to modularize a software system. The non-structural features considered are developers, directory path, lines of code, and time of the last update. Their results showed that ownership information had a positive impact on modularization and the use of lines of code is not a good idea. Time can be appropriate for a modularization factor in a different environment. To overcome the drawbacks in individual similarity criteria, such as Jaccard, Naseem et al. (2013) used cooperative clustering, which is a consensus-based technique. In this method, two similarity criteria named Jaccard and Jaccard-NM are employed to calculate the similarity between artifacts. The arbitrary decisions are the main problem of this algorithm. In Srinivas et al. (2013a, b), a method is proposed that applies the XOR similarity function to the Boolean matrix after specifying duplicate items for modularization. This method is greedy, and the input must be in binary forms. Naseem et al. (2014) used two modalities for modularization: one is a similarity criterion and another is distance aiming to improve the quality of the modules by reducing the number of arbitrary decisions. Misra (2012) and Misra et al. (2012) presented a hierarchical modularization algorithm that considers structural and non-structural features.

In search-based modularization techniques, the problem of modularization is treated as a search problem. Since searching the entire state space, transforms the problem into an NP-hard problem, it is used evolutionary approaches such as the genetic method to find the solution. Most search-based algorithms are single-objective, and their main aim is to find a modularization with maximum cohesion and minimum coupling. These algorithms aim is to maximize the objective function, MQ, indicated in Eq. 2. This function is applicable to weighted graphs, and its computational complexity is low, and this is one of the advantages of this objective function. This function is obtained from the sum of several module factors. The module factor for module i is shown with $\mathrm{CF}_{i}$, where $\mu_{i}$ represents the intra-connections and $\varepsilon_{i}$ represents interconnections between two modules.
$\mathrm{CF}_{i}=\frac{2 \times \mu_{i}}{2 \times \mu_{i}+\varepsilon_{i}}$
$\mathrm{MQ}=\sum_{i=1}^{k} \mathrm{CF}_{i}$
Mitchell in his Ph.D. thesis (Mitchell and Mancoridis 2002, 2006, 2008) proposed a genetic-based algorithm, named Bunch, for software modularization aiming to maximize the MQ. The encoding used in the Bunch is a value-based encoding so that the search space in it is $n^{n}$.

Parsa and Bushehrian (2005) proposed a modularization algorithm, named DAGC, which uses a permutation-based encoding against value-based encoding. This encoding is able to reduce the search space to n!. Both Bunch and DAGC are single-objective and consider CDG, as a structural feature, for modularization. Praditwong et al. (2011) proposed two multi-objective algorithms, named ECA and MCA, for modularization a software system. The objectives used in ECA are:

- The sum of edges within all modules should be maximized,
- The sum of edges within all modules should be minimized,
- The number of modules should be maximized,
- MQ should be maximized,
- The number of single-member modules should be minimized.

The objectives used in the MCA are similar to those used in ECA, with the difference that, instead of the last one, "the difference between the maximum and minimum number of artifacts in a module should be minimized," has been used. These two multi-objective algorithms consider only structural features and do not include the non-structural features. Tables 1, 2, 3, 4 and 5 show the algorithms available for hierarchical modularization methods, local search algorithms, global search algorithms, combining global and local search-based algorithm, and graph-based algorithms, respectively.

According to the literature, most modularization methods exploit search-based algorithms to modularize a software system. Also, according to Tables 2, 3, 4 and 5, most search-based methods utilize structural features such as calling relationship to perform modularization and do not consider the impact of inheritance relationship, as a structural feature, and non-structural features such as comments and identifier names. In this paper, in addition to structural features, we will also investigate the effect of non-structural features on modularization quality.

## 3 The proposed method

Due to the various factors affecting the result of modularization, this section, presents a method that resolves the limitations of the existing methods. Most existing methods only use call dependency graph as a structural feature for modularization, but for most programming languages, in the lack of the necessary tools, we will not be able to extract the call dependency graph. Hence, the proposed methods also consider semantic features (i.e., non-structural features) to extract software architecture. In this section, we will first present our multi-objective function and then five search-

Table 1 Hierarchical algorithms for modularization

Table 2 Local search-based algorithms for modularization
based algorithms from three different search-based strategies, are adapted to optimize this objective function.

### 3.1 New multi-objective fitness function

The new multi-objective function is able to consider both structural and non-structural features simultaneously and
also in separation. The structural features considered are calling dependency and inheritance similarity between artifacts, and the non-structural features considered are similarity between identifier names and similarity between comments. Clearly, for having a good modularization the following should hold:

Table 3 Global search algorithms for modularization

Table 4 Combining global and local search-based algorithms for modularization

Table 5 Graph-based algorithms for modularization
- The similarity between the comments should be maximized.
- The similarity between identifier names should be maximized.
- If there exist the inheritance relationships between artifacts, the similarity between them should be increased.
- Considering the calling dependency, the inter-connections within a module should be maximized and between modules should be minimized.

The overall process of the proposed method is shown in Fig. 1. To calculate these objectives (Fig. 1), we use the following relationships:

Textual similarity This criterion calculates the similarity between the two artifacts, considering the similarity between the comments in these two artifacts. Two artifacts are similar if they contain some of the same features. To calculate this similarity between two software's artifacts, we extract the comment strings from the source code and then tokenizes the strings into separate words. For example, consider the following comment.

Then, the stop words are eliminated from the lists generated, e.g., at, the, will, and so on. Finally, using Eq. 3, a co-occurrence matrix is constructed where the rows represent the artifacts and columns represent the number of repetitions of tokens.
$\delta_{\text {textual }}[i, j]=\sum_{r=1}^{r=1} C[i, r] C[j, r] / \sqrt{\sum_{r=1}^{r=1} C[i, r]^{2}} \sqrt{\sum_{r=1}^{r=1} C[i, r]^{2}}$
$t$, the total number of extracted tokens in the textual features; $C[i, r]$, the number of times of token $r$ occurs at artifact $i ; C[j, r]$, the number of times of token $r$ occurs at artifact $j ; \delta_{\text {textual }}[i, j]$, the textual similarity calculated between the two artifacts $i$ and $j$.

Identifier names similarity The artifact names, such as class name, method name, function name, are extracted from the source code and then tokenizes the extracted
artifact names into separate words. Equation 4 is used to create the co-occurrence matrix is. For example:
"Finance Control Manager"
includes the following tokens:
Finance, Control,Manager
$\delta_{\text {identifier }}[i, j]$
$=\sum_{r=1}^{r=Z_{c}} C[i, r] C[j, r] / \sqrt{\sum_{r=1}^{r=Z_{c}} C[i, r]^{2}} \sqrt{\sum_{r=1}^{r=Z_{c}} C[i, r]^{2}}$
$Z_{c}$, the total number of extracted tokens from artifact
names; $\delta_{\text {identifier }}[i, j]$, the identifier names similarity between the two artifacts $i$ and $j$.

Inheritance-based similarity To calculate the similarity between classes considering inheritance dependency, we extract the list of class-names, which are being extended or implemented by the class. For example:
Class className implements A1, A2, A3

The inheritance list extracted for the className would be $\{A 1, A 2, A 3\}$. Let $W_{\text {in }}[i]$ and $W_{\text {in }}[j]$ denote the inheritance list calculated for two classes $i$ and $j$, respectively. This similarity is calculated by Eq. 5.
$\delta_{\text {in }}[i, j]=\left|\frac{W_{\text {in }}[i] \cap W_{\text {in }}[j]}{\left|W_{\text {in }}[i] \cup W_{\text {in }}[j]\right|}\right|$
$\delta_{\text {in }}[i, j]$ the inheritance similarity between the two classes
$i$ and $j$.
To get the inheritance list for each class, we perform the following:
(a) Find the names of the classes which are in the inheritance list of this class.
(b) Find the names of the classes that this class is in their inheritance list.

![img-0.jpeg](img-0.jpeg)

Fig. 1 The overall process of combining structural and non-structural features

Considering these three similarity functions, the combined similarity between artifacts $i$ and $j$ is calculated by Eq. 6.
$\alpha_{i}+\alpha_{c}+\alpha_{\text {in }}=1$
$\delta_{\text {combined }}[i, j]=\alpha_{i} \times \delta_{\text {textual }}[i, j]+\alpha_{c} \times \delta_{\text {class }}[i, j]+\alpha_{\text {in }} \times \delta_{\text {in }}[i, j]$

Structural similarity To calculate the structural similarity, we consider the calling dependency between two artifacts. Let $\mu_{i}$ and $\varepsilon_{i, j}$ represent the intra-connections of module i and inter-connections between two modules $i$ and $j$, respectively. The quality of module i and an obtained modularization calculated by Eqs. 7 and 8, respectively.
$\mathrm{CF}_{i}= \begin{cases}0 & \mu_{i}=0 \\ \mu_{i}+\frac{1}{2} \sum_{i=1, j \neq i}^{k}\left(\varepsilon_{i, j}+\varepsilon_{j, i}\right) & \text { otherwise }\end{cases}$
$\delta_{\text {strutural }}=\sum_{i=1}^{k} \mathrm{CF}_{i}$
where $k$ indicates the number of modules. Let $m$ denote the number of artifacts, considering the combined similarity and structural similarity functions, the new multi-objective fitness function is calculated by Eq. 9.
$\delta_{n}+\delta_{s}=1$
$\mathrm{MOF}=\delta_{n} \times \frac{\sum_{i, j=1}^{m} \delta_{\text {combined }}[i, j]}{\frac{m(m-1)}{2}}+\delta_{s} \times \frac{\delta_{\text {strutural }}}{k}$

### 3.2 Discovering latent semantic between features

Latent Semantic Analysis (LSA) is a technique in natural language processing for discovering hidden concepts in document data and applied to a term-document matrix (Dumais, 2004). LSA represents the semantic similarity between documents that are utilized in the similar context. We use this technique for discovering latent semantic between non-structural features. An LSA uses a mathematical technique from linear algebra named Singular Value Decomposition (SVD) to reveal latent semantic. This technique applies on a term-document matrix and is represented by Eq. 10 and Fig. 2.
$M=U S V^{\mathrm{T}}$
$S$, ( $r$ : rank of the matrix); $U_{\mathrm{mr}}$, ( $m$ : document, $r$ : rank of the matrix); $V_{\mathrm{m}}^{\mathrm{T}}$, ( $n$ : term, $r$ : rank of the matrix).

Dimensionality reduction Let M indicate an artifact-feature matrix containing features counts per artifact (rows represent each artifact and columns represent unique

Fig. 2 The form of singular value decomposition after dimensionality reduction
![img-1.jpeg](img-1.jpeg)

Fig. 3 The overall evolutionary process of genetic algorithm
features) is formed from the source code. We use tf-idf (Abualigah et al. 2017a, b) to compute the value that each entry in the matrix should take. Then, SVD is used to reduce the number of features (i.e., dimensionality reduction) while preserving the similarity structure among artifacts. After reducing this matrix dimensions, artifacts that share with together, at the start, become more similar to together, and unlike artifacts, become more dissimilar as well. Therefore, dimensionality reduction makes it possible two artifacts that the exact same token do not appear in all of them, but both are from a particular subject, become more similar.

After extracting features and applying dimensionality reduction, we use genetic algorithm with two encodings, combining genetic algorithm and hill climbing in two different modes, and estimation of distribution to maximize the multi-objective fitness function. These algorithms are explained in the following subsections.

### 3.2.1 Modularization using genetic algorithm

A genetic algorithm is a search-based optimization technique, which mimics the principles of Genetics and Natural Selection to find a near optimal solution. This kind of algorithms use biological concepts such as selection,
crossover, and mutation. This algorithm is an iterative optimization procedure that works with a population of possible solutions represented by a chromosome aiming to improve the quality of chromosomes in each iterative. The steps to solve a problem with the genetic algorithm are shown in Fig. 3.

The main problem with a genetic algorithm is how to encode the solutions. Selecting the proper encoding scheme for solutions is a vital task. We use two types of encoding in the developed genetic algorithm named value-based encoding and permutation-based encoding. In both encodings, the number of genes of a chromosome is equal to the number of artifacts. Let $N$ denote the number of artifacts in the source code. In the value-based encoding, the content of each gene indicates a module number $\{1 \leq$ module number $\leq N\}$ that contains the corresponding artifact. In the permutation-based encoding, the content of gene ' $m$ ' of a chromosome includes an artifact number like ' $p$ ' $(1 \leq p \leq N)$, so that if ' $p$ ' is equal or greater than ' $m$ ', then ' $m$ ' is placed in a new module otherwise ' $m$ ' belongs to the same module that ' $p$ ' is located. Figures 4 and 5 give an example of these two encodings.

A fitness function is employed to evaluate the quality of each chromosome. In our algorithm, the fitness function for each chromosome is calculated as follows:

![img-2.jpeg](img-2.jpeg)

Fig. 4 Value-based encoding
![img-3.jpeg](img-3.jpeg)

Fig. 5 Permutation-based encoding

1. From the updated co-occurrence matrix, the artifact-toartifact similarity is calculated using Eq. 6;
2. The structural similarity is calculated for obtained modularization using Eq. 8;
3. The multi-objective fitness function is calculated using Eq. 9.

The roulette wheel method has been used to select parents. The main task of the crossover operator is to improve the fitness of a population and the most important task of the mutation operator is to avoid convergence to the local optimum. To apply a crossover operator, for each chromosome, a random number is chosen between $[0,1]$, if this number is less than or equal to the probability of crossover, the crossover is applied to that chromosome.

Fig. 6 One-point crossover

Parents

Children

Fig. 5. From the updated co-occurrence matrix, the artifact-toartifact similarity is calculated using Eq. 6;
2. The structural similarity is calculated for obtained modularization using Eq. 8;
3. The multi-objective fitness function is calculated using Eq. 9.

The roulette wheel method has been used to select parents. The main task of the crossover operator is to improve the fitness of a population and the most important task of the mutation operator is to avoid convergence to the local optimum. To apply a crossover operator, for each chromosome, a random number is chosen between $[0,1]$, if this number is less than or equal to the probability of crossover, the crossover is applied to that chromosome.

```
Algorithm 1: Estimation of Distribution Algorithm
1) Creating a probability Matrix
    - Create a square matrix \(\mathrm{n} * \mathrm{n}\) (n denotes the number of artifacts)
    - Initially, the values of all elements except the main diagonal are 1/n.
2) Generate initial Population
3) Evaluating the chromosomes by Eq. 9
4) Selecting and Updating:
    - Find the highest quality and lowest quality chromosomes
    - Update the probability model from the highest quality and lowest quality chromosomes as
        follows:
            - If two artifacts i and j are located in the same module in the highest quality chromosome
                but are not located in the same module in the lowest quality chromosome, their probability
                values are added in the probability matrix by \(1 /\) t, where t is the number of iterations.
                If two artifacts i and j are located in the same module in the lowest quality chromosome
                but are not located in the same module in the highest quality chromosome, their probability
                in the probability matrix are reduced by \(1 /\) t, where t is the number of iterations.
    5) Sampling (creating a new population using new probability matrix):
        - Creating a new population using the new probability model
        - Use the upper triangular matrix to produce each chromosome
        - Select, randomly, a row from probability matrix
        - Generate a random number for each selected row element between \([0,1]\)
            - If this value is smaller or equal to the probability of the element, the related artifacts are
                located in the same module.
```

6) Elitism
7) Test the termination condition

We illustrate with an example how to create and update a probabilistic model. Suppose a software system consists of five artifacts denoted by F1-F5. Figure 7 shows the initial probabilistic model matrix for this software system so that the values of all elements except the main diagonal are $1 / n$ ( $n$ is the number of artifacts). Also, assume that $a$, $b$ and $t=10$ indicate the chromosome with the highest quality in the initial population, the chromosome with the lowest quality in the initial population, and the algorithm iterations, respectively (Fig. 8). To update the probabilistic model matrix, since two artifacts F1 and F2 are located in the same module in the highest quality chromosome but are not located in the same module in the lowest quality chromosome, hence, their probabilities values are added in the probability matrix by $1 / 10$. In contrast, because two artifacts F3 and F4 are located in the same module in the lowest quality chromosome but are not located in the same module in the highest quality chromosome; hence, their probabilities in the probability matrix are reduced by $1 / 10$. Figure 9 shows the updated probabilistic model matrix.

In the EoD, the new population is sampled as follows: from the probabilistic model, a row is randomly selected. Given the upper triangular part of the probabilistic matrix,

Fig. 7 A sample initial probability matrix for a software system with five artifacts


a: the highest quality chromosome
b: the lowest quality chromosome
Fig. 8 Selecting the highest quality and lowest quality chromosome

Fig. 9 Updated probability matrix
for each element of the selected row, a random number is generated between 0 and 1 ; if this random number is equal to or less than the probability of the element in the row, these two artifacts will be placed in the same module in the new chromosome. This is repeated for all elements in the selected row. If all elements of the selected row in the probability matrix were examined, but the chromosome was not completely modularized, then a new row from the probability model matrix would be randomly selected and, until the chromosome is completed, the random number generation operation is repeated.

For example, consider Fig. 10. In this figure, R1 shows the selected row and F1-F5 represents artifacts. For each element of the selected row, a random number is generated

Fig. 10 Create a new population using a new probability matrix
![img-4.jpeg](img-4.jpeg)

Fig. 11 Two first generations of distribution estimation algorithm
between 0 and 1 , which is represented by $R 2$. Suppose $R 1=2$ and the random number generated is equal to 0.12 ; since this random number is smaller than the probability value of the element in F2F3 (Fig. 9), these two artifacts in the chromosome will be in the same module (Fig. 10). A random number is generated for all elements of row 2 ; as shown in Fig. 10, the random number 0.43 is larger than the probable value in F2F4. So this entry will remain currently empty. The random number 0.2 is generated for the F2F5 element, which is equal to its probability value; so F5 with F2 and F3 will be placed in the same module. Since all the elements of the selected row in the probability matrix were examined, but the chromosome was not completely modularized, the new row is randomly selected again, as shown in Fig. 10, $R 1=1$ is randomly selected, and the steps above are repeated until the chromosome is completed.

Figure 11 shows first two generations of our proposed algorithm, and Fig. 12 shows the construction process of probability model for distribution estimation algorithm.

### 3.2.3 Modularization using the genetic and hill climbing algorithm

The hill climbing algorithm is one of the most popular local search algorithms to modularize the source code. It is
an iterative algorithm that starts with a random initial solution from the search space and then, a new solution is produced by modifying the initial one (Isazadeh et al. 2017). Two major drawbacks of the hill climbing algorithm are trapping in local optima and its low stability. In the hill climbing, several percent of the chromosomes are selected from a population and each chromosome selected from this population is regularly improved by this algorithm. The concept of neighbor modularization is illustrated in Fig. 13. In this figure, A shows the current modularization and B-D are three neighbor modularizations for it. For example consider the node $a$, so that in B , it moved into module 4 , in C , it moved into module 2 , and in D , it moved into module 3 .

We define two versions of hill climbing namely Next Ascent Hill Climbing (NAHC) and Steepest Ascent Hill Climbing (SAHC). In NAHC, the algorithm stops when the first neighboring modularization found with a higher fitness value. In SAHC, the algorithm stops after examining the percentage of neighboring modularizations and choosing the one with the largest fitness value. The total number of neighbors for the current modularization is calculated by Eq. 11. Algorithm 2 shows the hill climbing algorithm.

```
Algorithm 2: Hill-Climbing Algorithm
Input: getting a current modularization
Output: the best neighbor of a modularization
Step1- Compute the total number of neighbors for current modularization using Eq. 11, and determine the
threshold t. This threshold determines how many percents of the current modularization neighbors must be
assessed to find the next modularization.
Step 2- Searching for the best neighbor for current modularization:
    - In the NAHC: algorithm generates a random neighbor modularization and examine it. If the quality of
        the neighbor modularization, i.e. MOF, is higher than the current modularization, another neighbor
        modularization is produced to the new modularization, and so on until no further improvements can be
        found.
    - In the SAHC: algorithm generates all neighbors for a modularization and examine them, then, the best
        neighbor modularization is returned.
```

The genetic algorithm (GA) is a global search algorithm and the hill climbing algorithm is a local search algorithm. To use the advantage of these two search algorithms, we combine them. This approach is applied in two ways: (1) the combining genetic algorithm with hill climbing algorithm named CGH, and (2) applying genetic algorithm and
![img-5.jpeg](img-5.jpeg)

Fig. 12 Probability model of distribution estimation algorithm

![img-6.jpeg](img-6.jpeg)

Fig. 13 Neighborhood for node $a$
then running hill climbing algorithm once at the end of process named CGoH. In the combination of these two algorithms, the process of the genetic algorithm is similar to Sec. 3.2.1, with the difference that in the proposed approach after the elitism stage, on the percentage of the selected population, the hill climbing algorithm is applied. Among the selected chromosomes, a chromosome has the highest fitness value, and the rest are randomly selected. In the CGH, in each generation of the genetic algorithm, a number of solutions are given to the hill climbing algorithm aiming to improve the quality of these solutions. Figure 14 shows this process. In the CGoH, after the run of the genetic algorithm is completed, for improving the quality of the modules obtained, the solutions are given to the hill climbing algorithm. Figure 15 shows this process.

## 4 Experimental results

In this section, the performance of MOF is evaluated using the developed algorithms. Also, the effect of discussed features (structural and non-structural) is addressed on the modularization quality of a software system. The groundtruth architectures are used to evaluate the reliability of the modularization algorithms (Garcia et al. 2013). In this paper, the MoJo (Tzerpos and Holt 1999) and MoJoFM (Wen and Tzerpos 2004) criteria are exploited to validate and compare the modularization obtained by the algorithms on Mozilla Firefox, which have a ground-truth structure. We used Build, Browser, Db, which are the folders from Mozilla Firefox, for this aim. The MoJo criterion calculates the number of "move" and "join" operations needed to
reach from one modularization to another and is defined as a distance criterion. The less number of moves and join operations, the more similar the two clusters are. The MoJoFM measure is specified in Eq. 12.
$\operatorname{MoJoFM}=1-\frac{\operatorname{mno}(A, B)}{\max (\operatorname{mno}(\forall A, B))} \times 100 \%$
where $\operatorname{mno}(A, B)$ indicates the minimum number of move or join operations required to transform modularization $A$ to $B$ and $\max (\operatorname{mno}(\forall A, B))$ indicates the maximum of the minimum number of possible operations of move or join needed to transform $A$ to $B$. This measure allows us to compare the modularization obtained by various techniques according to their similarity with the expert modularization, i.e., the higher value of MoJoFM, the more similar of modularization obtained by an algorithm to expert modularization. A value of $100 \%$ confirms that the modularization obtained is the same with an expert's modularization.

In brief, a small value of MoJo and large value of MoJoFM show that the resultant modularization is close to the domain expert modularization (ground-truth modularization). Let $n$ denote the number of artifacts, Table 6 gives the parameter setting for the experiments. In genetic algorithms, the number of generations is usually greater than the population size. Therefore, we have followed this principle in the proposed algorithms, and we also considered this value linearly and a coefficient of the number of artifacts. To set the probability of mutation and crossover operators, twenty different pairs of mutation and crossover probabilities have been tested on the Db folder using the proposed algorithms. For example, Fig. 16 shows one of

![img-7.jpeg](img-7.jpeg)

Fig. 14 The combination of genetic and hill climbing algorithms. a Combining genetic algorithm and Steepest Ascent Hill climbing algorithm (SAHC), b combining genetic algorithm and Next Ascent Hill climbing algorithm (NAHC)
these experiments using the genetic with value-based encoding.

The MoJoFM values computed for the algorithms, considering each extracted feature and combination of these features, on three folders of Mozilla Firefox are shown in Tables 7, 8, 9 and 10. NA (Next Ascent) and SA (Steepest Ascent) indicate the type of hill climbing, and "Best" and "Average" show the best and mean results of the used criterion among 10 runs of the algorithms. The best results in Tables 7, 8, 9 and 10 are highlighted in bold. As shown in Tables 7, 8, 9 and 10, in $75 \%$ of the cases, the distribution estimation algorithm (EoD) gives better results compared to the best MoJoFM, and in $67 \%$ of the cases, this algorithm gives better results compared with the average. After that, the combination of genetic algorithm and hill climbing, i.e., CGH, leads to better results.

In the following, the convergence and stability of the algorithms and features are evaluated; and moreover, for more evaluation, $T$-test is used to assess the stability.

Convergence To evaluate more precisely, we investigate the results of the algorithms from the convergence diagrams. Figures 17, 18, 19, 20, 21, 22 and 23 indicate the convergence of algorithms on features. The algorithms for Build, Browser, and Db folders are, respectively, executed in three generations of 400,800 and 1000 . The best individual of each generation in these figures is represented by a blue line. As can be seen in these figures, the best individual of every generation is above the average of that generation's fitness. In comparison between algorithms, the CGH and EoD algorithms are convergent in a smaller number of iteration. Compared to the features, the

![img-8.jpeg](img-8.jpeg)

Fig. 15 Applying genetic algorithm and then running hill climbing algorithm once at the end of process. a Combining genetic algorithm and Next Ascent Hill climbing algorithm (NAHC), b combining genetic algorithm and Steepest Ascent Hill climbing algorithm (SAHC)

Table 6 The parameter setting for experiments

structural feature converges in a smaller number of iterations than the rest, but other features also have no significant difference with the structural feature.

Stability The meta-heuristic algorithms such as genetic algorithms are stochastic optimizers. Hence, to compare the results, they need to be run multiple time and some statistical techniques such t-test should be used to compare the results. The stability of evolutionary algorithms in different runs is one of the problems with these algorithms. An evolutionary algorithm is stable if the results are close to each other, in different runs. Figures 24, 25, 26, 27, 28, 29, 30, 31 and 32 depict stability of algorithms on features. In these figures, the width axis represents the fitness value obtained from different runs and the length axis represents the run number. To calculate the stability, the algorithms are executed ten times. The comparisons between the algorithms in the stability diagrams show that in the CGH and EoD algorithms, the results are close together in different runs. The comparisons between the features in

Fig. 16 Parameter setting for crossover and mutation
![img-9.jpeg](img-9.jpeg)

Table 7 Comparing the algorithms on text features in terms of MoJoFM

Table 8 Comparing the algorithms on identifier names features in terms of MoJoFM

Table 9 Comparing the algorithms on structural features in terms of MoJoFM

Figs. 29, 30, 31 and 32 demonstrate that using non-structural features for modularization, the stability is also close to the algorithms that use structural features.

T-test Independent samples test has been used to assess the stability of an algorithm by computing the difference between the mean of two populations with each other.

Table 10 Comparing the algorithms considering the multi-objective fitness function in terms of MoJoFM

![img-10.jpeg](img-10.jpeg)

Fig. 17 Genetic with value-based encoding on textual features
![img-11.jpeg](img-11.jpeg)

Fig. 18 Genetic with permutation-based encoding on textual features
![img-12.jpeg](img-12.jpeg)

Fig. 19 EoD algorithm on structural features
Tables 11, 12, 13 and 14 show $T$-test results for the algorithms. To apply this test, the modularization results of the 10 runs of the algorithms are grouped into two groups of 5 , named $N 1$ and $N 2$. We apply this test in two ways:
![img-13.jpeg](img-13.jpeg)

Fig. 20 CGH on text features
![img-14.jpeg](img-14.jpeg)

Fig. 21 EoD algorithm on textual features
![img-15.jpeg](img-15.jpeg)

Fig. 22 EoD algorithm on identifier names features
descriptive statistics (including the first three columns) and the inferential statistics (including last two columns). In the descriptive statistics, Mean, SD and SE Mean denote the

![img-16.jpeg](img-16.jpeg)

Fig. 23 EoD algorithm on MOF
![img-17.jpeg](img-17.jpeg)

Fig. 24 Genetic with permutation-based encoding on structural features
![img-18.jpeg](img-18.jpeg)

Fig. 25 Genetic with value-based encoding on textual features
![img-19.jpeg](img-19.jpeg)

Fig. 26 EoD algorithm on structural features
average of both groups, the standard deviation of the two groups, and the standard error between mean the two groups, respectively. Inferential statistics also include two parts. In the first part of the fourth column, the output of the inferential statistics, if Sig. be greater than 0.05 , the
![img-20.jpeg](img-20.jpeg)

Fig. 27 CGH on structural features
![img-21.jpeg](img-21.jpeg)

Fig. 28 CGoH on structural features
![img-22.jpeg](img-22.jpeg)

Fig. 29 EoD on textual features
![img-23.jpeg](img-23.jpeg)

Fig. 30 EoD on identifier names features
assumption of the equality of variance is not rejected, and the information in the second part of this column is used to assess the average. if Sin. be greater than 0.05 , the assumption of the equality of the meanings is determined but if the equality of variance is rejected. The information of the second part of the fifth column is examined for the comparison of the mean. Comparison of stability and

![img-24.jpeg](img-24.jpeg)

Fig. 31 EoD on structure features
![img-25.jpeg](img-25.jpeg)

Fig. 32 EoD on MOF
convergence between features showed that in the absence of structural features, non-structural features can also be used.

Figures 33, 34 and 35 compare the number of modules generated from the proposed algorithms and created by the expert, considering structural and identifier names features. As these figures indicate, the number of modules generated by EoD and CGH algorithms is close to the number of modules created by the expert. As the figures show, in these two algorithms, the number of modules generated from the identifier names features is close to the number of modules generated from the structural features. This means that in the absence of tools for extracting structural features, identifier names features can be used.

Figures 36, 37 and 38 depict the best MoJo obtained by the proposed algorithms for the three folders of Mozilla Firefox. The blue color gives mojo for the structural features and orange color for the code features. In EoD and CGH algorithms, in most cases, the results are better, as can be seen in these figures. Given that MoJo has an inverse relation with quality, the smaller MoJo denotes the more quality. The comparison between the features demonstrates that structure feature, identifier names features, and then textual features, respectively, have the best MoJo (smaller MoJo are perfected). Moreover, it can be concluded that, in most cases, the modularization quality obtained using structural features is greater than those obtained using non-structural features.

Table 15 compares the EoD algorithm with a number of state-of-the-art modularization algorithms in terms of

Table 11 T-test code feature for the Build, Browser, and Db folders

Table 12 T-test textual feature for the Build, Browser, and Db folders

Table 13 T-test combining structural and non-structural features for the Build, Browser, and Db folders

Table 14 T-test Structure feature for the Build, Browser, and Db folders

Fig. 33 The number of modules obtained in the proposed algorithms for the Build

Fig. 34 The number of modules obtained in the proposed algorithms for the Browser
![img-26.jpeg](img-26.jpeg)

Fig. 34 The number of modules obtained in the proposed algorithmS for the Browser
![img-27.jpeg](img-27.jpeg)

MoJoFM. The best results in Table 15 are highlighted in bold. As can be seen in this table, in folders of Db and Build, the EoD outperforms other algorithms. In contrast, in the Browser folder, the MCA and Neighborhood tree
algorithms outperform other algorithms. The reasons why the proposed algorithm, in this folder, failed to perform better than these two algorithms are: (1) by checking this folder, we found that call dependency, as a structural

Fig. 35 The number of modules obtained in the proposed algorithms for the Db
![img-28.jpeg](img-28.jpeg)
![img-29.jpeg](img-29.jpeg)

Fig. 36 MoJo in the proposed algorithms for the Build
![img-30.jpeg](img-30.jpeg)

Fig. 37 MoJo in the proposed algorithms for the Browser
![img-31.jpeg](img-31.jpeg)

Fig. 38 MoJo in the proposed algorithms for the Db
features, in this folder is high and effects on other features; and (2) also the artifacts names are not named meaningfully by developers.

The results from this study indicate:

Table 15 Comparison of EoD with a number of state-of-the-art algorithms in terms of MoJoFM

(1) In software systems where the comments and identifier names are chosen meaningful by developers, the modularization achieved by the proposed multi-objective fitness function will have a higher quality.
(2) Due to the maintenance of building blocks during the evolutionary process, in most cases estimation of distribution algorithms achieve higher-quality solutions, in contrast to the genetic algorithm and hill climbing and their combination.
(3) By studying the structural and non-structural features separately, we realized that the modularization obtained by an algorithm which considers structural features has a higher quality than those which consider non-structural features. Of course, this difference is not high. Therefore, non-structural features can be used if it is not possible to extract structural features from a program.

## 5 Conclusions

Software architecture recovery plays an increasingly essential role in software maintenance tasks. Source code comprehension (source code understanding) is a vital

software maintenance activity concerned with the ways software engineers maintain existing source code. To recover software architecture, various modularization techniques have been employed to automatically partition a software system into meaningful subsystems, to support source code comprehension. This paper presented a new multi-objective fitness function aiming to modularize a software system from its source code. The presented objective function enables evolutionary algorithms to modularize a source code taking into account structural non-structural features. The structural features used in this paper are call dependency graph and inheritance relationships, and non-structural features used are textual, identifier names, and comment. We presented the equations to calculate these features from a source code. Also, to simplify the interpretation of information, the dimensionality reduction is applied to non-structural features. To modularize a software system using these features, five algorithms namely genetic algorithms with two encodings, distribution estimation algorithm, a combination of the genetic and hill climbing algorithms in two ways, are adapted to optimize the presented multi-objective fitness function. The results of the proposed algorithms are evaluated with different criteria such as Mojo and MoJoFM. The results of the evaluations indicated that the modularization produced by distribution estimation algorithm is close to the expert modularization. Also, we evaluated the results in terms of convergence and stability. Using these evaluations and the slight differences between the features, it is observed that in the absence of structural features, non-structural features could be used instead. It is concluded that identifier names features could be a better alternative in the absence of structural features.

### 5.1 Future work

The following suggestions are made for future works:

- Presenting semantic and nominal dependency graphs, to support multi-programming software systems modularization;
- Creating a thesaurus for programming languages and using it to calculate the similarity between comments and identifier names;
- Using the information theory in the objective function
- Using feature selection methods such as algorithms presented in (Abualigah and Khader 2017; Abualigah et al. 2016) for extracting features from the source code.
- In the estimation of distribution algorithms, the quality of the solutions depends on the probabilistic model that has been made. We believe that the Gaussian
probability distribution function can improve the accuracy of the constructed probability model.

Funding There is no funding for this study.

## Compliance with ethical standards

Conflict of interest All authors declare that they have no conflict of interest.

Ethical approval This article does not contain any studies with human participants performed by any of the authors.
