# Using an Estimation of Distribution Algorithm to Achieve Multitasking Semantic Web Service Composition 

Chen Wang ${ }^{\oplus}$, Hui Ma ${ }^{\ominus}$, Member, IEEE, Gang Chen ${ }^{\ominus}$, Member, IEEE, and Sven Hartmann ${ }^{\ominus}$, Member, IEEE


#### Abstract

Web service composition composes existing Web services to accommodate users' requests for required functionalities with the best possible quality of services (QoS). Due to the computational complexity of this problem, evolutionary computation (EC) techniques have been employed to efficiently find composite services with near-optimal functional quality (i.e., quality of semantic matchmaking, QoSM for short) or nonfunctional quality (i.e., QoS) for each composition request individually. With a rapid increase in composition requests from a growing number of users, solving one composition request at a time can hardly meet the efficiency target anymore. Driven by the idea that the solutions obtained from solving one request can be highly useful for tackling other related requests, multitasking service composition approaches have been proposed to efficiently deal with multiple composition requests concurrently. However, existing attempts have not been effective in learning and sharing knowledge among solutions for multiple requests. In this article, we model the problem of collectively handling multiple service composition requests as a new multitasking service composition problem and propose a new permutation-based multifactorial evolutionary algorithm based on an estimation of distribution algorithm (EDA), named PMFEA-EDA, to effectively and efficiently solve this problem. In particular, we introduce a novel method for effective knowledge sharing across different service composition requests. For that, we develop a new sampling mechanism to increase the chance of identifying high-quality service compositions in both the single-tasking and multitasking contexts. Our experiment shows that our proposed approach, PMFEAEDA, takes much less time than existing approaches that process each service request separately, and also outperforms them in terms of both QoSM and QoS.


Index Terms-Combinatorial optimization, estimation of distribution algorithm (EDA), evolutionary multitasking, quality of services (QoS) optimization, Web service composition.

[^0]
## I. INTRODUCTION

SERVICE-ORIENTED computing employs the concept of Web services, i.e., self-describing Web-based applications that can be invoked over the Internet. Since a single Web service often fails to accommodate users' complex requirements, Web service composition [1] aims to loosely couple independent Web services in the form of service execution workflows, providing value-added functionalities to end-users. Web service composition is a promising research area and is highly desirable given the increasing number of services available in GIS [2], manufacturing [3], smartphone applications [4], [5], oil and gas industry [6], IoT applications [7], [8], logistics [9], and E-learning [10].

Since the service execution workflows are often unknown or not given in advance, many researchers have been interested in fully automated service composition that automatically constructs workflows with required functionalities while optimizing the overall quality of composite services. This overall quality usually refers to the functional quality (i.e., quality of semantic matchmaking, QoSM for short) or the nonfunctional quality (i.e., quality of service, QoS for short) of the composite services that stand for the service composition solutions [11]-[20].

The Web service composition problem has been proven to be NP-hard [21]. To tackle such a difficult problem, evolutionary computation (EC) techniques have been widely used to efficiently find near-optimal composition solutions in a cost-effective manner [12]-[20], [22]-[25]. These EC-based approaches are mainly designed to solve one service request at a time by improving users' quality preferences quantified in the form of either a single optimization objective [12], [14], [16]-[20], [25] or multiple objectives [13], [15], [22]-[24]. With the significant increase in the amount of service composition requests, a common disadvantage of these methods is that many service requests have to be dealt with repetitively and independently. In fact, similarities across these service requests that could be dealt with collectively have been consistently ignored by existing methods.

Many service requests have identical functional requirements on inputs and outputs but may vary due to different preferences on QoSM and/or QoS [26]. In a market-oriented environment, service composers often strategically group relevant service composition requests into several user segments (e.g., platinum, gold, silver, and bronze user segments), and


[^0]:    Manuscript received 28 August 2021; revised 29 December 2021 and 27 February 2022; accepted 18 April 2022. Date of publication 29 April 2022; date of current version 31 May 2023. This work was supported by the New Zealand Marsden Fund administrated by the Royal Society of New Zealand under Grant VUW1510. (Corresponding author: Chen Wang.)

    Chen Wang is with the HPC and Data Science Department, National Institute of Water and Atmospheric Research, Wellington 6021, New Zealand (e-mail: chen.wang@niwa.co.nz).

    Hui Ma and Gang Chen are with the School of Engineering and Computer Science, Victoria University of Wellington, Wellington 6041, New Zealand (e-mail: hui.ma@ecs.vuw.ac.nz; aaron.chen@ecs.vuw.ac.nz). Sven Hartmann is with the Department of Informatics, Clausthal University of Technology, 38678 Clausthal-Zellerfeld, Germany (e-mail: sven.hartmann@to-clausthal.de). This article has supplementary material provided by the authors and color versions of one or more figures available at https://doi.org/10.1109/TEVC.2022.3170899.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Two composite booking services produced by TripPlanner. (a) Composite booking service A. (b) Composite booking service B.
each user segment presents distinguishable preferences over the service composition requests. Therefore, one composite service (i.e., a service composition solution) for a user segment can comfortably satisfy requirements from all users belonging to the same segment. In other words, any new service requests arising from the same segment will be immediately served by the same composite service designed a priori for that segment.

Herein, we use an example to demonstrate composite services for different user segments. TripPlanner is a service composition design system that produces composite booking services for many travel companies. See an example of two composite booking services utilized by TripPlanner in Fig. 1. Both composite services can be used to book airlines, hotels, and local transportation for travelers. Both are also composed by existing Web services from thousands of available Web services over the Internet. In Fig. 1, some services composed in composite booking service A (i.e., Service 2: City Hotel Reservation Service and Service 3: Taxi Service) are different from those composed in composite booking service B (i.e., Service 4: City Luxury Hotel Service with Transportation). In particular, Service 4 aggregates the functionalities of Service 2 and Service 3, providing high-quality hotel and taxi services. Apart from that, the cost of Service 4 (i.e., 32 cents) is much higher than that of Service 2 and Service 3 (i.e., $8+5=13$ cents). Apparently, these two composite booking services differ in QoSM and QoS. This is important to cater for different users with varied QoSM and QoS requirements. For example, large international travel companies (i.e., platinum segment users of TripPlaner) often care about their customers' needs more than small local travel companies (i.e., bronze segment users of TripPlaner), by providing high-quality services. These high-quality services contribute to a reliable and accurate user experience. In other words, composite services with high QoSM as employed by composite service B in Fig. 1 are preferably considered by the platinum segment users. In contrast, composite services with low QoSM with a tradeoff in cost, such as the composite booking service A, is preferred by bronze segment users of small local travel companies. From the perspective of service providers, they should distinguish
different types of companies and provide different segment offers (i.e., composite services) to different segments.

The problem demonstrated above is clearly a multitasking problem. In line with this problem, we specifically consider multiple related service composition tasks, each of which corresponds to a separate user segment with different preferences (e.g., QoSM preference). A very recent work [26] proposed to handle such problems with multiple user segments collectively, where each segment captures the vital preference differences in terms of QoSM. They also adopted an emerging EC computing paradigm, namely, the multifactorial evolutionary algorithm (MFEA) [27]. Building on MFEA, a permutation-based MFEA (PMFEA) was developed to support intertask solution sharing via assortative mating. This is particularly achieved by using crossover and mutation operators. See Algorithm 3 in Appendix A for technical details.

However, empirical studies showed that the performance gain achievable by PMFEA is not prominent in comparison to single-tasking algorithms, indicating that assortative mating has limited effectiveness in promoting constructive intertask knowledge sharing. To tackle this limitation, we will propose a new technique to extract knowledge jointly from promising solutions to different tasks in the form of a series of related node histogram matrices (NHMs). The learned NHMs can be further utilized by the estimation of distribution algorithm (EDA) to search for promising regions of the solution space effectively. Note that existing EDA-based approaches for service composition have never been designed to extract and utilize knowledge from multiple tasks. In this article, we will propose the first PMFEA based on EDA (PMFEA-EDA) to simultaneously solve several fully automated service composition tasks for multiple user segments. PMFEA-EDA features the use of innovative intertask knowledge sharing techniques and solution sampling methods, all designed to improve the effectiveness and efficiency of the algorithm for multitasking service composition. The contributions of this article are as follows.

