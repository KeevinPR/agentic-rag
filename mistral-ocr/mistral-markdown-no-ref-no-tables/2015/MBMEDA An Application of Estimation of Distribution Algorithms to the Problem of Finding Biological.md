# MBMEDA: An Application of Estimation of Distribution Algorithms to the Problem of Finding Biological Motifs 

Carlos I. Jordán ${ }^{(\boxtimes)}$ and Carlos. J. Jordán<br>Facultad de Ingeniería en Electricidad y Computación, Escuela Superior Politécnica del Litoral (ESPOL), Guayaquil, Ecuador<br>cjordan@espol.edu.ec


#### Abstract

In this work we examine the problem of finding biological motifs in DNA databases. The problem was solved by applying MBMEDA, which is a evolutionary method based on the Estimation of Distribution Algorithm (EDA). Though it assumes statistical independence between the main variables of the problem, results were quite satisfactory when compared with those obtained by other methods; in some cases even better. Its performance was measured by using two metrics: precision and recall, both taken from the field of information retrieval. The comparison involved searching a motif on two types of DNA datasets: synthetic and real. On a set a five real databases the average values of precision and recall were 0.866 and 0.798 , respectively.


Keywords: DNA dataset $\cdot$ Estimation of distribution algorithms $\cdot$ Molecular biology $\cdot$ Transcription factor $\cdot$ Motifs

## 1 Introduction

The search for biological motifs is an important problem in molecular biology. A motif or transcription factor binding site (TFBS) is the sequence of nucleotides in the promoting zone of a gene, where a transcription factor (TF) binds and controls the process of transcription of that gene into an mRNA molecule [1]. This molecule eventually will be translated into a protein at a cells ribosome; all this happens according to the central dogma of molecular biology.

Basically the problem can be formulated as follows: given a DNA base consisting of n promoting zones of size m , with one TFBS per sequence, find a pattern of length 1 that constitutes a motif. No doubt this problem is rather difficult, because we dont know a priori the length of the motif or its location in the promoting zone, neither the specific sequence of nucleotides we are looking for. To make matters even worse, the TFBS may mutate from one instance to another. Fig. 1 shows how difficult is to find a pattern of nucleotides on a real DNA base.

There exists, however, a key to break this code: the motif is a sequence of nucleotides of length 1 that repeats with the highest frequency in the DNA

taatgtttgtgctggtttttgtggcatcgggcgagaatagcgcgtggtgtgaaagactgtttttttgatcgttttcacaaaaatggaagtccacagtcttgacag gacaaaaaacgcgtaacaaaagtgtotataatcacggcagaaaagtccacattgattatttgcacggcgtcacactttgctatgccatagcatttttatccataag acaaatcccaataacttaattattgggatttgttatatataactttataaattcctaaaattaacaaaagttaataactgtgagcatggtcatatttttatcaat cacaaagcgaaagctatgctaaaacagtcaggatgctacagtaatacattgatgtactgcatgtatgcaaaggacgtcacattaccgtgcagtacagttgatagc acggtgctacacttgtatgtagcgcatctttctttacggtcaatcagcaaggtgttaaattgatcacgttttagaccattttttcgtcgtgaaactaaaaaaacc agtgaattatttgaaccagatcgcattacagtgatgcaaacttgtaagtagatttccttaattgtgatgtgtatcgaagtgtgttgcggagtagatgttagaata gcgcataaaaaacggctaaattcttgtgtaaacgatttccactaatttatccatgtcacacttttcgcatctttgttatgctatggttatttcataccataagcc gctccggcggggttttttgttatctgcaattcagtacaaaacgtgatcaacccctcaattttccctttgctgaaaaattttccatttgtctcccctgtaaagctgt aacgcaattaatgtgagttagctcactcattaggcaccccaggctttacactttatgcttccggctcgtatgttgtgtggaattgtgagcggataacaatttcac acattaccgccaattctgtaacagagatcacacaaagcgacggtggggcgtaggggcaaggaggatggaaagaggttgccgtataaagaaactagagtccgttta ggaggaggcgggaggatgagaacacggcttctgtgaactaaaccgaggtcatgtaaggaatttcgtgatgttgcttgcaaaaatcgtggcgattttatgtgcgca gatcagcgtcgttttaggtgagttgttaataaagatttggaattgtgacacagtgcaaaatccagacacataaaaaacgtcatcgcttgcattagaaaggtttct gctgacaaaaaagattaaacataccttatacaagactttttttttcatatgcctgacggagttcacacttgtaagttttcaactacgttgtagactttacatcgcc ttttttaaacattaaaattcttacgtaatttataatctttaaaaaaaagcatttaatattgctccccgaacgatttgtgatttcgattcacatttaaacaatttcaga cccatgagagtgaaattgttgtgatgtggttaacccaattagaatttgggatttgacatgtcttaccaaaaggtagaacttatacgccatctcatccgatgcaagc ctggcttaactatgcggcatcagagcagatttgtactgagagtgcaccatatgcggtgtgaaataccgcacagatgcgtaaggagaaaataccgcatcaggcgctc ctgtgacggaagatcacttcgcagaataaataaatcctggtgtccctgttgataccgggaagccctgggccaactttttggcgaaaatgagacgttgatcggcacg gattttttatactttaacttgttgatatttaaaggtatttaattgtaataacgatactctggaaagtattaaaagttaatttgtgagtggtcgcacatatcctgtt

