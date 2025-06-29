# Multisource Heterogeneous User-Generated Contents-Driven Interactive Estimation of Distribution Algorithms for Personalized Search 

Lin Bao ${ }^{\circledR}$, Xiaoyan Sun ${ }^{\circledR}$, Member, IEEE, Dunwei Gong ${ }^{\circledR}$, Member, IEEE, and Yong Zhang ${ }^{\circledR}$, Member, IEEE


#### Abstract

Personalized search is essentially a complex qualitative optimization problem, and interactive evolutionary algorithms (EAs) have been extended from EAs to adapt to solving it. However, the multisource user-generated contents (UGCs) in the personalized services have not been concerned on in the adaptation. Accordingly, we here present an enhanced restricted Boltzmann machine (RBM)-driven interactive estimation of distribution algorithms (IEDAs) with multisource heterogeneous data from the viewpoint of effectively extracting users' preferences and requirements from UGCs to strengthen the performance of IEDA for personalized search. The multisource heterogeneous UGCs, including users' ratings and reviews, items' category tags, social networks, and other available information, are sufficiently collected and represented to construct an RBMbased model to extract users' comprehensive preferences. With this RBM, the probability model for conducting the reproduction operator of estimation of distribution algorithms (EDAs) and the surrogate for quantitatively evaluating an individual (item) fitness are further developed to enhance the EDA-based personalized search. The UGCs-driven IEDA is applied to various publicly released Amazon datasets, e.g., recommendation of Digital Music, Apps for Android, Movies, and TV, to experimentally demonstrate its performance in efficiently improving the IEDA in personalized search with less interactions and higher satisfaction.


Index Terms-Estimation of distribution algorithm (EDA), interactive, multisource heterogeneous user-generated contents (UGCs), personalized search, restricted Boltzmann machine (RBM).

[^0]
## I. INTRODUCTION

AVARIETY of evolutionary algorithms (EAs) has been successfully extended and adapted to solving complex industry problems instead of benchmark functions [1]-[5]. For example, interactive EAs (IEAs) by involving a user's subjective evaluations in the EA process have been successfully applied to optimize many qualitative problems, such as image processing, project planning, innovative design, filter design, and melody composition [6]-[10]. These actual optimization problems have the complex characteristics of multisource heterogeneous data, such as the description of personalized requirements, specific data representation, image information, etc. When developing EAs to optimize practical problems in industry, the fusion of domain knowledge and conversion of optimal objectives for adapting to the EA framework are the most difficult issues. For the domain knowledge, its collection, feature extraction, and representation are critical. With the represented domain knowledge, the optimal objectives may be practically derived. The EAs can be adjusted and improved by valuably fusing the domain knowledge. Therefore, the key points of studying specific EAs for practical problems lie in how to effectively represent the domain knowledge and derive the optimized objectives within the framework of EAs. Apparently, these two issues vary tremendously for different problems; here, we will focus on applying an IEA, i.e., interactive estimation of distribution algorithm (IEDAs) to solve the complex personalized search where items are described with user-generated contents (UGCs), such as ratings, reviews, tags, relationships, etc.

Personalized search has been becoming more and more important for product search in E-commerce and APPs. The target of personalized search is to find out several products satisfied by the user. The traditional method for searching satisfactory items is to rank all the corresponding products. However, the search space in the personalized search with user-generated contents now becomes super large due to the sharp increase of the products, which makes the personalized search more difficult [11]. Personalized search is essentially an optimization problem in getting solutions (items or products) mostly satisfied by the user (user's satisfaction is the objective) [12]. Different users have different preferences and


[^0]:    Manuscript received 12 June 2020; revised 6 October 2020, 18 January 2021, 12 May 2021, and 5 July 2021; accepted 24 August 2021. Date of publication 2 September 2021; date of current version 3 October 2022. This work was supported in part by the National Natural Science Foundation of China under Grant 61876184 and Grant 61473298, and in part by the Key Program of National Natural Science Foundation of China under Grant 62133015. (Corresponding author: Xiaoyan Sun.)
    Lin Bao is with the School of Electronics and Information, Jiangsu University of Science and Technology, Zhenjiang 212100, China, and also with the School of Information and Control Engineering, China University of Mining and Technology, Xuzhou 221116, China.
    Xiaoyan Sun, Dunwei Gong, and Yong Zhang are with the School of Information and Control Engineering, China University of Mining and Technology, Xuzhou 221116, China (e-mail: xysun78@126.com).
    Color versions of one or more figures in this article are available at https://doi.org/10.1109/TEVC.2021.3109576.
    Digital Object Identifier 10.1109/TEVC. 2021.3109576

requirements, and their "satisfaction" objectives cannot be explicitly defined with an analytical mathematical expression [13]-[15]. Thus, traditional optimization algorithms and EAs cannot be applied to efficiently solve the personalized search. IEAs [16], [17], incorporating the user interactions into EAs to provide evaluations or preference information, are more suitable for the personalized search with user-generated contents [12], [18].
Along with the rapid development on smart terminals, social APPs, and platforms, users are encouraged to actively provide as much as possible information to the platforms. These data are termed as UGCs. UGCs [19]-[21] come from many users with heterogeneous data, including users' ratings, category tags, text reviews, pictures or videos, social relationships, etc. These multisource heterogeneous UGCs comprehensively reflect users' preferences and interests on the searched items. Clearly, they are valuable for the Apps keepers to perform accurate recommendation and beneficial to the personalized search. However, such domain knowledge has not been sufficiently excavated in the IEA-based personalized search approaches due to the difficulty in representing and fusing the multisource heterogeneous UGCs under the IEA's framework.
Motivated by this, an IEDA is designed here to optimize the personalized search by effectively fusing the domain knowledge extracted from UGCs. Two issues as domain knowledge representation and optimal objective construction must be addressed when applying IEDA to handle the personalized search with UGCs. Some primary studies have been implemented. Chen et al. [12] considered the historical searching behaviors and the length of the interaction time to combine a Bayesian model with a radial basis function neural network to extract the user's preferences and represent the ranks of a searched laptop and proposed an IEDA using domain knowledge for personalized search. They further integrated the language information of the personalized search and presented a doc2vec-based preference surrogate to obtain the distributions of preferred features [22]. Lv et al. [8] constructed user's cognitive surrogate model based on the BP neural network to present a fitness estimation strategy and proposed an interactive genetic algorithm with individual fuzzy interval fitness based on the error backpropagation neural network user cognitive surrogate model to design complex innovative patterns. Fukumoto and Hanada [10] divided user's evaluation tasks into multiple days to present continuous evaluation-based interactive evolutionary computation (IEC) for composing melody. Bao et al. [18] adopted a binary feature chromosome to represent a searched item by considering which features of the item are involved, and constructed a restricted Boltzmann machine (RBM)based preference surrogate from the domain knowledge or the searching interactions and derived the probability model of preferable features to drive the estimation of distribution algorithm (EDA) in the personalized evolutionary search. In these studies, only the domain knowledge as simple features or the tags of searched items are involved. Contents of UGCs have not been well integrated in these algorithms.

For developing IEDA to the personalized search with UGCs, the great challenge is to effectively construct the preference surrogate with multisource heterogeneous data to successfully drive the EDA for evolution. Some research in obtaining the user interest model in personalized recommendation can be a great benefit for our study. Many outstanding models, such as the Bayesian model [23], [24], multilayer perceptron (MLP) [25], [26], RBM [27], [28], autoencoder (AE) [29], [30], convolutional neural network (CNN) [31], [32], and recurrent neural network (RNN) [33], [34], have been widely developed and applied. In recent years, more studies have been conducted to capture users interests from partial of UGCs, e.g., images or video information, items text descriptions, users' portrait, and users' comments, and have achieved better preference prediction and recommendation effects than traditional models. Wang et al. [24] presented a collaborative deep learning with collaborative filtering (CF) for the ratings matrix and content information. Covington et al. [25] utilized deep learning to construct a deep candidate generation model and a separate deep ranking model for YouTube recommendation. Nguyen and Lauw [28] incorporated social network into RBM-based models to learn the latent representations of the user preferences from uses' behaviors. Kim et al. [31] proposed a context-aware recommendation model, convolutional matrix factorization (ConvMF) that integrates CNN into probabilistic matrix factorization to capture the contextual information of documents for enhancing the prediction accuracy. Zheng et al. [32] presented a deep cooperative neural networks (DeepCoNNs) to learn the latent representations of user behaviors and item properties for recommendation, which consists of two parallel CNNs coupled in the last layers for the rating prediction and item recommendation. These models have not been well integrated with IEAs to evolutionarily optimize the personalized search and efficiently find out the required items.

Lower computation cost and powerful knowledge extraction in constructing users preference surrogate are more important for personalized search with UGCs due to timely interaction requirements and lack of preference related labels. RBM is a good choice in comparing with supervised learning-based models (need labels) and deep learning ones (higher computation cost). Besides, in our previous IEDA with RBM research [18], the better performance of RBM in representing and tracking users preference by only using category tags has been illustrated. As we have stated in work [18], RBM-based preference surrogate can not only construct a computable preference fitness by using its energy function but also obtain a probability distribution model of the searched item features preferred by the user in the visible layer. Such a probability model is greatly benefit in guiding the user efficiently find the satisfied items and should be sufficiently combined with the evolutionary search. As is well known, EDA is just an evolutionary scheme driven by a well-designed probability model, and it is naturally selected here as an evolutionary search tool. In such a combination, the energy function of RBM-based surrogate is calculated to get the fitness of each individual for the selection operator. The probability model of the visible layer is

collected as that of the EDA sampling operator. With the RBM surrogate-based EDA, items more preferred by the user can be accurately and rapidly searched. Accordingly, we present an IEDA to solve the personalized search with multisource heterogeneous UGCs (denoted as IEDA-MsH) by effectively fusing the domain knowledge with RBM.
RBM here is to construct a user's preference surrogate from the multisource heterogeneous UGCs, including users ratings, text comments, items category tags, and social relationship, which has seldom concerned in the RBM-based studies. Three particular problems must be focused: 1) representation of these heterogeneous input data for the RBM: the text comments are represented by using the doc2vec model, and the category tags are conveyed into a binary feature vector. These domain knowledge are fed to the RBM as training data to construct a user preference model by extracting the continuous semantic features of user comments and the discrete category features of items; 2) the structure of the RBM for dealing with different kinds of UGCs: an RBM with two visible layers is designed to separately deal with the discrete binary input and continuous semantic variables, which are different from existing RBM models; 3) effective usage on the energy function and probability model of the RBM for improving the EDA: the users' rating and social relationship will be combined with the RBM energy function since they are related with the users' preference. As for the probability model of EDA for reproduction, items in the personalized search are mainly determined by categories; therefore, only the reproduction probability of the category features is constructed and updated for an item.
The main contributions of our work are as follows.

1) Domain knowledge from multisource heterogeneous UGCs are collected to design an interactive EDA to effectively solve the personalized search.
2) The RBM trained with multisource heterogeneous UGCs is developed to represent the user preference, which has not been studied in EAs or in personalized search.
3) A more accurate and reliable surrogate model based on the RBM is subtly designed as the fitness function of EDA by incorporating the social knowledge and the energy function of the trained RBM.
The remainder of this article is organized as follows. Section II introduces the related work and notations of our study. In Section III, the proposed algorithm is described in detail. Section IV presents the comparative experiments and corresponding analysis. Finally, the conclusion is drawn in Section VI.