1) We propose a new algorithm (named PMFEA-EDA) to handle multiple service requests with respect to several predetermined user segments jointly. Our algorithm significantly outperforms existing methods by explicitly learning and sharing knowledge across solutions for different service requests (i.e., tasks). Particularly, PMFEAEDA iteratively builds a set of single-tasking NHMs. Each NHM captures the knowledge of good solutions with respect to one task. Meanwhile, to facilitate knowledge sharing across different tasks, PMFEA-EDA also learns multitasking NHMs in association with every two tasks with similar preferences on QoSM (i.e., adjacent tasks). To the best of our knowledge, this is the first time that a combined set of single-tasking and multitasking NHMs is utilized for effectively handling the multitasking optimization problem.
2) We propose a new sampling mechanism over a combined set of single-tasking and multitasking NHMs to construct new composite services from these NHMs. This new sampling mechanism inspired by the principle of assortative mating in [27] is introduced in PMFEA-EDA to overcome the difficulty of using the node histogram-based sampling

(NHBSA) algorithm in a multitasking context. By using this mechanism, we can also effectively maintain high population diversity and prevent our method from premature convergence. To the best of our knowledge, this is the first time that sampling over a combined set of single-tasking and multitasking NHMs is used to balance between exploration and exploitation of the evolutionary search process in a multitasking context.
3) We evaluate the effectiveness and efficiency of our proposed approach by conducting experiments to compare it against state-of-the-art approaches, including a pure multitasking one, a pure single-tasking one, and a nonevolutionary one. We also analyze the effectiveness of knowledge sharing across adjacent tasks in terms of its impact on the aggregated quality of obtained solutions for the different tasks. This is achieved by experimentally comparing PMFEA-EDA without knowledge sharing (named PMFEA-EDA-WOT) with PMFEA-EDA.
The remainder of this article is organized as follows. Section II reviews some related work on semiautomated/fully automated Web service composition problems in singletasking and multitasking contexts. Section III formulates service composition problems in single-tasking and multitasking contexts. Section IV presents an overview of the proposed PMFEA-EDA method and illustrates important components of this method. Section V demonstrates the effectiveness and efficiency of our PMFEA-EDA by comparing it against recent algorithms. Section VI discusses the main conclusions reached by our contribution and insights that guide the future work.

## II. Related Work

Web service composition is performed using two strategies: 1) semiautomated Web service composition and 2) fully automated Web service composition. The first one assumes a predefined service composition workflow, which consists of abstract service slots that specify the required functionalities for atomic Web services, is known and selects an atomic service for each of the abstract service slots. The second one does not assume a workflow of abstract service slots is known and constructs a workflow simultaneously with atomic service selection. Apparently, compared to semiautomated Web service composition, fully automated Web service composition is more difficult, but it also opens new opportunities to improve QoS and QoSM without being restricted to a predefined workflow.

## A. Literature on Single-Tasking Semiautomated Approaches

Non-EC service composition techniques try to identify optimal composite services by using some general optimization techniques, such as integer linear programming (ILP), dynamic programming, and reinforcement learning. However, due to the larger number of decision variables, nonEC service composition techniques, such as ILP, may lead to exponentially increased complexity and cost in computation [28]. Besides that, QoS of composite services in ILPbased approaches is calculated by summing up the individual QoS score of every component service. Such a QoS calculation is not always appropriate. Machine learning approaches have been proposed for service composition. Wang et al. [29],
[30] and Liang et al. [31] developed service composition approaches based on deep reinforcement learning to adaptively construct composite services at the execution stage in response to QoS changes. However, these approaches only work for semiautomated service composition, where a composite service workflow must be provided in advance by users. As we have seen above, none of these existing works on automated Web service composition can solve multiple semantic service requests with different QoSM constraints. Therefore, effective and efficient approaches are needed to solve multitasking semantic service composition.

A variety of EC techniques has been demonstrated to be highly promising in solving single-tasking semiautomated Web service composition. This is because EC techniques are particularly useful in practice as they can efficiently find "good enough" (i.e., near-optimal) composite services. Based on the number of objectives to be optimized via these EC techniques, two subgroups of works are classified, i.e., single-tasking single-objective and single-tasking multiobjective EC-based semiautomated Web service composition. One subgroup aims to find composite services with an optimized unified score. For example, some works jointly optimize QoS and QoSM as an unified score [32]-[34]. The other subgroup aims to produce a set of tradeoff composite services with different objectives, e.g., time and cost [35].

The single objective and multiple objectives are optimized using various EC techniques, e.g., genetic algorithm (GA) [33], [35]-[37] and particle swarm optimization (PSO) [23], [38]. For example, Wada et al. [36] investigates a semiautomated approach with a vector-based representation in multiobjective GA. Two multiobjective GAs (called $E^{3}$ MOGA and $\mathrm{X}-E^{3}$ ) are proposed in this work. Particularly, $E^{3}$-MOGA is designed to search for equally distributed Paretooptimal solutions in the multiobjective space, while $\mathrm{X}-E^{3}$ is designed to search for Pareto-optimal solutions that can reveal the maximum range of tradeoffs, covering extreme solutions in the search space.

## B. Literature on Multitasking Semiautomated Approaches

A new EC computing paradigm, namely, MFEA [27], has been introduced recently. MFEA can solve multiple combinatorial optimization tasks concurrently and produce multiple solutions, with one for each task. MFEA searches a unified search space based on a unified random-key representation over multiple tasks and transfers implicit knowledge of promising solutions through the use of simple genetic operators across multiple tasks. The implicit knowledge transformation is achieved by performing crossover on two randomly selected parents solutions from two different tasks. This mechanism is called assortative mating. Apart from that, offspring is only evaluated on one task that is determined by its parents based on vertical cultural transmission. See Algorithm 3 in Appendix A and Algorithm 4 in Appendix B for technical details.

MFEA has shown its efficiency and effectiveness in several problem domains [11], [39]-[41]. To meet the efficiency and cost requirements, Bao et al. [11] reported the first attempt that employs MFEA to solve multiple service composition tasks together. Bao et al. [11] optimized QoS for two unrelated service requests simultaneously using MFEA,

achieving competitive results compared to single-objective EC techniques. However, this work cannot support fully automated service composition, where the service execution workflow is unknown or not given by the users. Furthermore, the number of tasks to be optimized concurrently is relatively small (i.e., two tasks). In this article, we will propose an MFEA (PMFEA) to solve more than two fully automated service composition tasks concurrently.

## C. Literature on Single-Tasking Fully Automated Approaches

Graph search [42]-[47] is an alternative approach to fully automated service composition. Graph search works on searching composite services, which are constructed by subgraphs or paths from a service dependency graph. Constructing such a service dependency graph may suffer from the scalability issue when dealing with a large service repository with complex service dependencies. This issue can get even worse when QoS optimization is considered [48]. To consider multiple quality criteria in QoS, a recent work, named PathSearch [43], proposes an improved path-based search method over a graph [42]. Particularly, a node (i.e., an atomic service) associated with a higher rank is preferred in a path construction, and nodes are ranked based on the concept of dominance over multiple QoS quality criteria. In this article, we will compare PMFEA-EDA with the state-of-the-art graph search technique, i.e., PathSearch [43].

Evolutionary single-tasking fully automated service composition has been well studied in the majority of existing EC-based works. In particular, each service composition request is processed independently by using singleobjective [12], [14], [16], [17], [19], [25] or multiobjective EC techniques [13], [15].
In the single-objective single-tasking setting, most of the existing service composition approaches used conventional EC techniques, which rely on the use of the implicit knowledge of promising solutions based on one or more variations of genetic operators on parent individuals. For example, tree-based composite solutions in [12], [14], [19], and [25] are produced using implicit knowledge defined by one or more variations of GPbased genetic operators on parent individuals. Apart from these conventional EC techniques, other approaches, such as [20], sample high-quality composite solutions using explicit knowledge that is learned by a distribution model, e.g., NHM. Their experiment demonstrates that learning an NHM of promising solutions does help to find near-optimal solutions. In the multiobjective single-tasking settings, there are very limited works, to the best of our knowledge, [13], [15], and [24] are the three recent attempts along this research direction. Very recently, an EDA-guided local search has been proposed that constructs distribution models from suitable Pareto front solutions and other good candidate solutions [24]. This approach can effectively and efficiently produce much better Pareto optimal solutions compared to other state-of-the-art methods [13], [15].