Fig. 1. DNA base for searching the TFBS of CRP in Escherichia Coli
dataset. This clue reduces the problem to a mathematical one, i.e., an optimization problem. To solve it a number of different methods have been devised; among others: MEME (Multiple Expectation Maximization for Motif Elicitation) and BioProspector [2].

It is well known that optimization problems can be solved efficiently by evolutionary methods [3]. For instance: genetic algorithms are a good option; but in this case we are required to guess appropriate values for the rates of crossover and mutation, which are its classical operators [4]. We could avoid guessing these values if we use the method Estimation of Distribution Algorithm (EDA) [5]. However, in this case the challenge is to construct a good estimator. For the problem of finding biological motifs, it has been proposed in [6] to use a multivariate Gaussian estimator in order to capture possible correlations among the positions in the motif instances.

However, looking for simplicity and better processing times, we assume here that the nucleotides on a motif instance are statistically independent. Then, four univariate Gaussian Estimators (GE) will be required instead of a multivariate one to generate a new individual, where each estimator represents the distribution of a particular nucleotide estimated from the best individuals in the population. Our method will be called MBMEDA (Mtodo de Bsqueda de Motivos con base en un Algoritmo por Estimacin de Distribuciones) and its results will be compared systematically with those of EDAMD (Estimation of Distribution Algorithms for Motifs Discovery) published in [6]; this will allow us to explore two questions: 1) whether our method gives better or similar results compared with those of the multivariate approach, and 2) whether an EDA based motif search algorithm is more efficient than other computational motif search methods.

# 2 Materials and Methods 

To test MBMEDA we used two types of DNA datasets: synthetic and real. A synthetic base is generated artificially following criteria used in other similar

works: the length of the motif, the size of the promoting zones and the presence of noise [7]; in this bases a motif is implanted at known sites. On the other hand, in the real or biological DNA datasets, the sequences of nucleotides of the motif were determined experimentally by analyzing a number of promoting regions for each particular organism. Each biological dataset is labeled with the name of the TF that binds on its motif. Here we use five databases: CRP, E2F, ERF, ME2F and MYOD.

MBMEDA is a method that does a global search on the problem space of possible solutions, where a solution -also known as an individual- is defined by a vector VIP of the initial positions of a candidate motif on the n rows of the DNA dataset. Therefore, with each individual we associate a vector S of n sequences of length 1 that starts at the initial positions specified in VIP; we also associate with each individual a matrix of positional weights, denoted as PWM $\mathrm{m} \times \mathrm{l}$, where l is the length of the motif sequence and m the cardinality of the nucleotide alphabet, in this case $\mathrm{m}=4$. The PWM has one row for each symbol of the alphabet: 4 rows in our case; it also has one column for each position in the pattern of sequences [8]. Each entry on the PWM represents the relative frequency of a nucleotide on its correspondent column in S. See Fig. 2.
![img-0.jpeg](img-0.jpeg)

Fig. 2. Representation of an individual or candidate solution in MBMEDA

The initial population of individuals is usually generated randomly. The quality of a solution is evaluated by the fitness function, which in this case is the information content (IC) of the individual as defined by expression (1) [9] where fb is the frequency that nucleotide b appears at position i on the PWM and pb

is the frequency of b on the entire DNA base. At each iteration, a number of the best individuals in the current population will be chosen by a tournament selection operator, in order to model with them how solutions will distribute in the next generation.