## II. Related Work

## A. Domain Knowledge-Based EAs

Various improved EAs have been deeply studied and experimentally validated through benchmark functions. However, they are difficult to be directly applied to optimize practical problems due to specific domain knowledge, descriptions, and constraints. When applying EAs in practice, the greatest challenge is to mathematically construct the optimized objectives together with constraints according to the domain knowledge. The domain knowledge-based EAs can be
summarized into three categories, i.e., knowledge-driven EA's operators, knowledge-embedded representation of evolving individuals, and knowledge-based surrogate as evolutionary objectives.

The operators of EAs are adaptively developed by fusing the domain knowledge. Wang et al. [35] developed a two-stage multiobjective EA (MOEA) for a multiobjective multidepot vehicle routing problem with time windows. Zuowen et al. [36] developed the dynamic repulsion technique to remedy the drawback of the repulsion techniques with static radius and presented a general framework based on the dynamic repulsion technique and EAs to effectively solve nonlinear equations system. Zhang et al. [37] proposed a network reduction-based MOEA for the community detection in large-scale complex networks, in which suggests a network reduction strategy based on the local communities found by the elite individuals and a local community repairing strategy to correct some misidentified nodes after each reduction of the network.

Individuals can be effectively represented if domain knowledge is incorporated. Yan et al. [38] presented a graph-based representation of individuals combined with estimated fuzzy assignment values and presented a graph-based fuzzy EA based on satellite-to-customer assignment to seek robust solutions for solving the two-echelon vehicle routing problem. Compared with applying EAs to solve the problems described with mathematical equations, IEAs are more complex. The representations of the searched individuals and objectives are more difficult due to the involvement of users. In IEAs, the phenotypes displayed to a user for evaluation can be photos, graphs, design schemes or styles, and productions or items described with texts or videos [39]-[42]. Such phenotypes possessing more complicated domain knowledge are quite different from that of EAs. Hao et al. [39] used the indices of each part of a dress graph to encode clothes to be designed for the fashion design problem. Pei and Takagi [40] proposed a triple comparison-based interactive differential evolution by memetic search from a local fitness landscape obtained by the comparison of target and trail vectors. The individual (either target vector or trail vector) with better fitness expresses a potential promising search region. Chen et al. [12] utilized a binary feature chromosome to represent a searched laptop in the personality search. Clearly, these representations only use partial domain knowledge to encode the phenotype and even may be cause sparse or infeasibility in the search space.

As for the domain knowledge-based surrogates in EAs, Pan et al. [43] gave a classification-based surrogate-assisted EA for solving expensive many-objective optimization problems, which predicts the dominance relationship between candidate solutions and reference solutions. In IEAs, the construction of surrogate-based objective is always the core problem since the optimized targets are more subjective, personalized, and changeable. Accordingly, the objectives are difficult to be expressed with an accurate mathematical function. Surrogate objectives established with machine learning methods based on the domain knowledge is the main solution for the qualitative optimization problems. Funaki et al. [44] adopted paired comparison-based interactive differential evolution to extract the user evaluation

criteria through a smaller number of evaluation steps for the estimation of influence of each variable on users evaluation in IEA. Bontrager et al. [6] combined generative adversarial networks (GANs) with IEC to present a deep interactive evolution for evolving images, in which a GAN trained on a specific target domain can act as a compact and robust genotype-tophenotype mapping. Bao et al. [18] constructed RBM-based surrogate to extract the user preferences by considering the distributions of the preferred attributes. Guo et al. [45] built a fitness prediction method based on gray support vector regression and four comparative measures of set-based individual evolution and proposed a set-based IEC with forecasting fitness. In summary, the collection and extraction of the domain knowledge together with the design of machine learning-based surrogate are the most important contents in surrogate-assisted IEAs.

## B. Personalized Search by Incorporating Multisource Heterogeneous UGCs

Many recommendation systems or personalized search methods have utilized a part of UGCs in building the user interest model or searching the satisfied items. Cremonesi et al. [46] and Guo et al. [47] made full use of users' rating data for recommendation, but the sparsity of those ratings severely restricts the performance of these algorithms. To address these problems, researchers attempt to take use of the available auxiliary information, such as users reviews, items' descriptions, social relationships, images, etc., to further improve the performance of recommendation algorithms [26], [32], [48]-[52]. Qiu et al. [48] proposed a Bayesian personalized ranking method for heterogeneous implicit feedback to enhance the recommendation performance. Li et al. [49] presented a review-driven neural sequence recommendation model by considering users intrinsic preferences (long-term) and sequential patterns (shortterm). Wei et al. [50] exploited user-item interactions to guide the representation learning in each modality, and designed a multimodal graph convolution network framework to yield the modal-specific representations of users and items for personalized micro-video recommendations. Jin et al. [51] proposed an efficient end-to-end neighborhood-based interaction model in the heterogeneous information network-based recommendations, which captures the interactive patterns between each pair of nodes through their metapath-guided neighborhoods. Hu et al. [52] modeled the user-news interactions as a bipartite graph by encoding the high-order relationships into user and news representations and presented a graph neural news recommendation model with unsupervised preference disentanglement for personalized news recommendation. The successful applications of these methods show that multisource heterogeneous data are beneficial to the performance of recommendation system and personalized search. These studies, however, did not regard the personalized search or recommendation as an optimization problem from the perspective of an evolutionary optimization to use EAs to improve the search efficiency and recommendation results.

## C. Applications of Restricted Boltzmann Machine

RBM is an unsupervised random neural network model with a two-layer network structure, symmetrical connections, and no self-feedback [53], [54]. It has a visible layer with visible units to input the observed data and a hidden layer with hidden units to extract the features of the input data. In 2002, Hinton [55] designed a fast learning algorithm for RBM, namely, the contrastive divergence (CD) algorithm, which greatly improves the learning efficiency of RBM.

RBM has boosted many applications. Salakhutdinov et al. [56] first used RBM to model users ratings of movies, and presented an efficient learning and inference procedures of this model for movie recommendation. Ji et al. [57] developed a sparse RBM model to learn sparser and more discriminative representations for better classification performance. Feng and Chen [58] utilized the crisp possibilistic mean value of a fuzzy number to attain the expression of the defuzzified free energy function to present a fuzzy RBM learning algorithm for better learning accuracy and generalization capacity. Bao et al. [59] presented an RBM-assisted EDA to effectively solve computationally expensive optimization problems with discrete variables. Hazrati et al. [60] used RBM to map system entities into dense feature spaces and designed a model-based pairwise collaborative ranking algorithm for the recommendations based on pairwise preference data. Due to the powerful representation learning and feature extraction abilities, RBM can produce effective learning representations even when handling sparse data. Compared with the deep neural network (DNN)-based approaches, the RBM-based methods have better performance with shorter training time to adapt to a dynamical scenario for complex personality search environment. Therefore, it is a feasible approach to use the RBM-based algorithm to obtain users preferences for the personalized evolutionary search in the big data environment.

## III. NOTATION AND FRAMEWORK

We devote to adapting interactive EDA to personalized search whose items are described with multisource heterogeneous UGCs, and first address the notation of such personalized search from the viewpoint of evolutionary optimization. The framework of our algorithm is then stated in detail. The mathematical notations in this article are summarized in Table I.

## A. Definition of UGCs-Described Personalized Search

Personalized search with a large amount of UGCs is essentially a complex optimization problem with qualitative indicators, and here is formally described as follows:

$$
\left\{\begin{array}{l}
f_{u}(\mathbf{x}) \\
\text { s.t. } \quad u \in U, \quad \mathbf{x} \in X
\end{array}\right.
$$

where $U=\left\{u_{1}, u_{2}, \ldots, u_{|U|}\right\}$ is the user set with $|U|$ number of involved users; $X=\left\{\mathbf{x}_{1}, \mathbf{x}_{2}, \ldots, \mathbf{x}_{|X|}\right\}$ is the search space with total $|X|$ number of items; and an item (solution) $\mathbf{x}_{i}$ is described with UGCs, such as items category tags and user comments. $f_{u}(\mathbf{x})$ indicates the preference or interest of user $u$

TABLE I
Notations of the Symbols

| Symbol | Definition and Description |
| :--: | :--: |
| $u$ | User |
| $\mathbf{x}$ | Item |
| $U$ | User set |
| $X$ | Item set |
| $\mathbf{R}$ | Rating matrix of users on items |
| $r_{i, i}$ | Rating of user $u_{i}$ on item $\mathbf{x}_{i}$ |
| $\mathbf{c}$ | Items category tags |
| $c_{i j}$ | The $j$-th category tag of item $\mathbf{x}_{i}$ |
| $\mathbf{T}$ | Sentence vectors of users comments |
| $\mathbf{t}_{i, i}$ | Sentence vector of the comment written by user $u_{i}$ on item $\mathbf{x}_{i}$ |
| $n_{1}$ | Number of the category tags in all of items |
| $n_{2}$ | Length of the sentence vectors of text comments |
| $k$ | Number of similar users |
| $\delta$ | Score threshold |
| $D_{u}$ | Dominant group of user $u$ |
| $\mathbf{C}^{u}$ | Matrix of category features of user $u$ |
| $\mathbf{c}^{u}$ | Vector of the category features of item $\mathbf{x}_{i}$ in $D_{u}$ |
| $\mathbf{T}^{u}$ | Matrix of the sentence vectors of comments in $D_{u}$ |
| $\mathbf{t}_{i}^{u}$ | Sentence vector of the comment of user $u$ on item $\mathbf{x}_{i}$ |
| $G$ | Training dataset |
| $\mathbf{v}_{1}$ | The first visible layer in RBM |
| $\mathbf{v}_{2}$ | The second visible layer in RBM |
| $\mathbf{h}$ | The hidden layer in RBM |
| $m$ | Number of hidden units in RBM |
| $\mathbf{V}^{u}$ | Vector matrix of all of the features in RBM |
| $P o p$ | Population in IEDA |
| $S^{u}$ | Feasible item set |
| $\alpha$ | Adjustment coefficient |

on item $\mathbf{x}$ and is determined by the users subjective, fuzzy, and inconsistent cognitive experience or interest preference, which cannot be accurately expressed with a specific mathematical function. Apparently, the personalized problem stated in (1) is completely different from those traditional problems solved by EAs w.r.t. the optimized objective and variables.

The domain knowledge-based representations of the optimized objective $f_{u}(\mathbf{x})$ and variable $\mathbf{x}$ must be concerned on to effectively design EAs to conduct the personalized evolutionary search. The UGCs used to describe the variable $\mathbf{x}$ are first collected and then vectorized to mathematically encode $\mathbf{x}$. The preferences included in the UGCs are then extracted with the RBM model to obtain $f_{u}(\mathbf{x})$. In our task, the personalized evolutionary search is to develop an IEDA to explore a TopN item list whose items are most interested by the current user, i.e., $N$ items with higher $f_{u}(\mathbf{x})$.

## B. Framework of IEDA-MsH

The framework of the proposed IEDA-MsH for effective personalized search is illustrated in Fig. 1.

The proposed algorithm has the following four crucial problems.

1) Preprocessing of multisource heterogeneous UGCs, including data collection and corresponding vectorization representations. Here, the users ratings, category tags, text comments about items, and social relationships are concerned on.
2) Building an RBM-based user preference model by integrating multisource heterogeneous UGCs.
3) Design and implementation of IEDA for personalized search according to the RBM preference model,