## D. Literature on Multitasking Fully Automated Approaches

As discussed in Section II-B, Bao et al. [11] reported the first attempt to optimize QoS for two unrelated service

Authorized licensed use limited to: Univ Politecnica de Madrid. Downloaded on July 29,2024 at 16:05:15 UTC from IEEE Xplore. Restrictions apply.
requests simultaneously in semiautomated service composition. To overcome the limitations in [11], [26] proposed an MFEA (PMFEA) to solve more than two fully automated service composition tasks concurrently. Compared to singletasking approaches, this method requires only a fraction of time. However, this work did not significantly outperform single-tasking approaches in finding high-quality solutions through the use of implicit learning. Motivated by the existing attempts to address multitasking service composition problems, with the aim to jointly find high-quality solutions for all tasks. In this article, we will propose a PMFEA-EDA to support explicit knowledge learning and explicit knowledge sharing across different tasks.

## III. Preliminaries

## A. Single-Tasking Semantic Web Service Composition

We review the formulation of the single-tasking semantic Web service composition problem. The following definitions are also given in [20].

A semantic Web service (service, for short) is considered as a tuple $S=\left(I_{S}, O_{S}, Q o S_{S}\right)$ where $I_{S}$ is a set of service inputs that are consumed by $S, O_{S}$ is a set of service outputs that are produced by $S$, and $Q o S_{S}=\left\{t_{S}, c t_{S}, r_{S}, a_{S}\right\}$ is a set of nonfunctional attributes of $S$. The inputs in $I_{S}$ and outputs in $O_{S}$ are parameters modeled through concepts in a domain-specific ontology $\mathcal{O}$. The attributes $t_{S}, c t_{S}, r_{S}$, and $a_{S}$ refer to the response time, cost, reliability, and availability of service $S$, respectively, which are four commonly used QoS attributes [49].

A service repository $\mathcal{S R}$ is a finite collection of services supported by a common ontology $\mathcal{O}$.

A composition task (also called service request) over a given $\mathcal{S R}$ is a tuple $T=\left(I_{T}, O_{T}\right)$ where $I_{T}$ is a set of task inputs, and $O_{T}$ is a set of task outputs. The inputs in $I_{T}$ and outputs in $O_{T}$ are parameters that are semantically described by concepts in the ontology $\mathcal{O}$. Two special atomic services Start $=\left(\emptyset, I_{T}, \emptyset\right)$ and End $=\left(O_{T}, \emptyset, \emptyset\right)$ are always included in $\mathcal{S R}$ to account for the input and output of a given composition task $T$.

We use matchmaking types to describe the level of a match between outputs and inputs [50]. For concepts $\mathfrak{a}$ and $\mathfrak{b}$ in $\mathcal{O}$, the matchmaking returns exact if $\mathfrak{a}$ and $\mathfrak{b}$ are equivalent ( $\mathfrak{a} \equiv \mathfrak{b}$ ), plugin if $\mathfrak{a}$ is a subconcept of $\mathfrak{b}(\mathfrak{a} \subseteq \mathfrak{b})$, subsume if $\mathfrak{a}$ is a superconcept of $\mathfrak{b}(\mathfrak{a} \supseteq \mathfrak{b})$, and fail if none of the previous matchmaking types is returned. In this article, we are only interested in exact and plugin matches for robust compositions. As argued in [34], plugin matches are less preferable than exact matches due to the overheads associated with data processing. For plugin matches, the semantic similarity of concepts is suggested to be considered when comparing different plugin matches.

A robust causal link [51] is a link between two matched services $S$ and $S^{\prime}$, denoted as $S \rightarrow S^{\prime}$, if an output $\mathfrak{a}\left(\mathfrak{a} \in O_{S}\right)$ of $S$ serves as the input $\mathfrak{b}\left(\mathfrak{b} \in O_{S^{\prime}}\right)$ of $S^{\prime}$ satisfying either $\mathfrak{a} \equiv \mathfrak{b}$ or $\mathfrak{a} \subseteq \mathfrak{b}$. For concepts $\mathfrak{a}$ and $\mathfrak{b}$ in $\mathcal{O}$, the semantic similarity $\operatorname{sim}(\mathfrak{a}, \mathfrak{b})$ is calculated based on the edge counting method in a taxonomy like WorldNet [52]. Advantages of this method are simple calculation and accurate measure [52]. Therefore, the matchmaking type and semantic similarity of a robust causal

TABLE I
QoS Calculation for a Composite SErvice Expression $C$


link are defined as follows:

$$
\begin{aligned}
& \text { type }_{\text {link }}=\left\{\begin{array}{ll}
1 & \text { if } \mathfrak{a} \equiv \mathfrak{b} \text { (exact match) } \\
p & \text { if } \mathfrak{a} \subseteq \mathfrak{b} \text { (plugin match) } \\
& \operatorname{sim}_{\text {link }}=\operatorname{sim}(\mathfrak{a}, \mathfrak{b})=\frac{2 N_{\mathfrak{c}}}{N_{\mathfrak{a}}+N_{\mathfrak{b}}}
\end{array}\right.
\end{aligned}
$$

with a suitable parameter $p, 0<p<1$, and with $N_{\mathfrak{a}}, N_{\mathfrak{b}}$, and $N_{\mathfrak{c}}$, which measure the distances from concept $\mathfrak{a}$, concept $\mathfrak{b}$, and the closest common ancestor $\mathfrak{c}$ of $\mathfrak{a}$ and $\mathfrak{b}$ to the top concept of the ontology $\mathcal{O}$, respectively. However, if more than one pair of matched output and input exist from service $S$ to service $S^{\prime}$, type $_{e}$ and $\operatorname{sim}_{e}$ will take on their average values.

The QoSM of a composite service is obtained by aggregating over all the robust causal links as follows:

$$
\begin{aligned}
\mathrm{MT} & =\prod_{j=1}^{m} \operatorname{type}_{\operatorname{link}_{j}} \\
\mathrm{SIM} & =\frac{1}{m} \sum_{j=1}^{m} \operatorname{sim}_{\operatorname{link}_{j}}
\end{aligned}
$$

Formal expressions as in [53] are used to represent service compositions. The constructors $\bullet \cdot, \|,+$, and $*$ are used to denote sequential composition, parallel composition, choice, and iteration, respectively. The set of composite service expressions is the smallest collection $\mathcal{S C}$ that contains all atomic services and that is closed under sequential composition, parallel composition, choice, and iteration. That is, whenever $C_{0}, C_{1}, \ldots, C_{d}$ are in $\mathcal{S C}$, then $\bullet\left(C_{1}, \ldots, C_{d}\right),\left\|\left(C_{1}, \ldots, C_{d}\right)\right.$, $+\left(C_{1}, \ldots, C_{d}\right)$, and $* C_{0}$ are in $\mathcal{S C}$, too. Let $C$ be a composite service expression. If $C$ denotes an atomic service $S$, then its QoS is given by $Q o S_{S}$. Otherwise, the QoS of $C$ can be obtained inductively as summarized in Table I. Herein, $p_{1}, \ldots, p_{d}$ with $\sum_{k=1}^{d} p_{k}=1$ denote the probabilities of the different options of the choice + , while $\ell$ denotes the average number of iterations. Therefore, QoS of a composite service, i.e., availability $(A)$, reliability $(R)$, execution time $(T)$, and $\operatorname{cost}(C T)$, can be obtained by aggregating $a_{C}, r_{C}, t_{C}$, and $c t_{C}$ as in Table I.

In the presentation of this article, we mainly focus on two constructors, sequence $\bullet$ and parallel $\|$, similar as most automated service composition works [14], [54]-[56] do, where composite services are represented as directed acyclic graphs (DAGs). The nodes of the DAG correspond to those services (also called component services) in service repository $\mathcal{S} \mathcal{R}$ that are used in the composition. Let $\mathcal{G}=(V, E)$ be a DAGbased service composition solution from Start to End, where nodes correspond to the services and edges correspond to the
matchmaking quality between the services. Often, $\mathcal{G}$ does not contain all services in $\mathcal{S} \mathcal{R}$. The decoded DAG allows easy calculation of QoS in Table I and presents users with a complete workflow of service execution [20]. For example, the response time of a composite service is the time of the most time-consuming path in the DAG.

When multiple quality criteria are involved in decision making, the fitness of a solution is defined as a weighted sum of all individual criteria in (5), assuming the preference of each quality criterion based on its relative importance is provided by the user [57]

$$
\begin{aligned}
F(C)= & w_{1} \mathrm{ATT}+w_{2} \mathrm{SIM}+w_{3} \hat{A} \\
& +w_{4} \hat{R}+w_{5}(1-\hat{T})+w_{6}(1-\hat{C T})
\end{aligned}
$$

with $\sum_{k=1}^{6} w_{k}=1\left(w_{k} \geq 0\right)$. This objective function is defined as a comprehensive quality model for service composition. We can adjust the weights according to the user's preferences. $\overline{\mathrm{MT}}, \overline{\mathrm{SIM}}, \hat{A}, \hat{R}, \hat{T}$, and $\hat{C T}$ are normalized values calculated within the range from 0 to 1 using (6). To simplify the presentation, we also use the notation $\left(Q_{1}, Q_{2}, Q_{3}, Q_{4}, Q_{5}, Q_{6}\right)=(\mathrm{MT}, \mathrm{SIM}, A, R, T, C T) . Q_{1}$ and $Q_{2}$ have a minimum value of 0 and a maximum value of 1. The minimum and maximum value of $Q_{3}, Q_{4}, Q_{5}$, and $Q_{6}$ are calculated across all the relevant services, which are discovered using a greedy search technique in [14] and [54]

$$
\hat{Q}_{k}= \begin{cases}\frac{Q_{k}-Q_{k, \min }}{Q_{k, \max }-Q_{k, \min }}, & \text { if } k=1, \ldots, 4 \text { and } Q_{k, \max }-Q_{k, \min } \neq 0 \\ \frac{Q_{k, \max }-Q_{k}}{Q_{k, \max }-Q_{k, \min }}, & \text { if } k=5,6 \text { and } Q_{k, \max }-Q_{k, \min } \neq 0 \\ 1 & \text { otherwise. }\end{cases}
$$

The goal of single-tasking Web semantic service composition is to find a composite service expression $C^{*}$ that maximizes the objective function in (5). $C^{*}$ is hence considered as the best solution for a given composition task $T$.

## B. Multitasking Semantic Web Service Composition

In this article, we study the semantic Web service composition problem for multiple user segments with different QoSM preferences (henceforth, referred to as WSC-MQP). This problem is also defined in [26]. WSC-MQP is perceived as an evolutionary multitasking problem that aims to optimize $K$ composition tasks concurrently with respect to $K$ user segments.

Different from the composition task defined in the singletasking context, a composition task in the multitasking context

![img-1.jpeg](img-1.jpeg)

Fig. 2. Example of the neighborhood structure over four tasks.
is a tuple $T_{j}=\left(I_{T}, O_{T}\right.$, interval $\left._{j}\right)$ where $I_{T}$ is a set of task inputs, $O_{T}$ is a set of task outputs, and interval ${ }_{j}$ is an interval based on QoSM for $j \in\{1,2, \ldots, K\}$. The inputs in $I_{T}$ and outputs in $O_{T}$ are parameters that are semantically described by concepts in an ontology $\mathcal{O}$. The interval interval $i=$ $\left(\mathrm{QoSM}_{j}^{\mathrm{a}}, \mathrm{QoSM}_{j}^{\mathrm{b}}\right], j \in\{1,2, \ldots, K\}$ and $\mathrm{QoSM}_{j}^{\mathrm{a}}$ and $\mathrm{QoSM}_{j}^{\mathrm{b}}$ are lower and upper bounds of QoSM for each user segment. Different user segments can be distinguished by their preferences on QoSM. The preferences of each user segment are defined as an interval, such as $Q o S M \in(0.75,0.1]$.

Wang et al. [26] introduced a neighborhood structure over $T_{j}$, where $j \in\{1,2, \ldots, K\}$. This neighborhood structure is determined based on the tasks whose segment preferences on QoSM are adjacent to each other. For example, in Fig. 2, we consider $K=4$ and let $T_{1}, T_{2}, T_{3}$, and $T_{4}$ be the four composition tasks corresponding to interval ${ }_{1} \in(0,0.25]$, interval ${ }_{2} \in$ $(0.25,0.5]$, interval $_{3} \in(0.5,0.75]$, and interval ${ }_{4} \in(0.75,1]$, respectively. Therefore, the adjacent tasks of $T_{2}$ are $T_{1}$ and $T_{3}$, whose segment preference on QoSM (i.e., interval ${ }_{1}$ and interval $_{3}$ ) is adjacent to that of $T_{2}$ (i.e., interval ${ }_{2}$ ).

The goal of multitasking semantic Web service composition is to find the $K$ best solutions concurrently with one for each user segment.

## C. Multifactorial Optimization

MFEA is a new evolutionary paradigm that considers $K$ optimization tasks concurrently, where each task affects the evolution of a single population. In MFEA, a unified representation for the $K$ tasks allows a unified search space made for all the $K$ tasks. This unified representation of solutions can be decoded into solutions of the individual tasks. The following definitions are also given in [27] and capture the key attributes associated with each individual $\Pi$. For simplicity, we assume that all the tasks are maximization problems (see details in Section III-B).

Definition 1: The factorial cost $f_{j}^{\Pi}$ of individual $\Pi$ measures the fitness value with respect to the $K$ tasks, where $j \in\{1,2, \ldots, K\}$.

Definition 2: The factorial rank $r_{j}^{\Pi}$ of individual $\Pi$ on task $T_{j}$, where $j \in\{1,2, \ldots, K\}$, is the position of $\Pi$ in the population sorted in descending order according to their factorial cost with respect to task $T_{j}$.

Definition 3: The scalar fitness $\varphi^{\Pi}$ of individual $\Pi$ is calculated based on its best factorial rank over the $K$ tasks, which is given by $\varphi^{\Pi}={ }^{1} / \min _{i=1,2, \ldots, K i\}^{n}}$.

Definition 4: The skill factor of individual $\Pi$ denotes the most effective task of the $K$ tasks, and is given by $\tau^{\Pi}=$ $\operatorname{argmin}_{j}\left\{r_{j}^{\Pi}\right\}$, where $j \in\{1,2, \ldots, K\}$.

Based on the scalar fitness, evolved solutions in a population can be compared across the $K$ tasks. In particular, an individual associated with a higher scalar fitness is considered to be better. Therefore, multifactorial optimality is defined as follows.

Definition 5: An individual $\Pi^{\star}$ associated with factorial cost $\left\{f_{1}^{\star}, f_{2}^{\star}, \ldots, f_{K}^{\star}\right\}$ is optimal iff $\exists j \in\{1,2, \ldots, K\}$ such that $f_{j}^{\star} \geq$ $f_{j}(\Pi)$, where $\Pi$ denotes any feasible solution on task $T_{j}$.

## IV. PMFEA-EDA METHOD

We first present an outline of PMFEA-EDA for WSCMQP in Section IV-A. Subsequently, we will discuss the two main innovations of this method: 1) constructing and learning NHMs for effective exploration of the solution space over multiple tasks and 2) a new sampling mechanism to balance the tradeoff between exploration and exploitation in a multitasking context.

To learn a single-tasking NHM with respect to each task, we assign composite solutions to different solution pools based on their skill factors. Therefore, every solution pool stores promising solutions for one task. On the other hand, as shown in [26], solutions that are promising for one task can be used to evolve new solutions for its adjacent tasks (whose QoSM preferences are close). Due to this reason, we also prepare additional solution pools to store solutions that are promising for every two adjacent tasks. Every two adjacent tasks are identified as the most suitable tasks for knowledge sharing. Therefore, learning multitasking NHMs of these additional pools allows knowledge to be shared across adjacent tasks (see details in Section IV-C).

