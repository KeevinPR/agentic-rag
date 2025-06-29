# DPM-IEDA: Dual Probabilistic Model Assisted Interactive Estimation of Distribution Algorithm for Personalized Search 

YANG CHEN ${ }^{\odot 1}$, XIAOYAN SUN ${ }^{\odot 1}$, (Member, IEEE), DUNWEI GONG ${ }^{\odot 2}$, (Member, IEEE), AND XIANGJUAN YAO ${ }^{3}$<br>${ }^{1}$ School of Information and Control Engineering, China University of Mining and Technology, Xuzhou 221116, China<br>${ }^{2}$ School of Information Science and Technology, Qingdao University of Science and Technology, Qingdao 266061, China<br>${ }^{3}$ School of Science, China University of Mining and Technology, Xuzhou 221116, China<br>Corresponding author: Xiaoyan Sun (xysun78@126.com)

This work was supported by the National Natural Science Foundation of China under Grant 61876184, Grant 61473298, Grant 61573362, and Grant 61773384 .

#### Abstract

An interactive evolutionary algorithm (IEA) is powerful for solving personalized search when the user's preference can be well caught, expressed, and applied in the process of searching. Hybrid recommendation by articulating the content-based and collaborative filtering techniques is popular and effective for the personalized recommendation, but has not been developed to improve the performance of IEA for fulfilling the personalized search. Accordingly, we here propose an enhanced interactive estimation of distribution algorithm by designing dual-probabilistic models based on the hybrid recommendation for personalized search. The concept of hybrid personalized search is first defined from the viewpoint of using not only the historical search information but also the social or group preference. A dual-probabilistic model by sufficiently combining the content-based and collaborative filtering is presented and used to design the effective interactive estimation of distribution algorithm (IEDA). The probabilistic model is directly combined with the initialization of IEDA for illuminating the sparsity of the traditional IEA in encoding. The effectiveness of the proposed algorithm in fast and efficient searching with a lower computational cost is experimentally illustrated by two typical personalized searches on movies and TV series described with documents.


#### Abstract

INDEX TERMS Collaborative filtering, estimation of distribution algorithm, interactive evolutionary computation, personalized search.


## I. INTRODUCTION

Personalized search is a powerful solution to the explosive growth in the volume of available products for customers who do the shopping online. The central task in personalized search is to help users/customers locate as more satisfactory ones as possible from innumerable items; thus, it is essentially an optimization problem. However, no explicit mathematical expression of the problem can be precisely defined.

Interactive evolutionary algorithm (IEA) is a sub-area of evolutionary computation research, which develops a class of nature-inspired, population-based search algorithms for optimization. Although, a large number of engineering projects and applications have proved the effectiveness of
evolutionary algorithms (EA). However, many personalized needs or preference related optimization cannot be addressed by EA due to the lack of precise mathematical objectives. IEA [1]-[3] is more practical and suitable in such scenarios as its framework involves a human user offering evaluations; this kind of algorithm has been developed and successfully tested by various related problems, such as product design and web page layout design [4], [5].

In the field of personalized recommendation, three technologies, i.e., content-based, collaborative filtering and their hybrid techniques, have been successfully developed and applied to improve the accuracy of recommender systems [6]. Combining collaborative filtering and content-based filtering could be more effective, and thus hybrid recommendation is more popular in recent years [7]-[9]. Even these methods have been widely studied and used for recommending

The associate editor coordinating the review of this manuscript and approving it for publication was Jagdish Chand Bansal.

accurate and reliable items to users, they have not been well combined with the optimization to further enhance the personalized search or recommendation.

Because of human users are required by IEA, there normally exists a limit of the population size or evolutionary generations unlike the approaches of EA. So, concern for user fatigue sets a great barrier for applying this techniques into a wide range of problems [2]. Therefore, from different perspectives, some improvements have been proposed, and the related following two are listed:

1. With the help of constructing preference surrogates as fitness functions, IEA is greatly improved since their population size and evolutionary generations can be enlarged as conventional EA did [10], [11].
2. Extracted knowledge assisted evolutionary operators were designed to accelerate search and reduce user burdens [12], [13].
These aforementioned surrogate/knowledge-assisted IEAs that employ user's preference reflected in interactions and historical search information can be regarded the combination of IEA and content-based filtering. In these algorithms, the social or group preference has not been well used to guide the current user to fast get his/her preferred items. Clearly, combining the advantage of collaborative filtering with the content-based IEA, i.e., designing a hybrid recommender assisted IEA, should be an effective strategy on presenting a powerful tool for the personalized search. To the best of our knowledge, no corresponding research has been conducted in neither EA fields nor recommender systems.

In this study, following the hybrid mechanisms of contentbased filtering and collaborative filtering, we present an enhanced interactive estimation of distribution algorithm (IEDA) employing two probabilistic models. Specifically, they play their roles of a preference surrogate and a knowledge extractor, respectively. The main contributions of this study are as follows.

1. We study and design a dual-probabilistic-model EDA. With the appropriately designed dual-loop framework, the presented algorithm helps to involve both contentbased and collaborative filtering knowledge in the offspring generation and the selected items for user evaluation.
2. The probabilistic models are not only used in the EDA in generating individuals but also directly applied to the initialization to reduce the computation cost caused by sparse encoding in those existing IEAs.
3. The searched items or encoded objectives are described in documents, which has not been studied in the field of IEAs.
4. On two mainstream datasets, this study conducts extensive experiments to evaluate the proposed dual-probabilistic-model based IEDA, and the results show the algorithm's advantages.
The remainder of this paper is organized as follows. The corresponding EA assisted personalized search, EDA, and collaborative filtering will be briefly introduced in Section II.

And then, the detail of the proposed algorithm, including the definition of hybrid personalized search, the running example, the framework of our algorithm, the initialization and update of dual-probabilistic-model, and the IEDA, is presented in Section III. Section IV addresses the application of the proposed algorithm together with the experimental results and analyses. Conclusions are drawn in Section V.

## II. RELATED WORK

## A. EVOLUTIONARY ALGORITHM ASSISTED PERSONALIZED SEARCH

As aforementioned, personalized search is considered as an optimization problem without explicit mathematical expression. User preferences reflected in evaluating the searched items are utilized and tracked in studies of personalized search or recommendation [14], [15]. Abou-Zleikha et al. [16], [17] focused on the optimization of preference model structures, together with corresponding parameters. However, the search process was not addressed as an optimization in these studies.