## Algorithm 1 Pseudocode of IEDA-MsH

Input: UGCs and the current user $u$
Output: TopN item recommendation list for user $u$

1: Initialization: Multisource heterogeneous UGCs are collected. The dominant group $D_{u}$ is formed based on the historical behaviors of user $u$ in UGCs.
2: Representation of Multisource Heterogeneous UGCs: A doc2vec model is trained by the corpus of users' comments. The category features $\mathbf{C}^{u}$ and the comment representation $\mathbf{T}^{u}$ are formed to build the training dataset G. $k$ similar users of user $u$ are selected by the Pearson correlation.
3: while Termination conditions are not met do
4: Enhanced RBM User Preference Model: The enhanced RBM user preference model is obtained to extract the preferences of user $u$.
5: Probability Model: A RBM-based probability model $P_{u}(\mathbf{x})$ is presented to generate new items with the user preferences to form $S^{u}$ itemset.
6: Surrogate Model: Considering social knowledge, a surrogate model $\hat{f}_{u}(\mathbf{x})$ is designed to estimate the individual fitness in $S^{u}$. An item list TopN is generated by the elitist selection strategy.
7: Interactive Evaluations: The TopN list is submitted to user $u$ for interactive evaluations. Then, $D_{u}$ is updated along with new UGCs.
8: end while
9: Model Management: The accuracy of the algorithm is evaluated. If it meets the requirements, keep these models. Otherwise, update the RBM user preference model and other models.
especially the construction of the probability and surrogate models used by reproduction and selection strategies.
4) A global model management mechanism to guarantee the effectiveness of the RBM-based models in the personalized search. The specific implementations of our algorithm are given in Algorithm 1.

## IV. IMPLEMENTATION OF IEDA-MSH

## A. Representation of Multisource Heterogeneous UGCs Described Items

Multisource heterogeneous UGCs are collected and represented, and the items are described with three kinds of UGCs in our algorithm: 1) users' historical interaction behaviors, e.g., users' ratings and text comments on items; 2) items' contents, such as items' category tags; and 3) social relationships between users. The category tags and text comments are used to represent the genotype of an item in the search space. The users' ratings and social relationships will serve for the fitness surrogate by integrating with the RBM preference model.

Category Tags: Items' category tags describe specific content information and to some extent reflect users' preference features. Supposing an item $\mathbf{x}_{i}$ with $n_{1}$ category tags,

![img-0.jpeg](img-0.jpeg)

Fig. 1. Framework of our IEDA-MsH.
it is embedded as $\mathbf{c}_{i}=\left\{c_{i 1}, c_{i 2}, \ldots, c_{i n_{1}}\right\}$ with $0-1$ code. If $c_{i j}=1$, then $\mathbf{x}_{i}$ has the $j$ th category tag; and vice versa. The category tags will be used as part of genotype of the individual (item $\mathbf{x}_{i}$ ).

Text Comments: Users express their preferences by the sentimental attitude and semantic meaning of text comments. These text comments are vectorized with the doc2vec [61] model by using the collected comments of UGCs. The doc2vec is an unsupervised paragraph vector model that learns fixedlength feature representations from variable-length pieces of texts, such as sentences, paragraphs, and documents. The structure of the doc2vec model is shown in Fig. 2. It can represent each document by a dense vector, which is trained to predict words in the document. The representation vectors $\mathbf{t}=\left\{t_{1}, t_{2}, \ldots, t_{n_{2}}\right\}$ of the trained doc2vec can express the latent semantic features of those comments. The representation
![img-1.jpeg](img-1.jpeg)

Fig. 2. Framework of the doc2vec model.
vector $\mathbf{t}_{i}=\left\{t_{i 1}, t_{i 2}, \ldots, t_{i n_{2}}\right\}$ of the comment of the current user on the item $\mathbf{x}_{i}$ is regard as the other part of genotype of individual (item $\mathbf{x}_{i}$ ).

Ratings: Users' ratings explicitly present users' preferences for items, and are expressed as a matrix $\mathbf{R}=\left[r_{i j}\right]_{|U| \times|X|}$. A larger value $r_{i j}$ indicates higher interest of user $u_{i}$ on item $\mathbf{x}_{j}$.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Enhanced RBM user preference model.

The rating matrix will be used to provide a reference criterion for selecting a dominant group and similar users in our algorithm.

Social Relationships: Similar users usually have similar interest preferences in the social network. Therefore, the preference information of similar users can be used to improve the performance of personalized search.

## B. UGCs Enhanced RBM Preference Model

By considering users' ratings, text comments, items' category tags, and social relationship in UGCs, an enhanced RBM model with multisource heterogeneous data is constructed to extract the user preference features for personalized search. The preprocessing of training dataset and the construction of the RBM model are mainly concerned on here.

According to the current user's query, the evaluated items with higher ratings than a score threshold $\delta$ will be first filtered by the rating matrix $\mathbf{R}$. These items mostly preferred by the user $u$ are termed as a dominant group $D_{u}\left(D_{u} \in X\right)$ with its size being $\left|D_{u}\right|$, and are used as the initial population. Then, these individuals in $D_{u}$ take full advantage of their category tags and text comments for the data preprocessing. They can be encoded as $\left|D_{u}\right| \times n_{1}$ category vectors $\mathbf{C}^{u}$ and $\left|D_{u}\right| \times n_{2}$ comment vectors $\mathbf{T}^{u}$

$$
\begin{array}{ll}
\mathbf{C}^{u}=\left[\mathbf{c}_{1}^{u}, \mathbf{c}_{2}^{u}, \ldots, \mathbf{c}_{\left|D_{u}\right|}^{u}\right]^{T}, & \mathbf{C}^{u} \in R^{\left|D_{u}\right| \times n_{1}} \\
\mathbf{T}^{u}=\left[\mathbf{t}_{1}^{u}, \mathbf{t}_{2}^{u}, \ldots, \mathbf{t}_{\left|D_{u}\right|}^{u}\right]^{T}, & \mathrm{~T}^{u} \in R^{\left|D_{u}\right| \times n_{2}}
\end{array}
$$

Those individuals are selected as training dataset, and the $i$ th sample is represented as $\left(u, \mathbf{x}_{i}, \mathbf{C}_{i}^{u}, \mathbf{T}_{i}^{u}\right)$ in this dataset. Then, the RBM-based user preference model is constructed and trained by such samples in the training dataset. The structure of our RBM is built as in Fig. 3 with two groups of input layers $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$ for representing the category and comment vectors, respectively.

Combining the representation vectors of the category tags and text comment, the item $\mathbf{x}_{i}$ can be mathematically represented as $\mathbf{x}_{i}=\left\{\mathbf{c}_{i}, \mathbf{t}_{i}\right\}=\left\{c_{i 1}, c_{i 2}, \ldots, c_{i n_{1}}, t_{i 1}, t_{i 2}, \ldots, t_{i n_{2}}\right\}$, where $c_{i j}, j=1,2, \ldots, n_{1}$ is a binary number and $t_{i k}, k=$ $1,2, \ldots, n_{2}$ is a real value. The representation vectors $\mathbf{C}^{u}$ and $\mathbf{T}^{u}$ of the individuals (items) in the dominant group $D_{u}$ are concatenated into $\left|D_{u}\right| \times n$ vector matrix $\mathbf{V}^{u}$ as the input of the enhanced RBM user preference model

$$
\mathbf{V}^{u}=\left[\mathbf{v}_{1}^{u}, \mathbf{v}_{2}^{u}, \ldots, \mathbf{v}_{\left|D_{u}\right|}^{u}\right]^{T}
$$

where $n=\begin{array}{lll}n_{1}+n_{2}, & \mathbf{v}_{i}^{u}= & \left\{\mathbf{c}_{i}^{u}, \mathbf{t}_{i}^{u}\right\} \quad= \\ \left.c_{i 1}, c_{i 2}, \ldots, c_{i n_{1}}, t_{i 1}, t_{i 2}, \ldots, t_{i n_{2}}\right\}\end{array}$
Accordingly, $\mathbf{v}_{1}$ in the RBM has $n_{1}$ units to express the binary encoded category features of the preferred items, and $\mathbf{v}_{2}$ in that has $n_{2}$ units to represent the real vectorized comment features. The hidden layer $\mathbf{h}$ has $m$ units and expresses the latent user preference features. Combining the category features $\mathbf{C}^{u}$ with the comment representation $\mathbf{T}^{u}$ is input the RBM to train the enhanced RBM-based user preference model, in which the preference features implied in the UGCs are fused and extracted.

Given the state of visible units, the active probability of the $j$ th hidden unit in the RBM is calculated

$$
P_{\theta}\left(h_{j}=1 \mid \mathbf{v}_{1}, \mathbf{v}_{2}\right)=\sigma\left(b_{j}+\sum_{i=1}^{n_{1}} v_{1 i} w_{i j}+\sum_{i=1}^{n_{2}} v_{2 i} w_{i j}\right)
$$

where $v_{1 i}$ and $v_{2 i}$ are the states of the $i$ th visible unit of the first and second visible layers, respectively; $h_{j}$ is the state of the $j$ th hidden unit; $w_{1 i j}$ and $w_{2 i j}$ represent the connection weights; $b_{j}$ is the bias of the $j$ th hidden unit; and $\sigma(x)=1 /(1+\exp (-x))$ is the Sigmoid active function.

Given the state of hidden units, the active probabilities of the $i$ th visible unit of two visible layers in the RBM are as follows:

$$
\begin{aligned}
& P_{\theta}\left(v_{1 i}=1 \mid \mathbf{h}\right)=\sigma\left(a_{1 i}+\sum_{j=1}^{m} w_{i j} h_{j}\right) \\
& P_{\theta}\left(v_{2 i}=1 \mid \mathbf{h}\right)=\sigma\left(a_{2 i}+\sum_{j=1}^{m} w_{i j} h_{j}\right)
\end{aligned}
$$

where $a_{1 i}$ and $a_{2 i}$ are the bias vectors of the $i$ th visible units in two visible layers, respectively.

According to the training dataset and the CD learning algorithm [57], the enhanced RBM model is trained to obtain the model parameters $\theta=\{\mathbf{w}, \mathbf{a}, \mathbf{b}\}$ with the use preference information. After training, the latent preference features of the current user for the desirable items are fetched by the hidden layer in that RBM. Meanwhile, the distributions of the preference information on the categories and comments along with the preferred features can be obtained as $P_{\theta}\left(\mathbf{v}_{1} \mid \mathbf{h}\right)$ and $P_{\theta}\left(\mathbf{v}_{2} \mid \mathbf{h}\right)$ by resampling the trained RBM model. Clearly, the enhanced RBM user preference model not only extracts the user preference features but also models the distributions of the user preferred features, which is greatly valuable for designing the evolutionary strategies of the IEDA in personalized search.

## C. RBM-Based Reproduction Probability Model of IEDA

The performance of EDA is fundamentally determined by the construction and update of its reproduction probability model. The probability model is developed here according to the trained RBM preference model in Section IV-B. The items in the personalized search are mainly determined by categories and their corresponding comments are beneficial supplements. Therefore, only the reproduction probability of the category features $\mathbf{C}^{u}$ is constructed and updated for an item $\mathbf{x}_{i}=\left\{\mathbf{c}_{i}, \mathbf{t}_{i}\right\}=\left\{c_{i 1}, c_{i 2}, \ldots, c_{i n_{1}}, t_{i 1}, t_{i 2}, \ldots, t_{i n_{2}}\right\}$. The sampling probability $\hat{p}\left(c_{i}=1 \mid \theta, \mathbf{h}\right), i=1,2, \ldots, n_{1}$ is estimated based on the feature distributions in the visible layer

and the parameters of the trained RBM [18]

$$
p\left(c_{i}=1 \mid \theta, \mathbf{h}\right)=\frac{\hat{p}\left(c_{i}=1 \mid \theta, \mathbf{h}\right)}{\sum_{i=1}^{n_{1}} \hat{p}\left(c_{i}=1 \mid \theta, \mathbf{h}\right)}
$$

where the values of $\hat{p}\left(c_{i}=1 \mid \theta, \mathbf{h}\right), i=1,2, \ldots, n_{1}$ are normalized to ensure $\sum_{i=1}^{n_{1}} p\left(c_{i}=1 \mid \theta, \mathbf{h}\right)=1$.
Then, the probability model $P_{u}(\mathbf{x})$ of EDA is shown in
$P_{u}(\mathbf{C})=\left[p\left(c_{1}=1 \mid \theta, \mathbf{h}\right), p\left(c_{2}=1 \mid \theta, \mathbf{h}\right), \ldots, p\left(c_{n_{1}}=1 \mid \theta, \mathbf{h}\right)\right]$.

In our IEDA, $P_{u}(\mathbf{C})$ is randomly sampled to generate Pop new individuals (items). According to the similarity criterion, $\left|D_{u}\right|$ items with higher estimated fitness in the search space are matched to form a feasible item set $S^{a}$ as the recommended set for the next interactions.

## D. Fitness Surrogate of IEDA With RBM and Social Group

The enhanced RBM model given in Section IV-B extracts the user preference features when the energy function of the RBM is minimized, i.e., if an item has a smaller energy value in the RBM, then it is more preferred for the current user. Therefore, the RBM energy function of the enhanced RBM user preference model can be used to measure the user preference degree on the items in the search space. On the other hand, users preferences may be also affected by public preferences or social groups in the searching process. Accordingly, we integrate social knowledge with the RBM energy function to accurately construct the evaluation model of the user preference level as the fitness surrogate of IEDA to estimate the individual fitness in the interactive evolutionary process.

For an individual $\mathbf{x}=\left[\mathbf{c}^{a}, \mathbf{t}^{a}\right]$ in the item set $S^{a}$, the energy function $E_{\theta}(\mathbf{x})$ in the RBM model with multisource heterogeneous UGCs is expressed as follows:

$$
E_{\theta}(\mathbf{x})=E_{\theta}(\mathbf{v})=-\sum_{i=1}^{n_{1}+n_{2}} \sum_{j=1}^{m} v_{i} w_{i j} h_{j}-\sum_{i=1}^{n_{1}+n_{2}} a_{i} v_{i}-\sum_{j=1}^{m} b_{j} h_{j}
$$

where $\mathbf{v}=\left[\mathbf{v}_{1}, \mathbf{v}_{2}\right]=\left[\mathbf{c}^{a}, \mathbf{t}^{a}\right]$ expresses the category vectors $\mathbf{c}^{a}$ of item $\mathbf{x}$ and the representation vectors $\mathbf{t}^{a}$ of the comments of user $u$ on item $\mathbf{x}$.

The rating $\hat{R}_{a \mathbf{x}}$ of user $u$ on item $\mathbf{x}$ is estimated based on the energy function of the enhanced RBM user preference model

$$
\hat{R}_{a \mathbf{x}}=\frac{\max \left(E_{\theta}\right)-E_{\theta}(\mathbf{x})}{\max \left(E_{\theta}\right)-\min \left(E_{\theta}\right)}
$$

where $\max \left(E_{\theta}\right)$ and $\min \left(E_{\theta}\right)$ are the maximum and minimum of the individual energy values in the EDA population, respectively.

According to the rating matrix $\mathbf{R}$, the similarity coefficient $\operatorname{sim}\left(u_{i}, u_{j}\right)$ between user $u_{i}$ and $u_{j}$ is calculated with Pearson correlation. Then, $k$ similar users with higher similarities are recognized as the social group of the current user $u$. The social contribution of these similar users is defined as in

$$
\operatorname{social}(\mathbf{x})=\sum_{j=1}^{k} \operatorname{sim}\left(u, u_{j}\right) \times R_{u_{j} \mathbf{x}}
$$

where $R_{u_{j} \mathbf{x}}$ is the rating of user $u_{j}$ on item $\mathbf{x}$.

TABLE II
\# OF USERS, ITEMS, AND RATINGS OF THE DATASETS

| Dataset | \# of Users | \# of Items | \# of Ratings |
| :--: | :--: | :--: | :--: |
| Digital_Music (Music) | 478,235 | 266,414 | 836,006 |
| Video_Games (Games) | 826,767 | 50,210 | 1,324,753 |
| Apps_for_Android (Apps) | 1,323,884 | 61,275 | 2,638,173 |
| Kindle_Store (Kindle) | 1,406,890 | 430,530 | 3,205,467 |
| CDs_and_Vinyl (CDs) | 1,578,597 | 486,360 | 3,749,004 |
| Movies_and_TV (Movies) | 2,088,620 | 200,941 | 4,607,047 |

The surrogate model $\hat{f}_{u}(\mathbf{x})$ is presented to estimate the fitness of the individual $\mathbf{x}$ by incorporating $E_{\theta}(\mathbf{x})$ and social $(\mathbf{x})$

$$
\hat{f}_{u}(\mathbf{x})=\sigma\left(\alpha \times \hat{R}_{a \mathbf{x}}+(1-\alpha) \times \operatorname{social}(\mathbf{x})\right)
$$

where $\alpha \in(0,1)$ is an adjustment coefficient.
According to the surrogate model $\hat{f}_{u}(\mathbf{x})$, the individual fitness of the feasible items set $S^{a}$ generated in Section IV-C is estimated. Then, top-N excellent individuals are generated by using the elite selection strategy to form the item recommendation list TopN. The recommendation list TopN is submitted to the current user for interactive evaluations in a round of interactive personality evolutionary search.

## E. Computational Complexity Analysis

The computational complexity of the proposed algorithm is determined by training a doc2vec model, calculating social relationships, training an enhanced RBM user preference model, and filtering feasible solutions. Among them, the doc2vec model and social relationships can be both completed offline. The computational cost of training the RBM model integrating multisource heterogeneous UGCs is $O\left(\left|D_{u}\right| \times\left(n_{1}+n_{2}\right) \times m\right)$. The time consumption of selecting $S^{a}$ candidate solutions is $O\left(S^{a} \times D\right)$, where $D$ is the number of the items in the search space. Therefore, the total computational complexity of our algorithm is $O\left(\left|D_{u}\right| \times\left(n_{1}+n_{2}\right) \times m+S^{a} \times D\right)$. It is mainly determined by the representations of categories and comments because the time cost of $O\left(S^{a} \times D\right)$ is the same by comparing with traditional search methods. Additionally, the extra computational cost of our algorithm can be ignored with appropriate $n_{1}+n_{2}$ when the size of $D$ is great large.

## V. APPLICATIONS IN AMAZON DATASETS AND EXPERIMENTAL ANALYSIS

## A. Datasets and Parameter Settings

Datasets: The proposed algorithm is verified by applying it to several typical personalized search datasets from Amazon [62], including Digital_Music, Video_Games, Apps_for_Android, Kindle_Store, CDs_and_Vinyl, and Movies_and_TV datasets. These datasets provide users' ID, items' ID, users' ratings with 1-5 integer values, items' categories, users' comments, stamp time, and other information. The statistical information of these datasets is listed in Table II.

Taking the Digital_Music dataset as an example, each item has 79 category tags and these tags are fed into the visible units of the first group RBM, that is, $n_{1}=79$ in the enhanced RBM

TABLE III
DEScriptions of COMPARED AlGORITHMS

| Algorithm | Description |
| :--: | :--: |
| Random | Non-personalized method that randomly selects items for recommendations |
| Popularity [46] | Non-personalized method in which the most popular items are recommended by items' popularity |
| BPR [23] | Bayesian personalized ranking (BPR) algorithm based on supervised learning, and the hidden factor is set to 20 |
| ConvMF [26] | Convolutional matrix factorization (ConvMF) based on CNN |
| DeepCoNN [32] | Deep Cooperative Neural Networks (DeepCoNN) based on CNN |
| RBMEDA [59] | Restricted Boltzmann Machine-assisted Estimation of Distribution Algorithm (RBMEDA), and a personalized search method based on unsupervised learning |
| RBFIEDA [12] | Radial Basis Function-assisted Interactive Estimation of Distribution Algorithm (RBFIEDA) |
| DRBMEDA [18] | Dual Restricted Boltzmann Machine-driven Estimation of Distribution Algorithm (DRBMEDA), and a personalized search method based on unsupervised learning |
| DRBMIEDA [18] | Dual Restricted Boltzmann Machine-driven Interactive Estimation of Distribution Algorithm (DRBMIEDA) |
| EGEDA [63] | Enhancing Gaussian Estimation of Distribution Algorithm |