Moreover, we propose a sampling mechanism to balance exploration and exploitation. Particularly, a random sampling probability (rsp) is predefined to determine which NHM will be used to build new solutions. This mechanism is inspired by assortative mating in [27], where a random probability is defined for the occurrence of crossover on two parent solutions from the same skill factor or different skill factors.

The generation updates used in PMFEA-EDA are illustrated in Fig. 3. From the current population in Fig. 3, one sampled offspring population is created and further combined with the current population to produce the next population that only keeps the fittest solutions. Particularly, this sampled offspring population is formed from new solutions that are sampled from both single-tasking and multitasking NHMs. These NHMs are learned from multiple solution pools that consist of solutions assigned based on their skill factors.

## A. Outline of PMFEA-EDA

The outline of PMFEA-EDA is shown in Algorithm 1. We first randomly initialize $m$ permutation-based $\Pi_{k}^{g}$ solutions, where $0 \leq k<m$ and $g=0$. Each solution is represented as a random sequence of service indexes ranging from 0 to $|\mathcal{S R}|-1$, and $\mathcal{S R}$ is a service repository containing registered Web services. For example, a permutation is represented as $\Pi=\left(\pi_{1}, \ldots, \pi_{t}, \ldots, \pi_{n}\right)$ such that $\pi_{b} \neq \pi_{d}$ for all $b \neq d$. Every permutation-based solution will be decoded into a DAG-based solution $\hat{\varphi}_{k}^{\mathrm{g}}$ for interpreting its service execution

![img-2.jpeg](img-2.jpeg)

Fig. 3. Generation updates in PMFEA-EDA.

## Algorithm 1: PMFEA-EDA for WSC-MQP

Input : $T_{j}, K$, and $g_{\max }$
Output: A set of composition solutions
Randomly initialize population $\mathcal{P}^{g}$ of $m$ permutations $\Pi_{k}^{g}$ as solutions (where $g=0$ and $k=1, \ldots, m$ );
2: Decode each $\Pi_{k}^{g}$ into DAG $\mathcal{G}_{k}^{g}$ using the decoding method;
3: Calculate $f_{j}^{\Pi_{k}^{g}}, r_{j}^{\Pi_{k}^{g}}, \varphi^{\Pi_{k}^{g}}$ and $\tau^{\Pi_{k}^{g}}$ of $\Pi_{k}^{g}$ over $T_{j}$, where $j \in\{1,2, \ldots, K\}$
4: $\quad$ Encode each solution $\Pi_{k}^{g}$ in $\mathcal{P}^{g}$ with another permutation $\Pi_{k}^{g} ;$
5: while $g<g_{\max }$ do
6: $\quad$ Generate offspring population $\mathcal{P}_{o}^{g+1}$ via multiple NHMs learning and sampling using Algorithm 2 ;
7: Decode solutions in $\mathcal{P}_{o}^{g+1}$ into DAG $\mathcal{G}_{k}^{g+1}$ using the decoding method;
8: Calculate $f^{\Pi_{k}^{g+1}}$ of solutions in $\mathcal{P}_{o}^{g+1}$ on the selected tasks related to the skill factors determined in its corresponding NHM;
9: $\quad$ Encode each solution $\Pi_{k}^{g}$ in $\mathcal{P}^{g}$ with an another permutation $\Pi_{k}^{g}$;
10: $\mathcal{P}^{g+1}=\mathcal{P}^{g} \cup \mathcal{P}_{o}^{g+1}$;
11: Update $r_{j}^{\Pi_{k}^{g+1}}, \varphi^{\Pi_{k}^{g+1}}$ and $\tau^{\Pi_{k}^{g+1}}$ of offspring in $\mathcal{P}^{g+1}$;
12: Keep top half the fittest individuals in $\mathcal{P}^{g+1}$ based on $\varphi^{\Pi_{k}^{g+1}}$
13: Return the best $\Pi_{j}^{\star}$ over all the generations for $T_{j}$;
workflow using a decoding method proposed in [17]. Based on $\mathcal{G}_{k}^{g}$, we can easily determine $f_{j}^{\Pi_{k}^{g}}, r_{j}^{\Pi_{k}^{g}}, \varphi^{\Pi_{k}^{g}}$, and $\tau^{\Pi_{k}^{g}}$ of $\Pi_{k}^{g}$ over task $T_{j}$, where $j \in\{1,2, \ldots, K\}$. Afterward, we encode each solution $\Pi_{k}^{g}$ in $\mathcal{P}^{g}$ into another permutation $\Pi_{k}^{g}$ based on its decoded DAG form $\mathcal{G}_{k}^{g}$ (see details in Section IV-B). This encoding step is essential and enables reliable and accurate learning of an NHM [20]. The iterative part of PMFEA-EDA comprises lines $6-12$, which are repeated until a maximum
generation $g_{\max }$ is reached. During each iteration, we generate an offspring population $\mathcal{P}_{o}^{g+1}$ via multiple NMHs using Algorithm 2 (see details in Section IV-C). Again, the same decoding and encoding techniques are employed to these solutions in $\mathcal{P}_{o}^{g+1}$. Afterward, we evaluate the fitness $f^{\Pi_{k}^{g+1}}$ of solutions in $\mathcal{P}_{o}^{g+1}$ on the task related to the imitated tasks skill factor, which is determined based on the principle of vertical culture transmission [27]. In particular, the skill factor of every produced solution is determined based on its corresponding NHM, where it is sampled from. We then produce the next population $\mathcal{P}^{g+1}$ by combining the current population $\mathcal{P}^{g}$ and the offspring population $\mathcal{P}_{o}^{g}$. Consequently, we update $r_{j}^{\Pi_{k}^{g+1}}, \varphi^{\Pi_{k}^{g+1}}$, and $\tau^{\Pi_{k}^{g+1}}$ of the combined population $\mathcal{P}^{g+1}$, and keep half of the population $\mathcal{P}^{g+1}$ based on $\varphi^{\Pi_{k}^{g+1}}$. When the maximum generation $g_{\max }$ is reached, the algorithm returns the best $\Pi_{j}^{\star}$ over all the generations for $T_{j}$.

## B. Permutation-Based Representation

Permutations were utilized in the domain of fully automated service composition to indirectly represent a set of service composition solutions [16], [26]. Such a permutation, however, needs to be interpreted. For that, a forward graph building algorithm [17] is used to map a permutation to a DAG.

Since different permutations could be mapped to the same DAG, these permutations can lead to conflicts in learning the knowledge of service positions for one composition solution in NHM. As suggested in [20], we encode the permutation into a nearly unique and more reliable service permutation based on the decoded DAG, compared to its original permutation. Particularly, we produce this new permutation by combining two parts. One part comprises indexes of component services in the DAG, sorted in ascending order based on the longest distance from Start to every component service of the DAG while the second part comprises indexes of the remaining services in the permutation not utilized by the DAG (see details in [20]).