Another manner of applying EA into personalized search is to involve human users to evaluate items and quantify their preference with rankings [18], [19]. None of this research integrated the preference model constructed upon user's interactions to accelerate the search process.

Some IEA-assisted personalized search by constructing a preference model have been further studied [20], [21]. Chen et al. presented a fast interactive estimation of distribution algorithm (IEDA) utilizing the domain knowledge of personalized search [22]. In this study, the IEDA maintained a Bayesian model describing user preference on variables to enhance its performance in fast locating the satisfactory items. However, this work did not consider the help from the social preference.

In these existing IEA-based personalized search studies, the items to be searched are expressed as the combinations of the corresponding features. Thus, the individuals of the IEA is the encoding of the contents based features, and the search in the each generation of the evolutionary process is to find the optimal combinatorial features most matching the user's current preference. And the user's preference is usually obtained based on the similarities of the current individuals (items) to those he/she preferred. Clearly, this procedure in each generation is quite similar to the content-based recommendation except that the user's preference is induced from his/her current interactions not only from the query terms [23].

## B. ESTIMATION OF DISTRIBUTION ALGORITHMS

Estimation of distribution algorithms (EDAs) [24], [25] start with an initial population that consists of a certain number of candidate solutions to a problem. Offspring, i.e. new solutions, are generated by sampling from a probabilistic model [26]-[29]. Promising candidate solutions are then selected according to their fitness to build an explicit

probabilistic. Iterations continue until certain termination conditions are met. Approaches based on dependent chains/trees, factorization, neural trees, Bayesian networks, and genetic programming have been proposed for maintaining the probability distribution of population [26].
In [22], Chen et al. first integrated EDA into the framework of IEA to propose a novel IEDA, which proved its effectiveness and efficiency in personalized search. When applying EDA into the interactive evolutionary optimization, the key is to design a competitive probabilistic model for generating new individuals. In our previous work, the Bayesian statistic was applied to construct the probabilistic model based on the user's interactions. The information on the historical and searched items or individuals is involved in building and updating the probabilistic model, however, the information of other users or the social preference on searching similar items has not been concerned on. Social preference can be a good guidance for the personalized search due to the peer pressure. Therefore, it will be beneficial in further improving the capability of IEDA in fast and accurately searching personalized items.

## C. COLLABORATIVE FILTERING

Collaborative filtering (CF) is further introduced here since it is more important for our algorithm in designing a dual-probabilistic-model IEDA. Collaborative filtering is a technique widely used in recommender systems (RSs) [30]. It predicts the interests of a user with the help of collected preference or taste information from lots of other users. The approach holds the assumption that person $\mathbf{A}$ tends to have more similar opinions with person $\mathbf{B}$, when they share the same opinion or quite similar opinions towards a certain number of issues, compared with a randomly chosen $\mathbf{C}$.

CF techniques can be broadly divided into the following two types.

1. The memory-based approach utilizes rating data to calculate the similarity between users/items, e.g. item-based/user-based top-K recommendations [31], [32].
2. The model-based approach adopts models that are developed with different data mining or machine learning algorithms to predict ratings, e.g. singular value decomposition (SVD), probabilistic latent semantic analysis (pLSA), and latent Dirichlet allocation (LDA) [30], [33].
By introducing CF techniques into the IEDA-assisted personalized search, it and content-based methods are expected to be the complement to each other, and then greatly improve the performance of IEDA.

## III. DUAL-PROBABILISTIC-MODEL BASED INTERACTIVE ESTIMATION OF DISTRIBUTION ALGORITHM

## A. DEFINITION OF HYBRID PERSONALIZED SEARCH

To the active user who is using the personalized search service, items are divided into two sets, i.e., the evaluated ones, $I$, and those to be evaluated, $I_{e}$. Her/his preference in the i-th item is $f(i)$, where $i \in I_{e}$; then, the search can be formulated as Eq. 1, where $D$ is the feasible space of existing items. The original problem cannot be solved because mathematical formula $f(\cdot)$ is scarcely defined.