user preference model. The vectorization representation of comments is obtained by the doc2vec model and corresponding to the visible units in the second group, that is, $n_{2}=200$ in that RBM. Therefore, the code of an individual (item) $\mathbf{x}$ is expressed as $\mathbf{v}=\left[v_{1}, v_{2}, \ldots, v_{79}, v_{79+1}, \ldots, v_{79+200}\right]$ in IEDA by concatenating the representation vectors of category tags and text comments. The size of the input $\mathbf{v}$ of the enhanced RBM user preference model is $(79+200)$.

Compared Algorithms: Several state-of-the-art algorithms are selected as comparisons: Random, Popularity [46], BPR [23], ConvMF [26], DeepCoNN [32], RBMEDA [59], RBFIEDA [12], DRBMEDA [18], and EGEDA [63]. Random and popularity are both nonpersonalized methods. Sometimes these nonpersonalized methods are better than the personalized search algorithms, so they are used as the baselines to measure the performance of other algorithms. Considering users historical ratings and text reviews, ConvMF and DeepCoNN are both the state-of-the-art recommendation algorithms based on CNN. Additionally, the same doc2vec model is pretrained to generate the vectorization representations of text comments in the algorithms that utilize users' comments. RBMEDA, RBFIEDA, DRBMEDA, and EGEDA are the state-of-the-art personalized search methods or single objective optimization algorithms. Their brief descriptions are detailed in Table III.

Evaluation Metrics: From the viewpoint of practical applications, the metrics of measuring EAs should be in accordance with the applications. Therefore, four metrics as root mean square error (RMSE), hit ratio (HR) [64], average precision (AP) [18], and mean AP (MAP) [18] often used in personalized search are used to demonstrate the prediction accuracy and recommendation performance of the proposed algorithm. RMSE measures the prediction accuracy of the algorithms. HR refers to the ratio between the number of preferred items in recommendation list and that in the test dataset to reflect the recommendation accuracy. The higher the HR value, the better the search results. AP expresses the ranking performance of the item recommendation list generated by the algorithms, and is sensitive to the position or order of the preferred items in the list. The higher the ranking of the favored items in TopN, the higher the AP. It means that the algorithm has obtained better ranking accuracy. Furthermore, MAP is the average AP of all test users and measures the overall ranking performance

TABLE IV
EXPERIMENTAL PARAMETERS OF OUR ALGORITHM

| Parameter | Value |
| :--: | :--: |
| $n_{1}$ | Number of category tags |
| $n_{2}$ | 200 |
| $m$ | $(0.8-1.2) \times$ Number of category tags |
| Learning rate | 0.1 |
| Momentum | $0.5-0.9$ |
| Training epochs in RBM | 20 |
| Pop | $0.3 \times$ Number of test |
| $k$ | 10 |
| $\alpha$ | 0.3 |
| \# of TopN list $(N)$ | 10 |

of the algorithms. In particular, it focuses on whether the items near the front of the list are the ones that users are of favorite.

Parameter Settings: After try and errors, the experimental parameters of the proposed IEDA-MsH algorithm are shown in Table IV.

Two groups of experiments are designed to investigate the feasibility, effectiveness, and accuracy of the IEDA-MsH algorithm: 1) personalized search without interaction: the effectiveness of the RBM model and surrogate by integrating multisource heterogeneous UGCs; a user is randomly selected to show the results of the personalized searching in different sparsity datasets and 2) interactive personalized search: the comprehensive performance of the proposed algorithm by comparing with other interactive personalized search algorithms. The experimental environment is a Dell computer with an Intel Core i5-4590 CPU 3.30 GHz and 4-GB RAM, and the experimental platform is developed by using Python 3.6.

## B. Performance of Personalized Search Algorithms Without Interaction

1) Effectiveness of UGCs-Driven RBM and Surrogate Model: The performance of our IEDA is basically determined by the UGCs-based RBM model since both the reproduction probability and fitness surrogate of EDA are derived from the RBM model. Accordingly, the effectiveness of the UGCsdriven RBM and surrogate model are first concerned on and analyzed.

The items with ratings, category tags, and text comments from randomly selected ten users in each dataset are collected to obtain the enhanced RBM and surrogate models.

TABLE V
Effectiveness of UGCs-Driven RBM and Surrogate by Comparing With Popular Personalized Algorithms. Root Mean Square Error: RMSE, Hit Ratio: HR, and Average Precision: AP. See Tables II and III FOR USED Abbreviations

| Algorithms |  | Random | Popularity | BPR | ConvMF | DeepCoNN | RBMEDA | DRBMEDA | $\begin{gathered} \text { RBM- } \\ \text { categ } \end{gathered}$ | RBM | $\begin{gathered} \text { ERBM } \\ \text {-MsH } \end{gathered}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Music | RMSE | - | 3.144* | $1.898 *$ | 3.130* | 2.156* | 1.218 | 1.264* | 1.258 | 1.173 | 1.123 |
|  | HR | 0.0765* | 0.0793* | 0.0764* | 0.0742* | 0.0984 | 0.0812* | 0.0924* | 0.0997 | 0.1017 | 0.0981 |
|  | MAP | 0.761* | 0.723* | 0.811* | 0.728* | 0.829* | 0.809* | 0.887 | 0.897 | 0.878 | 0.913 |
|  | Time(s) | 0.020 | 0.182 | 0.494 | 276.716 | 40.035 | 0.221 | 1.599 | 0.584 | 0.672 | 0.690 |
| Games | RMSE | - | 3.516* | $1.973 *$ | 3.497* | 1.317 | 1.321* | 1.332* | 1.305 | 1.289 | 1.226 |
|  | HR | 0.0810* | 0.0930* | 0.0753* | 0.0945* | 0.0934* | 0.0735* | 0.0815* | 0.0763 | 0.0859 | 0.1021* |
|  | MAP | 0.747* | 0.873* | 0.707* | 0.915 | 0.828* | 0.692* | 0.760* | 0.737 | 0.894 | 0.906* |
|  | Time(s) | 0.014 | 0.196 | 0.402 | 131.716 | 40.164 | 0.151 | 2.346 | 0.125 | 0.719 | 0.775 |
| Apps | RMSE | - | 3.164* | 2.146* | 3.119* | 1.414 | 1.523* | 1.543* | 1.481 | 1.496 | 1.367 |
|  | HR | 0.0799* | 0.0795* | 0.0852* | 0.0701* | 0.0948* | 0.0827* | 0.0746* | 0.0759 | 0.0807 | 0.1034 |
|  | MAP | 0.736* | 0.714* | 0.736* | 0.688* | 0.830* | 0.756* | 0.712* | 0.729 | 0.770 | 0.881 |
|  | Time(s) | 0.014 | 0.170 | 0.344 | 90.489 | 33.959 | 0.103 | 0.646 | 0.086 | 0.388 | 0.399 |
| Kindle | RMSE | - | 4.319* | 2.284* | 4.317* | 1.040* | 1.433* | 1.549* | 1.304 | 1.256 | 1.232 |
|  | HR | 0.0298* | 0.0222* | 0.0278* | 0.0221* | 0.0283* | 0.0292* | 0.0295* | 0.0303 | 0.0299 | 0.0312 |
|  | MAP | 0.914* | 0.922* | 0.857* | 0.833* | 0.857* | 0.909* | 0.867* | 0.938 | 0.915 | 0.971 |
|  | Time(s) | 0.014 | 0.761 | 1.205 | 416.532 | 103.890 | 10.060 | 26.223 | 2.501 | 7.224 | 7.351 |
| CDs | RMSE | - | 4.218* | 2.182* | 4.217* | 2.357* | 1.480* | 1.534* | 1.229 | 1.393 | 1.205 |
|  | HR | 0.0119* | 0.0136* | 0.0101* | 0.0107* | 0.0136* | 0.0110* | 0.0110* | 0.0121 | 0.0116 | 0.0124 |
|  | MAP | 0.847* | 0.825* | 0.826* | 0.817* | 0.903* | 0.837* | 0.852* | 0.838 | 0.865 | 0.976 |
|  | Time(s) | 0.016 | 3.833 | 5.406 | 884.519 | 274.451 | 5.345 | 31.382 | 6.013 | 28.111 | 30.886 |
| Movies | RMSE | - | 3.068* | 1.960* | 3.029* | 1.714* | 1.187 | 1.185 | 1.180 | 1.169 | 1.149 |
|  | HR | 0.0134* | 0.0153* | 0.0144* | 0.0183* | 0.0158* | 0.0138* | 0.0154* | 0.0144 | 0.0177 | 0.0246 |
|  | MAP | 0.668* | 0.769* | 0.702* | 0.838* | 0.763* | 0.670* | 0.766* | 0.695 | 0.749 | 0.973 |
|  | Time(s) | 0.014 | 2.186 | 3.261 | 506.125 | 211.441 | 0.465 | 9.468 | 0.464 | 1.815 | 1.902 |

The performances of these two models on approximating users preferences and executing effective search are investigated by measuring the average RMSE, HR, and MAP metrics. Some baselines and popular personalized search methods as Random, Popularity [46], BPR [23], ConvMF [26], DeepCoNN [32], RBMEDA [59], and DRBMEDA [18] are used as comparison algorithms with the enhanced RBM and surrogate models constructed with multisource heterogeneous UGCs (shorten as ERBM-MsH), i.e., ratings, items category tags, comments, and social knowledge. Additionally, three variations of our algorithm in fusing different domain knowledge are also compared in this experiment, including the RBM model built only on ratings and category tags (shorten as RBM-categ), the RBM one only uses ratings and comments (shorten as RBM-text), and the RBM one using ratings, category tags, and comments (shorten as RBM-CT). The results of these algorithms can provide an insight into the effect of different domain knowledge on constructing the RBM and surrogate models.

Ten times of experiments are conducted, and the average values of these metrics are recorded and compared in Table V. The consumed time of constructing each model is also given to directly show the computational cost of our algorithm since this process has a great effect on the interactive EDA in personalized search. See Table II for abbreviations of dataset names and Table III in Section V-B for the algorithm names, respectively. The proposed ERBM-MsH algorithm is compared with other algorithms, such as Random, Popularity, BPR, ConvMF, DeepCoNN, RBMEDA, and DRBMEDA, to conduct the Kruskal-Wallis test with Bonferroni correction test to analyze the distribution differences in the experimental results between groups. If the ERBM-MsH has a significant difference (progressive significance $p<0.05$ ) with the
comparative algorithm, then the experimental result of this comparative algorithm is marked with * in Table V. The best solution is bolded.