$$
I C=\sum_{i=1}^{L} \sum_{b} f_{b}(i) \log \left(\frac{f_{b}(i)}{p_{b}}\right)
$$

The information content of an individual is a measure of the difference between the distribution of the nucleotides in the PWM -which represents a solution- and the distribution of the nucleotides on the entire DNA dataset. The larger is this difference, the more information content the solution has and, therefore, the larger is the possibility that it to be a motif. This concept of IC is crucial to the process of getting a subset of the best individuals in a population [10]; with them well estimate the four univariate gaussian models that will be used to calculate the next population.

Since we work here with the assumption of statistical independence of nucleotides on the motif instances, we have to estimate a set of four Univariate Gaussian distributions, one for each nucleotide, by calculating their corresponding values of mean and variance [11]. Then, by sampling the frequencies of these distributions using expression (2), well get the components for the new individuals in the next generation.

$$
I_{b}=\mu_{b}+Z * \sigma_{b}^{2}
$$

Where $I_{b}$ represents the component of nucleotide b for a sampled individual, $m u_{b}$ represents the mean of the distribution for nucleotide $b, \operatorname{sigma}_{b}^{2}$ represents its variance and Z is a vector of random values obtained by the Box Muller Transformation.

The EDA algorithm iterates until appropriate termination conditions are satisfied; in our case, the value of the fitness function for the best individual remains constant through at least 10 generations [12]. To avoid being trapped on local minima, at each iteration two operators unique to this method are applied after sampling: the Shift and the Local Filtering operators [6]. Fig. 3 presents a pseudo-code for the MBMEDA algorithm.

To measure the performance of EDA so that we are able to compare its results with those obtained by other methods, two metrics were used: Precision and Recall; both were taken from the field of Information Retrieval [13] and calculated by the following expressions (3) and (4), respectively; where $N_{c}$ represents the correct number of motif instances found by the algorithm, $N_{p}$ the number of promoter regions in the DNA database and $N_{t}$ represents the total number of real instances of the motif.

$$
\begin{gathered}
\text { Precision }=\frac{N_{c}}{N_{p}} \\
\text { Recall }=\frac{N_{c}}{N_{t}}
\end{gathered}
$$

```
MBMEDA (DNA database B):
    P // Population Set
    M // Estimated Gaussian Model
    Parents // Set of best individuals, chosen to estimate M
    Children // Set of new individuals generated from sampling M
    initialize P {randomly generated from B}
    repeat:
        for each individual pi in P do:
            fitness (pi)
        Best_Individual <- Best(P) // Best individual in P
        Parents <- Tournament Selection (P)
        M <- Estimate Gaussian Model (Parents)
        Children <- Sample Gaussian Model (M)
        Every 10 Generations do:
            Local Filtering (Children)
            Shift (Best (Children))
        P <- P U Children
    until (termination condition)
    return Best_Individual
```

Fig. 3. MBMEDA algorithm

Table 1. Results of MBMEDA applied on synthetic bases

# 3 Results 

Table 1 shows the MBMEDAs performance with different synthetic DNA bases that corresponds to each row in the table. When we include noise for each base -which represents a more realistic situation-, the average values for both metrics were above 0.90 ; this is certainly promising

Table 2. Results of applying MBMEDA and EDAMD on real DNA bases

Table 3. Results when MBMEDA and other methods are applied on real DNA bases
![img-1.jpeg](img-1.jpeg)

Fig. 5. Sequence logo of CRP motif consensus found by MBMEDA
[6]. Figure 5 on the other hand presents the sequence logo for the same motif as it was found by MBMEDA, the method proposed in this work.

# 4 Discussion and Conclusion 

From the tables and figures above, its clear that the results of applying MBMEDA on DNA synthetic and real databases are quite satisfactory; they are similar and in some cases better than those obtained by other methods, like EDAMD for example.

Comparing Fig. 4 and Fig. 5, we observe that logo sequences for the motif consensus of the TFBS of protein CRP resemble each other quite well, which confirms the good results obtained with MBMEDA when searching for a motif. All this would imply that the assumption of statistical independence among the positions of the nucleotides in the motif instances is a reasonable one. However, we still consider necessary to make a more rigorous analysis of this assumption, which is fundamental to the performance of EDA based methods, since it simplifies the modeling of distributions and the process of sampling new individual for the next population.

Acknowledgements. The authors would like to thank Dr. Daniel Ochoa, Director of the Artificial Vision and Robotics Laboratory at ESPOL, for its constructive comments that helped shape the present form of this work.
