# Full-Space LDA With Evolutionary Selection for Face Recognition ${ }^{1}$ 

Xin Li, Bin Li, Hong Chen<br>University of Science and Technology of China<br>MOE-Microsoft Key Laboratory of Multimedia Computing and Communication Hefei, 230026 Anhui, China<br>\{simonlee,hongchen\}@mail.ustc.edu.cn<br>binli@ustc.edu.cn


#### Abstract

Linear Discriminant Analysis (LDA) is a popular feature extraction technique for face recognition. However, it often suffers from the small sample size problem when dealing with the high dimensional face data. Some approaches have been proposed to overcome this problem, but they usually utilize all eigenvectors of null or range subspaces of within-class scatter matrix( $S_{W}$ ). However, experimental results testified that not all the eigenvectors in the full space of $S_{W}$ are positive to the classification performance, some of which might be negative. As far as we know, there have been no effective ways to determine which eigenvectors should be adopted. This paper proposes a new method EDA+Full-space LDA, which takes full advantage of the discriminative information of the null and range subspaces of $S_{W}$ by selecting an optimal subset of eigenvectors. An Estimation of Distribution Algorithm (EDA) is used to pursuit a subset of eigenvectors with significant discriminative information in full space of $S_{W}$. EDA+Full-space LDA is tested on ORL face image database. Experimental results show that our method outperforms other LDA methods.


## 1. Introduction

Linear Discriminant Analysis (LDA)[1] is a wellknown scheme for feature extraction and dimension reduction. It has been used widely in many applications such as face recognition, image retrieval, etc. The basic idea of LDA is to find a set of projection

XianJi Wang, ZhengQuan Zhuang<br>University of Science and Technology of China<br>MOE-Microsoft Key Laboratory of Multimedia Computing and Communication Hefei, 230026 Anhui, China xjw @ mail.ustc.edu.cn zqzhuang @ ustc.edu.cn

vectors maximizing the between-class scatter matrix $\left(S_{k}\right)$ while minimizing the within-class scatter matrix ( $S_{W}$ ) in the projected feature subspace. A major drawback of LDA is that it often suffers from the small sample size (S3) problem when dealing with the high dimensional face data. When there are not enough training samples, $S_{W}$ would be singular, and it would be difficult to compute the LDA vectors.

In recent years, direct linear discriminant analysis (DLDA)[2] and null-space linear discriminant analysis (NLDA)[3] have been proposed to overcome the S3 problem in the face recognition. DLDA discards the null space of $S_{k}$, since the rank of $S_{k}$ is smaller than of $S_{W}$, that might lose some information of null space of $S_{W}$. NLDA extracts discriminant information from the null space of $S_{W}$, however, when the number of training sample is large, the null space of $S_{W}$ becomes small, and much discriminative information outside this null space will be lost. Both DLDA and NLDA may lose some discriminative information. In order to solve the S3 problem and still preserve all discriminative information, Optimal Fisher Linear Discriminant Algorithm (OFLDA) [4] and Dual-space LDA [5] are proposed to simultaneously apply discriminant analysis in the range and null subspaces of $S_{W}$ respectively, here called Full-space LDA. A common drawback of Full-space LDA is that they use all eigenvector in the range and null subspaces of $S_{W}$. They assume that keeping all eigenvector means keeping all of the discriminative information that can improve the classification accuracy efficiently.

[^0]
[^0]:    ${ }^{1}$ Correspondence should be addressed to Bin Li(email: binli@ustc.edu.cn).

However, from the pattern classification point of view, this assumption may not incorrect. The main reason is that not all the eigenvectors in the full space of $S_{W}$ are positive to the classification performance, some of which may be passive to classification. Therefore, choosing all eigenvector of the range and null subspaces of $S_{W}$ as the bases for LDA may not be optimal. As far as we known, there is no systematic way to determine which eigenvectors should be used.

Along this line, this paper focuses on the Full-space LDA as mentioned and proposes a Full-space LDA with evolutionary selection. EDA is used to pursuit a subset of eigenvectors with significant discriminative information in full space of $S_{W}$. Compared with FullSpace LDA, the proposed method can effectively eliminate less discriminatory eigenvectors and improve classification accuracy. The experiments on ORL face database clearly demonstrate its efficacy.