From Table V, we can observe the following conclusions.

1) RBM surrogate assisted with multisource heterogeneous UGCs can approximate users preferences with higher precision, demonstrating that UGCs exactly benefit the construction of users preference model in the personalized search. Meanwhile, the experimental results indicate the proposed ERBM-MsH is significantly different to other comparative algorithms in the RMSE, HR, and MAP of most cases. For example, ERBMMsH achieves a smallest value 1.149 of RMSE on the Movies dataset, improving $41.38 \%$ compared with the supervised learning BPR. However, DeepCoNN obtains the highest accuracy of score prediction for the Kindle one. The main reason may be that the features of the text comments and categories for this kind of products are relatively simpler than other datasets so that our ERBM-MsH has not taken full advantage of multisource heterogeneous information in UGCs for further improving the performance of the personalized search method.
2) The statistical analysis tests of the Kruskal-Wallis show that ERBM-MsH has higher ranking and individualized recommendation accuracy on the metrics of most datasets. Such higher performance superiority proves further that the surrogate induced from ERBM-MsH is more reliable and appropriate to predict the individual fitness in EDA for guiding the evolutionary search.
3) From the perspective of the computational cost, the unsupervised learning-based ERBM-MsH is superior to the supervised learning-based ConvMF and DeepCoNN

TABLE VI
Performance of ERBM-MsH for User "A3W4D8XOGLWUN5." See the Caftions of Table V

| Percent (\%) | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| RMSE | 0.957 | 1.051 | 1.048 | 1.066 | 1.021 | 1.018 | 1.078 | 1.071 | 1.001 |
| HR | 0.0133 (6) | 0.0194 (8) | 0.0192 (8) | 0.0249 (8) | 0.0262 (8) | 0.0409 (9) | 0.0539 (9) | 0.0729 (10) | 0.1703 (9) |
| AP | 0.654 | 0.852 | 0.909 | 0.932 | 0.947 | 0.960 | 0.989 | 1.0 | 0.987 |

![img-3.jpeg](img-3.jpeg)

Fig. 4. Personalized searching of user "A3W4D8XOGLWUN5" along with percentage of training data. (a) Root mean square error: RMSE. (b) Hit ratio: HR. (c) Average precision: AP. See Table III for abbreviations of algorithms.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Personalized searching of user A9Q28YTLYRE07 along with percentage of training data. (a) RMSE. (b) HR. (c) AP.
methods. ConvMF and DeepCoNN need expensive computation cost for dynamically approximating users preferences because they are the CNN-based recommendation algorithms with longer online training time. On the contrary, our algorithm utilizes the RBM, a shallow model, which not only has lower time cost in constructing user preference model but also has higher precision accuracy for the personalized search. Such results demonstrate that multisource heterogeneous UGCs-driven RBM and surrogate models are more suitable for the interactive personalized evolutionary search in complex environment and have better adaptability and scalability in practical applications.
2) Performance on Ranking and Spatial Sparsity: The ranking sparsity on the searched items is always a great difficulty for the personalized search [12], [18]. This is also challengeable when designing EAs to solve the search. Besides, the spatial sparsity will disable the encoding mode and evolutionary operators since many generated points are corresponding to infeasible solutions in the evolutionary searching. The performance of the developed UCGs-based IEDA in finding out satisfactory solutions with different sizes of ranking and spatial sparsity is specifically addressed here.

We randomly select two users with ID as "A3W4D8XOGLWUN5" and "A9Q28YTLYRE07" from
the Digital_Music to carry out the personalized search with different sparsity. The samples are reordered according to the user's rating time. The data in the forepart \# \% are used as the training data. The rest of the samples are regarded as the practical search space. A smaller percent of the training data means a larger ranking and spatial sparsity in the personalized search. The RMSE, HR, and AP metrics of the ERBM-MsH for the user "A3W4D8XOGLWUN5" are shown in Table VI. The detailed results for users "A3W4D8XOGLWUN5" and "A9Q28YTLYRE07" under algorithms as RBMEDA, DRBMEDA, and ERBM-MsH are shown in Figs. 4 and 5.

1) The performance of ERBM-MsH has a certain volatility but is relatively robust when the sparsity changes. The RMSE measures the approximation of the RBMbased surrogate. It increases when the training data increase from $30 \%$ to $70 \%$ and decrease when the training data increase more, which seems to conflict with the traditional machine learning. The possible reason is that more UGCs without filtering may bring noisy and deteriorate the approximation performance. Therefore, UGCs selection will be further considered in the future. But, we can also conclude that such variations of the RMSE are in a relatively smaller range, i.e., $[0.957,1.078]$, and the largest relative volatility is $(1.078-0.957) / 0.957=12.64 \%$. Such a value

TABLE VII
COMPREHENSIVE PERFORMANCE AMONG COMPARED IEAs. See TABLEs II and III AND Fig. 4 FOR Used Abbreviations

| Algorithms |  | IEDA | RBMIGA | RBFIEDA | RBMEDA | DRBMIEDA | EGEDA | IEDA-categ | IEDA-CT | IEDA-MsH |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Music | RMSE | - | 1.230 | $2.525 *$ | 1.223 | $1.439 *$ | - | 1.246 | 1.263 | 1.218 |
|  | HR | $0.0459 *$ | $0.0473 *$ | $0.0420 *$ | $0.0485 *$ | $0.0506 *$ | $0.0468 *$ | 0.0518 | 0.0573 | 0.0659 |
|  | MAP | $0.775 *$ | $0.794 *$ | $0.788 *$ | $0.826 *$ | 0.879 | $0.764 *$ | 0.853 | 0.864 | 0.881 |
| Games | RMSE | - | $1.364 *$ | $2.854 *$ | $1.361 *$ | 1.506 | - | 1.288 | 1.266 | 1.519 |
|  | HR | $0.0475 *$ | $0.0488 *$ | $0.0534 *$ | $0.0465 *$ | $0.0501 *$ | $0.0488 *$ | 0.0501 | 0.0600 | 0.0714 |
|  | MAP | $0.743 *$ | $0.737 *$ | 0.836 | $0.729 *$ | 0.823 | $0.748 *$ | 0.752 | 0.851 | 0.824 |
| Apps | RMSE | - | $1.521 *$ | $1.901 *$ | 1.525 | $1.621 *$ | - | 1.479 | 1.470 | 1.605 |
|  | HR | $0.0484 *$ | $0.0486 *$ | $0.0470 *$ | $0.0489 *$ | $0.0528 *$ | $0.0458 *$ | 0.0473 | 0.0545 | 0.0771 |
|  | MAP | $0.747 *$ | $0.742 *$ | $0.724 *$ | $0.759 *$ | $0.807 *$ | $0.694 *$ | 0.724 | 0.826 | 0.893 |
| Kindle | RMSE | - | $1.468 *$ | $4.214 *$ | $1.449 *$ | $1.731 *$ | - | 1.370 | 1.297 | 1.335 |
|  | HR | $0.0177 *$ | $0.0178 *$ | $0.0175 *$ | $0.0174 *$ | $0.0179 *$ | $0.0181 *$ | 0.0180 | 0.0175 | 0.0192 |
|  | MAP | $0.921 *$ | 0.932 | $0.923 *$ | $0.925 *$ | 0.938 | 0.939 | 0.935 | 0.921 | 0.941 |
| CDs | RMSE | - | $1.456 *$ | $3.705 *$ | $1.458 *$ | 1.659 | - | 1.448 | 1.444 | 1.747 |
|  | HR | $0.00697 *$ | $0.00683 *$ | $0.00715 *$ | $0.00718 *$ | $0.00727 *$ | $0.00652 *$ | 0.00714 | 0.00744 | 0.00832 |
|  | MAP | $0.844 *$ | $0.878 *$ | $0.849 *$ | $0.886 *$ | $0.866 *$ | $0.828 *$ | 0.876 | 0.897 | 0.998 |
| Movies | RMSE | - | 1.198 | $1.234 *$ | 1.201 | $1.333 *$ | - | 1.177 | 1.176 | 1.164 |
|  | HR | $0.00777 *$ | $0.00787 *$ | $0.00926 *$ | $0.00816 *$ | $0.00850 *$ | $0.00814 *$ | 0.00798 | 0.00881 | 0.01168 |
|  | MAP | $0.686 *$ | $0.667 *$ | $0.737 *$ | $0.675 *$ | $0.720 *$ | $0.665 *$ | 0.690 | 0.725 | 0.839 |

demonstrates that the RMSE of ERBM-MsH is robust to some extent on the approximation when the sparsity changes.
2) The HR value reflects the ratio of the preferred items in the TopN list to the total number of the preferred ones in the explored space. There are 364 items with scores larger than 4 in the search space. Top 10 items searched by ERBM-MsH are provided to the current user for recommendation, and the number in brackets indicates the number of favored items in Top 10 for the current user. It shows that this value has a smaller change from 6 to 9 when the sparsity decreases. Therefore, ERBMMsH can effectively search the favorite items of the current user for recommendation. The similar conclusion can also be drawn from the AP values, which will not be repeated any more.
The results shown in Figs. 4 and 5 are consistent with that of Table VI and provide an intuitive performance comparison of our algorithm with RBMEDA and DRBMEDA. These figures clearly present the fluctuation on the three metrics of the algorithms along with the sparsity decrease. The performance of ERBMMsH is gradually improved with the sparsity of the dataset, and the proposed algorithm is obviously better than other comparison algorithms.

In summary, the proposed ERBM-MsH has better performance for a sparse search space by taking full use of multisource heterogeneous UGCs to construct the RBMbased preference probability model and surrogate for the personalized search.

## C. Comprehensive Performance of Interactive Personalized Search Algorithms

The comprehensive performance of the proposed IEDAMsH for the personalized search in an interactive environment is sufficiently discussed here by comparing with eight IEAs, i.e., traditional IEDA (baseline), RBM-assisted interactive genetic algorithm (RBMIGA), RBFIEDA [12], RBMEDA [59], DRBMIEDA [18], EGEDA [63], RBM-categ assisted IEDA (IEDA-categ), and RBM-CT assisted IEDA (IEDA-CT). In these experiments, ten users are randomly selected to conduct the interactive personalized search, and all items of each dataset are reordered chronologically according to their evaluation timestamps. The half forepart of the items is used as the training dataset, and the remaining is regarded as the searching space in the personalized search. In addition, the forepart $20 \%$ of the training data is treated as initial historical interactions, and the last $30 \%$ of that is split into ten parts as new UGCs for each iteration. Each algorithm iterates ten generations to provide predicted scores and elitist items to the current user. The average results of ten independent runs are shown in Table VII, and the best solutions are in bold. The proposed IEDA-MsH algorithm is compared with other algorithms, such as IEDA, RBMIGA, RBFIEDA, RBMEDA, DRBMIEDA, and EGEDA, to conduct the Kruskal-Wallis test with Bonferroni correction test to analyze the distribution differences in the experimental results between groups. If IEDA-MsH has a significant difference (progressive significance $p<0.05$ ) from the compared algorithm, then the experimental result of this comparative algorithm is marked with "*" in Table VII.