Example 1: Let us consider a composition task $T=$ $(\{a, b\},\{e, f\})$ and a service repository $\mathcal{S} \mathcal{R}$ consisting of six atomic services: $S_{0}=(\{e, f\},\{g\}, Q o S_{S_{0}}), S_{1}=(\{b\},\{c, d\}$,

## Algorithm 2: Multiple NHMs Learning and Sampling Over $K$ Tasks

Input : $\mathcal{P}^{g}$
Output: $\mathcal{P}_{a}^{g+1}$

1: Initialize a set of empty $\mathcal{A}_{q}$ for each task and every two adjacent tasks;
2: Assign each solution $\Pi_{k}^{\gamma g}$ in $\mathcal{P}^{g}$ to $\mathcal{A}_{q}$ based on its skill factor $\varphi^{\Pi_{k}^{\gamma g}}$;
3: Learn $2 K-1 \mathrm{NHMs} \mathcal{N} \mathcal{H} \mathcal{M}_{q}^{g}$ from the $2 K-1 \mathcal{A}_{q}$;
4: while $\left|\mathcal{P}^{g+1}\right| \leq m$ do
5: $\quad$ rand $\leftarrow \operatorname{Rand}(0,1)$;
6: if rand $<$ rsp then
7: Select one NHM from multitasking NHMs randomly;
8: else
9: Select one NHM from single-tasking NHMs randomly;
10: $\quad$ Sample one solution $\Pi_{k}^{g+1}$ from the selected NHM and put the solution into $\mathcal{P}^{g+1}$;
11: $\quad \Pi_{k}^{g+1}$ inherts the skill factor based on the selected NHM;
12: Return offspring population $\mathcal{P}_{a}^{g+1}$;
![img-3.jpeg](img-3.jpeg)

Fig. 4. Decoding a permutation into a DAG.
$Q o S_{S_{1}}\rangle, S_{2}=\left(\{c\},\{e\}, Q o S_{S_{2}}\right), S_{3}=\left(\{d\},\{f\}, Q o S_{S_{3}}\right), S_{4}=$ $\left(\{a\},\{h\}, Q o S_{S_{4}}\right.$ ), and $S_{5}=\left(\{c\},\{e, f\}, Q o S_{S_{5}}\right.$ ). The two special services Start $=(\emptyset,\{a, b\}, \emptyset)$ and End $=(\{e, f\}, \emptyset, \emptyset)$ are defined by a given composition task $T$. Fig. 4 illustrates an example of producing a DAG from decoding a given permutation $\{4,1,0,2,3,5\}$ and producing another permutation $[1$, $2,3,4,0,5]$.

In the example, we check the satisfaction on the inputs of services in the permutation from left to right. If any services can be immediately satisfied by the provided inputs of composition task $I_{T}$, we remove it from the permutation and add it to the DAG with a connection to Start. Afterward, we continue checking on services' inputs by using $I_{T}$ and outputs of the services, and add satisfied services to the DAG. We continue this process until we can add End to the graph. In the
last phase of the decoding process, some redundant services, such as 4 , whose outputs contribute nothing to End, will be removed. In addition, this DAG is encoded as a new permutation $[1,2,3,4,0,5]$ consisting of two parts: one part $[1,2$, $3]$ corresponds to a service discovered by the discussed sorted method on the DAG and another part $[4,0,5]$ corresponds to the remaining atomic services in $\mathcal{S R}$, but not in the DAG. Furthermore, we also permit the encoding $[1,2,3,0,4,5]$, as no information can be extracted from the DAG to determine the order of 0,4 , and 5 .

## C. NHMs Learning and Sampling

Considering $K$ composition tasks in PMFEA-EDA, we learn $2 K-1$ NHMs based on promising solutions for sampling new candidate solutions. Every entry of NMHs roughly counts the number of times that a service index appears in the position of the permutation over all promising solutions in the pool. Among the NHMs, there are $K$ single-tasking NHMs and $K-1$ multitasking NHMs. With respect to each NHM, a separate solution pool will be maintained by PMFEA-EDA to keep track of useful solutions for building the corresponding NHM. For example, considering the example of the four composition tasks discussed in Section III-B, i.e., $T_{1}, T_{2}, T_{3}$, and $T_{4}$, seven pools must be initialized for the four composition tasks and three adjacent task pairs (i.e., $T_{1}$ and $T_{2}, T_{2}$ and $T_{3}$, and $T_{3}$ and $T_{4}$ ).

Moreover, a parameter rsp is used to determine whether multitasking or single-tasking NHMs are selected for sampling. Particularly, a value of rsp close to 0 implies that single-tasking NHMs are more frequently used to build new solutions, while a value close to 1 implies that multitasking NHMs are used with high probability to build new solutions for two adjacent tasks.

The outline of multiple NHMs learning and sampling over $K$ tasks is summarized in Algorithm 2. We first initialize a set of empty solution pools $\mathcal{A}_{q}$, where $1 \leq q \leq(2 K-1)$. Afterward, we assign these encoded solutions to these pools based on the solutions' skill factors $\tau^{\Pi_{k}^{g}}$. For example, if $\tau^{\Pi_{k}^{g}}=1$, this solution $\Pi_{k}^{\gamma g}$ is assigned to two pools, one for task $T_{1}$, and the other is for both tasks $T_{1}$ and $T_{2}$. Afterward, we learn $2 K-1$ NHMs from the $2 K-1$ pools, respectively (see details in Section IV-D). The iteration part comprises lines 5-12. This iteration will not stop until $m$ new solutions are constructed to form the offspring population $\mathcal{P}_{a}^{g+1}$. During the iteration, rsp is used to determine whether one NHM is randomly selected from the $2 K-1$ single-tasking NHMs or multitasking NHMs. The selected NHM is used to build one solution. Hence, the skill factor of the newly created solution will also be determined by the associated tasks with the chosen NHM, inspired by the principle of vertical culture transmission [27]. After all iterations have been completed, Algorithm 2 returns the newly produced population $\mathcal{P}_{a}^{g+1}$ required in line 6 of Algorithm 1.

## D. Application of Node Histogram-Based Sampling

We employ node histogram-based sampling [58] as a tool to create new permutations from the selected NHMs in step 7 or 9 in Algorithm 2. NHBSA can effectively sample new and

good candidate composite services from every node histogram matrix learned in each generation. This is because the learned node histogram can capture the explicit knowledge of a set of promising composite services in every generation with respect to each task and every adjacent task.

An NHM learned from solutions in each pool $\mathcal{A}_{q}$ at generation $g$, denoted by $\mathcal{N} \mathcal{H} \mathcal{M}_{q}^{g}$, is an $n \times n$-matrix with entries $e_{i, r}^{g}$ as follows:

$$
\begin{aligned}
e_{i, r}^{g} & =\sum_{k=0}^{m-1} \delta_{i, r}\left(\Pi_{k}^{r g}\right)+\varepsilon \\
\delta_{i, r}\left(\Pi_{k}^{r g}\right) & = \begin{cases}1, & \text { if } \pi_{i}=\mathrm{r} \\
0, & \text { otherwise }\end{cases}
\end{aligned}
$$

where $i, r=0,1, \ldots, n-1, \varepsilon=[m /(n-1)] b_{\text {ratio }}$ is a predetermined bias, and $n=|\mathcal{S R}|$. Roughly speaking, entry $e_{i, r}^{g}$ counts the number of times that service index $\pi_{i}$ appears in position $r$ of the permutation over all solutions in pool $\mathcal{A}_{q}$.

Example 2: Let us consider a pool $\mathcal{A}_{q}$ at generation $g$. This pool is assigned with $m$ permutations. For $m=6$, an example of $\mathcal{A}_{q}^{g}$ may look as follows:

$$
\mathcal{A}_{q}^{g}=\left[\begin{array}{c}
\Pi_{0}^{g} \\
\Pi_{1}^{g} \\
\Pi_{2}^{g} \\
\Pi_{3}^{g} \\
\Pi_{5}^{g}
\end{array}\right]=\left[\begin{array}{llllllll}
1 & 2 & 3 & 4 & 0 & 5 \\
0 & 1 & 2 & 3 & 4 & 5 \\
0 & 1 & 2 & 3 & 4 & 5 \\
4 & 3 & 0 & 1 & 2 & 5 \\
4 & 3 & 0 & 1 & 2 & 5 \\
2 & 1 & 3 & 0 & 4 & 5
\end{array}\right]
$$

Consider $b_{\text {ratio }}=0.2, m=6$, and $n=6$, then $\varepsilon=0.24$. Thus, we can calculate $\mathcal{N} \mathcal{H} \mathcal{M}_{q}^{g}$ as follows:

$$
\mathcal{N} \mathcal{H} \mathcal{M}_{q}^{g}=\left[\begin{array}{cccccc}
2.24 & 1.24 & 1.24 & 0.24 & 2.24 & 0.24 \\
0.24 & 3.24 & 1.24 & 2.24 & 0.24 & 0.24 \\
2.24 & 0.24 & 2.24 & 2.24 & 0.24 & 0.24 \\
2.24 & 2.24 & 0.24 & 2.24 & 0.24 & 0.24 \\
0.24 & 0.24 & 2.24 & 0.24 & 4.24 & 6.24
\end{array}\right]
$$

We use one entry $e_{0,0}^{g}=2.24$ as an example to explain the meaning behind this value. The integer part 2 states that service $S_{0}$ appears twice in the first position over all the permutations in $\mathcal{A}_{q}^{g}$. The decimal part $0.24=6 * 0.2 /(6-1)$ is the bias $\varepsilon$.

Once we have computed $\mathcal{N} \mathcal{H} \mathcal{M}_{q}^{g}$, we use NHBSA [58] to sample new candidate solutions $\Pi_{k}^{g+1}$ for the population $\mathcal{P}_{0}^{g+1}$ (see Algorithm 5 in Appendix C for technical details). Afterward, the same decoding part discussed in Section IV-B will be employed on each newly sampled permutation to ensure its functional validity in its corresponding DAG form.

## E. Fitness Evaluations for K Tasks

It is essential to include infeasible individuals (i.e., composite solutions that violate interval of task $T_{j}$ ) into each population since infeasible composite solutions may help to find optimal solutions of other tasks. For example, we take an arbitrary example of a composite service whose QoSM equals 0.3. Based on the segment preferences in Fig. 2, this composite service is only feasible for just one task (i.e., $T_{2}$ ), since it complies with interval ${ }_{2}$. However, this solution is infeasible
for the other tasks (i.e., $T_{1}, T_{3}$, and $T_{4}$ ) as it violates interval ${ }_{1}$, interval $_{3}$, and interval ${ }_{4}$, respectively. We allow infeasible individuals in the population, but their fitness (i.e., factorial cost in a multitasking context) must be penalized for tasks $T_{1}, T_{3}$, and $T_{4}$ (see details in (9)). According to the fitness function in (9) with respect to $T_{j}$, we guarantee that $f_{j}^{\Pi}$ of an infeasible individual falls below 0.5 while $f_{j}^{\Pi}$ of a feasible individual stays above 0.5 . Equation (11) quantifies the violation of interval $_{j}$ by measuring how far it is from $\operatorname{QoSM}(\Pi)$ in (10). In particular, an infeasible individual that violates interval $j_{j}$ more should be penalized more

$$
f_{j}^{\Pi}= \begin{cases}0.5+0.5 * F(\Pi), & \text { if } \mathrm{QoSM}(\Pi) \in \text { interval }_{j} \\ 0.5 * F(\Pi)-0.5 * V_{j}(\Pi), & \text { otherwise }\end{cases}
$$

$$
\begin{aligned}
& \operatorname{QoSM}(\Pi)=w_{7} \mathrm{MT}+w_{8} \mathrm{SIM} \\
& V_{j}(\Pi)= \begin{cases}\mathrm{QoSM}_{j}^{a}-\mathrm{QoSM}(\Pi), & \text { if } \mathrm{QoSM}(\Pi) \leq \mathrm{QoSM}_{j}^{a} \\
\mathrm{QoSM}(\Pi)-\mathrm{QoSM}_{j}^{b}, & \text { otherwise }\end{cases}
\end{aligned}
$$

with $\sum_{k=7}^{8} w_{k}=1$. We can adjust the weights according to the preferences of user segments. MT and SIM are normalized values calculated within the range from 0 to 1 using (6).

To find the $K$ best solutions with one for each task, the goal of multitasking semantic Web service composition is to maximize the objective function in (9) concerning the $K$ tasks.

## V. EXPERIMENTAL EVALUATION

To demonstrate the effectiveness and efficiency of our PMFEA-EDA, we conduct experiments to compare it against four recent works: one evolutionary multitasking approach developed in [26]; two works [16], [20] that employed ECbased single-tasking techniques; one recent non-EC work [43] based on a graph traversal technique. Moreover, we also study the effectiveness of knowledge sharing across adjacent tasks in PMFEA-EDA to understand its impact on the quality of obtained solutions for all the tasks. This is achieved by experimentally comparing PMFEA-EDA without knowledge sharing (named PMFEA-EDA-WOT) with PMFEA-EDA.

We employ a quantitative evaluation approach for studying the effectiveness and efficiency of PMFEA-EDA ${ }^{1}$ with augmented benchmark datasets ${ }^{2}$ (i.e., WSC08-1 to WSC08-8 and WSC09-1 to WSC09-5 with increasing service repository $\mathcal{S R}$ ) used by the very recent studies [20], [26], [43], [59]. The benchmark datasets originally come from WSC 08 [60] and WSC09 [61] and were extended with real QoS attributes in QWS [62]. In WSC08 and WSC09, the semantics of service inputs and outputs are described by the OWL-S language. This language allows a high degree of automation in discovering, invoking, composing, and monitoring Web resources. Other Web service description languages, such as WSDL, RSDL, and OpenAI, can be transformed into OWL-S [63]-[65]. In other words, these different description languages can be supported by our algorithm technically.

[^0]
[^0]:    ${ }^{1}$ The code of PMFEA-EDA for automated Web service composition is available from https://github.com/chenwangnida/PMFEA-EDA-Code.
    ${ }^{2}$ The two augmented benchmarks for automated Web service composition are available from https://github.com/chenwangnida/Dataset.

TABLE II
MeAn Fitness Values of Solutions per Task for Our Approaches in Comparison to PMFEA [26], EDA [20], FL [16], and PathSearch [43] for WSC08 (Note: the Higher the Fitness the Better)

Wang et al. [26] defined four composition tasks for each dataset, which has identical $t_{T}$ and $O_{T}$ but four different QoSM preferences introduced at the beginning of Section III-B. We evaluate three multitasking methods: PMFEA-EDA, PMFEAWTO, and PMFEA [26], and three single-tasking methods: EDA [20], FL [16], and PathSearch [43] (see the comparison results in Sections V-A and V-B). In particular, the three multitasking methods are utilized to optimize the four composition tasks concurrently, while the three single-tasking methods are utilized to optimize each task one by one, and the execution time is the aggregation of time spent on all tasks. We run 30 times of each EC-based method independently for all the datasets while we run 1 time of the deterministic non-EC method, i.e., PathSearch [43].
To make fair comparisons over all the methods, we use the same number of evaluations in PMFEA-EDA, PMFEA-WTO, PMFEA [26], EDA [20], and FL [16] for each run, i.e., the population size is 30 with 200 generations. We define rsp as 0.2 so that every single-tasking NHM and every multitasking NHM are expected to create 6 and 2 solutions, respectively, for the population size of 30 . Therefore, each task has roughly the same number of solutions from the sampling. $b_{\text {total }}$ is 0.0002 according to EDA [20]. Other parameters of PMFEA [26], EDA [20], FL [16], and PathSearch [43] follow the common
settings reported in the literature. For PathSearch [43], the parameter $k$ (i.e., the number of services considered in the path construction at each step) associated with this algorithm is set to 7 , which reported the highest quality in their paper. All the weights in (5) and (10) follow PMFEA [26]: $w_{1}$ and $w_{2}$ are set equally to 0.25 , and $w_{3}, w_{4}, w_{5}$, and $w_{6}$ are all set to 0.125 , these weights are set to properly balance QoSM and QoS; $w_{7}$ and $w_{8}$ are set to 0.5 , these weights are set to balance all quality criteria in QoSM. In general, weight settings are decided to reflect user segments' preferences. We have conducted tests with other weights and observed similar results to those reported below.

All the methods are run on a grid engine system (i.e., N1 Grid Engine 6.1 software) that performs tasks via a collection of computing resources, i.e., Linux PCs and each PC with an Intel Core i7-4770 CPU ( 3.4 GHz ) and 8-GB RAM. This hardware configuration is used for all the methods compared in this article.

## A. Comparison of the Fitness

Wilcoxon rank-sum test is employed at a significance level of $5 \%$ to verify the observed differences in fitness values. Particularly, pairwise comparisons of all the competing methods are carried out to count the number of times they are found

TABLE III
Mean Fitness Values of Solutions per Task for Our Approaches in Comparison to PMFEA [26], EDA [20], FL [16], and PathSearch [43] for WSC09 (Note: the Higher the Fitness the Better)

TABLE IV
Mean Execution Time (in Seconds) Over All the Tasks for Our Approaches in Comparison to PMFEA [26], EDA [20], FL [16], and PathSEARCH [43] for WSC08 (Note: the Shorter the Time the Better)

to be better, similar, or worse than the others. Consequently, we can rank all the competing methods and highlight the top performance in green color.

Tables II and III show the mean value of the solution fitness and the standard deviation over 30 repetitions for each task solved by PMFEA-EDA, PMFEA-EDA-WOT, PMFEA, EDA, and FL, and deterministic fitness value over one run for each task solved by PathSearch. We observe that the quality (i.e., QoSM and QoS) of solutions produced by using our PMFEA-EDA and EDA [20] is generally higher than those obtained by PMFEA and FL [16]. This corresponds well with our expectation that learning the knowledge of promising solutions explicitly can effectively improve the quality of composite services.

Furthermore, PMFEA-EDA performs better than singletasking EDA [20]. This observation indicates that addressing multiple tasks collectively is often more effective than addressing each task individually, through the use of NHM. Particularly, compared to single-tasking EDA, multitasking methods are more likely to evolve a well-diversified population of solutions. Consequently, we can easily prevent the evolutionary process from converging prematurely.

In addition, PMFEA-EDA also outperforms PMFEA-EDAWTO significantly and is labeled as top performance. This corresponds well with our expectation that explicit knowledge sharing through multitasking NHMs can significantly improve its ability in finding high-quality solutions.

Finally, PathSearch [43] achieves the worst performance in finding high-quality solutions, despite 5 out of 52 composition tasks are marked in green. It is due to that PathSearch [43] was designed to make the locally best choice over the $k$ services at each step and gradually build a path-based composite solution.

## B. Comparison of the Execution Time

Wilcoxon rank-sum test at a significance level of $5 \%$ is also employed to verify the observed differences in values of execution time (in seconds). Tables IV and V show the mean value of the execution time and the standard deviation over 30 repetitions for all tasks solved by PMFEA-EDA, PMFEAEDA-WOT, PMFEA, EDA, and FL, and the value of execution time over 1 run for all tasks solved by PathSearch.

TABLE V
Mean Execution Time (in Seconds) Over All the Tasks for Our Approaches in Comparison to PMFEA [26], EDA [20], FL [16], and PathSearch [43] for WSC09 (Note: the Shorter the Time the Better)


![img-4.jpeg](img-4.jpeg)

Fig. 5. Mean fitness over generations for tasks 1-4, for WSC08-8 and WSC09-2 (Note: the larger the fitness the better). (a) WSC08-8 Task 1. (b) WSC08-8 Task 2. (c) WSC08-8 Task 3. (d) WSC08-8 Task 4. (e) WSC09-2 Task 1. (f) WSC09-2 Task 2. (g) WSC09-2 Task 3. (h) WSC09-2 Task 4.

First, PathSearch [43] requires the least execution time. This is because PathSearch [43] only searches the constructed path based on the $k$ best services from a prestored service dependency graph. However, efficiency is not the focus of this article because finding high-quality composite services at the design stage is our focus.

Apart from PathSearch [43], PMFEA-EDA, PMFEA-EDAWTO, and PMFEA appear to be more efficient than EDA [20] and FL [16]. Although the same number of evaluations is assigned for each run of every method, EDA [20] and FL [16] are single-tasking methods that have to solve each composition task one by one.

Finally, PMFEA-EDA-WTO requires slightly less execution time for all the tasks since PMFEA-EDA demands more time for learning NHMs when service repository $\mathcal{S} \mathcal{R}$ becomes larger and larger. However, the extra time incurred in PMFEA-EDA is not substantial compared to other multitasking methods.

## C. Comparison of the Convergence Rate

We also study the convergence rate of PMFEA-EDA, PMFEA-EDA-WTO, PMFEA, EDA [20], and FL [16]. Using WSC08 and WSC09-2 as two examples, we show the behaviors of the effectiveness of all the methods in Fig. 5.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Population diversity measured by standard deviation over generations. (a) WSC08-8. (b) WSC09-2.

Fig. 5 shows the evolution of the mean fitness value of the best solutions found so far along 200 generations for all the approaches. We can see that PMFEA-EDA converges much faster than all the other methods in all the tasks (except task 1 on WSC 08-08). Besides that, PMFEA-EDA converges faster than PMFEA-EDA-WTO, and eventually reaches the highest plateau. This observation matches well with our expectation that knowledge sharing across tasks is very effective.

## D. Comparison of the Population Diversity

To explore the effectiveness of our proposed sampling strategy from multitasking NHMs with knowledge sharing, we investigated the diversity of the sampled population using 30 independent runs. We have used WSC08-8 and WSC09-2 as examples to illustrate the population diversity of the two methods, i.e., PMFEA-EDA and PMFEA-EDA-WTO. To examine the population diversity of these two methods over WSC08-8 and WSC09-2, we run 500 generations, instead of 200 generations, for WSC08-8 because the size of the service repository in WSC08-8 (i.e., 16238) is much bigger (with larger searching space) than that of WSC09-2 (i.e., 8258). Fig. 6 shows the population diversity, measured by the standard deviation of fitness values in (5) across 500 and 200 generations for WSC08-8 and WSC09-2, respectively.

In Fig. 6(a) and (b), PMFEA-EDA focuses more on exploration than PMFEA-EDA-WOT at the beginning of the evolutionary process, with the standard deviation of fitness values reaching its peak at generation 120 and 50 for WSC08-8 and WSC09-2, respectively. Starting from generation 350 and 100 for WSC08-8 and WSC09-2, respectively, PMFEA-EDA focuses comparatively more on exploitation than PMFEA-EDA-WOT, and the corresponding fitness standard deviation continues to decrease to a low level. This observation matches
![img-6.jpeg](img-6.jpeg)

Fig. 7. Mean fitness values of PMFEA-EDA with different $b_{\text {ratio }}$ over four tasks in WSC08-8.
well with our expectation that more exploration is performed in the beginning, and more exploitation happens in later phases of the evolution. On the other hand, PMFEA-EDA-WOT performs exploitation all the time as the standard deviation of fitness values stays at roughly the same levels.

## E. Sensitivity Analysis of the Model Parameter

In the literature, $b_{\text {ratio }}$ was set to 0.0002 in the single-tasking context [20], [58]. To study its sensitivity in a multitasking context, we study the performance of PMFEA-EDA with varying values of $b_{\text {ratio }}$. Particularly, we use WSC08-8 as an example to test the sensitivity of $b_{\text {ratio }}$ under a wide range of settings, i.e., $0.2,0.02,0.002$, and 0.0002 .

Fig. 7 shows the mean fitness values of the best solutions found after 200 generations for tasks $T_{1}, T_{2}, T_{3}$, and $T_{4}$ with respect to four different $b_{\text {ratio }}$ values over 30 runs. As shown in Fig. 7, we observed no significant differences in the mean fitness values for different values of $b_{\text {ratio }}$ in each task. This finding indicates that the performance of PMFEA-EDA is not sensitive to the settings of $b_{\text {ratio }}$.

## VI. CONCLUSION

In this article, we introduced a new PMFEA-EDA to solve service composition tasks from multiple user segments with different QoSM preferences in the context of fully automated Web service composition. In particular, single-tasking and multitasking NHMs are constructed to learn explicit knowledge of promising solutions for each task and every two adjacent tasks, respectively. This explicit learning mechanism is expected to perform knowledge learning and sharing better with an aim to find high-quality composite services for multiple tasks simultaneously. In addition, we also allow explicit knowledge to be effectively shared across every two adjacent tasks through the use of multitasking NHMs.

Furthermore, a sampling mechanism is proposed to balance the exploration and exploitation of the evolutionary search process for multiple tasks. Our experimental evaluations show that our proposed method outperforms two state-of-the-art singletasking and one recent multitasking EC-based approaches for finding high-quality solutions. Besides that, the execution time of our approach is comparable to the recent multitasking approach and outperforms two state-of-the-art single-tasking EC approaches by saving a large fraction of time. Future work can investigate the adaptions of NMHs for handling a dynamically updated service repository in an online fashion and study our EDA-based multitasking techniques to handle the dynamic and multitasking semantic Web service composition problem.