The rest of the paper is organized as follows: Section 2 provides the background on LDA and Fullspace LDA. Section 3 describes the details of EDA + Full-space LDA. Experimental results are reported in Section 4. Finally, we draw the conclusion in Section 5.

## 2. Background of LDA and Full-space LDA

### 2.1. LDA

Let the training set contains $C$ classes and each class $X_{i}$ has $n_{i}$ samples, $x_{k}$ is a sample belonging to class $X_{i}, m_{i}$ is the center of class $X_{i}, m$ is the center of the whole training set. $S_{W}$ and $S_{b}$ are defined as Eq. (1) and Eq. (2),

$$
\begin{aligned}
& S_{w}=\sum_{i=1}^{C} \sum_{k=C_{i}}\left(x_{k}-m_{i}\right)\left(x_{k}-m_{i}\right)^{T} \\
& S_{b}=\sum_{i=1}^{C} n_{i}\left(m_{i}-m\right)\left(m_{i}-m\right)^{T}
\end{aligned}
$$

The total-class scatter matrix is defined as Eq. (3)

$$
S_{t}=S_{b}+S_{w}=\sum_{i=1}^{n}\left(x_{i}-m\right)\left(x_{i}-m\right)^{T}
$$

LDA method tries to find a set of projection vectors $W_{n p t}=\left(w_{1}, w_{2}, \ldots, w_{L}\right)$ that maximizes the ratio of the absolute value of the between-class scatter matrix to the absolute value of the within-class scatter matrix (Fisher's criterion), as defined in Eq. (4).

$$
J\left(W_{o p t}\right)=\arg \max _{W} \frac{\left|W^{T} S_{b} W\right|}{\left|W^{T} S_{W} W\right|}
$$

If $S_{W}$ is not singular, $w_{1}, w_{2}, \ldots, w_{L}$ are the eigenvectors of $S_{W}^{-1} S_{b}$, corresponding to $\mathrm{L}(\mathrm{C}-1)$ largest eigenvalues. However, when the small sample size problem occurs, $S_{W}$ becomes singular and the inverse of $S_{W}$ does not exist. To avoid the singularity of $S_{W}$, Fisherface[6], DLDA and NLDA is usually adopted. A common problem with all these LDA approaches is that they all prone to lose some discriminative information in the high dimensional face space. Then Full-space LDA (OFLDA and Dualspace LDA) is proposed, which simultaneously apply discriminant analysis in the range and null subspaces of $S_{W}$ in order to preserve the all discriminative information. The experimental results in [7] show that full-space LDA outperforms the other LDAs.

### 2.2. Full-space LDA

Let $R^{d}$ be the original sample space, $V$ be the range subspace of $S_{W}$, and $V^{\perp}$ be the null subspace of $S_{W}$. That is

$$
V=\operatorname{span}\left\{\alpha_{k} \mid S_{w} \alpha_{k} \neq 0 \quad, k=1, \ldots, r\right\}
$$

And

$$
V^{\perp}=\operatorname{span}\left\{\alpha_{k} \mid S_{w} \alpha_{k}=0 \quad, k=r+1, \ldots, d\right\}
$$

Where $r<d$ is the rank of $S_{W},\left\{\alpha_{1}, \ldots, \alpha_{d}\right\}$ is an orthonormal set, and $\left\{\alpha_{1}, \ldots, \alpha_{r}\right\}$ is the set of orhtonormal eigenvectors corresponding to the nonzero eigenvalues of $S_{W}$.

From the range and null subspaces of $S_{W}$, the LDA projection vectors can be computed according to different criterions, respectively.

$$
\begin{gathered}
\left\{\begin{array}{c}
J_{\text {range }}\left(W_{\text {nept }}\right)=\arg \max \left|\frac{W_{r}^{T} S_{b} W_{r}}{W_{r}^{T} S_{w} W_{r}}\right| \\
W_{r}^{T} S_{w} W_{r}>0
\end{array}\right. \\
\left\{\begin{array}{c}
J_{\text {null }}\left(W_{\text {nept }}\right)=\arg \max \left|W_{n}^{T} S_{b} W_{n}\right| \\
W_{n}^{T} S_{n} W_{n}=0
\end{array}\right.
\end{gathered}
$$

This is to say, we intend to find the discriminant vectors of the range subspace of $S_{W}$ based on the Fisher criterion and utilize $J_{\text {null }}\left(W_{\text {nup }}\right)$ to get those of the null subspace of $S_{W}$. The two sets of discriminative features are combined for recognition.

### 2.3. Analysis on Full-space LDA

Full-space LDA uses all eigenvectors in the range and null subspaces of $S_{W}$. It assumes that keeping all eigenvectors means keeping all of the discriminative information that can improve the classification accuracy efficiently. However, experimental results show that this is not definitely right. The main reason probably is that not all the eigenvectors in the full space of $S_{W}$ are positive to the classification performance, some of which may be negative to classification. So simply using all the eigenvectors is not optimal from the point of view of pattern classification.

The ORL database with 40 persons (three training images/person and two test images/person) is used to perform an experiment as an example. Fig. 1 plots accuracy rates with the different number of eigenvectors in full space of $S_{W}$, the eigenvectors of the null subspace of $S_{W}$ are all selected. When the number of eigenvector in range subspace increases to 51 , the accuracy reaches the $96.25 \%$. However, when the eigenvectors are all selected, the rate is just $91.25 \%$. This intuitive observation indicates that some eigenvectors might be negative to classification accuracy. Therefore, a strategy for selecting the eigenvectors with significant discriminative information in full space of within-class scatter matrix is required.
![img-0.jpeg](img-0.jpeg)

Figure 1.Accuracy rate with the different number of eigenvectors in full space of $S_{W}$, when the eigenvectors of null subspace of $S_{W}$ are all selected.

## 3. EDA + Full-space LDA

As discussed in the previous section, we need to find the subset of eigenvectors with significant discriminative information in full space of $S_{W}$. In this section a new algorithm is proposed, which adopts Estimation of Distribution Algorithms [8] and establishes the optimal subset of eigenvectors through evolutionary selection.
EDAs emerged as a new form of evolutionary computation during the last decade. The basic idea of EDAs is to build a probabilistic model from the parental distribution in the parameter space and to generate offspring individuals by sampling from the model. The use of EDA for selecting subset of features was reported to yield speed-up in time with respect to the traditional wrapper methods for feature selection [9]. Since eigenvectors of full space of $S_{W}$ are independent to each other, we adopt here the Univariate Marginal Distribution Algorithm (UMDA, [10]) to perform feature selection, which is a simple EDA based on the assumption that all variables are independent. The main scheme of the UMDA approach is shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Schematic overview of the UMDA algorithm.

### 3.1. Chromosome Representation

We use binary string to represent the composition of optimal feature subset. Each bit $g_{i}(i=1,2, \cdots, l)$ is corresponding to an eigenvector, that means: if $g_{i}=1$, the $i$ th eigenvector is selected into the optimal subset, otherwise, it is not selected. The length of chromosome is set to be $l$ according to the number of all

eigenvectors in the full space of $S_{W}$. A chromosome represents a solution of feature selection problem.

### 3.2. Fitness Function

Fitness function plays a crucial role in choosing offspring for the next generation from the current generation. It guides the direction of the evolution. In this paper, the fitness function is defined as Eq.(9):

$$
\text { fitness }=\mu F(R)+\lambda F_{\text {range }}(G)+F_{\text {sull }}(G)
$$

Where $\mathrm{F}(\mathrm{R})$ is the performance accuracy term in tuning set, $F_{\text {range }}(G)$ and $F_{\text {null }}(G)$ are the generalization terms which aim to select eigenvectors that have better generalization at the testing set. Here $F_{\text {range }}(G)$ and $F_{\text {null }}(G)$ are defined as Eq.(10) and Eq.(11):

$$
\begin{aligned}
& F_{\text {range }}(G)=\min \left(D_{r b}\right) / \max \left(D_{r W}\right) \\
& F_{\text {null }}(G)=\min \left(D_{r b}\right) / \max \left(D_{r W}\right)
\end{aligned}
$$

Where $D_{r b}$ and $D_{r w}$ are the distance of betweenclass and within-class in the range subspace of $S_{W}$, respectively. $D_{s l b}$ and $D_{n w}$ are the distance of between-class and within-class in the null subspace of $S_{W}$, respectively.

Weight $\mu$ and $\lambda$ are empirically chosen to represent contribution of three terms to the fitness. By combining those two terms together(with proper weight $\mu$ and $\lambda$ ), EDA can evolve balanced results displaying good performance on both turning and testing set.

### 3.3. EDA+ Full space LDA

The EDA+ Full-space LDA algorithm can be described as follows:
i. A m-dimensional PCA subspace is constructed first, and all samples are mapped into this subspace, calculate the within-class and between-class scatter matrices $S_{w}^{\prime}$ and $S_{b}^{\prime}$ :
ii. Calculate the eigenvector matrix $P=\left(\alpha_{1}, \alpha_{2}, \cdots, \alpha_{q}, \alpha_{q+1}, \cdots \alpha_{m}\right)$ of $S_{w}^{\prime}$. Suppose the first q eigenvectors of $S_{w}^{\prime}$ correspond to its non-zeros eigenvalues. UMDA is performed to pursuit a subset of eigenvectors with
significant discriminant information in full space of within-class scatter matrix on tuning set.
Step 1 A projection matrix $P_{1}$ is formed by the eigenvectors selected by the UMDA in the range subspace of $S_{w}^{\prime}$ . Define $\hat{S}_{k}=P_{1}^{T} S_{k}^{\prime} P_{1}$ and $\hat{S}_{w}=P_{1}^{T} S_{w}^{\prime} P_{1}$, the transformation matrix $U_{1}$ is then constructed by the eigenvectors corresponding to the largest eigenvalues of $\hat{S}_{k} / \hat{S}_{k}$. The first set of discriminant vectors are given by $W_{1}=U_{1} P_{1}$.
Step 2 A second projection matrix $P_{2}$ is formed by the eigenvectors selected by the UMDA in the null subspace of $S_{w}^{\prime}$. Define $\widetilde{S}_{k}=P_{2}^{T} S_{k}^{\prime} P_{2}$, the transformation matrix $U_{2}$ is then constructed by the eigenvectors corresponding to the largest eigenvalues of $\widetilde{S}_{k}^{\prime}=P_{2}^{T} S_{k}^{\prime} P_{2}$. The second set of discriminant vectors are given by $W_{2}=U_{2} P_{2}$.
Step 3 Fuse the two kinds of features given by W1 and W2 using normalizeddistance for classification.
Step 4 Calculate fitness function on tuning set; select a number of individuals; estimate probability model; generate the new population by sampling the estimated model.
An iterative procedure repeating step 1,2,3 and 4 is carried out until a termination criterion is met.
iii Let $W_{o p t 1}^{T}=W_{1}^{T} W_{p r a}^{T}$ and $W_{o p t 2}^{T}=W_{2}^{T} W_{p r a}^{T}$. Then $W_{o p t 1}^{T}$ and $W_{o p t 2}^{T}$ are the optimal projections of EDA+Full-space LDA

## 4. Experimental results

In this section, we apply our method to face recognition and compare it with the existing variant LDA methods such as Fisherface, NLDA, DLDA and Full-space LDA approaches.

The proposed method is tested on ORL face database, which contains 40 people, each person has 10 different images. The images of the same person are taken at different times, under slightly varying lighting conditions and with various facial expressions. The

images in the database are grayscale and the size are rescaled to be $92 \times 112$. Figure 3 show ten images of one person in ORL.
![img-2.jpeg](img-2.jpeg)

Figure 3. Ten images of one person in ORL face database

In this experiment, the ORL face database is broken into three disjoint sets: training, tuning and testing. The tuning set is used to provide tuning feedback to the UMDA, to select a subset of eigenvectors with significant discriminant information in full space of within-class scatter matrix by UMDA, as described previously in section 3.2. Once the UMDA run was finished(the optimal subset of eigenvectors are selected), the test set was used to perform unbiased testing on the subset found by UMDA. For every person, we use the first three images for training, the 4,5 images for turning and the remaining five for testing. A 1-NN(Nearest Neighbor) classifier is adopted. The parameters of UMDA used in this experiment are set as follows: population size is 500 ; the maximum number of generation is 30 ; the number of the selected promising solution is 200.The recognition results are shown in table 1.

Table 1. Comparison of recognition result with Fisherface, DLDA, NLDA, Full-space LDA and proposed method

| Method | Number <br> of <br> features | Recognition performance |  |
| :-- | :--: | :--: | :--: |
|  |  |  |  |
|  | 39 | 0.875 | 0.815 |
| NLDA | 39 | 0.9 | 0.835 |
| DLDA | 39 | 0.8875 | 0.795 |
| Full-space LDA | 78 | 0.9125 | 0.85 |
| EDA+Full-space | 59 | 0.9875 | 0.955 |
| LDA |  |  |  |

Table 1 shows the comparative tuning and testing performance of Fisherface, DLDA, NLDA, Full-space LDA and EDA+Full-space LDA. One can see that EDA+Full-space LDA outperforms the other LDA methods. The optimal number of eigenvectors be selected in the range and null subspace of $S_{W}$ is presented in Table 2.

Table 2. Comparison of number of eigenvectors in ranger and null subspace of $S_{W}$ with Full-space LDA and proposed method

| Method | Number <br> eigenvectors <br> ranger subspace | of Number <br> eigenvector <br> null subspace | of <br> in <br> in <br> null subspace |
| :-- | :--: | :--: | :--: |
| Full-space LDA | 80 | 39 |  |
| EDA+Full-space | 35 | 24 |  |
| LDA |  |  |  |

![img-3.jpeg](img-3.jpeg)

Figure 4. (a)Cumulative accuracy rates and (b)Rank-1 accuracy rates with the different number of features of Full-space LDA and EDA+Full-space LDA on ORL face database

From Fig.4(a) , by comparing the accuracy with Full-space LDA, the effectiveness of EDA+Full-space LDA can be seen. By employing the EDA to select eigenvectors in the full subspace of $S_{W}$, EDA+Fullspace LDA can increase the accuracy rate from $85 \%$ to $95.5 \%$ at rank 1. Fig.4.(b) show Rank-1 accuracy rates with the different number of features. It can be seen that the recognition rate is close before the null subspace eigenvectors are utilized. It indicates that the recognition rate of the proposed method does not decrease even though the number of eigenvectors of $S_{W}$ is less than the number of Full-space LDA. After

the eigenvectors in null-space are considered, the accuracy rate of EDA+Full-space LDA increases obviously.

## 5. Conclusions

In this paper, a EDA+full-space LDA approach for the eigenvectors selection in the full space of $S_{w}$ is proposed. EDA is used to pursuit a subset of eigenvectors with significant discriminative information. EDA+Full-space LDA is tested on ORL face image database. Experimental results demonstrate that our method is better than others LDA methods. In future research, we will investigate other more effective definition of fitness function for feature selection.

## Acknowledgement

The work is partially supported by the Natural Science Foundation of China(NSFC) under grand No. 60401015 and No. 60518002, the Natural Science Foundation of Anhui province under grand No. 050420201, and the Science Research Fund of MOEMicrosoft Key Laboratory of Multimedia Computing and Communication under grant No. 05071811.

## References

[1] K. Fukunaga: Introduction to statistical pattern recognition, Academic Press, Boston, 2nd edition, 1990.
[2] H. Yu and J. Yang: A direct lda algorithm for highdimensional data with application to face recognition. Pattern Recognition, 2001.
[3] L. Chen, H. Liao, M. Ko, J. Lin, and G. Yu.:A new ldabased face recognition system which can solve the samll sample size problem. Pattern Recognition, 2000.
[4] J. Yang and J.Yang : Optimal FLD algorithm for facial feature extraction, SPIE Proceedings of the Intelligent Robots and Computer Vision XX: Algorithms,Techniques, and Active Vision, vol. 4572, pp. 438-444, 2001.
[5] X.Wang and X.Tang: Dual-space linear discrminant analysis for face recognition, Proceeding of CVPR'04, vol.2.pp.564-569, 2004.
[6] P.N. Belhumeur, J. Hespanha, and D.J. Kriegman.: Eigenfaces vs. fisherfaces: Recognition using class specific linear projection. IEEE Trans. on PAMI, 19(7):711-720, 1997.
[7] Thomaz, C.E and Gillies, D.F.: A Maximum Uncertainty LDA-Based Approach for Limited Sample Size Problems With Application to Face Recognition. Computer Graphics and Image Processing, 2005. SIBGRAPI 2005 Page(s):89-96
[8] Larrañaga P, Lozano JA: Estimation of Distribution Algorithms. A New Tool for Evolutionary Computation. Kluwer Academic Publishers; 2001.
[9] Saeys Y, Degroeve S, Aeyels D, Van de Peer Y, Rouzé P: Fast feature selection using a simple Estimation of Distribution Algorithm: A case study on splice site prediction. Bioinformatics 2003, 19(Suppl 2):II179-II188.
[10] Muhlenbein H: The equation for response to selection and its use for prediction. Evol Comput 1997, 5:303-346.