Note that IEDA and EGEDA have no RMSE because these methods do not design the surrogate model for the prediction of the individual fitness in the evolutionary process. From Table VII, it can be concluded as follows.

1) The proposed IEDA-MsH achieves better results on the compared metrics for most of the used Amazon datasets. EDA-MSH is not only superior to the state-of-the-art evolutionary optimization algorithms, RBFIEDA and EGEDA, but also better than the RBMEDA and DRBMIEDA methods that use RBM as a surrogate model in the EDA framework. Meanwhile, the statistical analysis experiments indicate IEDA-MsH is significantly different to other comparative algorithms on the metrics of most cases. Such a result is reasonable. IEDA-MsH takes multisource heterogeneous UGCs into consideration to carry on the personalized search, and IEDA-CT only involves the categories and comment

![img-5.jpeg](img-5.jpeg)

Fig. 6. Personalized search in music. (a) RMSE. (b) HR. (c) AP. See captions of Fig. 4 and Table III.
![img-6.jpeg](img-6.jpeg)
(a)
![img-7.jpeg](img-7.jpeg)
(b)
![img-8.jpeg](img-8.jpeg)
(c)

Fig. 7. Personalized search in Apps. (a) RMSE. (b) HR. (c) AP.
![img-9.jpeg](img-9.jpeg)

Fig. 8. Personalized search in movies. (a) RMSE. (b) HR. (c) AP.
information. More knowledge should be more helpful if it is effectively extracted and applied. Furthermore, taking Movies as an example, the RMSE of IEDA-MsH is $1.164,5.67 \%$ lower than that of the result given by RBFIEDA. The HR and MAP are 0.01168 and 0.839 , improving $26.13 \%$ and $13.84 \%$ higher than those values of the RBFIEDA, respectively. These results demonstrate the IEDA assisted with UGCs-driven RBM can help users to more accurately find preferred items in most cases.
2) IEDA-MsH and IEDA-CT perform better than IEDAcateg on most datasets, which demonstrates that fusing both users text comments and items categories with IEDA is more valuable than only using items categories as traditional personalized search methods did. The reason lies in that more preference information implied in the comments is further extracted with our RBM model to enhance the optimization performance of IEDA. Especially, the UGCs-driven RBM model can not only track users preference but also provide a reliable fitness surrogate and probability model for IEDA. Such results also turn out the feasibility and effectiveness of the proposed methods on integrating and representing the domain knowledge of the personalized search with EAs.

Ten users are randomly selected in each dataset to perform the IEAs on personalized search, and the comparative algorithms on RMSE, HR, and AP metrics are visualized to intuitively show the superiority of our algorithm. Each IEA method performs ten iterations and the evolutionary searching results are shown in Figs. 6-8 on Music, Apps, and Movies.

In Figs. 6-8, IEDA-MsH represented with blue star line is significantly superior to other compared algorithms on the evaluation metrics in these cases. The experiments on multiple real-world datasets from different domains demonstrate that the proposed algorithm outperforms other compared IEAs in prediction accuracy and recommendation results. Accordingly, we can also conclude that the developed IEDA with UGCs and corresponding knowledge fusion is effective and applicable for the personalized search in the complex environment.

## VI. CONCLUSION

We first state two key points of applying EAs to solve practical optimization problems, i.e., the fusion of domain knowledge and conversion of optimal objectives. Aiming at the personalized search with UGCs, we present a multisource heterogeneous UGCs-enhanced IEDA to improve the search efficiency by sufficiently extracting the users preference and individualized requirements. The UGCs are mathematically

represented by using binary and doc2vec-based feature vectors, and then used to train an RBM to track the users preference. Based on the RBM, the reproduction probability model together with the optimization objectives termed as fitness surrogate is designed for successfully driving the EDA process. The effectiveness of representing UGCs-based domain knowledge, constructing RBM surrogate, and fusing such knowledge with IEDA is experimentally demonstrated by comparing with popular algorithms on Amazon datasets.
The UGCs used here only includes items ranks, comments, and category tags. Besides these, other domain knowledge as images or videos is also very helpful on designing more competitive IEAs for solving personalized search problems. We will carry out further work from these viewpoints in the future.

## REFERENCES

[1] H. Wang, Y. Jin, C. Sun, and J. Doherty, "Offline data-driven evolutionary optimization using selective surrogate ensembles," IEEE Trans. Evol. Comput., vol. 23, no. 2, pp. 203-216, Apr. 2019.
[2] M. A. Dulebenets, "Application of evolutionary computation for berth scheduling at marine container terminals: Parameter tuning versus parameter control," IEEE Trans. Intell. Transp. Syst., vol. 19, no. 1, pp. 25-37, Jan. 2018.
[3] J. Sun et al., "Learning from a stream of nonstationary and dependent data in multiobjective evolutionary optimization," IEEE Trans. Evol. Comput., vol. 23, no. 4, pp. 541-555, Aug. 2019.
[4] Y. Xiang, Y. Zhou, L. Tang, and Z. Chen, "A decomposition-based manyobjective artificial bee colony algorithm," IEEE Trans. Cybern., vol. 49, no. 1, pp. 287-300, Jan. 2019.
[5] Y. Tian, X. Zhang, C. Wang, and Y. Jin, "An evolutionary algorithm for large-scale sparse multiobjective optimization problems," IEEE Trans. Evol. Comput., vol. 24, no. 2, pp. 380-393, Apr. 2020.
[6] P. Bontrager, W. Lin, J. Togelius, and S. Risi, "Deep interactive evolution," in Computational Intelligence in Music, Sound, Art and Design (Lecture Notes in Computer Science), vol. 10783. A. Liapis, J. R. Cardalda, A. Ekärt, Eds. Cham, Switzerland: Springer, 2018. [Online]. Available: https://doi.org/10.1007/978-3-319-77583-8_18
[7] N. D. F. Ross, M. B. Johns, E. C. Reedwell, and D. A. Savic, "Humanevolutionary problem solving through gamification of a bin-packing problem," in Proc. Genet. Evol. Comput. Conf. Companion, 2019, pp. 1465-1473.
[8] J. Lv, M. Zhu, W. Pan, and X. Liu, "Interactive genetic algorithm oriented toward the novel design of traditional patterns," Information, vol. 10, no. 2, p. 36, 2019.
[9] S. Ono, H. Maeda, K. Sakimoto, and S. Nakayama, "Optimizing quantitative and qualitative objectives by user-system cooperative evolutionary computation for image processing filter design," in Proc. Online World Conf. Soft Comput. Ind. Appl., 2014, pp. 167-178.
[10] M. Fukumoto and Y. Hanada, "Investigation of the efficiency of continuous evaluation-based interactive evolutionary computation for composing melody," IEEJ Trans. Elect. Electron. Eng., vol. 15, no. 2, pp. 235-241, 2020.
[11] X. Bu, J. Zhu, and X. Qian, "Personalized product search based on user transaction history and hypergraph learning," Multimedia Tools Appl., vol. 79, pp. 22157-22175, May 2020.
[12] Y. Chen, X. Sun, D. Gong, Y. Zhang, J. Choi, and S. Klasky, "Personalized search inspired fast interactive estimation of distribution algorithm and its application," IEEE Trans. Evol. Comput., vol. 21, no. 4, pp. 588-600, Aug. 2017.
[13] T. Cunha, C. Soares, and A. C. P. L. F. de Carvalho, "Metalearning and recommender systems: A literature review and empirical study on the algorithm selection problem for collaborative filtering," Inf. Sci., vol. 423, pp. 128-144, Jan. 2018.
[14] C. Wu, F. Wu, M. An, J. Huang, Y. Huang, and X. Xie, "NPA: Neural news recommendation with personalized attention," in Proc. 25th ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., 2019, pp. 2576-2584.
[15] Z. Ma, Z. Dou, G. Bian, and J.-R. Wen, "PSTIE: Time information enhanced personalized search," in Proc. 29th ACM Int. Conf. Inf. Knowl. Manage., 2020, pp. 1075-1084.
[16] X. Sun, D. Gong, Y. Jin, and S. Chen, "A new surrogate-assisted interactive genetic algorithm with weighted semisupervised learning," IEEE Trans. Cybern., vol. 43, no. 2, pp. 685-698, Apr. 2013.
[17] H. Sayama, "Complexity, development, and evolution in morphogenetic collective systems," in Evolution, Development and Complexity. Cham, Switzerland: Springer, 2019, pp. 293-305.
[18] L. Bao, X. Sun, Y. Chen, D. Gong, and Y. Zhang, "Restricted Boltzmann machine-driven interactive estimation of distribution algorithm for personalized search," Knowl. Based Syst., vol. 200, Jul. 2020, Art. no. 106930. [Online]. Available: http://www.sciencedirect.com/science/article/pii/S0950705120303269
[19] J. Lu, D. Wu, M. Mao, W. Wang, and G. Zhang, "Recommender system application developments: A survey," Decis. Support Syst., vol. 74, pp. 12-32, Jun. 2015.
[20] Z. Batmaz, A. Yurekli, A. Bilge, and C. Kaleli, "A review on deep learning for recommender systems: Challenges and remedies," Artif. Intell. Rec., vol. 52, no. 1, pp. 1-37, 2019.
[21] H. Fang, G. Guo, D. Zhang, and Y. Shu, "Deep learning-based sequential recommender systems: Concepts, algorithms, and evaluations," in Proc. Int. Conf. Web Eng., 2019, pp. 574-577.
[22] Y. Chen, Y. Jin, and X. Sun, "Language model based interactive estimation of distribution algorithm," Knowl. Based Syst., vol. 200, Jul. 2020, Art. no. 105980. [Online]. Available: http://www.sciencedirect.com/ science/article/pii/S0950705120302938
[23] S. Rendle, C. Freudenthaler, Z. Gantner, and L. Schmidt-Thieme, "BPR: Bayesian personalized ranking from implicit feedback," 2012. [Online]. Available: arXiv:1205.2618.
[24] H. Wang, N. Wang, and D.-Y. Yeung, "Collaborative deep learning for recommender systems," in Proc. 21st ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., 2015, pp. 1235-1244.
[25] P. Covington, J. Adams, and E. Sargin, "Deep neural networks for YouTube recommendations," in Proc. 10th ACM Conf. Recommender Syst., 2016, pp. 191-198.
[26] D. Kim, C. Park, J. Oh, and H. Yu, "Deep hybrid recommender systems via exploiting document context and statistics of items," Inf. Sci., vol. 417, pp. 72-87, Nov. 2017.
[27] K. Georgiev and P. Nakov, "A non-IID framework for collaborative filtering with restricted Boltzmann machines," in Proc. 30th Int. Conf. Mach. Learn., 2013, pp. 1148-1156.
[28] T. T. Nguyen and H. W. Lauw, "Representation learning for homophilic preferences," in Proc. 10th ACM Conf. Recommender Syst., 2016, pp. 317-324.
[29] Y. Wu, C. DuBois, A. X. Zheng, and M. Ester, "Collaborative denoising auto-encoders for top-n recommender systems," in Proc. 9th ACM Int. Conf. Web Search Data Min., 2016, pp. 153-162.
[30] D. Liang, R. G. Krishnan, M. D. Hoffman, and T. Jebara, "Variational autoencoders for collaborative filtering," in Proc. World Wide Web Conf., 2018, pp. 689-698.
[31] D. Kim, C. Park, J. Oh, S. Lee, and H. Yu, "Convolutional matrix factorization for document context-aware recommendation," in Proc. 10th ACM Conf. Recommender Syst., 2016, pp. 233-240.
[32] L. Zheng, V. Noroozi, and P. S. Yu, "Joint deep modeling of users and items using reviews for recommendation," in Proc. 10th ACM Int. Conf. Web Search Data Min., 2017, pp. 425-434. [Online]. Available: https://doi.org/10.1145/3018661.3018665
[33] H. Dai, Y. Wang, R. Trivedi, and L. Song, "Deep coevolutionary network: Embedding user and item features for recommendation," 2016. [Online]. Available: arXiv:1609.03675.
[34] C.-Y. Wu, A. Ahmed, A. Beutel, A. J. Smola, and H. Jing, "Recurrent recommender networks," in Proc. 10th ACM Int. Conf. Web Search Data Min., 2017, pp. 495-503.
[35] J. Wang, T. Weng, and Q. Zhang, "A two-stage multiobjective evolutionary algorithm for multiobjective multidepot vehicle routing problem with time windows," IEEE Trans. Cybern., vol. 49, no. 7, pp. 2467-2478, Jul. 2019.
[36] L. Zuowen, G. Wenyin, Y. Xuesong, W. Ling, and H. Chengyu, "Solving nonlinear equations system with dynamic repulsion-based evolutionary algorithms," IEEE Trans. Syst., Man, Cybern., Syst., vol. 50, no. 4, pp. 1590-1601, Apr. 2020.
[37] X. Zhang, K. Zhou, H. Pan, L. Zhang, X. Zeng, and Y. Jin, "A network reduction-based multiobjective evolutionary algorithm for community detection in large-scale complex networks," IEEE Trans. Cybern., vol. 50, no. 2, pp. 703-716, Feb. 2020.
[38] X. Yan, H. Huang, Z. Hao, and J. Wang, "A graph-based fuzzy evolutionary algorithm for solving two-echelon vehicle routing problems," IEEE Trans. Evol. Comput., vol. 24, no. 1, pp. 129-141, Feb. 2020.