$$
\left\{\begin{array}{l}
\max f(i) \\
\text { s.t. } i \in D
\end{array}\right.
$$

From the viewpoint of optimization, the items to be evaluated can be regarded the individuals to be searched, and the evaluation or preference on the i-th item $f(i)$ is the fitness of it. For IEDA, the framework are as follows: (1) For evaluated items, their fitness is depicted through quantifying preference reflected by interactions. (2) The probabilistic model is updated upon the fitness, $\hat{f}(i, t)$; here, $t$ in the equation indicates that the personalized search is divided into iterations, with which user's preference is obtained more and more accurately. (3) Then, offspring are generated from sampling the model, and candidates are located according to the individuals. (4) Evaluations are carried out on these candidates. The process keeps iterating until the active user gets her/his preferred item [22]. Therefore, the personalized search can be redefined as Eq. 2.

$$
\left\{\begin{array}{l}
\max \hat{f}(i, t) \\
\text { s.t. } i \in s
\end{array}\right.
$$

where $s$ represents the encoding space, and $D \subset s$.
Within the field of recommendation, according to how items to be dealt with, techniques are classified into contentbased and CF-based approaches. Hybrid recommender systems are often built by combining both approaches to achieve better performance [6]. Inspired by this, the presented IEA-assisted hybrid personalized search is detailed as follows.

Notations are shown in Table 1. As detailed, documents, termed as doc $=$ \{description\} $\cup$ \{comments\}, are the original descriptions of items from sellers and customers; they are identified by their IDs, termed as $i$. In two settings, fitness of unevaluated items are estimated in different methods. For the content-based one, a SVR (support vector regression) keeps being retrained with evaluated items $\left(\operatorname{word} 2 \operatorname{vec}\left(d o c_{i}\right), r_{i}\right), i \in I_{e}$ in each iteration; word $2 \operatorname{vec}\left(d o c_{i}\right)$ indicates that the language model word $2 \operatorname{vec}(\cdot)$ converts $d o c_{i}$ into a fixed-length vector $x$ as the input of SVR, and its corresponding output $r_{i}$ is the rating. Assisted with the SVR, all items belonging to $I$ are assigned estimated ratings $\left(d o c_{i}, \tilde{r}_{i}\right), i \in I$.

For the CF-based one, ratings $\left(i, \tilde{r}_{i}\right), i \in I$ are estimated by the CF algorithm that is trained on all records before the search. Training dataset involves all stored users and items. Within the personalized search, the algorithm keeps fixed. With these two predicted ratings, the probabilities of each possible outcome can be estimated.

TABLE 1. Notation.

| Notation | Formula | Used by | Usage |
| :-- | :-- | :-- | :-- |
| Document | doc | User | Evaluation |
| ID | $i$ | Both Probabilistic Models | Identification |
| Predicted rating | $\hat{r}$ | Collaborative Filtering Probabilistic Model | Predicted Preference |
| Semantic vector | $x$ | Cotent-Based Probabilistic Model | Measurement of Item Similarity |

![img-0.jpeg](img-0.jpeg)

FIGURE 1. A running example of dual-probabilistic-model-based IEDA.

## B. RUNNING EXAMPLE

In this section, a running example of the presented method is introduced to enhance readers' understanding. It is illustrated in Fig. 1.

In personalized search, an active user first requests a search service by inputting queries. Based on the queries, nonpersonalized pre-filtering is conducted to return a prefiltered list by simply matching the offered queries with the movies stored in database.

With the help of CF model, e.g. SVD++ and SVD, rating prediction is carried out to arrange all the items in the prefiltered list estimated ratings, i.e. rating '(user, item $_{i}$ ). The following step is the categorization, which first removes the items with estimated ratings lower than a threshold; sorts them into different categories according to their predicted ratings. Then, the search list is obtained.

If the CF-based probabilistic model initialization has not been conducted yet, it is then carried out. With the probabilistic model, CF-based sampling is thus performed to generate the population. Similarly, Content-based probabilistic model initialization and Content-based sampling are executed sequentially; hence, the evaluation list is obtained.
To the items in the evaluation list, the active user conducts interaction, i.e. user evaluation. Therefore, to the evaluated items, their ratings are known, and the evaluation list becomes $s_{e, t}$ that will be used to update the two probabilistic models.

If the active user feels satisfied or tired, ${ }^{1}$ the personalized search is then terminated. If not so, the other decision that determining whether to execute the inner or the outer loop is to be made. Since all evaluated items are deleted from the population, population size keeps decreasing. If there are sufficient items in the population and it performs well, the inner loop is carried out to update the contentbased probabilistic model with $s_{e, t}$. If not so, the outer loop is chosen to update the CF-based probabilistic model with $s_{e, t-m: t}$.

## C. MAIN FRAMEWORK

The main framework of the proposed algorithm is shown in Fig. 2. Two models, Doc2Vec and CF, are trained in the offline phase. Upon them, two probabilistic models are initialized. The CF-based part first samples to generate the
${ }^{1} 240$ items has been evaluated in our experimental setting

![img-1.jpeg](img-1.jpeg)

FIGURE 3. The framework of dual-probabilistic-model-based IEDA.
population from all candidate items; then, the content-based probabilistic model samples to obtain the items for the user to evaluate.

After evaluation, the user decides whether to stop or not. If the user chooses to continue, one of these two probabilistic models are selected to update according to the number of unevaluated items in the population and the quality of the population. The procedures repeat until the user terminates the search.

The critical part of our algorithm involves four components:

1. CF-based probabilistic model initialization,
2. CF-based probabilistic model update,
3. content-based probabilistic model initialization,
4. content-based probabilistic model update.

They are shaded in Fig. 2 and explained into two groups in Section III-D and Section III-E.

## D. CF-BASED PROBABILISTIC MODEL INITIALIZATION/UPDATE

At each generation $t$, collaborative filtering based probabilistic model initialization/update maintains:

1. a list of items to be searched falling into K categories $L_{\text {search }}=\left\{\ldots, L_{\text {search }, k}, \ldots\right\}$, and these categories' corresponding estimated probabilities are $\left\{\ldots, \hat{P_{k}}, \ldots\right\}$, $k \in\{1,2, \ldots, \mathrm{~K}\}$; in Fig. 1 the list is labeled with Search List. The items' probabilities, represented as circles, belonging to different categories are in different colors. For example, Category $k$ is in blue. The Search

List is selected by excluding the items with too low estimated ratings, which are represented with shaded circles.
2. a CF-based probabilistic model $\boldsymbol{p}=\left(\ldots, p_{j}, \ldots\right), j \in$ $L_{\text {search }, k}$ and $k \in\{1,2, \ldots, \mathrm{~K}\}$; in the example given in Fig. 1, the depth of circles' colors indicates the searched probabilities of the corresponding items. The deeper its color is, the higher the item's probability is.
3. a set $s_{e, t-m: t}$ storing evaluated items in last $m$ rounds of evaluation; $m$ is not fixed but determined upon the quality and size of the population. In the illustration, the Evaluation Lists located at the bottom correspond to the set $s_{e, t-m: t}$. The initialization of the CF-based probabilistic model executes at the initial and is presented in Algorithm 1.
Its main components are explained as follows.

1. Initialization of Search List: In lines 1-5, the search list is initialized with threshold $r_{\text {threshold }}$. Its value is determined with the help of a test set that is randomly chosen from evaluation records, and data in the test set are not involved in training. For the items involved in the set, both their ratings $r$ and estimated ratings $\hat{r}$ are known. So, the value of $r_{\text {threshold }}$ meeting $P(r>$ $r_{\text {threshold_target }} \mid \hat{r}>r_{\text {threshold }}$ ) $>0.9$ in the test set is selected since personalized search is expected to hold a similar assumption.
2. Categorization: Lines 6 and 7 execute the categorization and make sure that the items with similar estimated ratings belong to the same or adjacent categories.

Algorithm 1 CF-Based Probabilistic Model Initialization
Input: the items of pre-filtered list indexed by $i \in$ $\{1,2,3, \ldots, n\}$, their corresponding CF-based estimated ratings $\hat{r}_{i}$, threshold $r_{\text {threshold }}$ used to define list $L_{\text {search }}$ for searching, these items falling into K categories indexed by $k$, estimated probability $\hat{P}_{k}$
Output: CF-based probabilistic model $\boldsymbol{p}=\left(\ldots, p_{j}, \ldots\right), j \in$ $L_{\text {search }, k}$ and $k \in\{1,2, \ldots, \mathrm{~K}\}$, len $_{k}, a_{k}, b_{k}$
for $i=1 \rightarrow n$ do
if $\hat{r}_{i}>r_{\text {threshold }}$ then
add $i$ to $L_{\text {search }}$
end if
end for
sort $L_{\text {search }}$ by $\hat{r}$
evenly arrange the items belonging to $L_{\text {search }}$ in categories $L_{\text {search }, k}$
for $k=1 \rightarrow K$ do
for $j \in L_{\text {search }, k}$ do
$p_{j}=\hat{P}_{k} * e^{\hat{r}_{j}} / \sum_{1}\left|L_{\text {search }, k}\right| e^{\hat{r}_{j}}$
end for
len $_{k} \leftarrow\left|L_{\text {search }, k}\right|$
$a_{k} \leftarrow 0$
$b_{k} \leftarrow 0$
end for

## Algorithm 2 CF-Based Probabilistic Model Update

Input: estimated category probability $\hat{P}_{k}$, categorized lists $\{\ldots, L_{\text {search }, k}, \ldots\}$, evaluated items per iteration $\left(i, r_{i}\right)$, $i \in s_{e, t-m: t}$, threshold $r_{\text {threshold_target }}$ used to distinguish targets from other items, len $_{k}, a_{k}, b_{k}$
Output: CF-based probabilistic model $\boldsymbol{p}=\left(\ldots, p_{j}, \ldots\right), j \in$ $L_{\text {search }}$ and $k \in\{1,2, \ldots, \mathrm{~K}\}$
for $i \in s_{e, t-m: t}$ do
get category $k$ of evaluated item $i$
reomove item $i$ from $L_{\text {search }, k}$
if $r_{i}>=r_{\text {threshold_target }}$ then
$a_{k} \leftarrow a_{k}+1$
end if
$b_{k} \leftarrow b_{k}+1$
end for
for $k=1 \rightarrow K$ do
$\hat{P}_{k}^{r} \leftarrow \frac{\text { len }_{k}-a_{k}}{\text { len }_{k} * \hat{P}_{k}-a_{k}-b_{k}}$
for $j \in L_{\text {search }, k}$ do
$p_{j}=\hat{P}^{r}{ }_{k} * e^{\hat{r}_{j}} / \sum_{1}\left|L_{\text {search }, k}\right| e^{\hat{r}_{j}}$
end for
end for
3. Probabilistic Model Initialization: In lines 8-15, the probabilistic vector $\boldsymbol{p}=\left(\ldots, p_{j}, \ldots\right), j \in L_{\text {seacrch }, k}$ and $k \in\{1,2, \ldots, \mathrm{~K}\}$ is constructed by considering category probabilities $\hat{P}_{k}$ and estimated ratings $\hat{r}_{j}$. First, items in the same category share the $\hat{P}_{k}$. Moreover, a non-linear map is used to depict the relation between

Algorithm 3 Content-Based Probabilistic Model Initialization
Input: population pop indexed by $l \in\{1,2, \ldots,|\text { pop }|\}$, pretrained $\operatorname{SVR}(\cdot)$
Output: content-based probabilistic model $\boldsymbol{p}=$ $\left(\ldots, p_{l}, \ldots\right), l \in$ pop
for $l=1 \rightarrow|\operatorname{pop}|$ do
$\hat{r}_{l} \leftarrow \operatorname{SVR}\left(p o p_{l}\right)$
$p_{l} \leftarrow e^{\hat{r}_{l}} / \sum_{1}^{|p o p_{l}} e^{\hat{r}_{l}}$
end for

Algorithm 4 Content-Based Probabilistic Model Update
Input: population pop indexed by $l \in\{1,2, \ldots,|\text { pop }|\}$, $\operatorname{SVR}(\cdot)$ to retrain, evaluated items per iteration $\left(i, r_{i}\right), i \in$ $s_{e, t}$, iteration $t$
Output: content-based probabilistic model $\boldsymbol{p}=$ $\left(\ldots, p_{l}, \ldots\right), l \in$ pop
for $i \in s_{e, t}$ do
remove item $i$ from pop
end for
retrain $\operatorname{SVR}(\cdot)$ with the help of newly evaluated items $\left(i, r_{i}\right)$
for $l=1 \rightarrow|\operatorname{pop}|$ do
$\hat{r}_{l} \leftarrow \operatorname{SVR}\left(p o p_{l}\right)$
$p_{l} \leftarrow e^{\hat{r}_{l}} / \sum_{1}^{|p o p_{l}} e^{\hat{r}_{l}}$
end for
the estimated rating $\hat{r}$ and its shares of the category probability. Additionally, lengths of category lists are stored, and $a_{k}$, the number of satisfactory items from category $k$ and $b_{k}$ recording the number of all evaluated items of category $k$ are reset.
The CF-based probabilistic model update is presented in Algorithm 2, and its main components are explained as follows.

1. Evaluation-Assisted Category Update: Line 2 gets the index $k$ of the evaluated item $i$ based on which category it belongs to; then, line 3 removes it from its corresponding category. If its rating is higher than threshold $r_{\text {threshold_target }}$, counter $a_{k}$ is updated. $b_{k}$ always increases by 1 .
2. Probability Update: In line 10, category probability $\hat{P}^{r}{ }_{k}$ is altered with the updated counters $a_{k}$ and $b_{k}$. In lines 11-13, items of category $k$ share the revised category probability, and their estimated ratings determine ratios. The same non-linear map to that of Algorithm 1 is used here.

## E. CONTENT-BASED PROBABILISTIC MODEL INITIALIZATION/UPDATE

Similarly, at each iteration $t$, this section maintains:

1. a population pop; in the example illustrated in Fig. 1, termed as Population, it appears in the right upper

corner of the figure, consisting of the items and their probabilities represented as purple circles.
2. a content-based model $\operatorname{SVR}(\cdot)$;
3. a content-based probabilistic model $\boldsymbol{p}=\left(\ldots, p_{l}, \ldots\right)$, $l \in$ pop; in the illustration, the corresponding probabilities are indicated with the depth of the color.
4. a set $s_{e, t}$ storing evaluated items at iteration $t$; in Fig. 1, the set is beneath the Population.
The initialization executes at iteration 0 and is presented in Algorithm 3, whose components are explained as follows.

1. Rating Prediction: In line $1, \operatorname{SVR}(\cdot)$ returns predicted rating of the item.
2. Probability Initialization: Lines 3, probability $p_{l}$ is set according to its predicted rating. Additionally, the same non-linear map is used.
The content-based probabilistic model is updated at each iteration $t$, which is presented in Algorithm 4. We further explain it as follows.
3. Evaluation-Assisted pop Update: In lines 1-3, eliminating evaluated items in $s_{e, t}$ from pop.
4. $\operatorname{SVR}(\cdot)$ Update: In line 4, retrain $\operatorname{SVR}(\cdot)$ with newly evaluated items.
5. Rating Re-prediction: In line 6, re-predict ratings of unevaluated items with the updated $\operatorname{SVR}(\cdot)$.
6. Probability Update: Line 7 alters the probability by updated predicted ratings; the same non-linear map is utilized.

## IV. EXPERIMENTS AND ANALYSES

## A. EXPERIMENTAL SETTINGS

Two noted datasets, MovieLens 20M Dataset [34] and Amazon product data [35], are adopted to design extensive experiments to demonstrate the superiority of the proposed dual-probabilistic-model-based IEDA. The MovieLens 20M is a stable benchmark widely used in the studies of recommender systems. It involves 20 million ratings applied to 27,000 movies by 138,000 users. To fulfill the requirement of our experiment, related texts from $\mathrm{IMDb}^{2}$ including introductions and reviews from users are added as complements. As for the Amazon Dataset, only the subset of Movies and TV (5-core) is specifically used; additionally, dissimilar to the texts in MovieLens dataset, these documents only consist of customer reviews.

In the following experiments, the proposed dual-probabilistic-model-based interactive estimation of distribution algorithm (DPM-IEDA), together with the other four algorithms

1. CF-based, short for collaborative-filtering-based personalized search algorithm,
2. CF-based+, short for collaborative-filtering-based+ personalized search algorithm,
3. content-based (IGA), short for content-based (IGA) personalized search algorithm [21], [23], [36],
4. content-based (SVR), short for content-based (SVR) personalized search algorithm [37].
is tested in the following experiments. Specifically, the difference between CF-based and CF-based+ is that the latter one employs a threshold to filter out the items with too low estimated ratings and evaluated items to update its probabilistic vector.

These CF techniques are first considered to construct personalized search algorithms. Mainstream methods addressing this task largely belong to the content-based group. Apart from the IGA-assisted personalized search algorithm, the SVM-assisted one from a different domain to EA, i.e. machine learning, is included as well.

In the probabilistic initialization, the two datasets are separated into a training set and a test one with the percentage of the former data's size being split to simulate real cases. Then, all standard compliant users ${ }^{3}$ are selected from each dataset as active users; specifically, the standard requires users to have sufficient records in the test set, i.e. more than 240, so that there are adequate items to evaluate in experiments. For the selected users, algorithms are expected to help find satisfactory items ${ }^{4}$ throughout the personalized search.

The metrics used to measure the performance here is somewhat different from the traditional recommendation ones. The traditional recommendation task is to find the best item and top-N items based on their predicted ratings, and therefore, the predicting ratings and accuracy, e.g., RMSE and MAE [38], [39], are mainly used as the comparing indicators. However, in the framework of our IEDA, the focus is on helping the active user locate more satisfactory items with limited evaluation burden, and enhance user experience throughout the search process. Accordingly, the following indicators are used here.

Indicators ${ }^{5}$ are adopted as follows:

1. Average relative performance ratio (ARPR) is defined to asses the algorithm performance on a group of standard compliant users, termed as $U$. Given an active user, it is easy to compare algorithms with the help of the number of found satisfactory items; however, light and heavy users are normally of different levels of participation. Simply calculating the average without considering the scale issue would lead to unreliable results.
First, to an active user $\left(u_{j} \in U\right)$ together with a set of compared algorithms, their performance is termed as $C_{j}=\left[c_{1, j}, \ldots, c_{i, j}, \ldots\right]$, where $c_{i, j}$ is the $i$-th algorithm's number of found satisfactory items. The corresponding relative performance ratio (RPR) is defined as: $R P R_{i, j}=\frac{c_{i, j}}{c_{\text {best }}}$, where $c_{\text {best }}=\max \left(C_{j}\right)$.
[^0]
[^0]:    ${ }^{3}$ Given split $=30 \%$, MovieLens 20M includes 13337 standard compliant users; Amazon Dataset (Movie and TV 5-core) includes 255 standard compliant users.
    ${ }^{4}$ the items with the highest rating, i.e., 5.0 in MovieLens 20M \& Amazon product data
    ${ }^{5}$ The indicators are obtained within twenty iterations and twelve items for a active user to evaluate at each iteration

TABLE 2. Experiment on split.

| Metric | $10 \%$ | $30 \%$ | $50 \%$ | $70 \%$ |
| :-- | :-- | :-- | :-- | :-- |
| ARPR | $83.63 \%$ | $89.38 \%$ | $87.81 \%$ | $86.89 \%$ |
| Average Rating | 3.40 | 3.45 | 3.46 | 3.43 |

* Average Relative Performance Ratio (ARPR)
This group of experiment is conducted on CF-based algorithm. All involved cases are from MovieLens 20M. Each datapoint is calculated upon 20 repetitions.

TABLE 3. Parameters.

| Parameter | Range |
| :-- | :-- |
| $C F$ | $\{S V D, S V D++^{*}$, SlopeOne $\}$ |
| $K$ | $\left\{3^{*}, 5,7\right\}$ |
| split $_{\text {threshold }}$ | $\left\{10 \%, 20 \%,^{*}, 30 \%\right\}$ |

* Default setting

Therefore, the $i$-th algorithm's ARPR is defined as: $A R P R_{i}=\frac{\sum_{j \in U} R P R_{i, j}}{|U|}$.
2. Average rating evaluates the overall quality of all items recommended to active users. It considers not only the satisfactory items, but the others, since both of them affect user experience.
3. Intra-list distance (ILD) is the most frequently used diversity metric [40], [41]. Given a recommended set $R$, its ILD is defined as the average pairwise distance of the items belonging to the set: ILD $=$ $\frac{1}{|R|(|R|-1)} \sum_{i \in R} \sum_{j \in R} d(i, j)$, where $d(i, j)$ is a distance measure and is specified as the cosine distance in this study.
4. Algorithm runtime states the computational cost.

Normally, the number of generations are limited to twenty in IEA since user fatigue is considered [1].
The first experiment is carried out to figure out how the split impacts upon the CF model involved in personalized search algorithms. Therefore, the CF-based one is selected as the algorithm to test, and ARPR as well as average rating are compared. Its results are shown in Table 2. The influences over different users are distinct. Overall, they are slight. 30\% is set as default in the following experiments.
Then, two groups of experiments are further conducted, i.e., the effect of the key parameters and the overall performance of the compared algorithms. Table 3 lists key parameters in compared algorithms, where $C F$ specifies the collaborative filtering model adopted in algorithms, $K$ corresponds to the number of categories, and split threshold determines the percentage of the data reserved from training data for estimating $r_{\text {threshold }}$.

## B. EFFECT OF PARAMETERS

The purpose of the parameter related experiments is to discuss the impact of different parameter values upon the algorithms' performance, not to find a most appropriate one. All experiments in this section are carried out on MovieLens 20M, and ARPR as well as average rating are also chosen as indicators.

TABLE 4. Experiment on $C F$.

| Metric | SVD | SVD++ | SlopeOne |
| :-- | :-- | :-- | :-- |
| ARPR* | $90.31 \%$ | $97.21 \%$ | $83.91 \%$ |
| Average Rating | 3.41 | 3.45 | 3.35 |

* Average Relative Performance Ratio (ARPR)
This group of experiment is conducted on CF-based algorithm. All involved cases are from MovieLens 20M. Each datapoint is calculated upon 20 repetitions.

TABLE 5. Experiment on $K$.

| Metric | CF-based | CF-based+ <br> $\varnothing K=3$ | CF-based+ <br> $\varnothing K=5$ | CF-based+ <br> $\varnothing K=7$ |
| :-- | :-- | :-- | :-- | :-- |
| ARPR* | $79.88 \%$ | $95.89 \%$ | $96.39 \%$ | $94.83 \%$ |
| Average Rating | 3.45 | 3.56 | 3.56 | 3.56 |

* Average Relative Performance Ratio (ARPR)
This group of experiment is conducted on CF-based and CFbased+. All involved cases are from MovieLens 20M. Each datapoint is calculated upon 20 repetitions.

TABLE 6. Experiment on split threshold.

| Metric | $10 \%$ | $20 \%$ | $30 \%$ |
| :-- | :-- | :-- | :-- |
| ARPR* | $93.88 \%$ | $93.58 \%$ | $94.28 \%$ |
| Average Rating | 3.56 | 3.56 | 3.56 |

Each experiment on a certain parameter listed in Table 3 is conducted while the others are set as default values.

## 1) ANALYSIS ON $C F$

The same experimental setting to the first experiment regarding split is used here. Three CF models, i.e. SVD [30], [42], SVD++ [43], and SlopeOne [44], are compared because of their outstanding performance in recommendation tasks.

Suggested by the results shown in Table 4, SVD++ outperforms the other two on all cases. Therefore, it is used as the CF model in related approaches.

## 2) ANALYSIS ON $K$

Experiments on $K$ are executed between CF-based and CF-based+ personalized search algorithms. Two conclusions can be drawn from the results given in Table 5.

1. When comparing the first column with the others, the CF-based+ approach outperforms the CF-based one; moreover, the strategy filtering out the items with too low estimated ratings and employing evaluated items to update CF-based probabilistic model is efficient.
2. CF-based+ approach, as well as the aforementioned strategy, is not sensitive to the number of categories $K$.

## 3) ANALYSIS ON split threshold

As introduced, a certain amount of training data is reserved for estimating $r_{\text {threshold }}$. The experiment on its percentage split threshold is performed. According to the experimental data detailed in Table 6, the conclusion similar to that of the

TABLE 7. Overall performance of compared algorithms.

| Dataset | Metric | CF-based | CF-based + | DPM-IEDA | content-based (SVR) | content-based (IGA) |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| MovieLens 20M | ARPR* | $75.94 \%$ | 87.77\% | $\mathbf{9 5 . 0 4 \%}$ | $48.87 \%$ | $46.11 \%$ |
|  | Average Rating | 3.55 | 3.64 | 3.71 | 3.27 | 3.26 |
|  | ILD** | 0.78 | 0.77 | 0.79 | 0.84 | 0.83 |
| Amazon Dataset <br> (Movie and TV 5-core) | ARPR | $90.16 \%$ | $95.55 \%$ | 97.53\% | $85.08 \%$ | $66.52 \%$ |
|  | Average Rating | 3.95 | 3.98 | 4.02 | 3.89 | 3.72 |
|  | ILD | 0.99 | 0.99 | 0.99 | 1.00 | 1.00 |

* Average Relative Performance Ratio (ARPR)
**Intra-List Distance (ILD)
This group of experiments is conducted on the proposed DPM-IEDA and the other four compared algorithms.
Each datapoint is calculated upon 30 repetitions.
![img-2.jpeg](img-2.jpeg)

FIGURE 3. Algorithm runtime.
experiment on $K$ is obtained. The proposed strategy involved in the CF-based + approach etc. is not sensitive to $s p l i t_{\text {threshold }}$ either.

## C. PERFORMANCE OF COMPARED ALGORITHMS

In this Section, content-based (IGA), content-based (SVR), CF-based, CF-based+ and the presented dual-probabilistic model based IEDA algorithms (DPM-IEDA) are compared on the aforementioned two tasks aiming at helping the users locate satisfactory movies and TV series given limited interactions, i.e., twenty iterations and twelve items in each iteration.

13337 standard compliant users from MovieLens 20M and 255 standard compliant users from Amazon Dataset (Movie and TV 5-core) are adopted to clearly analyze the performance of compared algorithms. All involved experiments are repeated thirty times.

Results w.r.t. the three indicators are shown in Table 7, and the average rating is bracketed after the number of found satisfactory items. The following observations are obtained:

1. The presented algorithm, DPM-IEDA outperforms all the other compared ones on ARPR and average rating. When considering the diversity (ILD), two contentbased methods (SVR and IGA) produce better performance than others, while the rest perform similarly.
2. When comparing the CF-based approach and the CF-based+ one, i.e. data in the third and fourth columns, it is easy to find that the proposed improvement on CF-based model is effective.
3. When the fourth and fifth columns come into focus, the improvement brought by the content-based probabilistic model is therefore noticed.
4. The worst performance is obtained by content-based (SVR) and content-based (IGA) personalized search methods, although their search results are of better diversity.
Meanwhile, the algorithm runtime is also recorded. Given the same limited iterations, the average time spent by these algorithms is calculated and then illustrated in the 2-D column chart in Fig. 3.

When considering the computational cost:

1. CF-based and CF-based+ approaches perform the best while the content-based ones (SVR and IGA) are the worst.
2. The proposed DPM-IEDA is in the mid-range position and of higher time cost. Since human customers are involved in the process and they are required to cooperate with algorithms, DPM-IEDA's performance is still acceptable.
3. The comparison between the DPM-IEDA and the content-based (IGA) experimentally proves the sparse problem caused by the too large encoding space and the limited feasible solutions, i.e. existing items. Moreover, the much longer run time is needed to locate the corresponding item to each coding.

## v. CONCLUSIONS

Two probabilistic models, i.e., CF-based and content-based ones, are utilized in the presented DPM-IEDA by involving two dissimilar information sources to more precisely model the user's preference on the searched items. Specifically, they cooperate to work in two loops. The outer-loop probabilistic model first filters out the items with estimated ratings lower than a threshold and updates itself according to user interaction in an iterative manner. This loop maintains a population for being selected by the inner-loop.

Apart from its duty of extracting knowledge from text descriptions, the inner-loop probabilistic model plays the rule as a surrogate to avoid user fatigue.

The presented DPM-IEDA is then applied to twenty cases from two main-stream dataset, and the results experimentally demonstrate its superiority in the effectiveness and efficiency

of helping user locate satisfactory items. Moreover, a better comprehensive experience, together with less user fatigue, is achieved.

In our future study, the diversity of the results offered by personalized search to users will be considered. On the other hand, the privacy-preserving personalized search will be studied to enlarge the application of these techniques since users concern more and more about their privacy.

## REFERENCES

[1] H. Takagi, "Interactive evolutionary computation: Fusion of the capabilities of EC optimization and human evaluation," Proc. IEEE, vol. 89, no. 9, pp. 1275-1296, Sep. 2001.
[2] M. Kuzma and G. Andrejková, "Interactive evolutionary computation in modelling user preferences," in Emergent Trends in Robotics and Intelligent Systems, P. Sincák, P. Hartono, M. Vieß́ková, J. Valcák, and R. Jakša, Eds. Cham, Switzerland: Springer, 2015, pp. 341-350.
[3] B. Xin, L. Chen, J. Chen, H. Ishibuchi, K. Hirota, and B. Liu, "Interactive multiobjective optimization: A review of the state-of-the-art," IEEE Access, vol. 6, pp. 41256-41279, 2018.
[4] M. Fukumoto and S. Koga, "A proposal for user's intervention in interactive evolutionary computation for optimizing fragrance composition," in HCI International-Posters' Extended Abstracts, vol. 434, C. Stephanidis, Ed. Cham, Switzerland: Springer, 2014, pp. 85-89.
[5] A. Oliver, O. Regragui, N. Monmarch, and G. Venturini, "Genetic and interactive optimization of web sites," in Proc. Int. World Wide Web Conf., vol. 1, 2002, p. 4.
[6] F. Ricci, L. Rokach, and B. Shapira, Recommender Systems: Introduction and Challenges. Boston, MA, USA: Springer, 2015, pp. 1-34. doi: 10.1007/978-1-4899-7637-6_1.
[7] T. K. Paradarami, N. D. Bastian, and J. L. Wightman, "A hybrid recommender system using artificial neural networks," Expert Syst. Appl., vol. 83, pp. 300-313, Oct. 2017.
[8] M. E. B. H. Kbaier, H. Masri, and S. Krichen, "A personalized hybrid tourism recommender system," in Proc. IEEE/ACS Int. Conf. Comput. Syst. Appl., Oct./Nov. 2018, pp. 244-250.
[9] M. E. Ibrahim, Y. Yang, D. L. Ndzi, G. Yang, and M. Al-Maliki, "Ontology-based personalized course recommendation framework," IEEE Access, vol. 7, pp. 5180-5199, 2019.
[10] Y. Li, "Adaptive learning evaluation model for evolutionary art," in Proc. IEEE Congr. Evol. Comput. (CEC), Jun. 2012, pp. 1-8.
[11] R. Kamalian, E. Yeh, Y. Zhang, A. M. Agogino, and H. Takagi, "Reducing human fatigue in interactive evolutionary computation through fuzzy systems and machine learning systems," in Proc. IEEE Int. Conf. Fuzzy Syst., Jul. 2006, pp. 678-684.
[12] T. Chugh, K. Sindhya, J. Hakanen, and K. Miettinen, "An interactive simple indicator-based evolutionary algorithm (I-SIBEA) for multiobjective optimization problems," in Evolutionary Multi-Criterion Optimization, A. Gaspar-Cunha, C. H. Antunes, and C. C. Coello, Eds. Cham, Switzerland: Springer, 2015, pp. 277-291.
[13] A. B. Ruiz, M. Luque, K. Miettinen, and R. Saborido, "An interactive evolutionary multiobjective optimization method: Interactive WASF-GA," in Evolutionary Multi-Criterion Optimization, A. GasparCunha, C. H. Antunes, and C. C. Coello, Eds. Cham, Switzerland: Springer, 2015, pp. 249-263.
[14] Y. Sun, W. Liu, R. Qiu, and C. Huang, "Research development of user interest modeling in China," J. Intell., vol. 32, no. 5, pp. 145-149, 2013.
[15] W. Guoxia and L. Heping, "Survey of personalized recommendation system," Comput. Eng. Appl., vol. 48, no. 7, pp. 66-76, 2012.
[16] M. Abou-Zleikha and N. Shaker, "Evolving random forest for preference learning," in Applications of Evolutionary Computation, A. M. Mora and G. Squillero, Eds. Cham, Switzerland: Springer, 2015, pp. 318-330.
[17] M. Abou-Zleikha, N. Shaker, and M. G. Christensen, "Preference learning with evolutionary multivariate adaptive regression spline model," in Proc. IEEE Congr. Evol. Comput. (CEC), May 2015, pp. 2184-2191.
[18] H.-T. Kim, E. Kim, J.-H. Lee, and C. W. Ahn, "A recommender system based on genetic algorithm for music data," in Proc. Int. Conf. Comput. Eng. Technol., vol. 6, 2010, pp. 414-417.
[19] V. Kant and K. K. Bharadwaj, "A user-oriented content based recommender system based on reclusive methods and interactive genetic algorithm," in Proc. 7th Int. Conf. Bio-Inspired Comput., Theories Appl. (BICTA), J. C. Bansal, P. K. Singh, K. Deep, M. Pant, and A. K. Nagar, Eds. New Delhi, India: Springer, 2013, pp. 543-554.
[20] X.-Y. Sun, Y.-N. Lu, D.-W. Gong, and K.-K. Zhang, "Interactive genetic algorithm with CP-nets preference surrogate and application in personalized search," Control Decis., vol. 30, no. 7, pp. 1153-1161, 2015.
[21] X. Sun, L. Zhu, L. Bao, L. Liu, and X. Nie, "Interactive genetic algorithm with group intelligence articulated possibilistic condition preference model," in Proc. Asia-Pacific Conf. Simulated Evol. Learn. Cham, Switzerland: Springer, 2017, pp. 158-169.
[22] Y. Chen, X. Sun, D. Gong, Y. Zhang, J. Choi, and S. Klasky, "Personalized search inspired fast interactive estimation of distribution algorithm and its application," IEEE Trans. Evol. Comput., vol. 21, no. 4, pp. 588-600, Aug. 2017.
[23] X. Sun, Y. Chen, L. Bao, and R. Xu, "Interactive genetic algorithm with implicit uncertainty evaluation for application in personalized search," in Proc. IEEE Symp. Ser. Comput. Intell. (SSCI), Nov./Dec. 2017, pp. 1-8.
[24] H. Mühlenbein and G. Paass, "From recombination of genes to the estimation of distributions I. Binary parameters," in Parallel Problem Solving from Nature-PPSN IV. Berlin, Germany: Springer, 1996, pp. 178-187.
[25] H. Mühlenbein, J. Bendisch, and H.-M. Voigt, "From recombination of genes to the estimation of distributions II. Continuous parameters," in Parallel Problem Solving from Nature-PPSN IV. Berlin, Germany: Springer, 1996, pp. 188-197.
[26] M. Pelikan, M. W. Hauschild, and F. G. Lobo, Estimation of Distribution Algorithms. Berlin, Germany: Springer, 2015.
[27] P. Larrahaga and J. A. Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation, vol. 2. Boston, MA, USA: Springer Science \& Business Media, 2002.
[28] M. Pelikan, D. E. Goldberg, and E. Cantú-Paz, "Linkage problem, distribution estimation, and Bayesian networks," Evol. Comput., vol. 8, no. 3, pp. 311-340, 2000.
[29] G. R. Harik, F. G. Lobo, and D. E. Goldberg, "The compact genetic algorithm," IEEE Trans. Evol. Comput., vol. 3, no. 4, pp. 287-297, Nov. 1999.
[30] Y. Koren and R. Bell, "Advances in collaborative filtering," in Recommender Systems Handbook. Boston, MA, USA: Springer, 2015, pp. 77-118.
[31] J. Delgado and N. Ishii, "Memory-based weighted majority prediction," in Proc. SIGIR Workshop Recomm. Syst. Circuses, 1999, pp. 137-158.
[32] M. Deshpande and G. Karypis, "Item-based top-n recommendation algorithms," ACM Trans. Inf. Syst., vol. 22, no. 1, pp. 143-177, 2004.
[33] D. M. Blei, A. Y. Ng, and M. I. Jordan, "Latent Dirichlet allocation," J. Mach. Learn. Res., vol. 3, pp. 993-1022, Mar. 2003.
[34] F. M. Harper and J. A. Konstan, "The movielens datasets: History and context," ACM Trans. Interact. Intell. Syst., vol. 5, no. 4, p. 19, Jan. 2016.
[35] J. McAuley, C. Targett, Q. Shi, and A. Van Den Hengel, "Image-based recommendations on styles and substitutes," in Proc. 36th Int. ACM SIGIR Conf. Res. Develop. Inf. Retr., 2015, pp. 43-52.
[36] H. Takagi, "Interactive evolutionary computation for analyzing human characteristics," in Emergent Trends in Robotics and Intelligent Systems, P. Sincák, P. Hartono, M. Vieß́ková, J. Valcák, and R. Jakša, Eds. Cham, Switzerland: Springer, 2015, pp. 189-195.
[37] H. Wang and K. Wong, "Personalized search: An interactive and iterative approach," in Proc. IEEE World Congr. Services, Jun./Jul. 2014, pp. 3-10.
[38] M. Sharma, "Preference modeling and accuracy in recommender systems," M.S. thesis, Univ. Minnesota, Minneapolis, MN, USA, Sep. 2017.
[39] X. Ning, C. Desrosiers, and G. Karypis, A Comprehensive Survey of Neighborhood-Based Recommendation Methods. Boston, MA, USA: Springer, 2015, pp. 37-76. doi: 10.1007/978-1-4899-7637-6_2.
[40] B. Smyth and P. McClave, "Similarity vs. Diversity," in Proc. Int. Conf. Cirac-Based Reasoning. Berlin, Germany: Springer, 2001, pp. 347-361.
[41] M. Zhang and N. Hurley, "Avoiding monotony: Improving the diversity of recommendation lists," in Proc. ACM Conf. Recommender Syst., 2008, pp. 123-130.
[42] S. Funk (Dec. 2006), Netflix Update: Try this at Home [Online]. Available: http://sifter.org/ simon/journal/20061211.html
[43] Y. Koren, "Factorization meets the neighborhood: A multifaceted collaborative filtering model," in Proc. 14th ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining, 2008, pp. 426-434.
[44] D. Lemire and A. Maclachlan, "Slope one predictors for online ratingbased collaborative filtering," in Proc. SIAM Int. Conf. Data Mining, 2005, pp. 471-475.

![img-6.jpeg](img-6.jpeg)

YANG CHEN is currently pursuing the Ph.D. degree in control theory and control engineering with the School of Information and Control Engineering, China University of Mining and Technology, China.
He is an Interactive Evolutionary Computation (IEC) Researcher with an interest in multiobjective optimization and machine learning.
![img-4.jpeg](img-4.jpeg)

XIAOYAN SUN received the Ph.D. degree in control theory and control engineering from the China University of Mining and Technology, in 2009.
She is currently a Professor with the School of Information and Control Engineering, China University of Mining and Technology. Her research interests include interactive evolutionary computation, big data, and intelligence optimization.
![img-5.jpeg](img-5.jpeg)

DUNWEI GONG received the B.S. degree in applied mathematics from the China University of Mining and Technology, Xuzhou, China, in 1992, the M.S. degree in control theory and its applications from the Beijing University of Aeronautics and Astronautics, Beijing, China, in 1995, and the Ph.D. degree in control theory and control engineering from the China University of Mining and Technology, in 1999.
He is currently a Professor and the Ph.D. Advisor with the School of Information and Electrical Engineering, China University of Mining and Technology. He is also with the School of Information Science and Technology, Qingdao University of Science and Technology, Qingdao, China. His main research interests include evolutionary computation, intelligence optimization, and data mining.
![img-6.jpeg](img-6.jpeg)

XIANGIUAN YAO was born in Hebei. She received the Ph.D. degree in control theory and control engineering from the China University of Mining and Technology, Xuzhou, Jiangsu, China, in 2011.
She is currently a Professor with the School of Science, China University of Mining and Technology. Her main research interest is search-based software testing and evolutionary computation.