[39] G.-S. Hao, D.-W. Gong, and Y.-Q. Huang, "Interactive genetic algorithms based on estimation of user's most satisfactory individuals," in Proc. 6th Int. Conf. Intell. Syst. Design Appl., vol. 3. Jian, China, 2006, pp. 132-137.
[40] Y. Pei and H. Takagi, "Local information of fitness landscape obtained by paired comparison-based memetic search for interactive differential evolution," in Proc. IEEE Congr. Evol. Comput. (CEC), Sendai, Japan, 2015, pp. 2215-2221.
[41] K. Ishibashi, "Interactive texture chooser using interactive evolutionary computation and similarity search," in Proc. Nicograph Int. (NicoInt), Tainan, Taiwan, 2018, pp. 37-44.
[42] M. Fukumoto and Y. Hanada, "A proposal for creation of beverage suited for user by blending juices based on interactive genetic algorithm*," in Proc. IEEE Int. Conf. Syst. Man Cybern. (SMC), Bari, Italy, 2019, pp. 1104-1109.
[43] L. Pan, C. He, Y. Tian, H. Wang, X. Zhang, and Y. Jin, "A classificationbased surrogate-assisted evolutionary algorithm for expensive manyobjective optimization," IEEE Trans. Evol. Comput., vol. 23, no. 1, pp. 74-88, Feb. 2019.
[44] R. Funaki, K. Sugimoto, and J. Murata, "Estimation of influence of each variable on user's evaluation in interactive evolutionary computation," in Proc. 9th Int. Conf. Awareness Sci. Technol. (iCAST), Fukuoka, Japan, 2018, pp. 167-174.
[45] G. Guo, Z. Wen, and G. Hao, "Set-based interactive evolutionary computation with forecasting fitness by grey support vector regression," Control Decis., vol. 35, no. 2, pp. 309-318, 2020.
[46] P. Cremonesi, Y. Koren, and R. Turrin, "Performance of recommender algorithms on top-n recommendation tasks," in Proc. 4th ACM Conf. Recommender Syst., 2010, pp. 39-46.
[47] L. Guo, J. Liang, Y. Zhu, Y. Luo, L. Sun, and X. Zheng, "Collaborative filtering recommendation based on trust and emotion," J. Intell. Inf. Syst., vol. 53, no. 1, pp. 113-135, 2019.
[48] H. Qiu, Y. Liu, G. Guo, Z. Sun, J. Zhang, and H. T. Nguyen, "BPRH: Bayesian personalized ranking for heterogeneous implicit feedback," Inf. Sci., vol. 453, pp. 80-98, Jul. 2018.
[49] C. Li, X. Niu, X. Luo, Z. Chen, and C. Quan, "A review-driven neural model for sequential recommendation," 2019. [Online]. Available: arXiv:1907.00590.
[50] Y. Wei, X. Wang, L. Nie, X. He, R. Hong, and T.-S. Chua, "MMGCN: Multi-modal graph convolution network for personalized recommendation of micro-video," in Proc. 27th ACM Int. Conf. Multimedia, 2019, pp. 1437-1445.
[51] J. Jin et al., "An efficient neighborhood-based interaction model for recommendation on heterogeneous graph," in Proc. 26th ACM SIGKDD Conf. Knowl. Discov. Data Min. (KDD), 2020, pp. 75-84.
[52] L. Hu et al., "Graph neural news recommendation with unsupervised preference disentanglement," in Proc. 58th Annu. Meeting Assoc. Comput. Linguist., 2020, pp. 4255-4264.
[53] N. Le Roux and Y. Bengio, "Representational power of restricted Boltzmann machines and deep belief networks," Neural Comput., vol. 20, no. 6, pp. 1631-1649, Jun. 2008.
[54] L.-W. Kim, "DeepX: Deep learning accelerator for restricted Boltzmann machine artificial neural networks," IEEE Trans. Neural Netw. Learn. Syst., vol. 29, no. 5, pp. 1441-1453, May 2018.
[55] G. E. Hinton, "Training products of experts by minimizing contrastive divergence," Neural Comput., vol. 14, no. 8, pp. 1771-1800, 2002.
[56] R. Salakhutdinov, A. Mnih, and G. Hinton, "Restricted Boltzmann machines for collaborative filtering," in Proc. 24th Int. Conf. Mach. Learn., 2007, pp. 791-798.
[57] N. Ji, J. Zhang, C. Zhang, and Q. Yin, "Enhancing performance of restricted Boltzmann machines via log-sum regularization," Knowl. Based Syst., vol. 63, pp. 82-96, Jun. 2014.
[58] S. Feng and C. L. P. Chen, "A fuzzy restricted Boltzmann machine: Novel learning algorithms based on the crisp possibilistic mean value of fuzzy numbers," IEEE Trans. Fuzzy Syst., vol. 26, no. 1, pp. 117-130, Feb. 2018.
[59] L. Bao, X. Sun, Y. Chen, G. Man, and H. Shao, "Restricted Boltzmann machine-assisted estimation of distribution algorithm for complex problems," Complexity, vol. 2018, Nov. 2018, Art. no. 2609014. [Online]. Available: https://doi.org/10.1155/2018/2609014
[60] N. Hazrati, B. Shams, and S. Haratizadeh, "Entity representation for pairwise collaborative ranking using restricted Boltzmann machine," Expert Syst. Appl., vol. 116, pp. 161-171, Feb. 2019.
[61] Q. Le and T. Mikolov, "Distributed representations of sentences and documents," in Proc. 31st Int. Conf. Mach. Learn., 2014, pp. 1188-1196.
[62] R. He and J. McAuley, "Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering," in Proc. 25th Int. Conf. World Wide Web, 2016, pp. 507-517.
[63] Y. Liang, Z. Ren, X. Yao, Z. Feng, A. Chen, and W. Guo, "Enhancing Gaussian estimation of distribution algorithm by exploiting evolution direction with archive," IEEE Trans. Cybern., vol. 50, no. 1, pp. 140-152, Jan. 2020.
[64] X. He, L. Liao, H. Zhang, L. Nie, X. Hu, and T.-S. Chua, "Neural collaborative filtering," in Proc. 26th Int. Conf. World Wide Web, 2017, pp. 173-182.
![img-10.jpeg](img-10.jpeg)

Lin Bao received the Ph.D. degree in control theory and control engineering from the China University of Mining and Technology, Xuzhou, China, in 2020. She is a Lecturer with the School of Electronics and Information, Jiangsu University of Science and Technology, Zhenjiang, China. Her research interest covers evolutionary computation and machine learning.
![img-11.jpeg](img-11.jpeg)

Xiaoyan Sun (Member, IEEE) received the Ph.D. degree in control theory and control engineering from the China University of Mining and Technology, Xuzhou, China, in 2009.
She is a Professor with the School of Information and Control Engineering, China University of Mining and Technology. Her research interest covers evolutionary computation and machine learning.

Dunwei Gong (Member, IEEE) received the Ph.D. degree in control of Mining and Technology, Xuzhou, China, in 1999.
He is a Professor with the School of Information and Control Engineering, China University of
Mining and Technology. His current research interests include computation intelligence in multi-/many-objective optimization, dynamic and uncertain optimization, as well as applications in software engineering, integrated energy systems, scheduling, and healthcare.
![img-12.jpeg](img-12.jpeg)

Yong Zhang (Member, IEEE) received the Ph.D. degree in control of Mining and Technology, Xuzhou, China, in 2009.
He is a Professor with the School of Information and Control Engineering, China University of Mining and Technology. His research interest covers swarm intelligence and machine learning.